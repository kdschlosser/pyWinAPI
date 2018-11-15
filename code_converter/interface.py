# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2016 EventGhost Project <http://www.eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function, absolute_import
from code_converter.utils import process_param, split_strip
from code_converter.comment import parse_comment, equalize_width

CLS_TEMPLATE = '''
class {cls_name}({parent_cls}):
    _case_insensitive_ = True
    _iid_ = {iid_name}
    _idlflags_ = [{idl_flags}]
'''


CLS_TEMPLATE_EXTENSION = '''    _methods_ = [
{methods}
    ]'''


METHOD_PARAM_EXTENSION = ''',
{method_params}
        ),'''


METHOD_EXTENSION = '''
        ),'''


GUID_TEMPLATE = '''{iid_name} = IID(
    '{iid}'
)

'''


LIBRARY_TEMPLATE = '''class {library_name}(object):
    name = '{library_name}'
    _reg_typelib_ = ({iid_name}, {version}, 0)


'''


CO_CLASS_TEMPLATE = '''class {co_class_name}(comtypes.CoClass):
    _reg_clsid_ = {co_clsid_name}
    _idlflags_ = []
    _reg_typelib_ = ({iid_name}, {version}, 0)
    _com_interfaces_ = [
{com_interfaces}
    ]


'''

TEMPLATE_METHOD = '''{indent}{comment}
{indent}    COMMETHOD(
{indent}        {method_options},
{indent}        {method_data_type},
{indent}        '{method_name}',{params}
{indent}    ),
'''

TEMPLATE_INTERFACE = '''{indent}{iid_name} = {iid}
{indent}
{indent}
{indent}class {cls_name}({parent_cls}):{helpstring}
{indent}    _case_insensitive_ = True
{indent}    _idlflags_ = {idl_flags}
{indent}    _iid_ = {iid_name}
'''

TEMPLATE_COCLASS = '''{indent}{iid_name} = {iid}
{indent}
{indent}
{indent}class {cls_name}(comtypes.CoClass):{helpstring}
{indent}    _case_insensitive_ = True
{indent}    _idlflags_ = {idl_flags}
{indent}    _reg_clsid_ = {iid_name}
{indent}    _reg_typelib_ = {reg_typelib}
{indent}    _com_interfaces_ = {com_interfaces}
'''

TEMPLATE_LIBRARY = '''{indent}{iid_name} = {iid}
{indent}
{indent}
{indent}class {cls_name}(object):{helpstring}
{indent}    _case_insensitive_ = True
{indent}    _reg_typelib_ = {reg_typelib}
{indent}    name = '{cls_name}'
'''


TEMPLATE_METHODS = '''{indent}{cls_name}._methods_ = [
{methods}{indent}]
'''


TEMPLATE_PARAM1 = '''
{indent}        ({param_direction}, {param_data_type}, '{param_name}'),'''

TEMPLATE_PARAM2 = '''
{indent}        (
{indent}            {param_direction},
{indent}            {param_data_type},
{indent}           '{param_name}'
{indent}        ),'''

TEMPLATE_HELPSTRING = '''\n{indent}    """{indent}\n    {helpstring}\n{indent}    """'''


interface_declarations = []


class Options(dict):

    def __init__(self, options):
        dict.__init__(self)
        self.options = options.replace('in,', '"in",').replace('in]', '"in"]')
        for item in ('length_is', 'size_is'):
            if item in self.options:
                new_options = ''
                while item + '(' in self.options:

                    pattern = self.options[:self.options.find(item + '(') + len(item) + 1]
                    new_options += pattern
                    self.options = self.options.replace(pattern, '', 1)
                    brace_count = 1
                    for i, char in enumerate(list(self.options)):
                        if char == ')':
                            brace_count -= 1
                        if char == '(':
                            brace_count += 1
                        if brace_count == 0:
                            break
                    else:
                        continue

                    self.options = self.options[i + 1:]
                    new_options += ')'

                self.options = new_options + self.options
        self.found_options = []

    def helpstring(self, value):
        return 'comtypes.helpstring({0})'.format(repr(value))

    def id(self, value):
        return 'comtypes.dispid({0})'.format(repr(value))

    def annotation(self, value):
        values = []

        def check_options(itm):
            if itm + ',' not in self.options and itm + ']' not in self.options:
                values.append(itm)

        if '_Inout' in value:
            check_options('in')
            check_options('out')

        elif '_Out' in value:
            check_options('out')

        elif '_In' in value:
            check_options('in')

        if '_Ret' in value:
            values += ['retval']

        if '_opt_' in values:
            if 'defaultvalue(' not in self.options:
                values += ['defaultvalue(None)']

        values += ['annotation({0}),'.format(repr(value))]
        return values
        # return values

    def defaultvalue(self, value):
        return 'defaultvalue({0})'.format(repr(value))

    def size_is(self):
        return 'size_is'

    def length_is(self):
        return 'length_is'

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

        if hasattr(self, item):
            return getattr(self, item)

        class Wrapper:
            def __call__(self, _):
                return ''

            def __str__(self):
                if item == 'string':
                    return ''

                return repr(item)

            def __repr__(self):
                if item == 'string':
                    return ''
                return repr(item)


        return Wrapper()

    def __str__(self):
        exec('found_options = ' + self.options + '\n', self)
        found_options = []
        for item in self.found_options:
            if isinstance(item, list):
                found_options += item
            else:
                found_options += [item]

        options = dict(
            list((item, 1) for item in found_options)
        )

        size_is = options.pop('size_is', 0)
        length_is = options.pop('length_is', 0)

        options = options.keys()[:]

        if size_is and length_is:
            if "in" not in options:
                options += ["in"]

            if "out" not in options:
                options += ["out"]

        res = repr(list(item for item in options if item))\

        res = res.replace('"a', 'a').replace(',"', '')
        res = res.replace(")'", ')').replace(')"', ')')
        res = res.replace("'comtypes", 'comtypes')
        res = res.replace('"comtypes', 'comtypes')
        res = res.replace(',,', ',')
        res = res.replace('[, ', '[')

        for itm in ('in', 'out', 'retval'):
            while res.count("'{0}'".format(itm)):
                if (
                    res.count("'{0}',".format(itm)) == 1 and
                    res.count("'{0}']".format(itm)) == 0
                ):
                    break
                elif res.count("'{0}',".format(itm)) > 1:
                    res = res.replace("'{0}',".format(itm), '', 1)
                else:
                    break

        return res


def get_help_string(indent, data):
    help_string = data.pop('helpstring')
    if help_string:
        help_string = TEMPLATE_HELPSTRING.format(
            indent=indent,
            helpstring=help_string
        )
    return help_string


def parse_keys(in_data):
    b_count = 0
    res = ''
    for char in list(in_data):
        if char == '[':
            b_count += 1
        elif char == ']':
            b_count -= 1

        res += char

        if b_count == 0:
            return res


def parse_options(line):
    options = parse_keys(line)
    return options, Options(options)


def parse_interface(indent, methods, importer, interface_data, dec):
    if 'declared' in interface_data and dec:
        dec = False

    if dec is True:
        help_string = get_help_string(indent, interface_data)
        interface_data['iid'] = interface_data['iid'].format(indent=indent)
        interface_data['declared'] = True

        if interface_data['co_class']:
            co_class = TEMPLATE_COCLASS.format(
                indent='',
                helpstring=help_string,
                **interface_data
            )
            interface_declarations.append(co_class)

        elif interface_data['library']:
            library = TEMPLATE_LIBRARY.format(
                indent='',
                helpstring=help_string,
                **interface_data
            )

            interface_declarations.append(library)
        else:
            interface = TEMPLATE_INTERFACE.format(
                indent='',
                helpstring=help_string,
                **interface_data
            )

            interface_declarations.append(interface)
        return

    if interface_data['co_class'] or interface_data['library']:
        return

    cls_name = interface_data['cls_name']

    chained_comment = False
    chained_method = False
    found_methods = []
    for line_num, method in enumerate(methods):

        if chained_method:
            if ';' in method:
                chained_method = False
            continue

        if chained_comment:
            if '*/' in method:
                chained_comment = False

            continue

        method, comment = parse_comment(method)

        if method is None and comment is None:
            comment = ''
            chained_comment = True
            for comnt in methods[line_num:]:
                comnt = comnt.strip()

                if (
                    not comnt.startswith('**/') and
                    not comnt.startswith('*/') and
                    comnt.startswith('*')
                ):
                    comnt = comnt[1:].strip()

                comment += ' ' + comnt
                if '*/' in comnt:
                    break
            method, new_comment = parse_comment(comment)

        if method and not method.endswith(';'):
            chained_method = True

            method = ''
            comment = ''
            for meth in methods[line_num:]:
                meth = meth.strip()
                meth, new_comment = parse_comment(meth)
                comment += ' ' + new_comment
                method += ' ' + meth

                if meth.endswith('\\'):
                    method = method[:-1]

                if ';' in meth:
                    break

        comment = equalize_width(indent + '    ', comment)

        if comment:
            if '\n' in comment:
                found_methods += ['\n']
                split_comment = comment.split('\n')
                for comnt in split_comment[:-1]:
                    found_methods += [comnt + '\n']

                found_methods += [split_comment[-1]]
            else:
                try:
                    if found_methods[-1].strip().endswith('\n'):
                        found_methods += [comment.rstrip() + '\n']
                    else:
                        found_methods += ['\n' + comment.rstrip()]
                except IndexError:
                    found_methods += [comment.rstrip() + '\n']

            comment = ''

        if not method:
            continue

        if method.strip().startswith('['):
            pattern, method_options = parse_options(method.strip())
            method = method.replace(pattern, '')
        else:
            method_options = Options('[]')

        try:
            method_name, temp_params = method.split('(', 1)
        except ValueError:
            continue

        method_name = method_name.strip()
        try:
            method_data_type, method_name = method_name.split(' ')
        except ValueError:
            continue

        method_name = method_name.strip()
        method_data_type = method_data_type.strip()
        temp_params = temp_params.strip()[:-2]

        found_params = []

        while temp_params:
            if temp_params.startswith('['):
                pattern, param_direction = parse_options(temp_params)
                temp_params = temp_params.replace(pattern, '')
            else:
                param_direction = Options('[]')

            if ',' in temp_params:
                param, temp_params = split_strip(temp_params, ',')
            else:
                param = temp_params
                temp_params = ''

            try:
                param_data_type, param_name = split_strip(param, ' ')
            except ValueError:
                continue

            param_name, param_data_type = process_param(
                param_name,
                param_data_type
            )
            template = TEMPLATE_PARAM1.format(
                indent=indent,
                param_direction=param_direction,
                param_data_type=param_data_type,
                param_name=param_name,
                comment=comment
            )
            if len(template) > 79:
                template = TEMPLATE_PARAM2.format(
                    indent=indent,
                    param_direction=param_direction,
                    param_data_type=param_data_type,
                    param_name=param_name,
                    comment=comment
                )

            found_params += [template]

        found_methods += [
            TEMPLATE_METHOD.format(
                indent=indent,
                method_options=method_options,
                method_data_type=method_data_type,
                method_name=method_name,
                params=''.join(found_params) if found_params else '',
                comment=comment
            )
        ]

    template = TEMPLATE_METHODS.format(
        indent=indent,
        cls_name=cls_name,
        methods=''.join(found_methods),
    )
    if not found_methods:
        template = template.split('[')[0]
        template += '[]\n\n'

    print(template)
