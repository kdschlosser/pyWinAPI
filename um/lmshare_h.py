import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMSHARE_ = None
_LMSESSION_ = None
_LMCONNECTION_ = None
_LMFILE_ = None


class _SHARE_INFO_0(ctypes.Structure):
    pass


SHARE_INFO_0 = _SHARE_INFO_0
PSHARE_INFO_0 = POINTER(_SHARE_INFO_0)
LPSHARE_INFO_0 = POINTER(_SHARE_INFO_0)


class _SHARE_INFO_1(ctypes.Structure):
    pass


SHARE_INFO_1 = _SHARE_INFO_1
PSHARE_INFO_1 = POINTER(_SHARE_INFO_1)
LPSHARE_INFO_1 = POINTER(_SHARE_INFO_1)


class _SHARE_INFO_2(ctypes.Structure):
    pass


SHARE_INFO_2 = _SHARE_INFO_2
PSHARE_INFO_2 = POINTER(_SHARE_INFO_2)
LPSHARE_INFO_2 = POINTER(_SHARE_INFO_2)


class _SHARE_INFO_501(ctypes.Structure):
    pass


SHARE_INFO_501 = _SHARE_INFO_501
PSHARE_INFO_501 = POINTER(_SHARE_INFO_501)
LPSHARE_INFO_501 = POINTER(_SHARE_INFO_501)


class _SHARE_INFO_502(ctypes.Structure):
    pass


SHARE_INFO_502 = _SHARE_INFO_502
PSHARE_INFO_502 = POINTER(_SHARE_INFO_502)
LPSHARE_INFO_502 = POINTER(_SHARE_INFO_502)


class _SHARE_INFO_503(ctypes.Structure):
    pass


SHARE_INFO_503 = _SHARE_INFO_503
PSHARE_INFO_503 = POINTER(_SHARE_INFO_503)
LPSHARE_INFO_503 = POINTER(_SHARE_INFO_503)


class _SHARE_INFO_1004(ctypes.Structure):
    pass


SHARE_INFO_1004 = _SHARE_INFO_1004
PSHARE_INFO_1004 = POINTER(_SHARE_INFO_1004)
LPSHARE_INFO_1004 = POINTER(_SHARE_INFO_1004)


class _SHARE_INFO_1005(ctypes.Structure):
    pass


SHARE_INFO_1005 = _SHARE_INFO_1005
PSHARE_INFO_1005 = POINTER(_SHARE_INFO_1005)
LPSHARE_INFO_1005 = POINTER(_SHARE_INFO_1005)


class _SHARE_INFO_1006(ctypes.Structure):
    pass


SHARE_INFO_1006 = _SHARE_INFO_1006
PSHARE_INFO_1006 = POINTER(_SHARE_INFO_1006)
LPSHARE_INFO_1006 = POINTER(_SHARE_INFO_1006)


class _SHARE_INFO_1501(ctypes.Structure):
    pass


SHARE_INFO_1501 = _SHARE_INFO_1501
PSHARE_INFO_1501 = POINTER(_SHARE_INFO_1501)
LPSHARE_INFO_1501 = POINTER(_SHARE_INFO_1501)


class _SHARE_INFO_1503(ctypes.Structure):
    pass


SHARE_INFO_1503 = _SHARE_INFO_1503
PSHARE_INFO_1503 = POINTER(_SHARE_INFO_1503)
LPSHARE_INFO_1503 = POINTER(_SHARE_INFO_1503)


class _SERVER_ALIAS_INFO_0(ctypes.Structure):
    pass


SERVER_ALIAS_INFO_0 = _SERVER_ALIAS_INFO_0
PSERVER_ALIAS_INFO_0 = POINTER(_SERVER_ALIAS_INFO_0)
LPSERVER_ALIAS_INFO_0 = POINTER(_SERVER_ALIAS_INFO_0)


class _SESSION_INFO_0(ctypes.Structure):
    pass


SESSION_INFO_0 = _SESSION_INFO_0
PSESSION_INFO_0 = POINTER(_SESSION_INFO_0)
LPSESSION_INFO_0 = POINTER(_SESSION_INFO_0)


class _SESSION_INFO_1(ctypes.Structure):
    pass


SESSION_INFO_1 = _SESSION_INFO_1
PSESSION_INFO_1 = POINTER(_SESSION_INFO_1)
LPSESSION_INFO_1 = POINTER(_SESSION_INFO_1)


class _SESSION_INFO_2(ctypes.Structure):
    pass


SESSION_INFO_2 = _SESSION_INFO_2
PSESSION_INFO_2 = POINTER(_SESSION_INFO_2)
LPSESSION_INFO_2 = POINTER(_SESSION_INFO_2)


class _SESSION_INFO_10(ctypes.Structure):
    pass


SESSION_INFO_10 = _SESSION_INFO_10
PSESSION_INFO_10 = POINTER(_SESSION_INFO_10)
LPSESSION_INFO_10 = POINTER(_SESSION_INFO_10)


class _SESSION_INFO_502(ctypes.Structure):
    pass


SESSION_INFO_502 = _SESSION_INFO_502
PSESSION_INFO_502 = POINTER(_SESSION_INFO_502)
LPSESSION_INFO_502 = POINTER(_SESSION_INFO_502)


class _CONNECTION_INFO_0(ctypes.Structure):
    pass


CONNECTION_INFO_0 = _CONNECTION_INFO_0
PCONNECTION_INFO_0 = POINTER(_CONNECTION_INFO_0)
LPCONNECTION_INFO_0 = POINTER(_CONNECTION_INFO_0)


class _CONNECTION_INFO_1(ctypes.Structure):
    pass


CONNECTION_INFO_1 = _CONNECTION_INFO_1
PCONNECTION_INFO_1 = POINTER(_CONNECTION_INFO_1)
LPCONNECTION_INFO_1 = POINTER(_CONNECTION_INFO_1)


class _FILE_INFO_2(ctypes.Structure):
    pass


FILE_INFO_2 = _FILE_INFO_2
PFILE_INFO_2 = POINTER(_FILE_INFO_2)
LPFILE_INFO_2 = POINTER(_FILE_INFO_2)


class _FILE_INFO_3(ctypes.Structure):
    pass


FILE_INFO_3 = _FILE_INFO_3
PFILE_INFO_3 = POINTER(_FILE_INFO_3)
LPFILE_INFO_3 = POINTER(_FILE_INFO_3)




# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) 1990-1999 Microsoft Corporation Module Name: lmshare.h
# Abstract: This module defines the API function prototypes and data
# structures for the following groups of NT API functions: NetShare NetSession
# NetFile NetConnection Environment: User Mode - Win32 Notes: You must include
# <windef.h> and <lmcons.h> before this file. --
from pyWinAPI.shared.winapifamily_h import * # NOQA

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
    # SHARE API
    netapi32 = ctypes.windll.NETAPI32

    from pyWinAPI.shared.lmcons_h import *  # NOQA

    if not defined(_LMSHARE_):
        _LMSHARE_ = VOID

        from pyWinAPI.um.winnt_h import * # NOQA
        if _MSC_VER > 1000:
            pass
        # END IF

        if defined(__cplusplus):
            pass
        # END IF

        # // Function Prototypes - Share
        #
        #
        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetShareAdd(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _When_( level ==  2, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_2)) )
        # _When_( level ==  502, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_502)) )
        # _When_( level ==  503, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_503)) )
        # LPBYTE buf,
        # _Out_opt_ LPDWORD parm_err
        # );
        NetShareAdd = netapi32.NetShareAdd
        NetShareAdd.restype = NET_API_STATUS

        # _Check_return_
        # _Success_( return == 0 or return == ERROR_MORE_DATA )
        # NET_API_STATUS NET_API_FUNCTION
        # NetShareEnum(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _When_( level == 0,_Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SHARE_INFO_0)) )
        # _When_( level == 1, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SHARE_INFO_1)) )
        # _When_( level == 2, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SHARE_INFO_2)) )
        # _When_( level == 502, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SHARE_INFO_502)) )
        # _When_( level == 503, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SHARE_INFO_503)) )
        # LPBYTE *bufptr,
        # _In_ DWORD prefmaxlen,
        # _Out_ LPDWORD entriesread,
        # _Out_ LPDWORD totalentries,
        # _Inout_opt_ LPDWORD resume_handle
        # );
        NetShareEnum = netapi32.NetShareEnum
        NetShareEnum.restype = NET_API_STATUS

        # _Check_return_
        # _Success_( return == 0 or return == ERROR_MORE_DATA )
        # NET_API_STATUS NET_API_FUNCTION
        # NetShareEnumSticky(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _When_( level == 0, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SHARE_INFO_0)) )
        # _When_( level == 1, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SHARE_INFO_1)) )
        # _When_( level == 2, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SHARE_INFO_2)) )
        # _When_( level == 502, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SHARE_INFO_502)) )
        # _When_( level == 503, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SHARE_INFO_503)) )
        # LPBYTE *bufptr,
        # _In_ DWORD prefmaxlen,
        # _Out_ LPDWORD entriesread,
        # _Out_ LPDWORD totalentries,
        # _Inout_opt_ LPDWORD resume_handle
        # );
        NetShareEnumSticky = netapi32.NetShareEnumSticky
        NetShareEnumSticky.restype = NET_API_STATUS

        # _Check_return_
        # _Success_( return == 0 or return == ERROR_MORE_DATA )
        # NET_API_STATUS NET_API_FUNCTION
        # NetShareGetInfo(
        # _In_opt_ LMSTR servername,
        # _In_ LMSTR netname,
        # _In_ DWORD level,
        # _When_( level == 0, _Outptr_result_bytebuffer_((ctypes.sizeof(SHARE_INFO_0)) )
        # _When_( level == 1, _Outptr_result_bytebuffer_((ctypes.sizeof(SHARE_INFO_1)) )
        # _When_( level == 2, _Outptr_result_bytebuffer_((ctypes.sizeof(SHARE_INFO_2)) )
        # _When_( level == 501, _Outptr_result_bytebuffer_((ctypes.sizeof(SHARE_INFO_501)) )
        # _When_( level == 502, _Outptr_result_bytebuffer_((ctypes.sizeof(SHARE_INFO_502)) )
        # _When_( level == 503, _Outptr_result_bytebuffer_((ctypes.sizeof(SHARE_INFO_503)) )
        # _When_( level == 1005, _Outptr_result_bytebuffer_((ctypes.sizeof(SHARE_INFO_1005)) )
        # LPBYTE *bufptr
        # );
        NetShareGetInfo = netapi32.NetShareGetInfo
        NetShareGetInfo.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetShareSetInfo(
        # _In_opt_ LMSTR servername,
        # _In_ LMSTR netname,
        # _In_ DWORD level,
        # _When_( level == 1, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_1)) )
        # _When_( level == 2, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_2)) )
        # _When_( level == 502, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_502)) )
        # _When_( level == 503, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_503)) )
        # _When_( level == 1004, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_1004)) )
        # _When_( level == 1005, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_1005)) )
        # _When_( level == 1006, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_1006)) )
        # _When_( level == 1501, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_1501)) )
        # LPBYTE  buf,
        # _Out_opt_ LPDWORD parm_err
        # );
        NetShareSetInfo = netapi32.NetShareSetInfo
        NetShareSetInfo.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetShareDel(
        # _In_opt_ LMSTR servername,
        # _In_ LMSTR netname,
        # _Reserved_ DWORD reserved
        # );
        NetShareDel = netapi32.NetShareDel
        NetShareDel.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetShareDelSticky(
        # _In_opt_ LMSTR servername,
        # _In_ LMSTR netname,
        # _Reserved_ DWORD reserved
        # );
        NetShareDelSticky = netapi32.NetShareDelSticky
        NetShareDelSticky.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetShareCheck(
        # _In_opt_ LMSTR servername,
        # _In_ LMSTR device,
        # _Out_ LPDWORD type
        # );
        NetShareCheck = netapi32.NetShareCheck
        NetShareCheck.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetShareDelEx(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _When_( level == 0, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_0)) )
        # _When_( level == 1, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_1)) )
        # _When_( level == 2, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_2)) )
        # _When_( level == 502, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_502)) )
        # _When_( level == 503, _In_reads_bytes_((ctypes.sizeof(SHARE_INFO_503)) )
        # LPBYTE buf
        # );
        NetShareDelEx = netapi32.NetShareDelEx
        NetShareDelEx.restype = NET_API_STATUS

        # Data Structures - Share
        _SHARE_INFO_0._fields_ = [
            ('shi0_netname', LMSTR),
        ]
        _SHARE_INFO_1._fields_ = [
            ('shi1_netname', LMSTR),
            ('shi1_type', DWORD),
            ('shi1_remark', LMSTR),
        ]
        _SHARE_INFO_2._fields_ = [
            ('shi2_netname', LMSTR),
            ('shi2_type', DWORD),
            ('shi2_remark', LMSTR),
            ('shi2_permissions', DWORD),
            ('shi2_max_uses', DWORD),
            ('shi2_current_uses', DWORD),
            ('shi2_path', LMSTR),
            ('shi2_passwd', LMSTR),
        ]
        _SHARE_INFO_501._fields_ = [
            ('shi501_netname', LMSTR),
            ('shi501_type', DWORD),
            ('shi501_remark', LMSTR),
            ('shi501_flags', DWORD),
        ]
        _SHARE_INFO_502._fields_ = [
            ('shi502_netname', LMSTR),
            ('shi502_type', DWORD),
            ('shi502_remark', LMSTR),
            ('shi502_permissions', DWORD),
            ('shi502_max_uses', DWORD),
            ('shi502_current_uses', DWORD),
            ('shi502_path', LMSTR),
            ('shi502_passwd', LMSTR),
            ('shi502_reserved', DWORD),
            ('shi502_security_descriptor', PSECURITY_DESCRIPTOR),
        ]
        _SHARE_INFO_503._fields_ = [
            ('shi503_netname', LMSTR),
            ('shi503_type', DWORD),
            ('shi503_remark', LMSTR),
            ('shi503_permissions', DWORD),
            ('shi503_max_uses', DWORD),
            ('shi503_current_uses', DWORD),
            ('shi503_path', LMSTR),
            ('shi503_passwd', LMSTR),
            ('shi503_servername', LMSTR),
            ('shi503_reserved', DWORD),
            ('shi503_security_descriptor', PSECURITY_DESCRIPTOR),
        ]
        _SHARE_INFO_1004._fields_ = [
            ('shi1004_remark', LMSTR),
        ]
        _SHARE_INFO_1005._fields_ = [
            ('shi1005_flags', DWORD),
        ]
        _SHARE_INFO_1006._fields_ = [
            ('shi1006_max_uses', DWORD),
        ]
        _SHARE_INFO_1501._fields_ = [
            ('shi1501_reserved', DWORD),
            ('shi1501_security_descriptor', PSECURITY_DESCRIPTOR),
        ]
        _SHARE_INFO_1503._fields_ = [
            ('shi1503_sharefilter', GUID),
        ]
        # NetShareAlias functions
        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerAliasAdd(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _In_reads_bytes_((ctypes.sizeof(SERVER_ALIAS_INFO_0)) LPBYTE buf
        # );
        NetServerAliasAdd = netapi32.NetServerAliasAdd
        NetServerAliasAdd.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerAliasDel(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _When_( level == 0, _In_reads_bytes_((ctypes.sizeof(SERVER_ALIAS_INFO_0_CONTAINER)) )
        # LPBYTE buf
        # );
        NetServerAliasDel = netapi32.NetServerAliasDel
        NetServerAliasDel.restype = NET_API_STATUS

        # _Check_return_
        # _Success_( return == 0 or return == ERROR_MORE_DATA )
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerAliasEnum(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _When_( level == 0, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SERVER_ALIAS_INFO_0_CONTAINER)) )
        # LPBYTE *bufptr,
        # _In_ DWORD prefmaxlen,
        # _Out_ LPDWORD entriesread,
        # _Out_ LPDWORD totalentries,
        # _Inout_opt_ LPDWORD resumehandle
        # );
        NetServerAliasEnum = netapi32.NetServerAliasEnum
        NetServerAliasEnum.restype = NET_API_STATUS

        _SERVER_ALIAS_INFO_0._fields_ = [
            ('srvai0_alias', LMSTR),
            ('srvai0_target', LMSTR),
            ('srvai0_default', BOOLEAN),
            ('srvai0_reserved', ULONG),
        ]
        # Special Values and Constants - Share
        # Values for parm_err parameter.
        SHARE_NETNAME_PARMNUM = 1
        SHARE_TYPE_PARMNUM = 3
        SHARE_REMARK_PARMNUM = 4
        SHARE_PERMISSIONS_PARMNUM = 5
        SHARE_MAX_USES_PARMNUM = 6
        SHARE_CURRENT_USES_PARMNUM = 7
        SHARE_PATH_PARMNUM = 8
        SHARE_PASSWD_PARMNUM = 9
        SHARE_FILE_SD_PARMNUM = 501
        SHARE_SERVER_PARMNUM = 503
        # Single-field infolevels for NetShareSetInfo.
        SHARE_REMARK_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SHARE_REMARK_PARMNUM
        )
        SHARE_MAX_USES_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SHARE_MAX_USES_PARMNUM
        )
        SHARE_FILE_SD_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SHARE_FILE_SD_PARMNUM
        )
        SHI1_NUM_ELEMENTS = 4
        SHI2_NUM_ELEMENTS = 10
        # Share types (shi1_type and shi2_type fields).
        STYPE_DISKTREE = 0
        STYPE_PRINTQ = 1
        STYPE_DEVICE = 2
        STYPE_IPC = 3
        STYPE_MASK = 0x000000FF  # AND with shi_type to
        STYPE_RESERVED1 = 0x01000000  # Reserved for internal processing
        STYPE_RESERVED2 = 0x02000000
        STYPE_RESERVED3 = 0x04000000
        STYPE_RESERVED4 = 0x08000000
        STYPE_RESERVED5 = 0x00100000
        STYPE_RESERVED_ALL = 0x3FFFFF00
        STYPE_TEMPORARY = 0x40000000
        STYPE_SPECIAL = 0x80000000
        SHI_USES_UNLIMITED = -1
        # Flags values for the 501 and 1005 levels
        SHI1005_FLAGS_DFS = 0x0001  # Share is in the DFS
        SHI1005_FLAGS_DFS_ROOT = 0x0002  # Share is root of DFS
        # Used to mask off the following states
        # (including SHI1005_FLAGS_ENABLE_HASH)
        CSC_MASK_EXT = 0x2030
        CSC_MASK = 0x0030  # Used to mask off the following states
        CSC_CACHE_MANUAL_REINT = 0x0000  # No automatic file by file reintegration
        CSC_CACHE_AUTO_REINT = 0x0010  # File by file reintegration is OK
        CSC_CACHE_VDO = 0x0020  # no need to flow opens
        CSC_CACHE_NONE = 0x0030  # no CSC for this share
        SHI1005_FLAGS_RESTRICT_EXCLUSIVE_OPENS = 0x00100  # Used to disallow read-deny read behavior
        SHI1005_FLAGS_FORCE_SHARED_DELETE = 0x00200  # Used to allows force shared delete
        SHI1005_FLAGS_ALLOW_NAMESPACE_CACHING = 0x00400  # The clients may cache the namespace
        SHI1005_FLAGS_ACCESS_BASED_DIRECTORY_ENUM = 0x00800  # Trim visible files in enumerations based on access
        SHI1005_FLAGS_FORCE_LEVELII_OPLOCK = 0x01000  # Only issue level2 oplock
        SHI1005_FLAGS_ENABLE_HASH = 0x02000  # Enable hash generation and retrieval requests from share
        SHI1005_FLAGS_ENABLE_CA = 0x04000  # Enable continuously available
        SHI1005_FLAGS_ENCRYPT_DATA = 0x08000  # Require encryption
        SHI1005_FLAGS_RESERVED = 0x10000  # Reserved for internal use
        SHI1005_FLAGS_DISABLE_CLIENT_BUFFERING = 0x20000  # Used to set the allowed client buffering
        SHI1005_FLAGS_IDENTITY_REMOTING = 0x40000  # Allows auth tunneling
        SHI1005_FLAGS_CLUSTER_MANAGED = 0x80000  # Used to prevent share from being modified by users
        # The subset of 1005 infolevel flags that can be set via the API
        SHI1005_VALID_FLAGS_SET = (
            CSC_MASK |
            SHI1005_FLAGS_RESTRICT_EXCLUSIVE_OPENS |
            SHI1005_FLAGS_FORCE_SHARED_DELETE |
            SHI1005_FLAGS_ALLOW_NAMESPACE_CACHING |
            SHI1005_FLAGS_ACCESS_BASED_DIRECTORY_ENUM |
            SHI1005_FLAGS_FORCE_LEVELII_OPLOCK |
            SHI1005_FLAGS_ENABLE_HASH |
            SHI1005_FLAGS_ENABLE_CA |
            SHI1005_FLAGS_ENCRYPT_DATA |
            SHI1005_FLAGS_DISABLE_CLIENT_BUFFERING |
            SHI1005_FLAGS_IDENTITY_REMOTING |
            SHI1005_FLAGS_CLUSTER_MANAGED |
            SHI1005_FLAGS_RESERVED
        )
        # END IF   _LMSHARE_
        # SESSION API
    if not defined(_LMSESSION_):
        _LMSESSION_ = VOID

        # Function Prototypes Session

        # _Check_return_
        # _Success_( return == 0 or return == ERROR_MORE_DATA )
        # NET_API_STATUS NET_API_FUNCTION
        # NetSessionEnum(
        # _In_opt_ LMSTR servername,
        # _In_opt_ LMSTR UncClientName,
        # _In_opt_ LMSTR username,
        # _In_ DWORD level,
        # _When_( level ==  0, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SESSION_INFO_0)) )
        # _When_( level ==  1, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SESSION_INFO_1)) )
        # _When_( level ==  2, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SESSION_INFO_2)) )
        # _When_( level ==  10, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SESSION_INFO_10)) )
        # _When_( level ==  502, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SESSION_INFO_502)) )
        # LPBYTE *bufptr,
        # _In_ DWORD prefmaxlen,
        # _Out_ LPDWORD entriesread,
        # _Out_ LPDWORD totalentries,
        # _Inout_opt_ LPDWORD resume_handle
        # );
        NetSessionEnum = netapi32.NetSessionEnum
        NetSessionEnum.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetSessionDel(
        # _In_opt_ LMSTR servername,
        # _In_opt_ LMSTR UncClientName,
        # _In_opt_ LMSTR username
        # );
        NetSessionDel = netapi32.NetSessionDel
        NetSessionDel.restype = NET_API_STATUS

        # _Check_return_
        # _Success_( return == 0 )
        # NET_API_STATUS NET_API_FUNCTION
        # NetSessionGetInfo(
        # _In_opt_ LMSTR servername,
        # _In_ LMSTR UncClientName,
        # _In_ LMSTR username,
        # _In_ DWORD level,
        # _When_( level == 0, _Outptr_result_bytebuffer_((ctypes.sizeof(SESSION_INFO_0)) )
        # _When_( level == 1, _Outptr_result_bytebuffer_((ctypes.sizeof(SESSION_INFO_1)) )
        # _When_( level == 2, _Outptr_result_bytebuffer_((ctypes.sizeof(SESSION_INFO_2)) )
        # _When_( level == 10, _Outptr_result_bytebuffer_((ctypes.sizeof(SESSION_INFO_10)) )
        # LPBYTE *bufptr
        # );
        NetSessionGetInfo = netapi32.NetSessionGetInfo
        NetSessionGetInfo.restype = NET_API_STATUS

        # Data Structures - Session
        # client name (no backslashes)
        _SESSION_INFO_0._fields_ = [
            ('sesi0_cname', LMSTR),
        ]
        # client name (no backslashes)
        _SESSION_INFO_1._fields_ = [
            ('sesi1_cname', LMSTR),
            ('sesi1_username', LMSTR),
            ('sesi1_num_opens', DWORD),
            ('sesi1_time', DWORD),
            ('sesi1_idle_time', DWORD),
            ('sesi1_user_flags', DWORD),
        ]
        # client name (no backslashes)
        _SESSION_INFO_2._fields_ = [
            ('sesi2_cname', LMSTR),
            ('sesi2_username', LMSTR),
            ('sesi2_num_opens', DWORD),
            ('sesi2_time', DWORD),
            ('sesi2_idle_time', DWORD),
            ('sesi2_user_flags', DWORD),
            ('sesi2_cltype_name', LMSTR),
        ]
        # client name (no backslashes)
        _SESSION_INFO_10._fields_ = [
            ('sesi10_cname', LMSTR),
            ('sesi10_username', LMSTR),
            ('sesi10_time', DWORD),
            ('sesi10_idle_time', DWORD),
        ]
        # client name (no backslashes)
        _SESSION_INFO_502._fields_ = [
            ('sesi502_cname', LMSTR),
            ('sesi502_username', LMSTR),
            ('sesi502_num_opens', DWORD),
            ('sesi502_time', DWORD),
            ('sesi502_idle_time', DWORD),
            ('sesi502_user_flags', DWORD),
            ('sesi502_cltype_name', LMSTR),
            ('sesi502_transport', LMSTR),
        ]
        # Special Values and Constants - Session
        # Bits defined in sesi1_user_flags.
        SESS_GUEST = 0x00000001  # session is logged on as a guest
        SESS_NOENCRYPTION = 0x00000002  # session is not using encryption
        SESI1_NUM_ELEMENTS = 8
        SESI2_NUM_ELEMENTS = 9
    # END IF   _LMSESSION_
    # CONNECTION API

    if not defined(_LMCONNECTION_):
        _LMCONNECTION_ = VOID
        # Function Prototypes - CONNECTION

        # _Check_return_
        # _Success_( return == 0  or return == ERROR_MORE_DATA )
        # NET_API_STATUS NET_API_FUNCTION
        # NetConnectionEnum(
        # _In_opt_ LMSTR servername,
        # _In_ LMSTR qualifier,
        # _In_ DWORD level,
        # _When_( level == 0, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(CONNECTION_INFO_0)) )
        # _When_( level == 1, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(CONNECTION_INFO_1)) )
        # LPBYTE *bufptr,
        # _In_ DWORD prefmaxlen,
        # _Out_ LPDWORD entriesread,
        # _Out_ LPDWORD totalentries,
        # _Inout_opt_ LPDWORD resume_handle
        # );
        NetConnectionEnum = netapi32.NetConnectionEnum
        NetConnectionEnum.restype = NET_API_STATUS

        # Data Structures - CONNECTION
        _CONNECTION_INFO_0._fields_ = [
            ('coni0_id', DWORD),
        ]
        _CONNECTION_INFO_1._fields_ = [
            ('coni1_id', DWORD),
            ('coni1_type', DWORD),
            ('coni1_num_opens', DWORD),
            ('coni1_num_users', DWORD),
            ('coni1_time', DWORD),
            ('coni1_username', LMSTR),
            ('coni1_netname', LMSTR),
        ]
        # END IF   _LMCONNECTION_
        # FILE API
    if not defined(_LMFILE_):
        _LMFILE_ = VOID
        # Function Prototypes - FILE

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetFileClose(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD fileid
        # );
        NetFileClose = netapi32.NetFileClose
        NetFileClose.restype = NET_API_STATUS

        # _Check_return_
        # _Success_( return == 0 or return == ERROR_MORE_DATA )
        # NET_API_STATUS NET_API_FUNCTION
        # NetFileEnum(
        # _In_opt_ LMSTR servername,
        # _In_opt_ LMSTR basepath,
        # _In_opt_ LMSTR username,
        # _In_ DWORD level,
        # _When_( level == 2, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(FILE_INFO_2)) )
        # _When_( level == 3, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(FILE_INFO_3)) )
        # LPBYTE *bufptr,
        # _In_ DWORD prefmaxlen,
        # _Out_ LPDWORD entriesread,
        # _Out_ LPDWORD totalentries,
        # _Inout_opt_ PDWORD_PTR resume_handle
        # );
        NetFileEnum = netapi32.NetFileEnum
        NetFileEnum.restype = NET_API_STATUS

        # _Check_return_
        # _Success_( return == 0)
        # NET_API_STATUS NET_API_FUNCTION
        # NetFileGetInfo(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD fileid,
        # _In_ DWORD level,
        # _When_( level == 2, _Outptr_result_bytebuffer_((ctypes.sizeof(FILE_INFO_2)) )
        # _When_( level == 3, _Outptr_result_bytebuffer_((ctypes.sizeof(FILE_INFO_3)) )
        # LPBYTE *bufptr
        # );
        NetFileGetInfo = netapi32.NetFileGetInfo
        NetFileGetInfo.restype = NET_API_STATUS

        # Data Structures - File
        # File APIs are available at information levels 2 & 3 only. Levels
        # 0 &
        # 1 are not supported.
        _FILE_INFO_2._fields_ = [
            ('fi2_id', DWORD),
        ]
        _FILE_INFO_3._fields_ = [
            ('fi3_id', DWORD),
            ('fi3_permissions', DWORD),
            ('fi3_num_locks', DWORD),
            ('fi3_pathname', LMSTR),
            ('fi3_username', LMSTR),
        ]
        # Special Values and Constants - File
        # bit values for permissions
        PERM_FILE_READ = 0x1  # user has read access
        PERM_FILE_WRITE = 0x2  # user has write access
        PERM_FILE_CREATE = 0x4  # user has create access

        if defined(__cplusplus):
            pass
        # END IF
    # END IF   _LMFILE_
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)


