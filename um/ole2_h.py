import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_OLE2_H_ = None
WIN32 = None
ISOLATION_AWARE_ENABLED = None
_OBJBASE_H_ = None
CreateDataAdviseHolder = None


class _OLESTREAMVTBL(ctypes.Structure):
    pass


OLESTREAMVTBL = _OLESTREAMVTBL


class _OLESTREAM(ctypes.Structure):
    pass


OLESTREAM = _OLESTREAM


from pyWinAPI.shared.winapifamily_h import * # NOQA

if _MSC_VER >= 1200:
    pass
# END IF


# + ---------------------------------------------------------------------------
# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.
# File:  OLE2.h
# Contents: Main OLE2 header; Defines Linking and Emmebbeding interfaces, and
# API's.
# Also includes .h files for the compobj, and oleauto subcomponents.
# ----------------------------------------------------------------------------
if not defined(_OLE2_H_):
    _OLE2_H_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    # Set packing to 8
    from pyWinAPI.shared.pshpack8_h import * # NOQA

    # Make 100% sure WIN32 is defined
    if not defined(WIN32):
        WIN32 = 100        # 100 == NT version 1.0
    # END IF

    # SET to remove _export from interface definitions
    from pyWinAPI.shared.winerror_h import * # NOQA
    from pyWinAPI.um.objbase_h import * # NOQA
    from pyWinAPI.um.oleauto_h import * # NOQA
    from pyWinAPI.um.coml2api_h import * # NOQA

    ole32 = ctypes.windll.OLE32

    # View OBJECT Error Codes
    E_DRAW = VIEW_E_DRAW

    # IDataObject Error Codes
    DATA_E_FORMATETC = DV_E_FORMATETC

    # Common stuff gleamed from OLE.2,
    # verbs
    OLEIVERB_PRIMARY = 0
    OLEIVERB_SHOW = -1
    OLEIVERB_OPEN = -2
    OLEIVERB_HIDE = -3
    OLEIVERB_UIACTIVATE = -4
    OLEIVERB_INPLACEACTIVATE = -5
    OLEIVERB_DISCARDUNDOSTATE = -6

    # for OleCreateEmbeddingHelper flags; roles in low word; options in high
    # word
    EMBDHLP_INPROC_HANDLER = 0x0000
    EMBDHLP_INPROC_SERVER = 0x0001
    EMBDHLP_CREATENOW = 0x00000000
    EMBDHLP_DELAYCREATE = 0x00010000

    # extended create function flags
    OLECREATE_LEAVERUNNING = 0x00000001

    # pull in the MIDL generated header
    from pyWinAPI.um.oleidl_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # **** DV APIs
        # *********************************************************
        # /* This function is declared in objbase.h and ole2.h. IsolationAware
        # support is via objbase.h.
        if (
            not defined(ISOLATION_AWARE_ENABLED) or
            not ISOLATION_AWARE_ENABLED or
            not defined(_OBJBASE_H_) or
            not defined(CreateDataAdviseHolder)
        ):
            # WINOLEAPI CreateDataAdviseHolder(_Outptr_ LPDATAADVISEHOLDER FAR* ppDAHolder);
            CreateDataAdviseHolder = ole32.CreateDataAdviseHolder
            CreateDataAdviseHolder.restype = WINOLEAPI

        # END IF

        # **** OLE API Prototypes
        # **********************************************

        # WINOLEAPI_(DWORD) OleBuildVersion( VOID );
        OleBuildVersion = ole32.OleBuildVersion
        OleBuildVersion.restype = DWORD

        # init/term
        # _Check_return_ WINOLEAPI OleInitialize(IN LPVOID pvReserved);
        OleInitialize = ole32.OleInitialize
        OleInitialize.restype = WINOLEAPI

        # /* APIs to query whether (Embedded/Linked) object can be created
        # from the data object
        # WINOLEAPI  OleQueryLinkFromData(IN LPDATAOBJECT pSrcDataObject);
        OleQueryLinkFromData = ole32.OleQueryLinkFromData
        OleQueryLinkFromData.restype = WINOLEAPI

        # WINOLEAPI  OleQueryCreateFromData(IN LPDATAOBJECT pSrcDataObject);
        OleQueryCreateFromData = ole32.OleQueryCreateFromData
        OleQueryCreateFromData.restype = WINOLEAPI

        # Object creation APIs
        # WINOLEAPI  OleCreate(IN REFCLSID rclsid, IN REFIID riid, IN DWORD renderopt,
        # IN LPFORMATETC pFormatEtc, IN LPOLECLIENTSITE pClientSite,
        # IN LPSTORAGE pStg, OUT LPVOID FAR* ppvObj);
        OleCreate = ole32.OleCreate
        OleCreate.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI  OleCreateEx(IN REFCLSID rclsid, IN REFIID riid, IN DWORD dwFlags,
        # IN DWORD renderopt, IN ULONG cFormats, IN DWORD* rgAdvf,
        # IN LPFORMATETC rgFormatEtc, IN IAdviseSink FAR* lpAdviseSink,
        # OUT DWORD FAR* rgdwConnection, IN LPOLECLIENTSITE pClientSite,
        # IN LPSTORAGE pStg, OUT LPVOID FAR* ppvObj);
        OleCreateEx = ole32.OleCreateEx
        OleCreateEx.restype = WINOLEAPI

        # WINOLEAPI  OleCreateFromData(IN LPDATAOBJECT pSrcDataObj, IN REFIID riid,
        # IN DWORD renderopt, IN LPFORMATETC pFormatEtc,
        # IN LPOLECLIENTSITE pClientSite, IN LPSTORAGE pStg,
        # OUT LPVOID FAR* ppvObj);
        OleCreateFromData = ole32.OleCreateFromData
        OleCreateFromData.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI  OleCreateFromDataEx(IN LPDATAOBJECT pSrcDataObj, IN REFIID riid,
        # IN DWORD dwFlags, IN DWORD renderopt, IN ULONG cFormats, IN DWORD* rgAdvf,
        # IN LPFORMATETC rgFormatEtc, IN IAdviseSink FAR* lpAdviseSink,
        # OUT DWORD FAR* rgdwConnection, IN LPOLECLIENTSITE pClientSite,
        # IN LPSTORAGE pStg, OUT LPVOID FAR* ppvObj);
        OleCreateFromDataEx = ole32.OleCreateFromDataEx
        OleCreateFromDataEx.restype = WINOLEAPI

        # WINOLEAPI  OleCreateLinkFromData(IN LPDATAOBJECT pSrcDataObj, IN REFIID riid,
        # IN DWORD renderopt, IN LPFORMATETC pFormatEtc,
        # IN LPOLECLIENTSITE pClientSite, IN LPSTORAGE pStg,
        # OUT LPVOID FAR* ppvObj);
        OleCreateLinkFromData = ole32.OleCreateLinkFromData
        OleCreateLinkFromData.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI  OleCreateLinkFromDataEx(IN LPDATAOBJECT pSrcDataObj, IN REFIID riid,
        # IN DWORD dwFlags, IN DWORD renderopt, IN ULONG cFormats, IN DWORD* rgAdvf,
        # IN LPFORMATETC rgFormatEtc, IN IAdviseSink FAR* lpAdviseSink,
        # OUT IN DWORD FAR* rgdwConnection, IN LPOLECLIENTSITE pClientSite,
        # IN LPSTORAGE pStg, OUT LPVOID FAR* ppvObj);
        OleCreateLinkFromDataEx = ole32.OleCreateLinkFromDataEx
        OleCreateLinkFromDataEx.restype = WINOLEAPI

        # WINOLEAPI  OleCreateStaticFromData(IN LPDATAOBJECT pSrcDataObj, IN REFIID iid,
        # IN DWORD renderopt, IN LPFORMATETC pFormatEtc,
        # IN LPOLECLIENTSITE pClientSite, IN LPSTORAGE pStg,
        # OUT LPVOID FAR* ppvObj);
        OleCreateStaticFromData = ole32.OleCreateStaticFromData
        OleCreateStaticFromData.restype = WINOLEAPI

        # WINOLEAPI  OleCreateLink(IN LPMONIKER pmkLinkSrc, IN REFIID riid,
        # IN DWORD renderopt, IN LPFORMATETC lpFormatEtc,
        # IN LPOLECLIENTSITE pClientSite, IN LPSTORAGE pStg, OUT LPVOID FAR* ppvObj);
        OleCreateLink = ole32.OleCreateLink
        OleCreateLink.restype = WINOLEAPI

        # WINOLEAPI  OleCreateLinkEx(IN LPMONIKER pmkLinkSrc, IN REFIID riid,
        # IN DWORD dwFlags, IN DWORD renderopt, IN ULONG cFormats, IN DWORD* rgAdvf,
        # IN LPFORMATETC rgFormatEtc, IN IAdviseSink FAR* lpAdviseSink,
        # OUT DWORD FAR* rgdwConnection, IN LPOLECLIENTSITE pClientSite,
        # IN LPSTORAGE pStg, OUT LPVOID FAR* ppvObj);
        OleCreateLinkEx = ole32.OleCreateLinkEx
        OleCreateLinkEx.restype = WINOLEAPI

        # WINOLEAPI  OleCreateLinkToFile(IN LPCOLESTR lpszFileName, IN REFIID riid,
        # IN DWORD renderopt, IN LPFORMATETC lpFormatEtc,
        # IN LPOLECLIENTSITE pClientSite, IN LPSTORAGE pStg, OUT LPVOID FAR* ppvObj);
        OleCreateLinkToFile = ole32.OleCreateLinkToFile
        OleCreateLinkToFile.restype = WINOLEAPI

        # WINOLEAPI  OleCreateLinkToFileEx(IN LPCOLESTR lpszFileName, IN REFIID riid,
        # IN DWORD dwFlags, IN DWORD renderopt, IN ULONG cFormats, IN DWORD* rgAdvf,
        # IN LPFORMATETC rgFormatEtc, IN IAdviseSink FAR* lpAdviseSink,
        # OUT DWORD FAR* rgdwConnection, IN LPOLECLIENTSITE pClientSite,
        # IN LPSTORAGE pStg, OUT LPVOID FAR* ppvObj);
        OleCreateLinkToFileEx = ole32.OleCreateLinkToFileEx
        OleCreateLinkToFileEx.restype = WINOLEAPI

        # WINOLEAPI  OleCreateFromFile(IN REFCLSID rclsid, IN LPCOLESTR lpszFileName, IN REFIID riid,
        # IN DWORD renderopt, IN LPFORMATETC lpFormatEtc,
        # IN LPOLECLIENTSITE pClientSite, IN LPSTORAGE pStg, OUT LPVOID FAR* ppvObj);
        OleCreateFromFile = ole32.OleCreateFromFile
        OleCreateFromFile.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI  OleCreateFromFileEx(IN REFCLSID rclsid, IN LPCOLESTR lpszFileName, IN REFIID riid,
        # IN DWORD dwFlags, IN DWORD renderopt, IN ULONG cFormats, IN DWORD* rgAdvf,
        # IN LPFORMATETC rgFormatEtc, IN IAdviseSink FAR* lpAdviseSink,
        # OUT DWORD FAR* rgdwConnection, IN LPOLECLIENTSITE pClientSite,
        # IN LPSTORAGE pStg, OUT LPVOID FAR* ppvObj);
        OleCreateFromFileEx = ole32.OleCreateFromFileEx
        OleCreateFromFileEx.restype = WINOLEAPI

        # WINOLEAPI  OleLoad(IN LPSTORAGE pStg, IN REFIID riid, IN LPOLECLIENTSITE pClientSite,
        # OUT LPVOID FAR* ppvObj);
        OleLoad = ole32.OleLoad
        OleLoad.restype = WINOLEAPI

        # WINOLEAPI  OleSave(_In_ LPPERSISTSTORAGE pPS, _In_ LPSTORAGE pStg, _In_ BOOL fSameAsLoad);
        OleSave = ole32.OleSave
        OleSave.restype = WINOLEAPI

        # WINOLEAPI  OleLoadFromStream( IN LPSTREAM pStm, IN REFIID iidInterface, OUT LPVOID FAR* ppvObj);
        OleLoadFromStream = ole32.OleLoadFromStream
        OleLoadFromStream.restype = WINOLEAPI

        # WINOLEAPI  OleSaveToStream( IN LPPERSISTSTREAM pPStm, IN LPSTREAM pStm );
        OleSaveToStream = ole32.OleSaveToStream
        OleSaveToStream.restype = WINOLEAPI

        # WINOLEAPI  OleSetContainedObject(IN LPUNKNOWN pUnknown, IN BOOL fContained);
        OleSetContainedObject = ole32.OleSetContainedObject
        OleSetContainedObject.restype = WINOLEAPI

        # WINOLEAPI  OleNoteObjectVisible(IN LPUNKNOWN pUnknown, IN BOOL fVisible);
        OleNoteObjectVisible = ole32.OleNoteObjectVisible
        OleNoteObjectVisible.restype = WINOLEAPI

        # Drag/Drop APIs
        # WINOLEAPI  RegisterDragDrop(IN HWND hwnd, IN LPDROPTARGET pDropTarget);
        RegisterDragDrop = ole32.RegisterDragDrop
        RegisterDragDrop.restype = WINOLEAPI

        # WINOLEAPI  RevokeDragDrop(IN HWND hwnd);
        RevokeDragDrop = ole32.RevokeDragDrop
        RevokeDragDrop.restype = WINOLEAPI

        # WINOLEAPI  DoDragDrop(IN LPDATAOBJECT pDataObj, IN LPDROPSOURCE pDropSource,
        # IN DWORD dwOKEffects, OUT LPDWORD pdwEffect);
        DoDragDrop = ole32.DoDragDrop
        DoDragDrop.restype = WINOLEAPI

        # Clipboard APIs
        # WINOLEAPI  OleSetClipboard(IN LPDATAOBJECT pDataObj);
        OleSetClipboard = ole32.OleSetClipboard
        OleSetClipboard.restype = WINOLEAPI

        # WINOLEAPI  OleGetClipboard(_Outptr_ LPDATAOBJECT FAR* ppDataObj);
        OleGetClipboard = ole32.OleGetClipboard
        OleGetClipboard.restype = WINOLEAPI

        if NTDDI_VERSION >= NTDDI_WIN10_RS1:
            # WINOLEAPI  OleGetClipboardWithEnterpriseInfo(_Outptr_result_nullonfailure_ IDataObject** dataObject,
            # _Outptr_result_nullonfailure_ PWSTR* dataEnterpriseId,
            # _Outptr_result_nullonfailure_ PWSTR* sourceDescription,
            # _Outptr_result_nullonfailure_ PWSTR* targetDescription,
            # _Outptr_result_nullonfailure_ PWSTR* dataDescription);
            OleGetClipboardWithEnterpriseInfo = (
                ole32.OleGetClipboardWithEnterpriseInfo
            )
            OleGetClipboardWithEnterpriseInfo.restype = WINOLEAPI

        # END IF

        # WINOLEAPI  OleIsCurrentClipboard(IN LPDATAOBJECT pDataObj);
        OleIsCurrentClipboard = ole32.OleIsCurrentClipboard
        OleIsCurrentClipboard.restype = WINOLEAPI

        # InPlace Editing APIs
        # Helper APIs
        # _Check_return_ WINOLEAPI          OleRun(IN LPUNKNOWN pUnknown);
        OleRun = ole32.OleRun
        OleRun.restype = WINOLEAPI

        # WINOLEAPI_(BOOL)   OleIsRunning(IN LPOLEOBJECT pObject);
        OleIsRunning = ole32.OleIsRunning
        OleIsRunning.restype = BOOL

        # WINOLEAPI          OleLockRunning(IN LPUNKNOWN pUnknown, IN BOOL fLock, IN BOOL fLastUnlockCloses);
        OleLockRunning = ole32.OleLockRunning
        OleLockRunning.restype = WINOLEAPI

        # WINOLEAPI_(VOID)   ReleaseStgMedium(IN LPSTGMEDIUM);
        ReleaseStgMedium = ole32.ReleaseStgMedium
        ReleaseStgMedium.restype = VOID

        # WINOLEAPI          CreateOleAdviseHolder(_Out_ LPOLEADVISEHOLDER FAR* ppOAHolder);
        CreateOleAdviseHolder = ole32.CreateOleAdviseHolder
        CreateOleAdviseHolder.restype = WINOLEAPI

        # WINOLEAPI          OleCreateDefaultHandler(IN REFCLSID clsid, IN LPUNKNOWN pUnkOuter,
        # IN REFIID riid, OUT LPVOID FAR* lplpObj);
        OleCreateDefaultHandler = ole32.OleCreateDefaultHandler
        OleCreateDefaultHandler.restype = WINOLEAPI

        # WINOLEAPI          OleCreateEmbeddingHelper(IN REFCLSID clsid, IN LPUNKNOWN pUnkOuter,
        # IN DWORD flags, IN LPCLASSFACTORY pCF,
        # IN REFIID riid, OUT LPVOID FAR* lplpObj);
        OleCreateEmbeddingHelper = ole32.OleCreateEmbeddingHelper
        OleCreateEmbeddingHelper.restype = WINOLEAPI

        # WINOLEAPI_(BOOL)   IsAccelerator(IN HACCEL hAccel, IN INT cAccelEntries, IN LPMSG lpMsg,
        # OUT WORD FAR* lpwCmd);
        IsAccelerator = ole32.IsAccelerator
        IsAccelerator.restype = BOOL

        # Icon extraction Helper APIs
        # WINOLEAPI_(HGLOBAL) OleGetIconOfFile(_In_ LPOLESTR lpszPath, IN BOOL fUseFileAsLabel);
        OleGetIconOfFile = ole32.OleGetIconOfFile
        OleGetIconOfFile.restype = HGLOBAL

        # WINOLEAPI_(HGLOBAL) OleGetIconOfClass(IN REFCLSID rclsid, _In_opt_ LPOLESTR lpszLabel,
        # IN BOOL fUseTypeAsLabel);
        OleGetIconOfClass = ole32.OleGetIconOfClass
        OleGetIconOfClass.restype = HGLOBAL

        # WINOLEAPI_(HGLOBAL) OleMetafilePictFromIconAndLabel(IN HICON hIcon, _In_ LPOLESTR lpszLabel,
        # _In_ LPOLESTR lpszSourceFile, IN UINT iIconIndex);
        OleMetafilePictFromIconAndLabel = ole32.OleMetafilePictFromIconAndLabel
        OleMetafilePictFromIconAndLabel.restype = HGLOBAL

        # Registration Database Helper APIs
        # WINOLEAPI OleRegEnumFormatEtc(IN REFCLSID clsid, IN DWORD dwDirection,
        # _Outptr_ LPENUMFORMATETC FAR* ppenum);
        OleRegEnumFormatEtc = ole32.OleRegEnumFormatEtc
        OleRegEnumFormatEtc.restype = WINOLEAPI

        # OLE 1.0 conversion APIS
        # *** OLE 1.0 OLESTREAM declarations
        # ***********************************
        LPOLESTREAM = POINTER(_OLESTREAM)
        Get = CALLBACK(DWORD, LPOLESTREAM, PVOID, DWORD)
        Put = CALLBACK(DWORD, LPOLESTREAM, PVOID, DWORD)

        _OLESTREAMVTBL._fields_ = [
            ('Get', Get),
            ('Put', Put)
        ]
        LPOLESTREAMVTBL = POINTER(OLESTREAMVTBL)

        _OLESTREAM._fields_ = [
            ('lpstbl', LPOLESTREAMVTBL),
        ]

        # ConvertTo APIS
        # WINOLEAPI OleDoAutoConvert(IN LPSTORAGE pStg, OUT LPCLSID pClsidNew);
        OleDoAutoConvert = ole32.OleDoAutoConvert
        OleDoAutoConvert.restype = WINOLEAPI

        # WINOLEAPI OleGetAutoConvert(IN REFCLSID clsidOld, OUT LPCLSID pClsidNew);
        OleGetAutoConvert = ole32.OleGetAutoConvert
        OleGetAutoConvert.restype = WINOLEAPI

        # WINOLEAPI OleSetAutoConvert(IN REFCLSID clsidOld, IN REFCLSID clsidNew);
        OleSetAutoConvert = ole32.OleSetAutoConvert
        OleSetAutoConvert.restype = WINOLEAPI

        # WINOLEAPI SetConvertStg(IN LPSTORAGE pStg, IN BOOL fConvert);
        SetConvertStg = ole32.SetConvertStg
        SetConvertStg.restype = WINOLEAPI

        # WINOLEAPI
        # OleConvertIStorageToOLESTREAMEx
        # (IN LPSTORAGE          pstg,
        # // Presentation data to OLESTREAM
        # IN CLIPFORMAT         cfFormat, // format
        # IN LONG               lWidth, // width
        # IN LONG               lHeight, // height
        # IN DWORD              dwSize, // size in bytes
        # IN LPSTGMEDIUM        pmedium, // bits
        # OUT LPOLESTREAM        polestm);

        OleConvertIStorageToOLESTREAMEx = ole32.OleConvertIStorageToOLESTREAMEx
        OleConvertIStorageToOLESTREAMEx.restype = WINOLEAPI

        # WINOLEAPI
        # OleConvertOLESTREAMToIStorageEx
        # (IN LPOLESTREAM        polestm,
        # OUT LPSTORAGE          pstg,
        # // Presentation data from OLESTREAM
        # OUT CLIPFORMAT FAR * pcfFormat, // format
        # OUT LONG FAR * plwWidth, // width
        # OUT LONG FAR * plHeight, // height
        # OUT DWORD FAR * pdwSize, // size in bytes
        # OUT LPSTGMEDIUM        pmedium); // bits

        OleConvertOLESTREAMToIStorageEx = ole32.OleConvertOLESTREAMToIStorageEx
        OleConvertOLESTREAMToIStorageEx.restype = WINOLEAPI

    if not defined(RC_INVOKED):
        from pyWinAPI.shared.poppack_h import * # NOQA
    # END IF   RC_INVOKED
# END IF   __OLE2_H__

if _MSC_VER >= 1200:
    pass
# END IF


