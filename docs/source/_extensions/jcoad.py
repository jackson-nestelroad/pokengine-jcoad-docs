from typing import Tuple, Dict, Any, Iterator

from docutils import nodes
from docutils.nodes import Element
from docutils.parsers.rst import directives
from sphinx import addnodes
from sphinx.addnodes import desc_signature, pending_xref
from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.directives import ObjectDescription
from sphinx.directives.code import CodeBlock
from sphinx.domains import Domain, ObjType
from sphinx.environment import BuildEnvironment
from sphinx.locale import _, __
from sphinx.roles import XRefRole
from sphinx.util import logging
from sphinx.util.nodes import make_id, make_refnode

logger = logging.getLogger(__name__)


class JCoadObject(ObjectDescription):
    # Prefix right before documentation entry
    prefix = None   # type: str

    option_spec = {
        'suffix': directives.unchanged,
        'noindex': directives.flag,
        'noindexentry': directives.flag,
    }

    def handle_signature(self, sig: str, signode: desc_signature) -> Tuple[str, str]:
        name = sig.strip()

        if self.prefix:
            signode += addnodes.desc_annotation(self.prefix, self.prefix)

        signode += addnodes.desc_name(name, name)

        return name, self.prefix

    def add_target_and_index(self, name_prefix: Tuple[str, str], sig: str, signode: desc_signature) -> None:
        fullname = self.objtype + '-' + name_prefix[0]
        node_id = make_id(self.env, self.state.document, '', sig)
        signode['ids'].append(node_id)

        self.state.document.note_explicit_target(signode)

        domain = self.env.get_domain('jcoad')
        print(fullname)
        domain.add_object(fullname, self.objtype, node_id, location=signode)

        if 'noindexentry' not in self.options:
            indextext = self.get_index_text(name_prefix)
            if indextext:
                self.indexnode['entries'].append(('single', indextext, node_id, '', None))

    def get_index_text(self, name_prefix: Tuple[str, str]) -> str:
        name, prefix = name_prefix
        return _('%s%s (%s)') % (name, prefix, self.objtype) if self.objtype else ''

    def transform_content(self, contentnode: addnodes.desc_content) -> None:
        name, prefix = self.names[0]

        code_block_content = name
        if 'suffix' in self.options:
            code_block_content += self.options['suffix']
        if prefix:
            code_block_content = prefix + code_block_content

        code_block_directive = CodeBlock(
            name='code-block',
            arguments=[],
            options={},
            content=[code_block_content],
            lineno=self.lineno,
            content_offset=self.content_offset,
            block_text='',
            state=self.state,
            state_machine=self.state_machine
        )

        contentnode.insert(0, code_block_directive.run()[0])


class JCoadFunction(JCoadObject):
    pass


class JCoadProperty(JCoadObject):
    prefix = 'name.'


class JCoadTrigger(JCoadObject):
    prefix = '&'


class JCoadVariable(JCoadObject):
    prefix = '(var) '


class JCoadFunctionXRefRole(XRefRole):
    def process_link(self, env: BuildEnvironment, refnode: Element,
                     has_explicit_title: bool, title: str, target: str) -> Tuple[str, str]:
        return title + '()', target


class JCoadPropertyXRefRole(XRefRole):
    def process_link(self, env: BuildEnvironment, refnode: Element,
                     has_explicit_title: bool, title: str, target: str) -> Tuple[str, str]:
        return 'name.' + title + '()', target


class JCoadTriggerXRefRole(XRefRole):
    def process_link(self, env: BuildEnvironment, refnode: Element,
                     has_explicit_title: bool, title: str, target: str) -> Tuple[str, str]:
        return '&' + title, target


class JCoadVariableXRefRole(XRefRole):
    def process_link(self, env: BuildEnvironment, refnode: Element,
                     has_explicit_title: bool, title: str, target: str) -> Tuple[str, str]:
        return title, target


class JCoadDomain(Domain):
    name = 'jcoad'
    label = 'jCoad'

    object_types = {
        'function':     ObjType(_('function'), 'func'),
        'property':     ObjType(_('property'), 'prop'),
        'trigger':      ObjType(_('trigger'), 'trigger'),
        'variable':     ObjType(_('variable'), 'var'),
    }

    directives = {
        'function':     JCoadFunction,
        'trigger':      JCoadTrigger,
        'variable':     JCoadVariable,
        'property':     JCoadProperty,
    }

    roles = {
        'func': JCoadFunctionXRefRole(),
        'prop': JCoadPropertyXRefRole(),
        'trigger': JCoadTriggerXRefRole(),
        'var': JCoadVariableXRefRole(),
    }

    initial_data = {
        'objects': {},  # refname -> docname, node_id, objtype
    }

    @property
    def objects(self) -> Dict[str, Tuple[str, str, str]]:
        return self.data.setdefault('objects', {})

    def add_object(self, refname: str, objtype: str, node_id: str, location: Any = None) -> None:
        if refname in self.objects:
            docname = self.objects[refname][0]
            logger.warning(__('duplicate description of %s, other %s in %s'),
                           refname, objtype, docname, location=location)
        self.objects[refname] = (self.env.docname, node_id, objtype)

    def get_objects(self) -> Iterator[Tuple[str, str, str, str, str, int]]:
        for refname, (docname, node_id, objtype) in list(self.objects.items()):
            yield refname, refname, objtype, docname, node_id, 1

    def find_obj(self, name: str, typ: str) -> Tuple[str, str, str]:
        objtype = next((x for x in self.object_types if self.object_types[x].roles[0] == typ), None)
        return self.objects.get(objtype + '-' + name)

    def resolve_xref(self, env: BuildEnvironment, fromdocname: str, builder: Builder,
                     typ: str, target: str, node: pending_xref, contnode: Element
                     ) -> Element:
        obj = self.find_obj(target, typ)
        if not obj:
            return None
        return make_refnode(builder, fromdocname, obj[0], obj[1], contnode, target)

    def clear_doc(self, docname: str) -> None:
        for name, (pkg_docname, node_id, _l) in list(self.objects.items()):
            if pkg_docname == docname:
                del self.objects[name]


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_domain(JCoadDomain)

    return {
        'version': 'builtin',
        'env_version': 2,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }