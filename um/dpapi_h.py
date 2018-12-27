import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__DPAPI_H__ = None
DPAPI_IMP = None
_CRYPT32_ = None
CRYPTO_BLOBS_DEFINED = None


class _CRYPTOAPI_BLOB(ctypes.Structure):
    pass


CRYPT_INTEGER_BLOB = _CRYPTOAPI_BLOB
PCRYPT_INTEGER_BLOB = POINTER(_CRYPTOAPI_BLOB)
CRYPT_UINT_BLOB = _CRYPTOAPI_BLOB
PCRYPT_UINT_BLOB = POINTER(_CRYPTOAPI_BLOB)
CRYPT_OBJID_BLOB = _CRYPTOAPI_BLOB
PCRYPT_OBJID_BLOB = POINTER(_CRYPTOAPI_BLOB)
CERT_NAME_BLOB = _CRYPTOAPI_BLOB
PCERT_NAME_BLOB = POINTER(_CRYPTOAPI_BLOB)
CERT_RDN_VALUE_BLOB = _CRYPTOAPI_BLOB
PCERT_RDN_VALUE_BLOB = POINTER(_CRYPTOAPI_BLOB)
CERT_BLOB = _CRYPTOAPI_BLOB
PCERT_BLOB = POINTER(_CRYPTOAPI_BLOB)
CRL_BLOB = _CRYPTOAPI_BLOB
PCRL_BLOB = POINTER(_CRYPTOAPI_BLOB)
DATA_BLOB = _CRYPTOAPI_BLOB
PDATA_BLOB = POINTER(_CRYPTOAPI_BLOB)
CRYPT_DATA_BLOB = _CRYPTOAPI_BLOB
PCRYPT_DATA_BLOB = POINTER(_CRYPTOAPI_BLOB)
CRYPT_HASH_BLOB = _CRYPTOAPI_BLOB
PCRYPT_HASH_BLOB = POINTER(_CRYPTOAPI_BLOB)
CRYPT_DIGEST_BLOB = _CRYPTOAPI_BLOB
PCRYPT_DIGEST_BLOB = POINTER(_CRYPTOAPI_BLOB)
CRYPT_DER_BLOB = _CRYPTOAPI_BLOB
PCRYPT_DER_BLOB = POINTER(_CRYPTOAPI_BLOB)
CRYPT_ATTR_BLOB = _CRYPTOAPI_BLOB
PCRYPT_ATTR_BLOB = POINTER(_CRYPTOAPI_BLOB)


class _CRYPTPROTECT_PROMPTSTRUCT(ctypes.Structure):
    pass


CRYPTPROTECT_PROMPTSTRUCT = _CRYPTPROTECT_PROMPTSTRUCT
PCRYPTPROTECT_PROMPTSTRUCT = POINTER(_CRYPTPROTECT_PROMPTSTRUCT)

# + ---------------------------------------------------------------------------
# Microsoft Windows
# Copyright (C) Microsoft Corporation, 2009.
# File:  dpapi.h
# Contents: Data Protection API
# ----------------------------------------------------------------------------
if not defined(__DPAPI_H__):
    __DPAPI_H__ = VOID
    if _MSC_VER > 1020:
        pass
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN8:
        if not defined(DPAPI_IMP):
            DPAPI_IMP = VOID
        # END IF
    else:
        if not defined(_CRYPT32_):
            DPAPI_IMP = DECLSPEC_IMPORT
        else:
            DPAPI_IMP = VOID
        # END IF
    # END IF  (NTDDI_VERSION >= NTDDI_WIN7)

    if defined(__cplusplus):
        pass
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(CRYPTO_BLOBS_DEFINED):
            CRYPTO_BLOBS_DEFINED = VOID

            _CRYPTOAPI_BLOB._fields_ = [
                ('cbData', DWORD),
                ('pbData', POINTER(BYTE)),
            ]
        # END IF

        # Registry value for controlling Data Protection API (DPAPI) UI
        # settings.
        szFORCE_KEY_PROTECTION = "ForceKeyProtection"
        dwFORCE_KEY_PROTECTION_DISABLED = 0x0
        dwFORCE_KEY_PROTECTION_USER_SELECT = 0x1
        dwFORCE_KEY_PROTECTION_HIGH = 0x2

        # Data protection APIs enable applications to easily secure data.
        # The base provider provides protection based on the users' logon
        # credentials. The data secured with these APIs follow the same
        # roaming characteristics as HKCU -- if HKCU roams, the data
        # protected by the base provider may roam as well. This makes
        # the API ideal for the munging of data stored in the registry.
        # Prompt struct -- what to tell users about the access
        _CRYPTPROTECT_PROMPTSTRUCT._fields_ = [
            ('cbSize', DWORD),
            ('dwPromptFlags', DWORD),
            ('hwndApp', HWND),
            ('szPrompt', LPCWSTR),
        ]

        # base provider action
        CRYPTPROTECT_DEFAULT_PROVIDER = [
            0xDF9D8CD0,
            0x1501,
            0x11D1,
            [0x8C, 0x7A, 0x00, 0xC0, 0x4F, 0xC2, 0x97, 0xEB],
        ]

        # CryptProtect PromptStruct dwPromtFlags
        # prompt on unprotect
        CRYPTPROTECT_PROMPT_ON_UNPROTECT = 0x1        # 1 << 0

        # prompt on protect
        CRYPTPROTECT_PROMPT_ON_PROTECT = 0x2        # 1 << 1
        CRYPTPROTECT_PROMPT_RESERVED = 0x04        # reserved, do not use.

        # default to strong variant UI protection
        # (user supplied password currently).
        CRYPTPROTECT_PROMPT_STRONG = 0x08        # 1 << 3

        # require strong variant UI protection
        # (user supplied password currently).
        CRYPTPROTECT_PROMPT_REQUIRE_STRONG = 0x10        # 1 << 4

        # CryptProtectData and CryptUnprotectData dwFlags
        # for remote-access situations where ui is not an option
        # if UI was specified on protect or unprotect operation, the call
        # will fail and GetLastError() will indicate ERROR_PASSWORD_RESTRICTION
        CRYPTPROTECT_UI_FORBIDDEN = 0x1

        # per machine protected data -- any user on machine where
        # CryptProtectData
        # took place may CryptUnprotectData
        CRYPTPROTECT_LOCAL_MACHINE = 0x4

        # force credential synchronize during CryptProtectData()
        # Synchronize is only operation that occurs during this operation
        CRYPTPROTECT_CRED_SYNC = 0x8

        # Generate an Audit on protect and unprotect operations
        CRYPTPROTECT_AUDIT = 0x10

        # Protect data with a non-recoverable key
        CRYPTPROTECT_NO_RECOVERY = 0x20

        # Verify the protection of a protected blob
        CRYPTPROTECT_VERIFY_PROTECTION = 0x40

        # Regenerate the local machine protection
        CRYPTPROTECT_CRED_REGENERATE = 0x80

        # flags reserved for system use
        CRYPTPROTECT_FIRST_RESERVED_FLAGVAL = 0x0FFFFFFF
        CRYPTPROTECT_LAST_RESERVED_FLAGVAL = 0xFFFFFFFF

        # flags specific to base provider
        crypt32 = ctypes.windll.CRYPT32

        # DPAPI_IMP
        # BOOL
        # WINAPI
        # CryptProtectData(
        # _In_            DATA_BLOB*      pDataIn,
        # _In_opt_        LPCWSTR         szDataDescr,
        # _In_opt_        DATA_BLOB*      pOptionalEntropy,
        # _Reserved_      PVOID           pvReserved,
        # _In_opt_        CRYPTPROTECT_PROMPTSTRUCT*  pPromptStruct,
        # _In_            DWORD           dwFlags,
        # _Out_           DATA_BLOB*      pDataOut // out encr blob
        # );
        CryptProtectData = crypt32.CryptProtectData
        CryptProtectData.restype = BOOL

        # DPAPI_IMP
        # BOOL
        # WINAPI
        # CryptUnprotectData(
        # _In_            DATA_BLOB*      pDataIn, // in encr blob
        # _Outptr_opt_result_maybenull_ LPWSTR*     ppszDataDescr, // out
        # _In_opt_        DATA_BLOB*      pOptionalEntropy,
        # _Reserved_      PVOID           pvReserved,
        # _In_opt_        CRYPTPROTECT_PROMPTSTRUCT*  pPromptStruct,
        # _In_            DWORD           dwFlags,
        # _Out_           DATA_BLOB*      pDataOut
        # );
        CryptUnprotectData = crypt32.CryptUnprotectData
        CryptUnprotectData.restype = BOOL
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if NTDDI_VERSION >= NTDDI_WIN8:
            # out encr blo
            # b
            # in encr blob
            # out
            # END IF
            pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if NTDDI_VERSION >= NTDDI_VISTA:
            crypt32 = ctypes.windll.CRYPT32

            # DPAPI_IMP
            # BOOL
            # WINAPI
            # CryptUpdateProtectedState(
            # _In_opt_        PSID            pOldSid,
            # _In_opt_        LPCWSTR         pwszOldPassword,
            # _In_            DWORD           dwFlags,
            # _Out_opt_       DWORD           *pdwSuccessCount,
            # _Out_opt_       DWORD           *pdwFailureCount);
            CryptUpdateProtectedState = crypt32.CryptUpdateProtectedState
            CryptUpdateProtectedState.restype = BOOL
        # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # The buffer length passed into CryptProtectMemory and
        # CryptUnprotectMemory
        # must be a multiple of this length (or zero).
        CRYPTPROTECTMEMORY_BLOCK_SIZE = 16

        # CryptProtectMemory/CryptUnprotectMemory dwFlags
        # Encrypt/Decrypt within current process context.
        CRYPTPROTECTMEMORY_SAME_PROCESS = 0x00

        # Encrypt/Decrypt across process boundaries.
        # eg: encrypted buffer passed across LPC to another process which
        # calls CryptUnprotectMemory.
        CRYPTPROTECTMEMORY_CROSS_PROCESS = 0x01

        # Encrypt/Decrypt across callers with same LogonId.
        # eg: encrypted buffer passed across LPC to another process which
        # calls CryptUnprotectMemory whilst impersonating.
        CRYPTPROTECTMEMORY_SAME_LOGON = 0x02
        crypt32 = ctypes.windll.CRYPT32

        # DPAPI_IMP
        # BOOL
        # WINAPI
        # CryptProtectMemory(
        # _Inout_         LPVOID          pDataIn, // in out data to encrypt
        # _In_            DWORD           cbDataIn, // multiple of CRYPTPROTECTMEMORY_BLOCK_SIZE
        # _In_            DWORD           dwFlags
        # );
        CryptProtectMemory = crypt32.CryptProtectMemory
        CryptProtectMemory.restype = BOOL

        # DPAPI_IMP
        # BOOL
        # WINAPI
        # CryptUnprotectMemory(
        # _Inout_         LPVOID          pDataIn, // in out data to decrypt
        # _In_            DWORD           cbDataIn, // multiple of CRYPTPROTECTMEMORY_BLOCK_SIZE
        # _In_            DWORD           dwFlags
        # );
        CryptUnprotectMemory = crypt32.CryptUnprotectMemory
        CryptUnprotectMemory.restype = BOOL

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if defined(__cplusplus):
        # extern "C"
        pass
    # END IF
# END IF   __DPAPI_H__


