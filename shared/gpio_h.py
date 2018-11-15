from pyWinAPI import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.devioctl_h import *


# + + Copyright (c) Microsoft Corporation. All rights reserved. THIS CODE AND
# INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER
# EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. Module Name: gpio.h
# Abstract: Header file that defines structures, prototypes and definitions
# required by consumers of GPIO services. Environment: Kernel mode - -
__GPIO_W__ = None

if not defined(__GPIO_W__):
    __GPIO_W__ = 1
    from winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if NTDDI_VERSION >= NTDDI_WIN8:
            if defined(__cplusplus):
                pass
            # END IF

            # Define IOCTL to read from a set of GPIO pins (input).
            IOCTL_GPIO_READ_PINS = CTL_CODE(
                FILE_DEVICE_GPIO,
                0x0,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )

            # Define IOCTL to write to a set of GPIO pins (output).
            IOCTL_GPIO_WRITE_PINS = CTL_CODE(
                FILE_DEVICE_GPIO,
                0x1,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )

            # Define IOCTL for handling GPIO controller - specific
            # functionality.
            IOCTL_GPIO_CONTROLLER_SPECIFIC_FUNCTION = CTL_CODE(
                FILE_DEVICE_GPIO,
                0x2,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )

            if NTDDI_VERSION >= NTDDI_WIN10_RS1:
                # Define IOCTL to commit function config pin settings to HW.
                IOCTL_GPIO_COMMIT_FUNCTION_CONFIG_PINS = CTL_CODE(
                    FILE_DEVICE_GPIO,
                    0x4,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
            # END IF
            if defined(__cplusplus):
                pass
            # END IF        # END IF   (NTDDI_VERSION >= NTDDI_WIN8)    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)# END IF   __GPIO_W__
