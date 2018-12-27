import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMCONFIG_ = None


class _CONFIG_INFO_0(ctypes.Structure):
    pass


CONFIG_INFO_0 = _CONFIG_INFO_0
PCONFIG_INFO_0 = POINTER(_CONFIG_INFO_0)
LPCONFIG_INFO_0 = POINTER(_CONFIG_INFO_0)


# /* + + BUILD Version: 0003 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmconfig.h
# Abstract: This module defines the API function prototypes and data
# structures for the following groups of NT API functions: NetConfig
# Environment: User Mode - Win32 Notes: You must include NETCONS.H before this
# file, since this file depends on values defined in NETCONS.H. --
if not defined(_LMCONFIG_):
    _LMCONFIG_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if defined(__cplusplus):
            pass
        # ENDIF

        from pyWinAPI.shared.lmcons_h import *  # NOQA

        netapi32 = ctypes.windll.NETAPI32

        REVISED_CONFIG_APIS = VOID
        # // Function Prototypes - Config
        # // SAL Annotations not available for obsolete APIs

        # NET_API_STATUS NET_API_FUNCTION
        # NetConfigGet(
        # IN  LPCWSTR  server OPTIONAL,
        # IN  LPCWSTR  component,
        # IN  LPCWSTR  parameter,
        # #ifdef REVISED_CONFIG_APIS
        # OUT LPBYTE  *bufptr
        # #else
        # OUT LPBYTE  *bufptr,
        # OUT LPDWORD totalavailable
        # #endif
        # );
        NetConfigGet = netapi32.NetConfigGet
        NetConfigGet.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetConfigGetAll(
        # IN  LPCWSTR  server OPTIONAL,
        # IN  LPCWSTR  component,
        # #ifdef REVISED_CONFIG_APIS
        # OUT LPBYTE  *bufptr
        # #else
        # OUT LPBYTE  *bufptr,
        # OUT LPDWORD totalavailable
        # #endif
        # );
        NetConfigGetAll = netapi32.NetConfigGetAll
        NetConfigGetAll.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetConfigSet(
        # IN  LPCWSTR  server OPTIONAL,
        # IN  LPCWSTR  reserved1 OPTIONAL,
        # IN  LPCWSTR  component,
        # IN  DWORD   level,
        # IN  DWORD   reserved2,
        # IN  LPBYTE  buf,
        # IN  DWORD   reserved3
        # );
        NetConfigSet = netapi32.NetConfigSet
        NetConfigSet.restype = NET_API_STATUS

        # Data Structures - Config
        _CONFIG_INFO_0._fields_ = [
            ('cfgi0_key', LPWSTR),
            ('cfgi0_data', LPWSTR),
        ]
        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   _LMCONFIG_


