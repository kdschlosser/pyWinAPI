import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _MSiSCSI_HBAInformation(ctypes.Structure):
    pass


MSiSCSI_HBAInformation = _MSiSCSI_HBAInformation
PMSiSCSI_HBAInformation = POINTER(_MSiSCSI_HBAInformation)


class _MSiSCSI_HBASessionConfig(ctypes.Structure):
    pass


MSiSCSI_HBASessionConfig = _MSiSCSI_HBASessionConfig
PMSiSCSI_HBASessionConfig = POINTER(_MSiSCSI_HBASessionConfig)


class _ISCSI_ConnectionStaticInfo(ctypes.Structure):
    pass


ISCSI_ConnectionStaticInfo = _ISCSI_ConnectionStaticInfo
PISCSI_ConnectionStaticInfo = POINTER(_ISCSI_ConnectionStaticInfo)


class _ISCSI_SessionStaticInfo(ctypes.Structure):
    pass


ISCSI_SessionStaticInfo = _ISCSI_SessionStaticInfo
PISCSI_SessionStaticInfo = POINTER(_ISCSI_SessionStaticInfo)


class _ISCSI_PortalInfo(ctypes.Structure):
    pass


ISCSI_PortalInfo = _ISCSI_PortalInfo
PISCSI_PortalInfo = POINTER(_ISCSI_PortalInfo)


class _MSiSCSI_PortalInfoClass(ctypes.Structure):
    pass


MSiSCSI_PortalInfoClass = _MSiSCSI_PortalInfoClass
PMSiSCSI_PortalInfoClass = POINTER(_MSiSCSI_PortalInfoClass)


class _MSiSCSI_InitiatorSessionInfo(ctypes.Structure):
    pass


MSiSCSI_InitiatorSessionInfo = _MSiSCSI_InitiatorSessionInfo
PMSiSCSI_InitiatorSessionInfo = POINTER(_MSiSCSI_InitiatorSessionInfo)


class _MSiSCSI_InitiatorNodeFailureEvent(ctypes.Structure):
    pass


MSiSCSI_InitiatorNodeFailureEvent = _MSiSCSI_InitiatorNodeFailureEvent
PMSiSCSI_InitiatorNodeFailureEvent = POINTER(_MSiSCSI_InitiatorNodeFailureEvent)


class _MSiSCSI_InitiatorInstanceFailureEvent(ctypes.Structure):
    pass


MSiSCSI_InitiatorInstanceFailureEvent = _MSiSCSI_InitiatorInstanceFailureEvent
PMSiSCSI_InitiatorInstanceFailureEvent = POINTER(_MSiSCSI_InitiatorInstanceFailureEvent)


class _ISCSI_Path(ctypes.Structure):
    pass


ISCSI_Path = _ISCSI_Path
PISCSI_Path = POINTER(_ISCSI_Path)


class _ISCSI_Supported_LB_Policies(ctypes.Structure):
    pass


ISCSI_Supported_LB_Policies = _ISCSI_Supported_LB_Policies
PISCSI_Supported_LB_Policies = POINTER(_ISCSI_Supported_LB_Policies)


class _SetLoadBalancePolicy_IN(ctypes.Structure):
    pass


SetLoadBalancePolicy_IN = _SetLoadBalancePolicy_IN
PSetLoadBalancePolicy_IN = POINTER(_SetLoadBalancePolicy_IN)


class _SetLoadBalancePolicy_OUT(ctypes.Structure):
    pass


SetLoadBalancePolicy_OUT = _SetLoadBalancePolicy_OUT
PSetLoadBalancePolicy_OUT = POINTER(_SetLoadBalancePolicy_OUT)


class _MSiSCSI_QueryLBPolicy(ctypes.Structure):
    pass


MSiSCSI_QueryLBPolicy = _MSiSCSI_QueryLBPolicy
PMSiSCSI_QueryLBPolicy = POINTER(_MSiSCSI_QueryLBPolicy)


class _MSiSCSI_Eventlog(ctypes.Structure):
    pass


MSiSCSI_Eventlog = _MSiSCSI_Eventlog
PMSiSCSI_Eventlog = POINTER(_MSiSCSI_Eventlog)


class _ISCSI_RedirectPortalInfo(ctypes.Structure):
    pass


ISCSI_RedirectPortalInfo = _ISCSI_RedirectPortalInfo
PISCSI_RedirectPortalInfo = POINTER(_ISCSI_RedirectPortalInfo)


class _ISCSI_RedirectSessionInfo(ctypes.Structure):
    pass


ISCSI_RedirectSessionInfo = _ISCSI_RedirectSessionInfo
PISCSI_RedirectSessionInfo = POINTER(_ISCSI_RedirectSessionInfo)


class _MSiSCSI_RedirectPortalInfoClass(ctypes.Structure):
    pass


MSiSCSI_RedirectPortalInfoClass = _MSiSCSI_RedirectPortalInfoClass
PMSiSCSI_RedirectPortalInfoClass = POINTER(_MSiSCSI_RedirectPortalInfoClass)


class _PingIPAddress_IN(ctypes.Structure):
    pass


PingIPAddress_IN = _PingIPAddress_IN
PPingIPAddress_IN = POINTER(_PingIPAddress_IN)


class _PingIPAddress_OUT(ctypes.Structure):
    pass


PingIPAddress_OUT = _PingIPAddress_OUT
PPingIPAddress_OUT = POINTER(_PingIPAddress_OUT)

_iscsimgt_h_ = None
if not defined(_iscsimgt_h_):
    _iscsimgt_h_ = 1

    # MSiSCSI_HBAInformation - MSiSCSI_HBAInformation
    # ********************************************************************
    # iscsimgt.h
    # Module: iScsi Discovery api
    # Purpose: Internal header defining interface between user mode discovery
    # api dll and HBA driver miniport.
    # Copyright (c) 2001 Microsoft Corporation
    # ********************************************************************
    from pyWinAPI.km.iscsidef_h import * # NOQA

    # This class is required.
    # Adapter Information class. The iSCSI initiator service relies upon this
    # class in order to interface with your adapter. Implement one instance
    # per adapter instance.
    # This class must be registered using PDO instance names with a single
    # instance
    MSiSCSI_HBAInformationGuid = [
        0x58515BF3,
        0x2F59,
        0x4F37,
        [0xB7, 0x4F, 0x85, 0xAE, 0xEC, 0x65, 0x2A, 0xD6],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_HBAInformation_GUID = DEFINE_GUID(
            0x58515BF3,
            0x2F59,
            0x4F37,
            0xB7,
            0x4F,
            0x85,
            0xAE,
            0xEC,
            0x65,
            0x2A,
            0xD6
        )
    # END IF

    MSiSCSI_HBAInformation_UniqueAdapterId_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_HBAInformation_UniqueAdapterId_ID = 1
    MSiSCSI_HBAInformation_IntegratedTCPIP_SIZE = ctypes.sizeof(BOOLEAN)
    MSiSCSI_HBAInformation_IntegratedTCPIP_ID = 2
    MSiSCSI_HBAInformation_RequiresBinaryIpAddresses_SIZE = (
        ctypes.sizeof(BOOLEAN)
    )
    MSiSCSI_HBAInformation_RequiresBinaryIpAddresses_ID = 3
    MSiSCSI_HBAInformation_VersionMin_SIZE = ctypes.sizeof(UCHAR)
    MSiSCSI_HBAInformation_VersionMin_ID = 4
    MSiSCSI_HBAInformation_VersionMax_SIZE = ctypes.sizeof(UCHAR)
    MSiSCSI_HBAInformation_VersionMax_ID = 5
    MSiSCSI_HBAInformation_MultifunctionDevice_SIZE = ctypes.sizeof(BOOLEAN)
    MSiSCSI_HBAInformation_MultifunctionDevice_ID = 6
    MSiSCSI_HBAInformation_CacheValid_SIZE = ctypes.sizeof(BOOLEAN)
    MSiSCSI_HBAInformation_CacheValid_ID = 7
    MSiSCSI_HBAInformation_NumberOfPorts_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_HBAInformation_NumberOfPorts_ID = 8
    MSiSCSI_HBAInformation_Status_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_HBAInformation_Status_ID = 9
    MSiSCSI_HBAInformation_FunctionalitySupported_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_HBAInformation_FunctionalitySupported_ID = 10
    MSiSCSI_HBAInformation_GenerationalGuid_SIZE = ctypes.sizeof(UCHAR[16])
    MSiSCSI_HBAInformation_GenerationalGuid_ID = 11
    MSiSCSI_HBAInformation_MaxCDBLength_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_HBAInformation_MaxCDBLength_ID = 12
    MSiSCSI_HBAInformation_BiDiScsiCommands_SIZE = ctypes.sizeof(BOOLEAN)
    MSiSCSI_HBAInformation_BiDiScsiCommands_ID = 13
    MSiSCSI_HBAInformation_VendorID_ID = 14
    MSiSCSI_HBAInformation_VendorModel_ID = 15
    MSiSCSI_HBAInformation_VendorVersion_ID = 16
    MSiSCSI_HBAInformation_FirmwareVersion_ID = 17
    MSiSCSI_HBAInformation_AsicVersion_ID = 18
    MSiSCSI_HBAInformation_OptionRomVersion_ID = 19
    MSiSCSI_HBAInformation_SerialNumber_ID = 20
    MSiSCSI_HBAInformation_DriverName_ID = 21

    _MSiSCSI_HBAInformation._fields_ = [
        # Id that is globally unique for all instances of iSCSI initiators.
        # Use the address of the Adapter Extension or another address owned by
        # the device driver.
        ('UniqueAdapterId', ULONGLONG),
        # TRUE if TCP/IP traffic is integrated with the Windows networking
        # TCP/IP stack via a software only initiator. An adapter with its own
        # TCP/IP stack would set this to FALSE.
        ('IntegratedTCPIP', BOOLEAN),
        # If TRUE the iSCSI Initiator service will perform any DNS lookup and
        # pass binary IP addresses to the adapter; the adapter must be on the
        # same network as the Windows TCP/IP stack. If FALSE then DNS must be
        # available on adapter.
        ('RequiresBinaryIpAddresses', BOOLEAN),
        # Minimum version number of the iScsi spec supported by adapter
        ('VersionMin', UCHAR),
        # Maximum version number of the iSCSI spec supported by adapter
        ('VersionMax', UCHAR),
        # TRUE if this adapter is a multifunction device, that is it also
        # exposes a netcard interface
        ('MultifunctionDevice', BOOLEAN),
        # TRUE if the adapter caches are valid
        ('CacheValid', BOOLEAN),
        # Number of ports (or TCP/IP addresses) on the adapter
        ('NumberOfPorts', ULONG),
        # **typedef** Current status of adapter
        ('Status', ULONG),
        # **typedef** Bit flags that indicate various functionality supported
        ('FunctionalitySupported', ULONG),
        # This is the GUID value last set by the SetGenerationalGuid method in
        # the MSiSCSI_Operations class.
        ('GenerationalGuid', UCHAR * 16),
        # Maxumum CDB length supported by the adapter
        ('MaxCDBLength', ULONG),
        # TRUE if Bi - directionsal SCSI comamnd supported
        ('BiDiScsiCommands', BOOLEAN),
        # A text string describing the manufacturer of adapter
        ('VendorID', WCHAR * 255 + 1),
        # A text string set by the manufacturer describing the model of adapter
        ('VendorModel', WCHAR * 255 + 1),
        # A text string set by the manufacturer describing the version of
        # adapter
        ('VendorVersion', WCHAR * 255 + 1),
        # A text string set by the manufacturer describing the firmware
        # version of adapter
        ('FirmwareVersion', WCHAR * 255 + 1),
        # A text string set by the manufacturer describing the Asic version
        ('AsicVersion', WCHAR * 255 + 1),
        # A text string set by the manufacturer describing the option rom
        # version of adapter
        ('OptionRomVersion', WCHAR * 255 + 1),
        # A text string set by the manufacturer describing the serial number
        # of adapter
        ('SerialNumber', WCHAR * 255 + 1),
        # A text string specifying the name of the driver for the adapter
        ('DriverName', WCHAR * 255 + 1),
    ]

    # MSiSCSI_HBASessionConfig - MSiSCSI_HBASessionConfig
    # This class is optional.
    # This class allows the default session configuration to be managed. It
    # contains the default values to use when establishing a session.
    # This class must be registered using PDO instance names with a single
    # instance
    MSiSCSI_HBASessionConfigGuid = [
        0xB35694DE,
        0xD323,
        0x49D2,
        [0xAB, 0xB2, 0x81, 0x39, 0x20, 0x9A, 0xD1, 0x50],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_HBASessionConfig_GUID = DEFINE_GUID(
            0xB35694DE,
            0xD323,
            0x49D2,
            0xAB,
            0xB2,
            0x81,
            0x39,
            0x20,
            0x9A,
            0xD1,
            0x50
        )
    # END IF

    MSiSCSI_HBASessionConfig_InitialR2T_SIZE = ctypes.sizeof(BOOLEAN)
    MSiSCSI_HBASessionConfig_InitialR2T_ID = 1
    MSiSCSI_HBASessionConfig_ImmediateData_SIZE = ctypes.sizeof(BOOLEAN)
    MSiSCSI_HBASessionConfig_ImmediateData_ID = 2
    MSiSCSI_HBASessionConfig_MaxRecvDataSegmentLength_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_HBASessionConfig_MaxRecvDataSegmentLength_ID = 3
    MSiSCSI_HBASessionConfig_MaxBurstLength_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_HBASessionConfig_MaxBurstLength_ID = 4
    MSiSCSI_HBASessionConfig_FirstBurstLength_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_HBASessionConfig_FirstBurstLength_ID = 5
    MSiSCSI_HBASessionConfig_MaxOutstandingR2T_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_HBASessionConfig_MaxOutstandingR2T_ID = 6

    _MSiSCSI_HBASessionConfig._fields_ = [
        # The InitialR2T key is used to turn off the default use of R2T, thus
        # allowing an initiator to start sending data to a target as if it has
        # received an initial R2T with Buffer Offset=0 and Desired Data
        # Transfer Length=min (FirstBurstSize, Expected Data Transfer Length).
        ('InitialR2T', BOOLEAN),
        # The initiator and target negotiate support for immediate data. To
        # turn immediate data off, the initiator or target must state its
        # desire to do so. ImmediateData can be turned on if both the
        # initiator and target have ImmediateData=Yes.
        ('ImmediateData', BOOLEAN),
        # Maximum data segment length in bytes they can receive in an iSCSI
        # PDU.
        ('MaxRecvDataSegmentLength', ULONG),
        # Maximum SCSI data payload in bytes in an Data - In or a solicited
        # Data - Out iSCSI sequence.
        ('MaxBurstLength', ULONG),
        # maximum amount in bytes of unsolicited data an iSCSI initiator may
        # send to the target, during the execution of a single SCSI command.
        # This covers the immediate data (if any) and the sequence of
        # unsolicited Data - Out PDUs (if any) that follow the command.
        ('FirstBurstLength', ULONG),
        # Initiator and target negotiate the maximum number of outstanding
        # R2Ts per task, excluding any implied initial R2T that might be part
        # of that task. An R2T is considered outstanding until the last data
        # PDU (with the F bit set to 1) is transferred, or a sequence
        # reception timeout (section 6.12.1) is encountered for that data
        # sequence.
        ('MaxOutstandingR2T', ULONG),
    ]
    MSiSCSI_HBASessionConfig_SIZE = (
        FIELD_OFFSET(MSiSCSI_HBASessionConfig, 'MaxOutstandingR2T') +
        MSiSCSI_HBASessionConfig_MaxOutstandingR2T_SIZE
    )

    # ISCSI_ConnectionStaticInfo - ISCSI_ConnectionStaticInfo
    # iSCSI Static Connection Statistics Information
    ISCSI_ConnectionStaticInfoGuid = [
        0x3CE2D6A0,
        0x7346,
        0x4826,
        [0x97, 0x2F, 0xF2, 0xC1, 0x97, 0x79, 0xD1, 0xD1],
    ]
    if not defined(MIDL_PASS):
        ISCSI_ConnectionStaticInfo_GUID = DEFINE_GUID(
            0x3CE2D6A0,
            0x7346,
            0x4826,
            0x97,
            0x2F,
            0xF2,
            0xC1,
            0x97,
            0x79,
            0xD1,
            0xD1
        )
    # END IF

    ISCSI_ConnectionStaticInfo_UniqueConnectionId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    ISCSI_ConnectionStaticInfo_UniqueConnectionId_ID = 1
    ISCSI_ConnectionStaticInfo_CID_SIZE = ctypes.sizeof(USHORT)
    ISCSI_ConnectionStaticInfo_CID =_ID = 2
    ISCSI_ConnectionStaticInfo_State_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_ConnectionStaticInfo_State_ID = 3
    ISCSI_ConnectionStaticInfo_Protocol_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_ConnectionStaticInfo_Protocol_ID = 4
    ISCSI_ConnectionStaticInfo_HeaderIntegrity_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_ConnectionStaticInfo_HeaderIntegrity_ID = 5
    ISCSI_ConnectionStaticInfo_DataIntegrity_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_ConnectionStaticInfo_DataIntegrity_ID = 6
    ISCSI_ConnectionStaticInfo_Reserved_SIZE = ctypes.sizeof(USHORT)
    ISCSI_ConnectionStaticInfo_Reserved_ID = 7
    ISCSI_ConnectionStaticInfo_MaxRecvDataSegmentLength_SIZE = (
        ctypes.sizeof(ULONG)
    )
    ISCSI_ConnectionStaticInfo_MaxRecvDataSegmentLength_ID = 8
    ISCSI_ConnectionStaticInfo_AuthType_SIZE = ctypes.sizeof(ULONG)
    ISCSI_ConnectionStaticInfo_AuthType_ID = 9
    ISCSI_ConnectionStaticInfo_LocalAddr_SIZE = ctypes.sizeof(ISCSI_IP_Address)
    ISCSI_ConnectionStaticInfo_LocalAddr_ID = 10
    ISCSI_ConnectionStaticInfo_LocalPort_SIZE = ctypes.sizeof(ULONG)
    ISCSI_ConnectionStaticInfo_LocalPort_ID = 11
    ISCSI_ConnectionStaticInfo_RemoteAddr_SIZE = (
        ctypes.sizeof(ISCSI_IP_Address)
    )
    ISCSI_ConnectionStaticInfo_RemoteAddr_ID = 12
    ISCSI_ConnectionStaticInfo_RemotePort_SIZE = ctypes.sizeof(ULONG)
    ISCSI_ConnectionStaticInfo_RemotePort_ID = 13
    ISCSI_ConnectionStaticInfo_EstimatedThroughput_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    ISCSI_ConnectionStaticInfo_EstimatedThroughput_ID = 14
    ISCSI_ConnectionStaticInfo_MaxDatagramSize_SIZE = ctypes.sizeof(ULONG)
    ISCSI_ConnectionStaticInfo_MaxDatagramSize_ID = 15

    _ISCSI_ConnectionStaticInfo._fields_ = [
        # A uniquely generated connection ID. Do not confuse this with CID.
        ('UniqueConnectionId', ULONGLONG),
        # The iSCSI connection ID for this connection instance.
        ('CID', USHORT),
        # **typedef** Indicates the current state of this connection
        ('State', UCHAR),
        # **typedef** The transport protocol over which this connection
        # instance is running.
        ('Protocol', UCHAR),
        # **typedef** The name of the iSCSI header digest scheme in use within
        # this session.
        ('HeaderIntegrity', UCHAR),
        # **typedef** The name of the iSCSI data digest scheme in use within
        # this session.
        ('DataIntegrity', UCHAR),
        # Must be zero
        ('Reserved', USHORT),
        # The maximum data payload size supported for command or data PDUs
        # within this session.
        ('MaxRecvDataSegmentLength', ULONG),
        # **typedef** Authentication type used when establishing the
        # connection.
        ('AuthType', ULONG),
        # The local network address used for the connection
        ('LocalAddr', ISCSI_IP_Address),
        # The local port used for the connection
        ('LocalPort', ULONG),
        # The remote network address used for the connection
        ('RemoteAddr', ISCSI_IP_Address),
        # The remote port used for the connection
        ('RemotePort', ULONG),
        # Estimated throughput of the link in bytes per second
        ('EstimatedThroughput', ULONGLONG),
        # Maximum Datagram size supported by the transport in bytes
        ('MaxDatagramSize', ULONG),
    ]
    ISCSI_ConnectionStaticInfo_SIZE = (
        FIELD_OFFSET(ISCSI_ConnectionStaticInfo, 'MaxDatagramSize') +
        ISCSI_ConnectionStaticInfo_MaxDatagramSize_SIZE
    )

    # ISCSI_SessionStaticInfo - ISCSI_SessionStaticInfo
    # iSCSI Static Sessions Statistics Information
    ISCSI_SessionStaticInfoGuid = [
        0xB71D2538,
        0x57E2,
        0x4228,
        [0x88, 0x8B, 0x1A, 0xF9, 0xB3, 0xBD, 0x01, 0xCD],
    ]

    if not defined(MIDL_PASS):
        ISCSI_SessionStaticInfo_GUID = DEFINE_GUID(
            0xB71D2538,
            0x57E2,
            0x4228,
            0x88,
            0x8B,
            0x1A,
            0xF9,
            0xB3,
            0xBD,
            0x01,
            0xCD
        )
    # END IF

    ISCSI_SessionStaticInfo_UniqueSessionId_SIZE = ctypes.sizeof(ULONGLONG)
    ISCSI_SessionStaticInfo_UniqueSessionId_ID = 1
    ISCSI_SessionStaticInfo_InitiatoriSCSIName_ID = 2
    ISCSI_SessionStaticInfo_TargetiSCSIName_ID = 3
    ISCSI_SessionStaticInfo_TSID_SIZE = ctypes.sizeof(USHORT)
    ISCSI_SessionStaticInfo_TSID_ID = 4
    ISCSI_SessionStaticInfo_ISID_SIZE = ctypes.sizeof(UCHAR[6])
    ISCSI_SessionStaticInfo_ISID_ID = 5
    ISCSI_SessionStaticInfo_InitialR2t_SIZE = ctypes.sizeof(BOOLEAN)
    ISCSI_SessionStaticInfo_InitialR2t_ID = 6
    ISCSI_SessionStaticInfo_ImmediateData_SIZE = ctypes.sizeof(BOOLEAN)
    ISCSI_SessionStaticInfo_ImmediateData_ID = 7
    ISCSI_SessionStaticInfo_Type_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_SessionStaticInfo_Type_ID = 8
    ISCSI_SessionStaticInfo_DataSequenceInOrder_SIZE = ctypes.sizeof(BOOLEAN)
    ISCSI_SessionStaticInfo_DataSequenceInOrder_ID = 9
    ISCSI_SessionStaticInfo_DataPduInOrder_SIZE = ctypes.sizeof(BOOLEAN)
    ISCSI_SessionStaticInfo_DataPduInOrder_ID = 10
    ISCSI_SessionStaticInfo_ErrorRecoveryLevel_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_SessionStaticInfo_ErrorRecoveryLevel_ID = 11
    ISCSI_SessionStaticInfo_MaxOutstandingR2t_SIZE = ctypes.sizeof(ULONG)
    ISCSI_SessionStaticInfo_MaxOutstandingR2t_ID = 12
    ISCSI_SessionStaticInfo_FirstBurstLength_SIZE = ctypes.sizeof(ULONG)
    ISCSI_SessionStaticInfo_FirstBurstLength_ID = 13
    ISCSI_SessionStaticInfo_MaxBurstLength_SIZE = ctypes.sizeof(ULONG)
    ISCSI_SessionStaticInfo_MaxBurstLength_ID = 14
    ISCSI_SessionStaticInfo_MaxConnections_SIZE = ctypes.sizeof(ULONG)
    ISCSI_SessionStaticInfo_MaxConnections_ID = 15
    ISCSI_SessionStaticInfo_ConnectionCount_SIZE = ctypes.sizeof(USHORT)
    ISCSI_SessionStaticInfo_ConnectionCount_ID = 16
    ISCSI_SessionStaticInfo_ConnectionsList_ID = 17

    _ISCSI_SessionStaticInfo._fields_ = [
        # A uniquely generated session ID, it is the same id returned by the
        # LoginToTarget method. Do not confuse this with ISID or SSID.
        ('UniqueSessionId', ULONGLONG),
        # Initiator node name used to establish the session
        ('InitiatoriSCSIName', WCHAR * 223 + 1),
        # iSCSI node name of the target
        ('TargetiSCSIName', WCHAR * 223 + 1),
        # Target - defined portion of the iSCSI Session ID
        ('TSID', USHORT),
        # Initiator - defined portion of the iSCSI Session ID
        ('ISID', UCHAR * 6),
        # If TRUE, the initiator must wait for an R2T before sending data to
        # the target. If FALSE, the initiator may send data immediately,
        # within limits set by FirstBurstSize and the expected data transfer
        # length of the request.
        ('InitialR2t', BOOLEAN),
        # If TRUE indicates whether the initiator and target have agreed to
        # support immediate commands on this session.
        ('ImmediateData', BOOLEAN),
        # **typedef** Type of iSCSI session
        ('Type', UCHAR),
        # If FALSE indicates that data PDU Sequences may be transferred in any
        # order. If TRUE indicates that data PDU sequences must be transferred
        # using continuously increasing offsets, except during error recovery.
        ('DataSequenceInOrder', BOOLEAN),
        # If FALSE indicates that data PDUs within sequences may be in any
        # order. If TRUE indicates that data PDUs within sequences must be at
        # continuously increasing addresses, with no gaps or overlay between
        # PDUs.
        ('DataPduInOrder', BOOLEAN),
        # The level of error recovery negotiated between the initiator and the
        # target.
        ('ErrorRecoveryLevel', UCHAR),
        # The maximum number of outstanding request - to - transmit (R2T) per
        # task within this session
        ('MaxOutstandingR2t', ULONG),
        # The maximum length supported for unsolicited data sent within this
        # session
        ('FirstBurstLength', ULONG),
        # The maximum number of bytes which can be sent within a single
        # sequence of Data - In or Data - Out PDUs
        ('MaxBurstLength', ULONG),
        # The maximum number of connections that will be allowed within this
        # session
        ('MaxConnections', ULONG),
        # The number of connections that currently belong to this session
        ('ConnectionCount', USHORT),
        # List of ISCSI_ConnectionStaticInfo. ConnectionCount specifies the
        # number of elements in the array. NOTE: This is a variable length
        # array.
        ('ConnectionsList', ISCSI_ConnectionStaticInfo * 1),
    ]

    # ISCSI_PortalInfo - ISCSI_PortalInfo
    # iSCSI Portal Info
    ISCSI_PortalInfoGuid = [
        0x4FB9130E,
        0x1FEF,
        0x4AE6,
        [0x9E, 0x48, 0x77, 0x83, 0x92, 0x04, 0xD4, 0x13],
    ]

    if not defined(MIDL_PASS):
        ISCSI_PortalInfo_GUID = DEFINE_GUID(
            0x4FB9130E,
            0x1FEF,
            0x4AE6,
            0x9E,
            0x48,
            0x77,
            0x83,
            0x92,
            0x04,
            0xD4,
            0x13
        )
    # END IF

    ISCSI_PortalInfo_Index_SIZE = ctypes.sizeof(ULONG)
    ISCSI_PortalInfo_Index_ID = 1
    ISCSI_PortalInfo_PortalType_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_PortalInfo_PortalType_ID = 2
    ISCSI_PortalInfo_Protocol_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_PortalInfo_Protocol_ID = 3
    ISCSI_PortalInfo_Reserved1_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_PortalInfo_Reserved1_ID = 4
    ISCSI_PortalInfo_Reserved2_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_PortalInfo_Reserved2_ID = 5
    ISCSI_PortalInfo_IPAddr_SIZE = ctypes.sizeof(ISCSI_IP_Address)
    ISCSI_PortalInfo_IPAddr_ID = 6
    ISCSI_PortalInfo_Port_SIZE = ctypes.sizeof(ULONG)
    ISCSI_PortalInfo_Port_ID = 7
    ISCSI_PortalInfo_PortalTag_SIZE = ctypes.sizeof(USHORT)
    ISCSI_PortalInfo_PortalTag_ID = 8

    _ISCSI_PortalInfo._fields_ = [
        # An integer used to uniquely identify a paticular port
        ('Index', ULONG),
        # **typedef** The type of portal (Initiator or Target)
        ('PortalType', UCHAR),
        # The portal's transport protocol
        ('Protocol', UCHAR),
        ('Reserved1', UCHAR),
        ('Reserved2', UCHAR),
        # The portal's network address
        ('IPAddr', ISCSI_IP_Address),
        # The portal's socket number
        ('Port', ULONG),
        # The portal's aggregation tag
        ('PortalTag', USHORT),
    ]
    ISCSI_PortalInfo_SIZE = (
        FIELD_OFFSET(ISCSI_PortalInfo, 'PortalTag') +
        ISCSI_PortalInfo_PortalTag_SIZE
    )

    # MSiSCSI_PortalInfoClass - MSiSCSI_PortalInfoClass
    # iScsi Portal Information Class
    # This class is recommended.
    # This class exposes portal information.
    # This class must be registered using PDO instance names with a single
    # instance
    MSiSCSI_PortalInfoClassGuid = [
        0x84CA6FD6,
        0xB152,
        0x4E6A,
        [0x88, 0x69, 0xFD, 0xE5, 0xE3, 0x7B, 0x61, 0x57],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_PortalInfoClass_GUID = DEFINE_GUID(
            0x84CA6FD6,
            0xB152,
            0x4E6A,
            0x88,
            0x69,
            0xFD,
            0xE5,
            0xE3,
            0x7B,
            0x61,
            0x57
        )
    # END IF

    MSiSCSI_PortalInfoClass_PortalInfoCount_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_PortalInfoClass_PortalInfoCount_ID = 1
    MSiSCSI_PortalInfoClass_PortalInformation_ID = 2

    _MSiSCSI_PortalInfoClass._fields_ = [
        # Number of elements in iScsiPortalInfo array
        ('PortalInfoCount', ULONG),
        # Variable length array of iScsiPortalInfo. PortalInfoCount specifies
        # the number of elements in the array. NOTE: this is a variable length
        # array.
        ('PortalInformation', ISCSI_PortalInfo * 1),
    ]

    # MSiSCSI_InitiatorSessionInfo - MSiSCSI_InitiatorSessionInfo
    # iSCSI Static Initiator Session Information
    # This class is required.
    # This class exposes session and connection information on the initiator.
    # This class should use PDO instance names with a single instance.
    MSiSCSI_InitiatorSessionInfoGuid = [
        0xD7931411,
        0x0376,
        0x4869,
        [0xA4, 0x91, 0x8D, 0x67, 0x9B, 0xFC, 0x00, 0x4A],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_InitiatorSessionInfo_GUID = DEFINE_GUID(
            0xD7931411,
            0x0376,
            0x4869,
            0xA4,
            0x91,
            0x8D,
            0x67,
            0x9B,
            0xFC,
            0x00,
            0x4A
        )
    # END IF

    MSiSCSI_InitiatorSessionInfo_UniqueAdapterId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_InitiatorSessionInfo_UniqueAdapterId_ID = 1
    MSiSCSI_InitiatorSessionInfo_SessionCount_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_InitiatorSessionInfo_SessionCount_ID = 2
    MSiSCSI_InitiatorSessionInfo_SessionsList_ID = 3

    _MSiSCSI_InitiatorSessionInfo._fields_ = [
        # Id that is globally unique to each instance of each adapter. Using
        # the address of the Adapter Extension is a good idea.
        ('UniqueAdapterId', ULONGLONG),
        # Number of elements in SessionList array
        ('SessionCount', ULONG),
        # Variable length array of sessions. SessionCount specifies the number
        # of elements in the array. NOTE: this is a variable length array.
        ('SessionsList', ISCSI_SessionStaticInfo * 1),
    ]

    # MSiSCSI_InitiatorNodeFailureEvent - MSiSCSI_InitiatorNodeFailureEvent
    # iSCSI Initiator Node Failure Event
    # This class is recommended.
    # This class fires an event when a node failure occurs.
    # This class should use PDO instance names with a single instance.
    MSiSCSI_InitiatorNodeFailureEventGuid = [
        0x1221948A,
        0x6332,
        0x4AC2,
        [0xAA, 0x04, 0x26, 0x8A, 0xAB, 0xCE, 0xCE, 0x4F],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_InitiatorNodeFailureEvent_GUID = DEFINE_GUID(
            0x1221948A,
            0x6332,
            0x4AC2,
            0xAA,
            0x04,
            0x26,
            0x8A,
            0xAB,
            0xCE,
            0xCE,
            0x4F
        )
    # END IF

    MSiSCSI_InitiatorNodeFailureEvent_FailureTime_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_InitiatorNodeFailureEvent_FailureTime_ID = 1
    MSiSCSI_InitiatorNodeFailureEvent_FailureType_SIZE = ctypes.sizeof(UCHAR)
    MSiSCSI_InitiatorNodeFailureEvent_FailureType_ID = 2
    MSiSCSI_InitiatorNodeFailureEvent_TargetFailureName_ID = 3
    MSiSCSI_InitiatorNodeFailureEvent_TargetFailureAddr_SIZE = (
        ctypes.sizeof(ISCSI_IP_Address)
    )
    MSiSCSI_InitiatorNodeFailureEvent_TargetFailureAddr_ID = 4

    _MSiSCSI_InitiatorNodeFailureEvent._fields_ = [
        # Timestamp denoting time failure occured
        ('FailureTime', ULONGLONG),
        # **typedef** Types of initiator node failure
        ('FailureType', UCHAR),
        # Name of target involved in failure
        ('TargetFailureName', WCHAR * 223 + 1),
        # Network address of target involved in failure
        ('TargetFailureAddr', ISCSI_IP_Address),
    ]
    MSiSCSI_InitiatorNodeFailureEvent_SIZE = (
        FIELD_OFFSET(MSiSCSI_InitiatorNodeFailureEvent, 'TargetFailureAddr') +
        MSiSCSI_InitiatorNodeFailureEvent_TargetFailureAddr_SIZE
    )

    # MSiSCSI_InitiatorInstanceFailureEvent -
    # MSiSCSI_InitiatorInstanceFailureEvent
    # iSCSI Initiator Instance Failure Event
    # This class is recommended.
    # This class fires an event when an initiator failure occurs.
    # This class should use PDO instance names with a single instance.
    MSiSCSI_InitiatorInstanceFailureEventGuid = [
        0xE67E1BDB,
        0xD130,
        0x4143,
        [0x9E, 0xB2, 0x8B, 0xEE, 0x18, 0x99, 0xFD, 0x52],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_InitiatorInstanceFailureEvent_GUID = DEFINE_GUID(
            0xE67E1BDB,
            0xD130,
            0x4143,
            0x9E,
            0xB2,
            0x8B,
            0xEE,
            0x18,
            0x99,
            0xFD,
            0x52
        )
    # END IF

    MSiSCSI_InitiatorInstanceFailureEvent_FailureType_SIZE = ctypes.sizeof(UCHAR)
    MSiSCSI_InitiatorInstanceFailureEvent_FailureType_ID = 1
    MSiSCSI_InitiatorInstanceFailureEvent_RemoteNodeName_ID = 2

    _MSiSCSI_InitiatorInstanceFailureEvent._fields_ = [
        # **typedef** Type of failure
        ('FailureType', UCHAR),
        # Name of target involved in failure
        ('RemoteNodeName', WCHAR * 223 + 1),
    ]

    # ISCSI_Path - ISCSI_Path
    # This class describes an iSCSI Path (A TCP Connection to the target)
    ISCSI_PathGuid = [
        0xC8775641,
        0x5430,
        0x4220,
        [0xBA, 0x25, 0x7D, 0xA5, 0x61, 0xCB, 0x64, 0xCE],
    ]

    if not defined(MIDL_PASS):
        ISCSI_Path_GUID = DEFINE_GUID(
            0xC8775641,
            0x5430,
            0x4220,
            0xBA,
            0x25,
            0x7D,
            0xA5,
            0x61,
            0xCB,
            0x64,
            0xCE
        )
    # END IF

    ISCSI_Path_UniqueConnectionId_SIZE = ctypes.sizeof(ULONGLONG)
    ISCSI_Path_UniqueConnectionId_ID = 1
    ISCSI_Path_EstimatedLinkSpeed_SIZE = ctypes.sizeof(ULONGLONG)
    ISCSI_Path_EstimatedLinkSpeed_ID = 2
    ISCSI_Path_PathWeight_SIZE = ctypes.sizeof(ULONG)
    ISCSI_Path_PathWeight_ID = 3
    ISCSI_Path_PrimaryPath_SIZE = ctypes.sizeof(ULONG)
    ISCSI_Path_PrimaryPath_ID = 4
    ISCSI_Path_ConnectionStatus_SIZE = ctypes.sizeof(ULONG)
    ISCSI_Path_ConnectionStatus_ID = 5
    ISCSI_Path_TCPOffLoadAvailable_SIZE = ctypes.sizeof(ULONG)
    ISCSI_Path_TCPOffLoadAvailable_ID = 6

    _ISCSI_Path._fields_ = [
        # iSCSI Unique connection id
        ('UniqueConnectionId', ULONGLONG),
        # Estimated speed of the connection in MegaBits Per Second
        ('EstimatedLinkSpeed', ULONGLONG),
        # Weight assigned to the path
        ('PathWeight', ULONG),
        # Flag set to 1 if the path is a primary path, 0 otherwise.
        ('PrimaryPath', ULONG),
        # Status of the path - connected, disconnected, reconnecting
        ('ConnectionStatus', ULONG),
        # Flag set to 1 if TCP offload is supported for this connection, 0
        # otherwise.
        ('TCPOffLoadAvailable', ULONG),
    ]

    ISCSI_Path_SIZE = (
        FIELD_OFFSET(ISCSI_Path, 'TCPOffLoadAvailable') +
        ISCSI_Path_TCPOffLoadAvailable_SIZE
    )

    # ISCSI_Supported_LB_Policies - ISCSI_Supported_LB_Policies
    # iSCSI Initiator Load Balance Policies supported
    ISCSI_Supported_LB_PoliciesGuid = [
        0x749AFE4D,
        0x804D,
        0x4662,
        [0xA6, 0x8B, 0xDC, 0x69, 0x66, 0x55, 0xC7, 0x9A],
    ]

    if not defined(MIDL_PASS):
        ISCSI_Supported_LB_Policies_GUID = DEFINE_GUID(
            0x749AFE4D,
            0x804D,
            0x4662,
            0xA6,
            0x8B,
            0xDC,
            0x69,
            0x66,
            0x55,
            0xC7,
            0x9A
        )
    # END IF

    ISCSI_Supported_LB_Policies_UniqueSessionId_SIZE = ctypes.sizeof(ULONGLONG)
    ISCSI_Supported_LB_Policies_UniqueSessionId_ID = 1
    ISCSI_Supported_LB_Policies_LoadBalancePolicy_SIZE = ctypes.sizeof(ULONG)
    ISCSI_Supported_LB_Policies_LoadBalancePolicy_ID = 2
    ISCSI_Supported_LB_Policies_iSCSI_PathCount_SIZE = ctypes.sizeof(ULONG)
    ISCSI_Supported_LB_Policies_iSCSI_PathCount_ID = 3
    ISCSI_Supported_LB_Policies_iSCSI_Paths_ID = 4

    _ISCSI_Supported_LB_Policies._fields_ = [
        # Id that is unique to this session within this adapter.
        ('UniqueSessionId', ULONGLONG),
        # Load Balance policy supported by the iSCSI Initiator
        ('LoadBalancePolicy', ULONG),
        # Number of entries in MSiSCSI_Paths array
        ('iSCSI_PathCount', ULONG),
        # Describes iSCSI Initiator Paths
        ('iSCSI_Paths', ISCSI_Path * 1),
    ]

    # MSiSCSI_LB_Operations - MSiSCSI_LB_Operations
    # Set iSCSI Initiator Load Balance Policies
    MSiSCSI_LB_OperationsGuid = [
        0xA7DFE761,
        0xB6BC,
        0x4490,
        [0x91, 0xB0, 0xD9, 0xCF, 0x4A, 0x24, 0xD3, 0x7C],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_LB_Operations_GUID = DEFINE_GUID(
            0xA7DFE761,
            0xB6BC,
            0x4490,
            0x91,
            0xB0,
            0xD9,
            0xCF,
            0x4A,
            0x24,
            0xD3,
            0x7C
        )
    # END IF

    # Method id definitions for MSiSCSI_LB_Operations
    # SetLoadBalancePolicy instructs the iSCSI Initiator what Load Balance
    # policy to use.
    SetLoadBalancePolicy = 10

    SetLoadBalancePolicy_IN_LoadBalancePolicies_SIZE = (
        ctypes.sizeof(ISCSI_Supported_LB_Policies)
    )
    SetLoadBalancePolicy_IN_LoadBalancePolicies_ID = 1

    _SetLoadBalancePolicy_IN._fields_ = [
        # New Load Balance policy to be set
        ('LoadBalancePolicies', ISCSI_Supported_LB_Policies),
    ]
    SetLoadBalancePolicy_IN_SIZE = (
        FIELD_OFFSET(SetLoadBalancePolicy_IN, 'LoadBalancePolicies') +
        SetLoadBalancePolicy_IN_LoadBalancePolicies_SIZE
    )

    SetLoadBalancePolicy_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    SetLoadBalancePolicy_OUT_Status_ID = 2

    _SetLoadBalancePolicy_OUT._fields_ = [
        # Status of the operation
        ('Status', ULONG),
    ]
    SetLoadBalancePolicy_OUT_SIZE = (
        FIELD_OFFSET(SetLoadBalancePolicy_OUT, 'Status') +
        SetLoadBalancePolicy_OUT_Status_SIZE
    )

    # MSiSCSI_QueryLBPolicy - MSiSCSI_QueryLBPolicy
    # Query Load Balance policy used by iSCSI Initiator
    # MSiSCSI_QueryLBPolicy class is used to query the Initiator about
    # the load balance policy that is currently used.
    MSiSCSI_QueryLBPolicyGuid = [
        0xE0AECAEE,
        0xB311,
        0x426F,
        [0xB6, 0x7A, 0x18, 0xD5, 0xE5, 0x5D, 0x09, 0x96],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_QueryLBPolicy_GUID = DEFINE_GUID(
            0xE0AECAEE,
            0xB311,
            0x426F,
            0xB6,
            0x7A,
            0x18,
            0xD5,
            0xE5,
            0x5D,
            0x09,
            0x96
        )
    # END IF

    MSiSCSI_QueryLBPolicy_UniqueAdapterId_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_QueryLBPolicy_UniqueAdapterId_ID = 1
    MSiSCSI_QueryLBPolicy_Reserved_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_QueryLBPolicy_Reserved_ID = 2
    MSiSCSI_QueryLBPolicy_SessionCount_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_QueryLBPolicy_SessionCount_ID = 3
    MSiSCSI_QueryLBPolicy_LoadBalancePolicies_ID = 4

    _MSiSCSI_QueryLBPolicy._fields_ = [
        # Id that is globally unique to each instance of each adapter. Using
        # the address of the Adapter Extension is a good idea.
        ('UniqueAdapterId', ULONGLONG),
        ('Reserved', ULONG),
        # Number of elements in LoadBalancePolicies array
        ('SessionCount', ULONG),
        # Load Balance Policy that is currently being used by iSCSI Initiator
        # - one element for each session on the adapter
        ('LoadBalancePolicies', ISCSI_Supported_LB_Policies * 1),
    ]

    # MSiSCSI_Eventlog - MSiSCSI_Eventlog
    # iSCSI Eventlog generation event
    # Miniports can fire this event to cause eventlog entries to be
    # included in the system eventlog. This is useful as the iscsilog.h
    # header has many iSCSI specific eventlog messages that are useful for
    # troubleshooting, but can't be fired directly by a miniport. By
    # firing this WMI event appropriately a miniport can cause a useful
    # eventlog entry to be included in the system eventlog
    MSiSCSI_EventlogGuid = [
        0xE6B8552B,
        0x7C62,
        0x4C6E,
        [0x99, 0xEB, 0x67, 0xCE, 0x60, 0x87, 0x89, 0x4C],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_Eventlog_GUID = DEFINE_GUID(
            0xE6B8552B,
            0x7C62,
            0x4C6E,
            0x99,
            0xEB,
            0x67,
            0xCE,
            0x60,
            0x87,
            0x89,
            0x4C
        )
    # END IF

    MSiSCSI_Eventlog_Type_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_Eventlog_Type_ID = 1
    MSiSCSI_Eventlog_LogToEventlog_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_Eventlog_LogToEventlog_ID = 2
    MSiSCSI_Eventlog_Size_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_Eventlog_Size_ID = 3
    MSiSCSI_Eventlog_AdditionalData_ID = 4

    _MSiSCSI_Eventlog._fields_ = [
        # Type of eventlog message
        ('Type', ULONG),
        # If zero then this event is not logged to system eventlog
        ('LogToEventlog', ULONG),
        # Size of Additional Data
        ('Size', ULONG),
        # Additional data to include in eventlog message, typically iSCSI
        # Header
        ('AdditionalData', UCHAR * 1),
    ]

    # ISCSI_RedirectPortalInfo - ISCSI_RedirectPortalInfo
    # iSCSI Redirect Portal Info
    ISCSI_RedirectPortalInfoGuid = [
        0xF6004CE6,
        0x9507,
        0x4D86,
        [0xAE, 0x1E, 0xE9, 0xD6, 0x4F, 0x16, 0x6F, 0x2F],
    ]

    if not defined(MIDL_PASS):
        ISCSI_RedirectPortalInfo_GUID = DEFINE_GUID(
            0xF6004CE6,
            0x9507,
            0x4D86,
            0xAE,
            0x1E,
            0xE9,
            0xD6,
            0x4F,
            0x16,
            0x6F,
            0x2F
        )
    # END IF

    ISCSI_RedirectPortalInfo_UniqueConnectionId_SIZE = ctypes.sizeof(ULONGLONG)
    ISCSI_RedirectPortalInfo_UniqueConnectionId_ID = 1
    ISCSI_RedirectPortalInfo_OriginalIPAddr_SIZE = ctypes.sizeof(
        ISCSI_IP_Address)
    ISCSI_RedirectPortalInfo_OriginalIPAddr_ID = 2
    ISCSI_RedirectPortalInfo_OriginalPort_SIZE = ctypes.sizeof(ULONG)
    ISCSI_RedirectPortalInfo_OriginalPort_ID = 3
    ISCSI_RedirectPortalInfo_RedirectedIPAddr_SIZE = ctypes.sizeof(
        ISCSI_IP_Address)
    ISCSI_RedirectPortalInfo_RedirectedIPAddr_ID = 4
    ISCSI_RedirectPortalInfo_RedirectedPort_SIZE = ctypes.sizeof(ULONG)
    ISCSI_RedirectPortalInfo_RedirectedPort_ID = 5
    ISCSI_RedirectPortalInfo_Redirected_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_RedirectPortalInfo_Redirected_ID = 6
    ISCSI_RedirectPortalInfo_TemporaryRedirect_SIZE = ctypes.sizeof(UCHAR)
    ISCSI_RedirectPortalInfo_TemporaryRedirect_ID = 7

    _ISCSI_RedirectPortalInfo._fields_ = [
        # A uniquely generated connection ID. Do not confuse this with CID.
        ('UniqueConnectionId', ULONGLONG),
        # Original Target IP Address given in the login
        ('OriginalIPAddr', ISCSI_IP_Address),
        # Original Target portal's socket number given in the login
        ('OriginalPort', ULONG),
        # Redirected Target IP Address
        ('RedirectedIPAddr', ISCSI_IP_Address),
        # Redirected Target portal's socket number
        ('RedirectedPort', ULONG),
        # TRUE if login was redirected. RedirectedIPAddr and RedirectedPort
        # are valid then.
        ('Redirected', UCHAR),
        # TRUE if the redirection is temporary. FALSE otherwise
        ('TemporaryRedirect', UCHAR),
    ]
    ISCSI_RedirectPortalInfo_SIZE = (
        FIELD_OFFSET(ISCSI_RedirectPortalInfo, 'TemporaryRedirect') +
        ISCSI_RedirectPortalInfo_TemporaryRedirect_SIZE
    )

    # ISCSI_RedirectSessionInfo - ISCSI_RedirectSessionInfo
    # iSCSI Redirect Session Info
    ISCSI_RedirectSessionInfoGuid = [
        0xED60BC3F,
        0x3D56,
        0x42F0,
        [0xB4, 0xD0, 0x81, 0xDD, 0x16, 0xE2, 0x85, 0x15],
    ]

    if not defined(MIDL_PASS):
        ISCSI_RedirectSessionInfo_GUID = DEFINE_GUID(
            0xED60BC3F,
            0x3D56,
            0x42F0,
            0xB4,
            0xD0,
            0x81,
            0xDD,
            0x16,
            0xE2,
            0x85,
            0x15
        )
    # END IF

    ISCSI_RedirectSessionInfo_UniqueSessionId_SIZE = ctypes.sizeof(ULONGLONG)
    ISCSI_RedirectSessionInfo_UniqueSessionId_ID = 1
    ISCSI_RedirectSessionInfo_TargetPortalGroupTag_SIZE = ctypes.sizeof(ULONG)
    ISCSI_RedirectSessionInfo_TargetPortalGroupTag_ID = 2
    ISCSI_RedirectSessionInfo_ConnectionCount_SIZE = ctypes.sizeof(ULONG)
    ISCSI_RedirectSessionInfo_ConnectionCount_ID = 3
    ISCSI_RedirectSessionInfo_RedirectPortalList_ID = 4

    _ISCSI_RedirectSessionInfo._fields_ = [
        # A uniquely generated session ID, it is the same id returned by the
        # LoginToTarget method. Do not confuse this with ISID or SSID.
        ('UniqueSessionId', ULONGLONG),
        # Target portal group tag for this Session
        ('TargetPortalGroupTag', ULONG),
        # Number of elements in RedirectPortalList array
        ('ConnectionCount', ULONG),
        # Redirect portal info - one element for each connection in the session
        ('RedirectPortalList', ISCSI_RedirectPortalInfo * 1),
    ]

    # MSiSCSI_RedirectPortalInfoClass - MSiSCSI_RedirectPortalInfoClass
    # iScsi Redirect Portal Information Class
    # This class is recommended.
    # This class exposes portal information. It provides the original and
    # redirected target portal information for an iSCSI Connection.
    # This class must be registered using PDO instance names with a single
    # instance
    MSiSCSI_RedirectPortalInfoClassGuid = [
        0xDAF7F63A,
        0xF9EA,
        0x4869,
        [0x87, 0xE1, 0xAE, 0x8A, 0x7C, 0x22, 0x61, 0xE2],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_RedirectPortalInfoClass_GUID = DEFINE_GUID(
            0xDAF7F63A,
            0xF9EA,
            0x4869,
            0x87,
            0xE1,
            0xAE,
            0x8A,
            0x7C,
            0x22,
            0x61,
            0xE2
        )
    # END IF

    MSiSCSI_RedirectPortalInfoClass_UniqueAdapterId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_RedirectPortalInfoClass_UniqueAdapterId_ID = 1
    MSiSCSI_RedirectPortalInfoClass_SessionCount_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_RedirectPortalInfoClass_SessionCount_ID = 2
    MSiSCSI_RedirectPortalInfoClass_RedirectSessionList_ID = 3

    _MSiSCSI_RedirectPortalInfoClass._fields_ = [
        # Id that is globally unique for all instances of iSCSI initiators.
        ('UniqueAdapterId', ULONGLONG),
        # Number of elements in RedirectSessionInfo array
        ('SessionCount', ULONG),
        # Variable length array of ISCSI_RedirectSessionInfo. SessionCount
        # specifies the number of elements in the array. NOTE: this is a
        # variable length array.
        ('RedirectSessionList', ISCSI_RedirectSessionInfo * 1),
    ]

    # MSiSCSI_ManagementOperations - MSiSCSI_ManagementOperations
    # This class is recommended.
    # iSCSI management applications rely upon this
    # class in order to interface with the adapter. Implement one instance
    # per miniport instance (adapter).
    # This class must be registered using PDO instance names with a single
    # instance.
    MSiSCSI_ManagementOperationsGuid = [
        0xB8D765F0,
        0x2D93,
        0x4DA2,
        [0x81, 0x86, 0xA1, 0x87, 0x62, 0x2B, 0x43, 0x02],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_ManagementOperations_GUID = DEFINE_GUID(
            0xB8D765F0,
            0x2D93,
            0x4DA2,
            0x81,
            0x86,
            0xA1,
            0x87,
            0x62,
            0x2B,
            0x43,
            0x02
        )
    # END IF

    # Method id definitions for MSiSCSI_ManagementOperations
    # This method is recommended.
    # Ping will perform ICMP ping requests to the destination address
    # and return the number of ping responses received. This is only supported
    # by some HBA, use the ping command for the software initiator.
    PingIPAddress = 10

    PingIPAddress_IN_RequestCount_SIZE = ctypes.sizeof(ULONG)
    PingIPAddress_IN_RequestCount_ID = 1
    PingIPAddress_IN_RequestSize_SIZE = ctypes.sizeof(ULONG)
    PingIPAddress_IN_RequestSize_ID = 2
    PingIPAddress_IN_Timeout_SIZE = ctypes.sizeof(ULONG)
    PingIPAddress_IN_Timeout_ID = 3
    PingIPAddress_IN_Address_SIZE = ctypes.sizeof(ISCSI_IP_Address)
    PingIPAddress_IN_Address_ID = 4

    _PingIPAddress_IN._fields_ = [
        # Number of requests to send
        ('RequestCount', ULONG),
        # Number of bytes in each request
        ('RequestSize', ULONG),
        # Number of ms to wait for response
        ('Timeout', ULONG),
        # IP address to ping
        ('Address', ISCSI_IP_Address),
    ]
    PingIPAddress_IN_SIZE = (
        FIELD_OFFSET(PingIPAddress_IN, 'Address') +
        PingIPAddress_IN_Address_SIZE
    )

    PingIPAddress_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    PingIPAddress_OUT_Status_ID = 5
    PingIPAddress_OUT_ResponsesReceived_SIZE = ctypes.sizeof(ULONG)
    PingIPAddress_OUT_ResponsesReceived_ID = 6

    _PingIPAddress_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
        # Number of responses received
        ('ResponsesReceived', ULONG),
    ]
    PingIPAddress_OUT_SIZE = (
        FIELD_OFFSET(PingIPAddress_OUT, 'ResponsesReceived') +
        PingIPAddress_OUT_ResponsesReceived_SIZE
    )
# END IF
