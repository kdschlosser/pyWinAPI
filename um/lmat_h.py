import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMAT_ = None

class _AT_INFO(ctypes.Structure):
    pass


AT_INFO = _AT_INFO
PAT_INFO = POINTER(_AT_INFO)
LPAT_INFO = POINTER(_AT_INFO)


class _AT_ENUM(ctypes.Structure):
    pass


AT_ENUM = _AT_ENUM
PAT_ENUM = POINTER(_AT_ENUM)
LPAT_ENUM = POINTER(_AT_ENUM)


# /* + + BUILD Version: 0006 // Increment this if a change has global effects
# Copyright (c) 1992-1999 Microsoft Corporation Module Name: lmat.h Abstract:
# This file contains structures, function prototypes, and definitions for the
# schedule service API-s. Environment: User Mode - Win32 Portable to any flat,
# 32-bit environment. (Uses Win32 typedefs.) Requires ANSI C extensions:
# slash-slash comments, LONG external names. Notes: You must include NETCONS.H
# before this file, since this file depends on values defined in NETCONS.H.
# Revision History: --
if not defined(_LMAT_):
    _LMAT_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.shared.lmcons_h import *  # NOQA


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if defined(__cplusplus):
            pass
        # END IF

        # The following bits are used with Flags field in structures below.
        # Do we exec programs for this job periodically (/EVERY switch)
        # or one time (/NEXT switch).
        JOB_RUN_PERIODICALLY = 0x01        # set if EVERY

        # Was there an error last time we tried to exec a program on behalf of
        # this job.
        # This flag is meaningfull on output onlynot
        JOB_EXEC_ERROR = 0x02        # set if error

        # Will this job run today or tomorrow.
        # This flag is meaningfull on output onlynot
        JOB_RUNS_TODAY = 0x04        # set if today

        # Add current day of the month to DaysOfMonth input.
        # This flag is meaningfull on input onlynot
        JOB_ADD_CURRENT_DATE = 0x08        # set if to add current date

        # Will this job be run interactively or not. Windows NT 3.1 do not
        # know about this bit, i.e. they submit interactive jobs only.
        JOB_NONINTERACTIVE = 0x10        # set for noninteractive
        JOB_INPUT_FLAGS = (
            JOB_RUN_PERIODICALLY |
            JOB_ADD_CURRENT_DATE |
            JOB_NONINTERACTIVE
        )
        JOB_OUTPUT_FLAGS = (
            JOB_RUN_PERIODICALLY |
            JOB_EXEC_ERROR |
            JOB_RUNS_TODAY |
            JOB_NONINTERACTIVE
        )

        _AT_INFO._fields_ = [
            ('JobTime', DWORD_PTR),
            ('DaysOfMonth', DWORD),
            ('DaysOfWeek', UCHAR),
            ('Flags', UCHAR),
            ('Command', LPWSTR),
        ]

        _AT_ENUM._fields_ = [
            ('JobId', DWORD),
            ('JobTime', DWORD_PTR),
            ('DaysOfMonth', DWORD),
            ('DaysOfWeek', UCHAR),
            ('Flags', UCHAR),
            ('Command', LPWSTR),
        ]
        netapi32 = ctypes.windll.NETAPI32

        # NET_API_STATUS NET_API_FUNCTION
        # NetScheduleJobAdd(
        # IN      LPCWSTR         Servername  OPTIONAL,
        # IN      LPBYTE          Buffer,
        # OUT     LPDWORD         JobId
        # );
        NetScheduleJobAdd = netapi32.NetScheduleJobAdd
        NetScheduleJobAdd.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetScheduleJobDel(
        # IN      LPCWSTR         Servername  OPTIONAL,
        # IN      DWORD           MinJobId,
        # IN      DWORD           MaxJobId
        # );
        NetScheduleJobDel = netapi32.NetScheduleJobDel
        NetScheduleJobDel.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetScheduleJobEnum(
        # IN      LPCWSTR         Servername              OPTIONAL,
        # OUT     LPBYTE *        PointerToBuffer,
        # IN      DWORD           PrefferedMaximumLength,
        # OUT     LPDWORD         EntriesRead,
        # OUT     LPDWORD         TotalEntries,
        # IN OUT  LPDWORD         ResumeHandle
        # );
        NetScheduleJobEnum = netapi32.NetScheduleJobEnum
        NetScheduleJobEnum.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetScheduleJobGetInfo(
        # IN      LPCWSTR         Servername              OPTIONAL,
        # IN      DWORD           JobId,
        # OUT     LPBYTE *        PointerToBuffer
        # );
        NetScheduleJobGetInfo = netapi32.NetScheduleJobGetInfo
        NetScheduleJobGetInfo.restype = NET_API_STATUS

        if defined(__cplusplus):
            pass
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF   _LMAT_


