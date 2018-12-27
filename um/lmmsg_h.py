import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMMSG_ = None


class _MSG_INFO_0(ctypes.Structure):
    pass


MSG_INFO_0 = _MSG_INFO_0
PMSG_INFO_0 = POINTER(_MSG_INFO_0)
LPMSG_INFO_0 = POINTER(_MSG_INFO_0)


class _MSG_INFO_1(ctypes.Structure):
    pass


MSG_INFO_1 = _MSG_INFO_1
PMSG_INFO_1 = POINTER(_MSG_INFO_1)
LPMSG_INFO_1 = POINTER(_MSG_INFO_1)


# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmmsg.h Abstract:
# This file contains structures, function prototypes, and definitions for the
# NetMessage API. [Environment:] User Mode - Win32 [Notes:] You must include
# NETCONS.H before this file, since this file depends on values defined in
# NETCONS.H. --
if not defined(_LMMSG_):
    _LMMSG_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.shared.lmcons_h import *  # NOQA

    netapi32 = ctypes.windll.NETAPI32

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if defined(__cplusplus):
            pass
        # END IF

        # // Function Prototypes

        # NET_API_STATUS NET_API_FUNCTION
        # NetMessageNameAdd(
        # _In_opt_  LPCWSTR  servername,
        # _In_      LPCWSTR  msgname
        # );
        NetMessageNameAdd = netapi32.NetMessageNameAdd
        NetMessageNameAdd.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetMessageNameEnum(
        # _In_opt_  LPCWSTR  servername,
        # _In_      DWORD    level,
        # _In_      LPBYTE  *bufptr,
        # _In_      DWORD    prefmaxlen,
        # _Out_     LPDWORD  entriesread,
        # _Out_     LPDWORD  totalentries,
        # _Out_     LPDWORD  resume_handle
        # );
        NetMessageNameEnum = netapi32.NetMessageNameEnum
        NetMessageNameEnum.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetMessageNameGetInfo(
        # _In_opt_  LPCWSTR  servername,
        # _In_      LPCWSTR  msgname,
        # _In_      DWORD    level,
        # _In_      LPBYTE  *bufptr
        # );
        NetMessageNameGetInfo = netapi32.NetMessageNameGetInfo
        NetMessageNameGetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetMessageNameDel(
        # _In_opt_  LPCWSTR  servername,
        # _In_      LPCWSTR  msgname
        # );
        NetMessageNameDel = netapi32.NetMessageNameDel
        NetMessageNameDel.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetMessageBufferSend(
        # _In_opt_  LPCWSTR servername,
        # _In_      LPCWSTR msgname,
        # _In_      LPCWSTR fromname,
        # _In_      LPBYTE  buf,
        # _In_      DWORD   buflen
        # );
        NetMessageBufferSend = netapi32.NetMessageBufferSend
        NetMessageBufferSend.restype = NET_API_STATUS


        # Data Structures
        _MSG_INFO_0._fields_ = [
            ('msgi0_name', LPWSTR),
        ]
        _MSG_INFO_1._fields_ = [
            ('msgi1_name', LPWSTR),
            ('msgi1_forward_flag', DWORD),
            ('msgi1_forward', LPWSTR),
        ]
        # Special Values and Constants
        # Values for msgi1_forward_flag.
        MSGNAME_NOT_FORWARDED = 0  # Name not forwarded
        MSGNAME_FORWARDED_TO = 0x04  # Name forward to remote station
        MSGNAME_FORWARDED_FROM = 0x10  # Name forwarded from remote station

        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF  _LMMSG_
