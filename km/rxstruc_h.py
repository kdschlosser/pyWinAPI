import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _RDBSS_EXPORTS(ctypes.Structure):
    pass


RDBSS_EXPORTS = _RDBSS_EXPORTS
PRDBSS_EXPORTS = POINTER(_RDBSS_EXPORTS)


class _RDBSS_DATA(ctypes.Structure):
    pass


RDBSS_DATA = _RDBSS_DATA


class _RDBSS_STARTSTOP_CONTEXT_(ctypes.Structure):
    pass


RDBSS_STARTSTOP_CONTEXT = _RDBSS_STARTSTOP_CONTEXT_
PRDBSS_STARTSTOP_CONTEXT = POINTER(_RDBSS_STARTSTOP_CONTEXT_)


class _MRX_CALLDOWN_COMPLETION_CONTEXT_(ctypes.Structure):
    pass


MRX_CALLDOWN_COMPLETION_CONTEXT = _MRX_CALLDOWN_COMPLETION_CONTEXT_
PMRX_CALLDOWN_COMPLETION_CONTEXT = POINTER(_MRX_CALLDOWN_COMPLETION_CONTEXT_)


class _MRX_CALLDOWN_CONTEXT_(ctypes.Structure):
    pass


MRX_CALLDOWN_CONTEXT = _MRX_CALLDOWN_CONTEXT_
PMRX_CALLDOWN_CONTEXT = POINTER(_MRX_CALLDOWN_CONTEXT_)


class _RX_DISPATCHER_CONTEXT_(ctypes.Structure):
    pass


RX_DISPATCHER_CONTEXT = _RX_DISPATCHER_CONTEXT_
PRX_DISPATCHER_CONTEXT = POINTER(_RX_DISPATCHER_CONTEXT_)


class _RDBSS_DEVICE_OBJECT(ctypes.Structure):
    pass


RDBSS_DEVICE_OBJECT = _RDBSS_DEVICE_OBJECT
PRDBSS_DEVICE_OBJECT = POINTER(_RDBSS_DEVICE_OBJECT)


# /* + + Copyright (c) 1989 Microsoft Corporation Module Name: RxStruc.h
# Abstract: This module defines the data structures that make up the major
# internal part of the Rx file system. Author: - -
_RDBSSSTRUC_ = None
if not defined(_RDBSSSTRUC_):
    _RDBSSSTRUC_ = 1

    from pyWinAPI.km.prefix_h import * # NOQA
    from pyWinAPI.km.lowio_h import * # NOQA

    # scavenger related definitions.
    from pyWinAPI.km.scavengr_h import * # NOQA
    from pyWinAPI.km.rxcontx_h import * # NOQA
    from pyWinAPI.km.mrx_h import * # NOQA
    from pyWinAPI.km.fcb_h import * # NOQA

    # define our byte offsets to be the full 64 bits
    RXVBO = LONGLONG

    if 0:
        # Define who many freed structures we are willing to keep around
        FREE_FOBX_SIZE = 8
        FREE_FCB_SIZE = 8
        FREE_NON_PAGED_FCB_SIZE = 8
        FREE_128_BYTE_SIZE = 16
        FREE_256_BYTE_SIZE = 16
        FREE_512_BYTE_SIZE = 16
    # END IF    0

    # We will use both a common and private dispatch tables on a per FCB basis
    # to (a) get
    # some encapsulation and (b) [less important] go a little faster. The
    # driver table then gets
    # optimized for the most common case. Right now we just use the common
    # dispatch...later and
    # Eventually, all the FCBs will have pointers to optimized dispatch tables.
    # used to synchronize access to rxcontxs and structures
    _RDBSS_EXPORTS._fields_ = [
        ('pRxStrucSupSpinLock', PRX_SPIN_LOCK),
        ('pRxDebugTraceIndent', PLONG),
    ]

    # this type is used with table locks to track whether or not the lock
    # should be released
    class _LOCK_HOLDING_STATE(ENUM):
        LHS_LockNotHeld = 1
        LHS_SharedLockHeld = 2
        LHS_ExclusiveLockHeld = 3

    LOCK_HOLDING_STATE = _LOCK_HOLDING_STATE
    PLOCK_HOLDING_STATE = POINTER(_LOCK_HOLDING_STATE)

    # The RDBSS_DATA record is the top record in the Rx file system in - memory
    # data structure. This structure must be allocated from non - paged pool.
    _RDBSS_DATA._fields_ = [
        # The type and size of this record (must be RDBSS_NTC_DATA_HEADER)
        ('NodeTypeCode', NODE_TYPE_CODE),
        ('NodeByteSize', NODE_BYTE_SIZE),
        # The Driver object we were initialized with
        ('DriverObject', PDRIVER_OBJECT),
        # Mini Rdr registration related fields
        ('LONG NumberOfMinirdrsStarted', __volatile),
        ('MinirdrRegistrationMutex', FAST_MUTEX),
        # protected by the mutex
        ('RegisteredMiniRdrs', LIST_ENTRY),
        # protected by the mutex
        ('NumberOfMinirdrsRegistered', LONG),
        # Cache Management subsystem.
        ('OurProcess', PEPROCESS),
        # to CcInitializeCacheMap.
        ('CacheManagerCallbacks', CACHE_MANAGER_CALLBACKS),
        # To control access to the global Rx data record
        ('Resource', ERESOURCE),
    ]
    PRDBSS_DATA = POINTER(RDBSS_DATA)
    rdbss = ctypes.windll.RDBSS

    # PEPROCESS
    # RxGetRDBSSProcess(
    # VOID
    # );
    RxGetRDBSSProcess = rdbss.RxGetRDBSSProcess
    RxGetRDBSSProcess.restype = PEPROCESS

    # Note: A Strategy needs to be in place to deal with requests for stopping
    # the
    # RDBSS when requests are active.
    class _RX_RDBSS_STATE_(ENUM):
        RDBSS_STARTABLE = 0
        RDBSS_STARTED = 1
        RDBSS_STOP_IN_PROGRESS = 2

    RX_RDBSS_STATE = _RX_RDBSS_STATE_
    PRX_RDBSS_STATE = POINTER(_RX_RDBSS_STATE_)

    _RDBSS_STARTSTOP_CONTEXT_._fields_ = [
        ('State', RX_RDBSS_STATE),
        ('Version', ULONG),
        ('pStopContext', PRX_CONTEXT),
    ]

    _MRX_CALLDOWN_COMPLETION_CONTEXT_._fields_ = [
        ('WaitCount', LONG),
        ('Event', KEVENT),
    ]

    # NTSTATUS
    # (NTAPI *PMRX_CALLDOWN_ROUTINE) (
    # IN OUT PVOID CalldownParameter
    # );

    PMRX_CALLDOWN_ROUTINE = NTAPI(NTSTATUS, PVOID)

    _MRX_CALLDOWN_CONTEXT_._fields_ = [
        ('WorkQueueItem', RX_WORK_QUEUE_ITEM),
        ('pMRxDeviceObject', PRDBSS_DEVICE_OBJECT),
        ('pCompletionContext', PMRX_CALLDOWN_COMPLETION_CONTEXT),
        ('pRoutine', PMRX_CALLDOWN_ROUTINE),
        ('CompletionStatus', NTSTATUS),
        ('pParameter', PVOID),
    ]

    _RX_DISPATCHER_CONTEXT_._fields_ = [
        ('LONG NumberOfWorkerThreads', __volatile),
        ('PKEVENT pTearDownEvent', __volatile),
    ]


    def RxSetRdbssState(RxDeviceObject, NewState):
        SavedIrql = KIRQL()
        KeAcquireSpinLock(ctypes.byref(RxStrucSupSpinLock), ctypes.byref(SavedIrql))
        RxDeviceObject.StartStopContext.State = NewState
        KeReleaseSpinLock(ctypes.byref(RxStrucSupSpinLock), SavedIrql)

    def RxGetRdbssState(RxDeviceObject):
        return RxDeviceObject.StartStopContext.State


    # The RDBSS Device Object is an I/O system device object with additions for
    # the various structures needed by each minirdr: the dispatch, export - to
    # - minirdr
    # structure, MUP call characteristics, list of active operations, etc.

    # INLINE
    # VOID
    # NTAPI
    # RxUnregisterMinirdr(
    # IN PRDBSS_DEVICE_OBJECT RxDeviceObject
    # );
    RxUnregisterMinirdr = rdbss.RxUnregisterMinirdr
    RxUnregisterMinirdr.restype = VOID
    ntoskrnl = ctypes.windll.NTOSKRNL

    if RDBSSDeviceObject != NULL:
        # ObDereferenceObject( RDBSSDeviceObject );
        ObDereferenceObject = ntoskrnl.ObDereferenceObject
        ObDereferenceObject.restype = VOID


# END IF   _RDBSSSTRUC_
