import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *



# + + BUILD Version: 0162 // Increment this if a change has global effects
# Copyright (c) Microsoft Corporation. All rights reserved. Module Name: wdm.h
# Abstract: This module defines the WDM types, constants, and functions that
# are exposed to device drivers. Revision History: - -
if not defined(_WDMDDK_):
    _WDMDDK_ = 1

    if not defined(_NTDDK_):
        _WDM_INCLUDED_ = 1
        _DDK_DRIVER_ = 1

        # Use 9x compat Interlocked functions by default when including wdm.h
        NO_INTERLOCKED_INTRINSICS = 1
    # END IF
    _NTDDK_ = 1
    _STRSAFE_USE_SECURE_CRT = 0

        if _MSC_VER < 1300:
            pass
        # END IF
    if not defined(RC_INVOKED):
        pass
    # END IF   RC_INVOKED
    NT_INCLUDED = 1
    _CTYPE_DISABLE_MACROS = 1

    if _MSC_VER >= 1200:
        pass
    # END IF
    if defined(__cplusplus):
        pass
    # END IF
    PCALLBACK_OBJECT = POINTER(_CALLBACK_OBJECT)

    if defined(_NTHAL_INCLUDED_):
        PEPROCESS = POINTER(_KPROCESS)

        PETHREAD = POINTER(_ETHREAD)

    elif defined(_NTIFS_INCLUDED_):
        PEPROCESS = POINTER(_KPROCESS)

        PETHREAD = POINTER(_KTHREAD)

    else:
        PEPROCESS = POINTER(_EPROCESS)

        PETHREAD = POINTER(_ETHREAD)

    # END IF
    PIO_TIMER = POINTER(_IO_TIMER)

    PKINTERRUPT = POINTER(_KINTERRUPT)

    PRKTHREAD = POINTER(*PKTHREAD,)

    PRKPROCESS = POINTER(*PKPROCESS,)

    POBJECT_TYPE = POINTER(_OBJECT_TYPE)

    PSECURITY_QUALITY_OF_SERVICE = POINTER(_SECURITY_QUALITY_OF_SERVICE)


    # Declare empty structure definitions so that they may be referenced by
    # routines before they are defined
    PCONTEXT = POINTER(_CONTEXT)

    PIO_STACK_LOCATION = POINTER(_IO_STACK_LOCATION)

    PVPB = POINTER(_VPB)

    PFILE_GET_QUOTA_INFORMATION = POINTER(_FILE_GET_QUOTA_INFORMATION)

    if defined(_M_AMD64):
        pass
    # END IF   defined(_M_AMD64)
    if defined(_M_IX86) or defined(_M_ARM) or defined(_M_ARM64):
        pass
    # END IF   defined(_M_IX86) or defined(_M_ARM) or defined(_M_ARM64)
    # Define base address for kernel and user space
    if not defined(_WIN64):
        KADDRESS_BASE = 0
        UADDRESS_BASE = 0
    # END IF   not _WIN64

    if not defined(FAR):
        FAR = 1
    # END IF
    PsGetCurrentProcess = IoGetCurrentProcess

        if defined(_X86_) or defined(_AMD64_):
            pass
        else:
            pass
        # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    elif NTDDI_VERSION >= NTDDI_WINXP:
        pass
    else:
        pass
    # END IF
    if defined(_X86_):

        # Interrupt Request Level definitions
        PASSIVE_LEVEL = 0
        LOW_LEVEL = 0
        APC_LEVEL = 1
        DISPATCH_LEVEL = 2
        CMCI_LEVEL = 5
        PROFILE_LEVEL = 27
        CLOCK1_LEVEL = 28
        CLOCK2_LEVEL = 28
        IPI_LEVEL = 29
        POWER_LEVEL = 30
        HIGH_LEVEL = 31
        CLOCK_LEVEL = CLOCK2_LEVEL
    # END IF

    if defined(_AMD64_):

        # Interrupt Request Level definitions
        PASSIVE_LEVEL = 0
        LOW_LEVEL = 0
        APC_LEVEL = 1
        DISPATCH_LEVEL = 2
        CMCI_LEVEL = 5
        CLOCK_LEVEL = 13
        IPI_LEVEL = 14
        DRS_LEVEL = 14
        POWER_LEVEL = 14
        PROFILE_LEVEL = 15
        HIGH_LEVEL = 15
    # END IF

    if defined(_ARM_):

        # Interrupt Request Level definitions
        PASSIVE_LEVEL = 0
        LOW_LEVEL = 0
        APC_LEVEL = 1
        DISPATCH_LEVEL = 2
        CLOCK_LEVEL = 13
        IPI_LEVEL = 14
        DRS_LEVEL = 14
        POWER_LEVEL = 14
        PROFILE_LEVEL = 15
        HIGH_LEVEL = 15
    # END IF

    if defined(_ARM64_):

        # Interrupt Request Level definitions
        PASSIVE_LEVEL = 0
        LOW_LEVEL = 0
        APC_LEVEL = 1
        DISPATCH_LEVEL = 2
        CLOCK_LEVEL = 13
        IPI_LEVEL = 14
        DRS_LEVEL = 14
        POWER_LEVEL = 14
        PROFILE_LEVEL = 15
        HIGH_LEVEL = 15
    # END IF
    LOW_PRIORITY = 0
    LOW_REALTIME_PRIORITY = 16
    HIGH_PRIORITY = 31
    MAXIMUM_PRIORITY = 32
    MAXIMUM_WAIT_OBJECTS = 64
    MAXIMUM_SUSPEND_COUNT = MAXCHAR

    # Define system time structure.
    class _KSYSTEM_TIME(ctypes.Structure):
        pass


    _KSYSTEM_TIME._fields_ = [
        ('LowPart', ULONG),
        ('High1Time', LONG),
        ('High2Time', LONG),
    ]
    KSYSTEM_TIME = _KSYSTEM_TIME
    PKSYSTEM_TIME = POINTER(_KSYSTEM_TIME)

    # Thread priority
    KPRIORITY = LONG

    # Spin Lock
    KSPIN_LOCK = ULONG_PTR
    PKSPIN_LOCK = POINTER(KSPIN_LOCK)

    # Define per processor lock queue structure.
    # N.B. The lock field of the spin lock queue structure contains the address
    # of the associated kernel spin lock, an owner bit, and a lock bit. Bit
    # 0 of the spin lock address is the wait bit and bit 1 is the owner bit.
    # The use of this field is such that the bits can be set and cleared
    # noninterlocked, however, the back pointer must be preserved.
    # The lock wait bit is set when a processor enqueues itself on the lock
    # queue and it is not the only entry in the queue. The processor will
    # spin on this bit waiting for the lock to be granted.
    # The owner bit is set when the processor owns the respective lock.
    # The next field of the spin lock queue structure is used to line the
    # queued lock structures together in fifo order. It also can set set and
    # cleared noninterlocked.
    LOCK_QUEUE_WAIT = 1
    LOCK_QUEUE_WAIT_BIT = 0
    LOCK_QUEUE_OWNER = 2
    LOCK_QUEUE_OWNER_BIT = 1

    if defined(_AMD64_):
        KSPIN_LOCK_QUEUE_NUMBER = ULONG64
        LockQueueUnusedSpare0 = 0
        LockQueueUnusedSpare1 = 1
        LockQueueUnusedSpare2 = 2
        LockQueueUnusedSpare3 = 3
        LockQueueVacbLock = 4
        LockQueueMasterLock = 5
        LockQueueNonPagedPoolLock = 6
        LockQueueIoCancelLock = 7
        LockQueueUnusedSpare8 = 8
        LockQueueIoVpbLock = 9
        LockQueueIoDatabaseLock = 10
        LockQueueIoCompletionLock = 11
        LockQueueNtfsStructLock = 12
        LockQueueAfdWorkQueueLock = 13
        LockQueueBcbLock = 14
        LockQueueUnusedSpare15 = 15
        LockQueueUnusedSpare16 = 16
        LockQueueMaximumLock = LockQueueUnusedSpare16 + 1


    else:
        class _KSPIN_LOCK_QUEUE_NUMBER(ENUM):
            LockQueueUnusedSpare0 = 1
            LockQueueUnusedSpare1 = 2
            LockQueueUnusedSpare2 = 3
            LockQueueUnusedSpare3 = 4
            LockQueueVacbLock = 5
            LockQueueMasterLock = 6
            LockQueueNonPagedPoolLock = 7
            LockQueueIoCancelLock = 8
            LockQueueUnusedSpare8 = 9
            LockQueueIoVpbLock = 10
            LockQueueIoDatabaseLock = 11
            LockQueueIoCompletionLock = 12
            LockQueueNtfsStructLock = 13
            LockQueueAfdWorkQueueLock = 14
            LockQueueBcbLock = 15
            LockQueueUnusedSpare15 = 16
            LockQueueUnusedSpare16 = 17
            LockQueueMaximumLock = LockQueueUnusedSpare16 + 1


        KSPIN_LOCK_QUEUE_NUMBER = _KSPIN_LOCK_QUEUE_NUMBER
        PKSPIN_LOCK_QUEUE_NUMBER = POINTER(_KSPIN_LOCK_QUEUE_NUMBER)
    # END IF
    class _KSPIN_LOCK_QUEUE(ctypes.Structure):
        pass


    _KSPIN_LOCK_QUEUE._fields_ = [
        (' volatile Next', POINTER(_KSPIN_LOCK_QUEUE)),
        ('volatile Lock', PKSPIN_LOCK),
    ]
    KSPIN_LOCK_QUEUE = _KSPIN_LOCK_QUEUE
    PKSPIN_LOCK_QUEUE = POINTER(_KSPIN_LOCK_QUEUE)
    class _KLOCK_QUEUE_HANDLE(ctypes.Structure):
        pass


    _KLOCK_QUEUE_HANDLE._fields_ = [
        ('LockQueue', KSPIN_LOCK_QUEUE),
        ('OldIrql', KIRQL),
    ]
    KLOCK_QUEUE_HANDLE = _KLOCK_QUEUE_HANDLE
    PKLOCK_QUEUE_HANDLE = POINTER(_KLOCK_QUEUE_HANDLE)

    # Profile source types
    class _KPROFILE_SOURCE(ENUM):
        ProfileTime = 1
        ProfileAlignmentFixup = 2
        ProfileTotalIssues = 3
        ProfilePipelineDry = 4
        ProfileLoadInstructions = 5
        ProfilePipelineFrozen = 6
        ProfileBranchInstructions = 7
        ProfileTotalNonissues = 8
        ProfileDcacheMisses = 9
        ProfileIcacheMisses = 10
        ProfileCacheMisses = 11
        ProfileBranchMispredictions = 12
        ProfileStoreInstructions = 13
        ProfileFpInstructions = 14
        ProfileIntegerInstructions = 15
        Profile2Issue = 16
        Profile3Issue = 17
        Profile4Issue = 18
        ProfileSpecialInstructions = 19
        ProfileTotalCycles = 20
        ProfileIcacheIssues = 21
        ProfileDcacheAccesses = 22
        ProfileMemoryBarrierCycles = 23
        ProfileLoadLinkedIssues = 24
        ProfileMaximum = 25


    KPROFILE_SOURCE = _KPROFILE_SOURCE

    # Define global triage information for DPC watchdog profile
    DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK_SIGNATURE = 0xAEBECEDE
    DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK_REVISION_1 = 0x1
    DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK_VER_1_SIZE = RTL_SIZEOF_THROUGH_FIELD(
        DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK,
        DpcWatchdogProfileLength,
    )
    class _DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK(ctypes.Structure):
        pass


    _DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK._fields_ = [
        ('Signature', ULONG),
        ('Revision', USHORT),
        ('Size', USHORT),
        ('DpcWatchdogProfileOffset', USHORT),
        ('DpcWatchdogProfileLength', ULONG),
    ]
    DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK = _DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK
    PDPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK = POINTER(_DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK)

    # Define 128 - bit 16 - byte aligned xmm register type.
    class _M128A(ctypes.Structure):
        pass


    _M128A._fields_ = [
        ('Low', ULONGLONG),
        ('High', LONGLONG),
    ]
    M128A = _M128A
    PM128A = POINTER(_M128A)

    # Format of data for (F)XSAVE/(F)XRSTOR instruction
    class _XSAVE_FORMAT(ctypes.Structure):
        pass


    _XSAVE_FORMAT._fields_ = [
        ('ControlWord', USHORT),
        ('StatusWord', USHORT),
        ('TagWord', UCHAR),
        ('Reserved1', UCHAR),
        ('ErrorOpcode', USHORT),
        ('ErrorOffset', ULONG),
        ('ErrorSelector', USHORT),
        ('Reserved2', USHORT),
        ('DataOffset', ULONG),
        ('DataSelector', USHORT),
        ('Reserved3', USHORT),
        ('MxCsr', ULONG),
        ('MxCsr_Mask', ULONG),
        ('FloatRegisters', M128A * 8),
            ('XmmRegisters', M128A * 16),
            ('Reserved4', UCHAR * 96),
            ('XmmRegisters', M128A * 8),
            ('Reserved4', UCHAR * 224),
    ]
    XSAVE_FORMAT = _XSAVE_FORMAT
    PXSAVE_FORMAT = POINTER(_XSAVE_FORMAT)

    if defined(_WIN64):
        pass
    else:
        pass
    # END IF
    class _XSAVE_AREA_HEADER(ctypes.Structure):
        pass


    _XSAVE_AREA_HEADER._fields_ = [
        ('Mask', ULONG64),
        ('CompactionMask', ULONG64),
        ('Reserved2', ULONG64 * 6),
    ]
    XSAVE_AREA_HEADER = _XSAVE_AREA_HEADER
    PXSAVE_AREA_HEADER = POINTER(_XSAVE_AREA_HEADER)
    class _XSAVE_AREA(ctypes.Structure):
        pass


    _XSAVE_AREA._fields_ = [
        ('LegacyState', XSAVE_FORMAT),
        ('Header', XSAVE_AREA_HEADER),
    ]
    XSAVE_AREA = _XSAVE_AREA
    PXSAVE_AREA = POINTER(_XSAVE_AREA)
    class _XSTATE_CONTEXT(ctypes.Structure):
        pass


    _XSTATE_CONTEXT._fields_ = [
        ('Mask', ULONG64),
        ('Length', ULONG),
        ('Reserved1', ULONG),
        ('Area', PXSAVE_AREA),
            ('Reserved2', ULONG),
        ('Buffer', PVOID),
            ('Reserved3', ULONG),
    ]
    XSTATE_CONTEXT = _XSTATE_CONTEXT
    PXSTATE_CONTEXT = POINTER(_XSTATE_CONTEXT)
    if defined(_X86_):
        pass
    # END IF
    if defined(_X86_):
        pass
    # END IF
    if defined(_X86_):

        # Some intrinsics have a redundant __cdecl calling - convention
        # specifier when
        # not compiled with /clr:pure.
        if defined(_M_CEE_PURE):
            CDECL_NON_WVMPURE = 1
        else:
            CDECL_NON_WVMPURE = __cdecl
        # END IF
        # Disable these two pragmas that evaluate to "sti" "cli" on x86 so
        # that driver
        # writers to not leave them inadvertantly in their code.

                if _MSC_VER >= 1200:
                    pass
                # END IF   _MSC_VER >= 1200
        if not defined(MIDL_PASS):
            if not defined(RC_INVOKED):

                # pragma warning(disable:4164) // disable C4164 warning so
                # that apps that
                # build with /Od don't get weird errors not
                if _MSC_VER >= 1200:
                    pass
                else:
                    pass
                # END IF   _MSC_VER >= 1200            # END IF   not defined(MIDL_PASS)        # END IF   not defined(RC_INVOKED)
            if defined(__cplusplus):
                pass
            # END IF
        if defined(_M_IX86) and not defined(RC_INVOKED) and not defined(MIDL_PASS):
            if not defined(_MANAGED):

                # Define bit scan intrinsics.
                BitScanForward = _BitScanForward
                BitScanReverse = _BitScanReverse
            # END IF   not defined(_MANAGED)

            if not defined(_MANAGED):
                pass
            # END IF   not defined(_MANAGED)
            InterlockedAnd = _InterlockedAnd
            InterlockedAndAcquire = _InterlockedAnd
            InterlockedAndRelease = _InterlockedAnd
            InterlockedAndNoFence = _InterlockedAnd
            InterlockedOr = _InterlockedOr
            InterlockedOrAcquire = _InterlockedOr
            InterlockedOrRelease = _InterlockedOr
            InterlockedOrNoFence = _InterlockedOr
            InterlockedXor = _InterlockedXor
            InterlockedXorAcquire = _InterlockedXor
            InterlockedXorRelease = _InterlockedXor
            InterlockedXorNoFence = _InterlockedXor
            InterlockedIncrement = _InterlockedIncrement
            InterlockedIncrementAcquire = _InterlockedIncrement
            InterlockedIncrementRelease = _InterlockedIncrement
            InterlockedIncrementNoFence = _InterlockedIncrement
            InterlockedDecrement = _InterlockedDecrement
            InterlockedDecrementAcquire = _InterlockedDecrement
            InterlockedDecrementRelease = _InterlockedDecrement
            InterlockedDecrementNoFence = _InterlockedDecrement
            InterlockedAdd = _InlineInterlockedAdd
            InterlockedAddAcquire = _InlineInterlockedAdd
            InterlockedAddRelease = _InlineInterlockedAdd
            InterlockedAddNoFence = _InlineInterlockedAdd
            InterlockedAddNoFence64 = _InlineInterlockedAdd64
            InterlockedExchange = _InterlockedExchange
            InterlockedExchangeAcquire = _InterlockedExchange
            InterlockedExchangeNoFence = _InterlockedExchange
            InterlockedExchangeAdd = _InterlockedExchangeAdd
            InterlockedExchangeAddAcquire = _InterlockedExchangeAdd
            InterlockedExchangeAddRelease = _InterlockedExchangeAdd
            InterlockedExchangeAddNoFence = _InterlockedExchangeAdd
            InterlockedCompareExchange = _InterlockedCompareExchange
            InterlockedCompareExchangeAcquire = _InterlockedCompareExchange
            InterlockedCompareExchangeRelease = _InterlockedCompareExchange
            InterlockedCompareExchangeNoFence = _InterlockedCompareExchange
            InterlockedExchange16 = _InterlockedExchange16

                if _MSC_VER >= 1600:
                    pass
                # END IF   _MSC_VER >= 1600
            if not defined(_MANAGED):
                if _MSC_FULL_VER >= 140041204:
                    InterlockedExchangeAdd8 = _InterlockedExchangeAdd8
                    InterlockedAnd8 = _InterlockedAnd8
                    InterlockedOr8 = _InterlockedOr8
                    InterlockedXor8 = _InterlockedXor8
                    InterlockedAnd16 = _InterlockedAnd16
                    InterlockedOr16 = _InterlockedOr16
                    InterlockedXor16 = _InterlockedXor16
                    InterlockedCompareExchange16 = (
                        _InterlockedCompareExchange16
                    )
                    InterlockedIncrement16 = _InterlockedIncrement16
                    InterlockedDecrement16 = _InterlockedDecrement16
                # END IF  _MSC_FULL_VER >= 140040816
                # Define 64 - bit operations in terms of
                # InterlockedCompareExchange64
                InterlockedCompareExchange64 = _InterlockedCompareExchange64
            # END IF   not defined(_MANAGED)
            InterlockedXor = _InterlockedXor

            if not defined(_MANAGED):
                pass
            # END IF   not defined(_MANAGED)
            if not defined(_M_CEE_PURE):
                if _MSC_VER >= 1500:

                    # Define extended CPUID intrinsic.
                    CpuIdEx = __cpuidex
                # END IF
                # Define FS read/write intrinsics            # END IF   not defined(_M_CEE_PURE)

            if not defined(_MANAGED) and not defined(_M_HYBRID_X86_ARM64):
                YieldProcessor = _mm_pause
            # END IF   not defined(_MANAGED) and not defined(_M_HYBRID_X86_ARM64)

            if defined(__cplusplus):
                pass
            # END IF        # END IF  not defined(MIDL_PASS) or defined(_M_IX86)
        if not defined(__midl) and not defined(MIDL_PASS):
            pass
        # END IF
        if defined(_KERNEL_MODE) or defined(_BOOT_ENVIRONMENT):
            KI_USER_SHARED_DATA = 0xFFDF0000
            SharedUserData = (KUSER_SHARED_DATA * const) KI_USER_SHARED_DATA
        # END IF    # END IF   _X86_

    if defined(_AMD64_):
        if defined(_M_AMD64) and not defined(RC_INVOKED) and not defined(MIDL_PASS):

            # Define bit test intrinsics.
            if defined(__cplusplus):
                pass
            # END IF
            # Define bit scan intrinsics.
            BitScanForward = _BitScanForward
            BitScanReverse = _BitScanReverse
            BitScanForward64 = _BitScanForward64
            BitScanReverse64 = _BitScanReverse64

            # Interlocked intrinsic functions.
            InterlockedIncrement16 = _InterlockedIncrement16
            InterlockedIncrementAcquire16 = _InterlockedIncrement16
            InterlockedIncrementRelease16 = _InterlockedIncrement16
            InterlockedIncrementNoFence16 = _InterlockedIncrement16
            InterlockedDecrement16 = _InterlockedDecrement16
            InterlockedDecrementAcquire16 = _InterlockedDecrement16
            InterlockedDecrementRelease16 = _InterlockedDecrement16
            InterlockedDecrementNoFence16 = _InterlockedDecrement16
            InterlockedCompareExchange16 = _InterlockedCompareExchange16
            InterlockedCompareExchangeAcquire16 = _InterlockedCompareExchange16
            InterlockedCompareExchangeRelease16 = _InterlockedCompareExchange16
            InterlockedCompareExchangeNoFence16 = _InterlockedCompareExchange16
            InterlockedAnd = _InterlockedAnd
            InterlockedAndAcquire = _InterlockedAnd
            InterlockedAndRelease = _InterlockedAnd
            InterlockedAndNoFence = _InterlockedAnd
            InterlockedOr = _InterlockedOr
            InterlockedOrAcquire = _InterlockedOr
            InterlockedOrRelease = _InterlockedOr
            InterlockedOrNoFence = _InterlockedOr
            InterlockedXor = _InterlockedXor
            InterlockedXorAcquire = _InterlockedXor
            InterlockedXorRelease = _InterlockedXor
            InterlockedXorNoFence = _InterlockedXor
            InterlockedIncrement = _InterlockedIncrement
            InterlockedIncrementAcquire = _InterlockedIncrement
            InterlockedIncrementRelease = _InterlockedIncrement
            InterlockedIncrementNoFence = _InterlockedIncrement
            InterlockedDecrement = _InterlockedDecrement
            InterlockedDecrementAcquire = _InterlockedDecrement
            InterlockedDecrementRelease = _InterlockedDecrement
            InterlockedDecrementNoFence = _InterlockedDecrement
            InterlockedAdd = _InlineInterlockedAdd
            InterlockedAddAcquire = _InlineInterlockedAdd
            InterlockedAddRelease = _InlineInterlockedAdd
            InterlockedAddNoFence = _InlineInterlockedAdd
            InterlockedExchange = _InterlockedExchange
            InterlockedExchangeAcquire = _InterlockedExchange
            InterlockedExchangeNoFence = _InterlockedExchange
            InterlockedExchangeAdd = _InterlockedExchangeAdd
            InterlockedExchangeAddAcquire = _InterlockedExchangeAdd
            InterlockedExchangeAddRelease = _InterlockedExchangeAdd
            InterlockedExchangeAddNoFence = _InterlockedExchangeAdd
            InterlockedCompareExchange = _InterlockedCompareExchange
            InterlockedCompareExchangeAcquire = _InterlockedCompareExchange
            InterlockedCompareExchangeRelease = _InterlockedCompareExchange
            InterlockedCompareExchangeNoFence = _InterlockedCompareExchange
            InterlockedAnd64 = _InterlockedAnd64
            InterlockedAnd64Acquire = _InterlockedAnd64
            InterlockedAnd64Release = _InterlockedAnd64
            InterlockedAnd64NoFence = _InterlockedAnd64
            InterlockedAndAffinity = InterlockedAnd64
            InterlockedOr64 = _InterlockedOr64
            InterlockedOr64Acquire = _InterlockedOr64
            InterlockedOr64Release = _InterlockedOr64
            InterlockedOr64NoFence = _InterlockedOr64
            InterlockedOrAffinity = InterlockedOr64
            InterlockedXor64 = _InterlockedXor64
            InterlockedXor64Acquire = _InterlockedXor64
            InterlockedXor64Release = _InterlockedXor64
            InterlockedXor64NoFence = _InterlockedXor64
            InterlockedIncrement64 = _InterlockedIncrement64
            InterlockedIncrementAcquire64 = _InterlockedIncrement64
            InterlockedIncrementRelease64 = _InterlockedIncrement64
            InterlockedIncrementNoFence64 = _InterlockedIncrement64
            InterlockedDecrement64 = _InterlockedDecrement64
            InterlockedDecrementAcquire64 = _InterlockedDecrement64
            InterlockedDecrementRelease64 = _InterlockedDecrement64
            InterlockedDecrementNoFence64 = _InterlockedDecrement64
            InterlockedAdd64 = _InlineInterlockedAdd64
            InterlockedAddAcquire64 = _InlineInterlockedAdd64
            InterlockedAddRelease64 = _InlineInterlockedAdd64
            InterlockedAddNoFence64 = _InlineInterlockedAdd64
            InterlockedExchange64 = _InterlockedExchange64
            InterlockedExchangeAcquire64 = InterlockedExchange64
            InterlockedExchangeNoFence64 = InterlockedExchange64
            InterlockedExchangeAdd64 = _InterlockedExchangeAdd64
            InterlockedExchangeAddAcquire64 = _InterlockedExchangeAdd64
            InterlockedExchangeAddRelease64 = _InterlockedExchangeAdd64
            InterlockedExchangeAddNoFence64 = _InterlockedExchangeAdd64
            InterlockedCompareExchange64 = _InterlockedCompareExchange64
            InterlockedCompareExchangeAcquire64 = InterlockedCompareExchange64
            InterlockedCompareExchangeRelease64 = InterlockedCompareExchange64
            InterlockedCompareExchangeNoFence64 = InterlockedCompareExchange64
            InterlockedCompareExchange128 = _InterlockedCompareExchange128
            InterlockedExchangePointer = _InterlockedExchangePointer
            InterlockedExchangePointerNoFence = _InterlockedExchangePointer
            InterlockedExchangePointerAcquire = _InterlockedExchangePointer
            InterlockedCompareExchangePointer = (
                _InterlockedCompareExchangePointer
            )
            InterlockedCompareExchangePointerAcquire = (
                _InterlockedCompareExchangePointer
            )
            InterlockedCompareExchangePointerRelease = (
                _InterlockedCompareExchangePointer
            )
            InterlockedCompareExchangePointerNoFence = (
                _InterlockedCompareExchangePointer
            )


            def InterlockedExchangeAddSizeT(a, b):
                return InterlockedExchangeAdd64(LONG64 *a, b)


            def InterlockedExchangeAddSizeTAcquire(a, b):
                return InterlockedExchangeAdd64(LONG64 *a, b)


            def InterlockedExchangeAddSizeTNoFence(a, b):
                return InterlockedExchangeAdd64(LONG64 *a, b)


            def InterlockedIncrementSizeT(a):
                return InterlockedIncrement64(LONG64 *a)


            def InterlockedIncrementSizeTNoFence(a):
                return InterlockedIncrement64(LONG64 *a)


            def InterlockedDecrementSizeT(a):
                return InterlockedDecrement64(LONG64 *a)


            def InterlockedDecrementSizeTNoFence(a):
                return InterlockedDecrement64(LONG64 *a)

            if not defined(_X86AMD64_):
                pass
            # END IF
            if not defined(_X86AMD64_):
                pass
            # END IF
            if _MSC_VER >= 1500:
                pass
            # END IF
            if _MSC_VER >= 1600:
                InterlockedExchange8 = _InterlockedExchange8
                InterlockedExchange16 = _InterlockedExchange16
            # END IF  _MSC_VER >= 1600

            if _MSC_FULL_VER >= 140041204:
                InterlockedExchangeAdd8 = _InterlockedExchangeAdd8
                InterlockedAnd8 = _InterlockedAnd8
                InterlockedOr8 = _InterlockedOr8
                InterlockedXor8 = _InterlockedXor8
                InterlockedAnd16 = _InterlockedAnd16
                InterlockedOr16 = _InterlockedOr16
                InterlockedXor16 = _InterlockedXor16
            # END IF
            # Define extended CPUID intrinsic.
            CpuIdEx = __cpuidex

            # Define function to flush a cache line.


            def CacheLineFlush(Address):
                return _mm_clflushAddress

            # Define memory fence intrinsics
            FastFence = __faststorefence
            LoadFence = _mm_lfence
            MemoryFence = _mm_mfence
            StoreFence = _mm_sfence

            # Define constants for use with _mm_prefetch.
            _MM_HINT_T0 = 1
            _MM_HINT_T1 = 2
            _MM_HINT_T2 = 3
            _MM_HINT_NTA = 0
            YieldProcessor = _mm_pause
            MemoryBarrier = __faststorefence


            def PreFetchCacheLine(l, a):
                return _mm_prefetch(CHAR CONST * a, l)


            def PrefetchForWrite(p):
                return _m_prefetchwp


            def ReadForWriteAccess(p):
                return (_m_prefetchwp, *p)

            # PreFetchCacheLine level defines.
            PF_TEMPORAL_LEVEL_1 = _MM_HINT_T0
            PF_TEMPORAL_LEVEL_2 = _MM_HINT_T1
            PF_TEMPORAL_LEVEL_3 = _MM_HINT_T2
            PF_NON_TEMPORAL_LEVEL_ALL = _MM_HINT_NTA

            # Define get/set MXCSR intrinsics.
            ReadMxCsr = _mm_getcsr
            WriteMxCsr = _mm_setcsr

            # Define function to get the caller's EFLAGs value.


            def GetCallersEflags():
                return __getcallerseflags

            # Define function to get segment limit.
            GetSegmentLimit = __segmentlimit

            # Define function to read the value of a performance counter.
            ReadPMC = __readpmc

            # Define function to read the value of the time stamp counter


            def ReadTimeStampCounter():
                return __rdtsc

            # Define functions to move strings as bytes, words, dwords, and
            # qwords.
            # Define functions to store strings as bytes, words, dwords, and
            # qwords.
            # Define functions to capture the high 64 - bits of a 128 - bit
            # multiply.
            MultiplyHigh = __mulh
            UnINTMultiplyHigh = __umulh

            # Define population count intrinsic.
            PopulationCount64 = __popcnt64

            if _MSC_VER >= 1500:
                pass
            # END IF
            # Define functions to perform 128 - bit shifts
            ShiftLeft128 = __shiftleft128
            ShiftRight128 = __shiftright128

            # Define functions to perform 128 - bit multiplies.
            Multiply128 = _mul128

            if not defined(UnINTMultiply128):
                UnINTMultiply128 = _umul128
            # END IF

                if 0:
                    pass
                # END IF
            if not defined(_MANAGED):
                pass
            # END IF   not defined(_MANAGED)
            if defined(__cplusplus):
                pass
            # END IF        # END IF   defined(_M_AMD64) and not defined(RC_INVOKED) and not defined(MIDL_PASS)
        if defined(_KERNEL_MODE) or defined(_BOOT_ENVIRONMENT):
            KI_USER_SHARED_DATA = 0xFFFFF78000000000UI64
            SharedUserData = (KUSER_SHARED_DATA * const)KI_USER_SHARED_DATA
            SharedInterruptTime = KI_USER_SHARED_DATA + 0x8
            SharedSystemTime = KI_USER_SHARED_DATA + 0x14
            SharedTickCount = KI_USER_SHARED_DATA + 0x320


            def KeQueryInterruptTime():
                return *volatile ULONG64 *SharedInterruptTime


            def KeQuerySystemTime(CurrentCount):
                return *PULONG64CurrentCount = *(volatile ULONG64 *SharedSystemTime)


            def KeQueryTickCount(CurrentCount):
                return *PULONG64CurrentCount = *(volatile ULONG64 *SharedTickCount)
        # END IF    # END IF   _AMD64_

                if defined(__cplusplus):
                    pass
                # END IF
                if _MSC_FULL_VER >= 170040825:
                    pass
                else:
                    pass
                # END IF
                if defined(__cplusplus):
                    pass
                # END IF
            if not defined(_M_CEE_PURE):
                pass
            # END IF   not defined(_M_CEE_PURE)
        if defined(_M_ARM) and not defined(RC_INVOKED) and not defined(MIDL_PASS):
            pass
        # END IF   defined(_M_ARM) and not defined(RC_INVOKED) and not defined(MIDL_PASS) and not defined(_M_CEE_PURE)
        if defined(_M_CEE_PURE):
            pass
        # END IF
        if defined(_KERNEL_MODE) or defined(_BOOT_ENVIRONMENT):
            pass
        # END IF
    if defined(_ARM_):
        pass
    # END IF   _ARM_
                if defined(_M_ARM64):
                    pass
                # END IF   defined(_M_ARM64)
                    if defined(_M_HYBRID_X86_ARM64):
                        pass
                    # END IF
    if defined(_ARM64_) or defined(_CHPE_X86_ARM64_):
        if not defined(_M_CEE_PURE):
            if not defined(RC_INVOKED) and not defined(MIDL_PASS):
                if defined(_M_ARM64) or defined(_M_HYBRID_X86_ARM64):

                    # Define function to read the value of the time stamp
                    # counter.
                    if defined(_M_HYBRID_X86_ARM64):
                        pass
                    # END IF
                    if defined(_M_HYBRID_X86_ARM64):
                        pass
                    else:
                        pass
                    # END IF                # END IF   defined(_M_ARM64) or defined(_M_HYBRID_X86_ARM64)            # END IF   not defined(RC_INVOKED) and not defined(MIDL_PASS)
        else: #  defined(_M_CEE_PURE)
            pass
        # END IF   not defined(_M_CEE_PURE)
        if defined(_M_CEE_PURE):
            pass
        # END IF
        if defined(_KERNEL_MODE) or defined(_BOOT_ENVIRONMENT)) and defined(_ARM64_:
            pass
        # END IF    # END IF   defined(_ARM64_) or defined(_CHPE_X86_ARM64_)
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
        if (defined(_M_AMD64) or defined(_M_IX86)) and not defined(_M_HYBRID_X86_ARM64)) or defined(_M_CEE_PURE:
            pass
        # END IF   defined(_M_AMD64) or defined(_M_IX86) or defined(_M_CEE_PURE)
        if not defined(_WIN64):
            pass
        else: #  not defined(_WIN64)
            pass
        # END IF   not defined(_WIN64)
    if not defined(RC_INVOKED) and not defined(MIDL_PASS):
        pass
    # END IF   not defined(RC_INVOKED) and not defined(MIDL_PASS)
    if defined(__cplusplus):
        pass
    # END IF
        if defined(_PREFAST_):
            pass
        # END IF
    if not defined(_DBGRAISEASSERTIONFAILURE_) and not defined(RC_INVOKED) and not defined(MIDL_PASS):
        if defined(_AMD64_):
            if defined(_M_AMD64):
                if not defined(_PREFAST_):


                    def DbgRaiseAssertionFailure():
                        return __int2c
                # END IF   not defined(_PREFAST_)            # END IF   defined(_M_AMD64)

        elif defined(_X86_) and not defined(_M_HYBRID_X86_ARM64):
            if defined(_M_IX86) and not defined(_M_HYBRID_X86_ARM64):
                if _MSC_FULL_VER >= 140030222:
                    if not defined(_PREFAST_):


                        def DbgRaiseAssertionFailure():
                            return __int2c
                    # END IF   not defined(_PREFAST_)

                    if not defined(_PREFAST_):
                        pass
                    # END IF   not defined(_PREFAST_)
                else: #  _MSC_FULL_VER >= 140030222
                    pass
                # END IF   _MSC_FULL_VER >= 140030222            # END IF   defined(_M_IX86)
        elif defined(_IA64_):
            if defined(_M_IA64):
                BREAK_DEBUG_BASE = 0x080000
                ASSERT_BREAKPOINT = BREAK_DEBUG_BASE + 3

                if not defined(_PREFAST_):


                    def DbgRaiseAssertionFailure():
                        return __breakASSERT_BREAKPOINT
                # END IF   not defined(_PREFAST_)            # END IF   defined(_M_IA64)

        elif defined(_ARM64_) or defined(_CHPE_X86_ARM64_):
            if defined(_M_ARM64) or defined(_M_HYBRID_X86_ARM64):
                if not defined(_PREFAST_):


                    def DbgRaiseAssertionFailure():
                        return __break0xF001
                # END IF   not defined(_PREFAST_)            # END IF   defined(_M_ARM64) or defined(_M_HYBRID_X86_ARM64)

        elif defined(_ARM_):
            if defined(_M_ARM):
                if not defined(_PREFAST_):


                    def DbgRaiseAssertionFailure():
                        return __emit0xDEFC
                # END IF   not defined(_PREFAST_)            # END IF   defined(_M_ARM)        # END IF   _AMD64_, _X86_, _IA64_, _ARM64_, _ARM_    # END IF   not defined(_DBGRAISEASSERTIONFAILURE_) and not defined(RC_INVOKED) and not defined(MIDL_PASS)

    if defined(__cplusplus):
        pass
    # END IF
        if defined(_PREFAST_):
            pass
            if DBG:
                pass
            else: #  DBG
                pass
            # END IF   DBG
        else: #  _PREFAST_
            pass
        # END IF   _PREFAST_
        if DBG:
            pass
        else: #  DBG
            pass
        # END IF   DBG
        if defined(NT_ASSERT_ALWAYS_ASSUMES):
            pass
        else: #  NT_ASSERT_ALWAYS_ASSUMES
            pass
        # END IF   NT_ASSERT_ALWAYS_ASSUMES
    if _MSC_VER >= 1300:
        pass
    # END IF   _MSC_VER >= 1300
    PACCESS_MASK = POINTER(ACCESS_MASK)

    # The following are masks for the predefined standard access types
    DELETE = 0x00010000
    READ_CONTROL = 0x00020000
    WRITE_DAC = 0x00040000
    WRITE_OWNER = 0x00080000
    SYNCHRONIZE = 0x00100000
    STANDARD_RIGHTS_REQUIRED = 0x000F0000
    STANDARD_RIGHTS_READ = READ_CONTROL
    STANDARD_RIGHTS_WRITE = READ_CONTROL
    STANDARD_RIGHTS_EXECUTE = READ_CONTROL
    STANDARD_RIGHTS_ALL = 0x001F0000
    SPECIFIC_RIGHTS_ALL = 0x0000FFFF

    # AccessSystemAcl access type
    ACCESS_SYSTEM_SECURITY = 0x01000000

    # MaximumAllowed access type
    MAXIMUM_ALLOWED = 0x02000000

    # These are the generic rights.
    GENERIC_READ = 0x80000000
    GENERIC_WRITE = 0x40000000
    GENERIC_EXECUTE = 0x20000000
    GENERIC_ALL = 0x10000000

    # Define the generic mapping array. This is used to denote the
    # mapping of each generic access right to a specific access mask.
    class _GENERIC_MAPPING(ctypes.Structure):
        pass


    _GENERIC_MAPPING._fields_ = [
        ('GenericRead', ACCESS_MASK),
        ('GenericWrite', ACCESS_MASK),
        ('GenericExecute', ACCESS_MASK),
        ('GenericAll', ACCESS_MASK),
    ]
    GENERIC_MAPPING = _GENERIC_MAPPING
    PGENERIC_MAPPING = POINTER(GENERIC_MAPPING)

    # //////////////////////////////////////////////////////////////////////
    # //
    # LUID_AND_ATTRIBUTES     //
    # //
    # //////////////////////////////////////////////////////////////////////
    class _LUID_AND_ATTRIBUTES(ctypes.Structure):
        pass


    _LUID_AND_ATTRIBUTES._fields_ = [
        ('Luid', LUID),
        ('Attributes', ULONG),
    ]
    LUID_AND_ATTRIBUTES = _LUID_AND_ATTRIBUTES
     PLUID_AND_ATTRIBUTES = POINTER(_LUID_AND_ATTRIBUTES)
    LUID_AND_ATTRIBUTES_ARRAY = LUID_AND_ATTRIBUTES * ANYSIZE_ARRAY
    PLUID_AND_ATTRIBUTES_ARRAY = POINTER(LUID_AND_ATTRIBUTES_ARRAY)

    # This is the *current* ACL revision
    ACL_REVISION = 2
    ACL_REVISION_DS = 4

    # This is the history of ACL revisions. Add a new one whenever
    # ACL_REVISION is updated
    ACL_REVISION1 = 1
    MIN_ACL_REVISION = ACL_REVISION2
    ACL_REVISION2 = 2
    ACL_REVISION3 = 3
    ACL_REVISION4 = 4
    MAX_ACL_REVISION = ACL_REVISION4
    class _ACL(ctypes.Structure):
        pass


    _ACL._fields_ = [
        ('AclRevision', UCHAR),
        ('Sbz1', UCHAR),
        ('AclSize', USHORT),
        ('AceCount', USHORT),
        ('Sbz2', USHORT),
    ]
    ACL = _ACL
    PACL = POINTER(ACL)

    # Current security descriptor revision value
    SECURITY_DESCRIPTOR_REVISION = 1
    SECURITY_DESCRIPTOR_REVISION1 = 1

    # Privilege attributes
    SE_PRIVILEGE_ENABLED_BY_DEFAULT = 0x00000001
    SE_PRIVILEGE_ENABLED = 0x00000002
    SE_PRIVILEGE_REMOVED = 0x00000004
    SE_PRIVILEGE_USED_FOR_ACCESS = 0x80000000
    SE_PRIVILEGE_VALID_ATTRIBUTES = (
        SE_PRIVILEGE_ENABLED_BY_DEFAULT |
        SE_PRIVILEGE_ENABLED |
        SE_PRIVILEGE_REMOVED |
        SE_PRIVILEGE_USED_FOR_ACCESS
    )

    # Privilege Set Control flags
    PRIVILEGE_SET_ALL_NECESSARY = 1

    # Privilege Set - This is defined for a privilege set of one.
    # If more than one privilege is needed, then this structure
    # will need to be allocated with more space.
    # Note: don't change this structure without fixing the
    # INITIAL_PRIVILEGE_SET
    # structure (defined in se.h)
    class _PRIVILEGE_SET(ctypes.Structure):
        pass


    _PRIVILEGE_SET._fields_ = [
        ('PrivilegeCount', ULONG),
        ('Control', ULONG),
        ('Privilege', LUID_AND_ATTRIBUTES * ANYSIZE_ARRAY),
    ]
    PRIVILEGE_SET = _PRIVILEGE_SET
     PPRIVILEGE_SET = POINTER(_PRIVILEGE_SET)

    # These must be converted to LUIDs before use.
    SE_MIN_WELL_KNOWN_PRIVILEGE = 2L
    SE_CREATE_TOKEN_PRIVILEGE = 2L
    SE_ASSIGNPRIMARYTOKEN_PRIVILEGE = 3L
    SE_LOCK_MEMORY_PRIVILEGE = 4L
    SE_INCREASE_QUOTA_PRIVILEGE = 5L
    SE_MACHINE_ACCOUNT_PRIVILEGE = 6L
    SE_TCB_PRIVILEGE = 7L
    SE_SECURITY_PRIVILEGE = 8L
    SE_TAKE_OWNERSHIP_PRIVILEGE = 9L
    SE_LOAD_DRIVER_PRIVILEGE = 10L
    SE_SYSTEM_PROFILE_PRIVILEGE = 11L
    SE_SYSTEMTIME_PRIVILEGE = 12L
    SE_PROF_SINGLE_PROCESS_PRIVILEGE = 13L
    SE_INC_BASE_PRIORITY_PRIVILEGE = 14L
    SE_CREATE_PAGEFILE_PRIVILEGE = 15L
    SE_CREATE_PERMANENT_PRIVILEGE = 16L
    SE_BACKUP_PRIVILEGE = 17L
    SE_RESTORE_PRIVILEGE = 18L
    SE_SHUTDOWN_PRIVILEGE = 19L
    SE_DEBUG_PRIVILEGE = 20L
    SE_AUDIT_PRIVILEGE = 21L
    SE_SYSTEM_ENVIRONMENT_PRIVILEGE = 22L
    SE_CHANGE_NOTIFY_PRIVILEGE = 23L
    SE_REMOTE_SHUTDOWN_PRIVILEGE = 24L
    SE_UNDOCK_PRIVILEGE = 25L
    SE_SYNC_AGENT_PRIVILEGE = 26L
    SE_ENABLE_DELEGATION_PRIVILEGE = 27L
    SE_MANAGE_VOLUME_PRIVILEGE = 28L
    SE_IMPERSONATE_PRIVILEGE = 29L
    SE_CREATE_GLOBAL_PRIVILEGE = 30L
    SE_TRUSTED_CREDMAN_ACCESS_PRIVILEGE = 31L
    SE_RELABEL_PRIVILEGE = 32L
    SE_INC_WORKING_SET_PRIVILEGE = 33L
    SE_TIME_ZONE_PRIVILEGE = 34L
    SE_CREATE_SYMBOLIC_LINK_PRIVILEGE = 35L
    SE_DELEGATE_SESSION_USER_IMPERSONATE_PRIVILEGE = 36L
    SE_MAX_WELL_KNOWN_PRIVILEGE = (
        SE_DELEGATE_SESSION_USER_IMPERSONATE_PRIVILEGE
    )

    # Impersonation Level
    # Impersonation level is represented by a pair of bits in Windows.
    # If a new impersonation level is added or lowest value is changed from
    # 0 to something else, fix the Windows CreateFile call.


    class _SECURITY_IMPERSONATION_LEVEL(ENUM):
        SecurityAnonymous = 1
        SecurityIdentification = 2
        SecurityImpersonation = 3
        SecurityDelegation = 4


    SECURITY_IMPERSONATION_LEVEL = _SECURITY_IMPERSONATION_LEVEL
    PSECURITY_IMPERSONATION_LEVEL = POINTER(_SECURITY_IMPERSONATION_LEVEL)
    SECURITY_MAX_IMPERSONATION_LEVEL = SecurityDelegation
    SECURITY_MIN_IMPERSONATION_LEVEL = SecurityAnonymous
    DEFAULT_IMPERSONATION_LEVEL = SecurityImpersonation


    def VALID_IMPERSONATION_LEVEL(L):
        return (L >= SECURITY_MIN_IMPERSONATION_LEVEL) and (L <= SECURITY_MAX_IMPERSONATION_LEVEL)

    # Security Tracking Mode
    SECURITY_DYNAMIC_TRACKING = TRUE
    SECURITY_STATIC_TRACKING = FALSE

    # Quality Of Service
    class _SECURITY_QUALITY_OF_SERVICE(ctypes.Structure):
        pass


    _SECURITY_QUALITY_OF_SERVICE._fields_ = [
        ('Length', ULONG),
        ('ImpersonationLevel', SECURITY_IMPERSONATION_LEVEL),
        ('ContextTrackingMode', SECURITY_CONTEXT_TRACKING_MODE),
        ('EffectiveOnly', BOOLEAN),
    ]
    SECURITY_QUALITY_OF_SERVICE = _SECURITY_QUALITY_OF_SERVICE
     PSECURITY_QUALITY_OF_SERVICE = POINTER(_SECURITY_QUALITY_OF_SERVICE)

    # Used to represent information related to a thread impersonation
    class _SE_IMPERSONATION_STATE(ctypes.Structure):
        pass


    _SE_IMPERSONATION_STATE._fields_ = [
        ('Token', PACCESS_TOKEN),
        ('CopyOnOpen', BOOLEAN),
        ('EffectiveOnly', BOOLEAN),
        ('Level', SECURITY_IMPERSONATION_LEVEL),
    ]
    SE_IMPERSONATION_STATE = _SE_IMPERSONATION_STATE
    PSE_IMPERSONATION_STATE = POINTER(_SE_IMPERSONATION_STATE)
    SECURITY_INFORMATION = ULONG
    PSECURITY_INFORMATION = POINTER(ULONG)
    OWNER_SECURITY_INFORMATION = 0x00000001
    GROUP_SECURITY_INFORMATION = 0x00000002
    DACL_SECURITY_INFORMATION = 0x00000004
    SACL_SECURITY_INFORMATION = 0x00000008
    LABEL_SECURITY_INFORMATION = 0x00000010
    ATTRIBUTE_SECURITY_INFORMATION = 0x00000020
    SCOPE_SECURITY_INFORMATION = 0x00000040
    PROCESS_TRUST_LABEL_SECURITY_INFORMATION = 0x00000080
    ACCESS_FILTER_SECURITY_INFORMATION = 0x00000100
    BACKUP_SECURITY_INFORMATION = 0x00010000
    PROTECTED_DACL_SECURITY_INFORMATION = 0x80000000
    PROTECTED_SACL_SECURITY_INFORMATION = 0x40000000
    UNPROTECTED_DACL_SECURITY_INFORMATION = 0x20000000
    UNPROTECTED_SACL_SECURITY_INFORMATION = 0x10000000

    if not defined(_NTLSA_IFS_):

        # All of this stuff (between the Ifndef _NTLSA_AUDIT_ and its endif)
        # were not
        # present in NTIFS prior to Windows Server 2003 SP1. All of the
        # definitions however
        # exist down to windows 2000
        # (except for the few exceptions noted in the code).
        if not defined(_NTLSA_AUDIT_):
            _NTLSA_AUDIT_ = 1

            # ///////////////////////////////////////////////////////////////////////
            #
            # //
            # Data types related to Auditing       //
            # //
            # ///////////////////////////////////////////////////////////////////////
            #
            # The following enumerated type is used between the reference
            # monitor and
            # LSA in the generation of audit messages. It is used to indicate
            # the
            # type of data being passed as a parameter from the reference
            # monitor
            # to LSA. LSA is responsible for transforming the specified data
            # type
            # into a set of unicode strings that are added to the event record
            # in
            # the audit log.


            class _SE_ADT_PARAMETER_TYPE(ENUM):
                SeAdtParmTypeNone = 0
                SeAdtParmTypeString = 1
                SeAdtParmTypeFileSpec = 2
                SeAdtParmTypeULONG = 3
                SeAdtParmTypeSid = 4
                SeAdtParmTypeLogonId = 5
                SeAdtParmTypeNoLogonId = 6
                SeAdtParmTypeAccessMask = 7
                SeAdtParmTypePrivs = 8
                SeAdtParmTypeObjectTypes = 9
                SeAdtParmTypeHexULONG = 10
                SeAdtParmTypePtr = 11
                SeAdtParmTypeTime = 12
                SeAdtParmTypeGuid = 13
                SeAdtParmTypeLuid = 14
                SeAdtParmTypeHexInt64 = 15
                SeAdtParmTypeStringList = 16
                SeAdtParmTypeSidList = 17
                SeAdtParmTypeDuration = 18
                SeAdtParmTypeUserAccountControl = 19
                SeAdtParmTypeNoUac = 20
                SeAdtParmTypeMessage = 21
                SeAdtParmTypeDateTime = 22
                SeAdtParmTypeSockAddr = 23
                SeAdtParmTypeSD = 24
                SeAdtParmTypeLogonHours = 25
                SeAdtParmTypeLogonIdNoSid = 26
                SeAdtParmTypeULONGNoConv = 27
                SeAdtParmTypeSockAddrNoPort = 28
                SeAdtParmTypeAccessReason = 29
                SeAdtParmTypeStagingReason = 30
                SeAdtParmTypeResourceAttribute = 31
                SeAdtParmTypeClaims = 32
                SeAdtParmTypeLogonIdAsSid = 33
                SeAdtParmTypeMultiSzString = 34
                SeAdtParmTypeLogonIdEx = 35


            SE_ADT_PARAMETER_TYPE = _SE_ADT_PARAMETER_TYPE
            PSE_ADT_PARAMETER_TYPE = POINTER(_SE_ADT_PARAMETER_TYPE)
            if not defined(GUID_DEFINED):
                pass
            # END IF  GUID_DEFINED
            class _SE_ADT_OBJECT_TYPE(ctypes.Structure):
                pass


            _SE_ADT_OBJECT_TYPE._fields_ = [
                ('ObjectType', GUID),
                ('Flags', USHORT),
                ('Level', USHORT),
                ('AccessMask', ACCESS_MASK),
            ]
            SE_ADT_OBJECT_TYPE = _SE_ADT_OBJECT_TYPE
            PSE_ADT_OBJECT_TYPE = POINTER(_SE_ADT_OBJECT_TYPE)
            class _SE_ADT_PARAMETER_ARRAY_ENTRY(ctypes.Structure):
                pass


            _SE_ADT_PARAMETER_ARRAY_ENTRY._fields_ = [
                ('Type', SE_ADT_PARAMETER_TYPE),
                ('Length', ULONG),
                ('Data', ULONG_PTR * 2),
                ('Address', PVOID),
            ]
            SE_ADT_PARAMETER_ARRAY_ENTRY = _SE_ADT_PARAMETER_ARRAY_ENTRY
            PSE_ADT_PARAMETER_ARRAY_ENTRY = POINTER(_SE_ADT_PARAMETER_ARRAY_ENTRY)
            class _SE_ADT_ACCESS_REASON(ctypes.Structure):
                pass


            _SE_ADT_ACCESS_REASON._fields_ = [
                ('AccessMask', ACCESS_MASK),
                ('AccessReasons', ULONG * 32),
                ('ObjectTypeIndex', ULONG),
                ('AccessGranted', ULONG),
                ('SecurityDescriptor', PSECURITY_DESCRIPTOR), # multple SDs may be stored here in self - relative way.
            ]
            SE_ADT_ACCESS_REASON = _SE_ADT_ACCESS_REASON
            PSE_ADT_ACCESS_REASON = POINTER(_SE_ADT_ACCESS_REASON)
            class _SE_ADT_CLAIMS(ctypes.Structure):
                pass


            _SE_ADT_CLAIMS._fields_ = [
                ('Length', ULONG),
                ('Claims', PCLAIMS_BLOB), # one claim blob will be stored here in self - relative way
            ]
            SE_ADT_CLAIMS = _SE_ADT_CLAIMS
            PSE_ADT_CLAIMS = POINTER(_SE_ADT_CLAIMS)

            # Structure that will be passed between the Reference Monitor and
            # LSA
            # to transmit auditing information.
            SE_MAX_AUDIT_PARAMETERS = 32
            SE_MAX_GENERIC_AUDIT_PARAMETERS = 28
            class _SE_ADT_PARAMETER_ARRAY(ctypes.Structure):
                pass


            _SE_ADT_PARAMETER_ARRAY._fields_ = [
                ('CategoryId', ULONG),
                ('AuditId', ULONG),
                ('ParameterCount', ULONG),
                ('Length', ULONG),
                ('FlatSubCategoryId', USHORT),
                ('Type', USHORT),
                ('Flags', ULONG),
                ('Parameters', SE_ADT_PARAMETER_ARRAY_ENTRY * SE_MAX_AUDIT_PARAMETERS),
            ]
            SE_ADT_PARAMETER_ARRAY = _SE_ADT_PARAMETER_ARRAY
            PSE_ADT_PARAMETER_ARRAY = POINTER(_SE_ADT_PARAMETER_ARRAY)
            class _SE_ADT_PARAMETER_ARRAY_EX(ctypes.Structure):
                pass


            _SE_ADT_PARAMETER_ARRAY_EX._fields_ = [
                ('CategoryId', ULONG),
                ('AuditId', ULONG),
                ('Version', ULONG),
                ('ParameterCount', ULONG),
                ('Length', ULONG),
                ('FlatSubCategoryId', USHORT),
                ('Type', USHORT),
                ('Flags', ULONG),
                ('Parameters', SE_ADT_PARAMETER_ARRAY_ENTRY * SE_MAX_AUDIT_PARAMETERS),
            ]
            SE_ADT_PARAMETER_ARRAY_EX = _SE_ADT_PARAMETER_ARRAY_EX
            PSE_ADT_PARAMETER_ARRAY_EX = POINTER(_SE_ADT_PARAMETER_ARRAY_EX)
            SE_ADT_PARAMETERS_SELF_RELATIVE = 0x00000001
            SE_ADT_PARAMETERS_SEND_TO_LSA = 0x00000002
            SE_ADT_PARAMETER_EXTENSIBLE_AUDIT = 0x00000004
            SE_ADT_PARAMETER_GENERIC_AUDIT = 0x00000008
            SE_ADT_PARAMETER_WRITE_SYNCHRONOUS = 0x00000010

            # This macro only existed in Windows Server 2008 and after


            def LSAP_SE_ADT_PARAMETER_ARRAY_TRUE_SIZE(AuditParameters):
                return (ctypes.sizeofSE_ADT_PARAMETER_ARRAY - ctypes.sizeofSE_ADT_PARAMETER_ARRAY_ENTRY * (SE_MAX_AUDIT_PARAMETERS - AuditParameters - >ParameterCount))
        # END IF   _NTLSA_AUDIT_    # END IF   _NTLSA_IFS_
    # Define the various device type values. Note that values used by Microsoft
    # Corporation are in the range 0 - 32767, and 32768 - 65535 are reserved
    # for use
    # by customers.
    DEVICE_TYPE = ULONG
    FILE_DEVICE_BEEP = 0x00000001
    FILE_DEVICE_CD_ROM = 0x00000002
    FILE_DEVICE_CD_ROM_FILE_SYSTEM = 0x00000003
    FILE_DEVICE_CONTROLLER = 0x00000004
    FILE_DEVICE_DATALINK = 0x00000005
    FILE_DEVICE_DFS = 0x00000006
    FILE_DEVICE_DISK = 0x00000007
    FILE_DEVICE_DISK_FILE_SYSTEM = 0x00000008
    FILE_DEVICE_FILE_SYSTEM = 0x00000009
    FILE_DEVICE_INPORT_PORT = 0x0000000A
    FILE_DEVICE_KEYBOARD = 0x0000000B
    FILE_DEVICE_MAILSLOT = 0x0000000C
    FILE_DEVICE_MIDI_IN = 0x0000000D
    FILE_DEVICE_MIDI_OUT = 0x0000000E
    FILE_DEVICE_MOUSE = 0x0000000F
    FILE_DEVICE_MULTI_UNC_PROVIDER = 0x00000010
    FILE_DEVICE_NAMED_PIPE = 0x00000011
    FILE_DEVICE_NETWORK = 0x00000012
    FILE_DEVICE_NETWORK_BROWSER = 0x00000013
    FILE_DEVICE_NETWORK_FILE_SYSTEM = 0x00000014
    FILE_DEVICE_NULL = 0x00000015
    FILE_DEVICE_PARALLEL_PORT = 0x00000016
    FILE_DEVICE_PHYSICAL_NETCARD = 0x00000017
    FILE_DEVICE_PRINTER = 0x00000018
    FILE_DEVICE_SCANNER = 0x00000019
    FILE_DEVICE_SERIAL_MOUSE_PORT = 0x0000001A
    FILE_DEVICE_SERIAL_PORT = 0x0000001B
    FILE_DEVICE_SCREEN = 0x0000001C
    FILE_DEVICE_SOUND = 0x0000001D
    FILE_DEVICE_STREAMS = 0x0000001E
    FILE_DEVICE_TAPE = 0x0000001F
    FILE_DEVICE_TAPE_FILE_SYSTEM = 0x00000020
    FILE_DEVICE_TRANSPORT = 0x00000021
    FILE_DEVICE_UNKNOWN = 0x00000022
    FILE_DEVICE_VIDEO = 0x00000023
    FILE_DEVICE_VIRTUAL_DISK = 0x00000024
    FILE_DEVICE_WAVE_IN = 0x00000025
    FILE_DEVICE_WAVE_OUT = 0x00000026
    FILE_DEVICE_8042_PORT = 0x00000027
    FILE_DEVICE_NETWORK_REDIRECTOR = 0x00000028
    FILE_DEVICE_BATTERY = 0x00000029
    FILE_DEVICE_BUS_EXTENDER = 0x0000002A
    FILE_DEVICE_MODEM = 0x0000002B
    FILE_DEVICE_VDM = 0x0000002C
    FILE_DEVICE_MASS_STORAGE = 0x0000002D
    FILE_DEVICE_SMB = 0x0000002E
    FILE_DEVICE_KS = 0x0000002F
    FILE_DEVICE_CHANGER = 0x00000030
    FILE_DEVICE_SMARTCARD = 0x00000031
    FILE_DEVICE_ACPI = 0x00000032
    FILE_DEVICE_DVD = 0x00000033
    FILE_DEVICE_FULLSCREEN_VIDEO = 0x00000034
    FILE_DEVICE_DFS_FILE_SYSTEM = 0x00000035
    FILE_DEVICE_DFS_VOLUME = 0x00000036
    FILE_DEVICE_SERENUM = 0x00000037
    FILE_DEVICE_TERMSRV = 0x00000038
    FILE_DEVICE_KSEC = 0x00000039
    FILE_DEVICE_FIPS = 0x0000003A
    FILE_DEVICE_INFINIBAND = 0x0000003B
    FILE_DEVICE_VMBUS = 0x0000003E
    FILE_DEVICE_CRYPT_PROVIDER = 0x0000003F
    FILE_DEVICE_WPD = 0x00000040
    FILE_DEVICE_BLUETOOTH = 0x00000041
    FILE_DEVICE_MT_COMPOSITE = 0x00000042
    FILE_DEVICE_MT_TRANSPORT = 0x00000043
    FILE_DEVICE_BIOMETRIC = 0x00000044
    FILE_DEVICE_PMI = 0x00000045
    FILE_DEVICE_EHSTOR = 0x00000046
    FILE_DEVICE_DEVAPI = 0x00000047
    FILE_DEVICE_GPIO = 0x00000048
    FILE_DEVICE_USBEX = 0x00000049
    FILE_DEVICE_CONSOLE = 0x00000050
    FILE_DEVICE_NFP = 0x00000051
    FILE_DEVICE_SYSENV = 0x00000052
    FILE_DEVICE_VIRTUAL_BLOCK = 0x00000053
    FILE_DEVICE_POINT_OF_SERVICE = 0x00000054
    FILE_DEVICE_STORAGE_REPLICATION = 0x00000055
    FILE_DEVICE_TRUST_ENV = 0x00000056
    FILE_DEVICE_UCM = 0x00000057
    FILE_DEVICE_UCMTCPCI = 0x00000058
    FILE_DEVICE_PERSISTENT_MEMORY = 0x00000059
    FILE_DEVICE_NVDIMM = 0x0000005A
    FILE_DEVICE_HOLOGRAPHIC = 0x0000005B
    FILE_DEVICE_SDFXHCI = 0x0000005C

    # Macro definition for defining IOCTL and FSCTL function control codes.
    # Note
    # that function codes 0 - 2047 are reserved for Microsoft Corporation, and
    # 2048 - 4095 are reserved for customers.


    def CTL_CODE(DeviceType, Function, Method, Access):
        return (DeviceType << 16) | (Access << 14) | (Function << 2) | Method

    # Macro to extract device type out of the device io control code


    def DEVICE_TYPE_FROM_CTL_CODE(ctrlCode):
        return ((ULONG(ctrlCode & 0xFFFF0000)) >> 16)

    # Macro to extract buffering method out of the device io control code


    def METHOD_FROM_CTL_CODE(ctrlCode):
        return ULONG(ctrlCode & 3)

    # Define the method codes for how buffers are passed for I/O and FS
    # controls
    METHOD_BUFFERED = 0
    METHOD_IN_DIRECT = 1
    METHOD_OUT_DIRECT = 2
    METHOD_NEITHER = 3

    # Define some easier to comprehend aliases:
    # METHOD_DIRECT_TO_HARDWARE (writes, aka METHOD_IN_DIRECT)
    # METHOD_DIRECT_FROM_HARDWARE (reads, aka METHOD_OUT_DIRECT)
    METHOD_DIRECT_TO_HARDWARE = METHOD_IN_DIRECT
    METHOD_DIRECT_FROM_HARDWARE = METHOD_OUT_DIRECT

    # Define the access check value for any access
    # The FILE_READ_ACCESS and FILE_WRITE_ACCESS constants are also defined in
    # ntioapi.h as FILE_READ_DATA and FILE_WRITE_DATA. The values for these
    # constants *MUST* always be in sync.
    # FILE_SPECIAL_ACCESS is checked by the NT I/O system the same as
    # FILE_ANY_ACCESS.
    # The file systems, however, may add additional access checks for I/O and
    # FS controls
    # that use this value.
    FILE_ANY_ACCESS = 0
    FILE_SPECIAL_ACCESS = FILE_ANY_ACCESS
    FILE_READ_ACCESS = 0x0001
    FILE_WRITE_ACCESS = 0x0002

    # begin_access
    # Define access rights to files and directories
    # The FILE_READ_DATA and FILE_WRITE_DATA constants are also defined in
    # devioctl.h as FILE_READ_ACCESS and FILE_WRITE_ACCESS. The values for
    # these
    # constants *MUST* always be in sync.
    # The values are redefined in devioctl.h because they must be available to
    # both DOS and NT.
    FILE_READ_DATA = 0x0001
    FILE_LIST_DIRECTORY = 0x0001
    FILE_WRITE_DATA = 0x0002
    FILE_ADD_FILE = 0x0002
    FILE_APPEND_DATA = 0x0004
    FILE_ADD_SUBDIRECTORY = 0x0004
    FILE_CREATE_PIPE_INSTANCE = 0x0004
    FILE_READ_EA = 0x0008
    FILE_WRITE_EA = 0x0010
    FILE_EXECUTE = 0x0020
    FILE_TRAVERSE = 0x0020
    FILE_DELETE_CHILD = 0x0040
    FILE_READ_ATTRIBUTES = 0x0080
    FILE_WRITE_ATTRIBUTES = 0x0100
    FILE_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0x1FF
    FILE_GENERIC_READ = (
        STANDARD_RIGHTS_READ |
        FILE_READ_DATA |
        FILE_READ_ATTRIBUTES |
        FILE_READ_EA |
        SYNCHRONIZE
    )
    FILE_GENERIC_WRITE = (
        STANDARD_RIGHTS_WRITE |
        FILE_WRITE_DATA |
        FILE_WRITE_ATTRIBUTES |
        FILE_WRITE_EA |
        FILE_APPEND_DATA |
        SYNCHRONIZE
    )
    FILE_GENERIC_EXECUTE = (
        STANDARD_RIGHTS_EXECUTE |
        FILE_READ_ATTRIBUTES |
        FILE_EXECUTE |
        SYNCHRONIZE
    )

    # end_access
    # Define share access rights to files and directories
    FILE_SHARE_READ = 0x00000001
    FILE_SHARE_WRITE = 0x00000002
    FILE_SHARE_DELETE = 0x00000004
    FILE_SHARE_VALID_FLAGS = 0x00000007

    # Define the file attributes values
    # Note: 0x00000008 is reserved for use for the old DOS VOLID (volume ID)
    # and is therefore not considered valid in NT.
    # Note: Note also that the order of these flags is set to allow both the
    # FAT and the Pinball File Systems to directly set the attributes
    # flags in attributes words without having to pick each flag out
    # individually. The order of these flags should not be changednot
    FILE_ATTRIBUTE_READONLY = 0x00000001
    FILE_ATTRIBUTE_HIDDEN = 0x00000002
    FILE_ATTRIBUTE_SYSTEM = 0x00000004

    # OLD DOS VOLID      0x00000008
    FILE_ATTRIBUTE_DIRECTORY = 0x00000010
    FILE_ATTRIBUTE_ARCHIVE = 0x00000020
    FILE_ATTRIBUTE_DEVICE = 0x00000040
    FILE_ATTRIBUTE_NORMAL = 0x00000080
    FILE_ATTRIBUTE_TEMPORARY = 0x00000100
    FILE_ATTRIBUTE_SPARSE_FILE = 0x00000200
    FILE_ATTRIBUTE_REPARSE_POINT = 0x00000400
    FILE_ATTRIBUTE_COMPRESSED = 0x00000800
    FILE_ATTRIBUTE_OFFLINE = 0x00001000
    FILE_ATTRIBUTE_NOT_CONTENT_INDEXED = 0x00002000
    FILE_ATTRIBUTE_ENCRYPTED = 0x00004000

    if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
        FILE_ATTRIBUTE_INTEGRITY_STREAM = 0x00008000
    # END IF
    # N.B. FILE_ATTRIBUTE_VIRTUAL is synthesized by LuaFV and not persisted
    # on disk by NTFS. See FILE_ATTRIBUTE_VALID_SET_FLAGS below.
    FILE_ATTRIBUTE_VIRTUAL = 0x00010000

    if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
        FILE_ATTRIBUTE_NO_SCRUB_DATA = 0x00020000
    # END IF

    if _WIN32_WINNT > _WIN32_WINNT_WINBLUE or (_WIN32_WINNT == _WIN32_WINNT_WINBLUE and defined(WINBLUE_KBSPRING14)):
        FILE_ATTRIBUTE_EA = 0x00040000
    # END IF

    if _WIN32_WINNT >= _WIN32_WINNT_WIN10_RS2:
        FILE_ATTRIBUTE_PINNED = 0x00080000
        FILE_ATTRIBUTE_UNPINNED = 0x00100000

        # This attribute only appears in directory enumeration classes
        # (FILE_DIRECTORY_INFORMATION,
        # FILE_BOTH_DIR_INFORMATION,
        # etc.). When this attribute is set, it means that the file or
        # directory has no physical representation on the local system; the
        # item is virtual. Opening the
        # item will be more expensive than normal, e.g. it will cause at least
        # some of it to be fetched
        # from a remote store.
        FILE_ATTRIBUTE_RECALL_ON_OPEN = 0x00040000

        # When this attribute is set, it means that the file or directory is
        # not fully present locally.
        # For a file that means that not all of its data is on local storage
        # (e.g. it is sparse with some
        # data still in remote
        # storage). For a directory it means that some of the directory contents are
        #
        # being virtualized from another location. Reading the file /
        # enumerating the directory will be
        # more expensive than normal, e.g. it will cause at least some of the
        # file/directory content to be
        # fetched from a remote store. Only kernel - mode callers can set this
        # bit.
        FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS = 0x00400000

        # Attributes for FILE_CREATE_TREE_CONNECT opens. These overlap with
        # FILE_ATTRIBUTE_xyz values.
        TREE_CONNECT_ATTRIBUTE_PRIVACY = 0x00004000
        TREE_CONNECT_ATTRIBUTE_INTEGRITY = 0x00008000
        TREE_CONNECT_ATTRIBUTE_GLOBAL = 0x00000004
    # END IF

    if _WIN32_WINNT >= _WIN32_WINNT_WIN10_RS3:

        # The value of this flag is chosen to overlap with an internal bit
        # used by NTFS.
        FILE_ATTRIBUTE_STRICTLY_SEQUENTIAL = 0x20000000
    # END IF

    if _WIN32_WINNT < _WIN32_WINNT_WIN8:
        FILE_ATTRIBUTE_VALID_FLAGS = 0x00007FB7
        FILE_ATTRIBUTE_VALID_SET_FLAGS = 0x000031A7
    elif _WIN32_WINNT < _WIN32_WINNT_WIN10_RS2:
        FILE_ATTRIBUTE_VALID_FLAGS = 0x0002FFB7
        FILE_ATTRIBUTE_VALID_SET_FLAGS = 0x000231A7
    elif _WIN32_WINNT < _WIN32_WINNT_WIN10_RS3:
        FILE_ATTRIBUTE_VALID_FLAGS = 0x005AFFB7
        FILE_ATTRIBUTE_VALID_SET_FLAGS = 0x001A31A7

        # This mask describes the set of attributes that kernel - mode callers
        # may set.
        FILE_ATTRIBUTE_VALID_KERNEL_SET_FLAGS = 0x005A31A7
    else:
        FILE_ATTRIBUTE_VALID_FLAGS = 0x005AFFB7
        FILE_ATTRIBUTE_VALID_SET_FLAGS = 0x001A31A7

        # This mask describes the set of attributes that kernel - mode callers
        # may set.
        FILE_ATTRIBUTE_VALID_KERNEL_SET_FLAGS = 0x005A31A7
    # END IF
    # Define the create disposition values
    FILE_SUPERSEDE = 0x00000000
    FILE_OPEN = 0x00000001
    FILE_CREATE = 0x00000002
    FILE_OPEN_IF = 0x00000003
    FILE_OVERWRITE = 0x00000004
    FILE_OVERWRITE_IF = 0x00000005
    FILE_MAXIMUM_DISPOSITION = 0x00000005

    # Define the create/open option flags
    FILE_DIRECTORY_FILE = 0x00000001
    FILE_WRITE_THROUGH = 0x00000002
    FILE_SEQUENTIAL_ONLY = 0x00000004
    FILE_NO_INTERMEDIATE_BUFFERING = 0x00000008
    FILE_SYNCHRONOUS_IO_ALERT = 0x00000010
    FILE_SYNCHRONOUS_IO_NONALERT = 0x00000020
    FILE_NON_DIRECTORY_FILE = 0x00000040
    FILE_CREATE_TREE_CONNECTION = 0x00000080
    FILE_COMPLETE_IF_OPLOCKED = 0x00000100
    FILE_NO_EA_KNOWLEDGE = 0x00000200
    FILE_OPEN_REMOTE_INSTANCE = 0x00000400
    FILE_RANDOM_ACCESS = 0x00000800
    FILE_DELETE_ON_CLOSE = 0x00001000
    FILE_OPEN_BY_FILE_ID = 0x00002000
    FILE_OPEN_FOR_BACKUP_INTENT = 0x00004000
    FILE_NO_COMPRESSION = 0x00008000

    if NTDDI_VERSION >= NTDDI_WIN7:
        FILE_OPEN_REQUIRING_OPLOCK = 0x00010000
        FILE_DISALLOW_EXCLUSIVE = 0x00020000
    # END IF  NTDDI_VERSION >= NTDDI_WIN7

    if NTDDI_VERSION >= NTDDI_WIN8:
        FILE_SESSION_AWARE = 0x00040000
    # END IF  NTDDI_VERSION >= NTDDI_WIN8
    FILE_RESERVE_OPFILTER = 0x00100000
    FILE_OPEN_REPARSE_POINT = 0x00200000
    FILE_OPEN_NO_RECALL = 0x00400000
    FILE_OPEN_FOR_FREE_SPACE_QUERY = 0x00800000

    # The FILE_VALID_OPTION_FLAGS mask cannot be expanded to include the
    # highest 8 bits of the DWORD because those are used to represent the
    # create disposition in the IO Request Packet when sending information
    # to the file system
    FILE_VALID_OPTION_FLAGS = 0x00FFFFFF
    FILE_VALID_PIPE_OPTION_FLAGS = 0x00000032
    FILE_VALID_MAILSLOT_OPTION_FLAGS = 0x00000032
    FILE_VALID_SET_FLAGS = 0x00000036

    # Define the I/O status information return values for
    # NtCreateFile/NtOpenFile
    FILE_SUPERSEDED = 0x00000000
    FILE_OPENED = 0x00000001
    FILE_CREATED = 0x00000002
    FILE_OVERWRITTEN = 0x00000003
    FILE_EXISTS = 0x00000004
    FILE_DOES_NOT_EXIST = 0x00000005

    if NTDDI_VERSION >= NTDDI_WIN10_RS3:

        # Define the QueryFlags values for NtQueryDirectoryFileEx.
        FILE_QUERY_RESTART_SCAN = 0x00000001
        FILE_QUERY_RETURN_SINGLE_ENTRY = 0x00000002
        FILE_QUERY_INDEX_SPECIFIED = 0x00000004
        FILE_QUERY_RETURN_ON_DISK_ENTRIES_ONLY = 0x00000008
    # END IF
    # Define special ByteOffset parameters for read and write operations
    FILE_WRITE_TO_END_OF_FILE = 0xFFFFFFFF
    FILE_USE_FILE_POINTER_POSITION = 0xFFFFFFFE

    # Define alignment requirement values
    FILE_BYTE_ALIGNMENT = 0x00000000
    FILE_WORD_ALIGNMENT = 0x00000001
    FILE_LONG_ALIGNMENT = 0x00000003
    FILE_QUAD_ALIGNMENT = 0x00000007
    FILE_OCTA_ALIGNMENT = 0x0000000F
    FILE_32_BYTE_ALIGNMENT = 0x0000001F
    FILE_64_BYTE_ALIGNMENT = 0x0000003F
    FILE_128_BYTE_ALIGNMENT = 0x0000007F
    FILE_256_BYTE_ALIGNMENT = 0x000000FF
    FILE_512_BYTE_ALIGNMENT = 0x000001FF

    # Define the maximum length of a filename string
    MAXIMUM_FILENAME_LENGTH = 256

    # Define the various device CHARacteristics flags
    FILE_REMOVABLE_MEDIA = 0x00000001
    FILE_READ_ONLY_DEVICE = 0x00000002
    FILE_FLOPPY_DISKETTE = 0x00000004
    FILE_WRITE_ONCE_MEDIA = 0x00000008
    FILE_REMOTE_DEVICE = 0x00000010
    FILE_DEVICE_IS_MOUNTED = 0x00000020
    FILE_VIRTUAL_VOLUME = 0x00000040
    FILE_AUTOGENERATED_DEVICE_NAME = 0x00000080
    FILE_DEVICE_SECURE_OPEN = 0x00000100
    FILE_CHARACTERISTIC_PNP_DEVICE = 0x00000800
    FILE_CHARACTERISTIC_TS_DEVICE = 0x00001000
    FILE_CHARACTERISTIC_WEBDAV_DEVICE = 0x00002000
    FILE_CHARACTERISTIC_CSV = 0x00010000
    FILE_DEVICE_ALLOW_APPCONTAINER_TRAVERSAL = 0x00020000
    FILE_PORTABLE_DEVICE = 0x00040000

    # Define the base asynchronous I/O argument types
    class _IO_STATUS_BLOCK(ctypes.Structure):
        pass


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('Status', NTSTATUS),
        ('Pointer', PVOID),
    ]
    _IO_STATUS_BLOCK.DUMMYUNIONNAME = DUMMYUNIONNAME
    _IO_STATUS_BLOCK._fields_ = [
        ('DUMMYUNIONNAME', _IO_STATUS_BLOCK.DUMMYUNIONNAME),
        ('Information', ULONG_PTR),
    ]
    IO_STATUS_BLOCK = _IO_STATUS_BLOCK
    PIO_STATUS_BLOCK = POINTER(_IO_STATUS_BLOCK)
    class _IO_STATUS_BLOCK32(ctypes.Structure):
        pass


    _IO_STATUS_BLOCK32._fields_ = [
        ('Status', NTSTATUS),
        ('Information', ULONG),
    ]
    IO_STATUS_BLOCK32 = _IO_STATUS_BLOCK32
    PIO_STATUS_BLOCK32 = POINTER(_IO_STATUS_BLOCK32)

    # Define an Asynchronous Procedure Call from I/O viewpoint
    PIO_APC_ROUTINE_DEFINED = 1

    # Define the session states and events


    class _IO_SESSION_EVENT(ENUM):
        IoSessionEventIgnore = 0
        IoSessionEventCreated = 1
        IoSessionEventTerminated = 2
        IoSessionEventConnected = 3
        IoSessionEventDisconnected = 4
        IoSessionEventLogon = 5
        IoSessionEventLogoff = 6
        IoSessionEventMax = 7


    IO_SESSION_EVENT = _IO_SESSION_EVENT
    PIO_SESSION_EVENT = POINTER(_IO_SESSION_EVENT)
    class _IO_SESSION_STATE(ENUM):
        IoSessionStateCreated = 1
        IoSessionStateInitialized = 2
        IoSessionStateConnected = 3
        IoSessionStateDisconnected = 4
        IoSessionStateDisconnectedLoggedOn = 5
        IoSessionStateLoggedOn = 6
        IoSessionStateLoggedOff = 7
        IoSessionStateTerminated = 8
        IoSessionStateMax = 9


    IO_SESSION_STATE = _IO_SESSION_STATE
    PIO_SESSION_STATE = POINTER(_IO_SESSION_STATE)

    # Define masks that determine which events a driver that registers for
    # callbacks care about
    IO_SESSION_STATE_ALL_EVENTS = 0xFFFFFFFF
    IO_SESSION_STATE_CREATION_EVENT = 0x00000001
    IO_SESSION_STATE_TERMINATION_EVENT = 0x00000002
    IO_SESSION_STATE_CONNECT_EVENT = 0x00000004
    IO_SESSION_STATE_DISCONNECT_EVENT = 0x00000008
    IO_SESSION_STATE_LOGON_EVENT = 0x00000010
    IO_SESSION_STATE_LOGOFF_EVENT = 0x00000020
    IO_SESSION_STATE_VALID_EVENT_MASK = 0x0000003F
    IO_SESSION_MAX_PAYLOAD_SIZE = 256L

    # Payload structures
    # IoSessionEventConnected
    class _IO_SESSION_CONNECT_INFO(ctypes.Structure):
        pass


    _IO_SESSION_CONNECT_INFO._fields_ = [
        ('SessionId', ULONG),
        ('LocalSession', BOOLEAN),
    ]
    IO_SESSION_CONNECT_INFO = _IO_SESSION_CONNECT_INFO
    PIO_SESSION_CONNECT_INFO = POINTER(_IO_SESSION_CONNECT_INFO)

    # Define the file information class values
    # WARNING: The order of the following values are assumed by the I/O system.
    # Any changes made here should be reflected there as well.


    class _FILE_INFORMATION_CLASS(ENUM):
        FileDirectoryInformation = 1
        FileFullDirectoryInformation = 2
        FileBothDirectoryInformation = 3
        FileBasicInformation = 4
        FileStandardInformation = 5
        FileInternalInformation = 6
        FileEaInformation = 7
        FileAccessInformation = 8
        FileNameInformation = 9
        FileRenameInformation = 10
        FileLinkInformation = 11
        FileNamesInformation = 12
        FileDispositionInformation = 13
        FilePositionInformation = 14
        FileFullEaInformation = 15
        FileModeInformation = 16
        FileAlignmentInformation = 17
        FileAllInformation = 18
        FileAllocationInformation = 19
        FileEndOfFileInformation = 20
        FileAlternateNameInformation = 21
        FileStreamInformation = 22
        FilePipeInformation = 23
        FilePipeLocalInformation = 24
        FilePipeRemoteInformation = 25
        FileMailslotQueryInformation = 26
        FileMailslotSetInformation = 27
        FileCompressionInformation = 28
        FileObjectIdInformation = 29
        FileCompletionInformation = 30
        FileMoveClusterInformation = 31
        FileQuotaInformation = 32
        FileReparsePointInformation = 33
        FileNetworkOpenInformation = 34
        FileAttributeTagInformation = 35
        FileTrackingInformation = 36
        FileIdBothDirectoryInformation = 37
        FileIdFullDirectoryInformation = 38
        FileValidDataLengthInformation = 39
        FileShortNameInformation = 40
        FileIoCompletionNotificationInformation = 41
        FileIoStatusBlockRangeInformation = 42
        FileIoPriorityHintInformation = 43
        FileSfioReserveInformation = 44
        FileSfioVolumeInformation = 45
        FileHardLinkInformation = 46
        FileProcessIdsUsingFileInformation = 47
        FileNormalizedNameInformation = 48
        FileNetworkPhysicalNameInformation = 49
        FileIdGlobalTxDirectoryInformation = 50
        FileIsRemoteDeviceInformation = 51
        FileUnusedInformation = 52
        FileNumaNodeInformation = 53
        FileStandardLinkInformation = 54
        FileRemoteProtocolInformation = 55
        FileRenameInformationBypassAccessCheck = 56
        FileLinkInformationBypassAccessCheck = 57
        FileVolumeNameInformation = 58
        FileIdInformation = 59
        FileIdExtdDirectoryInformation = 60
        FileReplaceCompletionInformation = 61
        FileHardLinkFullIdInformation = 62
        FileIdExtdBothDirectoryInformation = 63
        FileDispositionInformationEx = 64
        FileRenameInformationEx = 65
        FileRenameInformationExBypassAccessCheck = 66
        FileDesiredStorageClassInformation = 67
        FileStatInformation = 68
        FileMemoryPartitionInformation = 69
        FileStatLxInformation = 70
        FileCaseSensitiveInformation = 71
        FileMaximumInformation = 72


    FILE_INFORMATION_CLASS = _FILE_INFORMATION_CLASS
    PFILE_INFORMATION_CLASS = POINTER(_FILE_INFORMATION_CLASS)
    class _DIRECTORY_NOTIFY_INFORMATION_CLASS(ENUM):
        DirectoryNotifyInformation = 1
        DirectoryNotifyExtendedInformation = 2


    DIRECTORY_NOTIFY_INFORMATION_CLASS = _DIRECTORY_NOTIFY_INFORMATION_CLASS
    PDIRECTORY_NOTIFY_INFORMATION_CLASS = POINTER(_DIRECTORY_NOTIFY_INFORMATION_CLASS)

    # Define the various structures which are returned on query operations
    class _FILE_BASIC_INFORMATION(ctypes.Structure):
        pass


    _FILE_BASIC_INFORMATION._fields_ = [
        ('CreationTime', LARGE_INTEGER),
        ('LastAccessTime', LARGE_INTEGER),
        ('LastWriteTime', LARGE_INTEGER),
        ('ChangeTime', LARGE_INTEGER),
        ('FileAttributes', ULONG),
    ]
    FILE_BASIC_INFORMATION = _FILE_BASIC_INFORMATION
    PFILE_BASIC_INFORMATION = POINTER(_FILE_BASIC_INFORMATION)
    class _FILE_STANDARD_INFORMATION(ctypes.Structure):
        pass


    _FILE_STANDARD_INFORMATION._fields_ = [
        ('AllocationSize', LARGE_INTEGER),
        ('EndOfFile', LARGE_INTEGER),
        ('NumberOfLinks', ULONG),
        ('DeletePending', BOOLEAN),
        ('Directory', BOOLEAN),
    ]
    FILE_STANDARD_INFORMATION = _FILE_STANDARD_INFORMATION
    PFILE_STANDARD_INFORMATION = POINTER(_FILE_STANDARD_INFORMATION)
    if _WIN32_WINNT >= _WIN32_WINNT_WINTHRESHOLD:
        class _FILE_STANDARD_INFORMATION_EX(ctypes.Structure):
            pass


        _FILE_STANDARD_INFORMATION_EX._fields_ = [
            ('AllocationSize', LARGE_INTEGER),
            ('EndOfFile', LARGE_INTEGER),
            ('NumberOfLinks', ULONG),
            ('DeletePending', BOOLEAN),
            ('Directory', BOOLEAN),
            ('AlternateStream', BOOLEAN),
            ('MetadataAttribute', BOOLEAN),
        ]
        FILE_STANDARD_INFORMATION_EX = _FILE_STANDARD_INFORMATION_EX
        PFILE_STANDARD_INFORMATION_EX = POINTER(_FILE_STANDARD_INFORMATION_EX)
    # END IF
    class _FILE_POSITION_INFORMATION(ctypes.Structure):
        pass


    _FILE_POSITION_INFORMATION._fields_ = [
        ('CurrentByteOffset', LARGE_INTEGER),
    ]
    FILE_POSITION_INFORMATION = _FILE_POSITION_INFORMATION
    PFILE_POSITION_INFORMATION = POINTER(_FILE_POSITION_INFORMATION)
    class _FILE_NETWORK_OPEN_INFORMATION(ctypes.Structure):
        pass


    _FILE_NETWORK_OPEN_INFORMATION._fields_ = [
        ('CreationTime', LARGE_INTEGER),
        ('LastAccessTime', LARGE_INTEGER),
        ('LastWriteTime', LARGE_INTEGER),
        ('ChangeTime', LARGE_INTEGER),
        ('AllocationSize', LARGE_INTEGER),
        ('EndOfFile', LARGE_INTEGER),
        ('FileAttributes', ULONG),
    ]
    FILE_NETWORK_OPEN_INFORMATION = _FILE_NETWORK_OPEN_INFORMATION
    PFILE_NETWORK_OPEN_INFORMATION = POINTER(_FILE_NETWORK_OPEN_INFORMATION)
    class _FILE_FULL_EA_INFORMATION(ctypes.Structure):
        pass


    _FILE_FULL_EA_INFORMATION._fields_ = [
        ('NextEntryOffset', ULONG),
        ('Flags', UCHAR),
        ('EaNameLength', UCHAR),
        ('EaValueLength', USHORT),
        ('EaName', CHAR * 1),
    ]
    FILE_FULL_EA_INFORMATION = _FILE_FULL_EA_INFORMATION
    PFILE_FULL_EA_INFORMATION = POINTER(_FILE_FULL_EA_INFORMATION)

    # Support to reserve bandwidth for a file handle.
    class _FILE_SFIO_RESERVE_INFORMATION(ctypes.Structure):
        pass


    _FILE_SFIO_RESERVE_INFORMATION._fields_ = [
        ('RequestsPerPeriod', ULONG),
        ('Period', ULONG),
        ('RetryFailures', BOOLEAN),
        ('Discardable', BOOLEAN),
        ('RequestSize', ULONG),
        ('NumOutstandingRequests', ULONG),
    ]
    FILE_SFIO_RESERVE_INFORMATION = _FILE_SFIO_RESERVE_INFORMATION
    PFILE_SFIO_RESERVE_INFORMATION = POINTER(_FILE_SFIO_RESERVE_INFORMATION)

    # Support to query bandwidth properties of a volume.
    class _FILE_SFIO_VOLUME_INFORMATION(ctypes.Structure):
        pass


    _FILE_SFIO_VOLUME_INFORMATION._fields_ = [
        ('MaximumRequestsPerPeriod', ULONG),
        ('MinimumPeriod', ULONG),
        ('MinimumTransferSize', ULONG),
    ]
    FILE_SFIO_VOLUME_INFORMATION = _FILE_SFIO_VOLUME_INFORMATION
    PFILE_SFIO_VOLUME_INFORMATION = POINTER(_FILE_SFIO_VOLUME_INFORMATION)

    # Support to set priority hints on a filehandle.
    class _IO_PRIORITY_HINT(ENUM):
        IoPriorityVeryLow = 0
        IoPriorityLow = 1
        IoPriorityNormal = 2
        IoPriorityHigh = 3
        IoPriorityCritical = 4
        MaxIoPriorityTypes = 5


    IO_PRIORITY_HINT = _IO_PRIORITY_HINT
    class _FILE_IO_PRIORITY_HINT_INFORMATION(ctypes.Structure):
        pass


    _FILE_IO_PRIORITY_HINT_INFORMATION._fields_ = [
        ('PriorityHint', IO_PRIORITY_HINT),
    ]
    FILE_IO_PRIORITY_HINT_INFORMATION = _FILE_IO_PRIORITY_HINT_INFORMATION
    PFILE_IO_PRIORITY_HINT_INFORMATION = POINTER(_FILE_IO_PRIORITY_HINT_INFORMATION)
    class _FILE_IO_PRIORITY_HINT_INFORMATION_EX(ctypes.Structure):
        pass


    _FILE_IO_PRIORITY_HINT_INFORMATION_EX._fields_ = [
        ('PriorityHint', IO_PRIORITY_HINT),
        ('BoostOutstanding', BOOLEAN),
    ]
    FILE_IO_PRIORITY_HINT_INFORMATION_EX = _FILE_IO_PRIORITY_HINT_INFORMATION_EX
    PFILE_IO_PRIORITY_HINT_INFORMATION_EX = POINTER(_FILE_IO_PRIORITY_HINT_INFORMATION_EX)

    # Don't queue an entry to an associated completion port if returning
    # success
    # synchronously.
    FILE_SKIP_COMPLETION_PORT_ON_SUCCESS = 0x1

    # Don't set the file handle event on IO completion.
    FILE_SKIP_SET_EVENT_ON_HANDLE = 0x2

    # Don't set user supplied event on successful fast - path IO completion.
    FILE_SKIP_SET_USER_EVENT_ON_FAST_IO = 0x4
    class _FILE_IS_REMOTE_DEVICE_INFORMATION(ctypes.Structure):
        pass


    _FILE_IS_REMOTE_DEVICE_INFORMATION._fields_ = [
        ('IsRemote', BOOLEAN),
    ]
    FILE_IS_REMOTE_DEVICE_INFORMATION = _FILE_IS_REMOTE_DEVICE_INFORMATION
    PFILE_IS_REMOTE_DEVICE_INFORMATION = POINTER(_FILE_IS_REMOTE_DEVICE_INFORMATION)
    class _FILE_NUMA_NODE_INFORMATION(ctypes.Structure):
        pass


    _FILE_NUMA_NODE_INFORMATION._fields_ = [
        ('NodeNumber', USHORT),
    ]
    FILE_NUMA_NODE_INFORMATION = _FILE_NUMA_NODE_INFORMATION
    PFILE_NUMA_NODE_INFORMATION = POINTER(_FILE_NUMA_NODE_INFORMATION)

    # Set an range of IOSBs on a file handle.
    class _FILE_IOSTATUSBLOCK_RANGE_INFORMATION(ctypes.Structure):
        pass


    _FILE_IOSTATUSBLOCK_RANGE_INFORMATION._fields_ = [
        ('IoStatusBlockRange', PUCHAR),
        ('Length', ULONG),
    ]
    FILE_IOSTATUSBLOCK_RANGE_INFORMATION = _FILE_IOSTATUSBLOCK_RANGE_INFORMATION
    PFILE_IOSTATUSBLOCK_RANGE_INFORMATION = POINTER(_FILE_IOSTATUSBLOCK_RANGE_INFORMATION)

    if _WIN32_WINNT >= _WIN32_WINNT_WIN10_RS3:
        class _FILE_MEMORY_PARTITION_INFORMATION(ctypes.Structure):
            pass


        class Flags(ctypes.Structure):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('NoCrossPartitionAccess', UCHAR),
            ('Spare', UCHAR * 3),
        ]
        Flags.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        Flags._fields_ = [
            ('DUMMYSTRUCTNAME', Flags.DUMMYSTRUCTNAME),
            ('AllFlags', ULONG),
        ]
        _FILE_MEMORY_PARTITION_INFORMATION.Flags = Flags
        _FILE_MEMORY_PARTITION_INFORMATION._fields_ = [
            ('OwnerPartitionHandle', ULONG_PTR),
            ('Flags', _FILE_MEMORY_PARTITION_INFORMATION.Flags),
        ]
        FILE_MEMORY_PARTITION_INFORMATION = _FILE_MEMORY_PARTITION_INFORMATION
        PFILE_MEMORY_PARTITION_INFORMATION = POINTER(_FILE_MEMORY_PARTITION_INFORMATION)
    # END IF
    # Define the file system information class values
    # WARNING: The order of the following values are assumed by the I/O system.
    # Any changes made here should be reflected there as well.
    class _FSINFOCLASS(ENUM):
        FileFsVolumeInformation = 1
        FileFsLabelInformation = 2
        FileFsSizeInformation = 3
        FileFsDeviceInformation = 4
        FileFsAttributeInformation = 5
        FileFsControlInformation = 6
        FileFsFullSizeInformation = 7
        FileFsObjectIdInformation = 8
        FileFsDriverPathInformation = 9
        FileFsVolumeFlagsInformation = 10
        FileFsSectorSizeInformation = 11
        FileFsDataCopyInformation = 12
        FileFsMetadataSizeInformation = 13
        FileFsMaximumInformation = 14


    FS_INFORMATION_CLASS = _FSINFOCLASS
    PFS_INFORMATION_CLASS = POINTER(_FSINFOCLASS)
    class _FILE_FS_DEVICE_INFORMATION(ctypes.Structure):
        pass


    _FILE_FS_DEVICE_INFORMATION._fields_ = [
        ('DeviceType', DEVICE_TYPE),
        ('Characteristics', ULONG),
    ]
    FILE_FS_DEVICE_INFORMATION = _FILE_FS_DEVICE_INFORMATION
    PFILE_FS_DEVICE_INFORMATION = POINTER(_FILE_FS_DEVICE_INFORMATION)

    # Define segement buffer structure for scatter/gather read/write.
    class _FILE_SEGMENT_ELEMENT(ctypes.Union):
        pass


    _FILE_SEGMENT_ELEMENT._fields_ = [
        ('Buffer', PVOID64),
        ('Alignment', ULONGLONG),
    ]
    FILE_SEGMENT_ELEMENT = _FILE_SEGMENT_ELEMENT
    PFILE_SEGMENT_ELEMENT = POINTER(_FILE_SEGMENT_ELEMENT)
    if NTDDI_VERSION >= NTDDI_WIN8:

        # Flag defintions for NtFlushBuffersFileEx
        # If none of the below flags are specified the following will occur
        # for a
        # given file handle:
        # - Write any modified data for the given file from the Windows in -
        # memory
        # cache.
        # - Commit all pending metadata changes for the given file from the
        # Windows in - memory cache.
        # - Send a SYNC command to the underlying storage device to commit all
        # written data in the devices cache to persistent storage.
        # If a volume handle is specified:
        # - Write all modified data for all files on the volume from the
        # Windows
        # in - memory cache.
        # - Commit all pending metadata changes for all files on the volume
        # from
        # the Windows in - memory cache.
        # - Send a SYNC command to the underlying storage device to commit all
        # written data in the devices cache to persistent storage.
        # This is equivalent to how NtFlushBuffersFile has always worked.
        # If set, this operation will write the data for the given file from
        # the
        # Windows in - memory cache. This will NOT commit any associated
        # metadata
        # changes. This will NOT send a SYNC to the storage device to flush its
        # cache. Not supported on volume handles. Only supported by the NTFS
        # filesystem.
        FLUSH_FLAGS_FILE_DATA_ONLY = 0x00000001

        # If set, this operation will commit both the data and metadata
        # changes for
        # the given file from the Windows in - memory cache. This will NOT
        # send a SYNC
        # to the storage device to flush its cache. Not supported on volume
        # handles.
        # Only supported by the NTFS filesystem.
        FLUSH_FLAGS_NO_SYNC = 0x00000002
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    if NTDDI_VERSION >= NTDDI_WIN10_RS1:

        # If set, this operation will write the data for the given file from
        # the
        # Windows in - memory cache. It will also try to skip updating the
        # timestamp
        # as much as possible. This will send a SYNC to the storage device to
        # flush its
        # cache. Not supported on volume or directory handles. Only supported
        # by the NTFS
        # filesystem.
        FLUSH_FLAGS_FILE_DATA_SYNC_ONLY = 0x00000004
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS1)
    # Define the I/O bus interface types.


    class _INTERFACE_TYPE(ENUM):
        InterfaceTypeUndefined = - 1
        Internal = 0
        Isa = 1
        Eisa = 2
        MicroChannel = 3
        TurboChannel = 4
        PCIBus = 5
        VMEBus = 6
        NuBus = 7
        PCMCIABus = 8
        CBus = 9
        MPIBus = 10
        MPSABus = 11
        ProcessorInternal = 12
        InternalPowerBus = 13
        PNPISABus = 14
        PNPBus = 15
        Vmcs = 16
        ACPIBus = 17
        MaximumInterfaceType = 18


    INTERFACE_TYPE = _INTERFACE_TYPE
    PINTERFACE_TYPE = POINTER(_INTERFACE_TYPE)

    # Define the DMA transfer widths.
    class _DMA_WIDTH(ENUM):
        Width8Bits = 1
        Width16Bits = 2
        Width32Bits = 3
        Width64Bits = 4
        WidthNoWrap = 5
        MaximumDmaWidth = 6


    DMA_WIDTH = _DMA_WIDTH
    PDMA_WIDTH = POINTER(_DMA_WIDTH)

    # Define DMA transfer speeds.
    class _DMA_SPEED(ENUM):
        Compatible = 1
        TypeA = 2
        TypeB = 3
        TypeC = 4
        TypeF = 5
        MaximumDmaSpeed = 6


    DMA_SPEED = _DMA_SPEED
    PDMA_SPEED = POINTER(_DMA_SPEED)

    # Define Interface reference/dereference routines for
    # Interfaces exported by IRP_MN_QUERY_INTERFACE
    (*PINTERFACE_REFERENCE)(PVOID = VOID
    Context) = VOID
    (*PINTERFACE_DEREFERENCE)(PVOID = VOID
    Context) = VOID

    # Define I/O Driver error log packet structure. This structure is filled in
    # by the driver.
    class _IO_ERROR_LOG_PACKET(ctypes.Structure):
        pass


    _IO_ERROR_LOG_PACKET._fields_ = [
        ('MajorFunctionCode', UCHAR),
        ('RetryCount', UCHAR),
        ('DumpDataSize', USHORT),
        ('NumberOfStrings', USHORT),
        ('StringOffset', USHORT),
        ('EventCategory', USHORT),
        ('ErrorCode', NTSTATUS),
        ('UniqueErrorValue', ULONG),
        ('FinalStatus', NTSTATUS),
        ('SequenceNumber', ULONG),
        ('IoControlCode', ULONG),
        ('DeviceOffset', LARGE_INTEGER),
        ('DumpData', ULONG * 1),
    ]
    IO_ERROR_LOG_PACKET = _IO_ERROR_LOG_PACKET
    PIO_ERROR_LOG_PACKET = POINTER(_IO_ERROR_LOG_PACKET)

    # Define the I/O error log message. This message is sent by the error log
    # thread over the lpc port.
    class _IO_ERROR_LOG_MESSAGE(ctypes.Structure):
        pass


    _IO_ERROR_LOG_MESSAGE._fields_ = [
        ('Type', USHORT),
        ('Size', USHORT),
        ('DriverNameLength', USHORT),
        ('TimeStamp', LARGE_INTEGER),
        ('DriverNameOffset', ULONG),
        ('EntryData', IO_ERROR_LOG_PACKET),
    ]
    IO_ERROR_LOG_MESSAGE = _IO_ERROR_LOG_MESSAGE
    PIO_ERROR_LOG_MESSAGE = POINTER(_IO_ERROR_LOG_MESSAGE)

    # Define the maximum message size that will be sent over the LPC to the
    # application reading the error log entries.
    # Regardless of LPC size restrictions, ERROR_LOG_MAXIMUM_SIZE must remain
    # a value that can fit in a UCHAR.
    ERROR_LOG_LIMIT_SIZE = 256 - 16

    # This limit, exclusive of IO_ERROR_LOG_MESSAGE_HEADER_LENGTH, also applies
    # to IO_ERROR_LOG_MESSAGE_LENGTH
    IO_ERROR_LOG_MESSAGE_HEADER_LENGTH = (
        ctypes.sizeof(IO_ERROR_LOG_MESSAGE) -                                                    ctypes.sizeof(IO_ERROR_LOG_PACKET) +                                                     (ctypes.sizeof(WCHAR) * 40)
    )
    ERROR_LOG_MESSAGE_LIMIT_SIZE = (
        ERROR_LOG_LIMIT_SIZE + IO_ERROR_LOG_MESSAGE_HEADER_LENGTH
    )

    # IO_ERROR_LOG_MESSAGE_LENGTH is
    # min(PORT_MAXIMUM_MESSAGE_LENGTH, ERROR_LOG_MESSAGE_LIMIT_SIZE)
    IO_ERROR_LOG_MESSAGE_LENGTH = (
        (PORT_MAXIMUM_MESSAGE_LENGTH > ERROR_LOG_MESSAGE_LIMIT_SIZE) ?                       ERROR_LOG_MESSAGE_LIMIT_SIZE :                                                    PORT_MAXIMUM_MESSAGE_LENGTH
    )

    # Define the maximum packet size a driver can allocate.
    ERROR_LOG_MAXIMUM_SIZE = (
        IO_ERROR_LOG_MESSAGE_LENGTH -                                                     IO_ERROR_LOG_MESSAGE_HEADER_LENGTH
    )

    if defined(_WIN64):
        PORT_MAXIMUM_MESSAGE_LENGTH = 512
    else:
        PORT_MAXIMUM_MESSAGE_LENGTH = 256
    # END IF
    # begin_access
    # Registry Specific Access Rights.
    KEY_QUERY_VALUE = 0x0001
    KEY_SET_VALUE = 0x0002
    KEY_CREATE_SUB_KEY = 0x0004
    KEY_ENUMERATE_SUB_KEYS = 0x0008
    KEY_NOTIFY = 0x0010
    KEY_CREATE_LINK = 0x0020
    KEY_WOW64_32KEY = 0x0200
    KEY_WOW64_64KEY = 0x0100
    KEY_WOW64_RES = 0x0300
    KEY_READ = (
        (STANDARD_RIGHTS_READ |
        KEY_QUERY_VALUE |
        KEY_ENUMERATE_SUB_KEYS |
        KEY_NOTIFY)                                                       &                                                                (~SYNCHRONIZE)
    )
    KEY_WRITE = (
        (STANDARD_RIGHTS_WRITE |
        KEY_SET_VALUE |
        KEY_CREATE_SUB_KEY)                                               &                                                                (~SYNCHRONIZE)
    )
    KEY_EXECUTE = (
        (KEY_READ)                                                         &                                                                (~SYNCHRONIZE)
    )
    KEY_ALL_ACCESS = (
        (STANDARD_RIGHTS_ALL |
        KEY_QUERY_VALUE |
        KEY_SET_VALUE |
        KEY_CREATE_SUB_KEY |
        KEY_ENUMERATE_SUB_KEYS |
        KEY_NOTIFY |
        KEY_CREATE_LINK)                                                  &                                                                (~SYNCHRONIZE)
    )

    # end_access
    # Open/Create Options
    REG_OPTION_RESERVED = 0x00000000
    REG_OPTION_NON_VOLATILE = 0x00000000

    # when system is rebooted
    REG_OPTION_VOLATILE = 0x00000001

    # when system is rebooted
    REG_OPTION_CREATE_LINK = 0x00000002

    # symbolic link
    REG_OPTION_BACKUP_RESTORE = 0x00000004

    # special access rules
    # privilege required
    REG_OPTION_OPEN_LINK = 0x00000008
    REG_OPTION_DONT_VIRTUALIZE = 0x00000010

    # virtualization for this
    # open and the resulting
    # handle.
    REG_LEGAL_OPTION = (
        REG_OPTION_RESERVED |
        REG_OPTION_NON_VOLATILE |
        REG_OPTION_VOLATILE |
        REG_OPTION_CREATE_LINK |
        REG_OPTION_BACKUP_RESTORE |
        REG_OPTION_OPEN_LINK |
        REG_OPTION_DONT_VIRTUALIZE
    )
    REG_OPEN_LEGAL_OPTION = (
        REG_OPTION_RESERVED |
        REG_OPTION_BACKUP_RESTORE |
        REG_OPTION_OPEN_LINK |
        REG_OPTION_DONT_VIRTUALIZE
    )

    # Key creation/open disposition
    REG_CREATED_NEW_KEY = 0x00000001
    REG_OPENED_EXISTING_KEY = 0x00000002

    # hive format to be used by Reg(Nt)SaveKeyEx
    REG_STANDARD_FORMAT = 1
    REG_LATEST_FORMAT = 2
    REG_NO_COMPRESSION = 4

    # Key restore & hive load flags
    REG_WHOLE_HIVE_VOLATILE = 0x00000001
    REG_REFRESH_HIVE = 0x00000002
    REG_NO_LAZY_FLUSH = 0x00000004
    REG_FORCE_RESTORE = 0x00000008
    REG_APP_HIVE = 0x00000010
    REG_PROCESS_PRIVATE = 0x00000020
    REG_START_JOURNAL = 0x00000040
    REG_HIVE_EXACT_FILE_GROWTH = 0x00000080
    REG_HIVE_NO_RM = 0x00000100
    REG_HIVE_SINGLE_LOG = 0x00000200
    REG_BOOT_HIVE = 0x00000400
    REG_LOAD_HIVE_OPEN_HANDLE = 0x00000800
    REG_FLUSH_HIVE_FILE_GROWTH = 0x00001000
    REG_OPEN_READ_ONLY = 0x00002000
    REG_IMMUTABLE = 0x00004000
    REG_APP_HIVE_OPEN_READ_ONLY = REG_OPEN_READ_ONLY

    # Unload Flags
    REG_FORCE_UNLOAD = 1
    REG_UNLOAD_LEGAL_FLAGS = REG_FORCE_UNLOAD

    # Notify filter values
    REG_NOTIFY_CHANGE_NAME = 0x00000001
    REG_NOTIFY_CHANGE_ATTRIBUTES = 0x00000002
    REG_NOTIFY_CHANGE_LAST_SET = 0x00000004
    REG_NOTIFY_CHANGE_SECURITY = 0x00000008
    REG_NOTIFY_THREAD_AGNOSTIC = 0x10000000

    # for async user event based notification
    REG_LEGAL_CHANGE_FILTER = (
        REG_NOTIFY_CHANGE_NAME |
        REG_NOTIFY_CHANGE_ATTRIBUTES |
        REG_NOTIFY_CHANGE_LAST_SET |
        REG_NOTIFY_CHANGE_SECURITY |
        REG_NOTIFY_THREAD_AGNOSTIC
    )

    # Key query structures
    class _KEY_BASIC_INFORMATION(ctypes.Structure):
        pass


    _KEY_BASIC_INFORMATION._fields_ = [
        ('LastWriteTime', LARGE_INTEGER),
        ('TitleIndex', ULONG),
        ('NameLength', ULONG),
        ('Name', WCHAR * 1), # Variable length string
    ]
    KEY_BASIC_INFORMATION = _KEY_BASIC_INFORMATION
    PKEY_BASIC_INFORMATION = POINTER(_KEY_BASIC_INFORMATION)
    class _KEY_NODE_INFORMATION(ctypes.Structure):
        pass


    _KEY_NODE_INFORMATION._fields_ = [
        ('LastWriteTime', LARGE_INTEGER),
        ('TitleIndex', ULONG),
        ('ClassOffset', ULONG),
        ('ClassLength', ULONG),
        ('NameLength', ULONG),
        ('Name', WCHAR * 1), # Variable length string
    ]
    KEY_NODE_INFORMATION = _KEY_NODE_INFORMATION
    PKEY_NODE_INFORMATION = POINTER(_KEY_NODE_INFORMATION)
    class _KEY_FULL_INFORMATION(ctypes.Structure):
        pass


    _KEY_FULL_INFORMATION._fields_ = [
        ('LastWriteTime', LARGE_INTEGER),
        ('TitleIndex', ULONG),
        ('ClassOffset', ULONG),
        ('ClassLength', ULONG),
        ('SubKeys', ULONG),
        ('MaxNameLen', ULONG),
        ('MaxClassLen', ULONG),
        ('Values', ULONG),
        ('MaxValueNameLen', ULONG),
        ('MaxValueDataLen', ULONG),
        ('Class', WCHAR * 1), # Variable length
    ]
    KEY_FULL_INFORMATION = _KEY_FULL_INFORMATION
    PKEY_FULL_INFORMATION = POINTER(_KEY_FULL_INFORMATION)


    class _KEY_INFORMATION_CLASS(ENUM):
        KeyBasicInformation = 1
        KeyNodeInformation = 2
        KeyFullInformation = 3
        KeyNameInformation = 4
        KeyCachedInformation = 5
        KeyFlagsInformation = 6
        KeyVirtualizationInformation = 7
        KeyHandleTagsInformation = 8
        KeyTrustInformation = 9
        KeyLayerInformation = 10
        MaxKeyInfoClass = 11


    KEY_INFORMATION_CLASS = _KEY_INFORMATION_CLASS
    class _KEY_WRITE_TIME_INFORMATION(ctypes.Structure):
        pass


    _KEY_WRITE_TIME_INFORMATION._fields_ = [
        ('LastWriteTime', LARGE_INTEGER),
    ]
    KEY_WRITE_TIME_INFORMATION = _KEY_WRITE_TIME_INFORMATION
    PKEY_WRITE_TIME_INFORMATION = POINTER(_KEY_WRITE_TIME_INFORMATION)
    class _KEY_WOW64_FLAGS_INFORMATION(ctypes.Structure):
        pass


    _KEY_WOW64_FLAGS_INFORMATION._fields_ = [
        ('UserFlags', ULONG),
    ]
    KEY_WOW64_FLAGS_INFORMATION = _KEY_WOW64_FLAGS_INFORMATION
    PKEY_WOW64_FLAGS_INFORMATION = POINTER(_KEY_WOW64_FLAGS_INFORMATION)
    class _KEY_CONTROL_FLAGS_INFORMATION(ctypes.Structure):
        pass


    _KEY_CONTROL_FLAGS_INFORMATION._fields_ = [
        ('ControlFlags', ULONG),
    ]
    KEY_CONTROL_FLAGS_INFORMATION = _KEY_CONTROL_FLAGS_INFORMATION
    PKEY_CONTROL_FLAGS_INFORMATION = POINTER(_KEY_CONTROL_FLAGS_INFORMATION)
    class _KEY_SET_VIRTUALIZATION_INFORMATION(ctypes.Structure):
        pass


    _KEY_SET_VIRTUALIZATION_INFORMATION._fields_ = [
        ('VirtualTarget', ULONG, 1), # Tells if the key is a virtual target key.
        ('VirtualStore', ULONG, 1), # Tells if the key is a virtual store key.
        ('VirtualSource', ULONG, 1), # Tells if the key has been virtualized at least one (virtual hint)
        ('Reserved', ULONG, 29),
    ]
    KEY_SET_VIRTUALIZATION_INFORMATION = _KEY_SET_VIRTUALIZATION_INFORMATION
    PKEY_SET_VIRTUALIZATION_INFORMATION = POINTER(_KEY_SET_VIRTUALIZATION_INFORMATION)
    class _KEY_SET_INFORMATION_CLASS(ENUM):
        KeyWriteTimeInformation = 1
        KeyWow64FlagsInformation = 2
        KeyControlFlagsInformation = 3
        KeySetVirtualizationInformation = 4
        KeySetDebugInformation = 5
        KeySetHandleTagsInformation = 6
        KeySetLayerInformation = 7
        MaxKeySetInfoClass = 8


    KEY_SET_INFORMATION_CLASS = _KEY_SET_INFORMATION_CLASS

    # Value entry query structures
    class _KEY_VALUE_BASIC_INFORMATION(ctypes.Structure):
        pass


    _KEY_VALUE_BASIC_INFORMATION._fields_ = [
        ('TitleIndex', ULONG),
        ('Type', ULONG),
        ('NameLength', ULONG),
        ('Name', WCHAR * 1), # Variable size
    ]
    KEY_VALUE_BASIC_INFORMATION = _KEY_VALUE_BASIC_INFORMATION
    PKEY_VALUE_BASIC_INFORMATION = POINTER(_KEY_VALUE_BASIC_INFORMATION)
    class _KEY_VALUE_FULL_INFORMATION(ctypes.Structure):
        pass


    _KEY_VALUE_FULL_INFORMATION._fields_ = [
        ('TitleIndex', ULONG),
        ('Type', ULONG),
        ('DataOffset', ULONG),
        ('DataLength', ULONG),
        ('NameLength', ULONG),
        ('Name', WCHAR * 1), # Variable size
    ]
    KEY_VALUE_FULL_INFORMATION = _KEY_VALUE_FULL_INFORMATION
    PKEY_VALUE_FULL_INFORMATION = POINTER(_KEY_VALUE_FULL_INFORMATION)
    class _KEY_VALUE_PARTIAL_INFORMATION(ctypes.Structure):
        pass


    _KEY_VALUE_PARTIAL_INFORMATION._fields_ = [
        ('TitleIndex', ULONG),
        ('Type', ULONG),
        ('DataLength', ULONG),
        ('Data', UCHAR * 1), # Variable size
    ]
    KEY_VALUE_PARTIAL_INFORMATION = _KEY_VALUE_PARTIAL_INFORMATION
    PKEY_VALUE_PARTIAL_INFORMATION = POINTER(_KEY_VALUE_PARTIAL_INFORMATION)
    class _KEY_VALUE_PARTIAL_INFORMATION_ALIGN64(ctypes.Structure):
        pass


    _KEY_VALUE_PARTIAL_INFORMATION_ALIGN64._fields_ = [
        ('Type', ULONG),
        ('DataLength', ULONG),
        ('Data', UCHAR * 1), # Variable size
    ]
    KEY_VALUE_PARTIAL_INFORMATION_ALIGN64 = _KEY_VALUE_PARTIAL_INFORMATION_ALIGN64
    PKEY_VALUE_PARTIAL_INFORMATION_ALIGN64 = POINTER(_KEY_VALUE_PARTIAL_INFORMATION_ALIGN64)
    class _KEY_VALUE_LAYER_INFORMATION(ctypes.Structure):
        pass


    _KEY_VALUE_LAYER_INFORMATION._fields_ = [
        ('IsTombstone', ULONG, 1),
        ('Reserved', ULONG, 31),
    ]
    KEY_VALUE_LAYER_INFORMATION = _KEY_VALUE_LAYER_INFORMATION
    PKEY_VALUE_LAYER_INFORMATION = POINTER(_KEY_VALUE_LAYER_INFORMATION)
    class _KEY_VALUE_ENTRY(ctypes.Structure):
        pass


    _KEY_VALUE_ENTRY._fields_ = [
        ('ValueName', PUNICODE_STRING),
        ('DataLength', ULONG),
        ('DataOffset', ULONG),
        ('Type', ULONG),
    ]
    KEY_VALUE_ENTRY = _KEY_VALUE_ENTRY
    PKEY_VALUE_ENTRY = POINTER(_KEY_VALUE_ENTRY)
    class _KEY_VALUE_INFORMATION_CLASS(ENUM):
        KeyValueBasicInformation = 1
        KeyValueFullInformation = 2
        KeyValuePartialInformation = 3
        KeyValueFullInformationAlign64 = 4
        KeyValuePartialInformationAlign64 = 5
        KeyValueLayerInformation = 6
        MaxKeyValueInfoClass = 7


    KEY_VALUE_INFORMATION_CLASS = _KEY_VALUE_INFORMATION_CLASS
    class _KEY_TRUST_INFORMATION(ctypes.Structure):
        pass


    _KEY_TRUST_INFORMATION._fields_ = [
        ('TrustedKey', ULONG, 1), # Tells if key is opened from a trusted hive.
        ('Reserved', ULONG, 31),
    ]
    KEY_TRUST_INFORMATION = _KEY_TRUST_INFORMATION
    PKEY_TRUST_INFORMATION = POINTER(_KEY_TRUST_INFORMATION)
    OBJ_NAME_PATH_SEPARATOR = (WCHAR)L'\\'

    # Object Manager Object Type Specific Access Rights.
    OBJECT_TYPE_CREATE = 0x0001
    OBJECT_TYPE_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | 0x1

    # Object Manager Directory Specific Access Rights.
    DIRECTORY_QUERY = 0x0001
    DIRECTORY_TRAVERSE = 0x0002
    DIRECTORY_CREATE_OBJECT = 0x0004
    DIRECTORY_CREATE_SUBDIRECTORY = 0x0008
    DIRECTORY_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | 0xF

    # begin_winnt
    # begin_access
    # Object Manager Symbolic Link Specific Access Rights.
    # end_winnt
    SYMBOLIC_LINK_QUERY = 0x0001
    SYMBOLIC_LINK_SET = 0x0002
    SYMBOLIC_LINK_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | 0x1
    SYMBOLIC_LINK_ALL_ACCESS_EX = STANDARD_RIGHTS_REQUIRED | 0xFFFF

    # end_access
    class _OBJECT_NAME_INFORMATION(ctypes.Structure):
        pass


    _OBJECT_NAME_INFORMATION._fields_ = [
        ('Name', UNICODE_STRING),
    ]
    OBJECT_NAME_INFORMATION = _OBJECT_NAME_INFORMATION
    POBJECT_NAME_INFORMATION = POINTER(_OBJECT_NAME_INFORMATION)

    # begin_access
    DUPLICATE_CLOSE_SOURCE = 0x00000001
    DUPLICATE_SAME_ACCESS = 0x00000002
    DUPLICATE_SAME_ATTRIBUTES = 0x00000004

    # Section Information Structures.


    class _SECTION_INHERIT(ENUM):
        ViewShare = 1
        ViewUnmap = 2


    SECTION_INHERIT = _SECTION_INHERIT

    # begin_access
    # Section Access Rights.
    SECTION_QUERY = 0x0001
    SECTION_MAP_WRITE = 0x0002
    SECTION_MAP_READ = 0x0004
    SECTION_MAP_EXECUTE = 0x0008
    SECTION_EXTEND_SIZE = 0x0010
    SECTION_MAP_EXECUTE_EXPLICIT = 0x0020
    SECTION_ALL_ACCESS = (
        STANDARD_RIGHTS_REQUIRED |
        SECTION_QUERY |
        SECTION_MAP_WRITE |
        SECTION_MAP_READ |
        SECTION_MAP_EXECUTE |
        SECTION_EXTEND_SIZE
    )

    # Session Specific Access Rights.
    SESSION_QUERY_ACCESS = 0x0001
    SESSION_MODIFY_ACCESS = 0x0002
    SESSION_ALL_ACCESS = (
        STANDARD_RIGHTS_REQUIRED |
        SESSION_QUERY_ACCESS |
        SESSION_MODIFY_ACCESS
    )

    # end_access
    SEGMENT_ALL_ACCESS = SECTION_ALL_ACCESS
    PAGE_NOACCESS = 0x01
    PAGE_READONLY = 0x02
    PAGE_READWRITE = 0x04
    PAGE_WRITECOPY = 0x08
    PAGE_EXECUTE = 0x10
    PAGE_EXECUTE_READ = 0x20
    PAGE_EXECUTE_READWRITE = 0x40
    PAGE_EXECUTE_WRITECOPY = 0x80
    PAGE_GUARD = 0x100
    PAGE_NOCACHE = 0x200
    PAGE_WRITECOMBINE = 0x400

    # PAGE_REVERT_TO_FILE_MAP can be combined with other protection
    # values to specify to VirtualProtect that the argument range
    # should be reverted to point back to the backing file. This
    # means the contents of any private (copy on write) pages in the
    # range will be discarded. Any reverted pages that were locked
    # into the working set are unlocked as well.
    PAGE_ENCLAVE_THREAD_CONTROL = 0x80000000
    PAGE_REVERT_TO_FILE_MAP = 0x80000000
    PAGE_TARGETS_NO_UPDATE = 0x40000000
    PAGE_TARGETS_INVALID = 0x40000000
    PAGE_ENCLAVE_UNVALIDATED = 0x20000000
    PAGE_ENCLAVE_NO_CHANGE = 0x20000000
    PAGE_ENCLAVE_DECOMMIT = 0x10000000
    MEM_COMMIT = 0x00001000
    MEM_RESERVE = 0x00002000
    MEM_RESET = 0x00080000
    MEM_TOP_DOWN = 0x00100000
    MEM_RESET_UNDO = 0x01000000
    MEM_LARGE_PAGES = 0x20000000
    MEM_4MB_PAGES = 0x80000000
    MEM_64K_PAGES = MEM_LARGE_PAGES | MEM_PHYSICAL
    MEM_DECOMMIT = 0x00004000
    MEM_RELEASE = 0x00008000
    MEM_FREE = 0x00010000
    SEC_64K_PAGES = 0x00080000
    SEC_FILE = 0x00800000
    SEC_RESERVE = 0x04000000
    SEC_COMMIT = 0x08000000
    SEC_LARGE_PAGES = 0x80000000
    MEM_PRIVATE = 0x00020000
    MEM_MAPPED = 0x00040000
    PROCESS_DUP_HANDLE = 0x0040

    if NTDDI_VERSION >= NTDDI_VISTA:
        PROCESS_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xFFFF
    else:
        PROCESS_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xFFF
    # END IF
    # Thread Specific Access Rights
    THREAD_TERMINATE = 0x0001
    THREAD_SUSPEND_RESUME = 0x0002
    THREAD_ALERT = 0x0004
    THREAD_GET_CONTEXT = 0x0008
    THREAD_SET_CONTEXT = 0x0010
    THREAD_SET_INFORMATION = 0x0020
    THREAD_SET_LIMITED_INFORMATION = 0x0400
    THREAD_QUERY_LIMITED_INFORMATION = 0x0800
    THREAD_RESUME = 0x1000

    if NTDDI_VERSION >= NTDDI_VISTA:
        THREAD_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xFFFF
    else:
        THREAD_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0x3FF
    # END IF
    # ClientId
    class _CLIENT_ID(ctypes.Structure):
        pass


    _CLIENT_ID._fields_ = [
        ('UniqueProcess', HANDLE),
        ('UniqueThread', HANDLE),
    ]
    CLIENT_ID = _CLIENT_ID
    PCLIENT_ID = POINTER(CLIENT_ID)


    def NtCurrentProcess():
        return (HANDLELONG_PTR - 1)


    def ZwCurrentProcess():
        return NtCurrentProcess


    def NtCurrentThread():
        return (HANDLELONG_PTR - 2)


    def ZwCurrentThread():
        return NtCurrentThread


    def NtCurrentSession():
        return (HANDLELONG_PTR - 3)


    def ZwCurrentSession():
        return NtCurrentSession

    # == == == == == == == == == == == == == == == == == == == == =
    # Define GUIDs which represent well - known power schemes
    # == == == == == == == == == == == == == == == == == == == == =
    # Maximum Power Savings - indicates that very aggressive power savings
    # measures will be used to help
    # stretch battery life.
    # {a1841308 - 3541 - 4fab - bc81 - f71556f20b4a}
    GUID_MAX_POWER_SAVINGS = DEFINE_GUID(
        0xA1841308,
        0x3541,
        0x4FAB,
        0xBC,
        0x81,
        0xF7,
        0x15,
        0x56,
        0xF2,
        0x0B,
        0x4A
    )

    # No Power Savings - indicates that almost no power savings measures will
    # be used.
    # {8c5e7fda - e8bf - 4a96 - 9a85 - a6e23a8c635c}
    GUID_MIN_POWER_SAVINGS = DEFINE_GUID(
        0x8C5E7FDA,
        0xE8BF,
        0x4A96,
        0x9A,
        0x85,
        0xA6,
        0xE2,
        0x3A,
        0x8C,
        0x63,
        0x5C
    )

    # Typical Power Savings - indicates that fairly aggressive power savings
    # measures will be used.
    # {381b4222 - f694 - 41f0 - 9685 - ff5bb260df2e}
    GUID_TYPICAL_POWER_SAVINGS = DEFINE_GUID(
        0x381B4222,
        0xF694,
        0x41F0,
        0x96,
        0x85,
        0xFF,
        0x5B,
        0xB2,
        0x60,
        0xDF,
        0x2E
    )

    # This is a special GUID that represents "no subgroup" of settings. That
    # is, it indicates
    # that settings that are in the root of the power policy hierarchy as
    # opposed to settings
    # that are buried under a subgroup of settings. This should be used when
    # querying for
    # power settings that may not fall into a subgroup.
    NO_SUBGROUP_GUID = DEFINE_GUID(
        0xFEA3413E,
        0x7E05,
        0x4911,
        0x9A,
        0x71,
        0x70,
        0x03,
        0x31,
        0xF1,
        0xC2,
        0x94
    )

    # This is a special GUID that represents "every power scheme". That is, it
    # indicates
    # that any write to this power scheme should be reflected to every scheme
    # present.
    # This allows users to write a single setting once and have it apply to
    # all schemes. They
    # can then apply custom settings to specific power schemes that they care
    # about.
    ALL_POWERSCHEMES_GUID = DEFINE_GUID(
        0x68A1E95E,
        0x13EA,
        0x41E1,
        0x80,
        0x11,
        0x0C,
        0x49,
        0x6C,
        0xA4,
        0x90,
        0xB0
    )

    # This is a special GUID that represents a 'personality' that each power
    # scheme will have.
    # In other words, each power scheme will have this key indicating
    # "I'm most like *this* base
    # power scheme." This individual setting will have one of three settings:
    # GUID_MAX_POWER_SAVINGS
    # GUID_MIN_POWER_SAVINGS
    # GUID_TYPICAL_POWER_SAVINGS
    # This allows several features:
    # 1. Drivers and applications can register for notification of this GUID.
    # So when this power
    # scheme is activiated, this GUID's setting will be sent across the system
    # and drivers/applications
    # can see "GUID_MAX_POWER_SAVINGS" which will tell them in a generic
    # fashion "get real aggressive
    # about conserving power".
    # 2. UserB may install a driver or application which creates power
    # settings, and UserB may modify
    # those power settings. Now UserA logs in. How does he see those settings?
    # They simply don't
    # exist in his private power key. Well they do exist over in the system
    # power key. When we
    # enumerate all the power settings in this system power key and don't find
    # a corresponding entry
    # in the user's private power key, then we can go look at this
    # "personality" key in the users
    # power scheme. We can then go get a default value for the power setting,
    # depending on which
    # "personality" power scheme is being operated on. Here's an example:
    # A. UserB installs an application that creates a power setting Seetting1
    # B. UserB changes Setting1 to have a value of 50 because that's one of
    # the possible settings
    # available for setting1.
    # C. UserB logs out
    # D. UserA logs in and his active power scheme is some custom scheme that
    # was derived from
    # the GUID_TYPICAL_POWER_SAVINGS. But remember that UserA has no setting1
    # in his
    # private power key.
    # E. When activating UserA's selected power scheme, all power settings in
    # the system power key will
    # be enumerated (including Setting1).
    # F. The power manager will see that UserA has no Setting1 power setting
    # in his private power scheme.
    # G. The power manager will query UserA's power scheme for its personality
    # and retrieve
    # GUID_TYPICAL_POWER_SAVINGS.
    # H. The power manager then looks in Setting1 in the system power key and
    # looks in its set of default
    # values for the corresponding value for GUID_TYPICAL_POWER_SAVINGS power
    # schemes.
    # I. This derived power setting is applied.
    GUID_POWERSCHEME_PERSONALITY = DEFINE_GUID(
        0x245D8541,
        0x3943,
        0x4422,
        0xB0,
        0x25,
        0x13,
        0xA7,
        0x84,
        0xF6,
        0x79,
        0xB7
    )

    # Define a special GUID which will be used to define the active power
    # scheme.
    # User will register for this power setting GUID, and when the active power
    # scheme changes, they'll get a callback where the payload is the GUID
    # representing the active powerscheme.
    # ( 31F9F286 - 5084 - 42FE - B720 - 2B0264993763 }
    GUID_ACTIVE_POWERSCHEME = DEFINE_GUID(
        0x31F9F286,
        0x5084,
        0x42FE,
        0xB7,
        0x20,
        0x2B,
        0x02,
        0x64,
        0x99,
        0x37,
        0x63
    )

    # == == == == == == == == == == == == == == == == == == == == =
    # Define GUIDs which represent well - known power settings
    # == == == == == == == == == == == == == == == == == == == == =
    # Idle resiliency settings
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Specifies the subgroup which will contain all of the idle resiliency
    # settings for a single policy.
    # {2E601130 - 5351 - 4d9d - 8E04 - 252966BAD054}
    GUID_IDLE_RESILIENCY_SUBGROUP = DEFINE_GUID(
        0x2E601130,
        0x5351,
        0x4D9D,
        0x8E,
        0x4,
        0x25,
        0x29,
        0x66,
        0xBA,
        0xD0,
        0x54
    )

    # Specifies the maximum clock interrupt period (in ms)
    # N.B. This power setting is DEPRECATED.
    # {C42B79AA - AA3A - 484b - A98F - 2CF32AA90A28}
    GUID_IDLE_RESILIENCY_PERIOD = DEFINE_GUID(
        0xC42B79AA,
        0xAA3A,
        0x484B,
        0xA9,
        0x8F,
        0x2C,
        0xF3,
        0x2A,
        0xA9,
        0xA,
        0x28
    )

    # Specifies the deep sleep policy setting.
    # This is intended to override the GUID_IDLE_RESILIENCY_PERIOD
    # {d502f7ee - 1dc7 - 4efd - a55d - f04b6f5c0545}
    GUID_DEEP_SLEEP_ENABLED = DEFINE_GUID(
        0xD502F7EE,
        0x1DC7,
        0x4EFD,
        0xA5,
        0x5D,
        0xF0,
        0x4B,
        0x6F,
        0x5C,
        0x5,
        0x45
    )

    # Specifies the platform idle state index associated with idle resiliency
    # period.
    # N.B. This power setting is DEPRECATED.
    # {D23F2FB8 - 9536 - 4038 - 9C94 - 1CE02E5C2152}
    GUID_DEEP_SLEEP_PLATFORM_STATE = DEFINE_GUID(
        0xD23F2FB8,
        0x9536,
        0x4038,
        0x9C,
        0x94,
        0x1C,
        0xE0,
        0x2E,
        0x5C,
        0x21,
        0x52
    )

    # Specifies (in milliseconds) how LONG we wait after the last disk access
    # before we power off the disk in case when IO coalescing is active.
    # {C36F0EB4 - 2988 - 4a70 - 8EEE - 0884FC2C2433}
    GUID_DISK_COALESCING_POWERDOWN_TIMEOUT = DEFINE_GUID(
        0xC36F0EB4,
        0x2988,
        0x4A70,
        0x8E,
        0xEE,
        0x8,
        0x84,
        0xFC,
        0x2C,
        0x24,
        0x33
    )

    # Specifies (in seconds) how LONG we wait after the CS Enter before
    # we deactivate execution required request.
    # 0 : implies execution power requests are disabled and have no effect
    # - 1 : implies execution power requests are never deactivated
    # Note: Execution required power requests are mapped into system required
    # power requests on non - AoAc machines and this value has no effect.
    # {3166BC41 - 7E98 - 4e03 - B34E - EC0F5F2B218E}
    GUID_EXECUTION_REQUIRED_REQUEST_TIMEOUT = DEFINE_GUID(
        0x3166BC41,
        0x7E98,
        0x4E03,
        0xB3,
        0x4E,
        0xEC,
        0xF,
        0x5F,
        0x2B,
        0x21,
        0x8E
    )

    # Video settings
    # - - - - - - - - - - - - - -
    # Specifies the subgroup which will contain all of the video
    # settings for a single policy.
    # {7516b95f - f776 - 4464 - 8c53 - 06167f40cc99}
    GUID_VIDEO_SUBGROUP = DEFINE_GUID(
        0x7516B95F,
        0xF776,
        0x4464,
        0x8C,
        0x53,
        0x06,
        0x16,
        0x7F,
        0x40,
        0xCC,
        0x99
    )

    # Specifies (in seconds) how LONG we wait after the last user input has
    # been
    # received before we power off the video.
    # {3c0bc021 - c8a8 - 4e07 - a973 - 6b14cbcb2b7e}
    GUID_VIDEO_POWERDOWN_TIMEOUT = DEFINE_GUID(
        0x3C0BC021,
        0xC8A8,
        0x4E07,
        0xA9,
        0x73,
        0x6B,
        0x14,
        0xCB,
        0xCB,
        0x2B,
        0x7E
    )

    # Specifies whether adaptive display dimming is turned on or off.
    # N.B. This setting is DEPRECATED in Windows 8.1
    # {82DBCF2D - CD67 - 40C5 - BFDC - 9F1A5CCD4663}
    GUID_VIDEO_ANNOYANCE_TIMEOUT = DEFINE_GUID(
        0x82DBCF2D,
        0xCD67,
        0x40C5,
        0xBF,
        0xDC,
        0x9F,
        0x1A,
        0x5C,
        0xCD,
        0x46,
        0x63
    )

    # Specifies how much adaptive dim time out will be increased by.
    # N.B. This setting is DEPRECATED in Windows 8.1
    # {EED904DF - B142 - 4183 - B10B - 5A1197A37864}
    GUID_VIDEO_ADAPTIVE_PERCENT_INCREASE = DEFINE_GUID(
        0xEED904DF,
        0xB142,
        0x4183,
        0xB1,
        0x0B,
        0x5A,
        0x11,
        0x97,
        0xA3,
        0x78,
        0x64
    )

    # Specifies (in seconds) how LONG we wait after the last user input has
    # been
    # received before we dim the video.
    # {17aaa29b - 8b43 - 4b94 - aafe - 35f64daaf1ee}
    GUID_VIDEO_DIM_TIMEOUT = DEFINE_GUID(
        0x17AAA29B,
        0x8B43,
        0x4B94,
        0xAA,
        0xFE,
        0x35,
        0xF6,
        0x4D,
        0xAA,
        0xF1,
        0xEE
    )

    # Specifies if the operating system should use adaptive timers (based on
    # previous behavior) to power down the video.
    # {90959d22 - d6a1 - 49b9 - af93 - bce885ad335b}
    GUID_VIDEO_ADAPTIVE_POWERDOWN = DEFINE_GUID(
        0x90959D22,
        0xD6A1,
        0x49B9,
        0xAF,
        0x93,
        0xBC,
        0xE8,
        0x85,
        0xAD,
        0x33,
        0x5B
    )

    # Specifies if the monitor is currently being powered or not.
    # {02731015 - 4510 - 4526 - 99E6 - E5A17EBD1AEA}
    GUID_MONITOR_POWER_ON = DEFINE_GUID(
        0x02731015,
        0x4510,
        0x4526,
        0x99,
        0xE6,
        0xE5,
        0xA1,
        0x7E,
        0xBD,
        0x1A,
        0xEA
    )

    # Monitor brightness policy when in normal state.
    # {aded5e82 - b909 - 4619 - 9949 - f5d71dac0bcb}
    GUID_DEVICE_POWER_POLICY_VIDEO_BRIGHTNESS = DEFINE_GUID(
        0xADED5E82,
        0xB909,
        0x4619,
        0x99,
        0x49,
        0xF5,
        0xD7,
        0x1D,
        0xAC,
        0x0B,
        0xCB
    )

    # Monitor brightness policy when in dim state.
    # {f1fbfde2 - a960 - 4165 - 9f88 - 50667911ce96}
    GUID_DEVICE_POWER_POLICY_VIDEO_DIM_BRIGHTNESS = DEFINE_GUID(
        0xF1FBFDE2,
        0xA960,
        0x4165,
        0x9F,
        0x88,
        0x50,
        0x66,
        0x79,
        0x11,
        0xCE,
        0x96
    )

    # Current monitor brightness.
    # {8ffee2c6 - 2d01 - 46be - adb9 - 398addc5b4ff}
    GUID_VIDEO_CURRENT_MONITOR_BRIGHTNESS = DEFINE_GUID(
        0x8FFEE2C6,
        0x2D01,
        0x46BE,
        0xAD,
        0xB9,
        0x39,
        0x8A,
        0xDD,
        0xC5,
        0xB4,
        0xFF
    )

    # Specifies if the operating system should use ambient light sensor to
    # change
    # adaptively the display's brightness.
    # {FBD9AA66 - 9553 - 4097 - BA44 - ED6E9D65EAB8}
    GUID_VIDEO_ADAPTIVE_DISPLAY_BRIGHTNESS = DEFINE_GUID(
        0xFBD9AA66,
        0x9553,
        0x4097,
        0xBA,
        0x44,
        0xED,
        0x6E,
        0x9D,
        0x65,
        0xEA,
        0xB8
    )

    # Specifies a change in the current monitor's display state.
    # {6fe69556 - 704a - 47a0 - 8f24 - c28d936fda47}
    GUID_CONSOLE_DISPLAY_STATE = DEFINE_GUID(
        0x6FE69556,
        0x704A,
        0x47A0,
        0x8F,
        0x24,
        0xC2,
        0x8D,
        0x93,
        0x6F,
        0xDA,
        0x47
    )

    # Defines a guid for enabling/disabling the ability to create display
    # required
    # power requests.
    # {A9CEB8DA - CD46 - 44FB - A98B - 02AF69DE4623}
    GUID_ALLOW_DISPLAY_REQUIRED = DEFINE_GUID(
        0xA9CEB8DA,
        0xCD46,
        0x44FB,
        0xA9,
        0x8B,
        0x02,
        0xAF,
        0x69,
        0xDE,
        0x46,
        0x23
    )

    # Specifies the video power down timeout (in seconds) after the interactive
    # console is locked (and sensors indicate UserNotPresent). Value 0
    # effectively disables this feature.
    # {8EC4B3A5 - 6868 - 48c2 - BE75 - 4F3044BE88A7}
    GUID_VIDEO_CONSOLE_LOCK_TIMEOUT = DEFINE_GUID(
        0x8EC4B3A5,
        0x6868,
        0x48C2,
        0xBE,
        0x75,
        0x4F,
        0x30,
        0x44,
        0xBE,
        0x88,
        0xA7
    )

    # Adaptive power behavior settings
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # {8619B916 - E004 - 4dd8 - 9B66 - DAE86F806698}
    GUID_ADAPTIVE_POWER_BEHAVIOR_SUBGROUP = DEFINE_GUID(
        0x8619B916,
        0xE004,
        0x4DD8,
        0x9B,
        0x66,
        0xDA,
        0xE8,
        0x6F,
        0x80,
        0x66,
        0x98
    )

    # Specifies the input timeout (in seconds) to be used to indicate
    # UserUnkown.
    # Value 0 effectively disables this feature.
    # {5ADBBFBC - 074E - 4da1 - BA38 - DB8B36B2C8F3}
    GUID_NON_ADAPTIVE_INPUT_TIMEOUT = DEFINE_GUID(
        0x5ADBBFBC,
        0x74E,
        0x4DA1,
        0xBA,
        0x38,
        0xDB,
        0x8B,
        0x36,
        0xB2,
        0xC8,
        0xF3
    )

    # Specifies a change in the input controller(s) global system's state:
    # e.g. enabled, suppressed, filtered.
    # {0E98FAE9 - F45A - 4DE1 - A757 - 6031F197F6EA}
    GUID_ADAPTIVE_INPUT_CONTROLLER_STATE = DEFINE_GUID(
        0xE98FAE9,
        0xF45A,
        0x4DE1,
        0xA7,
        0x57,
        0x60,
        0x31,
        0xF1,
        0x97,
        0xF6,
        0xEA
    )

    # Harddisk settings
    # - - - - - - - - - - - - - - - - -
    # Specifies the subgroup which will contain all of the harddisk
    # settings for a single policy.
    GUID_DISK_SUBGROUP = DEFINE_GUID(
        0x0012EE47,
        0x9041,
        0x4B5D,
        0x9B,
        0x77,
        0x53,
        0x5F,
        0xBA,
        0x8B,
        0x14,
        0x42
    )

    # Specifies a maximum power consumption level.
    GUID_DISK_MAX_POWER = DEFINE_GUID(
        0x51DEA550,
        0xBB38,
        0x4BC4,
        0x99,
        0x1B,
        0xEA,
        0xCF,
        0x37,
        0xBE,
        0x5E,
        0xC8
    )

    # Specifies (in seconds) how LONG we wait after the last disk access
    # before we power off the disk.
    GUID_DISK_POWERDOWN_TIMEOUT = DEFINE_GUID(
        0x6738E2C4,
        0xE8A5,
        0x4A42,
        0xB1,
        0x6A,
        0xE0,
        0x40,
        0xE7,
        0x69,
        0x75,
        0x6E
    )

    # Specifies (in milliseconds) how LONG we wait after the last disk access
    # before we power off the disk taking into account if IO coalescing is
    # active.
    # {58E39BA8 - B8E6 - 4EF6 - 90D0 - 89AE32B258D6}
    GUID_DISK_IDLE_TIMEOUT = DEFINE_GUID(
        0x58E39BA8,
        0xB8E6,
        0x4EF6,
        0x90,
        0xD0,
        0x89,
        0xAE,
        0x32,
        0xB2,
        0x58,
        0xD6
    )

    # Specifies the amount of contiguous disk activity time to ignore when
    # calculating disk idleness.
    # 80e3c60e - bb94 - 4ad8 - bbe0 - 0d3195efc663
    GUID_DISK_BURST_IGNORE_THRESHOLD = DEFINE_GUID(
        0x80E3C60E,
        0xBB94,
        0x4AD8,
        0xBB,
        0xE0,
        0x0D,
        0x31,
        0x95,
        0xEF,
        0xC6,
        0x63
    )

    # Specifies if the operating system should use adaptive timers (based on
    # previous behavior) to power down the disk,
    GUID_DISK_ADAPTIVE_POWERDOWN = DEFINE_GUID(
        0x396A32E1,
        0x499A,
        0x40B2,
        0x91,
        0x24,
        0xA9,
        0x6A,
        0xFE,
        0x70,
        0x76,
        0x67
    )

    # System sleep settings
    # - - - - - - - - - - - - - - - - - - - - -
    # Specifies the subgroup which will contain all of the sleep
    # settings for a single policy.
    # { 238C9FA8 - 0AAD - 41ED - 83F4 - 97BE242C8F20 }
    GUID_SLEEP_SUBGROUP = DEFINE_GUID(
        0x238C9FA8,
        0x0AAD,
        0x41ED,
        0x83,
        0xF4,
        0x97,
        0xBE,
        0x24,
        0x2C,
        0x8F,
        0x20
    )

    # Specifies an idle treshold percentage (0 - 100). The system must be this
    # idle
    # over a period of time in order to idle to sleep.
    # N.B. DEPRECATED IN WINDOWS 6.1
    GUID_SLEEP_IDLE_THRESHOLD = DEFINE_GUID(
        0x81CD32E0,
        0x7833,
        0x44F3,
        0x87,
        0x37,
        0x70,
        0x81,
        0xF3,
        0x8D,
        0x1F,
        0x70
    )

    # Specifies (in seconds) how LONG we wait after the system is deemed
    # "idle" before moving to standby (S1, S2 or S3).
    GUID_STANDBY_TIMEOUT = DEFINE_GUID(
        0x29F6C1DB,
        0x86DA,
        0x48C5,
        0x9F,
        0xDB,
        0xF2,
        0xB6,
        0x7B,
        0x1F,
        0x44,
        0xDA
    )

    # Specifies (in seconds) how LONG the system should go back to sleep after
    # waking unattended. 0 indicates that the standard standby/hibernate idle
    # policy should be used instead.
    # {7bc4a2f9 - d8fc - 4469 - b07b - 33eb785aaca0}
    GUID_UNATTEND_SLEEP_TIMEOUT = DEFINE_GUID(
        0x7BC4A2F9,
        0xD8FC,
        0x4469,
        0xB0,
        0x7B,
        0x33,
        0xEB,
        0x78,
        0x5A,
        0xAC,
        0xA0
    )

    # Specifies (in seconds) how LONG we wait after the system is deemed
    # "idle" before moving to hibernate (S4).
    GUID_HIBERNATE_TIMEOUT = DEFINE_GUID(
        0x9D7815A6,
        0x7EE4,
        0x497E,
        0x88,
        0x88,
        0x51,
        0x5A,
        0x05,
        0xF0,
        0x23,
        0x64
    )

    # Specifies whether or not Fast S4 should be enabled if the system
    # supports it
    # 94AC6D29 - 73CE - 41A6 - 809F - 6363BA21B47E
    GUID_HIBERNATE_FASTS4_POLICY = DEFINE_GUID(
        0x94AC6D29,
        0x73CE,
        0x41A6,
        0x80,
        0x9F,
        0x63,
        0x63,
        0xBA,
        0x21,
        0xB4,
        0x7E
    )

    # Define a GUID for controlling the criticality of sleep state transitions.
    # Critical sleep transitions do not query applications, services or drivers
    # before transitioning the platform to a sleep state.
    # {B7A27025 - E569 - 46c2 - A504 - 2B96CAD225A1}
    GUID_CRITICAL_POWER_TRANSITION = DEFINE_GUID(
        0xB7A27025,
        0xE569,
        0x46C2,
        0xA5,
        0x04,
        0x2B,
        0x96,
        0xCA,
        0xD2,
        0x25,
        0xA1
    )

    # Specifies if the system is entering or exiting 'away mode'.
    # 98A7F580 - 01F7 - 48AA - 9C0F - 44352C29E5C0
    GUID_SYSTEM_AWAYMODE = DEFINE_GUID(
        0x98A7F580,
        0x01F7,
        0x48AA,
        0x9C,
        0x0F,
        0x44,
        0x35,
        0x2C,
        0x29,
        0xE5,
        0xC0
    )

    # Specify whether away mode is allowed
    # {25DFA149 - 5DD1 - 4736 - B5AB - E8A37B5B8187}
    GUID_ALLOW_AWAYMODE = DEFINE_GUID(
        0x25DFA149,
        0x5DD1,
        0x4736,
        0xB5,
        0xAB,
        0xE8,
        0xA3,
        0x7B,
        0x5B,
        0x81,
        0x87
    )

    # Defines a guid to control User Presence Prediction mode.
    # {82011705 - FB95 - 4D46 - 8D35 - 4042B1D20DEF}
    GUID_USER_PRESENCE_PREDICTION = DEFINE_GUID(
        0x82011705,
        0xFB95,
        0x4D46,
        0x8D,
        0x35,
        0x40,
        0x42,
        0xB1,
        0xD2,
        0xD,
        0xEF
    )

    # Defines a guid to control Standby Budget Grace Period.
    # {60C07FE1 - 0556 - 45CF - 9903 - D56E32210242}
    GUID_STANDBY_BUDGET_GRACE_PERIOD = DEFINE_GUID(
        0x60C07FE1,
        0x0556,
        0x45CF,
        0x99,
        0x03,
        0xD5,
        0x6E,
        0x32,
        0x21,
        0x2,
        0x42
    )

    # Defines a guid to control Standby Budget Percent.
    # {9FE527BE - 1B70 - 48DA - 930D - 7BCF17B44990}
    GUID_STANDBY_BUDGET_PERCENT = DEFINE_GUID(
        0x9FE527BE,
        0x1B70,
        0x48DA,
        0x93,
        0x0D,
        0x7B,
        0xCF,
        0x17,
        0xB4,
        0x49,
        0x90
    )

    # Defines a guid to control Standby Reserve Grace Period.
    # {C763EE92 - 71E8 - 4127 - 84EB - F6ED043A3E3D}
    GUID_STANDBY_RESERVE_GRACE_PERIOD = DEFINE_GUID(
        0xC763EE92,
        0x71E8,
        0x4127,
        0x84,
        0xEB,
        0xF6,
        0xED,
        0x04,
        0x3A,
        0x3E,
        0x3D
    )

    # Defines a guid to control Standby Reserve Time.
    # {468FE7E5 - 1158 - 46EC - 88BC - 5B96C9E44FD0}
    GUID_STANDBY_RESERVE_TIME = DEFINE_GUID(
        0x468FE7E5,
        0x1158,
        0x46EC,
        0x88,
        0xBC,
        0x5B,
        0x96,
        0xC9,
        0xE4,
        0x4F,
        0xD0
    )

    # Defines a guid to control Standby Reset Percentage.
    # {49CB11A5 - 56E2 - 4AFB - 9D38 - 3DF47872E21B}
    GUID_STANDBY_RESET_PERCENT = DEFINE_GUID(
        0x49CB11A5,
        0x56E2,
        0x4AFB,
        0x9D,
        0x38,
        0x3D,
        0xF4,
        0x78,
        0x72,
        0xE2,
        0x1B
    )

    # Defines a guid for enabling/disabling standby (S1 - S3) states. This
    # does not
    # affect hibernation (S4).
    # {abfc2519 - 3608 - 4c2a - 94ea - 171b0ed546ab}
    GUID_ALLOW_STANDBY_STATES = DEFINE_GUID(
        0xABFC2519,
        0x3608,
        0x4C2A,
        0x94,
        0xEA,
        0x17,
        0x1B,
        0x0E,
        0xD5,
        0x46,
        0xAB
    )

    # Defines a guid for enabling/disabling the ability to wake via RTC.
    # {BD3B718A - 0680 - 4D9D - 8AB2 - E1D2B4AC806D}
    GUID_ALLOW_RTC_WAKE = DEFINE_GUID(
        0xBD3B718A,
        0x0680,
        0x4D9D,
        0x8A,
        0xB2,
        0xE1,
        0xD2,
        0xB4,
        0xAC,
        0x80,
        0x6D
    )

    # Defines a guid for enabling/disabling legacy RTC mitigations.
    # {1A34BDC3 - 7E6B - 442E - A9D0 - 64B6EF378E84}
    GUID_LEGACY_RTC_MITIGATION = DEFINE_GUID(
        0x1A34BDC3,
        0x7E6B,
        0x442E,
        0xA9,
        0xD0,
        0x64,
        0xB6,
        0xEF,
        0x37,
        0x8E,
        0x84
    )

    # Defines a guid for enabling/disabling the ability to create system
    # required
    # power requests.
    # {A4B195F5 - 8225 - 47D8 - 8012 - 9D41369786E2}
    GUID_ALLOW_SYSTEM_REQUIRED = DEFINE_GUID(
        0xA4B195F5,
        0x8225,
        0x47D8,
        0x80,
        0x12,
        0x9D,
        0x41,
        0x36,
        0x97,
        0x86,
        0xE2
    )

    # Energy Saver settings
    # - - - - - - - - - - - - - - - - - - - - -
    # Indicates if Enegry Saver is ON or OFF.
    # {E00958C0 - C213 - 4ACE - AC77 - FECCED2EEEA5}
    GUID_POWER_SAVING_STATUS = DEFINE_GUID(
        0xE00958C0,
        0xC213,
        0x4ACE,
        0xAC,
        0x77,
        0xFE,
        0xCC,
        0xED,
        0x2E,
        0xEE,
        0xA5
    )

    # Specifies the subgroup which will contain all of the Energy Saver
    # settings
    # for a single policy.
    # {DE830923 - A562 - 41AF - A086 - E3A2C6BAD2DA}
    GUID_ENERGY_SAVER_SUBGROUP = DEFINE_GUID(
        0xDE830923,
        0xA562,
        0x41AF,
        0xA0,
        0x86,
        0xE3,
        0xA2,
        0xC6,
        0xBA,
        0xD2,
        0xDA
    )

    # Defines a guid to engage Energy Saver at specific battery CHARge level
    # {E69653CA - CF7F - 4F05 - AA73 - CB833FA90AD4}
    GUID_ENERGY_SAVER_BATTERY_THRESHOLD = DEFINE_GUID(
        0xE69653CA,
        0xCF7F,
        0x4F05,
        0xAA,
        0x73,
        0xCB,
        0x83,
        0x3F,
        0xA9,
        0x0A,
        0xD4
    )

    # Defines a guid to specify display brightness weight when Energy Saver is
    # engaged
    # {13D09884 - F74E - 474A - A852 - B6BDE8AD03A8}
    GUID_ENERGY_SAVER_BRIGHTNESS = DEFINE_GUID(
        0x13D09884,
        0xF74E,
        0x474A,
        0xA8,
        0x52,
        0xB6,
        0xBD,
        0xE8,
        0xAD,
        0x03,
        0xA8
    )

    # Defines a guid to specify the Energy Saver policy
    # {5C5BB349 - AD29 - 4ee2 - 9D0B - 2B25270F7A81}
    GUID_ENERGY_SAVER_POLICY = DEFINE_GUID(
        0x5C5BB349,
        0xAD29,
        0x4EE2,
        0x9D,
        0xB,
        0x2B,
        0x25,
        0x27,
        0xF,
        0x7A,
        0x81
    )

    # System button actions
    # - - - - - - - - - - - - - - - - - - - - -
    # Specifies the subgroup which will contain all of the system button
    # settings for a single policy.
    GUID_SYSTEM_BUTTON_SUBGROUP = DEFINE_GUID(
        0x4F971E89,
        0xEEBD,
        0x4455,
        0xA8,
        0xDE,
        0x9E,
        0x59,
        0x04,
        0x0E,
        0x73,
        0x47
    )
    POWERBUTTON_ACTION_INDEX_NOTHING = 0
    POWERBUTTON_ACTION_INDEX_SLEEP = 1
    POWERBUTTON_ACTION_INDEX_HIBERNATE = 2
    POWERBUTTON_ACTION_INDEX_SHUTDOWN = 3
    POWERBUTTON_ACTION_INDEX_TURN_OFF_THE_DISPLAY = 4

    # System button values which contain the PowerAction* value for each
    # action.
    POWERBUTTON_ACTION_VALUE_NOTHING = 0
    POWERBUTTON_ACTION_VALUE_SLEEP = 2
    POWERBUTTON_ACTION_VALUE_HIBERNATE = 3
    POWERBUTTON_ACTION_VALUE_SHUTDOWN = 6
    POWERBUTTON_ACTION_VALUE_TURN_OFF_THE_DISPLAY = 8

    # Specifies (in a POWER_ACTION_POLICY structure) the appropriate action to
    # take when the system power button is pressed.
    GUID_POWERBUTTON_ACTION = DEFINE_GUID(
        0x7648EFA3,
        0xDD9C,
        0x4E3E,
        0xB5,
        0x66,
        0x50,
        0xF9,
        0x29,
        0x38,
        0x62,
        0x80
    )

    # Specifies (in a POWER_ACTION_POLICY structure) the appropriate action to
    # take when the system sleep button is pressed.
    GUID_SLEEPBUTTON_ACTION = DEFINE_GUID(
        0x96996BC0,
        0xAD50,
        0x47EC,
        0x92,
        0x3B,
        0x6F,
        0x41,
        0x87,
        0x4D,
        0xD9,
        0xEB
    )

    # Specifies (in a POWER_ACTION_POLICY structure) the appropriate action to
    # take when the system sleep button is pressed.
    # { A7066653 - 8D6C - 40A8 - 910E - A1F54B84C7E5 }
    GUID_USERINTERFACEBUTTON_ACTION = DEFINE_GUID(
        0xA7066653,
        0x8D6C,
        0x40A8,
        0x91,
        0x0E,
        0xA1,
        0xF5,
        0x4B,
        0x84,
        0xC7,
        0xE5
    )

    # Specifies (in a POWER_ACTION_POLICY structure) the appropriate action to
    # take when the system lid is closed.
    GUID_LIDCLOSE_ACTION = DEFINE_GUID(
        0x5CA83367,
        0x6E45,
        0x459F,
        0xA2,
        0x7B,
        0x47,
        0x6B,
        0x1D,
        0x01,
        0xC9,
        0x36
    )
    GUID_LIDOPEN_POWERSTATE = DEFINE_GUID(
        0x99FF10E7,
        0x23B1,
        0x4C07,
        0xA9,
        0xD1,
        0x5C,
        0x32,
        0x06,
        0xD7,
        0x41,
        0xB4
    )

    # Battery DisCHARge Settings
    # - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Specifies the subgroup which will contain all of the battery disCHARge
    # settings for a single policy.
    GUID_BATTERY_SUBGROUP = DEFINE_GUID(
        0xE73A048D,
        0xBF27,
        0x4F12,
        0x97,
        0x31,
        0x8B,
        0x20,
        0x76,
        0xE8,
        0x89,
        0x1F
    )

    # 4 battery disCHARge alarm settings.
    # GUID_BATTERY_DISCHARGE_ACTION_x - This is the action to take. It is a
    # value
    # of type POWER_ACTION
    # GUID_BATTERY_DISCHARGE_LEVEL_x - This is the battery level (%)
    # GUID_BATTERY_DISCHARGE_FLAGS_x - Flags defined below:
    # POWER_ACTION_POLICY - >EventCode flags
    # BATTERY_DISCHARGE_FLAGS_EVENTCODE_MASK
    # BATTERY_DISCHARGE_FLAGS_ENABLE
    GUID_BATTERY_DISCHARGE_ACTION_0 = DEFINE_GUID(
        0x637EA02F,
        0xBBCB,
        0x4015,
        0x8E,
        0x2C,
        0xA1,
        0xC7,
        0xB9,
        0xC0,
        0xB5,
        0x46
    )
    GUID_BATTERY_DISCHARGE_LEVEL_0 = DEFINE_GUID(
        0x9A66D8D7,
        0x4FF7,
        0x4EF9,
        0xB5,
        0xA2,
        0x5A,
        0x32,
        0x6C,
        0xA2,
        0xA4,
        0x69
    )
    GUID_BATTERY_DISCHARGE_FLAGS_0 = DEFINE_GUID(
        0x5DBB7C9F,
        0x38E9,
        0x40D2,
        0x97,
        0x49,
        0x4F,
        0x8A,
        0x0E,
        0x9F,
        0x64,
        0x0F
    )
    GUID_BATTERY_DISCHARGE_ACTION_1 = DEFINE_GUID(
        0xD8742DCB,
        0x3E6A,
        0x4B3C,
        0xB3,
        0xFE,
        0x37,
        0x46,
        0x23,
        0xCD,
        0xCF,
        0x06
    )
    GUID_BATTERY_DISCHARGE_LEVEL_1 = DEFINE_GUID(
        0x8183BA9A,
        0xE910,
        0x48DA,
        0x87,
        0x69,
        0x14,
        0xAE,
        0x6D,
        0xC1,
        0x17,
        0x0A
    )
    GUID_BATTERY_DISCHARGE_FLAGS_1 = DEFINE_GUID(
        0xBCDED951,
        0x187B,
        0x4D05,
        0xBC,
        0xCC,
        0xF7,
        0xE5,
        0x19,
        0x60,
        0xC2,
        0x58
    )
    GUID_BATTERY_DISCHARGE_ACTION_2 = DEFINE_GUID(
        0x421CBA38,
        0x1A8E,
        0x4881,
        0xAC,
        0x89,
        0xE3,
        0x3A,
        0x8B,
        0x04,
        0xEC,
        0xE4
    )
    GUID_BATTERY_DISCHARGE_LEVEL_2 = DEFINE_GUID(
        0x07A07CA2,
        0xADAF,
        0x40D7,
        0xB0,
        0x77,
        0x53,
        0x3A,
        0xAD,
        0xED,
        0x1B,
        0xFA
    )
    GUID_BATTERY_DISCHARGE_FLAGS_2 = DEFINE_GUID(
        0x7FD2F0C4,
        0xFEB7,
        0x4DA3,
        0x81,
        0x17,
        0xE3,
        0xFB,
        0xED,
        0xC4,
        0x65,
        0x82
    )
    GUID_BATTERY_DISCHARGE_ACTION_3 = DEFINE_GUID(
        0x80472613,
        0x9780,
        0x455E,
        0xB3,
        0x08,
        0x72,
        0xD3,
        0x00,
        0x3C,
        0xF2,
        0xF8
    )
    GUID_BATTERY_DISCHARGE_LEVEL_3 = DEFINE_GUID(
        0x58AFD5A6,
        0xC2DD,
        0x47D2,
        0x9F,
        0xBF,
        0xEF,
        0x70,
        0xCC,
        0x5C,
        0x59,
        0x65
    )
    GUID_BATTERY_DISCHARGE_FLAGS_3 = DEFINE_GUID(
        0x73613CCF,
        0xDBFA,
        0x4279,
        0x83,
        0x56,
        0x49,
        0x35,
        0xF6,
        0xBF,
        0x62,
        0xF3
    )

    # Processor power settings
    # - - - - - - - - - - - - - - - - - - - - - - - -
    # Specifies the subgroup which will contain all of the processor
    # settings for a single policy.
    # {54533251 - 82be - 4824 - 96c1 - 47b60b740d00}
    GUID_PROCESSOR_SETTINGS_SUBGROUP = DEFINE_GUID(
        0x54533251,
        0x82BE,
        0x4824,
        0x96,
        0xC1,
        0x47,
        0xB6,
        0x0B,
        0x74,
        0x0D,
        0x00
    )

    # Specifies various attributes that control processor performance/throttle
    # states.
    GUID_PROCESSOR_THROTTLE_POLICY = DEFINE_GUID(
        0x57027304,
        0x4AF6,
        0x4104,
        0x92,
        0x60,
        0xE3,
        0xD9,
        0x52,
        0x48,
        0xFC,
        0x36
    )
    PERFSTATE_POLICY_CHANGE_IDEAL = 0
    PERFSTATE_POLICY_CHANGE_SINGLE = 1
    PERFSTATE_POLICY_CHANGE_ROCKET = 2
    PERFSTATE_POLICY_CHANGE_IDEAL_AGGRESSIVE = 3
    PERFSTATE_POLICY_CHANGE_DECREASE_MAX = PERFSTATE_POLICY_CHANGE_ROCKET
    PERFSTATE_POLICY_CHANGE_INCREASE_MAX = (
        PERFSTATE_POLICY_CHANGE_IDEAL_AGGRESSIVE
    )

    # Specifies a percentage (between 0 and 100) that the processor frequency
    # should never go above. For example, if this value is set to 80, then
    # the processor frequency will never be throttled above 80 percent of its
    # maximum frequency by the system.
    # {bc5038f7 - 23e0 - 4960 - 96da - 33abaf5935ec}
    GUID_PROCESSOR_THROTTLE_MAXIMUM = DEFINE_GUID(
        0xBC5038F7,
        0x23E0,
        0x4960,
        0x96,
        0xDA,
        0x33,
        0xAB,
        0xAF,
        0x59,
        0x35,
        0xEC
    )

    # Specifies a percentage (between 0 and 100) that the processor frequency
    # should never go above for Processor Power Efficiency Class 1.
    # For example, if this value is set to 80, then the processor frequency
    # will
    # never be throttled above 80 percent of its maximum frequency by the
    # system.
    # {bc5038f7 - 23e0 - 4960 - 96da - 33abaf5935ed}
    GUID_PROCESSOR_THROTTLE_MAXIMUM_1 = DEFINE_GUID(
        0xBC5038F7,
        0x23E0,
        0x4960,
        0x96,
        0xDA,
        0x33,
        0xAB,
        0xAF,
        0x59,
        0x35,
        0xED
    )

    # Specifies a percentage (between 0 and 100) that the processor frequency
    # should not drop below. For example, if this value is set to 50, then the
    # processor frequency will never be throttled below 50 percent of its
    # maximum frequency by the system.
    # {893dee8e - 2bef - 41e0 - 89c6 - b55d0929964c}
    GUID_PROCESSOR_THROTTLE_MINIMUM = DEFINE_GUID(
        0x893DEE8E,
        0x2BEF,
        0x41E0,
        0x89,
        0xC6,
        0xB5,
        0x5D,
        0x09,
        0x29,
        0x96,
        0x4C
    )

    # Specifies a percentage (between 0 and 100) that the processor frequency
    # should not drop below for Processor Power Efficiency Class 1.
    # For example, if this value is set to 50, then the processor frequency
    # will
    # never be throttled below 50 percent of its maximum frequency by the
    # system.
    # {893dee8e - 2bef - 41e0 - 89c6 - b55d0929964d}
    GUID_PROCESSOR_THROTTLE_MINIMUM_1 = DEFINE_GUID(
        0x893DEE8E,
        0x2BEF,
        0x41E0,
        0x89,
        0xC6,
        0xB5,
        0x5D,
        0x09,
        0x29,
        0x96,
        0x4D
    )

    # Specifies the maximum processor frequency (expresssed in MHz).
    # {75B0AE3F - BCE0 - 45a7 - 8C89 - C9611C25E100}
    GUID_PROCESSOR_FREQUENCY_LIMIT = DEFINE_GUID(
        0x75B0AE3F,
        0xBCE0,
        0x45A7,
        0x8C,
        0x89,
        0xC9,
        0x61,
        0x1C,
        0x25,
        0xE1,
        0x00
    )

    # {75B0AE3F - BCE0 - 45a7 - 8C89 - C9611C25E101}
    GUID_PROCESSOR_FREQUENCY_LIMIT_1 = DEFINE_GUID(
        0x75B0AE3F,
        0xBCE0,
        0x45A7,
        0x8C,
        0x89,
        0xC9,
        0x61,
        0x1C,
        0x25,
        0xE1,
        0x01
    )

    # Specifies whether throttle states are allowed to be used even when
    # performance states are available.
    # {3b04d4fd - 1cc7 - 4f23 - ab1c - d1337819c4bb}
    GUID_PROCESSOR_ALLOW_THROTTLING = DEFINE_GUID(
        0x3B04D4FD,
        0x1CC7,
        0x4F23,
        0xAB,
        0x1C,
        0xD1,
        0x33,
        0x78,
        0x19,
        0xC4,
        0xBB
    )
    PROCESSOR_THROTTLE_DISABLED = 0
    PROCESSOR_THROTTLE_ENABLED = 1
    PROCESSOR_THROTTLE_AUTOMATIC = 2

    # Specifies processor power settings for CState policy data
    # {68F262A7 - F621 - 4069 - B9A5 - 4874169BE23C}
    GUID_PROCESSOR_IDLESTATE_POLICY = DEFINE_GUID(
        0x68F262A7,
        0xF621,
        0x4069,
        0xB9,
        0xA5,
        0x48,
        0x74,
        0x16,
        0x9B,
        0xE2,
        0x3C
    )

    # Specifies processor power settings for PerfState policy data
    # {BBDC3814 - 18E9 - 4463 - 8A55 - D197327C45C0}
    GUID_PROCESSOR_PERFSTATE_POLICY = DEFINE_GUID(
        0xBBDC3814,
        0x18E9,
        0x4463,
        0x8A,
        0x55,
        0xD1,
        0x97,
        0x32,
        0x7C,
        0x45,
        0xC0
    )

    # Specifies the increase busy percentage threshold that must be met before
    # increasing the processor performance state.
    # {06cadf0e - 64ed - 448a - 8927 - ce7bf90eb35d}
    GUID_PROCESSOR_PERF_INCREASE_THRESHOLD = DEFINE_GUID(
        0x06CADF0E,
        0x64ED,
        0x448A,
        0x89,
        0x27,
        0xCE,
        0x7B,
        0xF9,
        0x0E,
        0xB3,
        0x5D
    )

    # Specifies the increase busy percentage threshold that must be met before
    # increasing the processor performance state for Processor Power Efficiency
    # Class 1.
    # {06cadf0e - 64ed - 448a - 8927 - ce7bf90eb35e}
    GUID_PROCESSOR_PERF_INCREASE_THRESHOLD_1 = DEFINE_GUID(
        0x06CADF0E,
        0x64ED,
        0x448A,
        0x89,
        0x27,
        0xCE,
        0x7B,
        0xF9,
        0x0E,
        0xB3,
        0x5E
    )

    # Specifies the decrease busy percentage threshold that must be met before
    # decreasing the processor performance state.
    # {12a0ab44 - fe28 - 4fa9 - b3bd - 4b64f44960a6}
    GUID_PROCESSOR_PERF_DECREASE_THRESHOLD = DEFINE_GUID(
        0x12A0AB44,
        0xFE28,
        0x4FA9,
        0xB3,
        0xBD,
        0x4B,
        0x64,
        0xF4,
        0x49,
        0x60,
        0xA6
    )

    # Specifies the decrease busy percentage threshold that must be met before
    # decreasing the processor performance state for Processor Power Efficiency
    # Class 1.
    # {12a0ab44 - fe28 - 4fa9 - b3bd - 4b64f44960a7}
    GUID_PROCESSOR_PERF_DECREASE_THRESHOLD_1 = DEFINE_GUID(
        0x12A0AB44,
        0xFE28,
        0x4FA9,
        0xB3,
        0xBD,
        0x4B,
        0x64,
        0xF4,
        0x49,
        0x60,
        0xA7
    )

    # Specifies, either as ideal, single or rocket, how aggressive performance
    # states should be selected when increasing the processor performance
    # state.
    # {465E1F50 - B610 - 473a - AB58 - 00D1077DC418}
    GUID_PROCESSOR_PERF_INCREASE_POLICY = DEFINE_GUID(
        0x465E1F50,
        0xB610,
        0x473A,
        0xAB,
        0x58,
        0x0,
        0xD1,
        0x7,
        0x7D,
        0xC4,
        0x18
    )

    # Specifies, either as ideal, single or rocket, how aggressive performance
    # states should be selected when increasing the processor performance state
    # for Processor Power Efficiency Class 1.
    # {465E1F50 - B610 - 473a - AB58 - 00D1077DC419}
    GUID_PROCESSOR_PERF_INCREASE_POLICY_1 = DEFINE_GUID(
        0x465E1F50,
        0xB610,
        0x473A,
        0xAB,
        0x58,
        0x0,
        0xD1,
        0x7,
        0x7D,
        0xC4,
        0x19
    )

    # Specifies, either as ideal, single or rocket, how aggressive performance
    # states should be selected when decreasing the processor performance
    # state.
    # {40FBEFC7 - 2E9D - 4d25 - A185 - 0CFD8574BAC6}
    GUID_PROCESSOR_PERF_DECREASE_POLICY = DEFINE_GUID(
        0x40FBEFC7,
        0x2E9D,
        0x4D25,
        0xA1,
        0x85,
        0xC,
        0xFD,
        0x85,
        0x74,
        0xBA,
        0xC6
    )

    # Specifies, either as ideal, single or rocket, how aggressive performance
    # states should be selected when decreasing the processor performance
    # state for
    # Processor Power Efficiency Class 1.
    # {40FBEFC7 - 2E9D - 4d25 - A185 - 0CFD8574BAC7}
    GUID_PROCESSOR_PERF_DECREASE_POLICY_1 = DEFINE_GUID(
        0x40FBEFC7,
        0x2E9D,
        0x4D25,
        0xA1,
        0x85,
        0xC,
        0xFD,
        0x85,
        0x74,
        0xBA,
        0xC7
    )

    # Specifies, in milliseconds, the minimum amount of time that must elapse
    # after
    # the last processor performance state change before increasing the
    # processor
    # performance state.
    # {984CF492 - 3BED - 4488 - A8F9 - 4286C97BF5AA}
    GUID_PROCESSOR_PERF_INCREASE_TIME = DEFINE_GUID(
        0x984CF492,
        0x3BED,
        0x4488,
        0xA8,
        0xF9,
        0x42,
        0x86,
        0xC9,
        0x7B,
        0xF5,
        0xAA
    )

    # Specifies, in milliseconds, the minimum amount of time that must elapse
    # after
    # the last processor performance state change before increasing the
    # processor
    # performance state for Processor Power Efficiency Class 1.
    # {984CF492 - 3BED - 4488 - A8F9 - 4286C97BF5AB}
    GUID_PROCESSOR_PERF_INCREASE_TIME_1 = DEFINE_GUID(
        0x984CF492,
        0x3BED,
        0x4488,
        0xA8,
        0xF9,
        0x42,
        0x86,
        0xC9,
        0x7B,
        0xF5,
        0xAB
    )

    # Specifies, in milliseconds, the minimum amount of time that must elapse
    # after
    # the last processor performance state change before increasing the
    # processor
    # performance state.
    # {D8EDEB9B - 95CF - 4f95 - A73C - B061973693C8}
    GUID_PROCESSOR_PERF_DECREASE_TIME = DEFINE_GUID(
        0xD8EDEB9B,
        0x95CF,
        0x4F95,
        0xA7,
        0x3C,
        0xB0,
        0x61,
        0x97,
        0x36,
        0x93,
        0xC8
    )

    # Specifies, in milliseconds, the minimum amount of time that must elapse
    # after
    # the last processor performance state change before increasing the
    # processor
    # performance state for Processor Power Efficiency Class 1.
    # {D8EDEB9B - 95CF - 4f95 - A73C - B061973693C9}
    GUID_PROCESSOR_PERF_DECREASE_TIME_1 = DEFINE_GUID(
        0xD8EDEB9B,
        0x95CF,
        0x4F95,
        0xA7,
        0x3C,
        0xB0,
        0x61,
        0x97,
        0x36,
        0x93,
        0xC9
    )

    # Specifies the time, in milliseconds, that must expire before considering
    # a change in the processor performance states or parked core set.
    # {4D2B0152 - 7D5C - 498b - 88E2 - 34345392A2C5}
    GUID_PROCESSOR_PERF_TIME_CHECK = DEFINE_GUID(
        0x4D2B0152,
        0x7D5C,
        0x498B,
        0x88,
        0xE2,
        0x34,
        0x34,
        0x53,
        0x92,
        0xA2,
        0xC5
    )

    # Specifies how the processor should manage performance and efficiency
    # tradeoffs when boosting frequency above the maximum.
    # {45BCC044 - D885 - 43e2 - 8605 - EE0EC6E96B59}
    GUID_PROCESSOR_PERF_BOOST_POLICY = DEFINE_GUID(
        0x45BCC044,
        0xD885,
        0x43E2,
        0x86,
        0x5,
        0xEE,
        0xE,
        0xC6,
        0xE9,
        0x6B,
        0x59
    )
    PROCESSOR_PERF_BOOST_POLICY_DISABLED = 0
    PROCESSOR_PERF_BOOST_POLICY_MAX = 100

    # Specifies how a processor opportunistically increases frequency above
    # the maximum when operating contitions allow it to do so safely.
    # {BE337238 - 0D82 - 4146 - A960 - 4F3749D470C7}
    GUID_PROCESSOR_PERF_BOOST_MODE = DEFINE_GUID(
        0xBE337238,
        0xD82,
        0x4146,
        0xA9,
        0x60,
        0x4F,
        0x37,
        0x49,
        0xD4,
        0x70,
        0xC7
    )
    PROCESSOR_PERF_BOOST_MODE_DISABLED = 0
    PROCESSOR_PERF_BOOST_MODE_ENABLED = 1
    PROCESSOR_PERF_BOOST_MODE_AGGRESSIVE = 2
    PROCESSOR_PERF_BOOST_MODE_EFFICIENT_ENABLED = 3
    PROCESSOR_PERF_BOOST_MODE_EFFICIENT_AGGRESSIVE = 4
    PROCESSOR_PERF_BOOST_MODE_AGGRESSIVE_AT_GUARANTEED = 5
    PROCESSOR_PERF_BOOST_MODE_EFFICIENT_AGGRESSIVE_AT_GUARANTEED = 6
    PROCESSOR_PERF_BOOST_MODE_MAX = (
        PROCESSOR_PERF_BOOST_MODE_EFFICIENT_AGGRESSIVE_AT_GUARANTEED
    )

    # Specifies whether or not a procesor should autonomously select its
    # operating performance state.
    # {8BAA4A8A - 14C6 - 4451 - 8E8B - 14BDBD197537}
    GUID_PROCESSOR_PERF_AUTONOMOUS_MODE = DEFINE_GUID(
        0x8BAA4A8A,
        0x14C6,
        0x4451,
        0x8E,
        0x8B,
        0x14,
        0xBD,
        0xBD,
        0x19,
        0x75,
        0x37
    )
    PROCESSOR_PERF_AUTONOMOUS_MODE_DISABLED = 0
    PROCESSOR_PERF_AUTONOMOUS_MODE_ENABLED = 1

    # Specifies the tradeoff between performance and energy the processor
    # should
    # make when operating in autonomous mode.
    # {36687F9E - E3A5 - 4dbf - B1DC - 15EB381C6863}
    GUID_PROCESSOR_PERF_ENERGY_PERFORMANCE_PREFERENCE = DEFINE_GUID(
        0x36687F9E,
        0xE3A5,
        0x4DBF,
        0xB1,
        0xDC,
        0x15,
        0xEB,
        0x38,
        0x1C,
        0x68,
        0x63
    )
    PROCESSOR_PERF_PERFORMANCE_PREFERENCE = 0xFF
    PROCESSOR_PERF_ENERGY_PREFERENCE = 0

    # Specifies the window over which the processor should observe utilization
    # when
    # operating in autonomous mode, in microseconds.
    # {CFEDA3D0 - 7697 - 4566 - A922 - A9086CD49DFA}
    GUID_PROCESSOR_PERF_AUTONOMOUS_ACTIVITY_WINDOW = DEFINE_GUID(
        0xCFEDA3D0,
        0x7697,
        0x4566,
        0xA9,
        0x22,
        0xA9,
        0x8,
        0x6C,
        0xD4,
        0x9D,
        0xFA
    )
    PROCESSOR_PERF_MINIMUM_ACTIVITY_WINDOW = 0
    PROCESSOR_PERF_MAXIMUM_ACTIVITY_WINDOW = 1270000000

    # Specifies whether the processor should perform duty cycling.
    # {4E4450B3 - 6179 - 4e91 - B8F1 - 5BB9938F81A1}
    GUID_PROCESSOR_DUTY_CYCLING = DEFINE_GUID(
        0x4E4450B3,
        0x6179,
        0x4E91,
        0xB8,
        0xF1,
        0x5B,
        0xB9,
        0x93,
        0x8F,
        0x81,
        0xA1
    )
    PROCESSOR_DUTY_CYCLING_DISABLED = 0
    PROCESSOR_DUTY_CYCLING_ENABLED = 1

    # Specifies if idle state promotion and demotion values should be scaled
    # based
    # on the current peformance state.
    # {6C2993B0 - 8F48 - 481f - BCC6 - 00DD2742AA06}
    GUID_PROCESSOR_IDLE_ALLOW_SCALING = DEFINE_GUID(
        0x6C2993B0,
        0x8F48,
        0x481F,
        0xBC,
        0xC6,
        0x0,
        0xDD,
        0x27,
        0x42,
        0xAA,
        0x6
    )

    # Specifies if idle states should be disabled.
    # {5D76A2CA - E8C0 - 402f - A133 - 2158492D58AD}
    GUID_PROCESSOR_IDLE_DISABLE = DEFINE_GUID(
        0x5D76A2CA,
        0xE8C0,
        0x402F,
        0xA1,
        0x33,
        0x21,
        0x58,
        0x49,
        0x2D,
        0x58,
        0xAD
    )

    # Specifies the deepest idle state type that should be used. If this value
    # is
    # set to zero, this setting is ignored. Values higher than supported by the
    # processor then this setting has no effect.
    # {9943e905 - 9a30 - 4ec1 - 9b99 - 44dd3b76f7a2}
    GUID_PROCESSOR_IDLE_STATE_MAXIMUM = DEFINE_GUID(
        0x9943E905,
        0x9A30,
        0x4EC1,
        0x9B,
        0x99,
        0x44,
        0xDD,
        0x3B,
        0x76,
        0xF7,
        0xA2
    )

    # Specifies the time that elapsed since the last idle state promotion or
    # demotion before idle states may be promoted or demoted again (in
    # microseconds).
    # {C4581C31 - 89AB - 4597 - 8E2B - 9C9CAB440E6B}
    GUID_PROCESSOR_IDLE_TIME_CHECK = DEFINE_GUID(
        0xC4581C31,
        0x89AB,
        0x4597,
        0x8E,
        0x2B,
        0x9C,
        0x9C,
        0xAB,
        0x44,
        0xE,
        0x6B
    )

    # Specifies the upper busy threshold that must be met before demoting the
    # processor to a lighter idle state (in percentage).
    # {4B92D758 - 5A24 - 4851 - A470 - 815D78AEE119}
    GUID_PROCESSOR_IDLE_DEMOTE_THRESHOLD = DEFINE_GUID(
        0x4B92D758,
        0x5A24,
        0x4851,
        0xA4,
        0x70,
        0x81,
        0x5D,
        0x78,
        0xAE,
        0xE1,
        0x19
    )

    # Specifies the lower busy threshold that must be met before promoting the
    # processor to a deeper idle state (in percentage).
    # {7B224883 - B3CC - 4d79 - 819F - 8374152CBE7C}
    GUID_PROCESSOR_IDLE_PROMOTE_THRESHOLD = DEFINE_GUID(
        0x7B224883,
        0xB3CC,
        0x4D79,
        0x81,
        0x9F,
        0x83,
        0x74,
        0x15,
        0x2C,
        0xBE,
        0x7C
    )

    # Specifies the utilization threshold in percent that must be crossed in
    # order to un - park cores.
    # N.B. This power setting is DEPRECATED.
    # {df142941 - 20f3 - 4edf - 9a4a - 9c83d3d717d1}
    GUID_PROCESSOR_CORE_PARKING_INCREASE_THRESHOLD = DEFINE_GUID(
        0xDF142941,
        0x20F3,
        0x4EDF,
        0x9A,
        0x4A,
        0x9C,
        0x83,
        0xD3,
        0xD7,
        0x17,
        0xD1
    )

    # Specifies the utilization threshold in percent that must be crossed in
    # order to park cores.
    # N.B. This power setting is DEPRECATED.
    # {68dd2f27 - a4ce - 4e11 - 8487 - 3794e4135dfa}
    GUID_PROCESSOR_CORE_PARKING_DECREASE_THRESHOLD = DEFINE_GUID(
        0x68DD2F27,
        0xA4CE,
        0x4E11,
        0x84,
        0x87,
        0x37,
        0x94,
        0xE4,
        0x13,
        0x5D,
        0xFA
    )

    # Specifies, either as ideal, single or rocket, how aggressive core
    # parking is when cores must be unparked.
    # {c7be0679 - 2817 - 4d69 - 9d02 - 519a537ed0c6}
    GUID_PROCESSOR_CORE_PARKING_INCREASE_POLICY = DEFINE_GUID(
        0xC7BE0679,
        0x2817,
        0x4D69,
        0x9D,
        0x02,
        0x51,
        0x9A,
        0x53,
        0x7E,
        0xD0,
        0xC6
    )
    CORE_PARKING_POLICY_CHANGE_IDEAL = 0
    CORE_PARKING_POLICY_CHANGE_SINGLE = 1
    CORE_PARKING_POLICY_CHANGE_ROCKET = 2
    CORE_PARKING_POLICY_CHANGE_MULTISTEP = 3
    CORE_PARKING_POLICY_CHANGE_MAX = CORE_PARKING_POLICY_CHANGE_MULTISTEP

    # Specifies, either as ideal, single or rocket, how aggressive core
    # parking is when cores must be parked.
    # {71021b41 - c749 - 4d21 - be74 - a00f335d582b}
    GUID_PROCESSOR_CORE_PARKING_DECREASE_POLICY = DEFINE_GUID(
        0x71021B41,
        0xC749,
        0x4D21,
        0xBE,
        0x74,
        0xA0,
        0x0F,
        0x33,
        0x5D,
        0x58,
        0x2B
    )

    # Specifies, on a per processor group basis, the maximum number of cores
    # that can be kept unparked.
    # {ea062031 - 0e34 - 4ff1 - 9b6d - eb1059334028}
    GUID_PROCESSOR_CORE_PARKING_MAX_CORES = DEFINE_GUID(
        0xEA062031,
        0x0E34,
        0x4FF1,
        0x9B,
        0x6D,
        0xEB,
        0x10,
        0x59,
        0x33,
        0x40,
        0x28
    )

    # Specifies, on a per processor group basis, the maximum number of cores
    # that
    # can be kept unparked for Processor Power Efficiency Class 1.
    # {ea062031 - 0e34 - 4ff1 - 9b6d - eb1059334029}
    GUID_PROCESSOR_CORE_PARKING_MAX_CORES_1 = DEFINE_GUID(
        0xEA062031,
        0x0E34,
        0x4FF1,
        0x9B,
        0x6D,
        0xEB,
        0x10,
        0x59,
        0x33,
        0x40,
        0x29
    )

    # Specifies, on a per processor group basis, the minimum number of cores
    # that must be kept unparked.
    # {0cc5b647 - c1df - 4637 - 891a - dec35c318583}
    GUID_PROCESSOR_CORE_PARKING_MIN_CORES = DEFINE_GUID(
        0x0CC5B647,
        0xC1DF,
        0x4637,
        0x89,
        0x1A,
        0xDE,
        0xC3,
        0x5C,
        0x31,
        0x85,
        0x83
    )

    # Specifies, on a per processor group basis, the minimum number of cores
    # that
    # must be kept unparked in Processor Power Efficiency Class 1.
    # {0cc5b647 - c1df - 4637 - 891a - dec35c318584}
    GUID_PROCESSOR_CORE_PARKING_MIN_CORES_1 = DEFINE_GUID(
        0x0CC5B647,
        0xC1DF,
        0x4637,
        0x89,
        0x1A,
        0xDE,
        0xC3,
        0x5C,
        0x31,
        0x85,
        0x84
    )

    # Specifies, in milliseconds, the minimum amount of time a core must be
    # parked before it can be unparked.
    # {2ddd5a84 - 5a71 - 437e - 912a - db0b8c788732}
    GUID_PROCESSOR_CORE_PARKING_INCREASE_TIME = DEFINE_GUID(
        0x2DDD5A84,
        0x5A71,
        0x437E,
        0x91,
        0x2A,
        0xDB,
        0x0B,
        0x8C,
        0x78,
        0x87,
        0x32
    )

    # Specifies, in milliseconds, the minimum amount of time a core must be
    # unparked before it can be parked.
    # {dfd10d17 - d5eb - 45dd - 877a - 9a34ddd15c82}
    GUID_PROCESSOR_CORE_PARKING_DECREASE_TIME = DEFINE_GUID(
        0xDFD10D17,
        0xD5EB,
        0x45DD,
        0x87,
        0x7A,
        0x9A,
        0x34,
        0xDD,
        0xD1,
        0x5C,
        0x82
    )

    # Specifies the factor by which to decrease affinity history on each core
    # after each check.
    # {8f7b45e3 - c393 - 480a - 878c - f67ac3d07082}
    GUID_PROCESSOR_CORE_PARKING_AFFINITY_HISTORY_DECREASE_FACTOR = DEFINE_GUID(
        0x8F7B45E3,
        0xC393,
        0x480A,
        0x87,
        0x8C,
        0xF6,
        0x7A,
        0xC3,
        0xD0,
        0x70,
        0x82
    )

    # Specifies the threshold above which a core is considered to have had
    # significant affinitized work scheduled to it while parked.
    # {5b33697b - e89d - 4d38 - aa46 - 9e7dfb7cd2f9}
    GUID_PROCESSOR_CORE_PARKING_AFFINITY_HISTORY_THRESHOLD = DEFINE_GUID(
        0x5B33697B,
        0xE89D,
        0x4D38,
        0xAA,
        0x46,
        0x9E,
        0x7D,
        0xFB,
        0x7C,
        0xD2,
        0xF9
    )

    # Specifies the weighting given to each occurence where affinitized work
    # was scheduled to a parked core.
    # {e70867f1 - fa2f - 4f4e - aea1 - 4d8a0ba23b20}
    GUID_PROCESSOR_CORE_PARKING_AFFINITY_WEIGHTING = DEFINE_GUID(
        0xE70867F1,
        0xFA2F,
        0x4F4E,
        0xAE,
        0xA1,
        0x4D,
        0x8A,
        0x0B,
        0xA2,
        0x3B,
        0x20
    )

    # Specifies the factor by which to decrease the over utilization history
    # on each core after the current performance check.
    # {1299023c - bc28 - 4f0a - 81ec - d3295a8d815d}
    GUID_PROCESSOR_CORE_PARKING_OVER_UTILIZATION_HISTORY_DECREASE_FACTOR = DEFINE_GUID(
        0x1299023C,
        0xBC28,
        0x4F0A,
        0x81,
        0xEC,
        0xD3,
        0x29,
        0x5A,
        0x8D,
        0x81,
        0x5D
    )

    # Specifies the threshold above which a core is considered to have been
    # recently over utilized while parked.
    # {9ac18e92 - aa3c - 4e27 - b307 - 01ae37307129}
    GUID_PROCESSOR_CORE_PARKING_OVER_UTILIZATION_HISTORY_THRESHOLD = DEFINE_GUID(
        0x9AC18E92,
        0xAA3C,
        0x4E27,
        0xB3,
        0x07,
        0x01,
        0xAE,
        0x37,
        0x30,
        0x71,
        0x29
    )

    # Specifies the weighting given to each occurence where a parked core is
    # found to be over utilized.
    # {8809c2d8 - b155 - 42d4 - bcda - 0d345651b1db}
    GUID_PROCESSOR_CORE_PARKING_OVER_UTILIZATION_WEIGHTING = DEFINE_GUID(
        0x8809C2D8,
        0xB155,
        0x42D4,
        0xBC,
        0xDA,
        0x0D,
        0x34,
        0x56,
        0x51,
        0xB1,
        0xDB
    )

    # Specifies, in percentage, the busy threshold that must be met before a
    # parked core is considered over utilized.
    # {943c8cb6 - 6f93 - 4227 - ad87 - e9a3feec08d1}
    GUID_PROCESSOR_CORE_PARKING_OVER_UTILIZATION_THRESHOLD = DEFINE_GUID(
        0x943C8CB6,
        0x6F93,
        0x4227,
        0xAD,
        0x87,
        0xE9,
        0xA3,
        0xFE,
        0xEC,
        0x08,
        0xD1
    )

    # Specifies if at least one processor per core should always remain
    # unparked.
    # {a55612aa - f624 - 42c6 - a443 - 7397d064c04f}
    GUID_PROCESSOR_PARKING_CORE_OVERRIDE = DEFINE_GUID(
        0xA55612AA,
        0xF624,
        0x42C6,
        0xA4,
        0x43,
        0x73,
        0x97,
        0xD0,
        0x64,
        0xC0,
        0x4F
    )

    # Specifies what performance state a processor should enter when first
    # parked.
    # {447235c7 - 6a8d - 4cc0 - 8e24 - 9eaf70b96e2b}
    GUID_PROCESSOR_PARKING_PERF_STATE = DEFINE_GUID(
        0x447235C7,
        0x6A8D,
        0x4CC0,
        0x8E,
        0x24,
        0x9E,
        0xAF,
        0x70,
        0xB9,
        0x6E,
        0x2B
    )

    # Specifies what performance state a processor should enter when first
    # parked
    # for Processor Power Efficiency Class 1.
    # {447235c7 - 6a8d - 4cc0 - 8e24 - 9eaf70b96e2c}
    GUID_PROCESSOR_PARKING_PERF_STATE_1 = DEFINE_GUID(
        0x447235C7,
        0x6A8D,
        0x4CC0,
        0x8E,
        0x24,
        0x9E,
        0xAF,
        0x70,
        0xB9,
        0x6E,
        0x2C
    )

    # Specify the busy threshold that must be met when calculating the
    # concurrency of a node's workload.
    # {2430ab6f - a520 - 44a2 - 9601 - f7f23b5134b1}
    GUID_PROCESSOR_PARKING_CONCURRENCY_THRESHOLD = DEFINE_GUID(
        0x2430AB6F,
        0xA520,
        0x44A2,
        0x96,
        0x01,
        0xF7,
        0xF2,
        0x3B,
        0x51,
        0x34,
        0xB1
    )

    # Specify the busy threshold that must be met by all cores in a
    # concurrency set to unpark an extra core.
    # {f735a673 - 2066 - 4f80 - a0c5 - ddee0cf1bf5d}
    GUID_PROCESSOR_PARKING_HEADROOM_THRESHOLD = DEFINE_GUID(
        0xF735A673,
        0x2066,
        0x4F80,
        0xA0,
        0xC5,
        0xDD,
        0xEE,
        0x0C,
        0xF1,
        0xBF,
        0x5D
    )

    # Specify the percentage utilization used to calculate the distribution
    # concurrency.
    # {4bdaf4e9 - d103 - 46d7 - a5f0 - 6280121616ef}
    GUID_PROCESSOR_PARKING_DISTRIBUTION_THRESHOLD = DEFINE_GUID(
        0x4BDAF4E9,
        0xD103,
        0x46D7,
        0xA5,
        0xF0,
        0x62,
        0x80,
        0x12,
        0x16,
        0x16,
        0xEF
    )

    # Specifies the number of perf time check intervals to average utility
    # over.
    # {7d24baa7 - 0b84 - 480f - 840c - 1b0743c00f5f}
    GUID_PROCESSOR_PERF_HISTORY = DEFINE_GUID(
        0x7D24BAA7,
        0x0B84,
        0x480F,
        0x84,
        0x0C,
        0x1B,
        0x07,
        0x43,
        0xC0,
        0x0F,
        0x5F
    )

    # Specifies the number of perf time check intervals to average utility
    # over in
    # Processor Power Efficiency Class 1.
    # {7d24baa7 - 0b84 - 480f - 840c - 1b0743c00f60}
    GUID_PROCESSOR_PERF_HISTORY_1 = DEFINE_GUID(
        0x7D24BAA7,
        0x0B84,
        0x480F,
        0x84,
        0x0C,
        0x1B,
        0x07,
        0x43,
        0xC0,
        0x0F,
        0x60
    )

    # Specifies the number of perf time check intervals to average utility
    # over to
    # determine performance increase.
    # N.B. This power setting is DEPRECATED.
    # {99B3EF01 - 752F - 46a1 - 80FB - 7730011F2354}
    GUID_PROCESSOR_PERF_INCREASE_HISTORY = DEFINE_GUID(
        0x99B3EF01,
        0x752F,
        0x46A1,
        0x80,
        0xFB,
        0x77,
        0x30,
        0x1,
        0x1F,
        0x23,
        0x54
    )

    # Specifies the number of perf time check intervals to average utility
    # over to
    # determine performance decrease.
    # N.B. This power setting is DEPRECATED.
    # {0300F6F8 - ABD6 - 45a9 - B74F - 4908691A40B5}
    GUID_PROCESSOR_PERF_DECREASE_HISTORY = DEFINE_GUID(
        0x300F6F8,
        0xABD6,
        0x45A9,
        0xB7,
        0x4F,
        0x49,
        0x8,
        0x69,
        0x1A,
        0x40,
        0xB5
    )

    # Specifies the number of perf time check intervals to average utility
    # over for
    # core parking.
    # N.B. This power setting is DEPRECATED.
    # {77D7F282 - 8F1A - 42cd - 8537 - 45450A839BE8}
    GUID_PROCESSOR_PERF_CORE_PARKING_HISTORY = DEFINE_GUID(
        0x77D7F282,
        0x8F1A,
        0x42CD,
        0x85,
        0x37,
        0x45,
        0x45,
        0xA,
        0x83,
        0x9B,
        0xE8
    )

    # Specifies whether latency sensitivity hints should be taken into account
    # by
    # the perf state engine.
    # N.B. This power setting is DEPRECATED.
    # {0822df31 - 9c83 - 441c - a079 - 0de4cf009c7b}
    GUID_PROCESSOR_PERF_LATENCY_HINT = DEFINE_GUID(
        0x0822DF31,
        0x9C83,
        0x441C,
        0xA0,
        0x79,
        0x0D,
        0xE4,
        0xCF,
        0x00,
        0x9C,
        0x7B
    )

    # Specifies the processor performance state in response to latency
    # sensitivity hints.
    # {619b7505 - 003b - 4e82 - b7a6 - 4dd29c300971}
    GUID_PROCESSOR_PERF_LATENCY_HINT_PERF = DEFINE_GUID(
        0x619B7505,
        0x3B,
        0x4E82,
        0xB7,
        0xA6,
        0x4D,
        0xD2,
        0x9C,
        0x30,
        0x9,
        0x71
    )

    # Specifies the processor performance state in response to latency
    # sensitivity
    # hints for Processor Power Efficiency Class 1.
    # {619b7505 - 003b - 4e82 - b7a6 - 4dd29c300972}
    GUID_PROCESSOR_PERF_LATENCY_HINT_PERF_1 = DEFINE_GUID(
        0x619B7505,
        0x3B,
        0x4E82,
        0xB7,
        0xA6,
        0x4D,
        0xD2,
        0x9C,
        0x30,
        0x9,
        0x72
    )

    # Specifies the minimum unparked processors when a latency hint is active
    # (in a percentage).
    # {616cdaa5 - 695e - 4545 - 97ad - 97dc2d1bdd88}
    GUID_PROCESSOR_LATENCY_HINT_MIN_UNPARK = DEFINE_GUID(
        0x616CDAA5,
        0x695E,
        0x4545,
        0x97,
        0xAD,
        0x97,
        0xDC,
        0x2D,
        0x1B,
        0xDD,
        0x88
    )

    # Specifies the minimum unparked processors when a latency hint is active
    # for Processor Power Efficiency Class 1 (in a percentage).
    # {616cdaa5 - 695e - 4545 - 97ad - 97dc2d1bdd89}
    GUID_PROCESSOR_LATENCY_HINT_MIN_UNPARK_1 = DEFINE_GUID(
        0x616CDAA5,
        0x695E,
        0x4545,
        0x97,
        0xAD,
        0x97,
        0xDC,
        0x2D,
        0x1B,
        0xDD,
        0x89
    )

    # Specifies whether the core parking engine should distribute processor
    # utility.
    # {e0007330 - f589 - 42ed - a401 - 5ddb10e785d3}
    GUID_PROCESSOR_DISTRIBUTE_UTILITY = DEFINE_GUID(
        0xE0007330,
        0xF589,
        0x42ED,
        0xA4,
        0x01,
        0x5D,
        0xDB,
        0x10,
        0xE7,
        0x85,
        0xD3
    )

    # GUIDS to control PPM settings on computer system with more than one
    # Processor Power Efficiency Classes (heterogeneous system).
    # - - - - - - - - - - - - - - - - -
    # Specifies the current active heterogeneous policy.
    # {7f2f5cfa - f10c - 4823 - b5e1 - e93ae85f46b5}
    GUID_PROCESSOR_HETEROGENEOUS_POLICY = DEFINE_GUID(
        0x7F2F5CFA,
        0xF10C,
        0x4823,
        0xB5,
        0xE1,
        0xE9,
        0x3A,
        0xE8,
        0x5F,
        0x46,
        0xB5
    )

    # Specifies the number of perf check cycles required to decrease the
    # number of
    # Processor Power Efficiency Class 1 processors.
    # {7f2492b6 - 60b1 - 45e5 - ae55 - 773f8cd5caec}
    GUID_PROCESSOR_HETERO_DECREASE_TIME = DEFINE_GUID(
        0x7F2492B6,
        0x60B1,
        0x45E5,
        0xAE,
        0x55,
        0x77,
        0x3F,
        0x8C,
        0xD5,
        0xCA,
        0xEC
    )

    # Specifies the number of perf check cycles required to increase the
    # number of
    # Processor Power Efficiency Class 1 processors.
    # {4009efa7 - e72d - 4cba - 9edf - 91084ea8cbc3}
    GUID_PROCESSOR_HETERO_INCREASE_TIME = DEFINE_GUID(
        0x4009EFA7,
        0xE72D,
        0x4CBA,
        0x9E,
        0xDF,
        0x91,
        0x08,
        0x4E,
        0xA8,
        0xCB,
        0xC3
    )

    # Specifies the performance level (in units of Processor Power Efficiency
    # Class 0 processor performance) at which the number of Processor Power
    # Efficiency Class 1 processors is decreased.
    # {f8861c27 - 95e7 - 475c - 865b - 13c0cb3f9d6b}
    GUID_PROCESSOR_HETERO_DECREASE_THRESHOLD = DEFINE_GUID(
        0xF8861C27,
        0x95E7,
        0x475C,
        0x86,
        0x5B,
        0x13,
        0xC0,
        0xCB,
        0x3F,
        0x9D,
        0x6B
    )

    # Specifies the performance level (in units of Processor Power Efficiency
    # Class 0 processor performance) at which the number of Processor Power
    # Efficiency Class 1 processors is increased.
    # {b000397d - 9b0b - 483d - 98c9 - 692a6060cfbf}
    GUID_PROCESSOR_HETERO_INCREASE_THRESHOLD = DEFINE_GUID(
        0xB000397D,
        0x9B0B,
        0x483D,
        0x98,
        0xC9,
        0x69,
        0x2A,
        0x60,
        0x60,
        0xCF,
        0xBF
    )

    # Specifies the performance target floor of a Processor Power Efficiency
    # Class 0 processor when the system unparks Processor Power Efficiency
    # Class 1
    # processor(s).
    # {fddc842b - 8364 - 4edc - 94cf - c17f60de1c80}
    GUID_PROCESSOR_CLASS0_FLOOR_PERF = DEFINE_GUID(
        0xFDDC842B,
        0x8364,
        0x4EDC,
        0x94,
        0xCF,
        0xC1,
        0x7F,
        0x60,
        0xDE,
        0x1C,
        0x80
    )

    # Specifies the initial performance target of a Processor Power Efficiency
    # Class 1 processor when the system makes a transition up from zero
    # Processor
    # Power Efficiency Class 1 processors.
    # {1facfc65 - a930 - 4bc5 - 9f38 - 504ec097bbc0}
    GUID_PROCESSOR_CLASS1_INITIAL_PERF = DEFINE_GUID(
        0x1FACFC65,
        0xA930,
        0x4BC5,
        0x9F,
        0x38,
        0x50,
        0x4E,
        0xC0,
        0x97,
        0xBB,
        0xC0
    )

    # Specifies the scheduling policy for threads in a given QoS class.
    # {93B8B6DC - 0698 - 4d1c - 9EE4 - 0644E900C85D}
    GUID_PROCESSOR_THREAD_SCHEDULING_POLICY = DEFINE_GUID(
        0x93B8B6DC,
        0x698,
        0x4D1C,
        0x9E,
        0xE4,
        0x6,
        0x44,
        0xE9,
        0x0,
        0xC8,
        0x5D
    )

    # Specifies the scheduling policy for SHORT running threads in a given QoS
    # class.
    # {BAE08B81 - 2D5E - 4688 - AD6A - 13243356654B}
    GUID_PROCESSOR_SHORT_THREAD_SCHEDULING_POLICY = DEFINE_GUID(
        0xBAE08B81,
        0x2D5E,
        0x4688,
        0xAD,
        0x6A,
        0x13,
        0x24,
        0x33,
        0x56,
        0x65,
        0x4B
    )

    # Specifies active vs passive cooling. Although not directly related to
    # processor settings, it is the processor that gets throttled if we're
    # doing
    # passive cooling, so it is fairly strongly related.
    # {94D3A615 - A899 - 4AC5 - AE2B - E4D8F634367F}
    GUID_SYSTEM_COOLING_POLICY = DEFINE_GUID(
        0x94D3A615,
        0xA899,
        0x4AC5,
        0xAE,
        0x2B,
        0xE4,
        0xD8,
        0xF6,
        0x34,
        0x36,
        0x7F
    )

    # Lock Console on Wake
    # - - - - - - - - - - - - - - - - - - - -
    # Specifies the behavior of the system when we wake from standby or
    # hibernate. If this is set, then we will cause the console to lock
    # after we resume.
    GUID_LOCK_CONSOLE_ON_WAKE = DEFINE_GUID(
        0x0E796BDB,
        0x100D,
        0x47D6,
        0xA2,
        0xD5,
        0xF7,
        0xD2,
        0xDA,
        0xA5,
        0x1F,
        0x51
    )

    # Device idle CHARacteristics
    # - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Specifies whether to use the "performance" or "conservative" timeouts for
    # device idle management.
    # 4faab71a - 92e5 - 4726 - b531 - 224559672d19
    GUID_DEVICE_IDLE_POLICY = DEFINE_GUID(
        0x4FAAB71A,
        0x92E5,
        0x4726,
        0xB5,
        0x31,
        0x22,
        0x45,
        0x59,
        0x67,
        0x2D,
        0x19
    )
    POWER_DEVICE_IDLE_POLICY_PERFORMANCE = 0
    POWER_DEVICE_IDLE_POLICY_CONSERVATIVE = 1

    # Specifies standby connectivity preference.
    # F15576E8 - 98B7 - 4186 - B944 - EAFA664402D9
    GUID_CONNECTIVITY_IN_STANDBY = DEFINE_GUID(
        0xF15576E8,
        0x98B7,
        0x4186,
        0xB9,
        0x44,
        0xEA,
        0xFA,
        0x66,
        0x44,
        0x02,
        0xD9
    )
    POWER_CONNECTIVITY_IN_STANDBY_DISABLED = 0
    POWER_CONNECTIVITY_IN_STANDBY_ENABLED = 1
    POWER_CONNECTIVITY_IN_STANDBY_SYSTEM_MANAGED = 2

    # Specifies the mode for disconnected standby.
    # 68AFB2D9 - EE95 - 47A8 - 8F50 - 4115088073B1
    GUID_DISCONNECTED_STANDBY_MODE = DEFINE_GUID(
        0x68AFB2D9,
        0xEE95,
        0x47A8,
        0x8F,
        0x50,
        0x41,
        0x15,
        0x08,
        0x80,
        0x73,
        0xB1
    )
    POWER_DISCONNECTED_STANDBY_MODE_NORMAL = 0
    POWER_DISCONNECTED_STANDBY_MODE_AGGRESSIVE = 1

    # AC/DC power source
    # - - - - - - - - - - - - - - - - - -
    # Specifies the power source for the system. consumers may register for
    # notification when the power source changes and will be notified with
    # one of 3 values:
    # 0 - Indicates the system is being powered by an AC power source.
    # 1 - Indicates the system is being powered by a DC power source.
    # 2 - Indicates the system is being powered by a SHORT - term DC power
    # source. For example, this would be the case if the system is
    # being powed by a SHORT - term battery supply in a backing UPS
    # system. When this value is recieved, the consumer should make
    # preparations for either a system hibernate or system shutdown.
    # { 5D3E9A59 - E9D5 - 4B00 - A6BD - FF34FF516548 }
    GUID_ACDC_POWER_SOURCE = DEFINE_GUID(
        0x5D3E9A59,
        0xE9D5,
        0x4B00,
        0xA6,
        0xBD,
        0xFF,
        0x34,
        0xFF,
        0x51,
        0x65,
        0x48
    )

    # Lid state changes
    # - - - - - - - - - - - - - - - - -
    # Specifies the current state of the lid (open or closed). The callback
    # won't
    # be called at all until a lid device is found and its current state is
    # known.
    # Values:
    # 0 - closed
    # 1 - opened
    # { BA3E0F4D - B817 - 4094 - A2D1 - D56379E6A0F3 }
    GUID_LIDSWITCH_STATE_CHANGE = DEFINE_GUID(
        0xBA3E0F4D,
        0xB817,
        0x4094,
        0xA2,
        0xD1,
        0xD5,
        0x63,
        0x79,
        0xE6,
        0xA0,
        0xF3
    )

    # Battery status changes
    # - - - - - - - - - - - - - - - - - - - - - -
    # Specifies the percentage of battery life remaining. The consumer
    # may register for notification in order to track battery life in
    # a fine - grained manner.
    # Once registered, the consumer can expect to be notified as the battery
    # life percentage changes.
    # The consumer will recieve a value between 0 and 100 (inclusive) which
    # indicates percent battery life remaining.
    # { A7AD8041 - B45A - 4CAE - 87A3 - EECBB468A9E1 }
    GUID_BATTERY_PERCENTAGE_REMAINING = DEFINE_GUID(
        0xA7AD8041,
        0xB45A,
        0x4CAE,
        0x87,
        0xA3,
        0xEE,
        0xCB,
        0xB4,
        0x68,
        0xA9,
        0xE1
    )

    # Specifies change in number of batteries present on the system. The
    # consumer
    # may register for notification in order to track change in number of
    # batteries
    # available on a system.
    # Once registered, the consumer can expect to be notified whenever the
    # batteries are added or removed from the system.
    # The consumer will recieve a value indicating number of batteries
    # currently
    # present on the system.
    # {7D263F15 - FCA4 - 49E5 - 854B - A9F2BFBD5C24}
    GUID_BATTERY_COUNT = DEFINE_GUID(
        0x7D263F15,
        0xFCA4,
        0x49E5,
        0x85,
        0x4B,
        0xA9,
        0xF2,
        0xBF,
        0xBD,
        0x5C,
        0x24
    )

    # Global notification indicating to listeners user activity/presence
    # accross
    # all sessions in the system (Present, NotPresent, Inactive)
    # {786E8A1D - B427 - 4344 - 9207 - 09E70BDCBEA9}
    GUID_GLOBAL_USER_PRESENCE = DEFINE_GUID(
        0x786E8A1D,
        0xB427,
        0x4344,
        0x92,
        0x7,
        0x9,
        0xE7,
        0xB,
        0xDC,
        0xBE,
        0xA9
    )

    # Session specific notification indicating to listeners whether or not the
    # display
    # related to the given session is on/off/dim
    # N.B. This is a session - specific notification, sent only to interactive
    # session registrants. Session 0 and kernel mode consumers do not receive
    # this notification.
    # {2B84C20E - AD23 - 4ddf - 93DB - 05FFBD7EFCA5}
    GUID_SESSION_DISPLAY_STATUS = DEFINE_GUID(
        0x2B84C20E,
        0xAD23,
        0x4DDF,
        0x93,
        0xDB,
        0x5,
        0xFF,
        0xBD,
        0x7E,
        0xFC,
        0xA5
    )

    # Session specific notification indicating to listeners user
    # activity/presence
    # (Present, NotPresent, Inactive)
    # N.B. This is a session - specific notification, sent only to interactive
    # session registrants. Session 0 and kernel mode consumers do not receive
    # this notification.
    # {3C0F4548 - C03F - 4c4d - B9F2 - 237EDE686376}
    GUID_SESSION_USER_PRESENCE = DEFINE_GUID(
        0x3C0F4548,
        0xC03F,
        0x4C4D,
        0xB9,
        0xF2,
        0x23,
        0x7E,
        0xDE,
        0x68,
        0x63,
        0x76
    )

    # Notification to listeners that the system is fairly busy and won't be
    # moving
    # into an idle state any time soon. This can be used as a hint to listeners
    # that now might be a good time to do background tasks.
    GUID_IDLE_BACKGROUND_TASK = DEFINE_GUID(
        0x515C31D8,
        0xF734,
        0x163D,
        0xA0,
        0xFD,
        0x11,
        0xA0,
        0x8C,
        0x91,
        0xE8,
        0xF1
    )

    # Notification to listeners that the system is fairly busy and won't be
    # moving
    # into an idle state any time soon. This can be used as a hint to listeners
    # that now might be a good time to do background tasks.
    # { CF23F240 - 2A54 - 48D8 - B114 - DE1518FF052E }
    GUID_BACKGROUND_TASK_NOTIFICATION = DEFINE_GUID(
        0xCF23F240,
        0x2A54,
        0x48D8,
        0xB1,
        0x14,
        0xDE,
        0x15,
        0x18,
        0xFF,
        0x05,
        0x2E
    )

    # Define a GUID that will represent the action of a direct experience
    # button
    # on the platform. Users will register for this DPPE setting and recieve
    # notification when the h/w button is pressed.
    # { 1A689231 - 7399 - 4E9A - 8F99 - B71F999DB3FA }
    GUID_APPLAUNCH_BUTTON = DEFINE_GUID(
        0x1A689231,
        0x7399,
        0x4E9A,
        0x8F,
        0x99,
        0xB7,
        0x1F,
        0x99,
        0x9D,
        0xB3,
        0xFA
    )

    # PCI Express power settings
    # - - - - - - - - - - - - - - - - - - - - - - - -
    # Specifies the subgroup which will contain all of the PCI Express
    # settings for a single policy.
    # {501a4d13 - 42af - 4429 - 9fd1 - a8218c268e20}
    GUID_PCIEXPRESS_SETTINGS_SUBGROUP = DEFINE_GUID(
        0x501A4D13,
        0x42AF,
        0x4429,
        0x9F,
        0xD1,
        0xA8,
        0x21,
        0x8C,
        0x26,
        0x8E,
        0x20
    )

    # Specifies the PCI Express ASPM power policy.
    # {ee12f906 - d277 - 404b - b6da - e5fa1a576df5}
    GUID_PCIEXPRESS_ASPM_POLICY = DEFINE_GUID(
        0xEE12F906,
        0xD277,
        0x404B,
        0xB6,
        0xDA,
        0xE5,
        0xFA,
        0x1A,
        0x57,
        0x6D,
        0xF5
    )

    # POWER Shutdown settings
    # - - - - - - - - - - - - - - - - - - - - - - - -
    # Specifies if forced shutdown should be used for all button and lid
    # initiated
    # shutdown actions.
    # {833a6b62 - dfa4 - 46d1 - 82f8 - e09e34d029d6}
    GUID_ENABLE_SWITCH_FORCED_SHUTDOWN = DEFINE_GUID(
        0x833A6B62,
        0xDFA4,
        0x46D1,
        0x82,
        0xF8,
        0xE0,
        0x9E,
        0x34,
        0xD0,
        0x29,
        0xD6
    )

    # Interrupt Steering power settings
    # - - - - - - - - - - - - - - - - - - - - - - - -
    # {48672F38 - 7A9A - 4bb2 - 8BF8 - 3D85BE19DE4E}
    GUID_INTSTEER_SUBGROUP = DEFINE_GUID(
        0x48672F38,
        0x7A9A,
        0x4BB2,
        0x8B,
        0xF8,
        0x3D,
        0x85,
        0xBE,
        0x19,
        0xDE,
        0x4E
    )

    # {2BFC24F9 - 5EA2 - 4801 - 8213 - 3DBAE01AA39D}
    GUID_INTSTEER_MODE = DEFINE_GUID(
        0x2BFC24F9,
        0x5EA2,
        0x4801,
        0x82,
        0x13,
        0x3D,
        0xBA,
        0xE0,
        0x1A,
        0xA3,
        0x9D
    )

    # {73CDE64D - D720 - 4bb2 - A860 - C755AFE77EF2}
    GUID_INTSTEER_LOAD_PER_PROC_TRIGGER = DEFINE_GUID(
        0x73CDE64D,
        0xD720,
        0x4BB2,
        0xA8,
        0x60,
        0xC7,
        0x55,
        0xAF,
        0xE7,
        0x7E,
        0xF2
    )

    # {D6BA4903 - 386F - 4c2c - 8ADB - 5C21B3328D25}
    GUID_INTSTEER_TIME_UNPARK_TRIGGER = DEFINE_GUID(
        0xD6BA4903,
        0x386F,
        0x4C2C,
        0x8A,
        0xDB,
        0x5C,
        0x21,
        0xB3,
        0x32,
        0x8D,
        0x25
    )

    # Graphics power settings
    # - - - - - - - - - - - - - - - - - - - - - - - -
    # Specified the subgroup which contains all inbox graphics settings.
    # {5FB4938D - 1EE8 - 4b0f - 9A3C - 5036B0AB995C}
    GUID_GRAPHICS_SUBGROUP = DEFINE_GUID(
        0x5FB4938D,
        0x1EE8,
        0x4B0F,
        0x9A,
        0x3C,
        0x50,
        0x36,
        0xB0,
        0xAB,
        0x99,
        0x5C
    )

    # Specifies the GPU preference policy.
    # {DD848B2A - 8A5D - 4451 - 9AE2 - 39CD41658F6C}
    GUID_GPU_PREFERENCE_POLICY = DEFINE_GUID(
        0xDD848B2A,
        0x8A5D,
        0x4451,
        0x9A,
        0xE2,
        0x39,
        0xCD,
        0x41,
        0x65,
        0x8F,
        0x6C
    )

    # Other miscellaneous power notification GUIDs
    # - - - - - - - - - - - - - - - - - - - - - - - -
    # Specifies whether mixed reality mode is engaged.
    # {1E626B4E - CF04 - 4f8d - 9CC7 - C97C5B0F2391}
    GUID_MIXED_REALITY_MODE = DEFINE_GUID(
        0x1E626B4E,
        0xCF04,
        0x4F8D,
        0x9C,
        0xC7,
        0xC9,
        0x7C,
        0x5B,
        0xF,
        0x23,
        0x91
    )

    # Specifies a change (start/end) in System Power Report's Active Session.
    # {0E24CE38 - C393 - 4742 - BDB1 - 744F4B9EE08E}
    GUID_SPR_ACTIVE_SESSION_CHANGE = DEFINE_GUID(
        0xE24CE38,
        0xC393,
        0x4742,
        0xBD,
        0xB1,
        0x74,
        0x4F,
        0x4B,
        0x9E,
        0xE0,
        0x8E
    )

    if not defined(_PO_DDK_):
        _PO_DDK_ = 1


        class _SYSTEM_POWER_STATE(ENUM):
            PowerSystemUnspecified = 0
            PowerSystemWorking = 1
            PowerSystemSleeping1 = 2
            PowerSystemSleeping2 = 3
            PowerSystemSleeping3 = 4
            PowerSystemHibernate = 5
            PowerSystemShutdown = 6
            PowerSystemMaximum = 7


        SYSTEM_POWER_STATE = _SYSTEM_POWER_STATE
        PSYSTEM_POWER_STATE = POINTER(_SYSTEM_POWER_STATE)
        POWER_SYSTEM_MAXIMUM = 7


        class POWER_ACTION(ENUM):
            PowerActionNone = 0
            PowerActionReserved = 1
            PowerActionSleep = 2
            PowerActionHibernate = 3
            PowerActionShutdown = 4
            PowerActionShutdownReset = 5
            PowerActionShutdownOff = 6
            PowerActionWarmEject = 7
            PowerActionDisplayOff = 8


        PPOWER_ACTION = POINTER(POWER_ACTION)
        PowerActionNone = POWER_ACTION.PowerActionNone
        PowerActionReserved = POWER_ACTION.PowerActionReserved
        PowerActionSleep = POWER_ACTION.PowerActionSleep
        PowerActionHibernate = POWER_ACTION.PowerActionHibernate
        PowerActionShutdown = POWER_ACTION.PowerActionShutdown
        PowerActionShutdownReset = POWER_ACTION.PowerActionShutdownReset
        PowerActionShutdownOff = POWER_ACTION.PowerActionShutdownOff
        PowerActionWarmEject = POWER_ACTION.PowerActionWarmEject
        PowerActionDisplayOff = POWER_ACTION.PowerActionDisplayOff
        class _DEVICE_POWER_STATE(ENUM):
            PowerDeviceUnspecified = 0
            PowerDeviceD0 = 1
            PowerDeviceD1 = 2
            PowerDeviceD2 = 3
            PowerDeviceD3 = 4
            PowerDeviceMaximum = 5


        DEVICE_POWER_STATE = _DEVICE_POWER_STATE
        PDEVICE_POWER_STATE = POINTER(_DEVICE_POWER_STATE)
        class _MONITOR_DISPLAY_STATE(ENUM):
            PowerMonitorOff = 0
            PowerMonitorOn = 1
            PowerMonitorDim = 2


        MONITOR_DISPLAY_STATE = _MONITOR_DISPLAY_STATE
        PMONITOR_DISPLAY_STATE = POINTER(_MONITOR_DISPLAY_STATE)
        class _USER_ACTIVITY_PRESENCE(ENUM):
            PowerUserPresent = 0
            PowerUserNotPresent = 1
            PowerUserInactive = 2
            PowerUserMaximum = 3
            PowerUserInvalid = PowerUserMaximum


        USER_ACTIVITY_PRESENCE = _USER_ACTIVITY_PRESENCE
        PUSER_ACTIVITY_PRESENCE = POINTER(_USER_ACTIVITY_PRESENCE)
        class _POWER_STATE(ctypes.Union):
            pass


        _POWER_STATE._fields_ = [
            ('SystemState', SYSTEM_POWER_STATE),
            ('DeviceState', DEVICE_POWER_STATE),
        ]
        POWER_STATE = _POWER_STATE
        PPOWER_STATE = POINTER(_POWER_STATE)
        class _POWER_STATE_TYPE(ENUM):
            SystemPowerState = 0
            DevicePowerState = 1


        POWER_STATE_TYPE = _POWER_STATE_TYPE
        PPOWER_STATE_TYPE = POINTER(_POWER_STATE_TYPE)
        if NTDDI_VERSION >= NTDDI_VISTA:
            class _SYSTEM_POWER_STATE_CONTEXT(ctypes.Structure):
                pass


            class DUMMYUNIONNAME(ctypes.Structure):
                pass


            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('Reserved1', ULONG, 8),
                ('TargetSystemState', ULONG, 4),
                ('EffectiveSystemState', ULONG, 4),
                ('CurrentSystemState', ULONG, 4),
                ('IgnoreHibernationPath', ULONG, 1),
                ('PseudoTransition', ULONG, 1),
                ('KernelSoftReboot', ULONG, 1),
                ('Reserved2', ULONG, 9),
            ]
            DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
            DUMMYUNIONNAME._fields_ = [
                ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
                ('ContextAsULONG', ULONG),
            ]
            _SYSTEM_POWER_STATE_CONTEXT.DUMMYUNIONNAME = DUMMYUNIONNAME
            _SYSTEM_POWER_STATE_CONTEXT._fields_ = [
                ('DUMMYUNIONNAME', _SYSTEM_POWER_STATE_CONTEXT.DUMMYUNIONNAME),
            ]
            SYSTEM_POWER_STATE_CONTEXT = _SYSTEM_POWER_STATE_CONTEXT
            PSYSTEM_POWER_STATE_CONTEXT = POINTER(_SYSTEM_POWER_STATE_CONTEXT)
        # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
        if NTDDI_VERSION >= NTDDI_WIN7:
            class _COUNTED_REASON_CONTEXT(ctypes.Structure):
                pass


            class DUMMYUNIONNAME(ctypes.Structure):
                pass


            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('ResourceFileName', UNICODE_STRING),
                ('ResourceReasonId', USHORT),
                ('StringCount', ULONG),
                ('ReasonStrings', PUNICODE_STRING),
            ]
            DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
            DUMMYUNIONNAME._fields_ = [
                ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
                ('SimpleString', UNICODE_STRING),
            ]
            _COUNTED_REASON_CONTEXT.DUMMYUNIONNAME = DUMMYUNIONNAME
            _COUNTED_REASON_CONTEXT._fields_ = [
                ('Version', ULONG),
                ('Flags', ULONG),
                ('DUMMYUNIONNAME', _COUNTED_REASON_CONTEXT.DUMMYUNIONNAME),
            ]
            COUNTED_REASON_CONTEXT = _COUNTED_REASON_CONTEXT
            PCOUNTED_REASON_CONTEXT = POINTER(_COUNTED_REASON_CONTEXT)
        # END IF   (NTDDI_VERSION >= NTDDI_WIN7)
        # Generic power related IOCTLs
        IOCTL_QUERY_DEVICE_POWER_STATE = CTL_CODE(
            (FILE_DEVICE_BATTERY,
            0x0,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )
        IOCTL_SET_DEVICE_WAKE = CTL_CODE(
            (FILE_DEVICE_BATTERY,
            0x1,
            METHOD_BUFFERED,
            FILE_WRITE_ACCESS,
        )
        IOCTL_CANCEL_DEVICE_WAKE = CTL_CODE(
            (FILE_DEVICE_BATTERY,
            0x2,
            METHOD_BUFFERED,
            FILE_WRITE_ACCESS,
        )

        # Defines for W32 interfaces
        ES_SYSTEM_REQUIRED = (ULONG)0x00000001
        ES_DISPLAY_REQUIRED = (ULONG)0x00000002
        ES_USER_PRESENT = (ULONG)0x00000004
        ES_AWAYMODE_REQUIRED = (ULONG)0x00000040
        ES_CONTINUOUS = (ULONG)0x80000000
        EXECUTION_STATE = ULONG
        PEXECUTION_STATE = POINTER(ULONG)


        class LATENCY_TIME(ENUM):
            LT_DONT_CARE = 1
            LT_LOWEST_LATENCY = 2


        LT_DONT_CARE = LATENCY_TIME.LT_DONT_CARE
        LT_LOWEST_LATENCY = LATENCY_TIME.LT_LOWEST_LATENCY
        DIAGNOSTIC_REASON_VERSION = 0
        DIAGNOSTIC_REASON_SIMPLE_STRING = 0x00000001
        DIAGNOSTIC_REASON_DETAILED_STRING = 0x00000002
        DIAGNOSTIC_REASON_NOT_SPECIFIED = 0x80000000
        DIAGNOSTIC_REASON_INVALID_FLAGS = ~0x80000007

        # Defines for power request APIs
        POWER_REQUEST_CONTEXT_VERSION = DIAGNOSTIC_REASON_VERSION
        POWER_REQUEST_CONTEXT_SIMPLE_STRING = DIAGNOSTIC_REASON_SIMPLE_STRING
        POWER_REQUEST_CONTEXT_DETAILED_STRING = (
            DIAGNOSTIC_REASON_DETAILED_STRING
        )


        class _POWER_REQUEST_TYPE(ENUM):
            PowerRequestDisplayRequired = 1
            PowerRequestSystemRequired = 2
            PowerRequestAwayModeRequired = 3
            PowerRequestExecutionRequired = 4


        POWER_REQUEST_TYPE = _POWER_REQUEST_TYPE
        PPOWER_REQUEST_TYPE = POINTER(_POWER_REQUEST_TYPE)
        if NTDDI_VERSION >= NTDDI_WINXP:

            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # Device Power Information
            # Accessable via
            # CM_Get_DevInst_Registry_Property_Ex(CM_DRP_DEVICE_POWER_DATA)
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            PDCAP_D0_SUPPORTED = 0x00000001
            PDCAP_D1_SUPPORTED = 0x00000002
            PDCAP_D2_SUPPORTED = 0x00000004
            PDCAP_D3_SUPPORTED = 0x00000008
            PDCAP_WAKE_FROM_D0_SUPPORTED = 0x00000010
            PDCAP_WAKE_FROM_D1_SUPPORTED = 0x00000020
            PDCAP_WAKE_FROM_D2_SUPPORTED = 0x00000040
            PDCAP_WAKE_FROM_D3_SUPPORTED = 0x00000080
            PDCAP_WARM_EJECT_SUPPORTED = 0x00000100
            class CM_Power_Data_s(ctypes.Structure):
                pass


            CM_Power_Data_s._fields_ = [
                ('PD_Size', ULONG),
                ('PD_MostRecentPowerState', DEVICE_POWER_STATE),
                ('PD_Capabilities', ULONG),
                ('PD_D1Latency', ULONG),
                ('PD_D2Latency', ULONG),
                ('PD_D3Latency', ULONG),
                ('PD_PowerStateMapping', DEVICE_POWER_STATE * POWER_SYSTEM_MAXIMUM),
                ('PD_DeepestSystemWake', SYSTEM_POWER_STATE),
            ]
            CM_POWER_DATA = CM_Power_Data_s
            PCM_POWER_DATA = POINTER(CM_Power_Data_s)
        # END IF   (NTDDI_VERSION >= NTDDI_WINXP)


        class POWER_INFORMATION_LEVEL(ENUM):
            SystemPowerPolicyAc = 1
            SystemPowerPolicyDc = 2
            VerifySystemPolicyAc = 3
            VerifySystemPolicyDc = 4
            SystemPowerCapabilities = 5
            SystemBatteryState = 6
            SystemPowerStateHandler = 7
            ProcessorStateHandler = 8
            SystemPowerPolicyCurrent = 9
            AdministratorPowerPolicy = 10
            SystemReserveHiberFile = 11
            ProcessorInformation = 12
            SystemPowerInformation = 13
            ProcessorStateHandler2 = 14
            LastWakeTime = 15
            LastSleepTime = 16
            SystemExecutionState = 17
            SystemPowerStateNotifyHandler = 18
            ProcessorPowerPolicyAc = 19
            ProcessorPowerPolicyDc = 20
            VerifyProcessorPowerPolicyAc = 21
            VerifyProcessorPowerPolicyDc = 22
            ProcessorPowerPolicyCurrent = 23
            SystemPowerStateLogging = 24
            SystemPowerLoggingEntry = 25
            SetPowerSettingValue = 26
            NotifyUserPowerSetting = 27
            PowerInformationLevelUnused0 = 28
            SystemMonitorHiberBootPowerOff = 29
            SystemVideoState = 30
            TraceApplicationPowerMessage = 31
            TraceApplicationPowerMessageEnd = 32
            ProcessorPerfStates = 33
            ProcessorIdleStates = 34
            ProcessorCap = 35
            SystemWakeSource = 36
            SystemHiberFileInformation = 37
            TraceServicePowerMessage = 38
            ProcessorLoad = 39
            PowerShutdownNotification = 40
            MonitorCapabilities = 41
            SessionPowerInit = 42
            SessionDisplayState = 43
            PowerRequestCreate = 44
            PowerRequestAction = 45
            GetPowerRequestList = 46
            ProcessorInformationEx = 47
            NotifyUserModeLegacyPowerEvent = 48
            GroupPark = 49
            ProcessorIdleDomains = 50
            WakeTimerList = 51
            SystemHiberFileSize = 52
            ProcessorIdleStatesHv = 53
            ProcessorPerfStatesHv = 54
            ProcessorPerfCapHv = 55
            ProcessorSetIdle = 56
            LogicalProcessorIdling = 57
            UserPresence = 58
            PowerSettingNotificationName = 59
            GetPowerSettingValue = 60
            IdleResiliency = 61
            SessionRITState = 62
            SessionConnectNotification = 63
            SessionPowerCleanup = 64
            SessionLockState = 65
            SystemHiberbootState = 66
            PlatformInformation = 67
            PdcInvocation = 68
            MonitorInvocation = 69
            FirmwareTableInformationRegistered = 70
            SetShutdownSelectedTime = 71
            SuspendResumeInvocation = 72
            PlmPowerRequestCreate = 73
            ScreenOff = 74
            CsDeviceNotification = 75
            PlatformRole = 76
            LastResumePerformance = 77
            DisplayBurst = 78
            ExitLatencySamplingPercentage = 79
            RegisterSpmPowerSettings = 80
            PlatformIdleStates = 81
            ProcessorIdleVeto = 82
            PlatformIdleVeto = 83
            SystemBatteryStatePrecise = 84
            ThermalEvent = 85
            PowerRequestActionInternal = 86
            BatteryDeviceState = 87
            PowerInformationInternal = 88
            ThermalStandby = 89
            SystemHiberFileType = 90
            PhysicalPowerButtonPress = 91
            QueryPotentialDripsConstraint = 92
            EnergyTrackerCreate = 93
            EnergyTrackerQuery = 94
            UpdateBlackBoxRecorder = 95
            PowerInformationLevelMaximum = 96


        SystemPowerPolicyAc = POWER_INFORMATION_LEVEL.SystemPowerPolicyAc
        SystemPowerPolicyDc = POWER_INFORMATION_LEVEL.SystemPowerPolicyDc
        VerifySystemPolicyAc = POWER_INFORMATION_LEVEL.VerifySystemPolicyAc
        VerifySystemPolicyDc = POWER_INFORMATION_LEVEL.VerifySystemPolicyDc
        SystemPowerCapabilities = POWER_INFORMATION_LEVEL.SystemPowerCapabilities
        SystemBatteryState = POWER_INFORMATION_LEVEL.SystemBatteryState
        SystemPowerStateHandler = POWER_INFORMATION_LEVEL.SystemPowerStateHandler
        ProcessorStateHandler = POWER_INFORMATION_LEVEL.ProcessorStateHandler
        SystemPowerPolicyCurrent = POWER_INFORMATION_LEVEL.SystemPowerPolicyCurrent
        AdministratorPowerPolicy = POWER_INFORMATION_LEVEL.AdministratorPowerPolicy
        SystemReserveHiberFile = POWER_INFORMATION_LEVEL.SystemReserveHiberFile
        ProcessorInformation = POWER_INFORMATION_LEVEL.ProcessorInformation
        SystemPowerInformation = POWER_INFORMATION_LEVEL.SystemPowerInformation
        ProcessorStateHandler2 = POWER_INFORMATION_LEVEL.ProcessorStateHandler2
        LastWakeTime = POWER_INFORMATION_LEVEL.LastWakeTime
        LastSleepTime = POWER_INFORMATION_LEVEL.LastSleepTime
        SystemExecutionState = POWER_INFORMATION_LEVEL.SystemExecutionState
        SystemPowerStateNotifyHandler = POWER_INFORMATION_LEVEL.SystemPowerStateNotifyHandler
        ProcessorPowerPolicyAc = POWER_INFORMATION_LEVEL.ProcessorPowerPolicyAc
        ProcessorPowerPolicyDc = POWER_INFORMATION_LEVEL.ProcessorPowerPolicyDc
        VerifyProcessorPowerPolicyAc = POWER_INFORMATION_LEVEL.VerifyProcessorPowerPolicyAc
        VerifyProcessorPowerPolicyDc = POWER_INFORMATION_LEVEL.VerifyProcessorPowerPolicyDc
        ProcessorPowerPolicyCurrent = POWER_INFORMATION_LEVEL.ProcessorPowerPolicyCurrent
        SystemPowerStateLogging = POWER_INFORMATION_LEVEL.SystemPowerStateLogging
        SystemPowerLoggingEntry = POWER_INFORMATION_LEVEL.SystemPowerLoggingEntry
        SetPowerSettingValue = POWER_INFORMATION_LEVEL.SetPowerSettingValue
        NotifyUserPowerSetting = POWER_INFORMATION_LEVEL.NotifyUserPowerSetting
        PowerInformationLevelUnused0 = POWER_INFORMATION_LEVEL.PowerInformationLevelUnused0
        SystemMonitorHiberBootPowerOff = POWER_INFORMATION_LEVEL.SystemMonitorHiberBootPowerOff
        SystemVideoState = POWER_INFORMATION_LEVEL.SystemVideoState
        TraceApplicationPowerMessage = POWER_INFORMATION_LEVEL.TraceApplicationPowerMessage
        TraceApplicationPowerMessageEnd = POWER_INFORMATION_LEVEL.TraceApplicationPowerMessageEnd
        ProcessorPerfStates = POWER_INFORMATION_LEVEL.ProcessorPerfStates
        ProcessorIdleStates = POWER_INFORMATION_LEVEL.ProcessorIdleStates
        ProcessorCap = POWER_INFORMATION_LEVEL.ProcessorCap
        SystemWakeSource = POWER_INFORMATION_LEVEL.SystemWakeSource
        SystemHiberFileInformation = POWER_INFORMATION_LEVEL.SystemHiberFileInformation
        TraceServicePowerMessage = POWER_INFORMATION_LEVEL.TraceServicePowerMessage
        ProcessorLoad = POWER_INFORMATION_LEVEL.ProcessorLoad
        PowerShutdownNotification = POWER_INFORMATION_LEVEL.PowerShutdownNotification
        MonitorCapabilities = POWER_INFORMATION_LEVEL.MonitorCapabilities
        SessionPowerInit = POWER_INFORMATION_LEVEL.SessionPowerInit
        SessionDisplayState = POWER_INFORMATION_LEVEL.SessionDisplayState
        PowerRequestCreate = POWER_INFORMATION_LEVEL.PowerRequestCreate
        PowerRequestAction = POWER_INFORMATION_LEVEL.PowerRequestAction
        GetPowerRequestList = POWER_INFORMATION_LEVEL.GetPowerRequestList
        ProcessorInformationEx = POWER_INFORMATION_LEVEL.ProcessorInformationEx
        NotifyUserModeLegacyPowerEvent = POWER_INFORMATION_LEVEL.NotifyUserModeLegacyPowerEvent
        GroupPark = POWER_INFORMATION_LEVEL.GroupPark
        ProcessorIdleDomains = POWER_INFORMATION_LEVEL.ProcessorIdleDomains
        WakeTimerList = POWER_INFORMATION_LEVEL.WakeTimerList
        SystemHiberFileSize = POWER_INFORMATION_LEVEL.SystemHiberFileSize
        ProcessorIdleStatesHv = POWER_INFORMATION_LEVEL.ProcessorIdleStatesHv
        ProcessorPerfStatesHv = POWER_INFORMATION_LEVEL.ProcessorPerfStatesHv
        ProcessorPerfCapHv = POWER_INFORMATION_LEVEL.ProcessorPerfCapHv
        ProcessorSetIdle = POWER_INFORMATION_LEVEL.ProcessorSetIdle
        LogicalProcessorIdling = POWER_INFORMATION_LEVEL.LogicalProcessorIdling
        UserPresence = POWER_INFORMATION_LEVEL.UserPresence
        PowerSettingNotificationName = POWER_INFORMATION_LEVEL.PowerSettingNotificationName
        GetPowerSettingValue = POWER_INFORMATION_LEVEL.GetPowerSettingValue
        IdleResiliency = POWER_INFORMATION_LEVEL.IdleResiliency
        SessionRITState = POWER_INFORMATION_LEVEL.SessionRITState
        SessionConnectNotification = POWER_INFORMATION_LEVEL.SessionConnectNotification
        SessionPowerCleanup = POWER_INFORMATION_LEVEL.SessionPowerCleanup
        SessionLockState = POWER_INFORMATION_LEVEL.SessionLockState
        SystemHiberbootState = POWER_INFORMATION_LEVEL.SystemHiberbootState
        PlatformInformation = POWER_INFORMATION_LEVEL.PlatformInformation
        PdcInvocation = POWER_INFORMATION_LEVEL.PdcInvocation
        MonitorInvocation = POWER_INFORMATION_LEVEL.MonitorInvocation
        FirmwareTableInformationRegistered = POWER_INFORMATION_LEVEL.FirmwareTableInformationRegistered
        SetShutdownSelectedTime = POWER_INFORMATION_LEVEL.SetShutdownSelectedTime
        SuspendResumeInvocation = POWER_INFORMATION_LEVEL.SuspendResumeInvocation
        PlmPowerRequestCreate = POWER_INFORMATION_LEVEL.PlmPowerRequestCreate
        ScreenOff = POWER_INFORMATION_LEVEL.ScreenOff
        CsDeviceNotification = POWER_INFORMATION_LEVEL.CsDeviceNotification
        PlatformRole = POWER_INFORMATION_LEVEL.PlatformRole
        LastResumePerformance = POWER_INFORMATION_LEVEL.LastResumePerformance
        DisplayBurst = POWER_INFORMATION_LEVEL.DisplayBurst
        ExitLatencySamplingPercentage = POWER_INFORMATION_LEVEL.ExitLatencySamplingPercentage
        RegisterSpmPowerSettings = POWER_INFORMATION_LEVEL.RegisterSpmPowerSettings
        PlatformIdleStates = POWER_INFORMATION_LEVEL.PlatformIdleStates
        ProcessorIdleVeto = POWER_INFORMATION_LEVEL.ProcessorIdleVeto
        PlatformIdleVeto = POWER_INFORMATION_LEVEL.PlatformIdleVeto
        SystemBatteryStatePrecise = POWER_INFORMATION_LEVEL.SystemBatteryStatePrecise
        ThermalEvent = POWER_INFORMATION_LEVEL.ThermalEvent
        PowerRequestActionInternal = POWER_INFORMATION_LEVEL.PowerRequestActionInternal
        BatteryDeviceState = POWER_INFORMATION_LEVEL.BatteryDeviceState
        PowerInformationInternal = POWER_INFORMATION_LEVEL.PowerInformationInternal
        ThermalStandby = POWER_INFORMATION_LEVEL.ThermalStandby
        SystemHiberFileType = POWER_INFORMATION_LEVEL.SystemHiberFileType
        PhysicalPowerButtonPress = POWER_INFORMATION_LEVEL.PhysicalPowerButtonPress
        QueryPotentialDripsConstraint = POWER_INFORMATION_LEVEL.QueryPotentialDripsConstraint
        EnergyTrackerCreate = POWER_INFORMATION_LEVEL.EnergyTrackerCreate
        EnergyTrackerQuery = POWER_INFORMATION_LEVEL.EnergyTrackerQuery
        UpdateBlackBoxRecorder = POWER_INFORMATION_LEVEL.UpdateBlackBoxRecorder
        PowerInformationLevelMaximum = POWER_INFORMATION_LEVEL.PowerInformationLevelMaximum

        # User Presence Values
        class POWER_USER_PRESENCE_TYPE(ENUM):
            UserNotPresent = 0
            UserPresent = 1
            UserUnknown = 0xFF


        PPOWER_USER_PRESENCE_TYPE = POINTER(POWER_USER_PRESENCE_TYPE)
        UserNotPresent = POWER_USER_PRESENCE_TYPE.UserNotPresent
        UserPresent = POWER_USER_PRESENCE_TYPE.UserPresent
        UserUnknown = POWER_USER_PRESENCE_TYPE.UserUnknown
        class _POWER_USER_PRESENCE(ctypes.Structure):
            pass


        _POWER_USER_PRESENCE._fields_ = [
            ('UserPresence', POWER_USER_PRESENCE_TYPE),
        ]
        POWER_USER_PRESENCE = _POWER_USER_PRESENCE
        PPOWER_USER_PRESENCE = POINTER(_POWER_USER_PRESENCE)

        # Session Connect/Disconnect
        class _POWER_SESSION_CONNECT(ctypes.Structure):
            pass


        _POWER_SESSION_CONNECT._fields_ = [
            ('Connected', BOOLEAN), # TRUE - connected, FALSE - disconnected
            ('Console', BOOLEAN), # TRUE - console, FALSE - TS (not used for Connected = FALSE)
        ]
        POWER_SESSION_CONNECT = _POWER_SESSION_CONNECT
        PPOWER_SESSION_CONNECT = POINTER(_POWER_SESSION_CONNECT)
        class _POWER_SESSION_TIMEOUTS(ctypes.Structure):
            pass


        _POWER_SESSION_TIMEOUTS._fields_ = [
            ('InputTimeout', ULONG),
            ('DisplayTimeout', ULONG),
        ]
        POWER_SESSION_TIMEOUTS = _POWER_SESSION_TIMEOUTS
        PPOWER_SESSION_TIMEOUTS = POINTER(_POWER_SESSION_TIMEOUTS)

        # Session RIT State
        class _POWER_SESSION_RIT_STATE(ctypes.Structure):
            pass


        _POWER_SESSION_RIT_STATE._fields_ = [
            ('Active', BOOLEAN), # TRUE - RIT input received, FALSE - RIT timeout
            ('LastInputTime', ULONG), # last input time held for this session
        ]
        POWER_SESSION_RIT_STATE = _POWER_SESSION_RIT_STATE
        PPOWER_SESSION_RIT_STATE = POINTER(_POWER_SESSION_RIT_STATE)

        # Winlogon notifications
        class _POWER_SESSION_WINLOGON(ctypes.Structure):
            pass


        _POWER_SESSION_WINLOGON._fields_ = [
            ('SessionId', ULONG), # the Win32k session identifier
            ('Console', BOOLEAN), # TRUE - for console session, FALSE - for remote session
            ('Locked', BOOLEAN), # TRUE - lock, FALSE - unlock
        ]
        POWER_SESSION_WINLOGON = _POWER_SESSION_WINLOGON
        PPOWER_SESSION_WINLOGON = POINTER(_POWER_SESSION_WINLOGON)

        # Idle resiliency
        class _POWER_IDLE_RESILIENCY(ctypes.Structure):
            pass


        _POWER_IDLE_RESILIENCY._fields_ = [
            ('CoalescingTimeout', ULONG),
            ('IdleResiliencyPeriod', ULONG),
        ]
        POWER_IDLE_RESILIENCY = _POWER_IDLE_RESILIENCY
        PPOWER_IDLE_RESILIENCY = POINTER(_POWER_IDLE_RESILIENCY)

        # Monitor on/off reasons
        # N.B. Update power - event mapping when adding new events.
        class POWER_MONITOR_REQUEST_REASON(ENUM):
            MonitorRequestReasonUnknown = 1
            MonitorRequestReasonPowerButton = 2
            MonitorRequestReasonRemoteConnection = 3
            MonitorRequestReasonScMonitorpower = 4
            MonitorRequestReasonUserInput = 5
            MonitorRequestReasonAcDcDisplayBurst = 6
            MonitorRequestReasonUserDisplayBurst = 7
            MonitorRequestReasonPoSetSystemState = 8
            MonitorRequestReasonSetThreadExecutionState = 9
            MonitorRequestReasonFullWake = 10
            MonitorRequestReasonSessionUnlock = 11
            MonitorRequestReasonScreenOffRequest = 12
            MonitorRequestReasonIdleTimeout = 13
            MonitorRequestReasonPolicyChange = 14
            MonitorRequestReasonSleepButton = 15
            MonitorRequestReasonLid = 16
            MonitorRequestReasonBatteryCountChange = 17
            MonitorRequestReasonGracePeriod = 18
            MonitorRequestReasonPnP = 19
            MonitorRequestReasonDP = 20
            MonitorRequestReasonSxTransition = 21
            MonitorRequestReasonSystemIdle = 22
            MonitorRequestReasonNearProximity = 23
            MonitorRequestReasonThermalStandby = 24
            MonitorRequestReasonResumePdc = 25
            MonitorRequestReasonResumeS4 = 26
            MonitorRequestReasonTerminal = 27
            MonitorRequestReasonPdcSignal = 28
            MonitorRequestReasonAcDcDisplayBurstSuppressed = 29
            MonitorRequestReasonSystemStateEntered = 30
            MonitorRequestReasonWinrt = 31
            MonitorRequestReasonUserInputKeyboard = 32
            MonitorRequestReasonUserInputMouse = 33
            MonitorRequestReasonUserInputTouch = 34
            MonitorRequestReasonUserInputPen = 35
            MonitorRequestReasonUserInputAccelerometer = 36
            MonitorRequestReasonUserInputHid = 37
            MonitorRequestReasonUserInputPoUserPresent = 38
            MonitorRequestReasonUserInputSessionSwitch = 39
            MonitorRequestReasonUserInputInitialization = 40
            MonitorRequestReasonPdcSignalWindowsMobilePwrNotif = 41
            MonitorRequestReasonPdcSignalWindowsMobileShell = 42
            MonitorRequestReasonPdcSignalHeyCortana = 43
            MonitorRequestReasonPdcSignalHolographicShell = 44
            MonitorRequestReasonPdcSignalFingerprint = 45
            MonitorRequestReasonMax = 46


        MonitorRequestReasonUnknown = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUnknown
        MonitorRequestReasonPowerButton = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonPowerButton
        MonitorRequestReasonRemoteConnection = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonRemoteConnection
        MonitorRequestReasonScMonitorpower = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonScMonitorpower
        MonitorRequestReasonUserInput = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUserInput
        MonitorRequestReasonAcDcDisplayBurst = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonAcDcDisplayBurst
        MonitorRequestReasonUserDisplayBurst = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUserDisplayBurst
        MonitorRequestReasonPoSetSystemState = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonPoSetSystemState
        MonitorRequestReasonSetThreadExecutionState = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonSetThreadExecutionState
        MonitorRequestReasonFullWake = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonFullWake
        MonitorRequestReasonSessionUnlock = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonSessionUnlock
        MonitorRequestReasonScreenOffRequest = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonScreenOffRequest
        MonitorRequestReasonIdleTimeout = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonIdleTimeout
        MonitorRequestReasonPolicyChange = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonPolicyChange
        MonitorRequestReasonSleepButton = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonSleepButton
        MonitorRequestReasonLid = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonLid
        MonitorRequestReasonBatteryCountChange = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonBatteryCountChange
        MonitorRequestReasonGracePeriod = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonGracePeriod
        MonitorRequestReasonPnP = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonPnP
        MonitorRequestReasonDP = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonDP
        MonitorRequestReasonSxTransition = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonSxTransition
        MonitorRequestReasonSystemIdle = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonSystemIdle
        MonitorRequestReasonNearProximity = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonNearProximity
        MonitorRequestReasonThermalStandby = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonThermalStandby
        MonitorRequestReasonResumePdc = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonResumePdc
        MonitorRequestReasonResumeS4 = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonResumeS4
        MonitorRequestReasonTerminal = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonTerminal
        MonitorRequestReasonPdcSignal = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonPdcSignal
        MonitorRequestReasonAcDcDisplayBurstSuppressed = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonAcDcDisplayBurstSuppressed
        MonitorRequestReasonSystemStateEntered = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonSystemStateEntered
        MonitorRequestReasonWinrt = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonWinrt
        MonitorRequestReasonUserInputKeyboard = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUserInputKeyboard
        MonitorRequestReasonUserInputMouse = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUserInputMouse
        MonitorRequestReasonUserInputTouch = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUserInputTouch
        MonitorRequestReasonUserInputPen = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUserInputPen
        MonitorRequestReasonUserInputAccelerometer = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUserInputAccelerometer
        MonitorRequestReasonUserInputHid = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUserInputHid
        MonitorRequestReasonUserInputPoUserPresent = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUserInputPoUserPresent
        MonitorRequestReasonUserInputSessionSwitch = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUserInputSessionSwitch
        MonitorRequestReasonUserInputInitialization = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonUserInputInitialization
        MonitorRequestReasonPdcSignalWindowsMobilePwrNotif = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonPdcSignalWindowsMobilePwrNotif
        MonitorRequestReasonPdcSignalWindowsMobileShell = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonPdcSignalWindowsMobileShell
        MonitorRequestReasonPdcSignalHeyCortana = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonPdcSignalHeyCortana
        MonitorRequestReasonPdcSignalHolographicShell = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonPdcSignalHolographicShell
        MonitorRequestReasonPdcSignalFingerprint = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonPdcSignalFingerprint
        MonitorRequestReasonMax = POWER_MONITOR_REQUEST_REASON.MonitorRequestReasonMax
        class _POWER_MONITOR_REQUEST_TYPE(ENUM):
            MonitorRequestTypeOff = 1
            MonitorRequestTypeOnAndPresent = 2
            MonitorRequestTypeToggleOn = 3


        POWER_MONITOR_REQUEST_TYPE = _POWER_MONITOR_REQUEST_TYPE

        # Monitor invocation
        class _POWER_MONITOR_INVOCATION(ctypes.Structure):
            pass


        _POWER_MONITOR_INVOCATION._fields_ = [
            ('Console', BOOLEAN),
            ('RequestReason', POWER_MONITOR_REQUEST_REASON),
        ]
        POWER_MONITOR_INVOCATION = _POWER_MONITOR_INVOCATION
        PPOWER_MONITOR_INVOCATION = POINTER(_POWER_MONITOR_INVOCATION)

        # Last resume performance structure
        class _RESUME_PERFORMANCE(ctypes.Structure):
            pass


        _RESUME_PERFORMANCE._fields_ = [
            ('PostTimeMs', ULONG),
            ('TotalResumeTimeMs', ULONGLONG),
            ('ResumeCompleteTimestamp', ULONGLONG),
        ]
        RESUME_PERFORMANCE = _RESUME_PERFORMANCE
        PRESUME_PERFORMANCE = POINTER(_RESUME_PERFORMANCE)

        # Power Setting definitions
        class SYSTEM_POWER_CONDITION(ENUM):
            PoAc = 1
            PoDc = 2
            PoHot = 3
            PoConditionMaximum = 4


        PoAc = SYSTEM_POWER_CONDITION.PoAc
        PoDc = SYSTEM_POWER_CONDITION.PoDc
        PoHot = SYSTEM_POWER_CONDITION.PoHot
        PoConditionMaximum = SYSTEM_POWER_CONDITION.PoConditionMaximum
        class SET_POWER_SETTING_VALUE(ctypes.Structure):
            pass


        SET_POWER_SETTING_VALUE._fields_ = [
            ('Version', ULONG), # POWER_SETTING_VALUE_VERSION.
            ('Guid', GUID), # GUID representing the power setting being applied.
            ('PowerCondition', SYSTEM_POWER_CONDITION), # AC, DC, thermal, ...
            ('DataLength', ULONG), # Length (in bytes) of the 'Data' member.
            ('Data', UCHAR * ANYSIZE_ARRAY), # Data which contains the actual setting value.
        ]
        PSET_POWER_SETTING_VALUE = POINTER(SET_POWER_SETTING_VALUE)
        POWER_SETTING_VALUE_VERSION = 0x1
        class NOTIFY_USER_POWER_SETTING(ctypes.Structure):
            pass


        NOTIFY_USER_POWER_SETTING._fields_ = [
            ('Guid', GUID),
        ]
        PNOTIFY_USER_POWER_SETTING = POINTER(NOTIFY_USER_POWER_SETTING)

        # Package definition for an experience button device notification. When
        # someone registers for GUID_EXPERIENCE_BUTTON, this is the definition
        # of
        # the setting data they'll get.
        class _APPLICATIONLAUNCH_SETTING_VALUE(ctypes.Structure):
            pass


        _APPLICATIONLAUNCH_SETTING_VALUE._fields_ = [
            ('ActivationTime', LARGE_INTEGER), # specified in 100ns internvals since January 1, 1601.
            ('Flags', ULONG), # Reserved for internal use.
            ('ButtonInstanceID', ULONG), # which instance of this device was pressed?
        ]
        APPLICATIONLAUNCH_SETTING_VALUE = _APPLICATIONLAUNCH_SETTING_VALUE
        PAPPLICATIONLAUNCH_SETTING_VALUE = POINTER(_APPLICATIONLAUNCH_SETTING_VALUE)

        # define platform roles


        class _POWER_PLATFORM_ROLE(ENUM):
            PlatformRoleUnspecified = 0
            PlatformRoleDesktop = 1
            PlatformRoleMobile = 2
            PlatformRoleWorkstation = 3
            PlatformRoleEnterpriseServer = 4
            PlatformRoleSOHOServer = 5
            PlatformRoleAppliancePC = 6
            PlatformRolePerformanceServer = 7
            PlatformRoleSlate = 8
            PlatformRoleMaximum = 9


        POWER_PLATFORM_ROLE = _POWER_PLATFORM_ROLE
        PPOWER_PLATFORM_ROLE = POINTER(_POWER_PLATFORM_ROLE)
        POWER_PLATFORM_ROLE_V1 = 0x00000001
        POWER_PLATFORM_ROLE_V1_MAX = (PlatformRolePerformanceServer + 1)
        POWER_PLATFORM_ROLE_V2 = 0x00000002
        POWER_PLATFORM_ROLE_V2_MAX = (PlatformRoleSlate + 1)

        if NTDDI_VERSION >= NTDDI_WIN8:
            POWER_PLATFORM_ROLE_VERSION = POWER_PLATFORM_ROLE_V2
            POWER_PLATFORM_ROLE_VERSION_MAX = POWER_PLATFORM_ROLE_V2_MAX
        else:
            POWER_PLATFORM_ROLE_VERSION = POWER_PLATFORM_ROLE_V1
            POWER_PLATFORM_ROLE_VERSION_MAX = POWER_PLATFORM_ROLE_V1_MAX
        # END IF
        class _POWER_PLATFORM_INFORMATION(ctypes.Structure):
            pass


        _POWER_PLATFORM_INFORMATION._fields_ = [
            ('AoAc', BOOLEAN),
        ]
        POWER_PLATFORM_INFORMATION = _POWER_PLATFORM_INFORMATION
        PPOWER_PLATFORM_INFORMATION = POINTER(_POWER_PLATFORM_INFORMATION)

        # System power manager capabilities

        if NTDDI_VERSION >= NTDDI_WINXP) or not defined(_BATCLASS_:
            class BATTERY_REPORTING_SCALE(ctypes.Structure):
                pass


            BATTERY_REPORTING_SCALE._fields_ = [
                ('Granularity', ULONG),
                ('Capacity', ULONG),
            ]
            PBATTERY_REPORTING_SCALE = POINTER(BATTERY_REPORTING_SCALE)
        # END IF   (NTDDI_VERSION >= NTDDI_WINXP) or not defined(_BATCLASS_)    # END IF   not _PO_DDK_
    # Predefined Value Types.
    REG_NONE = 0ul
    REG_SZ = 1ul
    REG_EXPAND_SZ = 2ul

    # (with environment variable references)
    REG_BINARY = 3ul
    REG_DWORD = 4ul
    REG_DWORD_LITTLE_ENDIAN = 4ul
    REG_DWORD_BIG_ENDIAN = 5ul
    REG_LINK = 6ul
    REG_MULTI_SZ = 7ul
    REG_RESOURCE_LIST = 8ul
    REG_FULL_RESOURCE_DESCRIPTOR = 9ul
    REG_RESOURCE_REQUIREMENTS_LIST = 10ul
    REG_QWORD = 11ul
    REG_QWORD_LITTLE_ENDIAN = 11ul

    # Service Types (Bit Mask)
    SERVICE_KERNEL_DRIVER = 0x00000001
    SERVICE_FILE_SYSTEM_DRIVER = 0x00000002
    SERVICE_ADAPTER = 0x00000004
    SERVICE_RECOGNIZER_DRIVER = 0x00000008
    SERVICE_DRIVER = (
        SERVICE_KERNEL_DRIVER |
        SERVICE_FILE_SYSTEM_DRIVER |
        SERVICE_RECOGNIZER_DRIVER
    )
    SERVICE_WIN32_OWN_PROCESS = 0x00000010
    SERVICE_WIN32_SHARE_PROCESS = 0x00000020
    SERVICE_WIN32 = SERVICE_WIN32_OWN_PROCESS | SERVICE_WIN32_SHARE_PROCESS
    SERVICE_USER_SERVICE = 0x00000040
    SERVICE_USERSERVICE_INSTANCE = 0x00000080
    SERVICE_USER_SHARE_PROCESS = (
        SERVICE_USER_SERVICE |
        SERVICE_WIN32_SHARE_PROCESS
    )
    SERVICE_USER_OWN_PROCESS = SERVICE_USER_SERVICE | SERVICE_WIN32_OWN_PROCESS
    SERVICE_INTERACTIVE_PROCESS = 0x00000100
    SERVICE_PKG_SERVICE = 0x00000200
    SERVICE_TYPE_ALL = (
        SERVICE_WIN32 |
        SERVICE_ADAPTER |
        SERVICE_DRIVER |
        SERVICE_INTERACTIVE_PROCESS |
        SERVICE_USER_SERVICE |
        SERVICE_USERSERVICE_INSTANCE |
        SERVICE_PKG_SERVICE
    )

    # Start Type
    SERVICE_BOOT_START = 0x00000000
    SERVICE_SYSTEM_START = 0x00000001
    SERVICE_AUTO_START = 0x00000002
    SERVICE_DEMAND_START = 0x00000003
    SERVICE_DISABLED = 0x00000004

    # Error control type
    SERVICE_ERROR_IGNORE = 0x00000000
    SERVICE_ERROR_NORMAL = 0x00000001
    SERVICE_ERROR_SEVERE = 0x00000002
    SERVICE_ERROR_CRITICAL = 0x00000003

    # Define the registry driver node enumerations


    class _CM_SERVICE_NODE_TYPE(ENUM):
        #~#~#~ DriverType               = SERVICE_KERNEL_DRIVER        #~#~#~ FileSystemType           = SERVICE_FILE_SYSTEM_DRIVER        #~#~#~ Win32ServiceOwnProcess   = SERVICE_WIN32_OWN_PROCESS        #~#~#~ Win32ServiceShareProcess = SERVICE_WIN32_SHARE_PROCESS        #~#~#~ AdapterType              = SERVICE_ADAPTER        #~#~#~ RecognizerType           = SERVICE_RECOGNIZER_DRIVER
        pass


    SERVICE_NODE_TYPE = _CM_SERVICE_NODE_TYPE
    class _CM_SERVICE_LOAD_TYPE(ENUM):
        #~#~#~ BootLoad    = SERVICE_BOOT_START        #~#~#~ SystemLoad  = SERVICE_SYSTEM_START        #~#~#~ AutoLoad    = SERVICE_AUTO_START        #~#~#~ DemandLoad  = SERVICE_DEMAND_START        #~#~#~ DisableLoad = SERVICE_DISABLED
        pass


    SERVICE_LOAD_TYPE = _CM_SERVICE_LOAD_TYPE
    class _CM_ERROR_CONTROL_TYPE(ENUM):
        #~#~#~ IgnoreError   = SERVICE_ERROR_IGNORE        #~#~#~ NormalError   = SERVICE_ERROR_NORMAL        #~#~#~ SevereError   = SERVICE_ERROR_SEVERE        #~#~#~ CriticalError = SERVICE_ERROR_CRITICAL
        pass


    SERVICE_ERROR_TYPE = _CM_ERROR_CONTROL_TYPE

    # Service node Flags. These flags are used by the OS loader to promote
    # a driver's start type to boot start if the system is booting using
    # the specified mechanism. The flags should be set in the driver's
    # registry configuration.
    # CM_SERVICE_NETWORK_BOOT_LOAD - Specified if a driver should be
    # promoted on network boot.
    # CM_SERVICE_VIRTUAL_DISK_BOOT_LOAD - Specified if a driver should be
    # promoted on booting from a VHD.
    # CM_SERVICE_USB_DISK_BOOT_LOAD - Specified if a driver should be promoted
    # while booting from a USB disk.
    # CM_SERVICE_SD_DISK_BOOT_LOAD - Specified if a driver should be promoted
    # while booting from SD storage.
    # CM_SERVICE_USB3_DISK_BOOT_LOAD - Specified if a driver should be promoted
    # while booting from a disk on a USB3 controller.
    # CM_SERVICE_MEASURED_BOOT_LOAD - Specified if a driver should be promoted
    # while booting with measured boot enabled.
    # CM_SERVICE_VERIFIER_BOOT_LOAD - Specified if a driver should be promoted
    # while booting with verifier boot enabled.
    # CM_SERVICE_WINPE_BOOT_LOAD - Specified if a driver should be promoted
    # on WinPE boot.
    CM_SERVICE_NETWORK_BOOT_LOAD = 0x00000001
    CM_SERVICE_VIRTUAL_DISK_BOOT_LOAD = 0x00000002
    CM_SERVICE_USB_DISK_BOOT_LOAD = 0x00000004
    CM_SERVICE_SD_DISK_BOOT_LOAD = 0x00000008
    CM_SERVICE_USB3_DISK_BOOT_LOAD = 0x00000010
    CM_SERVICE_MEASURED_BOOT_LOAD = 0x00000020
    CM_SERVICE_VERIFIER_BOOT_LOAD = 0x00000040
    CM_SERVICE_WINPE_BOOT_LOAD = 0x00000080

    # Mask defining the legal promotion flag values.
    CM_SERVICE_VALID_PROMOTION_MASK = (
        CM_SERVICE_NETWORK_BOOT_LOAD |
        CM_SERVICE_VIRTUAL_DISK_BOOT_LOAD |
        CM_SERVICE_USB_DISK_BOOT_LOAD |
        CM_SERVICE_SD_DISK_BOOT_LOAD |
        CM_SERVICE_USB3_DISK_BOOT_LOAD |
        CM_SERVICE_MEASURED_BOOT_LOAD |
        CM_SERVICE_VERIFIER_BOOT_LOAD |
        CM_SERVICE_WINPE_BOOT_LOAD
    )

    # Resource List definitions
    # Defines the Type in the RESOURCE_DESCRIPTOR
    # NOTE: For all CM_RESOURCE_TYPE values, there must be a
    # corresponding ResType value in the 32 - bit ConfigMgr headerfile
    # (cfgmgr32.h). Values in the range [0x6,0x80) use the same values
    # as their ConfigMgr counterparts. CM_RESOURCE_TYPE values with
    # the high bit set (i.e., in the range [0x80,0xFF]), are
    # non - arbitrated resources. These correspond to the same values
    # in cfgmgr32.h that have their high bit set (however, since
    # cfgmgr32.h uses 16 bits for ResType values, these values are in
    # the range [0x8000,0x807F). Note that ConfigMgr ResType values
    # cannot be in the range [0x8080,0xFFFF), because they would not
    # be able to map into CM_RESOURCE_TYPE values. (0xFFFF itself is
    # a special value, because it maps to CmResourceTypeDeviceSpecific.)
    CM_RESOURCE_TYPE = INT

    # CmResourceTypeNull is reserved
    CmResourceTypeNull = 0
    CmResourceTypePort = 1
    CmResourceTypeInterrupt = 2
    CmResourceTypeMemory = 3
    CmResourceTypeDma = 4
    CmResourceTypeDeviceSpecific = 5
    CmResourceTypeBusNumber = 6
    CmResourceTypeMemoryLarge = 7
    CmResourceTypeNonArbitrated = 128
    CmResourceTypeConfigData = 128
    CmResourceTypeDevicePrivate = 129
    CmResourceTypePcCardConfig = 130
    CmResourceTypeMfCardConfig = 131
    CmResourceTypeConnection = 132

    # Defines the ShareDisposition in the RESOURCE_DESCRIPTOR


    class _CM_SHARE_DISPOSITION(ENUM):
        CmResourceShareUndetermined = 0
        CmResourceShareDeviceExclusive = 1
        CmResourceShareDriverExclusive = 2
        CmResourceShareShared = 3


    CM_SHARE_DISPOSITION = _CM_SHARE_DISPOSITION

    # Define the bit masks for Flags when type is CmResourceTypeInterrupt
    CM_RESOURCE_INTERRUPT_LEVEL_SENSITIVE = 0x00
    CM_RESOURCE_INTERRUPT_LATCHED = 0x01
    CM_RESOURCE_INTERRUPT_MESSAGE = 0x02
    CM_RESOURCE_INTERRUPT_POLICY_INCLUDED = 0x04
    CM_RESOURCE_INTERRUPT_SECONDARY_INTERRUPT = 0x10
    CM_RESOURCE_INTERRUPT_WAKE_HINT = 0x20

    # A bitmask defining the bits in a resource or requirements descriptor
    # flags field that corresponds to the latch mode or a level triggered
    # interrupt.
    CM_RESOURCE_INTERRUPT_LEVEL_LATCHED_BITS = 0x0001

    # Define the token value used for an interrupt vector to mean that the
    # vector
    # is message signaled. This value is used in the MaximumVector field.
    CM_RESOURCE_INTERRUPT_MESSAGE_TOKEN = (ULONG) - 2

    # Define the bit masks for Flags when type is CmResourceTypeMemory
    # or CmResourceTypeMemoryLarge
    CM_RESOURCE_MEMORY_READ_WRITE = 0x0000
    CM_RESOURCE_MEMORY_READ_ONLY = 0x0001
    CM_RESOURCE_MEMORY_WRITE_ONLY = 0x0002
    CM_RESOURCE_MEMORY_WRITEABILITY_MASK = 0x0003
    CM_RESOURCE_MEMORY_PREFETCHABLE = 0x0004
    CM_RESOURCE_MEMORY_COMBINEDWRITE = 0x0008
    CM_RESOURCE_MEMORY_24 = 0x0010
    CM_RESOURCE_MEMORY_CACHEABLE = 0x0020
    CM_RESOURCE_MEMORY_WINDOW_DECODE = 0x0040
    CM_RESOURCE_MEMORY_BAR = 0x0080
    CM_RESOURCE_MEMORY_COMPAT_FOR_INACCESSIBLE_RANGE = 0x0100

    # Define the bit masks exclusive to type CmResourceTypeMemoryLarge.
    CM_RESOURCE_MEMORY_LARGE = 0x0E00
    CM_RESOURCE_MEMORY_LARGE_40 = 0x0200
    CM_RESOURCE_MEMORY_LARGE_48 = 0x0400
    CM_RESOURCE_MEMORY_LARGE_64 = 0x0800

    # Define limits for large memory resources
    CM_RESOURCE_MEMORY_LARGE_40_MAXLEN = 0x000000FFFFFFFF00
    CM_RESOURCE_MEMORY_LARGE_48_MAXLEN = 0x0000FFFFFFFF0000
    CM_RESOURCE_MEMORY_LARGE_64_MAXLEN = 0xFFFFFFFF00000000

    # Define the bit masks for Flags when type is CmResourceTypePort
    CM_RESOURCE_PORT_MEMORY = 0x0000
    CM_RESOURCE_PORT_IO = 0x0001
    CM_RESOURCE_PORT_10_BIT_DECODE = 0x0004
    CM_RESOURCE_PORT_12_BIT_DECODE = 0x0008
    CM_RESOURCE_PORT_16_BIT_DECODE = 0x0010
    CM_RESOURCE_PORT_POSITIVE_DECODE = 0x0020
    CM_RESOURCE_PORT_PASSIVE_DECODE = 0x0040
    CM_RESOURCE_PORT_WINDOW_DECODE = 0x0080
    CM_RESOURCE_PORT_BAR = 0x0100

    # Define the bit masks for Flags when type is CmResourceTypeDma
    CM_RESOURCE_DMA_8 = 0x0000
    CM_RESOURCE_DMA_16 = 0x0001
    CM_RESOURCE_DMA_32 = 0x0002
    CM_RESOURCE_DMA_8_AND_16 = 0x0004
    CM_RESOURCE_DMA_BUS_MASTER = 0x0008
    CM_RESOURCE_DMA_TYPE_A = 0x0010
    CM_RESOURCE_DMA_TYPE_B = 0x0020
    CM_RESOURCE_DMA_TYPE_F = 0x0040
    CM_RESOURCE_DMA_V3 = 0x0080

    # Define the different types of DMA transfer width values.
    DMAV3_TRANFER_WIDTH_8 = 0x00
    DMAV3_TRANFER_WIDTH_16 = 0x01
    DMAV3_TRANFER_WIDTH_32 = 0x02
    DMAV3_TRANFER_WIDTH_64 = 0x03
    DMAV3_TRANFER_WIDTH_128 = 0x04
    DMAV3_TRANFER_WIDTH_256 = 0x05

    # Define the Class and Type values for CmResourceTypeConnection
    CM_RESOURCE_CONNECTION_CLASS_GPIO = 0x01
    CM_RESOURCE_CONNECTION_CLASS_SERIAL = 0x02
    CM_RESOURCE_CONNECTION_CLASS_FUNCTION_CONFIG = 0x03
    CM_RESOURCE_CONNECTION_TYPE_GPIO_IO = 0x02
    CM_RESOURCE_CONNECTION_TYPE_SERIAL_I2C = 0x01
    CM_RESOURCE_CONNECTION_TYPE_SERIAL_SPI = 0x02
    CM_RESOURCE_CONNECTION_TYPE_SERIAL_UART = 0x03
    CM_RESOURCE_CONNECTION_TYPE_FUNCTION_CONFIG = 0x01

    # This structure defines one type of resource used by a driver.
    # There can only be *1* DeviceSpecificData block. It must be located at
    # the end of all resource descriptors in a full descriptor block.
    # Make sure alignment is made properly by compiler; otherwise move
    # flags back to the top of the structure (common to all members of the
    # union).
    class _CM_PARTIAL_RESOURCE_DESCRIPTOR(ctypes.Structure):
        pass


    class u(ctypes.Structure):
        pass


    class Generic(ctypes.Structure):
        pass


    Generic._fields_ = [
        ('Start', PHYSICAL_ADDRESS),
        ('Length', ULONG),
    ]
    u.Generic = Generic
    class Port(ctypes.Structure):
        pass


    Port._fields_ = [
        ('Start', PHYSICAL_ADDRESS),
        ('Length', ULONG),
    ]
    u.Port = Port
    class Interrupt(ctypes.Structure):
        pass


    Interrupt._fields_ = [
            ('Level', USHORT),
            ('Group', USHORT),
            ('Level', ULONG),
        ('Vector', ULONG),
        ('Affinity', KAFFINITY),
    ]
    u.Interrupt = Interrupt
    class MessageInterrupt(ctypes.Structure):
        pass


    class DUMMYUNIONNAME(ctypes.Structure):
        pass


    class Raw(ctypes.Structure):
        pass


    Raw._fields_ = [
            ('Group', USHORT),
            ('Reserved', USHORT),
        ('MessageCount', USHORT),
        ('Vector', ULONG),
        ('Affinity', KAFFINITY),
    ]
    DUMMYUNIONNAME.Raw = Raw
    class Translated(ctypes.Structure):
        pass


    Translated._fields_ = [
            ('Level', USHORT),
            ('Group', USHORT),
            ('Level', ULONG),
        ('Vector', ULONG),
        ('Affinity', KAFFINITY),
    ]
    DUMMYUNIONNAME.Translated = Translated
    DUMMYUNIONNAME._fields_ = [
        ('Raw', DUMMYUNIONNAME.Raw),
        ('Translated', DUMMYUNIONNAME.Translated),
    ]
    MessageInterrupt.DUMMYUNIONNAME = DUMMYUNIONNAME
    MessageInterrupt._fields_ = [
        ('DUMMYUNIONNAME', MessageInterrupt.DUMMYUNIONNAME),
    ]
    u.MessageInterrupt = MessageInterrupt
    class Memory(ctypes.Structure):
        pass


    Memory._fields_ = [
        ('Start', PHYSICAL_ADDRESS), # 64 bit physical addresses.
        ('Length', ULONG),
    ]
    u.Memory = Memory
    class Dma(ctypes.Structure):
        pass


    Dma._fields_ = [
        ('Channel', ULONG),
        ('Port', ULONG),
        ('Reserved1', ULONG),
    ]
    u.Dma = Dma
    class DmaV3(ctypes.Structure):
        pass


    DmaV3._fields_ = [
        ('Channel', ULONG),
        ('RequestLine', ULONG),
        ('TransferWidth', UCHAR),
        ('Reserved1', UCHAR),
        ('Reserved2', UCHAR),
        ('Reserved3', UCHAR),
    ]
    u.DmaV3 = DmaV3
    class DevicePrivate(ctypes.Structure):
        pass


    DevicePrivate._fields_ = [
        ('Data', ULONG * 3),
    ]
    u.DevicePrivate = DevicePrivate
    class BusNumber(ctypes.Structure):
        pass


    BusNumber._fields_ = [
        ('Start', ULONG),
        ('Length', ULONG),
        ('Reserved', ULONG),
    ]
    u.BusNumber = BusNumber
    class DeviceSpecificData(ctypes.Structure):
        pass


    DeviceSpecificData._fields_ = [
        ('DataSize', ULONG),
        ('Reserved1', ULONG),
        ('Reserved2', ULONG),
    ]
    u.DeviceSpecificData = DeviceSpecificData
    class Memory40(ctypes.Structure):
        pass


    Memory40._fields_ = [
        ('Start', PHYSICAL_ADDRESS),
        ('Length40', ULONG),
    ]
    u.Memory40 = Memory40
    class Memory48(ctypes.Structure):
        pass


    Memory48._fields_ = [
        ('Start', PHYSICAL_ADDRESS),
        ('Length48', ULONG),
    ]
    u.Memory48 = Memory48
    class Memory64(ctypes.Structure):
        pass


    Memory64._fields_ = [
        ('Start', PHYSICAL_ADDRESS),
        ('Length64', ULONG),
    ]
    u.Memory64 = Memory64
    class Connection(ctypes.Structure):
        pass


    Connection._fields_ = [
        ('Class', UCHAR),
        ('Type', UCHAR),
        ('Reserved1', UCHAR),
        ('Reserved2', UCHAR),
        ('IdLowPart', ULONG),
        ('IdHighPart', ULONG),
    ]
    u.Connection = Connection
    u._fields_ = [
        ('Generic', u.Generic), # as Generic.
        ('Port', u.Port),
        ('Interrupt', u.Interrupt),
        ('MessageInterrupt', u.MessageInterrupt), # raw and translated cases.
        ('Memory', u.Memory), # HalTranslateBusAddress().
        ('Dma', u.Dma), # Physical DMA channel.
        ('DmaV3', u.DmaV3),
        ('DevicePrivate', u.DevicePrivate), # what the resource assignments decisions that were made.
        ('BusNumber', u.BusNumber), # Bus Number information.
        ('DeviceSpecificData', u.DeviceSpecificData), # the structure.
        ('Memory40', u.Memory40), # IO resources greater than MAXULONG
        ('Memory48', u.Memory48),
        ('Memory64', u.Memory64),
        ('Connection', u.Connection),
    ]
    _CM_PARTIAL_RESOURCE_DESCRIPTOR.u = u
    _CM_PARTIAL_RESOURCE_DESCRIPTOR._fields_ = [
        ('Type', UCHAR),
        ('ShareDisposition', UCHAR),
        ('Flags', USHORT),
        ('u', _CM_PARTIAL_RESOURCE_DESCRIPTOR.u),
    ]
    CM_PARTIAL_RESOURCE_DESCRIPTOR = _CM_PARTIAL_RESOURCE_DESCRIPTOR
    PCM_PARTIAL_RESOURCE_DESCRIPTOR = POINTER(_CM_PARTIAL_RESOURCE_DESCRIPTOR)

    if defined(NT_PROCESSOR_GROUPS):
        pass
    else:
        pass
    # END IF
    if defined(NT_PROCESSOR_GROUPS):
        pass
    else:
        pass
    # END IF
    if defined(NT_PROCESSOR_GROUPS):
        pass
    else:
        pass
    # END IF
    # A Partial Resource List is what can be found in the ARC firmware
    # or will be generated by ntdetect.com.
    # The configuration manager will transform this structure into a Full
    # resource descriptor when it is about to store it in the regsitry.
    # Note: There must a be a convention to the order of fields of same type,
    # (defined on a device by device basis) so that the fields can make sense
    # to a driver (i.e. when multiple memory ranges are necessary).
    class _CM_PARTIAL_RESOURCE_LIST(ctypes.Structure):
        pass


    _CM_PARTIAL_RESOURCE_LIST._fields_ = [
        ('Version', USHORT),
        ('Revision', USHORT),
        ('Count', ULONG),
        ('PartialDescriptors', CM_PARTIAL_RESOURCE_DESCRIPTOR * 1),
    ]
    CM_PARTIAL_RESOURCE_LIST = _CM_PARTIAL_RESOURCE_LIST
    PCM_PARTIAL_RESOURCE_LIST = POINTER(_CM_PARTIAL_RESOURCE_LIST)

    # A Full Resource Descriptor is what can be found in the registry.
    # This is what will be returned to a driver when it queries the registry
    # to get device information; it will be stored under a key in the hardware
    # description tree.
    # Note: There must a be a convention to the order of fields of same type,
    # (defined on a device by device basis) so that the fields can make sense
    # to a driver (i.e. when multiple memory ranges are necessary).
    class _CM_FULL_RESOURCE_DESCRIPTOR(ctypes.Structure):
        pass


    _CM_FULL_RESOURCE_DESCRIPTOR._fields_ = [
        ('InterfaceType', INTERFACE_TYPE), # unused for WDM
        ('BusNumber', ULONG), # unused for WDM
        ('PartialResourceList', CM_PARTIAL_RESOURCE_LIST),
    ]
    CM_FULL_RESOURCE_DESCRIPTOR = _CM_FULL_RESOURCE_DESCRIPTOR
    PCM_FULL_RESOURCE_DESCRIPTOR = POINTER(_CM_FULL_RESOURCE_DESCRIPTOR)

    # The Resource list is what will be stored by the drivers into the
    # resource map via the IO API.
    class _CM_RESOURCE_LIST(ctypes.Structure):
        pass


    _CM_RESOURCE_LIST._fields_ = [
        ('Count', ULONG),
        ('List', CM_FULL_RESOURCE_DESCRIPTOR * 1),
    ]
    CM_RESOURCE_LIST = _CM_RESOURCE_LIST
    PCM_RESOURCE_LIST = POINTER(_CM_RESOURCE_LIST)

    # Define the structures used to interpret configuration data of
    # \\Registry\machine\hardware\description tree.
    # Basically, these structures are used to interpret component
    # sepcific data.
    # Define DEVICE_FLAGS
    class _DEVICE_FLAGS(ctypes.Structure):
        pass


    _DEVICE_FLAGS._fields_ = [
        ('Failed', ULONG, 1),
        ('ReadOnly', ULONG, 1),
        ('Removable', ULONG, 1),
        ('ConsoleIn', ULONG, 1),
        ('ConsoleOut', ULONG, 1),
        ('Input', ULONG, 1),
        ('Output', ULONG, 1),
    ]
    DEVICE_FLAGS = _DEVICE_FLAGS
    PDEVICE_FLAGS = POINTER(_DEVICE_FLAGS)

    # Define Component Information structure
    class _CM_COMPONENT_INFORMATION(ctypes.Structure):
        pass


    _CM_COMPONENT_INFORMATION._fields_ = [
        ('Flags', DEVICE_FLAGS),
        ('Version', ULONG),
        ('Key', ULONG),
        ('AffinityMask', KAFFINITY),
    ]
    CM_COMPONENT_INFORMATION = _CM_COMPONENT_INFORMATION
    PCM_COMPONENT_INFORMATION = POINTER(_CM_COMPONENT_INFORMATION)

    # The following structures are used to interpret x86
    # DeviceSpecificData of CM_PARTIAL_RESOURCE_DESCRIPTOR.
    # (Most of the structures are defined by BIOS. They are
    # not aligned on word (or dword) boundary.
    # Define the Rom Block structure
    class _CM_ROM_BLOCK(ctypes.Structure):
        pass


    _CM_ROM_BLOCK._fields_ = [
        ('Address', ULONG),
        ('Size', ULONG),
    ]
    CM_ROM_BLOCK = _CM_ROM_BLOCK
    PCM_ROM_BLOCK = POINTER(_CM_ROM_BLOCK)

    # Define INT13 driver parameter block
    class _CM_INT13_DRIVE_PARAMETER(ctypes.Structure):
        pass


    _CM_INT13_DRIVE_PARAMETER._fields_ = [
        ('DriveSelect', USHORT),
        ('MaxCylinders', ULONG),
        ('SectorsPerTrack', USHORT),
        ('MaxHeads', USHORT),
        ('NumberDrives', USHORT),
    ]
    CM_INT13_DRIVE_PARAMETER = _CM_INT13_DRIVE_PARAMETER
    PCM_INT13_DRIVE_PARAMETER = POINTER(_CM_INT13_DRIVE_PARAMETER)

    # Define Mca POS data block for slot
    class _CM_MCA_POS_DATA(ctypes.Structure):
        pass


    _CM_MCA_POS_DATA._fields_ = [
        ('AdapterId', USHORT),
        ('PosData1', UCHAR),
        ('PosData2', UCHAR),
        ('PosData3', UCHAR),
        ('PosData4', UCHAR),
    ]
    CM_MCA_POS_DATA = _CM_MCA_POS_DATA
    PCM_MCA_POS_DATA = POINTER(_CM_MCA_POS_DATA)

    # Memory configuration of eisa data block structure
    class _EISA_MEMORY_TYPE(ctypes.Structure):
        pass


    _EISA_MEMORY_TYPE._fields_ = [
        ('ReadWrite', UCHAR, 1),
        ('Cached', UCHAR, 1),
        ('Reserved0', UCHAR, 1),
        ('Type', UCHAR, 2),
        ('Shared', UCHAR, 1),
        ('Reserved1', UCHAR, 1),
        ('MoreEntries', UCHAR, 1),
    ]
    EISA_MEMORY_TYPE = _EISA_MEMORY_TYPE
    PEISA_MEMORY_TYPE = POINTER(_EISA_MEMORY_TYPE)
    class _EISA_MEMORY_CONFIGURATION(ctypes.Structure):
        pass


    _EISA_MEMORY_CONFIGURATION._fields_ = [
        ('ConfigurationByte', EISA_MEMORY_TYPE),
        ('DataSize', UCHAR),
        ('AddressLowWord', USHORT),
        ('AddressHighByte', UCHAR),
        ('MemorySize', USHORT),
    ]
    EISA_MEMORY_CONFIGURATION = _EISA_MEMORY_CONFIGURATION
    PEISA_MEMORY_CONFIGURATION = POINTER(_EISA_MEMORY_CONFIGURATION)

    # Interrupt configurationn of eisa data block structure
    class _EISA_IRQ_DESCRIPTOR(ctypes.Structure):
        pass


    _EISA_IRQ_DESCRIPTOR._fields_ = [
        ('Interrupt', UCHAR, 4),
        ('Reserved', UCHAR, 1),
        ('LevelTriggered', UCHAR, 1),
        ('Shared', UCHAR, 1),
        ('MoreEntries', UCHAR, 1),
    ]
    EISA_IRQ_DESCRIPTOR = _EISA_IRQ_DESCRIPTOR
    PEISA_IRQ_DESCRIPTOR = POINTER(_EISA_IRQ_DESCRIPTOR)
    class _EISA_IRQ_CONFIGURATION(ctypes.Structure):
        pass


    _EISA_IRQ_CONFIGURATION._fields_ = [
        ('ConfigurationByte', EISA_IRQ_DESCRIPTOR),
        ('Reserved', UCHAR),
    ]
    EISA_IRQ_CONFIGURATION = _EISA_IRQ_CONFIGURATION
    PEISA_IRQ_CONFIGURATION = POINTER(_EISA_IRQ_CONFIGURATION)

    # DMA description of eisa data block structure
    class _DMA_CONFIGURATION_BYTE0(ctypes.Structure):
        pass


    _DMA_CONFIGURATION_BYTE0._fields_ = [
        ('Channel', UCHAR, 3),
        ('Reserved', UCHAR, 3),
        ('Shared', UCHAR, 1),
        ('MoreEntries', UCHAR, 1),
    ]
    DMA_CONFIGURATION_BYTE0 = _DMA_CONFIGURATION_BYTE0
    class _DMA_CONFIGURATION_BYTE1(ctypes.Structure):
        pass


    _DMA_CONFIGURATION_BYTE1._fields_ = [
        ('Reserved0', UCHAR, 2),
        ('TransferSize', UCHAR, 2),
        ('Timing', UCHAR, 2),
        ('Reserved1', UCHAR, 2),
    ]
    DMA_CONFIGURATION_BYTE1 = _DMA_CONFIGURATION_BYTE1
    class _EISA_DMA_CONFIGURATION(ctypes.Structure):
        pass


    _EISA_DMA_CONFIGURATION._fields_ = [
        ('ConfigurationByte0', DMA_CONFIGURATION_BYTE0),
        ('ConfigurationByte1', DMA_CONFIGURATION_BYTE1),
    ]
    EISA_DMA_CONFIGURATION = _EISA_DMA_CONFIGURATION
    PEISA_DMA_CONFIGURATION = POINTER(_EISA_DMA_CONFIGURATION)

    # Port description of eisa data block structure
    class _EISA_PORT_DESCRIPTOR(ctypes.Structure):
        pass


    _EISA_PORT_DESCRIPTOR._fields_ = [
        ('NumberPorts', UCHAR, 5),
        ('Reserved', UCHAR, 1),
        ('Shared', UCHAR, 1),
        ('MoreEntries', UCHAR, 1),
    ]
    EISA_PORT_DESCRIPTOR = _EISA_PORT_DESCRIPTOR
    PEISA_PORT_DESCRIPTOR = POINTER(_EISA_PORT_DESCRIPTOR)
    class _EISA_PORT_CONFIGURATION(ctypes.Structure):
        pass


    _EISA_PORT_CONFIGURATION._fields_ = [
        ('Configuration', EISA_PORT_DESCRIPTOR),
        ('PortAddress', USHORT),
    ]
    EISA_PORT_CONFIGURATION = _EISA_PORT_CONFIGURATION
    PEISA_PORT_CONFIGURATION = POINTER(_EISA_PORT_CONFIGURATION)

    # Eisa slot information definition
    # N.B. This structure is different from the one defined
    # in ARC eisa addendum.
    class _CM_EISA_SLOT_INFORMATION(ctypes.Structure):
        pass


    _CM_EISA_SLOT_INFORMATION._fields_ = [
        ('ReturnCode', UCHAR),
        ('ReturnFlags', UCHAR),
        ('MajorRevision', UCHAR),
        ('MinorRevision', UCHAR),
        ('Checksum', USHORT),
        ('NumberFunctions', UCHAR),
        ('FunctionInformation', UCHAR),
        ('CompressedId', ULONG),
    ]
    CM_EISA_SLOT_INFORMATION = _CM_EISA_SLOT_INFORMATION
    PCM_EISA_SLOT_INFORMATION = POINTER(_CM_EISA_SLOT_INFORMATION)

    # Eisa function information definition
    class _CM_EISA_FUNCTION_INFORMATION(ctypes.Structure):
        pass


    _CM_EISA_FUNCTION_INFORMATION._fields_ = [
        ('CompressedId', ULONG),
        ('IdSlotFlags1', UCHAR),
        ('IdSlotFlags2', UCHAR),
        ('MinorRevision', UCHAR),
        ('MajorRevision', UCHAR),
        ('Selections', UCHAR * 26),
        ('FunctionFlags', UCHAR),
        ('TypeString', UCHAR * 80),
        ('EisaMemory', EISA_MEMORY_CONFIGURATION * 9),
        ('EisaIrq', EISA_IRQ_CONFIGURATION * 7),
        ('EisaDma', EISA_DMA_CONFIGURATION * 4),
        ('EisaPort', EISA_PORT_CONFIGURATION * 20),
        ('InitializationData', UCHAR * 60),
    ]
    CM_EISA_FUNCTION_INFORMATION = _CM_EISA_FUNCTION_INFORMATION
    PCM_EISA_FUNCTION_INFORMATION = POINTER(_CM_EISA_FUNCTION_INFORMATION)

    # The following defines the way pnp bios information is stored in
    # the registry
    # \\HKEY_LOCAL_MACHINE\HARDWARE\Description\System\MultifunctionAdapter\x
    # key, where x is an integer number indicating adapter instance. The
    # "Identifier" of the key must equal to "PNP BIOS" and the
    # "ConfigurationData" is organized as follow:
    # CM_PNP_BIOS_INSTALLATION_CHECK  +
    # CM_PNP_BIOS_DEVICE_NODE for device 1 +
    # CM_PNP_BIOS_DEVICE_NODE for device 2 +
    # ...
    # CM_PNP_BIOS_DEVICE_NODE for device n
    # Pnp BIOS device node structure
    class _CM_PNP_BIOS_DEVICE_NODE(ctypes.Structure):
        pass


    _CM_PNP_BIOS_DEVICE_NODE._fields_ = [
        ('Size', USHORT),
        ('Node', UCHAR),
        ('ProductId', ULONG),
        ('DeviceType', UCHAR * 3),
        ('DeviceAttributes', USHORT),
    ]
    CM_PNP_BIOS_DEVICE_NODE = _CM_PNP_BIOS_DEVICE_NODE
    PCM_PNP_BIOS_DEVICE_NODE = POINTER(_CM_PNP_BIOS_DEVICE_NODE)

    # Pnp BIOS Installation check
    class _CM_PNP_BIOS_INSTALLATION_CHECK(ctypes.Structure):
        pass


    _CM_PNP_BIOS_INSTALLATION_CHECK._fields_ = [
        ('Signature', UCHAR * 4), # $PnP (ascii)
        ('Revision', UCHAR),
        ('Length', UCHAR),
        ('ControlField', USHORT),
        ('Checksum', UCHAR),
        ('EventFlagAddress', ULONG), # Physical address
        ('RealModeEntryOffset', USHORT),
        ('RealModeEntrySegment', USHORT),
        ('ProtectedModeEntryOffset', USHORT),
        ('ProtectedModeCodeBaseAddress', ULONG),
        ('OemDeviceId', ULONG),
        ('RealModeDataBaseAddress', USHORT),
        ('ProtectedModeDataBaseAddress', ULONG),
    ]
    CM_PNP_BIOS_INSTALLATION_CHECK = _CM_PNP_BIOS_INSTALLATION_CHECK
    PCM_PNP_BIOS_INSTALLATION_CHECK = POINTER(_CM_PNP_BIOS_INSTALLATION_CHECK)

    # Masks for EISA function information
    EISA_FUNCTION_ENABLED = 0x80
    EISA_FREE_FORM_DATA = 0x40
    EISA_HAS_PORT_INIT_ENTRY = 0x20
    EISA_HAS_PORT_RANGE = 0x10
    EISA_HAS_DMA_ENTRY = 0x08
    EISA_HAS_IRQ_ENTRY = 0x04
    EISA_HAS_MEMORY_ENTRY = 0x02
    EISA_HAS_TYPE_ENTRY = 0x01
    EISA_HAS_INFORMATION = (
        EISA_HAS_PORT_RANGE +                                                     EISA_HAS_DMA_ENTRY +                                                     EISA_HAS_IRQ_ENTRY +                                                     EISA_HAS_MEMORY_ENTRY +                                                     EISA_HAS_TYPE_ENTRY
    )

    # Masks for EISA memory configuration
    EISA_MORE_ENTRIES = 0x80
    EISA_SYSTEM_MEMORY = 0x00
    EISA_MEMORY_TYPE_RAM = 0x01

    # Returned error code for EISA bios call
    EISA_INVALID_SLOT = 0x80
    EISA_INVALID_FUNCTION = 0x81
    EISA_INVALID_CONFIGURATION = 0x82
    EISA_EMPTY_SLOT = 0x83
    EISA_INVALID_BIOS_CALL = 0x86

    # The following structures are used to interpret mips
    # DeviceSpecificData of CM_PARTIAL_RESOURCE_DESCRIPTOR.
    # Device data records for adapters.
    # The device data record for the Emulex SCSI controller.
    class _CM_SCSI_DEVICE_DATA(ctypes.Structure):
        pass


    _CM_SCSI_DEVICE_DATA._fields_ = [
        ('Version', USHORT),
        ('Revision', USHORT),
        ('HostIdentifier', UCHAR),
    ]
    CM_SCSI_DEVICE_DATA = _CM_SCSI_DEVICE_DATA
    PCM_SCSI_DEVICE_DATA = POINTER(_CM_SCSI_DEVICE_DATA)

    # Device data records for controllers.
    # The device data record for the Video controller.
    class _CM_VIDEO_DEVICE_DATA(ctypes.Structure):
        pass


    _CM_VIDEO_DEVICE_DATA._fields_ = [
        ('Version', USHORT),
        ('Revision', USHORT),
        ('VideoClock', ULONG),
    ]
    CM_VIDEO_DEVICE_DATA = _CM_VIDEO_DEVICE_DATA
    PCM_VIDEO_DEVICE_DATA = POINTER(_CM_VIDEO_DEVICE_DATA)

    # The device data record for the SONIC network controller.
    class _CM_SONIC_DEVICE_DATA(ctypes.Structure):
        pass


    _CM_SONIC_DEVICE_DATA._fields_ = [
        ('Version', USHORT),
        ('Revision', USHORT),
        ('DataConfigurationRegister', USHORT),
        ('EthernetAddress', UCHAR * 8),
    ]
    CM_SONIC_DEVICE_DATA = _CM_SONIC_DEVICE_DATA
    PCM_SONIC_DEVICE_DATA = POINTER(_CM_SONIC_DEVICE_DATA)

    # The device data record for the serial controller.
    class _CM_SERIAL_DEVICE_DATA(ctypes.Structure):
        pass


    _CM_SERIAL_DEVICE_DATA._fields_ = [
        ('Version', USHORT),
        ('Revision', USHORT),
        ('BaudClock', ULONG),
    ]
    CM_SERIAL_DEVICE_DATA = _CM_SERIAL_DEVICE_DATA
    PCM_SERIAL_DEVICE_DATA = POINTER(_CM_SERIAL_DEVICE_DATA)

    # Device data records for peripherals.
    # The device data record for the Monitor peripheral.
    class _CM_MONITOR_DEVICE_DATA(ctypes.Structure):
        pass


    _CM_MONITOR_DEVICE_DATA._fields_ = [
        ('Version', USHORT),
        ('Revision', USHORT),
        ('HorizontalScreenSize', USHORT),
        ('VerticalScreenSize', USHORT),
        ('HorizontalResolution', USHORT),
        ('VerticalResolution', USHORT),
        ('HorizontalDisplayTimeLow', USHORT),
        ('HorizontalDisplayTime', USHORT),
        ('HorizontalDisplayTimeHigh', USHORT),
        ('HorizontalBackPorchLow', USHORT),
        ('HorizontalBackPorch', USHORT),
        ('HorizontalBackPorchHigh', USHORT),
        ('HorizontalFrontPorchLow', USHORT),
        ('HorizontalFrontPorch', USHORT),
        ('HorizontalFrontPorchHigh', USHORT),
        ('HorizontalSyncLow', USHORT),
        ('HorizontalSync', USHORT),
        ('HorizontalSyncHigh', USHORT),
        ('VerticalBackPorchLow', USHORT),
        ('VerticalBackPorch', USHORT),
        ('VerticalBackPorchHigh', USHORT),
        ('VerticalFrontPorchLow', USHORT),
        ('VerticalFrontPorch', USHORT),
        ('VerticalFrontPorchHigh', USHORT),
        ('VerticalSyncLow', USHORT),
        ('VerticalSync', USHORT),
        ('VerticalSyncHigh', USHORT),
    ]
    CM_MONITOR_DEVICE_DATA = _CM_MONITOR_DEVICE_DATA
    PCM_MONITOR_DEVICE_DATA = POINTER(_CM_MONITOR_DEVICE_DATA)

    # The device data record for the Floppy peripheral.
    class _CM_FLOPPY_DEVICE_DATA(ctypes.Structure):
        pass


    _CM_FLOPPY_DEVICE_DATA._fields_ = [
        ('Version', USHORT),
        ('Revision', USHORT),
        ('Size', CHAR * 8),
        ('MaxDensity', ULONG),
        ('MountDensity', ULONG),
        ('StepRateHeadUnloadTime', UCHAR), # New data fields for version >= 2.0
        ('HeadLoadTime', UCHAR),
        ('MotorOffTime', UCHAR),
        ('SectorLengthCode', UCHAR),
        ('SectorPerTrack', UCHAR),
        ('ReadWriteGapLength', UCHAR),
        ('DataTransferLength', UCHAR),
        ('FormatGapLength', UCHAR),
        ('FormatFillCharacter', UCHAR),
        ('HeadSettleTime', UCHAR),
        ('MotorSettleTime', UCHAR),
        ('MaximumTrackValue', UCHAR),
        ('DataTransferRate', UCHAR),
    ]
    CM_FLOPPY_DEVICE_DATA = _CM_FLOPPY_DEVICE_DATA
    PCM_FLOPPY_DEVICE_DATA = POINTER(_CM_FLOPPY_DEVICE_DATA)

    # The device data record for the Keyboard peripheral.
    # The KeyboardFlags is defined (by x86 BIOS INT 16h, function 02) as:
    # bit 7 : Insert on
    # bit 6 : Caps Lock on
    # bit 5 : Num Lock on
    # bit 4 : Scroll Lock on
    # bit 3 : Alt Key is down
    # bit 2 : Ctrl Key is down
    # bit 1 : Left shift key is down
    # bit 0 : Right shift key is down
    class _CM_KEYBOARD_DEVICE_DATA(ctypes.Structure):
        pass


    _CM_KEYBOARD_DEVICE_DATA._fields_ = [
        ('Version', USHORT),
        ('Revision', USHORT),
        ('Type', UCHAR),
        ('Subtype', UCHAR),
        ('KeyboardFlags', USHORT),
    ]
    CM_KEYBOARD_DEVICE_DATA = _CM_KEYBOARD_DEVICE_DATA
    PCM_KEYBOARD_DEVICE_DATA = POINTER(_CM_KEYBOARD_DEVICE_DATA)

    # Declaration of the structure for disk geometries
    class _CM_DISK_GEOMETRY_DEVICE_DATA(ctypes.Structure):
        pass


    _CM_DISK_GEOMETRY_DEVICE_DATA._fields_ = [
        ('BytesPerSector', ULONG),
        ('NumberOfCylinders', ULONG),
        ('SectorsPerTrack', ULONG),
        ('NumberOfHeads', ULONG),
    ]
    CM_DISK_GEOMETRY_DEVICE_DATA = _CM_DISK_GEOMETRY_DEVICE_DATA
    PCM_DISK_GEOMETRY_DEVICE_DATA = POINTER(_CM_DISK_GEOMETRY_DEVICE_DATA)

    # Define the bitmasks for resource options
    IO_RESOURCE_PREFERRED = 0x01
    IO_RESOURCE_DEFAULT = 0x02
    IO_RESOURCE_ALTERNATIVE = 0x08

    # Define interrupt affinity policy values

    if defined(NT_PROCESSOR_GROUPS):
        IRQ_DEVICE_POLICY = USHORT
        PIRQ_DEVICE_POLICY = POINTER(USHORT)
        class _IRQ_DEVICE_POLICY_USHORT(ENUM):
            IrqPolicyMachineDefault = 0
            IrqPolicyAllCloseProcessors = 1
            IrqPolicyOneCloseProcessor = 2
            IrqPolicyAllProcessorsInMachine = 3
            IrqPolicyAllProcessorsInGroup = 3
            IrqPolicySpecifiedProcessors = 4
            IrqPolicySpreadMessagesAcrossAllProcessors = 5
            IrqPolicyAllProcessorsInMachineWhenSteered = 6
            IrqPolicyAllProcessorsInGroupWhenSteered = 6


        IrqPolicyMachineDefault = _IRQ_DEVICE_POLICY_USHORT.IrqPolicyMachineDefault
        IrqPolicyAllCloseProcessors = _IRQ_DEVICE_POLICY_USHORT.IrqPolicyAllCloseProcessors
        IrqPolicyOneCloseProcessor = _IRQ_DEVICE_POLICY_USHORT.IrqPolicyOneCloseProcessor
        IrqPolicyAllProcessorsInMachine = _IRQ_DEVICE_POLICY_USHORT.IrqPolicyAllProcessorsInMachine
        IrqPolicyAllProcessorsInGroup = _IRQ_DEVICE_POLICY_USHORT.IrqPolicyAllProcessorsInGroup
        IrqPolicySpecifiedProcessors = _IRQ_DEVICE_POLICY_USHORT.IrqPolicySpecifiedProcessors
        IrqPolicySpreadMessagesAcrossAllProcessors = _IRQ_DEVICE_POLICY_USHORT.IrqPolicySpreadMessagesAcrossAllProcessors
        IrqPolicyAllProcessorsInMachineWhenSteered = _IRQ_DEVICE_POLICY_USHORT.IrqPolicyAllProcessorsInMachineWhenSteered
        IrqPolicyAllProcessorsInGroupWhenSteered = _IRQ_DEVICE_POLICY_USHORT.IrqPolicyAllProcessorsInGroupWhenSteered
    else:
        class _IRQ_DEVICE_POLICY(ENUM):
            IrqPolicyMachineDefault = 0
            IrqPolicyAllCloseProcessors = 1
            IrqPolicyOneCloseProcessor = 2
            IrqPolicyAllProcessorsInMachine = 3
            IrqPolicySpecifiedProcessors = 4
            IrqPolicySpreadMessagesAcrossAllProcessors = 5
            IrqPolicyAllProcessorsInMachineWhenSteered = 6


        IRQ_DEVICE_POLICY = _IRQ_DEVICE_POLICY
        PIRQ_DEVICE_POLICY = POINTER(_IRQ_DEVICE_POLICY)
    # END IF
    # Define interrupt priority policy values
    class _IRQ_PRIORITY(ENUM):
        IrqPriorityUndefined = 0
        IrqPriorityLow = 1
        IrqPriorityNormal = 2
        IrqPriorityHigh = 3


    IRQ_PRIORITY = _IRQ_PRIORITY
    PIRQ_PRIORITY = POINTER(_IRQ_PRIORITY)

    # Define interrupt group affinity policy
    class _IRQ_GROUP_POLICY(ENUM):
        GroupAffinityAllGroupZero = 0
        GroupAffinityDontCare = 1


    IRQ_GROUP_POLICY = _IRQ_GROUP_POLICY
    PIRQ_GROUP_POLICY = POINTER(_IRQ_GROUP_POLICY)

    # This structure defines one type of resource requested by the driver
    class _IO_RESOURCE_DESCRIPTOR(ctypes.Structure):
        pass


    class u(ctypes.Structure):
        pass


    class Port(ctypes.Structure):
        pass


    Port._fields_ = [
        ('Length', ULONG),
        ('Alignment', ULONG),
        ('MinimumAddress', PHYSICAL_ADDRESS),
        ('MaximumAddress', PHYSICAL_ADDRESS),
    ]
    u.Port = Port
    class Memory(ctypes.Structure):
        pass


    Memory._fields_ = [
        ('Length', ULONG),
        ('Alignment', ULONG),
        ('MinimumAddress', PHYSICAL_ADDRESS),
        ('MaximumAddress', PHYSICAL_ADDRESS),
    ]
    u.Memory = Memory
    class Interrupt(ctypes.Structure):
        pass


    Interrupt._fields_ = [
        ('MinimumVector', ULONG),
        ('MaximumVector', ULONG),
            ('AffinityPolicy', IRQ_DEVICE_POLICY),
            ('Group', USHORT),
            ('AffinityPolicy', IRQ_DEVICE_POLICY),
        ('PriorityPolicy', IRQ_PRIORITY),
        ('TargetedProcessors', KAFFINITY),
    ]
    u.Interrupt = Interrupt
    class Dma(ctypes.Structure):
        pass


    Dma._fields_ = [
        ('MinimumChannel', ULONG),
        ('MaximumChannel', ULONG),
    ]
    u.Dma = Dma
    class DmaV3(ctypes.Structure):
        pass


    DmaV3._fields_ = [
        ('RequestLine', ULONG),
        ('Reserved', ULONG),
        ('Channel', ULONG),
        ('TransferWidth', ULONG),
    ]
    u.DmaV3 = DmaV3
    class Generic(ctypes.Structure):
        pass


    Generic._fields_ = [
        ('Length', ULONG),
        ('Alignment', ULONG),
        ('MinimumAddress', PHYSICAL_ADDRESS),
        ('MaximumAddress', PHYSICAL_ADDRESS),
    ]
    u.Generic = Generic
    class DevicePrivate(ctypes.Structure):
        pass


    DevicePrivate._fields_ = [
        ('Data', ULONG * 3),
    ]
    u.DevicePrivate = DevicePrivate
    class BusNumber(ctypes.Structure):
        pass


    BusNumber._fields_ = [
        ('Length', ULONG),
        ('MinBusNumber', ULONG),
        ('MaxBusNumber', ULONG),
        ('Reserved', ULONG),
    ]
    u.BusNumber = BusNumber
    class ConfigData(ctypes.Structure):
        pass


    ConfigData._fields_ = [
        ('Priority', ULONG), # use LCPRI_Xxx values in cfg.h
        ('Reserved1', ULONG),
        ('Reserved2', ULONG),
    ]
    u.ConfigData = ConfigData
    class Memory40(ctypes.Structure):
        pass


    Memory40._fields_ = [
        ('Length40', ULONG),
        ('Alignment40', ULONG),
        ('MinimumAddress', PHYSICAL_ADDRESS),
        ('MaximumAddress', PHYSICAL_ADDRESS),
    ]
    u.Memory40 = Memory40
    class Memory48(ctypes.Structure):
        pass


    Memory48._fields_ = [
        ('Length48', ULONG),
        ('Alignment48', ULONG),
        ('MinimumAddress', PHYSICAL_ADDRESS),
        ('MaximumAddress', PHYSICAL_ADDRESS),
    ]
    u.Memory48 = Memory48
    class Memory64(ctypes.Structure):
        pass


    Memory64._fields_ = [
        ('Length64', ULONG),
        ('Alignment64', ULONG),
        ('MinimumAddress', PHYSICAL_ADDRESS),
        ('MaximumAddress', PHYSICAL_ADDRESS),
    ]
    u.Memory64 = Memory64
    class Connection(ctypes.Structure):
        pass


    Connection._fields_ = [
        ('Class', UCHAR),
        ('Type', UCHAR),
        ('Reserved1', UCHAR),
        ('Reserved2', UCHAR),
        ('IdLowPart', ULONG),
        ('IdHighPart', ULONG),
    ]
    u.Connection = Connection
    u._fields_ = [
        ('Port', u.Port),
        ('Memory', u.Memory),
        ('Interrupt', u.Interrupt),
        ('Dma', u.Dma),
        ('DmaV3', u.DmaV3),
        ('Generic', u.Generic),
        ('DevicePrivate', u.DevicePrivate),
        ('BusNumber', u.BusNumber), # Bus Number information.
        ('ConfigData', u.ConfigData),
        ('Memory40', u.Memory40), # for memory resource requirement greater than MAXULONG
        ('Memory48', u.Memory48),
        ('Memory64', u.Memory64),
        ('Connection', u.Connection),
    ]
    _IO_RESOURCE_DESCRIPTOR.u = u
    _IO_RESOURCE_DESCRIPTOR._fields_ = [
        ('Option', UCHAR),
        ('Type', UCHAR), # use CM_RESOURCE_TYPE
        ('ShareDisposition', UCHAR), # use CM_SHARE_DISPOSITION
        ('Spare1', UCHAR),
        ('Flags', USHORT), # use CM resource flag defines
        ('Spare2', USHORT), # align
        ('u', _IO_RESOURCE_DESCRIPTOR.u),
    ]
    IO_RESOURCE_DESCRIPTOR = _IO_RESOURCE_DESCRIPTOR
    PIO_RESOURCE_DESCRIPTOR = POINTER(_IO_RESOURCE_DESCRIPTOR)
    if defined(NT_PROCESSOR_GROUPS):
        pass
    else:
        pass
    # END IF
    class _IO_RESOURCE_LIST(ctypes.Structure):
        pass


    _IO_RESOURCE_LIST._fields_ = [
        ('Version', USHORT),
        ('Revision', USHORT),
        ('Count', ULONG),
        ('Descriptors', IO_RESOURCE_DESCRIPTOR * 1),
    ]
    IO_RESOURCE_LIST = _IO_RESOURCE_LIST
    PIO_RESOURCE_LIST = POINTER(_IO_RESOURCE_LIST)
    class _IO_RESOURCE_REQUIREMENTS_LIST(ctypes.Structure):
        pass


    _IO_RESOURCE_REQUIREMENTS_LIST._fields_ = [
        ('ListSize', ULONG),
        ('InterfaceType', INTERFACE_TYPE), # unused for WDM
        ('BusNumber', ULONG), # unused for WDM
        ('SlotNumber', ULONG),
        ('Reserved', ULONG * 3),
        ('AlternativeLists', ULONG),
        ('List', IO_RESOURCE_LIST * 1),
    ]
    IO_RESOURCE_REQUIREMENTS_LIST = _IO_RESOURCE_REQUIREMENTS_LIST
    PIO_RESOURCE_REQUIREMENTS_LIST = POINTER(_IO_RESOURCE_REQUIREMENTS_LIST)

    # for move macros
        if not defined(_INC_STRING):
            pass
        # END IF  _INC_STRING
    if defined(_MAC):
        pass
    else:
        pass
    # END IF   _MAC
    if not defined(_SLIST_HEADER_):
        _SLIST_HEADER_ = 1

        if defined(_WIN64):

            # The type SINGLE_LIST_ENTRY is not suitable for use with SLISTs.
            # For
            # WIN64, an entry on an SLIST is required to be 16 - byte aligned,
            # while a
            # SINGLE_LIST_ENTRY structure has only 8 byte alignment.
            # Therefore, all SLIST code should use the SLIST_ENTRY type
            # instead of the
            # SINGLE_LIST_ENTRY type.
            class _SLIST_ENTRY(ctypes.Structure):
                pass


            _SLIST_ENTRY._fields_ = [
                ('Next', POINTER(_SLIST_ENTRY)),
            ]
            SLIST_ENTRY = _SLIST_ENTRY
            PSLIST_ENTRY = POINTER(_SLIST_ENTRY)
        else:
            PSLIST_ENTRY = POINTER(SLIST_ENTRY,)

        # END IF   _WIN64
        if defined(_AMD64_):
            class _SLIST_HEADER(ctypes.Union):
                pass


            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('Alignment', ULONGLONG),
                ('Region', ULONGLONG),
            ]
            _SLIST_HEADER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
            class HeaderX64(ctypes.Structure):
                pass


            HeaderX64._fields_ = [
                ('Depth', ULONGLONG, 16),
                ('Sequence', ULONGLONG, 48),
                ('Reserved', ULONGLONG, 4),
                ('NextEntry', ULONGLONG, 60), # last 4 bits are always 0's
            ]
            _SLIST_HEADER.HeaderX64 = HeaderX64
            _SLIST_HEADER._fields_ = [
                ('DUMMYSTRUCTNAME', _SLIST_HEADER.DUMMYSTRUCTNAME), # original struct
                ('HeaderX64', _SLIST_HEADER.HeaderX64), # x64 16 - byte header
            ]
            SLIST_HEADER = _SLIST_HEADER
            PSLIST_HEADER = POINTER(_SLIST_HEADER)
        elif defined(_ARM64_):

            # ARM64_WORKITEM: should this be merged with AMD64 above?
        elif defined(_X86_):
        elif defined(_ARM_):
        # END IF    # END IF   _SLIST_HEADER_
    # If debugging support enabled, define an ASSERT macro that works.
    # Otherwise
    # define the ASSERT macro to expand to an empty expression.
    # The ASSERT macro has been updated to be an expression instead of a
    # statement.
    ntdll = ctypes.windll.ntdll

    # NTSYSAPI
    # __analysis_noreturn
    # VOID
    # NTAPI
    # RtlAssert(
    # _In_ PVOID VoidFailedAssertion,
    # _In_ PVOID VoidFileName,
    # _In_ ULONG LineNumber,
    # _In_opt_ PSTR MutableMessage
    # );
    RtlAssert = ntdll.RtlAssert
    RtlAssert.restype = VOID
    if DBG:


        def ASSERT(exp):
            return ((not exp) ? (RtlAssert( PVOID#exp, PVOID__FILE__, __LINE__, NULL ),FALSE) : TRUE)


        def ASSERTMSG(msg, exp):
            return ((not exp) ? (RtlAssert( PVOID#exp, PVOID__FILE__, __LINE__, msg ),FALSE) : TRUE)


        def RTL_SOFT_ASSERT(_exp):
            return ((not _exp) ? (DbgPrint("%s%d: Soft assertion failed\n Expression: %s\n", __FILE__, __LINE__, #_exp),FALSE) : TRUE)


        def RTL_SOFT_ASSERTMSG(_msg, _exp):
            return ((not _exp) ? (DbgPrint("%s%d: Soft assertion failed\n Expression: %s\n Message: %s\n", __FILE__, __LINE__, #_exp, _msg),FALSE) : TRUE)
        RTL_VERIFY = ASSERT
        RTL_VERIFYMSG = ASSERTMSG
        RTL_SOFT_VERIFY = RTL_SOFT_ASSERT
        RTL_SOFT_VERIFYMSG = RTL_SOFT_ASSERTMSG
    else:


        def ASSERT(exp):
            return (VOID 0)


        def ASSERTMSG(msg, exp):
            return (VOID 0)


        def RTL_SOFT_ASSERT(_exp):
            return (VOID 0)


        def RTL_SOFT_ASSERTMSG(_msg, _exp):
            return (VOID 0)


        def RTL_VERIFY(exp):
            return (exp ? TRUE : FALSE)


        def RTL_VERIFYMSG(msg, exp):
            return (exp ? TRUE : FALSE)


        def RTL_SOFT_VERIFY(_exp):
            return (_exp ? TRUE : FALSE)


        def RTL_SOFT_VERIFYMSG(msg, _exp):
            return (_exp ? TRUE : FALSE)
    # END IF   DBG

    if not defined(MIDL_PASS) and not defined(SORTPP_PASS):

        # Include the more obscure SAL annotations (like __drv_aliasesMem)
        # instead of assuming the crtdefs.h will include them.
        # Fast fail failure codes.
        # N.B. Failure code zero should not be used, but is required to be
        # reserved
        # for compatibility with previous handling of the
        # STATUS_STACK_BUFFER_OVERRUN exception status code.
        # When updating failure codes here, please also update references in
        # the debugger codebase
        # (currently onecore\sdktools\debuggers\ntsd64\util.cpp)
        FAST_FAIL_LEGACY_GS_VIOLATION = 0
        FAST_FAIL_VTGUARD_CHECK_FAILURE = 1
        FAST_FAIL_STACK_COOKIE_CHECK_FAILURE = 2
        FAST_FAIL_CORRUPT_LIST_ENTRY = 3
        FAST_FAIL_INCORRECT_STACK = 4
        FAST_FAIL_INVALID_ARG = 5
        FAST_FAIL_GS_COOKIE_INIT = 6
        FAST_FAIL_FATAL_APP_EXIT = 7
        FAST_FAIL_RANGE_CHECK_FAILURE = 8
        FAST_FAIL_UNSAFE_REGISTRY_ACCESS = 9
        FAST_FAIL_GUARD_ICALL_CHECK_FAILURE = 10
        FAST_FAIL_GUARD_WRITE_CHECK_FAILURE = 11
        FAST_FAIL_INVALID_FIBER_SWITCH = 12
        FAST_FAIL_INVALID_SET_OF_CONTEXT = 13
        FAST_FAIL_INVALID_REFERENCE_COUNT = 14
        FAST_FAIL_INVALID_JUMP_BUFFER = 18
        FAST_FAIL_MRDATA_MODIFIED = 19
        FAST_FAIL_CERTIFICATION_FAILURE = 20
        FAST_FAIL_INVALID_EXCEPTION_CHAIN = 21
        FAST_FAIL_CRYPTO_LIBRARY = 22
        FAST_FAIL_INVALID_CALL_IN_DLL_CALLOUT = 23
        FAST_FAIL_INVALID_IMAGE_BASE = 24
        FAST_FAIL_DLOAD_PROTECTION_FAILURE = 25
        FAST_FAIL_UNSAFE_EXTENSION_CALL = 26
        FAST_FAIL_DEPRECATED_SERVICE_INVOKED = 27
        FAST_FAIL_INVALID_BUFFER_ACCESS = 28
        FAST_FAIL_INVALID_BALANCED_TREE = 29
        FAST_FAIL_INVALID_NEXT_THREAD = 30
        FAST_FAIL_GUARD_ICALL_CHECK_SUPPRESSED = 31
        FAST_FAIL_APCS_DISABLED = 32
        FAST_FAIL_INVALID_IDLE_STATE = 33
        FAST_FAIL_MRDATA_PROTECTION_FAILURE = 34
        FAST_FAIL_UNEXPECTED_HEAP_EXCEPTION = 35
        FAST_FAIL_INVALID_LOCK_STATE = 36
        FAST_FAIL_GUARD_JUMPTABLE = 37
        FAST_FAIL_INVALID_LONGJUMP_TARGET = 38
        FAST_FAIL_INVALID_DISPATCH_CONTEXT = 39
        FAST_FAIL_INVALID_THREAD = 40
        FAST_FAIL_INVALID_SYSCALL_NUMBER = 41
        FAST_FAIL_INVALID_FILE_OPERATION = 42
        FAST_FAIL_LPAC_ACCESS_DENIED = 43
        FAST_FAIL_GUARD_SS_FAILURE = 44
        FAST_FAIL_LOADER_CONTINUITY_FAILURE = 45
        FAST_FAIL_GUARD_EXPORT_SUPPRESSION_FAILURE = 46
        FAST_FAIL_INVALID_CONTROL_STACK = 47
        FAST_FAIL_SET_CONTEXT_DENIED = 48
        FAST_FAIL_INVALID_IAT = 49
        FAST_FAIL_HEAP_METADATA_CORRUPTION = 50
        FAST_FAIL_PAYLOAD_RESTRICTION_VIOLATION = 51
        FAST_FAIL_LOW_LABEL_ACCESS_DENIED = 52
        FAST_FAIL_ENCLAVE_CALL_FAILURE = 53
        FAST_FAIL_UNHANDLED_LSS_EXCEPTON = 54
        FAST_FAIL_ADMINLESS_ACCESS_DENIED = 55
        FAST_FAIL_UNEXPECTED_CALL = 56
        FAST_FAIL_INVALID_FAST_FAIL_CODE = 0xFFFFFFFF

        if _MSC_VER >= 1610:
            pass
        # END IF
        if _MSC_VER >= 1610:

            # + +
            # VOID
            # RtlFailFast (
            # _In_ ULONG Code
            # );
            # Routine Description:
            # This routine brings down the caller immediately in the event that
            # critical corruption has been detected. No exception handlers are
            # invoked.
            # The routine may be used in libraries shared with user mode and
            # kernel mode. In user mode, the process is terminated, whereas in
            # kernel mode, a KERNEL_SECURITY_CHECK_FAILURE bug check is raised.
            # Arguments
            # Code - Supplies the reason code describing what type of
            # corruption
            # was detected.
            # Return Value:
            # None. There is no return from this routine.
            # - -        # END IF   _MSC_VER
            if not defined(NO_KERNEL_LIST_ENTRY_CHECKS):
                pass
            # END IF
        if not defined(_MSC_FULL_VER) or (_MSC_FULL_VER < 161030716) or defined(_M_CEE_PURE) or defined(_M_CEE_SAFE):
            pass
        # END IF


        def InitializeListHead32(ListHead):
            return (ListHead - >Flink = ListHead - >Blink = PtrToULONG(ListHead))


        def RTL_STATIC_LIST_HEAD(x):
            return LIST_ENTRY x = { & x, & x }

        if defined(NO_KERNEL_LIST_ENTRY_CHECKS):
            pass
        else: #  NO_KERNEL_LIST_ENTRY_CHECKS

            # Routine Description:
            # This routine reports a fatal list entry error. It is implemented
            # here as a
            # wrapper around RtlFailFast so that alternative reporting
            # mechanisms (such
            # as simply logging and trying to
            # continue) can be easily switched in.
            # Arguments:
            # p1 - Supplies the first failure parameter.
            # p2 - Supplies the second failure parameter.
            # p3 - Supplies the third failure parameter.
            # Return Value:
            # None.
            # - -
            if DBG:
                pass
            # END IF
            if DBG:
                pass
            # END IF
            if DBG:
                pass
            # END IF
            if DBG:
                pass
            # END IF        # END IF   NO_KERNEL_LIST_ENTRY_CHECKS    # END IF   not MIDL_PASS
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if defined(_WIN64):


        def RtlIntPtrToUnicodeString(Value, Base, String):
            return RtlInt64ToUnicodeStringValue, Base, String
    else:


        def RtlIntPtrToUnicodeString(Value, Base, String):
            return RtlIntegerToUnicodeStringValue, Base, String
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if not defined(BLDR_KERNEL_RUNTIME):
        pass
    # END IF
    # String manipulation routines
    if defined(_NTSYSTEM_):
        NLS_MB_CODE_PAGE_TAG = NlsMbCodePageTag
        NLS_MB_OEM_CODE_PAGE_TAG = NlsMbOemCodePageTag
    else:
        NLS_MB_CODE_PAGE_TAG = *NlsMbCodePageTag
        NLS_MB_OEM_CODE_PAGE_TAG = *NlsMbOemCodePageTag
    # END IF   _NTSYSTEM_

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # @[comment("MVI_tracked")]
    if not defined(MIDL_PASS):
        pass
    # END IF   not defined(MIDL_PASS)
    PRTL_QUERY_REGISTRY_ROUTINE = POINTER(RTL_QUERY_REGISTRY_ROUTINE)
    class _RTL_QUERY_REGISTRY_TABLE(ctypes.Structure):
        pass


    _RTL_QUERY_REGISTRY_TABLE._fields_ = [
        ('QueryRoutine', PRTL_QUERY_REGISTRY_ROUTINE),
        ('Flags', ULONG),
        ('Name', PWSTR),
        ('EntryContext', PVOID),
        ('DefaultType', ULONG),
        ('DefaultData', PVOID),
        ('DefaultLength', ULONG),
    ]
    RTL_QUERY_REGISTRY_TABLE = _RTL_QUERY_REGISTRY_TABLE
    PRTL_QUERY_REGISTRY_TABLE = POINTER(_RTL_QUERY_REGISTRY_TABLE)

    # The following flags specify how the Name field of a
    # RTL_QUERY_REGISTRY_TABLE
    # entry is interpreted. A NULL name indicates the end of the table.
    RTL_QUERY_REGISTRY_SUBKEY = 0x00000001

    # table or until next subkey are value
    # names for that subkey to look at.
    RTL_QUERY_REGISTRY_TOPKEY = 0x00000002

    # this and all following table entries.
    RTL_QUERY_REGISTRY_REQUIRED = 0x00000004

    # entry.
    RTL_QUERY_REGISTRY_NOVALUE = 0x00000008

    # value name, just wants a call out, not
    # an enumeration of all values.
    RTL_QUERY_REGISTRY_NOEXPAND = 0x00000010

    # REG_MULTI_SZ into multiple callouts or
    # to prevent the expansion of environment
    # variable values in REG_EXPAND_SZ
    RTL_QUERY_REGISTRY_DIRECT = 0x00000020

    # field points to location to store value.
    # For null terminated strings, EntryContext
    # points to UNICODE_STRING structure that
    # that describes maximum size of buffer.
    # If .Buffer field is NULL then a buffer is
    # allocated.
    RTL_QUERY_REGISTRY_DELETE = 0x00000040

    # are queried.
    RTL_QUERY_REGISTRY_NOSTRING = 0x00000080

    # Used with RTL_QUERY_REGISTRY_DIRECT in
    # cases where the caller expects a
    # non - string value. Otherwise, the
    # assumption that EntryContext points to
    # a UNICODE_STRING structure can overrun
    # the caller's buffer.
    RTL_QUERY_REGISTRY_TYPECHECK = 0x00000100

    # validate the registry value type
    # expected by caller with actual type thats
    # read from the registry.
    # Use the most significant byte of DefaultType from QueryTable, as the
    # caller's expected REG_TYPE
    RTL_QUERY_REGISTRY_TYPECHECK_SHIFT = 24
    RTL_QUERY_REGISTRY_TYPECHECK_MASK = (
        0xFF << RTL_QUERY_REGISTRY_TYPECHECK_SHIFT
    )

    if NTDDI_VERSION >= NTDDI_WIN2K:

        # //@[comment("MVI_tracked")]    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8) and not defined(MIDL_PASS:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8) and not defined(MIDL_PASS:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following values for the RelativeTo parameter determine what the
    # Path parameter to RtlQueryRegistryValues is relative to.
    RTL_REGISTRY_ABSOLUTE = 0
    RTL_REGISTRY_SERVICES = 1
    RTL_REGISTRY_CONTROL = 2
    RTL_REGISTRY_WINDOWS_NT = 3
    RTL_REGISTRY_DEVICEMAP = 4
    RTL_REGISTRY_USER = 5
    RTL_REGISTRY_MAXIMUM = 6
    RTL_REGISTRY_HANDLE = 0x40000000
    RTL_REGISTRY_OPTIONAL = 0x80000000

    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
    # NLS String functions
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    HASH_STRING_ALGORITHM_DEFAULT = 0
    HASH_STRING_ALGORITHM_X65599 = 1
    HASH_STRING_ALGORITHM_INVALID = 0xFFFFFFFF

    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # NTSYSAPI
    # ULONG
    # NTAPI
    # RtlUnicodeStringToAnsiSize(
    # PUNICODE_STRING UnicodeString
    # );


    def RtlUnicodeStringToAnsiSize(STRING):
        return (NLS_MB_CODE_PAGE_TAG ? RtlxUnicodeStringToAnsiSizeSTRING : STRING - >Length + ctypes.sizeofUNICODE_NULL / ctypes.sizeofWCHAR)

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # NTSYSAPI
    # ULONG
    # NTAPI
    # RtlAnsiStringToUnicodeSize(
    # PANSI_STRING AnsiString
    # );


    def RtlAnsiStringToUnicodeSize(STRING):
        return (NLS_MB_CODE_PAGE_TAG ? RtlxAnsiStringToUnicodeSizeSTRING : STRING - >Length + ctypes.sizeofANSI_NULL * ctypes.sizeofWCHAR)

    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if not defined(DEFINE_GUIDEX):


        def DEFINE_GUIDEX(name):
            return EXTERN_C CDECL GUID name
    # END IF   not defined(DEFINE_GUIDEX)

    if not defined(STATICGUIDOF):


        def STATICGUIDOF(guid):
            return STATIC_##guid
    # END IF   not defined(STATICGUIDOF)

    if not defined(__IID_ALIGNED__):
        __IID_ALIGNED__ = 1

        if defined(__cplusplus):
            pass
        else: #  not __cplusplus
            pass
        # END IF   not __cplusplus    # END IF   not __IID_ALIGNED__
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)
    # Fast primitives to compare, move, and zero memory
    if defined(_DBG_MEMCPY_INLINE_) and not defined(MIDL_PASS) and not defined(_MEMCPY_INLINE_) and not defined(_CRTBLD):
        _MEMCPY_INLINE_ = 1
        # }
        # return memcpy(dst, src, size);
        memcpy = ntdll.memcpy
        memcpy.restype = return    # END IF

        if defined(_M_AMD64):
            pass
            if not defined(_M_CEE) and (defined(_M_ARM) or defined(_M_ARM64)):
                pass
            else:
                pass
            # END IF
        else:
            pass
        # END IF   _M_AMD64
    if not defined(MIDL_PASS):
        pass
    # END IF
    if defined(_M_AMD64):
        pass
    else:
        RtlCopyMemoryNonTemporal = RtlCopyMemory
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2KSP3:
        pass
    # END IF
    # Define kernel debugger print prototypes and macros.
    # N.B. The following function cannot be directly imported because there are
    # a few places in the source tree where this function is redefined.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        if _MSC_FULL_VER >= 150030729) and not defined(IMPORT_NATIVE_DBG_BREAK:
            DbgBreakPoint = __debugbreak
        else:
            # __analysis_noreturn
            # VOID
            # NTAPI
            # DbgBreakPoint(
            # VOID
            # );
            DbgBreakPoint = ntdll.DbgBreakPoint
            DbgBreakPoint.restype = VOID        # END IF    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    DBG_STATUS_CONTROL_C = 1
    DBG_STATUS_SYSRQ = 2
    DBG_STATUS_BUGCHECK_FIRST = 3
    DBG_STATUS_BUGCHECK_SECOND = 4
    DBG_STATUS_FATAL = 5
    DBG_STATUS_DEBUG_CONTROL = 6
    DBG_STATUS_WORKER = 7

    if DBG:


        def KdPrint(_x_):
            return DbgPrint _x_


        def KdPrintEx(_x_):
            return DbgPrintEx _x_


        def vKdPrintEx(_x_):
            return vDbgPrintEx _x_


        def vKdPrintExWithPrefix(_x_):
            return vDbgPrintExWithPrefix _x_


        def KdBreakPoint():
            return DbgBreakPoint


        def KdBreakPointWithStatus(s):
            return DbgBreakPointWithStatuss
    else:


        def KdPrint(_x_):
            return 1


        def KdPrintEx(_x_):
            return 1


        def vKdPrintEx(_x_):
            return 1


        def vKdPrintExWithPrefix(_x_):
            return 1


        def KdBreakPoint():
            return 1


        def KdBreakPointWithStatus(s):
            return 1
    # END IF   DBG wudfwdm

        if NTDDI_VERSION >= NTDDI_WINXP:
            pass
        # END IF
    if not defined(_DBGNT_):
        if defined(_VA_LIST_DEFINED):
            if NTDDI_VERSION >= NTDDI_WINXP:
                # NTSYSAPI
                # ULONG
                # NTAPI
                # vDbgPrintEx(
                # _In_ ULONG ComponentId,
                # _In_ ULONG Level,
                # _In_z_ PCCH Format,
                # _In_ va_list arglist
                # );
                vDbgPrintEx = ntdll.vDbgPrintEx
                vDbgPrintEx.restype = ULONG            # END IF        # END IF   _VA_LIST_DEFINED
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WINXP:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WINXP:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF    # END IF   _DBGNT_
    # Large integer arithmetic routines.
    # Large integer add - 64 - bits + 64 - bits - > 64 - bits
        if defined(_AMD64_) or defined(_ARM64_) or defined(_M_HYBRID_X86_ARM64)) and not defined(_M_CEE_PURE:
            pass
        # END IF   defined(_AMD64_) or defined(_ARM64_)
            if NTDDI_VERSION >= NTDDI_WIN2K:
                pass
            # END IF
        if defined(_X86_) and not defined(_M_HYBRID_X86_ARM64)) or defined(_ARM_) or defined(_IA64_:
            pass
        # END IF   defined(_X86_) or defined(_ARM_) or defined(_IA64_)
    if not defined(MIDL_PASS):
        if defined(_AMD64_) or defined(_ARM_) or defined(_ARM64_) or defined(_IA64_) or defined(_CHPE_X86_ARM64_):

            # Large Integer divide - 64 - bits / 32 - bits - > 64 - bits
            if NTDDI_VERSION >= NTDDI_WIN2K:
                pass
            # END IF
        else:

            # Extended integer multiply - 32 - bits * 64 - bits - > 64 - bits
            if NTDDI_VERSION >= NTDDI_WIN2K:
                pass
            # END IF        # END IF   defined(_AMD64_) or defined(_ARM_) or defined(_ARM64_) or defined(_IA64_)
        # Large integer and - 64 - bite & 64 - bits - > 64 - bits.
        if PRAGMA_DEPRECATED_DDK:
            pass
        # END IF


        def RtlLargeIntegerAnd(Result, Source, Mask):
            return Result.QuadPart = Source.QuadPart & Mask.QuadPart

        # Convert INTeger to large integer.

        if PRAGMA_DEPRECATED_DDK:
            pass
        # END IF    # END IF   not defined(MIDL_PASS)
    PTIME_FIELDS = POINTER(TIME_FIELDS)
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # A time field record (Weekday ignored) - > 64 bit Time value
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following macros store and retrieve USHORTS and ULONGS from
    # potentially
    # unaligned addresses, aVOIDing alignment faults. they should probably be
    # rewritten in assembler
    SHORT_SIZE = ctypes.sizeof(USHORT)
    SHORT_MASK = SHORT_SIZE - 1
    LONG_SIZE = ctypes.sizeof(LONG)
    LONGLONG_SIZE = ctypes.sizeof(LONGLONG)
    LONG_MASK = LONG_SIZE - 1
    LONGLONG_MASK = LONGLONG_SIZE - 1
    LOWBYTE_MASK = 0x00FF


    def FIRSTBYTE(VALUE):
        return (VALUE & LOWBYTE_MASK)


    def SECONDBYTE(VALUE):
        return ((VALUE >> 8) & LOWBYTE_MASK)


    def THIRDBYTE(VALUE):
        return ((VALUE >> 16) & LOWBYTE_MASK)


    def FOURTHBYTE(VALUE):
        return ((VALUE >> 24) & LOWBYTE_MASK)

    # if MIPS Big Endian, order of bytes is reversed.
    SHORT_LEAST_SIGNIFICANT_BIT = 0
    SHORT_MOST_SIGNIFICANT_BIT = 1
    LONG_LEAST_SIGNIFICANT_BIT = 0
    LONG_3RD_MOST_SIGNIFICANT_BIT = 1
    LONG_2ND_MOST_SIGNIFICANT_BIT = 2
    LONG_MOST_SIGNIFICANT_BIT = 3

    # + +
    # VOID
    # RtlStoreUSHORT (
    # PUSHORT ADDRESS
    # USHORT VALUE
    # )
    # Routine Description:
    # This macro stores a USHORT value in at a particular address, aVOIDing
    # alignment faults.
    # Arguments:
    # ADDRESS - where to store USHORT value
    # VALUE - USHORT to store
    # Return Value:
    # none.
    # - -

    if defined(_AMD64_):


        def RtlStoreUSHORT(ADDRESS, VALUE):
            return *USHORT UNALIGNED *ADDRESS = VALUE
    else:


        def RtlStoreUSHORT(ADDRESS, VALUE):
            return if ULONG_PTRADDRESS & SHORT_MASK) { (PUCHAR ADDRESS[SHORT_LEAST_SIGNIFICANT_BIT] = UCHAR(FIRSTBYTEVALUE); (PUCHAR ADDRESS)[SHORT_MOST_SIGNIFICANT_BIT ] = UCHAR(SECONDBYTEVALUE); } else { *(PUSHORT ADDRESS) = USHORT VALUE; }
    # END IF
    # + +
    # VOID
    # RtlStoreULONG (
    # PULONG ADDRESS
    # ULONG VALUE
    # )
    # Routine Description:
    # This macro stores a ULONG value in at a particular address, aVOIDing
    # alignment faults.
    # Arguments:
    # ADDRESS - where to store ULONG value
    # VALUE - ULONG to store
    # Return Value:
    # none.
    # Note:
    # Depending on the machine, we might want to call storeuSHORT in the
    # unaligned case.
    # - -

    if defined(_AMD64_):


        def RtlStoreULONG(ADDRESS, VALUE):
            return *ULONG UNALIGNED *ADDRESS = VALUE
    else:


        def RtlStoreULONG(ADDRESS, VALUE):
            return if ULONG_PTRADDRESS & LONG_MASK) { (PUCHAR ADDRESS[LONG_LEAST_SIGNIFICANT_BIT ] = UCHAR(FIRSTBYTEVALUE); (PUCHAR ADDRESS)[LONG_3RD_MOST_SIGNIFICANT_BIT ] = UCHAR(SECONDBYTEVALUE); (PUCHAR ADDRESS)[LONG_2ND_MOST_SIGNIFICANT_BIT ] = UCHAR(THIRDBYTEVALUE); (PUCHAR ADDRESS)[LONG_MOST_SIGNIFICANT_BIT ] = UCHAR(FOURTHBYTEVALUE); } else { *(PULONG ADDRESS) = ULONG VALUE; }
    # END IF
    # + +
    # VOID
    # RtlStoreULONGLONG (
    # PULONGLONG ADDRESS
    # ULONG VALUE
    # )
    # Routine Description:
    # This macro stores a ULONGLONG value in at a particular address, aVOIDing
    # alignment faults.
    # Arguments:
    # ADDRESS - where to store ULONGLONG value
    # VALUE - ULONGLONG to store
    # Return Value:
    # none.
    # - -

    if defined(_AMD64_):


        def RtlStoreULONGLONG(ADDRESS, VALUE):
            return *ULONGLONG UNALIGNED *ADDRESS = VALUE
    else:


        def RtlStoreULONGLONG(ADDRESS, VALUE):
            return if ULONG_PTRADDRESS & LONGLONG_MASK) { RtlStoreULONG(ULONG_PTRADDRESS, ULONGLONGVALUE & 0xFFFFFFFF); RtlStoreULONG(ULONG_PTRADDRESS + ctypes.sizeofULONG, ULONGLONGVALUE >> 32); } else { *(PULONGLONGADDRESS = ULONGLONGVALUE; }
    # END IF
    # + +
    # VOID
    # RtlStoreULONGPtr (
    # PULONG_PTR ADDRESS
    # ULONG_PTR VALUE
    # )
    # Routine Description:
    # This macro stores a ULONG_PTR value in at a particular address, aVOIDing
    # alignment faults.
    # Arguments:
    # ADDRESS - where to store ULONG_PTR value
    # VALUE - ULONG_PTR to store
    # Return Value:
    # none.
    # - -

    if defined(_WIN64):


        def RtlStoreULONGPtr(ADDRESS, VALUE):
            return RtlStoreULONGLONGADDRESS,VALUE
    else:


        def RtlStoreULONGPtr(ADDRESS, VALUE):
            return RtlStoreULONGADDRESS,VALUE
    # END IF
    # + +
    # VOID
    # RtlRetrieveUSHORT (
    # PUSHORT DESTINATION_ADDRESS
    # PUSHORT SOURCE_ADDRESS
    # )
    # Routine Description:
    # This macro retrieves a USHORT value from the SOURCE address, aVOIDing
    # alignment faults. The DESTINATION address is assumed to be aligned.
    # Arguments:
    # DESTINATION_ADDRESS - where to store USHORT value
    # SOURCE_ADDRESS - where to retrieve USHORT value from
    # Return Value:
    # none.
    # - -

    if defined(_AMD64_):


        def RtlRetrieveUSHORT(DEST_ADDRESS, SRC_ADDRESS):
            return *USHORT UNALIGNED *DEST_ADDRESS = *PUSHORTSRC_ADDRESS
    else:


        def RtlRetrieveUSHORT(DEST_ADDRESS, SRC_ADDRESS):
            return if ULONG_PTRSRC_ADDRESS & SHORT_MASK) { (PUCHAR DEST_ADDRESS[0] = (PUCHAR SRC_ADDRESS)[0]; (PUCHAR DEST_ADDRESS)[1] = (PUCHAR SRC_ADDRESS)[1]; } else { *(PUSHORT DEST_ADDRESS) = *(PUSHORT SRC_ADDRESS); }
    # END IF
    # + +
    # VOID
    # RtlRetrieveULONG (
    # PULONG DESTINATION_ADDRESS
    # PULONG SOURCE_ADDRESS
    # )
    # Routine Description:
    # This macro retrieves a ULONG value from the SOURCE address, aVOIDing
    # alignment faults. The DESTINATION address is assumed to be aligned.
    # Arguments:
    # DESTINATION_ADDRESS - where to store ULONG value
    # SOURCE_ADDRESS - where to retrieve ULONG value from
    # Return Value:
    # none.
    # Note:
    # Depending on the machine, we might want to call retrieveuSHORT in the
    # unaligned case.
    # - -

    if defined(_AMD64_):


        def RtlRetrieveULONG(DEST_ADDRESS, SRC_ADDRESS):
            return *ULONG UNALIGNED *DEST_ADDRESS = *PULONGSRC_ADDRESS
    else:


        def RtlRetrieveULONG(DEST_ADDRESS, SRC_ADDRESS):
            return if ULONG_PTRSRC_ADDRESS & LONG_MASK) { (PUCHAR DEST_ADDRESS[0] = (PUCHAR SRC_ADDRESS)[0]; (PUCHAR DEST_ADDRESS)[1] = (PUCHAR SRC_ADDRESS)[1]; (PUCHAR DEST_ADDRESS)[2] = (PUCHAR SRC_ADDRESS)[2]; (PUCHAR DEST_ADDRESS)[3] = (PUCHAR SRC_ADDRESS)[3]; } else { *(PULONG DEST_ADDRESS) = *(PULONG SRC_ADDRESS); }
    # END IF
    # BitMap routines. The following structure, routines, and macros are
    # for manipulating bitmaps. The user is responsible for allocating a bitmap
    # structure (which is really a header) and a buffer (which must be LONGword
    # aligned and multiple LONGwords in size).
    class _RTL_BITMAP(ctypes.Structure):
        pass


    _RTL_BITMAP._fields_ = [
        ('SizeOfBitMap', ULONG), # Number of bits in bit map
        ('Buffer', PULONG), # Pointer to the bit map itself
    ]
    RTL_BITMAP = _RTL_BITMAP
    PRTL_BITMAP = POINTER(RTL_BITMAP)

    # begin_ntoshvbootp
    # The following routine initializes a new bitmap. It does not alter the
    # data currently in the bitmap. This routine must be called before
    # any other bitmap routine/macro.

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following three routines clear, set, and test the state of a
    # single bit in a bitmap.
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    # The following two routines either clear or set all of the bits
    # in a bitmap.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following two routines locate a contiguous region of either
    # clear or set bits within the bitmap. The region will be at least
    # as large as the number specified, and the search of the bitmap will
    # begin at the specified hint index (which is a bit index within the
    # bitmap, zero based). The return value is the bit index of the located
    # region (zero based) or - 1 (i.e., 0xffffffff) if such a region cannot
    # be located
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following two routines locate a contiguous region of either
    # clear or set bits within the bitmap and either set or clear the bits
    # within the located region. The region will be as large as the number
    # specified, and the search for the region will begin at the specified
    # hint index (which is a bit index within the bitmap, zero based). The
    # return value is the bit index of the located region (zero based) or
    # - 1 (i.e., 0xffffffff) if such a region cannot be located. If a region
    # cannot be located then the setting/clearing of the bitmap is not
    # performed.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following two routines clear or set bits within a specified region
    # of the bitmap. The starting index is zero based.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following routine locates a set of contiguous regions of clear
    # bits within the bitmap. The caller specifies whether to return the
    # LONGest runs or just the first found lcoated. The following structure is
    # used to denote a contiguous run of bits. The two routines return an array
    # of this structure, one for each run located.
    class _RTL_BITMAP_RUN(ctypes.Structure):
        pass


    _RTL_BITMAP_RUN._fields_ = [
        ('StartingIndex', ULONG),
        ('NumberOfBits', ULONG),
    ]
    RTL_BITMAP_RUN = _RTL_BITMAP_RUN
    PRTL_BITMAP_RUN = POINTER(RTL_BITMAP_RUN)
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following routine locates the LONGest contiguous region of
    # clear bits within the bitmap. The returned starting index value
    # denotes the first contiguous region located satisfying our requirements
    # The return value is the length (in bits) of the LONGest region found.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following routine locates the first contiguous region of
    # clear bits within the bitmap. The returned starting index value
    # denotes the first contiguous region located satisfying our requirements
    # The return value is the length (in bits) of the region found.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following macro returns the value of the bit stored within the
    # bitmap at the specified location. If the bit is set a value of 1 is
    # returned otherwise a value of 0 is returned.
    # ULONG
    # RtlCheckBit (
    # PRTL_BITMAP BitMapHeader,
    # ULONG BitPosition
    # );
    # To implement CheckBit the macro retrieves the LONGword containing the
    # bit in question, shifts the LONGword to get the bit in question into the
    # low order bit position and masks out all other bits.
    if defined(_M_AMD64) and not defined(MIDL_PASS):
        pass
    else:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following two procedures return to the caller a BOOL value
    # indicating if the specified range of bits are all clear or set.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following two procedures return to the caller a value indicating
    # the position within a ULONGLONG of the most or least significant non -
    # zero
    # bit. A value of zero results in a return value of - 1.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following procedure finds the number of set bits within a ULONG_PTR
    # value.
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    # BOOLEAN
    # RtlEqualLuid(
    # PLUID L1,
    # PLUID L2
    # );


    def RtlEqualLuid(L1, L2):
        return (L1 - >LowPart == L2 - >LowPart) and (L1 - >HighPart == L2 - >HighPart)

    # BOOLEAN
    # RtlIsZeroLuid(
    # PLUID L1
    # );


    def RtlIsZeroLuid(L1):
        return BOOLEAN ((L1 - >LowPart | L1 - >HighPart) == 0)

    # SecurityDescriptor RTL routine definitions

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    SEF_DACL_AUTO_INHERIT = 0x01
    SEF_SACL_AUTO_INHERIT = 0x02
    SEF_DEFAULT_DESCRIPTOR_FOR_OBJECT = 0x04
    SEF_AVOID_PRIVILEGE_CHECK = 0x08
    SEF_AVOID_OWNER_CHECK = 0x10
    SEF_DEFAULT_OWNER_FROM_PARENT = 0x20
    SEF_DEFAULT_GROUP_FROM_PARENT = 0x40
    SEF_MACL_NO_WRITE_UP = 0x100
    SEF_MACL_NO_READ_UP = 0x200
    SEF_MACL_NO_EXECUTE_UP = 0x400
    SEF_AI_USE_EXTRA_PARAMS = 0x800
    SEF_AVOID_OWNER_RESTRICTION = 0x1000
    SEF_FORCE_USER_MODE = 0x2000
    SEF_MACL_VALID_FLAGS = (
        SEF_MACL_NO_WRITE_UP |
        SEF_MACL_NO_READ_UP |
        SEF_MACL_NO_EXECUTE_UP
    )

    # Byte swap routines. These are used to convert from little - endian to
    # big - endian and vice - versa.

        if defined(__cplusplus):
            pass
        # END IF
    if defined(_M_IX86) and (_MSC_FULL_VER > 13009037)) or ((defined(_M_AMD64) or defined(_M_IA64)) and (_MSC_FULL_VER > 13009175)) or defined(_M_ARM) or defined(_M_ARM64:
        ucrtbase = ctypes.windll.ucrtbase

        # _Check_return_ UINT INT64 __cdecl _byteswap_uint64(_In_ UINT INT64);
        _byteswap_uint64 = ucrtbase._byteswap_uint64
        _byteswap_uint64.restype = INT64
        if defined(__cplusplus):
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
    else:
        pass
    # END IF
    class _OSVERSIONINFOA(ctypes.Structure):
        pass


    _OSVERSIONINFOA._fields_ = [
        ('dwOSVersionInfoSize', ULONG),
        ('dwMajorVersion', ULONG),
        ('dwMinorVersion', ULONG),
        ('dwBuildNumber', ULONG),
        ('dwPlatformId', ULONG),
        ('szCSDVersion', CHAR * 128), # Maintenance string for PSS usage
    ]
    OSVERSIONINFOA = _OSVERSIONINFOA
    POSVERSIONINFOA = POINTER(_OSVERSIONINFOA)
    LPOSVERSIONINFOA = POINTER(_OSVERSIONINFOA)
    class _OSVERSIONINFOW(ctypes.Structure):
        pass


    _OSVERSIONINFOW._fields_ = [
        ('dwOSVersionInfoSize', ULONG),
        ('dwMajorVersion', ULONG),
        ('dwMinorVersion', ULONG),
        ('dwBuildNumber', ULONG),
        ('dwPlatformId', ULONG),
        ('szCSDVersion', WCHAR * 128), # Maintenance string for PSS usage
    ]
    OSVERSIONINFOW = _OSVERSIONINFOW
    POSVERSIONINFOW = POINTER(_OSVERSIONINFOW)
    LPOSVERSIONINFOW = POINTER(_OSVERSIONINFOW)
    RTL_OSVERSIONINFOW = _OSVERSIONINFOW
    PRTL_OSVERSIONINFOW = POINTER(_OSVERSIONINFOW)
    if defined(UNICODE):
        OSVERSIONINFO = OSVERSIONINFOW
        POSVERSIONINFO = POSVERSIONINFOW
        LPOSVERSIONINFO = LPOSVERSIONINFOW
    else:
        OSVERSIONINFO = OSVERSIONINFOA
        POSVERSIONINFO = POSVERSIONINFOA
        LPOSVERSIONINFO = LPOSVERSIONINFOA
    # END IF   UNICODE
    class _OSVERSIONINFOEXA(ctypes.Structure):
        pass


    _OSVERSIONINFOEXA._fields_ = [
        ('dwOSVersionInfoSize', ULONG),
        ('dwMajorVersion', ULONG),
        ('dwMinorVersion', ULONG),
        ('dwBuildNumber', ULONG),
        ('dwPlatformId', ULONG),
        ('szCSDVersion', CHAR * 128), # Maintenance string for PSS usage
        ('wServicePackMajor', USHORT),
        ('wServicePackMinor', USHORT),
        ('wSuiteMask', USHORT),
        ('wProductType', UCHAR),
        ('wReserved', UCHAR),
    ]
    OSVERSIONINFOEXA = _OSVERSIONINFOEXA
    POSVERSIONINFOEXA = POINTER(_OSVERSIONINFOEXA)
    LPOSVERSIONINFOEXA = POINTER(_OSVERSIONINFOEXA)
    class _OSVERSIONINFOEXW(ctypes.Structure):
        pass


    _OSVERSIONINFOEXW._fields_ = [
        ('dwOSVersionInfoSize', ULONG),
        ('dwMajorVersion', ULONG),
        ('dwMinorVersion', ULONG),
        ('dwBuildNumber', ULONG),
        ('dwPlatformId', ULONG),
        ('szCSDVersion', WCHAR * 128), # Maintenance string for PSS usage
        ('wServicePackMajor', USHORT),
        ('wServicePackMinor', USHORT),
        ('wSuiteMask', USHORT),
        ('wProductType', UCHAR),
        ('wReserved', UCHAR),
    ]
    OSVERSIONINFOEXW = _OSVERSIONINFOEXW
    POSVERSIONINFOEXW = POINTER(_OSVERSIONINFOEXW)
    LPOSVERSIONINFOEXW = POINTER(_OSVERSIONINFOEXW)
    RTL_OSVERSIONINFOEXW = _OSVERSIONINFOEXW
    PRTL_OSVERSIONINFOEXW = POINTER(_OSVERSIONINFOEXW)
    if defined(UNICODE):
        OSVERSIONINFOEX = OSVERSIONINFOEXW
        POSVERSIONINFOEX = POSVERSIONINFOEXW
        LPOSVERSIONINFOEX = LPOSVERSIONINFOEXW
    else:
        OSVERSIONINFOEX = OSVERSIONINFOEXA
        POSVERSIONINFOEX = POSVERSIONINFOEXA
        LPOSVERSIONINFOEX = LPOSVERSIONINFOEXA
    # END IF   UNICODE
    # RtlVerifyVersionInfo() conditions
    VER_EQUAL = 1
    VER_GREATER = 2
    VER_GREATER_EQUAL = 3
    VER_LESS = 4
    VER_LESS_EQUAL = 5
    VER_AND = 6
    VER_OR = 7
    VER_CONDITION_MASK = 7
    VER_NUM_BITS_PER_CONDITION_MASK = 3

    # RtlVerifyVersionInfo() type mask bits
    VER_MINORVERSION = 0x0000001
    VER_MAJORVERSION = 0x0000002
    VER_BUILDNUMBER = 0x0000004
    VER_PLATFORMID = 0x0000008
    VER_SERVICEPACKMINOR = 0x0000010
    VER_SERVICEPACKMAJOR = 0x0000020
    VER_SUITENAME = 0x0000040
    VER_PRODUCT_TYPE = 0x0000080

    # RtlVerifyVersionInfo() os product type values
    VER_NT_WORKSTATION = 0x0000001
    VER_NT_DOMAIN_CONTROLLER = 0x0000002
    VER_NT_SERVER = 0x0000003

    # dwPlatformId defines:
    VER_PLATFORM_WIN32s = 0
    VER_PLATFORM_WIN32_WINDOWS = 1
    VER_PLATFORM_WIN32_NT = 2

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):

        # VerifyVersionInfo() macro to set the condition mask
        # For documentation sakes here's the old version of the macro that got
        # changed to call an API
        # define VER_SET_CONDITION(_m_,_t_,_c_) _m_=(_m_ | (_c_ << (1 << _t_)))


        def VER_SET_CONDITION(_m_, _t_, _c_):
            return (_m_=VerSetConditionMask(_m_,_t_,_c_))

        if not defined(_WINBASE_) and not defined(MIDL_PASS):
            if NTDDI_VERSION >= NTDDI_WIN2K:
                # NTSYSAPI
                # ULONGLONG
                # NTAPI
                # VerSetConditionMask(
                # _In_ ULONGLONG ConditionMask,
                # _In_ ULONG TypeMask,
                # _In_ UCHAR Condition
                # );
                VerSetConditionMask = ntdll.VerSetConditionMask
                VerSetConditionMask.restype = ULONGLONG            # END IF        # END IF   not defined(_WINBASE_) and not defined(MIDL_PASS)    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    if NTDDI_VERSION >= NTDDI_WIN2K:

        # //@[comment("MVI_tracked")]    # END IF
    # Interlocked bit manipulation interfaces


    def RtlInterlockedSetBits(Flags, Flag):
        return InterlockedOr(PLONGFlags, Flag)


    def RtlInterlockedAndBits(Flags, Flag):
        return InterlockedAnd(PLONGFlags, Flag)


    def RtlInterlockedClearBits(Flags, Flag):
        return RtlInterlockedAndBits(Flags, ~Flag)


    def RtlInterlockedXorBits(Flags, Flag):
        return InterlockedXorFlags, Flag


    def RtlInterlockedSetBitsDiscardReturn(Flags, Flag):
        return VOID RtlInterlockedSetBitsFlags, Flag


    def RtlInterlockedAndBitsDiscardReturn(Flags, Flag):
        return VOID RtlInterlockedAndBitsFlags, Flag


    def RtlInterlockedClearBitsDiscardReturn(Flags, Flag):
        return RtlInterlockedAndBitsDiscardReturn(Flags, ~Flag)

    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8) and not defined(MIDL_PASS:
        pass
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8) and not defined(MIDL_PASS)
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if not defined(VRL_GLOBAL_LEVEL):
        if NTDDI_VERSION >= NTDDI_WIN8:

            # VRL_GLOBAL_LEVEL is a SHORTcut to querying the global validation
            # runlevel.
            # This should only be used when the component - specific level is
            # unavailable or
            # cannot be queried for whatever reason.
            # The following define can only be used by kernel - mode callers.
            # It is redefined
            # suitably for user - mode callers if nturtl is included after.
            VRL_GLOBAL_LEVEL = SharedUserData - >GlobalValidationRunlevel
        # END IF   (NTDDI_VERSION >= NTDDI_WIN8)    # END IF   not defined(VRL_GLOBAL_LEVEL)

    if not defined(IS_VALIDATION_ENABLED):
        if NTDDI_VERSION >= NTDDI_WIN8:

            # Validation runlevel helper macro: checks if a particular level L
            # enables the
            # validation class C.
            # Returns a non - zero scalar if class C is enabled, and zero
            # otherwise.


            def IS_VALIDATION_ENABLED(C, L):
                return L & C

            # Validation classes are broken into:
            # 8 predefined validation classes, spanning bits 0 to 7 of the
            # level value
            # 24 custom - defined validation classes, spanning bits 8 to 31
            VRL_PREDEFINED_CLASS_BEGIN = 1 << 0
            VRL_CUSTOM_CLASS_BEGIN = 1 << 8

            # The following are predefined validation classes.
            VRL_CLASS_CONSISTENCY = VRL_PREDEFINED_CLASS_BEGIN << 0

            # Do not ignore kernel breaks when kernel debugging is disabled
            # (debug builds only)
            VRL_ENABLE_KERNEL_BREAKS = 1 << 31
        # END IF   (NTDDI_VERSION >= NTDDI_WIN8)    # END IF   not defined(IS_VALIDATION_ENABLED)

    if NTDDI_VERSION >= NTDDI_WIN8:

        # RtlCheckTokenMembership flags.
        CTMF_INCLUDE_APPCONTAINER = 0x00000001
        CTMF_INCLUDE_LPAC = 0x00000002
        CTMF_VALID_FLAGS = CTMF_INCLUDE_APPCONTAINER | CTMF_INCLUDE_LPAC
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    if NTDDI_VERSION >= NTDDI_WIN8:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):

            # Crc32 and Crc64 routines that use standardized algorithms        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:

        # API to detect what type of OS Deployment this is. Current valid
        # values
        # are listed below
        # Valid OsDeployment values that can be returned
        class _OS_DEPLOYEMENT_STATE_VALUES(ENUM):
            OS_DEPLOYMENT_STANDARD = 1
            OS_DEPLOYMENT_COMPACT = 2


        OS_DEPLOYEMENT_STATE_VALUES = _OS_DEPLOYEMENT_STATE_VALUES
    # END IF   NTDDI_VERSION >= NTDDI_WINTHRESHOLD
    # Support for process policy settings embedded into executable image.
    IMAGE_POLICY_METADATA_VERSION = 1
    IMAGE_POLICY_SECTION_NAME = ".tPolicy"
    IMAGE_POLICY_METADATA_NAME = __ImagePolicyMetadata


    class _IMAGE_POLICY_ENTRY_TYPE(ENUM):
        ImagePolicyEntryTypeNone = 0
        ImagePolicyEntryTypeBool = 1
        ImagePolicyEntryTypeInt8 = 2
        ImagePolicyEntryTypeUInt8 = 3
        ImagePolicyEntryTypeInt16 = 4
        ImagePolicyEntryTypeUInt16 = 5
        ImagePolicyEntryTypeInt32 = 6
        ImagePolicyEntryTypeUInt32 = 7
        ImagePolicyEntryTypeInt64 = 8
        ImagePolicyEntryTypeUInt64 = 9
        ImagePolicyEntryTypeAnsiString = 10
        ImagePolicyEntryTypeUnicodeString = 11
        ImagePolicyEntryTypeOverride = 12
        ImagePolicyEntryTypeMaximum = 13


    IMAGE_POLICY_ENTRY_TYPE = _IMAGE_POLICY_ENTRY_TYPE
    class _IMAGE_POLICY_ID(ENUM):
        ImagePolicyIdNone = 0
        ImagePolicyIdEtw = 1
        ImagePolicyIdDebug = 2
        ImagePolicyIdCrashDump = 3
        ImagePolicyIdCrashDumpKey = 4
        ImagePolicyIdCrashDumpKeyGuid = 5
        ImagePolicyIdParentSd = 6
        ImagePolicyIdParentSdRev = 7
        ImagePolicyIdSvn = 8
        ImagePolicyIdDeviceId = 9
        ImagePolicyIdCapability = 10
        ImagePolicyIdScenarioId = 11
        ImagePolicyIdMaximum = 12


    IMAGE_POLICY_ID = _IMAGE_POLICY_ID
    class _IMAGE_POLICY_ENTRY(ctypes.Structure):
        pass


    class u(ctypes.Union):
        pass


    u._fields_ = [
        ('None', POINTER(VOID)),
        ('BoolValue', BOOLEAN),
        ('Int8Value', INT8),
        ('UInt8Value', UINT8),
        ('Int16Value', INT16),
        ('UInt16Value', UINT16),
        ('Int32Value', INT32),
        ('UInt32Value', UINT32),
        ('Int64Value', INT64),
        ('UInt64Value', UINT64),
        ('AnsiStringValue', PCSTR),
        ('UnicodeStringValue', PCWSTR),
    ]
    _IMAGE_POLICY_ENTRY.u = u
    _IMAGE_POLICY_ENTRY._fields_ = [
        ('Type', IMAGE_POLICY_ENTRY_TYPE),
        ('PolicyId', IMAGE_POLICY_ID),
        ('u', _IMAGE_POLICY_ENTRY.u),
    ]
    IMAGE_POLICY_ENTRY = _IMAGE_POLICY_ENTRY
    PCIMAGE_POLICY_ENTRY = POINTER(IMAGE_POLICY_ENTRY)
    class _IMAGE_POLICY_METADATA(ctypes.Structure):
        pass


    _IMAGE_POLICY_METADATA._fields_ = [
        ('Version', UCHAR),
        ('Reserved0', UCHAR * 7),
        ('ApplicationId', ULONGLONG),
        ('Policies', IMAGE_POLICY_ENTRY * ),
    ]
    IMAGE_POLICY_METADATA = _IMAGE_POLICY_METADATA
    PCIMAGE_POLICY_METADATA = POINTER(IMAGE_POLICY_METADATA)


    def IMAGE_POLICY_START(_ApplicationId_):
        return __pragma(const_segpush, IMAGE_POLICY_SECTION_NAME); EXTERN_C __declspecdllexport IMAGE_POLICY_METADATA IMAGE_POLICY_METADATA_NAME = { IMAGE_POLICY_METADATA_VERSION, {0}, _ApplicationId_, {


    def IMAGE_POLICY_END():
        return {ImagePolicyEntryTypeNone, ImagePolicyIdNone, NULL} } }; __pragma(const_segpop)


    def IMAGE_POLICY_BOOL(_PolicyId_, _Value_):
        return {ImagePolicyEntryTypeBool, _PolicyId_, VOID*_Value_},


    def IMAGE_POLICY_INT8(_PolicyId_, _Value_):
        return {ImagePolicyEntryTypeInt8, _PolicyId_, VOID*_Value_},


    def IMAGE_POLICY_UINT8(_PolicyId_, _Value_):
        return {ImagePolicyEntryTypeUInt8, _PolicyId_, VOID*_Value_},


    def IMAGE_POLICY_INT16(_PolicyId_, _Value_):
        return {ImagePolicyEntryTypeInt16, _PolicyId_, VOID*_Value_},


    def IMAGE_POLICY_UINT16(_PolicyId_, _Value_):
        return {ImagePolicyEntryTypeUInt16, _PolicyId_, VOID*_Value_},


    def IMAGE_POLICY_INT32(_PolicyId_, _Value_):
        return {ImagePolicyEntryTypeInt32, _PolicyId_, VOID*_Value_},


    def IMAGE_POLICY_UINT32(_PolicyId_, _Value_):
        return {ImagePolicyEntryTypeUInt32, _PolicyId_, VOID*_Value_},


    def IMAGE_POLICY_INT64(_PolicyId_, _Value_):
        return {ImagePolicyEntryTypeInt64, _PolicyId_, VOID*_Value_},


    def IMAGE_POLICY_UINT64(_PolicyId_, _Value_):
        return {ImagePolicyEntryTypeUInt64, _PolicyId_, VOID*_Value_},


    def IMAGE_POLICY_ANSI_STRING(_PolicyId_, _Value_):
        return {ImagePolicyEntryTypeAnsiString, _PolicyId_, _Value_},


    def IMAGE_POLICY_UNICODE_STRING(_PolicyId_, _Value_):
        return {ImagePolicyEntryTypeUnicodeString, _PolicyId_, _Value_},


    def IMAGE_POLICY_OVERRIDE(_PolicyId_):
        return {ImagePolicyEntryTypeOverride, _PolicyId_, 0},

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if NTDDI_VERSION >= NTDDI_WIN2K:
            # _Check_return_
            # NTSYSAPI
            # SIZE_T
            # NTAPI
            # RtlCompareMemory(
            # _In_ VOID* Source1,
            # _In_ VOID* Source2,
            # _In_ SIZE_T Length
            # );
            RtlCompareMemory = ntdll.RtlCompareMemory
            RtlCompareMemory.restype = SIZE_T        # END IF    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    if not defined(_NTTMAPI_):
        _NTTMAPI_ = 1

        if defined(__cplusplus):
            pass
        # END IF
        if _MSC_VER >= 1200:
            pass
        # END IF
        class _TRANSACTION_STATE(ENUM):
            TransactionStateNormal = 1
            TransactionStateIndoubt = 2
            TransactionStateCommittedNotify = 3


        TRANSACTION_STATE = _TRANSACTION_STATE
        class _TRANSACTION_BASIC_INFORMATION(ctypes.Structure):
            pass


        _TRANSACTION_BASIC_INFORMATION._fields_ = [
            ('TransactionId', GUID),
            ('State', ULONG),
            ('Outcome', ULONG),
        ]
        TRANSACTION_BASIC_INFORMATION = _TRANSACTION_BASIC_INFORMATION
        PTRANSACTION_BASIC_INFORMATION = POINTER(_TRANSACTION_BASIC_INFORMATION)
        class _TRANSACTIONMANAGER_BASIC_INFORMATION(ctypes.Structure):
            pass


        _TRANSACTIONMANAGER_BASIC_INFORMATION._fields_ = [
            ('TmIdentity', GUID),
            ('VirtualClock', LARGE_INTEGER),
        ]
        TRANSACTIONMANAGER_BASIC_INFORMATION = _TRANSACTIONMANAGER_BASIC_INFORMATION
        PTRANSACTIONMANAGER_BASIC_INFORMATION = POINTER(_TRANSACTIONMANAGER_BASIC_INFORMATION)
        class _TRANSACTIONMANAGER_LOG_INFORMATION(ctypes.Structure):
            pass


        _TRANSACTIONMANAGER_LOG_INFORMATION._fields_ = [
            ('LogIdentity', GUID),
        ]
        TRANSACTIONMANAGER_LOG_INFORMATION = _TRANSACTIONMANAGER_LOG_INFORMATION
        PTRANSACTIONMANAGER_LOG_INFORMATION = POINTER(_TRANSACTIONMANAGER_LOG_INFORMATION)
        class _TRANSACTIONMANAGER_LOGPATH_INFORMATION(ctypes.Structure):
            pass


        _TRANSACTIONMANAGER_LOGPATH_INFORMATION._fields_ = [
            ('LogPathLength', ULONG),
            ('LogPath', WCHAR * 1), # Variable size
        ]
        TRANSACTIONMANAGER_LOGPATH_INFORMATION = _TRANSACTIONMANAGER_LOGPATH_INFORMATION
        PTRANSACTIONMANAGER_LOGPATH_INFORMATION = POINTER(_TRANSACTIONMANAGER_LOGPATH_INFORMATION)
        class _TRANSACTIONMANAGER_RECOVERY_INFORMATION(ctypes.Structure):
            pass


        _TRANSACTIONMANAGER_RECOVERY_INFORMATION._fields_ = [
            ('LastRecoveredLsn', ULONGLONG),
        ]
        TRANSACTIONMANAGER_RECOVERY_INFORMATION = _TRANSACTIONMANAGER_RECOVERY_INFORMATION
        PTRANSACTIONMANAGER_RECOVERY_INFORMATION = POINTER(_TRANSACTIONMANAGER_RECOVERY_INFORMATION)
        class _TRANSACTION_PROPERTIES_INFORMATION(ctypes.Structure):
            pass


        _TRANSACTION_PROPERTIES_INFORMATION._fields_ = [
            ('IsolationLevel', ULONG),
            ('IsolationFlags', ULONG),
            ('Timeout', LARGE_INTEGER),
            ('Outcome', ULONG),
            ('DescriptionLength', ULONG),
            ('Description', WCHAR * 1), # Variable size
        ]
        TRANSACTION_PROPERTIES_INFORMATION = _TRANSACTION_PROPERTIES_INFORMATION
        PTRANSACTION_PROPERTIES_INFORMATION = POINTER(_TRANSACTION_PROPERTIES_INFORMATION)

        # The following info - class is intended for DTC's use only; it will be
        # deprecated, and no one else should take a dependency on it.
        class _TRANSACTION_BIND_INFORMATION(ctypes.Structure):
            pass


        _TRANSACTION_BIND_INFORMATION._fields_ = [
            ('TmHandle', HANDLE),
        ]
        TRANSACTION_BIND_INFORMATION = _TRANSACTION_BIND_INFORMATION
        PTRANSACTION_BIND_INFORMATION = POINTER(_TRANSACTION_BIND_INFORMATION)
        class _TRANSACTION_ENLISTMENT_PAIR(ctypes.Structure):
            pass


        _TRANSACTION_ENLISTMENT_PAIR._fields_ = [
            ('EnlistmentId', GUID),
            ('ResourceManagerId', GUID),
        ]
        TRANSACTION_ENLISTMENT_PAIR = _TRANSACTION_ENLISTMENT_PAIR
        PTRANSACTION_ENLISTMENT_PAIR = POINTER(_TRANSACTION_ENLISTMENT_PAIR)
        class _TRANSACTION_ENLISTMENTS_INFORMATION(ctypes.Structure):
            pass


        _TRANSACTION_ENLISTMENTS_INFORMATION._fields_ = [
            ('NumberOfEnlistments', ULONG),
            ('EnlistmentPair', TRANSACTION_ENLISTMENT_PAIR * 1), # Variable size
        ]
        TRANSACTION_ENLISTMENTS_INFORMATION = _TRANSACTION_ENLISTMENTS_INFORMATION
        PTRANSACTION_ENLISTMENTS_INFORMATION = POINTER(_TRANSACTION_ENLISTMENTS_INFORMATION)
        class _TRANSACTION_SUPERIOR_ENLISTMENT_INFORMATION(ctypes.Structure):
            pass


        _TRANSACTION_SUPERIOR_ENLISTMENT_INFORMATION._fields_ = [
            ('SuperiorEnlistmentPair', TRANSACTION_ENLISTMENT_PAIR),
        ]
        TRANSACTION_SUPERIOR_ENLISTMENT_INFORMATION = _TRANSACTION_SUPERIOR_ENLISTMENT_INFORMATION
        PTRANSACTION_SUPERIOR_ENLISTMENT_INFORMATION = POINTER(_TRANSACTION_SUPERIOR_ENLISTMENT_INFORMATION)
        class _RESOURCEMANAGER_BASIC_INFORMATION(ctypes.Structure):
            pass


        _RESOURCEMANAGER_BASIC_INFORMATION._fields_ = [
            ('ResourceManagerId', GUID),
            ('DescriptionLength', ULONG),
            ('Description', WCHAR * 1), # Variable size
        ]
        RESOURCEMANAGER_BASIC_INFORMATION = _RESOURCEMANAGER_BASIC_INFORMATION
        PRESOURCEMANAGER_BASIC_INFORMATION = POINTER(_RESOURCEMANAGER_BASIC_INFORMATION)
        class _RESOURCEMANAGER_COMPLETION_INFORMATION(ctypes.Structure):
            pass


        _RESOURCEMANAGER_COMPLETION_INFORMATION._fields_ = [
            ('IoCompletionPortHandle', HANDLE),
            ('CompletionKey', ULONG_PTR),
        ]
        RESOURCEMANAGER_COMPLETION_INFORMATION = _RESOURCEMANAGER_COMPLETION_INFORMATION
        PRESOURCEMANAGER_COMPLETION_INFORMATION = POINTER(_RESOURCEMANAGER_COMPLETION_INFORMATION)
        class _TRANSACTION_INFORMATION_CLASS(ENUM):
            TransactionBasicInformation = 1
            TransactionPropertiesInformation = 2
            TransactionEnlistmentInformation = 3
            TransactionSuperiorEnlistmentInformation = 4


        TRANSACTION_INFORMATION_CLASS = _TRANSACTION_INFORMATION_CLASS
        class _TRANSACTIONMANAGER_INFORMATION_CLASS(ENUM):
            TransactionManagerBasicInformation = 1
            TransactionManagerLogInformation = 2
            TransactionManagerLogPathInformation = 3
            TransactionManagerRecoveryInformation = 4


        TRANSACTIONMANAGER_INFORMATION_CLASS = _TRANSACTIONMANAGER_INFORMATION_CLASS
        class _RESOURCEMANAGER_INFORMATION_CLASS(ENUM):
            ResourceManagerBasicInformation = 1
            ResourceManagerCompletionInformation = 2


        RESOURCEMANAGER_INFORMATION_CLASS = _RESOURCEMANAGER_INFORMATION_CLASS
        class _ENLISTMENT_BASIC_INFORMATION(ctypes.Structure):
            pass


        _ENLISTMENT_BASIC_INFORMATION._fields_ = [
            ('EnlistmentId', GUID),
            ('TransactionId', GUID),
            ('ResourceManagerId', GUID),
        ]
        ENLISTMENT_BASIC_INFORMATION = _ENLISTMENT_BASIC_INFORMATION
        PENLISTMENT_BASIC_INFORMATION = POINTER(_ENLISTMENT_BASIC_INFORMATION)
        class _ENLISTMENT_CRM_INFORMATION(ctypes.Structure):
            pass


        _ENLISTMENT_CRM_INFORMATION._fields_ = [
            ('CrmTransactionManagerId', GUID),
            ('CrmResourceManagerId', GUID),
            ('CrmEnlistmentId', GUID),
        ]
        ENLISTMENT_CRM_INFORMATION = _ENLISTMENT_CRM_INFORMATION
        PENLISTMENT_CRM_INFORMATION = POINTER(_ENLISTMENT_CRM_INFORMATION)
        class _ENLISTMENT_INFORMATION_CLASS(ENUM):
            EnlistmentBasicInformation = 1
            EnlistmentRecoveryInformation = 2
            EnlistmentCrmInformation = 3


        ENLISTMENT_INFORMATION_CLASS = _ENLISTMENT_INFORMATION_CLASS
        class _TRANSACTION_LIST_ENTRY(ctypes.Structure):
            pass


        TRANSACTION_LIST_ENTRY = _TRANSACTION_LIST_ENTRY
        PTRANSACTION_LIST_ENTRY = POINTER(_TRANSACTION_LIST_ENTRY)
        class _TRANSACTION_LIST_INFORMATION(ctypes.Structure):
            pass


        _TRANSACTION_LIST_INFORMATION._fields_ = [
            ('NumberOfTransactions', ULONG),
            ('TransactionInformation', TRANSACTION_LIST_ENTRY * 1), # Var size
        ]
        TRANSACTION_LIST_INFORMATION = _TRANSACTION_LIST_INFORMATION
        PTRANSACTION_LIST_INFORMATION = POINTER(_TRANSACTION_LIST_INFORMATION)

        # Types of objects known to the kernel transaction manager.
        class _KTMOBJECT_TYPE(ENUM):
            KTMOBJECT_TRANSACTION = 1
            KTMOBJECT_TRANSACTION_MANAGER = 2
            KTMOBJECT_RESOURCE_MANAGER = 3
            KTMOBJECT_ENLISTMENT = 4
            KTMOBJECT_INVALID = 5


        KTMOBJECT_TYPE = _KTMOBJECT_TYPE
        PKTMOBJECT_TYPE = POINTER(_KTMOBJECT_TYPE)

        # KTMOBJECT_CURSOR
        # Used by NtEnumerateTransactionObject to enumerate a transaction
        # object namespace (e.g. enlistments in a resource manager).
        class _KTMOBJECT_CURSOR(ctypes.Structure):
            pass


        _KTMOBJECT_CURSOR._fields_ = [
            ('LastQuery', GUID), #
            ('ObjectIdCount', ULONG), #
            ('ObjectIds', GUID * 1), #
        ]
        KTMOBJECT_CURSOR = _KTMOBJECT_CURSOR
        PKTMOBJECT_CURSOR = POINTER(_KTMOBJECT_CURSOR)

        # Nt level transaction manager API calls
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   NTDDI_VERSION >= NTDDI_VISTA
        if _MSC_VER >= 1200:
            pass
        # END IF
        if defined(__cplusplus):
            pass
        # END IF    # END IF   _NTTMAPI_
    if not defined(FIELD_OFFSET):
        pass
    # END IF
    if not defined(FIELD_SIZE):
        pass
    # END IF
    if defined (_WIN64):
        pass
    else:
        pass
    # END IF
    if DBG:
        pass
    else:
        pass
    # END IF
    # Define General Lookaside and supporting types here
    enum = _Enum_is_bitflag_
    _POOL_TYPE = _Enum_is_bitflag_
    POOL_TYPE = _Enum_is_bitflag_
    PALLOCATE_FUNCTION = POINTER(ALLOCATE_FUNCTION)
    PFREE_FUNCTION = POINTER(FREE_FUNCTION)
    PLOOKASIDE_LIST_EX = POINTER(_LOOKASIDE_LIST_EX)

    PALLOCATE_FUNCTION_EX = POINTER(ALLOCATE_FUNCTION_EX)
    PFREE_FUNCTION_EX = POINTER(FREE_FUNCTION_EX)
    if not defined(_WIN64) and (defined(_NTDDK_) or defined(_NTIFS_) or defined(_NDIS_)):
        LOOKASIDE_ALIGN = 1
    else:
        LOOKASIDE_ALIGN = DECLSPEC_CACHEALIGN
    # END IF
    # The goal here is to end up with two structure types that are identical
    # except
    # for the fact that one (GENERAL_LOOKASIDE) is cache aligned, and the other
    # (GENERAL_LOOKASIDE_POOL) is merely naturally aligned.
    # An anonymous structure element would do the trick except that C + +
    # can't handle
    # such complex syntax, so we're stuck with this macro technique.
    GENERAL_LOOKASIDE_LAYOUT = (
        union [                                                 SLIST_HEADER ListHead;                              SINGLE_LIST_ENTRY SingleListHead;               ] DUMMYUNIONNAME;                                   USHORT Depth;                                       USHORT MaximumDepth;                                ULONG TotalAllocates;                               union [                                                 ULONG AllocateMisses;                               ULONG AllocateHits;                             ] DUMMYUNIONNAME2;                                                                                      ULONG TotalFrees;                                   union [                                                 ULONG FreeMisses;                                   ULONG FreeHits;                                 ] DUMMYUNIONNAME3;                                                                                      POOL_TYPE Type;                                     ULONG Tag;                                          ULONG Size;                                         union [                                                 PALLOCATE_FUNCTION_EX AllocateEx;                   PALLOCATE_FUNCTION Allocate;                    ] DUMMYUNIONNAME4;                                                                                      union [                                                 PFREE_FUNCTION_EX FreeEx;                           PFREE_FUNCTION Free;                            ] DUMMYUNIONNAME5;                                                                                      LIST_ENTRY ListEntry;                               ULONG LastTotalAllocates;                           union [                                                 ULONG LastAllocateMisses;                           ULONG LastAllocateHits;                         ] DUMMYUNIONNAME6;                                  ULONG Future[2];
    )

    # GENERAL_LOOKASIDE is a cache aligned type, typically shared between
    # multiple processors

    if _MSC_VER >= 1200:
        pass
    # END IF
    class _GENERAL_LOOKASIDE(LOOKASIDE_ALIGN):
        pass


    GENERAL_LOOKASIDE = _GENERAL_LOOKASIDE
    PGENERAL_LOOKASIDE = POINTER(GENERAL_LOOKASIDE)
    if _MSC_VER >= 1200:
        pass
    # END IF
    # GENERAL_LOOKASIDE_POOL is the same layout as GENERAL_LOOKASIDE but is
    # not cacheblock aligned, for use in cases where access is limited to a
    # single processor
    class _GENERAL_LOOKASIDE_POOL(ctypes.Structure):
        pass


    GENERAL_LOOKASIDE_POOL = _GENERAL_LOOKASIDE_POOL
    PGENERAL_LOOKASIDE_POOL = POINTER(_GENERAL_LOOKASIDE_POOL)

    # The above two structures should have identical layouts. A few spot -
    # checks
    # just to make sure.


    def LOOKASIDE_CHECK(f):
        return C_ASSERT(FIELD_OFFSETGENERAL_LOOKASIDE,f == FIELD_OFFSETGENERAL_LOOKASIDE_POOL,f)

    # Kernel definitions that need to be here for forward reference purposes
    # Processor modes.
    KPROCESSOR_MODE = CCHAR


    class _MODE(ENUM):
        KernelMode = 1
        UserMode = 2
        MaximumMode = 3


    MODE = _MODE
    PKSYNCHRONIZE_ROUTINE = POINTER(KSYNCHRONIZE_ROUTINE)
    class _KAPC(ctypes.Structure):
        pass


    _KAPC._fields_ = [
        ('Type', UCHAR),
        ('SpareByte0', UCHAR),
        ('Size', UCHAR),
        ('SpareByte1', UCHAR),
        ('SpareLong0', ULONG),
        ('Thread', POINTER(_KTHREAD)),
        ('ApcListEntry', LIST_ENTRY),
        ('Reserved', PVOID * 3),
        ('NormalContext', PVOID),
        ('SystemArgument1', PVOID),
        ('SystemArgument2', PVOID),
        ('ApcStateIndex', CCHAR),
        ('ApcMode', KPROCESSOR_MODE),
        ('Inserted', BOOLEAN),
    ]
    KAPC = _KAPC
    PKAPC = POINTER(_KAPC)
    PRKAPC = POINTER(_KAPC)
    KAPC_OFFSET_TO_SPARE_BYTE0 = FIELD_OFFSET(KAPC, SpareByte0)
    KAPC_OFFSET_TO_SPARE_BYTE1 = FIELD_OFFSET(KAPC, SpareByte1)
    KAPC_OFFSET_TO_SPARE_LONG = FIELD_OFFSET(KAPC, SpareLong0)
    KAPC_OFFSET_TO_SYSTEMARGUMENT1 = FIELD_OFFSET(KAPC, SystemArgument1)
    KAPC_OFFSET_TO_SYSTEMARGUMENT2 = FIELD_OFFSET(KAPC, SystemArgument2)
    KAPC_OFFSET_TO_APCSTATEINDEX = FIELD_OFFSET(KAPC, ApcStateIndex)
    KAPC_ACTUAL_LENGTH = (
        FIELD_OFFSET(KAPC,
        Inserted) + ctypes.sizeof(BOOLEAN),
    )

    # DPC routine
    _KDPC = struct

    PKDEFERRED_ROUTINE = POINTER(KDEFERRED_ROUTINE)

    # Define DPC importance.
    # LowImportance - Queue DPC at end of target DPC queue.
    # MediumImportance - Queue DPC at end of target DPC queue.
    # MediumHighImportance - Queue DPC at end of target DPC queue.
    # HighImportance - Queue DPC at front of target DPC DPC queue.
    # If there is currently a DPC active on the target processor, or a DPC
    # interrupt has already been requested on the target processor when a
    # DPC is queued, then no further action is necessary. The DPC will be
    # executed on the target processor when its queue entry is processed.
    # If there is not a DPC active on the target processor and a DPC interrupt
    # has not been requested on the target processor, then the exact treatment
    # of the DPC is dependent on whether the host system is a UP system or an
    # MP system.
    # UP system.
    # If the DPC is not of low importance, the current DPC queue depth
    # is greater than the maximum target depth, or current DPC request rate is
    # less the minimum target rate, then a DPC interrupt is requested on the
    # host processor and the DPC will be processed when the interrupt occurs.
    # Otherwise, no DPC interrupt is requested and the DPC execution will be
    # delayed until the DPC queue depth is greater that the target depth or the
    # minimum DPC rate is less than the target rate.
    # MP system.
    # If the DPC is being queued to another processor and the depth of the DPC
    # queue on the target processor is greater than the maximum target depth or
    # the DPC is of medium high or high importance, then a DPC interrupt is
    # requested on the target processor and the DPC will be processed when the
    # Interrupt occurs. Otherwise, the DPC execution will be delayed on the
    # target
    # processor until the DPC queue depth on the target processor is greater
    # that
    # the maximum target depth or the minimum DPC rate on the target processor
    # is
    # less than the target minimum rate.
    # If the DPC is being queued to the current processor and the DPC is not of
    # low importance, the current DPC queue depth is greater than the maximum
    # target depth, or the minimum DPC rate is less than the minimum target
    # rate,
    # then a DPC interrupt is request on the current processor and the DPV will
    # be processed when the interrupt occurs. Otherwise, no DPC interrupt is
    # requested and the DPC execution will be delayed until the DPC queue depth
    # is greater that the target depth or the minimum DPC rate is less than the
    # target rate.


    class _KDPC_IMPORTANCE(ENUM):
        LowImportance = 1
        MediumImportance = 2
        HighImportance = 3
        MediumHighImportance = 4


    KDPC_IMPORTANCE = _KDPC_IMPORTANCE

    # Define DPC type indices.
    DPC_NORMAL = 0
    DPC_THREADED = 1

    # Deferred Procedure Call (DPC) object


    def ASSERT_DPC(Object):
        return NT_ASSERT(Object - >Type == 0) or (Object - >Type == DpcObject) or (Object - >Type == ThreadedDpcObject)
    class _KDPC(ctypes.Structure):
        pass


    class DUMMYUNIONNAME(ctypes.Structure):
        pass


    class DUMMYSTRUCTNAME(ctypes.Structure):
        pass


    DUMMYSTRUCTNAME._fields_ = [
        ('Type', UCHAR),
        ('Importance', UCHAR),
        ('USHORT Number', volatile),
    ]
    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('TargetInfoAsULONG', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]
    _KDPC.DUMMYUNIONNAME = DUMMYUNIONNAME
    _KDPC._fields_ = [
        ('DUMMYUNIONNAME', _KDPC.DUMMYUNIONNAME),
        ('DpcListEntry', SINGLE_LIST_ENTRY),
        ('ProcessorHistory', KAFFINITY),
        ('DeferredRoutine', PKDEFERRED_ROUTINE),
        ('DeferredContext', PVOID),
        ('SystemArgument1', PVOID),
        ('SystemArgument2', PVOID),
        ('PVOID DpcData', __volatile),
    ]
    KDPC = _KDPC
    PKDPC = POINTER(_KDPC)
    PRKDPC = POINTER(_KDPC)

    if defined(_X86_):

        # i386 Specific portions of Mm component.
        # Define the page size for the Intel 386 as 4096 (0x1000).
        PAGE_SIZE = 0x1000

        # Define the number of trailing zeros in a page aligned virtual
        # address.
        # This is used as the shift count when shifting virtual addresses to
        # virtual page numbers.
        PAGE_SHIFT = 12L
    elif defined(_AMD64_):

        # AMD64 Specific portions of Mm component.
        # Define the page size for the AMD64 as 4096 (0x1000).
        PAGE_SIZE = 0x1000

        # Define the number of trailing zeros in a page aligned virtual
        # address.
        # This is used as the shift count when shifting virtual addresses to
        # virtual page numbers.
        PAGE_SHIFT = 12L
    elif defined(_ARM64_):

        # ARM Specific portions of Mm component.
        # Define the page size for the ARM64 as 4096 (0x1000).
        PAGE_SIZE = 0x1000

        # Define the number of trailing zeros in a page aligned virtual
        # address.
        # This is used as the shift count when shifting virtual addresses to
        # virtual page numbers.
        PAGE_SHIFT = 12L
    elif defined(_ARM_):

        # ARM Specific portions of Mm component.
        # Define the page size for the ARM as 4096 (0x1000).
        PAGE_SIZE = 0x1000

        # Define the number of trailing zeros in a page aligned virtual
        # address.
        # This is used as the shift count when shifting virtual addresses to
        # virtual page numbers.
        PAGE_SHIFT = 12L
    # END IF
    # I/O system definitions.
    # Define a Memory Descriptor List (MDL)
    # An MDL describes pages in a virtual buffer in terms of physical pages.
    # The
    # pages associated with the buffer are described in an array that is
    # allocated
    # just after the MDL header structure itself.
    # One simply calculates the base of the array by adding one to the base
    # MDL pointer:
    # Pages = (PPFN_NUMBER) (Mdl + 1);
    # Notice that while in the context of the subject thread, the base virtual
    # address of a buffer mapped by an MDL may be referenced using the
    # following:
    # Mdl - >StartVa | Mdl - >ByteOffset
    # Use _Inexpressible_ until the definition can be fixed
    # (PAGE_SIZE may not be
    # defined at this point).
    Process = POINTER(_EPROCESS)

    MDL = _Readable_bytes_(_Inexpressible_(polymorphism))
    PMDLX = POINTER(_Readable_bytes_(_Inexpressible_(polymorphism)))
    MDL_MAPPED_TO_SYSTEM_VA = 0x0001
    MDL_PAGES_LOCKED = 0x0002
    MDL_SOURCE_IS_NONPAGED_POOL = 0x0004
    MDL_ALLOCATED_FIXED_SIZE = 0x0008
    MDL_PARTIAL = 0x0010
    MDL_PARTIAL_HAS_BEEN_MAPPED = 0x0020
    MDL_IO_PAGE_READ = 0x0040
    MDL_WRITE_OPERATION = 0x0080
    MDL_LOCKED_PAGE_TABLES = 0x0100
    MDL_PARENT_MAPPED_SYSTEM_VA = MDL_LOCKED_PAGE_TABLES
    MDL_FREE_EXTRA_PTES = 0x0200
    MDL_DESCRIBES_AWE = 0x0400
    MDL_IO_SPACE = 0x0800
    MDL_NETWORK_HEADER = 0x1000
    MDL_MAPPING_CAN_FAIL = 0x2000
    MDL_PAGE_CONTENTS_INVARIANT = 0x4000
    MDL_ALLOCATED_MUST_SUCCEED = MDL_PAGE_CONTENTS_INVARIANT
    MDL_INTERNAL = 0x8000
    MDL_MAPPING_FLAGS = (
        MDL_MAPPED_TO_SYSTEM_VA |
        MDL_PAGES_LOCKED |
        MDL_SOURCE_IS_NONPAGED_POOL |
        MDL_PARTIAL_HAS_BEEN_MAPPED |
        MDL_PARENT_MAPPED_SYSTEM_VA |
        MDL_SYSTEM_VA |
        MDL_IO_SPACE
    )

    # switch to PREFast or DBG when appropriate

    if defined(_PREFAST_):


        def PAGED_CODE():
            return __PREfastPagedCode;


        def PAGED_CODE_LOCKED():
            return __PREfastPagedCodeLocked;

    elif DBG:
        if NTDDI_VERSION >= NTDDI_VISTA:


            def PAGED_ASSERT(exp):
                return NT_ASSERT exp
        else:


            def PAGED_ASSERT(exp):
                return ASSERT exp
        # END IF


        def PAGED_CODE():
            return PAGED_ASSERT(KeGetCurrentIrql <= APC_LEVEL);


        def PAGED_CODE_LOCKED():
            return NOP_FUNCTION;
    else:


        def PAGED_CODE():
            return NOP_FUNCTION;


        def PAGED_CODE_LOCKED():
            return NOP_FUNCTION;
    # END IF
    NTKERNELAPI = DECLSPEC_IMPORT

    if defined(_X86_) and not defined(_NTHAL_):
        _DECL_HAL_KE_IMPORT = DECLSPEC_IMPORT
    elif defined(_X86_):
        _DECL_HAL_KE_IMPORT = 1
    else:
        _DECL_HAL_KE_IMPORT = NTKERNELAPI
    # END IF

    if not defined(_NTHALDLL_) and not defined(_BLDR_):
        NTHALAPI = DECLSPEC_IMPORT
    else:
        NTHALAPI = 1
    # END IF
    # Common dispatcher object header
    # N.B. The size field contains the number of dwords in the structure.

    if defined(_X86_):
        KENCODED_TIMER_PROCESSOR = 1
    # END IF
    TIMER_TOLERABLE_DELAY_BITS = 6
    TIMER_EXPIRED_INDEX_BITS = 6
    TIMER_PROCESSOR_INDEX_BITS = 5
    class _DISPATCHER_HEADER(ctypes.Structure):
        pass


    class DUMMYUNIONNAME(ctypes.Structure):
        pass


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('LONG Lock', volatile),
        ('LockNV', LONG),
    ]
    DUMMYUNIONNAME.DUMMYUNIONNAME = DUMMYUNIONNAME
    class DUMMYSTRUCTNAME(ctypes.Structure):
        pass


    DUMMYSTRUCTNAME._fields_ = [
        ('Type', UCHAR), # All (accessible via KOBJECT_TYPE)
        ('Signalling', UCHAR),
        ('Size', UCHAR),
        ('Reserved1', UCHAR),
    ]
    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    class DUMMYSTRUCTNAME2(ctypes.Structure):
        pass


    class _Struct_1(ctypes.Structure):
        pass


    class DUMMYSTRUCTNAME(ctypes.Structure):
        pass


    DUMMYSTRUCTNAME._fields_ = [
        ('Absolute', UCHAR, 1),
        ('Wake', UCHAR, 1),
        ('EncodedTolerableDelay', UCHAR, TIMER_TOLERABLE_DELAY_BITS),
    ]
    _Struct_1.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _Struct_1._fields_ = [
        ('TimerControlFlags', UCHAR),
        ('DUMMYSTRUCTNAME', _Struct_1.DUMMYSTRUCTNAME),
    ]
    DUMMYSTRUCTNAME2._Struct_1 = _Struct_1
    class DUMMYUNIONNAME(ctypes.Structure):
        pass


    class DUMMYSTRUCTNAME(ctypes.Structure):
        pass


    DUMMYSTRUCTNAME._fields_ = [
            ('Index', UCHAR, TIMER_EXPIRED_INDEX_BITS),
            ('Index', UCHAR, 1),
            ('Processor', UCHAR, TIMER_PROCESSOR_INDEX_BITS),
        ('Inserted', UCHAR, 1),
        ('UCHAR Expired', volatile, 1),
    ]
    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('TimerMiscFlags', UCHAR),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]
    DUMMYSTRUCTNAME2.DUMMYUNIONNAME = DUMMYUNIONNAME
    DUMMYSTRUCTNAME2._anonymous_ = (
        '_Struct_1',
    )
    DUMMYSTRUCTNAME2._fields_ = [
        ('TimerType', UCHAR),
        ('_Struct_1', DUMMYSTRUCTNAME2._Struct_1),
        ('Hand', UCHAR),
        ('DUMMYUNIONNAME', DUMMYSTRUCTNAME2.DUMMYUNIONNAME),
    ]
    DUMMYUNIONNAME.DUMMYSTRUCTNAME2 = DUMMYSTRUCTNAME2
    class DUMMYSTRUCTNAME3(ctypes.Structure):
        pass


    class DUMMYUNIONNAME(ctypes.Structure):
        pass


    class DUMMYSTRUCTNAME(ctypes.Structure):
        pass


    DUMMYSTRUCTNAME._fields_ = [
        ('Timer2Inserted', UCHAR, 1),
        ('Timer2Expiring', UCHAR, 1),
        ('Timer2CancelPending', UCHAR, 1),
        ('Timer2SetPending', UCHAR, 1),
        ('Timer2Running', UCHAR, 1),
        ('Timer2Disabled', UCHAR, 1),
        ('Timer2ReservedFlags', UCHAR, 2),
    ]
    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Timer2Flags', UCHAR),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]
    DUMMYSTRUCTNAME3.DUMMYUNIONNAME = DUMMYUNIONNAME
    DUMMYSTRUCTNAME3._fields_ = [
        ('Timer2Type', UCHAR),
        ('DUMMYUNIONNAME', DUMMYSTRUCTNAME3.DUMMYUNIONNAME),
        ('Timer2ComponentId', UCHAR),
        ('Timer2RelativeId', UCHAR),
    ]
    DUMMYUNIONNAME.DUMMYSTRUCTNAME3 = DUMMYSTRUCTNAME3
    class DUMMYSTRUCTNAME4(ctypes.Structure):
        pass


    class DUMMYUNIONNAME(ctypes.Structure):
        pass


    class DUMMYSTRUCTNAME(ctypes.Structure):
        pass


    DUMMYSTRUCTNAME._fields_ = [
        ('Abandoned', UCHAR, 1),
        ('DisableIncrement', UCHAR, 1),
        ('QueueReservedControlFlags', UCHAR, 6),
    ]
    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('QueueControlFlags', UCHAR),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]
    DUMMYSTRUCTNAME4.DUMMYUNIONNAME = DUMMYUNIONNAME
    DUMMYSTRUCTNAME4._fields_ = [
        ('QueueType', UCHAR),
        ('DUMMYUNIONNAME', DUMMYSTRUCTNAME4.DUMMYUNIONNAME),
        ('QueueSize', UCHAR),
        ('QueueReserved', UCHAR),
    ]
    DUMMYUNIONNAME.DUMMYSTRUCTNAME4 = DUMMYSTRUCTNAME4
    class DUMMYSTRUCTNAME5(ctypes.Structure):
        pass


    class DUMMYUNIONNAME(ctypes.Structure):
        pass


    class DUMMYSTRUCTNAME(ctypes.Structure):
        pass


    DUMMYSTRUCTNAME._fields_ = [
        ('CycleProfiling', UCHAR, 1),
        ('CounterProfiling', UCHAR, 1),
        ('GroupScheduling', UCHAR, 1),
        ('AffinitySet', UCHAR, 1),
        ('Tagged', UCHAR, 1),
        ('EnergyProfiling', UCHAR, 1),
        ('SchedulerAssist', UCHAR, 1),
            ('ThreadReservedControlFlags', UCHAR, 1),
            ('Instrumented', UCHAR, 1),
    ]
    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('ThreadControlFlags', UCHAR),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]
    DUMMYSTRUCTNAME5.DUMMYUNIONNAME = DUMMYUNIONNAME
    class DUMMYUNIONNAME2(ctypes.Structure):
        pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('ActiveDR7', BOOLEAN, 1),
            ('Instrumented', BOOLEAN, 1),
            ('Minimal', BOOLEAN, 1),
            ('Reserved4', BOOLEAN, 3),
            ('UmsScheduled', BOOLEAN, 1),
            ('UmsPrimary', BOOLEAN, 1),
        ]
        DUMMYUNIONNAME2.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME2._fields_ = [
        ('DebugActive', UCHAR),
            ('DUMMYSTRUCTNAME', DUMMYUNIONNAME2.DUMMYSTRUCTNAME),
    ]
    DUMMYSTRUCTNAME5.DUMMYUNIONNAME2 = DUMMYUNIONNAME2
    DUMMYSTRUCTNAME5._fields_ = [
        ('ThreadType', UCHAR),
        ('ThreadReserved', UCHAR),
        ('DUMMYUNIONNAME', DUMMYSTRUCTNAME5.DUMMYUNIONNAME),
        ('DUMMYUNIONNAME2', DUMMYSTRUCTNAME5.DUMMYUNIONNAME2),
    ]
    DUMMYUNIONNAME.DUMMYSTRUCTNAME5 = DUMMYSTRUCTNAME5
    class DUMMYSTRUCTNAME6(ctypes.Structure):
        pass


    DUMMYSTRUCTNAME6._fields_ = [
        ('MutantType', UCHAR),
        ('MutantSize', UCHAR),
        ('DpcActive', BOOLEAN),
        ('MutantReserved', UCHAR),
    ]
    DUMMYUNIONNAME.DUMMYSTRUCTNAME6 = DUMMYSTRUCTNAME6
    DUMMYUNIONNAME._fields_ = [
        ('DUMMYUNIONNAME', DUMMYUNIONNAME.DUMMYUNIONNAME),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME), # Events, Semaphores, Gates, etc.
        ('DUMMYSTRUCTNAME2', DUMMYUNIONNAME.DUMMYSTRUCTNAME2), # Timer
        ('DUMMYSTRUCTNAME3', DUMMYUNIONNAME.DUMMYSTRUCTNAME3), # Timer2
        ('DUMMYSTRUCTNAME4', DUMMYUNIONNAME.DUMMYSTRUCTNAME4), # Queue
        ('DUMMYSTRUCTNAME5', DUMMYUNIONNAME.DUMMYSTRUCTNAME5), # Thread
        ('DUMMYSTRUCTNAME6', DUMMYUNIONNAME.DUMMYSTRUCTNAME6), # Mutant
    ]
    _DISPATCHER_HEADER.DUMMYUNIONNAME = DUMMYUNIONNAME
    _DISPATCHER_HEADER._fields_ = [
        ('DUMMYUNIONNAME', _DISPATCHER_HEADER.DUMMYUNIONNAME),
        ('SignalState', LONG), # Object lock
        ('WaitListHead', LIST_ENTRY), # Object lock
    ]
    DISPATCHER_HEADER = _DISPATCHER_HEADER
    PDISPATCHER_HEADER = POINTER(_DISPATCHER_HEADER)

    if not defined(KENCODED_TIMER_PROCESSOR):
        pass
    else:
        pass
    # END IF
    if not defined(_X86_):
        pass
    else:
        pass
    # END IF
    if not defined(_X86_):
        pass
    # END IF
    # Event object
    class _KEVENT(ctypes.Structure):
        pass


    _KEVENT._fields_ = [
        ('Header', DISPATCHER_HEADER),
    ]
    KEVENT = _KEVENT
    PKEVENT = POINTER(_KEVENT)
    PRKEVENT = POINTER(_KEVENT)

    # Gate object
    # N.B. Gate object services allow the specification of synchronization
    # events. This allows fast mutex to be transparently replaced with
    # gates.
    class _KGATE(ctypes.Structure):
        pass


    _KGATE._fields_ = [
        ('Header', DISPATCHER_HEADER),
    ]
    KGATE = _KGATE
    PKGATE = POINTER(_KGATE)

    # Timer object
    # N.B. The period field must be the last member of this structure.
    class _KTIMER(ctypes.Structure):
        pass


    _KTIMER._fields_ = [
        ('Header', DISPATCHER_HEADER),
        ('DueTime', ULARGE_INTEGER),
        ('TimerListEntry', LIST_ENTRY),
        ('Dpc', POINTER(_KDPC)),
            ('Processor', ULONG),
        ('Period', ULONG),
    ]
    KTIMER = _KTIMER
    PKTIMER = POINTER(_KTIMER)
    PRKTIMER = POINTER(_KTIMER)
    if not defined(KENCODED_TIMER_PROCESSOR):
        pass
    # END IF
    KTIMER_ACTUAL_LENGTH = (
        FIELD_OFFSET(KTIMER,
        Period) + ctypes.sizeof(LONG),
    )


    class _LOCK_OPERATION(ENUM):
        IoReadAccess = 1
        IoWriteAccess = 2
        IoModifyAccess = 3


    LOCK_OPERATION = _LOCK_OPERATION
    class _FAST_MUTEX(ctypes.Structure):
        pass


    _FAST_MUTEX._fields_ = [
        ('Count', LONG),
        ('Owner', PVOID),
        ('Contention', ULONG),
        ('Event', KEVENT),
        ('OldIrql', ULONG),
    ]
    FAST_MUTEX = _FAST_MUTEX
    PFAST_MUTEX = POINTER(_FAST_MUTEX)
    KGUARDED_MUTEX = _FAST_MUTEX
    PKGUARDED_MUTEX = POINTER(_FAST_MUTEX)
    if defined(_X86_):

        # Types to use to contain PFNs and their counts.
        PFN_COUNT = ULONG
        SPFN_NUMBER = LONG
        PSPFN_NUMBER = POINTER(LONG)
        PFN_NUMBER = ULONG
        PPFN_NUMBER = POINTER(ULONG)

        # Define maximum size of flush multiple TB request.
        FLUSH_MULTIPLE_MAXIMUM = 32

        # Indicate that the i386 compiler supports the pragma textout
        # construct.
        ALLOC_PRAGMA = 1

        # Indicate that the i386 compiler supports the DATA_SEG("INIT") and
        # DATA_SEG("PAGE") pragmas
        ALLOC_DATA_PRAGMA = 1

        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF


        def KeLowerIrql(a):
            return KfLowerIrqla


        def KeRaiseIrql(a, b):
            return *b = KfRaiseIrqla

        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
        # I/O space read and write macros.
        # These have to be actual functions on the 386, because we need
        # to use assembler, but cannot return a value if we inline it.
        # The READ/WRITE_REGISTER_* calls manipulate I/O registers in MEMORY
        # space.
        # (Use x86 move instructions, with LOCK prefix to force correct behavior
        #
        # w.r.t. caches and write buffers.)
        # The READ/WRITE_PORT_* calls manipulate I/O registers in PORT space.
        # (Use x86 in/out instructions.)
        # Get data cache fill size.
        if PRAGMA_DEPRECATED_DDK:
            pass
        # END IF


        def KeGetDcacheFillSize():
            return 1L

        if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
            pass
        else:


            def KeFlushIoBuffers(Mdl, ReadOperation, DmaOperation):
                return 1
        # END IF


        def ExAcquireSpinLock(Lock, OldIrql):
            return KeAcquireSpinLockLock, OldIrql


        def ExReleaseSpinLock(Lock, OldIrql):
            return KeReleaseSpinLockLock, OldIrql


        def ExAcquireSpinLockAtDpcLevel(Lock):
            return KeAcquireSpinLockAtDpcLevelLock


        def ExReleaseSpinLockFromDpcLevel(Lock):
            return KeReleaseSpinLockFromDpcLevelLock


        def KeQueryTickCount(CurrentCount):
            return { KSYSTEM_TIME volatile *_TickCount = *PKSYSTEM_TIME *( & KeTickCount); for ;; { CurrentCount - >HighPart = _TickCount - >High1Time; CurrentCount - >LowPart = _TickCount - >LowPart; if (CurrentCount - >HighPart == _TickCount - >High2Time) break; YieldProcessor; } }

        # The non - volatile 387 state
        class _KFLOATING_SAVE(ctypes.Structure):
            pass


        _KFLOATING_SAVE._fields_ = [
            ('ControlWord', ULONG),
            ('StatusWord', ULONG),
            ('ErrorOffset', ULONG),
            ('ErrorSelector', ULONG),
            ('DataOffset', ULONG), # Not used in wdm
            ('DataSelector', ULONG),
            ('Spare0', ULONG),
            ('Spare1', ULONG), # Not used in wdm
        ]
        KFLOATING_SAVE = _KFLOATING_SAVE
        PKFLOATING_SAVE = POINTER(_KFLOATING_SAVE)

        # Structure of AMD cache information returned by CPUID instruction
        class _AMD_L1_CACHE_INFO(ctypes.Union):
            pass


        class _Struct_1(ctypes.Structure):
            pass


        _Struct_1._fields_ = [
            ('LineSize', UCHAR),
            ('LinesPerTag', UCHAR),
            ('Associativity', UCHAR),
            ('Size', UCHAR),
        ]
        _AMD_L1_CACHE_INFO._Struct_1 = _Struct_1
        _AMD_L1_CACHE_INFO._anonymous_ = (
            '_Struct_1',
        )
        _AMD_L1_CACHE_INFO._fields_ = [
            ('_Struct_1', _AMD_L1_CACHE_INFO._Struct_1),
        ]
        AMD_L1_CACHE_INFO = _AMD_L1_CACHE_INFO
        PAMD_L1_CACHE_INFO = POINTER(_AMD_L1_CACHE_INFO)
        class _AMD_L2_CACHE_INFO(ctypes.Union):
            pass


        class _Struct_2(ctypes.Structure):
            pass


        _Struct_2._fields_ = [
            ('LineSize', UCHAR),
            ('LinesPerTag', UCHAR, 4),
            ('Associativity', UCHAR, 4),
            ('Size', USHORT),
        ]
        _AMD_L2_CACHE_INFO._Struct_2 = _Struct_2
        _AMD_L2_CACHE_INFO._anonymous_ = (
            '_Struct_2',
        )
        _AMD_L2_CACHE_INFO._fields_ = [
            ('_Struct_2', _AMD_L2_CACHE_INFO._Struct_2),
        ]
        AMD_L2_CACHE_INFO = _AMD_L2_CACHE_INFO
        PAMD_L2_CACHE_INFO = POINTER(_AMD_L2_CACHE_INFO)
        class _AMD_L3_CACHE_INFO(ctypes.Union):
            pass


        class _Struct_3(ctypes.Structure):
            pass


        _Struct_3._fields_ = [
            ('LineSize', UCHAR),
            ('LinesPerTag', UCHAR, 4),
            ('Associativity', UCHAR, 4),
            ('Reserved', USHORT, 2),
            ('Size', USHORT, 14),
        ]
        _AMD_L3_CACHE_INFO._Struct_3 = _Struct_3
        _AMD_L3_CACHE_INFO._anonymous_ = (
            '_Struct_3',
        )
        _AMD_L3_CACHE_INFO._fields_ = [
            ('_Struct_3', _AMD_L3_CACHE_INFO._Struct_3),
        ]
        AMD_L3_CACHE_INFO = _AMD_L3_CACHE_INFO
        PAMD_L3_CACHE_INFO = POINTER(_AMD_L3_CACHE_INFO)

        # Structure of Intel deterministic cache information returned by
        # CPUID instruction


        class _INTEL_CACHE_TYPE(ENUM):
            IntelCacheNull = 1
            IntelCacheData = 2
            IntelCacheInstruction = 3
            IntelCacheUnified = 4
            IntelCacheRam = 5
            IntelCacheTrace = 6


        INTEL_CACHE_TYPE = _INTEL_CACHE_TYPE
        class INTEL_CACHE_INFO_EAX(ctypes.Union):
            pass


        class _Struct_4(ctypes.Structure):
            pass


        _Struct_4._fields_ = [
            ('Type', INTEL_CACHE_TYPE, 5),
            ('Level', ULONG, 3),
            ('SelfInitializing', ULONG, 1),
            ('FullyAssociative', ULONG, 1),
            ('Reserved', ULONG, 4),
            ('ThreadsSharing', ULONG, 12),
            ('ProcessorCores', ULONG, 6),
        ]
        INTEL_CACHE_INFO_EAX._Struct_4 = _Struct_4
        INTEL_CACHE_INFO_EAX._anonymous_ = (
            '_Struct_4',
        )
        INTEL_CACHE_INFO_EAX._fields_ = [
            ('_Struct_4', INTEL_CACHE_INFO_EAX._Struct_4),
        ]
        PINTEL_CACHE_INFO_EAX = POINTER(INTEL_CACHE_INFO_EAX)
        class INTEL_CACHE_INFO_EBX(ctypes.Union):
            pass


        class _Struct_5(ctypes.Structure):
            pass


        _Struct_5._fields_ = [
            ('LineSize', ULONG, 12),
            ('Partitions', ULONG, 10),
            ('Associativity', ULONG, 10),
        ]
        INTEL_CACHE_INFO_EBX._Struct_5 = _Struct_5
        INTEL_CACHE_INFO_EBX._anonymous_ = (
            '_Struct_5',
        )
        INTEL_CACHE_INFO_EBX._fields_ = [
            ('_Struct_5', INTEL_CACHE_INFO_EBX._Struct_5),
        ]
        PINTEL_CACHE_INFO_EBX = POINTER(INTEL_CACHE_INFO_EBX)


        def MmGetProcedureAddress(Address):
            return Address


        def MmLockPagableCodeSection(Address):
            return MmLockPagableDataSectionAddress

        # Result type definition for i386. (Machine specific enumerate type
        # which is return type for portable exinterlockedincrement/decrement
        # procedures.) In general, you should use the enumerated type defined
        # in ex.h instead of directly referencing these constants.
        # Flags loaded into AH by LAHF instruction
        EFLAG_SIGN = 0x8000
        EFLAG_ZERO = 0x4000
        EFLAG_SELECT = EFLAG_SIGN | EFLAG_ZERO
        RESULT_NEGATIVE = (EFLAG_SIGN & ~EFLAG_ZERO) & EFLAG_SELECT
        RESULT_ZERO = (~EFLAG_SIGN & EFLAG_ZERO) & EFLAG_SELECT
        RESULT_POSITIVE = (~EFLAG_SIGN & ~EFLAG_ZERO) & EFLAG_SELECT

        # Convert various portable ExInterlock APIs into their architectural
        # equivalents.

        if PRAGMA_DEPRECATED_DDK:
            pass
        # END IF


        def ExInterlockedIncrementLong(Addend, Lock):
            return Exfi386InterlockedIncrementLongAddend


        def ExInterlockedDecrementLong(Addend, Lock):
            return Exfi386InterlockedDecrementLongAddend


        def ExInterlockedExchangeULONG(Target, Value, Lock):
            return Exfi386InterlockedExchangeULONGTarget,Value
        ExInterlockedAddULONG = ExfInterlockedAddULONG
        ExInterlockedInsertHeadList = ExfInterlockedInsertHeadList
        ExInterlockedInsertTailList = ExfInterlockedInsertTailList
        ExInterlockedRemoveHeadList = ExfInterlockedRemoveHeadList
        ExInterlockedPopEntryList = ExfInterlockedPopEntryList
        ExInterlockedPushEntryList = ExfInterlockedPushEntryList

        if not defined(MIDL_PASS) and defined(_M_IX86):

            # i386 function definitions
            # Get current IRQL.
            # On x86 this function resides in the HAL
            if NTDDI_VERSION >= NTDDI_WIN7:
                pass
            # END IF        # END IF   not defined(MIDL_PASS) and defined(_M_IX86)
        if defined(__cplusplus):
            pass
        # END IF
        # Define function to invalidate a page.


        def InvalidatePage(Page):
            return __invlpgPage


        def WritebackInvalidate():
            return __wbinvd

        # Define functions to read and write CR3.


        def ReadCR3():
            return __readcr3


        def WriteCR3(Data):
            return __writecr3Data

        # Define function to get eflags.


        def ReadEflags():
            return __readeflags

        if defined(__cplusplus):
            pass
        # END IF    # END IF   defined(_X86_)
    if defined(_M_AMD64) and not defined(RC_INVOKED) and not defined(MIDL_PASS):

        # Define intrinsic function to do in's and out's.
        if defined(__cplusplus):
            pass
        # END IF
        if defined(__cplusplus):
            pass
        # END IF    # END IF   defined(_M_AMD64) and not defined(RC_INVOKED) and not defined(MIDL_PASS)
    if defined(_AMD64_): #  ntddk nthal irqls
        SPFN_NUMBER = LONG64
        PSPFN_NUMBER = POINTER(LONG64)
        PFN_NUMBER = ULONG64
        PPFN_NUMBER = POINTER(ULONG64)

        # Define maximum size of flush multiple TB request.
        FLUSH_MULTIPLE_MAXIMUM = 19

        # Indicate that the AMD64 compiler supports the allocate pragmas.
        ALLOC_PRAGMA = 1
        ALLOC_DATA_PRAGMA = 1

        # Define functions to read and write CR8.
        # CR8 is the APIC TPR register.

        if defined(__cplusplus):
            pass
        # END IF


        def WriteCR8(Data):
            return __writecr8Data

        if defined(__cplusplus):
            pass
        # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
        if defined(_AMD64_) and not defined(DSF_DRIVER):
            pass
        # END IF
        if PRAGMA_DEPRECATED_DDK:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
            pass
        else:


            def KeFlushIoBuffers(Mdl, ReadOperation, DmaOperation):
                return 1
        # END IF


        def ExAcquireSpinLock(Lock, OldIrql):
            return KeAcquireSpinLockLock, OldIrql


        def ExReleaseSpinLock(Lock, OldIrql):
            return KeReleaseSpinLockLock, OldIrql


        def ExAcquireSpinLockAtDpcLevel(Lock):
            return KeAcquireSpinLockAtDpcLevelLock


        def ExReleaseSpinLockFromDpcLevel(Lock):
            return KeReleaseSpinLockFromDpcLevelLock

        # Dummy nonvolatile FLOATing state structure.


        def MmGetProcedureAddress(Address):
            return Address


        def MmLockPagableCodeSection(Address):
            return MmLockPagableDataSectionAddress

        if NTDDI_VERSION >= NTDDI_WIN7:
            pass
        # END IF
        if not defined(_CROSS_PLATFORM_):
            pass
        else:
            pass
        # END IF    # END IF   defined(_AMD64_)
        if ((NTDDI_VERSION >= NTDDI_WIN8) and \:
            pass
        else:
            pass
        # END IF
    if defined(_AMD64_) and not defined(MIDL_PASS):
        pass
    # END IF   defined(_AMD64_) and not defined(MIDL_PASS)
    if defined(_M_ARM) and not defined(RC_INVOKED) and not defined(MIDL_PASS):
        pass
    # END IF   defined(_M_ARM) and not defined(RC_INVOKED) and not defined(MIDL_PASS)
    if defined(_ARM_): #  ntddk nthal irqls
        SPFN_NUMBER = LONG
        PSPFN_NUMBER = POINTER(LONG)
        PFN_NUMBER = ULONG
        PPFN_NUMBER = POINTER(ULONG)

        # Maximum number of event counters in performance monitoring unit.
        MAX_EVENT_COUNTERS = 31

        # Define maximum size of flush multiple TB request.
        FLUSH_MULTIPLE_MAXIMUM = 32

        # Indicate that the ARM compiler supports the allocate pragmas.
        ALLOC_PRAGMA = 1
        ALLOC_DATA_PRAGMA = 1

        if defined(__cplusplus):
            pass
        # END IF
        if defined(__cplusplus):
            pass
        # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
        if defined(_ARM_):
            pass
        # END IF
        if PRAGMA_DEPRECATED_DDK:
            pass
        # END IF


        def ExAcquireSpinLock(Lock, OldIrql):
            return KeAcquireSpinLockLock, OldIrql


        def ExReleaseSpinLock(Lock, OldIrql):
            return KeReleaseSpinLockLock, OldIrql


        def ExAcquireSpinLockAtDpcLevel(Lock):
            return KeAcquireSpinLockAtDpcLevelLock


        def ExReleaseSpinLockFromDpcLevel(Lock):
            return KeReleaseSpinLockFromDpcLevelLock


        def KeQueryTickCount(CurrentCount):
            return { KSYSTEM_TIME volatile *_TickCount = *PKSYSTEM_TIME *( & KeTickCount); for ;; { CurrentCount - >HighPart = _TickCount - >High1Time; CurrentCount - >LowPart = _TickCount - >LowPart; if (CurrentCount - >HighPart == _TickCount - >High2Time) break; YieldProcessor; } }

        # Definitions for CP15 Register 0 e.g. ID and cache information
        class _ARM_IDCODE(ctypes.Union):
            pass


        class _Struct_6(ctypes.Structure):
            pass


        _Struct_6._fields_ = [
            ('MinorRevision', ULONG, 4),
            ('Model', ULONG, 12),
            ('Architecture', ULONG, 4),
            ('Revision', ULONG, 4),
            ('Implementer', ULONG, 8),
        ]
        _ARM_IDCODE._Struct_6 = _Struct_6
        _ARM_IDCODE._anonymous_ = (
            '_Struct_6',
        )
        _ARM_IDCODE._fields_ = [
            ('_Struct_6', _ARM_IDCODE._Struct_6),
        ]
        ARM_IDCODE = _ARM_IDCODE
        PARM_IDCODE = POINTER(_ARM_IDCODE)

        # Dummy nonvolatile FLOATing state structure.


        def MmGetProcedureAddress(Address):
            return Address


        def MmLockPagableCodeSection(Address):
            return MmLockPagableDataSectionAddress
        CP15_PCR_RESERVED_MASK = 0xFFF


        def KIPCR():
            return (ULONG_PTR(_MoveFromCoprocessorCP15_TPIDRPRW) & ~CP15_PCR_RESERVED_MASK)

        if NTDDI_VERSION >= NTDDI_WIN7:
            pass
        # END IF
        if not defined(_CROSS_PLATFORM_):
            pass
        else:


            def KeMemoryBarrier():
                return 1


            def KeMemoryBarrierWithoutFence():
                return 1
        # END IF    # END IF   defined(_ARM_)

    if defined(_ARM_) and not defined(MIDL_PASS):


        def KeLowerIrql(a):
            return KfLowerIrqla


        def KeRaiseIrql(a, b):
            return *b = KfRaiseIrqla
    # END IF   defined(_ARM_) and not defined(MIDL_PASS)

    if defined(_M_ARM64) and not defined(RC_INVOKED) and not defined(MIDL_PASS):
        pass
    # END IF   defined(_M_ARM64) and not defined(RC_INVOKED) and not defined(MIDL_PASS)
    if defined(_ARM64_): #  ntddk nthal irqls ntoshvp

        # Types to use to contain PFNs and their counts.
        PFN_COUNT = ULONG
        SPFN_NUMBER = LONG64
        PSPFN_NUMBER = POINTER(LONG64)
        PFN_NUMBER = ULONG64
        PPFN_NUMBER = POINTER(ULONG64)

        # Maximum number of event counters in performance monitoring unit.
        MAX_EVENT_COUNTERS = 31

        # Define maximum size of flush multiple TB request.
        FLUSH_MULTIPLE_MAXIMUM = 32

        # Indicate that the ARM64 compiler supports the allocate pragmas.
        ALLOC_PRAGMA = 1
        ALLOC_DATA_PRAGMA = 1

        if defined(__cplusplus):
            pass
        # END IF
        if defined(__cplusplus):
            pass
        # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
        if defined(_ARM64_):
            pass
        # END IF
        if PRAGMA_DEPRECATED_DDK:
            pass
        # END IF


        def ExAcquireSpinLock(Lock, OldIrql):
            return KeAcquireSpinLockLock, OldIrql


        def ExReleaseSpinLock(Lock, OldIrql):
            return KeReleaseSpinLockLock, OldIrql


        def ExAcquireSpinLockAtDpcLevel(Lock):
            return KeAcquireSpinLockAtDpcLevelLock


        def ExReleaseSpinLockFromDpcLevel(Lock):
            return KeReleaseSpinLockFromDpcLevelLock

        # Definitions for MIDR Register e.g. ID and cache information
        class _ARM64_IDCODE(ctypes.Union):
            pass


        class _Struct_7(ctypes.Structure):
            pass


        _Struct_7._fields_ = [
            ('MinorRevision', ULONG64, 4),
            ('Model', ULONG64, 12),
            ('Architecture', ULONG64, 4),
            ('Revision', ULONG64, 4),
            ('Implementer', ULONG64, 8),
            ('Reserved', ULONG64, 32),
        ]
        _ARM64_IDCODE._Struct_7 = _Struct_7
        _ARM64_IDCODE._anonymous_ = (
            '_Struct_7',
        )
        _ARM64_IDCODE._fields_ = [
            ('ULONG', ULONG64),
            ('_Struct_7', _ARM64_IDCODE._Struct_7),
        ]
        ARM64_IDCODE = _ARM64_IDCODE
        PARM64_IDCODE = POINTER(_ARM64_IDCODE)

        # Dummy nonvolatile FLOATing state structure.


        def MmGetProcedureAddress(Address):
            return Address


        def MmLockPagableCodeSection(Address):
            return MmLockPagableDataSectionAddress
        ARM64_PCR_RESERVED_MASK = 0xFFF


        def KIPCR():
            return (ULONG_PTR(_ReadStatusRegARM64_TPIDR_EL1) & ~ARM64_PCR_RESERVED_MASK)

        if NTDDI_VERSION >= NTDDI_WIN7:
            pass
        # END IF
        if not defined(_CROSS_PLATFORM_):
            pass
        else:


            def KeMemoryBarrier():
                return 1


            def KeMemoryBarrierWithoutFence():
                return 1
        # END IF    # END IF   defined(_ARM64_)

    if defined(_ARM64_) and not defined(MIDL_PASS):


        def KeLowerIrql(a):
            return KfLowerIrqla


        def KeRaiseIrql(a, b):
            return *b = KfRaiseIrqla
    # END IF   defined(_ARM64_) and not defined(MIDL_PASS)


    class _FIRMWARE_TYPE(ENUM):
        FirmwareTypeUnknown = 1
        FirmwareTypeBios = 2
        FirmwareTypeUefi = 3
        FirmwareTypeMax = 4


    FIRMWARE_TYPE = _FIRMWARE_TYPE
    PFIRMWARE_TYPE = POINTER(_FIRMWARE_TYPE)

    # begin_access
    # Event Specific Access Rights.
    EVENT_QUERY_STATE = 0x0001
    EVENT_MODIFY_STATE = 0x0002
    EVENT_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0x3

    # Semaphore Specific Access Rights.
    SEMAPHORE_QUERY_STATE = 0x0001
    SEMAPHORE_MODIFY_STATE = 0x0002
    SEMAPHORE_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0x3


    class _LOGICAL_PROCESSOR_RELATIONSHIP(ENUM):
        RelationProcessorCore = 1
        RelationNumaNode = 2
        RelationCache = 3
        RelationProcessorPackage = 4
        RelationGroup = 5
        RelationAll = 0xFFFF


    LOGICAL_PROCESSOR_RELATIONSHIP = _LOGICAL_PROCESSOR_RELATIONSHIP
    LTP_PC_SMT = 0x1


    class _PROCESSOR_CACHE_TYPE(ENUM):
        CacheUnified = 1
        CacheInstruction = 2
        CacheData = 3
        CacheTrace = 4


    PROCESSOR_CACHE_TYPE = _PROCESSOR_CACHE_TYPE
    CACHE_FULLY_ASSOCIATIVE = 0xFF
    class _CACHE_DESCRIPTOR(ctypes.Structure):
        pass


    _CACHE_DESCRIPTOR._fields_ = [
        ('Level', UCHAR),
        ('Associativity', UCHAR),
        ('LineSize', USHORT),
        ('Size', ULONG),
        ('Type', PROCESSOR_CACHE_TYPE),
    ]
    CACHE_DESCRIPTOR = _CACHE_DESCRIPTOR
    PCACHE_DESCRIPTOR = POINTER(_CACHE_DESCRIPTOR)
    class _SYSTEM_LOGICAL_PROCESSOR_INFORMATION(ctypes.Structure):
        pass


    class DUMMYUNIONNAME(ctypes.Structure):
        pass


    class ProcessorCore(ctypes.Structure):
        pass


    ProcessorCore._fields_ = [
        ('Flags', UCHAR),
    ]
    DUMMYUNIONNAME.ProcessorCore = ProcessorCore
    class NumaNode(ctypes.Structure):
        pass


    NumaNode._fields_ = [
        ('NodeNumber', ULONG),
    ]
    DUMMYUNIONNAME.NumaNode = NumaNode
    DUMMYUNIONNAME._fields_ = [
        ('ProcessorCore', DUMMYUNIONNAME.ProcessorCore),
        ('NumaNode', DUMMYUNIONNAME.NumaNode),
        ('Cache', CACHE_DESCRIPTOR),
        ('Reserved', ULONGLONG * 2),
    ]
    _SYSTEM_LOGICAL_PROCESSOR_INFORMATION.DUMMYUNIONNAME = DUMMYUNIONNAME
    _SYSTEM_LOGICAL_PROCESSOR_INFORMATION._fields_ = [
        ('ProcessorMask', ULONG_PTR),
        ('Relationship', LOGICAL_PROCESSOR_RELATIONSHIP),
        ('DUMMYUNIONNAME', _SYSTEM_LOGICAL_PROCESSOR_INFORMATION.DUMMYUNIONNAME),
    ]
    SYSTEM_LOGICAL_PROCESSOR_INFORMATION = _SYSTEM_LOGICAL_PROCESSOR_INFORMATION
    PSYSTEM_LOGICAL_PROCESSOR_INFORMATION = POINTER(_SYSTEM_LOGICAL_PROCESSOR_INFORMATION)
    class _PROCESSOR_RELATIONSHIP(ctypes.Structure):
        pass


    _PROCESSOR_RELATIONSHIP._fields_ = [
        ('Flags', UCHAR),
        ('EfficiencyClass', UCHAR),
        ('Reserved', UCHAR * 20),
        ('GroupCount', USHORT),
        ('GroupMask', GROUP_AFFINITY * ANYSIZE_ARRAY),
    ]
    PROCESSOR_RELATIONSHIP = _PROCESSOR_RELATIONSHIP
    PPROCESSOR_RELATIONSHIP = POINTER(_PROCESSOR_RELATIONSHIP)
    class _NUMA_NODE_RELATIONSHIP(ctypes.Structure):
        pass


    _NUMA_NODE_RELATIONSHIP._fields_ = [
        ('NodeNumber', ULONG),
        ('Reserved', UCHAR * 20),
        ('GroupMask', GROUP_AFFINITY),
    ]
    NUMA_NODE_RELATIONSHIP = _NUMA_NODE_RELATIONSHIP
    PNUMA_NODE_RELATIONSHIP = POINTER(_NUMA_NODE_RELATIONSHIP)
    class _CACHE_RELATIONSHIP(ctypes.Structure):
        pass


    _CACHE_RELATIONSHIP._fields_ = [
        ('Level', UCHAR),
        ('Associativity', UCHAR),
        ('LineSize', USHORT),
        ('CacheSize', ULONG),
        ('Type', PROCESSOR_CACHE_TYPE),
        ('Reserved', UCHAR * 20),
        ('GroupMask', GROUP_AFFINITY),
    ]
    CACHE_RELATIONSHIP = _CACHE_RELATIONSHIP
    PCACHE_RELATIONSHIP = POINTER(_CACHE_RELATIONSHIP)
    class _PROCESSOR_GROUP_INFO(ctypes.Structure):
        pass


    _PROCESSOR_GROUP_INFO._fields_ = [
        ('MaximumProcessorCount', UCHAR),
        ('ActiveProcessorCount', UCHAR),
        ('Reserved', UCHAR * 38),
        ('ActiveProcessorMask', KAFFINITY),
    ]
    PROCESSOR_GROUP_INFO = _PROCESSOR_GROUP_INFO
    PPROCESSOR_GROUP_INFO = POINTER(_PROCESSOR_GROUP_INFO)
    class _GROUP_RELATIONSHIP(ctypes.Structure):
        pass


    _GROUP_RELATIONSHIP._fields_ = [
        ('MaximumGroupCount', USHORT),
        ('ActiveGroupCount', USHORT),
        ('Reserved', UCHAR * 20),
        ('GroupInfo', PROCESSOR_GROUP_INFO * ANYSIZE_ARRAY),
    ]
    GROUP_RELATIONSHIP = _GROUP_RELATIONSHIP
    PGROUP_RELATIONSHIP = POINTER(_GROUP_RELATIONSHIP)
    class _SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX(ctypes.Structure):
        pass


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('Processor', PROCESSOR_RELATIONSHIP),
        ('NumaNode', NUMA_NODE_RELATIONSHIP),
        ('Cache', CACHE_RELATIONSHIP),
        ('Group', GROUP_RELATIONSHIP),
    ]
    _SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX.DUMMYUNIONNAME = DUMMYUNIONNAME
    _SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX._fields_ = [
        ('Relationship', LOGICAL_PROCESSOR_RELATIONSHIP),
        ('Size', ULONG),
        ('DUMMYUNIONNAME', _SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX.DUMMYUNIONNAME),
    ]
    PSYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX = POINTER(SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX,)



    class _CPU_SET_INFORMATION_TYPE(ENUM):
        CpuSetInformation = 1


    CPU_SET_INFORMATION_TYPE = _CPU_SET_INFORMATION_TYPE
    PCPU_SET_INFORMATION_TYPE = POINTER(_CPU_SET_INFORMATION_TYPE)
    class _SYSTEM_CPU_SET_INFORMATION(ctypes.Structure):
        pass


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    class CpuSet(ctypes.Union):
        pass


    class DUMMYUNIONNAME2(ctypes.Structure):
        pass


    class DUMMYSTRUCTNAME(ctypes.Structure):
        pass


    DUMMYSTRUCTNAME._fields_ = [
        ('Parked', UCHAR, 1),
        ('Allocated', UCHAR, 1),
        ('AllocatedToTargetProcess', UCHAR, 1),
        ('RealTime', UCHAR, 1),
        ('ReservedFlags', UCHAR, 4),
    ]
    DUMMYUNIONNAME2.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME2._fields_ = [
        ('AllFlags', UCHAR),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME2.DUMMYSTRUCTNAME),
    ]
    CpuSet.DUMMYUNIONNAME2 = DUMMYUNIONNAME2
    class _Union_1(ctypes.Union):
        pass


    _Union_1._fields_ = [
        ('Reserved', ULONG),
        ('SchedulingClass', UCHAR),
    ]
    CpuSet._Union_1 = _Union_1
    CpuSet._anonymous_ = (
        '_Union_1',
    )
    CpuSet._fields_ = [
        ('Id', ULONG),
        ('Group', USHORT),
        ('LogicalProcessorIndex', UCHAR),
        ('CoreIndex', UCHAR),
        ('LastLevelCacheIndex', UCHAR),
        ('NumaNodeIndex', UCHAR),
        ('EfficiencyClass', UCHAR),
        ('DUMMYUNIONNAME2', CpuSet.DUMMYUNIONNAME2),
        ('_Union_1', CpuSet._Union_1),
        ('AllocationTag', ULONG64),
    ]
    DUMMYUNIONNAME.CpuSet = CpuSet
    DUMMYUNIONNAME._fields_ = [
        ('CpuSet', DUMMYUNIONNAME.CpuSet),
    ]
    _SYSTEM_CPU_SET_INFORMATION.DUMMYUNIONNAME = DUMMYUNIONNAME
    _SYSTEM_CPU_SET_INFORMATION._fields_ = [
        ('Size', ULONG),
        ('Type', CPU_SET_INFORMATION_TYPE),
        ('DUMMYUNIONNAME', _SYSTEM_CPU_SET_INFORMATION.DUMMYUNIONNAME),
    ]
    PSYSTEM_CPU_SET_INFORMATION = POINTER(SYSTEM_CPU_SET_INFORMATION,)


    # Defined processor features
    PF_FLOATING_POINT_PRECISION_ERRATA = 0
    PF_FLOATING_POINT_EMULATED = 1
    PF_COMPARE_EXCHANGE_DOUBLE = 2
    PF_MMX_INSTRUCTIONS_AVAILABLE = 3
    PF_PPC_MOVEMEM_64BIT_OK = 4
    PF_ALPHA_BYTE_INSTRUCTIONS = 5
    PF_XMMI_INSTRUCTIONS_AVAILABLE = 6
    PF_3DNOW_INSTRUCTIONS_AVAILABLE = 7
    PF_RDTSC_INSTRUCTION_AVAILABLE = 8
    PF_PAE_ENABLED = 9
    PF_XMMI64_INSTRUCTIONS_AVAILABLE = 10
    PF_SSE_DAZ_MODE_AVAILABLE = 11
    PF_NX_ENABLED = 12
    PF_SSE3_INSTRUCTIONS_AVAILABLE = 13
    PF_COMPARE_EXCHANGE128 = 14
    PF_COMPARE64_EXCHANGE128 = 15
    PF_CHANNELS_ENABLED = 16
    PF_XSAVE_ENABLED = 17
    PF_ARM_VFP_32_REGISTERS_AVAILABLE = 18
    PF_ARM_NEON_INSTRUCTIONS_AVAILABLE = 19
    PF_SECOND_LEVEL_ADDRESS_TRANSLATION = 20
    PF_VIRT_FIRMWARE_ENABLED = 21
    PF_RDWRFSGSBASE_AVAILABLE = 22
    PF_FASTFAIL_AVAILABLE = 23
    PF_ARM_DIVIDE_INSTRUCTION_AVAILABLE = 24
    PF_ARM_64BIT_LOADSTORE_ATOMIC = 25
    PF_ARM_EXTERNAL_CACHE_AVAILABLE = 26
    PF_ARM_FMAC_INSTRUCTIONS_AVAILABLE = 27
    PF_RDRAND_INSTRUCTION_AVAILABLE = 28
    PF_ARM_V8_INSTRUCTIONS_AVAILABLE = 29
    PF_ARM_V8_CRYPTO_INSTRUCTIONS_AVAILABLE = 30
    PF_ARM_V8_CRC32_INSTRUCTIONS_AVAILABLE = 31
    PF_RDTSCP_INSTRUCTION_AVAILABLE = 32


    class _ALTERNATIVE_ARCHITECTURE_TYPE(ENUM):
        StandardDesign = 1
        NEC98x86 = 2
        EndAlternatives = 3


    ALTERNATIVE_ARCHITECTURE_TYPE = _ALTERNATIVE_ARCHITECTURE_TYPE

    # correctly define these run - time definitions for non X86 machines
    if not defined(_X86_):
        if not defined(IsNEC_98):
            IsNEC_98 = FALSE
        # END IF

        if not defined(IsNotNEC_98):
            IsNotNEC_98 = TRUE
        # END IF

        if not defined(SetNEC_98):
            SetNEC_98 = 1
        # END IF

        if not defined(SetNotNEC_98):
            SetNotNEC_98 = 1
        # END IF    # END IF   _X86_
    PROCESSOR_FEATURE_MAX = 64

    # Exception flag definitions.
    EXCEPTION_NONCONTINUABLE = 0x1
    EXCEPTION_UNWINDING = 0x2
    EXCEPTION_EXIT_UNWIND = 0x4
    EXCEPTION_STACK_INVALID = 0x8
    EXCEPTION_NESTED_CALL = 0x10
    EXCEPTION_TARGET_UNWIND = 0x20
    EXCEPTION_COLLIDED_UNWIND = 0x40
    EXCEPTION_UNWIND = (
        EXCEPTION_UNWINDING |
        EXCEPTION_EXIT_UNWIND |
        EXCEPTION_TARGET_UNWIND |
        EXCEPTION_COLLIDED_UNWIND
    )


    def IS_UNWINDING(Flag):
        return ((Flag & EXCEPTION_UNWIND) != 0)


    def IS_DISPATCHING(Flag):
        return ((Flag & EXCEPTION_UNWIND) == 0)


    def IS_TARGET_UNWIND(Flag):
        return (Flag & EXCEPTION_TARGET_UNWIND)

    # Define maximum number of exception parameters.
    EXCEPTION_MAXIMUM_PARAMETERS = 15

    # Exception record definition.
    class _EXCEPTION_RECORD(ctypes.Structure):
        pass


    _EXCEPTION_RECORD._fields_ = [
        ('ExceptionCode', NTSTATUS),
        ('ExceptionFlags', ULONG),
        ('ExceptionRecord', POINTER(_EXCEPTION_RECORD)),
        ('ExceptionAddress', PVOID),
        ('NumberParameters', ULONG),
        ('ExceptionInformation', ULONG_PTR * EXCEPTION_MAXIMUM_PARAMETERS),
    ]
    EXCEPTION_RECORD = _EXCEPTION_RECORD
    PEXCEPTION_RECORD = POINTER(EXCEPTION_RECORD)
    class _EXCEPTION_RECORD32(ctypes.Structure):
        pass


    _EXCEPTION_RECORD32._fields_ = [
        ('ExceptionCode', NTSTATUS),
        ('ExceptionFlags', ULONG),
        ('ExceptionRecord', ULONG),
        ('ExceptionAddress', ULONG),
        ('NumberParameters', ULONG),
        ('ExceptionInformation', ULONG * EXCEPTION_MAXIMUM_PARAMETERS),
    ]
    EXCEPTION_RECORD32 = _EXCEPTION_RECORD32
    PEXCEPTION_RECORD32 = POINTER(_EXCEPTION_RECORD32)
    class _EXCEPTION_RECORD64(ctypes.Structure):
        pass


    _EXCEPTION_RECORD64._fields_ = [
        ('ExceptionCode', NTSTATUS),
        ('ExceptionFlags', ULONG),
        ('ExceptionRecord', ULONG64),
        ('ExceptionAddress', ULONG64),
        ('NumberParameters', ULONG),
        ('__unusedAlignment', ULONG),
        ('ExceptionInformation', ULONG64 * EXCEPTION_MAXIMUM_PARAMETERS),
    ]
    EXCEPTION_RECORD64 = _EXCEPTION_RECORD64
    PEXCEPTION_RECORD64 = POINTER(_EXCEPTION_RECORD64)

    # Typedef for pointer returned by exception_info()
    class _EXCEPTION_POINTERS(ctypes.Structure):
        pass


    _EXCEPTION_POINTERS._fields_ = [
        ('ExceptionRecord', PEXCEPTION_RECORD),
        ('ContextRecord', PCONTEXT),
    ]
    EXCEPTION_POINTERS = _EXCEPTION_POINTERS
    PEXCEPTION_POINTERS = POINTER(_EXCEPTION_POINTERS)
    THREAD_WAIT_OBJECTS = 3

    # Several routines have an architecture specific implementation. Generate
    # an error if a supported target is not defined.

    if not (defined(_X86_) or defined(_AMD64_) or defined(_ARM_) or defined(_ARM64_)):
        pass
    # END IF
    if NTDDI_VERSION < NTDDI_WIN7) or defined(_X86_) or not defined(NT_PROCESSOR_GROUPS:
        SINGLE_GROUP_LEGACY_API = 1
    # END IF
    # Interrupt modes.


    class _KINTERRUPT_MODE(ENUM):
        LevelSensitive = 1
        Latched = 2


    KINTERRUPT_MODE = _KINTERRUPT_MODE
    class _KINTERRUPT_POLARITY(ENUM):
        InterruptPolarityUnknown = 1
        InterruptActiveHigh = 2
        InterruptRisingEdge = InterruptActiveHigh
        InterruptActiveLow = 3
        InterruptFallingEdge = InterruptActiveLow
    if NTDDI_VERSION >= NTDDI_WIN8:
        #~#~#~ if NTDDI_VERSION >= NTDDI_WIN8:
        InterruptActiveBoth = 4
    # END IF
if NTDDI_VERSION >= NTDDI_WINBLUE:
    #~#~#~ if NTDDI_VERSION >= NTDDI_WINBLUE:
    InterruptActiveBothTriggerLow = InterruptActiveBoth
    InterruptActiveBothTriggerHigh = 5
# END IF


KINTERRUPT_POLARITY = _KINTERRUPT_POLARITY
PKINTERRUPT_POLARITY = POINTER(_KINTERRUPT_POLARITY)
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        pass
    # END IF
    # Wait reasons
    class _KWAIT_REASON(ENUM):
        Executive = 1
        FreePage = 2
        PageIn = 3
        PoolAllocation = 4
        DelayExecution = 5
        Suspended = 6
        UserRequest = 7
        WrExecutive = 8
        WrFreePage = 9
        WrPageIn = 10
        WrPoolAllocation = 11
        WrDelayExecution = 12
        WrSuspended = 13
        WrUserRequest = 14
        WrSpare0 = 15
        WrQueue = 16
        WrLpcReceive = 17
        WrLpcReply = 18
        WrVirtualMemory = 19
        WrPageOut = 20
        WrRendezvous = 21
        WrKeyedEvent = 22
        WrTerminated = 23
        WrProcessInSwap = 24
        WrCpuRateControl = 25
        WrCalloutStack = 26
        WrKernel = 27
        WrResource = 28
        WrPushLock = 29
        WrMutex = 30
        WrQuantumEnd = 31
        WrDispatchInt = 32
        WrPreempted = 33
        WrYieldExecution = 34
        WrFastMutex = 35
        WrGuardedMutex = 36
        WrRundown = 37
        WrAlertByThreadId = 38
        WrDeferredPreempt = 39
        WrPhysicalFault = 40
        MaximumWaitReason = 41


    KWAIT_REASON = _KWAIT_REASON
    class _KWAIT_BLOCK(ctypes.Structure):
        pass


    class _Union_1(ctypes.Union):
        pass


    _Union_1._fields_ = [
        ('Thread', POINTER(_KTHREAD)),
        ('NotificationQueue', POINTER(_KQUEUE)),
    ]
    _KWAIT_BLOCK._Union_1 = _Union_1
    _KWAIT_BLOCK._anonymous_ = (
        '_Union_1',
    )
    _KWAIT_BLOCK._fields_ = [
        ('WaitListEntry', LIST_ENTRY),
        ('WaitType', UCHAR),
        ('UCHAR BlockState', volatile),
        ('WaitKey', USHORT),
            ('SpareLong', LONG),
        ('_Union_1', _KWAIT_BLOCK._Union_1),
        ('Object', PVOID),
        ('SparePtr', PVOID),
    ]
    KWAIT_BLOCK = _KWAIT_BLOCK
    PKWAIT_BLOCK = POINTER(_KWAIT_BLOCK)
    PRKWAIT_BLOCK = POINTER(_KWAIT_BLOCK)
    if defined(_WIN64):
        pass
    # END IF
    # Thread start function
    PKSTART_ROUTINE = POINTER(KSTART_ROUTINE)

    # Kernel object structure definitions
    # Device Queue object and entry


    def ASSERT_DEVICE_QUEUE(E):
        return NT_ASSERT(E - >Type == DeviceQueueObject)
    class _KDEVICE_QUEUE(ctypes.Structure):
        pass


        class _Struct_8(ctypes.Structure):
            pass


        class _Struct_9(ctypes.Structure):
            pass


        _Struct_9._fields_ = [
            ('Reserved', LONG64, 8),
            ('Hint', LONG64, 56),
        ]
        _Struct_8._Struct_9 = _Struct_9
        _Struct_8._anonymous_ = (
            '_Struct_9',
        )
        _Struct_8._fields_ = [
            ('Busy', BOOLEAN),
            ('_Struct_9', _Struct_8._Struct_9),
        ]
        _KDEVICE_QUEUE._Struct_8 = _Struct_8
    _KDEVICE_QUEUE._anonymous_ = (
        '_Struct_8',
    )
    _KDEVICE_QUEUE._fields_ = [
        ('Type', CSHORT),
        ('Size', CSHORT),
        ('DeviceListHead', LIST_ENTRY),
        ('Lock', KSPIN_LOCK),
            ('_Struct_8', _KDEVICE_QUEUE._Struct_8),
            ('Busy', BOOLEAN),
    ]
    KDEVICE_QUEUE = _KDEVICE_QUEUE
    PKDEVICE_QUEUE = POINTER(_KDEVICE_QUEUE)
    PRKDEVICE_QUEUE = POINTER(_KDEVICE_QUEUE)

    if defined(_AMD64_):
        pass
    else:
        pass
    # END IF
    class _KDEVICE_QUEUE_ENTRY(ctypes.Structure):
        pass


    _KDEVICE_QUEUE_ENTRY._fields_ = [
        ('DeviceListEntry', LIST_ENTRY),
        ('SortKey', ULONG),
        ('Inserted', BOOLEAN),
    ]
    KDEVICE_QUEUE_ENTRY = _KDEVICE_QUEUE_ENTRY
    PKDEVICE_QUEUE_ENTRY = POINTER(_KDEVICE_QUEUE_ENTRY)
    PRKDEVICE_QUEUE_ENTRY = POINTER(_KDEVICE_QUEUE_ENTRY)

    # Define the interrupt service function type and the empty struct
    # type.
    PKSERVICE_ROUTINE = POINTER(KSERVICE_ROUTINE)
    PKMESSAGE_SERVICE_ROUTINE = POINTER(KMESSAGE_SERVICE_ROUTINE)

    # Mutant object
    class _KMUTANT(ctypes.Structure):
        pass


    _KMUTANT._fields_ = [
        ('Header', DISPATCHER_HEADER),
        ('MutantListEntry', LIST_ENTRY),
        ('OwnerThread', POINTER(_KTHREAD)),
        ('Abandoned', BOOLEAN),
        ('ApcDisable', UCHAR),
    ]
    KMUTANT = _KMUTANT
    PKMUTANT = POINTER(_KMUTANT)
    PRKMUTANT = POINTER(_KMUTANT)
    KMUTEX = _KMUTANT
    PKMUTEX = POINTER(_KMUTANT)
    PRKMUTEX = POINTER(_KMUTANT)

    # Semaphore object
    # N.B. The limit field must be the last member of this structure.
    class _KSEMAPHORE(ctypes.Structure):
        pass


    _KSEMAPHORE._fields_ = [
        ('Header', DISPATCHER_HEADER),
        ('Limit', LONG),
    ]
    KSEMAPHORE = _KSEMAPHORE
    PKSEMAPHORE = POINTER(_KSEMAPHORE)
    PRKSEMAPHORE = POINTER(_KSEMAPHORE)
    KSEMAPHORE_ACTUAL_LENGTH = (
        FIELD_OFFSET(KSEMAPHORE,
        Limit) + ctypes.sizeof(LONG),
    )

    # DPC object

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K) and defined(SINGLE_GROUP_LEGACY_API:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXPSP2:
        pass
    # END IF
    # Device queue object
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    # Kernel dispatcher object functions
    # Event Object
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Mutex object
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Semaphore object
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K) and defined(SINGLE_GROUP_LEGACY_API:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K) and defined(SINGLE_GROUP_LEGACY_API:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA) and defined(SINGLE_GROUP_LEGACY_API:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_LONGHORN) and defined(SINGLE_GROUP_LEGACY_API:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    # Timer object
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    KeWaitForMutexObject = KeWaitForSingleObject

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Define interprocess interrupt generic call types.
    PKIPI_BROADCAST_WORKER = POINTER(KIPI_BROADCAST_WORKER)
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    # Spin lock functions
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
    if ((defined(_X86_) and (defined(_WDM_INCLUDED_) or defined(WIN9X_COMPAT_SPINLOCK))) or \:
        pass
    else:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
    if defined(_X86_): #  ntifs


        def KeAcquireSpinLockAtDpcLevel(a):
            return KefAcquireSpinLockAtDpcLevela


        def KeReleaseSpinLockFromDpcLevel(a):
            return KefReleaseSpinLockFromDpcLevela

        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF


        def KeAcquireSpinLock(a, b):
            return *b = KfAcquireSpinLocka


        def KeReleaseSpinLock(a, b):
            return KfReleaseSpinLocka,b
    else: #  ntifs

        # These functions are imported for ARM, ntddk, ntifs, nthal, ntosp,
        # and wdm.
        # They can be inlined for the system on AMD64.


        def KeAcquireSpinLock(SpinLock, OldIrql):
            return *OldIrql = KeAcquireSpinLockRaiseToDpcSpinLock

        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF    # END IF   ntifs
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    # Queued spin lock functions for "in stack" lock handles.
    # The following three functions RAISE and LOWER IRQL when a queued
    # in stack spin lock is acquired or released using these routines.
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    # The following two functions do NOT raise or lower IRQL when a queued
    # in stack spin lock is acquired or released using these functions.
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    # The following two functions conditionally raise or lower IRQL when a
    # queued in - stack spin lock is acquired or released using these
    # functions.
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    # Miscellaneous kernel functions
    class _KDPC_WATCHDOG_INFORMATION(ctypes.Structure):
        pass


    _KDPC_WATCHDOG_INFORMATION._fields_ = [
        ('DpcTimeLimit', ULONG),
        ('DpcTimeCount', ULONG),
        ('DpcWatchdogLimit', ULONG),
        ('DpcWatchdogCount', ULONG),
        ('Reserved', ULONG),
    ]
    KDPC_WATCHDOG_INFORMATION = _KDPC_WATCHDOG_INFORMATION
    PKDPC_WATCHDOG_INFORMATION = POINTER(_KDPC_WATCHDOG_INFORMATION)
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS4:
        pass
    # END IF
    class _KBUGCHECK_BUFFER_DUMP_STATE(ENUM):
        BufferEmpty = 1
        BufferInserted = 2
        BufferStarted = 3
        BufferFinished = 4
        BufferIncomplete = 5


    KBUGCHECK_BUFFER_DUMP_STATE = _KBUGCHECK_BUFFER_DUMP_STATE
    PKBUGCHECK_CALLBACK_ROUTINE = POINTER(KBUGCHECK_CALLBACK_ROUTINE)
    class _KBUGCHECK_CALLBACK_RECORD(ctypes.Structure):
        pass


    _KBUGCHECK_CALLBACK_RECORD._fields_ = [
        ('Entry', LIST_ENTRY),
        ('CallbackRoutine', PKBUGCHECK_CALLBACK_ROUTINE),
        ('Buffer', PVOID),
        ('Length', ULONG),
        ('Component', PUCHAR),
        ('Checksum', ULONG_PTR),
        ('State', UCHAR),
    ]
    KBUGCHECK_CALLBACK_RECORD = _KBUGCHECK_CALLBACK_RECORD
    PKBUGCHECK_CALLBACK_RECORD = POINTER(_KBUGCHECK_CALLBACK_RECORD)


    def KeInitializeCallbackRecord(CallbackRecord):
        return CallbackRecord - >State = BufferEmpty

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    class _KBUGCHECK_CALLBACK_REASON(ENUM):
        KbCallbackInvalid = 1
        KbCallbackReserved1 = 2
        KbCallbackSecondaryDumpData = 3
        KbCallbackDumpIo = 4
        KbCallbackAddPages = 5
        KbCallbackSecondaryMultiPartDumpData = 6
        KbCallbackRemovePages = 7
        KbCallbackTriageDumpData = 8


    KBUGCHECK_CALLBACK_REASON = _KBUGCHECK_CALLBACK_REASON
    PKBUGCHECK_REASON_CALLBACK_ROUTINE = POINTER(KBUGCHECK_REASON_CALLBACK_ROUTINE)
    class _KBUGCHECK_REASON_CALLBACK_RECORD(ctypes.Structure):
        pass


    _KBUGCHECK_REASON_CALLBACK_RECORD._fields_ = [
        ('Entry', LIST_ENTRY),
        ('CallbackRoutine', PKBUGCHECK_REASON_CALLBACK_ROUTINE),
        ('Component', PUCHAR),
        ('Checksum', ULONG_PTR),
        ('Reason', KBUGCHECK_CALLBACK_REASON),
        ('State', UCHAR),
    ]
    KBUGCHECK_REASON_CALLBACK_RECORD = _KBUGCHECK_REASON_CALLBACK_RECORD
    PKBUGCHECK_REASON_CALLBACK_RECORD = POINTER(_KBUGCHECK_REASON_CALLBACK_RECORD)
    class _KBUGCHECK_SECONDARY_DUMP_DATA(ctypes.Structure):
        pass


    _KBUGCHECK_SECONDARY_DUMP_DATA._fields_ = [
        ('InBuffer', PVOID),
        ('InBufferLength', ULONG),
        ('MaximumAllowed', ULONG),
        ('Guid', GUID),
        ('OutBuffer', PVOID),
        ('OutBufferLength', ULONG),
    ]
    KBUGCHECK_SECONDARY_DUMP_DATA = _KBUGCHECK_SECONDARY_DUMP_DATA
    PKBUGCHECK_SECONDARY_DUMP_DATA = POINTER(_KBUGCHECK_SECONDARY_DUMP_DATA)
    class _KBUGCHECK_SECONDARY_DUMP_DATA_EX(ctypes.Structure):
        pass


    _KBUGCHECK_SECONDARY_DUMP_DATA_EX._fields_ = [
        ('InBuffer', PVOID),
        ('InBufferLength', ULONG),
        ('MaximumAllowed', ULONG),
        ('Guid', GUID),
        ('PVOID OutBuffer', _Inout_),
        ('ULONG OutBufferLength', _Inout_),
        ('PVOID Context', _Inout_),
        ('ULONG Flags', _Inout_), # KB_SECONDARY_DATA_FLAG_xxx
        ('DumpType', ULONG), # DUMP_TYPE defined in ntiodump.h
        ('BugCheckCode', ULONG),
        ('BugCheckParameter1', ULONG_PTR),
        ('BugCheckParameter2', ULONG_PTR),
        ('BugCheckParameter3', ULONG_PTR),
        ('BugCheckParameter4', ULONG_PTR),
    ]
    KBUGCHECK_SECONDARY_DUMP_DATA_EX = _KBUGCHECK_SECONDARY_DUMP_DATA_EX
    PKBUGCHECK_SECONDARY_DUMP_DATA_EX = POINTER(_KBUGCHECK_SECONDARY_DUMP_DATA_EX)
    KB_SECONDARY_DATA_FLAG_ADDITIONAL_DATA = 0x00000001
    KB_SECONDARY_DATA_FLAG_NO_DEVICE_ACCESS = 0x00000002


    class _KBUGCHECK_DUMP_IO_TYPE(ENUM):
        KbDumpIoInvalid = 1
        KbDumpIoHeader = 2
        KbDumpIoBody = 3
        KbDumpIoSecondaryData = 4
        KbDumpIoComplete = 5


    KBUGCHECK_DUMP_IO_TYPE = _KBUGCHECK_DUMP_IO_TYPE
    class _KBUGCHECK_DUMP_IO(ctypes.Structure):
        pass


    _KBUGCHECK_DUMP_IO._fields_ = [
        ('Offset', ULONG64),
        ('Buffer', PVOID),
        ('BufferLength', ULONG),
        ('Type', KBUGCHECK_DUMP_IO_TYPE),
    ]
    KBUGCHECK_DUMP_IO = _KBUGCHECK_DUMP_IO
    PKBUGCHECK_DUMP_IO = POINTER(_KBUGCHECK_DUMP_IO)

    # KbCallbackAddPages related definitions
    KB_ADD_PAGES_FLAG_VIRTUAL_ADDRESS = 0x00000001
    KB_ADD_PAGES_FLAG_PHYSICAL_ADDRESS = 0x00000002
    KB_ADD_PAGES_FLAG_ADDITIONAL_RANGES_EXIST = 0x80000000
    class _KBUGCHECK_ADD_PAGES(ctypes.Structure):
        pass


    _KBUGCHECK_ADD_PAGES._fields_ = [
        ('PVOID Context', _Inout_), # Private context for callback use
        ('ULONG Flags', _Inout_), # Zero initialized on input
        ('BugCheckCode', ULONG),
        ('Address', ULONG_PTR),
        ('Count', ULONG_PTR),
    ]
    KBUGCHECK_ADD_PAGES = _KBUGCHECK_ADD_PAGES
    PKBUGCHECK_ADD_PAGES = POINTER(_KBUGCHECK_ADD_PAGES)

    # KbCallbackRemovePages related definitions
    KB_REMOVE_PAGES_FLAG_VIRTUAL_ADDRESS = 0x00000001
    KB_REMOVE_PAGES_FLAG_PHYSICAL_ADDRESS = 0x00000002
    KB_REMOVE_PAGES_FLAG_ADDITIONAL_RANGES_EXIST = 0x80000000
    class _KBUGCHECK_REMOVE_PAGES(ctypes.Structure):
        pass


    _KBUGCHECK_REMOVE_PAGES._fields_ = [
        ('PVOID Context', _Inout_), # Private context for callback use
        ('ULONG Flags', _Inout_), # Zero initialized on input
        ('BugCheckCode', ULONG),
        ('Address', ULONG_PTR),
        ('Count', ULONG_PTR),
    ]
    KBUGCHECK_REMOVE_PAGES = _KBUGCHECK_REMOVE_PAGES
    PKBUGCHECK_REMOVE_PAGES = POINTER(_KBUGCHECK_REMOVE_PAGES)

    # Define simple address range structure.
    class _KADDRESS_RANGE(ctypes.Structure):
        pass


    _KADDRESS_RANGE._fields_ = [
        ('Address', PVOID),
        ('Size', SIZE_T),
    ]
    KADDRESS_RANGE = _KADDRESS_RANGE
    PKADDRESS_RANGE = POINTER(_KADDRESS_RANGE)
    class _KADDRESS_RANGE_DESCRIPTOR(ctypes.Structure):
        pass


    _KADDRESS_RANGE_DESCRIPTOR._fields_ = [
        ('KADDRESS_RANGE *AddressRanges', CONST),
        ('AddressRangeCount', SIZE_T),
    ]
    KADDRESS_RANGE_DESCRIPTOR = _KADDRESS_RANGE_DESCRIPTOR
    PKADDRESS_RANGE_DESCRIPTOR = POINTER(_KADDRESS_RANGE_DESCRIPTOR)

    # KbCallbackTriageDumpData related definitions
    KB_TRIAGE_DUMP_DATA_FLAG_BUGCHECK_ACTIVE = 0x00000001
    class _KBUGCHECK_TRIAGE_DUMP_DATA(ctypes.Structure):
        pass


    _KBUGCHECK_TRIAGE_DUMP_DATA._fields_ = [
        ('PKTRIAGE_DUMP_DATA_ARRAY DataArray', _Out_opt_),
        ('Flags', ULONG), # KB_TRIAGE_DUMP_DATA_FLAG_xxx
        ('MaxVirtMemSize', ULONG),
        ('BugCheckCode', ULONG),
        ('BugCheckParameter1', ULONG_PTR),
        ('BugCheckParameter2', ULONG_PTR),
        ('BugCheckParameter3', ULONG_PTR),
        ('BugCheckParameter4', ULONG_PTR),
    ]
    KBUGCHECK_TRIAGE_DUMP_DATA = _KBUGCHECK_TRIAGE_DUMP_DATA
    PKBUGCHECK_TRIAGE_DUMP_DATA = POINTER(_KBUGCHECK_TRIAGE_DUMP_DATA)

    # Equates for exceptions which cause system fatal error
    EXCEPTION_DIVIDED_BY_ZERO = 0
    EXCEPTION_DEBUG = 1
    EXCEPTION_NMI = 2
    EXCEPTION_INT3 = 3
    EXCEPTION_BOUND_CHECK = 5
    EXCEPTION_INVALID_OPCODE = 6
    EXCEPTION_NPX_NOT_AVAILABLE = 7
    EXCEPTION_DOUBLE_FAULT = 8
    EXCEPTION_NPX_OVERRUN = 9
    EXCEPTION_INVALID_TSS = 0x0A
    EXCEPTION_SEGMENT_NOT_PRESENT = 0x0B
    EXCEPTION_STACK_FAULT = 0x0C
    EXCEPTION_GP_FAULT = 0x0D
    EXCEPTION_RESERVED_TRAP = 0x0F
    EXCEPTION_NPX_ERROR = 0x10
    EXCEPTION_ALIGNMENT_CHECK = 0x11
    EXCEPTION_VIRTUALIZATION_FAULT = 0x20

    if NTDDI_VERSION >= NTDDI_WINXPSP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXPSP1:
        pass
    # END IF
    PNMI_CALLBACK = POINTER(NMI_CALLBACK)
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    if defined(_X86_) or defined(_AMD64_):
        if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
            class _BOUND_CALLBACK_STATUS(ENUM):
                BoundExceptionContinueSearch = 0
                BoundExceptionHandled = 1
                BoundExceptionError = 2
                BoundExceptionMaximum = 3


            BOUND_CALLBACK_STATUS = _BOUND_CALLBACK_STATUS
            PBOUND_CALLBACK_STATUS = POINTER(_BOUND_CALLBACK_STATUS)
        # END IF
        if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
            PBOUND_CALLBACK = POINTER(BOUND_CALLBACK)
        # END IF
        if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
            pass
        # END IF    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
    if not defined(_AMD64_) and not defined(_ARM64_):
        pass
    # END IF   not _AMD64_
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_THRESHOLD:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K) and defined(SINGLE_GROUP_LEGACY_API:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA) and defined(SINGLE_GROUP_LEGACY_API:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_LONGHORN) and defined(SINGLE_GROUP_LEGACY_API:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if defined(_X86_) or defined(_ARM_):
        pass
    # END IF
    class _MEMORY_CACHING_TYPE_ORIG(ENUM):
        MmFrameBufferCached = 2


    MEMORY_CACHING_TYPE_ORIG = _MEMORY_CACHING_TYPE_ORIG
    class _MEMORY_CACHING_TYPE(ENUM):
        #~#~#~ MmNonCached = FALSE        #~#~#~ MmCached = TRUE
        MmWriteCombined = MmFrameBufferCached
        MmHardwareCoherentCached = 3
        MmNonCachedUnordered = 4
        MmUSWCCached = 5
        MmMaximumCacheType = 6
        MmNotMapped = - 1


    MEMORY_CACHING_TYPE = _MEMORY_CACHING_TYPE
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    # Define dynamic processor add types.
    class KE_PROCESSOR_CHANGE_NOTIFY_STATE(ENUM):
        KeProcessorAddStartNotify = 0
        KeProcessorAddCompleteNotify = 1
        KeProcessorAddFailureNotify = 2


    KeProcessorAddStartNotify = KE_PROCESSOR_CHANGE_NOTIFY_STATE.KeProcessorAddStartNotify
    KeProcessorAddCompleteNotify = KE_PROCESSOR_CHANGE_NOTIFY_STATE.KeProcessorAddCompleteNotify
    KeProcessorAddFailureNotify = KE_PROCESSOR_CHANGE_NOTIFY_STATE.KeProcessorAddFailureNotify
    class _KE_PROCESSOR_CHANGE_NOTIFY_CONTEXT(ctypes.Structure):
        pass


    _KE_PROCESSOR_CHANGE_NOTIFY_CONTEXT._fields_ = [
        ('State', KE_PROCESSOR_CHANGE_NOTIFY_STATE),
        ('NtNumber', ULONG),
        ('Status', NTSTATUS),
            ('ProcNumber', PROCESSOR_NUMBER),
    ]
    KE_PROCESSOR_CHANGE_NOTIFY_CONTEXT = _KE_PROCESSOR_CHANGE_NOTIFY_CONTEXT
    PKE_PROCESSOR_CHANGE_NOTIFY_CONTEXT = POINTER(_KE_PROCESSOR_CHANGE_NOTIFY_CONTEXT)
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    PPROCESSOR_CALLBACK_FUNCTION = POINTER(PROCESSOR_CALLBACK_FUNCTION)
    KE_PROCESSOR_CHANGE_ADD_EXISTING = 1

    if NTDDI_VERSION >= NTDDI_WS08:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS08:
        pass
    # END IF
    INVALID_PROCESSOR_INDEX = 0xFFFFFFFF
    class _XSTATE_SAVE(ctypes.Structure):
        pass


        class _Struct_9(ctypes.Structure):
            pass


        class _Struct_10(ctypes.Structure):
            pass


        _Struct_10._fields_ = [
            ('Reserved1', LONG64),
            ('Reserved2', ULONG),
            ('Prev', POINTER(_XSTATE_SAVE)),
            ('Reserved3', PXSAVE_AREA),
            ('Thread', POINTER(_KTHREAD)),
            ('Reserved4', PVOID),
            ('Level', UCHAR),
        ]
        _Struct_9._Struct_10 = _Struct_10
        _Struct_9._anonymous_ = (
            '_Struct_10',
        )
        _Struct_9._fields_ = [
            ('_Struct_10', _Struct_9._Struct_10),
            ('XStateContext', XSTATE_CONTEXT),
        ]
        _XSTATE_SAVE._Struct_9 = _Struct_9
    _XSTATE_SAVE._anonymous_ = (
        '_Struct_9',
    )
    _XSTATE_SAVE._fields_ = [
            ('Prev', POINTER(_XSTATE_SAVE)),
            ('Thread', POINTER(_KTHREAD)),
            ('Level', UCHAR),
            ('XStateContext', XSTATE_CONTEXT),
            ('Dummy', ULONG),
            ('_Struct_9', _XSTATE_SAVE._Struct_9),
    ]
    XSTATE_SAVE = _XSTATE_SAVE
    PXSTATE_SAVE = POINTER(_XSTATE_SAVE)

    if defined(_AMD64_):
        pass
    elif defined(_ARM_) or defined(_ARM64_):
        pass
    elif defined(_X86_):
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    class _EXT_SET_PARAMETERS_V0(ctypes.Structure):
        pass


    _EXT_SET_PARAMETERS_V0._fields_ = [
        ('Version', ULONG),
        ('Reserved', ULONG),
        ('NoWakeTolerance', LONGLONG),
    ]
    EXT_SET_PARAMETERS = _EXT_SET_PARAMETERS_V0
    PEXT_SET_PARAMETERS = POINTER(_EXT_SET_PARAMETERS_V0)
    KT2_SET_PARAMETERS = EXT_SET_PARAMETERS
    PKT2_SET_PARAMETERS = POINTER(EXT_SET_PARAMETERS)
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
    class _KWAIT_CHAIN(ctypes.Structure):
        pass


    _KWAIT_CHAIN._fields_ = [
        ('Head', PVOID),
    ]
    KWAIT_CHAIN = _KWAIT_CHAIN
    PKWAIT_CHAIN = POINTER(_KWAIT_CHAIN)

    # Define external data.
    if defined(_NTDDK_) or defined(_NTIFS_) or defined(_NTHAL_) or defined(_WDMDDK_) or defined(_NTOSP_):
        KD_DEBUGGER_ENABLED = *KdDebuggerEnabled
        KD_DEBUGGER_NOT_PRESENT = *KdDebuggerNotPresent
    else:
        KD_DEBUGGER_ENABLED = KdDebuggerEnabled
        KD_DEBUGGER_NOT_PRESENT = KdDebuggerNotPresent
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # KdRefreshDebuggerPresent attempts to communicate with
    # the debugger host machine to refresh the state of
    # KdDebuggerNotPresent. It returns the state of
    # KdDebuggerNotPresent while the kd locks are held.
    # KdDebuggerNotPresent may immediately change state
    # after the kd locks are released so it may not
    # match the return value.
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    class _KD_OPTION(ENUM):
        KD_OPTION_SET_BLOCK_ENABLE = 1


    KD_OPTION = _KD_OPTION
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    # Pool Allocation routines (in pool.c)
    POOL_COLD_ALLOCATION = 256
    POOL_NX_ALLOCATION = 512

    # POOL_NX_OPTIN_AUTO makes non - paged pool allocations non - executable by
    # default without dynamically checking if this is supported by the
    # operating
    # system. This opt - in method should only be used by drivers that are
    # targeted
    # to run on operating system versions that are known to support NX non -
    # paged
    # pool allocations.
    # POOL_NX_OPTIN allows device drivers to dynamically opt - in to making
    # non - paged pool allocations non - executable by default based on
    # whether or not
    # this is supported by the version of the operating system. Device drivers
    # must call ExInitializeDriverRuntime (DrvRtPoolNxOptIn) during driver
    # initialization to dynamically opt - in. This opt - in method should be
    # used by
    # drivers that are deINT to run on versions of Windows that may or may not
    # support NX non - paged pool allocations.
    # In both cases, NonPagedPoolExecute should be used by drivers that need to
    # explicitly allocate executable memory from the non - paged pool.
    # POOL_NX_OPTOUT may be used to locally override the pool opt - in setting
    # for a
    # single source file. It is intended to be useful as an aid for porting
    # large
    # projects to NX pool, where most source files do not contain code that
    # needs
    # to allocate executable NonPaged pool
    # (and thus it may be convenient to set
    # the opt - in define
    # globally). In this case, if there existed a source file
    # that needed to manually control executable versus non - executable pool
    # opt - in
    # then that source file could define POOL_NX_OPTOUT to 0 in order to
    # override
    # the global default.

    if not defined(_X86_) and not defined(_AMD64_) and not defined(_NTOS_):

        # New platforms default to NonPagedPoolNx unless explicitly
        # overridden. The
        # exemption for _NTOS_ is there to allow NonPagedPool to be referenced
        # when
        # cracking pool types. This is henceforth the default for platforms
        # that
        # require a recompilation.
        # N.B. The remapping is carefully performed with a preprocessor define
        # such
        # that code which is NonPagedPoolNx - aware and which needs to crack
        # the
        # pool type may undefine the symbol.
        POOL_NX_OPTIN_AUTO = 1
    # END IF   not defined(_X86_) and not defined(_AMD64_) and not defined(_NTOSP_)

    if not POOL_NX_OPTOUT:
        if POOL_NX_OPTIN_AUTO:
            NonPagedPool = NonPagedPoolNx
            NonPagedPoolCacheAligned = NonPagedPoolNxCacheAligned
        elif POOL_NX_OPTIN:
            NonPagedPool = ExDefaultNonPagedPoolType
            NonPagedPoolCacheAligned = (
                (POOL_TYPE)(ExDefaultNonPagedPoolType + 4)
            )
        # END IF   POOL_NX_OPTIN_AUTO    # END IF   not POOL_NX_OPTOUT
    POOL_QUOTA_FAIL_INSTEAD_OF_RAISE = 8
    POOL_RAISE_IF_ALLOCATION_FAILURE = 16

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # _EX_POOL_PRIORITY_ provides a method for the system to handle requests
    # intelligently in low resource conditions.
    # LowPoolPriority should be used when it is acceptable to the driver for
    # the
    # mapping request to fail if the system is low on resources. An example of
    # this could be for a non - critical network connection where the driver
    # can
    # handle the failure case when system resources are close to being
    # depleted.
    # NormalPoolPriority should be used when it is acceptable to the driver
    # for the
    # mapping request to fail if the system is very low on resources. An
    # example
    # of this could be for a non - critical local filesystem request.
    # HighPoolPriority should be used when it is unacceptable to the driver
    # for the
    # mapping request to fail unless the system is completely out of resources.
    # An example of this would be the paging file path in a driver.
    # SpecialPool can be specified to bound the allocation at a page end (or
    # beginning). This should only be done on systems being debugged as the
    # memory cost is expensive.
    # N.B. These values are very carefully chosen so that the pool allocation
    # code can quickly crack the priority request.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if not defined(POOL_TAGGING):


        def ExAllocatePoolWithTag(a, b, c):
            return ExAllocatePoola,b
    # END IF  POOL_TAGGING

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if not defined(POOL_TAGGING):


        def ExAllocatePoolWithQuotaTag(a, b, c):
            return ExAllocatePoolWithQuotaa,b
    # END IF  POOL_TAGGING

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Routines to support fast mutexes.
    FM_LOCK_BIT = 0x1
    FM_LOCK_BIT_V = 0x0

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
        if defined(__cplusplus):
            pass
        # END IF
        if defined(__cplusplus):
            pass
        # END IF
    if defined(_X86_):
        pass
    else:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN2K
    if defined(_AMD64_) or defined(_ARM_) or defined(_ARM64_):


        def ExInterlockedCompareExchange64(Destination, Exchange, Comperand, Lock):
            return InterlockedCompareExchange64(Destination, *Exchange, *Comperand)
    else:


        def ExInterlockedCompareExchange64(Destination, Exchange, Comperand, Lock):
            return ExfInterlockedCompareExchange64Destination, Exchange, Comperand
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Define interlocked sequenced listhead functions.
    # A sequenced interlocked list is a singly linked list with a header that
    # contains the current depth and a sequence number. Each time an entry is
    # inserted or removed from the list the depth is updated and the sequence
    # number is incremented. This enables AMD64, ARM, and Pentium and later
    # machines to insert and remove from the list without the use of spinlocks.
    # (Ex)InitializeSListHead
        if defined(_WIN64) and (defined(_NTDRIVER_) or defined(_NTDDK_) or defined(_NTIFS_) or defined(_NTHAL_) or defined(_NTOSP_)):
            pass
    if not defined(_WINBASE_):
        else: #  defined(_WIN64) and (defined(_NTDRIVER_) or defined(_NTDDK_) or defined(_NTIFS_) or defined(_NTHAL_) or defined(_NTOSP_))

            # Since the following function will be compiled inline for user
            # code, the
            # initialization changes for x86 will only take effect if the user
            # code is
            # recompiled with this new header. For those binaries that are
            # recompiled with
            # this new code, it will not have to go through an extra step of
            # header
            # initialization on its first push or pop operation. Note that the
            # SLIST code
            # will still work perfectly even without the changes in this
            # initialization
            # function.
            if defined(_WIN64):
                # }
                #
                # #endif
                #
                # RtlZeroMemory(SListHead, ctypes.sizeof(SLIST_HEADER));
                RtlZeroMemory = ntdll.RtlZeroMemory
                RtlZeroMemory.restype = #endif            # END IF        # END IF   defined(_WIN64) and (defined(_NTDRIVER_) or defined(_NTDDK_) or defined(_NTIFS_) or defined(_NTHAL_) or defined(_NTOSP_))    # END IF   not defined(_WINBASE_)
    # (Ex)QueryDepthSList
        if defined(_NTDRIVER_) or defined(_NTDDK_) or defined(_NTIFS_) or defined(_NTHAL_) or defined(_NTOSP_):
            pass
            if defined(_WIN64):
                pass
            else:
                pass
            # END IF
        else: #  (defined(_NTDRIVER_) or defined(_NTDDK_) or defined(_NTIFS_) or defined(_NTHAL_) or defined(_NTOSP_))
            pass
        # END IF   (defined(_NTDRIVER_) or defined(_NTDDK_) or defined(_NTIFS_) or defined(_NTHAL_) or defined(_NTOSP_))
    if not defined(_X86_):
        pass
    else: #  not defined(_X86_)
        pass
    # END IF   not defined(_X86_)
    if not defined(_WINBASE_):
        pass
    # END IF   not defined(_WINBASE_)
        if not defined(_WINBASE_):
            pass
        # END IF   not defined(_WINBASE_)
    if not defined(_X86_):
        pass
        if defined(_WIN2K_COMPAT_SLIST_USAGE):
            pass
    else: #  not defined(_X86_)
        else: #  defined(_WIN2K_COMPAT_SLIST_USAGE)


            def ExInterlockedPopEntrySList(ListHead, Lock):
                return InterlockedPopEntrySListListHead


            def ExInterlockedPushEntrySList(ListHead, ListEntry, Lock):
                return InterlockedPushEntrySListListHead, ListEntry
        # END IF   defined(_WIN2K_COMPAT_SLIST_USAGE)

        if not defined(_WINBASE_):


            def InterlockedFlushSList(Head):
                return ExInterlockedFlushSListHead
        # END IF   not defined(_WINBASE_)    # END IF   not defined(_X86_)
    LOOKASIDE_MINIMUM_BLOCK_SIZE = (
        RTL_SIZEOF_THROUGH_FIELD (SLIST_ENTRY,
        Next),
    )

    # N.B. Note that this structure is not cache aligned to enable its use
    # in a larger containing structure.
    class _LOOKASIDE_LIST_EX(ctypes.Structure):
        pass


    _LOOKASIDE_LIST_EX._fields_ = [
        ('L', GENERAL_LOOKASIDE_POOL),
    ]
    LOOKASIDE_LIST_EX = _LOOKASIDE_LIST_EX
    PLOOKASIDE_LIST_EX = POINTER(_LOOKASIDE_LIST_EX)

    if NTDDI_VERSION >= NTDDI_VISTA:
        EX_LOOKASIDE_LIST_EX_FLAGS_RAISE_ON_FAIL = 0x00000001
        EX_LOOKASIDE_LIST_EX_FLAGS_FAIL_NO_RAISE = 0x00000002
        EX_MAXIMUM_LOOKASIDE_DEPTH_BASE = 256
        EX_MAXIMUM_LOOKASIDE_DEPTH_LIMIT = 1024
        kernel32 = ctypes.windll.kernel32

        # Entry = InterlockedPopEntrySList( & Lookaside - >L.ListHead);
        InterlockedPopEntrySList = kernel32.InterlockedPopEntrySList
        InterlockedPopEntrySList.restype = =
        # } else {
        # InterlockedPushEntrySList( & Lookaside - >L.ListHead, (PSLIST_ENTRY)Entry);
        InterlockedPushEntrySList = kernel32.InterlockedPushEntrySList
        InterlockedPushEntrySList.restype = else    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

    if defined(_X86_):
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        if not POOL_NX_OPTOUT and (POOL_NX_OPTIN or POOL_NX_OPTIN_AUTO):

            # If NX Pool Opt - In is enabled, then
            # ExInitializeNPagedLookasideList calls are
            # remapped to go through the following forceinline.
            # N.B. Should NX Pool Opt - In be enabled,
            # ExInitializeDriverRuntime(...) *MUST*
            # be invoked before any calls to ExInitializeNPagedLookasideList in
            # order for Opt - In to be correctly applied.
            if POOL_NX_OPTIN_AUTO:
                pass
            else:
                pass
            # END IF        # END IF   not POOL_NX_OPTOUT and (POOL_NX_OPTIN or POOL_NX_OPTIN_AUTO)    # END IF   (NTDDI_VERSION >= NTDDK_WIN2K)
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if defined(_WIN2K_COMPAT_SLIST_USAGE) and defined(_X86_):
        pass
    else:
        # Entry = InterlockedPopEntrySList( & Lookaside - >L.ListHead);
        InterlockedPopEntrySList = kernel32.InterlockedPopEntrySList
        InterlockedPopEntrySList.restype = =    # END IF
    if defined(_WIN2K_COMPAT_SLIST_USAGE) and defined(_X86_):
        pass
    else:
        pass
    # END IF
    if defined(_X86_):
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if defined(_WIN2K_COMPAT_SLIST_USAGE) and defined(_X86_):
        pass
    else:
        # Entry = InterlockedPopEntrySList( & Lookaside - >L.ListHead);
        InterlockedPopEntrySList = kernel32.InterlockedPopEntrySList
        InterlockedPopEntrySList.restype = =    # END IF
    if defined(_WIN2K_COMPAT_SLIST_USAGE) and defined(_X86_):
        pass
    else:
        # } else {
        # InterlockedPushEntrySList( & Lookaside - >L.ListHead,
        # (PSLIST_ENTRY)Entry);
        InterlockedPushEntrySList = kernel32.InterlockedPushEntrySList
        InterlockedPushEntrySList.restype = else    # END IF
            if defined(_PREFAST_):
                pass
            else:
                pass
            # END IF   _PREFAST_
        if NTDDI_VERSION >= NTDDI_WIN2K:
            pass
        # END IF
    if defined(_NTDDK_) or defined(_NTIFS_):
        pass
    # END IF
    # Raise status from kernel mode.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Common probe for write functions.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Worker Thread
    PWORKER_THREAD_ROUTINE = POINTER(WORKER_THREAD_ROUTINE)
    class _WORK_QUEUE_ITEM(ctypes.Structure):
        pass


    _WORK_QUEUE_ITEM._fields_ = [
        ('List', LIST_ENTRY),
        ('WorkerRoutine', PWORKER_THREAD_ROUTINE),
        ('PVOID Parameter', __volatile),
    ]
    WORK_QUEUE_ITEM = _WORK_QUEUE_ITEM
    PWORK_QUEUE_ITEM = POINTER(_WORK_QUEUE_ITEM)
        if defined(_NTDDK_):
            pass
        # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Define executive resource data structures.
    ERESOURCE_THREAD = ULONG_PTR
    PERESOURCE_THREAD = POINTER(ERESOURCE_THREAD)
    class _OWNER_ENTRY(ctypes.Structure):
        pass


    class _Struct_10(ctypes.Structure):
        pass


    class _Struct_11(ctypes.Structure):
        pass


    _Struct_11._fields_ = [
        ('IoPriorityBoosted', ULONG, 1),
        ('OwnerReferenced', ULONG, 1),
        ('IoQoSPriorityBoosted', ULONG, 1),
        ('OwnerCount', ULONG, 29),
    ]
    _Struct_10._Struct_11 = _Struct_11
    _Struct_10._anonymous_ = (
        '_Struct_11',
    )
    _Struct_10._fields_ = [
        ('_Struct_11', _Struct_10._Struct_11),
        ('TableSize', ULONG),
    ]
    _OWNER_ENTRY._Struct_10 = _Struct_10
    _OWNER_ENTRY._anonymous_ = (
        '_Struct_10',
    )
    _OWNER_ENTRY._fields_ = [
        ('OwnerThread', ERESOURCE_THREAD),
        ('_Struct_10', _OWNER_ENTRY._Struct_10),
    ]
    OWNER_ENTRY = _OWNER_ENTRY
    POWNER_ENTRY = POINTER(_OWNER_ENTRY)
    class _ERESOURCE(ctypes.Structure):
        pass


    class _Struct_11(ctypes.Structure):
        pass


    class _Struct_12(ctypes.Structure):
        pass


    _Struct_12._fields_ = [
        ('ReservedLowFlags', UCHAR),
        ('WaiterPriority', UCHAR),
    ]
    _Struct_11._Struct_12 = _Struct_12
    _Struct_11._anonymous_ = (
        '_Struct_12',
    )
    _Struct_11._fields_ = [
        ('Flag', USHORT),
        ('_Struct_12', _Struct_11._Struct_12),
    ]
    _ERESOURCE._Struct_11 = _Struct_11
    class _Union_2(ctypes.Union):
        pass


    _Union_2._fields_ = [
        ('Address', PVOID),
        ('CreatorBackTraceIndex', ULONG_PTR),
    ]
    _ERESOURCE._Union_2 = _Union_2
    _ERESOURCE._anonymous_ = (
        '_Struct_11',
        '_Union_2',
    )
    _ERESOURCE._fields_ = [
        ('SystemResourcesList', LIST_ENTRY),
        ('OwnerTable', POWNER_ENTRY),
        ('ActiveCount', SHORT), # non - zero and back.
        ('_Struct_11', _ERESOURCE._Struct_11),
        ('SharedWaiters', PVOID),
        ('ExclusiveWaiters', PVOID),
        ('OwnerEntry', OWNER_ENTRY), # of the shared owners.
        ('ActiveEntries', ULONG),
        ('ContentionCount', ULONG),
        ('NumberOfSharedWaiters', ULONG),
        ('NumberOfExclusiveWaiters', ULONG),
            ('Reserved2', PVOID),
        ('_Union_2', _ERESOURCE._Union_2),
        ('SpinLock', KSPIN_LOCK),
    ]
    ERESOURCE = _ERESOURCE
    PERESOURCE = POINTER(_ERESOURCE)
    if defined(_WIN64):
        pass
    # END IF
    # Values for ERESOURCE.Flag
    ResourceNeverExclusive = 0x0010
    ResourceReleaseByOtherThread = 0x0020
    ResourceOwnedExclusive = 0x0080
    RESOURCE_HASH_TABLE_SIZE = 64
    class _RESOURCE_HASH_ENTRY(ctypes.Structure):
        pass


    _RESOURCE_HASH_ENTRY._fields_ = [
        ('ListEntry', LIST_ENTRY),
        ('Address', PVOID),
        ('ContentionCount', ULONG),
        ('Number', ULONG),
    ]
    RESOURCE_HASH_ENTRY = _RESOURCE_HASH_ENTRY
    PRESOURCE_HASH_ENTRY = POINTER(_RESOURCE_HASH_ENTRY)
    class _RESOURCE_PERFORMANCE_DATA(ctypes.Structure):
        pass


    _RESOURCE_PERFORMANCE_DATA._fields_ = [
        ('ActiveResourceCount', ULONG),
        ('TotalResourceCount', ULONG),
        ('ExclusiveAcquire', ULONG),
        ('SharedFirstLevel', ULONG),
        ('SharedSecondLevel', ULONG),
        ('StarveFirstLevel', ULONG),
        ('StarveSecondLevel', ULONG),
        ('WaitForExclusive', ULONG),
        ('OwnerTableExpands', ULONG),
        ('MaximumTableExpand', ULONG),
        ('HashTable', LIST_ENTRY * RESOURCE_HASH_TABLE_SIZE),
    ]
    RESOURCE_PERFORMANCE_DATA = _RESOURCE_PERFORMANCE_DATA
    PRESOURCE_PERFORMANCE_DATA = POINTER(_RESOURCE_PERFORMANCE_DATA)

    # Define executive resource function prototypes.

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA or NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA or NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA or NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    # VOID
    # ExReleaseResource(
    # IN PERESOURCE Resource
    # );
    if PRAGMA_DEPRECATED_DDK:
        pass
    # END IF


    def ExReleaseResource(R):
        return (ExReleaseResourceLiteR)

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA or NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        FLAG_OWNER_POINTER_IS_THREAD = 0x1
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # ERESOURCE_THREAD
    # ExGetCurrentResourceThread(
    # VOID
    # );


    def ExGetCurrentResourceThread():
        return (ULONG_PTRPsGetCurrentThread)

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # An acquired resource is always owned shared, as shared ownership is a
    # subset
    # of exclusive ownership.
    ExIsResourceAcquiredLite = ExIsResourceAcquiredSharedLite

    # Rundown protection structure
    class _EX_RUNDOWN_REF(ctypes.Structure):
        pass


    class _Union_3(ctypes.Union):
        pass


    _Union_3._fields_ = [
        ('ULONG_PTR Count', __volatile),
        ('PVOID Ptr', __volatile),
    ]
    _EX_RUNDOWN_REF._Union_3 = _Union_3
    _EX_RUNDOWN_REF._anonymous_ = (
        '_Union_3',
    )
    _EX_RUNDOWN_REF._fields_ = [
        ('_Union_3', _EX_RUNDOWN_REF._Union_3),
    ]
    EX_RUNDOWN_REF = _EX_RUNDOWN_REF
    PEX_RUNDOWN_REF = POINTER(_EX_RUNDOWN_REF)

    # Opaque cache - aware rundown ref structure
    PEX_RUNDOWN_REF_CACHE_AWARE = POINTER()


    # Get previous mode

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Set timer resolution.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Query timer resolution.
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    # Subtract time zone bias from system time to get local time.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Add time zone bias to local time to get system time.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    PEX_TIMER = POINTER(_EX_TIMER)

    PEXT_CALLBACK = POINTER(EXT_CALLBACK)
    PEXT_DELETE_CALLBACK = POINTER(EXT_DELETE_CALLBACK)
    PEXT_CANCEL_PARAMETERS = PVOID
    class _EXT_DELETE_PARAMETERS(ctypes.Structure):
        pass


    _EXT_DELETE_PARAMETERS._fields_ = [
        ('Version', ULONG),
        ('Reserved', ULONG),
        ('DeleteCallback', PEXT_DELETE_CALLBACK),
        ('DeleteContext', PVOID),
    ]
    EXT_DELETE_PARAMETERS = _EXT_DELETE_PARAMETERS
    PEXT_DELETE_PARAMETERS = POINTER(_EXT_DELETE_PARAMETERS)
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        EX_TIMER_HIGH_RESOLUTION = 0x4
        EX_TIMER_NO_WAKE = 0x8
        EX_TIMER_UNLIMITED_TOLERANCE = (LONGLONG) - 1
        EX_TIMER_NOTIFICATION = 1UL << 31
    # END IF
    PCALLBACK_FUNCTION = POINTER(CALLBACK_FUNCTION)

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # suite support
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    # Rundown Locks
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXPSP2 or NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXPSP2 or NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    # TODO: t - chrisk - Need to update this to the Blue + 1 constant once
    # available.
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        EX_CARR_ALLOCATE_PAGED_POOL = 0x00000000
        EX_CARR_ALLOCATE_NONPAGED_POOL = 0x00000001
        EX_CARR_DISABLE_EXPANSION = 0x00000002
        EX_CARR_VALID_FLAGS = (
            EX_CARR_ALLOCATE_NONPAGED_POOL |
            EX_CARR_DISABLE_EXPANSION
        )
    # END IF
    # TODO: t - chrisk - Need to update this to the Blue + 1 constant once
    # available.

    if NTDDI_VERSION >= NTDDI_WINBLUE:
        pass
    # END IF
    # Define shared spinlock type and function prototypes.
    LONG = volatile
    EX_SPIN_LOCK = volatile
    PEX_SPIN_LOCK = POINTER(volatile)
    ALIGNED_EX_SPINLOCK = DECLSPEC_CACHEALIGN EX_SPIN_LOCK

    if NTDDI_VERSION >= NTDDI_VISTASP1:
        pass
    # END IF  #if (NTDDI_VERSION >= NTDDI_VISTASP1)
    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        pass
    # END IF
    # Define a block to hold the actual routine registration.
    PEX_CALLBACK_FUNCTION = POINTER(EX_CALLBACK_FUNCTION)
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF   #if (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)
    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        pass
    # END IF   #if (NTDDI_VERSION >= NTDDI_WIN10_RS3)
    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        pass
    # END IF   #if (NTDDI_VERSION >= NTDDI_WIN10_RS3)
    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        pass
    # END IF   #if (NTDDI_VERSION >= NTDDI_WIN10_RS1)
    # Registry kernel mode callbacks
    # Hook selector
    class _REG_NOTIFY_CLASS(ENUM):
        RegNtDeleteKey = 1
        RegNtPreDeleteKey = RegNtDeleteKey
        RegNtSetValueKey = 2
        RegNtPreSetValueKey = RegNtSetValueKey
        RegNtDeleteValueKey = 3
        RegNtPreDeleteValueKey = RegNtDeleteValueKey
        RegNtSetInformationKey = 4
        RegNtPreSetInformationKey = RegNtSetInformationKey
        RegNtRenameKey = 5
        RegNtPreRenameKey = RegNtRenameKey
        RegNtEnumerateKey = 6
        RegNtPreEnumerateKey = RegNtEnumerateKey
        RegNtEnumerateValueKey = 7
        RegNtPreEnumerateValueKey = RegNtEnumerateValueKey
        RegNtQueryKey = 8
        RegNtPreQueryKey = RegNtQueryKey
        RegNtQueryValueKey = 9
        RegNtPreQueryValueKey = RegNtQueryValueKey
        RegNtQueryMultipleValueKey = 10
        RegNtPreQueryMultipleValueKey = RegNtQueryMultipleValueKey
        RegNtPreCreateKey = 11
        RegNtPostCreateKey = 12
        RegNtPreOpenKey = 13
        RegNtPostOpenKey = 14
        RegNtKeyHandleClose = 15
        RegNtPreKeyHandleClose = RegNtKeyHandleClose
        RegNtPostDeleteKey = 16
        RegNtPostSetValueKey = 17
        RegNtPostDeleteValueKey = 18
        RegNtPostSetInformationKey = 19
        RegNtPostRenameKey = 20
        RegNtPostEnumerateKey = 21
        RegNtPostEnumerateValueKey = 22
        RegNtPostQueryKey = 23
        RegNtPostQueryValueKey = 24
        RegNtPostQueryMultipleValueKey = 25
        RegNtPostKeyHandleClose = 26
        RegNtPreCreateKeyEx = 27
        RegNtPostCreateKeyEx = 28
        RegNtPreOpenKeyEx = 29
        RegNtPostOpenKeyEx = 30
        RegNtPreFlushKey = 31
        RegNtPostFlushKey = 32
        RegNtPreLoadKey = 33
        RegNtPostLoadKey = 34
        RegNtPreUnLoadKey = 35
        RegNtPostUnLoadKey = 36
        RegNtPreQueryKeySecurity = 37
        RegNtPostQueryKeySecurity = 38
        RegNtPreSetKeySecurity = 39
        RegNtPostSetKeySecurity = 40
        RegNtCallbackObjectContextCleanup = 41
        RegNtPreRestoreKey = 42
        RegNtPostRestoreKey = 43
        RegNtPreSaveKey = 44
        RegNtPostSaveKey = 45
        RegNtPreReplaceKey = 46
        RegNtPostReplaceKey = 47
        RegNtPreQueryKeyName = 48
        RegNtPostQueryKeyName = 49
        MaxRegNtNotifyClass = 50


    REG_NOTIFY_CLASS = _REG_NOTIFY_CLASS

    # Parameter description for each notify class
    class _REG_DELETE_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_DELETE_KEY_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_DELETE_KEY_INFORMATION = _REG_DELETE_KEY_INFORMATION
    PREG_DELETE_KEY_INFORMATION
    #if (NTDDI_VERSION >= NTDDI_VISTA) = POINTER(_REG_DELETE_KEY_INFORMATION)
    REG_FLUSH_KEY_INFORMATION = _REG_DELETE_KEY_INFORMATION
    PREG_FLUSH_KEY_INFORMATION
    #endif // NTDDI_VERSION >= NTDDI_VISTA = POINTER(_REG_DELETE_KEY_INFORMATION)
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_VISTA
    class _REG_SET_VALUE_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_SET_VALUE_KEY_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('ValueName', PUNICODE_STRING), # IN
        ('TitleIndex', ULONG), # IN
        ('Type', ULONG), # IN
        ('Data', PVOID), # IN
        ('DataSize', ULONG), # IN
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_SET_VALUE_KEY_INFORMATION = _REG_SET_VALUE_KEY_INFORMATION
    PREG_SET_VALUE_KEY_INFORMATION = POINTER(_REG_SET_VALUE_KEY_INFORMATION)
    class _REG_DELETE_VALUE_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_DELETE_VALUE_KEY_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('ValueName', PUNICODE_STRING), # IN
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_DELETE_VALUE_KEY_INFORMATION = _REG_DELETE_VALUE_KEY_INFORMATION
    PREG_DELETE_VALUE_KEY_INFORMATION = POINTER(_REG_DELETE_VALUE_KEY_INFORMATION)
    class _REG_SET_INFORMATION_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_SET_INFORMATION_KEY_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('KeySetInformationClass', KEY_SET_INFORMATION_CLASS), # IN
        ('KeySetInformation', PVOID), # IN
        ('KeySetInformationLength', ULONG), # IN
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_SET_INFORMATION_KEY_INFORMATION = _REG_SET_INFORMATION_KEY_INFORMATION
    PREG_SET_INFORMATION_KEY_INFORMATION = POINTER(_REG_SET_INFORMATION_KEY_INFORMATION)
    class _REG_ENUMERATE_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_ENUMERATE_KEY_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('Index', ULONG), # IN
        ('KeyInformationClass', KEY_INFORMATION_CLASS), # IN
        ('KeyInformation', PVOID), # IN
        ('Length', ULONG), # IN
        ('ResultLength', PULONG), # OUT
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_ENUMERATE_KEY_INFORMATION = _REG_ENUMERATE_KEY_INFORMATION
    PREG_ENUMERATE_KEY_INFORMATION = POINTER(_REG_ENUMERATE_KEY_INFORMATION)
    class _REG_ENUMERATE_VALUE_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_ENUMERATE_VALUE_KEY_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('Index', ULONG), # IN
        ('KeyValueInformationClass', KEY_VALUE_INFORMATION_CLASS), # IN
        ('KeyValueInformation', PVOID), # IN
        ('Length', ULONG), # IN
        ('ResultLength', PULONG), # OUT
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_ENUMERATE_VALUE_KEY_INFORMATION = _REG_ENUMERATE_VALUE_KEY_INFORMATION
    PREG_ENUMERATE_VALUE_KEY_INFORMATION = POINTER(_REG_ENUMERATE_VALUE_KEY_INFORMATION)
    class _REG_QUERY_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_QUERY_KEY_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('KeyInformationClass', KEY_INFORMATION_CLASS), # IN
        ('KeyInformation', PVOID), # IN
        ('Length', ULONG), # IN
        ('ResultLength', PULONG), # OUT
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_QUERY_KEY_INFORMATION = _REG_QUERY_KEY_INFORMATION
    PREG_QUERY_KEY_INFORMATION = POINTER(_REG_QUERY_KEY_INFORMATION)
    class _REG_QUERY_VALUE_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_QUERY_VALUE_KEY_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('ValueName', PUNICODE_STRING), # IN
        ('KeyValueInformationClass', KEY_VALUE_INFORMATION_CLASS), # IN
        ('KeyValueInformation', PVOID), # IN
        ('Length', ULONG), # IN
        ('ResultLength', PULONG), # OUT
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_QUERY_VALUE_KEY_INFORMATION = _REG_QUERY_VALUE_KEY_INFORMATION
    PREG_QUERY_VALUE_KEY_INFORMATION = POINTER(_REG_QUERY_VALUE_KEY_INFORMATION)
    class _REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('ValueEntries', PKEY_VALUE_ENTRY), # IN
        ('EntryCount', ULONG), # IN
        ('ValueBuffer', PVOID), # IN
        ('BufferLength', PULONG), # IN OUT
        ('RequiredBufferLength', PULONG), # OUT
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION = _REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION
    PREG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION = POINTER(_REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION)
    class _REG_RENAME_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_RENAME_KEY_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('NewName', PUNICODE_STRING), # IN
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_RENAME_KEY_INFORMATION = _REG_RENAME_KEY_INFORMATION
    PREG_RENAME_KEY_INFORMATION = POINTER(_REG_RENAME_KEY_INFORMATION)
    class _REG_KEY_HANDLE_CLOSE_INFORMATION(ctypes.Structure):
        pass


    _REG_KEY_HANDLE_CLOSE_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_KEY_HANDLE_CLOSE_INFORMATION = _REG_KEY_HANDLE_CLOSE_INFORMATION
    PREG_KEY_HANDLE_CLOSE_INFORMATION = POINTER(_REG_KEY_HANDLE_CLOSE_INFORMATION)

    # .Net Only
    class _REG_CREATE_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_CREATE_KEY_INFORMATION._fields_ = [
        ('CompleteName', PUNICODE_STRING), # IN
        ('RootObject', PVOID), # IN
        ('ObjectType', PVOID), # new to Windows Vista
        ('CreateOptions', ULONG), # new to Windows Vista
        ('Class', PUNICODE_STRING), # new to Windows Vista
        ('SecurityDescriptor', PVOID), # new to Windows Vista
        ('SecurityQualityOfService', PVOID), # new to Windows Vista
        ('DesiredAccess', ACCESS_MASK), # new to Windows Vista
        ('GrantedAccess', ACCESS_MASK), # new to Windows Vista
        ('Disposition', PULONG), # new to Windows Vista
        ('ResultObject', POINTER(PVOID)), # new to Windows Vista
        ('CallContext', PVOID), # new to Windows Vista
        ('RootObjectContext', PVOID), # new to Windows Vista
        ('Transaction', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_CREATE_KEY_INFORMATION = _REG_CREATE_KEY_INFORMATION
    REG_OPEN_KEY_INFORMATION = _REG_CREATE_KEY_INFORMATION
    PREG_CREATE_KEY_INFORMATION = POINTER(_REG_CREATE_KEY_INFORMATION)
    PREG_OPEN_KEY_INFORMATION = POINTER(_REG_CREATE_KEY_INFORMATION)
    class _REG_CREATE_KEY_INFORMATION_V1(ctypes.Structure):
        pass


    _REG_CREATE_KEY_INFORMATION_V1._fields_ = [
        ('CompleteName', PUNICODE_STRING), # IN
        ('RootObject', PVOID), # IN
        ('ObjectType', PVOID), # new to Windows Vista
        ('Options', ULONG), # new to Windows Vista
        ('Class', PUNICODE_STRING), # new to Windows Vista
        ('SecurityDescriptor', PVOID), # new to Windows Vista
        ('SecurityQualityOfService', PVOID), # new to Windows Vista
        ('DesiredAccess', ACCESS_MASK), # new to Windows Vista
        ('GrantedAccess', ACCESS_MASK), # new to Windows Vista
        ('Disposition', PULONG), # new to Windows Vista
        ('ResultObject', POINTER(PVOID)), # new to Windows Vista
        ('CallContext', PVOID), # new to Windows Vista
        ('RootObjectContext', PVOID), # new to Windows Vista
        ('Transaction', PVOID), # new to Windows Vista
        ('Version', ULONG_PTR), # following is new to Windows 7
        ('RemainingName', PUNICODE_STRING), # the true path left to parse
        ('Wow64Flags', ULONG), # Wow64 specific flags gotten from DesiredAccess input
        ('Attributes', ULONG), # ObjectAttributes - >Attributes
        ('CheckAccessMode', KPROCESSOR_MODE), # mode used for the security checks
    ]
    REG_CREATE_KEY_INFORMATION_V1 = _REG_CREATE_KEY_INFORMATION_V1
    REG_OPEN_KEY_INFORMATION_V1 = _REG_CREATE_KEY_INFORMATION_V1
    PREG_CREATE_KEY_INFORMATION_V1 = POINTER(_REG_CREATE_KEY_INFORMATION_V1)
    PREG_OPEN_KEY_INFORMATION_V1 = POINTER(_REG_CREATE_KEY_INFORMATION_V1)
    class _REG_POST_OPERATION_INFORMATION(ctypes.Structure):
        pass


    _REG_POST_OPERATION_INFORMATION._fields_ = [
        ('Object', PVOID), # IN
        ('Status', NTSTATUS), # IN

        # new to Windows Vista; identical with the pre information that was
        # sent
        ('PreInformation', PVOID),

        # new to Windows Vista; callback can now change the outcome of the
        # operation
        ('ReturnStatus', NTSTATUS),
        ('CallContext', PVOID), # new to Windows Vista
        ('ObjectContext', PVOID), # new to Windows Vista
        ('Reserved', PVOID), # new to Windows Vista
    ]
    REG_POST_OPERATION_INFORMATION = _REG_POST_OPERATION_INFORMATION
    PREG_POST_OPERATION_INFORMATION = POINTER(_REG_POST_OPERATION_INFORMATION)

    # end .Net Only
    # XP only
    class _REG_PRE_CREATE_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_PRE_CREATE_KEY_INFORMATION._fields_ = [
        ('CompleteName', PUNICODE_STRING), # IN
    ]
    REG_PRE_CREATE_KEY_INFORMATION = _REG_PRE_CREATE_KEY_INFORMATION
    REG_PRE_OPEN_KEY_INFORMATION = _REG_PRE_CREATE_KEY_INFORMATION
    PREG_PRE_CREATE_KEY_INFORMATION = POINTER(_REG_PRE_CREATE_KEY_INFORMATION)
    PREG_PRE_OPEN_KEY_INFORMATION = POINTER(_REG_PRE_CREATE_KEY_INFORMATION)
    class _REG_POST_CREATE_KEY_INFORMATION(ctypes.Structure):
        pass


    _REG_POST_CREATE_KEY_INFORMATION._fields_ = [
        ('CompleteName', PUNICODE_STRING), # IN
        ('Object', PVOID), # IN
        ('Status', NTSTATUS), # IN
    ]
    REG_POST_CREATE_KEY_INFORMATION = _REG_POST_CREATE_KEY_INFORMATION
    REG_POST_OPEN_KEY_INFORMATION = _REG_POST_CREATE_KEY_INFORMATION
    PREG_POST_CREATE_KEY_INFORMATION = POINTER(_REG_POST_CREATE_KEY_INFORMATION)
    PREG_POST_OPEN_KEY_INFORMATION = POINTER(_REG_POST_CREATE_KEY_INFORMATION)

    # end XP only
    # new to Windows Vista
    if NTDDI_VERSION >= NTDDI_VISTA:
        class _REG_LOAD_KEY_INFORMATION(ctypes.Structure):
            pass


        _REG_LOAD_KEY_INFORMATION._fields_ = [
            ('Object', PVOID),
            ('KeyName', PUNICODE_STRING),
            ('SourceFile', PUNICODE_STRING),
            ('Flags', ULONG),
            ('TrustClassObject', PVOID),
            ('UserEvent', PVOID),
            ('DesiredAccess', ACCESS_MASK),
            ('RootHandle', PHANDLE),
            ('CallContext', PVOID),
            ('ObjectContext', PVOID),
            ('Reserved', PVOID),
        ]
        REG_LOAD_KEY_INFORMATION = _REG_LOAD_KEY_INFORMATION
        PREG_LOAD_KEY_INFORMATION = POINTER(_REG_LOAD_KEY_INFORMATION)
        class _REG_UNLOAD_KEY_INFORMATION(ctypes.Structure):
            pass


        _REG_UNLOAD_KEY_INFORMATION._fields_ = [
            ('Object', PVOID),
            ('UserEvent', PVOID),
            ('CallContext', PVOID),
            ('ObjectContext', PVOID),
            ('Reserved', PVOID),
        ]
        REG_UNLOAD_KEY_INFORMATION = _REG_UNLOAD_KEY_INFORMATION
        PREG_UNLOAD_KEY_INFORMATION = POINTER(_REG_UNLOAD_KEY_INFORMATION)
        class _REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION(ctypes.Structure):
            pass


        _REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION._fields_ = [
            ('Object', PVOID),
            ('ObjectContext', PVOID),
            ('Reserved', PVOID),
        ]
        REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION = _REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION
        PREG_CALLBACK_CONTEXT_CLEANUP_INFORMATION = POINTER(_REG_CALLBACK_CONTEXT_CLEANUP_INFORMATION)
        class _REG_QUERY_KEY_SECURITY_INFORMATION(ctypes.Structure):
            pass


        _REG_QUERY_KEY_SECURITY_INFORMATION._fields_ = [
            ('Object', PVOID),
            ('SecurityInformation', PSECURITY_INFORMATION), # IN
            ('SecurityDescriptor', PSECURITY_DESCRIPTOR), # INOUT
            ('Length', PULONG), # INOUT
            ('CallContext', PVOID),
            ('ObjectContext', PVOID),
            ('Reserved', PVOID),
        ]
        REG_QUERY_KEY_SECURITY_INFORMATION = _REG_QUERY_KEY_SECURITY_INFORMATION
        PREG_QUERY_KEY_SECURITY_INFORMATION = POINTER(_REG_QUERY_KEY_SECURITY_INFORMATION)
        class _REG_SET_KEY_SECURITY_INFORMATION(ctypes.Structure):
            pass


        _REG_SET_KEY_SECURITY_INFORMATION._fields_ = [
            ('Object', PVOID),
            ('SecurityInformation', PSECURITY_INFORMATION), # IN
            ('SecurityDescriptor', PSECURITY_DESCRIPTOR), # IN
            ('CallContext', PVOID),
            ('ObjectContext', PVOID),
            ('Reserved', PVOID),
        ]
        REG_SET_KEY_SECURITY_INFORMATION = _REG_SET_KEY_SECURITY_INFORMATION
        PREG_SET_KEY_SECURITY_INFORMATION = POINTER(_REG_SET_KEY_SECURITY_INFORMATION)

        # new in Vista SP2 - Restore, Save, Replace
        class _REG_RESTORE_KEY_INFORMATION(ctypes.Structure):
            pass


        _REG_RESTORE_KEY_INFORMATION._fields_ = [
            ('Object', PVOID),
            ('FileHandle', HANDLE),
            ('Flags', ULONG),
            ('CallContext', PVOID),
            ('ObjectContext', PVOID),
            ('Reserved', PVOID),
        ]
        REG_RESTORE_KEY_INFORMATION = _REG_RESTORE_KEY_INFORMATION
        PREG_RESTORE_KEY_INFORMATION = POINTER(_REG_RESTORE_KEY_INFORMATION)
        class _REG_SAVE_KEY_INFORMATION(ctypes.Structure):
            pass


        _REG_SAVE_KEY_INFORMATION._fields_ = [
            ('Object', PVOID),
            ('FileHandle', HANDLE),
            ('Format', ULONG),
            ('CallContext', PVOID),
            ('ObjectContext', PVOID),
            ('Reserved', PVOID),
        ]
        REG_SAVE_KEY_INFORMATION = _REG_SAVE_KEY_INFORMATION
        PREG_SAVE_KEY_INFORMATION = POINTER(_REG_SAVE_KEY_INFORMATION)
        class _REG_REPLACE_KEY_INFORMATION(ctypes.Structure):
            pass


        _REG_REPLACE_KEY_INFORMATION._fields_ = [
            ('Object', PVOID),
            ('OldFileName', PUNICODE_STRING),
            ('NewFileName', PUNICODE_STRING),
            ('CallContext', PVOID),
            ('ObjectContext', PVOID),
            ('Reserved', PVOID),
        ]
        REG_REPLACE_KEY_INFORMATION = _REG_REPLACE_KEY_INFORMATION
        PREG_REPLACE_KEY_INFORMATION = POINTER(_REG_REPLACE_KEY_INFORMATION)
    # END IF   NTDDI_VERSION >= NTDDI_VISTA
    class _REG_QUERY_KEY_NAME(ctypes.Structure):
        pass


    _REG_QUERY_KEY_NAME._fields_ = [
        ('Object', PVOID),
        ('ObjectNameInfo', POBJECT_NAME_INFORMATION),
        ('Length', ULONG),
        ('ReturnLength', PULONG),
        ('CallContext', PVOID),
        ('ObjectContext', PVOID),
        ('Reserved', PVOID),
    ]
    REG_QUERY_KEY_NAME = _REG_QUERY_KEY_NAME
    PREG_QUERY_KEY_NAME = POINTER(_REG_QUERY_KEY_NAME)
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_VISTA
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN8
    # Priority increment definitions. The comment for each definition gives
    # the names of the system services that use the definition when satisfying
    # a wait.
    # Priority increment used when satisfying a wait on an executive event
    # (NtPulseEvent and NtSetEvent)
    EVENT_INCREMENT = 1

    # Priority increment when no I/O has been done. This is used by device
    # and file system drivers when completing an IRP (IoCompleteRequest).
    IO_NO_INCREMENT = 0

    # Priority increment for completing CD - ROM I/O. This is used by CD - ROM
    # device
    # and file system drivers when completing an IRP (IoCompleteRequest)
    IO_CD_ROM_INCREMENT = 1

    # Priority increment for completing disk I/O. This is used by disk device
    # and file system drivers when completing an IRP (IoCompleteRequest)
    IO_DISK_INCREMENT = 1

    # Priority increment for completing keyboard I/O. This is used by keyboard
    # device drivers when completing an IRP (IoCompleteRequest)
    IO_KEYBOARD_INCREMENT = 6

    # Priority increment for completing mailslot I/O. This is used by the mail
    # -
    # slot file system driver when completing an IRP (IoCompleteRequest).
    IO_MAILSLOT_INCREMENT = 2

    # Priority increment for completing mouse I/O. This is used by mouse device
    # drivers when completing an IRP (IoCompleteRequest)
    IO_MOUSE_INCREMENT = 6

    # Priority increment for completing named pipe I/O. This is used by the
    # named pipe file system driver when completing an IRP (IoCompleteRequest).
    IO_NAMED_PIPE_INCREMENT = 2

    # Priority increment for completing network I/O. This is used by network
    # device and network file system drivers when completing an IRP
    # (IoCompleteRequest).
    IO_NETWORK_INCREMENT = 2

    # Priority increment for completing parallel I/O. This is used by parallel
    # device drivers when completing an IRP (IoCompleteRequest)
    IO_PARALLEL_INCREMENT = 1

    # Priority increment for completing serial I/O. This is used by serial
    # device
    # drivers when completing an IRP (IoCompleteRequest)
    IO_SERIAL_INCREMENT = 2

    # Priority increment for completing sound I/O. This is used by sound device
    # drivers when completing an IRP (IoCompleteRequest)
    IO_SOUND_INCREMENT = 8

    # Priority increment for completing video I/O. This is used by video device
    # drivers when completing an IRP (IoCompleteRequest)
    IO_VIDEO_INCREMENT = 1

    # Priority increment used when satisfying a wait on an executive semaphore
    # (NtReleaseSemaphore)
    SEMAPHORE_INCREMENT = 1

    # Indicates the system may do I/O to physical addresses above 4 GB.
    # Provides a known bad pointer address which always bugchecks if
    # acccessed. This gives drivers a way to find pointer bugs by
    # initializing invalid pointers to this value.
    MM_BAD_POINTER = (
        __pragma(warning(push))                                    __pragma(warning(disable:4995))                            *(PVOID *) MmBadPointer                                    __pragma(warning(pop))
    )

    # Define the old maximum disk transfer size to be used by MM and Cache
    # Manager. Current transfer sizes can typically be much larger.
    MM_MAXIMUM_DISK_IO_SIZE = 0x10000

    # + +
    # ULONG_PTR
    # ROUND_TO_PAGES (
    # _In_ ULONG_PTR Size
    # )
    # Routine Description:
    # The ROUND_TO_PAGES macro takes a size in bytes and rounds it up to a
    # multiple of the page size.
    # NOTE: This macro fails for values 0xFFFFFFFF - (PAGE_SIZE - 1).
    # Arguments:
    # Size - Size in bytes to round up to a page multiple.
    # Return Value:
    # Returns the size rounded up to a multiple of the page size.
    # - -


    def ROUND_TO_PAGES(Size):
        return (ULONG_PTRSize + PAGE_SIZE - 1) & ~(PAGE_SIZE - 1)

    # + +
    # ULONG
    # BYTES_TO_PAGES (
    # _In_ ULONG Size
    # )
    # Routine Description:
    # The BYTES_TO_PAGES macro takes the size in bytes and calculates the
    # number of pages required to contain the bytes.
    # Arguments:
    # Size - Size in bytes.
    # Return Value:
    # Returns the number of pages required to contain the specified size.
    # - -


    def BYTES_TO_PAGES(Size):
        return ((Size >> PAGE_SHIFT) + ((Size & (PAGE_SIZE - 1)) != 0))

    # + +
    # ULONG
    # BYTE_OFFSET (
    # _In_ PVOID Va
    # )
    # Routine Description:
    # The BYTE_OFFSET macro takes a virtual address and returns the byte offset
    # of that address within the page.
    # Arguments:
    # Va - Virtual address.
    # Return Value:
    # Returns the byte offset portion of the virtual address.
    # - -


    def BYTE_OFFSET(Va):
        return (ULONG(LONG_PTRVa & (PAGE_SIZE - 1)))

    # + +
    # PVOID
    # PAGE_ALIGN (
    # _In_ PVOID Va
    # )
    # Routine Description:
    # The PAGE_ALIGN macro takes a virtual address and returns a page - aligned
    # virtual address for that page.
    # Arguments:
    # Va - Virtual address.
    # Return Value:
    # Returns the page aligned virtual address.
    # - -


    def PAGE_ALIGN(Va):
        return (PVOID(ULONG_PTRVa & ~(PAGE_SIZE - 1)))

    # + +
    # SIZE_T
    # ADDRESS_AND_SIZE_TO_SPAN_PAGES (
    # _In_ PVOID Va,
    # _In_ SIZE_T Size
    # )
    # Routine Description:
    # The ADDRESS_AND_SIZE_TO_SPAN_PAGES macro takes a virtual address and
    # size and returns the number of pages spanned by the size.
    # Arguments:
    # Va - Virtual address.
    # Size - Size in bytes.
    # Return Value:
    # Returns the number of pages spanned by the size.
    # - -


    def ADDRESS_AND_SIZE_TO_SPAN_PAGES(Va, Size):
        return ((BYTE_OFFSET Va + (SIZE_T Size) + (PAGE_SIZE - 1)) >> PAGE_SHIFT)

    if PRAGMA_DEPRECATED_DDK:
        pass
    # END IF


    def COMPUTE_PAGES_SPANNED(Va, Size):
        return ADDRESS_AND_SIZE_TO_SPAN_PAGESVa,Size

    # + +
    # PPFN_NUMBER
    # MmGetMdlPfnArray (
    # _In_ PMDL Mdl
    # )
    # Routine Description:
    # The MmGetMdlPfnArray routine returns the virtual address of the
    # first element of the array of physical page numbers associated with
    # the MDL.
    # Arguments:
    # Mdl - Pointer to an MDL.
    # Return Value:
    # Returns the virtual address of the first element of the array of
    # physical page numbers associated with the MDL.
    # - -


    def MmGetMdlPfnArray(Mdl):
        return PPFN_NUMBER(Mdl + 1)

    # + +
    # PVOID
    # MmGetMdlVirtualAddress (
    # _In_ PMDL Mdl
    # )
    # Routine Description:
    # The MmGetMdlVirtualAddress returns the virtual address of the buffer
    # described by the Mdl.
    # Arguments:
    # Mdl - Pointer to an MDL.
    # Return Value:
    # Returns the virtual address of the buffer described by the Mdl
    # - -


    def MmGetMdlVirtualAddress(Mdl):
        return PVOID (PCHAR (Mdl - >StartVa) + Mdl - >ByteOffset)

    # + +
    # ULONG
    # MmGetMdlByteCount (
    # _In_ PMDL Mdl
    # )
    # Routine Description:
    # The MmGetMdlByteCount returns the length in bytes of the buffer
    # described by the Mdl.
    # Arguments:
    # Mdl - Pointer to an MDL.
    # Return Value:
    # Returns the byte count of the buffer described by the Mdl
    # - -


    def MmGetMdlByteCount(Mdl):
        return (Mdl - >ByteCount)

    # + +
    # ULONG
    # MmGetMdlByteOffset (
    # _In_ PMDL Mdl
    # )
    # Routine Description:
    # The MmGetMdlByteOffset returns the byte offset within the page
    # of the buffer described by the Mdl.
    # Arguments:
    # Mdl - Pointer to an MDL.
    # Return Value:
    # Returns the byte offset within the page of the buffer described by the
    # Mdl
    # - -


    def MmGetMdlByteOffset(Mdl):
        return (Mdl - >ByteOffset)

    # + +
    # PVOID
    # MmGetMdlStartVa (
    # _In_ PMDL Mdl
    # )
    # Routine Description:
    # The MmGetMdlBaseVa returns the virtual address of the buffer
    # described by the Mdl rounded down to the nearest page.
    # Arguments:
    # Mdl - Pointer to an MDL.
    # Return Value:
    # Returns the starting virtual address of the MDL.
    # - -


    def MmGetMdlBaseVa(Mdl):
        return (Mdl - >StartVa)


    class _MM_SYSTEM_SIZE(ENUM):
        MmSmallSystem = 1
        MmMediumSystem = 2
        MmLargeSystem = 3


    MM_SYSTEMSIZE = _MM_SYSTEM_SIZE
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    # I/O support routines.
    if NTDDI_VERSION >= NTDDI_WIN2K:

        # @[comment("MVI_tracked")]    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        class _MM_PHYSICAL_ADDRESS_LIST(ctypes.Structure):
            pass


        _MM_PHYSICAL_ADDRESS_LIST._fields_ = [
            ('PhysicalAddress', PHYSICAL_ADDRESS),
            ('NumberOfBytes', SIZE_T),
        ]
        MM_PHYSICAL_ADDRESS_LIST = _MM_PHYSICAL_ADDRESS_LIST
        PMM_PHYSICAL_ADDRESS_LIST = POINTER(_MM_PHYSICAL_ADDRESS_LIST)
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        MM_PERMANENT_ADDRESS_IS_IO_SPACE = 0x1
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        PMM_MDL_ROUTINE = POINTER(MM_MDL_ROUTINE)
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    # _MM_PAGE_PRIORITY_ provides a method for the system to handle requests
    # intelligently in low resource conditions.
    # LowPagePriority should be used when it is acceptable to the driver for
    # the
    # mapping request to fail if the system is low on resources. An example of
    # this could be for a non - critical network connection where the driver
    # can
    # handle the failure case when system resources are close to being
    # depleted.
    # NormalPagePriority should be used when it is acceptable to the driver
    # for the
    # mapping request to fail if the system is very low on resources. An
    # example
    # of this could be for a non - critical local filesystem request.
    # HighPagePriority should be used when it is unacceptable to the driver
    # for the
    # mapping request to fail unless the system is completely out of resources.
    # An example of this would be the paging file path in a driver.
    class _MM_PAGE_PRIORITY(ENUM):
        LowPagePriority = 1
        NormalPagePriority = 16
        HighPagePriority = 32


    MM_PAGE_PRIORITY = _MM_PAGE_PRIORITY
    MdlMappingNoWrite = 0x80000000
    MdlMappingNoExecute = 0x40000000

    # Note: This function is not available in WDM 1.0

    if NTDDI_VERSION >= NTDDI_WIN2K:
        if not POOL_NX_OPTOUT and (POOL_NX_OPTIN or POOL_NX_OPTIN_AUTO):

            # If NX Pool Opt - In is enabled, then
            # MmMapLockedPagesSpecifyCache calls are
            # remapped to go through the following forceinline.
            # N.B. Should NX Pool Opt - In be enabled,
            # ExInitializeDriverRuntime(...) *MUST*
            # be invoked before any calls to MmMapLockedPagesSpecifyCache in
            # order
            # for Opt - In to be correctly applied.
            if POOL_NX_OPTIN_AUTO:
                pass
            else:
                pass
            # END IF        # END IF   not POOL_NX_OPTOUT and (POOL_NX_OPTIN or POOL_NX_OPTIN_AUTO)    # END IF   (NTDDI_VERSION >= NTDDI_WIN2K)
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    MM_DONT_ZERO_ALLOCATION = 0x00000001
    MM_ALLOCATE_FROM_LOCAL_NODE_ONLY = 0x00000002
    MM_ALLOCATE_FULLY_REQUIRED = 0x00000004
    MM_ALLOCATE_NO_WAIT = 0x00000008
    MM_ALLOCATE_PREFER_CONTIGUOUS = 0x00000010
    MM_ALLOCATE_REQUIRE_CONTIGUOUS_CHUNKS = 0x00000020
    MM_ALLOCATE_FAST_LARGE_PAGES = 0x00000040
    MM_ALLOCATE_TRIM_IF_NECESSARY = 0x00000080
    MM_ALLOCATE_AND_HOT_REMOVE = 0x00000100

    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        MM_FREE_MDL_PAGES_ZERO = 0x1
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        NODE_REQUIREMENT = ULONG
        MM_ANY_NODE_OK = 0x80000000
    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        class _MM_MDL_PAGE_CONTENTS_STATE(ENUM):
            MmMdlPageContentsDynamic = 1
            MmMdlPageContentsInvariant = 2
            MmMdlPageContentsQuery = 3


        MM_MDL_PAGE_CONTENTS_STATE = _MM_MDL_PAGE_CONTENTS_STATE
        PMM_MDL_PAGE_CONTENTS_STATE = _MM_MDL_PAGE_CONTENTS_STATE
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if PRAGMA_DEPRECATED_DDK:
        pass
    # END IF
    # Define an empty typedef for the _DRIVER_OBJECT structure so it may be
    # referenced by function types before it is actually defined.
    _DRIVER_OBJECT = struct

    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    # Security operation codes
    class _SECURITY_OPERATION_CODE(ENUM):
        SetSecurityDescriptor = 1
        QuerySecurityDescriptor = 2
        DeleteSecurityDescriptor = 3
        AssignSecurityDescriptor = 4


    SECURITY_OPERATION_CODE = _SECURITY_OPERATION_CODE
    PSECURITY_OPERATION_CODE = POINTER(_SECURITY_OPERATION_CODE)

    # Data structure used to capture subject security context
    # for access validations and auditing.
    # THE FIELDS OF THIS DATA STRUCTURE SHOULD BE CONSIDERED OPAQUE
    # BY ALL EXCEPT THE SECURITY ROUTINES.
    class _SECURITY_SUBJECT_CONTEXT(ctypes.Structure):
        pass


    _SECURITY_SUBJECT_CONTEXT._fields_ = [
        ('ClientToken', PACCESS_TOKEN),
        ('ImpersonationLevel', SECURITY_IMPERSONATION_LEVEL),
        ('PrimaryToken', PACCESS_TOKEN),
        ('ProcessAuditId', PVOID),
    ]
    SECURITY_SUBJECT_CONTEXT = _SECURITY_SUBJECT_CONTEXT
    PSECURITY_SUBJECT_CONTEXT = POINTER(_SECURITY_SUBJECT_CONTEXT)

    # /////////////////////////////////////////////////////////////////////////////
    #
    # //
    # ACCESS_STATE and related structures    //
    # //
    # /////////////////////////////////////////////////////////////////////////////
    #
    # Initial Privilege Set - Room for three privileges, which should
    # be enough for most applications. This structure exists so that
    # it can be embedded in an ACCESS_STATE structure. Use PRIVILEGE_SET
    # for all other references to Privilege sets.
    INITIAL_PRIVILEGE_COUNT = 3
    class _INITIAL_PRIVILEGE_SET(ctypes.Structure):
        pass


    _INITIAL_PRIVILEGE_SET._fields_ = [
        ('PrivilegeCount', ULONG),
        ('Control', ULONG),
        ('Privilege', LUID_AND_ATTRIBUTES * INITIAL_PRIVILEGE_COUNT),
    ]
    INITIAL_PRIVILEGE_SET = _INITIAL_PRIVILEGE_SET
    PINITIAL_PRIVILEGE_SET = POINTER(_INITIAL_PRIVILEGE_SET)

    # Combine the information that describes the state
    # of an access - in - progress into a single structure
    class _ACCESS_STATE(ctypes.Structure):
        pass


    class Privileges(ctypes.Union):
        pass


    Privileges._fields_ = [
        ('InitialPrivilegeSet', INITIAL_PRIVILEGE_SET),
        ('PrivilegeSet', PRIVILEGE_SET),
    ]
    _ACCESS_STATE.Privileges = Privileges
    _ACCESS_STATE._fields_ = [
        ('OperationID', LUID), # Currently unused, replaced by TransactionId in AUX_ACCESS_DATA
        ('SecurityEvaluated', BOOLEAN),
        ('GenerateAudit', BOOLEAN),
        ('GenerateOnClose', BOOLEAN),
        ('PrivilegesAllocated', BOOLEAN),
        ('Flags', ULONG),
        ('RemainingDesiredAccess', ACCESS_MASK),
        ('PreviouslyGrantedAccess', ACCESS_MASK),
        ('OriginalDesiredAccess', ACCESS_MASK),
        ('SubjectSecurityContext', SECURITY_SUBJECT_CONTEXT),
        ('SecurityDescriptor', PSECURITY_DESCRIPTOR), # it stores SD supplied by caller when creating a new object.
        ('AuxData', PVOID),
        ('Privileges', _ACCESS_STATE.Privileges),
        ('AuditPrivileges', BOOLEAN),
        ('ObjectName', UNICODE_STRING),
        ('ObjectTypeName', UNICODE_STRING),
    ]
    ACCESS_STATE = _ACCESS_STATE
    PACCESS_STATE = POINTER(_ACCESS_STATE)
    PNTFS_DEREF_EXPORTED_SECURITY_DESCRIPTOR = POINTER(NTFS_DEREF_EXPORTED_SECURITY_DESCRIPTOR)

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF
    if defined(SE_NTFS_WORLD_CACHE):
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Types of images.
    class _SE_IMAGE_TYPE(ENUM):
        SeImageTypeElamDriver = 0
        SeImageTypeDriver = 1
        SeImageTypePlatformSecureFile = 2
        SeImageTypeDynamicCodeFile = 3
        SeImageTypeMax = 4


    SE_IMAGE_TYPE = _SE_IMAGE_TYPE
    PSE_IMAGE_TYPE = POINTER(_SE_IMAGE_TYPE)
    PBDCB_IMAGE_INFORMATION = POINTER(_BDCB_IMAGE_INFORMATION)

    PSE_IMAGE_VERIFICATION_CALLBACK_FUNCTION = POINTER(SE_IMAGE_VERIFICATION_CALLBACK_FUNCTION)
    class _SE_IMAGE_VERIFICATION_CALLBACK_TYPE(ENUM):
        SeImageVerificationCallbackInformational = 0


    SE_IMAGE_VERIFICATION_CALLBACK_TYPE = _SE_IMAGE_VERIFICATION_CALLBACK_TYPE
    PSE_IMAGE_VERIFICATION_CALLBACK_TYPE = POINTER(_SE_IMAGE_VERIFICATION_CALLBACK_TYPE)
    SE_IMAGE_VERIFICATION_CALLBACK_TOKEN = PVOID
    PSE_IMAGE_VERIFICATION_CALLBACK_TOKEN = POINTER(PVOID)
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        pass
    # END IF
    if not defined(_PSGETCURRENTTHREAD_):
        _PSGETCURRENTTHREAD_ = 1
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    # Define I/O system data structure type codes. Each major data structure in
    # the I/O system has a type code The type field in each structure is at the
    # same offset. The following values can be used to determine which type of
    # data structure a pointer refers to.
    IO_TYPE_ADAPTER = 0x00000001
    IO_TYPE_CONTROLLER = 0x00000002
    IO_TYPE_DEVICE = 0x00000003
    IO_TYPE_DRIVER = 0x00000004
    IO_TYPE_FILE = 0x00000005
    IO_TYPE_IRP = 0x00000006
    IO_TYPE_MASTER_ADAPTER = 0x00000007
    IO_TYPE_OPEN_PACKET = 0x00000008
    IO_TYPE_TIMER = 0x00000009
    IO_TYPE_VPB = 0x0000000A
    IO_TYPE_ERROR_LOG = 0x0000000B
    IO_TYPE_ERROR_MESSAGE = 0x0000000C
    IO_TYPE_DEVICE_OBJECT_EXTENSION = 0x0000000D

    # Define the major function codes for IRPs.
    IRP_MJ_CREATE = 0x00
    IRP_MJ_CREATE_NAMED_PIPE = 0x01
    IRP_MJ_CLOSE = 0x02
    IRP_MJ_READ = 0x03
    IRP_MJ_WRITE = 0x04
    IRP_MJ_QUERY_INFORMATION = 0x05
    IRP_MJ_SET_INFORMATION = 0x06
    IRP_MJ_QUERY_EA = 0x07
    IRP_MJ_SET_EA = 0x08
    IRP_MJ_FLUSH_BUFFERS = 0x09
    IRP_MJ_QUERY_VOLUME_INFORMATION = 0x0A
    IRP_MJ_SET_VOLUME_INFORMATION = 0x0B
    IRP_MJ_DIRECTORY_CONTROL = 0x0C
    IRP_MJ_FILE_SYSTEM_CONTROL = 0x0D
    IRP_MJ_DEVICE_CONTROL = 0x0E
    IRP_MJ_INTERNAL_DEVICE_CONTROL = 0x0F
    IRP_MJ_SHUTDOWN = 0x10
    IRP_MJ_LOCK_CONTROL = 0x11
    IRP_MJ_CLEANUP = 0x12
    IRP_MJ_CREATE_MAILSLOT = 0x13
    IRP_MJ_QUERY_SECURITY = 0x14
    IRP_MJ_SET_SECURITY = 0x15
    IRP_MJ_POWER = 0x16
    IRP_MJ_SYSTEM_CONTROL = 0x17
    IRP_MJ_DEVICE_CHANGE = 0x18
    IRP_MJ_QUERY_QUOTA = 0x19
    IRP_MJ_SET_QUOTA = 0x1A
    IRP_MJ_PNP = 0x1B
    IRP_MJ_PNP_POWER = IRP_MJ_PNP
    IRP_MJ_MAXIMUM_FUNCTION = 0x1B

    # Make the Scsi major code the same as internal device control.
    IRP_MJ_SCSI = IRP_MJ_INTERNAL_DEVICE_CONTROL

    # Define the minor function codes for IRPs. The lower 128 codes, from 0x00
    # to
    # 0x7f are reserved to Microsoft. The upper 128 codes, from 0x80 to 0xff,
    # are
    # reserved to customers of Microsoft.
    # Device Control Request minor function codes for SCSI support. Note that
    # user requests are assumed to be zero.
    IRP_MN_SCSI_CLASS = 0x01

    # PNP minor function codes.
    IRP_MN_START_DEVICE = 0x00
    IRP_MN_QUERY_REMOVE_DEVICE = 0x01
    IRP_MN_REMOVE_DEVICE = 0x02
    IRP_MN_CANCEL_REMOVE_DEVICE = 0x03
    IRP_MN_STOP_DEVICE = 0x04
    IRP_MN_QUERY_STOP_DEVICE = 0x05
    IRP_MN_CANCEL_STOP_DEVICE = 0x06
    IRP_MN_QUERY_DEVICE_RELATIONS = 0x07
    IRP_MN_QUERY_INTERFACE = 0x08
    IRP_MN_QUERY_CAPABILITIES = 0x09
    IRP_MN_QUERY_RESOURCES = 0x0A
    IRP_MN_QUERY_RESOURCE_REQUIREMENTS = 0x0B
    IRP_MN_QUERY_DEVICE_TEXT = 0x0C
    IRP_MN_FILTER_RESOURCE_REQUIREMENTS = 0x0D
    IRP_MN_READ_CONFIG = 0x0F
    IRP_MN_WRITE_CONFIG = 0x10
    IRP_MN_EJECT = 0x11
    IRP_MN_SET_LOCK = 0x12
    IRP_MN_QUERY_ID = 0x13
    IRP_MN_QUERY_PNP_DEVICE_STATE = 0x14
    IRP_MN_QUERY_BUS_INFORMATION = 0x15
    IRP_MN_DEVICE_USAGE_NOTIFICATION = 0x16
    IRP_MN_SURPRISE_REMOVAL = 0x17

    if NTDDI_VERSION >= NTDDI_WIN7:
        IRP_MN_DEVICE_ENUMERATED = 0x19
    # END IF
    # POWER minor function codes
    IRP_MN_WAIT_WAKE = 0x00
    IRP_MN_POWER_SEQUENCE = 0x01
    IRP_MN_SET_POWER = 0x02
    IRP_MN_QUERY_POWER = 0x03

    # WMI minor function codes under IRP_MJ_SYSTEM_CONTROL
    IRP_MN_QUERY_ALL_DATA = 0x00
    IRP_MN_QUERY_SINGLE_INSTANCE = 0x01
    IRP_MN_CHANGE_SINGLE_INSTANCE = 0x02
    IRP_MN_CHANGE_SINGLE_ITEM = 0x03
    IRP_MN_ENABLE_EVENTS = 0x04
    IRP_MN_DISABLE_EVENTS = 0x05
    IRP_MN_ENABLE_COLLECTION = 0x06
    IRP_MN_DISABLE_COLLECTION = 0x07
    IRP_MN_REGINFO = 0x08
    IRP_MN_EXECUTE_METHOD = 0x09

    # Minor code 0x0a is reserved
    IRP_MN_REGINFO_EX = 0x0B

    # Minor code 0x0c is reserved
    # Define option flags for IoCreateFile. Note that these values must be
    # exactly the same as the SL_... flags for a create function. Note also
    # that there are flags that may be passed to IoCreateFile that are not
    # placed in the stack location for the create IRP. These flags start in
    # the next byte.
    IO_FORCE_ACCESS_CHECK = 0x0001
    IO_NO_PARAMETER_CHECKING = 0x0100

    # Define Information fields for whether or not a REPARSE or a REMOUNT has
    # occurred in the file system.
    IO_REPARSE = 0x0
    IO_REMOUNT = 0x1
    IO_REPARSE_GLOBAL = 0x2

    # Define the objects that can be created by IoCreateFile.


    class _CREATE_FILE_TYPE(ENUM):
        CreateFileTypeNone = 1
        CreateFileTypeNamedPipe = 2
        CreateFileTypeMailslot = 3


    CREATE_FILE_TYPE = _CREATE_FILE_TYPE

    # Define the named pipe create parameters structure used for internal calls
    # to IoCreateFile when a named pipe is being created. This structure allows
    # code invoking this routine to pass information specific to this function
    # when creating a named pipe.
    class _NAMED_PIPE_CREATE_PARAMETERS(ctypes.Structure):
        pass


    _NAMED_PIPE_CREATE_PARAMETERS._fields_ = [
        ('NamedPipeType', ULONG),
        ('ReadMode', ULONG),
        ('CompletionMode', ULONG),
        ('MaximumInstances', ULONG),
        ('InboundQuota', ULONG),
        ('OutboundQuota', ULONG),
        ('DefaultTimeout', LARGE_INTEGER),
        ('TimeoutSpecified', BOOLEAN),
    ]
    NAMED_PIPE_CREATE_PARAMETERS = _NAMED_PIPE_CREATE_PARAMETERS
    PNAMED_PIPE_CREATE_PARAMETERS = POINTER(_NAMED_PIPE_CREATE_PARAMETERS)

    # Define the mailslot create parameters structure used for internal calls
    # to IoCreateFile when a mailslot is being created. This structure allows
    # code invoking this routine to pass information specific to this function
    # when creating a mailslot.
    class _MAILSLOT_CREATE_PARAMETERS(ctypes.Structure):
        pass


    _MAILSLOT_CREATE_PARAMETERS._fields_ = [
        ('MailslotQuota', ULONG),
        ('MaximumMessageSize', ULONG),
        ('ReadTimeout', LARGE_INTEGER),
        ('TimeoutSpecified', BOOLEAN),
    ]
    MAILSLOT_CREATE_PARAMETERS = _MAILSLOT_CREATE_PARAMETERS
    PMAILSLOT_CREATE_PARAMETERS = POINTER(_MAILSLOT_CREATE_PARAMETERS)

    # Define the structures used by the I/O system
    # Define empty typedefs for the _IRP, _DEVICE_OBJECT, and _DRIVER_OBJECT
    # structures so they may be referenced by function types before they are
    # actually defined.
    _DEVICE_DESCRIPTION = struct

    _DEVICE_OBJECT = struct

    _DMA_ADAPTER = struct

    _DRIVER_OBJECT = struct

    _DRIVE_LAYOUT_INFORMATION = struct

    _DISK_PARTITION = struct

    _FILE_OBJECT = struct

    if defined(_WIN64):
        POINTER_ALIGNMENT = DECLSPEC_ALIGN(8)
    else:
        POINTER_ALIGNMENT = 1
    # END IF
    _IRP = DECLSPEC_ALIGN(MEMORY_ALLOCATION_ALIGNMENT)

    _SCSI_REQUEST_BLOCK = struct

    _SCATTER_GATHER_LIST = struct


    # Define the I/O version of a DPC routine.
    PIO_DPC_ROUTINE = POINTER(IO_DPC_ROUTINE)

    # Define driver timer routine type.
    PIO_TIMER_ROUTINE = POINTER(IO_TIMER_ROUTINE)

    # Define driver initialization routine type.
    PDRIVER_INITIALIZE = POINTER(DRIVER_INITIALIZE)

    # Define driver cancel routine type.
    PDRIVER_CANCEL = POINTER(DRIVER_CANCEL)

    # Define driver dispatch routine type.
    # The default is that it can be called <= DISPATCH
    # because it might be called from another driver.
    # See also below.
    PDRIVER_DISPATCH = POINTER(DRIVER_DISPATCH)

    # Convenience typedef to indicate that the IRQL level
    # of the function has been considered, and that it might
    # be called at DISPATCH_LEVEL.
    DRIVER_DISPATCH_RAISED = DRIVER_DISPATCH

    # Use this variant when there is no possibility of the
    # dispatch function being called at raised IRQL, as in
    # a top - level only driver. This is preferred when it is
    # safe because it enables more paged code.
    # (There may be reasons not to page a dispatch routine
    # that meets that criterion, but it can still use this
    # definition.)
    PDRIVER_DISPATCH_PAGED = POINTER(DRIVER_DISPATCH_PAGED)

    # Define driver start I/O routine type.
    PDRIVER_STARTIO = POINTER(DRIVER_STARTIO)

    # Define driver unload routine type.
    PDRIVER_UNLOAD = POINTER(DRIVER_UNLOAD)

    # Define driver AddDevice routine type.
    PDRIVER_ADD_DEVICE = POINTER(DRIVER_ADD_DEVICE)

    # Define fast I/O procedure prototypes.
    # Fast I/O read and write procedures.
    PFAST_IO_CHECK_IF_POSSIBLE = POINTER(FAST_IO_CHECK_IF_POSSIBLE)
    PFAST_IO_READ = POINTER(FAST_IO_READ)
    PFAST_IO_WRITE = POINTER(FAST_IO_WRITE)

    # Fast I/O query basic and standard information procedures.
    PFAST_IO_QUERY_BASIC_INFO = POINTER(FAST_IO_QUERY_BASIC_INFO)
    PFAST_IO_QUERY_STANDARD_INFO = POINTER(FAST_IO_QUERY_STANDARD_INFO)

    # Fast I/O lock and unlock procedures.
    PFAST_IO_LOCK = POINTER(FAST_IO_LOCK)
    PFAST_IO_UNLOCK_SINGLE = POINTER(FAST_IO_UNLOCK_SINGLE)
    PFAST_IO_UNLOCK_ALL = POINTER(FAST_IO_UNLOCK_ALL)
    PFAST_IO_UNLOCK_ALL_BY_KEY = POINTER(FAST_IO_UNLOCK_ALL_BY_KEY)

    # Fast I/O device control procedure.
    PFAST_IO_DEVICE_CONTROL = POINTER(FAST_IO_DEVICE_CONTROL)

    # Define callbacks for NtCreateSection to synchronize correctly with
    # the file system. It pre - acquires the resources that will be needed
    # when calling to query and set file/allocation size in the file system.
    PFAST_IO_ACQUIRE_FILE = POINTER(FAST_IO_ACQUIRE_FILE)
    PFAST_IO_RELEASE_FILE = POINTER(FAST_IO_RELEASE_FILE)

    # Define callback for drivers that have device objects attached to lower -
    # level drivers' device objects. This callback is made when the lower -
    # level
    # driver is deleting its device object.
    PFAST_IO_DETACH_DEVICE = POINTER(FAST_IO_DETACH_DEVICE)

    # This structure is used by the server to quickly get the information
    # needed
    # to service a server open call. It is takes what would be two fast io
    # calls
    # one for basic information and the other for standard information and
    # makes
    # it into one call.
    PFAST_IO_QUERY_NETWORK_OPEN_INFO = POINTER(FAST_IO_QUERY_NETWORK_OPEN_INFO)

    # Define Mdl - based routines for the server to call
    PFAST_IO_MDL_READ = POINTER(FAST_IO_MDL_READ)
    PFAST_IO_MDL_READ_COMPLETE = POINTER(FAST_IO_MDL_READ_COMPLETE)
    PFAST_IO_PREPARE_MDL_WRITE = POINTER(FAST_IO_PREPARE_MDL_WRITE)
    PFAST_IO_MDL_WRITE_COMPLETE = POINTER(FAST_IO_MDL_WRITE_COMPLETE)

    # If this routine is present, it will be called by FsRtl
    # to acquire the file for the mapped page writer.
    PFAST_IO_ACQUIRE_FOR_MOD_WRITE = POINTER(FAST_IO_ACQUIRE_FOR_MOD_WRITE)
    PFAST_IO_RELEASE_FOR_MOD_WRITE = POINTER(FAST_IO_RELEASE_FOR_MOD_WRITE)

    # If this routine is present, it will be called by FsRtl
    # to acquire the file for the mapped page writer.
    PFAST_IO_ACQUIRE_FOR_CCFLUSH = POINTER(FAST_IO_ACQUIRE_FOR_CCFLUSH)
    PFAST_IO_RELEASE_FOR_CCFLUSH = POINTER(FAST_IO_RELEASE_FOR_CCFLUSH)
    PFAST_IO_READ_COMPRESSED = POINTER(FAST_IO_READ_COMPRESSED)
    PFAST_IO_WRITE_COMPRESSED = POINTER(FAST_IO_WRITE_COMPRESSED)
    PFAST_IO_MDL_READ_COMPLETE_COMPRESSED = POINTER(FAST_IO_MDL_READ_COMPLETE_COMPRESSED)
    PFAST_IO_MDL_WRITE_COMPLETE_COMPRESSED = POINTER(FAST_IO_MDL_WRITE_COMPLETE_COMPRESSED)
    PFAST_IO_QUERY_OPEN = POINTER(FAST_IO_QUERY_OPEN)

    # Define the structure to describe the Fast I/O dispatch routines. Any
    # additions made to this structure MUST be added monotonically to the end
    # of the structure, and fields CANNOT be removed from the middle.
    class _FAST_IO_DISPATCH(ctypes.Structure):
        pass


    _FAST_IO_DISPATCH._fields_ = [
        ('SizeOfFastIoDispatch', ULONG),
        ('FastIoCheckIfPossible', PFAST_IO_CHECK_IF_POSSIBLE),
        ('FastIoRead', PFAST_IO_READ),
        ('FastIoWrite', PFAST_IO_WRITE),
        ('FastIoQueryBasicInfo', PFAST_IO_QUERY_BASIC_INFO),
        ('FastIoQueryStandardInfo', PFAST_IO_QUERY_STANDARD_INFO),
        ('FastIoLock', PFAST_IO_LOCK),
        ('FastIoUnlockSingle', PFAST_IO_UNLOCK_SINGLE),
        ('FastIoUnlockAll', PFAST_IO_UNLOCK_ALL),
        ('FastIoUnlockAllByKey', PFAST_IO_UNLOCK_ALL_BY_KEY),
        ('FastIoDeviceControl', PFAST_IO_DEVICE_CONTROL),
        ('AcquireFileForNtCreateSection', PFAST_IO_ACQUIRE_FILE),
        ('ReleaseFileForNtCreateSection', PFAST_IO_RELEASE_FILE),
        ('FastIoDetachDevice', PFAST_IO_DETACH_DEVICE),
        ('FastIoQueryNetworkOpenInfo', PFAST_IO_QUERY_NETWORK_OPEN_INFO),
        ('AcquireForModWrite', PFAST_IO_ACQUIRE_FOR_MOD_WRITE),
        ('MdlRead', PFAST_IO_MDL_READ),
        ('MdlReadComplete', PFAST_IO_MDL_READ_COMPLETE),
        ('PrepareMdlWrite', PFAST_IO_PREPARE_MDL_WRITE),
        ('MdlWriteComplete', PFAST_IO_MDL_WRITE_COMPLETE),
        ('FastIoReadCompressed', PFAST_IO_READ_COMPRESSED),
        ('FastIoWriteCompressed', PFAST_IO_WRITE_COMPRESSED),
        ('MdlReadCompleteCompressed', PFAST_IO_MDL_READ_COMPLETE_COMPRESSED),
        ('MdlWriteCompleteCompressed', PFAST_IO_MDL_WRITE_COMPLETE_COMPRESSED),
        ('FastIoQueryOpen', PFAST_IO_QUERY_OPEN),
        ('ReleaseForModWrite', PFAST_IO_RELEASE_FOR_MOD_WRITE),
        ('AcquireForCcFlush', PFAST_IO_ACQUIRE_FOR_CCFLUSH),
        ('ReleaseForCcFlush', PFAST_IO_RELEASE_FOR_CCFLUSH),
    ]
    FAST_IO_DISPATCH = _FAST_IO_DISPATCH
    PFAST_IO_DISPATCH = POINTER(_FAST_IO_DISPATCH)

    # Define the actions that a driver execution routine may request of the
    # adapter/controller allocation routines upon return.


    class _IO_ALLOCATION_ACTION(ENUM):
        KeepObject = 1
        DeallocateObject = 2
        DeallocateObjectKeepRegisters = 3


    IO_ALLOCATION_ACTION = _IO_ALLOCATION_ACTION
    PIO_ALLOCATION_ACTION = POINTER(_IO_ALLOCATION_ACTION)

    # Define device driver adapter/controller execution routine.
    PDRIVER_CONTROL = POINTER(DRIVER_CONTROL)

    # Define the I/O system's security context type for use by file system's
    # when checking access to volumes, files, and directories.
    class _IO_SECURITY_CONTEXT(ctypes.Structure):
        pass


    _IO_SECURITY_CONTEXT._fields_ = [
        ('SecurityQos', PSECURITY_QUALITY_OF_SERVICE),
        ('AccessState', PACCESS_STATE),
        ('DesiredAccess', ACCESS_MASK),
        ('FullCreateOptions', ULONG),
    ]
    IO_SECURITY_CONTEXT = _IO_SECURITY_CONTEXT
    PIO_SECURITY_CONTEXT = POINTER(_IO_SECURITY_CONTEXT)

    # Define Volume Parameter Block (VPB) flags.
    VPB_MOUNTED = 0x00000001
    VPB_LOCKED = 0x00000002
    VPB_PERSISTENT = 0x00000004
    VPB_REMOVE_PENDING = 0x00000008
    VPB_RAW_MOUNT = 0x00000010
    VPB_DIRECT_WRITES_ALLOWED = 0x00000020

    # Volume Parameter Block (VPB)
    MAXIMUM_VOLUME_LABEL_LENGTH = 32 * ctypes.sizeof(WCHAR)
    class _VPB(ctypes.Structure):
        pass


    _VPB._fields_ = [
        ('Type', CSHORT),
        ('Size', CSHORT),
        ('Flags', USHORT),
        ('VolumeLabelLength', USHORT), # in bytes
        ('DeviceObject', POINTER(_DEVICE_OBJECT)),
        ('RealDevice', POINTER(_DEVICE_OBJECT)),
        ('SerialNumber', ULONG),
        ('ReferenceCount', ULONG),
        ('VolumeLabel', WCHAR * MAXIMUM_VOLUME_LABEL_LENGTH / ctypes.sizeof(WCHAR)),
    ]
    VPB = _VPB
    PVPB = POINTER(_VPB)

    if defined(_WIN64) or defined(_ARM_):

        # Use __inline DMA macros (hal.h)
        if not defined(USE_DMA_MACROS):
            USE_DMA_MACROS = 1
        # END IF
        # Only PnP driversnot

        if not defined(NO_LEGACY_DRIVERS):
            NO_LEGACY_DRIVERS = 1
        # END IF    # END IF   _WIN64

    if defined(USE_DMA_MACROS) and not defined(_NTHAL_) and ( defined(_NTDDK_) or defined(_NTDRIVER_) or defined(_NTOSP_)):

        # Define object type specific fields of various objects used by the
        # I/O system
        PADAPTER_OBJECT = POINTER(_DMA_ADAPTER)

    elif defined(_WDM_INCLUDED_):
        PADAPTER_OBJECT = POINTER(_DMA_ADAPTER)

    else:

        # Define object type specific fields of various objects used by the
        # I/O system
         = *PADAPTER_OBJECT;

    # END IF   USE_DMA_MACROS and (_NTDDK_ or _NTDRIVER_ or _NTOSP_)
    # Define Wait Context Block (WCB)
    class _WAIT_CONTEXT_BLOCK(ctypes.Structure):
        pass


    class _Struct_12(ctypes.Structure):
        pass


    class _Struct_13(ctypes.Structure):
        pass


    _Struct_13._fields_ = [
        ('DmaWaitEntry', LIST_ENTRY),
        ('NumberOfChannels', ULONG),
        ('SyncCallback', ULONG, 1),
        ('DmaContext', ULONG, 1),
        ('ZeroMapRegisters', ULONG, 1),
        ('Reserved', ULONG, 29),
    ]
    _Struct_12._Struct_13 = _Struct_13
    _Struct_12._anonymous_ = (
        '_Struct_13',
    )
    _Struct_12._fields_ = [
        ('WaitQueueEntry', KDEVICE_QUEUE_ENTRY),
        ('_Struct_13', _Struct_12._Struct_13),
    ]
    _WAIT_CONTEXT_BLOCK._Struct_12 = _Struct_12
    _WAIT_CONTEXT_BLOCK._anonymous_ = (
        '_Struct_12',
    )
    _WAIT_CONTEXT_BLOCK._fields_ = [
        ('_Struct_12', _WAIT_CONTEXT_BLOCK._Struct_12),
        ('DeviceRoutine', PDRIVER_CONTROL),
        ('DeviceContext', PVOID),
        ('NumberOfMapRegisters', ULONG),
        ('DeviceObject', PVOID),
        ('CurrentIrp', PVOID),
        ('BufferChainingDpc', PKDPC),
    ]
    WAIT_CONTEXT_BLOCK = _WAIT_CONTEXT_BLOCK
    PWAIT_CONTEXT_BLOCK = POINTER(_WAIT_CONTEXT_BLOCK)

    # Define Device Object (DO) flags
    # DO_DAX_VOLUME - If set, this is a DAX volume i.e. the volume supports
    # mapping a file directly
    # on the persistent memory device. The cached and memory mapped IO to user
    # files wouldn't
    # generate paging IO.
    DO_VERIFY_VOLUME = 0x00000002
    DO_BUFFERED_IO = 0x00000004
    DO_EXCLUSIVE = 0x00000008
    DO_DIRECT_IO = 0x00000010
    DO_MAP_IO_BUFFER = 0x00000020
    DO_DEVICE_INITIALIZING = 0x00000080
    DO_SHUTDOWN_REGISTERED = 0x00000800
    DO_BUS_ENUMERATED_DEVICE = 0x00001000
    DO_POWER_PAGABLE = 0x00002000
    DO_POWER_INRUSH = 0x00004000
    DO_DEVICE_TO_BE_RESET = 0x04000000
    DO_DAX_VOLUME = 0x10000000

    # Device Object structure definition

    if _MSC_VER >= 1200:
        pass
    # END IF
    class _DEVICE_OBJECT(ctypes.Structure):
        pass


    class Queue(ctypes.Union):
        pass


    Queue._fields_ = [
        ('ListEntry', LIST_ENTRY),
        ('Wcb', WAIT_CONTEXT_BLOCK),
    ]
    _DEVICE_OBJECT.Queue = Queue
    _DEVICE_OBJECT._fields_ = [
        ('Type', CSHORT),
        ('Size', USHORT),
        ('ReferenceCount', LONG),
        ('DriverObject', POINTER(_DRIVER_OBJECT)),
        ('NextDevice', POINTER(_DEVICE_OBJECT)),
        ('AttachedDevice', POINTER(_DEVICE_OBJECT)),
        ('CurrentIrp', POINTER(_IRP)),
        ('Timer', PIO_TIMER),
        ('Flags', ULONG), # See above: DO_...
        ('Characteristics', ULONG), # See ntioapi: FILE_...
        ('PVPB Vpb', __volatile),
        ('DeviceExtension', PVOID),
        ('DeviceType', DEVICE_TYPE),
        ('StackSize', CCHAR),
        ('Queue', _DEVICE_OBJECT.Queue),
        ('AlignmentRequirement', ULONG),
        ('DeviceQueue', KDEVICE_QUEUE),
        ('Dpc', KDPC),
        ('ActiveThreadCount', ULONG), # track of the number of Fsp threads currently using the device
        ('SecurityDescriptor', PSECURITY_DESCRIPTOR),
        ('DeviceLock', KEVENT),
        ('SectorSize', USHORT),
        ('Spare1', USHORT),
        ('DeviceObjectExtension', POINTER(_DEVOBJ_EXTENSION)),
        ('Reserved', PVOID),
    ]
    DEVICE_OBJECT = _DEVICE_OBJECT
     = *PDEVICE_OBJECT;

    if _MSC_VER >= 1200:
        pass
    # END IF
    _DEVICE_OBJECT_POWER_EXTENSION =

    class _DEVOBJ_EXTENSION(ctypes.Structure):
        pass


    _DEVOBJ_EXTENSION._fields_ = [
        ('Type', CSHORT),
        ('Size', USHORT),
        ('DeviceObject', PDEVICE_OBJECT), # owning device object
        ('PowerFlags', ULONG), # The remaining fields are reserved for system use.
        ('Dope', POINTER(_DEVICE_OBJECT_POWER_EXTENSION)),
        ('ExtensionFlags', ULONG),
        ('DeviceNode', PVOID),
        ('AttachedTo', PDEVICE_OBJECT),
        ('LONG StartIoCount', __volatile),
        ('StartIoKey', LONG),
        ('StartIoFlags', ULONG),
        ('Vpb', PVPB),
        ('DependencyNode', PVOID),
        ('InterruptContext', PVOID),
        ('PVOID VerifierContext', __volatile),
    ]
    DEVOBJ_EXTENSION = _DEVOBJ_EXTENSION
    PDEVOBJ_EXTENSION = POINTER(_DEVOBJ_EXTENSION)

    # Define Driver Object (DRVO) flags
    DRVO_UNLOAD_INVOKED = 0x00000001
    DRVO_LEGACY_DRIVER = 0x00000002
    DRVO_BUILTIN_DRIVER = 0x00000004
    class _DRIVER_EXTENSION(ctypes.Structure):
        pass


    _DRIVER_EXTENSION._fields_ = [
        ('DriverObject', POINTER(_DRIVER_OBJECT)), # Back pointer to Driver Object
        ('AddDevice', PDRIVER_ADD_DEVICE), # driver must control.
        ('Count', ULONG), # had its registered reinitialization routine invoked.
        ('ServiceKeyName', UNICODE_STRING), # where the driver related info is stored in the registry.
    ]
    DRIVER_EXTENSION = _DRIVER_EXTENSION
    PDRIVER_EXTENSION = POINTER(_DRIVER_EXTENSION)
    class _DRIVER_OBJECT(ctypes.Structure):
        pass


    _DRIVER_OBJECT._fields_ = [
        ('Type', CSHORT),
        ('Size', CSHORT),
        ('DeviceObject', PDEVICE_OBJECT), # location for driver objects.
        ('Flags', ULONG),
        ('DriverStart', PVOID), # registered reinitialization routine invoked.
        ('DriverSize', ULONG),
        ('DriverSection', PVOID),
        ('DriverExtension', PDRIVER_EXTENSION),
        ('DriverName', UNICODE_STRING), # determine the name of the driver that an I/O request is/was bound.
        ('HardwareDatabase', PUNICODE_STRING), # to the path to the hardware information in the registry
        ('FastIoDispatch', PFAST_IO_DISPATCH), # the file is cached.
        ('DriverInit', PDRIVER_INITIALIZE), # field in the object so that it remains extensible.
        ('DriverStartIo', PDRIVER_STARTIO),
        ('DriverUnload', PDRIVER_UNLOAD),
        ('MajorFunction', PDRIVER_DISPATCH * IRP_MJ_MAXIMUM_FUNCTION + 1),
    ]
    DRIVER_OBJECT = _DRIVER_OBJECT
     = *PDRIVER_OBJECT;


    # The following structure is pointed to by the SectionObject pointer field
    # of a file object, and is allocated by the various NT file systems.
    class _SECTION_OBJECT_POINTERS(ctypes.Structure):
        pass


    _SECTION_OBJECT_POINTERS._fields_ = [
        ('DataSectionObject', PVOID),
        ('SharedCacheMap', PVOID),
        ('ImageSectionObject', PVOID),
    ]
    SECTION_OBJECT_POINTERS = _SECTION_OBJECT_POINTERS
    PSECTION_OBJECT_POINTERS = POINTER(SECTION_OBJECT_POINTERS)

    # Define the format of a completion message.
    class _IO_COMPLETION_CONTEXT(ctypes.Structure):
        pass


    _IO_COMPLETION_CONTEXT._fields_ = [
        ('Port', PVOID),
        ('Key', PVOID),
    ]
    IO_COMPLETION_CONTEXT = _IO_COMPLETION_CONTEXT
    PIO_COMPLETION_CONTEXT = POINTER(_IO_COMPLETION_CONTEXT)

    # Define File Object (FO) flags
    FO_FILE_OPEN = 0x00000001
    FO_SYNCHRONOUS_IO = 0x00000002
    FO_ALERTABLE_IO = 0x00000004
    FO_NO_INTERMEDIATE_BUFFERING = 0x00000008
    FO_WRITE_THROUGH = 0x00000010
    FO_SEQUENTIAL_ONLY = 0x00000020
    FO_CACHE_SUPPORTED = 0x00000040
    FO_NAMED_PIPE = 0x00000080
    FO_STREAM_FILE = 0x00000100
    FO_MAILSLOT = 0x00000200
    FO_GENERATE_AUDIT_ON_CLOSE = 0x00000400
    FO_QUEUE_IRP_TO_THREAD = FO_GENERATE_AUDIT_ON_CLOSE
    FO_DIRECT_DEVICE_OPEN = 0x00000800
    FO_FILE_MODIFIED = 0x00001000
    FO_FILE_SIZE_CHANGED = 0x00002000
    FO_CLEANUP_COMPLETE = 0x00004000
    FO_TEMPORARY_FILE = 0x00008000
    FO_DELETE_ON_CLOSE = 0x00010000
    FO_OPENED_CASE_SENSITIVE = 0x00020000
    FO_HANDLE_CREATED = 0x00040000
    FO_FILE_FAST_IO_READ = 0x00080000
    FO_RANDOM_ACCESS = 0x00100000
    FO_FILE_OPEN_CANCELLED = 0x00200000
    FO_VOLUME_OPEN = 0x00400000
    FO_REMOTE_ORIGIN = 0x01000000
    FO_DISALLOW_EXCLUSIVE = 0x02000000
    FO_SKIP_COMPLETION_PORT = FO_DISALLOW_EXCLUSIVE
    FO_SKIP_SET_EVENT = 0x04000000
    FO_SKIP_SET_FAST_IO = 0x08000000
    FO_INDIRECT_WAIT_OBJECT = 0x10000000
    FO_SECTION_MINSTORE_TREATMENT = 0x20000000

    # This mask allows us to re - use flags that are not present during a
    # create
    # operation for uses that are only valid for the duration of the create.
    FO_FLAGS_VALID_ONLY_DURING_CREATE = FO_DISALLOW_EXCLUSIVE
    class _FILE_OBJECT(ctypes.Structure):
        pass


    _FILE_OBJECT._fields_ = [
        ('Type', CSHORT),
        ('Size', CSHORT),
        ('DeviceObject', PDEVICE_OBJECT),
        ('Vpb', PVPB),
        ('FsContext', PVOID),
        ('FsContext2', PVOID),
        ('SectionObjectPointer', PSECTION_OBJECT_POINTERS),
        ('PrivateCacheMap', PVOID),
        ('FinalStatus', NTSTATUS),
        ('RelatedFileObject', POINTER(_FILE_OBJECT)),
        ('LockOperation', BOOLEAN),
        ('DeletePending', BOOLEAN),
        ('ReadAccess', BOOLEAN),
        ('WriteAccess', BOOLEAN),
        ('DeleteAccess', BOOLEAN),
        ('SharedRead', BOOLEAN),
        ('SharedWrite', BOOLEAN),
        ('SharedDelete', BOOLEAN),
        ('Flags', ULONG),
        ('FileName', UNICODE_STRING),
        ('CurrentByteOffset', LARGE_INTEGER),
        ('ULONG Waiters', __volatile),
        ('ULONG Busy', __volatile),
        ('LastLock', PVOID),
        ('Lock', KEVENT),
        ('Event', KEVENT),
        ('PIO_COMPLETION_CONTEXT CompletionContext', __volatile),
        ('IrpListLock', KSPIN_LOCK),
        ('IrpList', LIST_ENTRY),
        ('PVOID FileObjectExtension', __volatile),
    ]
    FILE_OBJECT = _FILE_OBJECT
     = *PFILE_OBJECT;


    # Define I/O Request Packet (IRP) flags
    IRP_NOCACHE = 0x00000001
    IRP_PAGING_IO = 0x00000002
    IRP_MOUNT_COMPLETION = 0x00000002
    IRP_SYNCHRONOUS_API = 0x00000004
    IRP_ASSOCIATED_IRP = 0x00000008
    IRP_BUFFERED_IO = 0x00000010
    IRP_DEALLOCATE_BUFFER = 0x00000020
    IRP_INPUT_OPERATION = 0x00000040
    IRP_SYNCHRONOUS_PAGING_IO = 0x00000040
    IRP_CREATE_OPERATION = 0x00000080
    IRP_READ_OPERATION = 0x00000100
    IRP_WRITE_OPERATION = 0x00000200
    IRP_CLOSE_OPERATION = 0x00000400
    IRP_DEFER_IO_COMPLETION = 0x00000800
    IRP_OB_QUERY_NAME = 0x00001000
    IRP_HOLD_DEVICE_QUEUE = 0x00002000
    IRP_UM_DRIVER_INITIATED_IO = 0x00400000

    # Define I/O request packet (IRP) alternate flags for allocation control.
    IRP_QUOTA_CHARGED = 0x01
    IRP_ALLOCATED_MUST_SUCCEED = 0x02
    IRP_ALLOCATED_FIXED_SIZE = 0x04
    IRP_LOOKASIDE_ALLOCATION = 0x08

    # I/O Request Packet (IRP) definition
    class _IRP(ctypes.Structure):
        pass


    class AssociatedIrp(ctypes.Union):
        pass


    AssociatedIrp._fields_ = [
        ('MasterIrp', POINTER(_IRP)),
        ('LONG IrpCount', __volatile),
        ('SystemBuffer', PVOID),
    ]
    _IRP.AssociatedIrp = AssociatedIrp
    class Overlay(ctypes.Union):
        pass


    class AsynchronousParameters(ctypes.Union):
        pass


    class _Union_4(ctypes.Union):
        pass


    _Union_4._fields_ = [
        ('UserApcRoutine', PIO_APC_ROUTINE),
        ('IssuingProcess', PVOID),
    ]
    AsynchronousParameters._Union_4 = _Union_4
    AsynchronousParameters._anonymous_ = (
        '_Union_4',
    )
    AsynchronousParameters._fields_ = [
        ('_Union_4', AsynchronousParameters._Union_4),
        ('UserApcContext', PVOID),
    ]
    Overlay.AsynchronousParameters = AsynchronousParameters
    Overlay._fields_ = [
        ('AsynchronousParameters', Overlay.AsynchronousParameters),
        ('AllocationSize', LARGE_INTEGER),
    ]
    _IRP.Overlay = Overlay
    class Tail(ctypes.Union):
        pass


    class Overlay(ctypes.Union):
        pass


    class _Struct_13(ctypes.Structure):
        pass


    class _Struct_14(ctypes.Structure):
        pass


    _Struct_14._fields_ = [
        ('DriverContext', PVOID * 4), # packet.
    ]
    _Struct_13._Struct_14 = _Struct_14
    _Struct_13._anonymous_ = (
        '_Struct_14',
    )
    _Struct_13._fields_ = [
        ('DeviceQueueEntry', KDEVICE_QUEUE_ENTRY), # queue the IRP to the device driver device queue.
        ('_Struct_14', _Struct_13._Struct_14),
    ]
    Overlay._Struct_13 = _Struct_13
    class _Union_4(ctypes.Union):
        pass


    class _Union_5(ctypes.Union):
        pass


    _Union_5._fields_ = [
        ('CurrentStackLocation', POINTER(_IO_STACK_LOCATION)), # use the standard functions.
        ('PacketType', ULONG), # Minipacket type.
    ]
    _Union_4._Union_5 = _Union_5
    _Union_4._anonymous_ = (
        '_Union_5',
    )
    _Union_4._fields_ = [
        ('ListEntry', LIST_ENTRY), # others.
        ('_Union_5', _Union_4._Union_5),
    ]
    Overlay._Union_4 = _Union_4
    Overlay._anonymous_ = (
        '_Struct_13',
        '_Union_4',
    )
    Overlay._fields_ = [
        ('_Struct_13', Overlay._Struct_13),
        ('Thread', PETHREAD), # Thread - pointer to caller's Thread Control Block.
        ('AuxiliaryBuffer', PCHAR), # in a normal buffer.
        ('_Union_4', Overlay._Union_4), # for completion queue entries.
        ('OriginalFileObject', PFILE_OBJECT), # I/O system and should not be used by any other drivers.
    ]
    Tail.Overlay = Overlay
    Tail._fields_ = [
        ('Overlay', Tail.Overlay),
        ('Apc', KAPC), # invoked before the APC gets control simply deallocates the IRP.
        ('CompletionKey', PVOID), # individual I/O operations initiated on a single file handle.
    ]
    _IRP.Tail = Tail
    _IRP._fields_ = [
        ('Type', CSHORT),
        ('Size', USHORT),
        ('MdlAddress', PMDL), # request. This field is only used if the I/O is "direct I/O".
        ('Flags', ULONG), # Flags word - used to remember various flags.
        ('AssociatedIrp', _IRP.AssociatedIrp), # the system space buffer.
        ('ThreadListEntry', LIST_ENTRY), # request packet list.
        ('IoStatus', IO_STATUS_BLOCK), # I/O status - final status of operation.
        ('RequestorMode', KPROCESSOR_MODE), # Requester mode - mode of the original requester of this operation.
        ('PendingReturned', BOOLEAN), # status for this packet.
        ('StackCount', CHAR), # Stack state information.
        ('CurrentLocation', CHAR),
        ('Cancel', BOOLEAN), # Cancel - packet has been canceled.
        ('CancelIrql', KIRQL), # Cancel Irql - Irql at which the cancel spinlock was acquired.
        ('ApcEnvironment', CCHAR), # packet was initialized.
        ('AllocationFlags', UCHAR), # Allocation control flags.
        ('UserIosb', PIO_STATUS_BLOCK), # User parameters.
        ('UserEvent', PKEVENT),
        ('Overlay', _IRP.Overlay),
        ('PDRIVER_CANCEL CancelRoutine', __volatile), # by a device driver when the IRP is in a cancelable state.
        ('UserBuffer', PVOID), # the UserBuffer field is NULL, then no copy is performed.
        ('Tail', _IRP.Tail), # alignment of other fields in the IRP.
    ]
    IRP = _IRP
    PIRP = POINTER(IRP)

    # Define completion routine types for use in stack locations in an IRP
    PIO_COMPLETION_ROUTINE = POINTER(IO_COMPLETION_ROUTINE)

    # Define stack location control flags
    SL_PENDING_RETURNED = 0x01
    SL_ERROR_RETURNED = 0x02
    SL_INVOKE_ON_CANCEL = 0x20
    SL_INVOKE_ON_SUCCESS = 0x40
    SL_INVOKE_ON_ERROR = 0x80

    # Define flags for various functions
    # Create / Create Named Pipe (IRP_MJ_CREATE/IRP_MJ_CREATE_NAMED_PIPE)
    # The following flags must exactly match those in the IoCreateFile call's
    # options. The case sensitive flag is added in later, by the parse routine,
    # and is not an actual option to open. Rather, it is part of the object
    # manager's attributes structure.
    SL_FORCE_ACCESS_CHECK = 0x01
    SL_OPEN_PAGING_FILE = 0x02
    SL_OPEN_TARGET_DIRECTORY = 0x04
    SL_STOP_ON_SYMLINK = 0x08
    SL_IGNORE_READONLY_ATTRIBUTE = 0x40
    SL_CASE_SENSITIVE = 0x80

    # Read / Write (IRP_MJ_READ/IRP_MJ_WRITE)
    SL_KEY_SPECIFIED = 0x01
    SL_OVERRIDE_VERIFY_VOLUME = 0x02
    SL_WRITE_THROUGH = 0x04
    SL_FT_SEQUENTIAL_WRITE = 0x08
    SL_FORCE_DIRECT_WRITE = 0x10
    SL_REALTIME_STREAM = 0x20
    SL_PERSISTENT_MEMORY_FIXED_MAPPING = 0x20

    # SL_KEY_SPECIFIED - when set this flag indicates that the
    # IO_STACK_LOCATION.Parameters.Read(OrWrite).Key
    # contains which copy of a given sector should be read when redundancy is
    # enabled. Today this flag is
    # only used with IRP_MJ_READ operations but could be expanded to
    # IRP_MJ_WRITE in the future.
    # SL_REALTIME_STREAM - flag hints that the IO is for real - time streaming
    # requests to CD - ROM class driver.
    # This hints the driver to perform READ / WRITE operations at a guaranteed
    # speed for real - time streaming.
    # SL_PERSISTENT_MEMORY_FIXED_MAPPING - The persistent memory mapping of
    # the bytes in the write request
    # cannot change while handling this write request.
    # One of the reasons for remapping
    # (modifying the physical address of a given LBA) on persistent memory
    # devices is to provide efficient sector level atomicity.
    # If the flag is not set, remapping is allowed especially if it results in
    # the driver providing sector
    # atomicity. File systems (or the requester) prefer that a persistent
    # memory device driver provides
    # sector atomicity.
    # If the flag is set, a persistent memory driver shall not remap the
    # physical addresses corresponding
    # to the LBAs. If that means sector atomicity can't be provided, so be it.
    # However, the driver is more
    # than welcome to provide sector atomicity as LONG as there is no
    # remapping.
    # IRP_MJ_FLUSH_BUFFERS
    SL_FORCE_ASYNCHRONOUS = 0x01

    # SL_FORCE_ASYNCHRONOUS - a flush IRP specific flag in IrpStack to specify
    # that the flush operation needs
    # to be async. This behavior is needed by Spaces as Spaces issues flushes
    # to disks in a pool serially and
    # does not want to be blocked by disks whose flush operation is slow.
    # Device I/O Control
    # Same SL_OVERRIDE_VERIFY_VOLUME as for read/write above.
    SL_READ_ACCESS_GRANTED = 0x01
    SL_WRITE_ACCESS_GRANTED = 0x04

    # Lock (IRP_MJ_LOCK_CONTROL)
    SL_FAIL_IMMEDIATELY = 0x01
    SL_EXCLUSIVE_LOCK = 0x02

    # QueryDirectory / QueryEa / QueryQuota
    # (IRP_MJ_DIRECTORY_CONTROL/IRP_MJ_QUERY_EA/IRP_MJ_QUERY_QUOTA))
    SL_RESTART_SCAN = 0x01
    SL_RETURN_SINGLE_ENTRY = 0x02
    SL_INDEX_SPECIFIED = 0x04
    SL_RETURN_ON_DISK_ENTRIES_ONLY = 0x08
    SL_QUERY_DIRECTORY_MASK = 0x0B

    # SL_RETURN_ON_DISK_ENTRIES_ONLY - Instructs any filters that perform
    # directory virtualization or just - in - time expansion to simply pass the
    # request through to the file system and return entries that are currently
    # on disk.
    # SL_QUERY_DIRECTORY_MASK - The set of SL_ flags that are valid for
    # IRP_MJ_DIRECTORY_CONTROL.
    # NotifyDirectory (IRP_MJ_DIRECTORY_CONTROL)
    SL_WATCH_TREE = 0x01

    # FileSystemControl (IRP_MJ_FILE_SYSTEM_CONTROL)
    # minor: mount/verify volume
    SL_ALLOW_RAW_MOUNT = 0x01

    # SetInformationFile (IRP_MJ_SET_INFORMATION)
    # Rename/Link Information
    SL_BYPASS_ACCESS_CHECK = 0x01

    # Define PNP/POWER types required by IRP_MJ_PNP/IRP_MJ_POWER.


    class _DEVICE_RELATION_TYPE(ENUM):
        BusRelations = 1
        EjectionRelations = 2
        PowerRelations = 3
        RemovalRelations = 4
        TargetDeviceRelation = 5
        SingleBusRelations = 6
        TransportRelations = 7


    DEVICE_RELATION_TYPE = _DEVICE_RELATION_TYPE
    PDEVICE_RELATION_TYPE = POINTER(_DEVICE_RELATION_TYPE)
    class _DEVICE_RELATIONS(ctypes.Structure):
        pass


    _DEVICE_RELATIONS._fields_ = [
        ('Count', ULONG),
        ('Objects', PDEVICE_OBJECT * 1), # variable length
    ]
    DEVICE_RELATIONS = _DEVICE_RELATIONS
    PDEVICE_RELATIONS = POINTER(_DEVICE_RELATIONS)

    # IRP_MN_DEVICE_USAGE_NOTIFICATION types
    # DeviceUsageTypePostDisplay - The POST display adapter must be sent this
    # IRP
    # before IRP_MN_START_DEVICE, and with Parameters.UsageNotification.InPath
    # set to TRUE. After that, the adapter cannot be sent an
    # IRP_MN_DEVICE_USAGE_NOTIFICATION with InPath set to FALSE.
    class _DEVICE_USAGE_NOTIFICATION_TYPE(ENUM):
        DeviceUsageTypeUndefined = 1
        DeviceUsageTypePaging = 2
        DeviceUsageTypeHibernation = 3
        DeviceUsageTypeDumpFile = 4
        DeviceUsageTypeBoot = 5
        DeviceUsageTypePostDisplay = 6


    DEVICE_USAGE_NOTIFICATION_TYPE = _DEVICE_USAGE_NOTIFICATION_TYPE

    # workaround overloaded definition
    # (rpc generated headers all define INTERFACE
    # to match the class name).
    class _INTERFACE(ctypes.Structure):
        pass


    _INTERFACE._fields_ = [
        ('Size', USHORT),
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
    ]
    INTERFACE = _INTERFACE
    PINTERFACE = POINTER(_INTERFACE)
    class _POWER_SEQUENCE(ctypes.Structure):
        pass


    _POWER_SEQUENCE._fields_ = [
        ('SequenceD1', ULONG),
        ('SequenceD2', ULONG),
        ('SequenceD3', ULONG),
    ]
    POWER_SEQUENCE = _POWER_SEQUENCE
    PPOWER_SEQUENCE = POINTER(_POWER_SEQUENCE)
    class BUS_QUERY_ID_TYPE(ENUM):
        BusQueryDeviceID = 0
        BusQueryHardwareIDs = 1
        BusQueryCompatibleIDs = 2
        BusQueryInstanceID = 3
        BusQueryDeviceSerialNumber = 4
        BusQueryContainerID = 5


    PBUS_QUERY_ID_TYPE = POINTER(BUS_QUERY_ID_TYPE)
    BusQueryDeviceID = BUS_QUERY_ID_TYPE.BusQueryDeviceID
    BusQueryHardwareIDs = BUS_QUERY_ID_TYPE.BusQueryHardwareIDs
    BusQueryCompatibleIDs = BUS_QUERY_ID_TYPE.BusQueryCompatibleIDs
    BusQueryInstanceID = BUS_QUERY_ID_TYPE.BusQueryInstanceID
    BusQueryDeviceSerialNumber = BUS_QUERY_ID_TYPE.BusQueryDeviceSerialNumber
    BusQueryContainerID = BUS_QUERY_ID_TYPE.BusQueryContainerID
    PNP_DEVICE_STATE = ULONG
    PPNP_DEVICE_STATE = POINTER(ULONG)
    PNP_DEVICE_DISABLED = 0x00000001
    PNP_DEVICE_DONT_DISPLAY_IN_UI = 0x00000002
    PNP_DEVICE_FAILED = 0x00000004
    PNP_DEVICE_REMOVED = 0x00000008
    PNP_DEVICE_RESOURCE_REQUIREMENTS_CHANGED = 0x00000010
    PNP_DEVICE_NOT_DISABLEABLE = 0x00000020
    PNP_DEVICE_DISCONNECTED = 0x00000040


    class DEVICE_TEXT_TYPE(ENUM):
        DeviceTextDescription = 0
        DeviceTextLocationInformation = 1


    PDEVICE_TEXT_TYPE = POINTER(DEVICE_TEXT_TYPE)
    DeviceTextDescription = DEVICE_TEXT_TYPE.DeviceTextDescription
    DeviceTextLocationInformation = DEVICE_TEXT_TYPE.DeviceTextLocationInformation

    # Define I/O Request Packet (IRP) stack locations
    if not defined(_AMD64_) and not defined(_ARM_) and not defined(_ARM64_):
        pass
    # END IF
    if defined(_WIN64):
        POINTER_ALIGNMENT = DECLSPEC_ALIGN(8)
    else:
        POINTER_ALIGNMENT = 1
    # END IF

    if _MSC_VER >= 1200:
        pass
    # END IF
    class _IO_STACK_LOCATION(ctypes.Structure):
        pass


    class Parameters(ctypes.Structure):
        pass


    class Create(ctypes.Structure):
        pass


    Create._fields_ = [
        ('SecurityContext', PIO_SECURITY_CONTEXT),
        ('Options', ULONG),
        ('POINTER_ALIGNMENT FileAttributes', USHORT),
        ('ShareAccess', USHORT),
        ('POINTER_ALIGNMENT EaLength', ULONG),
    ]
    Parameters.Create = Create
    class CreatePipe(ctypes.Structure):
        pass


    CreatePipe._fields_ = [
        ('SecurityContext', PIO_SECURITY_CONTEXT),
        ('Options', ULONG),
        ('POINTER_ALIGNMENT Reserved', USHORT),
        ('ShareAccess', USHORT),
        ('Parameters', PNAMED_PIPE_CREATE_PARAMETERS),
    ]
    Parameters.CreatePipe = CreatePipe
    class CreateMailslot(ctypes.Structure):
        pass


    CreateMailslot._fields_ = [
        ('SecurityContext', PIO_SECURITY_CONTEXT),
        ('Options', ULONG),
        ('POINTER_ALIGNMENT Reserved', USHORT),
        ('ShareAccess', USHORT),
        ('Parameters', PMAILSLOT_CREATE_PARAMETERS),
    ]
    Parameters.CreateMailslot = CreateMailslot
    class Read(ctypes.Structure):
        pass


    Read._fields_ = [
        ('Length', ULONG),
        ('POINTER_ALIGNMENT Key', ULONG),
        ('ByteOffset', LARGE_INTEGER),
    ]
    Parameters.Read = Read
    class Write(ctypes.Structure):
        pass


    Write._fields_ = [
        ('Length', ULONG),
        ('POINTER_ALIGNMENT Key', ULONG),
        ('ByteOffset', LARGE_INTEGER),
    ]
    Parameters.Write = Write
    class QueryDirectory(ctypes.Structure):
        pass


    QueryDirectory._fields_ = [
        ('Length', ULONG),
        ('FileName', PUNICODE_STRING),
        ('FileInformationClass', FILE_INFORMATION_CLASS),
        ('POINTER_ALIGNMENT FileIndex', ULONG),
    ]
    Parameters.QueryDirectory = QueryDirectory
    class NotifyDirectory(ctypes.Structure):
        pass


    NotifyDirectory._fields_ = [
        ('Length', ULONG),
        ('POINTER_ALIGNMENT CompletionFilter', ULONG),
    ]
    Parameters.NotifyDirectory = NotifyDirectory
    class NotifyDirectoryEx(ctypes.Structure):
        pass


    NotifyDirectoryEx._fields_ = [
        ('Length', ULONG),
        ('POINTER_ALIGNMENT CompletionFilter', ULONG),
        ('POINTER_ALIGNMENT DirectoryNotifyInformationClass', DIRECTORY_NOTIFY_INFORMATION_CLASS),
    ]
    Parameters.NotifyDirectoryEx = NotifyDirectoryEx
    class QueryFile(ctypes.Structure):
        pass


    QueryFile._fields_ = [
        ('Length', ULONG),
        ('POINTER_ALIGNMENT FileInformationClass', FILE_INFORMATION_CLASS),
    ]
    Parameters.QueryFile = QueryFile
    class SetFile(ctypes.Structure):
        pass


    class _Struct_13(ctypes.Structure):
        pass


    class _Struct_14(ctypes.Structure):
        pass


    _Struct_14._fields_ = [
        ('ReplaceIfExists', BOOLEAN),
        ('AdvanceOnly', BOOLEAN),
    ]
    _Struct_13._Struct_14 = _Struct_14
    _Struct_13._anonymous_ = (
        '_Struct_14',
    )
    _Struct_13._fields_ = [
        ('_Struct_14', _Struct_13._Struct_14),
        ('ClusterCount', ULONG),
        ('DeleteHandle', HANDLE),
    ]
    SetFile._Struct_13 = _Struct_13
    SetFile._anonymous_ = (
        '_Struct_13',
    )
    SetFile._fields_ = [
        ('Length', ULONG),
        ('POINTER_ALIGNMENT FileInformationClass', FILE_INFORMATION_CLASS),
        ('FileObject', PFILE_OBJECT),
        ('_Struct_13', SetFile._Struct_13),
    ]
    Parameters.SetFile = SetFile
    class QueryEa(ctypes.Structure):
        pass


    QueryEa._fields_ = [
        ('Length', ULONG),
        ('EaList', PVOID),
        ('EaListLength', ULONG),
        ('POINTER_ALIGNMENT EaIndex', ULONG),
    ]
    Parameters.QueryEa = QueryEa
    class SetEa(ctypes.Structure):
        pass


    SetEa._fields_ = [
        ('Length', ULONG),
    ]
    Parameters.SetEa = SetEa
    class QueryVolume(ctypes.Structure):
        pass


    QueryVolume._fields_ = [
        ('Length', ULONG),
        ('POINTER_ALIGNMENT FsInformationClass', FS_INFORMATION_CLASS),
    ]
    Parameters.QueryVolume = QueryVolume
    class SetVolume(ctypes.Structure):
        pass


    SetVolume._fields_ = [
        ('Length', ULONG),
        ('POINTER_ALIGNMENT FsInformationClass', FS_INFORMATION_CLASS),
    ]
    Parameters.SetVolume = SetVolume
    class FileSystemControl(ctypes.Structure):
        pass


    FileSystemControl._fields_ = [
        ('OutputBufferLength', ULONG),
        ('POINTER_ALIGNMENT InputBufferLength', ULONG),
        ('POINTER_ALIGNMENT FsControlCode', ULONG),
        ('Type3InputBuffer', PVOID),
    ]
    Parameters.FileSystemControl = FileSystemControl
    class LockControl(ctypes.Structure):
        pass


    LockControl._fields_ = [
        ('Length', PLARGE_INTEGER),
        ('POINTER_ALIGNMENT Key', ULONG),
        ('ByteOffset', LARGE_INTEGER),
    ]
    Parameters.LockControl = LockControl
    class DeviceIoControl(ctypes.Structure):
        pass


    DeviceIoControl._fields_ = [
        ('OutputBufferLength', ULONG),
        ('POINTER_ALIGNMENT InputBufferLength', ULONG),
        ('POINTER_ALIGNMENT IoControlCode', ULONG),
        ('Type3InputBuffer', PVOID),
    ]
    Parameters.DeviceIoControl = DeviceIoControl
    class QuerySecurity(ctypes.Structure):
        pass


    QuerySecurity._fields_ = [
        ('SecurityInformation', SECURITY_INFORMATION),
        ('POINTER_ALIGNMENT Length', ULONG),
    ]
    Parameters.QuerySecurity = QuerySecurity
    class SetSecurity(ctypes.Structure):
        pass


    SetSecurity._fields_ = [
        ('SecurityInformation', SECURITY_INFORMATION),
        ('SecurityDescriptor', PSECURITY_DESCRIPTOR),
    ]
    Parameters.SetSecurity = SetSecurity
    class MountVolume(ctypes.Structure):
        pass


    MountVolume._fields_ = [
        ('Vpb', PVPB),
        ('DeviceObject', PDEVICE_OBJECT),
    ]
    Parameters.MountVolume = MountVolume
    class VerifyVolume(ctypes.Structure):
        pass


    VerifyVolume._fields_ = [
        ('Vpb', PVPB),
        ('DeviceObject', PDEVICE_OBJECT),
    ]
    Parameters.VerifyVolume = VerifyVolume
    class Scsi(ctypes.Structure):
        pass


    Scsi._fields_ = [
        ('Srb', POINTER(_SCSI_REQUEST_BLOCK)),
    ]
    Parameters.Scsi = Scsi
    class QueryQuota(ctypes.Structure):
        pass


    QueryQuota._fields_ = [
        ('Length', ULONG),
        ('StartSid', PSID),
        ('SidList', PFILE_GET_QUOTA_INFORMATION),
        ('SidListLength', ULONG),
    ]
    Parameters.QueryQuota = QueryQuota
    class SetQuota(ctypes.Structure):
        pass


    SetQuota._fields_ = [
        ('Length', ULONG),
    ]
    Parameters.SetQuota = SetQuota
    class QueryDeviceRelations(ctypes.Structure):
        pass


    QueryDeviceRelations._fields_ = [
        ('Type', DEVICE_RELATION_TYPE),
    ]
    Parameters.QueryDeviceRelations = QueryDeviceRelations
    class QueryInterface(ctypes.Structure):
        pass


    QueryInterface._fields_ = [
        ('GUID *InterfaceType', CONST),
        ('Size', USHORT),
        ('Version', USHORT),
        ('Interface', PINTERFACE),
        ('InterfaceSpecificData', PVOID),
    ]
    Parameters.QueryInterface = QueryInterface
    class DeviceCapabilities(ctypes.Structure):
        pass


    DeviceCapabilities._fields_ = [
        ('Capabilities', PDEVICE_CAPABILITIES),
    ]
    Parameters.DeviceCapabilities = DeviceCapabilities
    class FilterResourceRequirements(ctypes.Structure):
        pass


    FilterResourceRequirements._fields_ = [
        ('IoResourceRequirementList', PIO_RESOURCE_REQUIREMENTS_LIST),
    ]
    Parameters.FilterResourceRequirements = FilterResourceRequirements
    class ReadWriteConfig(ctypes.Structure):
        pass


    ReadWriteConfig._fields_ = [
        ('WhichSpace', ULONG),
        ('Buffer', PVOID),
        ('Offset', ULONG),
        ('POINTER_ALIGNMENT Length', ULONG),
    ]
    Parameters.ReadWriteConfig = ReadWriteConfig
    class SetLock(ctypes.Structure):
        pass


    SetLock._fields_ = [
        ('Lock', BOOLEAN),
    ]
    Parameters.SetLock = SetLock
    class QueryId(ctypes.Structure):
        pass


    QueryId._fields_ = [
        ('IdType', BUS_QUERY_ID_TYPE),
    ]
    Parameters.QueryId = QueryId
    class QueryDeviceText(ctypes.Structure):
        pass


    QueryDeviceText._fields_ = [
        ('DeviceTextType', DEVICE_TEXT_TYPE),
        ('POINTER_ALIGNMENT LocaleId', LCID),
    ]
    Parameters.QueryDeviceText = QueryDeviceText
    class UsageNotification(ctypes.Structure):
        pass


    UsageNotification._fields_ = [
        ('InPath', BOOLEAN),
        ('Reserved', BOOLEAN * 3),
        ('POINTER_ALIGNMENT Type', DEVICE_USAGE_NOTIFICATION_TYPE),
    ]
    Parameters.UsageNotification = UsageNotification
    class WaitWake(ctypes.Structure):
        pass


    WaitWake._fields_ = [
        ('PowerState', SYSTEM_POWER_STATE),
    ]
    Parameters.WaitWake = WaitWake
    class PowerSequence(ctypes.Structure):
        pass


    PowerSequence._fields_ = [
        ('PowerSequence', PPOWER_SEQUENCE),
    ]
    Parameters.PowerSequence = PowerSequence
        class Power(ctypes.Union):
            pass


        class _Union_4(ctypes.Union):
            pass


        _Union_4._fields_ = [
            ('SystemContext', ULONG),
            ('SystemPowerStateContext', SYSTEM_POWER_STATE_CONTEXT),
        ]
        Power._Union_4 = _Union_4
        Power._anonymous_ = (
            '_Union_4',
        )
        Power._fields_ = [
            ('_Union_4', Power._Union_4),
            ('POINTER_ALIGNMENT Type', POWER_STATE_TYPE),
            ('POINTER_ALIGNMENT State', POWER_STATE),
            ('POINTER_ALIGNMENT ShutdownType', POWER_ACTION),
        ]
        Parameters.Power = Power
        class Power(ctypes.Structure):
            pass


        Power._fields_ = [
            ('SystemContext', ULONG),
            ('POINTER_ALIGNMENT Type', POWER_STATE_TYPE),
            ('POINTER_ALIGNMENT State', POWER_STATE),
            ('POINTER_ALIGNMENT ShutdownType', POWER_ACTION),
        ]
        Parameters.Power = Power
    class StartDevice(ctypes.Structure):
        pass


    StartDevice._fields_ = [
        ('AllocatedResources', PCM_RESOURCE_LIST),
        ('AllocatedResourcesTranslated', PCM_RESOURCE_LIST),
    ]
    Parameters.StartDevice = StartDevice
    class WMI(ctypes.Structure):
        pass


    WMI._fields_ = [
        ('ProviderId', ULONG_PTR),
        ('DataPath', PVOID),
        ('BufferSize', ULONG),
        ('Buffer', PVOID),
    ]
    Parameters.WMI = WMI
    class Others(ctypes.Structure):
        pass


    Others._fields_ = [
        ('Argument1', PVOID),
        ('Argument2', PVOID),
        ('Argument3', PVOID),
        ('Argument4', PVOID),
    ]
    Parameters.Others = Others
    Parameters._fields_ = [
        ('Create', Parameters.Create), # System service parameters for: NtCreateFile
        ('CreatePipe', Parameters.CreatePipe), # parse routine other than for the last LONGword.
        ('CreateMailslot', Parameters.CreateMailslot), # parse routine other than for the last LONGword.
        ('Read', Parameters.Read), # System service parameters for: NtReadFile
        ('Write', Parameters.Write), # System service parameters for: NtWriteFile
        ('QueryDirectory', Parameters.QueryDirectory), # System service parameters for: NtQueryDirectoryFile

        # System service parameters for: NtNotifyChangeDirectoryFile /
        # NtNotifyChangeDirectoryFileEx
        ('NotifyDirectory', Parameters.NotifyDirectory),
        ('NotifyDirectoryEx', Parameters.NotifyDirectoryEx), # N.B. Keep Length and CompletionFilter aligned with NotifyDirectory.
        ('QueryFile', Parameters.QueryFile), # System service parameters for: NtQueryInformationFile
        ('SetFile', Parameters.SetFile), # System service parameters for: NtSetInformationFile
        ('QueryEa', Parameters.QueryEa), # System service parameters for: NtQueryEaFile
        ('SetEa', Parameters.SetEa), # System service parameters for: NtSetEaFile
        ('QueryVolume', Parameters.QueryVolume), # System service parameters for: NtQueryVolumeInformationFile
        ('SetVolume', Parameters.SetVolume), # System service parameters for: NtSetVolumeInformationFile
        ('FileSystemControl', Parameters.FileSystemControl), # and the user's input buffer is stored in the SystemBuffer field.
        ('LockControl', Parameters.LockControl), # System service parameters for: NtLockFile/NtUnlockFile
        ('DeviceIoControl', Parameters.DeviceIoControl), # and the user's input buffer is stored in the SystemBuffer field.
        ('QuerySecurity', Parameters.QuerySecurity), # System service parameters for: NtQuerySecurityObject
        ('SetSecurity', Parameters.SetSecurity), # System service parameters for: NtSetSecurityObject
        ('MountVolume', Parameters.MountVolume), # Parameters for MountVolume
        ('VerifyVolume', Parameters.VerifyVolume), # Parameters for VerifyVolume
        ('Scsi', Parameters.Scsi), # Parameters for Scsi with internal device control.
        ('QueryQuota', Parameters.QueryQuota), # System service parameters for: NtQueryQuotaInformationFile
        ('SetQuota', Parameters.SetQuota), # System service parameters for: NtSetQuotaInformationFile
        ('QueryDeviceRelations', Parameters.QueryDeviceRelations), # Parameters for IRP_MN_QUERY_DEVICE_RELATIONS
        ('QueryInterface', Parameters.QueryInterface), # Parameters for IRP_MN_QUERY_INTERFACE
        ('DeviceCapabilities', Parameters.DeviceCapabilities), # Parameters for IRP_MN_QUERY_CAPABILITIES
        ('FilterResourceRequirements', Parameters.FilterResourceRequirements), # Parameters for IRP_MN_FILTER_RESOURCE_REQUIREMENTS
        ('ReadWriteConfig', Parameters.ReadWriteConfig), # Parameters for IRP_MN_READ_CONFIG and IRP_MN_WRITE_CONFIG
        ('SetLock', Parameters.SetLock), # Parameters for IRP_MN_SET_LOCK
        ('QueryId', Parameters.QueryId), # Parameters for IRP_MN_QUERY_ID
        ('QueryDeviceText', Parameters.QueryDeviceText), # Parameters for IRP_MN_QUERY_DEVICE_TEXT
        ('UsageNotification', Parameters.UsageNotification), # Parameters for IRP_MN_DEVICE_USAGE_NOTIFICATION
        ('WaitWake', Parameters.WaitWake), # Parameters for IRP_MN_WAIT_WAKE
        ('PowerSequence', Parameters.PowerSequence), # Parameter for IRP_MN_POWER_SEQUENCE
            ('Power', Parameters.Power), # Parameters for IRP_MN_SET_POWER and IRP_MN_QUERY_POWER
            ('Power', Parameters.Power),
        ('StartDevice', Parameters.StartDevice), # Parameters for StartDevice
        ('WMI', Parameters.WMI), # WMI Irps
        ('Others', Parameters.Others), # Others - driver - specific
    ]
    _IO_STACK_LOCATION.Parameters = Parameters
    _IO_STACK_LOCATION._fields_ = [
        ('MajorFunction', UCHAR),
        ('MinorFunction', UCHAR),
        ('Flags', UCHAR),
        ('Control', UCHAR),
        ('Parameters', _IO_STACK_LOCATION.Parameters), # on the above major and minor function codes.
        ('DeviceObject', PDEVICE_OBJECT), # so it can be passed to the completion routine if needed.
        ('FileObject', PFILE_OBJECT), # request.
        ('CompletionRoutine', PIO_COMPLETION_ROUTINE), # flags field.
        ('Context', PVOID), # that should be passed to the CompletionRoutine.
    ]
    IO_STACK_LOCATION = _IO_STACK_LOCATION
    PIO_STACK_LOCATION = POINTER(_IO_STACK_LOCATION)
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    else:
        pass
    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
    if _MSC_VER >= 1200:
        pass
    # END IF
    if not defined(_AMD64_) and not defined(_ARM_) and not defined(_ARM64_):
        pass
    # END IF
    # Define the share access structure used by file systems to determine
    # whether or not another accessor may open the file.
    class _SHARE_ACCESS(ctypes.Structure):
        pass


    _SHARE_ACCESS._fields_ = [
        ('OpenCount', ULONG),
        ('Readers', ULONG),
        ('Writers', ULONG),
        ('Deleters', ULONG),
        ('SharedRead', ULONG),
        ('SharedWrite', ULONG),
        ('SharedDelete', ULONG),
    ]
    SHARE_ACCESS = _SHARE_ACCESS
    PSHARE_ACCESS = POINTER(_SHARE_ACCESS)

    # Define the share access structure used by file systems (only link files)
    # to determine whether or not another accessor may delete the link.
    # This LCB_SHARE_ACCESS structure is a SHORT version of SHARE_ACCESS and it
    # only contains delete - related share access information.
    # The reason to use this instead of SHARE_ACCESS in LCB is to save space.
    class _LINK_SHARE_ACCESS(ctypes.Structure):
        pass


    _LINK_SHARE_ACCESS._fields_ = [
        ('OpenCount', ULONG),
        ('Deleters', ULONG),
        ('SharedDelete', ULONG),
    ]
    LINK_SHARE_ACCESS = _LINK_SHARE_ACCESS
    PLINK_SHARE_ACCESS = POINTER(_LINK_SHARE_ACCESS)

    # Public I/O routine definitions
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        DEVICE_WITH_IRP_EXTENSION = (PDEVICE_OBJECT)  - 1
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    class _IO_PAGING_PRIORITY(ENUM):
        IoPagingPriorityInvalid = 1
        IoPagingPriorityNormal = 2
        IoPagingPriorityHigh = 3
        IoPagingPriorityReserved1 = 4
        IoPagingPriorityReserved2 = 5


    IO_PAGING_PRIORITY = _IO_PAGING_PRIORITY
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    class _BOOTDISK_INFORMATION(ctypes.Structure):
        pass


    _BOOTDISK_INFORMATION._fields_ = [
        ('BootPartitionOffset', LONGLONG),
        ('SystemPartitionOffset', LONGLONG),
        ('BootDeviceSignature', ULONG),
        ('SystemDeviceSignature', ULONG),
    ]
    BOOTDISK_INFORMATION = _BOOTDISK_INFORMATION
    PBOOTDISK_INFORMATION = POINTER(_BOOTDISK_INFORMATION)

    # This structure should follow the previous structure field for field.
    class _BOOTDISK_INFORMATION_EX(ctypes.Structure):
        pass


    _BOOTDISK_INFORMATION_EX._fields_ = [
        ('BootPartitionOffset', LONGLONG),
        ('SystemPartitionOffset', LONGLONG),
        ('BootDeviceSignature', ULONG),
        ('SystemDeviceSignature', ULONG),
        ('BootDeviceGuid', GUID),
        ('SystemDeviceGuid', GUID),
        ('BootDeviceIsGpt', BOOLEAN),
        ('SystemDeviceIsGpt', BOOLEAN),
    ]
    BOOTDISK_INFORMATION_EX = _BOOTDISK_INFORMATION_EX
    PBOOTDISK_INFORMATION_EX = POINTER(_BOOTDISK_INFORMATION_EX)
    if NTDDI_VERSION >= NTDDI_WIN7:
        class _LOADER_PARTITION_INFORMATION_EX(ctypes.Structure):
            pass


        class _Union_4(ctypes.Union):
            pass


        _Union_4._fields_ = [
            ('Signature', ULONG),
            ('DeviceId', GUID),
        ]
        _LOADER_PARTITION_INFORMATION_EX._Union_4 = _Union_4
        _LOADER_PARTITION_INFORMATION_EX._anonymous_ = (
            '_Union_4',
        )
        _LOADER_PARTITION_INFORMATION_EX._fields_ = [
            ('PartitionStyle', ULONG),
            ('PartitionNumber', ULONG),
            ('_Union_4', _LOADER_PARTITION_INFORMATION_EX._Union_4),
            ('Flags', ULONG),
        ]
        LOADER_PARTITION_INFORMATION_EX = _LOADER_PARTITION_INFORMATION_EX
        PLOADER_PARTITION_INFORMATION_EX = POINTER(_LOADER_PARTITION_INFORMATION_EX)
        class _BOOTDISK_INFORMATION_LITE(ctypes.Structure):
            pass


        _BOOTDISK_INFORMATION_LITE._fields_ = [
            ('NumberEntries', ULONG),
            ('Entries', LOADER_PARTITION_INFORMATION_EX * 1),
        ]
        BOOTDISK_INFORMATION_LITE = _BOOTDISK_INFORMATION_LITE
        PBOOTDISK_INFORMATION_LITE = POINTER(_BOOTDISK_INFORMATION_LITE)
    else:
        if NTDDI_VERSION >= NTDDI_VISTA:
        # END IF   NTDDI_VERSION >= NTDDI_VISTA    # END IF   NTDDI_VERSION >= NTDDI_VISTA
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_VISTA
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:

        # @[comment("MVI_tracked")]    # END IF


    def IoCallDriver(a, b):
        return IofCallDrivera,b

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        pass
    # END IF
    # Define flags taken by Io*ShareAccess routines.
    # Common flags are defined from MSb and function specific flags are
    # defined from LSb.
    # Common Flag
    # Specifies the user has no write permission for the file;
    # this is used to prevent opening a file for exclusive read access
    # when the user does not have appropriate permission. Used when
    # calling IoSetShareAccess and IoCheckShareAccess routines.
    IO_SHARE_ACCESS_NO_WRITE_PERMISSION = 0x80000000

    # Function specific flag
    # Indicates whether we're going to update following structure
    # or not when calling IoCheckLinkShareAccess.
    IO_CHECK_SHARE_ACCESS_UPDATE_SHARE_ACCESS = 0x00000001
    IO_CHECK_SHARE_ACCESS_DONT_UPDATE_FILE_OBJECT = 0x00000002

    # Indicate which part (read/write/delete) of SHARE_ACCESS we're checking
    IO_CHECK_SHARE_ACCESS_DONT_CHECK_READ = 0x00000004
    IO_CHECK_SHARE_ACCESS_DONT_CHECK_WRITE = 0x00000008
    IO_CHECK_SHARE_ACCESS_DONT_CHECK_DELETE = 0x00000010
    IO_CHECK_SHARE_ACCESS_FORCE_CHECK = 0x00000020

    # This value should be returned from completion routines to continue
    # completing the IRP upwards. Otherwise, STATUS_MORE_PROCESSING_REQUIRED
    # should be returned.
    STATUS_CONTINUE_COMPLETION = STATUS_SUCCESS

    # Completion routines can also use this enumeration in place of status
    # codes.


    class _IO_COMPLETION_ROUTINE_RESULT(ENUM):
        #~#~#~ ContinueCompletion = STATUS_CONTINUE_COMPLETION        #~#~#~ StopCompletion = STATUS_MORE_PROCESSING_REQUIRED
        pass


    IO_COMPLETION_ROUTINE_RESULT = _IO_COMPLETION_ROUTINE_RESULT
    PIO_COMPLETION_ROUTINE_RESULT = POINTER(_IO_COMPLETION_ROUTINE_RESULT)
    if NTDDI_VERSION >= NTDDI_WIN2K:

        # @[comment("MVI_tracked")]    # END IF


    def IoCompleteRequest(a, b):
        return IofCompleteRequesta,b

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Interrupt message information table entry definition
    class _IO_INTERRUPT_MESSAGE_INFO_ENTRY(ctypes.Structure):
        pass


    _IO_INTERRUPT_MESSAGE_INFO_ENTRY._fields_ = [
        ('MessageAddress', PHYSICAL_ADDRESS), # generate this message signaled interrupt.
        ('TargetProcessorSet', KAFFINITY), # message in allowed to interrupt.
        ('InterruptObject', PKINTERRUPT), # with this interrupt message. This structure is opaque to drivers.
        ('MessageData', ULONG), # message address in order to generate this interrupt message.
        ('Vector', ULONG), # IoConnectInterruptEx.
        ('Irql', KIRQL),
        ('Mode', KINTERRUPT_MODE),
        ('Polarity', KINTERRUPT_POLARITY),
    ]
    IO_INTERRUPT_MESSAGE_INFO_ENTRY = _IO_INTERRUPT_MESSAGE_INFO_ENTRY
    PIO_INTERRUPT_MESSAGE_INFO_ENTRY = POINTER(_IO_INTERRUPT_MESSAGE_INFO_ENTRY)

    # Interrupt message information table definition
    class _IO_INTERRUPT_MESSAGE_INFO(ctypes.Structure):
        pass


    _IO_INTERRUPT_MESSAGE_INFO._fields_ = [
        ('UnifiedIrql', KIRQL), # will be set to zero.
        ('MessageCount', ULONG), # message information table.
        ('MessageInfo', IO_INTERRUPT_MESSAGE_INFO_ENTRY * 1), # different interrupt message that has been allocated to this device.
    ]
    IO_INTERRUPT_MESSAGE_INFO = _IO_INTERRUPT_MESSAGE_INFO
    PIO_INTERRUPT_MESSAGE_INFO = POINTER(_IO_INTERRUPT_MESSAGE_INFO)

    # Define the connection parameters associated with a fully specified
    # interrupt connection request.
    class _IO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS(ctypes.Structure):
        pass


    _IO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS._fields_ = [
        ('PhysicalDeviceObject', PDEVICE_OBJECT), # interrupt.
        ('InterruptObject', POINTER(PKINTERRUPT)), # association with the interrupt being connected.
        ('ServiceRoutine', PKSERVICE_ROUTINE), # (ISR) that should be executed when the interrupt occurs.
        ('ServiceContext', PVOID), # information that should be passed to the ISR.
        ('PKSPIN_LOCK SpinLock', _In_opt_), # appropriate IRQL and thus synchronize with the ISR.
        ('SynchronizeIrql', KIRQL), # preempted by some other ISR.
        ('FloatingSave', BOOLEAN), # FLOATing point state should be saved before invoking the ISR.
        ('ShareVector', BOOLEAN), # with IRP_MN_START_DEVICE.
        ('Vector', ULONG), # IRP_MN_START_DEVICE.
        ('Irql', KIRQL), # resources sent aLONG with IRP_MN_START_DEVICE.
        ('InterruptMode', KINTERRUPT_MODE), # resources sent aLONG with IRP_MN_START_DEVICE.
        ('ProcessorEnableMask', KAFFINITY), # resources sent aLONG with IRP_MN_START_DEVICE.
        ('Group', USHORT), # group number is always 0.
    ]
    IO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS = _IO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS
    PIO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS = POINTER(_IO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS)

    # Define the connection parameters associated with a line based interrupt
    # connection request.
    class _IO_CONNECT_INTERRUPT_LINE_BASED_PARAMETERS(ctypes.Structure):
        pass


    _IO_CONNECT_INTERRUPT_LINE_BASED_PARAMETERS._fields_ = [
        ('PhysicalDeviceObject', PDEVICE_OBJECT), # device that generates the interrupt of interest.
        ('InterruptObject', POINTER(PKINTERRUPT)), # association with the interrupt being connected.
        ('ServiceRoutine', PKSERVICE_ROUTINE), # (ISR) that should be executed when the interrupt occurs.
        ('ServiceContext', PVOID), # information that should be passed to the ISR.
        ('PKSPIN_LOCK SpinLock', _In_opt_), # appropriate IRQL and thus synchronize with the ISR.
        ('KIRQL SynchronizeIrql', _In_opt_), # case where the spin lock is omitted.
        ('FloatingSave', BOOLEAN), # FLOATing point state should be saved before invoking the ISR.
    ]
    IO_CONNECT_INTERRUPT_LINE_BASED_PARAMETERS = _IO_CONNECT_INTERRUPT_LINE_BASED_PARAMETERS
    PIO_CONNECT_INTERRUPT_LINE_BASED_PARAMETERS = POINTER(_IO_CONNECT_INTERRUPT_LINE_BASED_PARAMETERS)

    # Define the connection parameters associated with a message signaled
    # interrupt connection request.
    class _IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS(ctypes.Structure):
        pass


    class ConnectionContext(ctypes.Union):
        pass


    ConnectionContext._fields_ = [
        ('Generic', POINTER(PVOID)),
        ('InterruptMessageTable', POINTER(PIO_INTERRUPT_MESSAGE_INFO)),
        ('InterruptObject', POINTER(PKINTERRUPT)),
    ]
    _IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS.ConnectionContext = ConnectionContext
    _IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS._fields_ = [
        ('PhysicalDeviceObject', PDEVICE_OBJECT), # device that generates the interrupt messages of interest.
        ('ConnectionContext', _IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS.ConnectionContext), # associated interrupt object.
        ('MessageServiceRoutine', PKMESSAGE_SERVICE_ROUTINE), # messages being connected is signaled.
        ('ServiceContext', PVOID), # information that should be passed to the IMSR.
        ('PKSPIN_LOCK SpinLock', _In_opt_), # signaled.
        ('KIRQL SynchronizeIrql', _In_opt_), # messages with different associated IRQLs.
        ('FloatingSave', BOOLEAN), # FLOATing point state should be saved before invoking the IMSR.
        ('PKSERVICE_ROUTINE FallBackServiceRoutine', _In_opt_), # for the IMSR are reused when connecting the ISR.
    ]
    IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS = _IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS
    PIO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS = POINTER(_IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS)

    # Define the different interrupt connection types that can be requested
    # through IoConnectInterruptEx
    CONNECT_FULLY_SPECIFIED = 0x1
    CONNECT_LINE_BASED = 0x2
    CONNECT_MESSAGE_BASED = 0x3
    CONNECT_FULLY_SPECIFIED_GROUP = 0x4
    CONNECT_MESSAGE_BASED_PASSIVE = 0x5
    CONNECT_CURRENT_VERSION = 0x5

    # Interrupt connection parameter structure definition
    class _IO_CONNECT_INTERRUPT_PARAMETERS(ctypes.Structure):
        pass


    class _Union_5(ctypes.Union):
        pass


    _Union_5._fields_ = [
        ('FullySpecified', IO_CONNECT_INTERRUPT_FULLY_SPECIFIED_PARAMETERS),
        ('LineBased', IO_CONNECT_INTERRUPT_LINE_BASED_PARAMETERS),
        ('MessageBased', IO_CONNECT_INTERRUPT_MESSAGE_BASED_PARAMETERS),
    ]
    _IO_CONNECT_INTERRUPT_PARAMETERS._Union_5 = _Union_5
    _IO_CONNECT_INTERRUPT_PARAMETERS._anonymous_ = (
        '_Union_5',
    )
    _IO_CONNECT_INTERRUPT_PARAMETERS._fields_ = [
        ('ULONG Version', _Inout_), # interrupt connection routine.
        ('_Union_5', _IO_CONNECT_INTERRUPT_PARAMETERS._Union_5), # associated with the different connection types on top of one another.
    ]
    IO_CONNECT_INTERRUPT_PARAMETERS = _IO_CONNECT_INTERRUPT_PARAMETERS
    PIO_CONNECT_INTERRUPT_PARAMETERS = POINTER(_IO_CONNECT_INTERRUPT_PARAMETERS)

    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_VISTA
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    WDM_MAJORVERSION = 0x06
    WDM_MINORVERSION = 0x00

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Interrupt disconnection parameter structure definition
    class _IO_DISCONNECT_INTERRUPT_PARAMETERS(ctypes.Structure):
        pass


    class ConnectionContext(ctypes.Union):
        pass


    ConnectionContext._fields_ = [
        ('Generic', PVOID),
        ('InterruptObject', PKINTERRUPT),
        ('InterruptMessageTable', PIO_INTERRUPT_MESSAGE_INFO),
    ]
    _IO_DISCONNECT_INTERRUPT_PARAMETERS.ConnectionContext = ConnectionContext
    _IO_DISCONNECT_INTERRUPT_PARAMETERS._fields_ = [
        ('Version', ULONG), # IoConnectInterruptEx.
        ('ConnectionContext', _IO_DISCONNECT_INTERRUPT_PARAMETERS.ConnectionContext), # interrupt messages were initially connected.
    ]
    IO_DISCONNECT_INTERRUPT_PARAMETERS = _IO_DISCONNECT_INTERRUPT_PARAMETERS
    PIO_DISCONNECT_INTERRUPT_PARAMETERS = POINTER(_IO_DISCONNECT_INTERRUPT_PARAMETERS)
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_VISTA
    # Interrupt active/inactive reporting parameter structure definition
    class _IO_REPORT_INTERRUPT_ACTIVE_STATE_PARAMETERS(ctypes.Structure):
        pass


    class ConnectionContext(ctypes.Union):
        pass


    ConnectionContext._fields_ = [
        ('Generic', PVOID),
        ('InterruptObject', PKINTERRUPT),
        ('InterruptMessageTable', PIO_INTERRUPT_MESSAGE_INFO),
    ]
    _IO_REPORT_INTERRUPT_ACTIVE_STATE_PARAMETERS.ConnectionContext = ConnectionContext
    _IO_REPORT_INTERRUPT_ACTIVE_STATE_PARAMETERS._fields_ = [
        ('Version', ULONG), # IoConnectInterruptEx.
        ('ConnectionContext', _IO_REPORT_INTERRUPT_ACTIVE_STATE_PARAMETERS.ConnectionContext), # interrupt messages were initially connected.
    ]
    IO_REPORT_INTERRUPT_ACTIVE_STATE_PARAMETERS = _IO_REPORT_INTERRUPT_ACTIVE_STATE_PARAMETERS
    PIO_REPORT_INTERRUPT_ACTIVE_STATE_PARAMETERS = POINTER(_IO_REPORT_INTERRUPT_ACTIVE_STATE_PARAMETERS)
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN8
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN7
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS4:
        PDMA_IOMMU_INTERFACE = POINTER(DMA_IOMMU_INTERFACE,)

    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        IoForwardAndCatchIrp = IoForwardIrpSynchronously
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    # + +
    # ULONG
    # IoGetFunctionCodeFromCtlCode(
    # _In_ ULONG ControlCode
    # )
    # Routine Description:
    # This routine extracts the function code from IOCTL and FSCTL function
    # control codes.
    # This routine should only be used by kernel mode code.
    # Arguments:
    # ControlCode - A function control code (IOCTL or FSCTL) from which the
    # function code must be extracted.
    # Return Value:
    # The extracted function code.
    # Note:
    # The CTL_CODE macro, used to create IOCTL and FSCTL function control
    # codes, is defined in ntioapi.h
    # - -


    def IoGetFunctionCodeFromCtlCode(ControlCode):
        return (( ControlCode >> 2) & 0x00000FFF)

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF


    def IoCallDriverStackSafeDefault(a, b):
        return IoCallDrivera, b

    # The following function is used to tell the caller how much stack is
    # available

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
        if defined(_AMD64_) or defined(_X86_):
            pass
        # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # + +
    # BOOLEAN
    # IoIsErrorUserInduced(
    # _In_ NTSTATUS Status
    # )
    # Routine Description:
    # This routine is invoked to determine if an error was as a
    # result of user actions. Typically these error are related
    # to removable media and will result in a pop - up.
    # Arguments:
    # Status - The status value to check.
    # Return Value:
    # The function value is TRUE if the user induced the error,
    # otherwise FALSE is returned.
    # - -


    def IoIsErrorUserInduced(Status):
        return (BOOLEAN ((Status == STATUS_DEVICE_NOT_READY) or (Status == STATUS_IO_TIMEOUT) or (Status == STATUS_MEDIA_WRITE_PROTECTED) or (Status == STATUS_NO_MEDIA_IN_DEVICE) or (Status == STATUS_VERIFY_REQUIRED) or (Status == STATUS_UNRECOGNIZED_MEDIA) or (Status == STATUS_WRONG_VOLUME)))

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    PIO_REMOVE_LOCK_TRACKING_BLOCK = POINTER()

    class _IO_REMOVE_LOCK_COMMON_BLOCK(ctypes.Structure):
        pass


    _IO_REMOVE_LOCK_COMMON_BLOCK._fields_ = [
        ('Removed', BOOLEAN),
        ('Reserved', BOOLEAN * 3),
        ('LONG        IoCount', __volatile),
        ('RemoveEvent', KEVENT),
    ]
    IO_REMOVE_LOCK_COMMON_BLOCK = _IO_REMOVE_LOCK_COMMON_BLOCK
    class _IO_REMOVE_LOCK_DBG_BLOCK(ctypes.Structure):
        pass


    _IO_REMOVE_LOCK_DBG_BLOCK._fields_ = [
        ('Signature', LONG),
        ('HighWatermark', ULONG),
        ('MaxLockedTicks', LONGLONG),
        ('AllocateTag', LONG),
        ('LockList', LIST_ENTRY),
        ('Spin', KSPIN_LOCK),
        ('LONG        LowMemoryCount', __volatile),
        ('Reserved1', ULONG * 4),
        ('Reserved2', PVOID),
        ('Blocks', PIO_REMOVE_LOCK_TRACKING_BLOCK),
    ]
    IO_REMOVE_LOCK_DBG_BLOCK = _IO_REMOVE_LOCK_DBG_BLOCK
    class _IO_REMOVE_LOCK(ctypes.Structure):
        pass


    _IO_REMOVE_LOCK._fields_ = [
        ('Common', IO_REMOVE_LOCK_COMMON_BLOCK),
            ('Dbg', IO_REMOVE_LOCK_DBG_BLOCK),
    ]
    IO_REMOVE_LOCK = _IO_REMOVE_LOCK
    PIO_REMOVE_LOCK = POINTER(_IO_REMOVE_LOCK)
    if DBG:
        pass
    # END IF


    def IoInitializeRemoveLock(Lock, Tag, Maxmin, HighWater):
        return IoInitializeRemoveLockEx (Lock, Tag, Maxmin, HighWater, ctypes.sizeof IO_REMOVE_LOCK)

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Initialize a remove lock.
    # Note: Allocation for remove locks needs to be within the device
    # extension,
    # so that the memory for this structure stays allocated until such time as
    # the
    # device object itself is deallocated.
    if DBG:


        def IoAcquireRemoveLock(RemoveLock, Tag):
            return IoAcquireRemoveLockEx(RemoveLock, Tag, __FILE__, __LINE__, ctypes.sizeof IO_REMOVE_LOCK)
    else:


        def IoAcquireRemoveLock(RemoveLock, Tag):
            return IoAcquireRemoveLockEx(RemoveLock, Tag, "", 1, ctypes.sizeof IO_REMOVE_LOCK)
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Routine Description:
    # This routine is called to acquire the remove lock for a device object.
    # While the lock is held, the caller can assume that no pending pnp REMOVE
    # requests will be completed.
    # The lock should be acquired immediately upon entering a dispatch routine.
    # It should also be acquired before creating any new reference to the
    # device object if there's a chance of releasing the reference before the
    # new one is done, in addition to references to the driver code itself,
    # which is removed from memory when the last device object goes.
    # Arguments:
    # RemoveLock - A pointer to an initialized REMOVE_LOCK structure.
    # Tag - Used for tracking lock allocation and release. The same tag
    # specified when acquiring the lock must be used to release the lock.
    # Tags are only checked in checked versions of the driver.
    # File - set to __FILE__ as the location in the code where the lock was
    # taken.
    # Line - set to __LINE__.
    # Return Value:
    # Returns whether or not the remove lock was obtained.
    # If successful the caller should continue with work calling
    # IoReleaseRemoveLock when finished.
    # If not successful the lock was not obtained. The caller should abort the
    # work but not call IoReleaseRemoveLock.


    def IoReleaseRemoveLock(RemoveLock, Tag):
        return IoReleaseRemoveLockEx(RemoveLock, Tag, ctypes.sizeof IO_REMOVE_LOCK)

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Routine Description:
    # This routine is called to release the remove lock on the device object.
    # It
    # must be called when finished using a previously locked reference to the
    # device object. If an Tag was specified when acquiring the lock then the
    # same Tag must be specified when releasing the lock.
    # When the lock count reduces to zero, this routine will signal the waiting
    # event to release the waiting thread deleting the device object protected
    # by this lock.
    # Arguments:
    # DeviceObject - the device object to lock
    # Tag - The TAG (if any) specified when acquiring the lock. This is used
    # for lock tracking purposes
    # Return Value:
    # none


    def IoReleaseRemoveLockAndWait(RemoveLock, Tag):
        return IoReleaseRemoveLockAndWaitEx(RemoveLock, Tag, ctypes.sizeof IO_REMOVE_LOCK)

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Routine Description:
    # This routine is called when the client would like to delete the
    # remove - locked resource. This routine will block until all the remove
    # locks have released.
    # This routine MUST be called after acquiring the lock.
    # Arguments:
    # RemoveLock
    # Return Value:
    # none
    # + +
    # USHORT
    # IoSizeOfIrp(
    # _In_ CCHAR StackSize
    # )
    # Routine Description:
    # Determines the size of an IRP given the number of stack locations
    # the IRP will have.
    # Arguments:
    # StackSize - Number of stack locations for the IRP.
    # Return Value:
    # Size in bytes of the IRP.
    # - -


    def IoSizeOfIrp(StackSize):
        return (USHORT (ctypes.sizeof IRP + (StackSize * (ctypes.sizeof IO_STACK_LOCATION ))))

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:

        # @[comment("MVI_tracked")]    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
        if defined(_AMD64_) or defined(_X86_):
            pass
        # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
        if defined(_AMD64_) or defined(_X86_):
            pass
        # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    PIO_WORKITEM = POINTER(_IO_WORKITEM)

    PIO_WORKITEM_ROUTINE = POINTER(IO_WORKITEM_ROUTINE)
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    PIO_WORKITEM_ROUTINE_EX = POINTER(IO_WORKITEM_ROUTINE_EX)
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Action code for IoWMIRegistrationControl api
    WMIREG_ACTION_REGISTER = 1
    WMIREG_ACTION_DEREGISTER = 2
    WMIREG_ACTION_REREGISTER = 3
    WMIREG_ACTION_UPDATE_GUIDS = 4
    WMIREG_ACTION_BLOCK_IRPS = 5

    # Code passed in IRP_MN_REGINFO WMI irp
    WMIREGISTER = 0
    WMIUPDATE = 1

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if defined(_WIN64):
        pass
    else:


        def IoWMIDeviceObjectToProviderId(DeviceObject):
            return ULONGDeviceObject
    # END IF

    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    WMI_NOTIFICATION_CALLBACK = POINTER(FWMI_NOTIFICATION_CALLBACK)
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN8
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    # Cancel SAFE API set start
    # The following APIs are to help ease the pain of writing queue packages
    # that
    # handle the cancellation race well. The idea of this set of APIs is to not
    # force a single queue data structure but allow the cancel logic to be
    # hidden
    # from the drivers. A driver implements a queue and as part of its header
    # includes the IO_CSQ structure. In its initialization routine it calls
    # IoInitializeCsq. Then in the dispatch routine when the driver wants to
    # insert an IRP into the queue it calls IoCsqInsertIrp. When the driver
    # wants
    # to remove something from the queue it calls IoCsqRemoveIrp. Note that
    # Insert
    # can fail if the IRP was canceled in the meantime. Remove can also fail if
    # the IRP was already canceled.
    # There are typically two modes where drivers queue IRPs. These two modes
    # are
    # covered by the cancel safe queue API set.
    # Mode 1:
    # One is where the driver queues the IRP and at some later
    # point in time dequeues an IRP and issues the IO request.
    # For this mode the driver should use IoCsqInsertIrp and
    # IoCsqRemoveNextIrp.
    # The driver in this case is expected to pass NULL to the irp context
    # parameter in IoInsertIrp.
    # Mode 2:
    # In this the driver queues theIRP, issues the IO request
    # (like issuing a DMA
    # request or writing to a
    # register) and when the IO request completes (either
    # using a DPC or
    # timer) the driver dequeues the IRP and completes it. For this
    # mode the driver should use IoCsqInsertIrp and IoCsqRemoveIrp. In this
    # case
    # the driver should allocate an IRP context and pass it in to
    # IoCsqInsertIrp.
    # The cancel API code creates an association between the IRP and the
    # context
    # and thus ensures that when the time comes to remove the IRP it can
    # ascertain
    # correctly.
    # Note that the cancel API set assumes that the field DriverContext[3] is
    # always available for use and that the driver does not use it.
    # Bookkeeping structure. This should be opaque to drivers.
    # Drivers typically include this as part of their queue headers.
    # Given a CSQ pointer the driver should be able to get its
    # queue header using CONTAINING_RECORD macro
    PIO_CSQ = POINTER(IO_CSQ,)

    IO_TYPE_CSQ_IRP_CONTEXT = 1
    IO_TYPE_CSQ = 2
    IO_TYPE_CSQ_EX = 3

    # IRP context structure. This structure is necessary if the driver is using
    # the second mode.
    class _IO_CSQ_IRP_CONTEXT(ctypes.Structure):
        pass


    _IO_CSQ_IRP_CONTEXT._fields_ = [
        ('Type', ULONG),
        ('Irp', PIRP),
        ('Csq', PIO_CSQ),
    ]
    IO_CSQ_IRP_CONTEXT = _IO_CSQ_IRP_CONTEXT
    PIO_CSQ_IRP_CONTEXT = POINTER(_IO_CSQ_IRP_CONTEXT)

    # Routines that insert/remove IRP
    PIO_CSQ_INSERT_IRP = POINTER(IO_CSQ_INSERT_IRP)
    PIO_CSQ_INSERT_IRP_EX = POINTER(IO_CSQ_INSERT_IRP_EX)
    PIO_CSQ_REMOVE_IRP = POINTER(IO_CSQ_REMOVE_IRP)

    # Retrieves next entry after Irp from the queue.
    # Returns NULL if there are no entries in the queue.
    # If Irp is NUL, returns the entry in the head of the queue.
    # This routine does not remove the IRP from the queue.
    PIO_CSQ_PEEK_NEXT_IRP = POINTER(IO_CSQ_PEEK_NEXT_IRP)

    # Lock routine that protects the cancel safe queue.
    PIO_CSQ_ACQUIRE_LOCK = POINTER(IO_CSQ_ACQUIRE_LOCK)
    PIO_CSQ_RELEASE_LOCK = POINTER(IO_CSQ_RELEASE_LOCK)

    # Completes the IRP with STATUS_CANCELLED. IRP is guaranteed to be valid
    # In most cases this routine just calls
    # IoCompleteRequest(Irp, STATUS_CANCELLED);
    PIO_CSQ_COMPLETE_CANCELED_IRP = POINTER(IO_CSQ_COMPLETE_CANCELED_IRP)

    # Bookkeeping structure. This should be opaque to drivers.
    # Drivers typically include this as part of their queue headers.
    # Given a CSQ pointer the driver should be able to get its
    # queue header using CONTAINING_RECORD macro
    class _IO_CSQ(ctypes.Structure):
        pass


    _IO_CSQ._fields_ = [
        ('Type', ULONG),
        ('CsqInsertIrp', PIO_CSQ_INSERT_IRP),
        ('CsqRemoveIrp', PIO_CSQ_REMOVE_IRP),
        ('CsqPeekNextIrp', PIO_CSQ_PEEK_NEXT_IRP),
        ('CsqAcquireLock', PIO_CSQ_ACQUIRE_LOCK),
        ('CsqReleaseLock', PIO_CSQ_RELEASE_LOCK),
        ('CsqCompleteCanceledIrp', PIO_CSQ_COMPLETE_CANCELED_IRP),
        ('ReservePointer', PVOID), # Future expansion
    ]
    IO_CSQ = _IO_CSQ
    PIO_CSQ = POINTER(_IO_CSQ)

    # Initializes the cancel queue structure.

    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    # The caller calls this routine to insert the IRP and return
    # STATUS_PENDING.
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS03:
        pass
    # END IF
    # Returns an IRP if one can be found. NULL otherwise.
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    # This routine is called from timeout or DPCs.
    # The context is presumably part of the DPC or timer context.
    # If successful returns the IRP associated with context.
    if NTDDI_VERSION >= NTDDI_WINXP:
        pass
    # END IF
    # Cancel SAFE API set end
    if NTDDI_VERSION >= NTDDI_WINXPSP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        IO_ATTRIBUTION_INFO_V1 = 1
        class _IO_ATTRIBUTION_INFORMATION(ctypes.Structure):
            pass


        class Flags(ctypes.Structure):
            pass


        class _Struct_13(ctypes.Structure):
            pass


        _Struct_13._fields_ = [
            ('MajorCode', ULONG, 8),
            ('IoStart', ULONG, 1),
            ('QueueOnly', ULONG, 1),
            ('IoFailed', ULONG, 1),
            ('VirtualDevice', ULONG, 1),
            ('Spare', ULONG, 20),
        ]
        Flags._Struct_13 = _Struct_13
        Flags._anonymous_ = (
            '_Struct_13',
        )
        Flags._fields_ = [
            ('_Struct_13', Flags._Struct_13),
            ('AllFlags', ULONG),
        ]
        _IO_ATTRIBUTION_INFORMATION.Flags = Flags
        _IO_ATTRIBUTION_INFORMATION._fields_ = [
            ('Version', ULONG),
            ('Flags', _IO_ATTRIBUTION_INFORMATION.Flags),
            ('Length', ULONG),
            ('ServiceStartTime', ULONGLONG), # Times in units of 100ns.
            ('CurrentTime', ULONGLONG),
        ]
        IO_ATTRIBUTION_INFORMATION = _IO_ATTRIBUTION_INFORMATION
        PIO_ATTRIBUTION_INFORMATION = POINTER(_IO_ATTRIBUTION_INFORMATION)
        IO_SET_IRP_IO_ATTRIBUTION_FROM_THREAD = 0x1
        IO_SET_IRP_IO_ATTRIBUTION_FROM_PROCESS = 0x2
        IO_SET_IRP_IO_ATTRIBUTION_FLAGS_MASK = 0x3
    # END IF


    class _IO_ACCESS_TYPE(ENUM):
        ReadAccess = 1
        WriteAccess = 2
        ModifyAccess = 3


    IO_ACCESS_TYPE = _IO_ACCESS_TYPE
    class _IO_ACCESS_MODE(ENUM):
        SequentialAccess = 1
        RandomAccess = 2


    IO_ACCESS_MODE = _IO_ACCESS_MODE
    class _IO_CONTAINER_NOTIFICATION_CLASS(ENUM):
        IoSessionStateNotification = 1
        IoMaxContainerNotificationClass = 2


    IO_CONTAINER_NOTIFICATION_CLASS = _IO_CONTAINER_NOTIFICATION_CLASS
    class _IO_SESSION_STATE_NOTIFICATION(ctypes.Structure):
        pass


    _IO_SESSION_STATE_NOTIFICATION._fields_ = [
        ('Size', ULONG),
        ('Flags', ULONG),
        ('IoObject', PVOID),
        ('EventMask', ULONG),
        ('Context', PVOID),
    ]
    IO_SESSION_STATE_NOTIFICATION = _IO_SESSION_STATE_NOTIFICATION
    PIO_SESSION_STATE_NOTIFICATION = POINTER(_IO_SESSION_STATE_NOTIFICATION)
    class _IO_CONTAINER_INFORMATION_CLASS(ENUM):
        IoSessionStateInformation = 1
        IoMaxContainerInformationClass = 2


    IO_CONTAINER_INFORMATION_CLASS = _IO_CONTAINER_INFORMATION_CLASS
    class _IO_SESSION_STATE_INFORMATION(ctypes.Structure):
        pass


    _IO_SESSION_STATE_INFORMATION._fields_ = [
        ('SessionId', ULONG),
        ('SessionState', IO_SESSION_STATE),
        ('LocalSession', BOOLEAN),
    ]
    IO_SESSION_STATE_INFORMATION = _IO_SESSION_STATE_INFORMATION
    PIO_SESSION_STATE_INFORMATION = POINTER(_IO_SESSION_STATE_INFORMATION)
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        (*PIO_CONTAINER_NOTIFICATION_FUNCTION)(VOID) = NTSTATUS
        PIO_SESSION_NOTIFICATION_FUNCTION = POINTER(IO_SESSION_NOTIFICATION_FUNCTION)
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if defined(RUN_WPP):
        pass
    # END IF   #ifdef RUN_WPP
    if not defined(_TRACEHANDLE_DEFINED):
        _TRACEHANDLE_DEFINED = 1
        TRACEHANDLE = ULONG64
        PTRACEHANDLE = POINTER(ULONG64)
    # END IF
    # Trace Provider APIs

        if NTDDI_VERSION >= NTDDI_WINXP:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WINXP:
            pass
        # END IF
    if defined(RUN_WPP):
        pass
    # END IF   #ifdef RUN_WPP
    if not defined(TRACE_INFORMATION_CLASS_DEFINE):
        class _ETW_TRACE_SESSION_SETTINGS(ctypes.Structure):
            pass


        _ETW_TRACE_SESSION_SETTINGS._fields_ = [
            ('Version', ULONG),
            ('BufferSize', ULONG),
            ('MinimumBuffers', ULONG),
            ('MaximumBuffers', ULONG),
            ('LoggerMode', ULONG),
            ('FlushTimer', ULONG),
            ('FlushThreshold', ULONG),
            ('ClockType', ULONG),
        ]
        ETW_TRACE_SESSION_SETTINGS = _ETW_TRACE_SESSION_SETTINGS
        PETW_TRACE_SESSION_SETTINGS = POINTER(_ETW_TRACE_SESSION_SETTINGS)
        class _TRACE_INFORMATION_CLASS(ENUM):
            TraceIdClass = 1
            TraceHandleClass = 2
            TraceEnableFlagsClass = 3
            TraceEnableLevelClass = 4
            GlobalLoggerHandleClass = 5
            EventLoggerHandleClass = 6
            AllLoggerHandlesClass = 7
            TraceHandleByNameClass = 8
            LoggerEventsLostClass = 9
            TraceSessionSettingsClass = 10
            LoggerEventsLoggedClass = 11
            DiskIoNotifyRoutinesClass = 12
            TraceInformationClassReserved1 = 13
            FltIoNotifyRoutinesClass = 14
            TraceInformationClassReserved2 = 15
            WdfNotifyRoutinesClass = 16
            MaxTraceInformationClass = 17


        TRACE_INFORMATION_CLASS = _TRACE_INFORMATION_CLASS
        if NTDDI_VERSION >= NTDDI_WINXP:
            pass
        # END IF
        TRACE_INFORMATION_CLASS_DEFINE = 1
    # END IF   TRACE_INFORMATION_CLASS_DEFINE

    if not defined(_ETW_KM_):
        _ETW_KM_ = 1
    # END IF
    # Optional callback function that users provide.
    PETWENABLECALLBACK = POINTER(ETWENABLECALLBACK)

    # Kernel Mode Registration APIs.

    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_THRESHOLD:
        pass
    # END IF
    # Kernel Mode Control (Is Enabled) APIs
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    # Kernel Mode Writing (Publishing/Logging) APIs
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_THRESHOLD:
        pass
    # END IF
    # Define PnP Device Property for IoGetDeviceProperty
    if defined(_PREFAST_):
        __string_type = 0x1000
        __guid_type = 0x2000
        __multiString_type = 0x4000
    else:
        __string_type = 0
        __guid_type = 0
        __multiString_type = 0
    # END IF


    class DEVICE_REGISTRY_PROPERTY(ENUM):
        #~#~#~ DevicePropertyDeviceDescription = 0x0 | __string_type        #~#~#~ DevicePropertyHardwareID = 0x1 | __multiString_type        #~#~#~ DevicePropertyCompatibleIDs = 0x2 | __multiString_type
        DevicePropertyBootConfiguration = 0x3
        DevicePropertyBootConfigurationTranslated = 0x4
        #~#~#~ DevicePropertyClassName = 0x5 | __string_type        #~#~#~ DevicePropertyClassGuid = 0x6 | __string_type        #~#~#~ DevicePropertyDriverKeyName = 0x7 | __string_type        #~#~#~ DevicePropertyManufacturer = 0x8 | __string_type        #~#~#~ DevicePropertyFriendlyName = 0x9 | __string_type        #~#~#~ DevicePropertyLocationInformation = 0xa | __string_type        #~#~#~ DevicePropertyPhysicalDeviceObjectName = 0xb | __string_type        #~#~#~ DevicePropertyBusTypeGuid = 0xc | __guid_type
        DevicePropertyLegacyBusType = 0xD
        DevicePropertyBusNumber = 0xE
        #~#~#~ DevicePropertyEnumeratorName = 0xf | __string_type
        DevicePropertyAddress = 0x10
        DevicePropertyUINumber = 0x11
        DevicePropertyInstallState = 0x12
        DevicePropertyRemovalPolicy = 0x13
        DevicePropertyResourceRequirements = 0x14
        DevicePropertyAllocatedResources = 0x15
        #~#~#~ DevicePropertyContainerID = 0x16 | __string_type


    DevicePropertyBootConfiguration = DEVICE_REGISTRY_PROPERTY.DevicePropertyBootConfiguration
    DevicePropertyBootConfigurationTranslated = DEVICE_REGISTRY_PROPERTY.DevicePropertyBootConfigurationTranslated
    DevicePropertyLegacyBusType = DEVICE_REGISTRY_PROPERTY.DevicePropertyLegacyBusType
    DevicePropertyBusNumber = DEVICE_REGISTRY_PROPERTY.DevicePropertyBusNumber
    DevicePropertyAddress = DEVICE_REGISTRY_PROPERTY.DevicePropertyAddress
    DevicePropertyUINumber = DEVICE_REGISTRY_PROPERTY.DevicePropertyUINumber
    DevicePropertyInstallState = DEVICE_REGISTRY_PROPERTY.DevicePropertyInstallState
    DevicePropertyRemovalPolicy = DEVICE_REGISTRY_PROPERTY.DevicePropertyRemovalPolicy
    DevicePropertyResourceRequirements = DEVICE_REGISTRY_PROPERTY.DevicePropertyResourceRequirements
    DevicePropertyAllocatedResources = DEVICE_REGISTRY_PROPERTY.DevicePropertyAllocatedResources
    PTRANSLATE_BUS_ADDRESS = POINTER(TRANSLATE_BUS_ADDRESS)
    PGET_DMA_ADAPTER = POINTER(GET_DMA_ADAPTER)
    PGET_SET_DEVICE_DATA = POINTER(GET_SET_DEVICE_DATA)
    class _DEVICE_INSTALL_STATE(ENUM):
        InstallStateInstalled = 1
        InstallStateNeedsReinstall = 2
        InstallStateFailedInstall = 3
        InstallStateFinishInstall = 4


    DEVICE_INSTALL_STATE = _DEVICE_INSTALL_STATE
    PDEVICE_INSTALL_STATE = POINTER(_DEVICE_INSTALL_STATE)

    # Define structure returned in response to IRP_MN_QUERY_BUS_INFORMATION by
    # a
    # PDO indicating the type of bus the device exists on.
    class _PNP_BUS_INFORMATION(ctypes.Structure):
        pass


    _PNP_BUS_INFORMATION._fields_ = [
        ('BusTypeGuid', GUID),
        ('LegacyBusType', INTERFACE_TYPE),
        ('BusNumber', ULONG),
    ]
    PNP_BUS_INFORMATION = _PNP_BUS_INFORMATION
    PPNP_BUS_INFORMATION = POINTER(_PNP_BUS_INFORMATION)

    # Define structure returned in response to
    # IRP_MN_QUERY_LEGACY_BUS_INFORMATION
    # by an FDO indicating the type of bus it is. This is normally the same bus
    # type as the device's children
    # (i.e., as retrieved from the child PDO's via
    # IRP_MN_QUERY_BUS_INFORMATION) except for cases like CardBus, which can
    # support both 16 - bit (PCMCIABus) and 32 - bit (PCIBus) cards.
    class _LEGACY_BUS_INFORMATION(ctypes.Structure):
        pass


    _LEGACY_BUS_INFORMATION._fields_ = [
        ('BusTypeGuid', GUID),
        ('LegacyBusType', INTERFACE_TYPE),
        ('BusNumber', ULONG),
    ]
    LEGACY_BUS_INFORMATION = _LEGACY_BUS_INFORMATION
    PLEGACY_BUS_INFORMATION = POINTER(_LEGACY_BUS_INFORMATION)

    # Defines for IoGetDeviceProperty(DevicePropertyRemovalPolicy).
    class _DEVICE_REMOVAL_POLICY(ENUM):
        RemovalPolicyExpectNoRemoval = 1
        RemovalPolicyExpectOrderlyRemoval = 2
        RemovalPolicyExpectSurpriseRemoval = 3


    DEVICE_REMOVAL_POLICY = _DEVICE_REMOVAL_POLICY
    PDEVICE_REMOVAL_POLICY = POINTER(_DEVICE_REMOVAL_POLICY)
    class _BUS_INTERFACE_STANDARD(ctypes.Structure):
        pass


    _BUS_INTERFACE_STANDARD._fields_ = [
        ('Size', USHORT), # generic interface header
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('TranslateBusAddress', PTRANSLATE_BUS_ADDRESS), # standard bus interfaces
        ('GetDmaAdapter', PGET_DMA_ADAPTER),
        ('SetBusData', PGET_SET_DEVICE_DATA),
        ('GetBusData', PGET_SET_DEVICE_DATA),
    ]
    BUS_INTERFACE_STANDARD = _BUS_INTERFACE_STANDARD
    PBUS_INTERFACE_STANDARD = POINTER(_BUS_INTERFACE_STANDARD)
    PGET_VIRTUAL_DEVICE_DATA = POINTER(GET_VIRTUAL_DEVICE_DATA)
    PSET_VIRTUAL_DEVICE_DATA = POINTER(SET_VIRTUAL_DEVICE_DATA)
    PGET_VIRTUAL_DEVICE_LOCATION = POINTER(GET_VIRTUAL_DEVICE_LOCATION)
    PGET_VIRTUAL_DEVICE_RESOURCES = POINTER(GET_VIRTUAL_DEVICE_RESOURCES)
    PENABLE_VIRTUALIZATION = POINTER(ENABLE_VIRTUALIZATION)
    PGET_VIRTUAL_FUNCTION_PROBED_BARS = POINTER(GET_VIRTUAL_FUNCTION_PROBED_BARS)
    class _PCI_VIRTUALIZATION_INTERFACE(ctypes.Structure):
        pass


    _PCI_VIRTUALIZATION_INTERFACE._fields_ = [
        ('Size', USHORT), # generic interface header
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('SetVirtualFunctionData', PSET_VIRTUAL_DEVICE_DATA), # virtualization interfaces
        ('GetVirtualFunctionData', PGET_VIRTUAL_DEVICE_DATA),
        ('GetLocation', PGET_VIRTUAL_DEVICE_LOCATION),
        ('GetResources', PGET_VIRTUAL_DEVICE_RESOURCES),
        ('EnableVirtualization', PENABLE_VIRTUALIZATION),
        ('GetVirtualFunctionProbedBars', PGET_VIRTUAL_FUNCTION_PROBED_BARS),
    ]
    PCI_VIRTUALIZATION_INTERFACE = _PCI_VIRTUALIZATION_INTERFACE
    PPCI_VIRTUALIZATION_INTERFACE = POINTER(_PCI_VIRTUALIZATION_INTERFACE)

    # PCI Security Interface - 6e7f1451 - 199e - 4acc - ba2d - 762b4edf4674
    PCI_SECURITY_INTERFACE_VERSION = 1


    class _PCI_ACS_BIT(ENUM):
        PciAcsReserved = 0
        PciAcsBitEnable = 1
        PciAcsBitDisable = 2
        PciAcsBitDontCare = 3


    PCI_ACS_BIT = _PCI_ACS_BIT
    PPCI_ACS_BIT = POINTER(_PCI_ACS_BIT)
    PPCI_SET_ACS = POINTER(PCI_SET_ACS)
    class _PCI_SECURITY_INTERFACE(ctypes.Structure):
        pass


    _PCI_SECURITY_INTERFACE._fields_ = [
        ('Size', USHORT), # generic interface header
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('SetAccessControlServices', PPCI_SET_ACS),
    ]
    PCI_SECURITY_INTERFACE = _PCI_SECURITY_INTERFACE
    PPCI_SECURITY_INTERFACE = POINTER(_PCI_SECURITY_INTERFACE)
    class _REENUMERATE_SELF_INTERFACE_STANDARD(ctypes.Structure):
        pass


    _REENUMERATE_SELF_INTERFACE_STANDARD._fields_ = [
        ('Size', USHORT), # generic interface header
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('SurpriseRemoveAndReenumerateSelf', PREENUMERATE_SELF), # Self - reenumeration interface
    ]
    REENUMERATE_SELF_INTERFACE_STANDARD = _REENUMERATE_SELF_INTERFACE_STANDARD
    PREENUMERATE_SELF_INTERFACE_STANDARD = POINTER(_REENUMERATE_SELF_INTERFACE_STANDARD)

    # Interface to query the extended address for a device on the bus.
    class _PNP_EXTENDED_ADDRESS_INTERFACE(ctypes.Structure):
        pass


    _PNP_EXTENDED_ADDRESS_INTERFACE._fields_ = [
        ('Size', USHORT), # generic interface header
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('QueryExtendedAddress', PQUERYEXTENDEDADDRESS), # query extended address interface pointer.
    ]
    PNP_EXTENDED_ADDRESS_INTERFACE = _PNP_EXTENDED_ADDRESS_INTERFACE
    PPNP_EXTENDED_ADDRESS_INTERFACE = POINTER(_PNP_EXTENDED_ADDRESS_INTERFACE)
    PNP_EXTENDED_ADDRESS_INTERFACE_VERSION = 0x1

    # D3Cold Support Interface
    D3COLD_SUPPORT_INTERFACE_VERSION = 1
    PSET_D3COLD_SUPPORT = POINTER(SET_D3COLD_SUPPORT)


    class _DEVICE_WAKE_DEPTH(ENUM):
        DeviceWakeDepthNotWakeable = 0
        DeviceWakeDepthD0 = 1
        DeviceWakeDepthD1 = 2
        DeviceWakeDepthD2 = 3
        DeviceWakeDepthD3hot = 4
        DeviceWakeDepthD3cold = 5
        DeviceWakeDepthMaximum = 6


    DEVICE_WAKE_DEPTH = _DEVICE_WAKE_DEPTH
    PDEVICE_WAKE_DEPTH = POINTER(_DEVICE_WAKE_DEPTH)
    PGET_IDLE_WAKE_INFO = POINTER(GET_IDLE_WAKE_INFO)
    PGET_D3COLD_CAPABILITY = POINTER(GET_D3COLD_CAPABILITY)
    class _D3COLD_LAST_TRANSITION_STATUS(ENUM):
        LastDStateTransitionStatusUnknown = 0
        LastDStateTransitionD3hot = 1
        LastDStateTransitionD3cold = 2


    D3COLD_LAST_TRANSITION_STATUS = _D3COLD_LAST_TRANSITION_STATUS
    PD3COLD_LAST_TRANSITION_STATUS = POINTER(_D3COLD_LAST_TRANSITION_STATUS)
    PGET_D3COLD_LAST_TRANSITION_STATUS = POINTER(GET_D3COLD_LAST_TRANSITION_STATUS)
    class _D3COLD_SUPPORT_INTERFACE(ctypes.Structure):
        pass


    _D3COLD_SUPPORT_INTERFACE._fields_ = [
        ('Size', USHORT),
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('SetD3ColdSupport', PSET_D3COLD_SUPPORT),
        ('GetIdleWakeInfo', PGET_IDLE_WAKE_INFO),
        ('GetD3ColdCapability', PGET_D3COLD_CAPABILITY),
        ('GetBusDriverD3ColdSupport', PGET_D3COLD_CAPABILITY),
        ('GetLastTransitionStatus', PGET_D3COLD_LAST_TRANSITION_STATUS),
    ]
    D3COLD_SUPPORT_INTERFACE = _D3COLD_SUPPORT_INTERFACE
    PD3COLD_SUPPORT_INTERFACE = POINTER(_D3COLD_SUPPORT_INTERFACE)
    PD3COLD_REQUEST_CORE_POWER_RAIL = POINTER(D3COLD_REQUEST_CORE_POWER_RAIL)
    PD3COLD_REQUEST_AUX_POWER = POINTER(D3COLD_REQUEST_AUX_POWER)
    PD3COLD_REQUEST_PERST_DELAY = POINTER(D3COLD_REQUEST_PERST_DELAY)
    class _D3COLD_AUX_POWER_AND_TIMING_INTERFACE(ctypes.Structure):
        pass


    _D3COLD_AUX_POWER_AND_TIMING_INTERFACE._fields_ = [
        ('Size', USHORT),
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('RequestCorePowerRail', PD3COLD_REQUEST_CORE_POWER_RAIL),
        ('RequestAuxPower', PD3COLD_REQUEST_AUX_POWER),
        ('RequestPerstDelay', PD3COLD_REQUEST_PERST_DELAY),
    ]
    D3COLD_AUX_POWER_AND_TIMING_INTERFACE = _D3COLD_AUX_POWER_AND_TIMING_INTERFACE
    PD3COLD_AUX_POWER_AND_TIMING_INTERFACE = POINTER(_D3COLD_AUX_POWER_AND_TIMING_INTERFACE)
    PFPGA_BUS_SCAN = POINTER(FPGA_BUS_SCAN)
    PFPGA_CONTROL_LINK = POINTER(FPGA_CONTROL_LINK)
    PFPGA_CONTROL_CONFIG_SPACE = POINTER(FPGA_CONTROL_CONFIG_SPACE)
    PFPGA_CONTROL_ERROR_REPORTING = POINTER(FPGA_CONTROL_ERROR_REPORTING)
    class _FPGA_CONTROL_INTERFACE(ctypes.Structure):
        pass


    _FPGA_CONTROL_INTERFACE._fields_ = [
        ('Size', USHORT),
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('BusScan', PFPGA_BUS_SCAN),
        ('ControlLink', PFPGA_CONTROL_LINK),
        ('ControlConfigSpace', PFPGA_CONTROL_CONFIG_SPACE),
        ('ControlErrorReporting', PFPGA_CONTROL_ERROR_REPORTING),
    ]
    FPGA_CONTROL_INTERFACE = _FPGA_CONTROL_INTERFACE
    PFPGA_CONTROL_INTERFACE = POINTER(_FPGA_CONTROL_INTERFACE)

    # The following definitions are used in ACPI QueryInterface
    class _ACPI_INTERFACE_STANDARD(ctypes.Structure):
        pass


    _ACPI_INTERFACE_STANDARD._fields_ = [
        ('Size', USHORT), # Generic interface header
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('GpeConnectVector', PGPE_CONNECT_VECTOR), # ACPI interfaces
        ('GpeDisconnectVector', PGPE_DISCONNECT_VECTOR),
        ('GpeEnableEvent', PGPE_ENABLE_EVENT),
        ('GpeDisableEvent', PGPE_DISABLE_EVENT),
        ('GpeClearStatus', PGPE_CLEAR_STATUS),
        ('RegisterForDeviceNotifications', PREGISTER_FOR_DEVICE_NOTIFICATIONS),
        ('UnregisterForDeviceNotifications', PUNREGISTER_FOR_DEVICE_NOTIFICATIONS),
    ]
    ACPI_INTERFACE_STANDARD = _ACPI_INTERFACE_STANDARD
    PACPI_INTERFACE_STANDARD = POINTER(_ACPI_INTERFACE_STANDARD)

    # The following definitions are used in GUID_ACPI_INTERFACE_STANDARD2,
    # The first version (above) passes in DEVICE_OBJECs, where this one
    # is based on Contexts.
    class ACPI_INTERFACE_STANDARD2(ctypes.Structure):
        pass


    ACPI_INTERFACE_STANDARD2._fields_ = [
        ('Size', USHORT), # Generic interface header
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('GpeConnectVector', PGPE_CONNECT_VECTOR2), # ACPI interfaces
        ('GpeDisconnectVector', PGPE_DISCONNECT_VECTOR2),
        ('GpeEnableEvent', PGPE_ENABLE_EVENT2),
        ('GpeDisableEvent', PGPE_DISABLE_EVENT2),
        ('GpeClearStatus', PGPE_CLEAR_STATUS2),
        ('RegisterForDeviceNotifications', PREGISTER_FOR_DEVICE_NOTIFICATIONS2),
        ('UnregisterForDeviceNotifications', PUNREGISTER_FOR_DEVICE_NOTIFICATIONS2),
    ]
    PACPI_INTERFACE_STANDARD2 = POINTER(ACPI_INTERFACE_STANDARD2)
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # The following definitions are used in IoOpenDeviceRegistryKey
    PLUGPLAY_REGKEY_DEVICE = 1
    PLUGPLAY_REGKEY_DRIVER = 2
    PLUGPLAY_REGKEY_CURRENT_HWPROFILE = 4

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    DEVICE_INTERFACE_INCLUDE_NONACTIVE = 0x00000001

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Define PnP notification event categories
    class _IO_NOTIFICATION_EVENT_CATEGORY(ENUM):
        EventCategoryReserved = 1
        EventCategoryHardwareProfileChange = 2
        EventCategoryDeviceInterfaceChange = 3
        EventCategoryTargetDeviceChange = 4


    IO_NOTIFICATION_EVENT_CATEGORY = _IO_NOTIFICATION_EVENT_CATEGORY

    # Define flags that modify the behavior of IoRegisterPlugPlayNotification
    # for the various event categories...
    PNPNOTIFY_DEVICE_INTERFACE_INCLUDE_EXISTING_INTERFACES = 0x00000001

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    PDEVICE_CHANGE_COMPLETE_CALLBACK = POINTER(DEVICE_CHANGE_COMPLETE_CALLBACK)
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF


    def IoAdjustPagingPathCount(_count_, _paging_):
        return { if _paging_ { InterlockedIncrement_count_; } else { InterlockedDecrement_count_; } }

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS4:
        class _DRIVER_DIRECTORY_TYPE(ENUM):
            DriverDirectoryImage = 0
            DriverDirectoryData = 1


        DRIVER_DIRECTORY_TYPE = _DRIVER_DIRECTORY_TYPE
        PDRIVER_DIRECTORY_TYPE = POINTER(_DRIVER_DIRECTORY_TYPE)
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS4:
        class _DEVICE_DIRECTORY_TYPE(ENUM):
            DeviceDirectoryData = 0


        DEVICE_DIRECTORY_TYPE = _DEVICE_DIRECTORY_TYPE
        PDEVICE_DIRECTORY_TYPE = POINTER(_DEVICE_DIRECTORY_TYPE)
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS4:
        class _DRIVER_REGKEY_TYPE(ENUM):
            DriverRegKeyParameters = 0
            DriverRegKeyPersistentState = 1


        DRIVER_REGKEY_TYPE = _DRIVER_REGKEY_TYPE
        PDRIVER_REGKEY_TYPE = POINTER(_DRIVER_REGKEY_TYPE)
    # END IF
    # Header structure for all Plug & Play notification events...
    class _PLUGPLAY_NOTIFICATION_HEADER(ctypes.Structure):
        pass


    _PLUGPLAY_NOTIFICATION_HEADER._fields_ = [
        ('Version', USHORT), # presently at version 1.
        ('Size', USHORT), # size (in bytes) of header + event - specific data.
        ('Event', GUID),
    ]
    PLUGPLAY_NOTIFICATION_HEADER = _PLUGPLAY_NOTIFICATION_HEADER
    PPLUGPLAY_NOTIFICATION_HEADER = POINTER(_PLUGPLAY_NOTIFICATION_HEADER)

    # Notification structure for all EventCategoryHardwareProfileChange
    # events...
    class _HWPROFILE_CHANGE_NOTIFICATION(ctypes.Structure):
        pass


    _HWPROFILE_CHANGE_NOTIFICATION._fields_ = [
        ('Version', USHORT),
        ('Size', USHORT),
        ('Event', GUID),
    ]
    HWPROFILE_CHANGE_NOTIFICATION = _HWPROFILE_CHANGE_NOTIFICATION
    PHWPROFILE_CHANGE_NOTIFICATION = POINTER(_HWPROFILE_CHANGE_NOTIFICATION)

    # Notification structure for all EventCategoryDeviceInterfaceChange
    # events...
    class _DEVICE_INTERFACE_CHANGE_NOTIFICATION(ctypes.Structure):
        pass


    _DEVICE_INTERFACE_CHANGE_NOTIFICATION._fields_ = [
        ('Version', USHORT),
        ('Size', USHORT),
        ('Event', GUID),
        ('InterfaceClassGuid', GUID), # Event - specific data
        ('SymbolicLinkName', PUNICODE_STRING),
    ]
    DEVICE_INTERFACE_CHANGE_NOTIFICATION = _DEVICE_INTERFACE_CHANGE_NOTIFICATION
    PDEVICE_INTERFACE_CHANGE_NOTIFICATION = POINTER(_DEVICE_INTERFACE_CHANGE_NOTIFICATION)

    # Notification structures for EventCategoryTargetDeviceChange...
    # The following structure is used for TargetDeviceQueryRemove,
    # TargetDeviceRemoveCancelled, and TargetDeviceRemoveComplete:
    class _TARGET_DEVICE_REMOVAL_NOTIFICATION(ctypes.Structure):
        pass


    _TARGET_DEVICE_REMOVAL_NOTIFICATION._fields_ = [
        ('Version', USHORT),
        ('Size', USHORT),
        ('Event', GUID),
        ('FileObject', PFILE_OBJECT), # Event - specific data
    ]
    TARGET_DEVICE_REMOVAL_NOTIFICATION = _TARGET_DEVICE_REMOVAL_NOTIFICATION
    PTARGET_DEVICE_REMOVAL_NOTIFICATION = POINTER(_TARGET_DEVICE_REMOVAL_NOTIFICATION)

    # The following structure header is used for all other (i.e., 3rd - party)
    # target device change events. The structure accommodates both a
    # variable - length binary data buffer, and a variable - length unicode
    # text
    # buffer. The header must indicate where the text buffer begins, so that
    # the data can be delivered in the appropriate format (ANSI or Unicode)
    # to user - mode recipients (i.e., that have registered for handle - based
    # notification via RegisterDeviceNotification).
    class _TARGET_DEVICE_CUSTOM_NOTIFICATION(ctypes.Structure):
        pass


    _TARGET_DEVICE_CUSTOM_NOTIFICATION._fields_ = [
        ('Version', USHORT),
        ('Size', USHORT),
        ('Event', GUID),
        ('FileObject', PFILE_OBJECT), # This field must be set to NULL by callers of
        ('NameBufferOffset', LONG), # offset (in bytes) from beginning of
        ('CustomDataBuffer', UCHAR * 1), # variable - length buffer, containing (optionally)
    ]
    TARGET_DEVICE_CUSTOM_NOTIFICATION = _TARGET_DEVICE_CUSTOM_NOTIFICATION
    PTARGET_DEVICE_CUSTOM_NOTIFICATION = POINTER(_TARGET_DEVICE_CUSTOM_NOTIFICATION)
    if NTDDI_VERSION >= NTDDI_VISTA:

        # Custom device properties...
        # Definitions of property flags.
        PLUGPLAY_PROPERTY_PERSISTENT = 0x00000001
    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WS08:
        pass
    # END IF
    # Define replace driver entrypoint.
    PPNP_REPLACE_DRIVER_INTERFACE = POINTER(_PNP_REPLACE_DRIVER_INTERFACE)


    # Define parameters to replace driver.
    PNP_REPLACE_NO_MAP = MAXLONGLONG
    class _PNP_REPLACE_MEMORY_LIST(ctypes.Structure):
        pass


    _PNP_REPLACE_MEMORY_LIST.Ranges = Ranges
    _PNP_REPLACE_MEMORY_LIST._fields_ = [
        ('AllocatedCount', ULONG),
        ('Count', ULONG),
        ('TotalLength', ULONGLONG),
        ('Ranges', _PNP_REPLACE_MEMORY_LIST.Ranges * ANYSIZE_ARRAY),
    ]
    PNP_REPLACE_MEMORY_LIST = _PNP_REPLACE_MEMORY_LIST
    PPNP_REPLACE_MEMORY_LIST = POINTER(_PNP_REPLACE_MEMORY_LIST)
    class _PNP_REPLACE_PROCESSOR_LIST(ctypes.Structure):
        pass


    _PNP_REPLACE_PROCESSOR_LIST._fields_ = [
        ('Affinity', PKAFFINITY),
        ('GroupCount', ULONG),
        ('AllocatedCount', ULONG),
        ('Count', ULONG),
        ('ApicIds', ULONG * ANYSIZE_ARRAY),
    ]
    PNP_REPLACE_PROCESSOR_LIST = _PNP_REPLACE_PROCESSOR_LIST
    PPNP_REPLACE_PROCESSOR_LIST = POINTER(_PNP_REPLACE_PROCESSOR_LIST)
    class _PNP_REPLACE_PROCESSOR_LIST_V1(ctypes.Structure):
        pass


    _PNP_REPLACE_PROCESSOR_LIST_V1._fields_ = [
        ('AffinityMask', KAFFINITY),
        ('AllocatedCount', ULONG),
        ('Count', ULONG),
        ('ApicIds', ULONG * ANYSIZE_ARRAY),
    ]
    PNP_REPLACE_PROCESSOR_LIST_V1 = _PNP_REPLACE_PROCESSOR_LIST_V1
    PPNP_REPLACE_PROCESSOR_LIST_V1 = POINTER(_PNP_REPLACE_PROCESSOR_LIST_V1)
    PNP_REPLACE_PARAMETERS_VERSION = 2
    class _PNP_REPLACE_PARAMETERS(ctypes.Structure):
        pass


    _PNP_REPLACE_PARAMETERS._fields_ = [
        ('Size', ULONG),
        ('Version', ULONG),
        ('Target', ULONG64),
        ('Spare', ULONG64),
        ('TargetProcessors', PPNP_REPLACE_PROCESSOR_LIST),
        ('SpareProcessors', PPNP_REPLACE_PROCESSOR_LIST),
        ('TargetMemory', PPNP_REPLACE_MEMORY_LIST),
        ('SpareMemory', PPNP_REPLACE_MEMORY_LIST),
        ('MapMemory', PREPLACE_MAP_MEMORY),
    ]
    PNP_REPLACE_PARAMETERS = _PNP_REPLACE_PARAMETERS
    PPNP_REPLACE_PARAMETERS = POINTER(_PNP_REPLACE_PARAMETERS)

    # Define replace driver interface.
    PNP_REPLACE_DRIVER_INTERFACE_VERSION = 1
    PNP_REPLACE_DRIVER_INTERFACE_MINIMUM_SIZE = UFIELD_OFFSET(
        PNP_REPLACE_DRIVER_INTERFACE,
        InitiateHardwareMirror,
    )
    PNP_REPLACE_MEMORY_SUPPORTED = 0x0001
    PNP_REPLACE_PROCESSOR_SUPPORTED = 0x0002
    PNP_REPLACE_HARDWARE_MEMORY_MIRRORING = 0x0004
    PNP_REPLACE_HARDWARE_PAGE_COPY = 0x0008
    PNP_REPLACE_HARDWARE_QUIESCE = 0x0010

    # Define interface structure.
    class _PNP_REPLACE_DRIVER_INTERFACE(ctypes.Structure):
        pass


    _PNP_REPLACE_DRIVER_INTERFACE._fields_ = [
        ('Size', ULONG),
        ('Version', ULONG),
        ('Flags', ULONG),
        ('Unload', PREPLACE_UNLOAD),
        ('BeginReplace', PREPLACE_BEGIN),
        ('EndReplace', PREPLACE_END),
        ('MirrorPhysicalMemory', PREPLACE_MIRROR_PHYSICAL_MEMORY),
        ('SetProcessorId', PREPLACE_SET_PROCESSOR_ID),
        ('Swap', PREPLACE_SWAP),
        ('InitiateHardwareMirror', PREPLACE_INITIATE_HARDWARE_MIRROR),
        ('MirrorPlatformMemory', PREPLACE_MIRROR_PLATFORM_MEMORY),
        ('GetMemoryDestination', PREPLACE_GET_MEMORY_DESTINATION),
        ('EnableDisableHardwareQuiesce', PREPLACE_ENABLE_DISABLE_HARDWARE_QUIESCE),
    ]
    PNP_REPLACE_DRIVER_INTERFACE = _PNP_REPLACE_DRIVER_INTERFACE
    PPNP_REPLACE_DRIVER_INTERFACE = POINTER(_PNP_REPLACE_DRIVER_INTERFACE)

    if NTDDI_VERSION >= NTDDI_WINBLUE:

        # Define crashdump runtime power interface.
        class _CRASHDUMP_FUNCTIONS_INTERFACE(ctypes.Structure):
            pass


        _CRASHDUMP_FUNCTIONS_INTERFACE._fields_ = [
            ('Size', USHORT), # generic interface header
            ('Version', USHORT),
            ('Context', PVOID),
            ('InterfaceReference', PINTERFACE_REFERENCE),
            ('InterfaceDereference', PINTERFACE_DEREFERENCE),
            ('PowerOn', PCRASHDUMP_POWER_ON), # Power - on at crashdump time method
        ]
        CRASHDUMP_FUNCTIONS_INTERFACE = _CRASHDUMP_FUNCTIONS_INTERFACE
        PCRASHDUMP_FUNCTIONS_INTERFACE = POINTER(_CRASHDUMP_FUNCTIONS_INTERFACE)
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        DEVICE_RESET_INTERFACE_VERSION = 1

        # Define an enum for various reset types supported.
        # Note reset type value should not exceed 31 as the
        # "SupportedResetTypes"
        # field within the reset interface is a ULONG.


        class _DEVICE_RESET_TYPE(ENUM):
            FunctionLevelDeviceReset = 1
            PlatformLevelDeviceReset = 2


        DEVICE_RESET_TYPE = _DEVICE_RESET_TYPE
        PDEVICE_RESET_COMPLETION = POINTER(DEVICE_RESET_COMPLETION)
        class _FUNCTION_LEVEL_DEVICE_RESET_PARAMETERS(ctypes.Structure):
            pass


        _FUNCTION_LEVEL_DEVICE_RESET_PARAMETERS._fields_ = [
            ('Size', ULONG),
            ('DeviceResetCompletion', PDEVICE_RESET_COMPLETION),
            ('CompletionContext', PVOID),
        ]
        FUNCTION_LEVEL_DEVICE_RESET_PARAMETERS = _FUNCTION_LEVEL_DEVICE_RESET_PARAMETERS
        PFUNCTION_LEVEL_DEVICE_RESET_PARAMETERS = POINTER(_FUNCTION_LEVEL_DEVICE_RESET_PARAMETERS)
        class _DEVICE_RESET_INTERFACE_STANDARD(ctypes.Structure):
            pass


        _DEVICE_RESET_INTERFACE_STANDARD._fields_ = [
            ('Size', USHORT), # generic interface header
            ('Version', USHORT),
            ('Context', PVOID),
            ('InterfaceReference', PINTERFACE_REFERENCE),
            ('InterfaceDereference', PINTERFACE_DEREFERENCE),
            ('DeviceReset', PDEVICE_RESET_HANDLER), # device reset interface
            ('SupportedResetTypes', ULONG),
            ('Reserved', PVOID),
        ]
        DEVICE_RESET_INTERFACE_STANDARD = _DEVICE_RESET_INTERFACE_STANDARD
        PDEVICE_RESET_INTERFACE_STANDARD = POINTER(_DEVICE_RESET_INTERFACE_STANDARD)
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS2:
        SECURE_DRIVER_INTERFACE_VERSION = 1
        PSECURE_DRIVER_PROCESS_REFERENCE = POINTER(SECURE_DRIVER_PROCESS_REFERENCE)
        PSECURE_DRIVER_PROCESS_DEREFERENCE = POINTER(SECURE_DRIVER_PROCESS_DEREFERENCE)
        class _SECURE_DRIVER_INTERFACE(ctypes.Structure):
            pass


        _SECURE_DRIVER_INTERFACE._fields_ = [
            ('InterfaceHeader', INTERFACE),
            ('ProcessReference', PSECURE_DRIVER_PROCESS_REFERENCE),
            ('ProcessDereference', PSECURE_DRIVER_PROCESS_DEREFERENCE),
            ('Reserved', ULONG),
        ]
        SECURE_DRIVER_INTERFACE = _SECURE_DRIVER_INTERFACE
        PSECURE_DRIVER_INTERFACE = POINTER(_SECURE_DRIVER_INTERFACE)
    # END IF
    SDEV_IDENTIFIER_INTERFACE_VERSION = 1
    PGET_SDEV_IDENTIFIER = POINTER(GET_SDEV_IDENTIFIER)
    class _SDEV_IDENTIFIER_INTERFACE(ctypes.Structure):
        pass


    _SDEV_IDENTIFIER_INTERFACE._fields_ = [
        ('InterfaceHeader', INTERFACE),
        ('GetIdentifier', PGET_SDEV_IDENTIFIER),
    ]
    SDEV_IDENTIFIER_INTERFACE = _SDEV_IDENTIFIER_INTERFACE
    PSDEV_IDENTIFIER_INTERFACE = POINTER(_SDEV_IDENTIFIER_INTERFACE)

    # Define the device description structure.
    class _DEVICE_DESCRIPTION(ctypes.Structure):
        pass


    _DEVICE_DESCRIPTION._fields_ = [
        ('Version', ULONG),
        ('Master', BOOLEAN),
        ('ScatterGather', BOOLEAN),
        ('DemandMode', BOOLEAN),
        ('AutoInitialize', BOOLEAN),
        ('Dma32BitAddresses', BOOLEAN),
        ('IgnoreCount', BOOLEAN),
        ('Reserved1', BOOLEAN), # must be false
        ('Dma64BitAddresses', BOOLEAN),
        ('BusNumber', ULONG), # unused for WDM
        ('DmaChannel', ULONG),
        ('InterfaceType', INTERFACE_TYPE),
        ('DmaWidth', DMA_WIDTH),
        ('DmaSpeed', DMA_SPEED),
        ('MaximumLength', ULONG),
        ('DmaPort', ULONG),
            ('DmaAddressWidth', ULONG),
            ('DmaControllerInstance', ULONG),
            ('DmaRequestLine', ULONG),
            ('DeviceAddress', PHYSICAL_ADDRESS),
    ]
    DEVICE_DESCRIPTION = _DEVICE_DESCRIPTION
    PDEVICE_DESCRIPTION = POINTER(_DEVICE_DESCRIPTION)

    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF  NTDDI_VERSION >= NTDDI_WIN8
    # Define the supported version numbers for the device description
    # structure.
    DEVICE_DESCRIPTION_VERSION = 0
    DEVICE_DESCRIPTION_VERSION1 = 1
    DEVICE_DESCRIPTION_VERSION2 = 2
    DEVICE_DESCRIPTION_VERSION3 = 3

    # Define the supported version numbers for DMA adapter info and the
    # DMA transfer info structure.
    DMA_ADAPTER_INFO_VERSION1 = 1
    DMA_TRANSFER_INFO_VERSION1 = 1
    class _DMA_ADAPTER_INFO_V1(ctypes.Structure):
        pass


    _DMA_ADAPTER_INFO_V1._fields_ = [
        ('ReadDmaCounterAvailable', ULONG),
        ('ScatterGatherLimit', ULONG),
        ('DmaAddressWidth', ULONG),
        ('Flags', ULONG),
        ('MinimumTransferUnit', ULONG),
    ]
    DMA_ADAPTER_INFO_V1 = _DMA_ADAPTER_INFO_V1
    PDMA_ADAPTER_INFO_V1 = POINTER(_DMA_ADAPTER_INFO_V1)
    class _DMA_ADAPTER_INFO(ctypes.Structure):
        pass


    class _Union_6(ctypes.Union):
        pass


    _Union_6._fields_ = [
        ('V1', DMA_ADAPTER_INFO_V1),
    ]
    _DMA_ADAPTER_INFO._Union_6 = _Union_6
    _DMA_ADAPTER_INFO._anonymous_ = (
        '_Union_6',
    )
    _DMA_ADAPTER_INFO._fields_ = [
        ('Version', ULONG),
        ('_Union_6', _DMA_ADAPTER_INFO._Union_6),
    ]
    DMA_ADAPTER_INFO = _DMA_ADAPTER_INFO
    PDMA_ADAPTER_INFO = POINTER(_DMA_ADAPTER_INFO)

    # Define the bits in the adapter info flags.
    ADAPTER_INFO_SYNCHRONOUS_CALLBACK = 0x0001
    ADAPTER_INFO_API_BYPASS = 0x0002
    class _DMA_TRANSFER_INFO_V1(ctypes.Structure):
        pass


    _DMA_TRANSFER_INFO_V1._fields_ = [
        ('MapRegisterCount', ULONG),
        ('ScatterGatherElementCount', ULONG),
        ('ScatterGatherListSize', ULONG),
    ]
    DMA_TRANSFER_INFO_V1 = _DMA_TRANSFER_INFO_V1
    PDMA_TRANSFER_INFO_V1 = POINTER(_DMA_TRANSFER_INFO_V1)
    class _DMA_TRANSFER_INFO(ctypes.Structure):
        pass


    class _Union_7(ctypes.Union):
        pass


    _Union_7._fields_ = [
        ('V1', DMA_TRANSFER_INFO_V1),
    ]
    _DMA_TRANSFER_INFO._Union_7 = _Union_7
    _DMA_TRANSFER_INFO._anonymous_ = (
        '_Union_7',
    )
    _DMA_TRANSFER_INFO._fields_ = [
        ('Version', ULONG),
        ('_Union_7', _DMA_TRANSFER_INFO._Union_7),
    ]
    DMA_TRANSFER_INFO = _DMA_TRANSFER_INFO
    PDMA_TRANSFER_INFO = POINTER(_DMA_TRANSFER_INFO)

    # Define the supported version numbers and the corresponding sizes of
    # opaque
    # DMA transfer context structure.
    DMA_TRANSFER_CONTEXT_VERSION1 = 1

    if defined (_WIN64):
        DMA_TRANSFER_CONTEXT_SIZE_V1 = 128
    else:
        DMA_TRANSFER_CONTEXT_SIZE_V1 = 64
    # END IF
    # Define the flags used in AllocateAdapterChannelEx,
    # GetScatterGatherListEx,
    # and BuildScatterGatherListEx.
    DMA_SYNCHRONOUS_CALLBACK = 0x01
    DMA_ZERO_BUFFERS = 0x02

    # Performance counter function.

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Stall processor execution function.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    HAL_MASK_UNMASK_FLAGS_NONE = 0x0
    HAL_MASK_UNMASK_FLAGS_SERVICING_DEFERRED = 0x1
    HAL_MASK_UNMASK_FLAGS_SERVICING_COMPLETE = 0x2

    # Processor driver halt routine.
    PPROCESSOR_HALT_ROUTINE = POINTER(PROCESSOR_HALT_ROUTINE)
    class _SCATTER_GATHER_ELEMENT(ctypes.Structure):
        pass


    _SCATTER_GATHER_ELEMENT._fields_ = [
        ('Address', PHYSICAL_ADDRESS),
        ('Length', ULONG),
        ('Reserved', ULONG_PTR),
    ]
    SCATTER_GATHER_ELEMENT = _SCATTER_GATHER_ELEMENT
    PSCATTER_GATHER_ELEMENT = POINTER(_SCATTER_GATHER_ELEMENT)

        if _MSC_VER >= 1200:
            pass
        # END IF
    if defined(_MSC_EXTENSIONS):
        class _SCATTER_GATHER_LIST(ctypes.Structure):
            pass


        _SCATTER_GATHER_LIST._fields_ = [
            ('NumberOfElements', ULONG),
            ('Reserved', ULONG_PTR),
            ('Elements', SCATTER_GATHER_ELEMENT * ),
        ]
        SCATTER_GATHER_LIST = _SCATTER_GATHER_LIST
        PSCATTER_GATHER_LIST = POINTER(_SCATTER_GATHER_LIST)
        if _MSC_VER >= 1200:
            pass
        else:
            pass
        # END IF
    else:
        _SCATTER_GATHER_LIST = struct

        PSCATTER_GATHER_LIST = POINTER(SCATTER_GATHER_LIST,)

    # END IF
    PDMA_OPERATIONS = POINTER(_DMA_OPERATIONS)

    HAL_DMA_ADAPTER_VERSION_1 = 1
    class _DMA_ADAPTER(ctypes.Structure):
        pass


    _DMA_ADAPTER._fields_ = [
        ('Version', USHORT),
        ('Size', USHORT),
        ('DmaOperations', PDMA_OPERATIONS),
    ]
    DMA_ADAPTER = _DMA_ADAPTER
    PDMA_ADAPTER = POINTER(_DMA_ADAPTER)


    class DMA_COMPLETION_STATUS(ENUM):
        DmaComplete = 1
        DmaAborted = 2
        DmaError = 3
        DmaCancelled = 4


    DmaComplete = DMA_COMPLETION_STATUS.DmaComplete
    DmaAborted = DMA_COMPLETION_STATUS.DmaAborted
    DmaError = DMA_COMPLETION_STATUS.DmaError
    DmaCancelled = DMA_COMPLETION_STATUS.DmaCancelled
    PDRIVER_LIST_CONTROL = POINTER(DRIVER_LIST_CONTROL)
    PDMA_COMPLETION_ROUTINE = POINTER(DMA_COMPLETION_ROUTINE)

    # Define the bits in the allocate domain common buffer flags.
    DOMAIN_COMMON_BUFFER_LARGE_PAGE = 0x0001
    class _DMA_OPERATIONS(ctypes.Structure):
        pass


    _DMA_OPERATIONS._fields_ = [
        ('Size', ULONG),
        ('PutDmaAdapter', PPUT_DMA_ADAPTER),
        ('AllocateCommonBuffer', PALLOCATE_COMMON_BUFFER),
        ('FreeCommonBuffer', PFREE_COMMON_BUFFER),
        ('AllocateAdapterChannel', PALLOCATE_ADAPTER_CHANNEL),
        ('FlushAdapterBuffers', PFLUSH_ADAPTER_BUFFERS),
        ('FreeAdapterChannel', PFREE_ADAPTER_CHANNEL),
        ('FreeMapRegisters', PFREE_MAP_REGISTERS),
        ('MapTransfer', PMAP_TRANSFER),
        ('GetDmaAlignment', PGET_DMA_ALIGNMENT),
        ('ReadDmaCounter', PREAD_DMA_COUNTER),
        ('GetScatterGatherList', PGET_SCATTER_GATHER_LIST),
        ('PutScatterGatherList', PPUT_SCATTER_GATHER_LIST),
        ('CalculateScatterGatherList', PCALCULATE_SCATTER_GATHER_LIST_SIZE),
        ('BuildScatterGatherList', PBUILD_SCATTER_GATHER_LIST),
        ('BuildMdlFromScatterGatherList', PBUILD_MDL_FROM_SCATTER_GATHER_LIST),
        ('GetDmaAdapterInfo', PGET_DMA_ADAPTER_INFO),
        ('GetDmaTransferInfo', PGET_DMA_TRANSFER_INFO),
        ('InitializeDmaTransferContext', PINITIALIZE_DMA_TRANSFER_CONTEXT),
        ('AllocateCommonBufferEx', PALLOCATE_COMMON_BUFFER_EX),
        ('AllocateAdapterChannelEx', PALLOCATE_ADAPTER_CHANNEL_EX),
        ('ConfigureAdapterChannel', PCONFIGURE_ADAPTER_CHANNEL),
        ('CancelAdapterChannel', PCANCEL_ADAPTER_CHANNEL),
        ('MapTransferEx', PMAP_TRANSFER_EX),
        ('GetScatterGatherListEx', PGET_SCATTER_GATHER_LIST_EX),
        ('BuildScatterGatherListEx', PBUILD_SCATTER_GATHER_LIST_EX),
        ('FlushAdapterBuffersEx', PFLUSH_ADAPTER_BUFFERS_EX),
        ('FreeAdapterObject', PFREE_ADAPTER_OBJECT),
        ('CancelMappedTransfer', PCANCEL_MAPPED_TRANSFER),
        ('AllocateDomainCommonBuffer', PALLOCATE_DOMAIN_COMMON_BUFFER),
        ('FlushDmaBuffer', PFLUSH_DMA_BUFFER),
        ('JoinDmaDomain', PJOIN_DMA_DOMAIN),
        ('LeaveDmaDomain', PLEAVE_DMA_DOMAIN),
        ('GetDmaDomain', PGET_DMA_DOMAIN),
        ('AllocateCommonBufferWithBounds', PALLOCATE_COMMON_BUFFER_WITH_BOUNDS),
    ]
    DMA_OPERATIONS = _DMA_OPERATIONS

    if defined(USE_DMA_MACROS) and not defined(_NTHAL_) and (defined(_NTDDK_) or defined(_NTDRIVER_)) or defined(_WDM_INCLUDED_): #  ntddk
        pass
    # END IF   USE_DMA_MACROS and (_NTDDK_ or _NTDRIVER_)
    if NTDDI_VERSION >= NTDDI_WIN10_RS4:

        # Types for domain configuration.
        class _DOMAIN_CONFIGURATION_ARCH(ENUM):
            DomainConfigurationArm64 = 1
            DomainConfigurationInvalid = 2


        DOMAIN_CONFIGURATION_ARCH = _DOMAIN_CONFIGURATION_ARCH
        PDOMAIN_CONFIGURATION_ARCH = POINTER(_DOMAIN_CONFIGURATION_ARCH)
        class _DOMAIN_CONFIGURATION_ARM64(ctypes.Structure):
            pass


        _DOMAIN_CONFIGURATION_ARM64._fields_ = [
            ('Ttbr0', PHYSICAL_ADDRESS),
            ('Ttbr1', PHYSICAL_ADDRESS),
            ('Mair0', ULONG),
            ('Mair1', ULONG),
            ('InputSize0', UCHAR),
            ('InputSize1', UCHAR),
        ]
        DOMAIN_CONFIGURATION_ARM64 = _DOMAIN_CONFIGURATION_ARM64
        PDOMAIN_CONFIGURATION_ARM64 = POINTER(_DOMAIN_CONFIGURATION_ARM64)
        class _DOMAIN_CONFIGURATION(ctypes.Structure):
            pass


        class _Union_8(ctypes.Union):
            pass


        _Union_8._fields_ = [
            ('Arm64', DOMAIN_CONFIGURATION_ARM64),
        ]
        _DOMAIN_CONFIGURATION._Union_8 = _Union_8
        _DOMAIN_CONFIGURATION._anonymous_ = (
            '_Union_8',
        )
        _DOMAIN_CONFIGURATION._fields_ = [
            ('Type', DOMAIN_CONFIGURATION_ARCH),
            ('_Union_8', _DOMAIN_CONFIGURATION._Union_8),
        ]
        DOMAIN_CONFIGURATION = _DOMAIN_CONFIGURATION
        PDOMAIN_CONFIGURATION = POINTER(_DOMAIN_CONFIGURATION)

        # Types for fault information.
        class _FAULT_INFORMATION_ARCH(ENUM):
            FaultInformationInvalid = 1
            FaultInformationArm64 = 2


        FAULT_INFORMATION_ARCH = _FAULT_INFORMATION_ARCH
        PFAULT_INFORMATION_ARCH = POINTER(_FAULT_INFORMATION_ARCH)
        class _FAULT_INFORMATION_ARM64(ctypes.Structure):
            pass


        class Flags(ctypes.Structure):
            pass


        Flags._fields_ = [
            ('WriteNotRead', ULONG, 1),
            ('InstructionNotData', ULONG, 1),
            ('Privileged', ULONG, 1),
            ('Multi', ULONG, 1),
            ('Asynchronous', ULONG, 1),
            ('PageTableWalkFault', ULONG, 1),
            ('Reserved', ULONG, 26),
        ]
        _FAULT_INFORMATION_ARM64.Flags = Flags
        _FAULT_INFORMATION_ARM64._fields_ = [
            ('DomainHandle', PVOID),
            ('FaultAddress', PVOID),
            ('PhysicalDeviceObject', PDEVICE_OBJECT),
            ('InputMappingId', ULONG),
            ('Flags', _FAULT_INFORMATION_ARM64.Flags),
            ('{ UnsupportedUpstreamTransaction', enum),
            ('AddressSizeFault', enum),
            ('TlbMatchConflict', enum),
            ('ExternalFault', enum),
            ('PermissionFault', enum),
            ('AccessFlagFault', enum),
            ('TranslationFault', enum),
            ('} Type', enum),
        ]
        FAULT_INFORMATION_ARM64 = _FAULT_INFORMATION_ARM64
        PFAULT_INFORMATION_ARM64 = POINTER(_FAULT_INFORMATION_ARM64)
        class _FAULT_INFORMATION(ctypes.Structure):
            pass


        class _Union_9(ctypes.Union):
            pass


        _Union_9._fields_ = [
            ('Arm64', FAULT_INFORMATION_ARM64),
        ]
        _FAULT_INFORMATION._Union_9 = _Union_9
        _FAULT_INFORMATION._anonymous_ = (
            '_Union_9',
        )
        _FAULT_INFORMATION._fields_ = [
            ('Type', FAULT_INFORMATION_ARCH),
            ('_Union_9', _FAULT_INFORMATION._Union_9),
        ]
        FAULT_INFORMATION = _FAULT_INFORMATION
        PFAULT_INFORMATION = POINTER(_FAULT_INFORMATION)
        PIOMMU_DOMAIN_FAULT_HANDLER = POINTER(IOMMU_DOMAIN_FAULT_HANDLER)

        # + + Routine Description: This routine creates a new DMA remapping
        # device domain (effectively a container for a set of page tables).
        # Arguments: OsManagedPageTable - Supplies a BOOL indicating whether
        # the page table will be managed by the caller or by the HAL. TRUE
        # indicates the HAL owns the page table. Map/Unmap are available.
        # Configure/Flush are unavailable. FALSE indicates that the caller
        # owns the page table. Map/Unmap are unavailable. Configure/Flush are
        # available. DomainOut - Supplies a pointer to receive an opaque
        # handle used to reference the domain. Return Value: NTSTATUS code. - -
        PIOMMU_DOMAIN_CREATE = POINTER(IOMMU_DOMAIN_CREATE)

        # + + Routine Description: This routine deletes an existing domain.
        # The domain must contain no devices in order to be successfully
        # deleted. Arguments: Domain - Supplies a handle to the domain to
        # delete. Return Value: NTSTATUS code. - -
        PIOMMU_DOMAIN_DELETE = POINTER(IOMMU_DOMAIN_DELETE)

        # + + Routine Description: This routine attaches a device to an
        # existing domain. Arguments: Domain - Supplies a handle to the
        # domain. PhysicalDeviceObject - Supplies the device object.
        # InputMappingIdBase - Supplies the input mapping base for the
        # device's desired stream. MappingCount - Supplies the count of
        # mappings beginning at the base. N.B. InputMappingIdBase and
        # MappingCount are intended only to accommodate ACPI enumerated
        # devices which support multiple stream IDs on ARM64. For any other
        # device or architecture, these values must be: InputMappingIdBase = 0
        # MappingCount = 1 Return Value: NTSTATUS code. - -
        PIOMMU_DOMAIN_ATTACH_DEVICE = POINTER(IOMMU_DOMAIN_ATTACH_DEVICE)

        # + + Routine Description: This routine detaches a device from an
        # existing domain. Arguments: Domain - Supplies a handle to the
        # domain. PhysicalDeviceObject - Supplies a pointer to the device
        # object representing the device. InputMappingId - Supplies the input
        # mapping for the device's desired stream. N.B. InputMappingId is used
        # only for ACPI enumerated devices on ARM64. In all other cases this
        # value must be zero. N.B. If multiple devices are simultaneously
        # attached using MappingCount, then those devices can only be detached
        # as a group by specifying an InputMappingId equal to the
        # InputMappingIdBase used when attaching. Return Value: NTSTATUS code.
        # - -
        PIOMMU_DOMAIN_DETACH_DEVICE = POINTER(IOMMU_DOMAIN_DETACH_DEVICE)

        # + + Routine Description: This routine configures a domain for use. A
        # domain will have all DMA blocked until it is configured. Arguments:
        # Domain - Supplies a pointer to the domain. Configuration - Supplies
        # a new configuration for the domain. Return Value: NTSTATUS code. - -
        PIOMMU_DOMAIN_CONFIGURE = POINTER(IOMMU_DOMAIN_CONFIGURE)

        # + + Routine Description: This routine flushes the TLB for all
        # entries which match this domain. Arguments: Domain - Supplies a
        # handle to the domain. Return Value: NTSTATUS code. - -
        PIOMMU_FLUSH_DOMAIN = POINTER(IOMMU_FLUSH_DOMAIN)

        # + + Routine Description: This routine flushes the TLB for all
        # entries which match this domain's ASID and one of the addresses in
        # the provided list. Arguments: Domain - Supplies a pointer to the
        # domain. LastLevel - Supplies whether only entries pertaining to the
        # last level of translation require flushing. Number - Supplies the
        # number of entries in the VA list. VaList - Supplies a list of flush
        # addresses. Return Value: NTSTATUS code. - -
        PIOMMU_FLUSH_DOMAIN_VA_LIST = POINTER(IOMMU_FLUSH_DOMAIN_VA_LIST)
        class _INPUT_MAPPING_ELEMENT(ctypes.Structure):
            pass


        _INPUT_MAPPING_ELEMENT._fields_ = [
            ('InputMappingId', ULONG),
        ]
        INPUT_MAPPING_ELEMENT = _INPUT_MAPPING_ELEMENT
        PINPUT_MAPPING_ELEMENT = POINTER(_INPUT_MAPPING_ELEMENT)

        # + + Routine Description: This routine will attempt to find input
        # mapping IDs which are valid for the given device and populate the
        # provied buffer with those IDs. If the buffer is of insufficient
        # length, no IDs will be written and ReturnLength (if provided) will
        # be populated with the required buffer size. This routine is
        # currently only supported on ARM64 architectures. Arguments:
        # PhysicalDeviceObject - Supplies the device object to query. Buffer -
        # Supplies a pointer to the buffer to populate. BufferLength -
        # Supplies the length of the buffer. ReturnLength - Supplies an
        # optional pointer to store the amount of data written
        # (or data that would be written if a buffer of sufficient size was provided). Return Value: STATUS_BUFFER_TOO_SMALL if the provided buffer is of insufficient size. STATUS_UNSUCCESSFUL if the request cannot be satisfied. STATUS_SUCCESS if the buffer has been populated correctly. - -
        #
        PIOMMU_QUERY_INPUT_MAPPINGS = POINTER(IOMMU_QUERY_INPUT_MAPPINGS)

        # + + Routine Description: This routine maps a range of pages into the
        # address space of a domain. N.B. The provided MDL must specify a
        # whole number of pages and the logical address must be page aligned.
        # Arguments: Domain - Supplies a pointer to the domain. Permissions -
        # Supplies the permissions to map the pages with. Mdl - Supplies the
        # MDL to map. LogicalAddress - Supplies the logical address to begin
        # mapping at. Return Value: NTSTATUS. - -
        PIOMMU_MAP_LOGICAL_RANGE = POINTER(IOMMU_MAP_LOGICAL_RANGE)

        # + + Routine Description: This routine unmaps a linear range from a
        # domain. N.B. The supplied logical address must be page aligned.
        # Arguments: Domain - Supplies a pointer to the domain. LogicalAddress
        # - Supplies the beginning address to unmap. NumberOfPages - Supplies
        # the number of pages to unmap. Return Value: NTSTATUS. - -
        PIOMMU_UNMAP_LOGICAL_RANGE = POINTER(IOMMU_UNMAP_LOGICAL_RANGE)

        # + + Routine Description: This routine creates an identity mapping
        # for the provided MDL in the provided domain. Arguments: Domain -
        # Supplies a pointer to the domain. Permissions - Supplies the
        # permissions for the mapping. Mdl - Supplies the MDL to map. Return
        # Value: NTSTATUS. - -
        PIOMMU_MAP_IDENTITY_RANGE = POINTER(IOMMU_MAP_IDENTITY_RANGE)

        # + + Routine Description: This routine deletes an identity mapping
        # for the specified MDL. Arguments: Domain - Supplies a pointer to the
        # domain. Mdl - Supplies a pointer to the MDL to unmap. Return Value:
        # NTSTATUS. - -
        PIOMMU_UNMAP_IDENTITY_RANGE = POINTER(IOMMU_UNMAP_IDENTITY_RANGE)
        DMA_IOMMU_INTERFACE_VERSION_1 = 1UL
        DMA_IOMMU_INTERFACE_VERSION = DMA_IOMMU_INTERFACE_VERSION_1
        class _DMA_IOMMU_INTERFACE(ctypes.Structure):
            pass


        _DMA_IOMMU_INTERFACE._fields_ = [
            ('Version', ULONG),
            ('CreateDomain', PIOMMU_DOMAIN_CREATE), # Version 1 routines.
            ('DeleteDomain', PIOMMU_DOMAIN_DELETE),
            ('AttachDevice', PIOMMU_DOMAIN_ATTACH_DEVICE),
            ('DetachDevice', PIOMMU_DOMAIN_DETACH_DEVICE),
            ('ConfigureDomain', PIOMMU_DOMAIN_CONFIGURE),
            ('FlushDomain', PIOMMU_FLUSH_DOMAIN),
            ('FlushDomainByVaList', PIOMMU_FLUSH_DOMAIN_VA_LIST),
            ('QueryInputMappings', PIOMMU_QUERY_INPUT_MAPPINGS),
            ('MapLogicalRange', PIOMMU_MAP_LOGICAL_RANGE),
            ('UnmapLogicalRange', PIOMMU_UNMAP_LOGICAL_RANGE),
            ('MapIdentityRange', PIOMMU_MAP_IDENTITY_RANGE),
            ('UnmapIdentityRange', PIOMMU_UNMAP_IDENTITY_RANGE),
        ]
        DMA_IOMMU_INTERFACE = _DMA_IOMMU_INTERFACE
        PDMA_IOMMU_INTERFACE = POINTER(_DMA_IOMMU_INTERFACE)
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS4)
    # memory_range.Type
    PO_MEM_PRESERVE = 0x00000001
    PO_MEM_CLONE = 0x00000002
    PO_MEM_CL_OR_NCHK = 0x00000004
    PO_MEM_DISCARD = 0x00008000
    PO_MEM_PAGE_ADDRESS = 0x00004000
    PO_MEM_BOOT_PHASE = 0x00010000

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    PREQUEST_POWER_COMPLETE = POINTER(REQUEST_POWER_COMPLETE)
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF


    def PoSetDeviceBusy(IdlePointer):
        return *IdlePointer = 0

    if NTDDI_VERSION >= NTDDI_WIN6SP1:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    PPOWER_SETTING_CALLBACK = POINTER(POWER_SETTING_CALLBACK)
    if NTDDI_VERSION >= NTDDI_VISTA:

        # @[comment("MVI_tracked")]    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    # \Callback\PowerState values
    PO_CB_SYSTEM_POWER_POLICY = 0
    PO_CB_AC_STATUS = 1
    PO_CB_BUTTON_COLLISION = 2
    PO_CB_SYSTEM_STATE_LOCK = 3
    PO_CB_LID_SWITCH_STATE = 4
    PO_CB_PROCESSOR_POWER_POLICY = 5

    # Runtime Power Management Framework
    PO_FX_VERSION_V1 = 0x00000001
    PO_FX_VERSION_V2 = 0x00000002
    PO_FX_VERSION = PO_FX_VERSION_V1
    POHANDLE = DECLARE_HANDLE()
    PPO_FX_POWER_CONTROL_CALLBACK = POINTER(PO_FX_POWER_CONTROL_CALLBACK)
    class _PO_FX_COMPONENT_IDLE_STATE(ctypes.Structure):
        pass


    _PO_FX_COMPONENT_IDLE_STATE._fields_ = [
        ('TransitionLatency', ULONGLONG),
        ('ResidencyRequirement', ULONGLONG),
        ('NominalPower', ULONG),
    ]
    PO_FX_COMPONENT_IDLE_STATE = _PO_FX_COMPONENT_IDLE_STATE
    PPO_FX_COMPONENT_IDLE_STATE = POINTER(_PO_FX_COMPONENT_IDLE_STATE)
    class _PO_FX_COMPONENT_V1(ctypes.Structure):
        pass


    _PO_FX_COMPONENT_V1._fields_ = [
        ('Id', GUID),
        ('IdleStateCount', ULONG),
        ('DeepestWakeableIdleState', ULONG),
        ('IdleStates', PPO_FX_COMPONENT_IDLE_STATE),
    ]
    PO_FX_COMPONENT_V1 = _PO_FX_COMPONENT_V1
    PPO_FX_COMPONENT_V1 = POINTER(_PO_FX_COMPONENT_V1)
    class _PO_FX_DEVICE_V1(ctypes.Structure):
        pass


    _PO_FX_DEVICE_V1._fields_ = [
        ('Version', ULONG),
        ('ComponentCount', ULONG),
        ('ComponentActiveConditionCallback', PPO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK),
        ('ComponentIdleConditionCallback', PPO_FX_COMPONENT_IDLE_CONDITION_CALLBACK),
        ('ComponentIdleStateCallback', PPO_FX_COMPONENT_IDLE_STATE_CALLBACK),
        ('DevicePowerRequiredCallback', PPO_FX_DEVICE_POWER_REQUIRED_CALLBACK),
        ('DevicePowerNotRequiredCallback', PPO_FX_DEVICE_POWER_NOT_REQUIRED_CALLBACK),
        ('PowerControlCallback', PPO_FX_POWER_CONTROL_CALLBACK),
        ('DeviceContext', PVOID),
        ('Components', PO_FX_COMPONENT_V1 * ANYSIZE_ARRAY),
    ]
    PO_FX_DEVICE_V1 = _PO_FX_DEVICE_V1
    PPO_FX_DEVICE_V1 = POINTER(_PO_FX_DEVICE_V1)
    PO_FX_COMPONENT_FLAG_F0_ON_DX = 0x0000000000000001
    PO_FX_COMPONENT_FLAG_NO_DEBOUNCE = 0x0000000000000002
    class _PO_FX_COMPONENT_V2(ctypes.Structure):
        pass


    _PO_FX_COMPONENT_V2._fields_ = [
        ('Id', GUID),
        ('Flags', ULONGLONG),
        ('DeepestWakeableIdleState', ULONG),
        ('IdleStateCount', ULONG),
        ('IdleStates', PPO_FX_COMPONENT_IDLE_STATE),
        ('ProviderCount', ULONG),
        ('Providers', PULONG),
    ]
    PO_FX_COMPONENT_V2 = _PO_FX_COMPONENT_V2
    PPO_FX_COMPONENT_V2 = POINTER(_PO_FX_COMPONENT_V2)
    class _PO_FX_DEVICE_V2(ctypes.Structure):
        pass


    _PO_FX_DEVICE_V2._fields_ = [
        ('Version', ULONG),
        ('Flags', ULONGLONG),
        ('ComponentActiveConditionCallback', PPO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK),
        ('ComponentIdleConditionCallback', PPO_FX_COMPONENT_IDLE_CONDITION_CALLBACK),
        ('ComponentIdleStateCallback', PPO_FX_COMPONENT_IDLE_STATE_CALLBACK),
        ('DevicePowerRequiredCallback', PPO_FX_DEVICE_POWER_REQUIRED_CALLBACK),
        ('DevicePowerNotRequiredCallback', PPO_FX_DEVICE_POWER_NOT_REQUIRED_CALLBACK),
        ('PowerControlCallback', PPO_FX_POWER_CONTROL_CALLBACK),
        ('DeviceContext', PVOID),
        ('ComponentCount', ULONG),
        ('Components', PO_FX_COMPONENT_V2 * ANYSIZE_ARRAY),
    ]
    PO_FX_DEVICE_V2 = _PO_FX_DEVICE_V2
    PPO_FX_DEVICE_V2 = POINTER(_PO_FX_DEVICE_V2)

    if PO_FX_VERSION == PO_FX_VERSION_V1:
        PO_FX_COMPONENT = PO_FX_COMPONENT_V1
        PPO_FX_COMPONENT = POINTER(PO_FX_COMPONENT_V1)
        PO_FX_DEVICE = PO_FX_DEVICE_V1
        PPO_FX_DEVICE = POINTER(PO_FX_DEVICE_V1)
    elif PO_FX_VERSION == PO_FX_VERSION_V2:
        PO_FX_COMPONENT = PO_FX_COMPONENT_V2
        PPO_FX_COMPONENT = POINTER(PO_FX_COMPONENT_V2)
        PO_FX_DEVICE = PO_FX_DEVICE_V2
        PPO_FX_DEVICE = POINTER(PO_FX_DEVICE_V2)
    else:
        pass
    # END IF
    class _PO_FX_PERF_STATE_UNIT(ENUM):
        PoFxPerfStateUnitOther = 1
        PoFxPerfStateUnitFrequency = 2
        PoFxPerfStateUnitBandwidth = 3
        PoFxPerfStateUnitMaximum = 4


    PO_FX_PERF_STATE_UNIT = _PO_FX_PERF_STATE_UNIT
    PPO_FX_PERF_STATE_UNIT = POINTER(_PO_FX_PERF_STATE_UNIT)
    class _PO_FX_PERF_STATE_TYPE(ENUM):
        PoFxPerfStateTypeDiscrete = 1
        PoFxPerfStateTypeRange = 2
        PoFxPerfStateTypeMaximum = 3


    PO_FX_PERF_STATE_TYPE = _PO_FX_PERF_STATE_TYPE
    PPO_FX_PERF_STATE_TYPE = POINTER(_PO_FX_PERF_STATE_TYPE)
    class _PO_FX_PERF_STATE(ctypes.Structure):
        pass


    _PO_FX_PERF_STATE._fields_ = [
        ('Value', ULONGLONG),
        ('Context', PVOID),
    ]
    PO_FX_PERF_STATE = _PO_FX_PERF_STATE
    PPO_FX_PERF_STATE = POINTER(_PO_FX_PERF_STATE)
    class _PO_FX_COMPONENT_PERF_SET(ctypes.Structure):
        pass


    class _Struct_13(ctypes.Structure):
        pass


    class Discrete(ctypes.Structure):
        pass


    Discrete._fields_ = [
        ('Count', ULONG),
        ('States', PPO_FX_PERF_STATE),
    ]
    _Struct_13.Discrete = Discrete
    class Range(ctypes.Structure):
        pass


    Range._fields_ = [
        ('Minimum', ULONGLONG),
        ('Maximum', ULONGLONG),
    ]
    _Struct_13.Range = Range
    _Struct_13._fields_ = [
        ('Discrete', _Struct_13.Discrete),
        ('Range', _Struct_13.Range),
    ]
    _PO_FX_COMPONENT_PERF_SET._Struct_13 = _Struct_13
    _PO_FX_COMPONENT_PERF_SET._anonymous_ = (
        '_Struct_13',
    )
    _PO_FX_COMPONENT_PERF_SET._fields_ = [
        ('Name', UNICODE_STRING),
        ('Flags', ULONGLONG),
        ('Unit', PO_FX_PERF_STATE_UNIT),
        ('Type', PO_FX_PERF_STATE_TYPE),
        ('_Struct_13', _PO_FX_COMPONENT_PERF_SET._Struct_13),
    ]
    PO_FX_COMPONENT_PERF_SET = _PO_FX_COMPONENT_PERF_SET
    PPO_FX_COMPONENT_PERF_SET = POINTER(_PO_FX_COMPONENT_PERF_SET)
    class _PO_FX_COMPONENT_PERF_INFO(ctypes.Structure):
        pass


    _PO_FX_COMPONENT_PERF_INFO._fields_ = [
        ('PerfStateSetsCount', ULONG),
        ('PerfStateSets', PO_FX_COMPONENT_PERF_SET * ANYSIZE_ARRAY),
    ]
    PO_FX_COMPONENT_PERF_INFO = _PO_FX_COMPONENT_PERF_INFO
    PPO_FX_COMPONENT_PERF_INFO = POINTER(_PO_FX_COMPONENT_PERF_INFO)
    class _PO_FX_PERF_STATE_CHANGE(ctypes.Structure):
        pass


    class _Union_10(ctypes.Union):
        pass


    _Union_10._fields_ = [
        ('StateIndex', ULONG),
        ('StateValue', ULONGLONG),
    ]
    _PO_FX_PERF_STATE_CHANGE._Union_10 = _Union_10
    _PO_FX_PERF_STATE_CHANGE._anonymous_ = (
        '_Union_10',
    )
    _PO_FX_PERF_STATE_CHANGE._fields_ = [
        ('Set', ULONG),
        ('_Union_10', _PO_FX_PERF_STATE_CHANGE._Union_10),
    ]
    PO_FX_PERF_STATE_CHANGE = _PO_FX_PERF_STATE_CHANGE
    PPO_FX_PERF_STATE_CHANGE = POINTER(_PO_FX_PERF_STATE_CHANGE)

    # Driver interfaces for runtime framework.
    PO_FX_UNKNOWN_POWER = 0xFFFFFFFF
    PO_FX_UNKNOWN_TIME = 0xFFFFFFFFFFFFFFFF
    PO_FX_FLAG_BLOCKING = 0x01
    PO_FX_FLAG_ASYNC_ONLY = 0x02
    PO_FX_FLAG_PERF_PEP_OPTIONAL = 0x01
    PO_FX_FLAG_PERF_QUERY_ON_F0 = 0x02
    PO_FX_FLAG_PERF_QUERY_ON_ALL_IDLE_STATES = 0x04

    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
    class _PO_THERMAL_REQUEST_TYPE(ENUM):
        PoThermalRequestPassive = 1
        PoThermalRequestActive = 2


    PO_THERMAL_REQUEST_TYPE = _PO_THERMAL_REQUEST_TYPE
    PPO_THERMAL_REQUEST_TYPE = POINTER(_PO_THERMAL_REQUEST_TYPE)
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS2:
        pass
    # END IF
    # Object Manager types
    class _OBJECT_HANDLE_INFORMATION(ctypes.Structure):
        pass


    _OBJECT_HANDLE_INFORMATION._fields_ = [
        ('HandleAttributes', ULONG),
        ('GrantedAccess', ACCESS_MASK),
    ]
    OBJECT_HANDLE_INFORMATION = _OBJECT_HANDLE_INFORMATION
    POBJECT_HANDLE_INFORMATION = POINTER(_OBJECT_HANDLE_INFORMATION)
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:

        # @[comment("MVI_tracked")]    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:


        def ObDereferenceObject(a):
            return ObfDereferenceObjecta


        def ObReferenceObject(Object):
            return ObfReferenceObjectObject


        def ObDereferenceObjectWithTag(a, t):
            return ObfDereferenceObjectWithTaga, t


        def ObReferenceObjectWithTag(Object, Tag):
            return ObfReferenceObjectWithTagObject, Tag
    else:


        def ObDereferenceObject(a):
            return ObfDereferenceObjecta


        def ObReferenceObject(Object):
            return ObfReferenceObjectObject
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN2K:
        pass
    # END IF
    # Registration version for Vista SP1 and Windows Server 2007
    OB_FLT_REGISTRATION_VERSION_0100 = 0x0100

    # This value should be used by filters for registration
    OB_FLT_REGISTRATION_VERSION = OB_FLT_REGISTRATION_VERSION_0100
    OB_OPERATION = ULONG
    OB_OPERATION_HANDLE_CREATE = 0x00000001
    OB_OPERATION_HANDLE_DUPLICATE = 0x00000002
    class _OB_PRE_CREATE_HANDLE_INFORMATION(ctypes.Structure):
        pass


    _OB_PRE_CREATE_HANDLE_INFORMATION._fields_ = [
        ('ACCESS_MASK         DesiredAccess', _Inout_),
        ('OriginalDesiredAccess', ACCESS_MASK),
    ]
    OB_PRE_CREATE_HANDLE_INFORMATION = _OB_PRE_CREATE_HANDLE_INFORMATION
    POB_PRE_CREATE_HANDLE_INFORMATION = POINTER(_OB_PRE_CREATE_HANDLE_INFORMATION)
    class _OB_PRE_DUPLICATE_HANDLE_INFORMATION(ctypes.Structure):
        pass


    _OB_PRE_DUPLICATE_HANDLE_INFORMATION._fields_ = [
        ('ACCESS_MASK         DesiredAccess', _Inout_),
        ('OriginalDesiredAccess', ACCESS_MASK),
        ('SourceProcess', PVOID),
        ('TargetProcess', PVOID),
    ]
    OB_PRE_DUPLICATE_HANDLE_INFORMATION = _OB_PRE_DUPLICATE_HANDLE_INFORMATION
     POB_PRE_DUPLICATE_HANDLE_INFORMATION = POINTER(_OB_PRE_DUPLICATE_HANDLE_INFORMATION)
    class _OB_PRE_OPERATION_PARAMETERS(ctypes.Union):
        pass


    _OB_PRE_OPERATION_PARAMETERS._fields_ = [
        ('OB_PRE_CREATE_HANDLE_INFORMATION        CreateHandleInformation', _Inout_),
        ('OB_PRE_DUPLICATE_HANDLE_INFORMATION     DuplicateHandleInformation', _Inout_),
    ]
    OB_PRE_OPERATION_PARAMETERS = _OB_PRE_OPERATION_PARAMETERS
    POB_PRE_OPERATION_PARAMETERS = POINTER(_OB_PRE_OPERATION_PARAMETERS)
    class _OB_PRE_OPERATION_INFORMATION(ctypes.Structure):
        pass


    class _Struct_14(ctypes.Structure):
        pass


    class _Struct_15(ctypes.Structure):
        pass


    _Struct_15._fields_ = [
        ('KernelHandle', ULONG, 1),
        ('Reserved', ULONG, 31),
    ]
    _Struct_14._Struct_15 = _Struct_15
    _Struct_14._anonymous_ = (
        '_Struct_15',
    )
    _Struct_14._fields_ = [
        ('Flags', ULONG),
        ('_Struct_15', _Struct_14._Struct_15),
    ]
    _OB_PRE_OPERATION_INFORMATION._Struct_14 = _Struct_14
    _OB_PRE_OPERATION_INFORMATION._anonymous_ = (
        '_Struct_14',
    )
    _OB_PRE_OPERATION_INFORMATION._fields_ = [
        ('Operation', OB_OPERATION),
        ('_Struct_14', _OB_PRE_OPERATION_INFORMATION._Struct_14),
        ('Object', PVOID),
        ('ObjectType', POBJECT_TYPE),
        ('CallContext', PVOID),
        ('Parameters', POB_PRE_OPERATION_PARAMETERS),
    ]
    OB_PRE_OPERATION_INFORMATION = _OB_PRE_OPERATION_INFORMATION
    POB_PRE_OPERATION_INFORMATION = POINTER(_OB_PRE_OPERATION_INFORMATION)
    class _OB_POST_CREATE_HANDLE_INFORMATION(ctypes.Structure):
        pass


    _OB_POST_CREATE_HANDLE_INFORMATION._fields_ = [
        ('GrantedAccess', ACCESS_MASK),
    ]
    OB_POST_CREATE_HANDLE_INFORMATION = _OB_POST_CREATE_HANDLE_INFORMATION
    POB_POST_CREATE_HANDLE_INFORMATION = POINTER(_OB_POST_CREATE_HANDLE_INFORMATION)
    class _OB_POST_DUPLICATE_HANDLE_INFORMATION(ctypes.Structure):
        pass


    _OB_POST_DUPLICATE_HANDLE_INFORMATION._fields_ = [
        ('GrantedAccess', ACCESS_MASK),
    ]
    OB_POST_DUPLICATE_HANDLE_INFORMATION = _OB_POST_DUPLICATE_HANDLE_INFORMATION
     POB_POST_DUPLICATE_HANDLE_INFORMATION = POINTER(_OB_POST_DUPLICATE_HANDLE_INFORMATION)
    class _OB_POST_OPERATION_PARAMETERS(ctypes.Union):
        pass


    _OB_POST_OPERATION_PARAMETERS._fields_ = [
        ('CreateHandleInformation', OB_POST_CREATE_HANDLE_INFORMATION),
        ('DuplicateHandleInformation', OB_POST_DUPLICATE_HANDLE_INFORMATION),
    ]
    OB_POST_OPERATION_PARAMETERS = _OB_POST_OPERATION_PARAMETERS
    POB_POST_OPERATION_PARAMETERS = POINTER(_OB_POST_OPERATION_PARAMETERS)
    class _OB_POST_OPERATION_INFORMATION(ctypes.Structure):
        pass


    class _Struct_15(ctypes.Structure):
        pass


    class _Struct_16(ctypes.Structure):
        pass


    _Struct_16._fields_ = [
        ('KernelHandle', ULONG, 1),
        ('Reserved', ULONG, 31),
    ]
    _Struct_15._Struct_16 = _Struct_16
    _Struct_15._anonymous_ = (
        '_Struct_16',
    )
    _Struct_15._fields_ = [
        ('Flags', ULONG),
        ('_Struct_16', _Struct_15._Struct_16),
    ]
    _OB_POST_OPERATION_INFORMATION._Struct_15 = _Struct_15
    _OB_POST_OPERATION_INFORMATION._anonymous_ = (
        '_Struct_15',
    )
    _OB_POST_OPERATION_INFORMATION._fields_ = [
        ('Operation', OB_OPERATION),
        ('_Struct_15', _OB_POST_OPERATION_INFORMATION._Struct_15),
        ('Object', PVOID),
        ('ObjectType', POBJECT_TYPE),
        ('CallContext', PVOID),
        ('ReturnStatus', NTSTATUS),
        ('Parameters', POB_POST_OPERATION_PARAMETERS),
    ]
    OB_POST_OPERATION_INFORMATION = _OB_POST_OPERATION_INFORMATION
    POB_POST_OPERATION_INFORMATION = POINTER(_OB_POST_OPERATION_INFORMATION)


    class _OB_PREOP_CALLBACK_STATUS(ENUM):
        OB_PREOP_SUCCESS = 1


    OB_PREOP_CALLBACK_STATUS = _OB_PREOP_CALLBACK_STATUS
    POB_PREOP_CALLBACK_STATUS = POINTER(_OB_PREOP_CALLBACK_STATUS)
    class _OB_OPERATION_REGISTRATION(ctypes.Structure):
        pass


    _OB_OPERATION_REGISTRATION._fields_ = [
        ('ObjectType', POINTER(POBJECT_TYPE)),
        ('Operations', OB_OPERATION),
        ('PreOperation', POB_PRE_OPERATION_CALLBACK),
        ('PostOperation', POB_POST_OPERATION_CALLBACK),
    ]
    OB_OPERATION_REGISTRATION = _OB_OPERATION_REGISTRATION
    POB_OPERATION_REGISTRATION = POINTER(_OB_OPERATION_REGISTRATION)
    class _OB_CALLBACK_REGISTRATION(ctypes.Structure):
        pass


    _OB_CALLBACK_REGISTRATION._fields_ = [
        ('Version', USHORT),
        ('OperationRegistrationCount', USHORT),
        ('Altitude', UNICODE_STRING),
        ('RegistrationContext', PVOID),
        ('OperationRegistration', POINTER(OB_OPERATION_REGISTRATION)),
    ]
    OB_CALLBACK_REGISTRATION = _OB_CALLBACK_REGISTRATION
    POB_CALLBACK_REGISTRATION = POINTER(_OB_CALLBACK_REGISTRATION)
    if NTDDI_VERSION >= NTDDI_VISTASP1:

        # @[comment("MVI_tracked")]    # END IF
    if not defined(_PCI_X_):
        _PCI_X_ = 1

        # A PCI driver can read the complete 256 bytes of configuration
        # information for any PCI device by calling:
        # ULONG
        # HalGetBusData (
        # _In_ BUS_DATA_TYPE  PCIConfiguration,
        # _In_ ULONG   PciBusNumber,
        # _In_ PCI_SLOT_NUMBER VirtualSlotNumber,
        # _In_ PPCI_COMMON_CONFIG & PCIDeviceConfig,
        # _In_ ULONG   ctypes.sizeof (PCIDeviceConfig)
        # );
        # A return value of 0 means that the specified PCI bus does not exist.
        # A return value of 2, with a VendorID of PCI_INVALID_VENDORID means
        # that the PCI bus does exist, but there is no device at the specified
        # VirtualSlotNumber (PCI Device/Function number).
        class _PCI_SLOT_NUMBER(ctypes.Structure):
            pass


        class u(ctypes.Structure):
            pass


        class bits(ctypes.Structure):
            pass


        bits._fields_ = [
            ('DeviceNumber', ULONG, 5),
            ('FunctionNumber', ULONG, 3),
            ('Reserved', ULONG, 24),
        ]
        u.bits = bits
        u._fields_ = [
            ('bits', u.bits),
            ('AsULONG', ULONG),
        ]
        _PCI_SLOT_NUMBER.u = u
        _PCI_SLOT_NUMBER._fields_ = [
            ('u', _PCI_SLOT_NUMBER.u),
        ]
        PCI_SLOT_NUMBER = _PCI_SLOT_NUMBER
        PPCI_SLOT_NUMBER = POINTER(_PCI_SLOT_NUMBER)
        PCI_TYPE0_ADDRESSES = 6
        PCI_TYPE1_ADDRESSES = 2
        PCI_TYPE2_ADDRESSES = 5


        class _PCI_COMMON_HEADER(ctypes.Structure):
            pass


        class u(ctypes.Structure):
            pass


        class type0(ctypes.Structure):
            pass


        type0._fields_ = [
            ('BaseAddresses', ULONG * PCI_TYPE0_ADDRESSES),
            ('CIS', ULONG),
            ('SubVendorID', USHORT),
            ('SubSystemID', USHORT),
            ('ROMBaseAddress', ULONG),
            ('CapabilitiesPtr', UCHAR),
            ('Reserved1', UCHAR * 3),
            ('Reserved2', ULONG),
            ('InterruptLine', UCHAR),
            ('InterruptPin', UCHAR), # (ro)
            ('MinimumGrant', UCHAR), # (ro)
            ('MaximumLatency', UCHAR), # (ro)
        ]
        u.type0 = type0


        class type1(ctypes.Structure):
            pass


        type1._fields_ = [
            ('BaseAddresses', ULONG * PCI_TYPE1_ADDRESSES),
            ('PrimaryBus', UCHAR),
            ('SecondaryBus', UCHAR),
            ('SubordinateBus', UCHAR),
            ('SecondaryLatency', UCHAR),
            ('IOBase', UCHAR),
            ('IOLimit', UCHAR),
            ('SecondaryStatus', USHORT),
            ('MemoryBase', USHORT),
            ('MemoryLimit', USHORT),
            ('PrefetchBase', USHORT),
            ('PrefetchLimit', USHORT),
            ('PrefetchBaseUpper32', ULONG),
            ('PrefetchLimitUpper32', ULONG),
            ('IOBaseUpper16', USHORT),
            ('IOLimitUpper16', USHORT),
            ('CapabilitiesPtr', UCHAR),
            ('Reserved1', UCHAR * 3),
            ('ROMBaseAddress', ULONG),
            ('InterruptLine', UCHAR),
            ('InterruptPin', UCHAR),
            ('BridgeControl', USHORT),
        ]
        u.type1 = type1


        class type2(ctypes.Structure):
            pass


        type2.Range = Range
        type2._fields_ = [
            ('SocketRegistersBaseAddress', ULONG),
            ('CapabilitiesPtr', UCHAR),
            ('Reserved', UCHAR),
            ('SecondaryStatus', USHORT),
            ('PrimaryBus', UCHAR),
            ('SecondaryBus', UCHAR),
            ('SubordinateBus', UCHAR),
            ('SecondaryLatency', UCHAR),
            ('Range', type2.Range * PCI_TYPE2_ADDRESSES - 1),
            ('InterruptLine', UCHAR),
            ('InterruptPin', UCHAR),
            ('BridgeControl', USHORT),
        ]
        u.type2 = type2
        u._fields_ = [
            ('type0', u.type0),
            ('type1', u.type1), # PCI to PCI Bridge
            ('type2', u.type2), # PCI to CARDBUS Bridge
        ]
        _PCI_COMMON_HEADER.u = u
        _PCI_COMMON_HEADER._fields_ = [
            ('VendorID', USHORT), # (ro)
            ('DeviceID', USHORT), # (ro)
            ('Command', USHORT), # Device control
            ('Status', USHORT),
            ('RevisionID', UCHAR), # (ro)
            ('ProgIf', UCHAR), # (ro)
            ('SubClass', UCHAR), # (ro)
            ('BaseClass', UCHAR), # (ro)
            ('CacheLineSize', UCHAR), # (ro + )
            ('LatencyTimer', UCHAR), # (ro + )
            ('HeaderType', UCHAR), # (ro)
            ('BIST', UCHAR), # Built in self test
            ('u', _PCI_COMMON_HEADER.u),
        ]
        PCI_COMMON_HEADER = _PCI_COMMON_HEADER
        PPCI_COMMON_HEADER = POINTER(_PCI_COMMON_HEADER)

        if defined(__cplusplus):
            class _PCI_COMMON_CONFIG(ctypes.Structure):
                pass


            _PCI_COMMON_CONFIG._fields_ = [
                ('DUMMYSTRUCTNAME', PCI_COMMON_HEADER),
                ('DeviceSpecific', UCHAR * 192),
            ]
            PCI_COMMON_CONFIG = _PCI_COMMON_CONFIG
            PPCI_COMMON_CONFIG = POINTER(_PCI_COMMON_CONFIG)
        else:
            class _PCI_COMMON_CONFIG(ctypes.Structure):
                pass


            _PCI_COMMON_CONFIG._fields_ = [
                ('DUMMYSTRUCTNAME', PCI_COMMON_HEADER),
                ('DeviceSpecific', UCHAR * 192),
            ]
            PCI_COMMON_CONFIG = _PCI_COMMON_CONFIG
            PPCI_COMMON_CONFIG = POINTER(_PCI_COMMON_CONFIG)
        # END IF

        PCI_COMMON_HDR_LENGTH = (
            UFIELD_OFFSET (PCI_COMMON_CONFIG, PCI_COMMON_CONFIG.DeviceSpecific)
        )
        PCI_EXTENDED_CONFIG_LENGTH = 0x1000
        PCI_MAX_DEVICES = 32
        PCI_MAX_FUNCTION = 8
        PCI_MAX_BRIDGE_NUMBER = 0xFF
        PCI_INVALID_VENDORID = 0xFFFF

        # Bit encodings for PCI_COMMON_CONFIG.HeaderType
        PCI_MULTIFUNCTION = 0x80
        PCI_DEVICE_TYPE = 0x00
        PCI_BRIDGE_TYPE = 0x01
        PCI_CARDBUS_BRIDGE_TYPE = 0x02


        def PCI_CONFIGURATION_TYPE(PciData):
            return (
                ctypes.cast(PPCI_COMMON_CONFIG, PciData).HeaderType & ~PCI_MULTIFUNCTION
            )


        def PCI_MULTIFUNCTION_DEVICE(PciData):
            return (
                (
                    ctypes.cast(PPCI_COMMON_CONFIG, PciData).HeaderType &
                    PCI_MULTIFUNCTION
                ) != 0
            )

        # Bit encodings for PCI_COMMON_CONFIG.Command
        PCI_ENABLE_IO_SPACE = 0x0001
        PCI_ENABLE_MEMORY_SPACE = 0x0002
        PCI_ENABLE_BUS_MASTER = 0x0004
        PCI_ENABLE_SPECIAL_CYCLES = 0x0008
        PCI_ENABLE_WRITE_AND_INVALIDATE = 0x0010
        PCI_ENABLE_VGA_COMPATIBLE_PALETTE = 0x0020
        PCI_ENABLE_PARITY = 0x0040
        PCI_ENABLE_WAIT_CYCLE = 0x0080
        PCI_ENABLE_SERR = 0x0100
        PCI_ENABLE_FAST_BACK_TO_BACK = 0x0200
        PCI_DISABLE_LEVEL_INTERRUPT = 0x0400

        # Bit encodings for PCI_COMMON_CONFIG.Status
        PCI_STATUS_INTERRUPT_PENDING = 0x0008
        PCI_STATUS_CAPABILITIES_LIST = 0x0010
        PCI_STATUS_66MHZ_CAPABLE = 0x0020
        PCI_STATUS_UDF_SUPPORTED = 0x0040
        PCI_STATUS_FAST_BACK_TO_BACK = 0x0080
        PCI_STATUS_DATA_PARITY_DETECTED = 0x0100
        PCI_STATUS_DEVSEL = 0x0600
        PCI_STATUS_SIGNALED_TARGET_ABORT = 0x0800
        PCI_STATUS_RECEIVED_TARGET_ABORT = 0x1000
        PCI_STATUS_RECEIVED_MASTER_ABORT = 0x2000
        PCI_STATUS_SIGNALED_SYSTEM_ERROR = 0x4000
        PCI_STATUS_DETECTED_PARITY_ERROR = 0x8000

        # The NT PCI Driver uses a WhichSpace parameter on its
        # CONFIG_READ/WRITE
        # routines. The following values are defined -
        PCI_WHICHSPACE_CONFIG = 0x0
        PCI_WHICHSPACE_ROM = 0x52696350

        # PCI Capability IDs
        PCI_CAPABILITY_ID_POWER_MANAGEMENT = 0x01
        PCI_CAPABILITY_ID_AGP = 0x02
        PCI_CAPABILITY_ID_VPD = 0x03
        PCI_CAPABILITY_ID_SLOT_ID = 0x04
        PCI_CAPABILITY_ID_MSI = 0x05
        PCI_CAPABILITY_ID_CPCI_HOTSWAP = 0x06
        PCI_CAPABILITY_ID_PCIX = 0x07
        PCI_CAPABILITY_ID_HYPERTRANSPORT = 0x08
        PCI_CAPABILITY_ID_VENDOR_SPECIFIC = 0x09
        PCI_CAPABILITY_ID_DEBUG_PORT = 0x0A
        PCI_CAPABILITY_ID_CPCI_RES_CTRL = 0x0B
        PCI_CAPABILITY_ID_SHPC = 0x0C
        PCI_CAPABILITY_ID_P2P_SSID = 0x0D
        PCI_CAPABILITY_ID_AGP_TARGET = 0x0E
        PCI_CAPABILITY_ID_SECURE = 0x0F
        PCI_CAPABILITY_ID_PCI_EXPRESS = 0x10
        PCI_CAPABILITY_ID_MSIX = 0x11
        PCI_CAPABILITY_ID_SATA_CONFIG = 0x12
        PCI_CAPABILITY_ID_ADVANCED_FEATURES = 0x13

        # All PCI Capability structures have the following header.
        # CapabilityID is used to identify the type of the structure (is
        # one of the PCI_CAPABILITY_ID values above.
        # Next is the offset in PCI Configuration space (0x40 - 0xfc) of the
        # next capability structure in the list, or 0x00 if there are no more
        # entries.
        class _PCI_CAPABILITIES_HEADER(ctypes.Structure):
            pass


        _PCI_CAPABILITIES_HEADER._fields_ = [
            ('CapabilityID', UCHAR),
            ('Next', UCHAR),
        ]
        PCI_CAPABILITIES_HEADER = _PCI_CAPABILITIES_HEADER
        PPCI_CAPABILITIES_HEADER = POINTER(_PCI_CAPABILITIES_HEADER)

        # Power Management Capability
        class _PCI_PMC(ctypes.Structure):
            pass


        class Support(ctypes.Structure):
            pass


        Support._fields_ = [
            ('Rsvd2', UCHAR, 1),
            ('D1', UCHAR, 1),
            ('D2', UCHAR, 1),
            ('PMED0', UCHAR, 1),
            ('PMED1', UCHAR, 1),
            ('PMED2', UCHAR, 1),
            ('PMED3Hot', UCHAR, 1),
            ('PMED3Cold', UCHAR, 1),
        ]
        _PCI_PMC.Support = Support
        _PCI_PMC._fields_ = [
            ('Version', UCHAR, 3),
            ('PMEClock', UCHAR, 1),
            ('Rsvd1', UCHAR, 1),
            ('DeviceSpecificInitialization', UCHAR, 1),
            ('Rsvd2', UCHAR, 2),
            ('Support', _PCI_PMC.Support),
        ]
        PCI_PMC = _PCI_PMC
        PPCI_PMC = POINTER(_PCI_PMC)


        class _PCI_PMCSR(ctypes.Structure):
            pass


        _PCI_PMCSR._fields_ = [
            ('PowerState', USHORT, 2),
            ('Rsvd1', USHORT, 1),
            ('NoSoftReset', USHORT, 1),
            ('Rsvd2', USHORT, 4),
            ('PMEEnable', USHORT, 1),
            ('DataSelect', USHORT, 4),
            ('DataScale', USHORT, 2),
            ('PMEStatus', USHORT, 1),
        ]
        PCI_PMCSR = _PCI_PMCSR
        PPCI_PMCSR = POINTER(_PCI_PMCSR)


        class _PCI_PMCSR_BSE(ctypes.Structure):
            pass


        _PCI_PMCSR_BSE._fields_ = [
            ('Rsvd1', UCHAR, 6),
            ('D3HotSupportsStopClock', UCHAR, 1), # B2_B3
            ('BusPowerClockControlEnabled', UCHAR, 1), # BPCC_EN
        ]
        PCI_PMCSR_BSE = _PCI_PMCSR_BSE
        PPCI_PMCSR_BSE = POINTER(_PCI_PMCSR_BSE)


        class _PCI_PM_CAPABILITY(ctypes.Structure):
            pass


        class PMC(ctypes.Union):
            pass


        PMC._fields_ = [
            ('Capabilities', PCI_PMC),
            ('AsUSHORT', USHORT),
        ]
        _PCI_PM_CAPABILITY.PMC = PMC


        class PMCSR(ctypes.Union):
            pass


        PMCSR._fields_ = [
            ('ControlStatus', PCI_PMCSR),
            ('AsUSHORT', USHORT),
        ]
        _PCI_PM_CAPABILITY.PMCSR = PMCSR


        class PMCSR_BSE(ctypes.Union):
            pass


        PMCSR_BSE._fields_ = [
            ('BridgeSupport', PCI_PMCSR_BSE),
            ('AsUCHAR', UCHAR),
        ]
        _PCI_PM_CAPABILITY.PMCSR_BSE = PMCSR_BSE
        _PCI_PM_CAPABILITY._fields_ = [
            ('Header', PCI_CAPABILITIES_HEADER),
            ('PMC', _PCI_PM_CAPABILITY.PMC), # Power Management Capabilities (Offset = 2)
            ('PMCSR', _PCI_PM_CAPABILITY.PMCSR), # Power Management Control/Status (Offset = 4)
            ('PMCSR_BSE', _PCI_PM_CAPABILITY.PMCSR_BSE), # PMCSR PCI - PCI Bridge Support Extensions
            ('Data', UCHAR), # DataSelect and DataScale in ControlStatus.
        ]
        PCI_PM_CAPABILITY = _PCI_PM_CAPABILITY
        PPCI_PM_CAPABILITY = POINTER(_PCI_PM_CAPABILITY)

        # PCI - X Capability
        class PCI_X_CAPABILITY(ctypes.Structure):
            pass


        class Command(ctypes.Structure):
            pass


        class bits(ctypes.Structure):
            pass


        bits._fields_ = [
            ('DataParityErrorRecoveryEnable', USHORT, 1),
            ('EnableRelaxedOrdering', USHORT, 1),
            ('MaxMemoryReadByteCount', USHORT, 2),
            ('MaxOutstandingSplitTransactions', USHORT, 3),
            ('Reserved', USHORT, 9),
        ]
        Command.bits = bits
        Command._fields_ = [
            ('bits', Command.bits),
            ('AsUSHORT', USHORT),
        ]
        PCI_X_CAPABILITY.Command = Command


        class Status(ctypes.Structure):
            pass


        class bits(ctypes.Structure):
            pass


        bits._fields_ = [
            ('FunctionNumber', ULONG, 3),
            ('DeviceNumber', ULONG, 5),
            ('BusNumber', ULONG, 8),
            ('Device64Bit', ULONG, 1),
            ('Capable133MHz', ULONG, 1),
            ('SplitCompletionDiscarded', ULONG, 1),
            ('UnexpectedSplitCompletion', ULONG, 1),
            ('DeviceComplexity', ULONG, 1),
            ('DeINTMaxMemoryReadByteCount', ULONG, 2),
            ('DeINTMaxOutstandingSplitTransactions', ULONG, 3),
            ('DeINTMaxCumulativeReadSize', ULONG, 3),
            ('ReceivedSplitCompletionErrorMessage', ULONG, 1),
            ('CapablePCIX266', ULONG, 1),
            ('CapablePCIX533', ULONG, 1),
        ]
        Status.bits = bits
        Status._fields_ = [
            ('bits', Status.bits),
            ('AsULONG', ULONG),
        ]
        PCI_X_CAPABILITY.Status = Status
        PCI_X_CAPABILITY._fields_ = [
            ('Header', PCI_CAPABILITIES_HEADER),
            ('Command', PCI_X_CAPABILITY.Command),
            ('Status', PCI_X_CAPABILITY.Status),
        ]
        PPCI_X_CAPABILITY = POINTER(PCI_X_CAPABILITY)

        # PCI Express Extended Capabilities.
        PCI_EXPRESS_ADVANCED_ERROR_REPORTING_CAP_ID = 0x0001
        PCI_EXPRESS_VIRTUAL_CHANNEL_CAP_ID = 0x0002
        PCI_EXPRESS_DEVICE_SERIAL_NUMBER_CAP_ID = 0x0003
        PCI_EXPRESS_POWER_BUDGETING_CAP_ID = 0x0004
        PCI_EXPRESS_RC_LINK_DECLARATION_CAP_ID = 0x0005
        PCI_EXPRESS_RC_INTERNAL_LINK_CONTROL_CAP_ID = 0x0006
        PCI_EXPRESS_RC_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION_CAP_ID = 0x0007
        PCI_EXPRESS_MFVC_CAP_ID = 0x0008
        PCI_EXPRESS_VC_AND_MFVC_CAP_ID = 0x0009
        PCI_EXPRESS_RCRB_HEADER_CAP_ID = 0x000A
        PCI_EXPRESS_VENDOR_SPECIFIC_CAP_ID = 0x000B
        PCI_EXPRESS_CONFIGURATION_ACCESS_CORRELATION_CAP_ID = 0x000C
        PCI_EXPRESS_ACCESS_CONTROL_SERVICES_CAP_ID = 0x000D
        PCI_EXPRESS_ARI_CAP_ID = 0x000E
        PCI_EXPRESS_ATS_CAP_ID = 0x000F
        PCI_EXPRESS_SINGLE_ROOT_IO_VIRTUALIZATION_CAP_ID = 0x0010
        PCI_EXPRESS_MULTI_ROOT_IO_VIRTUALIZATION_CAP_ID = 0x0011
        PCI_EXPRESS_MULTICAST_CAP_ID = 0x0012
        PCI_EXPRESS_PAGE_REQUEST_CAP_ID = 0x0013
        PCI_EXPRESS_RESERVED_FOR_AMD_CAP_ID = 0x0014
        PCI_EXPRESS_RESIZABLE_BAR_CAP_ID = 0x0015
        PCI_EXPRESS_DPA_CAP_ID = 0x0016
        PCI_EXPRESS_TPH_REQUESTER_CAP_ID = 0x0017
        PCI_EXPRESS_LTR_CAP_ID = 0x0018
        PCI_EXPRESS_SECONDARY_PCI_EXPRESS_CAP_ID = 0x0019
        PCI_EXPRESS_PMUX_CAP_ID = 0x001A
        PCI_EXPRESS_PASID_CAP_ID = 0x001B
        PCI_EXPRESS_LN_REQUESTER_CAP_ID = 0x001C
        PCI_EXPRESS_DPC_CAP_ID = 0x001D
        PCI_EXPRESS_L1_PM_SS_CAP_ID = 0x001E
        PCI_EXPRESS_PTM_CAP_ID = 0x001F
        PCI_EXPRESS_MPCIE_CAP_ID = 0x0020
        PCI_EXPRESS_FRS_QUEUEING_CAP_ID = 0x0021
        PCI_EXPRESS_READINESS_TIME_REPORTING_CAP_ID = 0x0022
        PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_CAP_ID = 0x0023

        # All Enhanced capabilities have the following header.
        class _PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER(ctypes.Structure):
            pass


        _PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER._fields_ = [
            ('CapabilityID', USHORT),
            ('Version', USHORT, 4),
            ('Next', USHORT, 12),
        ]
        PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER = _PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER
        PPCI_EXPRESS_ENHANCED_CAPABILITY_HEADER = POINTER(_PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER)

        # Vendor Specific Capability
        class _PCI_EXPRESS_VENDOR_SPECIFIC_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_VENDOR_SPECIFIC_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('VsecId', USHORT),
            ('VsecRev', USHORT, 4),
            ('VsecLength', USHORT, 12),
        ]
        PCI_EXPRESS_VENDOR_SPECIFIC_CAPABILITY = _PCI_EXPRESS_VENDOR_SPECIFIC_CAPABILITY
        PPCI_EXPRESS_VENDOR_SPECIFIC_CAPABILITY = POINTER(_PCI_EXPRESS_VENDOR_SPECIFIC_CAPABILITY)

        # Serial Number Capability.
        class _PCI_EXPRESS_SERIAL_NUMBER_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_SERIAL_NUMBER_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('LowSerialNumber', ULONG),
            ('HighSerialNumber', ULONG),
        ]
        PCI_EXPRESS_SERIAL_NUMBER_CAPABILITY = _PCI_EXPRESS_SERIAL_NUMBER_CAPABILITY
        PPCI_EXPRESS_SERIAL_NUMBER_CAPABILITY = POINTER(_PCI_EXPRESS_SERIAL_NUMBER_CAPABILITY)

        # ARI Capability structures
        class _PCI_EXPRESS_ARI_CAPABILITY_REGISTER(ctypes.Structure):
            pass


        _PCI_EXPRESS_ARI_CAPABILITY_REGISTER._fields_ = [
            ('MfvcFunctionGroupsCapability', USHORT, 1),
            ('AcsFunctionGroupsCapability', USHORT, 1),
            ('Reserved', USHORT, 6),
            ('NextFunctionNumber', USHORT, 8),
        ]
        PCI_EXPRESS_ARI_CAPABILITY_REGISTER = _PCI_EXPRESS_ARI_CAPABILITY_REGISTER
        PPCI_EXPRESS_ARI_CAPABILITY_REGISTER = POINTER(_PCI_EXPRESS_ARI_CAPABILITY_REGISTER)


        class _PCI_EXPRESS_ARI_CONTROL_REGISTER(ctypes.Structure):
            pass


        _PCI_EXPRESS_ARI_CONTROL_REGISTER._fields_ = [
            ('MfvcFunctionGroupsEnable', USHORT, 1),
            ('AcsFunctionGroupsEnable', USHORT, 1),
            ('Reserved1', USHORT, 2),
            ('FunctionGroup', USHORT, 3),
            ('Reserved2', USHORT, 9),
        ]
        PCI_EXPRESS_ARI_CONTROL_REGISTER = _PCI_EXPRESS_ARI_CONTROL_REGISTER
        PPCI_EXPRESS_ARI_CONTROL_REGISTER = POINTER(_PCI_EXPRESS_ARI_CONTROL_REGISTER)


        class _PCI_EXPRESS_ARI_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_ARI_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('Capability', PCI_EXPRESS_ARI_CAPABILITY_REGISTER),
            ('Control', PCI_EXPRESS_ARI_CONTROL_REGISTER),
        ]
        PCI_EXPRESS_ARI_CAPABILITY = _PCI_EXPRESS_ARI_CAPABILITY
        PPCI_EXPRESS_ARI_CAPABILITY = POINTER(_PCI_EXPRESS_ARI_CAPABILITY)

        # Virtual Channel (VC) Capability structures
        class _VIRTUAL_CHANNEL_CAPABILITIES1(ctypes.Union):
            pass


        class _Struct_16(ctypes.Structure):
            pass


        _Struct_16._fields_ = [
            ('ExtendedVCCount', ULONG, 3),
            ('RsvdP1', ULONG, 1),
            ('LowPriorityExtendedVCCount', ULONG, 3),
            ('RsvdP2', ULONG, 1),
            ('ReferenceClock', ULONG, 2),
            ('PortArbitrationTableEntrySize', ULONG, 2),
            ('RsvdP3', ULONG, 20),
        ]
        _VIRTUAL_CHANNEL_CAPABILITIES1._Struct_16 = _Struct_16
        _VIRTUAL_CHANNEL_CAPABILITIES1._anonymous_ = (
            '_Struct_16',
        )
        _VIRTUAL_CHANNEL_CAPABILITIES1._fields_ = [
            ('_Struct_16', _VIRTUAL_CHANNEL_CAPABILITIES1._Struct_16),
            ('AsULONG', ULONG),
        ]
        VIRTUAL_CHANNEL_CAPABILITIES1 = _VIRTUAL_CHANNEL_CAPABILITIES1
        PVIRTUAL_CHANNEL_CAPABILITIES1 = POINTER(_VIRTUAL_CHANNEL_CAPABILITIES1)


        class _VIRTUAL_CHANNEL_CAPABILITIES2(ctypes.Union):
            pass


        class _Struct_17(ctypes.Structure):
            pass


        _Struct_17._fields_ = [
            ('VCArbitrationCapability', ULONG, 8),
            ('RsvdP', ULONG, 16),
            ('VCArbitrationTableOffset', ULONG, 8),
        ]
        _VIRTUAL_CHANNEL_CAPABILITIES2._Struct_17 = _Struct_17
        _VIRTUAL_CHANNEL_CAPABILITIES2._anonymous_ = (
            '_Struct_17',
        )
        _VIRTUAL_CHANNEL_CAPABILITIES2._fields_ = [
            ('_Struct_17', _VIRTUAL_CHANNEL_CAPABILITIES2._Struct_17),
            ('AsULONG', ULONG),
        ]
        VIRTUAL_CHANNEL_CAPABILITIES2 = _VIRTUAL_CHANNEL_CAPABILITIES2
        PVIRTUAL_CHANNEL_CAPABILITIES2 = POINTER(_VIRTUAL_CHANNEL_CAPABILITIES2)


        class _VIRTUAL_CHANNEL_CONTROL(ctypes.Union):
            pass


        class _Struct_18(ctypes.Structure):
            pass


        _Struct_18._fields_ = [
            ('LoadVCArbitrationTable', USHORT, 1),
            ('VCArbitrationSelect', USHORT, 3),
            ('RsvdP', USHORT, 12),
        ]
        _VIRTUAL_CHANNEL_CONTROL._Struct_18 = _Struct_18
        _VIRTUAL_CHANNEL_CONTROL._anonymous_ = (
            '_Struct_18',
        )
        _VIRTUAL_CHANNEL_CONTROL._fields_ = [
            ('_Struct_18', _VIRTUAL_CHANNEL_CONTROL._Struct_18),
            ('AsUSHORT', USHORT),
        ]
        VIRTUAL_CHANNEL_CONTROL = _VIRTUAL_CHANNEL_CONTROL
        PVIRTUAL_CHANNEL_CONTROL = POINTER(_VIRTUAL_CHANNEL_CONTROL)


        class _VIRTUAL_CHANNEL_STATUS(ctypes.Union):
            pass


        class _Struct_19(ctypes.Structure):
            pass


        _Struct_19._fields_ = [
            ('VCArbitrationTableStatus', USHORT, 1),
            ('RsvdZ', USHORT, 15),
        ]
        _VIRTUAL_CHANNEL_STATUS._Struct_19 = _Struct_19
        _VIRTUAL_CHANNEL_STATUS._anonymous_ = (
            '_Struct_19',
        )
        _VIRTUAL_CHANNEL_STATUS._fields_ = [
            ('_Struct_19', _VIRTUAL_CHANNEL_STATUS._Struct_19),
            ('AsUSHORT', USHORT),
        ]
        VIRTUAL_CHANNEL_STATUS = _VIRTUAL_CHANNEL_STATUS
        PVIRTUAL_CHANNEL_STATUS = POINTER(_VIRTUAL_CHANNEL_STATUS)


        class _VIRTUAL_RESOURCE_CAPABILITY(ctypes.Union):
            pass


        class _Struct_20(ctypes.Structure):
            pass


        _Struct_20._fields_ = [
            ('PortArbitrationCapability', ULONG, 8),
            ('RsvdP1', ULONG, 6),
            ('Undefined', ULONG, 1),
            ('RejectSnoopTransactions', ULONG, 1),
            ('MaximumTimeSlots', ULONG, 7),
            ('RsvdP2', ULONG, 1),
            ('PortArbitrationTableOffset', ULONG, 8),
        ]
        _VIRTUAL_RESOURCE_CAPABILITY._Struct_20 = _Struct_20
        _VIRTUAL_RESOURCE_CAPABILITY._anonymous_ = (
            '_Struct_20',
        )
        _VIRTUAL_RESOURCE_CAPABILITY._fields_ = [
            ('_Struct_20', _VIRTUAL_RESOURCE_CAPABILITY._Struct_20),
            ('AsULONG', ULONG),
        ]
        VIRTUAL_RESOURCE_CAPABILITY = _VIRTUAL_RESOURCE_CAPABILITY
        PVIRTUAL_RESOURCE_CAPABILITY = POINTER(_VIRTUAL_RESOURCE_CAPABILITY)


        class _VIRTUAL_RESOURCE_CONTROL(ctypes.Union):
            pass


        class _Struct_21(ctypes.Structure):
            pass


        _Struct_21._fields_ = [
            ('TcVcMap', ULONG, 8),
            ('RsvdP1', ULONG, 8),
            ('LoadPortArbitrationTable', ULONG, 1),
            ('PortArbitrationSelect', ULONG, 3),
            ('RsvdP2', ULONG, 4),
            ('VcID', ULONG, 3),
            ('RsvdP3', ULONG, 4),
            ('VcEnable', ULONG, 1),
        ]
        _VIRTUAL_RESOURCE_CONTROL._Struct_21 = _Struct_21
        _VIRTUAL_RESOURCE_CONTROL._anonymous_ = (
            '_Struct_21',
        )
        _VIRTUAL_RESOURCE_CONTROL._fields_ = [
            ('_Struct_21', _VIRTUAL_RESOURCE_CONTROL._Struct_21),
            ('AsULONG', ULONG),
        ]
        VIRTUAL_RESOURCE_CONTROL = _VIRTUAL_RESOURCE_CONTROL
        PVIRTUAL_RESOURCE_CONTROL = POINTER(_VIRTUAL_RESOURCE_CONTROL)


        class _VIRTUAL_RESOURCE_STATUS(ctypes.Union):
            pass


        class _Struct_22(ctypes.Structure):
            pass


        _Struct_22._fields_ = [
            ('PortArbitrationTableStatus', USHORT, 1),
            ('VcNegotiationPending', USHORT, 1),
            ('RsvdZ', USHORT, 14),
        ]
        _VIRTUAL_RESOURCE_STATUS._Struct_22 = _Struct_22
        _VIRTUAL_RESOURCE_STATUS._anonymous_ = (
            '_Struct_22',
        )
        _VIRTUAL_RESOURCE_STATUS._fields_ = [
            ('_Struct_22', _VIRTUAL_RESOURCE_STATUS._Struct_22),
            ('AsUSHORT', USHORT),
        ]
        VIRTUAL_RESOURCE_STATUS = _VIRTUAL_RESOURCE_STATUS
        PVIRTUAL_RESOURCE_STATUS = POINTER(_VIRTUAL_RESOURCE_STATUS)


        class _VIRTUAL_RESOURCE(ctypes.Structure):
            pass


        _VIRTUAL_RESOURCE._fields_ = [
            ('Capability', VIRTUAL_RESOURCE_CAPABILITY),
            ('Control', VIRTUAL_RESOURCE_CONTROL),
            ('RsvdP', USHORT),
            ('Status', VIRTUAL_RESOURCE_STATUS),
        ]
        VIRTUAL_RESOURCE = _VIRTUAL_RESOURCE
        PVIRTUAL_RESOURCE = POINTER(_VIRTUAL_RESOURCE)


        class _PCI_EXPRESS_VIRTUAL_CHANNEL_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_VIRTUAL_CHANNEL_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('Capabilities1', VIRTUAL_CHANNEL_CAPABILITIES1),
            ('Capabilities2', VIRTUAL_CHANNEL_CAPABILITIES2),
            ('Control', VIRTUAL_CHANNEL_CONTROL),
            ('Status', VIRTUAL_CHANNEL_STATUS),
            ('Resource', VIRTUAL_RESOURCE * 8),
        ]
        PCI_EXPRESS_VIRTUAL_CHANNEL_CAPABILITY = _PCI_EXPRESS_VIRTUAL_CHANNEL_CAPABILITY
        PPCI_EXPRESS_VIRTUAL_CHANNEL_CAPABILITY = POINTER(_PCI_EXPRESS_VIRTUAL_CHANNEL_CAPABILITY)

        # ATS Capability structures
        class _PCI_EXPRESS_ATS_CAPABILITY_REGISTER(ctypes.Structure):
            pass


        _PCI_EXPRESS_ATS_CAPABILITY_REGISTER._fields_ = [
            ('InvalidateQueueDepth', USHORT, 5),
            ('PageAlignedRequest', USHORT, 1),
            ('GlobalInvalidateSupported', USHORT, 1),
            ('Reserved', USHORT, 9),
        ]
        PCI_EXPRESS_ATS_CAPABILITY_REGISTER = _PCI_EXPRESS_ATS_CAPABILITY_REGISTER
        PPCI_EXPRESS_ATS_CAPABILITY_REGISTER = POINTER(_PCI_EXPRESS_ATS_CAPABILITY_REGISTER)


        class _PCI_EXPRESS_ATS_CONTROL_REGISTER(ctypes.Structure):
            pass


        _PCI_EXPRESS_ATS_CONTROL_REGISTER._fields_ = [
            ('SmallestTransactionUnit', USHORT, 5),
            ('Reserved', USHORT, 10),
            ('Enable', USHORT, 1),
        ]
        PCI_EXPRESS_ATS_CONTROL_REGISTER = _PCI_EXPRESS_ATS_CONTROL_REGISTER
        PPCI_EXPRESS_ATS_CONTROL_REGISTER = POINTER(_PCI_EXPRESS_ATS_CONTROL_REGISTER)


        class _PCI_EXPRESS_ATS_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_ATS_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('Capability', PCI_EXPRESS_ATS_CAPABILITY_REGISTER),
            ('Control', PCI_EXPRESS_ATS_CONTROL_REGISTER),
        ]
        PCI_EXPRESS_ATS_CAPABILITY = _PCI_EXPRESS_ATS_CAPABILITY
        PPCI_EXPRESS_ATS_CAPABILITY = POINTER(_PCI_EXPRESS_ATS_CAPABILITY)

        # PASID Extended Capability Structure
        class _PCI_EXPRESS_PASID_CAPABILITY_REGISTER(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('Rsvd', USHORT, 1),
            ('ExecutePermissionSupported', USHORT, 1),
            ('PrivilegedModeSupported', USHORT, 1),
            ('Rsvd2', USHORT, 5),
            ('MaxPASIDWidth', USHORT, 5),
            ('Rsvd3', USHORT, 3),
        ]
        _PCI_EXPRESS_PASID_CAPABILITY_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_PASID_CAPABILITY_REGISTER._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_PASID_CAPABILITY_REGISTER.DUMMYSTRUCTNAME),
            ('AsUSHORT', USHORT),
        ]
        PCI_EXPRESS_PASID_CAPABILITY_REGISTER = _PCI_EXPRESS_PASID_CAPABILITY_REGISTER
        PPCI_EXPRESS_PASID_CAPABILITY_REGISTER = POINTER(_PCI_EXPRESS_PASID_CAPABILITY_REGISTER)


        class _PCI_EXPRESS_PASID_CONTROL_REGISTER(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('PASIDEnable', USHORT, 1),
            ('ExecutePermissionEnable', USHORT, 1),
            ('PrivilegedModeEnable', USHORT, 1),
            ('Rsvd', USHORT, 13),
        ]
        _PCI_EXPRESS_PASID_CONTROL_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_PASID_CONTROL_REGISTER._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_PASID_CONTROL_REGISTER.DUMMYSTRUCTNAME),
            ('AsUSHORT', USHORT),
        ]
        PCI_EXPRESS_PASID_CONTROL_REGISTER = _PCI_EXPRESS_PASID_CONTROL_REGISTER
        PPCI_EXPRESS_PASID_CONTROL_REGISTER = POINTER(_PCI_EXPRESS_PASID_CONTROL_REGISTER)


        class _PCI_EXPRESS_PASID_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_PASID_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('Capability', PCI_EXPRESS_PASID_CAPABILITY_REGISTER),
            ('Control', PCI_EXPRESS_PASID_CONTROL_REGISTER),
        ]
        PCI_EXPRESS_PASID_CAPABILITY = _PCI_EXPRESS_PASID_CAPABILITY
        PPCI_EXPRESS_PASID_CAPABILITY = POINTER(_PCI_EXPRESS_PASID_CAPABILITY)

        # PRI Extended Capability Structure
        class _PCI_EXPRESS_PRI_STATUS_REGISTER(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('ResponseFailure', USHORT, 1),
            ('UnexpectedPageRequestGroupIndex', USHORT, 1),
            ('Rsvd', USHORT, 6),
            ('Stopped', USHORT, 1),
            ('Rsvd2', USHORT, 6),
            ('PrgResponsePasidRequired', USHORT, 1),
        ]
        _PCI_EXPRESS_PRI_STATUS_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_PRI_STATUS_REGISTER._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_PRI_STATUS_REGISTER.DUMMYSTRUCTNAME),
            ('AsUSHORT', USHORT),
        ]
        PCI_EXPRESS_PRI_STATUS_REGISTER = _PCI_EXPRESS_PRI_STATUS_REGISTER
        PPCI_EXPRESS_PRI_STATUS_REGISTER = POINTER(_PCI_EXPRESS_PRI_STATUS_REGISTER)


        class _PCI_EXPRESS_PRI_CONTROL_REGISTER(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('Enable', USHORT, 1),
            ('Reset', USHORT, 1),
            ('Rsvd', USHORT, 14),
        ]
        _PCI_EXPRESS_PRI_CONTROL_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_PRI_CONTROL_REGISTER._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_PRI_CONTROL_REGISTER.DUMMYSTRUCTNAME),
            ('AsUSHORT', USHORT),
        ]
        PCI_EXPRESS_PRI_CONTROL_REGISTER = _PCI_EXPRESS_PRI_CONTROL_REGISTER
        PPCI_EXPRESS_PRI_CONTROL_REGISTER = POINTER(_PCI_EXPRESS_PRI_CONTROL_REGISTER)


        class _PCI_EXPRESS_PRI_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_PRI_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('Control', PCI_EXPRESS_PRI_CONTROL_REGISTER),
            ('Status', PCI_EXPRESS_PRI_STATUS_REGISTER),
            ('PRCapacity', ULONG),
            ('PRAllocation', ULONG),
        ]
        PCI_EXPRESS_PRI_CAPABILITY = _PCI_EXPRESS_PRI_CAPABILITY
        PPCI_EXPRESS_PRI_CAPABILITY = POINTER(_PCI_EXPRESS_PRI_CAPABILITY)

        # PCI Express Advanced Error Reporting structures.
        class _PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('Undefined', ULONG, 1),
            ('Reserved1', ULONG, 3),
            ('DataLinkProtocolError', ULONG, 1),
            ('SurpriseDownError', ULONG, 1),
            ('Reserved2', ULONG, 6),
            ('PoisonedTLP', ULONG, 1),
            ('FlowControlProtocolError', ULONG, 1),
            ('CompletionTimeout', ULONG, 1),
            ('CompleterAbort', ULONG, 1),
            ('UnexpectedCompletion', ULONG, 1),
            ('ReceiverOverflow', ULONG, 1),
            ('MalformedTLP', ULONG, 1),
            ('ECRCError', ULONG, 1),
            ('UnsupportedRequestError', ULONG, 1),
            ('AcsViolation', ULONG, 1),
            ('UncorrectableInternalError', ULONG, 1),
            ('MCBlockedTlp', ULONG, 1),
            ('AtomicOpEgressBlocked', ULONG, 1),
            ('TlpPrefixBlocked', ULONG, 1),
            ('Reserved3', ULONG, 6),
        ]
        _PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS = _PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS
        PPCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS = POINTER(_PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS)


        class _PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('Undefined', ULONG, 1),
            ('Reserved1', ULONG, 3),
            ('DataLinkProtocolError', ULONG, 1),
            ('SurpriseDownError', ULONG, 1),
            ('Reserved2', ULONG, 6),
            ('PoisonedTLP', ULONG, 1),
            ('FlowControlProtocolError', ULONG, 1),
            ('CompletionTimeout', ULONG, 1),
            ('CompleterAbort', ULONG, 1),
            ('UnexpectedCompletion', ULONG, 1),
            ('ReceiverOverflow', ULONG, 1),
            ('MalformedTLP', ULONG, 1),
            ('ECRCError', ULONG, 1),
            ('UnsupportedRequestError', ULONG, 1),
            ('AcsViolation', ULONG, 1),
            ('UncorrectableInternalError', ULONG, 1),
            ('MCBlockedTlp', ULONG, 1),
            ('AtomicOpEgressBlocked', ULONG, 1),
            ('TlpPrefixBlocked', ULONG, 1),
            ('Reserved3', ULONG, 6),
        ]
        _PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK = _PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK
        PPCI_EXPRESS_UNCORRECTABLE_ERROR_MASK = POINTER(_PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK)


        class _PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('Undefined', ULONG, 1),
            ('Reserved1', ULONG, 3),
            ('DataLinkProtocolError', ULONG, 1),
            ('SurpriseDownError', ULONG, 1),
            ('Reserved2', ULONG, 6),
            ('PoisonedTLP', ULONG, 1),
            ('FlowControlProtocolError', ULONG, 1),
            ('CompletionTimeout', ULONG, 1),
            ('CompleterAbort', ULONG, 1),
            ('UnexpectedCompletion', ULONG, 1),
            ('ReceiverOverflow', ULONG, 1),
            ('MalformedTLP', ULONG, 1),
            ('ECRCError', ULONG, 1),
            ('UnsupportedRequestError', ULONG, 1),
            ('AcsViolation', ULONG, 1),
            ('UncorrectableInternalError', ULONG, 1),
            ('MCBlockedTlp', ULONG, 1),
            ('AtomicOpEgressBlocked', ULONG, 1),
            ('TlpPrefixBlocked', ULONG, 1),
            ('Reserved3', ULONG, 6),
        ]
        _PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY = _PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY
        PPCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY = POINTER(_PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY)


        class _PCI_EXPRESS_CORRECTABLE_ERROR_STATUS(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('ReceiverError', ULONG, 1),
            ('Reserved1', ULONG, 5),
            ('BadTLP', ULONG, 1),
            ('BadDLLP', ULONG, 1),
            ('ReplayNumRollover', ULONG, 1),
            ('Reserved2', ULONG, 3),
            ('ReplayTimerTimeout', ULONG, 1),
            ('AdvisoryNonFatalError', ULONG, 1),
            ('CorrectedInternalError', ULONG, 1),
            ('HeaderLogOverflow', ULONG, 1),
            ('Reserved3', ULONG, 16),
        ]
        _PCI_EXPRESS_CORRECTABLE_ERROR_STATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_CORRECTABLE_ERROR_STATUS._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_CORRECTABLE_ERROR_STATUS.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_CORRECTABLE_ERROR_STATUS = _PCI_EXPRESS_CORRECTABLE_ERROR_STATUS
        PPCI_CORRECTABLE_ERROR_STATUS = POINTER(_PCI_EXPRESS_CORRECTABLE_ERROR_STATUS)


        class _PCI_EXPRESS_CORRECTABLE_ERROR_MASK(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('ReceiverError', ULONG, 1),
            ('Reserved1', ULONG, 5),
            ('BadTLP', ULONG, 1),
            ('BadDLLP', ULONG, 1),
            ('ReplayNumRollover', ULONG, 1),
            ('Reserved2', ULONG, 3),
            ('ReplayTimerTimeout', ULONG, 1),
            ('AdvisoryNonFatalError', ULONG, 1),
            ('CorrectedInternalError', ULONG, 1),
            ('HeaderLogOverflow', ULONG, 1),
            ('Reserved3', ULONG, 16),
        ]
        _PCI_EXPRESS_CORRECTABLE_ERROR_MASK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_CORRECTABLE_ERROR_MASK._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_CORRECTABLE_ERROR_MASK.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_CORRECTABLE_ERROR_MASK = _PCI_EXPRESS_CORRECTABLE_ERROR_MASK
        PPCI_CORRECTABLE_ERROR_MASK = POINTER(_PCI_EXPRESS_CORRECTABLE_ERROR_MASK)


        class _PCI_EXPRESS_AER_CAPABILITIES(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('FirstErrorPointer', ULONG, 5),
            ('ECRCGenerationCapable', ULONG, 1),
            ('ECRCGenerationEnable', ULONG, 1),
            ('ECRCCheckCapable', ULONG, 1),
            ('ECRCCheckEnable', ULONG, 1),
            ('MultipleHeaderRecordingCapable', ULONG, 1),
            ('MultipleHeaderRecordingEnable', ULONG, 1),
            ('TlpPrefixLogPresent', ULONG, 1),
            ('Reserved', ULONG, 20),
        ]
        _PCI_EXPRESS_AER_CAPABILITIES.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_AER_CAPABILITIES._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_AER_CAPABILITIES.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_AER_CAPABILITIES = _PCI_EXPRESS_AER_CAPABILITIES
        PPCI_EXPRESS_AER_CAPABILITIES = POINTER(_PCI_EXPRESS_AER_CAPABILITIES)


        class _PCI_EXPRESS_ROOT_ERROR_COMMAND(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('CorrectableErrorReportingEnable', ULONG, 1),
            ('NonFatalErrorReportingEnable', ULONG, 1),
            ('FatalErrorReportingEnable', ULONG, 1),
            ('Reserved', ULONG, 29),
        ]
        _PCI_EXPRESS_ROOT_ERROR_COMMAND.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_ROOT_ERROR_COMMAND._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_ROOT_ERROR_COMMAND.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_ROOT_ERROR_COMMAND = _PCI_EXPRESS_ROOT_ERROR_COMMAND
        PPCI_EXPRESS_ROOT_ERROR_COMMAND = POINTER(_PCI_EXPRESS_ROOT_ERROR_COMMAND)


        class _PCI_EXPRESS_ROOT_ERROR_STATUS(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('CorrectableErrorReceived', ULONG, 1),
            ('MultipleCorrectableErrorsReceived', ULONG, 1),
            ('UncorrectableErrorReceived', ULONG, 1),
            ('MultipleUncorrectableErrorsReceived', ULONG, 1),
            ('FirstUncorrectableFatal', ULONG, 1),
            ('NonFatalErrorMessagesReceived', ULONG, 1),
            ('FatalErrorMessagesReceived', ULONG, 1),
            ('Reserved', ULONG, 20),
            ('AdvancedErrorInterruptMessageNumber', ULONG, 5),
        ]
        _PCI_EXPRESS_ROOT_ERROR_STATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_ROOT_ERROR_STATUS._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_ROOT_ERROR_STATUS.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_ROOT_ERROR_STATUS = _PCI_EXPRESS_ROOT_ERROR_STATUS
        PPCI_EXPRESS_ROOT_ERROR_STATUS = POINTER(_PCI_EXPRESS_ROOT_ERROR_STATUS)

        class _PCI_EXPRESS_ERROR_SOURCE_ID(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('CorrectableSourceIdFun', USHORT, 3),
            ('CorrectableSourceIdDev', USHORT, 5),
            ('CorrectableSourceIdBus', USHORT, 8),
            ('UncorrectableSourceIdFun', USHORT, 3),
            ('UncorrectableSourceIdDev', USHORT, 5),
            ('UncorrectableSourceIdBus', USHORT, 8),
        ]
        _PCI_EXPRESS_ERROR_SOURCE_ID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_ERROR_SOURCE_ID._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_ERROR_SOURCE_ID.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_ERROR_SOURCE_ID = _PCI_EXPRESS_ERROR_SOURCE_ID
        PPCI_EXPRESS_ERROR_SOURCE_ID = POINTER(_PCI_EXPRESS_ERROR_SOURCE_ID)


        class _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_STATUS(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('TargetAbortOnSplitCompletion', ULONG, 1),
            ('MasterAbortOnSplitCompletion', ULONG, 1),
            ('ReceivedTargetAbort', ULONG, 1),
            ('ReceivedMasterAbort', ULONG, 1),
            ('RsvdZ', ULONG, 1),
            ('UnexpectedSplitCompletionError', ULONG, 1),
            ('UncorrectableSplitCompletion', ULONG, 1),
            ('UncorrectableDataError', ULONG, 1),
            ('UncorrectableAttributeError', ULONG, 1),
            ('UncorrectableAddressError', ULONG, 1),
            ('DelayedTransactionDiscardTimerExpired', ULONG, 1),
            ('PERRAsserted', ULONG, 1),
            ('SERRAsserted', ULONG, 1),
            ('InternalBridgeError', ULONG, 1),
            ('Reserved', ULONG, 18),
        ]
        _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_STATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_STATUS._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_STATUS.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_STATUS = _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_STATUS
        PPCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_STATUS = POINTER(_PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_STATUS)


        class _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('TargetAbortOnSplitCompletion', ULONG, 1),
            ('MasterAbortOnSplitCompletion', ULONG, 1),
            ('ReceivedTargetAbort', ULONG, 1),
            ('ReceivedMasterAbort', ULONG, 1),
            ('RsvdZ', ULONG, 1),
            ('UnexpectedSplitCompletionError', ULONG, 1),
            ('UncorrectableSplitCompletion', ULONG, 1),
            ('UncorrectableDataError', ULONG, 1),
            ('UncorrectableAttributeError', ULONG, 1),
            ('UncorrectableAddressError', ULONG, 1),
            ('DelayedTransactionDiscardTimerExpired', ULONG, 1),
            ('PERRAsserted', ULONG, 1),
            ('SERRAsserted', ULONG, 1),
            ('InternalBridgeError', ULONG, 1),
            ('Reserved', ULONG, 18),
        ]
        _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK = _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK
        PPCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK = POINTER(_PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK)


        class _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_SEVERITY(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('TargetAbortOnSplitCompletion', ULONG, 1),
            ('MasterAbortOnSplitCompletion', ULONG, 1),
            ('ReceivedTargetAbort', ULONG, 1),
            ('ReceivedMasterAbort', ULONG, 1),
            ('RsvdZ', ULONG, 1),
            ('UnexpectedSplitCompletionError', ULONG, 1),
            ('UncorrectableSplitCompletion', ULONG, 1),
            ('UncorrectableDataError', ULONG, 1),
            ('UncorrectableAttributeError', ULONG, 1),
            ('UncorrectableAddressError', ULONG, 1),
            ('DelayedTransactionDiscardTimerExpired', ULONG, 1),
            ('PERRAsserted', ULONG, 1),
            ('SERRAsserted', ULONG, 1),
            ('InternalBridgeError', ULONG, 1),
            ('Reserved', ULONG, 18),
        ]
        _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_SEVERITY.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_SEVERITY._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_SEVERITY.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_SEVERITY = _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_SEVERITY
        PPCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_SEVERITY = POINTER(_PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_SEVERITY)


        class _PCI_EXPRESS_SEC_AER_CAPABILITIES(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('SecondaryUncorrectableFirstErrorPtr', ULONG, 5),
            ('Reserved', ULONG, 27),
        ]
        _PCI_EXPRESS_SEC_AER_CAPABILITIES.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_SEC_AER_CAPABILITIES._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_SEC_AER_CAPABILITIES.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_SEC_AER_CAPABILITIES = _PCI_EXPRESS_SEC_AER_CAPABILITIES
        PPCI_EXPRESS_SEC_AER_CAPABILITIES = POINTER(_PCI_EXPRESS_SEC_AER_CAPABILITIES)
        ROOT_CMD_ENABLE_CORRECTABLE_ERROR_REPORTING = 0x00000001
        ROOT_CMD_ENABLE_NONFATAL_ERROR_REPORTING = 0x00000002
        ROOT_CMD_ENABLE_FATAL_ERROR_REPORTING = 0x00000004
        ROOT_CMD_ERROR_REPORTING_ENABLE_MASK = (
            ROOT_CMD_ENABLE_FATAL_ERROR_REPORTING |
            ROOT_CMD_ENABLE_NONFATAL_ERROR_REPORTING |
            ROOT_CMD_ENABLE_CORRECTABLE_ERROR_REPORTING
        )

        # Advanced Error Reporting Capability structure.
        class _PCI_EXPRESS_AER_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_AER_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('UncorrectableErrorStatus', PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS),
            ('UncorrectableErrorMask', PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK),
            ('UncorrectableErrorSeverity', PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY),
            ('CorrectableErrorStatus', PCI_EXPRESS_CORRECTABLE_ERROR_STATUS),
            ('CorrectableErrorMask', PCI_EXPRESS_CORRECTABLE_ERROR_MASK),
            ('CapabilitiesAndControl', PCI_EXPRESS_AER_CAPABILITIES),
            ('HeaderLog', ULONG * 4),
            ('SecUncorrectableErrorStatus', PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_STATUS),
            ('SecUncorrectableErrorMask', PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK),
            ('SecUncorrectableErrorSeverity', PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_SEVERITY),
            ('SecCapabilitiesAndControl', PCI_EXPRESS_SEC_AER_CAPABILITIES),
            ('SecHeaderLog', ULONG * 4),
        ]
        PCI_EXPRESS_AER_CAPABILITY = _PCI_EXPRESS_AER_CAPABILITY
        PPCI_EXPRESS_AER_CAPABILITY = POINTER(_PCI_EXPRESS_AER_CAPABILITY)

        # Advanced Error Reporting Capability structure for root port.
        class _PCI_EXPRESS_ROOTPORT_AER_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_ROOTPORT_AER_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('UncorrectableErrorStatus', PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS),
            ('UncorrectableErrorMask', PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK),
            ('UncorrectableErrorSeverity', PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY),
            ('CorrectableErrorStatus', PCI_EXPRESS_CORRECTABLE_ERROR_STATUS),
            ('CorrectableErrorMask', PCI_EXPRESS_CORRECTABLE_ERROR_MASK),
            ('CapabilitiesAndControl', PCI_EXPRESS_AER_CAPABILITIES),
            ('HeaderLog', ULONG * 4),
            ('RootErrorCommand', PCI_EXPRESS_ROOT_ERROR_COMMAND),
            ('RootErrorStatus', PCI_EXPRESS_ROOT_ERROR_STATUS),
            ('ErrorSourceId', PCI_EXPRESS_ERROR_SOURCE_ID),
        ]
        PCI_EXPRESS_ROOTPORT_AER_CAPABILITY = _PCI_EXPRESS_ROOTPORT_AER_CAPABILITY
        PPCI_EXPRESS_ROOTPORT_AER_CAPABILITY = POINTER(_PCI_EXPRESS_ROOTPORT_AER_CAPABILITY)

        # Advanced Error Reporting Capability structure for root port.
        class _PCI_EXPRESS_BRIDGE_AER_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_BRIDGE_AER_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('UncorrectableErrorStatus', PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS),
            ('UncorrectableErrorMask', PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK),
            ('UncorrectableErrorSeverity', PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY),
            ('CorrectableErrorStatus', PCI_EXPRESS_CORRECTABLE_ERROR_STATUS),
            ('CorrectableErrorMask', PCI_EXPRESS_CORRECTABLE_ERROR_MASK),
            ('CapabilitiesAndControl', PCI_EXPRESS_AER_CAPABILITIES),
            ('HeaderLog', ULONG * 4),
            ('SecUncorrectableErrorStatus', PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_STATUS),
            ('SecUncorrectableErrorMask', PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK),
            ('SecUncorrectableErrorSeverity', PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_SEVERITY),
            ('SecCapabilitiesAndControl', PCI_EXPRESS_SEC_AER_CAPABILITIES),
            ('SecHeaderLog', ULONG * 4),
        ]
        PCI_EXPRESS_BRIDGE_AER_CAPABILITY = _PCI_EXPRESS_BRIDGE_AER_CAPABILITY
        PPCI_EXPRESS_BRIDGE_AER_CAPABILITY = POINTER(_PCI_EXPRESS_BRIDGE_AER_CAPABILITY)

        # Access Control Services Capability structure.
        class _PCI_EXPRESS_ACS_CAPABILITY_REGISTER(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('SourceValidation', USHORT, 1),
            ('TranslationBlocking', USHORT, 1),
            ('RequestRedirect', USHORT, 1),
            ('CompletionRedirect', USHORT, 1),
            ('UpstreamForwarding', USHORT, 1),
            ('EgressControl', USHORT, 1),
            ('DirectTranslation', USHORT, 1),
            ('Reserved', USHORT, 1),
            ('EgressControlVectorSize', USHORT, 8),
        ]
        _PCI_EXPRESS_ACS_CAPABILITY_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_ACS_CAPABILITY_REGISTER._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_ACS_CAPABILITY_REGISTER.DUMMYSTRUCTNAME),
            ('AsUSHORT', USHORT),
        ]
        PCI_EXPRESS_ACS_CAPABILITY_REGISTER = _PCI_EXPRESS_ACS_CAPABILITY_REGISTER
        PPCI_EXPRESS_ACS_CAPABILITY_REGISTER = POINTER(_PCI_EXPRESS_ACS_CAPABILITY_REGISTER)


        class _PCI_EXPRESS_ACS_CONTROL(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('SourceValidation', USHORT, 1),
            ('TranslationBlocking', USHORT, 1),
            ('RequestRedirect', USHORT, 1),
            ('CompletionRedirect', USHORT, 1),
            ('UpstreamForwarding', USHORT, 1),
            ('EgressControl', USHORT, 1),
            ('DirectTranslation', USHORT, 1),
            ('Reserved', USHORT, 9),
        ]
        _PCI_EXPRESS_ACS_CONTROL.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_ACS_CONTROL._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_ACS_CONTROL.DUMMYSTRUCTNAME),
            ('AsUSHORT', USHORT),
        ]
        PCI_EXPRESS_ACS_CONTROL = _PCI_EXPRESS_ACS_CONTROL
        PPCI_EXPRESS_ACS_CONTROL = POINTER(_PCI_EXPRESS_ACS_CONTROL)


        class _PCI_EXPRESS_ACS_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_ACS_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('Capability', PCI_EXPRESS_ACS_CAPABILITY_REGISTER),
            ('Control', PCI_EXPRESS_ACS_CONTROL),
            ('EgressControl', ULONG * 1),
        ]
        PCI_EXPRESS_ACS_CAPABILITY = _PCI_EXPRESS_ACS_CAPABILITY
        PPCI_EXPRESS_ACS_CAPABILITY = POINTER(_PCI_EXPRESS_ACS_CAPABILITY)

        # Single - Root I/O Virtualization Capability structure for endpoints
        class _PCI_EXPRESS_SRIOV_CAPS(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('VFMigrationCapable', ULONG, 1),
            ('Reserved1', ULONG, 20),
            ('VFMigrationInterruptNumber', ULONG, 11),
        ]
        _PCI_EXPRESS_SRIOV_CAPS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_SRIOV_CAPS._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_SRIOV_CAPS.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_SRIOV_CAPS = _PCI_EXPRESS_SRIOV_CAPS
        PPCI_EXPRESS_SRIOV_CAPS = POINTER(_PCI_EXPRESS_SRIOV_CAPS)


        class _PCI_EXPRESS_SRIOV_CONTROL(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('VFEnable', USHORT, 1),
            ('VFMigrationEnable', USHORT, 1),
            ('VFMigrationInterruptEnable', USHORT, 1),
            ('VFMemorySpaceEnable', USHORT, 1),
            ('ARICapableHierarchy', USHORT, 1),
            ('Reserved1', USHORT, 11),
        ]
        _PCI_EXPRESS_SRIOV_CONTROL.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_SRIOV_CONTROL._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_SRIOV_CONTROL.DUMMYSTRUCTNAME),
            ('AsUSHORT', USHORT),
        ]
        PCI_EXPRESS_SRIOV_CONTROL = _PCI_EXPRESS_SRIOV_CONTROL
        PPCI_EXPRESS_SRIOV_CONTROL = POINTER(_PCI_EXPRESS_SRIOV_CONTROL)


        class _PCI_EXPRESS_SRIOV_STATUS(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('VFMigrationStatus', USHORT, 1),
            ('Reserved1', USHORT, 15),
        ]
        _PCI_EXPRESS_SRIOV_STATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_SRIOV_STATUS._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_SRIOV_STATUS.DUMMYSTRUCTNAME),
            ('AsUSHORT', USHORT),
        ]
        PCI_EXPRESS_SRIOV_STATUS = _PCI_EXPRESS_SRIOV_STATUS
        PPCI_EXPRESS_SRIOV_STATUS = POINTER(_PCI_EXPRESS_SRIOV_STATUS)


        class _PCI_EXPRESS_SRIOV_MIGRATION_STATE_ARRAY(ctypes.Union):
            pass


        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('VFMigrationStateBIR', ULONG, 3),
            ('VFMigrationStateOffset', ULONG, 29),
        ]
        _PCI_EXPRESS_SRIOV_MIGRATION_STATE_ARRAY.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        _PCI_EXPRESS_SRIOV_MIGRATION_STATE_ARRAY._fields_ = [
            ('DUMMYSTRUCTNAME', _PCI_EXPRESS_SRIOV_MIGRATION_STATE_ARRAY.DUMMYSTRUCTNAME),
            ('AsULONG', ULONG),
        ]
        PCI_EXPRESS_SRIOV_MIGRATION_STATE_ARRAY = _PCI_EXPRESS_SRIOV_MIGRATION_STATE_ARRAY
        PPCI_EXPRESS_SRIOV_MIGRATION_STATE_ARRAY = POINTER(_PCI_EXPRESS_SRIOV_MIGRATION_STATE_ARRAY)


        class _PCI_EXPRESS_SRIOV_CAPABILITY(ctypes.Structure):
            pass


        _PCI_EXPRESS_SRIOV_CAPABILITY._fields_ = [
            ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
            ('SRIOVCapabilities', PCI_EXPRESS_SRIOV_CAPS),
            ('SRIOVControl', PCI_EXPRESS_SRIOV_CONTROL),
            ('SRIOVStatus', PCI_EXPRESS_SRIOV_STATUS),
            ('InitialVFs', USHORT),
            ('TotalVFs', USHORT),
            ('NumVFs', USHORT),
            ('FunctionDependencyLink', UCHAR),
            ('RsvdP1', UCHAR),
            ('FirstVFOffset', USHORT),
            ('VFStride', USHORT),
            ('RsvdP2', USHORT),
            ('VFDeviceId', USHORT),
            ('SupportedPageSizes', ULONG),
            ('SystemPageSize', ULONG),
            ('BaseAddresses', ULONG * PCI_TYPE0_ADDRESSES),
            ('VFMigrationStateArrayOffset', PCI_EXPRESS_SRIOV_MIGRATION_STATE_ARRAY),
        ]
        PCI_EXPRESS_SRIOV_CAPABILITY = _PCI_EXPRESS_SRIOV_CAPABILITY
        PPCI_EXPRESS_SRIOV_CAPABILITY = POINTER(_PCI_EXPRESS_SRIOV_CAPABILITY)

        # Base Class Code encodings for Base Class (from PCI spec rev 2.1).
        PCI_CLASS_PRE_20 = 0x00
        PCI_CLASS_MASS_STORAGE_CTLR = 0x01
        PCI_CLASS_NETWORK_CTLR = 0x02
        PCI_CLASS_DISPLAY_CTLR = 0x03
        PCI_CLASS_MULTIMEDIA_DEV = 0x04
        PCI_CLASS_MEMORY_CTLR = 0x05
        PCI_CLASS_BRIDGE_DEV = 0x06
        PCI_CLASS_SIMPLE_COMMS_CTLR = 0x07
        PCI_CLASS_BASE_SYSTEM_DEV = 0x08
        PCI_CLASS_INPUT_DEV = 0x09
        PCI_CLASS_DOCKING_STATION = 0x0A
        PCI_CLASS_PROCESSOR = 0x0B
        PCI_CLASS_SERIAL_BUS_CTLR = 0x0C
        PCI_CLASS_WIRELESS_CTLR = 0x0D
        PCI_CLASS_INTELLIGENT_IO_CTLR = 0x0E
        PCI_CLASS_SATELLITE_COMMS_CTLR = 0x0F
        PCI_CLASS_ENCRYPTION_DECRYPTION = 0x10
        PCI_CLASS_DATA_ACQ_SIGNAL_PROC = 0x11

        # 0d thru fe reserved
        PCI_CLASS_NOT_DEFINED = 0xFF

        # Sub Class Code encodings (PCI rev 2.1).
        # Class 00 - PCI_CLASS_PRE_20
        PCI_SUBCLASS_PRE_20_NON_VGA = 0x00
        PCI_SUBCLASS_PRE_20_VGA = 0x01

        # Class 01 - PCI_CLASS_MASS_STORAGE_CTLR
        PCI_SUBCLASS_MSC_SCSI_BUS_CTLR = 0x00
        PCI_SUBCLASS_MSC_IDE_CTLR = 0x01
        PCI_SUBCLASS_MSC_FLOPPY_CTLR = 0x02
        PCI_SUBCLASS_MSC_IPI_CTLR = 0x03
        PCI_SUBCLASS_MSC_RAID_CTLR = 0x04
        PCI_SUBCLASS_MSC_AHCI_CTLR = 0x06
        PCI_SUBCLASS_MSC_NVM_CTLR = 0x08
        PCI_SUBCLASS_MSC_OTHER = 0x80

        # SubClass 08 - PCI_SUBCLASS_MSC_NVM_CTLR
        PCI_PROGRAMMING_INTERFACE_MSC_NVM_EXPRESS = 0x02

        # Class 02 - PCI_CLASS_NETWORK_CTLR
        PCI_SUBCLASS_NET_ETHERNET_CTLR = 0x00
        PCI_SUBCLASS_NET_TOKEN_RING_CTLR = 0x01
        PCI_SUBCLASS_NET_FDDI_CTLR = 0x02
        PCI_SUBCLASS_NET_ATM_CTLR = 0x03
        PCI_SUBCLASS_NET_ISDN_CTLR = 0x04
        PCI_SUBCLASS_NET_OTHER = 0x80

        # Class 03 - PCI_CLASS_DISPLAY_CTLR
        # N.B. Sub Class 00 could be VGA or 8514 depending on Interface byte
        PCI_SUBCLASS_VID_VGA_CTLR = 0x00
        PCI_SUBCLASS_VID_XGA_CTLR = 0x01
        PCI_SUBLCASS_VID_3D_CTLR = 0x02
        PCI_SUBCLASS_VID_OTHER = 0x80

        # Class 04 - PCI_CLASS_MULTIMEDIA_DEV
        PCI_SUBCLASS_MM_VIDEO_DEV = 0x00
        PCI_SUBCLASS_MM_AUDIO_DEV = 0x01
        PCI_SUBCLASS_MM_TELEPHONY_DEV = 0x02
        PCI_SUBCLASS_MM_OTHER = 0x80

        # Class 05 - PCI_CLASS_MEMORY_CTLR
        PCI_SUBCLASS_MEM_RAM = 0x00
        PCI_SUBCLASS_MEM_FLASH = 0x01
        PCI_SUBCLASS_MEM_OTHER = 0x80

        # Class 06 - PCI_CLASS_BRIDGE_DEV
        PCI_SUBCLASS_BR_HOST = 0x00
        PCI_SUBCLASS_BR_ISA = 0x01
        PCI_SUBCLASS_BR_EISA = 0x02
        PCI_SUBCLASS_BR_MCA = 0x03
        PCI_SUBCLASS_BR_PCI_TO_PCI = 0x04
        PCI_SUBCLASS_BR_PCMCIA = 0x05
        PCI_SUBCLASS_BR_NUBUS = 0x06
        PCI_SUBCLASS_BR_CARDBUS = 0x07
        PCI_SUBCLASS_BR_RACEWAY = 0x08
        PCI_SUBCLASS_BR_OTHER = 0x80

        # Class 07 - PCI_CLASS_SIMPLE_COMMS_CTLR
        # N.B. Sub Class 00 and 01 additional info in Interface byte
        PCI_SUBCLASS_COM_SERIAL = 0x00
        PCI_SUBCLASS_COM_PARALLEL = 0x01
        PCI_SUBCLASS_COM_MULTIPORT = 0x02
        PCI_SUBCLASS_COM_MODEM = 0x03
        PCI_SUBCLASS_COM_OTHER = 0x80

        # Class 08 - PCI_CLASS_BASE_SYSTEM_DEV
        # N.B. See Interface byte for additional info.
        PCI_SUBCLASS_SYS_INTERRUPT_CTLR = 0x00
        PCI_SUBCLASS_SYS_DMA_CTLR = 0x01
        PCI_SUBCLASS_SYS_SYSTEM_TIMER = 0x02
        PCI_SUBCLASS_SYS_REAL_TIME_CLOCK = 0x03
        PCI_SUBCLASS_SYS_GEN_HOTPLUG_CTLR = 0x04
        PCI_SUBCLASS_SYS_SDIO_CTRL = 0x05
        PCI_SUBCLASS_SYS_OTHER = 0x80

        # Class 09 - PCI_CLASS_INPUT_DEV
        PCI_SUBCLASS_INP_KEYBOARD = 0x00
        PCI_SUBCLASS_INP_DIGITIZER = 0x01
        PCI_SUBCLASS_INP_MOUSE = 0x02
        PCI_SUBCLASS_INP_SCANNER = 0x03
        PCI_SUBCLASS_INP_GAMEPORT = 0x04
        PCI_SUBCLASS_INP_OTHER = 0x80

        # Class 0a - PCI_CLASS_DOCKING_STATION
        PCI_SUBCLASS_DOC_GENERIC = 0x00
        PCI_SUBCLASS_DOC_OTHER = 0x80

        # Class 0b - PCI_CLASS_PROCESSOR
        PCI_SUBCLASS_PROC_386 = 0x00
        PCI_SUBCLASS_PROC_486 = 0x01
        PCI_SUBCLASS_PROC_PENTIUM = 0x02
        PCI_SUBCLASS_PROC_ALPHA = 0x10
        PCI_SUBCLASS_PROC_POWERPC = 0x20
        PCI_SUBCLASS_PROC_COPROCESSOR = 0x40

        # Class 0c - PCI_CLASS_SERIAL_BUS_CTLR
        PCI_SUBCLASS_SB_IEEE1394 = 0x00
        PCI_SUBCLASS_SB_ACCESS = 0x01
        PCI_SUBCLASS_SB_SSA = 0x02
        PCI_SUBCLASS_SB_USB = 0x03
        PCI_SUBCLASS_SB_FIBRE_CHANNEL = 0x04
        PCI_SUBCLASS_SB_SMBUS = 0x05
        PCI_SUBCLASS_SB_THUNDERBOLT = 0x0A

        # Class 0d - PCI_CLASS_WIRELESS_CTLR
        PCI_SUBCLASS_WIRELESS_IRDA = 0x00
        PCI_SUBCLASS_WIRELESS_CON_IR = 0x01
        PCI_SUBCLASS_WIRELESS_RF = 0x10
        PCI_SUBCLASS_WIRELESS_OTHER = 0x80

        # Class 0e - PCI_CLASS_INTELLIGENT_IO_CTLR
        PCI_SUBCLASS_INTIO_I2O = 0x00

        # Class 0f - PCI_CLASS_SATELLITE_CTLR
        PCI_SUBCLASS_SAT_TV = 0x01
        PCI_SUBCLASS_SAT_AUDIO = 0x02
        PCI_SUBCLASS_SAT_VOICE = 0x03
        PCI_SUBCLASS_SAT_DATA = 0x04

        # Class 10 - PCI_CLASS_ENCRYPTION_DECRYPTION
        PCI_SUBCLASS_CRYPTO_NET_COMP = 0x00
        PCI_SUBCLASS_CRYPTO_ENTERTAINMENT = 0x10
        PCI_SUBCLASS_CRYPTO_OTHER = 0x80

        # Class 11 - PCI_CLASS_DATA_ACQ_SIGNAL_PROC
        PCI_SUBCLASS_DASP_DPIO = 0x00
        PCI_SUBCLASS_DASP_OTHER = 0x80

        # Bit encodes for PCI_COMMON_CONFIG.u.type0.BaseAddresses
        PCI_ADDRESS_IO_SPACE = 0x00000001
        PCI_ADDRESS_MEMORY_TYPE_MASK = 0x00000006
        PCI_ADDRESS_MEMORY_PREFETCHABLE = 0x00000008
        PCI_ADDRESS_IO_ADDRESS_MASK = 0xFFFFFFFC
        PCI_ADDRESS_MEMORY_ADDRESS_MASK = 0xFFFFFFF0
        PCI_ADDRESS_ROM_ADDRESS_MASK = 0xFFFFF800
        PCI_TYPE_32BIT = 0
        PCI_TYPE_20BIT = 2
        PCI_TYPE_64BIT = 4

        # Bit encodes for PCI_COMMON_CONFIG.u.type0.ROMBaseAddresses
        PCI_ROMADDRESS_ENABLED = 0x00000001

        # Reference notes for PCI configuration fields:
        # ro these field are read only. changes to these fields are ignored
        # ro+ these field are intended to be read only and should be
        # initialized
        # by the system to their proper values. However, driver may change
        # these settings.
        # - - -
        # All resources consumed by a PCI device start as uninitialized
        # under NT. An uninitialized memory or I/O base address can be
        # determined by checking it's corresponding enabled bit in the
        # PCI_COMMON_CONFIG.Command value. An InterruptLine is uninitialized
        # if it contains the value of - 1.
    # END IF   _PCI_X_

    # Device Presence interface
    PCI_DEVICE_PRESENT_INTERFACE_VERSION = 1

    # Flags for PCI_DEVICE_PRESENCE_PARAMETERS
    PCI_USE_SUBSYSTEM_IDS = 0x00000001
    PCI_USE_REVISION = 0x00000002

    # The following flags are only valid for IsDevicePresentEx
    PCI_USE_VENDEV_IDS = 0x00000004
    PCI_USE_CLASS_SUBCLASS = 0x00000008
    PCI_USE_PROGIF = 0x00000010
    PCI_USE_LOCAL_BUS = 0x00000020
    PCI_USE_LOCAL_DEVICE = 0x00000040


    # Search parameters structure for IsDevicePresentEx
    class _PCI_DEVICE_PRESENCE_PARAMETERS(ctypes.Structure):
        pass


    _PCI_DEVICE_PRESENCE_PARAMETERS._fields_ = [
        ('Size', ULONG),
        ('Flags', ULONG),
        ('VendorID', USHORT),
        ('DeviceID', USHORT),
        ('RevisionID', UCHAR),
        ('SubVendorID', USHORT),
        ('SubSystemID', USHORT),
        ('BaseClass', UCHAR),
        ('SubClass', UCHAR),
        ('ProgIf', UCHAR),
    ]
    PCI_DEVICE_PRESENCE_PARAMETERS = _PCI_DEVICE_PRESENCE_PARAMETERS
    PPCI_DEVICE_PRESENCE_PARAMETERS = POINTER(_PCI_DEVICE_PRESENCE_PARAMETERS)
    PPCI_IS_DEVICE_PRESENT = POINTER(PCI_IS_DEVICE_PRESENT)
    PPCI_IS_DEVICE_PRESENT_EX = POINTER(PCI_IS_DEVICE_PRESENT_EX)


    class _PCI_DEVICE_PRESENT_INTERFACE(ctypes.Structure):
        pass


    _PCI_DEVICE_PRESENT_INTERFACE._fields_ = [
        ('Size', USHORT), # generic interface header
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('IsDevicePresent', PPCI_IS_DEVICE_PRESENT), # pci device info
        ('IsDevicePresentEx', PPCI_IS_DEVICE_PRESENT_EX),
    ]
    PCI_DEVICE_PRESENT_INTERFACE = _PCI_DEVICE_PRESENT_INTERFACE
    PPCI_DEVICE_PRESENT_INTERFACE = POINTER(_PCI_DEVICE_PRESENT_INTERFACE)

    # Pci Express Link Quiesce Interface
    PCI_EXPRESS_LINK_QUIESCENT_INTERFACE_VERSION = 1
    PPCI_EXPRESS_ENTER_LINK_QUIESCENT_MODE = POINTER(PCI_EXPRESS_ENTER_LINK_QUIESCENT_MODE)
    PPCI_EXPRESS_EXIT_LINK_QUIESCENT_MODE = POINTER(PCI_EXPRESS_EXIT_LINK_QUIESCENT_MODE)


    class _PCI_EXPRESS_LINK_QUIESCENT_INTERFACE(ctypes.Structure):
        pass


    _PCI_EXPRESS_LINK_QUIESCENT_INTERFACE._fields_ = [
        ('Size', USHORT),
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('PciExpressEnterLinkQuiescentMode', PPCI_EXPRESS_ENTER_LINK_QUIESCENT_MODE),
        ('PciExpressExitLinkQuiescentMode', PPCI_EXPRESS_EXIT_LINK_QUIESCENT_MODE),
    ]
    PCI_EXPRESS_LINK_QUIESCENT_INTERFACE = _PCI_EXPRESS_LINK_QUIESCENT_INTERFACE
    PPCI_EXPRESS_LINK_QUIESCENT_INTERFACE = POINTER(_PCI_EXPRESS_LINK_QUIESCENT_INTERFACE)

    # Pci Express Root Port Access Interface
    PCI_EXPRESS_ROOT_PORT_INTERFACE_VERSION = 1


    class _PCI_EXPRESS_ROOT_PORT_INTERFACE(ctypes.Structure):
        pass


    _PCI_EXPRESS_ROOT_PORT_INTERFACE._fields_ = [
        ('Size', USHORT),
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('ReadConfigSpace', PPCI_EXPRESS_ROOT_PORT_READ_CONFIG_SPACE),
        ('WriteConfigSpace', PPCI_EXPRESS_ROOT_PORT_WRITE_CONFIG_SPACE),
    ]
    PCI_EXPRESS_ROOT_PORT_INTERFACE = _PCI_EXPRESS_ROOT_PORT_INTERFACE
    PPCI_EXPRESS_ROOT_PORT_INTERFACE = POINTER(_PCI_EXPRESS_ROOT_PORT_INTERFACE)

    # MSI - X interrupt table configuration interface
    PCI_MSIX_TABLE_CONFIG_INTERFACE_VERSION = 1
    PPCI_MSIX_SET_ENTRY = POINTER(PCI_MSIX_SET_ENTRY)
    PPCI_MSIX_MASKUNMASK_ENTRY = POINTER(PCI_MSIX_MASKUNMASK_ENTRY)
    PPCI_MSIX_GET_ENTRY = POINTER(PCI_MSIX_GET_ENTRY)
    PPCI_MSIX_GET_TABLE_SIZE = POINTER(PCI_MSIX_GET_TABLE_SIZE)


    class _PCI_MSIX_TABLE_CONFIG_INTERFACE(ctypes.Structure):
        pass


    _PCI_MSIX_TABLE_CONFIG_INTERFACE._fields_ = [
        ('Size', USHORT),
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('SetTableEntry', PPCI_MSIX_SET_ENTRY),
        ('MaskTableEntry', PPCI_MSIX_MASKUNMASK_ENTRY),
        ('UnmaskTableEntry', PPCI_MSIX_MASKUNMASK_ENTRY),
        ('GetTableEntry', PPCI_MSIX_GET_ENTRY),
        ('GetTableSize', PPCI_MSIX_GET_TABLE_SIZE),
    ]
    PCI_MSIX_TABLE_CONFIG_INTERFACE = _PCI_MSIX_TABLE_CONFIG_INTERFACE
    PPCI_MSIX_TABLE_CONFIG_INTERFACE = POINTER(_PCI_MSIX_TABLE_CONFIG_INTERFACE)
    PCI_MSIX_TABLE_CONFIG_MINIMUM_SIZE = RTL_SIZEOF_THROUGH_FIELD(
        PCI_MSIX_TABLE_CONFIG_INTERFACE,
        PCI_MSIX_TABLE_CONFIG_INTERFACE.UnmaskTableEntry,
    )
    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwCreateFile(
        # _Out_ PHANDLE FileHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _Out_ PIO_STATUS_BLOCK IoStatusBlock,
        # _In_opt_ PLARGE_INTEGER AllocationSize,
        # _In_ ULONG FileAttributes,
        # _In_ ULONG ShareAccess,
        # _In_ ULONG CreateDisposition,
        # _In_ ULONG CreateOptions,
        # _In_reads_bytes_opt_(EaLength) PVOID EaBuffer,
        # _In_ ULONG EaLength
        # );
        ZwCreateFile = ntdll.ZwCreateFile
        ZwCreateFile.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenFile(
        # _Out_ PHANDLE FileHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _Out_ PIO_STATUS_BLOCK IoStatusBlock,
        # _In_ ULONG ShareAccess,
        # _In_ ULONG OpenOptions
        # );
        ZwOpenFile = ntdll.ZwOpenFile
        ZwOpenFile.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwLoadDriver(
        # _In_ PUNICODE_STRING DriverServiceName
        # );
        ZwLoadDriver = ntdll.ZwLoadDriver
        ZwLoadDriver.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwUnloadDriver(
        # _In_ PUNICODE_STRING DriverServiceName
        # );
        ZwUnloadDriver = ntdll.ZwUnloadDriver
        ZwUnloadDriver.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwQueryInformationFile(
        # _In_ HANDLE FileHandle,
        # _Out_ PIO_STATUS_BLOCK IoStatusBlock,
        # _Out_writes_bytes_(Length) PVOID FileInformation,
        # _In_ ULONG Length,
        # _In_ FILE_INFORMATION_CLASS FileInformationClass
        # );
        ZwQueryInformationFile = ntdll.ZwQueryInformationFile
        ZwQueryInformationFile.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwSetInformationFile(
        # _In_ HANDLE FileHandle,
        # _Out_ PIO_STATUS_BLOCK IoStatusBlock,
        # _In_reads_bytes_(Length) PVOID FileInformation,
        # _In_ ULONG Length,
        # _In_ FILE_INFORMATION_CLASS FileInformationClass
        # );
        ZwSetInformationFile = ntdll.ZwSetInformationFile
        ZwSetInformationFile.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwReadFile(
        # _In_ HANDLE FileHandle,
        # _In_opt_ HANDLE Event,
        # _In_opt_ PIO_APC_ROUTINE ApcRoutine,
        # _In_opt_ PVOID ApcContext,
        # _Out_ PIO_STATUS_BLOCK IoStatusBlock,
        # _Out_writes_bytes_(Length) PVOID Buffer,
        # _In_ ULONG Length,
        # _In_opt_ PLARGE_INTEGER ByteOffset,
        # _In_opt_ PULONG Key
        # );
        ZwReadFile = ntdll.ZwReadFile
        ZwReadFile.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwWriteFile(
        # _In_ HANDLE FileHandle,
        # _In_opt_ HANDLE Event,
        # _In_opt_ PIO_APC_ROUTINE ApcRoutine,
        # _In_opt_ PVOID ApcContext,
        # _Out_ PIO_STATUS_BLOCK IoStatusBlock,
        # _In_reads_bytes_(Length) PVOID Buffer,
        # _In_ ULONG Length,
        # _In_opt_ PLARGE_INTEGER ByteOffset,
        # _In_opt_ PULONG Key
        # );
        ZwWriteFile = ntdll.ZwWriteFile
        ZwWriteFile.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwClose(
        # _In_ HANDLE Handle
        # );
        ZwClose = ntdll.ZwClose
        ZwClose.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwCreateDirectoryObject(
        # _Out_ PHANDLE DirectoryHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes
        # );
        ZwCreateDirectoryObject = ntdll.ZwCreateDirectoryObject
        ZwCreateDirectoryObject.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwMakeTemporaryObject(
        # _In_ HANDLE Handle
        # );
        ZwMakeTemporaryObject = ntdll.ZwMakeTemporaryObject
        ZwMakeTemporaryObject.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(APC_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwCreateSection (
        # _Out_ PHANDLE SectionHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _In_opt_ PLARGE_INTEGER MaximumSize,
        # _In_ ULONG SectionPageProtection,
        # _In_ ULONG AllocationAttributes,
        # _In_opt_ HANDLE FileHandle
        # );
        ZwCreateSection = ntdll.ZwCreateSection
        ZwCreateSection.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenSection(
        # _Out_ PHANDLE SectionHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes
        # );
        ZwOpenSection = ntdll.ZwOpenSection
        ZwOpenSection.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _Must_inspect_result_
        # _Post_satisfies_(*ViewSize >= _Old_(*ViewSize))
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwMapViewOfSection(
        # _In_ HANDLE SectionHandle,
        # _In_ HANDLE ProcessHandle,
        # _Outptr_result_bytebuffer_(*ViewSize) PVOID *BaseAddress,
        # _In_ ULONG_PTR ZeroBits,
        # _In_ SIZE_T CommitSize,
        # _Inout_opt_ PLARGE_INTEGER SectionOffset,
        # _Inout_ PSIZE_T ViewSize,
        # _In_ SECTION_INHERIT InheritDisposition,
        # _In_ ULONG AllocationType,
        # _In_ ULONG Win32Protect
        # );
        ZwMapViewOfSection = ntdll.ZwMapViewOfSection
        ZwMapViewOfSection.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwUnmapViewOfSection(
        # _In_ HANDLE ProcessHandle,
        # _In_opt_ PVOID BaseAddress
        # );
        ZwUnmapViewOfSection = ntdll.ZwUnmapViewOfSection
        ZwUnmapViewOfSection.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwCreateKey(
        # _Out_ PHANDLE KeyHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _Reserved_ ULONG TitleIndex,
        # _In_opt_ PUNICODE_STRING Class,
        # _In_ ULONG CreateOptions,
        # _Out_opt_ PULONG Disposition
        # );
        ZwCreateKey = ntdll.ZwCreateKey
        ZwCreateKey.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # ZwCreateKeyTransacted(
        # _Out_ PHANDLE KeyHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _Reserved_ ULONG TitleIndex,
        # _In_opt_ PUNICODE_STRING Class,
        # _In_ ULONG CreateOptions,
        # _In_ HANDLE TransactionHandle,
        # _Out_opt_ PULONG Disposition
        # );
        ZwCreateKeyTransacted = ntdll.ZwCreateKeyTransacted
        ZwCreateKeyTransacted.restype = NTSYSAPI

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN10_TH2:
        # _Must_inspect_result_
        # _IRQL_requires_max_ (PASSIVE_LEVEL)
        # __kernel_entry NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwCreateRegistryTransaction (
        # _Out_ PHANDLE TransactionHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _In_opt_ ULONG CreateOptions
        # );
        ZwCreateRegistryTransaction = ntdll.ZwCreateRegistryTransaction
        ZwCreateRegistryTransaction.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN10_TH2:
        # _Must_inspect_result_
        # _IRQL_requires_max_ (PASSIVE_LEVEL)
        # __kernel_entry NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # NtOpenRegistryTransaction (
        # _Out_ PHANDLE TransactionHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes
        # );
        NtOpenRegistryTransaction = ntdll.NtOpenRegistryTransaction
        NtOpenRegistryTransaction.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN10_TH2:
        # _IRQL_requires_max_ (PASSIVE_LEVEL)
        # __kernel_entry NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwCommitRegistryTransaction (
        # _In_ HANDLE TransactionHandle,
        # _In_ ULONG Flags
        # );
        ZwCommitRegistryTransaction = ntdll.ZwCommitRegistryTransaction
        ZwCommitRegistryTransaction.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN10_TH2:
        # _IRQL_requires_max_ (PASSIVE_LEVEL)
        # __kernel_entry NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # NtRollbackRegistryTransaction (
        # _In_ HANDLE TransactionHandle,
        # _In_ ULONG Flags
        # );
        NtRollbackRegistryTransaction = ntdll.NtRollbackRegistryTransaction
        NtRollbackRegistryTransaction.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenKey(
        # _Out_ PHANDLE KeyHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes
        # );
        ZwOpenKey = ntdll.ZwOpenKey
        ZwOpenKey.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN7:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenKeyEx(
        # _Out_ PHANDLE KeyHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _In_ ULONG OpenOptions
        # );
        ZwOpenKeyEx = ntdll.ZwOpenKeyEx
        ZwOpenKeyEx.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenKeyTransacted(
        # _Out_ PHANDLE KeyHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _In_ HANDLE TransactionHandle
        # );
        ZwOpenKeyTransacted = ntdll.ZwOpenKeyTransacted
        ZwOpenKeyTransacted.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN7:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenKeyTransactedEx(
        # _Out_ PHANDLE KeyHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _In_ ULONG OpenOptions,
        # _In_ HANDLE TransactionHandle
        # );
        ZwOpenKeyTransactedEx = ntdll.ZwOpenKeyTransactedEx
        ZwOpenKeyTransactedEx.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwDeleteKey(
        # _In_ HANDLE KeyHandle
        # );
        ZwDeleteKey = ntdll.ZwDeleteKey
        ZwDeleteKey.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwDeleteValueKey(
        # _In_ HANDLE KeyHandle,
        # _In_ PUNICODE_STRING ValueName
        # );
        ZwDeleteValueKey = ntdll.ZwDeleteValueKey
        ZwDeleteValueKey.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _When_(Length == 0, _Post_satisfies_(return < 0))
        # _When_(Length > 0, _Post_satisfies_(return <= 0))
        # _Success_(return == STATUS_SUCCESS)
        # _On_failure_(_When_(return == STATUS_BUFFER_OVERFLOW || return == STATUS_BUFFER_TOO_SMALL, _Post_satisfies_(*ResultLength > Length)))
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwEnumerateKey(
        # _In_ HANDLE KeyHandle,
        # _In_ ULONG Index,
        # _In_ KEY_INFORMATION_CLASS KeyInformationClass,
        # _Out_writes_bytes_to_opt_(Length, *ResultLength) PVOID KeyInformation,
        # _In_ ULONG Length,
        # _Out_ PULONG ResultLength
        # );
        ZwEnumerateKey = ntdll.ZwEnumerateKey
        ZwEnumerateKey.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _When_(Length == 0, _Post_satisfies_(return < 0))
        # _When_(Length > 0, _Post_satisfies_(return <= 0))
        # _Success_(return == STATUS_SUCCESS)
        # _On_failure_(_When_(return == STATUS_BUFFER_OVERFLOW || return == STATUS_BUFFER_TOO_SMALL, _Post_satisfies_(*ResultLength > Length)))
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwEnumerateValueKey(
        # _In_ HANDLE KeyHandle,
        # _In_ ULONG Index,
        # _In_ KEY_VALUE_INFORMATION_CLASS KeyValueInformationClass,
        # _Out_writes_bytes_to_opt_(Length, *ResultLength) PVOID KeyValueInformation,
        # _In_ ULONG Length,
        # _Out_ PULONG ResultLength
        # );
        ZwEnumerateValueKey = ntdll.ZwEnumerateValueKey
        ZwEnumerateValueKey.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwFlushKey(
        # _In_ HANDLE KeyHandle
        # );
        ZwFlushKey = ntdll.ZwFlushKey
        ZwFlushKey.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _When_(Length == 0, _Post_satisfies_(return < 0))
        # _When_(Length > 0, _Post_satisfies_(return <= 0))
        # _Success_(return == STATUS_SUCCESS)
        # _On_failure_(_When_(return == STATUS_BUFFER_OVERFLOW || return == STATUS_BUFFER_TOO_SMALL, _Post_satisfies_(*ResultLength > Length)))
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwQueryKey(
        # _In_ HANDLE KeyHandle,
        # _In_ KEY_INFORMATION_CLASS KeyInformationClass,
        # _Out_writes_bytes_to_opt_(Length, *ResultLength) PVOID KeyInformation,
        # _In_ ULONG Length,
        # _Out_ PULONG ResultLength
        # );
        ZwQueryKey = ntdll.ZwQueryKey
        ZwQueryKey.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _When_(Length == 0, _Post_satisfies_(return < 0))
        # _When_(Length > 0, _Post_satisfies_(return <= 0))
        # _Success_(return == STATUS_SUCCESS)
        # _On_failure_(_When_(return == STATUS_BUFFER_OVERFLOW || return == STATUS_BUFFER_TOO_SMALL, _Post_satisfies_(*ResultLength > Length)))
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwQueryValueKey(
        # _In_ HANDLE KeyHandle,
        # _In_ PUNICODE_STRING ValueName,
        # _In_ KEY_VALUE_INFORMATION_CLASS KeyValueInformationClass,
        # _Out_writes_bytes_to_opt_(Length, *ResultLength) PVOID KeyValueInformation,
        # _In_ ULONG Length,
        # _Out_ PULONG ResultLength
        # );
        ZwQueryValueKey = ntdll.ZwQueryValueKey
        ZwQueryValueKey.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN7:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwRenameKey(
        # _In_ HANDLE           KeyHandle,
        # _In_ PUNICODE_STRING  NewName
        # );
        ZwRenameKey = ntdll.ZwRenameKey
        ZwRenameKey.restype = NTSTATUS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwSaveKey (
        # _In_ HANDLE KeyHandle,
        # _In_ HANDLE FileHandle
        # );
        ZwSaveKey = ntdll.ZwSaveKey
        ZwSaveKey.restype = NTSTATUS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwSaveKeyEx (
        # _In_ HANDLE KeyHandle,
        # _In_ HANDLE FileHandle,
        # _In_ ULONG  Format
        # );
        ZwSaveKeyEx = ntdll.ZwSaveKeyEx
        ZwSaveKeyEx.restype = NTSTATUS

        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwRestoreKey (
        # _In_ HANDLE KeyHandle,
        # _In_opt_ HANDLE FileHandle,
        # _In_ ULONG Flags
        # );
        ZwRestoreKey = ntdll.ZwRestoreKey
        ZwRestoreKey.restype = NTSTATUS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwSetInformationKey (
        # _In_ HANDLE KeyHandle,
        # _In_ __drv_strictTypeMatch(__drv_typeConst)
        # KEY_SET_INFORMATION_CLASS KeySetInformationClass,
        # _In_reads_bytes_(KeySetInformationLength) PVOID KeySetInformation,
        # _In_ ULONG KeySetInformationLength
        # );
        ZwSetInformationKey = ntdll.ZwSetInformationKey
        ZwSetInformationKey.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # //@[comment("MVI_tracked")]
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwSetValueKey(
        # _In_ HANDLE KeyHandle,
        # _In_ PUNICODE_STRING ValueName,
        # _In_opt_ ULONG TitleIndex,
        # _In_ ULONG Type,
        # _In_reads_bytes_opt_(DataSize) PVOID Data,
        # _In_ ULONG DataSize
        # );
        ZwSetValueKey = ntdll.ZwSetValueKey
        ZwSetValueKey.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenSymbolicLinkObject(
        # _Out_ PHANDLE LinkHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes
        # );
        ZwOpenSymbolicLinkObject = ntdll.ZwOpenSymbolicLinkObject
        ZwOpenSymbolicLinkObject.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwQuerySymbolicLinkObject(
        # _In_ HANDLE LinkHandle,
        # _Inout_ PUNICODE_STRING LinkTarget,
        # _Out_opt_ PULONG ReturnedLength
        # );
        ZwQuerySymbolicLinkObject = ntdll.ZwQuerySymbolicLinkObject
        ZwQuerySymbolicLinkObject.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwCreateTransactionManager (
        # _Out_ PHANDLE TmHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _In_opt_ PUNICODE_STRING LogFileName,
        # _In_opt_ ULONG CreateOptions,
        # _In_opt_ ULONG CommitStrength
        # );
        ZwCreateTransactionManager = ntdll.ZwCreateTransactionManager
        ZwCreateTransactionManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenTransactionManager (
        # _Out_ PHANDLE TmHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _In_opt_ PUNICODE_STRING LogFileName,
        # _In_opt_ LPGUID TmIdentity,
        # _In_opt_ ULONG OpenOptions
        # );
        ZwOpenTransactionManager = ntdll.ZwOpenTransactionManager
        ZwOpenTransactionManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwRollforwardTransactionManager (
        # _In_ HANDLE TransactionManagerHandle,
        # _In_opt_ PLARGE_INTEGER TmVirtualClock
        # );
        ZwRollforwardTransactionManager = ntdll.ZwRollforwardTransactionManager
        ZwRollforwardTransactionManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwRecoverTransactionManager (
        # _In_ HANDLE TransactionManagerHandle
        # );
        ZwRecoverTransactionManager = ntdll.ZwRecoverTransactionManager
        ZwRecoverTransactionManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwQueryInformationTransactionManager (
        # _In_ HANDLE TransactionManagerHandle,
        # _In_ TRANSACTIONMANAGER_INFORMATION_CLASS TransactionManagerInformationClass,
        # _Out_writes_bytes_(TransactionManagerInformationLength) PVOID TransactionManagerInformation,
        # _In_ ULONG TransactionManagerInformationLength,
        # _Out_opt_ PULONG ReturnLength
        # );
        ZwQueryInformationTransactionManager = ntdll.ZwQueryInformationTransactionManager
        ZwQueryInformationTransactionManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwSetInformationTransactionManager (
        # _In_ HANDLE TmHandle,
        # _In_ TRANSACTIONMANAGER_INFORMATION_CLASS TransactionManagerInformationClass,
        # _In_ PVOID TransactionManagerInformation,
        # _In_ ULONG TransactionManagerInformationLength
        # );
        ZwSetInformationTransactionManager = ntdll.ZwSetInformationTransactionManager
        ZwSetInformationTransactionManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwEnumerateTransactionObject (
        # _In_opt_ HANDLE            RootObjectHandle,
        # _In_     KTMOBJECT_TYPE    QueryType,
        # _Inout_updates_bytes_(ObjectCursorLength) PKTMOBJECT_CURSOR ObjectCursor,
        # _In_     ULONG             ObjectCursorLength,
        # _Out_    PULONG            ReturnLength
        # );
        ZwEnumerateTransactionObject = ntdll.ZwEnumerateTransactionObject
        ZwEnumerateTransactionObject.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwCreateTransaction (
        # _Out_ PHANDLE TransactionHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _In_opt_ LPGUID Uow,
        # _In_opt_ HANDLE TmHandle,
        # _In_opt_ ULONG CreateOptions,
        # _In_opt_ ULONG IsolationLevel,
        # _In_opt_ ULONG IsolationFlags,
        # _In_opt_ PLARGE_INTEGER Timeout,
        # _In_opt_ PUNICODE_STRING Description
        # );
        ZwCreateTransaction = ntdll.ZwCreateTransaction
        ZwCreateTransaction.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenTransaction (
        # _Out_ PHANDLE TransactionHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _In_ LPGUID Uow,
        # _In_opt_ HANDLE TmHandle
        # );
        ZwOpenTransaction = ntdll.ZwOpenTransaction
        ZwOpenTransaction.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwQueryInformationTransaction (
        # _In_ HANDLE TransactionHandle,
        # _In_ TRANSACTION_INFORMATION_CLASS TransactionInformationClass,
        # _Out_writes_bytes_(TransactionInformationLength) PVOID TransactionInformation,
        # _In_ ULONG TransactionInformationLength,
        # _Out_opt_ PULONG ReturnLength
        # );
        ZwQueryInformationTransaction = ntdll.ZwQueryInformationTransaction
        ZwQueryInformationTransaction.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwSetInformationTransaction (
        # _In_ HANDLE TransactionHandle,
        # _In_ TRANSACTION_INFORMATION_CLASS TransactionInformationClass,
        # _In_ PVOID TransactionInformation,
        # _In_ ULONG TransactionInformationLength
        # );
        ZwSetInformationTransaction = ntdll.ZwSetInformationTransaction
        ZwSetInformationTransaction.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwCommitTransaction (
        # _In_ HANDLE  TransactionHandle,
        # _In_ BOOLEAN Wait
        # );
        ZwCommitTransaction = ntdll.ZwCommitTransaction
        ZwCommitTransaction.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwRollbackTransaction (
        # _In_ HANDLE  TransactionHandle,
        # _In_ BOOLEAN Wait
        # );
        ZwRollbackTransaction = ntdll.ZwRollbackTransaction
        ZwRollbackTransaction.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwCreateResourceManager (
        # _Out_ PHANDLE ResourceManagerHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ HANDLE TmHandle,
        # _In_opt_ LPGUID ResourceManagerGuid,
        # _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _In_opt_ ULONG CreateOptions,
        # _In_opt_ PUNICODE_STRING Description
        # );
        ZwCreateResourceManager = ntdll.ZwCreateResourceManager
        ZwCreateResourceManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenResourceManager (
        # _Out_ PHANDLE ResourceManagerHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ HANDLE TmHandle,
        # _In_ LPGUID ResourceManagerGuid,
        # _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes
        # );
        ZwOpenResourceManager = ntdll.ZwOpenResourceManager
        ZwOpenResourceManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwRecoverResourceManager (
        # _In_ HANDLE ResourceManagerHandle
        # );
        ZwRecoverResourceManager = ntdll.ZwRecoverResourceManager
        ZwRecoverResourceManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwGetNotificationResourceManager (
        # _In_ HANDLE             ResourceManagerHandle,
        # _Out_ PTRANSACTION_NOTIFICATION TransactionNotification,
        # _In_ ULONG              NotificationLength,
        # _In_ PLARGE_INTEGER         Timeout,
        # _Out_opt_ PULONG                    ReturnLength,
        # _In_ ULONG                          Asynchronous,
        # _In_opt_ ULONG_PTR                  AsynchronousContext
        # );
        ZwGetNotificationResourceManager = ntdll.ZwGetNotificationResourceManager
        ZwGetNotificationResourceManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwQueryInformationResourceManager (
        # _In_ HANDLE ResourceManagerHandle,
        # _In_ RESOURCEMANAGER_INFORMATION_CLASS ResourceManagerInformationClass,
        # _Out_writes_bytes_(ResourceManagerInformationLength) PVOID ResourceManagerInformation,
        # _In_ ULONG ResourceManagerInformationLength,
        # _Out_opt_ PULONG ReturnLength
        # );
        ZwQueryInformationResourceManager = ntdll.ZwQueryInformationResourceManager
        ZwQueryInformationResourceManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwSetInformationResourceManager (
        # _In_ HANDLE ResourceManagerHandle,
        # _In_ RESOURCEMANAGER_INFORMATION_CLASS ResourceManagerInformationClass,
        # _In_reads_bytes_(ResourceManagerInformationLength) PVOID ResourceManagerInformation,
        # _In_ ULONG ResourceManagerInformationLength
        # );
        ZwSetInformationResourceManager = ntdll.ZwSetInformationResourceManager
        ZwSetInformationResourceManager.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwCreateEnlistment (
        # _Out_ PHANDLE EnlistmentHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ HANDLE ResourceManagerHandle,
        # _In_ HANDLE TransactionHandle,
        # _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _In_opt_ ULONG CreateOptions,
        # _In_ NOTIFICATION_MASK NotificationMask,
        # _In_opt_ PVOID EnlistmentKey
        # );
        ZwCreateEnlistment = ntdll.ZwCreateEnlistment
        ZwCreateEnlistment.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenEnlistment (
        # _Out_ PHANDLE EnlistmentHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ HANDLE RmHandle,
        # _In_ LPGUID EnlistmentGuid,
        # _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes
        # );
        ZwOpenEnlistment = ntdll.ZwOpenEnlistment
        ZwOpenEnlistment.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwQueryInformationEnlistment (
        # _In_ HANDLE EnlistmentHandle,
        # _In_ ENLISTMENT_INFORMATION_CLASS EnlistmentInformationClass,
        # _Out_writes_bytes_(EnlistmentInformationLength) PVOID EnlistmentInformation,
        # _In_ ULONG EnlistmentInformationLength,
        # _Out_opt_ PULONG ReturnLength
        # );
        ZwQueryInformationEnlistment = ntdll.ZwQueryInformationEnlistment
        ZwQueryInformationEnlistment.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwSetInformationEnlistment (
        # _In_ HANDLE EnlistmentHandle,
        # _In_ ENLISTMENT_INFORMATION_CLASS EnlistmentInformationClass,
        # _In_reads_bytes_(EnlistmentInformationLength) PVOID EnlistmentInformation,
        # _In_ ULONG EnlistmentInformationLength
        # );
        ZwSetInformationEnlistment = ntdll.ZwSetInformationEnlistment
        ZwSetInformationEnlistment.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwRecoverEnlistment (
        # _In_ HANDLE EnlistmentHandle,
        # _In_opt_ PVOID EnlistmentKey
        # );
        ZwRecoverEnlistment = ntdll.ZwRecoverEnlistment
        ZwRecoverEnlistment.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwPrePrepareEnlistment (
        # _In_ HANDLE EnlistmentHandle,
        # _In_opt_ PLARGE_INTEGER TmVirtualClock
        # );
        ZwPrePrepareEnlistment = ntdll.ZwPrePrepareEnlistment
        ZwPrePrepareEnlistment.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwPrepareEnlistment (
        # _In_ HANDLE EnlistmentHandle,
        # _In_opt_ PLARGE_INTEGER TmVirtualClock
        # );
        ZwPrepareEnlistment = ntdll.ZwPrepareEnlistment
        ZwPrepareEnlistment.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwCommitEnlistment (
        # _In_ HANDLE EnlistmentHandle,
        # _In_opt_ PLARGE_INTEGER TmVirtualClock
        # );
        ZwCommitEnlistment = ntdll.ZwCommitEnlistment
        ZwCommitEnlistment.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwRollbackEnlistment (
        # _In_ HANDLE EnlistmentHandle,
        # _In_opt_ PLARGE_INTEGER TmVirtualClock
        # );
        ZwRollbackEnlistment = ntdll.ZwRollbackEnlistment
        ZwRollbackEnlistment.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwPrePrepareComplete (
        # _In_ HANDLE            EnlistmentHandle,
        # _In_opt_ PLARGE_INTEGER TmVirtualClock
        # );
        ZwPrePrepareComplete = ntdll.ZwPrePrepareComplete
        ZwPrePrepareComplete.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwPrepareComplete (
        # _In_ HANDLE            EnlistmentHandle,
        # _In_opt_ PLARGE_INTEGER TmVirtualClock
        # );
        ZwPrepareComplete = ntdll.ZwPrepareComplete
        ZwPrepareComplete.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwCommitComplete (
        # _In_ HANDLE            EnlistmentHandle,
        # _In_opt_ PLARGE_INTEGER TmVirtualClock
        # );
        ZwCommitComplete = ntdll.ZwCommitComplete
        ZwCommitComplete.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwReadOnlyEnlistment (
        # _In_ HANDLE            EnlistmentHandle,
        # _In_opt_ PLARGE_INTEGER TmVirtualClock
        # );
        ZwReadOnlyEnlistment = ntdll.ZwReadOnlyEnlistment
        ZwReadOnlyEnlistment.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwRollbackComplete (
        # _In_ HANDLE            EnlistmentHandle,
        # _In_opt_ PLARGE_INTEGER TmVirtualClock
        # );
        ZwRollbackComplete = ntdll.ZwRollbackComplete
        ZwRollbackComplete.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwSinglePhaseReject (
        # _In_ HANDLE            EnlistmentHandle,
        # _In_opt_ PLARGE_INTEGER TmVirtualClock
        # );
        ZwSinglePhaseReject = ntdll.ZwSinglePhaseReject
        ZwSinglePhaseReject.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WS03:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSCALLAPI
        # NTSTATUS
        # NTAPI
        # ZwOpenEvent (
        # _Out_ PHANDLE EventHandle,
        # _In_ ACCESS_MASK DesiredAccess,
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes
        # );
        ZwOpenEvent = ntdll.ZwOpenEvent
        ZwOpenEvent.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN10_RS2:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwQueryInformationByName (
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _Out_ PIO_STATUS_BLOCK IoStatusBlock,
        # _Out_writes_bytes_(Length) PVOID FileInformation,
        # _In_ ULONG Length,
        # _In_ FILE_INFORMATION_CLASS FileInformationClass
        # );
        ZwQueryInformationByName = ntdll.ZwQueryInformationByName
        ZwQueryInformationByName.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # NTSYSAPI
        # NTSTATUS
        # NTAPI
        # ZwQueryFullAttributesFile(
        # _In_ POBJECT_ATTRIBUTES ObjectAttributes,
        # _Out_ PFILE_NETWORK_OPEN_INFORMATION FileInformation
        # );
        ZwQueryFullAttributesFile = ntdll.ZwQueryFullAttributesFile
        ZwQueryFullAttributesFile.restype = NTSTATUS

    # END IF

    if not defined(_CLFS_PUBLIC_H_):
        _CLFS_PUBLIC_H_ = 1
        CLFSUSER_API = None

        if not defined(CLFSUSER_API):
            if defined(__CLFSUSER_EXPORTS__):
                CLFSUSER_API = 1
            else:
                CLFSUSER_API = 1
            # END IF
        # END IF

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # FILE_ATTRIBUTE_DEDICATED is defined as FILE_ATTRIBUTE_TEMPORARY.
            FILE_ATTRIBUTE_DEDICATED = FILE_ATTRIBUTE_TEMPORARY

            # Container name and container size extended attribute entry names.
            EA_CONTAINER_NAME = "ContainerName"
            EA_CONTAINER_SIZE = "ContainerSize"

            # Base log file name 3 - letter extension.
            CLFS_BASELOG_EXTENSION = ".blf"

            # Common log file system public flags and constants.
            CLFS_FLAG_NO_FLAGS = 0x00000000
            CLFS_FLAG_FORCE_APPEND = 0x00000001
            CLFS_FLAG_FORCE_FLUSH = 0x00000002
            CLFS_FLAG_USE_RESERVATION = 0x00000004
            CLFS_FLAG_REENTRANT_FILE_SYSTEM = 0x00000008
            CLFS_FLAG_NON_REENTRANT_FILTER = 0x00000010
            CLFS_FLAG_REENTRANT_FILTER = 0x00000020
            CLFS_FLAG_IGNORE_SHARE_ACCESS = 0x00000040
            CLFS_FLAG_READ_IN_PROGRESS = 0x00000080
            CLFS_FLAG_MINIFILTER_LEVEL = 0x00000100
            CLFS_FLAG_HIDDEN_SYSTEM_LOG = 0x00000200

            #
            # Marshalling Context Flag
            CLFS_MARSHALLING_FLAG_NONE = 0x00000000
            CLFS_MARSHALLING_FLAG_DISABLE_BUFF_INIT = 0x00000001

            # Flag indicating all CLFS I/O will be targeted to an intermediate
            # level of the I/O stack
            CLFS_FLAG_FILTER_INTERMEDIATE_LEVEL = (
                CLFS_FLAG_NON_REENTRANT_FILTER
            )

            # Flag indicating all CLFS I/O will be targeted to the top level
            # of the I/O stack
            CLFS_FLAG_FILTER_TOP_LEVEL = CLFS_FLAG_REENTRANT_FILTER

            # CLFS_CONTAINER_INDEX
            # Index into the container table.
            CLFS_CONTAINER_ID = ULONG
            PCLFS_CONTAINER_ID = POINTER(CLFS_CONTAINER_ID)
            PPCLFS_CONTAINER_ID = POINTER(POINTER(CLFS_CONTAINER_ID))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        __CLFS_PRIVATE_LSN__ = None
        if defined(__CLFS_PRIVATE_LSN__):
            from pyWinAPI.shared.clfslsn_h import *
        else:
            if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
                # CLS_LSN
                class _CLS_LSN(ctypes.Structure):
                    pass


                _CLS_LSN._fields_ = [
                    ('Internal', ULONGLONG),
                ]
                CLS_LSN = _CLS_LSN
                PCLS_LSN = POINTER(_CLS_LSN)
                PPCLS_LSN = POINTER(POINTER(_CLS_LSN))
            # END IF  NTDDI_VERSION or _WIN32_WINNT

        # END IF  __CLFS_PRIVATE_LSN__

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # Alias CLS prefixed types with CLFS prefixes.
            CLFS_LSN = CLS_LSN
            PCLFS_LSN = POINTER(CLFS_LSN)
            PPCLFS_LSN = POINTER(POINTER(CLFS_LSN))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if defined(__cplusplus):
            pass
        # END IF  __cplusplus

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            CLFS_LSN_INVALID = CLS_LSN
            CLFS_LSN_INVALID_NULL = CLFS_LSN
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if defined(__cplusplus):
            pass
        # END IF  __cplusplus

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            if defined(__cplusplus):
            ClfsNullRecord = 0x00 # Null record type.
                ClfsDataRecord = 0x01 # Client data record.
                ClfsRestartRecord = 0x02 # Restart record.
                # Valid client records are restart and data records.
                ClfsClientRecord = 0x3
            else:
                ClfsNullRecord = 0x00  # Null record type.
                ClfsDataRecord = 0x01  # Client data record.
                ClfsRestartRecord = 0x02  # Restart record.
                # Valid client records are restart and data records.
                ClfsClientRecord = ClfsDataRecord | ClfsRestartRecord
            # END IF  _cplusplus
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # Log container path prefix indicating the log container's
            # location is
            # actually a stream inside of the BLF.

            if defined(_cplusplus):
                CLFS_CONTAINER_STREAM_PREFIX = "%BLF%:"
            else:
                CLFS_CONTAINER_STREAM_PREFIX = "%BLF%:"
            # END IF  _cplusplus
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # Log container path prefix indicating the log container's location
            # is
            # relative to the base log file (BLF) and not an absolute path.
            # Paths which do not being with said prefix are absolute paths.

            if defined(_cplusplus):
                CLFS_CONTAINER_RELATIVE_PREFIX = "%BLF%\\"
            else:
                CLFS_CONTAINER_RELATIVE_PREFIX = "%BLF%\\"
            # END IF  _cplusplus
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # Alias CLS prefix with CLFS prefixes.
            CLS_RECORD_TYPE = UCHAR
            PCLS_RECORD_TYPE = POINTER(UCHAR)
            PPCLS_RECORD_TYPE = POINTER(POINTER(UCHAR))

            CLFS_RECORD_TYPE = CLS_RECORD_TYPE
            PCLFS_RECORD_TYPE = POINTER(CLS_RECORD_TYPE)
            PPCLFS_RECORD_TYPE = POINTER(POINTER(CLS_RECORD_TYPE))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLS_CONTEXT_MODE
            # The context mode specifies the direction and access methods used
            # to scan the
            # log file.
            class _CLS_CONTEXT_MODE(ENUM):
                ClsContextNone = 0x00
                ClsContextUndoNext = 1
                ClsContextPrevious = 2
                ClsContextForward = 3


            CLS_CONTEXT_MODE = _CLS_CONTEXT_MODE
            PCLS_CONTEXT_MODE = POINTER(_CLS_CONTEXT_MODE)
            PPCLS_CONTEXT_MODE = POINTER(POINTER(_CLS_CONTEXT_MODE))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # Alias all CLS prefixes with CLFS prefixes.
            class _CLFS_CONTEXT_MODE(ENUM):
                ClfsContextNone = 0x00
                ClfsContextUndoNext = 1
                ClfsContextPrevious = 2
                ClfsContextForward = 3


            CLFS_CONTEXT_MODE = _CLFS_CONTEXT_MODE
            PCLFS_CONTEXT_MODE = POINTER(_CLFS_CONTEXT_MODE)
            PPCLFS_CONTEXT_MODE = POINTER(POINTER(_CLFS_CONTEXT_MODE))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLFSD_NODE_ID
            # Common log file system node identifier. Every CLFS file system
            # structure has a node identity and type. The node type is a
            # signature
            # field while the size is used in for consistency checking.
            class _CLFS_NODE_ID(ctypes.Structure):
                pass


            _CLFS_NODE_ID._fields_ = [
                ('cType', ULONG), # CLFS node type.
                ('cbNode', ULONG), # CLFS node size.
            ]
            CLFS_NODE_ID = _CLFS_NODE_ID
            PCLFS_NODE_ID = POINTER(_CLFS_NODE_ID)
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLS_WRITE_ENTRY
            # Write entry specifying the contents of a user buffer and length
            # that are
            # marshaled in the space reservation and append interface of the
            # CLS API.
            class _CLS_WRITE_ENTRY(ctypes.Structure):
                pass


            _CLS_WRITE_ENTRY._fields_ = [
                ('Buffer', PVOID),
                ('ByteLength', ULONG),
            ]
            CLS_WRITE_ENTRY = _CLS_WRITE_ENTRY
            PCLS_WRITE_ENTRY = POINTER(_CLS_WRITE_ENTRY)
            PPCLS_WRITE_ENTRY = POINTER(POINTER(_CLS_WRITE_ENTRY))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_WRITE_ENTRY = CLS_WRITE_ENTRY
            PCLFS_WRITE_ENTRY = POINTER(CLFS_WRITE_ENTRY)
            PPCLFS_WRITE_ENTRY = POINTER(POINTER(CLFS_WRITE_ENTRY))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLFS_LOG_ID
            #
            # A log identifier is a GUID that describes uniquely a physical
            # log file.
            CLFS_LOG_ID = GUID
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLFS_INFORMATION
            # Logical log file information structure describing either virtual
            # or physical log
            # file data, depending on the type of information queried.
            class _CLS_INFORMATION(ctypes.Structure):
                pass


            _CLS_INFORMATION._fields_ = [
                ('TotalAvailable', LONGLONG), # Total log data space available.
                ('CurrentAvailable', LONGLONG), # Usable space in the log file.
                ('TotalReservation', LONGLONG), # Space reserved for UNDO's (aggregate for physical log)
                ('BaseFileSize', ULONGLONG), # Size of the base log file.
                ('ContainerSize', ULONGLONG), # Uniform size of log containers.
                ('TotalContainers', ULONG), # Total number of containers.
                ('FreeContainers', ULONG), # Number of containers not in active log.
                ('TotalClients', ULONG), # Total number of clients.
                ('Attributes', ULONG), # Log file attributes.
                ('FlushThreshold', ULONG), # Log file flush threshold.
                ('SectorSize', ULONG), # Underlying container sector size.
                ('MinArchiveTailLsn', CLS_LSN), # Marks the global archive tail.
                ('BaseLsn', CLS_LSN), # Start of the active log region.
                ('LastFlushedLsn', CLS_LSN), # Last flushed LSN in active log.
                ('LastLsn', CLS_LSN), # End of active log region.
                ('RestartLsn', CLS_LSN), # Location of restart record.
                ('Identity', GUID), # Unique identifier for the log.
            ]
            CLS_INFORMATION = _CLS_INFORMATION
            PCLS_INFORMATION = POINTER(_CLS_INFORMATION)
            PPCLS_INFORMATION = POINTER(_CLS_INFORMATION)
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # Alias CLS prefixes with CLS prefixes.
            CLFS_INFORMATION = CLS_INFORMATION
            PCLFS_INFORMATION = POINTER(CLFS_INFORMATION)
            PPCLFS_INFORMATION = POINTER(CLFS_INFORMATION)
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        # CLFS_CLIENT_INFORMATION
        # The client information structure
        # maintains client - based log metadata.
        # typedef struct _CLS_CLIENT_INFORMATION
        # {
        # CLS_INFORMATION ClfsInfo; Contains base log file information.
        # ULONG ClientAttributes; Virtual log file attributes.
        # LONGLONG ClientUndoCommitment; Max. undo commitment for client.
        # CLS_LSN ClientArchiveTailLsn; Marks the client archive tail.
        # CLS_LSN ClientBaseLsn; Min. client LSN in active log region.
        # CLS_LSN ClientLastLsn; Max. client LSN in active log region.
        # CLS_LSN ClientRestartLsn; Location of restart record.
        # } CLS_CLIENT_INFORMATION, *PCLS_CLIENT_INFORMATION, **PPCLS_CLIENT_INFORMATION;
        #
        # Alias CLS prefixes with CLS prefixes.
        # typedef CLS_CLIENT_INFORMATION CLFS_CLIENT_INFORMATION;
        # typedef CLFS_CLIENT_INFORMATION *PCLFS_CLIENT_INFORMATION, *PPCLFS_CLIENT_INFORMATION;
        #
        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLFS_LOG_NAME_INFORMATION
            #
            # The client information structure stores the name of a log. It is
            # used
            # to communicate ClfsLogNameInformation and
            # ClfsLogPhysicalNameInformation.
            class _CLFS_LOG_NAME_INFORMATION(ctypes.Structure):
                pass


            _CLFS_LOG_NAME_INFORMATION._fields_ = [
                ('NameLengthInBytes', USHORT),
                ('Name', WCHAR * 1),
            ]
            CLFS_LOG_NAME_INFORMATION = _CLFS_LOG_NAME_INFORMATION
            PCLFS_LOG_NAME_INFORMATION = POINTER(_CLFS_LOG_NAME_INFORMATION)
            PPCLFS_LOG_NAME_INFORMATION = POINTER(POINTER(_CLFS_LOG_NAME_INFORMATION))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLFS_STREAM_ID_INFORMATION
            #
            # The client information structure provides a permanent identifier
            # unique
            # to the log for the stream in question.
            class _CLFS_STREAM_ID_INFORMATION(ctypes.Structure):
                pass


            _CLFS_STREAM_ID_INFORMATION._fields_ = [
                ('StreamIdentifier', UCHAR),
            ]
            CLFS_STREAM_ID_INFORMATION = _CLFS_STREAM_ID_INFORMATION
            PCLFS_STREAM_ID_INFORMATION = POINTER(_CLFS_STREAM_ID_INFORMATION)
            PPCLFS_STREAM_ID_INFORMATION = POINTER(POINTER(_CLFS_STREAM_ID_INFORMATION))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_VISTA or _WIN32_WINNT >= _WIN32_WINNT_LONGHORN:

            # CLFS_PHYSICAL_LSN_INFORMATION
            #
            # An information structure that describes a virtual:physical LSN
            # pairing
            # for the stream identified in the structure.
            class _CLFS_PHYSICAL_LSN_INFORMATION(ctypes.Structure):
                pass


            _CLFS_PHYSICAL_LSN_INFORMATION._fields_ = [
                ('StreamIdentifier', UCHAR),
                ('VirtualLsn', CLFS_LSN),
                ('PhysicalLsn', CLFS_LSN),
            ]
            CLFS_PHYSICAL_LSN_INFORMATION = _CLFS_PHYSICAL_LSN_INFORMATION
            PCLFS_PHYSICAL_LSN_INFORMATION = POINTER(_CLFS_PHYSICAL_LSN_INFORMATION)
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLS_CONTAINER_STATE
            # At any point in time a container could be inactive or
            # uninitialized, active,
            # pending deletion from the list of free containers, pending
            # archival, or
            # pending deletion while waiting to be archived.
            CLS_CONTAINER_STATE = UINT32
            PCLS_CONTAINER_STATE = POINTER(UINT32)
            PPCLS_CONTAINER_STATE = POINTER(UINT32)
            CLFS_CONTAINER_STATE = CLS_CONTAINER_STATE
            PCLFS_CONTAINER_STATE = POINTER(CLS_CONTAINER_STATE)
            PPCLFS_CONTAINER_STATE = POINTER(CLS_CONTAINER_STATE)
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if defined(__cplusplus):
            if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
                ClsContainerInitializing = 0x01
                ClsContainerInactive = 0x02
                ClsContainerActive = 0x04
                ClsContainerActivePendingDelete = 0x08
                ClsContainerPendingArchive = 0x10
                ClsContainerPendingArchiveAndDelete = 0x20
                ClfsContainerInitializing = 0x01
                ClfsContainerInactive = 0x02
                ClfsContainerActive = 0x04
                ClfsContainerActivePendingDelete = 0x08
                ClfsContainerPendingArchive = 0x10
                ClfsContainerPendingArchiveAndDelete = 0x20
            # END IF  NTDDI_VERSION or _WIN32_WINNT
        else:
            if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
                ClsContainerInitializing = 0x01
                ClsContainerInactive = 0x02
                ClsContainerActive = 0x04
                ClsContainerActivePendingDelete = 0x08
                ClsContainerPendingArchive = 0x10
                ClsContainerPendingArchiveAndDelete = 0x20
                ClfsContainerInitializing = 0x01
                ClfsContainerInactive = 0x02
                ClfsContainerActive = 0x04
                ClfsContainerActivePendingDelete = 0x08
                ClfsContainerPendingArchive = 0x10
                ClfsContainerPendingArchiveAndDelete = 0x20
            # END IF  NTDDI_VERSION or _WIN32_WINNT
        # END IF  __cplusplus

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLFS_MAX_CONTAINER_INFO
            # The maximum length, in bytes, of the FileName field in the CLFS
            # container information structure.
            if defined(__cplusplus):
                CLFS_MAX_CONTAINER_INFO = 256
            else:
                CLFS_MAX_CONTAINER_INFO = 256
            # END IF  __cplusplus
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLS_CONTAINER_INFORMATION
            # This structure defines a container descriptor. The descriptor
            # specifies the
            # container's creation and access times, size, file system name,
            # file system
            # attributes, state, minimum, and maximum LSNs.
            class _CLS_CONTAINER_INFORMATION(ctypes.Structure):
                pass


            _CLS_CONTAINER_INFORMATION._fields_ = [
                ('FileAttributes', ULONG), # File system attribute flag.
                ('CreationTime', ULONGLONG), # File creation time.
                ('LastAccessTime', ULONGLONG), # Last time container was read/written.
                ('LastWriteTime', ULONGLONG), # Last time container was written.
                ('ContainerSize', LONGLONG), # Size of container in bytes.
                ('FileNameActualLength', ULONG), # Length of the actual file name.
                ('FileNameLength', ULONG), # Length of file name in buffer
                ('FileName', WCHAR * CLFS_MAX_CONTAINER_INFO), # File system name for container.
                ('State', CLFS_CONTAINER_STATE), # Current state of the container.
                ('PhysicalContainerId', CLFS_CONTAINER_ID), # Physical container identifier.
                ('LogicalContainerId', CLFS_CONTAINER_ID), # Logical container identifier.
            ]
            CLS_CONTAINER_INFORMATION = _CLS_CONTAINER_INFORMATION
            PCLS_CONTAINER_INFORMATION = POINTER(_CLS_CONTAINER_INFORMATION)
            PPCLS_CONTAINER_INFORMATION = POINTER(POINTER(_CLS_CONTAINER_INFORMATION))

            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_CONTAINER_INFORMATION = CLS_CONTAINER_INFORMATION
            PCLFS_CONTAINER_INFORMATION = POINTER(CLFS_CONTAINER_INFORMATION)
            PPCLFS_CONTAINER_INFORMATION = POINTER(POINTER(CLFS_CONTAINER_INFORMATION))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:

            # CLFS_LOG_INFORMATION_CLASS
            # The information class specifies the kind of information a caller
            # wishes to query or set on a log file.
            class _CLS_LOG_INFORMATION_CLASS(ENUM):

                # For virtual or physical logs, indicates the respective basic
                # information.
                ClfsLogBasicInformation = 0x00
                ClfsLogBasicInformationPhysical = 1
                ClfsLogPhysicalNameInformation = 2
                ClfsLogStreamIdentifierInformation = 3
            if NTDDI_VERSION >= NTDDI_VISTA or _WIN32_WINNT >= _WIN32_WINNT_LONGHORN:
                ClfsLogSystemMarkingInformation = 4
                # Maps virtual LSNs to physical LSNs; only valid for physical
                # logs.
                ClfsLogPhysicalLsnInformation = 5
            # END IF


            CLS_LOG_INFORMATION_CLASS = _CLS_LOG_INFORMATION_CLASS
            PCLS_LOG_INFORMATION_CLASS = POINTER(_CLS_LOG_INFORMATION_CLASS)
            PPCLS_LOG_INFORMATION_CLASS = POINTER(POINTER(_CLS_LOG_INFORMATION_CLASS))

            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_LOG_INFORMATION_CLASS = CLS_LOG_INFORMATION_CLASS
            PCLFS_LOG_INFORMATION_CLASS = POINTER(CLFS_LOG_INFORMATION_CLASS)
            PPCLFS_LOG_INFORMATION_CLASS = POINTER(POINTER(CLFS_LOG_INFORMATION_CLASS))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLS_IOSTATS_CLASS
            # Enumerated type defining the class of I/O statistics.
            class _CLS_IOSTATS_CLASS(ENUM):
                ClsIoStatsDefault = 0x0000
                ClsIoStatsMax = 0xFFFF


            CLS_IOSTATS_CLASS = _CLS_IOSTATS_CLASS
            PCLS_IOSTATS_CLASS = POINTER(_CLS_IOSTATS_CLASS)
            PPCLS_IOSTATS_CLASS = POINTER(POINTER(_CLS_IOSTATS_CLASS))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:

            # CLFS_IOSTATS_CLASS
            # Alias all CLS prefixes with CLFS prefixes.
            class _CLFS_IOSTATS_CLASS(ENUM):
                ClfsIoStatsDefault = 0x0000
                ClfsIoStatsMax = 0xFFFF


            CLFS_IOSTATS_CLASS = _CLFS_IOSTATS_CLASS
            PCLFS_IOSTATS_CLASS = POINTER(_CLFS_IOSTATS_CLASS)
            PPCLFS_IOSTATS_CLASS = POINTER(POINTER(_CLFS_IOSTATS_CLASS))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLS_IO_STATISTICS
            # This structure defines I/O performance counters particular to a
            # log file. It consists
            # of a header followed by the I/O statistics counters. The header
            # is being ignored for
            # now.
            class _CLS_IO_STATISTICS_HEADER(ctypes.Structure):
                pass


            _CLS_IO_STATISTICS_HEADER._fields_ = [
                ('ubMajorVersion', UCHAR), # Major version of the statistics buffer.
                ('ubMinorVersion', UCHAR), # Minor version of the statistics buffer.
                ('eStatsClass', CLFS_IOSTATS_CLASS), # I/O statistics class.
                ('cbLength', USHORT), # Length of the statistics buffer.
                ('coffData', ULONG), # Offset of statistics counters.
            ]
            CLS_IO_STATISTICS_HEADER = _CLS_IO_STATISTICS_HEADER
            PCLS_IO_STATISTICS_HEADER = POINTER(_CLS_IO_STATISTICS_HEADER)
            PPCLS_IO_STATISTICS_HEADER = POINTER(POINTER(_CLS_IO_STATISTICS_HEADER))

            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_IO_STATISTICS_HEADER = CLS_IO_STATISTICS_HEADER
            PCLFS_IO_STATISTICS_HEADER = POINTER(CLFS_IO_STATISTICS_HEADER)
            PPCLFS_IO_STATISTICS_HEADER = POINTER(POINTER(CLFS_IO_STATISTICS_HEADER))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            class _CLS_IO_STATISTICS(ctypes.Structure):
                pass


            _CLS_IO_STATISTICS._fields_ = [
                ('hdrIoStats', CLS_IO_STATISTICS_HEADER), # Statistics buffer header.
                ('cFlush', ULONGLONG), # Flush count.
                ('cbFlush', ULONGLONG), # Cumulative number of bytes flushed.
                ('cMetaFlush', ULONGLONG), # Metadata flush count.
                ('cbMetaFlush', ULONGLONG), # Cumulative number of metadata bytes flushed.
            ]
            CLS_IO_STATISTICS = _CLS_IO_STATISTICS
            PCLS_IO_STATISTICS = POINTER(_CLS_IO_STATISTICS)
            PPCLS_IO_STATISTICS = POINTER(POINTER(_CLS_IO_STATISTICS))

            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_IO_STATISTICS = CLS_IO_STATISTICS
            PCLFS_IO_STATISTICS = POINTER(CLFS_IO_STATISTICS)
            PPCLFS_IO_STATISTICS = POINTER(POINTER(CLFS_IO_STATISTICS))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLFS_SCAN_MODE
            # Container scan mode flags.
            if defined(__cplusplus):
                pass
            else:
                CLFS_SCAN_INIT = 0x01
                CLFS_SCAN_FORWARD = 0x02
                CLFS_SCAN_BACKWARD = 0x04
                CLFS_SCAN_CLOSE = 0x08
                CLFS_SCAN_INITIALIZED = 0x10
                CLFS_SCAN_BUFFERED = 0x20
            # END IF

            CLFS_SCAN_MODE = UCHAR
            PCLFS_SCAN_MODE = POINTER(UCHAR)
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # CLFS_SCAN_CONTEXT
            # Container scan context for scanning all containers in a given
            # physical log
            # file.
            # The log file object wraps an NT file object and the size of the
            # structure.
            # The log file object may be modified in the near future and there
            # should be no
            # dependencies on the size of the structure itself.
            LOG_FILE_OBJECT = FILE_OBJECT
            PLOG_FILE_OBJECT = POINTER(FILE_OBJECT)
            PPLOG_FILE_OBJECT = POINTER(POINTER(FILE_OBJECT))


            if defined(_MSC_VER):
                if _MSC_VER >= 1200:
                    pass
                # END IF
            # END IF

            class _CLS_SCAN_CONTEXT(ctypes.Structure):
                pass


            _CLS_SCAN_CONTEXT._fields_ = [
                ('cidNode', CLFS_NODE_ID),
                ('plfoLog', PLOG_FILE_OBJECT),
                ('ULONG cIndex', __declspec(align(8))),
                ('ULONG cContainers', __declspec(align(8))),
                ('ULONG cContainersReturned', __declspec(align(8))),
                ('CLFS_SCAN_MODE eScanMode', __declspec(align(8))),
                ('PCLS_CONTAINER_INFORMATION pinfoContainer', __declspec(align(8))),
            ]
            CLS_SCAN_CONTEXT = _CLS_SCAN_CONTEXT
            PCLS_SCAN_CONTEXT = POINTER(_CLS_SCAN_CONTEXT)
            PPCLS_SCAN_CONTEXT = POINTER(POINTER(_CLS_SCAN_CONTEXT))

            if defined(_MSC_VER):
                if _MSC_VER >= 1200:
                    pass
                # END IF
            # END IF
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:

            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_SCAN_CONTEXT = CLS_SCAN_CONTEXT
            PCLFS_SCAN_CONTEXT = POINTER(CLFS_SCAN_CONTEXT)
            PPCLFS_SCAN_CONTEXT = POINTER(POINTER(CLFS_SCAN_CONTEXT))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:

            # CLFS_ARCHIVE_DESCRIPTOR
            # Log archive descriptors describe the set of discrete but
            # logically
            # contiguous disk extents comprising a snapshot of the active log
            # when
            # preparing for archival. Log archive descriptors specify enough
            # information
            # for log archive clients directly access the relevant contents of
            # containers
            # for archiving and restoring a snapshot of the log.
            class _CLS_ARCHIVE_DESCRIPTOR(ctypes.Structure):
                pass


            _CLS_ARCHIVE_DESCRIPTOR._fields_ = [
                ('coffLow', ULONGLONG),
                ('coffHigh', ULONGLONG),
                ('infoContainer', CLS_CONTAINER_INFORMATION),
            ]
            CLS_ARCHIVE_DESCRIPTOR = _CLS_ARCHIVE_DESCRIPTOR
            PCLS_ARCHIVE_DESCRIPTOR = POINTER(_CLS_ARCHIVE_DESCRIPTOR)
            PPCLS_ARCHIVE_DESCRIPTOR = POINTER(POINTER(_CLS_ARCHIVE_DESCRIPTOR))

            # Alias CLS prefixes with CLFS prefixes.
            CLFS_ARCHIVE_DESCRIPTOR = CLS_ARCHIVE_DESCRIPTOR
            PCLFS_ARCHIVE_DESCRIPTOR = POINTER(CLFS_ARCHIVE_DESCRIPTOR)
            PPCLFS_ARCHIVE_DESCRIPTOR = POINTER(POINTER(CLFS_ARCHIVE_DESCRIPTOR))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:

            # CLFS_ALLOCATION_ROUTINE
            # Allocate a blocks for marshaled reads or writes
            # typedef PVOID (* CLFS_BLOCK_ALLOCATION) (ULONG cbBufferLength, PVOID pvUserContext);
            CLFS_BLOCK_ALLOCATION = CALLBACK(PVOID, ULONG, PVOID)


            # CLFS_DEALLOCATION_ROUTINE
            # Deallocate buffers allocated by the CLFS_ALLOCATION_ROUTINE.
            # typedef void (* CLFS_BLOCK_DEALLOCATION) (PVOID pvBuffer, PVOID pvUserContext);
            CLFS_BLOCK_DEALLOCATION = CALLBACK(VOID, PVOID, PVOID)

        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:

            # CLFS_LOG_ARCHIVE_MODE
            # Describes the archive support behavior for the log.
            class _CLFS_LOG_ARCHIVE_MODE(ENUM):
                ClfsLogArchiveEnabled = 0x01
                ClfsLogArchiveDisabled = 0x02


            CLFS_LOG_ARCHIVE_MODE = _CLFS_LOG_ARCHIVE_MODE
            PCLFS_LOG_ARCHIVE_MODE = POINTER(_CLFS_LOG_ARCHIVE_MODE)
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # - - - - - - - - -
        # LSN OPERATORS
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # - - - - - - - - -
        if defined(__cplusplus):
            pass
        # END IF

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # ClfsLsnLess
            # Method Description:
            # Check if LSN1 is less than LSN2.
            # Arguments:
            # plsn1 - - first LSN comparator
            # plsn2 - - second LSN comparator
            #
            # Return Value:
            # TRUE if LSN1 is less than LSN2 and FALSE otherwise.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        #  END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # ClfsLsnGreater
            # Method Description:
            # Check if LSN1 is greater than LSN2.
            # Arguments:
            # plsn1 - - first LSN comparator
            # plsn2 - - second LSN comparator
            #
            # Return Value:
            # TRUE if LSN1 is greater than LSN2 and FALSE otherwise.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # ClfsLsnNull (Inline)
            # Method Description:
            # Check whether or not an LSN is CLFS_LSN_NULL.
            # Arguments:
            # plsn  - - reference to LSN tested against the NULL value.
            #
            # Return Value:
            # TRUE if and only if an LSN is equivalent to CLFS_LSN_NULL.
            # LSNs with the value CLFS_LSN_INVALID will return FALSE.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # ClfsLsnContainer (Inline)
            # Routine Description:
            # Extract the container identifier from the LSN.
            # Arguments:
            # plsn - - get block offset from this LSN
            # Return Value:
            # Returns the container identifier for the LSN.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # ClfsLsnCreate (Inline)
            # Routine Description:
            # Create an LSN given a log identifier, a container identifier, a
            # block
            # offset and a bucket identifier. Caller must test for invalid LSN
            # after
            # making this call.
            # Arguments:
            # cidContainer  - - container identifier
            # offBlock  - - block offset
            # cRecord  - - ordinal number of the record in block
            # Return Value:
            # Returns a valid LSN if successful, otherwise it returns
            # CLFS_LSN_INVALID
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # ClfsLsnBlockOffset (Inline)
            # Routine Description:
            # Extract the block offset from the LSN.
            # Arguments:
            # plsn - - get block offset from this LSN
            # Return Value:
            # Returns the block offset for the LSN.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # ClfsLsnRecordSequence (Inline)
            # Routine Description:
            # Extract the bucket identifier from the LSN.
            # Arguments:
            # plsn  - - get block offset from this LSN
            # Return Value:
            # Returns the bucket identifier for the LSN.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # ClfsLsnInvalid
            # Method Description:
            # Check whether or not an LSN is CLFS_LSN_INVALID.
            # Arguments:
            # plsn  - - reference to LSN tested against CLFS_LSN_INVALID.
            #
            # Return Value:
            # TRUE if and only if an LSN is equivalent to CLFS_LSN_INVALID.
            # LSNs with the value CLFS_LSN_NULL will return FALSE.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # ClfsLsnIncrement
            # Method Description:
            # Increment and LSN by 1
            # Arguments:
            # plsn - - LSN to be incremented.
            #
            # Return Value:
            # A valid LSN next in sequence to the input LSN, if successful.
            # Otherwise, this function returns CLFS_LSN_INVALID.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if defined(__cplusplus):
            pass
        # END IF

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if defined(__cplusplus):
            pass
        # END IF

        if defined(__cplusplus):
            if defined(CLFS_OPERATORS):
                pass
            # END IF  CLFS_OPERATORS
        # END IF  __cplusplus
    # END IF  _CLFS_PUBLIC_H_

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        class _CLFS_MGMT_POLICY_TYPE(ENUM):
            ClfsMgmtPolicyMaximumSize = 0x0
            ClfsMgmtPolicyMinimumSize = 0x1
            ClfsMgmtPolicyNewContainerSize = 0x2
            ClfsMgmtPolicyGrowthRate = 0x3
            ClfsMgmtPolicyLogTail = 0x4
            ClfsMgmtPolicyAutoShrink = 0x5
            ClfsMgmtPolicyAutoGrow = 0x6
            ClfsMgmtPolicyNewContainerPrefix = 0x7
            ClfsMgmtPolicyNewContainerSuffix = 0x8
            ClfsMgmtPolicyNewContainerExtension = 0x9
            ClfsMgmtPolicyInvalid = 0x0a
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        CLFS_MGMT_NUM_POLICIES = _CLFS_MGMT_POLICY_TYPE.ClfsMgmtPolicyInvalid
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # Relative sizes used when explicitly setting log size.
        CLFS_LOG_SIZE_MINIMUM = 0
        CLFS_LOG_SIZE_MAXIMUM = -1
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # The version of a given policy structure. See CLFS_MGMT_POLICY.
        CLFS_MGMT_POLICY_VERSION = 0x01
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # Log policy flags.
        # LOG_POLICY_OVERWRITE: If set when adding a log policy, the previous
        # policy of given type will be replaced.
        # LOG_POLICY_PERSIST: If set when adding a log policy, the policy
        # will be persisted with the log metadata.
        LOG_POLICY_OVERWRITE = 0x01
        LOG_POLICY_PERSIST = 0x02
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # CLFS_MGMT_POLICY
        # This structure describes one particular policy that
        # may be present on a log file. These are installed
        # via InstallLogPolicy (Win32) or ClfsMgmtInstallPolicy (kernel).

        class _CLFS_MGMT_POLICY(ctypes.Structure):
            pass


        class PolicyParameters(ctypes.Structure):
            pass


        class MaximumSize(ctypes.Structure):
            pass


        MaximumSize._fields_ = [
            ('Containers', ULONG),
        ]
        PolicyParameters.MaximumSize = MaximumSize


        class MinimumSize(ctypes.Structure):
            pass


        MinimumSize._fields_ = [
            ('Containers', ULONG),
        ]
        PolicyParameters.MinimumSize = MinimumSize


        class NewContainerSize(ctypes.Structure):
            pass


        NewContainerSize._fields_ = [
            ('SizeInBytes', ULONG),
        ]
        PolicyParameters.NewContainerSize = NewContainerSize


        class GrowthRate(ctypes.Structure):
            pass


        GrowthRate._fields_ = [
            ('AbsoluteGrowthInContainers', ULONG),
            ('RelativeGrowthPercentage', ULONG),
        ]
        PolicyParameters.GrowthRate = GrowthRate


        class LogTail(ctypes.Structure):
            pass


        LogTail._fields_ = [
            ('MinimumAvailablePercentage', ULONG),
            ('MinimumAvailableContainers', ULONG),
        ]
        PolicyParameters.LogTail = LogTail


        class AutoShrink(ctypes.Structure):
            pass


        AutoShrink._fields_ = [
            ('Percentage', ULONG),
        ]
        PolicyParameters.AutoShrink = AutoShrink


        class AutoGrow(ctypes.Structure):
            pass


        AutoGrow._fields_ = [
            ('Enabled', ULONG),
        ]
        PolicyParameters.AutoGrow = AutoGrow


        class NewContainerPrefix(ctypes.Structure):
            pass


        NewContainerPrefix._fields_ = [
            ('PrefixLengthInBytes', USHORT),
            ('PrefixString', WCHAR * 1),
            # dynamic in length depending on PrefixLength
        ]
        PolicyParameters.NewContainerPrefix = NewContainerPrefix


        class NewContainerSuffix(ctypes.Structure):
            pass


        NewContainerSuffix._fields_ = [
            ('NextContainerSuffix', ULONGLONG),
        ]
        PolicyParameters.NewContainerSuffix = NewContainerSuffix


        class NewContainerExtension(ctypes.Structure):
            pass


        NewContainerExtension._fields_ = [
            ('ExtensionLengthInBytes', USHORT),
            ('ExtensionString', WCHAR * 1),
            # dynamic in length depending on ExtensionLengthInBytes
        ]
        PolicyParameters.NewContainerExtension = NewContainerExtension
        PolicyParameters._fields_ = [
            ('MaximumSize', PolicyParameters.MaximumSize),
            ('MinimumSize', PolicyParameters.MinimumSize),
            ('NewContainerSize', PolicyParameters.NewContainerSize),
            ('GrowthRate', PolicyParameters.GrowthRate),
            ('LogTail', PolicyParameters.LogTail),
            ('AutoShrink', PolicyParameters.AutoShrink),
            ('AutoGrow', PolicyParameters.AutoGrow),
            ('NewContainerPrefix', PolicyParameters.NewContainerPrefix),
            ('NewContainerSuffix', PolicyParameters.NewContainerSuffix),
            ('NewContainerExtension', PolicyParameters.NewContainerExtension),
        ]
        _CLFS_MGMT_POLICY.PolicyParameters = PolicyParameters
        _CLFS_MGMT_POLICY._fields_ = [
            ('Version', ULONG),
            # Version of the structure. Should be CLFS_MGMT_POLICY_VERSION.
            ('LengthInBytes', ULONG),  # The entire length of the structure.
            ('PolicyFlags', ULONG),  # and LOG_POLICY_PERSIST.
            ('PolicyType', CLFS_MGMT_POLICY_TYPE),
            # Determines how PolicyParameters union is interpreted.
            ('PolicyParameters', _CLFS_MGMT_POLICY.PolicyParameters),
            # MaximumSize structure is the relevant one.
        ]
        CLFS_MGMT_POLICY = _CLFS_MGMT_POLICY
        PCLFS_MGMT_POLICY = POINTER(_CLFS_MGMT_POLICY)
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # CLFS_MGMT_NOTIFICATION_TYPE
        #
        # The types of notifications given to either the callback proxy
        # or to readers of notifications.
        class _CLFS_MGMT_NOTIFICATION_TYPE(ENUM):
            ClfsMgmtAdvanceTailNotification = 0
            ClfsMgmtLogFullHandlerNotification = 1
            ClfsMgmtLogUnpinnedNotification = 2
            ClfsMgmtLogWriteNotification = 3


        CLFS_MGMT_NOTIFICATION_TYPE = _CLFS_MGMT_NOTIFICATION_TYPE
        PCLFS_MGMT_NOTIFICATION_TYPE = POINTER(_CLFS_MGMT_NOTIFICATION_TYPE)
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # CLFS_MGMT_NOTIFICATION
        # A notification and associated parameters.
        class _CLFS_MGMT_NOTIFICATION(ctypes.Structure):
            pass


        _CLFS_MGMT_NOTIFICATION._fields_ = [
            ('Notification', CLFS_MGMT_NOTIFICATION_TYPE),
            # Nature of the notification.
            ('Lsn', CLFS_LSN),
            # notification type is ClfsMgmtAdvanceTailNotification.
            ('LogIsPinned', USHORT),
            # status for ClfsMgmtLogFullHandlerNotification.
        ]
        CLFS_MGMT_NOTIFICATION = _CLFS_MGMT_NOTIFICATION
        PCLFS_MGMT_NOTIFICATION = POINTER(_CLFS_MGMT_NOTIFICATION)
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    # Kernel interface described below.
    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # The advance tail callback is required when log clients
        # register for management. It is invoked whenever the
        # management library decides that this client needs to
        # advance the tail of its log. Only minimal processing is
        # allowed.

        # typedef
        # NTSTATUS
        # (*PCLFS_CLIENT_ADVANCE_TAIL_CALLBACK) (
        # _In_ PLOG_FILE_OBJECT LogFile,
        # _In_ PCLFS_LSN TargetLsn,
        # _In_ PVOID ClientData
        # );
        PCLFS_CLIENT_ADVANCE_TAIL_CALLBACK = CALLBACK(
            NTSTATUS,
            PLOG_FILE_OBJECT,
            PCLFS_LSN,
            PVOID
        )
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # The log file full handler complete callback is invoked upon
        # completion of a log growth request (that is, via a call
        # to ClfsMgmtHandleLogFileFull).

        # typedef
        # VOID
        # (*PCLFS_CLIENT_LFF_HANDLER_COMPLETE_CALLBACK) (
        # _In_ PLOG_FILE_OBJECT LogFile,
        # _In_ NTSTATUS OperationStatus,
        # _In_ BOOLEAN LogIsPinned,
        # _In_ PVOID ClientData
        # );
        PCLFS_CLIENT_LFF_HANDLER_COMPLETE_CALLBACK = CALLBACK(
            VOID,
            PLOG_FILE_OBJECT,
            NTSTATUS,
            BOOLEAN,
            PVOID
        )

    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # The log pinned callback is invoked when log space is freed up
        # after a log file full handler completion callback indicates an
        # NT_ERROR status code and LogIsPinned = TRUE.

        # typedef
        # VOID
        # (*PCLFS_CLIENT_LOG_UNPINNED_CALLBACK) (
        # _In_ PLOG_FILE_OBJECT LogFile,
        # _In_ PVOID ClientData
        # );
        PCLFS_CLIENT_LOG_UNPINNED_CALLBACK = CALLBACK(
            VOID,
            PLOG_FILE_OBJECT,
            PVOID
        )
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # The log size complete callback is invoked whenever
        # ClfsMgmtSetLogFileSize operation which returned
        # STATUS_PENDING is completed.

        # typedef
        # VOID
        # (*PCLFS_SET_LOG_SIZE_COMPLETE_CALLBACK) (
        # _In_ PLOG_FILE_OBJECT LogFile,
        # _In_ NTSTATUS OperationStatus,
        # _In_ PVOID ClientData
        # );
        PCLFS_SET_LOG_SIZE_COMPLETE_CALLBACK = CALLBACK(
            VOID,
            PLOG_FILE_OBJECT,
            NTSTATUS,
            PVOID
        )
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # CLFS_MGMT_CLIENT_REGISTRATION
        # This structure is given to the CLFS management infrastructure
        # by clients who wish to be managed
        # (via ClfsMgmtRegisterManagedClient).
        # The CLFS_MGMT_CLIENT_REGISTRATION_VERSION value must be stored
        # in the 'Version' field of the structure.

        CLFS_MGMT_CLIENT_REGISTRATION_VERSION = 0x1


        class _CLFS_MGMT_CLIENT_REGISTRATION(ctypes.Structure):
            pass


        _CLFS_MGMT_CLIENT_REGISTRATION._fields_ = [
            ('Version', ULONG),
            # Initialize Version to CLFS_MGMT_CLIENT_REGISTRATION_VERSION.
            ('AdvanceTailCallback', PCLFS_CLIENT_ADVANCE_TAIL_CALLBACK),
            ('AdvanceTailCallbackData', PVOID),
            ('LogGrowthCompleteCallback',
            PCLFS_CLIENT_LFF_HANDLER_COMPLETE_CALLBACK),
            ('LogGrowthCompleteCallbackData', PVOID),
            ('LogUnpinnedCallback', PCLFS_CLIENT_LOG_UNPINNED_CALLBACK),
            ('LogUnpinnedCallbackData', PVOID),
        ]
        CLFS_MGMT_CLIENT_REGISTRATION = _CLFS_MGMT_CLIENT_REGISTRATION
        PCLFS_MGMT_CLIENT_REGISTRATION = POINTER(_CLFS_MGMT_CLIENT_REGISTRATION)
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        # CLFS_MGMT_CLIENT
        # This is the cookie that clients are given when registering and
        # must give back to the management infrastructure whenever
        # performing an operation.
        CLFS_MGMT_CLIENT = PVOID
        PCLFS_MGMT_CLIENT = POINTER(PVOID)
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        pass
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        pass
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        pass
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        pass
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        pass
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        pass
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        pass
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_WS03SP1 or _WIN32_WINNT >= _WIN32_WINNT_WS03:
        pass
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if NTDDI_VERSION >= NTDDI_VISTA or _WIN32_WINNT >= _WIN32_WINNT_LONGHORN:
        pass
    # END IF  NTDDI_VERSION or _WIN32_WINNT

    if defined(__cplusplus):
        pass
    # END IF

    if not defined(__CLFSPROC_H__):
        __CLFSPROC_H__ = 0

        if defined(__cplusplus):
            pass
        # END IF  __cplusplus

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsFinalize
            # Utility to cleanup CLFS global resources, lookaside lists, and
            # memory.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsCreateLogFile
            # Entry point to create a physical log file consisting of
            # uniformly sized
            # containers lying in a given directory path.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsDeleteLogByPointer
            # Entry point to delete a physical log file and its underlying
            # container
            # storage referencing a log file object.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        #  END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsDeleteLogFile
            # Entry point to delete a physical log file and its underlying
            # container
            # storage by name.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION
        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsAddLogContainer
            # Adds a log container to a given physical file identified by the
            # log
            # file object pointer.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsAddLogContainerSet
            # Adds a set of log containers to a given physical file identified
            # by the log
            # file object pointer.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsRemoveLogContainer
            # Removes a log container from a physical log file identified by
            # the log file object pointer.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsRemoveLogContainerSet
            # Removes a set of log containers from a physical log file
            # identified by
            # the log file object pointer.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsSetArchiveTail
            # Sets the archive tail for either a client or physical log file
            # depending on the type of the log handle.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsSetEndOfLog
            # Sets the end of log for either a client or physical log file
            # depending on the type of the log handle.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsCreateScanContext
            # Create a scan context to enumerate scan descriptors for storage
            # containers
            # that back the physical log file object.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsScanLogContainers
            # Scan descriptors for storage containers backing the physical
            # log file stream.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsGetContainerName
            # ClfsGetContainerName gets the full path name of a container
            # given its logical
            # container identifier.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsGetLogFileInformation
            # Get log file information for a physical log and client stream
            # specific to the log file object pointer.
            # Deprecated. Use ClfsQueryLogFileInformation instead
            # (it is equivalent
            # to this call if ClfsLogBasicInformation is used as information
            # class).
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_VISTA:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsQueryLogFileInformation
            # Get log file information for a physical log and client stream
            # specific to the log file object pointer.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsSetLogFileInformation
            # Sets log file information for a physical log and client stream
            # specific to the log file object pointer.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsReadRestartArea
            # Read the last restart area successfully written to a physical or
            # client log stream given a marshaling context.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsReadPreviousRestartArea
            # Read the previous restart area successfully written to a
            # physical or
            # client log stream given the read context created by the a call to
            # ClfsReadRestartArea.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsWriteRestartArea
            # Write a new restart area to a physical or client log stream
            # given a
            # a marshaling context.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsAdvanceLogBase
            # Set a new log base LSN without writing a restart record.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsCloseAndResetLogFile
            # Orderly shutdown of a physical or client log file stream given
            # the log file
            # object pointer.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsCloseLogFileObject
            # Close a log file object without the orderly shutdown of the log.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsCreateMarshallingArea
            # Initialize a marshaling area for a physical or client log
            # file stream given log file object pointer.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WIN8:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsCreateMarshallingAreaEx
            # Extended version of ClfsCreateMarshallingArea to Initialize a
            # marshaling area.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsDeleteMarshallingArea
            # Delete a marshaling area for a physical or client log
            # file stream.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsReserveAndAppendLog
            # Reserve space and append log buffers to a physical or client
            # log stream.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsReserveAndAppendLogAligned
            # Reserve space and append log buffers to a physical or client
            # log stream, aligning each of the write entries according to
            # the alignment specified.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsAlignReservedLog
            # Given a valid marshaling context, allocate an aggregate number
            # of reserved
            # records and bytes.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsAllocReservedLog
            # Given a valid marshaling context, allocate an aggregate number
            # of reserved
            # records and bytes.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsFreeReservedLog
            # Set the reserved log space to a new size or specify a delta
            # for the reserved space given log file.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsFlushBuffers
            #
            # Append all buffers in the marshaling area up to the flush queue
            # and flush
            # all buffers up to the disk.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsFlushToLsn
            #
            # Flush all buffers in the marshaling area up to a target LSN to
            # the flush
            # queue and flush all buffers up to the target LSN to the disk.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsReadLogRecord
            # Read a log record from a physical or client log stream given
            # a starting LSN.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsReadNextLogRecord
            # Read the next log record from a given marshaling context.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsTerminateReadLog
            # Terminate the read context.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsGetLastLsn
            # Get the last used LSN.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            # ClfsGetIoStatistics
            # Get I/O statistics on the CLFS log file.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # ClfsLaterLsn
            # Method Description:
            # Increment an LSN by 1
            # Arguments:
            # plsn - - LSN to be incremented.
            #
            # Return Value:
            # A valid LSN next in sequence to the input LSN, if successful.
            # Otherwise, this function returns CLFS_LSN_INVALID.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            # ClfsEarlierLsn
            # Method Description:
            # Decrement an LSN by 1
            # Arguments:
            # plsn - - LSN to be decremented.
            #
            # Return Value:
            # A valid LSN next in sequence to the input LSN, if successful.
            # Otherwise, this function returns CLFS_LSN_INVALID.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - -
            # ClfsLsnDifference
            # Method Description:
            # Find the approximate number of bytes between two LSNs.
            # Arguments:
            # plsnStart  - - LSN start of the log file range
            # plsnFinish  - - LSN finish of the log file range
            # cbContainer - - size of a container
            # cbMaxBlock  - - maximum size of an I/O block
            # pcbDifference - - approximate number of bytes between two LSNs.
            #
            #
            # Return Value:
            # STATUS_SUCCESS if difference is succeeds and an error status
            # otherwise.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if NTDDI_VERSION >= NTDDI_VISTA:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - -
            # ClfsValidTopLevelContext
            # Method Description:
            # Check that the current top level context is a common log (CLFS)
            # context.
            # Arguments:
            # pirp   - - reference to top of top - level context stack
            #
            # Return Value:
            # TRUE if this is a valid CLFS top - level context and FALSE
            # otherwise.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - -
            pass
        # END IF  NTDDI_VERSION

        if defined(__cplusplus):
            pass
        # END IF  __cplusplus
    # END IF  __CLFSPROC_H__

    KTRANSACTION = _KTRANSACTION
    PRKENLISTMENT = POINTER(_KTRANSACTION)
    PRKRESOURCEMANAGER = POINTER(_KTRANSACTION)

    KENLISTMENT = _KENLISTMENT
    PKENLISTMENT = POINTER(_KENLISTMENT)
    PRKENLISTMENT = POINTER(_KENLISTMENT)

    KRESOURCEMANAGER = _KRESOURCEMANAGER
    PKRESOURCEMANAGER = POINTER(_KRESOURCEMANAGER)
    PRKRESOURCEMANAGER = POINTER(_KRESOURCEMANAGER)

    KTM = _KTM
    PKTM = POINTER(_KTM)
    PRKTM = POINTER(_KTM)

    UOW = GUID
    PUOW = POINTER(GUID)
    PGUID = POINTER(GUID)

    # Define ResourceManager Notification routine type.
    # CRM Protocol object
    KCRM_PROTOCOL_ID = GUID
    PKCRM_PROTOCOL_ID = POINTER(GUID)

    # Tm - level Transaction APIs
    # ResourceManager APIs
    PCW_VERSION_1 = 0x0100
    PCW_CURRENT_VERSION = PCW_VERSION_1

    PPCW_INSTANCE = POINTER(_PCW_INSTANCE)
    PPCW_REGISTRATION = POINTER(_PCW_REGISTRATION)
    PPCW_BUFFER = POINTER(_PCW_BUFFER)


    class _PCW_COUNTER_DESCRIPTOR(ctypes.Structure):
        pass


    _PCW_COUNTER_DESCRIPTOR._fields_ = [
        ('Id', USHORT),
        ('StructIndex', USHORT),
        ('Offset', USHORT),
        ('Size', USHORT),
    ]
    PCW_COUNTER_DESCRIPTOR = _PCW_COUNTER_DESCRIPTOR
    PPCW_COUNTER_DESCRIPTOR = POINTER(_PCW_COUNTER_DESCRIPTOR)


    class _PCW_DATA(ctypes.Structure):
        pass


    _PCW_DATA._fields_ = [
        ('Data', POINTER(VOID)),
        ('Size', ULONG),
    ]
    PCW_DATA = _PCW_DATA
    PPCW_DATA = POINTER(_PCW_DATA)


    class _PCW_COUNTER_INFORMATION(ctypes.Structure):
        pass


    _PCW_COUNTER_INFORMATION._fields_ = [
        ('CounterMask', ULONG64),
        ('InstanceMask', PCUNICODE_STRING),
    ]
    PCW_COUNTER_INFORMATION = _PCW_COUNTER_INFORMATION
    PPCW_COUNTER_INFORMATION = POINTER(_PCW_COUNTER_INFORMATION)


    class _PCW_MASK_INFORMATION(ctypes.Structure):
        pass


    _PCW_MASK_INFORMATION._fields_ = [
        ('CounterMask', ULONG64),
        ('InstanceMask', PCUNICODE_STRING),
        ('InstanceId', ULONG),
        ('CollectMultiple', BOOLEAN),
        ('Buffer', PPCW_BUFFER),
        ('CancelEvent', PKEVENT),
    ]
    PCW_MASK_INFORMATION = _PCW_MASK_INFORMATION
    PPCW_MASK_INFORMATION = POINTER(_PCW_MASK_INFORMATION)


    class _PCW_CALLBACK_INFORMATION(ctypes.Union):
        pass


    _PCW_CALLBACK_INFORMATION._fields_ = [
        ('AddCounter', PCW_COUNTER_INFORMATION),
        ('RemoveCounter', PCW_COUNTER_INFORMATION),
        ('EnumerateInstances', PCW_MASK_INFORMATION),
        ('CollectData', PCW_MASK_INFORMATION),
    ]
    PCW_CALLBACK_INFORMATION = _PCW_CALLBACK_INFORMATION
    PPCW_CALLBACK_INFORMATION = POINTER(_PCW_CALLBACK_INFORMATION)


    class _PCW_CALLBACK_TYPE(ENUM):
        PcwCallbackAddCounter = 0
        PcwCallbackRemoveCounter = 1
        PcwCallbackEnumerateInstances = 2
        PcwCallbackCollectData = 3


    PCW_CALLBACK_TYPE = _PCW_CALLBACK_TYPE
    PPCW_CALLBACK_TYPE = POINTER(_PCW_CALLBACK_TYPE)
    PPCW_CALLBACK = POINTER(PCW_CALLBACK)


    class _PCW_REGISTRATION_INFORMATION(ctypes.Structure):
        pass


    _PCW_REGISTRATION_INFORMATION._fields_ = [
        ('Version', ULONG),
        ('Name', PCUNICODE_STRING),
        ('CounterCount', ULONG),
        ('Counters', PPCW_COUNTER_DESCRIPTOR),
        ('PPCW_CALLBACK Callback', _In_opt_),
        ('PVOID CallbackContext', _In_opt_),
    ]
    PCW_REGISTRATION_INFORMATION = _PCW_REGISTRATION_INFORMATION
    PPCW_REGISTRATION_INFORMATION = POINTER(_PCW_REGISTRATION_INFORMATION)

    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS2:
        SECURE_SECTION_ALLOW_PARTIAL_MDL = 1
    # END IF

    if not defined(_OB_REFERENCE_TAGS_):
        _OB_REFERENCE_TAGS_ = 1

        # Object Manager Public Reference Tags
        REFTAG_AFDCONN = 'CdfA'
        REFTAG_AFDENDPOINT = 'EdfA'
        REFTAG_AFDPOLL = 'PdfA'
        REFTAG_ALEIO = 'IelA'
        REFTAG_ALEPROCTBL = 'PelA'
        REFTAG_ALESIDTOKEN = 'SelA'
        REFTAG_CFSFILTER = 'FsfC'
        REFTAG_DWMKERNEL = 'KmwD'
        REFTAG_HTTP = 'pttH'
        REFTAG_MAILSLOT = 'sFsM'
        REFTAG_NFSVOLUME = 'VsfN'
        REFTAG_PGMFILE = 'TmgP'
        REFTAG_PSLOOKUP = 'ULsP'
        REFTAG_PSNOTIFICATION = 'oNsP'
        REFTAG_PSWAKE = 'kWsP'
        REFTAG_RAWENDPOINT = 'EwaR'
        REFTAG_TCPENDPOINT = 'EpcT'
        REFTAG_TCPLISTENER = 'LpcT'
        REFTAG_TCPTCB = 'TpcT'
        REFTAG_UDPENDPOINT = 'EpdU'
        REFTAG_USRKDESKTOP = 'DrsU'
        REFTAG_VIDEO_PORT_I386 = 'idiV'
        REFTAG_VIDEO_PORT = 'PdiV'
        REFTAG_WIN32K = 'k23W'
        REFTAG_WIN32KQUEUE = 'q23W'
        REFTAG_WIN32KRESTRICT = 'r23W'
        REFTAG_WIN32KSERVER = 'S23W'
        REFTAG_WIN32KSTUBS = 's23W'
        REFTAG_WS2IFSL = 'i2sW'
        REFTAG_WSKNAMERES = 'NksW'
        REFTAG_WSKPROV = 'PksW'
        REFTAG_WSKTDI = 'TksW'
    # END IF   _OB_REFERENCE_TAGS_
    # Define possible flags to be passed to ExInitializeDriverRuntime. These
    # flags define the behavior of the driver runtime opt - in package.


    class _DRIVER_RUNTIME_INIT_FLAGS(ENUM):
        DrvRtPoolNxOptIn = 0x00000001
        LastDrvRtFlag = 2


    DRIVER_RUNTIME_INIT_FLAGS = _DRIVER_RUNTIME_INIT_FLAGS
    PDRIVER_RUNTIME_INIT_FLAGS = POINTER(_DRIVER_RUNTIME_INIT_FLAGS)
    PCDRIVER_RUNTIME_INIT_FLAGS = POINTER(_DRIVER_RUNTIME_INIT_FLAGS)


    CmKeyObjectType = POINTER(POBJECT_TYPE)
    IoFileObjectType = POINTER(POBJECT_TYPE)
    ExEventObjectType = POINTER(POBJECT_TYPE)
    ExSemaphoreObjectType = POINTER(POBJECT_TYPE)
    TmTransactionManagerObjectType = POINTER(POBJECT_TYPE)
    TmResourceManagerObjectType = POINTER(POBJECT_TYPE)
    TmEnlistmentObjectType = POINTER(POBJECT_TYPE)
    TmTransactionObjectType = POINTER(POBJECT_TYPE)
    PsProcessType = POINTER(POBJECT_TYPE)
    PsThreadType = POINTER(POBJECT_TYPE)
    PsJobType = POINTER(POBJECT_TYPE)
    SeTokenObjectType = POINTER(POBJECT_TYPE)
    if NTDDI_VERSION >= NTDDI_THRESHOLD:
        ExDesktopObjectType = POINTER(POBJECT_TYPE)
    # END IF
    if defined(__cplusplus):
        pass
    # END IF
    if _MSC_VER >= 1200:
        pass
    else:
        pass
    # END IF
# END IF   _WDMDDK_
