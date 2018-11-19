import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _MRX_NORMAL_NODE_HEADER(ctypes.Structure):
    pass


MRX_NORMAL_NODE_HEADER = _MRX_NORMAL_NODE_HEADER


class _MRX_SRV_CALL_(ctypes.Structure):
    pass

typedef struct _MRX_SRV_CALL_ {
                MRX_NORMAL_NODE_HEADER
        #endif // __cplusplus
         // not not not not  changes above this require realignment with fcb.h
         // the context fields for extensions required by the mini redirectors
        PVOID Context
        PVOID Context2
         // Associated DeviceObject which also contains the dispatch vector
        PRDBSS_DEVICE_OBJECT RxDeviceObject
         // the srv call name = _MRX_SRV_CALL_
the server principal name and the server domain name.
        PUNICODE_STRING pSrvCallName
        PUNICODE_STRING pPrincipalName
        PUNICODE_STRING pDomainName
         // Flags used to denote the state of the SRV_CALL.
        ULONG Flags
         // Server parameters updated by the mini redirectors.
        LONG MaximumNumberOfCloseDelayedFiles
         // Status return from the transport in case of failure
        NTSTATUS Status = _MRX_SRV_CALL_


class _NETROOT_THROTTLING_PARAMETERS(ctypes.Structure):
    pass

NETROOT_THROTTLING_PARAMETERS = _NETROOT_THROTTLING_PARAMETERS
PNETROOT_THROTTLING_PARAMETERS = POINTER(_NETROOT_THROTTLING_PARAMETERS)


class _MRX_NET_ROOT_(ctypes.Structure):
    pass


class _MRX_V_NET_ROOT_(ctypes.Structure):
    pass

typedef struct _MRX_V_NET_ROOT_ {
                MRX_NORMAL_NODE_HEADER
                #endif // __cplusplus
                 // the MRX_NET_ROOT instance with which the MRX_V_NET_ROOT instance is associated
                PMRX_NET_ROOT pNetRoot
                 // not not not not  changes above this require realignment with fcb.h
                 // the context fields provided for storing additional information as deemed
                 // necessary by the mini redirectors
                PVOID Context
                PVOID Context2
                ULONG Flags
                 // This field should not be updated by the mini redirectors. Its usage is intended
                 // to provide an easy mechanism for accessing certain state information
                ULONG NumberOfOpens
                 // We count the number of Fobxss on the virtual netroot
                __volatile ULONG NumberOfFobxs
                 // the security parameters associated with the V_NET_ROOT instance.
                LUID LogonId
                 // These are the parameters supplied by the used in a NtCreateFile call in
                 // which the FILE_CREATE_TREE_CONNECTION flag is specified as part of the
                 // CreateOptions.
                PUNICODE_STRING pUserDomainName
                PUNICODE_STRING pUserName
                PUNICODE_STRING pPassword
                ULONG SessionId
                NTSTATUS ConstructionStatus
                BOOLEAN IsExplicitConnection = _MRX_V_NET_ROOT_


class _MRX_FCB_(ctypes.Structure):
    pass

MRX_FCB = _MRX_FCB_
PMRX_FCB = POINTER(_MRX_FCB_)


class MRXSHADOW_SRV_OPEN(ctypes.Structure):
    pass

PMRXSHADOW_SRV_OPEN = POINTER(MRXSHADOW_SRV_OPEN)


class _MRX_SRV_OPEN_(ctypes.Structure):
    pass

typedef struct _MRX_SRV_OPEN_ {
                    MRX_NORMAL_NODE_HEADER
                    #endif // __cplusplus
                     // the MRX_FCB instance with which the SRV_OPEN is associated.
                    PMRX_FCB pFcb
                     // the V_NET_ROOT instance with which the SRV_OPEN is associated
                    PMRX_V_NET_ROOT pVNetRoot
                     // not not not not  changes above this require realignment with fcb.h
                     // the context fields to store additional state information as deemed necessary
                     // by the mini redirectors
                    PVOID Context
                    PVOID Context2
                     // shadow context = _MRX_SRV_OPEN_
mini - rdr allocates and deallocates this structure
                    PMRXSHADOW_SRV_OPEN ShadowContext
                     // The flags are split into two groups = _MRX_SRV_OPEN_
i.e. = _MRX_SRV_OPEN_
visible to mini rdrs and invisible
                     // to mini rdrs. The visible ones are defined above and the definitions for the
                     // invisible ones can be found in fcb.h. The convention that has been adopted is
                     // that the lower 16 flags will be visible to the mini rdr and the upper 16 flags
                     // will be reserved for the wrapper. This needs to be enforced in defining new flags.
                    ULONG Flags
                     // the name alongwith the MRX_NET_ROOT prefix = _MRX_SRV_OPEN_
i.e. fully qualified name
                    PUNICODE_STRING pAlreadyPrefixedName
                     // the number of Fobx's associated with this open for which a cleanup IRP
                     // has not been processed.
                    CLONG UncleanFobxCount
                     // the number of local opens associated with this open on the server
                    CLONG OpenCount
                     // the Key assigned by the mini redirector for this SRV_OPEN. Since the various mini
                     // redirectors do not always get to pick the unique id for a open instance = _MRX_SRV_OPEN_
the key
                     // used to identify the open to the server is different for different mini redirectors
                     // based upon the convention adopted at the server.
                    PVOID Key
                     // the access and sharing rights specified for this SRV_OPEN. This is used in
                     // determining is subsequent open requests can be collapsed  with an existing
                     // SRV_OPEN instance.
                    ACCESS_MASK DesiredAccess
                    ULONG ShareAccess
                    ULONG CreateOptions
                     // The BufferingFlags field is temporal.....it does not really belong to the
                     // srvopen rather the srvopen is used as a representative of the fcb. On
                     // each open = _MRX_SRV_OPEN_
the bufferingflags field of the srvopen is taken as the minirdr's
                     // contribution to the buffering state. On an oplock break = _MRX_SRV_OPEN_
a srvopen is passed
                     // (the one that's being broken) whose bufferflags field is taken as the new
                     // proxy. On a close that changes the minirdr's contribution = _MRX_SRV_OPEN_
the minirdr should
                     // take steps to cause a ChangeBufferingState to the new state.
                     // just to reiterate = _MRX_SRV_OPEN_
the field is just used to carry the information from
                     // the minirdr to RxChangeBufferingState and does not hold longterm coherent
                     // information.
                    ULONG BufferingFlags
                     // List Entry to wire the SRV_OPEN to the list of SRV_OPENS maintained as
                     // part of theFCB
                     // THIS FIELD IS READONLY FOR MINIS
                    ULONG ulFileSizeVersion
                    LIST_ENTRY SrvOpenQLinks = _MRX_SRV_OPEN_


class _MRX_PIPE_HANDLE_INFORMATION(ctypes.Structure):
    pass

MRX_PIPE_HANDLE_INFORMATION = _MRX_PIPE_HANDLE_INFORMATION
PMRX_PIPE_HANDLE_INFORMATION = POINTER(_MRX_PIPE_HANDLE_INFORMATION)


class _MRX_FOBX_(ctypes.Structure):
    pass

// The following field is used as an offset into the Eas for a
                         // particular file.  This will be the offset for the next
                         // Ea to return.  A value of 0xffffffff indicates that the
                         // Ea's are exhausted.
                        
                        
                         // This field is manipulated directly by the smbmini....maybe it should move down
                         // one thing is that it is a reminder that NT allows a resume on getting EAs
                        
                        
                        ULONG OffsetOfNextEaToReturn = _MRX_FOBX_


# /* + + Copyright (c) 1994 Microsoft Corporation Module Name: mrxfFcb.h
# Abstract: This module defines the macros/inline functions and function
# prototypes used by the mini redirectors to access the RDBSS wrapper data
# structures. IMPORTANT: All mini redirector writers cannot and should not
# make any assumptions about the layout of the RDBSS wrapper data structures.
# They are not guaranteed to be the same across platforms and even on a single
# platform are liable to change across versions. The following six data
# structure abstractions are available to the mini redirector writer.
# 1) Server Call Context (SRV_CALL) The context associated with each known file system server. 2) Net Roots (NET_ROOT) The root of a file system volume( local/remote) opened by the user. 3) Virtual Net Roots (V_NET_ROOT) The view of a file system volume on a server. The view can be constrained along multiple dimensions. As an example the view can be associated with a logon id. which will constrain the operations that can be performed on the file system volume. 4) File Control Blocks (FCB) The RDBSS data structure associated with each unique file opened. 5) File Object Extensions (FOXB) 6) ServerSide Open Context (SRV_OPEN) A common convention that is adopted for defining Flags in all of these data structures is to define a ULONG ( 32 ) flags and split them into two groups - - those that are visible to the mini redirector and those that are invisible. These flags are not meant for use by the mini redirector writers and are reserved for the wrapper. Author: Revision History: - -
# 
if not defined(__MRXFCB_H__):
    #~#~#~    #define __MRXFCB_H__
    # The SRVCALL flags are split into two groups, i.e., visible to mini rdrs
    # and invisible to mini rdrs.
    # The visible ones are defined above and the definitions for the invisible
    # ones can be found
    # in fcb.h. The convention that has been adopted is that the lower 16
    # flags will be visible
    # to the mini rdr and the upper 16 flags will be reserved for the wrapper.
    # This needs to be
    # enforced in defining new flags.
    SRVCALL_FLAG_MAILSLOT_SERVER = 0x1
    SRVCALL_FLAG_FILE_SERVER = 0x2
    SRVCALL_FLAG_CASE_INSENSITIVE_NETROOTS = 0x4
    SRVCALL_FLAG_CASE_INSENSITIVE_FILENAMES = 0x8
    SRVCALL_FLAG_DFS_AWARE_SERVER = 0x10
    SRVCALL_FLAG_FORCE_FINALIZED = 0x20
    SRVCALL_FLAG_LWIO_AWARE_SERVER = 0x40
    SRVCALL_FLAG_LOOPBACK_SERVER = 0x80


    _MRX_NORMAL_NODE_HEADER._fields_ = [
        ('NodeTypeCode', NODE_TYPE_CODE),
        ('NodeByteSize', NODE_BYTE_SIZE),
        ('ULONG                    NodeReferenceCount', __volatile),
    ]
    if defined(__cplusplus):
    _MRX_SRV_CALL_._fields_ = [
        # the context fields for extensions required by the mini redirectors
        ('Context', PVOID),
        ('Context2', PVOID),
        # Associated DeviceObject which also contains the dispatch vector
        ('RxDeviceObject', PRDBSS_DEVICE_OBJECT),
        # the srv call name, the server principal name and the server domain
        # name.
        ('pSrvCallName', PUNICODE_STRING),
        ('pPrincipalName', PUNICODE_STRING),
        ('pDomainName', PUNICODE_STRING),
        # Flags used to denote the state of the SRV_CALL.
        ('Flags', ULONG),
        # Server parameters updated by the mini redirectors.
        ('MaximumNumberOfCloseDelayedFiles', LONG),
        # Status return from the transport in case of failure
        ('Status', NTSTATUS),
    ]


        # The various types of NET_ROOT's currently supported by the wrapper.
        NET_ROOT_DISK = (UCHAR)0
        NET_ROOT_PIPE = (UCHAR)1
        NET_ROOT_COMM = (UCHAR)2
        NET_ROOT_PRINT = (UCHAR)3
        NET_ROOT_WILD = (UCHAR)4
        NET_ROOT_MAILSLOT = (UCHAR)5
        NET_ROOT_TYPE = UCHAR
        PNET_ROOT_TYPE = POINTER(UCHAR)


        # The pipe buffer size for transferring cannot be larger than 0xffff
        MAX_PIPE_BUFFER_SIZE = 0xFFFF


        # The possible states associated with a NET_ROOT. These have been
        # defined to be
        # line with the definitions foe the LanManager service to avoid
        # redundant mappings.
        # These MUST agree with sdkinc\lmuse.h use_ok, etc.....
        MRX_NET_ROOT_STATE_GOOD = (UCHAR)0
        MRX_NET_ROOT_STATE_PAUSED = (UCHAR)1
        MRX_NET_ROOT_STATE_DISCONNECTED = (UCHAR)2
        MRX_NET_ROOT_STATE_ERROR = (UCHAR)3
        MRX_NET_ROOT_STATE_CONNECTED = (UCHAR)4
        MRX_NET_ROOT_STATE_RECONN = (UCHAR)5
        MRX_NET_ROOT_STATE = UCHAR
        PMRX_NET_ROOT_STATE = POINTER(UCHAR)


        # The file systems on the remote servers provide varying levels of
        # functionality to
        # detect aliasing between file names. As an example consider two
        # shares on the same
        # file system volume. In the absence of any support from the file
        # system on the server
        # the correct and conservative approach is to flush all the files to
        # the server as
        # opposed to all the files on the same NET_ROOT to preserve coherency
        # and handle
        # delayed close operations.
        MRX_PURGE_SAME_NETROOT = (UCHAR)0
        MRX_PURGE_SAME_SRVCALL = (UCHAR)1


        # these are not implemented yet....
        # define MRX_PURGE_SAME_FCB   ((UCHAR)2)
        # define MRX_PURGE_SAME_VOLUME  ((UCHAR)3)
        # define MRX_PURGE_ALL   ((UCHAR)4)
        MRX_PURGE_RELATIONSHIP = UCHAR
        PMRX_PURGE_RELATIONSHIP = POINTER(UCHAR)
        MRX_PURGE_SYNC_AT_NETROOT = (UCHAR)0
        MRX_PURGE_SYNC_AT_SRVCALL = (UCHAR)1
        MRX_PURGE_SYNCLOCATION = UCHAR
        PMRX_PURGE_SYNCLOCATION = POINTER(UCHAR)


        # The NET_ROOT flags are split into two groups, i.e., visible to mini
        # rdrs and
        # invisible to mini rdrs. The visible ones are defined above and the
        # definitions
        # for the invisible ones can be found in fcb.h. The convention that
        # has been
        # adopted is that the lower 16 flags will be visible to the mini rdr
        # and the
        # upper 16 flags will be reserved for the wrapper. This needs to be
        # enforced
        # in defining new flags.
        NETROOT_FLAG_SUPPORTS_SYMBOLIC_LINKS = 0x0001
        NETROOT_FLAG_DFS_AWARE_NETROOT = 0x0002
        NETROOT_FLAG_DEFER_READAHEAD = 0x0004
        NETROOT_FLAG_VOLUMEID_INITIALIZED = 0x0008
        NETROOT_FLAG_FINALIZE_INVOKED = 0x0010
        NETROOT_FLAG_UNIQUE_FILE_NAME = 0x0020


        # Read ahead amount used for normal data files (32k)
        DEFAULT_READ_AHEAD_GRANULARITY = 0x08000


        # the wrapper implements throttling for certain kinds of operations:
        # PeekNamedPipe/ReadNamedPipe
        # LockFile
        # a minirdr can set the timing parameters for this in the netroot.
        # leaving them
        # as zero will disable throttling.
        _NETROOT_THROTTLING_PARAMETERS._fields_ = [
            # to the network fails.
            ('Increment', ULONG),
            # in milliseconds.
            ('MaximumDelay', ULONG),
        ]
        

        def RxInitializeNetRootThrottlingParameters(__tp, __incr, __maxdelay):
            return { PNETROOT_THROTTLING_PARAMETERS tp = __tp; tp - >Increment = __incr; tp - >MaximumDelay = __maxdelay; }

        if defined(__cplusplus):
        _MRX_NET_ROOT_._fields_ = [
            # the MRX_SRV_CALL instance with which this MRX_NET_ROOT instance
            # is associated
            ('pSrvCall', PMRX_SRV_CALL),
            # additional state.
            ('Context', PVOID),
            ('Context2', PVOID),
            # The flags used to denote the state of the NET_ROOT instance.
            ('Flags', ULONG),
            # We count the number of fcbs, srvopens on the netroot
            ('ULONG NumberOfFcbs', __volatile),
            ('ULONG NumberOfSrvOpens', __volatile),
            # provided by the file system on the server.
            ('MRxNetRootState', MRX_NET_ROOT_STATE),
            ('Type', NET_ROOT_TYPE),
            ('PurgeRelationship', MRX_PURGE_RELATIONSHIP),
            ('PurgeSyncLocation', MRX_PURGE_SYNCLOCATION),
            # the type of device, i.e., file system volume, printer, com port
            # etc.
            ('DeviceType', DEVICE_TYPE),
            # Name of the NET_ROOT instance
            ('pNetRootName', PUNICODE_STRING),
            # the name to be prepended to all FCBS associated with this
            # NET_ROOT
            ('InnerNamePrefix', UNICODE_STRING),
            # Parameters based upon the type of the NET_ROOT.
            ('ParameterValidationStamp', ULONG),
        ]

            # The VNET_ROOT flags are split into two groups, i.e., visible to
            # mini rdrs and
            # invisible to mini rdrs. The visible ones are defined below and
            # the definitions
            # for the invisible ones can be found in fcb.h. The convention
            # that has been
            # adopted is that the lower 16 flags will be visible to the mini
            # rdr and the
            # upper 16 flags will be reserved for the wrapper. This needs to
            # be enforced
            # in defining new flags.
            VNETROOT_FLAG_CSCAGENT_INSTANCE = 0x00000001
            VNETROOT_FLAG_FINALIZE_INVOKED = 0x00000002
            VNETROOT_FLAG_FORCED_FINALIZE = 0x00000004
            VNETROOT_FLAG_NOT_FINALIZED = 0x00000008

            if defined(__cplusplus):
            _MRX_V_NET_ROOT_._fields_ = [
                # the MRX_NET_ROOT instance with which the MRX_V_NET_ROOT
                # instance is associated
                ('pNetRoot', PMRX_NET_ROOT),
                # necessary by the mini redirectors
                ('Context', PVOID),
                ('Context2', PVOID),
                ('Flags', ULONG),
                # to provide an easy mechanism for accessing certain state
                # information
                ('NumberOfOpens', ULONG),
                # We count the number of Fobxss on the virtual netroot
                ('ULONG NumberOfFobxs', __volatile),
                # the security parameters associated with the V_NET_ROOT
                # instance.
                ('LogonId', LUID),
                # CreateOptions.
                ('pUserDomainName', PUNICODE_STRING),
                ('pUserName', PUNICODE_STRING),
                ('pPassword', PUNICODE_STRING),
                ('SessionId', ULONG),
                ('ConstructionStatus', NTSTATUS),
            ]

                # ALL FIELDS IN AN FCB ARE READONLY EXCEPT Context and
                # Context2....
                # Also, Context is read only the the mini has specified
                # RDBSS_MANAGE_FCB_EXTENSION
                _MRX_FCB_._fields_ = [
                    ('Header', FSRTL_ADVANCED_FCB_HEADER),
                    # The MRX_NET_ROOT instance with which this is associated
                    ('pNetRoot', PMRX_NET_ROOT),
                    # mini redirectors.
                    ('Context', PVOID),
                    ('Context2', PVOID),
                    # the FSRTL_COMMON_FCB_HEADER structure.
                    ('ULONG NodeReferenceCount', __volatile),
                    # The internal state of the Fcb. THIS FIELD IS READONLY
                    # FOR MINIRDRS
                    ('FcbState', ULONG),
                    # while the OpenCount below gets decremented in
                    # RxCommonClose.
                    ('CLONG UncleanCount', __volatile),
                    # purges are required to maintain coherence.
                    ('UncachedUncleanCount', CLONG),
                    # file object points to this record.
                    ('CLONG OpenCount', __volatile),
                    # shared to manipulate it but you have to have it
                    # exclusive to use it.
                    ('ULONG OutstandingLockOperationsCount', __volatile),
                    # The actual allocation length as opposed to the valid
                    # data length
                    ('ActualAllocationLength', ULONGLONG),
                    # Attributes of the MRX_FCB,
                    ('Attributes', ULONG),
                    # DWORD boundaries.
                    ('IsFileWritten', BOOLEAN),
                    ('fShouldBeOrphaned', BOOLEAN),
                    ('fMiniInited', BOOLEAN),
                    # Type of the associated MRX_NET_ROOT, intended to avoid
                    # pointer chasing.
                    ('CachedNetRootType', UCHAR),
                    # THIS FIELD IS READONLY FOR MINIS
                    ('SrvOpenList', LIST_ENTRY),
                    # THIS FIELD IS READONLY FOR MINIS
                    ('SrvOpenListVersion', ULONG),
                ]

                # The following flags define the various types of buffering
                # that can be selectively
                # enabled or disabled for each SRV_OPEN.
                SRVOPEN_FLAG_DONTUSE_READ_CACHING = 0x1
                SRVOPEN_FLAG_DONTUSE_WRITE_CACHING = 0x2
                SRVOPEN_FLAG_CLOSED = 0x4
                SRVOPEN_FLAG_CLOSE_DELAYED = 0x8
                SRVOPEN_FLAG_FILE_RENAMED = 0x10
                SRVOPEN_FLAG_FILE_DELETED = 0x20
                SRVOPEN_FLAG_BUFFERING_STATE_CHANGE_PENDING = 0x40
                SRVOPEN_FLAG_COLLAPSING_DISABLED = 0x80
                SRVOPEN_FLAG_BUFFERING_STATE_CHANGE_REQUESTS_PURGED = 0x100
                SRVOPEN_FLAG_NO_BUFFERING_STATE_CHANGE = 0x200
                SRVOPEN_FLAG_ORPHANED = 0x400
                (NTAPI *PMRX_SHADOW_CALLDOWN) (
                IN OUT struct _RX_CONTEXT * RxContext
                ) = NTSTATUS

                # Minirdrs allocate, initialize and free this structure
                MRXSHADOW_SRV_OPEN._fields_ = [
                    # after the handle is successfully created in the usermode.
                    ('UnderlyingFileObject', PFILE_OBJECT),
                    # above.
                    ('UnderlyingDeviceObject', PDEVICE_OBJECT),
                    ('LockKey', ULONG),
                    ('FastIoRead', PFAST_IO_READ),
                    ('FastIoWrite', PFAST_IO_WRITE),
                    ('DispatchRoutine', PMRX_SHADOW_CALLDOWN),
                ]
                if defined(__cplusplus):
                _MRX_SRV_OPEN_._fields_ = [
                    # the MRX_FCB instance with which the SRV_OPEN is
                    # associated.
                    ('pFcb', PMRX_FCB),
                    # the V_NET_ROOT instance with which the SRV_OPEN is
                    # associated
                    ('pVNetRoot', PMRX_V_NET_ROOT),
                    # by the mini redirectors
                    ('Context', PVOID),
                    ('Context2', PVOID),
                    # shadow context, mini - rdr allocates and deallocates
                    # this structure
                    ('ShadowContext', PMRXSHADOW_SRV_OPEN),
                    # will be reserved for the wrapper. This needs to be
                    # enforced in defining new flags.
                    ('Flags', ULONG),
                    # the name alongwith the MRX_NET_ROOT prefix, i.e. fully
                    # qualified name
                    ('pAlreadyPrefixedName', PUNICODE_STRING),
                    # has not been processed.
                    ('UncleanFobxCount', CLONG),
                    # the number of local opens associated with this open on
                    # the server
                    ('OpenCount', CLONG),
                    # based upon the convention adopted at the server.
                    ('Key', PVOID),
                    # SRV_OPEN instance.
                    ('DesiredAccess', ACCESS_MASK),
                    ('ShareAccess', ULONG),
                    ('CreateOptions', ULONG),
                    # information.
                    ('BufferingFlags', ULONG),
                    # THIS FIELD IS READONLY FOR MINIS
                    ('ulFileSizeVersion', ULONG),
                    ('SrvOpenQLinks', LIST_ENTRY),
                ]
                    FOBX_FLAG_DFS_OPEN = 0x0001
                    FOBX_FLAG_BAD_HANDLE = 0x0002
                    FOBX_FLAG_BACKUP_INTENT = 0x0004
                    FOBX_FLAG_NOT_USED = 0x0008
                    FOBX_FLAG_FLUSH_EVEN_CACHED_READS = 0x0010
                    FOBX_FLAG_DONT_ALLOW_PAGING_IO = 0x0020
                    FOBX_FLAG_DONT_ALLOW_FASTIO_READ = 0x0040


                    _MRX_PIPE_HANDLE_INFORMATION._fields_ = [
                        ('TypeOfPipe', ULONG),
                        ('ReadMode', ULONG),
                        ('CompletionMode', ULONG),
                    ]
                    if defined(__cplusplus):
                    _MRX_FOBX_._fields_ = [
                        # the MRX_SRV_OPEN instance with which the FOBX is
                        # associated
                        ('pSrvOpen', PMRX_SRV_OPEN),
                        # is NULL.
                        ('AssociatedFileObject', PFILE_OBJECT),
                        # by the various mini redirectors
                        ('Context', PVOID),
                        ('Context2', PVOID),
                        # enforced in defining new flags.
                        ('Flags', ULONG),
                    ]

                        # Resource accquisition routines.
                        # The synchronization resources of interest to mini
                        # redirector writers are
                        # primarily associated with the FCB. There is a paging
                        # I/O resource and a
                        # regular resource. The paging I/O resource is managed
                        # by the wrapper. The only
                        # resource accesible to mini redirector writers is the
                        # regular resource which
                        # should be accessed using the supplied routines.
                        rdbss = ctypes.windll.RDBSS


                        # NTSTATUS
                        # RxAcquireExclusiveFcbResourceInMRx(
                        # _Inout_ PMRX_FCB Fcb
                        # );
                        RxAcquireExclusiveFcbResourceInMRx = (
                            rdbss.RxAcquireExclusiveFcbResourceInMRx
                        )
                        RxAcquireExclusiveFcbResourceInMRx.restype = NTSTATUS


                        # NTSTATUS
                        # RxAcquireSharedFcbResourceInMRx(
                        # _Inout_ PMRX_FCB Fcb
                        # );
                        RxAcquireSharedFcbResourceInMRx = (
                            rdbss.RxAcquireSharedFcbResourceInMRx
                        )
                        RxAcquireSharedFcbResourceInMRx.restype = NTSTATUS


                        # VOID
                        # RxReleaseFcbResourceInMRx(
                        # PMRX_FCB Fcb
                        # );
                        RxReleaseFcbResourceInMRx = (
                            rdbss.RxReleaseFcbResourceInMRx
                        )
                        RxReleaseFcbResourceInMRx.restype = VOID


                        # extern VOID
                        # RxReleaseFcbResourceForThreadInMRx(
                        # IN PRX_CONTEXT      pRxContext,
                        # IN OUT PMRX_FCB     MrxFcb,
                        # IN ERESOURCE_THREAD ResourceThreadId);
                        RxReleaseFcbResourceForThreadInMRx = (
                            rdbss.RxReleaseFcbResourceForThreadInMRx
                        )
                        RxReleaseFcbResourceForThreadInMRx.restype = VOID

                    # END IF   __MRXFCB_H__
