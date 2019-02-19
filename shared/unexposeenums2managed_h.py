import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


# ----------------------------------------------------------------------------
# File: expose.h
# Desc: macros to allow the same enum to be exposed to native and managed.
# USAGE:
# see comments at top of exposeenums2managed.h
# Copyright (c) 2003-2004, Microsoft Corporation. All rights reserved.
# ----------------------------------------------------------------------------
# not not not do not pragma once or macro guard this file.
# it gets used multiple times by the same compilation units
from pyWinAPI.shared.winapifamily_h import * # NOQA
if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    # undef V1_ENUM
    # undef V1_ENUMG
    # undef ENUM
    # undef ENUMG
    # undef ENUM16
    # undef FLAGS
    # undef FLAGS16
    # undef TAG
    # undef EHRECVR_MGD_NAMESPACE
    # undef ANALOG_VIDEO_STANDARD_NAMESPACE
    # undef RATLEVEL
    # undef RATATTR
    pass
    # end of file - expose.h
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
