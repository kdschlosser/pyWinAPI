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


import ctypes
import comtypes
from shared.wtypes_h import POINTER

ULONG = ctypes.c_ulong


# noinspection PyTypeChecker,PyCallingNonCallable
class GUID(comtypes.GUID):

    def __bool__(self):
        return self != GUID_NULL

    def __copy__(self):
        return GUID(str(self))

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
            if not guid.startswith('{'):
                guid = '{' + guid + '}'
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

        if guid is None:
            comtypes.GUID.__init__(self)
        else:
            comtypes.GUID.__init__(self, guid)


GUID_NULL = GUID()


def InlineIsEqualGUID(rguid1, rguid2):
    return rguid1 == rguid2


def IsEqualGUID(rguid1, rguid2):
    return InlineIsEqualGUID(rguid1, rguid2)


def DEFINE_GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
    return GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8)


def DEFINE_OLEGUID(l, w1, w2):
    return DEFINE_GUID(l, w1, w2, 0xC0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x46)


def EXTERN_GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
    return GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8)


def MIDL_INTERFACE(g):
    return GUID(g)


LPGUID = POINTER(GUID)
LPCGUID = POINTER(GUID)


IID = GUID
LPIID = POINTER(IID)
IID_NULL = GUID()


def IsEqualIID(riid1, riid2):
    return IsEqualGUID(riid1, riid2)


CLSID = GUID
LPCLSID = POINTER(CLSID)
CLSID_NULL = GUID()


def IsEqualCLSID(rclsid1, rclsid2):
    return IsEqualGUID(rclsid1, rclsid2)


FMTID = GUID
LPFMTID = POINTER(FMTID)
FMTID_NULL = GUID()


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


def DECLSPEC_UUID(guid):
    return GUID(guid)


class _tagPROPERTYKEY(ctypes.Structure):
    _fields_ = [
        ('fmtid', GUID),
        ('pid', ULONG),
    ]


PROPERTYKEY = _tagPROPERTYKEY

uuid = GUID

__all__ = (
    'GUID', 'GUID_NULL', 'InlineIsEqualGUID', 'IsEqualGUID', 'DEFINE_GUID',
    'DEFINE_OLEGUID', 'EXTERN_GUID', 'LPGUID', 'LPCGUID', 'IID', 'LPIID',
    'IID_NULL', 'IsEqualIID', 'CLSID', 'LPCLSID', 'CLSID_NULL', 'IsEqualCLSID',
    'FMTID', 'LPFMTID', 'FMTID_NULL', 'IsEqualFMTID', 'REFGUID', 'REFIID',
    'REFCLSID', 'REFFMTID', 'DEFINE_GUIDSTRUCT', 'DEFINE_GUIDNAMED',
    'DECLSPEC_UUID', 'PROPERTYKEY', 'uuid', 'MIDL_INTERFACE'
)
