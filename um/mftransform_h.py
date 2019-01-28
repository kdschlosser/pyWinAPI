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
__mftransform_h__ = None
__IMFTransform_FWD_DEFINED__ = None
__IMFDeviceTransform_FWD_DEFINED__ = None
__IMFDeviceTransformCallback_FWD_DEFINED__ = None
MFT_UNIQUE_METHOD_NAMES = None
__IMFTransform_INTERFACE_DEFINED__ = None
__IMFDeviceTransform_INTERFACE_DEFINED__ = None
__IMFDeviceTransformCallback_INTERFACE_DEFINED__ = None


class _MFT_INPUT_STREAM_INFO(ctypes.Structure):
    pass


MFT_INPUT_STREAM_INFO = _MFT_INPUT_STREAM_INFO


class _MFT_OUTPUT_STREAM_INFO(ctypes.Structure):
    pass


MFT_OUTPUT_STREAM_INFO = _MFT_OUTPUT_STREAM_INFO


class _MFT_OUTPUT_DATA_BUFFER(ctypes.Structure):
    pass


MFT_OUTPUT_DATA_BUFFER = _MFT_OUTPUT_DATA_BUFFER


class _STREAM_MEDIUM(ctypes.Structure):
    pass


STREAM_MEDIUM = _STREAM_MEDIUM


class MFAudioDecoderDegradationInfo(ctypes.Structure):
    pass





class _MFT_STREAM_STATE_PARAM(ctypes.Structure):
    pass


MFT_STREAM_STATE_PARAM = _MFT_STREAM_STATE_PARAM



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

    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF


if not defined(__mftransform_h__):
    # Forward Declarations
    if not defined(__IMFTransform_FWD_DEFINED__):
        class IMFTransform(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None

    # END IF  __IMFTransform_FWD_DEFINED__

    if not defined(__IMFDeviceTransform_FWD_DEFINED__):
        class IMFDeviceTransform(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFDeviceTransform_FWD_DEFINED__

    if not defined(__IMFDeviceTransformCallback_FWD_DEFINED__):
        class IMFDeviceTransformCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFDeviceTransformCallback_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.mfobjects_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_mftransform_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class _MFT_INPUT_DATA_BUFFER_FLAGS(ENUM):
            MFT_INPUT_DATA_BUFFER_PLACEHOLDER = 0xFFFFFFFF

        MFT_INPUT_DATA_BUFFER_PLACEHOLDER = _MFT_INPUT_DATA_BUFFER_FLAGS.MFT_INPUT_DATA_BUFFER_PLACEHOLDER


        class _MFT_OUTPUT_DATA_BUFFER_FLAGS(ENUM):
            MFT_OUTPUT_DATA_BUFFER_INCOMPLETE = 0x1000000
            MFT_OUTPUT_DATA_BUFFER_FORMAT_CHANGE = 0x100
            MFT_OUTPUT_DATA_BUFFER_STREAM_END = 0x200
            MFT_OUTPUT_DATA_BUFFER_NO_SAMPLE = 0x300

        MFT_OUTPUT_DATA_BUFFER_INCOMPLETE = _MFT_OUTPUT_DATA_BUFFER_FLAGS.MFT_OUTPUT_DATA_BUFFER_INCOMPLETE
        MFT_OUTPUT_DATA_BUFFER_FORMAT_CHANGE = _MFT_OUTPUT_DATA_BUFFER_FLAGS.MFT_OUTPUT_DATA_BUFFER_FORMAT_CHANGE
        MFT_OUTPUT_DATA_BUFFER_STREAM_END = _MFT_OUTPUT_DATA_BUFFER_FLAGS.MFT_OUTPUT_DATA_BUFFER_STREAM_END
        MFT_OUTPUT_DATA_BUFFER_NO_SAMPLE = _MFT_OUTPUT_DATA_BUFFER_FLAGS.MFT_OUTPUT_DATA_BUFFER_NO_SAMPLE


        class _MFT_INPUT_STATUS_FLAGS(ENUM):
            MFT_INPUT_STATUS_ACCEPT_DATA = 0x1

        MFT_INPUT_STATUS_ACCEPT_DATA = _MFT_INPUT_STATUS_FLAGS.MFT_INPUT_STATUS_ACCEPT_DATA


        class _MFT_OUTPUT_STATUS_FLAGS(ENUM):
            MFT_OUTPUT_STATUS_SAMPLE_READY = 0x1

        MFT_OUTPUT_STATUS_SAMPLE_READY = _MFT_OUTPUT_STATUS_FLAGS.MFT_OUTPUT_STATUS_SAMPLE_READY


        class _MFT_INPUT_STREAM_INFO_FLAGS(ENUM):
            MFT_INPUT_STREAM_WHOLE_SAMPLES = 0x1
            MFT_INPUT_STREAM_SINGLE_SAMPLE_PER_BUFFER = 0x2
            MFT_INPUT_STREAM_FIXED_SAMPLE_SIZE = 0x4
            MFT_INPUT_STREAM_HOLDS_BUFFERS = 0x8
            MFT_INPUT_STREAM_DOES_NOT_ADDREF = 0x100
            MFT_INPUT_STREAM_REMOVABLE = 0x200
            MFT_INPUT_STREAM_OPTIONAL = 0x400
            MFT_INPUT_STREAM_PROCESSES_IN_PLACE = 0x800

        MFT_INPUT_STREAM_WHOLE_SAMPLES = _MFT_INPUT_STREAM_INFO_FLAGS.MFT_INPUT_STREAM_WHOLE_SAMPLES
        MFT_INPUT_STREAM_SINGLE_SAMPLE_PER_BUFFER = _MFT_INPUT_STREAM_INFO_FLAGS.MFT_INPUT_STREAM_SINGLE_SAMPLE_PER_BUFFER
        MFT_INPUT_STREAM_FIXED_SAMPLE_SIZE = _MFT_INPUT_STREAM_INFO_FLAGS.MFT_INPUT_STREAM_FIXED_SAMPLE_SIZE
        MFT_INPUT_STREAM_HOLDS_BUFFERS = _MFT_INPUT_STREAM_INFO_FLAGS.MFT_INPUT_STREAM_HOLDS_BUFFERS
        MFT_INPUT_STREAM_DOES_NOT_ADDREF = _MFT_INPUT_STREAM_INFO_FLAGS.MFT_INPUT_STREAM_DOES_NOT_ADDREF
        MFT_INPUT_STREAM_REMOVABLE = _MFT_INPUT_STREAM_INFO_FLAGS.MFT_INPUT_STREAM_REMOVABLE
        MFT_INPUT_STREAM_OPTIONAL = _MFT_INPUT_STREAM_INFO_FLAGS.MFT_INPUT_STREAM_OPTIONAL
        MFT_INPUT_STREAM_PROCESSES_IN_PLACE = _MFT_INPUT_STREAM_INFO_FLAGS.MFT_INPUT_STREAM_PROCESSES_IN_PLACE


        class _MFT_OUTPUT_STREAM_INFO_FLAGS(ENUM):
            MFT_OUTPUT_STREAM_WHOLE_SAMPLES = 0x1
            MFT_OUTPUT_STREAM_SINGLE_SAMPLE_PER_BUFFER = 0x2
            MFT_OUTPUT_STREAM_FIXED_SAMPLE_SIZE = 0x4
            MFT_OUTPUT_STREAM_DISCARDABLE = 0x8
            MFT_OUTPUT_STREAM_OPTIONAL = 0x10
            MFT_OUTPUT_STREAM_PROVIDES_SAMPLES = 0x100
            MFT_OUTPUT_STREAM_CAN_PROVIDE_SAMPLES = 0x200
            MFT_OUTPUT_STREAM_LAZY_READ = 0x400
            MFT_OUTPUT_STREAM_REMOVABLE = 0x800

        MFT_OUTPUT_STREAM_WHOLE_SAMPLES = _MFT_OUTPUT_STREAM_INFO_FLAGS.MFT_OUTPUT_STREAM_WHOLE_SAMPLES
        MFT_OUTPUT_STREAM_SINGLE_SAMPLE_PER_BUFFER = _MFT_OUTPUT_STREAM_INFO_FLAGS.MFT_OUTPUT_STREAM_SINGLE_SAMPLE_PER_BUFFER
        MFT_OUTPUT_STREAM_FIXED_SAMPLE_SIZE = _MFT_OUTPUT_STREAM_INFO_FLAGS.MFT_OUTPUT_STREAM_FIXED_SAMPLE_SIZE
        MFT_OUTPUT_STREAM_DISCARDABLE = _MFT_OUTPUT_STREAM_INFO_FLAGS.MFT_OUTPUT_STREAM_DISCARDABLE
        MFT_OUTPUT_STREAM_OPTIONAL = _MFT_OUTPUT_STREAM_INFO_FLAGS.MFT_OUTPUT_STREAM_OPTIONAL
        MFT_OUTPUT_STREAM_PROVIDES_SAMPLES = _MFT_OUTPUT_STREAM_INFO_FLAGS.MFT_OUTPUT_STREAM_PROVIDES_SAMPLES
        MFT_OUTPUT_STREAM_CAN_PROVIDE_SAMPLES = _MFT_OUTPUT_STREAM_INFO_FLAGS.MFT_OUTPUT_STREAM_CAN_PROVIDE_SAMPLES
        MFT_OUTPUT_STREAM_LAZY_READ = _MFT_OUTPUT_STREAM_INFO_FLAGS.MFT_OUTPUT_STREAM_LAZY_READ
        MFT_OUTPUT_STREAM_REMOVABLE = _MFT_OUTPUT_STREAM_INFO_FLAGS.MFT_OUTPUT_STREAM_REMOVABLE


        class _MFT_SET_TYPE_FLAGS(ENUM):
            MFT_SET_TYPE_TEST_ONLY = 0x1

        MFT_SET_TYPE_TEST_ONLY = _MFT_SET_TYPE_FLAGS.MFT_SET_TYPE_TEST_ONLY


        class _MFT_PROCESS_OUTPUT_FLAGS(ENUM):
            MFT_PROCESS_OUTPUT_DISCARD_WHEN_NO_BUFFER = 0x1
            MFT_PROCESS_OUTPUT_REGENERATE_LAST_OUTPUT = 0x2

        MFT_PROCESS_OUTPUT_DISCARD_WHEN_NO_BUFFER = _MFT_PROCESS_OUTPUT_FLAGS.MFT_PROCESS_OUTPUT_DISCARD_WHEN_NO_BUFFER
        MFT_PROCESS_OUTPUT_REGENERATE_LAST_OUTPUT = _MFT_PROCESS_OUTPUT_FLAGS.MFT_PROCESS_OUTPUT_REGENERATE_LAST_OUTPUT


        class _MFT_PROCESS_OUTPUT_STATUS(ENUM):
            MFT_PROCESS_OUTPUT_STATUS_NEW_STREAMS = 0x100

        MFT_PROCESS_OUTPUT_STATUS_NEW_STREAMS = _MFT_PROCESS_OUTPUT_STATUS.MFT_PROCESS_OUTPUT_STATUS_NEW_STREAMS


        class _MFT_DRAIN_TYPE(ENUM):
            MFT_DRAIN_PRODUCE_TAILS = 0
            MFT_DRAIN_NO_TAILS = 0x1

        MFT_DRAIN_PRODUCE_TAILS = _MFT_DRAIN_TYPE.MFT_DRAIN_PRODUCE_TAILS
        MFT_DRAIN_NO_TAILS = _MFT_DRAIN_TYPE.MFT_DRAIN_NO_TAILS


        class _MFT_MESSAGE_TYPE(ENUM):
            MFT_MESSAGE_COMMAND_FLUSH = 0
            MFT_MESSAGE_COMMAND_DRAIN = 0x1
            MFT_MESSAGE_SET_D3D_MANAGER = 0x2
            MFT_MESSAGE_DROP_SAMPLES = 0x3
            MFT_MESSAGE_COMMAND_TICK = 0x4
            MFT_MESSAGE_NOTIFY_BEGIN_STREAMING = 0x10000000
            MFT_MESSAGE_NOTIFY_END_STREAMING = 0x10000001
            MFT_MESSAGE_NOTIFY_END_OF_STREAM = 0x10000002
            MFT_MESSAGE_NOTIFY_START_OF_STREAM = 0x10000003
            MFT_MESSAGE_NOTIFY_RELEASE_RESOURCES = 0x10000004
            MFT_MESSAGE_NOTIFY_REACQUIRE_RESOURCES = 0x10000005
            MFT_MESSAGE_NOTIFY_EVENT = 0x10000006
            MFT_MESSAGE_COMMAND_SET_OUTPUT_STREAM_STATE = 0x10000007
            MFT_MESSAGE_COMMAND_FLUSH_OUTPUT_STREAM = 0x10000008
            MFT_MESSAGE_COMMAND_MARKER = 0x20000000

        MFT_MESSAGE_TYPE = _MFT_MESSAGE_TYPE

        _MFT_INPUT_STREAM_INFO._fields_ = [
            ('hnsMaxLatency', LONGLONG),
            ('dwFlags', DWORD),
            ('cbSize', DWORD),
            ('cbMaxLookahead', DWORD),
            ('cbAlignment', DWORD),
        ]

        _MFT_OUTPUT_STREAM_INFO._fields_ = [
            ('dwFlags', DWORD),
            ('cbSize', DWORD),
            ('cbAlignment', DWORD),
        ]

        _MFT_OUTPUT_DATA_BUFFER._fields_ = [
            ('dwStreamID', DWORD),
            ('pSample', POINTER(IMFSample)),
            ('dwStatus', DWORD),
            ('pEvents', POINTER(IMFCollection)),
        ]
        PMFT_OUTPUT_DATA_BUFFER = POINTER(_MFT_OUTPUT_DATA_BUFFER)

        # redefine all the method names to have MFT at the beginning so they
        # don't class with DMO methods.
        if defined(MFT_UNIQUE_METHOD_NAMES):
            pass
        # END IF

        if not defined(__IMFTransform_INTERFACE_DEFINED__):
            # interface IMFTransform
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFTransform = MIDL_INTERFACE(
                    "{BF94C121-5B05-4E6F-8000-BA598961414D}"
                )
                IMFTransform._iid_ = IID_IMFTransform

                IMFTransform._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetStreamLimits')],
                        HRESULT,
                        'GetStreamLimits',
                        (['out'], POINTER(DWORD), 'pdwInputMinimum'),
                        (['out'], POINTER(DWORD), 'pdwInputMaximum'),
                        (['out'], POINTER(DWORD), 'pdwOutputMinimum'),
                        (['out'], POINTER(DWORD), 'pdwOutputMaximum'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamCount')],
                        HRESULT,
                        'GetStreamCount',
                        (['out'], POINTER(DWORD), 'pcInputStreams'),
                        (['out'], POINTER(DWORD), 'pcOutputStreams'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamIDs')],
                        HRESULT,
                        'GetStreamIDs',
                        ([], DWORD, 'dwInputIDArraySize'),
                        (['out', 'in'], POINTER(DWORD), 'pdwInputIDs'),
                        ([], DWORD, 'dwOutputIDArraySize'),
                        (['out'], POINTER(DWORD), 'pdwOutputIDs'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputStreamInfo')],
                        HRESULT,
                        'GetInputStreamInfo',
                        ([], DWORD, 'dwInputStreamID'),
                        (
                            ['out'],
                            POINTER(MFT_INPUT_STREAM_INFO),
                            'pStreamInfo'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputStreamInfo')],
                        HRESULT,
                        'GetOutputStreamInfo',
                        ([], DWORD, 'dwOutputStreamID'),
                        (
                            ['out'],
                            POINTER(MFT_OUTPUT_STREAM_INFO),
                            'pStreamInfo'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAttributes')],
                        HRESULT,
                        'GetAttributes',
                        (
                            ['out'],
                            POINTER(POINTER(IMFAttributes)),
                            'pAttributes'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputStreamAttributes')],
                        HRESULT,
                        'GetInputStreamAttributes',
                        ([], DWORD, 'dwInputStreamID'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFAttributes)),
                            'pAttributes'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputStreamAttributes')],
                        HRESULT,
                        'GetOutputStreamAttributes',
                        ([], DWORD, 'dwOutputStreamID'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFAttributes)),
                            'pAttributes'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method DeleteInputStream')],
                        HRESULT,
                        'DeleteInputStream',
                        ([], DWORD, 'dwStreamID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddInputStreams')],
                        HRESULT,
                        'AddInputStreams',
                        ([], DWORD, 'cStreams'),
                        (['in'], POINTER(DWORD), 'adwStreamIDs'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputAvailableType')],
                        HRESULT,
                        'GetInputAvailableType',
                        ([], DWORD, 'dwInputStreamID'),
                        ([], DWORD, 'dwTypeIndex'),
                        (['out'], POINTER(POINTER(IMFMediaType)), 'ppType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputAvailableType')],
                        HRESULT,
                        'GetOutputAvailableType',
                        ([], DWORD, 'dwOutputStreamID'),
                        ([], DWORD, 'dwTypeIndex'),
                        (['out'], POINTER(POINTER(IMFMediaType)), 'ppType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetInputType')],
                        HRESULT,
                        'SetInputType',
                        ([], DWORD, 'dwInputStreamID'),
                        (['in'], POINTER(IMFMediaType), 'pType'),
                        ([], DWORD, 'dwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetOutputType')],
                        HRESULT,
                        'SetOutputType',
                        ([], DWORD, 'dwOutputStreamID'),
                        (['in'], POINTER(IMFMediaType), 'pType'),
                        ([], DWORD, 'dwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputCurrentType')],
                        HRESULT,
                        'GetInputCurrentType',
                        ([], DWORD, 'dwInputStreamID'),
                        (['out'], POINTER(POINTER(IMFMediaType)), 'ppType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputCurrentType')],
                        HRESULT,
                        'GetOutputCurrentType',
                        ([], DWORD, 'dwOutputStreamID'),
                        (['out'], POINTER(POINTER(IMFMediaType)), 'ppType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputStatus')],
                        HRESULT,
                        'GetInputStatus',
                        ([], DWORD, 'dwInputStreamID'),
                        (['out'], POINTER(DWORD), 'pdwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputStatus')],
                        HRESULT,
                        'GetOutputStatus',
                        (['out'], POINTER(DWORD), 'pdwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetOutputBounds')],
                        HRESULT,
                        'SetOutputBounds',
                        ([], LONGLONG, 'hnsLowerBound'),
                        ([], LONGLONG, 'hnsUpperBound'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ProcessEvent')],
                        HRESULT,
                        'ProcessEvent',
                        ([], DWORD, 'dwInputStreamID'),
                        (['in'], POINTER(IMFMediaEvent), 'pEvent'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ProcessMessage')],
                        HRESULT,
                        'ProcessMessage',
                        ([], MFT_MESSAGE_TYPE, 'eMessage'),
                        ([], ULONG_PTR, 'ulParam'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ProcessInput'), 'local'],
                        HRESULT,
                        'ProcessInput',
                        ([], DWORD, 'dwInputStreamID'),
                        ([], POINTER(IMFSample), 'pSample'),
                        ([], DWORD, 'dwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ProcessOutput'), 'local'],
                        HRESULT,
                        'ProcessOutput',
                        ([], DWORD, 'dwFlags'),
                        ([], DWORD, 'cOutputBufferCount'),
                        (
                            ['out', 'in'],
                            POINTER(MFT_OUTPUT_DATA_BUFFER),
                            'pOutputSamples'
                        ),
                        (['out'], POINTER(DWORD), 'pdwStatus'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFTransform_INTERFACE_DEFINED__

        # interface __MIDL_itf_mftransform_0000_0001
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    class _DeviceStreamState(ENUM):
        DeviceStreamState_Stop = 0
        DeviceStreamState_Pause = DeviceStreamState_Stop + 1
        DeviceStreamState_Run = DeviceStreamState_Pause + 1
        DeviceStreamState_Disabled = DeviceStreamState_Run + 1

    DeviceStreamState = _DeviceStreamState
    PDeviceStreamState = POINTER(_DeviceStreamState)

    MEDeviceStreamCreated = EXTERN_GUID(
        0x0252A1CF,
        0x3540,
        0x43B4,
        0x91,
        0x64,
        0xD7,
        0x2E,
        0xB4,
        0x05,
        0xFA,
        0x40
    )
    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            _STREAM_MEDIUM._fields_ = [
                ('gidMedium', GUID),
                ('unMediumInstance', UINT32),
            ]
            PSTREAM_MEDIUM = POINTER(_STREAM_MEDIUM)

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # Define the MFT methods back so we don't accidentally hose the
        # IMediaObject interface.
        if defined(MFT_UNIQUE_METHOD_NAMES):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
        if not defined(__IMFDeviceTransform_INTERFACE_DEFINED__):
            # interface IMFDeviceTransform
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFDeviceTransform = MIDL_INTERFACE(
                    "{D818FBD8-FC46-42F2-87AC-1EA2D1F9BF32}"
                )
                IMFDeviceTransform._iid_ = IID_IMFDeviceTransform

                IMFDeviceTransform._methods_ = [
                    COMMETHOD(
                        [helpstring('Method InitializeTransform')],
                        HRESULT,
                        'InitializeTransform',
                        (['in'], POINTER(IMFAttributes), 'pAttributes'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputAvailableType')],
                        HRESULT,
                        'GetInputAvailableType',
                        (['in'], DWORD, 'dwInputStreamID'),
                        (['in'], DWORD, 'dwTypeIndex'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaType)),
                            'pMediaType'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputCurrentType')],
                        HRESULT,
                        'GetInputCurrentType',
                        (['in'], DWORD, 'dwInputStreamID'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaType)),
                            'pMediaType'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputStreamAttributes')],
                        HRESULT,
                        'GetInputStreamAttributes',
                        (['in'], DWORD, 'dwInputStreamID'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFAttributes)),
                            'ppAttributes'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputAvailableType')],
                        HRESULT,
                        'GetOutputAvailableType',
                        (['in'], DWORD, 'dwOutputStreamID'),
                        (['in'], DWORD, 'dwTypeIndex'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaType)),
                            'pMediaType'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputCurrentType')],
                        HRESULT,
                        'GetOutputCurrentType',
                        (['in'], DWORD, 'dwOutputStreamID'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaType)),
                            'pMediaType'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputStreamAttributes')],
                        HRESULT,
                        'GetOutputStreamAttributes',
                        (['in'], DWORD, 'dwOutputStreamID'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFAttributes)),
                            'ppAttributes'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamCount')],
                        HRESULT,
                        'GetStreamCount',
                        (['out'], POINTER(DWORD), 'pcInputStreams'),
                        (['out'], POINTER(DWORD), 'pcOutputStreams'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamIDs')],
                        HRESULT,
                        'GetStreamIDs',
                        (['in'], DWORD, 'dwInputIDArraySize'),
                        (['out'], POINTER(DWORD), 'pdwInputStreamIds'),
                        (['in'], DWORD, 'dwOutputIDArraySize'),
                        (['out'], POINTER(DWORD), 'pdwOutputStreamIds'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ProcessEvent')],
                        HRESULT,
                        'ProcessEvent',
                        (['in'], DWORD, 'dwInputStreamID'),
                        (['in'], POINTER(IMFMediaEvent), 'pEvent'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ProcessInput')],
                        HRESULT,
                        'ProcessInput',
                        (['in'], DWORD, 'dwInputStreamID'),
                        (['in'], POINTER(IMFSample), 'pSample'),
                        (['in'], DWORD, 'dwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ProcessMessage')],
                        HRESULT,
                        'ProcessMessage',
                        (['in'], MFT_MESSAGE_TYPE, 'eMessage'),
                        (['in'], ULONG_PTR, 'ulParam'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ProcessOutput')],
                        HRESULT,
                        'ProcessOutput',
                        (['in'], DWORD, 'dwFlags'),
                        (['in'], DWORD, 'cOutputBufferCount'),
                        (
                            ['out', 'in'],
                            POINTER(MFT_OUTPUT_DATA_BUFFER),
                            'pOutputSample'
                        ),
                        (['out'], POINTER(DWORD), 'pdwStatus'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetInputStreamState')],
                        HRESULT,
                        'SetInputStreamState',
                        (['in'], DWORD, 'dwStreamID'),
                        (['in'], POINTER(IMFMediaType), 'pMediaType'),
                        (['in'], DeviceStreamState, 'value'),
                        (['in'], DWORD, 'dwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputStreamState')],
                        HRESULT,
                        'GetInputStreamState',
                        (['in'], DWORD, 'dwStreamID'),
                        (['out'], POINTER(DeviceStreamState), 'value'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetOutputStreamState')],
                        HRESULT,
                        'SetOutputStreamState',
                        (['in'], DWORD, 'dwStreamID'),
                        (['in'], POINTER(IMFMediaType), 'pMediaType'),
                        (['in'], DeviceStreamState, 'value'),
                        (['in'], DWORD, 'dwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputStreamState')],
                        HRESULT,
                        'GetOutputStreamState',
                        (['in'], DWORD, 'dwStreamID'),
                        (['out'], POINTER(DeviceStreamState), 'value'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputStreamPreferredState')],
                        HRESULT,
                        'GetInputStreamPreferredState',
                        (['in'], DWORD, 'dwStreamID'),
                        (['out'], POINTER(DeviceStreamState), 'value'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaType)),
                            'ppMediaType'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method FlushInputStream')],
                        HRESULT,
                        'FlushInputStream',
                        (['in'], DWORD, 'dwStreamIndex'),
                        (['in'], DWORD, 'dwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FlushOutputStream')],
                        HRESULT,
                        'FlushOutputStream',
                        (['in'], DWORD, 'dwStreamIndex'),
                        (['in'], DWORD, 'dwFlags'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFDeviceTransform_INTERFACE_DEFINED__

        # interface __MIDL_itf_mftransform_0000_0002
        # [local]
    # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD )

    if WINVER >= _WIN32_WINNT_WIN10:
        MF_DMFT_FRAME_BUFFER_INFO = EXTERN_GUID(
            0x396CE1C9,
            0x67A9,
            0x454C,
            0x87,
            0x97,
            0x95,
            0xA4,
            0x57,
            0x99,
            0xD8,
            0x04
        )
        if not defined(__IMFDeviceTransformCallback_INTERFACE_DEFINED__):
            # interface IMFDeviceTransformCallback
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFDeviceTransformCallback = MIDL_INTERFACE(
                    "{6D5CB646-29EC-41FB-8179-8C4C6D750811}"
                )
                IMFDeviceTransformCallback._iid_ = IID_IMFDeviceTransformCallback

                IMFDeviceTransformCallback._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnBufferSent')],
                        HRESULT,
                        'OnBufferSent',
                        (
                            ['in'],
                            POINTER(IMFAttributes),
                            'pCallbackAttributes'
                        ),
                        (['in'], DWORD, 'pinId'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFDeviceTransformCallback_INTERFACE_DEFINED__

        # interface __MIDL_itf_mftransform_0000_0003
        # [local]
    # END IF   (WINVER >= _WIN32_WINNT_WIN10 )

    if WINVER >= _WIN32_WINNT_WIN8:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            class _MF3DVideoOutputType(ENUM):
                MF3DVideoOutputType_BaseView = 0
                MF3DVideoOutputType_Stereo = 1

            MF3DVideoOutputType = _MF3DVideoOutputType
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN8)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            mfplat = ctypes.windll.MFPLAT

            # STDAPI
            # MFCreateTransformActivate(
            # _Out_ IMFActivate** ppActivate
            # );
            MFCreateTransformActivate = mfplat.MFCreateTransformActivate

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

    if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
        MFT_AUDIO_DECODER_DEGRADATION_INFO_ATTRIBUTE = EXTERN_GUID(
            0x6C3386AD,
            0xEC20,
            0x430D,
            0xB2,
            0xA5,
            0x50,
            0x5C,
            0x71,
            0x78,
            0xD9,
            0xC4
        )


        class MFT_AUDIO_DECODER_DEGRADATION_REASON(ENUM):
            MFT_AUDIO_DECODER_DEGRADATION_REASON_NONE = 0
            MFT_AUDIO_DECODER_DEGRADATION_REASON_LICENSING_REQUIREMENT = 1


        class MFT_AUDIO_DECODER_DEGRADATION_TYPE(ENUM):
            MFT_AUDIO_DECODER_DEGRADATION_TYPE_NONE = 0
            MFT_AUDIO_DECODER_DEGRADATION_TYPE_DOWNMIX2CHANNEL = 1
            MFT_AUDIO_DECODER_DEGRADATION_TYPE_DOWNMIX6CHANNEL = 2
            MFT_AUDIO_DECODER_DEGRADATION_TYPE_DOWNMIX8CHANNEL = 3

        MFAudioDecoderDegradationInfo._fields_ = [
            ('eDegradationReason', MFT_AUDIO_DECODER_DEGRADATION_REASON),
            ('eType', MFT_AUDIO_DECODER_DEGRADATION_TYPE),
        ]

        _MFT_STREAM_STATE_PARAM._fields_ = [
            ('StreamId', DWORD),
            ('State', MF_STREAM_STATE),
        ]
        PMFT_STREAM_STATE_PARAM = POINTER(_MFT_STREAM_STATE_PARAM)

    # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


