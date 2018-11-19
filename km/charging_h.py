import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _POWERSOURCESTATUS(ctypes.Structure):
    pass


POWERSOURCESTATUS = _POWERSOURCESTATUS
PPOWERSOURCESTATUS = POINTER(_POWERSOURCESTATUS)


class _CHARGINGSTATUSCOMPLETE(ctypes.Structure):
    pass


CHARGINGSTATUSCOMPLETE = _CHARGINGSTATUSCOMPLETE
PCHARGINGSTATUSCOMPLETE = POINTER(_CHARGINGSTATUSCOMPLETE)


class _POWERSOURCEUPDATE(ctypes.Structure):
    pass


POWERSOURCEUPDATE = _POWERSOURCEUPDATE
PPOWERSOURCEUPDATE = POINTER(_POWERSOURCEUPDATE)


class _POWERSOURCEUPDATEEX(ctypes.Structure):
    pass


POWERSOURCEUPDATEEX = _POWERSOURCEUPDATEEX
PPOWERSOURCEUPDATEEX = POINTER(_POWERSOURCEUPDATEEX)


class _CAD_POWER_SOURCE_INFO(ctypes.Structure):
    pass


CAD_POWER_SOURCE_INFO = _CAD_POWER_SOURCE_INFO
PCAD_POWER_SOURCE_INFO = POINTER(_CAD_POWER_SOURCE_INFO)


class _CAD_POWER_SOURCE_INFO_USB(ctypes.Structure):
    pass


CAD_POWER_SOURCE_INFO_USB = _CAD_POWER_SOURCE_INFO_USB
PCAD_POWER_SOURCE_INFO_USB = POINTER(_CAD_POWER_SOURCE_INFO_USB)


class _BATTERYPROVISIONINGSTATUS(ctypes.Structure):
    pass


BATTERYPROVISIONINGSTATUS = _BATTERYPROVISIONINGSTATUS
PBATTERYPROVISIONINGSTATUS = POINTER(_BATTERYPROVISIONINGSTATUS)


class _CONFIGURABLE_CHARGER_PROPERTY_HEADER(ctypes.Structure):
    pass


CONFIGURABLE_CHARGER_PROPERTY_HEADER = _CONFIGURABLE_CHARGER_PROPERTY_HEADER
PCONFIGURABLE_CHARGER_PROPERTY_HEADER = POINTER(_CONFIGURABLE_CHARGER_PROPERTY_HEADER)


# /* + + Copyright (C) Microsoft Corporation Module Name: charging.h Abstract:
# This file specifies the USB - CAD interface. Environment: Kernel mode - -
from pyWinAPI.shared.usbfnbase_h import * # NOQA
from pyWinAPI.shared.initguid_h import * # NOQA
from pyWinAPI.shared.devioctl_h import * # NOQA

# //////////////////////////////////////////////////////////////////////////////
#
# Device interfaces
# {EC0A1CC9 - 4294 - 43FB - BF37 - B850CE95F337}
GUID_DEVINTERFACE_CHARGING_ARBITRATION = DEFINE_GUID(
    0xEC0A1CC9,
    0x4294,
    0x43FB,
    0xBF,
    0x37,
    0xB8,
    0x50,
    0xCE,
    0x95,
    0xF3,
    0x37
)


# Device interfaces to be created by the corresponding devices handling
# configurable chargers (eg. setting configurable properties)
# {7158C35C - C1BC - 4D90 - ACB1 - 8020BD0E19CA}
GUID_DEVINTERFACE_CONFIGURABLE_USBFN_CHARGER = DEFINE_GUID(
    0x7158C35C,
    0xC1BC,
    0x4D90,
    0xAC,
    0xB1,
    0x80,
    0x20,
    0xBD,
    0xE,
    0x19,
    0xCA
)

# {3612B1C8 - 3633 - 47D3 - 8AF5 - 00A4DFA04793}
GUID_DEVINTERFACE_CONFIGURABLE_WIRELESS_CHARGER = DEFINE_GUID(
    0x3612B1C8,
    0x3633,
    0x47D3,
    0x8A,
    0xF5,
    0x0,
    0xA4,
    0xDF,
    0xA0,
    0x47,
    0x93
)

# //////////////////////////////////////////////////////////////////////////////
#
# IoControl definitions
IOCTL_CAD_DISABLE_CHARGING = CTL_CODE(
    FILE_DEVICE_BATTERY,
    0x120,
    METHOD_BUFFERED,
    FILE_READ_ACCESS | FILE_WRITE_ACCESS,
)


# Received by CAD.
# Issued to query known power sources and their properties.
IOCTL_CAD_GET_CHARGING_STATUS_COMPLETE = CTL_CODE(
    FILE_DEVICE_BATTERY,
    0x122,
    METHOD_BUFFERED,
    FILE_READ_ACCESS | FILE_WRITE_ACCESS,
)

# 0x123 entry is reserved - do not use
# Issued by power source, limited to Wireless charger
# Received by CAD.
# Issued to advertise power source properties.
# Note - IOCTL_CAD_POWER_SOURCE_UPDATE_EX should be preferred over this IOCL.
IOCTL_INTERNAL_CAD_POWER_SOURCE_UPDATE = CTL_CODE(
    FILE_DEVICE_BATTERY,
    0x130,
    METHOD_BUFFERED,
    FILE_READ_ACCESS | FILE_WRITE_ACCESS,
)
IOCTL_CAD_GET_BATTERY_PROVISIONING_STATUS = CTL_CODE(
    FILE_DEVICE_BATTERY,
    0x131,
    METHOD_BUFFERED,
    FILE_READ_ACCESS | FILE_WRITE_ACCESS,
)

# Issued by power source such as USB, Wireless charger, etc.
# Received by CAD.
# Issued to advertise power source properties.
IOCTL_CAD_POWER_SOURCE_UPDATE_EX = CTL_CODE(
    FILE_DEVICE_BATTERY,
    0x132,
    METHOD_BUFFERED,
    FILE_READ_ACCESS | FILE_WRITE_ACCESS,
)

# IoControl to be implemented by configurable chargers
# The IOCTL(s) here must be sent to the IoTarget of the devices creating the
# device interfaces above, not the CAD.
IOCTL_INTERNAL_CONFIGURE_CHARGER_PROPERTY = CTL_CODE(
    FILE_DEVICE_BATTERY,
    0x140,
    METHOD_BUFFERED,
    FILE_READ_ACCESS | FILE_WRITE_ACCESS,
)

# //////////////////////////////////////////////////////////////////////////////
#
# Type Definitions
class _POWERSOURCEID(ENUM):
    PowerSourceInvalid = 0x00
    PowerSourceNone = 1
    PowerSourceUsbfn = 2
    PowerSourceWirelessCharger = 3
    PowerSourceKD = 4
    PowerSourceUsbTypeC = 5
    PowerSourceMax = 6

POWERSOURCEID = _POWERSOURCEID
PPOWERSOURCEID = POINTER(_POWERSOURCEID)

# IOCTL_CAD_GET_CHARGING_STATUS_COMPLETE response.
_POWERSOURCESTATUS._fields_ = [
    # Identifies power source
    ('PowerSourceId', POWERSOURCEID),
    # through the power source in mA
    ('MaxChargeCurrent', ULONG),
    # <other values> | <undefined>
    ('PowerSourceInformation', ULONG),
    # Set to true if the power source is available (attached)
    ('PowerSourceStatus', BOOLEAN),
]

_CHARGINGSTATUSCOMPLETE._fields_ = [
    # Legacy USB port status
    ('UsbFnStatus', POWERSOURCESTATUS),
    # USB Type - C port status
    ('UsbTypeCStatus', POWERSOURCESTATUS),
    # KD Power Source Status
    ('KDStatus', POWERSOURCESTATUS),
    # Wireless Charger Power Source Status
    ('WirelessStatus', POWERSOURCESTATUS),
    # 0 implies that force disable is off.
    ('ForceDisableChargingRefCount', ULONG),
]

# IOCTL_INTERNAL_CAD_POWER_SOURCE_UPDATE payload.
_POWERSOURCEUPDATE._fields_ = [
    # API.
    ('PowerSourceId', POWERSOURCEID),
    # through the power source in mA
    ('MaxChargeCurrent', ULONG),
    # Set to true if the power source is available (attached)
    ('PowerSourceAvailableStatus', BOOLEAN),
    # 64 - bit systems.
    ('PowerSourceInformation', PVOID),
]

_POWERSOURCEUPDATEEX._fields_ = [
    # Identifies the power source
    ('Source', POWERSOURCEUPDATE),
    # supported.
    ('ChargerId', GUID),
]

# IOCTL_CAD_POWER_SOURCE_UPDATE_EX payload.
# This type describes dynamic properties of a power source, this is a new and
# improved variant of POWERSOURCEUPDATE and POWERSOURCEUPDATEEX.
_CAD_POWER_SOURCE_INFO._fields_ = [
    # Identifies the power source.
    ('SourceId', POWERSOURCEID),
    # Identifies revision number of the data contained in VaData.
    ('Version', USHORT),
    # charging source type identified by SourceId.
    ('VaData', ULONG * 1),
]


# Specializes CAD_POWER_SOURCE_INFO for USB.
# IOCTL_CAD_POWER_SOURCE_UPDATE_EX payload when:
# - SourceId is set to PowerSourceUsbfn (for Legacy USB) or
# PowerSourceUsbTypeC (for USB Type - C).
# - Version is set to zero.
# N.B. next revision of this type should be named CAD_POWER_SOURCE_INFO_USB_V1
# and Version should hold value 1.
_CAD_POWER_SOURCE_INFO_USB._fields_ = [
    # Identifies the power source.
    ('SourceId', POWERSOURCEID),
    # Identifies revision number of the data contained in this structure.
    ('Version', USHORT),
    # Flags.
    ('Flags', ULONG),
    # case zero will be interpreted as unknown value.
    ('MaxCurrent', ULONG),
    # case zero will be interpreted as unknown value.
    ('Voltage', ULONG),
    # Actual underlying type is USB_CHARGER_PORT.
    ('PortType', LONG),
    # When set to 0 indicates that port information is unavailable.
    ('PortId', ULONGLONG),
    # USB port type information, provided by the USB stack.
    ('PowerSourceInformation', USBFN_PORT_TYPE),
    # Represents OEM proprietary charger type when not GUID_EMPTY.
    ('OemCharger', GUID),
]


# This is the output argument to IOCTL_CAD_GET_BATTERY_PROVISIONING_STATUS
_BATTERYPROVISIONINGSTATUS._fields_ = [
    # is device provisioned for battery blank?
    ('IsDeviceProvisionedForBatteryBlank', BOOLEAN),
]


# This is the input argument to IOCTL_INTERNAL_CONFIGURE_CHARGER_PROPERTY
_CONFIGURABLE_CHARGER_PROPERTY_HEADER._fields_ = [
    # Size of the struct
    ('Size', ULONG),
    # Charger Id
    ('ChargerId', GUID),
    # Id of the property to be configured
    ('PropertyId', ULONG),
]

