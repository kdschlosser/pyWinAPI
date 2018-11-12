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

    # if '0x' in value:
    #     if (
    #         ',' in value and
    #         '(' not in value and
    #         ')' not in value and
    #         value.count('0x') > 1
    #     ):
    #         value = '(' + ', '.join(
    #             '0x' +
    #             val.strip().replace('0x', '').upper().replace('L', '')
    #                 for val in value.split(',')
    #         ) + ')'
    #     else:
    #         try:
    #             if (
    #                 value.count('0x') == 1 and
    #                 '(' in value and
    #                 value.endswith(')')
    #             ):
    #                 hex_value = value.split('(', 1)[1][:-1].strip()
    #                 hex_value = process_hex(hex_value)
    #                 value = value.split('(', 1)[0] + '(' + hex_value + ')'
    #             else:
    #                 raise ValueError
    #
    #         except ValueError:
    #             new_value = ''
    #
    #             while '0x' in value:
    #                 start = value.find('0x')
    #                 new_value += value[:start]
    #
    #                 stop = 0
    #                 for char in list(value[start + 2:]):
    #                     if char.isdigit() or char in ('L', 'l'):
    #                         stop += 1
    #                     else:
    #                         break
    #
    #                 stop += start + 2
    #
    #                 if stop == 0:
    #                     break
    #
    #                 hx = value[start:stop]
    #                 value = value[stop:]
    #                 try:
    #                     new_value += process_hex(hx)
    #                 except ValueError:
    #                     print(indent + '#~#~#~', old_define)
    #                     return False
    #
    #             value = new_value + value

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
                    for val in value.split(',')
                ) +
                '\n' + indent + ')'
            )
            ret = var_name + ' = ' + value

        # elif 'DEFINE_GUIDNAMED' in value:
        #     # new_name, value = value.split(' ', 1)
        #
        #     value = value.replace('DEFINE_GUIDNAMED(', '')[:-1]
        #     value = (
        #         'DEFINE_GUIDNAMED(\n' +
        #         '\n'.join(
        #             '    ' + val.strip()
        #             for val in value.split(',')
        #         ) +
        #         '\n)'
        #     )
        #
        #     ret = var_name + ' = ' + value

        elif value and var_name != value:
            value = value.replace('{', '[').replace('}', ']')

            # if value.lower().startswith('0x'):
            #     value = value[2:].upper().replace('L', '')
            #
            #     while len(value) < 8:
            #         value = '0' + value
            #
            #     value = '0x' + value
            #
            # elif (
            #     (value.upper().endswith('L') and value[:-1].isdigit())
            #     or value.isdigit()
            # ):
            #     value = (
            #         hex(
            #             int(value.upper().replace('L', ''))
            #         )[2:].upper()
            #     )
            #
            #     while len(value) < 8:
            #         value = '0' + value
            #
            #     value = '0x' + value

            ret = var_name + ' = ' + value

            if len(indent + ret) > 76:
                if (
                    ',' in ret and
                    (
                        ('(' in ret and ret.endswith(')')) or
                        ('[' in ret and ret.endswith(']'))
                    )
                ):
                    if ret.endswith(']'):
                        start_marker = '['
                        end_marker = ']'
                    else:
                        start_marker = '('
                        end_marker = ')'
                    beg, end = ret.split(start_marker, 1)
                    end = end[:-1].split(',')
                    end = list(indent + '    ' + itm.strip() + ',' for itm in end)
                    beg += start_marker + '\n' + '\n'.join(
                        end) + '\n' + indent + end_marker
                    ret = beg

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

        print(DEFINE_TEMPLATE.format(indent, res, comment))
        return True

#
# class Define(object):
#     def __init__(self, importer, data):
#         self.importer = importer
#         self.lines = {}
#         self.all = set()
#
#         start = None
#         print "\n\n-- DEFINE ---------------------------------------------\n\n"
#
#         for i, line in enumerate(data[:]):
#             if 'This' in line:
#                 continue
#
#             if 'GUID_BUILDER' in line:
#                 continue
#
#             if line.startswith('#'):
#                 cut_index = 1
#
#                 for char in list(line)[1:]:
#                     if not char == ' ':
#                         break
#
#                     cut_index += 1
#
#                 line = '#' + line[cut_index:]
#
#             if line.startswith('#define INTERFACE'):
#                 continue
#
#             if line.startswith('#define') or line.startswith('# define'):
#                 start = i
#
#             if start is not None and not line.rstrip().endswith('\\'):
#                 new_line = ''
#
#                 for j in range(start, i + 1):
#                     new_data = data[j].strip()
#                     if new_data.endswith('\\'):
#                         new_data = new_data[:-1]
#                     new_line += ' ' + new_data
#                 self.lines[start] = new_line
#                 print self.lines[start]
#                 start = None
#
#     def process(self):
#
#         for line_num, line in self.lines.items()[:]:
#             line = line.replace('0X', '0x').replace('\t', '    ').replace('->', '.')
#             global value
#
#             try:
#                 var_name, value = line[1:].replace(
#                     'define',
#                     ''
#                 ).strip().split(' ', 1)
#             except ValueError:
#                 continue
#
#             var_name = var_name.strip()
#             value = value.strip()
#
#             if var_name == '#':
#                 try:
#                     var_name, value = value.split(' ', 1)
#
#                 except ValueError:
#                     continue
#
#             if '(' in var_name:
#                 brace_count = var_name.count('(')
#                 brace_count -= var_name.count(')')
#                 while brace_count > 0:
#                     var_name += value[:value.find(')') + 1]
#                     value = value[value.find(')') + 1:]
#                     brace_count = var_name.count('(')
#                     brace_count -= var_name.count(')')
#
#                 var_name = var_name.replace('=', '')
#
#             var_name = var_name.strip()
#             value = value.strip()
#
#             if var_name == value:
#                 continue
#
#             if '0x' in var_name:
#                 var_name, new_value = var_name.split('0x', 1)
#                 value = '0x' + new_value + value
#                 var_name = var_name.strip()
#                 value = value.strip()
#
#             if '0x' in value:
#                 if (
#                     ',' in value and
#                     '(' not in value and
#                     ')' not in value and
#                     value.count('0x') > 1
#                 ):
#                     value = '(' + ', '.join(
#                         '0x' +
#                         val.strip().replace('0x', '').upper().replace('L', '')
#                         for val in value.split(',')
#                     ) + ')'
#                 else:
#                     try:
#                         if (
#                             value.count('0x') == 1 and
#                             '(' in value and
#                             value.endswith(')')
#                         ):
#                             hex_value = value.split('(', 1)[1][:-1].strip()
#                             hex_value = process_hex(hex_value)
#                             value = value.split('(', 1)[0] + '(' + hex_value + ')'
#                         else:
#                             raise ValueError
#
#                     except ValueError:
#                         new_value = ''
#
#                         while '0x' in value:
#                             start = value.find('0x')
#                             new_value += value[:start]
#
#                             stop = 0
#                             for char in list(value[start + 2:]):
#                                 if char.isdigit() or char in ('L', 'l'):
#                                     stop += 1
#                                 else:
#                                     break
#
#                             stop += start + 2
#
#                             if stop == 0:
#                                 break
#
#                             hx = value[start:stop]
#                             value = value[stop:]
#                             try:
#                                 new_value += process_hex(hx)
#                             except ValueError:
#                                 print repr(var_name), repr(value)
#                                 import time
#                                 time.sleep(1)
#                                 raise
#
#                         value = new_value + value
#
#             elif '"' in value:
#                 if not value.endswith('"') or value == '"':
#                     value += '\\n"'
#
#             def get_ret():
#                 global value
#                 if not value.strip():
#                     return ''
#
#                 if value.startswith('L"'):
#                     value = value[1:]
#
#                 if var_name.startswith('def '):
#                     self.all.add(var_name.split('(')[0].replace('def ', ''))
#                     ret = '\n\n' + var_name + '    return ' + value
#
#                 elif 'CTL_CODE' in value:
#                     value = value.replace('CTL_CODE', '')[:-1]
#                     value = (
#                         'CTL_CODE(\n' +
#                         '\n'.join(
#                             '    ' + val.strip() + ','
#                             for val in value.split(',')
#                         ) +
#                         '\n)'
#                     )
#                     self.all.add(var_name)
#                     ret = var_name + ' = ' + value
#
#                 elif 'DEFINE_GUIDNAMED' in value:
#                     # new_name, value = value.split(' ', 1)
#
#                     value = value.replace('DEFINE_GUIDNAMED(', '')[:-1]
#                     value = (
#                         'DEFINE_GUIDNAMED(\n' +
#                         '\n'.join(
#                             '    ' + val.strip()
#                             for val in value.split(',')
#                         ) +
#                         '\n)'
#                     )
#                     self.all.add(var_name)
#                     ret = var_name + ' = ' + value
#
#                 elif value and var_name != value:
#                     value = value.replace('{', '[').replace('}', ']')
#                     self.all.add(var_name)
#
#                     if value.lower().startswith('0x'):
#                         value = value[2:].upper().replace('L', '')
#
#                         while len(value) < 8:
#                             value = '0' + value
#
#                         value = '0x' + value
#
#                     elif (
#                         (value.upper().endswith('L') and value[:-1].isdigit())
#                         or value.isdigit()
#                     ):
#                         value = (
#                             hex(
#                                 int(value.upper().replace('L', ''))
#                             )[2:].upper()
#                         )
#
#                         while len(value) < 8:
#                             value = '0' + value
#
#                         value = '0x' + value
#
#                     ret = var_name + ' = ' + value
#
#                     if len(ret) > 76:
#                         if (
#                             ',' in ret and (
#                                 ('(' in ret and ret.endswith(')')) or
#                                 ('[' in ret and ret.endswith(']'))
#                             )
#                         ):
#                             if ret.endswith(']'):
#                                 start_marker = '['
#                                 end_marker = ']'
#                             else:
#                                 start_marker = '('
#                                 end_marker = ')'
#                             beg, end = ret.split(start_marker, 1)
#                             end = end[:-1].split(',')
#                             end = list('    ' + itm.strip() + ',' for itm in end)
#                             beg += start_marker + '\n' + '\n'.join(end) + '\n' + end_marker
#                             ret = beg
#                 else:
#                     ret = ''
#
#                 if ret.endswith('A') and '0x' not in ret:
#                     ret = '# ' + ret
#                     return ret
#
#                 return ret
#
#             if '(' in var_name and var_name.endswith(')'):
#                 tmp_var_name = var_name.replace(' ', '').replace(',', ', ')
#                 self.all.add(tmp_var_name)
#                 var_name = 'def ' + tmp_var_name + ':\n'
#
#                 brace_count = value.count('(')
#                 brace_count -= value.count(')')
#
#                 if brace_count < 0:
#                     new_value = ''
#                     brace_count = 0
#                     for char in list(value.strip()):
#                         if char == '(':
#                             brace_count += 1
#                         elif char == ')':
#                             brace_count -= 1
#                         if brace_count != -1:
#                             new_value += char
#                         else:
#                             brace_count = 0
#                     value = new_value
#                 elif brace_count > 0:
#                     new_value = ''
#                     brace_count = 0
#                     for char in list(value.strip()):
#                         if char == '(':
#                             brace_count -= 1
#                         elif char == ')':
#                             brace_count += 1
#                         if brace_count != -1:
#                             value += char
#                         else:
#                             brace_count = 0
#                     value = new_value
#
#                 for key in self.importer.allowed:
#                     value = value.replace('(' + key + ')', '')
#
#                 if value.startswith('('):
#                     value = '(' + value[1:].strip()
#
#                 if value.endswith(')'):
#                     value = value[:-1].strip() + ')'
#
#                 if '((' in value:
#                     double_start = value.find('((')
#                     double_end = value.find('))')
#                     double_search = value[double_start + 2:double_end - 1]
#                     count = double_search.count('(') - double_search.count(')')
#                     if count == 0:
#                         value = value.replace('((', '(', 1)
#                         value = value.replace('))', ')', 1)
#
#                 list_value = []
#                 found_open = False
#                 markers = ('+', '-', '&', '|', '<', '>', '=')
#                 for char in list(value):
#                     if char == '(':
#                         found_open = True
#                     elif char in markers:
#                         found_open = False
#                     elif char == ')' and found_open:
#                         list_value.reverse()
#                         list_value.remove('(')
#                         list_value.reverse()
#                         found_open = False
#                         continue
#
#                     list_value += [char]
#
#                 value = ''.join(list_value)
#
#                 for i in range(10, 1, -1):
#                     value = value.replace(' ' * i, ' ')
#                 yield line_num, get_ret()
#                 continue
#
#             elif value.startswith('(DWORD)'):
#                 value = value[7:]
#
#             if (
#                 value.startswith('(') and
#                 value.endswith(')') and
#                 ',' not in value and
#                 '|' not in value and
#                 'and' not in value and
#                 'or' not in value
#             ):
#                 value = value[1:-1].strip()
#
#             if value.startswith('((HANDLE)(LONG_PTR)'):
#                 value = value.replace(
#                     '((HANDLE)(LONG_PTR)',
#                     'HANDLE(LONG_PTR('
#                 ) + ')'
#                 yield line_num, get_ret()
#                 continue
#
#             if value.startswith('((DWORD   )'):
#                 value = value.replace('((DWORD   )', '')[:-1]
#                 if '0x' not in value and not value.isdigit():
#                     yield line_num, get_ret()
#                     continue
#
#             if value.startswith('((DWORD)'):
#                 value = value.replace('((DWORD)', '')[:-1]
#                 if '0x' not in value and not value.isdigit():
#                     yield line_num, get_ret()
#                     continue
#
#             if value.startswith('((WORD)'):
#                 value = value.replace('((WORD)', '')[:-1]
#                 if '0x' not in value and not value.isdigit():
#                     yield line_num, get_ret()
#                     continue
#
#             if value.startswith('('):
#                 if value[1:-1].strip().isdigit():
#                     value = process_hex(value[1:-1].strip())
#
#             if not value.startswith('0x') and value.isdigit():
#                 value = process_hex(value)
#
#             if '|' in value or ' or ' in value:
#                 if '|' in value:
#                     splitter = '|'
#                     marker = ' | '
#                 else:
#                     splitter = ' or '
#                     marker = ' or '
#
#                 if value.startswith('(') and value.endswith(')'):
#                     value = value[1:-1]
#
#                     value = value.split(splitter)
#                     value = marker.join(d.strip() for d in value)
#
#                     if len(get_ret()) > 79:
#                         value = (
#                             '(\n    ' +
#                             (marker + '\n    ').join(value.split(splitter)) +
#                             '\n)'
#                         )
#
#             import fnmatch
#
#             res = get_ret()
#             if res:
#                 if res.startswith('def'):
#                     nm = res.split('(')[0].replace('def ', '')
#                     self.all.add(nm)
#                     if nm in self.importer.allowed:
#                         self.importer.add(nm)
#                         continue
#
#                 if ' = ' in res and not res.startswith('#'):
#                     nm = res.split(' = ')[0]
#                     self.all.add(nm)
#                     if nm in self.importer.allowed:
#                         self.importer.add(nm)
#                         continue
#
#                     if len(res) > 79 and '\n' not in res.strip():
#                         beg, end = res.split(' = ', 1)
#                         beg += ' = (\n'
#                         end = '    ' + end.strip() + '\n)'
#                         res = beg + end
#
#                 yield line_num, res
