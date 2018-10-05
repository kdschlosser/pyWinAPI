

from .wtypes_h import (
    ENUM,
    HINSTANCE,
    VOID,
    BOOL,
)
import ctypes


# combase = ctypes.windll.ComBase
ole32 = ctypes.windll.Ole32

from .winapifamily_h import * # NOQA
# +---------------------------------------------------------------------------

# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.

# File:       objbase.h

# Contents:   Component object model definitions.

# ----------------------------------------------------------------------------
# from .rpc_h import * # NOQA
# from .rpcndr_h import * # NOQA
# from .pshpack8_h import * # NOQA
from .combaseapi_h import * # NOQA
# from .coml2api_h import * # NOQA
# COM initialization flags; passed to CoInitialize.

class tagCOINIT(ENUM):
    COINIT_APARTMENTTHREADED = 0x2
    #if  (_WIN32_WINNT > = 3
    COINIT_MULTITHREADED = tagCOINITBASE.COINITBASE_MULTITHREADED
    COINIT_DISABLE_OLE1DDE = 0x4
    COINIT_SPEED_OVER_MEMORY = 0x8
    #endif = 9


COINIT = tagCOINIT


# Apartment model
# DCOM
# These constants are only valid on Windows NT 4.0
# Don't use DDE for Ole1 support.
# Trade memory for speed.
# DCOM
# INTerface marshaling definitions
# minimum number of bytes for INTerface marshal
MARSHALINTERFACE_MIN = 0x000001F4
# flags for INTernet asynchronous and layout docfile
ASYNC_MODE_COMPATIBILITY = 0x00000001
ASYNC_MODE_DEFAULT = 0x00000000
STGTY_REPEAT = 0x00000100
STG_TOEND = 0xFFFFFFFF
STG_LAYOUT_SEQUENTIAL = 0x00000000
STG_LAYOUT_INTERLEAVED = 0x00000001
from .objidl_h import * # NOQA

# BOOL _fastcall wIsEqualGUID(REFGUID rguid1, REFGUID rguid2);
IsEqualGUID = ole32.IsEqualGUID
IsEqualGUID.restype = WINOLEAPI

# _OLE32PRIV_
# _OLE32_
# ***** STD Object API Prototypes ****************************************
# init/uninit
# COM System Security Descriptors (used when the corresponding registry
# entries are absent)

# WINOLEAPI_(DWORD) CoBuildVersion( VOID );
# CoBuildVersion = combase.CoBuildVersion
# CoBuildVersion.restype = WINOLEAPI

# _Check_return_ WINOLEAPI  CoInitialize(_In_opt_ LPVOID pvReserved);
CoInitialize = ole32.CoInitialize
CoInitialize.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  CoRegisterMallocSpy(_In_ LPMALLOCSPY pMallocSpy);
CoRegisterMallocSpy = ole32.CoRegisterMallocSpy
CoRegisterMallocSpy.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  CoRevokeMallocSpy(void);
CoRevokeMallocSpy = ole32.CoRevokeMallocSpy
CoRevokeMallocSpy.restype = WINOLEAPI

# WINOLEAPI  CoCreateStandardMalloc(_In_ DWORD memctx, _Outptr_ IMalloc FAR* FAR* ppMalloc);
# CoCreateStandardMalloc = combase.CoCreateStandardMalloc
# CoCreateStandardMalloc.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  CoRegisterInitializeSpy(_In_ IInitializeSpy *pSpy, _Out_ ULARGE_INTEGER *puliCookie);
CoRegisterInitializeSpy = ole32.CoRegisterInitializeSpy
CoRegisterInitializeSpy.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  CoRevokeInitializeSpy(_In_ ULARGE_INTEGER uliCookie);
CoRevokeInitializeSpy = ole32.CoRevokeInitializeSpy
CoRevokeInitializeSpy.restype = WINOLEAPI


class tagCOMSD(ENUM):
    SD_LAUNCHPERMISSIONS = 0
    SD_ACCESSPERMISSIONS = 1
    SD_LAUNCHRESTRICTIONS = 2
    SD_ACCESSRESTRICTIONS = 3


COMSD = tagCOMSD

# _Check_return_ WINOLEAPI  CoGetSystemSecurityPermissions(COMSD comSDType, PSECURITY_DESCRIPTOR *ppSD);
# CoGetSystemSecurityPermissions = combase.CoGetSystemSecurityPermissions
# CoGetSystemSecurityPermissions.restype = WINOLEAPI


# dll loading helpers; keeps track of ref counts and unloads all on exit

# WINOLEAPI_(HINSTANCE) CoLoadLibrary(_In_ LPOLESTR lpszLibName, _In_ BOOL bAutoFree);
CoLoadLibrary = ole32.CoLoadLibrary
CoLoadLibrary.restype = WINOLEAPI_(HINSTANCE)


# WINOLEAPI_(void) CoFreeLibrary(_In_ HINSTANCE hInst);
CoFreeLibrary = ole32.CoFreeLibrary
CoFreeLibrary.restype = WINOLEAPI_(VOID)


# WINOLEAPI_(void) CoFreeAllLibraries(void);
CoFreeAllLibraries = ole32.CoFreeAllLibraries
CoFreeAllLibraries.restype = WINOLEAPI_(VOID)


# Machine wide launch permissions
# Machine wide acesss permissions
# Machine wide launch limits
# Machine wide access limits
# dll loading helpers; keeps track of ref counts and unloads all on exit
# DCOM

# _Check_return_ WINOLEAPI CoGetInstanceFromFile(
#     _In_opt_ COSERVERINFO *            pServerInfo,
#     _In_opt_ CLSID        *            pClsid,
#     _In_opt_ IUnknown     *            punkOuter,
#     _In_ DWORD                         dwClsCtx,
#     _In_ DWORD                         grfMode,
#     _In_ _Null_terminated_ OLECHAR *    pwszName,
#     _In_ DWORD                         dwCount,
#     _Inout_updates_(dwCount) MULTI_QI * pResults );
# CoGetInstanceFromFile = combase.CoGetInstanceFromFile
# CoGetInstanceFromFile.restype = WINOLEAPI

# only relevant locally

# _Check_return_ WINOLEAPI CoGetInstanceFromIStorage(
#     _In_opt_ COSERVERINFO *            pServerInfo,
#     _In_opt_ CLSID        *            pClsid,
#     _In_opt_ IUnknown     *            punkOuter,
#     _In_ DWORD                         dwClsCtx,
#     _In_ struct IStorage  *            pstg,
#     _In_ DWORD                         dwCount,
#     _Inout_updates_(dwCount) MULTI_QI * pResults );
CoGetInstanceFromIStorage = ole32.CoGetInstanceFromIStorage
CoGetInstanceFromIStorage.restype = WINOLEAPI

# only relevant locally
# DCOM
# Call related APIs
# DCOM
# other helpers

# WINOLEAPI CoAllowSetForegroundWindow(_In_ IUnknown *pUnk, _In_opt_ LPVOID lpvReserved);

CoAllowSetForegroundWindow = ole32.CoAllowSetForegroundWindow
CoAllowSetForegroundWindow.restype = WINOLEAPI

# WINOLEAPI DcomChannelSetHResult(_In_opt_ LPVOID pvReserved, _In_opt_ ULONG* pulReserved, _In_ HRESULT appsHR);

# WINOLEAPI_(BOOL) CoIsOle1Class(_In_ REFCLSID rclsid);
# _Check_return_ WINOLEAPI CLSIDFromProgIDEx (_In_ LPCOLESTR lpszProgID, _Out_ LPCLSID lpclsid);

CoIsOle1Class = ole32.CoIsOle1Class
CoIsOle1Class.restype = WINOLEAPI

# WINOLEAPI_(BOOL) CoFileTimeToDosDateTime(
#                  _In_ FILETIME FAR* lpFileTime, _Out_ LPWORD lpDosDate, _Out_ LPWORD lpDosTime);
CoFileTimeToDosDateTime = ole32.CoFileTimeToDosDateTime
CoFileTimeToDosDateTime.restype = WINOLEAPI_(BOOL)


# WINOLEAPI_(BOOL) CoDosDateTimeToFileTime(
#                        _In_ WORD nDosDate, _In_ WORD nDosTime, _Out_ FILETIME FAR* lpFileTime);
CoDosDateTimeToFileTime = ole32.CoDosDateTimeToFileTime
CoDosDateTimeToFileTime.restype = WINOLEAPI_(BOOL)


# WINOLEAPI  CoFileTimeNow( _Out_ FILETIME FAR* lpFileTime );
CoFileTimeNow = ole32.CoFileTimeNow
CoFileTimeNow.restype = WINOLEAPI

# _Check_return_ WINOLEAPI CoRegisterMessageFilter( _In_opt_ LPMESSAGEFILTER lpMessageFilter,
#                               _Outptr_opt_result_maybenull_ LPMESSAGEFILTER FAR* lplpMessageFilter );
CoRegisterMessageFilter = ole32.CoRegisterMessageFilter
CoRegisterMessageFilter.restype = WINOLEAPI


# WINOLEAPI CoRegisterChannelHook( _In_ REFGUID ExtensionUuid, _In_ IChannelHook *pChannelHook );
# CoRegisterChannelHook = combase.CoRegisterChannelHook
# CoRegisterChannelHook.restype = WINOLEAPI


# _Check_return_ WINOLEAPI CoTreatAsClass(_In_ REFCLSID clsidOld, _In_ REFCLSID clsidNew);
CoTreatAsClass = ole32.CoTreatAsClass
CoTreatAsClass.restype = WINOLEAPI

# ***** DV APIs **********************************************************

# WINOLEAPI CreateDataAdviseHolder(_Outptr_ LPDATAADVISEHOLDER FAR* ppDAHolder);
CreateDataAdviseHolder = ole32.CreateDataAdviseHolder
CreateDataAdviseHolder.restype = WINOLEAPI

# WINOLEAPI CreateDataCache(_In_opt_ LPUNKNOWN pUnkOuter, _In_ REFCLSID rclsid,
#                          _In_ REFIID iid, _Out_ LPVOID FAR* ppv);
CreateDataCache = ole32.CreateDataCache
CreateDataCache.restype = WINOLEAPI

# ***** Storage API Prototypes *******************************************


# _Check_return_ WINOLEAPI StgOpenAsyncDocfileOnIFillLockBytes( _In_ IFillLockBytes *pflb,
#              _In_ DWORD grfMode,
#              _In_ DWORD asyncFlags,
#              _Outptr_ IStorage** ppstgOpen);
StgOpenAsyncDocfileOnIFillLockBytes = ole32.StgOpenAsyncDocfileOnIFillLockBytes
StgOpenAsyncDocfileOnIFillLockBytes.restype = WINOLEAPI


# _Check_return_ WINOLEAPI StgGetIFillLockBytesOnILockBytes( _In_ ILockBytes *pilb,
#              _Outptr_ IFillLockBytes** ppflb);
StgGetIFillLockBytesOnILockBytes = ole32.StgGetIFillLockBytesOnILockBytes
StgGetIFillLockBytesOnILockBytes.restype = WINOLEAPI


# _Check_return_ WINOLEAPI StgGetIFillLockBytesOnFile(_In_ _Null_terminated_ OLECHAR const *pwcsName,
#              _Outptr_ IFillLockBytes** ppflb);
StgGetIFillLockBytesOnFile = ole32.StgGetIFillLockBytesOnFile
StgGetIFillLockBytesOnFile.restype = WINOLEAPI


# _Check_return_ WINOLEAPI StgOpenLayoutDocfile(_In_ _Null_terminated_ OLECHAR const *pwcsDfName,
#              _In_ DWORD grfMode,
#              _In_ DWORD reserved,
#              _Outptr_ IStorage** ppstgOpen);
# StgOpenLayoutDocfile = ole32.StgOpenLayoutDocfile
# StgOpenLayoutDocfile.restype = WINOLEAPI

# DCOM
# DCOM
# TreatAs APIS
# ***** DV APIs **********************************************************
# ***** Storage API Prototypes *******************************************
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

# WINOLEAPI  CoInstall(
#     _In_ IBindCtx     * pbc,
#     _In_ DWORD          dwFlags,
#     _In_ uCLSSPEC     * pClassSpec,
#     _In_ QUERYCONTEXT * pQuery,
#     _In_ LPWSTR         pszCodeBase);
CoInstall = ole32.CoInstall
CoInstall.restype = WINOLEAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

# Moniker APIs

# _Check_return_ WINOLEAPI  BindMoniker(_In_ LPMONIKER pmk, _In_ DWORD grfOpt, _In_ REFIID iidResult, _Outptr_ LPVOID FAR* ppvResult);
BindMoniker = ole32.BindMoniker
BindMoniker.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  CoGetObject(_In_ LPCWSTR pszName, _In_opt_ BIND_OPTS *pBindOptions, _In_ REFIID riid, _Outptr_ void **ppv);
CoGetObject = ole32.CoGetObject
CoGetObject.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  MkParseDisplayName(_In_ LPBC pbc, _In_ LPCOLESTR szUserName,
#                 _Out_ ULONG FAR * pchEaten, _Outptr_ LPMONIKER FAR * ppmk);
MkParseDisplayName = ole32.MkParseDisplayName
MkParseDisplayName.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  MonikerRelativePathTo(_In_ LPMONIKER pmkSrc, _In_ LPMONIKER pmkDest, _Outptr_ LPMONIKER
#                 FAR* ppmkRelPath, _In_ BOOL dwReserved);
MonikerRelativePathTo = ole32.MonikerRelativePathTo
MonikerRelativePathTo.restype = WINOLEAPI
# _Check_return_ WINOLEAPI  MonikerCommonPrefixWith(_In_ LPMONIKER pmkThis, _In_ LPMONIKER pmkOther,
#                 _Outptr_ LPMONIKER FAR* ppmkCommon);

MonikerCommonPrefixWith = ole32.MonikerCommonPrefixWith
MonikerCommonPrefixWith.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  CreateBindCtx(_In_ DWORD reserved, _Outptr_ LPBC FAR* ppbc);
CreateBindCtx = ole32.CreateBindCtx
CreateBindCtx.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  CreateGenericComposite(_In_opt_ LPMONIKER pmkFirst, _In_opt_ LPMONIKER pmkRest,
#                 _Outptr_ LPMONIKER FAR* ppmkComposite);
CreateGenericComposite = ole32.CreateGenericComposite
CreateGenericComposite.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  GetClassFile (_In_ LPCOLESTR szFilename, _Out_ CLSID FAR* pclsid);
GetClassFile = ole32.GetClassFile
GetClassFile.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  CreateClassMoniker(_In_ REFCLSID rclsid, _Outptr_ LPMONIKER FAR* ppmk);
CreateClassMoniker = ole32.CreateClassMoniker
CreateClassMoniker.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  CreateFileMoniker(_In_ LPCOLESTR lpszPathName, _Outptr_ LPMONIKER FAR* ppmk);
CreateFileMoniker = ole32.CreateFileMoniker
CreateFileMoniker.restype = WINOLEAPI


# _Check_return_ WINOLEAPI  CreateItemMoniker(_In_ LPCOLESTR lpszDelim, _In_ LPCOLESTR lpszItem,
#                           _Outptr_ LPMONIKER FAR* ppmk);
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

# _Check_return_ WINOLEAPI  GetRunningObjectTable( _In_ DWORD reserved, _Outptr_ LPRUNNINGOBJECTTABLE FAR* pprot);
GetRunningObjectTable = ole32.GetRunningObjectTable
GetRunningObjectTable.restype = WINOLEAPI


# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP)
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# from .urlmon_h import * # NOQA
from .propidl_h import * # NOQA

# Standard Progress Indicator implementation

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# RC_INVOKED
# from .poppack_h import * # NOQA
# __OBJBASE_H__

# *******
# WINOLEAPI CreateStdProgressIndicator(_In_ HWND hwndParent,
#                                   _In_ LPCOLESTR pszTitle,
#                                    _In_ IBindStatusCallback * pIbscCaller,
#                                    _Outptr_ IBindStatusCallback ** ppIbsc);
CreateStdProgressIndicator = ole32.CreateStdProgressIndicator
CreateStdProgressIndicator.restype = WINOLEAPI

__all__ = (
    'IsEqualGUID', 'STG_TOEND', 'STG_LAYOUT_INTERLEAVED', 'STGTY_REPEAT',
    'MARSHALINTERFACE_MIN', 'ASYNC_MODE_DEFAULT', 'STG_LAYOUT_SEQUENTIAL',
    'ASYNC_MODE_COMPATIBILITY', 'tagCOINIT', 'COMSD', 'COINIT', 'tagCOMSD',
    'CoGetInstanceFromIStorage',
    'CoAllowSetForegroundWindow', 'CoIsOle1Class', 'CoFileTimeToDosDateTime',
    'CoDosDateTimeToFileTime', 'CoFileTimeNow', 'CoRegisterMessageFilter',
    'CoTreatAsClass', 'CreateDataAdviseHolder',
    'CreateDataCache', 'StgOpenAsyncDocfileOnIFillLockBytes',
    'StgGetIFillLockBytesOnILockBytes', 'StgGetIFillLockBytesOnFile',
    'CoInstall', 'BindMoniker', 'CoGetObject', 'MkParseDisplayName',
    'MonikerRelativePathTo', 'MonikerCommonPrefixWith', 'CreateBindCtx',
    'CreateGenericComposite', 'GetClassFile', 'CreateClassMoniker',
    'CreateFileMoniker', 'CreateItemMoniker', 'CreateAntiMoniker',
    'CreatePointerMoniker', 'CreateObjrefMoniker', 'GetRunningObjectTable',
    'CreateStdProgressIndicator', 'IsEqualGUID',
    'CoInitialize', 'CoRegisterMallocSpy', 'CoRevokeMallocSpy',
    'CoRegisterInitializeSpy',
    'CoRevokeInitializeSpy',
    'CoLoadLibrary', 'CoFreeLibrary', 'CoFreeAllLibraries',
)
