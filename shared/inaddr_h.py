import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *


class in_addr(ctypes.Structure):
    pass


IN_ADDR = in_addr
PIN_ADDR = POINTER(in_addr)
LPIN_ADDR = POINTER(in_addr)


# /* + + Copyright (c) Microsoft Corporation Module Name: inaddr.h
# Environment: user mode or kernel mode - -
s_addr = None
if not defined(s_addr):
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # IPv4 Internet address
        # This is an 'on - wire' format structure.

        class S_un(ctypes.Union):
            pass

        class S_un_b(ctypes.Structure):
            pass

        S_un_b._fields_ = [
            ('s_b1', UCHAR),
            ('s_b2', UCHAR),
            ('s_b3', UCHAR),
            ('s_b4', UCHAR)
        ]

        S_un.S_un_b = S_un_b

        class S_un_w(ctypes.Structure):
            pass

        S_un_w._fields_ = [
            ('s_w1', USHORT),
            ('s_w2', USHORT),
        ]

        S_un.S_un_w = S_un_w

        S_un._field_ = [
            ('S_un_b', S_un.S_un_b),
            ('S_un_w', S_un.S_un_w),
            ('S_addr', ULONG),
        ]

        in_addr.S_un = S_un

        in_addr._fields_ = [
            ('S_un', in_addr.S_un),
        ]

        s_addr = S_un.S_addr  # can be used for most tcp & ip code
        s_host = S_un.S_un_b.s_b2  # host on imp
        s_net = S_un.S_un_b.s_b1  # network
        s_imp = S_un.S_un_w.s_w2  # imp
        s_impno = S_un.S_un_b.s_b4  # imp #
        s_lh = S_un.S_un_b.s_b3  # logical host

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
# END IF
