__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import * # NOQA
# from .rpcndr_h import * # NOQA
# from .windows_h import * # NOQA
# from .ole2_h import * # NOQA

from .unknwn_h import (
    IClassFactory
)

from .wtypes_h import (
    ENUM,
    BYTE,
    POINTER,
    DWORD,
    HRESULT,
    LPVOID,
    LPCWSTR,
    HANDLE_PTR,
    LONG,
    ULONG,
    REFIID,
    DWORD_PTR,
    LPSTR,
    VOID,
    LPWSTR,
    LPDWORD,
    HANDLE,
    REFGUID,
    HWND,
    CLSID,
    BOOL,
    LPOLESTR,
    LARGE_INTEGER,
    ULARGE_INTEGER,
    WCHAR,
    BSTR,
    REFCLSID,
    VARIANT_BOOL,
    SYSTEMTIME,
    SECURITY_ATTRIBUTES,
    TEXT,
    NULL,
    OLESTR
)
from .guiddef_h import (
    IID,
)
import ctypes
import comtypes


STDAPI = HRESULT
urlmon = ctypes.windll.Urlmon


IID_IPersistMoniker = IID(
    '{79eac9c9-baf9-11ce-8c82-00aa004ba90b}'
)


class IPersistMoniker(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPersistMoniker
    _idlflags_ = []


IID_IMonikerProp = IID(
    '{a5ca5f7f-1847-4d87-9c5b-918509f7511d}'
)


class IMonikerProp(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMonikerProp
    _idlflags_ = []


IID_IBindProtocol = IID(
    '{79eac9cd-baf9-11ce-8c82-00aa004ba90b}'
)


class IBindProtocol(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IBindProtocol
    _idlflags_ = []


IID_IBinding = IID(
    '{79eac9c0-baf9-11ce-8c82-00aa004ba90b}'
)


class IBinding(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IBinding
    _idlflags_ = []


IID_IBindStatusCallback = IID(
    '{79eac9c1-baf9-11ce-8c82-00aa004ba90b}'
)


class IBindStatusCallback(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IBindStatusCallback
    _idlflags_ = []


IID_IBindStatusCallbackEx = IID(
    '{aaa74ef9-8ee7-4659-88d9-f8c504da73cc}'
)


class IBindStatusCallbackEx(IBindStatusCallback):
    _case_insensitive_ = True
    _iid_ = IID_IBindStatusCallbackEx
    _idlflags_ = []


IID_IAuthenticate = IID(
    '{79eac9d0-baf9-11ce-8c82-00aa004ba90b}'
)


class IAuthenticate(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAuthenticate
    _idlflags_ = []


IID_IAuthenticateEx = IID(
    '{2ad1edaf-d83d-48b5-9adf-03dbe19f53bd}'
)


class IAuthenticateEx(IAuthenticate):
    _case_insensitive_ = True
    _iid_ = IID_IAuthenticateEx
    _idlflags_ = []


IID_IHttpNegotiate = IID(
    '{79eac9d2-baf9-11ce-8c82-00aa004ba90b}'
)


class IHttpNegotiate(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHttpNegotiate
    _idlflags_ = []


IID_IHttpNegotiate2 = IID(
    '{4F9F9FCB-E0F4-48eb-B7AB-FA2EA9365CB4}'
)


class IHttpNegotiate2(IHttpNegotiate):
    _case_insensitive_ = True
    _iid_ = IID_IHttpNegotiate2
    _idlflags_ = []


IID_IHttpNegotiate3 = IID(
    '{57b6c80a-34c2-4602-bc26-66a02fc57153}'
)


class IHttpNegotiate3(IHttpNegotiate2):
    _case_insensitive_ = True
    _iid_ = IID_IHttpNegotiate3
    _idlflags_ = []


IID_IWinInetFileStream = IID(
    '{F134C4B7-B1F8-4e75-B886-74B90943BECB}'
)


class IWinInetFileStream(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IWinInetFileStream
    _idlflags_ = []


IID_IWindowForBindingUI = IID(
    '{79eac9d5-bafa-11ce-8c82-00aa004ba90b}'
)


class IWindowForBindingUI(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IWindowForBindingUI
    _idlflags_ = []


IID_ICodeInstall = IID(
    '{79eac9d1-baf9-11ce-8c82-00aa004ba90b}'
)


class ICodeInstall(IWindowForBindingUI):
    _case_insensitive_ = True
    _iid_ = IID_ICodeInstall
    _idlflags_ = []


IID_IUri = IID(
    '{A39EE748-6A27-4817-A6F2-13914BEF5890}'
)


class IUri(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IUri
    _idlflags_ = []


IID_IUriContainer = IID(
    '{a158a630-ed6f-45fb-b987-f68676f57752}'
)


class IUriContainer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IUriContainer
    _idlflags_ = []


IID_IUriBuilder = IID(
    '{4221B2E1-8955-46c0-BD5B-DE9897565DE7}'
)


class IUriBuilder(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IUriBuilder
    _idlflags_ = []


IID_IUriBuilderFactory = IID(
    '{E982CE48-0B96-440c-BC37-0C869B27A29E}'
)


class IUriBuilderFactory(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IUriBuilderFactory
    _idlflags_ = []


IID_IWinInetInfo = IID(
    '{79eac9d6-bafa-11ce-8c82-00aa004ba90b}'
)


class IWinInetInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IWinInetInfo
    _idlflags_ = []


IID_IHttpSecurity = IID(
    '{79eac9d7-bafa-11ce-8c82-00aa004ba90b}'
)


class IHttpSecurity(IWindowForBindingUI):
    _case_insensitive_ = True
    _iid_ = IID_IHttpSecurity
    _idlflags_ = []


IID_IWinInetHttpInfo = IID(
    '{79eac9d8-bafa-11ce-8c82-00aa004ba90b}'
)


class IWinInetHttpInfo(IWinInetInfo):
    _case_insensitive_ = True
    _iid_ = IID_IWinInetHttpInfo
    _idlflags_ = []


IID_IWinInetHttpTimeouts = IID(
    '{F286FA56-C1FD-4270-8E67-B3EB790A81E8}'
)


class IWinInetHttpTimeouts(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IWinInetHttpTimeouts
    _idlflags_ = []


IID_IWinInetCacheHINTs = IID(
    '{DD1EC3B3-8391-4fdb-A9E6-347C3CAAA7DD}'
)


class IWinInetCacheHINTs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IWinInetCacheHINTs
    _idlflags_ = []


IID_IWinInetCacheHINTs2 = IID(
    '{7857AEAC-D31F-49bf-884E-DD46DF36780A}'
)


class IWinInetCacheHINTs2(IWinInetCacheHINTs):
    _case_insensitive_ = True
    _iid_ = IID_IWinInetCacheHINTs2
    _idlflags_ = []


IID_IBindHost = IID(
    '{fc4801a1-2ba9-11cf-a229-00aa003d7352}'
)


class IBindHost(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IBindHost
    _idlflags_ = []


IID_IInternet = IID(
    '{79eac9e0-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternet(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternet
    _idlflags_ = []


IID_IInternetBindInfo = IID(
    '{79eac9e1-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetBindInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetBindInfo
    _idlflags_ = []


IID_IInternetBindInfoEx = IID(
    '{a3e015b7-a82c-4dcd-a150-569aeeed36ab}'
)


class IInternetBindInfoEx(IInternetBindInfo):
    _case_insensitive_ = True
    _iid_ = IID_IInternetBindInfoEx
    _idlflags_ = []


IID_IInternetProtocolRoot = IID(
    '{79eac9e3-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetProtocolRoot(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetProtocolRoot
    _idlflags_ = []


IID_IInternetProtocol = IID(
    '{79eac9e4-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetProtocol(IInternetProtocolRoot):
    _case_insensitive_ = True
    _iid_ = IID_IInternetProtocol
    _idlflags_ = []


IID_IInternetProtocolEx = IID(
    '{C7A98E66-1010-492c-A1C8-C809E1F75905}'
)


class IInternetProtocolEx(IInternetProtocol):
    _case_insensitive_ = True
    _iid_ = IID_IInternetProtocolEx
    _idlflags_ = []


IID_IInternetProtocolSink = IID(
    '{79eac9e5-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetProtocolSink(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetProtocolSink
    _idlflags_ = []


IID_IInternetProtocolSinkStackable = IID(
    '{79eac9f0-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetProtocolSinkStackable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetProtocolSinkStackable
    _idlflags_ = []


IID_IInternetSession = IID(
    '{79eac9e7-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetSession(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetSession
    _idlflags_ = []


IID_IInternetThreadSwitch = IID(
    '{79eac9e8-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetThreadSwitch(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetThreadSwitch
    _idlflags_ = []


IID_IInternetPriority = IID(
    '{79eac9eb-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetPriority(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetPriority
    _idlflags_ = []


IID_IInternetProtocolInfo = IID(
    '{79eac9ec-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetProtocolInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetProtocolInfo
    _idlflags_ = []


IID_IInternetSecurityMgrSite = IID(
    '{79eac9ed-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetSecurityMgrSite(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetSecurityMgrSite
    _idlflags_ = []


IID_IInternetSecurityManager = IID(
    '{79eac9ee-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetSecurityManager(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetSecurityManager
    _idlflags_ = []


IID_IInternetSecurityManagerEx = IID(
    '{F164EDF1-CC7C-4f0d-9A94-34222625C393}'
)


class IInternetSecurityManagerEx(IInternetSecurityManager):
    _case_insensitive_ = True
    _iid_ = IID_IInternetSecurityManagerEx
    _idlflags_ = []


IID_IInternetSecurityManagerEx2 = IID(
    '{F1E50292-A795-4117-8E09-2B560A72AC60}'
)


class IInternetSecurityManagerEx2(IInternetSecurityManagerEx):
    _case_insensitive_ = True
    _iid_ = IID_IInternetSecurityManagerEx2
    _idlflags_ = []


IID_IZoneIdentifier = IID(
    '{cd45f185-1b21-48e2-967b-ead743a8914e}'
)


class IZoneIdentifier(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IZoneIdentifier
    _idlflags_ = []


IID_IZoneIdentifier2 = IID(
    '{EB5E760C-09EF-45C0-B510-70830CE31E6A}'
)


class IZoneIdentifier2(IZoneIdentifier):
    _case_insensitive_ = True
    _iid_ = IID_IZoneIdentifier2
    _idlflags_ = []


IID_IInternetHostSecurityManager = IID(
    '{3af280b6-cb3f-11d0-891e-00c04fb6bfc4}'
)


class IInternetHostSecurityManager(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetHostSecurityManager
    _idlflags_ = []


IID_IInternetZoneManager = IID(
    '{79eac9ef-baf9-11ce-8c82-00aa004ba90b}'
)


class IInternetZoneManager(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternetZoneManager
    _idlflags_ = []


IID_IInternetZoneManagerEx = IID(
    '{A4C23339-8E06-431e-9BF4-7E711C085648}'
)


class IInternetZoneManagerEx(IInternetZoneManager):
    _case_insensitive_ = True
    _iid_ = IID_IInternetZoneManagerEx
    _idlflags_ = []


IID_IInternetZoneManagerEx2 = IID(
    '{EDC17559-DD5D-4846-8EEF-8BECBA5A4ABF}'
)


class IInternetZoneManagerEx2(IInternetZoneManagerEx):
    _case_insensitive_ = True
    _iid_ = IID_IInternetZoneManagerEx2
    _idlflags_ = []


IID_ISoftDistExt = IID(
    '{B15B8DC1-C7E1-11d0-8680-00AA00BDCB71}'
)


class ISoftDistExt(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISoftDistExt
    _idlflags_ = []


IID_ICatalogFileInfo = IID(
    '{711C7600-6B48-11d1-B403-00AA00B92AF1}'
)


class ICatalogFileInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICatalogFileInfo
    _idlflags_ = []


IID_IDataFilter = IID(
    '{69d14c80-c18e-11d0-a9ce-006097942311}'
)


class IDataFilter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDataFilter
    _idlflags_ = []


IID_IEncodingFilterFactory = IID(
    '{70bdde00-c18e-11d0-a9ce-006097942311}'
)


class IEncodingFilterFactory(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEncodingFilterFactory
    _idlflags_ = []


IID_IWrappedProtocol = IID(
    '{53c84785-8425-4dc5-971b-e58d9c19f9b6}'
)


class IWrappedProtocol(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IWrappedProtocol
    _idlflags_ = []


IID_IGetBindHandle = IID(
    '{AF0FF408-129D-4b20-91F0-02BD23D88352}'
)


class IGetBindHandle(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IGetBindHandle
    _idlflags_ = []


IID_IBindCallbackRedirect = IID(
    '{11C81BC2-121E-4ed5-B9C4-B430BD54F2C0}'
)


class IBindCallbackRedirect(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IBindCallbackRedirect
    _idlflags_ = []


IID_IBindHttpSecurity = IID(
    '{a9eda967-f50e-4a33-b358-206f6ef3086d}'
)


class IBindHttpSecurity(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IBindHttpSecurity
    _idlflags_ = []


from .objidl_h import * # NOQA
from .oleidl_h import * # NOQA
# from .servprov_h import * # NOQA
# from .msxml_h import * # NOQA
from .winapifamily_h import * # NOQA

INVALID_P_ROOT_SECURITY_ID = -1
SZ_URLCONTEXT = OLESTR("URL Context")
SZ_ASYNC_CALLEE = OLESTR("AsyncCallee")
MKSYS_URLMONIKER = 0x6
URL_MK_LEGACY = 0x0
URL_MK_UNIFORM = 0x1
URL_MK_NO_CANONICALIZE = 0x2


# STDAPI CreateURLMoniker(_In_opt_ LPMONIKER pMkCtx, _In_ LPCWSTR szURL, _Outptr_ LPMONIKER FAR * ppmk);
CreateURLMoniker = urlmon.CreateURLMoniker
CreateURLMoniker.restype = STDAPI


# STDAPI CreateURLMonikerEx(_In_opt_ LPMONIKER pMkCtx, _In_ LPCWSTR szURL, _Outptr_ LPMONIKER FAR * ppmk, DWORD dwFlags);
CreateURLMonikerEx = urlmon.CreateURLMonikerEx
CreateURLMonikerEx.restype = STDAPI


# STDAPI GetClassURL(_In_ LPCWSTR szURL, _Out_ CLSID *pClsID);
GetClassURL = urlmon.GetClassURL
GetClassURL.restype = STDAPI


# STDAPI CreateAsyncBindCtx(DWORD reserved, _In_ IBindStatusCallback *pBSCb,
#                                 _In_opt_ IEnumFORMATETC *pEFetc, _Outptr_ IBindCtx **ppBC);
CreateAsyncBindCtx = urlmon.CreateAsyncBindCtx
CreateAsyncBindCtx.restype = STDAPI


# STDAPI CreateURLMonikerEx2(_In_opt_ LPMONIKER pMkCtx, _In_ IUri* pUri, _Outptr_ LPMONIKER FAR * ppmk, DWORD dwFlags);
CreateURLMonikerEx2 = urlmon.CreateURLMonikerEx2
CreateURLMonikerEx2.restype = STDAPI


# STDAPI CreateAsyncBindCtxEx(_In_ IBindCtx *pbc, DWORD dwOptions, _In_ IBindStatusCallback *pBSCb, _In_opt_ IEnumFORMATETC *pEnum,
#                             _Outptr_ IBindCtx **ppBC, DWORD reserved);
CreateAsyncBindCtxEx = urlmon.CreateAsyncBindCtxEx
CreateAsyncBindCtxEx.restype = STDAPI


# STDAPI MkParseDisplayNameEx(_In_ IBindCtx *pbc, _In_ LPCWSTR szDisplayName, _Out_ _Out_range_(<=, _String_length_(szDisplayName)) ULONG *pchEaten,
#                                 _Outptr_ LPMONIKER *ppmk);
MkParseDisplayNameEx = urlmon.MkParseDisplayNameEx
MkParseDisplayNameEx.restype = STDAPI


# STDAPI RegisterBindStatusCallback(_In_ LPBC pBC, _In_ IBindStatusCallback *pBSCb,
#                                 _Outptr_ IBindStatusCallback**  ppBSCBPrev, DWORD dwReserved);
RegisterBindStatusCallback = urlmon.RegisterBindStatusCallback
RegisterBindStatusCallback.restype = STDAPI


# STDAPI RevokeBindStatusCallback(_In_ LPBC pBC, _In_ IBindStatusCallback *pBSCb);
RevokeBindStatusCallback = urlmon.RevokeBindStatusCallback
RevokeBindStatusCallback.restype = STDAPI


# STDAPI GetClassFileOrMime(_In_opt_ LPBC pBC, _In_opt_ LPCWSTR szFilename, _In_reads_bytes_opt_(cbSize) LPVOID pBuffer, DWORD cbSize, _In_opt_ LPCWSTR szMime, DWORD dwReserved, _Out_ CLSID *pclsid);
GetClassFileOrMime = urlmon.GetClassFileOrMime
GetClassFileOrMime.restype = STDAPI


# STDAPI IsValidURL(_In_opt_ LPBC pBC, _In_ LPCWSTR szURL, DWORD dwReserved);
IsValidURL = urlmon.IsValidURL
IsValidURL.restype = STDAPI


# STDAPI CoGetClassObjectFromURL( _In_ REFCLSID rCLASSID,
#             _In_ LPCWSTR szCODE, DWORD dwFileVersionMS,
#             DWORD dwFileVersionLS, _In_ LPCWSTR szTYPE,
#             _In_ LPBINDCTX pBindCtx, DWORD dwClsContext,
#             _Reserved_ LPVOID pvReserved, REFIID riid, _Outptr_ LPVOID * ppv);
CoGetClassObjectFromURL = urlmon.CoGetClassObjectFromURL
CoGetClassObjectFromURL.restype = STDAPI


# STDAPI IEInstallScope(_Out_ LPDWORD pdwScope);
IEInstallScope = urlmon.IEInstallScope
IEInstallScope.restype = STDAPI


# STDAPI FaultInIEFeature( HWND hWnd,
#             _In_ uCLSSPEC *pClassSpec,
#             _Inout_opt_ QUERYCONTEXT *pQuery, DWORD dwFlags);
FaultInIEFeature = urlmon.FaultInIEFeature
FaultInIEFeature.restype = STDAPI


# STDAPI GetComponentIDFromCLSSPEC(_In_ uCLSSPEC *pClassspec,
#             _Outptr_ LPSTR * ppszComponentID);
GetComponentIDFromCLSSPEC = urlmon.GetComponentIDFromCLSSPEC
GetComponentIDFromCLSSPEC.restype = STDAPI


FIEF_FLAG_FORCE_JITUI = 0x1
FIEF_FLAG_PEEK = 0x2
FIEF_FLAG_SKIP_INSTALLED_VERSION_CHECK = 0x4
FIEF_FLAG_RESERVED_0 = 0x8



# STDAPI IsAsyncMoniker(_In_ IMoniker* pmk);
IsAsyncMoniker = urlmon.IsAsyncMoniker
IsAsyncMoniker.restype = STDAPI


# STDAPI CreateURLBinding(LPCWSTR lpszUrl, _In_ IBindCtx *pbc, _Inout_ IBinding **ppBdg);
# CreateURLBinding = urlmon.CreateURLBinding
# CreateURLBinding.restype = STDAPI


# STDAPI RegisterMediaTypes(_In_ _In_range_(>, 0) UINT ctypes, _In_reads_(ctypes) LPCSTR* rgszTypes, _Out_writes_(ctypes) CLIPFORMAT* rgcfTypes);
RegisterMediaTypes = urlmon.RegisterMediaTypes
RegisterMediaTypes.restype = STDAPI


# STDAPI FindMediaType(_In_ LPCSTR rgszTypes, _Out_ CLIPFORMAT* rgcfTypes);
FindMediaType = urlmon.FindMediaType
FindMediaType.restype = STDAPI


# STDAPI CreateFormatEnumerator( _In_ _In_range_(>, 0) UINT cfmtetc, _In_reads_(cfmtetc) FORMATETC* rgfmtetc, _Outptr_ IEnumFORMATETC** ppenumfmtetc);
CreateFormatEnumerator = urlmon.CreateFormatEnumerator
CreateFormatEnumerator.restype = STDAPI


# STDAPI RegisterFormatEnumerator(_In_ LPBC pBC, _In_ IEnumFORMATETC *pEFetc, DWORD reserved);
RegisterFormatEnumerator = urlmon.RegisterFormatEnumerator
RegisterFormatEnumerator.restype = STDAPI


# STDAPI RevokeFormatEnumerator(_In_ LPBC pBC, _In_ IEnumFORMATETC *pEFetc);
RevokeFormatEnumerator = urlmon.RevokeFormatEnumerator
RevokeFormatEnumerator.restype = STDAPI


# STDAPI RegisterMediaTypeClass(_In_ LPBC pBC, _In_ _In_range_(>, 0) UINT ctypes, _In_reads_(ctypes) LPCSTR* rgszTypes, _In_reads_(ctypes)  CLSID *rgclsID, DWORD reserved);
RegisterMediaTypeClass = urlmon.RegisterMediaTypeClass
RegisterMediaTypeClass.restype = STDAPI


# STDAPI FindMediaTypeClass(_In_ LPBC pBC, _In_ LPCSTR szType, _Out_ CLSID *pclsID, DWORD reserved);
FindMediaTypeClass = urlmon.FindMediaTypeClass
FindMediaTypeClass.restype = STDAPI


# STDAPI UrlMkSetSessionOption(DWORD dwOption, _In_reads_bytes_opt_(dwBufferLength) LPVOID pBuffer, DWORD dwBufferLength, _Reserved_ DWORD dwReserved);
UrlMkSetSessionOption = urlmon.UrlMkSetSessionOption
UrlMkSetSessionOption.restype = STDAPI


# STDAPI UrlMkGetSessionOption(DWORD dwOption, _Out_writes_bytes_to_opt_(dwBufferLength,*pdwBufferLengthOut) LPVOID pBuffer, DWORD dwBufferLength, _Out_ DWORD *pdwBufferLengthOut, _Reserved_ DWORD dwReserved);
UrlMkGetSessionOption = urlmon.UrlMkGetSessionOption
UrlMkGetSessionOption.restype = STDAPI


# STDAPI FindMimeFromData(
#     _In_opt_                     LPBC    pBC,
#     _In_opt_                     LPCWSTR pwzUrl,
#     _In_reads_bytes_opt_(cbSize) LPVOID  pBuffer,
#                                  DWORD   cbSize,
#     _In_opt_                     LPCWSTR pwzMimeProposed,
#                                  DWORD   dwMimeFlags,
#     _Outptr_                     LPWSTR  *ppwzMimeOut,
#     _Reserved_                   DWORD   dwReserved);
FindMimeFromData = urlmon.FindMimeFromData
FindMimeFromData.restype = STDAPI


FMFD_DEFAULT = 0x00000000
FMFD_URLASFILENAME = 0x00000001
FMFD_ENABLEMIMESNIFFING = 0x00000002
FMFD_IGNOREMIMETEXTPLAIN = 0x00000004
FMFD_SERVERMIME = 0x00000008
FMFD_RESPECTTEXTPLAIN = 0x00000010
FMFD_RETURNUPDATEDIMGMIMES = 0x00000020
FMFD_RESERVED_1 = 0x00000040
UAS_EXACTLEGACY = 0x00001000



# STDAPI ObtainUserAgentString(
#                                          DWORD dwOption,
#     _Out_writes_to_(*cbSize, *cbSize)    LPSTR pszUAOut,
#     _Inout_                              DWORD *cbSize);
ObtainUserAgentString = urlmon.ObtainUserAgentString
ObtainUserAgentString.restype = STDAPI


# STDAPI CompareSecurityIds(_In_reads_(dwLen1) BYTE* pbSecurityId1, _In_ DWORD dwLen1, _In_reads_(dwLen2) BYTE* pbSecurityId2, _In_ DWORD dwLen2, _In_ DWORD dwReserved);
CompareSecurityIds = urlmon.CompareSecurityIds
CompareSecurityIds.restype = STDAPI


# STDAPI CompatFlagsFromClsid(_In_ CLSID *pclsid, _Out_ LPDWORD pdwCompatFlags, _Out_ LPDWORD pdwMiscStatusFlags);
CompatFlagsFromClsid = urlmon.CompatFlagsFromClsid
CompatFlagsFromClsid.restype = STDAPI


class IEObjectType(ENUM):
    IE_EPM_OBJECT_EVENT = 0
    IE_EPM_OBJECT_MUTEX = 1
    IE_EPM_OBJECT_SEMAPHORE = 2
    IE_EPM_OBJECT_SHARED_MEMORY = 3
    IE_EPM_OBJECT_WAITABLE_TIMER = 4
    IE_EPM_OBJECT_FILE = 5
    IE_EPM_OBJECT_NAMED_PIPE = 6
    IE_EPM_OBJECT_REGISTRY = 7


# STDAPI SetAccessForIEAppContainer(
#     _In_ HANDLE hObject,
#     _In_ IEObjectType ieObjectType,
#     _In_ DWORD dwAccessMask
#     );
SetAccessForIEAppContainer = urlmon.SetAccessForIEAppContainer
SetAccessForIEAppContainer.restype = STDAPI


URLMON_OPTION_USERAGENT = 0x10000001
URLMON_OPTION_USERAGENT_REFRESH = 0x10000002
URLMON_OPTION_URL_ENCODING = 0x10000004
URLMON_OPTION_USE_BINDSTRINGCREDS = 0x10000008
URLMON_OPTION_USE_BROWSERAPPSDOCUMENTS = 0x10000010
CF_NULL = 0x0
CFSTR_MIME_NULL = NULL
CFSTR_MIME_TEXT = TEXT("text/plain")
CFSTR_MIME_RICHTEXT = TEXT("text/richtext")
CFSTR_MIME_MANIFEST = TEXT("text/cache-manifest")
CFSTR_MIME_WEBVTT = TEXT("text/vtt")
CFSTR_MIME_X_BITMAP = TEXT("image/x-xbitmap")
CFSTR_MIME_POSTSCRIPT = TEXT("application/postscript")
CFSTR_MIME_AIFF = TEXT("audio/aiff")
CFSTR_MIME_BASICAUDIO = TEXT("audio/basic")
CFSTR_MIME_WAV = TEXT("audio/wav")
CFSTR_MIME_X_WAV = TEXT("audio/x-wav")
CFSTR_MIME_GIF = TEXT("image/gif")
CFSTR_MIME_PJPEG = TEXT("image/pjpeg")
CFSTR_MIME_JPEG = TEXT("image/jpeg")
CFSTR_MIME_TIFF = TEXT("image/tiff")
CFSTR_MIME_JPEG_XR = TEXT("image/vnd.ms-photo")
CFSTR_MIME_PNG = TEXT("image/png")
CFSTR_MIME_DDS = TEXT("image/vnd.ms-dds")
CFSTR_MIME_X_PNG = TEXT("image/x-png")
CFSTR_MIME_X_ICON = TEXT("image/x-icon")
CFSTR_MIME_SVG_XML = TEXT("image/svg+xml")
CFSTR_MIME_BMP = TEXT("image/bmp")
CFSTR_MIME_X_EMF = TEXT("image/x-emf")
CFSTR_MIME_X_WMF = TEXT("image/x-wmf")
CFSTR_MIME_AVI = TEXT("video/avi")
CFSTR_MIME_MPEG = TEXT("video/mpeg")
CFSTR_MIME_FRACTALS = TEXT("application/fractals")
CFSTR_MIME_RAWDATA = TEXT("application/octet-stream")
CFSTR_MIME_RAWDATASTRM = TEXT("application/octet-stream")
CFSTR_MIME_PDF = TEXT("application/pdf")
CFSTR_MIME_HTA = TEXT("application/hta")
CFSTR_MIME_APP_XML = TEXT("application/xml")
CFSTR_MIME_XHTML = TEXT("application/xhtml+xml")
CFSTR_MIME_X_AIFF = TEXT("audio/x-aiff")
CFSTR_MIME_X_REALAUDIO = TEXT("audio/x-pn-realaudio")
CFSTR_MIME_XBM = TEXT("image/xbm")
CFSTR_MIME_QUICKTIME = TEXT("video/quicktime")
CFSTR_MIME_X_MSVIDEO = TEXT("video/x-msvideo")
CFSTR_MIME_X_SGI_MOVIE = TEXT("video/x-sgi-movie")
CFSTR_MIME_X_MIXED_REPLACE = TEXT("multipart/x-mixed-replace")
CFSTR_MIME_HTML = TEXT("text/html")
CFSTR_MIME_XML = TEXT("text/xml")
CFSTR_MIME_TTML = TEXT("application/ttml+xml")
CFSTR_MIME_TTAF = TEXT("application/ttaf+xml")
CFSTR_MIME_X_JAVASCRIPT = TEXT("application/x-javascript")
CFSTR_MIME_TEXT_JSON = TEXT("text/json")
CFSTR_MIME_APPLICATION_JAVASCRIPT = TEXT("application/javascript")

def _HRESULT_TYPEDEF_(h):
    return h

MK_S_ASYNCHRONOUS = _HRESULT_TYPEDEF_(0x000401E8)
S_ASYNCHRONOUS = MK_S_ASYNCHRONOUS
E_PENDING = _HRESULT_TYPEDEF_(0x8000000A)
INET_E_INVALID_URL = _HRESULT_TYPEDEF_(0x800C0002)
INET_E_NO_SESSION = _HRESULT_TYPEDEF_(0x800C0003)
INET_E_CANNOT_CONNECT = _HRESULT_TYPEDEF_(0x800C0004)
INET_E_RESOURCE_NOT_FOUND = _HRESULT_TYPEDEF_(0x800C0005)
INET_E_OBJECT_NOT_FOUND = _HRESULT_TYPEDEF_(0x800C0006)
INET_E_DATA_NOT_AVAILABLE = _HRESULT_TYPEDEF_(0x800C0007)
INET_E_DOWNLOAD_FAILURE = _HRESULT_TYPEDEF_(0x800C0008)
INET_E_AUTHENTICATION_REQUIRED = _HRESULT_TYPEDEF_(0x800C0009)
INET_E_NO_VALID_MEDIA = _HRESULT_TYPEDEF_(0x800C000A)
INET_E_CONNECTION_TIMEOUT = _HRESULT_TYPEDEF_(0x800C000B)
INET_E_INVALID_REQUEST = _HRESULT_TYPEDEF_(0x800C000C)
INET_E_UNKNOWN_PROTOCOL = _HRESULT_TYPEDEF_(0x800C000D)
INET_E_SECURITY_PROBLEM = _HRESULT_TYPEDEF_(0x800C000E)
INET_E_CANNOT_LOAD_DATA = _HRESULT_TYPEDEF_(0x800C000F)
INET_E_CANNOT_INSTANTIATE_OBJECT = _HRESULT_TYPEDEF_(0x800C0010)
INET_E_INVALID_CERTIFICATE = _HRESULT_TYPEDEF_(0x800C0019)
INET_E_REDIRECT_FAILED = _HRESULT_TYPEDEF_(0x800C0014)
INET_E_REDIRECT_TO_DIR = _HRESULT_TYPEDEF_(0x800C0015)
INET_E_CANNOT_LOCK_REQUEST = _HRESULT_TYPEDEF_(0x800C0016)
INET_E_USE_EXTEND_BINDING = _HRESULT_TYPEDEF_(0x800C0017)
INET_E_TERMINATED_BIND = _HRESULT_TYPEDEF_(0x800C0018)
INET_E_RESERVED_1 = _HRESULT_TYPEDEF_(0x800C001A)
INET_E_BLOCKED_REDIRECT_XSECURITYID = _HRESULT_TYPEDEF_(0x800C001B)
INET_E_DOMINJECTIONVALIDATION = _HRESULT_TYPEDEF_(0x800C001C)
INET_E_VTAB_SWITCH_FORCE_ENGINE = _HRESULT_TYPEDEF_(0x800C001D)
INET_E_HSTS_CERTIFICATE_ERROR = _HRESULT_TYPEDEF_(0x800C001E)
INET_E_RESERVED_2 = _HRESULT_TYPEDEF_(0x800C001F)
INET_E_RESERVED_3 = _HRESULT_TYPEDEF_(0x800C0020)
INET_E_RESERVED_4 = _HRESULT_TYPEDEF_(0x800C0021)
INET_E_ERROR_FIRST = _HRESULT_TYPEDEF_(0x800C0002)
INET_E_CODE_DOWNLOAD_DECLINED = _HRESULT_TYPEDEF_(0x800C0100)
INET_E_RESULT_DISPATCHED = _HRESULT_TYPEDEF_(0x800C0200)
INET_E_CANNOT_REPLACE_SFP_FILE = _HRESULT_TYPEDEF_(0x800C0300)
INET_E_CODE_INSTALL_SUPPRESSED = _HRESULT_TYPEDEF_(0x800C0400)
INET_E_CODE_INSTALL_BLOCKED_BY_HASH_POLICY = _HRESULT_TYPEDEF_(0x800C0500)
INET_E_DOWNLOAD_BLOCKED_BY_INPRIVATE = _HRESULT_TYPEDEF_(0x800C0501)
INET_E_CODE_INSTALL_BLOCKED_IMMERSIVE = _HRESULT_TYPEDEF_(0x800C0502)
INET_E_FORBIDFRAMING = _HRESULT_TYPEDEF_(0x800C0503)
INET_E_CODE_INSTALL_BLOCKED_ARM = _HRESULT_TYPEDEF_(0x800C0504)
INET_E_BLOCKED_PLUGGABLE_PROTOCOL = _HRESULT_TYPEDEF_(0x800C0505)
INET_E_BLOCKED_ENHANCEDPROTECTEDMODE = _HRESULT_TYPEDEF_(0x800C0506)
INET_E_CODE_INSTALL_BLOCKED_BITNESS = _HRESULT_TYPEDEF_(0x800C0507)
INET_E_DOWNLOAD_BLOCKED_BY_CSP = _HRESULT_TYPEDEF_(0x800C0508)
INET_E_ERROR_LAST = INET_E_DOWNLOAD_BLOCKED_BY_CSP
LPPERSISTMONIKER = POINTER(IPersistMoniker)
COMMETHOD = comtypes.COMMETHOD


IPersistMoniker._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetClassID',
        (['out'], POINTER(CLSID), 'pClassID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Load',
        (['in'], BOOL, 'fFullyAvailable'),
        (['in'], POINTER(IMoniker), 'pimkName'),
        (['in'], LPBC, 'pibc'),
        (['in'], DWORD, 'grfMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Save',
        (['in'], POINTER(IMoniker), 'pimkName'),
        (['in'], LPBC, 'pbc'),
        (['in'], BOOL, 'fRemember'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SaveCompleted',
        (['in'], POINTER(IMoniker), 'pimkName'),
        (['in'], LPBC, 'pibc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurMoniker',
        (['out'], POINTER(POINTER(IMoniker)), 'ppimkName'),
    ),
]


LPMONIKERPROP = POINTER(IMonikerProp)


class __MIDL_IMonikerProp_0001(ENUM):
    MIMETYPEPROP = 0
    USE_SRC_URL = 0x1
    CLASSIDPROP = 0x2
    TRUSTEDDOWNLOADPROP = 0x3
    POPUPLEVELPROP = 0x4


MONIKERPROPERTY = __MIDL_IMonikerProp_0001


IMonikerProp._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'PutProperty',
        (['in'], MONIKERPROPERTY, 'mkp'),
        (['in'], LPCWSTR, 'val'),
    ),
]


LPBINDPROTOCOL = POINTER(IBindProtocol)


IBindProtocol._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateBinding',
        (['in'], LPCWSTR, 'szUrl'),
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['out'], POINTER(POINTER(IBinding)), 'ppb'),
    ),
]


LPBINDING = POINTER(IBinding)


IBinding._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetPriority',
        (['in'], LONG, 'nPriority'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPriority',
        (['out'], POINTER(LONG), 'pnPriority'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBindResult',
        (['out'], POINTER(CLSID), 'pclsidProtocol'),
        (['out'], POINTER(DWORD), 'pdwResult'),
        (['out'], POINTER(LPOLESTR), 'pszResult'),
        (['in', 'out'], POINTER(DWORD), 'pdwReserved'),
    ),
]


LPBINDSTATUSCALLBACK = POINTER(IBindStatusCallback)


class __MIDL_IBindStatusCallback_0001(ENUM):
    BINDVERB_GET = 0
    BINDVERB_POST = 0x1
    BINDVERB_PUT = 0x2
    BINDVERB_CUSTOM = 0x3
    BINDVERB_RESERVED1 = 0x4


BINDVERB = __MIDL_IBindStatusCallback_0001


class __MIDL_IBindStatusCallback_0002(ENUM):
    BINDINFOF_URLENCODESTGMEDDATA = 0x1
    BINDINFOF_URLENCODEDEXTRAINFO = 0x2


BINDINFOF = __MIDL_IBindStatusCallback_0002


class __MIDL_IBindStatusCallback_0003(ENUM):
    BINDF_ASYNCHRONOUS = 0x1
    BINDF_ASYNCSTORAGE = 0x2
    BINDF_NOPROGRESSIVERENDERING = 0x4
    BINDF_OFFLINEOPERATION = 0x8
    BINDF_GETNEWESTVERSION = 0x10
    BINDF_NOWRITECACHE = 0x20
    BINDF_NEEDFILE = 0x40
    BINDF_PULLDATA = 0x80
    BINDF_IGNORESECURITYPROBLEM = 0x100
    BINDF_RESYNCHRONIZE = 0x200
    BINDF_HYPERLINK = 0x400
    BINDF_NO_UI = 0x800
    BINDF_SILENTOPERATION = 0x1000
    BINDF_PRAGMA_NO_CACHE = 0x2000
    BINDF_GETCLASSOBJECT = 0x4000
    BINDF_RESERVED_1 = 0x8000
    BINDF_FREE_THREADED = 0x10000
    BINDF_DIRECT_READ = 0x20000
    BINDF_FORMS_SUBMIT = 0x40000
    BINDF_GETFROMCACHE_IF_NET_FAIL = 0x80000
    BINDF_FROMURLMON = 0x100000
    BINDF_FWD_BACK = 0x200000
    BINDF_PREFERDEFAULTHANDLER = 0x400000
    BINDF_ENFORCERESTRICTED = 0x800000
    BINDF_RESERVED_2 = 0x80000000
    BINDF_RESERVED_3 = 0x1000000
    BINDF_RESERVED_4 = 0x2000000
    BINDF_RESERVED_5 = 0x4000000
    BINDF_RESERVED_6 = 0x8000000
    BINDF_RESERVED_7 = 0x40000000
    BINDF_RESERVED_8 = 0x20000000


BINDF = __MIDL_IBindStatusCallback_0003
BINDF_DONTUSECACHE = BINDF.BINDF_GETNEWESTVERSION
BINDF_DONTPUTINCACHE = BINDF.BINDF_NOWRITECACHE
BINDF_NOCOPYDATA = BINDF.BINDF_PULLDATA

class __MIDL_IBindStatusCallback_0004(ENUM):
    URL_ENCODING_NONE = 0
    URL_ENCODING_ENABLE_UTF8 = 0x10000000
    URL_ENCODING_DISABLE_UTF8 = 0x20000000


URL_ENCODING = __MIDL_IBindStatusCallback_0004


class _tagBINDINFO(ctypes.Structure):
    _fields_ = [
        ('cbSize', ULONG),
        ('szExtraInfo', LPWSTR),
        ('stgmedData', STGMEDIUM),
        ('grfBindInfoF', DWORD),
        ('dwBindVerb', DWORD),
        ('szCustomVerb', LPWSTR),
        ('cbstgmedData', DWORD),
        ('dwOptions', DWORD),
        ('dwOptionsFlags', DWORD),
        ('dwCodePage', DWORD),
        ('securityAttributes', SECURITY_ATTRIBUTES),
        ('iid', IID),
        ('pUnk', POINTER(comtypes.IUnknown)),
        ('dwReserved', DWORD),
    ]


BINDINFO = _tagBINDINFO


class _REMSECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ('nLength', DWORD),
        ('lpSecurityDescriptor', DWORD),
        ('bInheritHandle', BOOL),
    ]


REMSECURITY_ATTRIBUTES = _REMSECURITY_ATTRIBUTES
PREMSECURITY_ATTRIBUTES = POINTER(_REMSECURITY_ATTRIBUTES)
LPREMSECURITY_ATTRIBUTES = POINTER(_REMSECURITY_ATTRIBUTES)


class _tagRemBINDINFO(ctypes.Structure):
    _fields_ = [
        ('cbSize', ULONG),
        ('szExtraInfo', LPWSTR),
        ('grfBindInfoF', DWORD),
        ('dwBindVerb', DWORD),
        ('szCustomVerb', LPWSTR),
        ('cbstgmedData', DWORD),
        ('dwOptions', DWORD),
        ('dwOptionsFlags', DWORD),
        ('dwCodePage', DWORD),
        ('securityAttributes', REMSECURITY_ATTRIBUTES),
        ('iid', IID),
        ('pUnk', POINTER(comtypes.IUnknown)),
        ('dwReserved', DWORD),
    ]


RemBINDINFO = _tagRemBINDINFO


class tagRemFORMATETC(ctypes.Structure):
    _fields_ = [
        ('cfFormat', DWORD),
        ('ptd', DWORD),
        ('dwAspect', DWORD),
        ('lindex', LONG),
        ('tymed', DWORD),
    ]


RemFORMATETC = tagRemFORMATETC
LPREMFORMATETC = POINTER(tagRemFORMATETC)


class __MIDL_IBindStatusCallback_0005(ENUM):
    BINDINFO_OPTIONS_WININETFLAG = 0x10000
    BINDINFO_OPTIONS_ENABLE_UTF8 = 0x20000
    BINDINFO_OPTIONS_DISABLE_UTF8 = 0x40000
    BINDINFO_OPTIONS_USE_IE_ENCODING = 0x80000
    BINDINFO_OPTIONS_BINDTOOBJECT = 0x100000
    BINDINFO_OPTIONS_SECURITYOPTOUT = 0x200000
    BINDINFO_OPTIONS_IGNOREMIMETEXTPLAIN = 0x400000
    BINDINFO_OPTIONS_USEBINDSTRINGCREDS = 0x800000
    BINDINFO_OPTIONS_IGNOREHTTPHTTPSREDIRECTS = 0x1000000
    BINDINFO_OPTIONS_IGNORE_SSLERRORS_ONCE = 0x2000000
    BINDINFO_WPC_DOWNLOADBLOCKED = 0x8000000
    BINDINFO_WPC_LOGGING_ENABLED = 0x10000000
    BINDINFO_OPTIONS_ALLOWCONNECTDATA = 0x20000000
    BINDINFO_OPTIONS_DISABLEAUTOREDIRECTS = 0x40000000
    BINDINFO_OPTIONS_SHDOCVW_NAVIGATE = 0x80000000


BINDINFO_OPTIONS = __MIDL_IBindStatusCallback_0005


class __MIDL_IBindStatusCallback_0006(ENUM):
    BSCF_FIRSTDATANOTIFICATION = 0x1
    BSCF_INTERMEDIATEDATANOTIFICATION = 0x2
    BSCF_LASTDATANOTIFICATION = 0x4
    BSCF_DATAFULLYAVAILABLE = 0x8
    BSCF_AVAILABLEDATASIZEUNKNOWN = 0x10
    BSCF_SKIPDRAINDATAFORFILEURLS = 0x20
    BSCF_64BITLENGTHDOWNLOAD = 0x40


BSCF = __MIDL_IBindStatusCallback_0006


class tagBINDSTATUS(ENUM):
    BINDSTATUS_FINDINGRESOURCE = 1
    BINDSTATUS_CONNECTING = BINDSTATUS_FINDINGRESOURCE + 1
    BINDSTATUS_REDIRECTING = BINDSTATUS_CONNECTING + 1
    BINDSTATUS_BEGINDOWNLOADDATA = BINDSTATUS_REDIRECTING + 1
    BINDSTATUS_DOWNLOADINGDATA = BINDSTATUS_BEGINDOWNLOADDATA + 1
    BINDSTATUS_ENDDOWNLOADDATA = BINDSTATUS_DOWNLOADINGDATA + 1
    BINDSTATUS_BEGINDOWNLOADCOMPONENTS = BINDSTATUS_ENDDOWNLOADDATA + 1
    BINDSTATUS_INSTALLINGCOMPONENTS = BINDSTATUS_BEGINDOWNLOADCOMPONENTS + 1
    BINDSTATUS_ENDDOWNLOADCOMPONENTS = BINDSTATUS_INSTALLINGCOMPONENTS + 1
    BINDSTATUS_USINGCACHEDCOPY = BINDSTATUS_ENDDOWNLOADCOMPONENTS + 1
    BINDSTATUS_SENDINGREQUEST = BINDSTATUS_USINGCACHEDCOPY + 1
    BINDSTATUS_CLASSIDAVAILABLE = BINDSTATUS_SENDINGREQUEST + 1
    BINDSTATUS_MIMETYPEAVAILABLE = BINDSTATUS_CLASSIDAVAILABLE + 1
    BINDSTATUS_CACHEFILENAMEAVAILABLE = BINDSTATUS_MIMETYPEAVAILABLE + 1
    BINDSTATUS_BEGINSYNCOPERATION = BINDSTATUS_CACHEFILENAMEAVAILABLE + 1
    BINDSTATUS_ENDSYNCOPERATION = BINDSTATUS_BEGINSYNCOPERATION + 1
    BINDSTATUS_BEGINUPLOADDATA = BINDSTATUS_ENDSYNCOPERATION + 1
    BINDSTATUS_UPLOADINGDATA = BINDSTATUS_BEGINUPLOADDATA + 1
    BINDSTATUS_ENDUPLOADDATA = BINDSTATUS_UPLOADINGDATA + 1
    BINDSTATUS_PROTOCOLCLASSID = BINDSTATUS_ENDUPLOADDATA + 1
    BINDSTATUS_ENCODING = BINDSTATUS_PROTOCOLCLASSID + 1
    BINDSTATUS_VERIFIEDMIMETYPEAVAILABLE = BINDSTATUS_ENCODING + 1
    BINDSTATUS_CLASSINSTALLLOCATION = BINDSTATUS_VERIFIEDMIMETYPEAVAILABLE + 1
    BINDSTATUS_DECODING = BINDSTATUS_CLASSINSTALLLOCATION + 1
    BINDSTATUS_LOADINGMIMEHANDLER = BINDSTATUS_DECODING + 1
    BINDSTATUS_CONTENTDISPOSITIONATTACH = BINDSTATUS_LOADINGMIMEHANDLER + 1
    BINDSTATUS_FILTERREPORTMIMETYPE = BINDSTATUS_CONTENTDISPOSITIONATTACH + 1
    BINDSTATUS_CLSIDCANINSTANTIATE = BINDSTATUS_FILTERREPORTMIMETYPE + 1
    BINDSTATUS_IUNKNOWNAVAILABLE = BINDSTATUS_CLSIDCANINSTANTIATE + 1
    BINDSTATUS_DIRECTBIND = BINDSTATUS_IUNKNOWNAVAILABLE + 1
    BINDSTATUS_RAWMIMETYPE = BINDSTATUS_DIRECTBIND + 1
    BINDSTATUS_PROXYDETECTING = BINDSTATUS_RAWMIMETYPE + 1
    BINDSTATUS_ACCEPTRANGES = BINDSTATUS_PROXYDETECTING + 1
    BINDSTATUS_COOKIE_SENT = BINDSTATUS_ACCEPTRANGES + 1
    BINDSTATUS_COMPACT_POLICY_RECEIVED = BINDSTATUS_COOKIE_SENT + 1
    BINDSTATUS_COOKIE_SUPPRESSED = BINDSTATUS_COMPACT_POLICY_RECEIVED + 1
    BINDSTATUS_COOKIE_STATE_UNKNOWN = BINDSTATUS_COOKIE_SUPPRESSED + 1
    BINDSTATUS_COOKIE_STATE_ACCEPT = BINDSTATUS_COOKIE_STATE_UNKNOWN + 1
    BINDSTATUS_COOKIE_STATE_REJECT = BINDSTATUS_COOKIE_STATE_ACCEPT + 1
    BINDSTATUS_COOKIE_STATE_PROMPT = BINDSTATUS_COOKIE_STATE_REJECT + 1
    BINDSTATUS_COOKIE_STATE_LEASH = BINDSTATUS_COOKIE_STATE_PROMPT + 1
    BINDSTATUS_COOKIE_STATE_DOWNGRADE = BINDSTATUS_COOKIE_STATE_LEASH + 1
    BINDSTATUS_POLICY_HREF = BINDSTATUS_COOKIE_STATE_DOWNGRADE + 1
    BINDSTATUS_P3P_HEADER = BINDSTATUS_POLICY_HREF + 1
    BINDSTATUS_SESSION_COOKIE_RECEIVED = BINDSTATUS_P3P_HEADER + 1
    BINDSTATUS_PERSISTENT_COOKIE_RECEIVED = (
        BINDSTATUS_SESSION_COOKIE_RECEIVED + 1
    )
    BINDSTATUS_SESSION_COOKIES_ALLOWED = (
        BINDSTATUS_PERSISTENT_COOKIE_RECEIVED + 1
    )
    BINDSTATUS_CACHECONTROL = BINDSTATUS_SESSION_COOKIES_ALLOWED + 1
    BINDSTATUS_CONTENTDISPOSITIONFILENAME = BINDSTATUS_CACHECONTROL + 1
    BINDSTATUS_MIMETEXTPLAINMISMATCH = (
        BINDSTATUS_CONTENTDISPOSITIONFILENAME + 1
    )
    BINDSTATUS_PUBLISHERAVAILABLE = BINDSTATUS_MIMETEXTPLAINMISMATCH + 1
    BINDSTATUS_DISPLAYNAMEAVAILABLE = BINDSTATUS_PUBLISHERAVAILABLE + 1
    BINDSTATUS_SSLUX_NAVBLOCKED = BINDSTATUS_DISPLAYNAMEAVAILABLE + 1
    BINDSTATUS_SERVER_MIMETYPEAVAILABLE = BINDSTATUS_SSLUX_NAVBLOCKED + 1
    BINDSTATUS_SNIFFED_CLASSIDAVAILABLE = (
        BINDSTATUS_SERVER_MIMETYPEAVAILABLE + 1
    )
    BINDSTATUS_64BIT_PROGRESS = BINDSTATUS_SNIFFED_CLASSIDAVAILABLE + 1
    BINDSTATUS_LAST = BINDSTATUS_64BIT_PROGRESS
    BINDSTATUS_RESERVED_0 = BINDSTATUS_LAST + 1
    BINDSTATUS_RESERVED_1 = BINDSTATUS_RESERVED_0 + 1
    BINDSTATUS_RESERVED_2 = BINDSTATUS_RESERVED_1 + 1
    BINDSTATUS_RESERVED_3 = BINDSTATUS_RESERVED_2 + 1
    BINDSTATUS_RESERVED_4 = BINDSTATUS_RESERVED_3 + 1
    BINDSTATUS_RESERVED_5 = BINDSTATUS_RESERVED_4 + 1
    BINDSTATUS_RESERVED_6 = BINDSTATUS_RESERVED_5 + 1
    BINDSTATUS_RESERVED_7 = BINDSTATUS_RESERVED_6 + 1
    BINDSTATUS_RESERVED_8 = BINDSTATUS_RESERVED_7 + 1
    BINDSTATUS_RESERVED_9 = BINDSTATUS_RESERVED_8 + 1
    BINDSTATUS_RESERVED_A = BINDSTATUS_RESERVED_9 + 1
    BINDSTATUS_RESERVED_B = BINDSTATUS_RESERVED_A + 1
    BINDSTATUS_RESERVED_C = BINDSTATUS_RESERVED_B + 1
    BINDSTATUS_RESERVED_D = BINDSTATUS_RESERVED_C + 1
    BINDSTATUS_RESERVED_E = BINDSTATUS_RESERVED_D + 1
    BINDSTATUS_RESERVED_F = BINDSTATUS_RESERVED_E + 1
    BINDSTATUS_RESERVED_10 = BINDSTATUS_RESERVED_F + 1
    BINDSTATUS_RESERVED_11 = BINDSTATUS_RESERVED_10 + 1
    BINDSTATUS_RESERVED_12 = BINDSTATUS_RESERVED_11 + 1
    BINDSTATUS_RESERVED_13 = BINDSTATUS_RESERVED_12 + 1
    BINDSTATUS_LAST_PRIVATE = BINDSTATUS_RESERVED_13


BINDSTATUS = tagBINDSTATUS

from .objidl_h import (
    FORMATETC,
)

IBindStatusCallback._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnStartBinding',
        (['in'], DWORD, 'dwReserved'),
        (['in'], POINTER(IBinding), 'pib'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPriority',
        (['out'], POINTER(LONG), 'pnPriority'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnLowResource',
        (['in'], DWORD, 'reserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnProgress',
        (['in'], ULONG, 'ulProgress'),
        (['in'], ULONG, 'ulProgressMax'),
        (['in'], ULONG, 'ulStatusCode'),
        (['in'], LPCWSTR, 'szStatusText'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnStopBinding',
        (['in'], HRESULT, 'hresult'),
        (['in'], LPCWSTR, 'szError'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBindInfo',
        (['out'], POINTER(DWORD), 'grfBINDF'),
        (['in', 'out'], POINTER(BINDINFO), 'pbindinfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnDataAvailable',
        (['in'], DWORD, 'grfBSCF'),
        (['in'], DWORD, 'dwSize'),
        (['in'], POINTER(FORMATETC), 'pformatetc'),
        (['in'], POINTER(STGMEDIUM), 'pstgmed'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnObjectAvailable',
        (['in'], REFIID, 'riid'),
        (['in'], POINTER(comtypes.IUnknown), 'punk'),
    ),
]


LPBINDSTATUSCALLBACKEX = POINTER(IBindStatusCallbackEx)


class __MIDL_IBindStatusCallbackEx_0001(ENUM):
    BINDF2_DISABLEBASICOVERHTTP = 0x1
    BINDF2_DISABLEAUTOCOOKIEHANDLING = 0x2
    BINDF2_READ_DATA_GREATER_THAN_4GB = 0x4
    BINDF2_DISABLE_HTTP_REDIRECT_XSECURITYID = 0x8
    BINDF2_SETDOWNLOADMODE = 0x20
    BINDF2_DISABLE_HTTP_REDIRECT_CACHING = 0x40
    BINDF2_KEEP_CALLBACK_MODULE_LOADED = 0x80
    BINDF2_ALLOW_PROXY_CRED_PROMPT = 0x100
    BINDF2_RESERVED_17 = 0x200
    BINDF2_RESERVED_16 = 0x400
    BINDF2_RESERVED_15 = 0x800
    BINDF2_RESERVED_14 = 0x1000
    BINDF2_RESERVED_13 = 0x2000
    BINDF2_RESERVED_12 = 0x4000
    BINDF2_RESERVED_11 = 0x8000
    BINDF2_RESERVED_10 = 0x10000
    BINDF2_RESERVED_F = 0x20000
    BINDF2_RESERVED_E = 0x40000
    BINDF2_RESERVED_D = 0x80000
    BINDF2_RESERVED_C = 0x100000
    BINDF2_RESERVED_B = 0x200000
    BINDF2_RESERVED_A = 0x400000
    BINDF2_RESERVED_9 = 0x800000
    BINDF2_RESERVED_8 = 0x1000000
    BINDF2_RESERVED_7 = 0x2000000
    BINDF2_RESERVED_6 = 0x4000000
    BINDF2_RESERVED_5 = 0x8000000
    BINDF2_RESERVED_4 = 0x10000000
    BINDF2_RESERVED_3 = 0x20000000
    BINDF2_RESERVED_2 = 0x40000000
    BINDF2_RESERVED_1 = 0x80000000


BINDF2 = __MIDL_IBindStatusCallbackEx_0001


IBindStatusCallbackEx._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetBindInfoEx',
        (['out'], POINTER(DWORD), 'grfBINDF'),
        (['in', 'out'], POINTER(BINDINFO), 'pbindinfo'),
        (['out'], POINTER(DWORD), 'grfBINDF2'),
        (['out'], POINTER(DWORD), 'pdwReserved'),
    ),
]


LPAUTHENTICATION = POINTER(IAuthenticate)


IAuthenticate._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Authenticate',
        (['out'], POINTER(HWND), 'phwnd'),
        (['out'], POINTER(LPWSTR), 'pszUsername'),
        (['out'], POINTER(LPWSTR), 'pszPassword'),
    ),
]


LPAUTHENTICATIONEX = POINTER(IAuthenticateEx)


class __MIDL_IAuthenticateEx_0001(ENUM):
    AUTHENTICATEF_PROXY = 0x1
    AUTHENTICATEF_BASIC = 0x2
    AUTHENTICATEF_HTTP = 0x4


AUTHENTICATEF = __MIDL_IAuthenticateEx_0001


class _tagAUTHENTICATEINFO(ctypes.Structure):
    _fields_ = [
        ('dwFlags', DWORD),
        ('dwReserved', DWORD),
    ]


AUTHENTICATEINFO = _tagAUTHENTICATEINFO


IAuthenticateEx._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AuthenticateEx',
        (['out'], POINTER(HWND), 'phwnd'),
        (['out'], POINTER(LPWSTR), 'pszUsername'),
        (['out'], POINTER(LPWSTR), 'pszPassword'),
        (['in'], POINTER(AUTHENTICATEINFO), 'pauthinfo'),
    ),
]


LPHTTPNEGOTIATE = POINTER(IHttpNegotiate)


IHttpNegotiate._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'BeginningTransaction',
        (['in'], LPCWSTR, 'szURL'),
        (['in'], LPCWSTR, 'szHeaders'),
        (['in'], DWORD, 'dwReserved'),
        (['out'], POINTER(LPWSTR), 'pszAdditionalHeaders'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnResponse',
        (['in'], DWORD, 'dwResponseCode'),
        (['in'], LPCWSTR, 'szResponseHeaders'),
        (['in'], LPCWSTR, 'szRequestHeaders'),
        (['out'], POINTER(LPWSTR), 'pszAdditionalRequestHeaders'),
    ),
]


LPHTTPNEGOTIATE2 = POINTER(IHttpNegotiate2)


IHttpNegotiate2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetRootSecurityId',
        (['out'], POINTER(BYTE), 'pbSecurityId'),
        (['in', 'out'], POINTER(DWORD), 'pcbSecurityId'),
        (['in'], DWORD_PTR, 'dwReserved'),
    ),
]


LPHTTPNEGOTIATE3 = POINTER(IHttpNegotiate3)
IHttpNegotiate3._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetSerializedClientCertContext',
        (['out'], POINTER(POINTER(BYTE)), 'ppbCert'),
        (['out'], POINTER(DWORD), 'pcbCert'),
    ),
]


LPWININETFILESTREAM = POINTER(IWinInetFileStream)
IWinInetFileStream._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetHandleForUnlock',
        (['in'], DWORD_PTR, 'hWinInetLockHandle'),
        (['in'], DWORD_PTR, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDeleteFile',
        (['in'], DWORD_PTR, 'dwReserved'),
    ),
]


LPWINDOWFORBINDINGUI = POINTER(IWindowForBindingUI)
IWindowForBindingUI._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetWindow',
        (['in'], REFGUID, 'rguidReason'),
        (['out'], POINTER(HWND), 'phwnd'),
    ),
]


LPCODEINSTALL = POINTER(ICodeInstall)


class __MIDL_ICodeInstall_0001(ENUM):
    CIP_DISK_FULL = 0
    CIP_ACCESS_DENIED = CIP_DISK_FULL + 1
    CIP_NEWER_VERSION_EXISTS = CIP_ACCESS_DENIED + 1
    CIP_OLDER_VERSION_EXISTS = CIP_NEWER_VERSION_EXISTS + 1
    CIP_NAME_CONFLICT = CIP_OLDER_VERSION_EXISTS + 1
    CIP_TRUST_VERIFICATION_COMPONENT_MISSING = CIP_NAME_CONFLICT + 1
    CIP_EXE_SELF_REGISTERATION_TIMEOUT = (
        CIP_TRUST_VERIFICATION_COMPONENT_MISSING + 1
    )
    CIP_UNSAFE_TO_ABORT = CIP_EXE_SELF_REGISTERATION_TIMEOUT + 1
    CIP_NEED_REBOOT = CIP_UNSAFE_TO_ABORT + 1
    CIP_NEED_REBOOT_UI_PERMISSION = CIP_NEED_REBOOT + 1


CIP_STATUS = __MIDL_ICodeInstall_0001


ICodeInstall._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnCodeInstallProblem',
        (['in'], ULONG, 'ulStatusCode'),
        (['in'], LPCWSTR, 'szDestination'),
        (['in'], LPCWSTR, 'szSource'),
        (['in'], DWORD, 'dwReserved'),
    ),
]


class __MIDL_IUri_0001(ENUM):
    Uri_PROPERTY_ABSOLUTE_URI = 0
    Uri_PROPERTY_STRING_START = Uri_PROPERTY_ABSOLUTE_URI
    Uri_PROPERTY_AUTHORITY = 1
    Uri_PROPERTY_DISPLAY_URI = 2
    Uri_PROPERTY_DOMAIN = 3
    Uri_PROPERTY_EXTENSION = 4
    Uri_PROPERTY_FRAGMENT = 5
    Uri_PROPERTY_HOST = 6
    Uri_PROPERTY_PASSWORD = 7
    Uri_PROPERTY_PATH = 8
    Uri_PROPERTY_PATH_AND_QUERY = 9
    Uri_PROPERTY_QUERY = 10
    Uri_PROPERTY_RAW_URI = 11
    Uri_PROPERTY_SCHEME_NAME = 12
    Uri_PROPERTY_USER_INFO = 13
    Uri_PROPERTY_USER_NAME = 14
    Uri_PROPERTY_STRING_LAST = Uri_PROPERTY_USER_NAME
    Uri_PROPERTY_HOST_TYPE = 15
    Uri_PROPERTY_DWORD_START = Uri_PROPERTY_HOST_TYPE
    Uri_PROPERTY_PORT = 16
    Uri_PROPERTY_SCHEME = 17
    Uri_PROPERTY_ZONE = 18
    Uri_PROPERTY_DWORD_LAST = Uri_PROPERTY_ZONE


Uri_PROPERTY = __MIDL_IUri_0001


class __MIDL_IUri_0002(ENUM):
    Uri_HOST_UNKNOWN = 0
    Uri_HOST_DNS = Uri_HOST_UNKNOWN + 1
    Uri_HOST_IPV4 = Uri_HOST_DNS + 1
    Uri_HOST_IPV6 = Uri_HOST_IPV4 + 1
    Uri_HOST_IDN = Uri_HOST_IPV6 + 1


Uri_HOST_TYPE = __MIDL_IUri_0002


IUri._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetPropertyBSTR',
        (['in'], Uri_PROPERTY, 'uriProp'),
        (['out'], POINTER(BSTR), 'pbstrProperty'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPropertyLength',
        (['in'], Uri_PROPERTY, 'uriProp'),
        (['out'], POINTER(DWORD), 'pcchProperty'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPropertyDWORD',
        (['in'], Uri_PROPERTY, 'uriProp'),
        (['out'], POINTER(DWORD), 'pdwProperty'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'HasProperty',
        (['in'], Uri_PROPERTY, 'uriProp'),
        (['out'], POINTER(BOOL), 'pfHasProperty'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAbsoluteUri',
        (['out'], POINTER(BSTR), 'pbstrAbsoluteUri'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAuthority',
        (['out'], POINTER(BSTR), 'pbstrAuthority'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDisplayUri',
        (['out'], POINTER(BSTR), 'pbstrDisplayString'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDomain',
        (['out'], POINTER(BSTR), 'pbstrDomain'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetExtension',
        (['out'], POINTER(BSTR), 'pbstrExtension'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFragment',
        (['out'], POINTER(BSTR), 'pbstrFragment'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetHost',
        (['out'], POINTER(BSTR), 'pbstrHost'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPassword',
        (['out'], POINTER(BSTR), 'pbstrPassword'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPath',
        (['out'], POINTER(BSTR), 'pbstrPath'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPathAndQuery',
        (['out'], POINTER(BSTR), 'pbstrPathAndQuery'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetQuery',
        (['out'], POINTER(BSTR), 'pbstrQuery'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRawUri',
        (['out'], POINTER(BSTR), 'pbstrRawUri'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSchemeName',
        (['out'], POINTER(BSTR), 'pbstrSchemeName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetUserInfo',
        (['out'], POINTER(BSTR), 'pbstrUserInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetUserName',
        (['out'], POINTER(BSTR), 'pbstrUserName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetHostType',
        (['out'], POINTER(DWORD), 'pdwHostType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPort',
        (['out'], POINTER(DWORD), 'pdwPort'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScheme',
        (['out'], POINTER(DWORD), 'pdwScheme'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetZone',
        (['out'], POINTER(DWORD), 'pdwZone'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetProperties',
        (['out'], LPDWORD, 'pdwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsEqual',
        (['in'], POINTER(IUri), 'pUri'),
        (['out'], POINTER(BOOL), 'pfEqual'),
    ),
]


# STDAPI CreateUri(_In_ LPCWSTR pwzURI,
#                  _In_ DWORD dwFlags,
#                  _Reserved_ DWORD_PTR dwReserved,
#                  _Outptr_ IUri** ppURI);
CreateUri = urlmon.CreateUri
CreateUri.restype = STDAPI


# STDAPI CreateUriWithFragment(
#                  _In_ LPCWSTR pwzURI,
#                  _In_opt_ LPCWSTR pwzFragment,
#                  _In_ DWORD dwFlags,
#                  _Reserved_ DWORD_PTR dwReserved,
#                  _Outptr_ IUri** ppURI);
CreateUriWithFragment = urlmon.CreateUriWithFragment
CreateUriWithFragment.restype = STDAPI


# STDAPI CreateUriFromMultiByteString(
#     _In_       LPCSTR    pszANSIInputUri,
#                DWORD     dwEncodingFlags,
#                DWORD     dwCodePage,
#                DWORD     dwCreateFlags,
#     _Reserved_ DWORD_PTR dwReserved,
#     _Outptr_   IUri**    ppUri);
CreateUriFromMultiByteString = urlmon.CreateUriFromMultiByteString
CreateUriFromMultiByteString.restype = STDAPI


Uri_HAS_ABSOLUTE_URI = 1 << Uri_PROPERTY.Uri_PROPERTY_ABSOLUTE_URI
Uri_HAS_AUTHORITY = 1 << Uri_PROPERTY.Uri_PROPERTY_AUTHORITY
Uri_HAS_DISPLAY_URI = 1 << Uri_PROPERTY.Uri_PROPERTY_DISPLAY_URI
Uri_HAS_DOMAIN = 1 << Uri_PROPERTY.Uri_PROPERTY_DOMAIN
Uri_HAS_EXTENSION = 1 << Uri_PROPERTY.Uri_PROPERTY_EXTENSION
Uri_HAS_FRAGMENT = 1 << Uri_PROPERTY.Uri_PROPERTY_FRAGMENT
Uri_HAS_HOST = 1 << Uri_PROPERTY.Uri_PROPERTY_HOST
Uri_HAS_PASSWORD = 1 << Uri_PROPERTY.Uri_PROPERTY_PASSWORD
Uri_HAS_PATH = 1 << Uri_PROPERTY.Uri_PROPERTY_PATH
Uri_HAS_QUERY = 1 << Uri_PROPERTY.Uri_PROPERTY_QUERY
Uri_HAS_RAW_URI = 1 << Uri_PROPERTY.Uri_PROPERTY_RAW_URI
Uri_HAS_SCHEME_NAME = 1 << Uri_PROPERTY.Uri_PROPERTY_SCHEME_NAME
Uri_HAS_USER_NAME = 1 << Uri_PROPERTY.Uri_PROPERTY_USER_NAME
Uri_HAS_PATH_AND_QUERY = 1 << Uri_PROPERTY.Uri_PROPERTY_PATH_AND_QUERY
Uri_HAS_USER_INFO = 1 << Uri_PROPERTY.Uri_PROPERTY_USER_INFO
Uri_HAS_HOST_TYPE = 1 << Uri_PROPERTY.Uri_PROPERTY_HOST_TYPE
Uri_HAS_PORT = 1 << Uri_PROPERTY.Uri_PROPERTY_PORT
Uri_HAS_SCHEME = 1 << Uri_PROPERTY.Uri_PROPERTY_SCHEME
Uri_HAS_ZONE = 1 << Uri_PROPERTY.Uri_PROPERTY_ZONE

Uri_CREATE_ALLOW_RELATIVE = 0x00000001
Uri_CREATE_ALLOW_IMPLICIT_WILDCARD_SCHEME = 0x00000002
Uri_CREATE_ALLOW_IMPLICIT_FILE_SCHEME = 0x00000004
Uri_CREATE_NOFRAG = 0x00000008
Uri_CREATE_NO_CANONICALIZE = 0x00000010
Uri_CREATE_CANONICALIZE = 0x00000100
Uri_CREATE_FILE_USE_DOS_PATH = 0x00000020
Uri_CREATE_DECODE_EXTRA_INFO = 0x00000040
Uri_CREATE_NO_DECODE_EXTRA_INFO = 0x00000080
Uri_CREATE_CRACK_UNKNOWN_SCHEMES = 0x00000200
Uri_CREATE_NO_CRACK_UNKNOWN_SCHEMES = 0x00000400
Uri_CREATE_PRE_PROCESS_HTML_URI = 0x00000800
Uri_CREATE_NO_PRE_PROCESS_HTML_URI = 0x00001000
Uri_CREATE_IE_SETTINGS = 0x00002000
Uri_CREATE_NO_IE_SETTINGS = 0x00004000
Uri_CREATE_NO_ENCODE_FORBIDDEN_CHARACTERS = 0x00008000
Uri_CREATE_NORMALIZE_INTL_CHARACTERS = 0x00010000
Uri_CREATE_CANONICALIZE_ABSOLUTE = 0x00020000
Uri_DISPLAY_NO_FRAGMENT = 0x00000001
Uri_PUNYCODE_IDN_HOST = 0x00000002
Uri_DISPLAY_IDN_HOST = 0x00000004
Uri_DISPLAY_NO_PUNYCODE = 0x00000008
Uri_ENCODING_USER_INFO_AND_PATH_IS_PERCENT_ENCODED_UTF8 = 0x00000001
Uri_ENCODING_USER_INFO_AND_PATH_IS_CP = 0x00000002
Uri_ENCODING_HOST_IS_IDN = 0x00000004
Uri_ENCODING_HOST_IS_PERCENT_ENCODED_UTF8 = 0x00000008
Uri_ENCODING_HOST_IS_PERCENT_ENCODED_CP = 0x00000010
Uri_ENCODING_QUERY_AND_FRAGMENT_IS_PERCENT_ENCODED_UTF8 = 0x00000020
Uri_ENCODING_QUERY_AND_FRAGMENT_IS_CP = 0x00000040
Uri_ENCODING_RFC = (
    Uri_ENCODING_USER_INFO_AND_PATH_IS_PERCENT_ENCODED_UTF8  |
     Uri_ENCODING_HOST_IS_PERCENT_ENCODED_UTF8  |
     Uri_ENCODING_QUERY_AND_FRAGMENT_IS_PERCENT_ENCODED_UTF8
)
UriBuilder_USE_ORIGINAL_FLAGS = 0x00000001
IUriContainer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetIUri',
        (['out'], POINTER(POINTER(IUri)), 'ppIUri'),
    ),
]


IUriBuilder._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateUriSimple',
        (['in'], DWORD, 'dwAllowEncodingPropertyMask'),
        (['in'], DWORD_PTR, 'dwReserved'),
        (['out'], POINTER(POINTER(IUri)), 'ppIUri'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateUri',
        (['in'], DWORD, 'dwCreateFlags'),
        (['in'], DWORD, 'dwAllowEncodingPropertyMask'),
        (['in'], DWORD_PTR, 'dwReserved'),
        (['out'], POINTER(POINTER(IUri)), 'ppIUri'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateUriWithFlags',
        (['in'], DWORD, 'dwCreateFlags'),
        (['in'], DWORD, 'dwUriBuilderFlags'),
        (['in'], DWORD, 'dwAllowEncodingPropertyMask'),
        (['in'], DWORD_PTR, 'dwReserved'),
        (['out'], POINTER(POINTER(IUri)), 'ppIUri'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetIUri',
        (['out'], POINTER(POINTER(IUri)), 'ppIUri'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetIUri',
        (['in'], POINTER(IUri), 'pIUri'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFragment',
        (['out'], POINTER(DWORD), 'pcchFragment'),
        (['out'], POINTER(LPCWSTR), 'ppwzFragment'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetHost',
        (['out'], POINTER(DWORD), 'pcchHost'),
        (['out'], POINTER(LPCWSTR), 'ppwzHost'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPassword',
        (['out'], POINTER(DWORD), 'pcchPassword'),
        (['out'], POINTER(LPCWSTR), 'ppwzPassword'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPath',
        (['out'], POINTER(DWORD), 'pcchPath'),
        (['out'], POINTER(LPCWSTR), 'ppwzPath'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPort',
        (['out'], POINTER(BOOL), 'pfHasPort'),
        (['out'], POINTER(DWORD), 'pdwPort'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetQuery',
        (['out'], POINTER(DWORD), 'pcchQuery'),
        (['out'], POINTER(LPCWSTR), 'ppwzQuery'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSchemeName',
        (['out'], POINTER(DWORD), 'pcchSchemeName'),
        (['out'], POINTER(LPCWSTR), 'ppwzSchemeName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetUserName',
        (['out'], POINTER(DWORD), 'pcchUserName'),
        (['out'], POINTER(LPCWSTR), 'ppwzUserName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFragment',
        (['in'], LPCWSTR, 'pwzNewValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetHost',
        (['in'], LPCWSTR, 'pwzNewValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPassword',
        (['in'], LPCWSTR, 'pwzNewValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPath',
        (['in'], LPCWSTR, 'pwzNewValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPort',
        (['in'], BOOL, 'fHasPort'),
        (['in'], DWORD, 'dwNewValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetQuery',
        (['in'], LPCWSTR, 'pwzNewValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSchemeName',
        (['in'], LPCWSTR, 'pwzNewValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetUserName',
        (['in'], LPCWSTR, 'pwzNewValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveProperties',
        (['in'], DWORD, 'dwPropertyMask'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'HasBeenModified',
        (['out'], POINTER(BOOL), 'pfModified'),
    ),
]


IUriBuilderFactory._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateIUriBuilder',
        (['in'], DWORD, 'dwFlags'),
        (['in'], DWORD_PTR, 'dwReserved'),
        (['out'], POINTER(POINTER(IUriBuilder)), 'ppIUriBuilder'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateInitializedIUriBuilder',
        (['in'], DWORD, 'dwFlags'),
        (['in'], DWORD_PTR, 'dwReserved'),
        (['out'], POINTER(POINTER(IUriBuilder)), 'ppIUriBuilder'),
    ),
]


# STDAPI CreateIUriBuilder(
#     _In_opt_     IUri         *pIUri,
#     _In_         DWORD         dwFlags,
#     _In_         DWORD_PTR     dwReserved,
#     _Outptr_     IUriBuilder **ppIUriBuilder
#     );
CreateIUriBuilder = urlmon.CreateIUriBuilder
CreateIUriBuilder.restype = STDAPI

LPWININETINFO = POINTER(IWinInetInfo)
IWinInetInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryOption',
        (['in'], DWORD, 'dwOption'),
        (['in', 'out'], LPVOID, 'pBuffer'),
        (['in', 'out'], POINTER(DWORD), 'pcbBuf'),
    ),
]


WININETINFO_OPTION_LOCK_HANDLE = 0xFFFE
LPHTTPSECURITY = POINTER(IHttpSecurity)
IHttpSecurity._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnSecurityProblem',
        (['in'], DWORD, 'dwProblem'),
    ),
]


LPWININETHTTPINFO = POINTER(IWinInetHttpInfo)
IWinInetHttpInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryInfo',
        (['in'], DWORD, 'dwOption'),
        (['in', 'out'], LPVOID, 'pBuffer'),
        (['in', 'out'], POINTER(DWORD), 'pcbBuf'),
        (['in', 'out'], POINTER(DWORD), 'pdwFlags'),
        (['in', 'out'], POINTER(DWORD), 'pdwReserved'),
    ),
]


IWinInetHttpTimeouts._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetRequestTimeouts',
        (['out'], POINTER(DWORD), 'pdwConnectTimeout'),
        (['out'], POINTER(DWORD), 'pdwSendTimeout'),
        (['out'], POINTER(DWORD), 'pdwReceiveTimeout'),
    ),
]


LPWININETCACHEHINTS = POINTER(IWinInetCacheHINTs)
IWinInetCacheHINTs._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetCacheExtension',
        (['in'], LPCWSTR, 'pwzExt'),
        (['in', 'out'], LPVOID, 'pszCacheFile'),
        (['in', 'out'], POINTER(DWORD), 'pcbCacheFile'),
        (['in', 'out'], POINTER(DWORD), 'pdwWinInetError'),
        (['in', 'out'], POINTER(DWORD), 'pdwReserved'),
    ),
]


LPWININETCACHEHINTS2 = POINTER(IWinInetCacheHINTs2)
IWinInetCacheHINTs2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetCacheExtension2',
        (['in'], LPCWSTR, 'pwzExt'),
        (['out'], POINTER(WCHAR), 'pwzCacheFile'),
        (['in', 'out'], POINTER(DWORD), 'pcchCacheFile'),
        (['out'], POINTER(DWORD), 'pdwWinInetError'),
        (['out'], POINTER(DWORD), 'pdwReserved'),
    ),
]


SID_IBindHost = IID_IBindHost
SID_SBindHost = IID_IBindHost
LPBINDHOST = POINTER(IBindHost)
IBindHost._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateMoniker',
        (['in'], LPOLESTR, 'szName'),
        (['in'], POINTER(IBindCtx), 'pBC'),
        (['out'], POINTER(POINTER(IMoniker)), 'ppmk'),
        (['in'], DWORD, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'MonikerBindToStorage',
        (['in'], POINTER(IMoniker), 'pMk'),
        (['in'], POINTER(IBindCtx), 'pBC'),
        (['in'], POINTER(IBindStatusCallback), 'pBSC'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvObj'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'MonikerBindToObject',
        (['in'], POINTER(IMoniker), 'pMk'),
        (['in'], POINTER(IBindCtx), 'pBC'),
        (['in'], POINTER(IBindStatusCallback), 'pBSC'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvObj'),
    ),
]


URLOSTRM_USECACHEDCOPY_ONLY = 0x1
URLOSTRM_USECACHEDCOPY = 0x2
URLOSTRM_GETNEWESTVERSION = 0x3

# STDAPI HlinkSimpleNavigateToString(
#     _In_opt_ LPCWSTR szTarget,
#     _In_opt_ LPCWSTR szLocation,
#     _In_opt_ LPCWSTR szTargetFrameName,
#     _In_     IUnknown *pUnk,
#     _In_opt_ IBindCtx *pbc,
#     _In_opt_ IBindStatusCallback *,
#      DWORD grfHLNF,            // flags
#      DWORD dwReserved          // for future use, must be NULL
# );
HlinkSimpleNavigateToString = urlmon.HlinkSimpleNavigateToString
HlinkSimpleNavigateToString.restype = STDAPI

# STDAPI HlinkSimpleNavigateToMoniker(
#     _In_opt_ IMoniker *pmkTarget,
#     _In_opt_ LPCWSTR szLocation,
#     _In_opt_ LPCWSTR szTargetFrameName,
#     _In_opt_ IUnknown *pUnk,
#     _In_opt_ IBindCtx *pbc,
#     _In_opt_ IBindStatusCallback *,
#      DWORD grfHLNF,            // flags
#      DWORD dwReserved          // for future use, must be NULL
# );
HlinkSimpleNavigateToMoniker = urlmon.HlinkSimpleNavigateToMoniker
HlinkSimpleNavigateToMoniker.restype = STDAPI

# STDAPI URLOpenStreamA(_In_opt_ LPUNKNOWN, _In_ LPCSTR,DWORD, _In_opt_ LPBINDSTATUSCALLBACK);
URLOpenStreamA = urlmon.URLOpenStreamA
URLOpenStreamA.restype = STDAPI

# STDAPI URLOpenStreamW(_In_opt_ LPUNKNOWN, _In_ LPCWSTR,DWORD,_In_opt_ LPBINDSTATUSCALLBACK);
URLOpenStreamW = urlmon.URLOpenStreamW
URLOpenStreamW.restype = STDAPI

# STDAPI URLOpenPullStreamA(_In_opt_ LPUNKNOWN, _In_ LPCSTR,DWORD, _In_opt_ LPBINDSTATUSCALLBACK);
URLOpenPullStreamA = urlmon.URLOpenPullStreamA
URLOpenPullStreamA.restype = STDAPI

# STDAPI URLOpenPullStreamW(_In_opt_ LPUNKNOWN,_In_ LPCWSTR,DWORD, _In_opt_ LPBINDSTATUSCALLBACK);
URLOpenPullStreamW = urlmon.URLOpenPullStreamW
URLOpenPullStreamW.restype = STDAPI

# STDAPI URLDownloadToFileA(_In_opt_ LPUNKNOWN, _In_ LPCSTR, _In_opt_ LPCSTR,DWORD, _In_opt_ LPBINDSTATUSCALLBACK);
URLDownloadToFileA = urlmon.URLDownloadToFileA
URLDownloadToFileA.restype = STDAPI

# STDAPI URLDownloadToFileW(_In_opt_ LPUNKNOWN, _In_ LPCWSTR,_In_opt_ LPCWSTR,DWORD, _In_opt_ LPBINDSTATUSCALLBACK);
URLDownloadToFileW = urlmon.URLDownloadToFileW
URLDownloadToFileW.restype = STDAPI

# STDAPI URLDownloadToCacheFileA(_In_opt_ LPUNKNOWN, _In_ LPCSTR,  _Out_writes_(cchFileName) LPSTR,  DWORD cchFileName, DWORD, _In_opt_ LPBINDSTATUSCALLBACK);
URLDownloadToCacheFileA = urlmon.URLDownloadToCacheFileA
URLDownloadToCacheFileA.restype = STDAPI

# STDAPI URLDownloadToCacheFileW(_In_opt_ LPUNKNOWN, _In_ LPCWSTR, _Out_writes_(cchFileName) LPWSTR, DWORD cchFileName, DWORD, _In_opt_ LPBINDSTATUSCALLBACK);
URLDownloadToCacheFileW = urlmon.URLDownloadToCacheFileW
URLDownloadToCacheFileW.restype = STDAPI

# STDAPI URLOpenBlockingStreamA(_In_opt_ LPUNKNOWN, _In_ LPCSTR, _Outptr_ LPSTREAM*,DWORD, _In_opt_ LPBINDSTATUSCALLBACK);
URLOpenBlockingStreamA = urlmon.URLOpenBlockingStreamA
URLOpenBlockingStreamA.restype = STDAPI

# STDAPI URLOpenBlockingStreamW(_In_opt_ LPUNKNOWN, _In_ LPCWSTR, _Outptr_ LPSTREAM*,DWORD, _In_opt_ LPBINDSTATUSCALLBACK);
URLOpenBlockingStreamW = urlmon.URLOpenBlockingStreamW
URLOpenBlockingStreamW.restype = STDAPI

URLOpenStream = URLOpenStreamW
URLOpenPullStream = URLOpenPullStreamW
URLDownloadToFile = URLDownloadToFileW
URLDownloadToCacheFile = URLDownloadToCacheFileW
URLOpenBlockingStream = URLOpenBlockingStreamW
# URLOpenStream = URLOpenStreamA
# URLOpenPullStream = URLOpenPullStreamA
# URLDownloadToFile = URLDownloadToFileA
# URLDownloadToCacheFile = URLDownloadToCacheFileA
# URLOpenBlockingStream = URLOpenBlockingStreamA

# STDAPI HlinkGoBack(_In_ IUnknown *pUnk);
HlinkGoBack = urlmon.HlinkGoBack
HlinkGoBack.restype = STDAPI

# STDAPI HlinkGoForward(_In_ IUnknown *pUnk);
HlinkGoForward = urlmon.HlinkGoForward
HlinkGoForward.restype = STDAPI

# STDAPI HlinkNavigateString(_In_opt_ IUnknown *pUnk, _In_opt_ LPCWSTR szTarget);
HlinkNavigateString = urlmon.HlinkNavigateString
HlinkNavigateString.restype = STDAPI

# STDAPI HlinkNavigateMoniker(_In_opt_ IUnknown *pUnk, _In_opt_ IMoniker *pmkTarget);
HlinkNavigateMoniker = urlmon.HlinkNavigateMoniker
HlinkNavigateMoniker.restype = STDAPI


LPIINTERNET = POINTER(IInternet)
LPIINTERNETBINDINFO = POINTER(IInternetBindInfo)
class tagBINDSTRING(ENUM):
    BINDSTRING_HEADERS = 1
    BINDSTRING_ACCEPT_MIMES = BINDSTRING_HEADERS + 1
    BINDSTRING_EXTRA_URL = BINDSTRING_ACCEPT_MIMES + 1
    BINDSTRING_LANGUAGE = BINDSTRING_EXTRA_URL + 1
    BINDSTRING_USERNAME = BINDSTRING_LANGUAGE + 1
    BINDSTRING_PASSWORD = BINDSTRING_USERNAME + 1
    BINDSTRING_UA_PIXELS = BINDSTRING_PASSWORD + 1
    BINDSTRING_UA_COLOR = BINDSTRING_UA_PIXELS + 1
    BINDSTRING_OS = BINDSTRING_UA_COLOR + 1
    BINDSTRING_USER_AGENT = BINDSTRING_OS + 1
    BINDSTRING_ACCEPT_ENCODINGS = BINDSTRING_USER_AGENT + 1
    BINDSTRING_POST_COOKIE = BINDSTRING_ACCEPT_ENCODINGS + 1
    BINDSTRING_POST_DATA_MIME = BINDSTRING_POST_COOKIE + 1
    BINDSTRING_URL = BINDSTRING_POST_DATA_MIME + 1
    BINDSTRING_IID = BINDSTRING_URL + 1
    BINDSTRING_FLAG_BIND_TO_OBJECT = BINDSTRING_IID + 1
    BINDSTRING_PTR_BIND_CONTEXT = BINDSTRING_FLAG_BIND_TO_OBJECT + 1
    BINDSTRING_XDR_ORIGIN = BINDSTRING_PTR_BIND_CONTEXT + 1
    BINDSTRING_DOWNLOADPATH = BINDSTRING_XDR_ORIGIN + 1
    BINDSTRING_ROOTDOC_URL = BINDSTRING_DOWNLOADPATH + 1
    BINDSTRING_INITIAL_FILENAME = BINDSTRING_ROOTDOC_URL + 1
    BINDSTRING_PROXY_USERNAME = BINDSTRING_INITIAL_FILENAME + 1
    BINDSTRING_PROXY_PASSWORD = BINDSTRING_PROXY_USERNAME + 1
    BINDSTRING_ENTERPRISE_ID = BINDSTRING_PROXY_PASSWORD + 1
    BINDSTRING_DOC_URL = BINDSTRING_ENTERPRISE_ID + 1


BINDSTRING = tagBINDSTRING


IInternetBindInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetBindInfo',
        (['out'], POINTER(DWORD), 'grfBINDF'),
        (['in', 'out'], POINTER(BINDINFO), 'pbindinfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBindString',
        (['in'], ULONG, 'ulStringType'),
        (['in', 'out'], POINTER(LPOLESTR), 'ppwzStr'),
        (['in'], ULONG, 'cEl'),
        (['in', 'out'], POINTER(ULONG), 'pcElFetched'),
    ),
]


LPIINTERNETBINDINFOEX = POINTER(IInternetBindInfoEx)
IInternetBindInfoEx._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetBindInfoEx',
        (['out'], POINTER(DWORD), 'grfBINDF'),
        (['in', 'out'], POINTER(BINDINFO), 'pbindinfo'),
        (['out'], POINTER(DWORD), 'grfBINDF2'),
        (['out'], POINTER(DWORD), 'pdwReserved'),
    ),
]


LPIINTERNETPROTOCOLROOT = POINTER(IInternetProtocolRoot)
class _tagPI_FLAGS(ENUM):
    PI_PARSE_URL = 0x1
    PI_FILTER_MODE = 0x2
    PI_FORCE_ASYNC = 0x4
    PI_USE_WORKERTHREAD = 0x8
    PI_MIMEVERIFICATION = 0x10
    PI_CLSIDLOOKUP = 0x20
    PI_DATAPROGRESS = 0x40
    PI_SYNCHRONOUS = 0x80
    PI_APARTMENTTHREADED = 0x100
    PI_CLASSINSTALL = 0x200
    PI_PASSONBINDCTX = 0x2000
    PI_NOMIMEHANDLER = 0x8000
    PI_LOADAPPDIRECT = 0x4000
    PD_FORCE_SWITCH = 0x10000
    PI_PREFERDEFAULTHANDLER = 0x20000


PI_FLAGS = _tagPI_FLAGS
PI_DOCFILECLSIDLOOKUP = PI_FLAGS.PI_CLSIDLOOKUP


class _tagPROTOCOLDATA(ctypes.Structure):
    _fields_ = [
        ('grfFlags', DWORD),
        ('dwState', DWORD),
        ('pData', LPVOID),
        ('cbData', ULONG),
    ]


PROTOCOLDATA = _tagPROTOCOLDATA



class _tagStartParam(ctypes.Structure):
    _fields_ = [
        ('iid', IID),
        ('pIBindCtx', POINTER(IBindCtx)),
        ('pItf', POINTER(comtypes.IUnknown)),
    ]


StartParam = _tagStartParam


IInternetProtocolRoot._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Start',
        (['in'], LPCWSTR, 'szUrl'),
        (['in'], POINTER(IInternetProtocolSink), 'pOIProtSink'),
        (['in'], POINTER(IInternetBindInfo), 'pOIBindInfo'),
        (['in'], DWORD, 'grfPI'),
        (['in'], HANDLE_PTR, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Continue',
        (['in'], POINTER(PROTOCOLDATA), 'pProtocolData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Abort',
        (['in'], HRESULT, 'hrReason'),
        (['in'], DWORD, 'dwOptions'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Terminate',
        (['in'], DWORD, 'dwOptions'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Resume'
    ),
]


LPIINTERNETPROTOCOL = POINTER(IInternetProtocol)
IInternetProtocol._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Read',
        (['in', 'out'], POINTER(VOID), 'pv'),
        (['in'], ULONG, 'cb'),
        (['out'], POINTER(ULONG), 'pcbRead'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Seek',
        (['in'], LARGE_INTEGER, 'dlibMove'),
        (['in'], DWORD, 'dwOrigin'),
        (['out'], POINTER(ULARGE_INTEGER), 'plibNewPosition'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'LockRequest',
        (['in'], DWORD, 'dwOptions'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnlockRequest'
    ),
]


IInternetProtocolEx._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'StartEx',
        (['in'], POINTER(IUri), 'pUri'),
        (['in'], POINTER(IInternetProtocolSink), 'pOIProtSink'),
        (['in'], POINTER(IInternetBindInfo), 'pOIBindInfo'),
        (['in'], DWORD, 'grfPI'),
        (['in'], HANDLE_PTR, 'dwReserved'),
    ),
]


LPIINTERNETPROTOCOLSINK = POINTER(IInternetProtocolSink)
IInternetProtocolSink._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Switch',
        (['in'], POINTER(PROTOCOLDATA), 'pProtocolData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReportProgress',
        (['in'], ULONG, 'ulStatusCode'),
        (['in'], LPCWSTR, 'szStatusText'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReportData',
        (['in'], DWORD, 'grfBSCF'),
        (['in'], ULONG, 'ulProgress'),
        (['in'], ULONG, 'ulProgressMax'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReportResult',
        (['in'], HRESULT, 'hrResult'),
        (['in'], DWORD, 'dwError'),
        (['in'], LPCWSTR, 'szResult'),
    ),
]


LPIINTERNETPROTOCOLSINKStackable = POINTER(IInternetProtocolSinkStackable)
IInternetProtocolSinkStackable._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SwitchSink',
        (['in'], POINTER(IInternetProtocolSink), 'pOIProtSink'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RollbackSwitch'
    ),
]


LPIINTERNETSESSION = POINTER(IInternetSession)


class _tagOIBDG_FLAGS(ENUM):
    OIBDG_APARTMENTTHREADED = 0x100
    OIBDG_DATAONLY = 0x1000


OIBDG_FLAGS = _tagOIBDG_FLAGS


IInternetSession._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RegisterNameSpace',
        (['in'], POINTER(IClassFactory), 'pCF'),
        (['in'], REFCLSID, 'rclsid'),
        (['in'], LPCWSTR, 'pwzProtocol'),
        (['in'], ULONG, 'cPatterns'),
        (['in'], POINTER(LPCWSTR), 'ppwzPatterns'),
        (['in'], DWORD, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnregisterNameSpace',
        (['in'], POINTER(IClassFactory), 'pCF'),
        (['in'], LPCWSTR, 'pszProtocol'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterMimeFilter',
        (['in'], POINTER(IClassFactory), 'pCF'),
        (['in'], REFCLSID, 'rclsid'),
        (['in'], LPCWSTR, 'pwzType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnregisterMimeFilter',
        (['in'], POINTER(IClassFactory), 'pCF'),
        (['in'], LPCWSTR, 'pwzType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateBinding',
        (['in'], LPBC, 'pBC'),
        (['in'], LPCWSTR, 'szUrl'),
        (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppUnk'),
        (['out'], POINTER(POINTER(IInternetProtocol)), 'ppOInetProt'),
        (['in'], DWORD, 'dwOption'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSessionOption',
        (['in'], DWORD, 'dwOption'),
        (['in'], LPVOID, 'pBuffer'),
        (['in'], DWORD, 'dwBufferLength'),
        (['in'], DWORD, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSessionOption',
        (['in'], DWORD, 'dwOption'),
        (['in', 'out'], LPVOID, 'pBuffer'),
        (['in', 'out'], POINTER(DWORD), 'pdwBufferLength'),
        (['in'], DWORD, 'dwReserved'),
    ),
]


LPIINTERNETTHREADSWITCH = POINTER(IInternetThreadSwitch)
IInternetThreadSwitch._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Continue'
    ),
]


LPIINTERNETPRIORITY = POINTER(IInternetPriority)
IInternetPriority._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetPriority',
        (['in'], LONG, 'nPriority'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPriority',
        (['out'], POINTER(LONG), 'pnPriority'),
    ),
]


LPIINTERNETPROTOCOLINFO = POINTER(IInternetProtocolInfo)
class _tagPARSEACTION(ENUM):
    PARSE_CANONICALIZE = 1
    PARSE_FRIENDLY = PARSE_CANONICALIZE + 1
    PARSE_SECURITY_URL = PARSE_FRIENDLY + 1
    PARSE_ROOTDOCUMENT = PARSE_SECURITY_URL + 1
    PARSE_DOCUMENT = PARSE_ROOTDOCUMENT + 1
    PARSE_ANCHOR = PARSE_DOCUMENT + 1
    PARSE_ENCODE_IS_UNESCAPE = PARSE_ANCHOR + 1
    PARSE_DECODE_IS_ESCAPE = PARSE_ENCODE_IS_UNESCAPE + 1
    PARSE_PATH_FROM_URL = PARSE_DECODE_IS_ESCAPE + 1
    PARSE_URL_FROM_PATH = PARSE_PATH_FROM_URL + 1
    PARSE_MIME = PARSE_URL_FROM_PATH + 1
    PARSE_SERVER = PARSE_MIME + 1
    PARSE_SCHEMA = PARSE_SERVER + 1
    PARSE_SITE = PARSE_SCHEMA + 1
    PARSE_DOMAIN = PARSE_SITE + 1
    PARSE_LOCATION = PARSE_DOMAIN + 1
    PARSE_SECURITY_DOMAIN = PARSE_LOCATION + 1
    PARSE_ESCAPE = PARSE_SECURITY_DOMAIN + 1
    PARSE_UNESCAPE = PARSE_ESCAPE + 1


PARSEACTION = _tagPARSEACTION


class _tagPSUACTION(ENUM):
    PSU_DEFAULT = 1
    PSU_SECURITY_URL_ONLY = PSU_DEFAULT + 1


PSUACTION = _tagPSUACTION


class _tagQUERYOPTION(ENUM):
    QUERY_EXPIRATION_DATE = 1
    QUERY_TIME_OF_LAST_CHANGE = QUERY_EXPIRATION_DATE + 1
    QUERY_CONTENT_ENCODING = QUERY_TIME_OF_LAST_CHANGE + 1
    QUERY_CONTENT_TYPE = QUERY_CONTENT_ENCODING + 1
    QUERY_REFRESH = QUERY_CONTENT_TYPE + 1
    QUERY_RECOMBINE = QUERY_REFRESH + 1
    QUERY_CAN_NAVIGATE = QUERY_RECOMBINE + 1
    QUERY_USES_NETWORK = QUERY_CAN_NAVIGATE + 1
    QUERY_IS_CACHED = QUERY_USES_NETWORK + 1
    QUERY_IS_INSTALLEDENTRY = QUERY_IS_CACHED + 1
    QUERY_IS_CACHED_OR_MAPPED = QUERY_IS_INSTALLEDENTRY + 1
    QUERY_USES_CACHE = QUERY_IS_CACHED_OR_MAPPED + 1
    QUERY_IS_SECURE = QUERY_USES_CACHE + 1
    QUERY_IS_SAFE = QUERY_IS_SECURE + 1
    QUERY_USES_HISTORYFOLDER = QUERY_IS_SAFE + 1
    QUERY_IS_CACHED_AND_USABLE_OFFLINE = QUERY_USES_HISTORYFOLDER + 1


QUERYOPTION = _tagQUERYOPTION


IInternetProtocolInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ParseUrl',
        (['in'], LPCWSTR, 'pwzUrl'),
        (['in'], PARSEACTION, 'ParseAction'),
        (['in'], DWORD, 'dwParseFlags'),
        (['out'], LPWSTR, 'pwzResult'),
        (['in'], DWORD, 'cchResult'),
        (['out'], POINTER(DWORD), 'pcchResult'),
        (['in'], DWORD, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CombineUrl',
        (['in'], LPCWSTR, 'pwzBaseUrl'),
        (['in'], LPCWSTR, 'pwzRelativeUrl'),
        (['in'], DWORD, 'dwCombineFlags'),
        (['out'], LPWSTR, 'pwzResult'),
        (['in'], DWORD, 'cchResult'),
        (['out'], POINTER(DWORD), 'pcchResult'),
        (['in'], DWORD, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CompareUrl',
        (['in'], LPCWSTR, 'pwzUrl1'),
        (['in'], LPCWSTR, 'pwzUrl2'),
        (['in'], DWORD, 'dwCompareFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryInfo',
        (['in'], LPCWSTR, 'pwzUrl'),
        (['in'], QUERYOPTION, 'OueryOption'),
        (['in'], DWORD, 'dwQueryFlags'),
        (['in', 'out'], LPVOID, 'pBuffer'),
        (['in'], DWORD, 'cbBuffer'),
        (['in', 'out'], POINTER(DWORD), 'pcbBuf'),
        (['in'], DWORD, 'dwReserved'),
    ),
]


PARSE_ENCODE = PARSEACTION.PARSE_ENCODE_IS_UNESCAPE
PARSE_DECODE = PARSEACTION.PARSE_DECODE_IS_ESCAPE
IOInet = IInternet
IOInetBindInfo = IInternetBindInfo
IOInetBindInfoEx = IInternetBindInfoEx
IOInetProtocolRoot = IInternetProtocolRoot
IOInetProtocol = IInternetProtocol
IOInetProtocolEx = IInternetProtocolEx
IOInetProtocolSink = IInternetProtocolSink
IOInetProtocolInfo = IInternetProtocolInfo
IOInetSession = IInternetSession
IOInetPriority = IInternetPriority
IOInetThreadSwitch = IInternetThreadSwitch
IOInetProtocolSinkStackable = IInternetProtocolSinkStackable
LPOINET = LPIINTERNET
LPOINETPROTOCOLINFO = LPIINTERNETPROTOCOLINFO
LPOINETBINDINFO = LPIINTERNETBINDINFO
LPOINETPROTOCOLROOT = LPIINTERNETPROTOCOLROOT
LPOINETPROTOCOL = LPIINTERNETPROTOCOL
# LPOINETPROTOCOLEX = LPIINTERNETPROTOCOLEX
LPOINETPROTOCOLSINK = LPIINTERNETPROTOCOLSINK
LPOINETSESSION = LPIINTERNETSESSION
LPOINETTHREADSWITCH = LPIINTERNETTHREADSWITCH
LPOINETPRIORITY = LPIINTERNETPRIORITY
# LPOINETPROTOCOLSINKSTACKABLE = LPIINTERNETPROTOCOLSINKSTACKABLE
IID_IOInet = IID_IInternet
IID_IOInetBindInfo = IID_IInternetBindInfo
IID_IOInetBindInfoEx = IID_IInternetBindInfoEx
IID_IOInetProtocolRoot = IID_IInternetProtocolRoot
IID_IOInetProtocol = IID_IInternetProtocol
IID_IOInetProtocolEx = IID_IInternetProtocolEx
IID_IOInetProtocolSink = IID_IInternetProtocolSink
IID_IOInetProtocolInfo = IID_IInternetProtocolInfo
IID_IOInetSession = IID_IInternetSession
IID_IOInetPriority = IID_IInternetPriority
IID_IOInetThreadSwitch = IID_IInternetThreadSwitch
IID_IOInetProtocolSinkStackable = IID_IInternetProtocolSinkStackable


# STDAPI CoInternetParseUrl(
#                                              LPCWSTR      pwzUrl,
#                                              PARSEACTION  ParseAction,
#                                              DWORD        dwFlags,
#     _Out_writes_to_(cchResult,*pcchResult+1) LPWSTR       pszResult,
#                                              DWORD        cchResult,
#     _Out_                                    DWORD       *pcchResult,
#                                              DWORD        dwReserved
#     );
CoInternetParseUrl = urlmon.CoInternetParseUrl
CoInternetParseUrl.restype = STDAPI


# STDAPI CoInternetParseIUri(
#     _In_                                     IUri        *pIUri,
#                                              PARSEACTION  ParseAction,
#                                              DWORD        dwFlags,
#     _Out_writes_to_(cchResult,*pcchResult+1) LPWSTR       pwzResult,
#                                              DWORD        cchResult,
#     _Out_                                    DWORD       *pcchResult,
#     _Reserved_                               DWORD_PTR    dwReserved
#     );
CoInternetParseIUri = urlmon.CoInternetParseIUri
CoInternetParseIUri.restype = STDAPI


# STDAPI CoInternetCombineUrl(
#                                              LPCWSTR   pwzBaseUrl,
#                                              LPCWSTR   pwzRelativeUrl,
#                                              DWORD     dwCombineFlags,
#     _Out_writes_to_(cchResult,*pcchResult+1) LPWSTR    pszResult,
#                                              DWORD     cchResult,
#     _Out_opt_                                DWORD     *pcchResult,
#     _Reserved_                               DWORD     dwReserved
#     );
CoInternetCombineUrl = urlmon.CoInternetCombineUrl
CoInternetCombineUrl.restype = STDAPI


# STDAPI CoInternetCombineUrlEx(
#     _In_opt_     IUri       *pBaseUri,
#     _In_opt_     LPCWSTR     pwzRelativeUrl,
#                  DWORD       dwCombineFlags,
#     _Outptr_     IUri      **ppCombinedUri,
#     _In_opt_     DWORD_PTR   dwReserved
#     );
CoInternetCombineUrlEx = urlmon.CoInternetCombineUrlEx
CoInternetCombineUrlEx.restype = STDAPI


# STDAPI CoInternetCombineIUri (
#     _In_         IUri       *pBaseUri,
#     _In_         IUri       *pRelativeUri,
#                  DWORD       dwCombineFlags,
#     _Outptr_     IUri      **ppCombinedUri,
#     _In_opt_     DWORD_PTR   dwReserved
#     );
CoInternetCombineIUri= urlmon.CoInternetCombineIUri
CoInternetCombineIUri.restype = STDAPI


# STDAPI CoInternetCompareUrl(
#     LPCWSTR pwzUrl1,
#     LPCWSTR pwzUrl2,
#     DWORD dwFlags
#     );
CoInternetCompareUrl = urlmon.CoInternetCompareUrl
CoInternetCompareUrl.restype = STDAPI


# STDAPI CoInternetGetProtocolFlags(
#              LPCWSTR     pwzUrl,
#     _Out_    DWORD      *pdwFlags,
#              DWORD       dwReserved
#     );
CoInternetGetProtocolFlags = urlmon.CoInternetGetProtocolFlags
CoInternetGetProtocolFlags.restype = STDAPI


# STDAPI CoInternetQueryInfo(
#                                                  LPCWSTR     pwzUrl,
#                                                  QUERYOPTION QueryOptions,
#                                                  DWORD       dwQueryFlags,
#     _Out_writes_bytes_to_(cbBuffer, *pcbBuffer)  LPVOID      pvBuffer,
#     _In_range_(>=, ctypes.sizeof(DWORD))                DWORD       cbBuffer,
#     _Out_opt_                                    DWORD      *pcbBuffer,
#                                                  DWORD       dwReserved
#     );
CoInternetQueryInfo = urlmon.CoInternetQueryInfo
CoInternetQueryInfo.restype = STDAPI


# STDAPI CoInternetGetSession(
#                  DWORD               dwSessionMode,
#     _Outptr_     IInternetSession  **ppIInternetSession,
#                  DWORD               dwReserved
#     );
CoInternetGetSession = urlmon.CoInternetGetSession
CoInternetGetSession.restype = STDAPI


# STDAPI CoInternetGetSecurityUrl(
#                  LPCWSTR pwszUrl,
#     _Outptr_     LPWSTR *ppwszSecUrl,
#     _In_         PSUACTION   psuAction,
#     _Reserved_   DWORD dwReserved
#     );
CoInternetGetSecurityUrl = urlmon.CoInternetGetSecurityUrl
CoInternetGetSecurityUrl.restype = STDAPI


# STDAPI AsyncInstallDistributionUnit(
#     _In_ LPCWSTR szDistUnit,
#     _In_opt_ LPCWSTR szTYPE,
#     _In_opt_ LPCWSTR szExt,
#     DWORD dwFileVersionMS,
#     DWORD dwFileVersionLS,
#     _In_opt_ LPCWSTR szURL,
#     _In_ IBindCtx *pbc,
#     _Reserved_ LPVOID   pvReserved,
#     DWORD   flags
#     );
AsyncInstallDistributionUnit = urlmon.AsyncInstallDistributionUnit
AsyncInstallDistributionUnit.restype = STDAPI


# STDAPI CoInternetGetSecurityUrlEx(
#     _In_         IUri           *pUri,
#     _Outptr_     IUri          **ppSecUri,
#                  PSUACTION       psuAction,
#     _Reserved_   DWORD_PTR       dwReserved
#     );
CoInternetGetSecurityUrlEx = urlmon.CoInternetGetSecurityUrlEx
CoInternetGetSecurityUrlEx.restype = STDAPI


class _tagINTERNETFEATURELIST(ENUM):
    FEATURE_OBJECT_CACHING = 0
    FEATURE_ZONE_ELEVATION = FEATURE_OBJECT_CACHING + 1
    FEATURE_MIME_HANDLING = FEATURE_ZONE_ELEVATION + 1
    FEATURE_MIME_SNIFFING = FEATURE_MIME_HANDLING + 1
    FEATURE_WINDOW_RESTRICTIONS = FEATURE_MIME_SNIFFING + 1
    FEATURE_WEBOC_POPUPMANAGEMENT = FEATURE_WINDOW_RESTRICTIONS + 1
    FEATURE_BEHAVIORS = FEATURE_WEBOC_POPUPMANAGEMENT + 1
    FEATURE_DISABLE_MK_PROTOCOL = FEATURE_BEHAVIORS + 1
    FEATURE_LOCALMACHINE_LOCKDOWN = FEATURE_DISABLE_MK_PROTOCOL + 1
    FEATURE_SECURITYBAND = FEATURE_LOCALMACHINE_LOCKDOWN + 1
    FEATURE_RESTRICT_ACTIVEXINSTALL = FEATURE_SECURITYBAND + 1
    FEATURE_VALIDATE_NAVIGATE_URL = FEATURE_RESTRICT_ACTIVEXINSTALL + 1
    FEATURE_RESTRICT_FILEDOWNLOAD = FEATURE_VALIDATE_NAVIGATE_URL + 1
    FEATURE_ADDON_MANAGEMENT = FEATURE_RESTRICT_FILEDOWNLOAD + 1
    FEATURE_PROTOCOL_LOCKDOWN = FEATURE_ADDON_MANAGEMENT + 1
    FEATURE_HTTP_USERNAME_PASSWORD_DISABLE = FEATURE_PROTOCOL_LOCKDOWN + 1
    FEATURE_SAFE_BINDTOOBJECT = FEATURE_HTTP_USERNAME_PASSWORD_DISABLE + 1
    FEATURE_UNC_SAVEDFILECHECK = FEATURE_SAFE_BINDTOOBJECT + 1
    FEATURE_GET_URL_DOM_FILEPATH_UNENCODED = FEATURE_UNC_SAVEDFILECHECK + 1
    FEATURE_TABBED_BROWSING = FEATURE_GET_URL_DOM_FILEPATH_UNENCODED + 1
    FEATURE_SSLUX = FEATURE_TABBED_BROWSING + 1
    FEATURE_DISABLE_NAVIGATION_SOUNDS = FEATURE_SSLUX + 1
    FEATURE_DISABLE_LEGACY_COMPRESSION = FEATURE_DISABLE_NAVIGATION_SOUNDS + 1
    FEATURE_FORCE_ADDR_AND_STATUS = FEATURE_DISABLE_LEGACY_COMPRESSION + 1
    FEATURE_XMLHTTP = FEATURE_FORCE_ADDR_AND_STATUS + 1
    FEATURE_DISABLE_TELNET_PROTOCOL = FEATURE_XMLHTTP + 1
    FEATURE_FEEDS = FEATURE_DISABLE_TELNET_PROTOCOL + 1
    FEATURE_BLOCK_INPUT_PROMPTS = FEATURE_FEEDS + 1
    FEATURE_ENTRY_COUNT = FEATURE_BLOCK_INPUT_PROMPTS + 1


INTERNETFEATURELIST = _tagINTERNETFEATURELIST


SET_FEATURE_ON_THREAD = 0x00000001
SET_FEATURE_ON_PROCESS = 0x00000002
SET_FEATURE_IN_REGISTRY = 0x00000004
SET_FEATURE_ON_THREAD_LOCALMACHINE = 0x00000008
SET_FEATURE_ON_THREAD_INTRANET = 0x00000010
SET_FEATURE_ON_THREAD_TRUSTED = 0x00000020
SET_FEATURE_ON_THREAD_INTERNET = 0x00000040
SET_FEATURE_ON_THREAD_RESTRICTED = 0x00000080
GET_FEATURE_FROM_THREAD = 0x00000001
GET_FEATURE_FROM_PROCESS = 0x00000002
GET_FEATURE_FROM_REGISTRY = 0x00000004
GET_FEATURE_FROM_THREAD_LOCALMACHINE = 0x00000008
GET_FEATURE_FROM_THREAD_INTRANET = 0x00000010
GET_FEATURE_FROM_THREAD_TRUSTED = 0x00000020
GET_FEATURE_FROM_THREAD_INTERNET = 0x00000040
GET_FEATURE_FROM_THREAD_RESTRICTED = 0x00000080


# STDAPI CoInternetSetFeatureEnabled(
#     INTERNETFEATURELIST FeatureEntry,
#     DWORD dwFlags,
#     BOOL fEnable
#     );
CoInternetSetFeatureEnabled = urlmon.CoInternetSetFeatureEnabled
CoInternetSetFeatureEnabled.restype = STDAPI


# STDAPI CoInternetIsFeatureEnabled(
#     INTERNETFEATURELIST FeatureEntry,
#     DWORD dwFlags
#     );
CoInternetIsFeatureEnabled = urlmon.CoInternetIsFeatureEnabled
CoInternetIsFeatureEnabled.restype = STDAPI


# STDAPI CoInternetIsFeatureEnabledForUrl(
#     INTERNETFEATURELIST FeatureEntry,
#     DWORD dwFlags,
#     _In_opt_ LPCWSTR szURL,
#     _In_opt_ IInternetSecurityManager *pSecMgr
#     );
CoInternetIsFeatureEnabledForUrl = urlmon.CoInternetIsFeatureEnabledForUrl
CoInternetIsFeatureEnabledForUrl.restype = STDAPI


# STDAPI CoInternetIsFeatureEnabledForIUri(
#     INTERNETFEATURELIST FeatureEntry,
#     DWORD dwFlags,
#     _In_opt_ IUri * pIUri,
#     _In_opt_ IInternetSecurityManagerEx2 *pSecMgr
#     );
CoInternetIsFeatureEnabledForIUri = urlmon.CoInternetIsFeatureEnabledForIUri
CoInternetIsFeatureEnabledForIUri.restype = STDAPI


# STDAPI CoInternetIsFeatureZoneElevationEnabled(
#     _In_opt_ LPCWSTR szFromURL,
#     _In_ LPCWSTR szToURL,
#     _In_opt_ IInternetSecurityManager *pSecMgr,
#     DWORD dwFlags
#     );
CoInternetIsFeatureZoneElevationEnabled = (
    urlmon.CoInternetIsFeatureZoneElevationEnabled
)
CoInternetIsFeatureZoneElevationEnabled.restype = STDAPI


# STDAPI CopyStgMedium(_In_ STGMEDIUM * pcstgmedSrc,
#                      _Out_      STGMEDIUM * pstgmedDest);
CopyStgMedium = urlmon.CopyStgMedium
CopyStgMedium.restype = STDAPI


# STDAPI CopyBindInfo(_In_ BINDINFO * pcbiSrc,
#                     _Out_      BINDINFO * pbiDest );
CopyBindInfo = urlmon.CopyBindInfo
CopyBindInfo.restype = STDAPI


# STDAPI_(VOID) ReleaseBindInfo( _Inout_ BINDINFO * pbindinfo );
ReleaseBindInfo = urlmon.ReleaseBindInfo
ReleaseBindInfo.restype = STDAPI

INET_E_USE_DEFAULT_PROTOCOLHANDLER = _HRESULT_TYPEDEF_(0x800C0011)
INET_E_USE_DEFAULT_SETTING = _HRESULT_TYPEDEF_(0x800C0012)
INET_E_DEFAULT_ACTION = INET_E_USE_DEFAULT_PROTOCOLHANDLER
INET_E_QUERYOPTION_UNKNOWN = _HRESULT_TYPEDEF_(0x800C0013)
INET_E_REDIRECTING = _HRESULT_TYPEDEF_(0x800C0014)
OInetParseUrl = CoInternetParseUrl
OInetCombineUrl = CoInternetCombineUrl
OInetCombineUrlEx = CoInternetCombineUrlEx
OInetCombineIUri = CoInternetCombineIUri
OInetCompareUrl = CoInternetCompareUrl
OInetQueryInfo = CoInternetQueryInfo
OInetGetSession = CoInternetGetSession
PROTOCOLFLAG_NO_PICS_CHECK = 0x00000001

# STDAPI_(PWSTR) IEGetUserPrivateNamespaceName(VOID);
IEGetUserPrivateNamespaceName = urlmon.IEGetUserPrivateNamespaceName
IEGetUserPrivateNamespaceName.restype = STDAPI


# STDAPI CoInternetCreateSecurityManager(_In_opt_ IServiceProvider *pSP, _Outptr_ IInternetSecurityManager **ppSM, DWORD dwReserved);
CoInternetCreateSecurityManager = urlmon.CoInternetCreateSecurityManager
CoInternetCreateSecurityManager.restype = STDAPI


# STDAPI CoInternetCreateZoneManager(_In_opt_ IServiceProvider *pSP, _Outptr_ IInternetZoneManager **ppZM, DWORD dwReserved);
CoInternetCreateZoneManager = urlmon.CoInternetCreateZoneManager
CoInternetCreateZoneManager.restype = STDAPI

SID_SInternetSecurityManager = IID_IInternetSecurityManager
SID_SInternetSecurityManagerEx = IID_IInternetSecurityManagerEx
SID_SInternetSecurityManagerEx2 = IID_IInternetSecurityManagerEx2
SID_SInternetHostSecurityManager = IID_IInternetHostSecurityManager
IInternetSecurityMgrSite._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetWindow',
        (['out'], POINTER(HWND), 'phwnd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnableModeless',
        (['in'], BOOL, 'fEnable'),
    ),
]


MUTZ_NOSAVEDFILECHECK = 0x00000001
MUTZ_ISFILE = 0x00000002
MUTZ_ACCEPT_WILDCARD_SCHEME = 0x00000080
MUTZ_ENFORCERESTRICTED = 0x00000100
MUTZ_RESERVED = 0x00000200
MUTZ_REQUIRESAVEDFILECHECK = 0x00000400
MUTZ_DONT_UNESCAPE = 0x00000800
MUTZ_DONT_USE_CACHE = 0x00001000
MUTZ_FORCE_INTRANET_FLAGS = 0x00002000
MUTZ_IGNORE_ZONE_MAPPINGS = 0x00004000
MAX_SIZE_SECURITY_ID = 0x200


class __MIDL_IInternetSecurityManager_0001(ENUM):
    PUAF_DEFAULT = 0
    PUAF_NOUI = 0x1
    PUAF_ISFILE = 0x2
    PUAF_WARN_IF_DENIED = 0x4
    PUAF_FORCEUI_FOREGROUND = 0x8
    PUAF_CHECK_TIFS = 0x10
    PUAF_DONTCHECKBOXINDIALOG = 0x20
    PUAF_TRUSTED = 0x40
    PUAF_ACCEPT_WILDCARD_SCHEME = 0x80
    PUAF_ENFORCERESTRICTED = 0x100
    PUAF_NOSAVEDFILECHECK = 0x200
    PUAF_REQUIRESAVEDFILECHECK = 0x400
    PUAF_DONT_USE_CACHE = 0x1000
    PUAF_RESERVED1 = 0x2000
    PUAF_RESERVED2 = 0x4000
    PUAF_LMZ_UNLOCKED = 0x10000
    PUAF_LMZ_LOCKED = 0x20000
    PUAF_DEFAULTZONEPOL = 0x40000
    PUAF_NPL_USE_LOCKED_IF_RESTRICTED = 0x80000
    PUAF_NOUIIFLOCKED = 0x100000
    PUAF_DRAGPROTOCOLCHECK = 0x200000


PUAF = __MIDL_IInternetSecurityManager_0001


class __MIDL_IInternetSecurityManager_0002(ENUM):
    PUAFOUT_DEFAULT = 0
    PUAFOUT_ISLOCKZONEPOLICY = 0x1


PUAFOUT = __MIDL_IInternetSecurityManager_0002


class __MIDL_IInternetSecurityManager_0003(ENUM):
    SZM_CREATE = 0
    SZM_DELETE = 0x1


SZM_FLAGS = __MIDL_IInternetSecurityManager_0003


IInternetSecurityManager._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetSecuritySite',
        (['in'], POINTER(IInternetSecurityMgrSite), 'pSite'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSecuritySite',
        (['out'], POINTER(POINTER(IInternetSecurityMgrSite)), 'ppSite'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'MapUrlToZone',
        (['in'], LPCWSTR, 'pwszUrl'),
        (['out'], POINTER(DWORD), 'pdwZone'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSecurityId',
        (['in'], LPCWSTR, 'pwszUrl'),
        (['out'], POINTER(BYTE), 'pbSecurityId'),
        (['in', 'out'], POINTER(DWORD), 'pcbSecurityId'),
        (['in'], DWORD_PTR, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ProcessUrlAction',
        (['in'], LPCWSTR, 'pwszUrl'),
        (['in'], DWORD, 'dwAction'),
        (['out'], POINTER(BYTE), 'pPolicy'),
        (['in'], DWORD, 'cbPolicy'),
        (['in'], POINTER(BYTE), 'pContext'),
        (['in'], DWORD, 'cbContext'),
        (['in'], DWORD, 'dwFlags'),
        (['in'], DWORD, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryCustomPolicy',
        (['in'], LPCWSTR, 'pwszUrl'),
        (['in'], REFGUID, 'guidKey'),
        (['out'], POINTER(POINTER(BYTE)), 'ppPolicy'),
        (['out'], POINTER(DWORD), 'pcbPolicy'),
        (['in'], POINTER(BYTE), 'pContext'),
        (['in'], DWORD, 'cbContext'),
        (['in'], DWORD, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetZoneMapping',
        (['in'], DWORD, 'dwZone'),
        (['in'], LPCWSTR, 'lpszPattern'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetZoneMappings',
        (['in'], DWORD, 'dwZone'),
        (['out'], POINTER(POINTER(IEnumString)), 'ppenumString'),
        (['in'], DWORD, 'dwFlags'),
    ),
]


IInternetSecurityManagerEx._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ProcessUrlActionEx',
        (['in'], LPCWSTR, 'pwszUrl'),
        (['in'], DWORD, 'dwAction'),
        (['out'], POINTER(BYTE), 'pPolicy'),
        (['in'], DWORD, 'cbPolicy'),
        (['in'], POINTER(BYTE), 'pContext'),
        (['in'], DWORD, 'cbContext'),
        (['in'], DWORD, 'dwFlags'),
        (['in'], DWORD, 'dwReserved'),
        (['out'], POINTER(DWORD), 'pdwOutFlags'),
    ),
]


IInternetSecurityManagerEx2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'MapUrlToZoneEx2',
        (['in'], POINTER(IUri), 'pUri'),
        (['out'], POINTER(DWORD), 'pdwZone'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(LPWSTR), 'ppwszMappedUrl'),
        (['out'], POINTER(DWORD), 'pdwOutFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ProcessUrlActionEx2',
        (['in'], POINTER(IUri), 'pUri'),
        (['in'], DWORD, 'dwAction'),
        (['out'], POINTER(BYTE), 'pPolicy'),
        (['in'], DWORD, 'cbPolicy'),
        (['in'], POINTER(BYTE), 'pContext'),
        (['in'], DWORD, 'cbContext'),
        (['in'], DWORD, 'dwFlags'),
        (['in'], DWORD_PTR, 'dwReserved'),
        (['out'], POINTER(DWORD), 'pdwOutFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSecurityIdEx2',
        (['in'], POINTER(IUri), 'pUri'),
        (['out'], POINTER(BYTE), 'pbSecurityId'),
        (['in', 'out'], POINTER(DWORD), 'pcbSecurityId'),
        (['in'], DWORD_PTR, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryCustomPolicyEx2',
        (['in'], POINTER(IUri), 'pUri'),
        (['in'], REFGUID, 'guidKey'),
        (['out'], POINTER(POINTER(BYTE)), 'ppPolicy'),
        (['out'], POINTER(DWORD), 'pcbPolicy'),
        (['in'], POINTER(BYTE), 'pContext'),
        (['in'], DWORD, 'cbContext'),
        (['in'], DWORD_PTR, 'dwReserved'),
    ),
]


IZoneIdentifier._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetId',
        (['out'], POINTER(DWORD), 'pdwZone'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetId',
        (['in'], DWORD, 'dwZone'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Remove'
    ),
]


IZoneIdentifier2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetLastWriterPackageFamilyName',
        (['out'], POINTER(LPWSTR), 'packageFamilyName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetLastWriterPackageFamilyName',
        (['in'], LPCWSTR, 'packageFamilyName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAppZoneId',
        (['out'], POINTER(DWORD), 'zone'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetAppZoneId',
        (['in'], DWORD, 'zone'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveAppZoneId'
    ),
]


IInternetHostSecurityManager._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetSecurityId',
        (['out'], POINTER(BYTE), 'pbSecurityId'),
        (['in', 'out'], POINTER(DWORD), 'pcbSecurityId'),
        (['in'], DWORD_PTR, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ProcessUrlAction',
        (['in'], DWORD, 'dwAction'),
        (['out'], POINTER(BYTE), 'pPolicy'),
        (['in'], DWORD, 'cbPolicy'),
        (['in'], POINTER(BYTE), 'pContext'),
        (['in'], DWORD, 'cbContext'),
        (['in'], DWORD, 'dwFlags'),
        (['in'], DWORD, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryCustomPolicy',
        (['in'], REFGUID, 'guidKey'),
        (['out'], POINTER(POINTER(BYTE)), 'ppPolicy'),
        (['out'], POINTER(DWORD), 'pcbPolicy'),
        (['in'], POINTER(BYTE), 'pContext'),
        (['in'], DWORD, 'cbContext'),
        (['in'], DWORD, 'dwReserved'),
    ),
]


URLACTION_MIN = 0x00001000
URLACTION_DOWNLOAD_MIN = 0x00001000
URLACTION_DOWNLOAD_SIGNED_ACTIVEX = 0x00001001
URLACTION_DOWNLOAD_UNSIGNED_ACTIVEX = 0x00001004
URLACTION_DOWNLOAD_CURR_MAX = 0x00001004
URLACTION_DOWNLOAD_MAX = 0x000011FF
URLACTION_ACTIVEX_MIN = 0x00001200
URLACTION_ACTIVEX_RUN = 0x00001200
URLPOLICY_ACTIVEX_CHECK_LIST = 0x00010000
URLACTION_ACTIVEX_OVERRIDE_OBJECT_SAFETY = 0x00001201
URLACTION_ACTIVEX_OVERRIDE_DATA_SAFETY = 0x00001202
URLACTION_ACTIVEX_OVERRIDE_SCRIPT_SAFETY = 0x00001203
URLACTION_SCRIPT_OVERRIDE_SAFETY = 0x00001401
URLACTION_ACTIVEX_CONFIRM_NOOBJECTSAFETY = 0x00001204
URLACTION_ACTIVEX_TREATASUNTRUSTED = 0x00001205
URLACTION_ACTIVEX_NO_WEBOC_SCRIPT = 0x00001206
URLACTION_ACTIVEX_OVERRIDE_REPURPOSEDETECTION = 0x00001207
URLACTION_ACTIVEX_OVERRIDE_OPTIN = 0x00001208
URLACTION_ACTIVEX_SCRIPTLET_RUN = 0x00001209
URLACTION_ACTIVEX_DYNSRC_VIDEO_AND_ANIMATION = 0x0000120A
URLACTION_ACTIVEX_OVERRIDE_DOMAINLIST = 0x0000120B
URLACTION_ACTIVEX_ALLOW_TDC = 0x0000120C
URLACTION_ACTIVEX_CURR_MAX = 0x0000120C
URLACTION_ACTIVEX_MAX = 0x000013ff
URLACTION_SCRIPT_MIN = 0x00001400
URLACTION_SCRIPT_RUN = 0x00001400
URLACTION_SCRIPT_JAVA_USE = 0x00001402
URLACTION_SCRIPT_SAFE_ACTIVEX = 0x00001405
URLACTION_CROSS_DOMAIN_DATA = 0x00001406
URLACTION_SCRIPT_PASTE = 0x00001407
URLACTION_ALLOW_XDOMAIN_SUBFRAME_RESIZE = 0x00001408
URLACTION_SCRIPT_XSSFILTER = 0x00001409
URLACTION_SCRIPT_NAVIGATE = 0x0000140A
URLACTION_PLUGGABLE_PROTOCOL_XHR = 0x0000140B
URLACTION_ALLOW_VBSCRIPT_IE = 0x0000140C
URLACTION_SCRIPT_CURR_MAX = 0x0000140C
URLACTION_SCRIPT_MAX = 0x000015ff
URLACTION_HTML_MIN = 0x00001600
URLACTION_HTML_SUBMIT_FORMS = 0x00001601
URLACTION_HTML_SUBMIT_FORMS_FROM = 0x00001602
URLACTION_HTML_SUBMIT_FORMS_TO = 0x00001603
URLACTION_HTML_FONT_DOWNLOAD = 0x00001604
URLACTION_HTML_JAVA_RUN = 0x00001605
URLACTION_HTML_USERDATA_SAVE = 0x00001606
URLACTION_HTML_SUBFRAME_NAVIGATE = 0x00001607
URLACTION_HTML_META_REFRESH = 0x00001608
URLACTION_HTML_MIXED_CONTENT = 0x00001609
URLACTION_HTML_INCLUDE_FILE_PATH = 0x0000160A
URLACTION_HTML_ALLOW_INJECTED_DYNAMIC_HTML = 0x0000160B
URLACTION_HTML_REQUIRE_UTF8_DOCUMENT_CODEPAGE = 0x0000160C
URLACTION_HTML_ALLOW_CROSS_DOMAIN_CANVAS = 0x0000160D
URLACTION_HTML_ALLOW_WINDOW_CLOSE = 0x0000160E
URLACTION_HTML_ALLOW_CROSS_DOMAIN_WEBWORKER = 0x0000160F
URLACTION_HTML_ALLOW_CROSS_DOMAIN_TEXTTRACK = 0x00001610
URLACTION_HTML_ALLOW_INDEXEDDB = 0x00001611
URLACTION_HTML_MAX = 0x000017ff
URLACTION_SHELL_MIN = 0x00001800
URLACTION_SHELL_INSTALL_DTITEMS = 0x00001800
URLACTION_SHELL_MOVE_OR_COPY = 0x00001802
URLACTION_SHELL_FILE_DOWNLOAD = 0x00001803
URLACTION_SHELL_VERB = 0x00001804
URLACTION_SHELL_WEBVIEW_VERB = 0x00001805
URLACTION_SHELL_SHELLEXECUTE = 0x00001806
URLACTION_SHELL_EXECUTE_HIGHRISK = 0x00001806
URLACTION_SHELL_EXECUTE_MODRISK = 0x00001807
URLACTION_SHELL_EXECUTE_LOWRISK = 0x00001808
URLACTION_SHELL_POPUPMGR = 0x00001809
URLACTION_SHELL_RTF_OBJECTS_LOAD = 0x0000180A
URLACTION_SHELL_ENHANCED_DRAGDROP_SECURITY = 0x0000180B
URLACTION_SHELL_EXTENSIONSECURITY = 0x0000180C
URLACTION_SHELL_SECURE_DRAGSOURCE = 0x0000180D
URLACTION_SHELL_REMOTEQUERY = 0x0000180E
URLACTION_SHELL_PREVIEW = 0x0000180F
URLACTION_SHELL_SHARE = 0x00001810
URLACTION_SHELL_ALLOW_CROSS_SITE_SHARE = 0x00001811
URLACTION_SHELL_TOCTOU_RISK = 0x00001812
URLACTION_SHELL_CURR_MAX = 0x00001812
URLACTION_SHELL_MAX = 0x000019ff
URLACTION_NETWORK_MIN = 0x00001A00
URLACTION_CREDENTIALS_USE = 0x00001A00
URLPOLICY_CREDENTIALS_SILENT_LOGON_OK = 0x00000000
URLPOLICY_CREDENTIALS_MUST_PROMPT_USER = 0x00010000
URLPOLICY_CREDENTIALS_CONDITIONAL_PROMPT = 0x00020000
URLPOLICY_CREDENTIALS_ANONYMOUS_ONLY = 0x00030000
URLACTION_AUTHENTICATE_CLIENT = 0x00001A01
URLPOLICY_AUTHENTICATE_CLEARTEXT_OK = 0x00000000
URLPOLICY_AUTHENTICATE_CHALLENGE_RESPONSE = 0x00010000
URLPOLICY_AUTHENTICATE_MUTUAL_ONLY = 0x00030000
URLACTION_COOKIES = 0x00001A02
URLACTION_COOKIES_SESSION = 0x00001A03
URLACTION_CLIENT_CERT_PROMPT = 0x00001A04
URLACTION_COOKIES_THIRD_PARTY = 0x00001A05
URLACTION_COOKIES_SESSION_THIRD_PARTY = 0x00001A06
URLACTION_COOKIES_ENABLED = 0x00001A10
URLACTION_NETWORK_CURR_MAX = 0x00001A10
URLACTION_NETWORK_MAX = 0x00001Bff
URLACTION_JAVA_MIN = 0x00001C00
URLACTION_JAVA_PERMISSIONS = 0x00001C00
URLPOLICY_JAVA_PROHIBIT = 0x00000000
URLPOLICY_JAVA_HIGH = 0x00010000
URLPOLICY_JAVA_MEDIUM = 0x00020000
URLPOLICY_JAVA_LOW = 0x00030000
URLPOLICY_JAVA_CUSTOM = 0x00800000
URLACTION_JAVA_CURR_MAX = 0x00001C00
URLACTION_JAVA_MAX = 0x00001Cff
URLACTION_INFODELIVERY_MIN = 0x00001D00
URLACTION_INFODELIVERY_NO_ADDING_CHANNELS = 0x00001D00
URLACTION_INFODELIVERY_NO_EDITING_CHANNELS = 0x00001D01
URLACTION_INFODELIVERY_NO_REMOVING_CHANNELS = 0x00001D02
URLACTION_INFODELIVERY_NO_ADDING_SUBSCRIPTIONS = 0x00001D03
URLACTION_INFODELIVERY_NO_EDITING_SUBSCRIPTIONS = 0x00001D04
URLACTION_INFODELIVERY_NO_REMOVING_SUBSCRIPTIONS = 0x00001D05
URLACTION_INFODELIVERY_NO_CHANNEL_LOGGING = 0x00001D06
URLACTION_INFODELIVERY_CURR_MAX = 0x00001D06
URLACTION_INFODELIVERY_MAX = 0x00001Dff
URLACTION_CHANNEL_SOFTDIST_MIN = 0x00001E00
URLACTION_CHANNEL_SOFTDIST_PERMISSIONS = 0x00001E05
URLPOLICY_CHANNEL_SOFTDIST_PROHIBIT = 0x00010000
URLPOLICY_CHANNEL_SOFTDIST_PRECACHE = 0x00020000
URLPOLICY_CHANNEL_SOFTDIST_AUTOINSTALL = 0x00030000
URLACTION_CHANNEL_SOFTDIST_MAX = 0x00001Eff
URLACTION_DOTNET_USERCONTROLS = 0x00002005
URLACTION_BEHAVIOR_MIN = 0x00002000
URLACTION_BEHAVIOR_RUN = 0x00002000
URLPOLICY_BEHAVIOR_CHECK_LIST = 0x00010000
URLACTION_FEATURE_MIN = 0x00002100
URLACTION_FEATURE_MIME_SNIFFING = 0x00002100
URLACTION_FEATURE_ZONE_ELEVATION = 0x00002101
URLACTION_FEATURE_WINDOW_RESTRICTIONS = 0x00002102
URLACTION_FEATURE_SCRIPT_STATUS_BAR = 0x00002103
URLACTION_FEATURE_FORCE_ADDR_AND_STATUS = 0x00002104
URLACTION_FEATURE_BLOCK_INPUT_PROMPTS = 0x00002105
URLACTION_FEATURE_DATA_BINDING = 0x00002106
URLACTION_FEATURE_CROSSDOMAIN_FOCUS_CHANGE = 0x00002107
URLACTION_AUTOMATIC_DOWNLOAD_UI_MIN = 0x00002200
URLACTION_AUTOMATIC_DOWNLOAD_UI = 0x00002200
URLACTION_AUTOMATIC_ACTIVEX_UI = 0x00002201
URLACTION_ALLOW_RESTRICTEDPROTOCOLS = 0x00002300
URLACTION_ALLOW_APEVALUATION = 0x00002301
URLACTION_ALLOW_XHR_EVALUATION = 0x00002302
URLACTION_WINDOWS_BROWSER_APPLICATIONS = 0x00002400
URLACTION_XPS_DOCUMENTS = 0x00002401
URLACTION_LOOSE_XAML = 0x00002402
URLACTION_LOWRIGHTS = 0x00002500
URLACTION_WINFX_SETUP = 0x00002600
URLACTION_INPRIVATE_BLOCKING = 0x00002700
URLACTION_ALLOW_AUDIO_VIDEO = 0x00002701
URLACTION_ALLOW_ACTIVEX_FILTERING = 0x00002702
URLACTION_ALLOW_STRUCTURED_STORAGE_SNIFFING = 0x00002703
URLACTION_ALLOW_AUDIO_VIDEO_PLUGINS = 0x00002704
URLACTION_ALLOW_ZONE_ELEVATION_VIA_OPT_OUT = 0x00002705
URLACTION_ALLOW_ZONE_ELEVATION_OPT_OUT_ADDITION = 0x00002706
URLACTION_ALLOW_CROSSDOMAIN_DROP_WITHIN_WINDOW = 0x00002708
URLACTION_ALLOW_CROSSDOMAIN_DROP_ACROSS_WINDOWS = 0x00002709
URLACTION_ALLOW_CROSSDOMAIN_APPCACHE_MANIFEST = 0x0000270A
URLACTION_ALLOW_RENDER_LEGACY_DXTFILTERS = 0x0000270B
URLACTION_ALLOW_ANTIMALWARE_SCANNING_OF_ACTIVEX = 0x0000270C
URLACTION_ALLOW_CSS_EXPRESSIONS = 0x0000270D
URLPOLICY_ALLOW = 0x00
URLPOLICY_QUERY = 0x01
URLPOLICY_DISALLOW = 0x03
URLPOLICY_NOTIFY_ON_ALLOW = 0x10
URLPOLICY_NOTIFY_ON_DISALLOW = 0x20
URLPOLICY_LOG_ON_ALLOW = 0x40
URLPOLICY_LOG_ON_DISALLOW = 0x80
URLPOLICY_MASK_PERMISSIONS = 0x0f


def GetUrlPolicyPermissions(dw):
    return dw & URLPOLICY_MASK_PERMISSIONS


def SetUrlPolicyPermissions(dw, dw2):
    dw = (dw & ~URLPOLICY_MASK_PERMISSIONS) | dw2
    return dw


URLPOLICY_DONTCHECKDLGBOX = 0x100
LPURLZONEMANAGER = POINTER(IInternetZoneManager)


class tagURLZONE(ENUM):
    URLZONE_INVALID = - 1
    URLZONE_PREDEFINED_MIN = 0
    URLZONE_LOCAL_MACHINE = 0
    URLZONE_INTRANET = URLZONE_LOCAL_MACHINE + 1
    URLZONE_TRUSTED = URLZONE_INTRANET + 1
    URLZONE_INTERNET = URLZONE_TRUSTED + 1
    URLZONE_UNTRUSTED = URLZONE_INTERNET + 1
    URLZONE_PREDEFINED_MAX = 999
    URLZONE_USER_MIN = 1000
    URLZONE_USER_MAX = 10000


URLZONE = tagURLZONE


URLZONE_ESC_FLAG = 0x100
class tagURLTEMPLATE(ENUM):
    URLTEMPLATE_CUSTOM = 0
    URLTEMPLATE_PREDEFINED_MIN = 0x10000
    URLTEMPLATE_LOW = 0x10000
    URLTEMPLATE_MEDLOW = 0x10500
    URLTEMPLATE_MEDIUM = 0x11000
    URLTEMPLATE_MEDHIGH = 0x11500
    URLTEMPLATE_HIGH = 0x12000
    URLTEMPLATE_PREDEFINED_MAX = 0x20000


URLTEMPLATE = tagURLTEMPLATE


class __MIDL_IInternetZoneManager_0002(ENUM):
    ZAFLAGS_CUSTOM_EDIT = 0x1
    ZAFLAGS_ADD_SITES = 0x2
    ZAFLAGS_REQUIRE_VERIFICATION = 0x4
    ZAFLAGS_INCLUDE_PROXY_OVERRIDE = 0x8
    ZAFLAGS_INCLUDE_INTRANET_SITES = 0x10
    ZAFLAGS_NO_UI = 0x20
    ZAFLAGS_SUPPORTS_VERIFICATION = 0x40
    ZAFLAGS_UNC_AS_INTRANET = 0x80
    ZAFLAGS_DETECT_INTRANET = 0x100
    ZAFLAGS_USE_LOCKED_ZONES = 0x10000
    ZAFLAGS_VERIFY_TEMPLATE_SETTINGS = 0x20000
    ZAFLAGS_NO_CACHE = 0x40000


ZAFLAGS = __MIDL_IInternetZoneManager_0002



class _ZONEATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ('cbSize', ULONG),
        ('szDisplayName', WCHAR * 260),
        ('szDescription', WCHAR * 200),
        ('szIconPath', WCHAR * 260),
        ('dwTemplateMinLevel', DWORD),
        ('dwTemplateRecommended', DWORD),
        ('dwTemplateCurrentLevel', DWORD),
        ('dwFlags', DWORD),
    ]


ZONEATTRIBUTES = _ZONEATTRIBUTES


LPZONEATTRIBUTES = POINTER(_ZONEATTRIBUTES)


class _URLZONEREG(ENUM):
    URLZONEREG_DEFAULT = 0
    URLZONEREG_HKLM = URLZONEREG_DEFAULT + 1
    URLZONEREG_HKCU = URLZONEREG_HKLM + 1


URLZONEREG = _URLZONEREG


IInternetZoneManager._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetZoneAttributes',
        (['in'], DWORD, 'dwZone'),
        (['in', 'out'], POINTER(ZONEATTRIBUTES), 'pZoneAttributes'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetZoneAttributes',
        (['in'], DWORD, 'dwZone'),
        (['in'], POINTER(ZONEATTRIBUTES), 'pZoneAttributes'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetZoneCustomPolicy',
        (['in'], DWORD, 'dwZone'),
        (['in'], REFGUID, 'guidKey'),
        (['out'], POINTER(POINTER(BYTE)), 'ppPolicy'),
        (['out'], POINTER(DWORD), 'pcbPolicy'),
        (['in'], URLZONEREG, 'urlZoneReg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetZoneCustomPolicy',
        (['in'], DWORD, 'dwZone'),
        (['in'], REFGUID, 'guidKey'),
        (['in'], POINTER(BYTE), 'pPolicy'),
        (['in'], DWORD, 'cbPolicy'),
        (['in'], URLZONEREG, 'urlZoneReg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetZoneActionPolicy',
        (['in'], DWORD, 'dwZone'),
        (['in'], DWORD, 'dwAction'),
        (['out'], POINTER(BYTE), 'pPolicy'),
        (['in'], DWORD, 'cbPolicy'),
        (['in'], URLZONEREG, 'urlZoneReg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetZoneActionPolicy',
        (['in'], DWORD, 'dwZone'),
        (['in'], DWORD, 'dwAction'),
        (['in'], POINTER(BYTE), 'pPolicy'),
        (['in'], DWORD, 'cbPolicy'),
        (['in'], URLZONEREG, 'urlZoneReg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PromptAction',
        (['in'], DWORD, 'dwAction'),
        (['in'], HWND, 'hwndParent'),
        (['in'], LPCWSTR, 'pwszUrl'),
        (['in'], LPCWSTR, 'pwszText'),
        (['in'], DWORD, 'dwPromptFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'LogAction',
        (['in'], DWORD, 'dwAction'),
        (['in'], LPCWSTR, 'pwszUrl'),
        (['in'], LPCWSTR, 'pwszText'),
        (['in'], DWORD, 'dwLogFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateZoneEnumerator',
        (['out'], POINTER(DWORD), 'pdwEnum'),
        (['out'], POINTER(DWORD), 'pdwCount'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetZoneAt',
        (['in'], DWORD, 'dwEnum'),
        (['in'], DWORD, 'dwIndex'),
        (['out'], POINTER(DWORD), 'pdwZone'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DestroyZoneEnumerator',
        (['in'], DWORD, 'dwEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CopyTemplatePoliciesToZone',
        (['in'], DWORD, 'dwTemplate'),
        (['in'], DWORD, 'dwZone'),
        (['in'], DWORD, 'dwReserved'),
    ),
]


IInternetZoneManagerEx._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetZoneActionPolicyEx',
        (['in'], DWORD, 'dwZone'),
        (['in'], DWORD, 'dwAction'),
        (['out'], POINTER(BYTE), 'pPolicy'),
        (['in'], DWORD, 'cbPolicy'),
        (['in'], URLZONEREG, 'urlZoneReg'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetZoneActionPolicyEx',
        (['in'], DWORD, 'dwZone'),
        (['in'], DWORD, 'dwAction'),
        (['in'], POINTER(BYTE), 'pPolicy'),
        (['in'], DWORD, 'cbPolicy'),
        (['in'], URLZONEREG, 'urlZoneReg'),
        (['in'], DWORD, 'dwFlags'),
    ),
]


SECURITY_IE_STATE_GREEN = 0x00000000
SECURITY_IE_STATE_RED = 0x00000001
IInternetZoneManagerEx2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetZoneAttributesEx',
        (['in'], DWORD, 'dwZone'),
        (['in', 'out'], POINTER(ZONEATTRIBUTES), 'pZoneAttributes'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetZoneSecurityState',
        (['in'], DWORD, 'dwZoneIndex'),
        (['in'], BOOL, 'fRespectPolicy'),
        (['in', 'out'], LPDWORD, 'pdwState'),
        (['in', 'out'], POINTER(BOOL), 'pfPolicyEncountered'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetIESecurityState',
        (['in'], BOOL, 'fRespectPolicy'),
        (['in', 'out'], LPDWORD, 'pdwState'),
        (['in', 'out'], POINTER(BOOL), 'pfPolicyEncountered'),
        (['in'], BOOL, 'fNoCache'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FixUnsecureSettings'
    ),
]


SOFTDIST_FLAG_USAGE_EMAIL = 0x00000001
SOFTDIST_FLAG_USAGE_PRECACHE = 0x00000002
SOFTDIST_FLAG_USAGE_AUTOINSTALL = 0x00000004
SOFTDIST_FLAG_DELETE_SUBSCRIPTION = 0x00000008
SOFTDIST_ADSTATE_NONE = 0x00000000
SOFTDIST_ADSTATE_AVAILABLE = 0x00000001
SOFTDIST_ADSTATE_DOWNLOADED = 0x00000002
SOFTDIST_ADSTATE_INSTALLED = 0x00000003

class _tagCODEBASEHOLD(ctypes.Structure):
    _fields_ = [
        ('cbSize', ULONG),
        ('szDistUnit', LPWSTR),
        ('szCodeBase', LPWSTR),
        ('dwVersionMS', DWORD),
        ('dwVersionLS', DWORD),
        ('dwStyle', DWORD),
    ]


CODEBASEHOLD = _tagCODEBASEHOLD


LPCODEBASEHOLD = POINTER(_tagCODEBASEHOLD)



class _tagSOFTDISTINFO(ctypes.Structure):
    _fields_ = [
        ('cbSize', ULONG),
        ('dwFlags', DWORD),
        ('dwAdState', DWORD),
        ('szTitle', LPWSTR),
        ('szAbstract', LPWSTR),
        ('szHREF', LPWSTR),
        ('dwInstalledVersionMS', DWORD),
        ('dwInstalledVersionLS', DWORD),
        ('dwUpdateVersionMS', DWORD),
        ('dwUpdateVersionLS', DWORD),
        ('dwAdvertisedVersionMS', DWORD),
        ('dwAdvertisedVersionLS', DWORD),
        ('dwReserved', DWORD),
    ]


SOFTDISTINFO = _tagSOFTDISTINFO


LPSOFTDISTINFO = POINTER(_tagSOFTDISTINFO)


ISoftDistExt._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ProcessSoftDist',
        (['in'], LPCWSTR, 'szCDFURL'),
        (['in'], POINTER(VOID), 'pSoftDistElement'), # VOID = IXMLElement
        (['in', 'out'], LPSOFTDISTINFO, 'lpsdi'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFirstCodeBase',
        (['in'], POINTER(LPWSTR), 'szCodeBase'),
        (['in'], LPDWORD, 'dwMaxSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNextCodeBase',
        (['in'], POINTER(LPWSTR), 'szCodeBase'),
        (['in'], LPDWORD, 'dwMaxSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AsyncInstallDistributionUnit',
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], LPVOID, 'pvReserved'),
        (['in'], DWORD, 'flags'),
        (['in'], LPCODEBASEHOLD, 'lpcbh'),
    ),
]


# STDAPI GetSoftwareUpdateInfo( LPCWSTR szDistUnit, _Out_ LPSOFTDISTINFO psdi );
GetSoftwareUpdateInfo = urlmon.GetSoftwareUpdateInfo
GetSoftwareUpdateInfo.restype = STDAPI


# STDAPI SetSoftwareUpdateAdvertisementState( LPCWSTR szDistUnit, DWORD dwAdState, DWORD dwAdvertisedVersionMS, DWORD dwAdvertisedVersionLS );
SetSoftwareUpdateAdvertisementState = (
    urlmon.SetSoftwareUpdateAdvertisementState
)
SetSoftwareUpdateAdvertisementState.restype = STDAPI


LPCATALOGFILEINFO = POINTER(ICatalogFileInfo)
ICatalogFileInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCatalogFile',
        (['out'], POINTER(LPSTR), 'ppszCatalogFile'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetJavaTrust',
        (['out'], POINTER(POINTER(VOID)), 'ppJavaTrust'),
    ),
]


LPDATAFILTER = POINTER(IDataFilter)
IDataFilter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DoEncode',
        (['in'], DWORD, 'dwFlags'),
        (['in'], LONG, 'lInBufferSize'),
        (['in'], POINTER(BYTE), 'pbInBuffer'),
        (['in'], LONG, 'lOutBufferSize'),
        (['out'], POINTER(BYTE), 'pbOutBuffer'),
        (['in'], LONG, 'lInBytesAvailable'),
        (['out'], POINTER(LONG), 'plInBytesRead'),
        (['out'], POINTER(LONG), 'plOutBytesWritten'),
        (['in'], DWORD, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DoDecode',
        (['in'], DWORD, 'dwFlags'),
        (['in'], LONG, 'lInBufferSize'),
        (['in'], POINTER(BYTE), 'pbInBuffer'),
        (['in'], LONG, 'lOutBufferSize'),
        (['out'], POINTER(BYTE), 'pbOutBuffer'),
        (['in'], LONG, 'lInBytesAvailable'),
        (['out'], POINTER(LONG), 'plInBytesRead'),
        (['out'], POINTER(LONG), 'plOutBytesWritten'),
        (['in'], DWORD, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetEncodingLevel',
        (['in'], DWORD, 'dwEncLevel'),
    ),
]



class _tagPROTOCOLFILTERDATA(ctypes.Structure):
    _fields_ = [
        ('cbSize', DWORD),
        ('pProtocolSink', POINTER(IInternetProtocolSink)),
        ('pProtocol', POINTER(IInternetProtocol)),
        ('pUnk', POINTER(comtypes.IUnknown)),
        ('dwFilterFlags', DWORD),
    ]


PROTOCOLFILTERDATA = _tagPROTOCOLFILTERDATA


LPENCODINGFILTERFACTORY = POINTER(IEncodingFilterFactory)

class _tagDATAINFO(ctypes.Structure):
    _fields_ = [
        ('ulTotalSize', ULONG),
        ('ulavrPacketSize', ULONG),
        ('ulConnectSpeed', ULONG),
        ('ulProcessorSpeed', ULONG),
    ]


DATAINFO = _tagDATAINFO


IEncodingFilterFactory._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'FindBestFilter',
        (['in'], LPCWSTR, 'pwzCodeIn'),
        (['in'], LPCWSTR, 'pwzCodeOut'),
        (['in'], DATAINFO, 'info'),
        (['out'], POINTER(POINTER(IDataFilter)), 'ppDF'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultFilter',
        (['in'], LPCWSTR, 'pwzCodeIn'),
        (['in'], LPCWSTR, 'pwzCodeOut'),
        (['out'], POINTER(POINTER(IDataFilter)), 'ppDF'),
    ),
]


# BOOL WINAPI IsLoggingEnabledW(_In_ LPCWSTR  pwszUrl);
IsLoggingEnabledW = urlmon.IsLoggingEnabledW
IsLoggingEnabledW.restype = BOOL

IsLoggingEnabled = IsLoggingEnabledW
# IsLoggingEnabled = IsLoggingEnabledA


class _tagHIT_LOGGING_INFO(ctypes.Structure):
    _fields_ = [
        ('dwStructSize', DWORD),
        ('lpszLoggedUrlName', LPSTR),
        ('StartTime', SYSTEMTIME),
        ('EndTime', SYSTEMTIME),
        ('lpszExtendedInfo', LPSTR),
    ]


HIT_LOGGING_INFO = _tagHIT_LOGGING_INFO
LPHIT_LOGGING_INFO = POINTER(_tagHIT_LOGGING_INFO)

CONFIRMSAFETYACTION_LOADOBJECT = 0x00000001


class CONFIRMSAFETY(ctypes.Structure):
    _fields_ = [
        ('clsid', CLSID),
        ('pUnk', POINTER(comtypes.IUnknown)),
        ('dwFlags', DWORD),
    ]


LPIWRAPPEDPROTOCOL = POINTER(IWrappedProtocol)
IWrappedProtocol._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetWrapperCode',
        (['out'], POINTER(LONG), 'pnCode'),
        (['in'], DWORD_PTR, 'dwReserved'),
    ),
]


LPGETBINDHANDLE = POINTER(IGetBindHandle)


class __MIDL_IGetBindHandle_0001(ENUM):
    BINDHANDLETYPES_APPCACHE = 0
    BINDHANDLETYPES_DEPENDENCY = 0x1
    BINDHANDLETYPES_COUNT = BINDHANDLETYPES_DEPENDENCY + 1


BINDHANDLETYPES = __MIDL_IGetBindHandle_0001


IGetBindHandle._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetBindHandle',
        (['in'], BINDHANDLETYPES, 'enumRequestedHandle'),
        (['out'], POINTER(HANDLE), 'pRetHandle'),
    ),
]



class _tagPROTOCOL_ARGUMENT(ctypes.Structure):
    _fields_ = [
        ('szMethod', LPCWSTR),
        ('szTargetUrl', LPCWSTR),
    ]


PROTOCOL_ARGUMENT = _tagPROTOCOL_ARGUMENT


LPPROTOCOL_ARGUMENT = POINTER(_tagPROTOCOL_ARGUMENT)


LPBINDCALLBACKREDIRECT = POINTER(IBindCallbackRedirect)
IBindCallbackRedirect._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Redirect',
        (['in'], LPCWSTR, 'lpcUrl'),
        (['out'], POINTER(VARIANT_BOOL), 'vbCancel'),
    ),
]


IBindHttpSecurity._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetIgnoreCertMask',
        (['out'], POINTER(DWORD), 'pdwIgnoreCertMask'),
    ),
]



__all__ = (
    'IWinInetHttpInfo', 'IInternetProtocolSinkStackable', 'IZoneIdentifier',
    'IWinInetCacheHINTs', 'IBindCallbackRedirect', 'IWinInetHttpTimeouts',
    'IWinInetFileStream', 'IBindHost', 'IUriBuilder', 'IInternetPriority',
    'IWindowForBindingUI', 'IBindStatusCallbackEx', 'IInternetProtocol',
    'IInternetSecurityManager', 'IInternetZoneManagerEx', 'IInternetSession',
    'IInternetHostSecurityManager', 'IInternetProtocolSink', 'IHttpSecurity',
    'IEncodingFilterFactory', 'IAuthenticate', 'IHttpNegotiate2', 'IBinding',
    'IHttpNegotiate3', 'IInternetBindInfo', 'IWrappedProtocol', 'IDataFilter',
    'IInternetProtocolEx', 'IInternetZoneManagerEx2', 'IWinInetCacheHINTs2',
    'IUriBuilderFactory', 'IMonikerProp', 'IGetBindHandle', 'IUriContainer',
    'IAuthenticateEx', 'IInternetProtocolRoot', 'IHttpNegotiate', 'IInternet',
    'IInternetProtocolInfo', 'IZoneIdentifier2', 'ISoftDistExt', 'IUri',
    'IWinInetInfo', 'IBindProtocol', 'IInternetSecurityManagerEx2', 'CF_NULL',
    'IBindHttpSecurity', 'IInternetBindInfoEx', 'IInternetThreadSwitch',
    'IInternetSecurityMgrSite', 'IInternetSecurityManagerEx', 'ICodeInstall',
    'IBindStatusCallback', 'IInternetZoneManager', 'IPersistMoniker', 'PUAF',
    'ICatalogFileInfo', 'MUTZ_DONT_UNESCAPE', 'Uri_ENCODING_HOST_IS_IDN',
    'URLACTION_ALLOW_CROSSDOMAIN_APPCACHE_MANIFEST', 'CFSTR_MIME_X_MSVIDEO',
    'GET_FEATURE_FROM_THREAD_TRUSTED', 'FMFD_ENABLEMIMESNIFFING', 'IOInet',
    'URLACTION_FEATURE_BLOCK_INPUT_PROMPTS', 'LPOINETPROTOCOL', 'IID_IOInet',
    'GET_FEATURE_FROM_THREAD_LOCALMACHINE', 'URLPOLICY_MASK_PERMISSIONS',
    'URLPOLICY_CREDENTIALS_ANONYMOUS_ONLY', 'URLACTION_JAVA_PERMISSIONS',
    'URLACTION_ACTIVEX_OVERRIDE_SCRIPT_SAFETY', 'Uri_ENCODING_RFC', 'LPOINET',
    'GET_FEATURE_FROM_THREAD_INTERNET', 'INET_E_HSTS_CERTIFICATE_ERROR',
    'URLACTION_SHELL_EXTENSIONSECURITY', 'CFSTR_MIME_TIFF', 'OInetGetSession',
    'INET_E_CANNOT_CONNECT', 'CFSTR_MIME_PJPEG', 'URLACTION_CREDENTIALS_USE',
    'URLACTION_ALLOW_STRUCTURED_STORAGE_SNIFFING', 'URLPOLICY_QUERY', 'BINDF',
    'CFSTR_MIME_X_MIXED_REPLACE', 'URLACTION_SHELL_PREVIEW', 'Uri_HAS_PORT',
    'Uri_HAS_USER_INFO', 'CFSTR_MIME_HTML', 'IID_IOInetProtocol', 'E_PENDING',
    'CFSTR_MIME_X_PNG', 'URL_MK_LEGACY', 'Uri_CREATE_NO_CANONICALIZE', 'BSCF',
    'INET_E_CANNOT_REPLACE_SFP_FILE', 'URLACTION_JAVA_MIN', 'LPOINETBINDINFO',
    'INET_E_NO_VALID_MEDIA', 'URLACTION_SCRIPT_RUN', 'URLACTION_SHELL_MIN',
    'GET_FEATURE_FROM_REGISTRY', 'URLACTION_FEATURE_MIN', 'MUTZ_RESERVED',
    'GetUrlPolicyPermissions', 'SECURITY_IE_STATE_RED', 'IOInetBindInfo',
    'URLACTION_SHELL_FILE_DOWNLOAD', 'INET_E_DOWNLOAD_BLOCKED_BY_CSP',
    'CFSTR_MIME_XML', 'URLACTION_ACTIVEX_RUN', 'GET_FEATURE_FROM_THREAD',
    'INET_E_CANNOT_LOAD_DATA', 'URLACTION_INFODELIVERY_CURR_MAX', 'BINDINFOF',
    'URLPOLICY_JAVA_LOW', 'SECURITY_IE_STATE_GREEN', 'URLACTION_ACTIVEX_MIN',
    'URLACTION_DOWNLOAD_MIN', 'URLPOLICY_JAVA_HIGH', 'Uri_HAS_SCHEME',
    'INET_E_INVALID_REQUEST', 'URLACTION_HTML_ALLOW_WINDOW_CLOSE', 'PUAFOUT',
    'WININETINFO_OPTION_LOCK_HANDLE', 'URLACTION_PLUGGABLE_PROTOCOL_XHR',
    'CFSTR_MIME_JPEG_XR', 'URLACTION_FEATURE_MIME_SNIFFING', 'Uri_HAS_DOMAIN',
    'CONFIRMSAFETYACTION_LOADOBJECT', 'URLPOLICY_ACTIVEX_CHECK_LIST',
    'Uri_CREATE_ALLOW_IMPLICIT_WILDCARD_SCHEME', 'URLDownloadToFile',
    'OInetCompareUrl', 'MUTZ_ENFORCERESTRICTED', 'BINDF_DONTPUTINCACHE',
    'INET_E_CODE_INSTALL_BLOCKED_BY_HASH_POLICY', 'IID_IOInetThreadSwitch',
    'URLACTION_DOWNLOAD_SIGNED_ACTIVEX', 'LPOINETPRIORITY', 'CFSTR_MIME_PNG',
    'URLACTION_FEATURE_ZONE_ELEVATION', 'INET_E_VTAB_SWITCH_FORCE_ENGINE',
    'URLACTION_ALLOW_XDOMAIN_SUBFRAME_RESIZE', 'Uri_HAS_AUTHORITY', 'BINDF2',
    'URLACTION_ACTIVEX_TREATASUNTRUSTED', 'URLACTION_SHELL_REMOTEQUERY',
    'URLACTION_ALLOW_ANTIMALWARE_SCANNING_OF_ACTIVEX', 'CFSTR_MIME_RAWDATA',
    'SET_FEATURE_ON_THREAD', 'URLACTION_ALLOW_VBSCRIPT_IE', 'CFSTR_MIME_NULL',
    'URLZONE_ESC_FLAG', 'URLOSTRM_USECACHEDCOPY_ONLY', 'MUTZ_DONT_USE_CACHE',
    'URLACTION_ACTIVEX_DYNSRC_VIDEO_AND_ANIMATION', 'URLACTION_HTML_MAX',
    'URLACTION_SCRIPT_OVERRIDE_SAFETY', 'URLACTION_CROSS_DOMAIN_DATA',
    'URLACTION_AUTOMATIC_DOWNLOAD_UI_MIN', 'URLACTION_HTML_META_REFRESH',
    'URLACTION_ALLOW_RESTRICTEDPROTOCOLS', 'URLACTION_COOKIES_ENABLED',
    'URLOSTRM_USECACHEDCOPY', 'CFSTR_MIME_X_REALAUDIO', 'URLACTION_MIN',
    'URLACTION_INFODELIVERY_NO_REMOVING_SUBSCRIPTIONS', 'CFSTR_MIME_X_EMF',
    'URLACTION_SCRIPT_NAVIGATE', 'URLACTION_SCRIPT_PASTE', 'IOInetPriority',
    'URLACTION_INFODELIVERY_MAX', 'INET_E_CANNOT_LOCK_REQUEST', 'MUTZ_ISFILE',
    'INET_E_INVALID_CERTIFICATE', 'URLACTION_ALLOW_CSS_EXPRESSIONS',
    'URLACTION_ACTIVEX_OVERRIDE_DOMAINLIST', 'INET_E_UNKNOWN_PROTOCOL',
    'URLACTION_SCRIPT_JAVA_USE', 'MUTZ_REQUIRESAVEDFILECHECK', 'Uri_HAS_HOST',
    'Uri_DISPLAY_NO_PUNYCODE', 'Uri_ENCODING_HOST_IS_PERCENT_ENCODED_CP',
    'LPOINETTHREADSWITCH', 'URLMON_OPTION_USE_BROWSERAPPSDOCUMENTS',
    'URLACTION_AUTOMATIC_ACTIVEX_UI', 'URLACTION_NETWORK_CURR_MAX', 'ZAFLAGS',
    'Uri_CREATE_FILE_USE_DOS_PATH', 'LPOINETPROTOCOLINFO', 'CFSTR_MIME_DDS',
    'URLACTION_HTML_INCLUDE_FILE_PATH', 'URLACTION_LOOSE_XAML', 'OIBDG_FLAGS',
    'Uri_ENCODING_USER_INFO_AND_PATH_IS_CP', 'SID_IBindHost', 'SID_SBindHost',
    'INET_E_CONNECTION_TIMEOUT', 'SET_FEATURE_ON_THREAD_INTERNET', 'BINDVERB',
    'URLPOLICY_ALLOW', 'LPOINETPROTOCOLROOT', 'URLZONE',
    'URLACTION_COOKIES_SESSION_THIRD_PARTY', 'URLACTION_CLIENT_CERT_PROMPT',
    'Uri_ENCODING_QUERY_AND_FRAGMENT_IS_PERCENT_ENCODED_UTF8', 'Uri_HAS_PATH',
    'SOFTDIST_FLAG_USAGE_AUTOINSTALL', 'URLACTION_ALLOW_XHR_EVALUATION',
    'INET_E_SECURITY_PROBLEM', 'FMFD_URLASFILENAME', 'URLOpenPullStream',
    'URLACTION_ACTIVEX_CURR_MAX', 'CFSTR_MIME_XBM', 'CFSTR_MIME_SVG_XML',
    'MUTZ_ACCEPT_WILDCARD_SCHEME', 'URLACTION_SCRIPT_SAFE_ACTIVEX',
    'SetUrlPolicyPermissions', 'SID_SInternetHostSecurityManager', 'PI_FLAGS',
    'Uri_HAS_HOST_TYPE', 'URLACTION_HTML_SUBMIT_FORMS_TO', 'IOInetProtocol',
    'Uri_HAS_SCHEME_NAME', 'URLACTION_ACTIVEX_OVERRIDE_REPURPOSEDETECTION',
    'URLACTION_SHELL_VERB', '__REQUIRED_RPCNDR_H_VERSION__', 'CFSTR_MIME_WAV',
    'Uri_HAS_ABSOLUTE_URI', 'Uri_CREATE_DECODE_EXTRA_INFO', 'SZ_ASYNC_CALLEE',
    'URLACTION_NETWORK_MAX', 'URLPOLICY_CREDENTIALS_MUST_PROMPT_USER',
    'INET_E_RESULT_DISPATCHED', 'INET_E_CODE_INSTALL_BLOCKED_ARM', 'BINDINFO',
    'Uri_CREATE_IE_SETTINGS', 'URLACTION_HTML_SUBFRAME_NAVIGATE', 'SZM_FLAGS',
    'INET_E_CODE_INSTALL_BLOCKED_BITNESS', 'URLOSTRM_GETNEWESTVERSION',
    'URLACTION_INFODELIVERY_NO_EDITING_SUBSCRIPTIONS', 'INET_E_REDIRECTING',
    'URLACTION_ALLOW_CROSSDOMAIN_DROP_ACROSS_WINDOWS', 'IID_IOInetBindInfo',
    'URLACTION_SCRIPT_CURR_MAX', 'URLPOLICY_CHANNEL_SOFTDIST_PRECACHE',
    'URLACTION_INFODELIVERY_NO_ADDING_SUBSCRIPTIONS', 'SOFTDIST_ADSTATE_NONE',
    'CFSTR_MIME_X_WMF', 'IOInetProtocolRoot', 'URLPOLICY_DISALLOW',
    'URLACTION_DOWNLOAD_MAX', 'URLACTION_ACTIVEX_CONFIRM_NOOBJECTSAFETY',
    'URLACTION_JAVA_MAX', 'INET_E_USE_EXTEND_BINDING', 'IID_IOInetSession',
    'URLACTION_INPRIVATE_BLOCKING', 'URLACTION_AUTOMATIC_DOWNLOAD_UI',
    'MUTZ_IGNORE_ZONE_MAPPINGS', 'INET_E_REDIRECT_TO_DIR', 'CFSTR_MIME_MPEG',
    'URLPOLICY_NOTIFY_ON_ALLOW', 'INET_E_CODE_DOWNLOAD_DECLINED', 'PSUACTION',
    'IID_IOInetProtocolRoot', 'Uri_PUNYCODE_IDN_HOST', 'CFSTR_MIME_RICHTEXT',
    'URLOpenBlockingStream', 'URLPOLICY_JAVA_CUSTOM', 'URLACTION_SHELL_SHARE',
    'URLACTION_FEATURE_FORCE_ADDR_AND_STATUS', 'URLMON_OPTION_USERAGENT',
    'URLACTION_ACTIVEX_SCRIPTLET_RUN', 'PI_DOCFILECLSIDLOOKUP', 'BINDSTRING',
    'URLACTION_INFODELIVERY_MIN', 'MAX_SIZE_SECURITY_ID', 'CFSTR_MIME_WEBVTT',
    'URLACTION_SHELL_EXECUTE_HIGHRISK', 'LPOINETPROTOCOLSINK', 'PARSE_ENCODE',
    'INET_E_RESOURCE_NOT_FOUND', 'URLPOLICY_JAVA_MEDIUM', 'CFSTR_MIME_X_AIFF',
    'URLPOLICY_NOTIFY_ON_DISALLOW', 'URLACTION_SHELL_TOCTOU_RISK', 'DATAINFO',
    'URLACTION_INFODELIVERY_NO_ADDING_CHANNELS', 'URLACTION_HTML_MIN',
    'URLACTION_SHELL_SECURE_DRAGSOURCE', 'IOInetThreadSwitch', 'Uri_HAS_ZONE',
    'URLACTION_LOWRIGHTS', 'Uri_HAS_FRAGMENT', 'URLACTION_HTML_JAVA_RUN',
    'INET_E_DOMINJECTIONVALIDATION', 'IOInetProtocolInfo', 'CFSTR_MIME_X_WAV',
    'CFSTR_MIME_X_BITMAP', 'INET_E_BLOCKED_PLUGGABLE_PROTOCOL', 'BINDSTATUS',
    'URLACTION_SCRIPT_MAX', 'URLMON_OPTION_USERAGENT_REFRESH', 'FMFD_DEFAULT',
    'URLACTION_AUTHENTICATE_CLIENT', 'MUTZ_FORCE_INTRANET_FLAGS', 'LPBINDING',
    'PROTOCOLFLAG_NO_PICS_CHECK', 'CFSTR_MIME_HTA', 'FIEF_FLAG_RESERVED_0',
    'SET_FEATURE_ON_THREAD_INTRANET', 'FMFD_RESPECTTEXTPLAIN', 'PARSE_DECODE',
    'SID_SInternetSecurityManagerEx2', 'URLACTION_BEHAVIOR_RUN', 'CIP_STATUS',
    '__REQUIRED_RPCSAL_H_VERSION__', 'CFSTR_MIME_PDF', 'CFSTR_MIME_XHTML',
    'URLACTION_HTML_ALLOW_CROSS_DOMAIN_WEBWORKER', 'CFSTR_MIME_TEXT_JSON',
    'SOFTDIST_ADSTATE_DOWNLOADED', 'INET_E_BLOCKED_ENHANCEDPROTECTEDMODE',
    'SID_SInternetSecurityManagerEx', 'SET_FEATURE_ON_THREAD_LOCALMACHINE',
    'URLACTION_FEATURE_WINDOW_RESTRICTIONS', 'LPOINETSESSION', 'URL_ENCODING',
    'INET_E_CODE_INSTALL_BLOCKED_IMMERSIVE', 'INET_E_DEFAULT_ACTION',
    'URLACTION_INFODELIVERY_NO_CHANNEL_LOGGING', 'URLDownloadToCacheFile',
    'URLACTION_DOWNLOAD_UNSIGNED_ACTIVEX', 'SET_FEATURE_ON_PROCESS',
    'URLACTION_ACTIVEX_OVERRIDE_DATA_SAFETY', 'Uri_CREATE_NO_IE_SETTINGS',
    'URLACTION_ALLOW_AUDIO_VIDEO_PLUGINS', 'SOFTDIST_FLAG_USAGE_EMAIL',
    'OInetCombineUrl', 'URLACTION_WINDOWS_BROWSER_APPLICATIONS', 'tagURLZONE',
    'URLACTION_INFODELIVERY_NO_REMOVING_CHANNELS', 'URLPOLICY_JAVA_PROHIBIT',
    'MK_S_ASYNCHRONOUS', 'URLACTION_SHELL_ALLOW_CROSS_SITE_SHARE',
    'SOFTDIST_ADSTATE_INSTALLED', 'URLACTION_SHELL_SHELLEXECUTE',
    'INET_E_QUERYOPTION_UNKNOWN', 'URLACTION_HTML_ALLOW_INDEXEDDB',
    'URLACTION_NETWORK_MIN', 'URLPOLICY_LOG_ON_ALLOW', 'URL_MK_UNIFORM',
    'INET_E_ERROR_FIRST', 'Uri_CREATE_CANONICALIZE', 'IID_IOInetProtocolSink',
    'FMFD_RETURNUPDATEDIMGMIMES', 'Uri_ENCODING_QUERY_AND_FRAGMENT_IS_CP',
    'URLACTION_SHELL_ENHANCED_DRAGDROP_SECURITY', 'BINDF_NOCOPYDATA',
    'URLPOLICY_CHANNEL_SOFTDIST_AUTOINSTALL', 'URL_MK_NO_CANONICALIZE',
    'FIEF_FLAG_SKIP_INSTALLED_VERSION_CHECK', 'CFSTR_MIME_TEXT', 'URLZONEREG',
    'CFSTR_MIME_X_SGI_MOVIE', 'IID_IOInetProtocolEx', 'FIEF_FLAG_PEEK',
    'UriBuilder_USE_ORIGINAL_FLAGS', 'OInetParseUrl', 'IID_IOInetPriority',
    'FMFD_SERVERMIME', 'Uri_CREATE_NOFRAG', 'URLOpenStream', 'SZ_URLCONTEXT',
    'SOFTDIST_FLAG_USAGE_PRECACHE', 'URLACTION_SCRIPT_XSSFILTER',
    'SET_FEATURE_IN_REGISTRY', 'URLPOLICY_CREDENTIALS_CONDITIONAL_PROMPT',
    'IOInetProtocolSinkStackable', 'CFSTR_MIME_BMP', 'UAS_EXACTLEGACY',
    'Uri_CREATE_ALLOW_RELATIVE', 'GET_FEATURE_FROM_THREAD_INTRANET',
    'IOInetProtocolEx', 'URLACTION_ALLOW_CROSSDOMAIN_DROP_WITHIN_WINDOW',
    'Uri_HAS_USER_NAME', 'INET_E_TERMINATED_BIND', 'CFSTR_MIME_BASICAUDIO',
    'Uri_CREATE_NORMALIZE_INTL_CHARACTERS', 'URLACTION_COOKIES', 'StartParam',
    'URLACTION_SHELL_EXECUTE_LOWRISK', 'FMFD_IGNOREMIMETEXTPLAIN',
    'Uri_HAS_QUERY', 'URLACTION_FEATURE_CROSSDOMAIN_FOCUS_CHANGE',
    'URLACTION_BEHAVIOR_MIN', 'URLACTION_SHELL_CURR_MAX', 'Uri_HAS_EXTENSION',
    'CFSTR_MIME_APPLICATION_JAVASCRIPT', 'URLACTION_ACTIVEX_ALLOW_TDC',
    'SOFTDIST_FLAG_DELETE_SUBSCRIPTION', 'SID_SInternetSecurityManager',
    'INET_E_DOWNLOAD_BLOCKED_BY_INPRIVATE', 'URLACTION_CHANNEL_SOFTDIST_MAX',
    'Uri_HAS_PATH_AND_QUERY', 'IID_IOInetProtocolSinkStackable', 'LPBINDHOST',
    'URLACTION_SHELL_RTF_OBJECTS_LOAD', 'URLACTION_ALLOW_APEVALUATION',
    'URLACTION_ALLOW_ZONE_ELEVATION_VIA_OPT_OUT', 'INET_E_INVALID_URL',
    'URLACTION_SHELL_EXECUTE_MODRISK', 'URLACTION_ALLOW_AUDIO_VIDEO',
    'Uri_CREATE_NO_CRACK_UNKNOWN_SCHEMES', 'Uri_HAS_PASSWORD', '_tagPI_FLAGS',
    'Uri_ENCODING_USER_INFO_AND_PATH_IS_PERCENT_ENCODED_UTF8', 'IEObjectType',
    'Uri_HAS_RAW_URI', 'Uri_CREATE_CRACK_UNKNOWN_SCHEMES', 'CFSTR_MIME_TTAF',
    'URLPOLICY_AUTHENTICATE_CHALLENGE_RESPONSE', 'URLACTION_COOKIES_SESSION',
    'INET_E_USE_DEFAULT_PROTOCOLHANDLER', 'INET_E_DOWNLOAD_FAILURE',
    'URLACTION_ACTIVEX_NO_WEBOC_SCRIPT', 'SET_FEATURE_ON_THREAD_TRUSTED',
    'URLACTION_HTML_FONT_DOWNLOAD', 'INET_E_OBJECT_NOT_FOUND', 'QUERYOPTION',
    'Uri_ENCODING_HOST_IS_PERCENT_ENCODED_UTF8', 'INET_E_ERROR_LAST',
    'Uri_CREATE_NO_ENCODE_FORBIDDEN_CHARACTERS', 'INET_E_RESERVED_1',
    'INET_E_RESERVED_3', 'INET_E_RESERVED_2', 'INET_E_RESERVED_4',
    'IOInetProtocolSink', 'URLACTION_SHELL_POPUPMGR', 'IID_IOInetBindInfoEx',
    'URLACTION_SHELL_MOVE_OR_COPY', 'CFSTR_MIME_QUICKTIME', 'FMFD_RESERVED_1',
    'URLACTION_HTML_ALLOW_CROSS_DOMAIN_TEXTTRACK', 'URLACTION_JAVA_CURR_MAX',
    'URLACTION_HTML_REQUIRE_UTF8_DOCUMENT_CODEPAGE', 'BINDF_DONTUSECACHE',
    'URLACTION_SHELL_MAX', 'CFSTR_MIME_X_ICON', 'CFSTR_MIME_RAWDATASTRM',
    'SOFTDIST_ADSTATE_AVAILABLE', 'INET_E_REDIRECT_FAILED', 'OInetQueryInfo',
    'URLPOLICY_LOG_ON_DISALLOW', 'URLACTION_DOWNLOAD_CURR_MAX', '_URLZONEREG',
    'URLACTION_ACTIVEX_OVERRIDE_OBJECT_SAFETY', 'INET_E_FORBIDFRAMING',
    'OInetCombineIUri', 'URLACTION_COOKIES_THIRD_PARTY', 'CFSTR_MIME_GIF',
    'SET_FEATURE_ON_THREAD_RESTRICTED', 'URLACTION_ACTIVEX_OVERRIDE_OPTIN',
    'GET_FEATURE_FROM_PROCESS', 'URLACTION_SHELL_INSTALL_DTITEMS',
    'URLACTION_FEATURE_DATA_BINDING', 'URLACTION_DOTNET_USERCONTROLS',
    'URLACTION_SCRIPT_MIN', 'URLACTION_HTML_SUBMIT_FORMS_FROM', 'PARSEACTION',
    'INET_E_CANNOT_INSTANTIATE_OBJECT', 'URLACTION_FEATURE_SCRIPT_STATUS_BAR',
    'URLACTION_WINFX_SETUP', 'Uri_CREATE_NO_DECODE_EXTRA_INFO', 'URLTEMPLATE',
    'URLACTION_INFODELIVERY_NO_EDITING_CHANNELS', 'INET_E_DATA_NOT_AVAILABLE',
    'URLACTION_HTML_MIXED_CONTENT', 'URLACTION_SHELL_WEBVIEW_VERB',
    'URLACTION_HTML_USERDATA_SAVE', 'IsLoggingEnabled', 'IOInetBindInfoEx',
    'URLACTION_HTML_SUBMIT_FORMS', 'URLACTION_ACTIVEX_MAX', 'S_ASYNCHRONOUS',
    'URLACTION_HTML_ALLOW_CROSS_DOMAIN_CANVAS', 'CFSTR_MIME_TTML',
    'INET_E_BLOCKED_REDIRECT_XSECURITYID', 'CFSTR_MIME_JPEG', 'IOInetSession',
    'URLACTION_CHANNEL_SOFTDIST_PERMISSIONS', 'FIEF_FLAG_FORCE_JITUI',
    'URLACTION_ALLOW_ZONE_ELEVATION_OPT_OUT_ADDITION', 'CFSTR_MIME_AVI',
    'Uri_CREATE_NO_PRE_PROCESS_HTML_URI', 'Uri_HAS_DISPLAY_URI',
    'Uri_CREATE_ALLOW_IMPLICIT_FILE_SCHEME', 'URLMON_OPTION_URL_ENCODING',
    'GET_FEATURE_FROM_THREAD_RESTRICTED', 'OInetCombineUrlEx', 'Uri_PROPERTY',
    'URLPOLICY_BEHAVIOR_CHECK_LIST', 'INET_E_USE_DEFAULT_SETTING',
    'CFSTR_MIME_X_JAVASCRIPT', 'URLPOLICY_AUTHENTICATE_CLEARTEXT_OK',
    'URLPOLICY_DONTCHECKDLGBOX', 'Uri_CREATE_PRE_PROCESS_HTML_URI',
    'Uri_DISPLAY_IDN_HOST', 'URLACTION_HTML_ALLOW_INJECTED_DYNAMIC_HTML',
    'CFSTR_MIME_APP_XML', 'INVALID_P_ROOT_SECURITY_ID', 'CFSTR_MIME_FRACTALS',
    'URLMON_OPTION_USE_BINDSTRINGCREDS', 'URLACTION_XPS_DOCUMENTS',
    'URLPOLICY_CREDENTIALS_SILENT_LOGON_OK', 'CFSTR_MIME_MANIFEST',
    'URLACTION_ALLOW_RENDER_LEGACY_DXTFILTERS', 'CFSTR_MIME_POSTSCRIPT',
    'INET_E_AUTHENTICATION_REQUIRED', 'URLPOLICY_CHANNEL_SOFTDIST_PROHIBIT',
    'MUTZ_NOSAVEDFILECHECK', 'Uri_CREATE_CANONICALIZE_ABSOLUTE',
    'INET_E_NO_SESSION', 'URLACTION_ALLOW_ACTIVEX_FILTERING', 'AUTHENTICATEF',
    'URLACTION_CHANNEL_SOFTDIST_MIN',
    'INET_E_CODE_INSTALL_SUPPRESSED', 'IID_IOInetProtocolInfo', 'RemBINDINFO',
    'CFSTR_MIME_AIFF', 'MKSYS_URLMONIKER', 'Uri_DISPLAY_NO_FRAGMENT',
    'URLPOLICY_AUTHENTICATE_MUTUAL_ONLY', '_tagINTERNETFEATURELIST',
    '__MIDL_IInternetZoneManager_0002', '_tagPARSEACTION', 'Uri_HOST_TYPE',
    '__MIDL_IBindStatusCallback_0004', '__MIDL_ICodeInstall_0001',
    'MONIKERPROPERTY', '__MIDL_IMonikerProp_0001', 'tagURLTEMPLATE',
    '__MIDL_IBindStatusCallback_0003', '__MIDL_IAuthenticateEx_0001',
    '__MIDL_IBindStatusCallbackEx_0001', 'tagBINDSTRING', 'tagBINDSTATUS',
    '_tagQUERYOPTION', '__MIDL_IBindStatusCallback_0006', 'BINDHANDLETYPES',
    '__MIDL_IBindStatusCallback_0005', '__MIDL_IBindStatusCallback_0002',
    '__MIDL_IBindStatusCallback_0001', '__MIDL_IUri_0001', '__MIDL_IUri_0002',
    'INTERNETFEATURELIST', '_tagOIBDG_FLAGS', '_tagPSUACTION', 'SOFTDISTINFO',
    'BINDINFO_OPTIONS', '__MIDL_IInternetSecurityManager_0001', 'LPIINTERNET',
    '__MIDL_IGetBindHandle_0001', '__MIDL_IInternetSecurityManager_0003',
    '__MIDL_IInternetSecurityManager_0002', '_ZONEATTRIBUTES', 'RemFORMATETC',
    '_REMSECURITY_ATTRIBUTES', '_tagPROTOCOLDATA', 'ZONEATTRIBUTES',
    'LPHIT_LOGGING_INFO', '_tagRemBINDINFO', 'HIT_LOGGING_INFO',
    'LPREMFORMATETC', '_tagPROTOCOL_ARGUMENT', 'PREMSECURITY_ATTRIBUTES',
    'tagRemFORMATETC', 'LPSOFTDISTINFO', '_tagPROTOCOLFILTERDATA',
    'LPREMSECURITY_ATTRIBUTES', 'CONFIRMSAFETY', '_tagDATAINFO',
    '_tagBINDINFO', 'LPCODEBASEHOLD', 'REMSECURITY_ATTRIBUTES',
    '_tagSOFTDISTINFO', '_tagAUTHENTICATEINFO', 'LPZONEATTRIBUTES',
    '_tagHIT_LOGGING_INFO', 'AUTHENTICATEINFO', 'PROTOCOLFILTERDATA',
    '_tagCODEBASEHOLD', 'PROTOCOL_ARGUMENT', 'PROTOCOLDATA', 'CODEBASEHOLD',
    '_tagStartParam', 'LPPROTOCOL_ARGUMENT', 'LPIINTERNETPRIORITY',
    'LPIINTERNETPROTOCOLSINKStackable', 'LPHTTPNEGOTIATE2', 'LPGETBINDHANDLE',
    'LPHTTPNEGOTIATE3', 'LPIINTERNETPROTOCOL', 'LPAUTHENTICATION',
    'LPIINTERNETBINDINFOEX', 'LPBINDSTATUSCALLBACKEX', 'LPIINTERNETSESSION',
    'LPIWRAPPEDPROTOCOL', 'LPIINTERNETPROTOCOLROOT', 'LPBINDPROTOCOL',
    'LPIINTERNETPROTOCOLSINK', 'LPWININETINFO', 'LPHTTPNEGOTIATE',
    'LPWININETHTTPINFO', 'LPDATAFILTER', 'LPAUTHENTICATIONEX',
    'LPBINDSTATUSCALLBACK', 'LPENCODINGFILTERFACTORY', 'LPCATALOGFILEINFO',
    'LPHTTPSECURITY', 'LPCODEINSTALL', 'LPURLZONEMANAGER', 'LPMONIKERPROP',
    'LPWININETCACHEHINTS', 'LPIINTERNETTHREADSWITCH', 'LPIINTERNETBINDINFO',
    'LPIINTERNETPROTOCOLINFO', 'LPWINDOWFORBINDINGUI', 'LPPERSISTMONIKER',
    'LPBINDCALLBACKREDIRECT', 'LPWININETFILESTREAM', 'LPWININETCACHEHINTS2',
)
