import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *

# + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.
# File:  basetyps.h
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#

_BASETYPS_H_ = None
if not defined( _BASETYPS_H_ ):
    _BASETYPS_H_ = 1
    if _MSC_VER > 1000:
        pass
    # END IF

    # Common macros gleamed from COMPOBJ.H
    if defined(__cplusplus):
        EXTERN_C = None
    else:
        EXTERN_C = None
    # END IF

    if defined(_WIN32):
        # Win32 doesn't support
        def STDMETHODCALLTYPE(idl_flags, res_type, func_name):
            return comtypes.COMMETHOD(idl_flags, res_type, func_name)


        def STDMETHODVCALLTYPE(idl_flags, res_type, func_name, *args):
            return comtypes.COMMETHOD(idl_flags, res_type, func_name, *args)


        def STDAPICALLTYPE(restype):
            return comtypes.CFUNCTYPE(restype)


        def STDAPIVCALLTYPE(restype, *argtypes):
            return comtypes.CFUNCTYPE(restype, *argtypes)

    else:
        def STDMETHODCALLTYPE(idl_flags, res_type, func_name):
            return comtypes.COMMETHOD(idl_flags, res_type, func_name)


        def STDMETHODVCALLTYPE(idl_flags, res_type, func_name, *args):
            return comtypes.COMMETHOD(idl_flags, res_type, func_name, *args)


        def STDAPICALLTYPE(restype):
            return comtypes.CFUNCTYPE(restype)


        def STDAPIVCALLTYPE(restype, *argtypes):
            return comtypes.CFUNCTYPE(restype, *argtypes)
    # END IF

    def STDAPI():
        return STDAPICALLTYPE(HRESULT)

    def STDAPI_(type):
        return STDAPICALLTYPE(type)

    def STDMETHODIMP(method_name):
        return STDMETHODCALLTYPE([], HRESULT, method_name)

    def STDMETHODIMP_(type, method_name):
        return STDMETHODCALLTYPE([], type, method_name)

    # The 'V' versions allow Variable Argument lists.

    def STDAPIV(*args):
        return STDAPIVCALLTYPE(HRESULT, *args)

    def STDAPIV_(type, *args):
        return STDAPIVCALLTYPE(type, *args)

    def STDMETHODIMPV(method_name, *args):
        return STDMETHODCALLTYPE([], HRESULT, method_name, *args)


    def STDMETHODIMPV_(type, method_name, *args):
        return STDMETHODCALLTYPE([], type, method_name, *args)

    # **** Interface Declaration *********************************************
    # /*  These are macros for declaring interfaces. They exist so that  a
    # single definition of the interface is simulataneously a proper
    # declaration of the interface structures (C + + abstract classes) for
    # both C and C + + . DECLARE_INTERFACE(iface) is used to declare an
    # interface that does not derive from a base interface.
    # DECLARE_INTERFACE_(iface, baseiface) is used to declare an interface
    # that does derive from a base interface. By default if the source file
    # has a .c extension the C version of the interface declaratations will be
    # expanded; if it has a .cpp extension the C + + version will be expanded.
    # if you want to force the C version expansion even though the source file
    # has a .cpp extension, then define the macro "CINTERFACE". eg. cl -
    # DCINTERFACE file.cpp Example Interface declaration: undef INTERFACE
    # define INTERFACE IClassFactory
    # DECLARE_INTERFACE_(IClassFactory, IUnknown)
    # { // *** IUnknown methods *** STDMETHOD(QueryInterface) (
    # THIS_ REFIID riid, LPVOID FAR* ppvObj) PURE;
    # STDMETHOD_(ULONG,AddRef) (THIS) PURE;
    # STDMETHOD_(ULONG,Release) (THIS) PURE;
    # // *** IClassFactory methods *** STDMETHOD(CreateInstance) (
    # THIS_ LPUNKNOWN pUnkOuter,
    #  REFIID riid,
    # LPVOID FAR* ppvObject) PURE; };
    #
    # Example C + + expansion: struct FAR IClassFactory : public IUnknown {
    # virtual HRESULT STDMETHODCALLTYPE QueryInterface(
    #  IID FAR& riid,
    # LPVOID FAR* ppvObj) = 0;
    #  virtual HRESULT STDMETHODCALLTYPE AddRef(VOID) = 0;
    #  virtual HRESULT STDMETHODCALLTYPE Release(VOID) = 0;
    #  virtual HRESULT STDMETHODCALLTYPE CreateInstance(
    # LPUNKNOWN pUnkOuter,
    # IID FAR& riid,
    # LPVOID FAR* ppvObject) = 0;
    # }; NOTE: Our documentation says 'define interface class'
    # but we use 'struct' instead of 'class' to keep a lot of 'public:'
    # lines out of the interfaces. The 'FAR' forces the 'this' pointers to be
    # far, which is what we need. Example C expansion: typedef struct
    # IClassFactory { struct IClassFactoryVtbl FAR* lpVtbl; } IClassFactory;
    # typedef struct IClassFactoryVtbl IClassFactoryVtbl; struct
    # IClassFactoryVtbl { HRESULT (STDMETHODCALLTYPE * QueryInterface) (
    # IClassFactory FAR* This, IID FAR* riid, LPVOID FAR* ppvObj) ; HRESULT
    # (STDMETHODCALLTYPE * AddRef) (IClassFactory FAR* This) ; HRESULT
    # (STDMETHODCALLTYPE * Release) (IClassFactory FAR* This) ; HRESULT
    # (STDMETHODCALLTYPE * CreateInstance) ( IClassFactory FAR* This,
    # LPUNKNOWN pUnkOuter, IID FAR* riid, LPVOID FAR* ppvObject); HRESULT
    # (STDMETHODCALLTYPE * LockServer) ( IClassFactory FAR* This, BOOL fLock);
    #  };
    #
    if defined(__cplusplus) and not defined(CINTERFACE):
        # define interface   struct FAR

        COM_STDMETHOD_CAN_THROW = None
        if defined(COM_STDMETHOD_CAN_THROW):
            COM_DECLSPEC_NOTHROW = 1
        else:
            COM_DECLSPEC_NOTHROW = DECLSPEC_NOTHROW

        # END IF
        __STRUCT__ = ctypes.Structure
        interface = __STRUCT__


        def STDMETHOD(method):
            return STDMETHODCALLTYPE(HRESULT, method)


        def STDMETHOD_(type, method):
            return STDMETHODCALLTYPE(type, method)


        def STDMETHODV(method):
            def wrapper(*args):
                return STDMETHODVCALLTYPE(HRESULT, method, *args)
            return wrapper


        def STDMETHODV_(type, method):
            def wrapper(*args):
                return STDMETHODVCALLTYPE(type, method, *args)

            return wrapper


        PURE = 0
        THIS_ = 1
        THIS = VOID


        def DECLARE_INTERFACE(iface):
            class Wrapper(interface):
                __name__ = iface.__name__
                __dict__ = iface.__dict__

            return Wrapper

        def DECLARE_INTERFACE_(iface, baseiface):

            class Wrapper(baseiface, iface):
                __name__ = iface.__name__
                __dict__ = iface.__dict__

            return Wrapper


        def IFACEMETHOD(method):
            return STDMETHOD(method)


        def IFACEMETHOD_(type, method):
            return STDMETHOD_(type, method)


        def IFACEMETHODV(method):
            return STDMETHODV(method)

        def IFACEMETHODV_(type, method):
            return STDMETHODV_(type, method)
    else:
        interface = ctypes.Structure


        def STDMETHOD(method):
            return STDMETHODCALLTYPE(HRESULT, method)


        def STDMETHOD_(type, method):
            return STDMETHODCALLTYPE(type, method)


        def STDMETHODV(method):
            return STDMETHODVCALLTYPE(HRESULT, method)


        def STDMETHODV_(type, method):
            return STDMETHODVCALLTYPE(type, method)


        def IFACEMETHOD(method):
            return STDMETHOD(method)


        def IFACEMETHOD_(type, method):
            return STDMETHOD_(type, method)


        def IFACEMETHODV(method):
            return STDMETHODV(method)


        def IFACEMETHODV_(type, method):
            return STDMETHODV_(type,method)

        PURE = 1
        THIS_ = INTERFACE
        THIS = INTERFACE

        CONST_VTABLE = None
        if defined(CONST_VTABLE):
            def DECLARE_INTERFACE(iface):
                class Wrapper(interface):
                    __name__ = iface.__name__
                    __dict__ = iface.__dict__


                return Wrapper

        else:
            def DECLARE_INTERFACE(iface):
                class Wrapper(interface):
                    __name__ = iface.__name__
                    __dict__ = iface.__dict__


                return Wrapper
        # END IF

        def DECLARE_INTERFACE_(iface, baseiface):

            class Wrapper(baseiface, iface):
                __name__ = iface.__name__
                __dict__ = iface.__dict__


            return Wrapper

    # END IF
    from pyWinAPI.shared.guiddef_h import * # NOQA


    _ERROR_STATUS_T_DEFINED = None
    if not defined(_ERROR_STATUS_T_DEFINED):
        _ERROR_STATUS_T_DEFINED = 1
    # END IF

    _WCHAR_T_DEFINED = None
    if not defined(_WCHAR_T_DEFINED):
        _WCHAR_T_DEFINED = 1
    # END IF

# END IF
