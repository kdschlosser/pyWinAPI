
import ctypes

from pyWinAPI import *
from shared.sdkddkver_h import *

from shared.wtypes_h import *

# ********************************************************************** *
# minwinbase.h - - This module defines the 32 - Bit Windows Base APIs * *
# Copyright (c) Microsoft Corp. All rights reserved. * *
# *********************************************************************
if not defined(_MINWINBASE_):
    _MINWINBASE_ = 1

    MAX_PATH = 255

    if not defined(__WINDOWS_DONT_DISABLE_PRAGMA_PACK_WARNING__):
        pass
    # END IF
    if _MSC_VER >= 1200:
        pass
    # END IF
    if _MSC_VER >= 800:
        pass
    # END IF
    if defined(__cplusplus):
        pass
    # END IF

    from um.winnt_h import (
        RtlMoveMemory,
        RtlCopyMemory,
        RtlFillMemory,
        RtlZeroMemory,
        RTL_CRITICAL_SECTION,
        PRTL_CRITICAL_SECTION,
        RTL_CRITICAL_SECTION_DEBUG,
        PRTL_CRITICAL_SECTION_DEBUG,
        EXCEPTION_RECORD
    )

    MoveMemory = RtlMoveMemory
    CopyMemory = RtlCopyMemory
    FillMemory = RtlFillMemory
    ZeroMemory = RtlZeroMemory


    class _SECURITY_ATTRIBUTES(ctypes.Structure):
        pass


    _SECURITY_ATTRIBUTES._fields_ = [
        ('nLength', DWORD),
        ('lpSecurityDescriptor', LPVOID),
        ('bInheritHandle', BOOL),
    ]

    SECURITY_ATTRIBUTES = _SECURITY_ATTRIBUTES
    PSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)
    LPSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)


    class _OVERLAPPED(ctypes.Structure):
        pass

    class DUMMYSTRUCTNAME(ctypes.Structure):
        pass

    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYSTRUCTNAME._fields_ = [
        ('Offset', DWORD),
        ('OffsetHigh', DWORD),
    ]

    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME

    DUMMYUNIONNAME._fields_ = [
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
        ('Pointer', PVOID),
    ]

    _OVERLAPPED.DUMMYUNIONNAME = DUMMYUNIONNAME

    _OVERLAPPED._fields_ = [
        ('Internal', ULONG_PTR),
        ('InternalHigh', ULONG_PTR),
        ('DUMMYUNIONNAME', _OVERLAPPED.DUMMYUNIONNAME),
        ('hEvent', HANDLE),
    ]

    OVERLAPPED = _OVERLAPPED
    LPOVERLAPPED = POINTER(_OVERLAPPED)


    class _OVERLAPPED_ENTRY(ctypes.Structure):
        pass


    _OVERLAPPED_ENTRY._fields_ = [
        ('lpCompletionKey', ULONG_PTR),
        ('lpOverlapped', LPOVERLAPPED),
        ('Internal', ULONG_PTR),
        ('dwNumberOfBytesTransferred', DWORD),
    ]

    OVERLAPPED_ENTRY = _OVERLAPPED_ENTRY
    LPOVERLAPPED_ENTRY = POINTER(_OVERLAPPED_ENTRY)

    if not defined(_FILETIME_):
        _FILETIME_ = 1


        class _FILETIME(ctypes.Structure):
            pass


        _FILETIME._fields_ = [
            ('dwLowDateTime', DWORD),
            ('dwHighDateTime', DWORD),
        ]

        FILETIME = _FILETIME
        PFILETIME = POINTER(_FILETIME)
        LPFILETIME = POINTER(_FILETIME)

    # END IF


    class _SYSTEMTIME(ctypes.Structure):
        pass


    _SYSTEMTIME._fields_ = [
        ('wYear', WORD),
        ('wMonth', WORD),
        ('wDayOfWeek', WORD),
        ('wDay', WORD),
        ('wHour', WORD),
        ('wMinute', WORD),
        ('wSecond', WORD),
        ('wMilliseconds', WORD),
    ]

    SYSTEMTIME = _SYSTEMTIME
    PSYSTEMTIME = POINTER(_SYSTEMTIME)
    LPSYSTEMTIME = POINTER(_SYSTEMTIME)


    class _WIN32_FIND_DATAA(ctypes.Structure):
        pass


    _TEMP_FIELDS = [
        ('dwFileAttributes', DWORD),
        ('ftCreationTime', FILETIME),
        ('ftLastAccessTime', FILETIME),
        ('ftLastWriteTime', FILETIME),
        ('nFileSizeHigh', DWORD),
        ('nFileSizeLow', DWORD),
        ('dwReserved0', DWORD),
        ('dwReserved1', DWORD),
        ('cFileName', CHAR * MAX_PATH),
        ('cAlternateFileName', CHAR * 14),
    ]

    if defined(_MAC):
        _TEMP_FIELDS += [
            ('dwFileType', DWORD),
            ('dwCreatorType', DWORD),
            ('wFinderFlags', WORD),
        ]

    # END IF
    _WIN32_FIND_DATAA._fields_ = _TEMP_FIELDS
    WIN32_FIND_DATAA = _WIN32_FIND_DATAA
    PWIN32_FIND_DATAA = POINTER(_WIN32_FIND_DATAA)
    LPWIN32_FIND_DATAA = POINTER(_WIN32_FIND_DATAA)


    class _WIN32_FIND_DATAW(ctypes.Structure):
        pass


    _TEMP_FIELDS = [
        ('dwFileAttributes', DWORD),
        ('ftCreationTime', FILETIME),
        ('ftLastAccessTime', FILETIME),
        ('ftLastWriteTime', FILETIME),
        ('nFileSizeHigh', DWORD),
        ('nFileSizeLow', DWORD),
        ('dwReserved0', DWORD),
        ('dwReserved1', DWORD),
        ('cFileName', WCHAR * MAX_PATH),
        ('cAlternateFileName', WCHAR * 14),
    ]

    if defined(_MAC):
        _TEMP_FIELDS += [
            ('dwFileType', DWORD),
            ('dwCreatorType', DWORD),
            ('wFinderFlags', WORD),
        ]
    # END IF

    _WIN32_FIND_DATAW._fields_ = _TEMP_FIELDS
    WIN32_FIND_DATAW = _WIN32_FIND_DATAW
    PWIN32_FIND_DATAW = POINTER(_WIN32_FIND_DATAW)
    LPWIN32_FIND_DATAW = POINTER(_WIN32_FIND_DATAW)

    if defined(UNICODE):
        WIN32_FIND_DATA = WIN32_FIND_DATAW
        PWIN32_FIND_DATA = PWIN32_FIND_DATAW
        LPWIN32_FIND_DATA = LPWIN32_FIND_DATAW
    else:
        WIN32_FIND_DATA = WIN32_FIND_DATAA
        PWIN32_FIND_DATA = PWIN32_FIND_DATAA
        LPWIN32_FIND_DATA = LPWIN32_FIND_DATAA
    # END IF   UNICODE

    if _WIN32_WINNT >= 0x0400:

        class _FINDEX_INFO_LEVELS(ENUM):
            FindExInfoStandard = 1
            FindExInfoBasic = 2
            FindExInfoMaxInfoLevel = 3


        FINDEX_INFO_LEVELS = _FINDEX_INFO_LEVELS
        FIND_FIRST_EX_CASE_SENSITIVE = 0x00000001
        FIND_FIRST_EX_LARGE_FETCH = 0x00000002

        if NTDDI_VERSION >= NTDDI_WIN10_RS4:
            FIND_FIRST_EX_ON_DISK_ENTRIES_ONLY = 0x00000004
        # END IF


        class _FINDEX_SEARCH_OPS(ENUM):
            FindExSearchNameMatch = 1
            FindExSearchLimitToDirectories = 2
            FindExSearchLimitToDevices = 3
            FindExSearchMaxSearchOp = 4


        FINDEX_SEARCH_OPS = _FINDEX_SEARCH_OPS
    # END IF  _WIN32_WINNT >= 0x0400

    if _WIN32_WINNT >= 0x0400:
        if NTDDI_VERSION >= NTDDI_WIN10_RS3:

            class _READ_DIRECTORY_NOTIFY_INFORMATION_CLASS(ENUM):
                ReadDirectoryNotifyInformation = 1
                ReadDirectoryNotifyExtendedInformation = 2


            READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = _READ_DIRECTORY_NOTIFY_INFORMATION_CLASS
            PREAD_DIRECTORY_NOTIFY_INFORMATION_CLASS = POINTER(_READ_DIRECTORY_NOTIFY_INFORMATION_CLASS)
        # END IF
    # END IF  _WIN32_WINNT >= 0x0400


    class _GET_FILEEX_INFO_LEVELS(ENUM):
        GetFileExInfoStandard = 1
        GetFileExMaxInfoLevel = 2


    GET_FILEEX_INFO_LEVELS = _GET_FILEEX_INFO_LEVELS

    if _WIN32_WINNT >= _WIN32_WINNT_LONGHORN:

        class _FILE_INFO_BY_HANDLE_CLASS(ENUM):
            FileBasicInfo = 1
            FileStandardInfo = 2
            FileNameInfo = 3
            FileRenameInfo = 4
            FileDispositionInfo = 5
            FileAllocationInfo = 6
            FileEndOfFileInfo = 7
            FileStreamInfo = 8
            FileCompressionInfo = 9
            FileAttributeTagInfo = 10
            FileIdBothDirectoryInfo = 11
            FileIdBothDirectoryRestartInfo = 12
            FileIoPriorityHintInfo = 13
            FileRemoteProtocolInfo = 14
            FileFullDirectoryInfo = 15
            FileFullDirectoryRestartInfo = 16

            if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
                FileStorageInfo = 17
                FileAlignmentInfo = 18
                FileIdInfo = 19
                FileIdExtdDirectoryInfo = 20
                FileIdExtdDirectoryRestartInfo = 21
            # END IF

            if _WIN32_WINNT >= _WIN32_WINNT_WIN10_RS1:
                FileDispositionInfoEx = 22
                FileRenameInfoEx = 23
            # END IF
            MaximumFileInfoByHandleClass = 24

        FILE_INFO_BY_HANDLE_CLASS = _FILE_INFO_BY_HANDLE_CLASS
        PFILE_INFO_BY_HANDLE_CLASS = POINTER(_FILE_INFO_BY_HANDLE_CLASS)


        if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
            pass
        # END IF
        if _WIN32_WINNT >= _WIN32_WINNT_WIN10_RS1:
            pass

        # END IF
    # END IF

    CRITICAL_SECTION = RTL_CRITICAL_SECTION
    PCRITICAL_SECTION = PRTL_CRITICAL_SECTION
    LPCRITICAL_SECTION = PRTL_CRITICAL_SECTION

    CRITICAL_SECTION_DEBUG = RTL_CRITICAL_SECTION_DEBUG
    PCRITICAL_SECTION_DEBUG = PRTL_CRITICAL_SECTION_DEBUG
    LPCRITICAL_SECTION_DEBUG = PRTL_CRITICAL_SECTION_DEBUG

    LOCKFILE_FAIL_IMMEDIATELY = 0x00000001
    LOCKFILE_EXCLUSIVE_LOCK = 0x00000002


    class _PROCESS_HEAP_ENTRY(ctypes.Structure):
        pass

    class DUMMYUNIONNAME(ctypes.Union):
        pass

    class Region(ctypes.Structure):
        pass

    class Block(ctypes.Structure):
        pass


    Block._fields_ = [
        ('hMem', HANDLE),
        ('dwReserved', DWORD * 3),
    ]

    DUMMYUNIONNAME.Block = Block
    Region._fields_ = [
        ('dwCommittedSize', DWORD),
        ('dwUnCommittedSize', DWORD),
        ('lpFirstBlock', LPVOID),
        ('lpLastBlock', LPVOID),
    ]

    DUMMYUNIONNAME.Region = Region
    DUMMYUNIONNAME._fields_ = [
        ('Block', DUMMYUNIONNAME.Block),
        ('Region', DUMMYUNIONNAME.Region),
    ]

    _PROCESS_HEAP_ENTRY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_HEAP_ENTRY._fields_ = [
        ('lpData', PVOID),
        ('cbData', DWORD),
        ('cbOverhead', BYTE),
        ('iRegionIndex', BYTE),
        ('wFlags', WORD),
        ('DUMMYUNIONNAME', _PROCESS_HEAP_ENTRY.DUMMYUNIONNAME),
    ]

    PROCESS_HEAP_ENTRY = _PROCESS_HEAP_ENTRY
    LPPROCESS_HEAP_ENTRY = POINTER(_PROCESS_HEAP_ENTRY)
    PPROCESS_HEAP_ENTRY = POINTER(_PROCESS_HEAP_ENTRY)

    PROCESS_HEAP_REGION = 0x0001
    PROCESS_HEAP_UNCOMMITTED_RANGE = 0x0002
    PROCESS_HEAP_ENTRY_BUSY = 0x0004
    PROCESS_HEAP_SEG_ALLOC = 0x0008
    PROCESS_HEAP_ENTRY_MOVEABLE = 0x0010
    PROCESS_HEAP_ENTRY_DDESHARE = 0x0020


    class _REASON_CONTEXT(ctypes.Structure):
        pass


    class Detailed(ctypes.Structure):
        pass


    class Reason(ctypes.Union):
        pass

    Detailed._fields_ = [
        ('LocalizedReasonModule', HMODULE),
        ('LocalizedReasonId', ULONG),
        ('ReasonStringCount', ULONG),
        ('ReasonStrings', POINTER(LPWSTR)),
    ]

    Reason.Detailed = Detailed

    Reason._fields_ = [
        ('Detailed', Reason.Detailed),
        ('SimpleReasonString', LPWSTR),
    ]

    _REASON_CONTEXT.Reason = Reason
    _REASON_CONTEXT._fields_ = [
        ('Version', ULONG),
        ('Flags', DWORD),
        ('Reason', _REASON_CONTEXT.Reason),
    ]

    REASON_CONTEXT = _REASON_CONTEXT
    PREASON_CONTEXT = POINTER(_REASON_CONTEXT)

    EXCEPTION_DEBUG_EVENT = 1
    CREATE_THREAD_DEBUG_EVENT = 2
    CREATE_PROCESS_DEBUG_EVENT = 3
    EXIT_THREAD_DEBUG_EVENT = 4
    EXIT_PROCESS_DEBUG_EVENT = 5
    LOAD_DLL_DEBUG_EVENT = 6
    UNLOAD_DLL_DEBUG_EVENT = 7
    OUTPUT_DEBUG_STRING_EVENT = 8
    RIP_EVENT = 9

    PTHREAD_START_ROUTINE = WINAPI(DWORD, LPVOID)
    LPTHREAD_START_ROUTINE = PTHREAD_START_ROUTINE
    PENCLAVE_ROUTINE = WINAPI(LPVOID, LPVOID)


    class _EXCEPTION_DEBUG_INFO(ctypes.Structure):
        pass

    _EXCEPTION_DEBUG_INFO._fields_ = [
        ('ExceptionRecord', EXCEPTION_RECORD),
        ('dwFirstChance', DWORD),
    ]

    EXCEPTION_DEBUG_INFO = _EXCEPTION_DEBUG_INFO
    LPEXCEPTION_DEBUG_INFO = POINTER(_EXCEPTION_DEBUG_INFO)


    class _CREATE_THREAD_DEBUG_INFO(ctypes.Structure):
        pass


    _CREATE_THREAD_DEBUG_INFO._fields_ = [
        ('hThread', HANDLE),
        ('lpThreadLocalBase', LPVOID),
        ('lpStartAddress', LPTHREAD_START_ROUTINE),
    ]

    CREATE_THREAD_DEBUG_INFO = _CREATE_THREAD_DEBUG_INFO
    LPCREATE_THREAD_DEBUG_INFO = POINTER(_CREATE_THREAD_DEBUG_INFO)


    class _CREATE_PROCESS_DEBUG_INFO(ctypes.Structure):
        pass


    _CREATE_PROCESS_DEBUG_INFO._fields_ = [
        ('hFile', HANDLE),
        ('hProcess', HANDLE),
        ('hThread', HANDLE),
        ('lpBaseOfImage', LPVOID),
        ('dwDebugInfoFileOffset', DWORD),
        ('nDebugInfoSize', DWORD),
        ('lpThreadLocalBase', LPVOID),
        ('lpStartAddress', LPTHREAD_START_ROUTINE),
        ('lpImageName', LPVOID),
        ('fUnicode', WORD),
    ]

    CREATE_PROCESS_DEBUG_INFO = _CREATE_PROCESS_DEBUG_INFO
    LPCREATE_PROCESS_DEBUG_INFO = POINTER(_CREATE_PROCESS_DEBUG_INFO)


    class _EXIT_THREAD_DEBUG_INFO(ctypes.Structure):
        pass
    _EXIT_THREAD_DEBUG_INFO._fields_ = [
        ('dwExitCode', DWORD),
    ]

    EXIT_THREAD_DEBUG_INFO = _EXIT_THREAD_DEBUG_INFO
    LPEXIT_THREAD_DEBUG_INFO = POINTER(_EXIT_THREAD_DEBUG_INFO)


    class _EXIT_PROCESS_DEBUG_INFO(ctypes.Structure):
        pass
    _EXIT_PROCESS_DEBUG_INFO._fields_ = [
        ('dwExitCode', DWORD),
    ]

    EXIT_PROCESS_DEBUG_INFO = _EXIT_PROCESS_DEBUG_INFO
    LPEXIT_PROCESS_DEBUG_INFO = POINTER(_EXIT_PROCESS_DEBUG_INFO)


    class _LOAD_DLL_DEBUG_INFO(ctypes.Structure):
        pass


    _LOAD_DLL_DEBUG_INFO._fields_ = [
        ('hFile', HANDLE),
        ('lpBaseOfDll', LPVOID),
        ('dwDebugInfoFileOffset', DWORD),
        ('nDebugInfoSize', DWORD),
        ('lpImageName', LPVOID),
        ('fUnicode', WORD),
    ]

    LOAD_DLL_DEBUG_INFO = _LOAD_DLL_DEBUG_INFO
    LPLOAD_DLL_DEBUG_INFO = POINTER(_LOAD_DLL_DEBUG_INFO)


    class _UNLOAD_DLL_DEBUG_INFO(ctypes.Structure):
        pass
    _UNLOAD_DLL_DEBUG_INFO._fields_ = [
        ('lpBaseOfDll', LPVOID),
    ]

    UNLOAD_DLL_DEBUG_INFO = _UNLOAD_DLL_DEBUG_INFO
    LPUNLOAD_DLL_DEBUG_INFO = POINTER(_UNLOAD_DLL_DEBUG_INFO)


    class _OUTPUT_DEBUG_STRING_INFO(ctypes.Structure):
        pass


    _OUTPUT_DEBUG_STRING_INFO._fields_ = [
        ('lpDebugStringData', LPSTR),
        ('fUnicode', WORD),
        ('nDebugStringLength', WORD),
    ]

    OUTPUT_DEBUG_STRING_INFO = _OUTPUT_DEBUG_STRING_INFO
    LPOUTPUT_DEBUG_STRING_INFO = POINTER(_OUTPUT_DEBUG_STRING_INFO)


    class _RIP_INFO(ctypes.Structure):
        pass


    _RIP_INFO._fields_ = [
        ('dwError', DWORD),
        ('dwType', DWORD),
    ]

    RIP_INFO = _RIP_INFO
    LPRIP_INFO = POINTER(_RIP_INFO)


    class _DEBUG_EVENT(ctypes.Structure):
        pass


    class u(ctypes.Union):
        pass


    u._fields_ = [
        ('Exception', EXCEPTION_DEBUG_INFO),
        ('CreateThread', CREATE_THREAD_DEBUG_INFO),
        ('CreateProcessInfo', CREATE_PROCESS_DEBUG_INFO),
        ('ExitThread', EXIT_THREAD_DEBUG_INFO),
        ('ExitProcess', EXIT_PROCESS_DEBUG_INFO),
        ('LoadDll', LOAD_DLL_DEBUG_INFO),
        ('UnloadDll', UNLOAD_DLL_DEBUG_INFO),
        ('DebugString', OUTPUT_DEBUG_STRING_INFO),
        ('RipInfo', RIP_INFO),
    ]

    _DEBUG_EVENT.u = u

    _DEBUG_EVENT._fields_ = [
        ('dwDebugEventCode', DWORD),
        ('dwProcessId', DWORD),
        ('dwThreadId', DWORD),
        ('u', _DEBUG_EVENT.u),
    ]

    DEBUG_EVENT = _DEBUG_EVENT
    LPDEBUG_EVENT = POINTER(_DEBUG_EVENT)

    if not defined(MIDL_PASS):
        pass
    # END IF   not defined(MIDL_PASS)

    from shared.ntstatus_h import *

    STILL_ACTIVE = STATUS_PENDING
    EXCEPTION_ACCESS_VIOLATION = STATUS_ACCESS_VIOLATION
    EXCEPTION_DATATYPE_MISALIGNMENT = STATUS_DATATYPE_MISALIGNMENT
    EXCEPTION_BREAKPOINT = STATUS_BREAKPOINT
    EXCEPTION_SINGLE_STEP = STATUS_SINGLE_STEP
    EXCEPTION_ARRAY_BOUNDS_EXCEEDED = STATUS_ARRAY_BOUNDS_EXCEEDED
    EXCEPTION_FLT_DENORMAL_OPERAND = STATUS_FLOAT_DENORMAL_OPERAND
    EXCEPTION_FLT_DIVIDE_BY_ZERO = STATUS_FLOAT_DIVIDE_BY_ZERO
    EXCEPTION_FLT_INEXACT_RESULT = STATUS_FLOAT_INEXACT_RESULT
    EXCEPTION_FLT_INVALID_OPERATION = STATUS_FLOAT_INVALID_OPERATION
    EXCEPTION_FLT_OVERFLOW = STATUS_FLOAT_OVERFLOW
    EXCEPTION_FLT_STACK_CHECK = STATUS_FLOAT_STACK_CHECK
    EXCEPTION_FLT_UNDERFLOW = STATUS_FLOAT_UNDERFLOW
    EXCEPTION_INT_DIVIDE_BY_ZERO = STATUS_INTEGER_DIVIDE_BY_ZERO
    EXCEPTION_INT_OVERFLOW = STATUS_INTEGER_OVERFLOW
    EXCEPTION_PRIV_INSTRUCTION = STATUS_PRIVILEGED_INSTRUCTION
    EXCEPTION_IN_PAGE_ERROR = STATUS_IN_PAGE_ERROR
    EXCEPTION_ILLEGAL_INSTRUCTION = STATUS_ILLEGAL_INSTRUCTION
    EXCEPTION_NONCONTINUABLE_EXCEPTION = STATUS_NONCONTINUABLE_EXCEPTION
    EXCEPTION_STACK_OVERFLOW = STATUS_STACK_OVERFLOW
    EXCEPTION_INVALID_DISPOSITION = STATUS_INVALID_DISPOSITION
    EXCEPTION_GUARD_PAGE = STATUS_GUARD_PAGE_VIOLATION
    EXCEPTION_INVALID_HANDLE = STATUS_INVALID_HANDLE
    EXCEPTION_POSSIBLE_DEADLOCK = STATUS_POSSIBLE_DEADLOCK
    CONTROL_C_EXIT = STATUS_CONTROL_C_EXIT
    LMEM_FIXED = 0x0000
    LMEM_MOVEABLE = 0x0002
    LMEM_NOCOMPACT = 0x0010
    LMEM_NODISCARD = 0x0020
    LMEM_ZEROINIT = 0x0040
    LMEM_MODIFY = 0x0080
    LMEM_DISCARDABLE = 0x0F00
    LMEM_VALID_FLAGS = 0x0F72
    LMEM_INVALID_HANDLE = 0x8000
    LHND = LMEM_MOVEABLE | LMEM_ZEROINIT
    LPTR = LMEM_FIXED | LMEM_ZEROINIT
    NONZEROLHND = LMEM_MOVEABLE
    NONZEROLPTR = LMEM_FIXED


    def LocalDiscard(h):
        return LocalReAlloc( h, 0, LMEM_MOVEABLE)

    LMEM_DISCARDED = 0x4000
    LMEM_LOCKCOUNT = 0x00FF
    NUMA_NO_PREFERRED_NODE = - 1

    if defined(__cplusplus):
        pass
    # END IF
    if _MSC_VER >= 1200:
        pass
    else:
        pass
    # END IF
    if _MSC_VER >= 800:
        pass
    # END IF
# END IF   _MINWINBASE_
