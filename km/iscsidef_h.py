import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _ISCSI_IP_Address(ctypes.Structure):
    pass


ISCSI_IP_Address = _ISCSI_IP_Address
PISCSI_IP_Address = POINTER(_ISCSI_IP_Address)


class _ISCSI_TargetPortal(ctypes.Structure):
    pass


ISCSI_TargetPortal = _ISCSI_TargetPortal
PISCSI_TargetPortal = POINTER(_ISCSI_TargetPortal)


class _ISCSI_TargetPortalGroup(ctypes.Structure):
    pass


ISCSI_TargetPortalGroup = _ISCSI_TargetPortalGroup
PISCSI_TargetPortalGroup = POINTER(_ISCSI_TargetPortalGroup)


class _ISCSI_LoginOptions(ctypes.Structure):
    pass


ISCSI_LoginOptions = _ISCSI_LoginOptions
PISCSI_LoginOptions = POINTER(_ISCSI_LoginOptions)


class _ISCSI_LUNList(ctypes.Structure):
    pass


ISCSI_LUNList = _ISCSI_LUNList
PISCSI_LUNList = POINTER(_ISCSI_LUNList)


class _ISCSI_TargetMapping(ctypes.Structure):
    pass


ISCSI_TargetMapping = _ISCSI_TargetMapping
PISCSI_TargetMapping = POINTER(_ISCSI_TargetMapping)

_iscsidef_h_ = None
if not defined(_iscsidef_h_):
    _iscsidef_h_ = 1
    # ISCSI_IP_Address - ISCSI_IP_Address
    # *********************************************************************
    # iscsidef.h
    # Module: iScsi Discovery api
    # Purpose: Internal header defining interface between user mode discovery
    # api dll and HBA driver miniport.
    # Copyright (c) 2001 Microsoft Corporation
    # *********************************************************************
    # Definitions for iscsi security flags. These flags provide
    # information about the security expectations of a target portal and
    # are needed to insure a successful IKE/IPSEC negotiation. Note that
    # the flags and values are taken directly from the iSNS spec
    # 1 = Tunnel Mode Preferred; 0 = No Preference
    ISCSI_SECURITY_FLAG_TUNNEL_MODE_PREFERRED = 0x00000040

    # 1 = Transport Mode Preferred; 0 = No Preference
    ISCSI_SECURITY_FLAG_TRANSPORT_MODE_PREFERRED = 0x00000020

    # 1 = PFS Enabled; 0 = PFS Disabled
    ISCSI_SECURITY_FLAG_PFS_ENABLED = 0x00000010

    # 1 = Aggressive Mode Enabled; 0 = Disabled
    ISCSI_SECURITY_FLAG_AGGRESSIVE_MODE_ENABLED = 0x00000008

    # 1 = Main Mode Enabled; 0 = MM Disabled
    ISCSI_SECURITY_FLAG_MAIN_MODE_ENABLED = 0x00000004

    # 1 = IKE/IPSec Enabled; 0 = IKE/IPSec Disabled
    ISCSI_SECURITY_FLAG_IKE_IPSEC_ENABLED = 0x00000002

    # If set then all other ISCSI_SECURITY_FLAGS are valid
    ISCSI_SECURITY_FLAG_VALID = 0x00000001

    # Types of addresses that can be passed by management app to driver
    class ISCSIIPADDRESSTYPE(ENUM):
        ISCSI_IP_ADDRESS_TEXT = 0
        ISCSI_IP_ADDRESS_IPV4 = 1
        ISCSI_IP_ADDRESS_IPV6 = 2
        ISCSI_IP_ADDRESS_EMPTY = 3

    PISCSIIPADDRESSTYPE = POINTER(ISCSIIPADDRESSTYPE)
    ISCSI_IP_ADDRESS_TEXT = ISCSIIPADDRESSTYPE.ISCSI_IP_ADDRESS_TEXT
    ISCSI_IP_ADDRESS_IPV4 = ISCSIIPADDRESSTYPE.ISCSI_IP_ADDRESS_IPV4
    ISCSI_IP_ADDRESS_IPV6 = ISCSIIPADDRESSTYPE.ISCSI_IP_ADDRESS_IPV6
    ISCSI_IP_ADDRESS_EMPTY = ISCSIIPADDRESSTYPE.ISCSI_IP_ADDRESS_EMPTY
    ISCSI_IP_AddressGuid = [
        0x9AC5D4A1,
        0x1A1A,
        0x48EC,
        [0x8E, 0x79, 0x73, 0x58, 0x06, 0xE9, 0xA1, 0xFA]
    ]
    if not defined(MIDL_PASS):
        ISCSI_IP_Address_GUID = DEFINE_GUID(
            0x9AC5D4A1,
            0x1A1A,
            0x48EC,
            0x8E,
            0x79,
            0x73,
            0x58,
            0x06,
            0xE9,
            0xA1,
            0xFA
        )
    # END IF

    ISCSI_IP_Address_Type_SIZE = ctypes.sizeof(ULONG)
    ISCSI_IP_Address_Type_ID = 1
    ISCSI_IP_Address_IpV4Address_SIZE = ctypes.sizeof(ULONG)
    ISCSI_IP_Address_IpV4Address_ID = 2
    ISCSI_IP_Address_IpV6Address_SIZE = ctypes.sizeof(UCHAR[16])
    ISCSI_IP_Address_IpV6Address_ID = 3
    ISCSI_IP_Address_IpV6FlowInfo_SIZE = ctypes.sizeof(ULONG)
    ISCSI_IP_Address_IpV6FlowInfo_ID = 4
    ISCSI_IP_Address_IpV6ScopeId_SIZE = ctypes.sizeof(ULONG)
    ISCSI_IP_Address_IpV6ScopeId_ID = 5
    ISCSI_IP_Address_TextAddress_ID = 6

    _ISCSI_IP_Address._fields_ = [
        # Type of address specified. It can be text: a DNS or dotted address
        # or it can be a binary ipv4 or ipv6 address
        ('Type', ULONG),
        # If IPV4 Address is specified as the Address Format then this conains
        # the binary IPv4 ip address
        ('IpV4Address', ULONG),
        # If IPV6 Address is specified as the Address Format then this conains
        # the binary IPv6 ip address
        ('IpV6Address', UCHAR * 16),
        # IPV6 flow information
        ('IpV6FlowInfo', ULONG),
        # IPV6 scope id
        ('IpV6ScopeId', ULONG),
        # Text address, either a DNS address or dotted address
        ('TextAddress', WCHAR * 256 + 1),
    ]

    # ISCSI_TargetPortal - ISCSI_TargetPortal
    # ISCSI target portal
    ISCSI_TargetPortalGuid = [
        0xDE5051A7,
        0xBF27,
        0x48F1,
        [0xBD, 0x12, 0x07, 0xCA, 0xDE, 0x92, 0xAE, 0xFD],
    ]
    if not defined(MIDL_PASS):
        ISCSI_TargetPortal_GUID = DEFINE_GUID(
            0xDE5051A7,
            0xBF27,
            0x48F1,
            0xBD,
            0x12,
            0x07,
            0xCA,
            0xDE,
            0x92,
            0xAE,
            0xFD
        )
    # END IF

    ISCSI_TargetPortal_Address_SIZE = ctypes.sizeof(ISCSI_IP_Address)
    ISCSI_TargetPortal_Address_ID = 1
    ISCSI_TargetPortal_Reserved_SIZE = ctypes.sizeof(ULONG)
    ISCSI_TargetPortal_Reserved_ID = 2
    ISCSI_TargetPortal_Socket_SIZE = ctypes.sizeof(USHORT)
    ISCSI_TargetPortal_Socket_ID = 3

    _ISCSI_TargetPortal._fields_ = [
        # Network Address
        ('Address', ISCSI_IP_Address),
        # Reserved
        ('Reserved', ULONG),
        # Socket number
        ('Socket', USHORT),
    ]
    ISCSI_TargetPortal_SIZE = (
        FIELD_OFFSET(ISCSI_TargetPortal, 'Socket') +
        ISCSI_TargetPortal_Socket_SIZE
    )

    # ISCSI_TargetPortalGroup - ISCSI_TargetPortalGroup
    # iSCSI target portal group
    ISCSI_TargetPortalGroupGuid = [
        0x3081F2A5,
        0x95F5,
        0x4D2A,
        [0x81, 0x3D, 0xEE, 0x59, 0x86, 0x4C, 0x6F, 0xC5]
    ]
    if not defined(MIDL_PASS):
        ISCSI_TargetPortalGroup_GUID = DEFINE_GUID(
            0x3081F2A5,
            0x95F5,
            0x4D2A,
            0x81,
            0x3D,
            0xEE,
            0x59,
            0x86,
            0x4C,
            0x6F,
            0xC5
        )
    # END IF

    ISCSI_TargetPortalGroup_PortalCount_SIZE = ctypes.sizeof(ULONG)
    ISCSI_TargetPortalGroup_PortalCount_ID = 1
    ISCSI_TargetPortalGroup_Portals_ID = 2

    _ISCSI_TargetPortalGroup._fields_ = [
        # Number of portals in group
        ('PortalCount', ULONG),
        # Target portals in group
        ('Portals', ISCSI_TargetPortal * 1),
    ]

    # ISCSI_LoginOptions - ISCSI_LoginOptions
    # These are options that can be used for logging into a target

    _ISCSI_ISCSIDSC_ = None
    if not defined(_ISCSI_ISCSIDSC_):
        class ISCSI_DIGEST_TYPES(ENUM):
            ISCSI_DIGEST_TYPE_NONE = 0
            ISCSI_DIGEST_TYPE_CRC32C = 1

        PISCSI_DIGEST_TYPES = POINTER(ISCSI_DIGEST_TYPES)
        ISCSI_DIGEST_TYPE_NONE = ISCSI_DIGEST_TYPES.ISCSI_DIGEST_TYPE_NONE
        ISCSI_DIGEST_TYPE_CRC32C = ISCSI_DIGEST_TYPES.ISCSI_DIGEST_TYPE_CRC32C


        class ISCSI_AUTH_TYPES(ENUM):
            ISCSI_NO_AUTH_TYPE = 0
            ISCSI_CHAP_AUTH_TYPE = 1
            ISCSI_MUTUAL_CHAP_AUTH_TYPE = 2

        PISCSI_AUTH_TYPES = POINTER(ISCSI_AUTH_TYPES)
        ISCSI_NO_AUTH_TYPE = ISCSI_AUTH_TYPES.ISCSI_NO_AUTH_TYPE
        ISCSI_CHAP_AUTH_TYPE = ISCSI_AUTH_TYPES.ISCSI_CHAP_AUTH_TYPE
        ISCSI_MUTUAL_CHAP_AUTH_TYPE = ISCSI_AUTH_TYPES.ISCSI_MUTUAL_CHAP_AUTH_TYPE

    # END IF

    ISCSI_LoginOptionsGuid = [
        0x3011A7BD,
        0x0491,
        0x478E,
        [0x8C, 0x79, 0x3C, 0x76, 0x42, 0x4D, 0x05, 0xE2],
    ]

    if not defined(MIDL_PASS):
        ISCSI_LoginOptions_GUID = DEFINE_GUID(
            0x3011A7BD,
            0x0491,
            0x478E,
            0x8C,
            0x79,
            0x3C,
            0x76,
            0x42,
            0x4D,
            0x05,
            0xE2
        )
    # END IF

    ISCSI_LOGIN_OPTIONS_HEADER_DIGEST = 0x00000001
    ISCSI_LOGIN_OPTIONS_DATA_DIGEST = 0x00000002
    ISCSI_LOGIN_OPTIONS_MAXIMUM_CONNECTIONS = 0x00000004
    ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_WAIT = 0x00000008
    ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_RETAIN = 0x00000010
    ISCSI_LOGIN_OPTIONS_USERNAME = 0x00000020
    ISCSI_LOGIN_OPTIONS_PASSWORD = 0x00000040
    ISCSI_LOGIN_OPTIONS_AUTH_TYPE = 0x00000080

    ISCSI_LoginOptions_InformationSpecified_SIZE = ctypes.sizeof(ULONG)
    ISCSI_LoginOptions_InformationSpecified_ID = 1
    ISCSI_LoginOptions_HeaderDigest_SIZE = ctypes.sizeof(ULONG)
    ISCSI_LoginOptions_HeaderDigest_ID = 2
    ISCSI_LoginOptions_DataDigest_SIZE = ctypes.sizeof(ULONG)
    ISCSI_LoginOptions_DataDigest_ID = 3
    ISCSI_LoginOptions_MaximumConnections_SIZE = ctypes.sizeof(ULONG)
    ISCSI_LoginOptions_MaximumConnections_ID = 4
    ISCSI_LoginOptions_DefaultTime2Wait_SIZE = ctypes.sizeof(ULONG)
    ISCSI_LoginOptions_DefaultTime2Wait_ID = 5
    ISCSI_LoginOptions_DefaultTime2Retain_SIZE = ctypes.sizeof(ULONG)
    ISCSI_LoginOptions_DefaultTime2Retain_ID = 6
    ISCSI_LoginOptions_LoginFlags_SIZE = ctypes.sizeof(ULONG)
    ISCSI_LoginOptions_LoginFlags_ID = 7
    ISCSI_LoginOptions_AuthType_SIZE = ctypes.sizeof(ULONG)
    ISCSI_LoginOptions_AuthType_ID = 8

    if not defined(_ISCSI_ISCSIDSC_):
        ISCSI_LOGIN_FLAGS = ULONG
        ISCSI_LOGIN_FLAG_REQUIRE_IPSEC = 0x00000001
        ISCSI_LOGIN_FLAG_MULTIPATH_ENABLED = 0x00000002
        ISCSI_LOGIN_FLAG_RESERVED1 = 0x00000004
        ISCSI_LOGIN_FLAG_ALLOW_PORTAL_HOPPING = 0x00000008
        ISCSI_LOGIN_FLAG_USE_RADIUS_RESPONSE = 0x00000010
        ISCSI_LOGIN_FLAG_USE_RADIUS_VERIFICATION = 0x00000020

    # END IF

    _ISCSI_LoginOptions._fields_ = [
        # Bit flags that specify which login option values are specified
        ('InformationSpecified', ULONG),
        # cyclic integrity checksums that can be negotiated for the header
        # digests
        ('HeaderDigest', ULONG),
        # cyclic integrity checksums that can be negotiated for the header
        # digests
        ('DataDigest', ULONG),
        # Maximum number of connections, 0 implies no limit
        ('MaximumConnections', ULONG),
        # The initiator and target negotiate the minimum time, in seconds, to
        # wait before attempting an explicit/implicit logout or active task
        # reassignment after an unexpected connection termination or a
        # connection reset.
        ('DefaultTime2Wait', ULONG),
        # The initiator and target negotiate the maximum time, in seconds
        # after an initial wait (Time2Wait), before which an explicit/implicit
        # connection Logout or active task reassignment is still possible
        # after an unexpected connection termination or a connection reset.
        ('DefaultTime2Retain', ULONG),
        # Flags that affect how login occurs
        ('LoginFlags', ULONG),
        # Authentication method specified for login
        ('AuthType', ULONG),
    ]

    ISCSI_LoginOptions_SIZE = (
        FIELD_OFFSET(ISCSI_LoginOptions, 'AuthType') +
        ISCSI_LoginOptions_AuthType_SIZE
    )

    # ISCSI_LUNList - ISCSI_LUNList
    # This class describes a mapping from a an OS LUN to target device LUN
    ISCSI_LUNListGuid = [
        0x994FF278,
        0x3512,
        0x4D9B,
        [0xA2, 0x41, 0x54, 0xCE, 0xF4, 0x5F, 0x5A, 0x25],
    ]

    if not defined(MIDL_PASS):
        ISCSI_LUNList_GUID = DEFINE_GUID(
            0x994FF278,
            0x3512,
            0x4D9B,
            0xA2,
            0x41,
            0x54,
            0xCE,
            0xF4,
            0x5F,
            0x5A,
            0x25
        )
    # END IF

    ISCSI_LUNList_TargetLUN_SIZE = ctypes.sizeof(ULONGLONG)
    ISCSI_LUNList_TargetLUN_ID = 1
    ISCSI_LUNList_OSLUN_SIZE = ctypes.sizeof(ULONG)
    ISCSI_LUNList_OSLUN_ID = 2
    ISCSI_LUNList_Reserved_SIZE = ctypes.sizeof(ULONG)
    ISCSI_LUNList_Reserved_ID = 3

    _ISCSI_LUNList._fields_ = [
        # Target LUN
        ('TargetLUN', ULONGLONG),
        # OS Scsi bus number target is mapped to
        ('OSLUN', ULONG),
        # Reserved
        ('Reserved', ULONG),
    ]
    ISCSI_LUNList_SIZE = (
        FIELD_OFFSET(ISCSI_LUNList, 'Reserved') +
        ISCSI_LUNList_Reserved_SIZE
    )

    # ISCSI_TargetMapping - ISCSI_TargetMapping
    # This class describes a mapping from a target LUN to a Windows port
    # driver LUN
    ISCSI_TargetMappingGuid = [
        0x21A28820,
        0x3C4C,
        0x4944,
        [0xAC, 0x4F, 0xDA, 0x7F, 0xEB, 0xA2, 0x11, 0x68]
    ]

    if not defined(MIDL_PASS):
        ISCSI_TargetMapping_GUID = DEFINE_GUID(
            0x21A28820,
            0x3C4C,
            0x4944,
            0xAC,
            0x4F,
            0xDA,
            0x7F,
            0xEB,
            0xA2,
            0x11,
            0x68
        )
    # END IF

    ISCSI_TargetMapping_OSBus_SIZE = ctypes.sizeof(ULONG)
    ISCSI_TargetMapping_OSBus_ID = 1
    ISCSI_TargetMapping_OSTarget_SIZE = ctypes.sizeof(ULONG)
    ISCSI_TargetMapping_OSTarget_ID = 2
    ISCSI_TargetMapping_UniqueSessionId_SIZE = ctypes.sizeof(ULONGLONG)
    ISCSI_TargetMapping_UniqueSessionId_ID = 3
    ISCSI_TargetMapping_LUNCount_SIZE = ctypes.sizeof(ULONG)
    ISCSI_TargetMapping_LUNCount_ID = 4
    ISCSI_TargetMapping_TargetName_ID = 5
    ISCSI_TargetMapping_FromPersistentLogin_SIZE = ctypes.sizeof(BOOLEAN)
    ISCSI_TargetMapping_FromPersistentLogin_ID = 6
    ISCSI_TargetMapping_Reserved_SIZE = ctypes.sizeof(ULONGLONG)
    ISCSI_TargetMapping_Reserved_ID = 7
    ISCSI_TargetMapping_LUNList_ID = 8

    _ISCSI_TargetMapping._fields_ = [
        # OS Scsi bus number target is mapped to. If 0xffffffff then any value
        # can be picked by the miniport.
        ('OSBus', ULONG),
        # OS Scsi Target number target is mapped to. If 0xffffffff then any
        # value can be picked by the miniport.
        ('OSTarget', ULONG),
        # Unique Session ID for the target mapping
        ('UniqueSessionId', ULONGLONG),
        # Count of LUNs mapped for this target
        ('LUNCount', ULONG),
        # Target Name
        ('TargetName', WCHAR * 223 + 1),
        # TRUE if session created from a persistent login
        ('FromPersistentLogin', BOOLEAN),
        # Reserved
        ('Reserved', ULONGLONG),
        # List of LUNs mapped for this target
        ('LUNList', ISCSI_LUNList * 1),
    ]
# END IF
