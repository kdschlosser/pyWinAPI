import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_NETTYPES_ = None

class _FLAT_STRING(ctypes.Structure):
    pass


FLAT_STRING = _FLAT_STRING
PFLAT_STRING = POINTER(_FLAT_STRING)


class _NETWORK_NAME(ctypes.Structure):
    pass


NETWORK_NAME = _NETWORK_NAME
PNETWORK_NAME = POINTER(_NETWORK_NAME)


class _HARDWARE_ADDRESS(ctypes.Structure):
    pass


HARDWARE_ADDRESS = _HARDWARE_ADDRESS
PHARDWARE_ADDRESS = POINTER(_HARDWARE_ADDRESS)




# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: nettypes.h Abstract: This header file contains type definitions for
# the NT TDI, NDI, DDI, and PDI interfaces which are not specific to a single
# interface. Revision History: --
if not defined(_NETTYPES_):
    _NETTYPES_ = VOID
    from winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # The following basic type is used to provide extensibility in request
        # and response packets. The OFFSET type is used to contain a value
        # which
        # is interpreted as a relative address consisting of a number of bytes
        # from the beginning of the immediate parent structure.
        OFFSET = ULONG


        # The following basic type is used throughout all the layers to pass a
        # string through an I/O interface which does not allow embedded
        # pointers.
        # To allocate a FLAT_STRING, one must make room for the correct number
        # of
        # buffer bytes in the allocation.
        # total size of string buffer.
        _FLAT_STRING._fields_ = [
            ('MaximumLength', SHORT),
            # number of bytes represented in string.
            ('Length', SHORT),
            # the buffer itself follows this struct.
            ('Buffer', CHAR * 1),
        ]


        # Basic type used to represent a network name, typically as a
        # component of
        # a transport address structure through the TDI. This type is also
        # passed
        # through the NDI interface. This type is declared as a structure so
        # that
        # it can be extended easily without modifying applications, even
        # though it
        # currently only has one element.
        # network name in FLAT_STRING format.
        _NETWORK_NAME._fields_ = [
            ('Name', FLAT_STRING),
        ]

        # Basic type used to represent an address at the hardware level of the
        # network. Hardware addresses are abstract types which are mapped to
        # adapter addresses by the physical provider. See the Physical Driver
        # Interface specification for details on how this is accomplished.
        HARDWARE_ADDRESS_LENGTH = 6        # number of octets in a hardware address.


        _HARDWARE_ADDRESS._fields_ = [
            ('Address', UCHAR * HARDWARE_ADDRESS_LENGTH),
        ]

        # Network management variable types used by all interface levels.
        NETMAN_VARTYPE_ULONG = 0        # type is a ULONG.
        NETMAN_VARTYPE_HARDWARE_ADDRESS = 1        # type is a HARDWARE_ADDRESS.
        NETMAN_VARTYPE_STRING = 2        # type is a FLAT_STRING.
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   _NETTYPES_


