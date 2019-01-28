import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

_INC_MMSYSTEM = None
MMNOMCI = None
MMNOTIMER = None
NEWTRANSPARENT = None
SC_SCREENSAVE = None


# /* == == == == == == == == == == == == == == == == == == == == == == == ==
# == == == == == == == == == == == == == mmsystem.h -- Include file for
# Multimedia API's Version 4.00 Copyright (C) 1992-1998 Microsoft Corporation.
# All Rights Reserved.
# --------------------------------------------------------------------------
# Define: Prevent inclusion of: --------------
# -------------------------------------------------------- MMNODRV Installable
# driver support MMNOSOUND Sound support MMNOWAVE Waveform support MMNOMIDI
# MIDI support MMNOAUX Auxiliary audio support MMNOMIXER Mixer support
# MMNOTIMER Timer support MMNOJOY Joystick support MMNOMCI MCI support
# MMNOMMIO Multimedia file I/O support MMNOMMSYSTEM General MMSYSTEM functions
# == == == == == == == == == == == == == == == == == == == == == == == == ==
# == == == == == == == == == == == ==
if not defined(_INC_MMSYSTEM):
    _INC_MMSYSTEM = 1    # defined if mmsystem.h has been included
    from pyWinAPI.um.mmsyscom_h import * # NOQA
    if defined(_WIN32):
        from pyWinAPI.shared.pshpack1_h import * # NOQA
        if not defined(RC_INVOKED):
            pass
        # END IF
    else:
        pass
    # END IF

    if defined(__cplusplus):
        pass
    # END IF  __cplusplus

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # *********************************************************************
        # Multimedia Extensions Window Messages
        # *********************************************************************

        if not defined(MMNOMCI):
            # MMNOMCI  MCI support
            from pyWinAPI.um.mciapi_h import * # NOQA
        # END IF   #ifndef MMNOMCI

        # MMNODRV - Installable driver support
        from pyWinAPI.um.mmiscapi_h import * # NOQA
        from pyWinAPI.um.mmiscapi2_h import * # NOQA

        # MMNOSOUND Sound support
        from pyWinAPI.um.playsoundapi_h import * # NOQA
        from pyWinAPI.um.mmeapi_h import * # NOQA
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # *********************************************************************
        # Timer support
        # *********************************************************************

        if not defined(MMNOTIMER):
            from pyWinAPI.um.timeapi_h import * # NOQA
            # timer data types        
        # END IF  ifndef MMNOTIMER
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Joystickapi API Set contract
        from pyWinAPI.um.joystickapi_h import * # NOQA

        # *********************************************************************
        # DISPLAY Driver extensions
        # *********************************************************************

        if not defined(NEWTRANSPARENT):
            NEWTRANSPARENT = 3            # use with SetBkMode()
            QUERYROPSUPPORT = 40            # use to determine ROP support
        # END IF  ifndef NEWTRANSPARENT

        # *********************************************************************
        # DIB Driver extensions
        # *********************************************************************
        SELECTDIB = 41        # DIB.DRV select dib escape


        def DIBINDEX(n):
            return MAKELONG(n,0x10FF)

        # *********************************************************************
        # ScreenSaver support
        # The current application will receive a syscommand of SC_SCREENSAVE
        # just before the screen saver is invoked. If the app wishes to
        # prevent a screen save, return non-zero value, otherwise call
        # DefWindowProc().
        # *********************************************************************

        if not defined(SC_SCREENSAVE):
            SC_SCREENSAVE = 0xF140
        # END IF  ifndef SC_SCREENSAVE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if defined(__cplusplus):
        pass
    # END IF  __cplusplus
    if defined(_WIN32):
        from pyWinAPI.shared.poppack_h import * # NOQA
        if not defined(RC_INVOKED):
            pass
        # END IF
    else:
        pass
    # END IF
# END IF  _INC_MMSYSTEM


