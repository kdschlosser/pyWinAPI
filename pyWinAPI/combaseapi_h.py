# from stdlib_h import * # NOQA
# from wtypesbase_h import * # NOQA
# from unknwnbase_h import * # NOQA
# from objidlbase_h import * # NOQA
from .guiddef_h import * # NOQA
# from cguid_h import * # NOQA
from .wtypes_h import (
    ENUM,
    DWORD,
    UINT64,
    POINTER,
    HRESULT,
    LPVOID,
    STDAPI,
    VOID,
    CONST,
    FAR,
    ULONG,
    BOOL,
    STDAPICALLTYPE,
    INT
)
from .wtypesbase_h import (
    CLSCTX_INPROC_SERVER,
    CLSCTX_INPROC_HANDLER,
    CLSCTX_LOCAL_SERVER,
    CLSCTX_REMOTE_SERVER
)

from .propidl_h import PROPVARIANT
import ctypes
import comtypes


ole32 = ctypes.windll.Ole32
# combase = ctypes.windll.Combase

_WIN32_WINNT = 0x00000600

WINOLEAPI = STDAPI

def WINOLEAPI_(type):
    return type

def STDMETHOD(method):
    return method


def STDMETHOD_(type, method):
    return type


def STDMETHODV(method):
    return method


def STDMETHODV_(type, method):
    return type, method


PURE = 0
THIS = VOID


def DECLARE_INTERFACE(iface):
    return iface


def DECLARE_INTERFACE_(iface, baseiface):
    return iface , baseiface


def DECLARE_INTERFACE_IID(iface, iid):
    return DECLSPEC_UUID(iid), iface


def DECLARE_INTERFACE_IID_(iface, baseiface, iid):
    return DECLSPEC_UUID(iid), iface, baseiface


def IFACEMETHOD(method):
    return method


def IFACEMETHOD_(type, method):
    return type, method


def IFACEMETHODV(method):
    return method


def IFACEMETHODV_(type, method):
    return type, method

def IID_PPV_ARGS_Helper(ppType):
    return isinstance(ppType, comtypes.IUnknown)


def IID_PPV_ARGS(ppType):
    return ppType._iid_, IID_PPV_ARGS_Helper(ppType)

CONST_VTBL = CONST

FARSTRUCT = FAR
HUGEP = VOID


def LISet32(li, v):
    if v < 0:
        li.HighPart = v
        return -1
    else:
        li.LowPart = v
        return 0


def ULISet32(li, v):
    li.HighPart = 0
    li.LowPart = v
    return li


CLSCTX_INPROC = CLSCTX_INPROC_SERVER | CLSCTX_INPROC_HANDLER

CLSCTX_ALL = (
    CLSCTX_INPROC_SERVER |
    CLSCTX_INPROC_HANDLER |
    CLSCTX_LOCAL_SERVER |
    CLSCTX_REMOTE_SERVER
)
CLSCTX_SERVER = (
    CLSCTX_INPROC_SERVER |
    CLSCTX_LOCAL_SERVER |
    CLSCTX_REMOTE_SERVER
)


class tagREGCLS(ENUM):
    REGCLS_SINGLEUSE = 0
    REGCLS_MULTIPLEUSE = 1
    REGCLS_MULTI_SEPARATE = 2
    REGCLS_SUSPENDED = 4
    REGCLS_SURROGATE = 8
    REGCLS_AGILE = 0x10


REGCLS = tagREGCLS


class tagCOINITBASE(ENUM):
    COINITBASE_MULTITHREADED = 0x0


COINITBASE = tagCOINITBASE

# _Check_return_ WINOLEAPI
# CoGetMalloc(
#     _In_ DWORD dwMemContext,
#     _Outptr_ LPMALLOC  FAR * ppMalloc
#     );
CoGetMalloc = ole32.CoGetMalloc
CoGetMalloc.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CreateStreamOnHGlobal(
#     HGLOBAL hGlobal,
#     _In_ BOOL fDeleteOnRelease,
#     _Outptr_ LPSTREAM  FAR * ppstm
#     );
CreateStreamOnHGlobal = ole32.CreateStreamOnHGlobal
CreateStreamOnHGlobal.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# GetHGlobalFromStream(
#     _In_ LPSTREAM pstm,
#     _Out_ HGLOBAL  FAR * phglobal
#     );
GetHGlobalFromStream = ole32.GetHGlobalFromStream
GetHGlobalFromStream.restype = WINOLEAPI

# init/uninit

# WINOLEAPI_(VOID)
# CoUninitialize(
#     VOID
#     );
CoUninitialize = ole32.CoUninitialize
CoUninitialize.restype = WINOLEAPI_(VOID)

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# WINOLEAPI_(DWORD)
# CoGetCurrentProcess(
#     VOID
#     );
CoGetCurrentProcess = ole32.CoGetCurrentProcess
CoGetCurrentProcess.restype = WINOLEAPI_(DWORD)

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# DCOM

# _Check_return_ WINOLEAPI
# CoInitializeEx(
#     _In_opt_ LPVOID pvReserved,
#     _In_ DWORD dwCoInit
#     );
CoInitializeEx = ole32.CoInitializeEx
CoInitializeEx.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# WINOLEAPI
# CoGetCallerTID(
#     _Out_ LPDWORD lpdwTID
#     );
CoGetCallerTID = ole32.CoGetCallerTID
CoGetCallerTID.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

# WINOLEAPI
# CoGetCurrentLogicalThreadId(
#     _Out_ GUID* pguid
#     );
CoGetCurrentLogicalThreadId = ole32.CoGetCurrentLogicalThreadId
CoGetCurrentLogicalThreadId.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
# DCOM

# _Check_return_ WINOLEAPI
# CoGetContextToken(
#     _Out_ ULONG_PTR* pToken
#     );
CoGetContextToken = ole32.CoGetContextToken
CoGetContextToken.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoGetDefaultContext(
#     _In_ APTTYPE aptType,
#     _In_ REFIID riid,
#     _Outptr_ VOID** ppv
#     );
CoGetDefaultContext = ole32.CoGetDefaultContext
CoGetDefaultContext.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# definition for Win7 new APIs

# _Check_return_ WINOLEAPI
# CoGetApartmentType(
#     _Out_ APTTYPE* pAptType,
#     _Out_ APTTYPEQUALIFIER* pAptQualifier
#     );
CoGetApartmentType = ole32.CoGetApartmentType
CoGetApartmentType.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
# definition for Win8 new APIs


class tagServerInformation(ctypes.Structure):
    _fields_ = [
        ('dwServerPid', DWORD),
        ('dwServerTid', DWORD),
        ('ui64ServerAddress', UINT64),
    ]


ServerInformation = tagServerInformation
PServerInformation = POINTER(tagServerInformation)


# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoDecodeProxy(
#     _In_ DWORD dwClientPid,
#     _In_ UINT64 ui64ProxyAddress,
#     _Out_ PServerInformation pServerInformation
#     );
# CoDecodeProxy = combase.CoDecodeProxy
# CoDecodeProxy.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoIncrementMTAUsage(
#     _Out_ CO_MTA_USAGE_COOKIE* pCookie
#     );
# CoIncrementMTAUsage = ole32.CoIncrementMTAUsage
# CoIncrementMTAUsage.restype = WINOLEAPI


#                WINOLEAPI
# CoDecrementMTAUsage(
#     _In_ CO_MTA_USAGE_COOKIE Cookie
#     );
# CoDecrementMTAUsage = ole32.CoDecrementMTAUsage
# CoDecrementMTAUsage.restype = WINOLEAPI


# WINOLEAPI
# CoAllowUnmarshalerCLSID(
#     _In_ REFCLSID clsid
#     );
# CoAllowUnmarshalerCLSID = ole32.CoAllowUnmarshalerCLSID
# CoAllowUnmarshalerCLSID.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoGetObjectContext(
#     _In_ REFIID riid,
#     _Outptr_ LPVOID  FAR * ppv
#     );
CoGetObjectContext = ole32.CoGetObjectContext
CoGetObjectContext.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
# register/revoke/get class objects

# _Check_return_ WINOLEAPI
# CoGetClassObject(
#     _In_ REFCLSID rclsid,
#     _In_ DWORD dwClsContext,
#     _In_opt_ LPVOID pvReserved,
#     _In_ REFIID riid,
#     _Outptr_ LPVOID  FAR * ppv
#     );
CoGetClassObject = ole32.CoGetClassObject
CoGetClassObject.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoRegisterClassObject(
#     _In_ REFCLSID rclsid,
#     _In_ LPUNKNOWN pUnk,
#     _In_ DWORD dwClsContext,
#     _In_ DWORD flags,
#     _Out_ LPDWORD lpdwRegister
#     );
CoRegisterClassObject = ole32.CoRegisterClassObject
CoRegisterClassObject.restype = WINOLEAPI


# WINOLEAPI
# CoRevokeClassObject(
#     _In_ DWORD dwRegister
#     );
CoRevokeClassObject = ole32.CoRevokeClassObject
CoRevokeClassObject.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoResumeClassObjects(
#     VOID
#     );
CoResumeClassObjects = ole32.CoResumeClassObjects
CoResumeClassObjects.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoSuspendClassObjects(
#     VOID
#     );
CoSuspendClassObjects = ole32.CoSuspendClassObjects
CoSuspendClassObjects.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# WINOLEAPI_(ULONG)
# CoAddRefServerProcess(
#     VOID
#     );
CoAddRefServerProcess = ole32.CoAddRefServerProcess
CoAddRefServerProcess.restype = WINOLEAPI_(ULONG)


# WINOLEAPI_(ULONG)
# CoReleaseServerProcess(
#     VOID
#     );
CoReleaseServerProcess = ole32.CoReleaseServerProcess
CoReleaseServerProcess.restype = WINOLEAPI_(ULONG)


# _Check_return_ WINOLEAPI
# CoGetPSClsid(
#     _In_ REFIID riid,
#     _Out_ CLSID* pClsid
#     );
CoGetPSClsid = ole32.CoGetPSClsid
CoGetPSClsid.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoRegisterPSClsid(
#     _In_ REFIID riid,
#     _In_ REFCLSID rclsid
#     );
CoRegisterPSClsid = ole32.CoRegisterPSClsid
CoRegisterPSClsid.restype = WINOLEAPI

# Registering surrogate processes

# _Check_return_ WINOLEAPI
# CoRegisterSurrogate(
#     _In_ LPSURROGATE pSurrogate
#     );
CoRegisterSurrogate = ole32.CoRegisterSurrogate
CoRegisterSurrogate.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# marshaling INTerface poINTers

# _Check_return_ WINOLEAPI
# CoGetMarshalSizeMax(
#     _Out_ ULONG* pulSize,
#     _In_ REFIID riid,
#     _In_ LPUNKNOWN pUnk,
#     _In_ DWORD dwDestContext,
#     _In_opt_ LPVOID pvDestContext,
#     _In_ DWORD mshlflags
#     );
CoGetMarshalSizeMax = ole32.CoGetMarshalSizeMax
CoGetMarshalSizeMax.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoMarshalInterface(
#     _In_ LPSTREAM pStm,
#     _In_ REFIID riid,
#     _In_ LPUNKNOWN pUnk,
#     _In_ DWORD dwDestContext,
#     _In_opt_ LPVOID pvDestContext,
#     _In_ DWORD mshlflags
#     );
CoMarshalInterface = ole32.CoMarshalInterface
CoMarshalInterface.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoUnmarshalInterface(
#     _In_ LPSTREAM pStm,
#     _In_ REFIID riid,
#     _COM_Outptr_ LPVOID  FAR * ppv
#     );
CoUnmarshalInterface = ole32.CoUnmarshalInterface
CoUnmarshalInterface.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# WINOLEAPI
# CoMarshalHresult(
#     _In_ LPSTREAM pstm,
#     _In_ HRESULT hresult
#     );
CoMarshalHresult = ole32.CoMarshalHresult
CoMarshalHresult.restype = WINOLEAPI


# WINOLEAPI
# CoUnmarshalHresult(
#     _In_ LPSTREAM pstm,
#     _Out_ HRESULT  FAR * phresult
#     );
CoUnmarshalHresult = ole32.CoUnmarshalHresult
CoUnmarshalHresult.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoReleaseMarshalData(
#     _In_ LPSTREAM pStm
#     );
CoReleaseMarshalData = ole32.CoReleaseMarshalData
CoReleaseMarshalData.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoDisconnectObject(
#     _In_ LPUNKNOWN pUnk,
#     _In_ DWORD dwReserved
#     );
CoDisconnectObject = ole32.CoDisconnectObject
CoDisconnectObject.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoLockObjectExternal(
#     _In_ LPUNKNOWN pUnk,
#     _In_ BOOL fLock,
#     _In_ BOOL fLastUnlockReleases
#     );
CoLockObjectExternal = ole32.CoLockObjectExternal
CoLockObjectExternal.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoGetStandardMarshal(
#     _In_ REFIID riid,
#     _In_ LPUNKNOWN pUnk,
#     _In_ DWORD dwDestContext,
#     _In_opt_ LPVOID pvDestContext,
#     _In_ DWORD mshlflags,
#     _Outptr_ LPMARSHAL  FAR * ppMarshal
#     );
CoGetStandardMarshal = ole32.CoGetStandardMarshal
CoGetStandardMarshal.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoGetStdMarshalEx(
#     _In_ LPUNKNOWN pUnkOuter,
#     _In_ DWORD smexflags,
#     _Outptr_ LPUNKNOWN  FAR * ppUnkInner
#     );
CoGetStdMarshalEx = ole32.CoGetStdMarshalEx
CoGetStdMarshalEx.restype = WINOLEAPI


# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# flags for CoGetStdMarshalEx
class tagSTDMSHLFLAGS(ENUM):
    SMEXF_SERVER = 0x01
    SMEXF_HANDLER = 0x02


STDMSHLFLAGS = tagSTDMSHLFLAGS


# server side aggregated std marshaler
# client side (handler) agg std marshaler
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# WINOLEAPI_(BOOL)
# CoIsHandlerConnected(
#     _In_ LPUNKNOWN pUnk
#     );
CoIsHandlerConnected = ole32.CoIsHandlerConnected
CoIsHandlerConnected.restype = WINOLEAPI_(BOOL)

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# Apartment model INTer-thread INTerface passing helpers

# _Check_return_ WINOLEAPI
# CoMarshalInterThreadInterfaceInStream(
#     _In_ REFIID riid,
#     _In_ LPUNKNOWN pUnk,
#     _Outptr_ LPSTREAM* ppStm
#     );
CoMarshalInterThreadInterfaceInStream = (
    ole32.CoMarshalInterThreadInterfaceInStream
)
CoMarshalInterThreadInterfaceInStream.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoGetInterfaceAndReleaseStream(
#     _In_ LPSTREAM pStm,
#     _In_ REFIID iid,
#     _COM_Outptr_ LPVOID  FAR * ppv
#     );
CoGetInterfaceAndReleaseStream = ole32.CoGetInterfaceAndReleaseStream
CoGetInterfaceAndReleaseStream.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoCreateFreeThreadedMarshaler(
#     _In_opt_ LPUNKNOWN punkOuter,
#     _Outptr_ LPUNKNOWN* ppunkMarshal
#     );
CoCreateFreeThreadedMarshaler = ole32.CoCreateFreeThreadedMarshaler
CoCreateFreeThreadedMarshaler.restype = WINOLEAPI


# WINOLEAPI_(VOID)
# CoFreeUnusedLibraries(
#     VOID
#     );
CoFreeUnusedLibraries = ole32.CoFreeUnusedLibraries
CoFreeUnusedLibraries.restype = WINOLEAPI_(VOID)


# WINOLEAPI_(VOID)
# CoFreeUnusedLibrariesEx(
#     _In_ DWORD dwUnloadDelay,
#     _In_ DWORD dwReserved
#     );
CoFreeUnusedLibrariesEx = ole32.CoFreeUnusedLibrariesEx
CoFreeUnusedLibrariesEx.restype = WINOLEAPI_(VOID)

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoDisconnectContext(
#     DWORD dwTimeout
#     );
CoDisconnectContext = ole32.CoDisconnectContext
CoDisconnectContext.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# DCOM
# Call Security.

# _Check_return_ WINOLEAPI
# CoInitializeSecurity(
#     _In_opt_ PSECURITY_DESCRIPTOR pSecDesc,
#     _In_ LONG cAuthSvc,
#     _In_reads_opt_(cAuthSvc) SOLE_AUTHENTICATION_SERVICE* asAuthSvc,
#     _In_opt_ VOID* pReserved1,
#     _In_ DWORD dwAuthnLevel,
#     _In_ DWORD dwImpLevel,
#     _In_opt_ VOID* pAuthList,
#     _In_ DWORD dwCapabilities,
#     _In_opt_ VOID* pReserved3
#     );
CoInitializeSecurity = ole32.CoInitializeSecurity
CoInitializeSecurity.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoGetCallContext(
#     _In_ REFIID riid,
#     _Outptr_ VOID** ppInterface
#     );
CoGetCallContext = ole32.CoGetCallContext
CoGetCallContext.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoQueryProxyBlanket(
#     _In_ IUnknown* pProxy,
#     _Out_opt_ DWORD* pwAuthnSvc,
#     _Out_opt_ DWORD* pAuthzSvc,
#     _Outptr_opt_ LPOLESTR* pServerPrincName,
#     _Out_opt_ DWORD* pAuthnLevel,
#     _Out_opt_ DWORD* pImpLevel,
#     _Out_opt_ RPC_AUTH_IDENTITY_HANDLE* pAuthInfo,
#     _Out_opt_ DWORD* pCapabilites
#     );
CoQueryProxyBlanket = ole32.CoQueryProxyBlanket
CoQueryProxyBlanket.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoSetProxyBlanket(
#     _In_ IUnknown* pProxy,
#     _In_ DWORD dwAuthnSvc,
#     _In_ DWORD dwAuthzSvc,
#     _In_opt_ OLECHAR* pServerPrincName,
#     _In_ DWORD dwAuthnLevel,
#     _In_ DWORD dwImpLevel,
#     _In_opt_ RPC_AUTH_IDENTITY_HANDLE pAuthInfo,
#     _In_ DWORD dwCapabilities
#     );
CoSetProxyBlanket = ole32.CoSetProxyBlanket
CoSetProxyBlanket.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoCopyProxy(
#     _In_ IUnknown* pProxy,
#     _Outptr_ IUnknown** ppCopy
#     );
CoCopyProxy = ole32.CoCopyProxy
CoCopyProxy.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoQueryClientBlanket(
#     _Out_opt_ DWORD* pAuthnSvc,
#     _Out_opt_ DWORD* pAuthzSvc,
#     _Outptr_opt_ LPOLESTR* pServerPrincName,
#     _Out_opt_ DWORD* pAuthnLevel,
#     _Out_opt_ DWORD* pImpLevel,
#     _Outptr_opt_result_buffer_(_Inexpressible_("depends on pAuthnSvc")) RPC_AUTHZ_HANDLE* pPrivs,
#     _Inout_opt_ DWORD* pCapabilities
#     );
CoQueryClientBlanket = ole32.CoQueryClientBlanket
CoQueryClientBlanket.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoImpersonateClient(
#     VOID
#     );
CoImpersonateClient = ole32.CoImpersonateClient
CoImpersonateClient.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoRevertToSelf(
#     VOID
#     );
CoRevertToSelf = ole32.CoRevertToSelf
CoRevertToSelf.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoQueryAuthenticationServices(
#     _Out_ DWORD* pcAuthSvc,
#     _Outptr_result_buffer_(*pcAuthSvc) SOLE_AUTHENTICATION_SERVICE** asAuthSvc
#     );
CoQueryAuthenticationServices = ole32.CoQueryAuthenticationServices
CoQueryAuthenticationServices.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoSwitchCallContext(
#     _In_opt_ IUnknown* pNewObject,
#     _Outptr_ IUnknown** ppOldObject
#     );
CoSwitchCallContext = ole32.CoSwitchCallContext
CoSwitchCallContext.restype = WINOLEAPI

COM_RIGHTS_EXECUTE = 0x00000001
COM_RIGHTS_EXECUTE_LOCAL = 0x00000002
COM_RIGHTS_EXECUTE_REMOTE = 0x00000004
COM_RIGHTS_ACTIVATE_LOCAL = 0x00000008
COM_RIGHTS_ACTIVATE_REMOTE = 0x00000010
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
# DCOM
# helper for creating instances

# _Check_return_ WINOLEAPI
# CoCreateInstance(
#     _In_ REFCLSID rclsid,
#     _In_opt_ LPUNKNOWN pUnkOuter,
#     _In_ DWORD dwClsContext,
#     _In_ REFIID riid,
#     _COM_Outptr_ _At_(*ppv, _Post_readable_size_(_Inexpressible_(varies))) LPVOID  FAR * ppv
#     );
CoCreateInstance = ole32.CoCreateInstance
CoCreateInstance.restype = WINOLEAPI

# DCOM

# _Check_return_ WINOLEAPI
# CoCreateInstanceEx(
#     _In_ REFCLSID Clsid,
#     _In_opt_ IUnknown* punkOuter,
#     _In_ DWORD dwClsCtx,
#     _In_opt_ COSERVERINFO* pServerInfo,
#     _In_ DWORD dwCount,
#     _Inout_updates_(dwCount) MULTI_QI* pResults
#     );
CoCreateInstanceEx = ole32.CoCreateInstanceEx
CoCreateInstanceEx.restype = WINOLEAPI

# DCOM

# WINOLEAPI
# CoRegisterActivationFilter(
#     _In_ IActivationFilter* pActivationFilter
#     );
# CoRegisterActivationFilter = ole32.CoRegisterActivationFilter
# CoRegisterActivationFilter.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# CoCreateInstanceFromApp(
#     _In_ REFCLSID Clsid,
#     _In_opt_ IUnknown* punkOuter,
#     _In_ DWORD dwClsCtx,
#     _In_opt_ PVOID reserved,
#     _In_ DWORD dwCount,
#     _Inout_updates_(dwCount) MULTI_QI* pResults
#     );
# CoCreateInstanceFromApp = ole32.CoCreateInstanceFromApp
# CoCreateInstanceFromApp.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# __inline _Check_return_ HRESULT CoCreateInstance(
#     _In_     REFCLSID rclsid,
#     _In_opt_ LPUNKNOWN pUnkOuter,
#     _In_     DWORD dwClsContext,
#     _In_     REFIID riid,
#     _COM_Outptr_ _At_(*ppv, _Post_readable_size_(_Inexpressible_(varies))) LPVOID FAR* ppv)
# {
#     MULTI_QI    OneQI;
CoCreateInstance = ole32.CoCreateInstance
CoCreateInstance.restype = HRESULT


# __inline _Check_return_ HRESULT CoCreateInstanceEx(
#     _In_ REFCLSID                      Clsid,
#     _In_opt_ IUnknown     *            punkOuter,
#     _In_ DWORD                         dwClsCtx,
#     _In_opt_ COSERVERINFO *            pServerInfo,
#     _In_ DWORD                         dwCount,
#     _Inout_updates_(dwCount) MULTI_QI *pResults )
# {
#     return CoCreateInstanceFromApp(Clsid, punkOuter, dwClsCtx, pServerInfo, dwCount, pResults);
CoCreateInstanceEx = ole32.CoCreateInstanceEx
CoCreateInstanceEx.restype = HRESULT

# WINAPI_PARTITION_APP and !(WINAPI_PARTITION_DESKTOP |
# WINAPI_PARTITION_SYSTEM)
# Call related APIs
# DCOM

# _Check_return_ WINOLEAPI
# CoGetCancelObject(
#     _In_ DWORD dwThreadId,
#     _In_ REFIID iid,
#     _Outptr_ VOID** ppUnk
#     );
CoGetCancelObject = ole32.CoGetCancelObject
CoGetCancelObject.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoSetCancelObject(
#     _In_opt_ IUnknown* pUnk
#     );
CoSetCancelObject = ole32.CoSetCancelObject
CoSetCancelObject.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoCancelCall(
#     _In_ DWORD dwThreadId,
#     _In_ ULONG ulTimeout
#     );
CoCancelCall = ole32.CoCancelCall
CoCancelCall.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoTestCancel(
#     VOID
#     );
CoTestCancel = ole32.CoTestCancel
CoTestCancel.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoEnableCallCancellation(
#     _In_opt_ LPVOID pReserved
#     );
CoEnableCallCancellation = ole32.CoEnableCallCancellation
CoEnableCallCancellation.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CoDisableCallCancellation(
#     _In_opt_ LPVOID pReserved
#     );
CoDisableCallCancellation = ole32.CoDisableCallCancellation
CoDisableCallCancellation.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# other helpers

# _Check_return_ WINOLEAPI
# StringFromCLSID(
#     _In_ REFCLSID rclsid,
#     _Outptr_ LPOLESTR  FAR * lplpsz
#     );
StringFromCLSID = ole32.StringFromCLSID
StringFromCLSID.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CLSIDFromString(
#     _In_ LPCOLESTR lpsz,
#     _Out_ LPCLSID pclsid
#     );
CLSIDFromString = ole32.CLSIDFromString
CLSIDFromString.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# StringFromIID(
#     _In_ REFIID rclsid,
#     _Outptr_ LPOLESTR  FAR * lplpsz
#     );
StringFromIID = ole32.StringFromIID
StringFromIID.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# IIDFromString(
#     _In_ LPCOLESTR lpsz,
#     _Out_ LPIID lpiid
#     );
IIDFromString = ole32.IIDFromString
IIDFromString.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI
# ProgIDFromCLSID(
#     _In_ REFCLSID clsid,
#     _Outptr_ LPOLESTR  FAR * lplpszProgID
#     );
ProgIDFromCLSID = ole32.ProgIDFromCLSID
ProgIDFromCLSID.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CLSIDFromProgID(
#     _In_ LPCOLESTR lpszProgID,
#     _Out_ LPCLSID lpclsid
#     );
CLSIDFromProgID = ole32.CLSIDFromProgID
CLSIDFromProgID.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

# _Check_return_ WINOLEAPI_(INT)
# StringFromGUID2(
#     _In_ REFGUID rguid,
#     _Out_writes_to_(cchMax,return) LPOLESTR lpsz,
#     _In_ INT cchMax
#     );
StringFromGUID2 = ole32.StringFromGUID2
StringFromGUID2.restype = WINOLEAPI_(INT)


# _Check_return_ WINOLEAPI
# CoCreateGuid(
#     _Out_ GUID  FAR * pguid
#     );
CoCreateGuid = ole32.CoCreateGuid
CoCreateGuid.restype = WINOLEAPI

# Prop variant support

# WINOLEAPI
# PropVariantCopy(
#     _Out_ PROPVARIANT* pvarDest,
#     _In_ PROPVARIANT* pvarSrc
#     );
PropVariantCopy = ole32.PropVariantCopy
PropVariantCopy.restype = WINOLEAPI


# WINOLEAPI
# PropVariantClear(
#     _Inout_ PROPVARIANT* pvar
#     );
PropVariantClear = ole32.PropVariantClear
PropVariantClear.restype = WINOLEAPI


# WINOLEAPI
# FreePropVariantArray(
#     _In_ ULONG cVariants,
#     _Inout_updates_(cVariants) PROPVARIANT* rgvars
#     );
FreePropVariantArray = ole32.FreePropVariantArray
FreePropVariantArray.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
# DCOM
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# DCOM
# DCOM
# Synchronization API

# _Check_return_ WINOLEAPI
# CoWaitForMultipleHandles(
#     _In_ DWORD dwFlags,
#     _In_ DWORD dwTimeout,
#     _In_ ULONG cHandles,
#     _In_reads_(cHandles) LPHANDLE pHandles,
#     _Out_ LPDWORD lpdwindex
#     );
CoWaitForMultipleHandles = ole32.CoWaitForMultipleHandles
CoWaitForMultipleHandles.restype = WINOLEAPI


# Flags for Synchronization API and Classes
class tagCOWAIT_FLAGS(ENUM):
    COWAIT_DEFAULT = 0
    COWAIT_WAITALL = 1
    COWAIT_ALERTABLE = 2
    COWAIT_INPUTAVAILABLE = 4
    COWAIT_DISPATCH_CALLS = 8
    COWAIT_DISPATCH_WINDOW_MESSAGES = 0x10


COWAIT_FLAGS = tagCOWAIT_FLAGS


class CWMO_FLAGS(ENUM):
    CWMO_DEFAULT = 0
    CWMO_DISPATCH_CALLS = 1
    CWMO_DISPATCH_WINDOW_MESSAGES = 2


# WINOLEAPI
# CoWaitForMultipleObjects(
#     _In_ DWORD dwFlags,
#     _In_ DWORD dwTimeout,
#     _In_ ULONG cHandles,
#     _In_reads_(cHandles) HANDLE* pHandles,
#     _Out_ LPDWORD lpdwindex
#     );
# CoWaitForMultipleObjects = ole32.CoWaitForMultipleObjects
# CoWaitForMultipleObjects.restype = WINOLEAPI

# (NTDDI_VERSION >= NTDDI_WIN8)
CWMO_MAX_HANDLES = 0x00000038
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# DCOM

# _Check_return_ WINOLEAPI
# CoGetTreatAsClass(
#     _In_ REFCLSID clsidOld,
#     _Out_ LPCLSID pClsidNew
#     );
CoGetTreatAsClass = ole32.CoGetTreatAsClass
CoGetTreatAsClass.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# for flushing OLESCM remote binding handles

# _Check_return_ WINOLEAPI
# CoInvalidateRemoteMachineBindings(
#     _In_ LPOLESTR pszMachineName
#     );
CoInvalidateRemoteMachineBindings = ole32.CoInvalidateRemoteMachineBindings
CoInvalidateRemoteMachineBindings.restype = WINOLEAPI


# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
class AgileReferenceOptions(ENUM):
    AGILEREFERENCE_DEFAULT = 0
    AGILEREFERENCE_DELAYEDMARSHAL = 1


# _Check_return_ WINOLEAPI
# RoGetAgileReference(
#     _In_ enum AgileReferenceOptions options,
#     _In_ REFIID riid,
#     _In_ IUnknown* pUnk,
#     _COM_Outptr_ IAgileReference** ppAgileReference
#     );
# RoGetAgileReference = ole32.RoGetAgileReference
# RoGetAgileReference.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
# the server dlls must define their DllGetClassObject and DllCanUnloadNow
# * to match these; the typedefs are located here to ensure all are changed at
# * the same time.

from ctypes import CFUNCTYPE
LPFNGETCLASSOBJECT = CFUNCTYPE(HRESULT, REFCLSID, REFIID, LPVOID)
LPFNCANUNLOADNOW = CFUNCTYPE(HRESULT)

# STDAPI  DllGetClassObject(_In_ REFCLSID rclsid, _In_ REFIID riid, _Outptr_ LPVOID FAR* ppv);
DllGetClassObject = ole32.DllGetClassObject
DllGetClassObject.restype = STDAPI


# STDAPI  DllCanUnloadNow(VOID);
# DllCanUnloadNow = ole32.DllCanUnloadNow
# DllCanUnloadNow.restype = STDAPI

# ***** Default Memory Allocation *****************************************

# WINOLEAPI_(_Ret_opt_ _Post_writable_byte_size_(cb)  __drv_allocatesMem(Mem) _Check_return_ LPVOID)
# CoTaskMemAlloc(
#     _In_ SIZE_T cb
#     );
CoTaskMemAlloc = ole32.CoTaskMemAlloc
CoTaskMemAlloc.restype = LPVOID


# WINOLEAPI_(_Ret_opt_ _Post_writable_byte_size_(cb)  _When_(cb > 0, __drv_allocatesMem(Mem) _Check_return_) LPVOID)
# CoTaskMemRealloc(
#     _Pre_maybenull_ __drv_freesMem(Mem) _Post_invalid_ LPVOID pv,
#     _In_ SIZE_T cb
#     );
CoTaskMemRealloc = ole32.CoTaskMemRealloc
CoTaskMemRealloc.restype = WINOLEAPI_(LPVOID)


# WINOLEAPI_(VOID)
# CoTaskMemFree(
#     _Frees_ptr_opt_ LPVOID pv
#     );
CoTaskMemFree = ole32.CoTaskMemFree
CoTaskMemFree.restype = WINOLEAPI_(VOID)

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

# WINOLEAPI
# CoFileTimeNow(
#     _Out_ FILETIME  FAR * lpFileTime
#     );
CoFileTimeNow = ole32.CoFileTimeNow
CoFileTimeNow.restype = WINOLEAPI


# _Check_return_ WINOLEAPI
# CLSIDFromProgIDEx(
#     _In_ LPCOLESTR lpszProgID,
#     _Out_ LPCLSID lpclsid
#     );
CLSIDFromProgIDEx = ole32.CLSIDFromProgIDEx
CLSIDFromProgIDEx.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# RC_INVOKED
# from poppack_h import * # NOQA
# __COMBASEAPI_H__

__all__ = (
    'DECLARE_INTERFACE_', 'STDMETHODV', 'IFACEMETHOD_', 'THIS',
    'IFACEMETHODV', '_WIN32_WINNT', 'STDMETHOD', 'COM_RIGHTS_ACTIVATE_REMOTE',
    'CLSCTX_ALL', 'CLSCTX_SERVER', 'FARSTRUCT', 'WINOLEAPI_', 'STDMETHOD_',
    'COM_RIGHTS_ACTIVATE_LOCAL', 'IFACEMETHODV_', 'CONST_VTBL', 'WINOLEAPI',
    'DECLARE_INTERFACE_IID_', 'DECLARE_INTERFACE_IID', 'ULISet32', 'LISet32',
    'CWMO_MAX_HANDLES', 'CLSCTX_INPROC',
    'STDMETHODV_', 'DECLARE_INTERFACE', 'IID_PPV_ARGS', 'IFACEMETHOD', 'PURE',
    'COM_RIGHTS_EXECUTE_REMOTE', 'COM_RIGHTS_EXECUTE', 'HUGEP', 'REGCLS',
    'COM_RIGHTS_EXECUTE_LOCAL', 'tagCOINITBASE', 'CWMO_FLAGS', 'STDMSHLFLAGS',
    'tagCOWAIT_FLAGS', 'AgileReferenceOptions', 'COWAIT_FLAGS', 'COINITBASE',
    'tagSTDMSHLFLAGS', 'tagREGCLS', 'tagServerInformation', 'PROPVARIANT',
    'ServerInformation', 'PServerInformation', 'LPFNCANUNLOADNOW',
    'CoRegisterPSClsid', 'CoFileTimeNow', 'IIDFromString',
    'CoMarshalInterThreadInterfaceInStream', 'CoGetStdMarshalEx',
    'CoUnmarshalHresult', 'CoSetCancelObject',
    'CoDisconnectContext', 'CreateStreamOnHGlobal', 'CoCreateGuid',
    'CoSuspendClassObjects', 'CoTestCancel',
    'CoRevokeClassObject', 'CoInitializeSecurity', 'CoGetCurrentProcess',
    'CoDisconnectObject', 'CoGetCallerTID', 'CoRevertToSelf', 'StringFromIID',
    'CLSIDFromProgIDEx', 'CoSetProxyBlanket',
    'CoRegisterSurrogate', 'StringFromCLSID',
    'CoFreeUnusedLibrariesEx', 'CoGetInterfaceAndReleaseStream',
    'CoRegisterClassObject', 'CoLockObjectExternal', 'CoGetCancelObject',
    'CoCreateInstanceEx', 'CoQueryAuthenticationServices', 'CoInitializeEx',
    'CoGetContextToken', 'CoDisableCallCancellation', 'CoMarshalInterface',
    'CoUninitialize', 'CoQueryClientBlanket',
    'FreePropVariantArray', 'CoGetCurrentLogicalThreadId',
    'CoEnableCallCancellation', 'CoResumeClassObjects',
    'CoAddRefServerProcess', 'CoCopyProxy', 'CoGetMalloc',
    'CLSIDFromString', 'ProgIDFromCLSID', 'CoWaitForMultipleHandles',
    'CoQueryProxyBlanket', 'CoCreateInstance', 'CoTaskMemRealloc',
    'CoGetObjectContext', 'CoUnmarshalInterface', 'CoGetCallContext',
    'CoFreeUnusedLibraries', 'CoSwitchCallContext', 'GetHGlobalFromStream',
    'CoReleaseServerProcess', 'CoTaskMemFree', 'CoCancelCall', 'CoGetPSClsid',
    'CoImpersonateClient', 'CoGetMarshalSizeMax', 'CoMarshalHresult',
    'CoIsHandlerConnected', 'CoGetTreatAsClass', 'CoGetClassObject',
    'CoGetApartmentType', 'CoInvalidateRemoteMachineBindings',
    'CoGetStandardMarshal', 'PropVariantClear', 'PropVariantCopy',
    'CoCreateFreeThreadedMarshaler', 'DllGetClassObject', 'CoTaskMemAlloc',
    'CLSIDFromProgID', 'CoGetDefaultContext', 'CoReleaseMarshalData',
)

