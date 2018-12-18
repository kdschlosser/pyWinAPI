import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


s6_addr = None

class in6_addr(ctypes.Structure):
    pass


IN6_ADDR = in6_addr
PIN6_ADDR = POINTER(in6_addr)
LPIN6_ADDR = POINTER(in6_addr)

# /* + + Copyright (c) Microsoft Corporation Module Name: in6addr.h
# Environment: user mode or kernel mode --
if not defined(s6_addr):
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # IPv6 Internet address (RFC 2553)
        # This is an 'on-wire' format structure.
        class u(ctypes.Union):
            pass


        u._fields_ = [
            ('Byte', UCHAR * 16),
            ('Word', USHORT * 8),
        ]
        in6_addr.u = u

        in6_addr._fields_ = [
            ('u', in6_addr.u),
        ]
        in_addr6 = in6_addr

        # Defines to match RFC 2553.
        _S6_un = u
        _S6_u8 = Byte
        s6_addr = _S6_un._S6_u8

        # Defines for our implementation.
        s6_bytes = u.Byte
        s6_words = u.Word
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
# END IF


