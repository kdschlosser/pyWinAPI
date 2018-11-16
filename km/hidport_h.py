import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *


class _HID_MINIDRIVER_REGISTRATION(ctypes.Structure):
    pass


HID_MINIDRIVER_REGISTRATION = _HID_MINIDRIVER_REGISTRATION
PHID_MINIDRIVER_REGISTRATION = POINTER(_HID_MINIDRIVER_REGISTRATION)


class _HID_DEVICE_EXTENSION(ctypes.Structure):
    pass


HID_DEVICE_EXTENSION = _HID_DEVICE_EXTENSION
PHID_DEVICE_EXTENSION = POINTER(_HID_DEVICE_EXTENSION)


class _HID_DEVICE_ATTRIBUTES(ctypes.Structure):
    pass


HID_DEVICE_ATTRIBUTES = _HID_DEVICE_ATTRIBUTES
PHID_DEVICE_ATTRIBUTES = POINTER(_HID_DEVICE_ATTRIBUTES)


class _HID_DESCRIPTOR(ctypes.Structure):
    pass


HID_DESCRIPTOR = _HID_DESCRIPTOR
PHID_DESCRIPTOR = POINTER(_HID_DESCRIPTOR)


class _HID_SUBMIT_IDLE_NOTIFICATION_CALLBACK_INFO(ctypes.Structure):
    pass


HID_SUBMIT_IDLE_NOTIFICATION_CALLBACK_INFO = _HID_SUBMIT_IDLE_NOTIFICATION_CALLBACK_INFO
PHID_SUBMIT_IDLE_NOTIFICATION_CALLBACK_INFO = POINTER(_HID_SUBMIT_IDLE_NOTIFICATION_CALLBACK_INFO)


# /* + + Copyright (c) 1996 Microsoft Corporation Module Name: hidport.h
# Abstract Definitions that are common to all HID minidrivers. Environment:
# Kernel mode only - -

__HIDPORT_H__ = None
if not defined(__HIDPORT_H__):
    __HIDPORT_H__ = 1
    from pyWinAPI.shared.hidclass_h import * # NOQA
    from pyWinAPI.missing_structures_h import * # NOQA

    # HID_MINIDRIVER_REGISTRATION is a struct filled in by the HID minidriver
    # and passed to HIDCLASS via HidRegisterMinidriver()
    _HID_MINIDRIVER_REGISTRATION._fields_ = [
        # Revision must be set to HID_REVISION by the minidriver
        ('Revision', ULONG),
        # received as a DriverEntry() parameter.
        ('DriverObject', PDRIVER_OBJECT),
        # received as a DriverEntry() parameter.
        ('RegistryPath', PUNICODE_STRING),
        # extension.
        ('DeviceExtensionSize', ULONG),
        # Either all or none of the devices driven by a given minidriver are
        # polled.
        ('DevicesArePolled', BOOLEAN),
        ('Reserved', UCHAR * 3),
    ]

    # HID_DEVICE_EXTENSION is the public part of the device extension of a HID
    # functional device object.
    _HID_DEVICE_EXTENSION._fields_ = [
        # PhysicalDeviceObject... normally IRPs are not passed to this.
        ('PhysicalDeviceObject', PDEVICE_OBJECT),
        # objects on the way down.
        ('NextDeviceObject', PDEVICE_OBJECT),
        # MiniDeviceExtension = HidDeviceExtension - >MiniDeviceExtension;
        ('MiniDeviceExtension', PVOID),
    ]
    _HID_DEVICE_ATTRIBUTES._fields_ = [
        ('Size', ULONG),
        # Vendor ids of this hid device
        ('VendorID', USHORT),
        ('ProductID', USHORT),
        ('VersionNumber', USHORT),
        ('Reserved', USHORT * 11),
    ]

    class _HID_DESCRIPTOR_DESC_LIST(ctypes.Structure):
        pass


    _HID_DESCRIPTOR_DESC_LIST._fields_ = [
        ('bReportType', UCHAR),
        ('wReportLength', USHORT),
    ]
    DescriptorList = _HID_DESCRIPTOR_DESC_LIST

    _HID_DESCRIPTOR.DescriptorList  = DescriptorList
    _HID_DESCRIPTOR._fields_ = [
        ('bLength', UCHAR),
        ('bDescriptorType', UCHAR),
        ('bcdHID', USHORT),
        ('bCountry', UCHAR),
        ('bNumDescriptors', UCHAR),
        # An array of one OR MORE descriptors.
        ('DescriptorList ', _HID_DESCRIPTOR.DescriptorList  * 1),
    ]
    # Function prototypes for the HID services exported by the hid class driver
    # follow.
    hidclass = ctypes.windll.HIDCLASS
    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # _Must_inspect_result_
    # NTSTATUS
    # HidRegisterMinidriver(
    # _In_ PHID_MINIDRIVER_REGISTRATION  MinidriverRegistration
    # );
    HidRegisterMinidriver = hidclass.HidRegisterMinidriver
    HidRegisterMinidriver.restype = NTSTATUS

    if NTDDI_VERSION >= NTDDI_WINXPSP1:
        # NTSTATUS
        # HidNotifyPresence(
        # _In_ PDEVICE_OBJECT DeviceObject,
        # _In_ BOOLEAN IsPresent
        # );
        HidNotifyPresence = hidclass.HidNotifyPresence
        HidNotifyPresence.restype = NTSTATUS

    # END IF
    # The HID idle callback struct and callback function are used in
    # conjunction with IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST sent down
    # by HIDCLASS during runtime idling

    HID_SEND_IDLE_CALLBACK = CALLBACK(VOID, PVOID)

    _HID_SUBMIT_IDLE_NOTIFICATION_CALLBACK_INFO._fields_ = [
        ('IdleCallback', HID_SEND_IDLE_CALLBACK),
        ('IdleContext', PVOID),
    ]

    # Internal IOCTLs for the class/mini driver interface.
    IOCTL_HID_GET_DEVICE_DESCRIPTOR = HID_CTL_CODE(0)
    IOCTL_HID_GET_REPORT_DESCRIPTOR = HID_CTL_CODE(1)
    IOCTL_HID_READ_REPORT = HID_CTL_CODE(2)
    IOCTL_HID_WRITE_REPORT = HID_CTL_CODE(3)
    IOCTL_HID_GET_STRING = HID_CTL_CODE(4)
    IOCTL_HID_ACTIVATE_DEVICE = HID_CTL_CODE(7)
    IOCTL_HID_DEACTIVATE_DEVICE = HID_CTL_CODE(8)
    IOCTL_HID_GET_DEVICE_ATTRIBUTES = HID_CTL_CODE(9)
    IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST = HID_CTL_CODE(10)

    # Internal IOCTLs supported by UMDF HID minidriver.
    IOCTL_UMDF_HID_SET_FEATURE = HID_CTL_CODE(20)
    IOCTL_UMDF_HID_GET_FEATURE = HID_CTL_CODE(21)
    IOCTL_UMDF_HID_SET_OUTPUT_REPORT = HID_CTL_CODE(22)
    IOCTL_UMDF_HID_GET_INPUT_REPORT = HID_CTL_CODE(23)
    IOCTL_UMDF_GET_PHYSICAL_DESCRIPTOR = HID_CTL_CODE(24)

    # Codes for HID - specific descriptor types, from HID USB spec.
    HID_HID_DESCRIPTOR_TYPE = 0x21
    HID_REPORT_DESCRIPTOR_TYPE = 0x22
    HID_PHYSICAL_DESCRIPTOR_TYPE = 0x23
    # These are string IDs for use with IOCTL_HID_GET_STRING
    # They match the string field offsets in Chapter 9 of the USB Spec.
    HID_STRING_ID_IMANUFACTURER = 14
    HID_STRING_ID_IPRODUCT = 15
    HID_STRING_ID_ISERIALNUMBER = 16
# END IF   __HIDPORT_H__
