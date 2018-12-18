import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *


_COMBASEAPI_H_ = None
_OLE32_ = None
_68K_ = None
REQUIRESAPPLEPASCAL = None
COM_STDMETHOD_CAN_THROW = None
BEGIN_INTERFACE = None
_MPPC_ = None
__SC__ = None
__MWERKS__ = None
NO_NULL_VTABLE_ENTRY = None
SORTPP_PASS = None
CONST_VTABLE = None
FARSTRUCT = None
HUGEP = None
_WIN32_DCOM = None
_PREFAST_ = None
INITGUID = 1


class tagServerInformation(ctypes.Structure):
    pass


ServerInformation = tagServerInformation
PServerInformation = POINTER(tagServerInformation)

# ---------------------------------------------------------------------------
# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.
# File:  combaseapi.h
# Contents: Base Component Object Model defintions.
# ----------------------------------------------------------------------------

from pyWinAPI.shared.apiset_h import * # NOQA
from pyWinAPI.shared.apisetcconv_h import * # NOQA

# TODO version number should be bumped when _APISET_TARGET_VERSION_WIN10_RS2
# becomes available

from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA

if NTDDI_VERSION >= NTDDI_VISTA and not defined(_WIN32_WINNT):
    _WIN32_WINNT = 0x0600
# END IF

if NTDDI_VERSION >= NTDDI_WS03 and not defined(_WIN32_WINNT):
    _WIN32_WINNT = 0x0502
# END IF

if NTDDI_VERSION >= NTDDI_WINXP and not defined(_WIN32_WINNT):
    _WIN32_WINNT = 0x0501
# END IF

if NTDDI_VERSION >= NTDDI_WIN2K and not defined(_WIN32_WINNT):
    _WIN32_WINNT = 0x0500
# END IF


if not defined(_COMBASEAPI_H_):
    _COMBASEAPI_H_ = VOID

    if defined(_MSC_VER):
        pass
    # END IF   _MSC_VER

    ole32 = ctypes.windll.OLE32
    combase = ctypes.windll.COMBASE

    from pyWinAPI.shared.pshpack8_h import * # NOQA
    from pyWinAPI.um.wtypesbase_h import *  # NOQA
    from pyWinAPI.um.unknwnbase_h import *  # NOQA

    # TODO change _OLE32_ to _COMBASEAPI_
    if defined(_OLE32_):
        WINOLEAPI = STDAPI

        def WINOLEAPI_(type):
            return STDAPI_(type)
    else:
        if defined(_68K_):
            if not defined(REQUIRESAPPLEPASCAL):
                WINOLEAPI = HRESULT

                def WINOLEAPI_(type):
                    return DECLSPEC_IMPORT(type(PASCAL))
            else:
                WINOLEAPI = HRESULT

                def WINOLEAPI_(type):
                    return DECLSPEC_IMPORT(PASCAL(type))
            # END IF


        else:
            WINOLEAPI = HRESULT


            def WINOLEAPI_(type):
                return DECLSPEC_IMPORT(type(STDAPICALLTYPE))
        # END IF

    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # **** Interface Declaration
        # *********************************************
        # /*  These are macros for declaring interfaces. They exist so that  a
        # single definition of the interface is simulataneously a proper
        # declaration of the interface structures (C + + abstract classes) for
        # both C and C + + . DECLARE_INTERFACE(iface) is used to declare an
        # interface that does not derive from a base interface.
        # DECLARE_INTERFACE_(iface, baseiface) is used to declare an interface
        # that does derive from a base interface. By default if the source
        # file has a .c extension the C version of the interface
        # declaratations will be expanded; if it has a .cpp extension the C +
        # + version will be expanded. if you want to force the C version
        # expansion even though the source file has a .cpp extension, then
        # define the macro "CINTERFACE". eg. cl -DCINTERFACE file.cpp Example
        # Interface declaration: undef INTERFACE define INTERFACE
        # IClassFactory DECLARE_INTERFACE_(IClassFactory, IUnknown)
        # { // *** IUnknown methods ***
        # STDMETHOD(QueryInterface)
        # (THIS_ REFIID riid, LPVOID FAR* ppvObj) PURE;
        # STDMETHOD_(ULONG,AddRef) (THIS) PURE;
        #  STDMETHOD_(ULONG,Release) (THIS) PURE;
        # // *** IClassFactory methods ***
        # STDMETHOD(CreateInstance)
        # (THIS_ LPUNKNOWN pUnkOuter, REFIID riid, LPVOID FAR* ppvObject) PURE;
        #  };
        # Example C + + expansion:
        # struct FAR IClassFactory : public IUnknown {
        # virtual HRESULT STDMETHODCALLTYPE QueryInterface(
        # IID FAR& riid, LPVOID FAR* ppvObj
        # ) = 0;
        # virtual HRESULT STDMETHODCALLTYPE AddRef(VOID) = 0;
        # virtual HRESULT STDMETHODCALLTYPE Release(VOID) = 0;
        # virtual HRESULT STDMETHODCALLTYPE CreateInstance(
        # LPUNKNOWN pUnkOuter,
        # IID FAR& riid,
        #  LPVOID FAR* ppvObject
        # ) = 0;
        # };
        # NOTE: Our documentation says 'define interface class' but we use
        # 'struct' instead of 'class' to keep a lot of 'public:'
        # lines out of the interfaces. The 'FAR' forces the 'this'
        # pointers to be far, which is what we need.
        # Example C expansion:
        # typedef struct IClassFactory {
        # struct IClassFactoryVtbl FAR* lpVtbl;
        # }
        # IClassFactory; typedef struct IClassFactoryVtbl IClassFactoryVtbl;
        #  struct IClassFactoryVtbl {
        # HRESULT (STDMETHODCALLTYPE * QueryInterface) (
        #  IClassFactory FAR* This,
        # IID FAR* riid,
        # LPVOID FAR* ppvObj
        # ) ;
        #  HRESULT (STDMETHODCALLTYPE * AddRef) (IClassFactory FAR* This) ;
        # HRESULT (STDMETHODCALLTYPE * Release) (IClassFactory FAR* This) ;
        # HRESULT (STDMETHODCALLTYPE * CreateInstance) (
        # IClassFactory FAR* This,
        # LPUNKNOWN pUnkOuter,
        # IID FAR* riid,
        # LPVOID FAR* ppvObject
        # );
        # HRESULT (STDMETHODCALLTYPE * LockServer) (
        # IClassFactory FAR* This,
        # BOOL fLock
        # );
        # };

        if defined(__cplusplus) and not defined(CINTERFACE):
            # define interface   struct FAR
            if defined(COM_STDMETHOD_CAN_THROW):
                COM_DECLSPEC_NOTHROW = VOID
            else:
                COM_DECLSPEC_NOTHROW = DECLSPEC_NOTHROW
            # END IF

            __STRUCT__ = ctypes.Structure
            interface = __STRUCT__

            def STDMETHOD(method):
                return COM_DECLSPEC_NOTHROW(HRESULT(STDMETHODCALLTYPE(method)))


            def STDMETHOD_(type, method):
                return COM_DECLSPEC_NOTHROW(type(STDMETHODCALLTYPE(method)))


            def STDMETHODV(method):
                return COM_DECLSPEC_NOTHROW(HRESULT(STDMETHODVCALLTYPE(method)))


            def STDMETHODV_(type, method):
                return COM_DECLSPEC_NOTHROW(type(STDMETHODVCALLTYPE(method)))

            PURE = VOID
            THIS_ = VOID
            THIS = VOID


            def DECLARE_INTERFACE(iface):
                return interface(DECLSPEC_NOVTABLE(iface))


            def DECLARE_INTERFACE_(iface, baseiface):
                iface.__bases__ += (baseiface,)
                return iface


            def DECLARE_INTERFACE_IID(iface, iid):
                iface._iid_ = DECLSPEC_UUID(iid)
                return iface._iid_


            def DECLARE_INTERFACE_IID_(iface, baseiface, iid):
                iface = DECLARE_INTERFACE_(iface, baseiface)
                return DECLARE_INTERFACE_IID(iface, iid)


            def IFACEMETHOD(method):
                return STDMETHOD(method)


            def IFACEMETHOD_(type, method):
                return STDMETHOD_(type, method)


            def IFACEMETHODV(method):
                return STDMETHODV(method)


            def IFACEMETHODV_(type, method):
                return STDMETHODV_(type, method)


            if not defined(BEGIN_INTERFACE):
                if (
                    defined(_MPPC_) and
                    (
                        (
                            defined(_MSC_VER) or defined(__SC__) or
                            defined(__MWERKS__)
                            ) and
                        not defined(NO_NULL_VTABLE_ENTRY)
                    )
                ):
                    BEGIN_INTERFACE = VOID
                    END_INTERFACE = VOID
                else:
                    BEGIN_INTERFACE = VOID
                    END_INTERFACE = VOID
                # END IF

            # END IF

            if not defined(SORTPP_PASS):
                # This forward declaration has been left where this type was
                # previously defined, to preserve ordering.
                pass

            # END IF   not SORTPP_PASS

            def IID_PPV_ARGS(ppType):
                return POINTER(POINTER(ppType))._iid_, IID_PPV_ARGS_Helper(ppType)
        else:
            interface = ctypes.Structure


            def STDMETHOD(method):
                return HRESULT(STDMETHODCALLTYPE(method))


            def STDMETHOD_(type, method):
                return type(STDMETHODCALLTYPE(method))


            def STDMETHODV(method):
                return HRESULT(STDMETHODVCALLTYPE(method))


            def STDMETHODV_(type, method):
                return type(STDMETHODVCALLTYPE(method))


            def IFACEMETHOD(method):
                return STDMETHOD(method)


            def IFACEMETHOD_(type, method):
                return STDMETHOD_(type, method)


            def IFACEMETHODV(method):
                return STDMETHODV(method)


            def IFACEMETHODV_(type, method):
                return STDMETHODV_(type, method)

            if not defined(BEGIN_INTERFACE):
                if defined(_MPPC_):
                    BEGIN_INTERFACE = VOID
                    END_INTERFACE = VOID
                else:
                    BEGIN_INTERFACE = VOID
                    END_INTERFACE = VOID
                # END IF

            # END IF

            PURE = VOID
            THIS_ = VOID
            THIS = VOID

            if defined(CONST_VTABLE):
                CONST_VTBL = VOID

                def DECLARE_INTERFACE(iface):
                    return iface
            else:
                CONST_VTBL = VOID

                def DECLARE_INTERFACE(iface):
                    return iface
            # END IF


            def DECLARE_INTERFACE_(iface, baseiface):
                return DECLARE_INTERFACE(iface)


            def DECLARE_INTERFACE_IID(iface, iid):
                return DECLARE_INTERFACE(iface)


            def DECLARE_INTERFACE_IID_(iface, baseiface, iid):
                return DECLARE_INTERFACE_(iface, baseiface)
        # END IF

        # **** Additional basic types
        # ********************************************
        if not defined(FARSTRUCT):
            if defined(__cplusplus):
                FARSTRUCT = VOID
            else:
                FARSTRUCT = VOID
            # END IF   __cplusplus
        # END IF   FARSTRUCT

        if not defined(HUGEP):
            if defined(_WIN32) or defined(_MPPC_):
                HUGEP = VOID
            else:
                HUGEP = VOID
            # END IF   WIN32
        # END IF   HUGEP

        from pyWinAPI.km.crt.stdlib_h import * # NOQA


        def LISet32(li, v):
            if v < 0:
                li.HighPart = -1
            else:
                li.HighPart = 0
            li.LowPart = v

        def ULISet32(li, v):
            li.HighPart = 0
            li.LowPart = v


        CLSCTX_INPROC = (
            CLSCTX.CLSCTX_INPROC_SERVER |
            CLSCTX.CLSCTX_INPROC_HANDLER
        )
        # With DCOM, CLSCTX_REMOTE_SERVER should be included
        # DCOM
        if _WIN32_WINNT >= 0x0400 or defined(_WIN32_DCOM):
            CLSCTX_ALL = (
                CLSCTX.CLSCTX_INPROC_SERVER |
                CLSCTX.CLSCTX_INPROC_HANDLER |
                CLSCTX.CLSCTX_LOCAL_SERVER |
                CLSCTX.CLSCTX_REMOTE_SERVER
            )
            CLSCTX_SERVER = (
                CLSCTX.CLSCTX_INPROC_SERVER |
                CLSCTX.CLSCTX_LOCAL_SERVER |
                CLSCTX.CLSCTX_REMOTE_SERVER
            )
        else:
            CLSCTX_ALL = (
                CLSCTX.CLSCTX_INPROC_SERVER |
                CLSCTX.CLSCTX_INPROC_HANDLER |
                CLSCTX.CLSCTX_LOCAL_SERVER
            )
            CLSCTX_SERVER = (
                CLSCTX.CLSCTX_INPROC_SERVER |
                CLSCTX.CLSCTX_LOCAL_SERVER
            )
        # END IF

        # class registration flags; passed to CoRegisterClassObject
        class tagREGCLS(ENUM):
            REGCLS_SINGLEUSE = 0
            REGCLS_MULTIPLEUSE = 1
            REGCLS_MULTI_SEPARATE = 2
            REGCLS_SUSPENDED = 4
            REGCLS_SURROGATE = 8
            if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
                REGCLS_AGILE = 0x10
            # END IF


        REGCLS = tagREGCLS

        # here is where we pull in the MIDL generated headers for the
        # interfaces
        class IRpcStubBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []


        class IRpcChannelBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

        # COM initialization flags; passed to CoInitialize.
        class tagCOINITBASE(ENUM):
            if (_WIN32_WINNT >= 0x0400) or defined(_WIN32_DCOM):
                COINITBASE_MULTITHREADED = 0x0
            # END IF

        COINITBASE = tagCOINITBASE

        if defined(__cplusplus) and not defined(CINTERFACE):
            # IID_PPV_ARGS(ppType)
            # ppType is the variable of type IType that will be filled
            # RESULTS in: IID_IType, ppvType
            # will create a compiler error if wrong level of indirection is
            # used.            # make sure everyone derives from IUnknown
            pass

        # END IF defined(__cplusplus) and not defined(CINTERFACE)

        from pyWinAPI.um.objidlbase_h import * # NOQA
        from pyWinAPI.shared.guiddef_h import * # NOQA

        if defined(INITGUID):
            # // TODO change to cguidbase.h
            from pyWinAPI.um.cguid_h import * # NOQA
        # END IF

    # END IF WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    #
    # // **** STD Object API Prototypes ***************************************
    #
    # #pragma region Desktop or OneCore Family
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_ WINOLEAPI
        # CoGetMalloc(
        # _In_ DWORD dwMemContext,
        # _Outptr_ LPMALLOC  FAR * ppMalloc
        # );
        CoGetMalloc = ole32.CoGetMalloc
        CoGetMalloc.restype = WINOLEAPI
    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_ WINOLEAPI
        # CreateStreamOnHGlobal(
        # HGLOBAL hGlobal,
        # _In_ BOOL fDeleteOnRelease,
        # _Outptr_ LPSTREAM  FAR * ppstm
        # );
        CreateStreamOnHGlobal = ole32.CreateStreamOnHGlobal
        CreateStreamOnHGlobal.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # GetHGlobalFromStream(
        # _In_ LPSTREAM pstm,
        # _Out_ HGLOBAL  FAR * phglobal
        # );
        GetHGlobalFromStream = ole32.GetHGlobalFromStream
        GetHGlobalFromStream.restype = WINOLEAPI

        # init/uninit
        # WINOLEAPI_(VOID)
        # CoUninitialize(
        # void
        # );
        CoUninitialize = ole32.CoUninitialize
        CoUninitialize.restype = VOID

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAPI_(DWORD)
        # CoGetCurrentProcess(
        # void
        # );
        CoGetCurrentProcess = ole32.CoGetCurrentProcess
        CoGetCurrentProcess.restype = DWORD

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # DCOM
    if _WIN32_WINNT >= 0x0400 or defined(_WIN32_DCOM):
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            # _Check_return_ WINOLEAPI
            # CoInitializeEx(
            # _In_opt_ LPVOID pvReserved,
            # _In_ DWORD dwCoInit
            # );
            CoInitializeEx = ole32.CoInitializeEx
            CoInitializeEx.restype = WINOLEAPI

        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # WINOLEAPI
            # CoGetCallerTID(
            # _Out_ LPDWORD lpdwTID
            # );
            CoGetCallerTID = ole32.CoGetCallerTID
            CoGetCallerTID.restype = WINOLEAPI


        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            # WINOLEAPI
            # CoGetCurrentLogicalThreadId(
            # _Out_ GUID* pguid
            # );
            CoGetCurrentLogicalThreadId = ole32.CoGetCurrentLogicalThreadId
            CoGetCurrentLogicalThreadId.restype = WINOLEAPI

        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    # END IF   DCOM

    if _WIN32_WINNT >= 0x0501:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            # _Check_return_ WINOLEAPI
            # CoGetContextToken(
            # _Out_ ULONG_PTR* pToken
            # );
            CoGetContextToken = ole32.CoGetContextToken
            CoGetContextToken.restype = WINOLEAPI

            # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # _Check_return_ WINOLEAPI
            # CoGetDefaultContext(
            # _In_ APTTYPE aptType,
            # _In_ REFIID riid,
            # _Outptr_ void** ppv
            # );
            CoGetDefaultContext = ole32.CoGetDefaultContext
            CoGetDefaultContext.restype = WINOLEAPI

        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # definition for Win7 new APIs
        if NTDDI_VERSION >= NTDDI_WIN7:
            # _Check_return_ WINOLEAPI
            # CoGetApartmentType(
            # _Out_ APTTYPE* pAptType,
            # _Out_ APTTYPEQUALIFIER* pAptQualifier
            # );
            CoGetApartmentType = ole32.CoGetApartmentType
            CoGetApartmentType.restype = WINOLEAPI

        # END IF

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # definition for Win8 new APIs
    if NTDDI_VERSION >= NTDDI_WIN8:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            tagServerInformation._fields_ = [
                ('dwServerPid', DWORD),
                ('dwServerTid', DWORD),
                ('ui64ServerAddress', UINT64),
            ]
        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # _Check_return_ WINOLEAPI
            # CoDecodeProxy(
            # _In_ DWORD dwClientPid,
            # _In_ UINT64 ui64ProxyAddress,
            # _Out_ PServerInformation pServerInformation
            # );
            CoDecodeProxy = combase.CoDecodeProxy
            CoDecodeProxy.restype = WINOLEAPI

        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        CO_MTA_USAGE_COOKIE = DECLARE_HANDLE()
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            pass
        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # _Check_return_ WINOLEAPI
            # CoIncrementMTAUsage(
            # _Out_ CO_MTA_USAGE_COOKIE* pCookie
            # );
            CoIncrementMTAUsage = ole32.CoIncrementMTAUsage
            CoIncrementMTAUsage.restype = WINOLEAPI

            # WINOLEAPI
            # CoDecrementMTAUsage(
            # _In_ CO_MTA_USAGE_COOKIE Cookie
            # );
            CoDecrementMTAUsage = ole32.CoDecrementMTAUsage
            CoDecrementMTAUsage.restype = WINOLEAPI

            # WINOLEAPI
            # CoAllowUnmarshalerCLSID(
            # _In_ REFCLSID clsid
            # );
            CoAllowUnmarshalerCLSID = ole32.CoAllowUnmarshalerCLSID
            CoAllowUnmarshalerCLSID.restype = WINOLEAPI

        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_ WINOLEAPI
        # CoGetObjectContext(
        # _In_ REFIID riid,
        # _Outptr_ LPVOID  FAR * ppv
        # );
        CoGetObjectContext = ole32.CoGetObjectContext
        CoGetObjectContext.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # register/revoke/get class objects
        # _Check_return_ WINOLEAPI
        # CoGetClassObject(
        # _In_ REFCLSID rclsid,
        # _In_ DWORD dwClsContext,
        # _In_opt_ LPVOID pvReserved,
        # _In_ REFIID riid,
        # _Outptr_ LPVOID  FAR * ppv
        # );
        CoGetClassObject = ole32.CoGetClassObject
        CoGetClassObject.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_ WINOLEAPI
        # CoRegisterClassObject(
        # _In_ REFCLSID rclsid,
        # _In_ LPUNKNOWN pUnk,
        # _In_ DWORD dwClsContext,
        # _In_ DWORD flags,
        # _Out_ LPDWORD lpdwRegister
        # );
        CoRegisterClassObject = ole32.CoRegisterClassObject
        CoRegisterClassObject.restype = WINOLEAPI

        # WINOLEAPI
        # CoRevokeClassObject(
        # _In_ DWORD dwRegister
        # );
        CoRevokeClassObject = ole32.CoRevokeClassObject
        CoRevokeClassObject.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # CoResumeClassObjects(
        # void
        # );
        CoResumeClassObjects = ole32.CoResumeClassObjects
        CoResumeClassObjects.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # CoSuspendClassObjects(
        # void
        # );
        CoSuspendClassObjects = ole32.CoSuspendClassObjects
        CoSuspendClassObjects.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAPI_(ULONG)
        # CoAddRefServerProcess(
        # void
        # );
        CoAddRefServerProcess = ole32.CoAddRefServerProcess
        CoAddRefServerProcess.restype = WINOLEAPI_(ULONG)

        # WINOLEAPI_(ULONG)
        # CoReleaseServerProcess(
        # void
        # );
        CoReleaseServerProcess = ole32.CoReleaseServerProcess
        CoReleaseServerProcess.restype = WINOLEAPI_(ULONG)

        # _Check_return_ WINOLEAPI
        # CoGetPSClsid(
        # _In_ REFIID riid,
        # _Out_ CLSID* pClsid
        # );
        CoGetPSClsid = ole32.CoGetPSClsid
        CoGetPSClsid.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # CoRegisterPSClsid(
        # _In_ REFIID riid,
        # _In_ REFCLSID rclsid
        # );
        CoRegisterPSClsid = ole32.CoRegisterPSClsid
        CoRegisterPSClsid.restype = WINOLEAPI

        # Registering surrogate processes
        # _Check_return_ WINOLEAPI
        # CoRegisterSurrogate(
        # _In_ LPSURROGATE pSurrogate
        # );
        CoRegisterSurrogate = ole32.CoRegisterSurrogate
        CoRegisterSurrogate.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # marshaling interface pointers
        # _Check_return_ WINOLEAPI
        # CoGetMarshalSizeMax(
        # _Out_ ULONG* pulSize,
        # _In_ REFIID riid,
        # _In_ LPUNKNOWN pUnk,
        # _In_ DWORD dwDestContext,
        # _In_opt_ LPVOID pvDestContext,
        # _In_ DWORD mshlflags
        # );
        CoGetMarshalSizeMax = ole32.CoGetMarshalSizeMax
        CoGetMarshalSizeMax.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # CoMarshalInterface(
        # _In_ LPSTREAM pStm,
        # _In_ REFIID riid,
        # _In_ LPUNKNOWN pUnk,
        # _In_ DWORD dwDestContext,
        # _In_opt_ LPVOID pvDestContext,
        # _In_ DWORD mshlflags
        # );
        CoMarshalInterface = ole32.CoMarshalInterface
        CoMarshalInterface.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # CoUnmarshalInterface(
        # _In_ LPSTREAM pStm,
        # _In_ REFIID riid,
        # _COM_Outptr_ LPVOID  FAR * ppv
        # );
        CoUnmarshalInterface = ole32.CoUnmarshalInterface
        CoUnmarshalInterface.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAPI
        # CoMarshalHresult(
        # _In_ LPSTREAM pstm,
        # _In_ HRESULT hresult
        # );
        CoMarshalHresult = ole32.CoMarshalHresult
        CoMarshalHresult.restype = WINOLEAPI

        # WINOLEAPI
        # CoUnmarshalHresult(
        # _In_ LPSTREAM pstm,
        # _Out_ HRESULT  FAR * phresult
        # );
        CoUnmarshalHresult = ole32.CoUnmarshalHresult
        CoUnmarshalHresult.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_ WINOLEAPI
        # CoReleaseMarshalData(
        # _In_ LPSTREAM pStm
        # );
        CoReleaseMarshalData = ole32.CoReleaseMarshalData
        CoReleaseMarshalData.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # CoDisconnectObject(
        # _In_ LPUNKNOWN pUnk,
        # _In_ DWORD dwReserved
        # );
        CoDisconnectObject = ole32.CoDisconnectObject
        CoDisconnectObject.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_ WINOLEAPI
        # CoLockObjectExternal(
        # _In_ LPUNKNOWN pUnk,
        # _In_ BOOL fLock,
        # _In_ BOOL fLastUnlockReleases
        # );
        CoLockObjectExternal = ole32.CoLockObjectExternal
        CoLockObjectExternal.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_ WINOLEAPI
        # CoGetStandardMarshal(
        # _In_ REFIID riid,
        # _In_ LPUNKNOWN pUnk,
        # _In_ DWORD dwDestContext,
        # _In_opt_ LPVOID pvDestContext,
        # _In_ DWORD mshlflags,
        # _Outptr_ LPMARSHAL  FAR * ppMarshal
        # );
        CoGetStandardMarshal = ole32.CoGetStandardMarshal
        CoGetStandardMarshal.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_ WINOLEAPI
        # CoGetStdMarshalEx(
        # _In_ LPUNKNOWN pUnkOuter,
        # _In_ DWORD smexflags,
        # _Outptr_ LPUNKNOWN  FAR * ppUnkInner
        # );
        CoGetStdMarshalEx = ole32.CoGetStdMarshalEx
        CoGetStdMarshalEx.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # flags for CoGetStdMarshalEx
        class tagSTDMSHLFLAGS(ENUM):
            SMEXF_SERVER = 0x01
            SMEXF_HANDLER = 0x02


        STDMSHLFLAGS = tagSTDMSHLFLAGS
    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAPI_(BOOL)
        # CoIsHandlerConnected(
        # _In_ LPUNKNOWN pUnk
        # );
        CoIsHandlerConnected = ole32.CoIsHandlerConnected
        CoIsHandlerConnected.restype = WINOLEAPI_(BOOL)

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # Apartment model inter-thread interface passing helpers
        # _Check_return_ WINOLEAPI
        # CoMarshalInterThreadInterfaceInStream(
        # _In_ REFIID riid,
        # _In_ LPUNKNOWN pUnk,
        # _Outptr_ LPSTREAM* ppStm
        # );
        CoMarshalInterThreadInterfaceInStream = (
            ole32.CoMarshalInterThreadInterfaceInStream
        )
        CoMarshalInterThreadInterfaceInStream.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # CoGetInterfaceAndReleaseStream(
        # _In_ LPSTREAM pStm,
        # _In_ REFIID iid,
        # _COM_Outptr_ LPVOID  FAR * ppv
        # );
        CoGetInterfaceAndReleaseStream = (
            ole32.CoGetInterfaceAndReleaseStream
        )
        CoGetInterfaceAndReleaseStream.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # CoCreateFreeThreadedMarshaler(
        # _In_opt_ LPUNKNOWN punkOuter,
        # _Outptr_ LPUNKNOWN* ppunkMarshal
        # );
        CoCreateFreeThreadedMarshaler = ole32.CoCreateFreeThreadedMarshaler
        CoCreateFreeThreadedMarshaler.restype = WINOLEAPI

        # WINOLEAPI_(VOID)
        # CoFreeUnusedLibraries(
        # void
        # );
        CoFreeUnusedLibraries = ole32.CoFreeUnusedLibraries
        CoFreeUnusedLibraries.restype = WINOLEAPI_(VOID)

        if _WIN32_WINNT >= 0x0501:
            ole32 = ctypes.windll.OLE32

            # WINOLEAPI_(VOID)
            # CoFreeUnusedLibrariesEx(
            # _In_ DWORD dwUnloadDelay,
            # _In_ DWORD dwReserved
            # );
            CoFreeUnusedLibrariesEx = ole32.CoFreeUnusedLibrariesEx
            CoFreeUnusedLibrariesEx.restype = WINOLEAPI_(VOID)

        # END IF

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if _WIN32_WINNT >= 0x0600:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # _Check_return_ WINOLEAPI
            # CoDisconnectContext(
            # DWORD dwTimeout
            # );
            CoDisconnectContext = ole32.CoDisconnectContext
            CoDisconnectContext.restype = WINOLEAPI

        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    # END IF


    # DCOM
    if _WIN32_WINNT >= 0x0400 or defined(_WIN32_DCOM):
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            # Call Security.
            # _Check_return_ WINOLEAPI
            # CoInitializeSecurity(
            # _In_opt_ PSECURITY_DESCRIPTOR pSecDesc,
            # _In_ LONG cAuthSvc,
            # _In_reads_opt_(cAuthSvc) SOLE_AUTHENTICATION_SERVICE* asAuthSvc,
            # _In_opt_ void* pReserved1,
            # _In_ DWORD dwAuthnLevel,
            # _In_ DWORD dwImpLevel,
            # _In_opt_ void* pAuthList,
            # _In_ DWORD dwCapabilities,
            # _In_opt_ void* pReserved3
            # );
            CoInitializeSecurity = ole32.CoInitializeSecurity
            CoInitializeSecurity.restype = WINOLEAPI

        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # _Check_return_ WINOLEAPI
            # CoGetCallContext(
            # _In_ REFIID riid,
            # _Outptr_ void** ppInterface
            # );
            CoGetCallContext = ole32.CoGetCallContext
            CoGetCallContext.restype = WINOLEAPI

            # _Check_return_ WINOLEAPI
            # CoQueryProxyBlanket(
            # _In_ IUnknown* pProxy,
            # _Out_opt_ DWORD* pwAuthnSvc,
            # _Out_opt_ DWORD* pAuthzSvc,
            # _Outptr_opt_ LPOLESTR* pServerPrincName,
            # _Out_opt_ DWORD* pAuthnLevel,
            # _Out_opt_ DWORD* pImpLevel,
            # _Out_opt_ RPC_AUTH_IDENTITY_HANDLE* pAuthInfo,
            # _Out_opt_ DWORD* pCapabilites
            # );
            CoQueryProxyBlanket = ole32.CoQueryProxyBlanket
            CoQueryProxyBlanket.restype = WINOLEAPI

            # _Check_return_ WINOLEAPI
            # CoSetProxyBlanket(
            # _In_ IUnknown* pProxy,
            # _In_ DWORD dwAuthnSvc,
            # _In_ DWORD dwAuthzSvc,
            # _In_opt_ OLECHAR* pServerPrincName,
            # _In_ DWORD dwAuthnLevel,
            # _In_ DWORD dwImpLevel,
            # _In_opt_ RPC_AUTH_IDENTITY_HANDLE pAuthInfo,
            # _In_ DWORD dwCapabilities
            # );
            CoSetProxyBlanket = ole32.CoSetProxyBlanket
            CoSetProxyBlanket.restype = WINOLEAPI

            # _Check_return_ WINOLEAPI
            # CoCopyProxy(
            # _In_ IUnknown* pProxy,
            # _Outptr_ IUnknown** ppCopy
            # );
            CoCopyProxy = ole32.CoCopyProxy
            CoCopyProxy.restype = WINOLEAPI

            # _Check_return_ WINOLEAPI
            # CoQueryClientBlanket(
            # _Out_opt_ DWORD* pAuthnSvc,
            # _Out_opt_ DWORD* pAuthzSvc,
            # _Outptr_opt_ LPOLESTR* pServerPrincName,
            # _Out_opt_ DWORD* pAuthnLevel,
            # _Out_opt_ DWORD* pImpLevel,
            # _Outptr_opt_result_buffer_(_Inexpressible_("depends on pAuthnSvc")) RPC_AUTHZ_HANDLE* pPrivs,
            # _Inout_opt_ DWORD* pCapabilities
            # );
            CoQueryClientBlanket = ole32.CoQueryClientBlanket
            CoQueryClientBlanket.restype = WINOLEAPI

            # _Check_return_ WINOLEAPI
            # CoImpersonateClient(
            # void
            # );
            CoImpersonateClient = ole32.CoImpersonateClient
            CoImpersonateClient.restype = WINOLEAPI

            # _Check_return_ WINOLEAPI
            # CoRevertToSelf(
            # void
            # );
            CoRevertToSelf = ole32.CoRevertToSelf
            CoRevertToSelf.restype = WINOLEAPI

            # _Check_return_ WINOLEAPI
            # CoQueryAuthenticationServices(
            # _Out_ DWORD* pcAuthSvc,
            # _Outptr_result_buffer_(*pcAuthSvc) SOLE_AUTHENTICATION_SERVICE** asAuthSvc
            # );
            CoQueryAuthenticationServices = (
                ole32.CoQueryAuthenticationServices
            )
            CoQueryAuthenticationServices.restype = WINOLEAPI

        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            # _Check_return_ WINOLEAPI
            # CoSwitchCallContext(
            # _In_opt_ IUnknown* pNewObject,
            # _Outptr_ IUnknown** ppOldObject
            # );
            CoSwitchCallContext = ole32.CoSwitchCallContext
            CoSwitchCallContext.restype = WINOLEAPI

            COM_RIGHTS_EXECUTE = 1
            COM_RIGHTS_EXECUTE_LOCAL = 2
            COM_RIGHTS_EXECUTE_REMOTE = 4
            COM_RIGHTS_ACTIVATE_LOCAL = 8
            COM_RIGHTS_ACTIVATE_REMOTE = 16
        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    # END IF   DCOM

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # helper for creating instances
        # _Check_return_ WINOLEAPI
        # CoCreateInstance(
        # _In_ REFCLSID rclsid,
        # _In_opt_ LPUNKNOWN pUnkOuter,
        # _In_ DWORD dwClsContext,
        # _In_ REFIID riid,
        # _COM_Outptr_ _At_(*ppv, _Post_readable_size_(_Inexpressible_(varies))) LPVOID  FAR * ppv
        # );
        CoCreateInstance = ole32.CoCreateInstance
        CoCreateInstance.restype = WINOLEAPI

        # DCOM
        if _WIN32_WINNT >= 0x0400 or defined(_WIN32_DCOM):
            # _Check_return_ WINOLEAPI
            # CoCreateInstanceEx(
            # _In_ REFCLSID Clsid,
            # _In_opt_ IUnknown* punkOuter,
            # _In_ DWORD dwClsCtx,
            # _In_opt_ COSERVERINFO* pServerInfo,
            # _In_ DWORD dwCount,
            # _Inout_updates_(dwCount) MULTI_QI* pResults
            # );
            CoCreateInstanceEx = ole32.CoCreateInstanceEx
            CoCreateInstanceEx.restype = WINOLEAPI

        # END IF   DCOM

        # WINOLEAPI
        # CoRegisterActivationFilter(
        # _In_ IActivationFilter* pActivationFilter
        # );
        CoRegisterActivationFilter = ole32.CoRegisterActivationFilter
        CoRegisterActivationFilter.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if _WIN32_WINNT >= 0x0602:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            # _Check_return_ WINOLEAPI
            # CoCreateInstanceFromApp(
            # _In_ REFCLSID Clsid,
            # _In_opt_ IUnknown* punkOuter,
            # _In_ DWORD dwClsCtx,
            # _In_opt_ PVOID reserved,
            # _In_ DWORD dwCount,
            # _Inout_updates_(dwCount) MULTI_QI* pResults
            # );
            CoCreateInstanceFromApp = combase.CoCreateInstanceFromApp
            CoCreateInstanceFromApp.restype = WINOLEAPI

        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    # END IF

    if WINAPI_PARTITION_APP and not (WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # __inline _Check_return_ HRESULT CoCreateInstance(
        # _In_     REFCLSID rclsid,
        # _In_opt_ LPUNKNOWN pUnkOuter,
        # _In_     DWORD dwClsContext,
        # _In_     REFIID riid,
        # _COM_Outptr_ _At_(*ppv, _Post_readable_size_(_Inexpressible_(varies))) LPVOID FAR* ppv)
        # {
        # MULTI_QI    OneQI;
        CoCreateInstance = ole32.CoCreateInstance
        CoCreateInstance.restype = HRESULT

        if defined(__cplusplus):
            pass
        else:
            pass
        # END IF

        if defined(_PREFAST_):
            pass
        # END IF

        # }
        #
        # __inline _Check_return_ HRESULT CoCreateInstanceEx(
        # _In_ REFCLSID                      Clsid,
        # _In_opt_ IUnknown     *            punkOuter,
        # _In_ DWORD                         dwClsCtx,
        # _In_opt_ COSERVERINFO *            pServerInfo,
        # _In_ DWORD                         dwCount,
        # _Inout_updates_(dwCount) MULTI_QI *pResults )
        # {
        # return CoCreateInstanceFromApp(Clsid, punkOuter, dwClsCtx, pServerInfo, dwCount, pResults);
        CoCreateInstanceEx = ole32.CoCreateInstanceEx
        CoCreateInstanceEx.restype = HRESULT

        # }
        #
    # END IF WINAPI_PARTITION_APP and not (WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # // Call related APIs
    # // DCOM
    if _WIN32_WINNT >= 0x0500 or defined(_WIN32_DCOM):
        # #pragma region Desktop or OneCore Family
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            #
            # _Check_return_ WINOLEAPI
            # CoGetCancelObject(
            # _In_ DWORD dwThreadId,
            # _In_ REFIID iid,
            # _Outptr_ void** ppUnk
            # );
            CoGetCancelObject = ole32.CoGetCancelObject
            CoGetCancelObject.restype = WINOLEAPI
            # _Check_return_ WINOLEAPI
            # CoSetCancelObject(
            # _In_opt_ IUnknown* pUnk
            # );
            CoSetCancelObject = ole32.CoSetCancelObject
            CoSetCancelObject.restype = WINOLEAPI
            # _Check_return_ WINOLEAPI
            # CoCancelCall(
            # _In_ DWORD dwThreadId,
            # _In_ ULONG ulTimeout
            # );
            CoCancelCall = ole32.CoCancelCall
            CoCancelCall.restype = WINOLEAPI
            # _Check_return_ WINOLEAPI
            # CoTestCancel(
            # void
            # );
            CoTestCancel = ole32.CoTestCancel
            CoTestCancel.restype = WINOLEAPI
            # _Check_return_ WINOLEAPI
            # CoEnableCallCancellation(
            # _In_opt_ LPVOID pReserved
            # );
            CoEnableCallCancellation = ole32.CoEnableCallCancellation
            CoEnableCallCancellation.restype = WINOLEAPI
            # _Check_return_ WINOLEAPI
            # CoDisableCallCancellation(
            # _In_opt_ LPVOID pReserved
            # );
            CoDisableCallCancellation = ole32.CoDisableCallCancellation
            CoDisableCallCancellation.restype = WINOLEAPI
        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # other helpers

        # _Check_return_ WINOLEAPI
        # StringFromCLSID(
        # _In_ REFCLSID rclsid,
        # _Outptr_ LPOLESTR  FAR * lplpsz
        # );
        StringFromCLSID = ole32.StringFromCLSID
        StringFromCLSID.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # CLSIDFromString(
        # _In_ LPCOLESTR lpsz,
        # _Out_ LPCLSID pclsid
        # );
        CLSIDFromString = ole32.CLSIDFromString
        CLSIDFromString.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # StringFromIID(
        # _In_ REFIID rclsid,
        # _Outptr_ LPOLESTR  FAR * lplpsz
        # );
        StringFromIID = ole32.StringFromIID
        StringFromIID.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # IIDFromString(
        # _In_ LPCOLESTR lpsz,
        # _Out_ LPIID lpiid
        # );
        IIDFromString = ole32.IIDFromString
        IIDFromString.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_ WINOLEAPI
        # ProgIDFromCLSID(
        # _In_ REFCLSID clsid,
        # _Outptr_ LPOLESTR  FAR * lplpszProgID
        # );
        ProgIDFromCLSID = ole32.ProgIDFromCLSID
        ProgIDFromCLSID.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # CLSIDFromProgID(
        # _In_ LPCOLESTR lpszProgID,
        # _Out_ LPCLSID lpclsid
        # );
        CLSIDFromProgID = ole32.CLSIDFromProgID
        CLSIDFromProgID.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_ WINOLEAPI_(int)
        # StringFromGUID2(
        # _In_ REFGUID rguid,
        # _Out_writes_to_(cchMax,return) LPOLESTR lpsz,
        # _In_ INT cchMax
        # );
        StringFromGUID2 = ole32.StringFromGUID2
        StringFromGUID2.restype = INT

        # _Check_return_ WINOLEAPI
        # CoCreateGuid(
        # _Out_ GUID  FAR * pguid
        # );
        CoCreateGuid = ole32.CoCreateGuid
        CoCreateGuid.restype = WINOLEAPI

        # Prop variant support
        PROPVARIANT = tagPROPVARIANT

        # _Check_return_
        # WINOLEAPI
        # PropVariantCopy(
        # _Out_ PROPVARIANT* pvarDest,
        # _In_ PROPVARIANT* pvarSrc
        # );
        PropVariantCopy = ole32.PropVariantCopy
        PropVariantCopy.restype = WINOLEAPI

        # WINOLEAPI
        # PropVariantClear(
        # _Inout_ PROPVARIANT* pvar
        # );
        PropVariantClear = ole32.PropVariantClear
        PropVariantClear.restype = WINOLEAPI

        # WINOLEAPI
        # FreePropVariantArray(
        # _In_ ULONG cVariants,
        # _Inout_updates_(cVariants) PROPVARIANT* rgvars
        # );
        FreePropVariantArray = ole32.FreePropVariantArray
        FreePropVariantArray.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # DCOM
    if _WIN32_WINNT >= 0x0400 or defined(_WIN32_DCOM):
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            pass
        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    # END IF   DCOM

    # DCOM
    if (_WIN32_WINNT >= 0x0400) or defined(_WIN32_DCOM):
        # Synchronization API
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # _Check_return_ WINOLEAPI
            # CoWaitForMultipleHandles(
            # _In_ DWORD dwFlags,
            # _In_ DWORD dwTimeout,
            # _In_ ULONG cHandles,
            # _In_reads_(cHandles) LPHANDLE pHandles,
            # _Out_ LPDWORD lpdwindex
            # );
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

            if NTDDI_VERSION >= NTDDI_WIN8:
                class CWMO_FLAGS(ENUM):
                    CWMO_DEFAULT = 0
                    CWMO_DISPATCH_CALLS = 1
                    CWMO_DISPATCH_WINDOW_MESSAGES = 2


                # WINOLEAPI
                # CoWaitForMultipleObjects(
                # _In_ DWORD dwFlags,
                # _In_ DWORD dwTimeout,
                # _In_ ULONG cHandles,
                # _In_reads_(cHandles) HANDLE* pHandles,
                # _Out_ LPDWORD lpdwindex
                # );
                CoWaitForMultipleObjects = combase.CoWaitForMultipleObjects
                CoWaitForMultipleObjects.restype = WINOLEAPI

            # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

            CWMO_MAX_HANDLES = 56
        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    # END IF   DCOM

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_ WINOLEAPI
        # CoGetTreatAsClass(
        # _In_ REFCLSID clsidOld,
        # _Out_ LPCLSID pClsidNew
        # );
        CoGetTreatAsClass = ole32.CoGetTreatAsClass
        CoGetTreatAsClass.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # for flushing OLESCM remote binding handles
    if _WIN32_WINNT >= 0x0501:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # _Check_return_ WINOLEAPI
            # CoInvalidateRemoteMachineBindings(
            # _In_ LPOLESTR pszMachineName
            # );
            CoInvalidateRemoteMachineBindings = (
                ole32.CoInvalidateRemoteMachineBindings
            )
            CoInvalidateRemoteMachineBindings.restype = WINOLEAPI
        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    # END IF

    if NTDDI_VERSION >= NTDDI_WINBLUE:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            class AgileReferenceOptions(ENUM):
                AGILEREFERENCE_DEFAULT = 0
                AGILEREFERENCE_DELAYEDMARSHAL = 1

            AGILEREFERENCE_DEFAULT = AgileReferenceOptions.AGILEREFERENCE_DEFAULT
            AGILEREFERENCE_DELAYEDMARSHAL = AgileReferenceOptions.AGILEREFERENCE_DELAYEDMARSHAL

            # _Check_return_ WINOLEAPI
            # RoGetAgileReference(
            # _In_ enum AgileReferenceOptions options,
            # _In_ REFIID riid,
            # _In_ IUnknown* pUnk,
            # _COM_Outptr_ IAgileReference** ppAgileReference
            # );
            RoGetAgileReference = ole32.RoGetAgileReference
            RoGetAgileReference.restype = WINOLEAPI

        # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # /* the server dlls must define their DllGetClassObject and
        # DllCanUnloadNow to match these; the typedefs are located here to
        # ensure all are changed at the same time.
        # typedef HRESULT (STDAPICALLTYPE * LPFNGETCLASSOBJECT) (REFCLSID, REFIID, LPVOID *);
        LPFNGETCLASSOBJECT = STDAPICALLTYPE(
            HRESULT,
            REFCLSID,
            REFIID,
            LPVOID
        )

        # typedef HRESULT (STDAPICALLTYPE * LPFNCANUNLOADNOW)(VOID);
        LPFNCANUNLOADNOW = STDAPICALLTYPE(
            HRESULT,
            VOID
        )

        # **** Default Memory Allocation
        # ****************************************

        # WINOLEAPI_(_Ret_opt_ _Post_writable_byte_size_(cb)  __drv_allocatesMem(Mem) _Check_return_ LPVOID)
        # CoTaskMemAlloc(
        # _In_ SIZE_T cb
        # );
        CoTaskMemAlloc = ole32.CoTaskMemAlloc
        CoTaskMemAlloc.restype = LPVOID

        # WINOLEAPI_(_Ret_opt_ _Post_writable_byte_size_(cb)  _When_(cb > 0, __drv_allocatesMem(Mem) _Check_return_) LPVOID)
        # CoTaskMemRealloc(
        # _Pre_maybenull_ __drv_freesMem(Mem) _Post_invalid_ LPVOID pv,
        # _In_ SIZE_T cb
        # );
        CoTaskMemRealloc = ole32.CoTaskMemRealloc
        CoTaskMemRealloc.restype = LPVOID

        # WINOLEAPI_(VOID)
        # CoTaskMemFree(
        # _Frees_ptr_opt_ LPVOID pv
        # );
        CoTaskMemFree = ole32.CoTaskMemFree
        CoTaskMemFree.restype = VOID

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAPI
        # CoFileTimeNow(
        # _Out_ FILETIME  FAR * lpFileTime
        # );
        CoFileTimeNow = ole32.CoFileTimeNow
        CoFileTimeNow.restype = WINOLEAPI

        # _Check_return_ WINOLEAPI
        # CLSIDFromProgIDEx(
        # _In_ LPCOLESTR lpszProgID,
        # _Out_ LPCLSID lpclsid
        # );
        CLSIDFromProgIDEx = ole32.CLSIDFromProgIDEx
        CLSIDFromProgIDEx.restype = WINOLEAPI

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if not defined(RC_INVOKED):
        from pyWinAPI.shared.poppack_h import * # NOQA
    # END IF   RC_INVOKED
# END IF   __COMBASEAPI_H__


