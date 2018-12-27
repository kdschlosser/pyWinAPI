import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMAUDIT_ = None
_LMHLOGDEFINED_ = None

class _HLOG(ctypes.Structure):
    pass


HLOG = _HLOG
PHLOG = POINTER(_HLOG)
LPHLOG = POINTER(_HLOG)


class _AUDIT_ENTRY(ctypes.Structure):
    pass


AUDIT_ENTRY = _AUDIT_ENTRY
PAUDIT_ENTRY = POINTER(_AUDIT_ENTRY)
LPAUDIT_ENTRY = POINTER(_AUDIT_ENTRY)


class _AE_SRVSTATUS(ctypes.Structure):
    pass


AE_SRVSTATUS = _AE_SRVSTATUS
PAE_SRVSTATUS = POINTER(_AE_SRVSTATUS)
LPAE_SRVSTATUS = POINTER(_AE_SRVSTATUS)


class _AE_SESSLOGON(ctypes.Structure):
    pass


AE_SESSLOGON = _AE_SESSLOGON
PAE_SESSLOGON = POINTER(_AE_SESSLOGON)
LPAE_SESSLOGON = POINTER(_AE_SESSLOGON)


class _AE_SESSLOGOFF(ctypes.Structure):
    pass


AE_SESSLOGOFF = _AE_SESSLOGOFF
PAE_SESSLOGOFF = POINTER(_AE_SESSLOGOFF)
LPAE_SESSLOGOFF = POINTER(_AE_SESSLOGOFF)


class _AE_SESSPWERR(ctypes.Structure):
    pass


AE_SESSPWERR = _AE_SESSPWERR
PAE_SESSPWERR = POINTER(_AE_SESSPWERR)
LPAE_SESSPWERR = POINTER(_AE_SESSPWERR)


class _AE_CONNSTART(ctypes.Structure):
    pass


AE_CONNSTART = _AE_CONNSTART
PAE_CONNSTART = POINTER(_AE_CONNSTART)
LPAE_CONNSTART = POINTER(_AE_CONNSTART)


class _AE_CONNSTOP(ctypes.Structure):
    pass


AE_CONNSTOP = _AE_CONNSTOP
PAE_CONNSTOP = POINTER(_AE_CONNSTOP)
LPAE_CONNSTOP = POINTER(_AE_CONNSTOP)


class _AE_CONNREJ(ctypes.Structure):
    pass


AE_CONNREJ = _AE_CONNREJ
PAE_CONNREJ = POINTER(_AE_CONNREJ)
LPAE_CONNREJ = POINTER(_AE_CONNREJ)


class _AE_RESACCESS(ctypes.Structure):
    pass


AE_RESACCESS = _AE_RESACCESS
PAE_RESACCESS = POINTER(_AE_RESACCESS)
LPAE_RESACCESS = POINTER(_AE_RESACCESS)


class _AE_RESACCESSREJ(ctypes.Structure):
    pass


AE_RESACCESSREJ = _AE_RESACCESSREJ
PAE_RESACCESSREJ = POINTER(_AE_RESACCESSREJ)
LPAE_RESACCESSREJ = POINTER(_AE_RESACCESSREJ)


class _AE_CLOSEFILE(ctypes.Structure):
    pass


AE_CLOSEFILE = _AE_CLOSEFILE
PAE_CLOSEFILE = POINTER(_AE_CLOSEFILE)
LPAE_CLOSEFILE = POINTER(_AE_CLOSEFILE)


class _AE_SERVICESTAT(ctypes.Structure):
    pass


AE_SERVICESTAT = _AE_SERVICESTAT
PAE_SERVICESTAT = POINTER(_AE_SERVICESTAT)
LPAE_SERVICESTAT = POINTER(_AE_SERVICESTAT)


class _AE_ACLMOD(ctypes.Structure):
    pass


AE_ACLMOD = _AE_ACLMOD
PAE_ACLMOD = POINTER(_AE_ACLMOD)
LPAE_ACLMOD = POINTER(_AE_ACLMOD)


class _AE_UASMOD(ctypes.Structure):
    pass


AE_UASMOD = _AE_UASMOD
PAE_UASMOD = POINTER(_AE_UASMOD)
LPAE_UASMOD = POINTER(_AE_UASMOD)


class _AE_NETLOGON(ctypes.Structure):
    pass


AE_NETLOGON = _AE_NETLOGON
PAE_NETLOGON = POINTER(_AE_NETLOGON)
LPAE_NETLOGON = POINTER(_AE_NETLOGON)


class _AE_NETLOGOFF(ctypes.Structure):
    pass


AE_NETLOGOFF = _AE_NETLOGOFF
PAE_NETLOGOFF = POINTER(_AE_NETLOGOFF)
LPAE_NETLOGOFF = POINTER(_AE_NETLOGOFF)


class _AE_ACCLIM(ctypes.Structure):
    pass


AE_ACCLIM = _AE_ACCLIM
PAE_ACCLIM = POINTER(_AE_ACCLIM)
LPAE_ACCLIM = POINTER(_AE_ACCLIM)


class _AE_LOCKOUT(ctypes.Structure):
    pass


AE_LOCKOUT = _AE_LOCKOUT
PAE_LOCKOUT = POINTER(_AE_LOCKOUT)
LPAE_LOCKOUT = POINTER(_AE_LOCKOUT)


class _AE_GENERIC(ctypes.Structure):
    pass


AE_GENERIC = _AE_GENERIC
PAE_GENERIC = POINTER(_AE_GENERIC)
LPAE_GENERIC = POINTER(_AE_GENERIC)

# /* + + BUILD Version: 0003 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmaudit.h
# Abstract: This module defines the API function prototypes and data
# structures for the following groups of NT API functions: NetAudit
# Environment: User Mode - Win32 Notes: You must include NETCONS.H before this
# file, since this file depends on values defined in NETCONS.H. --
if not defined(_LMAUDIT_):
    _LMAUDIT_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.shared.lmcons_h import *  # NOQA


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if defined(__cplusplus):
            pass
        # END IF

        if not defined(_LMHLOGDEFINED_):
            _LMHLOGDEFINED_ = VOID


            _HLOG._fields_ = [
                ('time', DWORD),
                ('last_flags', DWORD),
                ('offset', DWORD),
                ('rec_offset', DWORD),
            ]
            LOGFLAGS_FORWARD = 0
            LOGFLAGS_BACKWARD = 0x1
            LOGFLAGS_SEEK = 0x2
        # END IF


        # Function Prototypes - Audit
        # SAL Annotations not available for obsolete APIs
        netapi32 = ctypes.windll.NETAPI32


        # NET_API_STATUS NET_API_FUNCTION
        # NetAuditClear(
        # IN  LPCWSTR  server OPTIONAL,
        # IN  LPCWSTR  backupfile OPTIONAL,
        # IN  LPCWSTR  service OPTIONAL // WARNING: buggy support before LM 2.0Cnot not
        # );
        NetAuditClear = netapi32.NetAuditClear
        NetAuditClear.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetAuditRead(
        # IN  LPCWSTR  server OPTIONAL,
        # IN  LPCWSTR  service OPTIONAL, // WARNING: buggy support before LM 2.0Cnot not
        # IN  LPHLOG   auditloghandle,
        # IN  DWORD    offset,
        # IN  LPDWORD  reserved1 OPTIONAL,
        # IN  DWORD   reserved2,
        # IN  DWORD   offsetflag,
        # OUT LPBYTE  *bufptr,
        # IN  DWORD   prefmaxlen,
        # OUT LPDWORD bytesread,
        # OUT LPDWORD totalavailable
        # );
        NetAuditRead = netapi32.NetAuditRead
        NetAuditRead.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetAuditWrite(
        # IN  DWORD    type,
        # IN  LPBYTE   buf,
        # IN  DWORD    numbytes,
        # IN  LPCWSTR  service OPTIONAL,
        # IN  LPBYTE   reserved OPTIONAL
        # );
        NetAuditWrite = netapi32.NetAuditWrite
        NetAuditWrite.restype = NET_API_STATUS

        # Data Structures - Audit
        _AUDIT_ENTRY._fields_ = [
            ('ae_len', DWORD),
            ('ae_reserved', DWORD),
            ('ae_time', DWORD),
            ('ae_type', DWORD),
            # byte count of ae_data area (not incl pad).
            ('ae_data_size', DWORD),
        ]
        REVISED_AUDIT_ENTRY_STRUCT = VOID


        _AE_SRVSTATUS._fields_ = [
            ('ae_sv_status', DWORD),
        ]

        _AE_SESSLOGON._fields_ = [
            ('ae_so_compname', DWORD),
            ('ae_so_username', DWORD),
            ('ae_so_privilege', DWORD),
        ]

        _AE_SESSLOGOFF._fields_ = [
            ('ae_sf_compname', DWORD),
            ('ae_sf_username', DWORD),
            ('ae_sf_reason', DWORD),
        ]

        _AE_SESSPWERR._fields_ = [
            ('ae_sp_compname', DWORD),
            ('ae_sp_username', DWORD),
        ]

        _AE_CONNSTART._fields_ = [
            ('ae_ct_compname', DWORD),
            ('ae_ct_username', DWORD),
            ('ae_ct_netname', DWORD),
            ('ae_ct_connid', DWORD),
        ]

        _AE_CONNSTOP._fields_ = [
            ('ae_cp_compname', DWORD),
            ('ae_cp_username', DWORD),
            ('ae_cp_netname', DWORD),
            ('ae_cp_connid', DWORD),
            ('ae_cp_reason', DWORD),
        ]

        _AE_CONNREJ._fields_ = [
            ('ae_cr_compname', DWORD),
            ('ae_cr_username', DWORD),
            ('ae_cr_netname', DWORD),
            ('ae_cr_reason', DWORD),
        ]

        _AE_RESACCESS._fields_ = [
            ('ae_ra_compname', DWORD),
            ('ae_ra_username', DWORD),
            ('ae_ra_resname', DWORD),
            ('ae_ra_operation', DWORD),
            ('ae_ra_returncode', DWORD),
            ('ae_ra_restype', DWORD),
            ('ae_ra_fileid', DWORD),
        ]

        _AE_RESACCESSREJ._fields_ = [
            ('ae_rr_compname', DWORD),
            ('ae_rr_username', DWORD),
            ('ae_rr_resname', DWORD),
            ('ae_rr_operation', DWORD),
        ]

        _AE_CLOSEFILE._fields_ = [
            ('ae_cf_compname', DWORD),
            ('ae_cf_username', DWORD),
            ('ae_cf_resname', DWORD),
            ('ae_cf_fileid', DWORD),
            ('ae_cf_duration', DWORD),
            ('ae_cf_reason', DWORD),
        ]

        _AE_SERVICESTAT._fields_ = [
            ('ae_ss_compname', DWORD),
            ('ae_ss_username', DWORD),
            ('ae_ss_svcname', DWORD),
            ('ae_ss_status', DWORD),
            ('ae_ss_code', DWORD),
            ('ae_ss_text', DWORD),
            ('ae_ss_returnval', DWORD),
        ]

        _AE_ACLMOD._fields_ = [
            ('ae_am_compname', DWORD),
            ('ae_am_username', DWORD),
            ('ae_am_resname', DWORD),
            ('ae_am_action', DWORD),
            ('ae_am_datalen', DWORD),
        ]

        _AE_UASMOD._fields_ = [
            ('ae_um_compname', DWORD),
            ('ae_um_username', DWORD),
            ('ae_um_resname', DWORD),
            ('ae_um_rectype', DWORD),
            ('ae_um_action', DWORD),
            ('ae_um_datalen', DWORD),
        ]

        _AE_NETLOGON._fields_ = [
            ('ae_no_compname', DWORD),
            ('ae_no_username', DWORD),
            ('ae_no_privilege', DWORD),
            ('ae_no_authflags', DWORD),
        ]

        _AE_NETLOGOFF._fields_ = [
            ('ae_nf_compname', DWORD),
            ('ae_nf_username', DWORD),
            ('ae_nf_reserved1', DWORD),
            ('ae_nf_reserved2', DWORD),
        ]

        _AE_ACCLIM._fields_ = [
            ('ae_al_compname', DWORD),
            ('ae_al_username', DWORD),
            ('ae_al_resname', DWORD),
            ('ae_al_limit', DWORD),
        ]
        ACTION_LOCKOUT = 00
        ACTION_ADMINUNLOCK = 01


        # Ptr to computername of client.
        _AE_LOCKOUT._fields_ = [
            ('ae_lk_compname', DWORD),
            # Ptr to username of client (NULL
            ('ae_lk_username', DWORD),
            # Action taken on account:
            ('ae_lk_action', DWORD),
            # Bad password count at the time
            ('ae_lk_bad_pw_count', DWORD),
        ]
        _AE_GENERIC._fields_ = [
            ('ae_ge_msgfile', DWORD),
            ('ae_ge_msgnum', DWORD),
            ('ae_ge_params', DWORD),
            ('ae_ge_param1', DWORD),
            ('ae_ge_param2', DWORD),
            ('ae_ge_param3', DWORD),
            ('ae_ge_param4', DWORD),
            ('ae_ge_param5', DWORD),
            ('ae_ge_param6', DWORD),
            ('ae_ge_param7', DWORD),
            ('ae_ge_param8', DWORD),
            ('ae_ge_param9', DWORD),
        ]
        # Special Values and Constants - Audit
        # Audit entry types (field ae_type in audit_entry).
        AE_SRVSTATUS = 0
        AE_SESSLOGON = 1
        AE_SESSLOGOFF = 2
        AE_SESSPWERR = 3
        AE_CONNSTART = 4
        AE_CONNSTOP = 5
        AE_CONNREJ = 6
        AE_RESACCESS = 7
        AE_RESACCESSREJ = 8
        AE_CLOSEFILE = 9
        AE_SERVICESTAT = 11
        AE_ACLMOD = 12
        AE_UASMOD = 13
        AE_NETLOGON = 14
        AE_NETLOGOFF = 15
        AE_NETLOGDENIED = 16
        AE_ACCLIMITEXCD = 17
        AE_RESACCESS2 = 18
        AE_ACLMODFAIL = 19
        AE_LOCKOUT = 20
        AE_GENERIC_TYPE = 21
        # Values for ae_ss_status field of ae_srvstatus.
        AE_SRVSTART = 0
        AE_SRVPAUSED = 1
        AE_SRVCONT = 2
        AE_SRVSTOP = 3
        # Values for ae_so_privilege field of ae_sesslogon.
        AE_GUEST = 0
        AE_USER = 1
        AE_ADMIN = 2
        # Values for various ae_XX_reason fields.
        AE_NORMAL = 0
        AE_USERLIMIT = 0
        AE_GENERAL = 0
        AE_ERROR = 1
        AE_SESSDIS = 1
        AE_BADPW = 1
        AE_AUTODIS = 2
        AE_UNSHARE = 2
        AE_ADMINPRIVREQD = 2
        AE_ADMINDIS = 3
        AE_NOACCESSPERM = 3
        AE_ACCRESTRICT = 4
        AE_NORMAL_CLOSE = 0
        AE_SES_CLOSE = 1
        AE_ADMIN_CLOSE = 2
        # Values for xx_subreason fields.
        AE_LIM_UNKNOWN = 0
        AE_LIM_LOGONHOURS = 1
        AE_LIM_EXPIRED = 2
        AE_LIM_INVAL_WKSTA = 3
        AE_LIM_DISABLED = 4
        AE_LIM_DELETED = 5
        # Values for xx_action fields
        AE_MOD = 0
        AE_DELETE = 1
        AE_ADD = 2
        # Types of UAS record for um_rectype field
        AE_UAS_USER = 0
        AE_UAS_GROUP = 1
        AE_UAS_MODALS = 2
        # Bitmasks for auditing events
        # The parentheses around the hex constants broke h_to_inc
        # and have been purged from the face of the earth.
        SVAUD_SERVICE = 0x1
        SVAUD_GOODSESSLOGON = 0x6
        SVAUD_BADSESSLOGON = 0x18
        SVAUD_SESSLOGON = SVAUD_GOODSESSLOGON | SVAUD_BADSESSLOGON
        SVAUD_GOODNETLOGON = 0x60
        SVAUD_BADNETLOGON = 0x180
        SVAUD_NETLOGON = SVAUD_GOODNETLOGON | SVAUD_BADNETLOGON
        SVAUD_LOGON = SVAUD_NETLOGON | SVAUD_SESSLOGON
        SVAUD_GOODUSE = 0x600
        SVAUD_BADUSE = 0x1800
        SVAUD_USE = SVAUD_GOODUSE | SVAUD_BADUSE
        SVAUD_USERLIST = 0x2000
        SVAUD_PERMISSIONS = 0x4000
        SVAUD_RESOURCE = 0x8000
        SVAUD_LOGONLIM = 0x00010000
        # Resource access audit bitmasks.
        AA_AUDIT_ALL = 0x0001
        AA_A_OWNER = 0x0004
        AA_CLOSE = 0x0008
        AA_S_OPEN = 0x0010
        AA_S_WRITE = 0x0020
        AA_S_CREATE = 0x0020
        AA_S_DELETE = 0x0040
        AA_S_ACL = 0x0080
        AA_S_ALL = AA_S_OPEN | AA_S_WRITE | AA_S_DELETE | AA_S_ACL
        AA_F_OPEN = 0x0100
        AA_F_WRITE = 0x0200
        AA_F_CREATE = 0x0200
        AA_F_DELETE = 0x0400
        AA_F_ACL = 0x0800
        AA_F_ALL = AA_F_OPEN | AA_F_WRITE | AA_F_DELETE | AA_F_ACL
        # Pinball-specific
        AA_A_OPEN = 0x1000
        AA_A_WRITE = 0x2000
        AA_A_CREATE = 0x2000
        AA_A_DELETE = 0x4000
        AA_A_ACL = 0x8000
        AA_A_ALL = AA_F_OPEN | AA_F_WRITE | AA_F_DELETE | AA_F_ACL
        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   _LMAUDIT_


