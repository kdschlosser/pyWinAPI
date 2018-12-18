import ctypes
import comtypes
import comtypes.automation
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

COMMETHOD = comtypes.COMMETHOD
IDispatch = comtypes.automation.IDispatch
helpstring = comtypes.helpstring


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
__wtypesbase_h__ = None
__IWinTypesBase_INTERFACE_DEFINED__ = None
OLE2ANSI = None
_WINDEF_ = None
_MINWINDEF_ = None
_DWORDLONG_ = None
_ULONGLONG_ = None
_WINBASE_ = None
_SYSTEMTIME_ = None
_SECURITY_ATTRIBUTES_ = None
SECURITY_DESCRIPTOR_REVISION = None
__OBJECTID_DEFINED = None
_ROTREGFLAGS_DEFINED = None
_APPIDREGFLAGS_DEFINED = None
_DCOMSCM_REMOTECALL_FLAGS_DEFINED = None
_tagBLOB_DEFINED = None
SID_IDENTIFIER_AUTHORITY_DEFINED = None
SID_DEFINED = None


class _LARGE_INTEGER(ctypes.Structure):
    pass


LARGE_INTEGER = _LARGE_INTEGER


class _ULARGE_INTEGER(ctypes.Structure):
    pass


ULARGE_INTEGER = _ULARGE_INTEGER


class _FILETIME(ctypes.Structure):
    pass


FILETIME = _FILETIME


class _SYSTEMTIME(ctypes.Structure):
    pass


SYSTEMTIME = _SYSTEMTIME


class _SECURITY_ATTRIBUTES(ctypes.Structure):
    pass


SECURITY_ATTRIBUTES = _SECURITY_ATTRIBUTES


class _ACL(ctypes.Structure):
    pass


ACL = _ACL


class _SECURITY_DESCRIPTOR(ctypes.Structure):
    pass


SECURITY_DESCRIPTOR = _SECURITY_DESCRIPTOR


class _COAUTHIDENTITY(ctypes.Structure):
    pass


COAUTHIDENTITY = _COAUTHIDENTITY


class _COAUTHINFO(ctypes.Structure):
    pass


COAUTHINFO = _COAUTHINFO


class _OBJECTID(ctypes.Structure):
    pass


OBJECTID = _OBJECTID


class _BYTE_BLOB(ctypes.Structure):
    pass


BYTE_BLOB = _BYTE_BLOB


class _WORD_BLOB(ctypes.Structure):
    pass


WORD_BLOB = _WORD_BLOB


class _DWORD_BLOB(ctypes.Structure):
    pass


DWORD_BLOB = _DWORD_BLOB


class _FLAGGED_BYTE_BLOB(ctypes.Structure):
    pass


FLAGGED_BYTE_BLOB = _FLAGGED_BYTE_BLOB


class _FLAGGED_WORD_BLOB(ctypes.Structure):
    pass


FLAGGED_WORD_BLOB = _FLAGGED_WORD_BLOB


class _BYTE_SIZEDARR(ctypes.Structure):
    pass


BYTE_SIZEDARR = _BYTE_SIZEDARR


class _SHORT_SIZEDARR(ctypes.Structure):
    pass


WORD_SIZEDARR = _SHORT_SIZEDARR


class _LONG_SIZEDARR(ctypes.Structure):
    pass


DWORD_SIZEDARR = _LONG_SIZEDARR


class _HYPER_SIZEDARR(ctypes.Structure):
    pass


HYPER_SIZEDARR = _HYPER_SIZEDARR


class tagBLOB(ctypes.Structure):
    pass


BLOB = tagBLOB


class _SID_IDENTIFIER_AUTHORITY(ctypes.Structure):
    pass


SID_IDENTIFIER_AUTHORITY = _SID_IDENTIFIER_AUTHORITY


class _SID(ctypes.Structure):
    pass


SID = _SID


class _SID_AND_ATTRIBUTES(ctypes.Structure):
    pass


SID_AND_ATTRIBUTES = _SID_AND_ATTRIBUTES


def annotation(value):
    if '_opt_' in value:
        return comtypes.defaultvalue(None)
    else:
        return None


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 8.01.0622
# @@MIDL_FILE_HEADING( )
# verify that the <rpcndr.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    pass
# END IF


# verify that the <rpcsal.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCSAL_H_VERSION__):
    pass
# END IF


from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA

if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF  __RPCNDR_H_VERSION__

    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF


if not defined(__wtypesbase_h__):
    # Forward Declarations
    # header files for imported files
    from pyWinAPI.shared.basetsd_h import * # NOQA
    from pyWinAPI.shared.guiddef_h import * # NOQA

    __ZERO__ = 0

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_wtypesbase_0000_0000
    # [local]
    # +
    # -------------------------------------------------------------------------
    # Microsoft Windows
    # Copyright (c) Microsoft Corporation. All rights reserved.
    # --------------------------------------------------------------------
    if _MSC_VER >= 1020:
        pass
    # END IF

    if _MSC_VER >= 1200:
        pass
    # END IF

    if not defined(__IWinTypesBase_INTERFACE_DEFINED__):
        # interface IWinTypesBase
        # [unique][version][uuid]

        if __ZERO__:
            WORD = USHORT
            BOOL = LONG
            DWORD = ULONG
            HANDLE = POINTER(VOID)
            LPWORD = POINTER(WORD)
            LPDWORD = POINTER(DWORD)

            # [string]
            LPSTR = POINTER(CHAR)

            # [string]
            LPCSTR = POINTER(CHAR)
            TCHAR = WCHAR

            # [string]
            LPWSTR = POINTER(WCHAR)

            # [string]
            LPTSTR = POINTER(TCHAR)

            # [string]
            LPCWSTR = POINTER(WCHAR)

            # [string]
            LPCTSTR = POINTER(TCHAR)
            LPHANDLE = POINTER(HANDLE)
        # END IF   0

        if defined(_WIN32) and not defined(OLE2ANSI):
            OLECHAR = WCHAR

            # [string]
            LPOLESTR = POINTER(OLECHAR)

            # [string]
            LPCOLESTR = POINTER(OLECHAR)
        else:
            OLECHAR = CHAR
            LPOLESTR = LPSTR
            LPCOLESTR = LPCSTR
        # END IF

        if not defined(_WINDEF_):
            if not defined(_MINWINDEF_):
                PVOID = POINTER(VOID)
                LPVOID = POINTER(VOID)
            # END IF  _MINWINDEF_
        # END IF  _WINDEF_

        ULONG = DWORD
        if not defined(_DWORDLONG_):
            DWORDLONG = INT64
            PDWORDLONG = POINTER(DWORDLONG)
        # END IF   not _DWORDLONG_

        if not defined(_ULONGLONG_):
            LONGLONG = INT64
            ULONGLONG = UINT64
            PLONGLONG = POINTER(LONGLONG)
            PULONGLONG = POINTER(ULONGLONG)
        # END IF   _ULONGLONG_

        if __ZERO__:
            _LARGE_INTEGER._fields_ = [
                ('QuadPart', LONGLONG),
            ]
            PLARGE_INTEGER = POINTER(LARGE_INTEGER)

            _ULARGE_INTEGER._fields_ = [
                ('QuadPart', ULONGLONG),
            ]
        # END IF   0

        if not defined(_WINBASE_):
            if not defined(_FILETIME_):
                _FILETIME._fields_ = [
                    ('dwLowDateTime', DWORD),
                    ('dwHighDateTime', DWORD),
                ]
                PFILETIME = POINTER(_FILETIME)

                LPFILETIME = POINTER(_FILETIME)

            # END IF   not _FILETIME

            if not defined(_SYSTEMTIME_):
                _SYSTEMTIME._fields_ = [
                    ('wYear', WORD),
                    ('wMonth', WORD),
                    ('wDayOfWeek', WORD),
                    ('wDay', WORD),
                    ('wHour', WORD),
                    ('wMinute', WORD),
                    ('wSecond', WORD),
                    ('wMilliseconds', WORD),
                ]
                PSYSTEMTIME = POINTER(_SYSTEMTIME)

                LPSYSTEMTIME = POINTER(_SYSTEMTIME)

            # END IF   not _SYSTEMTIME

            if not defined(_SECURITY_ATTRIBUTES_):
                _SECURITY_ATTRIBUTES._fields_ = [
                    ('nLength', DWORD),
                    ('lpSecurityDescriptor', LPVOID),
                    ('bInheritHandle', BOOL),
                ]
                PSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)

                LPSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)

            # END IF   not _SECURITY_ATTRIBUTES_

            if not defined(SECURITY_DESCRIPTOR_REVISION):
                SECURITY_DESCRIPTOR_CONTROL = USHORT
                PSECURITY_DESCRIPTOR_CONTROL = POINTER(USHORT)
                PSID = PVOID

                _ACL._fields_ = [
                    ('AclRevision', UCHAR),
                    ('Sbz1', UCHAR),
                    ('AclSize', USHORT),
                    ('AceCount', USHORT),
                    ('Sbz2', USHORT),
                ]
                PACL = POINTER(ACL)

                _SECURITY_DESCRIPTOR._fields_ = [
                    ('Revision', UCHAR),
                    ('Sbz1', UCHAR),
                    ('Control', SECURITY_DESCRIPTOR_CONTROL),
                    ('Owner', PSID),
                    ('Group', PSID),
                    ('Sacl', PACL),
                    ('Dacl', PACL),
                ]
                PISECURITY_DESCRIPTOR = POINTER(_SECURITY_DESCRIPTOR)

            # END IF   not SECURITY_DESCRIPTOR_REVISION
        # END IF  _WINBASE_

        _COAUTHIDENTITY._fields_ = [
            # [size_is]
            ('User', POINTER(USHORT)),
            # [range]
            ('UserLength', ULONG),
            # [size_is]
            ('Domain', POINTER(USHORT)),
            # [range]
            ('DomainLength', ULONG),
            # [size_is]
            ('Password', POINTER(USHORT)),
            # [range]
            ('PasswordLength', ULONG),
            ('Flags', ULONG),
        ]

        _COAUTHINFO._fields_ = [
            ('dwAuthnSvc', DWORD),
            ('dwAuthzSvc', DWORD),
            ('pwszServerPrincName', LPWSTR),
            ('dwAuthnLevel', DWORD),
            ('dwImpersonationLevel', DWORD),
            ('pAuthIdentityData', POINTER(COAUTHIDENTITY)),
            ('dwCapabilities', DWORD),
        ]
        SCODE = LONG
        PSCODE = POINTER(SCODE)
        if not defined(_HRESULT_DEFINED):
            if defined(__midl):
                HRESULT = LONG
            else:
                HRESULT = LONG

            # END IF   __midl
        # END IF   not _HRESULT_DEFINED

        if not defined(__OBJECTID_DEFINED):
            _OBJECTID._fields_ = [
                ('Lineage', GUID),
                ('Uniquifier', ULONG),
            ]
        # END IF   not _OBJECTID_DEFINED

        if __ZERO__:
            REFGUID = POINTER(GUID)
            REFIID = POINTER(IID)
            REFCLSID = POINTER(CLSID)
        # END IF   0


        class tagMEMCTX(ENUM):
            MEMCTX_TASK = 1
            MEMCTX_SHARED = 2
            MEMCTX_MACSYSTEM = 3
            MEMCTX_UNKNOWN = - 1
            MEMCTX_SAME = - 2

        MEMCTX = tagMEMCTX
        if not defined(_ROTREGFLAGS_DEFINED):
            pass
        # END IF   not _ROTREGFLAGS_DEFINED

        if not defined(_APPIDREGFLAGS_DEFINED):
            pass
        # END IF   not _APPIDREGFLAGS_DEFINED

        if not defined(_DCOMSCM_REMOTECALL_FLAGS_DEFINED):
            pass
        # END IF   not _DCOMSCM_REMOTECALL_FLAGS_DEFINED


        class tagCLSCTX(ENUM):
            CLSCTX_INPROC_SERVER = 0x1
            CLSCTX_INPROC_HANDLER = 0x2
            CLSCTX_LOCAL_SERVER = 0x4
            CLSCTX_INPROC_SERVER16 = 0x8
            CLSCTX_REMOTE_SERVER = 0x10
            CLSCTX_INPROC_HANDLER16 = 0x20
            CLSCTX_RESERVED1 = 0x40
            CLSCTX_RESERVED2 = 0x80
            CLSCTX_RESERVED3 = 0x100
            CLSCTX_RESERVED4 = 0x200
            CLSCTX_NO_CODE_DOWNLOAD = 0x400
            CLSCTX_RESERVED5 = 0x800
            CLSCTX_NO_CUSTOM_MARSHAL = 0x1000
            CLSCTX_ENABLE_CODE_DOWNLOAD = 0x2000
            CLSCTX_NO_FAILURE_LOG = 0x4000
            CLSCTX_DISABLE_AAA = 0x8000
            CLSCTX_ENABLE_AAA = 0x10000
            CLSCTX_FROM_DEFAULT_CONTEXT = 0x20000
            CLSCTX_ACTIVATE_32_BIT_SERVER = 0x40000
            CLSCTX_ACTIVATE_64_BIT_SERVER = 0x80000
            CLSCTX_ENABLE_CLOAKING = 0x100000
            CLSCTX_APPCONTAINER = 0x400000
            CLSCTX_ACTIVATE_AAA_AS_IU = 0x800000
            CLSCTX_PS_DLL = 0x80000000
        CLSCTX = tagCLSCTX


        class tagMSHLFLAGS(ENUM):
            MSHLFLAGS_NORMAL = 0
            MSHLFLAGS_TABLESTRONG = 1
            MSHLFLAGS_TABLEWEAK = 2
            MSHLFLAGS_NOPING = 4
            MSHLFLAGS_RESERVED1 = 8
            MSHLFLAGS_RESERVED2 = 16
            MSHLFLAGS_RESERVED3 = 32
            MSHLFLAGS_RESERVED4 = 64

        MSHLFLAGS = tagMSHLFLAGS


        class tagMSHCTX(ENUM):
            MSHCTX_LOCAL = 0
            MSHCTX_NOSHAREDMEM = 1
            MSHCTX_DIFFERENTMACHINE = 2
            MSHCTX_INPROC = 3
            MSHCTX_CROSSCTX = 4

        MSHCTX = tagMSHCTX

        _BYTE_BLOB._fields_ = [
            ('clSize', ULONG),
            # [size_is]
            ('abData', BYTE * 1),
        ]

        # [unique]
        UP_BYTE_BLOB = POINTER(BYTE_BLOB)

        _WORD_BLOB._fields_ = [
            ('clSize', ULONG),
            # [size_is]
            ('asData', USHORT * 1),
        ]

        # [unique]
        UP_WORD_BLOB = POINTER(WORD_BLOB)

        _DWORD_BLOB._fields_ = [
            ('clSize', ULONG),
            # [size_is]
            ('alData', ULONG * 1),
        ]

        # [unique]
        UP_DWORD_BLOB = POINTER(DWORD_BLOB)

        _FLAGGED_BYTE_BLOB._fields_ = [
            ('fFlags', ULONG),
            ('clSize', ULONG),
            # [size_is]
            ('abData', BYTE * 1),
        ]

        # [unique]
        UP_FLAGGED_BYTE_BLOB = POINTER(FLAGGED_BYTE_BLOB)

        _FLAGGED_WORD_BLOB._fields_ = [
            ('fFlags', ULONG),
            ('clSize', ULONG),
            # [size_is]
            ('asData', USHORT * 1),
        ]

        # [unique]
        UP_FLAGGED_WORD_BLOB = POINTER(FLAGGED_WORD_BLOB)

        _BYTE_SIZEDARR._fields_ = [
            ('clSize', ULONG),
            # [size_is]
            ('pData', POINTER(BYTE)),
        ]

        _SHORT_SIZEDARR._fields_ = [
            ('clSize', ULONG),
            # [size_is]
            ('pData', POINTER(USHORT)),
        ]

        _LONG_SIZEDARR._fields_ = [
            ('clSize', ULONG),
            # [size_is]
            ('pData', POINTER(ULONG)),
        ]

        _HYPER_SIZEDARR._fields_ = [
            ('clSize', ULONG),
            # [size_is]
            ('pData', POINTER(hyper)),
        ]
    # END IF  __IWinTypesBase_INTERFACE_DEFINED__

    # interface __MIDL_itf_wtypesbase_0000_0001
    # [local]
    if not defined(_tagBLOB_DEFINED):
        tagBLOB._fields_ = [
            ('cbSize', ULONG),
            # [size_is]
            ('pBlobData', POINTER(BYTE)),
        ]
        LPBLOB = POINTER(tagBLOB)

    # END IF

    if not defined(SID_IDENTIFIER_AUTHORITY_DEFINED):
        _SID_IDENTIFIER_AUTHORITY._fields_ = [
            ('Value', UCHAR * 6),
        ]
        PSID_IDENTIFIER_AUTHORITY = POINTER(_SID_IDENTIFIER_AUTHORITY)

    # END IF

    if not defined(SID_DEFINED):
        _SID._fields_ = [
            ('Revision', BYTE),
            ('SubAuthorityCount', BYTE),
            ('IdentifierAuthority', SID_IDENTIFIER_AUTHORITY),
            # [size_is]
            ('SubAuthority', ULONG * 1),
        ]
        PISID = POINTER(_SID)

        _SID_AND_ATTRIBUTES._fields_ = [
            ('Sid', POINTER(SID)),
            ('Attributes', DWORD),
        ]
        PSID_AND_ATTRIBUTES = POINTER(_SID_AND_ATTRIBUTES)

    # END IF

    if _MSC_VER >= 1200:
        pass
    # END IF

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


