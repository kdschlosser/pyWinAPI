import ctypes
from pyWinAPI import *
from pyWinAPI.shared.devpropdef_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *



# + + Copyright (c) 2012 Microsoft Corporation Module Name: BTHGUID.H
# Abstract: Public Interface and Property definitions for Bluetooth drivers
# Environment: Kernel & user mode Revision History: - -
if NTDDI_VERSION >= NTDDI_VISTA:

    # {81A7FDF3 - 86C1 - 4BE8 - A8C8 - 2A6D188B4177}
    GUID_BTHDDI_SDP_NODE_INTERFACE = DEFINE_GUID(
        0x81A7FDF3,
        0x86C1,
        0x4BE8,
        0xA8,
        0xC8,
        0x2A,
        0x6D,
        0x18,
        0x8B,
        0x41,
        0x77
    )

    # {4E719439 - 9CF1 - 4BAB - AC1D - 3279865743D2}
    GUID_BTHDDI_SDP_PARSE_INTERFACE = DEFINE_GUID(
        0x4E719439,
        0x9CF1,
        0x4BAB,
        0xAC,
        0x1D,
        0x32,
        0x79,
        0x86,
        0x57,
        0x43,
        0xD2
    )

    # {94A59AA8 - 4383 - 4286 - AA4F - 34A160F40004}
    GUID_BTHDDI_PROFILE_DRIVER_INTERFACE = DEFINE_GUID(
        0x94A59AA8,
        0x4383,
        0x4286,
        0xAA,
        0x4F,
        0x34,
        0xA1,
        0x60,
        0xF4,
        0x0,
        0x4
    )
# END IF   (NTDDI_VERSION >= NTDDI_VISTA)

# Bluetooth device interface GUID

# {00F40965 - E89D - 4487 - 9890 - 87C3ABB211F4}
GUID_BTH_DEVICE_INTERFACE = DEFINE_GUID(
    0x00F40965,
    0xE89D,
    0x4487,
    0x98,
    0x90,
    0x87,
    0xC3,
    0xAB,
    0xB2,
    0x11,
    0xF4
)

# Device properties, these properties are stored in Bluetooth device objects
# for both BR/EDR and LE devices.

# {2BD67D8B - 8BEB - 48D5 - 87E0 - 6CDA3428040A}
DEVPKEY_Bluetooth_DeviceAddress = DEFINE_DEVPROPKEY(
    0x2BD67D8B,
    0x8BEB,
    0x48D5,
    0x87,
    0xE0,
    0x6C,
    0xDA,
    0x34,
    0x28,
    0x04,
    0x0A,
    0x1
)
DEVPKEY_Bluetooth_ServiceGUID = DEFINE_DEVPROPKEY(
    0x2BD67D8B,
    0x8BEB,
    0x48D5,
    0x87,
    0xE0,
    0x6C,
    0xDA,
    0x34,
    0x28,
    0x04,
    0x0A,
    0x2
)
DEVPKEY_Bluetooth_DeviceFlags = DEFINE_DEVPROPKEY(
    0x2BD67D8B,
    0x8BEB,
    0x48D5,
    0x87,
    0xE0,
    0x6C,
    0xDA,
    0x34,
    0x28,
    0x04,
    0x0A,
    0x3
)
DEVPKEY_Bluetooth_DeviceManufacturer = DEFINE_DEVPROPKEY(
    0x2BD67D8B,
    0x8BEB,
    0x48D5,
    0x87,
    0xE0,
    0x6C,
    0xDA,
    0x34,
    0x28,
    0x04,
    0x0A,
    0x4
)
DEVPKEY_Bluetooth_DeviceModelNumber = DEFINE_DEVPROPKEY(
    0x2BD67D8B,
    0x8BEB,
    0x48D5,
    0x87,
    0xE0,
    0x6C,
    0xDA,
    0x34,
    0x28,
    0x04,
    0x0A,
    0x5
)
DEVPKEY_Bluetooth_DeviceVIDSource = DEFINE_DEVPROPKEY(
    0x2BD67D8B,
    0x8BEB,
    0x48D5,
    0x87,
    0xE0,
    0x6C,
    0xDA,
    0x34,
    0x28,
    0x04,
    0x0A,
    0x6
)
DEVPKEY_Bluetooth_DeviceVID = DEFINE_DEVPROPKEY(
    0x2BD67D8B,
    0x8BEB,
    0x48D5,
    0x87,
    0xE0,
    0x6C,
    0xDA,
    0x34,
    0x28,
    0x04,
    0x0A,
    0x7
)
DEVPKEY_Bluetooth_DevicePID = DEFINE_DEVPROPKEY(
    0x2BD67D8B,
    0x8BEB,
    0x48D5,
    0x87,
    0xE0,
    0x6C,
    0xDA,
    0x34,
    0x28,
    0x04,
    0x0A,
    0x8
)
DEVPKEY_Bluetooth_DeviceProductVersion = DEFINE_DEVPROPKEY(
    0x2BD67D8B,
    0x8BEB,
    0x48D5,
    0x87,
    0xE0,
    0x6C,
    0xDA,
    0x34,
    0x28,
    0x04,
    0x0A,
    0x9
)
if NTDDI_VERSION >= NTDDI_WIN10:
    DEVPKEY_Bluetooth_ClassOfDevice_Deprecated = DEFINE_DEVPROPKEY(
        0x2BD67D8B,
        0x8BEB,
        0x48D5,
        0x87,
        0xE0,
        0x6C,
        0xDA,
        0x34,
        0x28,
        0x04,
        0x0A,
        0x4
    )
    DEVPKEY_Bluetooth_LastConnectedTime_Deprecated = DEFINE_DEVPROPKEY(
        0x2BD67D8B,
        0x8BEB,
        0x48D5,
        0x87,
        0xE0,
        0x6C,
        0xDA,
        0x34,
        0x28,
        0x04,
        0x0A,
        0x5
    )
    DEVPKEY_Bluetooth_ClassOfDevice = DEFINE_DEVPROPKEY(
        0x2BD67D8B,
        0x8BEB,
        0x48D5,
        0x87,
        0xE0,
        0x6C,
        0xDA,
        0x34,
        0x28,
        0x04,
        0x0A,
        0xA
    )
    DEVPKEY_Bluetooth_LastConnectedTime = DEFINE_DEVPROPKEY(
        0x2BD67D8B,
        0x8BEB,
        0x48D5,
        0x87,
        0xE0,
        0x6C,
        0xDA,
        0x34,
        0x28,
        0x04,
        0x0A,
        0xB
    )
    if NTDDI_VERSION >= NTDDI_WIN10_RS2: # TODO_NTDDI_WIN10_RS3
        DEVPKEY_Bluetooth_LastSeenTime = DEFINE_DEVPROPKEY(
            0x2BD67D8B,
            0x8BEB,
            0x48D5,
            0x87,
            0xE0,
            0x6C,
            0xDA,
            0x34,
            0x28,
            0x04,
            0x0A,
            0xC
        )
    # END IF
# END IF
