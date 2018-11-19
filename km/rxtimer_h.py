import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *


class _RX_WORK_ITEM_(ctypes.Structure):
    pass


RX_WORK_ITEM = _RX_WORK_ITEM_
PRX_WORK_ITEM = POINTER(_RX_WORK_ITEM_)


# /* + + Copyright (c) 1994 Microsoft Corporation Module Name: RxTimer.h
# Abstract: This module defines the prototypes and structures for the timer on
# the rdbss architecture. What is provided is a 55ms timer...that is, if you
# register a routine then you get a call every 55ms. On NT, you're at DPC
# level. Also contained here are the routines for posting to a thread from DPC
# level. Author: - -

_RXTIMER_H_ = None
if not defined(_RXTIMER_H_):
    _RXTIMER_H_ = 1

    from pyWinAPI.km.rxworkq_h import * # NOQA

    # The RX_WORK_ITEM encapsulates the context for posting to a worker thread
    # as well as
    # a timer routine to be triggered after a specific interval.
    _RX_WORK_ITEM_._fields_ = [
        ('WorkQueueItem', RX_WORK_QUEUE_ITEM),
        ('LastTick', ULONG),
        ('Options', ULONG),
    ]
    rdbss = ctypes.windll.RDBSS

    # extern NTSTATUS
    # NTAPI
    # RxPostOneShotTimerRequest(
    # IN PRDBSS_DEVICE_OBJECT     pDeviceObject,
    # IN PRX_WORK_ITEM            pWorkItem,
    # IN PRX_WORKERTHREAD_ROUTINE Routine,
    # IN PVOID                    pContext,
    # IN LARGE_INTEGER            TimeInterval);
    RxPostOneShotTimerRequest = rdbss.RxPostOneShotTimerRequest
    RxPostOneShotTimerRequest.restype = NTSTATUS

    # extern NTSTATUS
    # NTAPI
    # RxPostRecurrentTimerRequest(
    # IN PRDBSS_DEVICE_OBJECT     pDeviceObject,
    # IN PRX_WORKERTHREAD_ROUTINE Routine,
    # IN PVOID                    pContext,
    # IN LARGE_INTEGER            TimeInterval);
    RxPostRecurrentTimerRequest = rdbss.RxPostRecurrentTimerRequest
    RxPostRecurrentTimerRequest.restype = NTSTATUS

    # extern NTSTATUS
    # NTAPI
    # RxCancelTimerRequest(
    # IN PRDBSS_DEVICE_OBJECT     pDeviceObject,
    # IN PRX_WORKERTHREAD_ROUTINE Routine,
    # IN PVOID                    pContext
    # );
    RxCancelTimerRequest = rdbss.RxCancelTimerRequest
    RxCancelTimerRequest.restype = NTSTATUS

    # Routines for initializing and tearing down the timer service in RDBSS

    # extern NTSTATUS
    # NTAPI
    # RxInitializeRxTimer();
    RxInitializeRxTimer = rdbss.RxInitializeRxTimer
    RxInitializeRxTimer.restype = NTSTATUS

    # extern VOID
    # NTAPI
    # RxTearDownRxTimer(void);
    RxTearDownRxTimer = rdbss.RxTearDownRxTimer
    RxTearDownRxTimer.restype = VOID
# END IF   _RXTIMER_STUFF_DEFINED_
