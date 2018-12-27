import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_ALERT_ = None


class _STD_ALERT(ctypes.Structure):
    pass


STD_ALERT = _STD_ALERT
PSTD_ALERT = POINTER(_STD_ALERT)
LPSTD_ALERT = POINTER(_STD_ALERT)


class _ADMIN_OTHER_INFO(ctypes.Structure):
    pass


ADMIN_OTHER_INFO = _ADMIN_OTHER_INFO
PADMIN_OTHER_INFO = POINTER(_ADMIN_OTHER_INFO)
LPADMIN_OTHER_INFO = POINTER(_ADMIN_OTHER_INFO)


class _ERRLOG_OTHER_INFO(ctypes.Structure):
    pass


ERRLOG_OTHER_INFO = _ERRLOG_OTHER_INFO
PERRLOG_OTHER_INFO = POINTER(_ERRLOG_OTHER_INFO)
LPERRLOG_OTHER_INFO = POINTER(_ERRLOG_OTHER_INFO)


class _PRINT_OTHER_INFO(ctypes.Structure):
    pass


PRINT_OTHER_INFO = _PRINT_OTHER_INFO
PPRINT_OTHER_INFO = POINTER(_PRINT_OTHER_INFO)
LPPRINT_OTHER_INFO = POINTER(_PRINT_OTHER_INFO)


class _USER_OTHER_INFO(ctypes.Structure):
    pass


USER_OTHER_INFO = _USER_OTHER_INFO
PUSER_OTHER_INFO = POINTER(_USER_OTHER_INFO)
LPUSER_OTHER_INFO = POINTER(_USER_OTHER_INFO)


# /* + + BUILD Version: 0003 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: alert.h Abstract:
# This file contains structures for communication with the Alerter service.
# Environment: User Mode - Win32 Notes: You must include LmCons.H before this
# file, since this file depends on values defined in LmCons.H. ALERT.H
# includes ALERTMSG.H which defines the alert message numbers --
if not defined(_ALERT_):
    _ALERT_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        netapi32 = ctypes.windll.NETAPI32
        from pyWinAPI.shared.lmcons_h import *  # NOQA

        if defined(__cplusplus):
            pass
            # extern "C" {
        # ENDIF
        #
        #
        # // Function Prototypes
        #
        #
        # NET_API_STATUS NET_API_FUNCTION
        # NetAlertRaise(
        # _In_ LPCWSTR AlertType,
        # _In_ LPVOID  Buffer,
        # _In_ DWORD   BufferSize
        # );
        NetAlertRaise = netapi32.NetAlertRaise
        NetAlertRaise.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetAlertRaiseEx(
        # _In_ LPCWSTR AlertType,
        # _In_ LPVOID  VariableInfo,
        # _In_ DWORD   VariableInfoSize,
        # _In_ LPCWSTR ServiceName
        # );
        NetAlertRaiseEx = netapi32.NetAlertRaiseEx
        NetAlertRaiseEx.restype = NET_API_STATUS

        # Data Structures
        _STD_ALERT._fields_ = [
            ('alrt_timestamp', DWORD),
            ('alrt_eventname', WCHAR * EVLEN + 1),
            ('alrt_servicename', WCHAR * SNLEN + 1),
        ]
        _ADMIN_OTHER_INFO._fields_ = [
            ('alrtad_errcode', DWORD),
            ('alrtad_numstrings', DWORD),
        ]
        _ERRLOG_OTHER_INFO._fields_ = [
            ('alrter_errcode', DWORD),
            ('alrter_offset', DWORD),
        ]
        _PRINT_OTHER_INFO._fields_ = [
            ('alrtpr_jobid', DWORD),
            ('alrtpr_status', DWORD),
            ('alrtpr_submitted', DWORD),
            ('alrtpr_size', DWORD),
        ]
        _USER_OTHER_INFO._fields_ = [
            ('alrtus_errcode', DWORD),
            ('alrtus_numstrings', DWORD),
        ]
        # Special Values and Constants
        # Name of mailslot to send alert notifications
        ALERTER_MAILSLOT = "\\\\.\\MAILSLOT\\Alerter"

        # The following macro gives a pointer to the other_info data.
        # It takes an alert structure and returns a pointer to structure
        # beyond the standard portion.
        def ALERT_OTHER_INFO(x):
            return x + ctypes.sizeof(STD_ALERT)


        # The following macro gives a pointer to the variable-length data.
        # It takes a pointer to one of the other-info structs and returns a
        # pointer to the variable data portion.
        def ALERT_VAR_DATA(p):
            return p + ctypes.sizeof(POINTER(p))


        # Names of standard Microsoft-defined alert events.
        ALERT_PRINT_EVENT = "PRINTING"
        ALERT_MESSAGE_EVENT = "MESSAGE"
        ALERT_ERRORLOG_EVENT = "ERRORLOG"
        ALERT_ADMIN_EVENT = "ADMIN"
        ALERT_USER_EVENT = "USER"
        # Bitmap masks for prjob_status field of PRINTJOB.
        # 2-7 bits also used in device status
        PRJOB_QSTATUS = 0x3  # Bits 0,1
        PRJOB_DEVSTATUS = 0x1FC  # 2-8 bits
        PRJOB_COMPLETE = 0x4  # Bit 2
        PRJOB_INTERV = 0x8  # Bit 3
        PRJOB_ERROR = 0x10  # Bit 4
        PRJOB_DESTOFFLINE = 0x20  # Bit 5
        PRJOB_DESTPAUSED = 0x40  # Bit 6
        PRJOB_NOTIFY = 0x80  # BIT 7
        PRJOB_DESTNOPAPER = 0x100  # BIT 8
        PRJOB_DELETED = 0x8000  # BIT 15
        # Values of PRJOB_QSTATUS bits in prjob_status field of PRINTJOB.
        PRJOB_QS_QUEUED = 0
        PRJOB_QS_PAUSED = 1
        PRJOB_QS_SPOOLING = 2
        PRJOB_QS_PRINTING = 3
        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   _ALERT_


