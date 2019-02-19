import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__BTHIOCTL_H__ = None
CTL_CODE = None
HANDLE_SDP_TYPE = None


class _BTH_DEVICE_INFO_LIST(ctypes.Structure):
    pass


BTH_DEVICE_INFO_LIST = _BTH_DEVICE_INFO_LIST
PBTH_DEVICE_INFO_LIST = POINTER(_BTH_DEVICE_INFO_LIST)


class _BTH_RADIO_INFO(ctypes.Structure):
    pass


BTH_RADIO_INFO = _BTH_RADIO_INFO
PBTH_RADIO_INFO = POINTER(_BTH_RADIO_INFO)


class _BTH_LOCAL_RADIO_INFO(ctypes.Structure):
    pass


BTH_LOCAL_RADIO_INFO = _BTH_LOCAL_RADIO_INFO
PBTH_LOCAL_RADIO_INFO = POINTER(_BTH_LOCAL_RADIO_INFO)


class _BTH_SDP_CONNECT(ctypes.Structure):
    pass


BTH_SDP_CONNECT = _BTH_SDP_CONNECT
PBTH_SDP_CONNECT = POINTER(_BTH_SDP_CONNECT)


class _BTH_SDP_DISCONNECT(ctypes.Structure):
    pass


BTH_SDP_DISCONNECT = _BTH_SDP_DISCONNECT
PBTH_SDP_DISCONNECT = POINTER(_BTH_SDP_DISCONNECT)


class _BTH_SDP_RECORD(ctypes.Structure):
    pass


BTH_SDP_RECORD = _BTH_SDP_RECORD
PBTH_SDP_RECORD = POINTER(_BTH_SDP_RECORD)


class _BTH_SDP_SERVICE_SEARCH_REQUEST(ctypes.Structure):
    pass


BTH_SDP_SERVICE_SEARCH_REQUEST = _BTH_SDP_SERVICE_SEARCH_REQUEST
PBTH_SDP_SERVICE_SEARCH_REQUEST = POINTER(_BTH_SDP_SERVICE_SEARCH_REQUEST)


class _BTH_SDP_ATTRIBUTE_SEARCH_REQUEST(ctypes.Structure):
    pass


BTH_SDP_ATTRIBUTE_SEARCH_REQUEST = _BTH_SDP_ATTRIBUTE_SEARCH_REQUEST
PBTH_SDP_ATTRIBUTE_SEARCH_REQUEST = POINTER(_BTH_SDP_ATTRIBUTE_SEARCH_REQUEST)


class _BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST(ctypes.Structure):
    pass


BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST = _BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST
PBTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST = POINTER(_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST)


class _BTH_SDP_STREAM_RESPONSE(ctypes.Structure):
    pass


BTH_SDP_STREAM_RESPONSE = _BTH_SDP_STREAM_RESPONSE
PBTH_SDP_STREAM_RESPONSE = POINTER(_BTH_SDP_STREAM_RESPONSE)


class _BTH_COMMAND_HEADER(ctypes.Structure):
    pass


BTH_COMMAND_HEADER = _BTH_COMMAND_HEADER
PBTH_COMMAND_HEADER = POINTER(_BTH_COMMAND_HEADER)


class _BTH_VENDOR_SPECIFIC_COMMAND(ctypes.Structure):
    pass


BTH_VENDOR_SPECIFIC_COMMAND = _BTH_VENDOR_SPECIFIC_COMMAND
PBTH_VENDOR_SPECIFIC_COMMAND = POINTER(_BTH_VENDOR_SPECIFIC_COMMAND)


class _BTH_VENDOR_PATTERN(ctypes.Structure):
    pass


BTH_VENDOR_PATTERN = _BTH_VENDOR_PATTERN
PBTH_VENDOR_PATTERN = POINTER(_BTH_VENDOR_PATTERN)


class _BTH_VENDOR_EVENT_INFO(ctypes.Structure):
    pass


BTH_VENDOR_EVENT_INFO = _BTH_VENDOR_EVENT_INFO
PBTH_VENDOR_EVENT_INFO = POINTER(_BTH_VENDOR_EVENT_INFO)


class _BTH_HOST_FEATURE_MASK(ctypes.Structure):
    pass


BTH_HOST_FEATURE_MASK = _BTH_HOST_FEATURE_MASK
PBTH_HOST_FEATURE_MASK = POINTER(_BTH_HOST_FEATURE_MASK)


# **************************************************************************
# Copyright (c) 2000 Microsoft Corporation Module Name: bthioctl.h Abstract:
# defines the IOCTL codes for the kernel/user calls Environment: Kernel & user
# mode Revision History: 4-4-00 : created by Husni Roukbi 2-4-05 : split into
# public and private header files by SandySp
# *************************************************************************
if not defined(__BTHIOCTL_H__):
    __BTHIOCTL_H__ = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.shared.winioctl_h import *  # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if _MSC_VER  >= 1200:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_VISTA:
            if not defined(CTL_CODE):
                pass
            # END IF
            # IOCTL defines.
            BTH_IOCTL_BASE = 0


            def BTH_CTL(id):
                return (
                    CTL_CODE(
                        FILE_DEVICE_BLUETOOTH,
                        id,
                        METHOD_BUFFERED,
                        FILE_ANY_ACCESS
                    )
                )


            def BTH_KERNEL_CTL(id):
                return (
                    CTL_CODE(
                        FILE_DEVICE_BLUETOOTH,
                        id,
                        METHOD_NEITHER,
                        FILE_ANY_ACCESS
                    )
                )


            # kernel-level (internal) IOCTLs
            IOCTL_INTERNAL_BTH_SUBMIT_BRB = (
                BTH_KERNEL_CTL(BTH_IOCTL_BASE + 0x00)
            )

            # Input: none
            # Output: BTH_ENUMERATOR_INFO
            IOCTL_INTERNAL_BTHENUM_GET_ENUMINFO = (
                BTH_KERNEL_CTL(BTH_IOCTL_BASE + 0x01)
            )

            # Input: none
            # Output: BTH_DEVICE_INFO
            IOCTL_INTERNAL_BTHENUM_GET_DEVINFO = (
                BTH_KERNEL_CTL(BTH_IOCTL_BASE + 0x02)
            )

            # IOCTLs
            # Input: none
            # Output: BTH_LOCAL_RADIO_INFO
            IOCTL_BTH_GET_LOCAL_INFO = BTH_CTL(BTH_IOCTL_BASE + 0x00)

            # Input: BTH_ADDR
            # Output: BTH_RADIO_INFO
            IOCTL_BTH_GET_RADIO_INFO = BTH_CTL(BTH_IOCTL_BASE + 0x01)

            # use this ioctl to get a list of cached discovered devices in the
            # port driver.
            # Input: None
            # Output: BTH_DEVICE_INFO_LIST
            IOCTL_BTH_GET_DEVICE_INFO = BTH_CTL(BTH_IOCTL_BASE + 0x02)

            # Input: BTH_ADDR
            # Output: none
            IOCTL_BTH_DISCONNECT_DEVICE = BTH_CTL(BTH_IOCTL_BASE + 0x03)
            if (NTDDI_VERSION  >  NTDDI_VISTASP1 or (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))):
                # Input: BTH_VENDOR_SPECIFIC_COMMAND
                # Output: PVOID
                IOCTL_BTH_HCI_VENDOR_COMMAND = BTH_CTL(BTH_IOCTL_BASE + 0x14)
            # END IF    >= SP1 + KB942567

            # Input: BTH_SDP_CONNECT
            # Output: BTH_SDP_CONNECT
            IOCTL_BTH_SDP_CONNECT = BTH_CTL(BTH_IOCTL_BASE + 0x80)

            # Input: HANDLE_SDP
            # Output: none
            IOCTL_BTH_SDP_DISCONNECT = BTH_CTL(BTH_IOCTL_BASE + 0x81)

            # Input: BTH_SDP_SERVICE_SEARCH_REQUEST
            # Output: ULONG * number of handles wanted
            IOCTL_BTH_SDP_SERVICE_SEARCH = BTH_CTL(BTH_IOCTL_BASE + 0x82)

            # Input: BTH_SDP_ATTRIBUTE_SEARCH_REQUEST
            # Output: BTH_SDP_STREAM_RESPONSE or bigger
            IOCTL_BTH_SDP_ATTRIBUTE_SEARCH = BTH_CTL(BTH_IOCTL_BASE + 0x83)

            # Input: BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST
            # Output: BTH_SDP_STREAM_RESPONSE or bigger
            IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH = (
                BTH_CTL(BTH_IOCTL_BASE + 0x84)
            )

            # Input: raw SDP stream (at least 2 bytes)
            # Ouptut: HANDLE_SDP
            IOCTL_BTH_SDP_SUBMIT_RECORD = BTH_CTL(BTH_IOCTL_BASE + 0x85)

            # Input: HANDLE_SDP
            # Output: none
            IOCTL_BTH_SDP_REMOVE_RECORD = BTH_CTL(BTH_IOCTL_BASE + 0x86)

            # Input: BTH_SDP_RECORD + raw SDP record
            # Output: HANDLE_SDP
            IOCTL_BTH_SDP_SUBMIT_RECORD_WITH_INFO = (
                BTH_CTL(BTH_IOCTL_BASE + 0x87)
            )
            if NTDDI_VERSION  >= NTDDI_WIN8:
                # Input: NONE
                # Output: BTH_HOST_FEATURE_MASK
                IOCTL_BTH_GET_HOST_SUPPORTED_FEATURES = (
                    BTH_CTL(BTH_IOCTL_BASE + 0x88)
                )
            # END IF    >= NTDDI_WIN8

            from pyWinAPI.shared.pshpack1_h import * # NOQA

            _BTH_DEVICE_INFO_LIST._fields_ = [
                # [IN/OUT] minimum of 1 device required
                ('numOfDevices', ULONG),
                # Open ended array of devices;
                ('deviceList', BTH_DEVICE_INFO * 1),
            ]

            _BTH_RADIO_INFO._fields_ = [
                # the desired bits.
                ('lmpSupportedFeatures', ULONGLONG),
                # Manufacturer ID (possibly BTH_MFG_XXX)
                ('mfg', USHORT),
                # LMP subversion
                ('lmpSubversion', USHORT),
                # LMP version
                ('lmpVersion', UCHAR),
            ]

            _BTH_LOCAL_RADIO_INFO._fields_ = [
                # Local BTH_ADDR, class of defice, and radio name
                ('localInfo', BTH_DEVICE_INFO),
                # Combo of LOCAL_RADIO_XXX values
                ('flags', ULONG),
                # HCI revision, see core spec
                ('hciRevision', USHORT),
                # HCI version, see core spec
                ('hciVersion', UCHAR),
                # More information about the local radio (LMP, MFG)
                ('radioInfo', BTH_RADIO_INFO),
            ]

            SDP_CONNECT_CACHE = 0x00000001
            SDP_CONNECT_ALLOW_PIN = 0x00000002
            SDP_REQUEST_TO_DEFAULT = 0
            SDP_REQUEST_TO_MIN = 10
            SDP_REQUEST_TO_MAX = 45
            SERVICE_OPTION_DO_NOT_PUBLISH = 0x00000002
            SERVICE_OPTION_NO_PUBLIC_BROWSE = 0x00000004
            SERVICE_OPTION_DO_NOT_PUBLISH_EIR = 0x00000008
            SERVICE_SECURITY_USE_DEFAULTS = 0x00000000
            SERVICE_SECURITY_NONE = 0x00000001
            SERVICE_SECURITY_AUTHORIZE = 0x00000002
            SERVICE_SECURITY_AUTHENTICATE = 0x00000004
            SERVICE_SECURITY_ENCRYPT_REQUIRED = 0x00000010
            SERVICE_SECURITY_ENCRYPT_OPTIONAL = 0x00000020
            SERVICE_SECURITY_DISABLED = 0x10000000
            SERVICE_SECURITY_NO_ASK = 0x20000000

            # Do not attempt to validate that the stream can be parsed
            SDP_SEARCH_NO_PARSE_CHECK = 0x00000001

            # Do not check the format of the results. This includes
            # suppression of both
            # the check for a record patten (SEQ of UINT16 + value) and the
            # validation
            # of each universal attribute's accordance to the spec.
            SDP_SEARCH_NO_FORMAT_CHECK = 0x00000002
            if not defined(HANDLE_SDP_TYPE):
                # TYPEDEF ERROR: 1ULONGLONG HANDLE_SDP, *PHANDLE_SDP;
                HANDLE_SDP_TYPE = HANDLE_SDP
                HANDLE_SDP_FIELD_NAME = hConnection
                HANDLE_SDP_NULL = 0x0
            # END IF

            HANDLE_SDP_LOCAL = (HANDLE_SDP) -2

            _BTH_SDP_CONNECT._fields_ = [
                # Address of the remote SDP server. Cannot be the local radio.
                ('bthAddress', BTH_ADDR),
                # Combination of SDP_CONNECT_XXX flags
                ('fSdpConnect', ULONG),
                # SDP connection to the remote server
                ('HANDLE_SDP_FIELD_NAME', HANDLE_SDP_TYPE),
                # 30 seconds.
                ('requestTimeout', UCHAR),
            ]

            _BTH_SDP_DISCONNECT._fields_ = [
                # hConnection returned by BTH_SDP_CONNECT
                ('HANDLE_SDP_FIELD_NAME', HANDLE_SDP_TYPE),
            ]

            _BTH_SDP_RECORD._fields_ = [
                # Combination of SERVICE_SECURITY_XXX flags
                ('fSecurity', ULONG),
                # Combination of SERVICE_OPTION_XXX flags
                ('fOptions', ULONG),
                # combo of COD_SERVICE_XXX flags
                ('fCodService', ULONG),
                # The length of the record array, in bytes.
                ('recordLength', ULONG),
                # The SDP record in its raw format
                ('record', UCHAR * 1),
            ]

            _BTH_SDP_SERVICE_SEARCH_REQUEST._fields_ = [
                # Handle returned by the connect request or HANDLE_SDP_LOCAL
                ('HANDLE_SDP_FIELD_NAME', HANDLE_SDP_TYPE),
                # UUID. SDP spec mandates that a request can have a maximum of
                # 12 UUIDs.
                ('uuids', SdpQueryUuid * MAX_UUIDS_IN_QUERY),
            ]

            _BTH_SDP_ATTRIBUTE_SEARCH_REQUEST._fields_ = [
                # Handle returned by the connect request or HANDLE_SDP_LOCAL
                ('HANDLE_SDP_FIELD_NAME', HANDLE_SDP_TYPE),
                # Combo of SDP_SEARCH_Xxx flags
                ('searchFlags', ULONG),
                # previous BTH_SDP_SERVICE_SEARCH_RESPONSE.
                ('recordHandle', ULONG),
                # if a range is specified, the minAttribute must be <=
                # maxAttribute.
                ('range', SdpAttributeRange * 1),
            ]

            _BTH_SDP_SERVICE_ATTRIBUTE_SEARCH_REQUEST._fields_ = [
                # Handle returned by the connect request or HANDLE_SDP_LOCAL
                ('HANDLE_SDP_FIELD_NAME', HANDLE_SDP_TYPE),
                # Combo of SDP_SEARCH_Xxx flags
                ('searchFlags', ULONG),
                # See comments in BTH_SDP_SERVICE_SEARCH_REQUEST
                ('uuids', SdpQueryUuid * MAX_UUIDS_IN_QUERY),
                # See comments in BTH_SDP_ATTRIBUTE_SEARCH_REQUEST
                ('range', SdpAttributeRange * 1),
            ]

            _BTH_SDP_STREAM_RESPONSE._fields_ = [
                # A response cannot exceed 4GB in size.
                ('requiredSize', ULONG),
                # response will be partially copied into the response array.
                ('responseSize', ULONG),
                # The raw SDP response from the search.
                ('response', UCHAR * 1),
            ]
            if (NTDDI_VERSION > NTDDI_VISTASP1 or (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))):
                # Vendor specific HCI command header
                _BTH_COMMAND_HEADER._fields_ = [
                    # Opcode for the command
                    ('OpCode', USHORT),
                    # TotalParameterLength = TotalCommandLength -
                    # (ctypes.sizeof(BTH_COMMAND_HEADER)
                    ('TotalParameterLength', UCHAR),
                ]
                # Vendor Specific Command structure
                _BTH_VENDOR_SPECIFIC_COMMAND._fields_ = [
                    # Manufacturer ID
                    ('ManufacturerId', ULONG),
                    # LMP version is greater than this value.
                    ('LmpVersion', UCHAR),
                    # then if a single pattern matches the command, we decide
                    # that we have a match.
                    ('MatchAnySinglePattern', BOOLEAN),
                    # HCI Command Header
                    ('HciHeader', BTH_COMMAND_HEADER),
                    # Data for the above command including patterns
                    ('Data', UCHAR * 1),
                ]
                # Structure of patterns
                _BTH_VENDOR_PATTERN._fields_ = [
                    # Pattern Offset in the event structure excluding EVENT
                    # header
                    ('Offset', UCHAR),
                    # Size of the Pattern
                    ('Size', UCHAR),
                    # Pattern
                    ('Pattern', UCHAR * 1),
                ]
                # The buffer associated with GUID_BLUETOOTH_HCI_VENDOR_EVENT
                _BTH_VENDOR_EVENT_INFO._fields_ = [
                    # Local radio address with which the event is associated.
                    ('BthAddress', BTH_ADDR),
                    # Size of the event buffer including Event header
                    ('EventSize', ULONG),
                    # Information associated with the event
                    ('EventInfo', UCHAR * 1),
                ]
            # END IF    >= SP1 + KB942567
            if NTDDI_VERSION  >= NTDDI_WIN8:
                # Host supported features
                BTH_HOST_FEATURE_ENHANCED_RETRANSMISSION_MODE = (
                    0x0000000000000001
                )

                BTH_HOST_FEATURE_STREAMING_MODE = 0x0000000000000002
                BTH_HOST_FEATURE_LOW_ENERGY = 0x0000000000000004
                BTH_HOST_FEATURE_SCO_HCI = 0x0000000000000008
                BTH_HOST_FEATURE_SCO_HCIBYPASS = 0x0000000000000010

                _BTH_HOST_FEATURE_MASK._fields_ = [
                    # Mask of supported features.
                    ('Mask', ULONGLONG),
                    # Reserved for future use.
                    ('Reserved1', ULONGLONG),
                    ('Reserved2', ULONGLONG),
                ]
            # END IF  NTDDI_WIN8

            from pyWinAPI.shared.poppack_h import * # NOQA
        # END IF   (NTDDI_VERSION  >= NTDDI_VISTA)

        if _MSC_VER  >= 1200:
            pass
        else:
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   __BTHIOCTL_H__


