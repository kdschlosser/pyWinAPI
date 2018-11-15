
# + + Copyright (c) 1998 - 2000 Microsoft Corporation Module Name: ioctl.h
# Abstract: Environment: Kernel & user mode Revision History: - -

from pyWinAPI.shared.winapifamily_h import * # NOQA
from pyWinAPI.shared.devioctl_h import * # NOQA
if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    # {28D78FAD - 5A12 - 11d1 - AE5B - 0000F803A8C2}
    GUID_DEVINTERFACE_USBPRINT = DEFINE_GUID(
        0x28D78FAD,
        0x5A12,
        0x11D1,
        0xAE,
        0x5B,
        0x0,
        0x0,
        0xF8,
        0x3,
        0xA8,
        0xC2
    )
    USBPRINT_IOCTL_INDEX = 0x0000
    IOCTL_USBPRINT_GET_LPT_STATUS = CTL_CODE(
        FILE_DEVICE_UNKNOWN,
        USBPRINT_IOCTL_INDEX + 12,
        METHOD_BUFFERED,
        FILE_ANY_ACCESS,
    )
    IOCTL_USBPRINT_GET_1284_ID = CTL_CODE(
        FILE_DEVICE_UNKNOWN,
        USBPRINT_IOCTL_INDEX + 13,
        METHOD_BUFFERED,
        FILE_ANY_ACCESS,
    )
    IOCTL_USBPRINT_VENDOR_SET_COMMAND = CTL_CODE(
        FILE_DEVICE_UNKNOWN,
        USBPRINT_IOCTL_INDEX + 14,
        METHOD_BUFFERED,
        FILE_ANY_ACCESS,
    )
    IOCTL_USBPRINT_VENDOR_GET_COMMAND = CTL_CODE(
        FILE_DEVICE_UNKNOWN,
        USBPRINT_IOCTL_INDEX + 15,
        METHOD_BUFFERED,
        FILE_ANY_ACCESS,
    )
    IOCTL_USBPRINT_SOFT_RESET = CTL_CODE(
        FILE_DEVICE_UNKNOWN,
        USBPRINT_IOCTL_INDEX + 16,
        METHOD_BUFFERED,
        FILE_ANY_ACCESS,
    )
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
