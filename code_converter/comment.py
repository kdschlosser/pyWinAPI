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


def equalize_width(indent, comment):
    saved_comments = []

    comments = comment.split('\n')

    for comment in comments:
        if not comment:
            continue

        comment = comment.replace('#', '').strip()
        comment = comment.replace('   ', ' ').replace('  ', ' ')
        c_len = len(indent + '# ' + comment)
        if c_len <= 79:
            saved_comments += [indent + '# ' + comment]
        else:
            quote_open = False
            brace_count = 0
            par_count = 0

            last_space = 0
            temp_comment = indent + '# '
            for i, char in enumerate(list(comment)):
                if char == '"':
                    quote_open = not quote_open
                elif char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                elif char == '(':
                    par_count += 1
                elif char == ')':
                    par_count -= 1
                elif (
                    char == ' ' and
                    not quote_open and
                    not brace_count and
                    not par_count
                ):
                    last_space = i + len(indent) + 2
                temp_comment += char
                if len(temp_comment) == 79 and last_space:
                    temp_comment = temp_comment[:last_space]
                    break
            comment = comment.replace(
                temp_comment[temp_comment.find('#') + 2:],
                ''
            )

            saved_comments += [(
                indent +
                temp_comment.strip() +
                '\n' +
                equalize_width(indent, '# ' + comment)
            )]

    return '\n'.join(saved_comments)


def parse_comment(line):

    if '//' in line and '/*' not in line and 'http://' not in line:
        try:
            temp_line, comment = line.split('//')
        except ValueError:
            temp_line = ''
            comment = line.strip()[2:].strip()

        temp_line = temp_line.strip()
        if comment:
            return temp_line, '# ' + comment
        else:
            return temp_line, ''

    elif '/*' in line and '*/' not in line:
        return None, None

    elif '*/' in line and '/*' not in line:
        return '', ''

    elif '/*' in line:

        indent_count = 0
        for char in list(line):
            if char != ' ':
                break
            indent_count += 1

        indent_count -= indent_count % 4
        indent = ' ' * indent_count
        line = line.replace('/**', '/*')
        line = line.replace('**/', '*/')
        line = line.replace('/*', '\n/*')
        line = line.replace('*/', '\n')
        lines = line.split('\n')
        new_lines = []
        comments = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith('/*'):
                comments += [line[2:].strip()]
            else:
                new_lines += [line]

        if new_lines:
            line = indent + ' '.join(new_lines)
        else:
            line = ''

        if comments:
            comment = indent + '# ' + ('\n' + indent + '# ').join(comments)
        else:
            comment = ''

        return line, comment

    return line, ''
#
#
# class Comment(object):
#     def __init__(self, data, use_comments):
#         self.lines = {}
#
#         found = []
#         line_start = None
#         self.any_size_array = False
#         virtual = False
#         self.use_comments = use_comments
#
#         for i, line in enumerate(data):
#             if 'STDMETHOD(DefineScope)(' in line:
#                 print '*************', i
#
#             if line.lstrip().startswith('virtual') or line.startswith('DECLARE_INTERFACE_'):
#                 virtual = True
#
#             if virtual:
#                 if '//' in line:
#                     test_line = line.rsplit('//', 1)[0]
#                 else:
#                     test_line = line
#
#                 if test_line.rstrip().endswith('};'):
#                     virtual = False
#                 continue
#
#             if 'ANYSIZE_ARRAY' in line:
#                 self.any_size_array = True
#
#             if line.strip().startswith('//') and not found:
#                 self.lines[i] = [line]
#                 data[i] = ''
#
#             elif line.strip().startswith('/*') and not found:
#                 line_start = i
#
#             elif '/*' in line and not found:
#                 start = line.find('/*')
#                 end = line.find('*/') + 2
#                 comment = line[start:end]
#                 self.lines[i] = [comment]
#                 data[i] = line.replace(comment, '')
#
#             elif '//' in line and not found:
#                 start = line.find('//')
#                 comment = line[start:]
#                 self.lines[i] = [comment]
#                 data[i] = line.replace(comment, '')
#
#             if line_start is not None:
#                 found += [line]
#                 data[i] = ''
#                 if line.strip().endswith('*/'):
#                     self.lines[line_start] = found[:]
#                     found = []
#                     line_start = None
#
#     def process(self, importer):
#         if self.any_size_array:
#             importer.add('ANYSIZE_ARRAY')
#
#         message_id = False
#         message_text = False
#         skip = False
#         if self.use_comments:
#             for line_num, lines in self.lines.items()[:]:
#                 new_lines = []
#                 for line in lines:
#                     if not line:
#                         continue
#                     def size_line(ln):
#
#                         count = len(ln) - 1
#
#                         if message_text:
#                             line_len = 64
#                         else:
#                             line_len = 76
#
#                         index = line_len
#                         loop_count = 0
#
#                         while count > 76:
#                             loop_count += 1
#                             if loop_count == 3:
#                                 break
#                             try:
#                                 while True:
#                                     index -= 1
#                                     idx = (len(ln) - count) + index
#                                     try:
#                                         if list(ln)[idx] == ' ':
#                                             ln = list(ln)
#                                             ln.insert(idx, '#')
#                                             if message_text:
#                                                 for _ in range(13):
#                                                     ln.insert(idx + 1, ' ')
#                                             ln.insert(idx, '\n')
#                                             count -= index + 3
#                                             index = line_len
#                                             ln = ''.join(ln)
#                                             loop_count = 0
#                                             break
#                                     except IndexError:
#                                         raise RuntimeError
#                             except RuntimeError:
#                                 break
#
#                         return ln
#
#                     line = line.replace('/*', '').replace('//', '').replace('*/', '')
#                     line = line.strip()
#
#                     if 'dderror' in line:
#                         continue
#
#                     if 'MessageId:' in line:
#                         print '************ MESSAGE ID'
#                         message_id = True
#                         yield line_num, '# ' + line
#                         continue
#
#                     elif 'MessageText:' in line:
#                         print '************ MESSAGE TEXT:'
#                         message_text = True
#                         message_id = False
#                         break
#
#                     if message_text and line:
#                         line = size_line(line)
#                         message_text = False
#                         print '************ MESSAGE TEXT:', '# MessageText: ' + line
#                         yield line_num, '# MessageText: ' + line
#                         skip = True
#                         break
#
#                     if message_id or message_text:
#                         continue
#
#                     if not line:
#                         if not message_text:
#                             new_lines += ['']
#                         continue
#
#                     new_lines += ['# ' + size_line(line)]
#
#                 if message_id or message_text or not new_lines:
#                     continue
#
#                 if skip:
#                     skip = False
#                     continue
#
#                 yield line_num, '\n'.join(new_lines)
