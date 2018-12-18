import ctypes
import comtypes
import comtypes.automation
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

IDispatch = comtypes.automation.IDispatch
COMMETHOD = comtypes.COMMETHOD
helpstring = comtypes.helpstring


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__dispex_h__ = None
__IDispatchEx_FWD_DEFINED__ = None
__IDispError_FWD_DEFINED__ = None
__IVariantChangeType_FWD_DEFINED__ = None
__IObjectIdentity_FWD_DEFINED__ = None
__ICanHandleException_FWD_DEFINED__ = None
__IProvideRuntimeContext_FWD_DEFINED__ = None
_NO_DISPATCHEX_CONSTS = None
__IDispatchEx_INTERFACE_DEFINED__ = None
__IDispError_INTERFACE_DEFINED__ = None
__IVariantChangeType_INTERFACE_DEFINED__ = None
__IObjectIdentity_INTERFACE_DEFINED__ = None
__ICanHandleException_INTERFACE_DEFINED__ = None
__IProvideRuntimeContext_INTERFACE_DEFINED__ = None
DISPEX_H_ = None
_NO_DISPATCHEX_GUIDS = None


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

if not defined(__dispex_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IDispatchEx_FWD_DEFINED__):

        class IDispatchEx(IDispatch):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None
    # END IF  __IDispatchEx_FWD_DEFINED__

    if not defined(__IDispError_FWD_DEFINED__):
        class IDispError(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IDispError_FWD_DEFINED__

    if not defined(__IVariantChangeType_FWD_DEFINED__):
        class IVariantChangeType(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IVariantChangeType_FWD_DEFINED__

    if not defined(__IObjectIdentity_FWD_DEFINED__):
        class IObjectIdentity(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IObjectIdentity_FWD_DEFINED__

    if not defined(__ICanHandleException_FWD_DEFINED__):
        class ICanHandleException(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICanHandleException_FWD_DEFINED__

    if not defined(__IProvideRuntimeContext_FWD_DEFINED__):
        class IProvideRuntimeContext(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IProvideRuntimeContext_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.ocidl_h import * # NOQA
    from pyWinAPI.um.oaidl_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_dispex_0000_0000
    # [local]
    # =-----------------------------------------------------------------------=
    # DispEx.h
    # =-----------------------------------------------------------------------=
    # (C Copyright 1997 Microsoft Corporation.  All Rights Reserved.
    # THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
    # ANY KIND EITHER EXPRESSED OR IMPIED, ICLUDING BUT NOT LIMITED TO
    # THE IMPIED WARRANTIES OF MERCHANTABIITY AND/OR FITNESS FOR A
    # PARTICUAR PURPOSE.
    # =-----------------------------------------------------------------------=

    # =-----------------------------------------------------------------------=
    # IDISPATCHEX INTERFACES.

    if not defined(DISPEX_H_):
        DISPEX_H_ = VOID
        from pyWinAPI.shared.winapifamily_h import * # NOQA

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            from pyWinAPI.um.servprov_h import * # NOQA

            if not defined(_NO_DISPATCHEX_GUIDS):

                # {A6EF9860-C720-11D0-9337-00A0C90DCAA9}
                IID_IDispatchEx = DEFINE_GUID(
                    0xA6EF9860,
                    0xC720,
                    0x11D0,
                    0x93,
                    0x37,
                    0x0,
                    0xA0,
                    0xC9,
                    0xD,
                    0xCA,
                    0xA9
                )
                # {A6EF9861-C720-11d0-9337-00A0C90DCAA9}
                IID_IDispError = DEFINE_GUID(
                    0xA6EF9861,
                    0xC720,
                    0x11D0,
                    0x93,
                    0x37,
                    0x0,
                    0xA0,
                    0xC9,
                    0xD,
                    0xCA,
                    0xA9
                )
                # {A6EF9862-C720-11d0-9337-00A0C90DCAA9}
                IID_IVariantChangeType = DEFINE_GUID(
                    0xA6EF9862,
                    0xC720,
                    0x11D0,
                    0x93,
                    0x37,
                    0x0,
                    0xA0,
                    0xC9,
                    0xD,
                    0xCA,
                    0xA9
                )
                # {1F101481-BCCD-11d0-9336-00A0C90DCAA9}
                SID_VariantConversion = DEFINE_GUID(
                    0x1F101481,
                    0xBCCD,
                    0x11D0,
                    0x93,
                    0x36,
                    0x0,
                    0xA0,
                    0xC9,
                    0xD,
                    0xCA,
                    0xA9
                )
                # {4717CC40-BCB9-11d0-9336-00A0C90DCAA9}
                SID_GetCaller = DEFINE_GUID(
                    0x4717CC40,
                    0xBCB9,
                    0x11D0,
                    0x93,
                    0x36,
                    0x0,
                    0xA0,
                    0xC9,
                    0xD,
                    0xCA,
                    0xA9
                )
                # {74A5040C-DD0C-48f0-AC85-194C3259180A}
                SID_ProvideRuntimeContext = DEFINE_GUID(
                    0x74A5040C,
                    0xDD0C,
                    0x48F0,
                    0xAC,
                    0x85,
                    0x19,
                    0x4C,
                    0x32,
                    0x59,
                    0x18,
                    0xA
                )
                # {10E2414A-EC59-49d2-BC51-5ADD2C36FEBC}
                IID_IProvideRuntimeContext = DEFINE_GUID(
                    0x10E2414A,
                    0xEC59,
                    0x49D2,
                    0xBC,
                    0x51,
                    0x5A,
                    0xDD,
                    0x2C,
                    0x36,
                    0xFE,
                    0xBC
                )
                # {CA04B7E6-0D21-11d1-8CC5-00C04FC2B085}
                IID_IObjectIdentity = DEFINE_GUID(
                    0xCA04B7E6,
                    0xD21,
                    0x11D1,
                    0x8C,
                    0xC5,
                    0x0,
                    0xC0,
                    0x4F,
                    0xC2,
                    0xB0,
                    0x85
                )
                # {c5598e60-b307-11d1-b27d-006008c3fbfb}
                IID_ICanHandleException = DEFINE_GUID(
                    0xC5598E60,
                    0xB307,
                    0x11D1,
                    0xB2,
                    0x7D,
                    0x0,
                    0x60,
                    0x08,
                    0xC3,
                    0xFB,
                    0xFB
                )
            # END IF   _NO_DISPATCHEX_GUIDS

            if not defined(_NO_DISPATCHEX_CONSTS):
                # Input flags for GetDispID
                # Output flags for GetMemberProperties
                # Input flags for GetNextDispID
                # Additional flags for Invoke - when object member is
                # used as a constructor.
                # Standard DISPIDs
                fdexPropCanGet = 0x00000001
                fdexPropCannotGet = 0x00000002
                fdexPropCanPut = 0x00000004
                fdexPropCannotPut = 0x00000008
                fdexPropCanPutRef = 0x00000010
                fdexPropCannotPutRef = 0x00000020
                fdexPropNoSideEffects = 0x00000040
                fdexPropDynamicType = 0x00000080
                fdexPropCanCall = 0x00000100
                fdexPropCannotCall = 0x00000200
                fdexPropCanConstruct = 0x00000400
                fdexPropCannotConstruct = 0x00000800
                fdexPropCanSourceEvents = 0x00001000
                fdexPropCannotSourceEvents = 0x00002000

                grfdexPropCanAll = (
                    fdexPropCanGet |
                    fdexPropCanPut |
                    fdexPropCanPutRef |
                    fdexPropCanCall |
                    fdexPropCanConstruct |
                    fdexPropCanSourceEvents
                )
                grfdexPropCannotAll = (
                    fdexPropCannotGet |
                    fdexPropCannotPut |
                    fdexPropCannotPutRef |
                    fdexPropCannotCall |
                    fdexPropCannotConstruct |
                    fdexPropCannotSourceEvents
                )
                grfdexPropExtraAll = (
                    fdexPropNoSideEffects |
                    fdexPropDynamicType
                )
                grfdexPropAll = (
                    grfdexPropCanAll |
                    grfdexPropCannotAll |
                    grfdexPropExtraAll
                )

                # Input flags for GetNextDispID
                fdexEnumDefault = 0x00000001
                fdexEnumAll = 0x00000002

                # Additional flags for Invoke - when object member is used as a
                # constructor.
                DISPATCH_CONSTRUCT = 0x4000

                # Standard DISPIDs
                DISPID_THIS = -613
                DISPID_STARTENUM = DISPID_UNKNOWN

            # END IF  _NO_DISPATCHEX_CONSTS

            if not defined(__IDispatchEx_INTERFACE_DEFINED__):
                # interface IDispatchEx
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IDispatchEx = MIDL_INTERFACE(
                        "{A6EF9860-C720-11D0-9337-00A0C90DCAA9}"
                    )
                    IDispatchEx._iid_ = IID_IDispatchEx

                    IDispatchEx._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetDispID')],
                            HRESULT,
                            'GetDispID',
                            (['in'], BSTR, 'bstrName'),
                            (['in'], DWORD, 'grfdex'),
                            (['out'], POINTER(DISPID), 'pid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method InvokeEx'), 'local'],
                            HRESULT,
                            'InvokeEx',
                            (['in'], DISPID, 'id'),
                            (['in'], LCID, 'lcid'),
                            (['in'], WORD, 'wFlags'),
                            (['in'], POINTER(DISPPARAMS), 'pdp'),
                            (['out'], POINTER(VARIANT), 'pvarRes'),
                            (['out'], POINTER(EXCEPINFO), 'pei'),
                            (['in'], POINTER(IServiceProvider), 'pspCaller'),
                        ),
                        COMMETHOD(
                            [helpstring('Method DeleteMemberByName')],
                            HRESULT,
                            'DeleteMemberByName',
                            (['in'], BSTR, 'bstrName'),
                            (['in'], DWORD, 'grfdex'),
                        ),
                        COMMETHOD(
                            [helpstring('Method DeleteMemberByDispID')],
                            HRESULT,
                            'DeleteMemberByDispID',
                            (['in'], DISPID, 'id'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMemberProperties')],
                            HRESULT,
                            'GetMemberProperties',
                            (['in'], DISPID, 'id'),
                            (['in'], DWORD, 'grfdexFetch'),
                            (['out'], POINTER(DWORD), 'pgrfdex'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMemberName')],
                            HRESULT,
                            'GetMemberName',
                            (['in'], DISPID, 'id'),
                            (['out'], POINTER(BSTR), 'pbstrName'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetNextDispID')],
                            HRESULT,
                            'GetNextDispID',
                            (['in'], DWORD, 'grfdex'),
                            (['in'], DISPID, 'id'),
                            (['out'], POINTER(DISPID), 'pid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetNameSpaceParent')],
                            HRESULT,
                            'GetNameSpaceParent',
                            (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppunk'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IDispatchEx_INTERFACE_DEFINED__

            if not defined(__IDispError_INTERFACE_DEFINED__):
                # interface IDispError
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IDispError = MIDL_INTERFACE(
                        "{A6EF9861-C720-11D0-9337-00A0C90DCAA9}"
                    )
                    IDispError._iid_ = IID_IDispError

                    IDispError._methods_ = [
                        COMMETHOD(
                            [helpstring('Method QueryErrorInfo')],
                            HRESULT,
                            'QueryErrorInfo',
                            (['in'], GUID, 'guidErrorType'),
                            (['out'], POINTER(POINTER(IDispError)), 'ppde'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetNext')],
                            HRESULT,
                            'GetNext',
                            (['out'], POINTER(POINTER(IDispError)), 'ppde'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetHresult')],
                            HRESULT,
                            'GetHresult',
                            (['out'], POINTER(HRESULT), 'phr'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSource')],
                            HRESULT,
                            'GetSource',
                            (['out'], POINTER(BSTR), 'pbstrSource'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetHelpInfo')],
                            HRESULT,
                            'GetHelpInfo',
                            (['out'], POINTER(BSTR), 'pbstrFileName'),
                            (['out'], POINTER(DWORD), 'pdwContext'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDescription')],
                            HRESULT,
                            'GetDescription',
                            (['out'], POINTER(BSTR), 'pbstrDescription'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IDispError_INTERFACE_DEFINED__

            if not defined(__IVariantChangeType_INTERFACE_DEFINED__):
                # interface IVariantChangeType
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IVariantChangeType = MIDL_INTERFACE(
                        "{A6EF9862-C720-11D0-9337-00A0C90DCAA9}"
                    )
                    IVariantChangeType._iid_ = IID_IVariantChangeType

                    IVariantChangeType._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ChangeType')],
                            HRESULT,
                            'ChangeType',
                            (['unique', 'out', 'in'], POINTER(VARIANT), 'pvarDst'),
                            (['unique', 'in'], POINTER(VARIANT), 'pvarSrc'),
                            (['in'], LCID, 'lcid'),
                            (['in'], VARTYPE, 'vtNew'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IVariantChangeType_INTERFACE_DEFINED__

            if not defined(__IObjectIdentity_INTERFACE_DEFINED__):
                # interface IObjectIdentity
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IObjectIdentity = MIDL_INTERFACE(
                        "{CA04B7E6-0D21-11D1-8CC5-00C04FC2B085}"
                    )
                    IObjectIdentity._iid_ = IID_IObjectIdentity

                    IObjectIdentity._methods_ = [
                        COMMETHOD(
                            [helpstring('Method IsEqualObject')],
                            HRESULT,
                            'IsEqualObject',
                            (['in'], POINTER(comtypes.IUnknown), 'punk'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IObjectIdentity_INTERFACE_DEFINED__

            if not defined(__ICanHandleException_INTERFACE_DEFINED__):
                # interface ICanHandleException
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_ICanHandleException = MIDL_INTERFACE(
                        "{C5598E60-B307-11D1-B27D-006008C3FBFB}"
                    )
                    ICanHandleException._iid_ = IID_ICanHandleException

                    ICanHandleException._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CanHandleException')],
                            HRESULT,
                            'CanHandleException',
                            (['in'], POINTER(EXCEPINFO), 'pExcepInfo'),
                            (['in'], POINTER(VARIANT), 'pvar'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __ICanHandleException_INTERFACE_DEFINED__

            if not defined(__IProvideRuntimeContext_INTERFACE_DEFINED__):
                # interface IProvideRuntimeContext
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IProvideRuntimeContext = MIDL_INTERFACE(
                        "{10E2414A-EC59-49D2-BC51-5ADD2C36FEBC}"
                    )
                    IProvideRuntimeContext._iid_ = IID_IProvideRuntimeContext

                    IProvideRuntimeContext._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCurrentSourceContext')],
                            HRESULT,
                            'GetCurrentSourceContext',
                            (['out'], POINTER(DWORD_PTR), 'pdwContext'),
                            (['out'], POINTER(VARIANT_BOOL), 'pfExecutingGlobalCode'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IProvideRuntimeContext_INTERFACE_DEFINED__

            # interface __MIDL_itf_dispex_0000_0006
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # END IF  DISPEX_H_

    # Additional Prototypes for ALL interfaces
    oleaut32 = ctypes.windll.OLEAUT32

    # ULONG BSTR_UserSize( __RPC__in ULONG *, ULONG, __RPC__in BSTR * );
    BSTR_UserSize = oleaut32.BSTR_UserSize
    BSTR_UserSize.restype = ULONG

    # UCHAR *  BSTR_UserMarshal(
    #  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal = oleaut32.BSTR_UserMarshal
    BSTR_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR * BSTR_UserUnmarshal(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal = oleaut32.BSTR_UserUnmarshal
    BSTR_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID BSTR_UserFree(__RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree = oleaut32.BSTR_UserFree
    BSTR_UserFree.restype = VOID

    # ULONG VARIANT_UserSize(__RPC__in ULONG *, ULONG, __RPC__in VARIANT * );
    VARIANT_UserSize = oleaut32.VARIANT_UserSize
    VARIANT_UserSize.restype = ULONG

    # UCHAR * VARIANT_UserMarshal(
    # __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in VARIANT * );
    VARIANT_UserMarshal = oleaut32.VARIANT_UserMarshal
    VARIANT_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR * VARIANT_UserUnmarshal(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out VARIANT * );
    VARIANT_UserUnmarshal = oleaut32.VARIANT_UserUnmarshal
    VARIANT_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID VARIANT_UserFree(__RPC__in ULONG *, __RPC__in VARIANT * );
    VARIANT_UserFree = oleaut32.VARIANT_UserFree
    VARIANT_UserFree.restype = VOID

    # ULONG BSTR_UserSize64(__RPC__in ULONG *, ULONG, __RPC__in BSTR * );
    BSTR_UserSize64 = oleaut32.BSTR_UserSize64
    BSTR_UserSize64.restype = ULONG

    # UCHAR *  BSTR_UserMarshal64(
    # __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal64 = oleaut32.BSTR_UserMarshal64
    BSTR_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR * BSTR_UserUnmarshal64(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal64 = oleaut32.BSTR_UserUnmarshal64
    BSTR_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID BSTR_UserFree64(__RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree64 = oleaut32.BSTR_UserFree64
    BSTR_UserFree64.restype = VOID

    # ULONG VARIANT_UserSize64(__RPC__in ULONG *, ULONG, __RPC__in VARIANT * );
    VARIANT_UserSize64 = oleaut32.VARIANT_UserSize64
    VARIANT_UserSize64.restype = ULONG

    # UCHAR *  VARIANT_UserMarshal64(
    # __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in VARIANT * );
    VARIANT_UserMarshal64 = oleaut32.VARIANT_UserMarshal64
    VARIANT_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  VARIANT_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out VARIANT * );
    VARIANT_UserUnmarshal64 = oleaut32.VARIANT_UserUnmarshal64
    VARIANT_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID VARIANT_UserFree64(     __RPC__in ULONG *, __RPC__in VARIANT * );
    VARIANT_UserFree64 = oleaut32.VARIANT_UserFree64
    VARIANT_UserFree64.restype = VOID

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


