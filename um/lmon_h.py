import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _PORT_INFO_FFA(ctypes.Structure):
    pass


PORT_INFO_FFA = _PORT_INFO_FFA
PPORT_INFO_FFA = POINTER(_PORT_INFO_FFA)
LPPORT_INFO_FFA = POINTER(_PORT_INFO_FFA)


class _PORT_INFO_FFW(ctypes.Structure):
    pass


PORT_INFO_FFW = _PORT_INFO_FFW
PPORT_INFO_FFW = POINTER(_PORT_INFO_FFW)
LPPORT_INFO_FFW = POINTER(_PORT_INFO_FFW)


# /* + + Copyright (c) 1991-1999 Microsoft Corporation All rights reserved
# Module Name: lmon.h --
from pyWinAPI.shared.winapifamily_h import * # NOQA

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    _PORT_INFO_FFA._fields_ = [
        ('pName', LPSTR),
        ('cbMonitorData', DWORD),
        ('pMonitorData', LPBYTE),
    ]

    _PORT_INFO_FFW._fields_ = [
        ('pName', LPWSTR),
        ('cbMonitorData', DWORD),
        ('pMonitorData', LPBYTE),
    ]
    if defined(UNICODE):
        PORT_INFO_FF = PORT_INFO_FFW
        PPORT_INFO_FF = PPORT_INFO_FFW
        LPPORT_INFO_FF = LPPORT_INFO_FFW
    else:
        PORT_INFO_FF = PORT_INFO_FFA
        PPORT_INFO_FF = PPORT_INFO_FFA
        LPPORT_INFO_FF = LPPORT_INFO_FFA
    # END IF   UNICODE
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)


