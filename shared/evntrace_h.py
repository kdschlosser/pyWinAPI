import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _EVENT_TRACE_HEADER(ctypes.Structure):
    pass


EVENT_TRACE_HEADER = _EVENT_TRACE_HEADER
PEVENT_TRACE_HEADER = POINTER(_EVENT_TRACE_HEADER)


class _EVENT_INSTANCE_HEADER(ctypes.Structure):
    pass

EVENT_INSTANCE_HEADER = _EVENT_INSTANCE_HEADER
PEVENT_INSTANCE_HEADER = POINTER(_EVENT_INSTANCE_HEADER)


class _MOF_FIELD(ctypes.Structure):
    pass

MOF_FIELD = _MOF_FIELD
PMOF_FIELD = POINTER(_MOF_FIELD)


class _TRACE_LOGFILE_HEADER(ctypes.Structure):
    pass

TRACE_LOGFILE_HEADER = _TRACE_LOGFILE_HEADER
PTRACE_LOGFILE_HEADER = POINTER(_TRACE_LOGFILE_HEADER)


class _TRACE_LOGFILE_HEADER32(ctypes.Structure):
    pass

TRACE_LOGFILE_HEADER32 = _TRACE_LOGFILE_HEADER32
PTRACE_LOGFILE_HEADER32 = POINTER(_TRACE_LOGFILE_HEADER32)


class _TRACE_LOGFILE_HEADER64(ctypes.Structure):
    pass

TRACE_LOGFILE_HEADER64 = _TRACE_LOGFILE_HEADER64
PTRACE_LOGFILE_HEADER64 = POINTER(_TRACE_LOGFILE_HEADER64)


class EVENT_INSTANCE_INFO(ctypes.Structure):
    pass

PEVENT_INSTANCE_INFO = POINTER(EVENT_INSTANCE_INFO)


class _EVENT_TRACE_PROPERTIES(ctypes.Structure):
    pass

EVENT_TRACE_PROPERTIES = _EVENT_TRACE_PROPERTIES
PEVENT_TRACE_PROPERTIES = POINTER(_EVENT_TRACE_PROPERTIES)


class _EVENT_TRACE_PROPERTIES_V2(ctypes.Structure):
    pass

EVENT_TRACE_PROPERTIES_V2 = _EVENT_TRACE_PROPERTIES_V2
PEVENT_TRACE_PROPERTIES_V2 = POINTER(_EVENT_TRACE_PROPERTIES_V2)


class _TRACE_GUID_REGISTRATION(ctypes.Structure):
    pass

TRACE_GUID_REGISTRATION = _TRACE_GUID_REGISTRATION
PTRACE_GUID_REGISTRATION = POINTER(_TRACE_GUID_REGISTRATION)


class _TRACE_GUID_PROPERTIES(ctypes.Structure):
    pass

TRACE_GUID_PROPERTIES = _TRACE_GUID_PROPERTIES
PTRACE_GUID_PROPERTIES = POINTER(_TRACE_GUID_PROPERTIES)


class _ETW_BUFFER_CONTEXT(ctypes.Structure):
    pass

ETW_BUFFER_CONTEXT = _ETW_BUFFER_CONTEXT
PETW_BUFFER_CONTEXT = POINTER(_ETW_BUFFER_CONTEXT)


class _TRACE_ENABLE_INFO(ctypes.Structure):
    pass

TRACE_ENABLE_INFO = _TRACE_ENABLE_INFO
PTRACE_ENABLE_INFO = POINTER(_TRACE_ENABLE_INFO)


class _TRACE_PROVIDER_INSTANCE_INFO(ctypes.Structure):
    pass

TRACE_PROVIDER_INSTANCE_INFO = _TRACE_PROVIDER_INSTANCE_INFO
PTRACE_PROVIDER_INSTANCE_INFO = POINTER(_TRACE_PROVIDER_INSTANCE_INFO)


class _TRACE_GUID_INFO(ctypes.Structure):
    pass

TRACE_GUID_INFO = _TRACE_GUID_INFO
PTRACE_GUID_INFO = POINTER(_TRACE_GUID_INFO)


class _PROFILE_SOURCE_INFO(ctypes.Structure):
    pass

PROFILE_SOURCE_INFO = _PROFILE_SOURCE_INFO
PPROFILE_SOURCE_INFO = POINTER(_PROFILE_SOURCE_INFO)


EVENT_TRACE = _EVENT_TRACE
PEVENT_TRACE = POINTER(_EVENT_TRACE)


class _EVENT_TRACE_LOGFILEW(ctypes.Structure):
    pass


class _EVENT_TRACE_LOGFILEA(ctypes.Structure):
    pass


class _ENABLE_TRACE_PARAMETERS_V1(ctypes.Structure):
    pass

ENABLE_TRACE_PARAMETERS_V1 = _ENABLE_TRACE_PARAMETERS_V1
PENABLE_TRACE_PARAMETERS_V1 = POINTER(_ENABLE_TRACE_PARAMETERS_V1)


ENABLE_TRACE_PARAMETERS = _ENABLE_TRACE_PARAMETERS
PENABLE_TRACE_PARAMETERS = POINTER(_ENABLE_TRACE_PARAMETERS)


class _CLASSIC_EVENT_ID(ctypes.Structure):
    pass

CLASSIC_EVENT_ID = _CLASSIC_EVENT_ID
PCLASSIC_EVENT_ID = POINTER(_CLASSIC_EVENT_ID)


class _TRACE_PROFILE_INTERVAL(ctypes.Structure):
    pass

TRACE_PROFILE_INTERVAL = _TRACE_PROFILE_INTERVAL
PTRACE_PROFILE_INTERVAL = POINTER(_TRACE_PROFILE_INTERVAL)


class _TRACE_VERSION_INFO(ctypes.Structure):
    pass

TRACE_VERSION_INFO = _TRACE_VERSION_INFO
PTRACE_VERSION_INFO = POINTER(_TRACE_VERSION_INFO)


class _TRACE_PERIODIC_CAPTURE_STATE_INFO(ctypes.Structure):
    pass

TRACE_PERIODIC_CAPTURE_STATE_INFO = _TRACE_PERIODIC_CAPTURE_STATE_INFO
PTRACE_PERIODIC_CAPTURE_STATE_INFO = POINTER(_TRACE_PERIODIC_CAPTURE_STATE_INFO)


class _ETW_TRACE_PARTITION_INFORMATION(ctypes.Structure):
    pass

ETW_TRACE_PARTITION_INFORMATION = _ETW_TRACE_PARTITION_INFORMATION
PETW_TRACE_PARTITION_INFORMATION = POINTER(_ETW_TRACE_PARTITION_INFORMATION)


from winapifamily_h import * # NOQA

# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: EvnTrace.h Abstract: Public headers for event tracing control
# applications, consumers and providers - -
if not defined(_EVNTRACE_):
    #~#~#~    #define _EVNTRACE_
    if _MSC_VER >= 1200:
        pass
    # END IF
    if defined(_WINNT_) or defined(WINNT):
        if not defined(NO_ETW_APP_DEPRECATION_WARNINGS):
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP) and not WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP) and not WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_SYSTEM):
            else:
                #~#~#~                #define ETW_APP_DECLSPEC_DEPRECATED            # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP) and not WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP) and not WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_SYSTEM)
        else:
            #~#~#~            #define ETW_APP_DECLSPEC_DEPRECATED        # END IF   NO_ETW_APP_DEPRECATION_WARNINGS
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            if not defined(WMIAPI):
                if not defined(MIDL_PASS):
                    if defined(_WMI_SOURCE_):
                        WMIAPI = __stdcall
                    else:
                        WMIAPI = DECLSPEC_IMPORT __stdcall
                    # END IF   _WMI_SOURCE
                # END IF   MIDL_PASS
            # END IF   WMIAPI
            from guiddef_h import * # NOQA
            if defined(_NTDDK_) or defined(_NTIFS_) or defined(_WMIKM_):
                #~#~#~                #define _EVNTRACE_KERNEL_MODE            # END IF
            if not defined(_EVNTRACE_KERNEL_MODE):
                from wmistr_h import * # NOQA
            # END IF
            # EventTraceGuid is used to identify a event tracing session
            DEFINE_GUID ( // 68fdd900 - 4a3e - 11d1 - 84f4 - 0000f80464e3 EventTraceGuid = DEFINE_GUID(
                0x68FDD900,
                0x4A3E,
                0x11D1,
                0x84,
                0xF4,
                0x00,
                0x00,
                0xF8,
                0x04,
                0x64,
                0xE3
            )
            # SystemTraceControlGuid. Used to specify event tracing for kernel
            DEFINE_GUID ( // 9e814aad - 3204 - 11d2 - 9a82 - 006008a86939 SystemTraceControlGuid = DEFINE_GUID(
                0x9E814AAD,
                0x3204,
                0x11D2,
                0x9A,
                0x82,
                0x00,
                0x60,
                0x08,
                0xA8,
                0x69,
                0x39
            )
            # EventTraceConfigGuid. Used to report system configuration records
            DEFINE_GUID ( // 01853a65 - 418f - 4f36 - aefc - dc0f1d2fd235 EventTraceConfigGuid = DEFINE_GUID(
                0x01853A65,
                0x418F,
                0x4F36,
                0xAE,
                0xFC,
                0xDC,
                0x0F,
                0x1D,
                0x2F,
                0xD2,
                0x35
            )
            # DefaultTraceSecurityGuid. Specifies the default event tracing
            # security
            DEFINE_GUID ( // 0811c1af - 7a07 - 4a06 - 82ed - 869455cdf713 DefaultTraceSecurityGuid = DEFINE_GUID(
                0x0811C1AF,
                0x7A07,
                0x4A06,
                0x82,
                0xED,
                0x86,
                0x94,
                0x55,
                0xCD,
                0xF7,
                0x13
            )
            # PrivateLoggerNotificationGuid
            # Used for private cross - process logger notifications.
            DEFINE_GUID ( // 3595ab5c - 042a - 4c8e - b942 - 2d059bfeb1b1 PrivateLoggerNotificationGuid = DEFINE_GUID(
                0x3595AB5C,
                0x042A,
                0x4C8E,
                0xB9,
                0x42,
                0x2D,
                0x05,
                0x9B,
                0xFE,
                0xB1,
                0xB1
            )
            KERNEL_LOGGER_NAMEW = "NT Kernel Logger"
            GLOBAL_LOGGER_NAMEW = "GlobalLogger"
            EVENT_LOGGER_NAMEW = "EventLog"
            DIAG_LOGGER_NAMEW = "DiagLog"
            KERNEL_LOGGER_NAMEA = "NT Kernel Logger"
            GLOBAL_LOGGER_NAMEA = "GlobalLogger"
            EVENT_LOGGER_NAMEA = "EventLog"
            DIAG_LOGGER_NAMEA = "DiagLog"
            MAX_MOF_FIELDS = 16            # Limit of USE_MOF_PTR fields
            if not defined(_TRACEHANDLE_DEFINED):
                #~#~#~                #define _TRACEHANDLE_DEFINED            # END IF
            # types for event data going to System Event Logger
            SYSTEM_EVENT_TYPE = 1


            # predefined generic event types (0x00 to 0x09 reserved).
            EVENT_TRACE_TYPE_INFO = 0x00            # Info or point event
            EVENT_TRACE_TYPE_START = 0x01            # Start event
            EVENT_TRACE_TYPE_END = 0x02            # End event
            EVENT_TRACE_TYPE_STOP = 0x02            # Stop event (WinEvent compatible)
            EVENT_TRACE_TYPE_DC_START = 0x03            # Collection start marker
            EVENT_TRACE_TYPE_DC_END = 0x04            # Collection end marker
            EVENT_TRACE_TYPE_EXTENSION = 0x05            # Extension/continuation
            EVENT_TRACE_TYPE_REPLY = 0x06            # Reply event
            EVENT_TRACE_TYPE_DEQUEUE = 0x07            # De - queue event
            EVENT_TRACE_TYPE_RESUME = 0x07            # Resume event (WinEvent compatible)
            EVENT_TRACE_TYPE_CHECKPOINT = 0x08            # Generic checkpoint event
            EVENT_TRACE_TYPE_SUSPEND = 0x08            # Suspend event (WinEvent compatible)
            EVENT_TRACE_TYPE_WINEVT_SEND = 0x09            # Send Event (WinEvent compatible)
            EVENT_TRACE_TYPE_WINEVT_RECEIVE = 0xF0            # Receive Event (WinEvent compatible)


            # Predefined Event Tracing Levels for Software/Debug Tracing
            # Trace Level is UCHAR and passed in through the EnableLevel
            # parameter
            # in EnableTrace API. It is retrieved by the provider using the
            # GetTraceEnableLevel macro.It should be interpreted as an integer
            # value
            # to mean everything at or below that level will be traced.
            # Here are the possible Levels.
            TRACE_LEVEL_NONE = 0            # Tracing is not on
            TRACE_LEVEL_CRITICAL = 1            # Abnormal exit or termination
            TRACE_LEVEL_FATAL = 1            # Deprecated name for Abnormal exit or termination
            TRACE_LEVEL_ERROR = 2            # Severe errors that need logging
            TRACE_LEVEL_WARNING = 3            # Warnings such as allocation failure
            TRACE_LEVEL_INFORMATION = 4            # Includes non - error cases(e.g.,Entry - Exit)
            TRACE_LEVEL_VERBOSE = 5            # Detailed traces from intermediate steps
            TRACE_LEVEL_RESERVED6 = 6
            TRACE_LEVEL_RESERVED7 = 7
            TRACE_LEVEL_RESERVED8 = 8
            TRACE_LEVEL_RESERVED9 = 9

            # Event types for Process & Threads
            EVENT_TRACE_TYPE_LOAD = 0x0A            # Load image
            EVENT_TRACE_TYPE_TERMINATE = 0x0B            # Terminate Process

            # Event types for IO subsystem
            EVENT_TRACE_TYPE_IO_READ = 0x0A
            EVENT_TRACE_TYPE_IO_WRITE = 0x0B
            EVENT_TRACE_TYPE_IO_READ_INIT = 0x0C
            EVENT_TRACE_TYPE_IO_WRITE_INIT = 0x0D
            EVENT_TRACE_TYPE_IO_FLUSH = 0x0E
            EVENT_TRACE_TYPE_IO_FLUSH_INIT = 0x0F
            EVENT_TRACE_TYPE_IO_REDIRECTED_INIT = 0x10

            # Event types for Memory subsystem
            EVENT_TRACE_TYPE_MM_TF = 0x0A            # Transition fault
            EVENT_TRACE_TYPE_MM_DZF = 0x0B            # Demand Zero fault
            EVENT_TRACE_TYPE_MM_COW = 0x0C            # Copy on Write
            EVENT_TRACE_TYPE_MM_GPF = 0x0D            # Guard Page fault
            EVENT_TRACE_TYPE_MM_HPF = 0x0E            # Hard page fault
            EVENT_TRACE_TYPE_MM_AV = 0x0F            # Access violation

            # Event types for Network subsystem, all protocols
            EVENT_TRACE_TYPE_SEND = 0x0A            # Send
            EVENT_TRACE_TYPE_RECEIVE = 0x0B            # Receive
            EVENT_TRACE_TYPE_CONNECT = 0x0C            # Connect
            EVENT_TRACE_TYPE_DISCONNECT = 0x0D            # Disconnect
            EVENT_TRACE_TYPE_RETRANSMIT = 0x0E            # ReTransmit
            EVENT_TRACE_TYPE_ACCEPT = 0x0F            # Accept
            EVENT_TRACE_TYPE_RECONNECT = 0x10            # ReConnect
            EVENT_TRACE_TYPE_CONNFAIL = 0x11            # Fail
            EVENT_TRACE_TYPE_COPY_TCP = 0x12            # Copy in PendData
            EVENT_TRACE_TYPE_COPY_ARP = 0x13            # NDIS_STATUS_RESOURCES Copy
            EVENT_TRACE_TYPE_ACKFULL = 0x14            # A full data ACK
            EVENT_TRACE_TYPE_ACKPART = 0x15            # A Partial data ACK
            EVENT_TRACE_TYPE_ACKDUP = 0x16            # A Duplicate data ACK

            # Event Types for the Header (to handle internal event headers)
            EVENT_TRACE_TYPE_GUIDMAP = 0x0A
            EVENT_TRACE_TYPE_CONFIG = 0x0B
            EVENT_TRACE_TYPE_SIDINFO = 0x0C
            EVENT_TRACE_TYPE_SECURITY = 0x0D
            EVENT_TRACE_TYPE_DBGID_RSDS = 0x40

            # Event Types for Registry subsystem
            EVENT_TRACE_TYPE_REGCREATE = 0x0A            # NtCreateKey
            EVENT_TRACE_TYPE_REGOPEN = 0x0B            # NtOpenKey
            EVENT_TRACE_TYPE_REGDELETE = 0x0C            # NtDeleteKey
            EVENT_TRACE_TYPE_REGQUERY = 0x0D            # NtQueryKey
            EVENT_TRACE_TYPE_REGSETVALUE = 0x0E            # NtSetValueKey
            EVENT_TRACE_TYPE_REGDELETEVALUE = 0x0F            # NtDeleteValueKey
            EVENT_TRACE_TYPE_REGQUERYVALUE = 0x10            # NtQueryValueKey
            EVENT_TRACE_TYPE_REGENUMERATEKEY = 0x11            # NtEnumerateKey
            EVENT_TRACE_TYPE_REGENUMERATEVALUEKEY = 0x12            # NtEnumerateValueKey
            EVENT_TRACE_TYPE_REGQUERYMULTIPLEVALUE = 0x13            # NtQueryMultipleValueKey
            EVENT_TRACE_TYPE_REGSETINFORMATION = 0x14            # NtSetInformationKey
            EVENT_TRACE_TYPE_REGFLUSH = 0x15            # NtFlushKey
            EVENT_TRACE_TYPE_REGKCBCREATE = 0x16            # KcbCreate
            EVENT_TRACE_TYPE_REGKCBDELETE = 0x17            # KcbDelete
            EVENT_TRACE_TYPE_REGKCBRUNDOWNBEGIN = 0x18            # KcbRundownBegin
            EVENT_TRACE_TYPE_REGKCBRUNDOWNEND = 0x19            # KcbRundownEnd
            EVENT_TRACE_TYPE_REGVIRTUALIZE = 0x1A            # VirtualizeKey
            EVENT_TRACE_TYPE_REGCLOSE = 0x1B            # NtClose (KeyObject)
            EVENT_TRACE_TYPE_REGSETSECURITY = 0x1C            # SetSecurityDescriptor (KeyObject)
            EVENT_TRACE_TYPE_REGQUERYSECURITY = 0x1D            # QuerySecurityDescriptor (KeyObject)
            EVENT_TRACE_TYPE_REGCOMMIT = 0x1E            # CmKtmNotification (TRANSACTION_NOTIFY_COMMIT)
            EVENT_TRACE_TYPE_REGPREPARE = 0x1F            # CmKtmNotification (TRANSACTION_NOTIFY_PREPARE)
            EVENT_TRACE_TYPE_REGROLLBACK = 0x20            # CmKtmNotification (TRANSACTION_NOTIFY_ROLLBACK)
            EVENT_TRACE_TYPE_REGMOUNTHIVE = 0x21            # NtLoadKey variations + system hives

            # Event types for system configuration records
            EVENT_TRACE_TYPE_CONFIG_CPU = 0x0A            # CPU Configuration
            EVENT_TRACE_TYPE_CONFIG_PHYSICALDISK = 0x0B            # Physical Disk Configuration
            EVENT_TRACE_TYPE_CONFIG_LOGICALDISK = 0x0C            # Logical Disk Configuration
            EVENT_TRACE_TYPE_CONFIG_NIC = 0x0D            # NIC Configuration
            EVENT_TRACE_TYPE_CONFIG_VIDEO = 0x0E            # Video Adapter Configuration
            EVENT_TRACE_TYPE_CONFIG_SERVICES = 0x0F            # Active Services
            EVENT_TRACE_TYPE_CONFIG_POWER = 0x10            # ACPI Configuration
            EVENT_TRACE_TYPE_CONFIG_NETINFO = 0x11            # Networking Configuration
            EVENT_TRACE_TYPE_CONFIG_OPTICALMEDIA = 0x12            # Optical Media Configuration
            EVENT_TRACE_TYPE_CONFIG_IRQ = 0x15            # IRQ assigned to devices
            EVENT_TRACE_TYPE_CONFIG_PNP = 0x16            # PnP device info
            EVENT_TRACE_TYPE_CONFIG_IDECHANNEL = 0x17            # Primary/Secondary IDE channel Configuration
            EVENT_TRACE_TYPE_CONFIG_NUMANODE = 0x18            # Numa configuration
            EVENT_TRACE_TYPE_CONFIG_PLATFORM = 0x19            # Platform Configuration
            EVENT_TRACE_TYPE_CONFIG_PROCESSORGROUP = 0x1A            # Processor Group Configuration
            EVENT_TRACE_TYPE_CONFIG_PROCESSORNUMBER = 0x1B            # ProcessorIndex - > ProcNumber mapping
            EVENT_TRACE_TYPE_CONFIG_DPI = 0x1C            # Display DPI Configuration
            EVENT_TRACE_TYPE_CONFIG_CI_INFO = 0x1D            # Display System Code Integrity Information
            EVENT_TRACE_TYPE_CONFIG_MACHINEID = 0x1E            # SQM Machine Id
            EVENT_TRACE_TYPE_CONFIG_DEFRAG = 0x1F            # Logical Disk Defragmenter Information
            EVENT_TRACE_TYPE_CONFIG_MOBILEPLATFORM = 0x20            # Mobile Platform Configuration
            EVENT_TRACE_TYPE_CONFIG_DEVICEFAMILY = 0x21            # Device Family Information
            EVENT_TRACE_TYPE_CONFIG_FLIGHTID = 0x22            # Flights on the machine
            EVENT_TRACE_TYPE_CONFIG_PROCESSOR = 0x23            # CentralProcessor records

            # Event types for Optical IO subsystem
            EVENT_TRACE_TYPE_OPTICAL_IO_READ = 0x37
            EVENT_TRACE_TYPE_OPTICAL_IO_WRITE = 0x38
            EVENT_TRACE_TYPE_OPTICAL_IO_FLUSH = 0x39
            EVENT_TRACE_TYPE_OPTICAL_IO_READ_INIT = 0x3A
            EVENT_TRACE_TYPE_OPTICAL_IO_WRITE_INIT = 0x3B
            EVENT_TRACE_TYPE_OPTICAL_IO_FLUSH_INIT = 0x3C

            # Event types for Filter Manager
            EVENT_TRACE_TYPE_FLT_PREOP_INIT = 0x60            # Minifilter preop initiation
            EVENT_TRACE_TYPE_FLT_POSTOP_INIT = 0x61            # Minifilter postop initiation
            EVENT_TRACE_TYPE_FLT_PREOP_COMPLETION = 0x62            # Minifilter preop completion
            EVENT_TRACE_TYPE_FLT_POSTOP_COMPLETION = 0x63            # Minifilter postop completion
            EVENT_TRACE_TYPE_FLT_PREOP_FAILURE = 0x64            # Minifilter failed preop
            EVENT_TRACE_TYPE_FLT_POSTOP_FAILURE = 0x65            # Minifilter failed postop

            # Enable flags for Kernel Events
            EVENT_TRACE_FLAG_PROCESS = 0x00000001            # process start & end
            EVENT_TRACE_FLAG_THREAD = 0x00000002            # thread start & end
            EVENT_TRACE_FLAG_IMAGE_LOAD = 0x00000004            # image load
            EVENT_TRACE_FLAG_DISK_IO = 0x00000100            # physical disk IO
            EVENT_TRACE_FLAG_DISK_FILE_IO = 0x00000200            # requires disk IO
            EVENT_TRACE_FLAG_MEMORY_PAGE_FAULTS = 0x00001000            # all page faults
            EVENT_TRACE_FLAG_MEMORY_HARD_FAULTS = 0x00002000            # hard faults only
            EVENT_TRACE_FLAG_NETWORK_TCPIP = 0x00010000            # tcpip send & receive
            EVENT_TRACE_FLAG_REGISTRY = 0x00020000            # registry calls
            EVENT_TRACE_FLAG_DBGPRINT = 0x00040000            # DbgPrint(ex) Calls

            # Enable flags for Kernel Events on Vista and above
            EVENT_TRACE_FLAG_PROCESS_COUNTERS = 0x00000008            # process perf counters
            EVENT_TRACE_FLAG_CSWITCH = 0x00000010            # context switches
            EVENT_TRACE_FLAG_DPC = 0x00000020            # deferred procedure calls
            EVENT_TRACE_FLAG_INTERRUPT = 0x00000040            # interrupts
            EVENT_TRACE_FLAG_SYSTEMCALL = 0x00000080            # system calls
            EVENT_TRACE_FLAG_DISK_IO_INIT = 0x00000400            # physical disk IO initiation
            EVENT_TRACE_FLAG_ALPC = 0x00100000            # ALPC traces
            EVENT_TRACE_FLAG_SPLIT_IO = 0x00200000            # split io traces (VolumeManager)
            EVENT_TRACE_FLAG_DRIVER = 0x00800000            # driver delays
            EVENT_TRACE_FLAG_PROFILE = 0x01000000            # sample based profiling
            EVENT_TRACE_FLAG_FILE_IO = 0x02000000            # file IO
            EVENT_TRACE_FLAG_FILE_IO_INIT = 0x04000000            # file IO initiation

            # Enable flags for Kernel Events on Win7 and above
            EVENT_TRACE_FLAG_DISPATCHER = 0x00000800            # scheduler (ReadyThread)
            EVENT_TRACE_FLAG_VIRTUAL_ALLOC = 0x00004000            # VM operations

            # Enable flags for Kernel Events on Win8 and above
            EVENT_TRACE_FLAG_VAMAP = 0x00008000            # map/unmap (excluding images)
            EVENT_TRACE_FLAG_NO_SYSCONFIG = 0x10000000            # Do not do sys config rundown

            # Enable flags for Kernel Events on Threshold and above
            EVENT_TRACE_FLAG_JOB = 0x00080000            # job start & end
            EVENT_TRACE_FLAG_DEBUG_EVENTS = 0x00400000            # debugger events (break/continue/...)

            # Pre - defined Enable flags for everybody else
            EVENT_TRACE_FLAG_EXTENSION = 0x80000000            # Indicates more flags
            EVENT_TRACE_FLAG_FORWARD_WMI = 0x40000000            # Can forward to WMI
            EVENT_TRACE_FLAG_ENABLE_RESERVE = 0x20000000            # Reserved

            # Logger Mode flags
            EVENT_TRACE_FILE_MODE_NONE = 0x00000000            # Logfile is off
            EVENT_TRACE_FILE_MODE_SEQUENTIAL = 0x00000001            # Log sequentially
            EVENT_TRACE_FILE_MODE_CIRCULAR = 0x00000002            # Log in circular manner
            EVENT_TRACE_FILE_MODE_APPEND = 0x00000004            # Append sequential log
            EVENT_TRACE_REAL_TIME_MODE = 0x00000100            # Real time mode on
            EVENT_TRACE_DELAY_OPEN_FILE_MODE = 0x00000200            # Delay opening file
            EVENT_TRACE_BUFFERING_MODE = 0x00000400            # Buffering mode only
            EVENT_TRACE_PRIVATE_LOGGER_MODE = 0x00000800            # Process Private Logger
            EVENT_TRACE_ADD_HEADER_MODE = 0x00001000            # Add a logfile header
            EVENT_TRACE_USE_GLOBAL_SEQUENCE = 0x00004000            # Use global sequence no.
            EVENT_TRACE_USE_LOCAL_SEQUENCE = 0x00008000            # Use local sequence no.
            EVENT_TRACE_RELOG_MODE = 0x00010000            # Relogger
            EVENT_TRACE_USE_PAGED_MEMORY = 0x01000000            # Use pageable buffers

            # Logger Mode flags on XP and above
            EVENT_TRACE_FILE_MODE_NEWFILE = 0x00000008            # Auto - switch log file
            EVENT_TRACE_FILE_MODE_PREALLOCATE = 0x00000020            # Pre - allocate mode

            # Logger Mode flags on Vista and above
            EVENT_TRACE_NONSTOPPABLE_MODE = 0x00000040            # Session cannot be stopped (Autologger only)
            EVENT_TRACE_SECURE_MODE = 0x00000080            # Secure session
            EVENT_TRACE_USE_KBYTES_FOR_SIZE = 0x00002000            # Use KBytes as file size unit
            EVENT_TRACE_PRIVATE_IN_PROC = 0x00020000            # In process private logger
            EVENT_TRACE_MODE_RESERVED = 0x00100000            # Reserved bit, used to signal Heap/Critsec tracing

            # Logger Mode flags on Win7 and above
            EVENT_TRACE_NO_PER_PROCESSOR_BUFFERING = 0x10000000            # Use this for low frequency sessions.

            # Logger Mode flags on Win8 and above
            EVENT_TRACE_SYSTEM_LOGGER_MODE = 0x02000000            # Receive events from SystemTraceProvider
            EVENT_TRACE_ADDTO_TRIAGE_DUMP = 0x80000000            # Add ETW buffers to triage dumps
            EVENT_TRACE_STOP_ON_HYBRID_SHUTDOWN = 0x00400000            # Stop on hybrid shutdown
            EVENT_TRACE_PERSIST_ON_HYBRID_SHUTDOWN = 0x00800000            # Persist on hybrid shutdown

            # Logger Mode flags on Blue and above
            EVENT_TRACE_INDEPENDENT_SESSION_MODE = 0x08000000            # Independent logger session

            # Logger Mode flags on Redstone and above
            EVENT_TRACE_COMPRESSED_MODE = 0x04000000            # Compressed logger session.

            # ControlTrace Codes
            EVENT_TRACE_CONTROL_QUERY = 0
            EVENT_TRACE_CONTROL_STOP = 1
            EVENT_TRACE_CONTROL_UPDATE = 2

            # Flush ControlTrace Codes for XP and above
            EVENT_TRACE_CONTROL_FLUSH = 3            # Flushes all the buffers

            # Flags used by WMI Trace Message
            # Note that the order or value of these flags should NOT be
            # changed as they are processed
            # in this order.
            TRACE_MESSAGE_SEQUENCE = 1            # Message should include a sequence number
            TRACE_MESSAGE_GUID = 2            # Message includes a GUID
            TRACE_MESSAGE_COMPONENTID = 4            # Message has no GUID, Component ID instead
            TRACE_MESSAGE_TIMESTAMP = 8            # Message includes a timestamp
            TRACE_MESSAGE_PERFORMANCE_TIMESTAMP = 16            # *Obsolete* Clock type is controlled by the logger
            TRACE_MESSAGE_SYSTEMINFO = 32            # Message includes system information TID,PID

            # Vista flags set by system to indicate provider pointer size.
            TRACE_MESSAGE_POINTER32 = 0x0040            # Message logged by 32 bit provider
            TRACE_MESSAGE_POINTER64 = 0x0080            # Message logged by 64 bit provider
            TRACE_MESSAGE_FLAG_MASK = 0xFFFF            # Only the lower 16 bits of flags are placed in the message

            # those above 16 bits are reserved for local processing
            # Maximum size allowed for a single TraceMessage message.
            # N.B. This limit was increased from 8K to 64K in Win8.
            TRACE_MESSAGE_MAXIMUM_SIZE = 64 * 1024


            # Flags to indicate to consumer which fields
            # in the EVENT_TRACE_HEADER are valid
            EVENT_TRACE_USE_PROCTIME = 0x0001            # ProcessorTime field is valid
            EVENT_TRACE_USE_NOCPUTIME = 0x0002            # No Kernel/User/Processor Times


            # TRACE_HEADER_FLAG values are used in the Flags field of
            # EVENT_TRACE_HEADER
            # structure while calling into TraceEvent API
            TRACE_HEADER_FLAG_USE_TIMESTAMP = 0x00000200
            TRACE_HEADER_FLAG_TRACED_GUID = 0x00020000            # denotes a trace
            TRACE_HEADER_FLAG_LOG_WNODE = 0x00040000            # request to log Wnode
            TRACE_HEADER_FLAG_USE_GUID_PTR = 0x00080000            # Guid is actually a pointer
            TRACE_HEADER_FLAG_USE_MOF_PTR = 0x00100000            # MOF data are dereferenced


            class ETW_COMPRESSION_RESUMPTION_MODE(ENUM):
                EtwCompressionModeRestart = 0
                EtwCompressionModeNoDisable = 1
                EtwCompressionModeNoRestart = 2

            EtwCompressionModeRestart = ETW_COMPRESSION_RESUMPTION_MODE.EtwCompressionModeRestart
            EtwCompressionModeNoDisable = ETW_COMPRESSION_RESUMPTION_MODE.EtwCompressionModeNoDisable
            EtwCompressionModeNoRestart = ETW_COMPRESSION_RESUMPTION_MODE.EtwCompressionModeNoRestart
            if _MSC_VER >= 1200:
                pass
            # END IF
            # Trace header for all legacy events.
            class DUMMYUNIONNAME(ctypes.Union):
                pass


            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                # Header type - internal use only
                ('HeaderType', UCHAR),
                # Marker - internal use only
                ('MarkerFlags', UCHAR),
            ]
            DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            DUMMYUNIONNAME._fields_ = [
                # Indicates valid fields
                ('FieldTypeFlags', USHORT),
                ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
            ]
            _EVENT_TRACE_HEADER.DUMMYUNIONNAME = DUMMYUNIONNAME


            class DUMMYUNIONNAME2(ctypes.Union):
                pass


            class Class(ctypes.Structure):
                pass


            Class._fields_ = [
                # event type
                ('Type', UCHAR),
                # trace instrumentation level
                ('Level', UCHAR),
                # version of trace record
                ('Version', USHORT),
            ]
            DUMMYUNIONNAME2.Class = Class


            DUMMYUNIONNAME2._fields_ = [
                ('Version', ULONG),
                ('Class', DUMMYUNIONNAME2.Class),
            ]
            _EVENT_TRACE_HEADER.DUMMYUNIONNAME2 = DUMMYUNIONNAME2


            class DUMMYUNIONNAME3(ctypes.Union):
                pass


            DUMMYUNIONNAME3._fields_ = [
                # Guid that identifies event
                ('Guid', GUID),
                # use with WNODE_FLAG_USE_GUID_PTR
                ('GuidPtr', ULONGLONG),
            ]
            _EVENT_TRACE_HEADER.DUMMYUNIONNAME3 = DUMMYUNIONNAME3


            class DUMMYUNIONNAME4(ctypes.Union):
                pass


            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                # Kernel Mode CPU ticks
                ('KernelTime', ULONG),
                # User mode CPU ticks
                ('UserTime', ULONG),
            ]
            DUMMYUNIONNAME4.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            class DUMMYSTRUCTNAME2(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME2._fields_ = [
                # Reserved
                ('ClientContext', ULONG),
                # Event Flags
                ('Flags', ULONG),
            ]
            DUMMYUNIONNAME4.DUMMYSTRUCTNAME2 = DUMMYSTRUCTNAME2


            DUMMYUNIONNAME4._fields_ = [
                ('DUMMYSTRUCTNAME', DUMMYUNIONNAME4.DUMMYSTRUCTNAME),
                # Processor Clock
                ('ProcessorTime', ULONG64),
                ('DUMMYSTRUCTNAME2', DUMMYUNIONNAME4.DUMMYSTRUCTNAME2),
            ]
            _EVENT_TRACE_HEADER.DUMMYUNIONNAME4 = DUMMYUNIONNAME4


            _EVENT_TRACE_HEADER._fields_ = [
                # overlays WNODE_HEADER USHORT Size; // Size of entire record
                ('DUMMYUNIONNAME', _EVENT_TRACE_HEADER.DUMMYUNIONNAME),
                ('DUMMYUNIONNAME2', _EVENT_TRACE_HEADER.DUMMYUNIONNAME2),
                # Thread Id
                ('ThreadId', ULONG),
                # Process Id
                ('ProcessId', ULONG),
                # time when event happens
                ('TimeStamp', LARGE_INTEGER),
                ('DUMMYUNIONNAME3', _EVENT_TRACE_HEADER.DUMMYUNIONNAME3),
                ('DUMMYUNIONNAME4', _EVENT_TRACE_HEADER.DUMMYUNIONNAME4),
            ]


            # This header is used to trace and track transaction co - relations
            class DUMMYUNIONNAME(ctypes.Union):
                pass


            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                # Header type - internal use only
                ('HeaderType', UCHAR),
                # Marker - internal use only
                ('MarkerFlags', UCHAR),
            ]
            DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            DUMMYUNIONNAME._fields_ = [
                # Indicates valid fields
                ('FieldTypeFlags', USHORT),
                ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
            ]
            _EVENT_INSTANCE_HEADER.DUMMYUNIONNAME = DUMMYUNIONNAME


            class DUMMYUNIONNAME2(ctypes.Union):
                pass


            class Class(ctypes.Structure):
                pass


            Class._fields_ = [
                ('Type', UCHAR),
                ('Level', UCHAR),
                ('Version', USHORT),
            ]
            DUMMYUNIONNAME2.Class = Class


            DUMMYUNIONNAME2._fields_ = [
                ('Version', ULONG),
                ('Class', DUMMYUNIONNAME2.Class),
            ]
            _EVENT_INSTANCE_HEADER.DUMMYUNIONNAME2 = DUMMYUNIONNAME2


            class DUMMYUNIONNAME3(ctypes.Union):
                pass


            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                # Kernel Mode CPU ticks
                ('KernelTime', ULONG),
                # User mode CPU ticks
                ('UserTime', ULONG),
            ]
            DUMMYUNIONNAME3.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            class DUMMYSTRUCTNAME2(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME2._fields_ = [
                # Event ID
                ('EventId', ULONG),
                # Trace header Flags
                ('Flags', ULONG),
            ]
            DUMMYUNIONNAME3.DUMMYSTRUCTNAME2 = DUMMYSTRUCTNAME2


            DUMMYUNIONNAME3._fields_ = [
                ('DUMMYSTRUCTNAME', DUMMYUNIONNAME3.DUMMYSTRUCTNAME),
                # Processor Clock
                ('ProcessorTime', ULONG64),
                ('DUMMYSTRUCTNAME2', DUMMYUNIONNAME3.DUMMYSTRUCTNAME2),
            ]
            _EVENT_INSTANCE_HEADER.DUMMYUNIONNAME3 = DUMMYUNIONNAME3


            _EVENT_INSTANCE_HEADER._fields_ = [
                ('Size', USHORT),
                ('DUMMYUNIONNAME', _EVENT_INSTANCE_HEADER.DUMMYUNIONNAME),
                ('DUMMYUNIONNAME2', _EVENT_INSTANCE_HEADER.DUMMYUNIONNAME2),
                ('ThreadId', ULONG),
                ('ProcessId', ULONG),
                ('TimeStamp', LARGE_INTEGER),
                ('RegHandle', ULONGLONG),
                ('InstanceId', ULONG),
                ('ParentInstanceId', ULONG),
                ('DUMMYUNIONNAME3', _EVENT_INSTANCE_HEADER.DUMMYUNIONNAME3),
                ('ParentRegHandle', ULONGLONG),
            ]
            if _MSC_VER >= 1200:
                pass
            # END IF
            # Following are structures and macros for use with USE_MOF_PTR
            # Trace data types
            ETW_NULL_TYPE_VALUE = 0
            ETW_OBJECT_TYPE_VALUE = 1
            ETW_STRING_TYPE_VALUE = 2
            ETW_SBYTE_TYPE_VALUE = 3
            ETW_BYTE_TYPE_VALUE = 4
            ETW_INT16_TYPE_VALUE = 5
            ETW_UINT16_TYPE_VALUE = 6
            ETW_INT32_TYPE_VALUE = 7
            ETW_UINT32_TYPE_VALUE = 8
            ETW_INT64_TYPE_VALUE = 9
            ETW_UINT64_TYPE_VALUE = 10
            ETW_CHAR_TYPE_VALUE = 11
            ETW_SINGLE_TYPE_VALUE = 12
            ETW_DOUBLE_TYPE_VALUE = 13
            ETW_BOOLEAN_TYPE_VALUE = 14
            ETW_DECIMAL_TYPE_VALUE = 15

            # Extended types
            ETW_GUID_TYPE_VALUE = 101
            ETW_ASCIICHAR_TYPE_VALUE = 102
            ETW_ASCIISTRING_TYPE_VALUE = 103
            ETW_COUNTED_STRING_TYPE_VALUE = 104
            ETW_POINTER_TYPE_VALUE = 105
            ETW_SIZET_TYPE_VALUE = 106
            ETW_HIDDEN_TYPE_VALUE = 107
            ETW_BOOL_TYPE_VALUE = 108
            ETW_COUNTED_ANSISTRING_TYPE_VALUE = 109
            ETW_REVERSED_COUNTED_STRING_TYPE_VALUE = 110
            ETW_REVERSED_COUNTED_ANSISTRING_TYPE_VALUE = 111
            ETW_NON_NULL_TERMINATED_STRING_TYPE_VALUE = 112
            ETW_REDUCED_ANSISTRING_TYPE_VALUE = 113
            ETW_REDUCED_STRING_TYPE_VALUE = 114
            ETW_SID_TYPE_VALUE = 115
            ETW_VARIANT_TYPE_VALUE = 116
            ETW_PTVECTOR_TYPE_VALUE = 117
            ETW_WMITIME_TYPE_VALUE = 118
            ETW_DATETIME_TYPE_VALUE = 119
            ETW_REFRENCE_TYPE_VALUE = 120
            

            def DEFINE_TRACE_MOF_FIELD(MOF, ptr, length, type):
                return MOF - >DataPtr = ULONG64ULONG_PTR ptr; MOF - >Length = ULONG length; MOF - >DataType = ULONG type;


            _MOF_FIELD._fields_ = [
                # Pointer to the field. Up to 64 - bits only
                ('DataPtr', ULONG64),
                # Length of the MOF field
                ('Length', ULONG),
                # Type of data
                ('DataType', ULONG),
            ]
                if _MSC_VER >= 1200:
                    pass
                # END IF
            if not defined(_EVNTRACE_KERNEL_MODE) or defined(_WMIKM_):
                # This is the header for every logfile. The memory for
                # LoggerName
                # and LogFileName must be contiguous adjacent to this structure
                # Allows both user - mode and kernel - mode to understand the
                # header.
                # TRACE_LOGFILE_HEADER32 and TRACE_LOGFILE_HEADER64 structures
                # are also provided to simplify cross platform decoding of the
                # header event.
                class DUMMYUNIONNAME(ctypes.Union):
                    pass


                class VersionDetail(ctypes.Structure):
                    pass


                VersionDetail._fields_ = [
                    ('MajorVersion', UCHAR),
                    ('MinorVersion', UCHAR),
                    ('SubVersion', UCHAR),
                    ('SubMinorVersion', UCHAR),
                ]
                DUMMYUNIONNAME.VersionDetail = VersionDetail


                DUMMYUNIONNAME._fields_ = [
                    # Logger version
                    ('Version', ULONG),
                    ('VersionDetail', DUMMYUNIONNAME.VersionDetail),
                ]
                _TRACE_LOGFILE_HEADER.DUMMYUNIONNAME = DUMMYUNIONNAME


                class DUMMYUNIONNAME2(ctypes.Union):
                    pass


                class DUMMYSTRUCTNAME(ctypes.Structure):
                    pass


                DUMMYSTRUCTNAME._fields_ = [
                    # Count of buffers written at start.
                    ('StartBuffers', ULONG),
                    # Size of pointer type in bits
                    ('PointerSize', ULONG),
                    # Events lost during log session
                    ('EventsLost', ULONG),
                    # Cpu Speed in MHz
                    ('CpuSpeedInMHz', ULONG),
                ]
                DUMMYUNIONNAME2.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


                DUMMYUNIONNAME2._fields_ = [
                    # For RealTime Buffer Delivery
                    ('LogInstanceGuid', GUID),
                    ('DUMMYSTRUCTNAME', DUMMYUNIONNAME2.DUMMYSTRUCTNAME),
                ]
                _TRACE_LOGFILE_HEADER.DUMMYUNIONNAME2 = DUMMYUNIONNAME2


                _TEMP__TRACE_LOGFILE_HEADER = [
                    # Logger buffer size in Kbytes
                    ('BufferSize', ULONG),
                    ('DUMMYUNIONNAME', _TRACE_LOGFILE_HEADER.DUMMYUNIONNAME),
                    # defaults to NT version
                    ('ProviderVersion', ULONG),
                    # Number of Processors
                    ('NumberOfProcessors', ULONG),
                    # Time when logger stops
                    ('EndTime', LARGE_INTEGER),
                    # assumes timer is constantnot not not
                    ('TimerResolution', ULONG),
                    # Maximum in Mbytes
                    ('MaximumFileSize', ULONG),
                    # specify logfile mode
                    ('LogFileMode', ULONG),
                    # used to file start of Circular File
                    ('BuffersWritten', ULONG),
                    ('DUMMYUNIONNAME2', _TRACE_LOGFILE_HEADER.DUMMYUNIONNAME2),
                ]
                if defined(_WMIKM_):
                        _TEMP__TRACE_LOGFILE_HEADER += [
                        ('LoggerName', PWCHAR),
                        ('LogFileName', PWCHAR),
                        ('TimeZone', RTL_TIME_ZONE_INFORMATION),
                        ]
                        else:
                            _TEMP__TRACE_LOGFILE_HEADER += [
                        ('LoggerName', LPWSTR),
                        ('LogFileName', LPWSTR),
                        ('TimeZone', TIME_ZONE_INFORMATION),
                            ]
                        # END IF
                            _TEMP__TRACE_LOGFILE_HEADER += [
                    ('BootTime', LARGE_INTEGER),
                    # Reserved
                    ('PerfFreq', LARGE_INTEGER),
                    # Reserved
                    ('StartTime', LARGE_INTEGER),
                    # ClockType
                    ('ReservedFlags', ULONG),
                    ('BuffersLost', ULONG),
                            ]
                            _TRACE_LOGFILE_HEADER._fields_ = _TEMP__TRACE_LOGFILE_HEADER


                class _Union_1(ctypes.Union):
                    pass


                class VersionDetail(ctypes.Structure):
                    pass


                VersionDetail._fields_ = [
                    ('MajorVersion', UCHAR),
                    ('MinorVersion', UCHAR),
                    ('SubVersion', UCHAR),
                    ('SubMinorVersion', UCHAR),
                ]
                _Union_1.VersionDetail = VersionDetail


                _Union_1._fields_ = [
                    # Logger version
                    ('Version', ULONG),
                    ('VersionDetail', _Union_1.VersionDetail),
                ]
                _TRACE_LOGFILE_HEADER32._Union_1 = _Union_1


                class _Union_2(ctypes.Union):
                    pass


                class _Struct_1(ctypes.Structure):
                    pass


                _Struct_1._fields_ = [
                    # Count of buffers written at start.
                    ('StartBuffers', ULONG),
                    # Size of pointer type in bits
                    ('PointerSize', ULONG),
                    # Events lost during log session
                    ('EventsLost', ULONG),
                    # Cpu Speed in MHz
                    ('CpuSpeedInMHz', ULONG),
                ]
                _Union_2._Struct_1 = _Struct_1

                _Union_2._anonymous_ = (
                    '_Struct_1',
                )

                _Union_2._fields_ = [
                    # For RealTime Buffer Delivery
                    ('LogInstanceGuid', GUID),
                    ('_Struct_1', _Union_2._Struct_1),
                ]
                _TRACE_LOGFILE_HEADER32._Union_2 = _Union_2

                _TRACE_LOGFILE_HEADER32._anonymous_ = (
                    '_Union_1',
                    '_Union_2',
                )

                _TEMP__TRACE_LOGFILE_HEADER32 = [
                    # Logger buffer size in Kbytes
                    ('BufferSize', ULONG),
                    ('_Union_1', _TRACE_LOGFILE_HEADER32._Union_1),
                    # defaults to NT version
                    ('ProviderVersion', ULONG),
                    # Number of Processors
                    ('NumberOfProcessors', ULONG),
                    # Time when logger stops
                    ('EndTime', LARGE_INTEGER),
                    # assumes timer is constantnot not not
                    ('TimerResolution', ULONG),
                    # Maximum in Mbytes
                    ('MaximumFileSize', ULONG),
                    # specify logfile mode
                    ('LogFileMode', ULONG),
                    # used to file start of Circular File
                    ('BuffersWritten', ULONG),
                    ('_Union_2', _TRACE_LOGFILE_HEADER32._Union_2),
                ]
                if defined(_WMIKM_):
                        _TEMP__TRACE_LOGFILE_HEADER32 += [
                        ('LoggerName', ULONG32),
                        ('LogFileName', ULONG32),
                        ('TimeZone', RTL_TIME_ZONE_INFORMATION),
                        ]
                        else:
                            _TEMP__TRACE_LOGFILE_HEADER32 += [
                        ('LoggerName', ULONG32),
                        ('LogFileName', ULONG32),
                        ('TimeZone', TIME_ZONE_INFORMATION),
                            ]
                        # END IF
                            _TEMP__TRACE_LOGFILE_HEADER32 += [
                    ('BootTime', LARGE_INTEGER),
                    # Reserved
                    ('PerfFreq', LARGE_INTEGER),
                    # Reserved
                    ('StartTime', LARGE_INTEGER),
                    # ClockType
                    ('ReservedFlags', ULONG),
                    ('BuffersLost', ULONG),
                            ]
                            _TRACE_LOGFILE_HEADER32._fields_ = _TEMP__TRACE_LOGFILE_HEADER32


                class _Union_3(ctypes.Union):
                    pass


                class VersionDetail(ctypes.Structure):
                    pass


                VersionDetail._fields_ = [
                    ('MajorVersion', UCHAR),
                    ('MinorVersion', UCHAR),
                    ('SubVersion', UCHAR),
                    ('SubMinorVersion', UCHAR),
                ]
                _Union_3.VersionDetail = VersionDetail


                _Union_3._fields_ = [
                    # Logger version
                    ('Version', ULONG),
                    ('VersionDetail', _Union_3.VersionDetail),
                ]
                _TRACE_LOGFILE_HEADER64._Union_3 = _Union_3


                class _Union_4(ctypes.Union):
                    pass


                class _Struct_1(ctypes.Structure):
                    pass


                _Struct_1._fields_ = [
                    # Count of buffers written at start.
                    ('StartBuffers', ULONG),
                    # Size of pointer type in bits
                    ('PointerSize', ULONG),
                    # Events lost during log session
                    ('EventsLost', ULONG),
                    # Cpu Speed in MHz
                    ('CpuSpeedInMHz', ULONG),
                ]
                _Union_4._Struct_1 = _Struct_1

                _Union_4._anonymous_ = (
                    '_Struct_1',
                )

                _Union_4._fields_ = [
                    # For RealTime Buffer Delivery
                    ('LogInstanceGuid', GUID),
                    ('_Struct_1', _Union_4._Struct_1),
                ]
                _TRACE_LOGFILE_HEADER64._Union_4 = _Union_4

                _TRACE_LOGFILE_HEADER64._anonymous_ = (
                    '_Union_3',
                    '_Union_4',
                )

                _TEMP__TRACE_LOGFILE_HEADER64 = [
                    # Logger buffer size in Kbytes
                    ('BufferSize', ULONG),
                    ('_Union_3', _TRACE_LOGFILE_HEADER64._Union_3),
                    # defaults to NT version
                    ('ProviderVersion', ULONG),
                    # Number of Processors
                    ('NumberOfProcessors', ULONG),
                    # Time when logger stops
                    ('EndTime', LARGE_INTEGER),
                    # assumes timer is constantnot not not
                    ('TimerResolution', ULONG),
                    # Maximum in Mbytes
                    ('MaximumFileSize', ULONG),
                    # specify logfile mode
                    ('LogFileMode', ULONG),
                    # used to file start of Circular File
                    ('BuffersWritten', ULONG),
                    ('_Union_4', _TRACE_LOGFILE_HEADER64._Union_4),
                ]
                if defined(_WMIKM_):
                        _TEMP__TRACE_LOGFILE_HEADER64 += [
                        ('LoggerName', ULONG64),
                        ('LogFileName', ULONG64),
                        ('TimeZone', RTL_TIME_ZONE_INFORMATION),
                        ]
                        else:
                            _TEMP__TRACE_LOGFILE_HEADER64 += [
                        ('LoggerName', ULONG64),
                        ('LogFileName', ULONG64),
                        ('TimeZone', TIME_ZONE_INFORMATION),
                            ]
                        # END IF
                            _TEMP__TRACE_LOGFILE_HEADER64 += [
                    ('BootTime', LARGE_INTEGER),
                    # Reserved
                    ('PerfFreq', LARGE_INTEGER),
                    # Reserved
                    ('StartTime', LARGE_INTEGER),
                    # ClockType
                    ('ReservedFlags', ULONG),
                    ('BuffersLost', ULONG),
                            ]
                            _TRACE_LOGFILE_HEADER64._fields_ = _TEMP__TRACE_LOGFILE_HEADER64
                if _MSC_VER >= 1200:
                    pass
                # END IF
            # END IF   not _EVNTRACE_KERNEL_MODE or _WMIKM_
            # Instance Information to track parent child relationship of
            # Instances.
            EVENT_INSTANCE_INFO._fields_ = [
                ('RegHandle', HANDLE),
                ('InstanceId', ULONG),
            ]
            if not defined(_EVNTRACE_KERNEL_MODE):
                # Structures that have UNICODE and ANSI versions are defined
                # here
                # Logger configuration and running statistics. This structure
                # is used
                # by user - mode callers, such as PDH library
                if _MSC_VER >= 1200:
                    pass
                # END IF
                PEVENT_FILTER_DESCRIPTOR = POINTER(_EVENT_FILTER_DESCRIPTOR EVENT_FILTER_DESCRIPTOR,)


                class DUMMYUNIONNAME(ctypes.Union):
                    pass


                DUMMYUNIONNAME._fields_ = [
                    # unused
                    ('AgeLimit', LONG),
                    # Number of buffers to fill before flushing
                    ('FlushThreshold', LONG),
                ]
                _EVENT_TRACE_PROPERTIES.DUMMYUNIONNAME = DUMMYUNIONNAME


                _EVENT_TRACE_PROPERTIES._fields_ = [
                    ('Wnode', WNODE_HEADER),
                    # buffer size for logging (kbytes)
                    ('BufferSize', ULONG),
                    # minimum to preallocate
                    ('MinimumBuffers', ULONG),
                    # maximum buffers allowed
                    ('MaximumBuffers', ULONG),
                    # maximum logfile size (in MBytes)
                    ('MaximumFileSize', ULONG),
                    # sequential, circular
                    ('LogFileMode', ULONG),
                    # buffer flush timer, in seconds
                    ('FlushTimer', ULONG),
                    # trace enable flags
                    ('EnableFlags', ULONG),
                    ('DUMMYUNIONNAME', _EVENT_TRACE_PROPERTIES.DUMMYUNIONNAME),
                    # no of buffers in use
                    ('NumberOfBuffers', ULONG),
                    # no of buffers free
                    ('FreeBuffers', ULONG),
                    # event records lost
                    ('EventsLost', ULONG),
                    # no of buffers written to file
                    ('BuffersWritten', ULONG),
                    # no of logfile write failures
                    ('LogBuffersLost', ULONG),
                    # no of rt delivery failures
                    ('RealTimeBuffersLost', ULONG),
                    # thread id of Logger
                    ('LoggerThreadId', HANDLE),
                    # Offset to LogFileName
                    ('LogFileNameOffset', ULONG),
                    # Offset to LoggerName
                    ('LoggerNameOffset', ULONG),
                ]


                class DUMMYUNIONNAME(ctypes.Union):
                    pass


                DUMMYUNIONNAME._fields_ = [
                    # unused
                    ('AgeLimit', LONG),
                    # Number of buffers to fill before flushing
                    ('FlushThreshold', LONG),
                ]
                _EVENT_TRACE_PROPERTIES_V2.DUMMYUNIONNAME = DUMMYUNIONNAME


                class DUMMYUNIONNAME2(ctypes.Union):
                    pass


                class DUMMYSTRUCTNAME(ctypes.Structure):
                    pass


                DUMMYSTRUCTNAME._fields_ = [
                    # Should be set to 2 for this version.
                    ('VersionNumber', ULONG, 8),
                ]
                DUMMYUNIONNAME2.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


                DUMMYUNIONNAME2._fields_ = [
                    ('DUMMYSTRUCTNAME', DUMMYUNIONNAME2.DUMMYSTRUCTNAME),
                    ('V2Control', ULONG),
                ]
                _EVENT_TRACE_PROPERTIES_V2.DUMMYUNIONNAME2 = DUMMYUNIONNAME2


                class DUMMYUNIONNAME3(ctypes.Union):
                    pass


                class DUMMYSTRUCTNAME(ctypes.Structure):
                    pass


                DUMMYSTRUCTNAME._fields_ = [
                    # Logger was started by a WOW64 process (output only).
                    ('Wow', ULONG, 1),
                ]
                DUMMYUNIONNAME3.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


                DUMMYUNIONNAME3._fields_ = [
                    ('DUMMYSTRUCTNAME', DUMMYUNIONNAME3.DUMMYSTRUCTNAME),
                    ('V2Options', ULONG64),
                ]
                _EVENT_TRACE_PROPERTIES_V2.DUMMYUNIONNAME3 = DUMMYUNIONNAME3


                _EVENT_TRACE_PROPERTIES_V2._fields_ = [
                    # Always have WNODE_FLAG_VERSIONED_PROPERTIES.
                    ('Wnode', WNODE_HEADER),
                    # buffer size for logging (kbytes)
                    ('BufferSize', ULONG),
                    # minimum to preallocate
                    ('MinimumBuffers', ULONG),
                    # maximum buffers allowed
                    ('MaximumBuffers', ULONG),
                    # maximum logfile size (in MBytes)
                    ('MaximumFileSize', ULONG),
                    # sequential, circular
                    ('LogFileMode', ULONG),
                    # buffer flush timer, in seconds
                    ('FlushTimer', ULONG),
                    # trace enable flags
                    ('EnableFlags', ULONG),
                    ('DUMMYUNIONNAME', _EVENT_TRACE_PROPERTIES_V2.DUMMYUNIONNAME),
                    # no of buffers in use
                    ('NumberOfBuffers', ULONG),
                    # no of buffers free
                    ('FreeBuffers', ULONG),
                    # event records lost
                    ('EventsLost', ULONG),
                    # no of buffers written to file
                    ('BuffersWritten', ULONG),
                    # no of logfile write failures
                    ('LogBuffersLost', ULONG),
                    # no of rt delivery failures
                    ('RealTimeBuffersLost', ULONG),
                    # thread id of Logger
                    ('LoggerThreadId', HANDLE),
                    # Offset to LogFileName
                    ('LogFileNameOffset', ULONG),
                    # Offset to LoggerName
                    ('LoggerNameOffset', ULONG),
                    # V2 data
                    ('DUMMYUNIONNAME2', _EVENT_TRACE_PROPERTIES_V2.DUMMYUNIONNAME2),
                    # Number of filters
                    ('FilterDescCount', ULONG),
                    # Only applicable for Private Loggers
                    ('FilterDesc', PEVENT_FILTER_DESCRIPTOR),
                    ('DUMMYUNIONNAME3', _EVENT_TRACE_PROPERTIES_V2.DUMMYUNIONNAME3),
                ]
                if _MSC_VER >= 1200:
                    pass
                # END IF
                # Data Provider structures
                # Used by RegisterTraceGuids()
                _TRACE_GUID_REGISTRATION._fields_ = [
                    # Guid of data block being registered or updated.
                    ('Guid', LPCGUID),
                    # Guid Registration Handle is returned.
                    ('RegHandle', HANDLE),
                ]


                # Data consumer structures            # END IF   not _EVNTRACE_KERNEL_MODE
            _TRACE_GUID_PROPERTIES._fields_ = [
                ('Guid', GUID),
                ('GuidType', ULONG),
                ('LoggerId', ULONG),
                ('EnableLevel', ULONG),
                ('EnableFlags', ULONG),
                ('IsEnable', BOOLEAN),
            ]
            if _MSC_VER >= 1200:
                pass
            # END IF
            if not defined(ETW_BUFFER_CONTEXT_DEF):
                #~#~#~                #define ETW_BUFFER_CONTEXT_DEF
                class DUMMYUNIONNAME(ctypes.Union):
                    pass


                class DUMMYSTRUCTNAME(ctypes.Structure):
                    pass


                DUMMYSTRUCTNAME._fields_ = [
                    ('ProcessorNumber', UCHAR),
                    ('Alignment', UCHAR),
                ]
                DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


                DUMMYUNIONNAME._fields_ = [
                    ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
                    ('ProcessorIndex', USHORT),
                ]
                _ETW_BUFFER_CONTEXT.DUMMYUNIONNAME = DUMMYUNIONNAME


                _ETW_BUFFER_CONTEXT._fields_ = [
                    ('DUMMYUNIONNAME', _ETW_BUFFER_CONTEXT.DUMMYUNIONNAME),
                    ('LoggerId', USHORT),
                ]
            # END IF
            if _MSC_VER >= 1200:
                pass
            # END IF
            # Provider Information Flags used on Vista and above.
            TRACE_PROVIDER_FLAG_LEGACY = 0x00000001
            TRACE_PROVIDER_FLAG_PRE_ENABLE = 0x00000002


            # Enable Information for Provider Instance
            # Used on Vista and above
            _TRACE_ENABLE_INFO._fields_ = [
                ('IsEnabled', ULONG),
                ('Level', UCHAR),
                ('Reserved1', UCHAR),
                ('LoggerId', USHORT),
                ('EnableProperty', ULONG),
                ('Reserved2', ULONG),
                ('MatchAnyKeyword', ULONGLONG),
                ('MatchAllKeyword', ULONGLONG),
            ]


            # Instance Information for Provider
            # Used on Vista and above
            _TRACE_PROVIDER_INSTANCE_INFO._fields_ = [
                ('NextOffset', ULONG),
                ('EnableCount', ULONG),
                ('Pid', ULONG),
                ('Flags', ULONG),
            ]


            # GUID Information Used on Vista and above
            _TRACE_GUID_INFO._fields_ = [
                ('InstanceCount', ULONG),
                ('Reserved', ULONG),
            ]

            _PROFILE_SOURCE_INFO._fields_ = [
                ('NextEntryOffset', ULONG),
                ('Source', ULONG),
                ('MinInterval', ULONG),
                ('MaxInterval', ULONG),
                ('Reserved', ULONG64),
                ('Description', WCHAR * ANYSIZE_ARRAY),
            ]


            # An EVENT_TRACE consists of a fixed header (EVENT_TRACE_HEADER)
            # and
            # optionally a variable portion pointed to by MofData. The
            # datablock
            # layout of the variable portion is unknown to the Logger and must
            # be obtained from WBEM CIMOM database.
            if _MSC_VER >= 1200:
                pass
            # END IF
            class DUMMYUNIONNAME(ctypes.Union):
                pass


            DUMMYUNIONNAME._fields_ = [
                ('ClientContext', ULONG),
                ('BufferContext', ETW_BUFFER_CONTEXT),
            ]
            _EVENT_TRACE.DUMMYUNIONNAME = DUMMYUNIONNAME


            _EVENT_TRACE._fields_ = [
                # Event trace header
                ('Header', EVENT_TRACE_HEADER),
                # Instance Id of this event
                ('InstanceId', ULONG),
                # Parent Instance Id.
                ('ParentInstanceId', ULONG),
                # Parent Guid;
                ('ParentGuid', GUID),
                # Pointer to Variable Data
                ('MofData', PVOID),
                # Variable Datablock Length
                ('MofLength', ULONG),
                ('DUMMYUNIONNAME', _EVENT_TRACE.DUMMYUNIONNAME),
            ]
            if _MSC_VER >= 1200:
                pass
            # END IF
            EVENT_CONTROL_CODE_DISABLE_PROVIDER = 0
            EVENT_CONTROL_CODE_ENABLE_PROVIDER = 1
            EVENT_CONTROL_CODE_CAPTURE_STATE = 2
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        if not defined(_EVNTRACE_KERNEL_MODE):
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                PEVENT_RECORD = POINTER(_EVENT_RECORD EVENT_RECORD,)
                PEVENT_TRACE_LOGFILEW = POINTER(_EVENT_TRACE_LOGFILEW EVENT_TRACE_LOGFILEW,)
                PEVENT_TRACE_LOGFILEA = POINTER(_EVENT_TRACE_LOGFILEA EVENT_TRACE_LOGFILEA,)

# typedef ULONG (WINAPI * PEVENT_TRACE_BUFFER_CALLBACKW)
# (PEVENT_TRACE_LOGFILEW Logfile);
                PEVENT_TRACE_BUFFER_CALLBACKW = WINAPI(
                    ULONG,                    (PEVENT_TRACE_LOGFILEW,                )
# typedef ULONG (WINAPI * PEVENT_TRACE_BUFFER_CALLBACKA)
# (PEVENT_TRACE_LOGFILEA Logfile);
                PEVENT_TRACE_BUFFER_CALLBACKA = WINAPI(
                    ULONG,                    (PEVENT_TRACE_LOGFILEA,                )
# typedef VOID (WINAPI *PEVENT_CALLBACK)( PEVENT_TRACE pEvent );
                PEVENT_CALLBACK = WINAPI(
                    VOID,                )
# typedef VOID (WINAPI *PEVENT_RECORD_CALLBACK) (PEVENT_RECORD EventRecord);
                PEVENT_RECORD_CALLBACK = WINAPI(
                    VOID,                )
                # Prototype for service request callback. Data providers
                # register with WMI
                # by passing a service request callback function that is
                # called for all
                # wmi requests.
# typedef ULONG (
# #ifndef MIDL_PASS
# WINAPI
# #endif
# *WMIDPREQUEST)(
# _In_ WMIDPREQUESTCODE RequestCode,
# _In_ PVOID RequestContext,
# _Inout_ ULONG *BufferSize,
# _Inout_ PVOID Buffer
# );
                [] = CALLBACK(
                    *WMIDPREQUEST),                    #ifndef,                    WMIDPREQUESTCODE,                    PVOID,                    POINTER(ULONG),                    PVOID,                )
                if _MSC_VER >= 1200:
                    pass
                # END IF
                class DUMMYUNIONNAME(ctypes.Union):
                    pass


                DUMMYUNIONNAME._fields_ = [
                    # Mode of the logfile
                    ('LogFileMode', ULONG),
                    # Processing flags used on Vista and above
                    ('ProcessTraceMode', ULONG),
                ]
                _EVENT_TRACE_LOGFILEW.DUMMYUNIONNAME = DUMMYUNIONNAME


                class DUMMYUNIONNAME2(ctypes.Union):
                    pass


                DUMMYUNIONNAME2._fields_ = [
                    # Callback with EVENT_TRACE
                    ('EventCallback', PEVENT_CALLBACK),
                    # Callback with EVENT_RECORD on Vista and above
                    ('EventRecordCallback', PEVENT_RECORD_CALLBACK),
                ]
                _EVENT_TRACE_LOGFILEW.DUMMYUNIONNAME2 = DUMMYUNIONNAME2


                _EVENT_TRACE_LOGFILEW._fields_ = [
                    # Logfile Name
                    ('LogFileName', LPWSTR),
                    # LoggerName
                    ('LoggerName', LPWSTR),
                    # timestamp of last event
                    ('CurrentTime', LONGLONG),
                    # buffers read to date
                    ('BuffersRead', ULONG),
                    ('DUMMYUNIONNAME', _EVENT_TRACE_LOGFILEW.DUMMYUNIONNAME),
                    # Current Event from this stream.
                    ('CurrentEvent', EVENT_TRACE),
                    # logfile header structure
                    ('LogfileHeader', TRACE_LOGFILE_HEADER),
                    # is read
                    ('BufferCallback', PEVENT_TRACE_BUFFER_CALLBACKW),
                    # following variables are filled for BufferCallback.
                    ('BufferSize', ULONG),
                    ('Filled', ULONG),
                    ('EventsLost', ULONG),
                    # following needs to be propagated to each buffer
                    ('DUMMYUNIONNAME2', _EVENT_TRACE_LOGFILEW.DUMMYUNIONNAME2),
                    # TRUE for kernel logfile
                    ('IsKernelTrace', ULONG),
                    # reserved for internal use
                    ('Context', PVOID),
                ]


                class DUMMYUNIONNAME(ctypes.Union):
                    pass


                DUMMYUNIONNAME._fields_ = [
                    # Mode of the logfile
                    ('LogFileMode', ULONG),
                    # Processing flags
                    ('ProcessTraceMode', ULONG),
                ]
                _EVENT_TRACE_LOGFILEA.DUMMYUNIONNAME = DUMMYUNIONNAME


                class DUMMYUNIONNAME2(ctypes.Union):
                    pass


                DUMMYUNIONNAME2._fields_ = [
                    # callback for every event
                    ('EventCallback', PEVENT_CALLBACK),
                    ('EventRecordCallback', PEVENT_RECORD_CALLBACK),
                ]
                _EVENT_TRACE_LOGFILEA.DUMMYUNIONNAME2 = DUMMYUNIONNAME2


                _EVENT_TRACE_LOGFILEA._fields_ = [
                    # Logfile Name
                    ('LogFileName', LPSTR),
                    # LoggerName
                    ('LoggerName', LPSTR),
                    # timestamp of last event
                    ('CurrentTime', LONGLONG),
                    # buffers read to date
                    ('BuffersRead', ULONG),
                    ('DUMMYUNIONNAME', _EVENT_TRACE_LOGFILEA.DUMMYUNIONNAME),
                    # Current Event from this stream
                    ('CurrentEvent', EVENT_TRACE),
                    # logfile header structure
                    ('LogfileHeader', TRACE_LOGFILE_HEADER),
                    # is read
                    ('BufferCallback', PEVENT_TRACE_BUFFER_CALLBACKA),
                    # following variables are filled for BufferCallback.
                    ('BufferSize', ULONG),
                    ('Filled', ULONG),
                    ('EventsLost', ULONG),
                    # following needs to be propagated to each buffer
                    ('DUMMYUNIONNAME2', _EVENT_TRACE_LOGFILEA.DUMMYUNIONNAME2),
                    # TRUE for kernel logfile
                    ('IsKernelTrace', ULONG),
                    # reserved for internal use
                    ('Context', PVOID),
                ]
                if _MSC_VER >= 1200:
                    pass
                # END IF
                # Define generic structures
                if defined(_UNICODE) or defined(UNICODE):
                    PEVENT_TRACE_BUFFER_CALLBACK = (
                        PEVENT_TRACE_BUFFER_CALLBACKW
                    )
                    EVENT_TRACE_LOGFILE = EVENT_TRACE_LOGFILEW
                    PEVENT_TRACE_LOGFILE = PEVENT_TRACE_LOGFILEW
                    KERNEL_LOGGER_NAME = KERNEL_LOGGER_NAMEW
                    GLOBAL_LOGGER_NAME = GLOBAL_LOGGER_NAMEW
                    EVENT_LOGGER_NAME = EVENT_LOGGER_NAMEW
                else:
                    PEVENT_TRACE_BUFFER_CALLBACK = (
                        PEVENT_TRACE_BUFFER_CALLBACKA
                    )
                    EVENT_TRACE_LOGFILE = EVENT_TRACE_LOGFILEA
                    PEVENT_TRACE_LOGFILE = PEVENT_TRACE_LOGFILEA
                    KERNEL_LOGGER_NAME = KERNEL_LOGGER_NAMEA
                    GLOBAL_LOGGER_NAME = GLOBAL_LOGGER_NAMEA
                    EVENT_LOGGER_NAME = EVENT_LOGGER_NAMEA
                # END IF
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
                advapi32 = ctypes.windll.ADVAPI32

            if defined(__cplusplus):
                # extern "C" {
                # #endif
                # 
                # #ifndef _APISET_EVENTING
                # 
                # #pragma region Application Family or OneCore Family
                # #if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
                # 
                # 
                # // Logger control APIs
                # 
                # 
                # 
                # // Use the routine below to start an event trace session
                # 
                # 
                # // ULONG
                # // StartTrace(
                # // _Out_ PTRACEHANDLE TraceHandle,
                # // _In_ LPTSTR InstanceName,
                # // _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # // );
                # 
                # 
                # EXTERN_C
                # ULONG
                # WMIAPI
                # StartTraceW(
                # _Out_ PTRACEHANDLE TraceHandle,
                # _In_ LPCWSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                StartTraceW = advapi32.StartTraceW
                StartTraceW.restype = ULONG
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
                advapi32 = ctypes.windll.ADVAPI32
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
                # EXTERN_C
                # ULONG
                # WMIAPI
                # StartTraceA(
                # _Out_ PTRACEHANDLE TraceHandle,
                # _In_ LPCSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                StartTraceA = advapi32.StartTraceA
                StartTraceA.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                # Use the routine below to stop an event trace session
                # ULONG
                # StopTrace(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_opt_ LPTSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                advapi32 = ctypes.windll.ADVAPI32


                # EXTERN_C
                # ULONG
                # WMIAPI
                # StopTraceW(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_opt_ LPCWSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                StopTraceW = advapi32.StopTraceW
                StopTraceW.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
                advapi32 = ctypes.windll.ADVAPI32

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
                # EXTERN_C
                # ULONG
                # WMIAPI
                # StopTraceA(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_opt_ LPCSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                StopTraceA = advapi32.StopTraceA
                StopTraceA.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                # Use the routine below to query the properties of an event
                # trace session
                # ULONG
                # QueryTrace(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_opt_ LPTSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                advapi32 = ctypes.windll.ADVAPI32


                # EXTERN_C
                # ULONG
                # WMIAPI
                # QueryTraceW(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_opt_ LPCWSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                QueryTraceW = advapi32.QueryTraceW
                QueryTraceW.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
                advapi32 = ctypes.windll.ADVAPI32

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
                # EXTERN_C
                # ULONG
                # WMIAPI
                # QueryTraceA(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_opt_ LPCSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                QueryTraceA = advapi32.QueryTraceA
                QueryTraceA.restype = ULONG


                # Use the routine below to update certain properties of an
                # event trace session
                # ULONG
                # UpdateTrace(
                # _In_ PTRACEHANDLE TraceHandle,
                # _In_opt_ LPTSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                # EXTERN_C
                # ULONG
                # WMIAPI
                # UpdateTraceW(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_opt_ LPCWSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                UpdateTraceW = advapi32.UpdateTraceW
                UpdateTraceW.restype = ULONG


                # EXTERN_C
                # ULONG
                # WMIAPI
                # UpdateTraceA(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_opt_ LPCSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                UpdateTraceA = advapi32.UpdateTraceA
                UpdateTraceA.restype = ULONG


                # Use the routine below to request that all active buffers an
                # event trace
                # session be "flushed", or written out.            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                # ULONG
                # FlushTrace(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_opt_ LPTSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                # );
                    advapi32 = ctypes.windll.ADVAPI32

                if WINVER >= _WIN32_WINNT_WINXP:
                    # EXTERN_C
                    # ULONG
                    # WMIAPI
                    # FlushTraceW(
                    # _In_ TRACEHANDLE TraceHandle,
                    # _In_opt_ LPCWSTR InstanceName,
                    # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                    # );
                    FlushTraceW = advapi32.FlushTraceW
                    FlushTraceW.restype = ULONG

                # END IF
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
                    advapi32 = ctypes.windll.ADVAPI32

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
                if WINVER >= _WIN32_WINNT_WINXP:
                    # EXTERN_C
                    # ULONG
                    # WMIAPI
                    # FlushTraceA(
                    # _In_ TRACEHANDLE TraceHandle,
                    # _In_opt_ LPCSTR InstanceName,
                    # _Inout_ PEVENT_TRACE_PROPERTIES Properties
                    # );
                    FlushTraceA = advapi32.FlushTraceA
                    FlushTraceA.restype = ULONG

                # END IF
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                # Generic trace control routine
                advapi32 = ctypes.windll.ADVAPI32


                # EXTERN_C
                # ULONG
                # WMIAPI
                # ControlTraceW(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_opt_ LPCWSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties,
                # _In_ ULONG ControlCode
                # );
                ControlTraceW = advapi32.ControlTraceW
                ControlTraceW.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
                advapi32 = ctypes.windll.ADVAPI32

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
                # EXTERN_C
                # ULONG
                # WMIAPI
                # ControlTraceA(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_opt_ LPCSTR InstanceName,
                # _Inout_ PEVENT_TRACE_PROPERTIES Properties,
                # _In_ ULONG ControlCode
                # );
                ControlTraceA = advapi32.ControlTraceA
                ControlTraceA.restype = ULONG


                # ULONG
                # QueryAllTraces(
                # _Out_writes_(PropertyArrayCount) PEVENT_TRACE_PROPERTIES
                # *PropertyArray,
                # _In_ ULONG PropertyArrayCount,
                # _Out_ PULONG LoggerCount
                # );
                # EXTERN_C
                # ULONG
                # WMIAPI
                # QueryAllTracesW(
                # _Out_writes_(PropertyArrayCount) PEVENT_TRACE_PROPERTIES *PropertyArray,
                # _In_  ULONG PropertyArrayCount,
                # _Out_ PULONG LoggerCount
                # );
                QueryAllTracesW = advapi32.QueryAllTracesW
                QueryAllTracesW.restype = ULONG


                # EXTERN_C
                # ULONG
                # WMIAPI
                # QueryAllTracesA(
                # _Out_writes_(PropertyArrayCount) PEVENT_TRACE_PROPERTIES *PropertyArray,
                # _In_  ULONG PropertyArrayCount,
                # _Out_ PULONG LoggerCount
                # );
                QueryAllTracesA = advapi32.QueryAllTracesA
                QueryAllTracesA.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                # Data Provider Enable APIs
                advapi32 = ctypes.windll.ADVAPI32


                # EXTERN_C
                # ULONG
                # WMIAPI
                # EnableTrace(
                # _In_ ULONG Enable,
                # _In_ ULONG EnableFlag,
                # _In_ ULONG EnableLevel,
                # _In_ LPCGUID ControlGuid,
                # _In_ TRACEHANDLE TraceHandle
                # );
                EnableTrace = advapi32.EnableTrace
                EnableTrace.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        # END IF   _APISET_EVENTING
                    advapi32 = ctypes.windll.ADVAPI32

        if not defined(_APISET_EVENTING):
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                if WINVER >= _WIN32_WINNT_VISTA:
                    # EXTERN_C
                    # ULONG
                    # WMIAPI
                    # EnableTraceEx(
                    # _In_ LPCGUID ProviderId,
                    # _In_opt_ LPCGUID SourceId,
                    # _In_ TRACEHANDLE TraceHandle,
                    # _In_ ULONG IsEnabled,
                    # _In_ UCHAR Level,
                    # _In_ ULONGLONG MatchAnyKeyword,
                    # _In_ ULONGLONG MatchAllKeyword,
                    # _In_ ULONG EnableProperty,
                    # _In_opt_ PEVENT_FILTER_DESCRIPTOR EnableFilterDesc
                    # );
                    EnableTraceEx = advapi32.EnableTraceEx
                    EnableTraceEx.restype = ULONG

                # END IF
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        # END IF   _APISET_EVENTING
        ENABLE_TRACE_PARAMETERS_VERSION = 1
        ENABLE_TRACE_PARAMETERS_VERSION_2 = 2


        _ENABLE_TRACE_PARAMETERS_V1._fields_ = [
            ('Version', ULONG),
            ('EnableProperty', ULONG),
            ('ControlFlags', ULONG),
            ('SourceId', GUID),
            ('EnableFilterDesc', PEVENT_FILTER_DESCRIPTOR),
        ]

        _ENABLE_TRACE_PARAMETERS._fields_ = [
            ('Version', ULONG),
            ('EnableProperty', ULONG),
            ('ControlFlags', ULONG),
            ('SourceId', GUID),
            ('EnableFilterDesc', PEVENT_FILTER_DESCRIPTOR),
            ('FilterDescCount', ULONG),
        ]
                    advapi32 = ctypes.windll.ADVAPI32

        if not defined(_APISET_EVENTING):
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                if WINVER >= _WIN32_WINNT_WIN7:
                    # EXTERN_C
                    # ULONG
                    # WMIAPI
                    # EnableTraceEx2(
                    # _In_ TRACEHANDLE TraceHandle,
                    # _In_ LPCGUID ProviderId,
                    # _In_ ULONG ControlCode,
                    # _In_ UCHAR Level,
                    # _In_ ULONGLONG MatchAnyKeyword,
                    # _In_ ULONGLONG MatchAllKeyword,
                    # _In_ ULONG Timeout,
                    # _In_opt_ PENABLE_TRACE_PARAMETERS EnableParameters
                    # );
                    EnableTraceEx2 = advapi32.EnableTraceEx2
                    EnableTraceEx2.restype = ULONG

                # END IF
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        # END IF   _APISET_EVENTING
        class _TRACE_QUERY_INFO_CLASS(ENUM):
            TraceGuidQueryList = 1
            TraceGuidQueryInfo = 2
            TraceGuidQueryProcess = 3
            TraceStackTracingInfo = 4
            TraceSystemTraceEnableFlagsInfo = 5
            TraceSampledProfileIntervalInfo = 6
            TraceProfileSourceConfigInfo = 7
            TraceProfileSourceListInfo = 8
            TracePmcEventListInfo = 9
            TracePmcCounterListInfo = 10
            TraceSetDisallowList = 11
            TraceVersionInfo = 12
            TraceGroupQueryList = 13
            TraceGroupQueryInfo = 14
            TraceDisallowListQuery = 15
            TraceCompressionInfo = 16
            TracePeriodicCaptureStateListInfo = 17
            TracePeriodicCaptureStateInfo = 18
            TraceProviderBinaryTracking = 19
            TraceMaxLoggersQuery = 20
            MaxTraceSetInfoClass = 21

        TRACE_QUERY_INFO_CLASS = _TRACE_QUERY_INFO_CLASS
        TRACE_INFO_CLASS = _TRACE_QUERY_INFO_CLASS
                    advapi32 = ctypes.windll.ADVAPI32

        if not defined(_APISET_EVENTING):
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                if WINVER >= _WIN32_WINNT_VISTA:
                    # EXTERN_C
                    # ULONG
                    # WMIAPI
                    # EnumerateTraceGuidsEx(
                    # _In_ TRACE_QUERY_INFO_CLASS TraceQueryInfoClass,
                    # _In_reads_bytes_opt_(InBufferSize) PVOID InBuffer,
                    # _In_ ULONG InBufferSize,
                    # _Out_writes_bytes_opt_(OutBufferSize) PVOID OutBuffer,
                    # _In_ ULONG OutBufferSize,
                    # _Out_ PULONG ReturnLength
                    # );
                    EnumerateTraceGuidsEx = advapi32.EnumerateTraceGuidsEx
                    EnumerateTraceGuidsEx.restype = ULONG

                # END IF
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        # END IF   _APISET_EVENTING
        _CLASSIC_EVENT_ID._fields_ = [
            ('EventGuid', GUID),
            ('Type', UCHAR),
            ('Reserved', UCHAR * 7),
        ]

        _TRACE_PROFILE_INTERVAL._fields_ = [
            ('Source', ULONG),
            ('Interval', ULONG),
        ]

        _TRACE_VERSION_INFO._fields_ = [
            ('EtwTraceProcessingVersion', UINT),
            ('Reserved', UINT),
        ]

        _TRACE_PERIODIC_CAPTURE_STATE_INFO._fields_ = [
            ('CaptureStateFrequencyInSeconds', ULONG),
            ('ProviderCount', USHORT),
            ('Reserved', USHORT),
        ]
                    advapi32 = ctypes.windll.ADVAPI32

        if not defined(_APISET_EVENTING):
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
                if WINVER >= _WIN32_WINNT_WIN7:
                    # EXTERN_C
                    # ULONG
                    # WMIAPI
                    # TraceSetInformation(
                    # _In_ TRACEHANDLE SessionHandle,
                    # _In_ TRACE_INFO_CLASS InformationClass,
                    # _In_reads_bytes_(InformationLength) PVOID TraceInformation,
                    # _In_ ULONG InformationLength
                    # );
                    TraceSetInformation = advapi32.TraceSetInformation
                    TraceSetInformation.restype = ULONG

                # END IF
                if WINVER >= _WIN32_WINNT_WIN8:
                    pass
                # END IF
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
            # Data Provider APIs
                advapi32 = ctypes.windll.ADVAPI32

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
                # EXTERN_C
                # ULONG
                # WMIAPI
                # CreateTraceInstanceId(
                # _In_ HANDLE RegHandle,
                # _Inout_ PEVENT_INSTANCE_INFO InstInfo
                # );
                CreateTraceInstanceId = advapi32.CreateTraceInstanceId
                CreateTraceInstanceId.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
                # Use the routine below to generate and record an event trace
                # EXTERN_C
                # ULONG
                # WMIAPI
                # TraceEvent(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_ PEVENT_TRACE_HEADER EventTrace
                # );
                TraceEvent = advapi32.TraceEvent
                TraceEvent.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
                advapi32 = ctypes.windll.ADVAPI32

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
                # EXTERN_C
                # ULONG
                # WMIAPI
                # TraceEventInstance(
                # _In_ TRACEHANDLE TraceHandle,
                # _In_ PEVENT_INSTANCE_HEADER EventTrace,
                # _In_ PEVENT_INSTANCE_INFO InstInfo,
                # _In_opt_ PEVENT_INSTANCE_INFO ParentInstInfo
                # );
                TraceEventInstance = advapi32.TraceEventInstance
                TraceEventInstance.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                # Use the routine below to register a guid for tracing.
                # ULONG
                # RegisterTraceGuids(
                # _In_ WMIDPREQUEST RequestAddress,
                # _In_opt_ PVOID RequestContext,
                # _In_ LPCGUID ControlGuid,
                # _In_ ULONG GuidCount,
                # _In_reads_opt_(GuidCount) PTRACE_GUID_REGISTRATION
                # TraceGuidReg,
                # _In_opt_ LPCTSTR MofImagePath,
                # _In_opt_ LPCTSTR MofResourceName,
                # _Out_ PTRACEHANDLE RegistrationHandle
                # );
                # EXTERN_C
                # ULONG
                # WMIAPI
                # RegisterTraceGuidsW(
                # _In_ WMIDPREQUEST RequestAddress,
                # _In_opt_ PVOID RequestContext,
                # _In_ LPCGUID ControlGuid,
                # _In_ ULONG GuidCount,
                # _In_reads_opt_(GuidCount) PTRACE_GUID_REGISTRATION TraceGuidReg,
                # _In_opt_ LPCWSTR MofImagePath,
                # _In_opt_ LPCWSTR MofResourceName,
                # _Out_ PTRACEHANDLE RegistrationHandle
                # );
                RegisterTraceGuidsW = advapi32.RegisterTraceGuidsW
                RegisterTraceGuidsW.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
                advapi32 = ctypes.windll.ADVAPI32

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
                # EXTERN_C
                # ULONG
                # WMIAPI
                # RegisterTraceGuidsA(
                # _In_ WMIDPREQUEST RequestAddress,
                # _In_opt_ PVOID RequestContext,
                # _In_ LPCGUID ControlGuid,
                # _In_ ULONG GuidCount,
                # _In_reads_opt_(GuidCount) PTRACE_GUID_REGISTRATION TraceGuidReg,
                # _In_opt_ LPCSTR MofImagePath,
                # _In_opt_ LPCSTR MofResourceName,
                # _Out_ PTRACEHANDLE RegistrationHandle
                # );
                RegisterTraceGuidsA = advapi32.RegisterTraceGuidsA
                RegisterTraceGuidsA.restype = ULONG


                    advapi32 = ctypes.windll.ADVAPI32

                if WINVER >= _WIN32_WINNT_WINXP:
                    # EXTERN_C
                    # ULONG
                    # WMIAPI
                    # EnumerateTraceGuids(
                    # _Inout_updates_(PropertyArrayCount) PTRACE_GUID_PROPERTIES *GuidPropertiesArray,
                    # _In_ ULONG PropertyArrayCount,
                    # _Out_ PULONG GuidCount
                    # );
                    EnumerateTraceGuids = advapi32.EnumerateTraceGuids
                    EnumerateTraceGuids.restype = ULONG

                # END IF
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
                advapi32 = ctypes.windll.ADVAPI32

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                # EXTERN_C
                # ULONG
                # WMIAPI
                # UnregisterTraceGuids(
                # _In_ TRACEHANDLE RegistrationHandle
                # );
                UnregisterTraceGuids = advapi32.UnregisterTraceGuids
                UnregisterTraceGuids.restype = ULONG


                # EXTERN_C
                # TRACEHANDLE
                # WMIAPI
                # GetTraceLoggerHandle(
                # _In_ PVOID Buffer
                # );
                GetTraceLoggerHandle = advapi32.GetTraceLoggerHandle
                GetTraceLoggerHandle.restype = TRACEHANDLE


                # EXTERN_C
                # UCHAR
                # WMIAPI
                # GetTraceEnableLevel(
                # _In_ TRACEHANDLE TraceHandle
                # );
                GetTraceEnableLevel = advapi32.GetTraceEnableLevel
                GetTraceEnableLevel.restype = UCHAR


                # EXTERN_C
                # ULONG
                # WMIAPI
                # GetTraceEnableFlags(
                # _In_ TRACEHANDLE TraceHandle
                # );
                GetTraceEnableFlags = advapi32.GetTraceEnableFlags
                GetTraceEnableFlags.restype = ULONG


                # Data Consumer APIs and structures start here
                # TRACEHANDLE
                # OpenTrace(
                # _Inout_ PEVENT_TRACE_LOGFILE Logfile
                # );
                # EXTERN_C
                # ETW_APP_DECLSPEC_DEPRECATED
                # TRACEHANDLE
                # WMIAPI
                # OpenTraceW(
                # _Inout_ PEVENT_TRACE_LOGFILEW Logfile
                # );
                OpenTraceW = advapi32.OpenTraceW
                OpenTraceW.restype = TRACEHANDLE


                # EXTERN_C
                # ETW_APP_DECLSPEC_DEPRECATED
                # ULONG
                # WMIAPI
                # ProcessTrace(
                # _In_reads_(HandleCount) PTRACEHANDLE HandleArray,
                # _In_ ULONG HandleCount,
                # _In_opt_ LPFILETIME StartTime,
                # _In_opt_ LPFILETIME EndTime
                # );
                ProcessTrace = advapi32.ProcessTrace
                ProcessTrace.restype = ULONG


                # EXTERN_C
                # ETW_APP_DECLSPEC_DEPRECATED
                # ULONG
                # WMIAPI
                # CloseTrace(
                # _In_ TRACEHANDLE TraceHandle
                # );
                CloseTrace = advapi32.CloseTrace
                CloseTrace.restype = ULONG


                # Structures and enums for QueryTraceProcessingHandle
                class _ETW_PROCESS_HANDLE_INFO_TYPE(ENUM):
                    EtwQueryPartitionInformation = 1
                    EtwQueryProcessHandleInfoMax = 2

                ETW_PROCESS_HANDLE_INFO_TYPE = _ETW_PROCESS_HANDLE_INFO_TYPE

                _ETW_TRACE_PARTITION_INFORMATION._fields_ = [
                    ('PartitionId', GUID),
                    ('ParentId', GUID),
                    ('Reserved', ULONG64),
                    ('PartitionType', ULONG),
                ]
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
                # Data Consumer APIs and structures start here
                # TRACEHANDLE
                # OpenTrace(
                # _Inout_ PEVENT_TRACE_LOGFILE Logfile
                # );
                # EXTERN_C
                # TRACEHANDLE
                # WMIAPI
                # OpenTraceA(
                # _Inout_ PEVENT_TRACE_LOGFILEA Logfile
                # );
                OpenTraceA = advapi32.OpenTraceA
                OpenTraceA.restype = TRACEHANDLE


                # EXTERN_C
                # ULONG
                # WMIAPI
                # SetTraceCallback(
                # _In_ LPCGUID pGuid,
                # _In_ PEVENT_CALLBACK EventCallback
                # );
                SetTraceCallback = advapi32.SetTraceCallback
                SetTraceCallback.restype = ULONG


                # EXTERN_C
                # ULONG
                # WMIAPI
                # RemoveTraceCallback(
                # _In_ LPCGUID pGuid
                # );
                RemoveTraceCallback = advapi32.RemoveTraceCallback
                RemoveTraceCallback.restype = ULONG


                # The routines for tracing Messages follow            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
                advapi32 = ctypes.windll.ADVAPI32

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                # EXTERN_C
                # ULONG
                # __cdecl
                # TraceMessage(
                # _In_ TRACEHANDLE LoggerHandle,
                # _In_ ULONG MessageFlags,
                # _In_ LPCGUID MessageGuid,
                # _In_ USHORT MessageNumber,
                # ...
                # );
                TraceMessage = advapi32.TraceMessage
                TraceMessage.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
                advapi32 = ctypes.windll.ADVAPI32

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
                # EXTERN_C
                # ULONG
                # TraceMessageVa(
                # _In_ TRACEHANDLE LoggerHandle,
                # _In_ ULONG MessageFlags,
                # _In_ LPCGUID MessageGuid,
                # _In_ USHORT MessageNumber,
                # _In_ va_list MessageArgList
                # );
                TraceMessageVa = advapi32.TraceMessageVa
                TraceMessageVa.restype = ULONG

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
        # END IF   _APISET_EVENTING
            advapi32 = ctypes.windll.ADVAPI32

        if defined(__cplusplus):
            # } // extern "C"
            # #endif
            # 
            # #pragma region Application Family or OneCore Family
            # #if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
            # 
            # #define INVALID_PROCESSTRACE_HANDLE ((TRACEHANDLE)INVALID_HANDLE_VALUE)
            # 
            # #endif // WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
            # #pragma endregion
            # 
            # #ifndef _APISET_EVENTING
            # 
            # 
            # 
            # // Define the encoding independent routines
            # 
            # 
            # #if defined(UNICODE) or defined(_UNICODE)
            # 
            # #pragma region Application Family or OneCore Family
            # #if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
            # 
            # #define RegisterTraceGuids      RegisterTraceGuidsW
            # #define StartTrace              StartTraceW
            # #define ControlTrace            ControlTraceW
            # #if defined(__TRACE_W2K_COMPATIBLE)
            # #define StopTrace(a,b,c)        ControlTraceW((a),(b),(c), EVENT_TRACE_CONTROL_STOP)
            # #define QueryTrace(a,b,c)       ControlTraceW((a),(b),(c), EVENT_TRACE_CONTROL_QUERY)
            # #define UpdateTrace(a,b,c)      ControlTraceW((a),(b),(c), EVENT_TRACE_CONTROL_UPDATE)
            # #else
            # #define StopTrace               StopTraceW
            # #define QueryTrace              QueryTraceW
            # #define UpdateTrace             UpdateTraceW
            # #endif
            # #if (NTDDI_VERSION >= NTDDI_WINXP)
            # #define FlushTrace              FlushTraceW
            # #endif // NTDDI_VERSION >= NTDDI_WINXP
            # #define QueryAllTraces          QueryAllTracesW
            # #define OpenTrace               OpenTraceW
            # 
            # #endif // WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP| WINAPI_PARTITION_SYSTEM)
            # #pragma endregion
            # 
            # #else
            # 
            # #pragma region Desktop Family
            # #if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
            # 
            # #define RegisterTraceGuids      RegisterTraceGuidsA
            # #define StartTrace              StartTraceA
            # #define ControlTrace            ControlTraceA
            # #if defined(__TRACE_W2K_COMPATIBLE)
            # #define StopTrace(a,b,c)        ControlTraceA((a),(b),(c), EVENT_TRACE_CONTROL_STOP)
            # #define QueryTrace(a,b,c)       ControlTraceA((a),(b),(c), EVENT_TRACE_CONTROL_QUERY)
            # #define UpdateTrace(a,b,c)      ControlTraceA((a),(b),(c), EVENT_TRACE_CONTROL_UPDATE)
            # #else
            # #define StopTrace               StopTraceA
            # #define QueryTrace              QueryTraceA
            # #define UpdateTrace             UpdateTraceA
            # #endif
            # #if (NTDDI_VERSION >= NTDDI_WINXP)
            # #define FlushTrace              FlushTraceA
            # #endif // NTDDI_VERSION >= NTDDI_WINXP
            # #define QueryAllTraces          QueryAllTracesA
            # #define OpenTrace               OpenTraceA
            # 
            # #endif // WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
            # #pragma endregion
            # 
            # #endif // UNICODE
            # 
            # #endif // _APISET_EVENTING
            # 
            # #endif // not _EVNTRACE_KERNEL_MODE
            # 
            # #endif // WINNT
            # 
            # #if _MSC_VER >= 1200
            # #pragma warning(pop)
            # #endif
            # 
            # #endif // _EVNTRACE_
            # 
            ControlTraceW = advapi32.ControlTraceW
            ControlTraceW.restype = #define
