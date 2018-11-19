import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *


class _BINDING_HANDLE(ctypes.Structure):
    pass


RX_BINDING_HANDLE = _BINDING_HANDLE
PRX_BINDING_HANDLE = POINTER(_BINDING_HANDLE)


class _RX_BINDING_CONTEXT(ctypes.Structure):
    pass


RX_BINDING_CONTEXT = _RX_BINDING_CONTEXT
PRX_BINDING_CONTEXT = POINTER(_RX_BINDING_CONTEXT)

_RXTYPES_INCL = None

if not defined(_RXTYPES_INCL):
    _RXTYPES_INCL = 1
    from pyWinAPI.km.nodetype_h import * # NOQA

    # MUST match MaximumWorkQueue in wdm.h for Win7 or earlier.
    RxMaximumWorkQueue = 3
    RX_HANDLE = PVOID
    PRX_HANDLE = POINTER(PVOID)
    RX_SPIN_LOCK = KSPIN_LOCK
    PRX_SPIN_LOCK = PKSPIN_LOCK

    # String definitions
    # The RX_STRING type corresponds to a UNICODE_STRING and all the Rtl
    # functions that are
    # available to manipulate Unicode strings can be used to manipulate the
    # strings
    _BINDING_HANDLE._fields_ = [
        # Win9X net structure
        ('pTdiEmulationContext', RX_HANDLE),
        # tdi transport information.
        ('pTransportInformation', RX_HANDLE),
    ]
    PUNICODE_STRING = POINTER(UNICODE_STRING)

    # This structure is transient. Most fields in this structure allow us to
    # move through the bind/addname part of activating a net. Runtime info
    # for the rxce and LONG term context is kept elsewhere.
    _RX_BINDING_CONTEXT._fields_ = [
        # Transport Name (unicode string).
        ('pTransportName', PUNICODE_STRING),
        # Requested QOS.
        ('QualityOfService', ULONG),
        # Handle to transport bind info.
        ('pBindHandle', PRX_BINDING_HANDLE),
    ]
# END IF   _RXTYPES_INCL
