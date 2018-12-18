import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *


class _CONSOLE_CURSOR_INFO(ctypes.Structure):
    pass


CONSOLE_CURSOR_INFO = _CONSOLE_CURSOR_INFO
PCONSOLE_CURSOR_INFO = POINTER(_CONSOLE_CURSOR_INFO)


class _CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    pass


CONSOLE_SCREEN_BUFFER_INFO = _CONSOLE_SCREEN_BUFFER_INFO
PCONSOLE_SCREEN_BUFFER_INFO = POINTER(_CONSOLE_SCREEN_BUFFER_INFO)


class _CONSOLE_SCREEN_BUFFER_INFOEX(ctypes.Structure):
    pass


CONSOLE_SCREEN_BUFFER_INFOEX = _CONSOLE_SCREEN_BUFFER_INFOEX
PCONSOLE_SCREEN_BUFFER_INFOEX = POINTER(_CONSOLE_SCREEN_BUFFER_INFOEX)


# *****************************************************************************
# * consoleapi2.h - - ApiSet Contract for api - ms - win - core - console - l2
# *
# * Copyright (c) Microsoft Corporation. All rights reserved.
# *
# * ***************************************************************************
#

if defined(_MSC_VER):
    pass
# END IF   _MSC_VER

_APISETCONSOLEL2_ = None
if not defined(_APISETCONSOLEL2_):
    _APISETCONSOLEL2_ = 1

    from pyWinAPI.shared.apiset_h import * # NOQA
    from pyWinAPI.shared.apisetcconv_h import * # NOQA
    from pyWinAPI.shared.minwindef_h import * # NOQA
    from pyWinAPI.um.minwinbase_h import * # NOQA
    from pyWinAPI.um.wincontypes_h import * # NOQA
    from pyWinAPI.shared.windef_h import * # NOQA

    kernel32 = ctypes.windll.KERNEL32

    if defined(__cplusplus):
        pass
        # extern "C" {
    # END IF


    # pragma region Application Family or OneCore Family
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        #
        #
        # // Attributes flags:
        #
        #
        FOREGROUND_BLUE = 0x0001 # text color contains blue.
        FOREGROUND_GREEN = 0x0002 # text color contains green.
        FOREGROUND_RED = 0x0004 # text color contains red.
        FOREGROUND_INTENSITY = 0x0008 # text color is intensified.
        BACKGROUND_BLUE = 0x0010 # background color contains blue.
        BACKGROUND_GREEN = 0x0020 # background color contains green.
        BACKGROUND_RED = 0x0040 # background color contains red.
        BACKGROUND_INTENSITY = 0x0080 # background color is intensified.
        COMMON_LVB_LEADING_BYTE = 0x0100 # Leading Byte of DBCS
        COMMON_LVB_TRAILING_BYTE = 0x0200 # Trailing Byte of DBCS
        COMMON_LVB_GRID_HORIZONTAL = 0x0400 # DBCS: Grid attribute: top horizontal.
        COMMON_LVB_GRID_LVERTICAL = 0x0800 # DBCS: Grid attribute: left vertical.
        COMMON_LVB_GRID_RVERTICAL = 0x1000 # DBCS: Grid attribute: right vertical.
        COMMON_LVB_REVERSE_VIDEO = 0x4000 # DBCS: Reverse fore/back ground attribute.
        COMMON_LVB_UNDERSCORE = 0x8000 # DBCS: Underscore.

        COMMON_LVB_SBCSDBCS = 0x0300 # SBCS or DBCS flag.
        #
        # WINBASEAPI
        # BOOL
        # WINAPI
        # FillConsoleOutputCharacterA(
        # _In_ HANDLE hConsoleOutput,
        # _In_ CHAR cCharacter,
        # _In_ DWORD nLength,
        # _In_ COORD dwWriteCoord,
        # _Out_ LPDWORD lpNumberOfCharsWritten
        # );
        FillConsoleOutputCharacterA = kernel32.FillConsoleOutputCharacterA
        FillConsoleOutputCharacterA.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # FillConsoleOutputCharacterW(
        # _In_ HANDLE hConsoleOutput,
        # _In_ WCHAR cCharacter,
        # _In_ DWORD nLength,
        # _In_ COORD dwWriteCoord,
        # _Out_ LPDWORD lpNumberOfCharsWritten
        # );
        FillConsoleOutputCharacterW = kernel32.FillConsoleOutputCharacterW
        FillConsoleOutputCharacterW.restype = BOOL

        if defined(UNICODE):
            FillConsoleOutputCharacter = FillConsoleOutputCharacterW
        else:
            FillConsoleOutputCharacter = FillConsoleOutputCharacterA
        # END IF   not UNICODE

        # WINBASEAPI
        # BOOL
        # WINAPI
        # FillConsoleOutputAttribute(
        # _In_ HANDLE hConsoleOutput,
        # _In_ WORD wAttribute,
        # _In_ DWORD nLength,
        # _In_ COORD dwWriteCoord,
        # _Out_ LPDWORD lpNumberOfAttrsWritten
        # );
        FillConsoleOutputAttribute = kernel32.FillConsoleOutputAttribute
        FillConsoleOutputAttribute.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # GenerateConsoleCtrlEvent(
        # _In_ DWORD dwCtrlEvent,
        # _In_ DWORD dwProcessGroupId
        # );
        GenerateConsoleCtrlEvent = kernel32.GenerateConsoleCtrlEvent
        GenerateConsoleCtrlEvent.restype = BOOL

        # WINBASEAPI
        # HANDLE
        # WINAPI
        # CreateConsoleScreenBuffer(
        # _In_ DWORD dwDesiredAccess,
        # _In_ DWORD dwShareMode,
        # _In_opt_ CONST SECURITY_ATTRIBUTES* lpSecurityAttributes,
        # _In_ DWORD dwFlags,
        # _Reserved_ LPVOID lpScreenBufferData
        # );
        CreateConsoleScreenBuffer = kernel32.CreateConsoleScreenBuffer
        CreateConsoleScreenBuffer.restype = HANDLE

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleActiveScreenBuffer(
        # _In_ HANDLE hConsoleOutput
        # );
        SetConsoleActiveScreenBuffer = kernel32.SetConsoleActiveScreenBuffer
        SetConsoleActiveScreenBuffer.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # FlushConsoleInputBuffer(
        # _In_ HANDLE hConsoleInput
        # );
        FlushConsoleInputBuffer = kernel32.FlushConsoleInputBuffer
        FlushConsoleInputBuffer.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleCP(
        # _In_ UINT wCodePageID
        # );
        SetConsoleCP = kernel32.SetConsoleCP
        SetConsoleCP.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleOutputCP(
        # _In_ UINT wCodePageID
        # );
        SetConsoleOutputCP = kernel32.SetConsoleOutputCP
        SetConsoleOutputCP.restype = BOOL

        _CONSOLE_CURSOR_INFO._fields_ = [
            ('dwSize', DWORD),
            ('bVisible', BOOL),
        ]

        # WINBASEAPI
        # BOOL
        # WINAPI
        # GetConsoleCursorInfo(
        # _In_ HANDLE hConsoleOutput,
        # _Out_ PCONSOLE_CURSOR_INFO lpConsoleCursorInfo
        # );
        GetConsoleCursorInfo = kernel32.GetConsoleCursorInfo
        GetConsoleCursorInfo.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleCursorInfo(
        # _In_ HANDLE hConsoleOutput,
        # _In_ CONST CONSOLE_CURSOR_INFO* lpConsoleCursorInfo
        # );
        SetConsoleCursorInfo = kernel32.SetConsoleCursorInfo
        SetConsoleCursorInfo.restype = BOOL

        _CONSOLE_SCREEN_BUFFER_INFO._fields_ = [
            ('dwSize', COORD),
            ('dwCursorPosition', COORD),
            ('wAttributes', WORD),
            ('srWindow', SMALL_RECT),
            ('dwMaximumWindowSize', COORD),
        ]

        # WINBASEAPI
        # BOOL
        # WINAPI
        # GetConsoleScreenBufferInfo(
        # _In_ HANDLE hConsoleOutput,
        # _Out_ PCONSOLE_SCREEN_BUFFER_INFO lpConsoleScreenBufferInfo
        # );
        GetConsoleScreenBufferInfo = kernel32.GetConsoleScreenBufferInfo
        GetConsoleScreenBufferInfo.restype = BOOL

        _CONSOLE_SCREEN_BUFFER_INFOEX._fields_ = [
            ('cbSize', ULONG),
            ('dwSize', COORD),
            ('dwCursorPosition', COORD),
            ('wAttributes', WORD),
            ('srWindow', SMALL_RECT),
            ('dwMaximumWindowSize', COORD),
            ('wPopupAttributes', WORD),
            ('bFullscreenSupported', BOOL),
            ('ColorTable', COLORREF * 16),
        ]

        # WINBASEAPI
        # BOOL
        # WINAPI
        # GetConsoleScreenBufferInfoEx(
        # _In_ HANDLE hConsoleOutput,
        # _Inout_ PCONSOLE_SCREEN_BUFFER_INFOEX lpConsoleScreenBufferInfoEx
        # );
        GetConsoleScreenBufferInfoEx = kernel32.GetConsoleScreenBufferInfoEx
        GetConsoleScreenBufferInfoEx.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleScreenBufferInfoEx(
        # _In_ HANDLE hConsoleOutput,
        # _In_ PCONSOLE_SCREEN_BUFFER_INFOEX lpConsoleScreenBufferInfoEx
        # );
        SetConsoleScreenBufferInfoEx = kernel32.SetConsoleScreenBufferInfoEx
        SetConsoleScreenBufferInfoEx.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleScreenBufferSize(
        # _In_ HANDLE hConsoleOutput,
        # _In_ COORD dwSize
        # );
        SetConsoleScreenBufferSize = kernel32.SetConsoleScreenBufferSize
        SetConsoleScreenBufferSize.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleCursorPosition(
        # _In_ HANDLE hConsoleOutput,
        # _In_ COORD dwCursorPosition
        # );
        SetConsoleCursorPosition = kernel32.SetConsoleCursorPosition
        SetConsoleCursorPosition.restype = BOOL

        # WINBASEAPI
        # COORD
        # WINAPI
        # GetLargestConsoleWindowSize(
        # _In_ HANDLE hConsoleOutput
        # );
        GetLargestConsoleWindowSize = kernel32.GetLargestConsoleWindowSize
        GetLargestConsoleWindowSize.restype = COORD

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleTextAttribute(
        # _In_ HANDLE hConsoleOutput,
        # _In_ WORD wAttributes
        # );
        SetConsoleTextAttribute = kernel32.SetConsoleTextAttribute
        SetConsoleTextAttribute.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleWindowInfo(
        # _In_ HANDLE hConsoleOutput,
        # _In_ BOOL bAbsolute,
        # _In_ CONST SMALL_RECT* lpConsoleWindow
        # );
        SetConsoleWindowInfo = kernel32.SetConsoleWindowInfo
        SetConsoleWindowInfo.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # WriteConsoleOutputCharacterA(
        # _In_ HANDLE hConsoleOutput,
        # _In_reads_(nLength) LPCSTR lpCharacter,
        # _In_ DWORD nLength,
        # _In_ COORD dwWriteCoord,
        # _Out_ LPDWORD lpNumberOfCharsWritten
        # );
        WriteConsoleOutputCharacterA = kernel32.WriteConsoleOutputCharacterA
        WriteConsoleOutputCharacterA.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # WriteConsoleOutputCharacterW(
        # _In_ HANDLE hConsoleOutput,
        # _In_reads_(nLength) LPCWSTR lpCharacter,
        # _In_ DWORD nLength,
        # _In_ COORD dwWriteCoord,
        # _Out_ LPDWORD lpNumberOfCharsWritten
        # );
        WriteConsoleOutputCharacterW = kernel32.WriteConsoleOutputCharacterW
        WriteConsoleOutputCharacterW.restype = BOOL

        if defined(UNICODE):
            WriteConsoleOutputCharacter = WriteConsoleOutputCharacterW
        else:
            WriteConsoleOutputCharacter = WriteConsoleOutputCharacterA
        # END IF   not UNICODE

        # WINBASEAPI
        # BOOL
        # WINAPI
        # WriteConsoleOutputAttribute(
        # _In_ HANDLE hConsoleOutput,
        # _In_reads_(nLength) CONST WORD* lpAttribute,
        # _In_ DWORD nLength,
        # _In_ COORD dwWriteCoord,
        # _Out_ LPDWORD lpNumberOfAttrsWritten
        # );
        WriteConsoleOutputAttribute = kernel32.WriteConsoleOutputAttribute
        WriteConsoleOutputAttribute.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # ReadConsoleOutputCharacterA(
        # _In_ HANDLE hConsoleOutput,
        # _Out_writes_(nLength) LPSTR lpCharacter,
        # _In_ DWORD nLength,
        # _In_ COORD dwReadCoord,
        # _Out_ LPDWORD lpNumberOfCharsRead
        # );
        ReadConsoleOutputCharacterA = kernel32.ReadConsoleOutputCharacterA
        ReadConsoleOutputCharacterA.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # ReadConsoleOutputCharacterW(
        # _In_ HANDLE hConsoleOutput,
        # _Out_writes_(nLength) LPWSTR lpCharacter,
        # _In_ DWORD nLength,
        # _In_ COORD dwReadCoord,
        # _Out_ LPDWORD lpNumberOfCharsRead
        # );
        ReadConsoleOutputCharacterW = kernel32.ReadConsoleOutputCharacterW
        ReadConsoleOutputCharacterW.restype = BOOL

        if defined(UNICODE):
            ReadConsoleOutputCharacter = ReadConsoleOutputCharacterW
        else:
            ReadConsoleOutputCharacter = ReadConsoleOutputCharacterA
        # END IF   not UNICODE

        # WINBASEAPI
        # BOOL
        # WINAPI
        # ReadConsoleOutputAttribute(
        # _In_ HANDLE hConsoleOutput,
        # _Out_writes_(nLength) LPWORD lpAttribute,
        # _In_ DWORD nLength,
        # _In_ COORD dwReadCoord,
        # _Out_ LPDWORD lpNumberOfAttrsRead
        # );
        ReadConsoleOutputAttribute = kernel32.ReadConsoleOutputAttribute
        ReadConsoleOutputAttribute.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # WriteConsoleInputA(
        # _In_ HANDLE hConsoleInput,
        # _In_reads_(nLength) CONST INPUT_RECORD* lpBuffer,
        # _In_ DWORD nLength,
        # _Out_ LPDWORD lpNumberOfEventsWritten
        # );
        WriteConsoleInputA = kernel32.WriteConsoleInputA
        WriteConsoleInputA.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # WriteConsoleInputW(
        # _In_ HANDLE hConsoleInput,
        # _In_reads_(nLength) CONST INPUT_RECORD* lpBuffer,
        # _In_ DWORD nLength,
        # _Out_ LPDWORD lpNumberOfEventsWritten
        # );
        WriteConsoleInputW = kernel32.WriteConsoleInputW
        WriteConsoleInputW.restype = BOOL

        if defined(UNICODE):
            WriteConsoleInput = WriteConsoleInputW
        else:
            WriteConsoleInput = WriteConsoleInputA
        # END IF   not UNICODE

        # WINBASEAPI
        # BOOL
        # WINAPI
        # ScrollConsoleScreenBufferA(
        # _In_ HANDLE hConsoleOutput,
        # _In_ CONST SMALL_RECT* lpScrollRectangle,
        # _In_opt_ CONST SMALL_RECT* lpClipRectangle,
        # _In_ COORD dwDestinationOrigin,
        # _In_ CONST CHAR_INFO* lpFill
        # );
        ScrollConsoleScreenBufferA = kernel32.ScrollConsoleScreenBufferA
        ScrollConsoleScreenBufferA.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # ScrollConsoleScreenBufferW(
        # _In_ HANDLE hConsoleOutput,
        # _In_ CONST SMALL_RECT* lpScrollRectangle,
        # _In_opt_ CONST SMALL_RECT* lpClipRectangle,
        # _In_ COORD dwDestinationOrigin,
        # _In_ CONST CHAR_INFO* lpFill
        # );
        ScrollConsoleScreenBufferW = kernel32.ScrollConsoleScreenBufferW
        ScrollConsoleScreenBufferW.restype = BOOL

        if defined(UNICODE):
            ScrollConsoleScreenBuffer = ScrollConsoleScreenBufferW
        else:
            ScrollConsoleScreenBuffer = ScrollConsoleScreenBufferA
        # END IF   not UNICODE

        # WINBASEAPI
        # BOOL
        # WINAPI
        # WriteConsoleOutputA(
        # _In_ HANDLE hConsoleOutput,
        # _In_reads_(dwBufferSize.X * dwBufferSize.Y) CONST CHAR_INFO* lpBuffer,
        # _In_ COORD dwBufferSize,
        # _In_ COORD dwBufferCoord,
        # _Inout_ PSMALL_RECT lpWriteRegion
        # );
        WriteConsoleOutputA = kernel32.WriteConsoleOutputA
        WriteConsoleOutputA.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # WriteConsoleOutputW(
        # _In_ HANDLE hConsoleOutput,
        # _In_reads_(dwBufferSize.X * dwBufferSize.Y) CONST CHAR_INFO* lpBuffer,
        # _In_ COORD dwBufferSize,
        # _In_ COORD dwBufferCoord,
        # _Inout_ PSMALL_RECT lpWriteRegion
        # );
        WriteConsoleOutputW = kernel32.WriteConsoleOutputW
        WriteConsoleOutputW.restype = BOOL

        if defined(UNICODE):
            WriteConsoleOutput = WriteConsoleOutputW
        else:
            WriteConsoleOutput = WriteConsoleOutputA
        # END IF   not UNICODE

        # WINBASEAPI
        # BOOL
        # WINAPI
        # ReadConsoleOutputA(
        # _In_ HANDLE hConsoleOutput,
        # _Out_writes_(dwBufferSize.X * dwBufferSize.Y) PCHAR_INFO lpBuffer,
        # _In_ COORD dwBufferSize,
        # _In_ COORD dwBufferCoord,
        # _Inout_ PSMALL_RECT lpReadRegion
        # );
        ReadConsoleOutputA = kernel32.ReadConsoleOutputA
        ReadConsoleOutputA.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # ReadConsoleOutputW(
        # _In_ HANDLE hConsoleOutput,
        # _Out_writes_(dwBufferSize.X * dwBufferSize.Y) PCHAR_INFO lpBuffer,
        # _In_ COORD dwBufferSize,
        # _In_ COORD dwBufferCoord,
        # _Inout_ PSMALL_RECT lpReadRegion
        # );
        ReadConsoleOutputW = kernel32.ReadConsoleOutputW
        ReadConsoleOutputW.restype = BOOL

        if defined(UNICODE):
            ReadConsoleOutput = ReadConsoleOutputW
        else:
            ReadConsoleOutput = ReadConsoleOutputA
        # END IF   not UNICODE

        # WINBASEAPI
        # DWORD
        # WINAPI
        # GetConsoleTitleA(
        # _Out_writes_(nSize) LPSTR lpConsoleTitle,
        # _In_ DWORD nSize
        # );
        GetConsoleTitleA = kernel32.GetConsoleTitleA
        GetConsoleTitleA.restype = DWORD

        # WINBASEAPI
        # DWORD
        # WINAPI
        # GetConsoleTitleW(
        # _Out_writes_(nSize) LPWSTR lpConsoleTitle,
        # _In_ DWORD nSize
        # );
        GetConsoleTitleW = kernel32.GetConsoleTitleW
        GetConsoleTitleW.restype = DWORD

        if defined(UNICODE):
            GetConsoleTitle = GetConsoleTitleW
        else:
            GetConsoleTitle = GetConsoleTitleA
        # END IF   not UNICODE

        if _WIN32_WINNT >= 0x0600:
            # WINBASEAPI
            # DWORD
            # WINAPI
            # GetConsoleOriginalTitleA(
            # _Out_writes_(nSize) LPSTR lpConsoleTitle,
            # _In_ DWORD nSize
            # );
            GetConsoleOriginalTitleA = kernel32.GetConsoleOriginalTitleA
            GetConsoleOriginalTitleA.restype = DWORD

            # WINBASEAPI
            # DWORD
            # WINAPI
            # GetConsoleOriginalTitleW(
            # _Out_writes_(nSize) LPWSTR lpConsoleTitle,
            # _In_ DWORD nSize
            # );
            GetConsoleOriginalTitleW = kernel32.GetConsoleOriginalTitleW
            GetConsoleOriginalTitleW.restype = DWORD

            if defined(UNICODE):
                GetConsoleOriginalTitle = GetConsoleOriginalTitleW
            else:
                GetConsoleOriginalTitle = GetConsoleOriginalTitleA
            # END IF   not UNICODE

        # END IF  _WIN32_WINNT >= 0x0600

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleTitleA(
        # _In_ LPCSTR lpConsoleTitle
        # );
        SetConsoleTitleA = kernel32.SetConsoleTitleA
        SetConsoleTitleA.restype = BOOL

        # WINBASEAPI
        # BOOL
        # WINAPI
        # SetConsoleTitleW(
        # _In_ LPCWSTR lpConsoleTitle
        # );
        SetConsoleTitleW = kernel32.SetConsoleTitleW
        SetConsoleTitleW.restype = BOOL

        if defined(UNICODE):
            SetConsoleTitle = SetConsoleTitleW
        else:
            SetConsoleTitle = SetConsoleTitleA
        # END IF   not UNICODE

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if defined(__cplusplus):
        pass
    # END IF

# END IF   _APISETCONSOLEL2_
