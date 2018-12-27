import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMSVC_ = None

class _SERVICE_INFO_0(ctypes.Structure):
    pass


SERVICE_INFO_0 = _SERVICE_INFO_0
PSERVICE_INFO_0 = POINTER(_SERVICE_INFO_0)
LPSERVICE_INFO_0 = POINTER(_SERVICE_INFO_0)


class _SERVICE_INFO_1(ctypes.Structure):
    pass


SERVICE_INFO_1 = _SERVICE_INFO_1
PSERVICE_INFO_1 = POINTER(_SERVICE_INFO_1)
LPSERVICE_INFO_1 = POINTER(_SERVICE_INFO_1)


class _SERVICE_INFO_2(ctypes.Structure):
    pass


SERVICE_INFO_2 = _SERVICE_INFO_2
PSERVICE_INFO_2 = POINTER(_SERVICE_INFO_2)
LPSERVICE_INFO_2 = POINTER(_SERVICE_INFO_2)


# /* + + BUILD Version: 0002 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmsvc.h Abstract:
# This file contains structures, function prototypes, and definitions for the
# NetService API. [Environment:] User Mode -Win32 [Notes:] You must include
# NETCONS.H before this file, since this file depends on values defined in
# NETCONS.H. --

if not defined(_LMSVC_):
    _LMSVC_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    netapi32 = ctypes.windll.NETAPI32

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if defined(__cplusplus):
            pass
        # END IF

        # Include the file which contains all the service name strings.
        from pyWinAPI.um.lmsname_h import * # NOQA
        from pyWinAPI.shared.lmcons_h import * # NOQA

        # Data Structures
        _SERVICE_INFO_0._fields_ = [
            ('svci0_name', LPWSTR),
        ]

        _SERVICE_INFO_1._fields_ = [
            ('svci1_name', LPWSTR),
            ('svci1_status', DWORD),
            ('svci1_code', DWORD),
            ('svci1_pid', DWORD),
        ]

        _SERVICE_INFO_2._fields_ = [
            ('svci2_name', LPWSTR),
            ('svci2_status', DWORD),
            ('svci2_code', DWORD),
            ('svci2_pid', DWORD),
            ('svci2_text', LPWSTR),
            ('svci2_specific_error', DWORD),
            ('svci2_display_name', LPWSTR),
        ]

        # Function Prototypes

        # NET_API_STATUS NET_API_FUNCTION
        # NetServiceControl(
        # _In_opt_    LPCWSTR servername,
        # _In_        LPCWSTR service,
        # _In_        DWORD   opcode,
        # _In_        DWORD   arg,
        # _Outptr_ LPBYTE *bufptr
        # );
        NetServiceControl = netapi32.NetServiceControl
        NetServiceControl.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetServiceEnum(
        # _In_opt_    LPCWSTR  servername,
        # _In_        DWORD    level,
        # _Outptr_result_buffer_(_Inexpressible_(entriesread)) LPBYTE  *bufptr,
        # _In_        DWORD    prefmaxlen,
        # _Out_       LPDWORD  entriesread,
        # _Out_       LPDWORD  totalentries,
        # _Inout_opt_ LPDWORD  resume_handle
        # );
        NetServiceEnum = netapi32.NetServiceEnum
        NetServiceEnum.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetServiceGetInfo(
        # _In_opt_    LPCWSTR  servername,
        # _In_        LPCWSTR  service,
        # _In_        DWORD    level,
        # _Outptr_ LPBYTE  *bufptr
        # );
        NetServiceGetInfo = netapi32.NetServiceGetInfo
        NetServiceGetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetServiceInstall(
        # _In_opt_          LPCWSTR  servername,
        # _In_              LPCWSTR  service,
        # _In_              DWORD    argc,
        # _In_reads_(argc) LPCWSTR  argv[],
        # _Outptr_       LPBYTE  *bufptr
        # );
        NetServiceInstall = netapi32.NetServiceInstall
        NetServiceInstall.restype = NET_API_STATUS

        # Special Values and Constants
        # Bitmask and bit values for svci1_status, and svci2_status
        # fields. For each "subfield", there is a mask defined,
        # and a number of constants representing the value
        # obtained by doing (status & mask).
        # Bits 0,1 -- general status

        SERVICE_INSTALL_STATE = 0x03
        SERVICE_UNINSTALLED = 0x00
        SERVICE_INSTALL_PENDING = 0x01
        SERVICE_UNINSTALL_PENDING = 0x02
        SERVICE_INSTALLED = 0x03

        # Bits 2,3 -- paused/active status
        SERVICE_PAUSE_STATE = 0x0C
        LM20_SERVICE_ACTIVE = 0x00
        LM20_SERVICE_CONTINUE_PENDING = 0x04
        LM20_SERVICE_PAUSE_PENDING = 0x08
        LM20_SERVICE_PAUSED = 0x0C

        # Bit 4 -- uninstallable indication
        SERVICE_NOT_UNINSTALLABLE = 0x00
        SERVICE_UNINSTALLABLE = 0x10

        # Bit 5 -- pausable indication
        SERVICE_NOT_PAUSABLE = 0x00
        SERVICE_PAUSABLE = 0x20

        # Workstation service only:
        # Bits 8,9,10 -- redirection paused/active
        SERVICE_REDIR_PAUSED = 0x700
        SERVICE_REDIR_DISK_PAUSED = 0x100
        SERVICE_REDIR_PRINT_PAUSED = 0x200
        SERVICE_REDIR_COMM_PAUSED = 0x400

        # Additional standard LAN Manager for MS-DOS services
        SERVICE_DOS_ENCRYPTION = "ENCRYPT"

        # NetServiceControl opcodes.
        SERVICE_CTRL_INTERROGATE = 0
        SERVICE_CTRL_PAUSE = 1
        SERVICE_CTRL_CONTINUE = 2
        SERVICE_CTRL_UNINSTALL = 3

        # Workstation service only: Bits used in the "arg" parameter
        # to NetServiceControl in conjunction with the opcode
        # SERVICE_CTRL_PAUSE or SERVICE_CTRL_CONTINUE, to pause or
        # continue redirection.
        SERVICE_CTRL_REDIR_DISK = 0x1
        SERVICE_CTRL_REDIR_PRINT = 0x2
        SERVICE_CTRL_REDIR_COMM = 0x4

        # Values for svci1_code, and svci2_code when status
        # of the service is SERVICE_INSTALL_PENDING or
        # SERVICE_UNINSTALL_PENDING.
        # A service can optionally provide a hint to the installer
        # that the install is proceeding and how LONG to wait
        # (in 0.1 second increments) before querying status again.
        SERVICE_IP_NO_HINT = 0x0
        SERVICE_CCP_NO_HINT = 0x0
        SERVICE_IP_QUERY_HINT = 0x10000
        SERVICE_CCP_QUERY_HINT = 0x10000

        # Mask for install proceeding checkpoint number
        SERVICE_IP_CHKPT_NUM = 0x0FF
        SERVICE_CCP_CHKPT_NUM = 0x0FF

        # Mask for wait time hint before querying again
        SERVICE_IP_WAIT_TIME = 0x0FF00
        SERVICE_CCP_WAIT_TIME = 0x0FF00

        # Shift count for building wait time _code values
        SERVICE_IP_WAITTIME_SHIFT = 8
        SERVICE_NTIP_WAITTIME_SHIFT = 12

        # Mask used for upper and lower portions of wait hint time.
        UPPER_HINT_MASK = 0x0000FF00
        LOWER_HINT_MASK = 0x000000FF
        UPPER_GET_HINT_MASK = 0x0FF00000
        LOWER_GET_HINT_MASK = 0x0000FF00
        SERVICE_NT_MAXTIME = 0x0000FFFF
        SERVICE_RESRV_MASK = 0x0001FFFF
        SERVICE_MAXTIME = 0x000000FF

        # SERVICE_BASE is the base of service error codes,
        # chosen to avoid conflict with OS, redirector,
        # netapi, and errlog codes.
        # Don't change the comments following the manifest constants without
        # understanding how mapmsg works.
        SERVICE_BASE = 3050
        SERVICE_UIC_NORMAL = 0

        # /* Uninstall codes, to be used in high byte of 'code' on final
        # NetStatus, which sets the status to UNINSTALLED.
        SERVICE_UIC_BADPARMVAL = SERVICE_BASE + 1

        # /* The Registry or the information you just typed includes an
        # illegal value for "%1".
        SERVICE_UIC_MISSPARM = SERVICE_BASE + 2

        # /* The required parameter was not provided on the command line or in
        # the configuration file.
        SERVICE_UIC_UNKPARM = SERVICE_BASE + 3

        # /* LAN Manager does not recognize "%1" as a valid option.
        SERVICE_UIC_RESOURCE = SERVICE_BASE + 4

        # /* A request for resource could not be satisfied.
        SERVICE_UIC_CONFIG = SERVICE_BASE + 5

        # /* A problem exists with the system configuration.
        SERVICE_UIC_SYSTEM = SERVICE_BASE + 6

        # /* A system error has occurred.
        SERVICE_UIC_INTERNAL = SERVICE_BASE + 7

        # /* An internal consistency error has occurred.
        SERVICE_UIC_AMBIGPARM = SERVICE_BASE + 8

        # /* The configuration file or the command line has an ambiguous
        # option.
        SERVICE_UIC_DUPPARM = SERVICE_BASE + 9

        # /* The configuration file or the command line has a duplicate
        # parameter.
        SERVICE_UIC_KILL = SERVICE_BASE + 10

        # /* The service did not respond to control and was stopped with the
        # DosKillProc function.
        SERVICE_UIC_EXEC = SERVICE_BASE + 11

        # /* An error occurred when attempting to run the service program.
        SERVICE_UIC_SUBSERV = SERVICE_BASE + 12

        # /* The sub-service failed to start.
        SERVICE_UIC_CONFLPARM = SERVICE_BASE + 13

        # /* There is a conflict in the value or use of these options: %1.
        SERVICE_UIC_FILE = SERVICE_BASE + 14

        # /* There is a problem with the file.
        # The modifiers
        # General:
        SERVICE_UIC_M_NULL = 0

        # RESOURCE:
        SERVICE_UIC_M_MEMORY = SERVICE_BASE + 20        # memory
        SERVICE_UIC_M_DISK = SERVICE_BASE + 21        # disk space
        SERVICE_UIC_M_THREADS = SERVICE_BASE + 22        # thread
        SERVICE_UIC_M_PROCESSES = SERVICE_BASE + 23        # process

        # CONFIG:
        # Security failure
        SERVICE_UIC_M_SECURITY = SERVICE_BASE + 24

        # Security Failure. %0
        SERVICE_UIC_M_LANROOT = SERVICE_BASE + 25

        # /* Bad or missing LAN Manager root directory.
        SERVICE_UIC_M_REDIR = SERVICE_BASE + 26

        # /* The network software is not installed.
        SERVICE_UIC_M_SERVER = SERVICE_BASE + 27

        # /* The server is not started.
        SERVICE_UIC_M_SEC_FILE_ERR = SERVICE_BASE + 28

        # /* The server cannot access the user accounts database (NET.ACC).
        SERVICE_UIC_M_FILES = SERVICE_BASE + 29

        # /* Incompatible files are installed in the LANMAN tree.
        SERVICE_UIC_M_LOGS = SERVICE_BASE + 30

        # /* The LANMAN\LOGS directory is invalid.
        SERVICE_UIC_M_LANGROUP = SERVICE_BASE + 31

        # /* The domain specified could not be used.
        SERVICE_UIC_M_MSGNAME = SERVICE_BASE + 32

        # /* The computer name is being used as a message alias on another
        # computer.
        SERVICE_UIC_M_ANNOUNCE = SERVICE_BASE + 33

        # /* The announcement of the server name failed.
        SERVICE_UIC_M_UAS = SERVICE_BASE + 34

        # /* The user accounts database is not configured correctly.
        SERVICE_UIC_M_SERVER_SEC_ERR = SERVICE_BASE + 35

        # /* The server is not running with user-level security.
        SERVICE_UIC_M_WKSTA = SERVICE_BASE + 37

        # /* The workstation is not configured properly.
        SERVICE_UIC_M_ERRLOG = SERVICE_BASE + 38

        # /* View your error log for details.
        SERVICE_UIC_M_FILE_UW = SERVICE_BASE + 39

        # /* Unable to write to this file.
        SERVICE_UIC_M_ADDPAK = SERVICE_BASE + 40

        # /* ADDPAK file is corrupted. Delete LANMAN\NETPROG\ADDPAK.SER and
        # reapply all ADDPAKs.
        SERVICE_UIC_M_LAZY = SERVICE_BASE + 41

        # /* The LM386 server cannot be started because CACHE.EXE is not
        # running.
        SERVICE_UIC_M_UAS_MACHINE_ACCT = SERVICE_BASE + 42

        # /* There is no account for this computer in the security database.
        SERVICE_UIC_M_UAS_SERVERS_NMEMB = SERVICE_BASE + 43

        # /* This computer is not a member of the group SERVERS.
        SERVICE_UIC_M_UAS_SERVERS_NOGRP = SERVICE_BASE + 44

        # /* The group SERVERS is not present in the local security database.
        SERVICE_UIC_M_UAS_INVALID_ROLE = SERVICE_BASE + 45

        # /* This computer is configured as a member of a workgroup, not as a
        # member of a domain. The Netlogon service does not need to run in
        # this configuration.
        SERVICE_UIC_M_NETLOGON_NO_DC = SERVICE_BASE + 46

        # /* The primary Domain Controller for this domain could not be
        # located.
        SERVICE_UIC_M_NETLOGON_DC_CFLCT = SERVICE_BASE + 47

        # /* This computer is configured to be the primary domain controller
        # of its domain. However, the computer %1 is currently claiming to be
        # the primary domain controller of the domain.
        SERVICE_UIC_M_NETLOGON_AUTH = SERVICE_BASE + 48

        # /* The service failed to authenticate with the primary domain
        # controller.
        SERVICE_UIC_M_UAS_PROLOG = SERVICE_BASE + 49

        # /* There is a problem with the security database creation date or
        # serial number.
        SERVICE2_BASE = 5600

        # new SEVICE_UIC messages go here
        SERVICE_UIC_M_NETLOGON_MPATH = SERVICE2_BASE + 0

        # /* Could not share the User or Script path.
        SERVICE_UIC_M_LSA_MACHINE_ACCT = SERVICE2_BASE + 1

        # /* The password for this computer is not found in the local security
        # database.
        SERVICE_UIC_M_DATABASE_ERROR = SERVICE2_BASE + 2

        # /* An internal error occurred while accessing the computer's local
        # or network security database.
        # End modifiers
        # Commonly used Macros:
        def SERVICE_IP_CODE(tt, nn):
            return (
                SERVICE_IP_QUERY_HINT |
                (nn | (tt << SERVICE_IP_WAITTIME_SHIFT))
            )


        def SERVICE_CCP_CODE(tt, nn):
            return (
               SERVICE_CCP_QUERY_HINT |
               (nn | (tt << SERVICE_IP_WAITTIME_SHIFT))
            )


        def SERVICE_UIC_CODE(cc, mm):
            return (cc << 16) | mm


        # This macro takes a wait hint (tt) which can have a maximum value of
        # 0xFFFF and puts it into the service status code field.
        # 0x0FF1FFnn (where nn is the checkpoint information).
        def SERVICE_NT_CCP_CODE(tt, nn):
            return (
                SERVICE_CCP_QUERY_HINT |
                nn |
                ((tt & LOWER_HINT_MASK) << SERVICE_IP_WAITTIME_SHIFT) |
                ((tt & UPPER_HINT_MASK) << SERVICE_NTIP_WAITTIME_SHIFT)
            )


        # This macro takes a status code field, and strips out the wait hint
        # from the upper and lower sections.
        # 0x0FF1FFnn results in 0x0000FFFF.
        def SERVICE_NT_WAIT_GET(code):
            return (
              ((code & UPPER_GET_HINT_MASK) >> SERVICE_NTIP_WAITTIME_SHIFT) |
              ((code & LOWER_GET_HINT_MASK) >> SERVICE_IP_WAITTIME_SHIFT)
            )


        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   _LMSVC_


