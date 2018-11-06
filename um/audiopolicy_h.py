__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
# from oaidl_h import * # NOQA
# from ocidl_h import * # NOQA
# from propidl_h import * # NOQA
from .audiosessiontypes_h import * # NOQA
from .audioclient_h import * # NOQA
from .winapifamily_h import * # NOQA

from .wtypes_h import (
    ENUM,
    POINTER,
    HRESULT,
    LPCWSTR,
    UINT32,
    LPWSTR,
    LPCGUID,
    GUID,
    DWORD,
    BOOL,
    INT,
    FLOAT,
    VOID
)
from .guiddef_h import IID
import comtypes


class AudioSessionDisconnectReason(ENUM):
    DisconnectReasonDeviceRemoval = 0
    DisconnectReasonServerShutdown = DisconnectReasonDeviceRemoval + 1
    DisconnectReasonFormatChanged = DisconnectReasonServerShutdown + 1
    DisconnectReasonSessionLogoff = DisconnectReasonFormatChanged + 1
    DisconnectReasonSessionDisconnected = DisconnectReasonSessionLogoff + 1
    DisconnectReasonExclusiveModeOverride = (
        DisconnectReasonSessionDisconnected + 1
    )


COMMETHOD = comtypes.COMMETHOD

IID_IAudioSessionEvents = IID(
    '{24918ACC-64B3-37C1-8CA9-74A66E9957A8}'
)


class IAudioSessionEvents(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioSessionEvents
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'OnDisplayNameChanged',
            (['in'], LPCWSTR, 'NewDisplayName'),
            (['in'], LPCGUID, 'EventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'OnIconPathChanged',
            (['in'], LPCWSTR, 'NewIconPath'),
            (['in'], LPCGUID, 'EventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'OnSimpleVolumeChanged',
            (['in'], FLOAT, 'NewVolume'),
            (['in'], BOOL, 'NewMute'),
            (['in'], LPCGUID, 'EventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'OnChannelVolumeChanged',
            (['in'], DWORD, 'ChannelCount'),
            (['in'], FLOAT * 8, 'NewChannelVolumeArray'),
            (['in'], DWORD, 'ChangedChannel'),
            (['in'], LPCGUID, 'EventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'OnGroupingParamChanged',
            (['in'], LPCGUID, 'NewGroupingParam'),
            (['in'], LPCGUID, 'EventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'OnStateChanged',
            (['in'], AudioSessionState, 'NewState'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'OnSessionDisconnected',
            (['in'], AudioSessionDisconnectReason, 'DisconnectReason'),
        ),
    ]


IID_IAudioSessionControl = IID(
    '{F4B1A599-7266-4319-A8CA-E70ACB11E8CD}'
)


class IAudioSessionControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioSessionControl
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetState',
            (['out'], POINTER(AudioSessionState), 'pRetVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetDisplayName',
            (['out'], POINTER(LPWSTR), 'pRetVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetDisplayName',
            (['in'], LPCWSTR, 'Value'),
            (['in'], LPCGUID, 'EventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetIconPath',
            (['out'], POINTER(LPWSTR), 'pRetVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetIconPath',
            (['in'], LPCWSTR, 'Value'),
            (['in'], LPCGUID, 'EventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetGroupingParam',
            (['out'], POINTER(GUID), 'pRetVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetGroupingParam',
            (['in'], LPCGUID, 'Override'),
            (['in'], LPCGUID, 'EventContext'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'RegisterAudioSessionNotification',
            (['in'], POINTER(IAudioSessionEvents), 'NewNotifications'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'UnregisterAudioSessionNotification',
            (['in'], POINTER(IAudioSessionEvents), 'NewNotifications'),
        ),
    ]


IID_IAudioSessionControl2 = IID(
    '{bfb7ff88-7239-4fc9-8fa2-07c950be9c6d}'
)


class IAudioSessionControl2(IAudioSessionControl):
    _case_insensitive_ = True
    _iid_ = IID_IAudioSessionControl2
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetSessionIdentifier',
            (['out'], POINTER(LPWSTR), 'pRetVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetSessionInstanceIdentifier',
            (['out'], POINTER(LPWSTR), 'pRetVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetProcessId',
            (['out'], POINTER(DWORD), 'pRetVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'IsSystemSoundsSession'
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetDuckingPreference',
            (['in'], BOOL, 'optOut'),
        ),
    ]


IID_IAudioSessionManager = IID(
    '{BFA971F1-4D5E-40BB-935E-967039BFBEE4}'
)


class IAudioSessionManager(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioSessionManager
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetAudioSessionControl',
            (['in'], LPCGUID, 'AudioSessionGuid'),
            (['in'], DWORD, 'StreamFlags'),
            (['out'], POINTER(POINTER(IAudioSessionControl)), 'SessionControl'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetSimpleAudioVolume',
            (['in'], LPCGUID, 'AudioSessionGuid'),
            (['in'], DWORD, 'StreamFlags'),
            (['out'], POINTER(POINTER(ISimpleAudioVolume)), 'AudioVolume'),
        ),
    ]


IID_IAudioVolumeDuckNotification = IID(
    '{C3B284D4-6D39-4359-B3CF-B56DDB3BB39C}'
)


class IAudioVolumeDuckNotification(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioVolumeDuckNotification
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'OnVolumeDuckNotification',
            (['in'], LPCWSTR, 'sessionID'),
            (['in'], UINT32, 'countCommunicationSessions'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'OnVolumeUnduckNotification',
            (['in'], LPCWSTR, 'sessionID'),
        ),
    ]


IID_IAudioSessionNotification = IID(
    '{641DD20B-4D41-49CC-ABA3-174B9477BB08}'
)


class IAudioSessionNotification(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioSessionNotification
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'OnSessionCreated',
            (['in'], POINTER(IAudioSessionControl), 'NewSession'),
        ),
    ]


IID_IAudioSessionEnumerator = IID(
    '{E2F5BB11-0570-40CA-ACDD-3AA01277DEE8}'
)


class IAudioSessionEnumerator(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioSessionEnumerator
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetCount',
            (['out'], POINTER(INT), 'SessionCount'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetSession',
            (['in'], INT, 'SessionCount'),
            (['out'], POINTER(POINTER(IAudioSessionControl)), 'Session'),
        ),
    ]


IID_IAudioSessionManager2 = IID(
    '{77AA99A0-1BD6-484F-8BC7-2C654C9A9B6F}'
)


class IAudioSessionManager2(IAudioSessionManager):
    _case_insensitive_ = True
    _iid_ = IID_IAudioSessionManager2
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetSessionEnumerator',
            (['out', 'retval'], POINTER(POINTER(IAudioSessionEnumerator)), 'SessionEnum'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'RegisterSessionNotification',
            ([], POINTER(IAudioSessionNotification), 'SessionNotification'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'UnregisterSessionNotification',
            ([], POINTER(IAudioSessionNotification), 'SessionNotification'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'RegisterDuckNotification',
            (['in'], LPCWSTR, 'sessionID'),
            (['in'], POINTER(IAudioVolumeDuckNotification), 'duckNotification'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'UnregisterDuckNotification',
            (['in'], POINTER(IAudioVolumeDuckNotification), 'duckNotification'),
        ),
    ]


_all_ = (
    'AudioSessionDisconnectReason', 'IID_IAudioSessionEvents',
    'IAudioSessionEvents', 'IID_IAudioSessionControl', 'IAudioSessionControl',
    'IID_IAudioSessionControl2', 'IAudioSessionControl2',
    'IID_IAudioSessionManager', 'IAudioSessionManager',
    'IID_IAudioVolumeDuckNotification', 'IAudioVolumeDuckNotification',
    'IID_IAudioSessionNotification', 'IAudioSessionNotification',
    'IID_IAudioSessionEnumerator', 'IAudioSessionEnumerator',
    'IID_IAudioSessionManager2', 'IAudioSessionManager2',
)
