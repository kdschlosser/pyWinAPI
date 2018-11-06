
from __future__ import print_function, absolute_import

import ctypes

from code_converter.data_types import (
    ENUM,
    HRESULT,
    POINTER,
    BOOL,
    SIZE_T,
    DWORD,
    LONG,
    ULONGLONG,
    LPCWSTR,
    HANDLE,
    PVOID,
    ULONG,
    UINT64,
    NULL,
    INT,
    BYTE,
    LPVOID,
    HMODULE,
    REFIID,
    LCID,
    WCHAR,
    ULONG_PTR
)

from comtypes import (
    IUnknown,
    COMMETHOD,
    BSTR
)
from comtypes.automation import VARIANT

__REQUIRED_RPCNDR_H_VERSION__ = 0x00000007
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000000

CLR_BUILD_VERSION = 0x0000001F


from guiddef_h import EXTERN_GUID # NOQA


LIBID_mscoree = EXTERN_GUID(
    0x5477469E,
    0x83B1,
    0x11D2,
    0x8B,
    0x49,
    0x00,
    0xA0,
    0xC9,
    0xB7,
    0xC9,
    0xC4
)
CLSID_CorRuntimeHost = EXTERN_GUID(
    0xCB2F6723,
    0xAB3A,
    0x11D2,
    0x9C,
    0x40,
    0x00,
    0xC0,
    0x4F,
    0xA3,
    0x0A,
    0x3E
)
CLSID_TypeNameFactory = EXTERN_GUID(
    0xB81FF171,
    0x20F3,
    0x11D2,
    0x8D,
    0xCC,
    0x00,
    0xA0,
    0xC9,
    0xB0,
    0x05,
    0x25
)
CLSID_CLRRuntimeHost = EXTERN_GUID(
    0x90F1A06E,
    0x7712,
    0x4762,
    0x86,
    0xB5,
    0x7A,
    0x5E,
    0xBA,
    0x6B,
    0xDB,
    0x02
)
CLSID_ComCallUnmarshal = EXTERN_GUID(
    0x3F281000,
    0xE95A,
    0x11D2,
    0x88,
    0x6B,
    0x00,
    0xC0,
    0x4F,
    0x86,
    0x9F,
    0x04
)
CLSID_ComCallUnmarshalV4 = EXTERN_GUID(
    0x45FB4600,
    0xE6E8,
    0x4928,
    0xB2,
    0x5E,
    0x50,
    0x47,
    0x6F,
    0xF7,
    0x94,
    0x25
)
IID_IObjectHandle = EXTERN_GUID(
    0xC460E2B4,
    0xE199,
    0x412A,
    0x84,
    0x56,
    0x84,
    0xDC,
    0x3E,
    0x48,
    0x38,
    0xC3
)
IID_IManagedObject = EXTERN_GUID(
    0xC3FCC19E,
    0xA970,
    0x11D2,
    0x8B,
    0x5A,
    0x00,
    0xA0,
    0xC9,
    0xB7,
    0xC9,
    0xC4
)
IID_IApartmentCallback = EXTERN_GUID(
    0x178E5337,
    0x1528,
    0x4591,
    0xB1,
    0xC9,
    0x1C,
    0x6E,
    0x48,
    0x46,
    0x86,
    0xD8
)
IID_ICatalogServices = EXTERN_GUID(
    0x04C6BE1E,
    0x1DB1,
    0x4058,
    0xAB,
    0x7A,
    0x70,
    0x0C,
    0xCC,
    0xFB,
    0xF2,
    0x54
)
IID_ICorRuntimeHost = EXTERN_GUID(
    0xCB2F6722,
    0xAB3A,
    0x11D2,
    0x9C,
    0x40,
    0x00,
    0xC0,
    0x4F,
    0xA3,
    0x0A,
    0x3E
)
IID_ICorThreadpool = EXTERN_GUID(
    0x84680D3A,
    0xB2C1,
    0x46E8,
    0xAC,
    0xC2,
    0xDB,
    0xC0,
    0xA3,
    0x59,
    0x15,
    0x9A
)
IID_ICLRDebugManager = EXTERN_GUID(
    0xDCAEC6,
    0x2AC0,
    0x43A9,
    0xAC,
    0xF9,
    0x1E,
    0x36,
    0xC1,
    0x39,
    0xB1,
    0xD
)
IID_IHostMemoryNeededCallback = EXTERN_GUID(
    0x47EB8E57,
    0x0846,
    0x4546,
    0xAF,
    0x76,
    0x6F,
    0x42,
    0xFC,
    0xFC,
    0x26,
    0x49
)
IID_IHostMalloc = EXTERN_GUID(
    0x1831991C,
    0xCC53,
    0x4A31,
    0xB2,
    0x18,
    0x04,
    0xE9,
    0x10,
    0x44,
    0x64,
    0x79
)
IID_IHostMemoryManager = EXTERN_GUID(
    0x7BC698D1,
    0xF9E3,
    0x4460,
    0x9C,
    0xDE,
    0xD0,
    0x42,
    0x48,
    0xE9,
    0xFA,
    0x25
)
IID_ICLRTask = EXTERN_GUID(
    0x28E66A4A,
    0x9906,
    0x4225,
    0xB2,
    0x31,
    0x91,
    0x87,
    0xC3,
    0xEB,
    0x86,
    0x11
)
IID_ICLRTask2 = EXTERN_GUID(
    0x28E66A4A,
    0x9906,
    0x4225,
    0xB2,
    0x31,
    0x91,
    0x87,
    0xC3,
    0xEB,
    0x86,
    0x12
)
IID_IHostTask = EXTERN_GUID(
    0xC2275828,
    0xC4B1,
    0x4B55,
    0x82,
    0xC9,
    0x92,
    0x13,
    0x5F,
    0x74,
    0xDF,
    0x1A
)
IID_ICLRTaskManager = EXTERN_GUID(
    0x4862EFBE,
    0x3AE5,
    0x44F8,
    0x8F,
    0xEB,
    0x34,
    0x61,
    0x90,
    0xEE,
    0x8A,
    0x34
)
IID_IHostTaskManager = EXTERN_GUID(
    0x997FF24C,
    0x43B7,
    0x4352,
    0x86,
    0x67,
    0x0D,
    0xC0,
    0x4F,
    0xAF,
    0xD3,
    0x54
)
IID_IHostThreadpoolManager = EXTERN_GUID(
    0x983D50E2,
    0xCB15,
    0x466B,
    0x80,
    0xFC,
    0x84,
    0x5D,
    0xC6,
    0xE8,
    0xC5,
    0xFD
)
IID_ICLRIoCompletionManager = EXTERN_GUID(
    0x2D74CE86,
    0xB8D6,
    0x4C84,
    0xB3,
    0xA7,
    0x97,
    0x68,
    0x93,
    0x3B,
    0x3C,
    0x12
)
IID_IHostIoCompletionManager = EXTERN_GUID(
    0x8BDE9D80,
    0xEC06,
    0x41D6,
    0x83,
    0xE6,
    0x22,
    0x58,
    0x0E,
    0xFF,
    0xCC,
    0x20
)
IID_IHostSyncManager = EXTERN_GUID(
    0x234330C7,
    0x5F10,
    0x4F20,
    0x96,
    0x15,
    0x51,
    0x22,
    0xDA,
    0xB7,
    0xA0,
    0xAC
)
IID_IHostCrst = EXTERN_GUID(
    0x6DF710A6,
    0x26A4,
    0x4A65,
    0x8C,
    0xD5,
    0x72,
    0x37,
    0xB8,
    0xBD,
    0xA8,
    0xDC
)
IID_IHostAutoEvent = EXTERN_GUID(
    0x50B0CFCE,
    0x4063,
    0x4278,
    0x96,
    0x73,
    0xE5,
    0xCB,
    0x4E,
    0xD0,
    0xBD,
    0xB8
)
IID_IHostManualEvent = EXTERN_GUID(
    0x1BF4EC38,
    0xAFFE,
    0x4FB9,
    0x85,
    0xA6,
    0x52,
    0x52,
    0x68,
    0xF1,
    0x5B,
    0x54
)
IID_IHostSemaphore = EXTERN_GUID(
    0x855EFD47,
    0xCC09,
    0x463A,
    0xA9,
    0x7D,
    0x16,
    0xAC,
    0xAB,
    0x88,
    0x26,
    0x61
)
IID_ICLRSyncManager = EXTERN_GUID(
    0x55FF199D,
    0xAD21,
    0x48F9,
    0xA1,
    0x6C,
    0xF2,
    0x4E,
    0xBB,
    0xB8,
    0x72,
    0x7D
)
IID_ICLRAppDomainResourceMonitor = EXTERN_GUID(
    0xC62DE18C,
    0x2E23,
    0x4AEA,
    0x84,
    0x23,
    0xB4,
    0x0C,
    0x1F,
    0xC5,
    0x9E,
    0xAE
)
IID_ICLRPolicyManager = EXTERN_GUID(
    0x7D290010,
    0xD781,
    0x45DA,
    0xA6,
    0xF8,
    0xAA,
    0x5D,
    0x71,
    0x1A,
    0x73,
    0x0E
)
IID_ICLRGCManager = EXTERN_GUID(
    0x54D9007E,
    0xA8E2,
    0x4885,
    0xB7,
    0xBF,
    0xF9,
    0x98,
    0xDE,
    0xEE,
    0x4F,
    0x2A
)
IID_ICLRGCManager2 = EXTERN_GUID(
    0x0603B793,
    0xA97A,
    0x4712,
    0x9C,
    0xB4,
    0x0C,
    0xD1,
    0xC7,
    0x4C,
    0x0F,
    0x7C
)
IID_ICLRErrorReportingManager = EXTERN_GUID(
    0x980D2F1A,
    0xBF79,
    0x4C08,
    0x81,
    0x2A,
    0xBB,
    0x97,
    0x78,
    0x92,
    0x8F,
    0x78
)
IID_IHostPolicyManager = EXTERN_GUID(
    0x7AE49844,
    0xB1E3,
    0x4683,
    0xBA,
    0x7C,
    0x1E,
    0x82,
    0x12,
    0xEA,
    0x3B,
    0x79
)
IID_IHostGCManager = EXTERN_GUID(
    0x5D4EC34E,
    0xF248,
    0x457B,
    0xB6,
    0x03,
    0x25,
    0x5F,
    0xAA,
    0xBA,
    0x0D,
    0x21
)
IID_IActionOnCLREvent = EXTERN_GUID(
    0x607BE24B,
    0xD91B,
    0x4E28,
    0xA2,
    0x42,
    0x61,
    0x87,
    0x1C,
    0xE5,
    0x6E,
    0x35
)
IID_ICLROnEventManager = EXTERN_GUID(
    0x1D0E0132,
    0xE64F,
    0x493D,
    0x92,
    0x60,
    0x02,
    0x5C,
    0x0E,
    0x32,
    0xC1,
    0x75
)
IID_ICLRRuntimeHost = EXTERN_GUID(
    0x90F1A06C,
    0x7712,
    0x4762,
    0x86,
    0xB5,
    0x7A,
    0x5E,
    0xBA,
    0x6B,
    0xDB,
    0x02
)
IID_ICLRHostProtectionManager = EXTERN_GUID(
    0x89F25F5C,
    0xCEEF,
    0x43E1,
    0x9C,
    0xFA,
    0xA6,
    0x8C,
    0xE8,
    0x63,
    0xAA,
    0xAC
)
IID_IHostAssemblyStore = EXTERN_GUID(
    0x7B102A88,
    0x3F7F,
    0x496D,
    0x8F,
    0xA2,
    0xC3,
    0x53,
    0x74,
    0xE0,
    0x1A,
    0xF3
)
IID_IHostAssemblyManager = EXTERN_GUID(
    0x613DABD7,
    0x62B2,
    0x493E,
    0x9E,
    0x65,
    0xC1,
    0xE3,
    0x2A,
    0x1E,
    0x0C,
    0x5E
)
IID_IHostSecurityManager = EXTERN_GUID(
    0x75AD2468,
    0xA349,
    0x4D02,
    0xA7,
    0x64,
    0x76,
    0xA6,
    0x8A,
    0xEE,
    0x0C,
    0x4F
)
IID_IHostSecurityContext = EXTERN_GUID(
    0x7E573CE4,
    0x343,
    0x4423,
    0x98,
    0xD7,
    0x63,
    0x18,
    0x34,
    0x8A,
    0x1D,
    0x3C
)
IID_ICLRAssemblyIdentityManager = EXTERN_GUID(
    0x15F0A9DA,
    0x3FF6,
    0x4393,
    0x9D,
    0xA9,
    0xFD,
    0xFD,
    0x28,
    0x4E,
    0x69,
    0x72
)
IID_ICLRDomainManager = EXTERN_GUID(
    0x270D00A2,
    0x8E15,
    0x4D0B,
    0xAD,
    0xEB,
    0x37,
    0xBC,
    0x3E,
    0x47,
    0xDF,
    0x77
)
IID_ITypeName = EXTERN_GUID(
    0xB81FF171,
    0x20F3,
    0x11D2,
    0x8D,
    0xCC,
    0x00,
    0xA0,
    0xC9,
    0xB0,
    0x05,
    0x22
)
IID_ICLRAssemblyReferenceList = EXTERN_GUID(
    0x1B2C9750,
    0x2E66,
    0x4BDA,
    0x8B,
    0x44,
    0x0A,
    0x64,
    0x2C,
    0x5C,
    0xD7,
    0x33
)
IID_ICLRReferenceAssemblyEnum = EXTERN_GUID(
    0xD509CB5D,
    0xCF32,
    0x4876,
    0xAE,
    0x61,
    0x67,
    0x77,
    0x0C,
    0xF9,
    0x19,
    0x73
)
IID_ICLRProbingAssemblyEnum = EXTERN_GUID(
    0xD0C5FB1F,
    0x416B,
    0x4F97,
    0x81,
    0xF4,
    0x7A,
    0xC7,
    0xDC,
    0x24,
    0xDD,
    0x5D
)
IID_ICLRHostBindingPolicyManager = EXTERN_GUID(
    0x4B3545E7,
    0x1856,
    0x48C9,
    0xA8,
    0xBA,
    0x24,
    0xB2,
    0x1A,
    0x75,
    0x3C,
    0x09
)
IID_ITypeNameBuilder = EXTERN_GUID(
    0xB81FF171,
    0x20F3,
    0x11D2,
    0x8D,
    0xCC,
    0x00,
    0xA0,
    0xC9,
    0xB0,
    0x05,
    0x23
)
IID_ITypeNameFactory = EXTERN_GUID(
    0xB81FF171,
    0x20F3,
    0x11D2,
    0x8D,
    0xCC,
    0x00,
    0xA0,
    0xC9,
    0xB0,
    0x05,
    0x21
)


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0000_0001(ENUM):
    HOST_TYPE_DEFAULT = 0
    HOST_TYPE_APPLAUNCH = 0x1
    HOST_TYPE_CORFLAG = 0x2


HOST_TYPE = __MIDL___MIDL_itf_mscoree_0000_0000_0001


FExecuteInAppDomainCallback = ctypes.WINFUNCTYPE(HRESULT, NULL)


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0000_0002(ENUM):
    STARTUP_CONCURRENT_GC = 0x1
    STARTUP_LOADER_OPTIMIZATION_MASK = 0x3 << 1
    STARTUP_LOADER_OPTIMIZATION_SINGLE_DOMAIN = 0x1 << 1
    STARTUP_LOADER_OPTIMIZATION_MULTI_DOMAIN = 0x2 << 1
    STARTUP_LOADER_OPTIMIZATION_MULTI_DOMAIN_HOST = 0x3 << 1
    STARTUP_LOADER_SAFEMODE = 0x10
    STARTUP_LOADER_SETPREFERENCE = 0x100
    STARTUP_SERVER_GC = 0x1000
    STARTUP_HOARD_GC_VM = 0x2000
    STARTUP_SINGLE_VERSION_HOSTING_INTERFACE = 0x4000
    STARTUP_LEGACY_IMPERSONATION = 0x10000
    STARTUP_DISABLE_COMMITTHREADSTACK = 0x20000
    STARTUP_ALWAYSFLOW_IMPERSONATION = 0x40000
    STARTUP_TRIM_GC_COMMIT = 0x80000
    STARTUP_ETW = 0x100000
    STARTUP_ARM = 0x400000


STARTUP_FLAGS = __MIDL___MIDL_itf_mscoree_0000_0000_0002


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0000_0003(ENUM):
    CLSID_RESOLUTION_DEFAULT = 0
    CLSID_RESOLUTION_REGISTERED = 0x1


CLSID_RESOLUTION_FLAGS = __MIDL___MIDL_itf_mscoree_0000_0000_0003


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0000_0004(ENUM):
    RUNTIME_INFO_UPGRADE_VERSION = 0x1
    RUNTIME_INFO_REQUEST_IA64 = 0x2
    RUNTIME_INFO_REQUEST_AMD64 = 0x4
    RUNTIME_INFO_REQUEST_X86 = 0x8
    RUNTIME_INFO_DONT_RETURN_DIRECTORY = 0x10
    RUNTIME_INFO_DONT_RETURN_VERSION = 0x20
    RUNTIME_INFO_DONT_SHOW_ERROR_DIALOG = 0x40
    RUNTIME_INFO_IGNORE_ERROR_MODE = 0x1000


RUNTIME_INFO_FLAGS = __MIDL___MIDL_itf_mscoree_0000_0000_0004


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0000_0005(ENUM):
    APPDOMAIN_SECURITY_DEFAULT = 0
    APPDOMAIN_SECURITY_SANDBOXED = 0x1
    APPDOMAIN_SECURITY_FORBID_CROSSAD_REVERSE_PINVOKE = 0x2
    APPDOMAIN_FORCE_TRIVIAL_WAIT_OPERATIONS = 0x8


APPDOMAIN_SECURITY_FLAGS = __MIDL___MIDL_itf_mscoree_0000_0000_0005


class IObjectHandle(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IObjectHandle
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Unwrap',
            (['out', 'retval'], POINTER(VARIANT), 'ppv'),
        ),
    ]


class IAppDomainBinding(IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'OnAppDomain',
            (['in'], POINTER(IUnknown), 'pAppdomain'),
        ),
    ]


class IGCThreadControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SuspensionEnding',
            ([], DWORD, 'Generation'),
        ),
    ]


class IGCHostControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'RequestVirtualMemLimit',
            (['in'], SIZE_T, 'sztMaxVirtualMemMB'),
            (['in', 'out'], POINTER(SIZE_T), 'psztNewMaxVirtualMemMB'),
        ),
    ]


WAITORTIMERCALLBACK = ctypes.WINFUNCTYPE(NULL, PVOID, BOOL)
LPTHREAD_START_ROUTINE = ctypes.WINFUNCTYPE(DWORD, LPVOID)
LPOVERLAPPED_COMPLETION_ROUTINE = ctypes.WINFUNCTYPE(
    NULL,
    DWORD,
    DWORD,
    LPVOID
)
PTLS_CALLBACK_FUNCTION = ctypes.WINFUNCTYPE(NULL, PVOID)


class ICorThreadpool(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICorThreadpool
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'CorRegisterWaitForSingleObject',
            (['in'], POINTER(HANDLE), 'phNewWaitObject'),
            (['in'], HANDLE, 'hWaitObject'),
            (['in'], WAITORTIMERCALLBACK, 'Callback'),
            (['in'], PVOID, 'Context'),
            (['in'], ULONG, 'timeout'),
            (['in'], BOOL, 'executeOnlyOnce'),
            (['out'], POINTER(BOOL), 'result'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CorUnregisterWait',
            (['in'], HANDLE, 'hWaitObject'),
            (['in'], HANDLE, 'CompletionEvent'),
            (['out'], POINTER(BOOL), 'result'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CorQueueUserWorkItem',
            (['in'], LPTHREAD_START_ROUTINE, 'Function'),
            (['in'], PVOID, 'Context'),
            (['in'], BOOL, 'executeOnlyOnce'),
            (['out'], POINTER(BOOL), 'result'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CorCreateTimer',
            (['in'], POINTER(HANDLE), 'phNewTimer'),
            (['in'], WAITORTIMERCALLBACK, 'Callback'),
            (['in'], PVOID, 'Parameter'),
            (['in'], DWORD, 'DueTime'),
            (['in'], DWORD, 'Period'),
            (['out'], POINTER(BOOL), 'result'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CorChangeTimer',
            (['in'], HANDLE, 'Timer'),
            (['in'], ULONG, 'DueTime'),
            (['in'], ULONG, 'Period'),
            (['out'], POINTER(BOOL), 'result'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CorDeleteTimer',
            (['in'], HANDLE, 'Timer'),
            (['in'], HANDLE, 'CompletionEvent'),
            (['out'], POINTER(BOOL), 'result'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CorBindIoCompletionCallback',
            (['in'], HANDLE, 'fileHandle'),
            (['in'], LPOVERLAPPED_COMPLETION_ROUTINE, 'callback'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CorCallOrQueueUserWorkItem',
            (['in'], LPTHREAD_START_ROUTINE, 'Function'),
            (['in'], PVOID, 'Context'),
            (['out'], POINTER(BOOL), 'result'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CorSetMaxThreads',
            (['in'], DWORD, 'MaxWorkerThreads'),
            (['in'], DWORD, 'MaxIOCompletionThreads'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CorGetMaxThreads',
            (['out'], POINTER(DWORD), 'MaxWorkerThreads'),
            (['out'], POINTER(DWORD), 'MaxIOCompletionThreads'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CorGetAvailableThreads',
            (['out'], POINTER(DWORD), 'AvailableWorkerThreads'),
            (['out'], POINTER(DWORD), 'AvailableIOCompletionThreads'),
        ),
    ]


IID_IDebuggerThreadControl = EXTERN_GUID(
    0x23D86786,
    0x0BB5,
    0x4774,
    0x8F,
    0xB5,
    0xE3,
    0x52,
    0x2A,
    0xDD,
    0x62,
    0x46
)


class IDebuggerThreadControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebuggerThreadControl
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'StartBlockingForDebugger',
            ([], DWORD, 'dwUnused'),
        ),
    ]


IID_IDebuggerInfo = EXTERN_GUID(
    0xBF24142D,
    0xA47D,
    0x4D24,
    0xA6,
    0x6D,
    0x8C,
    0x21,
    0x41,
    0x94,
    0x4E,
    0x44
)


class IDebuggerInfo(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebuggerInfo
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'IsDebuggerAttached',
            (['out'], POINTER(BOOL), 'pbAttached'),
        ),
    ]


IID_ICorConfiguration = EXTERN_GUID(
    0x5C2B07A5,
    0x1E98,
    0x11D3,
    0x87,
    0x2F,
    0x00,
    0xC0,
    0x4F,
    0x79,
    0xED,
    0x0D
)


class ICorConfiguration(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICorConfiguration
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetGCThreadControl',
            (['in'], POINTER(IGCThreadControl), 'pGCThreadControl'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetGCHostControl',
            (['in'], POINTER(IGCHostControl), 'pGCHostControl'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetDebuggerThreadControl',
            (
                ['in'],
                POINTER(IDebuggerThreadControl),
                'pDebuggerThreadControl'
            ),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'AddDebuggerSpecialThread',
            (['in'], DWORD, 'dwSpecialThreadId'),
        ),
    ]


HDOMAINENUM = POINTER(NULL)


class ICorRuntimeHost(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICorRuntimeHost
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SwitchInLogicalThreadState',
            (['in'], POINTER(DWORD), 'pFiberCookie'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SwitchOutLogicalThreadState',
            (['out'], POINTER(POINTER(DWORD)), 'pFiberCookie'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'LocksHeldByLogicalThread',
            (['out'], POINTER(DWORD), 'pCount'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'MapFile',
            (['in'], HANDLE, 'hFile'),
            (['out'], POINTER(HMODULE), 'hMapAddress'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetConfiguration',
            (['out'], POINTER(POINTER(ICorConfiguration)), 'pConfiguration'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateDomain',
            (['in'], LPCWSTR, 'pwzFriendlyName'),
            (['in'], POINTER(IUnknown), 'pIdentityArray'),
            (['out'], POINTER(POINTER(IUnknown)), 'pAppDomain'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetDefaultDomain',
            (['out'], POINTER(POINTER(IUnknown)), 'pAppDomain'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'EnumDomains',
            (['out'], POINTER(HDOMAINENUM), 'hEnum'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'NextDomain',
            (['in'], HDOMAINENUM, 'hEnum'),
            (['out'], POINTER(POINTER(IUnknown)), 'pAppDomain'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CloseEnum',
            (['in'], HDOMAINENUM, 'hEnum'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateDomainEx',
            (['in'], LPCWSTR, 'pwzFriendlyName'),
            (['in'], POINTER(IUnknown), 'pSetup'),
            (['in'], POINTER(IUnknown), 'pEvidence'),
            (['out'], POINTER(POINTER(IUnknown)), 'pAppDomain'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateDomainSetup',
            (['out'], POINTER(POINTER(IUnknown)), 'pAppDomainSetup'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateEvidence',
            (['out'], POINTER(POINTER(IUnknown)), 'pEvidence'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'UnloadDomain',
            (['in'], POINTER(IUnknown), 'pAppDomain'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CurrentDomain',
            (['out'], POINTER(POINTER(IUnknown)), 'pAppDomain'),
        ),
    ]


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0009_0001(ENUM):
    eMemoryAvailableLow = 1
    eMemoryAvailableNeutral = 2
    eMemoryAvailableHigh = 3


EMemoryAvailable = __MIDL___MIDL_itf_mscoree_0000_0009_0001


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0009_0002(ENUM):
    eTaskCritical = 0
    eAppDomainCritical = 1
    eProcessCritical = 2


EMemoryCriticalLevel = __MIDL___MIDL_itf_mscoree_0000_0009_0002


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0009_0003(ENUM):
    WAIT_MSGPUMP = 0x1
    WAIT_ALERTABLE = 0x2
    WAIT_NOTINDEADLOCK = 0x4


WAIT_OPTION = __MIDL___MIDL_itf_mscoree_0000_0009_0003


IID_ICLRMemoryNotificationCallback = EXTERN_GUID(
    0x47EB8E57,
    0x0846,
    0x4546,
    0xAF,
    0x76,
    0x6F,
    0x42,
    0xFC,
    0xFC,
    0x26,
    0x49
)


class ICLRMemoryNotificationCallback(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostMemoryNeededCallback
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'OnMemoryNotification',
            (['in'], EMemoryAvailable, 'eMemoryAvailable'),
        ),
    ]


class IHostMalloc(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostMalloc
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Alloc',
            (['in'], SIZE_T, 'cbSize'),
            (['in'], EMemoryCriticalLevel, 'eCriticalLevel'),
            (['out'], POINTER(POINTER(NULL)), 'ppMem'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'DebugAlloc',
            (['in'], SIZE_T, 'cbSize'),
            (['in'], EMemoryCriticalLevel, 'eCriticalLevel'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Free',
            (['in'], POINTER(NULL), 'pMem'),
        ),
    ]


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0011_0001(ENUM):
    MALLOC_THREADSAFE = 0x1
    MALLOC_EXECUTABLE = 0x2


MALLOC_TYPE = __MIDL___MIDL_itf_mscoree_0000_0011_0001


class IHostMemoryManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostMemoryManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'CreateMalloc',
            (['in'], DWORD, 'dwMallocType'),
            (['out'], POINTER(POINTER(IHostMalloc)), 'ppMalloc'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'VirtualAlloc',
            (['in'], POINTER(NULL), 'pAddress'),
            (['in'], SIZE_T, 'dwSize'),
            (['in'], DWORD, 'flAllocationType'),
            (['in'], DWORD, 'flProtect'),
            (['in'], EMemoryCriticalLevel, 'eCriticalLevel'),
            (['out'], POINTER(POINTER(NULL)), 'ppMem'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'VirtualFree',
            (['in'], LPVOID, 'lpAddress'),
            (['in'], SIZE_T, 'dwSize'),
            (['in'], DWORD, 'dwFreeType'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'VirtualQuery',
            (['in'], POINTER(NULL), 'lpAddress'),
            (['out'], POINTER(NULL), 'lpBuffer'),
            (['in'], SIZE_T, 'dwLength'),
            (['out'], POINTER(SIZE_T), 'pResult'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'VirtualProtect',
            (['in'], POINTER(NULL), 'lpAddress'),
            (['in'], SIZE_T, 'dwSize'),
            (['in'], DWORD, 'flNewProtect'),
            (['out'], POINTER(DWORD), 'pflOldProtect'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMemoryLoad',
            (['out'], POINTER(DWORD), 'pMemoryLoad'),
            (['out'], POINTER(SIZE_T), 'pAvailableBytes'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'RegisterMemoryNotificationCallback',
            (['in'], POINTER(ICLRMemoryNotificationCallback), 'pCallback'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'NeedsVirtualAddressSpace',
            (['in'], LPVOID, 'startAddress'),
            (['in'], SIZE_T, 'size'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'AcquiredVirtualAddressSpace',
            (['in'], LPVOID, 'startAddress'),
            (['in'], SIZE_T, 'size'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'ReleasedVirtualAddressSpace',
            (['in'], LPVOID, 'startAddress'),
        ),
    ]


# noinspection PyPep8Naming
class _COR_GC_THREAD_STATS(ctypes.Structure):
    _fields_ = [
        ('PerThreadAllocation', ULONGLONG),
        ('Flags', ULONG),
    ]


COR_GC_THREAD_STATS = _COR_GC_THREAD_STATS

TASKID = UINT64
CONNID = DWORD


class ICLRTask(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRTask
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SwitchIn',
            (['in'], HANDLE, 'threadHandle'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMemStats',
            (['out'], POINTER(COR_GC_THREAD_STATS), 'memUsage'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Reset',
            ([], BOOL, 'fFull'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'NeedsPriorityScheduling',
            (['out'], POINTER(BOOL), 'pbNeedsPriorityScheduling'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'LocksHeld',
            (['out'], POINTER(SIZE_T), 'pLockCount'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetTaskIdentifier',
            (['in'], TASKID, 'asked'),
        ),
    ]


class ICLRTask2(ICLRTask):
    _case_insensitive_ = True
    _iid_ = IID_ICLRTask2
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'EndPreventAsyncAbort'
        ),
    ]


class IHostTask(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostTask
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Join',
            (['in'], DWORD, 'dwMilliseconds'),
            (['in'], DWORD, 'option'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetPriority',
            (['in'], INT, 'newPriority'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetPriority',
            (['out'], POINTER(INT), 'pPriority'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetCLRTask',
            (['in'], POINTER(ICLRTask), 'pCLRTask'),
        ),
    ]


class ETaskType(ENUM):
    TT_DEBUGGERHELPER = 0x1
    TT_GC = 0x2
    TT_FINALIZER = 0x4
    TT_THREADPOOL_TIMER = 0x8
    TT_THREADPOOL_GATE = 0x10
    TT_THREADPOOL_WORKER = 0x20
    TT_THREADPOOL_IOCOMPLETION = 0x40
    TT_ADUNLOAD = 0x80
    TT_USER = 0x100
    TT_THREADPOOL_WAIT = 0x200
    TT_UNKNOWN = 0x80000000


class ICLRTaskManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRTaskManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'CreateTask',
            (['out'], POINTER(POINTER(ICLRTask)), 'pTask'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetCurrentTask',
            (['out'], POINTER(POINTER(ICLRTask)), 'pTask'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetUILocale',
            (['in'], LCID, 'lcid'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetLocale',
            (['in'], LCID, 'lcid'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetCurrentTaskType',
            (['out'], POINTER(ETaskType), 'pTaskType'),
        ),
    ]


class IHostTaskManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostTaskManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetCurrentTask',
            (['out'], POINTER(POINTER(IHostTask)), 'pTask'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateTask',
            (['in'], DWORD, 'dwStackSize'),
            (['in'], LPTHREAD_START_ROUTINE, 'pStartAddress'),
            (['in'], PVOID, 'pParameter'),
            (['out'], POINTER(POINTER(IHostTask)), 'ppTask'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Sleep',
            (['in'], DWORD, 'dwMilliseconds'),
            (['in'], DWORD, 'option'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SwitchToTask',
            (['in'], DWORD, 'option'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetUILocale',
            (['in'], LCID, 'lcid'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetLocale',
            (['in'], LCID, 'lcid'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CallNeedsHostHook',
            (['in'], SIZE_T, 'target'),
            (['out'], POINTER(BOOL), 'pbCallNeedsHostHook'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'LeaveRuntime',
            (['in'], SIZE_T, 'target'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetStackGuarantee',
            (['in'], ULONG, 'guarantee'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetStackGuarantee',
            (['out'], POINTER(ULONG), 'pGuarantee'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetCLRTaskManager',
            (['in'], POINTER(ICLRTaskManager), 'ppManager'),
        ),
    ]


class IHostThreadpoolManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostThreadpoolManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'QueueUserWorkItem',
            (['in'], LPTHREAD_START_ROUTINE, 'Function'),
            (['in'], PVOID, 'Context'),
            (['in'], ULONG, 'Flags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetMaxThreads',
            (['in'], DWORD, 'dwMaxWorkerThreads'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMaxThreads',
            (['out'], POINTER(DWORD), 'pdwMaxWorkerThreads'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetAvailableThreads',
            (['out'], POINTER(DWORD), 'pdwAvailableWorkerThreads'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetMinThreads',
            (['in'], DWORD, 'dwMinIOCompletionThreads'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMinThreads',
            (['out'], POINTER(DWORD), 'pdwMinIOCompletionThreads'),
        ),
    ]


class ICLRIoCompletionManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRIoCompletionManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'OnComplete',
            (['in'], DWORD, 'dwErrorCode'),
            (['in'], DWORD, 'NumberOfBytesTransferred'),
            (['in'], POINTER(NULL), 'pvOverlapped'),
        ),
    ]


class IHostIoCompletionManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostIoCompletionManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'CreateIoCompletionPort',
            (['out'], POINTER(HANDLE), 'phPort'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CloseIoCompletionPort',
            (['in'], HANDLE, 'hPort'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetMaxThreads',
            (['in'], DWORD, 'dwMaxIOCompletionThreads'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMaxThreads',
            (['out'], POINTER(DWORD), 'pdwMaxIOCompletionThreads'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetAvailableThreads',
            (['out'], POINTER(DWORD), 'pdwAvailableIOCompletionThreads'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetHostOverlappedSize',
            (['out'], POINTER(DWORD), 'pcbSize'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetCLRIoCompletionManager',
            (['in'], POINTER(ICLRIoCompletionManager), 'pManager'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'InitializeHostOverlapped',
            (['in'], POINTER(NULL), 'pvOverlapped'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Bind',
            (['in'], HANDLE, 'hPort'),
            (['in'], HANDLE, 'hHandle'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetMinThreads',
            (['in'], DWORD, 'dwMinIOCompletionThreads'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMinThreads',
            (['out'], POINTER(DWORD), 'pdwMinIOCompletionThreads'),
        ),
    ]


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0020_0001(ENUM):
    eSymbolReadingNever = 0
    eSymbolReadingAlways = 1
    eSymbolReadingFullTrustOnly = 2


ESymbolReadingPolicy = __MIDL___MIDL_itf_mscoree_0000_0020_0001


from winnt_h import PACL # NOQA


class ICLRDebugManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRDebugManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'BeginConnection',
            (['in'], CONNID, 'dwConnectionId'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetConnectionTasks',
            (['in'], CONNID, 'id'),
            (['in'], DWORD, 'dwCount'),
            (['in'], POINTER(POINTER(ICLRTask)), 'ppCLRTask'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'EndConnection',
            (['in'], CONNID, 'dwConnectionId'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetDacl',
            (['in'], PACL, 'pacl'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetDacl',
            (['out'], POINTER(PACL), 'pacl'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'IsDebuggerAttached',
            (['out'], POINTER(BOOL), 'pbAttached'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetSymbolReadingPolicy',
            (['in'], ESymbolReadingPolicy, 'policy'),
        ),
    ]


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0021_0001(ENUM):
    DUMP_FLAVOR_Mini = 0
    DUMP_FLAVOR_CriticalCLRState = 1
    DUMP_FLAVOR_NonHeapCLRState = 2
    DUMP_FLAVOR_Default = DUMP_FLAVOR_Mini


ECustomDumpFlavor = __MIDL___MIDL_itf_mscoree_0000_0021_0001


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0021_0002(ENUM):
    DUMP_ITEM_None = 0


ECustomDumpItemKind = __MIDL___MIDL_itf_mscoree_0000_0021_0002


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0021_0003(ctypes.Structure):
    _fields_ = (
        ('itemKind', ECustomDumpItemKind),
    )


CustomDumpItem = __MIDL___MIDL_itf_mscoree_0000_0021_0003


BucketParamLength = 0x00000005


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0021_0005(ENUM):
    Parameter1 = 0
    Parameter2 = Parameter1 + 1
    Parameter3 = Parameter2 + 1
    Parameter4 = Parameter3 + 1
    Parameter5 = Parameter4 + 1
    Parameter6 = Parameter5 + 1
    Parameter7 = Parameter6 + 1
    Parameter8 = Parameter7 + 1
    Parameter9 = Parameter8 + 1
    InvalidBucketParamIndex = Parameter9 + 1


BucketParameterIndex = __MIDL___MIDL_itf_mscoree_0000_0021_0005


# noinspection PyTypeChecker
class _BucketParameters(ctypes.Structure):
    _fields_ = (
        ('fInited', BOOL),
        ('pszEventTypeName', WCHAR * 255),
    )


BucketParameters = _BucketParameters


class ICLRErrorReportingManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRErrorReportingManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetBucketParametersForCurrentException',
            (['out'], POINTER(BucketParameters), 'pParams'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'BeginCustomDump',
            (['in'], ECustomDumpFlavor, 'dwFlavor'),
            (['in'], DWORD, 'dwNumItems'),
            (['in'], POINTER(CustomDumpItem), 'items'),
            ([], DWORD, 'dwReserved'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'EndCustomDump'
        ),
    ]


class IHostCrst(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostCrst
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Enter',
            (['in'], DWORD, 'option'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'TryEnter',
            (['in'], DWORD, 'option'),
            (['out'], POINTER(BOOL), 'pbSucceeded'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetSpinCount',
            (['in'], DWORD, 'dwSpinCount'),
        ),
    ]


class IHostAutoEvent(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostAutoEvent
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Wait',
            (['in'], DWORD, 'dwMilliseconds'),
            (['in'], DWORD, 'option'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Set'
        ),
    ]


class IHostManualEvent(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostManualEvent
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Wait',
            (['in'], DWORD, 'dwMilliseconds'),
            (['in'], DWORD, 'option'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Set'
        ),
    ]


class IHostSemaphore(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostSemaphore
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Wait',
            (['in'], DWORD, 'dwMilliseconds'),
            (['in'], DWORD, 'option'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'ReleaseSemaphore',
            (['in'], LONG, 'lReleaseCount'),
            (['out'], POINTER(LONG), 'lpPreviousCount'),
        ),
    ]


class ICLRSyncManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRSyncManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetMonitorOwner',
            (['in'], SIZE_T, 'Cookie'),
            (['out'], POINTER(POINTER(IHostTask)), 'ppOwnerHostTask'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateRWLockOwnerIterator',
            (['in'], SIZE_T, 'Cookie'),
            (['out'], POINTER(SIZE_T), 'pIterator'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetRWLockOwnerNext',
            (['in'], SIZE_T, 'Iterator'),
            (['out'], POINTER(POINTER(IHostTask)), 'ppOwnerHostTask'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'DeleteRWLockOwnerIterator',
            (['in'], SIZE_T, 'Iterator'),
        ),
    ]


class IHostSyncManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostSyncManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetCLRSyncManager',
            (['in'], POINTER(ICLRSyncManager), 'pManager'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateCrst',
            (['out'], POINTER(POINTER(IHostCrst)), 'ppCrst'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateCrstWithSpinCount',
            (['in'], DWORD, 'dwSpinCount'),
            (['out'], POINTER(POINTER(IHostCrst)), 'ppCrst'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateAutoEvent',
            (['out'], POINTER(POINTER(IHostAutoEvent)), 'ppEvent'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateManualEvent',
            (['in'], BOOL, 'bInitialState'),
            (['out'], POINTER(POINTER(IHostManualEvent)), 'ppEvent'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateMonitorEvent',
            (['in'], SIZE_T, 'Cookie'),
            (['out'], POINTER(POINTER(IHostAutoEvent)), 'ppEvent'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateRWLockWriterEvent',
            (['in'], SIZE_T, 'Cookie'),
            (['out'], POINTER(POINTER(IHostAutoEvent)), 'ppEvent'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateRWLockReaderEvent',
            (['in'], BOOL, 'bInitialState'),
            (['in'], SIZE_T, 'Cookie'),
            (['out'], POINTER(POINTER(IHostManualEvent)), 'ppEvent'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreateSemaphore',
            (['in'], DWORD, 'dwInitial'),
            (['in'], DWORD, 'dwMax'),
            (['out'], POINTER(POINTER(IHostSemaphore)), 'ppSemaphore'),
        ),
    ]


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0028_0001(ENUM):
    OPR_ThreadAbort = 0
    OPR_ThreadRudeAbortInNonCriticalRegion = OPR_ThreadAbort + 1
    OPR_ThreadRudeAbortInCriticalRegion = (
        OPR_ThreadRudeAbortInNonCriticalRegion + 1
    )
    OPR_AppDomainUnload = OPR_ThreadRudeAbortInCriticalRegion + 1
    OPR_AppDomainRudeUnload = OPR_AppDomainUnload + 1
    OPR_ProcessExit = OPR_AppDomainRudeUnload + 1
    OPR_FinalizerRun = OPR_ProcessExit + 1
    MaxClrOperation = OPR_FinalizerRun + 1


EClrOperation = __MIDL___MIDL_itf_mscoree_0000_0028_0001


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0028_0002(ENUM):
    FAIL_NonCriticalResource = 0
    FAIL_CriticalResource = FAIL_NonCriticalResource + 1
    FAIL_FatalRuntime = FAIL_CriticalResource + 1
    FAIL_OrphanedLock = FAIL_FatalRuntime + 1
    FAIL_StackOverflow = FAIL_OrphanedLock + 1
    FAIL_AccessViolation = FAIL_StackOverflow + 1
    FAIL_CodeContract = FAIL_AccessViolation + 1
    MaxClrFailure = FAIL_CodeContract + 1


EClrFailure = __MIDL___MIDL_itf_mscoree_0000_0028_0002


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0028_0003(ENUM):
    eRuntimeDeterminedPolicy = 0
    eHostDeterminedPolicy = eRuntimeDeterminedPolicy + 1


EClrUnhandledException = __MIDL___MIDL_itf_mscoree_0000_0028_0003


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0028_0004(ENUM):
    eNoAction = 0
    eThrowException = eNoAction + 1
    eAbortThread = eThrowException + 1
    eRudeAbortThread = eAbortThread + 1
    eUnloadAppDomain = eRudeAbortThread + 1
    eRudeUnloadAppDomain = eUnloadAppDomain + 1
    eExitProcess = eRudeUnloadAppDomain + 1
    eFastExitProcess = eExitProcess + 1
    eRudeExitProcess = eFastExitProcess + 1
    eDisableRuntime = eRudeExitProcess + 1
    MaxPolicyAction = eDisableRuntime + 1


EPolicyAction = __MIDL___MIDL_itf_mscoree_0000_0028_0004


class ICLRPolicyManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRPolicyManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetDefaultAction',
            (['in'], EClrOperation, 'operation'),
            (['in'], EPolicyAction, 'action'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetTimeout',
            (['in'], EClrOperation, 'operation'),
            (['in'], DWORD, 'dwMilliseconds'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetActionOnTimeout',
            (['in'], EClrOperation, 'operation'),
            (['in'], EPolicyAction, 'action'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetTimeoutAndAction',
            (['in'], EClrOperation, 'operation'),
            (['in'], DWORD, 'dwMilliseconds'),
            (['in'], EPolicyAction, 'action'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetActionOnFailure',
            (['in'], EClrFailure, 'failure'),
            (['in'], EPolicyAction, 'action'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetUnhandledExceptionPolicy',
            (['in'], EClrUnhandledException, 'policy'),
        ),
    ]


class IHostPolicyManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostPolicyManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'OnDefaultAction',
            (['in'], EClrOperation, 'operation'),
            (['in'], EPolicyAction, 'action'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'OnTimeout',
            (['in'], EClrOperation, 'operation'),
            (['in'], EPolicyAction, 'action'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'OnFailure',
            (['in'], EClrFailure, 'failure'),
            (['in'], EPolicyAction, 'action'),
        ),
    ]


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0030_0001(ENUM):
    Event_DomainUnload = 0
    Event_ClrDisabled = Event_DomainUnload + 1
    Event_MDAFired = Event_ClrDisabled + 1
    Event_StackOverflow = Event_MDAFired + 1
    MaxClrEvent = Event_StackOverflow + 1


EClrEvent = __MIDL___MIDL_itf_mscoree_0000_0030_0001


# noinspection PyPep8Naming
class _MDAInfo(ctypes.Structure):
    _fields_ = (
        ('lpMDACaption', LPCWSTR),
        ('lpMDAMessage', LPCWSTR),
    )


MDAInfo = _MDAInfo


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0030_0002(ENUM):
    SO_Managed = 0
    SO_ClrEngine = SO_Managed + 1
    SO_Other = SO_ClrEngine + 1


StackOverflowType = __MIDL___MIDL_itf_mscoree_0000_0030_0002


class _StackOverflowInfo(ctypes.Structure):
    _fields_ = (
        ('soType', StackOverflowType),
    )


StackOverflowInfo = _StackOverflowInfo


class IActionOnCLREvent(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActionOnCLREvent
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'OnEvent',
            (['in'], EClrEvent, 'event'),
            (['in'], PVOID, 'data'),
        ),
    ]


class ICLROnEventManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLROnEventManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'RegisterActionOnEvent',
            (['in'], EClrEvent, 'event'),
            (['in'], POINTER(IActionOnCLREvent), 'pAction'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'UnregisterActionOnEvent',
            (['in'], EClrEvent, 'event'),
            (['in'], POINTER(IActionOnCLREvent), 'pAction'),
        ),
    ]


class IHostGCManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostGCManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SuspensionEnding',
            ([], DWORD, 'Generation'),
        ),
    ]


class ICLRAssemblyReferenceList(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRAssemblyReferenceList
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'IsStringAssemblyReferenceInList',
            (['in'], LPCWSTR, 'pwzAssemblyName'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'IsAssemblyReferenceInList',
            (['in'], POINTER(IUnknown), 'pName'),
        ),
    ]


class ICLRReferenceAssemblyEnum(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRReferenceAssemblyEnum
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Get',
            (['in'], DWORD, 'dwIndex'),
        ),
    ]


class ICLRProbingAssemblyEnum(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRProbingAssemblyEnum
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Get',
            (['in'], DWORD, 'dwIndex'),
        ),
    ]


class _CLRAssemblyIdentityFlags(ENUM):
    CLR_ASSEMBLY_IDENTITY_FLAGS_DEFAULT = 0


ECLRAssemblyIdentityFlags = _CLRAssemblyIdentityFlags


from objidl_h import IStream # NOQA


class ICLRAssemblyIdentityManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRAssemblyIdentityManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetCLRAssemblyReferenceList',
            (['in'], POINTER(LPCWSTR), 'ppwzAssemblyReferences'),
            (['in'], DWORD, 'dwNumOfReferences'),
            (
                ['out'],
                POINTER(POINTER(ICLRAssemblyReferenceList)),
                'ppReferenceList'
            ),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetBindingIdentityFromFile',
            (['in'], LPCWSTR, 'pwzFilePath'),
            (['in'], DWORD, 'dwFlags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetBindingIdentityFromStream',
            (['in'], POINTER(IStream), 'pStream'),
            (['in'], DWORD, 'dwFlags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetReferencedAssembliesFromFile',
            (['in'], LPCWSTR, 'pwzFilePath'),
            (['in'], DWORD, 'dwFlags'),
            (
                ['in'],
                POINTER(ICLRAssemblyReferenceList),
                'pExcludeAssembliesList'
            ),
            (
                ['out'],
                POINTER(POINTER(ICLRReferenceAssemblyEnum)),
                'ppReferenceEnum'
            ),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetReferencedAssembliesFromStream',
            (['in'], POINTER(IStream), 'pStream'),
            (['in'], DWORD, 'dwFlags'),
            (
                ['in'],
                POINTER(ICLRAssemblyReferenceList),
                'pExcludeAssembliesList'
            ),
            (
                ['out'],
                POINTER(POINTER(ICLRReferenceAssemblyEnum)),
                'ppReferenceEnum'
            ),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetProbingAssembliesFromReference',
            (['in'], DWORD, 'dwMachineType'),
            (['in'], DWORD, 'dwFlags'),
            (['in'], LPCWSTR, 'pwzReferenceIdentity'),
            (
                ['out'],
                POINTER(POINTER(ICLRProbingAssemblyEnum)),
                'ppProbingAssemblyEnum'
            ),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'IsStronglyNamed',
            (['in'], LPCWSTR, 'pwzAssemblyIdentity'),
            (['out'], POINTER(BOOL), 'pbIsStronglyNamed'),
        ),
    ]


# noinspection PyPep8Naming
class _hostBiningPolicyModifyFlags(ENUM):
    HOST_BINDING_POLICY_MODIFY_DEFAULT = 0
    HOST_BINDING_POLICY_MODIFY_CHAIN = 1
    HOST_BINDING_POLICY_MODIFY_REMOVE = 2
    HOST_BINDING_POLICY_MODIFY_MAX = 3


EHostBindingPolicyModifyFlags = _hostBiningPolicyModifyFlags


class ICLRHostBindingPolicyManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRHostBindingPolicyManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'ModifyApplicationPolicy',
            (['in'], LPCWSTR, 'pwzSourceAssemblyIdentity'),
            (['in'], LPCWSTR, 'pwzTargetAssemblyIdentity'),
            (['in'], POINTER(BYTE), 'pbApplicationPolicy'),
            (['in'], DWORD, 'cbAppPolicySize'),
            (['in'], DWORD, 'dwPolicyModifyFlags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'EvaluatePolicy',
            (['in'], LPCWSTR, 'pwzReferenceIdentity'),
            (['in'], POINTER(BYTE), 'pbApplicationPolicy'),
            (['in'], DWORD, 'cbAppPolicySize'),
        ),
    ]


# noinspection PyTypeChecker,PyPep8Naming
class _COR_GC_STATS(ctypes.Structure):
    _fields_ = [
        ('Flags', ULONG),
        ('ExplicitGCCount', ULONG_PTR),
        ('GenCollectionsTaken', ULONG_PTR * 3),
        ('CommittedKBytes', ULONG_PTR),
        ('ReservedKBytes', ULONG_PTR),
        ('Gen0HeapSizeKBytes', ULONG_PTR),
        ('Gen1HeapSizeKBytes', ULONG_PTR),
        ('Gen2HeapSizeKBytes', ULONG_PTR),
        ('LargeObjectHeapSizeKBytes', ULONG_PTR),
        ('KBytesPromotedFromGen0', ULONG_PTR),
        ('KBytesPromotedFromGen1', ULONG_PTR),
    ]


COR_GC_STATS = _COR_GC_STATS


class ICLRGCManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRGCManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Collect',
            (['in'], LONG, 'Generation'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetStats',
            (['in', 'out'], POINTER(COR_GC_STATS), 'pStats'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetGCStartupLimits',
            (['in'], DWORD, 'SegmentSize'),
            (['in'], DWORD, 'MaxGen0Size'),
        ),
    ]


class ICLRGCManager2(ICLRGCManager):
    _case_insensitive_ = True
    _iid_ = IID_ICLRGCManager2
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetGCStartupLimitsEx',
            (['in'], SIZE_T, 'SegmentSize'),
            (['in'], SIZE_T, 'MaxGen0Size'),
        ),
    ]


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0040_0001(ENUM):
    ePolicyLevelNone = 0
    ePolicyLevelRetargetable = 0x1
    ePolicyUnifiedToCLR = 0x2
    ePolicyLevelApp = 0x4
    ePolicyLevelPublisher = 0x8
    ePolicyLevelHost = 0x10
    ePolicyLevelAdmin = 0x20
    ePolicyPortability = 0x40


EBindPolicyLevels = __MIDL___MIDL_itf_mscoree_0000_0040_0001


class _AssemblyBindInfo(ctypes.Structure):
    _fields_ = (
        ('dwAppDomainId', DWORD),
        ('lpReferencedIdentity', LPCWSTR),
        ('lpPostPolicyIdentity', LPCWSTR),
    )


AssemblyBindInfo = _AssemblyBindInfo


class _ModuleBindInfo(ctypes.Structure):
    _fields_ = (
        ('dwAppDomainId', DWORD),
        ('lpAssemblyIdentity', LPCWSTR),
    )


ModuleBindInfo = _ModuleBindInfo


class _HostApplicationPolicy(ENUM):
    HOST_APPLICATION_BINDING_POLICY = 1


EHostApplicationPolicy = _HostApplicationPolicy


class IHostAssemblyStore(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostAssemblyStore
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'ProvideAssembly',
            (['in'], POINTER(AssemblyBindInfo), 'pBindInfo'),
            (['out'], POINTER(UINT64), 'pAssemblyId'),
            (['out'], POINTER(UINT64), 'pContext'),
            (['out'], POINTER(POINTER(IStream)), 'ppStmAssemblyImage'),
            (['out'], POINTER(POINTER(IStream)), 'ppStmPDB'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'ProvideModule',
            (['in'], POINTER(ModuleBindInfo), 'pBindInfo'),
            (['out'], POINTER(DWORD), 'pdwModuleId'),
            (['out'], POINTER(POINTER(IStream)), 'ppStmModuleImage'),
            (['out'], POINTER(POINTER(IStream)), 'ppStmPDB'),
        ),
    ]


class IHostAssemblyManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostAssemblyManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetNonHostStoreAssemblies',
            (
                ['out'],
                POINTER(POINTER(ICLRAssemblyReferenceList)),
                'ppReferenceList'
            ),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetAssemblyStore',
            (['out'], POINTER(POINTER(IHostAssemblyStore)), 'ppAssemblyStore'),
        ),
    ]


IID_IHostControl = EXTERN_GUID(
    0x02CA073C,
    0x7079,
    0x4860,
    0x88,
    0x0A,
    0xC2,
    0xF7,
    0xA4,
    0x49,
    0xC9,
    0x91
)


class IHostControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostControl
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetHostManager',
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(NULL)), 'ppObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetAppDomainManager',
            (['in'], DWORD, 'dwAppDomainID'),
            (['in'], POINTER(IUnknown), 'pUnkAppDomainManager'),
        ),
    ]


IID_ICLRControl = EXTERN_GUID(
    0x9065597E,
    0xD1A1,
    0x4FB2,
    0xB6,
    0xBA,
    0x7E,
    0x1F,
    0xCE,
    0x23,
    0x0F,
    0x61
)


class ICLRControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRControl
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetCLRManager',
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(NULL)), 'ppObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetAppDomainManagerType',
            (['in'], LPCWSTR, 'pwzAppDomainManagerAssembly'),
            (['in'], LPCWSTR, 'pwzAppDomainManagerType'),
        ),
    ]


class ICLRRuntimeHost(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRRuntimeHost
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetHostControl',
            (['in'], POINTER(IHostControl), 'pHostControl'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetCLRControl',
            (['out'], POINTER(POINTER(ICLRControl)), 'pCLRControl'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'UnloadAppDomain',
            (['in'], DWORD, 'dwAppDomainId'),
            (['in'], BOOL, 'fWaitUntilDone'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'ExecuteInAppDomain',
            (['in'], DWORD, 'dwAppDomainId'),
            (['in'], FExecuteInAppDomainCallback, 'pCallback'),
            (['in'], POINTER(NULL), 'cookie'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetCurrentAppDomainId',
            (['out'], POINTER(DWORD), 'pdwAppDomainId'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'ExecuteApplication',
            (['in'], LPCWSTR, 'pwzAppFullName'),
            (['in'], DWORD, 'dwManifestPaths'),
            (['in'], POINTER(LPCWSTR), 'ppwzManifestPaths'),
            (['in'], DWORD, 'dwActivationData'),
            (['in'], POINTER(LPCWSTR), 'ppwzActivationData'),
            (['out'], POINTER(INT), 'pReturnValue'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'ExecuteInDefaultAppDomain',
            (['in'], LPCWSTR, 'pwzAssemblyPath'),
            (['in'], LPCWSTR, 'pwzTypeName'),
            (['in'], LPCWSTR, 'pwzMethodName'),
            (['in'], LPCWSTR, 'pwzArgument'),
            (['out'], POINTER(DWORD), 'pReturnValue'),
        ),
    ]


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0045_0001(ENUM):
    eNoChecks = 0
    eSynchronization = 0x1
    eSharedState = 0x2
    eExternalProcessMgmt = 0x4
    eSelfAffectingProcessMgmt = 0x8
    eExternalThreading = 0x10
    eSelfAffectingThreading = 0x20
    eSecurityInfrastructure = 0x40
    eUI = 0x80
    eMayLeakOnAbort = 0x100
    eAll = 0x1FF


EApiCategories = __MIDL___MIDL_itf_mscoree_0000_0045_0001


class ICLRHostProtectionManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRHostProtectionManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetProtectedCategories',
            (['in'], EApiCategories, 'categories'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetEagerSerializeGrantSets'
        ),
    ]


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0046_0001(ENUM):
    eInitializeNewDomainFlags_None = 0
    eInitializeNewDomainFlags_NoSecurityChanges = 0x2


EInitializeNewDomainFlags = __MIDL___MIDL_itf_mscoree_0000_0046_0001


class ICLRDomainManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRDomainManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetAppDomainManagerType',
            (['in'], LPCWSTR, 'wszAppDomainManagerAssembly'),
            (['in'], LPCWSTR, 'wszAppDomainManagerType'),
            (['in'], EInitializeNewDomainFlags, 'dwInitializeDomainFlags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetPropertiesForDefaultAppDomain',
            (['in'], DWORD, 'nProperties'),
            (['in'], POINTER(LPCWSTR), 'pwszPropertyNames'),
            (['in'], POINTER(LPCWSTR), 'pwszPropertyValues'),
        ),
    ]


class ITypeName(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITypeName
    _idlflags_ = []


ITypeName._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetNameCount',
        (['out', 'retval'], POINTER(DWORD), 'pCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNames',
        (['in'], DWORD, 'count'),
        (['out'], POINTER(BSTR), 'rgbszNames'),
        (['out', 'retval'], POINTER(DWORD), 'pCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeArgumentCount',
        (['out', 'retval'], POINTER(DWORD), 'pCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeArguments',
        (['in'], DWORD, 'count'),
        (['out'], POINTER(POINTER(ITypeName)), 'rgpArguments'),
        (['out', 'retval'], POINTER(DWORD), 'pCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetModifierLength',
        (['out', 'retval'], POINTER(DWORD), 'pCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetModifiers',
        (['in'], DWORD, 'count'),
        (['out'], POINTER(DWORD), 'rgModifiers'),
        (['out', 'retval'], POINTER(DWORD), 'pCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAssemblyName',
        (['out', 'retval'], POINTER(BSTR), 'rgbszAssemblyNames'),
    ),
]


class ITypeNameBuilder(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITypeNameBuilder
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'AddName',
            (['in'], LPCWSTR, 'szName'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'AddArray',
            (['in'], DWORD, 'rank'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'AddAssemblySpec',
            (['in'], LPCWSTR, 'szAssemblySpec'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'ToString',
            (['out', 'retval'], POINTER(BSTR), 'pszStringRepresentation'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Clear'
        ),
    ]


class ITypeNameFactory(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITypeNameFactory
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'ParseTypeName',
            (['in'], LPCWSTR, 'szName'),
            (['out'], POINTER(DWORD), 'pError'),
            (['out', 'retval'], POINTER(POINTER(ITypeName)), 'ppTypeName'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetTypeNameBuilder',
            (
                ['out', 'retval'],
                POINTER(POINTER(ITypeNameBuilder)),
                'ppTypeBuilder'
            ),
        ),
    ]


class IApartmentCallback(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IApartmentCallback
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'DoCallback',
            (['in'], SIZE_T, 'pFunc'),
            (['in'], SIZE_T, 'pData'),
        ),
    ]


class IManagedObject(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IManagedObject
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetSerializedBuffer',
            (['out'], POINTER(BSTR), 'pBSTR'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetObjectIdentity',
            (['out'], POINTER(BSTR), 'pBSTRGUID'),
            (['out'], POINTER(INT), 'AppDomainID'),
            (['out'], POINTER(INT), 'pCCW'),
        ),
    ]


class ICatalogServices(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICatalogServices
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'NotAutodone'
        ),
    ]


# noinspection PyPep8Naming
class __MIDL___MIDL_itf_mscoree_0000_0048_0001(ENUM):
    eCurrentContext = 0
    eRestrictedContext = 0x1


EContextType = __MIDL___MIDL_itf_mscoree_0000_0048_0001


class IHostSecurityContext(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostSecurityContext
    _idlflags_ = []


IHostSecurityContext._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Capture',
        (['out'], POINTER(POINTER(IHostSecurityContext)), 'ppClonedContext'),
    ),
]


class IHostSecurityManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHostSecurityManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'ImpersonateLoggedOnUser',
            (['in'], HANDLE, 'hToken'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'OpenThreadToken',
            (['in'], DWORD, 'dwDesiredAccess'),
            (['in'], BOOL, 'bOpenAsSelf'),
            (['out'], POINTER(HANDLE), 'phThreadToken'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetThreadToken',
            (['in'], HANDLE, 'hToken'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetSecurityContext',
            (['in'], EContextType, 'eContextType'),
            (
                ['out'],
                POINTER(POINTER(IHostSecurityContext)),
                'ppSecurityContext'
            ),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetSecurityContext',
            (['in'], EContextType, 'eContextType'),
            (['in'], POINTER(IHostSecurityContext), 'pSecurityContext'),
        ),
    ]


class ICLRAppDomainResourceMonitor(IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICLRAppDomainResourceMonitor
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetCurrentAllocated',
            (['in'], DWORD, 'dwAppDomainId'),
            (['out'], POINTER(ULONGLONG), 'pBytesAllocated'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetCurrentSurvived',
            (['in'], DWORD, 'dwAppDomainId'),
            (['out'], POINTER(ULONGLONG), 'pAppDomainBytesSurvived'),
            (['out'], POINTER(ULONGLONG), 'pTotalBytesSurvived'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetCurrentCpuTime',
            (['in'], DWORD, 'dwAppDomainId'),
            (['out'], POINTER(ULONGLONG), 'pMilliseconds'),
        ),
    ]
