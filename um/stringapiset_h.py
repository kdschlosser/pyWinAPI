import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_APISETSTRING_ = None



# ******************************************************************************              * stringapi.h -- ApiSet Contract for api-ms-win-core-string-l1   *              * Copyright (c) Microsoft Corporation. All rights reserved.    *              * *****************************************************************************
# 
if defined(_MSC_VER):
    pass
# END IF   _MSC_VER

if not defined(_APISETSTRING_):
    _APISETSTRING_ = VOID
    from pyWinAPI.shared.apiset_h import * # NOQA
    from pyWinAPI.shared.apisetcconv_h import * # NOQA
    from pyWinAPI.shared.minwindef_h import * # NOQA
    from pyWinAPI.um.winnls_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF


    if WINVER >= 0x0600:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # int
            # WINAPI
            # CompareStringEx(
            # _In_opt_ LPCWSTR lpLocaleName,
            # _In_ DWORD dwCmpFlags,
            # _In_NLS_string_(cchCount1) LPCWCH lpString1,
            # _In_ INT cchCount1,
            # _In_NLS_string_(cchCount2) LPCWCH lpString2,
            # _In_ INT cchCount2,
            # _Reserved_ LPNLSVERSIONINFO lpVersionInformation,
            # _Reserved_ LPVOID lpReserved,
            # _Reserved_ LPARAM lParam
            # );
            CompareStringEx = kernel32.CompareStringEx
            CompareStringEx.restype = int


            # WINBASEAPI
            # int
            # WINAPI
            # CompareStringOrdinal(
            # _In_NLS_string_(cchCount1) LPCWCH lpString1,
            # _In_ INT cchCount1,
            # _In_NLS_string_(cchCount2) LPCWCH lpString2,
            # _In_ INT cchCount2,
            # _In_ BOOL bIgnoreCase
            # );
            CompareStringOrdinal = kernel32.CompareStringOrdinal
            CompareStringOrdinal.restype = int
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    # END IF  (WINVER >= 0x0600)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        kernel32 = ctypes.windll.KERNEL32


        # WINBASEAPI
        # int
        # WINAPI
        # CompareStringW(
        # _In_ LCID Locale,
        # _In_ DWORD dwCmpFlags,
        # _In_NLS_string_(cchCount1) PCNZWCH lpString1,
        # _In_ INT cchCount1,
        # _In_NLS_string_(cchCount2) PCNZWCH lpString2,
        # _In_ INT cchCount2
        # );
        CompareStringW = kernel32.CompareStringW
        CompareStringW.restype = int

        if defined(UNICODE):
            CompareString = CompareStringW
        # END IF


        # WINBASEAPI
        # int
        # WINAPI
        # FoldStringW(
        # _In_ DWORD dwMapFlags,
        # _In_NLS_string_(cchSrc) LPCWCH lpSrcStr,
        # _In_ INT cchSrc,
        # _Out_writes_opt_(cchDest) LPWSTR lpDestStr,
        # _In_ INT cchDest
        # );
        FoldStringW = kernel32.FoldStringW
        FoldStringW.restype = int

        if defined(UNICODE):
            FoldString = FoldStringW
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        kernel32 = ctypes.windll.KERNEL32


        # WINBASEAPI
        # BOOL
        # WINAPI
        # GetStringTypeExW(
        # _In_ LCID Locale,
        # _In_ DWORD dwInfoType,
        # _In_NLS_string_(cchSrc) LPCWCH lpSrcStr,
        # _In_ INT cchSrc,
        # _Out_writes_(cchSrc) LPWORD lpCharType
        # );
        GetStringTypeExW = kernel32.GetStringTypeExW
        GetStringTypeExW.restype = BOOL

        if defined(UNICODE):
            GetStringTypeEx = GetStringTypeExW
        # END IF


        # WINBASEAPI
        # BOOL
        # WINAPI
        # GetStringTypeW(
        # _In_ DWORD dwInfoType,
        # _In_NLS_string_(cchSrc) LPCWCH lpSrcStr,
        # _In_ INT cchSrc,
        # _Out_ LPWORD lpCharType
        # );
        GetStringTypeW = kernel32.GetStringTypeW
        GetStringTypeW.restype = BOOL


        # NLS Code Page Dependent APIs.
        # WINBASEAPI
        # _Success_(return != 0)
        # _When_((cbMultiByte == -1) and (cchWideChar != 0), _Post_equal_to_(_String_length_(lpWideCharStr) + 1))
        # int
        # WINAPI
        # MultiByteToWideChar(
        # _In_ UINT CodePage,
        # _In_ DWORD dwFlags,
        # _In_NLS_string_(cbMultiByte) LPCCH lpMultiByteStr,
        # _In_ INT cbMultiByte,
        # _Out_writes_to_opt_(cchWideChar,return) LPWSTR lpWideCharStr,
        # _In_ INT cchWideChar
        # );
        MultiByteToWideChar = kernel32.MultiByteToWideChar
        MultiByteToWideChar.restype = int


        # WINBASEAPI
        # _Success_(return != 0)
        # _When_((cchWideChar == -1) and (cbMultiByte != 0), _Post_equal_to_(_String_length_(lpMultiByteStr) + 1))
        # int
        # WINAPI
        # WideCharToMultiByte(
        # _In_ UINT CodePage,
        # _In_ DWORD dwFlags,
        # _In_NLS_string_(cchWideChar) LPCWCH lpWideCharStr,
        # _In_ INT cchWideChar,
        # _Out_writes_bytes_to_opt_(cbMultiByte,return) LPSTR lpMultiByteStr,
        # _In_ INT cbMultiByte,
        # _In_opt_ LPCCH lpDefaultChar,
        # _Out_opt_ LPBOOL lpUsedDefaultChar
        # );
        WideCharToMultiByte = kernel32.WideCharToMultiByte
        WideCharToMultiByte.restype = int
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if defined(__cplusplus):
        pass
    # END IF

# END IF   _APISETSTRING_


