from pyWinAPI import *
from pyWinAPI.shared.sdkddkver_h import *


# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: apdevpkey.h Abstract: Defines Plug and Play Device property keys used
# for AutoPlay behavior. Environment: User and Kernel modes. - -
from winapifamily_h import * # NOQA
if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    if NTDDI_VERSION >= NTDDI_WIN8:
        from pyWinAPI.shared.devpropdef_h import * # NOQA

        # Indicate that AutoPlay should not be displayed for this device
        # interface.
        DEVPKEY_DeviceInterface_Autoplay_Silent = DEFINE_DEVPROPKEY(
            0x434DD28F,
            0x9E75,
            0x450A,
            0x9A,
            0xB9,
            0xFF,
            0x61,
            0xE6,
            0x18,
            0xBA,
            0xD0,
            2
        )
    # END IF
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
