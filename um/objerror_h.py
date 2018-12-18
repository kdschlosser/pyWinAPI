import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


# + ---------------------------------------------------------------------------
# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.
# File:  objerror.h
# ----------------------------------------------------------------------------
if _MSC_VER > 1000:
    pass
# END IF


from pyWinAPI.shared.winapifamily_h import * # NOQA
if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    from pyWinAPI.shared.winerror_h import * # NOQA
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)


