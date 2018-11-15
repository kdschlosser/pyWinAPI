from pyWinAPI import *

# Copyright (C) Microsoft. All rights reserved.
__USB200_H__ = None
if not defined(__USB200_H__):
    __USB200_H__ = 1

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        from pyWinAPI.shared.usbspec_h import * # NOQA
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF   __USB200_H__
