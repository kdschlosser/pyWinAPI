import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.guiddef_h import *


class _HID_XFER_PACKET(ctypes.Structure):
    pass


HID_XFER_PACKET = _HID_XFER_PACKET
PHID_XFER_PACKET = POINTER(_HID_XFER_PACKET)


class _HID_INTERFACE_NOTIFY_PNP(ctypes.Structure):
    pass


HID_INTERFACE_NOTIFY_PNP = _HID_INTERFACE_NOTIFY_PNP
PHID_INTERFACE_NOTIFY_PNP = POINTER(_HID_INTERFACE_NOTIFY_PNP)


class _HID_INTERFACE_HIDPARSE(ctypes.Structure):
    pass


HID_INTERFACE_HIDPARSE = _HID_INTERFACE_HIDPARSE
PHID_INTERFACE_HIDPARSE = POINTER(_HID_INTERFACE_HIDPARSE)


class _HID_COLLECTION_INFORMATION(ctypes.Structure):
    pass


HID_COLLECTION_INFORMATION = _HID_COLLECTION_INFORMATION
PHID_COLLECTION_INFORMATION = POINTER(_HID_COLLECTION_INFORMATION)


class _HID_DRIVER_CONFIG(ctypes.Structure):
    pass


HID_DRIVER_CONFIG = _HID_DRIVER_CONFIG
PHID_DRIVER_CONFIG = POINTER(_HID_DRIVER_CONFIG)


# + + Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# hidclass.h Abstract Definitions that are common to clients of the HID class
# driver. Environment: Kernel mode and user mode - -
from pyWinAPI.shared.basetyps_h import * # NOQA
from pyWinAPI.shared.winapifamily_h import * # NOQA
from pyWinAPI.shared.devpropdef_h import * # NOQA


if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
    # Define the HID class guid *OUTSIDE* the ifndef/endif to allow
    # multiple includes with precompiled headers.
    GUID_DEVINTERFACE_HID = DEFINE_GUID(
        0x4D1E55B2,
        0xF16F,
        0x11CF,
        0x88,
        0xCB,
        0x00,
        0x11,
        0x11,
        0x00,
        0x00,
        0x30
    )
    GUID_CLASS_INPUT = GUID_DEVINTERFACE_HID

    # 2c4e2e88 - 25e6 - 4c33 - 882f - 3d82e6073681
    GUID_HID_INTERFACE_NOTIFY = DEFINE_GUID(
        0x2C4E2E88,
        0x25E6,
        0x4C33,
        0x88,
        0x2F,
        0x3D,
        0x82,
        0xE6,
        0x07,
        0x36,
        0x81
    )

    # {F5C315A5 - 69AC - 4bc2 - 9279 - D0B64576F44B}
    GUID_HID_INTERFACE_HIDPARSE = DEFINE_GUID(
        0xF5C315A5,
        0x69AC,
        0x4BC2,
        0x92,
        0x79,
        0xD0,
        0xB6,
        0x45,
        0x76,
        0xF4,
        0x4B
    )

    if defined(DEFINE_DEVPROPKEY):
        # Device interface properties
        # Name:  System.DeviceInterface.Hid.UsagePage - -
        # DEVPKEY_DeviceInterface_HID_UsagePage
        # Type:  Two - Byte Integer - DEVPROP_TYPE_UINT16
        # FormatID: {CBF38310 - 4A17 - 4310 - A1EB - 247F0B67593B}, 2
        # HID Usage Page
        DEVPKEY_DeviceInterface_HID_UsagePage = DEFINE_DEVPROPKEY(
            0xCBF38310,
            0x4A17,
            0x4310,
            0xA1,
            0xEB,
            0x24,
            0x7F,
            0xB,
            0x67,
            0x59,
            0x3B,
            0x2
        )

        # Name:  System.DeviceInterface.Hid.UsageId - -
        # DEVPKEY_DeviceInterface_HID_UsageId
        # Type:  Two - Byte Integer - DEVPROP_TYPE_UINT16
        # FormatID: {CBF38310 - 4A17 - 4310 - A1EB - 247F0B67593B}, 3
        # HID Usage Id
        DEVPKEY_DeviceInterface_HID_UsageId = DEFINE_DEVPROPKEY(
            0xCBF38310,
            0x4A17,
            0x4310,
            0xA1,
            0xEB,
            0x24,
            0x7F,
            0xB,
            0x67,
            0x59,
            0x3B,
            0x3
        )

        # Name:  System.DeviceInterface.Hid.IsReadOnly - -
        # DEVPKEY_DeviceInterface_HID_IsReadOnly
        # Type:  Boolean - DEVPROP_TYPE_BOOLEAN
        # FormatID: {CBF38310 - 4A17 - 4310 - A1EB - 247F0B67593B}, 4
        # Read - only property indicator
        DEVPKEY_DeviceInterface_HID_IsReadOnly = DEFINE_DEVPROPKEY(
            0xCBF38310,
            0x4A17,
            0x4310,
            0xA1,
            0xEB,
            0x24,
            0x7F,
            0xB,
            0x67,
            0x59,
            0x3B,
            0x4
        )

        # Name:  System.DeviceInterface.Hid.VendorId
        # Type:  Two - Byte Integer - DEVPROP_TYPE_UINT16
        # FormatID: {CBF38310 - 4A17 - 4310 - A1EB - 247F0B67593B}, 5
        # VendorId of HID device
        DEVPKEY_DeviceInterface_HID_VendorId = DEFINE_DEVPROPKEY(
            0xCBF38310,
            0x4A17,
            0x4310,
            0xA1,
            0xEB,
            0x24,
            0x7F,
            0xB,
            0x67,
            0x59,
            0x3B,
            0x5
        )

        # Name:  System.DeviceInterface.Hid.ProductId
        # Type:  Two - Byte Integer - DEVPROP_TYPE_UINT16
        # FormatID: {CBF38310 - 4A17 - 4310 - A1EB - 247F0B67593B}, 6
        # ProductId of HID device
        DEVPKEY_DeviceInterface_HID_ProductId = DEFINE_DEVPROPKEY(
            0xCBF38310,
            0x4A17,
            0x4310,
            0xA1,
            0xEB,
            0x24,
            0x7F,
            0xB,
            0x67,
            0x59,
            0x3B,
            0x6
        )

        # Name:  System.DeviceInterface.Hid.VersionNumber
        # Type:  Two - byte integer - DEVPROP_TYPE_UINT16
        # FormatID: {CBF38310 - 4A17 - 4310 - A1EB - 247F0B67593B}, 7
        # Version number of HID device
        DEVPKEY_DeviceInterface_HID_VersionNumber = DEFINE_DEVPROPKEY(
            0xCBF38310,
            0x4A17,
            0x4310,
            0xA1,
            0xEB,
            0x24,
            0x7F,
            0xB,
            0x67,
            0x59,
            0x3B,
            0x7
        )

        # Type:  Boolean - DEVPROP_TYPE_BOOLEAN
        # FormatID: {CBF38310 - 4A17 - 4310 - A1EB - 247F0B67593B}, 8
        # Allow access from background tasks to this HID device
        DEVPKEY_DeviceInterface_HID_BackgroundAccess = DEFINE_DEVPROPKEY(
            0xCBF38310,
            0x4A17,
            0x4310,
            0xA1,
            0xEB,
            0x24,
            0x7F,
            0xB,
            0x67,
            0x59,
            0x3B,
            0x8
        )
    # END IF
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

__HIDCLASS_H__ = None

if not defined(__HIDCLASS_H__):
    __HIDCLASS_H__ = 1

    from pyWinAPI.shared.devioctl_h import *


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if _MSC_VER >= 1200:
            pass
        # END IF

        # HID_REVISION specifies the minimum revision of HIDCLASS.SYS
        # required to support minidrivers compiled with this header file.
        HID_REVISION = 0x00000001

        # Macro for defining HID ioctls
        def HID_CTL_CODE(id):
            return CTL_CODE(FILE_DEVICE_KEYBOARD, id, METHOD_NEITHER, FILE_ANY_ACCESS)


        def HID_BUFFER_CTL_CODE(id):
            return CTL_CODE(FILE_DEVICE_KEYBOARD, id, METHOD_BUFFERED, FILE_ANY_ACCESS)


        def HID_IN_CTL_CODE(id):
            return CTL_CODE(FILE_DEVICE_KEYBOARD, id, METHOD_IN_DIRECT, FILE_ANY_ACCESS)


        def HID_OUT_CTL_CODE(id):
            return CTL_CODE(FILE_DEVICE_KEYBOARD, id, METHOD_OUT_DIRECT, FILE_ANY_ACCESS)

        # IOCTLs supported by the upper edge of the HID class driver
        IOCTL_HID_GET_DRIVER_CONFIG = HID_BUFFER_CTL_CODE(100)
        IOCTL_HID_SET_DRIVER_CONFIG = HID_BUFFER_CTL_CODE(101)
        IOCTL_HID_GET_POLL_FREQUENCY_MSEC = HID_BUFFER_CTL_CODE(102)
        IOCTL_HID_SET_POLL_FREQUENCY_MSEC = HID_BUFFER_CTL_CODE(103)
        IOCTL_GET_NUM_DEVICE_INPUT_BUFFERS = HID_BUFFER_CTL_CODE(104)
        IOCTL_SET_NUM_DEVICE_INPUT_BUFFERS = HID_BUFFER_CTL_CODE(105)
        IOCTL_HID_GET_COLLECTION_INFORMATION = HID_BUFFER_CTL_CODE(106)
        IOCTL_HID_ENABLE_WAKE_ON_SX = HID_BUFFER_CTL_CODE(107)
        IOCTL_HID_SET_S0_IDLE_TIMEOUT = HID_BUFFER_CTL_CODE(108)
        IOCTL_HID_GET_COLLECTION_DESCRIPTOR = HID_BUFFER_CTL_CODE(100)
        IOCTL_HID_FLUSH_QUEUE = HID_BUFFER_CTL_CODE(101)
        IOCTL_HID_SET_FEATURE = HID_BUFFER_CTL_CODE(100)
        IOCTL_HID_SET_OUTPUT_REPORT = HID_BUFFER_CTL_CODE(101)
        IOCTL_HID_GET_FEATURE = HID_BUFFER_CTL_CODE(100)
        IOCTL_GET_PHYSICAL_DESCRIPTOR = HID_BUFFER_CTL_CODE(102)
        IOCTL_HID_GET_HARDWARE_ID = HID_BUFFER_CTL_CODE(103)
        IOCTL_HID_GET_INPUT_REPORT = HID_BUFFER_CTL_CODE(104)
        IOCTL_HID_GET_OUTPUT_REPORT = HID_BUFFER_CTL_CODE(105)
        IOCTL_HID_GET_MANUFACTURER_STRING = HID_BUFFER_CTL_CODE(110)
        IOCTL_HID_GET_PRODUCT_STRING = HID_BUFFER_CTL_CODE(111)
        IOCTL_HID_GET_SERIALNUMBER_STRING = HID_BUFFER_CTL_CODE(112)
        IOCTL_HID_GET_INDEXED_STRING = HID_BUFFER_CTL_CODE(120)
        IOCTL_HID_GET_MS_GENRE_DESCRIPTOR = HID_BUFFER_CTL_CODE(121)
        IOCTL_HID_ENABLE_SECURE_READ = HID_BUFFER_CTL_CODE(130)
        IOCTL_HID_DISABLE_SECURE_READ = HID_BUFFER_CTL_CODE(131)
        IOCTL_HID_DEVICERESET_NOTIFICATION = HID_BUFFER_CTL_CODE(140)

        # This is used to pass write - report and feature - report information
        # from HIDCLASS to a minidriver.
        _HID_XFER_PACKET._fields_ = [
            ('reportBuffer', PUCHAR),
            ('reportBufferLen', ULONG),
            ('reportId', UCHAR),
        ]

        NT_INCLUDED = 0

        if defined(NT_INCLUDED):
            class DeviceObjectState(ENUM):
                DeviceObjectStarted = 1
                DeviceObjectStopped = 2
                DeviceObjectRemoved = 3


            DeviceObjectStarted = DeviceObjectState.DeviceObjectStarted
            DeviceObjectStopped = DeviceObjectState.DeviceObjectStopped
            DeviceObjectRemoved = DeviceObjectState.DeviceObjectRemoved
            # typedef VOID (*PHID_STATUS_CHANGE)(_In_ PVOID Context, _In_ enum DeviceObjectState State);

            PHID_STATUS_CHANGE = CALLBACK(VOID, PVOID, DeviceObjectState)

            import comtypes

            INTERFACE = comtypes.IUnknown

            _HID_INTERFACE_NOTIFY_PNP._fields_ = [
                ('i', INTERFACE),
                ('StatusChangeFn', PHID_STATUS_CHANGE),
                ('CallbackContext', PVOID),
            ]

            if not defined(__cplusplus):
                pass
            else:
                pass
            # END IF

            __HIDPI_H__ = 0
            if defined(__HIDPI_H__):

                # _Must_inspect_result_
                # typedef
                # NTSTATUS
                # (__stdcall *PHIDP_GETCAPS) (
                # _In_  PHIDP_PREPARSED_DATA PreparsedData,
                # _Out_ PHIDP_CAPS Capabilities
                # );

                from pyWinAPI.shared.hidpi_h import *

                PHIDP_GETCAPS = CALLBACK(NTSTATUS, PHIDP_PREPARSED_DATA, PHIDP_CAPS)


                _HID_INTERFACE_HIDPARSE._fields_ = [
                    ('i', INTERFACE),
                    ('HidpGetCaps', PHIDP_GETCAPS),
                ]
                if not defined(__cplusplus):
                    pass
                else:
                    pass
                # END IF
            # END IF   __HIDPI_H__
        # END IF   NT_INCLUDED

        # Structure passed by IOCTL_HID_GET_COLLECTION_INFORMATION
        _HID_COLLECTION_INFORMATION._fields_ = [
            ('DescriptorSize', ULONG), # IOCTL_HID_GET_COLLECTION_DESCRIPTOR.
            ('Polled', BOOLEAN), # Polled is TRUE if this collection is a polled collection.
            ('Reserved1', UCHAR * 1), # Reserved1 must be set to zero.
            ('VendorID', USHORT), # Vendor ids of this hid device
            ('ProductID', USHORT),
            ('VersionNumber', USHORT),
        ]

        # Structure passed by IOCTL_HID_GET_DRIVER_CONFIG and
        # IOCTL_HID_SET_DRIVER_CONFIG
        _HID_DRIVER_CONFIG._fields_ = [
            ('Size', ULONG), # Size must be set to the size of this structure.

            # Size of the input report queue (in reports). This value can be
            # set.
            ('RingBufferSize', ULONG),
        ]
        if _MSC_VER >= 1200:
            pass
        else:
            pass
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF   __HIDCLASS_H__
