import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *
from pyWinAPI.shared.bthdef_h import *
from pyWinAPI.km.wdm_h import *


__BTHDDI_H__ = None

# + + Copyright (c) 2000 Microsoft Corporation Module Name: BTHDDI.H Abstract:
# Public structures common to the BTHPORT and BTH client device drivers
# Environment: Kernel & user mode Revision History: - -
if not defined(__BTHDDI_H__):
    __BTHDDI_H__ = 1

    if _MSC_VER >= 1200:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:

        # DEFINES

        # BTHPORT BRB header context size.
        BTHPORT_CONTEXT_SIZE = 4
        BTHPORT_RESERVED_FIELD_SIZE = 2

        # ////////////////////// NOTES
        # ///////////////////////////////////////////////

        # 1) BRB Clients need to send IRP_MJ_INTERNAL_DEVICE_CONTROL to
        # the BTH Port driver with IOCTL_INTERNAL_BTH_SUBMIT_BRB Device I/O
        # code.
        # In addition, the client driver needs to pass a BRB pointer in
        # Argument1
        # of IRP stack location.

        # 2) Client drivers can submit data buffers of either type MDL, or PVOID
        # buffer but not both.

        # 3) Client drivers need to QI the bus driver before they can submit any BRB.
        # This is necessary in order to provide the event callback entry
        # points.

        # Optional event handlers are designated as such with [O] in the
        # BTHPORT_INTERFACE structure below.

        # ///////////////////////////////////////////////////////////////////////////
        #

        # /////////////////////////////////////////////////////////////////////////////
        #

        # Possible error codes returned by the bus driver.

        # STATUS_PENDING : Request is queued for execution.
        # STATUS_SUCCESS: Request completed successfully.
        # STATUS_INSUFFICIENT_RESOURCES: request failed due to lack of
        # resources.
        # STATUS_UNSUCCESSFUL: Request did not complte successfully.
        # STATUS_CANCELLED: BRB/IRP was cancelled .
        # STATUS_INVALID_PARAMETER: sumbitted BRB has invalid paramters.
        # STATUS_INVALID_DEVICE_REQUEST: undefined request.
        # STATUS_PROTOCOL_UNREACHBLE: remote device did not accept the
        # l2cap connection with the specified PSM.
        # STATUS_DEVICE_CONFIGURATION_ERROR: remote device did not
        # agree to L2cap default configuration parameters and/or MTU size.
        # STATUS_DEVICE_NOT_EXIST: Radio is not available.
        # STATUS_BUFFER_TOO_SMALL: client submitted buffer is too small.

        # The following Bluetooth error codes will be mapped to NTSTATUS code:

        # BTHSTATUS:      NTSTATUS: BTH_ERROR_SUCCESS     STATUS_SUCCESS
        # BTH_ERROR_NO_CONNECTION STATUS_INVALID_HANDLE
        # BTH_ERROR_HARDWARE_FAILURE STATUS_ADAPTER_HARDWARE_ERROR
        # BTH_ERROR_PAGE_TIMEOUT STATUS_TIMEOUT
        # BTH_ERROR_AUTHENTICATION_FAILURE STATUS_MUTUAL_AUTHENTICATION_FAILED
        # BTH_ERROR_KEY_MISSING STATUS_NO_USER_SESSION_KEY
        # BTH_ERROR_MEMORY_FULL STATUS_INSUFFICIENT_RESOURCES
        # BTH_ERROR_CONNECTION_TIMEOUT STATUS_LINK_TIMEOUT
        # BTH_ERROR_MAX_NUMBER_OF_CONNECTIONS STATUS_CONNECTION_COUNT_LIMIT
        # BTH_ERROR_MAX_NUMBER_OF_SCO_CONNECTIONS
        # STATUS_CONNECTION_COUNT_LIMIT
        # BTH_ERROR_ACL_CONNECTION_ALREADY_EXISTS STATUS_CONNECTION_IN_USE
        # BTH_ERROR_COMMAND_DISALLOWED STATUS_INVALID_PARAMETER
        # BTH_ERROR_HOST_REJECTED_LIMITED_RESOURCES
        # STATUS_INSUFFICIENT_RESOURCES
        # BTH_ERROR_HOST_REJECTED_SECURITY_REASONS STATUS_CONNECTION_REFUSED
        # BTH_ERROR_HOST_REJECTED_PERSONAL_DEVICE STATUS_CONNECTION_REFUSED
        # BTH_ERROR_HOST_TIMEOUT STATUS_TIMEOUT
        # BTH_ERROR_UNSUPPORTED_FEATURE_OR_PARAMETER STATUS_INVALID_PARAMETER
        # BTH_ERROR_INVALID_HCI_PARAMETER STATUS_INVALID_PARAMETER
        # BTH_ERROR_REMOTE_USER_ENDED_CONNECTION STATUS_REMOTE_DISCONNECT
        # BTH_ERROR_REMOTE_LOW_RESOURCES STATUS_REMOTE_RESOURCES
        # BTH_ERROR_REMOTE_POWERING_OFF STATUS_REMOTE_RESOURCES
        # BTH_ERROR_LOCAL_HOST_TERMINATED_CONNECTION
        # STATUS_CONNECTION_DISCONNECTED BTH_ERROR_PAIRING_NOT_ALLOWED
        # STATUS_MUTUAL_AUTHENTICATION_FAILED
        # BTH_ERROR_UNSUPPORTED_REMOTE_FEATURE STATUS_ADAPTER_HARDWARE_ERROR
        # BTH_ERROR_UNSPECIFIED_ERROR STATUS_ADAPTER_HARDWARE_ERROR
        # BTH_ERROR_ROLE_CHANGE_NOT_ALLOWED STATUS_INVALID_PARAMETER

        # version for QI, encoded in binary encoded decimal, ie 1.0
        BTHDDI_ENUMERATOR_INTERFACE_VERSION_FOR_QI = 0x0200
        BTHDDI_PROFILE_DRIVER_INTERFACE_VERSION_FOR_QI = 0x0200

        # Create - enumerate the PDO, the device is in range
        # Remove - remove the PDO, the device is in range
        # Destroy - force remove the PDO, the user no LONGer wants to use this
        # protocol / service

        ENUMERATORACTION = None

        if not defined(ENUMERATORACTION):
            class _ENUMERATOR_ACTION(ENUM):
                ENUMERATOR_ACTION_CREATE = 0
                ENUMERATOR_ACTION_REMOVE = 1
                ENUMERATOR_ACTION_DESTROY = 2
                ENUMERATOR_ACTION_MAX = 3


            ENUMERATOR_ACTION = _ENUMERATOR_ACTION
            PENUMERATOR_ACTION = POINTER(_ENUMERATOR_ACTION)
        # END IF  ENUMERATOR_ACTION

        class _ENUMERATOR_TYPE(ENUM):
            ENUMERATOR_TYPE_PROTOCOL = 0
            ENUMERATOR_TYPE_SERVICE = 1
            ENUMERATOR_TYPE_DEVICE = 2
            ENUMERATOR_TYPE_MAX = 3


        ENUMERATOR_TYPE = _ENUMERATOR_TYPE
        PENUMERATOR_TYPE = POINTER(_ENUMERATOR_TYPE)

        # BTH_ENUMERATOR_INFO Flags
        BTH_ENUMERATORFL_INCOMING = 0x00000001
        BTH_ENUMERATORFL_OUTGOING = 0x00000002
        BTH_ENUMERATORFL_REENUM = 0x00000004


        class _BTH_ENUMERATOR_INFO(ctypes.Structure):
            pass


        _BTH_ENUMERATOR_INFO._fields_ = [
            ('EnumeratorType', ENUMERATOR_TYPE), # Type of connection being requested
            ('Action', ENUMERATOR_ACTION), # Action to take
            ('Port', ULONG), # DLCI if this is an RFCOMM connection request.
            ('Flags', ULONG), # Flags
            ('Guid', GUID), # Protocol / Service UUID for the enumeration action

            # Instance ID of the Protocol / Service for
            # BTH_ENUMERATORFL_INCOMING
            ('InstanceId', ULONG),

            # Instance ID str of the Protocol / Service for
            # BTH_ENUMERATORFL_OUTGOING
            ('InstanceIdStr', WCHAR * BTH_MAX_SERVICE_NAME_SIZE),
            ('Vid', USHORT), # Vendor ID, retrieved from DI SDP record
            ('Pid', USHORT), # Product ID, retrieved from DI SDP record
            ('Mfg', USHORT), # Manufacturer, retrieved from DI SDP record
            ('LocalMfg', USHORT), # Local radio manufacturer, retreived via HCI Command
            ('VidType', USHORT), # Vendor ID type, retrieved from DI SDP record
            ('ServiceName', WCHAR * BTH_MAX_SERVICE_NAME_SIZE), # Service Name (Used for local services)
            ('SdpPriLangServiceName', CHAR * BTH_MAX_SERVICE_NAME_SIZE), # Identifier used for remote services.
            ('DeviceString', WCHAR * BTH_MAX_SERVICE_NAME_SIZE), # Device string passed down on BTH_UPDATE ADD
        ]
        BTH_ENUMERATOR_INFO = _BTH_ENUMERATOR_INFO
        PBTH_ENUMERATOR_INFO = POINTER(_BTH_ENUMERATOR_INFO)
        L2CAP_CHANNEL_HANDLE = PVOID
        L2CAP_SERVER_HANDLE = PVOID
        SCO_SERVER_HANDLE = PVOID

        # BRB types..

        BRBTYPE = None
        if not defined(BRBTYPE):
            class _BRB_TYPE(ENUM):
                BRB_HCI_GET_LOCAL_BD_ADDR = 0x0001
                BRB_L2CA_REGISTER_SERVER = 0x0100
                BRB_L2CA_UNREGISTER_SERVER = 0x0101
                BRB_L2CA_OPEN_CHANNEL = 0x0102
                BRB_L2CA_OPEN_CHANNEL_RESPONSE = 0x0103
                BRB_L2CA_CLOSE_CHANNEL = 0x0104
                BRB_L2CA_ACL_TRANSFER = 0x0105
                BRB_L2CA_UPDATE_CHANNEL = 0x0106
                BRB_L2CA_PING = 0x0107
                BRB_L2CA_INFO_REQUEST = 0x0108
                BRB_REGISTER_PSM = 0x0109
                BRB_UNREGISTER_PSM = 0x010A
                BRB_SCO_REGISTER_SERVER = 0x0200
                BRB_SCO_UNREGISTER_SERVER = 0x0201
                BRB_SCO_OPEN_CHANNEL = 0x0202
                BRB_SCO_OPEN_CHANNEL_RESPONSE = 0x0203
                BRB_SCO_CLOSE_CHANNEL = 0x0204
                BRB_SCO_TRANSFER = 0x0205
                BRB_SCO_GET_CHANNEL_INFO = 0x0207
                BRB_SCO_GET_SYSTEM_INFO = 0x0209
                BRB_SCO_FLUSH_CHANNEL = 0x020A
                BRB_SCO_OPEN_UNMANAGED_CHANNEL = 0x0210
                BRB_SCO_OPEN_UNMANAGED_CHANNEL_RESPONSE = 0x0211

                if NTDDI_VERSION >= NTDDI_WIN8:
                    BRB_L2CA_OPEN_ENHANCED_CHANNEL = 0x0212
                    BRB_L2CA_OPEN_ENHANCED_CHANNEL_RESPONSE = 0x0213

                # END IF
                BRB_ACL_GET_MODE = 0x0300
                BRB_ACL_ENTER_ACTIVE_MODE = 0x0301
                BRB_STORED_LINK_KEY = 0x0310
                BRB_GET_DEVICE_INTERFACE_STRING = 0x0320


            BRB_TYPE = _BRB_TYPE
        # END IF

        class _BRB_VERSION(ENUM):
            BLUETOOTH_V1 = 0
            BLUETOOTH_V2 = 1


        BRB_VERSION = _BRB_VERSION

        # BRB HEADER
        class _BRB_HEADER(ctypes.Structure):
            pass


        _BRB_HEADER._fields_ = [
            ('ListEntry', LIST_ENTRY), # to enqueue the BRB.
            ('Length', ULONG), # [IN] Size of the BRB including this header
            ('Version', USHORT), # BRB_VERSION
            ('Type', USHORT), # BRB_TYPE
            ('BthportFlags', ULONG), # [PRIVATE] Internal flags for use by BTHPORT
            ('Status', NTSTATUS), # [OUT] BRB completion status
            ('BtStatus', BTHSTATUS), # [OUT] BRB completion BtStatus
            ('Context', PVOID * BTHPORT_CONTEXT_SIZE), # [PRIVATE] for internal use by BTHPORT only.
            ('ClientContext', PVOID * BTHPORT_CONTEXT_SIZE), # for use by client drivers, BTHPORT will never touch these fields.
            ('Reserved', ULONG * BTHPORT_RESERVED_FIELD_SIZE), # opaque reserved fields
        ]
        BRB_HEADER = _BRB_HEADER


        class _L2CAP_CONFIG_RANGE(ctypes.Structure):
            pass


        _L2CAP_CONFIG_RANGE._fields_ = [
            ('Min', USHORT),
            ('Max', USHORT),
        ]
        L2CAP_CONFIG_RANGE = _L2CAP_CONFIG_RANGE
        PL2CAP_CONFIG_RANGE = POINTER(_L2CAP_CONFIG_RANGE)


        class _L2CAP_CONFIG_VALUE_RANGE(ctypes.Structure):
            pass


        _L2CAP_CONFIG_VALUE_RANGE._fields_ = [
            ('Min', USHORT),
            ('Preferred', USHORT),
            ('Max', USHORT),
        ]
        L2CAP_CONFIG_VALUE_RANGE = _L2CAP_CONFIG_VALUE_RANGE
        PL2CAP_CONFIG_VALUE_RANGE = POINTER(_L2CAP_CONFIG_VALUE_RANGE)

        # Needs packing to match exact spec size


        class _L2CAP_FLOWSPEC(ctypes.Structure):
            pass


        _L2CAP_FLOWSPEC._fields_ = [
            ('Flags', UCHAR), # Reserved. Must be zero.
            ('ServiceType', UCHAR), # L2CAP_FLOW_SERVICE_TYPE_XXX value
            ('TokenRate', ULONG), # Bytes/sec
            ('TokenBucketSize', ULONG), # Bytes
            ('PeakBandwidth', ULONG), # Bytes/sec
            ('Latency', ULONG), # Microsoeonds
            ('DelayVariation', ULONG), # Microseconds
        ]
        L2CAP_FLOWSPEC = _L2CAP_FLOWSPEC
        PL2CAP_FLOWSPEC = POINTER(_L2CAP_FLOWSPEC)

        if NTDDI_VERSION >= NTDDI_WIN8:
            class _L2CAP_RETRANSMISSION_AND_FLOW_CONTROL(ctypes.Structure):
                pass


            _L2CAP_RETRANSMISSION_AND_FLOW_CONTROL._fields_ = [
                ('Mode', UCHAR), # Requested mode for the link.
                ('TxWindowSize', UCHAR), # supported and it has range 1 to 63.

                # in Retransmission mode and Enhanced Retransmission mode.
                # Minimum is 1.
                ('MaxTransmit', UCHAR),
                ('RetransmissionTO', USHORT), # Retransmission timeout
                ('MonitorTO', USHORT), # Monitor timeout
                ('MaxPDUSize', USHORT), # Maximum PDU Size
            ]
            L2CAP_RETRANSMISSION_AND_FLOW_CONTROL = _L2CAP_RETRANSMISSION_AND_FLOW_CONTROL
            PL2CAP_RETRANSMISSION_AND_FLOW_CONTROL = POINTER(_L2CAP_RETRANSMISSION_AND_FLOW_CONTROL)


            class _L2CAP_EXTENDED_FLOW_SPEC(ctypes.Structure):
                pass


            _L2CAP_EXTENDED_FLOW_SPEC._fields_ = [
                ('Identifier', UCHAR), # unique identifier for the flow specification
                ('ServiceType', UCHAR), # Indicates level of service required.
                ('MaxSDUSize', USHORT), # Maximum size of SDUs transmitted by the application.

                # Time between consecutive SDUs generated by the application
                # in microseconds.
                ('SDUInterArrivalTime', ULONG),
                ('AccessLatency', ULONG), # of the connection.
                ('FlushTimeout', ULONG), # and the controller.
            ]
            L2CAP_EXTENDED_FLOW_SPEC = _L2CAP_EXTENDED_FLOW_SPEC
            PL2CAP_EXTENDED_FLOW_SPEC = POINTER(_L2CAP_EXTENDED_FLOW_SPEC)
        # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

        # Use the DynamicBuffer field
        CO_DYNAMIC = 0x0001

        # Use the FixedBuffer field
        CO_FIXED = 0x0002

        # The option is unknown. Used during config request validation
        # callback, not

        # a valid flag when submitting options to bthport.
        CO_UNKNOWN = 0x0004
        VALID_CO_FLAGS = CO_DYNAMIC | CO_FIXED


        def IS_CO_TYPE_HINT(type):
            return (type & 0x80) == 0x80


        def IS_CO_TYPE_REQUIRED(type):
            return (type & 0x80) == 0x00


        CO_TYPE = UCHAR
        PCO_TYPE = POINTER(UCHAR)
        CO_LENGTH = UCHAR
        PCO_LENGTH = POINTER(UCHAR)
        CO_MTU = USHORT
        PCO_MTU = POINTER(USHORT)
        CO_FLUSHTO = USHORT
        PCO_FLUSHTO = POINTER(USHORT)

        if NTDDI_VERSION >= NTDDI_WIN8:
            CO_FCS = UCHAR
            PCO_FCS = POINTER(UCHAR)
            CO_EXTENDED_WINDOW_SIZE = USHORT
            PCO_EXTENDED_WINDOW_SIZE = POINTER(USHORT)
        # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

        # Config Option (CO) header
        class _CO_HEADER(ctypes.Structure):
            pass


        _CO_HEADER._fields_ = [

            # Type of vendor - specific option. can be either an option or a
            # hint.
            ('Type', CO_TYPE),
            ('Length', CO_LENGTH), # Size of the vendor - specific option.
        ]
        CO_HEADER = _CO_HEADER

        # HCI connection handle.
        CONNECTION_HANDLE = USHORT
        PCONNECTION_HANDLE = POINTER(USHORT)

        # HCI SCO Requests
        SCO_CHANNEL_HANDLE = PVOID
        PSCO_CHANNEL_HANDLE = POINTER(PVOID)

        # SCO retransmission effort.
        class _SCO_RETRANSMISSION_EFFORT(ENUM):
            SCO_RETRANSMISSION_NONE = 0x00
            SCO_RETRANSMISSION_MIN1_POWER = 0x01
            SCO_RETRANSMISSION_MIN1_QUALITY = 0x02
            SCO_RETRANSMISSION_DONT_CARE = 0xFF


        SCO_RETRANSMISSION_EFFORT = _SCO_RETRANSMISSION_EFFORT
        PSCO_RETRANSMISSION_EFFORT = POINTER(_SCO_RETRANSMISSION_EFFORT)

        # SCO voice setting.
        SCO_VS_IN_CODING_MASK = 0x0300
        SCO_VS_IN_CODING_LINEAR = 0x0000
        SCO_VS_IN_CODING_MULAW = 0x0100
        SCO_VS_IN_CODING_ALAW = 0x0200
        SCO_VS_IN_DATA_FORMAT_MASK = 0x00C0
        SCO_VS_IN_DATA_FORMAT_1C = 0x0000
        SCO_VS_IN_DATA_FORMAT_2C = 0x0040
        SCO_VS_IN_DATA_FORMAT_SM = 0x0080
        SCO_VS_IN_DATA_FORMAT_US = 0x00C0
        SCO_VS_IN_SAMPLE_SIZE_MASK = 0x0020
        SCO_VS_IN_SAMPLE_SIZE_8BIT = 0x0000
        SCO_VS_IN_SAMPLE_SIZE_16BIT = 0x0020
        SCO_VS_PCM_BIT_POS_MASK = 0x001C
        SCO_VS_AIR_CODING_FORMAT_MASK = 0x0003
        SCO_VS_AIR_CODING_FORMAT_CVSD = 0x0000
        SCO_VS_AIR_CODING_FORMAT_MULAW = 0x0001
        SCO_VS_AIR_CODING_FORMAT_ALAW = 0x0002
        SCO_VS_AIR_CODING_DATA = 0x0003
        SCO_VS_SETTING_DEFAULT = 0x0060

        # SCO link types.


        class _SCO_LINK_TYPE(ENUM):
            ScoLinkType = 0x00
            eScoLinkType = 0x02


        SCO_LINK_TYPE = _SCO_LINK_TYPE
        PSCO_LINK_TYPE = POINTER(_SCO_LINK_TYPE)

        # SCO and eSCO coding formats
        class _CODING_FORMAT(ENUM):
            ScoCodingFormatULaw = 0x00
            ScoCodingFormatALaw = 0x01
            ScoCodingFormatCVSD = 0x02
            ScoCodingFormatTransparent = 0x03
            ScoCodingFormatLinearPCM = 0x04
            ScoCodingFormatMSBC = 0x05
            ScoCodingFormatVendorSpecific = 0xFF


        CODING_FORMAT = _CODING_FORMAT
        PCODING_FORMAT = POINTER(_CODING_FORMAT)


        def IS_CODING_FORMAT_RESERVED(fmt):
            return (
                _CODING_FORMAT.ScoCodingFormatMSBC <
                fmt <
                _CODING_FORMAT.ScoCodingFormatVendorSpecific
            )

        # SCO and eSCO Datapath values

        #
        SCO_DATAPATH_HCI = 0x0
        SCO_DATAPATH_PCM = 0x1

        # SCO and eSCO PCM Data Formats


        class _PCM_DATA_FORMAT(ENUM):
            ScoPCMCFormatNA = 0x00
            ScoPCMFormat1sComplement = 0x01
            ScoPCMFormat2sComplement = 0x02
            ScoPCMFormatSignMagnitude = 0x03
            ScoPCMFormatUnInt = 0x04


        PCM_DATA_FORMAT = _PCM_DATA_FORMAT
        PPCM_DATA_FORMAT = POINTER(_PCM_DATA_FORMAT)


        def IS_PCM_FORMAT_RESERVED(fmt):
            return fmt > _PCM_DATA_FORMAT.ScoPCMFormatUnInt

        # BR SCO and eSCO packet types.
        SCO_HV1 = 0x0001
        SCO_HV2 = 0x0002
        SCO_HV3 = 0x0004
        SCO_EV3 = 0x0008
        SCO_EV4 = 0x0010
        SCO_EV5 = 0x0020
        SCO_PKT_ALL = 0x003F

        # EDR eSCO packet types are not defined. They are implicitly included,

        # but can be explicitly excluded with the following definitions.
        SCO_NO2EV3 = 0x0040
        SCO_NO3EV3 = 0x0080
        SCO_NO2EV5 = 0x0100
        SCO_NO3EV5 = 0x0200

        # Frequently used packet type combinations
        PKT_ALL = SCO_HV1 | SCO_HV2 | SCO_HV3 | SCO_EV3 | SCO_EV4 | SCO_EV5
        PKT_EDR_ESCO_NONE = SCO_NO2EV3 | SCO_NO3EV3 | SCO_NO2EV5 | SCO_NO3EV5
        PKT_HV1 = SCO_HV1 | PKT_EDR_ESCO_NONE
        PKT_HV2 = SCO_HV2 | PKT_EDR_ESCO_NONE
        PKT_HV3 = SCO_HV3 | PKT_EDR_ESCO_NONE
        PKT_BR_SCO_ALL = PKT_HV1 | PKT_HV2 | PKT_HV3
        PKT_EV3 = SCO_EV3 | PKT_EDR_ESCO_NONE
        PKT_EV4 = SCO_EV4 | PKT_EDR_ESCO_NONE
        PKT_EV5 = SCO_EV5 | PKT_EDR_ESCO_NONE
        PKT_BR_ESCO_ALL = PKT_EV3 | PKT_EV4 | PKT_EV5
        PKT_2EV3 = PKT_EDR_ESCO_NONE ^ SCO_NO2EV3
        PKT_3EV3 = PKT_EDR_ESCO_NONE ^ SCO_NO3EV3
        PKT_2EV5 = PKT_EDR_ESCO_NONE ^ SCO_NO2EV5
        PKT_3EV5 = PKT_EDR_ESCO_NONE ^ SCO_NO3EV5
        PKT_EDR_ESCO_ALL = ~PKT_EDR_ESCO_NONE
        PKT_ESCO_ALL = SCO_EV3 | SCO_EV4 | SCO_EV5

        # Valid SCO channel flags in OpenChannel/OpenChannel response.
        SCO_CF_LINK_AUTHENTICATED = 0x00020000
        SCO_CF_LINK_ENCRYPTED = 0x00040000
        SCO_CF_LINK_SUPPRESS_PIN = 0x00080000

        # Notify the client when a remote disconnect occurs
        SCO_CALLBACK_DISCONNECT = 0x00000001

        # Valid SCO connection indications in OpenChannel/OpenChannel response.
        SCO_VALID_CALLBACK_FLAGS = SCO_CALLBACK_DISCONNECT

        # SCO callback notification codes.


        class _SCO_INDICATION_CODE(ENUM):
            ScoIndicationAddReference = 0
            ScoIndicationReleaseReference = 1
            ScoIndicationRemoteConnect = 2
            ScoIndicationRemoteDisconnect = 3


        SCO_INDICATION_CODE = _SCO_INDICATION_CODE
        PSCO_INDICATION_CODE = POINTER(_SCO_INDICATION_CODE)

        # Reasons why a SCO channel has been disconnected
        class _SCO_DISCONNECT_REASON(ENUM):
            ScoHciDisconnect = 0
            ScoDisconnectRequest = 1
            ScoRadioPoweredDown = 2
            ScoHardwareRemoval = 3


        SCO_DISCONNECT_REASON = _SCO_DISCONNECT_REASON
        PSCO_DISCONNECT_REASON = POINTER(_SCO_DISCONNECT_REASON)

        # SCO callback parameters.
        class _SCO_INDICATION_PARAMETERS(ctypes.Structure):
            pass


        class Parameters(ctypes.Structure):
            pass


        class Connect(ctypes.Structure):
            pass


        class Request(ctypes.Structure):
            pass


        Request._fields_ = [
            ('LinkType', SCO_LINK_TYPE), # [IN] Type of link (SCO or ESCO).
        ]
        Connect.Request = Request
        Connect._fields_ = [
            ('Request', Connect.Request),
        ]
        Parameters.Connect = Connect

        class Disconnect(ctypes.Structure):
            pass


        Disconnect._fields_ = [
            ('Reason', SCO_DISCONNECT_REASON), # [IN] Reason why the remote device disconnected.
            ('CloseNow', BOOLEAN), # [OUT] TRUE to let caller close the connection.
        ]
        Parameters.Disconnect = Disconnect
        Parameters._fields_ = [
            ('Connect', Parameters.Connect), # ScoIndicationRemoteConnect
            ('Disconnect', Parameters.Disconnect), # ScoIndicationRemoteDisconnect
        ]

        _SCO_INDICATION_PARAMETERS.Parameters = Parameters
        _SCO_INDICATION_PARAMETERS._fields_ = [
            ('ConnectionHandle', SCO_CHANNEL_HANDLE), # [IN] SCO connection handle.
            ('BtAddress', BTH_ADDR), # [IN] Bluetooth address of remote device.
            ('Parameters', _SCO_INDICATION_PARAMETERS.Parameters),
        ]
        SCO_INDICATION_PARAMETERS = _SCO_INDICATION_PARAMETERS
        PSCO_INDICATION_PARAMETERS = POINTER(_SCO_INDICATION_PARAMETERS)

        # SCO callback prototype.
        # typedef
        # void
        # (*PFNSCO_INDICATION_CALLBACK)(
        # IN PVOID Context,
        # IN SCO_INDICATION_CODE Indication,
        # IN PSCO_INDICATION_PARAMETERS Parameters
        # );
        #

        PFNSCO_INDICATION_CALLBACK = CALLBACK(
            VOID,
            PVOID,
            SCO_INDICATION_CODE,
            PSCO_INDICATION_PARAMETERS
        )

        # Valid SCO 'connectionless indications' in service interface.
        SCO_INDICATION_SCO_REQUEST = 0x00000001
        SCO_INDICATION_ESCO_REQUEST = 0x00000002
        SCO_INDICATION_VALID_FLAGS = (
            SCO_INDICATION_SCO_REQUEST |
            SCO_INDICATION_ESCO_REQUEST
        )


        class _BRB_SCO_REGISTER_SERVER(ctypes.Structure):
            pass


        _BRB_SCO_REGISTER_SERVER._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR),
            ('Reserved', ULONG), # Reserved for future use (set to 0).
            ('IndicationFlags', ULONG), # [IN] Combination of SCO_INDICATION_Xxx flags.
            ('IndicationCallback', PFNSCO_INDICATION_CALLBACK),
            ('IndicationCallbackContext', PVOID),
            ('ReferenceObject', PVOID), # routine.
            ('ServerHandle', SCO_SERVER_HANDLE), # structure.
        ]


        class _BRB_SCO_UNREGISTER_SERVER(ctypes.Structure):
            pass


        _BRB_SCO_UNREGISTER_SERVER._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR),
            ('ServerHandle', PVOID),
        ]

        # Connect response signal Result values
        SCO_CONNECT_RSP_RESPONSE_SUCCESS = 0x00
        SCO_CONNECT_RSP_RESPONSE_NO_RESOURCES = 0x0D
        SCO_CONNECT_RSP_RESPONSE_SECURITY_BLOCK = 0x0E
        SCO_CONNECT_RSP_RESPONSE_BAD_BD_ADDR = 0x0F

        # This request will open an SCO connection on a physical link.
        class _BRB_SCO_OPEN_CHANNEL(ctypes.Structure):
            pass


        _BRB_SCO_OPEN_CHANNEL._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR), # [IN] Bluetooth address of target device
            ('TransmitBandwidth', ULONG), # [IN] Transmit bandwidth in (bytes/sec).
            ('ReceiveBandwidth', ULONG), # [IN] Receive bandwidth in (bytes/sec).
            ('MaxLatency', USHORT), # [IN] Max in air delay before discarding the packet (msec).
            ('PacketType', USHORT), # [IN] HV1 | HV2 | HV3 | EV3 | EV4 | EV5 (See SCO_HV1 etc.)
            ('ContentFormat', USHORT), # [IN] Content format. (See SCO_VS_Xxx defines).
            ('Reserved', USHORT), # [IN] Set to zero.
            ('RetransmissionEffort', SCO_RETRANSMISSION_EFFORT), # [IN] Retransmission effort
            ('ChannelFlags', ULONG), # [IN] Combination of SCO_CF_XXX flags
            ('CallbackFlags', ULONG), # [IN] Combo of SCO_CALLBACK_Xxx flags
            ('Callback', PFNSCO_INDICATION_CALLBACK), # [IN] Callback supplied by client
            ('CallbackContext', PVOID), # [IN] Context passed to callback

            # [IN] Object to be passed to ObReferenceObject,
            # ObDereferenceObject
            ('ReferenceObject', PVOID),
            ('ChannelHandle', SCO_CHANNEL_HANDLE), # in during ScoIndicationRemoteConnect.
            ('Response', UCHAR), # SCO_CONNECT_RSP_RESPONSE_Xxx values is used.
        ]

        # This request will close an SCO connection on a physical link.
        class _BRB_SCO_CLOSE_CHANNEL(ctypes.Structure):
            pass


        _BRB_SCO_CLOSE_CHANNEL._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR), # [IN] Address of the remote device
            ('ChannelHandle', SCO_CHANNEL_HANDLE), # [IN] SCO Connection handle to be provided to BTHPORT.
        ]

        # This request will flush the 'in' and/or 'out' channel's pipe.
        class _BRB_SCO_FLUSH_CHANNEL(ctypes.Structure):
            pass


        _BRB_SCO_FLUSH_CHANNEL._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR), # [IN] Address of the remote device
            ('ChannelHandle', SCO_CHANNEL_HANDLE), # [IN] SCO Connection handle to be provided to BTHPORT.
            ('FlushFlags', ULONG), # [IN] Combination of SCO_FLUSH_XXX flags.
        ]

        # SCO write pipe.
        SCO_FLUSH_DIRECTION_OUT = 0x00000001

        # SCO read pipe.
        SCO_FLUSH_DIRECTION_IN = 0x00000002

        # Baseband channel settings.
        class _BASEBAND_CHANNEL_INFO(ctypes.Structure):
            pass


        _BASEBAND_CHANNEL_INFO._fields_ = [
            ('Transmission_Interval', UCHAR), # 0 for SCO links.
            ('Retransmission_Window', UCHAR), # for SCO links.
            ('AirMode', UCHAR), # 0x04 - 0xFF - Reserved.
            ('Rx_Packet_Length', USHORT), # 0 for SCO links.
            ('Tx_Packet_Length', USHORT), # 0 for SCO links.
        ]
        BASEBAND_CHANNEL_INFO = _BASEBAND_CHANNEL_INFO
        PBASEBAND_CHANNEL_INFO = POINTER(_BASEBAND_CHANNEL_INFO)

        # This request will return the channel settings.
        class _BRB_SCO_GET_CHANNEL_INFO(ctypes.Structure):
            pass


        _BRB_SCO_GET_CHANNEL_INFO._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR), # [IN] Bluetooth address of target device
            ('ChannelHandle', SCO_CHANNEL_HANDLE), # [IN] SCO Connection handle to be provided to BTHPORT.
            ('InfoFlags', ULONG), # [OUT] Generic informational flags (See SCO_INFO_Xxx defines).
            ('TransmitBandwidth', ULONG), # [OUT] Transmit bandwidth in (bytes/sec).
            ('ReceiveBandwidth', ULONG), # [OUT] Receive bandwidth in (bytes/sec).
            ('MaxLatency', USHORT), # [OUT] Max in air delay before discarding the packet (msec).
            ('PacketType', USHORT), # [OUT] HV1 | HV2 | HV3 | EV3 | EV4 | EV5 (See SCO_HV1 etc.)
            ('ContentFormat', USHORT), # [OUT] Content format. (See SCO_VS_Xxx defines).
            ('Reserved', USHORT), # [OUT] Set to zero.
            ('RetransmissionEffort', SCO_RETRANSMISSION_EFFORT), # [OUT] Retransmission effort
            ('ChannelFlags', ULONG), # [OUT] Combination of SCO_CF_XXX flags
            ('HciConnectionHandle', CONNECTION_HANDLE), # [OUT] HCI connection handle.
            ('LinkType', SCO_LINK_TYPE), # [OUT] HCI link type.
            ('BasebandInfo', BASEBAND_CHANNEL_INFO), # for more info).
        ]

        # Get channel informational flags.
        SCO_INFO_BASEBAND_AVAILABLE = 0x00000001

        # This request will sumbit a data buffer by the client to be filled
        # from the

        # open SCO channel associated with the connection handle. The client
        # driver

        # can provide either an MDL ptr or PVOID ptr but not both. BufferSize

        # parameter will be updated upon completion of this request to reflect
        # the

        # total bytes read.
        class _BRB_SCO_TRANSFER(ctypes.Structure):
            pass


        _BRB_SCO_TRANSFER._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR), # [IN] Address of the remote device
            ('ChannelHandle', SCO_CHANNEL_HANDLE), # [IN] SCO Connection handle to be provided to BTHPORT.
            ('TransferFlags', ULONG), # [IN] Combination of SCO_TRANSFER_XXX flags.
            ('BufferSize', ULONG), # [IN/OUT] Length of buffer in bytes.
            ('Buffer', PVOID), # [IN] buffer ptr. should be NULL if BufferMDL is used.
            ('BufferMDL', PMDL), # [IN] MDL buffer ptr. should be NULL if Buffer id used.
            ('DataTag', ULONGLONG), # [OUT] additional info about the data.
        ]

        # SCO write
        SCO_TRANSFER_DIRECTION_OUT = 0x00000000

        # SCO read
        SCO_TRANSFER_DIRECTION_IN = 0x00000001

        # This request will return system wide SCO information.
        class _BRB_SCO_GET_SYSTEM_INFO(ctypes.Structure):
            pass


        _BRB_SCO_GET_SYSTEM_INFO._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('Features', ULONG), # [OUT] SCO features. (See SCO_FEATURE_Xxx defines).
            ('MaxChannels', ULONG), # Set to - 1 if no limit or unknown.
            ('TransferUnit', ULONG), # Set to - 1 if variable or unknown.
            ('PacketTypes', USHORT), # [OUT] Supported (e)SCO packet types. (See SCO_HV1 etc.).
            ('DataFormats', USHORT), # [OUT] Supported data formats. (See SCO_DATA_FORMAT_Xxx defines).
            ('Reserved', ULONG), # [OUT] Reserved for future use.
        ]

        # Supported SCO features.
        SCO_FEATURE_SCO_LINKS = 0x00000001
        SCO_FEATURE_ESCO_LINKS = 0x00000002
        SCO_FEATURE_STREAM_OFFSET_DATA_TAG = 0x00000010

        # Supported data formats (voice encodings).
        SCO_DATA_FORMAT_MU_LAW_LOG = 0x0001
        SCO_DATA_FORMAT_A_LAW_LOG = 0x0002
        SCO_DATA_FORMAT_CVSD = 0x0004
        SCO_DATA_FORMAT_TRANSPARENT = 0x0008
        SCO_DATA_FORMAT_ALL = 0x000F
        SCO_DATA_FORMAT_VENDOR_SPECIFIC = 0x00FF

        # Return TRUE if the reserved values are not used, or FALSE otherwise

        def ALL_RESERVED_DATA_FORMAT_BITS_ARE_ZERO(format):
            return bool(format)

        # L2CAP specific data types

        # FLOWSPEC related constants

        # No traffic will be transmitted in the specified direction.
        L2CAP_FLOW_SERVICE_TYPE_NOTRAFFIC = 0

        # Default value, and indicates reasonable efforts
        L2CAP_FLOW_SERVICE_TYPE_BESTEFFORT = 1

        # Guarantees ability to transmit data at token rate.
        L2CAP_FLOW_SERVICE_TYPE_GUARANTEED = 2

        # connect response signal Result & Status values
        CONNECT_RSP_RESULT_SUCCESS = 0x0
        CONNECT_RSP_RESULT_PENDING = 0x1
        CONNECT_RSP_RESULT_PSM_NEG = 0x2
        CONNECT_RSP_RESULT_SECURITY_BLOCK = 0x3
        CONNECT_RSP_RESULT_NO_RESOURCES = 0x4

        # Only valid if CONNECT_RSP_RESULT_PENDING is specified
        CONNECT_RSP_STATUS_NO_INFORMATION = 0x00
        CONNECT_RSP_STATUS_AUTHENTICATION_PENDING = 0x01
        CONNECT_RSP_STATUS_AUTHORIZATION_PENDING = 0x02

        # Config signal response codes
        CONFIG_STATUS_SUCCESS = 0
        CONFIG_STATUS_INVALID_PARAMETER = 1
        CONFIG_STATUS_REJECT = 2
        CONFIG_STATUS_UNKNOWN_OPTION = 3
        CONFIG_STATUS_DISCONNECT = 0xFFF

        # Connection parameter update response codes
        CONNECTION_PARAMETERS_ACCEPTED = 0x0000
        CONNECTION_PARAMETERS_REJECTED = 0x0001

        # Min, max, and default L2cap Signal MTU.

        # Min, max, default, no retransmit and infinite FlushTO values
        L2CAP_MIN_FLUSHTO = 1
        L2CAP_MAX_FLUSHTO = 0xFFFF
        L2CAP_DEFAULT_FLUSHTO = L2CAP_MAX_FLUSHTO
        L2CAP_NO_REXMIT_FLUSHTO = L2CAP_MIN_FLUSHTO
        L2CAP_INFINITE_FLUSHTO = L2CAP_MAX_FLUSHTO

        if NTDDI_VERSION >= NTDDI_WIN8:

            # Mode for Retransmission and Flow Control Option
            L2CAP_RAF_BASIC_MODE = 0x00
            L2CAP_RAF_ENHANCED_RETRANSMISSION_MODE = 0x03
            L2CAP_RAF_STREAMING_MODE = 0x04
            L2CAP_RAF_DEFAULT_MAX_PDU_SIZE = 0x1F40
            L2CAP_RAF_DEFAULT_TX_WINDOW_SIZE = 0x3F
            L2CAP_RAF_DEFAULT_MAXTRANSMIT = 0x10
            L2CAP_RAF_VALID_CONFIG_REQUEST_RETRANSMISSION_TO = 0x00
            L2CAP_RAF_VALID_CONFIG_REQUEST_MONITOR_TO = 0x00

            # Min, max, default value for FCS

            #
            L2CAP_NO_FCS = 0x00
            L2CAP_16_BIT_FCS = 0x01
            L2CAP_DEFAULT_FCS = L2CAP_16_BIT_FCS
        # END IF   NTDDI_WIN8

        # Specify which fields contain data.

        # In the case of OUT parameters where the flag is not set for a
        # particular

        # value, the default will be requested. If the default is rejected by
        # the

        # remote host, the suggested value (by the remote host) will be used.

        # In the case of IN parameters where the flag is not set for a
        # particular

        # value, the remote's request value will be accepted.

        # Link timeout is a local option and is not negotiated across the air.

        # QOS is specified for the outbound config request
        CFG_MTU = 0x00000001
        CFG_FLUSHTO = 0x00000002
        CFG_QOS = 0x00000004
        CFG_EXTRA = 0x00000008
        CFG_LINKTO = 0x00000010
        CFG_QOS_LOCAL = 0x00000020

        if NTDDI_VERSION >= NTDDI_WIN8:
            CFG_ENHANCED = 0x00000040
            CFG_FCS = 0x00000080
            CM_BASIC = 0x00000001
            CM_RETRANSMISSION_AND_FLOW = 0x00000002
            CM_STREAMING = 0x00000004
        # END IF   NTDDI_WIN8

        # Indicates the desired role in the connection
        CF_ROLE_EITHER = 0x00000000
        CF_ROLE_SLAVE = 0x00000001
        CF_ROLE_MASTER = 0x00000002
        CF_ROLE_MASK = CF_ROLE_EITHER | CF_ROLE_SLAVE | CF_ROLE_MASTER

        # Indicates requirenments on the HCI channel. Encryption requires

        # authentication.
        CF_LINK_NOTHING = 0x00010000
        CF_LINK_AUTHENTICATED = 0x00020000
        CF_LINK_ENCRYPTED = 0x00040000
        CF_LINK_SUPPRESS_PIN = 0x00080000
        CF_QUEUE_KEEP_OLD = 0x00000020
        CF_QUEUE_KEEP_NEW = 0x00000040
        CF_QUEUE_MASK = CF_QUEUE_KEEP_OLD | CF_QUEUE_KEEP_NEW

        # Notify the client when a remote disconnect occurs
        CALLBACK_DISCONNECT = 0x00000001

        # Involve the client when the remote host sends a config request with
        # a QOS

        # value. If this flag is not set and the remote host either specifies
        # a QOS

        # parameter in a config request or rejects the local host's request
        # for QOS,

        # then the channel is disconnected.
        CALLBACK_CONFIG_QOS = 0x00000002

        # If specified, the callback will be called when remote host rejects
        # an extra

        # config option.

        # If unspecified and the remote host rejects the config request due to
        # an extra

        # config option, the connection will be closed.
        CALLBACK_CONFIG_EXTRA_OUT = 0x00000004

        # If specified, the callback will be called when the remote host's
        # config

        # request contains extra options.

        # If unspecified, the extra config options will be rejected as unknown
        # options.
        CALLBACK_CONFIG_EXTRA_IN = 0x00000008

        # If specified, the callback will be called when the remote host
        # requests a

        # reconfiguration of the channel.

        # If this flag is not specified, any reconfig is rejected and the
        # channel is torn down.
        CALLBACK_RECONFIG = 0x00000010

        # Client wants to be involved in master / slave role switching
        CALLBACK_ROLE_CHANGE = 0x00000020

        # Client wants to be notified when an incoming L2CAP packet has been
        # received
        CALLBACK_RECV_PACKET = 0x00000040


        class _INDICATION_PARAMETERS(ctypes.Structure):
            pass


        class _INDICATION_PARAMETERS_ENHANCED(ctypes.Structure):
            pass

        PINDICATION_PARAMETERS = POINTER(_INDICATION_PARAMETERS)
        PINDICATION_PARAMETERS_ENHANCED = POINTER(_INDICATION_PARAMETERS_ENHANCED)

        INDICATIONCODE = None
        if not defined(INDICATIONCODE):
            if NTDDI_VERSION >= NTDDI_WIN8:
                class _INDICATION_CODE(ENUM):
                    IndicationAddReference = 0
                    IndicationReleaseReference = 1
                    IndicationRemoteConnect = 2
                    IndicationRemoteDisconnect = 3
                    IndicationRemoteConfigRequest = 4
                    IndicationRemoteConfigResponse = 5
                    IndicationFreeExtraOptions = 6
                    IndicationRecvPacket = 7
                    IndicationPairDevice = 8
                    IndicationUnpairDevice = 9
                    IndicationUnpersonalizeDevice = 10
                    IndicationRemoteConnectLE = 11


                INDICATION_CODE = _INDICATION_CODE
                PINDICATION_CODE = POINTER(_INDICATION_CODE)
            else:
                class _INDICATION_CODE(ENUM):
                    IndicationAddReference = 0
                    IndicationReleaseReference = 1
                    IndicationRemoteConnect = 2
                    IndicationRemoteDisconnect = 3
                    IndicationRemoteConfigRequest = 4
                    IndicationRemoteConfigResponse = 5
                    IndicationFreeExtraOptions = 6
                    IndicationRecvPacket = 7
                    IndicationPairDevice = 8
                    IndicationUnpairDevice = 9
                    IndicationUnpersonalizeDevice = 10


                INDICATION_CODE = _INDICATION_CODE
                PINDICATION_CODE = POINTER(_INDICATION_CODE)
            # END IF   NTDDI_WIN8
        # END IF   INDICATIONCODE

        # typedef
        # void
        # (*PFNBTHPORT_INDICATION_CALLBACK)(
        # IN PVOID Context,
        # IN INDICATION_CODE Indication,
        # IN PINDICATION_PARAMETERS Parameters
        # );
        PFNBTHPORT_INDICATION_CALLBACK = CALLBACK(
            VOID,
            PVOID,
            INDICATION_CODE,
            PINDICATION_PARAMETERS
        )

        if NTDDI_VERSION >= NTDDI_WIN8:
            # typedef
            # void
            # (*PFNBTHPORT_INDICATION_CALLBACK_ENHANCED)(
            # IN PVOID Context,
            # IN INDICATION_CODE Indication,
            # IN PINDICATION_PARAMETERS_ENHANCED Parameters
            # );
            PFNBTHPORT_INDICATION_CALLBACK_ENHANCED = CALLBACK(
                VOID,
                PVOID,
                INDICATION_CODE,
                PINDICATION_PARAMETERS_ENHANCED
            )

        # END IF   NTDDI_WIN8

        # Full description of config option header and associated data
        class _L2CAP_CONFIG_OPTION(ctypes.Structure):
            pass


        _L2CAP_CONFIG_OPTION._fields_ = [
            ('Header', CO_HEADER), # Header
            ('UNALIGNED *DynamicBuffer', VOID), # Valid if Flags == CO_DYNAMIC
            ('FixedBuffer', UCHAR * 4), # Valid if Flags == CO_FIXED
            ('Flags', USHORT), # Combo of CO_XXX flags
        ]
        L2CAP_CONFIG_OPTION = _L2CAP_CONFIG_OPTION
        PL2CAP_CONFIG_OPTION = POINTER(_L2CAP_CONFIG_OPTION)


        class _CHANNEL_CONFIG_PARAMETERS(ctypes.Structure):
            pass


        _CHANNEL_CONFIG_PARAMETERS._fields_ = [
            ('Flags', ULONG), # Combination of CFG_XXX flags
            ('Mtu', CO_MTU), # MTU for the direction
            ('FlushTO', CO_FLUSHTO), # Flush timeout for the direction
            ('NumExtraOptions', ULONG), # Number of elements in the ExtraOptions array
            ('ExtraOptions', PL2CAP_CONFIG_OPTION), # Array of extra options
            ('Flow', L2CAP_FLOWSPEC), # QOS for the direction
        ]
        CHANNEL_CONFIG_PARAMETERS = _CHANNEL_CONFIG_PARAMETERS
        PCHANNEL_CONFIG_PARAMETERS = POINTER(_CHANNEL_CONFIG_PARAMETERS)

        if NTDDI_VERSION >= NTDDI_WIN8:
            class _CHANNEL_CONFIG_PARAMETERS_ENHANCED(ctypes.Structure):
                pass


            _CHANNEL_CONFIG_PARAMETERS_ENHANCED._fields_ = [
                ('Flags', ULONG), # Combination of CFG_XXX flags
                ('Mtu', CO_MTU), # MTU for the direction
                ('FlushTO', CO_FLUSHTO), # Flush timeout for the direction
                ('NumExtraOptions', ULONG), # Number of elements in the ExtraOptions array
                ('ExtraOptions', PL2CAP_CONFIG_OPTION), # Array of extra options
                ('Flow', L2CAP_FLOWSPEC), # QOS for the direction
                ('RetransmissionAndFlow', L2CAP_RETRANSMISSION_AND_FLOW_CONTROL), # Retransmission and flow for the direction
                ('Fcs', CO_FCS), # Frame check sequnce
                ('ExtendedFlowSpec', L2CAP_EXTENDED_FLOW_SPEC), # Reserved
                ('ExtendedWindowSize', CO_EXTENDED_WINDOW_SIZE), # Reserved
            ]
            CHANNEL_CONFIG_PARAMETERS_ENHANCED = _CHANNEL_CONFIG_PARAMETERS_ENHANCED
            PCHANNEL_CONFIG_PARAMETERS_ENHANCED = POINTER(_CHANNEL_CONFIG_PARAMETERS_ENHANCED)


            class _CHANNEL_CONFIG_RESULTS_ENHANCED(ctypes.Structure):
                pass


            _CHANNEL_CONFIG_RESULTS_ENHANCED._fields_ = [
                ('Params', CHANNEL_CONFIG_PARAMETERS_ENHANCED), # Channel parameters for the given direction of the channel
                ('ExtraOptionsBufferSize', ULONG), # for the given direction
            ]
            CHANNEL_CONFIG_RESULTS_ENHANCED = _CHANNEL_CONFIG_RESULTS_ENHANCED
            PCHANNEL_CONFIG_RESULTS_ENHANCED = POINTER(_CHANNEL_CONFIG_RESULTS_ENHANCED)
        # END IF  (NTDDI_VERSION >= NTDDI_WIN8)

        class _CHANNEL_CONFIG_RESULTS(ctypes.Structure):
            pass


        _CHANNEL_CONFIG_RESULTS._fields_ = [
            ('Params', CHANNEL_CONFIG_PARAMETERS), # Channel parameters for the given direction of the channel
            ('ExtraOptionsBufferSize', ULONG), # for the given direction
        ]
        CHANNEL_CONFIG_RESULTS = _CHANNEL_CONFIG_RESULTS
        PCHANNEL_CONFIG_RESULTS = POINTER(_CHANNEL_CONFIG_RESULTS)

        L2CAP_DISCONNECT_REASON = None

        if not defined(L2CAP_DISCONNECT_REASON):

            # Reasons why a channel has been disconnected
            class _L2CAP_DISCONNECT_REASON(ENUM):
                HciDisconnect = 0
                L2capDisconnectRequest = 1
                RadioPoweredDown = 2
                HardwareRemoval = 3


            L2CAP_DISCONNECT_REASON = _L2CAP_DISCONNECT_REASON
        # END IF


        class Parameters(ctypes.Union):
            pass


        class Connect(ctypes.Structure):
            pass


        class Request(ctypes.Structure):
            pass

        Request._fields_ = [
            ('PSM', USHORT),
        ]
        Connect.Request = Request

        Connect._fields_ = [
            ('Request', Connect.Request),
        ]
        Parameters.Connect = Connect


        class ConfigRequest(ctypes.Structure):
            pass


        ConfigRequest._fields_ = [
            ('CurrentParams', CHANNEL_CONFIG_PARAMETERS), # if the channel was previously open and is now in config.
            ('RequestedParams', CHANNEL_CONFIG_PARAMETERS), # The parameters passed from the remote host for config request
            ('ResponseParams', CHANNEL_CONFIG_PARAMETERS), # needed.
            ('Response', USHORT), # A CONFIG_STATUS_XXX value
        ]
        Parameters.ConfigRequest = ConfigRequest


        class ConfigResponse(ctypes.Structure):
            pass


        ConfigResponse._fields_ = [
            ('CurrentParams', CHANNEL_CONFIG_PARAMETERS), # if the channel was previously open and is now in config.
            ('RequestedParams', CHANNEL_CONFIG_PARAMETERS), # The parameters that were sent across the wire previously
            ('RejectedParams', CHANNEL_CONFIG_PARAMETERS), # The parameters that were rejected by the remote host
            ('UnknownTypes', PCO_TYPE),
            ('NumUnknownTypes', ULONG),
            ('NewRequestParams', CHANNEL_CONFIG_PARAMETERS),
            ('Response', USHORT), # across the wire, otherwise the connection is torn down.
        ]
        Parameters.ConfigResponse = ConfigResponse


        class FreeExtraOptions(ctypes.Structure):
            pass


        FreeExtraOptions._fields_ = [
            ('NumExtraOptions', ULONG),
            ('ExtraOptions', PL2CAP_CONFIG_OPTION), # Array of extra options
        ]
        Parameters.FreeExtraOptions = FreeExtraOptions


        class Disconnect(ctypes.Structure):
            pass


        Disconnect._fields_ = [
            ('Reason', L2CAP_DISCONNECT_REASON),
            ('CloseNow', BOOLEAN),
        ]
        Parameters.Disconnect = Disconnect


        class RecvPacket(ctypes.Structure):
            pass


        RecvPacket._fields_ = [
            ('PacketLength', ULONG),
            ('TotalQueueLength', ULONG),
        ]
        Parameters.RecvPacket = RecvPacket
        Parameters._fields_ = [
            ('Connect', Parameters.Connect), # IndicationConnect
            ('ConfigRequest', Parameters.ConfigRequest),
            ('ConfigResponse', Parameters.ConfigResponse),
            ('FreeExtraOptions', Parameters.FreeExtraOptions),
            ('Disconnect', Parameters.Disconnect),
            ('RecvPacket', Parameters.RecvPacket),
        ]
        _INDICATION_PARAMETERS.Parameters = Parameters
        _INDICATION_PARAMETERS._fields_ = [
            ('ConnectionHandle', L2CAP_CHANNEL_HANDLE),
            ('BtAddress', BTH_ADDR),
            ('Parameters', _INDICATION_PARAMETERS.Parameters),
        ]
        INDICATION_PARAMETERS = _INDICATION_PARAMETERS
        PINDICATION_PARAMETERS = POINTER(_INDICATION_PARAMETERS)

        if NTDDI_VERSION >= NTDDI_WIN8:

            class Parameters(ctypes.Union):
                pass


            class Connect(ctypes.Structure):
                pass


            class Request(ctypes.Structure):
                pass


            Request._fields_ = [
                ('PSM', USHORT),
            ]
            Connect.Request = Request
            Connect._fields_ = [
                ('Request', Connect.Request),
            ]
            Parameters.Connect = Connect


            class ConfigRequest(ctypes.Structure):
                pass


            ConfigRequest._fields_ = [
                ('CurrentParams', CHANNEL_CONFIG_PARAMETERS_ENHANCED), # if the channel was previously open and is now in config.
                ('RequestedParams', CHANNEL_CONFIG_PARAMETERS_ENHANCED), # The parameters passed from the remote host for config request
                ('ResponseParams', CHANNEL_CONFIG_PARAMETERS_ENHANCED), # needed.
                ('Response', USHORT), # A CONFIG_STATUS_XXX value
            ]
            Parameters.ConfigRequest = ConfigRequest


            class ConfigResponse(ctypes.Structure):
                pass

            ConfigResponse._fields_ = [
                ('CurrentParams', CHANNEL_CONFIG_PARAMETERS_ENHANCED), # if the channel was previously open and is now in config.
                ('RequestedParams', CHANNEL_CONFIG_PARAMETERS_ENHANCED), # The parameters that were sent across the wire previously
                ('RejectedParams', CHANNEL_CONFIG_PARAMETERS_ENHANCED), # The parameters that were rejected by the remote host
                ('UnknownTypes', PCO_TYPE),
                ('NumUnknownTypes', ULONG),
                ('NewRequestParams', CHANNEL_CONFIG_PARAMETERS_ENHANCED),
                ('Response', USHORT), # across the wire, otherwise the connection is torn down.
            ]
            Parameters.ConfigResponse = ConfigResponse


            class FreeExtraOptions(ctypes.Structure):
                pass


            FreeExtraOptions._fields_ = [
                ('NumExtraOptions', ULONG),
                ('ExtraOptions', PL2CAP_CONFIG_OPTION), # Array of extra options
            ]
            Parameters.FreeExtraOptions = FreeExtraOptions


            class Disconnect(ctypes.Structure):
                pass


            Disconnect._fields_ = [
                ('Reason', L2CAP_DISCONNECT_REASON),
                ('CloseNow', BOOLEAN),
            ]
            Parameters.Disconnect = Disconnect


            class RecvPacket(ctypes.Structure):
                pass


            RecvPacket._fields_ = [
                ('PacketLength', ULONG),
                ('TotalQueueLength', ULONG),
            ]
            Parameters.RecvPacket = RecvPacket
            Parameters._fields_ = [
                ('Connect', Parameters.Connect), # IndicationConnect
                ('ConfigRequest', Parameters.ConfigRequest),
                ('ConfigResponse', Parameters.ConfigResponse),
                ('FreeExtraOptions', Parameters.FreeExtraOptions),
                ('Disconnect', Parameters.Disconnect),
                ('RecvPacket', Parameters.RecvPacket),
                ('Reserved', PVOID), # Reserved field
            ]
            _INDICATION_PARAMETERS_ENHANCED.Parameters = Parameters
            _INDICATION_PARAMETERS_ENHANCED._fields_ = [
                ('ConnectionHandle', L2CAP_CHANNEL_HANDLE),
                ('BtAddress', BTH_ADDR),
                ('Parameters', _INDICATION_PARAMETERS_ENHANCED.Parameters),
            ]
            INDICATION_PARAMETERS_ENHANCED = _INDICATION_PARAMETERS_ENHANCED
            PINDICATION_PARAMETERS_ENHANCED = POINTER(_INDICATION_PARAMETERS_ENHANCED)

            # Reserved field
        # END IF  (NTDDI_VERSION >= NTDDI_WIN8)

        # Caller wants to know about the device being unpaired
        INDICATION_PAIR_DEVICE = 0x00000001
        INDICATION_UNPAIR_DEVICE = 0x00000002
        INDICATION_UNPERSONALIZE_DEVICE = 0x00000004

        if NTDDI_VERSION >= NTDDI_WIN8:
            INDICATION_LE_DEVICE = 0x00010000
        # END IF   NTDDI_WIN8

        class _BRB_L2CA_REGISTER_SERVER(ctypes.Structure):
            pass


        _BRB_L2CA_REGISTER_SERVER._fields_ = [
            ('Hdr', BRB_HEADER), # Common BRB header
            ('BtAddress', BTH_ADDR),
            ('PSM', USHORT),
            ('IndicationFlags', ULONG),
            ('IndicationCallback', PFNBTHPORT_INDICATION_CALLBACK),
            ('IndicationCallbackContext', PVOID),
            ('ReferenceObject', PVOID), # routine.
            ('ServerHandle', L2CAP_SERVER_HANDLE), # structure.
        ]


        class _BRB_L2CA_UNREGISTER_SERVER(ctypes.Structure):
            pass


        _BRB_L2CA_UNREGISTER_SERVER._fields_ = [
            ('Hdr', BRB_HEADER), # Common BRB header
            ('BtAddress', BTH_ADDR),
            ('ServerHandle', PVOID),
            ('Psm', USHORT),
        ]

        if NTDDI_VERSION >= NTDDI_WIN8:
            class _BRB_L2CA_OPEN_ENHANCED_CHANNEL(ctypes.Structure):
                pass


            class _Struct_1(ctypes.Structure):
                pass


            class _Struct_2(ctypes.Structure):
                pass


            _Struct_2._fields_ = [
                ('Response', USHORT), # negative response from the remote host.
                ('ResponseStatus', USHORT), # is used.
            ]

            _Struct_1._Struct_2 = _Struct_2
            _Struct_1._anonymous_ = (
                '_Struct_2',
            )
            _Struct_1._fields_ = [
                ('_Struct_2', _Struct_1._Struct_2),
                ('Psm', USHORT), # is intended for.
            ]
            _BRB_L2CA_OPEN_ENHANCED_CHANNEL._Struct_1 = _Struct_1


            class ConfigOut(ctypes.Structure):
                pass


            class LocalQos(ctypes.Structure):
                pass


            LocalQos._fields_ = [
                ('ServiceType', UCHAR), # Must be L2CAP_FLOW_SERVICE_TYPE_GUARANTEED
                ('Latency', ULONG), # Latency in microseconds
            ]
            ConfigOut.LocalQos = LocalQos


            class ModeConfig(ctypes.Structure):
                pass


            ModeConfig._fields_ = [
                ('Flags', ULONG), # Combination of CM_XXX flags
                ('RetransmissionAndFlow', L2CAP_RETRANSMISSION_AND_FLOW_CONTROL),
            ]
            ConfigOut.ModeConfig = ModeConfig
            ConfigOut._fields_ = [
                ('Flags', ULONG), # Combination of CFG_XXX flags
                ('Mtu', L2CAP_CONFIG_VALUE_RANGE), # Range for MTU
                ('FlushTO', L2CAP_CONFIG_VALUE_RANGE), # Range for Flush timeout
                ('Flow', L2CAP_FLOWSPEC), # QOS data structure
                ('LinkTO', USHORT), # LM Link timeout
                ('NumExtraOptions', ULONG), # How many elements are in the ExtraOptions array
                ('ExtraOptions', PL2CAP_CONFIG_OPTION), # Array of extra options
                ('LocalQos', ConfigOut.LocalQos),
                ('ModeConfig', ConfigOut.ModeConfig), # Type of l2cap channel to open and corresponding parameters

                # Specifies Frame check sequence support. Valid for ERTM and
                # Streaming mode.
                ('Fcs', USHORT),
                ('ExtendedFlowSpec', L2CAP_EXTENDED_FLOW_SPEC), # Extended flow specification for the l2cap channel.
                ('ExtendedWindowSize', USHORT), # Extended Window size.
            ]
            _BRB_L2CA_OPEN_ENHANCED_CHANNEL.ConfigOut = ConfigOut


            class ConfigIn(ctypes.Structure):
                pass


            ConfigIn._fields_ = [
                ('Flags', ULONG), # Combination of CFG_XXX flags
                ('Mtu', L2CAP_CONFIG_VALUE_RANGE), # Range for MTU
                ('FlushTO', L2CAP_CONFIG_RANGE), # Range for Flush timeout
            ]
            _BRB_L2CA_OPEN_ENHANCED_CHANNEL.ConfigIn = ConfigIn
            _BRB_L2CA_OPEN_ENHANCED_CHANNEL._anonymous_ = (
                '_Struct_1',
            )
            _BRB_L2CA_OPEN_ENHANCED_CHANNEL._fields_ = [
                ('Hdr', BRB_HEADER), # Common BRB header
                ('ChannelHandle', L2CAP_CHANNEL_HANDLE), # during IndicationRemoteConnect.
                ('_Struct_1', _BRB_L2CA_OPEN_ENHANCED_CHANNEL._Struct_1),
                ('ChannelFlags', ULONG), # [IN] Combination of CF_XXX flags
                ('BtAddress', BTH_ADDR), # [IN] Address of the device the connection is intended for
                ('ConfigOut', _BRB_L2CA_OPEN_ENHANCED_CHANNEL.ConfigOut), # Parameters specifying outbound request to remote host
                ('ConfigIn', _BRB_L2CA_OPEN_ENHANCED_CHANNEL.ConfigIn), # Parameters specifying how to validate inbound requests
                ('CallbackFlags', ULONG), # Combo of CALLBACK_Xxx flags
                ('Callback', PFNBTHPORT_INDICATION_CALLBACK_ENHANCED), # Callback supplied by client
                ('CallbackContext', PVOID), # Context passed to callback
                ('ReferenceObject', PVOID), # If a callback is requested, this parameter is not optional.
                ('OutResults', CHANNEL_CONFIG_RESULTS_ENHANCED), # [OUT] Configuration parameters for the outbound direction.
                ('InResults', CHANNEL_CONFIG_RESULTS_ENHANCED), # [OUT] Configuration parametesr ofr the inbound direction
                ('IncomingQueueDepth', UCHAR),
                ('Reserved', PVOID), # Reserved field
            ]

        # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

        class _BRB_L2CA_OPEN_CHANNEL(ctypes.Structure):
            pass


        class _Struct_3(ctypes.Structure):
            pass


        class _Struct_4(ctypes.Structure):
            pass


        _Struct_4._fields_ = [
            ('Response', USHORT), # negative response from the remote host.
            ('ResponseStatus', USHORT), # is used.
        ]
        _Struct_3._Struct_4 = _Struct_4
        _Struct_3._anonymous_ = (
            '_Struct_4',
        )
        _Struct_3._fields_ = [
            ('_Struct_4', _Struct_3._Struct_4),
            ('Psm', USHORT), # is intended for.
        ]
        _BRB_L2CA_OPEN_CHANNEL._Struct_3 = _Struct_3


        class ConfigOut(ctypes.Structure):
            pass


        class LocalQos(ctypes.Structure):
            pass


        LocalQos._fields_ = [
            ('ServiceType', UCHAR), # Must be L2CAP_FLOW_SERVICE_TYPE_GUARANTEED
            ('Latency', ULONG), # Latency in microseconds
        ]
        ConfigOut.LocalQos = LocalQos
        ConfigOut._fields_ = [
            ('Flags', ULONG), # Combination of CFG_XXX flags
            ('Mtu', L2CAP_CONFIG_VALUE_RANGE), # Range for MTU
            ('FlushTO', L2CAP_CONFIG_VALUE_RANGE), # Range for Flush timeout
            ('Flow', L2CAP_FLOWSPEC), # QOS data structure
            ('LinkTO', USHORT), # LM Link timeout
            ('NumExtraOptions', ULONG), # How many elements are in the ExtraOptions array
            ('ExtraOptions', PL2CAP_CONFIG_OPTION), # Array of extra options
            ('LocalQos', ConfigOut.LocalQos),
        ]
        _BRB_L2CA_OPEN_CHANNEL.ConfigOut = ConfigOut


        class ConfigIn(ctypes.Structure):
            pass


        ConfigIn._fields_ = [
            ('Flags', ULONG), # Combination of CFG_XXX flags
            ('Mtu', L2CAP_CONFIG_VALUE_RANGE), # Range for MTU
            ('FlushTO', L2CAP_CONFIG_RANGE), # Range for Flush timeout
        ]
        _BRB_L2CA_OPEN_CHANNEL.ConfigIn = ConfigIn
        _BRB_L2CA_OPEN_CHANNEL._anonymous_ = (
            '_Struct_3',
        )
        _BRB_L2CA_OPEN_CHANNEL._fields_ = [
            ('Hdr', BRB_HEADER), # Common BRB header
            ('ChannelHandle', L2CAP_CHANNEL_HANDLE), # during IndicationRemoteConnect.
            ('_Struct_3', _BRB_L2CA_OPEN_CHANNEL._Struct_3),
            ('ChannelFlags', ULONG), # [IN] Combination of CF_XXX flags
            ('BtAddress', BTH_ADDR), # [IN] Address of the device the connection is intended for
            ('ConfigOut', _BRB_L2CA_OPEN_CHANNEL.ConfigOut), # Parameters specifying outbound request to remote host
            ('ConfigIn', _BRB_L2CA_OPEN_CHANNEL.ConfigIn), # Parameters specifying how to validate inbound requests
            ('CallbackFlags', ULONG), # Combo of CALLBACK_Xxx flags
            ('Callback', PFNBTHPORT_INDICATION_CALLBACK), # Callback supplied by client
            ('CallbackContext', PVOID), # Context passed to callback
            ('ReferenceObject', PVOID), # If a callback is requested, this parameter is not optional.
            ('OutResults', CHANNEL_CONFIG_RESULTS), # [OUT] Configuration parameters for the outbound direction.
            ('InResults', CHANNEL_CONFIG_RESULTS), # [OUT] Configuration parametesr ofr the inbound direction
            ('IncomingQueueDepth', UCHAR),
        ]


        class _BRB_L2CA_CLOSE_CHANNEL(ctypes.Structure):
            pass


        _BRB_L2CA_CLOSE_CHANNEL._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR), # [IN] Address of the remote device
            ('ChannelHandle', L2CAP_CHANNEL_HANDLE), # [IN] L2cap connection handle provided by port
        ]

        # This request will sumbit a data buffer by the client to be
        # filled/transmitted

        # from/to the open channel associated with the ChannelHandle.

        # The client driver can provide either an MDL ptr or PVOID pointer. The

        # BufferSize parameter will be updated upon completion of this request
        # to

        # reflect the total bytes read if BTHPORT_SHORT_TRANSFER_OK flag was
        # set.

        # Otherwise the port driver will return an error.

        # ACL write
        ACL_TRANSFER_DIRECTION_OUT = 0x00000000

        # ACl read
        ACL_TRANSFER_DIRECTION_IN = 0x00000001

        # Set for L2cap read BRB if the received buffer from remote device is
        # less

        # than the submitted buffer size.
        ACL_SHORT_TRANSFER_OK = 0x00000002

        # Set if the client desires to have the read timeout after a period of
        # time.
        ACL_TRANSFER_TIMEOUT = 0x00000004


        class _BRB_L2CA_ACL_TRANSFER(ctypes.Structure):
            pass


        _BRB_L2CA_ACL_TRANSFER._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR), # [IN] Address of the remote device
            ('ChannelHandle', L2CAP_CHANNEL_HANDLE), # [IN] L2cap connection handle provided by port

            # [IN] Combination of ACL_TRANSFER_XXX and ACL_SHORT_TRANSFER_OK
            # flags.
            ('TransferFlags', ULONG),
            ('BufferSize', ULONG), # [IN/OUT] Length of buffer in bytes.
            ('Buffer', PVOID), # [IN] buffer ptr. should be NULL if BufferMDL is used.
            ('BufferMDL', PMDL), # [IN] MDL buffer ptr. should be NULL if Buffer id used.
            ('Timeout', LONGLONG), # consumed so far
            ('RemainingBufferSize', ULONG), # [OUT] how much buffer remains if there is buffer underrun
        ]

        # HCI GENERAL Requests

        # This request will return the address of the local radio
        class _BRB_GET_LOCAL_BD_ADDR(ctypes.Structure):
            pass


        _BRB_GET_LOCAL_BD_ADDR._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR), # Address of local radio.
        ]


        class _BRB_GET_DEVICE_INTERFACE_STRING(ctypes.Structure):
            pass


        _BRB_GET_DEVICE_INTERFACE_STRING._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('DeviceInterfaceString', PWCHAR), # Pointer to the buffer that will contain the string
            ('DeviceInterfaceStringCbLength', ULONG), # upon success, the number of bytes copied.
        ]


        class _BRB_L2CA_PING(ctypes.Structure):
            pass


        _BRB_L2CA_PING._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR), # [IN] Device that the ping is sent to
            ('PingRequestLength', UCHAR), # [IN] lenth and data to send in the PING signal
            ('PingRequestData', UCHAR * MAX_L2CAP_PING_DATA_LENGTH),
            ('PingResponseLength', UCHAR), # [OUT] length and data that the remote device responded with
            ('PingResponseData', UCHAR * MAX_L2CAP_PING_DATA_LENGTH),
        ]


        class _BRB_L2CA_UPDATE_CHANNEL(ctypes.Structure):
            pass


        _BRB_L2CA_UPDATE_CHANNEL._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('BtAddress', BTH_ADDR), # [IN] Address of the remote device
            ('ChannelHandle', L2CAP_CHANNEL_HANDLE), # [IN] L2cap connection handle provided by port
            ('NewChannelFlags', ULONG), # The new flags that are required for the channel
            ('FailedChannelFlags', ULONG), # not able to honor.
        ]

        # + + Description: Send this BRB to register or unregister dynamic PSM
        # values. Clients can indicate their preference for a PSM value by
        # specifying the PSM value in _BRB_PSM.Psm. If the client has no
        # preference, set _BRB_PSM.Psm to 0, and then bthport will assign next
        # avaliable PSM. On successful completion of the BRB, _BRB_PSM.Psm
        # will contain the asINT PSM value. Return value: STATUS_SUCCESS
        # STATUS_INVALID_BUFFER_SIZE BrbSize is invalid
        # STATUS_INVALID_PARAMETER PSM not in dynamic range
        # STATUS_INSUFFICIENT_RESOURCES alloc failed STATUS_INVALID_CID Client
        # owns this PSM STATUS_ALREADY_COMMITTED PSM not avaliable
        # STATUS_CONNECTION_IN_USE PSM in use, cannot unregister - -
        class _BRB_PSM(ctypes.Structure):
            pass


        _BRB_PSM._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header
            ('Psm', USHORT), # The PSM that the client wants to register for
        ]

        # List of possible states of the ACL.


        class _ACL_MODE(ENUM):
            ACL_MODE_ACTIVE = 0x0
            ACL_MODE_HOLD = 0x1
            ACL_MODE_SNIFF = 0x2
            ACL_MODE_PARK = 0x3
            ACL_MODE_ENTER_ACTIVE = 0x4
            ACL_MODE_ENTER_HOLD = 0x5
            ACL_MODE_ENTER_SNIFF = 0x6
            ACL_MODE_ENTER_PARK = 0x7
            ACL_DISCONNECTED = 0x8


        ACL_MODE = _ACL_MODE

        # BRB to get the ACL mode for the specified remote device.
        class _BRB_ACL_GET_MODE(ctypes.Structure):
            pass


        _BRB_ACL_GET_MODE._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header.
            ('BtAddress', BTH_ADDR), # [IN] Address of the remote device.
            ('AclMode', ACL_MODE), # [OUT] The ACL mode.
        ]

        # BRB to put the specified ACL into active mode.

        # This BRB will fail if:

        # (1) the connection is disconnected or is about to be disconnected.

        # (2) the connection is in 'hold' mode.
        class _BRB_ACL_ENTER_ACTIVE_MODE(ctypes.Structure):
            pass


        _BRB_ACL_ENTER_ACTIVE_MODE._fields_ = [
            ('Hdr', BRB_HEADER), # BRB header.
            ('BtAddress', BTH_ADDR), # [IN] Address of the remote device.
        ]

        BRBTYPE = None
        if not defined(BRBTYPE):

            # Bluetooth Request Block
            class _BRB(ctypes.Structure):
                pass


            class _Union_1(ctypes.Union):
                pass


            _TEMP__Union_1 = [
                ('BrbHeader', _BRB_HEADER),
                ('BrbGetDeviceInterfaceString', _BRB_GET_DEVICE_INTERFACE_STRING),
                ('BrbL2caRegisterServer', _BRB_L2CA_REGISTER_SERVER),
                ('BrbL2caUnregisterServer', _BRB_L2CA_UNREGISTER_SERVER),
                ('BrbL2caOpenChannel', _BRB_L2CA_OPEN_CHANNEL),
                ('BrbL2caCloseChannel', _BRB_L2CA_CLOSE_CHANNEL),
                ('BrbL2caPing', _BRB_L2CA_PING),
                ('BrbL2caAclTransfer', _BRB_L2CA_ACL_TRANSFER),
                ('BrbGetLocalBdAddress', _BRB_GET_LOCAL_BD_ADDR),
                ('BrbPsm', _BRB_PSM),
                ('BrbL2caUpdateChannel', _BRB_L2CA_UPDATE_CHANNEL),
                ('BrbScoRegisterServer', _BRB_SCO_REGISTER_SERVER),
                ('BrbScoUnregisterServer', _BRB_SCO_UNREGISTER_SERVER),
                ('BrbScoOpenChannel', _BRB_SCO_OPEN_CHANNEL),
                ('BrbScoCloseChannel', _BRB_SCO_CLOSE_CHANNEL),
                ('BrbScoFlushChannel', _BRB_SCO_FLUSH_CHANNEL),
                ('BrbScoTransfer', _BRB_SCO_TRANSFER),
                ('BrbScoGetChannelInfo', _BRB_SCO_GET_CHANNEL_INFO),
                ('BrbScoGetSystemInfo', _BRB_SCO_GET_SYSTEM_INFO),
                ('BrbAclGetMode', _BRB_ACL_GET_MODE),
                ('BrbAclEnterActiveMode', _BRB_ACL_ENTER_ACTIVE_MODE),
            ]

            if NTDDI_VERSION >= NTDDI_WIN8:
                _TEMP__Union_1 += [
                    ('BrbL2caOpenEnhancedChannel', _BRB_L2CA_OPEN_ENHANCED_CHANNEL),
                ]
            _Union_1._fields_ = _TEMP__Union_1
            _BRB._Union_1 = _Union_1
            _BRB._anonymous_ = (
                '_Union_1',
            )
            _BRB._fields_ = [
                ('_Union_1', _BRB._Union_1),
            ]
            BRB = _BRB
            PBRB = POINTER(_BRB)

            # END IF  (NTDDI_VERSION >= NTDDI_WIN8)

            # BthAllocateBrb
            #
            # Purpose:
            # Allocates a Brb of a given type
            #
            # Returns:
            # Brb pointer or NULL if the system is out of memory
            #
            # Note this function is not exported on 1.x bluetooth versions
            #
            # _IRQL_requires_same_
            # _Must_inspect_result_
            # _When_(return!=0, __drv_allocatesMem(Mem))
            # typedef
            # PBRB
            # (*PFNBTH_ALLOCATE_BRB)(
            # _In_ BRB_TYPE brbType,
            # _In_ ULONG tag);
            PFNBTH_ALLOCATE_BRB = CALLBACK(PBRB, BRB_TYPE, ULONG)
            #
            #
            # BthFreeBrb
            #
            # Purpose:
            # Free a Brb
            #
            # Returns:
            # Nothing
            #
            # Note this function is not exported on 1.x bluetooth versions
            #
            # _IRQL_requires_same_
            # typedef
            # VOID
            # (*PFNBTH_FREE_BRB)(
            # _In_ __drv_freesMem(Mem) PBRB pBrb);
            PFNBTH_FREE_BRB = CALLBACK(VOID, PBRB)
            #
            # BthInitializeBrb
            #
            # Purpose:
            # This is used to Initialize stack allocated Brbs.
            #
            # Returns:
            # Nothing
            #
            # Note this function is not exported on 1.x bluetooth versions
            #
            # _IRQL_requires_same_
            # typedef
            # VOID
            # (*PFNBTH_INITIALIZE_BRB)(
            # _Inout_ PBRB pBrb,
            # _In_ BRB_TYPE brbType);
            PFNBTH_INITIALIZE_BRB = CALLBACK(VOID, PBRB, BRB_TYPE)
            #
            # BthReuseBrb
            #
            # Purpose:
            # This function is use to reinitialize brb for
            # reuse.
            #
            # Returns:
            # Nothing
            #
            # Note this function is not exported on 1.x bluetooth versions
            #
            # _IRQL_requires_same_
            # typedef
            # VOID
            # (*PFNBTH_REUSE_BRB)(
            # _Inout_ PBRB pBrb,
            # _In_ BRB_TYPE brbType);
            PFNBTH_REUSE_BRB = CALLBACK(VOID, PBRB, BRB_TYPE)
            #
            # IsBluetoothVersionAvailable
            #
            # Purpose:
            # Indicate if the installed Bluetooth binary set supports
            # the requested version
            #
            # Returns:
            # TRUE if the installed bluetooth binaries support the given
            # Major & Minor versions
            #
            # Note this function is not exported on 1.x bluetooth versions
            #
            # _IRQL_requires_same_
            # _Must_inspect_result_
            # typedef
            # BOOLEAN
            # (* PFNBTH_IS_BLUETOOTH_VERSION_AVAILABLE)(_In_ UCHAR MajorVersion, _In_ UCHAR MinorVersion);
            PFNBTH_IS_BLUETOOTH_VERSION_AVAILABLE = CALLBACK(BOOLEAN, UCHAR, UCHAR)
            #
            # Bluetooth QI Profile driver interface
            #
            #
            # Profile drivers should register with this QI in order to get function pointers
            # for allocating and freeing Brb.  All Brb should be allocated or Initialized using
            # these utilities.
            #
            # MajorFunction = IRP_MJ_PNP;
            # MinorFunction = IRP_MN_QUERY_INTERFACE;
            #
            # {94A59AA8-4383-4286-AA4F-34A160F40004}
            # DEFINE_GUID(GUID_BTHDDI_PROFILE_DRIVER_INTERFACE,
            # 0x94a59aa8, 0x4383, 0x4286, 0xaa, 0x4f, 0x34, 0xa1, 0x60,
            # 0xf4, 0x0, 0x4);
            #
            #
            # The QUERY_INTERFACE Irp will provide the profile driver a set of function
            # pointers for Brb allocation/frees and to verify if a Bluetooth version is available.
            #
            # Note this function is not exported on 1.x bluetooth versions

            import comtypes


            class _BTH_PROFILE_DRIVER_INTERFACE(ctypes.Structure):
                pass


            _BTH_PROFILE_DRIVER_INTERFACE._fields_ = [
                ('Interface', comtypes.IUnknown),
                ('BthAllocateBrb', PFNBTH_ALLOCATE_BRB), # Use this function to allocate Brb
                ('BthFreeBrb', PFNBTH_FREE_BRB), # Use this function to free Brb allocated with BthAllocateBrb
                ('BthInitializeBrb', PFNBTH_INITIALIZE_BRB), # Use this function to initialize stack allocated Brbs
                ('BthReuseBrb', PFNBTH_REUSE_BRB), # Use this function to reinitialize Brb for reuse

                # Indicates if the installed Bluetooth binary set supports the
                # requested version
                ('IsBluetoothVersionAvailable', PFNBTH_IS_BLUETOOTH_VERSION_AVAILABLE),
            ]
            BTH_PROFILE_DRIVER_INTERFACE = _BTH_PROFILE_DRIVER_INTERFACE
            PBTH_PROFILE_DRIVER_INTERFACE = POINTER(_BTH_PROFILE_DRIVER_INTERFACE)
        # END IF   BRBTYPE
    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
    if _MSC_VER >= 1200:
        pass
    else:
        pass
    # END IF
# END IF   __BTHDDI_H__
