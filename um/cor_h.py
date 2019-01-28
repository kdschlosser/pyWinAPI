import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


def INTERFACE(name):
    return type(name, (comtypes.IUnknown,), {})


def STDMETHOD(name):

    def method_wrapper(restype, *args):
        if isinstance(restype, tuple):
            args = (restype,) + args
            restype = HRESULT

        argtypes = tuple(arg[0] for arg in args)
        argnames = list(arg[1] for arg in args)
        res = comtypes.STDMETHOD(restype, name, argtypes)
        return argnames, res

    return method_wrapper


def DECLARE_INTERFACE_(cls, super_cls):
    if super_cls != comtypes.IUnknown:
        bases = super_cls.__bases__
        cls.__bases__ = (
            (super_cls,) +
            tuple(base for base in cls.__bases__ if base not in bases)
        )

    def wrapper(*args):
        argnames = list(arg[0] for arg in args)
        _methods_ = list(arg[1] for arg in args)

        method_names = list(itm[1] for itm in _methods_)

        for i, method_name in enumerate(method_names):
            defaults = argnames[i]

            class MethodWrapper(object):

                def __init__(self, parent, name, keywords):
                    self.__parent = parent
                    self.__name__ = name
                    self.__keywords = keywords

                def __call__(self, *args, **kwargs):
                    args = list(args)
                    for j, keyword in enumerate(self.__keywords):
                        if keyword in kwargs:
                            args.insert(j, kwargs.pop(keyword))

                    getattr(self.__parent, '__com_' + self.__name__)(*args)


            method = MethodWrapper(cls, method_name, defaults)
            setattr(cls, method_name, method)

        cls._methods_ = _methods_

    return wrapper


_COR_H_ = None
FEATURE_PAL = None
_WINDOWS_UPDATES_ = None
_DEFINE_META_DATA_META_CONSTANTS = None
_META_DATA_META_CONSTANTS_DEFINED = None
FORCEINLINE = None


class OSINFO(ctypes.Structure):
    pass


class ASSEMBLYMETADATA(ctypes.Structure):
    pass


class CVStruct(ctypes.Structure):
    pass


class CeeSectionRelocExtra(ctypes.Union):
    pass


class COR_NATIVE_LINK(ctypes.Structure):
    pass


# == + + ==
# Copyright (c) Microsoft Corporation. All rights reserved.
# == -- ==
# ***************************************************************************
# *   ** * Cor.h - general header for the Runtime. ** *   **
# **************************************************************************
if not defined(_COR_H_):
    _COR_H_ = VOID

    # **********************************************************************
    # Required includes
    # Definitions of OLE types.
    from pyWinAPI.um.ole2_h import * # NOQA
    from pyWinAPI.shared.specstrings_h import * # NOQA
    from pyWinAPI.um.corerror_h import * # NOQA

    # **********************************************************************
    if defined(__cplusplus):
        pass
    # END IF

    # {BED7F4EA-1A96-11d2-8F08-00A0C9A6186D}
    LIBID_ComPlusRuntime = EXTERN_GUID(
        0xBED7F4EA,
        0x1A96,
        0x11D2,
        0x8F,
        0x8,
        0x0,
        0xA0,
        0xC9,
        0xA6,
        0x18,
        0x6D
    )

    # {90883F05-3D28-11D2-8F17-00A0C9A6186D}
    GUID_ExportedFromComPlus = EXTERN_GUID(
        0x90883F05,
        0x3D28,
        0x11D2,
        0x8F,
        0x17,
        0x0,
        0xA0,
        0xC9,
        0xA6,
        0x18,
        0x6D
    )

    # {0F21F359-AB84-41e8-9A78-36D110E6D2F9}
    GUID_ManagedName = EXTERN_GUID(
        0xF21F359,
        0xAB84,
        0x41E8,
        0x9A,
        0x78,
        0x36,
        0xD1,
        0x10,
        0xE6,
        0xD2,
        0xF9
    )

    # {54FC8F55-38DE-4703-9C4E-250351302B1C}
    GUID_Function2Getter = EXTERN_GUID(
        0x54FC8F55,
        0x38DE,
        0x4703,
        0x9C,
        0x4E,
        0x25,
        0x3,
        0x51,
        0x30,
        0x2B,
        0x1C
    )

    # CLSID_CorMetaDataDispenserRuntime: {1EC2DE53-75CC-11d2-9775-00A0C9B4D50C}
    # Dispenser coclass for version 1.5 and 2.0 meta data. To get the "latest"
    # bind
    # to CLSID_MetaDataDispenser.
    CLSID_CorMetaDataDispenserRuntime = EXTERN_GUID(
        0x1EC2DE53,
        0x75CC,
        0x11D2,
        0x97,
        0x75,
        0x0,
        0xA0,
        0xC9,
        0xB4,
        0xD5,
        0xC
    )

    # {CD2BC5C9-F452-4326-B714-F9C539D4DA58}
    GUID_DispIdOverride = EXTERN_GUID(
        0xCD2BC5C9,
        0xF452,
        0x4326,
        0xB7,
        0x14,
        0xF9,
        0xC5,
        0x39,
        0xD4,
        0xDA,
        0x58
    )

    # {B64784EB-D8D4-4d9b-9ACD-0E30806426F7}
    GUID_ForceIEnumerable = EXTERN_GUID(
        0xB64784EB,
        0xD8D4,
        0x4D9B,
        0x9A,
        0xCD,
        0x0E,
        0x30,
        0x80,
        0x64,
        0x26,
        0xF7
    )

    # {2941FF83-88D8-4F73-B6A9-BDF8712D000D}
    GUID_PropGetCA = EXTERN_GUID(
        0x2941FF83,
        0x88D8,
        0x4F73,
        0xB6,
        0xA9,
        0xBD,
        0xF8,
        0x71,
        0x2D,
        0x00,
        0x0D
    )

    # {29533527-3683-4364-ABC0-DB1ADD822FA2}
    GUID_PropPutCA = EXTERN_GUID(
        0x29533527,
        0x3683,
        0x4364,
        0xAB,
        0xC0,
        0xDB,
        0x1A,
        0xDD,
        0x82,
        0x2F,
        0xA2
    )

    # CLSID_CLR_v1_MetaData: {005023CA-72B1-11D3-9FC4-00C04F79A0A3}
    # Used to generate v1 metadata (for v1.0 and v1.1 CLR compatibility).
    CLSID_CLR_v1_MetaData = EXTERN_GUID(
        0x005023CA,
        0x72B1,
        0x11D3,
        0x9F,
        0xC4,
        0x0,
        0xC0,
        0x4F,
        0x79,
        0xA0,
        0xA3
    )

    # CLSID_CLR_v2_MetaData: {EFEA471A-44FD-4862-9292-0C58D46E1F3A}
    # Used to generate v1 metadata (for v1.0 and v1.1 CLR compatibility).
    CLSID_CLR_v2_MetaData = EXTERN_GUID(
        0xEFEA471A,
        0x44FD,
        0x4862,
        0x92,
        0x92,
        0xC,
        0x58,
        0xD4,
        0x6E,
        0x1F,
        0x3A
    )

    # CLSID_CorMetaDataRuntime:
    # This will can always be used to generate the "latest" metadata available.
    CLSID_CorMetaDataRuntime = CLSID_CLR_v2_MetaData

    # {30FE7BE8-D7D9-11D2-9F80-00C04F79A0A3}
    MetaDataCheckDuplicatesFor = EXTERN_GUID(
        0x30FE7BE8,
        0xD7D9,
        0x11D2,
        0x9F,
        0x80,
        0x0,
        0xC0,
        0x4F,
        0x79,
        0xA0,
        0xA3
    )

    # {DE3856F8-D7D9-11D2-9F80-00C04F79A0A3}
    MetaDataRefToDefCheck = EXTERN_GUID(
        0xDE3856F8,
        0xD7D9,
        0x11D2,
        0x9F,
        0x80,
        0x0,
        0xC0,
        0x4F,
        0x79,
        0xA0,
        0xA3
    )

    # {E5D71A4C-D7DA-11D2-9F80-00C04F79A0A3}
    MetaDataNotificationForTokenMovement = EXTERN_GUID(
        0xE5D71A4C,
        0xD7DA,
        0x11D2,
        0x9F,
        0x80,
        0x0,
        0xC0,
        0x4F,
        0x79,
        0xA0,
        0xA3
    )

    # {2eee315c-d7db-11d2-9f80-00c04f79a0a3}
    MetaDataSetUpdate = EXTERN_GUID(
        0x2EEE315C,
        0xD7DB,
        0x11D2,
        0x9F,
        0x80,
        0x0,
        0xC0,
        0x4F,
        0x79,
        0xA0,
        0xA3
    )
    MetaDataSetENC = MetaDataSetUpdate

    # Use this guid in SetOption to indicate if the import enumerator should
    # skip over
    # delete items or not. The default is yes.
    # {79700F36-4AAC-11d3-84C3-009027868CB1}
    MetaDataImportOption = EXTERN_GUID(
        0x79700F36,
        0x4AAC,
        0x11D3,
        0x84,
        0xC3,
        0x0,
        0x90,
        0x27,
        0x86,
        0x8C,
        0xB1
    )

    # Use this guid in the SetOption if compiler wants to have MetaData API to
    # take reader/writer lock
    # {F7559806-F266-42ea-8C63-0ADB45E8B234}
    MetaDataThreadSafetyOptions = EXTERN_GUID(
        0xF7559806,
        0xF266,
        0x42EA,
        0x8C,
        0x63,
        0xA,
        0xDB,
        0x45,
        0xE8,
        0xB2,
        0x34
    )

    # Use this guid in the SetOption if compiler wants error when some tokens
    # are emitted out of order
    # {1547872D-DC03-11d2-9420-0000F8083460}
    MetaDataErrorIfEmitOutOfOrder = EXTERN_GUID(
        0x1547872D,
        0xDC03,
        0x11D2,
        0x94,
        0x20,
        0x0,
        0x0,
        0xF8,
        0x8,
        0x34,
        0x60
    )

    # Use this guid in the SetOption to indicate if the tlbimporter should
    # generate the
    # TCE adapters for COM connection point containers.
    # {DCC9DE90-4151-11d3-88D6-00902754C43A}
    MetaDataGenerateTCEAdapters = EXTERN_GUID(
        0xDCC9DE90,
        0x4151,
        0x11D3,
        0x88,
        0xD6,
        0x0,
        0x90,
        0x27,
        0x54,
        0xC4,
        0x3A
    )

    # Use this guid in the SetOption to specifiy a non-default namespace for
    # typelib import.
    # {F17FF889-5A63-11d3-9FF2-00C04FF7431A}
    MetaDataTypeLibImportNamespace = EXTERN_GUID(
        0xF17FF889,
        0x5A63,
        0x11D3,
        0x9F,
        0xF2,
        0x0,
        0xC0,
        0x4F,
        0xF7,
        0x43,
        0x1A
    )

    # Use this guid in the SetOption to specify the behavior of UnmarkAll. See
    # CorLinkerOptions.
    # {47E099B6-AE7C-4797-8317-B48AA645B8F9}
    MetaDataLinkerOptions = EXTERN_GUID(
        0x47E099B6,
        0xAE7C,
        0x4797,
        0x83,
        0x17,
        0xB4,
        0x8A,
        0xA6,
        0x45,
        0xB8,
        0xF9
    )

    # Use this guid in the SetOption to specify the runtime version stored in
    # the CLR metadata.
    # {47E099B7-AE7C-4797-8317-B48AA645B8F9}
    MetaDataRuntimeVersion = EXTERN_GUID(
        0x47E099B7,
        0xAE7C,
        0x4797,
        0x83,
        0x17,
        0xB4,
        0x8A,
        0xA6,
        0x45,
        0xB8,
        0xF9
    )

    # Use this guid in the SetOption to specify the behavior of the merger.
    # {132D3A6E-B35D-464e-951A-42EFB9FB6601}
    MetaDataMergerOptions = EXTERN_GUID(
        0x132D3A6E,
        0xB35D,
        0x464E,
        0x95,
        0x1A,
        0x42,
        0xEF,
        0xB9,
        0xFB,
        0x66,
        0x1
    )
    UVCP_CONSTANT = POINTER(VOID)

    # Constant for connection id and task id
    INVALID_CONNECTION_ID = 0x0
    INVALID_TASK_ID = 0x0
    MAX_CONNECTION_NAME = MAX_PATH

    # **********************************************************************
    # **********************************************************************
    # D L L P U B L I C E N T R Y P O I N T D E C L A R A T I O N S
    # **********************************************************************
    # **********************************************************************

    mscoree = ctypes.windll.MsCorEE

    #     BOOL STDMETHODCALLTYPE _CorDllMain(
    # HINSTANCE hInst,
    # DWORD dwReason,
    # LPVOID lpReserved
    # );
    _CorDllMain = mscoree._CorDllMain
    _CorDllMain.restype = BOOL

    #     __int32 STDMETHODCALLTYPE _CorExeMain();
    _CorExeMain = mscoree._CorExeMain
    _CorExeMain.restype = INT32

    #     __int32 STDMETHODCALLTYPE _CorExeMain2( // Executable exit code.
    #         PBYTE   pUnmappedPE,                // -> memory mapped code
    #         DWORD   cUnmappedPE,                // Size of memory mapped code
    #         _In_ LPWSTR  pImageNameIn,          // -> Executable Name
    #         _In_ LPWSTR  pLoadersFileName,      // -> Loaders Name
    #         _In_ LPWSTR  pCmdLine);             // -> Command Line
    _CorExeMain2 = mscoree._CorExeMain2
    _CorExeMain2.restype = INT32

    #     STDAPI _CorValidateImage(PVOID *ImageBase, LPCWSTR FileName);
    _CorValidateImage = mscoree._CorValidateImage

    #     STDAPI_(VOID) _CorImageUnloading(PVOID ImageBase);
    _CorImageUnloading = mscoree._CorImageUnloading
    _CorImageUnloading.restype = VOID

    #     STDAPI          CoInitializeEE(DWORD fFlags);
    CoInitializeEE = mscoree.CoInitializeEE

    #     STDAPI_(void)   CoUninitializeEE(BOOL fFlags);
    CoUninitializeEE = mscoree.CoUninitializeEE
    CoUninitializeEE.restype = VOID

    #     STDAPI_(void)   CoEEShutDownCOM(void);
    CoEEShutDownCOM = mscoree.CoEEShutDownCOM
    CoEEShutDownCOM.restype = VOID

    if not defined(FEATURE_PAL):
        MSCOREE_SHIM_W = "mscoree.dll"
        MSCOREE_SHIM_A = "mscoree.dll"
    else:
        MSCOREE_SHIM_W = MAKEDLLNAME_W("sscoree")
        MSCOREE_SHIM_A = MAKEDLLNAME_A("sscoree")
    # END IF   not FEATURE_PAL

    SWITCHOUT_HANDLE_VALUE = -2

    # CoInitializeCor flags.
    class tagCOINITCOR(ENUM):
        COINITCOR_DEFAULT = 0x0

    COINITICOR = tagCOINITCOR

    # CoInitializeEE flags.
    class tagCOINITEE(ENUM):
        COINITEE_DEFAULT = 0x0
        COINITEE_DLL = 0x1
        COINITEE_MAIN = 0x2

    COINITIEE = tagCOINITEE

    # CoInitializeEE flags.
    class tagCOUNINITEE(ENUM):
        COUNINITEE_DEFAULT = 0x0
        COUNINITEE_DLL = 0x1

    COUNINITIEE = tagCOUNINITEE

    # **********************************************************************
    # **********************************************************************
    # I L & F I L E F O R M A T D E C L A R A T I O N S
    # **********************************************************************
    # **********************************************************************
    # <STRIP>The following definitions will get moved into <windows.h> by RTM
    # but are
    # kept here for the Alpha's and Beta's.</STRIP>
    if not defined(_WINDOWS_UPDATES_):
        from pyWinAPI.um.corhdr_h import * # NOQA
    # END IF   <windows.h> updates

    # **********************************************************************
    # **********************************************************************
    # D L L P U B L I C E N T R Y P O I N T D E C L A R A T I O N S
    # **********************************************************************
    # **********************************************************************

    # STDAPI          CoInitializeCor(DWORD fFlags);
    CoInitializeCor = mscoree.CoInitializeCor

    # STDAPI_(void)   CoUninitializeCor(void);
    CoUninitializeCor = mscoree.CoUninitializeCor
    CoUninitializeCor.restype = VOID

    # typedef VOID (* TDestructorCallback)(EXCEPTION_RECORD*);
    TDestructorCallback = CALLBACK(
        VOID,
        POINTER(EXCEPTION_RECORD)
    )

    # STDAPI_(void) AddDestructorCallback(
    # int code,
    # TDestructorCallback callback
    # );
    AddDestructorCallback = mscoree.AddDestructorCallback
    AddDestructorCallback.restype = VOID

    # **********************************************************************
    # **********************************************************************
    # CLSID_Cor: {bee00000-ee77-11d0-a015-00c04fbbb884}
    CLSID_Cor = EXTERN_GUID(
        0xBEE00010,
        0xEE77,
        0x11D0,
        0xA0,
        0x15,
        0x00,
        0xC0,
        0x4F,
        0xBB,
        0xB8,
        0x84
    )

    # CLSID_CorMetaDataDispenser: {E5CB7A31-7512-11d2-89CE-0080C792E5D8}
    # This is the "Master Dispenser", always guaranteed to be the most recent
    # dispenser on the machine.
    CLSID_CorMetaDataDispenser = EXTERN_GUID(
        0xE5CB7A31,
        0x7512,
        0x11D2,
        0x89,
        0xCE,
        0x0,
        0x80,
        0xC7,
        0x92,
        0xE5,
        0xD8
    )

    # CLSID_CorMetaDataDispenserReg: {435755FF-7397-11d2-9771-00A0C9B4D50C}
    # Dispenser coclass for version 1.0 meta data. To get the "latest" bind
    # to CLSID_CorMetaDataDispenser.
    CLSID_CorMetaDataDispenserReg = EXTERN_GUID(
        0x435755FF,
        0x7397,
        0x11D2,
        0x97,
        0x71,
        0x0,
        0xA0,
        0xC9,
        0xB4,
        0xD5,
        0xC
    )

    # CLSID_CorMetaDataReg: {87F3A1F5-7397-11d2-9771-00A0C9B4D50C}
    # For COM+ Meta Data, Data Driven Registration
    CLSID_CorMetaDataReg = EXTERN_GUID(
        0x87F3A1F5,
        0x7397,
        0x11D2,
        0x97,
        0x71,
        0x0,
        0xA0,
        0xC9,
        0xB4,
        0xD5,
        0xC
    )

    # IID_IMetaDataInternal {39EE28B3-0181-4d48-B53C-2FFAFFD5FEC1}
    IID_IMetaDataInternal = EXTERN_GUID(
        0x39EE28B3,
        0x181,
        0x4D48,
        0xB5,
        0x3C,
        0x2F,
        0xFA,
        0xFF,
        0xD5,
        0xFE,
        0xC1
    )

    # -------------------------------------
    # --- IMetaDataError
    # -------------------------------------
    # {B81FF171-20F3-11d2-8DCC-00A0C9B09C19}
    IID_IMetaDataError = EXTERN_GUID(
        0xB81FF171,
        0x20F3,
        0x11D2,
        0x8D,
        0xCC,
        0x0,
        0xA0,
        0xC9,
        0xB0,
        0x9C,
        0x19
    )

    # ---
    IMetaDataError = INTERFACE('IMetaDataError')
    IMetaDataError._iid_ = IID_IMetaDataError
    DECLARE_INTERFACE_(IMetaDataError, comtypes.IUnknown)(
        STDMETHOD('OnError')(
            (HRESULT, 'hrError'),
            (mdToken, 'token')
        )
    )

    # -------------------------------------
    # --- IMapToken
    # -------------------------------------
    # IID_IMapToken: {06A3EA8B-0225-11d1-BF72-00C04FC31E12}
    IID_IMapToken = EXTERN_GUID(
        0x6A3EA8B,
        0x225,
        0x11D1,
        0xBF,
        0x72,
        0x0,
        0xC0,
        0x4F,
        0xC3,
        0x1E,
        0x12
    )

    # ---
    IMapToken = INTERFACE('IMapToken')
    IMapToken._iid_ = IID_IMapToken
    DECLARE_INTERFACE_(IMapToken, comtypes.IUnknown)(
        STDMETHOD('Map')(
            (mdToken, 'tkImp'),
            (mdToken, 'tkEmit')
        )
    )

    # -------------------------------------
    # --- IMetaDataDispenser
    # -------------------------------------
    # {B81FF171-20F3-11d2-8DCC-00A0C9B09C19}
    IID_IMetaDataDispenser = EXTERN_GUID(
        0x809C652E,
        0x7396,
        0x11D2,
        0x97,
        0x71,
        0x0,
        0xA0,
        0xC9,
        0xB4,
        0xD5,
        0xC
    )

    # ---
    IMetaDataDispenser = INTERFACE('IMetaDataDispenser')
    IMetaDataDispenser._iid_ = IID_IMetaDataDispenser
    DECLARE_INTERFACE_(IMetaDataDispenser, comtypes.IUnknown)(
        STDMETHOD('DefineScope')(
            # [in] What version to create.
            (REFCLSID, 'rclsid'),
            # [in] Flags on the create.
            (DWORD, 'dwCreateFlags'),
            # [in] The interface desired.
            (REFIID, 'riid'),
            # [out] Return interface on success.
            (POINTER(POINTER(comtypes.IUnknown)), 'ppIUnk')
        ),
        STDMETHOD('OpenScope')(
            # [in] The scope to open.
            (LPCWSTR, 'szScope'),
            # [in] Open mode flags.
            (DWORD, 'dwOpenFlags'),
            # [in] The interface desired.
            (REFIID, 'riid'),
            # [out] Return interface on success.
            (POINTER(POINTER(comtypes.IUnknown)), 'ppIUnk')
        ),
        STDMETHOD('OpenScopeOnMemory')(
            # [in] Location of scope data.
            (LPCVOID, 'pData'),
            # [in] Size of the data pointed to by pData.
            (ULONG, 'cbData'),
            # [in] Open mode flags.
            (DWORD, 'dwOpenFlags'),
            # [in] The interface desired.
            (REFIID, 'riid'),
            # [out] Return interface on success.
            (POINTER(POINTER(comtypes.IUnknown)), 'ppIUnk')
        )
    )

    # -------------------------------------
    # --- IMetaDataEmit
    # -------------------------------------
    # {BA3FEE4C-ECB9-4e41-83B7-183FA41CD859}
    IID_IMetaDataEmit = EXTERN_GUID(
        0xBA3FEE4C,
        0xECB9,
        0x4E41,
        0x83,
        0xB7,
        0x18,
        0x3F,
        0xA4,
        0x1C,
        0xD8,
        0x59
    )

    IMetaDataAssemblyImport = INTERFACE('IMetaDataAssemblyImport')
    IMetaDataImport = INTERFACE('IMetaDataImport')
    IMetaDataAssemblyEmit = INTERFACE('IMetaDataAssemblyEmit')

    # ---
    IMetaDataEmit = INTERFACE('IMetaDataEmit')
    IMetaDataEmit._iid_ = IID_IMetaDataEmit
    DECLARE_INTERFACE_(IMetaDataEmit, comtypes.IUnknown)(
        STDMETHOD('SetModuleProps')(
            # [IN] If not NULL, the name of the module to set.
            (LPCWSTR, 'szName')
        ),
        STDMETHOD('Save')(
            # [IN] The filename to save to.
            (LPCWSTR, 'szFile'),
            # [IN] Flags for the save.
            (DWORD, 'dwSaveFlags')
        ),
        STDMETHOD('SaveToStream')(
            # [IN] A writable stream to save to.
            (POINTER(IStream), 'pIStream'),
            # [IN] Flags for the save.
            (DWORD, 'dwSaveFlags')
        ),
        STDMETHOD('GetSaveSize')(
            # [IN] cssAccurate or cssQuick.
            (CorSaveSize, 'fSave'),
            # [OUT] Put the size here.
            (POINTER(DWORD), 'pdwSaveSize')
        ),
        STDMETHOD('DefineTypeDef')(
            # [IN] Name of TypeDef
            (LPCWSTR, 'szTypeDef'),
            # [IN] CustomAttribute flags
            (DWORD, 'dwTypeDefFlags'),
            # [IN] extends this TypeDef or typeref
            (mdToken, 'tkExtends'),
            # [IN] Implements interfaces
            (mdToken * 0, 'rtkImplements'),
            # [OUT] Put TypeDef token here
            (POINTER(mdTypeDef), 'ptd')
        ),
        STDMETHOD('DefineNestedType')(
            # [IN] Name of TypeDef
            (LPCWSTR, 'szTypeDef'),
            # [IN] CustomAttribute flags
            (DWORD, 'dwTypeDefFlags'),
            # [IN] extends this TypeDef or typeref
            (mdToken, 'tkExtends'),
            # [IN] Implements interfaces
            (mdToken * 0, 'rtkImplements'),
            # [IN] TypeDef token of the enclosing type.
            (mdTypeDef, 'tdEncloser'),
            # [OUT] Put TypeDef token here
            (POINTER(mdTypeDef), 'ptd')
        ),
        STDMETHOD('SetHandler')(
            # [IN] The new error handler.
            (POINTER(comtypes.IUnknown), 'pUnk')
        ),
        STDMETHOD('DefineMethod')(
            # Parent TypeDef
            (mdTypeDef, 'td'),
            # Name of member
            (LPCWSTR, 'szName'),
            # Member attributes
            (DWORD, 'dwMethodFlags'),
            # [IN] point to a blob value of CLR signature
            (PCCOR_SIGNATURE, 'pvSigBlob'),
            # [IN] count of bytes in the signature blob
            (ULONG, 'cbSigBlob'),
            (ULONG, 'ulCodeRVA'),
            (DWORD, 'dwImplFlags'),
            # Put member token here
            (POINTER(mdMethodDef), 'pmd')
        ),
        STDMETHOD('DefineMethodImpl')(
            # [IN] The class implementing the method
            (mdTypeDef, 'td'),
            # [IN] Method body - MethodDef or MethodRef
            (mdToken, 'tkBody'),
            # [IN] Method declaration - MethodDef or MethodRef
            (mdToken, 'tkDecl')
        ),
        STDMETHOD('DefineTypeRefByName')(
            # [IN] ModuleRef, AssemblyRef or TypeRef.
            (mdToken, 'tkResolutionScope'),
            # [IN] Name of the TypeRef.
            (LPCWSTR, 'szName'),
            # [OUT] Put TypeRef token here.
            (POINTER(mdTypeRef), 'ptr')
        ),
        STDMETHOD('DefineImportType')(
            # [IN] Assembly containing the TypeDef.
            (POINTER(IMetaDataAssemblyImport), 'pAssemImport'),
            # [IN] Hash Blob for Assembly.
            (POINTER(VOID), 'pbHashValue'),
            # [IN] Count of bytes.
            (ULONG, 'cbHashValue'),
            # [IN] Scope containing the TypeDef.
            (POINTER(IMetaDataImport), 'pImport'),
            # [IN] The imported TypeDef.
            (mdTypeDef, 'tdImport'),
            # [IN] Assembly into which the TypeDef is imported.
            (POINTER(IMetaDataAssemblyEmit), 'pAssemEmit'),
            # [OUT] Put TypeRef token here.
            (POINTER(mdTypeRef), 'ptr')
        ),
        STDMETHOD('DefineMemberRef')(
            # [IN] ClassRef or ClassDef importing a member.
            (mdToken, 'tkImport'),
            # [IN] member's name
            (LPCWSTR, 'szName'),
            # [IN] point to a blob value of CLR signature
            (PCCOR_SIGNATURE, 'pvSigBlob'),
            # [IN] count of bytes in the signature blob
            (ULONG, 'cbSigBlob'),
            # [OUT] memberref token
            (POINTER(mdMemberRef), 'pmr')
        ),
        STDMETHOD('DefineImportMember')(
            # [IN] Assembly containing the Member.
            (POINTER(IMetaDataAssemblyImport), 'pAssemImport'),
            # [IN] Hash Blob for Assembly.
            (POINTER(VOID), 'pbHashValue'),
            # [IN] Count of bytes.
            (ULONG, 'cbHashValue'),
            # [IN] Import scope, with member.
            (POINTER(IMetaDataImport), 'pImport'),
            # [IN] Member in import scope.
            (mdToken, 'mbMember'),
            # [IN] Assembly into which the Member is imported.
            (POINTER(IMetaDataAssemblyEmit), 'pAssemEmit'),
            # [IN] Classref or classdef in emit scope.
            (mdToken, 'tkParent'),
            # [OUT] Put member ref here.
            (POINTER(mdMemberRef), 'pmr')
        ),
        STDMETHOD('DefineEvent')(
            # [IN] the class/interface on which the event is being defined
            (mdTypeDef, 'td'),
            # [IN] Name of the event
            (LPCWSTR, 'szEvent'),
            # [IN] CorEventAttr
            (DWORD, 'dwEventFlags'),
            # [IN] a reference (mdTypeRef or mdTypeRef) to the Event class
            (mdToken, 'tkEventType'),
            # [IN] required add method
            (mdMethodDef, 'mdAddOn'),
            # [IN] required remove method
            (mdMethodDef, 'mdRemoveOn'),
            # [IN] optional fire method
            (mdMethodDef, 'mdFire'),
            # [IN] optional array of other methods associate with the event
            (mdMethodDef * 0, 'rmdOtherMethods'),
            # [OUT] output event token
            (POINTER(mdEvent), 'pmdEvent')
        ),
        STDMETHOD('SetClassLayout')(
            # [IN] typedef
            (mdTypeDef, 'td'),
            # [IN] packing size specified as 1, 2, 4, 8, or 16
            (DWORD, 'dwPackSize'),
            # [IN] array of layout specification
            (COR_FIELD_OFFSET * 0, 'rFieldOffsets'),
            # [IN] size of the class
            (ULONG, 'ulClassSize')
        ),
        STDMETHOD('DeleteClassLayout')(
            # [IN] typedef whose layout is to be deleted.
            (mdTypeDef, 'td')
        ),
        STDMETHOD('SetFieldMarshal')(
            # [IN] given a fieldDef or paramDef token
            (mdToken, 'tk'),
            # [IN] native type specification
            (PCCOR_SIGNATURE, 'pvNativeType'),
            # [IN] count of bytes of pvNativeType
            (ULONG, 'cbNativeType')
        ),
        STDMETHOD('DeleteFieldMarshal')(
            # [IN] given a fieldDef or paramDef token
            (mdToken, 'tk')
        ),
        STDMETHOD('DefinePermissionSet')(
            # [IN] the object to be decorated.
            (mdToken, 'tk'),
            # [IN] CorDeclSecurity.
            (DWORD, 'dwAction'),
            # [IN] permission blob.
            (POINTER(VOID), 'pvPermission'),
            # [IN] count of bytes of pvPermission.
            (ULONG, 'cbPermission'),
            # [OUT] returned permission token.
            (POINTER(mdPermission), 'ppm')
        ),
        STDMETHOD('SetRVA')(
            # [IN] Method for which to set offset
            (mdMethodDef, 'md'),
            # [IN] The offset
            (ULONG, 'ulRVA')
        ),
        STDMETHOD('GetTokenFromSig')(
            # [IN] Signature to define.
            (PCCOR_SIGNATURE, 'pvSig'),
            # [IN] Size of signature data.
            (ULONG, 'cbSig'),
            # [OUT] returned signature token.
            (POINTER(mdSignature), 'pmsig')
        ),
        STDMETHOD('DefineModuleRef')(
            # [IN] DLL name
            (LPCWSTR, 'szName'),
            # [OUT] returned
            (POINTER(mdModuleRef), 'pmur')
        ),
        # <TODO>@FUTURE: This should go away once everyone starts using
        # SetMemberRefProps.</TODO>
        STDMETHOD('SetParent')(
            # [IN] Token for the ref to be fixed up.
            (mdMemberRef, 'mr'),
            # [IN] The ref parent.
            (mdToken, 'tk')
        ),
        STDMETHOD('GetTokenFromTypeSpec')(
            # [IN] TypeSpec Signature to define.
            (PCCOR_SIGNATURE, 'pvSig'),
            # [IN] Size of signature data.
            (ULONG, 'cbSig'),
            # [OUT] returned TypeSpec token.
            (POINTER(mdTypeSpec), 'ptypespec')
        ),
        STDMETHOD('SaveToMemory')(
            # [OUT] Location to write data.
            (POINTER(VOID), 'pbData'),
            # [IN] Max size of data buffer.
            (ULONG, 'cbData')
        ),
        STDMETHOD('DefineUserString')(
            # [IN] User literal string.
            (LPCWSTR, 'szString'),
            # [IN] Length of string.
            (ULONG, 'cchString'),
            # [OUT] String token.
            (POINTER(mdString), 'pstk')
        ),
        STDMETHOD('DeleteToken')(
            # [IN] The token to be deleted
            (mdToken, 'tkObj')
        ),
        STDMETHOD('SetMethodProps')(
            # [IN] The MethodDef.
            (mdMethodDef, 'md'),
            # [IN] Method attributes.
            (DWORD, 'dwMethodFlags'),
            # [IN] Code RVA.
            (ULONG, 'ulCodeRVA'),
            # [IN] Impl flags.
            (DWORD, 'dwImplFlags')
        ),
        STDMETHOD('SetTypeDefProps')(
            # [IN] The TypeDef.
            (mdTypeDef, 'td'),
            # [IN] TypeDef flags.
            (DWORD, 'dwTypeDefFlags'),
            # [IN] Base TypeDef or TypeRef.
            (mdToken, 'tkExtends'),
            # [IN] Implemented interfaces.
            (mdToken * 0, 'rtkImplements')
        ),
        STDMETHOD('SetEventProps')(
            # [IN] The event token.
            (mdEvent, 'ev'),
            # [IN] CorEventAttr.
            (DWORD, 'dwEventFlags'),
            # [IN] A reference (mdTypeRef or mdTypeRef) to the Event class.
            (mdToken, 'tkEventType'),
            # [IN] Add method.
            (mdMethodDef, 'mdAddOn'),
            # [IN] Remove method.
            (mdMethodDef, 'mdRemoveOn'),
            # [IN] Fire method.
            (mdMethodDef, 'mdFire'),
            # [IN] Array of other methods associate with the event.
            (mdMethodDef * 0, 'rmdOtherMethods')
        ),
        STDMETHOD('SetPermissionSetProps')(
            # [IN] The object to be decorated.
            (mdToken, 'tk'),
            # [IN] CorDeclSecurity.
            (DWORD, 'dwAction'),
            # [IN] Permission blob.
            (POINTER(VOID), 'pvPermission'),
            # [IN] Count of bytes of pvPermission.
            (ULONG, 'cbPermission'),
            # [OUT] Permission token.
            (POINTER(mdPermission), 'ppm')
        ),
        STDMETHOD('DefinePinvokeMap')(
            # [IN] FieldDef or MethodDef.
            (mdToken, 'tk'),
            # [IN] Flags used for mapping.
            (DWORD, 'dwMappingFlags'),
            # [IN] Import name.
            (LPCWSTR, 'szImportName'),
            # [IN] ModuleRef token for the target DLL.
            (mdModuleRef, 'mrImportDLL')
        ),
        STDMETHOD('SetPinvokeMap')(
            # [IN] FieldDef or MethodDef.
            (mdToken, 'tk'),
            # [IN] Flags used for mapping.
            (DWORD, 'dwMappingFlags'),
            # [IN] Import name.
            (LPCWSTR, 'szImportName'),
            # [IN] ModuleRef token for the target DLL.
            (mdModuleRef, 'mrImportDLL')
        ),
        STDMETHOD('DeletePinvokeMap')(
            # [IN] FieldDef or MethodDef.
            (mdToken, 'tk')
        ),
        # New CustomAttribute functions.
        STDMETHOD('DefineCustomAttribute')(
            # [IN] The object to put the value on.
            (mdToken, 'tkObj'),
            # [IN] Type of the CustomAttribute (TypeRef/TypeDef).
            (mdToken, 'tkType'),
            # [IN] The custom value data.
            (POINTER(VOID), 'pCustomAttribute'),
            # [IN] The custom value data length.
            (ULONG, 'cbCustomAttribute'),
            # [OUT] The custom value token value on return.
            (POINTER(mdCustomAttribute), 'pcv')
        ),
        STDMETHOD('SetCustomAttributeValue')(
            # [IN] The custom value token whose value to replace.
            (mdCustomAttribute, 'pcv'),
            # [IN] The custom value data.
            (POINTER(VOID), 'pCustomAttribute'),
            # [IN] The custom value data length.
            (ULONG, 'cbCustomAttribute')
        ),
        STDMETHOD('DefineField')(
            # Parent TypeDef
            (mdTypeDef, 'td'),
            # Name of member
            (LPCWSTR, 'szName'),
            # Member attributes
            (DWORD, 'dwFieldFlags'),
            # [IN] point to a blob value of CLR signature
            (PCCOR_SIGNATURE, 'pvSigBlob'),
            # [IN] count of bytes in the signature blob
            (ULONG, 'cbSigBlob'),
            # [IN] flag for value type. selected ELEMENT_TYPE_*
            (DWORD, 'dwCPlusTypeFlag'),
            # [IN] constant value
            (POINTER(VOID), 'pValue'),
            # [IN] size of constant value (string, in wide chars).
            (ULONG, 'cchValue'),
            # [OUT] Put member token here
            (POINTER(mdFieldDef), 'pmd')
        ),
        STDMETHOD('DefineProperty')(
            # [IN] the class/interface on which the property is being defined
            (mdTypeDef, 'td'),
            # [IN] Name of the property
            (LPCWSTR, 'szProperty'),
            # [IN] CorPropertyAttr
            (DWORD, 'dwPropFlags'),
            # [IN] the required type signature
            (PCCOR_SIGNATURE, 'pvSig'),
            # [IN] the size of the type signature blob
            (ULONG, 'cbSig'),
            # [IN] flag for value type. selected ELEMENT_TYPE_*
            (DWORD, 'dwCPlusTypeFlag'),
            # [IN] constant value
            (POINTER(VOID), 'pValue'),
            # [IN] size of constant value (string, in wide chars).
            (ULONG, 'cchValue'),
            # [IN] optional setter of the property
            (mdMethodDef, 'mdSetter'),
            # [IN] optional getter of the property
            (mdMethodDef, 'mdGetter'),
            # [IN] an optional array of other methods
            (mdMethodDef * 0, 'rmdOtherMethods'),
            # [OUT] output property token
            (POINTER(mdProperty), 'pmdProp')
        ),
        STDMETHOD('DefineParam')(
            # [IN] Owning method
            (mdMethodDef, 'md'),
            # [IN] Which param
            (ULONG, 'ulParamSeq'),
            # [IN] Optional param name
            (LPCWSTR, 'szName'),
            # [IN] Optional param flags
            (DWORD, 'dwParamFlags'),
            # [IN] flag for value type. selected ELEMENT_TYPE_*
            (DWORD, 'dwCPlusTypeFlag'),
            # [IN] constant value
            (POINTER(VOID), 'pValue'),
            # [IN] size of constant value (string, in wide chars).
            (ULONG, 'cchValue'),
            # [OUT] Put param token here
            (POINTER(mdParamDef), 'ppd')
        ),
        STDMETHOD('SetFieldProps')(
            # [IN] The FieldDef.
            (mdFieldDef, 'fd'),
            # [IN] Field attributes.
            (DWORD, 'dwFieldFlags'),
            # [IN] Flag for the value type, selected ELEMENT_TYPE_*
            (DWORD, 'dwCPlusTypeFlag'),
            # [IN] Constant value.
            (POINTER(VOID), 'pValue'),
            # [IN] size of constant value (string, in wide chars).
            (ULONG, 'cchValue')
        ),
        STDMETHOD('SetPropertyProps')(
            # [IN] Property token.
            (mdProperty, 'pr'),
            # [IN] CorPropertyAttr.
            (DWORD, 'dwPropFlags'),
            # [IN] Flag for value type, selected ELEMENT_TYPE_*
            (DWORD, 'dwCPlusTypeFlag'),
            # [IN] Constant value.
            (POINTER(VOID), 'pValue'),
            # [IN] size of constant value (string, in wide chars).
            (ULONG, 'cchValue'),
            # [IN] Setter of the property.
            (mdMethodDef, 'mdSetter'),
            # [IN] Getter of the property.
            (mdMethodDef, 'mdGetter'),
            # [IN] Array of other methods.
            (mdMethodDef * 0, 'rmdOtherMethods')
        ),
        STDMETHOD('SetParamProps')(
            # [IN] Param token.
            (mdParamDef, 'pd'),
            # [IN] Param name.
            (LPCWSTR, 'szName'),
            # [IN] Param flags.
            (DWORD, 'dwParamFlags'),
            # [IN] Flag for value type. selected ELEMENT_TYPE_*.
            (DWORD, 'dwCPlusTypeFlag'),
            # [OUT] Constant value.
            (POINTER(VOID), 'pValue'),
            # [IN] size of constant value (string, in wide chars).
            (ULONG, 'cchValue')
        ),
        # Specialized Custom Attributes for security.
        STDMETHOD('DefineSecurityAttributeSet')(
            # [IN] Class or method requiring security attributes.
            (mdToken, 'tkObj'),
            # [IN] Array of security attribute descriptions.
            (COR_SECATTR * 0, 'rSecAttrs'),
            # [IN] Count of elements in above array.
            (ULONG, 'cSecAttrs'),
            # [OUT] On error, index of attribute causing problem.
            (POINTER(ULONG), 'pulErrorAttr')
        ),
        STDMETHOD('ApplyEditAndContinue')(
            # [IN] Metadata from the delta PE.
            (POINTER(comtypes.IUnknown), 'pImport')
        ),
        STDMETHOD('TranslateSigWithScope')(
            # [IN] importing assembly interface
            (POINTER(IMetaDataAssemblyImport), 'pAssemImport'),
            # [IN] Hash Blob for Assembly.
            (POINTER(VOID), 'pbHashValue'),
            # [IN] Count of bytes.
            (ULONG, 'cbHashValue'),
            # [IN] importing interface
            (POINTER(IMetaDataImport), 'import'),
            # [IN] signature in the importing scope
            (PCCOR_SIGNATURE, 'pbSigBlob'),
            # [IN] count of bytes of signature
            (ULONG, 'cbSigBlob'),
            # [IN] emit assembly interface
            (POINTER(IMetaDataAssemblyEmit), 'pAssemEmit'),
            # [IN] emit interface
            (POINTER(IMetaDataEmit), 'emit'),
            # [OUT] buffer to hold translated signature
            (PCOR_SIGNATURE, 'pvTranslatedSig'),
            (ULONG, 'cbTranslatedSigMax'),
            # [OUT] count of bytes in the translated signature
            (POINTER(ULONG), 'pcbTranslatedSig')
        ),
        STDMETHOD('SetMethodImplFlags')(
            # [IN] Method for which to set ImplFlags
            (mdMethodDef, 'md'),
            (DWORD, 'dwImplFlags')
        ),
        STDMETHOD('SetFieldRVA')(
            # [IN] Field for which to set offset
            (mdFieldDef, 'fd'),
            # [IN] The offset
            (ULONG, 'ulRVA')
        ),
        STDMETHOD('Merge')(
            # [IN] The scope to be merged.
            (POINTER(IMetaDataImport), 'pImport'),
            # [IN] Host IMapToken interface to receive token remap notification
            (POINTER(IMapToken), 'pHostMapToken'),
            # [IN] An object to receive to receive error notification.
            (POINTER(comtypes.IUnknown), 'pHandler')
        ),
        STDMETHOD('MergeEnd')(
        ),
        # This interface is sealed. Do not change, add, or remove anything.
        # Instead, derive a new iterface.
        # IMetaDataEmi
    )

    # -------------------------------------
    # --- IMetaDataEmit2
    # -------------------------------------
    # {F5DD9950-F693-42e6-830E-7B833E8146A9}
    IID_IMetaDataEmit2 = EXTERN_GUID(
        0xF5DD9950,
        0xF693,
        0x42E6,
        0x83,
        0xE,
        0x7B,
        0x83,
        0x3E,
        0x81,
        0x46,
        0xA9
    )

    # ---
    IMetaDataEmit2 = INTERFACE('IMetaDataEmit2')
    IMetaDataEmit2._iid_ = IID_IMetaDataEmit2
    DECLARE_INTERFACE_(IMetaDataEmit2, IMetaDataEmit)(
        STDMETHOD('DefineMethodSpec')(
            # [IN] MethodDef or MemberRef
            (mdToken, 'tkParent'),
            # [IN] point to a blob value of COM+ signature
            (PCCOR_SIGNATURE, 'pvSigBlob'),
            # [IN] count of bytes in the signature blob
            (ULONG, 'cbSigBlob'),
            # [OUT] method instantiation token
            (POINTER(mdMethodSpec), 'pmi')
        ),
        STDMETHOD('GetDeltaSaveSize')(
            # [IN] cssAccurate or cssQuick.
            (CorSaveSize, 'fSave'),
            # [OUT] Put the size here.
            (POINTER(DWORD), 'pdwSaveSize')
        ),
        STDMETHOD('SaveDelta')(
            # [IN] The filename to save to.
            (LPCWSTR, 'szFile'),
            # [IN] Flags for the save.
            (DWORD, 'dwSaveFlags')
        ),
        STDMETHOD('SaveDeltaToStream')(
            # [IN] A writable stream to save to.
            (POINTER(IStream), 'pIStream'),
            # [IN] Flags for the save.
            (DWORD, 'dwSaveFlags')
        ),
        STDMETHOD('SaveDeltaToMemory')(
            # [OUT] Location to write data.
            (POINTER(VOID), 'pbData'),
            # [IN] Max size of data buffer.
            (ULONG, 'cbData')
        ),
        STDMETHOD('DefineGenericParam')(
            # [IN] TypeDef or MethodDef
            (mdToken, 'tk'),
            # [IN] Index of the type parameter
            (ULONG, 'ulParamSeq'),
            # [IN] Flags, for future use (e.g. variance)
            (DWORD, 'dwParamFlags'),
            # [IN] Name
            (LPCWSTR, 'szname'),
            # [IN] For future use (e.g. non-type parameters)
            (DWORD, 'reserved'),
            # [IN] Array of type constraints (TypeDef,TypeRef,TypeSpec)
            (mdToken * 0, 'rtkConstraints'),
            # [OUT] Put GenericParam token here
            (POINTER(mdGenericParam), 'pgp')
        ),
        STDMETHOD('SetGenericParamProps')(
            # [IN] GenericParam
            (mdGenericParam, 'gp'),
            # [IN] Flags, for future use (e.g. variance)
            (DWORD, 'dwParamFlags'),
            # [IN] Optional name
            (LPCWSTR, 'szName'),
            # [IN] For future use (e.g. non-type parameters)
            (DWORD, 'reserved'),
            # [IN] Array of type constraints (TypeDef,TypeRef,TypeSpec)
            (mdToken * 0, 'rtkConstraints')
        ),
        STDMETHOD('ResetENCLog')(
        )
    )

    # -------------------------------------
    # --- IMetaDataImport
    # -------------------------------------
    # {7DAC8207-D3AE-4c75-9B67-92801A497D44}
    IID_IMetaDataImport = EXTERN_GUID(
        0x7DAC8207,
        0xD3AE,
        0x4C75,
        0x9B,
        0x67,
        0x92,
        0x80,
        0x1A,
        0x49,
        0x7D,
        0x44
    )

    # ---

    IMetaDataImport._iid_ = IID_IMetaDataImport
    DECLARE_INTERFACE_(IMetaDataImport, comtypes.IUnknown)(
        STDMETHOD('VOID, CloseEnum')(
            (HCORENUM, 'hEnum')
        ),
        STDMETHOD('CountEnum')(
            (HCORENUM, 'hEnum'),
            (POINTER(ULONG), 'pulCount')
        ),
        STDMETHOD('ResetEnum')(
            (HCORENUM, 'hEnum'),
            (ULONG, 'ulPos')
        ),
        STDMETHOD('EnumTypeDefs')(
            (POINTER(HCORENUM), 'phEnum'),
            (mdTypeDef * 0, 'rTypeDefs'),
            (ULONG, 'cMax'),
            (POINTER(ULONG), 'pcTypeDefs')
        ),
        STDMETHOD('EnumInterfaceImpls')(
            (POINTER(HCORENUM), 'phEnum'),
            (mdTypeDef, 'td'),
            (mdInterfaceImpl * 0, 'rImpls'),
            (ULONG, 'cMax'),
            (POINTER(ULONG), 'pcImpls')
        ),
        STDMETHOD('EnumTypeRefs')(
            (POINTER(HCORENUM), 'phEnum'),
            (mdTypeRef * 0, 'rTypeRefs'),
            (ULONG, 'cMax'),
            (POINTER(ULONG), 'pcTypeRefs')
        ),
        STDMETHOD('FindTypeDefByName')(
            # [IN] Name of the Type.
            (LPCWSTR, 'szTypeDef'),
            # [IN] TypeDef/TypeRef for Enclosing class.
            (mdToken, 'tkEnclosingClass'),
            # [OUT] Put the TypeDef token here.
            (POINTER(mdTypeDef), 'ptd')
        ),
        STDMETHOD('GetScopeProps')(
            (LPWSTR, 'szName'),
            # [OUT] Put the name here.
            (ULONG, 'cchName'),
            # [IN] Size of name buffer in wide chars.
            (POINTER(ULONG), 'pchName'),
            # [OUT] Put size of name (wide chars) here.
            (POINTER(GUID), 'pmvid')
        ),
        STDMETHOD('GetModuleFromScope')(
            # [OUT] Put mdModule token here.
            (POINTER(mdModule), 'pmd')
        ),
        STDMETHOD('GetTypeDefProps')(
            # [IN] TypeDef token for inquiry.
            (mdTypeDef, 'td'),
            (LPWSTR, 'szTypeDef'),
            # [OUT] Put name here.
            (ULONG, 'cchTypeDef'),
            # [IN] size of name buffer in wide chars.
            (POINTER(ULONG), 'pchTypeDef'),
            # [OUT] put size of name (wide chars) here.
            (POINTER(DWORD), 'pdwTypeDefFlags'),
            # [OUT] Put flags here.
            (POINTER(mdToken), 'ptkExtends')
        ),
        STDMETHOD('GetInterfaceImplProps')(
            # [IN] InterfaceImpl token.
            (mdInterfaceImpl, 'iiImpl'),
            # [OUT] Put implementing class token here.
            (POINTER(mdTypeDef), 'pClass'),
            # [OUT] Put implemented interface token here.
            (POINTER(mdToken), 'ptkIface')
        ),
        STDMETHOD('GetTypeRefProps')(
            # [IN] TypeRef token.
            (mdTypeRef, 'tr'),
            # [OUT] Resolution scope, ModuleRef or AssemblyRef.
            (POINTER(mdToken), 'ptkResolutionScope'),
            (LPWSTR, 'szName'),
            # [OUT] Name of the TypeRef.
            (ULONG, 'cchName'),
            # [IN] Size of buffer.
            (POINTER(ULONG), 'pchName')
        ),
        STDMETHOD('ResolveTypeRef')(
            (mdTypeRef, 'tr'),
            (REFIID, 'riid'),
            (POINTER(POINTER(comtypes.IUnknown)), 'ppIScope'),
            (POINTER(mdTypeDef), 'ptd')
        ),
        STDMETHOD('EnumMembers')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] TypeDef to scope the enumeration.
            (mdTypeDef, 'cl'),
            # [OUT] Put MemberDefs here.
            (mdToken * 0, 'rMembers'),
            # [IN] Max MemberDefs to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumMembersWithName')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] TypeDef to scope the enumeration.
            (mdTypeDef, 'cl'),
            # [IN] Limit results to those with this name.
            (LPCWSTR, 'szName'),
            # [OUT] Put MemberDefs here.
            (mdToken * 0, 'rMembers'),
            # [IN] Max MemberDefs to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumMethods')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] TypeDef to scope the enumeration.
            (mdTypeDef, 'cl'),
            # [OUT] Put MethodDefs here.
            (mdMethodDef * 0, 'rMethods'),
            # [IN] Max MethodDefs to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumMethodsWithName')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] TypeDef to scope the enumeration.
            (mdTypeDef, 'cl'),
            # [IN] Limit results to those with this name.
            (LPCWSTR, 'szName'),
            # [OU] Put MethodDefs here.
            (mdMethodDef * 0, 'rMethods'),
            # [IN] Max MethodDefs to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumFields')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] TypeDef to scope the enumeration.
            (mdTypeDef, 'cl'),
            # [OUT] Put FieldDefs here.
            (mdFieldDef * 0, 'rFields'),
            # [IN] Max FieldDefs to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumFieldsWithName')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] TypeDef to scope the enumeration.
            (mdTypeDef, 'cl'),
            # [IN] Limit results to those with this name.
            (LPCWSTR, 'szName'),
            # [OUT] Put MemberDefs here.
            (mdFieldDef * 0, 'rFields'),
            # [IN] Max MemberDefs to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumParams')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] MethodDef to scope the enumeration.
            (mdMethodDef, 'mb'),
            # [OUT] Put ParamDefs here.
            (mdParamDef * 0, 'rParams'),
            # [IN] Max ParamDefs to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumMemberRefs')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] Parent token to scope the enumeration.
            (mdToken, 'tkParent'),
            # [OUT] Put MemberRefs here.
            (mdMemberRef * 0, 'rMemberRefs'),
            # [IN] Max MemberRefs to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumMethodImpls')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] TypeDef to scope the enumeration.
            (mdTypeDef, 'td'),
            # [OUT] Put Method Body tokens here.
            (mdToken * 0, 'rMethodBody'),
            # [OUT] Put Method Declaration tokens here.
            (mdToken * 0, 'rMethodDecl'),
            # [IN] Max tokens to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumPermissionSets')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] if not NIL, token to scope the enumeration.
            (mdToken, 'tk'),
            # [IN] if not 0, return only these actions.
            (DWORD, 'dwActions'),
            # [OUT] Put Permissions here.
            (mdPermission * 0, 'rPermission'),
            # [IN] Max Permissions to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('FindMember')(
            # [IN] given typedef
            (mdTypeDef, 'td'),
            # [IN] member name
            (LPCWSTR, 'szName'),
            # [IN] point to a blob value of CLR signature
            (PCCOR_SIGNATURE, 'pvSigBlob'),
            # [IN] count of bytes in the signature blob
            (ULONG, 'cbSigBlob'),
            # [OUT] matching memberdef
            (POINTER(mdToken), 'pmb')
        ),
        STDMETHOD('FindMethod')(
            # [IN] given typedef
            (mdTypeDef, 'td'),
            # [IN] member name
            (LPCWSTR, 'szName'),
            # [IN] point to a blob value of CLR signature
            (PCCOR_SIGNATURE, 'pvSigBlob'),
            # [IN] count of bytes in the signature blob
            (ULONG, 'cbSigBlob'),
            # [OUT] matching memberdef
            (POINTER(mdMethodDef), 'pmb')
        ),
        STDMETHOD('FindField')(
            # [IN] given typedef
            (mdTypeDef, 'td'),
            # [IN] member name
            (LPCWSTR, 'szName'),
            # [IN] point to a blob value of CLR signature
            (PCCOR_SIGNATURE, 'pvSigBlob'),
            # [IN] count of bytes in the signature blob
            (ULONG, 'cbSigBlob'),
            # [OUT] matching memberdef
            (POINTER(mdFieldDef), 'pmb')
        ),
        STDMETHOD('FindMemberRef')(
            # [IN] given typeRef
            (mdTypeRef, 'td'),
            # [IN] member name
            (LPCWSTR, 'szName'),
            # [IN] point to a blob value of CLR signature
            (PCCOR_SIGNATURE, 'pvSigBlob'),
            # [IN] count of bytes in the signature blob
            (ULONG, 'cbSigBlob'),
            # [OUT] matching memberref
            (POINTER(mdMemberRef), 'pmr')
        ),
        STDMETHOD('GetMethodProps')(
            # The method for which to get props.
            (mdMethodDef, 'mb'),
            # Put method's class here.
            (POINTER(mdTypeDef), 'pClass'),
            (LPWSTR, 'szMethod'),
            # Put method's name here.
            (ULONG, 'cchMethod'),
            # Size of szMethod buffer in wide chars.
            (POINTER(ULONG), 'pchMethod'),
            # Put actual size here
            (POINTER(DWORD), 'pdwAttr'),
            # Put flags here.
            (POINTER(PCCOR_SIGNATURE), 'ppvSigBlob'),
            # [OUT] point to the blob value of meta data
            (POINTER(ULONG), 'pcbSigBlob'),
            # [OUT] actual size of signature blob
            (POINTER(ULONG), 'pulCodeRVA'),
            # [OUT] codeRVA
            (POINTER(DWORD), 'pdwImplFlags')
        ),
        STDMETHOD('GetMemberRefProps')(
            # [IN] given memberref
            (mdMemberRef, 'mr'),
            # [OUT] Put classref or classdef here.
            (POINTER(mdToken), 'ptk'),
            (LPWSTR, 'szMember'),
            # [OUT] buffer to fill for member's name
            (ULONG, 'cchMember'),
            # [IN] the count of CHAR of szMember
            (POINTER(ULONG), 'pchMember'),
            # [OUT] actual count of CHAR in member name
            (POINTER(PCCOR_SIGNATURE), 'ppvSigBlob'),
            # [OUT] point to meta data blob value
            (POINTER(ULONG), 'pbSig')
        ),
        STDMETHOD('EnumProperties')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] TypeDef to scope the enumeration.
            (mdTypeDef, 'td'),
            # [OUT] Put Properties here.
            (mdProperty * 0, 'rProperties'),
            # [IN] Max properties to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcProperties')
        ),
        STDMETHOD('EnumEvents')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] TypeDef to scope the enumeration.
            (mdTypeDef, 'td'),
            # [OUT] Put events here.
            (mdEvent * 0, 'rEvents'),
            # [IN] Max events to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcEvents')
        ),
        STDMETHOD('GetEventProps')(
            # [IN] event token
            (mdEvent, 'ev'),
            # [OUT] typedef containing the event declarion.
            (POINTER(mdTypeDef), 'pClass'),
            # [OUT] Event name
            (LPCWSTR, 'szEvent'),
            # [IN] the count of wchar of szEvent
            (ULONG, 'cchEvent'),
            # [OUT] actual count of wchar for event's name
            (POINTER(ULONG), 'pchEvent'),
            # [OUT] Event flags.
            (POINTER(DWORD), 'pdwEventFlags'),
            # [OUT] EventType class
            (POINTER(mdToken), 'ptkEventType'),
            # [OUT] AddOn method of the event
            (POINTER(mdMethodDef), 'pmdAddOn'),
            # [OUT] RemoveOn method of the event
            (POINTER(mdMethodDef), 'pmdRemoveOn'),
            # [OUT] Fire method of the event
            (POINTER(mdMethodDef), 'pmdFire'),
            # [OUT] other method of the event
            (mdMethodDef * 0, 'rmdOtherMethod'),
            # [IN] size of rmdOtherMethod
            (ULONG, 'cMax'),
            # [OUT] total number of other method of this event
            (POINTER(ULONG), 'pcOtherMethod')
        ),
        STDMETHOD('EnumMethodSemantics')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] MethodDef to scope the enumeration.
            (mdMethodDef, 'mb'),
            # [OUT] Put Event/Property here.
            (mdToken * 0, 'rEventProp'),
            # [IN] Max properties to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcEventProp')
        ),
        STDMETHOD('GetMethodSemantics')(
            # [IN] method token
            (mdMethodDef, 'mb'),
            # [IN] event/property token.
            (mdToken, 'tkEventProp'),
            # [OUT] the role flags for the method/propevent pair
            (POINTER(DWORD), 'pdwSemanticsFlags')
        ),
        STDMETHOD('GetClassLayout')(
            # [IN] give typedef
            (mdTypeDef, 'td'),
            # [OUT] 1, 2, 4, 8, or 16
            (POINTER(DWORD), 'pdwPackSize'),
            # [OUT] field offset array
            (COR_FIELD_OFFSET * 0, 'rFieldOffset'),
            # [IN] size of the array
            (ULONG, 'cMax'),
            # [OUT] needed array size
            (POINTER(ULONG), 'pcFieldOffset'),
            # [OUT] the size of the class
            (POINTER(ULONG), 'pulClassSize')
        ),
        STDMETHOD('GetFieldMarshal')(
            # [IN] given a field's memberdef
            (mdToken, 'tk'),
            # [OUT] native type of this field
            (POINTER(PCCOR_SIGNATURE), 'ppvNativeType'),
            # [OUT] the count of bytes of *ppvNativeType
            (POINTER(ULONG), 'pcbNativeType')
        ),
        STDMETHOD('GetRVA')(
            # Member for which to set offset
            (mdToken, 'tk'),
            # The offset
            (POINTER(ULONG), 'pulCodeRVA'),
            # the implementation flags
            (POINTER(DWORD), 'pdwImplFlags')
        ),
        STDMETHOD('GetPermissionSetProps')(
            # [IN] the permission token.
            (mdPermission, 'pm'),
            # [OUT] CorDeclSecurity.
            (POINTER(DWORD), 'pdwAction'),
            # [OUT] permission blob.
            (POINTER(POINTER(VOID)), 'ppvPermission'),
            # [OUT] count of bytes of pvPermission.
            (POINTER(ULONG), 'pcbPermission')
        ),
        STDMETHOD('GetSigFromToken')(
            # [IN] Signature token.
            (mdSignature, 'mdSig'),
            # [OUT] return pointer to token.
            (POINTER(PCCOR_SIGNATURE), 'ppvSig'),
            # [OUT] return size of signature.
            (POINTER(ULONG), 'pcbSig')
        ),
        STDMETHOD('GetModuleRefProps')(
            # [IN] moduleref token.
            (mdModuleRef, 'mur'),
            (LPWSTR, 'szName'),
            # [OUT] buffer to fill with the moduleref name.
            (ULONG, 'cchName'),
            # [IN] size of szName in wide characters.
            (POINTER(ULONG), 'pchName')
        ),
        STDMETHOD('EnumModuleRefs')(
            # [IN | OUT] pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [OUT] put modulerefs here.
            (mdModuleRef * 0, 'rModuleRefs'),
            # [IN] max memberrefs to put.
            (ULONG, 'cmax'),
            # [OUT] put put here.
            (POINTER(ULONG), 'pcModuleRefs')
        ),
        STDMETHOD('GetTypeSpecFromToken')(
            # [IN] TypeSpec token.
            (mdTypeSpec, 'typespec'),
            # [OUT] return pointer to TypeSpec signature
            (POINTER(PCCOR_SIGNATURE), 'ppvSig'),
            # [OUT] return size of signature.
            (POINTER(ULONG), 'pcbSig')
        ),
        STDMETHOD('GetNameFromToken')(
            # [IN] Token to get name from. Must have a name.
            (mdToken, 'tk'),
            # [OUT] Return pointer to UTF8 name in heap.
            (POINTER(MDUTF8CSTR), 'pszUtf8NamePtr')
        ),
        STDMETHOD('EnumUnresolvedMethods')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [OUT] Put MemberDefs here.
            (mdToken * 0, 'rMethods'),
            # [IN] Max MemberDefs to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('GetUserString')(
            # [IN] String token.
            (mdString, 'stk'),
            (LPWSTR, 'szString'),
            # [OUT] Copy of string.
            (ULONG, 'cchString'),
            # [IN] Max chars of room in szString.
            (POINTER(ULONG), 'pchString')
        ),
        STDMETHOD('GetPinvokeMap')(
            # [IN] FieldDef or MethodDef.
            (mdToken, 'tk'),
            # [OUT] Flags used for mapping.
            (POINTER(DWORD), 'pdwMappingFlags'),
            (LPWSTR, 'szImportName'),
            # [OUT] Import name.
            (ULONG, 'cchImportName'),
            # [IN] Size of the name buffer.
            (POINTER(ULONG), 'pchImportName'),
            # [OUT] Actual number of characters stored.
            (POINTER(mdModuleRef), 'pmrImportDLL')
        ),
        STDMETHOD('EnumSignatures')(
            # [IN | OUT] pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [OUT] put signatures here.
            (mdSignature * 0, 'rSignatures'),
            # [IN] max signatures to put.
            (ULONG, 'cmax'),
            # [OUT] put put here.
            (POINTER(ULONG), 'pcSignatures')
        ),
        STDMETHOD('EnumTypeSpecs')(
            # [IN | OUT] pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [OUT] put TypeSpecs here.
            (mdTypeSpec * 0, 'rTypeSpecs'),
            # [IN] max TypeSpecs to put.
            (ULONG, 'cmax'),
            # [OUT] put put here.
            (POINTER(ULONG), 'pcTypeSpecs')
        ),
        STDMETHOD('EnumUserStrings')(
            # [IN/OUT] pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [OUT] put Strings here.
            (mdString * 0, 'rStrings'),
            # [IN] max Strings to put.
            (ULONG, 'cmax'),
            # [OUT] put put here.
            (POINTER(ULONG), 'pcStrings')
        ),
        STDMETHOD('GetParamForMethodIndex')(
            # [IN] Method token.
            (mdMethodDef, 'md'),
            # [IN] Parameter sequence.
            (ULONG, 'ulParamSeq'),
            # [IN] Put Param token here.
            (POINTER(mdParamDef), 'ppd')
        ),
        STDMETHOD('EnumCustomAttributes')(
            # [IN, OUT] COR enumerator.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] Token to scope the enumeration, 0 for all.
            (mdToken, 'tk'),
            # [IN] Type of interest, 0 for all.
            (mdToken, 'tkType'),
            # [OUT] Put custom attribute tokens here.
            (mdCustomAttribute * 0, 'rCustomAttributes'),
            # [IN] Size of rCustomAttributes.
            (ULONG, 'cMax'),
            # [OUT, OPTIONAL] Put count of token values here.
            (POINTER(ULONG), 'pcCustomAttributes')
        ),
        STDMETHOD('GetCustomAttributeProps')(
            # [IN] CustomAttribute token.
            (mdCustomAttribute, 'cv'),
            # [OUT, OPTIONAL] Put object token here.
            (POINTER(mdToken), 'ptkObj'),
            # [OUT, OPTIONAL] Put AttrType token here.
            (POINTER(mdToken), 'ptkType'),
            # [OUT, OPTIONAL] Put pointer to data here.
            (POINTER(POINTER(VOID)), 'ppBlob'),
            # [OUT, OPTIONAL] Put size of date here.
            (POINTER(ULONG), 'pcbSize')
        ),
        STDMETHOD('FindTypeRef')(
            # [IN] ModuleRef, AssemblyRef or TypeRef.
            (mdToken, 'tkResolutionScope'),
            # [IN] TypeRef Name.
            (LPCWSTR, 'szName'),
            # [OUT] matching TypeRef.
            (POINTER(mdTypeRef), 'ptr')
        ),
        STDMETHOD('GetMemberProps')(
            # The member for which to get props.
            (mdToken, 'mb'),
            # Put member's class here.
            (POINTER(mdTypeDef), 'pClass'),
            (LPWSTR, 'szMember'),
            # Put member's name here.
            (ULONG, 'cchMember'),
            # Size of szMember buffer in wide chars.
            (POINTER(ULONG), 'pchMember'),
            # Put actual size here
            (POINTER(DWORD), 'pdwAttr'),
            # Put flags here.
            (POINTER(PCCOR_SIGNATURE), 'ppvSigBlob'),
            # [OUT] point to the blob value of meta data
            (POINTER(ULONG), 'pcbSigBlob'),
            # [OUT] actual size of signature blob
            (POINTER(ULONG), 'pulCodeRVA'),
            # [OUT] codeRVA
            (POINTER(DWORD), 'pdwImplFlags'),
            # [OUT] Impl. Flags
            (POINTER(DWORD), 'pdwCPlusTypeFlag'),
            # [OUT] flag for value type. selected ELEMENT_TYPE_*
            (POINTER(UVCP_CONSTANT), 'ppValue'),
            # [OUT] constant value
            (POINTER(ULONG), 'pcchValue')
        ),
        STDMETHOD('GetFieldProps')(
            # The field for which to get props.
            (mdFieldDef, 'mb'),
            # Put field's class here.
            (POINTER(mdTypeDef), 'pClass'),
            (LPWSTR, 'szField'),
            # Put field's name here.
            (ULONG, 'cchField'),
            # Size of szField buffer in wide chars.
            (POINTER(ULONG), 'pchField'),
            # Put actual size here
            (POINTER(DWORD), 'pdwAttr'),
            # Put flags here.
            (POINTER(PCCOR_SIGNATURE), 'ppvSigBlob'),
            # [OUT] point to the blob value of meta data
            (POINTER(ULONG), 'pcbSigBlob'),
            # [OUT] actual size of signature blob
            (POINTER(DWORD), 'pdwCPlusTypeFlag'),
            # [OUT] flag for value type. selected ELEMENT_TYPE_*
            (POINTER(UVCP_CONSTANT), 'ppValue'),
            # [OUT] constant value
            (POINTER(ULONG), 'pcchValue')
        ),
        STDMETHOD('GetPropertyProps')(
            # [IN] property token
            (mdProperty, 'prop'),
            # [OUT] typedef containing the property declarion.
            (POINTER(mdTypeDef), 'pClass'),
            # [OUT] Property name
            (LPCWSTR, 'szProperty'),
            # [IN] the count of wchar of szProperty
            (ULONG, 'cchProperty'),
            # [OUT] actual count of wchar for property name
            (POINTER(ULONG), 'pchProperty'),
            # [OUT] property flags.
            (POINTER(DWORD), 'pdwPropFlags'),
            # [OUT] property type. pointing to meta data internal blob
            (POINTER(PCCOR_SIGNATURE), 'ppvSig'),
            # [OUT] count of bytes in *ppvSig
            (POINTER(ULONG), 'pbSig'),
            # [OUT] flag for value type. selected ELEMENT_TYPE_*
            (POINTER(DWORD), 'pdwCPlusTypeFlag'),
            # [OUT] constant value
            (POINTER(UVCP_CONSTANT), 'ppDefaultValue'),
            # [OUT] size of constant string in chars, 0 for non-strings.
            (POINTER(ULONG), 'pcchDefaultValue'),
            # [OUT] setter method of the property
            (POINTER(mdMethodDef), 'pmdSetter'),
            # [OUT] getter method of the property
            (POINTER(mdMethodDef), 'pmdGetter'),
            # [OUT] other method of the property
            (mdMethodDef * 0, 'rmdOtherMethod'),
            # [IN] size of rmdOtherMethod
            (ULONG, 'cMax'),
            # [OUT] total number of other method of this property
            (POINTER(ULONG), 'pcOtherMethod')
        ),
        STDMETHOD('GetParamProps')(
            # [IN]The Parameter.
            (mdParamDef, 'tk'),
            # [OUT] Parent Method token.
            (POINTER(mdMethodDef), 'pmd'),
            # [OUT] Parameter sequence.
            (POINTER(ULONG), 'pulSequence'),
            (LPWSTR, 'szName'),
            # [OUT] Put name here.
            (ULONG, 'cchName'),
            # [OUT] Size of name buffer.
            (POINTER(ULONG), 'pchName'),
            # [OUT] Put actual size of name here.
            (POINTER(DWORD), 'pdwAttr'),
            # [OUT] Put flags here.
            (POINTER(DWORD), 'pdwCPlusTypeFlag'),
            # [OUT] Flag for value type. selected ELEMENT_TYPE_*.
            (POINTER(UVCP_CONSTANT), 'ppValue'),
            # [OUT] Constant value.
            (POINTER(ULONG), 'pcchValue')
        ),
        STDMETHOD('GetCustomAttributeByName')(
            # [IN] Object with Custom Attribute.
            (mdToken, 'tkObj'),
            # [IN] Name of desired Custom Attribute.
            (LPCWSTR, 'szName'),
            # [OUT] Put pointer to data here.
            (POINTER(POINTER(VOID)), 'ppData'),
            # [OUT] Put size of data here.
            (POINTER(ULONG), 'pcbData')
        ),
        STDMETHOD('BOOL, IsValidToken')(
            # [IN] Given token.
            (mdToken, 'tk')
        ),
        STDMETHOD('GetNestedClassProps')(
            # [IN] NestedClass token.
            (mdTypeDef, 'tdNestedClass'),
            # [OUT] EnclosingClass token.
            (POINTER(mdTypeDef), 'ptdEnclosingClass')
        ),
        STDMETHOD('GetNativeCallConvFromSig')(
            # [IN] Pointer to signature.
            (POINTER(VOID), 'pvSig'),
            # [IN] Count of signature bytes.
            (ULONG, 'cbSig'),
            # [OUT] Put calling conv here (see CorPinvokemap).
            (POINTER(ULONG), 'pCallConv')
        ),
        STDMETHOD('IsGlobal')(
            # [IN] Type, Field, or Method token.
            (mdToken, 'pd'),
            # [OUT] Put 1 if global, 0 otherwise.
            (POINTER(INT), 'pbGlobal')
        ),
        # This interface is sealed. Do not change, add, or remove anything.
        # Instead, derive a new iterface.
        # IMetaDataImpor
    )

    # -------------------------------------
    # --- IMetaDataImport2
    # -------------------------------------
    # {FCE5EFA0-8BBA-4f8e-A036-8F2022B08466}
    IID_IMetaDataImport2 = EXTERN_GUID(
        0xFCE5EFA0,
        0x8BBA,
        0x4F8E,
        0xA0,
        0x36,
        0x8F,
        0x20,
        0x22,
        0xB0,
        0x84,
        0x66
    )

    # ---
    IMetaDataImport2 = INTERFACE('IMetaDataImport2')
    IMetaDataImport2._iid_ = IID_IMetaDataImport2
    DECLARE_INTERFACE_(IMetaDataImport2, IMetaDataImport)(
        STDMETHOD('EnumGenericParams')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] TypeDef or MethodDef whose generic parameters are requested
            (mdToken, 'tk'),
            # [OUT] Put GenericParams here.
            (mdGenericParam * 0, 'rGenericParams'),
            # [IN] Max GenericParams to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcGenericParams')
        ),
        STDMETHOD('GetGenericParamProps')(
            # [IN] GenericParam
            (mdGenericParam, 'gp'),
            # [OUT] Index of the type parameter
            (POINTER(ULONG), 'pulParamSeq'),
            # [OUT] Flags, for future use (e.g. variance)
            (POINTER(DWORD), 'pdwParamFlags'),
            # [OUT] Owner (TypeDef or MethodDef)
            (POINTER(mdToken), 'ptOwner'),
            # [OUT] For future use (e.g. non-type parameters)
            (POINTER(DWORD), 'reserved'),
            (LPWSTR, 'wzname'),
            # [OUT] Put name here
            (ULONG, 'cchName'),
            # [IN] Size of buffer
            (POINTER(ULONG), 'pchName')
        ),
        STDMETHOD('GetMethodSpecProps')(
            # [IN] The method instantiation
            (mdMethodSpec, 'mi'),
            # [OUT] MethodDef or MemberRef
            (POINTER(mdToken), 'tkParent'),
            # [OUT] point to the blob value of meta data
            (POINTER(PCCOR_SIGNATURE), 'ppvSigBlob'),
            # [OUT] actual size of signature blob
            (POINTER(ULONG), 'pcbSigBlob')
        ),
        STDMETHOD('EnumGenericParamConstraints')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] GenericParam whose constraints are requested
            (mdGenericParam, 'tk'),
            # [OUT] Put GenericParamConstraints here.
            (mdGenericParamConstraint * 0, 'rGenericParamConstraints'),
            # [IN] Max GenericParamConstraints to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcGenericParamConstraints')
        ),
        STDMETHOD('GetGenericParamConstraintProps')(
            # [IN] GenericParamConstraint
            (mdGenericParamConstraint, 'gpc'),
            # [OUT] GenericParam that is constrained
            (POINTER(mdGenericParam), 'ptGenericParam'),
            # [OUT] TypeDef/Ref/Spec constraint
            (POINTER(mdToken), 'ptkConstraintType')
        ),
        STDMETHOD('GetPEKind')(
            # [OUT] The kind of PE (0 - not a PE)
            (POINTER(DWORD), 'pdwPEKind'),
            # [OUT] Machine as defined in NT header
            (POINTER(DWORD), 'pdwMAchine')
        ),
        STDMETHOD('GetVersionString')(
            (LPWSTR, 'pwzBuf'),
            # [OUT[ Put version string here.
            (DWORD, 'cchBufSize'),
            # [IN] size of the buffer, in wide chars
            (POINTER(DWORD), 'pccBufSize')
        ),
        STDMETHOD('EnumMethodSpecs')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [IN] MethodDef or MemberRef whose MethodSpecs are requested
            (mdToken, 'tk'),
            # [OUT] Put MethodSpecs here.
            (mdMethodSpec * 0, 'rMethodSpecs'),
            # [IN] Max tokens to put.
            (ULONG, 'cMax'),
            # [OUT] Put actual count here.
            (POINTER(ULONG), 'pcMethodSpecs')
        ),
        # IMetaDataImport
    )
    # -------------------------------------
    # --- IMetaDataFilter
    # -------------------------------------
    # {D0E80DD1-12D4-11d3-B39D-00C04FF81795}
    IID_IMetaDataFilter = EXTERN_GUID(
        0xD0E80DD1,
        0x12D4,
        0x11D3,
        0xB3,
        0x9D,
        0x0,
        0xC0,
        0x4F,
        0xF8,
        0x17,
        0x95
    )
    # ---
    IMetaDataFilter = INTERFACE('IMetaDataFilter')
    IMetaDataFilter._iid_ = IID_IMetaDataFilter
    DECLARE_INTERFACE_(IMetaDataFilter, comtypes.IUnknown)(
        STDMETHOD('UnmarkAll')(
        ),
        STDMETHOD('MarkToken')(
            (mdToken, 'tk')
        ),
        STDMETHOD('IsTokenMarked')(
            (mdToken, 'tk'),
            (POINTER(BOOL), 'pIsMarked')
        )
    )
    # -------------------------------------
    # --- IHostFilter
    # -------------------------------------
    # {D0E80DD3-12D4-11d3-B39D-00C04FF81795}
    IID_IHostFilter = EXTERN_GUID(
        0xD0E80DD3,
        0x12D4,
        0x11D3,
        0xB3,
        0x9D,
        0x0,
        0xC0,
        0x4F,
        0xF8,
        0x17,
        0x95
    )
    # ---
    IHostFilter = INTERFACE('IHostFilter')
    IHostFilter._iid_ = IID_IHostFilter
    DECLARE_INTERFACE_(IHostFilter, comtypes.IUnknown)(
        STDMETHOD('MarkToken')(
            (mdToken, 'tk')
        )
    )
    # --------------------------------------
    # --- IMetaDataConverter
    # --------------------------------------
    # {D9DEBD79-2992-11d3-8BC1-0000F8083A57}
    IID_IMetaDataConverter = EXTERN_GUID(
        0xD9DEBD79,
        0x2992,
        0x11D3,
        0x8B,
        0xC1,
        0x0,
        0x0,
        0xF8,
        0x8,
        0x3A,
        0x57
    )
    # ---
    IMetaDataConverter = INTERFACE('IMetaDataConverter')
    IMetaDataConverter._iid_ = IID_IMetaDataConverter
    DECLARE_INTERFACE_(IMetaDataConverter, comtypes.IUnknown)(
        STDMETHOD('GetMetaDataFromTypeInfo')(
            # [in] Type info
            (POINTER(ITypeInfo), 'pITI'),
            # [out] return IMetaDataImport on success
            (POINTER(POINTER(IMetaDataImport)), 'ppMDI')
        ),
        STDMETHOD('GetMetaDataFromTypeLib')(
            # [in] Type library
            (POINTER(ITypeLib), 'pITL'),
            # [out] return IMetaDataImport on success
            (POINTER(POINTER(IMetaDataImport)), 'ppMDI')
        ),
        STDMETHOD('GetTypeLibFromMetaData')(
            # [in] Module name
            (BSTR, 'strModule'),
            # [in] Type library name
            (BSTR, 'strTlbName'),
            # [out] return ITypeLib on success
            (POINTER(POINTER(ITypeLib)), 'ppITL')
        )
    )
    # **********************************************************************
    # Assembly Declarations
    # **********************************************************************
    OSINFO._fields_ = [
        # Operating system platform.
        ('dwOSPlatformId', DWORD),
        # OS Major version.
        ('dwOSMajorVersion', DWORD),
        # OS Minor version.
        ('dwOSMinorVersion', DWORD),
    ]
    ASSEMBLYMETADATA._fields_ = [
        # Major Version.
        ('usMajorVersion', USHORT),
        # Minor Version.
        ('usMinorVersion', USHORT),
        # Build Number.
        ('usBuildNumber', USHORT),
        # Revision Number.
        ('usRevisionNumber', USHORT),
        # Locale.
        ('szLocale', LPWSTR),
        # [IN/OUT] Size of the buffer in wide chars/Actual size.
        ('cbLocale', ULONG),
        # Processor ID array.
        ('rProcessor', POINTER(DWORD)),
        # [IN/OUT] Size of the Processor ID array/Actual of entries filled in.
        ('ulProcessor', ULONG),
        # OSINFO array.
        ('rOS', POINTER(OSINFO)),
        # [IN/OUT]Size of the OSINFO array/Actual of entries filled in.
        ('ulOS', ULONG),
    ]
    # {211EF15B-5317-4438-B196-DEC87B887693}
    IID_IMetaDataAssemblyEmit = EXTERN_GUID(
        0x211EF15B,
        0x5317,
        0x4438,
        0xB1,
        0x96,
        0xDE,
        0xC8,
        0x7B,
        0x88,
        0x76,
        0x93
    )
    # ---
    IMetaDataAssemblyEmit._iid_ = IID_IMetaDataAssemblyEmit
    DECLARE_INTERFACE_(IMetaDataAssemblyEmit, comtypes.IUnknown)(
        STDMETHOD('DefineAssembly')(
            # [IN] Public key of the assembly.
            (POINTER(VOID), 'pbPublicKey'),
            # [IN] Count of bytes in the public key.
            (ULONG, 'cbPublicKey'),
            # [IN] Hash algorithm used to hash the files.
            (ULONG, 'ulHashAlgId'),
            # [IN] Name of the assembly.
            (LPCWSTR, 'szName'),
            # [IN] Assembly MetaData.
            (POINTER(ASSEMBLYMETADATA), 'pMetaData'),
            # [IN] Flags.
            (DWORD, 'dwAssemblyFlags'),
            # [OUT] Returned Assembly token.
            (POINTER(mdAssembly), 'pma')
        ),
        STDMETHOD('DefineAssemblyRef')(
            # [IN] Public key or token of the assembly.
            (POINTER(VOID), 'pbPublicKeyOrToken'),
            # [IN] Count of bytes in the public key or token.
            (ULONG, 'cbPublicKeyOrToken'),
            # [IN] Name of the assembly being referenced.
            (LPCWSTR, 'szName'),
            # [IN] Assembly MetaData.
            (POINTER(ASSEMBLYMETADATA), 'pMetaData'),
            # [IN] Hash Blob.
            (POINTER(VOID), 'pbHashValue'),
            # [IN] Count of bytes in the Hash Blob.
            (ULONG, 'cbHashValue'),
            # [IN] Flags.
            (DWORD, 'dwAssemblyRefFlags'),
            # [OUT] Returned AssemblyRef token.
            (POINTER(mdAssemblyRef), 'pmdar')
        ),
        STDMETHOD('DefineFile')(
            # [IN] Name of the file.
            (LPCWSTR, 'szName'),
            # [IN] Hash Blob.
            (POINTER(VOID), 'pbHashValue'),
            # [IN] Count of bytes in the Hash Blob.
            (ULONG, 'cbHashValue'),
            # [IN] Flags.
            (DWORD, 'dwFileFlags'),
            # [OUT] Returned File token.
            (POINTER(mdFile), 'pmdf')
        ),
        STDMETHOD('DefineExportedType')(
            # [IN] Name of the Com Type.
            (LPCWSTR, 'szName'),
            # [IN] mdFile or mdAssemblyRef or mdExportedType
            (mdToken, 'tkImplementation'),
            # [IN] TypeDef token within the file.
            (mdTypeDef, 'tkTypeDef'),
            # [IN] Flags.
            (DWORD, 'dwExportedTypeFlags'),
            # [OUT] Returned ExportedType token.
            (POINTER(mdExportedType), 'pmdct')
        ),
        STDMETHOD('DefineManifestResource')(
            # [IN] Name of the resource.
            (LPCWSTR, 'szName'),
            # [IN] mdFile or mdAssemblyRef that provides the resource.
            (mdToken, 'tkImplementation'),
            # [IN] Offset to the beginning of the resource within the file.
            (DWORD, 'dwOffset'),
            # [IN] Flags.
            (DWORD, 'dwResourceFlags'),
            # [OUT] Returned ManifestResource token.
            (POINTER(mdManifestResource), 'pmdmr')
        ),
        STDMETHOD('SetAssemblyProps')(
            # [IN] Assembly token.
            (mdAssembly, 'pma'),
            # [IN] Public key of the assembly.
            (POINTER(VOID), 'pbPublicKey'),
            # [IN] Count of bytes in the public key.
            (ULONG, 'cbPublicKey'),
            # [IN] Hash algorithm used to hash the files.
            (ULONG, 'ulHashAlgId'),
            # [IN] Name of the assembly.
            (LPCWSTR, 'szName'),
            # [IN] Assembly MetaData.
            (POINTER(ASSEMBLYMETADATA), 'pMetaData'),
            # [IN] Flags.
            (DWORD, 'dwAssemblyFlags')
        ),
        STDMETHOD('SetAssemblyRefProps')(
            # [IN] AssemblyRefToken.
            (mdAssemblyRef, 'ar'),
            # [IN] Public key or token of the assembly.
            (POINTER(VOID), 'pbPublicKeyOrToken'),
            # [IN] Count of bytes in the public key or token.
            (ULONG, 'cbPublicKeyOrToken'),
            # [IN] Name of the assembly being referenced.
            (LPCWSTR, 'szName'),
            # [IN] Assembly MetaData.
            (POINTER(ASSEMBLYMETADATA), 'pMetaData'),
            # [IN] Hash Blob.
            (POINTER(VOID), 'pbHashValue'),
            # [IN] Count of bytes in the Hash Blob.
            (ULONG, 'cbHashValue'),
            # [IN] Token for Execution Location.
            (DWORD, 'dwAssemblyRefFlags')
        ),
        STDMETHOD('SetFileProps')(
            # [IN] File token.
            (mdFile, 'file'),
            # [IN] Hash Blob.
            (POINTER(VOID), 'pbHashValue'),
            # [IN] Count of bytes in the Hash Blob.
            (ULONG, 'cbHashValue'),
            # [IN] Flags.
            (DWORD, 'dwFileFlags')
        ),
        STDMETHOD('SetExportedTypeProps')(
            # [IN] ExportedType token.
            (mdExportedType, 'ct'),
            # [IN] mdFile or mdAssemblyRef or mdExportedType.
            (mdToken, 'tkImplementation'),
            # [IN] TypeDef token within the file.
            (mdTypeDef, 'tkTypeDef'),
            # [IN] Flags.
            (DWORD, 'dwExportedTypeFlags')
        ),
        STDMETHOD('SetManifestResourceProps')(
            # [IN] ManifestResource token.
            (mdManifestResource, 'mr'),
            # [IN] mdFile or mdAssemblyRef that provides the resource.
            (mdToken, 'tkImplementation'),
            # [IN] Offset to the beginning of the resource within the file.
            (DWORD, 'dwOffset'),
            # [IN] Flags.
            (DWORD, 'dwResourceFlags')
        ),
        # IMetaDataAssemblyEmi
    )
    # {EE62470B-E94B-424e-9B7C-2F00C9249F93}
    IID_IMetaDataAssemblyImport = EXTERN_GUID(
        0xEE62470B,
        0xE94B,
        0x424E,
        0x9B,
        0x7C,
        0x2F,
        0x0,
        0xC9,
        0x24,
        0x9F,
        0x93
    )
    # ---
    IMetaDataAssemblyImport._iid_ = IID_IMetaDataAssemblyImport
    DECLARE_INTERFACE_(IMetaDataAssemblyImport, comtypes.IUnknown)(
        STDMETHOD('GetAssemblyProps')(
            # [IN] The Assembly for which to get the properties.
            (mdAssembly, 'mda'),
            # [OUT] Pointer to the public key.
            (POINTER(POINTER(VOID)), 'ppbPublicKey'),
            # [OUT] Count of bytes in the public key.
            (POINTER(ULONG), 'pcbPublicKey'),
            # [OUT] Hash Algorithm.
            (POINTER(ULONG), 'pulHashAlgId'),
            # [OUT] Buffer to fill with assembly's simply name.
            (ULONG, 'cchName'),
            # [IN] Size of buffer in wide chars.
            (POINTER(ULONG), 'pchName'),
            # [OUT] Actual of wide chars in name.
            (POINTER(ASSEMBLYMETADATA), 'pMetaData'),
            # [OUT] Assembly MetaData.
            (POINTER(DWORD), 'pdwAssemblyFlags')
        ),
        STDMETHOD('GetAssemblyRefProps')(
            # [IN] The AssemblyRef for which to get the properties.
            (mdAssemblyRef, 'mdar'),
            # [OUT] Pointer to the public key or token.
            (POINTER(POINTER(VOID)), 'ppbPublicKeyOrToken'),
            # [OUT] Count of bytes in the public key or token.
            (POINTER(ULONG), 'pcbPublicKeyOrToken'),
            # [OUT] Buffer to fill with name.
            (ULONG, 'cchName'),
            # [IN] Size of buffer in wide chars.
            (POINTER(ULONG), 'pchName'),
            # [OUT] Actual of wide chars in name.
            (POINTER(ASSEMBLYMETADATA), 'pMetaData'),
            # [OUT] Assembly MetaData.
            (POINTER(POINTER(VOID)), 'ppbHashValue'),
            # [OUT] Hash blob.
            (POINTER(ULONG), 'pcbHashValue'),
            # [OUT] Count of bytes in the hash blob.
            (POINTER(DWORD), 'pdwAssemblyRefFlags')
        ),
        STDMETHOD('GetFileProps')(
            # [IN] The File for which to get the properties.
            (mdFile, 'mdf'),
            # [OUT] Buffer to fill with name.
            (ULONG, 'cchName'),
            # [IN] Size of buffer in wide chars.
            (POINTER(ULONG), 'pchName'),
            # [OUT] Actual of wide chars in name.
            (POINTER(POINTER(VOID)), 'ppbHashValue'),
            # [OUT] Pointer to the Hash Value Blob.
            (POINTER(ULONG), 'pcbHashValue'),
            # [OUT] Count of bytes in the Hash Value Blob.
            (POINTER(DWORD), 'pdwFileFlags')
        ),
        STDMETHOD('GetExportedTypeProps')(
            # [IN] The ExportedType for which to get the properties.
            (mdExportedType, 'mdct'),
            # [OUT] Buffer to fill with name.
            (ULONG, 'cchName'),
            # [IN] Size of buffer in wide chars.
            (POINTER(ULONG), 'pchName'),
            # [OUT] Actual of wide chars in name.
            (POINTER(mdToken), 'ptkImplementation'),
            # [OUT] mdFile or mdAssemblyRef or mdExportedType.
            (POINTER(mdTypeDef), 'ptkTypeDef'),
            # [OUT] TypeDef token within the file.
            (POINTER(DWORD), 'pdwExportedTypeFlags')
        ),
        STDMETHOD('GetManifestResourceProps')(
            # [IN] The ManifestResource for which to get the properties.
            (mdManifestResource, 'mdmr'),
            # [OUT] Buffer to fill with name.
            (ULONG, 'cchName'),
            # [IN] Size of buffer in wide chars.
            (POINTER(ULONG), 'pchName'),
            # [OUT] Actual of wide chars in name.
            (POINTER(mdToken), 'ptkImplementation'),
            # [OUT] mdFile or mdAssemblyRef that provides the ManifestResource.
            (POINTER(DWORD), 'pdwOffset'),
            # [OUT] Offset to the beginning of the resource within the file.
            (POINTER(DWORD), 'pdwResourceFlags')
        ),
        STDMETHOD('EnumAssemblyRefs')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [OUT] Put AssemblyRefs here.
            (mdAssemblyRef * 0, 'rAssemblyRefs'),
            # [IN] Max AssemblyRefs to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumFiles')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [OUT] Put Files here.
            (mdFile * 0, 'rFiles'),
            # [IN] Max Files to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumExportedTypes')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [OUT] Put ExportedTypes here.
            (mdExportedType * 0, 'rExportedTypes'),
            # [IN] Max ExportedTypes to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('EnumManifestResources')(
            # [IN | OUT] Pointer to the enum.
            (POINTER(HCORENUM), 'phEnum'),
            # [OUT] Put ManifestResources here.
            (mdManifestResource * 0, 'rManifestResources'),
            # [IN] Max Resources to put.
            (ULONG, 'cMax'),
            # [OUT] Put put here.
            (POINTER(ULONG), 'pcTokens')
        ),
        STDMETHOD('GetAssemblyFromScope')(
            # [OUT] Put token here.
            (POINTER(mdAssembly), 'ptkAssembly')
        ),
        STDMETHOD('FindExportedTypeByName')(
            # [IN] Name of the ExportedType.
            (LPCWSTR, 'szName'),
            # [IN] ExportedType for the enclosing class.
            (mdToken, 'mdtExportedType'),
            # [OUT] Put the ExportedType token here.
            (POINTER(mdExportedType), 'ptkExportedType')
        ),
        STDMETHOD('FindManifestResourceByName')(
            # [IN] Name of the ManifestResource.
            (LPCWSTR, 'szName'),
            # [OUT] Put the ManifestResource token here.
            (POINTER(mdManifestResource), 'ptkManifestResource')
        ),
        STDMETHOD('VOID, CloseEnum')(
            # Enum to be closed.
            (HCORENUM, 'hEnum')
        ),
        STDMETHOD('FindAssembliesByName')(
            # [IN] optional - can be NULL
            (LPCWSTR, 'szAppBase'),
            # [IN] optional - can be NULL
            (LPCWSTR, 'szPrivateBin'),
            # [IN] required - this is the assembly you are requesting
            (LPCWSTR, 'szAssemblyName'),
            # [OUT] put IMetaDataAssemblyImport pointers here
            (POINTER(comtypes.IUnknown * 0), ''),
            # [IN] The max number to put
            (ppIUnkULONG, 'cMax'),
            # [OUT] The number of assemblies returned.
            (POINTER(ULONG), 'pcAssemblies')
        ),
        # IMetaDataAssemblyImpor
    )

    # **********************************************************************
    # End Assembly Declarations
    # **********************************************************************
    # **********************************************************************
    # MetaData Validator Declarations
    # **********************************************************************
    # Specifies the type of the module, PE file vs. .obj file.
    class CorValidatorModuleType(ENUM):
        ValidatorModuleTypeInvalid = 0x0
        ValidatorModuleTypeMin = 0x00000001
        ValidatorModuleTypePE = 0x00000001
        ValidatorModuleTypeObj = 0x00000002
        ValidatorModuleTypeEnc = 0x00000003
        ValidatorModuleTypeIncr = 0x00000004
        ValidatorModuleTypeMax = 0x00000004

    ValidatorModuleTypeInvalid = (
        CorValidatorModuleType.ValidatorModuleTypeInvalid
    )
    ValidatorModuleTypeMin = CorValidatorModuleType.ValidatorModuleTypeMin
    ValidatorModuleTypePE = CorValidatorModuleType.ValidatorModuleTypePE
    ValidatorModuleTypeObj = CorValidatorModuleType.ValidatorModuleTypeObj
    ValidatorModuleTypeEnc = CorValidatorModuleType.ValidatorModuleTypeEnc
    ValidatorModuleTypeIncr = CorValidatorModuleType.ValidatorModuleTypeIncr
    ValidatorModuleTypeMax = CorValidatorModuleType.ValidatorModuleTypeMax

    # {4709C9C6-81FF-11D3-9FC7-00C04F79A0A3}
    IID_IMetaDataValidate = EXTERN_GUID(
        0x4709C9C6,
        0x81FF,
        0x11D3,
        0x9F,
        0xC7,
        0x0,
        0xC0,
        0x4F,
        0x79,
        0xA0,
        0xA3
    )

    # ---
    IMetaDataValidate = INTERFACE('IMetaDataValidate')
    IMetaDataValidate._iid_ = IID_IMetaDataValidate
    DECLARE_INTERFACE_(IMetaDataValidate, comtypes.IUnknown)(
        STDMETHOD('ValidatorInit')(
            # [IN] Specifies the type of the module.
            (DWORD, 'dwModuleType'),
            # [IN] Validation error handler.
            (POINTER(comtypes.IUnknown), 'pUnk')
        ),
        STDMETHOD('ValidateMetaData')(
        ),
        # IMetaDataValidat
    )

    # **********************************************************************
    # End MetaData Validator Declarations
    # **********************************************************************
    # **********************************************************************
    # IMetaDataDispenserEx declarations.
    # **********************************************************************
    # {31BCFCE2-DAFB-11D2-9F81-00C04F79A0A3}
    IID_IMetaDataDispenserEx = EXTERN_GUID(
        0x31BCFCE2,
        0xDAFB,
        0x11D2,
        0x9F,
        0x81,
        0x0,
        0xC0,
        0x4F,
        0x79,
        0xA0,
        0xA3
    )
    IMetaDataDispenserEx = INTERFACE('IMetaDataDispenserEx')
    IMetaDataDispenserEx._iid_ = IID_IMetaDataDispenserEx
    DECLARE_INTERFACE_(IMetaDataDispenserEx, IMetaDataDispenser)(
        STDMETHOD('SetOption')(
            # [in] GUID for the option to be set.
            (REFGUID, 'optionid'),
            # [in] Value to which the option is to be set.
            (POINTER(VARIANT), 'value')
        ),
        STDMETHOD('GetOption')(
            # [in] GUID for the option to be set.
            (REFGUID, 'optionid'),
            # [out] Value to which the option is currently set.
            (POINTER(VARIANT), 'pvalue')
        ),
        STDMETHOD('OpenScopeOnITypeInfo')(
            # [in] ITypeInfo to open.
            (POINTER(ITypeInfo), 'pITI'),
            # [in] Open mode flags.
            (DWORD, 'dwOpenFlags'),
            # [in] The interface desired.
            (REFIID, 'riid'),
            # [out] Return interface on success.
            (POINTER(POINTER(comtypes.IUnknown)), 'ppIUnk')
        ),
        STDMETHOD('GetCORSystemDirectory')(
            (LPWSTR, 'szBuffer'),
            # [out] Buffer for the directory name
            (DWORD, 'cchBuffer'),
            # [in] Size of the buffer
            (POINTER(DWORD), 'pchBuffer')
        ),
        STDMETHOD('FindAssembly')(
            # [IN] optional - can be NULL
            (LPCWSTR, 'szAppBase'),
            # [IN] optional - can be NULL
            (LPCWSTR, 'szPrivateBin'),
            # [IN] optional - can be NULL
            (LPCWSTR, 'szGlobalBin'),
            # [IN] required - this is the assembly you are requesting
            (LPCWSTR, 'szAssemblyName'),
            # [OUT] buffer - to hold name
            (LPCWSTR, 'szName'),
            # [IN] the name buffer's size
            (ULONG, 'cchName'),
            # [OUT] the number of characters returend in the buffer
            (POINTER(ULONG), 'pcName')
        ),
        STDMETHOD('FindAssemblyModule')(
            # [IN] optional - can be NULL
            (LPCWSTR, 'szAppBase'),
            # [IN] optional - can be NULL
            (LPCWSTR, 'szPrivateBin'),
            # [IN] optional - can be NULL
            (LPCWSTR, 'szGlobalBin'),
            # [IN] required - this is the assembly you are requesting
            (LPCWSTR, 'szAssemblyName'),
            # [IN] required - the name of the module
            (LPCWSTR, 'szModuleName'),
            (LPWSTR, 'szName'),
            # [OUT] buffer - to hold name
            (ULONG, 'cchName'),
            # [IN] the name buffer's size
            (POINTER(ULONG), 'pcName')
        )
    )

    # **********************************************************************
    # **********************************************************************
    # Registration declarations. Will be replace by Services' Registration
    # implementation.
    # **********************************************************************
    # **********************************************************************
    # Various flags for use in installing a module or a composite
    class CorRegFlags(ENUM):
        regNoCopy = 0x00000001
        regConfig = 0x00000002
        regHasRefs = 0x00000004

    regNoCopy = CorRegFlags.regNoCopy
    regConfig = CorRegFlags.regConfig
    regHasRefs = CorRegFlags.regHasRefs
    CVID = GUID

    CVStruct._fields_ = [
        ('Major', SHORT),
        ('Minor', SHORT),
        ('Sub', SHORT),
        ('Build', SHORT),
    ]

    # **********************************************************************
    # **********************************************************************
    # CeeGen interfaces for generating in-memory Common Language Runtime files
    # **********************************************************************
    # **********************************************************************
    HCEESECTION = POINTER(VOID)


    class CeeSectionAttr(ENUM):
        sdNone = 0
        sdReadOnly = IMAGE_SCN_MEM_READ | IMAGE_SCN_CNT_INITIALIZED_DATA
        sdReadWrite = sdReadOnly | IMAGE_SCN_MEM_WRITE
        sdExecute = (
            IMAGE_SCN_MEM_READ |
            IMAGE_SCN_CNT_CODE |
            IMAGE_SCN_MEM_EXECUTE
        )

    sdNone = CeeSectionAttr.sdNone
    sdReadOnly = CeeSectionAttr.sdReadOnly
    sdReadWrite = CeeSectionAttr.sdReadWrite
    sdExecute = CeeSectionAttr.sdExecute

    # Relocation types.
    class CeeSectionRelocType(ENUM):
        srRelocAbsolute = 1
        srRelocHighLow = 3
        srRelocHighAdj = 4
        srRelocMapToken = 5
        srRelocRelative = 6
        srRelocFilePos = 7
        srRelocCodeRelative = 8
        srRelocIA64Imm64 = 9
        srRelocDir64 = 10
        srRelocIA64PcRel25 = 11
        srRelocIA64PcRel64 = 12
        srRelocAbsoluteTagged = 13
        srRelocSentinel = 14
        srNoBaseReloc = 0x4000
        srRelocPtr = 0x8000
        srRelocAbsolutePtr = srRelocPtr + srRelocAbsolute
        srRelocHighLowPtr = srRelocPtr + srRelocHighLow
        srRelocRelativePtr = srRelocPtr + srRelocRelative
        srRelocIA64Imm64Ptr = srRelocPtr + srRelocIA64Imm64
        srRelocDir64Ptr = srRelocPtr + srRelocDir64

    srRelocAbsolute = CeeSectionRelocType.srRelocAbsolute
    srRelocHighLow = CeeSectionRelocType.srRelocHighLow
    srRelocHighAdj = CeeSectionRelocType.srRelocHighAdj
    srRelocMapToken = CeeSectionRelocType.srRelocMapToken
    srRelocRelative = CeeSectionRelocType.srRelocRelative
    srRelocFilePos = CeeSectionRelocType.srRelocFilePos
    srRelocCodeRelative = CeeSectionRelocType.srRelocCodeRelative
    srRelocIA64Imm64 = CeeSectionRelocType.srRelocIA64Imm64
    srRelocDir64 = CeeSectionRelocType.srRelocDir64
    srRelocIA64PcRel25 = CeeSectionRelocType.srRelocIA64PcRel25
    srRelocIA64PcRel64 = CeeSectionRelocType.srRelocIA64PcRel64
    srRelocAbsoluteTagged = CeeSectionRelocType.srRelocAbsoluteTagged
    srRelocSentinel = CeeSectionRelocType.srRelocSentinel
    srNoBaseReloc = CeeSectionRelocType.srNoBaseReloc
    srRelocPtr = CeeSectionRelocType.srRelocPtr
    srRelocAbsolutePtr = CeeSectionRelocType.srRelocAbsolutePtr
    srRelocHighLowPtr = CeeSectionRelocType.srRelocHighLowPtr
    srRelocRelativePtr = CeeSectionRelocType.srRelocRelativePtr
    srRelocIA64Imm64Ptr = CeeSectionRelocType.srRelocIA64Imm64Ptr
    srRelocDir64Ptr = CeeSectionRelocType.srRelocDir64Ptr
    IMAGE_REL_BASED_REL32 = 7
    IMAGE_REL_BASED_IA64_PCREL21 = 11
    IMAGE_REL_BASED_IA64_PCREL60 = 12

    CeeSectionRelocExtra._fields_ = [
        ('highAdj', USHORT),
    ]

    # -------------------------------------
    # --- ICeeGen
    # -------------------------------------
    # {7ED1BDFF-8E36-11d2-9C56-00A0C9B7CC45}
    IID_ICeeGen = EXTERN_GUID(
        0x7ED1BDFF,
        0x8E36,
        0x11D2,
        0x9C,
        0x56,
        0x0,
        0xA0,
        0xC9,
        0xB7,
        0xCC,
        0x45
    )
    ICeeGen._iid_ = IID_ICeeGen
    DECLARE_INTERFACE_(ICeeGen, comtypes.IUnknown)(
        STDMETHOD('EmitString')(
            (LPWSTR, 'lpString'),
            # [IN] String to emit
            (POINTER(ULONG), 'RVA')
        ),
        STDMETHOD('GetString')(
            # [IN] RVA for string to return
            (ULONG, 'RVA'),
            (POINTER(LPWSTR), 'lpString')
        ),
        STDMETHOD('AllocateMethodBuffer')(
            # [IN] Length of buffer to create
            (ULONG, 'cchBuffer'),
            # [OUT] Returned buffer
            (POINTER(POINTER(UCHAR)), 'lpBuffer'),
            # [OUT] RVA for method
            (POINTER(ULONG), 'RVA')
        ),
        STDMETHOD('GetMethodBuffer')(
            # [IN] RVA for method to return
            (ULONG, 'RVA'),
            # [OUT] Returned buffer
            (POINTER(POINTER(UCHAR)), 'lpBuffer')
        ),
        STDMETHOD('GetIMapTokenIface')(
            (POINTER(POINTER(comtypes.IUnknown)), 'pIMapToken')
        ),
        STDMETHOD('GenerateCeeFile')(
        ),
        STDMETHOD('GetIlSection')(
            (POINTER(HCEESECTION), 'section')
        ),
        STDMETHOD('GetStringSection')(
            (POINTER(HCEESECTION), 'section')
        ),
        STDMETHOD('AddSectionReloc')(
            (HCEESECTION, 'section'),
            (ULONG, 'offset'),
            (HCEESECTION, 'relativeTo'),
            (CeeSectionRelocType, 'relocType')
        ),
        # use these only if you have special section requirements not handled
        # by other APIs
        STDMETHOD('GetSectionCreate')(
            (POINTER(CHAR), 'name'),
            (DWORD, 'flags'),
            (POINTER(HCEESECTION), 'section')
        ),
        STDMETHOD('GetSectionDataLen')(
            (HCEESECTION, 'section'),
            (POINTER(ULONG), 'dataLen')
        ),
        STDMETHOD('GetSectionBlock')(
            (HCEESECTION, 'section'),
            (ULONG, 'len'),
            (ULONG, 'align=1'),
            (POINTER(POINTER(VOID)), 'ppBytes=0')
        ),
        STDMETHOD('TruncateSection')(
            (HCEESECTION, 'section'),
            (ULONG, 'len')
        ),
        STDMETHOD('GenerateCeeMemoryImage')(
            (POINTER(POINTER(VOID)), 'ppImage')
        ),
        STDMETHOD('ComputePointer')(
            (HCEESECTION, 'section'),
            # [IN] RVA for method to return
            (ULONG, 'RVA'),
            # [OUT] Returned buffer
            (POINTER(POINTER(UCHAR)), 'lpBuffer')
        )
    )

    # **********************************************************************
    # **********************************************************************
    # End of CeeGen declarations.
    # **********************************************************************
    # **********************************************************************
    # **********************************************************************
    # CorModule interfaces for generating in-memory modules
    # **********************************************************************
    # **********************************************************************
    class ICorModuleInitializeFlags(ENUM):
        CORMODULE_MATCH = 0x00
        CORMODULE_NEW = 0x01

    CORMODULE_MATCH = ICorModuleInitializeFlags.CORMODULE_MATCH
    CORMODULE_NEW = ICorModuleInitializeFlags.CORMODULE_NEW

    # -------------------------------------
    # --- ICorModule
    # -------------------------------------
    # {2629F8E1-95E5-11d2-9C56-00A0C9B7CC45}
    IID_ICorModule = EXTERN_GUID(
        0x2629F8E1,
        0x95E5,
        0x11D2,
        0x9C,
        0x56,
        0x0,
        0xA0,
        0xC9,
        0xB7,
        0xCC,
        0x45
    )
    ICorModule._iid_ = IID_ICorModule
    DECLARE_INTERFACE_(ICorModule, comtypes.IUnknown)(
        STDMETHOD('Initialize')(
            # [IN] flags to control emitter returned
            (DWORD, 'flags'),
            # [IN] type of cee generator to initialize with
            (REFIID, 'riidCeeGen'),
            # [IN] type of emitter to initialize with
            (REFIID, 'riidEmitter')
        ),
        STDMETHOD('GetCeeGen')(
            # [OUT] cee generator
            (POINTER(POINTER(ICeeGen)), 'pCeeGen')
        ),
        STDMETHOD('GetMetaDataEmit')(
            # [OUT] emitter
            (POINTER(POINTER(IMetaDataEmit)), 'pEmitter')
        )
    )

    # **********************************************************************
    # **********************************************************************
    # End of CorModule declarations.
    # **********************************************************************
    # *********************************************************************
    # *********************************************************************
    # --- IMetaDataTables
    # -------------------------------------
    # This API isn't big endian friendly since it indexes directly into the
    # memory that
    # is stored in little endian format.
    # {D8F579AB-402D-4b8e-82D9-5D63B1065C68}
    IID_IMetaDataTables = EXTERN_GUID(
        0xD8F579AB,
        0x402D,
        0x4B8E,
        0x82,
        0xD9,
        0x5D,
        0x63,
        0xB1,
        0x6,
        0x5C,
        0x68
    )
    IMetaDataTables._iid_ = IID_IMetaDataTables
    DECLARE_INTERFACE_(IMetaDataTables, comtypes.IUnknown)(
        STDMETHOD('GetStringHeapSize')(
            # [OUT] Size of the string heap.
            (POINTER(ULONG), 'pcbStrings')
        ),
        STDMETHOD('GetBlobHeapSize')(
            # [OUT] Size of the Blob heap.
            (POINTER(ULONG), 'pcbBlobs')
        ),
        STDMETHOD('GetGuidHeapSize')(
            # [OUT] Size of the Guid heap.
            (POINTER(ULONG), 'pcbGuids')
        ),
        STDMETHOD('GetUserStringHeapSize')(
            # [OUT] Size of the User String heap.
            (POINTER(ULONG), 'pcbBlobs')
        ),
        STDMETHOD('GetNumTables')(
            # [OUT] Count of tables.
            (POINTER(ULONG), 'pcTables')
        ),
        STDMETHOD('GetTableIndex')(
            # [IN] Token for which to get table index.
            (ULONG, 'token'),
            # [OUT] Put table index here.
            (POINTER(ULONG), 'pixTbl')
        ),
        STDMETHOD('GetTableInfo')(
            # [IN] Which table.
            (ULONG, 'ixTbl'),
            # [OUT] Size of a row, bytes.
            (POINTER(ULONG), 'pcbRow'),
            # [OUT] Number of rows.
            (POINTER(ULONG), 'pcRows'),
            # [OUT] Number of columns in each row.
            (POINTER(ULONG), 'pcCols'),
            # [OUT] Key column, or -1 if none.
            (POINTER(ULONG), 'piKey'),
            # [OUT] Name of the table.
            (POINTER(POINTER(CHAR)), 'ppName')
        ),
        STDMETHOD('GetColumnInfo')(
            # [IN] Which Table
            (ULONG, 'ixTbl'),
            # [IN] Which Column in the table
            (ULONG, 'ixCol'),
            # [OUT] Offset of the column in the row.
            (POINTER(ULONG), 'poCol'),
            # [OUT] Size of a column, bytes.
            (POINTER(ULONG), 'pcbCol'),
            # [OUT] Type of the column.
            (POINTER(ULONG), 'pType'),
            # [OUT] Name of the Column.
            (POINTER(POINTER(CHAR)), 'ppName')
        ),
        STDMETHOD('GetCodedTokenInfo')(
            # [IN] Which kind of coded token.
            (ULONG, 'ixCdTkn'),
            # [OUT] Count of tokens.
            (POINTER(ULONG), 'pcTokens'),
            # [OUT] List of tokens.
            (POINTER(POINTER(ULONG)), 'ppTokens'),
            # [OUT] Name of the CodedToken.
            (POINTER(POINTER(CHAR)), 'ppName')
        ),
        STDMETHOD('GetRow')(
            # [IN] Which table.
            (ULONG, 'ixTbl'),
            # [IN] Which row.
            (ULONG, 'rid'),
            # [OUT] Put pointer to row here.
            (POINTER(POINTER(VOID)), 'ppRow')
        ),
        STDMETHOD('GetColumn')(
            # [IN] Which table.
            (ULONG, 'ixTbl'),
            # [IN] Which column.
            (ULONG, 'ixCol'),
            # [IN] Which row.
            (ULONG, 'rid'),
            # [OUT] Put the column contents here.
            (POINTER(ULONG), 'pVal')
        ),
        STDMETHOD('GetString')(
            # [IN] Value from a string column.
            (ULONG, 'ixString'),
            # [OUT] Put a pointer to the string here.
            (POINTER(POINTER(CHAR)), 'ppString')
        ),
        STDMETHOD('GetBlob')(
            # [IN] Value from a blob column.
            (ULONG, 'ixBlob'),
            # [OUT] Put size of the blob here.
            (POINTER(ULONG), 'pcbData'),
            # [OUT] Put a pointer to the blob here.
            (POINTER(POINTER(VOID)), 'ppData')
        ),
        STDMETHOD('GetGuid')(
            # [IN] Value from a guid column.
            (ULONG, 'ixGuid'),
            # [OUT] Put a pointer to the GUID here.
            (POINTER(POINTER(GUID)), 'ppGUID')
        ),
        STDMETHOD('GetUserString')(
            # [IN] Value from a UserString column.
            (ULONG, 'ixUserString'),
            # [OUT] Put size of the UserString here.
            (POINTER(ULONG), 'pcbData'),
            # [OUT] Put a pointer to the UserString here.
            (POINTER(POINTER(VOID)), 'ppData')
        ),
        STDMETHOD('GetNextString')(
            # [IN] Value from a string column.
            (ULONG, 'ixString'),
            # [OUT] Put the index of the next string here.
            (POINTER(ULONG), 'pNext')
        ),
        STDMETHOD('GetNextBlob')(
            # [IN] Value from a blob column.
            (ULONG, 'ixBlob'),
            # [OUT] Put the index of the netxt blob here.
            (POINTER(ULONG), 'pNext')
        ),
        STDMETHOD('GetNextGuid')(
            # [IN] Value from a guid column.
            (ULONG, 'ixGuid'),
            # [OUT] Put the index of the next guid here.
            (POINTER(ULONG), 'pNext')
        ),
        STDMETHOD('GetNextUserString')(
            # [IN] Value from a UserString column.
            (ULONG, 'ixUserString'),
            # [OUT] Put the index of the next user string here.
            (POINTER(ULONG), 'pNext')
        ),
        # Interface is sealed
    )

    # This API isn't big endian friendly since it indexes directly into the
    # memory that
    # is stored in little endian format.
    # {BADB5F70-58DA-43a9-A1C6-D74819F19B15}
    IID_IMetaDataTables2 = EXTERN_GUID(
        0xBADB5F70,
        0x58DA,
        0x43A9,
        0xA1,
        0xC6,
        0xD7,
        0x48,
        0x19,
        0xF1,
        0x9B,
        0x15
    )
    IMetaDataTables2._iid_ = IID_IMetaDataTables2
    DECLARE_INTERFACE_(IMetaDataTables2, IMetaDataTables)(
        STDMETHOD('GetMetaDataStorage')(
            # [OUT] put pointer to MD section here (aka, 'BSJB').
            (POINTER(POINTER(VOID)), 'ppvMd'),
            # [OUT] put size of the stream here.
            (POINTER(ULONG), 'pcbMd')
        ),
        STDMETHOD('GetMetaDataStreamInfo')(
            # [IN] Stream ordinal desired.
            (ULONG, 'ix'),
            # [OUT] put pointer to stream name here.
            (POINTER(POINTER(CHAR)), 'ppchName'),
            # [OUT] put pointer to MD stream here.
            (POINTER(POINTER(VOID)), 'ppv'),
            # [OUT] put size of the stream here.
            (POINTER(ULONG), 'pcb')
        ),
        # IMetaDataTables
    )

    if defined(_DEFINE_META_DATA_META_CONSTANTS):
        if not defined(_META_DATA_META_CONSTANTS_DEFINED):
            _META_DATA_META_CONSTANTS_DEFINED = VOID
            iRidMax = 63
            iCodedToken = 64  # base of coded tokens.
            iCodedTokenMax = 95
            iSHORT = 96  # fixed types.
            iUSHORT = 97
            iLONG = 98
            iULONG = 99
            iBYTE = 100
            iSTRING = 101  # pool types.
            iGUID = 102
            iBLOB = 103


            def IsRidType(ix):
                return ix <= iRidMax


            def IsCodedTokenType(ix):
                return (ix >= iCodedToken) and (ix <= iCodedTokenMax)


            def IsRidOrToken(ix):
                return ix <= iCodedTokenMax


            def IsHeapType(ix):
                return ix >= iSTRING


            def IsFixedType(ix):
                return (ix < iSTRING) and (ix > iCodedTokenMax)

        # END IF
    # END IF

    # *************************************************************************
    # End of IMetaDataTables.
    # *************************************************************************
    # Gets the dependancies of a native image. If these change
    # the native image cannot be used.
    #
    # IMetaDataImport::GetAssemblyRefProps() can be used to obtain information
    # about the mdAssemblyRefs.
    # *************************************************************************

    # {814C9E35-3F3F-4975-977A-371F0A878AC7}
    IID_INativeImageDependency = EXTERN_GUID(
        0x814C9E35,
        0x3F3F,
        0x4975,
        0x97,
        0x7A,
        0x37,
        0x1F,
        0xA,
        0x87,
        0x8A,
        0xC7
    )


    class CORCOMPILE_ASSEMBLY_SIGNATURE(ctypes.Structure):
        pass


    CORCOMPILE_NGEN_SIGNATURE = GUID
    INativeImageDependency._iid_ = IID_INativeImageDependency
    DECLARE_INTERFACE_(INativeImageDependency, comtypes.IUnknown)(
        # Get the referenced assembly
        STDMETHOD('GetILAssemblyRef')(
            # [OUT]
            (POINTER(mdAssemblyRef), 'pAssemblyRef')
        ),
        # Get the post-policy assembly actually used
        STDMETHOD('GetILAssemblyDef')(
            # [OUT]
            (POINTER(mdAssemblyRef), 'ppAssemblyDef'),
            # [OUT]
            (POINTER(CORCOMPILE_ASSEMBLY_SIGNATURE), 'pSign')
        ),
        # Get the native image corresponding to GetILAssemblyDef() IF
        # there is a hard-bound (directly-referenced) native dependancy
        # We do not need the configStrig because configStrings have to
        # be an exact part. Any partial matches are factored out into
        # GetConfigMask()
        STDMETHOD('GetNativeAssemblyDef')(
            # [OUT] INVALID_NGEN_SIGNATURE if there is no hard-bound
            # dependancy
            (POINTER(CORCOMPILE_NGEN_SIGNATURE), 'pNativeSign')
        )
    )
    # **************************************************************
    # Fusion uses IFusionNativeImageInfo to obtain (and cache)
    # informaton
    # about a native image being installed into the native image cache.
    # This allows Fusion to bind directly to native images
    # without requiring (expensively) binding to the IL assembly first.
    # IMetaDataAssemblyImport can be queried for this interface
    # **************************************************************
    # {0EA273D0-B4DA-4008-A60D-8D6EFFDD6E91}
    IID_INativeImageInstallInfo = EXTERN_GUID(
        0xEA273D0,
        0xB4DA,
        0x4008,
        0xA6,
        0xD,
        0x8D,
        0x6E,
        0xFF,
        0xDD,
        0x6E,
        0x91
    )
    INativeImageInstallInfo._iid_ = IID_INativeImageInstallInfo
    DECLARE_INTERFACE_(INativeImageInstallInfo, comtypes.IUnknown)(
        # Signature of the ngen image
        # This matches the argument type of
        # INativeImageDependency::GetNativeAssemblyDef
        STDMETHOD('GetSignature')(
            # [OUT]
            (POINTER(CORCOMPILE_NGEN_SIGNATURE), 'pNgenSign')
        ),
        # Signature of the source IL assembly. This can be used to
        # verify that the IL image matches a candidate ngen image.
        # This matches the argument type of
        # IAssemblyRuntimeSignature::CheckSignature
        STDMETHOD('GetILSignature')(
            # [OUT]
            (POINTER(CORCOMPILE_ASSEMBLY_SIGNATURE), 'pILSign')
        ),
        # Returns the equivalent of
        # ISNAssemblySignature::GetSNAssemblySignature,
        # except for UINT assemblies where the GetSNAssemblySignature will
        # fail.
        # This can be used for matching the IL assembly in the GAC when the
        # native-image is generated/installed.
        # Sets *pcbSig and returns ERROR_INSUFFICIENT_BUFFER for
        # insufficient buffer.
        # Returns CORSEC_E_MISSING_STRONGNAME if the IL assembly is not
        # strongly-named
        STDMETHOD('GetILStrongSignature')(
            # [IN, OUT] Buffer to write signature
            (POINTER(BYTE), 'pbSig'),
            # [IN, OUT] Size of buffer, bytes written
            (POINTER(DWORD), 'pcbSig')
        ),
        # Information about the contents/dependancies/assumptions of
        # NativeImage
        # All of this information has to match for the current NativeImage
        # to
        # be valid
        # Sets *pdwLength and returns ERROR_INSUFFICIENT_BUFFER for
        # insufficient szConfigString
        STDMETHOD('GetConfigString')(
            # [OUT]
            (LPWSTR, 'szConfigString'),
            # [IN|OUT] - Number of WCHARs written including terminating NULL
            (POINTER(DWORD), 'pdwLength')
        ),
        # A partial match is allowed for the current NativeImage to be
        # valid
        STDMETHOD('GetConfigMask')(
            # [OUT]
            (POINTER(DWORD), 'pConfigMask')
        ),
        # Cache data that the CLR will need to determine if the NativeImage
        # can be used (after the GetConfigString checks are satisfied)
        # Sets *pdwBufferSize and returns ERROR_INSUFFICIENT_BUFFER for
        # insufficient ppbBuffer
        STDMETHOD('GetEvaluationDataToCache')(
            # [OUT]
            (POINTER(BYTE), 'ppbBuffer'),
            # [IN | OUT] Total number of bytes written to *ppbBuffer
            (POINTER(DWORD), 'pdwBufferSize')
        ),
        # Dependancy assemblies. The native image is only valid
        # if the dependancies have not changed.
        STDMETHOD('EnumDependencies')(
            # [IN/OUT] - Pointer to the enum
            (POINTER(HCORENUM), 'phEnum'),
            # [OUT]
            (POINTER(INativeImageDependency * 0), 'rDeps'),
            # [IN] Max dependancies to enumerate in this iteration
            (ULONG, 'cMax'),
            # [OUT] - Number of dependancies actually enumerated
            (POINTER(DWORD), 'pdwCount')
        )
    )
    # **************************************************************
    # Runtime callback made by Fusion into the CLR to determine if the
    # NativeAssembly
    # can be used. The pUnkBindSink argument of
    # CAssemblyName::BindToObject() can
    # be queried for this interface
    # **************************************************************
    # {065AA013-9BDC-447c-922F-FEE929908447}
    IID_INativeImageEvaluate = EXTERN_GUID(
        0x65AA013,
        0x9BDC,
        0x447C,
        0x92,
        0x2F,
        0xFE,
        0xE9,
        0x29,
        0x90,
        0x84,
        0x47
    )
    INativeImageEvaluate._iid_ = IID_INativeImageEvaluate
    DECLARE_INTERFACE_(INativeImageEvaluate, comtypes.IUnknown)(
        # This will be called before the assemblies are actually loaded.
        # Returns S_FALSE if the native-image cannot be used.
        STDMETHOD('Evaluate')(
            # [IN] IL assembly in question
            (POINTER(IAssembly), 'pILAssembly'),
            # [IN] NGen image we are trying to use for pILAssembly
            (POINTER(IAssembly), 'pNativeAssembly'),
            # [IN] Data cached when the native-image was generated
            (POINTER(BYTE), 'pbCachedData'),
            # [IN] Size of the pbCachedData buffer
            (DWORD, 'dwDataSize')
        )
    )
    # *******************************************************
    # *******************************************************
    # Predefined CustomAttribute and structures for these custom value
    # *******************************************************
    # Native Link method custom value definitions. This is for
    # N-direct support.
    COR_NATIVE_LINK_CUSTOM_VALUE = "COMPLUS_NativeLink"
    COR_NATIVE_LINK_CUSTOM_VALUE_ANSI = "COMPLUS_NativeLink"
    # count of chars for COR_NATIVE_LINK_CUSTOM_VALUE(_ANSI)
    COR_NATIVE_LINK_CUSTOM_VALUE_CC = 18

    from pyWinAPI.shared.pshpack1_h import *  # NOQA

    COR_NATIVE_LINK._fields_ = [
        # see CorNativeLinkType below
        ('m_linkType', BYTE),
        # see CorNativeLinkFlags below
        ('m_flags', BYTE),
        # member ref token giving entry point, format is lib:entrypoint
        ('m_entryPoint', mdMemberRef),
    ]
    from pyWinAPI.shared.poppack_h import *  # NOQA


    class CorNativeLinkType(ENUM):
        nltNone = 1
        nltAnsi = 2
        nltUnicode = 3
        nltAuto = 4
        nltOle = 5

        # used so we can assert how many bits are required for this
        # enum
        nltMaxValue = 7


    nltNone = CorNativeLinkType.nltNone
    nltAnsi = CorNativeLinkType.nltAnsi
    nltUnicode = CorNativeLinkType.nltUnicode
    nltAuto = CorNativeLinkType.nltAuto
    nltOle = CorNativeLinkType.nltOle
    nltMaxValue = CorNativeLinkType.nltMaxValue


    class CorNativeLinkFlags(ENUM):
        nlfNone = 0x00
        nlfLastError = 0x01
        nlfNoMangle = 0x02

        # used so we can assert how many bits are required for this
        # enum
        nlfMaxValue = 0x03


    nlfNone = CorNativeLinkFlags.nlfNone
    nlfLastError = CorNativeLinkFlags.nlfLastError
    nlfNoMangle = CorNativeLinkFlags.nlfNoMangle
    nlfMaxValue = CorNativeLinkFlags.nlfMaxValue

    COR_DUAL_CUSTOM_VALUE = "IsDual"
    COR_DUAL_CUSTOM_VALUE_ANSI = "IsDual"
    COR_DISPATCH_CUSTOM_VALUE = "DISPID"
    COR_DISPATCH_CUSTOM_VALUE_ANSI = "DISPID"

    # Security custom value definitions (these are all deprecated).
    COR_PERM_REQUEST_REQD_CUSTOM_VALUE = "SecPermReq_Reqd"
    COR_PERM_REQUEST_REQD_CUSTOM_VALUE_ANSI = "SecPermReq_Reqd"
    COR_PERM_REQUEST_OPT_CUSTOM_VALUE = "SecPermReq_Opt"
    COR_PERM_REQUEST_OPT_CUSTOM_VALUE_ANSI = "SecPermReq_Opt"
    COR_PERM_REQUEST_REFUSE_CUSTOM_VALUE = "SecPermReq_Refuse"
    COR_PERM_REQUEST_REFUSE_CUSTOM_VALUE_ANSI = "SecPermReq_Refuse"

    # Base class for security custom attributes.
    COR_BASE_SECURITY_ATTRIBUTE_CLASS = (
        "System.Security.Permissions.SecurityAttribute"
    )
    COR_BASE_SECURITY_ATTRIBUTE_CLASS_ANSI = (
        "System.Security.Permissions.SecurityAttribute"
    )

    # Name of custom attribute used to indicate that per-call security
    # checks should
    # be disabled for P/Invoke calls.
    COR_SUPPRESS_UNMANAGED_CODE_CHECK_ATTRIBUTE = (
        "System.Security.SuppressUnmanagedCodeSecurityAttribute"
    )
    COR_SUPPRESS_UNMANAGED_CODE_CHECK_ATTRIBUTE_ANSI = (
        "System.Security.SuppressUnmanagedCodeSecurityAttribute"
    )

    # Name of custom attribute tagged on module to indicate it contains
    # unverifiable code.
    COR_UNVER_CODE_ATTRIBUTE = (
        "System.Security.UnverifiableCodeAttribute"
    )
    COR_UNVER_CODE_ATTRIBUTE_ANSI = (
        "System.Security.UnverifiableCodeAttribute"
    )

    # Name of custom attribute indicating that a method requires a
    # security object
    # slot on the caller's stack.
    COR_REQUIRES_SECOBJ_ATTRIBUTE = (
        "System.Security.DynamicSecurityMethodAttribute"
    )
    COR_REQUIRES_SECOBJ_ATTRIBUTE_ANSI = (
        "System.Security.DynamicSecurityMethodAttribute"
    )
    COR_COMPILERSERVICE_DISCARDABLEATTRIBUTE = (
        "System.Runtime.CompilerServices.DiscardableAttribute"
    )
    COR_COMPILERSERVICE_DISCARDABLEATTRIBUTE_ASNI = (
        "System.Runtime.CompilerServices.DiscardableAttribute"
    )
    if defined(__cplusplus):
        # **********************************************************
        # **********************************************************
        # C O M + s i g n a t u r e s u p p o r t
        # **********************************************************
        # **********************************************************
        if not defined(FORCEINLINE):
            if _MSC_VER < 1200:
                FORCEINLINE = VOID
            else:
                FORCEINLINE = VOID
            # END IF

        # END IF

        # return true if it is a primitive type, i.e. only need to
        # store CorElementType

        def CorIsPrimitiveType(elementtype):
            return (
                elementtype < ELEMENT_TYPE_PTR or
                elementtype == ELEMENT_TYPE_I or
                elementtype == ELEMENT_TYPE_U
            )

        # Return true if element type is a modifier, i.e.
        # ELEMENT_TYPE_MODIFIER bits are
        # turned on. For now, it is checking for ELEMENT_TYPE_PTR and
        # ELEMENT_TYPE_BYREF
        # as well. This will be removed when we turn on
        # ELEMENT_TYPE_MODIFIER bits for
        # these two enum members.

        def CorIsModifierElementType(elementtype):
            if elementtype in (ELEMENT_TYPE_PTR, ELEMENT_TYPE_BYREF):
                return 1
            return elementtype & ELEMENT_TYPE_MODIFIER


        # Given a compress byte (*pData), return the size of the
        # uncompressed data.

        def CorSigUncompressedDataSize(pData):
            if (pData & 0x80) == 0:
                return 1
            elif (pData & 0xC0) == 0x80:
                return 2
            else:
                return 4

        # /////////////////////////////////////////////////////////////////////

        def CorSigUncompressBigData(pData):  # [IN,OUT] compressed data

            # 1 byte data is handled in CorSigUncompressData
            # _ASSERTE(*pData & 0x80)

            # Medium.
            if (pData & 0xC0) == 0x80:  # 10?? ????
                res = ((pData + 1) & 0x3f) << 8
                res |= pData + 1

            else:  # 110? ????
                res = ((pData + 1) & 0x1f) << 24
                res |= (pData + 1) << 16
                res |= (pData + 1) << 8
                res |= pData + 1

            return res


        def CorSigUncompressData(pData):  # [IN,OUT] compressed data
            # Handle smallest data inline.
            if (pData & 0x80) == 0x00:  # 0??? ????
                return pData + 1
            return CorSigUncompressBigData(pData)


        def CorSigUncompressData(
            # return S_OK or E_BADIMAGEFORMAT if the signature is bad
            pData,  # [IN] compressed data
            len,  # [IN] length of the signature
            pDataOut,  # [OUT] the expanded *pData
            pDataLen  # [OUT] length of the expanded *pData
        ):
            hr = S_OK
            pBytes = ctypes.cast(pData, POINTER(BYTE)).value

            # Smallest.
            if (pBytes & 0x80) == 0x00:  # 0??? ????
                if len < 1:
                    hr = META_E_BAD_SIGNATURE
                else:
                    pDataOut.value = pBytes
                    pDataLen.value = 1
            # Medium.
            elif (pBytes & 0xC0) == 0x80:  # 10?? ????
                if len < 2:
                    hr = META_E_BAD_SIGNATURE
                else:
                    pDataOut.value = (pBytes & 0x3f) << 8 | (pBytes + 1)
                    pDataLen.value = 2
            elif (pBytes & 0xE0) == 0xC0:  # 110? ????
                if len < 4:
                    hr = META_E_BAD_SIGNATURE
                else:
                    pDataOut.value = (
                        (pBytes & 0x1f) << 24 |
                        (pBytes + 1) << 16 |
                        (pBytes + 2) << 8 |
                        (pBytes + 3)
                    )
                    pDataLen.value = 4

            else:  # We don't recognize this encoding
                hr = META_E_BAD_SIGNATURE
            return hr


        def CorSigUncompressData(
            # return number of bytes of that compressed data occupied in pData
            pData,  # [IN] compressed data
            pDataOut  # [OUT] the expanded *pData
        ):

            dwSizeOfData = 0

            #  We don't know how big the signature is, so we'll just say that
            # it's big enough
            if FAILED(
                CorSigUncompressData(pData, 0xff, pDataOut, dwSizeOfData)
            ):
                return -1

            return dwSizeOfData


        g_tkCorEncodeToken = [
            mdtTypeDef,
            mdtTypeRef,
            mdtTypeSpec,
            mdtBaseType
        ]

        # uncompress a token

        def CorSigUncompressToken(  # return the token.
            pData  # [IN,OUT] compressed data
        ):
            tk = CorSigUncompressData(pData)
            tkType = g_tkCorEncodeToken[tk & 0x3]
            tk.value = TokenFromRid(tk >> 2, tkType)
            return tk


        def CorSigUncompressToken(
            # return number of bytes of that compressed data occupied in pData
            pData,  # [IN] compressed data
            pToken  # [OUT] the expanded *pData
        ):

            tk = mdToken()

            cb = CorSigUncompressData(pData, tk)
            tkType = g_tkCorEncodeToken[tk & 0x3]
            tk = TokenFromRid(tk >> 2, tkType)
            pToken.value = tk
            return cb


        SIGN_MASK_ONEBYTE = 0xFFFFFFC0
        SIGN_MASK_TWOBYTE = 0xFFFFE000
        SIGN_MASK_FOURBYTE = 0xF0000000

    # END IF __cplusplus
# END IF   _COR_H_
