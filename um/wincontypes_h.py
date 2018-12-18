import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *


_WINCONTYPES_ = None


class _COORD(ctypes.Structure):
    pass


COORD = _COORD
PCOORD = POINTER(_COORD)


class _SMALL_RECT(ctypes.Structure):
    pass

SMALL_RECT = _SMALL_RECT
PSMALL_RECT = POINTER(_SMALL_RECT)


class _KEY_EVENT_RECORD(ctypes.Structure):
    pass

KEY_EVENT_RECORD = _KEY_EVENT_RECORD
PKEY_EVENT_RECORD = POINTER(_KEY_EVENT_RECORD)


class _MOUSE_EVENT_RECORD(ctypes.Structure):
    pass

MOUSE_EVENT_RECORD = _MOUSE_EVENT_RECORD
PMOUSE_EVENT_RECORD = POINTER(_MOUSE_EVENT_RECORD)


class _WINDOW_BUFFER_SIZE_RECORD(ctypes.Structure):
    pass

WINDOW_BUFFER_SIZE_RECORD = _WINDOW_BUFFER_SIZE_RECORD
PWINDOW_BUFFER_SIZE_RECORD = POINTER(_WINDOW_BUFFER_SIZE_RECORD)


class _MENU_EVENT_RECORD(ctypes.Structure):
    pass

MENU_EVENT_RECORD = _MENU_EVENT_RECORD
PMENU_EVENT_RECORD = POINTER(_MENU_EVENT_RECORD)


class _FOCUS_EVENT_RECORD(ctypes.Structure):
    pass

FOCUS_EVENT_RECORD = _FOCUS_EVENT_RECORD
PFOCUS_EVENT_RECORD = POINTER(_FOCUS_EVENT_RECORD)


class _INPUT_RECORD(ctypes.Structure):
    pass

INPUT_RECORD = _INPUT_RECORD
PINPUT_RECORD = POINTER(_INPUT_RECORD)


class _CHAR_INFO(ctypes.Structure):
    pass

CHAR_INFO = _CHAR_INFO
PCHAR_INFO = POINTER(_CHAR_INFO)


class _CONSOLE_FONT_INFO(ctypes.Structure):
    pass

CONSOLE_FONT_INFO = _CONSOLE_FONT_INFO
PCONSOLE_FONT_INFO = POINTER(_CONSOLE_FONT_INFO)


# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: wincontypes.h Abstract: This module contains the common data types
# exported by the NT console subsystem. Created: 08 - Sep - 2017 Revision
# History: 26 - Oct - 1990 - Originally created in wincon.h - -
if not defined(_WINCONTYPES_):

    from pyWinAPI.shared.minwindef_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        _COORD._fields_ = [
            ('X', SHORT),
            ('Y', SHORT),
        ]

        _SMALL_RECT._fields_ = [
            ('Left', SHORT),
            ('Top', SHORT),
            ('Right', SHORT),
            ('Bottom', SHORT),
        ]


        class uChar(ctypes.Union):
            pass


        uChar._fields_ = [
            ('UnicodeChar', WCHAR),
            ('AsciiChar', CHAR),
        ]
        _KEY_EVENT_RECORD.uChar = uChar

        _KEY_EVENT_RECORD._fields_ = [
            ('bKeyDown', BOOL),
            ('wRepeatCount', WORD),
            ('wVirtualKeyCode', WORD),
            ('wVirtualScanCode', WORD),
            ('uChar', _KEY_EVENT_RECORD.uChar),
            ('dwControlKeyState', DWORD),
        ]

        # ControlKeyState flags
        RIGHT_ALT_PRESSED = 0x0001        # the right alt key is pressed.
        LEFT_ALT_PRESSED = 0x0002        # the left alt key is pressed.
        RIGHT_CTRL_PRESSED = 0x0004        # the right ctrl key is pressed.
        LEFT_CTRL_PRESSED = 0x0008        # the left ctrl key is pressed.
        SHIFT_PRESSED = 0x0010        # the shift key is pressed.
        NUMLOCK_ON = 0x0020        # the numlock light is on.
        SCROLLLOCK_ON = 0x0040        # the scrolllock light is on.
        CAPSLOCK_ON = 0x0080        # the capslock light is on.
        ENHANCED_KEY = 0x0100        # the key is enhanced.
        NLS_DBCSCHAR = 0x00010000        # DBCS for JPN: SBCS/DBCS mode.
        NLS_ALPHANUMERIC = 0x00000000        # DBCS for JPN: Alphanumeric mode.
        NLS_KATAKANA = 0x00020000        # DBCS for JPN: Katakana mode.
        NLS_HIRAGANA = 0x00040000        # DBCS for JPN: Hiragana mode.
        NLS_ROMAN = 0x00400000        # DBCS for JPN: Roman/Noroman mode.
        NLS_IME_CONVERSION = 0x00800000        # DBCS for JPN: IME conversion.
        ALTNUMPAD_BIT = 0x04000000        # AltNumpad OEM CHAR (copied from ntuser\inc\kbd.h) ;internal_NT
        NLS_IME_DISABLE = 0x20000000        # DBCS for JPN: IME enable/disable.

        _MOUSE_EVENT_RECORD._fields_ = [
            ('dwMousePosition', COORD),
            ('dwButtonState', DWORD),
            ('dwControlKeyState', DWORD),
            ('dwEventFlags', DWORD),
        ]

        # ButtonState flags
        FROM_LEFT_1ST_BUTTON_PRESSED = 0x0001
        RIGHTMOST_BUTTON_PRESSED = 0x0002
        FROM_LEFT_2ND_BUTTON_PRESSED = 0x0004
        FROM_LEFT_3RD_BUTTON_PRESSED = 0x0008
        FROM_LEFT_4TH_BUTTON_PRESSED = 0x0010

        # EventFlags
        MOUSE_MOVED = 0x0001
        DOUBLE_CLICK = 0x0002
        MOUSE_WHEELED = 0x0004

        if _WIN32_WINNT >= 0x0600:
            MOUSE_HWHEELED = 0x0008
        # END IF  _WIN32_WINNT >= 0x0600

        _WINDOW_BUFFER_SIZE_RECORD._fields_ = [
            ('dwSize', COORD),
        ]

        _MENU_EVENT_RECORD._fields_ = [
            ('dwCommandId', UINT),
        ]

        _FOCUS_EVENT_RECORD._fields_ = [
            ('bSetFocus', BOOL),
        ]


        class Event(ctypes.Union):
            pass


        Event._fields_ = [
            ('KeyEvent', KEY_EVENT_RECORD),
            ('MouseEvent', MOUSE_EVENT_RECORD),
            ('WindowBufferSizeEvent', WINDOW_BUFFER_SIZE_RECORD),
            ('MenuEvent', MENU_EVENT_RECORD),
            ('FocusEvent', FOCUS_EVENT_RECORD),
        ]
        _INPUT_RECORD.Event = Event

        _INPUT_RECORD._fields_ = [
            ('EventType', WORD),
            ('Event', _INPUT_RECORD.Event),
        ]

        # EventType flags:
        KEY_EVENT = 0x0001        # Event contains key event record
        MOUSE_EVENT = 0x0002        # Event contains mouse event record
        WINDOW_BUFFER_SIZE_EVENT = 0x0004        # Event contains window change event record
        MENU_EVENT = 0x0008        # Event contains menu event record
        FOCUS_EVENT = 0x0010        # event contains focus change


        class Char(ctypes.Union):
            pass


        Char._fields_ = [
            ('UnicodeChar', WCHAR),
            ('AsciiChar', CHAR),
        ]
        _CHAR_INFO.Char = Char

        _CHAR_INFO._fields_ = [
            ('Char', _CHAR_INFO.Char),
            ('Attributes', WORD),
        ]

        _CONSOLE_FONT_INFO._fields_ = [
            ('nFont', DWORD),
            ('dwFontSize', COORD),
        ]

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    if defined(__cplusplus):
        pass
    # END IF
# END IF   _WINCONTYPES_
