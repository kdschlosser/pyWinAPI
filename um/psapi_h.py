import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_PSAPI_H_ = None
PSAPI_VERSION = None

class _MODULEINFO(ctypes.Structure):
    pass


MODULEINFO = _MODULEINFO
LPMODULEINFO = POINTER(_MODULEINFO)


class _PSAPI_WORKING_SET_BLOCK(ctypes.Union):
    pass


PSAPI_WORKING_SET_BLOCK = _PSAPI_WORKING_SET_BLOCK
PPSAPI_WORKING_SET_BLOCK = POINTER(_PSAPI_WORKING_SET_BLOCK)


class _PSAPI_WORKING_SET_INFORMATION(ctypes.Structure):
    pass


PSAPI_WORKING_SET_INFORMATION = _PSAPI_WORKING_SET_INFORMATION
PPSAPI_WORKING_SET_INFORMATION = POINTER(_PSAPI_WORKING_SET_INFORMATION)


class _PSAPI_WORKING_SET_EX_BLOCK(ctypes.Union):
    pass


PSAPI_WORKING_SET_EX_BLOCK = _PSAPI_WORKING_SET_EX_BLOCK
PPSAPI_WORKING_SET_EX_BLOCK = POINTER(_PSAPI_WORKING_SET_EX_BLOCK)


class _PSAPI_WORKING_SET_EX_INFORMATION(ctypes.Structure):
    pass


PSAPI_WORKING_SET_EX_INFORMATION = _PSAPI_WORKING_SET_EX_INFORMATION
PPSAPI_WORKING_SET_EX_INFORMATION = POINTER(_PSAPI_WORKING_SET_EX_INFORMATION)


class _PSAPI_WS_WATCH_INFORMATION(ctypes.Structure):
    pass


PSAPI_WS_WATCH_INFORMATION = _PSAPI_WS_WATCH_INFORMATION
PPSAPI_WS_WATCH_INFORMATION = POINTER(_PSAPI_WS_WATCH_INFORMATION)


class _PSAPI_WS_WATCH_INFORMATION_EX(ctypes.Structure):
    pass


PSAPI_WS_WATCH_INFORMATION_EX = _PSAPI_WS_WATCH_INFORMATION_EX
PPSAPI_WS_WATCH_INFORMATION_EX = POINTER(_PSAPI_WS_WATCH_INFORMATION_EX)


class _PROCESS_MEMORY_COUNTERS(ctypes.Structure):
    pass


PROCESS_MEMORY_COUNTERS = _PROCESS_MEMORY_COUNTERS


class _PROCESS_MEMORY_COUNTERS_EX(ctypes.Structure):
    pass


PROCESS_MEMORY_COUNTERS_EX = _PROCESS_MEMORY_COUNTERS_EX


class _PERFORMANCE_INFORMATION(ctypes.Structure):
    pass


PERFORMANCE_INFORMATION = _PERFORMANCE_INFORMATION
PPERFORMANCE_INFORMATION = POINTER(_PERFORMANCE_INFORMATION)
PERFORMACE_INFORMATION = _PERFORMANCE_INFORMATION
PPERFORMACE_INFORMATION = POINTER(_PERFORMANCE_INFORMATION)


class _ENUM_PAGE_FILE_INFORMATION(ctypes.Structure):
    pass


ENUM_PAGE_FILE_INFORMATION = _ENUM_PAGE_FILE_INFORMATION
PENUM_PAGE_FILE_INFORMATION = POINTER(_ENUM_PAGE_FILE_INFORMATION)


# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) 1994-1999 Microsoft Corporation Module Name: psapi.h Abstract:
# Include file for APIs provided by PSAPI.DLL Author: Richard Shupak
# [richards] 06-Jan-1994 Revision History: --
if not defined(_PSAPI_H_):
    _PSAPI_H_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    psapi = ctypes.windll.PSAPI

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if _MSC_VER >= 1200:
            # #pragma warning(push)
            # #pragma warning(disable:4820) // padding added after data member
            pass
        # END IF

        LIST_MODULES_DEFAULT = 0x0 # This is the default one app would get
        # without any flag.
        LIST_MODULES_32BIT = 0x01 # list 32bit modules in the target process.
        LIST_MODULES_64BIT = 0x02 # list all 64bit modules. 32bit exe will be
        # stripped off.

        # list all the modules
        LIST_MODULES_ALL = (LIST_MODULES_32BIT | LIST_MODULES_64BIT)

        # Give teams a choice of using a downlevel version of psapi.h for an
        # OS versions.
        # Teams can set C_DEFINES=$(C_DEFINES) -DPSAPI_VERSION=1 for
        # downlevel psapi
        # on windows 7 and higher.  We found that test code needs this
        # capability.

        if not defined(PSAPI_VERSION):
            if (NTDDI_VERSION >= NTDDI_WIN7):
                PSAPI_VERSION = 2
            else:
                PSAPI_VERSION = 1
            # END IF
        # END IF

        if (PSAPI_VERSION > 1):
            # #define EnumProcessModules          K32EnumProcessModules
            # #define EnumProcessModulesEx        K32EnumProcessModulesEx
            # #define GetModuleBaseNameA          K32GetModuleBaseNameA
            # #define GetModuleBaseNameW          K32GetModuleBaseNameW
            # #define GetModuleFileNameExA        K32GetModuleFileNameExA
            # #define GetModuleFileNameExW        K32GetModuleFileNameExW
            # #define EmptyWorkingSet             K32EmptyWorkingSet
            # #define QueryWorkingSet             K32QueryWorkingSet
            # #define QueryWorkingSetEx           K32QueryWorkingSetEx
            ##define InitializeProcessForWsWatch K32InitializeProcessForWsWatch
            # #define GetWsChanges                K32GetWsChanges
            # #define GetWsChangesEx              K32GetWsChangesEx
            # #define GetMappedFileNameW          K32GetMappedFileNameW
            # #define GetMappedFileNameA          K32GetMappedFileNameA
            # #define EnumDeviceDrivers           K32EnumDeviceDrivers
            # #define GetDeviceDriverBaseNameA    K32GetDeviceDriverBaseNameA
            # #define GetDeviceDriverBaseNameW    K32GetDeviceDriverBaseNameW
            # #define GetDeviceDriverFileNameA    K32GetDeviceDriverFileNameA
            # #define GetDeviceDriverFileNameW    K32GetDeviceDriverFileNameW
            # #define GetPerformanceInfo          K32GetPerformanceInfo
            # #define EnumPageFilesW              K32EnumPageFilesW
            # #define EnumPageFilesA              K32EnumPageFilesA
            # #define GetProcessImageFileNameA    K32GetProcessImageFileNameA
            # #define GetProcessImageFileNameW    K32GetProcessImageFileNameW
            pass
        # END IF

    # END IF WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(PSAPI_VERSION):
            if (NTDDI_VERSION >= NTDDI_WIN7):
                PSAPI_VERSION = 2
            else:
                PSAPI_VERSION = 1
            # END IF
        # END IF

        if (PSAPI_VERSION > 1):
            # #define EnumProcesses               K32EnumProcesses
            # #define GetProcessMemoryInfo        K32GetProcessMemoryInfo
            # #define GetModuleInformation        K32GetModuleInformation
            # #define GetModuleBaseNameA          K32GetModuleBaseNameA
            # #define GetModuleBaseNameW          K32GetModuleBaseNameW
            # #define GetModuleFileNameExA        K32GetModuleFileNameExA
            # #define GetModuleFileNameExW        K32GetModuleFileNameExW
            pass
        # END IF

        # BOOL
        # WINAPI
        # EnumProcesses(
        # _Out_writes_bytes_(cb) DWORD* lpidProcess,
        # _In_ DWORD cb,
        # _Out_ LPDWORD lpcbNeeded
        # );
        EnumProcesses = psapi.EnumProcesses
        EnumProcesses.restype = BOOL
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # BOOL
        # WINAPI
        # EnumProcessModules(
        # _In_ HANDLE hProcess,
        # _Out_writes_bytes_(cb) HMODULE* lphModule,
        # _In_ DWORD cb,
        # _Out_ LPDWORD lpcbNeeded
        # );
        EnumProcessModules = psapi.EnumProcessModules
        EnumProcessModules.restype = BOOL

        # BOOL
        # WINAPI
        # EnumProcessModulesEx(
        # _In_ HANDLE hProcess,
        # _Out_writes_bytes_(cb) HMODULE* lphModule,
        # _In_ DWORD cb,
        # _Out_ LPDWORD lpcbNeeded,
        # _In_ DWORD dwFilterFlag
        # );
        EnumProcessModulesEx = psapi.EnumProcessModulesEx
        EnumProcessModulesEx.restype = BOOL

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # DWORD
        # WINAPI
        # GetModuleBaseNameA(
        # _In_ HANDLE hProcess,
        # _In_opt_ HMODULE hModule,
        # _Out_writes_(nSize) LPSTR lpBaseName,
        # _In_ DWORD nSize
        # );
        GetModuleBaseNameA = psapi.GetModuleBaseNameA
        GetModuleBaseNameA.restype = DWORD

        # DWORD
        # WINAPI
        # GetModuleBaseNameW(
        # _In_ HANDLE hProcess,
        # _In_opt_ HMODULE hModule,
        # _Out_writes_(nSize) LPWSTR lpBaseName,
        # _In_ DWORD nSize
        # );
        GetModuleBaseNameW = psapi.GetModuleBaseNameW
        GetModuleBaseNameW.restype = DWORD

        if defined(UNICODE):
            GetModuleBaseName = GetModuleBaseNameW
        else:
            GetModuleBaseName = GetModuleBaseNameA
        # END IF   not UNICODE

        # _Success_(return != 0)
        # _Ret_range_(1, nSize)
        # DWORD
        # WINAPI
        # GetModuleFileNameExA(
        # _In_opt_ HANDLE hProcess,
        # _In_opt_ HMODULE hModule,
        # _When_(return < nSize, _Out_writes_to_(nSize, return + 1))
        # _When_(return == nSize, _Out_writes_all_(nSize))
        # LPSTR lpFilename,
        # _In_ DWORD nSize
        # );
        GetModuleFileNameExA = psapi.GetModuleFileNameExA
        GetModuleFileNameExA.restype = DWORD

        # _Success_(return != 0)
        # _Ret_range_(1, nSize)
        # DWORD
        # WINAPI
        # GetModuleFileNameExW(
        # _In_opt_ HANDLE hProcess,
        # _In_opt_ HMODULE hModule,
        # _When_(return < nSize, _Out_writes_to_(nSize, return + 1))
        # _When_(return == nSize, _Out_writes_all_(nSize))
        # LPWSTR lpFilename,
        # _In_ DWORD nSize
        # );
        GetModuleFileNameExW = psapi.GetModuleFileNameExW
        GetModuleFileNameExW.restype = DWORD

        if defined(UNICODE):
            GetModuleFileNameEx = GetModuleFileNameExW
        else:
            GetModuleFileNameEx = GetModuleFileNameExA
        # END IF   not UNICODE

        _MODULEINFO._fields_ = [
            ('lpBaseOfDll', LPVOID),
            ('SizeOfImage', DWORD),
            ('EntryPoint', LPVOID),
        ]

        # BOOL
        # WINAPI
        # GetModuleInformation(
        # _In_ HANDLE hProcess,
        # _In_ HMODULE hModule,
        # _Out_ LPMODULEINFO lpmodinfo,
        # _In_ DWORD cb
        # );
        GetModuleInformation = psapi.GetModuleInformation
        GetModuleInformation.restype = BOOL

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # BOOL
        # WINAPI
        # EmptyWorkingSet(
        # _In_ HANDLE hProcess
        # );
        EmptyWorkingSet = psapi.EmptyWorkingSet
        EmptyWorkingSet.restype = BOOL

        # Working set information structures. All non-specified bits are
        # reserved.
        if _MSC_VER >= 1200:
            pass
        # END IF


        class _Struct_1(ctypes.Structure):
            pass

        _TEMP__Struct_1 = [
            ('Protection', ULONG_PTR, 5),
            ('ShareCount', ULONG_PTR, 3),
            ('Shared', ULONG_PTR, 1),
            ('Reserved', ULONG_PTR, 3),
        ]
        if defined(_WIN64):
            _TEMP__Struct_1 += [
                ('VirtualPage', ULONG_PTR, 52),
            ]
        else:
            _TEMP__Struct_1 += [
                ('VirtualPage', ULONG_PTR, 20),
            ]
        # END IF

        _Struct_1._fields_ = _TEMP__Struct_1
        _PSAPI_WORKING_SET_BLOCK._Struct_1 = _Struct_1

        _PSAPI_WORKING_SET_BLOCK._anonymous_ = (
            '_Struct_1',
        )

        _PSAPI_WORKING_SET_BLOCK._fields_ = [
            ('Flags', ULONG_PTR),
            ('_Struct_1', _PSAPI_WORKING_SET_BLOCK._Struct_1),
        ]

        _PSAPI_WORKING_SET_INFORMATION._fields_ = [
            ('NumberOfEntries', ULONG_PTR),
            ('WorkingSetInfo', PSAPI_WORKING_SET_BLOCK * 1),
        ]


        class _Union_1(ctypes.Union):
            pass


        class _Struct_2(ctypes.Structure):
            pass

        _TEMP__Struct_2 = [
            ('Valid', ULONG_PTR, 1),
            ('ShareCount', ULONG_PTR, 3),
            ('Win32Protection', ULONG_PTR, 11),
            ('Shared', ULONG_PTR, 1),
            ('Node', ULONG_PTR, 6),
            ('Locked', ULONG_PTR, 1),
            ('LargePage', ULONG_PTR, 1),
            ('Reserved', ULONG_PTR, 7),
            ('Bad', ULONG_PTR, 1),
        ]
        if defined(_WIN64):
            _TEMP__Struct_2 += [
                ('ReservedUlong', ULONG_PTR, 32),
            ]
        # END IF

        _Struct_2._fields_ = _TEMP__Struct_2
        _Union_1._Struct_2 = _Struct_2

        # Valid = 0 in this format.
        class Invalid(ctypes.Structure):
            pass

        _TEMP_Invalid = [
            ('Valid', ULONG_PTR, 1),
            ('Reserved0', ULONG_PTR, 14),
            ('Shared', ULONG_PTR, 1),
            ('Reserved1', ULONG_PTR, 15),
            ('Bad', ULONG_PTR, 1),
        ]
        if defined(_WIN64):
            _TEMP_Invalid += [
                ('ReservedUlong', ULONG_PTR, 32),
            ]
        # END IF

        Invalid._fields_ = _TEMP_Invalid
        _Union_1.Invalid = Invalid

        _Union_1._anonymous_ = (
            '_Struct_2',
        )

        _Union_1._fields_ = [
            ('_Struct_2', _Union_1._Struct_2),
            ('Invalid', _Union_1.Invalid),
        ]
        _PSAPI_WORKING_SET_EX_BLOCK._Union_1 = _Union_1

        _PSAPI_WORKING_SET_EX_BLOCK._anonymous_ = (
            '_Union_1',
        )

        _PSAPI_WORKING_SET_EX_BLOCK._fields_ = [
            ('Flags', ULONG_PTR),
            ('_Union_1', _PSAPI_WORKING_SET_EX_BLOCK._Union_1),
        ]

        _PSAPI_WORKING_SET_EX_INFORMATION._fields_ = [
            ('VirtualAddress', PVOID),
            ('VirtualAttributes', PSAPI_WORKING_SET_EX_BLOCK),
        ]
        if _MSC_VER >= 1200:
            pass
        else:
            pass
        # END IF

        # BOOL
        # WINAPI
        # QueryWorkingSet(
        # _In_ HANDLE hProcess,
        # _Out_writes_bytes_(cb) PVOID pv,
        # _In_ DWORD cb
        # );
        QueryWorkingSet = psapi.QueryWorkingSet
        QueryWorkingSet.restype = BOOL

        # BOOL
        # WINAPI
        # QueryWorkingSetEx(
        # _In_ HANDLE hProcess,
        # _Out_writes_bytes_(cb) PVOID pv,
        # _In_ DWORD cb
        # );
        QueryWorkingSetEx = psapi.QueryWorkingSetEx
        QueryWorkingSetEx.restype = BOOL

        # BOOL
        # WINAPI
        # InitializeProcessForWsWatch(
        # _In_ HANDLE hProcess
        # );
        InitializeProcessForWsWatch = psapi.InitializeProcessForWsWatch
        InitializeProcessForWsWatch.restype = BOOL

        _PSAPI_WS_WATCH_INFORMATION._fields_ = [
            ('FaultingPc', LPVOID),
            ('FaultingVa', LPVOID),
        ]

        _PSAPI_WS_WATCH_INFORMATION_EX._fields_ = [
            ('BasicInfo', PSAPI_WS_WATCH_INFORMATION),
            ('FaultingThreadId', ULONG_PTR),
            # Reserved
            ('Flags', ULONG_PTR),
        ]

        # BOOL
        # WINAPI
        # GetWsChanges(
        # _In_ HANDLE hProcess,
        # _Out_writes_bytes_(cb) PPSAPI_WS_WATCH_INFORMATION lpWatchInfo,
        # _In_ DWORD cb
        # );
        GetWsChanges = psapi.GetWsChanges
        GetWsChanges.restype = BOOL

        # BOOL
        # WINAPI
        # GetWsChangesEx(
        # _In_ HANDLE hProcess,
        # _Out_writes_bytes_to_(*cb, *cb)
        # PPSAPI_WS_WATCH_INFORMATION_EX lpWatchInfoEx,
        # _Inout_ PDWORD cb
        # );
        GetWsChangesEx = psapi.GetWsChangesEx
        GetWsChangesEx.restype = BOOL

        # DWORD
        # WINAPI
        # GetMappedFileNameW(
        # _In_ HANDLE hProcess,
        # _In_ LPVOID lpv,
        # _Out_writes_(nSize) LPWSTR lpFilename,
        # _In_ DWORD nSize
        # );
        GetMappedFileNameW = psapi.GetMappedFileNameW
        GetMappedFileNameW.restype = DWORD

        # DWORD
        # WINAPI
        # GetMappedFileNameA(
        # _In_ HANDLE hProcess,
        # _In_ LPVOID lpv,
        # _Out_writes_(nSize) LPSTR lpFilename,
        # _In_ DWORD nSize
        # );
        GetMappedFileNameA = psapi.GetMappedFileNameA
        GetMappedFileNameA.restype = DWORD

        if defined(UNICODE):
            GetMappedFileName = GetMappedFileNameW
        else:
            GetMappedFileName = GetMappedFileNameA
        # END IF   not UNICODE

        # BOOL
        # WINAPI
        # EnumDeviceDrivers(
        # _Out_writes_bytes_(cb) LPVOID *lpImageBase,
        # _In_ DWORD cb,
        # _Out_ LPDWORD lpcbNeeded
        # );
        EnumDeviceDrivers = psapi.EnumDeviceDrivers
        EnumDeviceDrivers.restype = BOOL

        # DWORD
        # WINAPI
        # GetDeviceDriverBaseNameA(
        # _In_ LPVOID ImageBase,
        # _Out_writes_(nSize) LPSTR lpFilename,
        # _In_ DWORD nSize
        # );
        GetDeviceDriverBaseNameA = psapi.GetDeviceDriverBaseNameA
        GetDeviceDriverBaseNameA.restype = DWORD

        # DWORD
        # WINAPI
        # GetDeviceDriverBaseNameW(
        # _In_ LPVOID ImageBase,
        # _Out_writes_(nSize) LPWSTR lpBaseName,
        # _In_ DWORD nSize
        # );
        GetDeviceDriverBaseNameW = psapi.GetDeviceDriverBaseNameW
        GetDeviceDriverBaseNameW.restype = DWORD

        if defined(UNICODE):
            GetDeviceDriverBaseName = GetDeviceDriverBaseNameW
        else:
            GetDeviceDriverBaseName = GetDeviceDriverBaseNameA
        # END IF   not UNICODE

        # DWORD
        # WINAPI
        # GetDeviceDriverFileNameA(
        # _In_ LPVOID ImageBase,
        # _Out_writes_(nSize) LPSTR lpFilename,
        # _In_ DWORD nSize
        # );
        GetDeviceDriverFileNameA = psapi.GetDeviceDriverFileNameA
        GetDeviceDriverFileNameA.restype = DWORD

        # DWORD
        # WINAPI
        # GetDeviceDriverFileNameW(
        # _In_ LPVOID ImageBase,
        # _Out_writes_(nSize) LPWSTR lpFilename,
        # _In_ DWORD nSize
        # );
        GetDeviceDriverFileNameW = psapi.GetDeviceDriverFileNameW
        GetDeviceDriverFileNameW.restype = DWORD

        if defined(UNICODE):
            GetDeviceDriverFileName = GetDeviceDriverFileNameW
        else:
            GetDeviceDriverFileName = GetDeviceDriverFileNameA
        # END IF   not UNICODE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # Structure for GetProcessMemoryInfo()
        _PROCESS_MEMORY_COUNTERS._fields_ = [
            ('cb', DWORD),
            ('PageFaultCount', DWORD),
            ('PeakWorkingSetSize', SIZE_T),
            ('WorkingSetSize', SIZE_T),
            ('QuotaPeakPagedPoolUsage', SIZE_T),
            ('QuotaPagedPoolUsage', SIZE_T),
            ('QuotaPeakNonPagedPoolUsage', SIZE_T),
            ('QuotaNonPagedPoolUsage', SIZE_T),
            ('PagefileUsage', SIZE_T),
            ('PeakPagefileUsage', SIZE_T),
        ]
        PPROCESS_MEMORY_COUNTERS = POINTER(PROCESS_MEMORY_COUNTERS)
        if _WIN32_WINNT >= 0x0501:
            _PROCESS_MEMORY_COUNTERS_EX._fields_ = [
                ('cb', DWORD),
                ('PageFaultCount', DWORD),
                ('PeakWorkingSetSize', SIZE_T),
                ('WorkingSetSize', SIZE_T),
                ('QuotaPeakPagedPoolUsage', SIZE_T),
                ('QuotaPagedPoolUsage', SIZE_T),
                ('QuotaPeakNonPagedPoolUsage', SIZE_T),
                ('QuotaNonPagedPoolUsage', SIZE_T),
                ('PagefileUsage', SIZE_T),
                ('PeakPagefileUsage', SIZE_T),
                ('PrivateUsage', SIZE_T),
            ]
            PPROCESS_MEMORY_COUNTERS_EX = POINTER(PROCESS_MEMORY_COUNTERS_EX)
        # END IF

        # BOOL
        # WINAPI
        # GetProcessMemoryInfo(
        # HANDLE Process,
        # PPROCESS_MEMORY_COUNTERS ppsmemCounters,
        # DWORD cb
        # );
        GetProcessMemoryInfo = psapi.GetProcessMemoryInfo
        GetProcessMemoryInfo.restype = BOOL

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        _PERFORMANCE_INFORMATION._fields_ = [
            ('cb', DWORD),
            ('CommitTotal', SIZE_T),
            ('CommitLimit', SIZE_T),
            ('CommitPeak', SIZE_T),
            ('PhysicalTotal', SIZE_T),
            ('PhysicalAvailable', SIZE_T),
            ('SystemCache', SIZE_T),
            ('KernelTotal', SIZE_T),
            ('KernelPaged', SIZE_T),
            ('KernelNonpaged', SIZE_T),
            ('PageSize', SIZE_T),
            ('HandleCount', DWORD),
            ('ProcessCount', DWORD),
            ('ThreadCount', DWORD),
        ]

        # BOOL
        # WINAPI
        # GetPerformanceInfo(
        # PPERFORMANCE_INFORMATION pPerformanceInformation,
        # DWORD cb
        # );
        GetPerformanceInfo = psapi.GetPerformanceInfo
        GetPerformanceInfo.restype = BOOL

        _ENUM_PAGE_FILE_INFORMATION._fields_ = [
            ('cb', DWORD),
            ('Reserved', DWORD),
            ('TotalSize', SIZE_T),
            ('TotalInUse', SIZE_T),
            ('PeakUsage', SIZE_T),
        ]

        # typedef BOOL (__stdcall *PENUM_PAGE_FILE_CALLBACKW) (
        # LPVOID pContext,
        # PENUM_PAGE_FILE_INFORMATION pPageFileInfo,
        # LPCWSTR lpFilename
        # );
        PENUM_PAGE_FILE_CALLBACKW = CALLBACK(
            BOOL,
            LPVOID,
            PENUM_PAGE_FILE_INFORMATION,
            LPCWSTR,
        )

        # typedef BOOL (__stdcall *PENUM_PAGE_FILE_CALLBACKA) (
        # LPVOID pContext,
        #  PENUM_PAGE_FILE_INFORMATION pPageFileInfo,
        # LPCSTR lpFilename
        # );
        PENUM_PAGE_FILE_CALLBACKA = CALLBACK(
            BOOL,
            LPVOID,
            PENUM_PAGE_FILE_INFORMATION,
            LPCSTR,
        )

        # BOOL
        # WINAPI
        # EnumPageFilesW(
        # PENUM_PAGE_FILE_CALLBACKW pCallBackRoutine,
        # LPVOID pContext
        # );
        EnumPageFilesW = psapi.EnumPageFilesW
        EnumPageFilesW.restype = BOOL

        # BOOL
        # WINAPI
        # EnumPageFilesA(
        # PENUM_PAGE_FILE_CALLBACKA pCallBackRoutine,
        # LPVOID pContext
        # );
        EnumPageFilesA = psapi.EnumPageFilesA
        EnumPageFilesA.restype = BOOL

        if defined(UNICODE):
            PENUM_PAGE_FILE_CALLBACK = PENUM_PAGE_FILE_CALLBACKW
            EnumPageFiles = EnumPageFilesW
        else:
            PENUM_PAGE_FILE_CALLBACK = PENUM_PAGE_FILE_CALLBACKA
            EnumPageFiles = EnumPageFilesA
        # END IF   not UNICODE

        # DWORD
        # WINAPI
        # GetProcessImageFileNameA(
        # _In_ HANDLE hProcess,
        # _Out_writes_(nSize) LPSTR lpImageFileName,
        # _In_ DWORD nSize
        # );
        GetProcessImageFileNameA = psapi.GetProcessImageFileNameA
        GetProcessImageFileNameA.restype = DWORD

        # DWORD
        # WINAPI
        # GetProcessImageFileNameW(
        # _In_ HANDLE hProcess,
        # _Out_writes_(nSize) LPWSTR lpImageFileName,
        # _In_ DWORD nSize
        # );
        GetProcessImageFileNameW = psapi.GetProcessImageFileNameW
        GetProcessImageFileNameW.restype = DWORD

        if defined(UNICODE):
            GetProcessImageFileName = GetProcessImageFileNameW
        else:
            GetProcessImageFileName = GetProcessImageFileNameA
        # END IF   not UNICODE

        if _MSC_VER >= 1200:
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if defined(__cplusplus):
        pass
    # END IF

# END IF  _PSAPI_H_


