import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_APISETLIBLOADER_ = None
STRICT = None

class tagENUMUILANG(ctypes.Structure):
    pass


ENUMUILANG = tagENUMUILANG
PENUMUILANG = POINTER(tagENUMUILANG)




# ******************************************************************************              * libloaderapi.h -- ApiSet Contract for api-ms-win-core-libraryloader-l1  *              * Copyright (c) Microsoft Corporation. All rights reserved.    *              * *****************************************************************************
# 
if defined(_MSC_VER):
    pass
# END IF   _MSC_VER

if not defined(_APISETLIBLOADER_):
    _APISETLIBLOADER_ = VOID
    from pyWinAPI.shared.apiset_h import * # NOQA
    from pyWinAPI.shared.apisetcconv_h import * # NOQA
    from pyWinAPI.shared.minwindef_h import * # NOQA
    from pyWinAPI.um.minwinbase_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        FIND_RESOURCE_DIRECTORY_TYPES = 0x0100
        FIND_RESOURCE_DIRECTORY_NAMES = 0x0200
        FIND_RESOURCE_DIRECTORY_LANGUAGES = 0x0400
        RESOURCE_ENUM_LN = 0x0001
        RESOURCE_ENUM_MUI = 0x0002
        RESOURCE_ENUM_MUI_SYSTEM = 0x0004
        RESOURCE_ENUM_VALIDATE = 0x0008
        RESOURCE_ENUM_MODULE_EXACT = 0x0010
        SUPPORT_LANG_NUMBER = 32


        # Acutall number of enumerated languages
        tagENUMUILANG._fields_ = [
            ('NumOfEnumUILang', ULONG),
            # Buffer size of pMUIEnumUILanguages
            ('SizeOfEnumUIBuffer', ULONG),
            ('pEnumUIBuffer', POINTER(LANGID)),
        ]
        if defined(STRICT):
            # BOOL (CALLBACK* ENUMRESLANGPROCA)( _In_opt_ HMODULE hModule, _In_ LPCSTR lpType, _In_ LPCSTR lpName, _In_ WORD wLanguage, _In_ LONG_PTR lParam);
            ENUMRESLANGPROCA = CALLBACK(
                BOOL,
                HMODULE,
                LPCSTR,
                LPCSTR,
                WORD,
                LONG_PTR,
            )


            # BOOL (CALLBACK* ENUMRESLANGPROCW)( _In_opt_ HMODULE hModule, _In_ LPCWSTR lpType, _In_ LPCWSTR lpName, _In_ WORD wLanguage, _In_ LONG_PTR lParam);
            ENUMRESLANGPROCW = CALLBACK(
                BOOL,
                HMODULE,
                LPCWSTR,
                LPCWSTR,
                WORD,
                LONG_PTR,
            )


            if defined(UNICODE):
                ENUMRESLANGPROC = ENUMRESLANGPROCW
            else:
                ENUMRESLANGPROC = ENUMRESLANGPROCA
            # END IF   not UNICODE

            # BOOL (CALLBACK* ENUMRESNAMEPROCA)( _In_opt_ HMODULE hModule, _In_ LPCSTR lpType, _In_ LPSTR lpName, _In_ LONG_PTR lParam);
            ENUMRESNAMEPROCA = CALLBACK(
                BOOL,
                HMODULE,
                LPCSTR,
                LPSTR,
                LONG_PTR,
            )


            # BOOL (CALLBACK* ENUMRESNAMEPROCW)( _In_opt_ HMODULE hModule, _In_ LPCWSTR lpType, _In_ LPWSTR lpName, _In_ LONG_PTR lParam);
            ENUMRESNAMEPROCW = CALLBACK(
                BOOL,
                HMODULE,
                LPCWSTR,
                LPWSTR,
                LONG_PTR,
            )


            if defined(UNICODE):
                ENUMRESNAMEPROC = ENUMRESNAMEPROCW
            else:
                ENUMRESNAMEPROC = ENUMRESNAMEPROCA
            # END IF   not UNICODE

            # BOOL (CALLBACK* ENUMRESTYPEPROCA)( _In_opt_ HMODULE hModule, _In_ LPSTR lpType, _In_ LONG_PTR lParam );
            ENUMRESTYPEPROCA = CALLBACK(
                BOOL,
                HMODULE,
                LPSTR,
                LONG_PTR,
            )


            # BOOL (CALLBACK* ENUMRESTYPEPROCW)( _In_opt_ HMODULE hModule, _In_ LPWSTR lpType, _In_ LONG_PTR lParam );
            ENUMRESTYPEPROCW = CALLBACK(
                BOOL,
                HMODULE,
                LPWSTR,
                LONG_PTR,
            )


            if defined(UNICODE):
                ENUMRESTYPEPROC = ENUMRESTYPEPROCW
            else:
                ENUMRESTYPEPROC = ENUMRESTYPEPROCA
            # END IF   not UNICODE

        else:
            ENUMRESTYPEPROCA = FARPROC
            ENUMRESTYPEPROCW = FARPROC
            if defined(UNICODE):
                ENUMRESTYPEPROC = ENUMRESTYPEPROCW
            else:
                ENUMRESTYPEPROC = ENUMRESTYPEPROCA
            # END IF   UNICODE

            ENUMRESNAMEPROCA = FARPROC
            ENUMRESNAMEPROCW = FARPROC
            if defined(UNICODE):
                ENUMRESNAMEPROC = ENUMRESNAMEPROCW
            else:
                ENUMRESNAMEPROC = ENUMRESNAMEPROCA
            # END IF   UNICODE

            ENUMRESLANGPROCA = FARPROC
            ENUMRESLANGPROCW = FARPROC
            if defined(UNICODE):
                ENUMRESLANGPROC = ENUMRESLANGPROCW
            else:
                ENUMRESLANGPROC = ENUMRESLANGPROCA
            # END IF   UNICODE
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        kernel32 = ctypes.windll.KERNEL32


        # WINBASEAPI
        # BOOL
        # WINAPI
        # DisableThreadLibraryCalls(
        # _In_ HMODULE hLibModule
        # );
        DisableThreadLibraryCalls = kernel32.DisableThreadLibraryCalls
        DisableThreadLibraryCalls.restype = BOOL

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        kernel32 = ctypes.windll.KERNEL32


        # WINBASEAPI
        # _Ret_maybenull_
        # HRSRC
        # WINAPI
        # FindResourceExW(
        # _In_opt_ HMODULE hModule,
        # _In_ LPCWSTR lpType,
        # _In_ LPCWSTR lpName,
        # _In_ WORD wLanguage
        # );
        FindResourceExW = kernel32.FindResourceExW
        FindResourceExW.restype = HRSRC

        if defined(UNICODE):
            FindResourceEx = FindResourceExW
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if _WIN32_WINNT >= _WIN32_WINNT_WIN7:
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # int
            # WINAPI
            # FindStringOrdinal(
            # _In_ DWORD dwFindStringOrdinalFlags,
            # _In_reads_(cchSource) LPCWSTR lpStringSource,
            # _In_ INT cchSource,
            # _In_reads_(cchValue) LPCWSTR lpStringValue,
            # _In_ INT cchValue,
            # _In_ BOOL bIgnoreCase
            # );
            FindStringOrdinal = kernel32.FindStringOrdinal
            FindStringOrdinal.restype = int

        # END IF   (_WIN32_WINNT >= _WIN32_WINNT_WIN7)


        # WINBASEAPI
        # BOOL
        # WINAPI
        # FreeLibrary(
        # _In_ HMODULE hLibModule
        # );
        FreeLibrary = kernel32.FreeLibrary
        FreeLibrary.restype = BOOL


        # WINBASEAPI
        # DECLSPEC_NORETURN
        # VOID
        # WINAPI
        # FreeLibraryAndExitThread(
        # _In_ HMODULE hLibModule,
        # _In_ DWORD dwExitCode
        # );
        FreeLibraryAndExitThread = kernel32.FreeLibraryAndExitThread
        FreeLibraryAndExitThread.restype = VOID
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        kernel32 = ctypes.windll.KERNEL32


        # WINBASEAPI
        # BOOL
        # WINAPI
        # FreeResource(
        # _In_ HGLOBAL hResData
        # );
        FreeResource = kernel32.FreeResource
        FreeResource.restype = BOOL

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        kernel32 = ctypes.windll.KERNEL32


        # WINBASEAPI
        # _Success_(return != 0)
        # _Ret_range_(1,nSize)
        # DWORD
        # WINAPI
        # GetModuleFileNameA(
        # _In_opt_ HMODULE hModule,
        # _Out_writes_to_(nSize,((return < nSize) ? (return + 1) : nSize)) LPSTR lpFilename,
        # _In_ DWORD nSize
        # );
        GetModuleFileNameA = kernel32.GetModuleFileNameA
        GetModuleFileNameA.restype = DWORD


        # WINBASEAPI
        # _Success_(return != 0)
        # _Ret_range_(1,nSize)
        # DWORD
        # WINAPI
        # GetModuleFileNameW(
        # _In_opt_ HMODULE hModule,
        # _Out_writes_to_(nSize,((return < nSize) ? (return + 1) : nSize)) LPWSTR lpFilename,
        # _In_ DWORD nSize
        # );
        GetModuleFileNameW = kernel32.GetModuleFileNameW
        GetModuleFileNameW.restype = DWORD

        if defined(UNICODE):
            GetModuleFileName = GetModuleFileNameW
        else:
            GetModuleFileName = GetModuleFileNameA
        # END IF   not UNICODE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        kernel32 = ctypes.windll.KERNEL32


        # WINBASEAPI
        # _When_(lpModuleName == NULL,_Ret_notnull_)
        # _When_(lpModuleName != NULL,_Ret_maybenull_)
        # HMODULE
        # WINAPI
        # GetModuleHandleA(
        # _In_opt_ LPCSTR lpModuleName
        # );
        GetModuleHandleA = kernel32.GetModuleHandleA
        GetModuleHandleA.restype = HMODULE


        # WINBASEAPI
        # _When_(lpModuleName == NULL,_Ret_notnull_)
        # _When_(lpModuleName != NULL,_Ret_maybenull_)
        # HMODULE
        # WINAPI
        # GetModuleHandleW(
        # _In_opt_ LPCWSTR lpModuleName
        # );
        GetModuleHandleW = kernel32.GetModuleHandleW
        GetModuleHandleW.restype = HMODULE

        if defined(UNICODE):
            GetModuleHandle = GetModuleHandleW
        else:
            GetModuleHandle = GetModuleHandleA
        # END IF   not UNICODE

        if not defined(RC_INVOKED):
            GET_MODULE_HANDLE_EX_FLAG_PIN = 0x00000001
            GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT = 0x00000002
            GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS = 0x00000004

            # BOOL (WINAPI* PGET_MODULE_HANDLE_EXA)( _In_        DWORD        dwFlags, _In_opt_    LPCSTR     lpModuleName, _Outptr_ HMODULE*    phModule );
            PGET_MODULE_HANDLE_EXA = WINAPI(
                BOOL,
                ,
                ,
                ,
            )


            # BOOL (WINAPI* PGET_MODULE_HANDLE_EXW)( _In_        DWORD        dwFlags, _In_opt_    LPCWSTR     lpModuleName, _Outptr_ HMODULE*    phModule );
            PGET_MODULE_HANDLE_EXW = WINAPI(
                BOOL,
                ,
                ,
                ,
            )


            if defined(UNICODE):

Traceback (most recent call last):
  File "C:/Stackless27/Lib/site-packages/pyWinAPI/code_converter/__init__.py", line 1726, in run
    gen_code(input_file)
  File "C:/Stackless27/Lib/site-packages/pyWinAPI/code_converter/__init__.py", line 1187, in gen_code
    if func[i + 1] == ';':
IndexError: string index out of range
