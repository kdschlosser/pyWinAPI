import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *


class _CONSOLE_READCONSOLE_CONTROL(ctypes.Structure):
    pass


CONSOLE_READCONSOLE_CONTROL = _CONSOLE_READCONSOLE_CONTROL
PCONSOLE_READCONSOLE_CONTROL = POINTER(_CONSOLE_READCONSOLE_CONTROL)


# *****************************************************************************
# * consoleapi.h - - ApiSet Contract for api - ms - win - core - console - l1
# *
# * Copyright (c) Microsoft Corporation. All rights reserved.
# *
# * ***************************************************************************


if defined(_MSC_VER):
    pass
# END IF   _MSC_VER

_APISETCONSOLE_ = None
if not defined(_APISETCONSOLE_):
    _APISETCONSOLE_ = 1

    from pyWinAPI.shared.apiset_h import * # NOQA
    from pyWinAPI.shared.apisetcconv_h import * # NOQA
    from pyWinAPI.shared.minwindef_h import * # NOQA
    from pyWinAPI.um.minwinbase_h import * # NOQA
    from pyWinAPI.um.wincontypes_h import * # NOQA
    kernel32 = ctypes.windll.KERNEL32

    if defined(__cplusplus):
        # extern "C" {
        # #endif
        #
        # #pragma region Application Family or OneCore Family
        # #if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        #
        # WINBASEAPI
        # BOOL
        # WINAPI
        # AllocConsole(
        # VOID
        # );
        AllocConsole = kernel32.AllocConsole
        AllocConsole.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # FreeConsole(
        # VOID
        # );
        FreeConsole = kernel32.FreeConsole
        FreeConsole.restype = BOOL

        if _WIN32_WINNT >= 0x0500:
            # WINBASEAPI
            # BOOL
            # WINAPI
            # AttachConsole(
            # _In_ DWORD dwProcessId
            # );
            AttachConsole = kernel32.AttachConsole
            AttachConsole.restype = BOOL

            ATTACH_PARENT_PROCESS = -1
        # END IF  _WIN32_WINNT >= 0x0500

        # WINBASEAPI
        # UINT
        # WINAPI
        # GetConsoleCP(
        # VOID
        # );
        GetConsoleCP = kernel32.GetConsoleCP
        GetConsoleCP.restype = UINT

        # WINBASEAPI
        # UINT
        # WINAPI
        # GetConsoleOutputCP(
        # VOID
        # );
        GetConsoleOutputCP = kernel32.GetConsoleOutputCP
        GetConsoleOutputCP.restype = UINT

        # Input Mode flags:
        ENABLE_PROCESSED_INPUT = 0x0001
        ENABLE_LINE_INPUT = 0x0002
        ENABLE_ECHO_INPUT = 0x0004
        ENABLE_WINDOW_INPUT = 0x0008
        ENABLE_MOUSE_INPUT = 0x0010
        ENABLE_INSERT_MODE = 0x0020
        ENABLE_QUICK_EDIT_MODE = 0x0040
        ENABLE_EXTENDED_FLAGS = 0x0080
        ENABLE_AUTO_POSITION = 0x0100
        ENABLE_VIRTUAL_TERMINAL_INPUT = 0x0200

        # Output Mode flags:
        ENABLE_PROCESSED_OUTPUT = 0x0001
        ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        DISABLE_NEWLINE_AUTO_RETURN = 0x0008
        ENABLE_LVB_GRID_WORLDWIDE = 0x0010

        # WINBASEAPI
        # BOOL
        # WINAPI
        # GetConsoleMode(
        # _In_ HANDLE hConsoleHandle,
        # _Out_ LPDWORD lpMode
        # );
        GetConsoleMode = kernel32.GetConsoleMode
        GetConsoleMode.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleMode(
        # _In_ HANDLE hConsoleHandle,
        # _In_ DWORD dwMode
        # );
        SetConsoleMode = kernel32.SetConsoleMode
        SetConsoleMode.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # GetNumberOfConsoleInputEvents(
        # _In_ HANDLE hConsoleInput,
        # _Out_ LPDWORD lpNumberOfEvents
        # );
        GetNumberOfConsoleInputEvents = kernel32.GetNumberOfConsoleInputEvents
        GetNumberOfConsoleInputEvents.restype = BOOL

        # WINBASEAPI
        # _Success_(return != FALSE)
        # BOOL
        # WINAPI
        # ReadConsoleInputA(
        # _In_ HANDLE hConsoleInput,
        # _Out_writes_to_(nLength,*lpNumberOfEventsRead) PINPUT_RECORD lpBuffer,
        # _In_ DWORD nLength,
        # _Out_ _Deref_out_range_( <= ,nLength) LPDWORD lpNumberOfEventsRead
        # );
        ReadConsoleInputA = kernel32.ReadConsoleInputA
        ReadConsoleInputA.restype = BOOL

        # WINBASEAPI
        # _Success_(return != FALSE)
        # BOOL
        # WINAPI
        # ReadConsoleInputW(
        # _In_ HANDLE hConsoleInput,
        # _Out_writes_to_(nLength,*lpNumberOfEventsRead) PINPUT_RECORD lpBuffer,
        # _In_ DWORD nLength,
        # _Out_ _Deref_out_range_( <= ,nLength) LPDWORD lpNumberOfEventsRead
        # );
        ReadConsoleInputW = kernel32.ReadConsoleInputW
        ReadConsoleInputW.restype = BOOL

        if defined(UNICODE):
            ReadConsoleInput = ReadConsoleInputW
        else:
            ReadConsoleInput = ReadConsoleInputA
        # END IF   not UNICODE

        # WINBASEAPI
        # BOOL
        # WINAPI
        # PeekConsoleInputA(
        # _In_ HANDLE hConsoleInput,
        # _Out_writes_(nLength) PINPUT_RECORD lpBuffer,
        # _In_ DWORD nLength,
        # _Out_ LPDWORD lpNumberOfEventsRead
        # );
        PeekConsoleInputA = kernel32.PeekConsoleInputA
        PeekConsoleInputA.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # PeekConsoleInputW(
        # _In_ HANDLE hConsoleInput,
        # _Out_writes_(nLength) PINPUT_RECORD lpBuffer,
        # _In_ DWORD nLength,
        # _Out_ LPDWORD lpNumberOfEventsRead
        # );
        PeekConsoleInputW = kernel32.PeekConsoleInputW
        PeekConsoleInputW.restype = BOOL

        if defined(UNICODE):
            PeekConsoleInput = PeekConsoleInputW
        else:
            PeekConsoleInput = PeekConsoleInputA
        # END IF   not UNICODE

        _CONSOLE_READCONSOLE_CONTROL._fields_ = [
            ('nLength', ULONG),
            ('nInitialChars', ULONG),
            ('dwCtrlWakeupMask', ULONG),
            ('dwControlKeyState', ULONG),
        ]

        # WINBASEAPI
        # _Success_(return != FALSE)
        # BOOL
        # WINAPI
        # ReadConsoleA(
        # _In_ HANDLE hConsoleInput,
        # _Out_writes_bytes_to_(nNumberOfCharsToRead * (ctypes.sizeof(CHAR),*lpNumberOfCharsRead * (ctypes.sizeof(CHAR)) LPVOID lpBuffer,
        # _In_ DWORD nNumberOfCharsToRead,
        # _Out_ _Deref_out_range_( <= ,nNumberOfCharsToRead) LPDWORD lpNumberOfCharsRead,
        # _In_opt_ PCONSOLE_READCONSOLE_CONTROL pInputControl
        # );
        ReadConsoleA = kernel32.ReadConsoleA
        ReadConsoleA.restype = BOOL

        # WINBASEAPI
        # _Success_(return != FALSE)
        # BOOL
        # WINAPI
        # ReadConsoleW(
        # _In_ HANDLE hConsoleInput,
        # _Out_writes_bytes_to_(nNumberOfCharsToRead * (ctypes.sizeof(WCHAR),*lpNumberOfCharsRead * (ctypes.sizeof(WCHAR)) LPVOID lpBuffer,
        # _In_ DWORD nNumberOfCharsToRead,
        # _Out_ _Deref_out_range_( <= ,nNumberOfCharsToRead) LPDWORD lpNumberOfCharsRead,
        # _In_opt_ PCONSOLE_READCONSOLE_CONTROL pInputControl
        # );
        ReadConsoleW = kernel32.ReadConsoleW
        ReadConsoleW.restype = BOOL

        if defined(UNICODE):
            ReadConsole = ReadConsoleW
        else:
            ReadConsole = ReadConsoleA
        # END IF   not UNICODE

        # WINBASEAPI
        # BOOL
        # WINAPI
        # WriteConsoleA(
        # _In_ HANDLE hConsoleOutput,
        # _In_reads_(nNumberOfCharsToWrite) CONST VOID* lpBuffer,
        # _In_ DWORD nNumberOfCharsToWrite,
        # _Out_opt_ LPDWORD lpNumberOfCharsWritten,
        # _Reserved_ LPVOID lpReserved
        # );
        WriteConsoleA = kernel32.WriteConsoleA
        WriteConsoleA.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # WriteConsoleW(
        # _In_ HANDLE hConsoleOutput,
        # _In_reads_(nNumberOfCharsToWrite) CONST VOID* lpBuffer,
        # _In_ DWORD nNumberOfCharsToWrite,
        # _Out_opt_ LPDWORD lpNumberOfCharsWritten,
        # _Reserved_ LPVOID lpReserved
        # );
        WriteConsoleW = kernel32.WriteConsoleW
        WriteConsoleW.restype = BOOL

        if defined(UNICODE):
            WriteConsole = WriteConsoleW
        else:
            WriteConsole = WriteConsoleA
        # END IF   not UNICODE

        # Ctrl Event flags
        CTRL_C_EVENT = 0
        CTRL_BREAK_EVENT = 1
        CTRL_CLOSE_EVENT = 2

        # 3 is reservednot
        # 4 is reservednot
        CTRL_LOGOFF_EVENT = 5
        CTRL_SHUTDOWN_EVENT = 6

        # typedef for ctrl - c handler routines
        # BOOL
        # (WINAPI *PHANDLER_ROUTINE)(
        # _In_ DWORD CtrlType
        # );
        PHANDLER_ROUTINE = WINAPI(BOOL, DWORD)

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleCtrlHandler(
        # _In_opt_ PHANDLER_ROUTINE HandlerRoutine,
        # _In_ BOOL Add
        # );
        SetConsoleCtrlHandler = kernel32.SetConsoleCtrlHandler
        SetConsoleCtrlHandler.restype = BOOL

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if defined(__cplusplus):
        pass
    # END IF

# END IF   _APISETCONSOLE_
