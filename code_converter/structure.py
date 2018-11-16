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

from code_converter.utils import process_param, process_hex
from code_converter.comment import equalize_width, parse_comment
from code_converter.preprocessor import parse_macro


u_s_declarations = []


TEMPLATE_DECLARATION = '''{indent}class {cls_name}({parent_cls}):
{indent}    pass
'''

TEMPLATE_DECLARATION_FIELDS_START = '''{indent}{cls_name}._fields_ = ['''
TEMPLATE_DECLARATION_FIELDS_END = '''{indent}]'''
TEMPLATE_DECLARATION_FIELD = '''{indent}    ('{field_name}', {field_data_type}),{comment}'''
TEMPLATE_DECLARATION_FIELD_BIT = '''{indent}    ('{field_name}', {field_data_type}, {field_bit}),{comment}'''
TEMPLATE_DECLARATION_ANONYMOUS_START = '''{indent}{cls_name}._anonymous_ = ('''
TEMPLATE_DECLARATION_ANONYMOUS_END = '''{indent})'''
TEMPLATE_DECLARATION_ANONYMOUS = '''{indent}    '{anonymous}','''
TEMPLATE_DECLARATION_SUBSTRUCTURE = '''{indent}{cls_name}.{child_cls} = {child_cls}
'''


def parse_struct_union(
    indent,
    data,
    importer,
    struct_count,
    union_count,
    declarations,
    declare=False
):

    lines = data.split('\n')

    for i, line in enumerate(lines):
        if '_Struct_size_bytes_' in line:
            l1, l2 = line.split('_Struct_size_bytes_(', 1)
            l2 = l2.split(')', 1)[1]
            line = l1 + l2
            lines[i] = line

        if '_Union_size_bytes_' in line:
            l1, l2 = line.split('_Union_size_bytes_(', 1)
            l2 = l2.split(')', 1)[1]
            line = l1 + l2
            lines[i] = line

    if ':' in lines[0]:
        return struct_count, union_count

    if len(lines) == 1:
        lines = lines[0].split(' ')
        attr_name = lines[-1].replace(';', '').strip()
        value = lines[-2].strip()

        attr_name, value = process_param(attr_name, value)
        try:
            print(indent + attr_name + ' = ' + value + '\n')
        except TypeError:
            return struct_count, union_count
        return struct_count, union_count

    if 'struct' not in lines[0] or 'union' not in lines[0]:
        lines[0] += ' ' + lines.pop(1).lstrip()

    start_data = ''

    while '{' not in start_data:
        try:
            start_data += lines.pop(0)
        except IndexError:
            break

    try:
        start_data, extra = start_data.split('{', 1)
    except ValueError:
        extra = ''

    if extra.strip():
        lines.insert(0, extra)

    try:
        parent_cls, cls_name = start_data.rstrip().rsplit(' ', 1)
    except ValueError:
        return struct_count, union_count

    parent_cls = parent_cls.replace('typedef', '')
    cls_name = cls_name.replace('typedef', '')

    if 'struct' in parent_cls or 'struct' in cls_name:
        parent_cls = parent_cls.replace('struct', '').strip()
        cls_name = cls_name.replace('struct', '').strip()
        data_type = 'ctypes.Structure'
    else:
        parent_cls = parent_cls.replace('union', '').strip()
        cls_name = cls_name.replace('union', '').strip()
        data_type = 'ctypes.Union'

    if not parent_cls or 'DECLSPEC_ALIGN' in parent_cls:
        parent_cls = data_type

    cls_name = cls_name.replace('{', '').strip()
    if ';' in cls_name:
        cls_name = cls_name.replace(';', '')
        if parent_cls in ('ctypes.Structure', 'ctypes.Union'):
            if declare:
                u_s_declarations.append(
                    TEMPLATE_DECLARATION.format(
                        indent='',
                        cls_name=cls_name.strip(),
                        parent_cls=parent_cls
                    )
                )
            else:
                print(
                    TEMPLATE_DECLARATION.format(
                        indent=indent,
                        cls_name=cls_name.strip(),
                        parent_cls=parent_cls
                    )
                )
                print('\n')
            return struct_count, union_count
        else:
            if parent_cls == cls_name:
                return struct_count, union_count

            if '*' in cls_name or '*' in parent_cls:
                cls_name, parent_cls = process_param(cls_name, parent_cls)
                print(indent + cls_name + ' = ' + parent_cls)
            else:
                declarations += [cls_name.strip()]

                if declare:
                    u_s_declarations.append(
                        TEMPLATE_DECLARATION.format(
                            indent='',
                            cls_name=cls_name.strip(),
                            parent_cls=parent_cls
                        )
                    )
                else:
                    print(
                        TEMPLATE_DECLARATION.format(
                            indent=indent,
                            cls_name=cls_name.strip(),
                            parent_cls=parent_cls
                        )
                    )
                    print('\n')

            return struct_count, union_count
    try:
        var_names = data.rsplit('}', 1)[1].replace(';', '')
    except:
        var_names = data.replace(';', '')

    var_names = list(n.strip() for n in var_names.split(','))

    if not cls_name and var_names:
        cls_name = var_names.pop(0)

    elif not cls_name:
        print(indent + '#~#~#~', repr(data))
        return struct_count, union_count

    if cls_name in var_names:
        var_names.remove(cls_name)

    if cls_name not in declarations:
        declarations += [cls_name.strip()]

        if declare:
            u_s_declarations.append(
                TEMPLATE_DECLARATION.format(
                    indent='',
                    cls_name=cls_name.strip(),
                    parent_cls=parent_cls
                )
            )
        else:
            print(
                TEMPLATE_DECLARATION.format(
                    indent=indent,
                    cls_name=cls_name.strip(),
                    parent_cls=parent_cls
                )
            )
            print('\n')
    else:
        return struct_count, union_count

    anonymous = []
    fields = []
    sub_structure = []
    sub_structure_type = None
    brace_count = 0
    field = ''
    chained_comment = False
    field_comment = ''
    field_macro = ''

    data_fields = '~~~~'.join(lines)
    data_fields = data_fields[:data_fields.rfind('}')].split('~~~~')

    found_defines = []
    for line_num, line in enumerate(data_fields):

        if (
            line.strip().startswith('# define') or
            line.strip().startswith('#define')
        ):
            var_name, var_value = line.strip()[1:].replace('define', '', 1).strip().split(' ', 1)
            var_name = var_name.strip()
            var_value = var_value.strip()

            if var_value.startswith('('):
                var_value = var_value[1:].strip()

            def_template = '{0}{1} = {2}'.format(
                indent,
                var_name,
                var_value
            )

            if len(def_template) > 76:
                def_template = '{0}{1} = (\n{0}    {2}\n{0})'.format(
                    indent,
                    var_name,
                    var_value
                )

            found_defines += [def_template]
            continue

        if 'public' in line and '{' in line:
            return struct_count, union_count

        if ' ' not in line.strip():
            continue
        if chained_comment and '*/' not in line:
            continue

        chained_comment = False

        if sub_structure_type is None:
            line, comment = parse_comment(line)
        else:
            comment = ''

        if line is None and comment is None:
            comment = ''
            chained_comment = True
            for comnt in data_fields[line_num:]:
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

            line, comment = parse_comment(comment)
            field_comment = equalize_width(indent + '    ', comment)

            if not line:
                continue

        elif comment:
            field_comment = equalize_width(indent + '    ', comment)

        if sub_structure_type is None:
            import sys

            class STDOut(object):
                saved_data = ''
                stdout = sys.stdout

                def write(self, data):
                    STDOut.saved_data = data.rstrip()

                def __getattr__(self, item):
                    if item in self.__dict__:
                        return self.__dict__[item]
                    return getattr(STDOut.stdout, item)

            sys.stdout = STDOut()
            new_line, new_indent = parse_macro(indent, line.strip())
            sys.stdout = STDOut.stdout

            if new_line != line or new_indent != indent:
                field_macro = STDOut.saved_data
                line = new_line
                indent = new_indent
            else:
                field_macro = ''

        if not line:
            continue

        if line.startswith('#'):
            continue

        if '_Field_' in line:
            chunk_1, chunk_2 = line.split('_Field_', 1)
            chunk_2 = chunk_2.split('(', 1)[1]
            bad_chunk = ''
            brace_count = 1
            for char in list(chunk_2):
                brace_count += char.count('(')
                brace_count -= char.count(')')
                bad_chunk += char
                if not brace_count:
                    break
            else:
                continue

            chunk_2 = chunk_2.replace(bad_chunk, '', 1)
            line = chunk_1 + chunk_2

            if not line.strip():
                continue

        if 'OPTIONAL' in line:
            line = line[:line.find('OPTIONAL') - 1].rstrip()

        if (
            (
                line.strip().startswith('union') or
                line.strip().startswith('struct')
            ) and
            line.strip().endswith(';')
        ):
            line = line.replace('struct', '').replace('union', '')
        if line.strip().startswith('union'):
            sub_structure_type = 'union'

        elif line.strip().startswith('struct'):
            sub_structure_type = 'struct'

        if sub_structure_type is not None:
            if not sub_structure and line.strip().endswith(';'):
                mult = None
                line = line.replace(sub_structure_type, '').strip()[:-1]
                try:
                    p_cls, c_name = line.split(' ')
                except ValueError:
                    c_name = line
                    if sub_structure_type == 'union':
                        p_cls = 'ctypes.Union'
                    else:
                        p_cls = 'ctypes.Structure'

                if '*' in c_name:
                    f_name, f_data_type = process_param(
                        c_name,
                        c_name.replace('*', '')
                    )

                else:
                    f_name = c_name
                    f_data_type = cls_name + '.' + f_name
                    print(
                        TEMPLATE_DECLARATION.format(
                            indent=indent,
                            cls_name=f_name,
                            parent_cls=p_cls
                        )
                    )
                    print('\n')
                    print(
                        TEMPLATE_DECLARATION_SUBSTRUCTURE.format(
                            indent=indent,
                            cls_name=cls_name,
                            child_cls=f_name
                        )
                    )

            else:
                sub_structure += [line]
                brace_count += line.count('{')
                brace_count -= line.count('}')
                if brace_count == 0 and line.rstrip().endswith(';'):
                    f_name = (
                        line.replace(';', '').replace('}', '').strip()
                    )
                    if not f_name:

                        if sub_structure_type == 'union':
                            sub_count = union_count = union_count + 1
                        else:
                            sub_count = struct_count = struct_count + 1

                        f_name = '_{0}_{1}'.format(
                            sub_structure_type.title(),
                            sub_count
                        )

                        line = line.replace(
                            ';',
                            f_name + ';'
                        )
                        sub_structure[len(sub_structure) - 1] = line
                        anonymous += [f_name]

                    if '[' in f_name:
                        tmp_field_name, mult = f_name.split('[', 1)
                        mult = mult.replace(']', '').strip()

                        for i, ln in enumerate(sub_structure):
                            sub_structure[i] = ln.replace(
                                f_name,
                                tmp_field_name
                            )
                        f_name = tmp_field_name

                    else:
                        mult = None

                        sub_structure[0] = (
                            '{0}typedef {1} '.format(
                                indent,
                                sub_structure_type
                            )
                        )

                    if not sub_structure[1].strip().startswith('{'):
                        sub_structure[0] += '{'

                    parse_struct_union(
                        indent,
                        '\n'.join(sub_structure),
                        importer,
                        struct_count,
                        union_count,
                        []
                    )

                    f_data_type = cls_name + '.' + f_name

                else:
                    continue

            sub_structure = []
            sub_structure_type = None

            print(
                TEMPLATE_DECLARATION_SUBSTRUCTURE.format(
                    indent=indent,
                    cls_name=cls_name,
                    child_cls=f_name
                )
            )

            if '\n' in field_comment:
                fields += [[None, '\n' + field_comment]]
                field_comment = ''

            elif field_comment:
                field_comment = ' ' + field_comment[field_comment.find('#'):]

            if mult:
                if ':' in f_name:
                    f_name,  f_bit = f_name.split(':')
                    f_name = f_name.strip()
                    f_bit = f_bit.strip()
                    template = TEMPLATE_DECLARATION_FIELD_BIT.format(
                        indent=indent,
                        field_name=f_name,
                        field_data_type=f_data_type + ' * ' + mult,
                        field_bit=f_bit,
                        comment=''
                    )

                else:
                    template = TEMPLATE_DECLARATION_FIELD.format(
                        indent=indent,
                        field_name=f_name,
                        field_data_type=f_data_type + ' * ' + mult,
                        comment=''
                    )

                if field_comment is not None and field_comment.strip():
                    field_comment = equalize_width(indent + '    ',
                        field_comment)
                    template = '\n\n' + field_comment + '\n' + template

                fields += [[field_macro, template]]
            else:
                if ':' in f_name:
                    f_name,  f_bit = f_name.split(':')
                    f_name = f_name.strip()
                    f_bit = f_bit.strip()
                    template = TEMPLATE_DECLARATION_FIELD_BIT.format(
                        indent=indent,
                        field_name=f_name,
                        field_data_type=f_data_type,
                        field_bit=f_bit,
                        comment=''
                    )

                else:
                    template = TEMPLATE_DECLARATION_FIELD.format(
                        indent=indent,
                        field_name=f_name,
                        field_data_type=f_data_type,
                        comment=''
                    )

                if field_comment is not None and field_comment.strip():
                    field_comment = equalize_width(indent + '    ', field_comment)
                    template = '\n\n' + field_comment + '\n' + template

                fields += [[field_macro, template]]

            field_macro = ''
            field_comment = ''
            continue

        elif field:
            line = line.strip()
            if line.endswith('\\'):
                line = line[:-1].strip()
            field += ' ' + line
            if not line.endswith(';'):
                continue

        elif line.rstrip().endswith(';'):
            field = line
        else:
            line = line.strip()
            if line.endswith('\\'):
                line = line[:-1].strip()

            field = line
            continue

        try:
            field_data_type, field_name = (
                field[:-1].replace(';', '').strip().split(' ', 1)
            )
        except ValueError:

            if '}' in field:
                continue

            import sys
            sys.stderr.write('******* ' + str(field) + '\n')
            raise

        if ',' in field_name:
            field_names = list(
                fn.strip() for fn in field_name.split(',')
            )
            count = []
        elif '[' in field_name:
            count = []
            while '[' in field_name:
                field_name, c = field_name.rsplit('[', 1)
                count.insert(0, c.replace(']', '').strip())
            field_names = [field_name]
        else:
            count = []
            field_names = [field_name.strip()]

        for i, field_name in enumerate(field_names):
            while ' ' in field_name:
                try:
                    field_data_type, field_name = (
                        field_data_type.split(' ', 1)
                    )
                except ValueError:
                    break
            field_names[i] = field_name.strip()

        field_data_type = field_data_type.strip()
        field_data_type = field_data_type.replace(
            'IUnknown',
            'comtypes.IUnknown'
        )

        field_data_types = []
        for i, field_name in enumerate(field_names):

            field_name, fd_type = process_param(
                field_name,
                field_data_type
            )

            field_data_types += [fd_type]
            field_names[i] = field_name

        for i, field_data_type in enumerate(field_data_types):
            fd_type = field_data_type
            for j, cnt in enumerate(count):
                if j == 1:
                    fd_type = '(' + fd_type + ')'
                if j:
                    fd_type += '({0} * {1})'.format(
                        field_data_type,
                        cnt
                    )
                else:
                    fd_type += ' * ' + cnt

            field_data_types[i] = fd_type

        for i, field_name in enumerate(field_names):

            if '\n' in field_comment:
                fields += [[None, '\n' + field_comment]]
                field_comment = ''

            elif field_comment:
                field_comment = ' ' + field_comment[field_comment.find('#'):]

            if field_name is None:
                continue

            if field_data_types[i] in ('_In_', '_Out_', 'IN', 'OUT', '_Inout_'):
                field_data_types[i], field_name = field_name.split(' ', 1)
                field_data_types[i] = field_data_types[i].strip()
                field_name = field_name.strip()

                field_name, field_data_types[i] = process_param(field_name, field_data_types[i])

            if ':' in field_name:
                field_name, field_bit = field_name.split(':')
                field_name = field_name.strip()
                field_bit = field_bit.strip()
                template = TEMPLATE_DECLARATION_FIELD_BIT.format(
                    indent=indent,
                    field_name=field_name,
                    field_data_type=field_data_types[i],
                    field_bit=field_bit,
                    comment=''
                )

            else:
                template = TEMPLATE_DECLARATION_FIELD.format(
                    indent=indent,
                    field_name=field_name,
                    field_data_type=field_data_types[i],
                    comment=''
                )

            if field_comment is not None and field_comment.strip():
                field_comment = equalize_width(indent + '    ', field_comment)
                template = '\n\n' + field_comment + '\n' + template

            fields += [[field_macro, template]]

        field_macro = ''
        field_comment = ''
        field = ''

    if not cls_name:
        return struct_count, union_count

    if anonymous:
        print(
            TEMPLATE_DECLARATION_ANONYMOUS_START.format(
                indent=indent,
                cls_name=cls_name
            )
        )

        for anon in anonymous:
            print(
                TEMPLATE_DECLARATION_ANONYMOUS.format(
                    indent=indent,
                    anonymous=anon
                )
            )
        print(
            TEMPLATE_DECLARATION_ANONYMOUS_END.format(
                indent=indent,
            )
        )

    print(('\n'.join(found_defines)))
    if found_defines:
        print()

    if fields:
        macro_indexes = []

        for j, items in enumerate(fields[:]):
            if items[0]:
                macro_indexes += [[j, items]]
                fields.remove(items)

        if macro_indexes:
            print(indent + '_temp_fields_ = (')

        else:
            print(
                TEMPLATE_DECLARATION_FIELDS_START.format(
                    indent=indent,
                    cls_name=cls_name
                )
            )
        last_field = ''
        for _, field in fields:
            if field.startswith('\n\n') and last_field.endswith('\n'):
                field = field[2:]

            last_field = field
            print(field)

        print(
            TEMPLATE_DECLARATION_FIELDS_END.format(
                indent=indent,
            )
        )

        if macro_indexes:
            for index, items in macro_indexes:
                macro, field = items
                macro = macro[4:]

                print(macro)
                print(
                    '{0}    _temp_fields_.insert({1}, {2})'.format(
                        indent,
                        index,
                        field.strip()[:-1]
                    )
                )
            print(
                '{0}{1}._fields_ = _temp_fields_'.format(indent, cls_name)
            )

    variables = []

    for var_name in var_names:
        if not var_name:
            continue

        var_name, value = process_param(
            var_name,
            cls_name
        )

        if var_name is None:
            continue

        if declare:
            variables += [var_name + ' = ' + value]

        else:
            variables += [indent + var_name + ' = ' + value]

    if variables:
        variables = '\n'.join(variables)
        if declare:
            u_s_declarations.append('\n' + variables + '\n')
        else:
            print(variables)

    return struct_count, union_count
