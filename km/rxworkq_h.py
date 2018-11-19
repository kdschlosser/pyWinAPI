import ctypes
from pyWinAPI import *
from pyWinAPI.km.wdm_h import *
from pyWinAPI.shared.wtypes_h import *


class _RX_WORK_QUEUE_ITEM_(WORK_QUEUE_ITEM):
    pass


RX_WORK_QUEUE_ITEM = _RX_WORK_QUEUE_ITEM_
PRX_WORK_QUEUE_ITEM = POINTER(_RX_WORK_QUEUE_ITEM_)


class _RX_WORK_DISPATCH_ITEM_(ctypes.Structure):
    pass

RX_WORK_DISPATCH_ITEM = _RX_WORK_DISPATCH_ITEM_
PRX_WORK_DISPATCH_ITEM = POINTER(_RX_WORK_DISPATCH_ITEM_)


class _RX_WORK_QUEUE_RUNDOWN_CONTEXT_(ctypes.Structure):
    pass


RX_WORK_QUEUE_RUNDOWN_CONTEXT = _RX_WORK_QUEUE_RUNDOWN_CONTEXT_
PRX_WORK_QUEUE_RUNDOWN_CONTEXT = POINTER(_RX_WORK_QUEUE_RUNDOWN_CONTEXT_)


class _RX_WORK_QUEUE_(ctypes.Structure):
    pass


RX_WORK_QUEUE = _RX_WORK_QUEUE_
PRX_WORK_QUEUE = POINTER(_RX_WORK_QUEUE_)


class _RX_WORK_QUEUE_DISPATCHER_(ctypes.Structure):
    pass


RX_WORK_QUEUE_DISPATCHER = _RX_WORK_QUEUE_DISPATCHER_
PRX_WORK_QUEUE_DISPATCHER = POINTER(_RX_WORK_QUEUE_DISPATCHER_)


class _RX_DISPATCHER_(ctypes.Structure):
    pass


RX_DISPATCHER = _RX_DISPATCHER_
PRX_DISPATCHER = POINTER(_RX_DISPATCHER_)


# /* + + Copyright (c) 1994 Microsoft Corporation Module Name: rxworkq.h
# Abstract: This module defines the data structures required to implement the
# dispatching mechanism in RDBSS for use by RDBSS as well as all the mini
# redirectors. Author: - -

_RXWORKQ_H_ = None
if not defined(_RXWORKQ_H_):
    _RXWORKQ_H_ = 1

    from pyWinAPI.missing_structures_h import * # NOQA
    # The worker thread routine prototype definition.

    # VOID
    # (NTAPI *PRX_WORKERTHREAD_ROUTINE) (
    # IN PVOID Context
    # );

    PRX_WORKERTHREAD_ROUTINE = NTAPI(VOID, PVOID)

    # The RDBSS needs to keep track of the work items on a per device object
    # basis.
    # This enables the race conditions associated with loading/unloading as
    # well as
    # a mechanism for preventing a single mini redirector from unfairly
    # hogging all
    # the resources.
    if defined(__cplusplus):
        pass
    else:
        pass
    # END IF

    from pyWinAPI.km.rxstruc_h import * # NOQA

    _RX_WORK_QUEUE_ITEM_._fields_ = [
        ('pDeviceObject', PRDBSS_DEVICE_OBJECT)
    ]
    # There are certain scenarios in which dispatching of work items is
    # inevitable.
    # In such instance the WORK_QUEUE_ITEM is allocated as part of another
    # data
    # structure to avoid frequent allocation/freeing. In other scenarios
    # where
    # dispatching is rare it pays to avoid the allocation of the memory
    # till it
    # is rquired. The RDBSS work queue implementations provide for both
    # these
    # scenarios in the form of dispatching and posting work queue
    # requests. In
    # the case of dispatching no memory for the WORK_QUEUE_ITEM need be
    # allocated
    # by the caller while for posting the memory for WORK_QUEUE_ITEM needs
    # to be
    # allocated by the caller.
    _RX_WORK_DISPATCH_ITEM_._fields_ = [
        ('WorkQueueItem', RX_WORK_QUEUE_ITEM),
        ('DispatchRoutine', PRX_WORKERTHREAD_ROUTINE),
        ('DispatchRoutineParameter', PVOID),
    ]

    # The work queues typically come up in a active state and continue
    # till either
    # a non recoverable situation is encountered
    # ( lack of system resources ) when
    # it transitions to the Inactive state. When a rundown is initiated it
    # transitions
    # to the rundown in progress state.

    class _RX_WORK_QUEUE_STATE_(ENUM):
        RxWorkQueueActive = 1
        RxWorkQueueInactive = 2
        RxWorkQueueRundownInProgress = 3


    RX_WORK_QUEUE_STATE = _RX_WORK_QUEUE_STATE_
    PRX_WORK_QUEUE_STATE = POINTER(_RX_WORK_QUEUE_STATE_)

    # The rundown of work queues is not complete when the threads have
    # been spun down.
    # The termination of the threads needs to be ensured before the data
    # structures
    # can be torn down. The work queue implementation follows a protocol
    # in which
    # each of the threads being spundown stashes a reference to the thread
    # object
    # in the rundown context. The rundown issuing thread
    # ( which does not belong to
    # the work queue
    # ) waits for the completion of all the threads spundown before
    # tearing down the data structures.
    _RX_WORK_QUEUE_RUNDOWN_CONTEXT_._fields_ = [
        ('RundownCompletionEvent', KEVENT),
        ('NumberOfThreadsSpunDown', LONG),
        ('ThreadPointers', POINTER(PETHREAD)),
    ]

    # The work queue implementation is built around a KQUEUE
    # implementation. The
    # additional support involves the regulation of number of threads that
    # are
    # actively waiting for the work items. Each work queue data structure
    # is
    # allocated in nonpaged pool and has its own synchronization mechanism
    # ( spinlock).
    # In addition to the bookkeeing information, i.e., state, type etc. it
    # also includes
    # statistics that are gathered over the lifetime of the queue. This
    # will
    # provide valuable information in tuning a work queue instance. The
    # number of items
    # that have been processed , the number of items that have to be
    # processed and
    # the cumulative queue length is recorded. The cumulative queue length
    # is the
    # intersiting metric, it is the sum of the number of items awaiting to
    # be processed
    # each time an additional work item was queued. The cumulative queue
    # length
    # divided by the sum of the total number of items processed and the
    # anumber of
    # items to be processed gives an indication of the average length of
    # the
    # queue. A value much greater than one signifies that the minimum
    # number of
    # worker threads associated with the work queue can be increased. A
    # value much
    # less than one signifies that the maximum number of work threads
    # associated
    # with the queue can be decreased.
    _RX_WORK_QUEUE_._fields_ = [
        ('State', USHORT),
        ('SpinUpRequestPending', BOOLEAN),
        ('Type', UCHAR),
        ('SpinLock', KSPIN_LOCK),
        ('pRundownContext', PRX_WORK_QUEUE_RUNDOWN_CONTEXT),
        ('NumberOfWorkItemsDispatched', LONG),
        ('NumberOfWorkItemsToBeDispatched', LONG),
        ('CumulativeQueueLength', LONG),
        ('NumberOfSpinUpRequests', LONG),
        ('MaximumNumberOfWorkerThreads', LONG),
        ('MinimumNumberOfWorkerThreads', LONG),
        ('NumberOfActiveWorkerThreads', LONG),
        ('NumberOfIdleWorkerThreads', LONG),
        ('NumberOfFailedSpinUpRequests', LONG),
        ('WorkQueueItemForSpinUpWorkerThreadInUse', LONG),
        ('WorkQueueItemForTearDownWorkQueue', RX_WORK_QUEUE_ITEM),
        ('WorkQueueItemForSpinUpWorkerThread', RX_WORK_QUEUE_ITEM),
        ('WorkQueueItemForSpinDownWorkerThread', RX_WORK_QUEUE_ITEM),
        ('Queue', KQUEUE),
        # FREE build.
        ('ThreadPointers', POINTER(PETHREAD)),
    ]

    # The dispatching mechanism in RDBSS provides for multiple levels of
    # work queues
    # on a per processor basis. There are three levels of work queues
    # currently
    # supported, Critical,Delayed and HyperCritical. The distinction
    # between Critical
    # and delayed is one of priority where as HyperCritical iss different
    # from the
    # other two in that the routines should not block, i.e., wait for any
    # resource.
    # This requirement cannot be enforced hence the effectiveness of the
    # dispatching
    # mechanism relies on the implicit cooperation of the clients.

    from pyWinAPI.km.rxtypes_h import * # NOQA
    _RX_WORK_QUEUE_DISPATCHER_._fields_ = [
        ('WorkQueue', RX_WORK_QUEUE * RxMaximumWorkQueue),
    ]

    # The dispatcher typically come up in a active state and continue till
    # either
    # a non recoverable situation is encountered
    # ( lack of system resources ) when
    # it transitions to the Inactive state. When a rundown is initiated it
    # transitions
    # to the rundown in progress state.
    class _RX_DISPATCHER_STATE_(ENUM):
        RxDispatcherActive = 1
        RxDispatcherInactive = 2


    RX_DISPATCHER_STATE = _RX_DISPATCHER_STATE_
    PRX_DISPATCHER_STATE = POINTER(_RX_DISPATCHER_STATE_)

    # The RDBSS dispatching mechanism on any machine is an array of the
    # dispatchers
    # associated with each processor. When a work queue item is queued a
    # best effort
    # is made to contain the work emanating from a processor onto the same
    # processor.
    # This ensures that processor affinities setup by the NT dispatcher
    # are not
    # destroyed by the RDBSS dispatching mechanism as this could lead to
    # excessive
    # sloshing. When the work needs to be moved there are two metrics that
    # will be
    # useful in making the decision, teh amount of delay that will be
    # experienced
    # by the work item in the current queue and the effort involved in
    # moving the
    # work item to the other queue. It is very easy to quantify the former
    # but very
    # difficult to quantify the later.
    _RX_DISPATCHER_._fields_ = [
        ('NumberOfProcessors', LONG),
        ('OwnerProcess', PEPROCESS),
        ('pWorkQueueDispatcher', PRX_WORK_QUEUE_DISPATCHER),
        ('State', RX_DISPATCHER_STATE),
        ('SpinUpRequests', LIST_ENTRY),
        ('SpinUpRequestsLock', KSPIN_LOCK),
        ('SpinUpRequestsEvent', KEVENT),
        ('SpinUpRequestsTearDownEvent', KEVENT),
    ]

    # The function prototypes used for dispatching/posting work queue items
    rdbss = ctypes.windll.RDBSS

    # extern NTSTATUS
    # NTAPI
    # RxPostToWorkerThread(
    # IN PRDBSS_DEVICE_OBJECT     pMRxDeviceObject,
    # IN WORK_QUEUE_TYPE          WorkQueueType,
    # IN PRX_WORK_QUEUE_ITEM      pWorkQueueItem,
    # IN PRX_WORKERTHREAD_ROUTINE Routine,
    # IN PVOID                    pContext
    # );
    RxPostToWorkerThread = rdbss.RxPostToWorkerThread
    RxPostToWorkerThread.restype = NTSTATUS

    # extern NTSTATUS
    # NTAPI
    # RxDispatchToWorkerThread(
    # IN  PRDBSS_DEVICE_OBJECT     pMRxDeviceObject,
    # IN  WORK_QUEUE_TYPE          WorkQueueType,
    # IN  PRX_WORKERTHREAD_ROUTINE Routine,
    # IN  PVOID                    pContext);
    RxDispatchToWorkerThread = rdbss.RxDispatchToWorkerThread
    RxDispatchToWorkerThread.restype = NTSTATUS

    # The routines for initializing/tearing down the dispatching mechanism
# END IF
