import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMWKSTA_ = None


class _WKSTA_INFO_100(ctypes.Structure):
    pass


WKSTA_INFO_100 = _WKSTA_INFO_100
PWKSTA_INFO_100 = POINTER(_WKSTA_INFO_100)
LPWKSTA_INFO_100 = POINTER(_WKSTA_INFO_100)


class _WKSTA_INFO_101(ctypes.Structure):
    pass


WKSTA_INFO_101 = _WKSTA_INFO_101
PWKSTA_INFO_101 = POINTER(_WKSTA_INFO_101)
LPWKSTA_INFO_101 = POINTER(_WKSTA_INFO_101)


class _WKSTA_INFO_102(ctypes.Structure):
    pass


WKSTA_INFO_102 = _WKSTA_INFO_102
PWKSTA_INFO_102 = POINTER(_WKSTA_INFO_102)
LPWKSTA_INFO_102 = POINTER(_WKSTA_INFO_102)


class _WKSTA_INFO_302(ctypes.Structure):
    pass


WKSTA_INFO_302 = _WKSTA_INFO_302
PWKSTA_INFO_302 = POINTER(_WKSTA_INFO_302)
LPWKSTA_INFO_302 = POINTER(_WKSTA_INFO_302)


class _WKSTA_INFO_402(ctypes.Structure):
    pass


WKSTA_INFO_402 = _WKSTA_INFO_402
PWKSTA_INFO_402 = POINTER(_WKSTA_INFO_402)
LPWKSTA_INFO_402 = POINTER(_WKSTA_INFO_402)


class _WKSTA_INFO_502(ctypes.Structure):
    pass


WKSTA_INFO_502 = _WKSTA_INFO_502
PWKSTA_INFO_502 = POINTER(_WKSTA_INFO_502)
LPWKSTA_INFO_502 = POINTER(_WKSTA_INFO_502)


class _WKSTA_INFO_1010(ctypes.Structure):
    pass


WKSTA_INFO_1010 = _WKSTA_INFO_1010
PWKSTA_INFO_1010 = POINTER(_WKSTA_INFO_1010)
LPWKSTA_INFO_1010 = POINTER(_WKSTA_INFO_1010)


class _WKSTA_INFO_1011(ctypes.Structure):
    pass


WKSTA_INFO_1011 = _WKSTA_INFO_1011
PWKSTA_INFO_1011 = POINTER(_WKSTA_INFO_1011)
LPWKSTA_INFO_1011 = POINTER(_WKSTA_INFO_1011)


class _WKSTA_INFO_1012(ctypes.Structure):
    pass


WKSTA_INFO_1012 = _WKSTA_INFO_1012
PWKSTA_INFO_1012 = POINTER(_WKSTA_INFO_1012)
LPWKSTA_INFO_1012 = POINTER(_WKSTA_INFO_1012)


class _WKSTA_INFO_1027(ctypes.Structure):
    pass


WKSTA_INFO_1027 = _WKSTA_INFO_1027
PWKSTA_INFO_1027 = POINTER(_WKSTA_INFO_1027)
LPWKSTA_INFO_1027 = POINTER(_WKSTA_INFO_1027)


class _WKSTA_INFO_1028(ctypes.Structure):
    pass


WKSTA_INFO_1028 = _WKSTA_INFO_1028
PWKSTA_INFO_1028 = POINTER(_WKSTA_INFO_1028)
LPWKSTA_INFO_1028 = POINTER(_WKSTA_INFO_1028)


class _WKSTA_INFO_1032(ctypes.Structure):
    pass


WKSTA_INFO_1032 = _WKSTA_INFO_1032
PWKSTA_INFO_1032 = POINTER(_WKSTA_INFO_1032)
LPWKSTA_INFO_1032 = POINTER(_WKSTA_INFO_1032)


class _WKSTA_INFO_1013(ctypes.Structure):
    pass


WKSTA_INFO_1013 = _WKSTA_INFO_1013
PWKSTA_INFO_1013 = POINTER(_WKSTA_INFO_1013)
LPWKSTA_INFO_1013 = POINTER(_WKSTA_INFO_1013)


class _WKSTA_INFO_1018(ctypes.Structure):
    pass


WKSTA_INFO_1018 = _WKSTA_INFO_1018
PWKSTA_INFO_1018 = POINTER(_WKSTA_INFO_1018)
LPWKSTA_INFO_1018 = POINTER(_WKSTA_INFO_1018)


class _WKSTA_INFO_1023(ctypes.Structure):
    pass


WKSTA_INFO_1023 = _WKSTA_INFO_1023
PWKSTA_INFO_1023 = POINTER(_WKSTA_INFO_1023)
LPWKSTA_INFO_1023 = POINTER(_WKSTA_INFO_1023)


class _WKSTA_INFO_1033(ctypes.Structure):
    pass


WKSTA_INFO_1033 = _WKSTA_INFO_1033
PWKSTA_INFO_1033 = POINTER(_WKSTA_INFO_1033)
LPWKSTA_INFO_1033 = POINTER(_WKSTA_INFO_1033)


class _WKSTA_INFO_1041(ctypes.Structure):
    pass


WKSTA_INFO_1041 = _WKSTA_INFO_1041
PWKSTA_INFO_1041 = POINTER(_WKSTA_INFO_1041)
LPWKSTA_INFO_1041 = POINTER(_WKSTA_INFO_1041)


class _WKSTA_INFO_1042(ctypes.Structure):
    pass


WKSTA_INFO_1042 = _WKSTA_INFO_1042
PWKSTA_INFO_1042 = POINTER(_WKSTA_INFO_1042)
LPWKSTA_INFO_1042 = POINTER(_WKSTA_INFO_1042)


class _WKSTA_INFO_1043(ctypes.Structure):
    pass


WKSTA_INFO_1043 = _WKSTA_INFO_1043
PWKSTA_INFO_1043 = POINTER(_WKSTA_INFO_1043)
LPWKSTA_INFO_1043 = POINTER(_WKSTA_INFO_1043)


class _WKSTA_INFO_1044(ctypes.Structure):
    pass


WKSTA_INFO_1044 = _WKSTA_INFO_1044
PWKSTA_INFO_1044 = POINTER(_WKSTA_INFO_1044)
LPWKSTA_INFO_1044 = POINTER(_WKSTA_INFO_1044)


class _WKSTA_INFO_1045(ctypes.Structure):
    pass


WKSTA_INFO_1045 = _WKSTA_INFO_1045
PWKSTA_INFO_1045 = POINTER(_WKSTA_INFO_1045)
LPWKSTA_INFO_1045 = POINTER(_WKSTA_INFO_1045)


class _WKSTA_INFO_1046(ctypes.Structure):
    pass


WKSTA_INFO_1046 = _WKSTA_INFO_1046
PWKSTA_INFO_1046 = POINTER(_WKSTA_INFO_1046)
LPWKSTA_INFO_1046 = POINTER(_WKSTA_INFO_1046)


class _WKSTA_INFO_1047(ctypes.Structure):
    pass


WKSTA_INFO_1047 = _WKSTA_INFO_1047
PWKSTA_INFO_1047 = POINTER(_WKSTA_INFO_1047)
LPWKSTA_INFO_1047 = POINTER(_WKSTA_INFO_1047)


class _WKSTA_INFO_1048(ctypes.Structure):
    pass


WKSTA_INFO_1048 = _WKSTA_INFO_1048
PWKSTA_INFO_1048 = POINTER(_WKSTA_INFO_1048)
LPWKSTA_INFO_1048 = POINTER(_WKSTA_INFO_1048)


class _WKSTA_INFO_1049(ctypes.Structure):
    pass


WKSTA_INFO_1049 = _WKSTA_INFO_1049
PWKSTA_INFO_1049 = POINTER(_WKSTA_INFO_1049)
LPWKSTA_INFO_1049 = POINTER(_WKSTA_INFO_1049)


class _WKSTA_INFO_1050(ctypes.Structure):
    pass


WKSTA_INFO_1050 = _WKSTA_INFO_1050
PWKSTA_INFO_1050 = POINTER(_WKSTA_INFO_1050)
LPWKSTA_INFO_1050 = POINTER(_WKSTA_INFO_1050)


class _WKSTA_INFO_1051(ctypes.Structure):
    pass


WKSTA_INFO_1051 = _WKSTA_INFO_1051
PWKSTA_INFO_1051 = POINTER(_WKSTA_INFO_1051)
LPWKSTA_INFO_1051 = POINTER(_WKSTA_INFO_1051)


class _WKSTA_INFO_1052(ctypes.Structure):
    pass


WKSTA_INFO_1052 = _WKSTA_INFO_1052
PWKSTA_INFO_1052 = POINTER(_WKSTA_INFO_1052)
LPWKSTA_INFO_1052 = POINTER(_WKSTA_INFO_1052)


class _WKSTA_INFO_1053(ctypes.Structure):
    pass


WKSTA_INFO_1053 = _WKSTA_INFO_1053
PWKSTA_INFO_1053 = POINTER(_WKSTA_INFO_1053)
LPWKSTA_INFO_1053 = POINTER(_WKSTA_INFO_1053)


class _WKSTA_INFO_1054(ctypes.Structure):
    pass


WKSTA_INFO_1054 = _WKSTA_INFO_1054
PWKSTA_INFO_1054 = POINTER(_WKSTA_INFO_1054)
LPWKSTA_INFO_1054 = POINTER(_WKSTA_INFO_1054)


class _WKSTA_INFO_1055(ctypes.Structure):
    pass


WKSTA_INFO_1055 = _WKSTA_INFO_1055
PWKSTA_INFO_1055 = POINTER(_WKSTA_INFO_1055)
LPWKSTA_INFO_1055 = POINTER(_WKSTA_INFO_1055)


class _WKSTA_INFO_1056(ctypes.Structure):
    pass


WKSTA_INFO_1056 = _WKSTA_INFO_1056
PWKSTA_INFO_1056 = POINTER(_WKSTA_INFO_1056)
LPWKSTA_INFO_1056 = POINTER(_WKSTA_INFO_1056)


class _WKSTA_INFO_1057(ctypes.Structure):
    pass


WKSTA_INFO_1057 = _WKSTA_INFO_1057
PWKSTA_INFO_1057 = POINTER(_WKSTA_INFO_1057)
LPWKSTA_INFO_1057 = POINTER(_WKSTA_INFO_1057)


class _WKSTA_INFO_1058(ctypes.Structure):
    pass


WKSTA_INFO_1058 = _WKSTA_INFO_1058
PWKSTA_INFO_1058 = POINTER(_WKSTA_INFO_1058)
LPWKSTA_INFO_1058 = POINTER(_WKSTA_INFO_1058)


class _WKSTA_INFO_1059(ctypes.Structure):
    pass


WKSTA_INFO_1059 = _WKSTA_INFO_1059
PWKSTA_INFO_1059 = POINTER(_WKSTA_INFO_1059)
LPWKSTA_INFO_1059 = POINTER(_WKSTA_INFO_1059)


class _WKSTA_INFO_1060(ctypes.Structure):
    pass


WKSTA_INFO_1060 = _WKSTA_INFO_1060
PWKSTA_INFO_1060 = POINTER(_WKSTA_INFO_1060)
LPWKSTA_INFO_1060 = POINTER(_WKSTA_INFO_1060)


class _WKSTA_INFO_1061(ctypes.Structure):
    pass


WKSTA_INFO_1061 = _WKSTA_INFO_1061
PWKSTA_INFO_1061 = POINTER(_WKSTA_INFO_1061)
LPWKSTA_INFO_1061 = POINTER(_WKSTA_INFO_1061)


class _WKSTA_INFO_1062(ctypes.Structure):
    pass


WKSTA_INFO_1062 = _WKSTA_INFO_1062
PWKSTA_INFO_1062 = POINTER(_WKSTA_INFO_1062)
LPWKSTA_INFO_1062 = POINTER(_WKSTA_INFO_1062)


class _WKSTA_USER_INFO_0(ctypes.Structure):
    pass


WKSTA_USER_INFO_0 = _WKSTA_USER_INFO_0
PWKSTA_USER_INFO_0 = POINTER(_WKSTA_USER_INFO_0)
LPWKSTA_USER_INFO_0 = POINTER(_WKSTA_USER_INFO_0)


class _WKSTA_USER_INFO_1(ctypes.Structure):
    pass


WKSTA_USER_INFO_1 = _WKSTA_USER_INFO_1
PWKSTA_USER_INFO_1 = POINTER(_WKSTA_USER_INFO_1)
LPWKSTA_USER_INFO_1 = POINTER(_WKSTA_USER_INFO_1)


class _WKSTA_USER_INFO_1101(ctypes.Structure):
    pass


WKSTA_USER_INFO_1101 = _WKSTA_USER_INFO_1101
PWKSTA_USER_INFO_1101 = POINTER(_WKSTA_USER_INFO_1101)
LPWKSTA_USER_INFO_1101 = POINTER(_WKSTA_USER_INFO_1101)


class _WKSTA_TRANSPORT_INFO_0(ctypes.Structure):
    pass


WKSTA_TRANSPORT_INFO_0 = _WKSTA_TRANSPORT_INFO_0
PWKSTA_TRANSPORT_INFO_0 = POINTER(_WKSTA_TRANSPORT_INFO_0)
LPWKSTA_TRANSPORT_INFO_0 = POINTER(_WKSTA_TRANSPORT_INFO_0)


# /* + + BUILD Version: 0006 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmwksta.h
# Abstract: This file contains structures, function prototypes, and
# definitions for the NetWorkstation and NetWkstaTransport API. Environment:
# User Mode - Win32 Portable to any flat, 32-bit environment.
# (Uses Win32 typedefs.) Requires ANSI C extensions: slash-slash comments,
# LONG external names. Notes: You must include NETCONS.H before this file,
# since this file depends on values defined in NETCONS.H. --

if not defined(_LMWKSTA_):
    _LMWKSTA_ = VOID

    netapi32 = ctypes.windll.NETAPI32

    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if defined(__cplusplus):
            pass
        # END IF

        from pyWinAPI.shared.lmcons_h import * # NOQA
        from pyWinAPI.um.lmuseflg_h import * # NOQA

        if _MSC_VER >= 1200:
            pass
        # END IF

        # // Function Prototypes
        #
        #
        # NET_API_STATUS NET_API_FUNCTION
        # NetWkstaGetInfo(
        # _In_opt_ LMSTR   servername OPTIONAL,
        # _In_     DWORD   level,
        # _Outptr_opt_result_buffer_(_Inexpressible_("size varies with level")) OUT LPBYTE  *bufptr
        # );
        NetWkstaGetInfo = netapi32.NetWkstaGetInfo
        NetWkstaGetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetWkstaSetInfo(
        # _In_opt_  LMSTR   servername OPTIONAL,
        # _In_      DWORD   level,
        # _In_reads_(_Inexpressible_("varies")) LPBYTE  buffer,
        # _Out_opt_ OUT LPDWORD parm_err OPTIONAL
        # );
        NetWkstaSetInfo = netapi32.NetWkstaSetInfo
        NetWkstaSetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetWkstaUserGetInfo(
        # _In_opt_ LMSTR  reserved,
        # _In_     DWORD   level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) OUT LPBYTE  *bufptr
        # );
        NetWkstaUserGetInfo = netapi32.NetWkstaUserGetInfo
        NetWkstaUserGetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetWkstaUserSetInfo(
        # _In_opt_  LMSTR  reserved,
        # _In_      DWORD   level,
        # _In_reads_(_Inexpressible_("varies")) LPBYTE  buf,
        # _Out_opt_ LPDWORD parm_err OPTIONAL
        # );
        NetWkstaUserSetInfo = netapi32.NetWkstaUserSetInfo
        NetWkstaUserSetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetWkstaUserEnum(
        # _In_opt_ LMSTR       servername OPTIONAL,
        # IN  DWORD       level,
        # _Out_opt_ LPBYTE      *bufptr,
        # IN  DWORD       prefmaxlen,
        # _Out_opt_ LPDWORD     entriesread,
        # _Out_ LPDWORD     totalentries,
        # _Inout_opt_ LPDWORD resumehandle OPTIONAL
        # );
        NetWkstaUserEnum = netapi32.NetWkstaUserEnum
        NetWkstaUserEnum.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetWkstaTransportAdd(
        # _In_opt_ LPTSTR servername,
        # _In_ DWORD level,
        # _When_( level == 0, _In_reads_bytes_((ctypes.sizeof(WKSTA_TRANSPORT_INFO_0)))
        # LPBYTE buf,
        # _Out_opt_ LPDWORD parm_err
        # );
        NetWkstaTransportAdd = netapi32.NetWkstaTransportAdd
        NetWkstaTransportAdd.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetWkstaTransportDel(
        # _In_opt_ IN  LMSTR   servername OPTIONAL,
        # _In_opt_ IN  LMSTR   transportname,
        # IN  DWORD   ucond
        # );
        NetWkstaTransportDel = netapi32.NetWkstaTransportDel
        NetWkstaTransportDel.restype = NET_API_STATUS

        # _Check_return_
        # _Success_( return == NERR_Success or return == ERROR_MORE_DATA )
        # NET_API_STATUS NET_API_FUNCTION
        # NetWkstaTransportEnum(
        # _In_opt_ LPTSTR servername,
        # _In_ DWORD level,
        # _When_( level == 0, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(WKSTA_TRANSPORT_INFO_0)) )
        # LPBYTE *bufptr,
        # _In_ DWORD prefmaxlen,
        # _Out_ LPDWORD entriesread,
        # _Out_ LPDWORD totalentries,
        # _Inout_opt_ LPDWORD resume_handle
        # );
        NetWkstaTransportEnum = netapi32.NetWkstaTransportEnum
        NetWkstaTransportEnum.restype = NET_API_STATUS

        # Data Structures
        # NetWkstaGetInfo and NetWkstaSetInfo
        # NetWkstaGetInfo only. System information - guest access
        _WKSTA_INFO_100._fields_ = [
            ('wki100_platform_id', DWORD),
            ('wki100_computername', LMSTR),
            ('wki100_langroup', LMSTR),
            ('wki100_ver_major', DWORD),
            ('wki100_ver_minor', DWORD),
        ]
        # NetWkstaGetInfo only. System information - user access
        _WKSTA_INFO_101._fields_ = [
            ('wki101_platform_id', DWORD),
            ('wki101_computername', LMSTR),
            ('wki101_langroup', LMSTR),
            ('wki101_ver_major', DWORD),
            ('wki101_ver_minor', DWORD),
            ('wki101_lanroot', LMSTR),
        ]
        # NetWkstaGetInfo only. System information - admin or operator
        # access
        _WKSTA_INFO_102._fields_ = [
            ('wki102_platform_id', DWORD),
            ('wki102_computername', LMSTR),
            ('wki102_langroup', LMSTR),
            ('wki102_ver_major', DWORD),
            ('wki102_ver_minor', DWORD),
            ('wki102_lanroot', LMSTR),
            ('wki102_logged_on_users', DWORD),
        ]
        # Down-level NetWkstaGetInfo and NetWkstaSetInfo.
        # DOS specific workstation information -
        # admin or domain operator access
        _WKSTA_INFO_302._fields_ = [
            ('wki302_char_wait', DWORD),
            ('wki302_collection_time', DWORD),
            ('wki302_maximum_collection_count', DWORD),
            ('wki302_keep_conn', DWORD),
            ('wki302_keep_search', DWORD),
            ('wki302_max_cmds', DWORD),
            ('wki302_num_work_buf', DWORD),
            ('wki302_siz_work_buf', DWORD),
            ('wki302_max_wrk_cache', DWORD),
            ('wki302_sess_timeout', DWORD),
            ('wki302_siz_error', DWORD),
            ('wki302_num_alerts', DWORD),
            ('wki302_num_services', DWORD),
            ('wki302_errlog_sz', DWORD),
            ('wki302_print_buf_time', DWORD),
            ('wki302_num_char_buf', DWORD),
            ('wki302_siz_char_buf', DWORD),
            ('wki302_wrk_heuristics', LMSTR),
            ('wki302_mailslots', DWORD),
            ('wki302_num_dgram_buf', DWORD),
        ]
        # Down-level NetWkstaGetInfo and NetWkstaSetInfo
        # OS/2 specific workstation information -
        # admin or domain operator access
        _WKSTA_INFO_402._fields_ = [
            ('wki402_char_wait', DWORD),
            ('wki402_collection_time', DWORD),
            ('wki402_maximum_collection_count', DWORD),
            ('wki402_keep_conn', DWORD),
            ('wki402_keep_search', DWORD),
            ('wki402_max_cmds', DWORD),
            ('wki402_num_work_buf', DWORD),
            ('wki402_siz_work_buf', DWORD),
            ('wki402_max_wrk_cache', DWORD),
            ('wki402_sess_timeout', DWORD),
            ('wki402_siz_error', DWORD),
            ('wki402_num_alerts', DWORD),
            ('wki402_num_services', DWORD),
            ('wki402_errlog_sz', DWORD),
            ('wki402_print_buf_time', DWORD),
            ('wki402_num_char_buf', DWORD),
            ('wki402_siz_char_buf', DWORD),
            ('wki402_wrk_heuristics', LMSTR),
            ('wki402_mailslots', DWORD),
            ('wki402_num_dgram_buf', DWORD),
            ('wki402_max_threads', DWORD),
        ]
        # Same-level NetWkstaGetInfo and NetWkstaSetInfo.
        # NT specific workstation information -
        # admin or domain operator access
        _WKSTA_INFO_502._fields_ = [
            ('wki502_char_wait', DWORD),
            ('wki502_collection_time', DWORD),
            ('wki502_maximum_collection_count', DWORD),
            ('wki502_keep_conn', DWORD),
            ('wki502_max_cmds', DWORD),
            ('wki502_sess_timeout', DWORD),
            ('wki502_siz_char_buf', DWORD),
            ('wki502_max_threads', DWORD),
            ('wki502_lock_quota', DWORD),
            ('wki502_lock_increment', DWORD),
            ('wki502_lock_maximum', DWORD),
            ('wki502_pipe_increment', DWORD),
            ('wki502_pipe_maximum', DWORD),
            ('wki502_cache_file_timeout', DWORD),
            ('wki502_dormant_file_limit', DWORD),
            ('wki502_read_ahead_throughput', DWORD),
            ('wki502_num_mailslot_buffers', DWORD),
            ('wki502_num_srv_announce_buffers', DWORD),
            ('wki502_max_illegal_datagram_events', DWORD),
            ('wki502_illegal_datagram_event_reset_frequency', DWORD),
            ('wki502_log_election_packets', BOOL),
            ('wki502_use_opportunistic_locking', BOOL),
            ('wki502_use_unlock_behind', BOOL),
            ('wki502_use_close_behind', BOOL),
            ('wki502_buf_named_pipes', BOOL),
            ('wki502_use_lock_read_unlock', BOOL),
            ('wki502_utilize_nt_caching', BOOL),
            ('wki502_use_raw_read', BOOL),
            ('wki502_use_raw_write', BOOL),
            ('wki502_use_write_raw_data', BOOL),
            ('wki502_use_encryption', BOOL),
            ('wki502_buf_files_deny_write', BOOL),
            ('wki502_buf_read_only_files', BOOL),
            ('wki502_force_core_create_mode', BOOL),
            ('wki502_use_512_byte_max_transfer', BOOL),
        ]
        # The following info-levels are only valid for NetWkstaSetInfo
        # The following levels are supported on down-level systems
        # (LAN Man 2.x)
        # as well as NT systems:
        _WKSTA_INFO_1010._fields_ = [
            ('wki1010_char_wait', DWORD),
        ]
        _WKSTA_INFO_1011._fields_ = [
            ('wki1011_collection_time', DWORD),
        ]
        _WKSTA_INFO_1012._fields_ = [
            ('wki1012_maximum_collection_count', DWORD),
        ]
        # The following level are supported on down-level systems
        # (LAN Man 2.x)
        # only:
        _WKSTA_INFO_1027._fields_ = [
            ('wki1027_errlog_sz', DWORD),
        ]
        _WKSTA_INFO_1028._fields_ = [
            ('wki1028_print_buf_time', DWORD),
        ]
        _WKSTA_INFO_1032._fields_ = [
            ('wki1032_wrk_heuristics', DWORD),
        ]
        # The following levels are settable on NT systems, and have no
        # effect on down-level systems (i.e. LANMan 2.x) since these
        # fields cannot be set on them:
        _WKSTA_INFO_1013._fields_ = [
            ('wki1013_keep_conn', DWORD),
        ]
        _WKSTA_INFO_1018._fields_ = [
            ('wki1018_sess_timeout', DWORD),
        ]
        _WKSTA_INFO_1023._fields_ = [
            ('wki1023_siz_char_buf', DWORD),
        ]
        _WKSTA_INFO_1033._fields_ = [
            ('wki1033_max_threads', DWORD),
        ]
        # The following levels are only supported on NT systems:
        _WKSTA_INFO_1041._fields_ = [
            ('wki1041_lock_quota', DWORD),
        ]
        _WKSTA_INFO_1042._fields_ = [
            ('wki1042_lock_increment', DWORD),
        ]
        _WKSTA_INFO_1043._fields_ = [
            ('wki1043_lock_maximum', DWORD),
        ]
        _WKSTA_INFO_1044._fields_ = [
            ('wki1044_pipe_increment', DWORD),
        ]
        _WKSTA_INFO_1045._fields_ = [
            ('wki1045_pipe_maximum', DWORD),
        ]
        _WKSTA_INFO_1046._fields_ = [
            ('wki1046_dormant_file_limit', DWORD),
        ]
        _WKSTA_INFO_1047._fields_ = [
            ('wki1047_cache_file_timeout', DWORD),
        ]
        _WKSTA_INFO_1048._fields_ = [
            ('wki1048_use_opportunistic_locking', BOOL),
        ]
        _WKSTA_INFO_1049._fields_ = [
            ('wki1049_use_unlock_behind', BOOL),
        ]
        _WKSTA_INFO_1050._fields_ = [
            ('wki1050_use_close_behind', BOOL),
        ]
        _WKSTA_INFO_1051._fields_ = [
            ('wki1051_buf_named_pipes', BOOL),
        ]
        _WKSTA_INFO_1052._fields_ = [
            ('wki1052_use_lock_read_unlock', BOOL),
        ]
        _WKSTA_INFO_1053._fields_ = [
            ('wki1053_utilize_nt_caching', BOOL),
        ]
        _WKSTA_INFO_1054._fields_ = [
            ('wki1054_use_raw_read', BOOL),
        ]
        _WKSTA_INFO_1055._fields_ = [
            ('wki1055_use_raw_write', BOOL),
        ]
        _WKSTA_INFO_1056._fields_ = [
            ('wki1056_use_write_raw_data', BOOL),
        ]
        _WKSTA_INFO_1057._fields_ = [
            ('wki1057_use_encryption', BOOL),
        ]
        _WKSTA_INFO_1058._fields_ = [
            ('wki1058_buf_files_deny_write', BOOL),
        ]
        _WKSTA_INFO_1059._fields_ = [
            ('wki1059_buf_read_only_files', BOOL),
        ]
        _WKSTA_INFO_1060._fields_ = [
            ('wki1060_force_core_create_mode', BOOL),
        ]
        _WKSTA_INFO_1061._fields_ = [
            ('wki1061_use_512_byte_max_transfer', BOOL),
        ]
        _WKSTA_INFO_1062._fields_ = [
            ('wki1062_read_ahead_throughput', DWORD),
        ]
        # NetWkstaUserGetInfo (local only) and NetWkstaUserEnum -
        # no access restrictions.
        _WKSTA_USER_INFO_0._fields_ = [
            ('wkui0_username', LMSTR),
        ]
        # NetWkstaUserGetInfo (local only) and NetWkstaUserEnum -
        # no access restrictions.
        _WKSTA_USER_INFO_1._fields_ = [
            ('wkui1_username', LMSTR),
            ('wkui1_logon_domain', LMSTR),
            ('wkui1_oth_domains', LMSTR),
            ('wkui1_logon_server', LMSTR),
        ]
        # NetWkstaUserSetInfo - local access.
        _WKSTA_USER_INFO_1101._fields_ = [
            ('wkui1101_oth_domains', LMSTR),
        ]
        # NetWkstaTransportAdd - admin access
        _WKSTA_TRANSPORT_INFO_0._fields_ = [
            ('wkti0_quality_of_service', DWORD),
            ('wkti0_number_of_vcs', DWORD),
            ('wkti0_transport_name', LMSTR),
            ('wkti0_transport_address', LMSTR),
            ('wkti0_wan_ish', BOOL),
        ]
        # Special Values and Constants
        # Identifiers for use as NetWkstaSetInfo parmnum parameter
        # One of these values indicates the parameter within an information
        # structure that is invalid when ERROR_INVALID_PARAMETER is
        # returned by
        # NetWkstaSetInfo.
        WKSTA_PLATFORM_ID_PARMNUM = 100
        WKSTA_COMPUTERNAME_PARMNUM = 1
        WKSTA_LANGROUP_PARMNUM = 2
        WKSTA_VER_MAJOR_PARMNUM = 4
        WKSTA_VER_MINOR_PARMNUM = 5
        WKSTA_LOGGED_ON_USERS_PARMNUM = 6
        WKSTA_LANROOT_PARMNUM = 7
        WKSTA_LOGON_DOMAIN_PARMNUM = 8
        WKSTA_LOGON_SERVER_PARMNUM = 9
        WKSTA_CHARWAIT_PARMNUM = 10  # Supported by down-level.
        WKSTA_CHARTIME_PARMNUM = 11  # Supported by down-level.
        WKSTA_CHARCOUNT_PARMNUM = 12  # Supported by down-level.
        WKSTA_KEEPCONN_PARMNUM = 13
        WKSTA_KEEPSEARCH_PARMNUM = 14
        WKSTA_MAXCMDS_PARMNUM = 15
        WKSTA_NUMWORKBUF_PARMNUM = 16
        WKSTA_MAXWRKCACHE_PARMNUM = 17
        WKSTA_SESSTIMEOUT_PARMNUM = 18
        WKSTA_SIZERROR_PARMNUM = 19
        WKSTA_NUMALERTS_PARMNUM = 20
        WKSTA_NUMSERVICES_PARMNUM = 21
        WKSTA_NUMCHARBUF_PARMNUM = 22
        WKSTA_SIZCHARBUF_PARMNUM = 23
        WKSTA_ERRLOGSZ_PARMNUM = 27  # Supported by down-level.
        WKSTA_PRINTBUFTIME_PARMNUM = 28  # Supported by down-level.
        WKSTA_SIZWORKBUF_PARMNUM = 29
        WKSTA_MAILSLOTS_PARMNUM = 30
        WKSTA_NUMDGRAMBUF_PARMNUM = 31
        WKSTA_WRKHEURISTICS_PARMNUM = 32  # Supported by down-level.
        WKSTA_MAXTHREADS_PARMNUM = 33
        WKSTA_LOCKQUOTA_PARMNUM = 41
        WKSTA_LOCKINCREMENT_PARMNUM = 42
        WKSTA_LOCKMAXIMUM_PARMNUM = 43
        WKSTA_PIPEINCREMENT_PARMNUM = 44
        WKSTA_PIPEMAXIMUM_PARMNUM = 45
        WKSTA_DORMANTFILELIMIT_PARMNUM = 46
        WKSTA_CACHEFILETIMEOUT_PARMNUM = 47
        WKSTA_USEOPPORTUNISTICLOCKING_PARMNUM = 48
        WKSTA_USEUNLOCKBEHIND_PARMNUM = 49
        WKSTA_USECLOSEBEHIND_PARMNUM = 50
        WKSTA_BUFFERNAMEDPIPES_PARMNUM = 51
        WKSTA_USELOCKANDREADANDUNLOCK_PARMNUM = 52
        WKSTA_UTILIZENTCACHING_PARMNUM = 53
        WKSTA_USERAWREAD_PARMNUM = 54
        WKSTA_USERAWWRITE_PARMNUM = 55
        WKSTA_USEWRITERAWWITHDATA_PARMNUM = 56
        WKSTA_USEENCRYPTION_PARMNUM = 57
        WKSTA_BUFFILESWITHDENYWRITE_PARMNUM = 58
        WKSTA_BUFFERREADONLYFILES_PARMNUM = 59
        WKSTA_FORCECORECREATEMODE_PARMNUM = 60
        WKSTA_USE512BYTESMAXTRANSFER_PARMNUM = 61
        WKSTA_READAHEADTHRUPUT_PARMNUM = 62
        # One of these values indicates the parameter within an information
        # structure that is invalid when ERROR_INVALID_PARAMETER is
        # returned by
        # NetWkstaUserSetInfo.
        WKSTA_OTH_DOMAINS_PARMNUM = 101
        # One of these values indicates the parameter within an information
        # structure that is invalid when ERROR_INVALID_PARAMETER is
        # returned by
        # NetWkstaTransportAdd.
        TRANSPORT_QUALITYOFSERVICE_PARMNUM = 201
        TRANSPORT_NAME_PARMNUM = 202
        if _MSC_VER >= 1200:
            pass
        # END IF

        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF   _LMWKSTA_
