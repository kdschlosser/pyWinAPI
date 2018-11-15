import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _ALTERNATE_INTERFACE(ctypes.Structure):
    pass


ALTERNATE_INTERFACE = _ALTERNATE_INTERFACE
PALTERNATE_INTERFACE = POINTER(_ALTERNATE_INTERFACE)


class _USBFN_NOTIFICATION(ctypes.Structure):
    pass


USBFN_NOTIFICATION = _USBFN_NOTIFICATION
PUSBFN_NOTIFICATION = POINTER(_USBFN_NOTIFICATION)


class _USBFN_PIPE_INFORMATION(ctypes.Structure):
    pass


USBFN_PIPE_INFORMATION = _USBFN_PIPE_INFORMATION
PUSBFN_PIPE_INFORMATION = POINTER(_USBFN_PIPE_INFORMATION)


class _USBFN_CLASS_INTERFACE(ctypes.Structure):
    pass


USBFN_CLASS_INTERFACE = _USBFN_CLASS_INTERFACE
PUSBFN_CLASS_INTERFACE = POINTER(_USBFN_CLASS_INTERFACE)


class _USBFN_CLASS_INFORMATION_PACKET(ctypes.Structure):
    pass


USBFN_CLASS_INFORMATION_PACKET = _USBFN_CLASS_INFORMATION_PACKET
PUSBFN_CLASS_INFORMATION_PACKET = POINTER(_USBFN_CLASS_INFORMATION_PACKET)


class _USBFN_CLASS_INTERFACE_EX(ctypes.Structure):
    pass


USBFN_CLASS_INTERFACE_EX = _USBFN_CLASS_INTERFACE_EX
PUSBFN_CLASS_INTERFACE_EX = POINTER(_USBFN_CLASS_INTERFACE_EX)


class _USBFN_CLASS_INFORMATION_PACKET_EX(ctypes.Structure):
    pass


USBFN_CLASS_INFORMATION_PACKET_EX = _USBFN_CLASS_INFORMATION_PACKET_EX
PUSBFN_CLASS_INFORMATION_PACKET_EX = POINTER(_USBFN_CLASS_INFORMATION_PACKET_EX)


class _USBFN_INTERFACE_INFO(ctypes.Structure):
    pass


USBFN_INTERFACE_INFO = _USBFN_INTERFACE_INFO
PUSBFN_INTERFACE_INFO = POINTER(_USBFN_INTERFACE_INFO)


class _USBFN_USB_STRING(ctypes.Structure):
    pass


USBFN_USB_STRING = _USBFN_USB_STRING
PUSBFN_USB_STRING = POINTER(_USBFN_USB_STRING)


class _USBFN_BUS_CONFIGURATION_INFO(ctypes.Structure):
    pass


USBFN_BUS_CONFIGURATION_INFO = _USBFN_BUS_CONFIGURATION_INFO
PUSBFN_BUS_CONFIGURATION_INFO = POINTER(_USBFN_BUS_CONFIGURATION_INFO)


# + + Copyright (C) Microsoft Corporation. All rights reserved. Module Name:
# usbfnbase.h Abstract: This header defines all interfaces and macros that USB
# Function class drivers will require to implement class driver functionality.
# Environment: Kernel and user mode - -
# Includes
from pyWinAPI.shared.usbspec_h import * # NOQA

# Registry path for the USBFn Enumeration keys
KREGUSBFNENUMPATH = (
    "\\Registry\\Machine\\SYSTEM\\CurrentControlSet\\Control\\USBFN\\"
)
UREGUSBFNENUMPATH = (
    "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\USBFN\\"
)

# Registry path for the USBFn Enumeration keys (manufacturing mode)
KREGMANUSBFNENUMPATH = (
    "\\Registry\\Machine\\SYSTEM\\CurrentControlSet\\Control\\ManufacturingMode\\Current\\USBFN\\"
)
UREGMANUSBFNENUMPATH = (
    "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\ManufacturingMode\\Current\\USBFN\\"
)

# Structure definitions
# A configuration can have upto 15 endpoints plus Endpoint 0 which beLONGs to
# the device.
# That translates into 16 pipes, including the pipe beLONGing to EP0.
MAX_NUM_USBFN_ENDPOINTS = 15
MAX_NUM_USBFN_PIPES = (MAX_NUM_USBFN_ENDPOINTS) + 1

# Maximum length of a configuration length supported.
MAX_CONFIGURATION_NAME_LENGTH = 40
MAX_USB_STRING_LENGTH = 255

# Maximum number of supported configurations
MAX_SUPPORTED_CONFIGURATIONS = 12

# if an interrupt endpoint's wMaxPacketSize should not be updated based on
# the current speed of the device and limit it to whatever was mentioned in
# the registry, wMaxPacketSize's MSB should be set to 1. Or the function stack
# will update it to an optimal value based on current connection speed.
# If this mask is set to wMaxPacketSize of the endpoint descriptor, then that
# endpoint's wMaxPacketSize will not be updated according to the current speed.
USBFN_INTERRUPT_ENDPOINT_SIZE_NOT_UPDATEABLE_MASK = 0x80

# USB Electrical Test Mode selectors
USB_TEST_MODE_TEST_J = 0x01
USB_TEST_MODE_TEST_K = 0x02
USB_TEST_MODE_TEST_SE0_NAK = 0x03
USB_TEST_MODE_TEST_PACKET = 0x04
USB_TEST_MODE_TEST_FORCE_ENABLE = 0x05

# Maximum length of an interface name.
MAX_INTERFACE_NAME_LENGTH = 40
MAX_ALTERNATE_NAME_LENGTH = 40
MAX_ASSOCIATION_NAME_LENGTH = 40

# Maximum length of an interface GUID string.
MAX_INTERFACE_GUID_SIZE = (
    ctypes.sizeof("{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}")
)
MAX_INTERFACE_GUID_LENGTH = MAX_INTERFACE_GUID_SIZE / ctypes.sizeof(WCHAR)

# Notifications sent to class drivers.
class _USBFN_EVENT(ENUM):
    UsbfnEventMinimum = 0x0
    UsbfnEventAttach = 1
    UsbfnEventReset = 2
    UsbfnEventDetach = 3
    UsbfnEventSuspend = 4
    UsbfnEventResume = 5
    UsbfnEventSetupPacket = 6
    UsbfnEventConfigured = 7
    UsbfnEventUnConfigured = 8
    UsbfnEventPortType = 9
    UsbfnEventBusTearDown = 10
    UsbfnEventSetInterface = 11
    UsbfnEventMaximum = 12


USBFN_EVENT = _USBFN_EVENT
PUSBFN_EVENT = POINTER(_USBFN_EVENT)

# USBFN Port Types
class _USBFN_PORT_TYPE(ENUM):
    UsbfnUnknownPort = 0
    UsbfnStandardDownstreamPort = 1
    UsbfnChargingDownstreamPort = 2
    UsbfnDedicatedChargingPort = 3
    UsbfnInvalidDedicatedChargingPort = 4
    UsbfnProprietaryDedicatedChargingPort = 5
    UsbfnPortTypeMaximum = 6


USBFN_PORT_TYPE = _USBFN_PORT_TYPE
PUSBFN_PORT_TYPE = POINTER(_USBFN_PORT_TYPE)

# Possible USB Bus speeds
class _USBFN_BUS_SPEED(ENUM):
    UsbfnBusSpeedLow = 1
    UsbfnBusSpeedFull = 2
    UsbfnBusSpeedHigh = 3
    UsbfnBusSpeedSuper = 4
    UsbfnBusSpeedMaximum = 5


USBFN_BUS_SPEED = _USBFN_BUS_SPEED
PUSBFN_BUS_SPEED = POINTER(_USBFN_BUS_SPEED)

# Possible USB Bus transfer and endpoint directions
class _USBFN_DIRECTION(ENUM):
    UsbfnDirectionMinimum = 0x0
    UsbfnDirectionIn = 1
    UsbfnDirectionOut = 2
    UsbfnDirectionTx = UsbfnDirectionIn
    UsbfnDirectionRx = UsbfnDirectionOut
    UsbfnDirectionMaximum = 3


USBFN_DIRECTION = _USBFN_DIRECTION
PUSBFN_DIRECTION = POINTER(_USBFN_DIRECTION)

# These states indicated the current state of the USB driver.
# This should be used by class - extension clients only.
class _USBFN_DEVICE_STATE(ENUM):
    UsbfnDeviceStateMinimum = 0x0
    UsbfnDeviceStateAttached = 1
    UsbfnDeviceStateDefault = 2
    UsbfnDeviceStateDetached = 3
    UsbfnDeviceStateAddressed = 4
    UsbfnDeviceStateConfigured = 5
    UsbfnDeviceStateSuspended = 6
    UsbfnDeviceStateStateMaximum = 7


USBFN_DEVICE_STATE = _USBFN_DEVICE_STATE
PUSBFN_DEVICE_STATE = POINTER(_USBFN_DEVICE_STATE)
_ALTERNATE_INTERFACE._fields_ = [
    ('InterfaceNumber', USHORT),
    ('AlternateInterfaceNumber', USHORT),
]


# Notification structure used by class drivers to receive information
# about USBFN. Please see the definition of USBFN_EVENT to for details
# about each event.
class u(ctypes.Union):
    pass


u.__fields__ = [
    ('BusSpeed', USBFN_BUS_SPEED),
    ('SetupPacket', USB_DEFAULT_PIPE_SETUP_PACKET),
    ('ConfigurationValue', USHORT),
    ('PortType', USBFN_PORT_TYPE),
    ('AlternateInterface', ALTERNATE_INTERFACE),
]

_USBFN_NOTIFICATION.u = u

_USBFN_NOTIFICATION._fields_ = [
    ('Event', USBFN_EVENT),
    ('u', _USBFN_NOTIFICATION.u)
]

# Defines an endpoint pipe index (not the address)
USBFNPIPEID = ULONG
PUSBFNPIPEID = POINTER(USBFNPIPEID)
_USBFN_PIPE_INFORMATION._fields_ = [
    ('EpDesc', USB_ENDPOINT_DESCRIPTOR),
    ('PipeId', USBFNPIPEID),
]
_USBFN_CLASS_INTERFACE._fields_ = [
    ('InterfaceNumber', UINT8),
    ('PipeCount', UINT8),
    ('PipeArr', USBFN_PIPE_INFORMATION * MAX_NUM_USBFN_PIPES),
]
_USBFN_CLASS_INFORMATION_PACKET._fields_ = [
    ('FullSpeedClassInterface', USBFN_CLASS_INTERFACE),
    ('HighSpeedClassInterface', USBFN_CLASS_INTERFACE),
    ('InterfaceName', WCHAR * MAX_INTERFACE_NAME_LENGTH),
    ('InterfaceGuid', WCHAR * MAX_INTERFACE_GUID_LENGTH),
    ('HasInterfaceGuid', BOOLEAN),
    ('SuperSpeedClassInterface', USBFN_CLASS_INTERFACE),
]
_USBFN_CLASS_INTERFACE_EX._fields_ = [
    ('BaseInterfaceNumber', UINT8),
    ('InterfaceCount', UINT8),
    ('PipeCount', UINT8),
    ('PipeArr', USBFN_PIPE_INFORMATION * MAX_NUM_USBFN_PIPES),
]
_USBFN_CLASS_INFORMATION_PACKET_EX._fields_ = [
    ('FullSpeedClassInterfaceEx', USBFN_CLASS_INTERFACE_EX),
    ('HighSpeedClassInterfaceEx', USBFN_CLASS_INTERFACE_EX),
    ('SuperSpeedClassInterfaceEx', USBFN_CLASS_INTERFACE_EX),
    ('InterfaceName', WCHAR * MAX_INTERFACE_NAME_LENGTH),
    ('InterfaceGuid', WCHAR * MAX_INTERFACE_GUID_LENGTH),
    ('HasInterfaceGuid', BOOLEAN),
]
_USBFN_INTERFACE_INFO._fields_ = [
    ('InterfaceNumber', UINT8),
    ('Speed', USBFN_BUS_SPEED),
    ('Size', USHORT),
    ('InterfaceDescriptorSet', UCHAR * 1),
]
_USBFN_USB_STRING._fields_ = [
    ('StringIndex', UINT8),
    ('UsbString', WCHAR * MAX_USB_STRING_LENGTH),
]

# Configuration packet that gives information about
# an available configuration.
_USBFN_BUS_CONFIGURATION_INFO._fields_ = [
    ('ConfigurationName', WCHAR * MAX_CONFIGURATION_NAME_LENGTH), # NULL terminated wide CHAR string indicating the name of a configuration
    ('IsCurrent', BOOLEAN), # considered as current configuation.
    ('IsActive', BOOLEAN), # will be ignored in requests to Class extension.
]

