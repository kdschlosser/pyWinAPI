from .winapifamily_h import * # NOQA

from .wtypes_h import ENUM


class _AUDCLNT_SHAREMODE(ENUM):
    AUDCLNT_SHAREMODE_SHARED = 0
    AUDCLNT_SHAREMODE_EXCLUSIVE = 1


AUDCLNT_SHAREMODE = _AUDCLNT_SHAREMODE

# -------------------------------------------------------------------------
# Description: Audio stream categories

# ForegroundOnlyMedia     - (deprecated for Win10) Music, Streaming audio
# BackgroundCapableMedia  - (deprecated for Win10) Video with audio
# Communications          - VOIP, chat, phone call
# Alerts                  - Alarm, Ring tones
# SoundEffects            - Sound effects, clicks, dings
# GameEffects             - Game sound effects
# GameMedia               - Background audio for games
# GameChat                - In game player chat
# Speech                  - Speech recognition
# Media                   - Music, Streaming audio
# Movie                   - Video with audio
# Other                   - All other streams (default)

class _AUDIO_STREAM_CATEGORY(ENUM):
    AudioCategory_Other = 0
    AudioCategory_ForegroundOnlyMedia = 1
    AudioCategory_BackgroundCapableMedia = 2
    AudioCategory_Communications = 3
    AudioCategory_Alerts = 4
    AudioCategory_SoundEffects = 5
    AudioCategory_GameEffects = 6
    AudioCategory_GameMedia = 7
    AudioCategory_GameChat = 8
    AudioCategory_Speech = 9
    AudioCategory_Movie = 10
    AudioCategory_Media = 11


AUDIO_STREAM_CATEGORY = _AUDIO_STREAM_CATEGORY


# -------------------------------------------------------------------------
# Description: AudioClient stream flags

# Can be a combination of AUDCLNT_STREAMFLAGS and AUDCLNT_SYSFXFLAGS:

# AUDCLNT_STREAMFLAGS (this group of flags uses the high word,
# w/exception of high-bit which is reserved, 0x7FFF0000):


# AUDCLNT_STREAMFLAGS_CROSSPROCESS -             Audio policy control for this
# stream will be shared with
# with other process sessions that use the same audio session
# GUID.

# AUDCLNT_STREAMFLAGS_LOOPBACK -                 Initializes a renderer
# endpoINT for a loopback audio application.
# In this mode, a capture stream will be opened on the specified
# renderer endpoINT. Shared mode and a renderer endpoINT is required.
# Otherwise the IAudioClient::Initialize call will fail. If the
# initialize is successful, a capture stream will be available
# from the IAudioClient object.

# AUDCLNT_STREAMFLAGS_EVENTCALLBACK -            An exclusive mode client will
# supply an event handle that will be
# signaled when an IRP completes (or a waveRT buffer completes) telling
# it to fill the next buffer

# AUDCLNT_STREAMFLAGS_NOPERSIST -                Session state will not be
# persisted

# AUDCLNT_STREAMFLAGS_RATEADJUST -               The sample rate of the stream
# is adjusted to a rate specified by an application.

# AUDCLNT_STREAMFLAGS_SRC_DEFAULT_QUALITY -      When used with
# AUDCLNT_STREAMFLAGS_AUTOCONVERTPCM, a sample rate
# converter with better quality than the default conversion but with a
# higher performance cost is used. This should be used if the audio is
# ultimately INTended to be heard by humans as opposed to other
# scenarios such as pumping silence or populating a meter.

# AUDCLNT_STREAMFLAGS_AUTOCONVERTPCM -           A channel matrixer and a
# sample rate converter are inserted as necessary
# to convert between the uncompressed format supplied to
# IAudioClient::Initialize and the audio engine mix format.

# AUDCLNT_STREAMFLAGS_PREVENT_LOOPBACK_CAPTURE - MSFT: 14779533  -  This flag
# is delayed until RS5 when it can be better scoped
# Prevents the stream from being included in any loopback streams. Note that
# this stream will continue to be included in the endpoINT loopback stream

# AUDCLNT_SESSIONFLAGS_EXPIREWHENUNOWNED -       Session expires when there
# are no streams and no owning
# session controls.

# AUDCLNT_SESSIONFLAGS_DISPLAY_HIDE -            Don't show volume control in
# the Volume Mixer.

# AUDCLNT_SESSIONFLAGS_DISPLAY_HIDEWHENEXPIRED - Don't show volume control in
# the Volume Mixer after the
# session expires.

# AUDCLNT_SYSFXFLAGS (these flags use low word 0x0000FFFF):

# none defined currently

AUDCLNT_STREAMFLAGS_CROSSPROCESS = 0x00010000
AUDCLNT_STREAMFLAGS_LOOPBACK = 0x00020000
AUDCLNT_STREAMFLAGS_EVENTCALLBACK = 0x00040000
AUDCLNT_STREAMFLAGS_NOPERSIST = 0x00080000
AUDCLNT_STREAMFLAGS_RATEADJUST = 0x00100000
AUDCLNT_STREAMFLAGS_PREVENT_LOOPBACK_CAPTURE = 0x01000000
AUDCLNT_STREAMFLAGS_SRC_DEFAULT_QUALITY = 0x08000000
AUDCLNT_STREAMFLAGS_AUTOCONVERTPCM = 0x80000000
AUDCLNT_SESSIONFLAGS_EXPIREWHENUNOWNED = 0x10000000
AUDCLNT_SESSIONFLAGS_DISPLAY_HIDE = 0x20000000
# -------------------------------------------------------------------------
AUDCLNT_SESSIONFLAGS_DISPLAY_HIDEWHENEXPIRED = 0x40000000
# Description: AudioSession State.

# AudioSessionStateInactive - The session has no active audio streams.
# AudioSessionStateActive - The session has active audio streams.
# AudioSessionStateExpired - The session is dormant.

class _AudioSessionState(ENUM):
    AudioSessionStateInactive = 0
    AudioSessionStateActive = 1
    AudioSessionStateExpired = 2


AudioSessionState = _AudioSessionState


__all__ = (
    'AUDCLNT_STREAMFLAGS_CROSSPROCESS', 'AUDCLNT_STREAMFLAGS_LOOPBACK',
    'AUDCLNT_STREAMFLAGS_EVENTCALLBACK', 'AUDCLNT_STREAMFLAGS_NOPERSIST',
    'AUDCLNT_STREAMFLAGS_RATEADJUST', '_AudioSessionState',
    'AUDCLNT_STREAMFLAGS_PREVENT_LOOPBACK_CAPTURE', 'AUDCLNT_SHAREMODE',
    'AUDCLNT_STREAMFLAGS_SRC_DEFAULT_QUALITY',
    'AUDCLNT_STREAMFLAGS_AUTOCONVERTPCM', '_AUDIO_STREAM_CATEGORY',
    'AUDCLNT_SESSIONFLAGS_EXPIREWHENUNOWNED', 'AUDIO_STREAM_CATEGORY',
    'AUDCLNT_SESSIONFLAGS_DISPLAY_HIDE', 'AudioSessionState',
    'AUDCLNT_SESSIONFLAGS_DISPLAY_HIDEWHENEXPIRED', '_AUDCLNT_SHAREMODE',
)
