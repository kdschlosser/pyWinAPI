import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMSTATS_ = None
LM20_WORKSTATION_STATISTICS = None

class _STAT_WORKSTATION_0(ctypes.Structure):
    pass


STAT_WORKSTATION_0 = _STAT_WORKSTATION_0
PSTAT_WORKSTATION_0 = POINTER(_STAT_WORKSTATION_0)
LPSTAT_WORKSTATION_0 = POINTER(_STAT_WORKSTATION_0)


STAT_WORKSTATION_0 = _STAT_WORKSTATION_0
PSTAT_WORKSTATION_0 = POINTER(_STAT_WORKSTATION_0)
LPSTAT_WORKSTATION_0 = POINTER(_STAT_WORKSTATION_0)


class _STAT_SERVER_0(ctypes.Structure):
    pass


STAT_SERVER_0 = _STAT_SERVER_0
PSTAT_SERVER_0 = POINTER(_STAT_SERVER_0)
LPSTAT_SERVER_0 = POINTER(_STAT_SERVER_0)


# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmstats.h
# Abstract: This module defines the API function prototypes and data
# structures for the following groups of NT API functions: NetStatistics
# Environment: User Mode - Win32 Notes: You must include NETCONS.H before this
# file, since this file depends on values defined in NETCONS.H. --
if not defined(_LMSTATS_):
    _LMSTATS_ = VOID

    netapi32 = ctypes.windll.NETAPI32

    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if defined(__cplusplus):
            pass
        # END IF

        from pyWinAPI.shared.lmcons_h import * # NOQA

        # // Function Prototypes - Statistics
        #
        #
        # NET_API_STATUS NET_API_FUNCTION
        # NetStatisticsGet(
        # _In_        LPTSTR  ServerName,
        # _In_        LPTSTR  Service,
          # _In_        DWORD   Level,
        # _In_        DWORD   Options,
        # _Outptr_ LPBYTE *Buffer
        # );
        NetStatisticsGet = netapi32.NetStatisticsGet
        NetStatisticsGet.restype = NET_API_STATUS
        # Data Structures - Statistics

        if defined(LM20_WORKSTATION_STATISTICS):
            _STAT_WORKSTATION_0._fields_ = [
                ('stw0_start', DWORD),
                ('stw0_numNCB_r', DWORD),
                ('stw0_numNCB_s', DWORD),
                ('stw0_numNCB_a', DWORD),
                ('stw0_fiNCB_r', DWORD),
                ('stw0_fiNCB_s', DWORD),
                ('stw0_fiNCB_a', DWORD),
                ('stw0_fcNCB_r', DWORD),
                ('stw0_fcNCB_s', DWORD),
                ('stw0_fcNCB_a', DWORD),
                ('stw0_sesstart', DWORD),
                ('stw0_sessfailcon', DWORD),
                ('stw0_sessbroke', DWORD),
                ('stw0_uses', DWORD),
                ('stw0_usefail', DWORD),
                ('stw0_autorec', DWORD),
                ('stw0_bytessent_r_lo', DWORD),
                ('stw0_bytessent_r_hi', DWORD),
                ('stw0_bytesrcvd_r_lo', DWORD),
                ('stw0_bytesrcvd_r_hi', DWORD),
                ('stw0_bytessent_s_lo', DWORD),
                ('stw0_bytessent_s_hi', DWORD),
                ('stw0_bytesrcvd_s_lo', DWORD),
                ('stw0_bytesrcvd_s_hi', DWORD),
                ('stw0_bytessent_a_lo', DWORD),
                ('stw0_bytessent_a_hi', DWORD),
                ('stw0_bytesrcvd_a_lo', DWORD),
                ('stw0_bytesrcvd_a_hi', DWORD),
                ('stw0_reqbufneed', DWORD),
                ('stw0_bigbufneed', DWORD),
            ]

        else:
            # NB: The following structure is REDIR_STATISTICS in
            # sdk\inc\ntddnfs.h. If you
            # change the structure, change it in both places
            _STAT_WORKSTATION_0._fields_ = [
                ('StatisticsStartTime', LARGE_INTEGER),
                ('BytesReceived', LARGE_INTEGER),
                ('SmbsReceived', LARGE_INTEGER),
                ('PagingReadBytesRequested', LARGE_INTEGER),
                ('NonPagingReadBytesRequested', LARGE_INTEGER),
                ('CacheReadBytesRequested', LARGE_INTEGER),
                ('NetworkReadBytesRequested', LARGE_INTEGER),
                ('BytesTransmitted', LARGE_INTEGER),
                ('SmbsTransmitted', LARGE_INTEGER),
                ('PagingWriteBytesRequested', LARGE_INTEGER),
                ('NonPagingWriteBytesRequested', LARGE_INTEGER),
                ('CacheWriteBytesRequested', LARGE_INTEGER),
                ('NetworkWriteBytesRequested', LARGE_INTEGER),
                ('InitiallyFailedOperations', DWORD),
                ('FailedCompletionOperations', DWORD),
                ('ReadOperations', DWORD),
                ('RandomReadOperations', DWORD),
                ('ReadSmbs', DWORD),
                ('LargeReadSmbs', DWORD),
                ('SmallReadSmbs', DWORD),
                ('WriteOperations', DWORD),
                ('RandomWriteOperations', DWORD),
                ('WriteSmbs', DWORD),
                ('LargeWriteSmbs', DWORD),
                ('SmallWriteSmbs', DWORD),
                ('RawReadsDenied', DWORD),
                ('RawWritesDenied', DWORD),
                ('NetworkErrors', DWORD),
                # Connection/Session counts
                ('Sessions', DWORD),
                ('FailedSessions', DWORD),
                ('Reconnects', DWORD),
                ('CoreConnects', DWORD),
                ('Lanman20Connects', DWORD),
                ('Lanman21Connects', DWORD),
                ('LanmanNtConnects', DWORD),
                ('ServerDisconnects', DWORD),
                ('HungSessions', DWORD),
                ('UseCount', DWORD),
                ('FailedUseCount', DWORD),
                # RdrStatisticsSpinlock)
                ('CurrentCommands', DWORD),
            ]
        # END IF
        _STAT_SERVER_0._fields_ = [
            ('sts0_start', DWORD),
            ('sts0_fopens', DWORD),
            ('sts0_devopens', DWORD),
            ('sts0_jobsqueued', DWORD),
            ('sts0_sopens', DWORD),
            ('sts0_stimedout', DWORD),
            ('sts0_serrorout', DWORD),
            ('sts0_pwerrors', DWORD),
            ('sts0_permerrors', DWORD),
            ('sts0_syserrors', DWORD),
            ('sts0_bytessent_low', DWORD),
            ('sts0_bytessent_high', DWORD),
            ('sts0_bytesrcvd_low', DWORD),
            ('sts0_bytesrcvd_high', DWORD),
            ('sts0_avresponse', DWORD),
            ('sts0_reqbufneed', DWORD),
            ('sts0_bigbufneed', DWORD),
        ]
        # Special Values and Constants
        STATSOPT_CLR = 1
        STATS_NO_VALUE = -1
        STATS_OVERFLOW = -2

        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   _LMSTATS.H


