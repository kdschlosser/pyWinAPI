import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_TIMERAPI_H_ = None
MMNOTIMER = None


class timecaps_tag(ctypes.Structure):
    pass


TIMECAPS = timecaps_tag
PTIMECAPS = POINTER(timecaps_tag)
NPTIMECAPS = POINTER(timecaps_tag)
LPTIMECAPS = POINTER(timecaps_tag)


# *****************************************************************************
# timerapi.h -- ApiSet Contract for api-ms-win-mm-time-l1-1-0
# Copyright (c) Microsoft Corporation. All rights reserved.
# *****************************************************************************

if defined(_MSC_VER):
    pass
# END IF   _MSC_VER

if not defined(_TIMERAPI_H_):
    _TIMERAPI_H_ = VOID
    from pyWinAPI.shared.apiset_h import * # NOQA
    from pyWinAPI.shared.apisetcconv_h import * # NOQA
    from pyWinAPI.um.mmsyscom_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(MMNOTIMER):
            # *****************************************************************
            # Timer support
            # *****************************************************************

            # timer error return values
            TIMERR_NOERROR = 0            # no error
            TIMERR_NOCANDO = TIMERR_BASE + 1            # request not completed
            TIMERR_STRUCT = TIMERR_BASE + 33            # time struct size

            # timer device capabilities data structure
            # minimum period supported
            timecaps_tag._fields_ = [
                ('wPeriodMin', UINT),
                # maximum period supported
                ('wPeriodMax', UINT),
            ]

            # timer function prototypes
            winmm = ctypes.windll.WINMM

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # timeGetSystemTime(
            # _Out_writes_bytes_(cbmmt) LPMMTIME pmmt,
            # _In_ UINT cbmmt
            # );
            timeGetSystemTime = winmm.timeGetSystemTime
            timeGetSystemTime.restype = MMRESULT

            # WINMMAPI
            # DWORD
            # WINAPI
            # timeGetTime(
            # void
            # );
            timeGetTime = winmm.timeGetTime
            timeGetTime.restype = DWORD

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # timeGetDevCaps(
            # _Out_writes_bytes_(cbtc) LPTIMECAPS ptc,
            # _In_ UINT cbtc
            # );
            timeGetDevCaps = winmm.timeGetDevCaps
            timeGetDevCaps.restype = MMRESULT

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # timeBeginPeriod(
            # _In_ UINT uPeriod
            # );
            timeBeginPeriod = winmm.timeBeginPeriod
            timeBeginPeriod.restype = MMRESULT

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # timeEndPeriod(
            # _In_ UINT uPeriod
            # );
            timeEndPeriod = winmm.timeEndPeriod
            timeEndPeriod.restype = MMRESULT
        # END IF  ifndef MMNOTIMER
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if defined(__cplusplus):
        pass
    # END IF
# END IF   _TIMERAPI_H_


