import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _SendTargets_IN(ctypes.Structure):
    pass


SendTargets_IN = _SendTargets_IN
PSendTargets_IN = POINTER(_SendTargets_IN)


class _SendTargets_OUT(ctypes.Structure):
    pass


SendTargets_OUT = _SendTargets_OUT
PSendTargets_OUT = POINTER(_SendTargets_OUT)


class _LoginToTarget_IN(ctypes.Structure):
    pass


LoginToTarget_IN = _LoginToTarget_IN
PLoginToTarget_IN = POINTER(_LoginToTarget_IN)


class _LoginToTarget_OUT(ctypes.Structure):
    pass


LoginToTarget_OUT = _LoginToTarget_OUT
PLoginToTarget_OUT = POINTER(_LoginToTarget_OUT)


class _LogoutFromTarget_IN(ctypes.Structure):
    pass


LogoutFromTarget_IN = _LogoutFromTarget_IN
PLogoutFromTarget_IN = POINTER(_LogoutFromTarget_IN)


class _LogoutFromTarget_OUT(ctypes.Structure):
    pass


LogoutFromTarget_OUT = _LogoutFromTarget_OUT
PLogoutFromTarget_OUT = POINTER(_LogoutFromTarget_OUT)


class _AddConnectionToSession_IN(ctypes.Structure):
    pass


AddConnectionToSession_IN = _AddConnectionToSession_IN
PAddConnectionToSession_IN = POINTER(_AddConnectionToSession_IN)


class _AddConnectionToSession_OUT(ctypes.Structure):
    pass


AddConnectionToSession_OUT = _AddConnectionToSession_OUT
PAddConnectionToSession_OUT = POINTER(_AddConnectionToSession_OUT)


class _RemovePersistentLogin_IN(ctypes.Structure):
    pass


RemovePersistentLogin_IN = _RemovePersistentLogin_IN
PRemovePersistentLogin_IN = POINTER(_RemovePersistentLogin_IN)


class _RemovePersistentLogin_OUT(ctypes.Structure):
    pass

RemovePersistentLogin_OUT = _RemovePersistentLogin_OUT
PRemovePersistentLogin_OUT = POINTER(_RemovePersistentLogin_OUT)


class _RemoveConnectionFromSession_IN(ctypes.Structure):
    pass


RemoveConnectionFromSession_IN = _RemoveConnectionFromSession_IN
PRemoveConnectionFromSession_IN = POINTER(_RemoveConnectionFromSession_IN)


class _RemoveConnectionFromSession_OUT(ctypes.Structure):
    pass


RemoveConnectionFromSession_OUT = _RemoveConnectionFromSession_OUT
PRemoveConnectionFromSession_OUT = POINTER(_RemoveConnectionFromSession_OUT)


class _ScsiInquiry_IN(ctypes.Structure):
    pass


ScsiInquiry_IN = _ScsiInquiry_IN
PScsiInquiry_IN = POINTER(_ScsiInquiry_IN)


class _ScsiInquiry_OUT(ctypes.Structure):
    pass


ScsiInquiry_OUT = _ScsiInquiry_OUT
PScsiInquiry_OUT = POINTER(_ScsiInquiry_OUT)


class _ScsiReadCapacity_IN(ctypes.Structure):
    pass


ScsiReadCapacity_IN = _ScsiReadCapacity_IN
PScsiReadCapacity_IN = POINTER(_ScsiReadCapacity_IN)


class _ScsiReadCapacity_OUT(ctypes.Structure):
    pass


ScsiReadCapacity_OUT = _ScsiReadCapacity_OUT
PScsiReadCapacity_OUT = POINTER(_ScsiReadCapacity_OUT)


class _ScsiReportLuns_IN(ctypes.Structure):
    pass


ScsiReportLuns_IN = _ScsiReportLuns_IN
PScsiReportLuns_IN = POINTER(_ScsiReportLuns_IN)


class _ScsiReportLuns_OUT(ctypes.Structure):
    pass


ScsiReportLuns_OUT = _ScsiReportLuns_OUT
PScsiReportLuns_OUT = POINTER(_ScsiReportLuns_OUT)


class _SetCHAPSharedSecret_IN(ctypes.Structure):
    pass


SetCHAPSharedSecret_IN = _SetCHAPSharedSecret_IN
PSetCHAPSharedSecret_IN = POINTER(_SetCHAPSharedSecret_IN)


class _SetCHAPSharedSecret_OUT(ctypes.Structure):
    pass


SetCHAPSharedSecret_OUT = _SetCHAPSharedSecret_OUT
PSetCHAPSharedSecret_OUT = POINTER(_SetCHAPSharedSecret_OUT)


class _SetRADIUSSharedSecret_IN(ctypes.Structure):
    pass


SetRADIUSSharedSecret_IN = _SetRADIUSSharedSecret_IN
PSetRADIUSSharedSecret_IN = POINTER(_SetRADIUSSharedSecret_IN)


class _SetRADIUSSharedSecret_OUT(ctypes.Structure):
    pass


SetRADIUSSharedSecret_OUT = _SetRADIUSSharedSecret_OUT
PSetRADIUSSharedSecret_OUT = POINTER(_SetRADIUSSharedSecret_OUT)


class _DeleteInitiatorNodeName_IN(ctypes.Structure):
    pass


DeleteInitiatorNodeName_IN = _DeleteInitiatorNodeName_IN
PDeleteInitiatorNodeName_IN = POINTER(_DeleteInitiatorNodeName_IN)


class _DeleteInitiatorNodeName_OUT(ctypes.Structure):
    pass


DeleteInitiatorNodeName_OUT = _DeleteInitiatorNodeName_OUT
PDeleteInitiatorNodeName_OUT = POINTER(_DeleteInitiatorNodeName_OUT)


class _SetInitiatorNodeName_IN(ctypes.Structure):
    pass


SetInitiatorNodeName_IN = _SetInitiatorNodeName_IN
PSetInitiatorNodeName_IN = POINTER(_SetInitiatorNodeName_IN)


class _SetInitiatorNodeName_OUT(ctypes.Structure):
    pass


SetInitiatorNodeName_OUT = _SetInitiatorNodeName_OUT
PSetInitiatorNodeName_OUT = POINTER(_SetInitiatorNodeName_OUT)


class _AddiSNSServer_IN(ctypes.Structure):
    pass


AddiSNSServer_IN = _AddiSNSServer_IN
PAddiSNSServer_IN = POINTER(_AddiSNSServer_IN)


class _AddiSNSServer_OUT(ctypes.Structure):
    pass


AddiSNSServer_OUT = _AddiSNSServer_OUT
PAddiSNSServer_OUT = POINTER(_AddiSNSServer_OUT)


class _RemoveiSNSServer_IN(ctypes.Structure):
    pass


RemoveiSNSServer_IN = _RemoveiSNSServer_IN
PRemoveiSNSServer_IN = POINTER(_RemoveiSNSServer_IN)


class _RemoveiSNSServer_OUT(ctypes.Structure):
    pass


RemoveiSNSServer_OUT = _RemoveiSNSServer_OUT
PRemoveiSNSServer_OUT = POINTER(_RemoveiSNSServer_OUT)


class _AddRADIUSServer_IN(ctypes.Structure):
    pass


AddRADIUSServer_IN = _AddRADIUSServer_IN
PAddRADIUSServer_IN = POINTER(_AddRADIUSServer_IN)


class _AddRADIUSServer_OUT(ctypes.Structure):
    pass


AddRADIUSServer_OUT = _AddRADIUSServer_OUT
PAddRADIUSServer_OUT = POINTER(_AddRADIUSServer_OUT)


class _RemoveRADIUSServer_IN(ctypes.Structure):
    pass


RemoveRADIUSServer_IN = _RemoveRADIUSServer_IN
PRemoveRADIUSServer_IN = POINTER(_RemoveRADIUSServer_IN)


class _RemoveRADIUSServer_OUT(ctypes.Structure):
    pass


RemoveRADIUSServer_OUT = _RemoveRADIUSServer_OUT
PRemoveRADIUSServer_OUT = POINTER(_RemoveRADIUSServer_OUT)


class _ISCSI_Persistent_Login(ctypes.Structure):
    pass


ISCSI_Persistent_Login = _ISCSI_Persistent_Login
PISCSI_Persistent_Login = POINTER(_ISCSI_Persistent_Login)


class _MSiSCSI_PersistentLogins(ctypes.Structure):
    pass


MSiSCSI_PersistentLogins = _MSiSCSI_PersistentLogins
PMSiSCSI_PersistentLogins = POINTER(_MSiSCSI_PersistentLogins)


class _MSiSCSI_TargetMappings(ctypes.Structure):
    pass


MSiSCSI_TargetMappings = _MSiSCSI_TargetMappings
PMSiSCSI_TargetMappings = POINTER(_MSiSCSI_TargetMappings)


class _MSiSCSI_LUNMappingInformation(ctypes.Structure):
    pass


MSiSCSI_LUNMappingInformation = _MSiSCSI_LUNMappingInformation
PMSiSCSI_LUNMappingInformation = POINTER(_MSiSCSI_LUNMappingInformation)


class _SetPresharedKeyForId_IN(ctypes.Structure):
    pass


SetPresharedKeyForId_IN = _SetPresharedKeyForId_IN
PSetPresharedKeyForId_IN = POINTER(_SetPresharedKeyForId_IN)


class _SetPresharedKeyForId_OUT(ctypes.Structure):
    pass


SetPresharedKeyForId_OUT = _SetPresharedKeyForId_OUT
PSetPresharedKeyForId_OUT = POINTER(_SetPresharedKeyForId_OUT)


class _GetPresharedKeyForId_IN(ctypes.Structure):
    pass


GetPresharedKeyForId_IN = _GetPresharedKeyForId_IN
PGetPresharedKeyForId_IN = POINTER(_GetPresharedKeyForId_IN)


class _GetPresharedKeyForId_OUT(ctypes.Structure):
    pass


GetPresharedKeyForId_OUT = _GetPresharedKeyForId_OUT
PGetPresharedKeyForId_OUT = POINTER(_GetPresharedKeyForId_OUT)


class _SetGroupPresharedKey_IN(ctypes.Structure):
    pass


SetGroupPresharedKey_IN = _SetGroupPresharedKey_IN
PSetGroupPresharedKey_IN = POINTER(_SetGroupPresharedKey_IN)


class _SetGroupPresharedKey_OUT(ctypes.Structure):
    pass


SetGroupPresharedKey_OUT = _SetGroupPresharedKey_OUT
PSetGroupPresharedKey_OUT = POINTER(_SetGroupPresharedKey_OUT)


class _SetTunnelModeOuterAddress_IN(ctypes.Structure):
    pass


SetTunnelModeOuterAddress_IN = _SetTunnelModeOuterAddress_IN
PSetTunnelModeOuterAddress_IN = POINTER(_SetTunnelModeOuterAddress_IN)


class _SetTunnelModeOuterAddress_OUT(ctypes.Structure):
    pass


SetTunnelModeOuterAddress_OUT = _SetTunnelModeOuterAddress_OUT
PSetTunnelModeOuterAddress_OUT = POINTER(_SetTunnelModeOuterAddress_OUT)


class _ClearCache_OUT(ctypes.Structure):
    pass


ClearCache_OUT = _ClearCache_OUT
PClearCache_OUT = POINTER(_ClearCache_OUT)


class _SetGenerationalGuid_IN(ctypes.Structure):
    pass


SetGenerationalGuid_IN = _SetGenerationalGuid_IN
PSetGenerationalGuid_IN = POINTER(_SetGenerationalGuid_IN)


class _SetGenerationalGuid_OUT(ctypes.Structure):
    pass


SetGenerationalGuid_OUT = _SetGenerationalGuid_OUT
PSetGenerationalGuid_OUT = POINTER(_SetGenerationalGuid_OUT)


class _MSiSCSI_BootInformation(ctypes.Structure):
    pass


MSiSCSI_BootInformation = _MSiSCSI_BootInformation
PMSiSCSI_BootInformation = POINTER(_MSiSCSI_BootInformation)


class _MSiSCSI_AdapterEvent(ctypes.Structure):
    pass


MSiSCSI_AdapterEvent = _MSiSCSI_AdapterEvent
PMSiSCSI_AdapterEvent = POINTER(_MSiSCSI_AdapterEvent)

_iscsiop_h_ = None
if not defined(_iscsiop_h_):
    _iscsiop_h_ = 1

    # MSiSCSI_Operations - MSiSCSI_Operations
    # ********************************************************************
    # iscsiop.h
    # Module: iSCSI Discovery api
    # Purpose: Internal header defining interface between user mode discovery
    # api dll and HBA driver miniport.
    # Copyright (c) 2001 Microsoft Corporation
    # ********************************************************************
    from pyWinAPI.km.iscsidef_h import * # NOQA

    # This class is required.
    # The iSCSI initiator service relies upon this
    # class in order to interface with the adapter. Implement one instance
    # per miniport instance (adapter).
    # This class must be registered using PDO instance names with a single
    # instance.
    MSiSCSI_OperationsGuid = [
        0xEA4D82BF,
        0x29DA,
        0x4E12,
        [0x80, 0x0A, 0xE5, 0x43, 0x79, 0x64, 0x46, 0x2C],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_Operations_GUID = DEFINE_GUID(
            0xEA4D82BF,
            0x29DA,
            0x4E12,
            0x80,
            0x0A,
            0xE5,
            0x43,
            0x79,
            0x64,
            0x46,
            0x2C
        )

    # END IF
    # Method id definitions for MSiSCSI_Operations
    # This method is required.
    # SendTargets instructs the adapter to use an existing discovery session
    # with the target portal and issue the SendTargets command to it.
    # SendTargetsText specifies the value for the SendTargets key in
    # the PDU sent to the target.
    SendTargets = 10

    SendTargets_IN_UniqueSessionId_SIZE = ctypes.sizeof(ULONGLONG)
    SendTargets_IN_UniqueSessionId_ID = 1
    SendTargets_IN_SendTargetsText_ID = 2

    _SendTargets_IN._fields_ = [
        # Unique Session ID on which to do send targets. This is the session
        # ID returned from the LoginToTarget method.
        ('UniqueSessionId', ULONGLONG),
        # SendTargets key text
        ('SendTargetsText', WCHAR * 223 + 1),
    ]
    SendTargets_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    SendTargets_OUT_Status_ID = 3
    SendTargets_OUT_ResponseSize_SIZE = ctypes.sizeof(ULONG)
    SendTargets_OUT_ResponseSize_ID = 4
    SendTargets_OUT_Response_ID = 5

    _SendTargets_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
        # Number of bytes in SendTargets response
        ('ResponseSize', ULONG),
        # Response to SendTargets in UTF8 characters. NOTE: This field is a
        # variable length array
        ('Response', UCHAR * 1),
    ]

    # This method is required.
    # LoginTarget instructs the adapter to perform a login to the target
    # portal and esatablish a session with the target.
    # Types of login sessions.
    # Discovery - a discovery session is used exclusively for SendTargets
    # operations.
    # Informational - an informational session is a full featured session
    # but the miniport should not report the devices on
    # the target to the port driver since the devices
    # should not be exposed as local devices to Windows.
    # Instead a subset of SCSI commands can be executed
    # on the devices via other WMI methods. This allows
    # applications to gather information about the devices
    # without causing the corresponding Windows device
    # driver stack to be loaded.
    # Data - a data session is a full featured session and the miniport
    # should report the devices on the target to the port driver.
    # In this way the corresponding driver stack will be loaded and
    # the device will be available to all applications.
    # The session id assigned to a session must remain constant for
    # the lifetime of a session. Reconnections due to async logout or
    # network event should not affect the value of the session id. Also
    # the session must be reported to the MSiSCSI_InitiatorSessionInfo
    # class.
    # Data and informational sessions have specific rules related to
    # how reconnections should be handled. If a session is disconnected due
    # to async logout or a network event then the initiator must periodically
    # retry logging back into the session until the session is either
    # successfully reconnected or the initiator is called to
    # logout of the session. The period between retries is not mandated
    # though it is recommended that 5 seconds be a default value. Another
    # rule is that the miniport should not immediately call the port
    # driver to remove the devices on the target when a session is
    # disconnected due to a network event or async logout. If this were to
    # happen then the devices would disappear and no longer be available to
    # applications. Instead the miniport should maintain the availability
    # of the device by queueing requests and faking success for
    # INQUIRY and REPORT LUNS commands. It would need to do this for a
    # period of time (60 seconds is recommended). If the session is
    # reconnected before the end of that period then an application will
    # suffer no interruption in its work. If times runs out the miniport
    # should report the removal of the devices on the target to the port
    # driver. Note that a longer time might mean more requests being queued
    # and more system resources used. It is recommended that these value
    # be configurable.
    class LOGINSESSIONTYPE(ENUM):
        ISCSI_LOGINTARGET_DISCOVERY = 0
        ISCSI_LOGINTARGET_INFORMATIONAL = 1
        ISCSI_LOGINTARGET_DATA = 2

    PLOGINSESSIONTYPE = POINTER(LOGINSESSIONTYPE)
    ISCSI_LOGINTARGET_DISCOVERY = LOGINSESSIONTYPE.ISCSI_LOGINTARGET_DISCOVERY
    ISCSI_LOGINTARGET_INFORMATIONAL = LOGINSESSIONTYPE.ISCSI_LOGINTARGET_INFORMATIONAL
    ISCSI_LOGINTARGET_DATA = LOGINSESSIONTYPE.ISCSI_LOGINTARGET_DATA
    LoginToTarget = 30

    LoginToTarget_IN_PortNumber_SIZE = ctypes.sizeof(ULONG)
    LoginToTarget_IN_PortNumber_ID = 1
    LoginToTarget_IN_LoginOptions_SIZE = ctypes.sizeof(ISCSI_LoginOptions)
    LoginToTarget_IN_LoginOptions_ID = 2
    LoginToTarget_IN_SessionType_SIZE = ctypes.sizeof(ULONG)
    LoginToTarget_IN_SessionType_ID = 3
    LoginToTarget_IN_SecurityFlags_SIZE = ctypes.sizeof(ULONGLONG)
    LoginToTarget_IN_SecurityFlags_ID = 4
    LoginToTarget_IN_TargetPortal_SIZE = ctypes.sizeof(ISCSI_TargetPortal)
    LoginToTarget_IN_TargetPortal_ID = 5
    LoginToTarget_IN_UsernameSize_SIZE = ctypes.sizeof(ULONG)
    LoginToTarget_IN_UsernameSize_ID = 6
    LoginToTarget_IN_PasswordSize_SIZE = ctypes.sizeof(ULONG)
    LoginToTarget_IN_PasswordSize_ID = 7
    LoginToTarget_IN_KeySize_SIZE = ctypes.sizeof(ULONG)
    LoginToTarget_IN_KeySize_ID = 8
    LoginToTarget_IN_UniqueIdForISID_SIZE = ctypes.sizeof(USHORT)
    LoginToTarget_IN_UniqueIdForISID_ID = 9
    LoginToTarget_IN_PersistentLogin_SIZE = ctypes.sizeof(BOOLEAN)
    LoginToTarget_IN_PersistentLogin_ID = 10
    LoginToTarget_IN_InitiatorNode_ID = 11
    LoginToTarget_IN_InitiatorAlias_ID = 12
    LoginToTarget_IN_TargetName_ID = 13
    LoginToTarget_IN_Mappings_SIZE = ctypes.sizeof(ISCSI_TargetMapping)
    LoginToTarget_IN_Mappings_ID = 14
    LoginToTarget_IN_Key_ID = 15
    LoginToTarget_IN_Username_ID = 16
    LoginToTarget_IN_Password_ID = 17

    _LoginToTarget_IN._fields_ = [
        # Port number corresponding to port in which to initiate the session
        ('PortNumber', ULONG),
        # Options that affect how login is performed. See ISCSI_LoginOptions
        ('LoginOptions', ISCSI_LoginOptions),
        # **typedef**Specifies the session type - either discovery,
        # informational or data
        ('SessionType', ULONG),
        # Security flags
        ('SecurityFlags', ULONGLONG),
        # On target portal to use for initial connection.
        ('TargetPortal', ISCSI_TargetPortal),
        # Size in bytes of authentication Username
        ('UsernameSize', ULONG),
        # Size in bytes of authentication Password
        ('PasswordSize', ULONG),
        # Size in bytes of preshared key associated with target ip address
        ('KeySize', ULONG),
        # The service will pass an id that is guaranteed to be gloally unique
        # over all initiators for use when connecting to this target. It may
        # be useful as part of the the ISID
        ('UniqueIdForISID', USHORT),
        # If TRUE then this login should be persisted in non - volatile
        # memory. The adapter will then automatically login to the target
        # using the information passed each time the device driver loads. The
        # driver should not attempt to login, just save the information for
        # login later.
        ('PersistentLogin', BOOLEAN),
        # The InitiatorNode specifies the iSCSI name of the initiator node to
        # use for the connection. If empty, then the HBA can choose any
        # initiator node
        ('InitiatorNode', WCHAR * 223 + 1),
        # The InitiatorAlias specifies the iSCSI alias of the initiator node
        # to use for the connection.
        ('InitiatorAlias', WCHAR * 255 + 1),
        # TargetName specifies the iSCSI target name to which a session should
        # be established.
        ('TargetName', WCHAR * 223 + 1),
        # Target mappings. If no mappings are specified then the initiator can
        # use any mappings for the LUNs. If mappings are specified then any
        # LUN on the target that is not specified in the mappings should not
        # be exposed to the port driver.
        ('Mappings', ISCSI_TargetMapping),
        # **field**Preshared key associated with target ip address. NOTE: This
        # field is a variable length array, the field that follows this field
        # starts immediately after the end of this field subject to
        # appropriate padding. All fields after this are commented out in the
        # header.
        ('Key', UCHAR * 1),
    ]
    LoginToTarget_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    LoginToTarget_OUT_Status_ID = 18
    LoginToTarget_OUT_UniqueSessionId_SIZE = ctypes.sizeof(ULONGLONG)
    LoginToTarget_OUT_UniqueSessionId_ID = 19
    LoginToTarget_OUT_UniqueConnectionId_SIZE = ctypes.sizeof(ULONGLONG)
    LoginToTarget_OUT_UniqueConnectionId_ID = 20

    _LoginToTarget_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
        # Unique Session ID. This ID is used to identify this session in
        # subsqeuent method calls. The unique session ID can never change
        # until the session is logged out.
        ('UniqueSessionId', ULONGLONG),
        # Unique Connection ID
        ('UniqueConnectionId', ULONGLONG),
    ]
    LoginToTarget_OUT_SIZE = (
        FIELD_OFFSET(LoginToTarget_OUT, 'UniqueConnectionId') +
        LoginToTarget_OUT_UniqueConnectionId_SIZE
    )

    # This method is required.
    # This method causes a logout from the target and removal of all LUNs
    # exposed on that target. If the session is not connected to the target
    # then the driver should stop trying to reconnect.
    LogoutFromTarget = 31

    LogoutFromTarget_IN_UniqueSessionId_SIZE = ctypes.sizeof(ULONGLONG)
    LogoutFromTarget_IN_UniqueSessionId_ID = 1

    _LogoutFromTarget_IN._fields_ = [
        # Unique Session ID. This is the session ID that was returned by the
        # driver when the target was logged in.
        ('UniqueSessionId', ULONGLONG),
    ]
    LogoutFromTarget_IN_SIZE = (
        FIELD_OFFSET(LogoutFromTarget_IN, 'UniqueSessionId') +
        LogoutFromTarget_IN_UniqueSessionId_SIZE
    )

    LogoutFromTarget_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    LogoutFromTarget_OUT_Status_ID = 2

    _LogoutFromTarget_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    LogoutFromTarget_OUT_SIZE = (
        FIELD_OFFSET(LogoutFromTarget_OUT, 'Status') +
        LogoutFromTarget_OUT_Status_SIZE
    )

    # This method is required to exist, but the functionality may not be
    # implemented.
    # If the functionality is not implemented the driver should return an error
    # This method causes an additional connection to be established to a target
    # over a session
    AddConnectionToSession = 32

    AddConnectionToSession_IN_UniqueAdapterId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    AddConnectionToSession_IN_UniqueAdapterId_ID = 1
    AddConnectionToSession_IN_UniqueSessionId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    AddConnectionToSession_IN_UniqueSessionId_ID = 2
    AddConnectionToSession_IN_SecurityFlags_SIZE = ctypes.sizeof(ULONGLONG)
    AddConnectionToSession_IN_SecurityFlags_ID = 3
    AddConnectionToSession_IN_PortNumber_SIZE = ctypes.sizeof(ULONG)
    AddConnectionToSession_IN_PortNumber_ID = 4
    AddConnectionToSession_IN_LoginOptions_SIZE = (
        ctypes.sizeof(ISCSI_LoginOptions)
    )
    AddConnectionToSession_IN_LoginOptions_ID = 5
    AddConnectionToSession_IN_TargetPortal_SIZE = (
        ctypes.sizeof(ISCSI_TargetPortal)
    )
    AddConnectionToSession_IN_TargetPortal_ID = 6
    AddConnectionToSession_IN_UsernameSize_SIZE = ctypes.sizeof(ULONG)
    AddConnectionToSession_IN_UsernameSize_ID = 7
    AddConnectionToSession_IN_PasswordSize_SIZE = ctypes.sizeof(ULONG)
    AddConnectionToSession_IN_PasswordSize_ID = 8
    AddConnectionToSession_IN_KeySize_SIZE = ctypes.sizeof(ULONG)
    AddConnectionToSession_IN_KeySize_ID = 9
    AddConnectionToSession_IN_Key_ID = 10
    AddConnectionToSession_IN_Username_ID = 11
    AddConnectionToSession_IN_Password_ID = 12

    _AddConnectionToSession_IN._fields_ = [
        # Unique Adapter specific ID. This is the UniqueAdapterId returned by
        # the MSiSCSI_HBAInfo class.
        ('UniqueAdapterId', ULONGLONG),
        # Unique Session ID. This is the unique session id returned when the
        # target was logged in.
        ('UniqueSessionId', ULONGLONG),
        # Security flags
        ('SecurityFlags', ULONGLONG),
        # Port number corresponding to port from which to initiate the
        # connection
        ('PortNumber', ULONG),
        # Options that affect how login is performed. See ISCSI_LoginOptions
        ('LoginOptions', ISCSI_LoginOptions),
        # Target portal to use for additional connection.
        ('TargetPortal', ISCSI_TargetPortal),
        # Size in bytes of authentication Username.
        ('UsernameSize', ULONG),
        # Size in bytes of authentication Password.
        ('PasswordSize', ULONG),
        # Size in bytes of preshared key associated with target ip address.
        ('KeySize', ULONG),
        # **fields** Preshared key associated with target ip address. NOTE:
        # This field is a variable length array, the field that follows this
        # field starts immediately after the end of this field subject to
        # appropriate padding. All fields after this are commented out in the
        # header.
        ('Key', UCHAR * 1),
    ]
    AddConnectionToSession_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    AddConnectionToSession_OUT_Status_ID = 13
    AddConnectionToSession_OUT_UniqueConnectionId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    AddConnectionToSession_OUT_UniqueConnectionId_ID = 14

    _AddConnectionToSession_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
        # Unique Connection ID
        ('UniqueConnectionId', ULONGLONG),
    ]
    AddConnectionToSession_OUT_SIZE = (
        FIELD_OFFSET(AddConnectionToSession_OUT, 'UniqueConnectionId') +
        AddConnectionToSession_OUT_UniqueConnectionId_SIZE
    )

    # This method is required.
    # This method will remove a target from the list of persistent logins
    # maintained by the adapter.
    RemovePersistentLogin = 33

    RemovePersistentLogin_IN_PortNumber_SIZE = ctypes.sizeof(ULONG)
    RemovePersistentLogin_IN_PortNumber_ID = 1
    RemovePersistentLogin_IN_TargetName_ID = 2
    RemovePersistentLogin_IN_TargetPortal_SIZE = (
        ctypes.sizeof(ISCSI_TargetPortal)
    )
    RemovePersistentLogin_IN_TargetPortal_ID = 3

    _RemovePersistentLogin_IN._fields_ = [
        # Port number corresponding to port from which to initiate the session
        ('PortNumber', ULONG),
        # TargetName specifies the iSCSI target name which should be removed.
        ('TargetName', WCHAR * 223 + 1),
        # Target portal. If an empty target portal is specified then all
        # persistent logins to this target name for all portals are removed.
        ('TargetPortal', ISCSI_TargetPortal),
    ]
    RemovePersistentLogin_IN_SIZE = (
        FIELD_OFFSET(RemovePersistentLogin_IN, 'TargetPortal') +
        RemovePersistentLogin_IN_TargetPortal_SIZE
    )

    RemovePersistentLogin_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    RemovePersistentLogin_OUT_Status_ID = 4

    _RemovePersistentLogin_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    RemovePersistentLogin_OUT_SIZE = (
        FIELD_OFFSET(RemovePersistentLogin_OUT, 'Status') +
        RemovePersistentLogin_OUT_Status_SIZE
    )

    # This method is required.
    # This method will remove a connection from a session.
    # Note that it is specifically disallowed to remove the last
    # connection from a session, use LogoutIScsiTarget instead
    RemoveConnectionFromSession = 34

    RemoveConnectionFromSession_IN_UniqueSessionId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    RemoveConnectionFromSession_IN_UniqueSessionId_ID = 1
    RemoveConnectionFromSession_IN_UniqueConnectionId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    RemoveConnectionFromSession_IN_UniqueConnectionId_ID = 2

    _RemoveConnectionFromSession_IN._fields_ = [
        # Unique Session ID
        ('UniqueSessionId', ULONGLONG),
        # Unique Connection ID
        ('UniqueConnectionId', ULONGLONG),
    ]
    RemoveConnectionFromSession_IN_SIZE = (
        FIELD_OFFSET(RemoveConnectionFromSession_IN, 'UniqueConnectionId') +
        RemoveConnectionFromSession_IN_UniqueConnectionId_SIZE
    )

    RemoveConnectionFromSession_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    RemoveConnectionFromSession_OUT_Status_ID = 3

    _RemoveConnectionFromSession_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    RemoveConnectionFromSession_OUT_SIZE = (
        FIELD_OFFSET(RemoveConnectionFromSession_OUT, 'Status') +
        RemoveConnectionFromSession_OUT_Status_SIZE
    )

    # This method is required.
    # This method causes a SCSI INQUIRY CDB to be sent to a target. The method
    # should return success if the SCSI request succeeded. If the SCSI request
    # failed the Status returned should be ISDSC_SCSI_REQUEST_FAILED and the
    # ScsiStatus and SenseBuffer fields returned.
    ScsiInquiry = 50

    ScsiInquiry_IN_UniqueSessionId_SIZE = ctypes.sizeof(ULONGLONG)
    ScsiInquiry_IN_UniqueSessionId_ID = 1
    ScsiInquiry_IN_Lun_SIZE = ctypes.sizeof(ULONGLONG)
    ScsiInquiry_IN_Lun_ID = 2
    ScsiInquiry_IN_InquiryFlags_SIZE = ctypes.sizeof(UCHAR)
    ScsiInquiry_IN_InquiryFlags_ID = 3
    ScsiInquiry_IN_PageCode_SIZE = ctypes.sizeof(UCHAR)
    ScsiInquiry_IN_PageCode_ID = 4

    _ScsiInquiry_IN._fields_ = [
        # Unique Session ID
        ('UniqueSessionId', ULONGLONG),
        # Logical unit to which to send INQUIRY
        ('Lun', ULONGLONG),
        # Flags to use for inquiry
        ('InquiryFlags', UCHAR),
        # Page code
        ('PageCode', UCHAR),
    ]
    ScsiInquiry_IN_SIZE = (
        FIELD_OFFSET(ScsiInquiry_IN, 'PageCode') +
        ScsiInquiry_IN_PageCode_SIZE
    )

    ScsiInquiry_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    ScsiInquiry_OUT_Status_ID = 5
    ScsiInquiry_OUT_ResponseBufferSize_SIZE = ctypes.sizeof(ULONG)
    ScsiInquiry_OUT_ResponseBufferSize_ID = 6
    ScsiInquiry_OUT_ScsiStatus_SIZE = ctypes.sizeof(UCHAR)
    ScsiInquiry_OUT_ScsiStatus_ID = 7
    ScsiInquiry_OUT_SenseBuffer_SIZE = ctypes.sizeof(UCHAR[18])
    ScsiInquiry_OUT_SenseBuffer_ID = 8
    ScsiInquiry_OUT_ResponseBuffer_ID = 9

    _ScsiInquiry_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
        # Size of the response buffer in bytes
        ('ResponseBufferSize', ULONG),
        # SCSI Status result
        ('ScsiStatus', UCHAR),
        # Sense buffer returned if SCSI error occured
        ('SenseBuffer', UCHAR * 18),
        # Response to the SCSI CDB. NOTE: This field is a variable length
        # array.
        ('ResponseBuffer', UCHAR * 1),
    ]

    # This method is required.
    # This method causes a READ CAPACITY CDB to be sent to a target. The method
    # should return success if the SCSI request succeeded. If the SCSI request
    # failed the Status returned should be ISDSC_SCSI_REQUEST_FAILED and the
    # ScsiStatus and SenseBuffer fields returned.
    ScsiReadCapacity = 51

    ScsiReadCapacity_IN_UniqueSessionId_SIZE = ctypes.sizeof(ULONGLONG)
    ScsiReadCapacity_IN_UniqueSessionId_ID = 1
    ScsiReadCapacity_IN_Lun_SIZE = ctypes.sizeof(ULONGLONG)
    ScsiReadCapacity_IN_Lun_ID = 2

    _ScsiReadCapacity_IN._fields_ = [
        # Unique Session ID
        ('UniqueSessionId', ULONGLONG),
        # Logical unit to which to send READ CAPACITY
        ('Lun', ULONGLONG),
    ]
    ScsiReadCapacity_IN_SIZE = (
        FIELD_OFFSET(ScsiReadCapacity_IN, 'Lun') +
        ScsiReadCapacity_IN_Lun_SIZE
    )

    ScsiReadCapacity_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    ScsiReadCapacity_OUT_Status_ID = 3
    ScsiReadCapacity_OUT_ResponseBufferSize_SIZE = ctypes.sizeof(ULONG)
    ScsiReadCapacity_OUT_ResponseBufferSize_ID = 4
    ScsiReadCapacity_OUT_ScsiStatus_SIZE = ctypes.sizeof(UCHAR)
    ScsiReadCapacity_OUT_ScsiStatus_ID = 5
    ScsiReadCapacity_OUT_SenseBuffer_SIZE = ctypes.sizeof(UCHAR[18])
    ScsiReadCapacity_OUT_SenseBuffer_ID = 6
    ScsiReadCapacity_OUT_ResponseBuffer_ID = 7

    _ScsiReadCapacity_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
        # Size of the response buffer in bytes
        ('ResponseBufferSize', ULONG),
        # SCSI Status result
        ('ScsiStatus', UCHAR),
        # Sense buffer returned on SCSI error
        ('SenseBuffer', UCHAR * 18),
        # Response to the SCSI CDB. NOTE: This field is a variable length
        # array.
        ('ResponseBuffer', UCHAR * 1),
    ]

    # This method is required.
    # This method causes a REPORT LUNS CDB to be sent to a target. The method
    # should return success if the SCSI request succeeded. If the SCSI request
    # failed the Status returned should be ISDSC_SCSI_REQUEST_FAILED and the
    # ScsiStatus and SenseBuffer fields returned.
    ScsiReportLuns = 52

    ScsiReportLuns_IN_UniqueSessionId_SIZE = ctypes.sizeof(ULONGLONG)
    ScsiReportLuns_IN_UniqueSessionId_ID = 1

    _ScsiReportLuns_IN._fields_ = [
        # Unique Session ID
        ('UniqueSessionId', ULONGLONG),
    ]
    ScsiReportLuns_IN_SIZE = (
        FIELD_OFFSET(ScsiReportLuns_IN, 'UniqueSessionId') +
        ScsiReportLuns_IN_UniqueSessionId_SIZE
    )

    ScsiReportLuns_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    ScsiReportLuns_OUT_Status_ID = 2
    ScsiReportLuns_OUT_ResponseBufferSize_SIZE = ctypes.sizeof(ULONG)
    ScsiReportLuns_OUT_ResponseBufferSize_ID = 3
    ScsiReportLuns_OUT_ScsiStatus_SIZE = ctypes.sizeof(UCHAR)
    ScsiReportLuns_OUT_ScsiStatus_ID = 4
    ScsiReportLuns_OUT_SenseBuffer_SIZE = ctypes.sizeof(UCHAR[18])
    ScsiReportLuns_OUT_SenseBuffer_ID = 5
    ScsiReportLuns_OUT_ResponseBuffer_ID = 6

    _ScsiReportLuns_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
        # Size of the response buffer in bytes
        ('ResponseBufferSize', ULONG),
        # SCSI Status result
        ('ScsiStatus', UCHAR),
        # Sense buffer returned on SCSI error
        ('SenseBuffer', UCHAR * 18),
        # Response to the SCSI CDB. NOTE: This field is a variable length
        # array.
        ('ResponseBuffer', UCHAR * 1),
    ]

    # This method is required.
    # This method establishes a CHAP shared secret that is assigned to
    # this initiator and should be used when verifying the CHAP response
    # to a challange sent by the initiator. Note that the shared secret
    # that is used to generate the CHAP response to a target's challange
    # is passed in the LoginToTarget method
    SetCHAPSharedSecret = 71

    SetCHAPSharedSecret_IN_SharedSecretSize_SIZE = ctypes.sizeof(ULONG)
    SetCHAPSharedSecret_IN_SharedSecretSize_ID = 1
    SetCHAPSharedSecret_IN_SharedSecret_ID = 2

    _SetCHAPSharedSecret_IN._fields_ = [
        # Size of Chap shared secret in bytes
        ('SharedSecretSize', ULONG),
        # CHAP shared secret. NOTE: This field is a variable length array.
        ('SharedSecret', UCHAR * 1),
    ]
    SetCHAPSharedSecret_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    SetCHAPSharedSecret_OUT_Status_ID = 3

    _SetCHAPSharedSecret_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    SetCHAPSharedSecret_OUT_SIZE = (
        FIELD_OFFSET(SetCHAPSharedSecret_OUT, 'Status') +
        SetCHAPSharedSecret_OUT_Status_SIZE
    )

    # This method is required.
    # This method establishes a RADIUS shared secret that is assigned to
    # this initiator and should be used when authenticating oneself
    # to the RADIUS server.
    SetRADIUSSharedSecret = 72

    SetRADIUSSharedSecret_IN_SharedSecretSize_SIZE = ctypes.sizeof(ULONG)
    SetRADIUSSharedSecret_IN_SharedSecretSize_ID = 1
    SetRADIUSSharedSecret_IN_SharedSecret_ID = 2

    _SetRADIUSSharedSecret_IN._fields_ = [
        # Size of RADIUS shared secret in bytes
        ('SharedSecretSize', ULONG),
        # RADIUS shared secret. NOTE: This field is a variable length array.
        ('SharedSecret', UCHAR * 1),
    ]
    SetRADIUSSharedSecret_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    SetRADIUSSharedSecret_OUT_Status_ID = 3

    _SetRADIUSSharedSecret_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    SetRADIUSSharedSecret_OUT_SIZE = (
        FIELD_OFFSET(SetRADIUSSharedSecret_OUT, 'Status') +
        SetRADIUSSharedSecret_OUT_Status_SIZE
    )

    # This method is optional and does not need to be implemented.
    # This method informs the initiator that an initiator node name is no
    # longer in use.
    DeleteInitiatorNodeName = 91

    DeleteInitiatorNodeName_IN_DeletedInitiatorName_ID = 1

    _DeleteInitiatorNodeName_IN._fields_ = [
        # Initiator name that is deleted.
        ('DeletedInitiatorName', WCHAR * 223 + 1),
    ]
    DeleteInitiatorNodeName_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    DeleteInitiatorNodeName_OUT_Status_ID = 2

    _DeleteInitiatorNodeName_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    DeleteInitiatorNodeName_OUT_SIZE = (
        FIELD_OFFSET(DeleteInitiatorNodeName_OUT, 'Status') +
        DeleteInitiatorNodeName_OUT_Status_SIZE
    )


    # This method is optional and does not need to be implemented.
    # This method informs the initiator that a new initiator node name is
    # begin to be in use//
    SetInitiatorNodeName = 92

    SetInitiatorNodeName_IN_CreatedInitiatorName_ID = 1

    _SetInitiatorNodeName_IN._fields_ = [
        # New initiator name.
        ('CreatedInitiatorName', WCHAR * 223 + 1),
    ]
    SetInitiatorNodeName_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    SetInitiatorNodeName_OUT_Status_ID = 2

    _SetInitiatorNodeName_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    SetInitiatorNodeName_OUT_SIZE = (
        FIELD_OFFSET(SetInitiatorNodeName_OUT, 'Status') +
        SetInitiatorNodeName_OUT_Status_SIZE
    )

    # This method is optional and does not need to be implemented.
    # This method adds an iSNS server to the list of iSNS servers the HBA
    # should manage
    AddiSNSServer = 101

    AddiSNSServer_IN_iSNSServerName_ID = 1

    _AddiSNSServer_IN._fields_ = [
        # iSNS Server Name
        ('iSNSServerName', WCHAR * 223 + 1),
    ]
    AddiSNSServer_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    AddiSNSServer_OUT_Status_ID = 2

    _AddiSNSServer_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    AddiSNSServer_OUT_SIZE = (
        FIELD_OFFSET(AddiSNSServer_OUT, 'Status') +
        AddiSNSServer_OUT_Status_SIZE
    )

    # This method is optional and does not need to be implemented.
    # This method removes an iSNS server from the list of iSNS servers the HBA
    # should manage
    RemoveiSNSServer = 102

    RemoveiSNSServer_IN_iSNSServerName_ID = 1

    _RemoveiSNSServer_IN._fields_ = [
        # iSNS Server Name
        ('iSNSServerName', WCHAR * 223 + 1),
    ]
    RemoveiSNSServer_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    RemoveiSNSServer_OUT_Status_ID = 2

    _RemoveiSNSServer_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    RemoveiSNSServer_OUT_SIZE = (
        FIELD_OFFSET(RemoveiSNSServer_OUT, 'Status') +
        RemoveiSNSServer_OUT_Status_SIZE
    )


    # This method is optional and does not need to be implemented.
    # This method adds a RADIUS server to the list of RADIUS servers the
    # initiator/HBA
    # should manage
    AddRADIUSServer = 103

    AddRADIUSServer_IN_RADIUSIPAddress_SIZE = (
        ctypes.sizeof(ISCSI_IP_Address)
    )
    AddRADIUSServer_IN_RADIUSIPAddress_ID = 1

    _AddRADIUSServer_IN._fields_ = [
        # RADIUS Server Address
        ('RADIUSIPAddress', ISCSI_IP_Address),
    ]
    AddRADIUSServer_IN_SIZE = (
        FIELD_OFFSET(AddRADIUSServer_IN, 'RADIUSIPAddress') +
        AddRADIUSServer_IN_RADIUSIPAddress_SIZE
    )

    AddRADIUSServer_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    AddRADIUSServer_OUT_Status_ID = 2

    _AddRADIUSServer_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    AddRADIUSServer_OUT_SIZE = (
        FIELD_OFFSET(AddRADIUSServer_OUT, 'Status') +
        AddRADIUSServer_OUT_Status_SIZE
    )

    # This method is optional and does not need to be implemented.
    # This method removes a RADIUS server from the list of RADIUS servers the
    # initiator/HBA
    # should manage
    RemoveRADIUSServer = 104

    RemoveRADIUSServer_IN_RADIUSIPAddress_SIZE = (
        ctypes.sizeof(ISCSI_IP_Address)
    )
    RemoveRADIUSServer_IN_RADIUSIPAddress_ID = 1

    _RemoveRADIUSServer_IN._fields_ = [
        # RADIUS Server Address
        ('RADIUSIPAddress', ISCSI_IP_Address),
    ]
    RemoveRADIUSServer_IN_SIZE = (
        FIELD_OFFSET(RemoveRADIUSServer_IN, 'RADIUSIPAddress') +
        RemoveRADIUSServer_IN_RADIUSIPAddress_SIZE
    )

    RemoveRADIUSServer_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    RemoveRADIUSServer_OUT_Status_ID = 2

    _RemoveRADIUSServer_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    RemoveRADIUSServer_OUT_SIZE = (
        FIELD_OFFSET(RemoveRADIUSServer_OUT, 'Status') +
        RemoveRADIUSServer_OUT_Status_SIZE
    )

    # ISCSI_Persistent_Login - ISCSI_Persistent_Login
    # Persistent Target login
    ISCSI_Persistent_LoginGuid = [
        0x1AC62A5D,
        0xA418,
        0x4C15,
        [0x96, 0xBD, 0x2C, 0x3A, 0x9D, 0xB8, 0xC8, 0xCA],
    ]
    if not defined(MIDL_PASS):
        ISCSI_Persistent_Login_GUID = DEFINE_GUID(
            0x1AC62A5D,
            0xA418,
            0x4C15,
            0x96,
            0xBD,
            0x2C,
            0x3A,
            0x9D,
            0xB8,
            0xC8,
            0xCA
        )

    # END IF
    ISCSI_Persistent_Login_TargetName_ID = 1
    ISCSI_Persistent_Login_SecurityFlags_SIZE = ctypes.sizeof(ULONGLONG)
    ISCSI_Persistent_Login_SecurityFlags_ID = 2
    ISCSI_Persistent_Login_InitiatorPortNumber_SIZE = ctypes.sizeof(ULONG)
    ISCSI_Persistent_Login_InitiatorPortNumber_ID = 3
    ISCSI_Persistent_Login_UsernameSize_SIZE = ctypes.sizeof(ULONG)
    ISCSI_Persistent_Login_UsernameSize_ID = 4
    ISCSI_Persistent_Login_IsInformationalSession_SIZE = (
        ctypes.sizeof(BOOLEAN)
    )
    ISCSI_Persistent_Login_IsInformationalSession_ID = 5
    ISCSI_Persistent_Login_UniqueIdForISID_SIZE = ctypes.sizeof(USHORT)
    ISCSI_Persistent_Login_UniqueIdForISID_ID = 6
    ISCSI_Persistent_Login_TargetPortal_SIZE = (
        ctypes.sizeof(ISCSI_TargetPortal)
    )
    ISCSI_Persistent_Login_TargetPortal_ID = 7
    ISCSI_Persistent_Login_LoginOptions_SIZE = (
        ctypes.sizeof(ISCSI_LoginOptions)
    )
    ISCSI_Persistent_Login_LoginOptions_ID = 8
    ISCSI_Persistent_Login_TargetMapping_SIZE = (
        ctypes.sizeof(ISCSI_TargetMapping)
    )
    ISCSI_Persistent_Login_TargetMapping_ID = 9
    ISCSI_Persistent_Login_Username_ID = 10

    _ISCSI_Persistent_Login._fields_ = [
        # Name of the target for persistent login
        ('TargetName', WCHAR * 223 + 1),
        # Security flags
        ('SecurityFlags', ULONGLONG),
        # Port number on which to perform the login
        ('InitiatorPortNumber', ULONG),
        # Number of bytes in username
        ('UsernameSize', ULONG),
        # TRUE if informational session
        ('IsInformationalSession', BOOLEAN),
        # ISID that the persistent login will use for login
        ('UniqueIdForISID', USHORT),
        # Portal to use for initial connection
        ('TargetPortal', ISCSI_TargetPortal),
        # Login options
        ('LoginOptions', ISCSI_LoginOptions),
        # Target mappings
        ('TargetMapping', ISCSI_TargetMapping),
        # Authentication Username, for CHAP this is the CHAP Name (CHAP_N)
        # when authenticating the target. NOTE: This field is a variable
        # length array.
        ('Username', UCHAR * 1),
    ]

    # MSiSCSI_PersistentLogins - MSiSCSI_PersistentLogins
    # This class is required.
    # This class returns the list of persistent target logins. A persistent
    # target login is one where the initiator must login to the
    # target immediately upon loading so that the device is available
    # early in boot
    MSiSCSI_PersistentLoginsGuid = [
        0x420512D9,
        0x0537,
        0x4C67,
        [0xA7, 0x79, 0x84, 0xBA, 0x7B, 0x29, 0xCE, 0x9F],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_PersistentLogins_GUID = DEFINE_GUID(
            0x420512D9,
            0x0537,
            0x4C67,
            0xA7,
            0x79,
            0x84,
            0xBA,
            0x7B,
            0x29,
            0xCE,
            0x9F
        )

    # END IF
    MSiSCSI_PersistentLogins_PersistentLoginCount_SIZE = (
        ctypes.sizeof(ULONG)
    )
    MSiSCSI_PersistentLogins_PersistentLoginCount_ID = 1
    MSiSCSI_PersistentLogins_Reserved_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_PersistentLogins_Reserved_ID = 2
    MSiSCSI_PersistentLogins_PersistentLogins_ID = 3

    _MSiSCSI_PersistentLogins._fields_ = [
        # Number of persistent logins
        ('PersistentLoginCount', ULONG),
        # Reserved
        ('Reserved', ULONG),
        # Array of PersistentLoginCount ISCSI_Persistent_Login structures.
        # NOTE: This field is a variable length array.
        ('PersistentLogins', ISCSI_Persistent_Login * 1),
    ]

    # MSiSCSI_TargetMappings - MSiSCSI_TargetMappings
    # Target mappings for iSCSI LUNs
    # This class is required.
    # This class returns the list of current OS mappings for iSCSI LUNs
    # The iSCSI initiator service relies upon this
    # class in order to interface with your HBA. Implement one instance
    # per adapter. This class must be registered using PDO
    # instance names.
    MSiSCSI_TargetMappingsGuid = [
        0x41646815,
        0x7524,
        0x4BC0,
        [0x90, 0x4A, 0xCD, 0x7D, 0x51, 0x0E, 0xAC, 0x02],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_TargetMappings_GUID = DEFINE_GUID(
            0x41646815,
            0x7524,
            0x4BC0,
            0x90,
            0x4A,
            0xCD,
            0x7D,
            0x51,
            0x0E,
            0xAC,
            0x02
        )

    # END IF
    MSiSCSI_TargetMappings_UniqueAdapterId_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_TargetMappings_UniqueAdapterId_ID = 1
    MSiSCSI_TargetMappings_TargetMappingCount_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_TargetMappings_TargetMappingCount_ID = 2
    MSiSCSI_TargetMappings_Reserved_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_TargetMappings_Reserved_ID = 3
    MSiSCSI_TargetMappings_TargetMappings_ID = 4

    _MSiSCSI_TargetMappings._fields_ = [
        # Id that is globally unique to each instance of each adapter. This
        # should be the value returned by the MSiSCSI_HBAInformation class.
        ('UniqueAdapterId', ULONGLONG),
        # Number of target mappings
        ('TargetMappingCount', ULONG),
        # Reserved
        ('Reserved', ULONG),
        # Array of TargetMappingCount ISCSI_TargetMapping structures. NOTE:
        # This field is a variable length array.
        ('TargetMappings', ISCSI_TargetMapping * 1),
    ]

    # MSiSCSI_LUNMappingInformation - MSiSCSI_LUNMappingInformation
    # LUN Mapping Information
    # This class is required.
    # It must be implemented using PDO instance names by the PDO device object
    # This class exposes the OS SCSI address information for a particular LUN.
    # The SCSI address information must be consistent with the information
    # returned
    # by the MSIScsi_TargetMappings class and the information reported to the
    # port
    # driver. The class must be implemented on the PDO device object so that
    # there
    # will be one instance for each device created by the adapter and named by
    # the
    # PDO name for the created device and not the adapter
    MSiSCSI_LUNMappingInformationGuid = [
        0x7BB02370,
        0xB8AE,
        0x4D29,
        [0x88, 0xDE, 0x76, 0x95, 0x1D, 0x32, 0x45, 0xBA],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_LUNMappingInformation_GUID = DEFINE_GUID(
            0x7BB02370,
            0xB8AE,
            0x4D29,
            0x88,
            0xDE,
            0x76,
            0x95,
            0x1D,
            0x32,
            0x45,
            0xBA
        )

    # END IF
    MSiSCSI_LUNMappingInformation_UniqueAdapterId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_LUNMappingInformation_UniqueAdapterId_ID = 1
    MSiSCSI_LUNMappingInformation_UniqueSessionId_SIZE = (
        ctypes.sizeof(ULONGLONG)
    )
    MSiSCSI_LUNMappingInformation_UniqueSessionId_ID = 2
    MSiSCSI_LUNMappingInformation_OSBus_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_LUNMappingInformation_OSBus_ID = 3
    MSiSCSI_LUNMappingInformation_OSTarget_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_LUNMappingInformation_OSTarget_ID = 4
    MSiSCSI_LUNMappingInformation_OSLUN_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_LUNMappingInformation_OSLUN_ID = 5

    _MSiSCSI_LUNMappingInformation._fields_ = [
        # Id that is globally unique to each instance of each adapter. Using
        # the address of the Adapter Extension is a good idea.
        ('UniqueAdapterId', ULONGLONG),
        # Id that is unique to this session within this adapter. This should
        # be the same session id as the one assigned when the session was
        # logged in.
        ('UniqueSessionId', ULONGLONG),
        # OS Bus Number
        ('OSBus', ULONG),
        # OS Target Number
        ('OSTarget', ULONG),
        # OS LUN Number
        ('OSLUN', ULONG),
    ]
    MSiSCSI_LUNMappingInformation_SIZE = (
        FIELD_OFFSET(MSiSCSI_LUNMappingInformation, 'OSLUN') +
        MSiSCSI_LUNMappingInformation_OSLUN_SIZE
    )

    # MSiSCSI_SecurityConfigOperations - MSiSCSI_SecurityConfigOperations
    # This class is required if your adapter supports IPSEC or CHAP.
    # An adapter must support the appropriate methods if it implements
    # security including IKE (using preshared keys) and/or a non volatile
    # cache for IPSEC preshared keys and iSCSI authentication credentials
    # (ie, username and passwords). The adapter should also indicate that
    # that the cache is implemented by setting the appropriate flags in the
    # MSiSCSI_HBAInformation class
    # This class must be registered using PDO instance names with a single
    # instance
    MSiSCSI_SecurityConfigOperationsGuid = [
        0x391F3325,
        0x0BA3,
        0x4083,
        [0xA8, 0x61, 0xCF, 0x4F, 0x6F, 0x97, 0xA5, 0x27],
    ]
    if not defined(MIDL_PASS):
        MSiSCSI_SecurityConfigOperations_GUID = DEFINE_GUID(
            0x391F3325,
            0x0BA3,
            0x4083,
            0xA8,
            0x61,
            0xCF,
            0x4F,
            0x6F,
            0x97,
            0xA5,
            0x27
        )

    # END IF
    # Method id definitions for MSiSCSI_SecurityConfigOperations
    # This method is required if the initiator supports IKE.
    # SetPresharedKeyForId allows a management application to configure an
    # adapter with a preshared key that is associated with an id. The
    # id corresponds to the contents of the identification payload in the
    # IKE phase 1 aggressive or main mode exchange. The
    # key can be associated with an ip address for use in the IKE phase 1
    # main mode exchange. The adapter should maintain the key in its non
    # volatile storage if it is available. The adapter should also maintain
    # the key in its working memory so that it is available for IKE phase 1
    # negotiation. If NVRAM is not available then the initiator service will
    # maintain the key on behalf of the adapter.
    # IKE Identification payload types (from RFC 2407)
    ID_IPV4_ADDR = 1
    ID_FQDN = 2
    ID_USER_FQDN = 3
    ID_IPV6_ADDR = 5
    SetPresharedKeyForId = 1

    SetPresharedKeyForId_IN_PortNumber_SIZE = ctypes.sizeof(ULONG)
    SetPresharedKeyForId_IN_PortNumber_ID = 1
    SetPresharedKeyForId_IN_SecurityFlags_SIZE = ctypes.sizeof(ULONGLONG)
    SetPresharedKeyForId_IN_SecurityFlags_ID = 2
    SetPresharedKeyForId_IN_IdType_SIZE = ctypes.sizeof(UCHAR)
    SetPresharedKeyForId_IN_IdType_ID = 3
    SetPresharedKeyForId_IN_IdSize_SIZE = ctypes.sizeof(ULONG)
    SetPresharedKeyForId_IN_IdSize_ID = 4
    SetPresharedKeyForId_IN_KeySize_SIZE = ctypes.sizeof(ULONG)
    SetPresharedKeyForId_IN_KeySize_ID = 5
    SetPresharedKeyForId_IN_Id_ID = 6
    SetPresharedKeyForId_IN_Key_ID = 7

    _SetPresharedKeyForId_IN._fields_ = [
        # Specific port number or 0xffffffff for all ports
        ('PortNumber', ULONG),
        ('SecurityFlags', ULONGLONG),
        # Type of Id to associate with the preshared key
        ('IdType', UCHAR),
        # Size in bytes of the Id
        ('IdSize', ULONG),
        # Size in bytes of the Key
        ('KeySize', ULONG),
        # **fields** Id to associate with the key. NOTE: This field is a
        # variable length array, the field that follows this field starts
        # immediately after the end of this field subject to appropriate
        # padding. All fields after this are commented out in the header.
        ('Id', UCHAR * 1),
    ]
    SetPresharedKeyForId_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    SetPresharedKeyForId_OUT_Status_ID = 8

    _SetPresharedKeyForId_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    SetPresharedKeyForId_OUT_SIZE = (
        FIELD_OFFSET(SetPresharedKeyForId_OUT, 'Status') +
        SetPresharedKeyForId_OUT_Status_SIZE
    )

    # This method is required if the initiator supports IKE.
    # GetPresharedKeyForId allows a management application to determine if
    # a particular IKE identification payload is configured with a preshared
    # key
    GetPresharedKeyForId = 2

    GetPresharedKeyForId_IN_PortNumber_SIZE = ctypes.sizeof(ULONG)
    GetPresharedKeyForId_IN_PortNumber_ID = 1
    GetPresharedKeyForId_IN_IdType_SIZE = ctypes.sizeof(UCHAR)
    GetPresharedKeyForId_IN_IdType_ID = 2
    GetPresharedKeyForId_IN_IdSize_SIZE = ctypes.sizeof(ULONG)
    GetPresharedKeyForId_IN_IdSize_ID = 3
    GetPresharedKeyForId_IN_Id_ID = 4

    _GetPresharedKeyForId_IN._fields_ = [
        ('PortNumber', ULONG),
        # Type of Id to associate with the preshared key
        ('IdType', UCHAR),
        # Size in bytes of the Id
        ('IdSize', ULONG),
        # Id to associate with the key. NOTE: This field is a variable length
        # array.
        ('Id', UCHAR * 1),
    ]
    GetPresharedKeyForId_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    GetPresharedKeyForId_OUT_Status_ID = 5
    GetPresharedKeyForId_OUT_SecurityFlags_SIZE = ctypes.sizeof(ULONGLONG)
    GetPresharedKeyForId_OUT_SecurityFlags_ID = 6

    _GetPresharedKeyForId_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
        ('SecurityFlags', ULONGLONG),
    ]
    GetPresharedKeyForId_OUT_SIZE = (
        FIELD_OFFSET(GetPresharedKeyForId_OUT, 'SecurityFlags') +
        GetPresharedKeyForId_OUT_SecurityFlags_SIZE
    )

    # This method is required.if the initiator supports IKE
    # SetGroupPresharedKey allows a management application to configure an
    # adapter with a group preshared key that is used in an IKE phase 1
    # exchange
    # when there is no specific key available for that exchange. The adapter
    # should maintain the key in its non volatile storage if available and
    # maintain the key in its working memory so that it is available for IKE
    # phase 1 negotiation
    SetGroupPresharedKey = 3

    SetGroupPresharedKey_IN_KeySize_SIZE = ctypes.sizeof(ULONG)
    SetGroupPresharedKey_IN_KeySize_ID = 1
    SetGroupPresharedKey_IN_Key_ID = 2

    _SetGroupPresharedKey_IN._fields_ = [
        # Number of bytes passed in Key for the preshared key
        ('KeySize', ULONG),
        # Preshared key used as group key. NOTE: This field is a variable
        # length array.
        ('Key', UCHAR * 1),
    ]
    SetGroupPresharedKey_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    SetGroupPresharedKey_OUT_Status_ID = 3

    _SetGroupPresharedKey_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    SetGroupPresharedKey_OUT_SIZE = (
        FIELD_OFFSET(SetGroupPresharedKey_OUT, 'Status') +
        SetGroupPresharedKey_OUT_Status_SIZE
    )

    # This method is required.if the initiator supports IPSEC tunnel mode
    # SetTunnelModeOuterAddress allows a management application to configure
    # the
    # tunnel mode outer address that is used by a port on an adapter
    # The adapter should maintain the address in its non volatile
    # storage if available
    SetTunnelModeOuterAddress = 4

    SetTunnelModeOuterAddress_IN_PortNumber_SIZE = ctypes.sizeof(ULONG)
    SetTunnelModeOuterAddress_IN_PortNumber_ID = 1
    SetTunnelModeOuterAddress_IN_DestinationAddress_SIZE = (
        ctypes.sizeof(ISCSI_IP_Address)
    )
    SetTunnelModeOuterAddress_IN_DestinationAddress_ID = 2
    SetTunnelModeOuterAddress_IN_TunnelModeOuterAddress_SIZE = (
        ctypes.sizeof(ISCSI_IP_Address)
    )
    SetTunnelModeOuterAddress_IN_TunnelModeOuterAddress_ID = 3

    _SetTunnelModeOuterAddress_IN._fields_ = [
        # Port number to which to associate tunnel mode address. Use
        # 0xffffffff to associate with all ports.
        ('PortNumber', ULONG),
        # Destination address
        ('DestinationAddress', ISCSI_IP_Address),
        # Tunnel mode outer address
        ('TunnelModeOuterAddress', ISCSI_IP_Address),
    ]
    SetTunnelModeOuterAddress_IN_SIZE = (
        FIELD_OFFSET(SetTunnelModeOuterAddress_IN, 'TunnelModeOuterAddress') +
        SetTunnelModeOuterAddress_IN_TunnelModeOuterAddress_SIZE
    )

    SetTunnelModeOuterAddress_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    SetTunnelModeOuterAddress_OUT_Status_ID = 4

    _SetTunnelModeOuterAddress_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    SetTunnelModeOuterAddress_OUT_SIZE = (
        FIELD_OFFSET(SetTunnelModeOuterAddress_OUT, 'Status') +
        SetTunnelModeOuterAddress_OUT_Status_SIZE
    )

    # This method is required if the initiator caches information
    # ClearCache instructs the HBA to clear the iSCSI authentication and
    # preshared key caches
    ClearCache = 5

    ClearCache_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    ClearCache_OUT_Status_ID = 1

    _ClearCache_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    ClearCache_OUT_SIZE = (
        FIELD_OFFSET(ClearCache_OUT, 'Status') +
        ClearCache_OUT_Status_SIZE
    )

    # This method is required.if the initiator caches information
    # This method establishes a marker that the service can subsequently
    # validate to ensure that the initiator cache is valid
    SetGenerationalGuid = 6

    SetGenerationalGuid_IN_GenerationalGuid_SIZE = ctypes.sizeof(UCHAR[16])
    SetGenerationalGuid_IN_GenerationalGuid_ID = 1

    _SetGenerationalGuid_IN._fields_ = [
        # Generational Guid
        ('GenerationalGuid', UCHAR * 16),
    ]
    SetGenerationalGuid_IN_SIZE = (
        FIELD_OFFSET(SetGenerationalGuid_IN, 'GenerationalGuid') +
        SetGenerationalGuid_IN_GenerationalGuid_SIZE
    )

    SetGenerationalGuid_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    SetGenerationalGuid_OUT_Status_ID = 2

    _SetGenerationalGuid_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
    ]
    SetGenerationalGuid_OUT_SIZE = (
        FIELD_OFFSET(SetGenerationalGuid_OUT, 'Status') +
        SetGenerationalGuid_OUT_Status_SIZE
    )

    # MSiSCSI_BootInformation - MSiSCSI_BootInformation
    MSiSCSI_BootInformationGuid = [
        0xEE5A2356,
        0xC703,
        0x489B,
        [0xB1, 0x36, 0x69, 0xC9, 0x94, 0xAE, 0x3A, 0x20],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_BootInformation_GUID = DEFINE_GUID(
            0xEE5A2356,
            0xC703,
            0x489B,
            0xB1,
            0x36,
            0x69,
            0xC9,
            0x94,
            0xAE,
            0x3A,
            0x20
        )

    # END IF

    MSiSCSI_BootInformation_NodeName_SIZE = ctypes.sizeof(UCHAR[223])
    MSiSCSI_BootInformation_NodeName_ID = 1
    MSiSCSI_BootInformation_SharedSecretLength_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_BootInformation_SharedSecretLength_ID = 2
    MSiSCSI_BootInformation_SharedSecret_SIZE = ctypes.sizeof(UCHAR[255])
    MSiSCSI_BootInformation_SharedSecret_ID = 3

    _MSiSCSI_BootInformation._fields_ = [
        # Initiator Node Name used for boot
        ('NodeName', UCHAR * 223),
        # Length of Initiator Shared Secret
        ('SharedSecretLength', ULONG),
        # Initiator Shared Secret
        ('SharedSecret', UCHAR * 255),
    ]
    MSiSCSI_BootInformation_SIZE = (
        FIELD_OFFSET(MSiSCSI_BootInformation, 'SharedSecret') +
        MSiSCSI_BootInformation_SharedSecret_SIZE
    )

    # MSiSCSI_AdapterEvent - MSiSCSI_AdapterEvent
    class ISCSI_ADAPTER_EVENT_CODE(ENUM):
        ISCSI_ADAPTER_TARGETS_CHANGED = 3

    PISCSI_ADAPTER_EVENT_CODE = POINTER(ISCSI_ADAPTER_EVENT_CODE)
    ISCSI_ADAPTER_TARGETS_CHANGED = ISCSI_ADAPTER_EVENT_CODE.ISCSI_ADAPTER_TARGETS_CHANGED

    # This class is required if the HBA supports discovery
    # This class must be registered using PDO instance names with a single
    # instance
    MSiSCSI_AdapterEventGuid = [
        0x46B122C0,
        0x3767,
        0x4069,
        [0x91, 0x6E, 0x3A, 0x43, 0x70, 0x2F, 0x05, 0xCE],
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_AdapterEvent_GUID = DEFINE_GUID(
            0x46B122C0,
            0x3767,
            0x4069,
            0x91,
            0x6E,
            0x3A,
            0x43,
            0x70,
            0x2F,
            0x05,
            0xCE
        )

    # END IF
    MSiSCSI_AdapterEvent_UniqueAdapterId_SIZE = ctypes.sizeof(ULONGLONG)
    MSiSCSI_AdapterEvent_UniqueAdapterId_ID = 1
    MSiSCSI_AdapterEvent_EventCode_SIZE = ctypes.sizeof(ULONG)
    MSiSCSI_AdapterEvent_EventCode_ID = 2

    _MSiSCSI_AdapterEvent._fields_ = [
        # Id that is unique to each instance of each adapter. This is the ID
        # returned in the MSiSCSI_HBAInformation class.
        ('UniqueAdapterId', ULONGLONG),
        # **typedef**Adapter Event Code
        ('EventCode', ULONG),
    ]
    MSiSCSI_AdapterEvent_SIZE = (
        FIELD_OFFSET(MSiSCSI_AdapterEvent, 'EventCode') +
        MSiSCSI_AdapterEvent_EventCode_SIZE
    )
# END IF
