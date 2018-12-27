import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__NCRYPT_H__ = None
WINAPI = None
__SECSTATUS_DEFINED__ = None
HCRYPTPROV_DEFINED = None

class NCRYPT_ALLOC_PARA(ctypes.Structure):
    pass


class _NCRYPT_PLATFORM_ATTEST_PADDING_INFO(ctypes.Structure):
    pass


NCRYPT_PLATFORM_ATTEST_PADDING_INFO = _NCRYPT_PLATFORM_ATTEST_PADDING_INFO


class _NCRYPT_KEY_ATTEST_PADDING_INFO(ctypes.Structure):
    pass


NCRYPT_KEY_ATTEST_PADDING_INFO = _NCRYPT_KEY_ATTEST_PADDING_INFO


class _NCRYPT_ISOLATED_KEY_ATTESTED_ATTRIBUTES(ctypes.Structure):
    pass


NCRYPT_ISOLATED_KEY_ATTESTED_ATTRIBUTES = _NCRYPT_ISOLATED_KEY_ATTESTED_ATTRIBUTES
PNCRYPT_ISOLATED_KEY_ATTESTED_ATTRIBUTES = POINTER(_NCRYPT_ISOLATED_KEY_ATTESTED_ATTRIBUTES)


class _NCRYPT_VSM_KEY_ATTESTATION_STATEMENT(ctypes.Structure):
    pass


NCRYPT_VSM_KEY_ATTESTATION_STATEMENT = _NCRYPT_VSM_KEY_ATTESTATION_STATEMENT
PNCRYPT_VSM_KEY_ATTESTATION_STATEMENT = POINTER(_NCRYPT_VSM_KEY_ATTESTATION_STATEMENT)


class _NCRYPT_VSM_KEY_ATTESTATION_CLAIM_RESTRICTIONS(ctypes.Structure):
    pass


NCRYPT_VSM_KEY_ATTESTATION_CLAIM_RESTRICTIONS = _NCRYPT_VSM_KEY_ATTESTATION_CLAIM_RESTRICTIONS
PNCRYPT_VSM_KEY_ATTESTATION_CLAIM_RESTRICTIONS = POINTER(_NCRYPT_VSM_KEY_ATTESTATION_CLAIM_RESTRICTIONS)


class _NCRYPT_EXPORTED_ISOLATED_KEY_HEADER(ctypes.Structure):
    pass


NCRYPT_EXPORTED_ISOLATED_KEY_HEADER = _NCRYPT_EXPORTED_ISOLATED_KEY_HEADER
PNCRYPT_EXPORTED_ISOLATED_KEY_HEADER = POINTER(_NCRYPT_EXPORTED_ISOLATED_KEY_HEADER)


class _NCRYPT_EXPORTED_ISOLATED_KEY_ENVELOPE(ctypes.Structure):
    pass


NCRYPT_EXPORTED_ISOLATED_KEY_ENVELOPE = _NCRYPT_EXPORTED_ISOLATED_KEY_ENVELOPE
PNCRYPT_EXPORTED_ISOLATED_KEY_ENVELOPE = POINTER(_NCRYPT_EXPORTED_ISOLATED_KEY_ENVELOPE)


class __NCRYPT_PCP_TPM_WEB_AUTHN_ATTESTATION_STATEMENT(ctypes.Structure):
    pass


NCRYPT_PCP_TPM_WEB_AUTHN_ATTESTATION_STATEMENT = __NCRYPT_PCP_TPM_WEB_AUTHN_ATTESTATION_STATEMENT
PNCRYPT_PCP_TPM_WEB_AUTHN_ATTESTATION_STATEMENT = POINTER(__NCRYPT_PCP_TPM_WEB_AUTHN_ATTESTATION_STATEMENT)


class _NCRYPT_CIPHER_PADDING_INFO(ctypes.Structure):
    pass


NCRYPT_CIPHER_PADDING_INFO = _NCRYPT_CIPHER_PADDING_INFO
PNCRYPT_CIPHER_PADDING_INFO = POINTER(_NCRYPT_CIPHER_PADDING_INFO)


class _NCryptAlgorithmName(ctypes.Structure):
    pass


NCryptAlgorithmName = _NCryptAlgorithmName


class NCryptKeyName(ctypes.Structure):
    pass


class NCryptProviderName(ctypes.Structure):
    pass


class __NCRYPT_UI_POLICY(ctypes.Structure):
    pass


NCRYPT_UI_POLICY = __NCRYPT_UI_POLICY


class __NCRYPT_KEY_ACCESS_POLICY_BLOB(ctypes.Structure):
    pass


NCRYPT_KEY_ACCESS_POLICY_BLOB = __NCRYPT_KEY_ACCESS_POLICY_BLOB


class __NCRYPT_SUPPORTED_LENGTHS(ctypes.Structure):
    pass


NCRYPT_SUPPORTED_LENGTHS = __NCRYPT_SUPPORTED_LENGTHS


class __NCRYPT_PCP_HMAC_AUTH_SIGNATURE_INFO(ctypes.Structure):
    pass


NCRYPT_PCP_HMAC_AUTH_SIGNATURE_INFO = __NCRYPT_PCP_HMAC_AUTH_SIGNATURE_INFO


class __NCRYPT_PCP_TPM_FW_VERSION_INFO(ctypes.Structure):
    pass


NCRYPT_PCP_TPM_FW_VERSION_INFO = __NCRYPT_PCP_TPM_FW_VERSION_INFO


class __NCRYPT_PCP_RAW_POLICYDIGEST(ctypes.Structure):
    pass


NCRYPT_PCP_RAW_POLICYDIGEST_INFO = __NCRYPT_PCP_RAW_POLICYDIGEST


class _NCRYPT_KEY_BLOB_HEADER(ctypes.Structure):
    pass


NCRYPT_KEY_BLOB_HEADER = _NCRYPT_KEY_BLOB_HEADER
PNCRYPT_KEY_BLOB_HEADER = POINTER(_NCRYPT_KEY_BLOB_HEADER)


class NCRYPT_TPM_LOADABLE_KEY_BLOB_HEADER(ctypes.Structure):
    pass


PNCRYPT_TPM_LOADABLE_KEY_BLOB_HEADER = POINTER(NCRYPT_TPM_LOADABLE_KEY_BLOB_HEADER)



from pyWinAPI.shared.winapifamily_h import * # NOQA

# + ---------------------------------------------------------------------------
# Microsoft Windows
# Copyright (C) Microsoft Corporation, 2004.
# File:  ncrypt.h
# Contents: Cryptographic API Prototypes and Definitions
# ----------------------------------------------------------------------------
if not defined(__NCRYPT_H__):
    __NCRYPT_H__ = VOID
    if _MSC_VER >= 1200:
        pass
    # END IF

    if defined(__cplusplus):
        pass
    # END IF


    if not defined(WINAPI):
        WINAPI = ctypes.WINFUNCTYPE
    # END IF

    if not defined(__SECSTATUS_DEFINED__):
        SECURITY_STATUS = LONG
        __SECSTATUS_DEFINED__ = VOID
    # END IF

    from pyWinAPI.shared.bcrypt_h import * # NOQA

    if not defined(HCRYPTPROV_DEFINED):
        HCRYPTPROV_DEFINED = VOID
        HCRYPTPROV = ULONG_PTR
        HCRYPTKEY = ULONG_PTR
        HCRYPTHASH = ULONG_PTR
    # END IF

    # Maximum length of Key name, in characters
    NCRYPT_MAX_KEY_NAME_LENGTH = 512

    # Maximum length of Algorithm name, in characters
    NCRYPT_MAX_ALG_ID_LENGTH = 512

    # *************************************************************************
    # NCRYPT memory management routines for functions that require the caller
    # to allocate memory
    # *************************************************************************
    #
    # typedef LPVOID (WINAPI *PFN_NCRYPT_ALLOC)(
    # _In_ SIZE_T cbSize
    # );
    PFN_NCRYPT_ALLOC = WINAPI(
        LPVOID,
        SIZE_T,
    )

    # typedef VOID (WINAPI *PFN_NCRYPT_FREE)(
    # _In_ LPVOID pv
    # );
    PFN_NCRYPT_FREE = WINAPI(
        VOID,
        LPVOID,
    )

    # size of this structure
    NCRYPT_ALLOC_PARA._fields_ = [
        ('cbSize', DWORD),
        ('pfnAlloc', PFN_NCRYPT_ALLOC),
        ('pfnFree', PFN_NCRYPT_FREE),
    ]

    # Microsoft built-in providers.
    MS_KEY_STORAGE_PROVIDER = "Microsoft Software Key Storage Provider"
    MS_SMART_CARD_KEY_STORAGE_PROVIDER = (
        "Microsoft Smart Card Key Storage Provider"
    )
    MS_PLATFORM_KEY_STORAGE_PROVIDER = "Microsoft Platform Crypto Provider"
    MS_NGC_KEY_STORAGE_PROVIDER = "Microsoft Passport Key Storage Provider"

    # Key name for sealing
    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        TPM_RSA_SRK_SEAL_KEY = (
            "MICROSOFT_PCP_KSP_RSA_SEAL_KEY_3BD1C4BF-004E-4E2F-8A4D-0BF633DCB074"
        )
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS1)

    # Common algorithm identifiers.
    NCRYPT_RSA_ALGORITHM = BCRYPT_RSA_ALGORITHM
    NCRYPT_RSA_SIGN_ALGORITHM = BCRYPT_RSA_SIGN_ALGORITHM
    NCRYPT_DH_ALGORITHM = BCRYPT_DH_ALGORITHM
    NCRYPT_DSA_ALGORITHM = BCRYPT_DSA_ALGORITHM
    NCRYPT_MD2_ALGORITHM = BCRYPT_MD2_ALGORITHM
    NCRYPT_MD4_ALGORITHM = BCRYPT_MD4_ALGORITHM
    NCRYPT_MD5_ALGORITHM = BCRYPT_MD5_ALGORITHM
    NCRYPT_SHA1_ALGORITHM = BCRYPT_SHA1_ALGORITHM
    NCRYPT_SHA256_ALGORITHM = BCRYPT_SHA256_ALGORITHM
    NCRYPT_SHA384_ALGORITHM = BCRYPT_SHA384_ALGORITHM
    NCRYPT_SHA512_ALGORITHM = BCRYPT_SHA512_ALGORITHM
    NCRYPT_ECDSA_P256_ALGORITHM = BCRYPT_ECDSA_P256_ALGORITHM
    NCRYPT_ECDSA_P384_ALGORITHM = BCRYPT_ECDSA_P384_ALGORITHM
    NCRYPT_ECDSA_P521_ALGORITHM = BCRYPT_ECDSA_P521_ALGORITHM
    NCRYPT_ECDH_P256_ALGORITHM = BCRYPT_ECDH_P256_ALGORITHM
    NCRYPT_ECDH_P384_ALGORITHM = BCRYPT_ECDH_P384_ALGORITHM
    NCRYPT_ECDH_P521_ALGORITHM = BCRYPT_ECDH_P521_ALGORITHM

    if NTDDI_VERSION >= NTDDI_WIN8:
        NCRYPT_AES_ALGORITHM = BCRYPT_AES_ALGORITHM
        NCRYPT_RC2_ALGORITHM = BCRYPT_RC2_ALGORITHM
        NCRYPT_3DES_ALGORITHM = BCRYPT_3DES_ALGORITHM
        NCRYPT_DES_ALGORITHM = BCRYPT_DES_ALGORITHM
        NCRYPT_DESX_ALGORITHM = BCRYPT_DESX_ALGORITHM
        NCRYPT_3DES_112_ALGORITHM = BCRYPT_3DES_112_ALGORITHM
        NCRYPT_SP800108_CTR_HMAC_ALGORITHM = BCRYPT_SP800108_CTR_HMAC_ALGORITHM
        NCRYPT_SP80056A_CONCAT_ALGORITHM = BCRYPT_SP80056A_CONCAT_ALGORITHM
        NCRYPT_PBKDF2_ALGORITHM = BCRYPT_PBKDF2_ALGORITHM
        NCRYPT_CAPI_KDF_ALGORITHM = BCRYPT_CAPI_KDF_ALGORITHM
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        NCRYPT_ECDSA_ALGORITHM = BCRYPT_ECDSA_ALGORITHM
        NCRYPT_ECDH_ALGORITHM = BCRYPT_ECDH_ALGORITHM
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    NCRYPT_KEY_STORAGE_ALGORITHM = "KEY_STORAGE"

    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        # This algorithm is not supported by any BCrypt provider. This
        # identifier is for creating
        # persistent stored HMAC keys in the TPM KSP.
        NCRYPT_HMAC_SHA256_ALGORITHM = "HMAC-SHA256"
    # END IF


    # Interfaces
    if NTDDI_VERSION >= NTDDI_WIN8:
        NCRYPT_CIPHER_INTERFACE = BCRYPT_CIPHER_INTERFACE
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    NCRYPT_HASH_INTERFACE = BCRYPT_HASH_INTERFACE
    NCRYPT_ASYMMETRIC_ENCRYPTION_INTERFACE = (
        BCRYPT_ASYMMETRIC_ENCRYPTION_INTERFACE
    )
    NCRYPT_SECRET_AGREEMENT_INTERFACE = BCRYPT_SECRET_AGREEMENT_INTERFACE
    NCRYPT_SIGNATURE_INTERFACE = BCRYPT_SIGNATURE_INTERFACE

    if NTDDI_VERSION >= NTDDI_WIN8:
        NCRYPT_KEY_DERIVATION_INTERFACE = BCRYPT_KEY_DERIVATION_INTERFACE
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    NCRYPT_KEY_STORAGE_INTERFACE = 0x00010001
    NCRYPT_SCHANNEL_INTERFACE = 0x00010002

    if NTDDI_VERSION >= NTDDI_WIN7:
        NCRYPT_SCHANNEL_SIGNATURE_INTERFACE = 0x00010003
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN8:
        NCRYPT_KEY_PROTECTION_INTERFACE = 0x00010004
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    # algorithm groups.
    NCRYPT_RSA_ALGORITHM_GROUP = NCRYPT_RSA_ALGORITHM
    NCRYPT_DH_ALGORITHM_GROUP = NCRYPT_DH_ALGORITHM
    NCRYPT_DSA_ALGORITHM_GROUP = NCRYPT_DSA_ALGORITHM
    NCRYPT_ECDSA_ALGORITHM_GROUP = "ECDSA"
    NCRYPT_ECDH_ALGORITHM_GROUP = "ECDH"

    if NTDDI_VERSION >= NTDDI_WIN8:
        NCRYPT_AES_ALGORITHM_GROUP = NCRYPT_AES_ALGORITHM
        NCRYPT_RC2_ALGORITHM_GROUP = NCRYPT_RC2_ALGORITHM
        NCRYPT_DES_ALGORITHM_GROUP = "DES"
        NCRYPT_KEY_DERIVATION_GROUP = "KEY_DERIVATION"
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    # NCrypt generic memory descriptors
    NCRYPTBUFFER_VERSION = 0
    NCRYPTBUFFER_EMPTY = 0
    NCRYPTBUFFER_DATA = 1

    if NTDDI_VERSION >= NTDDI_WIN8:
        # The buffer contains a null-terminated Unicode string that contains
        # the Protection Descriptor.
        NCRYPTBUFFER_PROTECTION_DESCRIPTOR_STRING = 3

        # DWORD flags to be passed to NCryptCreateProtectionDescriptor
        # function.
        NCRYPTBUFFER_PROTECTION_FLAGS = 4
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    NCRYPTBUFFER_SSL_CLIENT_RANDOM = 20
    NCRYPTBUFFER_SSL_SERVER_RANDOM = 21
    NCRYPTBUFFER_SSL_HIGHEST_VERSION = 22
    NCRYPTBUFFER_SSL_CLEAR_KEY = 23
    NCRYPTBUFFER_SSL_KEY_ARG_DATA = 24

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        NCRYPTBUFFER_SSL_SESSION_HASH = 25
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    NCRYPTBUFFER_PKCS_OID = 40
    NCRYPTBUFFER_PKCS_ALG_OID = 41
    NCRYPTBUFFER_PKCS_ALG_PARAM = 42
    NCRYPTBUFFER_PKCS_ALG_ID = 43
    NCRYPTBUFFER_PKCS_ATTRS = 44
    NCRYPTBUFFER_PKCS_KEY_NAME = 45
    NCRYPTBUFFER_PKCS_SECRET = 46
    NCRYPTBUFFER_CERT_BLOB = 47

    # for threshold key attestation
    NCRYPTBUFFER_CLAIM_IDBINDING_NONCE = 48
    NCRYPTBUFFER_CLAIM_KEYATTESTATION_NONCE = 49
    NCRYPTBUFFER_KEY_PROPERTY_FLAGS = 50
    NCRYPTBUFFER_ATTESTATIONSTATEMENT_BLOB = 51
    NCRYPTBUFFER_ATTESTATION_CLAIM_TYPE = 52
    NCRYPTBUFFER_ATTESTATION_CLAIM_CHALLENGE_REQUIRED = 53

    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        NCRYPTBUFFER_VSM_KEY_ATTESTATION_CLAIM_RESTRICTIONS = 54
    # END IF

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        # for generic ecc
        NCRYPTBUFFER_ECC_CURVE_NAME = 60
        NCRYPTBUFFER_ECC_PARAMETERS = 61
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        # for TPM seal
        NCRYPTBUFFER_TPM_SEAL_PASSWORD = 70
        NCRYPTBUFFER_TPM_SEAL_POLICYINFO = 71
        NCRYPTBUFFER_TPM_SEAL_TICKET = 72
        NCRYPTBUFFER_TPM_SEAL_NO_DA_PROTECTION = 73
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS1)

    # NCRYPT shares the same BCRYPT definitions
    NCryptBuffer = BCryptBuffer
    PNCryptBuffer = POINTER(BCryptBuffer)
    NCryptBufferDesc = BCryptBufferDesc
    PNCryptBufferDesc = POINTER(BCryptBufferDesc)

    # NCrypt handles
    NCRYPT_HANDLE = ULONG_PTR
    NCRYPT_PROV_HANDLE = ULONG_PTR
    NCRYPT_KEY_HANDLE = ULONG_PTR
    NCRYPT_HASH_HANDLE = ULONG_PTR
    NCRYPT_SECRET_HANDLE = ULONG_PTR

    if NTDDI_VERSION >= NTDDI_WIN8:

        _NCRYPT_CIPHER_PADDING_INFO._fields_ = [
            # size of this struct
            ('cbSize', ULONG),
            # See NCRYPT_CIPHER_ flag values
            ('dwFlags', DWORD),
            # [in, out, optional]
            # The address of a buffer that contains the initialization vector
            # (IV) to use during encryption.
            # The cbIV parameter contains the size of this buffer. This
            # function will modify the contents of this buffer.
            # If you need to reuse the IV later, make sure you make a copy of
            # this buffer before calling this function.
            ('pbIV', PUCHAR),
            ('cbIV', ULONG),
            # [ in, out, optional]
            # The address of a buffer that contains the algorithm specific
            # info to use during encryption.
            # The cbOtherInfo parameter contains the size of this buffer. This
            # function will modify the contents of this buffer.
            # If you need to reuse the buffer later, make sure you make a copy
            # of this buffer before calling this function.
            #
            # For Microsoft providers, when an authenticated encryption mode
            # is used,
            # this parameter must point to a serialized
            # BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO structure.
            #
            # NOTE: All pointers inside a structure must be to a data
            # allocated within pbOtherInfo buffer.

            ('pbOtherInfo', PUCHAR),
            ('cbOtherInfo', ULONG),

        ]

        # The following flags are used with NCRYPT_CIPHER_PADDING_INFO
        NCRYPT_CIPHER_NO_PADDING_FLAG = 0x00000000
        NCRYPT_CIPHER_BLOCK_PADDING_FLAG = 0x00000001
        NCRYPT_CIPHER_OTHER_PADDING_FLAG = 0x00000002
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        NCRYPT_PLATFORM_ATTEST_MAGIC = 0x44504150        # 'PAPD'


        # 'PAPD'
        _NCRYPT_PLATFORM_ATTEST_PADDING_INFO._fields_ = [
            ('magic', ULONG),
            ('pcrMask', ULONG),
        ]
        NCRYPT_KEY_ATTEST_MAGIC = 0x4450414B        # 'KAPD'


        # 'KAPD'
        _NCRYPT_KEY_ATTEST_PADDING_INFO._fields_ = [
            ('magic', ULONG),
            ('pbKeyBlob', PUCHAR),
            ('cbKeyBlob', ULONG),
            ('pbKeyAuth', PUCHAR),
            ('cbKeyAuth', ULONG),
        ]
    # END IF   (NTDDI_VERSION >= NTDDI_WINBLUE)

    # key attestation claim type
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        NCRYPT_CLAIM_AUTHORITY_ONLY = 0x00000001
        NCRYPT_CLAIM_SUBJECT_ONLY = 0x00000002
        NCRYPT_CLAIM_WEB_AUTH_SUBJECT_ONLY = 0x00000102
        NCRYPT_CLAIM_AUTHORITY_AND_SUBJECT = 0x00000003
        if NTDDI_VERSION >= NTDDI_WIN10_RS3:
            NCRYPT_CLAIM_VSM_KEY_ATTESTATION_STATEMENT = 0x00000004
        # END IF


        NCRYPT_CLAIM_UNKNOWN = 0x00001000
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        # NCryptCreateClaim claim types, flags and buffer types
        NCRYPT_ISOLATED_KEY_FLAG_CREATED_IN_ISOLATION = 0x00000001        # if set, this key was generated in isolation, not imported
        NCRYPT_ISOLATED_KEY_FLAG_IMPORT_ONLY = 0x00000002        # if set, this key can only be used for importing other keys
        NCRYPT_ISOLATED_KEY_ATTESTED_ATTRIBUTES_V0 = 0
        NCRYPT_ISOLATED_KEY_ATTESTED_ATTRIBUTES_CURRENT_VERSION = (
            NCRYPT_ISOLATED_KEY_ATTESTED_ATTRIBUTES_V0
        )


        _NCRYPT_ISOLATED_KEY_ATTESTED_ATTRIBUTES._fields_ = [
            # set to NCRYPT_ISOLATED_KEY_ATTESTED_ATTRIBUTES_V0
            ('Version', ULONG),
            # NCRYPT_ISOLATED_KEY_FLAG_ flags
            ('Flags', ULONG),
            ('cbPublicKeyBlob', ULONG),
        ]
        NCRYPT_VSM_KEY_ATTESTATION_STATEMENT_V0 = 0
        NCRYPT_VSM_KEY_ATTESTATION_STATEMENT_CURRENT_VERSION = (
            NCRYPT_VSM_KEY_ATTESTATION_STATEMENT_V0
        )


        _NCRYPT_VSM_KEY_ATTESTATION_STATEMENT._fields_ = [
            # {'I', 'M', 'S', 'V'} - 'VSMI' for VSM Isolated
            ('Magic', ULONG),
            # Set to NCRYPT_VSM_KEY_ATTESTATION_STATEMENT_CURRENT_VERSION
            ('Version', ULONG),
            # Secure kernel signature over the isolation report
            ('cbSignature', ULONG),
            # Key isolation report from the secure kernel
            ('cbReport', ULONG),
            # Attributes of the isolated key including public key blob
            ('cbAttributes', ULONG),
        ]

        # Buffer contents for NCryptVerifyClaim
        # (for buffer type NCRYPTBUFFER_ISOLATED_KEY_ATTESTATION_CLAIM_RESTRICTIONS)
        #
        NCRYPT_VSM_KEY_ATTESTATION_CLAIM_RESTRICTIONS_V0 = 0
        NCRYPT_VSM_KEY_ATTESTATION_CLAIM_RESTRICTIONS_CURRENT_VERSION = (
            NCRYPT_VSM_KEY_ATTESTATION_CLAIM_RESTRICTIONS_V0
        )


        _NCRYPT_VSM_KEY_ATTESTATION_CLAIM_RESTRICTIONS._fields_ = [
            # Set to NCRYPT_VSM_KEY_ATTESTATION_CLAIM_RESTRICTIONS_V0
            ('Version', ULONG),
            # Trustlet type
            ('TrustletId', ULONGLONG),
            # Minimum acceptable trustlet SVN, 0 if don't care
            ('MinSvn', ULONG),
            # Which of NCRYPT_ISOLATED_KEY_ flags to check
            ('FlagsMask', ULONG),
            # Expected values of flags inside the mask
            ('FlagsExpected', ULONG),
            # Is it okay for the trustlet to be debugged, 0 if no
            ('AllowDebugging', ULONG, 1),
            # Future extension area, must be 0
            ('Reserved', ULONG, 31),
        ]

        # Structures to assist with importation of isolated keys
        NCRYPT_EXPORTED_ISOLATED_KEY_HEADER_V0 = 0
        NCRYPT_EXPORTED_ISOLATED_KEY_HEADER_CURRENT_VERSION = (
            NCRYPT_EXPORTED_ISOLATED_KEY_HEADER_V0
        )


        _NCRYPT_EXPORTED_ISOLATED_KEY_HEADER._fields_ = [
            # Set to NCRYPT_EXPORTED_ISOLATED_KEY_HEADER_V0
            ('Version', ULONG),
            # Set to NCRYPT_ALLOW_KEY_IMPORT_FLAG for import-only keys
            ('KeyUsage', ULONG),
            # Set to TRUE if the key is to be valid in the current boot cycle
            # only
            ('PerBootKey', ULONG, 1),
            # Leave as 0
            ('Reserved', ULONG, 31),
            # Number of bytes in Unicode algorithm name following header +
            # terminating NULL
            ('cbAlgName', ULONG),
            # Number of bytes in the nonce used to encrypt the isolated key
            ('cbNonce', ULONG),
            # Number of bytes in authentication tag resulting from encrypting
            # the isolated key
            ('cbAuthTag', ULONG),
            # Number of bytes in encrypted wrapping key blob
            ('cbWrappingKey', ULONG),
            # Number of bytes in encrypted isolated key blob
            ('cbIsolatedKey', ULONG),
        ]

        _NCRYPT_EXPORTED_ISOLATED_KEY_ENVELOPE._fields_ = [
            ('Header', NCRYPT_EXPORTED_ISOLATED_KEY_HEADER),
        ]
    # END IF


    if NTDDI_VERSION >= NTDDI_WIN10_RS2:
        __NCRYPT_PCP_TPM_WEB_AUTHN_ATTESTATION_STATEMENT._fields_ = [
            # { 'A', 'W', 'A', 'K' } - 'KAWA'
            ('Magic', UINT32),
            # 1 for the statement defined in this specification
            ('Version', UINT32),
            # 24
            ('HeaderSize', UINT32),
            ('cbCertifyInfo', UINT32),
            ('cbSignature', UINT32),
            ('cbTpmPublic', UINT32),
        ]
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS2)

    # NCrypt API Flags
    NCRYPT_NO_PADDING_FLAG = 0x00000001    # NCryptEncrypt/Decrypt
    NCRYPT_PAD_PKCS1_FLAG = 0x00000002    # NCryptEncrypt/Decrypt NCryptSignHash/VerifySignature
    NCRYPT_PAD_OAEP_FLAG = 0x00000004    # BCryptEncrypt/Decrypt
    NCRYPT_PAD_PSS_FLAG = 0x00000008    # BCryptSignHash/VerifySignature
    if NTDDI_VERSION >= NTDDI_WIN8:
        NCRYPT_PAD_CIPHER_FLAG = 0x00000010        # NCryptEncrypt/Decrypt
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        NCRYPT_ATTESTATION_FLAG = 0x00000020        # NCryptDecrypt for key attestation
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        NCRYPT_SEALING_FLAG = 0x00000100        # NCryptEncrypt/Decrypt for sealing
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS1)

    NCRYPT_REGISTER_NOTIFY_FLAG = 0x00000001    # NCryptNotifyChangeKey
    NCRYPT_UNREGISTER_NOTIFY_FLAG = 0x00000002    # NCryptNotifyChangeKey
    NCRYPT_NO_KEY_VALIDATION = BCRYPT_NO_KEY_VALIDATION
    NCRYPT_MACHINE_KEY_FLAG = 0x00000020    # same as CAPI CRYPT_MACHINE_KEYSET
    NCRYPT_SILENT_FLAG = 0x00000040    # same as CAPI CRYPT_SILENT
    NCRYPT_OVERWRITE_KEY_FLAG = 0x00000080
    NCRYPT_WRITE_KEY_TO_LEGACY_STORE_FLAG = 0x00000200
    NCRYPT_DO_NOT_FINALIZE_FLAG = 0x00000400
    NCRYPT_EXPORT_LEGACY_FLAG = 0x00000800
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        NCRYPT_IGNORE_DEVICE_STATE_FLAG = 0x00001000        # NCryptOpenStorageProvider
    # END IF   (NTDDI_VERSION >= NTDDI_WINBLUE)

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        NCRYPT_TREAT_NIST_AS_GENERIC_ECC_FLAG = 0x00002000
        NCRYPT_NO_CACHED_PASSWORD = 0x00004000
        NCRYPT_PROTECT_TO_LOCAL_SYSTEM = 0x00008000
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    NCRYPT_PERSIST_ONLY_FLAG = 0x40000000
    NCRYPT_PERSIST_FLAG = 0x80000000
    if NTDDI_VERSION >= NTDDI_WIN10_RS2:
        NCRYPT_PREFER_VIRTUAL_ISOLATION_FLAG = 0x00010000        # NCryptCreatePersistedKey NCryptImportKey
        NCRYPT_USE_VIRTUAL_ISOLATION_FLAG = 0x00020000        # NCryptCreatePersistedKey NCryptImportKey
        NCRYPT_USE_PER_BOOT_KEY_FLAG = 0x00040000        # NCryptCreatePersistedKey NCryptImportKey
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS2)

    # Functions used to manage persisted keys.
    # NCryptOpenStorageProvider flags
    NCRYPT_SILENT_FLAG = 0x00000040    # same as CAPI CRYPT_SILENT
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        NCRYPT_IGNORE_DEVICE_STATE_FLAG = 0x00001000        # NCryptOpenStorageProvider
    # END IF   (NTDDI_VERSION >= NTDDI_WINBLUE)

    ncrypt = ctypes.windll.NCRYPT


    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptOpenStorageProvider(
    # _Out_   NCRYPT_PROV_HANDLE *phProvider,
    # _In_opt_ LPCWSTR pszProviderName,
    # _In_    DWORD   dwFlags);
    NCryptOpenStorageProvider = ncrypt.NCryptOpenStorageProvider
    NCryptOpenStorageProvider.restype = SECURITY_STATUS


    # AlgOperations flags for use with NCryptEnumAlgorithms()
    NCRYPT_CIPHER_OPERATION = BCRYPT_CIPHER_OPERATION
    NCRYPT_HASH_OPERATION = BCRYPT_HASH_OPERATION
    NCRYPT_ASYMMETRIC_ENCRYPTION_OPERATION = (
        BCRYPT_ASYMMETRIC_ENCRYPTION_OPERATION
    )
    NCRYPT_SECRET_AGREEMENT_OPERATION = BCRYPT_SECRET_AGREEMENT_OPERATION
    NCRYPT_SIGNATURE_OPERATION = BCRYPT_SIGNATURE_OPERATION
    NCRYPT_RNG_OPERATION = BCRYPT_RNG_OPERATION
    if NTDDI_VERSION >= NTDDI_WIN8:
        NCRYPT_KEY_DERIVATION_OPERATION = BCRYPT_KEY_DERIVATION_OPERATION
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    # USE EXTREME CAUTION: editing comments that contain "certenrolls_*" tokens
    # could break building CertEnroll idl files:
    # certenrolls_begin -- NCryptAlgorithmName
    _NCryptAlgorithmName._fields_ = [
        ('pszName', LPWSTR),
        # the CNG interface that supports this algorithm
        ('dwClass', DWORD),
        # the types of operations supported by this algorithm
        ('dwAlgOperations', DWORD),
        ('dwFlags', DWORD),
    ]

    # certenrolls_end
    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptEnumAlgorithms(
    # _In_    NCRYPT_PROV_HANDLE hProvider,
    # _In_    DWORD   dwAlgOperations,
    # _Out_   DWORD * pdwAlgCount,
    # _Outptr_result_buffer_(*pdwAlgCount) NCryptAlgorithmName **ppAlgList,
    # _In_    DWORD   dwFlags);
    NCryptEnumAlgorithms = ncrypt.NCryptEnumAlgorithms
    NCryptEnumAlgorithms.restype = SECURITY_STATUS


    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptIsAlgSupported(
    # _In_    NCRYPT_PROV_HANDLE hProvider,
    # _In_    LPCWSTR pszAlgId,
    # _In_    DWORD   dwFlags);
    NCryptIsAlgSupported = ncrypt.NCryptIsAlgSupported
    NCryptIsAlgSupported.restype = SECURITY_STATUS


    # NCryptEnumKeys flags
    NCRYPT_MACHINE_KEY_FLAG = 0x00000020


    NCryptKeyName._fields_ = [
        ('pszName', LPWSTR),
        ('pszAlgid', LPWSTR),
        ('dwLegacyKeySpec', DWORD),
        ('dwFlags', DWORD),
    ]


    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptEnumKeys(
    # _In_    NCRYPT_PROV_HANDLE hProvider,
    # _In_opt_ LPCWSTR pszScope,
    # _Outptr_ NCryptKeyName **ppKeyName,
    # _Inout_ PVOID * ppEnumState,
    # _In_    DWORD   dwFlags);
    NCryptEnumKeys = ncrypt.NCryptEnumKeys
    NCryptEnumKeys.restype = SECURITY_STATUS


    NCryptProviderName._fields_ = [
        ('pszName', LPWSTR),
        ('pszComment', LPWSTR),
    ]
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        ncrypt = ctypes.windll.NCRYPT


        # _Check_return_
        # SECURITY_STATUS
        # WINAPI
        # NCryptEnumStorageProviders(
        # _Out_   DWORD * pdwProviderCount,
        # _Outptr_result_buffer_(*pdwProviderCount) NCryptProviderName **ppProviderList,
        # _In_    DWORD   dwFlags);
        NCryptEnumStorageProviders = ncrypt.NCryptEnumStorageProviders
        NCryptEnumStorageProviders.restype = SECURITY_STATUS


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)


    # SECURITY_STATUS
    # WINAPI
    # NCryptFreeBuffer(
    # _Pre_notnull_ PVOID   pvInput);
    NCryptFreeBuffer = ncrypt.NCryptFreeBuffer
    NCryptFreeBuffer.restype = WINAPI


    # NCryptOpenKey flags
    NCRYPT_MACHINE_KEY_FLAG = 0x00000020
    NCRYPT_SILENT_FLAG = 0x00000040
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        NCRYPT_AUTHORITY_KEY_FLAG = 0x00000100
    # END IF


    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptOpenKey(
    # _In_    NCRYPT_PROV_HANDLE hProvider,
    # _Out_   NCRYPT_KEY_HANDLE *phKey,
    # _In_    LPCWSTR pszKeyName,
    # _In_opt_ DWORD  dwLegacyKeySpec,
    # _In_    DWORD   dwFlags);
    NCryptOpenKey = ncrypt.NCryptOpenKey
    NCryptOpenKey.restype = SECURITY_STATUS


    # NCryptCreatePersistedKey flags
    NCRYPT_MACHINE_KEY_FLAG = 0x00000020
    NCRYPT_OVERWRITE_KEY_FLAG = 0x00000080


    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptCreatePersistedKey(
    # _In_    NCRYPT_PROV_HANDLE hProvider,
    # _Out_   NCRYPT_KEY_HANDLE *phKey,
    # _In_    LPCWSTR pszAlgId,
    # _In_opt_ LPCWSTR pszKeyName,
    # _In_    DWORD   dwLegacyKeySpec,
    # _In_    DWORD   dwFlags);
    NCryptCreatePersistedKey = ncrypt.NCryptCreatePersistedKey
    NCryptCreatePersistedKey.restype = SECURITY_STATUS


    # Standard property names.
    NCRYPT_NAME_PROPERTY = "Name"
    NCRYPT_UNIQUE_NAME_PROPERTY = "Unique Name"
    NCRYPT_ALGORITHM_PROPERTY = "Algorithm Name"
    NCRYPT_LENGTH_PROPERTY = "Length"
    NCRYPT_LENGTHS_PROPERTY = "Lengths"
    NCRYPT_BLOCK_LENGTH_PROPERTY = "Block Length"
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        NCRYPT_PUBLIC_LENGTH_PROPERTY = BCRYPT_PUBLIC_KEY_LENGTH
        NCRYPT_SIGNATURE_LENGTH_PROPERTY = BCRYPT_SIGNATURE_LENGTH
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    if NTDDI_VERSION >= NTDDI_WIN8:
        NCRYPT_CHAINING_MODE_PROPERTY = "Chaining Mode"
        NCRYPT_AUTH_TAG_LENGTH = "AuthTagLength"
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    NCRYPT_UI_POLICY_PROPERTY = "UI Policy"
    NCRYPT_EXPORT_POLICY_PROPERTY = "Export Policy"
    NCRYPT_WINDOW_HANDLE_PROPERTY = "HWND Handle"
    NCRYPT_USE_CONTEXT_PROPERTY = "Use Context"
    NCRYPT_IMPL_TYPE_PROPERTY = "Impl Type"
    NCRYPT_KEY_USAGE_PROPERTY = "Key Usage"
    NCRYPT_KEY_TYPE_PROPERTY = "Key Type"
    NCRYPT_VERSION_PROPERTY = "Version"
    NCRYPT_SECURITY_DESCR_SUPPORT_PROPERTY = "Security Descr Support"
    NCRYPT_SECURITY_DESCR_PROPERTY = "Security Descr"
    NCRYPT_USE_COUNT_ENABLED_PROPERTY = "Enabled Use Count"
    NCRYPT_USE_COUNT_PROPERTY = "Use Count"
    NCRYPT_LAST_MODIFIED_PROPERTY = "Modified"
    NCRYPT_MAX_NAME_LENGTH_PROPERTY = "Max Name Length"
    NCRYPT_ALGORITHM_GROUP_PROPERTY = "Algorithm Group"
    NCRYPT_DH_PARAMETERS_PROPERTY = BCRYPT_DH_PARAMETERS
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        NCRYPT_ECC_PARAMETERS_PROPERTY = BCRYPT_ECC_PARAMETERS
        NCRYPT_ECC_CURVE_NAME_PROPERTY = BCRYPT_ECC_CURVE_NAME
        NCRYPT_ECC_CURVE_NAME_LIST_PROPERTY = BCRYPT_ECC_CURVE_NAME_LIST
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    if NTDDI_VERSION >= NTDDI_WIN10_RS2:
        NCRYPT_USE_VIRTUAL_ISOLATION_PROPERTY = "Virtual Iso"
        NCRYPT_USE_PER_BOOT_KEY_PROPERTY = "Per Boot Key"
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS2)

    NCRYPT_PROVIDER_HANDLE_PROPERTY = "Provider Handle"
    NCRYPT_PIN_PROPERTY = "SmartCardPin"
    NCRYPT_READER_PROPERTY = "SmartCardReader"
    NCRYPT_SMARTCARD_GUID_PROPERTY = "SmartCardGuid"
    NCRYPT_CERTIFICATE_PROPERTY = "SmartCardKeyCertificate"
    NCRYPT_PIN_PROMPT_PROPERTY = "SmartCardPinPrompt"
    NCRYPT_USER_CERTSTORE_PROPERTY = "SmartCardUserCertStore"
    NCRYPT_ROOT_CERTSTORE_PROPERTY = "SmartcardRootCertStore"
    NCRYPT_SECURE_PIN_PROPERTY = "SmartCardSecurePin"
    if NTDDI_VERSION >= NTDDI_WIN7:
        NCRYPT_ASSOCIATED_ECDH_KEY = "SmartCardAssociatedECDHKey"
        NCRYPT_SCARD_PIN_ID = "SmartCardPinId"
        NCRYPT_SCARD_PIN_INFO = "SmartCardPinInfo"
    # END IF   (NTDDI_VERSION >= NTDDI_WIN7)

    if NTDDI_VERSION >= NTDDI_WIN8:
        NCRYPT_READER_ICON_PROPERTY = "SmartCardReaderIcon"
        NCRYPT_KDF_SECRET_VALUE = "KDFKeySecret"

        # Additional property strings specific for the Platform Crypto Provider
        NCRYPT_PCP_PLATFORM_TYPE_PROPERTY = "PCP_PLATFORM_TYPE"
        NCRYPT_PCP_PROVIDER_VERSION_PROPERTY = "PCP_PROVIDER_VERSION"
        NCRYPT_PCP_EKPUB_PROPERTY = "PCP_EKPUB"
        NCRYPT_PCP_EKCERT_PROPERTY = "PCP_EKCERT"
        NCRYPT_PCP_EKNVCERT_PROPERTY = "PCP_EKNVCERT"
        NCRYPT_PCP_RSA_EKPUB_PROPERTY = "PCP_RSA_EKPUB"
        NCRYPT_PCP_RSA_EKCERT_PROPERTY = "PCP_RSA_EKCERT"
        NCRYPT_PCP_RSA_EKNVCERT_PROPERTY = "PCP_RSA_EKNVCERT"
        NCRYPT_PCP_ECC_EKPUB_PROPERTY = "PCP_ECC_EKPUB"
        NCRYPT_PCP_ECC_EKCERT_PROPERTY = "PCP_ECC_EKCERT"
        NCRYPT_PCP_ECC_EKNVCERT_PROPERTY = "PCP_ECC_EKNVCERT"
        NCRYPT_PCP_SRKPUB_PROPERTY = "PCP_SRKPUB"
        NCRYPT_PCP_PCRTABLE_PROPERTY = "PCP_PCRTABLE"
        NCRYPT_PCP_CHANGEPASSWORD_PROPERTY = "PCP_CHANGEPASSWORD"
        NCRYPT_PCP_PASSWORD_REQUIRED_PROPERTY = "PCP_PASSWORD_REQUIRED"
        NCRYPT_PCP_USAGEAUTH_PROPERTY = "PCP_USAGEAUTH"
        NCRYPT_PCP_MIGRATIONPASSWORD_PROPERTY = "PCP_MIGRATIONPASSWORD"
        NCRYPT_PCP_EXPORT_ALLOWED_PROPERTY = "PCP_EXPORT_ALLOWED"
        NCRYPT_PCP_STORAGEPARENT_PROPERTY = "PCP_STORAGEPARENT"
        NCRYPT_PCP_PROVIDERHANDLE_PROPERTY = "PCP_PROVIDERMHANDLE"
        NCRYPT_PCP_PLATFORMHANDLE_PROPERTY = "PCP_PLATFORMHANDLE"
        NCRYPT_PCP_PLATFORM_BINDING_PCRMASK_PROPERTY = (
            "PCP_PLATFORM_BINDING_PCRMASK"
        )
        NCRYPT_PCP_PLATFORM_BINDING_PCRDIGESTLIST_PROPERTY = (
            "PCP_PLATFORM_BINDING_PCRDIGESTLIST"
        )
        NCRYPT_PCP_PLATFORM_BINDING_PCRDIGEST_PROPERTY = (
            "PCP_PLATFORM_BINDING_PCRDIGEST"
        )
        NCRYPT_PCP_KEY_USAGE_POLICY_PROPERTY = "PCP_KEY_USAGE_POLICY"
        NCRYPT_PCP_RSA_SCHEME_PROPERTY = "PCP_RSA_SCHEME"
        NCRYPT_PCP_RSA_SCHEME_HASH_ALG_PROPERTY = "PCP_RSA_SCHEME_HASH_ALG"
        NCRYPT_PCP_TPM12_IDBINDING_PROPERTY = "PCP_TPM12_IDBINDING"
        NCRYPT_PCP_TPM12_IDBINDING_DYNAMIC_PROPERTY = (
            "PCP_TPM12_IDBINDING_DYNAMIC"
        )
        NCRYPT_PCP_TPM12_IDACTIVATION_PROPERTY = "PCP_TPM12_IDACTIVATION"
        NCRYPT_PCP_KEYATTESTATION_PROPERTY = "PCP_TPM12_KEYATTESTATION"
        NCRYPT_PCP_ALTERNATE_KEY_STORAGE_LOCATION_PROPERTY = (
            "PCP_ALTERNATE_KEY_STORAGE_LOCATION"
        )
        NCRYPT_PCP_TPM_IFX_RSA_KEYGEN_PROHIBITED_PROPERTY = (
            "PCP_TPM_IFX_RSA_KEYGEN_PROHIBITED"
        )
        NCRYPT_PCP_TPM_IFX_RSA_KEYGEN_VULNERABILITY_PROPERTY = (
            "PCP_TPM_IFX_RSA_KEYGEN_VULNERABILITY"
        )
        if NTDDI_VERSION >= NTDDI_WIN10_RS1:
            NCRYPT_PCP_HMAC_AUTH_POLICYREF = "PCP_HMAC_AUTH_POLICYREF"
            NCRYPT_PCP_HMAC_AUTH_POLICYINFO = "PCP_HMAC_AUTH_POLICYINFO"
            NCRYPT_PCP_HMAC_AUTH_NONCE = "PCP_HMAC_AUTH_NONCE"
            NCRYPT_PCP_HMAC_AUTH_SIGNATURE = "PCP_HMAC_AUTH_SIGNATURE"
            NCRYPT_PCP_HMAC_AUTH_TICKET = "PCP_HMAC_AUTH_TICKET"
            NCRYPT_PCP_NO_DA_PROTECTION_PROPERTY = "PCP_NO_DA_PROTECTION"
        # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS1)

        if NTDDI_VERSION >= NTDDI_WIN10_RS2:
            NCRYPT_PCP_TPM_MANUFACTURER_ID_PROPERTY = "PCP_TPM_MANUFACTURER_ID"
            NCRYPT_PCP_TPM_FW_VERSION_PROPERTY = "PCP_TPM_FW_VERSION"
        # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS2)

        if NTDDI_VERSION >= NTDDI_WIN10_RS3:
            NCRYPT_PCP_TPM2BNAME_PROPERTY = "PCP_TPM2BNAME"
            NCRYPT_PCP_TPM_VERSION_PROPERTY = "PCP_TPM_VERSION"
        # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS3)

        if NTDDI_VERSION >= NTDDI_WIN10_RS4:
            NCRYPT_PCP_RAW_POLICYDIGEST_PROPERTY = "PCP_RAW_POLICYDIGEST"
            NCRYPT_PCP_KEY_CREATIONHASH_PROPERTY = "PCP_KEY_CREATIONHASH"
            NCRYPT_PCP_KEY_CREATIONTICKET_PROPERTY = "PCP_KEY_CREATIONTICKET"
        # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS4)

        if NTDDI_VERSION >= NTDDI_WIN10_RS5:
            NCRYPT_PCP_SESSIONID_PROPERTY = "PCP_SESSIONID"
        # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS5)

        # NCRYPT_PCP_TPM_IFX_RSA_KEYGEN_VULNERABILITY_PROPERTY values
        IFX_RSA_KEYGEN_VUL_NOT_AFFECTED = 0
        IFX_RSA_KEYGEN_VUL_AFFECTED_LEVEL_1 = 1
        IFX_RSA_KEYGEN_VUL_AFFECTED_LEVEL_2 = 2

        # BCRYPT_PCP_KEY_USAGE_POLICY values
        NCRYPT_TPM12_PROVIDER = 0x00010000
        NCRYPT_PCP_SIGNATURE_KEY = 0x00000001
        NCRYPT_PCP_ENCRYPTION_KEY = 0x00000002
        NCRYPT_PCP_GENERIC_KEY = (
            NCRYPT_PCP_SIGNATURE_KEY |
            NCRYPT_PCP_ENCRYPTION_KEY
        )
        NCRYPT_PCP_STORAGE_KEY = 0x00000004
        NCRYPT_PCP_IDENTITY_KEY = 0x00000008
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        NCRYPT_PCP_HMACVERIFICATION_KEY = 0x00000010
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS1)

    # Additional property strings specific for the Smart Card Key Storage
    # Provider
    if NTDDI_VERSION >= NTDDI_WIN10:
        NCRYPT_SCARD_NGC_KEY_NAME = "SmartCardNgcKeyName"
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10)

    if NTDDI_VERSION >= NTDDI_WIN10:
        NCRYPT_PCP_PLATFORM_BINDING_PCRALGID_PROPERTY = (
            "PCP_PLATFORM_BINDING_PCRALGID"
        )
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10)

    if NTDDI_VERSION >= NTDDI_WIN8:
        # Used to set IV for block ciphers, before calling
        # NCryptEncrypt/NCryptDecrypt
        NCRYPT_INITIALIZATION_VECTOR = BCRYPT_INITIALIZATION_VECTOR
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        NCRYPT_CHANGEPASSWORD_PROPERTY = NCRYPT_PCP_CHANGEPASSWORD_PROPERTY
        NCRYPT_ALTERNATE_KEY_STORAGE_LOCATION_PROPERTY = (
            NCRYPT_PCP_ALTERNATE_KEY_STORAGE_LOCATION_PROPERTY
        )
        NCRYPT_KEY_ACCESS_POLICY_PROPERTY = "Key Access Policy"
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    # Maximum length of property name (in characters)
    NCRYPT_MAX_PROPERTY_NAME = 64

    # Maximum length of property data (in bytes)
    NCRYPT_MAX_PROPERTY_DATA = 0x100000

    # NCRYPT_EXPORT_POLICY_PROPERTY property flags.
    NCRYPT_ALLOW_EXPORT_FLAG = 0x00000001
    NCRYPT_ALLOW_PLAINTEXT_EXPORT_FLAG = 0x00000002
    NCRYPT_ALLOW_ARCHIVING_FLAG = 0x00000004
    NCRYPT_ALLOW_PLAINTEXT_ARCHIVING_FLAG = 0x00000008

    # NCRYPT_IMPL_TYPE_PROPERTY property flags.
    NCRYPT_IMPL_HARDWARE_FLAG = 0x00000001
    NCRYPT_IMPL_SOFTWARE_FLAG = 0x00000002
    NCRYPT_IMPL_REMOVABLE_FLAG = 0x00000008
    NCRYPT_IMPL_HARDWARE_RNG_FLAG = 0x00000010

    if NTDDI_VERSION >= NTDDI_WIN10_RS4:
        NCRYPT_IMPL_VIRTUAL_ISOLATION_FLAG = 0x00000020
    # END IF

    # NCRYPT_KEY_USAGE_PROPERTY property flags.
    NCRYPT_ALLOW_DECRYPT_FLAG = 0x00000001
    NCRYPT_ALLOW_SIGNING_FLAG = 0x00000002
    NCRYPT_ALLOW_KEY_AGREEMENT_FLAG = 0x00000004

    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        NCRYPT_ALLOW_KEY_IMPORT_FLAG = 0x00000008
    # END IF

    NCRYPT_ALLOW_ALL_USAGES = 0x00FFFFFF

    # NCRYPT_UI_POLICY_PROPERTY property flags and structure
    NCRYPT_UI_PROTECT_KEY_FLAG = 0x00000001
    NCRYPT_UI_FORCE_HIGH_PROTECTION_FLAG = 0x00000002

    if NTDDI_VERSION >= NTDDI_WINBLUE:
        NCRYPT_UI_FINGERPRINT_PROTECTION_FLAG = 0x00000004
        NCRYPT_UI_APPCONTAINER_ACCESS_MEDIUM_FLAG = 0x00000008
    # END IF   (NTDDI_VERSION >= NTDDI_WINBLUE)

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        # Pin Cache Provider Properties
        NCRYPT_PIN_CACHE_FREE_APPLICATION_TICKET_PROPERTY = (
            "PinCacheFreeApplicationTicket"
        )

        if NTDDI_VERSION >= NTDDI_WIN10_RS1:
            NCRYPT_PIN_CACHE_FLAGS_PROPERTY = "PinCacheFlags"

            # The NCRYPT_PIN_CACHE_FLAGS_PROPERTY property is a DWORD value
            # that can be set from a trusted process. The
            # following flags can be set.
            NCRYPT_PIN_CACHE_DISABLE_DPL_FLAG = 0x00000001
        # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS1)

        # Pin Cache Key Properties
        NCRYPT_PIN_CACHE_APPLICATION_TICKET_PROPERTY = (
            "PinCacheApplicationTicket"
        )
        NCRYPT_PIN_CACHE_APPLICATION_IMAGE_PROPERTY = (
            "PinCacheApplicationImage"
        )
        NCRYPT_PIN_CACHE_APPLICATION_STATUS_PROPERTY = (
            "PinCacheApplicationStatus"
        )
        NCRYPT_PIN_CACHE_PIN_PROPERTY = "PinCachePin"
        NCRYPT_PIN_CACHE_IS_GESTURE_REQUIRED_PROPERTY = (
            "PinCacheIsGestureRequired"
        )
        NCRYPT_PIN_CACHE_REQUIRE_GESTURE_FLAG = 0x00000001

        # The NCRYPT_PIN_CACHE_PIN_PROPERTY and
        # NCRYPT_PIN_CACHE_APPLICATION_TICKET_PROPERTY properties
        # return a 32 byte random unique ID encoded as a null terminated
        # base64 Unicode string. The string length
        # is 32 * 4/3 + 1 characters = 45 characters, 90 bytes
        NCRYPT_PIN_CACHE_PIN_BYTE_LENGTH = 90
        NCRYPT_PIN_CACHE_APPLICATION_TICKET_BYTE_LENGTH = 90
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        NCRYPT_PIN_CACHE_CLEAR_PROPERTY = "PinCacheClear"

        # The NCRYPT_PIN_CACHE_CLEAR_PROPERTY property is a DWORD value. The
        # following option can be set:
        NCRYPT_PIN_CACHE_CLEAR_FOR_CALLING_PROCESS_OPTION = 0x00000001
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS1)


    __NCRYPT_UI_POLICY._fields_ = [
        ('dwVersion', DWORD),
        ('dwFlags', DWORD),
        ('pszCreationTitle', LPCWSTR),
        ('pszFriendlyName', LPCWSTR),
        ('pszDescription', LPCWSTR),
    ]
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        NCRYPT_KEY_ACCESS_POLICY_VERSION = 1
        NCRYPT_ALLOW_SILENT_KEY_ACCESS = 0x00000001


        __NCRYPT_KEY_ACCESS_POLICY_BLOB._fields_ = [
            ('dwVersion', DWORD),
            ('dwPolicyFlags', DWORD),
            ('cbUserSid', DWORD),
            ('cbApplicationSid', DWORD),
        ]
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    # NCRYPT_LENGTHS_PROPERTY property structure.
    __NCRYPT_SUPPORTED_LENGTHS._fields_ = [
        ('dwMinLength', DWORD),
        ('dwMaxLength', DWORD),
        ('dwIncrement', DWORD),
        ('dwDefaultLength', DWORD),
    ]
    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        # NCRYPT_PCP_HMAC_AUTH_SIGNATURE property structure.
        __NCRYPT_PCP_HMAC_AUTH_SIGNATURE_INFO._fields_ = [
            ('dwVersion', DWORD),
            ('iExpiration', INT32),
            ('pabNonce', BYTE * 32),
            ('pabPolicyRef', BYTE * 32),
            ('pabHMAC', BYTE * 32),
        ]
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS1)

    if NTDDI_VERSION >= NTDDI_WIN10_RS2:
        # NCRYPT_PCP_TPM_FW_VERSION property structure.
        __NCRYPT_PCP_TPM_FW_VERSION_INFO._fields_ = [
            ('major1', UINT16),
            ('major2', UINT16),
            ('minor1', UINT16),
            ('minor2', UINT16),
        ]
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS2)

    if NTDDI_VERSION >= NTDDI_WIN10_RS4:
        # NCRYPT_PCP_RAW_POLICYDIGEST_PROPERTY structure
        __NCRYPT_PCP_RAW_POLICYDIGEST._fields_ = [
            ('dwVersion', DWORD),
            ('cbDigest', DWORD),
        ]
    # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS2)

    # NCryptGetProperty flags
    NCRYPT_PERSIST_ONLY_FLAG = 0x40000000


    # _Check_return_
    # _Success_( return == 0 )
    # SECURITY_STATUS
    # WINAPI
    # NCryptGetProperty(
    # _In_    NCRYPT_HANDLE hObject,
    # _In_    LPCWSTR pszProperty,
    # _Out_writes_bytes_to_opt_(cbOutput, *pcbResult) PBYTE pbOutput,
    # _In_    DWORD   cbOutput,
    # _Out_   DWORD * pcbResult,
    # _In_    DWORD   dwFlags);
    NCryptGetProperty = ncrypt.NCryptGetProperty
    NCryptGetProperty.restype = SECURITY_STATUS


    # NCryptSetProperty flags
    NCRYPT_PERSIST_FLAG = 0x80000000
    NCRYPT_PERSIST_ONLY_FLAG = 0x40000000


    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptSetProperty(
    # _In_    NCRYPT_HANDLE hObject,
    # _In_    LPCWSTR pszProperty,
    # _In_reads_bytes_(cbInput) PBYTE pbInput,
    # _In_    DWORD   cbInput,
    # _In_    DWORD   dwFlags);
    NCryptSetProperty = ncrypt.NCryptSetProperty
    NCryptSetProperty.restype = SECURITY_STATUS


    # NCryptFinalizeKey flags
    NCRYPT_WRITE_KEY_TO_LEGACY_STORE_FLAG = 0x00000200


    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptFinalizeKey(
    # _In_    NCRYPT_KEY_HANDLE hKey,
    # _In_    DWORD   dwFlags);
    NCryptFinalizeKey = ncrypt.NCryptFinalizeKey
    NCryptFinalizeKey.restype = SECURITY_STATUS


    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptEncrypt(
    # _In_    NCRYPT_KEY_HANDLE hKey,
    # _In_reads_bytes_opt_(cbInput) PBYTE pbInput,
    # _In_    DWORD   cbInput,
    # _In_opt_    VOID *pPaddingInfo,
    # _Out_writes_bytes_to_opt_(cbOutput, *pcbResult) PBYTE pbOutput,
    # _In_    DWORD   cbOutput,
    # _Out_   DWORD * pcbResult,
    # _In_    DWORD   dwFlags);
    NCryptEncrypt = ncrypt.NCryptEncrypt
    NCryptEncrypt.restype = SECURITY_STATUS


    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptDecrypt(
    # _In_    NCRYPT_KEY_HANDLE hKey,
    # _In_reads_bytes_opt_(cbInput) PBYTE pbInput,
    # _In_    DWORD   cbInput,
    # _In_opt_    VOID *pPaddingInfo,
    # _Out_writes_bytes_to_opt_(cbOutput, *pcbResult) PBYTE pbOutput,
    # _In_    DWORD   cbOutput,
    # _Out_   DWORD * pcbResult,
    # _In_    DWORD   dwFlags);
    NCryptDecrypt = ncrypt.NCryptDecrypt
    NCryptDecrypt.restype = SECURITY_STATUS


    if NTDDI_VERSION >= NTDDI_WIN8:
        _NCRYPT_KEY_BLOB_HEADER._fields_ = [
            # size of this structure
            ('cbSize', ULONG),
            ('dwMagic', ULONG),
            # size of the algorithm, in bytes, including terminating 0
            ('cbAlgName', ULONG),
            ('cbKeyData', ULONG),
        ]
        NCRYPT_CIPHER_KEY_BLOB_MAGIC = 0x52485043        # CPHR
        NCRYPT_KDF_KEY_BLOB_MAGIC = 0x3146444B        # KDF1
        NCRYPT_PROTECTED_KEY_BLOB_MAGIC = 0x4B545250        # PRTK
        NCRYPT_CIPHER_KEY_BLOB = "CipherKeyBlob"
        NCRYPT_KDF_KEY_BLOB = "KDFKeyBlob"
        NCRYPT_PROTECTED_KEY_BLOB = "ProtectedKeyBlob"
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)


    NCRYPT_TPM_LOADABLE_KEY_BLOB_HEADER._fields_ = [
        ('magic', DWORD),
        ('cbHeader', DWORD),
        ('cbPublic', DWORD),
        ('cbPrivate', DWORD),
        ('cbName', DWORD),
    ]
    NCRYPT_TPM_LOADABLE_KEY_BLOB_MIN_SIZE = (
        ctypes.sizeof(NCRYPT_TPM_LOADABLE_KEY_BLOB_HEADER)
    )
    NCRYPT_TPM_LOADABLE_KEY_BLOB = "PcpTpmProtectedKeyBlob"
    NCRYPT_TPM_LOADABLE_KEY_BLOB_MAGIC = 0x4D54504B    # 'MTPK'
    NCRYPT_PKCS7_ENVELOPE_BLOB = "PKCS7_ENVELOPE"
    NCRYPT_PKCS8_PRIVATE_KEY_BLOB = "PKCS8_PRIVATEKEY"
    NCRYPT_OPAQUETRANSPORT_BLOB = "OpaqueTransport"

    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        NCRYPT_ISOLATED_KEY_ENVELOPE_BLOB = "ISOLATED_KEY_ENVELOPE"
    # END IF

    # NCryptImportKey flags
    NCRYPT_MACHINE_KEY_FLAG = 0x00000020
    NCRYPT_DO_NOT_FINALIZE_FLAG = 0x00000400
    NCRYPT_EXPORT_LEGACY_FLAG = 0x00000800

    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptImportKey(
    # _In_    NCRYPT_PROV_HANDLE hProvider,
    # _In_opt_ NCRYPT_KEY_HANDLE hImportKey,
    # _In_    LPCWSTR pszBlobType,
    # _In_opt_ NCryptBufferDesc *pParameterList,
    # _Out_   NCRYPT_KEY_HANDLE *phKey,
    # _In_reads_bytes_(cbData) PBYTE pbData,
    # _In_    DWORD   cbData,
    # _In_    DWORD   dwFlags);
    NCryptImportKey = ncrypt.NCryptImportKey
    NCryptImportKey.restype = SECURITY_STATUS

    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptExportKey(
    # _In_    NCRYPT_KEY_HANDLE hKey,
    # _In_opt_ NCRYPT_KEY_HANDLE hExportKey,
    # _In_    LPCWSTR pszBlobType,
    # _In_opt_ NCryptBufferDesc *pParameterList,
    # _Out_writes_bytes_to_opt_(cbOutput, *pcbResult) PBYTE pbOutput,
    # _In_    DWORD   cbOutput,
    # _Out_   DWORD * pcbResult,
    # _In_    DWORD   dwFlags);
    NCryptExportKey = ncrypt.NCryptExportKey
    NCryptExportKey.restype = SECURITY_STATUS

    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptSignHash(
    # _In_    NCRYPT_KEY_HANDLE hKey,
    # _In_opt_    VOID *pPaddingInfo,
    # _In_reads_bytes_(cbHashValue) PBYTE pbHashValue,
    # _In_    DWORD   cbHashValue,
    # _Out_writes_bytes_to_opt_(cbSignature, *pcbResult) PBYTE pbSignature,
    # _In_    DWORD   cbSignature,
    # _Out_   DWORD * pcbResult,
    # _In_    DWORD   dwFlags);
    NCryptSignHash = ncrypt.NCryptSignHash
    NCryptSignHash.restype = SECURITY_STATUS

    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptVerifySignature(
    # _In_    NCRYPT_KEY_HANDLE hKey,
    # _In_opt_    VOID *pPaddingInfo,
    # _In_reads_bytes_(cbHashValue) PBYTE pbHashValue,
    # _In_    DWORD   cbHashValue,
    # _In_reads_bytes_(cbSignature) PBYTE pbSignature,
    # _In_    DWORD   cbSignature,
    # _In_    DWORD   dwFlags);
    NCryptVerifySignature = ncrypt.NCryptVerifySignature
    NCryptVerifySignature.restype = SECURITY_STATUS

    # SECURITY_STATUS
    # WINAPI
    # NCryptDeleteKey(
    # _In_    NCRYPT_KEY_HANDLE hKey,
    # _In_    DWORD   dwFlags);
    NCryptDeleteKey = ncrypt.NCryptDeleteKey
    NCryptDeleteKey.restype = SECURITY_STATUS

    # SECURITY_STATUS
    # WINAPI
    # NCryptFreeObject(
    # _In_    NCRYPT_HANDLE hObject);
    NCryptFreeObject = ncrypt.NCryptFreeObject
    NCryptFreeObject.restype = SECURITY_STATUS


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        ncrypt = ctypes.windll.NCRYPT

        # BOOL
        # WINAPI
        # NCryptIsKeyHandle(
        # _In_    NCRYPT_KEY_HANDLE hKey);
        NCryptIsKeyHandle = ncrypt.NCryptIsKeyHandle
        NCryptIsKeyHandle.restype = BOOL

        # _Check_return_
        # SECURITY_STATUS
        # WINAPI
        # NCryptTranslateHandle(
        # _Out_opt_ NCRYPT_PROV_HANDLE *phProvider,
        # _Out_   NCRYPT_KEY_HANDLE *phKey,
        # _In_    HCRYPTPROV hLegacyProv,
        # _In_opt_ HCRYPTKEY hLegacyKey,
        # _In_opt_ DWORD  dwLegacyKeySpec,
        # _In_    DWORD   dwFlags);
        NCryptTranslateHandle = ncrypt.NCryptTranslateHandle
        NCryptTranslateHandle.restype = SECURITY_STATUS

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # NCryptNotifyChangeKey flags
    NCRYPT_REGISTER_NOTIFY_FLAG = 0x00000001
    NCRYPT_UNREGISTER_NOTIFY_FLAG = 0x00000002
    NCRYPT_MACHINE_KEY_FLAG = 0x00000020
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        ncrypt = ctypes.windll.NCRYPT

        # _Check_return_
        # SECURITY_STATUS
        # WINAPI
        # NCryptNotifyChangeKey(
        # _In_    NCRYPT_PROV_HANDLE hProvider,
        # _Inout_ HANDLE *phEvent,
        # _In_    DWORD   dwFlags);
        NCryptNotifyChangeKey = ncrypt.NCryptNotifyChangeKey
        NCryptNotifyChangeKey.restype = SECURITY_STATUS
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptSecretAgreement(
    # _In_    NCRYPT_KEY_HANDLE hPrivKey,
    # _In_    NCRYPT_KEY_HANDLE hPubKey,
    # _Out_   NCRYPT_SECRET_HANDLE *phAgreedSecret,
    # _In_    DWORD   dwFlags);
    NCryptSecretAgreement = ncrypt.NCryptSecretAgreement
    NCryptSecretAgreement.restype = SECURITY_STATUS

    # _Check_return_
    # SECURITY_STATUS
    # WINAPI
    # NCryptDeriveKey(
    # _In_        NCRYPT_SECRET_HANDLE hSharedSecret,
    # _In_        LPCWSTR              pwszKDF,
    # _In_opt_    NCryptBufferDesc     *pParameterList,
    # _Out_writes_bytes_to_opt_(cbDerivedKey, *pcbResult) PBYTE pbDerivedKey,
    # _In_        DWORD                cbDerivedKey,
    # _Out_       DWORD                *pcbResult,
    # _In_        ULONG                dwFlags);
    NCryptDeriveKey = ncrypt.NCryptDeriveKey
    NCryptDeriveKey.restype = SECURITY_STATUS

    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        pass
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        ncrypt = ctypes.windll.NCRYPT

        # _Check_return_
        # SECURITY_STATUS
        # WINAPI
        # NCryptVerifyClaim(
        # _In_        NCRYPT_KEY_HANDLE   hSubjectKey,
        # _In_opt_    NCRYPT_KEY_HANDLE   hAuthorityKey,
        # _In_        DWORD               dwClaimType,
        # _In_opt_    NCryptBufferDesc    *pParameterList,
        # _In_reads_bytes_(cbClaimBlob) PBYTE pbClaimBlob,
        # _In_        DWORD               cbClaimBlob,
        # _Out_       NCryptBufferDesc    *pOutput,
        # _In_        DWORD               dwFlags);
        NCryptVerifyClaim = ncrypt.NCryptVerifyClaim
        NCryptVerifyClaim.restype = SECURITY_STATUS
    # END IF   (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

    NCRYPT_KEY_STORAGE_INTERFACE_VERSION = (
        BCRYPT_MAKE_INTERFACE_VERSION(1, 0)
    )
    NCRYPT_KEY_STORAGE_INTERFACE_VERSION_2 = (
        BCRYPT_MAKE_INTERFACE_VERSION(2, 0)
    )
    NCRYPT_KEY_STORAGE_INTERFACE_VERSION_3 = (
        BCRYPT_MAKE_INTERFACE_VERSION(3, 0)
    )

    if defined(__cplusplus):
        # Balance extern "C" above
        pass
    # END IF

    if _MSC_VER >= 1200:
        pass
    # END IF
# END IF   __NCRYPT_H__


