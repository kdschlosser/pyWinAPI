from pyWinAPI import *

# + + Copyright 2004(c) Microsoft Corporation. All rights reserved. Module
# Name: USBDI.H Abstract: Obsolete header. Use usb.h. Environment: Kernel &
# user mode Revision History: 09 - 29 - 95 : created 02 - 01 - 04 : updated to
# use usb.h - -

__USBDI_H__ = None

if not defined(__USBDI_H__):
    __USBDI_H__ = 1
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        from pyWinAPI.shared.usb_h import * # NOQA
        from pyWinAPI.shared.usbioctl_h import * # NOQA

        # The following are deprecated definitions. These should not be used
        USBD_STATUS_CANCELLING = 0x00020000
        USBD_STATUS_CANCELING = 0x00020000
        USBD_STATUS_NO_MEMORY = 0x80000100
        USBD_STATUS_ERROR = 0x80000000
        USBD_STATUS_REQUEST_FAILED = 0x80000500
        USBD_STATUS_HALTED = 0xC0000000


        def USBD_HALTED(Status):
            return Status >> 30 == 3


        def USBD_STATUS(Status):
            return Status & 0x0FFFFFFF


        URB_FUNCTION_RESERVED0 = 0x0016
        URB_FUNCTION_RESERVED = 0x001D
        URB_FUNCTION_LAST = 0x0029
        USBD_PF_DOUBLE_BUFFER = 0x00000002

        if defined(USBD_PF_VALID_MASK):
            pass

        # END IF
        USBD_PF_VALID_MASK = (
            USBD_PF_CHANGE_MAX_PACKET |
            USBD_PF_DOUBLE_BUFFER |
            USBD_PF_ENABLE_RT_THREAD_ACCESS |
            USBD_PF_MAP_ADD_TRANSFERS
        )
        USBD_TRANSFER_DIRECTION_BIT = 0
        USBD_SHORT_TRANSFER_OK_BIT = 1
        USBD_START_ISO_TRANSFER_ASAP_BIT = 2

        if defined(USBD_TRANSFER_DIRECTION):
            pass
        # END IF

        def USBD_TRANSFER_DIRECTION(x):
            return x & USBD_TRANSFER_DIRECTION_IN

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF  __USBDI_H__
