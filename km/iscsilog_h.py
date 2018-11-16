from pyWinAPI import *

# /* Copyright (c) 1991 Microsoft Corporation Module Name: iscsilog.h
# Abstract: Constant definitions for the iSCSI error code log values.

_ISCSILOG_ = None
if not defined(_ISCSILOG_):
    _ISCSILOG_ = 1

    # Status values are 32 bit values layed out as follows:
    # 3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
    # 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
    # + - - - + - + - - - - - - - - - - - - - - - - - - - - - - - - - + - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
    # | Sev | C|  Facility  |   Code   |
    # + - - - + - + - - - - - - - - - - - - - - - - - - - - - - - - - + - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
    # where
    # Sev - is the severity code
    # 00 - Success
    # 01 - Informational
    # 10 - Warning
    # 11 - Error
    # C - is the Customer code flag
    # Facility - is the facility code
    # Code - is the facility's status code
    # Values are 32 bit values laid out as follows:
    # 3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
    # 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
    # + - - - + - + - + - - - - - - - - - - - - - - - - - - - - - - - + - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
    # | Sev | C | R|  Facility  |   Code   |
    # + - - - + - + - + - - - - - - - - - - - - - - - - - - - - - - - + - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
    # where
    # Sev - is the severity code
    # 00 - Success
    # 01 - Informational
    # 10 - Warning
    # 11 - Error
    # C - is the Customer code flag
    # R - is a reserved bit
    # Facility - is the facility code
    # Code - is the facility's status code
    # Define the facility codes
    # Define the severity codes
    STATUS_SEVERITY_SUCCESS = 0x0
    STATUS_SEVERITY_INFORMATIONAL = 0x1
    STATUS_SEVERITY_WARNING = 0x2
    STATUS_SEVERITY_ERROR = 0x3

    # MessageId: ISCSI_ERR_TDI_CONNECT_FAILED
    # MessageText:
    # Initiator failed to connect to the target. Target IP address and TCP
    # Port number are given in dump data.
    ISCSI_ERR_TDI_CONNECT_FAILED = 0xC0000001

    # MessageId: ISCSI_ERR_INSUFFICIENT_SESSION_RESOURCES
    # MessageText:
    # The initiator could not allocate resources for an iSCSI session.
    ISCSI_ERR_INSUFFICIENT_SESSION_RESOURCES = 0xC0000002

    # MessageId: ISCSI_ERR_INVALID_COMMAND_SEQUENCE_NUMBER
    # MessageText:
    # Maximum command sequence number is not serially greater than expected
    # command sequence number in login response.
    # Dump data contains Expected Command Sequence number followed by Maximum
    # Command Sequence number.
    ISCSI_ERR_INVALID_COMMAND_SEQUENCE_NUMBER = 0xC0000003

    # MessageId: ISCSI_ERR_INVALID_BURST_LENGTH
    # MessageText:
    # MaxBurstLength is not serially greater than FirstBurstLength.
    # Dump data contains FirstBurstLength followed by MaxBurstLength.
    ISCSI_ERR_INVALID_BURST_LENGTH = 0xC0000004

    # MessageId: ISCSI_ERR_SETUP_NETWORK_NODE
    # MessageText:
    # Failed to setup initiator portal. Error status is given in the dump data.
    ISCSI_ERR_SETUP_NETWORK_NODE = 0xC0000005

    # MessageId: ISCSI_ERR_INSUFFICIENT_CONNECTION_RESOURCES
    # MessageText:
    # The initiator could not allocate resources for an iSCSI connection
    ISCSI_ERR_INSUFFICIENT_CONNECTION_RESOURCES = 0xC0000006

    # MessageId: ISCSI_ERR_SEND_FAILED
    # MessageText:
    # The initiator could not send an iSCSI PDU. Error status is given in the
    # dump data.
    ISCSI_ERR_SEND_FAILED = 0xC0000007

    # MessageId: ISCSI_ERR_ISCSI_REQUEST_TIMEOUT
    # MessageText:
    # Target or discovery service did not respond in time for an iSCSI request
    # sent by the initiator.
    # iSCSI Function code is given in the dump data. For details about iSCSI
    # Function code please refer
    # to iSCSI User's Guide.
    ISCSI_ERR_ISCSI_REQUEST_TIMEOUT = 0xC0000008

    # MessageId: ISCSI_ERR_SCSI_REQUEST_TIMEOUT
    # MessageText:
    # Target did not respond in time for a SCSI request. The CDB is given in
    # the dump data.
    ISCSI_ERR_SCSI_REQUEST_TIMEOUT = 0xC0000009

    # MessageId: ISCSI_ERR_LOGIN_FAILED
    # MessageText:
    # Login request failed. The login response packet is given in the dump
    # data.
    ISCSI_ERR_LOGIN_FAILED = 0xC000000A

    # MessageId: ISCSI_ERR_LOGIN_PDU_ERROR
    # MessageText:
    # Target returned an invalid login response packet. The login response
    # packet is given in the dump data.
    ISCSI_ERR_LOGIN_PDU_ERROR = 0xC000000B

    # MessageId: ISCSI_ERR_INVALID_LOGIN_REDIRECT_DATA
    # MessageText:
    # Target provided invalid data for login redirect. Dump data contains the
    # data returned by the target.
    ISCSI_ERR_INVALID_LOGIN_REDIRECT_DATA = 0xC000000C

    # MessageId: ISCSI_ERR_INVALID_AUTHMETHOD
    # MessageText:
    # Target offered an unknown AuthMethod. Dump data contains the data
    # returned by the target.
    ISCSI_ERR_INVALID_AUTHMETHOD = 0xC000000D

    # MessageId: ISCSI_ERR_INVALID_CHAP_ALGORITHM
    # MessageText:
    # Target offered an unknown digest algorithm for CHAP. Dump data contains
    # the data returned by the target.
    ISCSI_ERR_INVALID_CHAP_ALGORITHM = 0xC000000E

    # MessageId: ISCSI_ERR_INVALID_CHAP_CHALLENGE
    # MessageText:
    # CHAP challenge given by the target contains invalid characters. Dump
    # data contains the challenge given.
    ISCSI_ERR_INVALID_CHAP_CHALLENGE = 0xC000000F

    # MessageId: ISCSI_ERR_INVALID_KEY_DURING_CHAP
    # MessageText:
    # An invalid key was received during CHAP negotiation. The key=value pair
    # is given in the dump data.
    ISCSI_ERR_INVALID_KEY_DURING_CHAP = 0xC0000010

    # MessageId: ISCSI_ERR_INVALID_CHAP_RESPONSE
    # MessageText:
    # CHAP Response given by the target did not match the expected one. Dump
    # data contains the CHAP response.
    ISCSI_ERR_INVALID_CHAP_RESPONSE = 0xC0000011

    # MessageId: ISCSI_ERR_HEADER_DIGEST_NEEDED
    # MessageText:
    # Header Digest is required by the initiator, but target did not offer it.
    ISCSI_ERR_HEADER_DIGEST_NEEDED = 0xC0000012

    # MessageId: ISCSI_ERR_HEADER_DATA_NEEDED
    # MessageText:
    # Data Digest is required by the initiator, but target did not offer it.
    ISCSI_ERR_HEADER_DATA_NEEDED = 0xC0000013

    # MessageId: ISCSI_ERR_CONNECTION_LOST
    # MessageText:
    # Connection to the target was lost. The initiator will attempt to retry
    # the connection.
    ISCSI_ERR_CONNECTION_LOST = 0xC0000014

    # MessageId: ISCSI_ERR_INVALID_DATA_SEGMENT_LENGTH
    # MessageText:
    # Data Segment Length given in the header exceeds MaxRecvDataSegmentLength
    # declared by the target.
    ISCSI_ERR_INVALID_DATA_SEGMENT_LENGTH = 0xC0000015

    # MessageId: ISCSI_ERR_HEADER_DIGEST_ERROR
    # MessageText:
    # Header digest error was detected for the given PDU. Dump data contains
    # the header and digest.
    ISCSI_ERR_HEADER_DIGEST_ERROR = 0xC0000016

    # MessageId: ISCSI_ERR_ISCSI_PDU_ERROR
    # MessageText:
    # Target sent an invalid iSCSI PDU. Dump data contains the entire iSCSI
    # header.
    ISCSI_ERR_ISCSI_PDU_ERROR = 0xC0000017

    # MessageId: ISCSI_ERR_UNKNOWN_ISCSI_OPCODE
    # MessageText:
    # Target sent an iSCSI PDU with an invalid opcode. Dump data contains the
    # entire iSCSI header.
    ISCSI_ERR_UNKNOWN_ISCSI_OPCODE = 0xC0000018

    # MessageId: ISCSI_ERR_DATA_DIGEST_ERROR
    # MessageText:
    # Data digest error was detected. Dump data contains the calculated
    # checksum followed by the given checksum.
    ISCSI_ERR_DATA_DIGEST_ERROR = 0xC0000019

    # MessageId: ISCSI_ERR_EXCESS_DATA_SENT
    # MessageText:
    # Target trying to send more data than requested by the initiator.
    ISCSI_ERR_EXCESS_DATA_SENT = 0xC000001A

    # MessageId: ISCSI_ERR_UNEXPECTED_PDU
    # MessageText:
    # Initiator could not find a match for the initiator task tag in the
    # received PDU. Dump data contains the entire iSCSI header.
    ISCSI_ERR_UNEXPECTED_PDU = 0xC000001B

    # MessageId: ISCSI_ERR_INVALID_RTT_PDU
    # MessageText:
    # Initiator received an invalid R2T packet. Dump data contains the entire
    # iSCSI header.
    ISCSI_ERR_INVALID_RTT_PDU = 0xC000001C

    # MessageId: ISCSI_ERR_ISCSI_PDU_REJECTED
    # MessageText:
    # Target rejected an iSCSI PDU sent by the initiator. Dump data contains
    # the rejected PDU.
    ISCSI_ERR_ISCSI_PDU_REJECTED = 0xC000001D

    # MessageId: ISCSI_ERR_INSUFFICIENT_WORKITEM_RESOURCES
    # MessageText:
    # Initiator could not allocate a workitem for processing a request.
    ISCSI_ERR_INSUFFICIENT_WORKITEM_RESOURCES = 0xC000001E

    # MessageId: ISCSI_ERR_INSUFFICIENT_REQ_PACKET_RESOURCES
    # MessageText:
    # Initiator could not allocate resource for processing a request.
    ISCSI_ERR_INSUFFICIENT_REQ_PACKET_RESOURCES = 0xC000001F

    # MessageId: ISCSI_INFO_RECEIVED_ASYNC_LOGOUT
    # MessageText:
    # Initiator received an asynchronous logout message. The Target name is
    # given in the dump data.
    ISCSI_INFO_RECEIVED_ASYNC_LOGOUT = 0x40000020

    # MessageId: ISCSI_ERR_INVALID_CHAP_CHALLENGE_SIZE
    # MessageText:
    # Challenge size given by the target exceeds the maximum specified in
    # iSCSI specification.
    ISCSI_ERR_INVALID_CHAP_CHALLENGE_SIZE = 0xC0000021

    # MessageId: ISCSI_INFO_RECONNECTED_TO_TARGET
    # MessageText:
    # A connection to the target was lost, but Initiator successfully
    # reconnected to the target. Dump data contains the target name.
    ISCSI_INFO_RECONNECTED_TO_TARGET = 0x40000022

    # MessageId: ISCSI_ERR_INVALID_TARGET_CHAP_SECRET
    # MessageText:
    # Target CHAP secret is smaller than the minimum size (12 bytes) required
    # by the spec.
    ISCSI_ERR_INVALID_TARGET_CHAP_SECRET = 0xC0000023

    # MessageId: ISCSI_ERR_INVALID_INITIATOR_CHAP_SECRET
    # MessageText:
    # Initiator CHAP secret is smaller than the minimum size (12 bytes)
    # required by the spec. Dump data contains the given CHAP secret.
    ISCSI_ERR_INVALID_INITIATOR_CHAP_SECRET = 0xC0000024

    # MessageId: ISCSI_ERR_FIPS_NOT_AVAILABLE
    # MessageText:
    # FIPS service could not be initialized. Persistent logons will not be
    # processed.
    ISCSI_ERR_FIPS_NOT_AVAILABLE = 0xC0000025

    # MessageId: ISCSI_ERR_CHAP_NOT_OFFERED
    # MessageText:
    # Initiator requires CHAP for logon authentication, but target did not
    # offer CHAP.
    ISCSI_ERR_CHAP_NOT_OFFERED = 0xC0000026

    # MessageId: ISCSI_ERR_DEVICE_RESET
    # MessageText:
    # Initiator sent a task management command to reset the target. The target
    # name is given in the dump data.
    ISCSI_ERR_DEVICE_RESET = 0xC0000027

    # MessageId: ISCSI_ERR_CHAP_OFFERED
    # MessageText:
    # Target requires logon authentication via CHAP, but Initiator is not
    # configured to perform CHAP.
    ISCSI_ERR_CHAP_OFFERED = 0xC0000028

    # MessageId: ISCSI_ERR_AUTH_METHOD_NOT_OFFERED
    # MessageText:
    # Target did not send AuthMethod key during security negotiation phase.
    ISCSI_ERR_AUTH_METHOD_NOT_OFFERED = 0xC0000029

    # MessageId: ISCSI_ERR_INVALID_STATUS_SEQ_NUM
    # MessageText:
    # Target sent an invalid status sequence number for a connection. Dump
    # data contains
    # Expected Status Sequence number followed by the given status sequence
    # number.
    ISCSI_ERR_INVALID_STATUS_SEQ_NUM = 0xC000002A

    # MessageId: ISCSI_ERR_LOGIN_TIMED_OUT
    # MessageText:
    # Target failed to respond in time for a login request.
    ISCSI_ERR_LOGIN_TIMED_OUT = 0xC000002B

    # MessageId: ISCSI_ERR_LOGOUT_TIMED_OUT
    # MessageText:
    # Target failed to respond in time for a logout request.
    ISCSI_ERR_LOGOUT_TIMED_OUT = 0xC000002C

    # MessageId: ISCSI_ERR_ADDCONNECTION_TIMED_OUT
    # MessageText:
    # Target failed to respond in time for a login request. This login request
    # was for adding a new connection to a session.
    ISCSI_ERR_ADDCONNECTION_TIMED_OUT = 0xC000002D

    # MessageId: ISCSI_ERR_SENDTARGETS_TIMED_OUT
    # MessageText:
    # Target failed to respond in time for a SendTargets command.
    ISCSI_ERR_SENDTARGETS_TIMED_OUT = 0xC000002E

    # MessageId: ISCSI_ERR_SCSICOMMAND_TIMED_OUT
    # MessageText:
    # Target failed to respond in time for a SCSI command sent through a WMI
    # request.
    ISCSI_ERR_SCSICOMMAND_TIMED_OUT = 0xC000002F

    # MessageId: ISCSI_ERR_NOP_TIMED_OUT
    # MessageText:
    # Target failed to respond in time to a NOP request.
    ISCSI_ERR_NOP_TIMED_OUT = 0xC0000030

    # MessageId: ISCSI_ERR_TASKMGMT_TIMED_OUT
    # MessageText:
    # Target failed to respond in time to a Task Management request.
    ISCSI_ERR_TASKMGMT_TIMED_OUT = 0xC0000031

    # MessageId: ISCSI_ERR_ASYNC_TEXT_CMD_TIMED_OUT
    # MessageText:
    # Target failed to respond in time to a Text Command sent to renegotiate
    # iSCSI parameters.
    ISCSI_ERR_ASYNC_TEXT_CMD_TIMED_OUT = 0xC0000032

    # MessageId: ISCSI_ERR_ASYNC_LOGOUT_TIMED_OUT
    # MessageText:
    # Target failed to respond in time to a logout request sent in response to
    # an asynchronous message from the target.
    ISCSI_ERR_ASYNC_LOGOUT_TIMED_OUT = 0xC0000033

    # MessageId: ISCSI_ERR_CONFIG_IPSEC_TIMED_OUT
    # MessageText:
    # Initiator Service failed to respond in time to a request to configure
    # IPSec resources for an iSCSI connection.
    ISCSI_ERR_CONFIG_IPSEC_TIMED_OUT = 0xC0000034

    # MessageId: ISCSI_ERR_RELEASE_IPSEC_TIMED_OUT
    # MessageText:
    # Initiator Service failed to respond in time to a request to release
    # IPSec resources allocated for an iSCSI connection.
    ISCSI_ERR_RELEASE_IPSEC_TIMED_OUT = 0xC0000035

    # MessageId: ISCSI_ERR_ENCRYPT_DECRYPT_TIMED_OUT
    # MessageText:
    # Initiator Service failed to respond in time to a request to encrypt or
    # decrypt data.
    ISCSI_ERR_ENCRYPT_DECRYPT_TIMED_OUT = 0xC0000036

    # MessageId: ISCSI_ERR_INSUFFICIENT_RESOURCES_FOR_SEND
    # MessageText:
    # Initiator failed to allocate resources to send data to target.
    ISCSI_ERR_INSUFFICIENT_RESOURCES_FOR_SEND = 0xC0000037

    # MessageId: ISCSI_ERR_FAILED_TO_GET_SYSTEM_ADDRESS
    # MessageText:
    # Initiator could not map an user virtual address to kernel virtual
    # address resulting in I/O failure.
    ISCSI_ERR_FAILED_TO_GET_SYSTEM_ADDRESS = 0xC0000038

    # MessageId: ISCSI_ERR_FAILED_TO_ALLOCATE_RESOURCES_FOR_IO
    # MessageText:
    # Initiator could not allocate required resources for processing a request
    # resulting in I/O failure.
    ISCSI_ERR_FAILED_TO_ALLOCATE_RESOURCES_FOR_IO = 0xC0000039

    # MessageId: ISCSI_ERR_FAILED_TO_ALLOCATE_REQUEST_TAG
    # MessageText:
    # Initiator could not allocate a tag for processing a request resulting in
    # I/O failure.
    ISCSI_ERR_FAILED_TO_ALLOCATE_REQUEST_TAG = 0xC000003A

    # MessageId: ISCSI_ERR_CONNECTION_DROPPED_BEFORE_FFP
    # MessageText:
    # Target dropped the connection before the initiator could transition to
    # Full Feature Phase.
    ISCSI_ERR_CONNECTION_DROPPED_BEFORE_FFP = 0xC000003B

    # MessageId: ISCSI_ERR_DATA_SENT_IN_SCSI_RESPONSE
    # MessageText:
    # Target sent data in SCSI Response PDU instead of Data_IN PDU. Only Sense
    # Data can be sent in SCSI Response.
    ISCSI_ERR_DATA_SENT_IN_SCSI_RESPONSE = 0xC000003C

    # MessageId: ISCSI_ERR_DATA_PDU_IN_ORDER_FALSE
    # MessageText:
    # Target set DataPduInOrder to NO when initiator requested YES. Login will
    # be failed.
    ISCSI_ERR_DATA_PDU_IN_ORDER_FALSE = 0xC000003D

    # MessageId: ISCSI_ERR_DATA_SEQ_IN_ORDER_FALSE
    # MessageText:
    # Target set DataSequenceInOrder to NO when initiator requested YES. Login
    # will be failed.
    ISCSI_ERR_DATA_SEQ_IN_ORDER_FALSE = 0xC000003E

    # MessageId: ISCSI_ERR_TOO_MANY_RESET_FAILURE
    # MessageText:
    # Can not Reset the Target or LUN. Will attempt session recovery.
    ISCSI_ERR_TOO_MANY_RESET_FAILURE = 0xC000003F

    # MessageId: ISCSI_INFO_NIC_BOOT
    # MessageText:
    # Attempt to bootstrap Windows using iSCSI NIC Boot (iBF)
    ISCSI_INFO_NIC_BOOT = 0x40000040

    # MessageId: ISCSI_PAGING_IRP_ERROR
    # MessageText:
    # Booting from iSCSI, but Could not set any NIC in Paging Path.
    ISCSI_PAGING_IRP_ERROR = 0xC0000041

    # MessageId: ISCSI_ERR_DISABLE_NAGLE
    # MessageText:
    # Attempt to disable the Nagle Algorithm for iSCSI connection failed.
    ISCSI_ERR_DISABLE_NAGLE = 0xC0000042

    # MessageId: ISCSI_USING_PROCESSOR_CRC32
    # MessageText:
    # If Digest support selected for iSCSI Session, Will use Processor support
    # for Digest computation.
    ISCSI_USING_PROCESSOR_CRC32 = 0x40000043

    # MessageId: ISCSI_ERR_FAILED_TO_RECOVER_SESSION_AFTER_ASYNCLOGOUT
    # MessageText:
    # After receiving an async logout from the target, attempt to relogin the
    # session failed. Error status is given in the dump data.
    ISCSI_ERR_FAILED_TO_RECOVER_SESSION_AFTER_ASYNCLOGOUT = (
        0xC0000044
    )

    # MessageId: ISCSI_ERR_FAILED_TO_RECOVER_UNEXPECTED_TERMINATED_SESSION
    # MessageText:
    # Attempt to recover an unexpected terminated session failed. Error status
    # is given in the dump data.
    ISCSI_ERR_FAILED_TO_RECOVER_UNEXPECTED_TERMINATED_SESSION = (
        0xC0000045
    )

    # MessageId: ISCSI_ERR_FAILED_TO_PROCESS_LOGON_REQUEST
    # MessageText:
    # Error occurred when processing iSCSI logon request. The request was not
    # retried. Error status is given in the dump data.
    ISCSI_ERR_FAILED_TO_PROCESS_LOGON_REQUEST = 0xC0000046

    # MessageId: ISCSI_SESSION_RECOVERY_REQUEST_NOT_STARTED
    # MessageText:
    # Initiator did not start a session recovery upon receiving the request.
    # Dump data contains the error status.
    ISCSI_SESSION_RECOVERY_REQUEST_NOT_STARTED = 0x40000047

    # MessageId: ISCSI_UNEXPECTED_TARGET_PORTAL_IP_TYPE
    # MessageText:
    # Unexpected target portal IP types. Dump data contains the expected IP
    # type.
    ISCSI_UNEXPECTED_TARGET_PORTAL_IP_TYPE = 0xC0000048
# END IF  _ISCSILOG_
