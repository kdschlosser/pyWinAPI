# from apiset_h import * # NOQA
# from apisetcconv_h import * # NOQA
from .mmsyscom_h import * # NOQA
from .wtypes_h import (
    WORD,
    WCHAR,
    DWORD,
    GUID,
    POINTER,
    CHAR,
    LONG,
    HWND,
    LPVOID,
    LPSTR,
    DWORD_PTR,
    FAR,
    UINT,
    HANDLE
)
import ctypes


winmm = ctypes.windll.Winmm
# *******************************************************************************
# *
#    *
# * mmeapi.h -- ApiSet Contract for api-ms-win-mm-mme-l1-1-0
#    *
# *
#    *
# * Copyright (c) Microsoft Corporation. All rights reserved.
#    *
# *
#    *
# *******************************************************************************
# _MSC_VER

# ***************************************************************************
# Waveform audio support
# ***************************************************************************
# waveform audio error return values
# unsupported wave format
# still something playing
WAVERR_BADFORMAT = WAVERR_BASE + 0
# header not prepared
WAVERR_STILLPLAYING = WAVERR_BASE + 1
# device is synchronous
WAVERR_UNPREPARED = WAVERR_BASE + 2
# last error in range
WAVERR_SYNC = WAVERR_BASE + 3
WAVERR_LASTERROR = WAVERR_BASE + 3
# waveform audio data types
HWAVE = HANDLE
HWAVEIN = HANDLE
HWAVEOUT = HANDLE

LPHWAVEIN = POINTER(HWAVEIN)
LPHWAVEOUT = POINTER(HWAVEOUT)
WAVECALLBACK = DRVCALLBACK
LPWAVECALLBACK = POINTER(WAVECALLBACK)
# wave callback messages
WOM_OPEN = MM_WOM_OPEN
WOM_CLOSE = MM_WOM_CLOSE
WOM_DONE = MM_WOM_DONE
WIM_OPEN = MM_WIM_OPEN
WIM_CLOSE = MM_WIM_CLOSE
# WIM_DATA = MM_WIM_DATA
# device ID for wave device mapper
WAVE_MAPPER = -1
# flags for dwFlags parameter in waveOutOpen() and waveInOpen()
WAVE_FORMAT_QUERY = 0x0001
WAVE_ALLOWSYNC = 0x0002
WAVE_MAPPED = 0x0004
WAVE_FORMAT_DIRECT = 0x0008
WAVE_FORMAT_DIRECT_QUERY = WAVE_FORMAT_QUERY | WAVE_FORMAT_DIRECT
# (WINVER >= 0x0400)
WAVE_MAPPED_DEFAULT_COMMUNICATION_DEVICE = 0x0010
# wave data block header


class wavehdr_tag(ctypes.Structure):
    pass


wavehdr_tag._fields_ = [
    ('lpData', LPSTR),
    ('dwBufferLength', DWORD),
    ('dwBytesRecorded', DWORD),
    ('dwUser', DWORD_PTR),
    ('dwFlags', DWORD),
    ('dwLoops', DWORD),
    ('lpNext', POINTER(wavehdr_tag)),
    ('reserved', DWORD_PTR),
]


WAVEHDR = wavehdr_tag
PWAVEHDR = POINTER(wavehdr_tag)
NPWAVEHDR = POINTER(wavehdr_tag)
LPWAVEHDR = POINTER(wavehdr_tag)


# poINTer to locked data buffer
# length of data buffer
# used for input only
# for client's use
# assorted flags (see defines)
# loop control counter
# reserved for driver
# reserved for driver
# flags for dwFlags field of WAVEHDR
# done bit
# set if this header has been prepared
WHDR_DONE = 0x00000001
# loop start block
WHDR_PREPARED = 0x00000002
# loop end block
WHDR_BEGINLOOP = 0x00000004
# reserved for driver
WHDR_ENDLOOP = 0x00000008
WHDR_INQUEUE = 0x00000010
# waveform output device capabilities structure


class tagWAVEOUTCAPSA(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('dwFormats', DWORD),
        ('wChannels', WORD),
        ('wReserved1', WORD),
        ('dwSupport', DWORD),
    ]


WAVEOUTCAPSA = tagWAVEOUTCAPSA
PWAVEOUTCAPSA = POINTER(tagWAVEOUTCAPSA)
NPWAVEOUTCAPSA = POINTER(tagWAVEOUTCAPSA)
LPWAVEOUTCAPSA = POINTER(tagWAVEOUTCAPSA)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# formats supported
# number of sources supported
# packing
# functionality supported by driver

class tagWAVEOUTCAPSW(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('dwFormats', DWORD),
        ('wChannels', WORD),
        ('wReserved1', WORD),
        ('dwSupport', DWORD),
    ]


WAVEOUTCAPSW = tagWAVEOUTCAPSW
PWAVEOUTCAPSW = POINTER(tagWAVEOUTCAPSW)
NPWAVEOUTCAPSW = POINTER(tagWAVEOUTCAPSW)
LPWAVEOUTCAPSW = POINTER(tagWAVEOUTCAPSW)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# formats supported
# number of sources supported
# packing
# functionality supported by driver
WAVEOUTCAPS = WAVEOUTCAPSW
PWAVEOUTCAPS = PWAVEOUTCAPSW
NPWAVEOUTCAPS = NPWAVEOUTCAPSW
LPWAVEOUTCAPS = LPWAVEOUTCAPSW
# UNICODE


class tagWAVEOUTCAPS2A(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('dwFormats', DWORD),
        ('wChannels', WORD),
        ('wReserved1', WORD),
        ('dwSupport', DWORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


WAVEOUTCAPS2A = tagWAVEOUTCAPS2A
PWAVEOUTCAPS2A = POINTER(tagWAVEOUTCAPS2A)
NPWAVEOUTCAPS2A = POINTER(tagWAVEOUTCAPS2A)
LPWAVEOUTCAPS2A = POINTER(tagWAVEOUTCAPS2A)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# formats supported
# number of sources supported
# packing
# functionality supported by driver
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry

class tagWAVEOUTCAPS2W(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('dwFormats', DWORD),
        ('wChannels', WORD),
        ('wReserved1', WORD),
        ('dwSupport', DWORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


WAVEOUTCAPS2W = tagWAVEOUTCAPS2W
PWAVEOUTCAPS2W = POINTER(tagWAVEOUTCAPS2W)
NPWAVEOUTCAPS2W = POINTER(tagWAVEOUTCAPS2W)
LPWAVEOUTCAPS2W = POINTER(tagWAVEOUTCAPS2W)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# formats supported
# number of sources supported
# packing
# functionality supported by driver
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry
WAVEOUTCAPS2 = WAVEOUTCAPS2W
PWAVEOUTCAPS2 = PWAVEOUTCAPS2W
NPWAVEOUTCAPS2 = NPWAVEOUTCAPS2W
LPWAVEOUTCAPS2 = LPWAVEOUTCAPS2W
# UNICODE

# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# formats supported
# number of sources supported
# functionality supported by driver
# flags for dwSupport field of WAVEOUTCAPS
# supports pitch control
# supports playback rate control
WAVECAPS_PITCH = 0x0001
# supports volume control
WAVECAPS_PLAYBACKRATE = 0x0002
# separate left-right volume control
WAVECAPS_VOLUME = 0x0004
WAVECAPS_LRVOLUME = 0x0008
WAVECAPS_SYNC = 0x0010
WAVECAPS_SAMPLEACCURATE = 0x0020
# waveform input device capabilities structure


class tagWAVEINCAPSA(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('dwFormats', DWORD),
        ('wChannels', WORD),
        ('wReserved1', WORD),
    ]


WAVEINCAPSA = tagWAVEINCAPSA
PWAVEINCAPSA = POINTER(tagWAVEINCAPSA)
NPWAVEINCAPSA = POINTER(tagWAVEINCAPSA)
LPWAVEINCAPSA = POINTER(tagWAVEINCAPSA)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# formats supported
# number of channels supported
# structure packing

class tagWAVEINCAPSW(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('dwFormats', DWORD),
        ('wChannels', WORD),
        ('wReserved1', WORD),
    ]


WAVEINCAPSW = tagWAVEINCAPSW
PWAVEINCAPSW = POINTER(tagWAVEINCAPSW)
NPWAVEINCAPSW = POINTER(tagWAVEINCAPSW)
LPWAVEINCAPSW = POINTER(tagWAVEINCAPSW)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# formats supported
# number of channels supported
# structure packing
WAVEINCAPS = WAVEINCAPSW
PWAVEINCAPS = PWAVEINCAPSW
NPWAVEINCAPS = NPWAVEINCAPSW
LPWAVEINCAPS = LPWAVEINCAPSW
# UNICODE


class tagWAVEINCAPS2A(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('dwFormats', DWORD),
        ('wChannels', WORD),
        ('wReserved1', WORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


WAVEINCAPS2A = tagWAVEINCAPS2A
PWAVEINCAPS2A = POINTER(tagWAVEINCAPS2A)
NPWAVEINCAPS2A = POINTER(tagWAVEINCAPS2A)
LPWAVEINCAPS2A = POINTER(tagWAVEINCAPS2A)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# formats supported
# number of channels supported
# structure packing
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry

class tagWAVEINCAPS2W(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('dwFormats', DWORD),
        ('wChannels', WORD),
        ('wReserved1', WORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


WAVEINCAPS2W = tagWAVEINCAPS2W
PWAVEINCAPS2W = POINTER(tagWAVEINCAPS2W)
NPWAVEINCAPS2W = POINTER(tagWAVEINCAPS2W)
LPWAVEINCAPS2W = POINTER(tagWAVEINCAPS2W)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# formats supported
# number of channels supported
# structure packing
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry
WAVEINCAPS2 = WAVEINCAPS2W
PWAVEINCAPS2 = PWAVEINCAPS2W
NPWAVEINCAPS2 = NPWAVEINCAPS2W
LPWAVEINCAPS2 = LPWAVEINCAPS2W
# UNICODE

# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# formats supported
# number of channels supported
# defines for dwFormat field of WAVEINCAPS and WAVEOUTCAPS
# invalid format
# 11.025 kHz, Mono,   8-bit
WAVE_INVALIDFORMAT = 0x00000000
# 11.025 kHz, Stereo, 8-bit
WAVE_FORMAT_1M08 = 0x00000001
# 11.025 kHz, Mono,   16-bit
WAVE_FORMAT_1S08 = 0x00000002
# 11.025 kHz, Stereo, 16-bit
WAVE_FORMAT_1M16 = 0x00000004
# 22.05  kHz, Mono,   8-bit
WAVE_FORMAT_1S16 = 0x00000008
# 22.05  kHz, Stereo, 8-bit
WAVE_FORMAT_2M08 = 0x00000010
# 22.05  kHz, Mono,   16-bit
WAVE_FORMAT_2S08 = 0x00000020
# 22.05  kHz, Stereo, 16-bit
WAVE_FORMAT_2M16 = 0x00000040
# 44.1   kHz, Mono,   8-bit
WAVE_FORMAT_2S16 = 0x00000080
# 44.1   kHz, Stereo, 8-bit
WAVE_FORMAT_4M08 = 0x00000100
# 44.1   kHz, Mono,   16-bit
WAVE_FORMAT_4S08 = 0x00000200
# 44.1   kHz, Stereo, 16-bit
WAVE_FORMAT_4M16 = 0x00000400
WAVE_FORMAT_4S16 = 0x00000800
# 44.1   kHz, Mono,   8-bit
# 44.1   kHz, Stereo, 8-bit
WAVE_FORMAT_44M08 = 0x00000100
# 44.1   kHz, Mono,   16-bit
WAVE_FORMAT_44S08 = 0x00000200
# 44.1   kHz, Stereo, 16-bit
WAVE_FORMAT_44M16 = 0x00000400
# 48     kHz, Mono,   8-bit
WAVE_FORMAT_44S16 = 0x00000800
# 48     kHz, Stereo, 8-bit
WAVE_FORMAT_48M08 = 0x00001000
# 48     kHz, Mono,   16-bit
WAVE_FORMAT_48S08 = 0x00002000
# 48     kHz, Stereo, 16-bit
WAVE_FORMAT_48M16 = 0x00004000
# 96     kHz, Mono,   8-bit
WAVE_FORMAT_48S16 = 0x00008000
# 96     kHz, Stereo, 8-bit
WAVE_FORMAT_96M08 = 0x00010000
# 96     kHz, Mono,   16-bit
WAVE_FORMAT_96S08 = 0x00020000
# 96     kHz, Stereo, 16-bit
WAVE_FORMAT_96M16 = 0x00040000
WAVE_FORMAT_96S16 = 0x00080000
# OLD general waveform format structure (information common to all formats)


class waveformat_tag(ctypes.Structure):
    _fields_ = [
        ('wFormatTag', WORD),
        ('nChannels', WORD),
        ('nSamplesPerSec', DWORD),
        ('nAvgBytesPerSec', DWORD),
        ('nBlockAlign', WORD),
    ]


WAVEFORMAT = waveformat_tag
PWAVEFORMAT = POINTER(waveformat_tag)
NPWAVEFORMAT = POINTER(waveformat_tag)
LPWAVEFORMAT = POINTER(waveformat_tag)


# format type
# number of channels (i.e. mono, stereo, etc.)
# sample rate
# for buffer estimation
# block size of data
# flags for wFormatTag field of WAVEFORMAT
WAVE_FORMAT_PCM = 0x1
# specific waveform format structure for PCM data


class pcmwaveformat_tag(ctypes.Structure):
    _fields_ = [
        ('wf', WAVEFORMAT),
        ('wBitsPerSample', WORD),
    ]


PCMWAVEFORMAT = pcmwaveformat_tag
PPCMWAVEFORMAT = POINTER(pcmwaveformat_tag)
NPPCMWAVEFORMAT = POINTER(pcmwaveformat_tag)
LPPCMWAVEFORMAT = POINTER(pcmwaveformat_tag)


# WAVE_FORMAT_PCM
# *  extended waveform format structure used for all non-PCM formats. this
# *  structure is common to all non-PCM formats.

class tWAVEFORMATEX(ctypes.Structure):
    _fields_ = [
        ('wFormatTag', WORD),
        ('nChannels', WORD),
        ('nSamplesPerSec', DWORD),
        ('nAvgBytesPerSec', DWORD),
        ('nBlockAlign', WORD),
        ('wBitsPerSample', WORD),
        ('cbSize', WORD),
    ]


WAVEFORMATEX = tWAVEFORMATEX
PWAVEFORMATEX = POINTER(tWAVEFORMATEX)
NPWAVEFORMATEX = POINTER(tWAVEFORMATEX)
LPWAVEFORMATEX = POINTER(tWAVEFORMATEX)


# format type
# number of channels (i.e. mono, stereo...)
# sample rate
# for buffer estimation
# block size of data
# number of bits per sample of mono data
# the count in bytes of the size of
# extra information (after cbSize)
# _WAVEFORMATEX_
LPCWAVEFORMATEX = POINTER(FAR)
# waveform audio function prototypes
# WINMMAPI
# UINT
# WINAPI
# waveOutGetNumDevs(
#     VOID
#     );
waveOutGetNumDevs = winmm.waveOutGetNumDevs
waveOutGetNumDevs.restype = UINT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutGetDevCapsA(
#     _In_ UINT_PTR uDeviceID,
#     _Out_ LPWAVEOUTCAPSA pwoc,
#     _In_ UINT cbwoc
#     );
waveOutGetDevCapsA = winmm.waveOutGetDevCapsA
waveOutGetDevCapsA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutGetDevCapsW(
#     _In_ UINT_PTR uDeviceID,
#     _Out_ LPWAVEOUTCAPSW pwoc,
#     _In_ UINT cbwoc
#     );
waveOutGetDevCapsW = winmm.waveOutGetDevCapsW
waveOutGetDevCapsW.restype = MMRESULT

waveOutGetDevCaps = waveOutGetDevCapsW
# !UNICODE
# waveOutGetDevCaps = waveOutGetDevCapsA
# WINMMAPI
# MMRESULT
# WINAPI
# waveOutGetVolume(
#     _In_opt_ HWAVEOUT hwo,
#     _Out_ LPDWORD pdwVolume
#     );
waveOutGetVolume = winmm.waveOutGetVolume
waveOutGetVolume.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutSetVolume(
#     _In_opt_ HWAVEOUT hwo,
#     _In_ DWORD dwVolume
#     );
waveOutSetVolume = winmm.waveOutSetVolume
waveOutSetVolume.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutGetErrorTextA(
#     _In_ MMRESULT mmrError,
#     _Out_writes_(cchText) LPSTR pszText,
#     _In_ UINT cchText
#     );
waveOutGetErrorTextA = winmm.waveOutGetErrorTextA
waveOutGetErrorTextA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutGetErrorTextW(
#     _In_ MMRESULT mmrError,
#     _Out_writes_(cchText) LPWSTR pszText,
#     _In_ UINT cchText
#     );
waveOutGetErrorTextW = winmm.waveOutGetErrorTextW
waveOutGetErrorTextW.restype = MMRESULT

waveOutGetErrorText = waveOutGetErrorTextW
# !UNICODE
# waveOutGetErrorText = waveOutGetErrorTextA
# WINMMAPI
# MMRESULT
# WINAPI
# waveOutOpen(
#     _Out_opt_ LPHWAVEOUT phwo,
#     _In_ UINT uDeviceID,
#     _In_ LPCWAVEFORMATEX pwfx,
#     _In_opt_ DWORD_PTR dwCallback,
#     _In_opt_ DWORD_PTR dwInstance,
#     _In_ DWORD fdwOpen
#     );
waveOutOpen = winmm.waveOutOpen
waveOutOpen.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutClose(
#     _In_ HWAVEOUT hwo
#     );
waveOutClose = winmm.waveOutClose
waveOutClose.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutPrepareHeader(
#     _In_ HWAVEOUT hwo,
#     _Inout_updates_bytes_(cbwh) LPWAVEHDR pwh,
#     _In_ UINT cbwh
#     );
waveOutPrepareHeader = winmm.waveOutPrepareHeader
waveOutPrepareHeader.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutUnprepareHeader(
#     _In_ HWAVEOUT hwo,
#     _Inout_updates_bytes_(cbwh) LPWAVEHDR pwh,
#     _In_ UINT cbwh
#     );
waveOutUnprepareHeader = winmm.waveOutUnprepareHeader
waveOutUnprepareHeader.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutWrite(
#     _In_ HWAVEOUT hwo,
#     _Inout_updates_bytes_(cbwh) LPWAVEHDR pwh,
#     _In_ UINT cbwh
#     );
waveOutWrite = winmm.waveOutWrite
waveOutWrite.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutPause(
#     _In_ HWAVEOUT hwo
#     );
waveOutPause = winmm.waveOutPause
waveOutPause.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutRestart(
#     _In_ HWAVEOUT hwo
#     );
waveOutRestart = winmm.waveOutRestart
waveOutRestart.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutReset(
#     _In_ HWAVEOUT hwo
#     );
waveOutReset = winmm.waveOutReset
waveOutReset.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutBreakLoop(
#     _In_ HWAVEOUT hwo
#     );
waveOutBreakLoop = winmm.waveOutBreakLoop
waveOutBreakLoop.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutGetPosition(
#     _In_ HWAVEOUT hwo,
#     _Inout_updates_bytes_(cbmmt) LPMMTIME pmmt,
#     _In_ UINT cbmmt
#     );
waveOutGetPosition = winmm.waveOutGetPosition
waveOutGetPosition.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutGetPitch(
#     _In_ HWAVEOUT hwo,
#     _Out_ LPDWORD pdwPitch
#     );
waveOutGetPitch = winmm.waveOutGetPitch
waveOutGetPitch.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutSetPitch(
#     _In_ HWAVEOUT hwo,
#     _In_ DWORD dwPitch
#     );
waveOutSetPitch = winmm.waveOutSetPitch
waveOutSetPitch.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutGetPlaybackRate(
#     _In_ HWAVEOUT hwo,
#     _Out_ LPDWORD pdwRate
#     );
waveOutGetPlaybackRate = winmm.waveOutGetPlaybackRate
waveOutGetPlaybackRate.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutSetPlaybackRate(
#     _In_ HWAVEOUT hwo,
#     _In_ DWORD dwRate
#     );
waveOutSetPlaybackRate = winmm.waveOutSetPlaybackRate
waveOutSetPlaybackRate.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutGetID(
#     _In_ HWAVEOUT hwo,
#     _Out_ LPUINT puDeviceID
#     );
waveOutGetID = winmm.waveOutGetID
waveOutGetID.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveOutMessage(
#     _In_opt_ HWAVEOUT hwo,
#     _In_ UINT uMsg,
#     _In_ DWORD_PTR dw1,
#     _In_ DWORD_PTR dw2
#     );
waveOutMessage = winmm.waveOutMessage
waveOutMessage.restype = MMRESULT

# ifdef WINVER >= 0x030a
# WINMMAPI
# UINT
# WINAPI
# waveInGetNumDevs(
#     VOID
#     );
waveInGetNumDevs = winmm.waveInGetNumDevs
waveInGetNumDevs.restype = UINT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInGetDevCapsA(
#     _In_ UINT_PTR uDeviceID,
#     _Out_writes_bytes_(cbwic) LPWAVEINCAPSA pwic,
#     _In_ UINT cbwic
#     );
waveInGetDevCapsA = winmm.waveInGetDevCapsA
waveInGetDevCapsA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInGetDevCapsW(
#     _In_ UINT_PTR uDeviceID,
#     _Out_writes_bytes_(cbwic) LPWAVEINCAPSW pwic,
#     _In_ UINT cbwic
#     );
waveInGetDevCapsW = winmm.waveInGetDevCapsW
waveInGetDevCapsW.restype = MMRESULT

waveInGetDevCaps = waveInGetDevCapsW
# !UNICODE
# waveInGetDevCaps = waveInGetDevCapsA
# WINMMAPI
# MMRESULT
# WINAPI
# waveInGetErrorTextA(
#     _In_ MMRESULT mmrError,
#     _Out_writes_(cchText) LPSTR pszText,
#     _In_ UINT cchText
#     );
waveInGetErrorTextA = winmm.waveInGetErrorTextA
waveInGetErrorTextA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInGetErrorTextW(
#     _In_ MMRESULT mmrError,
#     _Out_writes_(cchText) LPWSTR pszText,
#     _In_ UINT cchText
#     );
waveInGetErrorTextW = winmm.waveInGetErrorTextW
waveInGetErrorTextW.restype = MMRESULT

waveInGetErrorText = waveInGetErrorTextW
# !UNICODE
# waveInGetErrorText = waveInGetErrorTextA
# WINMMAPI
# MMRESULT
# WINAPI
# waveInOpen(
#     _Out_opt_ LPHWAVEIN phwi,
#     _In_ UINT uDeviceID,
#     _In_ LPCWAVEFORMATEX pwfx,
#     _In_opt_ DWORD_PTR dwCallback,
#     _In_opt_ DWORD_PTR dwInstance,
#     _In_ DWORD fdwOpen
#     );
waveInOpen = winmm.waveInOpen
waveInOpen.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInClose(
#     _In_ HWAVEIN hwi
#     );
waveInClose = winmm.waveInClose
waveInClose.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInPrepareHeader(
#     _In_ HWAVEIN hwi,
#     _Inout_updates_bytes_(cbwh) LPWAVEHDR pwh,
#     _In_ UINT cbwh
#     );
waveInPrepareHeader = winmm.waveInPrepareHeader
waveInPrepareHeader.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInUnprepareHeader(
#     _In_ HWAVEIN hwi,
#     _Inout_updates_bytes_(cbwh) LPWAVEHDR pwh,
#     _In_ UINT cbwh
#     );
waveInUnprepareHeader = winmm.waveInUnprepareHeader
waveInUnprepareHeader.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInAddBuffer(
#     _In_ HWAVEIN hwi,
#     _Inout_updates_bytes_(cbwh) LPWAVEHDR pwh,
#     _In_ UINT cbwh
#     );
waveInAddBuffer = winmm.waveInAddBuffer
waveInAddBuffer.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInStart(
#     _In_ HWAVEIN hwi
#     );
waveInStart = winmm.waveInStart
waveInStart.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInStop(
#     _In_ HWAVEIN hwi
#     );
waveInStop = winmm.waveInStop
waveInStop.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInReset(
#     _In_ HWAVEIN hwi
#     );
waveInReset = winmm.waveInReset
waveInReset.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInGetPosition(
#     _In_ HWAVEIN hwi,
#     _Inout_updates_bytes_(cbmmt) LPMMTIME pmmt,
#     _In_ UINT cbmmt
#     );
waveInGetPosition = winmm.waveInGetPosition
waveInGetPosition.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInGetID(
#     _In_ HWAVEIN hwi,
#     _In_ LPUINT puDeviceID
#     );
waveInGetID = winmm.waveInGetID
waveInGetID.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# waveInMessage(
#     _In_opt_ HWAVEIN hwi,
#     _In_ UINT uMsg,
#     _In_opt_ DWORD_PTR dw1,
#     _In_opt_ DWORD_PTR dw2
#     );
waveInMessage = winmm.waveInMessage
waveInMessage.restype = MMRESULT

# ifdef WINVER >= 0x030a
# ifndef MMNOWAVE
# ***************************************************************************
# MIDI audio support
# ***************************************************************************
# MIDI error return values
# header not prepared
# still something playing
MIDIERR_UNPREPARED = MIDIERR_BASE + 0
# no configured instruments
MIDIERR_STILLPLAYING = MIDIERR_BASE + 1
# hardware is still busy
MIDIERR_NOMAP = MIDIERR_BASE + 2
# port no LONGer connected
MIDIERR_NOTREADY = MIDIERR_BASE + 3
# invalid MIF
MIDIERR_NODEVICE = MIDIERR_BASE + 4
# operation unsupported w/ open mode
MIDIERR_INVALIDSETUP = MIDIERR_BASE + 5
# thru device 'eating' a message
MIDIERR_BADOPENMODE = MIDIERR_BASE + 6
# last error in range
MIDIERR_DONT_CONTINUE = MIDIERR_BASE + 7
MIDIERR_LASTERROR = MIDIERR_BASE + 7
# MIDI audio data types

HMIDI = HANDLE
HMIDIIN = HANDLE
HMIDIOUT = HANDLE
HMIDISTRM = HANDLE

LPHMIDI = POINTER(HMIDI)
LPHMIDIIN = POINTER(HMIDIIN)
LPHMIDIOUT = POINTER(HMIDIOUT)
LPHMIDISTRM = POINTER(HMIDISTRM)
MIDICALLBACK = DRVCALLBACK
LPMIDICALLBACK = POINTER(DRVCALLBACK)
MIDIPATCHSIZE = 0x80
PATCHARRAY = WORD * MIDIPATCHSIZE
LPPATCHARRAY = POINTER(PATCHARRAY)
KEYARRAY = WORD * MIDIPATCHSIZE
LPKEYARRAY = POINTER(KEYARRAY)

# MIDI callback messages
MIM_OPEN = MM_MIM_OPEN
MIM_CLOSE = MM_MIM_CLOSE
# MIM_DATA = MM_MIM_DATA
# MIM_LONGDATA = MM_MIM_LONGDATA
MIM_ERROR = MM_MIM_ERROR
MIM_LONGERROR = MM_MIM_LONGERROR
MOM_OPEN = MM_MOM_OPEN
MOM_CLOSE = MM_MOM_CLOSE
MOM_DONE = MM_MOM_DONE
# MIM_MOREDATA = MM_MIM_MOREDATA
# WINVER >= 0x0400
MOM_POSITIONCB = MM_MOM_POSITIONCB
# device ID for MIDI mapper
MIDIMAPPER = -1
MIDI_MAPPER = -1
# flags for dwFlags parm of midiInOpen()
# WINVER >= 0x0400
MIDI_IO_STATUS = 0x00000020
# flags for wFlags parm of midiOutCachePatches(), midiOutCacheDrumPatches()
MIDI_CACHE_ALL = 0x1
MIDI_CACHE_BESTFIT = 0x2
MIDI_CACHE_QUERY = 0x3
MIDI_UNCACHE = 0x4
# MIDI output device capabilities structure


class tagMIDIOUTCAPSA(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('wTechnology', WORD),
        ('wVoices', WORD),
        ('wNotes', WORD),
        ('wChannelMask', WORD),
        ('dwSupport', DWORD),
    ]


MIDIOUTCAPSA = tagMIDIOUTCAPSA
PMIDIOUTCAPSA = POINTER(tagMIDIOUTCAPSA)
NPMIDIOUTCAPSA = POINTER(tagMIDIOUTCAPSA)
LPMIDIOUTCAPSA = POINTER(tagMIDIOUTCAPSA)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# type of device
# # of voices (INTernal synth only)
# max # of notes (INTernal synth only)
# channels used (INTernal synth only)
# functionality supported by driver

class tagMIDIOUTCAPSW(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('wTechnology', WORD),
        ('wVoices', WORD),
        ('wNotes', WORD),
        ('wChannelMask', WORD),
        ('dwSupport', DWORD),
    ]


MIDIOUTCAPSW = tagMIDIOUTCAPSW
PMIDIOUTCAPSW = POINTER(tagMIDIOUTCAPSW)
NPMIDIOUTCAPSW = POINTER(tagMIDIOUTCAPSW)
LPMIDIOUTCAPSW = POINTER(tagMIDIOUTCAPSW)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# type of device
# # of voices (INTernal synth only)
# max # of notes (INTernal synth only)
# channels used (INTernal synth only)
# functionality supported by driver
MIDIOUTCAPS = MIDIOUTCAPSW
PMIDIOUTCAPS = PMIDIOUTCAPSW
NPMIDIOUTCAPS = NPMIDIOUTCAPSW
LPMIDIOUTCAPS = LPMIDIOUTCAPSW
# UNICODE


class tagMIDIOUTCAPS2A(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('wTechnology', WORD),
        ('wVoices', WORD),
        ('wNotes', WORD),
        ('wChannelMask', WORD),
        ('dwSupport', DWORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


MIDIOUTCAPS2A = tagMIDIOUTCAPS2A
PMIDIOUTCAPS2A = POINTER(tagMIDIOUTCAPS2A)
NPMIDIOUTCAPS2A = POINTER(tagMIDIOUTCAPS2A)
LPMIDIOUTCAPS2A = POINTER(tagMIDIOUTCAPS2A)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# type of device
# # of voices (INTernal synth only)
# max # of notes (INTernal synth only)
# channels used (INTernal synth only)
# functionality supported by driver
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry

class tagMIDIOUTCAPS2W(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('wTechnology', WORD),
        ('wVoices', WORD),
        ('wNotes', WORD),
        ('wChannelMask', WORD),
        ('dwSupport', DWORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


MIDIOUTCAPS2W = tagMIDIOUTCAPS2W
PMIDIOUTCAPS2W = POINTER(tagMIDIOUTCAPS2W)
NPMIDIOUTCAPS2W = POINTER(tagMIDIOUTCAPS2W)
LPMIDIOUTCAPS2W = POINTER(tagMIDIOUTCAPS2W)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# type of device
# # of voices (INTernal synth only)
# max # of notes (INTernal synth only)
# channels used (INTernal synth only)
# functionality supported by driver
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry
MIDIOUTCAPS2 = MIDIOUTCAPS2W
PMIDIOUTCAPS2 = PMIDIOUTCAPS2W
NPMIDIOUTCAPS2 = NPMIDIOUTCAPS2W
LPMIDIOUTCAPS2 = LPMIDIOUTCAPS2W
# UNICODE

# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# type of device
# # of voices (INTernal synth only)
# max # of notes (INTernal synth only)
# channels used (INTernal synth only)
# functionality supported by driver
# flags for wTechnology field of MIDIOUTCAPS structure
# output port
# generic INTernal synth
MOD_MIDIPORT = 0x1
# square wave INTernal synth
MOD_SYNTH = 0x2
# FM INTernal synth
MOD_SQSYNTH = 0x3
# MIDI mapper
MOD_FMSYNTH = 0x4
# hardware wavetable synth
MOD_MAPPER = 0x5
# software synth
MOD_WAVETABLE = 0x6
MOD_SWSYNTH = 0x7
# flags for dwSupport field of MIDIOUTCAPS structure
# supports volume control
# separate left-right volume control
MIDICAPS_VOLUME = 0x0001
MIDICAPS_LRVOLUME = 0x0002
MIDICAPS_CACHE = 0x0004
# driver supports midiStreamOut directly
# WINVER >= 0x0400
MIDICAPS_STREAM = 0x0008
# MIDI input device capabilities structure


class tagMIDIINCAPSA(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('dwSupport', DWORD),
    ]


MIDIINCAPSA = tagMIDIINCAPSA
PMIDIINCAPSA = POINTER(tagMIDIINCAPSA)
NPMIDIINCAPSA = POINTER(tagMIDIINCAPSA)
LPMIDIINCAPSA = POINTER(tagMIDIINCAPSA)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# functionality supported by driver

class tagMIDIINCAPSW(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('dwSupport', DWORD),
    ]


MIDIINCAPSW = tagMIDIINCAPSW
PMIDIINCAPSW = POINTER(tagMIDIINCAPSW)
NPMIDIINCAPSW = POINTER(tagMIDIINCAPSW)
LPMIDIINCAPSW = POINTER(tagMIDIINCAPSW)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# functionality supported by driver
MIDIINCAPS = MIDIINCAPSW
PMIDIINCAPS = PMIDIINCAPSW
NPMIDIINCAPS = NPMIDIINCAPSW
LPMIDIINCAPS = LPMIDIINCAPSW
# UNICODE


class tagMIDIINCAPS2A(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('dwSupport', DWORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


MIDIINCAPS2A = tagMIDIINCAPS2A
PMIDIINCAPS2A = POINTER(tagMIDIINCAPS2A)
NPMIDIINCAPS2A = POINTER(tagMIDIINCAPS2A)
LPMIDIINCAPS2A = POINTER(tagMIDIINCAPS2A)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# functionality supported by driver
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry

class tagMIDIINCAPS2W(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('dwSupport', DWORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


MIDIINCAPS2W = tagMIDIINCAPS2W
PMIDIINCAPS2W = POINTER(tagMIDIINCAPS2W)
NPMIDIINCAPS2W = POINTER(tagMIDIINCAPS2W)
LPMIDIINCAPS2W = POINTER(tagMIDIINCAPS2W)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# functionality supported by driver
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry
MIDIINCAPS2 = MIDIINCAPS2W
PMIDIINCAPS2 = PMIDIINCAPS2W
NPMIDIINCAPS2 = NPMIDIINCAPS2W
LPMIDIINCAPS2 = LPMIDIINCAPS2W
# UNICODE

# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# functionality supported by driver
# MIDI data block header


class midihdr_tag(ctypes.Structure):
    pass


midihdr_tag._fields_ = [
    ('lpData', LPSTR),
    ('dwBufferLength', DWORD),
    ('dwBytesRecorded', DWORD),
    ('dwUser', DWORD_PTR),
    ('dwFlags', DWORD),
    ('lpNext', POINTER(midihdr_tag)),
    ('reserved', DWORD_PTR),
    ('dwOffset', DWORD),
    ('dwReserved', DWORD_PTR * 8),
]


MIDIHDR = midihdr_tag
PMIDIHDR = POINTER(midihdr_tag)
NPMIDIHDR = POINTER(midihdr_tag)
LPMIDIHDR = POINTER(midihdr_tag)


# poINTer to locked data block
# length of data in data block
# used for input only
# for client's use
# assorted flags (see defines)
# reserved for driver
# reserved for driver
# Callback offset INTo buffer
# Reserved for MMSYSTEM

class midievent_tag(ctypes.Structure):
    _fields_ = [
        ('dwDeltaTime', DWORD),
        ('dwStreamID', DWORD),
        ('dwEvent', DWORD),
        ('dwParms', DWORD * 1),
    ]


MIDIEVENT = midievent_tag


# Ticks since last event
# Reserved; must be zero
# Event type and parameters
# Parameters if this is a LONG event

class midistrmbuffver_tag(ctypes.Structure):
    _fields_ = [
        ('dwVersion', DWORD),
        ('dwMid', DWORD),
        ('dwOEMVersion', DWORD),
    ]


MIDISTRMBUFFVER = midistrmbuffver_tag


# Stream buffer format version
# Manufacturer ID as defined in MMREG.H
# Manufacturer version for custom ext
# WINVER >= 0x0400
# flags for dwFlags field of MIDIHDR structure
# done bit
# set if header prepared
MHDR_DONE = 0x00000001
# reserved for driver
MHDR_PREPARED = 0x00000002
# Buffer is stream buffer
MHDR_INQUEUE = 0x00000004
MHDR_ISSTRM = 0x00000008

# Type codes which go in the high byte of the event DWORD of a stream buffer

# Type codes 00-7F contain parameters within the low 24 bits
# Type codes 80-FF contain a length of their parameter in the low 24
# bits, followed by their parameter data in the buffer. The event
# DWORD contains the exact byte length; the parm data itself must be
# padded to be an even multiple of 4 bytes LONG.

MEVT_F_SHORT = 0x00000000
MEVT_F_LONG = 0x80000000
MEVT_F_CALLBACK = 0x40000000


def MEVT_EVENTTYPE(x):
    return (x >> 24) & 0xFF


def MEVT_EVENTPARM(x):
    return x & 0x00FFFFFF


# parm = SHORTmsg for midiOutShortMsg
# parm = new tempo in microsec/qn
MEVT_SHORTMSG = 0x00
# parm = unused; does nothing
MEVT_TEMPO = 0x01
MEVT_NOP = 0x02
# 0x04-0x7F reserved
# parm = bytes to send verbatim
# parm = comment data
MEVT_LONGMSG = 0x80
# parm = MIDISTRMBUFFVER struct
MEVT_COMMENT = 0x82
MEVT_VERSION = 0x84
# 0x81-0xFF reserved
MIDISTRM_ERROR = -2

# Structures and defines for midiStreamProperty

MIDIPROP_SET = 0x80000000
MIDIPROP_GET = 0x40000000
# These are INTentionally both non-zero so the app cannot accidentally
# leave the operation off and happen to appear to work due to default
# action.
MIDIPROP_TIMEDIV = 0x00000001
MIDIPROP_TEMPO = 0x00000002


class midiproptimediv_tag(ctypes.Structure):
    _fields_ = [
        ('cbStruct', DWORD),
        ('dwTimeDiv', DWORD),
    ]


MIDIPROPTIMEDIV = midiproptimediv_tag
LPMIDIPROPTIMEDIV = POINTER(midiproptimediv_tag)


class midiproptempo_tag(ctypes.Structure):
    _fields_ = [
        ('cbStruct', DWORD),
        ('dwTempo', DWORD),
    ]


MIDIPROPTEMPO = midiproptempo_tag
LPMIDIPROPTEMPO = POINTER(midiproptempo_tag)


# WINVER >= 0x0400
# MIDI function prototypes
# WINMMAPI
# UINT
# WINAPI
# midiOutGetNumDevs(
#     VOID
#     );
midiOutGetNumDevs = winmm.midiOutGetNumDevs
midiOutGetNumDevs.restype = UINT

# WINMMAPI
# MMRESULT
# WINAPI
# midiStreamOpen(
#     _Out_ LPHMIDISTRM phms,
#     _Inout_updates_(cMidi) LPUINT puDeviceID,
#     _In_ DWORD cMidi,
#     _In_opt_ DWORD_PTR dwCallback,
#     _In_opt_ DWORD_PTR dwInstance,
#     _In_ DWORD fdwOpen
#     );
midiStreamOpen = winmm.midiStreamOpen
midiStreamOpen.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiStreamClose(
#     _In_ HMIDISTRM hms
#     );
midiStreamClose = winmm.midiStreamClose
midiStreamClose.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiStreamProperty(
#     _In_ HMIDISTRM hms,
#     _Inout_updates_bytes_(ctypes.sizeof(DWORD) + ctypes.sizeof(DWORD))
# LPBYTE lppropdata,
#     _In_ DWORD dwProperty
#     );
midiStreamProperty = winmm.midiStreamProperty
midiStreamProperty.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiStreamPosition(
#     _In_ HMIDISTRM hms,
#     _Out_writes_bytes_(cbmmt) LPMMTIME lpmmt,
#     _In_ UINT cbmmt
#     );
midiStreamPosition = winmm.midiStreamPosition
midiStreamPosition.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiStreamOut(
#     _In_ HMIDISTRM hms,
#     _Out_writes_bytes_(cbmh) LPMIDIHDR pmh,
#     _In_ UINT cbmh
#     );
midiStreamOut = winmm.midiStreamOut
midiStreamOut.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiStreamPause(
#     _In_ HMIDISTRM hms
#     );
midiStreamPause = winmm.midiStreamPause
midiStreamPause.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiStreamRestart(
#     _In_ HMIDISTRM hms
#     );
midiStreamRestart = winmm.midiStreamRestart
midiStreamRestart.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiStreamStop(
#     _In_ HMIDISTRM hms
#     );
midiStreamStop = winmm.midiStreamStop
midiStreamStop.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiConnect(
#     _In_ HMIDI hmi,
#     _In_ HMIDIOUT hmo,
#     _In_opt_ LPVOID pReserved
#     );
midiConnect = winmm.midiConnect
midiConnect.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiDisconnect(
#     _In_ HMIDI hmi,
#     _In_ HMIDIOUT hmo,
#     _In_opt_ LPVOID pReserved
#     );
midiDisconnect = winmm.midiDisconnect
midiDisconnect.restype = MMRESULT

# WINVER >= 0x0400
# WINMMAPI
# MMRESULT
# WINAPI
# midiOutGetDevCapsA(
#     _In_ UINT_PTR uDeviceID,
#     _Out_writes_bytes_(cbmoc) LPMIDIOUTCAPSA pmoc,
#     _In_ UINT cbmoc
#     );
midiOutGetDevCapsA = winmm.midiOutGetDevCapsA
midiOutGetDevCapsA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutGetDevCapsW(
#     _In_ UINT_PTR uDeviceID,
#     _Out_writes_bytes_(cbmoc) LPMIDIOUTCAPSW pmoc,
#     _In_ UINT cbmoc
#     );
midiOutGetDevCapsW = winmm.midiOutGetDevCapsW
midiOutGetDevCapsW.restype = MMRESULT

midiOutGetDevCaps = midiOutGetDevCapsW
# !UNICODE
# midiOutGetDevCaps = midiOutGetDevCapsA
# WINMMAPI
# MMRESULT
# WINAPI
# midiOutGetVolume(
#     _In_opt_ HMIDIOUT hmo,
#     _Out_ LPDWORD pdwVolume
#     );
midiOutGetVolume = winmm.midiOutGetVolume
midiOutGetVolume.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutSetVolume(
#     _In_opt_ HMIDIOUT hmo,
#     _In_ DWORD dwVolume
#     );
midiOutSetVolume = winmm.midiOutSetVolume
midiOutSetVolume.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutGetErrorTextA(
#     _In_ MMRESULT mmrError,
#     _Out_writes_(cchText) LPSTR pszText,
#     _In_ UINT cchText
#     );
midiOutGetErrorTextA = winmm.midiOutGetErrorTextA
midiOutGetErrorTextA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutGetErrorTextW(
#     _In_ MMRESULT mmrError,
#     _Out_writes_(cchText) LPWSTR pszText,
#     _In_ UINT cchText
#     );
midiOutGetErrorTextW = winmm.midiOutGetErrorTextW
midiOutGetErrorTextW.restype = MMRESULT

midiOutGetErrorText = midiOutGetErrorTextW
# !UNICODE
# midiOutGetErrorText = midiOutGetErrorTextA
# WINMMAPI
# MMRESULT
# WINAPI
# midiOutOpen(
#     _Out_ LPHMIDIOUT phmo,
#     _In_ UINT uDeviceID,
#     _In_opt_ DWORD_PTR dwCallback,
#     _In_opt_ DWORD_PTR dwInstance,
#     _In_ DWORD fdwOpen
#     );
midiOutOpen = winmm.midiOutOpen
midiOutOpen.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutClose(
#     _In_ HMIDIOUT hmo
#     );
midiOutClose = winmm.midiOutClose
midiOutClose.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutPrepareHeader(
#     _In_ HMIDIOUT hmo,
#     _Inout_updates_bytes_(cbmh) LPMIDIHDR pmh,
#     _In_ UINT cbmh
#     );
midiOutPrepareHeader = winmm.midiOutPrepareHeader
midiOutPrepareHeader.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutUnprepareHeader(
#     _In_ HMIDIOUT hmo,
#     _Inout_updates_bytes_(cbmh) LPMIDIHDR pmh,
#     _In_ UINT cbmh
#     );
midiOutUnprepareHeader = winmm.midiOutUnprepareHeader
midiOutUnprepareHeader.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutShortMsg(
#     _In_ HMIDIOUT hmo,
#     _In_ DWORD dwMsg
#     );
midiOutShortMsg = winmm.midiOutShortMsg
midiOutShortMsg.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutLongMsg(
#     _In_ HMIDIOUT hmo,
#     _In_reads_bytes_(cbmh) LPMIDIHDR pmh,
#     _In_ UINT cbmh
#     );
midiOutLongMsg = winmm.midiOutLongMsg
midiOutLongMsg.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutReset(
#     _In_ HMIDIOUT hmo
#     );
midiOutReset = winmm.midiOutReset
midiOutReset.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutCachePatches(
#     _In_ HMIDIOUT hmo,
#     _In_ UINT uBank,
#     _In_reads_(MIDIPATCHSIZE) LPWORD pwpa,
#     _In_ UINT fuCache
#     );
midiOutCachePatches = winmm.midiOutCachePatches
midiOutCachePatches.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutCacheDrumPatches(
#     _In_ HMIDIOUT hmo,
#     _In_ UINT uPatch,
#     _In_reads_(MIDIPATCHSIZE) LPWORD pwkya,
#     _In_ UINT fuCache
#     );
midiOutCacheDrumPatches = winmm.midiOutCacheDrumPatches
midiOutCacheDrumPatches.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutGetID(
#     _In_ HMIDIOUT hmo,
#     _Out_ LPUINT puDeviceID
#     );
midiOutGetID = winmm.midiOutGetID
midiOutGetID.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiOutMessage(
#     _In_opt_ HMIDIOUT hmo,
#     _In_ UINT uMsg,
#     _In_opt_ DWORD_PTR dw1,
#     _In_opt_ DWORD_PTR dw2
#     );
midiOutMessage = winmm.midiOutMessage
midiOutMessage.restype = MMRESULT

# ifdef WINVER >= 0x030a
# WINMMAPI
# UINT
# WINAPI
# midiInGetNumDevs(
#     VOID
#     );
midiInGetNumDevs = winmm.midiInGetNumDevs
midiInGetNumDevs.restype = UINT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInGetDevCapsA(
#     _In_ UINT_PTR uDeviceID,
#     _Out_writes_bytes_(cbmic) LPMIDIINCAPSA pmic,
#     _In_ UINT cbmic
#     );
midiInGetDevCapsA = winmm.midiInGetDevCapsA
midiInGetDevCapsA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInGetDevCapsW(
#     _In_ UINT_PTR uDeviceID,
#     _Out_writes_bytes_(cbmic) LPMIDIINCAPSW pmic,
#     _In_ UINT cbmic
#     );
midiInGetDevCapsW = winmm.midiInGetDevCapsW
midiInGetDevCapsW.restype = MMRESULT

midiInGetDevCaps = midiInGetDevCapsW
# !UNICODE
# midiInGetDevCaps = midiInGetDevCapsA
# WINMMAPI
# MMRESULT
# WINAPI
# midiInGetErrorTextA(
#     _In_ MMRESULT mmrError,
#     _Out_writes_(cchText) LPSTR pszText,
#     _In_ UINT cchText
#     );
midiInGetErrorTextA = winmm.midiInGetErrorTextA
midiInGetErrorTextA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInGetErrorTextW(
#     _In_ MMRESULT mmrError,
#     _Out_writes_(cchText) LPWSTR pszText,
#     _In_ UINT cchText
#     );
midiInGetErrorTextW = winmm.midiInGetErrorTextW
midiInGetErrorTextW.restype = MMRESULT

midiInGetErrorText = midiInGetErrorTextW
# !UNICODE
# midiInGetErrorText = midiInGetErrorTextA
# WINMMAPI
# MMRESULT
# WINAPI
# midiInOpen(
#     _Out_ LPHMIDIIN phmi,
#     _In_ UINT uDeviceID,
#     _In_opt_ DWORD_PTR dwCallback,
#     _In_opt_ DWORD_PTR dwInstance,
#     _In_ DWORD fdwOpen
#     );
midiInOpen = winmm.midiInOpen
midiInOpen.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInClose(
#     _In_ HMIDIIN hmi
#     );
midiInClose = winmm.midiInClose
midiInClose.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInPrepareHeader(
#     _In_ HMIDIIN hmi,
#     _Inout_updates_bytes_(cbmh) LPMIDIHDR pmh,
#     _In_ UINT cbmh
#     );
midiInPrepareHeader = winmm.midiInPrepareHeader
midiInPrepareHeader.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInUnprepareHeader(
#     _In_ HMIDIIN hmi,
#     _Inout_updates_bytes_(cbmh) LPMIDIHDR pmh,
#     _In_ UINT cbmh
#     );
midiInUnprepareHeader = winmm.midiInUnprepareHeader
midiInUnprepareHeader.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInAddBuffer(
#     _In_ HMIDIIN hmi,
#     _Out_writes_bytes_(cbmh) LPMIDIHDR pmh,
#     _In_ UINT cbmh
#     );
midiInAddBuffer = winmm.midiInAddBuffer
midiInAddBuffer.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInStart(
#     _In_ HMIDIIN hmi
#     );
midiInStart = winmm.midiInStart
midiInStart.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInStop(
#     _In_ HMIDIIN hmi
#     );
midiInStop = winmm.midiInStop
midiInStop.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInReset(
#     _In_ HMIDIIN hmi
#     );
midiInReset = winmm.midiInReset
midiInReset.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInGetID(
#     _In_ HMIDIIN hmi,
#     _Out_ LPUINT puDeviceID
#     );
midiInGetID = winmm.midiInGetID
midiInGetID.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# midiInMessage(
#     _In_opt_ HMIDIIN hmi,
#     _In_ UINT uMsg,
#     _In_opt_ DWORD_PTR dw1,
#     _In_opt_ DWORD_PTR dw2
#     );
midiInMessage = winmm.midiInMessage
midiInMessage.restype = MMRESULT

# ifdef WINVER >= 0x030a
# ifndef MMNOMIDI
# ***************************************************************************
# Auxiliary audio support
# ***************************************************************************
# device ID for aux device mapper
AUX_MAPPER = -1
# Auxiliary audio device capabilities structure


class tagAUXCAPSA(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('wTechnology', WORD),
        ('wReserved1', WORD),
        ('dwSupport', DWORD),
    ]


AUXCAPSA = tagAUXCAPSA
PAUXCAPSA = POINTER(tagAUXCAPSA)
NPAUXCAPSA = POINTER(tagAUXCAPSA)
LPAUXCAPSA = POINTER(tagAUXCAPSA)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# type of device
# padding
# functionality supported by driver

class tagAUXCAPSW(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('wTechnology', WORD),
        ('wReserved1', WORD),
        ('dwSupport', DWORD),
    ]


AUXCAPSW = tagAUXCAPSW
PAUXCAPSW = POINTER(tagAUXCAPSW)
NPAUXCAPSW = POINTER(tagAUXCAPSW)
LPAUXCAPSW = POINTER(tagAUXCAPSW)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# type of device
# padding
# functionality supported by driver
AUXCAPS = AUXCAPSW
PAUXCAPS = PAUXCAPSW
NPAUXCAPS = NPAUXCAPSW
LPAUXCAPS = LPAUXCAPSW
# UNICODE


class tagAUXCAPS2A(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('wTechnology', WORD),
        ('wReserved1', WORD),
        ('dwSupport', DWORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


AUXCAPS2A = tagAUXCAPS2A
PAUXCAPS2A = POINTER(tagAUXCAPS2A)
NPAUXCAPS2A = POINTER(tagAUXCAPS2A)
LPAUXCAPS2A = POINTER(tagAUXCAPS2A)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# type of device
# padding
# functionality supported by driver
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry

class tagAUXCAPS2W(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('wTechnology', WORD),
        ('wReserved1', WORD),
        ('dwSupport', DWORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


AUXCAPS2W = tagAUXCAPS2W
PAUXCAPS2W = POINTER(tagAUXCAPS2W)
NPAUXCAPS2W = POINTER(tagAUXCAPS2W)
LPAUXCAPS2W = POINTER(tagAUXCAPS2W)


# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# type of device
# padding
# functionality supported by driver
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry
AUXCAPS2 = AUXCAPS2W
PAUXCAPS2 = PAUXCAPS2W
NPAUXCAPS2 = NPAUXCAPS2W
LPAUXCAPS2 = LPAUXCAPS2W
# UNICODE

# manufacturer ID
# product ID
# version of the driver
# product name (NULL terminated string)
# type of device
# functionality supported by driver
# flags for wTechnology field in AUXCAPS structure
# audio from INTernal CD-ROM drive
# audio from auxiliary input jacks
AUXCAPS_CDAUDIO = 0x1
AUXCAPS_AUXIN = 0x2
# flags for dwSupport field in AUXCAPS structure
# supports volume control
# separate left-right volume control
AUXCAPS_VOLUME = 0x0001
AUXCAPS_LRVOLUME = 0x0002
# auxiliary audio function prototypes
# WINMMAPI
# UINT
# WINAPI
# auxGetNumDevs(
#     VOID
#     );
auxGetNumDevs = winmm.auxGetNumDevs
auxGetNumDevs.restype = UINT

# WINMMAPI
# MMRESULT
# WINAPI
# auxGetDevCapsA(
#     _In_ UINT_PTR uDeviceID,
#     _Out_writes_bytes_(cbac) LPAUXCAPSA pac,
#     _In_ UINT cbac
#     );
auxGetDevCapsA = winmm.auxGetDevCapsA
auxGetDevCapsA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# auxGetDevCapsW(
#     _In_ UINT_PTR uDeviceID,
#     _Out_writes_bytes_(cbac) LPAUXCAPSW pac,
#     _In_ UINT cbac
#     );
auxGetDevCapsW = winmm.auxGetDevCapsW
auxGetDevCapsW.restype = MMRESULT

auxGetDevCaps = auxGetDevCapsW
# !UNICODE
# auxGetDevCaps = auxGetDevCapsA
# WINMMAPI
# MMRESULT
# WINAPI
# auxSetVolume(
#     _In_ UINT uDeviceID,
#     _In_ DWORD dwVolume
#     );
auxSetVolume = winmm.auxSetVolume
auxSetVolume.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# auxGetVolume(
#     _In_ UINT uDeviceID,
#     _Out_ LPDWORD pdwVolume
#     );
auxGetVolume = winmm.auxGetVolume
auxGetVolume.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# auxOutMessage(
#     _In_ UINT uDeviceID,
#     _In_ UINT uMsg,
#     _In_opt_ DWORD_PTR dw1,
#     _In_opt_ DWORD_PTR dw2
#     );
auxOutMessage = winmm.auxOutMessage
auxOutMessage.restype = MMRESULT

# ifdef WINVER >= 0x030a
# ifndef MMNOAUX
# ***************************************************************************
# Mixer Support
# ***************************************************************************
LPHMIXEROBJ = POINTER(FAR)
LPHMIXER = POINTER(FAR)
MIXER_SHORT_NAME_CHARS = 0x10
MIXER_LONG_NAME_CHARS = 0x40

# MMRESULT error return values specific to the mixer API


MIXERR_INVALLINE = MIXERR_BASE + 0
MIXERR_INVALCONTROL = MIXERR_BASE + 1
MIXERR_INVALVALUE = MIXERR_BASE + 2
MIXERR_LASTERROR = MIXERR_BASE + 2
MIXER_OBJECTF_HANDLE = 0x80000000
MIXER_OBJECTF_MIXER = 0x00000000
MIXER_OBJECTF_HMIXER = MIXER_OBJECTF_HANDLE | MIXER_OBJECTF_MIXER
MIXER_OBJECTF_WAVEOUT = 0x10000000
MIXER_OBJECTF_HWAVEOUT = MIXER_OBJECTF_HANDLE | MIXER_OBJECTF_WAVEOUT
MIXER_OBJECTF_WAVEIN = 0x20000000
MIXER_OBJECTF_HWAVEIN = MIXER_OBJECTF_HANDLE | MIXER_OBJECTF_WAVEIN
MIXER_OBJECTF_MIDIOUT = 0x30000000
MIXER_OBJECTF_HMIDIOUT = MIXER_OBJECTF_HANDLE | MIXER_OBJECTF_MIDIOUT
MIXER_OBJECTF_MIDIIN = 0x40000000
MIXER_OBJECTF_HMIDIIN = MIXER_OBJECTF_HANDLE | MIXER_OBJECTF_MIDIIN
MIXER_OBJECTF_AUX = 0x50000000
# WINMMAPI
# UINT
# WINAPI
# mixerGetNumDevs(
#     VOID
#     );
mixerGetNumDevs = winmm.mixerGetNumDevs
mixerGetNumDevs.restype = UINT


class tagMIXERCAPSA(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('fdwSupport', DWORD),
        ('cDestinations', DWORD),
    ]


MIXERCAPSA = tagMIXERCAPSA
PMIXERCAPSA = POINTER(tagMIXERCAPSA)
LPMIXERCAPSA = POINTER(tagMIXERCAPSA)


# manufacturer id
# product id
# version of the driver
# product name
# misc. support bits
# count of destinations

class tagMIXERCAPSW(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('fdwSupport', DWORD),
        ('cDestinations', DWORD),
    ]


MIXERCAPSW = tagMIXERCAPSW
PMIXERCAPSW = POINTER(tagMIXERCAPSW)
LPMIXERCAPSW = POINTER(tagMIXERCAPSW)


# manufacturer id
# product id
# version of the driver
# product name
# misc. support bits
# count of destinations
MIXERCAPS = MIXERCAPSW
PMIXERCAPS = PMIXERCAPSW
LPMIXERCAPS = LPMIXERCAPSW
# UNICODE


class tagMIXERCAPS2A(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', CHAR * MAXPNAMELEN),
        ('fdwSupport', DWORD),
        ('cDestinations', DWORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


MIXERCAPS2A = tagMIXERCAPS2A
PMIXERCAPS2A = POINTER(tagMIXERCAPS2A)
LPMIXERCAPS2A = POINTER(tagMIXERCAPS2A)


# manufacturer id
# product id
# version of the driver
# product name
# misc. support bits
# count of destinations
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry

class tagMIXERCAPS2W(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('vDriverVersion', MMVERSION),
        ('szPname', WCHAR * MAXPNAMELEN),
        ('fdwSupport', DWORD),
        ('cDestinations', DWORD),
        ('ManufacturerGuid', GUID),
        ('ProductGuid', GUID),
        ('NameGuid', GUID),
    ]


MIXERCAPS2W = tagMIXERCAPS2W
PMIXERCAPS2W = POINTER(tagMIXERCAPS2W)
LPMIXERCAPS2W = POINTER(tagMIXERCAPS2W)


# manufacturer id
# product id
# version of the driver
# product name
# misc. support bits
# count of destinations
# for extensible MID mapping
# for extensible PID mapping
# for name lookup in registry
MIXERCAPS2 = MIXERCAPS2W
PMIXERCAPS2 = PMIXERCAPS2W
LPMIXERCAPS2 = LPMIXERCAPS2W
# UNICODE

# manufacturer id
# product id
# version of the driver
# product name
# misc. support bits
# count of destinations
# WINMMAPI
# MMRESULT
# WINAPI
# mixerGetDevCapsA(
#     _In_ UINT_PTR uMxId,
#     _Out_writes_bytes_(cbmxcaps) LPMIXERCAPSA pmxcaps,
#     _In_ UINT cbmxcaps
#     );
mixerGetDevCapsA = winmm.mixerGetDevCapsA
mixerGetDevCapsA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# mixerGetDevCapsW(
#     _In_ UINT_PTR uMxId,
#     _Out_writes_bytes_(cbmxcaps) LPMIXERCAPSW pmxcaps,
#     _In_ UINT cbmxcaps
#     );
mixerGetDevCapsW = winmm.mixerGetDevCapsW
mixerGetDevCapsW.restype = MMRESULT

mixerGetDevCaps = mixerGetDevCapsW
# !UNICODE
# mixerGetDevCaps = mixerGetDevCapsA
# WINMMAPI
# MMRESULT
# WINAPI
# mixerOpen(
#     _Out_opt_ LPHMIXER phmx,
#     _In_ UINT uMxId,
#     _In_opt_ DWORD_PTR dwCallback,
#     _In_opt_ DWORD_PTR dwInstance,
#     _In_ DWORD fdwOpen
#     );
mixerOpen = winmm.mixerOpen
mixerOpen.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# mixerClose(
#     _In_ HMIXER hmx
#     );
mixerClose = winmm.mixerClose
mixerClose.restype = MMRESULT

# WINMMAPI
# DWORD
# WINAPI
# mixerMessage(
#     _In_opt_ HMIXER hmx,
#     _In_ UINT uMsg,
#     _In_opt_ DWORD_PTR dwParam1,
#     _In_opt_ DWORD_PTR dwParam2
#     );
mixerMessage = winmm.mixerMessage
mixerMessage.restype = DWORD


class tagMIXERLINEA(ctypes.Structure):

    class Target(ctypes.Structure):
        _fields_ = [
            ('dwType', DWORD),
            ('dwDeviceID', DWORD),
            ('wMid', WORD),
            ('wPid', WORD),
            ('vDriverVersion', MMVERSION),
            ('szPname', CHAR * MAXPNAMELEN),
        ]

    _fields_ = [
        ('cbStruct', DWORD),
        ('dwDestination', DWORD),
        ('dwSource', DWORD),
        ('dwLineID', DWORD),
        ('fdwLine', DWORD),
        ('dwUser', DWORD_PTR),
        ('dwComponentType', DWORD),
        ('cChannels', DWORD),
        ('cConnections', DWORD),
        ('cControls', DWORD),
        ('szShortName', CHAR * MIXER_SHORT_NAME_CHARS),
        ('szName', CHAR * MIXER_LONG_NAME_CHARS),
        ('Target', Target),
    ]


MIXERLINEA = tagMIXERLINEA
PMIXERLINEA = POINTER(tagMIXERLINEA)
LPMIXERLINEA = POINTER(tagMIXERLINEA)


# size of MIXERLINE structure
# zero based destination index
# zero based source index (if source)
# unique line id for mixer device
# state/information about line
# driver specific information
# component type line connects to
# number of channels line supports
# number of connections [possible]
# number of controls at this line
# MIXERLINE_TARGETTYPE_xxxx
# target device ID of device type
# of target device
# "
# "
# "

class tagMIXERLINEW(ctypes.Structure):

    class Target(ctypes.Structure):
        _fields_ = [
            ('dwType', DWORD),
            ('dwDeviceID', DWORD),
            ('wMid', WORD),
            ('wPid', WORD),
            ('vDriverVersion', MMVERSION),
            ('szPname', WCHAR * MAXPNAMELEN),
        ]

    _fields_ = [
        ('cbStruct', DWORD),
        ('dwDestination', DWORD),
        ('dwSource', DWORD),
        ('dwLineID', DWORD),
        ('fdwLine', DWORD),
        ('dwUser', DWORD_PTR),
        ('dwComponentType', DWORD),
        ('cChannels', DWORD),
        ('cConnections', DWORD),
        ('cControls', DWORD),
        ('szShortName', WCHAR * MIXER_SHORT_NAME_CHARS),
        ('szName', WCHAR * MIXER_LONG_NAME_CHARS),
        ('Target', Target),
    ]


MIXERLINEW = tagMIXERLINEW
PMIXERLINEW = POINTER(tagMIXERLINEW)
LPMIXERLINEW = POINTER(tagMIXERLINEW)


# size of MIXERLINE structure
# zero based destination index
# zero based source index (if source)
# unique line id for mixer device
# state/information about line
# driver specific information
# component type line connects to
# number of channels line supports
# number of connections [possible]
# number of controls at this line
# MIXERLINE_TARGETTYPE_xxxx
# target device ID of device type
# of target device
# "
# "
# "
MIXERLINE = MIXERLINEW
PMIXERLINE = PMIXERLINEW
LPMIXERLINE = LPMIXERLINEW
# UNICODE

# size of MIXERLINE structure
# zero based destination index
# zero based source index (if source)
# unique line id for mixer device
# state/information about line
# driver specific information
# component type line connects to
# number of channels line supports
# number of connections [possible]
# number of controls at this line
# MIXERLINE_TARGETTYPE_xxxx
# target device ID of device type
# of target device
# "
# "
# "

# MIXERLINE.fdwLine


MIXERLINE_LINEF_ACTIVE = 0x00000001
MIXERLINE_LINEF_DISCONNECTED = 0x00008000
MIXERLINE_LINEF_SOURCE = 0x80000000

# MIXERLINE.dwComponentType

# component types for destinations and sources


MIXERLINE_COMPONENTTYPE_DST_FIRST = 0x00000000
MIXERLINE_COMPONENTTYPE_DST_UNDEFINED = MIXERLINE_COMPONENTTYPE_DST_FIRST + 0
MIXERLINE_COMPONENTTYPE_DST_DIGITAL = MIXERLINE_COMPONENTTYPE_DST_FIRST + 1
MIXERLINE_COMPONENTTYPE_DST_LINE = MIXERLINE_COMPONENTTYPE_DST_FIRST + 2
MIXERLINE_COMPONENTTYPE_DST_MONITOR = MIXERLINE_COMPONENTTYPE_DST_FIRST + 3
MIXERLINE_COMPONENTTYPE_DST_SPEAKERS = MIXERLINE_COMPONENTTYPE_DST_FIRST + 4
MIXERLINE_COMPONENTTYPE_DST_HEADPHONES = MIXERLINE_COMPONENTTYPE_DST_FIRST + 5
MIXERLINE_COMPONENTTYPE_DST_TELEPHONE = MIXERLINE_COMPONENTTYPE_DST_FIRST + 6
MIXERLINE_COMPONENTTYPE_DST_WAVEIN = MIXERLINE_COMPONENTTYPE_DST_FIRST + 7
MIXERLINE_COMPONENTTYPE_DST_VOICEIN = MIXERLINE_COMPONENTTYPE_DST_FIRST + 8
MIXERLINE_COMPONENTTYPE_DST_LAST = MIXERLINE_COMPONENTTYPE_DST_FIRST + 8
MIXERLINE_COMPONENTTYPE_SRC_FIRST = 0x00001000
MIXERLINE_COMPONENTTYPE_SRC_UNDEFINED = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 0
MIXERLINE_COMPONENTTYPE_SRC_DIGITAL = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 1
MIXERLINE_COMPONENTTYPE_SRC_LINE = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 2
MIXERLINE_COMPONENTTYPE_SRC_MICROPHONE = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 3
MIXERLINE_COMPONENTTYPE_SRC_SYNTHESIZER = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 4
MIXERLINE_COMPONENTTYPE_SRC_COMPACTDISC = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 5
MIXERLINE_COMPONENTTYPE_SRC_TELEPHONE = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 6
MIXERLINE_COMPONENTTYPE_SRC_PCSPEAKER = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 7
MIXERLINE_COMPONENTTYPE_SRC_WAVEOUT = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 8
MIXERLINE_COMPONENTTYPE_SRC_AUXILIARY = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 9
MIXERLINE_COMPONENTTYPE_SRC_ANALOG = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 10
MIXERLINE_COMPONENTTYPE_SRC_LAST = MIXERLINE_COMPONENTTYPE_SRC_FIRST + 10

# MIXERLINE.Target.dwType


MIXERLINE_TARGETTYPE_UNDEFINED = 0x0
MIXERLINE_TARGETTYPE_WAVEOUT = 0x1
MIXERLINE_TARGETTYPE_WAVEIN = 0x2
MIXERLINE_TARGETTYPE_MIDIOUT = 0x3
MIXERLINE_TARGETTYPE_MIDIIN = 0x4
MIXERLINE_TARGETTYPE_AUX = 0x5
# WINMMAPI
# MMRESULT
# WINAPI
# mixerGetLineInfoA(
#     _In_opt_ HMIXEROBJ hmxobj,
#     _Inout_ LPMIXERLINEA pmxl,
#     _In_ DWORD fdwInfo
#     );
mixerGetLineInfoA = winmm.mixerGetLineInfoA
mixerGetLineInfoA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# mixerGetLineInfoW(
#     _In_opt_ HMIXEROBJ hmxobj,
#     _Inout_ LPMIXERLINEW pmxl,
#     _In_ DWORD fdwInfo
#     );
mixerGetLineInfoW = winmm.mixerGetLineInfoW
mixerGetLineInfoW.restype = MMRESULT

mixerGetLineInfo = mixerGetLineInfoW
# !UNICODE
# mixerGetLineInfo = mixerGetLineInfoA
MIXER_GETLINEINFOF_DESTINATION = 0x00000000
MIXER_GETLINEINFOF_SOURCE = 0x00000001
MIXER_GETLINEINFOF_LINEID = 0x00000002
MIXER_GETLINEINFOF_COMPONENTTYPE = 0x00000003
MIXER_GETLINEINFOF_TARGETTYPE = 0x00000004
MIXER_GETLINEINFOF_QUERYMASK = 0x0000000F
# WINMMAPI
# MMRESULT
# WINAPI
# mixerGetID(
#     _In_opt_ HMIXEROBJ hmxobj,
#     _Out_ UINT  FAR * puMxId,
#     _In_ DWORD fdwId
#     );
mixerGetID = winmm.mixerGetID
mixerGetID.restype = MMRESULT


# MIXERCONTROL


class tagMIXERCONTROLA(ctypes.Structure):

    class Bounds(ctypes.Union):

        class DUMMYSTRUCTNAME(ctypes.Structure):
            _fields_ = [
                ('lMinimum', LONG),
                ('lMaximum', LONG),
            ]

        class DUMMYSTRUCTNAME2(ctypes.Structure):
            _fields_ = [
                ('dwMinimum', DWORD),
                ('dwMaximum', DWORD),
            ]

        _fields_ = [
            ('DUMMYSTRUCTNAME', DUMMYSTRUCTNAME),
            ('DUMMYSTRUCTNAME2', DUMMYSTRUCTNAME2),
            ('dwReserved', DWORD * 6),
        ]

    class Metrics(ctypes.Union):
        _fields_ = [
            ('cSteps', DWORD),
            ('cbCustomData', DWORD),
            ('dwReserved', DWORD * 6),
        ]

    _fields_ = [
        ('cbStruct', DWORD),
        ('dwControlID', DWORD),
        ('dwControlType', DWORD),
        ('fdwControl', DWORD),
        ('cMultipleItems', DWORD),
        ('szShortName', CHAR * MIXER_SHORT_NAME_CHARS),
        ('szName', CHAR * MIXER_LONG_NAME_CHARS),
        ('Bounds', Bounds),
        ('Metrics', Metrics),
    ]


MIXERCONTROLA = tagMIXERCONTROLA
PMIXERCONTROLA = POINTER(tagMIXERCONTROLA)
LPMIXERCONTROLA = POINTER(tagMIXERCONTROLA)


# size in bytes of MIXERCONTROL
# unique control id for mixer device
# MIXERCONTROL_CONTROLTYPE_xxx
# MIXERCONTROL_CONTROLF_xxx
# if MIXERCONTROL_CONTROLF_MULTIPLE set
# INT minimum for this control
# INT maximum for this control
# UINT minimum for this control
# UINT maximum for this control
# # of steps between min & max
# size in bytes of custom data
# !!! needed? we have cbStruct....

class tagMIXERCONTROLW(ctypes.Structure):

    class Bounds(ctypes.Union):

        class DUMMYSTRUCTNAME(ctypes.Structure):
            _fields_ = [
                ('lMinimum', LONG),
                ('lMaximum', LONG),
            ]

        class DUMMYSTRUCTNAME2(ctypes.Structure):
            _fields_ = [
                ('dwMinimum', DWORD),
                ('dwMaximum', DWORD),
            ]

        _fields_ = [
            ('DUMMYSTRUCTNAME', DUMMYSTRUCTNAME),
            ('DUMMYSTRUCTNAME2', DUMMYSTRUCTNAME2),
            ('dwReserved', DWORD * 6),
        ]

    class Metrics(ctypes.Union):
        _fields_ = [
            ('cSteps', DWORD),
            ('cbCustomData', DWORD),
            ('dwReserved', DWORD * 6),
        ]

    _fields_ = [
        ('cbStruct', DWORD),
        ('dwControlID', DWORD),
        ('dwControlType', DWORD),
        ('fdwControl', DWORD),
        ('cMultipleItems', DWORD),
        ('szShortName', WCHAR * MIXER_SHORT_NAME_CHARS),
        ('szName', WCHAR * MIXER_LONG_NAME_CHARS),
        ('Bounds', Bounds),
        ('Metrics', Metrics),
    ]


MIXERCONTROLW = tagMIXERCONTROLW
PMIXERCONTROLW = POINTER(tagMIXERCONTROLW)
LPMIXERCONTROLW = POINTER(tagMIXERCONTROLW)


# size in bytes of MIXERCONTROL
# unique control id for mixer device
# MIXERCONTROL_CONTROLTYPE_xxx
# MIXERCONTROL_CONTROLF_xxx
# if MIXERCONTROL_CONTROLF_MULTIPLE set
# INT minimum for this control
# INT maximum for this control
# UINT minimum for this control
# UINT maximum for this control
# # of steps between min & max
# size in bytes of custom data
# !!! needed? we have cbStruct....
MIXERCONTROL = MIXERCONTROLW
PMIXERCONTROL = PMIXERCONTROLW
LPMIXERCONTROL = LPMIXERCONTROLW
# UNICODE

# size in bytes of MIXERCONTROL
# unique control id for mixer device
# MIXERCONTROL_CONTROLTYPE_xxx
# MIXERCONTROL_CONTROLF_xxx
# if MIXERCONTROL_CONTROLF_MULTIPLE set
# INT minimum for this control
# INT maximum for this control
# UINT minimum for this control
# UINT maximum for this control
# # of steps between min & max
# size in bytes of custom data
# !!! needed? we have cbStruct....

# MIXERCONTROL.fdwControl


MIXERCONTROL_CONTROLF_UNIFORM = 0x00000001
MIXERCONTROL_CONTROLF_MULTIPLE = 0x00000002
MIXERCONTROL_CONTROLF_DISABLED = 0x80000000

# MIXERCONTROL_CONTROLTYPE_xxx building block defines


MIXERCONTROL_CT_CLASS_MASK = 0xF0000000
MIXERCONTROL_CT_CLASS_CUSTOM = 0x00000000
MIXERCONTROL_CT_CLASS_METER = 0x10000000
MIXERCONTROL_CT_CLASS_SWITCH = 0x20000000
MIXERCONTROL_CT_CLASS_NUMBER = 0x30000000
MIXERCONTROL_CT_CLASS_SLIDER = 0x40000000
MIXERCONTROL_CT_CLASS_FADER = 0x50000000
MIXERCONTROL_CT_CLASS_TIME = 0x60000000
MIXERCONTROL_CT_CLASS_LIST = 0x70000000
MIXERCONTROL_CT_SUBCLASS_MASK = 0x0F000000
MIXERCONTROL_CT_SC_SWITCH_BOOLEAN = 0x00000000
MIXERCONTROL_CT_SC_SWITCH_BUTTON = 0x01000000
MIXERCONTROL_CT_SC_METER_POLLED = 0x00000000
MIXERCONTROL_CT_SC_TIME_MICROSECS = 0x00000000
MIXERCONTROL_CT_SC_TIME_MILLISECS = 0x01000000
MIXERCONTROL_CT_SC_LIST_SINGLE = 0x00000000
MIXERCONTROL_CT_SC_LIST_MULTIPLE = 0x01000000
MIXERCONTROL_CT_UNITS_MASK = 0x00FF0000
MIXERCONTROL_CT_UNITS_CUSTOM = 0x00000000
MIXERCONTROL_CT_UNITS_BOOLEAN = 0x00010000
MIXERCONTROL_CT_UNITS_SIGNED = 0x00020000
# in 10ths
MIXERCONTROL_CT_UNITS_UNSIGNED = 0x00030000
# in 10ths
MIXERCONTROL_CT_UNITS_DECIBELS = 0x00040000
MIXERCONTROL_CT_UNITS_PERCENT = 0x00050000

# Commonly used control types for specifying MIXERCONTROL.dwControlType

MIXERCONTROL_CONTROLTYPE_CUSTOM = (
    MIXERCONTROL_CT_CLASS_CUSTOM |
    MIXERCONTROL_CT_UNITS_CUSTOM
)
MIXERCONTROL_CONTROLTYPE_BOOLEANMETER = (
    MIXERCONTROL_CT_CLASS_METER |
    MIXERCONTROL_CT_SC_METER_POLLED |
    MIXERCONTROL_CT_UNITS_BOOLEAN
)
MIXERCONTROL_CONTROLTYPE_SIGNEDMETER = (
    MIXERCONTROL_CT_CLASS_METER |
    MIXERCONTROL_CT_SC_METER_POLLED |
    MIXERCONTROL_CT_UNITS_SIGNED
)
MIXERCONTROL_CONTROLTYPE_PEAKMETER = MIXERCONTROL_CONTROLTYPE_SIGNEDMETER + 1
MIXERCONTROL_CONTROLTYPE_UNSIGNEDMETER = (
    MIXERCONTROL_CT_CLASS_METER |
    MIXERCONTROL_CT_SC_METER_POLLED |
    MIXERCONTROL_CT_UNITS_UNSIGNED
)
MIXERCONTROL_CONTROLTYPE_BOOLEAN = (
    MIXERCONTROL_CT_CLASS_SWITCH |
    MIXERCONTROL_CT_SC_SWITCH_BOOLEAN |
    MIXERCONTROL_CT_UNITS_BOOLEAN
)
MIXERCONTROL_CONTROLTYPE_ONOFF = MIXERCONTROL_CONTROLTYPE_BOOLEAN + 1
MIXERCONTROL_CONTROLTYPE_MUTE = MIXERCONTROL_CONTROLTYPE_BOOLEAN + 2
MIXERCONTROL_CONTROLTYPE_MONO = MIXERCONTROL_CONTROLTYPE_BOOLEAN + 3
MIXERCONTROL_CONTROLTYPE_LOUDNESS = MIXERCONTROL_CONTROLTYPE_BOOLEAN + 4
MIXERCONTROL_CONTROLTYPE_STEREOENH = MIXERCONTROL_CONTROLTYPE_BOOLEAN + 5
MIXERCONTROL_CONTROLTYPE_BASS_BOOST = (
    MIXERCONTROL_CONTROLTYPE_BOOLEAN + 0x00002277
)
MIXERCONTROL_CONTROLTYPE_BUTTON = (
    MIXERCONTROL_CT_CLASS_SWITCH |
    MIXERCONTROL_CT_SC_SWITCH_BUTTON |
    MIXERCONTROL_CT_UNITS_BOOLEAN
)
MIXERCONTROL_CONTROLTYPE_DECIBELS = (
    MIXERCONTROL_CT_CLASS_NUMBER |
    MIXERCONTROL_CT_UNITS_DECIBELS
)
MIXERCONTROL_CONTROLTYPE_SIGNED = (
    MIXERCONTROL_CT_CLASS_NUMBER |
    MIXERCONTROL_CT_UNITS_SIGNED
)
MIXERCONTROL_CONTROLTYPE_UNSIGNED = (
    MIXERCONTROL_CT_CLASS_NUMBER |
    MIXERCONTROL_CT_UNITS_UNSIGNED
)
MIXERCONTROL_CONTROLTYPE_PERCENT = (
    MIXERCONTROL_CT_CLASS_NUMBER |
    MIXERCONTROL_CT_UNITS_PERCENT
)
MIXERCONTROL_CONTROLTYPE_SLIDER = (
    MIXERCONTROL_CT_CLASS_SLIDER |
    MIXERCONTROL_CT_UNITS_SIGNED
)
MIXERCONTROL_CONTROLTYPE_PAN = MIXERCONTROL_CONTROLTYPE_SLIDER + 1
MIXERCONTROL_CONTROLTYPE_QSOUNDPAN = MIXERCONTROL_CONTROLTYPE_SLIDER + 2
MIXERCONTROL_CONTROLTYPE_FADER = (
    MIXERCONTROL_CT_CLASS_FADER |
    MIXERCONTROL_CT_UNITS_UNSIGNED
)
MIXERCONTROL_CONTROLTYPE_VOLUME = MIXERCONTROL_CONTROLTYPE_FADER + 1
MIXERCONTROL_CONTROLTYPE_BASS = MIXERCONTROL_CONTROLTYPE_FADER + 2
MIXERCONTROL_CONTROLTYPE_TREBLE = MIXERCONTROL_CONTROLTYPE_FADER + 3
MIXERCONTROL_CONTROLTYPE_EQUALIZER = MIXERCONTROL_CONTROLTYPE_FADER + 4
MIXERCONTROL_CONTROLTYPE_SINGLESELECT = (
    MIXERCONTROL_CT_CLASS_LIST |
    MIXERCONTROL_CT_SC_LIST_SINGLE |
    MIXERCONTROL_CT_UNITS_BOOLEAN
)
MIXERCONTROL_CONTROLTYPE_MUX = MIXERCONTROL_CONTROLTYPE_SINGLESELECT + 1
MIXERCONTROL_CONTROLTYPE_MULTIPLESELECT = (
    MIXERCONTROL_CT_CLASS_LIST |
    MIXERCONTROL_CT_SC_LIST_MULTIPLE |
    MIXERCONTROL_CT_UNITS_BOOLEAN
)
MIXERCONTROL_CONTROLTYPE_MIXER = MIXERCONTROL_CONTROLTYPE_MULTIPLESELECT + 1
MIXERCONTROL_CONTROLTYPE_MICROTIME = (
    MIXERCONTROL_CT_CLASS_TIME |
    MIXERCONTROL_CT_SC_TIME_MICROSECS |
    MIXERCONTROL_CT_UNITS_UNSIGNED
)
MIXERCONTROL_CONTROLTYPE_MILLITIME = (
    MIXERCONTROL_CT_CLASS_TIME |
    MIXERCONTROL_CT_SC_TIME_MILLISECS |
    MIXERCONTROL_CT_UNITS_UNSIGNED
)

# MIXERLINECONTROLS


class tagMIXERLINECONTROLSA(ctypes.Structure):

    class DUMMYUNIONNAME(ctypes.Union):
        _fields_ = [
            ('dwControlID', DWORD),
            ('dwControlType', DWORD),
        ]

    _fields_ = [
        ('cbStruct', DWORD),
        ('dwLineID', DWORD),
        ('DUMMYUNIONNAME', DUMMYUNIONNAME),
        ('cControls', DWORD),
        ('cbmxctrl', DWORD),
        ('pamxctrl', LPMIXERCONTROLA),
    ]


MIXERLINECONTROLSA = tagMIXERLINECONTROLSA
PMIXERLINECONTROLSA = POINTER(tagMIXERLINECONTROLSA)
LPMIXERLINECONTROLSA = POINTER(tagMIXERLINECONTROLSA)


# size in bytes of MIXERLINECONTROLS
# line id (from MIXERLINE.dwLineID)
# MIXER_GETLINECONTROLSF_ONEBYID
# MIXER_GETLINECONTROLSF_ONEBYTYPE
# count of controls pmxctrl poINTs to
# size in bytes of _one_ MIXERCONTROL
# poINTer to first MIXERCONTROL array

class tagMIXERLINECONTROLSW(ctypes.Structure):

    class DUMMYUNIONNAME(ctypes.Union):
        _fields_ = [
            ('dwControlID', DWORD),
            ('dwControlType', DWORD),
        ]

    _fields_ = [
        ('cbStruct', DWORD),
        ('dwLineID', DWORD),
        ('DUMMYUNIONNAME', DUMMYUNIONNAME),
        ('cControls', DWORD),
        ('cbmxctrl', DWORD),
        ('pamxctrl', LPMIXERCONTROLW),
    ]


MIXERLINECONTROLSW = tagMIXERLINECONTROLSW
PMIXERLINECONTROLSW = POINTER(tagMIXERLINECONTROLSW)
LPMIXERLINECONTROLSW = POINTER(tagMIXERLINECONTROLSW)


# size in bytes of MIXERLINECONTROLS
# line id (from MIXERLINE.dwLineID)
# MIXER_GETLINECONTROLSF_ONEBYID
# MIXER_GETLINECONTROLSF_ONEBYTYPE
# count of controls pmxctrl poINTs to
# size in bytes of _one_ MIXERCONTROL
# poINTer to first MIXERCONTROL array
MIXERLINECONTROLS = MIXERLINECONTROLSW
PMIXERLINECONTROLS = PMIXERLINECONTROLSW
LPMIXERLINECONTROLS = LPMIXERLINECONTROLSW
# UNICODE

# size in bytes of MIXERLINECONTROLS
# line id (from MIXERLINE.dwLineID)
# MIXER_GETLINECONTROLSF_ONEBYID
# MIXER_GETLINECONTROLSF_ONEBYTYPE
# count of controls pmxctrl poINTs to
# size in bytes of _one_ MIXERCONTROL
# poINTer to first MIXERCONTROL array



# WINMMAPI
# MMRESULT
# WINAPI
# mixerGetLineControlsA(
#     _In_opt_ HMIXEROBJ hmxobj,
#     _Inout_ LPMIXERLINECONTROLSA pmxlc,
#     _In_ DWORD fdwControls
#     );
mixerGetLineControlsA = winmm.mixerGetLineControlsA
mixerGetLineControlsA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# mixerGetLineControlsW(
#     _In_opt_ HMIXEROBJ hmxobj,
#     _Inout_ LPMIXERLINECONTROLSW pmxlc,
#     _In_ DWORD fdwControls
#     );
mixerGetLineControlsW = winmm.mixerGetLineControlsW
mixerGetLineControlsW.restype = MMRESULT

mixerGetLineControls = mixerGetLineControlsW
# !UNICODE
# mixerGetLineControls = mixerGetLineControlsA
MIXER_GETLINECONTROLSF_ALL = 0x00000000
MIXER_GETLINECONTROLSF_ONEBYID = 0x00000001
MIXER_GETLINECONTROLSF_ONEBYTYPE = 0x00000002
MIXER_GETLINECONTROLSF_QUERYMASK = 0x0000000F


class tMIXERCONTROLDETAILS(ctypes.Structure):

    class DUMMYUNIONNAME(ctypes.Union):
        _fields_ = [
            ('hwndOwner', HWND),
            ('cMultipleItems', DWORD),
        ]

    _fields_ = [
        ('cbStruct', DWORD),
        ('dwControlID', DWORD),
        ('cChannels', DWORD),
        ('DUMMYUNIONNAME', DUMMYUNIONNAME),
        ('cbDetails', DWORD),
        ('paDetails', LPVOID),
    ]


MIXERCONTROLDETAILS = tMIXERCONTROLDETAILS
PMIXERCONTROLDETAILS = POINTER(tMIXERCONTROLDETAILS)
LPMIXERCONTROLDETAILS = POINTER(tMIXERCONTROLDETAILS)


# size in bytes of MIXERCONTROLDETAILS
# control id to get/set details on
# number of channels in paDetails array
# for MIXER_SETCONTROLDETAILSF_CUSTOM
# if _MULTIPLE, the number of items per channel
# size of _one_ details_XX struct
# poINTer to array of details_XX structs

# MIXER_GETCONTROLDETAILSF_LISTTEXT


class tagMIXERCONTROLDETAILS_LISTTEXTA(ctypes.Structure):
    _fields_ = [
        ('dwParam1', DWORD),
        ('dwParam2', DWORD),
        ('szName', CHAR * MIXER_LONG_NAME_CHARS),
    ]


MIXERCONTROLDETAILS_LISTTEXTA = tagMIXERCONTROLDETAILS_LISTTEXTA
PMIXERCONTROLDETAILS_LISTTEXTA = POINTER(tagMIXERCONTROLDETAILS_LISTTEXTA)
LPMIXERCONTROLDETAILS_LISTTEXTA = POINTER(tagMIXERCONTROLDETAILS_LISTTEXTA)


class tagMIXERCONTROLDETAILS_LISTTEXTW(ctypes.Structure):
    _fields_ = [
        ('dwParam1', DWORD),
        ('dwParam2', DWORD),
        ('szName', WCHAR * MIXER_LONG_NAME_CHARS),
    ]


MIXERCONTROLDETAILS_LISTTEXTW = tagMIXERCONTROLDETAILS_LISTTEXTW
PMIXERCONTROLDETAILS_LISTTEXTW = POINTER(tagMIXERCONTROLDETAILS_LISTTEXTW)
LPMIXERCONTROLDETAILS_LISTTEXTW = POINTER(tagMIXERCONTROLDETAILS_LISTTEXTW)


MIXERCONTROLDETAILS_LISTTEXT = MIXERCONTROLDETAILS_LISTTEXTW
PMIXERCONTROLDETAILS_LISTTEXT = PMIXERCONTROLDETAILS_LISTTEXTW
LPMIXERCONTROLDETAILS_LISTTEXT = LPMIXERCONTROLDETAILS_LISTTEXTW
# UNICODE

# MIXER_GETCONTROLDETAILSF_VALUE


class tMIXERCONTROLDETAILS_BOOLEAN(ctypes.Structure):
    _fields_ = [
        ('fValue', LONG),
    ]


MIXERCONTROLDETAILS_BOOLEAN = tMIXERCONTROLDETAILS_BOOLEAN
PMIXERCONTROLDETAILS_BOOLEAN = POINTER(tMIXERCONTROLDETAILS_BOOLEAN)
LPMIXERCONTROLDETAILS_BOOLEAN = POINTER(tMIXERCONTROLDETAILS_BOOLEAN)


class tMIXERCONTROLDETAILS_SIGNED(ctypes.Structure):
    _fields_ = [
        ('lValue', LONG),
    ]


MIXERCONTROLDETAILS_SIGNED = tMIXERCONTROLDETAILS_SIGNED
PMIXERCONTROLDETAILS_SIGNED = POINTER(tMIXERCONTROLDETAILS_SIGNED)
LPMIXERCONTROLDETAILS_SIGNED = POINTER(tMIXERCONTROLDETAILS_SIGNED)


class tMIXERCONTROLDETAILS_UNSIGNED(ctypes.Structure):
    _fields_ = [
        ('dwValue', DWORD),
    ]


MIXERCONTROLDETAILS_UNSIGNED = tMIXERCONTROLDETAILS_UNSIGNED
PMIXERCONTROLDETAILS_UNSIGNED = POINTER(tMIXERCONTROLDETAILS_UNSIGNED)
LPMIXERCONTROLDETAILS_UNSIGNED = POINTER(tMIXERCONTROLDETAILS_UNSIGNED)


# WINMMAPI
# MMRESULT
# WINAPI
# mixerGetControlDetailsA(
#     _In_opt_ HMIXEROBJ hmxobj,
#     _Inout_ LPMIXERCONTROLDETAILS pmxcd,
#     _In_ DWORD fdwDetails
#     );
mixerGetControlDetailsA = winmm.mixerGetControlDetailsA
mixerGetControlDetailsA.restype = MMRESULT

# WINMMAPI
# MMRESULT
# WINAPI
# mixerGetControlDetailsW(
#     _In_opt_ HMIXEROBJ hmxobj,
#     _Inout_ LPMIXERCONTROLDETAILS pmxcd,
#     _In_ DWORD fdwDetails
#     );
mixerGetControlDetailsW = winmm.mixerGetControlDetailsW
mixerGetControlDetailsW.restype = MMRESULT

mixerGetControlDetails = mixerGetControlDetailsW
# !UNICODE
# mixerGetControlDetails = mixerGetControlDetailsA
MIXER_GETCONTROLDETAILSF_VALUE = 0x00000000
MIXER_GETCONTROLDETAILSF_LISTTEXT = 0x00000001
MIXER_GETCONTROLDETAILSF_QUERYMASK = 0x0000000F
# WINMMAPI
# MMRESULT
# WINAPI
# mixerSetControlDetails(
#     _In_opt_ HMIXEROBJ hmxobj,
#     _In_ LPMIXERCONTROLDETAILS pmxcd,
#     _In_ DWORD fdwDetails
#     );
mixerSetControlDetails = winmm.mixerSetControlDetails
mixerSetControlDetails.restype = MMRESULT

MIXER_SETCONTROLDETAILSF_VALUE = 0x00000000
MIXER_SETCONTROLDETAILSF_CUSTOM = 0x00000001
MIXER_SETCONTROLDETAILSF_QUERYMASK = 0x0000000F
# ifndef MMNOMIXER
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# _MMEAPI_H_

__all__ = (
    'WAVE_FORMAT_48S16', 'MIDIERR_NOMAP', 'MIXERCONTROLDETAILS_LISTTEXT',
    'MIXERCONTROL_CT_SUBCLASS_MASK', 'LPMIDIINCAPS2', 'WAVE_FORMAT_96M08',
    'waveOutGetErrorText', 'MIXERCONTROL_CONTROLTYPE_ONOFF', 'MIDIINCAPS2',
    'MIDIERR_NODEVICE', 'mixerGetControlDetails', 'WAVERR_BADFORMAT',
    'MIXERLINE_COMPONENTTYPE_DST_UNDEFINED', 'WAVE_MAPPER', 'WAVE_FORMAT_4S16',
    'WAVE_FORMAT_1S16', 'AUXCAPS2', 'MIXERLINE_COMPONENTTYPE_SRC_LINE',
    'WAVE_FORMAT_1M08', 'mixerGetLineInfo', 'AUXCAPS_LRVOLUME', 'WAVEOUTCAPS',
    'MIXER_LONG_NAME_CHARS', 'WAVE_FORMAT_2S08', 'WAVECAPS_LRVOLUME',
    'WAVE_MAPPED', 'MIXERCONTROL_CONTROLTYPE_VOLUME', 'MEVT_F_SHORT',
    'PMIXERCAPS2', 'LPAUXCAPS2', 'MIDIINCAPS', 'tagMIDIINCAPSA',
    'MIDIERR_STILLPLAYING', 'WAVE_FORMAT_DIRECT_QUERY', 'LPMIXERLINECONTROLS',
    'MIXERLINE_COMPONENTTYPE_SRC_DIGITAL', 'tagMIDIINCAPSW', 'LPWAVEINCAPS2',
    'MIXERLINE_LINEF_ACTIVE', 'MOD_MIDIPORT', 'LPWAVEOUTCAPS2', 'MHDR_INQUEUE',
    'tagMIDIINCAPS2A', 'MIXER_GETCONTROLDETAILSF_QUERYMASK', 'MIDI_UNCACHE',
    'MIDIPROP_TIMEDIV', 'MIXERLINE_COMPONENTTYPE_DST_LAST', 'MEVT_EVENTPARM',
    'NPMIDIINCAPS', 'WAVERR_SYNC', 'MIXERCONTROL_CONTROLTYPE_UNSIGNEDMETER',
    'MIXERLINE_COMPONENTTYPE_SRC_AUXILIARY', 'tagWAVEOUTCAPSW', 'WIM_OPEN',
    'MIXERCONTROL_CONTROLTYPE_MONO', 'WAVE_FORMAT_2M08', 'MIDIPROP_SET',
    'MIXERCONTROL_CT_UNITS_CUSTOM', 'MIXERCONTROL_CONTROLTYPE_BASS',
    'MIXERCONTROL_CT_SC_METER_POLLED', 'MIXERCONTROL_CONTROLTYPE_CUSTOM',
    'MIXER_SETCONTROLDETAILSF_VALUE', 'MIXERLINE_COMPONENTTYPE_SRC_TELEPHONE',
    'MIXERCONTROL_CT_SC_SWITCH_BOOLEAN', 'tMIXERCONTROLDETAILS_BOOLEAN',
    'WAVECAPS_VOLUME', 'WAVE_FORMAT_44M08', 'LPMIDIINCAPS', 'WAVECAPS_SYNC',
    'PAUXCAPS', 'tagMIDIINCAPS2W', 'MHDR_ISSTRM', 'LPMIDIOUTCAPS',
    'WAVECALLBACK', 'tWAVEFORMATEX', 'MIDICALLBACK', 'WAVE_FORMAT_48M16',
    'MIXERLINE_COMPONENTTYPE_SRC_ANALOG', 'NPMIDIINCAPS2', 'waveOutGetDevCaps',
    'MIXERLINE_COMPONENTTYPE_SRC_SYNTHESIZER', 'LPMIXERCONTROL',
    'MIXERLINE_COMPONENTTYPE_DST_FIRST', 'MIM_CLOSE', 'MIXER_OBJECTF_HWAVEIN',
    'MIDIERR_BADOPENMODE', 'MIXERCONTROL_CONTROLTYPE_TREBLE', 'MOM_CLOSE',
    'MIXERCONTROL_CONTROLTYPE_SINGLESELECT', 'WAVE_ALLOWSYNC',
    'MIXERCONTROL_CT_CLASS_MASK', 'MIXERCONTROL_CT_CLASS_NUMBER', 'MHDR_DONE',
    'LPMIXERLINE', 'MIXERCONTROL_CT_UNITS_UNSIGNED', 'MIDISTRM_ERROR',
    'MIXERCONTROL_CONTROLTYPE_BOOLEANMETER', 'WAVE_FORMAT_1S08',
    'MIXERCONTROL_CONTROLTYPE_MICROTIME', 'MEVT_TEMPO', 'MEVT_F_LONG',
    'MIDI_CACHE_ALL',  'WAVE_FORMAT_2M16', 'MIXER_GETLINEINFOF_QUERYMASK',
    'MIXERLINE_COMPONENTTYPE_DST_WAVEIN', 'MIXERCONTROL_CT_SC_LIST_MULTIPLE',
    'MIXER_OBJECTF_HWAVEOUT', 'MIXERLINE_COMPONENTTYPE_SRC_UNDEFINED',
    'MIDIMAPPER', 'MEVT_LONGMSG', 'PWAVEINCAPS2', 'MIXERR_LASTERROR',
    'MIXERCONTROL_CT_CLASS_TIME', 'MOM_DONE', 'tagWAVEINCAPSA',
    'MIXER_GETLINEINFOF_DESTINATION', 'MIXER_GETLINEINFOF_TARGETTYPE',
    'MIXERCONTROL_CONTROLTYPE_BOOLEAN', 'MIXER_GETLINECONTROLSF_ONEBYTYPE',
    'PWAVEOUTCAPS2', 'LPKEYARRAY', 'MIXERCONTROL_CT_CLASS_SWITCH',
    'LPPATCHARRAY', 'WIM_CLOSE', 'midistrmbuffver_tag', 'tagWAVEOUTCAPS2A',
    'MIXERLINE_LINEF_SOURCE', 'MIXERCONTROL_CONTROLF_MULTIPLE',
    'MIXERCONTROL_CONTROLTYPE_MIXER', 'MIDIPATCHSIZE', 'PMIXERLINE',
    'WHDR_INQUEUE', 'MIXERCONTROL_CT_UNITS_MASK', 'PMIDIOUTCAPS',
    'tagWAVEOUTCAPS2W', 'midiOutGetErrorText', 'MIXER_GETLINEINFOF_SOURCE',
    'MIDI_CACHE_BESTFIT', 'MOD_FMSYNTH', 'WAVE_FORMAT_44M16', 'MIM_ERROR',
    'MIXERLINE_TARGETTYPE_WAVEIN', 'tagMIXERCAPSA', 'MEVT_F_CALLBACK',
    'LPHMIXER', 'WAVE_FORMAT_1M16', 'WHDR_ENDLOOP', 'WOM_DONE', 'tagAUXCAPS2A',
    'WAVE_FORMAT_4M08', 'MIXER_GETCONTROLDETAILSF_VALUE', 'tagMIXERCAPSW',
    'LPHMIDIIN', 'KEYARRAY', 'MIXERR_INVALLINE', 'PMIXERLINECONTROLS',
    'MIDIERR_INVALIDSETUP', 'MIXER_OBJECTF_WAVEOUT', 'midiproptempo_tag',
    'MIXERLINE_COMPONENTTYPE_SRC_FIRST', 'MIXERLINECONTROLS', 'MIXERCAPS',
    'MIDICAPS_VOLUME', 'tagMIXERCONTROLA', 'LPHMIDISTRM', 'LPMIDIOUTCAPS2',
    'MIXERCONTROL_CT_UNITS_SIGNED', 'LPMIXERCONTROLDETAILS_LISTTEXT',
    'MIXERLINE_COMPONENTTYPE_SRC_MICROPHONE', 'AUX_MAPPER', 'AUXCAPS_VOLUME',
    'MIXER_OBJECTF_MIDIOUT', 'midievent_tag', 'tMIXERCONTROLDETAILS_UNSIGNED',
    'MIXER_SHORT_NAME_CHARS', 'MIDIERR_UNPREPARED', 'tagMIDIOUTCAPSA',
    'PMIXERCAPS', 'tMIXERCONTROLDETAILS', 'MIDI_CACHE_QUERY',
    'MIXERCONTROL_CT_CLASS_LIST', 'MIXER_GETLINECONTROLSF_ALL', 'NPWAVEINCAPS',
    'MIXERCONTROL_CONTROLTYPE_QSOUNDPAN', 'tagMIDIOUTCAPSW', 'MHDR_PREPARED',
    'MIXERLINE_TARGETTYPE_AUX', 'MIXERCONTROL_CONTROLTYPE_SIGNEDMETER',
    'midiOutGetDevCaps', 'MEVT_VERSION',
    'WAVE_FORMAT_44S08', 'MIXERCONTROL_CONTROLTYPE_MUTE', 'PWAVEOUTCAPS',
    'LPMIDICALLBACK', 'MIXERCONTROL_CONTROLTYPE_MILLITIME', 'WOM_CLOSE',
    'MOD_SQSYNTH', 'MIDICAPS_LRVOLUME', 'WAVERR_UNPREPARED',
    'MIXER_OBJECTF_AUX', 'MIDICAPS_STREAM', 'MIXER_OBJECTF_HMIDIIN',
    'waveInGetDevCaps', 'tagAUXCAPS2W', 'PMIXERCONTROLDETAILS_LISTTEXT',
    'MIXERLINE_COMPONENTTYPE_SRC_PCSPEAKER', 'WAVE_FORMAT_96S08', 'MIM_OPEN',
    'MIDIERR_DONT_CONTINUE', 'waveformat_tag', 'MIXERCONTROL_CT_CLASS_METER',
    'PWAVEINCAPS', 'tagWAVEINCAPS2W', 'WAVE_FORMAT_48S08',
    'midiInGetErrorText', 'PMIDIINCAPS', 'wavehdr_tag', 'NPWAVEOUTCAPS',
    'WAVE_FORMAT_96M16', 'tagWAVEINCAPS2A', 'MIDIOUTCAPS2',
    'MIXER_OBJECTF_HMIDIOUT', 'MIXERCONTROL_CT_CLASS_SLIDER',
    'MIXERCONTROL_CONTROLTYPE_BUTTON', 'WAVERR_LASTERROR',
    'MIXERLINE_COMPONENTTYPE_DST_TELEPHONE', 'WAVE_FORMAT_PCM',
    'MIXERCONTROL_CONTROLTYPE_PERCENT', 'tagMIXERLINECONTROLSW',
    'tagWAVEOUTCAPSA', 'LPMIXERCAPS', 'MIXERCONTROL_CONTROLF_UNIFORM',
    'MIXER_OBJECTF_MIDIIN', 'tagMIXERLINECONTROLSA', 'MIDI_MAPPER',
    'MEVT_EVENTTYPE', 'tagMIXERCONTROLW', 'LPWAVEOUTCAPS', 'tagMIXERLINEA',
    'LPHWAVEOUT', 'MIXERR_INVALCONTROL', 'tagMIXERLINEW',
    'MIXERCONTROL_CONTROLTYPE_MUX', 'mixerGetLineControls', 'MOD_SYNTH',
    'MEVT_SHORTMSG', 'tMIXERCONTROLDETAILS_SIGNED',
    'WAVE_FORMAT_4M16', 'WAVE_FORMAT_DIRECT',
    'MIXERLINE_COMPONENTTYPE_SRC_WAVEOUT', 'MIXERLINE_COMPONENTTYPE_DST_LINE',
    'MIXER_GETLINEINFOF_LINEID', 'MIXERLINE_COMPONENTTYPE_DST_DIGITAL',
    'MIXER_GETCONTROLDETAILSF_LISTTEXT', 'LPAUXCAPS', 'tagAUXCAPSW',
    'MIXERCONTROL_CT_UNITS_BOOLEAN', 'MIXER_GETLINEINFOF_COMPONENTTYPE',
    'MOM_POSITIONCB', 'MOD_SWSYNTH', 'WAVECAPS_SAMPLEACCURATE',
    'LPMIXERCAPS2', 'tagMIXERCONTROLDETAILS_LISTTEXTW', 'NPAUXCAPS',
    'NPMIDIOUTCAPS2', 'MIXERCONTROL_CONTROLTYPE_FADER', 'MOM_OPEN',
    'PMIDIOUTCAPS2', 'tagMIXERCONTROLDETAILS_LISTTEXTA',
    'MIXERCONTROL_CT_SC_TIME_MILLISECS', 'MIXERCONTROL_CT_UNITS_PERCENT',
    'MOD_MAPPER', 'auxGetDevCaps', 'NPWAVEINCAPS2', 'LPHMIXEROBJ',
    'MIXERCONTROL_CT_CLASS_FADER', 'WAVEOUTCAPS2',
    'MIXER_SETCONTROLDETAILSF_QUERYMASK', 'MIXERCONTROL_CT_CLASS_CUSTOM',
    'AUXCAPS', 'LPHWAVEIN', 'WAVE_FORMAT_96S16', 'MIXER_OBJECTF_MIXER',
    'MIM_LONGERROR', 'LPHMIDIOUT', 'midiproptimediv_tag',
    'MIXERCONTROL_CONTROLTYPE_EQUALIZER', 'MIXERLINE_COMPONENTTYPE_SRC_LAST',
    'midiInGetDevCaps', 'MIXERCONTROL_CT_SC_TIME_MICROSECS',
    'WAVE_FORMAT_48M08', 'PATCHARRAY', 'MIXER_GETLINECONTROLSF_QUERYMASK',
    'AUXCAPS_AUXIN', 'waveInGetErrorText', 'MIXER_SETCONTROLDETAILSF_CUSTOM',
    'MIXERLINE_COMPONENTTYPE_DST_HEADPHONES', 'MEVT_COMMENT',
    'MIXERCONTROL_CONTROLTYPE_MULTIPLESELECT', 'tagMIXERCAPS2A',
    'MIDIPROP_GET', 'MIXER_OBJECTF_WAVEIN', 'WAVE_FORMAT_4S08',
    'MIXERLINE_TARGETTYPE_WAVEOUT', 'LPCWAVEFORMATEX', 'tagMIXERCAPS2W',
    'LPHMIDI', 'MIXERLINE_LINEF_DISCONNECTED', 'WAVECAPS_PLAYBACKRATE',
    'WOM_OPEN', 'WAVE_INVALIDFORMAT', 'LPWAVEINCAPS',
    'MIXERCONTROL_CONTROLTYPE_SLIDER', 'MIXERCONTROL_CT_UNITS_DECIBELS',
    'WAVEINCAPS', 'MEVT_NOP', 'MIXERLINE_COMPONENTTYPE_DST_VOICEIN',
    'WHDR_BEGINLOOP', 'MIXER_OBJECTF_HMIXER', 'MIXERLINE_TARGETTYPE_MIDIIN',
    'MIXERLINE_COMPONENTTYPE_SRC_COMPACTDISC', 'midihdr_tag',
    'PMIXERCONTROL', 'PMIDIINCAPS2', 'MIXERCONTROL_CONTROLTYPE_LOUDNESS',
    'MIXERCONTROL_CONTROLTYPE_SIGNED', 'MOD_WAVETABLE', 'MIXERCONTROL',
    'MIDIPROP_TEMPO', 'MIXERLINE_TARGETTYPE_MIDIOUT', 'WAVECAPS_PITCH',
    'MIXER_GETLINECONTROLSF_ONEBYID', 'tagMIDIOUTCAPS2A',
    'MIDIERR_LASTERROR', 'MIDIOUTCAPS', 'MIXERCONTROL_CT_SC_LIST_SINGLE',
    'WAVE_FORMAT_QUERY', 'MIXER_OBJECTF_HANDLE', 'pcmwaveformat_tag',
    'tagMIDIOUTCAPS2W', 'tagWAVEINCAPSW', 'MIXERCONTROL_CONTROLTYPE_DECIBELS',
    'MIDICAPS_CACHE', 'MIXERR_INVALVALUE', 'MIXERLINE',
    'WAVE_MAPPED_DEFAULT_COMMUNICATION_DEVICE', 'PAUXCAPS2', 'LPWAVECALLBACK',
    'MIXERCONTROL_CONTROLTYPE_PEAKMETER', 'WAVERR_STILLPLAYING',
    'MIXERLINE_COMPONENTTYPE_DST_SPEAKERS', 'MIXERCONTROL_CONTROLTYPE_PAN',
    'NPWAVEOUTCAPS2', 'MIXERCONTROL_CONTROLTYPE_STEREOENH', 'MIXERCAPS2',
    'AUXCAPS_CDAUDIO', 'WAVE_FORMAT_44S16', 'MIXERCONTROL_CONTROLF_DISABLED',
    'MIDIERR_NOTREADY', 'MIXERLINE_TARGETTYPE_UNDEFINED',
    'MIXERLINE_COMPONENTTYPE_DST_MONITOR', 'mixerGetDevCaps', 'tagAUXCAPSA',
    'MIXERCONTROL_CONTROLTYPE_UNSIGNED', 'MIXERCONTROL_CONTROLTYPE_BASS_BOOST',
    'WAVEINCAPS2', 'MIXERCONTROL_CT_SC_SWITCH_BUTTON', 'WHDR_DONE',
    'NPMIDIOUTCAPS', 'WAVE_FORMAT_2S16', 'NPAUXCAPS2', 'WHDR_PREPARED',
    'MIDI_IO_STATUS',
)
