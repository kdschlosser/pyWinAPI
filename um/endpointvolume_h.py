__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
from .unknwn_h import * # NOQA
from .devicetopology_h import * # NOQA
from .winapifamily_h import * # NOQA

from .wtypes_h import (
    FLOAT,
    POINTER,
    HRESULT,
    UINT,
    UINT32,
    DWORD,
    LPCGUID,
    BOOL,
    GUID,
)
from .guiddef_h import IID
import ctypes
import comtypes


class AUDIO_VOLUME_NOTIFICATION_DATA(ctypes.Structure):
    _fields_ = [
        ('guidEventContext', GUID),
        ('bMuted', BOOL),
        ('fMasterVolume', FLOAT),
        ('nChannels', UINT),
        ('afChannelVolumes', FLOAT * 8),
    ]


PAUDIO_VOLUME_NOTIFICATION_DATA = POINTER(AUDIO_VOLUME_NOTIFICATION_DATA)
ENDPOINT_HARDWARE_SUPPORT_VOLUME = 0x00000001
ENDPOINT_HARDWARE_SUPPORT_MUTE = 0x00000002
ENDPOINT_HARDWARE_SUPPORT_METER = 0x00000004

COMMETHOD = comtypes.COMMETHOD


IID_IAudioEndpointVolumeCallback = IID(
    '{657804FA-D6AD-4496-8A60-352752AF4F89}'
)


class IAudioEndpointVolumeCallback(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpointVolumeCallback
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'OnNotify',
            (['in'], PAUDIO_VOLUME_NOTIFICATION_DATA, 'pNotify'),
        ),
    ]


IID_IAudioEndpointVolume = IID(
    '{5CDF2C82-841E-4546-9722-0CF74078229A}'
)


class IAudioEndpointVolume(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpointVolume
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'RegisterControlChangeNotify',
            ([], POINTER(IAudioEndpointVolumeCallback), 'pNotify'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'UnregisterControlChangeNotify',
            ([], POINTER(IAudioEndpointVolumeCallback), 'pNotify'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetChannelCount',
            (['out'], POINTER(UINT), 'pnChannelCount'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetMasterVolumeLevel',
            (['in'], FLOAT, 'fLevelDB'),
            (['in'], LPCGUID, 'pguidEventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetMasterVolumeLevelScalar',
            (['in'], FLOAT, 'fLevel'),
            (['in'], LPCGUID, 'pguidEventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMasterVolumeLevel',
            (['out'], POINTER(FLOAT), 'pfLevelDB'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMasterVolumeLevelScalar',
            (['out'], POINTER(FLOAT), 'pfLevel'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetChannelVolumeLevel',
            (['in'], UINT, 'nChannel'),
            (['in'], FLOAT, 'fLevelDB'),
            (['in'], LPCGUID, 'pguidEventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetChannelVolumeLevelScalar',
            (['in'], UINT, 'nChannel'),
            (['in'], FLOAT, 'fLevel'),
            (['in'], LPCGUID, 'pguidEventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetChannelVolumeLevel',
            (['in'], UINT, 'nChannel'),
            (['out'], POINTER(FLOAT), 'pfLevelDB'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetChannelVolumeLevelScalar',
            (['in'], UINT, 'nChannel'),
            (['out'], POINTER(FLOAT), 'pfLevel'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetMute',
            (['in'], BOOL, 'bMute'),
            (['in'], LPCGUID, 'pguidEventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMute',
            (['out'], POINTER(BOOL), 'pbMute'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetVolumeStepInfo',
            (['out'], POINTER(UINT), 'pnStep'),
            (['out'], POINTER(UINT), 'pnStepCount'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'VolumeStepUp',
            (['in'], LPCGUID, 'pguidEventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'VolumeStepDown',
            (['in'], LPCGUID, 'pguidEventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'QueryHardwareSupport',
            (['out'], POINTER(DWORD), 'pdwHardwareSupportMask'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetVolumeRange',
            (['out'], POINTER(FLOAT), 'pflVolumeMindB'),
            (['out'], POINTER(FLOAT), 'pflVolumeMaxdB'),
            (['out'], POINTER(FLOAT), 'pflVolumeIncrementdB'),
        ),
    ]


IID_IAudioEndpointVolumeEx = IID(
    '{66E11784-F695-4F28-A505-A7080081A78F}'
)


class IAudioEndpointVolumeEx(IAudioEndpointVolume):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpointVolumeEx
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetVolumeRangeChannel',
            (['in'], UINT, 'iChannel'),
            (['out'], POINTER(FLOAT), 'pflVolumeMindB'),
            (['out'], POINTER(FLOAT), 'pflVolumeMaxdB'),
            (['out'], POINTER(FLOAT), 'pflVolumeIncrementdB'),
        ),
    ]


IID_IAudioMeterInformation = IID(
    '{C02216F6-8C67-4B5B-9D00-D008E73E0064}'
)


class IAudioMeterInformation(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioMeterInformation
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetPeakValue',
            (['out'], POINTER(FLOAT), 'pfPeak'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMeteringChannelCount',
            (['out'], POINTER(UINT), 'pnChannelCount'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetChannelsPeakValues',
            (['in'], UINT32, 'u32ChannelCount'),
            (['out'], FLOAT * 8, 'afPeakValues'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'QueryHardwareSupport',
            (['out'], POINTER(DWORD), 'pdwHardwareSupportMask'),
        ),
    ]


__all__ = (
    'IAudioMeterInformation','IAudioEndpointVolume',
    'ENDPOINT_HARDWARE_SUPPORT_MUTE','IAudioEndpointVolumeEx',
    'ENDPOINT_HARDWARE_SUPPORT_METER','__REQUIRED_RPCNDR_H_VERSION__',
    'ENDPOINT_HARDWARE_SUPPORT_VOLUME','AUDIO_VOLUME_NOTIFICATION_DATA',
    'IAudioEndpointVolumeCallback','__REQUIRED_RPCSAL_H_VERSION__',
)
