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
__spatialaudiometadata_h__ = None
__ISpatialAudioMetadataItems_FWD_DEFINED__ = None
__ISpatialAudioMetadataWriter_FWD_DEFINED__ = None
__ISpatialAudioMetadataReader_FWD_DEFINED__ = None
__ISpatialAudioMetadataCopier_FWD_DEFINED__ = None
__ISpatialAudioMetadataItemsBuffer_FWD_DEFINED__ = None
__ISpatialAudioMetadataClient_FWD_DEFINED__ = None
__ISpatialAudioObjectForMetadataCommands_FWD_DEFINED__ = None
__ISpatialAudioObjectForMetadataItems_FWD_DEFINED__ = None
__ISpatialAudioObjectRenderStreamForMetadata_FWD_DEFINED__ = None
__ISpatialAudioMetadataItems_INTERFACE_DEFINED__ = None
__ISpatialAudioMetadataWriter_INTERFACE_DEFINED__ = None
__ISpatialAudioMetadataReader_INTERFACE_DEFINED__ = None
__ISpatialAudioMetadataCopier_INTERFACE_DEFINED__ = None
__ISpatialAudioMetadataItemsBuffer_INTERFACE_DEFINED__ = None
__ISpatialAudioMetadataClient_INTERFACE_DEFINED__ = None
__ISpatialAudioObjectForMetadataCommands_INTERFACE_DEFINED__ = None
__ISpatialAudioObjectForMetadataItems_INTERFACE_DEFINED__ = None
__ISpatialAudioObjectRenderStreamForMetadata_INTERFACE_DEFINED__ = None


class SpatialAudioMetadataItemsInfo(ctypes.Structure):
    pass


class SpatialAudioObjectRenderStreamForMetadataActivationParams(ctypes.Structure):
    pass


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

if not defined(__spatialaudiometadata_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__ISpatialAudioMetadataItems_FWD_DEFINED__):
        class ISpatialAudioMetadataItems(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None
    # END IF  __ISpatialAudioMetadataItems_FWD_DEFINED__

    if not defined(__ISpatialAudioMetadataWriter_FWD_DEFINED__):
        class ISpatialAudioMetadataWriter(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioMetadataWriter_FWD_DEFINED__

    if not defined(__ISpatialAudioMetadataReader_FWD_DEFINED__):
        class ISpatialAudioMetadataReader(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioMetadataReader_FWD_DEFINED__

    if not defined(__ISpatialAudioMetadataCopier_FWD_DEFINED__):
        class ISpatialAudioMetadataCopier(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioMetadataCopier_FWD_DEFINED__

    if not defined(__ISpatialAudioMetadataItemsBuffer_FWD_DEFINED__):
        class ISpatialAudioMetadataItemsBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioMetadataItemsBuffer_FWD_DEFINED__

    if not defined(__ISpatialAudioMetadataClient_FWD_DEFINED__):
        class ISpatialAudioMetadataClient(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioMetadataClient_FWD_DEFINED__

    if not defined(__ISpatialAudioObjectForMetadataCommands_FWD_DEFINED__):
        class ISpatialAudioObjectForMetadataCommands(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioObjectForMetadataCommands_FWD_DEFINED__

    if not defined(__ISpatialAudioObjectForMetadataItems_FWD_DEFINED__):
        class ISpatialAudioObjectForMetadataItems(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioObjectForMetadataItems_FWD_DEFINED__

    if not defined(__ISpatialAudioObjectRenderStreamForMetadata_FWD_DEFINED__):
        class ISpatialAudioObjectRenderStreamForMetadata(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioObjectRenderStreamForMetadata_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.shared.wtypes_h import * # NOQA
    from pyWinAPI.um.unknwn_h import * # NOQA
    from pyWinAPI.winrt.hstring_h import * # NOQA
    from pyWinAPI.um.propidl_h import * # NOQA
    from pyWinAPI.um.spatialaudioclient_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_spatialaudiometadata_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class SpatialAudioMetadataWriterOverflowMode(ENUM):
            SpatialAudioMetadataWriterOverflow_Fail = 0
            SpatialAudioMetadataWriterOverflow_MergeWithNew = (
                SpatialAudioMetadataWriterOverflow_Fail + 1
            )
            SpatialAudioMetadataWriterOverflow_MergeWithLast = (
                SpatialAudioMetadataWriterOverflow_MergeWithNew + 1
            )


        class SpatialAudioMetadataCopyMode(ENUM):
            SpatialAudioMetadataCopy_Overwrite = 0
            SpatialAudioMetadataCopy_Append = (
                SpatialAudioMetadataCopy_Overwrite + 1
            )
            SpatialAudioMetadataCopy_AppendMergeWithLast = (
                SpatialAudioMetadataCopy_Append + 1
            )
            SpatialAudioMetadataCopy_AppendMergeWithFirst = (
                SpatialAudioMetadataCopy_AppendMergeWithLast + 1
            )

        SpatialAudioMetadataItemsInfo._fields_ = [
            ('FrameCount', UINT16),
            ('ItemCount', UINT16),
            ('MaxItemCount', UINT16),
            ('MaxValueBufferLength', UINT32),
        ]

        SpatialAudioObjectRenderStreamForMetadataActivationParams._fields_ = [
            ('ObjectFormat', POINTER(WAVEFORMATEX)),
            ('StaticObjectTypeMask', AudioObjectType),
            ('MinDynamicObjectCount', UINT32),
            ('MaxDynamicObjectCount', UINT32),
            ('Category', AUDIO_STREAM_CATEGORY),
            ('EventHandle', HANDLE),
            ('MetadataFormatId', GUID),
            ('MaxMetadataItemCount', UINT16),
            ('MetadataActivationParams', POINTER(PROPVARIANT)),
            ('NotifyObject', POINTER(ISpatialAudioObjectRenderStreamNotify)),
        ]
        if not defined(__ISpatialAudioMetadataItems_INTERFACE_DEFINED__):
            # interface ISpatialAudioMetadataItems
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioMetadataItems = MIDL_INTERFACE(
                    "{BCD7C78F-3098-4F22-B547-A2F25A381269}"
                )
                ISpatialAudioMetadataItems._iid_ = IID_ISpatialAudioMetadataItems

                ISpatialAudioMetadataItems._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetFrameCount')],
                        HRESULT,
                        'GetFrameCount',
                        (['out'], POINTER(UINT16), 'frameCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetItemCount')],
                        HRESULT,
                        'GetItemCount',
                        (['out'], POINTER(UINT16), 'itemCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMaxItemCount')],
                        HRESULT,
                        'GetMaxItemCount',
                        (['out'], POINTER(UINT16), 'maxItemCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMaxValueBufferLength')],
                        HRESULT,
                        'GetMaxValueBufferLength',
                        (['out'], POINTER(UINT32), 'maxValueBufferLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInfo')],
                        HRESULT,
                        'GetInfo',
                        (
                            ['out'],
                            POINTER(SpatialAudioMetadataItemsInfo),
                            'info'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioMetadataItems_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioMetadataWriter_INTERFACE_DEFINED__):
            # interface ISpatialAudioMetadataWriter
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioMetadataWriter = MIDL_INTERFACE(
                    "{1B17CA01-2955-444D-A430-537DC589A844}"
                )
                ISpatialAudioMetadataWriter._iid_ = IID_ISpatialAudioMetadataWriter

                ISpatialAudioMetadataWriter._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Open')],
                        HRESULT,
                        'Open',
                        (
                            ['in'],
                            POINTER(ISpatialAudioMetadataItems),
                            'metadataItems'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method WriteNextItem')],
                        HRESULT,
                        'WriteNextItem',
                        (['in'], UINT16, 'frameOffset'),
                    ),
                    COMMETHOD(
                        [helpstring('Method WriteNextItemCommand')],
                        HRESULT,
                        'WriteNextItemCommand',
                        (['in'], BYTE, 'commandID'),
                        (['in'], POINTER(VOID), 'valueBuffer'),
                        (['in'], UINT32, 'valueBufferLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Close')],
                        HRESULT,
                        'Close',
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioMetadataWriter_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioMetadataReader_INTERFACE_DEFINED__):
            # interface ISpatialAudioMetadataReader
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioMetadataReader = MIDL_INTERFACE(
                    "{B78E86A2-31D9-4C32-94D2-7DF40FC7EBEC}"
                )
                ISpatialAudioMetadataReader._iid_ = IID_ISpatialAudioMetadataReader

                ISpatialAudioMetadataReader._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Open')],
                        HRESULT,
                        'Open',
                        (
                            ['in'],
                            POINTER(ISpatialAudioMetadataItems),
                            'metadataItems'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReadNextItem')],
                        HRESULT,
                        'ReadNextItem',
                        (['out'], POINTER(UINT8), 'commandCount'),
                        (['out'], POINTER(UINT16), 'frameOffset'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReadNextItemCommand')],
                        HRESULT,
                        'ReadNextItemCommand',
                        (['out'], POINTER(BYTE), 'commandID'),
                        (['out'], POINTER(VOID), 'valueBuffer'),
                        (['in'], UINT32, 'maxValueBufferLength'),
                        (['out'], POINTER(UINT32), 'valueBufferLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Close')],
                        HRESULT,
                        'Close',
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioMetadataReader_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioMetadataCopier_INTERFACE_DEFINED__):
            # interface ISpatialAudioMetadataCopier
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioMetadataCopier = MIDL_INTERFACE(
                    "{D224B233-E251-4FD0-9CA2-D5ECF9A68404}"
                )
                ISpatialAudioMetadataCopier._iid_ = IID_ISpatialAudioMetadataCopier

                ISpatialAudioMetadataCopier._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Open')],
                        HRESULT,
                        'Open',
                        (
                            ['in'],
                            POINTER(ISpatialAudioMetadataItems),
                            'metadataItems'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method CopyMetadataForFrames')],
                        HRESULT,
                        'CopyMetadataForFrames',
                        (['in'], UINT16, 'copyFrameCount'),
                        (['in'], SpatialAudioMetadataCopyMode, 'copyMode'),
                        (
                            ['in'],
                            POINTER(ISpatialAudioMetadataItems),
                            'dstMetadataItems'
                        ),
                        (['out'], POINTER(UINT16), 'itemsCopied'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Close')],
                        HRESULT,
                        'Close',
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioMetadataCopier_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioMetadataItemsBuffer_INTERFACE_DEFINED__):
            # interface ISpatialAudioMetadataItemsBuffer
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioMetadataItemsBuffer = MIDL_INTERFACE(
                    "{42640A16-E1BD-42D9-9FF6-031AB71A2DBA}"
                )
                ISpatialAudioMetadataItemsBuffer._iid_ = IID_ISpatialAudioMetadataItemsBuffer

                ISpatialAudioMetadataItemsBuffer._methods_ = [
                    COMMETHOD(
                        [helpstring('Method AttachToBuffer')],
                        HRESULT,
                        'AttachToBuffer',
                        (['out'], POINTER(BYTE), 'buffer'),
                        (['in'], UINT32, 'bufferLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AttachToPopulatedBuffer')],
                        HRESULT,
                        'AttachToPopulatedBuffer',
                        (['out'], POINTER(BYTE), 'buffer'),
                        (['in'], UINT32, 'bufferLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DetachBuffer')],
                        HRESULT,
                        'DetachBuffer',
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioMetadataItemsBuffer_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioMetadataClient_INTERFACE_DEFINED__):
            # interface ISpatialAudioMetadataClient
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioMetadataClient = MIDL_INTERFACE(
                    "{777D4A3B-F6FF-4A26-85DC-68D7CDEDA1D4}"
                )
                ISpatialAudioMetadataClient._iid_ = IID_ISpatialAudioMetadataClient

                ISpatialAudioMetadataClient._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ActivateSpatialAudioMetadataItems')],
                        HRESULT,
                        'ActivateSpatialAudioMetadataItems',
                        (['in'], UINT16, 'maxItemCount'),
                        (['in'], UINT16, 'frameCount'),
                        (
                            ['out'],
                            POINTER(POINTER(ISpatialAudioMetadataItemsBuffer)),
                            'metadataItemsBuffer'
                        ),
                        (
                            ['out'],
                            POINTER(POINTER(ISpatialAudioMetadataItems)),
                            'metadataItems'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSpatialAudioMetadataItemsBufferLength')],
                        HRESULT,
                        'GetSpatialAudioMetadataItemsBufferLength',
                        (['in'], UINT16, 'maxItemCount'),
                        (['out'], POINTER(UINT32), 'bufferLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ActivateSpatialAudioMetadataWriter')],
                        HRESULT,
                        'ActivateSpatialAudioMetadataWriter',
                        (
                            ['in'],
                            SpatialAudioMetadataWriterOverflowMode,
                            'overflowMode'
                        ),
                        (
                            ['out'],
                            POINTER(POINTER(ISpatialAudioMetadataWriter)),
                            'metadataWriter'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ActivateSpatialAudioMetadataCopier')],
                        HRESULT,
                        'ActivateSpatialAudioMetadataCopier',
                        (
                            ['out'],
                            POINTER(POINTER(ISpatialAudioMetadataCopier)),
                            'metadataCopier'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ActivateSpatialAudioMetadataReader')],
                        HRESULT,
                        'ActivateSpatialAudioMetadataReader',
                        (
                            ['out'],
                            POINTER(POINTER(ISpatialAudioMetadataReader)),
                            'metadataReader'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioMetadataClient_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioObjectForMetadataCommands_INTERFACE_DEFINED__):
            # interface ISpatialAudioObjectForMetadataCommands
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioObjectForMetadataCommands = MIDL_INTERFACE(
                    "{0DF2C94B-F5F9-472D-AF6B-C46E0AC9CD05}"
                )
                ISpatialAudioObjectForMetadataCommands._iid_ = IID_ISpatialAudioObjectForMetadataCommands

                ISpatialAudioObjectForMetadataCommands._methods_ = [
                    COMMETHOD(
                        [helpstring('Method WriteNextMetadataCommand')],
                        HRESULT,
                        'WriteNextMetadataCommand',
                        (['in'], BYTE, 'commandID'),
                        (['in'], POINTER(VOID), 'valueBuffer'),
                        (['in'], UINT32, 'valueBufferLength'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioObjectForMetadataCommands_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioObjectForMetadataItems_INTERFACE_DEFINED__):
            # interface ISpatialAudioObjectForMetadataItems
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioObjectForMetadataItems = MIDL_INTERFACE(
                    "{DDEA49FF-3BC0-4377-8AAD-9FBCFD808566}"
                )
                ISpatialAudioObjectForMetadataItems._iid_ = IID_ISpatialAudioObjectForMetadataItems

                ISpatialAudioObjectForMetadataItems._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetSpatialAudioMetadataItems')],
                        HRESULT,
                        'GetSpatialAudioMetadataItems',
                        (
                            ['out'],
                            POINTER(POINTER(ISpatialAudioMetadataItems)),
                            'metadataItems'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioObjectForMetadataItems_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioObjectRenderStreamForMetadata_INTERFACE_DEFINED__):
            # interface ISpatialAudioObjectRenderStreamForMetadata
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioObjectRenderStreamForMetadata = MIDL_INTERFACE(
                    "{BBC9C907-48D5-4A2E-A0C7-F7F0D67C1FB1}"
                )
                ISpatialAudioObjectRenderStreamForMetadata._iid_ = IID_ISpatialAudioObjectRenderStreamForMetadata

                ISpatialAudioObjectRenderStreamForMetadata._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ActivateSpatialAudioObjectForMetadataCommands')],
                        HRESULT,
                        'ActivateSpatialAudioObjectForMetadataCommands',
                        (['in'], AudioObjectType, 'type'),
                        (
                            ['out'],
                            POINTER(POINTER(ISpatialAudioObjectForMetadataCommands)),
                            'audioObject'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ActivateSpatialAudioObjectForMetadataItems')],
                        HRESULT,
                        'ActivateSpatialAudioObjectForMetadataItems',
                        (['in'], AudioObjectType, 'type'),
                        (
                            ['out'],
                            POINTER(POINTER(ISpatialAudioObjectForMetadataItems)),
                            'audioObject'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioObjectRenderStreamForMetadata_INTERFACE_DEFINED__

        # interface __MIDL_itf_spatialaudiometadata_0000_0009
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


