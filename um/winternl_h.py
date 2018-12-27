import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_WINTERNL_ = None
NT_SUCCESS = None
NT_INFORMATION = None
NT_WARNING = None
NT_ERROR = None
InitializeObjectAttributes = None


class _STRING(ctypes.Structure):
    pass


STRING = _STRING


class _UNICODE_STRING(ctypes.Structure):
    pass


UNICODE_STRING = _UNICODE_STRING


class _CLIENT_ID(ctypes.Structure):
    pass


CLIENT_ID = _CLIENT_ID


class _PEB_LDR_DATA(ctypes.Structure):
    pass


PEB_LDR_DATA = _PEB_LDR_DATA
PPEB_LDR_DATA = POINTER(_PEB_LDR_DATA)


class _LDR_DATA_TABLE_ENTRY(ctypes.Structure):
    pass


LDR_DATA_TABLE_ENTRY = _LDR_DATA_TABLE_ENTRY
PLDR_DATA_TABLE_ENTRY = POINTER(_LDR_DATA_TABLE_ENTRY)


class _RTL_USER_PROCESS_PARAMETERS(ctypes.Structure):
    pass


RTL_USER_PROCESS_PARAMETERS = _RTL_USER_PROCESS_PARAMETERS
PRTL_USER_PROCESS_PARAMETERS = POINTER(_RTL_USER_PROCESS_PARAMETERS)


class _PEB(ctypes.Structure):
    pass


PEB = _PEB
PPEB = POINTER(_PEB)


class _TEB(ctypes.Structure):
    pass


TEB = _TEB
PTEB = POINTER(_TEB)


class _OBJECT_ATTRIBUTES(ctypes.Structure):
    pass


OBJECT_ATTRIBUTES = _OBJECT_ATTRIBUTES


class _IO_STATUS_BLOCK(ctypes.Structure):
    pass


IO_STATUS_BLOCK = _IO_STATUS_BLOCK
PIO_STATUS_BLOCK = POINTER(_IO_STATUS_BLOCK)


class _PROCESS_BASIC_INFORMATION(ctypes.Structure):
    pass


PROCESS_BASIC_INFORMATION = _PROCESS_BASIC_INFORMATION


class _SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION(ctypes.Structure):
    pass


SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION = _SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION
PSYSTEM_PROCESSOR_PERFORMANCE_INFORMATION = POINTER(_SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION)


class _SYSTEM_PROCESS_INFORMATION(ctypes.Structure):
    pass


SYSTEM_PROCESS_INFORMATION = _SYSTEM_PROCESS_INFORMATION
PSYSTEM_PROCESS_INFORMATION = POINTER(_SYSTEM_PROCESS_INFORMATION)


class _SYSTEM_THREAD_INFORMATION(ctypes.Structure):
    pass


SYSTEM_THREAD_INFORMATION = _SYSTEM_THREAD_INFORMATION
PSYSTEM_THREAD_INFORMATION = POINTER(_SYSTEM_THREAD_INFORMATION)


class _SYSTEM_REGISTRY_QUOTA_INFORMATION(ctypes.Structure):
    pass


SYSTEM_REGISTRY_QUOTA_INFORMATION = _SYSTEM_REGISTRY_QUOTA_INFORMATION
PSYSTEM_REGISTRY_QUOTA_INFORMATION = POINTER(_SYSTEM_REGISTRY_QUOTA_INFORMATION)


class _SYSTEM_BASIC_INFORMATION(ctypes.Structure):
    pass


SYSTEM_BASIC_INFORMATION = _SYSTEM_BASIC_INFORMATION
PSYSTEM_BASIC_INFORMATION = POINTER(_SYSTEM_BASIC_INFORMATION)


class _SYSTEM_TIMEOFDAY_INFORMATION(ctypes.Structure):
    pass


SYSTEM_TIMEOFDAY_INFORMATION = _SYSTEM_TIMEOFDAY_INFORMATION
PSYSTEM_TIMEOFDAY_INFORMATION = POINTER(_SYSTEM_TIMEOFDAY_INFORMATION)


class _SYSTEM_PERFORMANCE_INFORMATION(ctypes.Structure):
    pass


SYSTEM_PERFORMANCE_INFORMATION = _SYSTEM_PERFORMANCE_INFORMATION
PSYSTEM_PERFORMANCE_INFORMATION = POINTER(_SYSTEM_PERFORMANCE_INFORMATION)


class _SYSTEM_EXCEPTION_INFORMATION(ctypes.Structure):
    pass


SYSTEM_EXCEPTION_INFORMATION = _SYSTEM_EXCEPTION_INFORMATION
PSYSTEM_EXCEPTION_INFORMATION = POINTER(_SYSTEM_EXCEPTION_INFORMATION)


class _SYSTEM_LOOKASIDE_INFORMATION(ctypes.Structure):
    pass


SYSTEM_LOOKASIDE_INFORMATION = _SYSTEM_LOOKASIDE_INFORMATION
PSYSTEM_LOOKASIDE_INFORMATION = POINTER(_SYSTEM_LOOKASIDE_INFORMATION)


class _SYSTEM_INTERRUPT_INFORMATION(ctypes.Structure):
    pass


SYSTEM_INTERRUPT_INFORMATION = _SYSTEM_INTERRUPT_INFORMATION
PSYSTEM_INTERRUPT_INFORMATION = POINTER(_SYSTEM_INTERRUPT_INFORMATION)


class _SYSTEM_POLICY_INFORMATION(ctypes.Structure):
    pass


SYSTEM_POLICY_INFORMATION = _SYSTEM_POLICY_INFORMATION
PSYSTEM_POLICY_INFORMATION = POINTER(_SYSTEM_POLICY_INFORMATION)


class _PUBLIC_OBJECT_BASIC_INFORMATION(ctypes.Structure):
    pass


PUBLIC_OBJECT_BASIC_INFORMATION = _PUBLIC_OBJECT_BASIC_INFORMATION
PPUBLIC_OBJECT_BASIC_INFORMATION = POINTER(_PUBLIC_OBJECT_BASIC_INFORMATION)


class __PUBLIC_OBJECT_TYPE_INFORMATION(ctypes.Structure):
    pass


PUBLIC_OBJECT_TYPE_INFORMATION = __PUBLIC_OBJECT_TYPE_INFORMATION
PPUBLIC_OBJECT_TYPE_INFORMATION = POINTER(__PUBLIC_OBJECT_TYPE_INFORMATION)


class _KEY_VALUE_ENTRY(ctypes.Structure):
    pass


KEY_VALUE_ENTRY = _KEY_VALUE_ENTRY
PKEY_VALUE_ENTRY = POINTER(_KEY_VALUE_ENTRY)


class _WINSTATIONINFORMATIONW(ctypes.Structure):
    pass


WINSTATIONINFORMATIONW = _WINSTATIONINFORMATIONW
PWINSTATIONINFORMATIONW = POINTER(_WINSTATIONINFORMATIONW)


# **********************************************************************
# * winternl.h -- This module defines the internal NT APIs and data *
# structures that are intended for the use only by internal core * Windows
# components. These APIs and data structures may change * at any time. * *
# These APIs and data structures are subject to changes from one * Windows
# release to another Windows release. To maintain the * compatiblity of your
# application, avoid using these APIs and * data structures. * * The
# appropriate mechanism for accessing the functions defined in * this header
# is to use LoadLibrary() for ntdll.dll and * GetProcAddress() for the
# particular function. By using this * approach, your application will be more
# resilient to changes * for these functions between Windows releases. If a
# function * prototype does change, then GetProcAddress() for that function *
# might detect the change and fail the function call, which your * application
# will be able to detect. GetProcAddress() may not * be able to detect all
# signature changes, thus avoid using these * internal functions. Instead,
# your application should use the * appropriate Win32 function that provides
# equivalent or similiar * functionality. * * Copyright (c) Microsoft Corp.
# All rights reserved. * *
# *********************************************************************
if not defined(_WINTERNL_):
    _WINTERNL_ = VOID

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.um.winnt_h import *  # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if _WIN32_WINNT >= 0x0500:
            from pyWinAPI.shared.windef_h import * # NOQA

            if defined(__cplusplus):
                pass
            # END IF

            # These data structures and type definitions are needed for
            # compilation and
            # use of the internal Windows APIs defined in this header.
            # typedef _Return_type_success_(return >= 0) LONG NTSTATUS;

            NTSTATUS = LONG
            PCSZ = POINTER(CHAR)

            _STRING._fields_ = [
                ('Length', USHORT),
                ('MaximumLength', USHORT),
                ('Buffer', PCHAR),
            ]

            PSTRING = POINTER(STRING)
            ANSI_STRING = STRING
            PANSI_STRING = PSTRING
            PCANSI_STRING = PSTRING
            OEM_STRING = STRING
            POEM_STRING = PSTRING
            PCOEM_STRING = POINTER(STRING)

            _UNICODE_STRING._fields_ = [
                ('Length', USHORT),
                ('MaximumLength', USHORT),
                ('Buffer', PWSTR),
            ]

            PUNICODE_STRING = POINTER(UNICODE_STRING)
            PCUNICODE_STRING = POINTER(UNICODE_STRING)
            KPRIORITY = LONG

            _CLIENT_ID._fields_ = [
                ('UniqueProcess', HANDLE),
                ('UniqueThread', HANDLE),
            ]

            # The PEB_LDR_DATA, LDR_DATA_TABLE_ENTRY,
            # RTL_USER_PROCESS_PARAMETERS, PEB
            # and TEB structures are subject to changes between Windows
            # releases; thus,
            # the field offsets and reserved fields may change. The reserved
            # fields are
            # reserved for use only by the Windows operating systems. Do not
            # assume a
            # maximum size for these structures.
            # Instead of using the InMemoryOrderModuleList field of the
            # LDR_DATA_TABLE_ENTRY structure, use the Win32 API
            # EnumProcessModules
            # Instead of using the IsBeingDebugged field of the PEB structure,
            # use the
            # Win32 APIs IsDebuggerPresent or CheckRemoteDebuggerPresent
            # Instead of using the SessionId field of the PEB structure, use
            # the Win32
            # APIs GetCurrentProcessId and ProcessIdToSessionId
            # Instead of using the Tls fields of the TEB structure, use the
            # Win32 APIs
            # TlsAlloc, TlsGetValue, TlsSetValue and TlsFree
            # Instead of using the ReservedForOle field, use the COM API
            # CoGetContextToken
            # Sample x86 assembly code that gets the SessionId
            # (subject to change
            # between Windows releases, use the Win32 APIs to make your
            # application
            # resilient to changes)
            # mov  eax,fs:[00000018]
            # mov  eax,[eax + 0x30]
            # mov  eax,[eax + 0x1d4]
            # N.B. Fields marked as reserved do not necessarily reflect the
            # structure
            # of the real struct. They may simply guarantee that the offets of
            # the exposed fields are correct. When code matches this pattern,
            # TYPE1 ExposedField1;
            # BYTE ReservedBytes[b];
            # PVOID ReservedPtrs[p];
            # TYPE2 ExposedField2;
            # or that pattern with ReservedBytes and ReservedPtrs swapped, it
            # is
            # likely that 'b' and 'p' are derived from the following system:
            # GapThirtyTwo = 4p + b
            # GapSixtyFour = 8p + b
            # where GapThirtyTwo is the number of bytes between the two exposed
            # fields in the 32-bit version of the real struct and GapSixtyFour
            # is the number of bytes between the two exposed fields in the
            # 64-bit
            # version of the real struct.
            # Also note that such code must take into account the alignment of
            # the ReservedPtrs field.
            _PEB_LDR_DATA._fields_ = [
                ('Reserved1', BYTE * 8),
                ('Reserved2', PVOID * 3),
                ('InMemoryOrderModuleList', LIST_ENTRY),
            ]


            class DUMMYUNIONNAME(ctypes.Union):
                pass


            DUMMYUNIONNAME._fields_ = [
                ('CheckSum', ULONG),
                ('Reserved6', PVOID),
            ]
            _LDR_DATA_TABLE_ENTRY.DUMMYUNIONNAME = DUMMYUNIONNAME


            _LDR_DATA_TABLE_ENTRY._fields_ = [
                ('Reserved1', PVOID * 2),
                ('InMemoryOrderLinks', LIST_ENTRY),
                ('Reserved2', PVOID * 2),
                ('DllBase', PVOID),
                ('Reserved3', PVOID * 2),
                ('FullDllName', UNICODE_STRING),
                ('Reserved4', BYTE * 8),
                ('Reserved5', PVOID * 3),
                # we'll always use the Microsoft compiler
                ('DUMMYUNIONNAME', _LDR_DATA_TABLE_ENTRY.DUMMYUNIONNAME),
                ('TimeDateStamp', ULONG),
            ]

            _RTL_USER_PROCESS_PARAMETERS._fields_ = [
                ('Reserved1', BYTE * 16),
                ('Reserved2', PVOID * 10),
                ('ImagePathName', UNICODE_STRING),
                ('CommandLine', UNICODE_STRING),
            ]

            # VOID
            # (NTAPI *PPS_POST_PROCESS_INIT_ROUTINE) (
            # VOID
            # );
            PPS_POST_PROCESS_INIT_ROUTINE = NTAPI(
                VOID,
            )


            _PEB._fields_ = [
                ('Reserved1', BYTE * 2),
                ('BeingDebugged', BYTE),
                ('Reserved2', BYTE * 1),
                ('Reserved3', PVOID * 2),
                ('Ldr', PPEB_LDR_DATA),
                ('ProcessParameters', PRTL_USER_PROCESS_PARAMETERS),
                ('Reserved4', PVOID * 3),
                ('AtlThunkSListPtr', PVOID),
                ('Reserved5', PVOID),
                ('Reserved6', ULONG),
                ('Reserved7', PVOID),
                ('Reserved8', ULONG),
                ('AtlThunkSListPtr32', ULONG),
                ('Reserved9', PVOID * 45),
                ('Reserved10', BYTE * 96),
                ('PostProcessInitRoutine', PPS_POST_PROCESS_INIT_ROUTINE),
                ('Reserved11', BYTE * 128),
                ('Reserved12', PVOID * 1),
                ('SessionId', ULONG),
            ]

            _TEB._fields_ = [
                ('Reserved1', PVOID * 12),
                ('ProcessEnvironmentBlock', PPEB),
                ('Reserved2', PVOID * 399),
                ('Reserved3', BYTE * 1952),
                ('TlsSlots', PVOID * 64),
                ('Reserved4', BYTE * 8),
                ('Reserved5', PVOID * 26),
                # Windows 2000 only
                ('ReservedForOle', PVOID),
                ('Reserved6', PVOID * 4),
                ('TlsExpansionSlots', PVOID),
            ]

            _OBJECT_ATTRIBUTES._fields_ = [
                ('Length', ULONG),
                ('RootDirectory', HANDLE),
                ('ObjectName', PUNICODE_STRING),
                ('Attributes', ULONG),
                ('SecurityDescriptor', PVOID),
                ('SecurityQualityOfService', PVOID),
            ]
            POBJECT_ATTRIBUTES = POINTER(OBJECT_ATTRIBUTES)


            class DUMMYUNIONNAME(ctypes.Union):
                pass


            DUMMYUNIONNAME._fields_ = [
                ('Status', NTSTATUS),
                ('Pointer', PVOID),
            ]
            _IO_STATUS_BLOCK.DUMMYUNIONNAME = DUMMYUNIONNAME


            _IO_STATUS_BLOCK._fields_ = [
                # we'll always use the Microsoft compiler
                ('DUMMYUNIONNAME', _IO_STATUS_BLOCK.DUMMYUNIONNAME),
            ]

            # VOID
            # (NTAPI *PIO_APC_ROUTINE) (
            # IN PVOID ApcContext,
            # IN PIO_STATUS_BLOCK IoStatusBlock,
            # IN ULONG Reserved
            # );
            PIO_APC_ROUTINE = NTAPI(
                VOID,
                PVOID,
                PIO_STATUS_BLOCK,
                ULONG,
            )


            _PROCESS_BASIC_INFORMATION._fields_ = [
                ('Reserved1', PVOID),
                ('PebBaseAddress', PPEB),
                ('Reserved2', PVOID * 2),
                ('UniqueProcessId', ULONG_PTR),
                ('Reserved3', PVOID),
            ]
            PPROCESS_BASIC_INFORMATION = POINTER(PROCESS_BASIC_INFORMATION)

            _SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION._fields_ = [
                ('IdleTime', LARGE_INTEGER),
                ('KernelTime', LARGE_INTEGER),
                ('UserTime', LARGE_INTEGER),
                ('Reserved1', LARGE_INTEGER * 2),
                ('Reserved2', ULONG),
            ]

            _SYSTEM_PROCESS_INFORMATION._fields_ = [
                ('NextEntryOffset', ULONG),
                ('NumberOfThreads', ULONG),
                ('Reserved1', BYTE * 48),
                ('ImageName', UNICODE_STRING),
                ('BasePriority', KPRIORITY),
                ('UniqueProcessId', HANDLE),
                ('Reserved2', PVOID),
                ('HandleCount', ULONG),
                ('SessionId', ULONG),
                ('Reserved3', PVOID),
                ('PeakVirtualSize', SIZE_T),
                ('VirtualSize', SIZE_T),
                ('Reserved4', ULONG),
                ('PeakWorkingSetSize', SIZE_T),
                ('WorkingSetSize', SIZE_T),
                ('Reserved5', PVOID),
                ('QuotaPagedPoolUsage', SIZE_T),
                ('Reserved6', PVOID),
                ('QuotaNonPagedPoolUsage', SIZE_T),
                ('PagefileUsage', SIZE_T),
                ('PeakPagefileUsage', SIZE_T),
                ('PrivatePageCount', SIZE_T),
                ('Reserved7', LARGE_INTEGER * 6),
            ]

            _SYSTEM_THREAD_INFORMATION._fields_ = [
                ('Reserved1', LARGE_INTEGER * 3),
                ('Reserved2', ULONG),
                ('StartAddress', PVOID),
                ('ClientId', CLIENT_ID),
                ('Priority', KPRIORITY),
                ('BasePriority', LONG),
                ('Reserved3', ULONG),
                ('ThreadState', ULONG),
                ('WaitReason', ULONG),
            ]

            _SYSTEM_REGISTRY_QUOTA_INFORMATION._fields_ = [
                ('RegistryQuotaAllowed', ULONG),
                ('RegistryQuotaUsed', ULONG),
                ('Reserved1', PVOID),
            ]

            _SYSTEM_BASIC_INFORMATION._fields_ = [
                ('Reserved1', BYTE * 24),
                ('Reserved2', PVOID * 4),
                ('NumberOfProcessors', CCHAR),
            ]

            _SYSTEM_TIMEOFDAY_INFORMATION._fields_ = [
                ('Reserved1', BYTE * 48),
            ]

            _SYSTEM_PERFORMANCE_INFORMATION._fields_ = [
                ('Reserved1', BYTE * 312),
            ]

            _SYSTEM_EXCEPTION_INFORMATION._fields_ = [
                ('Reserved1', BYTE * 16),
            ]

            _SYSTEM_LOOKASIDE_INFORMATION._fields_ = [
                ('Reserved1', BYTE * 32),
            ]

            _SYSTEM_INTERRUPT_INFORMATION._fields_ = [
                ('Reserved1', BYTE * 24),
            ]

            _SYSTEM_POLICY_INFORMATION._fields_ = [
                ('Reserved1', PVOID * 2),
                ('Reserved2', ULONG * 3),
            ]


            class _FILE_INFORMATION_CLASS(ENUM):
                FileDirectoryInformation = 1

            FILE_INFORMATION_CLASS = _FILE_INFORMATION_CLASS


            class _PROCESSINFOCLASS(ENUM):
                ProcessBasicInformation = 0
                ProcessDebugPort = 7
                ProcessWow64Information = 26
                ProcessImageFileName = 27
                ProcessBreakOnTermination = 29

            PROCESSINFOCLASS = _PROCESSINFOCLASS


            class _THREADINFOCLASS(ENUM):
                ThreadIsIoPending = 16

            THREADINFOCLASS = _THREADINFOCLASS


            class _SYSTEM_INFORMATION_CLASS(ENUM):
                SystemBasicInformation = 0
                SystemPerformanceInformation = 2
                SystemTimeOfDayInformation = 3
                SystemProcessInformation = 5
                SystemProcessorPerformanceInformation = 8
                SystemInterruptInformation = 23
                SystemExceptionInformation = 33
                SystemRegistryQuotaInformation = 37
                SystemLookasideInformation = 45
                SystemPolicyInformation = 134

            SYSTEM_INFORMATION_CLASS = _SYSTEM_INFORMATION_CLASS

            # Object Information Classes
            class _OBJECT_INFORMATION_CLASS(ENUM):
                ObjectBasicInformation = 0
                ObjectTypeInformation = 2

            OBJECT_INFORMATION_CLASS = _OBJECT_INFORMATION_CLASS

            # Public Object Information definitions
            _PUBLIC_OBJECT_BASIC_INFORMATION._fields_ = [
                ('Attributes', ULONG),
                ('GrantedAccess', ACCESS_MASK),
                ('HandleCount', ULONG),
                ('PointerCount', ULONG),
                # reserved for internal use
                ('Reserved', ULONG * 10),
            ]

            __PUBLIC_OBJECT_TYPE_INFORMATION._fields_ = [
                ('TypeName', UNICODE_STRING),
                # reserved for internal use
                ('Reserved', ULONG * 22),
            ]
            if _WIN32_WINNT >= 0x0501:
                # use the WTS API instead
                # WTSGetActiveConsoleSessionId
                # The active console id is cached as a volatile ULONG in a
                # constant
                # memory location. This x86 memory location is subject to
                # changes between
                # Windows releases. Use the WTS API to make your application
                # resilient to
                # changes.
                INTERNAL_TS_ACTIVE_CONSOLE_ID = 0x7FFE02D8
            # END IF   (_WIN32_WINNT >= 0x0501)

            # These functions are intended for use by internal core Windows
            # components
            # since these functions may change between Windows releases.
            def RtlMoveMemory(Destination, Source, Length):
                return ctypes.memmove(Destination,Source,Length)


            def RtlFillMemory(Destination, Length, Fill):
                return ctypes.memset(Destination, Fill, Length)

            def RtlZeroMemory(Destination, Length):
                return ctypes.memset(Destination, 0, Length)


            # use the Win32 API instead
            # CloseHandle
            ntdll = ctypes.windll.NTDLL

            # __kernel_entry NTSTATUS
            # NTAPI
            # NtClose(
            # IN HANDLE Handle
            # );
            NtClose = ntdll.NtClose
            NtClose.restype = NTSTATUS

            # use the Win32 API instead
            # CreateFile
            # __kernel_entry NTSTATUS
            # NTAPI
            # NtCreateFile(
            # OUT PHANDLE FileHandle,
            # IN ACCESS_MASK DesiredAccess,
            # IN POBJECT_ATTRIBUTES ObjectAttributes,
            # OUT PIO_STATUS_BLOCK IoStatusBlock,
            # IN PLARGE_INTEGER AllocationSize OPTIONAL,
            # IN ULONG FileAttributes,
            # IN ULONG ShareAccess,
            # IN ULONG CreateDisposition,
            # IN ULONG CreateOptions,
            # IN PVOID EaBuffer OPTIONAL,
            # IN ULONG EaLength
            # );
            NtCreateFile = ntdll.NtCreateFile
            NtCreateFile.restype = NTSTATUS

            # use the Win32 API instead
            # CreateFile
            # __kernel_entry NTSTATUS
            # NTAPI
            # NtOpenFile(
            # OUT PHANDLE FileHandle,
            # IN ACCESS_MASK DesiredAccess,
            # IN POBJECT_ATTRIBUTES ObjectAttributes,
            # OUT PIO_STATUS_BLOCK IoStatusBlock,
            # IN ULONG ShareAccess,
            # IN ULONG OpenOptions
            # );
            NtOpenFile = ntdll.NtOpenFile
            NtOpenFile.restype = NTSTATUS

            # use the Win32 API instead
            # N/A
            # __kernel_entry NTSTATUS
            # NTAPI
            # NtRenameKey(
            # _In_ HANDLE KeyHandle,
            # _In_ PUNICODE_STRING NewName
            # );
            NtRenameKey = ntdll.NtRenameKey
            NtRenameKey.restype = NTSTATUS

            # use the Win32 API instead
            # RegNotifyChangeKeyValue
            # __kernel_entry NTSTATUS
            # NTAPI
            # NtNotifyChangeMultipleKeys(
            # _In_ HANDLE MasterKeyHandle,
            # _In_opt_ ULONG Count,
            # _In_reads_opt_(Count) OBJECT_ATTRIBUTES SubordinateObjects[],
            # _In_opt_ HANDLE Event,
            # _In_opt_ PIO_APC_ROUTINE ApcRoutine,
            # _In_opt_ PVOID ApcContext,
            # _Out_ PIO_STATUS_BLOCK IoStatusBlock,
            # _In_ ULONG CompletionFilter,
            # _In_ BOOLEAN WatchTree,
            # _Out_writes_bytes_opt_(BufferSize) PVOID Buffer,
            # _In_ ULONG BufferSize,
            # _In_ BOOLEAN Asynchronous
            # );
            NtNotifyChangeMultipleKeys = ntdll.NtNotifyChangeMultipleKeys
            NtNotifyChangeMultipleKeys.restype = NTSTATUS

            # use the Win32 API instead
            # RegQueryValueEx
            _KEY_VALUE_ENTRY._fields_ = [
                ('ValueName', PUNICODE_STRING),
                ('DataLength', ULONG),
                ('DataOffset', ULONG),
                ('Type', ULONG),
            ]

            # __kernel_entry NTSTATUS
            # NTAPI
            # NtQueryMultipleValueKey(
            # _In_ HANDLE KeyHandle,
            # _Inout_updates_(EntryCount) PKEY_VALUE_ENTRY ValueEntries,
            # _In_ ULONG EntryCount,
            # _Out_writes_bytes_(*BufferLength) PVOID ValueBuffer,
            # _Inout_ PULONG BufferLength,
            # _Out_opt_ PULONG RequiredBufferLength
            # );
            NtQueryMultipleValueKey = ntdll.NtQueryMultipleValueKey
            NtQueryMultipleValueKey.restype = NTSTATUS

            # use the Win32 API instead
            # N/A
            class _KEY_SET_INFORMATION_CLASS(ENUM):
                KeyWriteTimeInformation = 1
                KeyWow64FlagsInformation = 2
                KeyControlFlagsInformation = 3
                KeySetVirtualizationInformation = 4
                KeySetDebugInformation = 5
                KeySetHandleTagsInformation = 6
                MaxKeySetInfoClass = 7

            KEY_SET_INFORMATION_CLASS = _KEY_SET_INFORMATION_CLASS

            # __kernel_entry NTSTATUS
            # NTAPI
            # NtSetInformationKey(
            # _In_ HANDLE KeyHandle,
            # _In_ _Strict_type_match_
            # KEY_SET_INFORMATION_CLASS KeySetInformationClass,
            # _In_reads_bytes_(KeySetInformationLength) PVOID KeySetInformation,
            # _In_ ULONG KeySetInformationLength
            # );
            NtSetInformationKey = ntdll.NtSetInformationKey
            NtSetInformationKey.restype = NTSTATUS

            # use the Win32 API instead
            # DeviceIoControl
            # __kernel_entry NTSTATUS
            # NTAPI
            # NtDeviceIoControlFile(
            # IN HANDLE FileHandle,
            # IN HANDLE Event OPTIONAL,
            # IN PIO_APC_ROUTINE ApcRoutine OPTIONAL,
            # IN PVOID ApcContext OPTIONAL,
            # OUT PIO_STATUS_BLOCK IoStatusBlock,
            # IN ULONG IoControlCode,
            # IN PVOID InputBuffer OPTIONAL,
            # IN ULONG InputBufferLength,
            # OUT PVOID OutputBuffer OPTIONAL,
            # IN ULONG OutputBufferLength
            # );
            NtDeviceIoControlFile = ntdll.NtDeviceIoControlFile
            NtDeviceIoControlFile.restype = NTSTATUS

            # use the Win32 API instead
            # WaitForSingleObjectEx
            # NTSTATUS
            # NTAPI
            # NtWaitForSingleObject(
            # IN HANDLE Handle,
            # IN BOOLEAN Alertable,
            # IN PLARGE_INTEGER Timeout OPTIONAL
            # );
            NtWaitForSingleObject = ntdll.NtWaitForSingleObject
            NtWaitForSingleObject.restype = NTSTATUS

            # use the Win32 API instead
            # CheckNameLegalDOS8Dot3
            # BOOLEAN
            # NTAPI
            # RtlIsNameLegalDOS8Dot3(
            # IN PUNICODE_STRING Name,
            # IN OUT POEM_STRING OemName OPTIONAL,
            # IN OUT PBOOLEAN NameContainsSpaces OPTIONAL
            # );
            RtlIsNameLegalDOS8Dot3 = ntdll.RtlIsNameLegalDOS8Dot3
            RtlIsNameLegalDOS8Dot3.restype = BOOLEAN

            # This function might be needed for some of the internal Windows
            # functions,
            # defined in this header file.
            # _When_(Status < 0, _Out_range_(>, 0))
            # _When_(Status >= 0, _Out_range_( == , 0))
            # ULONG
            # NTAPI
            # RtlNtStatusToDosError(
            # NTSTATUS Status
            # );
            RtlNtStatusToDosError = ntdll.RtlNtStatusToDosError
            RtlNtStatusToDosError.restype = ULONG

            # use the Win32 APIs instead
            # GetProcessHandleCount
            # GetProcessId
            # __kernel_entry NTSTATUS
            # NTAPI
            # NtQueryInformationProcess(
            # IN HANDLE ProcessHandle,
            # IN PROCESSINFOCLASS ProcessInformationClass,
            # OUT PVOID ProcessInformation,
            # IN ULONG ProcessInformationLength,
            # OUT PULONG ReturnLength OPTIONAL
            # );
            NtQueryInformationProcess = ntdll.NtQueryInformationProcess
            NtQueryInformationProcess.restype = NTSTATUS

            # use the Win32 API instead
            # GetThreadIOPendingFlag

            # __kernel_entry NTSTATUS
            # NTAPI
            # NtQueryInformationThread(
            # IN HANDLE ThreadHandle,
            # IN THREADINFOCLASS ThreadInformationClass,
            # OUT PVOID ThreadInformation,
            # IN ULONG ThreadInformationLength,
            # OUT PULONG ReturnLength OPTIONAL
            # );
            NtQueryInformationThread = ntdll.NtQueryInformationThread
            NtQueryInformationThread.restype = NTSTATUS

            # use the Win32 APIs instead
            # GetFileInformationByHandle
            # GetFileInformationByHandleEx
            # GetProcessInformation
            # GetThreadInformation

            # __kernel_entry NTSYSCALLAPI
            # NTSTATUS
            # NTAPI
            # NtQueryObject(
            # _In_opt_ HANDLE Handle,
            # _In_ OBJECT_INFORMATION_CLASS ObjectInformationClass,
            # _Out_writes_bytes_opt_(ObjectInformationLength) PVOID ObjectInformation,
            # _In_ ULONG ObjectInformationLength,
            # _Out_opt_ PULONG ReturnLength
            # );
            NtQueryObject = ntdll.NtQueryObject
            NtQueryObject.restype = NTSTATUS

            # use the Win32 APIs instead
            # GetSystemRegistryQuota
            # GetSystemTimes
            # use the CryptoAPIs instead for generating random data
            # CryptGenRandom

            # __kernel_entry NTSTATUS
            # NTAPI
            # NtQuerySystemInformation(
            # IN SYSTEM_INFORMATION_CLASS SystemInformationClass,
            # OUT PVOID SystemInformation,
            # IN ULONG SystemInformationLength,
            # OUT PULONG ReturnLength OPTIONAL
            # );
            NtQuerySystemInformation = ntdll.NtQuerySystemInformation
            NtQuerySystemInformation.restype = NTSTATUS

            # use the Win32 API instead
            # GetSystemTimeAsFileTime
            # __kernel_entry NTSTATUS
            # NTAPI
            # NtQuerySystemTime(
            # OUT PLARGE_INTEGER SystemTime
            # );
            NtQuerySystemTime = ntdll.NtQuerySystemTime
            NtQuerySystemTime.restype = NTSTATUS

            # use the Win32 API instead
            # LocalFileTimeToFileTime
            # NTSTATUS
            # NTAPI
            # RtlLocalTimeToSystemTime(
            # IN PLARGE_INTEGER LocalTime,
            # OUT PLARGE_INTEGER SystemTime
            # );
            RtlLocalTimeToSystemTime = ntdll.RtlLocalTimeToSystemTime
            RtlLocalTimeToSystemTime.restype = NTSTATUS

            # use the Win32 API instead
            # SystemTimeToFileTime to convert to FILETIME structures
            # copy the resulting FILETIME structures to ULARGE_INTEGER
            # structures
            # perform the calculation

            # BOOLEAN
            # NTAPI
            # RtlTimeToSecondsSince1970(
            # PLARGE_INTEGER Time,
            # PULONG ElapsedSeconds
            # );
            RtlTimeToSecondsSince1970 = ntdll.RtlTimeToSecondsSince1970
            RtlTimeToSecondsSince1970.restype = BOOLEAN

            # These APIs might be need for some of the internal Windows
            # functions,
            # defined in this header file.
            # VOID
            # NTAPI
            # RtlFreeAnsiString(
            # PANSI_STRING AnsiString
            # );
            RtlFreeAnsiString = ntdll.RtlFreeAnsiString
            RtlFreeAnsiString.restype = VOID

            # VOID
            # NTAPI
            # RtlFreeUnicodeString(
            # PUNICODE_STRING UnicodeString
            # );
            RtlFreeUnicodeString = ntdll.RtlFreeUnicodeString
            RtlFreeUnicodeString.restype = VOID

            # VOID
            # NTAPI
            # RtlFreeOemString(
            # POEM_STRING OemString
            # );
            RtlFreeOemString = ntdll.RtlFreeOemString
            RtlFreeOemString.restype = VOID

            # VOID
            # NTAPI
            # RtlInitString(
            # PSTRING DestinationString,
            # PCSZ SourceString
            # );
            RtlInitString = ntdll.RtlInitString
            RtlInitString.restype = VOID

            ntoskrnl = ctypes.windll.NTOSKRNL

            # NTSTATUS
            # NTAPI
            # RtlInitStringEx(
            # PSTRING DestinationString,
            # PCSZ SourceString
            # );
            RtlInitStringEx = ntoskrnl.RtlInitStringEx
            RtlInitStringEx.restype = NTSTATUS

            # VOID
            # NTAPI
            # RtlInitAnsiString(
            # PANSI_STRING DestinationString,
            # PCSZ SourceString
            # );
            RtlInitAnsiString = ntdll.RtlInitAnsiString
            RtlInitAnsiString.restype = VOID

            # NTSTATUS
            # NTAPI
            # RtlInitAnsiStringEx(
            # PANSI_STRING DestinationString,
            # PCSZ SourceString
            # );
            RtlInitAnsiStringEx = ntdll.RtlInitAnsiStringEx
            RtlInitAnsiStringEx.restype = NTSTATUS

            # VOID
            # NTAPI
            # RtlInitUnicodeString(
            # PUNICODE_STRING DestinationString,
            # PCWSTR SourceString
            # );
            RtlInitUnicodeString = ntdll.RtlInitUnicodeString
            RtlInitUnicodeString.restype = VOID

            # NTSTATUS
            # NTAPI
            # RtlAnsiStringToUnicodeString(
            # PUNICODE_STRING DestinationString,
            # PCANSI_STRING SourceString,
            # BOOLEAN AllocateDestinationString
            # );
            RtlAnsiStringToUnicodeString = ntdll.RtlAnsiStringToUnicodeString
            RtlAnsiStringToUnicodeString.restype = NTSTATUS

            # NTSTATUS
            # NTAPI
            # RtlUnicodeStringToAnsiString(
            # PANSI_STRING DestinationString,
            # PCUNICODE_STRING SourceString,
            # BOOLEAN AllocateDestinationString
            # );
            RtlUnicodeStringToAnsiString = ntdll.RtlUnicodeStringToAnsiString
            RtlUnicodeStringToAnsiString.restype = NTSTATUS

            # NTSTATUS
            # NTAPI
            # RtlUnicodeStringToOemString(
            # POEM_STRING DestinationString,
            # PCUNICODE_STRING SourceString,
            # BOOLEAN AllocateDestinationString
            # );
            RtlUnicodeStringToOemString = ntdll.RtlUnicodeStringToOemString
            RtlUnicodeStringToOemString.restype = NTSTATUS

            # Use the Win32 API instead
            # WideCharToMultiByte
            # set CodePage to CP_ACP
            # set cbMultiByte to 0
            # NTSTATUS
            # NTAPI
            # RtlUnicodeToMultiByteSize(
            # _Out_ PULONG BytesInMultiByteString,
            # _In_reads_bytes_(BytesInUnicodeString) PWCH UnicodeString,
            # _In_ ULONG BytesInUnicodeString
            # );
            RtlUnicodeToMultiByteSize = ntdll.RtlUnicodeToMultiByteSize
            RtlUnicodeToMultiByteSize.restype = NTSTATUS

            # Use the C runtime function instead
            # strtol
            # NTSTATUS
            # NTAPI
            # RtlCharToInteger(
            # PCSZ String,
            # ULONG Base,
            # PULONG Value
            # );
            RtlCharToInteger = ntdll.RtlCharToInteger
            RtlCharToInteger.restype = NTSTATUS

            # use the Win32 API instead
            # ConvertSidToStringSid
            # NTSTATUS
            # NTAPI
            # RtlConvertSidToUnicodeString(
            # PUNICODE_STRING UnicodeString,
            # PSID Sid,
            # BOOLEAN AllocateDestinationString
            # );
            RtlConvertSidToUnicodeString = ntdll.RtlConvertSidToUnicodeString
            RtlConvertSidToUnicodeString.restype = NTSTATUS

            # use the CryptoAPIs instead
            # CryptGenRandom
            # ULONG
            # NTAPI
            # RtlUniform(
            # PULONG Seed
            # );
            RtlUniform = ntdll.RtlUniform
            RtlUniform.restype = ULONG

            LOGONID_CURRENT = -1
            SERVERNAME_CURRENT = NULL


            class _WINSTATIONINFOCLASS(ENUM):
                WinStationInformation = 8

            WINSTATIONINFOCLASS = _WINSTATIONINFOCLASS

            _WINSTATIONINFORMATIONW._fields_ = [
                ('Reserved2', BYTE * 70),
                ('LogonId', ULONG),
                ('Reserved3', BYTE * 1140),
            ]

            # this function is implemented in winsta.dll
            # (you need to loadlibrary to call this function)
            # this internal function retrives the LogonId
            # (also called SessionId) for the current process
            # You should avoid using this function as it can change. you can
            # retrieve the same information
            # Using public api WTSQuerySessionInformation. Pass WTSSessionId
            # as the WTSInfoClass parameter
            # typedef BOOLEAN (WINAPI * PWINSTATIONQUERYINFORMATIONW)(
            # HANDLE, ULONG, WINSTATIONINFOCLASS, PVOID, ULONG, PULONG );
            PWINSTATIONQUERYINFORMATIONW = WINAPI(
                BOOLEAN,
                HANDLE,
                ULONG,
                WINSTATIONINFOCLASS,
                PVOID,
                ULONG,
                PULONG
            )

            # Generic test for success on any status value
            # (non-negative numbers
            # indicate success).
            if not defined(NT_SUCCESS):
                def NT_SUCCESS(Status):
                    return Status >= 0
            # END IF

            # Generic test for information on any status value.
            if not defined(NT_INFORMATION):
                def NT_INFORMATION(Status):
                    return (Status >> 30) == 1
            # END IF

            # Generic test for warning on any status value.
            if not defined(NT_WARNING):
                def NT_WARNING(Status):
                    return (Status >> 30) == 2
            # END IF

            # Generic test for error on any status value.
            if not defined(NT_ERROR):
                def NT_ERROR(Status):
                    return (Status >> 30) == 3
            # END IF

            # + +
            # VOID
            # InitializeObjectAttributes(
            # OUT POBJECT_ATTRIBUTES p,
            # IN PUNICODE_STRING n,
            # IN ULONG a,
            # IN HANDLE r,
            # IN PSECURITY_DESCRIPTOR s
            # )
            # --
            if not defined(InitializeObjectAttributes):
                def InitializeObjectAttributes(p, n, a, r, s):
                    p.Length = ctypes.sizeof(OBJECT_ATTRIBUTES)
                    p.RootDirectory = r
                    p.Attributes = a
                    p.ObjectName = n
                    p.SecurityDescriptor = s
                    p.SecurityQualityOfService = NULL
                    return p

            # END IF

            # Valid values for the Attributes field
            OBJ_INHERIT = 0x00000002
            OBJ_PERMANENT = 0x00000010
            OBJ_EXCLUSIVE = 0x00000020
            OBJ_CASE_INSENSITIVE = 0x00000040
            OBJ_OPENIF = 0x00000080
            OBJ_OPENLINK = 0x00000100
            OBJ_KERNEL_HANDLE = 0x00000200
            OBJ_FORCE_ACCESS_CHECK = 0x00000400
            OBJ_IGNORE_IMPERSONATED_DEVICEMAP = 0x00000800
            OBJ_DONT_REPARSE = 0x00001000
            OBJ_VALID_ATTRIBUTES = 0x00001FF2
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
            if _WIN32_WINNT >= _WIN32_WINNT_WIN7:
                FILE_OPEN_REQUIRING_OPLOCK = 0x00010000
            # END IF


            FILE_RESERVE_OPFILTER = 0x00100000
            FILE_OPEN_REPARSE_POINT = 0x00200000
            FILE_OPEN_NO_RECALL = 0x00400000
            FILE_OPEN_FOR_FREE_SPACE_QUERY = 0x00800000
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
            if defined(__cplusplus):
                pass
            # END IF

        # END IF   (_WIN32_WINNT >= 0x0500)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF   _WINTERNL_


