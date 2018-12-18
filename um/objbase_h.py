import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_OBJBASE_H_ = None
_WIN32_DCOM = None
_OLE32_ = None
_OLE32PRIV_ = None


from pyWinAPI.shared.winapifamily_h import * # NOQA

# + ---------------------------------------------------------------------------
# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.
# File:  objbase.h
# Contents: Component object model definitions.
# ----------------------------------------------------------------------------
from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA

if not defined(_OBJBASE_H_):
    _OBJBASE_H_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.pshpack8_h import * # NOQA
    from pyWinAPI.um.combaseapi_h import * # NOQA
    from pyWinAPI.um.coml2api_h import * # NOQA

    # COM initialization flags; passed to CoInitialize.
    class tagCOINIT(ENUM):
        COINIT_APARTMENTTHREADED = 0x2
        if _WIN32_WINNT >= 0x0400 or defined(_WIN32_DCOM):
            COINIT_MULTITHREADED = COINITBASE.COINITBASE_MULTITHREADED
            COINIT_DISABLE_OLE1DDE = 0x4
            COINIT_SPEED_OVER_MEMORY = 0x8
        # END IF

        COINIT = tagCOINIT

    # interface marshaling definitions
    MARSHALINTERFACE_MIN = 500 # minimum number of bytes for interface marshal

    # flags for internet asynchronous and layout docfile
    ASYNC_MODE_COMPATIBILITY = 0x00000001
    ASYNC_MODE_DEFAULT = 0x00000000
    STGTY_REPEAT = 0x00000100
    STG_TOEND = 0xFFFFFFFF
    STG_LAYOUT_SEQUENTIAL = 0x00000000
    STG_LAYOUT_INTERLEAVED = 0x00000001

    from pyWinAPI.um.objidl_h import * # NOQA

    ole32 = ctypes.windll.OLE32
    dflayout = ctypes.windll.DFLAYOUT

    if defined(_OLE32_):
        if defined(_OLE32PRIV_):
            pass
        else:
            __INLINE_ISEQUAL_GUID = VOID
        # END IF   _OLE32PRIV_
    # END IF   _OLE32_

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # **** STD Object API Prototypes
        # ***************************************

        # WINOLEAPI_(DWORD) CoBuildVersion( VOID );
        CoBuildVersion = ole32.CoBuildVersion
        CoBuildVersion.restype = WINOLEAPI_(DWORD)

        # init/uninit
        # _Check_return_ WINOLEAPI  CoInitialize(_In_opt_ LPVOID pvReserved);
        CoInitialize = ole32.CoInitialize
        CoInitialize.restype = WINOLEAPI

        COM_SUPPORT_MALLOC_SPIES = VOID

        # _Check_return_ WINOLEAPI  CoRegisterMallocSpy(_In_ LPMALLOCSPY pMallocSpy);
        CoRegisterMallocSpy = ole32.CoRegisterMallocSpy
        CoRegisterMallocSpy.restype = WINOLEAPI

        if _WIN32_WINNT >= 0x0501:
            # _Check_return_ WINOLEAPI  CoRegisterInitializeSpy(_In_ IInitializeSpy *pSpy, _Out_ ULARGE_INTEGER *puliCookie);
            CoRegisterInitializeSpy = ole32.CoRegisterInitializeSpy
            CoRegisterInitializeSpy.restype = WINOLEAPI

            # _Check_return_ WINOLEAPI  CoRevokeInitializeSpy(_In_ ULARGE_INTEGER uliCookie);
            CoRevokeInitializeSpy = ole32.CoRevokeInitializeSpy
            CoRevokeInitializeSpy.restype = WINOLEAPI

            # COM System Security Descriptors
            # (used when the corresponding registry
            # entries are absent)
            class tagCOMSD(ENUM):
                SD_LAUNCHPERMISSIONS = 0
                SD_ACCESSPERMISSIONS = 1
                SD_LAUNCHRESTRICTIONS = 2
                SD_ACCESSRESTRICTIONS = 3

            COMSD = tagCOMSD

            # _Check_return_ WINOLEAPI  CoGetSystemSecurityPermissions(COMSD comSDType, PSECURITY_DESCRIPTOR *ppSD);
            CoGetSystemSecurityPermissions = (
                ole32.CoGetSystemSecurityPermissions
            )
            CoGetSystemSecurityPermissions.restype = WINOLEAPI

        # END IF

        # dll loading helpers; keeps track of ref counts and unloads all on
        # exit
        # WINOLEAPI_(HINSTANCE) CoLoadLibrary(_In_ LPOLESTR lpszLibName, _In_ BOOL bAutoFree);
        CoLoadLibrary = ole32.CoLoadLibrary
        CoLoadLibrary.restype = WINOLEAPI_(HINSTANCE)

        # WINOLEAPI_(VOID) CoFreeLibrary(_In_ HINSTANCE hInst);
        CoFreeLibrary = ole32.CoFreeLibrary
        CoFreeLibrary.restype = WINOLEAPI_(VOID)

        if (_WIN32_WINNT >= 0x0400) or defined(_WIN32_DCOM):
            # _Check_return_ WINOLEAPI CoGetInstanceFromFile(
            # _In_opt_ COSERVERINFO *            pServerInfo,
            # _In_opt_ CLSID        *            pClsid,
            # _In_opt_ IUnknown     *            punkOuter, // only relevant locally
            # _In_ DWORD                         dwClsCtx,
            # _In_ DWORD                         grfMode,
            # _In_ _Null_terminated_ OLECHAR *    pwszName,
            # _In_ DWORD                         dwCount,
            # _Inout_updates_(dwCount) MULTI_QI * pResults );
            CoGetInstanceFromFile = ole32.CoGetInstanceFromFile
            CoGetInstanceFromFile.restype = WINOLEAPI

            # _Check_return_ WINOLEAPI CoGetInstanceFromIStorage(
            # _In_opt_ COSERVERINFO *            pServerInfo,
            # _In_opt_ CLSID        *            pClsid,
            # _In_opt_ IUnknown     *            punkOuter, // only relevant locally
            # _In_ DWORD                         dwClsCtx,
            # _In_ struct IStorage  *            pstg,
            # _In_ DWORD                         dwCount,
            # _Inout_updates_(dwCount) MULTI_QI * pResults );
            CoGetInstanceFromIStorage = ole32.CoGetInstanceFromIStorage
            CoGetInstanceFromIStorage.restype = WINOLEAPI

        # END IF   DCOM

        # Call related APIs
        if (_WIN32_WINNT >= 0x0500) or defined(_WIN32_DCOM):
            # WINOLEAPI CoAllowSetForegroundWindow(_In_ IUnknown *pUnk, _In_opt_ LPVOID lpvReserved);
            CoAllowSetForegroundWindow = ole32.CoAllowSetForegroundWindow
            CoAllowSetForegroundWindow.restype = WINOLEAPI

            # WINOLEAPI DcomChannelSetHResult(_In_opt_ LPVOID pvReserved, _In_opt_ ULONG* pulReserved, _In_ HRESULT appsHR);
            DcomChannelSetHResult = ole32.DcomChannelSetHResult
            DcomChannelSetHResult.restype = WINOLEAPI

        # END IF

        # other helpers
        # WINOLEAPI_(BOOL) CoIsOle1Class(_In_ REFCLSID rclsid);
        CoIsOle1Class = ole32.CoIsOle1Class
        CoIsOle1Class.restype = WINOLEAPI_(BOOL)

        # WINOLEAPI_(BOOL) CoFileTimeToDosDateTime(
        # _In_ FILETIME FAR* lpFileTime, _Out_ LPWORD lpDosDate, _Out_ LPWORD lpDosTime);
        CoFileTimeToDosDateTime = ole32.CoFileTimeToDosDateTime
        CoFileTimeToDosDateTime.restype = WINOLEAPI_(BOOL)

        # WINOLEAPI_(BOOL) CoDosDateTimeToFileTime(
        # _In_ WORD nDosDate, _In_ WORD nDosTime, _Out_ FILETIME FAR* lpFileTime);
        CoDosDateTimeToFileTime = ole32.CoDosDateTimeToFileTime
        CoDosDateTimeToFileTime.restype = WINOLEAPI_(BOOL)

        # WINOLEAPI  CoFileTimeNow( _Out_ FILETIME FAR* lpFileTime );
        CoFileTimeNow = ole32.CoFileTimeNow
        CoFileTimeNow.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI CoRegisterMessageFilter( _In_opt_ LPMESSAGEFILTER lpMessageFilter,
        # _Outptr_opt_result_maybenull_ LPMESSAGEFILTER FAR* lplpMessageFilter );
        CoRegisterMessageFilter = ole32.CoRegisterMessageFilter
        CoRegisterMessageFilter.restype = WINOLEAPI

        if (_WIN32_WINNT >= 0x0400) or defined(_WIN32_DCOM):
            # WINOLEAPI CoRegisterChannelHook( _In_ REFGUID ExtensionUuid, _In_ IChannelHook *pChannelHook );
            CoRegisterChannelHook = ole32.CoRegisterChannelHook
            CoRegisterChannelHook.restype = WINOLEAPI

        # END IF   DCOM

        # TreatAs APIS
        # _Check_return_ WINOLEAPI CoTreatAsClass(_In_ REFCLSID clsidOld, _In_ REFCLSID clsidNew);
        CoTreatAsClass = ole32.CoTreatAsClass
        CoTreatAsClass.restype = WINOLEAPI

        # **** DV APIs
        # *********************************************************
        # WINOLEAPI CreateDataAdviseHolder(_Outptr_ LPDATAADVISEHOLDER FAR* ppDAHolder);
        CreateDataAdviseHolder = ole32.CreateDataAdviseHolder
        CreateDataAdviseHolder.restype = WINOLEAPI

        # WINOLEAPI CreateDataCache(_In_opt_ LPUNKNOWN pUnkOuter, _In_ REFCLSID rclsid,
        # _In_ REFIID iid, _Out_ LPVOID FAR* ppv);
        CreateDataCache = ole32.CreateDataCache
        CreateDataCache.restype = WINOLEAPI

        # **** Storage API Prototypes
        # ******************************************
        # _Check_return_ WINOLEAPI StgOpenAsyncDocfileOnIFillLockBytes( _In_ IFillLockBytes *pflb,
        # _In_ DWORD grfMode,
        # _In_ DWORD asyncFlags,
        # _Outptr_ IStorage** ppstgOpen);
        StgOpenAsyncDocfileOnIFillLockBytes = (
            ole32.StgOpenAsyncDocfileOnIFillLockBytes
        )
        StgOpenAsyncDocfileOnIFillLockBytes.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI StgGetIFillLockBytesOnILockBytes( _In_ ILockBytes *pilb,
        # _Outptr_ IFillLockBytes** ppflb);
        StgGetIFillLockBytesOnILockBytes = (
            ole32.StgGetIFillLockBytesOnILockBytes
        )
        StgGetIFillLockBytesOnILockBytes.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI StgGetIFillLockBytesOnFile(_In_ _Null_terminated_ OLECHAR *pwcsName,
        # _Outptr_ IFillLockBytes** ppflb);
        StgGetIFillLockBytesOnFile = ole32.StgGetIFillLockBytesOnFile
        StgGetIFillLockBytesOnFile.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI StgOpenLayoutDocfile(_In_ _Null_terminated_ OLECHAR *pwcsDfName,
        # _In_ DWORD grfMode,
        # _In_ DWORD reserved,
        # _Outptr_ IStorage** ppstgOpen);
        StgOpenLayoutDocfile = dflayout.StgOpenLayoutDocfile
        StgOpenLayoutDocfile.restype = WINOLEAPI


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        ole32 = ctypes.windll.OLE32


        # WINOLEAPI  CoInstall(
        # _In_ IBindCtx     * pbc,
        # _In_ DWORD          dwFlags,
        # _In_ uCLSSPEC     * pClassSpec,
        # _In_ QUERYCONTEXT * pQuery,
        # _In_ LPWSTR         pszCodeBase);
        CoInstall = ole32.CoInstall
        CoInstall.restype = WINOLEAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP):
        # Moniker APIs
        # _Check_return_ WINOLEAPI  BindMoniker(_In_ LPMONIKER pmk, _In_ DWORD grfOpt, _In_ REFIID iidResult, _Outptr_ LPVOID FAR* ppvResult);
        BindMoniker = ole32.BindMoniker
        BindMoniker.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  CoGetObject(_In_ LPCWSTR pszName, _In_opt_ BIND_OPTS *pBindOptions, _In_ REFIID riid, _Outptr_ VOID **ppv);
        CoGetObject = ole32.CoGetObject
        CoGetObject.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  MkParseDisplayName(_In_ LPBC pbc, _In_ LPCOLESTR szUserName,
        # _Out_ ULONG FAR * pchEaten, _Outptr_ LPMONIKER FAR * ppmk);
        MkParseDisplayName = ole32.MkParseDisplayName
        MkParseDisplayName.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  MonikerRelativePathTo(_In_ LPMONIKER pmkSrc, _In_ LPMONIKER pmkDest, _Outptr_ LPMONIKER
        # FAR* ppmkRelPath, _In_ BOOL dwReserved);
        MonikerRelativePathTo = ole32.MonikerRelativePathTo
        MonikerRelativePathTo.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  MonikerCommonPrefixWith(_In_ LPMONIKER pmkThis, _In_ LPMONIKER pmkOther,
        # _Outptr_ LPMONIKER FAR* ppmkCommon);
        MonikerCommonPrefixWith = ole32.MonikerCommonPrefixWith
        MonikerCommonPrefixWith.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  CreateBindCtx(_In_ DWORD reserved, _Outptr_ LPBC FAR* ppbc);
        CreateBindCtx = ole32.CreateBindCtx
        CreateBindCtx.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  CreateGenericComposite(_In_opt_ LPMONIKER pmkFirst, _In_opt_ LPMONIKER pmkRest,
        # _Outptr_ LPMONIKER FAR* ppmkComposite);
        CreateGenericComposite = ole32.CreateGenericComposite
        CreateGenericComposite.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  CreateClassMoniker(_In_ REFCLSID rclsid, _Outptr_ LPMONIKER FAR* ppmk);
        CreateClassMoniker = ole32.CreateClassMoniker
        CreateClassMoniker.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  CreateFileMoniker(_In_ LPCOLESTR lpszPathName, _Outptr_ LPMONIKER FAR* ppmk);
        CreateFileMoniker = ole32.CreateFileMoniker
        CreateFileMoniker.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  CreateItemMoniker(_In_ LPCOLESTR lpszDelim, _In_ LPCOLESTR lpszItem,
        # _Outptr_ LPMONIKER FAR* ppmk);
        CreateItemMoniker = ole32.CreateItemMoniker
        CreateItemMoniker.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  CreateAntiMoniker(_Outptr_ LPMONIKER FAR* ppmk);
        CreateAntiMoniker = ole32.CreateAntiMoniker
        CreateAntiMoniker.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  CreatePointerMoniker(_In_opt_ LPUNKNOWN punk, _Outptr_ LPMONIKER FAR* ppmk);
        CreatePointerMoniker = ole32.CreatePointerMoniker
        CreatePointerMoniker.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI  CreateObjrefMoniker(_In_opt_ LPUNKNOWN punk, _Outptr_ LPMONIKER FAR * ppmk);
        CreateObjrefMoniker = ole32.CreateObjrefMoniker
        CreateObjrefMoniker.restype = WINOLEAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # _Check_return_ WINOLEAPI  GetRunningObjectTable( _In_ DWORD reserved, _Outptr_ LPRUNNINGOBJECTTABLE FAR* pprot);
        GetRunningObjectTable = ole32.GetRunningObjectTable
        GetRunningObjectTable.restype = WINOLEAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    from pyWinAPI.um.urlmon_h import * # NOQA
    from pyWinAPI.um.propidl_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Standard Progress Indicator implementation
        # WINOLEAPI CreateStdProgressIndicator(_In_ HWND hwndParent,
        # _In_ LPCOLESTR pszTitle,
        # _In_ IBindStatusCallback * pIbscCaller,
        # _Outptr_ IBindStatusCallback ** ppIbsc);
        CreateStdProgressIndicator = ole32.CreateStdProgressIndicator
        CreateStdProgressIndicator.restype = WINOLEAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if not defined(RC_INVOKED):
        from pyWinAPI.shared.poppack_h import * # NOQA
    # END IF   RC_INVOKED
# END IF   __OBJBASE_H__


