# from ..macwin32_h import * # NOQA
# from ..pshpack1_h import * # NOQA
from .winapifamily_h import * # NOQA

from .wtypes_h import (
    UINT,
    DWORD,
    BYTE,
    POINTER,
    VOID,
    DWORD_PTR,
    HANDLE
)
import ctypes

CALLBACK = VOID

# ==========================================================================
# *
# *  mmsyscom.h -- Commonm Include file for Multimedia API's
# *
# *  Version 4.00
# *
# *  Copyright (C) 1992-1998 Microsoft Corporation.  All Rights Reserved.
# *
# *==========================================================================
# #defined if mmsystem.h has been included
# nameless struct/union
# Assume C declarations for C++
# __cplusplus
# WINMMAPI = DECLSPEC_IMPORT
# _MAC
# ***************************************************************************
# General constants and data types
# ***************************************************************************
# general constants
# max product name length (including NULL)
# max error text length (including NULL)
MAXPNAMELEN = 0x20
# max oem vxd name length (including NULL)
MAXERRORLENGTH = 0x100
MAX_JOYSTICKOEMVXDNAME = 0x104
# *  Microsoft Manufacturer and Product ID's (these have been moved to
# *  MMREG.H for Windows 4.00 and above).
# Microsoft Corporation
MM_MICROSOFT = 0x1
# MIDI Mapper
# Wave Mapper
MM_MIDI_MAPPER = 0x1
# Sound Blaster MIDI output port
MM_WAVE_MAPPER = 0x2
# Sound Blaster MIDI input port
MM_SNDBLST_MIDIOUT = 0x3
# Sound Blaster INTernal synthesizer
MM_SNDBLST_MIDIIN = 0x4
# Sound Blaster waveform output
MM_SNDBLST_SYNTH = 0x5
# Sound Blaster waveform input
MM_SNDBLST_WAVEOUT = 0x6
# Ad Lib-compatible synthesizer
MM_SNDBLST_WAVEIN = 0x7
# MPU401-compatible MIDI output port
MM_ADLIB = 0x9
# MPU401-compatible MIDI input port
MM_MPU401_MIDIOUT = 0xA
# Joystick adapter
MM_MPU401_MIDIIN = 0xB
MM_PC_JOYSTICK = 0xC
# general data types
# major (high byte), minor (low byte)
MMVERSION = UINT
# major (high byte), minor (low byte)
VERSION = UINT
# error return code, 0 means no error
# call as if(err=xxxx(...)) Error(err); else
MMRESULT = UINT
# MMTIME data structure


class mmtime_tag(ctypes.Structure):

    class u(ctypes.Union):

        class smpte(ctypes.Structure):
            _fields_ = [
                ('hour', BYTE),
                ('min', BYTE),
                ('sec', BYTE),
                ('frame', BYTE),
                ('fps', BYTE),
                ('dummy', BYTE),
                ('pad', BYTE * 2),
            ]

        class midi(ctypes.Structure):
            _fields_ = [
                ('songptrpos', DWORD),
            ]

        _fields_ = [
            ('ms', DWORD),
            ('sample', DWORD),
            ('cb', DWORD),
            ('ticks', DWORD),
            ('smpte', smpte),
            ('midi', midi),
        ]

    _fields_ = [
        ('wType', UINT),
        ('u', u),
    ]


MMTIME = mmtime_tag
PMMTIME = POINTER(mmtime_tag)
NPMMTIME = mmtime_tag
LPMMTIME = mmtime_tag


# indicates the contents of the union
# milliseconds
# samples
# byte count
# ticks in MIDI stream
# SMPTE
# hours
# minutes
# seconds
# frames
# frames per second
# pad
# MIDI
# song poINTer position
# types for wType field in MMTIME struct
# time in milliseconds
# number of wave samples
TIME_MS = 0x0001
# current byte offset
TIME_SAMPLES = 0x0002
# SMPTE time
TIME_BYTES = 0x0004
# MIDI time
TIME_SMPTE = 0x0008
# Ticks within MIDI stream
TIME_MIDI = 0x0010
TIME_TICKS = 0x0020
# *
# *


def MAKEFOURCC(ch0, ch1, ch2, ch3):
    return ch0 | (ch1 << 8) | (ch2 << 16) | (ch3 << 24)
# ***************************************************************************
# Multimedia Extensions Window Messages
# ***************************************************************************


# joystick
MM_JOY1MOVE = 0x3A0
MM_JOY2MOVE = 0x3A1
MM_JOY1ZMOVE = 0x3A2
MM_JOY2ZMOVE = 0x3A3
MM_JOY1BUTTONDOWN = 0x3B5
MM_JOY2BUTTONDOWN = 0x3B6
MM_JOY1BUTTONUP = 0x3B7
MM_JOY2BUTTONUP = 0x3B8
# MCI
MM_MCINOTIFY = 0x3B9
# waveform output
MM_WOM_OPEN = 0x3BB
MM_WOM_CLOSE = 0x3BC
MM_WOM_DONE = 0x3BD
# waveform input
MM_WIM_OPEN = 0x3BE
MM_WIM_CLOSE = 0x3BF
MM_WIM_DATA = 0x3C0
# MIDI input
MM_MIM_OPEN = 0x3C1
MM_MIM_CLOSE = 0x3C2
MM_MIM_DATA = 0x3C3
MM_MIM_LONGDATA = 0x3C4
MM_MIM_ERROR = 0x3C5
MM_MIM_LONGERROR = 0x3C6
# MIDI output
MM_MOM_OPEN = 0x3C7
MM_MOM_CLOSE = 0x3C8
MM_MOM_DONE = 0x3C9
# these are also in msvideo.h
# installable drivers
# these are used by msacm.h
MM_STREAM_OPEN = 0x3D4
MM_STREAM_CLOSE = 0x3D5
MM_STREAM_DONE = 0x3D6
MM_STREAM_ERROR = 0x3D7
# Callback for MEVT_POSITIONCB
MM_MOM_POSITIONCB = 0x3CA
# MIM_DONE w/ pending events
MM_MIM_MOREDATA = 0x3CC
# WINVER >= 0x0400
# mixer line change notify
# mixer control change notify
MM_MIXM_LINE_CHANGE = 0x3D0
MM_MIXM_CONTROL_CHANGE = 0x3D1
# ***************************************************************************
# String resource number bases (INTernal use)
# ***************************************************************************
MMSYSERR_BASE = 0x0
WAVERR_BASE = 0x20
MIDIERR_BASE = 0x40
TIMERR_BASE = 0x60
JOYERR_BASE = 0xA0
MCIERR_BASE = 0x100
MIXERR_BASE = 0x400
MCI_STRING_OFFSET = 0x200
MCI_VD_OFFSET = 0x400
MCI_CD_OFFSET = 0x440
MCI_WAVE_OFFSET = 0x480
MCI_SEQ_OFFSET = 0x4C0
# ***************************************************************************
# General error return values
# ***************************************************************************
# general error return values
# no error
# unspecified error
MMSYSERR_NOERROR = 0x0
# device ID out of range
MMSYSERR_ERROR = MMSYSERR_BASE + 1
# driver failed enable
MMSYSERR_BADDEVICEID = MMSYSERR_BASE + 2
# device already allocated
MMSYSERR_NOTENABLED = MMSYSERR_BASE + 3
# device handle is invalid
MMSYSERR_ALLOCATED = MMSYSERR_BASE + 4
# no device driver present
MMSYSERR_INVALHANDLE = MMSYSERR_BASE + 5
# memory allocation error
MMSYSERR_NODRIVER = MMSYSERR_BASE + 6
# function isn't supported
MMSYSERR_NOMEM = MMSYSERR_BASE + 7
# error value out of range
MMSYSERR_NOTSUPPORTED = MMSYSERR_BASE + 8
# invalid flag passed
MMSYSERR_BADERRNUM = MMSYSERR_BASE + 9
# invalid parameter passed
MMSYSERR_INVALFLAG = MMSYSERR_BASE + 10
# handle being used
MMSYSERR_INVALPARAM = MMSYSERR_BASE + 11
# simultaneously on another
MMSYSERR_HANDLEBUSY = MMSYSERR_BASE + 12
# thread (eg callback)
# specified alias not found
# bad registry database
MMSYSERR_INVALIDALIAS = MMSYSERR_BASE + 13
# registry key not found
MMSYSERR_BADDB = MMSYSERR_BASE + 14
# registry read error
MMSYSERR_KEYNOTFOUND = MMSYSERR_BASE + 15
# registry write error
MMSYSERR_READERROR = MMSYSERR_BASE + 16
# registry delete error
MMSYSERR_WRITEERROR = MMSYSERR_BASE + 17
# registry value not found
MMSYSERR_DELETEERROR = MMSYSERR_BASE + 18
# driver does not call DriverCallback
MMSYSERR_VALNOTFOUND = MMSYSERR_BASE + 19
# more data to be returned
MMSYSERR_NODRIVERCB = MMSYSERR_BASE + 20
# last error in range
MMSYSERR_MOREDATA = MMSYSERR_BASE + 21
MMSYSERR_LASTERROR = MMSYSERR_BASE + 21

HDRVR = HANDLE

# ifdef WINVER < 0x030a
# ***************************************************************************
# Driver callback support
# ***************************************************************************
# flags used with waveOutOpen(), waveInOpen(), midiInOpen(), and
# midiOutOpen() to specify the type of the dwCallback parameter.
# callback type mask
# no callback
CALLBACK_TYPEMASK = 0x00070000
# dwCallback is a HWND
CALLBACK_NULL = 0x00000000
# dwCallback is a HTASK
CALLBACK_WINDOW = 0x00010000
# dwCallback is a FARPROC
CALLBACK_TASK = 0x00020000
CALLBACK_FUNCTION = 0x00030000
# thread ID replaces 16 bit task
# dwCallback is an EVENT Handle
CALLBACK_THREAD = CALLBACK_TASK
CALLBACK_EVENT = 0x00050000

DRVCALLBACK = ctypes.WINFUNCTYPE(
    CALLBACK,
    HDRVR,
    UINT,
    DWORD_PTR,
    DWORD_PTR,
    DWORD_PTR
)

LPDRVCALLBACK = POINTER(DRVCALLBACK)
PDRVCALLBACK = POINTER(DRVCALLBACK)

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# Assume C declarations for C++
# __cplusplus
# from .poppack_h import * # NOQA
# _INC_MMSYSCOM

__all__ = (
    'MM_WIM_OPEN', 'MM_SNDBLST_WAVEOUT', 'MIDIERR_BASE', 'CALLBACK_TASK',
    'MMSYSERR_READERROR', 'MMSYSERR_HANDLEBUSY', 'MM_MIM_LONGDATA',
    'MAKEFOURCC', 'MM_SNDBLST_WAVEIN', 'JOYERR_BASE', 'MM_MIM_CLOSE',
    'MMSYSERR_ERROR', 'MM_MCINOTIFY', 'MMSYSERR_MOREDATA',
    'MCI_CD_OFFSET', 'MM_WIM_CLOSE', 'MIXERR_BASE', 'MCI_VD_OFFSET',
    'MMSYSERR_NOTSUPPORTED', 'MMSYSERR_NOERROR', 'MM_JOY1BUTTONDOWN',
    'MM_MIXM_LINE_CHANGE', 'MM_MOM_CLOSE', 'MM_WOM_OPEN', 'TIME_SAMPLES',
    'MM_PC_JOYSTICK', 'MM_JOY1ZMOVE', 'MAX_JOYSTICKOEMVXDNAME',
    'MM_JOY1MOVE', 'MMSYSERR_BASE', 'MM_MIM_OPEN', 'MCI_WAVE_OFFSET',
    'MM_MIDI_MAPPER', 'MMSYSERR_NOMEM', 'MM_JOY2MOVE', 'MM_WAVE_MAPPER',
    'MMSYSERR_NODRIVERCB', 'MCI_SEQ_OFFSET', 'TIME_MIDI', 'MM_WOM_DONE',
    'TIME_TICKS', 'MMSYSERR_DELETEERROR', 'MM_STREAM_DONE',
    'MMSYSERR_ALLOCATED', 'MM_MOM_POSITIONCB', 'MCI_STRING_OFFSET',
    'MMSYSERR_BADDB', 'TIMERR_BASE', 'MMSYSERR_NODRIVER',
    'MM_SNDBLST_MIDIOUT', 'CALLBACK_TYPEMASK', 'MM_JOY2BUTTONDOWN',
    'CALLBACK_FUNCTION', 'CALLBACK_EVENT', 'MCIERR_BASE', 'MM_MOM_OPEN',
    'MMSYSERR_INVALPARAM', 'MM_JOY2BUTTONUP', 'MMSYSERR_VALNOTFOUND',
    'MM_MIXM_CONTROL_CHANGE', 'MMSYSERR_WRITEERROR',
    'MMSYSERR_INVALIDALIAS', 'MM_SNDBLST_MIDIIN', 'MM_MIM_MOREDATA',
    'MM_STREAM_OPEN', 'MM_MPU401_MIDIOUT', 'MMSYSERR_BADERRNUM',
    'MM_WOM_CLOSE', 'MAXERRORLENGTH', 'MM_JOY2ZMOVE', 'MM_MIM_LONGERROR',
    'MMSYSERR_LASTERROR', 'MM_STREAM_ERROR', 'CALLBACK_THREAD',
    'MM_WIM_DATA', 'MAXPNAMELEN', 'MM_MPU401_MIDIIN', 'CALLBACK_WINDOW',
    'MM_MICROSOFT', 'MM_MIM_DATA', 'MM_JOY1BUTTONUP', 'MM_SNDBLST_SYNTH',
    'MM_ADLIB', 'MMSYSERR_BADDEVICEID', 'WAVERR_BASE', 'TIME_BYTES',
    'MM_MOM_DONE', 'MMSYSERR_INVALFLAG', 'TIME_MS', 'MM_MIM_ERROR',
    'MM_STREAM_CLOSE', 'TIME_SMPTE', 'MMSYSERR_NOTENABLED',
    'CALLBACK_NULL', 'MMSYSERR_INVALHANDLE', 'MMSYSERR_KEYNOTFOUND',
    'mmtime_tag', 'PDRVCALLBACK', 'LPDRVCALLBACK', 'MMVERSION', 'VERSION',
    'MMRESULT', 'HDRVR', 'DRVCALLBACK'
)
