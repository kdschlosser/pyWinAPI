import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


COMMETHOD = comtypes.COMMETHOD


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__mfobjects_h__ = None
__IMFAttributes_FWD_DEFINED__ = None
__IMFMediaBuffer_FWD_DEFINED__ = None
__IMFSample_FWD_DEFINED__ = None
__IMF2DBuffer_FWD_DEFINED__ = None
__IMF2DBuffer2_FWD_DEFINED__ = None
__IMFDXGIBuffer_FWD_DEFINED__ = None
__IMFMediaType_FWD_DEFINED__ = None
__IMFAudioMediaType_FWD_DEFINED__ = None
__IMFVideoMediaType_FWD_DEFINED__ = None
__IMFAsyncResult_FWD_DEFINED__ = None
__IMFAsyncCallback_FWD_DEFINED__ = None
__IMFAsyncCallbackLogging_FWD_DEFINED__ = None
__IMFMediaEvent_FWD_DEFINED__ = None
__IMFMediaEventGenerator_FWD_DEFINED__ = None
__IMFRemoteAsyncCallback_FWD_DEFINED__ = None
__IMFByteStream_FWD_DEFINED__ = None
__IMFByteStreamProxyClassFactory_FWD_DEFINED__ = None
__IMFSampleOutputStream_FWD_DEFINED__ = None
__IMFCollection_FWD_DEFINED__ = None
__IMFMediaEventQueue_FWD_DEFINED__ = None
__IMFActivate_FWD_DEFINED__ = None
__IMFPluginControl_FWD_DEFINED__ = None
__IMFPluginControl2_FWD_DEFINED__ = None
__IMFDXGIDeviceManager_FWD_DEFINED__ = None
__IMFMuxStreamAttributesManager_FWD_DEFINED__ = None
__IMFMuxStreamMediaTypeManager_FWD_DEFINED__ = None
__IMFMuxStreamSampleManager_FWD_DEFINED__ = None
__IMFAttributes_INTERFACE_DEFINED__ = None
__IMFMediaBuffer_INTERFACE_DEFINED__ = None
__IMFSample_INTERFACE_DEFINED__ = None
__IMF2DBuffer_INTERFACE_DEFINED__ = None
__IMF2DBuffer2_INTERFACE_DEFINED__ = None
__IMFDXGIBuffer_INTERFACE_DEFINED__ = None
__IMFMediaType_INTERFACE_DEFINED__ = None
__IMFAudioMediaType_INTERFACE_DEFINED__ = None
_WINGDI_ = None
_MFVIDEOFORMAT_ = None
__IMFVideoMediaType_INTERFACE_DEFINED__ = None
__IMFAsyncResult_INTERFACE_DEFINED__ = None
__IMFAsyncCallback_INTERFACE_DEFINED__ = None
__IMFAsyncCallbackLogging_INTERFACE_DEFINED__ = None
__IMFMediaEvent_INTERFACE_DEFINED__ = None
__IMFMediaEventGenerator_INTERFACE_DEFINED__ = None
__IMFRemoteAsyncCallback_INTERFACE_DEFINED__ = None
__IMFByteStream_INTERFACE_DEFINED__ = None
__IMFByteStreamProxyClassFactory_INTERFACE_DEFINED__ = None
__IMFSampleOutputStream_INTERFACE_DEFINED__ = None
__IMFCollection_INTERFACE_DEFINED__ = None
__IMFMediaEventQueue_INTERFACE_DEFINED__ = None
__IMFActivate_INTERFACE_DEFINED__ = None
__IMFPluginControl_INTERFACE_DEFINED__ = None
__IMFPluginControl2_INTERFACE_DEFINED__ = None
__IMFDXGIDeviceManager_INTERFACE_DEFINED__ = None
__IMFMuxStreamAttributesManager_INTERFACE_DEFINED__ = None
__IMFMuxStreamMediaTypeManager_INTERFACE_DEFINED__ = None
__IMFMuxStreamSampleManager_INTERFACE_DEFINED__ = None


class __MIDL___MIDL_itf_mfobjects_0000_0008_0001(ctypes.Structure):
    pass


BITMAPINFOHEADER = __MIDL___MIDL_itf_mfobjects_0000_0008_0001


class __MIDL___MIDL_itf_mfobjects_0000_0008_0002(ctypes.Structure):
    pass


BITMAPINFO = __MIDL___MIDL_itf_mfobjects_0000_0008_0002


class __MIDL___MIDL_itf_mfobjects_0000_0008_0003(ctypes.Structure):
    pass


MFT_REGISTER_TYPE_INFO = __MIDL___MIDL_itf_mfobjects_0000_0008_0003


class _MFRatio(ctypes.Structure):
    pass


MFRatio = _MFRatio


class _MFOffset(ctypes.Structure):
    pass


MFOffset = _MFOffset


class _MFVideoArea(ctypes.Structure):
    pass


MFVideoArea = _MFVideoArea


class _MFVideoInfo(ctypes.Structure):
    pass


MFVideoInfo = _MFVideoInfo


class __MFAYUVSample(ctypes.Structure):
    pass


MFAYUVSample = __MFAYUVSample


class _MFARGB(ctypes.Structure):
    pass


MFARGB = _MFARGB


class _MFPaletteEntry(ctypes.Union):
    pass


MFPaletteEntry = _MFPaletteEntry


class _MFVideoSurfaceInfo(ctypes.Structure):
    pass


MFVideoSurfaceInfo = _MFVideoSurfaceInfo


class _MFVideoCompressedInfo(ctypes.Structure):
    pass


MFVideoCompressedInfo = _MFVideoCompressedInfo


class _MFVIDEOFORMAT(ctypes.Structure):
    pass


MFVIDEOFORMAT = _MFVIDEOFORMAT


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


if not defined(__mfobjects_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IMFAttributes_FWD_DEFINED__):

        class IMFAttributes(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None
    # END IF  __IMFAttributes_FWD_DEFINED__

    if not defined(__IMFMediaBuffer_FWD_DEFINED__):
        class IMFMediaBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaBuffer_FWD_DEFINED__

    if not defined(__IMFSample_FWD_DEFINED__):
        class IMFSample(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSample_FWD_DEFINED__

    if not defined(__IMF2DBuffer_FWD_DEFINED__):
        class IMF2DBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMF2DBuffer_FWD_DEFINED__

    if not defined(__IMF2DBuffer2_FWD_DEFINED__):
        class IMF2DBuffer2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMF2DBuffer2_FWD_DEFINED__

    if not defined(__IMFDXGIBuffer_FWD_DEFINED__):
        class IMFDXGIBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFDXGIBuffer_FWD_DEFINED__

    if not defined(__IMFMediaType_FWD_DEFINED__):
        class IMFMediaType(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaType_FWD_DEFINED__

    if not defined(__IMFAudioMediaType_FWD_DEFINED__):
        class IMFAudioMediaType(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFAudioMediaType_FWD_DEFINED__

    if not defined(__IMFVideoMediaType_FWD_DEFINED__):
        class IMFVideoMediaType(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoMediaType_FWD_DEFINED__

    if not defined(__IMFAsyncResult_FWD_DEFINED__):
        class IMFAsyncResult(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFAsyncResult_FWD_DEFINED__

    if not defined(__IMFAsyncCallback_FWD_DEFINED__):
        class IMFAsyncCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFAsyncCallback_FWD_DEFINED__

    if not defined(__IMFAsyncCallbackLogging_FWD_DEFINED__):
        class IMFAsyncCallbackLogging(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFAsyncCallbackLogging_FWD_DEFINED__

    if not defined(__IMFMediaEvent_FWD_DEFINED__):
        class IMFMediaEvent(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEvent_FWD_DEFINED__

    if not defined(__IMFMediaEventGenerator_FWD_DEFINED__):
        class IMFMediaEventGenerator(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEventGenerator_FWD_DEFINED__

    if not defined(__IMFRemoteAsyncCallback_FWD_DEFINED__):
        class IMFRemoteAsyncCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFRemoteAsyncCallback_FWD_DEFINED__

    if not defined(__IMFByteStream_FWD_DEFINED__):
        class IMFByteStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFByteStream_FWD_DEFINED__

    if not defined(__IMFByteStreamProxyClassFactory_FWD_DEFINED__):
        class IMFByteStreamProxyClassFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFByteStreamProxyClassFactory_FWD_DEFINED__

    if not defined(__IMFSampleOutputStream_FWD_DEFINED__):
        class IMFSampleOutputStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSampleOutputStream_FWD_DEFINED__

    if not defined(__IMFCollection_FWD_DEFINED__):
        class IMFCollection(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCollection_FWD_DEFINED__

    if not defined(__IMFMediaEventQueue_FWD_DEFINED__):
        class IMFMediaEventQueue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEventQueue_FWD_DEFINED__

    if not defined(__IMFActivate_FWD_DEFINED__):
        class IMFActivate(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFActivate_FWD_DEFINED__

    if not defined(__IMFPluginControl_FWD_DEFINED__):
        class IMFPluginControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFPluginControl_FWD_DEFINED__

    if not defined(__IMFPluginControl2_FWD_DEFINED__):
        class IMFPluginControl2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFPluginControl2_FWD_DEFINED__

    if not defined(__IMFDXGIDeviceManager_FWD_DEFINED__):
        class IMFDXGIDeviceManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFDXGIDeviceManager_FWD_DEFINED__

    if not defined(__IMFMuxStreamAttributesManager_FWD_DEFINED__):
        class IMFMuxStreamAttributesManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMuxStreamAttributesManager_FWD_DEFINED__

    if not defined(__IMFMuxStreamMediaTypeManager_FWD_DEFINED__):
        class IMFMuxStreamMediaTypeManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMuxStreamMediaTypeManager_FWD_DEFINED__

    if not defined(__IMFMuxStreamSampleManager_FWD_DEFINED__):
        class IMFMuxStreamSampleManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMuxStreamSampleManager_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.unknwn_h import * # NOQA
    from pyWinAPI.um.propsys_h import * # NOQA
    from pyWinAPI.um.mediaobj_h import * # NOQA
    from pyWinAPI.shared.mmreg_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_mfobjects_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    QWORD = ULONGLONG

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class _MF_ATTRIBUTE_TYPE(ENUM):
            MF_ATTRIBUTE_UINT32 = VARENUM.VT_UI4
            MF_ATTRIBUTE_UINT64 = VARENUM.VT_UI8
            MF_ATTRIBUTE_DOUBLE = VARENUM.VT_R8
            MF_ATTRIBUTE_GUID = VARENUM.VT_CLSID
            MF_ATTRIBUTE_STRING = VARENUM.VT_LPWSTR
            MF_ATTRIBUTE_BLOB = VARENUM.VT_VECTOR | VARENUM.VT_UI1
            MF_ATTRIBUTE_IUNKNOWN = VARENUM.VT_UNKNOWN


        MF_ATTRIBUTE_TYPE = _MF_ATTRIBUTE_TYPE


        class _MF_ATTRIBUTES_MATCH_TYPE(ENUM):
            MF_ATTRIBUTES_MATCH_OUR_ITEMS = 0
            MF_ATTRIBUTES_MATCH_THEIR_ITEMS = 1
            MF_ATTRIBUTES_MATCH_ALL_ITEMS = 2
            MF_ATTRIBUTES_MATCH_INTERSECTION = 3
            MF_ATTRIBUTES_MATCH_SMALLER = 4

        MF_ATTRIBUTES_MATCH_TYPE = _MF_ATTRIBUTES_MATCH_TYPE
        if not defined(__IMFAttributes_INTERFACE_DEFINED__):
            # interface IMFAttributes
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFAttributes = MIDL_INTERFACE(
                    "{2CD2D921-C447-44A7-A13C-4ADABFC247E3}"
                )
                IMFAttributes._iid_ = IID_IMFAttributes

                IMFAttributes._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetItem')],
                        HRESULT,
                        'GetItem',
                        (['in'], REFGUID, 'guidKey'),
                        (
                            ['out', 'full', 'in'],
                            POINTER(PROPVARIANT),
                            'pValue'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetItemType')],
                        HRESULT,
                        'GetItemType',
                        (['in'], REFGUID, 'guidKey'),
                        (['out'], POINTER(MF_ATTRIBUTE_TYPE), 'pType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CompareItem')],
                        HRESULT,
                        'CompareItem',
                        (['in'], REFGUID, 'guidKey'),
                        (['in'], REFPROPVARIANT, 'Value'),
                        (['out'], POINTER(BOOL), 'pbResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Compare')],
                        HRESULT,
                        'Compare',
                        (['in'], POINTER(IMFAttributes), 'pTheirs'),
                        (['in'], MF_ATTRIBUTES_MATCH_TYPE, 'MatchType'),
                        (['out'], POINTER(BOOL), 'pbResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetUINT32')],
                        HRESULT,
                        'GetUINT32',
                        (['in'], REFGUID, 'guidKey'),
                        (['out'], POINTER(UINT32), 'punValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetUINT64')],
                        HRESULT,
                        'GetUINT64',
                        (['in'], REFGUID, 'guidKey'),
                        (['out'], POINTER(UINT64), 'punValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDouble')],
                        HRESULT,
                        'GetDouble',
                        (['in'], REFGUID, 'guidKey'),
                        (['out'], POINTER(DOUBLE), 'pfValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetGUID')],
                        HRESULT,
                        'GetGUID',
                        (['in'], REFGUID, 'guidKey'),
                        (['out'], POINTER(GUID), 'pguidValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStringLength')],
                        HRESULT,
                        'GetStringLength',
                        (['in'], REFGUID, 'guidKey'),
                        (['out'], POINTER(UINT32), 'pcchLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetString')],
                        HRESULT,
                        'GetString',
                        (['in'], REFGUID, 'guidKey'),
                        (['out'], LPWSTR, 'pwszValue'),
                        ([], UINT32, 'cchBufSize'),
                        (
                            ['out', 'full', 'in'],
                            POINTER(UINT32),
                            'pcchLength'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAllocatedString')],
                        HRESULT,
                        'GetAllocatedString',
                        (['in'], REFGUID, 'guidKey'),
                        (['out'], POINTER(LPWSTR), 'ppwszValue'),
                        (['out'], POINTER(UINT32), 'pcchLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetBlobSize')],
                        HRESULT,
                        'GetBlobSize',
                        (['in'], REFGUID, 'guidKey'),
                        (['out'], POINTER(UINT32), 'pcbBlobSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetBlob')],
                        HRESULT,
                        'GetBlob',
                        (['in'], REFGUID, 'guidKey'),
                        (['out'], POINTER(UINT8), 'pBuf'),
                        ([], UINT32, 'cbBufSize'),
                        (
                            ['out', 'full', 'in'],
                            POINTER(UINT32),
                            'pcbBlobSize'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAllocatedBlob')],
                        HRESULT,
                        'GetAllocatedBlob',
                        (['in'], REFGUID, 'guidKey'),
                        (['out'], POINTER(POINTER(UINT8)), 'ppBuf'),
                        (['out'], POINTER(UINT32), 'pcbSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetUnknown')],
                        HRESULT,
                        'GetUnknown',
                        (['in'], REFGUID, 'guidKey'),
                        (['in'], REFIID, 'riid'),
                        (['out', 'iid_is'], POINTER(LPVOID), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetItem')],
                        HRESULT,
                        'SetItem',
                        (['in'], REFGUID, 'guidKey'),
                        (['in'], REFPROPVARIANT, 'Value'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DeleteItem')],
                        HRESULT,
                        'DeleteItem',
                        (['in'], REFGUID, 'guidKey'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DeleteAllItems')],
                        HRESULT,
                        'DeleteAllItems',
                    ),
                    COMMETHOD(
                        [helpstring('Method SetUINT32')],
                        HRESULT,
                        'SetUINT32',
                        (['in'], REFGUID, 'guidKey'),
                        ([], UINT32, 'unValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetUINT64')],
                        HRESULT,
                        'SetUINT64',
                        (['in'], REFGUID, 'guidKey'),
                        ([], UINT64, 'unValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetDouble')],
                        HRESULT,
                        'SetDouble',
                        (['in'], REFGUID, 'guidKey'),
                        ([], DOUBLE, 'fValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetGUID')],
                        HRESULT,
                        'SetGUID',
                        (['in'], REFGUID, 'guidKey'),
                        (['in'], REFGUID, 'guidValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetString')],
                        HRESULT,
                        'SetString',
                        (['in'], REFGUID, 'guidKey'),
                        (['in'], LPCWSTR, 'wszValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetBlob')],
                        HRESULT,
                        'SetBlob',
                        (['in'], REFGUID, 'guidKey'),
                        (['in'], POINTER(UINT8), 'pBuf'),
                        ([], UINT32, 'cbBufSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetUnknown')],
                        HRESULT,
                        'SetUnknown',
                        (['in'], REFGUID, 'guidKey'),
                        (['in'], POINTER(comtypes.IUnknown), 'pUnknown'),
                    ),
                    COMMETHOD(
                        [helpstring('Method LockStore')],
                        HRESULT,
                        'LockStore',
                    ),
                    COMMETHOD(
                        [helpstring('Method UnlockStore')],
                        HRESULT,
                        'UnlockStore',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCount')],
                        HRESULT,
                        'GetCount',
                        (['out'], POINTER(UINT32), 'pcItems'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetItemByIndex')],
                        HRESULT,
                        'GetItemByIndex',
                        ([], UINT32, 'unIndex'),
                        (['out'], POINTER(GUID), 'pguidKey'),
                        (
                            ['out', 'full', 'in'],
                            POINTER(PROPVARIANT),
                            'pValue'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method CopyAllItems')],
                        HRESULT,
                        'CopyAllItems',
                        (['in'], POINTER(IMFAttributes), 'pDest'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFAttributes_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfobjects_0000_0001
        # [local

        class MF_ATTRIBUTE_SERIALIZE_OPTIONS(ENUM):
            MF_ATTRIBUTE_SERIALIZE_UNKNOWN_BYREF = 0x1

        MF_ATTRIBUTE_SERIALIZE_UNKNOWN_BYREF = MF_ATTRIBUTE_SERIALIZE_OPTIONS.MF_ATTRIBUTE_SERIALIZE_UNKNOWN_BYREF
        mfplat = ctypes.windll.MFPLAT

        # STDAPI MFSerializeAttributesToStream(
        # IMFAttributes * pAttr,
        # DWORD dwOptions,
        # IStream * pStm);
        MFSerializeAttributesToStream = mfplat.MFSerializeAttributesToStream

        # STDAPI MFDeserializeAttributesFromStream(
        # IMFAttributes * pAttr,
        # DWORD dwOptions,
        # IStream * pStm);
        MFDeserializeAttributesFromStream = (
            mfplat.MFDeserializeAttributesFromStream
        )

        if not defined(__IMFMediaBuffer_INTERFACE_DEFINED__):
            # interface IMFMediaBuffer
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaBuffer = MIDL_INTERFACE(
                    "{045FA593-8799-42B8-BC8D-8968C6453507}"
                )
                IMFMediaBuffer._iid_ = IID_IMFMediaBuffer

                IMFMediaBuffer._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Lock')],
                        HRESULT,
                        'Lock',
                        (['out'], POINTER(POINTER(BYTE)), 'ppbBuffer'),
                        (['out'], POINTER(DWORD), 'pcbMaxLength'),
                        (['out'], POINTER(DWORD), 'pcbCurrentLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Unlock')],
                        HRESULT,
                        'Unlock',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCurrentLength')],
                        HRESULT,
                        'GetCurrentLength',
                        (['out'], POINTER(DWORD), 'pcbCurrentLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetCurrentLength')],
                        HRESULT,
                        'SetCurrentLength',
                        (['in'], DWORD, 'cbCurrentLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMaxLength')],
                        HRESULT,
                        'GetMaxLength',
                        (['out'], POINTER(DWORD), 'pcbMaxLength'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaBuffer_INTERFACE_DEFINED__

        if not defined(__IMFSample_INTERFACE_DEFINED__):
            # interface IMFSample
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSample = MIDL_INTERFACE(
                    "{C40A00F2-B93A-4D80-AE8C-5A1C634F58E4}"
                )
                IMFSample._iid_ = IID_IMFSample

                IMFSample._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetSampleFlags')],
                        HRESULT,
                        'GetSampleFlags',
                        (['out'], POINTER(DWORD), 'pdwSampleFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetSampleFlags')],
                        HRESULT,
                        'SetSampleFlags',
                        (['in'], DWORD, 'dwSampleFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSampleTime')],
                        HRESULT,
                        'GetSampleTime',
                        (['out'], POINTER(LONGLONG), 'phnsSampleTime'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetSampleTime')],
                        HRESULT,
                        'SetSampleTime',
                        (['in'], LONGLONG, 'hnsSampleTime'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSampleDuration')],
                        HRESULT,
                        'GetSampleDuration',
                        (['out'], POINTER(LONGLONG), 'phnsSampleDuration'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetSampleDuration')],
                        HRESULT,
                        'SetSampleDuration',
                        (['in'], LONGLONG, 'hnsSampleDuration'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetBufferCount')],
                        HRESULT,
                        'GetBufferCount',
                        (['out'], POINTER(DWORD), 'pdwBufferCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetBufferByIndex')],
                        HRESULT,
                        'GetBufferByIndex',
                        (['in'], DWORD, 'dwIndex'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaBuffer)),
                            'ppBuffer'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ConvertToContiguousBuffer')],
                        HRESULT,
                        'ConvertToContiguousBuffer',
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaBuffer)),
                            'ppBuffer'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddBuffer')],
                        HRESULT,
                        'AddBuffer',
                        (['in'], POINTER(IMFMediaBuffer), 'pBuffer'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RemoveBufferByIndex')],
                        HRESULT,
                        'RemoveBufferByIndex',
                        (['in'], DWORD, 'dwIndex'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RemoveAllBuffers')],
                        HRESULT,
                        'RemoveAllBuffers',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTotalLength')],
                        HRESULT,
                        'GetTotalLength',
                        (['out'], POINTER(DWORD), 'pcbTotalLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CopyToBuffer')],
                        HRESULT,
                        'CopyToBuffer',
                        (['in'], POINTER(IMFMediaBuffer), 'pBuffer'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSample_INTERFACE_DEFINED__

        if not defined(__IMF2DBuffer_INTERFACE_DEFINED__):
            # interface IMF2DBuffer
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMF2DBuffer = MIDL_INTERFACE(
                    "{7DC9D5F9-9ED9-44EC-9BBF-0600BB589FBB}"
                )
                IMF2DBuffer._iid_ = IID_IMF2DBuffer

                IMF2DBuffer._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Lock2D')],
                        HRESULT,
                        'Lock2D',
                        (
                            ['out', 'in'],
                            POINTER(POINTER(BYTE)),
                            'ppbScanline0'
                        ),
                        (['out'], POINTER(LONG), 'plPitch'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Unlock2D')],
                        HRESULT,
                        'Unlock2D',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetScanline0AndPitch')],
                        HRESULT,
                        'GetScanline0AndPitch',
                        (['out'], POINTER(POINTER(BYTE)), 'pbScanline0'),
                        (['out'], POINTER(LONG), 'plPitch'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsContiguousFormat')],
                        HRESULT,
                        'IsContiguousFormat',
                        (['out'], POINTER(BOOL), 'pfIsContiguous'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetContiguousLength')],
                        HRESULT,
                        'GetContiguousLength',
                        (['out'], POINTER(DWORD), 'pcbLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ContiguousCopyTo')],
                        HRESULT,
                        'ContiguousCopyTo',
                        (['out'], POINTER(BYTE), 'pbDestBuffer'),
                        (['in'], DWORD, 'cbDestBuffer'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ContiguousCopyFrom')],
                        HRESULT,
                        'ContiguousCopyFrom',
                        (['in'], POINTER(BYTE), 'pbSrcBuffer'),
                        (['in'], DWORD, 'cbSrcBuffer'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMF2DBuffer_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfobjects_0000_0004
        # [local]
        class _MF2DBuffer_LockFlags(ENUM):
            MF2DBuffer_LockFlags_LockTypeMask = (0x1 | 0x2) | 0x3
            MF2DBuffer_LockFlags_Read = 0x1
            MF2DBuffer_LockFlags_Write = 0x2
            MF2DBuffer_LockFlags_ReadWrite = 0x3
            MF2DBuffer_LockFlags_ForceDWORD = 0x7FFFFFFF


        MF2DBuffer_LockFlags = _MF2DBuffer_LockFlags

        if not defined(__IMF2DBuffer2_INTERFACE_DEFINED__):
            # interface IMF2DBuffer2
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMF2DBuffer2 = MIDL_INTERFACE(
                    "{33AE5EA6-4316-436F-8DDD-D73D22F829EC}"
                )
                IMF2DBuffer2._iid_ = IID_IMF2DBuffer2

                IMF2DBuffer2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Lock2DSize')],
                        HRESULT,
                        'Lock2DSize',
                        (['in'], MF2DBuffer_LockFlags, 'lockFlags'),
                        (
                            ['out', 'in'],
                            POINTER(POINTER(BYTE)),
                            'ppbScanline0'
                        ),
                        (['out'], POINTER(LONG), 'plPitch'),
                        (['out'], POINTER(POINTER(BYTE)), 'ppbBufferStart'),
                        (['out'], POINTER(DWORD), 'pcbBufferLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Copy2DTo')],
                        HRESULT,
                        'Copy2DTo',
                        (['in'], POINTER(IMF2DBuffer2), 'pDestBuffer'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMF2DBuffer2_INTERFACE_DEFINED__

        if not defined(__IMFDXGIBuffer_INTERFACE_DEFINED__):
            # interface IMFDXGIBuffer
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFDXGIBuffer = MIDL_INTERFACE(
                    "{E7174CFA-1C9E-48B1-8866-626226BFC258}"
                )
                IMFDXGIBuffer._iid_ = IID_IMFDXGIBuffer

                IMFDXGIBuffer._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetResource')],
                        HRESULT,
                        'GetResource',
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(LPVOID), 'ppvObject'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSubresourceIndex')],
                        HRESULT,
                        'GetSubresourceIndex',
                        (['out'], POINTER(UINT), 'puSubresource'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetUnknown')],
                        HRESULT,
                        'GetUnknown',
                        (['in'], REFIID, 'guid'),
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(LPVOID), 'ppvObject'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetUnknown')],
                        HRESULT,
                        'SetUnknown',
                        (['in'], REFIID, 'guid'),
                        (['in'], POINTER(comtypes.IUnknown), 'pUnkData'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFDXGIBuffer_INTERFACE_DEFINED__

        if not defined(__IMFMediaType_INTERFACE_DEFINED__):
            # interface IMFMediaType
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaType = MIDL_INTERFACE(
                    "{44AE0FA8-EA31-4109-8D2E-4CAE4997C555}"
                )
                IMFMediaType._iid_ = IID_IMFMediaType

                IMFMediaType._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetMajorType')],
                        HRESULT,
                        'GetMajorType',
                        (['out'], POINTER(GUID), 'pguidMajorType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsCompressedFormat')],
                        HRESULT,
                        'IsCompressedFormat',
                        (['out'], POINTER(BOOL), 'pfCompressed'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsEqual')],
                        HRESULT,
                        'IsEqual',
                        (['in'], POINTER(IMFMediaType), 'pIMediaType'),
                        (['out'], POINTER(DWORD), 'pdwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRepresentation'), 'local'],
                        HRESULT,
                        'GetRepresentation',
                        (['in'], GUID, 'guidRepresentation'),
                        (['out'], POINTER(LPVOID), 'ppvRepresentation'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FreeRepresentation'), 'local'],
                        HRESULT,
                        'FreeRepresentation',
                        (['in'], GUID, 'guidRepresentation'),
                        (['in'], LPVOID, 'pvRepresentation'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaType_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfobjects_0000_0007
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFAudioMediaType_INTERFACE_DEFINED__):
            # interface IMFAudioMediaType
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFAudioMediaType = MIDL_INTERFACE(
                    "{26A0ADC3-CE26-4672-9304-69552EDD3FAF}"
                )
                IMFAudioMediaType._iid_ = IID_IMFAudioMediaType

                IMFAudioMediaType._methods_ = [
                    COMMETHOD(
                        [helpstring('Method *GetAudioFormat')],
                        WAVEFORMATEX,
                        '*GetAudioFormat',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFAudioMediaType_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfobjects_0000_0008
        # [local]
        if not defined(_WINGDI_):
            RGBQUAD = DWORD

            __MIDL___MIDL_itf_mfobjects_0000_0008_0001._fields_ = [
                ('biSize', DWORD),
                ('biWidth', LONG),
                ('biHeight', LONG),
                ('biPlanes', WORD),
                ('biBitCount', WORD),
                ('biCompression', DWORD),
                ('biSizeImage', DWORD),
                ('biXPelsPerMeter', LONG),
                ('biYPelsPerMeter', LONG),
                ('biClrUsed', DWORD),
                ('biClrImportant', DWORD),
            ]

            __MIDL___MIDL_itf_mfobjects_0000_0008_0002._fields_ = [
                ('bmiHeader', BITMAPINFOHEADER),
                ('bmiColors', RGBQUAD * 1),
            ]
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        __MIDL___MIDL_itf_mfobjects_0000_0008_0003._fields_ = [
            ('guidMajorType', GUID),
            ('guidSubtype', GUID),
        ]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if not defined(_MFVIDEOFORMAT_):
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            class _MFVideoInterlaceMode(ENUM):
                MFVideoInterlace_Unknown = 0
                MFVideoInterlace_Progressive = 2
                MFVideoInterlace_FieldInterleavedUpperFirst = 3
                MFVideoInterlace_FieldInterleavedLowerFirst = 4
                MFVideoInterlace_FieldSingleUpper = 5
                MFVideoInterlace_FieldSingleLower = 6
                MFVideoInterlace_MixedInterlaceOrProgressive = 7
                MFVideoInterlace_Last = (
                    MFVideoInterlace_MixedInterlaceOrProgressive + 1
                )
                MFVideoInterlace_ForceDWORD = 0x7FFFFFFF
            MFVideoInterlaceMode = _MFVideoInterlaceMode


            class _MFVideoTransferFunction(ENUM):
                MFVideoTransFunc_Unknown = 0
                MFVideoTransFunc_10 = 1
                MFVideoTransFunc_18 = 2
                MFVideoTransFunc_20 = 3
                MFVideoTransFunc_22 = 4
                MFVideoTransFunc_709 = 5
                MFVideoTransFunc_240M = 6
                MFVideoTransFunc_sRGB = 7
                MFVideoTransFunc_28 = 8
                MFVideoTransFunc_Log_100 = 9
                MFVideoTransFunc_Log_316 = 10
                MFVideoTransFunc_709_sym = 11
                MFVideoTransFunc_2020_const = 12
                MFVideoTransFunc_2020 = 13
                MFVideoTransFunc_26 = 14
                MFVideoTransFunc_2084 = 15
                MFVideoTransFunc_HLG = 16
                MFVideoTransFunc_10_rel = 17
                MFVideoTransFunc_Last = MFVideoTransFunc_10_rel + 1
                MFVideoTransFunc_ForceDWORD = 0x7FFFFFFF


            MFVideoTransferFunction = _MFVideoTransferFunction


            class _MFVideoPrimaries(ENUM):
                MFVideoPrimaries_Unknown = 0
                MFVideoPrimaries_reserved = 1
                MFVideoPrimaries_BT709 = 2
                MFVideoPrimaries_BT470_2_SysM = 3
                MFVideoPrimaries_BT470_2_SysBG = 4
                MFVideoPrimaries_SMPTE170M = 5
                MFVideoPrimaries_SMPTE240M = 6
                MFVideoPrimaries_EBU3213 = 7
                MFVideoPrimaries_SMPTE_C = 8
                MFVideoPrimaries_BT2020 = 9
                MFVideoPrimaries_XYZ = 10
                MFVideoPrimaries_DCI_P3 = 11
                MFVideoPrimaries_ACES = 12
                MFVideoPrimaries_Last = MFVideoPrimaries_ACES + 1
                MFVideoPrimaries_ForceDWORD = 0x7FFFFFFF


            MFVideoPrimaries = _MFVideoPrimaries


            class _MFVideoLighting(ENUM):
                MFVideoLighting_Unknown = 0
                MFVideoLighting_bright = 1
                MFVideoLighting_office = 2
                MFVideoLighting_dim = 3
                MFVideoLighting_dark = 4
                MFVideoLighting_Last = MFVideoLighting_dark + 1
                MFVideoLighting_ForceDWORD = 0x7FFFFFFF


            MFVideoLighting = _MFVideoLighting


            class _MFVideoTransferMatrix(ENUM):
                MFVideoTransferMatrix_Unknown = 0
                MFVideoTransferMatrix_BT709 = 1
                MFVideoTransferMatrix_BT601 = 2
                MFVideoTransferMatrix_SMPTE240M = 3
                MFVideoTransferMatrix_BT2020_10 = 4
                MFVideoTransferMatrix_BT2020_12 = 5
                MFVideoTransferMatrix_Last = (
                    MFVideoTransferMatrix_BT2020_12 + 1
                )
                MFVideoTransferMatrix_ForceDWORD = 0x7FFFFFFF


            MFVideoTransferMatrix = _MFVideoTransferMatrix


            class _MFVideoChromaSubsampling(ENUM):
                MFVideoChromaSubsampling_Unknown = 0
                MFVideoChromaSubsampling_ProgressiveChroma = 0x8
                MFVideoChromaSubsampling_Horizontally_Cosited = 0x4
                MFVideoChromaSubsampling_Vertically_Cosited = 0x2
                MFVideoChromaSubsampling_Vertically_AlignedChromaPlanes = 0x1
                MFVideoChromaSubsampling_MPEG2 = (
                    MFVideoChromaSubsampling_Horizontally_Cosited |
                    MFVideoChromaSubsampling_Vertically_AlignedChromaPlanes
                )
                MFVideoChromaSubsampling_MPEG1 = (
                    MFVideoChromaSubsampling_Vertically_AlignedChromaPlanes
                )
                MFVideoChromaSubsampling_DV_PAL = (
                    MFVideoChromaSubsampling_Horizontally_Cosited |
                    MFVideoChromaSubsampling_Vertically_Cosited
                )
                MFVideoChromaSubsampling_Cosited = (
                    (
                        MFVideoChromaSubsampling_Horizontally_Cosited |
                        MFVideoChromaSubsampling_Vertically_Cosited
                    ) |
                    MFVideoChromaSubsampling_Vertically_AlignedChromaPlanes
                )
                MFVideoChromaSubsampling_Last = (
                    MFVideoChromaSubsampling_Cosited + 1
                )
                MFVideoChromaSubsampling_ForceDWORD = 0x7FFFFFFF


            MFVideoChromaSubsampling = _MFVideoChromaSubsampling


            class _MFNominalRange(ENUM):
                MFNominalRange_Unknown = 0
                MFNominalRange_Normal = 1
                MFNominalRange_Wide = 2
                MFNominalRange_0_255 = 1
                MFNominalRange_16_235 = 2
                MFNominalRange_48_208 = 3
                MFNominalRange_64_127 = 4
                MFNominalRange_Last = MFNominalRange_64_127 + 1
                MFNominalRange_ForceDWORD = 0x7FFFFFFF


            MFNominalRange = _MFNominalRange
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            class _MFVideoFlags(ENUM):
                MFVideoFlag_PAD_TO_Mask = 0x1 | 0x2
                MFVideoFlag_PAD_TO_None = 0 * 0x1
                MFVideoFlag_PAD_TO_4x3 = 1 * 0x1
                MFVideoFlag_PAD_TO_16x9 = 2 * 0x1
                MFVideoFlag_SrcContentHintMask = (0x4 | 0x8) | 0x10
                MFVideoFlag_SrcContentHintNone = 0 * 0x4
                MFVideoFlag_SrcContentHint16x9 = 1 * 0x4
                MFVideoFlag_SrcContentHint235_1 = 2 * 0x4
                MFVideoFlag_AnalogProtected = 0x20
                MFVideoFlag_DigitallyProtected = 0x40
                MFVideoFlag_ProgressiveContent = 0x80
                MFVideoFlag_FieldRepeatCountMask = (0x100 | 0x200) | 0x400
                MFVideoFlag_FieldRepeatCountShift = 8
                MFVideoFlag_ProgressiveSeqReset = 0x800
                MFVideoFlag_PanScanEnabled = 0x20000
                MFVideoFlag_LowerFieldFirst = 0x40000
                MFVideoFlag_BottomUpLinearRep = 0x80000
                MFVideoFlags_DXVASurface = 0x100000
                MFVideoFlags_RenderTargetSurface = 0x400000
                MFVideoFlags_ForceQWORD = 0x7FFFFFFF


            MFVideoFlags = _MFVideoFlags
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            _MFRatio._fields_ = [
                ('Numerator', DWORD),
                ('Denominator', DWORD),
            ]

            _MFOffset._fields_ = [
                ('fract', WORD),
                ('value', SHORT),
            ]

            _MFVideoArea._fields_ = [
                ('OffsetX', MFOffset),
                ('OffsetY', MFOffset),
                ('Area', SIZE),
            ]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if defined(_MSC_VER) and (_MSC_VER >= 1600):
            pass
        # END IF

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            _MFVideoInfo._fields_ = [
                ('dwWidth', DWORD),
                ('dwHeight', DWORD),
                ('PixelAspectRatio', MFRatio),
                ('SourceChromaSubsampling', MFVideoChromaSubsampling),
                ('InterlaceMode', MFVideoInterlaceMode),
                ('TransferFunction', MFVideoTransferFunction),
                ('ColorPrimaries', MFVideoPrimaries),
                ('TransferMatrix', MFVideoTransferMatrix),
                ('SourceLighting', MFVideoLighting),
                ('FramesPerSecond', MFRatio),
                ('NominalRange', MFNominalRange),
                ('GeometricAperture', MFVideoArea),
                ('MinimumDisplayAperture', MFVideoArea),
                ('PanScanAperture', MFVideoArea),
                ('INT64 VideoFlags', UINT),
            ]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if defined(_MSC_VER) and (_MSC_VER >= 1600):
            pass
        # END IF

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            __MFAYUVSample._fields_ = [
                ('bCrValue', BYTE),
                ('bCbValue', BYTE),
                ('bYValue', BYTE),
                ('bSampleAlpha8', BYTE),
            ]

            _MFARGB._fields_ = [
                ('rgbBlue', BYTE),
                ('rgbGreen', BYTE),
                ('rgbRed', BYTE),
                ('rgbAlpha', BYTE),
            ]

            _MFPaletteEntry._fields_ = [
                ('ARGB', MFARGB),
                ('AYCbCr', MFAYUVSample),
            ]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if defined(_MSC_VER) and (_MSC_VER >= 1600):
            pass
        # END IF

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            _MFVideoSurfaceInfo._fields_ = [
                ('Format', DWORD),
                ('PaletteEntries', DWORD),
                # [size_is]
                ('Palette', MFPaletteEntry * 1),
            ]

            _MFVideoCompressedInfo._fields_ = [
                ('AvgBitrate', LONGLONG),
                ('AvgBitErrorRate', LONGLONG),
                ('MaxKeyFrameSpacing', DWORD),
            ]

            _MFVIDEOFORMAT._fields_ = [
                ('dwSize', DWORD),
                ('videoInfo', MFVideoInfo),
                ('guidFormat', GUID),
                ('compressedInfo', MFVideoCompressedInfo),
                ('surfaceInfo', MFVideoSurfaceInfo),
            ]
            if defined(_MSC_VER) and (_MSC_VER >= 1600):
                pass
            # END IF


            class _MFStandardVideoFormat(ENUM):
                MFStdVideoFormat_reserved = 0
                MFStdVideoFormat_NTSC = MFStdVideoFormat_reserved + 1
                MFStdVideoFormat_PAL = MFStdVideoFormat_NTSC + 1
                MFStdVideoFormat_DVD_NTSC = MFStdVideoFormat_PAL + 1
                MFStdVideoFormat_DVD_PAL = MFStdVideoFormat_DVD_NTSC + 1
                MFStdVideoFormat_DV_PAL = MFStdVideoFormat_DVD_PAL + 1
                MFStdVideoFormat_DV_NTSC = MFStdVideoFormat_DV_PAL + 1
                MFStdVideoFormat_ATSC_SD480i = MFStdVideoFormat_DV_NTSC + 1
                MFStdVideoFormat_ATSC_HD1080i = (
                    MFStdVideoFormat_ATSC_SD480i + 1
                )
                MFStdVideoFormat_ATSC_HD720p = (
                    MFStdVideoFormat_ATSC_HD1080i + 1
                )


            MFStandardVideoFormat = _MFStandardVideoFormat

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # END IF
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFVideoMediaType_INTERFACE_DEFINED__):
            # interface IMFVideoMediaType
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFVideoMediaType = MIDL_INTERFACE(
                    "{B99F381F-A8F9-47A2-A5AF-CA3A225A3890}"
                )
                IMFVideoMediaType._iid_ = IID_IMFVideoMediaType

                IMFVideoMediaType._methods_ = [
                    COMMETHOD(
                        [helpstring('Method *GetVideoFormat')],
                        MFVIDEOFORMAT,
                        '*GetVideoFormat',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetVideoRepresentation')],
                        HRESULT,
                        'GetVideoRepresentation',
                        (['in'], GUID, 'guidRepresentation'),
                        (['out'], POINTER(LPVOID), 'ppvRepresentation'),
                        (['in'], LONG, 'lStride'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFVideoMediaType_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfobjects_0000_0009
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IMFAsyncResult_INTERFACE_DEFINED__):
            # interface IMFAsyncResult
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFAsyncResult = MIDL_INTERFACE(
                    "{AC6B7889-0740-4D51-8619-905994A55CC6}"
                )
                IMFAsyncResult._iid_ = IID_IMFAsyncResult

                IMFAsyncResult._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetState')],
                        HRESULT,
                        'GetState',
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                            'ppunkState'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStatus')],
                        HRESULT,
                        'GetStatus',
                    ),
                    COMMETHOD(
                        [helpstring('Method SetStatus')],
                        HRESULT,
                        'SetStatus',
                        (['in'], HRESULT, 'hrStatus'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetObject')],
                        HRESULT,
                        'GetObject',
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                            'ppObject'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method *GetStateNoAddRef'), 'local'],
                        IUnknown,
                        '*GetStateNoAddRef',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFAsyncResult_INTERFACE_DEFINED__

        if not defined(__IMFAsyncCallback_INTERFACE_DEFINED__):
            # interface IMFAsyncCallback
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFAsyncCallback = MIDL_INTERFACE(
                    "{A27003CF-2354-4F2A-8D6A-AB7CFF15437E}"
                )
                IMFAsyncCallback._iid_ = IID_IMFAsyncCallback

                IMFAsyncCallback._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetParameters')],
                        HRESULT,
                        'GetParameters',
                        (['out'], POINTER(DWORD), 'pdwFlags'),
                        (['out'], POINTER(DWORD), 'pdwQueue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Invoke')],
                        HRESULT,
                        'Invoke',
                        (['in'], POINTER(IMFAsyncResult), 'pAsyncResult'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFAsyncCallback_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfobjects_0000_0011
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFAsyncCallbackLogging_INTERFACE_DEFINED__):
            # interface IMFAsyncCallbackLogging
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFAsyncCallbackLogging = MIDL_INTERFACE(
                    "{C7A4DCA1-F5F0-47B6-B92B-BF0106D25791}"
                )
                IMFAsyncCallbackLogging._iid_ = IID_IMFAsyncCallbackLogging

                IMFAsyncCallbackLogging._methods_ = [
                    COMMETHOD(
                        [helpstring('Method *GetObjectPointer')],
                        VOID,
                        '*GetObjectPointer',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetObjectTag')],
                        DWORD,
                        'GetObjectTag',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFAsyncCallbackLogging_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfobjects_0000_0012
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class __MIDL___MIDL_itf_mfobjects_0000_0012_0001(ENUM):
            MEUnknown = 0
            MEError = 1
            MEExtendedType = 2
            MENonFatalError = 3
            MEGenericV1Anchor = MENonFatalError
            MESessionUnknown = 100
            MESessionTopologySet = 101
            MESessionTopologiesCleared = 102
            MESessionStarted = 103
            MESessionPaused = 104
            MESessionStopped = 105
            MESessionClosed = 106
            MESessionEnded = 107
            MESessionRateChanged = 108
            MESessionScrubSampleComplete = 109
            MESessionCapabilitiesChanged = 110
            MESessionTopologyStatus = 111
            MESessionNotifyPresentationTime = 112
            MENewPresentation = 113
            MELicenseAcquisitionStart = 114
            MELicenseAcquisitionCompleted = 115
            MEIndividualizationStart = 116
            MEIndividualizationCompleted = 117
            MEEnablerProgress = 118
            MEEnablerCompleted = 119
            MEPolicyError = 120
            MEPolicyReport = 121
            MEBufferingStarted = 122
            MEBufferingStopped = 123
            MEConnectStart = 124
            MEConnectEnd = 125
            MEReconnectStart = 126
            MEReconnectEnd = 127
            MERendererEvent = 128
            MESessionStreamSinkFormatChanged = 129
            MESessionV1Anchor = MESessionStreamSinkFormatChanged
            MESourceUnknown = 200
            MESourceStarted = 201
            MEStreamStarted = 202
            MESourceSeeked = 203
            MEStreamSeeked = 204
            MENewStream = 205
            MEUpdatedStream = 206
            MESourceStopped = 207
            MEStreamStopped = 208
            MESourcePaused = 209
            MEStreamPaused = 210
            MEEndOfPresentation = 211
            MEEndOfStream = 212
            MEMediaSample = 213
            MEStreamTick = 214
            MEStreamThinMode = 215
            MEStreamFormatChanged = 216
            MESourceRateChanged = 217
            MEEndOfPresentationSegment = 218
            MESourceCharacteristicsChanged = 219
            MESourceRateChangeRequested = 220
            MESourceMetadataChanged = 221
            MESequencerSourceTopologyUpdated = 222
            MESourceV1Anchor = MESequencerSourceTopologyUpdated
            MESinkUnknown = 300
            MEStreamSinkStarted = 301
            MEStreamSinkStopped = 302
            MEStreamSinkPaused = 303
            MEStreamSinkRateChanged = 304
            MEStreamSinkRequestSample = 305
            MEStreamSinkMarker = 306
            MEStreamSinkPrerolled = 307
            MEStreamSinkScrubSampleComplete = 308
            MEStreamSinkFormatChanged = 309
            MEStreamSinkDeviceChanged = 310
            MEQualityNotify = 311
            MESinkInvalidated = 312
            MEAudioSessionNameChanged = 313
            MEAudioSessionVolumeChanged = 314
            MEAudioSessionDeviceRemoved = 315
            MEAudioSessionServerShutdown = 316
            MEAudioSessionGroupingParamChanged = 317
            MEAudioSessionIconChanged = 318
            MEAudioSessionFormatChanged = 319
            MEAudioSessionDisconnected = 320
            MEAudioSessionExclusiveModeOverride = 321
            MESinkV1Anchor = MEAudioSessionExclusiveModeOverride
            MECaptureAudioSessionVolumeChanged = 322
            MECaptureAudioSessionDeviceRemoved = 323
            MECaptureAudioSessionFormatChanged = 324
            MECaptureAudioSessionDisconnected = 325
            MECaptureAudioSessionExclusiveModeOverride = 326
            MECaptureAudioSessionServerShutdown = 327
            MESinkV2Anchor = MECaptureAudioSessionServerShutdown
            METrustUnknown = 400
            MEPolicyChanged = 401
            MEContentProtectionMessage = 402
            MEPolicySet = 403
            METrustV1Anchor = MEPolicySet
            MEWMDRMLicenseBackupCompleted = 500
            MEWMDRMLicenseBackupProgress = 501
            MEWMDRMLicenseRestoreCompleted = 502
            MEWMDRMLicenseRestoreProgress = 503
            MEWMDRMLicenseAcquisitionCompleted = 506
            MEWMDRMIndividualizationCompleted = 508
            MEWMDRMIndividualizationProgress = 513
            MEWMDRMProximityCompleted = 514
            MEWMDRMLicenseStoreCleaned = 515
            MEWMDRMRevocationDownloadCompleted = 516
            MEWMDRMV1Anchor = MEWMDRMRevocationDownloadCompleted
            METransformUnknown = 600
            METransformNeedInput = METransformUnknown + 1
            METransformHaveOutput = METransformNeedInput + 1
            METransformDrainComplete = METransformHaveOutput + 1
            METransformMarker = METransformDrainComplete + 1
            METransformInputStreamStateChanged = METransformMarker + 1
            MEByteStreamCharacteristicsChanged = 700
            MEVideoCaptureDeviceRemoved = 800
            MEVideoCaptureDevicePreempted = 801
            MEStreamSinkFormatInvalidated = 802
            MEEncodingParameters = 803
            MEContentProtectionMetadata = 900
            MEDeviceThermalStateChanged = 950
            MEReservedMax = 10000


        MEUnknown = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEUnknown
        MEError = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEError
        MEExtendedType = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEExtendedType
        MENonFatalError = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MENonFatalError
        MEGenericV1Anchor = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEGenericV1Anchor
        MESessionUnknown = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionUnknown
        MESessionTopologySet = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionTopologySet
        MESessionTopologiesCleared = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionTopologiesCleared
        MESessionStarted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionStarted
        MESessionPaused = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionPaused
        MESessionStopped = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionStopped
        MESessionClosed = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionClosed
        MESessionEnded = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionEnded
        MESessionRateChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionRateChanged
        MESessionScrubSampleComplete = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionScrubSampleComplete
        MESessionCapabilitiesChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionCapabilitiesChanged
        MESessionTopologyStatus = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionTopologyStatus
        MESessionNotifyPresentationTime = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionNotifyPresentationTime
        MENewPresentation = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MENewPresentation
        MELicenseAcquisitionStart = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MELicenseAcquisitionStart
        MELicenseAcquisitionCompleted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MELicenseAcquisitionCompleted
        MEIndividualizationStart = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEIndividualizationStart
        MEIndividualizationCompleted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEIndividualizationCompleted
        MEEnablerProgress = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEEnablerProgress
        MEEnablerCompleted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEEnablerCompleted
        MEPolicyError = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEPolicyError
        MEPolicyReport = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEPolicyReport
        MEBufferingStarted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEBufferingStarted
        MEBufferingStopped = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEBufferingStopped
        MEConnectStart = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEConnectStart
        MEConnectEnd = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEConnectEnd
        MEReconnectStart = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEReconnectStart
        MEReconnectEnd = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEReconnectEnd
        MERendererEvent = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MERendererEvent
        MESessionStreamSinkFormatChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionStreamSinkFormatChanged
        MESessionV1Anchor = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESessionV1Anchor
        MESourceUnknown = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESourceUnknown
        MESourceStarted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESourceStarted
        MEStreamStarted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamStarted
        MESourceSeeked = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESourceSeeked
        MEStreamSeeked = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSeeked
        MENewStream = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MENewStream
        MEUpdatedStream = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEUpdatedStream
        MESourceStopped = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESourceStopped
        MEStreamStopped = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamStopped
        MESourcePaused = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESourcePaused
        MEStreamPaused = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamPaused
        MEEndOfPresentation = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEEndOfPresentation
        MEEndOfStream = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEEndOfStream
        MEMediaSample = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEMediaSample
        MEStreamTick = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamTick
        MEStreamThinMode = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamThinMode
        MEStreamFormatChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamFormatChanged
        MESourceRateChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESourceRateChanged
        MEEndOfPresentationSegment = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEEndOfPresentationSegment
        MESourceCharacteristicsChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESourceCharacteristicsChanged
        MESourceRateChangeRequested = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESourceRateChangeRequested
        MESourceMetadataChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESourceMetadataChanged
        MESequencerSourceTopologyUpdated = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESequencerSourceTopologyUpdated
        MESourceV1Anchor = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESourceV1Anchor
        MESinkUnknown = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESinkUnknown
        MEStreamSinkStarted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSinkStarted
        MEStreamSinkStopped = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSinkStopped
        MEStreamSinkPaused = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSinkPaused
        MEStreamSinkRateChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSinkRateChanged
        MEStreamSinkRequestSample = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSinkRequestSample
        MEStreamSinkMarker = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSinkMarker
        MEStreamSinkPrerolled = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSinkPrerolled
        MEStreamSinkScrubSampleComplete = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSinkScrubSampleComplete
        MEStreamSinkFormatChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSinkFormatChanged
        MEStreamSinkDeviceChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSinkDeviceChanged
        MEQualityNotify = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEQualityNotify
        MESinkInvalidated = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESinkInvalidated
        MEAudioSessionNameChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEAudioSessionNameChanged
        MEAudioSessionVolumeChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEAudioSessionVolumeChanged
        MEAudioSessionDeviceRemoved = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEAudioSessionDeviceRemoved
        MEAudioSessionServerShutdown = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEAudioSessionServerShutdown
        MEAudioSessionGroupingParamChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEAudioSessionGroupingParamChanged
        MEAudioSessionIconChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEAudioSessionIconChanged
        MEAudioSessionFormatChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEAudioSessionFormatChanged
        MEAudioSessionDisconnected = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEAudioSessionDisconnected
        MEAudioSessionExclusiveModeOverride = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEAudioSessionExclusiveModeOverride
        MESinkV1Anchor = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESinkV1Anchor
        MECaptureAudioSessionVolumeChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MECaptureAudioSessionVolumeChanged
        MECaptureAudioSessionDeviceRemoved = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MECaptureAudioSessionDeviceRemoved
        MECaptureAudioSessionFormatChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MECaptureAudioSessionFormatChanged
        MECaptureAudioSessionDisconnected = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MECaptureAudioSessionDisconnected
        MECaptureAudioSessionExclusiveModeOverride = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MECaptureAudioSessionExclusiveModeOverride
        MECaptureAudioSessionServerShutdown = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MECaptureAudioSessionServerShutdown
        MESinkV2Anchor = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MESinkV2Anchor
        METrustUnknown = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.METrustUnknown
        MEPolicyChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEPolicyChanged
        MEContentProtectionMessage = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEContentProtectionMessage
        MEPolicySet = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEPolicySet
        METrustV1Anchor = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.METrustV1Anchor
        MEWMDRMLicenseBackupCompleted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEWMDRMLicenseBackupCompleted
        MEWMDRMLicenseBackupProgress = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEWMDRMLicenseBackupProgress
        MEWMDRMLicenseRestoreCompleted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEWMDRMLicenseRestoreCompleted
        MEWMDRMLicenseRestoreProgress = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEWMDRMLicenseRestoreProgress
        MEWMDRMLicenseAcquisitionCompleted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEWMDRMLicenseAcquisitionCompleted
        MEWMDRMIndividualizationCompleted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEWMDRMIndividualizationCompleted
        MEWMDRMIndividualizationProgress = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEWMDRMIndividualizationProgress
        MEWMDRMProximityCompleted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEWMDRMProximityCompleted
        MEWMDRMLicenseStoreCleaned = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEWMDRMLicenseStoreCleaned
        MEWMDRMRevocationDownloadCompleted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEWMDRMRevocationDownloadCompleted
        MEWMDRMV1Anchor = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEWMDRMV1Anchor
        METransformUnknown = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.METransformUnknown
        METransformNeedInput = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.METransformNeedInput
        METransformHaveOutput = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.METransformHaveOutput
        METransformDrainComplete = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.METransformDrainComplete
        METransformMarker = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.METransformMarker
        METransformInputStreamStateChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.METransformInputStreamStateChanged
        MEByteStreamCharacteristicsChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEByteStreamCharacteristicsChanged
        MEVideoCaptureDeviceRemoved = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEVideoCaptureDeviceRemoved
        MEVideoCaptureDevicePreempted = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEVideoCaptureDevicePreempted
        MEStreamSinkFormatInvalidated = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEStreamSinkFormatInvalidated
        MEEncodingParameters = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEEncodingParameters
        MEContentProtectionMetadata = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEContentProtectionMetadata
        MEDeviceThermalStateChanged = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEDeviceThermalStateChanged
        MEReservedMax = __MIDL___MIDL_itf_mfobjects_0000_0012_0001.MEReservedMax
        MediaEventType = DWORD

        if not defined(__IMFMediaEvent_INTERFACE_DEFINED__):
            # interface IMFMediaEvent
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaEvent = MIDL_INTERFACE(
                    "{DF598932-F10C-4E39-BBA2-C308F101DAA3}"
                )
                IMFMediaEvent._iid_ = IID_IMFMediaEvent

                IMFMediaEvent._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetType')],
                        HRESULT,
                        'GetType',
                        (['out'], POINTER(MediaEventType), 'pmet'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetExtendedType')],
                        HRESULT,
                        'GetExtendedType',
                        (['out'], POINTER(GUID), 'pguidExtendedType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStatus')],
                        HRESULT,
                        'GetStatus',
                        (['out'], POINTER(HRESULT), 'phrStatus'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetValue')],
                        HRESULT,
                        'GetValue',
                        (['out'], POINTER(PROPVARIANT), 'pvValue'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaEvent_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfobjects_0000_0013
        # [local]
        if not defined(__IMFMediaEventGenerator_INTERFACE_DEFINED__):
            # interface IMFMediaEventGenerator
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaEventGenerator = MIDL_INTERFACE(
                    "{2CD0BD52-BCD5-4B89-B62C-EADC0C031E7D}"
                )
                IMFMediaEventGenerator._iid_ = IID_IMFMediaEventGenerator

                IMFMediaEventGenerator._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetEvent')],
                        HRESULT,
                        'GetEvent',
                        (['in'], DWORD, 'dwFlags'),
                        (['out'], POINTER(POINTER(IMFMediaEvent)), 'ppEvent'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginGetEvent'), 'local'],
                        HRESULT,
                        'BeginGetEvent',
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndGetEvent'), 'local'],
                        HRESULT,
                        'EndGetEvent',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                        (['out'], POINTER(POINTER(IMFMediaEvent)), 'ppEvent'),
                    ),
                    COMMETHOD(
                        [helpstring('Method QueueEvent')],
                        HRESULT,
                        'QueueEvent',
                        (['in'], MediaEventType, 'met'),
                        (['in'], REFGUID, 'guidExtendedType'),
                        (['in'], HRESULT, 'hrStatus'),
                        (['unique', 'in'], POINTER(PROPVARIANT), 'pvValue'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaEventGenerator_INTERFACE_DEFINED__
    # interface __MIDL_itf_mfobjects_0000_0014
    # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFRemoteAsyncCallback_INTERFACE_DEFINED__):
            # interface IMFRemoteAsyncCallback
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFRemoteAsyncCallback = MIDL_INTERFACE(
                    "{A27003D0-2354-4F2A-8D6A-AB7CFF15437E}"
                )
                IMFRemoteAsyncCallback._iid_ = IID_IMFRemoteAsyncCallback

                IMFRemoteAsyncCallback._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Invoke')],
                        HRESULT,
                        'Invoke',
                        (['in'], HRESULT, 'hr'),
                        (['in'], POINTER(comtypes.IUnknown), 'pRemoteResult'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFRemoteAsyncCallback_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfobjects_0000_0015
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class _MFBYTESTREAM_SEEK_ORIGIN(ENUM):
            msoBegin = 0
            msoCurrent = msoBegin + 1


        MFBYTESTREAM_SEEK_ORIGIN = _MFBYTESTREAM_SEEK_ORIGIN

        if not defined(__IMFByteStream_INTERFACE_DEFINED__):
            # interface IMFByteStream
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFByteStream = MIDL_INTERFACE(
                    "{AD4C1B00-4BF7-422F-9175-756693D9130D}"
                )
                IMFByteStream._iid_ = IID_IMFByteStream

                IMFByteStream._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCapabilities')],
                        HRESULT,
                        'GetCapabilities',
                        (['out'], POINTER(DWORD), 'pdwCapabilities'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetLength')],
                        HRESULT,
                        'GetLength',
                        (['out'], POINTER(QWORD), 'pqwLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetLength')],
                        HRESULT,
                        'SetLength',
                        (['in'], QWORD, 'qwLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCurrentPosition')],
                        HRESULT,
                        'GetCurrentPosition',
                        (['out'], POINTER(QWORD), 'pqwPosition'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetCurrentPosition')],
                        HRESULT,
                        'SetCurrentPosition',
                        (['in'], QWORD, 'qwPosition'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsEndOfStream')],
                        HRESULT,
                        'IsEndOfStream',
                        (['out'], POINTER(BOOL), 'pfEndOfStream'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Read')],
                        HRESULT,
                        'Read',
                        (['out'], POINTER(BYTE), 'pb'),
                        (['in'], ULONG, 'cb'),
                        (['out'], POINTER(ULONG), 'pcbRead'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginRead'), 'local'],
                        HRESULT,
                        'BeginRead',
                        (['out'], POINTER(BYTE), 'pb'),
                        (['in'], ULONG, 'cb'),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndRead'), 'local'],
                        HRESULT,
                        'EndRead',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                        (['out'], POINTER(ULONG), 'pcbRead'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Write')],
                        HRESULT,
                        'Write',
                        (['in'], POINTER(BYTE), 'pb'),
                        (['in'], ULONG, 'cb'),
                        (['out'], POINTER(ULONG), 'pcbWritten'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginWrite'), 'local'],
                        HRESULT,
                        'BeginWrite',
                        (['in'], POINTER(BYTE), 'pb'),
                        (['in'], ULONG, 'cb'),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndWrite'), 'local'],
                        HRESULT,
                        'EndWrite',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                        (['out'], POINTER(ULONG), 'pcbWritten'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Seek')],
                        HRESULT,
                        'Seek',
                        (['in'], MFBYTESTREAM_SEEK_ORIGIN, 'SeekOrigin'),
                        (['in'], LONGLONG, 'llSeekOffset'),
                        (['in'], DWORD, 'dwSeekFlags'),
                        (['out'], POINTER(QWORD), 'pqwCurrentPosition'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Flush')],
                        HRESULT,
                        'Flush',
                    ),
                    COMMETHOD(
                        [helpstring('Method Close')],
                        HRESULT,
                        'Close',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFByteStream_INTERFACE_DEFINED__
        # interface __MIDL_itf_mfobjects_0000_0016
        # [local]
        if WINVER >= _WIN32_WINNT_WIN7:
            pass
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        if WINVER >= _WIN32_WINNT_WIN8:
            pass
        # END IF   (WINVER >= _WIN32_WINNT_WIN8)

        MF_BYTESTREAM_ORIGIN_NAME = EXTERN_GUID(
            0xFC358288,
            0x3CB6,
            0x460C,
            0xA4,
            0x24,
            0xB6,
            0x68,
            0x12,
            0x60,
            0x37,
            0x5A
        )
        MF_BYTESTREAM_CONTENT_TYPE = EXTERN_GUID(
            0xFC358289,
            0x3CB6,
            0x460C,
            0xA4,
            0x24,
            0xB6,
            0x68,
            0x12,
            0x60,
            0x37,
            0x5A
        )
        MF_BYTESTREAM_DURATION = EXTERN_GUID(
            0xFC35828A,
            0x3CB6,
            0x460C,
            0xA4,
            0x24,
            0xB6,
            0x68,
            0x12,
            0x60,
            0x37,
            0x5A
        )
        MF_BYTESTREAM_LAST_MODIFIED_TIME = EXTERN_GUID(
            0xFC35828B,
            0x3CB6,
            0x460C,
            0xA4,
            0x24,
            0xB6,
            0x68,
            0x12,
            0x60,
            0x37,
            0x5A
        )
        if WINVER >= _WIN32_WINNT_WIN7:
            MF_BYTESTREAM_IFO_FILE_URI = EXTERN_GUID(
                0xFC35828C,
                0x3CB6,
                0x460C,
                0xA4,
                0x24,
                0xB6,
                0x68,
                0x12,
                0x60,
                0x37,
                0x5A
            )
            MF_BYTESTREAM_DLNA_PROFILE_ID = EXTERN_GUID(
                0xFC35828D,
                0x3CB6,
                0x460C,
                0xA4,
                0x24,
                0xB6,
                0x68,
                0x12,
                0x60,
                0x37,
                0x5A
            )
            MF_BYTESTREAM_EFFECTIVE_URL = EXTERN_GUID(
                0x9AFA0209,
                0x89D1,
                0x42AF,
                0x84,
                0x56,
                0x1D,
                0xE6,
                0xB5,
                0x62,
                0xD6,
                0x91
            )
            MF_BYTESTREAM_TRANSCODED = EXTERN_GUID(
                0xB6C5C282,
                0x4DC9,
                0x4DB9,
                0xAB,
                0x48,
                0xCF,
                0x3B,
                0x6D,
                0x8B,
                0xC5,
                0xE0
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        CLSID_MFByteStreamProxyClassFactory = EXTERN_GUID(
            0x770E8E77,
            0x4916,
            0x441C,
            0xA9,
            0xA7,
            0xB3,
            0x42,
            0xD0,
            0xEE,
            0xBC,
            0x71
        )
        if not defined(__IMFByteStreamProxyClassFactory_INTERFACE_DEFINED__):
            # interface IMFByteStreamProxyClassFactory
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFByteStreamProxyClassFactory = MIDL_INTERFACE(
                    "{A6B43F84-5C0A-42E8-A44D-B1857A76992F}"
                )
                IMFByteStreamProxyClassFactory._iid_ = IID_IMFByteStreamProxyClassFactory

                IMFByteStreamProxyClassFactory._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateByteStreamProxy')],
                        HRESULT,
                        'CreateByteStreamProxy',
                        (['in'], POINTER(IMFByteStream), 'pByteStream'),
                        (
                            ['unique', 'in'],
                            POINTER(IMFAttributes),
                            'pAttributes'
                        ),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(LPVOID), 'ppvObject'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFByteStreamProxyClassFactory_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfobjects_0000_0017
        # [local]
        class __MIDL___MIDL_itf_mfobjects_0000_0017_0001(ENUM):
            MF_ACCESSMODE_READ = 1
            MF_ACCESSMODE_WRITE = 2
            MF_ACCESSMODE_READWRITE = 3

        MF_FILE_ACCESSMODE = __MIDL___MIDL_itf_mfobjects_0000_0017_0001


        class __MIDL___MIDL_itf_mfobjects_0000_0017_0002(ENUM):
            MF_OPENMODE_FAIL_IF_NOT_EXIST = 0
            MF_OPENMODE_FAIL_IF_EXIST = 1
            MF_OPENMODE_RESET_IF_EXIST = 2
            MF_OPENMODE_APPEND_IF_EXIST = 3
            MF_OPENMODE_DELETE_IF_EXIST = 4

        MF_FILE_OPENMODE = __MIDL___MIDL_itf_mfobjects_0000_0017_0002


        class __MIDL___MIDL_itf_mfobjects_0000_0017_0003(ENUM):
            MF_FILEFLAGS_NONE = 0
            MF_FILEFLAGS_NOBUFFERING = 0x1
            MF_FILEFLAGS_ALLOW_WRITE_SHARING = 0x2

        MF_FILE_FLAGS = __MIDL___MIDL_itf_mfobjects_0000_0017_0003
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IMFSampleOutputStream_INTERFACE_DEFINED__):
            # interface IMFSampleOutputStream
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSampleOutputStream = MIDL_INTERFACE(
                    "{8FEED468-6F7E-440D-869A-49BDD283AD0D}"
                )
                IMFSampleOutputStream._iid_ = IID_IMFSampleOutputStream

                IMFSampleOutputStream._methods_ = [
                    COMMETHOD(
                        [helpstring('Method BeginWriteSample')],
                        HRESULT,
                        'BeginWriteSample',
                        (['in'], POINTER(IMFSample), 'pSample'),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndWriteSample')],
                        HRESULT,
                        'EndWriteSample',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Close')],
                        HRESULT,
                        'Close',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSampleOutputStream_INTERFACE_DEFINED__

        if not defined(__IMFCollection_INTERFACE_DEFINED__):
            # interface IMFCollection
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFCollection = MIDL_INTERFACE(
                    "{5BC8A76B-869A-46A3-9B03-FA218A66AEBE}"
                )
                IMFCollection._iid_ = IID_IMFCollection

                IMFCollection._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetElementCount')],
                        HRESULT,
                        'GetElementCount',
                        (['out'], POINTER(DWORD), 'pcElements'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetElement')],
                        HRESULT,
                        'GetElement',
                        (['in'], DWORD, 'dwElementIndex'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                            'ppUnkElement'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddElement')],
                        HRESULT,
                        'AddElement',
                        (['in'], POINTER(comtypes.IUnknown), 'pUnkElement'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RemoveElement')],
                        HRESULT,
                        'RemoveElement',
                        (['in'], DWORD, 'dwElementIndex'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                            'ppUnkElement'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method InsertElementAt')],
                        HRESULT,
                        'InsertElementAt',
                        (['in'], DWORD, 'dwIndex'),
                        (['in'], POINTER(comtypes.IUnknown), 'pUnknown'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RemoveAllElements')],
                        HRESULT,
                        'RemoveAllElements',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFCollection_INTERFACE_DEFINED__

        if not defined(__IMFMediaEventQueue_INTERFACE_DEFINED__):
            # interface IMFMediaEventQueue
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaEventQueue = MIDL_INTERFACE(
                    "{36F846FC-2256-48B6-B58E-E2B638316581}"
                )
                IMFMediaEventQueue._iid_ = IID_IMFMediaEventQueue

                IMFMediaEventQueue._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetEvent')],
                        HRESULT,
                        'GetEvent',
                        (['in'], DWORD, 'dwFlags'),
                        (['out'], POINTER(POINTER(IMFMediaEvent)), 'ppEvent'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginGetEvent')],
                        HRESULT,
                        'BeginGetEvent',
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndGetEvent')],
                        HRESULT,
                        'EndGetEvent',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                        (['out'], POINTER(POINTER(IMFMediaEvent)), 'ppEvent'),
                    ),
                    COMMETHOD(
                        [helpstring('Method QueueEvent')],
                        HRESULT,
                        'QueueEvent',
                        (['in'], POINTER(IMFMediaEvent), 'pEvent'),
                    ),
                    COMMETHOD(
                        [helpstring('Method QueueEventParamVar')],
                        HRESULT,
                        'QueueEventParamVar',
                        (['in'], MediaEventType, 'met'),
                        (['in'], REFGUID, 'guidExtendedType'),
                        (['in'], HRESULT, 'hrStatus'),
                        (['unique', 'in'], POINTER(PROPVARIANT), 'pvValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method QueueEventParamUnk')],
                        HRESULT,
                        'QueueEventParamUnk',
                        (['in'], MediaEventType, 'met'),
                        (['in'], REFGUID, 'guidExtendedType'),
                        (['in'], HRESULT, 'hrStatus'),
                        (
                            ['unique', 'in'],
                            POINTER(comtypes.IUnknown),
                            'pUnk'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Shutdown')],
                        HRESULT,
                        'Shutdown',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaEventQueue_INTERFACE_DEFINED__

        if not defined(__IMFActivate_INTERFACE_DEFINED__):
            # interface IMFActivate
            # [unique][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFActivate = MIDL_INTERFACE(
                    "{7FEE9E9A-4A89-47A6-899C-B6A53A70FB67}"
                )
                IMFActivate._iid_ = IID_IMFActivate

                IMFActivate._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ActivateObject')],
                        HRESULT,
                        'ActivateObject',
                        (['in'], REFIID, 'riid'),
                        (
                            ['out', 'retval', 'iid_is'],
                            POINTER(POINTER(VOID)),
                           'ppv'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ShutdownObject')],
                        HRESULT,
                        'ShutdownObject',
                    ),
                    COMMETHOD(
                        [helpstring('Method DetachObject')],
                        HRESULT,
                        'DetachObject',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFActivate_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfobjects_0000_0021
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            class _MF_Plugin_Type(ENUM):
                MF_Plugin_Type_MFT = 0
                MF_Plugin_Type_MediaSource = 1
                MF_Plugin_Type_MFT_MatchOutputType = 2
                MF_Plugin_Type_Other = -1


            MF_Plugin_Type = _MF_Plugin_Type

            if not defined(__IMFPluginControl_INTERFACE_DEFINED__):
                # interface IMFPluginControl
                # [unique][helpstring][uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFPluginControl = MIDL_INTERFACE(
                        "{5C6C44BF-1DB6-435B-9249-E8CD10FDEC96}"
                    )
                    IMFPluginControl._iid_ = IID_IMFPluginControl

                    IMFPluginControl._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetPreferredClsid')],
                            HRESULT,
                            'GetPreferredClsid',
                            (['in'], DWORD, 'pluginType'),
                            (['in'], LPCWSTR, 'selector'),
                            (['out'], POINTER(CLSID), 'clsid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPreferredClsidByIndex')],
                            HRESULT,
                            'GetPreferredClsidByIndex',
                            (['in'], DWORD, 'pluginType'),
                            (['in'], DWORD, 'index'),
                            (['out'], POINTER(LPWSTR), 'selector'),
                            (['out'], POINTER(CLSID), 'clsid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetPreferredClsid')],
                            HRESULT,
                            'SetPreferredClsid',
                            (['in'], DWORD, 'pluginType'),
                            (['in'], LPCWSTR, 'selector'),
                            (['in'], POINTER(CLSID), 'clsid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method IsDisabled')],
                            HRESULT,
                            'IsDisabled',
                            (['in'], DWORD, 'pluginType'),
                            (['in'], REFCLSID, 'clsid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDisabledByIndex')],
                            HRESULT,
                            'GetDisabledByIndex',
                            (['in'], DWORD, 'pluginType'),
                            (['in'], DWORD, 'index'),
                            (['out'], POINTER(CLSID), 'clsid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetDisabled')],
                            HRESULT,
                            'SetDisabled',
                            (['in'], DWORD, 'pluginType'),
                            (['in'], REFCLSID, 'clsid'),
                            (['in'], BOOL, 'disabled'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFPluginControl_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfobjects_0000_0022
            # [local]
            class MF_PLUGIN_CONTROL_POLICY(ENUM):
                MF_PLUGIN_CONTROL_POLICY_USE_ALL_PLUGINS = 0
                MF_PLUGIN_CONTROL_POLICY_USE_APPROVED_PLUGINS = 1
                MF_PLUGIN_CONTROL_POLICY_USE_WEB_PLUGINS = 2
                MF_PLUGIN_CONTROL_POLICY_USE_WEB_PLUGINS_EDGEMODE = 3

            if not defined(__IMFPluginControl2_INTERFACE_DEFINED__):
                # interface IMFPluginControl2
                # [unique][helpstring][uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFPluginControl2 = MIDL_INTERFACE(
                        "{C6982083-3DDC-45CB-AF5E-0F7A8CE4DE77}"
                    )
                    IMFPluginControl2._iid_ = IID_IMFPluginControl2

                    IMFPluginControl2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetPolicy')],
                            HRESULT,
                            'SetPolicy',
                            (['in'], MF_PLUGIN_CONTROL_POLICY, 'policy'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFPluginControl2_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfobjects_0000_0023
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IMFDXGIDeviceManager_INTERFACE_DEFINED__):
                # interface IMFDXGIDeviceManager
                # [unique][helpstring][uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFDXGIDeviceManager = MIDL_INTERFACE(
                        "{EB533D5D-2DB6-40F8-97A9-494692014F07}"
                    )
                    IMFDXGIDeviceManager._iid_ = IID_IMFDXGIDeviceManager

                    IMFDXGIDeviceManager._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CloseDeviceHandle')],
                            HRESULT,
                            'CloseDeviceHandle',
                            (['in'], HANDLE, 'hDevice'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetVideoService')],
                            HRESULT,
                            'GetVideoService',
                            (['in'], HANDLE, 'hDevice'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppService'),
                        ),
                        COMMETHOD(
                            [helpstring('Method LockDevice')],
                            HRESULT,
                            'LockDevice',
                            (['in'], HANDLE, 'hDevice'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppUnkDevice'),
                            (['in'], BOOL, 'fBlock'),
                        ),
                        COMMETHOD(
                            [helpstring('Method OpenDeviceHandle')],
                            HRESULT,
                            'OpenDeviceHandle',
                            (['out'], POINTER(HANDLE), 'phDevice'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ResetDevice')],
                            HRESULT,
                            'ResetDevice',
                            (
                                ['in'],
                                POINTER(comtypes.IUnknown),
                                'pUnkDevice'
                            ),
                            (['in'], UINT, 'resetToken'),
                        ),
                        COMMETHOD(
                            [helpstring('Method TestDevice')],
                            HRESULT,
                            'TestDevice',
                            (['in'], HANDLE, 'hDevice'),
                        ),
                        COMMETHOD(
                            [helpstring('Method UnlockDevice')],
                            HRESULT,
                            'UnlockDevice',
                            (['in'], HANDLE, 'hDevice'),
                            (['in'], BOOL, 'fSaveState'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFDXGIDeviceManager_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfobjects_0000_0024
            # [local]
            class _MF_STREAM_STATE(ENUM):
                MF_STREAM_STATE_STOPPED = 0
                MF_STREAM_STATE_PAUSED = MF_STREAM_STATE_STOPPED + 1
                MF_STREAM_STATE_RUNNING = MF_STREAM_STATE_PAUSED + 1


            MF_STREAM_STATE = _MF_STREAM_STATE

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if NTDDI_VERSION >= NTDDI_WIN10_RS2:
            if not defined(__IMFMuxStreamAttributesManager_INTERFACE_DEFINED__):
                # interface IMFMuxStreamAttributesManager
                # [unique][helpstring][uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMuxStreamAttributesManager = MIDL_INTERFACE(
                        "{CE8BD576-E440-43B3-BE34-1E53F565F7E8}"
                    )
                    IMFMuxStreamAttributesManager._iid_ = IID_IMFMuxStreamAttributesManager

                    IMFMuxStreamAttributesManager._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetStreamCount')],
                            HRESULT,
                            'GetStreamCount',
                            (['out'], POINTER(DWORD), 'pdwMuxStreamCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAttributes')],
                            HRESULT,
                            'GetAttributes',
                            (['in'], DWORD, 'dwMuxStreamIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFAttributes)),
                                'ppStreamAttributes'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMuxStreamAttributesManager_INTERFACE_DEFINED__

            if not defined(__IMFMuxStreamMediaTypeManager_INTERFACE_DEFINED__):
                # interface IMFMuxStreamMediaTypeManager
                # [unique][helpstring][uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMuxStreamMediaTypeManager = MIDL_INTERFACE(
                        "{505A2C72-42F7-4690-AEAB-8F513D0FFDB8}"
                    )
                    IMFMuxStreamMediaTypeManager._iid_ = IID_IMFMuxStreamMediaTypeManager

                    IMFMuxStreamMediaTypeManager._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetStreamCount')],
                            HRESULT,
                            'GetStreamCount',
                            (['out'], POINTER(DWORD), 'pdwMuxStreamCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMediaType')],
                            HRESULT,
                            'GetMediaType',
                            (['in'], DWORD, 'dwMuxStreamIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaType)),
                                'ppMediaType'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStreamConfigurationCount')],
                            HRESULT,
                            'GetStreamConfigurationCount',
                            (['out'], POINTER(DWORD), 'pdwCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddStreamConfiguration')],
                            HRESULT,
                            'AddStreamConfiguration',
                            (['in'], ULONGLONG, 'ullStreamMask'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveStreamConfiguration')],
                            HRESULT,
                            'RemoveStreamConfiguration',
                            (['in'], ULONGLONG, 'ullStreamMask'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStreamConfiguration')],
                            HRESULT,
                            'GetStreamConfiguration',
                            (['in'], DWORD, 'ulIndex'),
                            (['out'], POINTER(ULONGLONG), 'pullStreamMask'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMuxStreamMediaTypeManager_INTERFACE_DEFINED__

            if not defined(__IMFMuxStreamSampleManager_INTERFACE_DEFINED__):
                # interface IMFMuxStreamSampleManager
                # [unique][helpstring][uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMuxStreamSampleManager = MIDL_INTERFACE(
                        "{74ABBC19-B1CC-4E41-BB8B-9D9B86A8F6CA}"
                    )
                    IMFMuxStreamSampleManager._iid_ = IID_IMFMuxStreamSampleManager

                    IMFMuxStreamSampleManager._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetStreamCount')],
                            HRESULT,
                            'GetStreamCount',
                            (['out'], POINTER(DWORD), 'pdwMuxStreamCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSample')],
                            HRESULT,
                            'GetSample',
                            (['in'], DWORD, 'dwMuxStreamIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFSample)),
                                'ppSample'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStreamConfiguration')],
                            ULONGLONG,
                            'GetStreamConfiguration',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMuxStreamSampleManager_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfobjects_0000_0027
            # [local]
        # END IF   (WINVER  >= _WIN32_WINNT_WIN10_RS2)
    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # Additional Prototypes for ALL interfaces
    oleaut32 = ctypes.windll.OLEAUT32

    # ULONG              BSTR_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize = oleaut32.BSTR_UserSize
    BSTR_UserSize.restype = ULONG

    # UCHAR *  BSTR_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal = oleaut32.BSTR_UserMarshal
    BSTR_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  BSTR_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal = oleaut32.BSTR_UserUnmarshal
    BSTR_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       BSTR_UserFree(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree = oleaut32.BSTR_UserFree
    BSTR_UserFree.restype = VOID

    # ULONG              LPSAFEARRAY_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserSize = oleaut32.LPSAFEARRAY_UserSize
    LPSAFEARRAY_UserSize.restype = ULONG

    # UCHAR *  LPSAFEARRAY_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserMarshal = oleaut32.LPSAFEARRAY_UserMarshal
    LPSAFEARRAY_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  LPSAFEARRAY_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out LPSAFEARRAY * );
    LPSAFEARRAY_UserUnmarshal = oleaut32.LPSAFEARRAY_UserUnmarshal
    LPSAFEARRAY_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       LPSAFEARRAY_UserFree(     __RPC__in ULONG *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserFree = oleaut32.LPSAFEARRAY_UserFree
    LPSAFEARRAY_UserFree.restype = VOID

    # ULONG              BSTR_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize64 = oleaut32.BSTR_UserSize64
    BSTR_UserSize64.restype = ULONG

    # UCHAR *  BSTR_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal64 = oleaut32.BSTR_UserMarshal64
    BSTR_UserMarshal64.restype = POINTER(UCHAR)


    # UCHAR *  BSTR_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal64 = oleaut32.BSTR_UserUnmarshal64
    BSTR_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       BSTR_UserFree64(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree64 = oleaut32.BSTR_UserFree64
    BSTR_UserFree64.restype = VOID

    # ULONG              LPSAFEARRAY_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserSize64 = oleaut32.LPSAFEARRAY_UserSize64
    LPSAFEARRAY_UserSize64.restype = ULONG


    # UCHAR *  LPSAFEARRAY_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserMarshal64 = oleaut32.LPSAFEARRAY_UserMarshal64
    LPSAFEARRAY_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  LPSAFEARRAY_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out LPSAFEARRAY * );
    LPSAFEARRAY_UserUnmarshal64 = oleaut32.LPSAFEARRAY_UserUnmarshal64
    LPSAFEARRAY_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       LPSAFEARRAY_UserFree64(     __RPC__in ULONG *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserFree64 = oleaut32.LPSAFEARRAY_UserFree64
    LPSAFEARRAY_UserFree64.restype = VOID

    # end of Additional Prototypes

    if defined(__cplusplus):
        pass
    # END IF

# END IF


