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

DEFINE_TEMPLATE = '{0}{1}{2}'


def parse_define(indent, define, importer):
    old_define = define
    global value
    if 'This' in define:
        return

    if 'GUID_BUILDER' in define:
        return

    if define.startswith('#define INTERFACE'):
        return

    define, comment = parse_comment(define)
    comment = equalize_width(indent, comment)

    if '\n' in comment:
        print('\n' + comment)
        comment = ''

    if define is None and comment is None:
        print(indent + '#~#~#~', old_define)
        return False

    define = define.replace('0X', '0x').replace('\t', '    ').replace('->', '.')

    try:
        var_name, value = define[1:].replace('define', '').strip().split(' ', 1)
    except ValueError:
        var_name = define[1:].replace('define', '').strip()
        value = '1'
        # print(indent + '#~#~#~', old_define)
        # return False

    var_name = var_name.strip()
    value = value.strip()

    if var_name == '#':
        try:
            var_name, value = value.split(' ', 1)

        except ValueError:
            print(indent + '#~#~#~', old_define)
            return False

    if '(' in var_name:
        brace_count = var_name.count('(')
        brace_count -= var_name.count(')')
        while brace_count > 0:
            var_name += value[:value.find(')') + 1]
            value = value[value.find(')') + 1:]
            brace_count = var_name.count('(')
            brace_count -= var_name.count(')')

        var_name = var_name.replace('=', '')

    var_name = var_name.strip()
    value = value.strip()

    if var_name == value:
        print(indent + '#~#~#~', old_define)
        return False

    if '0x' in var_name:
        var_name, new_value = var_name.split('0x', 1)
        value = '0x' + new_value + value
        var_name = var_name.strip()
        value = value.strip()

    value = process_hex(value)

    if value.count('"') == 1:
        if not value.endswith('"') or value == '"':
            value += '\\n"'

    def get_ret():
        global value
        if not value.strip():
            value = '1'

        if value.startswith('L"'):
            value = value[1:]

        if var_name.startswith('def '):
            ret = (
                '\n\n' + indent +
                var_name +
                indent + '    return ' +
                value
            )

        elif 'CTL_CODE' in value:
            value = value.replace('CTL_CODE', '')[:-1]
            value = (
                'CTL_CODE(\n' +
                '\n'.join(
                    indent + '    ' + val.strip() + ','
                    for val in value[1:].split(',')
                ) +
                '\n' + indent + ')'
            )
            ret = var_name + ' = ' + value

        elif value and var_name != value:
            value = value.replace('{', '[').replace('}', ']')
            ret = var_name + ' = ' + value

            if len(indent + ret) > 76:
                if (
                    ',' in ret and
                    (
                        ('(' in ret and ret.endswith(')')) or
                        ('[' in ret and ret.endswith(']'))
                    )
                ):

                    new_ret, ret = ret.split(' = ', 1)
                    new_ret += ' = '
                    while ret:
                        try:
                            test_ret, ret = ret.split(',', 1)
                            test_ret = test_ret.strip()
                            if test_ret.startswith('[') or test_ret.startswith('('):
                                new_ret += test_ret[0] + '\n'
                                test_ret = test_ret[1:].strip()

                            new_ret += indent + '    ' + test_ret + ',\n'

                            if ret.strip().startswith('['):
                                test_ret = ret[:ret.find(']') + 1]
                                ret = ret.replace(test_ret, '', 1)

                                test_ret = ', '.join(
                                    itm.strip()
                                    for itm in test_ret.strip()[1:-1].split(',')
                                )
                                test_ret = '[' + test_ret + ']'
                                if ret.startswith(','):
                                    ret = ret[1:]
                                new_ret += indent + '    ' + test_ret + ',\n'
                        except:
                            new_ret += indent + '    ' + ret[:-1] + '\n'
                            new_ret += indent + ret[-1]
                            break
                    ret = new_ret

                    # if ret.endswith(']'):
                    #     start_marker = '['
                    #     end_marker = ']'
                    # else:
                    #     start_marker = '('
                    #     end_marker = ')'
                    # beg, end = ret.split(start_marker, 1)
                    # end = end[:-1].split(',')
                    # end = list(indent + '    ' + itm.strip() + ',' for itm in end)
                    # beg += start_marker + '\n' + '\n'.join(
                    #     end) + '\n' + indent + end_marker
                    # ret = beg
        else:
            ret = ''

        return ret

    if '(' in var_name and var_name.endswith(')'):
        tmp_var_name = var_name.replace(' ', '').replace(',', ', ')
        var_name = 'def ' + tmp_var_name + ':\n'

        brace_count = value.count('(')
        brace_count -= value.count(')')

        if brace_count < 0:
            new_value = ''
            brace_count = 0
            for char in list(value.strip()):
                if char == '(':
                    brace_count += 1
                elif char == ')':
                    brace_count -= 1
                if brace_count != -1:
                    new_value += char
                else:
                    brace_count = 0
            value = new_value
        elif brace_count > 0:
            new_value = ''
            brace_count = 0
            for char in list(value.strip()):
                if char == '(':
                    brace_count -= 1
                elif char == ')':
                    brace_count += 1
                if brace_count != -1:
                    value += char
                else:
                    brace_count = 0
            value = new_value

        for key in importer.allowed:
            value = value.replace('(' + key + ')', '')

        if value.startswith('('):
            value = '(' + value[1:].strip()

        if value.endswith(')'):
            value = value[:-1].strip() + ')'

        if '((' in value:
            double_start = value.find('((')
            double_end = value.find('))')
            double_search = value[double_start + 2:double_end - 1]
            count = double_search.count('(') - double_search.count(')')
            if count == 0:
                value = value.replace('((', '(', 1)
                value = value.replace('))', ')', 1)

        list_value = []
        found_open = False
        markers = ('+', '-', '&', '|', '<', '>', '=')
        for char in list(value):
            if char == '(':
                found_open = True
            elif char in markers:
                found_open = False
            elif char == ')' and found_open:
                list_value.reverse()
                list_value.remove('(')
                list_value.reverse()
                found_open = False
                continue

            list_value += [char]

        value = ''.join(list_value)

        for i in range(10, 1, -1):
            value = value.replace(' ' * i, ' ')
        print(DEFINE_TEMPLATE.format(indent, get_ret(), comment))
        return True

    elif value.startswith('(DWORD)'):
        value = value[7:]

    if (
        value.startswith('(') and
        value.endswith(')') and
        ',' not in value and
        '|' not in value and
        'and' not in value and
        'or' not in value
    ):
        value = value[1:-1].strip()

    if value.startswith('((HANDLE)(LONG_PTR)'):
        value = value.replace(
            '((HANDLE)(LONG_PTR)',
            'HANDLE(LONG_PTR('
        ) + '.value).value'
        print(DEFINE_TEMPLATE.format(indent, get_ret(), comment))
        return True

    if value.startswith('((DWORD   )'):
        value = value.replace('((DWORD   )', '')[:-1]
        if '0x' not in value and not value.isdigit():
            print(indent + get_ret())
            return

    if value.startswith('((DWORD)'):
        value = value.replace('((DWORD)', '')[:-1]
        if '0x' not in value and not value.isdigit():
            print(DEFINE_TEMPLATE.format(indent, get_ret(), comment))
            return True

    if value.startswith('((WORD)'):
        value = value.replace('((WORD)', '')[:-1]
        if '0x' not in value and not value.isdigit():
            print(DEFINE_TEMPLATE.format(indent, get_ret(), comment))
            return True

    if value.startswith('('):
        if value[1:-1].strip().isdigit():
            value = process_hex(value[1:-1].strip())

    if not value.startswith('0x') and value.isdigit():
        value = process_hex(value)

    if '|' in value or ' or ' in value:
        if '|' in value:
            splitter = '|'
            marker = ' | '
        else:
            splitter = ' or '
            marker = ' or '

        if value.startswith('(') and value.endswith(')'):
            value = value[1:-1]

            value = value.split(splitter)
            value = marker.join(d.strip() for d in value)

            if len(indent + get_ret()) > 79:
                value = (
                    '(\n' + indent + '    ' +
                    (marker + '\n' + indent + '    ').join(v.strip() for v in value.split(splitter)) +
                    '\n' + indent + ')'
                )

    res = get_ret()

    if 'FIELD_OFFSET' in res:

        beg, end = res.split('FIELD_OFFSET(', 1)
        brace_count = 1
        mid = ''
        for char in list(end):
            if char == '(':
                brace_count += 1
            if char == ')':
                brace_count -= 1
            if brace_count == 0:
                break
            mid += char

        end = end.replace(mid, '', 1)
        mid, param = mid.strip().rsplit(',', 1)
        param = ", '{0}'".format(param.strip())
        mid += param
        beg += 'FIELD_OFFSET(' + mid + end
        res = beg

    if res:
        if ' = ' in res and not res.startswith('#'):
            nm = res.split(' = ')[0]
            if nm in importer.allowed:
                importer.add(nm)
                return False

            if len(indent + res) > 79 and '\n' not in res.strip():
                beg, end = res.split(' = ', 1)
                beg += ' = (\n'
                end = indent + '    ' + end.strip() + '\n' + indent + ')'
                res = beg + end

        if '+' in res and 'FIELD_OFFSET' in res:
            res = res.replace('+ ', '+\n    ' + indent, 1)


        print(DEFINE_TEMPLATE.format(indent, res, comment))
        return True
