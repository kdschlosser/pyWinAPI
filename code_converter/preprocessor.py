# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2018 EventGhost Project <http://eventghost.net/>
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
from code_converter.comment import parse_comment
import pyparsing
new_defines = []

module_name = ''


KNOWN_DEFINES = (
    'DECLSPEC_DEPRECATED_DDK', 'MIDL_PASS', 'RC_INVOKED', '_MSC_VER',
    '_M_AMD64', '_M_IX86_FP', '_M_X64', '_WIN32', '_WIN32_WINNT', 'defined',
    '_WIN32_WINNT_LONGHORN', '_WIN32_WINNT_NT4',  '__AVX__', '__64BIT__',
    '_WIN32_WINNT_VISTA', '_WIN32_WINNT_WIN10', '_WIN32_WINNT_WIN2K', 'WINVER',
    '_WIN32_WINNT_WIN6', '_WIN32_WINNT_WIN7', '_WIN32_WINNT_WIN8', '__AVX2__',
    '_WIN32_WINNT_WINBLUE', '_WIN32_WINNT_WINTHRESHOLD', '_WINRT_DLL',
    '_WIN32_WINNT_WINXP', '_WIN32_WINNT_WS03', '_WIN32_WINNT_WS08', '_WIN64',
    'NTDDI_VERSION', '_WIN32_IE', 'MOFCOMP_PASS', '_INC_WINAPIFAMILY',
    'WINAPI_FAMILY', 'WINAPI_PARTITION_DESKTOP', 'WINAPI_PARTITION_APP',
    'WINAPI_PARTITION_PC_APP', 'WINAPI_PARTITION_PHONE_APP', 'CINTERFACE',
    'WINAPI_PARTITION_SYSTEM', 'WINAPI_PARTITION_SERVER', '__cplusplus',
    '_INC_WINPACKAGEFAMILY', '_NTDDK_', '_NTHAL_', '_MINWINBASE_',
    '__WINDOWS_DONT_DISABLE_PRAGMA_PACK_WARNING__', '_FILETIME_', '_MAC',
    'UNICODE', 'GUID_DEFS_ONLY', 'NO_GUID_DEFS', 'MAX_PATH', '_WIN32_WINDOWS',
    '__LPGUID_DEFINED__', 'DUMMYUNIONNAME', '_DEBUG', '_HRESULT_DEFINED',
    '_AMD64_', '_X86_', '_WIN32_WINNT_WIN10_RS2', '_WIN32_WINNT_WIN10_RS3',
    'WIN64', '_ARM_', 'VISTA_KB942567', 'DBG', '_M_ALPHA', '_NTSCSI_USER_MODE_',
    '__midl', '_M_MRX000', '_M_PPC', '_M_IA64', '_M_ARM', '_M_ARM64', '_M_IX86',
    'ENABLE_RESTRICTED', '_M_HYBRID_X86_ARM64', '_AXP64_', '_ALPHA_', '_IA64_',
    '_M_CEE_PURE', '_NTSYSTEM_', '_STDCALL_SUPPORTED', '_MSC_FULL_VER', '_MSC_VER',
    '_M_I86', '_M_AXP64', '_M_HYBRID', '_WIN32_FUSION',
)

def parse_macro(indent, lne, macro=False, struct=False):
    global line
    line, comment = parse_comment(lne)
    comment = comment.strip()
    line = line.strip()

    if comment:
        comment = ' ' + comment

    def set_pattern(repl, add):
        global line

        line = line.replace(repl, '').strip()

        if ' or ' in line:
            defines = list(d.strip() for d in line.split(' or '))
        elif ' and ' in line:
            defines = list(d.strip() for d in line.split(' and '))
        else:
            defines = [line]

        for define in defines:
            old_define = define
            open_brackets = ''
            while define.startswith('('):
                open_brackets += define[:1]
                define = define[1:]

            define = open_brackets + add + define
            define += ')'
            line = line.replace(old_define, define)

    try:
        if line.startswith('#ifndef'):
            set_pattern('#ifndef', 'not defined(')
            if (
                line.count('(') == 1 and
                line.count(')') == 1 and
                line.startswith('(') and
                line.endswith(')')
            ):
                line = line[1:-1]

            new_line = 'if ' + line + ':'
            new_line = new_line.replace('( ', '(').replace(' )', ')')

            if macro:
                print(indent + new_line)
            elif struct:
                print(indent[:-4] + new_line)
                return '', indent + '    '
            else:
                print(indent + '    ' + new_line)
                return '', indent + '    '

        if line.startswith('#ifdef'):
            set_pattern('#ifdef', 'defined(')
            if (
                line.count('(') == 1 and
                line.count(')') == 1 and
                line.startswith('(') and
                line.endswith(')')
            ):
                line = line[1:-1]

            line = 'if ' + line + ':' + comment
            line = line.replace('( ', '(').replace(' )', ')')
            if macro:
                print(indent + line)
            elif struct:
                print(indent[:-4] + line)
                return '', indent + '    '
            else:
                print(indent + '    ' + line)
                return '', indent + '    '

        if (
            line.startswith('#elif') or
            line.startswith('#else') or
            line.startswith('#if')
        ):

            for item in ('#elif', '#if'):
                if line.startswith(item):
                    line = line.replace(item, '').strip()

                    if (
                        line.count('(') == 1 and
                        line.count(')') == 1 and
                        line.startswith('(') and
                        line.endswith(')')
                    ):
                        line = line[1:-1]

                    line = item + ' ' + line
                    break

            line = line[1:] + ':' + comment
            line = line.replace('( ', '(').replace(' )', ')')

            if line.startswith('if'):
                if macro:
                    print(indent + line)
                elif struct:
                    print(indent[:-4] + line)
                    return '', indent + '    '
                else:
                    print(indent + '    ' + line)
                    return '', indent + '    '

            else:
                if macro:
                    print(indent + line)
                elif struct:
                    print(indent[:-4] + line)
                    return '', indent
                else:
                    print(indent + line)
                    return '', indent

        if line.startswith('#endif'):
            if struct:
                indent = indent[:-4]
                if comment:
                    print(indent[:-4] + '# END IF ' + comment[2:] + '\n')
                else:
                    print(indent[:-4] + '# END IF' + '\n\n')

                return '', indent

            if comment:
                print(indent + '# END IF ' + comment[2:] + '\n')
            else:
                print(indent + '# END IF' + '\n\n')
            return '', indent[:-4]

        return line, indent

    finally:
        data_type = pyparsing.oneOf("defined")
        decl_data_type = pyparsing.Combine(data_type)
        name = pyparsing.Word(pyparsing.alphas + '_',
            pyparsing.alphanums + '_')

        LPAR, RPAR = map(pyparsing.Suppress, "()")

        c_function = (
            decl_data_type("type")
            + LPAR + name("name") + RPAR
        )
        c_function.ignore(pyparsing.cStyleComment)

        for define in c_function.searchString(line):
            if (
                define['name'] not in new_defines and
                define['name'] not in KNOWN_DEFINES
            ):
                new_defines.append(define['name'])

