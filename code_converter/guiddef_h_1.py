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

import ctypes
from code_converter.data_types import POINTER, DWORD, WORD, BYTE, ULONG


_ole32 = ctypes.oledll.ole32

_StringFromCLSID = _ole32.StringFromCLSID
_CoTaskMemFree = ctypes.windll.ole32.CoTaskMemFree
_CLSIDFromString = _ole32.CLSIDFromString


# noinspection PyTypeChecker,PyCallingNonCallable
class _GUID(ctypes.Structure):
    _fields_ = [
        ('Data1', DWORD),
        ('Data2', WORD),
        ('Data3', WORD),
        ('Data4', BYTE * 8)
    ]

    def __cmp__(self, other):
        if isinstance(other, GUID):
            return cmp(bytes(self), bytes(other))
        return -1

    def __eq__(self, other):
        return isinstance(other, GUID) and bytes(self) == bytes(other)

    def __init__(self, *guid):
        """a144ed38 - 8e12 -4de4 - 9d 96 -e6 47 40 b1 a5 24}
        Data1 = 0xa144ed38
        Data2 = 0x8e12
        Data3 = 0x4de4
        data4[0] = -0x9d
        data4[1] = 0x96
        data4[2] = 0xe6
        data4[3] = 0x47
        data4[4] = 0x40
        data4[5] = 0xb1
        data4[6] = 0xa5
        data4[7] = 0x24
        """

        if not guid:
            guid = None

        elif len(guid) == 1:
            guid = guid[0]

        else:
            hex_guid = guid
            guid = []
            hex_four = ''
            hex_twelve = ''
            for h in hex_guid:
                h = hex(h)[2:].replace('L', '')

                if len(h) not in (8, 4, 2):
                    h = '0' + h

                if len(h) == 2:
                    if hex_four is not None and hex_four:
                        h = hex_four + h
                        hex_four = None
                    elif hex_four is None:
                        hex_twelve += h
                        if len(hex_twelve) == 12:
                            h = hex_twelve
                        else:
                            continue
                    else:
                        hex_four = h
                        continue
                guid += [h.upper()]

            guid = '{' + '-'.join(guid) + '}'

        ctypes.Structure.__init__(self)

        if guid is not None:
            _CLSIDFromString(unicode(guid), ctypes.byref(self))

    def __str__(self):
        p = ctypes.c_wchar_p()
        _StringFromCLSID(ctypes.byref(self), ctypes.byref(p))
        result = p.value
        _CoTaskMemFree(p)
        return result


GUID = _GUID

GUID_NULL = GUID()


def InlineIsEqualGUID(rguid1, rguid2):
    return rguid1 == rguid2


def IsEqualGUID(rguid1, rguid2):
    return InlineIsEqualGUID(rguid1, rguid2)


def DEFINE_GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
    return GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8)


def DEFINE_OLEGUID(l, w1, w2):
    return DEFINE_GUID(l, w1, w2, 0xC0, 0, 0, 0, 0, 0, 0, 0x46)


def EXTERN_GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
    return GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8)


LPGUID = POINTER(GUID)
LPCGUID = POINTER(GUID)


IID = GUID
LPIID = POINTER(IID)
IID_NULL = GUID_NULL


def IsEqualIID(riid1, riid2):
    return IsEqualGUID(riid1, riid2)


CLSID = GUID
LPCLSID = POINTER(CLSID)
CLSID_NULL = GUID_NULL


def IsEqualCLSID(rclsid1, rclsid2):
    return IsEqualGUID(rclsid1, rclsid2)


FMTID = GUID
LPFMTID = POINTER(FMTID)
FMTID_NULL = GUID_NULL


def IsEqualFMTID(rfmtid1, rfmtid2):
    return IsEqualGUID(rfmtid1, rfmtid2)


REFGUID = GUID
REFIID = IID
REFCLSID = IID
REFFMTID = IID


def DEFINE_GUIDSTRUCT(guid):
    return GUID(guid)


def DEFINE_GUIDNAMED(guid):
    if isinstance(guid, GUID):
        return guid
    return GUID(guid)


class _tagPROPERTYKEY(ctypes.Structure):
    _fields_ = [
        ('fmtid', GUID),
        ('pid', ULONG),
    ]


PROPERTYKEY = _tagPROPERTYKEY


def DEFINE_PROPERTYKEY(*guid):
    guid = GUID(*guid[:-1])
    index = guid[-1]

    return PROPERTYKEY(GUID(guid), index)
