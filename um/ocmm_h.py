import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


COMMETHOD = comtypes.COMMETHOD
helpstring = comtypes.helpstring


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__ocmm_h__ = None
__ITimerService_FWD_DEFINED__ = None
__ITimer_FWD_DEFINED__ = None
__ITimerEx_FWD_DEFINED__ = None
__ITimerSink_FWD_DEFINED__ = None
__IMapMIMEToCLSID_FWD_DEFINED__ = None
__IImageDecodeFilter_FWD_DEFINED__ = None
__IImageDecodeEventSink_FWD_DEFINED__ = None
__IImageDecodeEventSink2_FWD_DEFINED__ = None
RGBQUAD_DEFINED = None
__ITimerService_INTERFACE_DEFINED__ = None
__ITimer_INTERFACE_DEFINED__ = None
__ITimerEx_INTERFACE_DEFINED__ = None
__ITimerSink_INTERFACE_DEFINED__ = None
__IMapMIMEToCLSID_INTERFACE_DEFINED__ = None
__IImageDecodeFilter_INTERFACE_DEFINED__ = None
__IImageDecodeEventSink_INTERFACE_DEFINED__ = None
__IImageDecodeEventSink2_INTERFACE_DEFINED__ = None


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


if not defined(__ocmm_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__ITimerService_FWD_DEFINED__):
        class ITimerService(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITimerService_FWD_DEFINED__

    if not defined(__ITimer_FWD_DEFINED__):
        class ITimer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITimer_FWD_DEFINED__

    if not defined(__ITimerEx_FWD_DEFINED__):
        class ITimerEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITimerEx_FWD_DEFINED__

    if not defined(__ITimerSink_FWD_DEFINED__):
        class ITimerSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITimerSink_FWD_DEFINED__

    if not defined(__IMapMIMEToCLSID_FWD_DEFINED__):
        class IMapMIMEToCLSID(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMapMIMEToCLSID_FWD_DEFINED__

    if not defined(__IImageDecodeFilter_FWD_DEFINED__):
        class IImageDecodeFilter(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IImageDecodeFilter_FWD_DEFINED__

    if not defined(__IImageDecodeEventSink_FWD_DEFINED__):
        class IImageDecodeEventSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IImageDecodeEventSink_FWD_DEFINED__

    if not defined(__IImageDecodeEventSink2_FWD_DEFINED__):
        class IImageDecodeEventSink2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IImageDecodeEventSink2_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.oaidl_h import * # NOQA
    from pyWinAPI.um.oleidl_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_ocmm_0000_0000
    # [local]
    # =--------------------------------------------------------------------------=
    #
    # ocmm.h
    # =--------------------------------------------------------------------------=
    #
    # (C) Copyright Microsoft Corporation. All Rights Reserved.
    # THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
    # ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
    # THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
    # PARTICULAR PURPOSE.
    # =--------------------------------------------------------------------------=
    #
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        BFID = GUID
        if not defined(RGBQUAD_DEFINED):
            RGBQUAD = tagRGBQUAD

        # END IF

        if not defined(__ITimerService_INTERFACE_DEFINED__):
            # interface ITimerService
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITimerService = MIDL_INTERFACE(
                    "{3050F35F-98B5-11CF-BB82-00AA00BDCE0B}"
                )
                ITimerService._iid_ = IID_ITimerService

                ITimerService._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateTimer')],
                        HRESULT,
                        'CreateTimer',
                        (['in'], POINTER(ITimer), 'pReferenceTimer'),
                        (['out'], POINTER(POINTER(ITimer)), 'ppNewTimer'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetNamedTimer')],
                        HRESULT,
                        'GetNamedTimer',
                        (['in'], REFGUID, 'rguidName'),
                        (['out'], POINTER(POINTER(ITimer)), 'ppTimer'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetNamedTimerReference')],
                        HRESULT,
                        'SetNamedTimerReference',
                        (['in'], REFGUID, 'rguidName'),
                        (['in'], POINTER(ITimer), 'pReferenceTimer'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITimerService_INTERFACE_DEFINED__

        if not defined(__ITimer_INTERFACE_DEFINED__):
            # interface ITimer
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITimer = MIDL_INTERFACE(
                    "{3050F360-98B5-11CF-BB82-00AA00BDCE0B}"
                )
                ITimer._iid_ = IID_ITimer

                ITimer._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Advise')],
                        HRESULT,
                        'Advise',
                        (['in'], VARIANT, 'vtimeMin'),
                        (['in'], VARIANT, 'vtimeMax'),
                        (['in'], VARIANT, 'vtimeInterval'),
                        (['in'], DWORD, 'dwFlags'),
                        (['in'], POINTER(ITimerSink), 'pTimerSink'),
                        (['out'], POINTER(DWORD), 'pdwCookie'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Unadvise')],
                        HRESULT,
                        'Unadvise',
                        (['in'], DWORD, 'dwCookie'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Freeze')],
                        HRESULT,
                        'Freeze',
                        (['in'], BOOL, 'fFreeze'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTime')],
                        HRESULT,
                        'GetTime',
                        (['out'], POINTER(VARIANT), 'pvtime'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITimer_INTERFACE_DEFINED__

        if not defined(__ITimerEx_INTERFACE_DEFINED__):
            # interface ITimerEx
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITimerEx = MIDL_INTERFACE(
                    "{30510414-98B5-11CF-BB82-00AA00BDCE0B}"
                )
                ITimerEx._iid_ = IID_ITimerEx

                ITimerEx._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetMode')],
                        HRESULT,
                        'SetMode',
                        (['in'], DWORD, 'dwMode'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITimerEx_INTERFACE_DEFINED__

        if not defined(__ITimerSink_INTERFACE_DEFINED__):
            # interface ITimerSink
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITimerSink = MIDL_INTERFACE(
                    "{3050F361-98B5-11CF-BB82-00AA00BDCE0B}"
                )
                ITimerSink._iid_ = IID_ITimerSink

                ITimerSink._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnTimer')],
                        HRESULT,
                        'OnTimer',
                        (['in'], VARIANT, 'vtimeAdvise'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITimerSink_INTERFACE_DEFINED__

        # interface __MIDL_itf_ocmm_0000_0004
        # [local]
        if not defined(__IMapMIMEToCLSID_INTERFACE_DEFINED__):
            # interface IMapMIMEToCLSID
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMapMIMEToCLSID = MIDL_INTERFACE(
                    "{D9E89500-30FA-11D0-B724-00AA006C1A01}"
                )
                IMapMIMEToCLSID._iid_ = IID_IMapMIMEToCLSID

                IMapMIMEToCLSID._methods_ = [
                    COMMETHOD(
                        [helpstring('Method EnableDefaultMappings')],
                        HRESULT,
                        'EnableDefaultMappings',
                        ([], BOOL, 'bEnable'),
                    ),
                    COMMETHOD(
                        [helpstring('Method MapMIMEToCLSID')],
                        HRESULT,
                        'MapMIMEToCLSID',
                        (['in'], LPCOLESTR, 'pszMIMEType'),
                        (['in'], POINTER(CLSID), 'pCLSID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetMapping')],
                        HRESULT,
                        'SetMapping',
                        (['in'], LPCOLESTR, 'pszMIMEType'),
                        ([], DWORD, 'dwMapMode'),
                        (['in'], REFCLSID, 'clsid'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMapMIMEToCLSID_INTERFACE_DEFINED__

        if not defined(__IImageDecodeFilter_INTERFACE_DEFINED__):
            # interface IImageDecodeFilter
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IImageDecodeFilter = MIDL_INTERFACE(
                    "{A3CCEDF3-2DE2-11D0-86F4-00A0C913F750}"
                )
                IImageDecodeFilter._iid_ = IID_IImageDecodeFilter

                IImageDecodeFilter._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Initialize')],
                        HRESULT,
                        'Initialize',
                        (
                            ['in'],
                            POINTER(IImageDecodeEventSink),
                           'pEventSink'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Process')],
                        HRESULT,
                        'Process',
                        (['in'], POINTER(IStream), 'pStream'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Terminate')],
                        HRESULT,
                        'Terminate',
                        ([], HRESULT, 'hrStatus'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IImageDecodeFilter_INTERFACE_DEFINED__

        if not defined(__IImageDecodeEventSink_INTERFACE_DEFINED__):
            # interface IImageDecodeEventSink
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IImageDecodeEventSink = MIDL_INTERFACE(
                    "{BAA342A0-2DED-11D0-86F4-00A0C913F750}"
                )
                IImageDecodeEventSink._iid_ = IID_IImageDecodeEventSink

                IImageDecodeEventSink._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetSurface')],
                        HRESULT,
                        'GetSurface',
                        (['in'], LONG, 'nWidth'),
                        (['in'], LONG, 'nHeight'),
                        (['in'], REFGUID, 'bfid'),
                        (['in'], ULONG, 'nPasses'),
                        (['in'], DWORD, 'dwHints'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppSurface'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnBeginDecode')],
                        HRESULT,
                        'OnBeginDecode',
                        (['out'], POINTER(DWORD), 'pdwEvents'),
                        (['out'], POINTER(ULONG), 'pnFormats'),
                        (['out'], POINTER(POINTER(BFID)), 'ppFormats'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnBitsComplete')],
                        HRESULT,
                        'OnBitsComplete',
                    ),
                    COMMETHOD(
                        [helpstring('Method OnDecodeComplete')],
                        HRESULT,
                        'OnDecodeComplete',
                        (['in'], HRESULT, 'hrStatus'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnPalette')],
                        HRESULT,
                        'OnPalette',
                    ),
                    COMMETHOD(
                        [helpstring('Method OnProgress')],
                        HRESULT,
                        'OnProgress',
                        (['in'], POINTER(RECT), 'pBounds'),
                        (['in'], BOOL, 'bComplete'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IImageDecodeEventSink_INTERFACE_DEFINED__

        if not defined(__IImageDecodeEventSink2_INTERFACE_DEFINED__):
            # interface IImageDecodeEventSink2
            # [unique][helpstring][uuid][local][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IImageDecodeEventSink2 = MIDL_INTERFACE(
                    "{8EBD8A57-8A96-48C9-84A6-962E2DB9C931}"
                )
                IImageDecodeEventSink2._iid_ = IID_IImageDecodeEventSink2

                IImageDecodeEventSink2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method IsAlphaPremultRequired')],
                        HRESULT,
                        'IsAlphaPremultRequired',
                        (['out'], POINTER(BOOL), 'pfPremultAlpha'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IImageDecodeEventSink2_INTERFACE_DEFINED__

        # interface __MIDL_itf_ocmm_0000_0008
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # Additional Prototypes for ALL interfaces
    oleaut32 = ctypes.windll.OLEAUT32

    # ULONG              VARIANT_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in VARIANT * );
    VARIANT_UserSize = oleaut32.VARIANT_UserSize
    VARIANT_UserSize.restype = ULONG

    # UCHAR *  VARIANT_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in VARIANT * );
    VARIANT_UserMarshal = oleaut32.VARIANT_UserMarshal
    VARIANT_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  VARIANT_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out VARIANT * );
    VARIANT_UserUnmarshal = oleaut32.VARIANT_UserUnmarshal
    VARIANT_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       VARIANT_UserFree(     __RPC__in ULONG *, __RPC__in VARIANT * );
    VARIANT_UserFree = oleaut32.VARIANT_UserFree
    VARIANT_UserFree.restype = VOID

    # ULONG              VARIANT_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in VARIANT * );
    VARIANT_UserSize64 = oleaut32.VARIANT_UserSize64
    VARIANT_UserSize64.restype = ULONG

    # UCHAR *  VARIANT_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in VARIANT * );
    VARIANT_UserMarshal64 = oleaut32.VARIANT_UserMarshal64
    VARIANT_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  VARIANT_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out VARIANT * );
    VARIANT_UserUnmarshal64 = oleaut32.VARIANT_UserUnmarshal64
    VARIANT_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       VARIANT_UserFree64(     __RPC__in ULONG *, __RPC__in VARIANT * );
    VARIANT_UserFree64 = oleaut32.VARIANT_UserFree64
    VARIANT_UserFree64.restype = VOID

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


