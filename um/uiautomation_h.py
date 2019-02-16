import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *




# -------------------------------------------------------------
# UIAutomation.h
# UIAutomation API Header, brings in all the other UIAutomation headers
# Copyright (c) Microsoft Corporation. All rights reserved.
# -------------------------------------------------------------
from pyWinAPI.shared.winapifamily_h import * # NOQA
if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    from pyWinAPI.um.uiautomationcore_h import * # NOQA
    from pyWinAPI.um.uiautomationclient_h import * # NOQA
    from pyWinAPI.um.uiautomationcoreapi_h import * # NOQA
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)


