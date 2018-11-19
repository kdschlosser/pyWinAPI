import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _MRX_CREATENETROOT_CONTEXT(ctypes.Structure):
    pass


MRX_CREATENETROOT_CONTEXT = _MRX_CREATENETROOT_CONTEXT
PMRX_CREATENETROOT_CONTEXT = POINTER(_MRX_CREATENETROOT_CONTEXT)


class _MRX_SRVCALL_CALLBACK_CONTEXT(ctypes.Structure):
    pass


MRX_SRVCALL_CALLBACK_CONTEXT = _MRX_SRVCALL_CALLBACK_CONTEXT
PMRX_SRVCALL_CALLBACK_CONTEXT = POINTER(_MRX_SRVCALL_CALLBACK_CONTEXT)


class _MRX_SRVCALLDOWN_STRUCTURE(ctypes.Structure):
    pass


MRX_SRVCALLDOWN_STRUCTURE = _MRX_SRVCALLDOWN_STRUCTURE


class _LOWIO_LOCK_LIST(ctypes.Structure):
    pass


LOWIO_LOCK_LIST = _LOWIO_LOCK_LIST
PLOWIO_LOCK_LIST = POINTER(_LOWIO_LOCK_LIST)


class _XXCTL_LOWIO_COMPONENT(ctypes.Structure):
    pass


XXCTL_LOWIO_COMPONENT = _XXCTL_LOWIO_COMPONENT


class _LOWIO_CONTEXT(ctypes.Structure):
    pass


LOWIO_CONTEXT = _LOWIO_CONTEXT


class _MINIRDR_DISPATCH(ctypes.Structure):
    pass


MINIRDR_DISPATCH = _MINIRDR_DISPATCH
PMINIRDR_DISPATCH = POINTER(_MINIRDR_DISPATCH)


# /* + + Copyright (c) 1989 Microsoft Corporation Module Name: mrx.h Abstract:
# This module defines the interface between the MINI Redirectors and the
# RDBSS. The inteface is a dispatch table for the normal file system
# operations. In addition routines are provided for
# registrations/deregistration of mini redirectors. Author: Revision History:
# Notes: The interface definition between the mini redirectors and the wrapper
# consists of two parts, the data structures used and the dispatch vector. The
# data structures are defined in mrxfcb.h while the signatures of the various
# entries in the dispatch vector and the dispatch vector itself is defined in
# this file. - -

_RXMINIRDR_ = None
if not defined(_RXMINIRDR_):
    _RXMINIRDR_ = 1

    # RDBSS data structures shared with the mini redirectors
    from pyWinAPI.km.mrxfcb_h import * # NOQA


    # The following macros encapsulate commonly used operations in the mini
    # redirector.
    # These include setting the status/information associated with the
    # completion of
    # a request etc.
    # The following three macros are used for passing back operation status
    # from the
    # minirdr to the NT wrapper. information passed back is either the
    # open_action
    # for a create or the actual byte count or an operation. these should be
    # passed
    # back directly in the rxcontext.
    def RxSetIoStatusStatus(RXCONTEXT, STATUS):
        RXCONTEXT.CurrentIrp.IoStatus.Status = STATUS


    def RxSetIoStatusInfo(RXCONTEXT, INFORMATION):
        RXCONTEXT.CurrentIrp.IoStatus.Information = INFORMATION


    def RxGetIoStatusInfo(RXCONTEXT):
        return RXCONTEXT.CurrentIrp.IoStatus.Information


    def RxShouldPostCompletion():
        return KeGetCurrentIrql() >= DISPATCH_LEVEL


    # The mini rdr's register/unregister with the RDBSS whenever they are
    # loaded/unloaded.
    # The registartion process is a two way hand shake in which the mini rdr
    # informs the RDBSS
    # by invoking the registartion routine. The RDBSS completes the
    # initialization by invoking
    # the Start routine in the dispatch vector.
    RX_REGISTERMINI_FLAG_DONT_PROVIDE_UNCS = 0x00000001
    RX_REGISTERMINI_FLAG_DONT_PROVIDE_MAILSLOTS = 0x00000002
    RX_REGISTERMINI_FLAG_DONT_INIT_DRIVER_DISPATCH = 0x00000004
    RX_REGISTERMINI_FLAG_DONT_INIT_PREFIX_N_SCAVENGER = 0x00000008
    RX_REGISTERMINI_FLAG_DONT_USE_VISTA_REDIRECTOR = 0x00000010
    rdbss = ctypes.windll.RDBSS


    # NTSTATUS
    # NTAPI
    # RxRegisterMinirdr(
    # OUT PRDBSS_DEVICE_OBJECT *DeviceObject, // the deviceobject that was created
    # IN OUT PDRIVER_OBJECT DriverObject, // the minirdr driver object
    # IN PMINIRDR_DISPATCH MrdrDispatch, // the mini rdr dispatch vector
    # IN ULONG Controls,
    # IN PUNICODE_STRING DeviceName,
    # IN ULONG DeviceExtensionSize,
    # IN DEVICE_TYPE DeviceType,
    # IN ULONG DeviceCharacteristics
    # );
    RxRegisterMinirdr = rdbss.RxRegisterMinirdr
    RxRegisterMinirdr.restype = NTAPI


    def RxFillAndInstallFastIoDispatch(__devobj, __fastiodisp):
        return 1

    # NTSTATUS
    # RxStartMinirdr(
    # IN PRX_CONTEXT RxContext,
    # OUT PBOOLEAN PostToFsp
    # );
    RxStartMinirdr = rdbss.RxStartMinirdr
    RxStartMinirdr.restype = NTSTATUS


    # NTSTATUS
    # RxStopMinirdr(
    # IN PRX_CONTEXT RxContext,
    # OUT PBOOLEAN PostToFsp
    # );
    RxStopMinirdr = rdbss.RxStopMinirdr
    RxStopMinirdr.restype = NTSTATUS


    # NTSTATUS
    # RxSetDomainForMailslotBroadcast(
    # IN PUNICODE_STRING DomainName
    # );
    RxSetDomainForMailslotBroadcast = rdbss.RxSetDomainForMailslotBroadcast
    RxSetDomainForMailslotBroadcast.restype = NTSTATUS


    # NTSTATUS
    # RxFsdDispatch(
    # IN PRDBSS_DEVICE_OBJECT RxDeviceObject,
    # IN PIRP Irp
    # );
    RxFsdDispatch = rdbss.RxFsdDispatch
    RxFsdDispatch.restype = NTSTATUS

    # NTSTATUS
    # (NTAPI *PMRX_CALLDOWN) (
    # IN OUT PRX_CONTEXT RxContext
    # )

    PMRX_CALLDOWN = NTAPI(NTSTATUS, PRX_CONTEXT)

    # NTSTATUS
    # (NTAPI *PMRX_CALLDOWN_CTX) (
    # IN OUT PRX_CONTEXT RxContext,
    # IN OUT PRDBSS_DEVICE_OBJECT RxDeviceObject
    # )

    PMRX_CALLDOWN_CTX = NTAPI(NTSTATUS, PRX_CONTEXT, PRDBSS_DEVICE_OBJECT)

    # NTSTATUS
    # (NTAPI *PMRX_CHKDIR_CALLDOWN) (
    # IN OUT PRX_CONTEXT RxContext
    # IN PUNICODE_STRING DirectoryName
    # )

    PMRX_CHKDIR_CALLDOWN = NTAPI(NTSTATUS, PRX_CONTEXT, PUNICODE_STRING)

    # NTSTATUS
    # (NTAPI *PMRX_CHKFCB_CALLDOWN) (
    # IN PFCB Fcb1
    # IN PFCB Fcb2
    # )
    PMRX_CHKFCB_CALLDOWN = NTAPI(NTSTATUS, PFCB, PFCB)

    # The two important abstractions used in the interface between the mini
    # rdr and RDBSS are
    # Server Calls and Net Roots. The former corresponds to the context
    # associated with a
    # server with which a connection has been established and the later
    # corresponds to a
    # share on a server
    # ( This could also be viewed as a portion of the name space which has
    # been claimed by a mini rdr).
    # The creation of Server calls and net roots typically involve atleast one
    # network round trip.
    # In order to provide for asynchronous operations to continue these
    # operations are modelled
    # as a two phase activity. Each calldown to a mini rdr for creating a
    # server call and net root is
    # accompanied by a callup from the mini rdr to the RDBSS notifying with
    # the completion status
    # of the request. Currently these are synchronousnot
    # The creation of Srv calls is further complicated by the fact that the
    # RDBSS has to choose
    # from a number of mini rdr's to establish a connection with a server. In
    # order to provide
    # the RDBSS with maximum flexibility in choosing the mini rdr's that it
    # wishes to deploy the
    # creation of server calls involves a third phase in which the RDBSS
    # notifies the mini rdr of
    # a winner. All the losing mini rdrs destroy the associated context.
    class _RX_BLOCK_CONDITION(ENUM):
        Condition_Uninitialized = 0
        Condition_InTransition = 1
        Condition_Closing = 2
        Condition_Good = 3
        Condition_Bad = 4
        Condition_Closed = 5

    RX_BLOCK_CONDITION = _RX_BLOCK_CONDITION
    PRX_BLOCK_CONDITION = POINTER(_RX_BLOCK_CONDITION)


    def StableCondition(X):
        return X >= RX_BLOCK_CONDITION.Condition_Good


    # The routine for notifying the RDBSS about the completion status of the
    # NetRoot creation
    # request.
    # VOID
    # (NTAPI *PMRX_NETROOT_CALLBACK) (
    # IN OUT PMRX_CREATENETROOT_CONTEXT CreateContext
    # )
    PMRX_NETROOT_CALLBACK = NTAPI(VOID, PMRX_CREATENETROOT_CONTEXT)

    # this routine allows the minirdr to specify the netrootname. NetRootName
    # and RestOfName are set
    # to point to the appropriate places within FilePathName. SrvCall is used
    # to find the lengthof the srvcallname.
    # VOID
    # (NTAPI *PMRX_EXTRACT_NETROOT_NAME) (
    # IN PUNICODE_STRING FilePathName
    # IN PMRX_SRV_CALL SrvCall
    # OUT PUNICODE_STRING NetRootName
    # OUT PUNICODE_STRING RestOfName OPTIONAL
    # )
    PMRX_EXTRACT_NETROOT_NAME = NTAPI(
        VOID,
        PUNICODE_STRING,
        PMRX_SRV_CALL,
        PUNICODE_STRING,
        PUNICODE_STRING
    )

    # The resumption context for the RDBSS.
    _MRX_CREATENETROOT_CONTEXT._fields_ = [
        ('RxContext', PRX_CONTEXT),
        ('pVNetRoot', PV_NET_ROOT),
        ('FinishEvent', KEVENT),
        ('VirtualNetRootStatus', NTSTATUS),
        ('NetRootStatus', NTSTATUS),
        ('WorkQueueItem', RX_WORK_QUEUE_ITEM),
        ('Callback', PMRX_NETROOT_CALLBACK),
    ]


    # the calldown from RDBSS to the mini rdr for creating a netroot.
    # NTSTATUS
    # (NTAPI *PMRX_CREATE_V_NET_ROOT) (
    # IN OUT PMRX_CREATENETROOT_CONTEXT Context
    # )
    PMRX_CREATE_V_NET_ROOT = NTAPI(NTSTATUS, PMRX_CREATENETROOT_CONTEXT)

    # the calldown for querying a net root state.
    # NTSTATUS
    # (NTAPI *PMRX_UPDATE_NETROOT_STATE) (
    # IN OUT PMRX_NET_ROOT NetRoot
    # )
    PMRX_UPDATE_NETROOT_STATE = NTAPI(NTSTATUS, PMRX_NET_ROOT)


    # The resumption context for the RDBSS.
    _MRX_SRVCALL_CALLBACK_CONTEXT._fields_ = [
        # could be computed
        ('SrvCalldownStructure', POINTER(_MRX_SRVCALLDOWN_STRUCTURE)),
        ('CallbackContextOrdinal', ULONG),
        ('RxDeviceObject', PRDBSS_DEVICE_OBJECT),
        ('Status', NTSTATUS),
        ('RecommunicateContext', PVOID),
    ]


    # The routine for notifying the RDBSS about the completion status of the
    # SrvCall creation
    # request.
    (NTAPI *PMRX_SRVCALL_CALLBACK) (
            IN OUT PMRX_SRVCALL_CALLBACK_CONTEXT Context
            ) = VOID


    # The context passed from the RDBSS to the mini rdr for creating a server
    # call.
    _MRX_SRVCALLDOWN_STRUCTURE._fields_ = [
        ('FinishEvent', KEVENT),
        ('SrvCalldownList', LIST_ENTRY),
        ('RxContext', PRX_CONTEXT),
        ('SrvCall', PMRX_SRV_CALL),
        ('CallBack', PMRX_SRVCALL_CALLBACK),
        ('CalldownCancelled', BOOLEAN),
        ('NumberRemaining', ULONG),
        ('NumberToWait', ULONG),
        ('BestFinisherOrdinal', ULONG),
        ('BestFinisher', PRDBSS_DEVICE_OBJECT),
        ('CallbackContexts', MRX_SRVCALL_CALLBACK_CONTEXT * 1),
    ]


    # the calldown from the RDBSS to the mini rdr for creating a server call
    (NTAPI *PMRX_CREATE_SRVCALL) (
            IN OUT PMRX_SRV_CALL SrvCall = NTSTATUS
    IN OUT PMRX_SRVCALL_CALLBACK_CONTEXT SrvCallCallBackContext
            ) = NTSTATUS


    # the calldown from the RDBSS to the mini rdr for notifying the mini rdr's
    # of the winner.
    (NTAPI *PMRX_SRVCALL_WINNER_NOTIFY)(
            IN OUT PMRX_SRV_CALL SrvCall = NTSTATUS
    IN BOOLEAN ThisMinirdrIsTheWinner = NTSTATUS
    IN OUT PVOID RecommunicateContext
            ) = NTSTATUS


    # The prototypes for calldown routines relating to various file system
    # operations
    (NTAPI *PMRX_NEWSTATE_CALLDOWN) (
            IN OUT PVOID Context
            ) = VOID
    (NTAPI *PMRX_DEALLOCATE_FOR_FCB) (
            IN OUT PMRX_FCB Fcb
            ) = NTSTATUS
    (NTAPI *PMRX_DEALLOCATE_FOR_FOBX) (
            IN OUT PMRX_FOBX Fobx
            ) = NTSTATUS
    (NTAPI *PMRX_IS_LOCK_REALIZABLE) (
            IN OUT PMRX_FCB Fcb = NTSTATUS
    IN PLARGE_INTEGER ByteOffset = NTSTATUS
    IN PLARGE_INTEGER Length = NTSTATUS
    IN ULONG LowIoLockFlags
            ) = NTSTATUS
    (NTAPI *PMRX_FORCECLOSED_CALLDOWN) (
            IN OUT PMRX_SRV_OPEN SrvOpen
            ) = NTSTATUS
    (NTAPI *PMRX_FINALIZE_SRVCALL_CALLDOWN) (
            IN OUT PMRX_SRV_CALL SrvCall = NTSTATUS
    IN BOOLEAN Force
            ) = NTSTATUS
    (NTAPI *PMRX_FINALIZE_V_NET_ROOT_CALLDOWN) (
            IN OUT PMRX_V_NET_ROOT VirtualNetRoot = NTSTATUS
    IN PBOOLEAN Force
            ) = NTSTATUS
    (NTAPI *PMRX_FINALIZE_NET_ROOT_CALLDOWN) (
            IN OUT PMRX_NET_ROOT NetRoot = NTSTATUS
    IN PBOOLEAN Force
            ) = NTSTATUS
    (NTAPI *PMRX_EXTENDFILE_CALLDOWN) (
            IN OUT PRX_CONTEXT RxContext = ULONG
    IN OUT PLARGE_INTEGER NewFileSize = ULONG
    OUT PLARGE_INTEGER NewAllocationSize
            ) = ULONG
    (*PRX_LOCK_ENUMERATOR) (
            IN OUT PMRX_SRV_OPEN SrvOpen = BOOLEAN
    IN OUT PVOID *ContinuationHandle = BOOLEAN
    OUT PLARGE_INTEGER FileOffset = BOOLEAN
    OUT PLARGE_INTEGER LockRange = BOOLEAN
    OUT PBOOLEAN IsLockExclusive
            ) = BOOLEAN
    (NTAPI *PMRX_CHANGE_BUFFERING_STATE_CALLDOWN) (
            IN OUT PRX_CONTEXT RxContext = NTSTATUS
    IN OUT PMRX_SRV_OPEN SrvOpen = NTSTATUS
    IN PVOID MRxContext
            ) = NTSTATUS
    (NTAPI *PMRX_PREPARSE_NAME) (
            IN OUT PRX_CONTEXT RxContext = NTSTATUS
    IN PUNICODE_STRING Name
            ) = NTSTATUS
    (NTAPI *PMRX_GET_CONNECTION_ID) (
            IN OUT PRX_CONTEXT RxContext = NTSTATUS
    IN OUT PRX_CONNECTION_ID UniqueId
            ) = NTSTATUS


    # Buffering state/Policy management TBD
    class _MINIRDR_BUFSTATE_COMMANDS(ENUM):
        MRDRBUFSTCMD__COMMAND_FORCEPURGE0 = 1
        MRDRBUFSTCMD__1 = 2
        MRDRBUFSTCMD__2 = 3
        MRDRBUFSTCMD__3 = 4
        MRDRBUFSTCMD__4 = 5
        MRDRBUFSTCMD__5 = 6
        MRDRBUFSTCMD__6 = 7
        MRDRBUFSTCMD__7 = 8
        MRDRBUFSTCMD__8 = 9
        MRDRBUFSTCMD__9 = 10
        MRDRBUFSTCMD__10 = 11
        MRDRBUFSTCMD__11 = 12
        MRDRBUFSTCMD__12 = 13
        MRDRBUFSTCMD__13 = 14
        MRDRBUFSTCMD__14 = 15
        MRDRBUFSTCMD__15 = 16
        MRDRBUFSTCMD__16 = 17
        MRDRBUFSTCMD__17 = 18
        MRDRBUFSTCMD__18 = 19
        MRDRBUFSTCMD__19 = 20
        MRDRBUFSTCMD__20 = 21
        MRDRBUFSTCMD__21 = 22
        MRDRBUFSTCMD__22 = 23
        MRDRBUFSTCMD__23 = 24
        MRDRBUFSTCMD__24 = 25
        MRDRBUFSTCMD__25 = 26
        MRDRBUFSTCMD__26 = 27
        MRDRBUFSTCMD__27 = 28
        MRDRBUFSTCMD__28 = 29
        MRDRBUFSTCMD__29 = 30
        MRDRBUFSTCMD__30 = 31
        MRDRBUFSTCMD__31 = 32
        MRDRBUFSTCMD_MAXXX = 33

    MINIRDR_BUFSTATE_COMMANDS = _MINIRDR_BUFSTATE_COMMANDS
    MINIRDR_BUFSTATE_COMMAND_FORCEPURGE = 0x00000001
    MINIRDR_BUFSTATE_COMMAND_MASK = (MINIRDR_BUFSTATE_COMMAND_FORCEPURGE)
    (NTAPI *PMRX_COMPUTE_NEW_BUFFERING_STATE) (
            IN OUT PMRX_SRV_OPEN SrvOpen = NTSTATUS
    IN PVOID MRxContext = NTSTATUS
    OUT PULONG NewBufferingState
            ) = NTSTATUS


    class _LOWIO_OPS(ENUM):
        LOWIO_OP_READ = 0
        LOWIO_OP_WRITE = 1
        LOWIO_OP_SHAREDLOCK = 2
        LOWIO_OP_EXCLUSIVELOCK = 3
        LOWIO_OP_UNLOCK = 4
        LOWIO_OP_UNLOCK_MULTIPLE = 5
        LOWIO_OP_FSCTL = 6
        LOWIO_OP_IOCTL = 7
        LOWIO_OP_NOTIFY_CHANGE_DIRECTORY = 8
        LOWIO_OP_CLEAROUT = 9
        LOWIO_OP_MAXIMUM = 10

    LOWIO_OPS = _LOWIO_OPS
    (NTAPI *PLOWIO_COMPLETION_ROUTINE) (
            IN PRX_CONTEXT RxContext
            ) = NTSTATUS
    RXVBO = LONGLONG


    # we may, at some point, want a smarter implementation of this. we don't
    # statically allocate the first
    # element because that would make unlock behind much harder.
    _LOWIO_LOCK_LIST._fields_ = [
        ('Next', POINTER(_LOWIO_LOCK_LIST)),
        ('LockNumber', ULONG),
        ('ByteOffset', RXVBO),
        ('Length', LONGLONG),
        ('ExclusiveLock', BOOLEAN),
        ('Key', ULONG),
    ]
    ) = _RX_CONTEXT *RxContext
    _XXCTL_LOWIO_COMPONENT._fields_ = [
        ('Flags', ULONG),
    ]
    _LOWIO_CONTEXT._fields_ = [
        # paddingnot
        ('Operation', USHORT),
        ('Flags', USHORT),
        ('CompletionRoutine', PLOWIO_COMPLETION_ROUTINE),
        ('Resource', PERESOURCE),
        ('ResourceThreadId', ERESOURCE_THREAD),
    ]
    LOWIO_CONTEXT_FLAG_SYNCCALL = 0x0001    # this is set if lowiocompletion is called from lowiosubmit
    # WRAPPER INTERNAL: on NT, it means the unlock routine add unlocks to the
    # list
    LOWIO_CONTEXT_FLAG_SAVEUNLOCKS = 0x0002
    # WRAPPER INTERNAL: on NT, it means read and write routines generate dbg
    # output
    LOWIO_CONTEXT_FLAG_LOUDOPS = 0x0004
    LOWIO_CONTEXT_FLAG_CAN_COMPLETE_AT_DPC_LEVEL = 0x0008    # WRAPPER INTERNAL: on NT, it means the completion routine maybe can
    # complete when called at DPC. otherwise it cannnot. currently
    # none can.
    LOWIO_READWRITEFLAG_PAGING_IO = 0x01
    LOWIO_READWRITEFLAG_EXTENDING_FILESIZE = 0x02
    LOWIO_READWRITEFLAG_EXTENDING_VDL = 0x04
    # these must match the SL_ values in io.h (ntifs.h) since the flags field
    # is just copied
    LOWIO_LOCKSFLAG_FAIL_IMMEDIATELY = 0x01
    LOWIO_LOCKSFLAG_EXCLUSIVELOCK = 0x02
    if LOWIO_LOCKSFLAG_FAIL_IMMEDIATELY != SL_FAIL_IMMEDIATELY:
        pass
    # END IF
    if LOWIO_LOCKSFLAG_EXCLUSIVELOCK != SL_EXCLUSIVE_LOCK:
        pass
    # END IF
    # The six important data structures
    # (SRV_CALL,NET_ROOT,V_NET_ROOT,FCB,SRV_OPEN and
    # FOBX) that are an integral part of the mini rdr architecture have a corresponding
    #
    # counterpart in every mini rdr implementation. In order to provide
    # maximal flexibility
    # and at the same time enhance performance the sizes and the desired
    # allocation
    # behaviour are communicated at the registration time of a mini rdr.
    # There is no single way in which these extensions can be managed which
    # will
    # address the concerns of flexibility as well as performance. The solution
    # adopted
    # in the current architecture that meets the dual goals in most cases. The
    # solution
    # and the rationale is as follows ...
    # Each mini rdr implementor specifies the size of the data structure
    # extensions
    # alongwith a flag specfying if the allocation/free of the extensions are
    # to be
    # managed by the wrapper.
    # In all those cases where a one to one relationship exists between the
    # wrapper
    # data structure and the corresponding mini rdr counterpart specifying the
    # flag
    # results in maximal performance gains. There are a certain data
    # structures for
    # which many instances of a wrapper data structure map onto the same
    # extension in
    # the mini redirector. In such cases the mini rdr implementor will be
    # better off
    # managing the allocation/deallocation of the data structure extension
    # without the
    # intervention of the wrapper.
    # Irrespective of the mechanism choosen the convention is to always
    # associate the
    # extension with the Context field in the corresponding RDBSS data
    # structure.
    # not not not NO EXCEPTIONSnot not not
    # The remaining field in all the RDBSS data structures, i.e., Context2 is
    # left to
    # the discretion og the mini rdr implementor.
    # The SRV_CALL extension is not handled currently. This is because of
    # further fixes
    # required in RDBSS w.r.t the mecahsnism used to select the mini rdr and
    # to allow several
    # minis to share the srvcall.
    # Please do not use it till further notice; rather, the mini should manage
    # its own srcall
    # storage. There is a finalization calldown that assists in this endeavor.
    RDBSS_MANAGE_SRV_CALL_EXTENSION = 0x1
    RDBSS_MANAGE_NET_ROOT_EXTENSION = 0x2
    RDBSS_MANAGE_V_NET_ROOT_EXTENSION = 0x4
    RDBSS_MANAGE_FCB_EXTENSION = 0x8
    RDBSS_MANAGE_SRV_OPEN_EXTENSION = 0x10
    RDBSS_MANAGE_FOBX_EXTENSION = 0x20
    RDBSS_NO_DEFERRED_CACHE_READAHEAD = 0x1000


    _MINIRDR_DISPATCH._fields_ = [
        # Normal Header
        ('NodeTypeCode', NODE_TYPE_CODE),
        ('NodeByteSize', NODE_BYTE_SIZE),
        # and various other per - minirdr policies
        ('MRxFlags', ULONG),
        # size of the SRV_CALL extensions
        ('MRxSrvCallSize', ULONG),
        # size of the NET_ROOT extensions
        ('MRxNetRootSize', ULONG),
        # size of the V_NET_ROOT extensions
        ('MRxVNetRootSize', ULONG),
        # size of FCB extensions
        ('MRxFcbSize', ULONG),
        # size of SRV_OPEN extensions
        ('MRxSrvOpenSize', ULONG),
        # size of FOBX extensions
        ('MRxFobxSize', ULONG),
        # Call downs for starting/stopping the mini rdr
        ('MRxStart', PMRX_CALLDOWN_CTX),
        ('MRxStop', PMRX_CALLDOWN_CTX),
        # Call down for cancelling outstanding requests
        ('MRxCancel', PMRX_CALLDOWN),
        # Call downs related to creating/opening/closing file system objects
        ('MRxCreate', PMRX_CALLDOWN),
        ('MRxCollapseOpen', PMRX_CALLDOWN),
        ('MRxShouldTryToCollapseThisOpen', PMRX_CALLDOWN),
        ('MRxFlush', PMRX_CALLDOWN),
        ('MRxZeroExtend', PMRX_CALLDOWN),
        ('MRxTruncate', PMRX_CALLDOWN),
        ('MRxCleanupFobx', PMRX_CALLDOWN),
        ('MRxCloseSrvOpen', PMRX_CALLDOWN),
        ('MRxDeallocateForFcb', PMRX_DEALLOCATE_FOR_FCB),
        ('MRxDeallocateForFobx', PMRX_DEALLOCATE_FOR_FOBX),
        ('MRxIsLockRealizable', PMRX_IS_LOCK_REALIZABLE),
        ('MRxForceClosed', PMRX_FORCECLOSED_CALLDOWN),
        ('MRxAreFilesAliased', PMRX_CHKFCB_CALLDOWN),
        # the normal srvcall/netroot interface
        ('MRxOpenPrintFile', PMRX_CALLDOWN),
        ('MRxClosePrintFile', PMRX_CALLDOWN),
        ('MRxWritePrintFile', PMRX_CALLDOWN),
        ('MRxEnumeratePrintQueue', PMRX_CALLDOWN),
        # call downs related to unsatisfied requests, i.e., time outs
        ('MRxClosedSrvOpenTimeOut', PMRX_CALLDOWN),
        ('MRxClosedFcbTimeOut', PMRX_CALLDOWN),
        # call downs related to query/set information on file system objects
        ('MRxQueryDirectory', PMRX_CALLDOWN),
        ('MRxQueryFileInfo', PMRX_CALLDOWN),
        ('MRxSetFileInfo', PMRX_CALLDOWN),
        ('MRxSetFileInfoAtCleanup', PMRX_CALLDOWN),
        ('MRxQueryEaInfo', PMRX_CALLDOWN),
        ('MRxSetEaInfo', PMRX_CALLDOWN),
        ('MRxQuerySdInfo', PMRX_CALLDOWN),
        ('MRxSetSdInfo', PMRX_CALLDOWN),
        ('MRxQueryQuotaInfo', PMRX_CALLDOWN),
        ('MRxSetQuotaInfo', PMRX_CALLDOWN),
        ('MRxQueryVolumeInfo', PMRX_CALLDOWN),
        ('MRxSetVolumeInfo', PMRX_CALLDOWN),
        ('MRxIsValidDirectory', PMRX_CHKDIR_CALLDOWN),
        # call downs related to buffer management
        ('MRxComputeNewBufferingState', PMRX_COMPUTE_NEW_BUFFERING_STATE),
        # call downs related to Low I/O management
        # (reads/writes on file system objects)
        ('MRxLowIOSubmit', PMRX_CALLDOWN * LOWIO_OP_MAXIMUM + 1),
        ('MRxExtendForCache', PMRX_EXTENDFILE_CALLDOWN),
        ('MRxExtendForNonCache', PMRX_EXTENDFILE_CALLDOWN),
        ('MRxCompleteBufferingStateChangeRequest', PMRX_CHANGE_BUFFERING_STATE_CALLDOWN),
        # call downs related to name space management
        ('MRxCreateVNetRoot', PMRX_CREATE_V_NET_ROOT),
        ('MRxFinalizeVNetRoot', PMRX_FINALIZE_V_NET_ROOT_CALLDOWN),
        ('MRxFinalizeNetRoot', PMRX_FINALIZE_NET_ROOT_CALLDOWN),
        ('MRxUpdateNetRootState', PMRX_UPDATE_NETROOT_STATE),
        ('MRxExtractNetRootName', PMRX_EXTRACT_NETROOT_NAME),
        # call downs related to establishing connections with servers
        ('MRxCreateSrvCall', PMRX_CREATE_SRVCALL),
        ('MRxCancelCreateSrvCall', PMRX_CREATE_SRVCALL),
        ('MRxSrvCallWinnerNotify', PMRX_SRVCALL_WINNER_NOTIFY),
        ('MRxFinalizeSrvCall', PMRX_FINALIZE_SRVCALL_CALLDOWN),
        ('MRxDevFcbXXXControlFile', PMRX_CALLDOWN),
        # Allow a client to preparse the name
        ('MRxPreparseName', PMRX_PREPARSE_NAME),
        # call down for controlling multi - plexing
        ('MRxGetConnectionId', PMRX_GET_CONNECTION_ID),
        # scavenger time interval (in seconds)
        ('ScavengerTimeout', ULONG),
    ]
# END IF   _RXMINIRDR_
