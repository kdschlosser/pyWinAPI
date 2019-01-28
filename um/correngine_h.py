import ctypes
import comtypes
import comtypes.automation
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

COMMETHOD = comtypes.COMMETHOD
IDispatch = comtypes.automation.IDispatch
helpstring = comtypes.helpstring

__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__correngine_h__ = None
__ICorrelationEngine_FWD_DEFINED__ = None
__CorrelationEngine_FWD_DEFINED__ = None
__ICorrelationEngine_INTERFACE_DEFINED__ = None
__CorrEngineLib_LIBRARY_DEFINED__ = None


def annotation(value):
    if '_opt_' in value:
        return comtypes.defaultvalue(None)
    else:
        return None


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 8.01.0622
# @@MIDL_FILE_HEADING( )
# verify that the <rpcndr.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    pass
# END IF


# verify that the <rpcsal.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCSAL_H_VERSION__):
    pass
# END IF


from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA
if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF  __RPCNDR_H_VERSION__

if not defined(COM_NO_WINDOWS_H):
    from pyWinAPI.um.windows_h import * # NOQA
    from pyWinAPI.um.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H


if not defined(__correngine_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__ICorrelationEngine_FWD_DEFINED__):
        class ICorrelationEngine(IDispatch):
            """
            ICorrelationEngine Interface
            """
            _case_insensitive_ = True
            _idlflags_ = ['dual', 'nonextensible']
            _iid_ = IID_ICorrelationEngine

    # END IF  __ICorrelationEngine_FWD_DEFINED__

    if not defined(__CorrelationEngine_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            class CorrelationEngine(object):
                pass
        # END IF  __cplusplus
    # END IF  __CorrelationEngine_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.oaidl_h import * # NOQA
    from pyWinAPI.um.ocidl_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_correngine_0000_0000
    # [local]
    # +
    # --------------------------------------------------------------------
    # Microsoft Windows
    # Copyright (C) Microsoft Corporation, 1992-2007.
    # ---------------------------------------------------------------------
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__ICorrelationEngine_INTERFACE_DEFINED__):
            # interface ICorrelationEngine
            # [unique][helpstring][nonextensible][dual][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ICorrelationEngine = MIDL_INTERFACE(
                    "{A188440E-DB11-45B8-B42C-B2149FA71453}"
                )
                ICorrelationEngine._iid_ = IID_ICorrelationEngine

                ICorrelationEngine._methods_ = [
                    COMMETHOD(
                        [
                            helpstring('Method get_RetainGlobalEvents'),
                            'propget',
                            'in'
                        ],
                        HRESULT,
                        'get_RetainGlobalEvents',
                        (['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal'),
                    ),
                    COMMETHOD(
                        [
                            helpstring('Method put_RetainGlobalEvents'),
                            'propput',
                            'in'
                        ],
                        HRESULT,
                        'put_RetainGlobalEvents',
                        (['in'], VARIANT_BOOL, 'newVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Filter')],
                        HRESULT,
                        'Filter',
                        (['in'], BSTR, 'InputTraceFile'),
                        (['in'], BSTR, 'OutputTraceFile'),
                        (['in'], BSTR, 'FilterActivityId'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Normalize')],
                        HRESULT,
                        'Normalize',
                        (['in'], BSTR, 'InputTraceFile'),
                        (['in'], BSTR, 'OutputTraceFile'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_RetainPII'), 'propget', 'in'],
                        HRESULT,
                        'get_RetainPII',
                        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method put_RetainPII'), 'propput', 'in'],
                        HRESULT,
                        'put_RetainPII',
                        (['in'], VARIANT_BOOL, 'newVal'),
                    ),
                    COMMETHOD(
                        [
                            helpstring('Method get_RetainCorrelationEvents'),
                            'propget',
                            'in'
                        ],
                        HRESULT,
                        'get_RetainCorrelationEvents',
                        (['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal'),
                    ),
                    COMMETHOD(
                        [
                            helpstring('Method put_RetainCorrelationEvents'),
                            'propput',
                            'in'
                        ],
                        HRESULT,
                        'put_RetainCorrelationEvents',
                        (['in'], VARIANT_BOOL, 'newVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ICorrelationEngine_INTERFACE_DEFINED__

        if not defined(__CorrEngineLib_LIBRARY_DEFINED__):
            # library CorrEngineLib
            # [helpstring][version][uuid]
            if defined(__cplusplus):
                pass
            # END IF

        # END IF  __CorrEngineLib_LIBRARY_DEFINED__

        # interface __MIDL_itf_correngine_0000_0002
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # Additional Prototypes for ALL interfaces
    oleaut32 = ctypes.windll.OLEAUT32

    # ULONG              BSTR_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize = oleaut32.BSTR_UserSize
    BSTR_UserSize.restype = ULONG

    # UCHAR *  BSTR_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal = oleaut32.BSTR_UserMarshal
    BSTR_UserMarshal.restype = UCHAR

    # UCHAR *  BSTR_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal = oleaut32.BSTR_UserUnmarshal
    BSTR_UserUnmarshal.restype = UCHAR

    # VOID                       BSTR_UserFree(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree = oleaut32.BSTR_UserFree
    BSTR_UserFree.restype = VOID

    # ULONG              BSTR_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize64 = oleaut32.BSTR_UserSize64
    BSTR_UserSize64.restype = ULONG

    # UCHAR *  BSTR_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal64 = oleaut32.BSTR_UserMarshal64
    BSTR_UserMarshal64.restype = UCHAR

    # UCHAR *  BSTR_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal64 = oleaut32.BSTR_UserUnmarshal64
    BSTR_UserUnmarshal64.restype = UCHAR

    # VOID                       BSTR_UserFree64(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree64 = oleaut32.BSTR_UserFree64
    BSTR_UserFree64.restype = VOID

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


