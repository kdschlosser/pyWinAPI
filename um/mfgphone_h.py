import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

_MFGPHONE_ = None


class _MFGPHONE_SIMLINEDETAIL(ctypes.Structure):
    pass


MFGPHONE_SIMLINEDETAIL = _MFGPHONE_SIMLINEDETAIL
PMFGPHONE_SIMLINEDETAIL = POINTER(_MFGPHONE_SIMLINEDETAIL)

# Copyright (c) Microsoft Corporation. All rights reserved.
if defined(_MSC_VER):
    pass
# END IF   _MSC_VER

if not defined(_MFGPHONE_):
    _MFGPHONE_ = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_ONECORE_APP):
        if NTDDI_VERSION >= NTDDI_WIN10:
            # Manufacturing Phone API
            # Get the number of available SIM slots
            # Callback to receive SIM line change event notification
            class _MFGPHONE_SIMLINEEVENT(ENUM):
                MFGPHONE_SIMLINEEVENT_UNKNOWN = 0
                MFGPHONE_SIMLINEEVENT_SIMSTATE = 1
                MFGPHONE_SIMLINEEVENT_REGISTRATIONSTATE = 2
                MFGPHONE_SIMLINEEVENT_NETWORKNAME = 3
                MFGPHONE_SIMLINEEVENT_LINESYSTEMTYPE = 4
                MFGPHONE_SIMLINEEVENT_SIGNALSTRENGTH = 5
                MFGPHONE_SIMLINEEVENT_CALLSTATUS = 6

            MFGPHONE_SIMLINEEVENT = _MFGPHONE_SIMLINEEVENT

            # typedef VOID (CALLBACK *MFGPHONE_SIMLINEEVENT_NOTIFY_CALLBACK)(
            # _In_ UINT SimSlot,
            # _In_ MFGPHONE_SIMLINEEVENT SimLineEvent,
            # _In_ PVOID Context
            # );
            MFGPHONE_SIMLINEEVENT_NOTIFY_CALLBACK = CALLBACK(
                VOID,
                UINT,
                MFGPHONE_SIMLINEEVENT,
                PVOID,
            )

            # Detailed SIM slot line information
            MFGPHONE_SIMSLOT_NONE = -1


            class _MFGPHONE_SIMSTATE(ENUM):
                MFGPHONE_SIMSTATE_UNKNOWN = 0
                MFGPHONE_SIMSTATE_NONE = 1
                MFGPHONE_SIMSTATE_ACTIVE = 2
                MFGPHONE_SIMSTATE_INVALID = 3
                MFGPHONE_SIMSTATE_LOCKED = 4
                MFGPHONE_SIMSTATE_DISABLED = 5

            MFGPHONE_SIMSTATE = _MFGPHONE_SIMSTATE


            class _MFGPHONE_REGISTRATIONSTATE(ENUM):
                MFGPHONE_REGISTRATIONSTATE_UNKNOWN = 0
                MFGPHONE_REGISTRATIONSTATE_NOSIGNAL = 1
                MFGPHONE_REGISTRATIONSTATE_UNREGISTERED = 2
                MFGPHONE_REGISTRATIONSTATE_REGISTERING = 3
                MFGPHONE_REGISTRATIONSTATE_REGISTERED = 4
                MFGPHONE_REGISTRATIONSTATE_DENIED = 5

            MFGPHONE_REGISTRATIONSTATE = _MFGPHONE_REGISTRATIONSTATE


            class _MFGPHONE_CALLSTATUS(ENUM):
                MFGPHONE_CALLSTATUS_UNKNOWN = 0
                MFGPHONE_CALLSTATUS_IDLE = 1
                MFGPHONE_CALLSTATUS_CALLING = 2
                MFGPHONE_CALLSTATUS_INCOMING = 3
                MFGPHONE_CALLSTATUS_ACTIVE = 4

            MFGPHONE_CALLSTATUS = _MFGPHONE_CALLSTATUS


            class _MFGPHONE_LINESYSTEMTYPE(ENUM):
                MFGPHONE_LINESYSTEMTYPE_UNKNOWN = 0
                MFGPHONE_LINESYSTEMTYPE_GSM = 1
                MFGPHONE_LINESYSTEMTYPE_CDMA = 2
                MFGPHONE_LINESYSTEMTYPE_IMS = 3

            MFGPHONE_LINESYSTEMTYPE = _MFGPHONE_LINESYSTEMTYPE

            _MFGPHONE_SIMLINEDETAIL._fields_ = [
                ('SimSlot', UINT),
                ('SimState', MFGPHONE_SIMSTATE),
                ('RegistrationState', MFGPHONE_REGISTRATIONSTATE),
                ('NetworkName', WCHAR * 64),
                ('LineSystemType', MFGPHONE_LINESYSTEMTYPE),
                ('SignalStrength', UINT),
                ('CallStatus', MFGPHONE_CALLSTATUS),
            ]

            # Dial, End call
            # Speaker control while in a call
        # END IF   End NTDDI_WIN10 and greater
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_ONECORE_APP)

    if defined(__cplusplus):
        pass
    # END IF

# END IF   _MFGPHONE_


