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

OPERATORS = ['<<', '>>', '|', '&', '+', '-', '*', '/']
ALLOWED_HEX = '0123456789ABCDEF'


def process_hex(code):

    def modify_code(marker, temp_code):
        new_code = ''
        while marker in temp_code:
            t_code, h_code = temp_code.split(marker, 1)
            new_code += t_code
            hex_code = '0x'
            for char in list(h_code[:]):
                if not char.upper() in ALLOWED_HEX:
                    break
                hex_code += char.upper()
                h_code = h_code[1:]
            new_code += hex_code
            if h_code.upper().startswith('L'):
                h_code = h_code[1:]

            elif h_code.upper().startswith('UL'):
                h_code = h_code[2:]

            temp_code = h_code

        new_code += temp_code
        return new_code

    code = modify_code('0x', code)
    code = modify_code('0X', code)
    return code


def split_strip(item, marker, count=1):
    return list(itm.strip() for itm in item.strip().split(marker, count))


def process_param(key, value):
    if '[' in key:
        key, array = split_strip(key, '[')
        array = array[:-1].strip()
        if not array:
            array = 0

        array = ' * {0}'.format(array)
    else:
        array = ''

    key = key.strip()
    value = value.strip()

    if key == value:
        return None, None

    while value.endswith('*'):
        key = '*' + key
        value = value[:-1]
    value = value.strip()
    value += array

    while key.startswith('*'):
        value = 'POINTER(' + value + ')'
        key = key[1:].strip()

    if 'comtypes.IUnknown' not in value:
        value = value.replace('IUnknown', 'comtypes.IUnknown')

    return key, value
