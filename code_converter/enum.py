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

from code_converter.comment import parse_comment, equalize_width

from code_converter.utils import OPERATORS, process_hex
from code_converter.preprocessor import parse_macro


CLASS_TEMPLATE = '''{indent}class {cls_name}(ENUM):{comment}'''
SUBCLASS_TEMPLATE = '''{indent}class {cls_name}(type_name):{comment}'''
SYMBOL_TEMPLATE = '''{indent}{symbol} = {value}'''
ENUM_TEMPLATE = '''{indent}    {enum_symbol} = {value}'''
MODULE_SYMBOL_TEMPLATE = '''{indent}{enum_symbol} = {cls_name}.{enum_symbol}'''

TEMPLATE_EXTENSION = '''{var_names}


'''

ENTRY_TEMPLATE = '''    {entry} = {value}'''
VAR_NAME_TEMPLATE = '''{var_name} = {value}'''



'''
            if line.startswith('typedef') or line.startswith('enum'):
                if 'enum' in line:
                    line = line.replace('_Enum_is_bitflag_', '')
                    start = i
                elif 'enum' in data[i + 1] and 'typedef' not in data[i + 1]:
                    start = i
'''


def parse_enum(indent, enum, namespace):
    cls_name = None
    module_level = None
    module_symbols = []
    chained_comment = False
    enum_namespace = {}
    global enum_count

    enum_count = 0
    symbols = None
    hold_over = None

    for i, line in enumerate(enum):
        if chained_comment:
            if '*/' in line:
                chained_comment = False

            continue

        line, comment = parse_comment(line)

        if line is None and comment is None:
            # /*
            # * Aliases for StringPrep
            # */
            comment = ''
            chained_comment = True
            for comnt in enum[i:]:
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
            # print([comment])
            line, new_comment = parse_comment(comment)

            if cls_name:
                comment = equalize_width(indent + '    ', new_comment)
            else:
                comment = equalize_width(indent, new_comment)

            if '\n' in comment:
                print('\n' + comment)
                comment = ''
                if not line:
                    continue

            if not line and comment:
                print('\n' + comment)
                continue

        line, indent = parse_macro(indent, line, namespace)

        if not line:
            continue

        if cls_name:
            comment = equalize_width(indent + '    ', comment)
        else:
            comment = equalize_width(indent, comment)

        if '\n' in comment:
            print('\n' + comment)
            comment = ''

        if not line and comment:
            print(comment)
            continue

        if not line:
            continue

        if comment:
            comment = ' ' + comment[comment.find('#'):]

        if symbols is not None:
            symbols += list(s.strip() for s in line.replace(';', '').split(','))

        elif line.startswith('typedef'):
            module_level = False

        elif line.startswith('enum'):
            module_level = True

        elif line.startswith('{'):
            _, line = line.split('{', 1)
            line = line.strip()
            if not line:
                continue

        elif line.strip() == '{':
            continue

        elif '}' in line:
            new_line, symbls = line.split('}', 1)

            symbols = list(
                s.strip() for s in symbls.replace(';', '').split(',')
            )

            line = new_line.strip()

            if not line:
                continue

        line = line.strip()

        def process_enum_symbol():
            global hold_over
            global comment
            global enum_count

            if '=' in line:
                enum_symbol, value = line.split('=', 1)
                if value.endswith('/'):
                    hold_over = [enum_symbol, comment, value[:-1]]
                    return None
            else:
                enum_symbol = line
                enum_count += 1
                value = str(enum_count)

            enum_symbol = enum_symbol.strip().rstrip(',').strip()
            value = value.strip().rstrip(',').strip()

            if '(' in value:
                values = list(v.strip() for v in value.split('('))
                new_values = []
                for value in values:
                    if not value:
                        continue
                    for op in OPERATORS:
                        if op in value:
                            break
                    else:
                        if value.endswith(')'):
                            new_values += [value[:-1]]
                            continue

                    new_values += ['(' + value]

            value = process_hex(value)

            if not value.isdigit():
                for op in OPERATORS:
                    value = (' ' + op + ' ').join(
                        v.strip() for v in value.split(op))

            try:
                exec('{0}={1}'.format(enum_symbol, value), enum_namespace)
                enum_count = enum_namespace[enum_symbol]
            except:
                try:
                    exec('{0}={1}'.format(enum_symbol, value), namespace)
                    enum_count = namespace[enum_symbol]
                except:
                    print(indent + '    #~#~#~ ' + line)
                    return None

            if cls_name:
                template = ENUM_TEMPLATE.format(
                    indent=indent,
                    enum_symbol=enum_symbol,
                    value=value
                )

            else:
                template = indent + enum_symbol + ' = ' + value

            if len(template) > 79:
                if '|' in value:
                    value = (
                        ('(\n        ' + indent) +
                        (' |\n        ' + indent).join(value.split(' | ')) +
                        '\n' + indent + '    )'
                    )
                else:
                    value = '(\n        ' + indent + value + '\n' + indent + '    )'

                if cls_name:
                    template = ENUM_TEMPLATE.format(
                        indent=indent,
                        enum_symbol=enum_symbol,
                        value=value
                    )
                    print(template)

                else:
                    template = indent + enum_symbol + ' = ' + value
            elif cls_name:
                print(template)

            if cls_name:
                return MODULE_SYMBOL_TEMPLATE.format(
                    indent=indent,
                    enum_symbol=enum_symbol,
                    cls_name=cls_name
                )
            else:
                return template

        if module_level is not None and cls_name is None:

            '''enum { U_PARSE_CONTEXT_LEN = 16 };'''

            '''typedef enum {'''
            module_level = 'typedef enum' not in line

            line = line.replace('typedef enum', '').replace('enum', '').strip()

            if ';' in line:
                try:
                    line, symbols = line.split('}')
                except:
                    type_name, cls_name = line.replace(';', '').split(' ', 1)
                    if type_name != cls_name:
                        print(
                            SUBCLASS_TEMPLATE.format(
                                indent=indent,
                                cls_name=cls_name,
                                type_name=type_name,
                                comment=comment
                            )
                        )
                        print(indent + '    pass')

                    break

                cls_name, enums = line.split('{')
                cls_name = cls_name.strip()

                symbols = symbols.replace(';', '').strip()
                if symbols:
                    symbols = list(s.strip() for s in symbols.split(','))
                else:
                    symbols = None

                if not cls_name and symbols is not None:
                    cls_name = symbols.pop(0)

                if cls_name:
                    print(
                        CLASS_TEMPLATE.format(
                            indent=indent,
                            cls_name=cls_name,
                            comment=comment
                        )
                    )
                else:
                    module_level = True

                enums = list(e.strip() for e in enums.split(','))
                for line in enums:
                    mod_template = process_enum_symbol()
                    if mod_template is not None:
                        module_symbols += [mod_template]
                continue

            line = line.replace('{', '')

            if line:
                cls_name = line
            else:
                temp_enum = ''.join(enum)
                cls_name = temp_enum.rsplit('}', 1)[1]
                cls_name = cls_name.split(',')[0]
                cls_name = cls_name.replace(';', '').strip()
                module_level = True

            cls_name = cls_name.strip()

            # if not cls_name:
            #     print('# ' + '# '.join(enum))
            #     return
            if cls_name:
                print(
                    CLASS_TEMPLATE.format(
                        indent=indent,
                        cls_name=cls_name,
                        comment=comment
                    )
                )
            else:
                module_level = True
            continue

        if hold_over is not None:
            hold_over[2] += ' ' + line.rstrip('/').strip()
            if comment:
                hold_over[1] += comment[2:]

            if line.endswith('/'):
                continue

            enum_symbol, comment, value = hold_over
            hold_over = None

            mod_template = process_enum_symbol()
            if mod_template is None:
                continue

            module_symbols += [mod_template]

        else:
            old_line = line

            for line in old_line.split(','):
                line = line.strip()

                if not line:
                    continue

                mod_template = process_enum_symbol()
                if mod_template is None:
                    continue

                module_symbols += [mod_template]
    else:
        if cls_name and not module_symbols:
            print(indent + '    pass')

        if symbols and cls_name:
            print('\n')

        elif cls_name and module_level and module_symbols:
            print('\n')

        if symbols is not None and cls_name:

            for symbol in symbols:
                if not symbol or symbol.strip() == cls_name.strip():
                    continue
                value = cls_name
                while symbol.startswith('*'):
                    symbol = symbol[1:].strip()
                    value = 'POINTER(' + value + ')'
                print(
                    SYMBOL_TEMPLATE.format(
                        indent=indent,
                        symbol=symbol,
                        value=value,
                    )
                )

        if module_level is True:
            for symbol in module_symbols:
                print(symbol)

    namespace.update(enum_namespace)
