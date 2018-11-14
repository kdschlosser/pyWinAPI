import ctypes
from pyWinAPI.shared.wtypes_h import *

class _KDPC(ctypes.Structure):
    pass


KDPC = _KDPC
PKDPC = POINTER(_KDPC)


class _POWER_CHANNEL_SUMMARY(ctypes.Structure):
    pass


POWER_CHANNEL_SUMMARY = _POWER_CHANNEL_SUMMARY
PPOWER_CHANNEL_SUMMARY = POINTER(_POWER_CHANNEL_SUMMARY)


class _DEVICE_OBJECT_POWER_EXTENSION(ctypes.Structure):
    pass


DEVICE_OBJECT_POWER_EXTENSION = _DEVICE_OBJECT_POWER_EXTENSION
PDEVICE_OBJECT_POWER_EXTENSION = POINTER(_DEVICE_OBJECT_POWER_EXTENSION)


class _DEVOBJ_EXTENSION(ctypes.Structure):
    pass


DEVOBJ_EXTENSION = _DEVOBJ_EXTENSION
PDEVOBJ_EXTENSION = POINTER(_DEVOBJ_EXTENSION)


class _IO_STATUS_BLOCK(ctypes.Structure):
    pass


IO_STATUS_BLOCK = _IO_STATUS_BLOCK
PIO_STATUS_BLOCK = POINTER(_IO_STATUS_BLOCK)


class _MDL(ctypes.Structure):
    pass


MDL = _MDL
PMDL = POINTER(_MDL)


class _IRP(ctypes.Structure):
    pass


IRP = _IRP
PIRP = POINTER(_IRP)


class _FAST_IO_DISPATCH(ctypes.Structure):
    pass


FAST_IO_DISPATCH = _FAST_IO_DISPATCH
PFAST_IO_DISPATCH = POINTER(_FAST_IO_DISPATCH)


class _FS_FILTER_CALLBACKS(ctypes.Structure):
    pass


FS_FILTER_CALLBACKS = _FS_FILTER_CALLBACKS
PFS_FILTER_CALLBACKS = POINTER(_FS_FILTER_CALLBACKS)


class _IO_CLIENT_EXTENSION(ctypes.Structure):
    pass


IO_CLIENT_EXTENSION = _IO_CLIENT_EXTENSION
PIO_CLIENT_EXTENSION = POINTER(_IO_CLIENT_EXTENSION)


class _DRIVER_EXTENSION(ctypes.Structure):
    pass


DRIVER_EXTENSION = _DRIVER_EXTENSION
PDRIVER_EXTENSION = POINTER(_DRIVER_EXTENSION)


class _DRIVER_OBJECT(ctypes.Structure):
    pass


DRIVER_OBJECT = _DRIVER_OBJECT
PDRIVER_OBJECT = POINTER(_DRIVER_OBJECT)


class _VPB(ctypes.Structure):
    pass


VPB = _VPB
PVPB = POINTER(_VPB)


class _KDEVICE_QUEUE(ctypes.Structure):
    pass


KDEVICE_QUEUE = _KDEVICE_QUEUE
PKDEVICE_QUEUE = POINTER(_KDEVICE_QUEUE)


class _DEVICE_OBJECT(ctypes.Structure):
    pass


DEVICE_OBJECT = _DEVICE_OBJECT
PDEVICE_OBJECT = POINTER(_DEVICE_OBJECT)


class _IO_TIMER(ctypes.Structure):
    pass


IO_TIMER = _IO_TIMER
PIO_TIMER = POINTER(_IO_TIMER)


class _KINTERRUPT(ctypes.Structure):
    pass


KINTERRUPT = _KINTERRUPT
PKINTERRUPT = POINTER(_KINTERRUPT)


class _DISPATCHER_HEADER(ctypes.Structure):
    pass


DISPATCHER_HEADER = _DISPATCHER_HEADER
PDISPATCHER_HEADER = POINTER(_DISPATCHER_HEADER)


class _KAPC_STATE(ctypes.Structure):
    pass


KAPC_STATE = _KAPC_STATE
PKAPC_STATE = POINTER(_KAPC_STATE)


class _KWAIT_BLOCK(ctypes.Structure):
    pass


KWAIT_BLOCK = _KWAIT_BLOCK
PKWAIT_BLOCK = POINTER(_KWAIT_BLOCK)


class _KGATE(ctypes.Structure):
    pass


KGATE = _KGATE
PKGATE = POINTER(_KGATE)


class _KQUEUE(ctypes.Structure):
    pass


KQUEUE = _KQUEUE
PKQUEUE = POINTER(_KQUEUE)


class _KTIMER(ctypes.Structure):
    pass


KTIMER = _KTIMER
PKTIMER = POINTER(_KTIMER)


class _EXCEPTION_REGISTRATION_RECORD(ctypes.Structure):
    pass


EXCEPTION_REGISTRATION_RECORD = _EXCEPTION_REGISTRATION_RECORD
PEXCEPTION_REGISTRATION_RECORD = POINTER(_EXCEPTION_REGISTRATION_RECORD)


class _KTRAP_FRAME(ctypes.Structure):
    pass


KTRAP_FRAME = _KTRAP_FRAME
PKTRAP_FRAME = POINTER(_KTRAP_FRAME)


class _KAPC(ctypes.Structure):
    pass


KAPC = _KAPC
PKAPC = POINTER(_KAPC)


class _FLOATING_SAVE_AREA(ctypes.Structure):
    pass


FLOATING_SAVE_AREA = _FLOATING_SAVE_AREA
PFLOATING_SAVE_AREA = POINTER(_FLOATING_SAVE_AREA)


class _DESCRIPTOR(ctypes.Structure):
    pass


DESCRIPTOR = _DESCRIPTOR
PDESCRIPTOR = POINTER(_DESCRIPTOR)


class _KSPECIAL_REGISTERS(ctypes.Structure):
    pass


KSPECIAL_REGISTERS = _KSPECIAL_REGISTERS
PKSPECIAL_REGISTERS = POINTER(_KSPECIAL_REGISTERS)


class _CONTEXT(ctypes.Structure):
    pass


CONTEXT = _CONTEXT
PCONTEXT = POINTER(_CONTEXT)


class _KPROCESSOR_STATE(ctypes.Structure):
    pass


KPROCESSOR_STATE = _KPROCESSOR_STATE
PKPROCESSOR_STATE = POINTER(_KPROCESSOR_STATE)


class _KSPIN_LOCK_QUEUE(ctypes.Structure):
    pass


KSPIN_LOCK_QUEUE = _KSPIN_LOCK_QUEUE
PKSPIN_LOCK_QUEUE = POINTER(_KSPIN_LOCK_QUEUE)


class _SLIST_HEADER(ctypes.Structure):
    pass


SLIST_HEADER = _SLIST_HEADER
PSLIST_HEADER = POINTER(_SLIST_HEADER)


class _CACHED_KSTACK_LIST(ctypes.Structure):
    pass


CACHED_KSTACK_LIST = _CACHED_KSTACK_LIST
PCACHED_KSTACK_LIST = POINTER(_CACHED_KSTACK_LIST)


class _KNODE(ctypes.Structure):
    pass


KNODE = _KNODE
PKNODE = POINTER(_KNODE)


class _GENERAL_LOOKASIDE(ctypes.Structure):
    pass


GENERAL_LOOKASIDE = _GENERAL_LOOKASIDE
PGENERAL_LOOKASIDE = POINTER(_GENERAL_LOOKASIDE)


class _PP_LOOKASIDE_LIST(ctypes.Structure):
    pass


PP_LOOKASIDE_LIST = _PP_LOOKASIDE_LIST
PPP_LOOKASIDE_LIST = POINTER(_PP_LOOKASIDE_LIST)


class _GENERAL_LOOKASIDE_POOL(ctypes.Structure):
    pass


GENERAL_LOOKASIDE_POOL = _GENERAL_LOOKASIDE_POOL
PGENERAL_LOOKASIDE_POOL = POINTER(_GENERAL_LOOKASIDE_POOL)


class _KDPC_DATA(ctypes.Structure):
    pass


KDPC_DATA = _KDPC_DATA
PKDPC_DATA = POINTER(_KDPC_DATA)


class _KEVENT(ctypes.Structure):
    pass


KEVENT = _KEVENT
PKEVENT = POINTER(_KEVENT)


class PPM_IDLE_STATE(ctypes.Structure):
    pass


PPPM_IDLE_STATE = POINTER(PPM_IDLE_STATE)


class PPM_IDLE_STATES(ctypes.Structure):
    pass


PPPM_IDLE_STATES = POINTER(PPM_IDLE_STATES)


class PROCESSOR_IDLE_TIMES(ctypes.Structure):
    pass


PPROCESSOR_IDLE_TIMES = POINTER(PROCESSOR_IDLE_TIMES)


class PPM_IDLE_STATE_ACCOUNTING(ctypes.Structure):
    pass


PPPM_IDLE_STATE_ACCOUNTING = POINTER(PPM_IDLE_STATE_ACCOUNTING)


class PPM_IDLE_ACCOUNTING(ctypes.Structure):
    pass


PPPM_IDLE_ACCOUNTING = POINTER(PPM_IDLE_ACCOUNTING)


class PPM_PERF_STATE(ctypes.Structure):
    pass


PPPM_PERF_STATE = POINTER(PPM_PERF_STATE)


class PPM_PERF_STATES(ctypes.Structure):
    pass


PPPM_PERF_STATES = POINTER(PPM_PERF_STATES)


class _PROCESSOR_POWER_STATE(ctypes.Structure):
    pass


PROCESSOR_POWER_STATE = _PROCESSOR_POWER_STATE
PPROCESSOR_POWER_STATE = POINTER(_PROCESSOR_POWER_STATE)


class _CACHE_DESCRIPTOR(ctypes.Structure):
    pass


CACHE_DESCRIPTOR = _CACHE_DESCRIPTOR
PCACHE_DESCRIPTOR = POINTER(_CACHE_DESCRIPTOR)


class _FX_SAVE_AREA(ctypes.Structure):
    pass


FX_SAVE_AREA = _FX_SAVE_AREA
PFX_SAVE_AREA = POINTER(_FX_SAVE_AREA)


class _KPRCB(ctypes.Structure):
    pass


KPRCB = _KPRCB
PKPRCB = POINTER(_KPRCB)


class _KSEMAPHORE(ctypes.Structure):
    pass


KSEMAPHORE = _KSEMAPHORE
PKSEMAPHORE = POINTER(_KSEMAPHORE)


class _KTHREAD(ctypes.Structure):
    pass


KTHREAD = _KTHREAD
PKTHREAD = POINTER(_KTHREAD)


class _KGDTENTRY(ctypes.Structure):
    pass


KGDTENTRY = _KGDTENTRY
PKGDTENTRY = POINTER(_KGDTENTRY)


class _KIDTENTRY(ctypes.Structure):
    pass


KIDTENTRY = _KIDTENTRY
PKIDTENTRY = POINTER(_KIDTENTRY)


class _KEXECUTE_OPTIONS(ctypes.Structure):
    pass


KEXECUTE_OPTIONS = _KEXECUTE_OPTIONS
PKEXECUTE_OPTIONS = POINTER(_KEXECUTE_OPTIONS)


class _KPROCESS(ctypes.Structure):
    pass


KPROCESS = _KPROCESS
PKPROCESS = POINTER(_KPROCESS)


class _OWNER_ENTRY(ctypes.Structure):
    pass


OWNER_ENTRY = _OWNER_ENTRY
POWNER_ENTRY = POINTER(_OWNER_ENTRY)


class _ERESOURCE(ctypes.Structure):
    pass


ERESOURCE = _ERESOURCE
PERESOURCE = POINTER(_ERESOURCE)


class _GENERIC_MAPPING(ctypes.Structure):
    pass


GENERIC_MAPPING = _GENERIC_MAPPING
PGENERIC_MAPPING = POINTER(_GENERIC_MAPPING)


class _OBJECT_TYPE_INITIALIZER(ctypes.Structure):
    pass


OBJECT_TYPE_INITIALIZER = _OBJECT_TYPE_INITIALIZER
POBJECT_TYPE_INITIALIZER = POINTER(_OBJECT_TYPE_INITIALIZER)


class _EX_PUSH_LOCK(ctypes.Structure):
    pass


EX_PUSH_LOCK = _EX_PUSH_LOCK
PEX_PUSH_LOCK = POINTER(_EX_PUSH_LOCK)


class _OBJECT_TYPE(ctypes.Structure):
    pass


OBJECT_TYPE = _OBJECT_TYPE
POBJECT_TYPE = POINTER(_OBJECT_TYPE)


class _SECURITY_QUALITY_OF_SERVICE(ctypes.Structure):
    pass


SECURITY_QUALITY_OF_SERVICE = _SECURITY_QUALITY_OF_SERVICE
PSECURITY_QUALITY_OF_SERVICE = POINTER(_SECURITY_QUALITY_OF_SERVICE)


class _IO_STACK_LOCATION(ctypes.Structure):
    pass


IO_STACK_LOCATION = _IO_STACK_LOCATION
PIO_STACK_LOCATION = POINTER(_IO_STACK_LOCATION)


class _FILE_GET_QUOTA_INFORMATION(ctypes.Structure):
    pass


FILE_GET_QUOTA_INFORMATION = _FILE_GET_QUOTA_INFORMATION
PFILE_GET_QUOTA_INFORMATION = POINTER(_FILE_GET_QUOTA_INFORMATION)


class _TERMINATION_PORT(ctypes.Structure):
    pass


TERMINATION_PORT = _TERMINATION_PORT
PTERMINATION_PORT = POINTER(_TERMINATION_PORT)


class _CLIENT_ID(ctypes.Structure):
    pass


CLIENT_ID = _CLIENT_ID
PCLIENT_ID = POINTER(_CLIENT_ID)


class _PS_CLIENT_SECURITY_CONTEXT(ctypes.Structure):
    pass


PS_CLIENT_SECURITY_CONTEXT = _PS_CLIENT_SECURITY_CONTEXT
PPS_CLIENT_SECURITY_CONTEXT = POINTER(_PS_CLIENT_SECURITY_CONTEXT)


class _EX_RUNDOWN_REF(ctypes.Structure):
    pass


EX_RUNDOWN_REF = _EX_RUNDOWN_REF
PEX_RUNDOWN_REF = POINTER(_EX_RUNDOWN_REF)


class _PSP_RATE_APC(ctypes.Structure):
    pass


PSP_RATE_APC = _PSP_RATE_APC
PPSP_RATE_APC = POINTER(_PSP_RATE_APC)


class _JOB_ACCESS_STATE(ctypes.Structure):
    pass


JOB_ACCESS_STATE = _JOB_ACCESS_STATE
PJOB_ACCESS_STATE = POINTER(_JOB_ACCESS_STATE)


class _ETHREAD(ctypes.Structure):
    pass


ETHREAD = _ETHREAD
PETHREAD = POINTER(_ETHREAD)


class _FAST_MUTEX(ctypes.Structure):
    pass


FAST_MUTEX = _FAST_MUTEX
PFAST_MUTEX = POINTER(_FAST_MUTEX)


class _HANDLE_TRACE_DB_ENTRY(ctypes.Structure):
    pass


HANDLE_TRACE_DB_ENTRY = _HANDLE_TRACE_DB_ENTRY
PHANDLE_TRACE_DB_ENTRY = POINTER(_HANDLE_TRACE_DB_ENTRY)


class _HANDLE_TRACE_DEBUG_INFO(ctypes.Structure):
    pass


HANDLE_TRACE_DEBUG_INFO = _HANDLE_TRACE_DEBUG_INFO
PHANDLE_TRACE_DEBUG_INFO = POINTER(_HANDLE_TRACE_DEBUG_INFO)


class _HANDLE_TABLE_ENTRY_INFO(ctypes.Structure):
    pass


HANDLE_TABLE_ENTRY_INFO = _HANDLE_TABLE_ENTRY_INFO
PHANDLE_TABLE_ENTRY_INFO = POINTER(_HANDLE_TABLE_ENTRY_INFO)


class _HANDLE_TABLE_ENTRY(ctypes.Structure):
    pass


HANDLE_TABLE_ENTRY = _HANDLE_TABLE_ENTRY
PHANDLE_TABLE_ENTRY = POINTER(_HANDLE_TABLE_ENTRY)


class _HANDLE_TABLE(ctypes.Structure):
    pass


HANDLE_TABLE = _HANDLE_TABLE
PHANDLE_TABLE = POINTER(_HANDLE_TABLE)


class _EX_FAST_REF(ctypes.Structure):
    pass


EX_FAST_REF = _EX_FAST_REF
PEX_FAST_REF = POINTER(_EX_FAST_REF)


class _MMADDRESS_NODE(ctypes.Structure):
    pass


MMADDRESS_NODE = _MMADDRESS_NODE
PMMADDRESS_NODE = POINTER(_MMADDRESS_NODE)


class _MM_AVL_TABLE(ctypes.Structure):
    pass


MM_AVL_TABLE = _MM_AVL_TABLE
PMM_AVL_TABLE = POINTER(_MM_AVL_TABLE)


class _EJOB(ctypes.Structure):
    pass


EJOB = _EJOB
PEJOB = POINTER(_EJOB)


class _HARDWARE_PTE(ctypes.Structure):
    pass


HARDWARE_PTE = _HARDWARE_PTE
PHARDWARE_PTE = POINTER(_HARDWARE_PTE)


class _PEB_LDR_DATA(ctypes.Structure):
    pass


PEB_LDR_DATA = _PEB_LDR_DATA
PPEB_LDR_DATA = POINTER(_PEB_LDR_DATA)


class _CURDIR(ctypes.Structure):
    pass


CURDIR = _CURDIR
PCURDIR = POINTER(_CURDIR)


class _RTL_DRIVE_LETTER_CURDIR(ctypes.Structure):
    pass


RTL_DRIVE_LETTER_CURDIR = _RTL_DRIVE_LETTER_CURDIR
PRTL_DRIVE_LETTER_CURDIR = POINTER(_RTL_DRIVE_LETTER_CURDIR)


class _RTL_USER_PROCESS_PARAMETERS(ctypes.Structure):
    pass


RTL_USER_PROCESS_PARAMETERS = _RTL_USER_PROCESS_PARAMETERS
PRTL_USER_PROCESS_PARAMETERS = POINTER(_RTL_USER_PROCESS_PARAMETERS)


class _RTL_CRITICAL_SECTION_DEBUG(ctypes.Structure):
    pass


RTL_CRITICAL_SECTION_DEBUG = _RTL_CRITICAL_SECTION_DEBUG
PRTL_CRITICAL_SECTION_DEBUG = POINTER(_RTL_CRITICAL_SECTION_DEBUG)


class _RTL_CRITICAL_SECTION(ctypes.Structure):
    pass


RTL_CRITICAL_SECTION = _RTL_CRITICAL_SECTION
PRTL_CRITICAL_SECTION = POINTER(_RTL_CRITICAL_SECTION)


class _PEB_FREE_BLOCK(ctypes.Structure):
    pass


PEB_FREE_BLOCK = _PEB_FREE_BLOCK
PPEB_FREE_BLOCK = POINTER(_PEB_FREE_BLOCK)


class _ACTIVATION_CONTEXT_DATA(ctypes.Structure):
    pass


ACTIVATION_CONTEXT_DATA = _ACTIVATION_CONTEXT_DATA
PACTIVATION_CONTEXT_DATA = POINTER(_ACTIVATION_CONTEXT_DATA)


class _ASSEMBLY_STORAGE_MAP(ctypes.Structure):
    pass


ASSEMBLY_STORAGE_MAP = _ASSEMBLY_STORAGE_MAP
PASSEMBLY_STORAGE_MAP = POINTER(_ASSEMBLY_STORAGE_MAP)


class _FLS_CALLBACK_INFO(ctypes.Structure):
    pass


FLS_CALLBACK_INFO = _FLS_CALLBACK_INFO
PFLS_CALLBACK_INFO = POINTER(_FLS_CALLBACK_INFO)


class _PEB(ctypes.Structure):
    pass


PEB = _PEB
PPEB = POINTER(_PEB)


class _ALPC_PROCESS_CONTEXT(ctypes.Structure):
    pass


ALPC_PROCESS_CONTEXT = _ALPC_PROCESS_CONTEXT
PALPC_PROCESS_CONTEXT = POINTER(_ALPC_PROCESS_CONTEXT)


class _OBJECT_NAME_INFORMATION(ctypes.Structure):
    pass


OBJECT_NAME_INFORMATION = _OBJECT_NAME_INFORMATION
POBJECT_NAME_INFORMATION = POINTER(_OBJECT_NAME_INFORMATION)


class _SE_AUDIT_PROCESS_CREATION_INFO(ctypes.Structure):
    pass


SE_AUDIT_PROCESS_CREATION_INFO = _SE_AUDIT_PROCESS_CREATION_INFO
PSE_AUDIT_PROCESS_CREATION_INFO = POINTER(_SE_AUDIT_PROCESS_CREATION_INFO)


class _MMSUPPORT_FLAGS(ctypes.Structure):
    pass


MMSUPPORT_FLAGS = _MMSUPPORT_FLAGS
PMMSUPPORT_FLAGS = POINTER(_MMSUPPORT_FLAGS)


class _MMWSLE_HASH(ctypes.Structure):
    pass


MMWSLE_HASH = _MMWSLE_HASH
PMMWSLE_HASH = POINTER(_MMWSLE_HASH)


class _MMWSLE_NONDIRECT_HASH(ctypes.Structure):
    pass


MMWSLE_NONDIRECT_HASH = _MMWSLE_NONDIRECT_HASH
PMMWSLE_NONDIRECT_HASH = POINTER(_MMWSLE_NONDIRECT_HASH)


class _MMWSLENTRY(ctypes.Structure):
    pass


MMWSLENTRY = _MMWSLENTRY
PMMWSLENTRY = POINTER(_MMWSLENTRY)


class _MMWSLE_FREE_ENTRY(ctypes.Structure):
    pass


MMWSLE_FREE_ENTRY = _MMWSLE_FREE_ENTRY
PMMWSLE_FREE_ENTRY = POINTER(_MMWSLE_FREE_ENTRY)


class _MMWSLE(ctypes.Structure):
    pass


MMWSLE = _MMWSLE
PMMWSLE = POINTER(_MMWSLE)


class _MMWSL(ctypes.Structure):
    pass


MMWSL = _MMWSL
PMMWSL = POINTER(_MMWSL)


class _MMSUPPORT(ctypes.Structure):
    pass


MMSUPPORT = _MMSUPPORT
PMMSUPPORT = POINTER(_MMSUPPORT)


class _EPROCESS_QUOTA_BLOCK(ctypes.Structure):
    pass


EPROCESS_QUOTA_BLOCK = _EPROCESS_QUOTA_BLOCK
PEPROCESS_QUOTA_BLOCK = POINTER(_EPROCESS_QUOTA_BLOCK)


class _PAGEFAULT_HISTORY(ctypes.Structure):
    pass


PAGEFAULT_HISTORY = _PAGEFAULT_HISTORY
PPAGEFAULT_HISTORY = POINTER(_PAGEFAULT_HISTORY)


class _EPROCESS(ctypes.Structure):
    pass


EPROCESS = _EPROCESS
PEPROCESS = POINTER(_EPROCESS)


class _SECTION_OBJECT_POINTERS(ctypes.Structure):
    pass


SECTION_OBJECT_POINTERS = _SECTION_OBJECT_POINTERS
PSECTION_OBJECT_POINTERS = POINTER(_SECTION_OBJECT_POINTERS)


class _IO_COMPLETION_CONTEXT(ctypes.Structure):
    pass


IO_COMPLETION_CONTEXT = _IO_COMPLETION_CONTEXT
PIO_COMPLETION_CONTEXT = POINTER(_IO_COMPLETION_CONTEXT)


class _FILE_OBJECT(ctypes.Structure):
    pass


FILE_OBJECT = _FILE_OBJECT
PFILE_OBJECT = POINTER(_FILE_OBJECT)


class _KINTERRUPT_MODE(ENUM):
    LevelSensitive = 0
    Latched = 1


KINTERRUPT_MODE = _KINTERRUPT_MODE


class _KINTERRUPT_POLARITY(ENUM):
    InterruptPolarityUnknown = 0
    InterruptActiveHigh = 1
    InterruptActiveLow = 2


KINTERRUPT_POLARITY = _KINTERRUPT_POLARITY


class _DEVICE_POWER_STATE(ENUM):
    PowerDeviceUnspecified = 0
    PowerDeviceD0 = 1
    PowerDeviceD1 = 2
    PowerDeviceD2 = 3
    PowerDeviceD3 = 4
    PowerDeviceMaximum = 5


DEVICE_POWER_STATE = _DEVICE_POWER_STATE


class _EXCEPTION_DISPOSITION(ENUM):
    ExceptionContinueExecution = 0
    ExceptionContinueSearch = 1
    ExceptionNestedException = 2
    ExceptionCollidedUnwind = 3


EXCEPTION_DISPOSITION = _EXCEPTION_DISPOSITION
PEXCEPTION_DISPOSITION = POINTER(_EXCEPTION_DISPOSITION)


class _POOL_TYPE(ENUM):
    NonPagedPool = 0
    PagedPool = 1
    NonPagedPoolMustSucceed = 2
    DontUseThisType = 3
    NonPagedPoolCacheAligned = 4
    PagedPoolCacheAligned = 5
    NonPagedPoolCacheAlignedMustS = 6
    MaxPoolType = 7
    NonPagedPoolSession = 32
    PagedPoolSession = 33
    NonPagedPoolMustSucceedSession = 34
    DontUseThisTypeSession = 35
    NonPagedPoolCacheAlignedSession = 36
    PagedPoolCacheAlignedSession = 37
    NonPagedPoolCacheAlignedMustSSession = 38


POOL_TYPE = _POOL_TYPE


class _PROCESSOR_CACHE_TYPE(ENUM):
    CacheUnified = 0
    CacheInstruction = 1
    CacheData = 2
    CacheTrace = 3


PROCESSOR_CACHE_TYPE = _PROCESSOR_CACHE_TYPE


class _SECURITY_IMPERSONATION_LEVEL(ENUM):
    SecurityAnonymous = 0
    SecurityIdentification = 1
    SecurityImpersonation = 2
    SecurityDelegation = 3


SECURITY_IMPERSONATION_LEVEL = _SECURITY_IMPERSONATION_LEVEL


_KDPC._fields_ = [
    ('Type', UCHAR),
    ('Importance', UCHAR),
    ('Number', WORD),
    ('DpcListEntry', LIST_ENTRY),
    ('DeferredRoutine', PVOID),
    ('DeferredContext', PVOID),
    ('SystemArgument1', PVOID),
    ('SystemArgument2', PVOID),
    ('DpcData', PVOID),
]

_KEVENT._fields_ = [
    ('Header', DISPATCHER_HEADER),
]

_POWER_CHANNEL_SUMMARY._fields_ = [
    ('Signature', ULONG),
    ('TotalCount', ULONG),
    ('D0Count', ULONG),
    ('NotifyList', LIST_ENTRY),
]
_DEVICE_OBJECT_POWER_EXTENSION._fields_ = [
    ('IdleCount', LONG),
    ('ConservationIdleTime', ULONG),
    ('PerformanceIdleTime', ULONG),
    ('DeviceObject', PDEVICE_OBJECT),
    ('IdleList', LIST_ENTRY),
    ('DeviceType', UCHAR),
    ('State', DEVICE_POWER_STATE),
    ('NotifySourceList', LIST_ENTRY),
    ('NotifyTargetList', LIST_ENTRY),
    ('PowerChannelSummary', POWER_CHANNEL_SUMMARY),
    ('Volume', LIST_ENTRY),
    ('PreviousIdleCount', ULONG),
]
_DEVOBJ_EXTENSION._fields_ = [
    ('Type', SHORT),
    ('Size', WORD),
    ('DeviceObject', PDEVICE_OBJECT),
    ('PowerFlags', ULONG),
    ('Dope', PDEVICE_OBJECT_POWER_EXTENSION),
    ('ExtensionFlags', ULONG),
    ('DeviceNode', PVOID),
    ('AttachedTo', PDEVICE_OBJECT),
    ('StartIoCount', LONG),
    ('StartIoKey', LONG),
    ('StartIoFlags', ULONG),
    ('Vpb', PVPB),
]


class _Union_1(ctypes.Union):
    pass


_Union_1._fields_ = [
    ('Status', LONG),
    ('Pointer', PVOID),
]
_IO_STATUS_BLOCK._Union_1 = _Union_1

_IO_STATUS_BLOCK._anonymous_ = (
    '_Union_1',
)
_IO_STATUS_BLOCK._fields_ = [
    ('_Union_1', _IO_STATUS_BLOCK._Union_1),
    ('Information', ULONG),
]
_MDL._fields_ = [
    ('Next', PMDL),
    ('Size', SHORT),
    ('MdlFlags', SHORT),
    ('Process', PEPROCESS),
    ('MappedSystemVa', PVOID),
    ('StartVa', PVOID),
    ('ByteCount', ULONG),
    ('ByteOffset', ULONG),
]
_IRP._fields_ = [
    ('Type', SHORT),
    ('Size', WORD),
    ('MdlAddress', PMDL),
    ('Flags', ULONG),
    ('AssociatedIrp', ULONG),
    ('ThreadListEntry', LIST_ENTRY),
    ('IoStatus', IO_STATUS_BLOCK),
    ('RequestorMode', CHAR),
    ('PendingReturned', UCHAR),
    ('StackCount', CHAR),
    ('CurrentLocation', CHAR),
    ('Cancel', UCHAR),
    ('CancelIrql', UCHAR),
    ('ApcEnvironment', CHAR),
    ('AllocationFlags', UCHAR),
    ('UserIosb', PIO_STATUS_BLOCK),
    ('UserEvent', PKEVENT),
    ('Overlay', UINT64),
    ('CancelRoutine', PVOID),
    ('UserBuffer', PVOID),
    ('Tail', ULONG),
]
_FAST_IO_DISPATCH._fields_ = [
    ('SizeOfFastIoDispatch', ULONG),
    ('FastIoCheckIfPossible', POINTER(UCHAR)),
    ('FastIoRead', POINTER(UCHAR)),
    ('FastIoWrite', POINTER(UCHAR)),
    ('FastIoQueryBasicInfo', POINTER(UCHAR)),
    ('FastIoQueryStandardInfo', POINTER(UCHAR)),
    ('FastIoLock', POINTER(UCHAR)),
    ('FastIoUnlockSingle', POINTER(UCHAR)),
    ('FastIoUnlockAll', POINTER(UCHAR)),
    ('FastIoUnlockAllByKey', POINTER(UCHAR)),
    ('FastIoDeviceControl', POINTER(UCHAR)),
    ('AcquireFileForNtCreateSection', PVOID),
    ('ReleaseFileForNtCreateSection', PVOID),
    ('FastIoDetachDevice', PVOID),
    ('FastIoQueryNetworkOpenInfo', POINTER(UCHAR)),
    ('AcquireForModWrite', POINTER(LONG)),
    ('MdlRead', POINTER(UCHAR)),
    ('MdlReadComplete', POINTER(UCHAR)),
    ('PrepareMdlWrite', POINTER(UCHAR)),
    ('MdlWriteComplete', POINTER(UCHAR)),
    ('FastIoReadCompressed', POINTER(UCHAR)),
    ('FastIoWriteCompressed', POINTER(UCHAR)),
    ('MdlReadCompleteCompressed', POINTER(UCHAR)),
    ('MdlWriteCompleteCompressed', POINTER(UCHAR)),
    ('FastIoQueryOpen', POINTER(UCHAR)),
    ('ReleaseForModWrite', POINTER(LONG)),
    ('AcquireForCcFlush', POINTER(LONG)),
    ('ReleaseForCcFlush', POINTER(LONG)),
]
_FS_FILTER_CALLBACKS._fields_ = [
    ('SizeOfFsFilterCallbacks', ULONG),
    ('Reserved', ULONG),
    ('PreAcquireForSectionSynchronization', POINTER(LONG)),
    ('PostAcquireForSectionSynchronization', PVOID),
    ('PreReleaseForSectionSynchronization', POINTER(LONG)),
    ('PostReleaseForSectionSynchronization', PVOID),
    ('PreAcquireForCcFlush', POINTER(LONG)),
    ('PostAcquireForCcFlush', PVOID),
    ('PreReleaseForCcFlush', POINTER(LONG)),
    ('PostReleaseForCcFlush', PVOID),
    ('PreAcquireForModifiedPageWriter', POINTER(LONG)),
    ('PostAcquireForModifiedPageWriter', PVOID),
    ('PreReleaseForModifiedPageWriter', POINTER(LONG)),
    ('PostReleaseForModifiedPageWriter', PVOID),
]
_IO_CLIENT_EXTENSION._fields_ = [
    ('NextExtension', PIO_CLIENT_EXTENSION),
    ('ClientIdentificationAddress', PVOID),
]
_DRIVER_EXTENSION._fields_ = [
    ('DriverObject', PDRIVER_OBJECT),
    ('AddDevice', POINTER(LONG)),
    ('Count', ULONG),
    ('ServiceKeyName', UNICODE_STRING),
    ('ClientDriverExtension', PIO_CLIENT_EXTENSION),
    ('FsFilterCallbacks', PFS_FILTER_CALLBACKS),
]
_DRIVER_OBJECT._fields_ = [
    ('Type', SHORT),
    ('Size', SHORT),
    ('DeviceObject', PDEVICE_OBJECT),
    ('Flags', ULONG),
    ('DriverStart', PVOID),
    ('DriverSize', ULONG),
    ('DriverSection', PVOID),
    ('DriverExtension', PDRIVER_EXTENSION),
    ('DriverName', UNICODE_STRING),
    ('HardwareDatabase', PUNICODE_STRING),
    ('FastIoDispatch', PFAST_IO_DISPATCH),
    ('DriverInit', POINTER(LONG)),
    ('DriverStartIo', PVOID),
    ('DriverUnload', PVOID),
    ('MajorFunction', POINTER(LONG) * 28),
]
_VPB._fields_ = [
    ('Type', SHORT),
    ('Size', SHORT),
    ('Flags', WORD),
    ('VolumeLabelLength', WORD),
    ('DeviceObject', PDEVICE_OBJECT),
    ('RealDevice', PDEVICE_OBJECT),
    ('SerialNumber', ULONG),
    ('ReferenceCount', ULONG),
    ('VolumeLabel', WCHAR * 32),
]
_KDEVICE_QUEUE._fields_ = [
    ('Type', SHORT),
    ('Size', SHORT),
    ('DeviceListHead', LIST_ENTRY),
    ('Lock', ULONG),
    ('Busy', UCHAR),
]
_DEVICE_OBJECT._fields_ = [
    ('Type', SHORT),
    ('Size', WORD),
    ('ReferenceCount', LONG),
    ('DriverObject', PDRIVER_OBJECT),
    ('NextDevice', PDEVICE_OBJECT),
    ('AttachedDevice', PDEVICE_OBJECT),
    ('CurrentIrp', PIRP),
    ('Timer', PIO_TIMER),
    ('Flags', ULONG),
    ('Characteristics', ULONG),
    ('Vpb', PVPB),
    ('DeviceExtension', PVOID),
    ('DeviceType', ULONG),
    ('StackSize', CHAR),
    ('Queue', BYTE * 40),
    ('AlignmentRequirement', ULONG),
    ('DeviceQueue', KDEVICE_QUEUE),
    ('Dpc', KDPC),
    ('ActiveThreadCount', ULONG),
    ('SecurityDescriptor', PVOID),
    ('DeviceLock', KEVENT),
    ('SectorSize', WORD),
    ('Spare1', WORD),
    ('DeviceObjectExtension', PDEVOBJ_EXTENSION),
    ('Reserved', PVOID),
]
_IO_TIMER._fields_ = [
    ('Type', SHORT),
    ('TimerFlag', SHORT),
    ('TimerList', LIST_ENTRY),
    ('TimerRoutine', PVOID),
    ('Context', PVOID),
    ('DeviceObject', PDEVICE_OBJECT),
]
_KINTERRUPT._fields_ = [
    ('Type', SHORT),
    ('Size', SHORT),
    ('InterruptListEntry', LIST_ENTRY),
    ('ServiceRoutine', POINTER(UCHAR)),
    ('MessageServiceRoutine', POINTER(UCHAR)),
    ('MessageIndex', ULONG),
    ('ServiceContext', PVOID),
    ('SpinLock', ULONG),
    ('TickCount', ULONG),
    ('ActualLock', POINTER(ULONG)),
    ('DispatchAddress', PVOID),
    ('Vector', ULONG),
    ('Irql', UCHAR),
    ('SynchronizeIrql', UCHAR),
    ('FloatingSave', UCHAR),
    ('Connected', UCHAR),
    ('Number', CHAR),
    ('ShareVector', UCHAR),
    ('Mode', KINTERRUPT_MODE),
    ('Polarity', KINTERRUPT_POLARITY),
    ('ServiceCount', ULONG),
    ('DispatchCount', ULONG),
    ('Rsvd1', UINT64),
    ('DispatchCode', ULONG * 135),
]


class _Union_2(ctypes.Union):
    pass


class _Union_3(ctypes.Union):
    pass


class _Union_4(ctypes.Union):
    pass


_Union_4._fields_ = [
    ('Abandoned', UCHAR),
    ('Absolute', UCHAR),
    ('NpxIrql', UCHAR),
    ('Signalling', UCHAR),
]
_Union_3._Union_4 = _Union_4


class _Union_5(ctypes.Union):
    pass


_Union_5._fields_ = [
    ('Size', UCHAR),
    ('Hand', UCHAR),
]
_Union_3._Union_5 = _Union_5


class _Union_6(ctypes.Union):
    pass


_Union_6._fields_ = [
    ('Inserted', UCHAR),
    ('DebugActive', UCHAR),
    ('DpcActive', UCHAR),
]
_Union_3._Union_6 = _Union_6

_Union_3._anonymous_ = (
    '_Union_4',
    '_Union_5',
    '_Union_6',
)
_Union_3._fields_ = [
    ('Type', UCHAR),
    ('_Union_4', _Union_3._Union_4),
    ('_Union_5', _Union_3._Union_5),
    ('_Union_6', _Union_3._Union_6),
]
_Union_2._Union_3 = _Union_3

_Union_2._anonymous_ = (
    '_Union_3',
)
_Union_2._fields_ = [
    ('_Union_3', _Union_2._Union_3),
    ('Lock', LONG),
]
_DISPATCHER_HEADER._Union_2 = _Union_2

_DISPATCHER_HEADER._anonymous_ = (
    '_Union_2',
)

_KAPC_STATE._fields_ = [
    ('ApcListHead', LIST_ENTRY * 2),
    ('Process', PKPROCESS),
    ('KernelApcInProgress', UCHAR),
    ('KernelApcPending', UCHAR),
    ('UserApcPending', UCHAR),
]
_KWAIT_BLOCK._fields_ = [
    ('WaitListEntry', LIST_ENTRY),
    ('Thread', PKTHREAD),
    ('Object', PVOID),
    ('NextWaitBlock', PKWAIT_BLOCK),
    ('WaitKey', WORD),
    ('WaitType', UCHAR),
    ('SpareByte', UCHAR),
]
_KGATE._fields_ = [
    ('Header', DISPATCHER_HEADER),
]
_KQUEUE._fields_ = [
    ('Header', DISPATCHER_HEADER),
    ('EntryListHead', LIST_ENTRY),
    ('CurrentCount', ULONG),
    ('MaximumCount', ULONG),
    ('ThreadListHead', LIST_ENTRY),
]

_KTIMER._fields_ = [
    ('Header', DISPATCHER_HEADER),
    ('DueTime', ULARGE_INTEGER),
    ('TimerListEntry', LIST_ENTRY),
    ('Dpc', PKDPC),
    ('Period', LONG),
]
_EXCEPTION_REGISTRATION_RECORD._fields_ = [
    ('Next', PEXCEPTION_REGISTRATION_RECORD),
    ('Handler', PEXCEPTION_DISPOSITION),
]
_KTRAP_FRAME._fields_ = [
    ('DbgEbp', ULONG),
    ('DbgEip', ULONG),
    ('DbgArgMark', ULONG),
    ('DbgArgPointer', ULONG),
    ('TempSegCs', WORD),
    ('Logging', UCHAR),
    ('Reserved', UCHAR),
    ('TempEsp', ULONG),
    ('Dr0', ULONG),
    ('Dr1', ULONG),
    ('Dr2', ULONG),
    ('Dr3', ULONG),
    ('Dr6', ULONG),
    ('Dr7', ULONG),
    ('SegGs', ULONG),
    ('SegEs', ULONG),
    ('SegDs', ULONG),
    ('Edx', ULONG),
    ('Ecx', ULONG),
    ('Eax', ULONG),
    ('PreviousPreviousMode', ULONG),
    ('ExceptionList', PEXCEPTION_REGISTRATION_RECORD),
    ('SegFs', ULONG),
    ('Edi', ULONG),
    ('Esi', ULONG),
    ('Ebx', ULONG),
    ('Ebp', ULONG),
    ('ErrCode', ULONG),
    ('Eip', ULONG),
    ('SegCs', ULONG),
    ('EFlags', ULONG),
    ('HardwareEsp', ULONG),
    ('HardwareSegSs', ULONG),
    ('V86Es', ULONG),
    ('V86Ds', ULONG),
    ('V86Fs', ULONG),
    ('V86Gs', ULONG),
]
_KAPC._fields_ = [
    ('Type', UCHAR),
    ('SpareByte0', UCHAR),
    ('Size', UCHAR),
    ('SpareByte1', UCHAR),
    ('SpareLong0', ULONG),
    ('Thread', PKTHREAD),
    ('ApcListEntry', LIST_ENTRY),
    ('KernelRoutine', PVOID),
    ('RundownRoutine', PVOID),
    ('NormalRoutine', PVOID),
    ('NormalContext', PVOID),
    ('SystemArgument1', PVOID),
    ('SystemArgument2', PVOID),
    ('ApcStateIndex', CHAR),
    ('ApcMode', CHAR),
    ('Inserted', UCHAR),
]
_FLOATING_SAVE_AREA._fields_ = [
    ('ControlWord', ULONG),
    ('StatusWord', ULONG),
    ('TagWord', ULONG),
    ('ErrorOffset', ULONG),
    ('ErrorSelector', ULONG),
    ('DataOffset', ULONG),
    ('DataSelector', ULONG),
    ('RegisterArea', UCHAR * 80),
    ('Cr0NpxState', ULONG),
]
_DESCRIPTOR._fields_ = [
    ('Pad', WORD),
    ('Limit', WORD),
    ('Base', ULONG),
]
_KSPECIAL_REGISTERS._fields_ = [
    ('Cr0', ULONG),
    ('Cr2', ULONG),
    ('Cr3', ULONG),
    ('Cr4', ULONG),
    ('KernelDr0', ULONG),
    ('KernelDr1', ULONG),
    ('KernelDr2', ULONG),
    ('KernelDr3', ULONG),
    ('KernelDr6', ULONG),
    ('KernelDr7', ULONG),
    ('Gdtr', DESCRIPTOR),
    ('Idtr', DESCRIPTOR),
    ('Tr', WORD),
    ('Ldtr', WORD),
    ('Reserved', ULONG * 6),
]
_CONTEXT._fields_ = [
    ('ContextFlags', ULONG),
    ('Dr0', ULONG),
    ('Dr1', ULONG),
    ('Dr2', ULONG),
    ('Dr3', ULONG),
    ('Dr6', ULONG),
    ('Dr7', ULONG),
    ('FloatSave', FLOATING_SAVE_AREA),
    ('SegGs', ULONG),
    ('SegFs', ULONG),
    ('SegEs', ULONG),
    ('SegDs', ULONG),
    ('Edi', ULONG),
    ('Esi', ULONG),
    ('Ebx', ULONG),
    ('Edx', ULONG),
    ('Ecx', ULONG),
    ('Eax', ULONG),
    ('Ebp', ULONG),
    ('Eip', ULONG),
    ('SegCs', ULONG),
    ('EFlags', ULONG),
    ('Esp', ULONG),
    ('SegSs', ULONG),
    ('ExtendedRegisters', UCHAR * 512),
]
_KPROCESSOR_STATE._fields_ = [
    ('ContextFrame', CONTEXT),
    ('SpecialRegisters', KSPECIAL_REGISTERS),
]
_KSPIN_LOCK_QUEUE._fields_ = [
    ('Next', PKSPIN_LOCK_QUEUE),
    ('Lock', POINTER(ULONG)),
]


class _Struct_1(ctypes.Structure):
    pass


class _Struct_2(ctypes.Structure):
    pass


_Struct_2._fields_ = [
    ('Next', SINGLE_LIST_ENTRY),
    ('Depth', WORD),
    ('Sequence', WORD),
]
_Struct_1._Struct_2 = _Struct_2

_Struct_1._anonymous_ = (
    '_Struct_2',
)
_Struct_1._fields_ = [
    ('Alignment', UINT64),
    ('_Struct_2', _Struct_1._Struct_2),
]
_SLIST_HEADER._Struct_1 = _Struct_1

_SLIST_HEADER._anonymous_ = (
    '_Struct_1',
)
_SLIST_HEADER._fields_ = [
    ('_Struct_1', _SLIST_HEADER._Struct_1),
]
_CACHED_KSTACK_LIST._fields_ = [
    ('SListHead', SLIST_HEADER),
    ('MinimumFree', LONG),
    ('Misses', ULONG),
    ('MissesLast', ULONG),
]
_KNODE._fields_ = [
    ('PagedPoolSListHead', SLIST_HEADER),
    ('NonPagedPoolSListHead', SLIST_HEADER * 3),
    ('PfnDereferenceSListHead', SLIST_HEADER),
    ('ProcessorMask', ULONG),
    ('Color', UCHAR),
    ('Seed', UCHAR),
    ('NodeNumber', UCHAR),
    ('Flags', DWORD),
    ('MmShiftedColor', ULONG),
    ('FreeCount', ULONG * 2),
    ('PfnDeferredList', PSINGLE_LIST_ENTRY),
    ('CachedKernelStacks', CACHED_KSTACK_LIST),
]


class _Union_3(ctypes.Union):
    pass


_Union_3._fields_ = [
    ('ListHead', SLIST_HEADER),
    ('SingleListHead', SINGLE_LIST_ENTRY),
]
_GENERAL_LOOKASIDE._Union_3 = _Union_3


class _Union_4(ctypes.Union):
    pass


_Union_4._fields_ = [
    ('AllocateMisses', ULONG),
    ('AllocateHits', ULONG),
]
_GENERAL_LOOKASIDE._Union_4 = _Union_4


class _Union_5(ctypes.Union):
    pass


_Union_5._fields_ = [
    ('FreeMisses', ULONG),
    ('FreeHits', ULONG),
]
_GENERAL_LOOKASIDE._Union_5 = _Union_5


class _Union_6(ctypes.Union):
    pass


_Union_6._fields_ = [
    ('AllocateEx', POINTER(PVOID)),
    ('Allocate', POINTER(PVOID)),
]
_GENERAL_LOOKASIDE._Union_6 = _Union_6


class _Union_7(ctypes.Union):
    pass


_Union_7._fields_ = [
    ('FreeEx', PVOID),
    ('Free', PVOID),
]
_GENERAL_LOOKASIDE._Union_7 = _Union_7


class _Union_8(ctypes.Union):
    pass


_Union_8._fields_ = [
    ('LastAllocateMisses', ULONG),
    ('LastAllocateHits', ULONG),
]
_GENERAL_LOOKASIDE._Union_8 = _Union_8

_GENERAL_LOOKASIDE._anonymous_ = (
    '_Union_3',
    '_Union_4',
    '_Union_5',
    '_Union_6',
    '_Union_7',
    '_Union_8',
)
_GENERAL_LOOKASIDE._fields_ = [
    ('_Union_3', _GENERAL_LOOKASIDE._Union_3),
    ('Depth', WORD),
    ('MaximumDepth', WORD),
    ('TotalAllocates', ULONG),
    ('_Union_4', _GENERAL_LOOKASIDE._Union_4),
    ('TotalFrees', ULONG),
    ('_Union_5', _GENERAL_LOOKASIDE._Union_5),
    ('Type', POOL_TYPE),
    ('Tag', ULONG),
    ('Size', ULONG),
    ('_Union_6', _GENERAL_LOOKASIDE._Union_6),
    ('_Union_7', _GENERAL_LOOKASIDE._Union_7),
    ('ListEntry', LIST_ENTRY),
    ('LastTotalAllocates', ULONG),
    ('_Union_8', _GENERAL_LOOKASIDE._Union_8),
    ('Future', ULONG * 2),
]
_PP_LOOKASIDE_LIST._fields_ = [
    ('P', PGENERAL_LOOKASIDE),
    ('L', PGENERAL_LOOKASIDE),
]


class _Union_9(ctypes.Union):
    pass


_Union_9._fields_ = [
    ('ListHead', SLIST_HEADER),
    ('SingleListHead', SINGLE_LIST_ENTRY),
]
_GENERAL_LOOKASIDE_POOL._Union_9 = _Union_9


class _Union_10(ctypes.Union):
    pass


_Union_10._fields_ = [
    ('AllocateMisses', ULONG),
    ('AllocateHits', ULONG),
]
_GENERAL_LOOKASIDE_POOL._Union_10 = _Union_10


class _Union_11(ctypes.Union):
    pass


_Union_11._fields_ = [
    ('FreeMisses', ULONG),
    ('FreeHits', ULONG),
]
_GENERAL_LOOKASIDE_POOL._Union_11 = _Union_11


class _Union_12(ctypes.Union):
    pass


_Union_12._fields_ = [
    ('AllocateEx', POINTER(PVOID)),
    ('Allocate', POINTER(PVOID)),
]
_GENERAL_LOOKASIDE_POOL._Union_12 = _Union_12


class _Union_13(ctypes.Union):
    pass


_Union_13._fields_ = [
    ('FreeEx', PVOID),
    ('Free', PVOID),
]
_GENERAL_LOOKASIDE_POOL._Union_13 = _Union_13


class _Union_14(ctypes.Union):
    pass


_Union_14._fields_ = [
    ('LastAllocateMisses', ULONG),
    ('LastAllocateHits', ULONG),
]
_GENERAL_LOOKASIDE_POOL._Union_14 = _Union_14

_GENERAL_LOOKASIDE_POOL._anonymous_ = (
    '_Union_9',
    '_Union_10',
    '_Union_11',
    '_Union_12',
    '_Union_13',
    '_Union_14',
)
_GENERAL_LOOKASIDE_POOL._fields_ = [
    ('_Union_9', _GENERAL_LOOKASIDE_POOL._Union_9),
    ('Depth', WORD),
    ('MaximumDepth', WORD),
    ('TotalAllocates', ULONG),
    ('_Union_10', _GENERAL_LOOKASIDE_POOL._Union_10),
    ('TotalFrees', ULONG),
    ('_Union_11', _GENERAL_LOOKASIDE_POOL._Union_11),
    ('Type', POOL_TYPE),
    ('Tag', ULONG),
    ('Size', ULONG),
    ('_Union_12', _GENERAL_LOOKASIDE_POOL._Union_12),
    ('_Union_13', _GENERAL_LOOKASIDE_POOL._Union_13),
    ('ListEntry', LIST_ENTRY),
    ('LastTotalAllocates', ULONG),
    ('_Union_14', _GENERAL_LOOKASIDE_POOL._Union_14),
    ('Future', ULONG * 2),
]
_KDPC_DATA._fields_ = [
    ('DpcListHead', LIST_ENTRY),
    ('DpcLock', ULONG),
    ('DpcQueueDepth', LONG),
    ('DpcCount', ULONG),
]


PPM_IDLE_STATE._fields_ = [
    ('IdleHandler', POINTER(LONG)),
    ('Context', ULONG),
    ('Latency', ULONG),
    ('Power', ULONG),
    ('TimeCheck', ULONG),
    ('StateFlags', ULONG),
    ('PromotePercent', UCHAR),
    ('DemotePercent', UCHAR),
    ('PromotePercentBase', UCHAR),
    ('DemotePercentBase', UCHAR),
    ('StateType', UCHAR),
]
PPM_IDLE_STATES._fields_ = [
    ('Type', ULONG),
    ('Count', ULONG),
    ('Flags', ULONG),
    ('TargetState', ULONG),
    ('ActualState', ULONG),
    ('OldState', ULONG),
    ('TargetProcessors', ULONG),
    ('State', PPM_IDLE_STATE * 1),
]
PROCESSOR_IDLE_TIMES._fields_ = [
    ('StartTime', UINT64),
    ('EndTime', UINT64),
    ('Reserved', ULONG * 4),
]
PPM_IDLE_STATE_ACCOUNTING._fields_ = [
    ('IdleTransitions', ULONG),
    ('FailedTransitions', ULONG),
    ('InvalidBucketIndex', ULONG),
    ('TotalTime', UINT64),
    ('IdleTimeBuckets', ULONG * 6),
]
PPM_IDLE_ACCOUNTING._fields_ = [
    ('StateCount', ULONG),
    ('TotalTransitions', ULONG),
    ('ResetCount', ULONG),
    ('StartTime', UINT64),
    ('State', PPM_IDLE_STATE_ACCOUNTING * 1),
]
PPM_PERF_STATE._fields_ = [
    ('Frequency', ULONG),
    ('Power', ULONG),
    ('PercentFrequency', UCHAR),
    ('IncreaseLevel', UCHAR),
    ('DecreaseLevel', UCHAR),
    ('Type', UCHAR),
    ('Control', UINT64),
    ('Status', UINT64),
    ('TotalHitCount', ULONG),
    ('DesiredCount', ULONG),
]
PPM_PERF_STATES._fields_ = [
    ('Count', ULONG),
    ('MaxFrequency', ULONG),
    ('MaxPerfState', ULONG),
    ('MinPerfState', ULONG),
    ('LowestPState', ULONG),
    ('IncreaseTime', ULONG),
    ('DecreaseTime', ULONG),
    ('BusyAdjThreshold', UCHAR),
    ('Reserved', UCHAR),
    ('ThrottleStatesOnly', UCHAR),
    ('PolicyType', UCHAR),
    ('TimerInterval', ULONG),
    ('Flags', ULONG),
    ('TargetProcessors', ULONG),
    ('PStateHandler', POINTER(LONG)),
    ('PStateContext', ULONG),
    ('TStateHandler', POINTER(LONG)),
    ('TStateContext', ULONG),
    ('UINT * FeedbackHandler', LONG),
    ('State', PPM_PERF_STATE * 1),
]
_PROCESSOR_POWER_STATE._fields_ = [
    ('IdleFunction', PVOID),
    ('IdleStates', PPPM_IDLE_STATES),
    ('LastTimeCheck', UINT64),
    ('LastIdleTime', UINT64),
    ('IdleTimes', PROCESSOR_IDLE_TIMES),
    ('IdleAccounting', PPPM_IDLE_ACCOUNTING),
    ('PerfStates', PPPM_PERF_STATES),
    ('LastKernelUserTime', ULONG),
    ('LastIdleThreadKTime', ULONG),
    ('LastGlobalTimeHv', UINT64),
    ('LastProcessorTimeHv', UINT64),
    ('ThermalConstraint', UCHAR),
    ('LastBusyPercentage', UCHAR),
    ('Flags', BYTE * 6),
    ('PerfTimer', KTIMER),
    ('PerfDpc', KDPC),
    ('LastSysTime', ULONG),
    ('PStateMaster', PKPRCB),
    ('PStateSet', ULONG),
    ('CurrentPState', ULONG),
    ('Reserved0', ULONG),
    ('DesiredPState', ULONG),
    ('Reserved1', ULONG),
    ('PStateIdleStartTime', ULONG),
    ('PStateIdleTime', ULONG),
    ('LastPStateIdleTime', ULONG),
    ('PStateStartTime', ULONG),
    ('WmiDispatchPtr', ULONG),
    ('WmiInterfaceEnabled', LONG),
]
_CACHE_DESCRIPTOR._fields_ = [
    ('Level', UCHAR),
    ('Associativity', UCHAR),
    ('LineSize', WORD),
    ('Size', ULONG),
    ('Type', PROCESSOR_CACHE_TYPE),
]
_FX_SAVE_AREA._fields_ = [
    ('U', BYTE * 520),
    ('NpxSavedCpu', ULONG),
    ('Cr0NpxState', ULONG),
]


class _Struct_2(ctypes.Structure):
    pass


class _Struct_3(ctypes.Structure):
    pass


_Struct_3._fields_ = [
    ('CpuStepping', UCHAR),
    ('CpuModel', UCHAR),
]
_Struct_2._Struct_3 = _Struct_3

_Struct_2._anonymous_ = (
    '_Struct_3',
)
_Struct_2._fields_ = [
    ('CpuStep', WORD),
    ('_Struct_3', _Struct_2._Struct_3),
]
_KPRCB._Struct_2 = _Struct_2

_KPRCB._anonymous_ = (
    '_Struct_2',
)
_KPRCB._fields_ = [
    ('MinorVersion', WORD),
    ('MajorVersion', WORD),
    ('CurrentThread', PKTHREAD),
    ('NextThread', PKTHREAD),
    ('IdleThread', PKTHREAD),
    ('Number', UCHAR),
    ('NestingLevel', UCHAR),
    ('BuildType', WORD),
    ('SetMember', ULONG),
    ('CpuType', CHAR),
    ('CpuID', CHAR),
    ('_Struct_2', _KPRCB._Struct_2),
    ('ProcessorState', KPROCESSOR_STATE),
    ('KernelReserved', ULONG * 16),
    ('HalReserved', ULONG * 16),
    ('CFlushSize', ULONG),
    ('PrcbPad0', UCHAR * 88),
    ('LockQueue', KSPIN_LOCK_QUEUE * 33),
    ('NpxThread', PKTHREAD),
    ('InterruptCount', ULONG),
    ('KernelTime', ULONG),
    ('UserTime', ULONG),
    ('DpcTime', ULONG),
    ('DpcTimeCount', ULONG),
    ('InterruptTime', ULONG),
    ('AdjustDpcThreshold', ULONG),
    ('PageColor', ULONG),
    ('SkipTick', UCHAR),
    ('DebuggerSavedIRQL', UCHAR),
    ('NodeColor', UCHAR),
    ('PollSlot', UCHAR),
    ('NodeShiftedColor', ULONG),
    ('ParentNode', PKNODE),
    ('MultiThreadProcessorSet', ULONG),
    ('MultiThreadSetMaster', PKPRCB),
    ('SecondaryColorMask', ULONG),
    ('DpcTimeLimit', ULONG),
    ('CcFastReadNoWait', ULONG),
    ('CcFastReadWait', ULONG),
    ('CcFastReadNotPossible', ULONG),
    ('CcCopyReadNoWait', ULONG),
    ('CcCopyReadWait', ULONG),
    ('CcCopyReadNoWaitMiss', ULONG),
    ('MmSpinLockOrdering', LONG),
    ('IoReadOperationCount', LONG),
    ('IoWriteOperationCount', LONG),
    ('IoOtherOperationCount', LONG),
    ('IoReadTransferCount', LARGE_INTEGER),
    ('IoWriteTransferCount', LARGE_INTEGER),
    ('IoOtherTransferCount', LARGE_INTEGER),
    ('CcFastMdlReadNoWait', ULONG),
    ('CcFastMdlReadWait', ULONG),
    ('CcFastMdlReadNotPossible', ULONG),
    ('CcMapDataNoWait', ULONG),
    ('CcMapDataWait', ULONG),
    ('CcPinMappedDataCount', ULONG),
    ('CcPinReadNoWait', ULONG),
    ('CcPinReadWait', ULONG),
    ('CcMdlReadNoWait', ULONG),
    ('CcMdlReadWait', ULONG),
    ('CcLazyWriteHotSpots', ULONG),
    ('CcLazyWriteIos', ULONG),
    ('CcLazyWritePages', ULONG),
    ('CcDataFlushes', ULONG),
    ('CcDataPages', ULONG),
    ('CcLostDelayedWrites', ULONG),
    ('CcFastReadResourceMiss', ULONG),
    ('CcCopyReadWaitMiss', ULONG),
    ('CcFastMdlReadResourceMiss', ULONG),
    ('CcMapDataNoWaitMiss', ULONG),
    ('CcMapDataWaitMiss', ULONG),
    ('CcPinReadNoWaitMiss', ULONG),
    ('CcPinReadWaitMiss', ULONG),
    ('CcMdlReadNoWaitMiss', ULONG),
    ('CcMdlReadWaitMiss', ULONG),
    ('CcReadAheadIos', ULONG),
    ('KeAlignmentFixupCount', ULONG),
    ('KeExceptionDispatchCount', ULONG),
    ('KeSystemCalls', ULONG),
    ('PrcbPad1', ULONG * 3),
    ('PPLookasideList', PP_LOOKASIDE_LIST * 16),
    ('PPNPagedLookasideList', GENERAL_LOOKASIDE_POOL * 32),
    ('PPPagedLookasideList', GENERAL_LOOKASIDE_POOL * 32),
    ('PacketBarrier', ULONG),
    ('ReverseStall', LONG),
    ('IpiFrame', PVOID),
    ('PrcbPad2', UCHAR * 52),
    ('CurrentPacket', POINTER(VOID) * 3),
    ('TargetSet', ULONG),
    ('WorkerRoutine', PVOID),
    ('IpiFrozen', ULONG),
    ('PrcbPad3', UCHAR * 40),
    ('RequestSummary', ULONG),
    ('SignalDone', PKPRCB),
    ('PrcbPad4', UCHAR * 56),
    ('DpcData', KDPC_DATA * 2),
    ('DpcStack', PVOID),
    ('MaximumDpcQueueDepth', LONG),
    ('DpcRequestRate', ULONG),
    ('MinimumDpcRate', ULONG),
    ('DpcInterruptRequested', UCHAR),
    ('DpcThreadRequested', UCHAR),
    ('DpcRoutineActive', UCHAR),
    ('DpcThreadActive', UCHAR),
    ('PrcbLock', ULONG),
    ('DpcLastCount', ULONG),
    ('TimerHand', ULONG),
    ('TimerRequest', ULONG),
    ('PrcbPad41', PVOID),
    ('DpcEvent', KEVENT),
    ('ThreadDpcEnable', UCHAR),
    ('QuantumEnd', UCHAR),
    ('PrcbPad50', UCHAR),
    ('IdleSchedule', UCHAR),
    ('DpcSetEventRequest', LONG),
    ('Sleeping', LONG),
    ('PeriodicCount', ULONG),
    ('PeriodicBias', ULONG),
    ('PrcbPad5', UCHAR * 6),
    ('TickOffset', LONG),
    ('CallDpc', KDPC),
    ('ClockKeepAlive', LONG),
    ('ClockCheckSlot', UCHAR),
    ('ClockPollCycle', UCHAR),
    ('PrcbPad6', UCHAR * 2),
    ('DpcWatchdogPeriod', LONG),
    ('DpcWatchdogCount', LONG),
    ('ThreadWatchdogPeriod', LONG),
    ('ThreadWatchdogCount', LONG),
    ('PrcbPad70', ULONG * 2),
    ('WaitListHead', LIST_ENTRY),
    ('WaitLock', ULONG),
    ('ReadySummary', ULONG),
    ('QueueIndex', ULONG),
    ('DeferredReadyListHead', SINGLE_LIST_ENTRY),
    ('StartCycles', UINT64),
    ('CycleTime', UINT64),
    ('PrcbPad71', UINT64 * 3),
    ('DispatcherReadyListHead', LIST_ENTRY * 32),
    ('ChainedInterruptList', PVOID),
    ('LookasideIrpFloat', LONG),
    ('MmPageFaultCount', LONG),
    ('MmCopyOnWriteCount', LONG),
    ('MmTransitionCount', LONG),
    ('MmCacheTransitionCount', LONG),
    ('MmDemandZeroCount', LONG),
    ('MmPageReadCount', LONG),
    ('MmPageReadIoCount', LONG),
    ('MmCacheReadCount', LONG),
    ('MmCacheIoCount', LONG),
    ('MmDirtyPagesWriteCount', LONG),
    ('MmDirtyWriteIoCount', LONG),
    ('MmMappedPagesWriteCount', LONG),
    ('MmMappedWriteIoCount', LONG),
    ('CachedCommit', ULONG),
    ('CachedResidentAvailable', ULONG),
    ('HyperPte', PVOID),
    ('CpuVendor', UCHAR),
    ('PrcbPad9', UCHAR * 3),
    ('VendorString', UCHAR * 13),
    ('InitialApicId', UCHAR),
    ('CoresPerPhysicalProcessor', UCHAR),
    ('LogicalProcessorsPerPhysicalProcessor', UCHAR),
    ('MHz', ULONG),
    ('FeatureBits', ULONG),
    ('UpdateSignature', LARGE_INTEGER),
    ('IsrTime', UINT64),
    ('SpareField1', UINT64),
    ('NpxSaveArea', FX_SAVE_AREA),
    ('PowerState', PROCESSOR_POWER_STATE),
    ('DpcWatchdogDpc', KDPC),
    ('DpcWatchdogTimer', KTIMER),
    ('WheaInfo', PVOID),
    ('EtwSupport', PVOID),
    ('InterruptObjectPool', SLIST_HEADER),
    ('HypercallPagePhysical', LARGE_INTEGER),
    ('HypercallPageVirtual', PVOID),
    ('RateControl', PVOID),
    ('Cache', CACHE_DESCRIPTOR * 5),
    ('CacheCount', ULONG),
    ('CacheProcessorMask', ULONG * 5),
    ('LogicalProcessorsPerCore', UCHAR),
    ('PrcbPad8', UCHAR * 3),
    ('PackageProcessorSet', ULONG),
    ('CoreProcessorSet', ULONG),
]
_KSEMAPHORE._fields_ = [
    ('Header', DISPATCHER_HEADER),
    ('Limit', LONG),
]


class _Union_15(ctypes.Union):
    pass


_Union_15._fields_ = [
    ('ApcState', KAPC_STATE),
    ('ApcStateFill', UCHAR * 23),
]
_KTHREAD._Union_15 = _Union_15


class _Union_16(ctypes.Union):
    pass


_Union_16._fields_ = [
    ('WaitBlockList', PKWAIT_BLOCK),
    ('GateObject', PKGATE),
]
_KTHREAD._Union_16 = _Union_16


class _Union_17(ctypes.Union):
    pass


_Union_17._fields_ = [
    ('KernelStackResident', ULONG, 1),
    ('ReadyTransition', ULONG, 1),
    ('ProcessReadyQueue', ULONG, 1),
    ('WaitNext', ULONG, 1),
    ('SystemAffinityActive', ULONG, 1),
    ('Alertable', ULONG, 1),
    ('GdiFlushActive', ULONG, 1),
    ('Reserved', ULONG, 25),
    ('MiscFlags', LONG),
]
_KTHREAD._Union_17 = _Union_17


class _Union_18(ctypes.Union):
    pass


_Union_18._fields_ = [
    ('WaitListEntry', LIST_ENTRY),
    ('SwapListEntry', SINGLE_LIST_ENTRY),
]
_KTHREAD._Union_18 = _Union_18


class _Struct_3(ctypes.Structure):
    pass


class _Struct_4(ctypes.Structure):
    pass


_Struct_4._fields_ = [
    ('KernelApcDisable', SHORT),
    ('SpecialApcDisable', SHORT),
]
_Struct_3._Struct_4 = _Struct_4

_Struct_3._anonymous_ = (
    '_Struct_4',
)
_Struct_3._fields_ = [
    ('_Struct_4', _Struct_3._Struct_4),
    ('CombinedApcDisable', ULONG),
]
_KTHREAD._Struct_3 = _Struct_3


class _Union_19(ctypes.Union):
    pass


_Union_19._fields_ = [
    ('Timer', KTIMER),
    ('TimerFill', UCHAR * 40),
]
_KTHREAD._Union_19 = _Union_19


class _Union_20(ctypes.Union):
    pass


_Union_20._fields_ = [
    ('AutoAlignment', ULONG, 1),
    ('DisableBoost', ULONG, 1),
    ('EtwStackTraceApc1Inserted', ULONG, 1),
    ('EtwStackTraceApc2Inserted', ULONG, 1),
    ('CycleChargePending', ULONG, 1),
    ('CalloutActive', ULONG, 1),
    ('ApcQueueable', ULONG, 1),
    ('EnableStackSwap', ULONG, 1),
    ('GuiThread', ULONG, 1),
    ('ReservedFlags', ULONG, 23),
    ('ThreadFlags', LONG),
]
_KTHREAD._Union_20 = _Union_20


class _Struct_4(ctypes.Structure):
    pass


class _Struct_5(ctypes.Structure):
    pass


_Struct_5._fields_ = [
    ('WaitBlockFill0', UCHAR * 23),
    ('IdealProcessor', UCHAR),
]
_Struct_4._Struct_5 = _Struct_5


class _Struct_6(ctypes.Structure):
    pass


_Struct_6._fields_ = [
    ('WaitBlockFill1', UCHAR * 47),
    ('PreviousMode', CHAR),
]
_Struct_4._Struct_6 = _Struct_6


class _Struct_7(ctypes.Structure):
    pass


_Struct_7._fields_ = [
    ('WaitBlockFill2', UCHAR * 71),
    ('ResourceIndex', UCHAR),
]
_Struct_4._Struct_7 = _Struct_7

_Struct_4._anonymous_ = (
    '_Struct_5',
    '_Struct_6',
    '_Struct_7',
)
_Struct_4._fields_ = [
    ('WaitBlock', KWAIT_BLOCK * 4),
    ('_Struct_5', _Struct_4._Struct_5),
    ('_Struct_6', _Struct_4._Struct_6),
    ('_Struct_7', _Struct_4._Struct_7),
    ('WaitBlockFill3', UCHAR * 95),
]
_KTHREAD._Struct_4 = _Struct_4


class _Union_21(ctypes.Union):
    pass


_Union_21._fields_ = [
    ('CallbackStack', PVOID),
    ('CallbackDepth', ULONG),
]
_KTHREAD._Union_21 = _Union_21


class _Union_22(ctypes.Union):
    pass


_Union_22._fields_ = [
    ('SavedApcState', KAPC_STATE),
    ('SavedApcStateFill', UCHAR * 23),
]
_KTHREAD._Union_22 = _Union_22


class _Struct_5(ctypes.Structure):
    pass


class _Struct_6(ctypes.Structure):
    pass


_Struct_6._fields_ = [
    ('SuspendApcFill0', UCHAR * 1),
    ('Spare04', CHAR),
]
_Struct_5._Struct_6 = _Struct_6


class _Struct_7(ctypes.Structure):
    pass


_Struct_7._fields_ = [
    ('SuspendApcFill1', UCHAR * 3),
    ('QuantumReset', UCHAR),
]
_Struct_5._Struct_7 = _Struct_7


class _Struct_8(ctypes.Structure):
    pass


_Struct_8._fields_ = [
    ('SuspendApcFill2', UCHAR * 4),
    ('KernelTime', ULONG),
]
_Struct_5._Struct_8 = _Struct_8


class _Struct_9(ctypes.Structure):
    pass


_Struct_9._fields_ = [
    ('SuspendApcFill3', UCHAR * 36),
    ('WaitPrcb', PKPRCB),
]
_Struct_5._Struct_9 = _Struct_9


class _Struct_10(ctypes.Structure):
    pass


_Struct_10._fields_ = [
    ('SuspendApcFill4', UCHAR * 40),
    ('LegoData', PVOID),
]
_Struct_5._Struct_10 = _Struct_10

_Struct_5._anonymous_ = (
    '_Struct_6',
    '_Struct_7',
    '_Struct_8',
    '_Struct_9',
    '_Struct_10',
)
_Struct_5._fields_ = [
    ('SuspendApc', KAPC),
    ('_Struct_6', _Struct_5._Struct_6),
    ('_Struct_7', _Struct_5._Struct_7),
    ('_Struct_8', _Struct_5._Struct_8),
    ('_Struct_9', _Struct_5._Struct_9),
    ('_Struct_10', _Struct_5._Struct_10),
    ('SuspendApcFill5', UCHAR * 47),
]
_KTHREAD._Struct_5 = _Struct_5


class _Union_23(ctypes.Union):
    pass


_Union_23._fields_ = [
    ('SuspendSemaphore', KSEMAPHORE),
    ('SuspendSemaphorefill', UCHAR * 20),
]
_KTHREAD._Union_23 = _Union_23

_KTHREAD._anonymous_ = (
    '_Union_15',
    '_Union_16',
    '_Union_17',
    '_Union_18',
    '_Struct_3',
    '_Union_19',
    '_Union_20',
    '_Struct_4',
    '_Union_21',
    '_Union_22',
    '_Struct_5',
    '_Union_23',
)
_KTHREAD._fields_ = [
    ('Header', DISPATCHER_HEADER),
    ('CycleTime', UINT64),
    ('HighCycleTime', ULONG),
    ('QuantumTarget', UINT64),
    ('InitialStack', PVOID),
    ('StackLimit', PVOID),
    ('KernelStack', PVOID),
    ('ThreadLock', ULONG),
    ('_Union_15', _KTHREAD._Union_15),
    ('Priority', CHAR),
    ('NextProcessor', WORD),
    ('DeferredProcessor', WORD),
    ('ApcQueueLock', ULONG),
    ('ContextSwitches', ULONG),
    ('State', UCHAR),
    ('NpxState', UCHAR),
    ('WaitIrql', UCHAR),
    ('WaitMode', CHAR),
    ('WaitStatus', LONG),
    ('_Union_16', _KTHREAD._Union_16),
    ('_Union_17', _KTHREAD._Union_17),
    ('WaitReason', UCHAR),
    ('SwapBusy', UCHAR),
    ('Alerted', UCHAR * 2),
    ('_Union_18', _KTHREAD._Union_18),
    ('Queue', PKQUEUE),
    ('WaitTime', ULONG),
    ('_Struct_3', _KTHREAD._Struct_3),
    ('Teb', PVOID),
    ('_Union_19', _KTHREAD._Union_19),
    ('_Union_20', _KTHREAD._Union_20),
    ('_Struct_4', _KTHREAD._Struct_4),
    ('LargeStack', UCHAR),
    ('QueueListEntry', LIST_ENTRY),
    ('TrapFrame', PKTRAP_FRAME),
    ('FirstArgument', PVOID),
    ('_Union_21', _KTHREAD._Union_21),
    ('ServiceTable', PVOID),
    ('ApcStateIndex', UCHAR),
    ('BasePriority', CHAR),
    ('PriorityDecrement', CHAR),
    ('Preempted', UCHAR),
    ('AdjustReason', UCHAR),
    ('AdjustIncrement', CHAR),
    ('Spare01', UCHAR),
    ('Saturation', CHAR),
    ('SystemCallNumber', ULONG),
    ('Spare02', ULONG),
    ('UserAffinity', ULONG),
    ('Process', PKPROCESS),
    ('Affinity', ULONG),
    ('ApcStatePointer', PKAPC_STATE * 2),
    ('_Union_22', _KTHREAD._Union_22),
    ('FreezeCount', CHAR),
    ('SuspendCount', CHAR),
    ('UserIdealProcessor', UCHAR),
    ('Spare03', UCHAR),
    ('Iopl', UCHAR),
    ('Win32Thread', PVOID),
    ('StackBase', PVOID),
    ('_Struct_5', _KTHREAD._Struct_5),
    ('PowerState', UCHAR),
    ('UserTime', ULONG),
    ('_Union_23', _KTHREAD._Union_23),
    ('SListFaultCount', ULONG),
    ('ThreadListEntry', LIST_ENTRY),
    ('MutantListHead', LIST_ENTRY),
    ('SListFaultAddress', PVOID),
    ('MdlForLockedTeb', PVOID),
]
_KGDTENTRY._fields_ = [
    ('LimitLow', WORD),
    ('BaseLow', WORD),
    ('HighWord', ULONG),
]
_KIDTENTRY._fields_ = [
    ('Offset', WORD),
    ('Selector', WORD),
    ('Access', WORD),
    ('ExtendedOffset', WORD),
]
_KEXECUTE_OPTIONS._fields_ = [
    ('ExecuteDisable', ULONG, 1),
    ('ExecuteEnable', ULONG, 1),
    ('DisableThunkEmulation', ULONG, 1),
    ('Permanent', ULONG, 1),
    ('ExecuteDispatchEnable', ULONG, 1),
    ('ImageDispatchEnable', ULONG, 1),
    ('Spare', ULONG, 2),
]


class _Union_24(ctypes.Union):
    pass


_Union_24._fields_ = [
    ('AutoAlignment', ULONG, 1),
    ('DisableBoost', ULONG, 1),
    ('DisableQuantum', ULONG, 1),
    ('ReservedFlags', ULONG, 29),
    ('ProcessFlags', LONG),
]
_KPROCESS._Union_24 = _Union_24


class _Union_25(ctypes.Union):
    pass


_Union_25._fields_ = [
    ('Flags', KEXECUTE_OPTIONS),
    ('ExecuteOptions', UCHAR),
]
_KPROCESS._Union_25 = _Union_25

_KPROCESS._anonymous_ = (
    '_Union_24',
    '_Union_25',
)
_KPROCESS._fields_ = [
    ('Header', DISPATCHER_HEADER),
    ('ProfileListHead', LIST_ENTRY),
    ('DirectoryTableBase', ULONG),
    ('Unused0', ULONG),
    ('LdtDescriptor', KGDTENTRY),
    ('Int21Descriptor', KIDTENTRY),
    ('IopmOffset', WORD),
    ('Iopl', UCHAR),
    ('Unused', UCHAR),
    ('ActiveProcessors', ULONG),
    ('KernelTime', ULONG),
    ('UserTime', ULONG),
    ('ReadyListHead', LIST_ENTRY),
    ('SwapListEntry', SINGLE_LIST_ENTRY),
    ('VdmTrapcHandler', PVOID),
    ('ThreadListHead', LIST_ENTRY),
    ('ProcessLock', ULONG),
    ('Affinity', ULONG),
    ('_Union_24', _KPROCESS._Union_24),
    ('BasePriority', CHAR),
    ('QuantumReset', CHAR),
    ('State', UCHAR),
    ('ThreadSeed', UCHAR),
    ('PowerState', UCHAR),
    ('IdealNode', UCHAR),
    ('Visited', UCHAR),
    ('_Union_25', _KPROCESS._Union_25),
    ('StackCount', ULONG),
    ('ProcessListEntry', LIST_ENTRY),
    ('CycleTime', UINT64),
]


class _Union_26(ctypes.Union):
    pass


_Union_26._fields_ = [
    ('OwnerCount', LONG),
    ('TableSize', ULONG),
]
_OWNER_ENTRY._Union_26 = _Union_26

_OWNER_ENTRY._anonymous_ = (
    '_Union_26',
)
_OWNER_ENTRY._fields_ = [
    ('OwnerThread', ULONG),
    ('_Union_26', _OWNER_ENTRY._Union_26),
]


class _Union_27(ctypes.Union):
    pass


_Union_27._fields_ = [
    ('Address', PVOID),
    ('CreatorBackTraceIndex', ULONG),
]
_ERESOURCE._Union_27 = _Union_27

_ERESOURCE._anonymous_ = (
    '_Union_27',
)
_ERESOURCE._fields_ = [
    ('SystemResourcesList', LIST_ENTRY),
    ('OwnerTable', POWNER_ENTRY),
    ('ActiveCount', SHORT),
    ('Flag', WORD),
    ('SharedWaiters', PKSEMAPHORE),
    ('ExclusiveWaiters', PKEVENT),
    ('OwnerEntry', OWNER_ENTRY),
    ('ActiveEntries', ULONG),
    ('ContentionCount', ULONG),
    ('NumberOfSharedWaiters', ULONG),
    ('NumberOfExclusiveWaiters', ULONG),
    ('_Union_27', _ERESOURCE._Union_27),
    ('SpinLock', ULONG),
]
_GENERIC_MAPPING._fields_ = [
    ('GenericRead', ULONG),
    ('GenericWrite', ULONG),
    ('GenericExecute', ULONG),
    ('GenericAll', ULONG),
]
_OBJECT_TYPE_INITIALIZER._fields_ = [
    ('Length', WORD),
    ('ObjectTypeFlags', UCHAR),
    ('CaseInsensitive', ULONG, 1),
    ('UnnamedObjectsOnly', ULONG, 1),
    ('UseDefaultObject', ULONG, 1),
    ('SecurityRequired', ULONG, 1),
    ('MaintainHandleCount', ULONG, 1),
    ('MaintainTypeList', ULONG, 1),
    ('ObjectTypeCode', ULONG),
    ('InvalidAttributes', ULONG),
    ('GenericMapping', GENERIC_MAPPING),
    ('ValidAccessMask', ULONG),
    ('PoolType', POOL_TYPE),
    ('DefaultPagedPoolCharge', ULONG),
    ('DefaultNonPagedPoolCharge', ULONG),
    ('DumpProcedure', PVOID),
    ('OpenProcedure', POINTER(LONG)),
    ('CloseProcedure', PVOID),
    ('DeleteProcedure', PVOID),
    ('ParseProcedure', POINTER(LONG)),
    ('SecurityProcedure', POINTER(LONG)),
    ('QueryNameProcedure', POINTER(LONG)),
    ('OkayToCloseProcedure', POINTER(UCHAR)),
]


class _Union_28(ctypes.Union):
    pass


_Union_28._fields_ = [
    ('Locked', ULONG, 1),
    ('Waiting', ULONG, 1),
    ('Waking', ULONG, 1),
    ('MultipleShared', ULONG, 1),
    ('Shared', ULONG, 28),
    ('Value', ULONG),
    ('Ptr', PVOID),
]
_EX_PUSH_LOCK._Union_28 = _Union_28

_EX_PUSH_LOCK._anonymous_ = (
    '_Union_28',
)
_EX_PUSH_LOCK._fields_ = [
    ('_Union_28', _EX_PUSH_LOCK._Union_28),
]
_OBJECT_TYPE._fields_ = [
    ('Mutex', ERESOURCE),
    ('TypeList', LIST_ENTRY),
    ('Name', UNICODE_STRING),
    ('DefaultObject', PVOID),
    ('Index', ULONG),
    ('TotalNumberOfObjects', ULONG),
    ('TotalNumberOfHandles', ULONG),
    ('HighWaterNumberOfObjects', ULONG),
    ('HighWaterNumberOfHandles', ULONG),
    ('TypeInfo', OBJECT_TYPE_INITIALIZER),
    ('Key', ULONG),
    ('ObjectLocks', EX_PUSH_LOCK * 32),
]
_SECURITY_QUALITY_OF_SERVICE._fields_ = [
    ('Length', ULONG),
    ('ImpersonationLevel', SECURITY_IMPERSONATION_LEVEL),
    ('ContextTrackingMode', UCHAR),
    ('EffectiveOnly', UCHAR),
]
_IO_STACK_LOCATION._fields_ = [
    ('MajorFunction', UCHAR),
    ('MinorFunction', UCHAR),
    ('Flags', UCHAR),
    ('Control', UCHAR),
    ('Parameters', BYTE * 16),
    ('DeviceObject', PDEVICE_OBJECT),
    ('FileObject', PFILE_OBJECT),
    ('CompletionRoutine', POINTER(LONG)),
    ('Context', PVOID),
]
_FILE_GET_QUOTA_INFORMATION._fields_ = [
    ('NextEntryOffset', ULONG),
    ('SidLength', ULONG),
    ('Sid', SID),
]
_TERMINATION_PORT._fields_ = [
    ('Next', PTERMINATION_PORT),
    ('Port', PVOID),
]
_CLIENT_ID._fields_ = [
    ('UniqueProcess', PVOID),
    ('UniqueThread', PVOID),
]


class _Union_29(ctypes.Union):
    pass


_Union_29._fields_ = [
    ('ImpersonationData', ULONG),
    ('ImpersonationToken', PVOID),
    ('ImpersonationLevel', ULONG, 2),
    ('EffectiveOnly', ULONG, 1),
]
_PS_CLIENT_SECURITY_CONTEXT._Union_29 = _Union_29

_PS_CLIENT_SECURITY_CONTEXT._anonymous_ = (
    '_Union_29',
)
_PS_CLIENT_SECURITY_CONTEXT._fields_ = [
    ('_Union_29', _PS_CLIENT_SECURITY_CONTEXT._Union_29),
]


class _Union_30(ctypes.Union):
    pass


_Union_30._fields_ = [
    ('Count', ULONG),
    ('Ptr', PVOID),
]
_EX_RUNDOWN_REF._Union_30 = _Union_30

_EX_RUNDOWN_REF._anonymous_ = (
    '_Union_30',
)
_EX_RUNDOWN_REF._fields_ = [
    ('_Union_30', _EX_RUNDOWN_REF._Union_30),
]


class _Union_31(ctypes.Union):
    pass


_Union_31._fields_ = [
    ('NextApc', SINGLE_LIST_ENTRY),
    ('ExcessCycles', ULONGLONG),
]
_PSP_RATE_APC._Union_31 = _Union_31

_PSP_RATE_APC._anonymous_ = (
    '_Union_31',
)
_PSP_RATE_APC._fields_ = [
    ('_Union_31', _PSP_RATE_APC._Union_31),
    ('TargetGEneration', ULONGLONG),
    ('RateApc', KAPC),
]


class _Union_32(ctypes.Union):
    pass


_Union_32._fields_ = [
    ('ExitTime', LARGE_INTEGER),
    ('KeyedWaitChain', LIST_ENTRY),
]
_ETHREAD._Union_32 = _Union_32


class _Union_33(ctypes.Union):
    pass


_Union_33._fields_ = [
    ('ExitStatus', LONG),
    ('OfsChain', PVOID),
]
_ETHREAD._Union_33 = _Union_33


class _Struct_6(ctypes.Structure):
    pass


class _Struct_7(ctypes.Structure):
    pass


_Struct_7._fields_ = [
    ('ForwardLinkShadow', PVOID),
    ('StartAddress', PVOID),
]
_Struct_6._Struct_7 = _Struct_7

_Struct_6._anonymous_ = (
    '_Struct_7',
)
_Struct_6._fields_ = [
    ('PostBlockList', LIST_ENTRY),
    ('_Struct_7', _Struct_6._Struct_7),
]
_ETHREAD._Struct_6 = _Struct_6


class _Union_34(ctypes.Union):
    pass


_Union_34._fields_ = [
    ('TerminationPort', PTERMINATION_PORT),
    ('ReaperLink', PETHREAD),
    ('KeyedWaitValue', PVOID),
    ('Win32StartParameter', PVOID),
]
_ETHREAD._Union_34 = _Union_34


class _Union_35(ctypes.Union):
    pass


_Union_35._fields_ = [
    ('KeyedWaitSemaphore', KSEMAPHORE),
    ('AlpcWaitSemaphore', KSEMAPHORE),
]
_ETHREAD._Union_35 = _Union_35


class _Union_36(ctypes.Union):
    pass


_Union_36._fields_ = [
    ('AlpcMessage', PVOID),
    ('AlpcReceiveAttributeSet', ULONG),
]
_ETHREAD._Union_36 = _Union_36

_ETHREAD._anonymous_ = (
    '_Union_32',
    '_Union_33',
    '_Struct_6',
    '_Union_34',
    '_Union_35',
    '_Union_36',
)
_ETHREAD._fields_ = [
    ('Tcb', KTHREAD),
    ('CreateTime', LARGE_INTEGER),
    ('_Union_32', _ETHREAD._Union_32),
    ('_Union_33', _ETHREAD._Union_33),
    ('_Struct_6', _ETHREAD._Struct_6),
    ('_Union_34', _ETHREAD._Union_34),
    ('ActiveTimerListLock', ULONG),
    ('ActiveTimerListHead', LIST_ENTRY),
    ('Cid', CLIENT_ID),
    ('_Union_35', _ETHREAD._Union_35),
    ('ClientSecurity', PS_CLIENT_SECURITY_CONTEXT),
    ('IrpList', LIST_ENTRY),
    ('TopLevelIrp', ULONG),
    ('DeviceToVerify', PDEVICE_OBJECT),
    ('RateControlApc', POINTER(_PSP_RATE_APC)),
    ('Win32StartAddress', PVOID),
    ('SparePtr0', PVOID),
    ('ThreadListEntry', LIST_ENTRY),
    ('RundownProtect', EX_RUNDOWN_REF),
    ('ThreadLock', EX_PUSH_LOCK),
    ('ReadClusterSize', ULONG),
    ('MmLockOrdering', LONG),
    ('CrossThreadFlags', ULONG),
    ('Terminated', ULONG, 1),
    ('ThreadInserted', ULONG, 1),
    ('HideFromDebugger', ULONG, 1),
    ('ActiveImpersonationInfo', ULONG, 1),
    ('SystemThread', ULONG, 1),
    ('HardErrorsAreDisabled', ULONG, 1),
    ('BreakOnTermination', ULONG, 1),
    ('SkipCreationMsg', ULONG, 1),
    ('SkipTerminationMsg', ULONG, 1),
    ('CopyTokenOnOpen', ULONG, 1),
    ('ThreadIoPriority', ULONG, 3),
    ('ThreadPagePriority', ULONG, 3),
    ('RundownFail', ULONG, 1),
    ('SameThreadPassiveFlags', ULONG),
    ('ActiveExWorker', ULONG, 1),
    ('ExWorkerCanWaitUser', ULONG, 1),
    ('MemoryMaker', ULONG, 1),
    ('ClonedThread', ULONG, 1),
    ('KeyedEventInUse', ULONG, 1),
    ('RateApcState', ULONG, 2),
    ('SelfTerminate', ULONG, 1),
    ('SameThreadApcFlags', ULONG),
    ('Spare', ULONG, 1),
    ('StartAddressInvalid', ULONG, 1),
    ('EtwPageFaultCalloutActive', ULONG, 1),
    ('OwnsProcessWorkingSetExclusive', ULONG, 1),
    ('OwnsProcessWorkingSetShared', ULONG, 1),
    ('OwnsSystemWorkingSetExclusive', ULONG, 1),
    ('OwnsSystemWorkingSetShared', ULONG, 1),
    ('OwnsSessionWorkingSetExclusive', ULONG, 1),
    ('OwnsSessionWorkingSetShared', ULONG, 1),
    ('OwnsProcessAddressSpaceExclusive', ULONG, 1),
    ('OwnsProcessAddressSpaceShared', ULONG, 1),
    ('SuppressSymbolLoad', ULONG, 1),
    ('Prefetching', ULONG, 1),
    ('OwnsDynamicMemoryShared', ULONG, 1),
    ('OwnsChangeControlAreaExclusive', ULONG, 1),
    ('OwnsChangeControlAreaShared', ULONG, 1),
    ('PriorityRegionActive', ULONG, 4),
    ('CacheManagerActive', UCHAR),
    ('DisablePageFaultClustering', UCHAR),
    ('ActiveFaultCount', UCHAR),
    ('AlpcMessageId', ULONG),
    ('_Union_36', _ETHREAD._Union_36),
    ('AlpcWaitListEntry', LIST_ENTRY),
    ('CacheManagerCount', ULONG),
]
_FAST_MUTEX._fields_ = [
    ('Count', LONG),
    ('Owner', PKTHREAD),
    ('Contention', ULONG),
    ('Gate', KEVENT),
    ('OldIrql', ULONG),
]
_HANDLE_TRACE_DB_ENTRY._fields_ = [
    ('ClientId', CLIENT_ID),
    ('Handle', PVOID),
    ('Type', ULONG),
    ('StackTrace', POINTER(VOID) * 16),
]
_HANDLE_TRACE_DEBUG_INFO._fields_ = [
    ('RefCount', LONG),
    ('TableSize', ULONG),
    ('BitMaskFlags', ULONG),
    ('CloseCompactionLock', FAST_MUTEX),
    ('CurrentStackIndex', ULONG),
    ('TraceDb', HANDLE_TRACE_DB_ENTRY * 1),
]
_HANDLE_TABLE_ENTRY_INFO._fields_ = [
    ('AuditMask', ULONG32),
]


class _Union_37(ctypes.Union):
    pass


_Union_37._fields_ = [
    ('Object', POINTER(VOID)),
    ('ObAttributes', ULONG32),
    ('InfoTable', POINTER(_HANDLE_TABLE_ENTRY_INFO)),
    ('Value', UINT64),
]
_HANDLE_TABLE_ENTRY._Union_37 = _Union_37


class _Struct_7(ctypes.Structure):
    pass


class _Struct_8(ctypes.Structure):
    pass


_Struct_8._fields_ = [
    ('GrantedAccessIndex', UINT16),
    ('CreatorBackTraceIndex', UINT16),
    ('_PADDING0_', UINT8 * 0x4),
]
_Struct_7._Struct_8 = _Struct_8

_Struct_7._anonymous_ = (
    '_Struct_8',
)
_Struct_7._fields_ = [
    ('GrantedAccess', ULONG32),
    ('_Struct_8', _Struct_7._Struct_8),
    ('NextFreeTableEntry', ULONG32),
]
_HANDLE_TABLE_ENTRY._Struct_7 = _Struct_7

_HANDLE_TABLE_ENTRY._anonymous_ = (
    '_Union_37',
    '_Struct_7',
)
_HANDLE_TABLE_ENTRY._fields_ = [
    ('_Union_37', _HANDLE_TABLE_ENTRY._Union_37),
    ('_Struct_7', _HANDLE_TABLE_ENTRY._Struct_7),
]
_HANDLE_TABLE._fields_ = [
    ('TableCode', ULONG),
    ('QuotaProcess', PEPROCESS),
    ('UniqueProcessId', PVOID),
    ('HandleLock', EX_PUSH_LOCK),
    ('HandleTableList', LIST_ENTRY),
    ('HandleContentionEvent', EX_PUSH_LOCK),
    ('DebugInfo', PHANDLE_TRACE_DEBUG_INFO),
    ('ExtraInfoPages', LONG),
    ('Flags', ULONG),
    ('StrictFIFO', ULONG, 1),
    ('FirstFreeHandle', LONG),
    ('LastFreeHandleEntry', PHANDLE_TABLE_ENTRY),
    ('HandleCount', LONG),
    ('NextHandleNeedingPool', ULONG),
]


class _Union_38(ctypes.Union):
    pass


_Union_38._fields_ = [
    ('Object', PVOID),
    ('RefCnt', ULONG, 3),
    ('Value', ULONG),
]
_EX_FAST_REF._Union_38 = _Union_38

_EX_FAST_REF._anonymous_ = (
    '_Union_38',
)
_EX_FAST_REF._fields_ = [
    ('_Union_38', _EX_FAST_REF._Union_38),
]
_MMADDRESS_NODE._fields_ = [
    ('u1', ULONG),
    ('LeftChild', PMMADDRESS_NODE),
    ('RightChild', PMMADDRESS_NODE),
    ('StartingVpn', ULONG),
    ('EndingVpn', ULONG),
]
_MM_AVL_TABLE._fields_ = [
    ('BalancedRoot', MMADDRESS_NODE),
    ('DepthOfTree', ULONG, 5),
    ('Unused', ULONG, 3),
    ('NumberGenericTableElements', ULONG, 24),
    ('NodeHint', PVOID),
    ('NodeFreeHint', PVOID),
]
_EJOB._fields_ = [
    ('Event', KEVENT),
    ('JobLinks', LIST_ENTRY),
    ('ProcessListHead', LIST_ENTRY),
    ('JobLock', ERESOURCE),
    ('TotalUserTime', LARGE_INTEGER),
    ('TotalKernelTime', LARGE_INTEGER),
    ('ThisPeriodTotalUserTime', LARGE_INTEGER),
    ('ThisPeriodTotalKernelTime', LARGE_INTEGER),
    ('TotalPageFaultCount', ULONG),
    ('TotalProcesses', ULONG),
    ('ActiveProcesses', ULONG),
    ('TotalTerminatedProcesses', ULONG),
    ('PerProcessUserTimeLimit', LARGE_INTEGER),
    ('PerJobUserTimeLimit', LARGE_INTEGER),
    ('LimitFlags', ULONG),
    ('MinimumWorkingSetSize', ULONG),
    ('MaximumWorkingSetSize', ULONG),
    ('ActiveProcessLimit', ULONG),
    ('Affinity', ULONG),
    ('PriorityClass', UCHAR),
    ('AccessState', POINTER(_JOB_ACCESS_STATE)),
    ('UIRestrictionsClass', ULONG),
    ('EndOfJobTimeAction', ULONG),
    ('CompletionPort', PVOID),
    ('CompletionKey', PVOID),
    ('SessionId', ULONG),
    ('SchedulingClass', ULONG),
    ('ReadOperationCount', UINT64),
    ('WriteOperationCount', UINT64),
    ('OtherOperationCount', UINT64),
    ('ReadTransferCount', UINT64),
    ('WriteTransferCount', UINT64),
    ('OtherTransferCount', UINT64),
    ('ProcessMemoryLimit', ULONG),
    ('JobMemoryLimit', ULONG),
    ('PeakProcessMemoryUsed', ULONG),
    ('PeakJobMemoryUsed', ULONG),
    ('CurrentJobMemoryUsed', ULONG),
    ('MemoryLimitsLock', EX_PUSH_LOCK),
    ('JobSetLinks', LIST_ENTRY),
    ('MemberLevel', ULONG),
    ('JobFlags', ULONG),
]


class _Union_39(ctypes.Union):
    pass


_Union_39._fields_ = [
    ('Valid', ULONG, 1),
    ('Write', ULONG, 1),
    ('Owner', ULONG, 1),
    ('WriteThrough', ULONG, 1),
    ('CacheDisable', ULONG, 1),
    ('Accessed', ULONG, 1),
    ('Dirty', ULONG, 1),
    ('LargePage', ULONG, 1),
    ('Global', ULONG, 1),
    ('CopyOnWrite', ULONG, 1),
    ('Prototype', ULONG, 1),
    ('reserved0', ULONG, 1),
    ('PageFrameNumber', ULONG, 26),
    ('reserved1', ULONG, 26),
    ('LowPart', ULONG),
]
_HARDWARE_PTE._Union_39 = _Union_39

_HARDWARE_PTE._anonymous_ = (
    '_Union_39',
)
_HARDWARE_PTE._fields_ = [
    ('_Union_39', _HARDWARE_PTE._Union_39),
    ('HighPart', ULONG),
]
_PEB_LDR_DATA._fields_ = [
    ('Length', ULONG),
    ('Initialized', UCHAR),
    ('SsHandle', PVOID),
    ('InLoadOrderModuleList', LIST_ENTRY),
    ('InMemoryOrderModuleList', LIST_ENTRY),
    ('InInitializationOrderModuleList', LIST_ENTRY),
    ('EntryInProgress', PVOID),
]
_CURDIR._fields_ = [
    ('DosPath', UNICODE_STRING),
    ('Handle', PVOID),
]
_RTL_DRIVE_LETTER_CURDIR._fields_ = [
    ('Flags', WORD),
    ('Length', WORD),
    ('TimeStamp', ULONG),
    ('DosPath', STRING),
]
_RTL_USER_PROCESS_PARAMETERS._fields_ = [
    ('MaximumLength', ULONG),
    ('Length', ULONG),
    ('Flags', ULONG),
    ('DebugFlags', ULONG),
    ('ConsoleHandle', PVOID),
    ('ConsoleFlags', ULONG),
    ('StandardInput', PVOID),
    ('StandardOutput', PVOID),
    ('StandardError', PVOID),
    ('CurrentDirectory', CURDIR),
    ('DllPath', UNICODE_STRING),
    ('ImagePathName', UNICODE_STRING),
    ('CommandLine', UNICODE_STRING),
    ('Environment', PVOID),
    ('StartingX', ULONG),
    ('StartingY', ULONG),
    ('CountX', ULONG),
    ('CountY', ULONG),
    ('CountCharsX', ULONG),
    ('CountCharsY', ULONG),
    ('FillAttribute', ULONG),
    ('WindowFlags', ULONG),
    ('ShowWindowFlags', ULONG),
    ('WindowTitle', UNICODE_STRING),
    ('DesktopInfo', UNICODE_STRING),
    ('ShellInfo', UNICODE_STRING),
    ('RuntimeData', UNICODE_STRING),
    ('CurrentDirectores', RTL_DRIVE_LETTER_CURDIR * 32),
    ('EnvironmentSize', ULONG),
]
_RTL_CRITICAL_SECTION_DEBUG._fields_ = [
    ('Type', WORD),
    ('CreatorBackTraceIndex', WORD),
    ('CriticalSection', PRTL_CRITICAL_SECTION),
    ('ProcessLocksList', LIST_ENTRY),
    ('EntryCount', ULONG),
    ('ContentionCount', ULONG),
    ('Flags', ULONG),
    ('CreatorBackTraceIndexHigh', WORD),
    ('SpareUSHORT', WORD),
]
_RTL_CRITICAL_SECTION._fields_ = [
    ('DebugInfo', PRTL_CRITICAL_SECTION_DEBUG),
    ('LockCount', LONG),
    ('RecursionCount', LONG),
    ('OwningThread', PVOID),
    ('LockSemaphore', PVOID),
    ('SpinCount', ULONG),
]
_PEB_FREE_BLOCK._fields_ = [
    ('Next', PPEB_FREE_BLOCK),
    ('Size', ULONG),
]


class _Union_40(ctypes.Union):
    pass


_Union_40._fields_ = [
    ('KernelCallbackTable', PVOID),
    ('UserSharedInfoPtr', PVOID),
]
_PEB._Union_40 = _Union_40

_PEB._anonymous_ = (
    '_Union_40',
)
_PEB._fields_ = [
    ('InheritedAddressSpace', UCHAR),
    ('ReadImageFileExecOptions', UCHAR),
    ('BeingDebugged', UCHAR),
    ('BitField', UCHAR),
    ('ImageUsesLargePages', ULONG, 1),
    ('IsProtectedProcess', ULONG, 1),
    ('IsLegacyProcess', ULONG, 1),
    ('IsImageDynamicallyRelocated', ULONG, 1),
    ('SpareBits', ULONG, 4),
    ('Mutant', PVOID),
    ('ImageBaseAddress', PVOID),
    ('Ldr', PPEB_LDR_DATA),
    ('ProcessParameters', PRTL_USER_PROCESS_PARAMETERS),
    ('SubSystemData', PVOID),
    ('ProcessHeap', PVOID),
    ('FastPebLock', PRTL_CRITICAL_SECTION),
    ('AtlThunkSListPtr', PVOID),
    ('IFEOKey', PVOID),
    ('CrossProcessFlags', ULONG),
    ('ProcessInJob', ULONG, 1),
    ('ProcessInitializing', ULONG, 1),
    ('ReservedBits0', ULONG, 30),
    ('_Union_40', _PEB._Union_40),
    ('SystemReserved', ULONG * 1),
    ('SpareULONG', ULONG),
    ('FreeList', PPEB_FREE_BLOCK),
    ('TlsExpansionCounter', ULONG),
    ('TlsBitmap', PVOID),
    ('TlsBitmapBits', ULONG * 2),
    ('ReadOnlySharedMemoryBase', PVOID),
    ('HotpatchInformation', PVOID),
    ('ReadOnlyStaticServerData', POINTER(POINTER(VOID))),
    ('AnsiCodePageData', PVOID),
    ('OemCodePageData', PVOID),
    ('UnicodeCaseTableData', PVOID),
    ('NumberOfProcessors', ULONG),
    ('NtGlobalFlag', ULONG),
    ('CriticalSectionTimeout', LARGE_INTEGER),
    ('HeapSegmentReserve', ULONG),
    ('HeapSegmentCommit', ULONG),
    ('HeapDeCommitTotalFreeThreshold', ULONG),
    ('HeapDeCommitFreeBlockThreshold', ULONG),
    ('NumberOfHeaps', ULONG),
    ('MaximumNumberOfHeaps', ULONG),
    ('ProcessHeaps', POINTER(POINTER(VOID))),
    ('GdiSharedHandleTable', PVOID),
    ('ProcessStarterHelper', PVOID),
    ('GdiDCAttributeList', ULONG),
    ('LoaderLock', PRTL_CRITICAL_SECTION),
    ('OSMajorVersion', ULONG),
    ('OSMinorVersion', ULONG),
    ('OSBuildNumber', WORD),
    ('OSCSDVersion', WORD),
    ('OSPlatformId', ULONG),
    ('ImageSubsystem', ULONG),
    ('ImageSubsystemMajorVersion', ULONG),
    ('ImageSubsystemMinorVersion', ULONG),
    ('ImageProcessAffinityMask', ULONG),
    ('GdiHandleBuffer', ULONG * 34),
    ('PostProcessInitRoutine', PVOID),
    ('TlsExpansionBitmap', PVOID),
    ('TlsExpansionBitmapBits', ULONG * 32),
    ('SessionId', ULONG),
    ('AppCompatFlags', ULARGE_INTEGER),
    ('AppCompatFlagsUser', ULARGE_INTEGER),
    ('pShimData', PVOID),
    ('AppCompatInfo', PVOID),
    ('CSDVersion', UNICODE_STRING),
    ('ActivationContextData', POINTER(_ACTIVATION_CONTEXT_DATA)),
    ('ProcessAssemblyStorageMap', POINTER(_ASSEMBLY_STORAGE_MAP)),
    ('SystemDefaultActivationContextData', POINTER(_ACTIVATION_CONTEXT_DATA)),
    ('SystemAssemblyStorageMap', POINTER(_ASSEMBLY_STORAGE_MAP)),
    ('MinimumStackCommit', ULONG),
    ('FlsCallback', POINTER(_FLS_CALLBACK_INFO)),
    ('FlsListHead', LIST_ENTRY),
    ('FlsBitmap', PVOID),
    ('FlsBitmapBits', ULONG * 4),
    ('FlsHighIndex', ULONG),
    ('WerRegistrationData', PVOID),
    ('WerShipAssertPtr', PVOID),
]
_ALPC_PROCESS_CONTEXT._fields_ = [
    ('Lock', _EX_PUSH_LOCK),
    ('ViewListHead', _LIST_ENTRY),
    ('PagedPoolQuotaCache', UINT64),
]
_OBJECT_NAME_INFORMATION._fields_ = [
    ('Name', _UNICODE_STRING),
]
_SE_AUDIT_PROCESS_CREATION_INFO._fields_ = [
    ('ImageFileName', POINTER(_OBJECT_NAME_INFORMATION)),
]


class _Struct_8(ctypes.Structure):
    pass


_Struct_8._fields_ = [
    ('WorkingSetType', UINT8, 3),
    ('ModwriterAttached', UINT8, 1),
    ('TrimHard', UINT8, 1),
    ('MaximumWorkingSetHard', UINT8, 1),
    ('ForceTrim', UINT8, 1),
    ('MinimumWorkingSetHard', UINT8, 1),
]
_MMSUPPORT_FLAGS._Struct_8 = _Struct_8


class _Struct_9(ctypes.Structure):
    pass


_Struct_9._fields_ = [
    ('SessionMaster', UINT8, 1),
    ('TrimmerState', UINT8, 2),
    ('Reserved', UINT8, 1),
    ('PageStealers', UINT8, 4),
]
_MMSUPPORT_FLAGS._Struct_9 = _Struct_9


class _Struct_10(ctypes.Structure):
    pass


_Struct_10._fields_ = [
    ('WsleDeleted', UINT8, 1),
    ('VmExiting', UINT8, 1),
    ('ExpansionFailed', UINT8, 1),
    ('Available', UINT8, 5),
]
_MMSUPPORT_FLAGS._Struct_10 = _Struct_10

_MMSUPPORT_FLAGS._anonymous_ = (
    '_Struct_8',
    '_Struct_9',
    '_Struct_10',
)
_MMSUPPORT_FLAGS._fields_ = [
    ('_Struct_8', _MMSUPPORT_FLAGS._Struct_8),
    ('_Struct_9', _MMSUPPORT_FLAGS._Struct_9),
    ('MemoryPriority', UINT8, 8),
    ('_Struct_10', _MMSUPPORT_FLAGS._Struct_10),
]
_MMWSLE_HASH._fields_ = [
    ('Index', ULONG32),
]
_MMWSLE_NONDIRECT_HASH._fields_ = [
    ('Key', POINTER(VOID)),
    ('Index', ULONG32),
    ('_PADDING0_', UINT8 * 0x4),
]
_MMWSLENTRY._fields_ = [
    ('Valid', UINT64, 1),
    ('Spare', UINT64, 1),
    ('Hashed', UINT64, 1),
    ('Direct', UINT64, 1),
    ('Protection', UINT64, 5),
    ('Age', UINT64, 3),
    ('VirtualPageNumber', UINT64, 52),
]
_MMWSLE_FREE_ENTRY._fields_ = [
    ('MustBeZero', UINT64, 1),
    ('PreviousFree', UINT64, 31),
    ('NextFree', UINT64, 32),
]


class u1(ctypes.Union):
    pass


u1._fields_ = [
    ('VirtualAddress', POINTER(VOID)),
    ('Long', UINT64),
    ('e1', _MMWSLENTRY),
    ('e2', _MMWSLE_FREE_ENTRY),
]
_MMWSLE.u1 = u1

_MMWSLE._fields_ = [
    ('u1', _MMWSLE.u1),
]
_MMWSL._fields_ = [
    ('FirstFree', ULONG32),
    ('FirstDynamic', ULONG32),
    ('LastEntry', ULONG32),
    ('NextSlot', ULONG32),
    ('Wsle', POINTER(_MMWSLE)),
    ('LowestPagableAddress', POINTER(VOID)),
    ('LastInitializedWsle', ULONG32),
    ('NextAgingSlot', ULONG32),
    ('NumberOfCommittedPageTables', ULONG32),
    ('VadBitMapHint', ULONG32),
    ('NonDirectCount', ULONG32),
    ('LastVadBit', ULONG32),
    ('MaximumLastVadBit', ULONG32),
    ('LastAllocationSizeHint', ULONG32),
    ('LastAllocationSize', ULONG32),
    ('_PADDING0_', UINT8 * 0x4),
    ('NonDirectHash', POINTER(_MMWSLE_NONDIRECT_HASH)),
    ('HashTableStart', POINTER(_MMWSLE_HASH)),
    ('HighestPermittedHashAddress', POINTER(_MMWSLE_HASH)),
    ('MaximumUserPageTablePages', ULONG32),
    ('MaximumUserPageDirectoryPages', ULONG32),
    ('CommittedPageTables', POINTER(ULONG32)),
    ('NumberOfCommittedPageDirectories', ULONG32),
    ('_PADDING1_', UINT8 * 0x4),
    ('CommittedPageDirectories', UINT64 * 128),
    ('NumberOfCommittedPageDirectoryParents', ULONG32),
    ('_PADDING2_', UINT8 * 0x4),
    ('CommittedPageDirectoryParents', UINT64 * 1),
]
_MMSUPPORT._fields_ = [
    ('WorkingSetMutex', _EX_PUSH_LOCK),
    ('ExitGate', POINTER(_KGATE)),
    ('AccessLog', POINTER(VOID)),
    ('WorkingSetExpansionLinks', _LIST_ENTRY),
    ('AgeDistribution', ULONG32 * 7),
    ('MinimumWorkingSetSize', ULONG32),
    ('WorkingSetSize', ULONG32),
    ('WorkingSetPrivateSize', ULONG32),
    ('MaximumWorkingSetSize', ULONG32),
    ('ChargedWslePages', ULONG32),
    ('ActualWslePages', ULONG32),
    ('WorkingSetSizeOverhead', ULONG32),
    ('PeakWorkingSetSize', ULONG32),
    ('HardFaultCount', ULONG32),
    ('VmWorkingSetList', POINTER(_MMWSL)),
    ('NextPageColor', UINT16),
    ('LastTrimStamp', UINT16),
    ('PageFaultCount', ULONG32),
    ('RepurposeCount', ULONG32),
    ('Spare', ULONG32 * 2),
    ('Flags', _MMSUPPORT_FLAGS),
]


class _Union_41(ctypes.Union):
    pass


_Union_41._fields_ = [
    ('ExceptionPortData', PVOID),
    ('ExceptionPortValue', ULONG),
    ('ExceptionPortState', ULONG, 3),
]
_EPROCESS._Union_41 = _Union_41


class _Union_42(ctypes.Union):
    pass


_Union_42._fields_ = [
    ('PageDirectoryPte', HARDWARE_PTE),
    ('Filler', UINT64),
]
_EPROCESS._Union_42 = _Union_42


class _Struct_11(ctypes.Structure):
    pass


class _Struct_12(ctypes.Structure):
    pass


_Struct_12._fields_ = [
    ('SubSystemMinorVersion', UCHAR),
    ('SubSystemMajorVersion', UCHAR),
]
_Struct_11._Struct_12 = _Struct_12

_Struct_11._anonymous_ = (
    '_Struct_12',
)
_Struct_11._fields_ = [
    ('_Struct_12', _Struct_11._Struct_12),
    ('SubSystemVersion', WORD),
]
_EPROCESS._Struct_11 = _Struct_11

_EPROCESS._anonymous_ = (
    '_Union_41',
    '_Union_42',
    '_Struct_11',
)
_EPROCESS._fields_ = [
    ('Pcb', KPROCESS),
    ('ProcessLock', EX_PUSH_LOCK),
    ('CreateTime', LARGE_INTEGER),
    ('ExitTime', LARGE_INTEGER),
    ('RundownProtect', EX_RUNDOWN_REF),
    ('UniqueProcessId', PVOID),
    ('ActiveProcessLinks', LIST_ENTRY),
    ('QuotaUsage', ULONG * 3),
    ('QuotaPeak', ULONG * 3),
    ('CommitCharge', ULONG),
    ('PeakVirtualSize', ULONG),
    ('VirtualSize', ULONG),
    ('SessionProcessLinks', LIST_ENTRY),
    ('DebugPort', PVOID),
    ('_Union_41', _EPROCESS._Union_41),
    ('ObjectTable', PHANDLE_TABLE),
    ('Token', EX_FAST_REF),
    ('WorkingSetPage', ULONG),
    ('AddressCreationLock', EX_PUSH_LOCK),
    ('RotateInProgress', PETHREAD),
    ('ForkInProgress', PETHREAD),
    ('HardwareTrigger', ULONG),
    ('PhysicalVadRoot', PMM_AVL_TABLE),
    ('CloneRoot', PVOID),
    ('NumberOfPrivatePages', ULONG),
    ('NumberOfLockedPages', ULONG),
    ('Win32Process', PVOID),
    ('Job', PEJOB),
    ('SectionObject', PVOID),
    ('SectionBaseAddress', PVOID),
    ('QuotaBlock', POINTER(_EPROCESS_QUOTA_BLOCK)),
    ('WorkingSetWatch', POINTER(_PAGEFAULT_HISTORY)),
    ('Win32WindowStation', PVOID),
    ('InheritedFromUniqueProcessId', PVOID),
    ('LdtInformation', PVOID),
    ('VadFreeHint', PVOID),
    ('VdmObjects', PVOID),
    ('DeviceMap', PVOID),
    ('EtwDataSource', PVOID),
    ('FreeTebHint', PVOID),
    ('_Union_42', _EPROCESS._Union_42),
    ('Session', PVOID),
    ('ImageFileName', UCHAR * 16),
    ('JobLinks', LIST_ENTRY),
    ('LockedPagesList', PVOID),
    ('ThreadListHead', LIST_ENTRY),
    ('SecurityPort', PVOID),
    ('PaeTop', PVOID),
    ('ActiveThreads', ULONG),
    ('ImagePathHash', ULONG),
    ('DefaultHardErrorProcessing', ULONG),
    ('LastThreadExitStatus', LONG),
    ('Peb', PPEB),
    ('PrefetchTrace', EX_FAST_REF),
    ('ReadOperationCount', LARGE_INTEGER),
    ('WriteOperationCount', LARGE_INTEGER),
    ('OtherOperationCount', LARGE_INTEGER),
    ('ReadTransferCount', LARGE_INTEGER),
    ('WriteTransferCount', LARGE_INTEGER),
    ('OtherTransferCount', LARGE_INTEGER),
    ('CommitChargeLimit', ULONG),
    ('CommitChargePeak', ULONG),
    ('AweInfo', PVOID),
    ('SeAuditProcessCreationInfo', SE_AUDIT_PROCESS_CREATION_INFO),
    ('Vm', MMSUPPORT),
    ('MmProcessLinks', LIST_ENTRY),
    ('ModifiedPageCount', ULONG),
    ('Flags2', ULONG),
    ('JobNotReallyActive', ULONG, 1),
    ('AccountingFolded', ULONG, 1),
    ('NewProcessReported', ULONG, 1),
    ('ExitProcessReported', ULONG, 1),
    ('ReportCommitChanges', ULONG, 1),
    ('LastReportMemory', ULONG, 1),
    ('ReportPhysicalPageChanges', ULONG, 1),
    ('HandleTableRundown', ULONG, 1),
    ('NeedsHandleRundown', ULONG, 1),
    ('RefTraceEnabled', ULONG, 1),
    ('NumaAware', ULONG, 1),
    ('ProtectedProcess', ULONG, 1),
    ('DefaultPagePriority', ULONG, 3),
    ('PrimaryTokenFrozen', ULONG, 1),
    ('ProcessVerifierTarget', ULONG, 1),
    ('StackRandomizationDisabled', ULONG, 1),
    ('Flags', ULONG),
    ('CreateReported', ULONG, 1),
    ('NoDebugInherit', ULONG, 1),
    ('ProcessExiting', ULONG, 1),
    ('ProcessDelete', ULONG, 1),
    ('Wow64SplitPages', ULONG, 1),
    ('VmDeleted', ULONG, 1),
    ('OutswapEnabled', ULONG, 1),
    ('Outswapped', ULONG, 1),
    ('ForkFailed', ULONG, 1),
    ('Wow64VaSpace4Gb', ULONG, 1),
    ('AddressSpaceInitialized', ULONG, 2),
    ('SetTimerResolution', ULONG, 1),
    ('BreakOnTermination', ULONG, 1),
    ('DeprioritizeViews', ULONG, 1),
    ('WriteWatch', ULONG, 1),
    ('ProcessInSession', ULONG, 1),
    ('OverrideAddressSpace', ULONG, 1),
    ('HasAddressSpace', ULONG, 1),
    ('LaunchPrefetched', ULONG, 1),
    ('InjectInpageErrors', ULONG, 1),
    ('VmTopDown', ULONG, 1),
    ('ImageNotifyDone', ULONG, 1),
    ('PdeUpdateNeeded', ULONG, 1),
    ('VdmAllowed', ULONG, 1),
    ('SmapAllowed', ULONG, 1),
    ('ProcessInserted', ULONG, 1),
    ('DefaultIoPriority', ULONG, 3),
    ('SparePsFlags1', ULONG, 2),
    ('ExitStatus', LONG),
    ('Spare7', WORD),
    ('_Struct_11', _EPROCESS._Struct_11),
    ('PriorityClass', UCHAR),
    ('VadRoot', MM_AVL_TABLE),
    ('Cookie', ULONG),
    ('AlpcContext', ALPC_PROCESS_CONTEXT),
]
_SECTION_OBJECT_POINTERS._fields_ = [
    ('DataSectionObject', PVOID),
    ('SharedCacheMap', PVOID),
    ('ImageSectionObject', PVOID),
]
_IO_COMPLETION_CONTEXT._fields_ = [
    ('Port', PVOID),
    ('Key', PVOID),
]
_FILE_OBJECT._fields_ = [
    ('Type', SHORT),
    ('Size', SHORT),
    ('DeviceObject', PDEVICE_OBJECT),
    ('Vpb', PVPB),
    ('FsContext', PVOID),
    ('FsContext2', PVOID),
    ('SectionObjectPointer', PSECTION_OBJECT_POINTERS),
    ('PrivateCacheMap', PVOID),
    ('FinalStatus', LONG),
    ('RelatedFileObject', PFILE_OBJECT),
    ('LockOperation', UCHAR),
    ('DeletePending', UCHAR),
    ('ReadAccess', UCHAR),
    ('WriteAccess', UCHAR),
    ('DeleteAccess', UCHAR),
    ('SharedRead', UCHAR),
    ('SharedWrite', UCHAR),
    ('SharedDelete', UCHAR),
    ('Flags', ULONG),
    ('FileName', UNICODE_STRING),
    ('CurrentByteOffset', LARGE_INTEGER),
    ('Waiters', ULONG),
    ('Busy', ULONG),
    ('LastLock', PVOID),
    ('Lock', KEVENT),
    ('Event', KEVENT),
    ('CompletionContext', PIO_COMPLETION_CONTEXT),
    ('IrpListLock', ULONG),
    ('IrpList', LIST_ENTRY),
    ('FileObjectExtension', PVOID),
]

_DISPATCHER_HEADER._fields_ = [
    ('_Union_2', _DISPATCHER_HEADER._Union_2),
    ('SignalState', LONG),
    ('WaitListHead', LIST_ENTRY),
]

__all__ = (
    'PPPM_IDLE_STATE', 'PROCESSOR_CACHE_TYPE', '_EPROCESS_QUOTA_BLOCK',
    'CURDIR', 'PGENERAL_LOOKASIDE', 'HARDWARE_PTE', '_SLIST_HEADER',
    'PPM_IDLE_STATE_ACCOUNTING', 'PKPROCESSOR_STATE', 'PALPC_PROCESS_CONTEXT',
    'KTRAP_FRAME', '_FLS_CALLBACK_INFO', 'HANDLE_TABLE', '_DEVICE_OBJECT',
    'PPAGEFAULT_HISTORY', '_KINTERRUPT', '_KPROCESSOR_STATE', '_KTIMER',
    'FAST_IO_DISPATCH', 'EJOB', '_MMSUPPORT_FLAGS', 'PIRP', '_MMWSLE',
    'KPROCESSOR_STATE', '_ERESOURCE', 'PHANDLE_TABLE', 'PFLS_CALLBACK_INFO',
    'PPSP_RATE_APC', 'DISPATCHER_HEADER', 'MMWSLE_FREE_ENTRY', 'PMMWSL',
    'PEB_FREE_BLOCK', 'DRIVER_EXTENSION', '_MMADDRESS_NODE', 'PKAPC_STATE',
    '_KINTERRUPT_MODE', '_MDL', 'PFILE_GET_QUOTA_INFORMATION',
    'KSPIN_LOCK_QUEUE', 'PPM_PERF_STATES', 'PKIDTENTRY', '_MMWSLE_HASH',
    'PROCESSOR_POWER_STATE', 'PJOB_ACCESS_STATE', 'KGDTENTRY',
    '_RTL_CRITICAL_SECTION_DEBUG', 'EPROCESS_QUOTA_BLOCK', 'PMMSUPPORT',
    'PHARDWARE_PTE', '_PROCESSOR_POWER_STATE', 'EXCEPTION_REGISTRATION_RECORD',
    '_KQUEUE', '_HANDLE_TRACE_DB_ENTRY', '_FLOATING_SAVE_AREA',
    '_HANDLE_TABLE_ENTRY_INFO', 'DRIVER_OBJECT', 'IO_COMPLETION_CONTEXT',
    'PDEVOBJ_EXTENSION', 'PMMWSLE_FREE_ENTRY', '_MMSUPPORT', 'PEB_LDR_DATA',
    'POBJECT_TYPE', 'PIO_STACK_LOCATION', '_PAGEFAULT_HISTORY',
    '_PEB_FREE_BLOCK', '_CACHE_DESCRIPTOR', 'EX_RUNDOWN_REF',
    '_GENERAL_LOOKASIDE', '_PROCESSOR_CACHE_TYPE', 'POBJECT_NAME_INFORMATION',
    '_KINTERRUPT_POLARITY', 'PDRIVER_OBJECT', '_FILE_OBJECT', '_KTRAP_FRAME',
    'KEXECUTE_OPTIONS', '_GENERAL_LOOKASIDE_POOL', 'PMMWSLE_HASH', '_KPRCB',
    'CACHED_KSTACK_LIST', 'PPROCESSOR_POWER_STATE', 'MMWSLENTRY',
    'PPROCESSOR_IDLE_TIMES', 'PETHREAD', 'OWNER_ENTRY', '_DEVOBJ_EXTENSION',
    'PCACHED_KSTACK_LIST', 'PPM_IDLE_STATE', '_JOB_ACCESS_STATE',
    'PHANDLE_TABLE_ENTRY_INFO', '_CLIENT_ID', 'PRTL_CRITICAL_SECTION',
    '_FS_FILTER_CALLBACKS', '_SE_AUDIT_PROCESS_CREATION_INFO',
    '_IO_COMPLETION_CONTEXT', 'PKSPIN_LOCK_QUEUE',
    'PPS_CLIENT_SECURITY_CONTEXT', 'VPB', 'PIO_CLIENT_EXTENSION', 'PKDPC_DATA',
    '_EX_FAST_REF', 'EPROCESS', 'PKAPC', 'KTIMER', '_VPB',
    'PRTL_USER_PROCESS_PARAMETERS', 'RTL_CRITICAL_SECTION',
    'PHANDLE_TABLE_ENTRY', 'KQUEUE', 'PPP_LOOKASIDE_LIST', '_KDEVICE_QUEUE',
    '_FX_SAVE_AREA', 'SE_AUDIT_PROCESS_CREATION_INFO',
    'HANDLE_TRACE_DEBUG_INFO', 'PMMADDRESS_NODE', 'ASSEMBLY_STORAGE_MAP',
    'PCACHE_DESCRIPTOR', 'GENERAL_LOOKASIDE_POOL', 'PPPM_PERF_STATE', '_MMWSL',
    'PEX_RUNDOWN_REF', 'MMWSLE', '_TERMINATION_PORT', '_CACHED_KSTACK_LIST',
    'FS_FILTER_CALLBACKS', 'HANDLE_TABLE_ENTRY', 'ETHREAD', 'PPPM_PERF_STATES',
    'PPEB', 'PRTL_DRIVE_LETTER_CURDIR', 'PROCESSOR_IDLE_TIMES', '_KIDTENTRY',
    'KWAIT_BLOCK', 'RTL_DRIVE_LETTER_CURDIR', 'PHANDLE_TRACE_DB_ENTRY',
    'PDESCRIPTOR', '_SECURITY_QUALITY_OF_SERVICE',
    'SECURITY_IMPERSONATION_LEVEL', '_OBJECT_TYPE',
    'PRTL_CRITICAL_SECTION_DEBUG', 'KDPC', '_DRIVER_OBJECT', 'MMSUPPORT_FLAGS',
    'OBJECT_TYPE', 'MMSUPPORT', '_KEVENT', 'PVPB', 'PCURDIR', 'KAPC_STATE',
    'PKTHREAD', 'PMMWSLENTRY', 'IRP', 'PPPM_IDLE_STATES', '_CONTEXT', 'KGATE',
    'PMM_AVL_TABLE', '_IO_TIMER', 'PFAST_IO_DISPATCH',
    '_RTL_DRIVE_LETTER_CURDIR', 'PEPROCESS', 'PEB', '_HANDLE_TABLE_ENTRY',
    'PDEVICE_OBJECT_POWER_EXTENSION', 'PEJOB', '_RTL_USER_PROCESS_PARAMETERS',
    'PEXCEPTION_DISPOSITION', '_FILE_GET_QUOTA_INFORMATION',
    '_PS_CLIENT_SECURITY_CONTEXT', 'PGENERIC_MAPPING',
    'PSE_AUDIT_PROCESS_CREATION_INFO', 'KNODE', 'PEX_PUSH_LOCK',
    '_OBJECT_NAME_INFORMATION', 'PMDL', '_DEVICE_OBJECT_POWER_EXTENSION',
    '_MMWSLE_FREE_ENTRY', 'HANDLE_TABLE_ENTRY_INFO', 'PKINTERRUPT',
    'DEVICE_OBJECT_POWER_EXTENSION', '_SECURITY_IMPERSONATION_LEVEL',
    '_PP_LOOKASIDE_LIST', '_KDPC', 'PIO_COMPLETION_CONTEXT', '_IRP',
    'PPOWER_CHANNEL_SUMMARY', '_MMWSLENTRY', 'PP_LOOKASIDE_LIST',
    'IO_STATUS_BLOCK', 'KINTERRUPT_MODE', '_OWNER_ENTRY', 'MMWSL',
    'PFX_SAVE_AREA', '_EXCEPTION_DISPOSITION', 'KINTERRUPT',
    'FLOATING_SAVE_AREA', 'PFLOATING_SAVE_AREA', 'KTHREAD', '_POOL_TYPE',
    '_ACTIVATION_CONTEXT_DATA', '_KGDTENTRY', 'RTL_CRITICAL_SECTION_DEBUG',
    'PERESOURCE', 'PKEXECUTE_OPTIONS', 'DESCRIPTOR', 'CLIENT_ID',
    '_FAST_IO_DISPATCH', 'HANDLE_TRACE_DB_ENTRY', 'PTERMINATION_PORT',
    'PFAST_MUTEX', 'EXCEPTION_DISPOSITION', 'PFILE_OBJECT', 'KPRCB',
    '_KGATE', 'KDEVICE_QUEUE', '_KWAIT_BLOCK', 'PPPM_IDLE_STATE_ACCOUNTING',
    'PDEVICE_OBJECT', 'POBJECT_TYPE_INITIALIZER', '_DEVICE_POWER_STATE',
    '_KEXECUTE_OPTIONS', '_ASSEMBLY_STORAGE_MAP', '_FAST_MUTEX',
    '_POWER_CHANNEL_SUMMARY', 'KEVENT', 'PKEVENT', '_IO_CLIENT_EXTENSION',
    'PMMWSLE_NONDIRECT_HASH', '_PEB', 'KDPC_DATA', 'PKNODE',
    '_EXCEPTION_REGISTRATION_RECORD', '_IO_STACK_LOCATION',
    '_MMWSLE_NONDIRECT_HASH', '_EX_RUNDOWN_REF', 'PPEB_LDR_DATA',
    'MM_AVL_TABLE', 'PSECURITY_QUALITY_OF_SERVICE', '_CURDIR',
    'PPPM_IDLE_ACCOUNTING', 'PKDEVICE_QUEUE', 'PCONTEXT', 'MMWSLE_HASH',
    'ERESOURCE', 'PKDPC', 'PEXCEPTION_REGISTRATION_RECORD', 'PSLIST_HEADER',
    'PASSEMBLY_STORAGE_MAP', 'FILE_OBJECT', '_IO_STATUS_BLOCK',
    'PHANDLE_TRACE_DEBUG_INFO', 'DEVICE_OBJECT', '_KSPECIAL_REGISTERS',
    'DEVICE_POWER_STATE', '_KSEMAPHORE', 'PKTIMER', 'PEX_FAST_REF',
    'RTL_USER_PROCESS_PARAMETERS', '_KSPIN_LOCK_QUEUE', '_ETHREAD',
    'POWNER_ENTRY', '_HANDLE_TRACE_DEBUG_INFO', 'KPROCESS',
    '_ALPC_PROCESS_CONTEXT', 'ALPC_PROCESS_CONTEXT',
    'PS_CLIENT_SECURITY_CONTEXT', '_OBJECT_TYPE_INITIALIZER', '_DESCRIPTOR',
    'EX_PUSH_LOCK', 'DEVOBJ_EXTENSION', 'PAGEFAULT_HISTORY',
    'SECTION_OBJECT_POINTERS', 'MDL', '_EJOB', 'PIO_TIMER', 'IO_TIMER',
    'PCLIENT_ID', 'OBJECT_TYPE_INITIALIZER', '_DISPATCHER_HEADER',
    'SECURITY_QUALITY_OF_SERVICE', 'PSECTION_OBJECT_POINTERS',
    '_RTL_CRITICAL_SECTION', 'OBJECT_NAME_INFORMATION', 'PKPROCESS',
    'FX_SAVE_AREA', '_KAPC_STATE', 'PPEB_FREE_BLOCK', 'PDISPATCHER_HEADER',
    '_EX_PUSH_LOCK', 'CONTEXT', '_PEB_LDR_DATA', 'PKSEMAPHORE', '_EPROCESS',
    'PKQUEUE', 'KINTERRUPT_POLARITY', '_HANDLE_TABLE', '_DRIVER_EXTENSION',
    'KAPC', 'JOB_ACCESS_STATE', 'ACTIVATION_CONTEXT_DATA', 'PMMWSLE',
    'PMMSUPPORT_FLAGS', 'PGENERAL_LOOKASIDE_POOL', 'PSP_RATE_APC',
    'PACTIVATION_CONTEXT_DATA', '_HARDWARE_PTE', 'EX_FAST_REF',
    'PFS_FILTER_CALLBACKS', 'PKSPECIAL_REGISTERS', 'PDRIVER_EXTENSION',
    '_KDPC_DATA', 'FAST_MUTEX', '_KTHREAD', 'TERMINATION_PORT',
    'IO_CLIENT_EXTENSION', 'CACHE_DESCRIPTOR', 'GENERAL_LOOKASIDE',
    '_MM_AVL_TABLE', 'PKWAIT_BLOCK', '_GENERIC_MAPPING', 'PKPRCB',
    'KSEMAPHORE', '_SECTION_OBJECT_POINTERS', 'PKGATE', 'KIDTENTRY',
    'GENERIC_MAPPING', 'KSPECIAL_REGISTERS', 'PPM_PERF_STATE',
    'FILE_GET_QUOTA_INFORMATION', '_PSP_RATE_APC', 'PPM_IDLE_ACCOUNTING',
    'SLIST_HEADER', 'FLS_CALLBACK_INFO', 'PPM_IDLE_STATES', 'MMADDRESS_NODE',
    'PKGDTENTRY', 'PKTRAP_FRAME', 'PIO_STATUS_BLOCK', 'POOL_TYPE', '_KPROCESS',
    'IO_STACK_LOCATION', '_KNODE', '_KAPC', 'PEPROCESS_QUOTA_BLOCK',
    'POWER_CHANNEL_SUMMARY', 'MMWSLE_NONDIRECT_HASH'
)
