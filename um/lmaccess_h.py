import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMUSER_ = None
_LMGROUP_ = None
_LMLOCALGROUP_ = None
_LMACCESS_ = None
_WINBASE_ = None
_LMDOMAIN_ = None
_NTDEF_ = None

class _USER_INFO_0(ctypes.Structure):
    pass


USER_INFO_0 = _USER_INFO_0
PUSER_INFO_0 = POINTER(_USER_INFO_0)
LPUSER_INFO_0 = POINTER(_USER_INFO_0)


class _USER_INFO_1(ctypes.Structure):
    pass


USER_INFO_1 = _USER_INFO_1
PUSER_INFO_1 = POINTER(_USER_INFO_1)
LPUSER_INFO_1 = POINTER(_USER_INFO_1)


class _USER_INFO_2(ctypes.Structure):
    pass


USER_INFO_2 = _USER_INFO_2
PUSER_INFO_2 = POINTER(_USER_INFO_2)
LPUSER_INFO_2 = POINTER(_USER_INFO_2)


class _USER_INFO_3(ctypes.Structure):
    pass


USER_INFO_3 = _USER_INFO_3
PUSER_INFO_3 = POINTER(_USER_INFO_3)
LPUSER_INFO_3 = POINTER(_USER_INFO_3)


class _USER_INFO_4(ctypes.Structure):
    pass


USER_INFO_4 = _USER_INFO_4
PUSER_INFO_4 = POINTER(_USER_INFO_4)
LPUSER_INFO_4 = POINTER(_USER_INFO_4)


class _USER_INFO_10(ctypes.Structure):
    pass


USER_INFO_10 = _USER_INFO_10
PUSER_INFO_10 = POINTER(_USER_INFO_10)
LPUSER_INFO_10 = POINTER(_USER_INFO_10)


class _USER_INFO_11(ctypes.Structure):
    pass


USER_INFO_11 = _USER_INFO_11
PUSER_INFO_11 = POINTER(_USER_INFO_11)
LPUSER_INFO_11 = POINTER(_USER_INFO_11)


class _USER_INFO_20(ctypes.Structure):
    pass


USER_INFO_20 = _USER_INFO_20
PUSER_INFO_20 = POINTER(_USER_INFO_20)
LPUSER_INFO_20 = POINTER(_USER_INFO_20)


class _USER_INFO_21(ctypes.Structure):
    pass


USER_INFO_21 = _USER_INFO_21
PUSER_INFO_21 = POINTER(_USER_INFO_21)
LPUSER_INFO_21 = POINTER(_USER_INFO_21)


class _USER_INFO_22(ctypes.Structure):
    pass


USER_INFO_22 = _USER_INFO_22
PUSER_INFO_22 = POINTER(_USER_INFO_22)
LPUSER_INFO_22 = POINTER(_USER_INFO_22)


class _USER_INFO_23(ctypes.Structure):
    pass


USER_INFO_23 = _USER_INFO_23
PUSER_INFO_23 = POINTER(_USER_INFO_23)
LPUSER_INFO_23 = POINTER(_USER_INFO_23)


class _USER_INFO_24(ctypes.Structure):
    pass


USER_INFO_24 = _USER_INFO_24
PUSER_INFO_24 = POINTER(_USER_INFO_24)
LPUSER_INFO_24 = POINTER(_USER_INFO_24)


class _USER_INFO_1003(ctypes.Structure):
    pass


USER_INFO_1003 = _USER_INFO_1003
PUSER_INFO_1003 = POINTER(_USER_INFO_1003)
LPUSER_INFO_1003 = POINTER(_USER_INFO_1003)


class _USER_INFO_1005(ctypes.Structure):
    pass


USER_INFO_1005 = _USER_INFO_1005
PUSER_INFO_1005 = POINTER(_USER_INFO_1005)
LPUSER_INFO_1005 = POINTER(_USER_INFO_1005)


class _USER_INFO_1006(ctypes.Structure):
    pass


USER_INFO_1006 = _USER_INFO_1006
PUSER_INFO_1006 = POINTER(_USER_INFO_1006)
LPUSER_INFO_1006 = POINTER(_USER_INFO_1006)


class _USER_INFO_1007(ctypes.Structure):
    pass


USER_INFO_1007 = _USER_INFO_1007
PUSER_INFO_1007 = POINTER(_USER_INFO_1007)
LPUSER_INFO_1007 = POINTER(_USER_INFO_1007)


class _USER_INFO_1008(ctypes.Structure):
    pass


USER_INFO_1008 = _USER_INFO_1008
PUSER_INFO_1008 = POINTER(_USER_INFO_1008)
LPUSER_INFO_1008 = POINTER(_USER_INFO_1008)


class _USER_INFO_1009(ctypes.Structure):
    pass


USER_INFO_1009 = _USER_INFO_1009
PUSER_INFO_1009 = POINTER(_USER_INFO_1009)
LPUSER_INFO_1009 = POINTER(_USER_INFO_1009)


class _USER_INFO_1010(ctypes.Structure):
    pass


USER_INFO_1010 = _USER_INFO_1010
PUSER_INFO_1010 = POINTER(_USER_INFO_1010)
LPUSER_INFO_1010 = POINTER(_USER_INFO_1010)


class _USER_INFO_1011(ctypes.Structure):
    pass


USER_INFO_1011 = _USER_INFO_1011
PUSER_INFO_1011 = POINTER(_USER_INFO_1011)
LPUSER_INFO_1011 = POINTER(_USER_INFO_1011)


class _USER_INFO_1012(ctypes.Structure):
    pass


USER_INFO_1012 = _USER_INFO_1012
PUSER_INFO_1012 = POINTER(_USER_INFO_1012)
LPUSER_INFO_1012 = POINTER(_USER_INFO_1012)


class _USER_INFO_1013(ctypes.Structure):
    pass


USER_INFO_1013 = _USER_INFO_1013
PUSER_INFO_1013 = POINTER(_USER_INFO_1013)
LPUSER_INFO_1013 = POINTER(_USER_INFO_1013)


class _USER_INFO_1014(ctypes.Structure):
    pass


USER_INFO_1014 = _USER_INFO_1014
PUSER_INFO_1014 = POINTER(_USER_INFO_1014)
LPUSER_INFO_1014 = POINTER(_USER_INFO_1014)


class _USER_INFO_1017(ctypes.Structure):
    pass


USER_INFO_1017 = _USER_INFO_1017
PUSER_INFO_1017 = POINTER(_USER_INFO_1017)
LPUSER_INFO_1017 = POINTER(_USER_INFO_1017)


class _USER_INFO_1018(ctypes.Structure):
    pass


USER_INFO_1018 = _USER_INFO_1018
PUSER_INFO_1018 = POINTER(_USER_INFO_1018)
LPUSER_INFO_1018 = POINTER(_USER_INFO_1018)


class _USER_INFO_1020(ctypes.Structure):
    pass


USER_INFO_1020 = _USER_INFO_1020
PUSER_INFO_1020 = POINTER(_USER_INFO_1020)
LPUSER_INFO_1020 = POINTER(_USER_INFO_1020)


class _USER_INFO_1023(ctypes.Structure):
    pass


USER_INFO_1023 = _USER_INFO_1023
PUSER_INFO_1023 = POINTER(_USER_INFO_1023)
LPUSER_INFO_1023 = POINTER(_USER_INFO_1023)


class _USER_INFO_1024(ctypes.Structure):
    pass


USER_INFO_1024 = _USER_INFO_1024
PUSER_INFO_1024 = POINTER(_USER_INFO_1024)
LPUSER_INFO_1024 = POINTER(_USER_INFO_1024)


class _USER_INFO_1025(ctypes.Structure):
    pass


USER_INFO_1025 = _USER_INFO_1025
PUSER_INFO_1025 = POINTER(_USER_INFO_1025)
LPUSER_INFO_1025 = POINTER(_USER_INFO_1025)


class _USER_INFO_1051(ctypes.Structure):
    pass


USER_INFO_1051 = _USER_INFO_1051
PUSER_INFO_1051 = POINTER(_USER_INFO_1051)
LPUSER_INFO_1051 = POINTER(_USER_INFO_1051)


class _USER_INFO_1052(ctypes.Structure):
    pass


USER_INFO_1052 = _USER_INFO_1052
PUSER_INFO_1052 = POINTER(_USER_INFO_1052)
LPUSER_INFO_1052 = POINTER(_USER_INFO_1052)


class _USER_INFO_1053(ctypes.Structure):
    pass


USER_INFO_1053 = _USER_INFO_1053
PUSER_INFO_1053 = POINTER(_USER_INFO_1053)
LPUSER_INFO_1053 = POINTER(_USER_INFO_1053)


class _USER_MODALS_INFO_0(ctypes.Structure):
    pass


USER_MODALS_INFO_0 = _USER_MODALS_INFO_0
PUSER_MODALS_INFO_0 = POINTER(_USER_MODALS_INFO_0)
LPUSER_MODALS_INFO_0 = POINTER(_USER_MODALS_INFO_0)


class _USER_MODALS_INFO_1(ctypes.Structure):
    pass


USER_MODALS_INFO_1 = _USER_MODALS_INFO_1
PUSER_MODALS_INFO_1 = POINTER(_USER_MODALS_INFO_1)
LPUSER_MODALS_INFO_1 = POINTER(_USER_MODALS_INFO_1)


class _USER_MODALS_INFO_2(ctypes.Structure):
    pass


USER_MODALS_INFO_2 = _USER_MODALS_INFO_2
PUSER_MODALS_INFO_2 = POINTER(_USER_MODALS_INFO_2)
LPUSER_MODALS_INFO_2 = POINTER(_USER_MODALS_INFO_2)


class _USER_MODALS_INFO_3(ctypes.Structure):
    pass


USER_MODALS_INFO_3 = _USER_MODALS_INFO_3
PUSER_MODALS_INFO_3 = POINTER(_USER_MODALS_INFO_3)
LPUSER_MODALS_INFO_3 = POINTER(_USER_MODALS_INFO_3)


class _USER_MODALS_INFO_1001(ctypes.Structure):
    pass


USER_MODALS_INFO_1001 = _USER_MODALS_INFO_1001
PUSER_MODALS_INFO_1001 = POINTER(_USER_MODALS_INFO_1001)
LPUSER_MODALS_INFO_1001 = POINTER(_USER_MODALS_INFO_1001)


class _USER_MODALS_INFO_1002(ctypes.Structure):
    pass


USER_MODALS_INFO_1002 = _USER_MODALS_INFO_1002
PUSER_MODALS_INFO_1002 = POINTER(_USER_MODALS_INFO_1002)
LPUSER_MODALS_INFO_1002 = POINTER(_USER_MODALS_INFO_1002)


class _USER_MODALS_INFO_1003(ctypes.Structure):
    pass


USER_MODALS_INFO_1003 = _USER_MODALS_INFO_1003
PUSER_MODALS_INFO_1003 = POINTER(_USER_MODALS_INFO_1003)
LPUSER_MODALS_INFO_1003 = POINTER(_USER_MODALS_INFO_1003)


class _USER_MODALS_INFO_1004(ctypes.Structure):
    pass


USER_MODALS_INFO_1004 = _USER_MODALS_INFO_1004
PUSER_MODALS_INFO_1004 = POINTER(_USER_MODALS_INFO_1004)
LPUSER_MODALS_INFO_1004 = POINTER(_USER_MODALS_INFO_1004)


class _USER_MODALS_INFO_1005(ctypes.Structure):
    pass


USER_MODALS_INFO_1005 = _USER_MODALS_INFO_1005
PUSER_MODALS_INFO_1005 = POINTER(_USER_MODALS_INFO_1005)
LPUSER_MODALS_INFO_1005 = POINTER(_USER_MODALS_INFO_1005)


class _USER_MODALS_INFO_1006(ctypes.Structure):
    pass


USER_MODALS_INFO_1006 = _USER_MODALS_INFO_1006
PUSER_MODALS_INFO_1006 = POINTER(_USER_MODALS_INFO_1006)
LPUSER_MODALS_INFO_1006 = POINTER(_USER_MODALS_INFO_1006)


class _USER_MODALS_INFO_1007(ctypes.Structure):
    pass


USER_MODALS_INFO_1007 = _USER_MODALS_INFO_1007
PUSER_MODALS_INFO_1007 = POINTER(_USER_MODALS_INFO_1007)
LPUSER_MODALS_INFO_1007 = POINTER(_USER_MODALS_INFO_1007)


class _GROUP_INFO_0(ctypes.Structure):
    pass


GROUP_INFO_0 = _GROUP_INFO_0
PGROUP_INFO_0 = POINTER(_GROUP_INFO_0)
LPGROUP_INFO_0 = POINTER(_GROUP_INFO_0)


class _GROUP_INFO_1(ctypes.Structure):
    pass


GROUP_INFO_1 = _GROUP_INFO_1
PGROUP_INFO_1 = POINTER(_GROUP_INFO_1)
LPGROUP_INFO_1 = POINTER(_GROUP_INFO_1)


class _GROUP_INFO_2(ctypes.Structure):
    pass


GROUP_INFO_2 = _GROUP_INFO_2
PGROUP_INFO_2 = POINTER(_GROUP_INFO_2)


class _GROUP_INFO_3(ctypes.Structure):
    pass


GROUP_INFO_3 = _GROUP_INFO_3
PGROUP_INFO_3 = POINTER(_GROUP_INFO_3)


class _GROUP_INFO_1002(ctypes.Structure):
    pass


GROUP_INFO_1002 = _GROUP_INFO_1002
PGROUP_INFO_1002 = POINTER(_GROUP_INFO_1002)
LPGROUP_INFO_1002 = POINTER(_GROUP_INFO_1002)


class _GROUP_INFO_1005(ctypes.Structure):
    pass


GROUP_INFO_1005 = _GROUP_INFO_1005
PGROUP_INFO_1005 = POINTER(_GROUP_INFO_1005)
LPGROUP_INFO_1005 = POINTER(_GROUP_INFO_1005)


class _GROUP_USERS_INFO_0(ctypes.Structure):
    pass


GROUP_USERS_INFO_0 = _GROUP_USERS_INFO_0
PGROUP_USERS_INFO_0 = POINTER(_GROUP_USERS_INFO_0)
LPGROUP_USERS_INFO_0 = POINTER(_GROUP_USERS_INFO_0)


class _GROUP_USERS_INFO_1(ctypes.Structure):
    pass


GROUP_USERS_INFO_1 = _GROUP_USERS_INFO_1
PGROUP_USERS_INFO_1 = POINTER(_GROUP_USERS_INFO_1)
LPGROUP_USERS_INFO_1 = POINTER(_GROUP_USERS_INFO_1)


class _LOCALGROUP_INFO_0(ctypes.Structure):
    pass


LOCALGROUP_INFO_0 = _LOCALGROUP_INFO_0
PLOCALGROUP_INFO_0 = POINTER(_LOCALGROUP_INFO_0)
LPLOCALGROUP_INFO_0 = POINTER(_LOCALGROUP_INFO_0)


class _LOCALGROUP_INFO_1(ctypes.Structure):
    pass


LOCALGROUP_INFO_1 = _LOCALGROUP_INFO_1
PLOCALGROUP_INFO_1 = POINTER(_LOCALGROUP_INFO_1)
LPLOCALGROUP_INFO_1 = POINTER(_LOCALGROUP_INFO_1)


class _LOCALGROUP_INFO_1002(ctypes.Structure):
    pass


LOCALGROUP_INFO_1002 = _LOCALGROUP_INFO_1002
PLOCALGROUP_INFO_1002 = POINTER(_LOCALGROUP_INFO_1002)
LPLOCALGROUP_INFO_1002 = POINTER(_LOCALGROUP_INFO_1002)


class _LOCALGROUP_MEMBERS_INFO_0(ctypes.Structure):
    pass


LOCALGROUP_MEMBERS_INFO_0 = _LOCALGROUP_MEMBERS_INFO_0
PLOCALGROUP_MEMBERS_INFO_0 = POINTER(_LOCALGROUP_MEMBERS_INFO_0)
LPLOCALGROUP_MEMBERS_INFO_0 = POINTER(_LOCALGROUP_MEMBERS_INFO_0)


class _LOCALGROUP_MEMBERS_INFO_1(ctypes.Structure):
    pass


LOCALGROUP_MEMBERS_INFO_1 = _LOCALGROUP_MEMBERS_INFO_1
PLOCALGROUP_MEMBERS_INFO_1 = POINTER(_LOCALGROUP_MEMBERS_INFO_1)
LPLOCALGROUP_MEMBERS_INFO_1 = POINTER(_LOCALGROUP_MEMBERS_INFO_1)


class _LOCALGROUP_MEMBERS_INFO_2(ctypes.Structure):
    pass


LOCALGROUP_MEMBERS_INFO_2 = _LOCALGROUP_MEMBERS_INFO_2
PLOCALGROUP_MEMBERS_INFO_2 = POINTER(_LOCALGROUP_MEMBERS_INFO_2)
LPLOCALGROUP_MEMBERS_INFO_2 = POINTER(_LOCALGROUP_MEMBERS_INFO_2)


class _LOCALGROUP_MEMBERS_INFO_3(ctypes.Structure):
    pass


LOCALGROUP_MEMBERS_INFO_3 = _LOCALGROUP_MEMBERS_INFO_3
PLOCALGROUP_MEMBERS_INFO_3 = POINTER(_LOCALGROUP_MEMBERS_INFO_3)
LPLOCALGROUP_MEMBERS_INFO_3 = POINTER(_LOCALGROUP_MEMBERS_INFO_3)


class _LOCALGROUP_USERS_INFO_0(ctypes.Structure):
    pass


LOCALGROUP_USERS_INFO_0 = _LOCALGROUP_USERS_INFO_0
PLOCALGROUP_USERS_INFO_0 = POINTER(_LOCALGROUP_USERS_INFO_0)
LPLOCALGROUP_USERS_INFO_0 = POINTER(_LOCALGROUP_USERS_INFO_0)


class _NET_DISPLAY_USER(ctypes.Structure):
    pass


NET_DISPLAY_USER = _NET_DISPLAY_USER
PNET_DISPLAY_USER = POINTER(_NET_DISPLAY_USER)


class _NET_DISPLAY_MACHINE(ctypes.Structure):
    pass


NET_DISPLAY_MACHINE = _NET_DISPLAY_MACHINE
PNET_DISPLAY_MACHINE = POINTER(_NET_DISPLAY_MACHINE)


class _NET_DISPLAY_GROUP(ctypes.Structure):
    pass


NET_DISPLAY_GROUP = _NET_DISPLAY_GROUP
PNET_DISPLAY_GROUP = POINTER(_NET_DISPLAY_GROUP)


class _ACCESS_INFO_0(ctypes.Structure):
    pass


ACCESS_INFO_0 = _ACCESS_INFO_0
PACCESS_INFO_0 = POINTER(_ACCESS_INFO_0)
LPACCESS_INFO_0 = POINTER(_ACCESS_INFO_0)


class _ACCESS_INFO_1(ctypes.Structure):
    pass


ACCESS_INFO_1 = _ACCESS_INFO_1
PACCESS_INFO_1 = POINTER(_ACCESS_INFO_1)
LPACCESS_INFO_1 = POINTER(_ACCESS_INFO_1)


class _ACCESS_INFO_1002(ctypes.Structure):
    pass


ACCESS_INFO_1002 = _ACCESS_INFO_1002
PACCESS_INFO_1002 = POINTER(_ACCESS_INFO_1002)
LPACCESS_INFO_1002 = POINTER(_ACCESS_INFO_1002)


class _ACCESS_LIST(ctypes.Structure):
    pass


ACCESS_LIST = _ACCESS_LIST
PACCESS_LIST = POINTER(_ACCESS_LIST)
LPACCESS_LIST = POINTER(_ACCESS_LIST)


class _NET_VALIDATE_PASSWORD_HASH(ctypes.Structure):
    pass


NET_VALIDATE_PASSWORD_HASH = _NET_VALIDATE_PASSWORD_HASH
PNET_VALIDATE_PASSWORD_HASH = POINTER(_NET_VALIDATE_PASSWORD_HASH)


class _FILETIME(ctypes.Structure):
    pass


FILETIME = _FILETIME
LPFILETIME = POINTER(_FILETIME)
PFILETIME = POINTER(_FILETIME)


class _NET_VALIDATE_PERSISTED_FIELDS(ctypes.Structure):
    pass


NET_VALIDATE_PERSISTED_FIELDS = _NET_VALIDATE_PERSISTED_FIELDS
PNET_VALIDATE_PERSISTED_FIELDS = POINTER(_NET_VALIDATE_PERSISTED_FIELDS)


class _NET_VALIDATE_OUTPUT_ARG(ctypes.Structure):
    pass


NET_VALIDATE_OUTPUT_ARG = _NET_VALIDATE_OUTPUT_ARG
PNET_VALIDATE_OUTPUT_ARG = POINTER(_NET_VALIDATE_OUTPUT_ARG)


class _NET_VALIDATE_AUTHENTICATION_INPUT_ARG(ctypes.Structure):
    pass


NET_VALIDATE_AUTHENTICATION_INPUT_ARG = _NET_VALIDATE_AUTHENTICATION_INPUT_ARG
PNET_VALIDATE_AUTHENTICATION_INPUT_ARG = POINTER(_NET_VALIDATE_AUTHENTICATION_INPUT_ARG)


class _NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG(ctypes.Structure):
    pass


NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG = _NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG
PNET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG = POINTER(_NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG)


class _NET_VALIDATE_PASSWORD_RESET_INPUT_ARG(ctypes.Structure):
    pass


NET_VALIDATE_PASSWORD_RESET_INPUT_ARG = _NET_VALIDATE_PASSWORD_RESET_INPUT_ARG
PNET_VALIDATE_PASSWORD_RESET_INPUT_ARG = POINTER(_NET_VALIDATE_PASSWORD_RESET_INPUT_ARG)


class _NETLOGON_INFO_1(ctypes.Structure):
    pass


NETLOGON_INFO_1 = _NETLOGON_INFO_1
PNETLOGON_INFO_1 = POINTER(_NETLOGON_INFO_1)


class _NETLOGON_INFO_2(ctypes.Structure):
    pass


NETLOGON_INFO_2 = _NETLOGON_INFO_2
PNETLOGON_INFO_2 = POINTER(_NETLOGON_INFO_2)


class _NETLOGON_INFO_3(ctypes.Structure):
    pass


NETLOGON_INFO_3 = _NETLOGON_INFO_3
PNETLOGON_INFO_3 = POINTER(_NETLOGON_INFO_3)


class _NETLOGON_INFO_4(ctypes.Structure):
    pass


NETLOGON_INFO_4 = _NETLOGON_INFO_4
PNETLOGON_INFO_4 = POINTER(_NETLOGON_INFO_4)


class _MSA_INFO_0(ctypes.Structure):
    pass


MSA_INFO_0 = _MSA_INFO_0
PMSA_INFO_0 = POINTER(_MSA_INFO_0)
LPMSA_INFO_0 = POINTER(_MSA_INFO_0)




# /* + + BUILD Version: 0002 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmaccess.h
# Abstract: This file contains structures, function prototypes, and
# definitions for the NetUser, NetUserModals, NetGroup, NetAccess, and
# NetLogon API. Environment: User Mode - Win32 Notes: You must include
# NETCONS.H before this file, since this file depends on values defined in
# NETCONS.H. --
from pyWinAPI.shared.winapifamily_h import * # NOQA

netapi32 = ctypes.windll.NETAPI32
from pyWinAPI.shared.lmcons_h import *  # NOQA

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
    USER_POSIX_ID_PARMNUM = 0
    GROUP_POSIX_ID_PARMNUM = 0

    # User Class
    if not defined(_LMUSER_):
        _LMUSER_ = VOID
        if _MSC_VER > 1000:
            pass
        # END IF

        if defined(__cplusplus):
            pass
        # ENDIF

        # // Function Prototypes - User
        #
        #
        # NET_API_STATUS NET_API_FUNCTION
        # NetUserAdd(
        # _In_opt_  LPCWSTR    servername OPTIONAL,
        # _In_      DWORD      level,
        # _In_      LPBYTE     buf,
        # _Out_opt_ LPDWORD    parm_err OPTIONAL
        # );
        NetUserAdd = netapi32.NetUserAdd
        NetUserAdd.restype = NET_API_STATUS
        # NET_API_STATUS NET_API_FUNCTION
        # NetUserEnum(
        # _In_opt_    LPCWSTR     servername OPTIONAL,
        # _In_        DWORD      level,
        # _In_        DWORD      filter,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE     *bufptr,
        # _In_        DWORD      prefmaxlen,
        # _Out_       LPDWORD    entriesread,
        # _Out_       LPDWORD    totalentries,
        # _Inout_opt_ PDWORD resume_handle OPTIONAL
        # );
        NetUserEnum = netapi32.NetUserEnum
        NetUserEnum.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUserGetInfo(
        # _In_opt_  LPCWSTR     servername OPTIONAL,
        # _In_      LPCWSTR     username,
        # _In_      DWORD      level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE     *bufptr
        # );
        NetUserGetInfo = netapi32.NetUserGetInfo
        NetUserGetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUserSetInfo(
        # _In_opt_  LPCWSTR    servername OPTIONAL,
        # _In_      LPCWSTR    username,
        # _In_      DWORD     level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE    buf,
        # _Out_opt_ LPDWORD   parm_err OPTIONAL
        # );
        NetUserSetInfo = netapi32.NetUserSetInfo
        NetUserSetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUserDel(
        # _In_opt_  LPCWSTR    servername OPTIONAL,
        # _In_      LPCWSTR    username
        # );
        NetUserDel = netapi32.NetUserDel
        NetUserDel.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUserGetGroups(
        # _In_opt_  LPCWSTR    servername OPTIONAL,
        # _In_      LPCWSTR    username,
        # _In_      DWORD     level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE    *bufptr,
        # _In_      DWORD     prefmaxlen,
        # _Out_     LPDWORD   entriesread,
        # _Out_     LPDWORD   totalentries
        # );
        NetUserGetGroups = netapi32.NetUserGetGroups
        NetUserGetGroups.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUserSetGroups(
        # _In_opt_  LPCWSTR    servername OPTIONAL,
        # _In_      LPCWSTR    username,
        # _In_      DWORD     level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE    buf,
        # _In_      DWORD     num_entries
        # );
        NetUserSetGroups = netapi32.NetUserSetGroups
        NetUserSetGroups.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUserGetLocalGroups(
        # _In_opt_  LPCWSTR    servername OPTIONAL,
        # _In_      LPCWSTR    username,
        # _In_      DWORD     level,
        # _In_      DWORD     flags,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE    *bufptr,
        # _In_      DWORD     prefmaxlen,
        # _Out_     LPDWORD   entriesread,
        # _Out_     LPDWORD   totalentries
        # );
        NetUserGetLocalGroups = netapi32.NetUserGetLocalGroups
        NetUserGetLocalGroups.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUserModalsGet(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      DWORD     level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE    *bufptr
        # );
        NetUserModalsGet = netapi32.NetUserModalsGet
        NetUserModalsGet.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUserModalsSet(
        # _In_opt_  LPCWSTR    servername OPTIONAL,
        # _In_      DWORD     level,
        # _In_reads_(_Inexpressible_("varies"))      LPBYTE    buf,
        # _Out_opt_ LPDWORD   parm_err OPTIONAL
        # );
        NetUserModalsSet = netapi32.NetUserModalsSet
        NetUserModalsSet.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetUserChangePassword(
        # _In_opt_ IN  LPCWSTR   domainname OPTIONAL,
        # _In_opt_ IN  LPCWSTR   username OPTIONAL,
        # _In_ IN  LPCWSTR   oldpassword,
        # _In_ IN  LPCWSTR   newpassword
        # );
        NetUserChangePassword = netapi32.NetUserChangePassword
        NetUserChangePassword.restype = NET_API_STATUS

        # Data Structures - User
        _USER_INFO_0._fields_ = [
            ('usri0_name', LPWSTR),
        ]
        _USER_INFO_1._fields_ = [
            ('usri1_name', LPWSTR),
            ('usri1_password', LPWSTR),
            ('usri1_password_age', DWORD),
            ('usri1_priv', DWORD),
            ('usri1_home_dir', LPWSTR),
            ('usri1_comment', LPWSTR),
            ('usri1_flags', DWORD),
            ('usri1_script_path', LPWSTR),
        ]
        _USER_INFO_2._fields_ = [
            ('usri2_name', LPWSTR),
            ('usri2_password', LPWSTR),
            ('usri2_password_age', DWORD),
            ('usri2_priv', DWORD),
            ('usri2_home_dir', LPWSTR),
            ('usri2_comment', LPWSTR),
            ('usri2_flags', DWORD),
            ('usri2_script_path', LPWSTR),
            ('usri2_auth_flags', DWORD),
            ('usri2_full_name', LPWSTR),
            ('usri2_usr_comment', LPWSTR),
            ('usri2_parms', LPWSTR),
            ('usri2_workstations', LPWSTR),
            ('usri2_last_logon', DWORD),
            ('usri2_last_logoff', DWORD),
            ('usri2_acct_expires', DWORD),
            ('usri2_max_storage', DWORD),
            ('usri2_units_per_week', DWORD),
            ('usri2_logon_hours', PBYTE),
            ('usri2_bad_pw_count', DWORD),
            ('usri2_num_logons', DWORD),
            ('usri2_logon_server', LPWSTR),
            ('usri2_country_code', DWORD),
            ('usri2_code_page', DWORD),
        ]
        _USER_INFO_3._fields_ = [
            ('usri3_name', LPWSTR),
            ('usri3_password', LPWSTR),
            ('usri3_password_age', DWORD),
            ('usri3_priv', DWORD),
            ('usri3_home_dir', LPWSTR),
            ('usri3_comment', LPWSTR),
            ('usri3_flags', DWORD),
            ('usri3_script_path', LPWSTR),
            ('usri3_auth_flags', DWORD),
            ('usri3_full_name', LPWSTR),
            ('usri3_usr_comment', LPWSTR),
            ('usri3_parms', LPWSTR),
            ('usri3_workstations', LPWSTR),
            ('usri3_last_logon', DWORD),
            ('usri3_last_logoff', DWORD),
            ('usri3_acct_expires', DWORD),
            ('usri3_max_storage', DWORD),
            ('usri3_units_per_week', DWORD),
            ('usri3_logon_hours', PBYTE),
            ('usri3_bad_pw_count', DWORD),
            ('usri3_num_logons', DWORD),
            ('usri3_logon_server', LPWSTR),
            ('usri3_country_code', DWORD),
            ('usri3_code_page', DWORD),
            ('usri3_user_id', DWORD),
            ('usri3_primary_group_id', DWORD),
            ('usri3_profile', LPWSTR),
            ('usri3_home_dir_drive', LPWSTR),
            ('usri3_password_expired', DWORD),
        ]
        _USER_INFO_4._fields_ = [
            ('usri4_name', LPWSTR),
            ('usri4_password', LPWSTR),
            ('usri4_password_age', DWORD),
            ('usri4_priv', DWORD),
            ('usri4_home_dir', LPWSTR),
            ('usri4_comment', LPWSTR),
            ('usri4_flags', DWORD),
            ('usri4_script_path', LPWSTR),
            ('usri4_auth_flags', DWORD),
            ('usri4_full_name', LPWSTR),
            ('usri4_usr_comment', LPWSTR),
            ('usri4_parms', LPWSTR),
            ('usri4_workstations', LPWSTR),
            ('usri4_last_logon', DWORD),
            ('usri4_last_logoff', DWORD),
            ('usri4_acct_expires', DWORD),
            ('usri4_max_storage', DWORD),
            ('usri4_units_per_week', DWORD),
            ('usri4_logon_hours', PBYTE),
            ('usri4_bad_pw_count', DWORD),
            ('usri4_num_logons', DWORD),
            ('usri4_logon_server', LPWSTR),
            ('usri4_country_code', DWORD),
            ('usri4_code_page', DWORD),
            ('usri4_user_sid', PSID),
            ('usri4_primary_group_id', DWORD),
            ('usri4_profile', LPWSTR),
            ('usri4_home_dir_drive', LPWSTR),
            ('usri4_password_expired', DWORD),
        ]
        _USER_INFO_10._fields_ = [
            ('usri10_name', LPWSTR),
            ('usri10_comment', LPWSTR),
            ('usri10_usr_comment', LPWSTR),
            ('usri10_full_name', LPWSTR),
        ]
        _USER_INFO_11._fields_ = [
            ('usri11_name', LPWSTR),
            ('usri11_comment', LPWSTR),
            ('usri11_usr_comment', LPWSTR),
            ('usri11_full_name', LPWSTR),
            ('usri11_priv', DWORD),
            ('usri11_auth_flags', DWORD),
            ('usri11_password_age', DWORD),
            ('usri11_home_dir', LPWSTR),
            ('usri11_parms', LPWSTR),
            ('usri11_last_logon', DWORD),
            ('usri11_last_logoff', DWORD),
            ('usri11_bad_pw_count', DWORD),
            ('usri11_num_logons', DWORD),
            ('usri11_logon_server', LPWSTR),
            ('usri11_country_code', DWORD),
            ('usri11_workstations', LPWSTR),
            ('usri11_max_storage', DWORD),
            ('usri11_units_per_week', DWORD),
            ('usri11_logon_hours', PBYTE),
            ('usri11_code_page', DWORD),
        ]
        _USER_INFO_20._fields_ = [
            ('usri20_name', LPWSTR),
            ('usri20_full_name', LPWSTR),
            ('usri20_comment', LPWSTR),
            ('usri20_flags', DWORD),
            ('usri20_user_id', DWORD),
        ]
        _USER_INFO_21._fields_ = [
            ('usri21_password', BYTE * ENCRYPTED_PWLEN),
        ]
        _USER_INFO_22._fields_ = [
            ('usri22_name', LPWSTR),
            ('usri22_password', BYTE * ENCRYPTED_PWLEN),
            ('usri22_password_age', DWORD),
            ('usri22_priv', DWORD),
            ('usri22_home_dir', LPWSTR),
            ('usri22_comment', LPWSTR),
            ('usri22_flags', DWORD),
            ('usri22_script_path', LPWSTR),
            ('usri22_auth_flags', DWORD),
            ('usri22_full_name', LPWSTR),
            ('usri22_usr_comment', LPWSTR),
            ('usri22_parms', LPWSTR),
            ('usri22_workstations', LPWSTR),
            ('usri22_last_logon', DWORD),
            ('usri22_last_logoff', DWORD),
            ('usri22_acct_expires', DWORD),
            ('usri22_max_storage', DWORD),
            ('usri22_units_per_week', DWORD),
            ('usri22_logon_hours', PBYTE),
            ('usri22_bad_pw_count', DWORD),
            ('usri22_num_logons', DWORD),
            ('usri22_logon_server', LPWSTR),
            ('usri22_country_code', DWORD),
            ('usri22_code_page', DWORD),
        ]
        _USER_INFO_23._fields_ = [
            ('usri23_name', LPWSTR),
            ('usri23_full_name', LPWSTR),
            ('usri23_comment', LPWSTR),
            ('usri23_flags', DWORD),
            ('usri23_user_sid', PSID),
        ]
        _USER_INFO_24._fields_ = [
            ('usri24_internet_identity', BOOL),
            ('usri24_flags', DWORD),
            ('usri24_internet_provider_name', LPWSTR),
            ('usri24_internet_principal_name', LPWSTR),
            ('usri24_user_sid', PSID),
        ]
        _USER_INFO_1003._fields_ = [
            ('usri1003_password', LPWSTR),
        ]
        _USER_INFO_1005._fields_ = [
            ('usri1005_priv', DWORD),
        ]
        _USER_INFO_1006._fields_ = [
            ('usri1006_home_dir', LPWSTR),
        ]
        _USER_INFO_1007._fields_ = [
            ('usri1007_comment', LPWSTR),
        ]
        _USER_INFO_1008._fields_ = [
            ('usri1008_flags', DWORD),
        ]
        _USER_INFO_1009._fields_ = [
            ('usri1009_script_path', LPWSTR),
        ]
        _USER_INFO_1010._fields_ = [
            ('usri1010_auth_flags', DWORD),
        ]
        _USER_INFO_1011._fields_ = [
            ('usri1011_full_name', LPWSTR),
        ]
        _USER_INFO_1012._fields_ = [
            ('usri1012_usr_comment', LPWSTR),
        ]
        _USER_INFO_1013._fields_ = [
            ('usri1013_parms', LPWSTR),
        ]
        _USER_INFO_1014._fields_ = [
            ('usri1014_workstations', LPWSTR),
        ]
        _USER_INFO_1017._fields_ = [
            ('usri1017_acct_expires', DWORD),
        ]
        _USER_INFO_1018._fields_ = [
            ('usri1018_max_storage', DWORD),
        ]
        _USER_INFO_1020._fields_ = [
            ('usri1020_units_per_week', DWORD),
            ('usri1020_logon_hours', LPBYTE),
        ]
        _USER_INFO_1023._fields_ = [
            ('usri1023_logon_server', LPWSTR),
        ]
        _USER_INFO_1024._fields_ = [
            ('usri1024_country_code', DWORD),
        ]
        _USER_INFO_1025._fields_ = [
            ('usri1025_code_page', DWORD),
        ]
        _USER_INFO_1051._fields_ = [
            ('usri1051_primary_group_id', DWORD),
        ]
        _USER_INFO_1052._fields_ = [
            ('usri1052_profile', LPWSTR),
        ]
        _USER_INFO_1053._fields_ = [
            ('usri1053_home_dir_drive', LPWSTR),
        ]
        # Data Structures - User Modals
        _USER_MODALS_INFO_0._fields_ = [
            ('usrmod0_min_passwd_len', DWORD),
            ('usrmod0_max_passwd_age', DWORD),
            ('usrmod0_min_passwd_age', DWORD),
            ('usrmod0_force_logoff', DWORD),
            ('usrmod0_password_hist_len', DWORD),
        ]
        _USER_MODALS_INFO_1._fields_ = [
            ('usrmod1_role', DWORD),
            ('usrmod1_primary', LPWSTR),
        ]
        _USER_MODALS_INFO_2._fields_ = [
            ('usrmod2_domain_name', LPWSTR),
            ('usrmod2_domain_id', PSID),
        ]
        _USER_MODALS_INFO_3._fields_ = [
            ('usrmod3_lockout_duration', DWORD),
            ('usrmod3_lockout_observation_window', DWORD),
            ('usrmod3_lockout_threshold', DWORD),
        ]
        _USER_MODALS_INFO_1001._fields_ = [
            ('usrmod1001_min_passwd_len', DWORD),
        ]
        _USER_MODALS_INFO_1002._fields_ = [
            ('usrmod1002_max_passwd_age', DWORD),
        ]
        _USER_MODALS_INFO_1003._fields_ = [
            ('usrmod1003_min_passwd_age', DWORD),
        ]
        _USER_MODALS_INFO_1004._fields_ = [
            ('usrmod1004_force_logoff', DWORD),
        ]
        _USER_MODALS_INFO_1005._fields_ = [
            ('usrmod1005_password_hist_len', DWORD),
        ]
        _USER_MODALS_INFO_1006._fields_ = [
            ('usrmod1006_role', DWORD),
        ]
        _USER_MODALS_INFO_1007._fields_ = [
            ('usrmod1007_primary', LPWSTR),
        ]
        # Special Values and Constants - User
        # Bit masks for field usriX_flags of USER_INFO_X (X = 0/1).
        UF_SCRIPT = 0x0001
        UF_ACCOUNTDISABLE = 0x0002
        UF_HOMEDIR_REQUIRED = 0x0008
        UF_LOCKOUT = 0x0010
        UF_PASSWD_NOTREQD = 0x0020
        UF_PASSWD_CANT_CHANGE = 0x0040
        UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED = 0x0080
        # Account type bits as part of usri_flags.
        UF_TEMP_DUPLICATE_ACCOUNT = 0x0100
        UF_NORMAL_ACCOUNT = 0x0200
        UF_INTERDOMAIN_TRUST_ACCOUNT = 0x0800
        UF_WORKSTATION_TRUST_ACCOUNT = 0x1000
        UF_SERVER_TRUST_ACCOUNT = 0x2000
        UF_MACHINE_ACCOUNT_MASK = (
            UF_INTERDOMAIN_TRUST_ACCOUNT |
            UF_WORKSTATION_TRUST_ACCOUNT |
            UF_SERVER_TRUST_ACCOUNT
        )
        UF_ACCOUNT_TYPE_MASK = (
            UF_TEMP_DUPLICATE_ACCOUNT |
            UF_NORMAL_ACCOUNT |
            UF_INTERDOMAIN_TRUST_ACCOUNT |
            UF_WORKSTATION_TRUST_ACCOUNT |
            UF_SERVER_TRUST_ACCOUNT
        )
        UF_DONT_EXPIRE_PASSWD = 0x10000
        UF_MNS_LOGON_ACCOUNT = 0x20000
        UF_SMARTCARD_REQUIRED = 0x40000
        UF_TRUSTED_FOR_DELEGATION = 0x80000
        UF_NOT_DELEGATED = 0x100000
        UF_USE_DES_KEY_ONLY = 0x200000
        UF_DONT_REQUIRE_PREAUTH = 0x400000
        UF_PASSWORD_EXPIRED = 0x800000
        UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION = 0x1000000
        UF_NO_AUTH_DATA_REQUIRED = 0x2000000
        UF_PARTIAL_SECRETS_ACCOUNT = 0x4000000
        UF_USE_AES_KEYS = 0x8000000
        UF_SETTABLE_BITS = (
            UF_SCRIPT |
            UF_ACCOUNTDISABLE |
            UF_LOCKOUT |
            UF_HOMEDIR_REQUIRED |
            UF_PASSWD_NOTREQD |
            UF_PASSWD_CANT_CHANGE |
            UF_ACCOUNT_TYPE_MASK |
            UF_DONT_EXPIRE_PASSWD |
            UF_MNS_LOGON_ACCOUNT |
            UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED |
            UF_SMARTCARD_REQUIRED |
            UF_TRUSTED_FOR_DELEGATION |
            UF_NOT_DELEGATED |
            UF_USE_DES_KEY_ONLY |
            UF_DONT_REQUIRE_PREAUTH |
            UF_PASSWORD_EXPIRED |
            UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION |
            UF_NO_AUTH_DATA_REQUIRED |
            UF_USE_AES_KEYS |
            UF_PARTIAL_SECRETS_ACCOUNT
        )
        # bit masks for the NetUserEnum filter parameter.
        FILTER_TEMP_DUPLICATE_ACCOUNT = 0x0001
        FILTER_NORMAL_ACCOUNT = 0x0002
        # define FILTER_PROXY_ACCOUNT   (0x0004)
        FILTER_INTERDOMAIN_TRUST_ACCOUNT = 0x0008
        FILTER_WORKSTATION_TRUST_ACCOUNT = 0x0010
        FILTER_SERVER_TRUST_ACCOUNT = 0x0020
        # bit masks for the NetUserGetLocalGroups flags
        LG_INCLUDE_INDIRECT = 0x0001
        # Bit masks for field usri2_auth_flags of USER_INFO_2.
        AF_OP_PRINT = 0x1
        AF_OP_COMM = 0x2
        AF_OP_SERVER = 0x4
        AF_OP_ACCOUNTS = 0x8
        AF_SETTABLE_BITS = (
            AF_OP_PRINT |
            AF_OP_COMM |
            AF_OP_SERVER |
            AF_OP_ACCOUNTS
        )
        # UAS role manifests under NETLOGON
        UAS_ROLE_STANDALONE = 0
        UAS_ROLE_MEMBER = 1
        UAS_ROLE_BACKUP = 2
        UAS_ROLE_PRIMARY = 3
        # Values for ParmError for NetUserSetInfo.
        USER_NAME_PARMNUM = 1
        USER_PASSWORD_PARMNUM = 3
        USER_PASSWORD_AGE_PARMNUM = 4
        USER_PRIV_PARMNUM = 5
        USER_HOME_DIR_PARMNUM = 6
        USER_COMMENT_PARMNUM = 7
        USER_FLAGS_PARMNUM = 8
        USER_SCRIPT_PATH_PARMNUM = 9
        USER_AUTH_FLAGS_PARMNUM = 10
        USER_FULL_NAME_PARMNUM = 11
        USER_USR_COMMENT_PARMNUM = 12
        USER_PARMS_PARMNUM = 13
        USER_WORKSTATIONS_PARMNUM = 14
        USER_LAST_LOGON_PARMNUM = 15
        USER_LAST_LOGOFF_PARMNUM = 16
        USER_ACCT_EXPIRES_PARMNUM = 17
        USER_MAX_STORAGE_PARMNUM = 18
        USER_UNITS_PER_WEEK_PARMNUM = 19
        USER_LOGON_HOURS_PARMNUM = 20
        USER_PAD_PW_COUNT_PARMNUM = 21
        USER_NUM_LOGONS_PARMNUM = 22
        USER_LOGON_SERVER_PARMNUM = 23
        USER_COUNTRY_CODE_PARMNUM = 24
        USER_CODE_PAGE_PARMNUM = 25
        USER_PRIMARY_GROUP_PARMNUM = 51
        USER_PROFILE = 52  # ?? Delete when convenient
        USER_PROFILE_PARMNUM = 52
        USER_HOME_DIR_DRIVE_PARMNUM = 53
        # the new infolevel counterparts of the old info level + parmnum
        USER_NAME_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + USER_NAME_PARMNUM
        USER_PASSWORD_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_PASSWORD_PARMNUM
        )
        USER_PASSWORD_AGE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_PASSWORD_AGE_PARMNUM
        )
        USER_PRIV_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + USER_PRIV_PARMNUM
        USER_HOME_DIR_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_HOME_DIR_PARMNUM
        )
        USER_COMMENT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_COMMENT_PARMNUM
        )
        USER_FLAGS_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + USER_FLAGS_PARMNUM
        USER_SCRIPT_PATH_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_SCRIPT_PATH_PARMNUM
        )
        USER_AUTH_FLAGS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_AUTH_FLAGS_PARMNUM
        )
        USER_FULL_NAME_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_FULL_NAME_PARMNUM
        )
        USER_USR_COMMENT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_USR_COMMENT_PARMNUM
        )
        USER_PARMS_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + USER_PARMS_PARMNUM
        USER_WORKSTATIONS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_WORKSTATIONS_PARMNUM
        )
        USER_LAST_LOGON_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_LAST_LOGON_PARMNUM
        )
        USER_LAST_LOGOFF_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_LAST_LOGOFF_PARMNUM
        )
        USER_ACCT_EXPIRES_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_ACCT_EXPIRES_PARMNUM
        )
        USER_MAX_STORAGE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_MAX_STORAGE_PARMNUM
        )
        USER_UNITS_PER_WEEK_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_UNITS_PER_WEEK_PARMNUM
        )
        USER_LOGON_HOURS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_LOGON_HOURS_PARMNUM
        )
        USER_PAD_PW_COUNT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_PAD_PW_COUNT_PARMNUM
        )
        USER_NUM_LOGONS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_NUM_LOGONS_PARMNUM
        )
        USER_LOGON_SERVER_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_LOGON_SERVER_PARMNUM
        )
        USER_COUNTRY_CODE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_COUNTRY_CODE_PARMNUM
        )
        USER_CODE_PAGE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_CODE_PAGE_PARMNUM
        )
        USER_PRIMARY_GROUP_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_PRIMARY_GROUP_PARMNUM
        )
        USER_POSIX_ID_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_POSIX_ID_PARMNUM
        )
        USER_HOME_DIR_DRIVE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + USER_HOME_DIR_DRIVE_PARMNUM
        )
        # For SetInfo call (parmnum 0) when password change not required
        NULL_USERSETINFO_PASSWD = "              "
        TIMEQ_FOREVER = -1
        USER_MAXSTORAGE_UNLIMITED = -1
        USER_NO_LOGOFF = -1
        UNITS_PER_DAY = 24
        UNITS_PER_WEEK = UNITS_PER_DAY * 7
        # Privilege levels (USER_INFO_X field usriX_priv (X = 0/1)).
        USER_PRIV_MASK = 0x3
        USER_PRIV_GUEST = 0
        USER_PRIV_USER = 1
        USER_PRIV_ADMIN = 2
        # user modals related defaults
        MAX_PASSWD_LEN = PWLEN
        DEF_MIN_PWLEN = 6
        DEF_PWUNIQUENESS = 5
        DEF_MAX_PWHIST = 8
        DEF_MAX_PWAGE = TIMEQ_FOREVER  # forever
        DEF_MIN_PWAGE = 0  # 0 days
        DEF_FORCE_LOGOFF = 0xFFFFFFFF  # never
        DEF_MAX_BADPW = 0  # no limit
        ONE_DAY = 01 * 24 * 3600  # 01 day
        # User Logon Validation (codes returned)
        VALIDATED_LOGON = 0
        PASSWORD_EXPIRED = 2
        NON_VALIDATED_LOGON = 3
        VALID_LOGOFF = 1
        # parmnum manifests for user modals
        MODALS_MIN_PASSWD_LEN_PARMNUM = 1
        MODALS_MAX_PASSWD_AGE_PARMNUM = 2
        MODALS_MIN_PASSWD_AGE_PARMNUM = 3
        MODALS_FORCE_LOGOFF_PARMNUM = 4
        MODALS_PASSWD_HIST_LEN_PARMNUM = 5
        MODALS_ROLE_PARMNUM = 6
        MODALS_PRIMARY_PARMNUM = 7
        MODALS_DOMAIN_NAME_PARMNUM = 8
        MODALS_DOMAIN_ID_PARMNUM = 9
        MODALS_LOCKOUT_DURATION_PARMNUM = 10
        MODALS_LOCKOUT_OBSERVATION_WINDOW_PARMNUM = 11
        MODALS_LOCKOUT_THRESHOLD_PARMNUM = 12
        # the new infolevel counterparts of the old info level + parmnum
        MODALS_MIN_PASSWD_LEN_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + MODALS_MIN_PASSWD_LEN_PARMNUM
        )
        MODALS_MAX_PASSWD_AGE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + MODALS_MAX_PASSWD_AGE_PARMNUM
        )
        MODALS_MIN_PASSWD_AGE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + MODALS_MIN_PASSWD_AGE_PARMNUM
        )
        MODALS_FORCE_LOGOFF_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + MODALS_FORCE_LOGOFF_PARMNUM
        )
        MODALS_PASSWD_HIST_LEN_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + MODALS_PASSWD_HIST_LEN_PARMNUM
        )
        MODALS_ROLE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + MODALS_ROLE_PARMNUM
        )
        MODALS_PRIMARY_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + MODALS_PRIMARY_PARMNUM
        )
        MODALS_DOMAIN_NAME_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + MODALS_DOMAIN_NAME_PARMNUM
        )
        MODALS_DOMAIN_ID_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + MODALS_DOMAIN_ID_PARMNUM
        )
        # END IF   _LMUSER_
        # Group Class

    if not defined(_LMGROUP_):
        _LMGROUP_ = VOID

        # Function Prototypes

        # NET_API_STATUS NET_API_FUNCTION
        # NetGroupAdd(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      DWORD    level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE   buf,
        # _Out_opt_ LPDWORD  parm_err OPTIONAL
        # );
        NetGroupAdd = netapi32.NetGroupAdd
        NetGroupAdd.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetGroupAddUser(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      LPCWSTR   GroupName,
        # _In_      LPCWSTR   username
        # );
        NetGroupAddUser = netapi32.NetGroupAddUser
        NetGroupAddUser.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetGroupEnum(
        # _In_opt_    LPCWSTR      servername OPTIONAL,
        # _In_        DWORD       level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE      *bufptr,
        # _In_        DWORD       prefmaxlen,
        # _Out_       LPDWORD     entriesread,
        # _Out_       LPDWORD     totalentries,
        # _Inout_opt_ PDWORD_PTR resume_handle OPTIONAL
        # );
        NetGroupEnum = netapi32.NetGroupEnum
        NetGroupEnum.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetGroupGetInfo(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      LPCWSTR   groupname,
        # _In_      DWORD    level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE   *bufptr
        # );
        NetGroupGetInfo = netapi32.NetGroupGetInfo
        NetGroupGetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetGroupSetInfo(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      LPCWSTR   groupname,
        # _In_      DWORD    level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE   buf,
        # _Out_opt_ LPDWORD  parm_err OPTIONAL
        # );
        NetGroupSetInfo = netapi32.NetGroupSetInfo
        NetGroupSetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetGroupDel(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      LPCWSTR   groupname
        # );
        NetGroupDel = netapi32.NetGroupDel
        NetGroupDel.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetGroupDelUser(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      LPCWSTR   GroupName,
        # _In_      LPCWSTR   Username
        # );
        NetGroupDelUser = netapi32.NetGroupDelUser
        NetGroupDelUser.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetGroupGetUsers(
        # _In_opt_    LPCWSTR     servername OPTIONAL,
        # _In_        LPCWSTR     groupname,
        # _In_        DWORD      level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE     *bufptr,
        # _In_        DWORD      prefmaxlen,
        # _Out_       LPDWORD    entriesread,
        # _Out_       LPDWORD    totalentries,
        # _Inout_opt_ PDWORD_PTR ResumeHandle
        # );
        NetGroupGetUsers = netapi32.NetGroupGetUsers
        NetGroupGetUsers.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetGroupSetUsers(
        # _In_opt_  LPCWSTR     servername OPTIONAL,
        # _In_      LPCWSTR     groupname,
        # _In_      DWORD      level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE     buf,
        # _In_      DWORD      totalentries
        # );
        NetGroupSetUsers = netapi32.NetGroupSetUsers
        NetGroupSetUsers.restype = NET_API_STATUS

        # Data Structures - Group
        _GROUP_INFO_0._fields_ = [
            ('grpi0_name', LPWSTR),
        ]

        _GROUP_INFO_1._fields_ = [
            ('grpi1_name', LPWSTR),
            ('grpi1_comment', LPWSTR),
        ]

        _GROUP_INFO_2._fields_ = [
            ('grpi2_name', LPWSTR),
            ('grpi2_comment', LPWSTR),
            ('grpi2_group_id', DWORD),
            ('grpi2_attributes', DWORD),
        ]

        _GROUP_INFO_3._fields_ = [
            ('grpi3_name', LPWSTR),
            ('grpi3_comment', LPWSTR),
            ('grpi3_group_sid', PSID),
            ('grpi3_attributes', DWORD),
        ]

        _GROUP_INFO_1002._fields_ = [
            ('grpi1002_comment', LPWSTR),
        ]

        _GROUP_INFO_1005._fields_ = [
            ('grpi1005_attributes', DWORD),
        ]

        _GROUP_USERS_INFO_0._fields_ = [
            ('grui0_name', LPWSTR),
        ]

        _GROUP_USERS_INFO_1._fields_ = [
            ('grui1_name', LPWSTR),
            ('grui1_attributes', DWORD),
        ]

        # Special Values and Constants - Group
        GROUPIDMASK = 0x8000  # MSB set if uid refers

        # to a group
        # Predefined group for all normal users, administrators and guests
        # LOCAL is a special group for pinball local security.
        GROUP_SPECIALGRP_USERS = "USERS"
        GROUP_SPECIALGRP_ADMINS = "ADMINS"
        GROUP_SPECIALGRP_GUESTS = "GUESTS"
        GROUP_SPECIALGRP_LOCAL = "LOCAL"

        # parmnum manifests for SetInfo calls (only comment is settable)
        GROUP_ALL_PARMNUM = 0
        GROUP_NAME_PARMNUM = 1
        GROUP_COMMENT_PARMNUM = 2
        GROUP_ATTRIBUTES_PARMNUM = 3

        # the new infolevel counterparts of the old info level + parmnum
        GROUP_ALL_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + GROUP_ALL_PARMNUM
        GROUP_NAME_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + GROUP_NAME_PARMNUM
        GROUP_COMMENT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + GROUP_COMMENT_PARMNUM
        )
        GROUP_ATTRIBUTES_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + GROUP_ATTRIBUTES_PARMNUM
        )
        GROUP_POSIX_ID_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + GROUP_POSIX_ID_PARMNUM
        )
    # END IF   _LMGROUP_

    # LocalGroup Class
    if not defined(_LMLOCALGROUP_):
        _LMLOCALGROUP_ = VOID

        # Function Prototypes

        # NET_API_STATUS NET_API_FUNCTION
        # NetLocalGroupAdd(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      DWORD    level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE   buf,
        # _Out_opt_ LPDWORD  parm_err OPTIONAL
        # );
        NetLocalGroupAdd = netapi32.NetLocalGroupAdd
        NetLocalGroupAdd.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetLocalGroupAddMember(
        # IN  LPCWSTR   servername OPTIONAL,
        # IN  LPCWSTR   groupname,
        # IN  PSID     membersid
        # );
        NetLocalGroupAddMember = netapi32.NetLocalGroupAddMember
        NetLocalGroupAddMember.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_STATUS
        # NetLocalGroupEnum(
        # _In_opt_    LPCWSTR      servername OPTIONAL,
        # _In_        DWORD       level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE      *bufptr,
        # _In_        DWORD       prefmaxlen,
        # _Out_       LPDWORD     entriesread,
        # _Out_       LPDWORD     totalentries,
        # _Inout_opt_ PDWORD_PTR resumehandle OPTIONAL
        # );
        NetLocalGroupEnum = netapi32.NetLocalGroupEnum
        NetLocalGroupEnum.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_STATUS
        # NetLocalGroupGetInfo(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      LPCWSTR   groupname,
        # _In_      DWORD    level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE   *bufptr
        # );
        NetLocalGroupGetInfo = netapi32.NetLocalGroupGetInfo
        NetLocalGroupGetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetLocalGroupSetInfo(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      LPCWSTR   groupname,
        # _In_      DWORD    level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE   buf,
        # _Out_opt_ LPDWORD  parm_err OPTIONAL
        # );
        NetLocalGroupSetInfo = netapi32.NetLocalGroupSetInfo
        NetLocalGroupSetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetLocalGroupDel(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      LPCWSTR   groupname
        # );
        NetLocalGroupDel = netapi32.NetLocalGroupDel
        NetLocalGroupDel.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetLocalGroupDelMember(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      LPCWSTR   groupname,
        # _In_      PSID     membersid
        # );
        NetLocalGroupDelMember = netapi32.NetLocalGroupDelMember
        NetLocalGroupDelMember.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetLocalGroupGetMembers(
        # _In_opt_    LPCWSTR     servername OPTIONAL,
        # _In_        LPCWSTR     localgroupname,
        # _In_        DWORD      level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE     *bufptr,
        # _In_        DWORD      prefmaxlen,
        # _Out_       LPDWORD    entriesread,
        # _Out_       LPDWORD    totalentries,
        # _Inout_opt_ PDWORD_PTR resumehandle
        # );
        NetLocalGroupGetMembers = netapi32.NetLocalGroupGetMembers
        NetLocalGroupGetMembers.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetLocalGroupSetMembers(
        # _In_opt_  LPCWSTR     servername OPTIONAL,
        # _In_      LPCWSTR     groupname,
        # _In_      DWORD      level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE     buf,
        # _In_      DWORD      totalentries
        # );
        NetLocalGroupSetMembers = netapi32.NetLocalGroupSetMembers
        NetLocalGroupSetMembers.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetLocalGroupAddMembers(
        # _In_opt_  LPCWSTR     servername OPTIONAL,
        # _In_      LPCWSTR     groupname,
        # _In_      DWORD      level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE     buf,
        # _In_      DWORD      totalentries
        # );
        NetLocalGroupAddMembers = netapi32.NetLocalGroupAddMembers
        NetLocalGroupAddMembers.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetLocalGroupDelMembers(
        # _In_opt_  LPCWSTR     servername OPTIONAL,
        # _In_      LPCWSTR     groupname,
        # _In_      DWORD      level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE     buf,
        # _In_      DWORD      totalentries
        # );
        NetLocalGroupDelMembers = netapi32.NetLocalGroupDelMembers
        NetLocalGroupDelMembers.restype = NET_API_STATUS

        from pyWinAPI.um.winnt_h import *

        # Data Structures - LocalGroup
        _LOCALGROUP_INFO_0._fields_ = [
            ('lgrpi0_name', LPWSTR),
        ]

        _LOCALGROUP_INFO_1._fields_ = [
            ('lgrpi1_name', LPWSTR),
            ('lgrpi1_comment', LPWSTR),
        ]

        _LOCALGROUP_INFO_1002._fields_ = [
            ('lgrpi1002_comment', LPWSTR),
        ]

        _LOCALGROUP_MEMBERS_INFO_0._fields_ = [
            ('lgrmi0_sid', PSID),
        ]

        _LOCALGROUP_MEMBERS_INFO_1._fields_ = [
            ('lgrmi1_sid', PSID),
            ('lgrmi1_sidusage', SID_NAME_USE),
            ('lgrmi1_name', LPWSTR),
        ]

        _LOCALGROUP_MEMBERS_INFO_2._fields_ = [
            ('lgrmi2_sid', PSID),
            ('lgrmi2_sidusage', SID_NAME_USE),
            ('lgrmi2_domainandname', LPWSTR),
        ]

        _LOCALGROUP_MEMBERS_INFO_3._fields_ = [
            ('lgrmi3_domainandname', LPWSTR),
        ]

        _LOCALGROUP_USERS_INFO_0._fields_ = [
            ('lgrui0_name', LPWSTR),
        ]
        LOCALGROUP_NAME_PARMNUM = 1
        LOCALGROUP_COMMENT_PARMNUM = 2

        # Display Information APIs
        # NET_API_STATUS NET_API_FUNCTION
        # NetQueryDisplayInformation(
        # IN LPCWSTR ServerName OPTIONAL,
        # IN DWORD Level,
        # IN DWORD Index,
        # IN DWORD EntriesRequested,
        # IN DWORD PreferredMaximumLength,
        # OUT LPDWORD ReturnedEntryCount,
        # OUT PVOID   *SortedBuffer );
        NetQueryDisplayInformation = netapi32.NetQueryDisplayInformation
        NetQueryDisplayInformation.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetGetDisplayInformationIndex(
        # IN LPCWSTR ServerName OPTIONAL,
        # IN DWORD Level,
        # IN LPCWSTR Prefix,
        # OUT LPDWORD Index );
        NetGetDisplayInformationIndex = (
            netapi32.NetGetDisplayInformationIndex
        )
        NetGetDisplayInformationIndex.restype = NET_API_STATUS

        # QueryDisplayInformation levels
        _NET_DISPLAY_USER._fields_ = [
            ('usri1_name', LPWSTR),
            ('usri1_comment', LPWSTR),
            ('usri1_flags', DWORD),
            ('usri1_full_name', LPWSTR),
            ('usri1_user_id', DWORD),
            ('usri1_next_index', DWORD),
        ]

        _NET_DISPLAY_MACHINE._fields_ = [
            ('usri2_name', LPWSTR),
            ('usri2_comment', LPWSTR),
            ('usri2_flags', DWORD),
            ('usri2_user_id', DWORD),
            ('usri2_next_index', DWORD),
        ]

        _NET_DISPLAY_GROUP._fields_ = [
            ('grpi3_name', LPWSTR),
            ('grpi3_comment', LPWSTR),
            ('grpi3_group_id', DWORD),
            ('grpi3_attributes', DWORD),
            ('grpi3_next_index', DWORD),
        ]
    # END IF   _LMLOCALGROUP_
# END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

# Access Class
if not defined(_LMACCESS_):
    _LMACCESS_ = VOID
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Function Prototypes - Access

        # NET_API_STATUS NET_API_FUNCTION
        # NetAccessAdd(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      DWORD    level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE   buf,
        # _Out_opt_ LPDWORD  parm_err OPTIONAL
        # );
        NetAccessAdd = netapi32.NetAccessAdd
        NetAccessAdd.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetAccessEnum(
        # _In_opt_    LPCWSTR     servername OPTIONAL,
        # _In_        LPCWSTR     BasePath,
        # _In_        DWORD      Recursive,
        # _In_        DWORD      level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE     *bufptr,
        # _In_        DWORD      prefmaxlen,
        # _Out_       LPDWORD    entriesread,
        # _Out_       LPDWORD    totalentries,
        # _Inout_opt_ LPDWORD resume_handle OPTIONAL
        # );
        NetAccessEnum = netapi32.NetAccessEnum
        NetAccessEnum.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetAccessGetInfo(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      LPCWSTR   resource,
        # _In_      DWORD    level,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE   *bufptr
        # );
        NetAccessGetInfo = netapi32.NetAccessGetInfo
        NetAccessGetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetAccessSetInfo(
        # _In_opt_  LPCWSTR   servername OPTIONAL,
        # _In_      LPCWSTR   resource,
        # _In_      DWORD    level,
        # _In_reads_(_Inexpressible_("varies"))  LPBYTE   buf,
        # _Out_opt_ LPDWORD  parm_err OPTIONAL
        # );
        NetAccessSetInfo = netapi32.NetAccessSetInfo
        NetAccessSetInfo.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetAccessDel(
        # IN  LPCWSTR   servername OPTIONAL,
        # IN  LPCWSTR   resource
        # );
        NetAccessDel = netapi32.NetAccessDel
        NetAccessDel.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetAccessGetUserPerms(
        # IN  LPCWSTR   servername OPTIONAL,
        # IN  LPCWSTR   UGname,
        # IN  LPCWSTR   resource,
        # OUT LPDWORD  Perms
        # );
        NetAccessGetUserPerms = netapi32.NetAccessGetUserPerms
        NetAccessGetUserPerms.restype = NET_API_STATUS

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # Data Structures - Access
        _ACCESS_INFO_0._fields_ = [
            ('acc0_resource_name', LPWSTR),
        ]

        _ACCESS_INFO_1._fields_ = [
            ('acc1_resource_name', LPWSTR),
            ('acc1_attr', DWORD),
            ('acc1_count', DWORD),
        ]

        _ACCESS_INFO_1002._fields_ = [
            ('acc1002_attr', DWORD),
        ]

        _ACCESS_LIST._fields_ = [
            ('acl_ugname', LPWSTR),
            ('acl_access', DWORD),
        ]

        # Special Values and Constants - Access
        # Maximum number of permission entries for each resource.
        MAXPERMENTRIES = 64

        # Bit values for the access permissions. ACCESS_ALL is a handy
        # way to specify maximum permissions. These are used in
        # acl_access field of access_list structures.
        ACCESS_NONE = 0

        ACCESS_READ = 0x01
        ACCESS_WRITE = 0x02
        ACCESS_CREATE = 0x04
        ACCESS_EXEC = 0x08
        ACCESS_DELETE = 0x10
        ACCESS_ATRIB = 0x20
        ACCESS_PERM = 0x40
        ACCESS_GROUP = 0x8000

        ACCESS_ALL = (
            ACCESS_READ |
            ACCESS_WRITE |
            ACCESS_CREATE |
            ACCESS_EXEC |
            ACCESS_DELETE |
            ACCESS_ATRIB |
            ACCESS_PERM
        )

        # Bit values for the acc1_attr field of the ACCESS_INFO_1
        # structure.
        ACCESS_AUDIT = 0x1
        ACCESS_SUCCESS_OPEN = 0x10
        ACCESS_SUCCESS_WRITE = 0x20
        ACCESS_SUCCESS_DELETE = 0x40
        ACCESS_SUCCESS_ACL = 0x80
        ACCESS_SUCCESS_MASK = 0xF0
        ACCESS_FAIL_OPEN = 0x100
        ACCESS_FAIL_WRITE = 0x200
        ACCESS_FAIL_DELETE = 0x400
        ACCESS_FAIL_ACL = 0x800
        ACCESS_FAIL_MASK = 0xF00
        ACCESS_FAIL_SHIFT = 4

        # Parmnum value for NetAccessSetInfo.
        ACCESS_RESOURCE_NAME_PARMNUM = 1
        ACCESS_ATTR_PARMNUM = 2
        ACCESS_COUNT_PARMNUM = 3
        ACCESS_ACCESS_LIST_PARMNUM = 4

        # the new infolevel counterparts of the old info level + parmnum
        ACCESS_RESOURCE_NAME_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + ACCESS_RESOURCE_NAME_PARMNUM
        )
        ACCESS_ATTR_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + ACCESS_ATTR_PARMNUM
        )
        ACCESS_COUNT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + ACCESS_COUNT_PARMNUM
        )
        ACCESS_ACCESS_LIST_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + ACCESS_ACCESS_LIST_PARMNUM
        )

        # ACCESS_LETTERS defines a letter for each bit position in
        # the acl_access field of struct access_list. Note that some
        # bits have a corresponding letter of ' ' (space).
        ACCESS_LETTERS = "RWCXDAP         "


        # ********************************
        # Password Checking API structures
        # ********************************
        # What kind of password checking is to be performed?
        # NetValidateAuthentication : Check if the authentication can be
        # done
        # NetValidatePasswordChange: Check if the password can be changed
        # NetValidatePasswordReset: Reset the password to the given value
        class _NET_VALIDATE_PASSWORD_TYPE(ENUM):
            NetValidateAuthentication = 1
            NetValidatePasswordChange = 2
            NetValidatePasswordReset = 3


        NET_VALIDATE_PASSWORD_TYPE = _NET_VALIDATE_PASSWORD_TYPE
        PNET_VALIDATE_PASSWORD_TYPE = POINTER(_NET_VALIDATE_PASSWORD_TYPE)

        # Structure to keep the password hash
        _NET_VALIDATE_PASSWORD_HASH._fields_ = [
            ('Length', ULONG),
            ('Hash', LPBYTE),
        ]

        # To be used with PresentFields member of
        # NET_VALIDATE_PERSISTED_FIELDS
        NET_VALIDATE_PASSWORD_LAST_SET = 0x00000001
        NET_VALIDATE_BAD_PASSWORD_TIME = 0x00000002
        NET_VALIDATE_LOCKOUT_TIME = 0x00000004
        NET_VALIDATE_BAD_PASSWORD_COUNT = 0x00000008
        NET_VALIDATE_PASSWORD_HISTORY_LENGTH = 0x00000010
        NET_VALIDATE_PASSWORD_HISTORY = 0x00000020
        if not defined(_WINBASE_) and not defined(_FILETIME_):
            _FILETIME_ = VOID

            _FILETIME._fields_ = [
                ('dwLowDateTime', DWORD),
                ('dwHighDateTime', DWORD),
            ]
        # END IF

        # Structure to keep information about the password and related
        # things.
        # Present Fields: (used only in output args) which fields are
        # changed.
        # See the constants above.
        # PasswordLastSet: When the password is last set.
        # BadPasswordTime: When the password was incorrect for the last
        # time.
        # LockoutTime: When the account is locked out. If the account is
        # not locked out
        # it is 0.
        # BadPasswordCount: How many times the password has given
        # incorrectly in the
        # Observation Window.
        # PasswordHistoryLength: How many passwords are kept in the history
        # PasswordHistory: Password hashes that are in the history
        _NET_VALIDATE_PERSISTED_FIELDS._fields_ = [
            ('PresentFields', ULONG),
            ('PasswordLastSet', FILETIME),
            ('BadPasswordTime', FILETIME),
            ('LockoutTime', FILETIME),
            ('BadPasswordCount', ULONG),
            ('PasswordHistoryLength', ULONG),
            ('PasswordHistory', PNET_VALIDATE_PASSWORD_HASH),
        ]

        # Output Arg
        # ChangedPersistedFields: Any changes to the password related info
        # ValidationStatus: Shows the result of the request
        _NET_VALIDATE_OUTPUT_ARG._fields_ = [
            ('ChangedPersistedFields', NET_VALIDATE_PERSISTED_FIELDS),
            ('ValidationStatus', NET_API_STATUS),
        ]

        # If authentication type of password check is to be made,
        # this kind of input must be used
        # InputPersistedFields: Information about the account to be logged
        # into
        # PasswordMatched: Indicates the result of the application's
        # authentication of the supplied password
        _NET_VALIDATE_AUTHENTICATION_INPUT_ARG._fields_ = [
            ('InputPersistedFields', NET_VALIDATE_PERSISTED_FIELDS),
            ('PasswordMatched', BOOLEAN),
        ]

        # If password change type of check is to be made,
        # this kind of input must be used
        # InputPersistedFields: Information about the account to be logged
        # into
        # ClearPassword: The string which password is going to be
        # UserAccountName: Name of the user account
        # HashedPassword: Hash of the string that the password is going to
        # be
        # PasswordMatch: denotes if the old password supplied by user
        # matched or not
        _NET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG._fields_ = [
            ('InputPersistedFields', NET_VALIDATE_PERSISTED_FIELDS),
            ('ClearPassword', LPWSTR),
            ('UserAccountName', LPWSTR),
            ('HashedPassword', NET_VALIDATE_PASSWORD_HASH),
            ('PasswordMatch', BOOLEAN),
        ]

        # If password reset type of check is to be made,
        # this kind of input must be used
        # InputPersistedFields: Information about the account to be logged
        # into
        # ClearPassword: The string which password is going to be
        # UserAccountName: Name of the user account
        # HashedPassword: Hash of the string that the password is going to
        # be
        # PasswordMustChangeAtNextLogon: Password must change for the user
        # to be logged in
        # ClearLockout: If the account was locked out, this field can be
        # used to clear lockout
        _NET_VALIDATE_PASSWORD_RESET_INPUT_ARG._fields_ = [
            ('InputPersistedFields', NET_VALIDATE_PERSISTED_FIELDS),
            ('ClearPassword', LPWSTR),
            ('UserAccountName', LPWSTR),
            ('HashedPassword', NET_VALIDATE_PASSWORD_HASH),
            ('PasswordMustChangeAtNextLogon', BOOLEAN),
            ('ClearLockout', BOOLEAN),
        ]

        # Password Checking API structures end here

        # NET_API_STATUS NET_API_FUNCTION
        # NetValidatePasswordPolicy(
        # IN LPCWSTR ServerName,
        # IN LPVOID Qualifier,
        # IN NET_VALIDATE_PASSWORD_TYPE ValidationType,
        # IN LPVOID InputArg,
        # OUT LPVOID *OutputArg
        # );
        NetValidatePasswordPolicy = netapi32.NetValidatePasswordPolicy
        NetValidatePasswordPolicy.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetValidatePasswordPolicyFree(
        # IN LPVOID *OutputArg
        # );
        NetValidatePasswordPolicyFree = (
            netapi32.NetValidatePasswordPolicyFree
        )
        NetValidatePasswordPolicyFree.restype = NET_API_STATUS

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF   _LMACCESS_

# Domain Class
if not defined(_LMDOMAIN_):
    _LMDOMAIN_ = VOID

    if WINAPI_FAMILY_PARTITION(
        WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # Function Prototypes - Domain

        # NET_API_STATUS NET_API_FUNCTION
        # NetGetDCName(
        # _In_opt_ IN  LPCWSTR   servername OPTIONAL,
        # _In_opt_ IN  LPCWSTR   domainname OPTIONAL,
        # _At_((LPWSTR *)bufptr, _Outptr_result_z_) LPBYTE  *bufptr
        # );
        NetGetDCName = netapi32.NetGetDCName
        NetGetDCName.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetGetAnyDCName(
        # _In_opt_ IN  LPCWSTR   servername OPTIONAL,
        # _In_opt_ IN  LPCWSTR   domainname OPTIONAL,
        # _At_((LPWSTR *)bufptr, _Outptr_result_z_) LPBYTE  *bufptr
        # );
        NetGetAnyDCName = netapi32.NetGetAnyDCName
        NetGetAnyDCName.restype = NET_API_STATUS

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

        # NET_API_STATUS NET_API_FUNCTION
        # I_NetLogonControl(
        # _In_opt_ LPCWSTR ServerName OPTIONAL,
        # _In_     DWORD FunctionCode,
        # _In_     DWORD QueryLevel,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE *Buffer
        # );
        I_NetLogonControl = netapi32.I_NetLogonControl
        I_NetLogonControl.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # I_NetLogonControl2(
        # _In_opt_ LPCWSTR ServerName OPTIONAL,
        # _In_     DWORD FunctionCode,
        # _In_     DWORD QueryLevel,
        # _In_reads_(_Inexpressible_("varies")) LPBYTE Data,
        # _Outptr_result_buffer_(_Inexpressible_("varies")) LPBYTE *Buffer
        # );
        I_NetLogonControl2 = netapi32.I_NetLogonControl2
        I_NetLogonControl2.restype = NET_API_STATUS

        if not defined(_NTDEF_):
            # typedef _Return_type_success_(return >= 0) LONG NTSTATUS, *PNTSTATUS;
            pass

        # END IF

        # NTSTATUS NET_API_FUNCTION
        # NetEnumerateTrustedDomains(
        # _In_opt_ IN LPWSTR ServerName OPTIONAL,
        # _Outptr_ OUT LPWSTR *DomainNames
        # );
        NetEnumerateTrustedDomains = netapi32.NetEnumerateTrustedDomains
        NetEnumerateTrustedDomains.restype = NTSTATUS

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(
        WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # Special Values and Constants - Domain
        # FunctionCode values for I_NetLogonControl.
        # NOTE : if you change the following NETLOGON_CONTROL_* values,
        # change them in net\svcdlls\logonsrv\logon.idl file also.
        NETLOGON_CONTROL_QUERY = 1  # No-op: just query
        NETLOGON_CONTROL_REPLICATE = 2  # Force replicate on BDC
        NETLOGON_CONTROL_SYNCHRONIZE = 3  # Force synchronize on BDC
        NETLOGON_CONTROL_PDC_REPLICATE = 4  # Force PDC to broadcast change
        NETLOGON_CONTROL_REDISCOVER = 5  # Force to re-discover trusted domain DCs
        NETLOGON_CONTROL_TC_QUERY = 6  # Query status of specified trusted channel status
        NETLOGON_CONTROL_TRANSPORT_NOTIFY = 7  # Notify netlogon that a new transport has come online
        NETLOGON_CONTROL_FIND_USER = 8  # Find named user in a trusted domain
        NETLOGON_CONTROL_CHANGE_PASSWORD = 9  # Change machine password on a secure channel to a trusted domain
        NETLOGON_CONTROL_TC_VERIFY = 10  # Verify status of specified trusted channel
        NETLOGON_CONTROL_FORCE_DNS_REG = 11  # Force DNS re-registration of all registered records
        NETLOGON_CONTROL_QUERY_DNS_REG = 12  # Query the status of DNS updates
        NETLOGON_CONTROL_QUERY_ENC_TYPES = 13  # Query the supported encryption types

        # Debug function codes
        NETLOGON_CONTROL_UNLOAD_NETLOGON_DLL = 0xFFFB
        NETLOGON_CONTROL_BACKUP_CHANGE_LOG = 0xFFFC
        NETLOGON_CONTROL_TRUNCATE_LOG = 0xFFFD
        NETLOGON_CONTROL_SET_DBFLAG = 0xFFFE
        NETLOGON_CONTROL_BREAKPOINT = 0xFFFF

        # Query level 1 for I_NetLogonControl
        _NETLOGON_INFO_1._fields_ = [
            ('netlog1_flags', DWORD),
            ('netlog1_pdc_connection_status', NET_API_STATUS),
        ]

        _TEMP__NETLOGON_INFO_2 = [
            ('netlog2_flags', DWORD),
            # (useful for BDCs only).
            ('netlog2_pdc_connection_status', NET_API_STATUS),
        ]
        if defined(MIDL_PASS):
            _TEMP__NETLOGON_INFO_2 += [
                ('netlog2_trusted_dc_name', POINTER(WCHAR)),
            ]
        else:
            _TEMP__NETLOGON_INFO_2 += [
                ('netlog2_trusted_dc_name', LPWSTR),
            ]
        # END IF   MIDL_PASS

        _TEMP__NETLOGON_INFO_2 += [
            ('netlog2_tc_connection_status', NET_API_STATUS),
        ]
        _NETLOGON_INFO_2._fields_ = _TEMP__NETLOGON_INFO_2

        _NETLOGON_INFO_3._fields_ = [
            ('netlog3_flags', DWORD),
            ('netlog3_logon_attempts', DWORD),
            ('netlog3_reserved1', DWORD),
            ('netlog3_reserved2', DWORD),
            ('netlog3_reserved3', DWORD),
            ('netlog3_reserved4', DWORD),
            ('netlog3_reserved5', DWORD),
        ]

        _TEMP__NETLOGON_INFO_4 = [
        ]
        if defined(MIDL_PASS):
            _TEMP__NETLOGON_INFO_4 += [
                ('netlog4_trusted_dc_name', POINTER(WCHAR)),
                ('netlog4_trusted_domain_name', POINTER(WCHAR)),
            ]
        else:
            _TEMP__NETLOGON_INFO_4 += [
                ('netlog4_trusted_dc_name', LPWSTR),
                ('netlog4_trusted_domain_name', LPWSTR),
            ]
        # END IF   MIDL_PASS

        _NETLOGON_INFO_4._fields_ = _TEMP__NETLOGON_INFO_4

        # Values of netlog1_flags
        NETLOGON_REPLICATION_NEEDED = 0x01  # Database is out of date
        NETLOGON_REPLICATION_IN_PROGRESS = 0x02  # Replication is happening now
        NETLOGON_FULL_SYNC_REPLICATION = 0x04  # full sync replication required/progress
        NETLOGON_REDO_NEEDED = 0x08  # Redo of previous replication needed
        NETLOGON_HAS_IP = 0x10  # The trusted domain DC has an IP address
        NETLOGON_HAS_TIMESERV = 0x20  # The trusted domain DC runs the Windows Time Service
        NETLOGON_DNS_UPDATE_FAILURE = 0x40  # There was a failure in the last update for one of the DNS records

        # Trust verification status returned in
        # netlog2_pdc_connection_status
        NETLOGON_VERIFY_STATUS_RETURNED = 0x80
        SERVICE_ACCOUNT_PASSWORD = (
            TEXT("_SA_[262E99C9-6160-4871-ACEC-4E61736B6F21]")
        )
        SERVICE_ACCOUNT_SECRET_PREFIX = (
            TEXT("_SC_[262E99C9-6160-4871-ACEC-4E61736B6F21]_")
        )
        # 262e99c9-6160-4871-acec-4e61736b6f21
        ServiceAccountPasswordGUID = DEFINE_GUID(
            0x262E99C9,
            0x6160,
            0x4871,
            0xAC,
            0xEC,
            0x4E,
            0x61,
            0x73,
            0x6B,
            0x6F,
            0x21
        )

        # NTSTATUS
        # NetAddServiceAccount(
        # _In_opt_ LPWSTR ServerName,
        # _In_ LPWSTR AccountName,
        # _In_ LPWSTR Password,
        # _In_ DWORD Flags);
        NetAddServiceAccount = netapi32.NetAddServiceAccount
        NetAddServiceAccount.restype = NTSTATUS

        # Do not create an account by this name
        # Only link this account to my computer if it exists
        SERVICE_ACCOUNT_FLAG_LINK_TO_HOST_ONLY = 0x00000001

        # Add the service account against an RODC
        # The account must already exist and be linked
        # The third parameter contains the preset password
        SERVICE_ACCOUNT_FLAG_ADD_AGAINST_RODC = 0x00000002

        # Do not delete the service account object from AD
        # Simply unlink it from this computer and delete the local secret
        SERVICE_ACCOUNT_FLAG_UNLINK_FROM_HOST_ONLY = 0x00000001

        # Remove the account from password management on the local
        # machine. The DC is unavailable or read-only so do not
        # attempt to unlink or delete the account
        SERVICE_ACCOUNT_FLAG_REMOVE_OFFLINE = 0x00000002

        # NTSTATUS
        # NetRemoveServiceAccount(
        # _In_opt_ LPWSTR ServerName,
        # _In_ LPWSTR AccountName,
        # _In_ DWORD Flags);
        NetRemoveServiceAccount = netapi32.NetRemoveServiceAccount
        NetRemoveServiceAccount.restype = NTSTATUS

        # NTSTATUS
        # NetEnumerateServiceAccounts(
        # _In_opt_ LPWSTR ServerName,
        # _In_ DWORD Flags,
        # _Out_ DWORD* AccountsCount,
        # _Outptr_result_buffer_(*AccountsCount) PZPWSTR* Accounts);
        NetEnumerateServiceAccounts = netapi32.NetEnumerateServiceAccounts
        NetEnumerateServiceAccounts.restype = NTSTATUS

        # NTSTATUS
        # NetIsServiceAccount(
        # _In_opt_ LPWSTR ServerName,
        # _In_ LPWSTR AccountName,
        # _Out_ BOOL *IsService);
        NetIsServiceAccount = netapi32.NetIsServiceAccount
        NetIsServiceAccount.restype = NTSTATUS

        # NTSTATUS
        # NetQueryServiceAccount(
        # _In_opt_ LPWSTR ServerName,
        # _In_ LPWSTR AccountName,
        # _In_ DWORD InfoLevel,
        # _Outptr_ PBYTE* Buffer);
        NetQueryServiceAccount = netapi32.NetQueryServiceAccount
        NetQueryServiceAccount.restype = NTSTATUS


        # Data Structures - Service
        class _MSA_INFO_LEVEL(ENUM):
            MsaInfoLevel0 = 0
            MsaInfoLevelMax = 1


        MSA_INFO_LEVEL = _MSA_INFO_LEVEL
        PMSA_INFO_LEVEL = POINTER(_MSA_INFO_LEVEL)


        class _MSA_INFO_STATE(ENUM):
            MsaInfoNotExist = 1
            MsaInfoNotService = 2
            MsaInfoCannotInstall = 3
            MsaInfoCanInstall = 4
            MsaInfoInstalled = 5


        MSA_INFO_STATE = _MSA_INFO_STATE
        PMSA_INFO_STATE = POINTER(_MSA_INFO_STATE)

        _MSA_INFO_0._fields_ = [
            ('State', MSA_INFO_STATE),
        ]
        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF   _LMDOMAIN_


