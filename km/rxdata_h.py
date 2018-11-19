from pyWinAPI import *

# /* + + Copyright (c) 1989 Microsoft Corporation Module Name: RxData.h
# Abstract: This module declares the global data used by the RDBSS file
# system. Author: Revision History: - -

_RDBSSDATA_ = None
if not defined(_RDBSSDATA_):
    _RDBSSDATA_ = 1

    from pyWinAPI.km.rxworkq_h import * # NOQA

    MONOLITHIC_MINIRDR = None
    if not defined(MONOLITHIC_MINIRDR):
        RxIoWorkItem = PIO_WORKITEM

    # END IF

    RxDispatcher = RX_DISPATCHER
    RxDispatcherWorkQueues = RX_WORK_QUEUE_DISPATCHER

    # this constants are the same as the versions in ntexapi.h
    # but drivers are not supposed to import thatnot
    RX_PROCESSOR_ARCHITECTURE_INTEL = 0
    RX_PROCESSOR_ARCHITECTURE_MIPS = 1
    RX_PROCESSOR_ARCHITECTURE_ALPHA = 2
    RX_PROCESSOR_ARCHITECTURE_PPC = 3
    RX_PROCESSOR_ARCHITECTURE_UNKNOWN = 0xFFFF

    RxSerializationMutex = KMUTEX

    # RX_CONTEXT serialization
    def RxAcquireSerializationMutex():
        return KeWaitForSingleObject(
            ctypes.byref(RxSerializationMutex),
            Executive,
            KernelMode,
            FALSE,
            NULL
        )


    def RxReleaseSerializationMutex():
        return KeReleaseMutex(ctypes.byref(RxSerializationMutex), FALSE)

    # The global fsd data record, and global large integer constants
    # The status actually returned by the FsdDispatchStub.....usually not
    # implemented
    # The FCB for opens that refer to the device object directly or
    # for file objects that reference nonFcbs (like treecons)

    RxElapsedSecondsSinceStart = ULONG
    RxFileSystemDeviceObject = PRDBSS_DEVICE_OBJECT
    RxLargeZero = LARGE_INTEGER
    RxMaxLarge = LARGE_INTEGER
    Rx30Milliseconds = LARGE_INTEGER
    RxOneSecond = LARGE_INTEGER
    RxOneDay = LARGE_INTEGER
    RxJanOne1980 = LARGE_INTEGER
    RxDecThirtyOne1979 = LARGE_INTEGER

    # The status actually returned by the FsdDispatchStub.....usually not
    # implemented
    RxStubStatus = NTSTATUS

    # The FCB for opens that refer to the device object directly or
    # for file objects that reference nonFcbs (like treecons)
    RxDeviceFCB = FCB

    if 0:
        # Define maximum number of parallel Reads or Writes that will be
        # generated
        # per one request.
        RDBSS_MAX_IO_RUNS_ON_STACK = 5

        # Define the maximum number of delayed closes.
        RDBSS_MAX_DELAYED_CLOSES = 16
        RxMaxDelayedCloseCount = ULONG
    # END IF  0
    if DBG:
        # The following variables are used to keep track of the total amount
        # of requests processed by the file system, and the number of requests
        # that end up being processed by the Fsp thread. The first variable
        # is incremented whenever an Irp context is created (which is always
        # at the start of an Fsd entry point) and the second is incremented
        # by read request.

        RxFsdEntryCount = ULONG
        # extern ULONG RxFspEntryCount;
        # extern ULONG RxIoCallDriverCount;
        # extern ULONG RxTotalTicks[];
        RxIrpCodeCount = ULONG * 0

    #  END IF

    # The list of active RxContexts being processed by the RDBSS
    RxSrvCalldownList = LIST_ENTRY
    RxActiveContexts = LIST_ENTRY
    RxNumberOfActiveFcbs = LONG

    s_PipeShareName = UNICODE_STRING
    s_MailSlotShareName = UNICODE_STRING
    s_MailSlotServerPrefix = UNICODE_STRING
    s_IpcShareName = UNICODE_STRING
    s_PrimaryDomainName = UNICODE_STRING
    # To allow NFS to run RDBSS on W2K, we now look up the kenel routine
    # FsRtlTeardownPerStreamContexts dynamically at run time.
    # This is the global variable that contains the function pointer or NULL
    # if the routine could not be found (as on W2K.
# END IF   _RDBSSDATA_
