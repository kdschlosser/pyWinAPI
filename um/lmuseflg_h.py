import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMUSEFLG_ = None

# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmuseflg.h
# Abstract: This file contains deletion force levels for deleting a
# connection. Environment: User Mode - Win32 Notes: This file has no
# dependencies. It is included by lmwksta.h and lmuse.h. Revision History: --
if not defined(_LMUSEFLG_):
    _LMUSEFLG_ = VOID

    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # Definition for NetWkstaTransportDel and NetUseDel deletion force
        # levels and flags. The lower 16 bits
        # define the force levels and the upper 16 bits are the use flags
        # defined in lmuse.h
        USE_NOFORCE = 0
        USE_FORCE = 1
        USE_LOTS_OF_FORCE = 2


        def FORCE_LEVEL(LEVELFLAGS):
            return LEVELFLAGS & 0xFFFF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF   _LMUSEFLG_


