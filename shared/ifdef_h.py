import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_IFDEF_ = None
__IF_INDEX_DEFINED__ = None

class _NET_IF_RCV_ADDRESS_LH(ctypes.Structure):
    pass


NET_IF_RCV_ADDRESS_LH = _NET_IF_RCV_ADDRESS_LH
PNET_IF_RCV_ADDRESS_LH = POINTER(_NET_IF_RCV_ADDRESS_LH)


class _NET_IF_ALIAS_LH(ctypes.Structure):
    pass


NET_IF_ALIAS_LH = _NET_IF_ALIAS_LH
PNET_IF_ALIAS_LH = POINTER(_NET_IF_ALIAS_LH)


class _NET_LUID_LH(ctypes.Union):
    pass


NET_LUID_LH = _NET_LUID_LH
PNET_LUID_LH = POINTER(_NET_LUID_LH)


class _NET_PHYSICAL_LOCATION_LH(ctypes.Structure):
    pass


NET_PHYSICAL_LOCATION_LH = _NET_PHYSICAL_LOCATION_LH
PNET_PHYSICAL_LOCATION_LH = POINTER(_NET_PHYSICAL_LOCATION_LH)


class _IF_COUNTED_STRING_LH(ctypes.Structure):
    pass


IF_COUNTED_STRING_LH = _IF_COUNTED_STRING_LH
PIF_COUNTED_STRING_LH = POINTER(_IF_COUNTED_STRING_LH)


class _IF_PHYSICAL_ADDRESS_LH(ctypes.Structure):
    pass


IF_PHYSICAL_ADDRESS_LH = _IF_PHYSICAL_ADDRESS_LH
PIF_PHYSICAL_ADDRESS_LH = POINTER(_IF_PHYSICAL_ADDRESS_LH)


class _NDIS_INTERFACE_INFORMATION(ctypes.Structure):
    pass


NDIS_INTERFACE_INFORMATION = _NDIS_INTERFACE_INFORMATION
PNDIS_INTERFACE_INFORMATION = POINTER(_NDIS_INTERFACE_INFORMATION)



if not defined(_IFDEF_):
    _IFDEF_ = VOID
    from winapifamily_h import * # NOQA
        if defined(__cplusplus):
            pass
        # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # Get definitions for IFTYPE and IF_ACCESS_TYPE.
        from ipifcons_h import * # NOQA


        # Define compartment ID type:
        NET_IF_COMPARTMENT_ID = UINT32
        PNET_IF_COMPARTMENT_ID = POINTER(UINT32)
        NET_IF_COMPARTMENT_ID_UNSPECIFIED = (NET_IF_COMPARTMENT_ID)0
        NET_IF_COMPARTMENT_ID_PRIMARY = (NET_IF_COMPARTMENT_ID)1


        # Define NetworkGUID type:
        NET_IF_NETWORK_GUID = GUID
        PNET_IF_NETWORK_GUID = POINTER(GUID)


        class _NET_IF_OPER_STATUS(ENUM): # ifOperStatus
            NET_IF_OPER_STATUS_UP = 1
            NET_IF_OPER_STATUS_DOWN = 2
            NET_IF_OPER_STATUS_TESTING = 3
            NET_IF_OPER_STATUS_UNKNOWN = 4
            NET_IF_OPER_STATUS_DORMANT = 5
            NET_IF_OPER_STATUS_NOT_PRESENT = 6
            NET_IF_OPER_STATUS_LOWER_LAYER_DOWN = 7

        NET_IF_OPER_STATUS = _NET_IF_OPER_STATUS
        PNET_IF_OPER_STATUS = POINTER(_NET_IF_OPER_STATUS)
        NET_IF_OBJECT_ID = ULONG32
        PNET_IF_OBJECT_ID = POINTER(ULONG32)


        class _NET_IF_ADMIN_STATUS(ENUM): # ifAdminStatus
            NET_IF_ADMIN_STATUS_UP = 1
            NET_IF_ADMIN_STATUS_DOWN = 2
            NET_IF_ADMIN_STATUS_TESTING = 3

        NET_IF_ADMIN_STATUS = _NET_IF_ADMIN_STATUS
        PNET_IF_ADMIN_STATUS = POINTER(_NET_IF_ADMIN_STATUS)


        # Flags to extend operational status
        NET_IF_OPER_STATUS_DOWN_NOT_AUTHENTICATED = 0x00000001
        NET_IF_OPER_STATUS_DOWN_NOT_MEDIA_CONNECTED = 0x00000002
        NET_IF_OPER_STATUS_DORMANT_PAUSED = 0x00000004
        NET_IF_OPER_STATUS_DORMANT_LOW_POWER = 0x00000008
        NET_IF_COMPARTMENT_SCOPE = UINT32
        PNET_IF_COMPARTMENT_SCOPE = POINTER(UINT32)
        NET_IF_COMPARTMENT_SCOPE_UNSPECIFIED = (NET_IF_COMPARTMENT_SCOPE)0
        NET_IF_COMPARTMENT_SCOPE_ALL = (NET_IF_COMPARTMENT_SCOPE)-1
        NET_IF_OID_IF_ALIAS = 0x00000001        # identifies the ifAlias string for an interface
        NET_IF_OID_COMPARTMENT_ID = 0x00000002        # identifies the compartment ID for an interface.
        NET_IF_OID_NETWORK_GUID = 0x00000003        # identifies the NetworkGuid for an interface.
        NET_IF_OID_IF_ENTRY = 0x00000004        # identifies statistics for an interface.


        # Define macros for an "unspecified" NetworkGUID value to be used in
        # structures
        # that haven't had the NET_LUID field filled in yet.
        NET_SET_UNSPECIFIED_NETWORK_GUID(_pNetworkGuid) = VOID
        NET_IS_UNSPECIFIED_NETWORK_GUID(_NetworkGuidValue) = VOID


        # To prevent collisions between user-assigned and system-assigned
        # site-ids,
        # we partition the site-id space into two:
        # 1. User-Assigned: NET_SITEID_UNSPECIFIED < SiteId <
        # NET_SITEID_MAXUSER
        # 2. System-Assigned: NET_SITEID_MAXUSER < SiteId <
        # NET_SITEID_MAXSYSTEM
        # Note: A network's SiteId doesn't really need to be settable.
        # 1. The network profile manager creates a network per network profile.
        # 2. NDIS/IF assigns a unique SiteId to each network.
        NET_SITEID_UNSPECIFIED = 0
        NET_SITEID_MAXUSER = 0x07FFFFFF
        NET_SITEID_MAXSYSTEM = 0x0FFFFFFF


        class _NET_IF_RCV_ADDRESS_TYPE(ENUM): # ifRcvAddressType
            NET_IF_RCV_ADDRESS_TYPE_OTHER = 1
            NET_IF_RCV_ADDRESS_TYPE_VOLATILE = 2
            NET_IF_RCV_ADDRESS_TYPE_NON_VOLATILE = 3

        NET_IF_RCV_ADDRESS_TYPE = _NET_IF_RCV_ADDRESS_TYPE
        PNET_IF_RCV_ADDRESS_TYPE = POINTER(_NET_IF_RCV_ADDRESS_TYPE)

        _NET_IF_RCV_ADDRESS_LH._fields_ = [
            ('ifRcvAddressType', NET_IF_RCV_ADDRESS_TYPE),
            ('ifRcvAddressLength', USHORT),
            # from beginning of this struct
            ('ifRcvAddressOffset', USHORT),
        ]

        _NET_IF_ALIAS_LH._fields_ = [
            # in bytes, of ifAlias string
            ('ifAliasLength', USHORT),
            # in bytes, from beginning of this struct
            ('ifAliasOffset', USHORT),
        ]


        class Info(ctypes.Structure):
            pass


        Info._fields_ = [
            ('Reserved', ULONG64, 24),
            ('NetLuidIndex', ULONG64, 24),
            # equal to IANA IF type
            ('IfType', ULONG64, 16),
        ]
        _NET_LUID_LH.Info = Info


        _NET_LUID_LH._fields_ = [
            ('Value', ULONG64),
            ('Info', _NET_LUID_LH.Info),
        ]
        if NTDDI_VERSION >= NTDDI_VISTA:
            NET_IF_RCV_ADDRESS = NET_IF_RCV_ADDRESS_LH
            PNET_IF_RCV_ADDRESS = POINTER(NET_IF_RCV_ADDRESS)
            NET_IF_ALIAS = NET_IF_ALIAS_LH
            PNET_IF_ALIAS = POINTER(NET_IF_ALIAS)
        # END IF  NTDDI_VISTA

        # Need to make this visible on all platforms
        # (for the purpose of IF_LUID).
        NET_LUID = NET_LUID_LH
        PNET_LUID = POINTER(NET_LUID)

        # IF_LUID
        # Define the locally unique datalink interface identifier type.
        # This type is persistable.
        IF_LUID = NET_LUID
        PIF_LUID = POINTER(NET_LUID)

        # Interface Index (ifIndex)
        NET_IFINDEX = ULONG
        PNET_IFINDEX = POINTER(ULONG)

        # Interface Type (IANA ifType)
        NET_IFTYPE = UINT16
        PNET_IFTYPE = POINTER(UINT16)
        NET_IFINDEX_UNSPECIFIED = NET_IFINDEX)(0        # Not a valid ifIndex
        NET_IFLUID_UNSPECIFIED = 0        # Not a valid if Luid
        if not defined(__IF_INDEX_DEFINED__):
            __IF_INDEX_DEFINED__ = VOID


            # IF_INDEX
            # Define the interface index type.
            # This type is not persistable.
            # This must be UINT (not an enum) to replace previous uses of
            # an index that used a DWORD type.
        # END IF   __IF_INDEX_DEFINED__

        IF_INDEX = NET_IFINDEX
        PIF_INDEX = POINTER(NET_IFINDEX)


        class _NET_IF_CONNECTION_TYPE(ENUM):
            NET_IF_CONNECTION_DEDICATED = 1
            NET_IF_CONNECTION_PASSIVE = 2
            NET_IF_CONNECTION_DEMAND = 3
            NET_IF_CONNECTION_MAXIMUM = 4

        NET_IF_CONNECTION_TYPE = _NET_IF_CONNECTION_TYPE
        PNET_IF_CONNECTION_TYPE = POINTER(_NET_IF_CONNECTION_TYPE)

        # Types of tunnels
        # (sub-type of IF_TYPE when IF_TYPE is IF_TYPE_TUNNEL).
        class TUNNEL_TYPE(ENUM):
            TUNNEL_TYPE_NONE = 0
            TUNNEL_TYPE_OTHER = 1
            TUNNEL_TYPE_DIRECT = 2
            TUNNEL_TYPE_6TO4 = 11
            TUNNEL_TYPE_ISATAP = 13
            TUNNEL_TYPE_TEREDO = 14
            TUNNEL_TYPE_IPHTTPS = 15

        PTUNNEL_TYPE = POINTER(TUNNEL_TYPE)


        TUNNEL_TYPE_NONE = TUNNEL_TYPE.TUNNEL_TYPE_NONE
        TUNNEL_TYPE_OTHER = TUNNEL_TYPE.TUNNEL_TYPE_OTHER
        TUNNEL_TYPE_DIRECT = TUNNEL_TYPE.TUNNEL_TYPE_DIRECT
        TUNNEL_TYPE_6TO4 = TUNNEL_TYPE.TUNNEL_TYPE_6TO4
        TUNNEL_TYPE_ISATAP = TUNNEL_TYPE.TUNNEL_TYPE_ISATAP
        TUNNEL_TYPE_TEREDO = TUNNEL_TYPE.TUNNEL_TYPE_TEREDO
        TUNNEL_TYPE_IPHTTPS = TUNNEL_TYPE.TUNNEL_TYPE_IPHTTPS
        IFI_UNSPECIFIED = NET_IFINDEX_UNSPECIFIED

        # Definitions for NET_IF_INFORMATION.Flags
        NIIF_HARDWARE_INTERFACE = 0x00000001        # Set iff hardware
        NIIF_FILTER_INTERFACE = 0x00000002
        NIIF_NDIS_RESERVED1 = 0x00000004
        NIIF_NDIS_RESERVED2 = 0x00000008
        NIIF_NDIS_RESERVED3 = 0x00000010
        NIIF_NDIS_WDM_INTERFACE = 0x00000020
        NIIF_NDIS_ENDPOINT_INTERFACE = 0x00000040
        NIIF_NDIS_ISCSI_INTERFACE = 0x00000080
        NIIF_NDIS_RESERVED4 = 0x00000100
        NIIF_WAN_TUNNEL_TYPE_UNKNOWN = (-1)

        # Define datalink interface access types.
        class _NET_IF_ACCESS_TYPE(ENUM):
            NET_IF_ACCESS_LOOPBACK = 1
            NET_IF_ACCESS_BROADCAST = 2
            NET_IF_ACCESS_POINT_TO_POINT = 3
            NET_IF_ACCESS_POINT_TO_MULTI_POINT = 4
            NET_IF_ACCESS_MAXIMUM = 5

        NET_IF_ACCESS_TYPE = _NET_IF_ACCESS_TYPE
        PNET_IF_ACCESS_TYPE = POINTER(_NET_IF_ACCESS_TYPE)

        # Define datalink interface direction types.
        class _NET_IF_DIRECTION_TYPE(ENUM):
            NET_IF_DIRECTION_SENDRECEIVE = 1
            NET_IF_DIRECTION_SENDONLY = 2
            NET_IF_DIRECTION_RECEIVEONLY = 3
            NET_IF_DIRECTION_MAXIMUM = 4

        NET_IF_DIRECTION_TYPE = _NET_IF_DIRECTION_TYPE
        PNET_IF_DIRECTION_TYPE = POINTER(_NET_IF_DIRECTION_TYPE)


        class _NET_IF_MEDIA_CONNECT_STATE(ENUM):
            MediaConnectStateUnknown = 1
            MediaConnectStateConnected = 2
            MediaConnectStateDisconnected = 3

        NET_IF_MEDIA_CONNECT_STATE = _NET_IF_MEDIA_CONNECT_STATE
        PNET_IF_MEDIA_CONNECT_STATE = POINTER(_NET_IF_MEDIA_CONNECT_STATE)
        NET_IF_LINK_SPEED_UNKNOWN = (ULONG64)(-1)

        # Defines the duplex state of media
        class _NET_IF_MEDIA_DUPLEX_STATE(ENUM):
            MediaDuplexStateUnknown = 1
            MediaDuplexStateHalf = 2
            MediaDuplexStateFull = 3

        NET_IF_MEDIA_DUPLEX_STATE = _NET_IF_MEDIA_DUPLEX_STATE
        PNET_IF_MEDIA_DUPLEX_STATE = POINTER(_NET_IF_MEDIA_DUPLEX_STATE)

        # Special values for fields in NET_PHYSICAL_LOCATION
        NIIF_BUS_NUMBER_UNKNOWN = (-1)
        NIIF_SLOT_NUMBER_UNKNOWN = (-1)
        NIIF_FUNCTION_NUMBER_UNKNOWN = (-1)


        _NET_PHYSICAL_LOCATION_LH._fields_ = [
            # Physical location
            ('BusNumber', ULONG),
            # ... for hardware
            ('SlotNumber', ULONG),
            # ... devices.
            ('FunctionNumber', ULONG),
        ]

        # maximum string size in -wchar- units
        IF_MAX_STRING_SIZE = 256


        _IF_COUNTED_STRING_LH._fields_ = [
            # in -Bytes-
            ('Length', USHORT),
            ('String', WCHAR * IF_MAX_STRING_SIZE + 1),
        ]
        IF_MAX_PHYS_ADDRESS_LENGTH = 32


        _IF_PHYSICAL_ADDRESS_LH._fields_ = [
            ('Length', USHORT),
            ('Address', UCHAR * IF_MAX_PHYS_ADDRESS_LENGTH),
        ]
        if NTDDI_VERSION >= NTDDI_VISTA:
            NET_PHYSICAL_LOCATION = NET_PHYSICAL_LOCATION_LH
            PNET_PHYSICAL_LOCATION = POINTER(NET_PHYSICAL_LOCATION)
            IF_COUNTED_STRING = IF_COUNTED_STRING_LH
            PIF_COUNTED_STRING = POINTER(IF_COUNTED_STRING)
            IF_PHYSICAL_ADDRESS = IF_PHYSICAL_ADDRESS_LH
            PIF_PHYSICAL_ADDRESS = POINTER(IF_PHYSICAL_ADDRESS)
        # END IF


        # IF_ADMINISTRATIVE_STATE
        # Datalink Interface Administrative State.
        # Indicates whether the interface has been administratively enabled.
        class _IF_ADMINISTRATIVE_STATE(ENUM):
            IF_ADMINISTRATIVE_DISABLED = 1
            IF_ADMINISTRATIVE_ENABLED = 2
            IF_ADMINISTRATIVE_DEMANDDIAL = 3

        IF_ADMINISTRATIVE_STATE = _IF_ADMINISTRATIVE_STATE
        PIF_ADMINISTRATIVE_STATE = POINTER(_IF_ADMINISTRATIVE_STATE)


        # Note: Interface is Operational iff
        # ((MediaSense is Connected) and (AdministrativeState is Enabled))
        # or
        # ((MediaSense is Connected) and (AdministrativeState is OnDemand))
        # not Operational iff
        # ((MediaSense != Connected) or (AdministrativeState is Disabled))
        # OperStatus values from RFC 2863
        class IF_OPER_STATUS(ENUM):
            IfOperStatusUp = 1
            IfOperStatusDown = 2
            IfOperStatusTesting = 3
            IfOperStatusUnknown = 4
            IfOperStatusDormant = 5
            IfOperStatusNotPresent = 6
            IfOperStatusLowerLayerDown = 7

        IfOperStatusUp = IF_OPER_STATUS.IfOperStatusUp
        IfOperStatusDown = IF_OPER_STATUS.IfOperStatusDown
        IfOperStatusTesting = IF_OPER_STATUS.IfOperStatusTesting
        IfOperStatusUnknown = IF_OPER_STATUS.IfOperStatusUnknown
        IfOperStatusDormant = IF_OPER_STATUS.IfOperStatusDormant
        IfOperStatusNotPresent = IF_OPER_STATUS.IfOperStatusNotPresent
        IfOperStatusLowerLayerDown = IF_OPER_STATUS.IfOperStatusLowerLayerDown

        _NDIS_INTERFACE_INFORMATION._fields_ = [
            # rod fields
            ('ifOperStatus', NET_IF_OPER_STATUS),
            ('ifOperStatusFlags', ULONG),
            ('MediaConnectState', NET_IF_MEDIA_CONNECT_STATE),
            ('MediaDuplexState', NET_IF_MEDIA_DUPLEX_STATE),
            ('ifMtu', ULONG),
            ('ifPromiscuousMode', BOOLEAN),
            ('ifDeviceWakeUpEnable', BOOLEAN),
            ('XmitLinkSpeed', ULONG64),
            ('RcvLinkSpeed', ULONG64),
            ('ifLastChange', ULONG64),
            ('ifCounterDiscontinuityTime', ULONG64),
            ('ifInUnknownProtos', ULONG64),
            # OID_GEN_RCV_DISCARDS = OID_GEN_RCV_ERROR + OID_GEN_RCV_NO_BUFFER
            ('ifInDiscards', ULONG64),
            # OID_GEN_RCV_ERROR
            ('ifInErrors', ULONG64),
            # OID_GEN_BYTES_RCV = OID_GEN_DIRECTED_BYTES_RCV +
            # OID_GEN_MULTICAST_BYTES_RCV + OID_GEN_BROADCAST_BYTES_RCV
            ('ifHCInOctets', ULONG64),
            # OID_GEN_DIRECTED_FRAMES_RCV
            ('ifHCInUcastPkts', ULONG64),
            # OID_GEN_MULTICAST_FRAMES_RCV
            ('ifHCInMulticastPkts', ULONG64),
            # OID_GEN_BROADCAST_FRAMES_RCV
            ('ifHCInBroadcastPkts', ULONG64),
            # OID_GEN_BYTES_XMIT = OID_GEN_DIRECTED_BYTES_XMIT +
            # OID_GEN_MULTICAST_BYTES_XMIT + OID_GEN_BROADCAST_BYTES_XMIT
            ('ifHCOutOctets', ULONG64),
            # OID_GEN_DIRECTED_FRAMES_XMIT
            ('ifHCOutUcastPkts', ULONG64),
            # OID_GEN_MULTICAST_FRAMES_XMIT
            ('ifHCOutMulticastPkts', ULONG64),
            # OID_GEN_BROADCAST_FRAMES_XMIT
            ('ifHCOutBroadcastPkts', ULONG64),
            # OID_GEN_XMIT_ERROR
            ('ifOutErrors', ULONG64),
            # OID_GEN_XMIT_DISCARDS
            ('ifOutDiscards', ULONG64),
            # OID_GEN_DIRECTED_BYTES_RCV
            ('ifHCInUcastOctets', ULONG64),
            # OID_GEN_MULTICAST_BYTES_RCV
            ('ifHCInMulticastOctets', ULONG64),
            # OID_GEN_BROADCAST_BYTES_RCV
            ('ifHCInBroadcastOctets', ULONG64),
            # OID_GEN_DIRECTED_BYTES_XMIT
            ('ifHCOutUcastOctets', ULONG64),
            # OID_GEN_MULTICAST_BYTES_XMIT
            ('ifHCOutMulticastOctets', ULONG64),
            # OID_GEN_BROADCAST_BYTES_XMIT
            ('ifHCOutBroadcastOctets', ULONG64),
            ('CompartmentId', NET_IF_COMPARTMENT_ID),
            ('SupportedStatistics', ULONG),
        ]
        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
# END IF   _IFDEF_


