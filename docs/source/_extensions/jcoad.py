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
from sphinx.util import logging, docutils
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import make_id, make_refnode

logger = logging.getLogger(__name__)


class ParamDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 4
    final_argument_whitespace = True
    option_spec = {
        'type': directives.unchanged,
        'format': directives.unchanged,
        'default': directives.unchanged,
        'options': directives.unchanged,
    }

    def make_option_node(self, option: str, label: str) -> nodes.paragraph:
        if option in self.options and self.options[option]:
            option_node = nodes.paragraph()
            option_node['classes'] = ['option']
            option_node += nodes.strong('', label + ': ')
            option_node += nodes.Text(self.options[option])
            return option_node

    def run(self):
        if not self.arguments:
            raise self.error('Missing parameter name')

        name = self.arguments[0]

        param_node = nodes.container()
        param_node['classes'] = ['param']
        name_node = nodes.paragraph()
        name_node += nodes.strong('', name)
        if 'type' in self.options and self.options['type']:
            name_node += nodes.Text(' (')
            types = self.options['type'].split('|')
            type_role = self.env.get_domain('jcoad').role('type')

            put_separator = False
            for ref_type in types:
                if not put_separator:
                    put_separator = True
                else:
                    name_node += nodes.Text(' | ')

                if ref_type[0] == '"' and ref_type[-1] == '"':
                    name_node += docutils.roles.code_role('code', '', ref_type[1:-1], self.lineno, self.state.inliner)[0]
                else:
                    name_node += type_role('type', '', ref_type, self.lineno, self.state.inliner)[0]

            name_node += nodes.Text(')')
        param_node += name_node

        details_node = nodes.container()
        details_node['classes'] = ['details']
        self.state.nested_parse(self.content, self.content_offset, details_node)

        details_node += self.make_option_node('format', 'Format')
        details_node += self.make_option_node('options', 'Options')
        details_node += self.make_option_node('default', 'Default')

        param_node += details_node
        return [param_node]


class JCoadObject(ObjectDescription):
    # Prefix right before documentation entry
    display_prefix = None   # type: str
    display_code_block = True   # type: bool
    prefix_in_code_block = True # type: bool
    space_between_suffix = False    # type: bool

    option_spec = {
        'prefix': directives.unchanged,
        'suffix': directives.unchanged,
        'options': directives.unchanged,
        'examples': directives.unchanged,
        'noindex': directives.flag,
        'noindexentry': directives.flag,
    }

    def handle_signature(self, sig: str, signode: desc_signature) -> Tuple[str, str]:
        name = sig.strip()

        if self.display_prefix:
            signode += addnodes.desc_annotation('', self.display_prefix)

        signode += addnodes.desc_name(name, name)

        return name, self.display_prefix

    def add_target_and_index(self, name_prefix: Tuple[str, str], sig: str, signode: desc_signature) -> None:
        refname = self.objtype + '-' + name_prefix[0]
        node_id = make_id(self.env, self.state.document, '', sig)
        signode['ids'].append(node_id)

        self.state.document.note_explicit_target(signode)

        domain = self.env.get_domain('jcoad')
        domain.add_object(refname, self.objtype, node_id, location=signode)

        if 'noindexentry' not in self.options:
            indextext = self.get_index_text(name_prefix)
            if indextext:
                self.indexnode['entries'].append(('single', indextext, node_id, '', None))

    def get_index_text(self, name_prefix: Tuple[str, str]) -> str:
        name, prefix = name_prefix
        return _('%s%s (%s)') % (name, prefix, self.objtype) if self.objtype else ''

    def transform_content(self, contentnode: addnodes.desc_content) -> None:
        if 'options' in self.options:
            code_block_directive = CodeBlock(
                name='code-block',
                arguments=[],
                options={
                    'caption': 'Options',
                },
                content=[self.options['options']],
                lineno=self.lineno,
                content_offset=self.content_offset,
                block_text='',
                state=self.state,
                state_machine=self.state_machine
            )

            contentnode += code_block_directive.run()[0]

        if 'examples' in self.options:
            code_block_directive = CodeBlock(
                name='code-block',
                arguments=[],
                options={
                    'caption': 'Examples',
                },
                content=[self.options['examples'].replace('\n::\n', '\n\n')],
                lineno=self.lineno,
                content_offset=self.content_offset,
                block_text='',
                state=self.state,
                state_machine=self.state_machine
            )

            contentnode += code_block_directive.run()[0]

        if self.display_code_block:
            code_block_content = []
            for name_prefix in self.names:
                name, prefix = name_prefix
                line = name
                if 'suffix' in self.options:
                    if self.space_between_suffix:
                        line += ' '
                    line += self.options['suffix']
                if 'prefix' in self.options:
                    line = self.options['prefix'] + line
                if prefix and self.prefix_in_code_block:
                    line = prefix + line
                code_block_content.append(line)

            code_block_directive = CodeBlock(
                name='code-block',
                arguments=[],
                options={},
                content=code_block_content,
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
    display_prefix = 'name.'


class JCoadTrigger(JCoadObject):
    display_prefix = '&'


class JCoadCondition(JCoadObject):
    display_prefix = '(condition) '
    prefix_in_code_block = False


class JCoadType(JCoadObject):
    display_prefix = '(type) '
    display_code_block = False

class JCoadPokemonOption(JCoadObject):
    display_prefix = ''
    space_between_suffix = True

class JCoadBattleOption(JCoadObject):
    display_prefix = ''
    space_between_suffix = True

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


class JCoadDomain(Domain):
    name = 'jcoad'
    label = 'jCoad'

    object_types = {
        'function':     ObjType(_('function'), 'func'),
        'property':     ObjType(_('property'), 'prop'),
        'trigger':      ObjType(_('trigger'), 'trigger'),
        'condition':     ObjType(_('condition'), 'cond'),
        'type':         ObjType(_('type'), 'type'),
        'pokeoption':   ObjType(_('pokeoption'), 'pokeoption'),
        'battleoption': ObjType(_('battleoption'), 'battleoption'),
    }

    directives = {
        'function':     JCoadFunction,
        'trigger':      JCoadTrigger,
        'condition':    JCoadCondition,
        'property':     JCoadProperty,
        'type':         JCoadType,
        'pokeoption':   JCoadPokemonOption,
        'battleoption': JCoadBattleOption,
    }

    roles = {
        'func': JCoadFunctionXRefRole(),
        'prop': JCoadPropertyXRefRole(),
        'trigger': JCoadTriggerXRefRole(),
        'cond': XRefRole(),
        'type': XRefRole(),
        'pokeoption': XRefRole(),
        'battleoption': XRefRole(),
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
        return self.objects.get(objtype + '-' + name) if objtype is not None else None

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
    app.add_directive('param', ParamDirective)

    return {
        'version': 'builtin',
        'env_version': 2,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
