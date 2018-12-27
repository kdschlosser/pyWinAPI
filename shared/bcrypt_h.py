import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


WINAPI = None
_NTDEF_ = None
BCRYPT_SUCCESS = None
CONST = None
IN = None
OUT = None
OPTIONAL = None
WINBLUE_KBSPRING14 = None
KERNEL_MODE_CNG = None

class __BCRYPT_KEY_LENGTHS_STRUCT(ctypes.Structure):
    pass


BCRYPT_KEY_LENGTHS_STRUCT = __BCRYPT_KEY_LENGTHS_STRUCT


class _BCRYPT_OID(ctypes.Structure):
    pass


BCRYPT_OID = _BCRYPT_OID


class _BCRYPT_OID_LIST(ctypes.Structure):
    pass


BCRYPT_OID_LIST = _BCRYPT_OID_LIST


class _BCRYPT_PKCS1_PADDING_INFO(ctypes.Structure):
    pass


BCRYPT_PKCS1_PADDING_INFO = _BCRYPT_PKCS1_PADDING_INFO


class _BCRYPT_PSS_PADDING_INFO(ctypes.Structure):
    pass


BCRYPT_PSS_PADDING_INFO = _BCRYPT_PSS_PADDING_INFO


class _BCRYPT_OAEP_PADDING_INFO(ctypes.Structure):
    pass


BCRYPT_OAEP_PADDING_INFO = _BCRYPT_OAEP_PADDING_INFO


class _BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO(ctypes.Structure):
    pass


BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO = _BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO
PBCRYPT_AUTHENTICATED_CIPHER_MODE_INFO = POINTER(_BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO)


class _BCryptBuffer(ctypes.Structure):
    pass


BCryptBuffer = _BCryptBuffer
PBCryptBuffer = POINTER(_BCryptBuffer)


class _BCryptBufferDesc(ctypes.Structure):
    pass


BCryptBufferDesc = _BCryptBufferDesc
PBCryptBufferDesc = POINTER(_BCryptBufferDesc)


class _BCRYPT_KEY_BLOB(ctypes.Structure):
    pass


BCRYPT_KEY_BLOB = _BCRYPT_KEY_BLOB


class _BCRYPT_RSAKEY_BLOB(ctypes.Structure):
    pass


BCRYPT_RSAKEY_BLOB = _BCRYPT_RSAKEY_BLOB


class _BCRYPT_ECCKEY_BLOB(ctypes.Structure):
    pass


BCRYPT_ECCKEY_BLOB = _BCRYPT_ECCKEY_BLOB
PBCRYPT_ECCKEY_BLOB = POINTER(_BCRYPT_ECCKEY_BLOB)


class _SSL_ECCKEY_BLOB(ctypes.Structure):
    pass


SSL_ECCKEY_BLOB = _SSL_ECCKEY_BLOB
PSSL_ECCKEY_BLOB = POINTER(_SSL_ECCKEY_BLOB)


class _BCRYPT_ECCFULLKEY_BLOB(ctypes.Structure):
    pass


BCRYPT_ECCFULLKEY_BLOB = _BCRYPT_ECCFULLKEY_BLOB
PBCRYPT_ECCFULLKEY_BLOB = POINTER(_BCRYPT_ECCFULLKEY_BLOB)


class _BCRYPT_DH_KEY_BLOB(ctypes.Structure):
    pass


BCRYPT_DH_KEY_BLOB = _BCRYPT_DH_KEY_BLOB
PBCRYPT_DH_KEY_BLOB = POINTER(_BCRYPT_DH_KEY_BLOB)


class _BCRYPT_DSA_KEY_BLOB(ctypes.Structure):
    pass


BCRYPT_DSA_KEY_BLOB = _BCRYPT_DSA_KEY_BLOB
PBCRYPT_DSA_KEY_BLOB = POINTER(_BCRYPT_DSA_KEY_BLOB)


class _BCRYPT_DSA_KEY_BLOB_V2(ctypes.Structure):
    pass


BCRYPT_DSA_KEY_BLOB_V2 = _BCRYPT_DSA_KEY_BLOB_V2
PBCRYPT_DSA_KEY_BLOB_V2 = POINTER(_BCRYPT_DSA_KEY_BLOB_V2)


class _BCRYPT_KEY_DATA_BLOB_HEADER(ctypes.Structure):
    pass


BCRYPT_KEY_DATA_BLOB_HEADER = _BCRYPT_KEY_DATA_BLOB_HEADER
PBCRYPT_KEY_DATA_BLOB_HEADER = POINTER(_BCRYPT_KEY_DATA_BLOB_HEADER)


class _BCRYPT_DSA_PARAMETER_HEADER(ctypes.Structure):
    pass


BCRYPT_DSA_PARAMETER_HEADER = _BCRYPT_DSA_PARAMETER_HEADER


class _BCRYPT_DSA_PARAMETER_HEADER_V2(ctypes.Structure):
    pass


BCRYPT_DSA_PARAMETER_HEADER_V2 = _BCRYPT_DSA_PARAMETER_HEADER_V2


class _BCRYPT_ECC_CURVE_NAMES(ctypes.Structure):
    pass


BCRYPT_ECC_CURVE_NAMES = _BCRYPT_ECC_CURVE_NAMES


class _BCRYPT_MULTI_HASH_OPERATION(ctypes.Structure):
    pass


BCRYPT_MULTI_HASH_OPERATION = _BCRYPT_MULTI_HASH_OPERATION


class _BCRYPT_MULTI_OBJECT_LENGTH_STRUCT(ctypes.Structure):
    pass


BCRYPT_MULTI_OBJECT_LENGTH_STRUCT = _BCRYPT_MULTI_OBJECT_LENGTH_STRUCT


class _BCRYPT_ALGORITHM_IDENTIFIER(ctypes.Structure):
    pass


BCRYPT_ALGORITHM_IDENTIFIER = _BCRYPT_ALGORITHM_IDENTIFIER


class _BCRYPT_PROVIDER_NAME(ctypes.Structure):
    pass


BCRYPT_PROVIDER_NAME = _BCRYPT_PROVIDER_NAME


class _BCRYPT_INTERFACE_VERSION(ctypes.Structure):
    pass


BCRYPT_INTERFACE_VERSION = _BCRYPT_INTERFACE_VERSION
PBCRYPT_INTERFACE_VERSION = POINTER(_BCRYPT_INTERFACE_VERSION)


class _CRYPT_INTERFACE_REG(ctypes.Structure):
    pass


CRYPT_INTERFACE_REG = _CRYPT_INTERFACE_REG
PCRYPT_INTERFACE_REG = POINTER(_CRYPT_INTERFACE_REG)


class _CRYPT_IMAGE_REG(ctypes.Structure):
    pass


CRYPT_IMAGE_REG = _CRYPT_IMAGE_REG
PCRYPT_IMAGE_REG = POINTER(_CRYPT_IMAGE_REG)


class _CRYPT_PROVIDER_REG(ctypes.Structure):
    pass


CRYPT_PROVIDER_REG = _CRYPT_PROVIDER_REG
PCRYPT_PROVIDER_REG = POINTER(_CRYPT_PROVIDER_REG)


class _CRYPT_PROVIDERS(ctypes.Structure):
    pass


CRYPT_PROVIDERS = _CRYPT_PROVIDERS
PCRYPT_PROVIDERS = POINTER(_CRYPT_PROVIDERS)


class _CRYPT_CONTEXT_CONFIG(ctypes.Structure):
    pass


CRYPT_CONTEXT_CONFIG = _CRYPT_CONTEXT_CONFIG
PCRYPT_CONTEXT_CONFIG = POINTER(_CRYPT_CONTEXT_CONFIG)


class _CRYPT_CONTEXT_FUNCTION_CONFIG(ctypes.Structure):
    pass


CRYPT_CONTEXT_FUNCTION_CONFIG = _CRYPT_CONTEXT_FUNCTION_CONFIG
PCRYPT_CONTEXT_FUNCTION_CONFIG = POINTER(_CRYPT_CONTEXT_FUNCTION_CONFIG)


class _CRYPT_CONTEXTS(ctypes.Structure):
    pass


CRYPT_CONTEXTS = _CRYPT_CONTEXTS
PCRYPT_CONTEXTS = POINTER(_CRYPT_CONTEXTS)


class _CRYPT_CONTEXT_FUNCTIONS(ctypes.Structure):
    pass


CRYPT_CONTEXT_FUNCTIONS = _CRYPT_CONTEXT_FUNCTIONS
PCRYPT_CONTEXT_FUNCTIONS = POINTER(_CRYPT_CONTEXT_FUNCTIONS)


class _CRYPT_CONTEXT_FUNCTION_PROVIDERS(ctypes.Structure):
    pass


CRYPT_CONTEXT_FUNCTION_PROVIDERS = _CRYPT_CONTEXT_FUNCTION_PROVIDERS
PCRYPT_CONTEXT_FUNCTION_PROVIDERS = POINTER(_CRYPT_CONTEXT_FUNCTION_PROVIDERS)


class _CRYPT_PROPERTY_REF(ctypes.Structure):
    pass


CRYPT_PROPERTY_REF = _CRYPT_PROPERTY_REF
PCRYPT_PROPERTY_REF = POINTER(_CRYPT_PROPERTY_REF)


class _CRYPT_IMAGE_REF(ctypes.Structure):
    pass


CRYPT_IMAGE_REF = _CRYPT_IMAGE_REF
PCRYPT_IMAGE_REF = POINTER(_CRYPT_IMAGE_REF)


class _CRYPT_PROVIDER_REF(ctypes.Structure):
    pass


CRYPT_PROVIDER_REF = _CRYPT_PROVIDER_REF
PCRYPT_PROVIDER_REF = POINTER(_CRYPT_PROVIDER_REF)


class _CRYPT_PROVIDER_REFS(ctypes.Structure):
    pass


CRYPT_PROVIDER_REFS = _CRYPT_PROVIDER_REFS
PCRYPT_PROVIDER_REFS = POINTER(_CRYPT_PROVIDER_REFS)


class _BCRYPT_DH_PARAMETER_HEADER(ctypes.Structure):
    pass


BCRYPT_DH_PARAMETER_HEADER = _BCRYPT_DH_PARAMETER_HEADER

# + ---------------------------------------------------------------------------
# Microsoft Windows
# Copyright (C) Microsoft Corporation, 2004.
# File:  bcrypt.h
# Contents: Cryptographic Primitive API Prototypes and Definitions
# ----------------------------------------------------------------------------
# The __BCRYPT_H__ is used by other header files to conditionally define
# BCrypt-dependent extensions when bcrypt.h has been included.
__BCRYPT_H__ = 1

from pyWinAPI.shared.winapifamily_h import * # NOQA

if _MSC_VER >= 1200:
    pass
# END IF

if defined(__cplusplus):
    pass
# END IF


if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
    if not defined(WINAPI):
        WINAPI = ctypes.WINFUNCTYPE
    # END IF

    if not defined(_NTDEF_):
        # typedef _Return_type_success_(return >= 0) LONG NTSTATUS;
        NTSTATUS = LONG

        PNTSTATUS = POINTER(NTSTATUS)
    # END IF

    if not defined(BCRYPT_SUCCESS):
        def BCRYPT_SUCCESS(Status):
            return Status >= 0
    # END IF

    if not defined(CONST):
        CONST = VOID
    # END IF

    if not defined(IN):
        IN = VOID
    # END IF

    if not defined(OUT):
        OUT = VOID
    # END IF

    if not defined(OPTIONAL):
        OPTIONAL = VOID
    # END IF


    # Alignment macros
    # BCRYPT_OBJECT_ALIGNMENT must be a power of 2
    # We align all our internal data structures to 16 to
    # allow fast XMM memory accesses.
    # BCrypt callers do not need to take any alignment precautions.
    BCRYPT_OBJECT_ALIGNMENT = 16


    # BCRYPT_STRUCT_ALIGNMENT is an alignment macro that we no longer use.
    # It used to align declspec(align(4)) on x86 and declspec(align(8)) on
    # x64/ia64 but
    # all structures that used it contained a pointer so they were already 4/8
    # aligned.
    BCRYPT_STRUCT_ALIGNMENT = VOID


    # DeriveKey KDF Types
    BCRYPT_KDF_HASH = "HASH"
    BCRYPT_KDF_HMAC = "HMAC"
    BCRYPT_KDF_TLS_PRF = "TLS_PRF"
    if NTDDI_VERSION >= NTDDI_WIN7:
        BCRYPT_KDF_SP80056A_CONCAT = "SP800_56A_CONCAT"
    # END IF


    if NTDDI_VERSION >= NTDDI_WINBLUE:
        BCRYPT_KDF_RAW_SECRET = "TRUNCATE"
    # END IF


    if NTDDI_VERSION >= NTDDI_WIN10_RS4:
        BCRYPT_KDF_HKDF = "HKDF"
    # END IF


    # DeriveKey KDF BufferTypes
    # For BCRYPT_KDF_HASH and BCRYPT_KDF_HMAC operations, there may be an
    # arbitrary
    # number of KDF_SECRET_PREPEND and KDF_SECRET_APPEND buffertypes in the
    # parameter list. The BufferTypes are processed in order of appearence
    # within the parameter list.
    KDF_HASH_ALGORITHM = 0x0
    KDF_SECRET_PREPEND = 0x1
    KDF_SECRET_APPEND = 0x2
    KDF_HMAC_KEY = 0x3
    KDF_TLS_PRF_LABEL = 0x4
    KDF_TLS_PRF_SEED = 0x5
    KDF_SECRET_HANDLE = 0x6

    if NTDDI_VERSION >= NTDDI_WIN7:
        KDF_TLS_PRF_PROTOCOL = 0x7
        KDF_ALGORITHMID = 0x8
        KDF_PARTYUINFO = 0x9
        KDF_PARTYVINFO = 0xA
        KDF_SUPPPUBINFO = 0xB
        KDF_SUPPPRIVINFO = 0xC
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN8:
        KDF_LABEL = 0xD
        KDF_CONTEXT = 0xE
        KDF_SALT = 0xF
        KDF_ITERATION_COUNT = 0x10

        # Parameters for BCrypt(/NCrypt)KeyDerivation:
        # Generic parameters:
        # KDF_GENERIC_PARAMETER and KDF_HASH_ALGORITHM are the generic
        # parameters that can be passed for the following KDF algorithms:
        # BCRYPT/NCRYPT_SP800108_CTR_HMAC_ALGORITHM
        # KDF_GENERIC_PARAMETER = KDF_LABEL or 0x00 or KDF_CONTEXT
        # BCRYPT/NCRYPT_SP80056A_CONCAT_ALGORITHM
        # KDF_GENERIC_PARAMETER = KDF_ALGORITHMID or KDF_PARTYUINFO or
        # KDF_PARTYVINFO { | | KDF_SUPPPUBINFO } { | | KDF_SUPPPRIVINFO }
        # BCRYPT/NCRYPT_PBKDF2_ALGORITHM
        # KDF_GENERIC_PARAMETER = KDF_SALT
        # BCRYPT/NCRYPT_CAPI_KDF_ALGORITHM
        # KDF_GENERIC_PARAMETER = Not used
        # BCRYPT/NCRYPT_TLS1_1_KDF_ALGORITHM
        # KDF_GENERIC_PARAMETER = Not used
        # BCRYPT/NCRYPT_TLS1_2_KDF_ALGORITHM
        # KDF_GENERIC_PARAMETER = Not used
        # BCRYPT/NCRYPT_HKDF_ALGORITHM
        # KDF_GENERIC_PARAMETER = Not used
        # KDF specific parameters:
        # For BCRYPT/NCRYPT_SP800108_CTR_HMAC_ALGORITHM:
        # KDF_HASH_ALGORITHM, KDF_LABEL and KDF_CONTEXT are required
        # For BCRYPT/NCRYPT_SP80056A_CONCAT_ALGORITHM:
        # KDF_HASH_ALGORITHM, KDF_ALGORITHMID, KDF_PARTYUINFO, KDF_PARTYVINFO
        # are required
        # KDF_SUPPPUBINFO, KDF_SUPPPRIVINFO are optional
        # For BCRYPT/NCRYPT_PBKDF2_ALGORITHM
        # KDF_HASH_ALGORITHM is required
        # KDF_ITERATION_COUNT, KDF_SALT are optional
        # Iteration count, (if not specified) will default to 10,000
        # For BCRYPT/NCRYPT_CAPI_KDF_ALGORITHM
        # KDF_HASH_ALGORITHM is required
        # For BCRYPT/NCRYPT_TLS1_1_KDF_ALGORITHM
        # KDF_TLS_PRF_LABEL is required
        # KDF_TLS_PRF_SEED is required
        # For BCRYPT/NCRYPT_TLS1_2_KDF_ALGORITHM
        # KDF_HASH_ALGORITHM is required
        # KDF_TLS_PRF_LABEL is required
        # KDF_TLS_PRF_SEED is required
        # For BCRYPT/NCRYPT_HKDF_ALGORITHM
        # KDF_HKDF_INFO is optional
        KDF_GENERIC_PARAMETER = 0x11
        KDF_KEYBITLENGTH = 0x12
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN10_RS4:
        KDF_HKDF_INFO = 0x14
    # END IF

    # DeriveKey Flags:
    # KDF_USE_SECRET_AS_HMAC_KEY_FLAG causes the secret agreement to serve also
    # as the HMAC key. If this flag is used, the KDF_HMAC_KEY parameter should
    # NOT be specified.
    KDF_USE_SECRET_AS_HMAC_KEY_FLAG = 0x1

    # BCrypt structs
    __BCRYPT_KEY_LENGTHS_STRUCT._fields_ = [
        ('dwMinLength', ULONG),
        ('dwMaxLength', ULONG),
        ('dwIncrement', ULONG),
    ]
    BCRYPT_AUTH_TAG_LENGTHS_STRUCT = BCRYPT_KEY_LENGTHS_STRUCT

    _BCRYPT_OID._fields_ = [
        ('cbOID', ULONG),
        ('pbOID', PUCHAR),
    ]

    _BCRYPT_OID_LIST._fields_ = [
        ('dwOIDCount', ULONG),
        ('pOIDs', POINTER(BCRYPT_OID)),
    ]

    _BCRYPT_PKCS1_PADDING_INFO._fields_ = [
        ('pszAlgId', LPCWSTR),
    ]

    _BCRYPT_PSS_PADDING_INFO._fields_ = [
        ('pszAlgId', LPCWSTR),
        ('cbSalt', ULONG),
    ]

    _BCRYPT_OAEP_PADDING_INFO._fields_ = [
        ('pszAlgId', LPCWSTR),
        ('pbLabel', PUCHAR),
        ('cbLabel', ULONG),
    ]
    BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO_VERSION = 1
    BCRYPT_AUTH_MODE_CHAIN_CALLS_FLAG = 0x00000001
    BCRYPT_AUTH_MODE_IN_PROGRESS_FLAG = 0x00000002

    _BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO._fields_ = [
        ('cbSize', ULONG),
        ('dwInfoVersion', ULONG),
        ('pbNonce', PUCHAR),
        ('cbNonce', ULONG),
        ('pbAuthData', PUCHAR),
        ('cbAuthData', ULONG),
        ('pbTag', PUCHAR),
        ('cbTag', ULONG),
        ('pbMacContext', PUCHAR),
        ('cbMacContext', ULONG),
        ('cbAAD', ULONG),
        ('cbData', ULONGLONG),
        ('dwFlags', ULONG),
    ]


    def BCRYPT_INIT_AUTH_MODE_INFO(_AUTH_INFO_STRUCT_):
        RtlZeroMemory(ctypes.byref(_AUTH_INFO_STRUCT_), ctypes.sizeof(BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO))
        _AUTH_INFO_STRUCT_.cbSize = ctypes.sizeof(BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO)
        _AUTH_INFO_STRUCT_.dwInfoVersion = BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO_VERSION
        return _AUTH_INFO_STRUCT_


    # BCrypt String Properties
    # BCrypt(Import/Export)Key BLOB types
    BCRYPT_OPAQUE_KEY_BLOB = "OpaqueKeyBlob"
    BCRYPT_KEY_DATA_BLOB = "KeyDataBlob"

    if NTDDI_VERSION >= NTDDI_WIN7:
        BCRYPT_AES_WRAP_KEY_BLOB = "Rfc3565KeyWrapBlob"
    # END IF

    # BCryptGetProperty strings
    BCRYPT_OBJECT_LENGTH = "ObjectLength"
    BCRYPT_ALGORITHM_NAME = "AlgorithmName"
    BCRYPT_PROVIDER_HANDLE = "ProviderHandle"
    BCRYPT_CHAINING_MODE = "ChainingMode"
    BCRYPT_BLOCK_LENGTH = "BlockLength"
    BCRYPT_KEY_LENGTH = "KeyLength"
    BCRYPT_KEY_OBJECT_LENGTH = "KeyObjectLength"
    BCRYPT_KEY_STRENGTH = "KeyStrength"
    BCRYPT_KEY_LENGTHS = "KeyLengths"
    BCRYPT_BLOCK_SIZE_LIST = "BlockSizeList"
    BCRYPT_EFFECTIVE_KEY_LENGTH = "EffectiveKeyLength"
    BCRYPT_HASH_LENGTH = "HashDigestLength"
    BCRYPT_HASH_OID_LIST = "HashOIDList"
    BCRYPT_PADDING_SCHEMES = "PaddingSchemes"
    BCRYPT_SIGNATURE_LENGTH = "SignatureLength"
    BCRYPT_HASH_BLOCK_LENGTH = "HashBlockLength"
    BCRYPT_AUTH_TAG_LENGTH = "AuthTagLength"

    if NTDDI_VERSION >= NTDDI_WIN7:
        BCRYPT_PRIMITIVE_TYPE = "PrimitiveType"
        BCRYPT_IS_KEYED_HASH = "IsKeyedHash"
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN8:
        BCRYPT_IS_REUSABLE_HASH = "IsReusableHash"
        BCRYPT_MESSAGE_BLOCK_LENGTH = "MessageBlockLength"
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN8:
        BCRYPT_PUBLIC_KEY_LENGTH = "PublicKeyLength"
    # END IF

    # Additional BCryptGetProperty strings for the RNG Platform Crypto Provider
    BCRYPT_PCP_PLATFORM_TYPE_PROPERTY = "PCP_PLATFORM_TYPE"
    BCRYPT_PCP_PROVIDER_VERSION_PROPERTY = "PCP_PROVIDER_VERSION"

    if (NTDDI_VERSION > NTDDI_WINBLUE or (NTDDI_VERSION == NTDDI_WINBLUE and defined(WINBLUE_KBSPRING14))):
        BCRYPT_MULTI_OBJECT_LENGTH = "MultiObjectLength"
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN10_RS4:
        BCRYPT_IS_IFX_TPM_WEAK_KEY = "IsIfxTpmWeakKey"

        # Additional properties for the HKDF on BCRYPT_KEY_HANDLE (and
        # BCRYPT_SECRET_HANDLE). Both the hash algorithm property and
        # one of the "Finalize" properties are required for the key
        # (or secret) to be usable.
        # When the available inputs are the input keying material (IKM)
        # and the salt then the "SALT_AND_FINALIZE" path should be used:
        # - First the function which creates the key (or secret) takes
        # as input the IKM.
        # - Then the hash algorithm should be set via the
        # BCRYPT_HKDF_HASH_ALGORITHM
        # property on BCryptSetProperty.
        # - Finally the salt is input via the BCRYPT_HKDF_SALT_AND_FINALIZE
        # property. The salt parameter is optional; thus the property input
        # is allowed to be NULL.
        # When the available input is the pseudorandom key (PRK) then
        # the "PRK_AND_FINALIZE" path should be used:
        # - First the function which creates the key (or secret) takes
        # as input the PRK.
        # - Then the hash algorithm should be set via the
        # BCRYPT_HKDF_HASH_ALGORITHM
        # property on BCryptSetProperty.
        # - Finally the key (or secret) is finalized via the
        # BCRYPT_HKDF_PRK_AND_FINALIZE property. In this case the input
        # property
        # must be NULL since the PRK was already passed in.
        # After setting one of the two "Finalize" properties the key
        # (or the secret) is finalized and can be used to derive the
        # HKDF output.
        BCRYPT_HKDF_HASH_ALGORITHM = "HkdfHashAlgorithm"
        BCRYPT_HKDF_SALT_AND_FINALIZE = "HkdfSaltAndFinalize"
        BCRYPT_HKDF_PRK_AND_FINALIZE = "HkdfPrkAndFinalize"
    # END IF

    # BCryptSetProperty strings
    BCRYPT_INITIALIZATION_VECTOR = "IV"

    # Property Strings
    BCRYPT_CHAIN_MODE_NA = "ChainingModeN/A"
    BCRYPT_CHAIN_MODE_CBC = "ChainingModeCBC"
    BCRYPT_CHAIN_MODE_ECB = "ChainingModeECB"
    BCRYPT_CHAIN_MODE_CFB = "ChainingModeCFB"
    BCRYPT_CHAIN_MODE_CCM = "ChainingModeCCM"
    BCRYPT_CHAIN_MODE_GCM = "ChainingModeGCM"

    # Supported RSA Padding Types
    BCRYPT_SUPPORTED_PAD_ROUTER = 0x00000001
    BCRYPT_SUPPORTED_PAD_PKCS1_ENC = 0x00000002
    BCRYPT_SUPPORTED_PAD_PKCS1_SIG = 0x00000004
    BCRYPT_SUPPORTED_PAD_OAEP = 0x00000008
    BCRYPT_SUPPORTED_PAD_PSS = 0x00000010

    # BCrypt Flags
    BCRYPT_PROV_DISPATCH = 0x00000001    # BCryptOpenAlgorithmProvider
    BCRYPT_BLOCK_PADDING = 0x00000001    # BCryptEncrypt/Decrypt

    # RSA padding schemes
    BCRYPT_PAD_NONE = 0x00000001
    BCRYPT_PAD_PKCS1 = 0x00000002    # BCryptEncrypt/Decrypt BCryptSignHash/VerifySignature
    BCRYPT_PAD_OAEP = 0x00000004    # BCryptEncrypt/Decrypt
    BCRYPT_PAD_PSS = 0x00000008    # BCryptSignHash/VerifySignature

    if NTDDI_VERSION >= NTDDI_WINBLUE:
        BCRYPT_PAD_PKCS1_OPTIONAL_HASH_OID = 0x00000010        # BCryptVerifySignature
    # END IF

    BCRYPTBUFFER_VERSION = 0

    # Length of buffer, in bytes
    _BCryptBuffer._fields_ = [
        ('cbBuffer', ULONG),
        # Buffer type
        ('BufferType', ULONG),
        # Pointer to buffer
        ('pvBuffer', PVOID),
    ]

    # Version number
    _BCryptBufferDesc._fields_ = [
        ('ulVersion', ULONG),
        # Number of buffers
        ('cBuffers', ULONG),
        # Pointer to array of buffers
        ('pBuffers', PBCryptBuffer),
    ]

    # Primitive handles
    BCRYPT_HANDLE = PVOID
    BCRYPT_ALG_HANDLE = PVOID
    BCRYPT_KEY_HANDLE = PVOID
    BCRYPT_HASH_HANDLE = PVOID
    BCRYPT_SECRET_HANDLE = PVOID

    # Structures used to represent key blobs.
    BCRYPT_PUBLIC_KEY_BLOB = "PUBLICBLOB"
    BCRYPT_PRIVATE_KEY_BLOB = "PRIVATEBLOB"


    _BCRYPT_KEY_BLOB._fields_ = [
        ('Magic', ULONG),
    ]

    # The BCRYPT_RSAPUBLIC_BLOB and BCRYPT_RSAPRIVATE_BLOB blob types are used
    # to transport plaintext RSA keys. These blob types will be supported by
    # all RSA primitive providers.
    # The BCRYPT_RSAPRIVATE_BLOB includes the following values:
    # Public Exponent
    # Modulus
    # Prime1
    # Prime2
    BCRYPT_RSAPUBLIC_BLOB = "RSAPUBLICBLOB"
    BCRYPT_RSAPRIVATE_BLOB = "RSAPRIVATEBLOB"
    LEGACY_RSAPUBLIC_BLOB = "CAPIPUBLICBLOB"
    LEGACY_RSAPRIVATE_BLOB = "CAPIPRIVATEBLOB"
    BCRYPT_RSAPUBLIC_MAGIC = 0x31415352    # RSA1
    BCRYPT_RSAPRIVATE_MAGIC = 0x32415352    # RSA2

    _BCRYPT_RSAKEY_BLOB._fields_ = [
        ('Magic', ULONG),
        ('BitLength', ULONG),
        ('cbPublicExp', ULONG),
        ('cbModulus', ULONG),
        ('cbPrime1', ULONG),
        ('cbPrime2', ULONG),
    ]

    # The BCRYPT_RSAFULLPRIVATE_BLOB blob type is used to transport
    # plaintext private RSA keys. It includes the following values:
    # Public Exponent
    # Modulus
    # Prime1
    # Prime2
    # Private Exponent mod (Prime1 - 1)
    # Private Exponent mod (Prime2 - 1)
    # Inverse of Prime2 mod Prime1
    # PrivateExponent
    BCRYPT_RSAFULLPRIVATE_BLOB = "RSAFULLPRIVATEBLOB"
    BCRYPT_RSAFULLPRIVATE_MAGIC = 0x33415352    # RSA3

    # Properties of secret agreement algorithms
    if NTDDI_VERSION >= NTDDI_WIN8:
        BCRYPT_GLOBAL_PARAMETERS = "SecretAgreementParam"
        BCRYPT_PRIVATE_KEY = "PrivKeyVal"
    # END IF

    # The BCRYPT_ECCPUBLIC_BLOB and BCRYPT_ECCPRIVATE_BLOB blob types are used
    # to transport plaintext ECC keys. These blob types will be supported by
    # all ECC primitive providers.
    BCRYPT_ECCPUBLIC_BLOB = "ECCPUBLICBLOB"
    BCRYPT_ECCPRIVATE_BLOB = "ECCPRIVATEBLOB"

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        BCRYPT_ECCFULLPUBLIC_BLOB = "ECCFULLPUBLICBLOB"
        BCRYPT_ECCFULLPRIVATE_BLOB = "ECCFULLPRIVATEBLOB"
        SSL_ECCPUBLIC_BLOB = "SSLECCPUBLICBLOB"
    # END IF

    BCRYPT_ECDH_PUBLIC_P256_MAGIC = 0x314B4345    # ECK1
    BCRYPT_ECDH_PRIVATE_P256_MAGIC = 0x324B4345    # ECK2
    BCRYPT_ECDH_PUBLIC_P384_MAGIC = 0x334B4345    # ECK3
    BCRYPT_ECDH_PRIVATE_P384_MAGIC = 0x344B4345    # ECK4
    BCRYPT_ECDH_PUBLIC_P521_MAGIC = 0x354B4345    # ECK5
    BCRYPT_ECDH_PRIVATE_P521_MAGIC = 0x364B4345    # ECK6

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        BCRYPT_ECDH_PUBLIC_GENERIC_MAGIC = 0x504B4345        # ECKP
        BCRYPT_ECDH_PRIVATE_GENERIC_MAGIC = 0x564B4345        # ECKV
    # END IF

    BCRYPT_ECDSA_PUBLIC_P256_MAGIC = 0x31534345    # ECS1
    BCRYPT_ECDSA_PRIVATE_P256_MAGIC = 0x32534345    # ECS2
    BCRYPT_ECDSA_PUBLIC_P384_MAGIC = 0x33534345    # ECS3
    BCRYPT_ECDSA_PRIVATE_P384_MAGIC = 0x34534345    # ECS4
    BCRYPT_ECDSA_PUBLIC_P521_MAGIC = 0x35534345    # ECS5
    BCRYPT_ECDSA_PRIVATE_P521_MAGIC = 0x36534345    # ECS6

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        BCRYPT_ECDSA_PUBLIC_GENERIC_MAGIC = 0x50444345        # ECDP
        BCRYPT_ECDSA_PRIVATE_GENERIC_MAGIC = 0x56444345        # ECDV
    # END IF

    _BCRYPT_ECCKEY_BLOB._fields_ = [
        ('dwMagic', ULONG),
        ('cbKey', ULONG),
    ]
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        # SSL ECC Public Blob Version
        _SSL_ECCKEY_BLOB._fields_ = [
            ('dwCurveType', ULONG),
            ('cbKey', ULONG),
        ]

        # ECC Full versions
        BCRYPT_ECC_FULLKEY_BLOB_V1 = 0x1

        class ECC_CURVE_TYPE_ENUM(ENUM):
            BCRYPT_ECC_PRIME_SHORT_WEIERSTRASS_CURVE = 0x1
            BCRYPT_ECC_PRIME_TWISTED_EDWARDS_CURVE = 0x2
            BCRYPT_ECC_PRIME_MONTGOMERY_CURVE = 0x3

        BCRYPT_ECC_PRIME_SHORT_WEIERSTRASS_CURVE = ECC_CURVE_TYPE_ENUM.BCRYPT_ECC_PRIME_SHORT_WEIERSTRASS_CURVE
        BCRYPT_ECC_PRIME_TWISTED_EDWARDS_CURVE = ECC_CURVE_TYPE_ENUM.BCRYPT_ECC_PRIME_TWISTED_EDWARDS_CURVE
        BCRYPT_ECC_PRIME_MONTGOMERY_CURVE = ECC_CURVE_TYPE_ENUM.BCRYPT_ECC_PRIME_MONTGOMERY_CURVE


        class ECC_CURVE_ALG_ID_ENUM(ENUM):
            BCRYPT_NO_CURVE_GENERATION_ALG_ID = 0x0


        BCRYPT_NO_CURVE_GENERATION_ALG_ID = ECC_CURVE_ALG_ID_ENUM.BCRYPT_NO_CURVE_GENERATION_ALG_ID

        # The full version contains the curve parameters as well
        # as the public and potentially private exponent.
        _BCRYPT_ECCFULLKEY_BLOB._fields_ = [
            ('dwMagic', ULONG),
            # Version of the structure
            ('dwVersion', ULONG),
            # Supported curve types.
            ('dwCurveType', ECC_CURVE_TYPE_ENUM),
            # For X.592 verification purposes, if we include Seed we will need
            # to include the algorithm ID.
            ('dwCurveGenerationAlgId', ECC_CURVE_ALG_ID_ENUM),
            # Byte length of the fields P, A, B, X, Y.
            ('cbFieldLength', ULONG),
            # Byte length of the subgroup.
            ('cbSubgroupOrder', ULONG),
            # Byte length of cofactor of G in E.
            ('cbCofactor', ULONG),
            # Byte length of the seed used to generate the curve.
            ('cbSeed', ULONG),
        ]
    # END IF

    # The BCRYPT_DH_PUBLIC_BLOB and BCRYPT_DH_PRIVATE_BLOB blob types are used
    # to transport plaintext DH keys. These blob types will be supported by
    # all DH primitive providers.
    BCRYPT_DH_PUBLIC_BLOB = "DHPUBLICBLOB"
    BCRYPT_DH_PRIVATE_BLOB = "DHPRIVATEBLOB"
    LEGACY_DH_PUBLIC_BLOB = "CAPIDHPUBLICBLOB"
    LEGACY_DH_PRIVATE_BLOB = "CAPIDHPRIVATEBLOB"
    BCRYPT_DH_PUBLIC_MAGIC = 0x42504844    # DHPB
    BCRYPT_DH_PRIVATE_MAGIC = 0x56504844    # DHPV

    _BCRYPT_DH_KEY_BLOB._fields_ = [
        ('dwMagic', ULONG),
        ('cbKey', ULONG),
    ]

    # Property Strings for DH
    BCRYPT_DH_PARAMETERS = "DHParameters"
    BCRYPT_DH_PARAMETERS_MAGIC = 0x4D504844    # DHPM

    _BCRYPT_DH_PARAMETER_HEADER._fields_ = [
        ('cbLength', ULONG),
        ('dwMagic', ULONG),
        ('cbKeyLength', ULONG)
    ]

    # The BCRYPT_DSA_PUBLIC_BLOB and BCRYPT_DSA_PRIVATE_BLOB blob types are
    # used
    # to transport plaintext DSA keys. These blob types will be supported by
    # all DSA primitive providers.
    BCRYPT_DSA_PUBLIC_BLOB = "DSAPUBLICBLOB"
    BCRYPT_DSA_PRIVATE_BLOB = "DSAPRIVATEBLOB"
    LEGACY_DSA_PUBLIC_BLOB = "CAPIDSAPUBLICBLOB"
    LEGACY_DSA_PRIVATE_BLOB = "CAPIDSAPRIVATEBLOB"
    LEGACY_DSA_V2_PUBLIC_BLOB = "V2CAPIDSAPUBLICBLOB"
    LEGACY_DSA_V2_PRIVATE_BLOB = "V2CAPIDSAPRIVATEBLOB"
    BCRYPT_DSA_PUBLIC_MAGIC = 0x42505344    # DSPB
    BCRYPT_DSA_PRIVATE_MAGIC = 0x56505344    # DSPV
    if NTDDI_VERSION >= NTDDI_WIN8:
        BCRYPT_DSA_PUBLIC_MAGIC_V2 = 0x32425044        # DPB2
        BCRYPT_DSA_PRIVATE_MAGIC_V2 = 0x32565044        # DPV2
    # END IF


    _BCRYPT_DSA_KEY_BLOB._fields_ = [
        ('dwMagic', ULONG),
        ('cbKey', ULONG),
        ('Count', UCHAR * 4),
        ('Seed', UCHAR * 20),
        ('q', UCHAR * 20),
    ]
    if NTDDI_VERSION >= NTDDI_WIN8:
        class HASHALGORITHM_ENUM(ENUM):
            DSA_HASH_ALGORITHM_SHA1 = 1
            DSA_HASH_ALGORITHM_SHA256 = 2
            DSA_HASH_ALGORITHM_SHA512 = 3

        DSA_HASH_ALGORITHM_SHA1 = HASHALGORITHM_ENUM.DSA_HASH_ALGORITHM_SHA1
        DSA_HASH_ALGORITHM_SHA256 = HASHALGORITHM_ENUM.DSA_HASH_ALGORITHM_SHA256
        DSA_HASH_ALGORITHM_SHA512 = HASHALGORITHM_ENUM.DSA_HASH_ALGORITHM_SHA512


        class DSAFIPSVERSION_ENUM(ENUM):
            DSA_FIPS186_2 = 1
            DSA_FIPS186_3 = 2

        DSA_FIPS186_2 = DSAFIPSVERSION_ENUM.DSA_FIPS186_2
        DSA_FIPS186_3 = DSAFIPSVERSION_ENUM.DSA_FIPS186_3

        _BCRYPT_DSA_KEY_BLOB_V2._fields_ = [
            ('dwMagic', ULONG),
            ('cbKey', ULONG),
            ('hashAlgorithm', HASHALGORITHM_ENUM),
            ('standardVersion', DSAFIPSVERSION_ENUM),
            ('cbSeedLength', ULONG),
            ('cbGroupSize', ULONG),
            ('Count', UCHAR * 4),
        ]
    # END IF


    _BCRYPT_KEY_DATA_BLOB_HEADER._fields_ = [
        ('dwMagic', ULONG),
        ('dwVersion', ULONG),
        ('cbKeyData', ULONG),
    ]
    BCRYPT_KEY_DATA_BLOB_MAGIC = 0x4D42444B    # Key Data Blob Magic (KDBM)
    BCRYPT_KEY_DATA_BLOB_VERSION1 = 0x1

    # Property Strings for DSA
    BCRYPT_DSA_PARAMETERS = "DSAParameters"
    BCRYPT_DSA_PARAMETERS_MAGIC = 0x4D505344    # DSPM
    if NTDDI_VERSION >= NTDDI_WIN8:
        BCRYPT_DSA_PARAMETERS_MAGIC_V2 = 0x324D5044        # DPM2
    # END IF


    _BCRYPT_DSA_PARAMETER_HEADER._fields_ = [
        ('cbLength', ULONG),
        ('dwMagic', ULONG),
        ('cbKeyLength', ULONG),
        ('Count', UCHAR * 4),
        ('Seed', UCHAR * 20),
        ('q', UCHAR * 20),
    ]
    if NTDDI_VERSION >= NTDDI_WIN8:
        _BCRYPT_DSA_PARAMETER_HEADER_V2._fields_ = [
            ('cbLength', ULONG),
            ('dwMagic', ULONG),
            ('cbKeyLength', ULONG),
            ('hashAlgorithm', HASHALGORITHM_ENUM),
            ('standardVersion', DSAFIPSVERSION_ENUM),
            ('cbSeedLength', ULONG),
            ('cbGroupSize', ULONG),
            ('Count', UCHAR * 4),
        ]
    # END IF


    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        # Property Strings for ECC
        BCRYPT_ECC_PARAMETERS = "ECCParameters"
        BCRYPT_ECC_CURVE_NAME = "ECCCurveName"
        BCRYPT_ECC_CURVE_NAME_LIST = "ECCCurveNameList"
        BCRYPT_ECC_PARAMETERS_MAGIC = 0x50434345        # ECCP


        _BCRYPT_ECC_CURVE_NAMES._fields_ = [
            ('dwEccCurveNames', ULONG),
            ('pEccCurveNames', POINTER(LPWSTR)),
        ]

        # ECC Curve Names
        BCRYPT_ECC_CURVE_BRAINPOOLP160R1 = "brainpoolP160r1"
        BCRYPT_ECC_CURVE_BRAINPOOLP160T1 = "brainpoolP160t1"
        BCRYPT_ECC_CURVE_BRAINPOOLP192R1 = "brainpoolP192r1"
        BCRYPT_ECC_CURVE_BRAINPOOLP192T1 = "brainpoolP192t1"
        BCRYPT_ECC_CURVE_BRAINPOOLP224R1 = "brainpoolP224r1"
        BCRYPT_ECC_CURVE_BRAINPOOLP224T1 = "brainpoolP224t1"
        BCRYPT_ECC_CURVE_BRAINPOOLP256R1 = "brainpoolP256r1"
        BCRYPT_ECC_CURVE_BRAINPOOLP256T1 = "brainpoolP256t1"
        BCRYPT_ECC_CURVE_BRAINPOOLP320R1 = "brainpoolP320r1"
        BCRYPT_ECC_CURVE_BRAINPOOLP320T1 = "brainpoolP320t1"
        BCRYPT_ECC_CURVE_BRAINPOOLP384R1 = "brainpoolP384r1"
        BCRYPT_ECC_CURVE_BRAINPOOLP384T1 = "brainpoolP384t1"
        BCRYPT_ECC_CURVE_BRAINPOOLP512R1 = "brainpoolP512r1"
        BCRYPT_ECC_CURVE_BRAINPOOLP512T1 = "brainpoolP512t1"
        BCRYPT_ECC_CURVE_25519 = "curve25519"
        BCRYPT_ECC_CURVE_EC192WAPI = "ec192wapi"
        BCRYPT_ECC_CURVE_NISTP192 = "nistP192"
        BCRYPT_ECC_CURVE_NISTP224 = "nistP224"
        BCRYPT_ECC_CURVE_NISTP256 = "nistP256"
        BCRYPT_ECC_CURVE_NISTP384 = "nistP384"
        BCRYPT_ECC_CURVE_NISTP521 = "nistP521"
        BCRYPT_ECC_CURVE_NUMSP256T1 = "numsP256t1"
        BCRYPT_ECC_CURVE_NUMSP384T1 = "numsP384t1"
        BCRYPT_ECC_CURVE_NUMSP512T1 = "numsP512t1"
        BCRYPT_ECC_CURVE_SECP160K1 = "secP160k1"
        BCRYPT_ECC_CURVE_SECP160R1 = "secP160r1"
        BCRYPT_ECC_CURVE_SECP160R2 = "secP160r2"
        BCRYPT_ECC_CURVE_SECP192K1 = "secP192k1"
        BCRYPT_ECC_CURVE_SECP192R1 = "secP192r1"
        BCRYPT_ECC_CURVE_SECP224K1 = "secP224k1"
        BCRYPT_ECC_CURVE_SECP224R1 = "secP224r1"
        BCRYPT_ECC_CURVE_SECP256K1 = "secP256k1"
        BCRYPT_ECC_CURVE_SECP256R1 = "secP256r1"
        BCRYPT_ECC_CURVE_SECP384R1 = "secP384r1"
        BCRYPT_ECC_CURVE_SECP521R1 = "secP521r1"
        BCRYPT_ECC_CURVE_WTLS7 = "wtls7"
        BCRYPT_ECC_CURVE_WTLS9 = "wtls9"
        BCRYPT_ECC_CURVE_WTLS12 = "wtls12"
        BCRYPT_ECC_CURVE_X962P192V1 = "x962P192v1"
        BCRYPT_ECC_CURVE_X962P192V2 = "x962P192v2"
        BCRYPT_ECC_CURVE_X962P192V3 = "x962P192v3"
        BCRYPT_ECC_CURVE_X962P239V1 = "x962P239v1"
        BCRYPT_ECC_CURVE_X962P239V2 = "x962P239v2"
        BCRYPT_ECC_CURVE_X962P239V3 = "x962P239v3"
        BCRYPT_ECC_CURVE_X962P256V1 = "x962P256v1"
    # END IF


    # Operation types used in BCRYPT_MULTI_HASH_OPERATION structures
    class BCRYPT_HASH_OPERATION_TYPE(ENUM):
        BCRYPT_HASH_OPERATION_HASH_DATA = 1
        BCRYPT_HASH_OPERATION_FINISH_HASH = 2

    BCRYPT_HASH_OPERATION_HASH_DATA = BCRYPT_HASH_OPERATION_TYPE.BCRYPT_HASH_OPERATION_HASH_DATA
    BCRYPT_HASH_OPERATION_FINISH_HASH = BCRYPT_HASH_OPERATION_TYPE.BCRYPT_HASH_OPERATION_FINISH_HASH

    # index of hash object
    _BCRYPT_MULTI_HASH_OPERATION._fields_ = [
        ('iHash', ULONG),
        # operation to be performed
        ('hashOperation', BCRYPT_HASH_OPERATION_TYPE),
        # data to be hashed, or result buffer
        ('pbBuffer', PUCHAR),
        ('cbBuffer', ULONG),
    ]

    # Enum to specify type of multi-operation is passed to
    # BCryptProcesMultiOperations
    class BCRYPT_MULTI_OPERATION_TYPE(ENUM):
        BCRYPT_OPERATION_TYPE_HASH = 1

    BCRYPT_OPERATION_TYPE_HASH = BCRYPT_MULTI_OPERATION_TYPE.BCRYPT_OPERATION_TYPE_HASH

    _BCRYPT_MULTI_OBJECT_LENGTH_STRUCT._fields_ = [
        ('cbPerObject', ULONG),
        # required size for N elements is (cbPerObject + N * cbPerElement)
        ('cbPerElement', ULONG),
    ]

    # Microsoft built-in providers.
    MS_PRIMITIVE_PROVIDER = "Microsoft Primitive Provider"
    MS_PLATFORM_CRYPTO_PROVIDER = "Microsoft Platform Crypto Provider"

    # Common algorithm identifiers.
    BCRYPT_RSA_ALGORITHM = "RSA"
    BCRYPT_RSA_SIGN_ALGORITHM = "RSA_SIGN"
    BCRYPT_DH_ALGORITHM = "DH"
    BCRYPT_DSA_ALGORITHM = "DSA"
    BCRYPT_RC2_ALGORITHM = "RC2"
    BCRYPT_RC4_ALGORITHM = "RC4"
    BCRYPT_AES_ALGORITHM = "AES"
    BCRYPT_DES_ALGORITHM = "DES"
    BCRYPT_DESX_ALGORITHM = "DESX"
    BCRYPT_3DES_ALGORITHM = "3DES"
    BCRYPT_3DES_112_ALGORITHM = "3DES_112"
    BCRYPT_MD2_ALGORITHM = "MD2"
    BCRYPT_MD4_ALGORITHM = "MD4"
    BCRYPT_MD5_ALGORITHM = "MD5"
    BCRYPT_SHA1_ALGORITHM = "SHA1"
    BCRYPT_SHA256_ALGORITHM = "SHA256"
    BCRYPT_SHA384_ALGORITHM = "SHA384"
    BCRYPT_SHA512_ALGORITHM = "SHA512"
    BCRYPT_AES_GMAC_ALGORITHM = "AES-GMAC"
    BCRYPT_AES_CMAC_ALGORITHM = "AES-CMAC"
    BCRYPT_ECDSA_P256_ALGORITHM = "ECDSA_P256"
    BCRYPT_ECDSA_P384_ALGORITHM = "ECDSA_P384"
    BCRYPT_ECDSA_P521_ALGORITHM = "ECDSA_P521"
    BCRYPT_ECDH_P256_ALGORITHM = "ECDH_P256"
    BCRYPT_ECDH_P384_ALGORITHM = "ECDH_P384"
    BCRYPT_ECDH_P521_ALGORITHM = "ECDH_P521"
    BCRYPT_RNG_ALGORITHM = "RNG"
    BCRYPT_RNG_FIPS186_DSA_ALGORITHM = "FIPS186DSARNG"
    BCRYPT_RNG_DUAL_EC_ALGORITHM = "DUALECRNG"
    if NTDDI_VERSION >= NTDDI_WIN8:
        BCRYPT_SP800108_CTR_HMAC_ALGORITHM = "SP800_108_CTR_HMAC"
        BCRYPT_SP80056A_CONCAT_ALGORITHM = "SP800_56A_CONCAT"
        BCRYPT_PBKDF2_ALGORITHM = "PBKDF2"
        BCRYPT_CAPI_KDF_ALGORITHM = "CAPI_KDF"
        BCRYPT_TLS1_1_KDF_ALGORITHM = "TLS1_1_KDF"
        BCRYPT_TLS1_2_KDF_ALGORITHM = "TLS1_2_KDF"
    # END IF


    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        BCRYPT_ECDSA_ALGORITHM = "ECDSA"
        BCRYPT_ECDH_ALGORITHM = "ECDH"
        BCRYPT_XTS_AES_ALGORITHM = "XTS-AES"
    # END IF


    if NTDDI_VERSION >= NTDDI_WIN10_RS4:
        BCRYPT_HKDF_ALGORITHM = "HKDF"
    # END IF


    # Interfaces
    BCRYPT_CIPHER_INTERFACE = 0x00000001
    BCRYPT_HASH_INTERFACE = 0x00000002
    BCRYPT_ASYMMETRIC_ENCRYPTION_INTERFACE = 0x00000003
    BCRYPT_SECRET_AGREEMENT_INTERFACE = 0x00000004
    BCRYPT_SIGNATURE_INTERFACE = 0x00000005
    BCRYPT_RNG_INTERFACE = 0x00000006
    if NTDDI_VERSION >= NTDDI_WIN8:
        BCRYPT_KEY_DERIVATION_INTERFACE = 0x00000007
    # END IF


    # Algorithm pseudo-handles
    # Pseudo-handles are distinguished from normal handles by being 1 mod 16
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        BCRYPT_MD2_ALG_HANDLE = 0x00000001
        BCRYPT_MD4_ALG_HANDLE = 0x00000011
        BCRYPT_MD5_ALG_HANDLE = 0x00000021
        BCRYPT_SHA1_ALG_HANDLE = 0x00000031
        BCRYPT_SHA256_ALG_HANDLE = 0x00000041
        BCRYPT_SHA384_ALG_HANDLE = 0x00000051
        BCRYPT_SHA512_ALG_HANDLE = 0x00000061
        BCRYPT_RC4_ALG_HANDLE = 0x00000071
        BCRYPT_RNG_ALG_HANDLE = 0x00000081
        BCRYPT_HMAC_MD5_ALG_HANDLE = 0x00000091
        BCRYPT_HMAC_SHA1_ALG_HANDLE = 0x000000A1
        BCRYPT_HMAC_SHA256_ALG_HANDLE = 0x000000B1
        BCRYPT_HMAC_SHA384_ALG_HANDLE = 0x000000C1
        BCRYPT_HMAC_SHA512_ALG_HANDLE = 0x000000D1
        BCRYPT_RSA_ALG_HANDLE = 0x000000E1
        BCRYPT_ECDSA_ALG_HANDLE = 0x000000F1
        BCRYPT_AES_CMAC_ALG_HANDLE = 0x00000101
        BCRYPT_AES_GMAC_ALG_HANDLE = 0x00000111
        BCRYPT_HMAC_MD2_ALG_HANDLE = 0x00000121
        BCRYPT_HMAC_MD4_ALG_HANDLE = 0x00000131
        BCRYPT_3DES_CBC_ALG_HANDLE = 0x00000141
        BCRYPT_3DES_ECB_ALG_HANDLE = 0x00000151
        BCRYPT_3DES_CFB_ALG_HANDLE = 0x00000161
        BCRYPT_3DES_112_CBC_ALG_HANDLE = 0x00000171
        BCRYPT_3DES_112_ECB_ALG_HANDLE = 0x00000181
        BCRYPT_3DES_112_CFB_ALG_HANDLE = 0x00000191
        BCRYPT_AES_CBC_ALG_HANDLE = 0x000001A1
        BCRYPT_AES_ECB_ALG_HANDLE = 0x000001B1
        BCRYPT_AES_CFB_ALG_HANDLE = 0x000001C1
        BCRYPT_AES_CCM_ALG_HANDLE = 0x000001D1
        BCRYPT_AES_GCM_ALG_HANDLE = 0x000001E1
        BCRYPT_DES_CBC_ALG_HANDLE = 0x000001F1
        BCRYPT_DES_ECB_ALG_HANDLE = 0x00000201
        BCRYPT_DES_CFB_ALG_HANDLE = 0x00000211
        BCRYPT_DESX_CBC_ALG_HANDLE = 0x00000221
        BCRYPT_DESX_ECB_ALG_HANDLE = 0x00000231
        BCRYPT_DESX_CFB_ALG_HANDLE = 0x00000241
        BCRYPT_RC2_CBC_ALG_HANDLE = 0x00000251
        BCRYPT_RC2_ECB_ALG_HANDLE = 0x00000261
        BCRYPT_RC2_CFB_ALG_HANDLE = 0x00000271
        BCRYPT_DH_ALG_HANDLE = 0x00000281
        BCRYPT_ECDH_ALG_HANDLE = 0x00000291
        BCRYPT_ECDH_P256_ALG_HANDLE = 0x000002A1
        BCRYPT_ECDH_P384_ALG_HANDLE = 0x000002B1
        BCRYPT_ECDH_P521_ALG_HANDLE = 0x000002C1
        BCRYPT_DSA_ALG_HANDLE = 0x000002D1
        BCRYPT_ECDSA_P256_ALG_HANDLE = 0x000002E1
        BCRYPT_ECDSA_P384_ALG_HANDLE = 0x000002F1
        BCRYPT_ECDSA_P521_ALG_HANDLE = 0x00000301
        BCRYPT_RSA_SIGN_ALG_HANDLE = 0x00000311
        BCRYPT_CAPI_KDF_ALG_HANDLE = 0x00000321
        BCRYPT_PBKDF2_ALG_HANDLE = 0x00000331
        BCRYPT_SP800108_CTR_HMAC_ALG_HANDLE = 0x00000341
        BCRYPT_SP80056A_CONCAT_ALG_HANDLE = 0x00000351
        BCRYPT_TLS1_1_KDF_ALG_HANDLE = 0x00000361
        BCRYPT_TLS1_2_KDF_ALG_HANDLE = 0x00000371
        BCRYPT_XTS_AES_ALG_HANDLE = 0x00000381
        BCRYPT_HKDF_ALG_HANDLE = 0x00000391
    # END IF


    # Primitive algorithm provider functions.
    BCRYPT_ALG_HANDLE_HMAC_FLAG = 0x00000008
    BCRYPT_HASH_REUSABLE_FLAG = 0x00000020
    if NTDDI_VERSION >= NTDDI_WIN8:
        BCRYPT_CAPI_AES_FLAG = 0x00000010
    # END IF


    if (NTDDI_VERSION > NTDDI_WINBLUE or (NTDDI_VERSION == NTDDI_WINBLUE and defined(WINBLUE_KBSPRING14))):
        BCRYPT_MULTI_FLAG = 0x00000040
    # END IF


    # The BUFFERS_LOCKED flag used in BCryptEncrypt/BCryptDecrypt signals that
    # the pbInput and pbOutput buffers have been locked
    # (see MmProbeAndLockPages)
    # and CNG may not lock the buffers again.
    # This flag applies only to kernel mode, it is ignored in user mode.
    BCRYPT_BUFFERS_LOCKED_FLAG = 0x00000040

    # The EXTENDED_KEYSIZE flag extends the supported set of key sizes.
    # The original design has a per-algorithm maximum key size, and
    # BCryptGenerateSymmetricKey truncates any longer input to the maximum key
    # size for that
    # algorithm. Some callers depend on this feature and pass in large buffers.
    # This makes it impossible to silently extend the supported key size
    # without breaking
    # backward compatibility.
    # This flag indicates that the extended key size support is requested.
    # It has the following consequences:
    # - BCryptGetProperty will report a new maximum key size for
    # BCRYPT_KEY_LENGTHS.
    # - BCryptGenerateSymmetricKey will support the longer key sizes.
    # - BCryptGenerateSymmetricKey will no longer truncate keys that are too
    # long, but return an error instead.
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        BCRYPT_EXTENDED_KEYSIZE = 0x00000080
    # END IF


    # ENABLE_INCOMPATIBLE_FIPS_CHECKS flag enables some FIPS 140-2-mandated
    # checks that are incompatible
    # with the original algorithm.
    # Starting in Redstone 1 (summer 2016 release of Win10) this flag has the
    # following effect on the
    # Microsoft default algorithm provider.
    # - BCryptGenerateSymmetricKey when generating an XTS-AES key with this
    # flag specified and FIPS mode enabled
    # will verify that the two halves of the key are not identical. If they
    # are, an error is returned.
    # This is actually incompatible with the NIST SP 800-38E and IEEE Std
    # 1619-2007 definitions
    # of XTS-AES. Rather than change the standard, NIST added this requirement
    # in the FIPS 140-2
    # implementation guidance.
    # This check breaks existing usage of the algorithm, which is why we only
    # perform the check when the
    # caller explicitly asks for it.
    # Use of this flag for any algorithm other than XTS-AES generates an error.
    # Note that this flag is not supported for BCryptImportKey.
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        BCRYPT_ENABLE_INCOMPATIBLE_FIPS_CHECKS = 0x00000100
    # END IF

    ncrypt = ctypes.windll.NCRYPT

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptOpenAlgorithmProvider(
    # _Out_       BCRYPT_ALG_HANDLE   *phAlgorithm,
    # _In_        LPCWSTR pszAlgId,
    # _In_opt_    LPCWSTR pszImplementation,
    # _In_        ULONG   dwFlags);
    BCryptOpenAlgorithmProvider = ncrypt.BCryptOpenAlgorithmProvider
    BCryptOpenAlgorithmProvider.restype = NTSTATUS


    # AlgOperations flags for use with BCryptEnumAlgorithms()
    BCRYPT_CIPHER_OPERATION = 0x00000001
    BCRYPT_HASH_OPERATION = 0x00000002
    BCRYPT_ASYMMETRIC_ENCRYPTION_OPERATION = 0x00000004
    BCRYPT_SECRET_AGREEMENT_OPERATION = 0x00000008
    BCRYPT_SIGNATURE_OPERATION = 0x00000010
    BCRYPT_RNG_OPERATION = 0x00000020

    if NTDDI_VERSION >= NTDDI_WIN8:
        BCRYPT_KEY_DERIVATION_OPERATION = 0x00000040
    # END IF

    # USE EXTREME CAUTION: editing comments that contain "certenrolls_*" tokens
    # could break building CertEnroll idl files:
    # certenrolls_begin -- BCRYPT_ALGORITHM_IDENTIFIER
    _BCRYPT_ALGORITHM_IDENTIFIER._fields_ = [
        ('pszName', LPWSTR),
        ('dwClass', ULONG),
        ('dwFlags', ULONG),
    ]

    # certenrolls_end
    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptEnumAlgorithms(
    # _In_    ULONG   dwAlgOperations,
    # _Out_   ULONG   *pAlgCount,
    # _Out_   BCRYPT_ALGORITHM_IDENTIFIER **ppAlgList,
    # _In_    ULONG   dwFlags);
    BCryptEnumAlgorithms = ncrypt.BCryptEnumAlgorithms
    BCryptEnumAlgorithms.restype = NTSTATUS


    _BCRYPT_PROVIDER_NAME._fields_ = [
        ('pszProviderName', LPWSTR),
    ]
    cng = ctypes.windll.CNG

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptEnumProviders(
    # _In_    LPCWSTR pszAlgId,
    # _Out_   ULONG   *pImplCount,
    # _Out_   BCRYPT_PROVIDER_NAME    **ppImplList,
    # _In_    ULONG   dwFlags);
    BCryptEnumProviders = cng.BCryptEnumProviders
    BCryptEnumProviders.restype = NTSTATUS

    # Unused flags. Kept for backward compatibility.
    # "Flags for use with BCryptGetProperty and BCryptSetProperty"
    BCRYPT_PUBLIC_KEY_FLAG = 0x00000001
    BCRYPT_PRIVATE_KEY_FLAG = 0x00000002

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptGetProperty(
    # _In_                                        BCRYPT_HANDLE   hObject,
    # _In_                                        LPCWSTR pszProperty,
    # _Out_writes_bytes_to_opt_(cbOutput, *pcbResult) PUCHAR   pbOutput,
    # _In_                                        ULONG   cbOutput,
    # _Out_                                       ULONG   *pcbResult,
    # _In_                                        ULONG   dwFlags);
    BCryptGetProperty = ncrypt.BCryptGetProperty
    BCryptGetProperty.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptSetProperty(
    # _Inout_                 BCRYPT_HANDLE   hObject,
    # _In_                    LPCWSTR pszProperty,
    # _In_reads_bytes_(cbInput)    PUCHAR   pbInput,
    # _In_                    ULONG   cbInput,
    # _In_                    ULONG   dwFlags);
    BCryptSetProperty = ncrypt.BCryptSetProperty
    BCryptSetProperty.restype = NTSTATUS

    # NTSTATUS
    # WINAPI
    # BCryptCloseAlgorithmProvider(
    # _Inout_ BCRYPT_ALG_HANDLE   hAlgorithm,
    # _In_    ULONG   dwFlags);
    BCryptCloseAlgorithmProvider = ncrypt.BCryptCloseAlgorithmProvider
    BCryptCloseAlgorithmProvider.restype = WINAPI

    # VOID
    # WINAPI
    # BCryptFreeBuffer(
    # _In_ PVOID   pvBuffer);
    BCryptFreeBuffer = cng.BCryptFreeBuffer
    BCryptFreeBuffer.restype = WINAPI

    # Primitive encryption functions.
    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptGenerateSymmetricKey(
    # _Inout_                             BCRYPT_ALG_HANDLE   hAlgorithm,
    # _Out_                               BCRYPT_KEY_HANDLE   *phKey,
    # _Out_writes_bytes_all_opt_(cbKeyObject)  PUCHAR   pbKeyObject,
    # _In_                                ULONG   cbKeyObject,
    # _In_reads_bytes_(cbSecret)               PUCHAR   pbSecret,
    # _In_                                ULONG   cbSecret,
    # _In_                                ULONG   dwFlags);
    BCryptGenerateSymmetricKey = ncrypt.BCryptGenerateSymmetricKey
    BCryptGenerateSymmetricKey.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptGenerateKeyPair(
    # _Inout_ BCRYPT_ALG_HANDLE   hAlgorithm,
    # _Out_   BCRYPT_KEY_HANDLE   *phKey,
    # _In_    ULONG   dwLength,
    # _In_    ULONG   dwFlags);
    BCryptGenerateKeyPair = cng.BCryptGenerateKeyPair
    BCryptGenerateKeyPair.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptEncrypt(
    # _Inout_                                     BCRYPT_KEY_HANDLE hKey,
    # _In_reads_bytes_opt_(cbInput)                    PUCHAR   pbInput,
    # _In_                                        ULONG   cbInput,
    # _In_opt_                                    VOID    *pPaddingInfo,
    # _Inout_updates_bytes_opt_(cbIV)                    PUCHAR   pbIV,
    # _In_                                        ULONG   cbIV,
    # _Out_writes_bytes_to_opt_(cbOutput, *pcbResult) PUCHAR   pbOutput,
    # _In_                                        ULONG   cbOutput,
    # _Out_                                       ULONG   *pcbResult,
    # _In_                                        ULONG   dwFlags);
    BCryptEncrypt = cng.BCryptEncrypt
    BCryptEncrypt.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptDecrypt(
    # _Inout_                                     BCRYPT_KEY_HANDLE   hKey,
    # _In_reads_bytes_opt_(cbInput)                    PUCHAR   pbInput,
    # _In_                                        ULONG   cbInput,
    # _In_opt_                                    VOID    *pPaddingInfo,
    # _Inout_updates_bytes_opt_(cbIV)                    PUCHAR   pbIV,
    # _In_                                        ULONG   cbIV,
    # _Out_writes_bytes_to_opt_(cbOutput, *pcbResult) PUCHAR   pbOutput,
    # _In_                                        ULONG   cbOutput,
    # _Out_                                       ULONG   *pcbResult,
    # _In_                                        ULONG   dwFlags);
    BCryptDecrypt = ncrypt.BCryptDecrypt
    BCryptDecrypt.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptExportKey(
    # _In_                                        BCRYPT_KEY_HANDLE   hKey,
    # _In_opt_                                    BCRYPT_KEY_HANDLE   hExportKey,
    # _In_                                        LPCWSTR pszBlobType,
    # _Out_writes_bytes_to_opt_(cbOutput, *pcbResult) PUCHAR   pbOutput,
    # _In_                                        ULONG   cbOutput,
    # _Out_                                       ULONG   *pcbResult,
    # _In_                                        ULONG   dwFlags);
    BCryptExportKey = ncrypt.BCryptExportKey
    BCryptExportKey.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptImportKey(
    # _In_                                BCRYPT_ALG_HANDLE hAlgorithm,
    # _In_opt_                            BCRYPT_KEY_HANDLE hImportKey,
    # _In_                                LPCWSTR pszBlobType,
    # _Out_                               BCRYPT_KEY_HANDLE *phKey,
    # _Out_writes_bytes_all_opt_(cbKeyObject)  PUCHAR   pbKeyObject,
    # _In_                                ULONG   cbKeyObject,
    # _In_reads_bytes_(cbInput)                PUCHAR   pbInput,
    # _In_                                ULONG   cbInput,
    # _In_                                ULONG   dwFlags);
    BCryptImportKey = ncrypt.BCryptImportKey
    BCryptImportKey.restype = NTSTATUS

    BCRYPT_NO_KEY_VALIDATION = 0x00000008

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptImportKeyPair(
    # _In_                            BCRYPT_ALG_HANDLE hAlgorithm,
    # _In_opt_                        BCRYPT_KEY_HANDLE hImportKey,
    # _In_                            LPCWSTR pszBlobType,
    # _Out_                           BCRYPT_KEY_HANDLE *phKey,
    # _In_reads_bytes_(cbInput)            PUCHAR   pbInput,
    # _In_                            ULONG   cbInput,
    # _In_                            ULONG   dwFlags);
    BCryptImportKeyPair = cng.BCryptImportKeyPair
    BCryptImportKeyPair.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptDuplicateKey(
    # _In_                                BCRYPT_KEY_HANDLE   hKey,
    # _Out_                               BCRYPT_KEY_HANDLE   *phNewKey,
    # _Out_writes_bytes_all_opt_(cbKeyObject)  PUCHAR   pbKeyObject,
    # _In_                                ULONG   cbKeyObject,
    # _In_                                ULONG   dwFlags);
    BCryptDuplicateKey = ncrypt.BCryptDuplicateKey
    BCryptDuplicateKey.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptFinalizeKeyPair(
    # _Inout_ BCRYPT_KEY_HANDLE   hKey,
    # _In_    ULONG   dwFlags);
    BCryptFinalizeKeyPair = cng.BCryptFinalizeKeyPair
    BCryptFinalizeKeyPair.restype = NTSTATUS

    # NTSTATUS
    # WINAPI
    # BCryptDestroyKey(
    # _Inout_ BCRYPT_KEY_HANDLE   hKey);
    BCryptDestroyKey = cng.BCryptDestroyKey
    BCryptDestroyKey.restype = WINAPI

    # NTSTATUS
    # WINAPI
    # BCryptDestroySecret(
    # _Inout_ BCRYPT_SECRET_HANDLE   hSecret);
    BCryptDestroySecret = ncrypt.BCryptDestroySecret
    BCryptDestroySecret.restype = WINAPI

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptSignHash(
    # _In_                                        BCRYPT_KEY_HANDLE   hKey,
    # _In_opt_                                    VOID    *pPaddingInfo,
    # _In_reads_bytes_(cbInput)                        PUCHAR   pbInput,
    # _In_                                        ULONG   cbInput,
    # _Out_writes_bytes_to_opt_(cbOutput, *pcbResult) PUCHAR   pbOutput,
    # _In_                                        ULONG   cbOutput,
    # _Out_                                       ULONG   *pcbResult,
    # _In_                                        ULONG   dwFlags);
    BCryptSignHash = cng.BCryptSignHash
    BCryptSignHash.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptVerifySignature(
    # _In_                        BCRYPT_KEY_HANDLE   hKey,
    # _In_opt_                    VOID    *pPaddingInfo,
    # _In_reads_bytes_(cbHash)         PUCHAR   pbHash,
    # _In_                        ULONG   cbHash,
    # _In_reads_bytes_(cbSignature)    PUCHAR   pbSignature,
    # _In_                        ULONG   cbSignature,
    # _In_                        ULONG   dwFlags);
    BCryptVerifySignature = cng.BCryptVerifySignature
    BCryptVerifySignature.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptSecretAgreement(
    # _In_    BCRYPT_KEY_HANDLE       hPrivKey,
    # _In_    BCRYPT_KEY_HANDLE       hPubKey,
    # _Out_   BCRYPT_SECRET_HANDLE    *phAgreedSecret,
    # _In_    ULONG                   dwFlags);
    BCryptSecretAgreement = cng.BCryptSecretAgreement
    BCryptSecretAgreement.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptDeriveKey(
    # _In_        BCRYPT_SECRET_HANDLE hSharedSecret,
    # _In_        LPCWSTR              pwszKDF,
    # _In_opt_    BCryptBufferDesc     *pParameterList,
    # _Out_writes_bytes_to_opt_(cbDerivedKey, *pcbResult) PUCHAR pbDerivedKey,
    # _In_        ULONG                cbDerivedKey,
    # _Out_       ULONG                *pcbResult,
    # _In_        ULONG                dwFlags);
    BCryptDeriveKey = cng.BCryptDeriveKey
    BCryptDeriveKey.restype = NTSTATUS

    if NTDDI_VERSION >= NTDDI_WIN8:
        pass
    # END IF

    # Primitive hashing functions.
    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptCreateHash(
    # _Inout_                             BCRYPT_ALG_HANDLE   hAlgorithm,
    # _Out_                               BCRYPT_HASH_HANDLE  *phHash,
    # _Out_writes_bytes_all_opt_(cbHashObject) PUCHAR   pbHashObject,
    # _In_                                ULONG   cbHashObject,
    # _In_reads_bytes_opt_(cbSecret)           PUCHAR   pbSecret, // optional
    # _In_                                ULONG   cbSecret, // optional
    # _In_                                ULONG   dwFlags);
    BCryptCreateHash = cng.BCryptCreateHash
    BCryptCreateHash.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptHashData(
    # _Inout_                 BCRYPT_HASH_HANDLE  hHash,
    # _In_reads_bytes_(cbInput)    PUCHAR   pbInput,
    # _In_                    ULONG   cbInput,
    # _In_                    ULONG   dwFlags);
    BCryptHashData = cng.BCryptHashData
    BCryptHashData.restype = NTSTATUS

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptFinishHash(
    # _Inout_                     BCRYPT_HASH_HANDLE hHash,
    # _Out_writes_bytes_all_(cbOutput) PUCHAR   pbOutput,
    # _In_                        ULONG   cbOutput,
    # _In_                        ULONG   dwFlags);
    BCryptFinishHash = ncrypt.BCryptFinishHash
    BCryptFinishHash.restype = NTSTATUS

    if (NTDDI_VERSION > NTDDI_WINBLUE or (NTDDI_VERSION == NTDDI_WINBLUE and defined(WINBLUE_KBSPRING14))):
        bcrypt = ctypes.windll.BCRYPT

        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptCreateMultiHash(
        # _Inout_                                     BCRYPT_ALG_HANDLE   hAlgorithm,
        # _Out_                                       BCRYPT_HASH_HANDLE *phHash,
        # _In_                                        ULONG               nHashes,
        # _Out_writes_bytes_all_opt_(cbHashObject)    PUCHAR              pbHashObject,
        # _In_                                        ULONG               cbHashObject,
        # _In_reads_bytes_opt_(cbSecret)              PUCHAR              pbSecret, // optional
        # _In_                                        ULONG               cbSecret, // optional
        # _In_                                        ULONG               dwFlags);
        BCryptCreateMultiHash = bcrypt.BCryptCreateMultiHash
        BCryptCreateMultiHash.restype = NTSTATUS

        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptProcessMultiOperations(
        # _Inout_                         BCRYPT_HANDLE                   hObject,
        # _In_                            BCRYPT_MULTI_OPERATION_TYPE     operationType,
        # _In_reads_bytes_(cbOperations)  PVOID                           pOperations,
        # _In_                            ULONG                           cbOperations,
        # _In_                            ULONG                           dwFlags );
        BCryptProcessMultiOperations = bcrypt.BCryptProcessMultiOperations
        BCryptProcessMultiOperations.restype = NTSTATUS

    # END IF

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptDuplicateHash(
    # _In_                                BCRYPT_HASH_HANDLE  hHash,
    # _Out_                               BCRYPT_HASH_HANDLE  *phNewHash,
    # _Out_writes_bytes_all_opt_(cbHashObject) PUCHAR   pbHashObject,
    # _In_                                ULONG   cbHashObject,
    # _In_                                ULONG   dwFlags);
    BCryptDuplicateHash = cng.BCryptDuplicateHash
    BCryptDuplicateHash.restype = NTSTATUS

    # NTSTATUS
    # WINAPI
    # BCryptDestroyHash(
    # _Inout_ BCRYPT_HASH_HANDLE  hHash);
    BCryptDestroyHash = ncrypt.BCryptDestroyHash
    BCryptDestroyHash.restype = WINAPI

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        bcrypt = ctypes.windll.BCRYPT

        # NTSTATUS
        # WINAPI
        # BCryptHash(
        # _Inout_                             BCRYPT_ALG_HANDLE   hAlgorithm,
        # _In_reads_bytes_opt_(cbSecret)      PUCHAR              pbSecret, // for keyed algs
        # _In_                                ULONG               cbSecret, // for keyed algs
        # _In_reads_bytes_(cbInput)           PUCHAR              pbInput,
        # _In_                                ULONG               cbInput,
        # _Out_writes_bytes_all_(cbOutput)    PUCHAR              pbOutput,
        # _In_                                ULONG               cbOutput );
        BCryptHash = bcrypt.BCryptHash
        BCryptHash.restype = WINAPI

    # END IF

    # Primitive random number generation.
    # Flags to BCryptGenRandom
    # BCRYPT_RNG_USE_ENTROPY_IN_BUFFER is ignored in Win7 & later
    BCRYPT_RNG_USE_ENTROPY_IN_BUFFER = 0x00000001
    BCRYPT_USE_SYSTEM_PREFERRED_RNG = 0x00000002

    # _Must_inspect_result_
    # NTSTATUS
    # WINAPI
    # BCryptGenRandom(
    # _In_opt_                        BCRYPT_ALG_HANDLE   hAlgorithm,
    # _Out_writes_bytes_(cbBuffer)    PUCHAR  pbBuffer,
    # _In_                            ULONG   cbBuffer,
    # _In_                            ULONG   dwFlags);
    BCryptGenRandom = ncrypt.BCryptGenRandom
    BCryptGenRandom.restype = NTSTATUS

    if NTDDI_VERSION >= NTDDI_WIN7:
        # Primitive key derivation functions.
        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptDeriveKeyCapi(
        # _In_                            BCRYPT_HASH_HANDLE  hHash,
        # _In_opt_                        BCRYPT_ALG_HANDLE   hTargetAlg,
        # _Out_writes_bytes_( cbDerivedKey )    PUCHAR              pbDerivedKey,
        # _In_                            ULONG               cbDerivedKey,
        # _In_                            ULONG               dwFlags);
        BCryptDeriveKeyCapi = ncrypt.BCryptDeriveKeyCapi
        BCryptDeriveKeyCapi.restype = NTSTATUS

    # END IF

    if NTDDI_VERSION >= NTDDI_WIN7:
        cng = ctypes.windll.CNG

        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptDeriveKeyPBKDF2(
        # _In_                            BCRYPT_ALG_HANDLE   hPrf,
        # _In_reads_bytes_opt_( cbPassword )   PUCHAR              pbPassword,
        # _In_                            ULONG               cbPassword,
        # _In_reads_bytes_opt_( cbSalt )       PUCHAR              pbSalt,
        # _In_                            ULONG               cbSalt,
        # _In_                            ULONGLONG           cIterations,
        # _Out_writes_bytes_( cbDerivedKey )    PUCHAR              pbDerivedKey,
        # _In_                            ULONG               cbDerivedKey,
        # _In_                            ULONG               dwFlags);
        BCryptDeriveKeyPBKDF2 = cng.BCryptDeriveKeyPBKDF2
        BCryptDeriveKeyPBKDF2.restype = NTSTATUS

    # END IF


    # Interface version control...
    _BCRYPT_INTERFACE_VERSION._fields_ = [
        ('MajorVersion', USHORT),
        ('MinorVersion', USHORT),
    ]

    def BCRYPT_MAKE_INTERFACE_VERSION(major, minor):
        return major, minor

    def BCRYPT_IS_INTERFACE_VERSION_COMPATIBLE(loader, provider):
        return loader.MajorVersion <= provider.MajorVersion

    # Primitive provider interfaces.
    BCRYPT_CIPHER_INTERFACE_VERSION_1 = BCRYPT_MAKE_INTERFACE_VERSION(1,0)

    BCRYPT_HASH_INTERFACE_VERSION_1 = BCRYPT_MAKE_INTERFACE_VERSION(1,0)

    if (NTDDI_VERSION > NTDDI_WINBLUE or (NTDDI_VERSION == NTDDI_WINBLUE and defined(WINBLUE_KBSPRING14))):
        BCRYPT_HASH_INTERFACE_MAJORVERSION_2 = 2
        BCRYPT_HASH_INTERFACE_VERSION_2 = BCRYPT_MAKE_INTERFACE_VERSION(
            BCRYPT_HASH_INTERFACE_MAJORVERSION_2,
            0
        )
    # END IF

    BCRYPT_ASYMMETRIC_ENCRYPTION_INTERFACE_VERSION_1 = (
        BCRYPT_MAKE_INTERFACE_VERSION(1, 0)
    )
    BCRYPT_SECRET_AGREEMENT_INTERFACE_VERSION_1 = (
        BCRYPT_MAKE_INTERFACE_VERSION(1, 0)
    )
    BCRYPT_SIGNATURE_INTERFACE_VERSION_1 = (
        BCRYPT_MAKE_INTERFACE_VERSION(1, 0)
    )
    BCRYPT_RNG_INTERFACE_VERSION_1 = BCRYPT_MAKE_INTERFACE_VERSION(1, 0)

    # ////////////////////////////////////////////////////////////////////////////
    #
    # CryptoConfig Definitions
    # //////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////
    #
    # Interface registration flags
    CRYPT_MIN_DEPENDENCIES = 0x00000001
    CRYPT_PROCESS_ISOLATE = 0x00010000    # User-mode only

    # Processor modes supported by a provider
    # (Valid for BCryptQueryProviderRegistration and BCryptResolveProviders):
    CRYPT_UM = 0x00000001    # User mode only
    CRYPT_KM = 0x00000002    # Kernel mode only
    CRYPT_MM = 0x00000003    # Multi-mode: Must support BOTH UM and KM

    # (Valid only for BCryptQueryProviderRegistration):
    CRYPT_ANY = 0x00000004    # Wildcard: Either UM, or KM, or both

    # Write behavior flags
    CRYPT_OVERWRITE = 0x00000001

    # Configuration tables
    CRYPT_LOCAL = 0x00000001
    CRYPT_DOMAIN = 0x00000002

    # Context configuration flags
    CRYPT_EXCLUSIVE = 0x00000001
    CRYPT_OVERRIDE = 0x00010000    # Enterprise table only

    # Resolution and enumeration flags
    CRYPT_ALL_FUNCTIONS = 0x00000001
    CRYPT_ALL_PROVIDERS = 0x00000002

    # Priority list positions
    CRYPT_PRIORITY_TOP = 0x00000000
    CRYPT_PRIORITY_BOTTOM = 0xFFFFFFFF

    # Default system-wide context
    CRYPT_DEFAULT_CONTEXT = "Default"

    # ////////////////////////////////////////////////////////////////////////////
    #
    # CryptoConfig Structures
    # ///////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////
    #
    # Provider Registration Structures
    _CRYPT_INTERFACE_REG._fields_ = [
        ('dwInterface', ULONG),
        ('dwFlags', ULONG),
        ('cFunctions', ULONG),
        ('rgpszFunctions', POINTER(PWSTR)),
    ]

    _CRYPT_IMAGE_REG._fields_ = [
        ('pszImage', PWSTR),
        ('cInterfaces', ULONG),
        ('rgpInterfaces', POINTER(PCRYPT_INTERFACE_REG)),
    ]

    _CRYPT_PROVIDER_REG._fields_ = [
        ('cAliases', ULONG),
        ('rgpszAliases', POINTER(PWSTR)),
        ('pUM', PCRYPT_IMAGE_REG),
        ('pKM', PCRYPT_IMAGE_REG),
    ]

    _CRYPT_PROVIDERS._fields_ = [
        ('cProviders', ULONG),
        ('rgpszProviders', POINTER(PWSTR)),
    ]

    # Context Configuration Structures
    _CRYPT_CONTEXT_CONFIG._fields_ = [
        ('dwFlags', ULONG),
        ('dwReserved', ULONG),
    ]

    _CRYPT_CONTEXT_FUNCTION_CONFIG._fields_ = [
        ('dwFlags', ULONG),
        ('dwReserved', ULONG),
    ]

    _CRYPT_CONTEXTS._fields_ = [
        ('cContexts', ULONG),
        ('rgpszContexts', POINTER(PWSTR)),
    ]

    _CRYPT_CONTEXT_FUNCTIONS._fields_ = [
        ('cFunctions', ULONG),
        ('rgpszFunctions', POINTER(PWSTR)),
    ]

    _CRYPT_CONTEXT_FUNCTION_PROVIDERS._fields_ = [
        ('cProviders', ULONG),
        ('rgpszProviders', POINTER(PWSTR)),
    ]

    # Provider Resolution Structures
    _CRYPT_PROPERTY_REF._fields_ = [
        ('pszProperty', PWSTR),
        ('cbValue', ULONG),
        ('pbValue', PUCHAR),
    ]

    _CRYPT_IMAGE_REF._fields_ = [
        ('pszImage', PWSTR),
        ('dwFlags', ULONG),
    ]

    _CRYPT_PROVIDER_REF._fields_ = [
        ('dwInterface', ULONG),
        ('pszFunction', PWSTR),
        ('pszProvider', PWSTR),
        ('cProperties', ULONG),
        ('rgpProperties', POINTER(PCRYPT_PROPERTY_REF)),
        ('pUM', PCRYPT_IMAGE_REF),
        ('pKM', PCRYPT_IMAGE_REF),
    ]

    _CRYPT_PROVIDER_REFS._fields_ = [
        ('cProviders', ULONG),
        ('rgpProviders', POINTER(PCRYPT_PROVIDER_REF)),
    ]
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
    # ////////////////////////////////////////////////////////////////////////////
    #
    # CryptoConfig Functions
    # ////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////
    #
    if not defined(KERNEL_MODE_CNG):
        ncrypt = ctypes.windll.NCRYPT


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptQueryProviderRegistration(
        # _In_ LPCWSTR pszProvider,
        # _In_ ULONG dwMode,
        # _In_ ULONG dwInterface,
        # _Inout_ ULONG* pcbBuffer,
        # _Inout_
        # _When_(_Old_(*ppBuffer) != NULL, _At_(*ppBuffer, _Out_writes_bytes_to_(*pcbBuffer, *pcbBuffer)))
        # _When_(_Old_(*ppBuffer) == NULL, _Outptr_result_bytebuffer_all_(*pcbBuffer))
        # PCRYPT_PROVIDER_REG *ppBuffer);
        BCryptQueryProviderRegistration = (
            ncrypt.BCryptQueryProviderRegistration
        )
        BCryptQueryProviderRegistration.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptEnumRegisteredProviders(
        # _Inout_ ULONG* pcbBuffer,
        # _Inout_
        # _When_(_Old_(*ppBuffer) != NULL, _At_(*ppBuffer, _Out_writes_bytes_to_(*pcbBuffer, *pcbBuffer)))
        # _When_(_Old_(*ppBuffer) == NULL, _Outptr_result_bytebuffer_all_(*pcbBuffer))
        # PCRYPT_PROVIDERS *ppBuffer);
        BCryptEnumRegisteredProviders = ncrypt.BCryptEnumRegisteredProviders
        BCryptEnumRegisteredProviders.restype = NTSTATUS


        # Context Configuration Functions
        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptCreateContext(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext,
        # _In_opt_ PCRYPT_CONTEXT_CONFIG pConfig); // Optional
        BCryptCreateContext = ncrypt.BCryptCreateContext
        BCryptCreateContext.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptDeleteContext(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext);
        BCryptDeleteContext = ncrypt.BCryptDeleteContext
        BCryptDeleteContext.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptEnumContexts(
        # _In_ ULONG dwTable,
        # _Inout_ ULONG* pcbBuffer,
        # _Inout_
        # _When_(_Old_(*ppBuffer) != NULL, _At_(*ppBuffer, _Out_writes_bytes_to_(*pcbBuffer, *pcbBuffer)))
        # _When_(_Old_(*ppBuffer) == NULL, _Outptr_result_bytebuffer_all_(*pcbBuffer))
        # PCRYPT_CONTEXTS *ppBuffer);
        BCryptEnumContexts = ncrypt.BCryptEnumContexts
        BCryptEnumContexts.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptConfigureContext(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext,
        # _In_ PCRYPT_CONTEXT_CONFIG pConfig);
        BCryptConfigureContext = ncrypt.BCryptConfigureContext
        BCryptConfigureContext.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptQueryContextConfiguration(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext,
        # _Inout_ ULONG* pcbBuffer,
        # _Inout_
        # _When_(_Old_(*ppBuffer) != NULL, _At_(*ppBuffer, _Out_writes_bytes_to_(*pcbBuffer, *pcbBuffer)))
        # _When_(_Old_(*ppBuffer) == NULL, _Outptr_result_bytebuffer_all_(*pcbBuffer))
        # PCRYPT_CONTEXT_CONFIG *ppBuffer);
        BCryptQueryContextConfiguration = (
            ncrypt.BCryptQueryContextConfiguration
        )
        BCryptQueryContextConfiguration.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptAddContextFunction(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext,
        # _In_ ULONG dwInterface,
        # _In_ LPCWSTR pszFunction,
        # _In_ ULONG dwPosition);
        BCryptAddContextFunction = ncrypt.BCryptAddContextFunction
        BCryptAddContextFunction.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptRemoveContextFunction(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext,
        # _In_ ULONG dwInterface,
        # _In_ LPCWSTR pszFunction);
        BCryptRemoveContextFunction = ncrypt.BCryptRemoveContextFunction
        BCryptRemoveContextFunction.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptEnumContextFunctions(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext,
        # _In_ ULONG dwInterface,
        # _Inout_ ULONG* pcbBuffer,
        # _Inout_
        # _When_(_Old_(*ppBuffer) != NULL, _At_(*ppBuffer, _Out_writes_bytes_to_(*pcbBuffer, *pcbBuffer)))
        # _When_(_Old_(*ppBuffer) == NULL, _Outptr_result_bytebuffer_all_(*pcbBuffer))
        # PCRYPT_CONTEXT_FUNCTIONS *ppBuffer);
        BCryptEnumContextFunctions = ncrypt.BCryptEnumContextFunctions
        BCryptEnumContextFunctions.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptConfigureContextFunction(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext,
        # _In_ ULONG dwInterface,
        # _In_ LPCWSTR pszFunction,
        # _In_ PCRYPT_CONTEXT_FUNCTION_CONFIG pConfig);
        BCryptConfigureContextFunction = ncrypt.BCryptConfigureContextFunction
        BCryptConfigureContextFunction.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptQueryContextFunctionConfiguration(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext,
        # _In_ ULONG dwInterface,
        # _In_ LPCWSTR pszFunction,
        # _Inout_ ULONG* pcbBuffer,
        # _Inout_
        # _When_(_Old_(*ppBuffer) != NULL, _At_(*ppBuffer, _Out_writes_bytes_to_(*pcbBuffer, *pcbBuffer)))
        # _When_(_Old_(*ppBuffer) == NULL, _Outptr_result_bytebuffer_all_(*pcbBuffer))
        # PCRYPT_CONTEXT_FUNCTION_CONFIG *ppBuffer);
        BCryptQueryContextFunctionConfiguration = (
            ncrypt.BCryptQueryContextFunctionConfiguration
        )
        BCryptQueryContextFunctionConfiguration.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptEnumContextFunctionProviders(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext,
        # _In_ ULONG dwInterface,
        # _In_ LPCWSTR pszFunction,
        # _Inout_ ULONG* pcbBuffer,
        # _Inout_
        # _When_(_Old_(*ppBuffer) != NULL, _At_(*ppBuffer, _Out_writes_bytes_to_(*pcbBuffer, *pcbBuffer)))
        # _When_(_Old_(*ppBuffer) == NULL, _Outptr_result_bytebuffer_all_(*pcbBuffer))
        # PCRYPT_CONTEXT_FUNCTION_PROVIDERS *ppBuffer);
        BCryptEnumContextFunctionProviders = (
            ncrypt.BCryptEnumContextFunctionProviders
        )
        BCryptEnumContextFunctionProviders.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptSetContextFunctionProperty(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext,
        # _In_ ULONG dwInterface,
        # _In_ LPCWSTR pszFunction,
        # _In_ LPCWSTR pszProperty,
        # _In_ ULONG cbValue,
        # _In_reads_bytes_opt_(cbValue) PUCHAR pbValue);
        BCryptSetContextFunctionProperty = (
            ncrypt.BCryptSetContextFunctionProperty
        )
        BCryptSetContextFunctionProperty.restype = NTSTATUS


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptQueryContextFunctionProperty(
        # _In_ ULONG dwTable,
        # _In_ LPCWSTR pszContext,
        # _In_ ULONG dwInterface,
        # _In_ LPCWSTR pszFunction,
        # _In_ LPCWSTR pszProperty,
        # _Inout_ ULONG* pcbValue,
        # _Inout_
        # _When_(_Old_(*ppbValue) != NULL, _At_(*ppbValue, _Out_writes_bytes_to_(*pcbValue, *pcbValue)))
        # _When_(_Old_(*ppbValue) == NULL, _Outptr_result_bytebuffer_all_(*pcbValue))
        # PUCHAR *ppbValue);
        BCryptQueryContextFunctionProperty = (
            ncrypt.BCryptQueryContextFunctionProperty
        )
        BCryptQueryContextFunctionProperty.restype = NTSTATUS

    # END IF  #ifndef KERNEL_MODE_CNG

    # Configuration Change Notification Functions
    if defined(KERNEL_MODE_CNG):
        cng = ctypes.windll.CNG


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptRegisterConfigChangeNotify(
        # _In_ PRKEVENT pEvent);
        BCryptRegisterConfigChangeNotify = cng.BCryptRegisterConfigChangeNotify
        BCryptRegisterConfigChangeNotify.restype = NTSTATUS


    else:
        cng = ctypes.windll.CNG


        # _Must_inspect_result_
        # NTSTATUS
        # WINAPI
        # BCryptRegisterConfigChangeNotify(
        # _Out_ HANDLE *phEvent);
        BCryptRegisterConfigChangeNotify = cng.BCryptRegisterConfigChangeNotify
        BCryptRegisterConfigChangeNotify.restype = NTSTATUS


    # END IF


    if defined(KERNEL_MODE_CNG):
        ncrypt = ctypes.windll.NCRYPT


        # NTSTATUS
        # WINAPI
        # BCryptUnregisterConfigChangeNotify(
        # _In_ PRKEVENT pEvent);
        BCryptUnregisterConfigChangeNotify = (
            ncrypt.BCryptUnregisterConfigChangeNotify
        )
        BCryptUnregisterConfigChangeNotify.restype = WINAPI


    else:
        ncrypt = ctypes.windll.NCRYPT


        # NTSTATUS
        # WINAPI
        # BCryptUnregisterConfigChangeNotify(
        # _In_ HANDLE hEvent);
        BCryptUnregisterConfigChangeNotify = (
            ncrypt.BCryptUnregisterConfigChangeNotify
        )
        BCryptUnregisterConfigChangeNotify.restype = WINAPI


    # END IF


    # Provider Resolution Functions
    ncrypt = ctypes.windll.NCRYPT


    # _Must_inspect_result_
    # NTSTATUS WINAPI
    # BCryptResolveProviders(
    # _In_opt_ LPCWSTR pszContext,
    # _In_opt_ ULONG dwInterface,
    # _In_opt_ LPCWSTR pszFunction,
    # _In_opt_ LPCWSTR pszProvider,
    # _In_ ULONG dwMode,
    # _In_ ULONG dwFlags,
    # _Inout_ ULONG* pcbBuffer,
    # _Inout_
    # _When_(_Old_(*ppBuffer) != NULL, _At_(*ppBuffer, _Out_writes_bytes_to_(*pcbBuffer, *pcbBuffer)))
    # _When_(_Old_(*ppBuffer) == NULL, _Outptr_result_bytebuffer_all_(*pcbBuffer))
    # PCRYPT_PROVIDER_REFS *ppBuffer);
    BCryptResolveProviders = ncrypt.BCryptResolveProviders
    BCryptResolveProviders.restype = NTSTATUS


# END IF  WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
    # Miscellaneous queries about the crypto environment
    cng = ctypes.windll.CNG


    # NTSTATUS
    # WINAPI
    # BCryptGetFipsAlgorithmMode(
    # _Out_ BOOLEAN *pfEnabled
    # );
    BCryptGetFipsAlgorithmMode = cng.BCryptGetFipsAlgorithmMode
    BCryptGetFipsAlgorithmMode.restype = WINAPI


# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    pass
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

if defined(__cplusplus):
    pass
# END IF


if _MSC_VER >= 1200:
    pass
# END IF


