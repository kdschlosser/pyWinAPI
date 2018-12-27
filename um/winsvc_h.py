import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_WINSVC_ = None
WINADVAPI = None
_ADVAPI32_ = None

class SERVICE_TRIGGER_CUSTOM_STATE_ID(ctypes.Structure):
    pass





class _SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM(ctypes.Structure):
    pass


SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM = _SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM
LPSERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM = POINTER(_SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM)


class _SERVICE_DESCRIPTIONA(ctypes.Structure):
    pass


SERVICE_DESCRIPTIONA = _SERVICE_DESCRIPTIONA
LPSERVICE_DESCRIPTIONA = POINTER(_SERVICE_DESCRIPTIONA)


class _SERVICE_DESCRIPTIONW(ctypes.Structure):
    pass


SERVICE_DESCRIPTIONW = _SERVICE_DESCRIPTIONW
LPSERVICE_DESCRIPTIONW = POINTER(_SERVICE_DESCRIPTIONW)


class _SC_ACTION(ctypes.Structure):
    pass


SC_ACTION = _SC_ACTION
LPSC_ACTION = POINTER(_SC_ACTION)


class _SERVICE_FAILURE_ACTIONSA(ctypes.Structure):
    pass


SERVICE_FAILURE_ACTIONSA = _SERVICE_FAILURE_ACTIONSA
LPSERVICE_FAILURE_ACTIONSA = POINTER(_SERVICE_FAILURE_ACTIONSA)


class _SERVICE_FAILURE_ACTIONSW(ctypes.Structure):
    pass


SERVICE_FAILURE_ACTIONSW = _SERVICE_FAILURE_ACTIONSW
LPSERVICE_FAILURE_ACTIONSW = POINTER(_SERVICE_FAILURE_ACTIONSW)


class _SERVICE_DELAYED_AUTO_START_INFO(ctypes.Structure):
    pass


SERVICE_DELAYED_AUTO_START_INFO = _SERVICE_DELAYED_AUTO_START_INFO
LPSERVICE_DELAYED_AUTO_START_INFO = POINTER(_SERVICE_DELAYED_AUTO_START_INFO)


class _SERVICE_FAILURE_ACTIONS_FLAG(ctypes.Structure):
    pass


SERVICE_FAILURE_ACTIONS_FLAG = _SERVICE_FAILURE_ACTIONS_FLAG
LPSERVICE_FAILURE_ACTIONS_FLAG = POINTER(_SERVICE_FAILURE_ACTIONS_FLAG)


class _SERVICE_SID_INFO(ctypes.Structure):
    pass


SERVICE_SID_INFO = _SERVICE_SID_INFO
LPSERVICE_SID_INFO = POINTER(_SERVICE_SID_INFO)


class _SERVICE_REQUIRED_PRIVILEGES_INFOA(ctypes.Structure):
    pass


SERVICE_REQUIRED_PRIVILEGES_INFOA = _SERVICE_REQUIRED_PRIVILEGES_INFOA
LPSERVICE_REQUIRED_PRIVILEGES_INFOA = POINTER(_SERVICE_REQUIRED_PRIVILEGES_INFOA)


class _SERVICE_REQUIRED_PRIVILEGES_INFOW(ctypes.Structure):
    pass


SERVICE_REQUIRED_PRIVILEGES_INFOW = _SERVICE_REQUIRED_PRIVILEGES_INFOW
LPSERVICE_REQUIRED_PRIVILEGES_INFOW = POINTER(_SERVICE_REQUIRED_PRIVILEGES_INFOW)


class _SERVICE_PRESHUTDOWN_INFO(ctypes.Structure):
    pass


SERVICE_PRESHUTDOWN_INFO = _SERVICE_PRESHUTDOWN_INFO
LPSERVICE_PRESHUTDOWN_INFO = POINTER(_SERVICE_PRESHUTDOWN_INFO)


class _SERVICE_TRIGGER_SPECIFIC_DATA_ITEM(ctypes.Structure):
    pass


SERVICE_TRIGGER_SPECIFIC_DATA_ITEM = _SERVICE_TRIGGER_SPECIFIC_DATA_ITEM
PSERVICE_TRIGGER_SPECIFIC_DATA_ITEM = POINTER(_SERVICE_TRIGGER_SPECIFIC_DATA_ITEM)


class _SERVICE_TRIGGER(ctypes.Structure):
    pass


SERVICE_TRIGGER = _SERVICE_TRIGGER
PSERVICE_TRIGGER = POINTER(_SERVICE_TRIGGER)


class _SERVICE_TRIGGER_INFO(ctypes.Structure):
    pass


SERVICE_TRIGGER_INFO = _SERVICE_TRIGGER_INFO
PSERVICE_TRIGGER_INFO = POINTER(_SERVICE_TRIGGER_INFO)


class _SERVICE_PREFERRED_NODE_INFO(ctypes.Structure):
    pass


SERVICE_PREFERRED_NODE_INFO = _SERVICE_PREFERRED_NODE_INFO
LPSERVICE_PREFERRED_NODE_INFO = POINTER(_SERVICE_PREFERRED_NODE_INFO)


class _SERVICE_TIMECHANGE_INFO(ctypes.Structure):
    pass


SERVICE_TIMECHANGE_INFO = _SERVICE_TIMECHANGE_INFO
PSERVICE_TIMECHANGE_INFO = POINTER(_SERVICE_TIMECHANGE_INFO)


class _SERVICE_LAUNCH_PROTECTED_INFO(ctypes.Structure):
    pass


SERVICE_LAUNCH_PROTECTED_INFO = _SERVICE_LAUNCH_PROTECTED_INFO
PSERVICE_LAUNCH_PROTECTED_INFO = POINTER(_SERVICE_LAUNCH_PROTECTED_INFO)


class _SERVICE_STATUS(ctypes.Structure):
    pass


SERVICE_STATUS = _SERVICE_STATUS
LPSERVICE_STATUS = POINTER(_SERVICE_STATUS)


class _SERVICE_STATUS_PROCESS(ctypes.Structure):
    pass


SERVICE_STATUS_PROCESS = _SERVICE_STATUS_PROCESS
LPSERVICE_STATUS_PROCESS = POINTER(_SERVICE_STATUS_PROCESS)


class _ENUM_SERVICE_STATUSA(ctypes.Structure):
    pass


ENUM_SERVICE_STATUSA = _ENUM_SERVICE_STATUSA
LPENUM_SERVICE_STATUSA = POINTER(_ENUM_SERVICE_STATUSA)


class _ENUM_SERVICE_STATUSW(ctypes.Structure):
    pass


ENUM_SERVICE_STATUSW = _ENUM_SERVICE_STATUSW
LPENUM_SERVICE_STATUSW = POINTER(_ENUM_SERVICE_STATUSW)


class _ENUM_SERVICE_STATUS_PROCESSA(ctypes.Structure):
    pass


ENUM_SERVICE_STATUS_PROCESSA = _ENUM_SERVICE_STATUS_PROCESSA
LPENUM_SERVICE_STATUS_PROCESSA = POINTER(_ENUM_SERVICE_STATUS_PROCESSA)


class _ENUM_SERVICE_STATUS_PROCESSW(ctypes.Structure):
    pass


ENUM_SERVICE_STATUS_PROCESSW = _ENUM_SERVICE_STATUS_PROCESSW
LPENUM_SERVICE_STATUS_PROCESSW = POINTER(_ENUM_SERVICE_STATUS_PROCESSW)


class _QUERY_SERVICE_LOCK_STATUSA(ctypes.Structure):
    pass


QUERY_SERVICE_LOCK_STATUSA = _QUERY_SERVICE_LOCK_STATUSA
LPQUERY_SERVICE_LOCK_STATUSA = POINTER(_QUERY_SERVICE_LOCK_STATUSA)


class _QUERY_SERVICE_LOCK_STATUSW(ctypes.Structure):
    pass


QUERY_SERVICE_LOCK_STATUSW = _QUERY_SERVICE_LOCK_STATUSW
LPQUERY_SERVICE_LOCK_STATUSW = POINTER(_QUERY_SERVICE_LOCK_STATUSW)


class _QUERY_SERVICE_CONFIGA(ctypes.Structure):
    pass


QUERY_SERVICE_CONFIGA = _QUERY_SERVICE_CONFIGA
LPQUERY_SERVICE_CONFIGA = POINTER(_QUERY_SERVICE_CONFIGA)


class _QUERY_SERVICE_CONFIGW(ctypes.Structure):
    pass


QUERY_SERVICE_CONFIGW = _QUERY_SERVICE_CONFIGW
LPQUERY_SERVICE_CONFIGW = POINTER(_QUERY_SERVICE_CONFIGW)


class _SERVICE_TABLE_ENTRYA(ctypes.Structure):
    pass


SERVICE_TABLE_ENTRYA = _SERVICE_TABLE_ENTRYA
LPSERVICE_TABLE_ENTRYA = POINTER(_SERVICE_TABLE_ENTRYA)


class _SERVICE_TABLE_ENTRYW(ctypes.Structure):
    pass


SERVICE_TABLE_ENTRYW = _SERVICE_TABLE_ENTRYW
LPSERVICE_TABLE_ENTRYW = POINTER(_SERVICE_TABLE_ENTRYW)


class _SERVICE_NOTIFY_1(ctypes.Structure):
    pass


SERVICE_NOTIFY_1 = _SERVICE_NOTIFY_1
PSERVICE_NOTIFY_1 = POINTER(_SERVICE_NOTIFY_1)


class _SERVICE_NOTIFY_2A(ctypes.Structure):
    pass


SERVICE_NOTIFY_2A = _SERVICE_NOTIFY_2A
PSERVICE_NOTIFY_2A = POINTER(_SERVICE_NOTIFY_2A)


class _SERVICE_NOTIFY_2W(ctypes.Structure):
    pass


SERVICE_NOTIFY_2W = _SERVICE_NOTIFY_2W
PSERVICE_NOTIFY_2W = POINTER(_SERVICE_NOTIFY_2W)


class _SERVICE_CONTROL_STATUS_REASON_PARAMSA(ctypes.Structure):
    pass


SERVICE_CONTROL_STATUS_REASON_PARAMSA = _SERVICE_CONTROL_STATUS_REASON_PARAMSA
PSERVICE_CONTROL_STATUS_REASON_PARAMSA = POINTER(_SERVICE_CONTROL_STATUS_REASON_PARAMSA)


class _SERVICE_CONTROL_STATUS_REASON_PARAMSW(ctypes.Structure):
    pass


SERVICE_CONTROL_STATUS_REASON_PARAMSW = _SERVICE_CONTROL_STATUS_REASON_PARAMSW
PSERVICE_CONTROL_STATUS_REASON_PARAMSW = POINTER(_SERVICE_CONTROL_STATUS_REASON_PARAMSW)


class _SERVICE_START_REASON(ctypes.Structure):
    pass


SERVICE_START_REASON = _SERVICE_START_REASON
PSERVICE_START_REASON = POINTER(_SERVICE_START_REASON)


# /* + + BUILD Version: 0010 // Increment this if a change has global effects
# Copyright (c) 1995-1998 Microsoft Corporation Module Name: winsvc.h
# Abstract: Header file for the Service Control Manager Environment: User Mode
# - Win32 --
if not defined(_WINSVC_):
    _WINSVC_ = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.um.winnt_h import * # NOQA

    # Define API decoration for direct importing of DLL references.
    if not defined(WINADVAPI):
        if not defined(_ADVAPI32_):
            WINADVAPI = DECLSPEC_IMPORT
        else:
            WINADVAPI = VOID
        # END IF
    # END IF

    if _MSC_VER >= 1200:
        pass
    # END IF

    if defined(__cplusplus):
        pass
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # Constants
        # Service database names
        SERVICES_ACTIVE_DATABASEW = "ServicesActive"
        SERVICES_FAILED_DATABASEW = "ServicesFailed"
        SERVICES_ACTIVE_DATABASEA = "ServicesActive"
        SERVICES_FAILED_DATABASEA = "ServicesFailed"


        # Character to designate that a name is a group
        SC_GROUP_IDENTIFIERW = ' + '
        SC_GROUP_IDENTIFIERA = ' + '

        if defined(UNICODE):
            SERVICES_ACTIVE_DATABASE = SERVICES_ACTIVE_DATABASEW
            SERVICES_FAILED_DATABASE = SERVICES_FAILED_DATABASEW
            SC_GROUP_IDENTIFIER = SC_GROUP_IDENTIFIERW
        else:
            SERVICES_ACTIVE_DATABASE = SERVICES_ACTIVE_DATABASEA
            SERVICES_FAILED_DATABASE = SERVICES_FAILED_DATABASEA
            SC_GROUP_IDENTIFIER = SC_GROUP_IDENTIFIERA
        # END IF   ndef UNICODE

        # Value to indicate no change to an optional parameter
        SERVICE_NO_CHANGE = 0xFFFFFFFF

        # Service State -- for Enum Requests (Bit Mask)
        SERVICE_ACTIVE = 0x00000001
        SERVICE_INACTIVE = 0x00000002
        SERVICE_STATE_ALL = SERVICE_ACTIVE | SERVICE_INACTIVE

        # Controls
        SERVICE_CONTROL_STOP = 0x00000001
        SERVICE_CONTROL_PAUSE = 0x00000002
        SERVICE_CONTROL_CONTINUE = 0x00000003
        SERVICE_CONTROL_INTERROGATE = 0x00000004
        SERVICE_CONTROL_SHUTDOWN = 0x00000005
        SERVICE_CONTROL_PARAMCHANGE = 0x00000006
        SERVICE_CONTROL_NETBINDADD = 0x00000007
        SERVICE_CONTROL_NETBINDREMOVE = 0x00000008
        SERVICE_CONTROL_NETBINDENABLE = 0x00000009
        SERVICE_CONTROL_NETBINDDISABLE = 0x0000000A
        SERVICE_CONTROL_DEVICEEVENT = 0x0000000B
        SERVICE_CONTROL_HARDWAREPROFILECHANGE = 0x0000000C
        SERVICE_CONTROL_POWEREVENT = 0x0000000D
        SERVICE_CONTROL_SESSIONCHANGE = 0x0000000E
        SERVICE_CONTROL_PRESHUTDOWN = 0x0000000F
        SERVICE_CONTROL_TIMECHANGE = 0x00000010

        # define SERVICE_CONTROL_USER_LOGOFF  0x00000011
        SERVICE_CONTROL_TRIGGEREVENT = 0x00000020

        # reserved for internal use    0x00000021
        # reserved for internal use    0x00000050
        SERVICE_CONTROL_LOWRESOURCES = 0x00000060
        SERVICE_CONTROL_SYSTEMLOWRESOURCES = 0x00000061

        # Service State -- for CurrentState
        SERVICE_STOPPED = 0x00000001
        SERVICE_START_PENDING = 0x00000002
        SERVICE_STOP_PENDING = 0x00000003
        SERVICE_RUNNING = 0x00000004
        SERVICE_CONTINUE_PENDING = 0x00000005
        SERVICE_PAUSE_PENDING = 0x00000006
        SERVICE_PAUSED = 0x00000007

        # Controls Accepted (Bit Mask)
        SERVICE_ACCEPT_STOP = 0x00000001
        SERVICE_ACCEPT_PAUSE_CONTINUE = 0x00000002
        SERVICE_ACCEPT_SHUTDOWN = 0x00000004
        SERVICE_ACCEPT_PARAMCHANGE = 0x00000008
        SERVICE_ACCEPT_NETBINDCHANGE = 0x00000010
        SERVICE_ACCEPT_HARDWAREPROFILECHANGE = 0x00000020
        SERVICE_ACCEPT_POWEREVENT = 0x00000040
        SERVICE_ACCEPT_SESSIONCHANGE = 0x00000080
        SERVICE_ACCEPT_PRESHUTDOWN = 0x00000100
        SERVICE_ACCEPT_TIMECHANGE = 0x00000200
        SERVICE_ACCEPT_TRIGGEREVENT = 0x00000400
        SERVICE_ACCEPT_USER_LOGOFF = 0x00000800

        # reserved for internal use    0x00001000
        SERVICE_ACCEPT_LOWRESOURCES = 0x00002000
        SERVICE_ACCEPT_SYSTEMLOWRESOURCES = 0x00004000

        # Service Control Manager object specific access types
        SC_MANAGER_CONNECT = 0x0001
        SC_MANAGER_CREATE_SERVICE = 0x0002
        SC_MANAGER_ENUMERATE_SERVICE = 0x0004
        SC_MANAGER_LOCK = 0x0008
        SC_MANAGER_QUERY_LOCK_STATUS = 0x0010
        SC_MANAGER_MODIFY_BOOT_CONFIG = 0x0020
        SC_MANAGER_ALL_ACCESS = (
            STANDARD_RIGHTS_REQUIRED |
            SC_MANAGER_CONNECT |
            SC_MANAGER_CREATE_SERVICE |
            SC_MANAGER_ENUMERATE_SERVICE |
            SC_MANAGER_LOCK |
            SC_MANAGER_QUERY_LOCK_STATUS |
            SC_MANAGER_MODIFY_BOOT_CONFIG
        )

        # Service object specific access type
        SERVICE_QUERY_CONFIG = 0x0001
        SERVICE_CHANGE_CONFIG = 0x0002
        SERVICE_QUERY_STATUS = 0x0004
        SERVICE_ENUMERATE_DEPENDENTS = 0x0008
        SERVICE_START = 0x0010
        SERVICE_STOP = 0x0020
        SERVICE_PAUSE_CONTINUE = 0x0040
        SERVICE_INTERROGATE = 0x0080
        SERVICE_USER_DEFINED_CONTROL = 0x0100
        SERVICE_ALL_ACCESS = (
            STANDARD_RIGHTS_REQUIRED |
            SERVICE_QUERY_CONFIG |
            SERVICE_CHANGE_CONFIG |
            SERVICE_QUERY_STATUS |
            SERVICE_ENUMERATE_DEPENDENTS |
            SERVICE_START |
            SERVICE_STOP |
            SERVICE_PAUSE_CONTINUE |
            SERVICE_INTERROGATE |
            SERVICE_USER_DEFINED_CONTROL
        )


        # Service flags for QueryServiceStatusEx
        SERVICE_RUNS_IN_SYSTEM_PROCESS = 0x00000001


        # Info levels for ChangeServiceConfig2 and QueryServiceConfig2
        SERVICE_CONFIG_DESCRIPTION = 1
        SERVICE_CONFIG_FAILURE_ACTIONS = 2
        SERVICE_CONFIG_DELAYED_AUTO_START_INFO = 3
        SERVICE_CONFIG_FAILURE_ACTIONS_FLAG = 4
        SERVICE_CONFIG_SERVICE_SID_INFO = 5
        SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO = 6
        SERVICE_CONFIG_PRESHUTDOWN_INFO = 7
        SERVICE_CONFIG_TRIGGER_INFO = 8
        SERVICE_CONFIG_PREFERRED_NODE = 9

        # reserved       10
        # reserved       11
        SERVICE_CONFIG_LAUNCH_PROTECTED = 12


        # Info levels for NotifyServiceStatusChange
        SERVICE_NOTIFY_STATUS_CHANGE_1 = 1
        SERVICE_NOTIFY_STATUS_CHANGE_2 = 2
        SERVICE_NOTIFY_STATUS_CHANGE = SERVICE_NOTIFY_STATUS_CHANGE_2


        # Service notification masks
        SERVICE_NOTIFY_STOPPED = 0x00000001
        SERVICE_NOTIFY_START_PENDING = 0x00000002
        SERVICE_NOTIFY_STOP_PENDING = 0x00000004
        SERVICE_NOTIFY_RUNNING = 0x00000008
        SERVICE_NOTIFY_CONTINUE_PENDING = 0x00000010
        SERVICE_NOTIFY_PAUSE_PENDING = 0x00000020
        SERVICE_NOTIFY_PAUSED = 0x00000040
        SERVICE_NOTIFY_CREATED = 0x00000080
        SERVICE_NOTIFY_DELETED = 0x00000100
        SERVICE_NOTIFY_DELETE_PENDING = 0x00000200


        # The following defines are for service stop reason codes
        # Stop reason flags. Update SERVICE_STOP_REASON_FLAG_MAX when
        # new flags are added.
        SERVICE_STOP_REASON_FLAG_MIN = 0x00000000
        SERVICE_STOP_REASON_FLAG_UNPLANNED = 0x10000000
        SERVICE_STOP_REASON_FLAG_CUSTOM = 0x20000000
        SERVICE_STOP_REASON_FLAG_PLANNED = 0x40000000
        SERVICE_STOP_REASON_FLAG_MAX = 0x80000000


        # Microsoft major reasons. Update SERVICE_STOP_REASON_MAJOR_MAX when
        # new codes are added.
        SERVICE_STOP_REASON_MAJOR_MIN = 0x00000000
        SERVICE_STOP_REASON_MAJOR_OTHER = 0x00010000
        SERVICE_STOP_REASON_MAJOR_HARDWARE = 0x00020000
        SERVICE_STOP_REASON_MAJOR_OPERATINGSYSTEM = 0x00030000
        SERVICE_STOP_REASON_MAJOR_SOFTWARE = 0x00040000
        SERVICE_STOP_REASON_MAJOR_APPLICATION = 0x00050000
        SERVICE_STOP_REASON_MAJOR_NONE = 0x00060000
        SERVICE_STOP_REASON_MAJOR_MAX = 0x00070000
        SERVICE_STOP_REASON_MAJOR_MIN_CUSTOM = 0x00400000
        SERVICE_STOP_REASON_MAJOR_MAX_CUSTOM = 0x00FF0000


        # Microsoft minor reasons. Update SERVICE_STOP_REASON_MINOR_MAX when
        # new codes are added.
        SERVICE_STOP_REASON_MINOR_MIN = 0x00000000
        SERVICE_STOP_REASON_MINOR_OTHER = 0x00000001
        SERVICE_STOP_REASON_MINOR_MAINTENANCE = 0x00000002
        SERVICE_STOP_REASON_MINOR_INSTALLATION = 0x00000003
        SERVICE_STOP_REASON_MINOR_UPGRADE = 0x00000004
        SERVICE_STOP_REASON_MINOR_RECONFIG = 0x00000005
        SERVICE_STOP_REASON_MINOR_HUNG = 0x00000006
        SERVICE_STOP_REASON_MINOR_UNSTABLE = 0x00000007
        SERVICE_STOP_REASON_MINOR_DISK = 0x00000008
        SERVICE_STOP_REASON_MINOR_NETWORKCARD = 0x00000009
        SERVICE_STOP_REASON_MINOR_ENVIRONMENT = 0x0000000A
        SERVICE_STOP_REASON_MINOR_HARDWARE_DRIVER = 0x0000000B
        SERVICE_STOP_REASON_MINOR_OTHERDRIVER = 0x0000000C
        SERVICE_STOP_REASON_MINOR_SERVICEPACK = 0x0000000D
        SERVICE_STOP_REASON_MINOR_SOFTWARE_UPDATE = 0x0000000E
        SERVICE_STOP_REASON_MINOR_SECURITYFIX = 0x0000000F
        SERVICE_STOP_REASON_MINOR_SECURITY = 0x00000010
        SERVICE_STOP_REASON_MINOR_NETWORK_CONNECTIVITY = 0x00000011
        SERVICE_STOP_REASON_MINOR_WMI = 0x00000012
        SERVICE_STOP_REASON_MINOR_SERVICEPACK_UNINSTALL = 0x00000013
        SERVICE_STOP_REASON_MINOR_SOFTWARE_UPDATE_UNINSTALL = 0x00000014
        SERVICE_STOP_REASON_MINOR_SECURITYFIX_UNINSTALL = 0x00000015
        SERVICE_STOP_REASON_MINOR_MMC = 0x00000016
        SERVICE_STOP_REASON_MINOR_NONE = 0x00000017
        SERVICE_STOP_REASON_MINOR_MEMOTYLIMIT = 0x00000018
        SERVICE_STOP_REASON_MINOR_MAX = 0x00000019
        SERVICE_STOP_REASON_MINOR_MIN_CUSTOM = 0x00000100
        SERVICE_STOP_REASON_MINOR_MAX_CUSTOM = 0x0000FFFF


        # Info levels for ControlServiceEx
        SERVICE_CONTROL_STATUS_REASON_INFO = 1


        # Service SID types supported
        SERVICE_SID_TYPE_NONE = 0x00000000
        SERVICE_SID_TYPE_UNRESTRICTED = 0x00000001
        SERVICE_SID_TYPE_RESTRICTED = (
            0x00000002 |
            SERVICE_SID_TYPE_UNRESTRICTED
        )


        # Service trigger types
        SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL = 1
        SERVICE_TRIGGER_TYPE_IP_ADDRESS_AVAILABILITY = 2
        SERVICE_TRIGGER_TYPE_DOMAIN_JOIN = 3
        SERVICE_TRIGGER_TYPE_FIREWALL_PORT_EVENT = 4
        SERVICE_TRIGGER_TYPE_GROUP_POLICY = 5
        SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT = 6
        SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE = 7
        SERVICE_TRIGGER_TYPE_CUSTOM = 20
        SERVICE_TRIGGER_TYPE_AGGREGATE = 30


        # Service trigger data types
        SERVICE_TRIGGER_DATA_TYPE_BINARY = 1
        SERVICE_TRIGGER_DATA_TYPE_STRING = 2
        SERVICE_TRIGGER_DATA_TYPE_LEVEL = 3
        SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ANY = 4
        SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ALL = 5


        # Service start reason
        SERVICE_START_REASON_DEMAND = 0x00000001
        SERVICE_START_REASON_AUTO = 0x00000002
        SERVICE_START_REASON_TRIGGER = 0x00000004
        SERVICE_START_REASON_RESTART_ON_FAILURE = 0x00000008
        SERVICE_START_REASON_DELAYEDAUTO = 0x00000010


        # Service dynamic information levels
        SERVICE_DYNAMIC_INFORMATION_LEVEL_START_REASON = 1


        # Service LaunchProtected types supported
        SERVICE_LAUNCH_PROTECTED_NONE = 0
        SERVICE_LAUNCH_PROTECTED_WINDOWS = 1
        SERVICE_LAUNCH_PROTECTED_WINDOWS_LIGHT = 2
        SERVICE_LAUNCH_PROTECTED_ANTIMALWARE_LIGHT = 3

        # NETWORK_MANAGER_FIRST_IP_ADDRESS_ARRIVAL_GUID &
        # NETWORK_MANAGER_LAST_IP_ADDRESS_REMOVAL_GUID are used with
        # SERVICE_TRIGGER_TYPE_IP_ADDRESS_AVAILABILITY trigger.
        # 4f27f2de-14e2-430b-a549-7cd48cbc8245
        NETWORK_MANAGER_FIRST_IP_ADDRESS_ARRIVAL_GUID = DEFINE_GUID(
            0x4F27F2DE,
            0x14E2,
            0x430B,
            0xA5,
            0x49,
            0x7C,
            0xD4,
            0x8C,
            0xBC,
            0x82,
            0x45
        )
        # cc4ba62a-162e-4648-847a-b6bdf993e335
        NETWORK_MANAGER_LAST_IP_ADDRESS_REMOVAL_GUID = DEFINE_GUID(
            0xCC4BA62A,
            0x162E,
            0x4648,
            0x84,
            0x7A,
            0xB6,
            0xBD,
            0xF9,
            0x93,
            0xE3,
            0x35
        )
        # DOMAIN_JOIN_GUID & DOMAIN_LEAVE_GUID are used with
        # SERVICE_TRIGGER_TYPE_DOMAIN_JOIN trigger.
        #1ce20aba-9851-4421-9430-1ddeb766e809
        DOMAIN_JOIN_GUID = DEFINE_GUID(
            0x1CE20ABA,
            0x9851,
            0x4421,
            0x94,
            0x30,
            0x1D,
            0xDE,
            0xB7,
            0x66,
            0xE8,
            0x09
        )
        # ddaf516e-58c2-4866-9574-c3b615d42ea1
        DOMAIN_LEAVE_GUID = DEFINE_GUID(
            0xDDAF516E,
            0x58C2,
            0x4866,
            0x95,
            0x74,
            0xC3,
            0xB6,
            0x15,
            0xD4,
            0x2E,
            0xA1
        )
        # FIREWALL_PORT_OPEN_GUID & FIREWALL_PORT_CLOSE_GUID are used with
        # SERVICE_TRIGGER_TYPE_FIREWALL_PORT_EVENT trigger.
        # b7569e07-8421-4ee0-ad10-86915afdad09
        FIREWALL_PORT_OPEN_GUID = DEFINE_GUID(
            0xB7569E07,
            0x8421,
            0x4EE0,
            0xAD,
            0x10,
            0x86,
            0x91,
            0x5A,
            0xFD,
            0xAD,
            0x09
        )
        # a144ed38-8e12-4de4-9d96-e64740b1a524
        FIREWALL_PORT_CLOSE_GUID = DEFINE_GUID(
            0xA144ED38,
            0x8E12,
            0x4DE4,
            0x9D,
            0x96,
            0xE6,
            0x47,
            0x40,
            0xB1,
            0xA5,
            0x24
        )
        # MACHINE_POLICY_PRESENT_GUID & USER_POLICY_PRESENT_GUID are used with
        # SERVICE_TRIGGER_TYPE_GROUP_POLICY trigger.
        # 659FCAE6-5BDB-4DA9-B1FF-CA2A178D46E0
        MACHINE_POLICY_PRESENT_GUID = DEFINE_GUID(
            0x659FCAE6,
            0x5BDB,
            0x4DA9,
            0xB1,
            0xFF,
            0xCA,
            0x2A,
            0x17,
            0x8D,
            0x46,
            0xE0
        )
        # 54FB46C8-F089-464C-B1FD-59D1B62C3B50
        USER_POLICY_PRESENT_GUID = DEFINE_GUID(
            0x54FB46C8,
            0xF089,
            0x464C,
            0xB1,
            0xFD,
            0x59,
            0xD1,
            0xB6,
            0x2C,
            0x3B,
            0x50
        )
        # RPC_INTERFACE_EVENT_GUID, NAMED_PIPE_EVENT_GUID &
        # TCP_PORT_EVENT_GUID are
        # used with SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT trigger.
        # bc90d167-9470-4139-a9ba-be0bbbf5b74d
        RPC_INTERFACE_EVENT_GUID = DEFINE_GUID(
            0xBC90D167,
            0x9470,
            0x4139,
            0xA9,
            0xBA,
            0xBE,
            0x0B,
            0xBB,
            0xF5,
            0xB7,
            0x4D
        )
        # 1f81d131-3fac-4537-9e0c-7e7b0c2f4b55
        NAMED_PIPE_EVENT_GUID = DEFINE_GUID(
            0x1F81D131,
            0x3FAC,
            0x4537,
            0x9E,
            0x0C,
            0x7E,
            0x7B,
            0x0C,
            0x2F,
            0x4B,
            0x55
        )
        # CUSTOM_SYSTEM_STATE_CHANGE_EVENT_GUID is used with
        # SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE
        # 2d7a2816-0c5e-45fc-9ce7-570e5ecde9c9
        CUSTOM_SYSTEM_STATE_CHANGE_EVENT_GUID = DEFINE_GUID(
            0x2D7A2816,
            0x0C5E,
            0x45FC,
            0x9C,
            0xE7,
            0x57,
            0x0E,
            0x5E,
            0xCD,
            0xE9,
            0xC9
        )
        # Service notification trigger identifier
        SERVICE_TRIGGER_CUSTOM_STATE_ID._fields_ = [
            ('Data', DWORD * 2),
        ]


        class u(ctypes.Union):
            pass


        class s(ctypes.Structure):
            pass


        s._fields_ = [
            ('DataOffset', DWORD),
            ('Data', BYTE * 1),
        ]
        u.s = s


        u._fields_ = [
            ('CustomStateId', SERVICE_TRIGGER_CUSTOM_STATE_ID),
            ('s', u.s),
        ]
        _SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM.u = u


        _SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM._fields_ = [
            ('u', _SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM.u),
        ]

        # Service trigger actions
        SERVICE_TRIGGER_ACTION_SERVICE_START = 1
        SERVICE_TRIGGER_ACTION_SERVICE_STOP = 2

        # argv[1] passed into ServiceMain of trigger started services
        SERVICE_TRIGGER_STARTED_ARGUMENT = "TriggerStarted"

        # Service description string
        _SERVICE_DESCRIPTIONA._fields_ = [
            ('lpDescription', LPSTR),
        ]

        # Service description string
        _SERVICE_DESCRIPTIONW._fields_ = [
            ('lpDescription', LPWSTR),
        ]
        if defined(UNICODE):
            SERVICE_DESCRIPTION = SERVICE_DESCRIPTIONW
            LPSERVICE_DESCRIPTION = LPSERVICE_DESCRIPTIONW
        else:
            SERVICE_DESCRIPTION = SERVICE_DESCRIPTIONA
            LPSERVICE_DESCRIPTION = LPSERVICE_DESCRIPTIONA
        # END IF   UNICODE

        # Actions to take on service failure
        class _SC_ACTION_TYPE(ENUM):
            SC_ACTION_NONE = 0
            SC_ACTION_RESTART = 1
            SC_ACTION_REBOOT = 2
            SC_ACTION_RUN_COMMAND = 3
            SC_ACTION_OWN_RESTART = 4

        SC_ACTION_TYPE = _SC_ACTION_TYPE

        _SC_ACTION._fields_ = [
            ('Type', SC_ACTION_TYPE),
            ('Delay', DWORD),
        ]

        _TEMP__SERVICE_FAILURE_ACTIONSA = [
            ('dwResetPeriod', DWORD),
            ('lpRebootMsg', LPSTR),
            ('lpCommand', LPSTR),
        ]


        if defined(__midl):
            pass
        # END IF

        _TEMP__SERVICE_FAILURE_ACTIONSA += [
            ('cActions', DWORD),
        ]

        if defined(__midl):
            pass
        # END IF

        _TEMP__SERVICE_FAILURE_ACTIONSA += [
            ('lpsaActions', POINTER(SC_ACTION)),
        ]

        _SERVICE_FAILURE_ACTIONSA._fields_ = _TEMP__SERVICE_FAILURE_ACTIONSA

        _TEMP__SERVICE_FAILURE_ACTIONSW = [
            ('dwResetPeriod', DWORD),
            ('lpRebootMsg', LPWSTR),
            ('lpCommand', LPWSTR),
        ]

        if defined(__midl):
            pass
        # END IF

        _TEMP__SERVICE_FAILURE_ACTIONSW += [
            ('cActions', DWORD),
        ]

        if defined(__midl):
            pass
        # END IF

        _TEMP__SERVICE_FAILURE_ACTIONSW += [
            ('lpsaActions', POINTER(SC_ACTION)),
        ]

        _SERVICE_FAILURE_ACTIONSW._fields_ = _TEMP__SERVICE_FAILURE_ACTIONSW

        if defined(UNICODE):
            SERVICE_FAILURE_ACTIONS = SERVICE_FAILURE_ACTIONSW
            LPSERVICE_FAILURE_ACTIONS = LPSERVICE_FAILURE_ACTIONSW
        else:
            SERVICE_FAILURE_ACTIONS = SERVICE_FAILURE_ACTIONSA
            LPSERVICE_FAILURE_ACTIONS = LPSERVICE_FAILURE_ACTIONSA
        # END IF   UNICODE

        # Service delayed autostart info setting
        # Delayed autostart flag
        _SERVICE_DELAYED_AUTO_START_INFO._fields_ = [
            ('fDelayedAutostart', BOOL),
        ]

        # Service failure actions flag setting
        # Failure actions flag
        _SERVICE_FAILURE_ACTIONS_FLAG._fields_ = [
            ('fFailureActionsOnNonCrashFailures', BOOL),
        ]

        # Service SID info setting
        # Service SID type
        _SERVICE_SID_INFO._fields_ = [
            ('dwServiceSidType', DWORD),
        ]

        # Service required privileges information
        # Required privileges multi-sz
        _SERVICE_REQUIRED_PRIVILEGES_INFOA._fields_ = [
            ('pmszRequiredPrivileges', LPSTR),
        ]

        # Service required privileges information
        # Required privileges multi-sz
        _SERVICE_REQUIRED_PRIVILEGES_INFOW._fields_ = [
            ('pmszRequiredPrivileges', LPWSTR),
        ]
        if defined(UNICODE):
            SERVICE_REQUIRED_PRIVILEGES_INFO = SERVICE_REQUIRED_PRIVILEGES_INFOW
            LPSERVICE_REQUIRED_PRIVILEGES_INFO = LPSERVICE_REQUIRED_PRIVILEGES_INFOW
        else:
            SERVICE_REQUIRED_PRIVILEGES_INFO = SERVICE_REQUIRED_PRIVILEGES_INFOA
            LPSERVICE_REQUIRED_PRIVILEGES_INFO = LPSERVICE_REQUIRED_PRIVILEGES_INFOA
        # END IF   UNICODE

        # Service preshutdown timeout setting
        # Timeout in msecs
        _SERVICE_PRESHUTDOWN_INFO._fields_ = [
            ('dwPreshutdownTimeout', DWORD),
        ]

        # Service trigger data item
        _TEMP__SERVICE_TRIGGER_SPECIFIC_DATA_ITEM = [
            # Data type -- one of SERVICE_TRIGGER_DATA_TYPE_* constants
            ('dwDataType', DWORD),
        ]

        if defined(__midl):
            pass
        # END IF

        _TEMP__SERVICE_TRIGGER_SPECIFIC_DATA_ITEM += [
            # Size of trigger specific data
            ('cbData', DWORD),
        ]

        if defined(__midl):
            pass
        # END IF

        _TEMP__SERVICE_TRIGGER_SPECIFIC_DATA_ITEM += [
            # Trigger specific data
            ('pData', PBYTE),
        ]

        _SERVICE_TRIGGER_SPECIFIC_DATA_ITEM._fields_ = _TEMP__SERVICE_TRIGGER_SPECIFIC_DATA_ITEM

        # Trigger-specific information
        _TEMP__SERVICE_TRIGGER = [
            # One of SERVICE_TRIGGER_TYPE_* constants
            ('dwTriggerType', DWORD),
            # One of SERVICE_TRIGGER_ACTION_* constants
            ('dwAction', DWORD),
            # Provider GUID if the trigger type is SERVICE_TRIGGER_TYPE_CUSTOM
            ('pTriggerSubtype', POINTER(GUID)),
        ]

        if defined(__midl):
            pass
        # END IF

        _TEMP__SERVICE_TRIGGER += [
            # Number of data items in pDataItems array
            ('cDataItems', DWORD),
        ]

        if defined(__midl):
            pass
        # END IF

        _TEMP__SERVICE_TRIGGER += [
            # Trigger specific data
            ('pDataItems', PSERVICE_TRIGGER_SPECIFIC_DATA_ITEM),
        ]

        _SERVICE_TRIGGER._fields_ = _TEMP__SERVICE_TRIGGER

        # Service trigger information
        _TEMP__SERVICE_TRIGGER_INFO = [
        ]

        if defined(__midl):
            pass
        # END IF

        _TEMP__SERVICE_TRIGGER_INFO += [
            # Number of triggers in the pTriggers array
            ('cTriggers', DWORD),
        ]

        if defined(__midl):
            pass
        # END IF

        _TEMP__SERVICE_TRIGGER_INFO += [
            # Array of triggers
            ('pTriggers', PSERVICE_TRIGGER),
            # Reserved, must be NULL
            ('pReserved', PBYTE),
        ]

        _SERVICE_TRIGGER_INFO._fields_ = _TEMP__SERVICE_TRIGGER_INFO
        SC_AGGREGATE_STORAGE_KEY = (
            "System\\CurrentControlSet\\Control\\ServiceAggregatedEvents"
        )

        # Preferred node information
        # Preferred node
        _SERVICE_PREFERRED_NODE_INFO._fields_ = [
            ('usPreferredNode', USHORT),
            # Delete the preferred node setting
            ('fDelete', BOOLEAN),
        ]

        # Time change information
        # New time
        _SERVICE_TIMECHANGE_INFO._fields_ = [
            ('liNewTime', LARGE_INTEGER),
            # Old time
            ('liOldTime', LARGE_INTEGER),
        ]

        # Service launch protected setting
        # Service launch protected
        _SERVICE_LAUNCH_PROTECTED_INFO._fields_ = [
            ('dwLaunchProtected', DWORD),
        ]

        # Handle Types
        SC_HANDLE = DECLARE_HANDLE()
        LPSC_HANDLE = POINTER(SC_HANDLE)
        SERVICE_STATUS_HANDLE = DECLARE_HANDLE()

        # Info levels for QueryServiceStatusEx
        class _SC_STATUS_TYPE(ENUM):
            SC_STATUS_PROCESS_INFO = 0

        SC_STATUS_TYPE = _SC_STATUS_TYPE

        # Info levels for EnumServicesStatusEx
        class _SC_ENUM_TYPE(ENUM):
            SC_ENUM_PROCESS_INFO = 0

        SC_ENUM_TYPE = _SC_ENUM_TYPE

        # Service Status Structures
        _SERVICE_STATUS._fields_ = [
            ('dwServiceType', DWORD),
            ('dwCurrentState', DWORD),
            ('dwControlsAccepted', DWORD),
            ('dwWin32ExitCode', DWORD),
            ('dwServiceSpecificExitCode', DWORD),
            ('dwCheckPoint', DWORD),
            ('dwWaitHint', DWORD),
        ]

        _SERVICE_STATUS_PROCESS._fields_ = [
            ('dwServiceType', DWORD),
            ('dwCurrentState', DWORD),
            ('dwControlsAccepted', DWORD),
            ('dwWin32ExitCode', DWORD),
            ('dwServiceSpecificExitCode', DWORD),
            ('dwCheckPoint', DWORD),
            ('dwWaitHint', DWORD),
            ('dwProcessId', DWORD),
            ('dwServiceFlags', DWORD),
        ]

        # Service Status Enumeration Structure
        _ENUM_SERVICE_STATUSA._fields_ = [
            ('lpServiceName', LPSTR),
            ('lpDisplayName', LPSTR),
            ('ServiceStatus', SERVICE_STATUS),
        ]

        _ENUM_SERVICE_STATUSW._fields_ = [
            ('lpServiceName', LPWSTR),
            ('lpDisplayName', LPWSTR),
            ('ServiceStatus', SERVICE_STATUS),
        ]
        if defined(UNICODE):
            ENUM_SERVICE_STATUS = ENUM_SERVICE_STATUSW
            LPENUM_SERVICE_STATUS = LPENUM_SERVICE_STATUSW
        else:
            ENUM_SERVICE_STATUS = ENUM_SERVICE_STATUSA
            LPENUM_SERVICE_STATUS = LPENUM_SERVICE_STATUSA
        # END IF   UNICODE


        _ENUM_SERVICE_STATUS_PROCESSA._fields_ = [
            ('lpServiceName', LPSTR),
            ('lpDisplayName', LPSTR),
            ('ServiceStatusProcess', SERVICE_STATUS_PROCESS),
        ]

        _ENUM_SERVICE_STATUS_PROCESSW._fields_ = [
            ('lpServiceName', LPWSTR),
            ('lpDisplayName', LPWSTR),
            ('ServiceStatusProcess', SERVICE_STATUS_PROCESS),
        ]
        if defined(UNICODE):
            ENUM_SERVICE_STATUS_PROCESS = ENUM_SERVICE_STATUS_PROCESSW
            LPENUM_SERVICE_STATUS_PROCESS = LPENUM_SERVICE_STATUS_PROCESSW
        else:
            ENUM_SERVICE_STATUS_PROCESS = ENUM_SERVICE_STATUS_PROCESSA
            LPENUM_SERVICE_STATUS_PROCESS = LPENUM_SERVICE_STATUS_PROCESSA
        # END IF   UNICODE

        # Structures for the Lock API functions
        SC_LOCK = LPVOID

        _QUERY_SERVICE_LOCK_STATUSA._fields_ = [
            ('fIsLocked', DWORD),
            ('lpLockOwner', LPSTR),
            ('dwLockDuration', DWORD),
        ]

        _QUERY_SERVICE_LOCK_STATUSW._fields_ = [
            ('fIsLocked', DWORD),
            ('lpLockOwner', LPWSTR),
            ('dwLockDuration', DWORD),
        ]
        if defined(UNICODE):
            QUERY_SERVICE_LOCK_STATUS = QUERY_SERVICE_LOCK_STATUSW
            LPQUERY_SERVICE_LOCK_STATUS = LPQUERY_SERVICE_LOCK_STATUSW
        else:
            QUERY_SERVICE_LOCK_STATUS = QUERY_SERVICE_LOCK_STATUSA
            LPQUERY_SERVICE_LOCK_STATUS = LPQUERY_SERVICE_LOCK_STATUSA
        # END IF   UNICODE

        # Query Service Configuration Structure
        _QUERY_SERVICE_CONFIGA._fields_ = [
            ('dwServiceType', DWORD),
            ('dwStartType', DWORD),
            ('dwErrorControl', DWORD),
            ('lpBinaryPathName', LPSTR),
            ('lpLoadOrderGroup', LPSTR),
            ('dwTagId', DWORD),
            ('lpDependencies', LPSTR),
            ('lpServiceStartName', LPSTR),
            ('lpDisplayName', LPSTR),
        ]

        _QUERY_SERVICE_CONFIGW._fields_ = [
            ('dwServiceType', DWORD),
            ('dwStartType', DWORD),
            ('dwErrorControl', DWORD),
            ('lpBinaryPathName', LPWSTR),
            ('lpLoadOrderGroup', LPWSTR),
            ('dwTagId', DWORD),
            ('lpDependencies', LPWSTR),
            ('lpServiceStartName', LPWSTR),
            ('lpDisplayName', LPWSTR),
        ]
        if defined(UNICODE):
            QUERY_SERVICE_CONFIG = QUERY_SERVICE_CONFIGW
            LPQUERY_SERVICE_CONFIG = LPQUERY_SERVICE_CONFIGW
        else:
            QUERY_SERVICE_CONFIG = QUERY_SERVICE_CONFIGA
            LPQUERY_SERVICE_CONFIG = LPQUERY_SERVICE_CONFIGA
        # END IF   UNICODE

        # Function Prototype for the Service Main Function
        # typedef VOID WINAPI SERVICE_MAIN_FUNCTIONW (
        # DWORD dwNumServicesArgs,
        # LPWSTR *lpServiceArgVectors
        # );
        SERVICE_MAIN_FUNCTIONW = CALLBACK(
            VOID,
            DWORD,
            POINTER(LPWSTR),
        )

        # typedef VOID WINAPI SERVICE_MAIN_FUNCTIONA (
        # DWORD dwNumServicesArgs,
        # LPTSTR *lpServiceArgVectors
        # );
        SERVICE_MAIN_FUNCTIONA = CALLBACK(
            VOID,
            DWORD,
            POINTER(LPTSTR),
        )

        if defined(UNICODE):
            SERVICE_MAIN_FUNCTION = SERVICE_MAIN_FUNCTIONW
        else:
            SERVICE_MAIN_FUNCTION = SERVICE_MAIN_FUNCTIONA
        # END IF  UNICODE

        # typedef VOID (WINAPI *LPSERVICE_MAIN_FUNCTIONW)(
        # DWORD   dwNumServicesArgs,
        # LPWSTR  *lpServiceArgVectors
        # );
        LPSERVICE_MAIN_FUNCTIONW = CALLBACK(
            VOID,
            DWORD,
            POINTER(LPWSTR),
        )

        # typedef VOID (WINAPI *LPSERVICE_MAIN_FUNCTIONA)(
        # DWORD   dwNumServicesArgs,
        # LPSTR   *lpServiceArgVectors
        # );
        LPSERVICE_MAIN_FUNCTIONA = CALLBACK(
            VOID,
            DWORD,
            POINTER(LPWSTR),
        )

        if defined(UNICODE):
            LPSERVICE_MAIN_FUNCTION = LPSERVICE_MAIN_FUNCTIONW
        else:
            LPSERVICE_MAIN_FUNCTION = LPSERVICE_MAIN_FUNCTIONA
        # END IF  UNICODE

        # Service Start Table
        _SERVICE_TABLE_ENTRYA._fields_ = [
            ('lpServiceName', LPSTR),
            ('lpServiceProc', LPSERVICE_MAIN_FUNCTIONA),
        ]

        _SERVICE_TABLE_ENTRYW._fields_ = [
            ('lpServiceName', LPWSTR),
            ('lpServiceProc', LPSERVICE_MAIN_FUNCTIONW),
        ]
        if defined(UNICODE):
            SERVICE_TABLE_ENTRY = SERVICE_TABLE_ENTRYW
            LPSERVICE_TABLE_ENTRY = LPSERVICE_TABLE_ENTRYW
        else:
            SERVICE_TABLE_ENTRY = SERVICE_TABLE_ENTRYA
            LPSERVICE_TABLE_ENTRY = LPSERVICE_TABLE_ENTRYA
        # END IF   UNICODE

        # Prototype for the Service Control Handler Function
        # typedef VOID WINAPI HANDLER_FUNCTION (
        # DWORD    dwControl
        # );
        HANDLER_FUNCTION = CALLBACK(VOID, DWORD)

        # typedef DWORD WINAPI HANDLER_FUNCTION_EX (
        # DWORD    dwControl,
        # DWORD    dwEventType,
        # LPVOID   lpEventData,
        # LPVOID   lpContext
        # );
        HANDLER_FUNCTION_EX = CALLBACK(
            DWORD,
            DWORD,
            DWORD,
            LPVOID,
            LPVOID,
        )

        # typedef VOID (WINAPI *LPHANDLER_FUNCTION)(
        # DWORD    dwControl
        # );
        LPHANDLER_FUNCTION = CALLBACK(VOID, DWORD)

        # typedef DWORD (WINAPI *LPHANDLER_FUNCTION_EX)(
        # DWORD    dwControl,
        # DWORD    dwEventType,
        # LPVOID   lpEventData,
        # LPVOID   lpContext
        # );
        LPHANDLER_FUNCTION_EX = CALLBACK(
            DWORD,
            DWORD,
            DWORD,
            LPVOID,
            LPVOID,
        )

        # Service notification parameters
        # VOID
        # ( CALLBACK * PFN_SC_NOTIFY_CALLBACK ) (
        # _In_ PVOID pParameter
        # );
        PFN_SC_NOTIFY_CALLBACK = CALLBACK(VOID, PVOID)

        # Each new notify structure is a superset of the older version
        _SERVICE_NOTIFY_1._fields_ = [
            ('dwVersion', DWORD),
            ('pfnNotifyCallback', PFN_SC_NOTIFY_CALLBACK),
            ('pContext', PVOID),
            ('dwNotificationStatus', DWORD),
            ('ServiceStatus', SERVICE_STATUS_PROCESS),
        ]

        _SERVICE_NOTIFY_2A._fields_ = [
            ('dwVersion', DWORD),
            ('pfnNotifyCallback', PFN_SC_NOTIFY_CALLBACK),
            ('pContext', PVOID),
            ('dwNotificationStatus', DWORD),
            ('ServiceStatus', SERVICE_STATUS_PROCESS),
            ('dwNotificationTriggered', DWORD),
            ('pszServiceNames', LPSTR),
        ]

        _SERVICE_NOTIFY_2W._fields_ = [
            ('dwVersion', DWORD),
            ('pfnNotifyCallback', PFN_SC_NOTIFY_CALLBACK),
            ('pContext', PVOID),
            ('dwNotificationStatus', DWORD),
            ('ServiceStatus', SERVICE_STATUS_PROCESS),
            ('dwNotificationTriggered', DWORD),
            ('pszServiceNames', LPWSTR),
        ]
        if defined(UNICODE):
            SERVICE_NOTIFY_2 = SERVICE_NOTIFY_2W
            PSERVICE_NOTIFY_2 = PSERVICE_NOTIFY_2W
        else:
            SERVICE_NOTIFY_2 = SERVICE_NOTIFY_2A
            PSERVICE_NOTIFY_2 = PSERVICE_NOTIFY_2A
        # END IF   UNICODE

        SERVICE_NOTIFYA = SERVICE_NOTIFY_2A
        PSERVICE_NOTIFYA = POINTER(SERVICE_NOTIFY_2A)
        SERVICE_NOTIFYW = SERVICE_NOTIFY_2W
        PSERVICE_NOTIFYW = POINTER(SERVICE_NOTIFY_2W)
        if defined(UNICODE):
            SERVICE_NOTIFY = SERVICE_NOTIFYW
            PSERVICE_NOTIFY = PSERVICE_NOTIFYW
        else:
            SERVICE_NOTIFY = SERVICE_NOTIFYA
            PSERVICE_NOTIFY = PSERVICE_NOTIFYA
        # END IF   UNICODE

        # Service control status reason parameters
        _SERVICE_CONTROL_STATUS_REASON_PARAMSA._fields_ = [
            ('dwReason', DWORD),
            ('pszComment', LPSTR),
            ('ServiceStatus', SERVICE_STATUS_PROCESS),
        ]

        # Service control status reason parameters
        _SERVICE_CONTROL_STATUS_REASON_PARAMSW._fields_ = [
            ('dwReason', DWORD),
            ('pszComment', LPWSTR),
            ('ServiceStatus', SERVICE_STATUS_PROCESS),
        ]
        if defined(UNICODE):
            SERVICE_CONTROL_STATUS_REASON_PARAMS = SERVICE_CONTROL_STATUS_REASON_PARAMSW
            PSERVICE_CONTROL_STATUS_REASON_PARAMS = PSERVICE_CONTROL_STATUS_REASON_PARAMSW
        else:
            SERVICE_CONTROL_STATUS_REASON_PARAMS = SERVICE_CONTROL_STATUS_REASON_PARAMSA
            PSERVICE_CONTROL_STATUS_REASON_PARAMS = PSERVICE_CONTROL_STATUS_REASON_PARAMSA
        # END IF   UNICODE

        # Service start reason
        _SERVICE_START_REASON._fields_ = [
            ('dwReason', DWORD),
        ]

        # /////////////////////////////////////////////////////////////////////////
        #
        # API Function Prototypes
        # /////////////////////////////////////////////////////////////////////////
        #
        advapi32 = ctypes.windll.ADVAPI32

        # WINADVAPI
        # BOOL
        # WINAPI
        # ChangeServiceConfigA(
        # _In_        SC_HANDLE    hService,
        # _In_        DWORD        dwServiceType,
        # _In_        DWORD        dwStartType,
        # _In_        DWORD        dwErrorControl,
        # _In_opt_    LPCSTR     lpBinaryPathName,
        # _In_opt_    LPCSTR     lpLoadOrderGroup,
        # _Out_opt_   LPDWORD      lpdwTagId,
        # _In_opt_    LPCSTR     lpDependencies,
        # _In_opt_    LPCSTR     lpServiceStartName,
        # _In_opt_    LPCSTR     lpPassword,
        # _In_opt_    LPCSTR     lpDisplayName
        # );
        ChangeServiceConfigA = advapi32.ChangeServiceConfigA
        ChangeServiceConfigA.restype = BOOL

        # WINADVAPI
        # BOOL
        # WINAPI
        # ChangeServiceConfigW(
        # _In_        SC_HANDLE    hService,
        # _In_        DWORD        dwServiceType,
        # _In_        DWORD        dwStartType,
        # _In_        DWORD        dwErrorControl,
        # _In_opt_    LPCWSTR     lpBinaryPathName,
        # _In_opt_    LPCWSTR     lpLoadOrderGroup,
        # _Out_opt_   LPDWORD      lpdwTagId,
        # _In_opt_    LPCWSTR     lpDependencies,
        # _In_opt_    LPCWSTR     lpServiceStartName,
        # _In_opt_    LPCWSTR     lpPassword,
        # _In_opt_    LPCWSTR     lpDisplayName
        # );
        ChangeServiceConfigW = advapi32.ChangeServiceConfigW
        ChangeServiceConfigW.restype = BOOL

        if defined(UNICODE):
            ChangeServiceConfig = ChangeServiceConfigW
        else:
            ChangeServiceConfig = ChangeServiceConfigA
        # END IF   not UNICODE

        # WINADVAPI
        # BOOL
        # WINAPI
        # ChangeServiceConfig2A(
        # _In_        SC_HANDLE    hService,
        # _In_        DWORD        dwInfoLevel,
        # _In_opt_    LPVOID       lpInfo
        # );
        ChangeServiceConfig2A = advapi32.ChangeServiceConfig2A
        ChangeServiceConfig2A.restype = BOOL

        # WINADVAPI
        # BOOL
        # WINAPI
        # ChangeServiceConfig2W(
        # _In_        SC_HANDLE    hService,
        # _In_        DWORD        dwInfoLevel,
        # _In_opt_    LPVOID       lpInfo
        # );
        ChangeServiceConfig2W = advapi32.ChangeServiceConfig2W
        ChangeServiceConfig2W.restype = BOOL

        if defined(UNICODE):
            ChangeServiceConfig2 = ChangeServiceConfig2W
        else:
            ChangeServiceConfig2 = ChangeServiceConfig2A
        # END IF   not UNICODE

        # WINADVAPI
        # BOOL
        # WINAPI
        # CloseServiceHandle(
        # _In_        SC_HANDLE   hSCObject
        # );
        CloseServiceHandle = advapi32.CloseServiceHandle
        CloseServiceHandle.restype = BOOL

        # WINADVAPI
        # BOOL
        # WINAPI
        # ControlService(
        # _In_        SC_HANDLE           hService,
        # _In_        DWORD               dwControl,
        # _Out_       LPSERVICE_STATUS    lpServiceStatus
        # );
        ControlService = advapi32.ControlService
        ControlService.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # SC_HANDLE
        # WINAPI
        # CreateServiceA(
        # _In_        SC_HANDLE    hSCManager,
        # _In_        LPCSTR     lpServiceName,
        # _In_opt_    LPCSTR     lpDisplayName,
        # _In_        DWORD        dwDesiredAccess,
        # _In_        DWORD        dwServiceType,
        # _In_        DWORD        dwStartType,
        # _In_        DWORD        dwErrorControl,
        # _In_opt_    LPCSTR     lpBinaryPathName,
        # _In_opt_    LPCSTR     lpLoadOrderGroup,
        # _Out_opt_   LPDWORD      lpdwTagId,
        # _In_opt_    LPCSTR     lpDependencies,
        # _In_opt_    LPCSTR     lpServiceStartName,
        # _In_opt_    LPCSTR     lpPassword
        # );
        CreateServiceA = advapi32.CreateServiceA
        CreateServiceA.restype = SC_HANDLE

        # _Must_inspect_result_
        # WINADVAPI
        # SC_HANDLE
        # WINAPI
        # CreateServiceW(
        # _In_        SC_HANDLE    hSCManager,
        # _In_        LPCWSTR     lpServiceName,
        # _In_opt_    LPCWSTR     lpDisplayName,
        # _In_        DWORD        dwDesiredAccess,
        # _In_        DWORD        dwServiceType,
        # _In_        DWORD        dwStartType,
        # _In_        DWORD        dwErrorControl,
        # _In_opt_    LPCWSTR     lpBinaryPathName,
        # _In_opt_    LPCWSTR     lpLoadOrderGroup,
        # _Out_opt_   LPDWORD      lpdwTagId,
        # _In_opt_    LPCWSTR     lpDependencies,
        # _In_opt_    LPCWSTR     lpServiceStartName,
        # _In_opt_    LPCWSTR     lpPassword
        # );
        CreateServiceW = advapi32.CreateServiceW
        CreateServiceW.restype = SC_HANDLE

        if defined(UNICODE):
            CreateService = CreateServiceW
        else:
            CreateService = CreateServiceA
        # END IF   not UNICODE

        # WINADVAPI
        # BOOL
        # WINAPI
        # DeleteService(
        # _In_        SC_HANDLE   hService
        # );
        DeleteService = advapi32.DeleteService
        DeleteService.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # EnumDependentServicesA(
        # _In_            SC_HANDLE               hService,
        # _In_            DWORD                   dwServiceState,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPENUM_SERVICE_STATUSA  lpServices,
        # _In_            DWORD                   cbBufSize,
        # _Out_           LPDWORD                 pcbBytesNeeded,
        # _Out_           LPDWORD                 lpServicesReturned
        # );
        EnumDependentServicesA = advapi32.EnumDependentServicesA
        EnumDependentServicesA.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # EnumDependentServicesW(
        # _In_            SC_HANDLE               hService,
        # _In_            DWORD                   dwServiceState,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPENUM_SERVICE_STATUSW  lpServices,
        # _In_            DWORD                   cbBufSize,
        # _Out_           LPDWORD                 pcbBytesNeeded,
        # _Out_           LPDWORD                 lpServicesReturned
        # );
        EnumDependentServicesW = advapi32.EnumDependentServicesW
        EnumDependentServicesW.restype = BOOL

        if defined(UNICODE):
            EnumDependentServices = EnumDependentServicesW
        else:
            EnumDependentServices = EnumDependentServicesA
        # END IF   not UNICODE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        advapi32 = ctypes.windll.ADVAPI32

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # EnumServicesStatusA(
        # _In_            SC_HANDLE               hSCManager,
        # _In_            DWORD                   dwServiceType,
        # _In_            DWORD                   dwServiceState,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPENUM_SERVICE_STATUSA  lpServices,
        # _In_            DWORD                   cbBufSize,
        # _Out_           LPDWORD                 pcbBytesNeeded,
        # _Out_           LPDWORD                 lpServicesReturned,
        # _Inout_opt_     LPDWORD                 lpResumeHandle
        # );
        EnumServicesStatusA = advapi32.EnumServicesStatusA
        EnumServicesStatusA.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # EnumServicesStatusW(
        # _In_            SC_HANDLE               hSCManager,
        # _In_            DWORD                   dwServiceType,
        # _In_            DWORD                   dwServiceState,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPENUM_SERVICE_STATUSW  lpServices,
        # _In_            DWORD                   cbBufSize,
        # _Out_           LPDWORD                 pcbBytesNeeded,
        # _Out_           LPDWORD                 lpServicesReturned,
        # _Inout_opt_     LPDWORD                 lpResumeHandle
        # );
        EnumServicesStatusW = advapi32.EnumServicesStatusW
        EnumServicesStatusW.restype = BOOL

        if defined(UNICODE):
            EnumServicesStatus = EnumServicesStatusW
        else:
            EnumServicesStatus = EnumServicesStatusA
        # END IF   not UNICODE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        advapi32 = ctypes.windll.ADVAPI32

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # EnumServicesStatusExA(
        # _In_            SC_HANDLE               hSCManager,
        # _In_            SC_ENUM_TYPE            InfoLevel,
        # _In_            DWORD                   dwServiceType,
        # _In_            DWORD                   dwServiceState,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPBYTE                  lpServices,
        # _In_            DWORD                   cbBufSize,
        # _Out_           LPDWORD                 pcbBytesNeeded,
        # _Out_           LPDWORD                 lpServicesReturned,
        # _Inout_opt_     LPDWORD                 lpResumeHandle,
        # _In_opt_        LPCSTR                pszGroupName
        # );
        EnumServicesStatusExA = advapi32.EnumServicesStatusExA
        EnumServicesStatusExA.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # EnumServicesStatusExW(
        # _In_            SC_HANDLE               hSCManager,
        # _In_            SC_ENUM_TYPE            InfoLevel,
        # _In_            DWORD                   dwServiceType,
        # _In_            DWORD                   dwServiceState,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPBYTE                  lpServices,
        # _In_            DWORD                   cbBufSize,
        # _Out_           LPDWORD                 pcbBytesNeeded,
        # _Out_           LPDWORD                 lpServicesReturned,
        # _Inout_opt_     LPDWORD                 lpResumeHandle,
        # _In_opt_        LPCWSTR                pszGroupName
        # );
        EnumServicesStatusExW = advapi32.EnumServicesStatusExW
        EnumServicesStatusExW.restype = BOOL

        if defined(UNICODE):
            EnumServicesStatusEx = EnumServicesStatusExW
        else:
            EnumServicesStatusEx = EnumServicesStatusExA
        # END IF   not UNICODE

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # GetServiceKeyNameA(
        # _In_            SC_HANDLE               hSCManager,
        # _In_            LPCSTR                lpDisplayName,
        # _Out_writes_opt_(*lpcchBuffer)
        # LPSTR                 lpServiceName,
        # _Inout_         LPDWORD                 lpcchBuffer
        # );
        GetServiceKeyNameA = advapi32.GetServiceKeyNameA
        GetServiceKeyNameA.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # GetServiceKeyNameW(
        # _In_            SC_HANDLE               hSCManager,
        # _In_            LPCWSTR                lpDisplayName,
        # _Out_writes_opt_(*lpcchBuffer)
        # LPWSTR                 lpServiceName,
        # _Inout_         LPDWORD                 lpcchBuffer
        # );
        GetServiceKeyNameW = advapi32.GetServiceKeyNameW
        GetServiceKeyNameW.restype = BOOL

        if defined(UNICODE):
            GetServiceKeyName = GetServiceKeyNameW
        else:
            GetServiceKeyName = GetServiceKeyNameA
        # END IF   not UNICODE

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # GetServiceDisplayNameA(
        # _In_            SC_HANDLE               hSCManager,
        # _In_            LPCSTR                lpServiceName,
        # _Out_writes_opt_(*lpcchBuffer)
        # LPSTR                 lpDisplayName,
        # _Inout_         LPDWORD                 lpcchBuffer
        # );
        GetServiceDisplayNameA = advapi32.GetServiceDisplayNameA
        GetServiceDisplayNameA.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # GetServiceDisplayNameW(
        # _In_            SC_HANDLE               hSCManager,
        # _In_            LPCWSTR                lpServiceName,
        # _Out_writes_opt_(*lpcchBuffer)
        # LPWSTR                 lpDisplayName,
        # _Inout_         LPDWORD                 lpcchBuffer
        # );
        GetServiceDisplayNameW = advapi32.GetServiceDisplayNameW
        GetServiceDisplayNameW.restype = BOOL

        if defined(UNICODE):
            GetServiceDisplayName = GetServiceDisplayNameW
        else:
            GetServiceDisplayName = GetServiceDisplayNameA
        # END IF   not UNICODE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        advapi32 = ctypes.windll.ADVAPI32

        # WINADVAPI
        # SC_LOCK
        # WINAPI
        # LockServiceDatabase(
        # _In_            SC_HANDLE               hSCManager
        # );
        LockServiceDatabase = advapi32.LockServiceDatabase
        LockServiceDatabase.restype = SC_LOCK

        # WINADVAPI
        # BOOL
        # WINAPI
        # NotifyBootConfigStatus(
        # _In_            BOOL                    BootAcceptable
        # );
        NotifyBootConfigStatus = advapi32.NotifyBootConfigStatus
        NotifyBootConfigStatus.restype = BOOL

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        advapi32 = ctypes.windll.ADVAPI32

        # _Must_inspect_result_
        # WINADVAPI
        # SC_HANDLE
        # WINAPI
        # OpenSCManagerA(
        # _In_opt_        LPCSTR                lpMachineName,
        # _In_opt_        LPCSTR                lpDatabaseName,
        # _In_            DWORD                   dwDesiredAccess
        # );
        OpenSCManagerA = advapi32.OpenSCManagerA
        OpenSCManagerA.restype = SC_HANDLE

        # _Must_inspect_result_
        # WINADVAPI
        # SC_HANDLE
        # WINAPI
        # OpenSCManagerW(
        # _In_opt_        LPCWSTR                lpMachineName,
        # _In_opt_        LPCWSTR                lpDatabaseName,
        # _In_            DWORD                   dwDesiredAccess
        # );
        OpenSCManagerW = advapi32.OpenSCManagerW
        OpenSCManagerW.restype = SC_HANDLE

        if defined(UNICODE):
            OpenSCManager = OpenSCManagerW
        else:
            OpenSCManager = OpenSCManagerA
        # END IF   not UNICODE

        # _Must_inspect_result_
        # WINADVAPI
        # SC_HANDLE
        # WINAPI
        # OpenServiceA(
        # _In_            SC_HANDLE               hSCManager,
        # _In_            LPCSTR                lpServiceName,
        # _In_            DWORD                   dwDesiredAccess
        # );
        OpenServiceA = advapi32.OpenServiceA
        OpenServiceA.restype = SC_HANDLE

        # _Must_inspect_result_
        # WINADVAPI
        # SC_HANDLE
        # WINAPI
        # OpenServiceW(
        # _In_            SC_HANDLE               hSCManager,
        # _In_            LPCWSTR                lpServiceName,
        # _In_            DWORD                   dwDesiredAccess
        # );
        OpenServiceW = advapi32.OpenServiceW
        OpenServiceW.restype = SC_HANDLE

        if defined(UNICODE):
            OpenService = OpenServiceW
        else:
            OpenService = OpenServiceA
        # END IF   not UNICODE


        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # QueryServiceConfigA(
        # _In_            SC_HANDLE               hService,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPQUERY_SERVICE_CONFIGA lpServiceConfig,
        # _In_            DWORD                   cbBufSize,
        # _Out_           LPDWORD                 pcbBytesNeeded
        # );
        QueryServiceConfigA = advapi32.QueryServiceConfigA
        QueryServiceConfigA.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # QueryServiceConfigW(
        # _In_            SC_HANDLE               hService,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPQUERY_SERVICE_CONFIGW lpServiceConfig,
        # _In_            DWORD                   cbBufSize,
        # _Out_           LPDWORD                 pcbBytesNeeded
        # );
        QueryServiceConfigW = advapi32.QueryServiceConfigW
        QueryServiceConfigW.restype = BOOL

        if defined(UNICODE):
            QueryServiceConfig = QueryServiceConfigW
        else:
            QueryServiceConfig = QueryServiceConfigA
        # END IF   not UNICODE

        # _When_(dwInfoLevel == SERVICE_CONFIG_DESCRIPTION,
        # _At_(cbBufSize, _In_range_( >= , (ctypes.sizeof(LPSERVICE_DESCRIPTIONA))))
        # _When_(dwInfoLevel == SERVICE_CONFIG_FAILURE_ACTIONS,
        # _At_(cbBufSize, _In_range_( >= , (ctypes.sizeof(LPSERVICE_FAILURE_ACTIONSA))))
        # _When_(dwInfoLevel == SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO,
        # _At_(cbBufSize, _In_range_( >= ,
        # (ctypes.sizeof(LPSERVICE_REQUIRED_PRIVILEGES_INFOA))))
        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # QueryServiceConfig2A(
        # _In_            SC_HANDLE               hService,
        # _In_            DWORD                   dwInfoLevel,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPBYTE                  lpBuffer,
        # _In_            DWORD                   cbBufSize,
        # _Out_           LPDWORD                 pcbBytesNeeded
        # );
        QueryServiceConfig2A = advapi32.QueryServiceConfig2A
        QueryServiceConfig2A.restype = BOOL

        # _When_(dwInfoLevel == SERVICE_CONFIG_DESCRIPTION,
        # _At_(cbBufSize, _In_range_( >= , (ctypes.sizeof(LPSERVICE_DESCRIPTIONW))))
        # _When_(dwInfoLevel == SERVICE_CONFIG_FAILURE_ACTIONS,
        # _At_(cbBufSize, _In_range_( >= , (ctypes.sizeof(LPSERVICE_FAILURE_ACTIONSW))))
        # _When_(dwInfoLevel == SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO,
        # _At_(cbBufSize, _In_range_( >= ,
        # (ctypes.sizeof(LPSERVICE_REQUIRED_PRIVILEGES_INFOW))))
        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # QueryServiceConfig2W(
        # _In_            SC_HANDLE               hService,
        # _In_            DWORD                   dwInfoLevel,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPBYTE                  lpBuffer,
        # _In_            DWORD                   cbBufSize,
        # _Out_           LPDWORD                 pcbBytesNeeded
        # );
        QueryServiceConfig2W = advapi32.QueryServiceConfig2W
        QueryServiceConfig2W.restype = BOOL

        if defined(UNICODE):
            QueryServiceConfig2 = QueryServiceConfig2W
        else:
            QueryServiceConfig2 = QueryServiceConfig2A
        # END IF   not UNICODE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        advapi32 = ctypes.windll.ADVAPI32

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # QueryServiceLockStatusA(
        # _In_            SC_HANDLE                       hSCManager,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPQUERY_SERVICE_LOCK_STATUSA    lpLockStatus,
        # _In_            DWORD                           cbBufSize,
        # _Out_           LPDWORD                         pcbBytesNeeded
        # );
        QueryServiceLockStatusA = advapi32.QueryServiceLockStatusA
        QueryServiceLockStatusA.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # QueryServiceLockStatusW(
        # _In_            SC_HANDLE                       hSCManager,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPQUERY_SERVICE_LOCK_STATUSW    lpLockStatus,
        # _In_            DWORD                           cbBufSize,
        # _Out_           LPDWORD                         pcbBytesNeeded
        # );
        QueryServiceLockStatusW = advapi32.QueryServiceLockStatusW
        QueryServiceLockStatusW.restype = BOOL

        if defined(UNICODE):
            QueryServiceLockStatus = QueryServiceLockStatusW
        else:
            QueryServiceLockStatus = QueryServiceLockStatusA
        # END IF   not UNICODE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        advapi32 = ctypes.windll.ADVAPI32

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # QueryServiceObjectSecurity(
        # _In_            SC_HANDLE               hService,
        # _In_            SECURITY_INFORMATION    dwSecurityInformation,
        # _Out_writes_bytes_opt_(cbBufSize)
        # PSECURITY_DESCRIPTOR    lpSecurityDescriptor,
        # _In_            DWORD                   cbBufSize,
        # _Out_           LPDWORD                 pcbBytesNeeded
        # );
        QueryServiceObjectSecurity = advapi32.QueryServiceObjectSecurity
        QueryServiceObjectSecurity.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # QueryServiceStatus(
        # _In_            SC_HANDLE           hService,
        # _Out_           LPSERVICE_STATUS    lpServiceStatus
        # );
        QueryServiceStatus = advapi32.QueryServiceStatus
        QueryServiceStatus.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # BOOL
        # WINAPI
        # QueryServiceStatusEx(
        # _In_            SC_HANDLE           hService,
        # _In_            SC_STATUS_TYPE      InfoLevel,
        # _Out_writes_bytes_opt_(cbBufSize)
        # LPBYTE              lpBuffer,
        # _In_            DWORD               cbBufSize,
        # _Out_           LPDWORD             pcbBytesNeeded
        # );
        QueryServiceStatusEx = advapi32.QueryServiceStatusEx
        QueryServiceStatusEx.restype = BOOL

        # _Must_inspect_result_
        # WINADVAPI
        # SERVICE_STATUS_HANDLE
        # WINAPI
        # RegisterServiceCtrlHandlerA(
        # _In_    LPCSTR                    lpServiceName,
        # _In_    __callback
        # LPHANDLER_FUNCTION          lpHandlerProc
        # );
        RegisterServiceCtrlHandlerA = advapi32.RegisterServiceCtrlHandlerA
        RegisterServiceCtrlHandlerA.restype = SERVICE_STATUS_HANDLE

        # _Must_inspect_result_
        # WINADVAPI
        # SERVICE_STATUS_HANDLE
        # WINAPI
        # RegisterServiceCtrlHandlerW(
        # _In_    LPCWSTR                    lpServiceName,
        # _In_    __callback
        # LPHANDLER_FUNCTION          lpHandlerProc
        # );
        RegisterServiceCtrlHandlerW = advapi32.RegisterServiceCtrlHandlerW
        RegisterServiceCtrlHandlerW.restype = SERVICE_STATUS_HANDLE

        if defined(UNICODE):
            RegisterServiceCtrlHandler = RegisterServiceCtrlHandlerW
        else:
            RegisterServiceCtrlHandler = RegisterServiceCtrlHandlerA
        # END IF   not UNICODE

        # _Must_inspect_result_
        # WINADVAPI
        # SERVICE_STATUS_HANDLE
        # WINAPI
        # RegisterServiceCtrlHandlerExA(
        # _In_    LPCSTR                    lpServiceName,
        # _In_    __callback
        # LPHANDLER_FUNCTION_EX       lpHandlerProc,
        # _In_opt_ LPVOID                     lpContext
        # );
        RegisterServiceCtrlHandlerExA = advapi32.RegisterServiceCtrlHandlerExA
        RegisterServiceCtrlHandlerExA.restype = SERVICE_STATUS_HANDLE

        # _Must_inspect_result_
        # WINADVAPI
        # SERVICE_STATUS_HANDLE
        # WINAPI
        # RegisterServiceCtrlHandlerExW(
        # _In_    LPCWSTR                    lpServiceName,
        # _In_    __callback
        # LPHANDLER_FUNCTION_EX       lpHandlerProc,
        # _In_opt_ LPVOID                     lpContext
        # );
        RegisterServiceCtrlHandlerExW = advapi32.RegisterServiceCtrlHandlerExW
        RegisterServiceCtrlHandlerExW.restype = SERVICE_STATUS_HANDLE

        if defined(UNICODE):
            RegisterServiceCtrlHandlerEx = RegisterServiceCtrlHandlerExW
        else:
            RegisterServiceCtrlHandlerEx = RegisterServiceCtrlHandlerExA
        # END IF   not UNICODE

        # WINADVAPI
        # BOOL
        # WINAPI
        # SetServiceObjectSecurity(
        # _In_        SC_HANDLE               hService,
        # _In_        SECURITY_INFORMATION    dwSecurityInformation,
        # _In_        PSECURITY_DESCRIPTOR    lpSecurityDescriptor
        # );
        SetServiceObjectSecurity = advapi32.SetServiceObjectSecurity
        SetServiceObjectSecurity.restype = BOOL

        # WINADVAPI
        # BOOL
        # WINAPI
        # SetServiceStatus(
        # _In_        SERVICE_STATUS_HANDLE   hServiceStatus,
        # _In_        LPSERVICE_STATUS        lpServiceStatus
        # );
        SetServiceStatus = advapi32.SetServiceStatus
        SetServiceStatus.restype = BOOL

        # WINADVAPI
        # BOOL
        # WINAPI
        # StartServiceCtrlDispatcherA(
        # _In_ CONST  SERVICE_TABLE_ENTRYA    *lpServiceStartTable
        # );
        StartServiceCtrlDispatcherA = advapi32.StartServiceCtrlDispatcherA
        StartServiceCtrlDispatcherA.restype = BOOL

        # WINADVAPI
        # BOOL
        # WINAPI
        # StartServiceCtrlDispatcherW(
        # _In_ CONST  SERVICE_TABLE_ENTRYW    *lpServiceStartTable
        # );
        StartServiceCtrlDispatcherW = advapi32.StartServiceCtrlDispatcherW
        StartServiceCtrlDispatcherW.restype = BOOL

        if defined(UNICODE):
            StartServiceCtrlDispatcher = StartServiceCtrlDispatcherW
        else:
            StartServiceCtrlDispatcher = StartServiceCtrlDispatcherA
        # END IF   not UNICODE

        # WINADVAPI
        # BOOL
        # WINAPI
        # StartServiceA(
        # _In_            SC_HANDLE            hService,
        # _In_            DWORD                dwNumServiceArgs,
        # _In_reads_opt_(dwNumServiceArgs)
        # LPCSTR             *lpServiceArgVectors
        # );
        StartServiceA = advapi32.StartServiceA
        StartServiceA.restype = BOOL

        # WINADVAPI
        # BOOL
        # WINAPI
        # StartServiceW(
        # _In_            SC_HANDLE            hService,
        # _In_            DWORD                dwNumServiceArgs,
        # _In_reads_opt_(dwNumServiceArgs)
        # LPCWSTR             *lpServiceArgVectors
        # );
        StartServiceW = advapi32.StartServiceW
        StartServiceW.restype = BOOL

        if defined(UNICODE):
            StartService = StartServiceW
        else:
            StartService = StartServiceA
        # END IF   not UNICODE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        advapi32 = ctypes.windll.ADVAPI32

        # WINADVAPI
        # BOOL
        # WINAPI
        # UnlockServiceDatabase(
        # _In_            SC_LOCK             ScLock
        # );
        UnlockServiceDatabase = advapi32.UnlockServiceDatabase
        UnlockServiceDatabase.restype = BOOL
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if NTDDI_VERSION >= NTDDI_VISTA:
            advapi32 = ctypes.windll.ADVAPI32

            # WINADVAPI
            # DWORD
            # WINAPI
            # NotifyServiceStatusChangeA(
            # _In_        SC_HANDLE               hService,
            # _In_        DWORD                   dwNotifyMask,
            # _In_        PSERVICE_NOTIFYA        pNotifyBuffer
            # );
            NotifyServiceStatusChangeA = advapi32.NotifyServiceStatusChangeA
            NotifyServiceStatusChangeA.restype = DWORD

            # WINADVAPI
            # DWORD
            # WINAPI
            # NotifyServiceStatusChangeW(
            # _In_        SC_HANDLE               hService,
            # _In_        DWORD                   dwNotifyMask,
            # _In_        PSERVICE_NOTIFYW        pNotifyBuffer
            # );
            NotifyServiceStatusChangeW = advapi32.NotifyServiceStatusChangeW
            NotifyServiceStatusChangeW.restype = DWORD

            if defined(UNICODE):
                NotifyServiceStatusChange = NotifyServiceStatusChangeW
            else:
                NotifyServiceStatusChange = NotifyServiceStatusChangeA
            # END IF   not UNICODE

            # WINADVAPI
            # BOOL
            # WINAPI
            # ControlServiceExA(
            # _In_        SC_HANDLE               hService,
            # _In_        DWORD                   dwControl,
            # _In_        DWORD                   dwInfoLevel,
            # _Inout_     PVOID                   pControlParams
            # );
            ControlServiceExA = advapi32.ControlServiceExA
            ControlServiceExA.restype = BOOL

            # WINADVAPI
            # BOOL
            # WINAPI
            # ControlServiceExW(
            # _In_        SC_HANDLE               hService,
            # _In_        DWORD                   dwControl,
            # _In_        DWORD                   dwInfoLevel,
            # _Inout_     PVOID                   pControlParams
            # );
            ControlServiceExW = advapi32.ControlServiceExW
            ControlServiceExW.restype = BOOL

            if defined(UNICODE):
                ControlServiceEx = ControlServiceExW
            else:
                ControlServiceEx = ControlServiceExA
            # END IF   not UNICODE

            # WINADVAPI
            # BOOL
            # WINAPI
            # QueryServiceDynamicInformation(
            # _In_        SERVICE_STATUS_HANDLE   hServiceStatus,
            # _In_        DWORD                   dwInfoLevel,
            # _Outptr_    PVOID           *       ppDynamicInfo
            # );
            QueryServiceDynamicInformation = (
                advapi32.QueryServiceDynamicInformation
            )
            QueryServiceDynamicInformation.restype = BOOL

        # END IF   NTDDI_VERSION >= NTDDI_VISTA

        if NTDDI_VERSION >= NTDDI_WIN8:
            # Service status change notification API
            class _SC_EVENT_TYPE(ENUM):
                SC_EVENT_DATABASE_CHANGE = 1
                SC_EVENT_PROPERTY_CHANGE = 2
                SC_EVENT_STATUS_CHANGE = 3

            SC_EVENT_TYPE = _SC_EVENT_TYPE
            PSC_EVENT_TYPE = POINTER(_SC_EVENT_TYPE)

            # VOID
            # CALLBACK
            # SC_NOTIFICATION_CALLBACK (
            # _In_        DWORD                   dwNotify,
            # _In_opt_    PVOID                   pCallbackContext
            # );
            SC_NOTIFICATION_CALLBACK = CALLBACK(VOID, DWORD, PVOID)
            PSC_NOTIFICATION_CALLBACK = POINTER(SC_NOTIFICATION_CALLBACK)

            class _SC_NOTIFICATION_REGISTRATION(ctypes.Structure):
                pass

            PSC_NOTIFICATION_REGISTRATION = POINTER(_SC_NOTIFICATION_REGISTRATION)

        # END IF   NTDDI_VERSION >= NTDDI_WIN8

        if NTDDI_VERSION >= NTDDI_WIN10_RS4:
            # Service state type enums
            class SERVICE_REGISTRY_STATE_TYPE(ENUM):
                ServiceRegistryStateParameters = 0
                ServiceRegistryStatePersistent = 1
                MaxServiceRegistryStateType = 2

        # END IF   NTDDI_VERSION >= NTDDI_WIN10_RS4
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if defined(__cplusplus):
        pass
    # END IF


    if _MSC_VER >= 1200:
        pass
    # END IF

# END IF   _WINSVC_


