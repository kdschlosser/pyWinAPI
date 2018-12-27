import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMREPL_ = None


class _REPL_INFO_0(ctypes.Structure):
    pass


REPL_INFO_0 = _REPL_INFO_0
PREPL_INFO_0 = POINTER(_REPL_INFO_0)
LPREPL_INFO_0 = POINTER(_REPL_INFO_0)


class _REPL_INFO_1000(ctypes.Structure):
    pass


REPL_INFO_1000 = _REPL_INFO_1000
PREPL_INFO_1000 = POINTER(_REPL_INFO_1000)
LPREPL_INFO_1000 = POINTER(_REPL_INFO_1000)


class _REPL_INFO_1001(ctypes.Structure):
    pass


REPL_INFO_1001 = _REPL_INFO_1001
PREPL_INFO_1001 = POINTER(_REPL_INFO_1001)
LPREPL_INFO_1001 = POINTER(_REPL_INFO_1001)


class _REPL_INFO_1002(ctypes.Structure):
    pass


REPL_INFO_1002 = _REPL_INFO_1002
PREPL_INFO_1002 = POINTER(_REPL_INFO_1002)
LPREPL_INFO_1002 = POINTER(_REPL_INFO_1002)


class _REPL_INFO_1003(ctypes.Structure):
    pass


REPL_INFO_1003 = _REPL_INFO_1003
PREPL_INFO_1003 = POINTER(_REPL_INFO_1003)
LPREPL_INFO_1003 = POINTER(_REPL_INFO_1003)


class _REPL_EDIR_INFO_0(ctypes.Structure):
    pass


REPL_EDIR_INFO_0 = _REPL_EDIR_INFO_0
PREPL_EDIR_INFO_0 = POINTER(_REPL_EDIR_INFO_0)
LPREPL_EDIR_INFO_0 = POINTER(_REPL_EDIR_INFO_0)


class _REPL_EDIR_INFO_1(ctypes.Structure):
    pass


REPL_EDIR_INFO_1 = _REPL_EDIR_INFO_1
PREPL_EDIR_INFO_1 = POINTER(_REPL_EDIR_INFO_1)
LPREPL_EDIR_INFO_1 = POINTER(_REPL_EDIR_INFO_1)


class _REPL_EDIR_INFO_2(ctypes.Structure):
    pass


REPL_EDIR_INFO_2 = _REPL_EDIR_INFO_2
PREPL_EDIR_INFO_2 = POINTER(_REPL_EDIR_INFO_2)
LPREPL_EDIR_INFO_2 = POINTER(_REPL_EDIR_INFO_2)


class _REPL_EDIR_INFO_1000(ctypes.Structure):
    pass


REPL_EDIR_INFO_1000 = _REPL_EDIR_INFO_1000
PREPL_EDIR_INFO_1000 = POINTER(_REPL_EDIR_INFO_1000)
LPREPL_EDIR_INFO_1000 = POINTER(_REPL_EDIR_INFO_1000)


class _REPL_EDIR_INFO_1001(ctypes.Structure):
    pass


REPL_EDIR_INFO_1001 = _REPL_EDIR_INFO_1001
PREPL_EDIR_INFO_1001 = POINTER(_REPL_EDIR_INFO_1001)
LPREPL_EDIR_INFO_1001 = POINTER(_REPL_EDIR_INFO_1001)


class _REPL_IDIR_INFO_0(ctypes.Structure):
    pass


REPL_IDIR_INFO_0 = _REPL_IDIR_INFO_0
PREPL_IDIR_INFO_0 = POINTER(_REPL_IDIR_INFO_0)
LPREPL_IDIR_INFO_0 = POINTER(_REPL_IDIR_INFO_0)


class _REPL_IDIR_INFO_1(ctypes.Structure):
    pass


REPL_IDIR_INFO_1 = _REPL_IDIR_INFO_1
PREPL_IDIR_INFO_1 = POINTER(_REPL_IDIR_INFO_1)
LPREPL_IDIR_INFO_1 = POINTER(_REPL_IDIR_INFO_1)


# /* + + BUILD Version: 0004 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: LmRepl.h
# Abstract: This file contains structures, function prototypes, and
# definitions for the replicator APIs. Environment: User Mode - Win32 Portable
# to any flat, 32-bit environment. (Uses Win32 typedefs.) Requires ANSI C
# extensions: slash-slash comments, LONG external names. Notes: You must
# include LmCons.h before this file. --
if not defined(_LMREPL_):
    _LMREPL_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.shared.lmcons_h import *  # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

        if defined(__cplusplus):
            pass
        # END IF


        # SAL Annotations not available for obsolete APIs
        # Replicator Configuration APIs
        REPL_ROLE_EXPORT = 1
        REPL_ROLE_IMPORT = 2
        REPL_ROLE_BOTH = 3
        REPL_INTERVAL_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + 0
        REPL_PULSE_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + 1
        REPL_GUARDTIME_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + 2
        REPL_RANDOM_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + 3

        _REPL_INFO_0._fields_ = [
            ('rp0_role', DWORD),
            ('rp0_exportpath', LPWSTR),
            ('rp0_exportlist', LPWSTR),
            ('rp0_importpath', LPWSTR),
            ('rp0_importlist', LPWSTR),
            ('rp0_logonusername', LPWSTR),
            ('rp0_interval', DWORD),
            ('rp0_pulse', DWORD),
            ('rp0_guardtime', DWORD),
            ('rp0_random', DWORD),
        ]

        _REPL_INFO_1000._fields_ = [
            ('rp1000_interval', DWORD),
        ]

        _REPL_INFO_1001._fields_ = [
            ('rp1001_pulse', DWORD),
        ]

        _REPL_INFO_1002._fields_ = [
            ('rp1002_guardtime', DWORD),
        ]

        _REPL_INFO_1003._fields_ = [
            ('rp1003_random', DWORD),
        ]
        netapi32 = ctypes.windll.NETAPI32

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplGetInfo(
        # IN LPCWSTR servername OPTIONAL,
        # IN DWORD level,
        # OUT LPBYTE * bufptr
        # );
        NetReplGetInfo = netapi32.NetReplGetInfo
        NetReplGetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplSetInfo(
        # IN LPCWSTR servername OPTIONAL,
        # IN DWORD level,
        # IN LPBYTE buf,
        # OUT LPDWORD parm_err OPTIONAL
        # );
        NetReplSetInfo = netapi32.NetReplSetInfo
        NetReplSetInfo.restype = NET_API_STATUS

        # Replicator Export Directory APIs
        REPL_INTEGRITY_FILE = 1
        REPL_INTEGRITY_TREE = 2
        REPL_EXTENT_FILE = 1
        REPL_EXTENT_TREE = 2
        REPL_EXPORT_INTEGRITY_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + 0
        REPL_EXPORT_EXTENT_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + 1

        _REPL_EDIR_INFO_0._fields_ = [
            ('rped0_dirname', LPWSTR),
        ]

        _REPL_EDIR_INFO_1._fields_ = [
            ('rped1_dirname', LPWSTR),
            ('rped1_integrity', DWORD),
            ('rped1_extent', DWORD),
        ]

        _REPL_EDIR_INFO_2._fields_ = [
            ('rped2_dirname', LPWSTR),
            ('rped2_integrity', DWORD),
            ('rped2_extent', DWORD),
            ('rped2_lockcount', DWORD),
            ('rped2_locktime', DWORD),
        ]

        _REPL_EDIR_INFO_1000._fields_ = [
            ('rped1000_integrity', DWORD),
        ]

        _REPL_EDIR_INFO_1001._fields_ = [
            ('rped1001_extent', DWORD),
        ]

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplExportDirAdd(
        # IN LPCWSTR servername OPTIONAL,
        # IN DWORD level,
        # IN LPBYTE buf,
        # OUT LPDWORD parm_err OPTIONAL
        # );
        NetReplExportDirAdd = netapi32.NetReplExportDirAdd
        NetReplExportDirAdd.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplExportDirDel(
        # IN LPCWSTR servername OPTIONAL,
        # IN LPCWSTR dirname
        # );
        NetReplExportDirDel = netapi32.NetReplExportDirDel
        NetReplExportDirDel.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplExportDirEnum(
        # IN LPCWSTR servername OPTIONAL,
        # IN DWORD level,
        # OUT LPBYTE * bufptr,
        # IN DWORD prefmaxlen,
        # OUT LPDWORD entriesread,
        # OUT LPDWORD totalentries,
        # IN OUT LPDWORD resumehandle OPTIONAL
        # );
        NetReplExportDirEnum = netapi32.NetReplExportDirEnum
        NetReplExportDirEnum.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplExportDirGetInfo(
        # IN LPCWSTR servername OPTIONAL,
        # IN LPCWSTR dirname,
        # IN DWORD level,
        # OUT LPBYTE * bufptr
        # );
        NetReplExportDirGetInfo = netapi32.NetReplExportDirGetInfo
        NetReplExportDirGetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplExportDirSetInfo(
        # IN LPCWSTR servername OPTIONAL,
        # IN LPCWSTR dirname,
        # IN DWORD level,
        # IN LPBYTE buf,
        # OUT LPDWORD parm_err OPTIONAL
        # );
        NetReplExportDirSetInfo = netapi32.NetReplExportDirSetInfo
        NetReplExportDirSetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplExportDirLock(
        # IN LPCWSTR servername OPTIONAL,
        # IN LPCWSTR dirname
        # );
        NetReplExportDirLock = netapi32.NetReplExportDirLock
        NetReplExportDirLock.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplExportDirUnlock(
        # IN LPCWSTR servername OPTIONAL,
        # IN LPCWSTR dirname,
        # IN DWORD unlockforce
        # );
        NetReplExportDirUnlock = netapi32.NetReplExportDirUnlock
        NetReplExportDirUnlock.restype = NET_API_STATUS

        REPL_UNLOCK_NOFORCE = 0
        REPL_UNLOCK_FORCE = 1

        # Replicator Import Directory APIs
        _REPL_IDIR_INFO_0._fields_ = [
            ('rpid0_dirname', LPWSTR),
        ]

        _REPL_IDIR_INFO_1._fields_ = [
            ('rpid1_dirname', LPWSTR),
            ('rpid1_state', DWORD),
            ('rpid1_mastername', LPWSTR),
            ('rpid1_last_update_time', DWORD),
            ('rpid1_lockcount', DWORD),
            ('rpid1_locktime', DWORD),
        ]

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplImportDirAdd(
        # IN LPCWSTR servername OPTIONAL,
        # IN DWORD level,
        # IN LPBYTE buf,
        # OUT LPDWORD parm_err OPTIONAL
        # );
        NetReplImportDirAdd = netapi32.NetReplImportDirAdd
        NetReplImportDirAdd.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplImportDirDel(
        # IN LPCWSTR servername OPTIONAL,
        # IN LPCWSTR dirname
        # );
        NetReplImportDirDel = netapi32.NetReplImportDirDel
        NetReplImportDirDel.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplImportDirEnum(
        # IN LPCWSTR servername OPTIONAL,
        # IN DWORD level,
        # OUT LPBYTE * bufptr,
        # IN DWORD prefmaxlen,
        # OUT LPDWORD entriesread,
        # OUT LPDWORD totalentries,
        # IN OUT LPDWORD resumehandle OPTIONAL
        # );
        NetReplImportDirEnum = netapi32.NetReplImportDirEnum
        NetReplImportDirEnum.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplImportDirGetInfo(
        # IN LPCWSTR servername OPTIONAL,
        # IN LPCWSTR dirname,
        # IN DWORD level,
        # OUT LPBYTE * bufptr
        # );
        NetReplImportDirGetInfo = netapi32.NetReplImportDirGetInfo
        NetReplImportDirGetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplImportDirLock(
        # IN LPCWSTR servername OPTIONAL,
        # IN LPCWSTR dirname
        # );
        NetReplImportDirLock = netapi32.NetReplImportDirLock
        NetReplImportDirLock.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetReplImportDirUnlock(
        # IN LPCWSTR servername OPTIONAL,
        # IN LPCWSTR dirname,
        # IN DWORD unlockforce
        # );
        NetReplImportDirUnlock = netapi32.NetReplImportDirUnlock
        NetReplImportDirUnlock.restype = NET_API_FUNCTION

        REPL_STATE_OK = 0
        REPL_STATE_NO_MASTER = 1
        REPL_STATE_NO_SYNC = 2
        REPL_STATE_NEVER_REPLICATED = 3
        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF  _LMREPL_


