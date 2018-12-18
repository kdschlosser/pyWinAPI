import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *


class _CONSOLE_FONT_INFOEX(ctypes.Structure):
    pass


CONSOLE_FONT_INFOEX = _CONSOLE_FONT_INFOEX
PCONSOLE_FONT_INFOEX = POINTER(_CONSOLE_FONT_INFOEX)


class _CONSOLE_SELECTION_INFO(ctypes.Structure):
    pass


CONSOLE_SELECTION_INFO = _CONSOLE_SELECTION_INFO
PCONSOLE_SELECTION_INFO = POINTER(_CONSOLE_SELECTION_INFO)


class _CONSOLE_HISTORY_INFO(ctypes.Structure):
    pass


CONSOLE_HISTORY_INFO = _CONSOLE_HISTORY_INFO
PCONSOLE_HISTORY_INFO = POINTER(_CONSOLE_HISTORY_INFO)


# *****************************************************************************
# * consoleapi3.h - - ApiSet Contract for api - ms - win - core - console - l3
# *
# * Copyright (c) Microsoft Corporation. All rights reserved.
# *
# * ***************************************************************************
#
if defined(_MSC_VER):
    pass
# END IF   _MSC_VER

_APISETCONSOLEL3_ = None
if not defined(_APISETCONSOLEL3_):
    _APISETCONSOLEL3_ = None

    from pyWinAPI.shared.apiset_h import *  # NOQA
    from pyWinAPI.shared.apisetcconv_h import *  # NOQA
    from pyWinAPI.shared.minwindef_h import *  # NOQA
    from pyWinAPI.um.minwinbase_h import *  # NOQA
    from pyWinAPI.um.wincontypes_h import *  # NOQA
    from pyWinAPI.shared.windef_h import *  # NOQA


    NOGDI = None
    if not defined(NOGDI):
        from pyWinAPI.um.wingdi_h import * # NOQA
    # END IF

    kernel32 = ctypes.windll.KERNEL32

    if defined(__cplusplus):
        pass
        # extern "C" {
    # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        #
        # WINBASEAPI
        # BOOL
        # WINAPI
        # GetNumberOfConsoleMouseButtons(
        # _Out_ LPDWORD lpNumberOfMouseButtons
        # );
        GetNumberOfConsoleMouseButtons = (
            kernel32.GetNumberOfConsoleMouseButtons
        )
        GetNumberOfConsoleMouseButtons.restype = BOOL

        if _WIN32_WINNT >= 0x0500:
            # WINBASEAPI
            # COORD
            # WINAPI
            # GetConsoleFontSize(
            # _In_ HANDLE hConsoleOutput,
            # _In_ DWORD nFont
            # );
            GetConsoleFontSize = kernel32.GetConsoleFontSize
            GetConsoleFontSize.restype = COORD

            # WINBASEAPI
            # BOOL
            # WINAPI
            # GetCurrentConsoleFont(
            # _In_ HANDLE hConsoleOutput,
            # _In_ BOOL bMaximumWindow,
            # _Out_ PCONSOLE_FONT_INFO lpConsoleCurrentFont
            # );
            GetCurrentConsoleFont = kernel32.GetCurrentConsoleFont
            GetCurrentConsoleFont.restype = BOOL

            if not defined(NOGDI):
                _CONSOLE_FONT_INFOEX._fields_ = [
                    ('cbSize', ULONG),
                    ('nFont', DWORD),
                    ('dwFontSize', COORD),
                    ('FontFamily', UINT),
                    ('FontWeight', UINT),
                    ('FaceName', WCHAR * LF_FACESIZE),
                ]

                # WINBASEAPI
                # BOOL
                # WINAPI
                # GetCurrentConsoleFontEx(
                # _In_ HANDLE hConsoleOutput,
                # _In_ BOOL bMaximumWindow,
                # _Out_ PCONSOLE_FONT_INFOEX lpConsoleCurrentFontEx
                # );
                GetCurrentConsoleFontEx = kernel32.GetCurrentConsoleFontEx
                GetCurrentConsoleFontEx.restype = BOOL

                # WINBASEAPI
                # BOOL
                # WINAPI
                # SetCurrentConsoleFontEx(
                # _In_ HANDLE hConsoleOutput,
                # _In_ BOOL bMaximumWindow,
                # _In_ PCONSOLE_FONT_INFOEX lpConsoleCurrentFontEx
                # );
                SetCurrentConsoleFontEx = kernel32.SetCurrentConsoleFontEx
                SetCurrentConsoleFontEx.restype = BOOL

            # END IF

            # Selection flags
            CONSOLE_NO_SELECTION = 0x0000
            CONSOLE_SELECTION_IN_PROGRESS = 0x0001 # selection has begun
            CONSOLE_SELECTION_NOT_EMPTY = 0x0002 # non - null select rectangle
            CONSOLE_MOUSE_SELECTION = 0x0004 # selecting with mouse
            CONSOLE_MOUSE_DOWN = 0x0008 # mouse is down

            _CONSOLE_SELECTION_INFO._fields_ = [
                ('dwFlags', DWORD),
                ('dwSelectionAnchor', COORD),
                ('srSelection', SMALL_RECT),
            ]

            # WINBASEAPI
            # BOOL
            # WINAPI
            # GetConsoleSelectionInfo(
            # _Out_ PCONSOLE_SELECTION_INFO lpConsoleSelectionInfo
            # );
            GetConsoleSelectionInfo = kernel32.GetConsoleSelectionInfo
            GetConsoleSelectionInfo.restype = BOOL

            # History flags
            HISTORY_NO_DUP_FLAG = 0x1

            _CONSOLE_HISTORY_INFO._fields_ = [
                ('cbSize', UINT),
                ('HistoryBufferSize', UINT),
                ('NumberOfHistoryBuffers', UINT),
                ('dwFlags', DWORD),
            ]

            # WINBASEAPI
            # BOOL
            # WINAPI
            # GetConsoleHistoryInfo(
            # _Out_ PCONSOLE_HISTORY_INFO lpConsoleHistoryInfo
            # );
            GetConsoleHistoryInfo = kernel32.GetConsoleHistoryInfo
            GetConsoleHistoryInfo.restype = BOOL

            # WINBASEAPI
            # BOOL
            # WINAPI
            # SetConsoleHistoryInfo(
            # _In_ PCONSOLE_HISTORY_INFO lpConsoleHistoryInfo
            # );
            SetConsoleHistoryInfo = kernel32.SetConsoleHistoryInfo
            SetConsoleHistoryInfo.restype = BOOL

            CONSOLE_FULLSCREEN = 1 # fullscreen console
            CONSOLE_FULLSCREEN_HARDWARE = 2 # console owns the hardware

            # WINBASEAPI
            # BOOL
            # APIENTRY
            # GetConsoleDisplayMode(
            # _Out_ LPDWORD lpModeFlags
            # );
            GetConsoleDisplayMode = kernel32.GetConsoleDisplayMode
            GetConsoleDisplayMode.restype = BOOL

            CONSOLE_FULLSCREEN_MODE = 1
            CONSOLE_WINDOWED_MODE = 2

            # WINBASEAPI
            # BOOL
            # APIENTRY
            # SetConsoleDisplayMode(
            # _In_ HANDLE hConsoleOutput,
            # _In_ DWORD dwFlags,
            # _Out_opt_ PCOORD lpNewScreenBufferDimensions
            # );
            SetConsoleDisplayMode = kernel32.SetConsoleDisplayMode
            SetConsoleDisplayMode.restype = BOOL

            # WINBASEAPI
            # HWND
            # APIENTRY
            # GetConsoleWindow(
            # VOID
            # );
            GetConsoleWindow = kernel32.GetConsoleWindow
            GetConsoleWindow.restype = HWND

        # END IF  _WIN32_WINNT >= 0x0500

        if _WIN32_WINNT >= 0x0501:
            # WINBASEAPI
            # BOOL
            # APIENTRY
            # AddConsoleAliasA(
            # _In_ LPSTR Source,
            # _In_ LPSTR Target,
            # _In_ LPSTR ExeName
            # );
            AddConsoleAliasA = kernel32.AddConsoleAliasA
            AddConsoleAliasA.restype = BOOL

            # WINBASEAPI
            # BOOL
            # APIENTRY
            # AddConsoleAliasW(
            # _In_ LPWSTR Source,
            # _In_ LPWSTR Target,
            # _In_ LPWSTR ExeName
            # );
            AddConsoleAliasW = kernel32.AddConsoleAliasW
            AddConsoleAliasW.restype = BOOL

            if defined(UNICODE):
                AddConsoleAlias = AddConsoleAliasW
            else:
                AddConsoleAlias = AddConsoleAliasA
            # END IF   not UNICODE

            # WINBASEAPI
            # DWORD
            # APIENTRY
            # GetConsoleAliasA(
            # _In_ LPSTR Source,
            # _Out_writes_(TargetBufferLength) LPSTR TargetBuffer,
            # _In_ DWORD TargetBufferLength,
            # _In_ LPSTR ExeName
            # );
            GetConsoleAliasA = kernel32.GetConsoleAliasA
            GetConsoleAliasA.restype = DWORD

            # WINBASEAPI
            # DWORD
            # APIENTRY
            # GetConsoleAliasW(
            # _In_ LPWSTR Source,
            # _Out_writes_(TargetBufferLength) LPWSTR TargetBuffer,
            # _In_ DWORD TargetBufferLength,
            # _In_ LPWSTR ExeName
            # );
            GetConsoleAliasW = kernel32.GetConsoleAliasW
            GetConsoleAliasW.restype = DWORD

            if defined(UNICODE):
                GetConsoleAlias = GetConsoleAliasW
            else:
                GetConsoleAlias = GetConsoleAliasA
            # END IF   not UNICODE

            # WINBASEAPI
            # DWORD
            # APIENTRY
            # GetConsoleAliasesLengthA(
            # _In_ LPSTR ExeName
            # );
            GetConsoleAliasesLengthA = kernel32.GetConsoleAliasesLengthA
            GetConsoleAliasesLengthA.restype = DWORD

            # WINBASEAPI
            # DWORD
            # APIENTRY
            # GetConsoleAliasesLengthW(
            # _In_ LPWSTR ExeName
            # );
            GetConsoleAliasesLengthW = kernel32.GetConsoleAliasesLengthW
            GetConsoleAliasesLengthW.restype = DWORD

            if defined(UNICODE):
                GetConsoleAliasesLength = GetConsoleAliasesLengthW
            else:
                GetConsoleAliasesLength = GetConsoleAliasesLengthA
            # END IF   not UNICODE
            # WINBASEAPI
            # DWORD
            # APIENTRY
            # GetConsoleAliasExesLengthA(
            # VOID
            # );
            GetConsoleAliasExesLengthA = kernel32.GetConsoleAliasExesLengthA
            GetConsoleAliasExesLengthA.restype = DWORD

            # WINBASEAPI
            # DWORD
            # APIENTRY
            # GetConsoleAliasExesLengthW(
            # VOID
            # );
            GetConsoleAliasExesLengthW = kernel32.GetConsoleAliasExesLengthW
            GetConsoleAliasExesLengthW.restype = DWORD

            if defined(UNICODE):
                GetConsoleAliasExesLength = GetConsoleAliasExesLengthW
            else:
                GetConsoleAliasExesLength = GetConsoleAliasExesLengthA
            # END IF   not UNICODE

            # WINBASEAPI
            # DWORD
            # APIENTRY
            # GetConsoleAliasesA(
            # _Out_writes_(AliasBufferLength) LPSTR AliasBuffer,
            # _In_ DWORD AliasBufferLength,
            # _In_ LPSTR ExeName
            # );
            GetConsoleAliasesA = kernel32.GetConsoleAliasesA
            GetConsoleAliasesA.restype = DWORD

            # WINBASEAPI
            # DWORD
            # APIENTRY
            # GetConsoleAliasesW(
            # _Out_writes_(AliasBufferLength) LPWSTR AliasBuffer,
            # _In_ DWORD AliasBufferLength,
            # _In_ LPWSTR ExeName
            # );
            GetConsoleAliasesW = kernel32.GetConsoleAliasesW
            GetConsoleAliasesW.restype = DWORD

            if defined(UNICODE):
                GetConsoleAliases = GetConsoleAliasesW
            else:
                GetConsoleAliases = GetConsoleAliasesA
            # END IF   not UNICODE

            # WINBASEAPI
            # DWORD
            # APIENTRY
            # GetConsoleAliasExesA(
            # _Out_writes_(ExeNameBufferLength) LPSTR ExeNameBuffer,
            # _In_ DWORD ExeNameBufferLength
            # );
            GetConsoleAliasExesA = kernel32.GetConsoleAliasExesA
            GetConsoleAliasExesA.restype = DWORD

            # WINBASEAPI
            # DWORD
            # APIENTRY
            # GetConsoleAliasExesW(
            # _Out_writes_(ExeNameBufferLength) LPWSTR ExeNameBuffer,
            # _In_ DWORD ExeNameBufferLength
            # );
            GetConsoleAliasExesW = kernel32.GetConsoleAliasExesW
            GetConsoleAliasExesW.restype = DWORD

            if defined(UNICODE):
                GetConsoleAliasExes = GetConsoleAliasExesW
            else:
                GetConsoleAliasExes = GetConsoleAliasExesA
            # END IF   not UNICODE

        # END IF  _WIN32_WINNT >= 0x0501

        # WINBASEAPI
        # VOID
        # APIENTRY
        # ExpungeConsoleCommandHistoryA(
        # _In_ LPSTR ExeName
        # );
        ExpungeConsoleCommandHistoryA = kernel32.ExpungeConsoleCommandHistoryA
        ExpungeConsoleCommandHistoryA.restype = VOID

        # WINBASEAPI
        # VOID
        # APIENTRY
        # ExpungeConsoleCommandHistoryW(
        # _In_ LPWSTR ExeName
        # );
        ExpungeConsoleCommandHistoryW = kernel32.ExpungeConsoleCommandHistoryW
        ExpungeConsoleCommandHistoryW.restype = VOID

        if defined(UNICODE):
            ExpungeConsoleCommandHistory = ExpungeConsoleCommandHistoryW
        else:
            ExpungeConsoleCommandHistory = ExpungeConsoleCommandHistoryA
        # END IF   not UNICODE

        # WINBASEAPI
        # BOOL
        # APIENTRY
        # SetConsoleNumberOfCommandsA(
        # _In_ DWORD Number,
        # _In_ LPSTR ExeName
        # );
        SetConsoleNumberOfCommandsA = kernel32.SetConsoleNumberOfCommandsA
        SetConsoleNumberOfCommandsA.restype = BOOL

        # WINBASEAPI
        # BOOL
        # APIENTRY
        # SetConsoleNumberOfCommandsW(
        # _In_ DWORD Number,
        # _In_ LPWSTR ExeName
        # );
        SetConsoleNumberOfCommandsW = kernel32.SetConsoleNumberOfCommandsW
        SetConsoleNumberOfCommandsW.restype = BOOL

        if defined(UNICODE):
            SetConsoleNumberOfCommands = SetConsoleNumberOfCommandsW
        else:
            SetConsoleNumberOfCommands = SetConsoleNumberOfCommandsA
        # END IF   not UNICODE

        # WINBASEAPI
        # DWORD
        # APIENTRY
        # GetConsoleCommandHistoryLengthA(
        # _In_ LPSTR ExeName
        # );
        GetConsoleCommandHistoryLengthA = (
            kernel32.GetConsoleCommandHistoryLengthA
        )
        GetConsoleCommandHistoryLengthA.restype = DWORD

        # WINBASEAPI
        # DWORD
        # APIENTRY
        # GetConsoleCommandHistoryLengthW(
        # _In_ LPWSTR ExeName
        # );
        GetConsoleCommandHistoryLengthW = (
            kernel32.GetConsoleCommandHistoryLengthW
        )
        GetConsoleCommandHistoryLengthW.restype = DWORD

        if defined(UNICODE):
            GetConsoleCommandHistoryLength = GetConsoleCommandHistoryLengthW
        else:
            GetConsoleCommandHistoryLength = GetConsoleCommandHistoryLengthA
        # END IF   not UNICODE

        # WINBASEAPI
        # DWORD
        # APIENTRY
        # GetConsoleCommandHistoryA(
        # _Out_writes_bytes_(CommandBufferLength) LPSTR Commands,
        # _In_ DWORD CommandBufferLength,
        # _In_ LPSTR ExeName
        # );
        GetConsoleCommandHistoryA = kernel32.GetConsoleCommandHistoryA
        GetConsoleCommandHistoryA.restype = DWORD

        # WINBASEAPI
        # DWORD
        # APIENTRY
        # GetConsoleCommandHistoryW(
        # _Out_writes_bytes_(CommandBufferLength) LPWSTR Commands,
        # _In_ DWORD CommandBufferLength,
        # _In_ LPWSTR ExeName
        # );
        GetConsoleCommandHistoryW = kernel32.GetConsoleCommandHistoryW
        GetConsoleCommandHistoryW.restype = DWORD

        if defined(UNICODE):
            GetConsoleCommandHistory = GetConsoleCommandHistoryW
        else:
            GetConsoleCommandHistory = GetConsoleCommandHistoryA
        # END IF   not UNICODE

        if _WIN32_WINNT >= 0x0501:
            # WINBASEAPI
            # DWORD
            # APIENTRY
            # GetConsoleProcessList(
            # _Out_writes_(dwProcessCount) LPDWORD lpdwProcessList,
            # _In_ DWORD dwProcessCount
            # );
            GetConsoleProcessList = kernel32.GetConsoleProcessList
            GetConsoleProcessList.restype = DWORD

        # END IF  _WIN32_WINNT >= 0x0501

    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    if defined(__cplusplus):
        pass
    # END IF

# END IF   _APISETCONSOLEL3_
