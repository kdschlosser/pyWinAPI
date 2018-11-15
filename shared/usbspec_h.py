import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.guiddef_h import *


class _BM_REQUEST_TYPE(ctypes.Union):
    pass


BM_REQUEST_TYPE = _BM_REQUEST_TYPE
PBM_REQUEST_TYPE = POINTER(_BM_REQUEST_TYPE)


class _USB_DEFAULT_PIPE_SETUP_PACKET(ctypes.Structure):
    pass


USB_DEFAULT_PIPE_SETUP_PACKET = _USB_DEFAULT_PIPE_SETUP_PACKET
PUSB_DEFAULT_PIPE_SETUP_PACKET = POINTER(_USB_DEFAULT_PIPE_SETUP_PACKET)


class _USB_DEVICE_STATUS(ctypes.Union):
    pass


USB_DEVICE_STATUS = _USB_DEVICE_STATUS
PUSB_DEVICE_STATUS = POINTER(_USB_DEVICE_STATUS)


class _USB_INTERFACE_STATUS(ctypes.Union):
    pass


USB_INTERFACE_STATUS = _USB_INTERFACE_STATUS
PUSB_INTERFACE_STATUS = POINTER(_USB_INTERFACE_STATUS)


class _USB_ENDPOINT_STATUS(ctypes.Union):
    pass


USB_ENDPOINT_STATUS = _USB_ENDPOINT_STATUS
PUSB_ENDPOINT_STATUS = POINTER(_USB_ENDPOINT_STATUS)


class _USB_COMMON_DESCRIPTOR(ctypes.Structure):
    pass


USB_COMMON_DESCRIPTOR = _USB_COMMON_DESCRIPTOR
PUSB_COMMON_DESCRIPTOR = POINTER(_USB_COMMON_DESCRIPTOR)


class _USB_DEVICE_DESCRIPTOR(ctypes.Structure):
    pass


USB_DEVICE_DESCRIPTOR = _USB_DEVICE_DESCRIPTOR
PUSB_DEVICE_DESCRIPTOR = POINTER(_USB_DEVICE_DESCRIPTOR)


class _USB_DEVICE_QUALIFIER_DESCRIPTOR(ctypes.Structure):
    pass


USB_DEVICE_QUALIFIER_DESCRIPTOR = _USB_DEVICE_QUALIFIER_DESCRIPTOR
PUSB_DEVICE_QUALIFIER_DESCRIPTOR = POINTER(_USB_DEVICE_QUALIFIER_DESCRIPTOR)


class _USB_BOS_DESCRIPTOR(ctypes.Structure):
    pass


USB_BOS_DESCRIPTOR = _USB_BOS_DESCRIPTOR
PUSB_BOS_DESCRIPTOR = POINTER(_USB_BOS_DESCRIPTOR)


class _USB_DEVICE_CAPABILITY_USB20_EXTENSION_DESCRIPTOR(ctypes.Structure):
    pass


USB_DEVICE_CAPABILITY_USB20_EXTENSION_DESCRIPTOR = _USB_DEVICE_CAPABILITY_USB20_EXTENSION_DESCRIPTOR
PUSB_DEVICE_CAPABILITY_USB20_EXTENSION_DESCRIPTOR = POINTER(_USB_DEVICE_CAPABILITY_USB20_EXTENSION_DESCRIPTOR)


class _USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR(ctypes.Structure):
    pass


USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR = _USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR
PUSB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR = POINTER(_USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR)


class _USB_DEVICE_CAPABILITY_PD_CONSUMER_PORT_DESCRIPTOR(ctypes.Structure):
    pass


USB_DEVICE_CAPABILITY_PD_CONSUMER_PORT_DESCRIPTOR = _USB_DEVICE_CAPABILITY_PD_CONSUMER_PORT_DESCRIPTOR
PUSB_DEVICE_CAPABILITY_PD_CONSUMER_PORT_DESCRIPTOR = POINTER(_USB_DEVICE_CAPABILITY_PD_CONSUMER_PORT_DESCRIPTOR)


class _USB_DEVICE_CAPABILITY_SUPERSPEED_USB_DESCRIPTOR(ctypes.Structure):
    pass


USB_DEVICE_CAPABILITY_SUPERSPEED_USB_DESCRIPTOR = _USB_DEVICE_CAPABILITY_SUPERSPEED_USB_DESCRIPTOR
PUSB_DEVICE_CAPABILITY_SUPERSPEED_USB_DESCRIPTOR = POINTER(_USB_DEVICE_CAPABILITY_SUPERSPEED_USB_DESCRIPTOR)


class _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED(ctypes.Union):
    pass


USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED = _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED
PUSB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED = POINTER(_USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED)


class _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_USB_DESCRIPTOR(ctypes.Structure):
    pass


USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_USB_DESCRIPTOR = _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_USB_DESCRIPTOR
PUSB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_USB_DESCRIPTOR = POINTER(_USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_USB_DESCRIPTOR)


class _USB_DEVICE_CAPABILITY_CONTAINER_ID_DESCRIPTOR(ctypes.Structure):
    pass


USB_DEVICE_CAPABILITY_CONTAINER_ID_DESCRIPTOR = _USB_DEVICE_CAPABILITY_CONTAINER_ID_DESCRIPTOR
PUSB_DEVICE_CAPABILITY_CONTAINER_ID_DESCRIPTOR = POINTER(_USB_DEVICE_CAPABILITY_CONTAINER_ID_DESCRIPTOR)


class _USB_DEVICE_CAPABILITY_PLATFORM_DESCRIPTOR(ctypes.Structure):
    pass


USB_DEVICE_CAPABILITY_PLATFORM_DESCRIPTOR = _USB_DEVICE_CAPABILITY_PLATFORM_DESCRIPTOR
PUSB_DEVICE_CAPABILITY_PLATFORM_DESCRIPTOR = POINTER(_USB_DEVICE_CAPABILITY_PLATFORM_DESCRIPTOR)


class _USB_DEVICE_CAPABILITY_BILLBOARD_DESCRIPTOR(ctypes.Structure):
    pass


USB_DEVICE_CAPABILITY_BILLBOARD_DESCRIPTOR = _USB_DEVICE_CAPABILITY_BILLBOARD_DESCRIPTOR
PUSB_DEVICE_CAPABILITY_BILLBOARD_DESCRIPTOR = POINTER(_USB_DEVICE_CAPABILITY_BILLBOARD_DESCRIPTOR)


class _USB_DEVICE_CAPABILITY_DESCRIPTOR(ctypes.Structure):
    pass


USB_DEVICE_CAPABILITY_DESCRIPTOR = _USB_DEVICE_CAPABILITY_DESCRIPTOR
PUSB_DEVICE_CAPABILITY_DESCRIPTOR = POINTER(_USB_DEVICE_CAPABILITY_DESCRIPTOR)


class _USB_CONFIGURATION_DESCRIPTOR(ctypes.Structure):
    pass


USB_CONFIGURATION_DESCRIPTOR = _USB_CONFIGURATION_DESCRIPTOR
PUSB_CONFIGURATION_DESCRIPTOR = POINTER(_USB_CONFIGURATION_DESCRIPTOR)


class _USB_INTERFACE_ASSOCIATION_DESCRIPTOR(ctypes.Structure):
    pass


USB_INTERFACE_ASSOCIATION_DESCRIPTOR = _USB_INTERFACE_ASSOCIATION_DESCRIPTOR
PUSB_INTERFACE_ASSOCIATION_DESCRIPTOR = POINTER(_USB_INTERFACE_ASSOCIATION_DESCRIPTOR)


class _USB_INTERFACE_DESCRIPTOR(ctypes.Structure):
    pass


USB_INTERFACE_DESCRIPTOR = _USB_INTERFACE_DESCRIPTOR
PUSB_INTERFACE_DESCRIPTOR = POINTER(_USB_INTERFACE_DESCRIPTOR)


class _USB_ENDPOINT_DESCRIPTOR(ctypes.Structure):
    pass


USB_ENDPOINT_DESCRIPTOR = _USB_ENDPOINT_DESCRIPTOR
PUSB_ENDPOINT_DESCRIPTOR = POINTER(_USB_ENDPOINT_DESCRIPTOR)


class _USB_HIGH_SPEED_MAXPACKET(ctypes.Union):
    pass


USB_HIGH_SPEED_MAXPACKET = _USB_HIGH_SPEED_MAXPACKET
PUSB_HIGH_SPEED_MAXPACKET = POINTER(_USB_HIGH_SPEED_MAXPACKET)


class _USB_STRING_DESCRIPTOR(ctypes.Structure):
    pass


USB_STRING_DESCRIPTOR = _USB_STRING_DESCRIPTOR
PUSB_STRING_DESCRIPTOR = POINTER(_USB_STRING_DESCRIPTOR)


class _USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR(ctypes.Structure):
    pass


USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR = _USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR
PUSB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR = POINTER(_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR)


class _USB_SUPERSPEEDPLUS_ISOCH_ENDPOINT_COMPANION_DESCRIPTOR(ctypes.Structure):
    pass


USB_SUPERSPEEDPLUS_ISOCH_ENDPOINT_COMPANION_DESCRIPTOR = _USB_SUPERSPEEDPLUS_ISOCH_ENDPOINT_COMPANION_DESCRIPTOR
PUSB_SUPERSPEEDPLUS_ISOCH_ENDPOINT_COMPANION_DESCRIPTOR = POINTER(_USB_SUPERSPEEDPLUS_ISOCH_ENDPOINT_COMPANION_DESCRIPTOR)


class _USB_HUB_DESCRIPTOR(ctypes.Structure):
    pass


USB_HUB_DESCRIPTOR = _USB_HUB_DESCRIPTOR
PUSB_HUB_DESCRIPTOR = POINTER(_USB_HUB_DESCRIPTOR)


class _USB_30_HUB_DESCRIPTOR(ctypes.Structure):
    pass


USB_30_HUB_DESCRIPTOR = _USB_30_HUB_DESCRIPTOR
PUSB_30_HUB_DESCRIPTOR = POINTER(_USB_30_HUB_DESCRIPTOR)


class _USB_HUB_STATUS(ctypes.Union):
    pass


USB_HUB_STATUS = _USB_HUB_STATUS
PUSB_HUB_STATUS = POINTER(_USB_HUB_STATUS)


class _USB_HUB_CHANGE(ctypes.Union):
    pass


USB_HUB_CHANGE = _USB_HUB_CHANGE
PUSB_HUB_CHANGE = POINTER(_USB_HUB_CHANGE)


class _USB_HUB_STATUS_AND_CHANGE(ctypes.Union):
    pass


USB_HUB_STATUS_AND_CHANGE = _USB_HUB_STATUS_AND_CHANGE
PUSB_HUB_STATUS_AND_CHANGE = POINTER(_USB_HUB_STATUS_AND_CHANGE)


class _USB_20_PORT_STATUS(ctypes.Union):
    pass


USB_20_PORT_STATUS = _USB_20_PORT_STATUS
PUSB_20_PORT_STATUS = POINTER(_USB_20_PORT_STATUS)


class _USB_20_PORT_CHANGE(ctypes.Union):
    pass


USB_20_PORT_CHANGE = _USB_20_PORT_CHANGE
PUSB_20_PORT_CHANGE = POINTER(_USB_20_PORT_CHANGE)


class _USB_30_PORT_STATUS(ctypes.Union):
    pass


USB_30_PORT_STATUS = _USB_30_PORT_STATUS
PUSB_30_PORT_STATUS = POINTER(_USB_30_PORT_STATUS)


class _USB_30_PORT_CHANGE(ctypes.Union):
    pass


USB_30_PORT_CHANGE = _USB_30_PORT_CHANGE
PUSB_30_PORT_CHANGE = POINTER(_USB_30_PORT_CHANGE)


class _USB_PORT_STATUS(ctypes.Union):
    pass


USB_PORT_STATUS = _USB_PORT_STATUS
PUSB_PORT_STATUS = POINTER(_USB_PORT_STATUS)


class _USB_PORT_CHANGE(ctypes.Union):
    pass


USB_PORT_CHANGE = _USB_PORT_CHANGE
PUSB_PORT_CHANGE = POINTER(_USB_PORT_CHANGE)


class _USB_PORT_EXT_STATUS(ctypes.Union):
    pass


USB_PORT_EXT_STATUS = _USB_PORT_EXT_STATUS
PUSB_PORT_EXT_STATUS = POINTER(_USB_PORT_EXT_STATUS)


class _USB_PORT_STATUS_AND_CHANGE(ctypes.Union):
    pass


USB_PORT_STATUS_AND_CHANGE = _USB_PORT_STATUS_AND_CHANGE
PUSB_PORT_STATUS_AND_CHANGE = POINTER(_USB_PORT_STATUS_AND_CHANGE)


class _USB_PORT_EXT_STATUS_AND_CHANGE(ctypes.Union):
    pass


USB_PORT_EXT_STATUS_AND_CHANGE = _USB_PORT_EXT_STATUS_AND_CHANGE
PUSB_PORT_EXT_STATUS_AND_CHANGE = POINTER(_USB_PORT_EXT_STATUS_AND_CHANGE)


class _USB_HUB_30_PORT_REMOTE_WAKE_MASK(ctypes.Union):
    pass


USB_HUB_30_PORT_REMOTE_WAKE_MASK = _USB_HUB_30_PORT_REMOTE_WAKE_MASK
PUSB_HUB_30_PORT_REMOTE_WAKE_MASK = POINTER(_USB_HUB_30_PORT_REMOTE_WAKE_MASK)


class _USB_FUNCTION_SUSPEND_OPTIONS(ctypes.Union):
    pass


USB_FUNCTION_SUSPEND_OPTIONS = _USB_FUNCTION_SUSPEND_OPTIONS
PUSB_FUNCTION_SUSPEND_OPTIONS = POINTER(_USB_FUNCTION_SUSPEND_OPTIONS)


class _USB_CONFIGURATION_POWER_DESCRIPTOR(ctypes.Structure):
    pass


USB_CONFIGURATION_POWER_DESCRIPTOR = _USB_CONFIGURATION_POWER_DESCRIPTOR
PUSB_CONFIGURATION_POWER_DESCRIPTOR = POINTER(_USB_CONFIGURATION_POWER_DESCRIPTOR)


class _USB_INTERFACE_POWER_DESCRIPTOR(ctypes.Structure):
    pass


USB_INTERFACE_POWER_DESCRIPTOR = _USB_INTERFACE_POWER_DESCRIPTOR
PUSB_INTERFACE_POWER_DESCRIPTOR = POINTER(_USB_INTERFACE_POWER_DESCRIPTOR)


# Copyright (C) Microsoft. All rights reserved.
# This header file contains definitions based on information contained
# in the following Universal Serial Bus Specifications:
# Universal Serial Bus Specification, Revision 1.1, September 23, 1998
# Universal Serial Bus Specification, Revision 2.0, April 27, 2000
# Universal Serial Bus 3.0 Specification, Revision 1.0, November 12, 2008
# Universal Serial Bus 3.1 Specification, Revision 1.0, July 26, 2013
# Refer to the referenced sections in these specifications for further
# information.

__USBSPEC_H__ = None
if not defined(__USBSPEC_H__):
    __USBSPEC_H__ = 1
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if _MSC_VER >= 1200:
            pass
        # END IF

        # These definitions are not USB specification definitions and do not
        # beLONG in this header file. They are only here to preserve
        # compatibility with the previous usb200.h header file.
        class _USB_DEVICE_SPEED(ENUM):
            UsbLowSpeed = 0
            UsbFullSpeed = 1
            UsbHighSpeed = 2
            UsbSuperSpeed = 3


        USB_DEVICE_SPEED = _USB_DEVICE_SPEED


        class _USB_DEVICE_TYPE(ENUM):
            Usb11Device = 0
            Usb20Device = 1


        USB_DEVICE_TYPE = _USB_DEVICE_TYPE

        # Chapter 9 USB Device Framework
        # USB 1.1: 9.3 USB Device Requests, Table 9 - 2. Format of Setup Data
        # USB 2.1: 9.3 USB Device Requests, Table 9 - 2. Format of Setup Data
        # USB 3.0: 9.3 USB Device Requests, Table 9 - 2. Format of Setup Data
        class _Struct_1(ctypes.Structure):
            pass


        _Struct_1._fields_ = [
            ('Recipient', UCHAR, 2),
            ('Reserved', UCHAR, 3),
            ('Type', UCHAR, 2),
            ('Dir', UCHAR, 1),
        ]
        _BM_REQUEST_TYPE._Struct_1 = _Struct_1

        _BM_REQUEST_TYPE._anonymous_ = (
            '_Struct_1',
        )
        _BM_REQUEST_TYPE._fields_ = [
            ('_Struct_1', _BM_REQUEST_TYPE._Struct_1),
            ('B', UCHAR),
        ]


        class wValue(ctypes.Structure):
            pass


        class _Struct_2(ctypes.Structure):
            pass


        _Struct_2._fields_ = [
            ('LowByte', UCHAR),
            ('HiByte', UCHAR),
        ]
        wValue._Struct_2 = _Struct_2

        wValue._anonymous_ = (
            '_Struct_2',
        )
        wValue._fields_ = [
            ('_Struct_2', wValue._Struct_2),
            ('W', USHORT),
        ]
        _USB_DEFAULT_PIPE_SETUP_PACKET.wValue = wValue


        class wIndex(ctypes.Structure):
            pass


        class _Struct_2(ctypes.Structure):
            pass


        _Struct_2._fields_ = [
            ('LowByte', UCHAR),
            ('HiByte', UCHAR),
        ]
        wIndex._Struct_2 = _Struct_2

        wIndex._anonymous_ = (
            '_Struct_2',
        )
        wIndex._fields_ = [
            ('_Struct_2', wIndex._Struct_2),
            ('W', USHORT),
        ]
        _USB_DEFAULT_PIPE_SETUP_PACKET.wIndex = wIndex

        _USB_DEFAULT_PIPE_SETUP_PACKET._fields_ = [
            ('bmRequestType', BM_REQUEST_TYPE),
            ('bRequest', UCHAR),
            ('wValue', _USB_DEFAULT_PIPE_SETUP_PACKET.wValue),
            ('wIndex', _USB_DEFAULT_PIPE_SETUP_PACKET.wIndex),
            ('wLength', USHORT),
        ]

        # bmRequestType.Dir
        BMREQUEST_HOST_TO_DEVICE = 0
        BMREQUEST_DEVICE_TO_HOST = 1

        # bmRequestType.Type
        BMREQUEST_STANDARD = 0
        BMREQUEST_CLASS = 1
        BMREQUEST_VENDOR = 2

        # bmRequestType.Recipient
        BMREQUEST_TO_DEVICE = 0
        BMREQUEST_TO_INTERFACE = 1
        BMREQUEST_TO_ENDPOINT = 2
        BMREQUEST_TO_OTHER = 3

        # wValue for Get Descriptor request
        def USB_DESCRIPTOR_MAKE_TYPE_AND_INDEX(d, i):
            return (d << 8) | i

        # USB 1.1: 9.4 Standard Device Requests, Table 9 - 4. Standard Request
        # Codes
        # USB 2.0: 9.4 Standard Device Requests, Table 9 - 4. Standard Request
        # Codes
        USB_REQUEST_GET_STATUS = 0x00
        USB_REQUEST_CLEAR_FEATURE = 0x01
        USB_REQUEST_SET_FEATURE = 0x03
        USB_REQUEST_SET_ADDRESS = 0x05
        USB_REQUEST_GET_DESCRIPTOR = 0x06
        USB_REQUEST_SET_DESCRIPTOR = 0x07
        USB_REQUEST_GET_CONFIGURATION = 0x08
        USB_REQUEST_SET_CONFIGURATION = 0x09
        USB_REQUEST_GET_INTERFACE = 0x0A
        USB_REQUEST_SET_INTERFACE = 0x0B
        USB_REQUEST_SYNC_FRAME = 0x0C

        # USB 3.0: 9.4 Standard Device Requests, Table 9 - 4. Standard Request
        # Codes
        USB_REQUEST_SET_SEL = 0x30
        USB_REQUEST_ISOCH_DELAY = 0x31

        # USB 1.1: 9.4 Standard Device Requests, Table 9 - 5. Descriptor Types
        USB_DEVICE_DESCRIPTOR_TYPE = 0x01
        USB_CONFIGURATION_DESCRIPTOR_TYPE = 0x02
        USB_STRING_DESCRIPTOR_TYPE = 0x03
        USB_INTERFACE_DESCRIPTOR_TYPE = 0x04
        USB_ENDPOINT_DESCRIPTOR_TYPE = 0x05

        # USB 2.0: 9.4 Standard Device Requests, Table 9 - 5. Descriptor Types
        USB_DEVICE_QUALIFIER_DESCRIPTOR_TYPE = 0x06
        USB_OTHER_SPEED_CONFIGURATION_DESCRIPTOR_TYPE = 0x07
        USB_INTERFACE_POWER_DESCRIPTOR_TYPE = 0x08

        # USB 3.0: 9.4 Standard Device Requests, Table 9 - 5. Descriptor Types
        USB_OTG_DESCRIPTOR_TYPE = 0x09
        USB_DEBUG_DESCRIPTOR_TYPE = 0x0A
        USB_INTERFACE_ASSOCIATION_DESCRIPTOR_TYPE = 0x0B
        USB_BOS_DESCRIPTOR_TYPE = 0x0F
        USB_DEVICE_CAPABILITY_DESCRIPTOR_TYPE = 0x10
        USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR_TYPE = 0x30

        # USB 3.1: 9.4 Standard Device Requests, Table 9 - 6. Descriptor Types
        USB_SUPERSPEEDPLUS_ISOCH_ENDPOINT_COMPANION_DESCRIPTOR_TYPE = 0x31

        # Legacy definitions, do not use.
        USB_RESERVED_DESCRIPTOR_TYPE = 0x06
        USB_CONFIG_POWER_DESCRIPTOR_TYPE = 0x07

        # USB 1.1: 9.4 Standard Device Requests, Table 9 - 6. Standard Feature
        # Selectors
        USB_FEATURE_ENDPOINT_STALL = 0x00
        USB_FEATURE_REMOTE_WAKEUP = 0x01

        # USB 2.0: 9.4 Standard Device Requests, Table 9 - 6. Standard Feature
        # Selectors
        USB_FEATURE_TEST_MODE = 0x02

        # USB 3.0: 9.4 Standard Device Requests, Table 9 - 6. Standard Feature
        # Selectors
        USB_FEATURE_FUNCTION_SUSPEND = 0x00
        USB_FEATURE_U1_ENABLE = 0x30
        USB_FEATURE_U2_ENABLE = 0x31
        USB_FEATURE_LTM_ENABLE = 0x32

        # USB 3.1: 9.4 Standard Device Requests, Table 9 - 7. Standard Feature
        # Selectors
        USB_FEATURE_LDM_ENABLE = 0x35

        # USBPD Rev2.0: 9.3.1 Class - specific Device Requests, Table 9 - 8
        # PD. Class Feature Selectors
        USB_FEATURE_BATTERY_WAKE_MASK = 0x28
        USB_FEATURE_OS_IS_PD_AWARE = 0x29
        USB_FEATURE_POLICY_MODE = 0x2A
        USB_FEATURE_CHARGING_POLICY = 0x36

        # USBPD Rev2.0: 9.4.5.4 CHARGING_POLICY Feature Selector
        USB_CHARGING_POLICY_DEFAULT = 0x00
        USB_CHARGING_POLICY_ICCHPF = 0x01
        USB_CHARGING_POLICY_ICCLPF = 0x02
        USB_CHARGING_POLICY_NO_POWER = 0x03

        # USB 3.1: 10.16.2.6 Get Port Status, Table 10 - 12. Port Status Type
        # Codes
        USB_STATUS_PORT_STATUS = 0x00
        USB_STATUS_PD_STATUS = 0x01
        USB_STATUS_EXT_PORT_STATUS = 0x02

        # USB 1.1: 9.4.5 Get Status, Figure 9 - 4. Information Returned by a
        # GetStatus() Request to a Device
        # USB 2.0: 9.4.5 Get Status, Figure 9 - 4. Information Returned by a
        # GetStatus() Request to a Device
        USB_GETSTATUS_SELF_POWERED = 0x01
        USB_GETSTATUS_REMOTE_WAKEUP_ENABLED = 0x02

        # USB 3.0: 9.4.5 Get Status, Figure 9 - 5. Information Returned by a
        # GetStatus() Request to a Device
        USB_GETSTATUS_U1_ENABLE = 0x04
        USB_GETSTATUS_U2_ENABLE = 0x08
        USB_GETSTATUS_LTM_ENABLE = 0x10


        class _Struct_2(ctypes.Structure):
            pass


        _Struct_2._fields_ = [
            ('SelfPowered', USHORT, 1),
            ('RemoteWakeup', USHORT, 1),
            ('U1Enable', USHORT, 1), # (USB 1.1, USB 2.0 Reserved)
            ('U2Enable', USHORT, 1), # (USB 1.1, USB 2.0 Reserved)
            ('LtmEnable', USHORT, 1), # (USB 1.1, USB 2.0 Reserved)
            ('Reserved', USHORT, 11),
        ]
        _USB_DEVICE_STATUS._Struct_2 = _Struct_2

        _USB_DEVICE_STATUS._anonymous_ = (
            '_Struct_2',
        )
        _USB_DEVICE_STATUS._fields_ = [
            ('AsUSHORT16', USHORT),
            ('_Struct_2', _USB_DEVICE_STATUS._Struct_2),
        ]

        # USB 3.0: 9.4.5 Get Status, Figure 9 - 6. Information Returned by a
        # GetStatus() Request to an Interface
        class _Struct_3(ctypes.Structure):
            pass


        _Struct_3._fields_ = [
            ('RemoteWakeupCapable', USHORT, 1),
            ('RemoteWakeupEnabled', USHORT, 1),
            ('Reserved', USHORT, 14),
        ]
        _USB_INTERFACE_STATUS._Struct_3 = _Struct_3

        _USB_INTERFACE_STATUS._anonymous_ = (
            '_Struct_3',
        )
        _USB_INTERFACE_STATUS._fields_ = [
            ('AsUSHORT16', USHORT),
            ('_Struct_3', _USB_INTERFACE_STATUS._Struct_3),
        ]

        # USB 1.1: 9.4.5 Get Status, Figure 9 - 6. Information Returned by a
        # GetStatus() Request to an Endpoint
        # USB 2.0: 9.4.5 Get Status, Figure 9 - 6. Information Returned by a
        # GetStatus() Request to an Endpoint
        # USB 3.0: 9.4.5 Get Status, Figure 9 - 7. Information Returned by a
        # GetStatus() Request to an Endpoint
        class _Struct_4(ctypes.Structure):
            pass


        _Struct_4._fields_ = [
            ('Halt', USHORT, 1),
            ('Reserved', USHORT, 15),
        ]
        _USB_ENDPOINT_STATUS._Struct_4 = _Struct_4

        _USB_ENDPOINT_STATUS._anonymous_ = (
            '_Struct_4',
        )
        _USB_ENDPOINT_STATUS._fields_ = [
            ('AsUSHORT16', USHORT),
            ('_Struct_4', _USB_ENDPOINT_STATUS._Struct_4),
        ]
        _USB_COMMON_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
        ]

        # USB 1.1: 9.6.1 Device, Table 9 - 7. Standard Device Descriptor
        # USB 2.0: 9.6.1 Device, Table 9 - 8. Standard Device Descriptor
        # USB 3.0: 9.6.1 Device, Table 9 - 8. Standard Device Descriptor
        _USB_DEVICE_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bcdUSB', USHORT),
            ('bDeviceClass', UCHAR),
            ('bDeviceSubClass', UCHAR),
            ('bDeviceProtocol', UCHAR),
            ('bMaxPacketSize0', UCHAR),
            ('idVendor', USHORT),
            ('idProduct', USHORT),
            ('bcdDevice', USHORT),
            ('iManufacturer', UCHAR),
            ('iProduct', UCHAR),
            ('iSerialNumber', UCHAR),
            ('bNumConfigurations', UCHAR),
        ]

        # With the exception of the HUB device class, USB class codes are not
        # defined in the core USB 1.1, 2.0, 3.0 specifications.
        USB_DEVICE_CLASS_RESERVED = 0x00
        USB_DEVICE_CLASS_AUDIO = 0x01
        USB_DEVICE_CLASS_COMMUNICATIONS = 0x02
        USB_DEVICE_CLASS_HUMAN_INTERFACE = 0x03
        USB_DEVICE_CLASS_MONITOR = 0x04
        USB_DEVICE_CLASS_PHYSICAL_INTERFACE = 0x05
        USB_DEVICE_CLASS_POWER = 0x06
        USB_DEVICE_CLASS_IMAGE = 0x06
        USB_DEVICE_CLASS_PRINTER = 0x07
        USB_DEVICE_CLASS_STORAGE = 0x08
        USB_DEVICE_CLASS_HUB = 0x09
        USB_DEVICE_CLASS_CDC_DATA = 0x0A
        USB_DEVICE_CLASS_SMART_CARD = 0x0B
        USB_DEVICE_CLASS_CONTENT_SECURITY = 0x0D
        USB_DEVICE_CLASS_VIDEO = 0x0E
        USB_DEVICE_CLASS_PERSONAL_HEALTHCARE = 0x0F
        USB_DEVICE_CLASS_AUDIO_VIDEO = 0x10
        USB_DEVICE_CLASS_BILLBOARD = 0x11
        USB_DEVICE_CLASS_DIAGNOSTIC_DEVICE = 0xDC
        USB_DEVICE_CLASS_WIRELESS_CONTROLLER = 0xE0
        USB_DEVICE_CLASS_MISCELLANEOUS = 0xEF
        USB_DEVICE_CLASS_APPLICATION_SPECIFIC = 0xFE
        USB_DEVICE_CLASS_VENDOR_SPECIFIC = 0xFF

        # USB 2.0: 9.6.2 Device_Qualifier, Table 9 - 9. Device_Qualifier
        # Descriptor
        _USB_DEVICE_QUALIFIER_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bcdUSB', USHORT),
            ('bDeviceClass', UCHAR),
            ('bDeviceSubClass', UCHAR),
            ('bDeviceProtocol', UCHAR),
            ('bMaxPacketSize0', UCHAR),
            ('bNumConfigurations', UCHAR),
            ('bReserved', UCHAR),
        ]

        # USB 3.0: 9.6.2 Binary Device Object Store (BOS), Table 9 - 9. BOS
        # Descriptor
        _USB_BOS_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('wTotalLength', USHORT),
            ('bNumDeviceCaps', UCHAR),
        ]

        # USB 3.1: 9.6.2 Binary Device Object Store (BOS), Table 9 - 14.
        # Device Capability Type Codes
        USB_DEVICE_CAPABILITY_WIRELESS_USB = 0x01
        USB_DEVICE_CAPABILITY_USB20_EXTENSION = 0x02
        USB_DEVICE_CAPABILITY_SUPERSPEED_USB = 0x03
        USB_DEVICE_CAPABILITY_CONTAINER_ID = 0x04
        USB_DEVICE_CAPABILITY_PLATFORM = 0x05
        USB_DEVICE_CAPABILITY_POWER_DELIVERY = 0x06
        USB_DEVICE_CAPABILITY_BATTERY_INFO = 0x07
        USB_DEVICE_CAPABILITY_PD_CONSUMER_PORT = 0x08
        USB_DEVICE_CAPABILITY_PD_PROVIDER_PORT = 0x09
        USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_USB = 0x0A
        USB_DEVICE_CAPABILITY_PRECISION_TIME_MEASUREMENT = 0x0B
        USB_DEVICE_CAPABILITY_BILLBOARD = 0x0D

        # USB 2.0 ECN: Link Power Management (LPM), 3. Framework: USB Device
        # Capabilities - USB 2.0 Extension,
        # Table 3 - 1. USB Device Capabilities - USB 2.0 Extension Descriptor
        # USB 3.0: 9.6.2.1 USB 2.0 Extension, Table 9 - 12. USB 2.0 Extension
        # Descriptor
        class bmAttributes(ctypes.Structure):
            pass


        class _Struct_5(ctypes.Structure):
            pass


        _Struct_5._fields_ = [
            ('Reserved', ULONG, 1),
            ('LPMCapable', ULONG, 1),
            ('BESLAndAlternateHIRDSupported', ULONG, 1),
            ('BaselineBESLValid', ULONG, 1),
            ('DeepBESLValid', ULONG, 1),
            ('Reserved1', ULONG, 3),
            ('BaselineBESL', ULONG, 4),
            ('DeepBESL', ULONG, 4),
            ('Reserved2', ULONG, 16),
        ]
        bmAttributes._Struct_5 = _Struct_5

        bmAttributes._anonymous_ = (
            '_Struct_5',
        )
        bmAttributes._fields_ = [
            ('AsULONG', ULONG),
            ('_Struct_5', bmAttributes._Struct_5),
        ]
        _USB_DEVICE_CAPABILITY_USB20_EXTENSION_DESCRIPTOR.bmAttributes = bmAttributes

        _USB_DEVICE_CAPABILITY_USB20_EXTENSION_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bDevCapabilityType', UCHAR),
            ('bmAttributes', _USB_DEVICE_CAPABILITY_USB20_EXTENSION_DESCRIPTOR.bmAttributes),
        ]
        USB_DEVICE_CAPABILITY_USB20_EXTENSION_BMATTRIBUTES_RESERVED_MASK = (
            0xFFFF00E1
        )

        # USBPD Rev2.0: 9.2.1 USB Power Delivery Capability Descriptor, Table
        # 9 - 2. USB Power Delivery Capability Descriptor
        class bmAttributes(ctypes.Structure):
            pass


        class _Struct_5(ctypes.Structure):
            pass


        _Struct_5._fields_ = [
            ('Reserved1', ULONG, 1),
            ('BatteryCharging', ULONG, 1),
            ('USBPowerDelivery', ULONG, 1),
            ('Provider', ULONG, 1),
            ('Consumer', ULONG, 1),
            ('ChargingPolicy', ULONG, 1),
            ('TypeCCurrent', ULONG, 1),
            ('Reserved2', ULONG, 1),
            ('ACSupply', ULONG, 1),
            ('Battery', ULONG, 1),
            ('Other', ULONG, 1),
            ('NumBatteries', ULONG, 3),
            ('UsesVbus', ULONG, 1),
            ('Reserved3', ULONG, 17),
        ]
        bmAttributes._Struct_5 = _Struct_5

        bmAttributes._anonymous_ = (
            '_Struct_5',
        )
        bmAttributes._fields_ = [
            ('AsULONG', ULONG),
            ('_Struct_5', bmAttributes._Struct_5),
        ]
        _USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR.bmAttributes = bmAttributes

        _USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bDevCapabilityType', UCHAR),
            ('bReserved', UCHAR),
            ('bmAttributes', _USB_DEVICE_CAPABILITY_POWER_DELIVERY_DESCRIPTOR.bmAttributes),
            ('bmProviderPorts', USHORT),
            ('bmConsumerPorts', USHORT),
            ('bcdBCVersion', USHORT),
            ('bcdPDVersion', USHORT),
            ('bcdUSBTypeCVersion', USHORT),
        ]

        # USBPD Rev2.0: 9.2.3 PD Consumer Port Capability Descriptor, Table 9
        # - 4. PD Consumer Port Descriptor
        class bmCapabilities(ctypes.Structure):
            pass


        class _Struct_5(ctypes.Structure):
            pass


        _Struct_5._fields_ = [
            ('BatteryCharging', USHORT, 1),
            ('USBPowerDelivery', USHORT, 1),
            ('USBTypeCCurrent', USHORT, 1),
            ('Reserved', USHORT, 13),
        ]
        bmCapabilities._Struct_5 = _Struct_5

        bmCapabilities._anonymous_ = (
            '_Struct_5',
        )
        bmCapabilities._fields_ = [
            ('AsUSHORT', USHORT),
            ('_Struct_5', bmCapabilities._Struct_5),
        ]
        _USB_DEVICE_CAPABILITY_PD_CONSUMER_PORT_DESCRIPTOR.bmCapabilities = bmCapabilities

        _USB_DEVICE_CAPABILITY_PD_CONSUMER_PORT_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bDevCapabilityType', UCHAR),
            ('bReserved', UCHAR),
            ('bmCapabilities', _USB_DEVICE_CAPABILITY_PD_CONSUMER_PORT_DESCRIPTOR.bmCapabilities),
            ('wMinVoltage', USHORT),
            ('wMaxVoltage', USHORT),
            ('wReserved', USHORT),
            ('dwMaxOperatingPower', ULONG),
            ('dwMaxPeakPower', ULONG),
            ('dwMaxPeakPowerTime', ULONG),
        ]

        # USB 3.0: 9.6.2.2 SuperSpeed USB Device Capability, Table 9 - 13.
        # SuperSpeed Device Capabilities Descriptor
        _USB_DEVICE_CAPABILITY_SUPERSPEED_USB_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bDevCapabilityType', UCHAR),
            ('bmAttributes', UCHAR), # needs bitfield definitions
            ('wSpeedsSupported', USHORT), # needs bitfield definitions
            ('bFunctionalitySupport', UCHAR),
            ('bU1DevExitLat', UCHAR),
            ('wU2DevExitLat', USHORT),
        ]
        USB_DEVICE_CAPABILITY_SUPERSPEED_BMATTRIBUTES_RESERVED_MASK = 0xFD
        USB_DEVICE_CAPABILITY_SUPERSPEED_BMATTRIBUTES_LTM_CAPABLE = 0x02
        USB_DEVICE_CAPABILITY_SUPERSPEED_SPEEDS_SUPPORTED_RESERVED_MASK = (
            0xFFF0
        )
        USB_DEVICE_CAPABILITY_SUPERSPEED_SPEEDS_SUPPORTED_LOW = 0x0001
        USB_DEVICE_CAPABILITY_SUPERSPEED_SPEEDS_SUPPORTED_FULL = 0x0002
        USB_DEVICE_CAPABILITY_SUPERSPEED_SPEEDS_SUPPORTED_HIGH = 0x0004
        USB_DEVICE_CAPABILITY_SUPERSPEED_SPEEDS_SUPPORTED_SUPER = 0x0008
        USB_DEVICE_CAPABILITY_SUPERSPEED_U1_DEVICE_EXIT_MAX_VALUE = 0x0A
        USB_DEVICE_CAPABILITY_SUPERSPEED_U2_DEVICE_EXIT_MAX_VALUE = 0x07FF
        USB_DEVICE_CAPABILITY_MAX_U1_LATENCY = 0x0A
        USB_DEVICE_CAPABILITY_MAX_U2_LATENCY = 0x07FF

        # USB 3.1: 9.6.2.5 SuperSpeedPlus USB Device Capability, Table 9 - 19.
        # SuperSpeedPlus Device Capabilities Descriptor
        USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED_LSE_BPS = 0
        USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED_LSE_KBPS = 1
        USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED_LSE_MBPS = 2
        USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED_LSE_GBPS = 3
        USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED_MODE_SYMMETRIC = 0
        USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED_MODE_ASYMMETRIC = 1
        USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED_DIR_RX = 0
        USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED_DIR_TX = 1
        USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED_PROTOCOL_SS = 0
        USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED_PROTOCOL_SSP = 1


        class _Struct_5(ctypes.Structure):
            pass


        _Struct_5._fields_ = [
            ('SublinkSpeedAttrID', ULONG, 4),
            ('LaneSpeedExponent', ULONG, 2),
            ('SublinkTypeMode', ULONG, 1),
            ('SublinkTypeDir', ULONG, 1),
            ('Reserved', ULONG, 6),
            ('LinkProtocol', ULONG, 2),
            ('LaneSpeedMantissa', ULONG, 16),
        ]
        _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED._Struct_5 = _Struct_5

        _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED._anonymous_ = (
            '_Struct_5',
        )
        _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED._fields_ = [
            ('AsULONG32', ULONG),
            ('_Struct_5', _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED._Struct_5),
        ]


        class bmAttributes(ctypes.Structure):
            pass


        class _Struct_6(ctypes.Structure):
            pass


        _Struct_6._fields_ = [
            ('SublinkSpeedAttrCount', ULONG, 5),
            ('SublinkSpeedIDCount', ULONG, 4),
            ('Reserved', ULONG, 23),
        ]
        bmAttributes._Struct_6 = _Struct_6

        bmAttributes._anonymous_ = (
            '_Struct_6',
        )
        bmAttributes._fields_ = [
            ('AsULONG', ULONG),
            ('_Struct_6', bmAttributes._Struct_6),
        ]
        _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_USB_DESCRIPTOR.bmAttributes = bmAttributes


        class wFunctionalitySupport(ctypes.Structure):
            pass


        class _Struct_6(ctypes.Structure):
            pass


        _Struct_6._fields_ = [
            ('SublinkSpeedAttrID', USHORT, 4),
            ('Reserved', USHORT, 4),
            ('MinRxLaneCount', USHORT, 4),
            ('MinTxLaneCount', USHORT, 4),
        ]
        wFunctionalitySupport._Struct_6 = _Struct_6

        wFunctionalitySupport._anonymous_ = (
            '_Struct_6',
        )
        wFunctionalitySupport._fields_ = [
            ('AsUSHORT', USHORT),
            ('_Struct_6', wFunctionalitySupport._Struct_6),
        ]
        _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_USB_DESCRIPTOR.wFunctionalitySupport = wFunctionalitySupport

        _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_USB_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bDevCapabilityType', UCHAR),
            ('bReserved', UCHAR),
            ('bmAttributes', _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_USB_DESCRIPTOR.bmAttributes),
            ('wFunctionalitySupport', _USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_USB_DESCRIPTOR.wFunctionalitySupport),
            ('wReserved', USHORT),
            ('bmSublinkSpeedAttr', USB_DEVICE_CAPABILITY_SUPERSPEEDPLUS_SPEED * 1),
        ]

        # USB 3.0: 9.6.2.3 Container ID, Table 9 - 14. Container ID Descriptor
        _USB_DEVICE_CAPABILITY_CONTAINER_ID_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bDevCapabilityType', UCHAR),
            ('bReserved', UCHAR),
            ('ContainerID', UCHAR * 16),
        ]

        # USB Device Capability Platform Descriptor
        _USB_DEVICE_CAPABILITY_PLATFORM_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bDevCapabilityType', UCHAR),
            ('bReserved', UCHAR),
            ('PlatformCapabilityUuid', GUID),
            ('CapabililityData', UCHAR * 1),
        ]

        # USB Billboard 1.0: Section 3.1.5.2, Table 3 - 6. Billboard
        # Capability Descriptor
        class VconnPower(ctypes.Structure):
            pass


        class _Struct_6(ctypes.Structure):
            pass


        _Struct_6._fields_ = [
            ('VConnPowerNeededForFullFunctionality', USHORT, 3),
            ('Reserved', USHORT, 12),
            ('NoVconnPowerRequired', USHORT, 1),
        ]
        VconnPower._Struct_6 = _Struct_6

        VconnPower._anonymous_ = (
            '_Struct_6',
        )
        VconnPower._fields_ = [
            ('AsUSHORT', USHORT),
            ('_Struct_6', VconnPower._Struct_6),
        ]
        _USB_DEVICE_CAPABILITY_BILLBOARD_DESCRIPTOR.VconnPower = VconnPower


        class AlternateMode(ctypes.Structure):
            pass


        AlternateMode.__fields__ = [
            ('wSVID', USHORT),
            ('bAlternateMode', UCHAR),
            ('iAlternateModeSetting', UCHAR)
        ]

        _USB_DEVICE_CAPABILITY_BILLBOARD_DESCRIPTOR.AlternateMode = AlternateMode
        _USB_DEVICE_CAPABILITY_BILLBOARD_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bDevCapabilityType', UCHAR),
            ('iAddtionalInfoURL', UCHAR),
            ('bNumberOfAlternateModes', UCHAR),
            ('bPreferredAlternateMode', UCHAR),
            ('VconnPower', _USB_DEVICE_CAPABILITY_BILLBOARD_DESCRIPTOR.VconnPower),
            ('bmConfigured', UCHAR * 32),
            ('bReserved', ULONG),
            ('AlternateMode', _USB_DEVICE_CAPABILITY_BILLBOARD_DESCRIPTOR.AlternateMode * 1),
        ]

        # {D8DD60DF - 4589 - 4CC7 - 9CD2 - 659D9E648A9F}
        GUID_USB_MSOS20_PLATFORM_CAPABILITY_ID = DEFINE_GUID(
            0xD8DD60DF,
            0x4589,
            0x4CC7,
            0x9C,
            0xD2,
            0x65,
            0x9D,
            0x9E,
            0x64,
            0x8A,
            0x9F
        )

        # USB 3.0: 9.6.2 Binary Device Object Store, Table 9 - 10. Device
        # Capability Descriptor
        _USB_DEVICE_CAPABILITY_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bDevCapabilityType', UCHAR),
        ]

        # USB 1.1: 9.6.2 Configuration, Table 9 - 8. Standard Configuration
        # Descriptor
        # USB 2.0: 9.6.3 Configuration, Table 9 - 10. Standard Configuration
        # Descriptor
        # USB 3.0: 9.6.3 Configuration, Table 9 - 15. Standard Configuration
        # Descriptor
        _USB_CONFIGURATION_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('wTotalLength', USHORT),
            ('bNumInterfaces', UCHAR),
            ('bConfigurationValue', UCHAR),
            ('iConfiguration', UCHAR),
            ('bmAttributes', UCHAR),
            ('MaxPower', UCHAR),
        ]

        # Configuration Descriptor bmAttributes bit definitions
        USB_CONFIG_POWERED_MASK = 0xC0
        USB_CONFIG_BUS_POWERED = 0x80
        USB_CONFIG_SELF_POWERED = 0x40
        USB_CONFIG_REMOTE_WAKEUP = 0x20
        USB_CONFIG_RESERVED = 0x1F

        # USB 2.0 ECN: USB ECN : Interface Association Descriptor, 9.X.Y
        # Interface Association,
        # Table 9 - Z. Standard Interface Association Descriptor
        # USB 3.0: 9.6.4 Interface Association, Table 9 - 16. Standard
        # Interface Association Descriptor
        _USB_INTERFACE_ASSOCIATION_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bFirstInterface', UCHAR),
            ('bInterfaceCount', UCHAR),
            ('bFunctionClass', UCHAR),
            ('bFunctionSubClass', UCHAR),
            ('bFunctionProtocol', UCHAR),
            ('iFunction', UCHAR),
        ]

        # USB 1.1: 9.6.3 Interface, Table 9 - 9. Standard Interface Descriptor
        # USB 2.0: 9.6.5 Interface, Table 9 - 12. Standard Interface Descriptor
        # USB 3.0: 9.6.5 Interface, Table 9 - 17. Standard Interface Descriptor
        _USB_INTERFACE_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bInterfaceNumber', UCHAR),
            ('bAlternateSetting', UCHAR),
            ('bNumEndpoints', UCHAR),
            ('bInterfaceClass', UCHAR),
            ('bInterfaceSubClass', UCHAR),
            ('bInterfaceProtocol', UCHAR),
            ('iInterface', UCHAR),
        ]

        # USB 1.1: 9.6.4 Endpoint, Table 9 - 10. Standard Endpoint Descriptor
        # USB 2.0: 9.6.6 Endpoint, Table 9 - 13. Standard Endpoint Descriptor
        # USB 3.0: 9.6.6 Endpoint, Table 9 - 18. Standard Endpoint Descriptor
        _USB_ENDPOINT_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bEndpointAddress', UCHAR),
            ('bmAttributes', UCHAR),
            ('wMaxPacketSize', USHORT),
            ('bInterval', UCHAR),
        ]

        # USB_ENDPOINT_DESCRIPTOR bEndpointAddress bit 7
        USB_ENDPOINT_DIRECTION_MASK = 0x80


        def USB_ENDPOINT_DIRECTION_OUT(addr):
            return not addr & USB_ENDPOINT_DIRECTION_MASK


        def USB_ENDPOINT_DIRECTION_IN(addr):
            return addr & USB_ENDPOINT_DIRECTION_MASK


        USB_ENDPOINT_ADDRESS_MASK = 0x0F

        # USB_ENDPOINT_DESCRIPTOR bmAttributes bits 0 - 1
        USB_ENDPOINT_TYPE_MASK = 0x03
        USB_ENDPOINT_TYPE_CONTROL = 0x00
        USB_ENDPOINT_TYPE_ISOCHRONOUS = 0x01
        USB_ENDPOINT_TYPE_BULK = 0x02
        USB_ENDPOINT_TYPE_INTERRUPT = 0x03

        # USB_ENDPOINT_DESCRIPTOR bmAttributes bits 7 - 2
        USB_ENDPOINT_TYPE_BULK_RESERVED_MASK = 0xFC
        USB_ENDPOINT_TYPE_CONTROL_RESERVED_MASK = 0xFC
        USB_20_ENDPOINT_TYPE_INTERRUPT_RESERVED_MASK = 0xFC
        USB_30_ENDPOINT_TYPE_INTERRUPT_RESERVED_MASK = 0xCC
        USB_ENDPOINT_TYPE_ISOCHRONOUS_RESERVED_MASK = 0xC0
        USB_30_ENDPOINT_TYPE_INTERRUPT_USAGE_MASK = 0x30
        USB_30_ENDPOINT_TYPE_INTERRUPT_USAGE_PERIODIC = 0x00
        USB_30_ENDPOINT_TYPE_INTERRUPT_USAGE_NOTIFICATION = 0x10
        USB_30_ENDPOINT_TYPE_INTERRUPT_USAGE_RESERVED10 = 0x20
        USB_30_ENDPOINT_TYPE_INTERRUPT_USAGE_RESERVED11 = 0x30


        def USB_30_ENDPOINT_TYPE_INTERRUPT_USAGE(bmAttr):
            return bmAttr & USB_30_ENDPOINT_TYPE_INTERRUPT_USAGE_MASK


        USB_ENDPOINT_TYPE_ISOCHRONOUS_SYNCHRONIZATION_MASK = 0x0C
        USB_ENDPOINT_TYPE_ISOCHRONOUS_SYNCHRONIZATION_NO_SYNCHRONIZATION = 0x00
        USB_ENDPOINT_TYPE_ISOCHRONOUS_SYNCHRONIZATION_ASYNCHRONOUS = 0x04
        USB_ENDPOINT_TYPE_ISOCHRONOUS_SYNCHRONIZATION_ADAPTIVE = 0x08
        USB_ENDPOINT_TYPE_ISOCHRONOUS_SYNCHRONIZATION_SYNCHRONOUS = 0x0C


        def USB_ENDPOINT_TYPE_ISOCHRONOUS_SYNCHRONIZATION(bmAttr):
            return bmAttr & USB_ENDPOINT_TYPE_ISOCHRONOUS_SYNCHRONIZATION_MASK


        USB_ENDPOINT_TYPE_ISOCHRONOUS_USAGE_MASK = 0x30
        USB_ENDPOINT_TYPE_ISOCHRONOUS_USAGE_DATA_ENDOINT = 0x00
        USB_ENDPOINT_TYPE_ISOCHRONOUS_USAGE_FEEDBACK_ENDPOINT = 0x10
        USB_ENDPOINT_TYPE_ISOCHRONOUS_USAGE_IMPLICIT_FEEDBACK_DATA_ENDPOINT = (
            0x20
        )
        USB_ENDPOINT_TYPE_ISOCHRONOUS_USAGE_RESERVED = 0x30


        def USB_ENDPOINT_TYPE_ISOCHRONOUS_USAGE(bmAttr):
            return bmAttr & USB_ENDPOINT_TYPE_ISOCHRONOUS_USAGE_MASK


        # USB_ENDPOINT_DESCRIPTOR wMaxPacketSize
        class _Struct_6(ctypes.Structure):
            pass


        _Struct_6._fields_ = [
            ('MaxPacket', USHORT, 11), # 0 - 10
            ('HSmux', USHORT, 2), # 11 - 12
            ('Reserved', USHORT, 3), # 13 - 15
        ]
        _USB_HIGH_SPEED_MAXPACKET._Struct_6 = _Struct_6

        _USB_HIGH_SPEED_MAXPACKET._anonymous_ = (
            '_Struct_6',
        )
        _USB_HIGH_SPEED_MAXPACKET._fields_ = [
            ('_Struct_6', _USB_HIGH_SPEED_MAXPACKET._Struct_6),
            ('us', USHORT),
        ]
        USB_ENDPOINT_SUPERSPEED_BULK_MAX_PACKET_SIZE = 1024
        USB_ENDPOINT_SUPERSPEED_CONTROL_MAX_PACKET_SIZE = 512
        USB_ENDPOINT_SUPERSPEED_ISO_MAX_PACKET_SIZE = 1024
        USB_ENDPOINT_SUPERSPEED_INTERRUPT_MAX_PACKET_SIZE = 1024

        # USB 1.1: 9.6.5 String, Table 9 - 12. UNICODE String Descriptor
        # USB 2.0: 9.6.7 String, Table 9 - 16. UNICODE String Descriptor
        # USB 3.0: 9.6.8 String, Table 9 - 22. UNICODE String Descriptor
        _USB_STRING_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bString', WCHAR * 1),
        ]
        MAXIMUM_USB_STRING_LENGTH = 255

        # USB 3.0: 9.6.7 SuperSpeed Endpoint Companion, Table 9 - 20.
        # SuperSpeed Endpoint Companion Descriptor
        class bmAttributes(ctypes.Structure):
            pass


        class Bulk(ctypes.Structure):
            pass


        Bulk._fields_ = [
            ('MaxStreams', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
        ]
        bmAttributes.Bulk = Bulk


        class Isochronous(ctypes.Structure):
            pass


        Isochronous._fields_ = [
            ('Mult', UCHAR, 2),
            ('Reserved2', UCHAR, 5),
            ('SspCompanion', UCHAR, 1),
        ]
        bmAttributes.Isochronous = Isochronous

        bmAttributes._fields_ = [
            ('AsUCHAR', UCHAR),
            ('Bulk', bmAttributes.Bulk),
            ('Isochronous', bmAttributes.Isochronous),
        ]
        _USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR.bmAttributes = bmAttributes

        _USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bMaxBurst', UCHAR),
            ('bmAttributes', _USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR.bmAttributes),
            ('wBytesPerInterval', USHORT),
        ]
        USB_SUPERSPEED_ISOCHRONOUS_MAX_MULTIPLIER = 2

        # USB 3.1: 9.6.8 SuperSpeedPlus Isoch Endpoint Companion, Table 9 -
        # 27. SuperSpeedPlus Isoch Endpoint Companion Descriptor
        _USB_SUPERSPEEDPLUS_ISOCH_ENDPOINT_COMPANION_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('wReserved', USHORT),
            ('dwBytesPerInterval', ULONG),
        ]
        USB_SUPERSPEEDPLUS_ISOCHRONOUS_MIN_BYTESPERINTERVAL = 0xC001
        USB_SUPERSPEEDPLUS_ISOCHRONOUS_MAX_BYTESPERINTERVAL = 0xFFFFFF

        # Chapter 11 Hub Specification (USB 1.1, USB 2.0)
        # Chapter 10 Hub, Host Downstream Port, and Device Upstream Port
        # Specification (3.0)
        # USB 1.1: 11.15.2.1 Hub Descriptor, Table 11 - 8. Hub Descriptor
        # USB 2.0: 11.23.2.1 Hub Descriptor, Table 11 - 13. Hub Descriptor
        _USB_HUB_DESCRIPTOR._fields_ = [
            ('bDescriptorLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bNumberOfPorts', UCHAR),
            ('wHubCharacteristics', USHORT),
            ('bPowerOnToPowerGood', UCHAR),
            ('bHubControlCurrent', UCHAR),
            ('bRemoveAndPowerMask', UCHAR * 64),
        ]
        USB_20_HUB_DESCRIPTOR_TYPE = 0x29

        # USB 3.0: 10.13.2.1 Hub Descriptor, Table 10 - 3. SuperSpeed Hub
        # Descriptor
        _USB_30_HUB_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bNumberOfPorts', UCHAR),
            ('wHubCharacteristics', USHORT),
            ('bPowerOnToPowerGood', UCHAR),
            ('bHubControlCurrent', UCHAR),
            ('bHubHdrDecLat', UCHAR),
            ('wHubDelay', USHORT),
            ('DeviceRemovable', USHORT),
        ]
        USB_30_HUB_DESCRIPTOR_TYPE = 0x2A

        # USB 1.1: 11.16.2 Class - specific Requests, Table 11 - 11. Hub Class
        # Request Codes
        USB_REQUEST_GET_STATE = 0x02

        # USB 2.0: 11.24.2 Class - specific Requests, Table 11 - 16. Hub Class
        # Request Codes
        USB_REQUEST_CLEAR_TT_BUFFER = 0x08
        USB_REQUEST_RESET_TT = 0x09
        USB_REQUEST_GET_TT_STATE = 0x0A
        USB_REQUEST_STOP_TT = 0x0B

        # USB 3.0: 10.14.2 Class - specific Requests, Table 10 - 6. Hub Class
        # Request Codes
        USB_REQUEST_SET_HUB_DEPTH = 0x0C
        USB_REQUEST_GET_PORT_ERR_COUNT = 0x0D

        # USB 1.1: 11.16.2 Class - specific Requests, Table 11 - 12. Hub Class
        # Feature Selectors
        # USB 2.0: 11.24.2 Class - specific Requests, Table 11 - 17. Hub Class
        # Feature Selectors
        # USB 3.0: 10.14.2 Class - specific Requests, Table 10 - 7. Hub Class
        # Feature Selectors
        # typedef enum _USB_HUB_FEATURE_SELECTOR {
        #       C_HUB_LOCAL_POWER = 0,
        #       C_HUB_OVER_CURRENT = 1
        # }
        # USB_HUB_FEATURE_SELECTOR, *PUSB_HUB_FEATURE_SELECTOR;
        # typedef enum _USB_PORT_FEATURE_SELECTOR {
        #       PORT_CONNECTION = 0,
        #       PORT_ENABLE = 1,
        #       PORT_SUSPEND = 2,
        #       PORT_OVER_CURRENT = 3,
        #       PORT_RESET = 4,
        #       PORT_LINK_STATE = 5,
        #       PORT_POWER = 8,
        #       PORT_LOW_SPEED = 9,
        #       C_PORT_CONNECTION = 16,
        #       C_PORT_ENABLE = 17,
        #       C_PORT_SUSPEND = 18,
        #       C_PORT_OVER_CURRENT = 19,
        #       C_PORT_RESET = 20,
        #       PORT_TEST = 21,
        #       PORT_INDICATOR = 22,
        #       PORT_U1_TIMEOUT = 23,
        #       PORT_U2_TIMEOUT = 24,
        #       C_PORT_LINK_STATE = 25,
        #       C_PORT_CONFIG_ERROR = 26,
        #       PORT_REMOTE_WAKE_MASK = 27,
        #       BH_PORT_RESET = 28,
        #       C_BH_PORT_RESET = 29,
        #       FORCE_LINKPM_ACCEPT = 30
        # } USB_PORT_FEATURE_SELECTOR, *PUSB_PORT_FEATURE_SELECTOR;
        #
        # USB 1.1: 11.16.2.5 Get Hub Status, Table 11 - 13. Hub Status Field,
        # wHubStatus
        # USB 2.0: 11.24.2.6 Get Hub Status, Table 11 - 19. Hub Status Field,
        # wHubStatus
        # USB 3.0, 10.14.2.4 Get Hub Status, Table 10 - 8. Hub Status Field,
        # wHubStatus
        class _Struct_7(ctypes.Structure):
            pass


        _Struct_7._fields_ = [
            ('LocalPowerLost', USHORT, 1),
            ('OverCurrent', USHORT, 1),
            ('Reserved', USHORT, 14),
        ]
        _USB_HUB_STATUS._Struct_7 = _Struct_7

        _USB_HUB_STATUS._anonymous_ = (
            '_Struct_7',
        )
        _USB_HUB_STATUS._fields_ = [
            ('AsUSHORT16', USHORT),
            ('_Struct_7', _USB_HUB_STATUS._Struct_7),
        ]

        # USB 1.1: 11.16.2.5 Get Hub Status, Table 11 - 14. Hub Change Field,
        # wHubChange
        # USB 2.0: 11.24.2.6 Get Hub Status, Table 11 - 20. Hub Change Field,
        # wHubChange
        # USB 3.0, 10.14.2.4 Get Hub Status, Table 10 - 9. Hub Change Field,
        # wHubChange
        class _Struct_8(ctypes.Structure):
            pass


        _Struct_8._fields_ = [
            ('LocalPowerChange', USHORT, 1),
            ('OverCurrentChange', USHORT, 1),
            ('Reserved', USHORT, 14),
        ]
        _USB_HUB_CHANGE._Struct_8 = _Struct_8

        _USB_HUB_CHANGE._anonymous_ = (
            '_Struct_8',
        )
        _USB_HUB_CHANGE._fields_ = [
            ('AsUSHORT16', USHORT),
            ('_Struct_8', _USB_HUB_CHANGE._Struct_8),
        ]


        class _Struct_9(ctypes.Structure):
            pass


        _Struct_9._fields_ = [
            ('HubStatus', USB_HUB_STATUS), # 0 - 15
            ('HubChange', USB_HUB_CHANGE), # 16 - 32
        ]
        _USB_HUB_STATUS_AND_CHANGE._Struct_9 = _Struct_9

        _USB_HUB_STATUS_AND_CHANGE._anonymous_ = (
            '_Struct_9',
        )
        _USB_HUB_STATUS_AND_CHANGE._fields_ = [
            ('AsULONG32', ULONG),
            ('_Struct_9', _USB_HUB_STATUS_AND_CHANGE._Struct_9),
        ]

        # USB 1.1: 11.16.2.6.1 Port Status Bits, Table 11 - 15. Port Status
        # Field, wPortStatus
        # USB 2.0: 11.24.2.7.1 Port Status Bits, Table 11 - 21. Port Status
        # Field, wPortStatus
        class _Struct_10(ctypes.Structure):
            pass


        _Struct_10._fields_ = [
            ('CurrentConnectStatus', USHORT, 1), # 0
            ('PortEnabledDisabled', USHORT, 1), # 1
            ('Suspend', USHORT, 1), # 2
            ('OverCurrent', USHORT, 1), # 3
            ('Reset', USHORT, 1), # 4
            ('L1', USHORT, 1), # 5
            ('Reserved0', USHORT, 2), # 6 - 7
            ('PortPower', USHORT, 1), # 8
            ('LowSpeedDeviceAttached', USHORT, 1), # 9
            ('HighSpeedDeviceAttached', USHORT, 1), # 10 (USB 1.1 Reserved)
            ('PortTestMode', USHORT, 1), # 11 (USB 1.1 Reserved)
            ('PortIndicatorControl', USHORT, 1), # 12 (USB 1.1 Reserved)
            ('Reserved1', USHORT, 3), # 13 - 15
        ]
        _USB_20_PORT_STATUS._Struct_10 = _Struct_10

        _USB_20_PORT_STATUS._anonymous_ = (
            '_Struct_10',
        )
        _USB_20_PORT_STATUS._fields_ = [
            ('AsUSHORT16', USHORT),
            ('_Struct_10', _USB_20_PORT_STATUS._Struct_10),
        ]
        USB_PORT_STATUS_CONNECT = 0x0001
        USB_PORT_STATUS_ENABLE = 0x0002
        USB_PORT_STATUS_SUSPEND = 0x0004
        USB_PORT_STATUS_OVER_CURRENT = 0x0008
        USB_PORT_STATUS_RESET = 0x0010
        USB_PORT_STATUS_POWER = 0x0100
        USB_PORT_STATUS_LOW_SPEED = 0x0200
        USB_PORT_STATUS_HIGH_SPEED = 0x0400

        # USB 1.1: 11.16.2.6.2 Port Status Change Bits, Table 11 - 16. Port
        # Change Field, wPortChange
        # USB 2.0: 11.24.2.7.2 Port Status Change Bits, Table 11 - 22. Port
        # Change Field, wPortChange
        class _Struct_11(ctypes.Structure):
            pass


        _Struct_11._fields_ = [
            ('ConnectStatusChange', USHORT, 1), # 0
            ('PortEnableDisableChange', USHORT, 1), # 1
            ('SuspendChange', USHORT, 1), # 2
            ('OverCurrentIndicatorChange', USHORT, 1), # 3
            ('ResetChange', USHORT, 1), # 4
            ('Reserved2', USHORT, 11), # 5 - 15
        ]
        _USB_20_PORT_CHANGE._Struct_11 = _Struct_11

        _USB_20_PORT_CHANGE._anonymous_ = (
            '_Struct_11',
        )
        _USB_20_PORT_CHANGE._fields_ = [
            ('AsUSHORT16', USHORT),
            ('_Struct_11', _USB_20_PORT_CHANGE._Struct_11),
        ]

        # USB 3.0: 10.14.2.6.1 Port Status Bits, Table 10 - 10. Port Status
        # Field, wPortStatus
        class _Struct_12(ctypes.Structure):
            pass


        _Struct_12._fields_ = [
            ('CurrentConnectStatus', USHORT, 1), # 0
            ('PortEnabledDisabled', USHORT, 1), # 1
            ('Reserved0', USHORT, 1), # 2
            ('OverCurrent', USHORT, 1), # 3
            ('Reset', USHORT, 1), # 4
            ('PortLinkState', USHORT, 4), # 5 - 8
            ('PortPower', USHORT, 1), # 9
            ('NegotiatedDeviceSpeed', USHORT, 3), # 10 - 12
            ('Reserved1', USHORT, 3), # 13 - 15
        ]
        _USB_30_PORT_STATUS._Struct_12 = _Struct_12

        _USB_30_PORT_STATUS._anonymous_ = (
            '_Struct_12',
        )
        _USB_30_PORT_STATUS._fields_ = [
            ('AsUSHORT16', USHORT),
            ('_Struct_12', _USB_30_PORT_STATUS._Struct_12),
        ]
        PORT_LINK_STATE_U0 = 0
        PORT_LINK_STATE_U1 = 1
        PORT_LINK_STATE_U2 = 2
        PORT_LINK_STATE_U3 = 3
        PORT_LINK_STATE_DISABLED = 4
        PORT_LINK_STATE_RX_DETECT = 5
        PORT_LINK_STATE_INACTIVE = 6
        PORT_LINK_STATE_POLLING = 7
        PORT_LINK_STATE_RECOVERY = 8
        PORT_LINK_STATE_HOT_RESET = 9
        PORT_LINK_STATE_COMPLIANCE_MODE = 10
        PORT_LINK_STATE_LOOPBACK = 11
        PORT_LINK_STATE_TEST_MODE = 11

        # USB 3.0: 10.14.2.6.2 Port Status Change Bits, Table 10 - 11. Port
        # Change Field, wPortChange
        class _Struct_13(ctypes.Structure):
            pass


        _Struct_13._fields_ = [
            ('ConnectStatusChange', USHORT, 1), # 0
            ('Reserved2', USHORT, 2), # 1 - 2
            ('OverCurrentIndicatorChange', USHORT, 1), # 3
            ('ResetChange', USHORT, 1), # 4
            ('BHResetChange', USHORT, 1), # 5
            ('PortLinkStateChange', USHORT, 1), # 6
            ('PortConfigErrorChange', USHORT, 1), # 7
            ('Reserved3', USHORT, 8), # 8 - 15
        ]
        _USB_30_PORT_CHANGE._Struct_13 = _Struct_13

        _USB_30_PORT_CHANGE._anonymous_ = (
            '_Struct_13',
        )
        _USB_30_PORT_CHANGE._fields_ = [
            ('AsUSHORT16', USHORT),
            ('_Struct_13', _USB_30_PORT_CHANGE._Struct_13),
        ]
        _USB_PORT_STATUS._fields_ = [
            ('AsUSHORT16', USHORT),
            ('Usb20PortStatus', USB_20_PORT_STATUS),
            ('Usb30PortStatus', USB_30_PORT_STATUS),
        ]
        _USB_PORT_CHANGE._fields_ = [
            ('AsUSHORT16', USHORT),
            ('Usb20PortChange', USB_20_PORT_CHANGE),
            ('Usb30PortChange', USB_30_PORT_CHANGE),
        ]


        class _Struct_14(ctypes.Structure):
            pass


        _Struct_14._fields_ = [
            ('RxSublinkSpeedID', ULONG, 4),
            ('TxSublinkSpeedID', ULONG, 4),
            ('RxLaneCount', ULONG, 4),
            ('TxLaneCount', ULONG, 4),
            ('Reserved', ULONG, 16),
        ]
        _USB_PORT_EXT_STATUS._Struct_14 = _Struct_14

        _USB_PORT_EXT_STATUS._anonymous_ = (
            '_Struct_14',
        )
        _USB_PORT_EXT_STATUS._fields_ = [
            ('AsULONG32', ULONG),
            ('_Struct_14', _USB_PORT_EXT_STATUS._Struct_14),
        ]


        class _Struct_15(ctypes.Structure):
            pass


        _Struct_15._fields_ = [
            ('PortStatus', USB_PORT_STATUS), # 0 - 15
            ('PortChange', USB_PORT_CHANGE), # 16 - 31
        ]
        _USB_PORT_STATUS_AND_CHANGE._Struct_15 = _Struct_15

        _USB_PORT_STATUS_AND_CHANGE._anonymous_ = (
            '_Struct_15',
        )
        _USB_PORT_STATUS_AND_CHANGE._fields_ = [
            ('AsULONG32', ULONG),
            ('_Struct_15', _USB_PORT_STATUS_AND_CHANGE._Struct_15),
        ]


        class _Struct_16(ctypes.Structure):
            pass


        _Struct_16._fields_ = [
            ('PortStatusChange', USB_PORT_STATUS_AND_CHANGE), # 0 - 31
            ('PortExtStatus', USB_PORT_EXT_STATUS), # 32 - 63
        ]
        _USB_PORT_EXT_STATUS_AND_CHANGE._Struct_16 = _Struct_16

        _USB_PORT_EXT_STATUS_AND_CHANGE._anonymous_ = (
            '_Struct_16',
        )
        _USB_PORT_EXT_STATUS_AND_CHANGE._fields_ = [
            ('AsULONG64', ULONG64),
            ('_Struct_16', _USB_PORT_EXT_STATUS_AND_CHANGE._Struct_16),
        ]

        # USB 3.0: 10.14.2.10 Set Port Feature, Table 10 - 14. Downstream Port
        # Remote Wake Mask Encoding
        class _Struct_17(ctypes.Structure):
            pass


        _Struct_17._fields_ = [
            ('ConnectRemoteWakeEnable', UCHAR, 1), # 0
            ('DisconnectRemoteWakeEnable', UCHAR, 1), # 1
            ('OverCurrentRemoteWakeEnable', UCHAR, 1), # 2
            ('Reserved0', UCHAR, 5), # 3 - 7
        ]
        _USB_HUB_30_PORT_REMOTE_WAKE_MASK._Struct_17 = _Struct_17

        _USB_HUB_30_PORT_REMOTE_WAKE_MASK._anonymous_ = (
            '_Struct_17',
        )
        _USB_HUB_30_PORT_REMOTE_WAKE_MASK._fields_ = [
            ('AsUCHAR8', UCHAR),
            ('_Struct_17', _USB_HUB_30_PORT_REMOTE_WAKE_MASK._Struct_17),
        ]

        # USB 3.0: 9.4.9 Set Feature, Table 9 - 7. Suspend Options
        class _Struct_18(ctypes.Structure):
            pass


        _Struct_18._fields_ = [
            ('PowerState', UCHAR, 1), # 0
            ('RemoteWakeEnabled', UCHAR, 1), # 1
            ('Reserved', UCHAR, 6), # 2 - 7
        ]
        _USB_FUNCTION_SUSPEND_OPTIONS._Struct_18 = _Struct_18

        _USB_FUNCTION_SUSPEND_OPTIONS._anonymous_ = (
            '_Struct_18',
        )
        _USB_FUNCTION_SUSPEND_OPTIONS._fields_ = [
            ('AsUCHAR', UCHAR),
            ('_Struct_18', _USB_FUNCTION_SUSPEND_OPTIONS._Struct_18),
        ]

        # USB Interface Power Management Specification definitions.
        # The USB Interface Power Management Specification was never released
        # and these definitions should not be used. They are only included
        # here to preserve compatibility with the previous usb100.h header
        # file.
        USB_FEATURE_INTERFACE_POWER_D0 = 0x0002
        USB_FEATURE_INTERFACE_POWER_D1 = 0x0003
        USB_FEATURE_INTERFACE_POWER_D2 = 0x0004
        USB_FEATURE_INTERFACE_POWER_D3 = 0x0005
        USB_SUPPORT_D0_COMMAND = 0x01
        USB_SUPPORT_D1_COMMAND = 0x02
        USB_SUPPORT_D2_COMMAND = 0x04
        USB_SUPPORT_D3_COMMAND = 0x08
        USB_SUPPORT_D1_WAKEUP = 0x10
        USB_SUPPORT_D2_WAKEUP = 0x20
        _USB_CONFIGURATION_POWER_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('SelfPowerConsumedD0', UCHAR * 3),
            ('bPowerSummaryId', UCHAR),
            ('bBusPowerSavingD1', UCHAR),
            ('bSelfPowerSavingD1', UCHAR),
            ('bBusPowerSavingD2', UCHAR),
            ('bSelfPowerSavingD2', UCHAR),
            ('bBusPowerSavingD3', UCHAR),
            ('bSelfPowerSavingD3', UCHAR),
            ('TransitionTimeFromD1', USHORT),
            ('TransitionTimeFromD2', USHORT),
            ('TransitionTimeFromD3', USHORT),
        ]
        _USB_INTERFACE_POWER_DESCRIPTOR._fields_ = [
            ('bLength', UCHAR),
            ('bDescriptorType', UCHAR),
            ('bmCapabilitiesFlags', UCHAR),
            ('bBusPowerSavingD1', UCHAR),
            ('bSelfPowerSavingD1', UCHAR),
            ('bBusPowerSavingD2', UCHAR),
            ('bSelfPowerSavingD2', UCHAR),
            ('bBusPowerSavingD3', UCHAR),
            ('bSelfPowerSavingD3', UCHAR),
            ('TransitionTimeFromD1', USHORT),
            ('TransitionTimeFromD2', USHORT),
            ('TransitionTimeFromD3', USHORT),
        ]

        if _MSC_VER >= 1200:
            pass
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF
