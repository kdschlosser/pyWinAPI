import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_MANAGED = None
MANAGED_ENUMS = None
USING_EHRECVR_NAMESPACE = None


# ----------------------------------------------------------------------------
# File: exposeenums2managed.h
# Desc: macros to allow the same enum to be exposed to native and managed
# USAGE:
# in your whatever.h file that defines the enums use ENUM or
# FLAGS(for enums defining bitmasks/flags)
# at the top of the file include this .h
# at the bottom of the file include
# unexposeenums2managed.h(resets the macro state)
# in a native client .idl/.h/.cpp file as normal just
# include < whatever.h >
# this will include the file normally
# in a mgd cpp file
# include < whatever.h >
# once normally, this will make the enums available to native
# Copyright (c) 2003-2004, Microsoft Corporation. All rights reserved.
# ----------------------------------------------------------------------------
# not not not do not pragma once or macro guard this file.
# it gets used multiple times by the same compilation units
from pyWinAPI.shared.winapifamily_h import * # NOQA


if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    if defined(MANAGED_ENUMS):
        if not defined(_MANAGED):
            pass
        # END IF


        def ENUMG(g):
            return ENUM(g)

        ENUM16 = ENUM
        FLAGS = ENUM
        FLAGS16 = ENUM16

        def TAG(x):
            return x


        def RATLEVEL(x):
            return x

        def RATATTR(x):
            return x

        if defined(USING_EHRECVR_NAMESPACE):
            EHRECVR_MGD_OUTER_NAMESPACE = VOID

            def EHRECVR_MGD_NAMESPACE(x):
                return EHRECVR_MGD_OUTER_NAMESPACE(x)

            def ANALOG_VIDEO_STANDARD_NAMESPACE(x):
                return EHRECVR_MGD_NAMESPACEAnalogVideoStandard(x)
        else:
            def EHRECVR_MGD_NAMESPACE(x):
                return x

            def ANALOG_VIDEO_STANDARD_NAMESPACE(x):
                return x
        # END IF

    else:
        if defined(__midl):
            V1_ENUM = [v1_enum]

            def V1_ENUMG(g):
                return [uuid(g), v1_enum]
        else:
            V1_ENUM = VOID
            V1_ENUMG = VOID

        # END IF

        def RATLEVEL(x):
            return x

        def RATATTR(x):
            return x

        def ENUMG(g):
            return V1_ENUMG(g)


        ENUM16 = ENUM
        FLAGS = ENUM
        FLAGS16 = ENUM16

        def TAG(x):
            return x

        def EHRECVR_MGD_NAMESPACE(x):
            return x

        def ANALOG_VIDEO_STANDARD_NAMESPACE(x):
            return x
    # END IF

    # end of file - exposeenums2managed.h
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

