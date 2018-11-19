import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _RX_TOPLEVELIRP_CONTEXT(ctypes.Structure):
    pass


RX_TOPLEVELIRP_CONTEXT = _RX_TOPLEVELIRP_CONTEXT
PRX_TOPLEVELIRP_CONTEXT = POINTER(_RX_TOPLEVELIRP_CONTEXT)


class _RX_FCBTRACKER_CALLINFO(ctypes.Structure):
    pass


RX_FCBTRACKER_CALLINFO = _RX_FCBTRACKER_CALLINFO
PRX_FCBTRACKER_CALLINFO = POINTER(_RX_FCBTRACKER_CALLINFO)


class _NT_CREATE_PARAMETERS(ctypes.Structure):
    pass


NT_CREATE_PARAMETERS = _NT_CREATE_PARAMETERS
PNT_CREATE_PARAMETERS = POINTER(_NT_CREATE_PARAMETERS)


class _RX_CONTEXT(ctypes.Structure):
    pass


RX_CONTEXT = _RX_CONTEXT
PRX_CONTEXT = POINTER(_RX_CONTEXT)


# /* + + Copyright (c) 1994 Microsoft Corporation Module Name: RxContx.h
# Abstract: This module defines RxContext data structure. This structure is
# used to describe an Irp whil it is being processed and contains state
# information that allows global resources to be released as the irp is
# completed. Author: Notes: The RX_CONTEXT is a data structure to which
# additional information provided by the various mini redirectors need to be
# attached. This can be done in one of the following three ways
# 1) Allow for context pointers to be defined as part of the RX_CONTEXT which
# the mini redirectors can use to squirrel away their information. This
# implies that every time an RX_CONTEXT is allocated/destroyed the mini
# redirector has to perform an associated allocation/destruction. Since
# RX_CONTEXT's are created/destroyed in great numbers, this is not an
# acceptable solution. 2) The second approach consists of over allocating
# RX_CONTEXT's by a prespecified amount for each mini redirector which is
# then reserved for use by the mini redirector. Such an approach avoids the
# additional allocation/destruction but complicates the RX_CONTEXT management
# code in the wrapper. 3) The third approach ( the one that is implemented )
# consists of allocating a prespecfied area which is the same for all mini
# redirectors as part of each RX_CONTEXT. This is an unformatted area on top
# of which any desired structure can be imposed by the various mini
# redirectors. Such an approach overcomes the disadvantages associated with
# (1) and (2). All mini redirector writers must try and define the associated
# mini redirector contexts to fit into this area. Those mini redirectors who
# violate this rule will incur a significant performance penalty. - -
#

_RX_CONTEXT_STRUCT_DEFINED_ = None
if not defined(_RX_CONTEXT_STRUCT_DEFINED_):
    _RX_CONTEXT_STRUCT_DEFINED_ = 1

    RDBSS_TRACKER = 1

    if not defined(RDBSS_TRACKER):
        pass
    # END IF

    RX_TOPLEVELIRP_CONTEXT_SIGNATURE = 'LTxR'


    def RxInitializeTopLevelIrpContext(a, b, c):
        return __RxInitializeTopLevelIrpContext(a, b, c, 0)

    if defined(RDBSS_TRACKER):
        _RX_FCBTRACKER_CALLINFO._fields_ = [
            ('AcquireRelease', ULONG),
            ('SavedTrackerValue', USHORT),
            ('LineNumber', USHORT),
            ('FileName', PSZ),
            ('Flags', ULONG),
        ]
        RDBSS_TRACKER_HISTORY_SIZE = 32
    # END IF

    MRX_CONTEXT_FIELD_COUNT = 4
    MRX_CONTEXT_SIZE = ctypes.sizeof(PVOID) * MRX_CONTEXT_FIELD_COUNT


    # Define rxdriver dispatch routine type....almost all of the important
    # routine
    # will have this type.
    # NTSTATUS
    # (NTAPI *PRX_DISPATCH) (
    # IN PRX_CONTEXT RxContext,
    # IN PIRP Irp
    # );

    PRX_DISPATCH = NTAPI(NTSTATUS, PRX_CONTEXT, PIRP)

    # predeclare dfs types
    PDFS_NAME_CONTEXT = POINTER(_DFS_NAME_CONTEXT_)
    _NT_CREATE_PARAMETERS._fields_ = [
        ('DesiredAccess', ACCESS_MASK),
        ('AllocationSize', LARGE_INTEGER),
        ('FileAttributes', ULONG),
        ('ShareAccess', ULONG),
        ('Disposition', ULONG),
        ('CreateOptions', ULONG),
        ('SecurityContext', PIO_SECURITY_CONTEXT),
        ('ImpersonationLevel', SECURITY_IMPERSONATION_LEVEL),
        ('DfsContext', PVOID),
        ('DfsNameContext', PDFS_NAME_CONTEXT),
    ]
    _RX_CONTEXT._fields_ = [
        # the node type, size and reference count, aka standard header
        ('NodeTypeCode', NODE_TYPE_CODE),
        ('NodeByteSize', NODE_BYTE_SIZE),
        ('ReferenceCount', ULONG),
        # the list entry to wire the context to the list of active contexts
        ('ContextListEntry', LIST_ENTRY),
        # Major and minor function of the IRP associated with the context
        ('MajorFunction', UCHAR),
        ('MinorFunction', UCHAR),
        # to know whether to do asynchronous work or not
        ('PendingReturned', BOOLEAN),
        # indicates if the associated request is to be posted to a RDBSS
        # worker thread.
        ('PostRequest', BOOLEAN),
        # not currently used but could be used for local minis
        ('RealDevice', PDEVICE_OBJECT),
        # ptr to the originating Irp
        ('CurrentIrp', PIRP),
        # ptr to the IRP stack location
        ('CurrentIrpSp', PIO_STACK_LOCATION),
        # file object associated with the IRP
        ('pFcb', PMRX_FCB),
        ('pFobx', PMRX_FOBX),
        ('pRelevantSrvOpen', PMRX_SRV_OPEN),
        ('NonPagedFcb', PNON_PAGED_FCB),
        # device object calldown (not irpsp.....)
        ('RxDeviceObject', PRDBSS_DEVICE_OBJECT),
        # thread in which some processing associated with the context was done
        ('OriginalThread', PETHREAD),
        ('LastExecutionThread', PETHREAD),
        ('PVOID LockManagerContext', __volatile),
        # One word of the context is given to rdbss for dbg information
        ('RdbssDbgExtension', PVOID),
        ('ScavengerEntry', RX_SCAVENGER_ENTRY),
        # global serial number for this operation
        ('SerialNumber', ULONG),
        # of the same larger operation and (therefore) more cacheable
        ('FobxSerialNumber', ULONG),
        ('Flags', ULONG),
        ('FcbResourceAcquired', BOOLEAN),
        ('FcbPagingIoResourceAcquired', BOOLEAN),
        ('MustSucceedDescriptorNumber', UCHAR),
    ]


    class RX_CONTEXT_FLAGS(ENUM):
        RX_CONTEXT_FLAG_FROM_POOL = 0x00000001
        RX_CONTEXT_FLAG_WAIT = 0x00000002
        RX_CONTEXT_FLAG_WRITE_THROUGH = 0x00000004
        RX_CONTEXT_FLAG_FLOPPY = 0x00000008
        RX_CONTEXT_FLAG_RECURSIVE_CALL = 0x00000010
        RX_CONTEXT_FLAG_THIS_DEVICE_TOP_LEVEL = 0x00000020
        RX_CONTEXT_FLAG_DEFERRED_WRITE = 0x00000040
        RX_CONTEXT_FLAG_VERIFY_READ = 0x00000080
        RX_CONTEXT_FLAG_STACK_IO_CONTEZT = 0x00000100
        RX_CONTEXT_FLAG_IN_FSP = 0x00000200
        RX_CONTEXT_FLAG_CREATE_MAILSLOT = 0x00000400
        RX_CONTEXT_FLAG_MAILSLOT_REPARSE = 0x00000800
        RX_CONTEXT_FLAG_ASYNC_OPERATION = 0x00001000
        RX_CONTEXT_FLAG_NO_COMPLETE_FROM_FSP = 0x00002000
        RX_CONTEXT_FLAG_POST_ON_STABLE_CONDITION = 0x00004000
        RX_CONTEXT_FLAG_FSP_DELAYED_OVERFLOW_QUEUE = 0x00008000
        RX_CONTEXT_FLAG_FSP_CRITICAL_OVERFLOW_QUEUE = 0x00010000
        RX_CONTEXT_FLAG_MINIRDR_INVOKED = 0x00020000
        RX_CONTEXT_FLAG_WAITING_FOR_RESOURCE = 0x00040000
        RX_CONTEXT_FLAG_CANCELLED = 0x00080000
        RX_CONTEXT_FLAG_SYNC_EVENT_WAITERS = 0x00100000
        RX_CONTEXT_FLAG_NO_PREPOSTING_NEEDED = 0x00200000
        RX_CONTEXT_FLAG_BYPASS_VALIDOP_CHECK = 0x00400000
        RX_CONTEXT_FLAG_BLOCKED_PIPE_RESUME = 0x00800000
        RX_CONTEXT_FLAG_IN_SERIALIZATION_QUEUE = 0x01000000
        RX_CONTEXT_FLAG_NO_EXCEPTION_BREAKPOINT = 0x02000000
        RX_CONTEXT_FLAG_NEEDRECONNECT = 0x04000000
        RX_CONTEXT_FLAG_MUST_SUCCEED = 0x08000000
        RX_CONTEXT_FLAG_MUST_SUCCEED_NONBLOCKING = 0x10000000
        RX_CONTEXT_FLAG_MUST_SUCCEED_ALLOCATED = 0x20000000
        RX_CONTEXT_FLAG_MINIRDR_INITIATED = 0x80000000

    RX_CONTEXT_FLAG_FROM_POOL = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_FROM_POOL
    RX_CONTEXT_FLAG_WAIT = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_WAIT
    RX_CONTEXT_FLAG_WRITE_THROUGH = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_WRITE_THROUGH
    RX_CONTEXT_FLAG_FLOPPY = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_FLOPPY
    RX_CONTEXT_FLAG_RECURSIVE_CALL = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_RECURSIVE_CALL
    RX_CONTEXT_FLAG_THIS_DEVICE_TOP_LEVEL = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_THIS_DEVICE_TOP_LEVEL
    RX_CONTEXT_FLAG_DEFERRED_WRITE = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_DEFERRED_WRITE
    RX_CONTEXT_FLAG_VERIFY_READ = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_VERIFY_READ
    RX_CONTEXT_FLAG_STACK_IO_CONTEZT = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_STACK_IO_CONTEZT
    RX_CONTEXT_FLAG_IN_FSP = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_IN_FSP
    RX_CONTEXT_FLAG_CREATE_MAILSLOT = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_CREATE_MAILSLOT
    RX_CONTEXT_FLAG_MAILSLOT_REPARSE = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_MAILSLOT_REPARSE
    RX_CONTEXT_FLAG_ASYNC_OPERATION = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_ASYNC_OPERATION
    RX_CONTEXT_FLAG_NO_COMPLETE_FROM_FSP = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_NO_COMPLETE_FROM_FSP
    RX_CONTEXT_FLAG_POST_ON_STABLE_CONDITION = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_POST_ON_STABLE_CONDITION
    RX_CONTEXT_FLAG_FSP_DELAYED_OVERFLOW_QUEUE = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_FSP_DELAYED_OVERFLOW_QUEUE
    RX_CONTEXT_FLAG_FSP_CRITICAL_OVERFLOW_QUEUE = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_FSP_CRITICAL_OVERFLOW_QUEUE
    RX_CONTEXT_FLAG_MINIRDR_INVOKED = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_MINIRDR_INVOKED
    RX_CONTEXT_FLAG_WAITING_FOR_RESOURCE = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_WAITING_FOR_RESOURCE
    RX_CONTEXT_FLAG_CANCELLED = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_CANCELLED
    RX_CONTEXT_FLAG_SYNC_EVENT_WAITERS = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_SYNC_EVENT_WAITERS
    RX_CONTEXT_FLAG_NO_PREPOSTING_NEEDED = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_NO_PREPOSTING_NEEDED
    RX_CONTEXT_FLAG_BYPASS_VALIDOP_CHECK = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_BYPASS_VALIDOP_CHECK
    RX_CONTEXT_FLAG_BLOCKED_PIPE_RESUME = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_BLOCKED_PIPE_RESUME
    RX_CONTEXT_FLAG_IN_SERIALIZATION_QUEUE = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_IN_SERIALIZATION_QUEUE
    RX_CONTEXT_FLAG_NO_EXCEPTION_BREAKPOINT = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_NO_EXCEPTION_BREAKPOINT
    RX_CONTEXT_FLAG_NEEDRECONNECT = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_NEEDRECONNECT
    RX_CONTEXT_FLAG_MUST_SUCCEED = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_MUST_SUCCEED
    RX_CONTEXT_FLAG_MUST_SUCCEED_NONBLOCKING = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_MUST_SUCCEED_NONBLOCKING
    RX_CONTEXT_FLAG_MUST_SUCCEED_ALLOCATED = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_MUST_SUCCEED_ALLOCATED
    RX_CONTEXT_FLAG_MINIRDR_INITIATED = RX_CONTEXT_FLAGS.RX_CONTEXT_FLAG_MINIRDR_INITIATED
    RX_CONTEXT_PRESERVED_FLAGS = (
        RX_CONTEXT_FLAG_FROM_POOL |
        RX_CONTEXT_FLAG_MUST_SUCCEED_ALLOCATED |
        RX_CONTEXT_FLAG_IN_FSP
    )
    RX_CONTEXT_INITIALIZATION_FLAGS = (
        RX_CONTEXT_FLAG_WAIT |
        RX_CONTEXT_FLAG_MUST_SUCCEED |
        RX_CONTEXT_FLAG_MUST_SUCCEED_NONBLOCKING
    )


    class RX_CONTEXT_CREATE_FLAGS(ENUM):
        RX_CONTEXT_CREATE_FLAG_UNC_NAME = 0x1
        RX_CONTEXT_CREATE_FLAG_STRIPPED_TRAILING_BACKSLASH = 0x2
        RX_CONTEXT_CREATE_FLAG_ADDEDBACKSLASH = 0x4
        RX_CONTEXT_CREATE_FLAG_REPARSE = 0x8
        RX_CONTEXT_CREATE_FLAG_SPECIAL_PATH = 0x10

    RX_CONTEXT_CREATE_FLAG_UNC_NAME = RX_CONTEXT_CREATE_FLAGS.RX_CONTEXT_CREATE_FLAG_UNC_NAME
    RX_CONTEXT_CREATE_FLAG_STRIPPED_TRAILING_BACKSLASH = RX_CONTEXT_CREATE_FLAGS.RX_CONTEXT_CREATE_FLAG_STRIPPED_TRAILING_BACKSLASH
    RX_CONTEXT_CREATE_FLAG_ADDEDBACKSLASH = RX_CONTEXT_CREATE_FLAGS.RX_CONTEXT_CREATE_FLAG_ADDEDBACKSLASH
    RX_CONTEXT_CREATE_FLAG_REPARSE = RX_CONTEXT_CREATE_FLAGS.RX_CONTEXT_CREATE_FLAG_REPARSE
    RX_CONTEXT_CREATE_FLAG_SPECIAL_PATH = RX_CONTEXT_CREATE_FLAGS.RX_CONTEXT_CREATE_FLAG_SPECIAL_PATH


    class RX_CONTEXT_LOWIO_FLAGS(ENUM):
        RXCONTEXT_FLAG4LOWIO_PIPE_OPERATION = 0x1
        RXCONTEXT_FLAG4LOWIO_PIPE_SYNC_OPERATION = 0x2
        RXCONTEXT_FLAG4LOWIO_READAHEAD = 0x4
        RXCONTEXT_FLAG4LOWIO_THIS_READ_ENLARGED = 0x8
        RXCONTEXT_FLAG4LOWIO_THIS_IO_BUFFERED = 0x10
        RXCONTEXT_FLAG4LOWIO_LOCK_FCB_RESOURCE_HELD = 0x20
        RXCONTEXT_FLAG4LOWIO_LOCK_WAS_QUEUED_IN_LOCKMANAGER = 0x40
        RXCONTEXT_FLAG4LOWIO_THIS_IO_FAST = 0x80
        RXCONTEXT_FLAG4LOWIO_LOCK_OPERATION_COMPLETED = 0x100
        RXCONTEXT_FLAG4LOWIO_LOCK_BUFFERED_ON_ENTRY = 0x200
    if defined(__cplusplus):

        RXCONTEXT_FLAG4LOWIO_PIPE_OPERATION = RX_CONTEXT_LOWIO_FLAGS.RXCONTEXT_FLAG4LOWIO_PIPE_OPERATION
        RXCONTEXT_FLAG4LOWIO_PIPE_SYNC_OPERATION = RX_CONTEXT_LOWIO_FLAGS.RXCONTEXT_FLAG4LOWIO_PIPE_SYNC_OPERATION
        RXCONTEXT_FLAG4LOWIO_READAHEAD = RX_CONTEXT_LOWIO_FLAGS.RXCONTEXT_FLAG4LOWIO_READAHEAD
        RXCONTEXT_FLAG4LOWIO_THIS_READ_ENLARGED = RX_CONTEXT_LOWIO_FLAGS.RXCONTEXT_FLAG4LOWIO_THIS_READ_ENLARGED
        RXCONTEXT_FLAG4LOWIO_THIS_IO_BUFFERED = RX_CONTEXT_LOWIO_FLAGS.RXCONTEXT_FLAG4LOWIO_THIS_IO_BUFFERED
        RXCONTEXT_FLAG4LOWIO_LOCK_FCB_RESOURCE_HELD = RX_CONTEXT_LOWIO_FLAGS.RXCONTEXT_FLAG4LOWIO_LOCK_FCB_RESOURCE_HELD
        RXCONTEXT_FLAG4LOWIO_LOCK_WAS_QUEUED_IN_LOCKMANAGER = RX_CONTEXT_LOWIO_FLAGS.RXCONTEXT_FLAG4LOWIO_LOCK_WAS_QUEUED_IN_LOCKMANAGER
        RXCONTEXT_FLAG4LOWIO_THIS_IO_FAST = RX_CONTEXT_LOWIO_FLAGS.RXCONTEXT_FLAG4LOWIO_THIS_IO_FAST
        RXCONTEXT_FLAG4LOWIO_LOCK_OPERATION_COMPLETED = RX_CONTEXT_LOWIO_FLAGS.RXCONTEXT_FLAG4LOWIO_LOCK_OPERATION_COMPLETED
        RXCONTEXT_FLAG4LOWIO_LOCK_BUFFERED_ON_ENTRY = RX_CONTEXT_LOWIO_FLAGS.RXCONTEXT_FLAG4LOWIO_LOCK_BUFFERED_ON_ENTRY
    else:
        pass
    # END IF   __cplusplus

    # Macros used to control whether the wrapper breakpoints on an exception
    if DBG:
        def RxSaveAndSetExceptionNoBreakpointFlag(RXCONTEXT, OLDFLAG):
            # return { OLDFLAG = FlagOn( RxContext - >Flags, RX_CONTEXT_FLAG_NO_EXCEPTION_BREAKPOINT ); SetFlag( RxContext - >Flags, RX_CONTEXT_FLAG_NO_EXCEPTION_BREAKPOINT ); }
            pass

        def RxRestoreExceptionNoBreakpointFlag(RXCONTEXT, OLDFLAG):
            # return { ClearFlag( RxContext - >Flags, RX_CONTEXT_FLAG_NO_EXCEPTION_BREAKPOINT ); SetFlag( RxContext - >Flags, OLDFLAG ); }
            pass
    else:
        def RxSaveAndSetExceptionNoBreakpointFlag(RXCONTEXT,OLDFLAG):
            pass

        def RxRestoreExceptionNoBreakpointFlag(RXCONTEXT,OLDFLAG):
            pass

    # END IF
    # a macro used to ensure that a context hasn't been freed during a wait
    if DBG:
        def RxItsTheSameContext():
            # return {__RxItsTheSameContextRxContext,CapturedRxContextSerialNumber,__LINE__,__FILE__;}
            pass
    else:
        def RxItsTheSameContext():
            pass

    # END IF
    # Macros used in the RDBSS to wrap mini rdr calldowns
    def MINIRDR_CALL_THROUGH(STATUS, DISPATCH, FUNC, ARGLIST):
        # return { ASSERTDISPATCH; ASSERT( NodeTypeDISPATCH == RDBSS_NTC_MINIRDR_DISPATCH ); if (DISPATCH - >FUNC == NULL) { STATUS = STATUS_NOT_IMPLEMENTED; } else { RxDbgTrace(0, Dbg, ("MiniRdr Calldown - %s\n",#FUNC)); STATUS = DISPATCH - >FUNC ARGLIST; } }
        pass


    def MINIRDR_CALL(STATUS, CONTEXT, DISPATCH, FUNC, ARGLIST):
        return 1


    # VOID
    # RxWaitSync (
    # IN PRX_CONTEXT RxContext
    # )
    def RxWaitSync(RxContext):
        # return RxDbgTrace( + 1, Dbg, ("RxWaitSync, RxContext = %08lx\n", RxContext)); RxContext - >Flags | = RX_CONTEXT_FLAG_SYNC_EVENT_WAITERS; KeWaitForSingleObject( & RxContext - >SyncEvent, Executive, KernelMode, FALSE, NULL ); RxDbgTrace( - 1, Dbg, ("RxWaitSync - > VOID\n", 0 ))
        pass


    # VOID
    # RxSignalSynchronousWaiter (
    # IN PRX_CONTEXT RxContext
    # )
    def RxSignalSynchronousWaiter(RxContext):
        # return RxContext - >Flags & = ~RX_CONTEXT_FLAG_SYNC_EVENT_WAITERS; KeSetEvent( & RxContext - >SyncEvent, 0, FALSE)
        pass


    def RxInsertContextInSerializationQueue(SerializationQueue, RxContext):
        # return RxContext - >Flags | = RX_CONTEXT_FLAG_IN_SERIALIZATION_QUEUE; InsertTailList( SerializationQueue, & (RxContext - >RxContextSerializationQLinks ))
        pass


    # The following macros provide a mechanism for doing an en masse transfer
    # from one list onto another. This provides a powerful paradigm for dealing
    # with DPC level processing of lists.
    def RxTransferList(Destination, Source):
        # return if (IsListEmpty( Source )) { InitializeListHead( Destination ); } else { *Destination = *Source; Destination - >Flink - >Blink = Destination; Destination - >Blink - >Flink = Destination; InitializeListHead( Source ); }
        pass


    def RxTransferListWithMutex(Destination, Source, Mutex):
        # return { ExAcquireFastMutex Mutex ; RxTransferList Destination, Source ; ExReleaseFastMutex Mutex ; }
        pass

    rdbss = ctypes.windll.RDBSS


    # NTSTATUS
    # NTAPI
    # RxSetMinirdrCancelRoutine(
    # IN OUT PRX_CONTEXT RxContext,
    # IN PMRX_CALLDOWN MRxCancelRoutine
    # );
    RxSetMinirdrCancelRoutine = rdbss.RxSetMinirdrCancelRoutine
    RxSetMinirdrCancelRoutine.restype = NTAPI


    # VOID
    # NTAPI
    # RxInitializeContext(
    # IN PIRP Irp,
    # IN PRDBSS_DEVICE_OBJECT RxDeviceObject,
    # IN ULONG InitialContextFlags,
    # IN OUT PRX_CONTEXT RxContext
    # );
    RxInitializeContext = rdbss.RxInitializeContext
    RxInitializeContext.restype = NTAPI


    # PRX_CONTEXT
    # NTAPI
    # RxCreateRxContext(
    # IN PIRP Irp,
    # IN PRDBSS_DEVICE_OBJECT RxDeviceObject,
    # IN ULONG InitialContextFlags
    # );
    RxCreateRxContext = rdbss.RxCreateRxContext
    RxCreateRxContext.restype = NTAPI


    # VOID
    # NTAPI
    # RxPrepareContextForReuse(
    # IN OUT PRX_CONTEXT RxContext
    # );
    RxPrepareContextForReuse = rdbss.RxPrepareContextForReuse
    RxPrepareContextForReuse.restype = NTAPI


    # VOID
    # NTAPI
    # RxDereferenceAndDeleteRxContext_Real(
    # IN PRX_CONTEXT RxContext
    # );
    RxDereferenceAndDeleteRxContext_Real = (
        rdbss.RxDereferenceAndDeleteRxContext_Real
    )
    RxDereferenceAndDeleteRxContext_Real.restype = NTAPI


    # VOID
    # NTAPI
    # RxReinitializeContext(
    # IN OUT PRX_CONTEXT RxContext
    # );
    RxReinitializeContext = rdbss.RxReinitializeContext
    RxReinitializeContext.restype = NTAPI

    if DBG:
        def RxDereferenceAndDeleteRxContext(RXCONTEXT):
            return RxDereferenceAndDeleteRxContext_Real(RXCONTEXT)

    else:
        def RxDereferenceAndDeleteRxContext(RXCONTEXT):
            return RxDereferenceAndDeleteRxContext_Real(RXCONTEXT)


    # END IF
    # NTSTATUS
    # NTAPI
    # __RxSynchronizeBlockingOperations(
    # IN OUT PRX_CONTEXT RxContext,
    # IN PFCB Fcb,
    # IN OUT PLIST_ENTRY BlockingIoQ,
    # IN BOOLEAN DropFcbLock
    # );
    __RxSynchronizeBlockingOperations = rdbss.__RxSynchronizeBlockingOperations
    __RxSynchronizeBlockingOperations.restype = NTAPI


    def RxSynchronizeBlockingOperationsAndDropFcbLock(RXCONTEXT, FCB, IOQUEUE):
        return __RxSynchronizeBlockingOperations(RXCONTEXT, FCB, IOQUEUE, TRUE)


    def RxSynchronizeBlockingOperations(RXCONTEXT, FCB, IOQUEUE):
        return __RxSynchronizeBlockingOperations(RXCONTEXT, FCB, IOQUEUE, FALSE)

    # VOID
    # NTAPI
    # RxResumeBlockedOperations_Serially(
    # IN OUT PRX_CONTEXT RxContext,
    # IN OUT PLIST_ENTRY BlockingIoQ
    # );
    RxResumeBlockedOperations_Serially = rdbss.RxResumeBlockedOperations_Serially
    RxResumeBlockedOperations_Serially.restype = NTAPI

# END IF   _RX_CONTEXT_STRUCT_DEFINED_
