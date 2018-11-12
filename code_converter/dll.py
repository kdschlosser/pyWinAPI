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

from code_converter.win_functions import WIN_FUNCTIONS


TEMPLATE_DLL = '''{indent}{dll_lower} = ctypes.windll.{dll_upper}'''

TEMPLATE_FUNCTION = '''{original_lines}
{indent}{func_name} = {dll_lower}.{func_name}
{indent}{func_name}.restype = {return_value}'''


def parse_dll(indent, data, found_dlls):
    data = list(d.strip() for d in data)
    new_data = ' '.join(data)
    pos_funcs = new_data.split('(', 1)
    for i, pos_func in enumerate(pos_funcs):
        pos_func = pos_func.split(' ')[-1]
        for dll, known_funcs in WIN_FUNCTIONS.items():
            if pos_func in known_funcs:
                break
        else:
            continue

        break
    else:
        return ''

    lines = []
    if dll not in found_dlls:
        lines += [
            TEMPLATE_DLL.format(
                indent=indent,
                dll_lower=dll.lower(),
                dll_upper=dll
            ),
            ''
        ]
        found_dlls += [dll]

    return_values = pos_funcs[i].replace(pos_func, '').strip()
    return_values = list(item for item in return_values.split(' ') if item)

    if len(return_values) >= 3:
        return_value = return_values[-2]
    else:
        return_value = return_values[-1]

    original_lines = '\n'.join(indent + '# ' + ln for ln in data)
    lines += [
        TEMPLATE_FUNCTION.format(
            return_value=return_value,
            func_name=pos_func,
            indent=indent,
            dll_lower=dll.lower(),
            original_lines=original_lines
        )
    ]

    return '\n'.join(lines)






#
#
#
# class Dll(object):
#     def __init__(self, importer, data):
#         self.dlls = []
#
#
#         self.dll_string = dll.lower() + ' = ctypes.windll.' + dll
#         self.importer = importer
#         self.all = set()
#
#         self.lines = {}
#
#         found = []
#         start = None
#         brace_count = 0
#
#         for i, line in enumerate(data[:]):
#             if not line.strip():
#                 continue
#             if line.lstrip().startswith('#'):
#                 continue
#
#             if line.strip.startswith('typedef'):
#                 continue
#
#             for dll, functions in WIN_FUNCTIONS:
#
#
#
#
#
#
#
#             if (
#                 (line.startswith('WIN') and line.strip().endswith('API')) or
#                 line.startswith('PSSTDAPI') or
#                 line.startswith('STDAPI') or
#                 line.strip().startswith('extern') or
#                 'WINOLEAPI' in line or
#                 'NTAPI' in line or
#                 'NTSYSAPI' in line
#             ):
#                 start = i
#
#             elif line.rstrip().endswith('(') and not line.startswith(' '):
#                 start = i - 1
#
#             if start is not None:
#                 if line.strip().endswith(';') or line.strip().endswith(')'):
#                     found = data[start: i + 1]
#                     self.lines[start] = dict(
#                         line=' '.join(f.strip() for f in found),
#                         old_lines=found[:]
#                     )
#                     start = None
#
#             # WINSETUPAPI
#             # UINT
#             # WINAPI
#             # SetupRenameErrorW(
#             #     _In_ HWND hwndParent,
#             #     _In_opt_ PCWSTR DialogTitle,
#             #     _In_ PCWSTR SourceFile,
#             #     _In_ PCWSTR TargetFile,
#             #     _In_ UINT Win32ErrorCode,
#             #     _In_ DWORD Style
#             #     );
#
#     def process(self):
#         yield 0, self.dll_string
#
#         #     extern _Check_return_ HRESULT WINAPI DirectDrawEnumerateW( LPDDENUMCALLBACKW lpCallback, LPVOID lpContext );
#
#         for line_num, data in self.lines.items()[:]:
#             line = data['line']
#             old_lines = data['old_lines']
#
#             line = line.replace(' (', '(')
#
#             try:
#                 res_type, func_name = line[:line.find('(')].rsplit(' ', 1)
#             except ValueError:
#                 try:
#                     res_type, func_name = line[:line.rfind('(')].rsplit(' ', 1)
#                 except ValueError:
#                     print '*************** DLL ERROR1:', line
#                     continue
#
#             if res_type.startswith('STDAPI'):
#                 res_type = 'STDAPI'
#
#             elif 'PSSTDAPI' in res_type:
#                 res_type = 'PSSTDAPI'
#
#             elif 'extern' in res_type:
#                 for item in res_type.strip().split(' ')[1:]:
#                     if not item.startswith('_'):
#                         res_type = item
#                         break
#                 else:
#                     print '*********************** DLL ERROR2:', line
#                     continue
#
#             elif 'WINOLEAPI' in res_type:
#                 res_type = res_type.split(' ')[-1]
#             else:
#                 try:
#                     res_type = res_type.split(' ')[1]
#                 except IndexError:
#                     pass
#
#             func = func_name + ' = ' + self.dll + '.' + func_name
#
#             if len(func) > 79:
#                 func = (
#                     func_name +
#                     ' = (\n    ' +
#                     self.dll +
#                     '.' +
#                     func_name +
#                     '\n)'
#                 )
#
#             self.all.add(func_name)
#             if func_name in self.importer.allowed:
#                 self.importer.add(func_name)
#                 continue
#
#             new_lines = '\n# ' + '\n# '.join(old_lines)
#             new_lines += '\n'
#             new_lines += func
#             new_lines += '\n'
#             new_lines += func_name + '.restype = ' + res_type + '\n'
#             self.importer.add(res_type)
#
#
#             yield line_num, new_lines
