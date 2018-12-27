import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMUSE_ = None

class _USE_INFO_0(ctypes.Structure):
    pass


USE_INFO_0 = _USE_INFO_0
PUSE_INFO_0 = POINTER(_USE_INFO_0)
LPUSE_INFO_0 = POINTER(_USE_INFO_0)


class _USE_INFO_1(ctypes.Structure):
    pass


USE_INFO_1 = _USE_INFO_1
PUSE_INFO_1 = POINTER(_USE_INFO_1)
LPUSE_INFO_1 = POINTER(_USE_INFO_1)


class _USE_INFO_2(ctypes.Structure):
    pass


USE_INFO_2 = _USE_INFO_2
PUSE_INFO_2 = POINTER(_USE_INFO_2)
LPUSE_INFO_2 = POINTER(_USE_INFO_2)


class _USE_INFO_3(ctypes.Structure):
    pass


USE_INFO_3 = _USE_INFO_3
PUSE_INFO_3 = POINTER(_USE_INFO_3)
LPUSE_INFO_3 = POINTER(_USE_INFO_3)


class _USE_INFO_4(ctypes.Structure):
    pass


USE_INFO_4 = _USE_INFO_4
PUSE_INFO_4 = POINTER(_USE_INFO_4)
LPUSE_INFO_4 = POINTER(_USE_INFO_4)


class _USE_INFO_5(ctypes.Structure):
    pass


USE_INFO_5 = _USE_INFO_5
PUSE_INFO_5 = POINTER(_USE_INFO_5)
LPUSE_INFO_5 = POINTER(_USE_INFO_5)


# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmuse.c Abstract:
# This file contains structures, function prototypes, and definitions for the
# NetUse API. Environment: User Mode - Win32 Portable to any flat, 32-bit
# environment. (Uses Win32 typedefs.) Requires ANSI C extensions: slash-slash
# comments, LONG external names. Notes: You must include NETCONS.H before this
# file, since this file depends on values defined in NETCONS.H. --
if not defined(_LMUSE_):
    _LMUSE_ = VOID

    netapi32 = ctypes.windll.NETAPI32

    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if defined(__cplusplus):
            pass
        # END IF

        from pyWinAPI.shared.lmcons_h import * # NOQA
        from pyWinAPI.um.lmuseflg_h import * # NOQA

        # // LevelFlags : The lower 16 bits describe the use level while the upper 16 bits are flags.
        #
        #
        #
        USE_FLAG_GLOBAL_MAPPING = 0x10000

        def USE_LEVEL(LEVELFLAGS):
            return LEVELFLAGS & 0xffff


        def USE_FLAGS(LEVELFLAGS):
            return LEVELFLAGS & 0xffff0000

        # // Function Prototypes
        #
        #
        # NET_API_STATUS NET_API_FUNCTION
        # NetUseAdd(
        # _In_opt_ LPTSTR servername,
        # _In_ DWORD LevelFlags,
        # _When_( USE_LEVEL(LevelFlags)== 0, _In_reads_bytes_((ctypes.sizeof(USE_INFO_0)))
        # _When_( USE_LEVEL(LevelFlags)== 1, _In_reads_bytes_((ctypes.sizeof(USE_INFO_1)))
        # _When_( USE_LEVEL(LevelFlags)== 2, _In_reads_bytes_((ctypes.sizeof(USE_INFO_2)))
        # _When_( USE_LEVEL(LevelFlags)== 3, _In_reads_bytes_((ctypes.sizeof(USE_INFO_3)))
        # _When_( USE_LEVEL(LevelFlags)== 4, _In_reads_bytes_((ctypes.sizeof(USE_INFO_4)))
        # _When_( USE_LEVEL(LevelFlags)== 5, _In_reads_bytes_((ctypes.sizeof(USE_INFO_5)))
        # LPBYTE buf,
        # _Out_opt_ LPDWORD parm_err
        # );
        NetUseAdd = netapi32.NetUseAdd
        NetUseAdd.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUseDel(
        # _In_opt_ LMSTR  UncServerName OPTIONAL,
        # _In_ LMSTR  UseName,
        # _In_ DWORD ForceLevelFlags
        # );
        NetUseDel = netapi32.NetUseDel
        NetUseDel.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUseEnum(
        # _In_opt_ LMSTR  UncServerName,
        # _In_ DWORD LevelFlags,
        # _Outptr_opt_result_buffer_(_Inexpressible_(EntriesRead)) LPBYTE *BufPtr,
        # _In_ DWORD PreferedMaximumSize,
        # _Out_opt_ LPDWORD EntriesRead,
        # _Out_ LPDWORD TotalEntries,
        # _Inout_opt_ LPDWORD ResumeHandle
        # );
        NetUseEnum = netapi32.NetUseEnum
        NetUseEnum.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUseGetInfo(
        # _In_opt_ LMSTR  UncServerName,
        # _In_ LMSTR  UseName,
        # _In_ DWORD LevelFlags,
        # _When_(USE_LEVEL(LevelFlags) == 0, _Outptr_opt_result_bytebuffer_((ctypes.sizeof(USE_INFO_0)))
        # _When_(USE_LEVEL(LevelFlags) == 1, _Outptr_opt_result_bytebuffer_((ctypes.sizeof(USE_INFO_1)))
        # _When_(USE_LEVEL(LevelFlags) == 2, _Outptr_opt_result_bytebuffer_((ctypes.sizeof(USE_INFO_2)))
        # LPBYTE *bufptr
        # );
        NetUseGetInfo = netapi32.NetUseGetInfo
        NetUseGetInfo.restype = NET_API_STATUS

        # Data Structures
        _USE_INFO_0._fields_ = [
            ('ui0_local', LMSTR),
            ('ui0_remote', LMSTR),
        ]
        _USE_INFO_1._fields_ = [
            ('ui1_local', LMSTR),
            ('ui1_remote', LMSTR),
            ('ui1_password', LMSTR),
            ('ui1_status', DWORD),
            ('ui1_asg_type', DWORD),
            ('ui1_refcount', DWORD),
            ('ui1_usecount', DWORD),
        ]
        _USE_INFO_2._fields_ = [
            ('ui2_local', LMSTR),
            ('ui2_remote', LMSTR),
            ('ui2_password', LMSTR),
            ('ui2_status', DWORD),
            ('ui2_asg_type', DWORD),
            ('ui2_refcount', DWORD),
            ('ui2_usecount', DWORD),
            ('ui2_username', LMSTR),
            ('ui2_domainname', LMSTR),
        ]
        _USE_INFO_3._fields_ = [
            ('ui3_ui2', USE_INFO_2),
            ('ui3_flags', ULONG),
        ]
        _USE_INFO_4._fields_ = [
            ('ui4_ui3', USE_INFO_3),
            ('ui4_auth_identity_length', DWORD),
            ('ui4_auth_identity', PBYTE),
        ]
        _USE_INFO_5._fields_ = [
            ('ui4_ui3', USE_INFO_3),
            ('ui4_auth_identity_length', DWORD),
            ('ui4_auth_identity', PBYTE),
            ('ui5_security_descriptor_length', DWORD),
            ('ui5_security_descriptor', PBYTE),
            ('ui5_use_options_length', DWORD),
            ('ui5_use_options', PBYTE),
        ]
        # Special Values and Constants
        # One of these values indicates the parameter within an information
        # structure that is invalid when ERROR_INVALID_PARAMETER is
        # returned by
        # NetUseAdd.
        USE_LOCAL_PARMNUM = 1
        USE_REMOTE_PARMNUM = 2
        USE_PASSWORD_PARMNUM = 3
        USE_ASGTYPE_PARMNUM = 4
        USE_USERNAME_PARMNUM = 5
        USE_DOMAINNAME_PARMNUM = 6
        USE_FLAGS_PARMNUM = 7
        USE_AUTHIDENTITY_PARMNUM = 8
        USE_SD_PARMNUM = 9
        USE_OPTIONS_PARMNUM = 10
        # Values appearing in the ui1_status field of use_info_1 structure.
        # Note that USE_SESSLOST and USE_DISCONN are synonyms.
        USE_OK = 0
        USE_PAUSED = 1
        USE_SESSLOST = 2
        USE_DISCONN = 2
        USE_NETERR = 3
        USE_CONN = 4
        USE_RECONN = 5
        # Values of the ui1_asg_type field of use_info_1 structure
        USE_WILDCARD = (-1)
        USE_DISKDEV = 0
        USE_SPOOLDEV = 1
        USE_CHARDEV = 2
        USE_IPC = 3
        # Flags defined in the use_info_3 structure
        CREATE_NO_CONNECT = 0x1  # creation flags
        CREATE_BYPASS_CSC = 0x2  # force connection to server, bypassing CSC
        # all ops on this connection go to the server,
        # never to the cache
        CREATE_CRED_RESET = 0x4  # Create a connection with credentials passed in
        # this netuse if none exist. If connection already
        # exists then update credentials after issuing remote
        # tree connection. This is needed as CSC cannot verify
        # credentials while offline.
        USE_DEFAULT_CREDENTIALS = 0x4  # No explicit credentials passed to NetUseAdd
        CREATE_REQUIRE_CONNECTION_INTEGRITY = 0x8
        CREATE_REQUIRE_CONNECTION_PRIVACY = 0x10

        if defined(__cplusplus):
            pass
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF   _LMUSE_


