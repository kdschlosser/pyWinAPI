import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _MSiSCSI_MMIPSECStats(ctypes.Structure):
    pass


MSiSCSI_MMIPSECStats = _MSiSCSI_MMIPSECStats
PMSiSCSI_MMIPSECStats = POINTER(_MSiSCSI_MMIPSECStats)


class _MSiSCSI_QMIPSECStats(ctypes.Structure):
    pass


MSiSCSI_QMIPSECStats = _MSiSCSI_QMIPSECStats
PMSiSCSI_QMIPSECStats = POINTER(_MSiSCSI_QMIPSECStats)


class _MSiSCSI_ConnectionStatistics(ctypes.Structure):
    pass


MSiSCSI_ConnectionStatistics = _MSiSCSI_ConnectionStatistics
PMSiSCSI_ConnectionStatistics = POINTER(_MSiSCSI_ConnectionStatistics)


class _MSiSCSI_SessionStatistics(ctypes.Structure):
    pass


MSiSCSI_SessionStatistics = _MSiSCSI_SessionStatistics
PMSiSCSI_SessionStatistics = POINTER(_MSiSCSI_SessionStatistics)


class _MSiSCSI_InitiatorLoginStatistics(ctypes.Structure):
    pass


MSiSCSI_InitiatorLoginStatistics = _MSiSCSI_InitiatorLoginStatistics
PMSiSCSI_InitiatorLoginStatistics = POINTER(_MSiSCSI_InitiatorLoginStatistics)


class _MSiSCSI_InitiatorInstanceStatistics(ctypes.Structure):
    pass


MSiSCSI_InitiatorInstanceStatistics = _MSiSCSI_InitiatorInstanceStatistics
PMSiSCSI_InitiatorInstanceStatistics = POINTER(_MSiSCSI_InitiatorInstanceStatistics)


class _MSiSCSI_NICPerformance(ctypes.Structure):
    pass


MSiSCSI_NICPerformance = _MSiSCSI_NICPerformance
PMSiSCSI_NICPerformance = POINTER(_MSiSCSI_NICPerformance)


class _MSiSCSI_RequestTimeStatistics(ctypes.Structure):
    pass


MSiSCSI_RequestTimeStatistics = _MSiSCSI_RequestTimeStatistics
PMSiSCSI_RequestTimeStatistics = POINTER(_MSiSCSI_RequestTimeStatistics)

_iscsiprf_h_ = None
if not defined(_iscsiprf_h_):
    _iscsiprf_h_ = 1

    # MSiSCSI_MMIPSECStats - MSiSCSI_MMIPSECStats
    # iSCSI HBA main mode IPSEC Statistics
    # ********************************************************************
    # iscsiprf.h
    # Module: iSCSI Discovery api
    # Purpose: Internal header defining interface between user mode discovery
    # api dll and HBA driver miniport.
    # Note: These classes are recommended as by implementing them the data
    # exposed will be available in sysmon (perfmon) when running on
    # Windows XP and Windows .Net server
    # Copyright (c) 2001 Microsoft Corporation
    # ********************************************************************
    # This class exposes the main mode IPSEC statistics
    # This class must be registered with PDO instance names using a single
    # instance
    MSiSCSI_MMIPSECStatsGuid = [
        0x36B58EA2,
        0xC461,
        0x4BB0,
        [0xAC, 0x8E, 0x95, 0x2F, 0x59, 0xD2, 0x51, 0xED],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_MMIPSECStats_GUID = DEFINE_GUID(
            0x36B58EA2,
            0xC461,
            0x4BB0,
            0xAC,
            0x8E,
            0x95,
            0x2F,
            0x59,
            0xD2,
            0x51,
            0xED
        )
    # END IF
    MSiSCSI_MMIPSECStats_ActiveAcquire_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_ActiveAcquire_ID = 1
    MSiSCSI_MMIPSECStats_ActiveReceive_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_ActiveReceive_ID = 2
    MSiSCSI_MMIPSECStats_AcquireFailures_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_AcquireFailures_ID = 3
    MSiSCSI_MMIPSECStats_ReceiveFailures_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_ReceiveFailures_ID = 4
    MSiSCSI_MMIPSECStats_SendFailures_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_SendFailures_ID = 5
    MSiSCSI_MMIPSECStats_AcquireHeapSize_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_AcquireHeapSize_ID = 6
    MSiSCSI_MMIPSECStats_ReceiveHeapSize_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_ReceiveHeapSize_ID = 7
    MSiSCSI_MMIPSECStats_NegotiationFailures_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_NegotiationFailures_ID = 8
    MSiSCSI_MMIPSECStats_AuthenticationFailures_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_MMIPSECStats_AuthenticationFailures_ID = 9
    MSiSCSI_MMIPSECStats_InvalidCookiesReceived_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_MMIPSECStats_InvalidCookiesReceived_ID = 10
    MSiSCSI_MMIPSECStats_TotalGetSPI_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_TotalGetSPI_ID = 11
    MSiSCSI_MMIPSECStats_KeyAdditions_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_KeyAdditions_ID = 12
    MSiSCSI_MMIPSECStats_KeyUpdates_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_KeyUpdates_ID = 13
    MSiSCSI_MMIPSECStats_GetSPIFailures_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_GetSPIFailures_ID = 14
    MSiSCSI_MMIPSECStats_KeyAdditionFailures_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_KeyAdditionFailures_ID = 15
    MSiSCSI_MMIPSECStats_KeyUpdateFailures_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_KeyUpdateFailures_ID = 16
    MSiSCSI_MMIPSECStats_ConnectionListSize_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_ConnectionListSize_ID = 17
    MSiSCSI_MMIPSECStats_OakleyMainMode_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_OakleyMainMode_ID = 18
    MSiSCSI_MMIPSECStats_OakleyQuickMode_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_OakleyQuickMode_ID = 19
    MSiSCSI_MMIPSECStats_InvalidPackets_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_InvalidPackets_ID = 20
    MSiSCSI_MMIPSECStats_SoftAssociations_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_MMIPSECStats_SoftAssociations_ID = 21

    _MSiSCSI_MMIPSECStats._fields_ = [
        # An acquire is a request by the IPSEC driver to have IKE perform a
        # task. The active acquire statistic includes the outstanding request
        # and the number of any queued requests. Typically, the number of
        # active acquires is 1. Under a heavy load, the number of active
        # acquires is 1 and the number of requests that are queued by IKE for
        # processing.
        ('ActiveAcquire', ULONGLONG),
        # The number of IKE messages received that are queued for processing.
        ('ActiveReceive', ULONGLONG),
        # The number of times that an acquire has failed.
        ('AcquireFailures', ULONGLONG),
        # The number of times that the TCP stack has failed when receiving IKE
        # messages.
        ('ReceiveFailures', ULONGLONG),
        # The number of times that the TCP/IP stack has failed when sending
        # IKE messages.
        ('SendFailures', ULONGLONG),
        # The number of entries in the acquire heap, which stores active
        # acquires. This number increases under a heavy load and then
        # gradually decreases over time, as the acquire heap is cleared.
        ('AcquireHeapSize', ULONGLONG),
        # The number of entries in the IKE receive buffers for incoming IKE
        # messages.
        ('ReceiveHeapSize', ULONGLONG),
        # The total number of negotiation failures that occurred during main
        # mode (also known as Phase I) or quick mode (also known as Phase II)
        # negotiation.
        ('NegotiationFailures', ULONGLONG),
        # The total number of identity authentication failures
        # (Kerberos, certificate, and preshared key) that occurred during main
        # mode negotiation.
        ('AuthenticationFailures', ULONGLONG),
        # A cookie is a value contained in a received IKE message that is used
        # by IKE to find the state of an active main mode. A cookie in a
        # received IKE message that cannot be matched with an active main mode
        # is invalid.
        ('InvalidCookiesReceived', ULONGLONG),
        # The total number of requests submitted by IKE to obtain a unique
        # Security Parameters Index (SPI).
        ('TotalGetSPI', ULONGLONG),
        # The number of outbound quick mode security associations (SAs) added
        # by IKE
        ('KeyAdditions', ULONGLONG),
        # The number of inbound quick mode security associations (SAs) added
        # by IKE
        ('KeyUpdates', ULONGLONG),
        # The total number of requests submitted by IKE to obtain a unique
        # Security Parameters Index (SPI) that failed.
        ('GetSPIFailures', ULONGLONG),
        # The number of outbound quick mode security associations (SAs)
        # submitted by IKE that failed
        ('KeyAdditionFailures', ULONGLONG),
        # The number of inbound quick mode security associations (SAs) added
        # by IKE
        ('KeyUpdateFailures', ULONGLONG),
        # The number of quick mode state entries.
        ('ConnectionListSize', ULONGLONG),
        # The total number of successful SAs created during main mode
        # negotiations.
        ('OakleyMainMode', ULONGLONG),
        # The total number of successful SAs created during quick mode
        # negotiations
        ('OakleyQuickMode', ULONGLONG),
        # The number of received IKE messages that are invalid, including IKE
        # messages with invalid header fields, incorrect payload lengths, and
        # incorrect values for the responder cookie
        # (when it should be set to 0).
        ('InvalidPackets', ULONGLONG),
        # The total number of negotiations that resulted in the use of
        # plaintext (also known as soft SAs). This typically reflects the
        # number of associations formed with computers that did not respond to
        # main mode negotiation attempts. This can include both non - IPSEC -
        # aware computers and IPSEC - aware computers that do not have IPSEC
        # policy to negotiate security with this IPSEC peer.
        ('SoftAssociations', ULONGLONG),
    ]
    MSiSCSI_MMIPSECStats_SIZE = (
        FIELD_OFFSET(MSiSCSI_MMIPSECStats, 'SoftAssociations') +
        MSiSCSI_MMIPSECStats_SoftAssociations_SIZE
    )

    # MSiSCSI_QMIPSECStats - MSiSCSI_QMIPSECStats
    # iSCSI HBA quick mode IPSEC Statistics
    # This class exposes the quick mode IPSEC statistics
    # This class must be registered with PDO instance names using a single
    # instance
    MSiSCSI_QMIPSECStatsGuid = [
        0xB4D1C606,
        0x8682,
        0x4B7A,
        [0xAC, 0x6B, 0xD8, 0x83, 0xD9, 0x15, 0x55, 0xFB],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_QMIPSECStats_GUID = DEFINE_GUID(
            0xB4D1C606,
            0x8682,
            0x4B7A,
            0xAC,
            0x6B,
            0xD8,
            0x83,
            0xD9,
            0x15,
            0x55,
            0xFB
        )
    # END IF

    MSiSCSI_QMIPSECStats_ActiveSA_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_QMIPSECStats_ActiveSA_ID = 1
    MSiSCSI_QMIPSECStats_PendingKeyOperations_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_QMIPSECStats_PendingKeyOperations_ID = 2
    MSiSCSI_QMIPSECStats_KeyAdditions_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_QMIPSECStats_KeyAdditions_ID = 3
    MSiSCSI_QMIPSECStats_KeyDeletions_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_QMIPSECStats_KeyDeletions_ID = 4
    MSiSCSI_QMIPSECStats_ReKeys_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_QMIPSECStats_ReKeys_ID = 5
    MSiSCSI_QMIPSECStats_ActiveTunnels_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_QMIPSECStats_ActiveTunnels_ID = 6
    MSiSCSI_QMIPSECStats_BadSPIPackets_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_QMIPSECStats_BadSPIPackets_ID = 7
    MSiSCSI_QMIPSECStats_PacketsNotDecrypted_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_QMIPSECStats_PacketsNotDecrypted_ID = 8
    MSiSCSI_QMIPSECStats_PacketsNotAuthenticated_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_QMIPSECStats_PacketsNotAuthenticated_ID = 9
    MSiSCSI_QMIPSECStats_PacketsWithReplayDetection_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_QMIPSECStats_PacketsWithReplayDetection_ID = 10
    MSiSCSI_QMIPSECStats_ConfidentialBytesSent_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_QMIPSECStats_ConfidentialBytesSent_ID = 11
    MSiSCSI_QMIPSECStats_ConfidentialBytesReceived_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_QMIPSECStats_ConfidentialBytesReceived_ID = 12
    MSiSCSI_QMIPSECStats_AuthenticatedBytesSent_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_QMIPSECStats_AuthenticatedBytesSent_ID = 13
    MSiSCSI_QMIPSECStats_AuthenticatedBytesReceived_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_QMIPSECStats_AuthenticatedBytesReceived_ID = 14
    MSiSCSI_QMIPSECStats_TransportBytesSent_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_QMIPSECStats_TransportBytesSent_ID = 15
    MSiSCSI_QMIPSECStats_TransportBytesReceived_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_QMIPSECStats_TransportBytesReceived_ID = 16
    MSiSCSI_QMIPSECStats_TunnelBytesSent_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_QMIPSECStats_TunnelBytesSent_ID = 17
    MSiSCSI_QMIPSECStats_TunnelBytesReceived_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_QMIPSECStats_TunnelBytesReceived_ID = 18

    _MSiSCSI_QMIPSECStats._fields_ = [
        # The number of active IPSEC SAs
        ('ActiveSA', ULONGLONG),
        # The number of IPSEC key operations in progress
        ('PendingKeyOperations', ULONGLONG),
        # The total number of successful IPSEC SA negotiations
        ('KeyAdditions', ULONGLONG),
        # The total number of key deletions for IPSEC SA
        ('KeyDeletions', ULONGLONG),
        # The number of rekey operations for IPSEC SAs.
        ('ReKeys', ULONGLONG),
        # The number of active IPSEC tunnels.
        ('ActiveTunnels', ULONGLONG),
        # The total number of packets for which the Security Parameters Index
        # (SPI) was incorrect.
        ('BadSPIPackets', ULONGLONG),
        # The total number of packets that failed decryption.
        ('PacketsNotDecrypted', ULONGLONG),
        # The total number of packets for which data could not be verified.
        ('PacketsNotAuthenticated', ULONGLONG),
        # The total number of packets that contained a valid Sequence Number
        # field.
        ('PacketsWithReplayDetection', ULONGLONG),
        # The number of bytes sent using the ESP protocol.
        ('ConfidentialBytesSent', ULONGLONG),
        # The number of bytes received using the ESP protocol.
        ('ConfidentialBytesReceived', ULONGLONG),
        # The number of bytes sent using the AH protocol.
        ('AuthenticatedBytesSent', ULONGLONG),
        # The number of bytes received using the AH protocol.
        ('AuthenticatedBytesReceived', ULONGLONG),
        # The number of bytes sent using the IPSEC protocol.
        ('TransportBytesSent', ULONGLONG),
        # The number of bytes received using the IPSEC protocol.
        ('TransportBytesReceived', ULONGLONG),
        # The number of bytes sent using the IPSEC tunnel mode.
        ('TunnelBytesSent', ULONGLONG),
        # The number of bytes received using the IPSEC tunnel mode.
        ('TunnelBytesReceived', ULONGLONG),
    ]
    MSiSCSI_QMIPSECStats_SIZE = (
        FIELD_OFFSET(MSiSCSI_QMIPSECStats, 'TunnelBytesReceived') +
        MSiSCSI_QMIPSECStats_TunnelBytesReceived_SIZE
    )

    # MSiSCSI_ConnectionStatistics - MSiSCSI_ConnectionStatistics
    # iSCSI Connection Statistics
    # This class exposes connection statistics statistics
    # This class must be registered with dynamic instance names using
    # a specific format:
    # targetname_: where the first is the SID, and the second
    # is the CID.
    MSiSCSI_ConnectionStatisticsGuid = [
        0x4AE27CD9,
        0x8DFA,
        0x4C37,
        [0xA4, 0x2C, 0xB8, 0x8A, 0x93, 0xE3, 0xE5, 0x21],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_ConnectionStatistics_GUID = DEFINE_GUID(
            0x4AE27CD9,
            0x8DFA,
            0x4C37,
            0xA4,
            0x2C,
            0xB8,
            0x8A,
            0x93,
            0xE3,
            0xE5,
            0x21
        )
    # END IF

    MSiSCSI_ConnectionStatistics_iSCSIName_ID = 1
    MSiSCSI_ConnectionStatistics_CID_SIZE = ctypes.sizeof(USHORT)
    MSiSCSI_ConnectionStatistics_CID_ID = 2
    MSiSCSI_ConnectionStatistics_USID_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_ConnectionStatistics_USID_ID = 3
    MSiSCSI_ConnectionStatistics_UniqueAdapterId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_ConnectionStatistics_UniqueAdapterId_ID = 4
    MSiSCSI_ConnectionStatistics_BytesSent_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_ConnectionStatistics_BytesSent_ID = 5
    MSiSCSI_ConnectionStatistics_BytesReceived_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_ConnectionStatistics_BytesReceived_ID = 6
    MSiSCSI_ConnectionStatistics_PDUCommandsSent_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_ConnectionStatistics_PDUCommandsSent_ID = 7
    MSiSCSI_ConnectionStatistics_PDUResponsesReceived_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_ConnectionStatistics_PDUResponsesReceived_ID = 8

    _MSiSCSI_ConnectionStatistics._fields_ = [
        # Name of the iSCSI Target
        ('iSCSIName', WCHAR * 223 + 1),
        # The iSCSI connection ID for this connection instance.
        ('CID', USHORT),
        # A uniquely generated session ID used only internally. This is the
        # value returned by the LoginToTarget method.
        ('USID', ULONGLONG),
        # Id that is globally unique to each instance of each adapter. This is
        # the value reported by the MSiSCSI_HBAInformation class.
        ('UniqueAdapterId', ULONGLONG),
        # Count of of bytes sent over this connection
        ('BytesSent', ULONGLONG),
        # Count of of bytes received over this connection
        ('BytesReceived', ULONGLONG),
        # Count of of PDU sent over this connection
        ('PDUCommandsSent', ULONGLONG),
        # Count of of PDU received over this connection
        ('PDUResponsesReceived', ULONGLONG),
    ]
    MSiSCSI_ConnectionStatistics_SIZE = (
        FIELD_OFFSET(MSiSCSI_ConnectionStatistics, 'PDUResponsesReceived') +
        MSiSCSI_ConnectionStatistics_PDUResponsesReceived_SIZE
    )

    # MSiSCSI_SessionStatistics - MSiSCSI_SessionStatistics
    # iSCSI Session Statistics
    # This class exposes session statistics
    # This class must be registered with dynamic instance names using
    # a specific format:
    # targetname_ where the is the SID
    MSiSCSI_SessionStatisticsGuid = [
        0xC827993C,
        0x6D1F,
        0x4194,
        [0x9B, 0x5C, 0xD7, 0xC0, 0xA5, 0xF1, 0xCF, 0xB7],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_SessionStatistics_GUID = DEFINE_GUID(
            0xC827993C,
            0x6D1F,
            0x4194,
            0x9B,
            0x5C,
            0xD7,
            0xC0,
            0xA5,
            0xF1,
            0xCF,
            0xB7
        )
    # END IF

    MSiSCSI_SessionStatistics_iSCSIName_ID = 1
    MSiSCSI_SessionStatistics_USID_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_SessionStatistics_USID_ID = 2
    MSiSCSI_SessionStatistics_UniqueAdapterId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_SessionStatistics_UniqueAdapterId_ID = 3
    MSiSCSI_SessionStatistics_BytesSent_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_SessionStatistics_BytesSent_ID = 4
    MSiSCSI_SessionStatistics_BytesReceived_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_SessionStatistics_BytesReceived_ID = 5
    MSiSCSI_SessionStatistics_PDUCommandsSent_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_SessionStatistics_PDUCommandsSent_ID = 6
    MSiSCSI_SessionStatistics_PDUResponsesReceived_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_SessionStatistics_PDUResponsesReceived_ID = 7
    MSiSCSI_SessionStatistics_DigestErrors_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_SessionStatistics_DigestErrors_ID = 8
    MSiSCSI_SessionStatistics_ConnectionTimeoutErrors_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_SessionStatistics_ConnectionTimeoutErrors_ID = 9
    MSiSCSI_SessionStatistics_FormatErrors_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_SessionStatistics_FormatErrors_ID = 10

    _MSiSCSI_SessionStatistics._fields_ = [
        # Name of the iSCSI Target
        ('iSCSIName', WCHAR * 223 + 1),
        # A uniquely generated session ID used only internally. This is the
        # value returned by the LoginToTarget method.
        ('USID', ULONGLONG),
        # Id that is globally unique to each instance of each adapter. This is
        # the value reported by the MSiSCSI_HBAInformation class.
        ('UniqueAdapterId', ULONGLONG),
        # Number of bytes sent over this session
        ('BytesSent', ULONGLONG),
        # Number of bytes received over this session
        ('BytesReceived', ULONGLONG),
        # Number of PDU sent over this session
        ('PDUCommandsSent', ULONGLONG),
        # Number of PDU received over this session
        ('PDUResponsesReceived', ULONGLONG),
        # Count of Number of Digest errors occured in this session
        ('DigestErrors', ULONGLONG),
        # Count of Number of ConnectionTimeout errors occured in this session
        ('ConnectionTimeoutErrors', ULONGLONG),
        # Count of Number of Format errors occured in this session
        ('FormatErrors', ULONGLONG),
    ]
    MSiSCSI_SessionStatistics_SIZE = (
        FIELD_OFFSET(MSiSCSI_SessionStatistics, 'FormatErrors') +
        MSiSCSI_SessionStatistics_FormatErrors_SIZE
    )

    # MSiSCSI_InitiatorLoginStatistics - MSiSCSI_InitiatorLoginStatistics
    # iSCSI Initiator Login Statistics
    # This class exposes login statistics
    # This class must be registered with PDO instance names
    MSiSCSI_InitiatorLoginStatisticsGuid = [
        0xF022F413,
        0x3BF5,
        0x47EC,
        [0xA9, 0x42, 0x33, 0xB8, 0x1C, 0xF8, 0xE7, 0xFF],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_InitiatorLoginStatistics_GUID = DEFINE_GUID(
            0xF022F413,
            0x3BF5,
            0x47EC,
            0xA9,
            0x42,
            0x33,
            0xB8,
            0x1C,
            0xF8,
            0xE7,
            0xFF
        )
    # END IF
    MSiSCSI_InitiatorLoginStatistics_UniqueAdapterId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_InitiatorLoginStatistics_UniqueAdapterId_ID = 1
    MSiSCSI_InitiatorLoginStatistics_LoginAcceptRsps_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorLoginStatistics_LoginAcceptRsps_ID = 2
    MSiSCSI_InitiatorLoginStatistics_LoginOtherFailRsps_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorLoginStatistics_LoginOtherFailRsps_ID = 3
    MSiSCSI_InitiatorLoginStatistics_LoginRedirectRsps_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorLoginStatistics_LoginRedirectRsps_ID = 4
    MSiSCSI_InitiatorLoginStatistics_LoginAuthFailRsps_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorLoginStatistics_LoginAuthFailRsps_ID = 5
    MSiSCSI_InitiatorLoginStatistics_LoginAuthenticateFails_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorLoginStatistics_LoginAuthenticateFails_ID = 6
    MSiSCSI_InitiatorLoginStatistics_LoginNegotiateFails_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorLoginStatistics_LoginNegotiateFails_ID = 7
    MSiSCSI_InitiatorLoginStatistics_LogoutNormals_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorLoginStatistics_LogoutNormals_ID = 8
    MSiSCSI_InitiatorLoginStatistics_LogoutOtherCodes_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorLoginStatistics_LogoutOtherCodes_ID = 9
    MSiSCSI_InitiatorLoginStatistics_LoginFailures_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorLoginStatistics_LoginFailures_ID = 10

    _MSiSCSI_InitiatorLoginStatistics._fields_ = [
        # Id that is globally unique to each instance of each adapter. This is
        # the value reported by the MSiSCSI_HBAInformation class.
        ('UniqueAdapterId', ULONGLONG),
        # Count of Login Accept Responses
        ('LoginAcceptRsps', ULONG),
        # Count of Login other failed Responses
        ('LoginOtherFailRsps', ULONG),
        # Count of Login Redirect Responses
        ('LoginRedirectRsps', ULONG),
        # Count of Login Authentication Failed Responses
        ('LoginAuthFailRsps', ULONG),
        # Count of the number of times a login is aborted due to a target
        # authentication failure
        ('LoginAuthenticateFails', ULONG),
        # Count of the number of times login failed due to negotiation failure
        # with target
        ('LoginNegotiateFails', ULONG),
        # Count of Logout command PDU with reason code 0
        ('LogoutNormals', ULONG),
        # Count of Logout command PDUs with status code other than 0
        ('LogoutOtherCodes', ULONG),
        # The object counts the number of times a login attempt from this
        # local initiator has failed
        ('LoginFailures', ULONG),
    ]
    MSiSCSI_InitiatorLoginStatistics_SIZE = (
        FIELD_OFFSET(MSiSCSI_InitiatorLoginStatistics, 'LoginFailures') +
        MSiSCSI_InitiatorLoginStatistics_LoginFailures_SIZE
    )

    # MSiSCSI_InitiatorInstanceStatistics - MSiSCSI_InitiatorInstanceStatistics
    # iSCSI Initiator Instance Statistics
    # This class exposes initiator statistics
    # This class must be registered with PDO instance names
    MSiSCSI_InitiatorInstanceStatisticsGuid = [
        0xFA30C290,
        0x68DB,
        0x430A,
        [0xAF, 0x76, 0x91, 0xA2, 0xE1, 0xC4, 0x91, 0x54],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_InitiatorInstanceStatistics_GUID = DEFINE_GUID(
            0xFA30C290,
            0x68DB,
            0x430A,
            0xAF,
            0x76,
            0x91,
            0xA2,
            0xE1,
            0xC4,
            0x91,
            0x54
        )
    # END IF
    MSiSCSI_InitiatorInstanceStatistics_UniqueAdapterId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_InitiatorInstanceStatistics_UniqueAdapterId_ID = 1
    MSiSCSI_InitiatorInstanceStatistics_SessionDigestErrorCount_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorInstanceStatistics_SessionDigestErrorCount_ID = 2
    MSiSCSI_InitiatorInstanceStatistics_SessionConnectionTimeoutErrorCount_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorInstanceStatistics_SessionConnectionTimeoutErrorCount_ID = (
        3
    )
    MSiSCSI_InitiatorInstanceStatistics_SessionFormatErrorCount_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorInstanceStatistics_SessionFormatErrorCount_ID = 4
    MSiSCSI_InitiatorInstanceStatistics_SessionFailureCount_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_InitiatorInstanceStatistics_SessionFailureCount_ID = 5

    _MSiSCSI_InitiatorInstanceStatistics._fields_ = [
        # Id that is globally unique to each instance of each adapter. This is
        # the value reported by the MSiSCSI_HBAInformation class.
        ('UniqueAdapterId', ULONGLONG),
        # Count of Session digest errors
        ('SessionDigestErrorCount', ULONG),
        # Count of Session connection timeout error
        ('SessionConnectionTimeoutErrorCount', ULONG),
        # Count of Session format error
        ('SessionFormatErrorCount', ULONG),
        # Number of Sessions failed belonging to this instance
        ('SessionFailureCount', ULONG),
    ]
    MSiSCSI_InitiatorInstanceStatistics_SIZE = (
        FIELD_OFFSET(MSiSCSI_InitiatorInstanceStatistics, 'SessionFailureCount') +
        MSiSCSI_InitiatorInstanceStatistics_SessionFailureCount_SIZE
    )

    # MSiSCSI_NICPerformance - MSiSCSI_NICPerformance
    # NIC performance information class, implement one instance for each port
    # on
    # your adapter.
    # This class must be registered with PDO instance names with one instance
    # names for each port
    MSiSCSI_NICPerformanceGuid = [
        0x5C59FD61,
        0xE919,
        0x4687,
        [0x84, 0xE2, 0x72, 0x00, 0xAB, 0xE2, 0x20, 0x9B],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_NICPerformance_GUID = DEFINE_GUID(
            0x5C59FD61,
            0xE919,
            0x4687,
            0x84,
            0xE2,
            0x72,
            0x00,
            0xAB,
            0xE2,
            0x20,
            0x9B
        )
    # END IF
    MSiSCSI_NICPerformance_BytesTransmitted_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_NICPerformance_BytesTransmitted_ID = 1
    MSiSCSI_NICPerformance_BytesReceived_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_NICPerformance_BytesReceived_ID = 2
    MSiSCSI_NICPerformance_PDUTransmitted_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_NICPerformance_PDUTransmitted_ID = 3
    MSiSCSI_NICPerformance_PDUReceived_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_NICPerformance_PDUReceived_ID = 4

    _MSiSCSI_NICPerformance._fields_ = [
        # Number of bytes transmitted via ethernet port
        ('BytesTransmitted', ULONG),
        # Number of bytes received via ethernet port
        ('BytesReceived', ULONG),
        # Number of PDU transmitted via ethernet port
        ('PDUTransmitted', ULONG),
        # Number of PDU received via ethernet port
        ('PDUReceived', ULONG),
    ]
    MSiSCSI_NICPerformance_SIZE = (
        FIELD_OFFSET(MSiSCSI_NICPerformance, 'PDUReceived') +
        MSiSCSI_NICPerformance_PDUReceived_SIZE
    )

    # MSiSCSI_RequestTimeStatistics - MSiSCSI_RequestTimeStatistics
    # iSCSI Request Processing Time
    # This class exposes request processing time statistics
    # This class must be registered with dynamic instance names using
    # a specific format:
    # targetname_: where the first is the SID, and the second
    # is the CID.
    MSiSCSI_RequestTimeStatisticsGuid = [
        0xE0B40AA8,
        0x544B,
        0x4D5E,
        [0xBA, 0x60, 0xA0, 0x3F, 0x13, 0x6D, 0xA8, 0x3D],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_RequestTimeStatistics_GUID = DEFINE_GUID(
            0xE0B40AA8,
            0x544B,
            0x4D5E,
            0xBA,
            0x60,
            0xA0,
            0x3F,
            0x13,
            0x6D,
            0xA8,
            0x3D
        )
    # END IF
    MSiSCSI_RequestTimeStatistics_iSCSIName_ID = 1
    MSiSCSI_RequestTimeStatistics_CID_SIZE = ctypes.sizeof(USHORT)
    MSiSCSI_RequestTimeStatistics_CID_ID = 2
    MSiSCSI_RequestTimeStatistics_USID_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_RequestTimeStatistics_USID_ID = 3
    MSiSCSI_RequestTimeStatistics_UniqueAdapterId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_RequestTimeStatistics_UniqueAdapterId_ID = 4
    MSiSCSI_RequestTimeStatistics_MaximumProcessingTime_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_RequestTimeStatistics_MaximumProcessingTime_ID = 5
    MSiSCSI_RequestTimeStatistics_AverageProcessingTime_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_RequestTimeStatistics_AverageProcessingTime_ID = 6

    _MSiSCSI_RequestTimeStatistics._fields_ = [
        # Name of the iSCSI Target
        ('iSCSIName', WCHAR * 223 + 1),
        # The iSCSI connection ID for this connection instance.
        ('CID', USHORT),
        # A uniquely generated session ID used only internally. This is the
        # value returned by the LoginToTarget method.
        ('USID', ULONGLONG),
        # Id that is globally unique to each instance of each adapter. This is
        # the value reported by the MSiSCSI_HBAInformation class.
        ('UniqueAdapterId', ULONGLONG),
        # Maximum time taken to process a request over this connection
        ('MaximumProcessingTime', ULONG),
        # Average time taken to process a request over this connection
        ('AverageProcessingTime', ULONG),
    ]
    MSiSCSI_RequestTimeStatistics_SIZE = (
        FIELD_OFFSET(MSiSCSI_RequestTimeStatistics, 'AverageProcessingTime') +
        MSiSCSI_RequestTimeStatistics_AverageProcessingTime_SIZE
    )
# END IF
