import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMREMUTL_ = None
DESC_CHAR_UNICODE = None

class _TIME_OF_DAY_INFO(ctypes.Structure):
    pass


TIME_OF_DAY_INFO = _TIME_OF_DAY_INFO
PTIME_OF_DAY_INFO = POINTER(_TIME_OF_DAY_INFO)
LPTIME_OF_DAY_INFO = POINTER(_TIME_OF_DAY_INFO)


# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmremutl.h
# Abstract: This file contains structures, function prototypes, and
# definitions for the NetRemote API. Environment: User Mode - Win32 Portable
# to any flat, 32-bit environment. (Uses Win32 typedefs.) Requires ANSI C
# extensions: slash-slash comments, LONG external names. --
if not defined(_LMREMUTL_):
    _LMREMUTL_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.shared.lmcons_h import *  # NOQA

    netapi32 = ctypes.windll.NETAPI32

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if defined(__cplusplus):
            pass
        # END IF

        # Type Definitions
        if not defined(DESC_CHAR_UNICODE):
            DESC_CHAR = CHAR
            LPDESC = LPSTR
        else:
            DESC_CHAR = WCHAR
            LPDESC = LPWSTR
        # END IF   DESC_CHAR_UNICODE is defined

        # Function Prototypes

        # _Check_return_
        # _Success_( return == 0 )
        # NET_API_STATUS NET_API_FUNCTION
        # NetRemoteTOD(
        # _In_opt_ LPCWSTR UncServerName,
        # _Outptr_result_bytebuffer_((ctypes.sizeof(TIME_OF_DAY_INFO)) LPBYTE *BufferPtr
        # );
        NetRemoteTOD = netapi32.NetRemoteTOD
        NetRemoteTOD.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetRemoteComputerSupports(
        # IN LPCWSTR UncServerName OPTIONAL, // Must start with "\\".
        # IN DWORD OptionsWanted, // Set SUPPORTS_ bits wanted.
        # OUT LPDWORD OptionsSupported // Supported features, masked.
        # );
        NetRemoteComputerSupports = netapi32.NetRemoteComputerSupports
        NetRemoteComputerSupports.restype = NET_API_STATUS
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # NET_API_STATUS
        # __cdecl
        # RxRemoteApi(
        # IN DWORD ApiNumber,
        # _In_ IN LPCWSTR UncServerName, // Required, with \\name.
        # _In_ IN LPDESC ParmDescString,
        # _In_opt_ IN LPDESC DataDesc16 OPTIONAL,
        # _In_opt_ IN LPDESC DataDesc32 OPTIONAL,
        # _In_opt_ IN LPDESC DataDescSmb OPTIONAL,
        # _In_opt_ IN LPDESC AuxDesc16 OPTIONAL,
        # _In_opt_ IN LPDESC AuxDesc32 OPTIONAL,
        # _In_opt_ IN LPDESC AuxDescSmb OPTIONAL,
        # IN DWORD  Flags,
        # ... // rest of API's arguments
        # );
        RxRemoteApi = netapi32.RxRemoteApi
        RxRemoteApi.restype = NET_API_STATUS
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # Data Structures
        _TIME_OF_DAY_INFO._fields_ = [
            ('tod_elapsedt', DWORD),
            ('tod_msecs', DWORD),
            ('tod_hours', DWORD),
            ('tod_mins', DWORD),
            ('tod_secs', DWORD),
            ('tod_hunds', DWORD),
            ('tod_timezone', LONG),
            ('tod_tinterval', DWORD),
            ('tod_day', DWORD),
            ('tod_month', DWORD),
            ('tod_year', DWORD),
            ('tod_weekday', DWORD),
        ]

        # Special Values and Constants
        # Mask bits for use with NetRemoteComputerSupports:
        SUPPORTS_REMOTE_ADMIN_PROTOCOL = 0x00000002
        SUPPORTS_RPC = 0x00000004
        SUPPORTS_SAM_PROTOCOL = 0x00000008
        SUPPORTS_UNICODE = 0x00000010
        SUPPORTS_LOCAL = 0x00000020
        SUPPORTS_ANY = 0xFFFFFFFF

        # Flag bits for RxRemoteApi:
        NO_PERMISSION_REQUIRED = 0x00000001        # set if use NULL session
        ALLOCATE_RESPONSE = 0x00000002        # set if RxRemoteApi allocates response buffer
        USE_SPECIFIC_TRANSPORT = 0x80000000

        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF  _LMREMUTL_


