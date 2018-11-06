__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import * # NOQA
# from .rpcndr_h import * # NOQA
from .unknwn_h import * # NOQA
from .wtypes_h import * # NOQA

import ctypes



# INTerface __MIDL_itf_shtypes_0000_0000
# [local]
# nonstandard extension : single line comment
# padding added after data member
# +-------------------------------------------------------------------------

# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.

# --------------------------------------------------------------------------

# For compilers that don't support nameless unions
# ===========================================================================

# Object identifiers in the explorer's name space (ItemID and IDList)

# All the items that the user can browse with the explorer (such as files,
# directories, servers, work-groups, etc.) has an identifier which is unique
# among items within the parent folder. Those identifiers are called item
# IDs (SHITEMID). Since all its parent folders have their own item IDs,
# any items can be uniquely identified by a list of item IDs, which is called
# an ID list (ITEMIDLIST).

# ID lists are almost always allocated by the task allocator (see some
# description below as well as OLE 2.0 SDK) and may be passed across
# some of shell INTerfaces (such as IShellFolder). Each item ID in an ID list
# is only meaningful to its parent folder (which has generated it), and all
# the clients must treat it as an opaque binary data except the first two
# bytes, which indicates the size of the item ID.

# When a shell extension -- which implements the IShellFolder INTerace --
# generates an item ID, it may put any information in it, not only the data
# with that it needs to identifies the item, but also some additional
# information, which would help implementing some other functions efficiently.
# For example, the shell's IShellFolder implementation of file system items
# stores the primary (LONG) name of a file or a directory as the item
# identifier, but it also stores its alternative (SHORT) name, size and date
# etc.

# When an ID list is passed to one of shell APIs (such as SHGetPathFromIDList),
# it is always an absolute path -- relative from the root of the name space,
# which is the desktop folder. When an ID list is passed to one of IShellFolder
# member function, it is always a relative path from the folder (unless it
# is explicitly specified).

# ===========================================================================

# SHITEMID -- Item ID  (mkid)
# USHORT      cb;              Size of the ID (including cb itself)
# BYTE        abID[];          The item ID (variable length)

# from .pshpack1_h import * # NOQA

class _SHITEMID(ctypes.Structure):
    _fields_ = [
        ('cb', USHORT),
        ('abID', BYTE * 1),
    ]


SHITEMID = _SHITEMID


# from .poppack_h import * # NOQA
# __unaligned
LPSHITEMID = POINTER(SHITEMID)
LPCSHITEMID = POINTER(SHITEMID)

# ITEMIDLIST -- List if item IDs (combined with 0-terminator)

# from .pshpack1_h import * # NOQA

class _ITEMIDLIST(ctypes.Structure):
    _fields_ = [
        ('mkid', SHITEMID),
    ]


ITEMIDLIST = _ITEMIDLIST

ITEMIDLIST_RELATIVE = ITEMIDLIST
ITEMID_CHILD = ITEMIDLIST
ITEMIDLIST_ABSOLUTE = ITEMIDLIST

# from .poppack_h import * # NOQA
wirePIDL = POINTER(BYTE_BLOB)
LPITEMIDLIST = POINTER(ITEMIDLIST)
LPCITEMIDLIST = POINTER(ITEMIDLIST)
PIDLIST_ABSOLUTE = POINTER(ITEMIDLIST_ABSOLUTE)
PCIDLIST_ABSOLUTE = POINTER(ITEMIDLIST_ABSOLUTE)
PCUIDLIST_ABSOLUTE = POINTER(ITEMIDLIST_ABSOLUTE)
PIDLIST_RELATIVE = POINTER(ITEMIDLIST_RELATIVE)
PCIDLIST_RELATIVE = POINTER(ITEMIDLIST_RELATIVE)
PUIDLIST_RELATIVE = POINTER(ITEMIDLIST_RELATIVE)
PCUIDLIST_RELATIVE = POINTER(ITEMIDLIST_RELATIVE)
PITEMID_CHILD = POINTER(ITEMID_CHILD)
PCITEMID_CHILD = POINTER(ITEMID_CHILD)
PUITEMID_CHILD = POINTER(ITEMID_CHILD)
PCUITEMID_CHILD = POINTER(ITEMID_CHILD)
PCUITEMID_CHILD_ARRAY = POINTER(PCUITEMID_CHILD)
PCUIDLIST_RELATIVE_ARRAY = POINTER(PCUIDLIST_RELATIVE)
PCIDLIST_ABSOLUTE_ARRAY = POINTER(PCIDLIST_ABSOLUTE)
PCUIDLIST_ABSOLUTE_ARRAY = POINTER(PCUIDLIST_ABSOLUTE)
PCIDLIST_ABSOLUTE = LPCITEMIDLIST
PCUIDLIST_ABSOLUTE = LPCITEMIDLIST
PCUIDLIST_RELATIVE = LPCITEMIDLIST
PCUITEMID_CHILD = LPCITEMIDLIST


class _WIN32_FIND_DATAA(ctypes.Structure):
    _fields_ = [
        ('dwFileAttributes', DWORD),
        ('ftCreationTime', FILETIME),
        ('ftLastAccessTime', FILETIME),
        ('ftLastWriteTime', FILETIME),
        ('nFileSizeHigh', DWORD),
        ('nFileSizeLow', DWORD),
        ('dwReserved0', DWORD),
        ('dwReserved1', DWORD),
        ('cFileName', CHAR * 260),
        ('cAlternateFileName', CHAR * 14),
    ]


WIN32_FIND_DATAA = _WIN32_FIND_DATAA
PWIN32_FIND_DATAA = POINTER(_WIN32_FIND_DATAA)
LPWIN32_FIND_DATAA = POINTER(_WIN32_FIND_DATAA)


class _WIN32_FIND_DATAW(ctypes.Structure):
    _fields_ = [
        ('dwFileAttributes', DWORD),
        ('ftCreationTime', FILETIME),
        ('ftLastAccessTime', FILETIME),
        ('ftLastWriteTime', FILETIME),
        ('nFileSizeHigh', DWORD),
        ('nFileSizeLow', DWORD),
        ('dwReserved0', DWORD),
        ('dwReserved1', DWORD),
        ('cFileName', WCHAR * 260),
        ('cAlternateFileName', WCHAR * 14),
    ]


WIN32_FIND_DATAW = _WIN32_FIND_DATAW
PWIN32_FIND_DATAW = POINTER(_WIN32_FIND_DATAW)
LPWIN32_FIND_DATAW = POINTER(_WIN32_FIND_DATAW)


# MIDL_PASS
# -------------------------------------------------------------------------

# struct STRRET

# structure for returning strings from IShellFolder member functions

# -------------------------------------------------------------------------

# uType indicate which union member to use
# STRRET_WSTR    Use STRRET.pOleStr     must be freed by caller of
# GetDisplayNameOf
# STRRET_OFFSET  Use STRRET.uOffset     Offset INTo SHITEMID for ANSI string
# STRRET_CSTR    Use STRRET.cStr        ANSI Buffer

# [v1_enum]
class tagSTRRET_TYPE(ENUM):
    STRRET_WSTR = 0
    STRRET_OFFSET = 0x1
    STRRET_CSTR = 0x2


STRRET_TYPE = tagSTRRET_TYPE


# nonstandard extension used : nameless struct/union
# from .pshpack8_h import * # NOQA

class _STRRET(ctypes.Structure):

    class DUMMYUNIONNAME(ctypes.Union):
        _fields_ = [
            ('pOleStr', LPWSTR),
            ('uOffset', UINT),
            ('cStr', CHAR * 260),
        ]

    _fields_ = [
        ('uType', UINT),
        ('DUMMYUNIONNAME', DUMMYUNIONNAME),
    ]


STRRET = _STRRET
LPSTRRET = POINTER(STRRET)
# -------------------------------------------------------------------------

# struct SHELLDETAILS

# structure for returning strings from IShellDetails

# -------------------------------------------------------------------------

# fmt;             LVCFMT_* value (header only)
# cxChar;          Number of 'average' CHARacters (header only)
# str;             String information


class _SHELLDETAILS(ctypes.Structure):
    _fields_ = [
        ('fmt', INT),
        ('cxChar', INT),
        ('str', STRRET),
    ]


SHELLDETAILS = _SHELLDETAILS
LPSHELLDETAILS = POINTER(_SHELLDETAILS)


class tagPERCEIVED(ENUM):
    PERCEIVED_TYPE_FIRST = - 3
    PERCEIVED_TYPE_CUSTOM = - 3
    PERCEIVED_TYPE_UNSPECIFIED = - 2
    PERCEIVED_TYPE_FOLDER = - 1
    PERCEIVED_TYPE_UNKNOWN = 0
    PERCEIVED_TYPE_TEXT = 1
    PERCEIVED_TYPE_IMAGE = 2
    PERCEIVED_TYPE_AUDIO = 3
    PERCEIVED_TYPE_VIDEO = 4
    PERCEIVED_TYPE_COMPRESSED = 5
    PERCEIVED_TYPE_DOCUMENT = 6
    PERCEIVED_TYPE_SYSTEM = 7
    PERCEIVED_TYPE_APPLICATION = 8
    PERCEIVED_TYPE_GAMEMEDIA = 9
    PERCEIVED_TYPE_CONTACTS = 10
    PERCEIVED_TYPE_LAST = 10


PERCEIVED = tagPERCEIVED


PERCEIVEDFLAG_UNDEFINED = 0x0000
PERCEIVEDFLAG_SOFTCODED = 0x0001
PERCEIVEDFLAG_HARDCODED = 0x0002
PERCEIVEDFLAG_NATIVESUPPORT = 0x0004
PERCEIVEDFLAG_GDIPLUS = 0x0010
PERCEIVEDFLAG_WMSDK = 0x0020
PERCEIVEDFLAG_ZIPFOLDER = 0x0040
PERCEIVEDFLAG = DWORD


class _COMDLG_FILTERSPEC(ctypes.Structure):
    _fields_ = [
        ('pszName', LPCWSTR),
        ('pszSpec', LPCWSTR),
    ]


COMDLG_FILTERSPEC = _COMDLG_FILTERSPEC
KNOWNFOLDERID = GUID
REFKNOWNFOLDERID = POINTER(KNOWNFOLDERID)
KF_REDIRECT_FLAGS = DWORD
FOLDERTYPEID = GUID
REFFOLDERTYPEID = POINTER(FOLDERTYPEID)
TASKOWNERID = GUID
REFTASKOWNERID = POINTER(TASKOWNERID)
ELEMENTID = GUID
REFELEMENTID = POINTER(ELEMENTID)


class tagLOGFONTA(ctypes.Structure):
    _fields_ = [
        ('lfHeight', LONG),
        ('lfWidth', LONG),
        ('lfEscapement', LONG),
        ('lfOrientation', LONG),
        ('lfWeight', LONG),
        ('lfItalic', BYTE),
        ('lfUnderline', BYTE),
        ('lfStrikeOut', BYTE),
        ('lfCharSet', BYTE),
        ('lfOutPrecision', BYTE),
        ('lfClipPrecision', BYTE),
        ('lfQuality', BYTE),
        ('lfPitchAndFamily', BYTE),
        ('lfFaceName', CHAR * 32),
    ]


LOGFONTA = tagLOGFONTA


class tagLOGFONTW(ctypes.Structure):
    _fields_ = [
        ('lfHeight', LONG),
        ('lfWidth', LONG),
        ('lfEscapement', LONG),
        ('lfOrientation', LONG),
        ('lfWeight', LONG),
        ('lfItalic', BYTE),
        ('lfUnderline', BYTE),
        ('lfStrikeOut', BYTE),
        ('lfCharSet', BYTE),
        ('lfOutPrecision', BYTE),
        ('lfClipPrecision', BYTE),
        ('lfQuality', BYTE),
        ('lfPitchAndFamily', BYTE),
        ('lfFaceName', WCHAR * 32),
    ]


LOGFONTW = tagLOGFONTW
LOGFONT = LOGFONTW


class tagSHCOLSTATE(ENUM):
    SHCOLSTATE_DEFAULT = 0
    SHCOLSTATE_TYPE_STR = 0x1
    SHCOLSTATE_TYPE_INT = 0x2
    SHCOLSTATE_TYPE_DATE = 0x3
    SHCOLSTATE_TYPEMASK = 0xF
    SHCOLSTATE_ONBYDEFAULT = 0x10
    SHCOLSTATE_SLOW = 0x20
    SHCOLSTATE_EXTENDED = 0x40
    SHCOLSTATE_SECONDARYUI = 0x80
    SHCOLSTATE_HIDDEN = 0x100
    SHCOLSTATE_PREFER_VARCMP = 0x200
    SHCOLSTATE_PREFER_FMTCMP = 0x400
    SHCOLSTATE_NOSORTBYFOLDERNESS = 0x800
    SHCOLSTATE_VIEWONLY = 0x10000
    SHCOLSTATE_BATCHREAD = 0x20000
    SHCOLSTATE_NO_GROUPBY = 0x40000
    SHCOLSTATE_FIXED_WIDTH = 0x1000
    SHCOLSTATE_NODPISCALE = 0x2000
    SHCOLSTATE_FIXED_RATIO = 0x4000
    SHCOLSTATE_DISPLAYMASK = 0xF000


SHCOLSTATE = tagSHCOLSTATE


SHCOLSTATEF = DWORD
SHCOLUMNID = PROPERTYKEY
LPCSHCOLUMNID = POINTER(SHCOLUMNID)


class DEVICE_SCALE_FACTOR(ENUM):
    DEVICE_SCALE_FACTOR_INVALID = 0
    SCALE_100_PERCENT = 100
    SCALE_120_PERCENT = 120
    SCALE_125_PERCENT = 125
    SCALE_140_PERCENT = 140
    SCALE_150_PERCENT = 150
    SCALE_160_PERCENT = 160
    SCALE_175_PERCENT = 175
    SCALE_180_PERCENT = 180
    SCALE_200_PERCENT = 200
    SCALE_225_PERCENT = 225
    SCALE_250_PERCENT = 250
    SCALE_300_PERCENT = 300
    SCALE_350_PERCENT = 350
    SCALE_400_PERCENT = 400
    SCALE_450_PERCENT = 450
    SCALE_500_PERCENT = 500


__all__ = (
    'PUITEMID_CHILD', 'REFELEMENTID', 'REFKNOWNFOLDERID', 'PCUITEMID_CHILD',
    'PERCEIVEDFLAG_NATIVESUPPORT', 'PERCEIVEDFLAG_WMSDK', 'REFFOLDERTYPEID',
    'PERCEIVEDFLAG_UNDEFINED', 'PUIDLIST_RELATIVE', 'LOGFONTA', 'LOGFONTW',
    'PCUIDLIST_ABSOLUTE_ARRAY', 'PCUIDLIST_ABSOLUTE', 'PCUIDLIST_RELATIVE',
    '__REQUIRED_RPCNDR_H_VERSION__', 'PCIDLIST_ABSOLUTE_ARRAY', '_STRRET',
    'PCIDLIST_ABSOLUTE', 'PERCEIVEDFLAG_GDIPLUS', 'PIDLIST_ABSOLUTE',
    'PCIDLIST_RELATIVE', 'PERCEIVEDFLAG_HARDCODED', 'PCUITEMID_CHILD_ARRAY',
    'PIDLIST_RELATIVE', 'PCUIDLIST_RELATIVE_ARRAY', 'PERCEIVEDFLAG_SOFTCODED',
    'PCITEMID_CHILD', 'PITEMID_CHILD', 'REFTASKOWNERID', 'tagSHCOLSTATE',
    '__REQUIRED_RPCSAL_H_VERSION__', 'PERCEIVEDFLAG_ZIPFOLDER', 'tagLOGFONTA',
    'DEVICE_SCALE_FACTOR', 'tagSTRRET_TYPE', 'tagPERCEIVED', '_SHELLDETAILS',
    '_WIN32_FIND_DATAW', '_COMDLG_FILTERSPEC', '_ITEMIDLIST', '_SHITEMID',
    '_WIN32_FIND_DATAA', 'tagLOGFONTW', 'KF_REDIRECT_FLAGS', 'KNOWNFOLDERID',
    'SHCOLSTATEF', 'LPSTRRET', 'ITEMIDLIST_ABSOLUTE', 'LPSHITEMID', 'LOGFONT',
    'ITEMID_CHILD', 'TASKOWNERID', 'PERCEIVEDFLAG', 'ITEMIDLIST_RELATIVE',
    'ELEMENTID', 'LPCITEMIDLIST', 'SHCOLUMNID', 'LPITEMIDLIST', 'wirePIDL',
    'LPCSHCOLUMNID', 'FOLDERTYPEID', 'LPCSHITEMID',
)
