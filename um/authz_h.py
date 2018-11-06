

# TODO: Finish up module imports
import ctypes
from pyWinAPI import *
from shared.sdkddkver_h import *
from shared.wtypes_h import *
from shared.winapifamily_h import *
from shared.wtypes_h import *


# + + Copyright (c) 2000 Microsoft Corporation Module Name: authz.h Abstract:
# This module contains the authorization framework APIs and any public data
# .structures needed to call these APIs. Revision History: Created - March
# 2000 - -
if _MSC_VER >= 1200:
    pass
# END IF
if not defined(__AUTHZ_H__):
    __AUTHZ_H__ = 1

    if defined(__cplusplus):
        pass
    # END IF
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(_AUTHZ_):
            AUTHZAPI = DECLSPEC_IMPORT
        else:
            AUTHZAPI = 1
        # END IF

        if not defined(MIDL_PASS):
            pass
        # END IF

        if _MSC_VER >= 1200:
            pass
        # END IF

        AUTHZ_SKIP_TOKEN_GROUPS = 0x2
        AUTHZ_REQUIRE_S4U_LOGON = 0x4
        AUTHZ_COMPUTE_PRIVILEGES = 0x8
        AUTHZ_ACCESS_CHECK_RESULTS_HANDLE = DECLARE_HANDLE()
        AUTHZ_CLIENT_CONTEXT_HANDLE = DECLARE_HANDLE()
        AUTHZ_RESOURCE_MANAGER_HANDLE = DECLARE_HANDLE()
        AUTHZ_AUDIT_EVENT_HANDLE = DECLARE_HANDLE()
        AUTHZ_AUDIT_EVENT_TYPE_HANDLE = DECLARE_HANDLE()
        AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE = DECLARE_HANDLE()
        AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE = DECLARE_HANDLE()

        from um.winnt_h import (
            ACCESS_MASK,
            PACCESS_MASK,
            POBJECT_TYPE_LIST
        )

        if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
            pass
        # END IF   (_WIN32_WINNT >= _WIN32_WINNT_WIN8)

        if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
            pass
        # END IF   (_WIN32_WINNT >= _WIN32_WINNT_WIN8)

        class _AUTHZ_ACCESS_REQUEST(ctypes.Structure):
            pass


        _AUTHZ_ACCESS_REQUEST._fields_ = [
            ('DesiredAccess', ACCESS_MASK),
            ('PrincipalSelfSid', PSID), # To replace the principal self sid in the acl.
            ('ObjectTypeList', POBJECT_TYPE_LIST), # property access is desired.
            ('ObjectTypeListLength', DWORD),
            ('OptionalArguments', PVOID), # not interpret these.
        ]

        AUTHZ_ACCESS_REQUEST = _AUTHZ_ACCESS_REQUEST
        PAUTHZ_ACCESS_REQUEST = POINTER(_AUTHZ_ACCESS_REQUEST)


        class _AUTHZ_ACCESS_REPLY(ctypes.Structure):
            pass


        _AUTHZ_ACCESS_REPLY._fields_ = [
            ('ResultListLength', DWORD), # Note: This parameter must be fillednot
            ('GrantedAccessMask', PACCESS_MASK), # check routines just fill in the values.
            ('SaclEvaluationResults', PDWORD), # Sacl evaluation will only be performed if auditing is requested.
            ('Error', PDWORD), # by the RM. Access check routines just fill in the values.
        ]

        AUTHZ_ACCESS_REPLY = _AUTHZ_ACCESS_REPLY
        PAUTHZ_ACCESS_REPLY = POINTER(_AUTHZ_ACCESS_REPLY)

        AUTHZ_GENERATE_SUCCESS_AUDIT = 0x1
        AUTHZ_GENERATE_FAILURE_AUDIT = 0x2

        if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
            pass
        # END IF   (_WIN32_WINNT >= _WIN32_WINNT_WIN8)

        AUTHZ_SECURITY_ATTRIBUTE_TYPE_INVALID = 0x00
        AUTHZ_SECURITY_ATTRIBUTE_TYPE_INT64 = 0x01
        AUTHZ_SECURITY_ATTRIBUTE_TYPE_UINT64 = 0x02
        AUTHZ_SECURITY_ATTRIBUTE_TYPE_STRING = 0x03


        class _AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE(ctypes.Structure):
            pass


        _AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE._fields_ = [
            ('Version', ULONG64),
            ('pName', PWSTR),
        ]

        AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE = _AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE
        PAUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE = POINTER(_AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE)

        AUTHZ_SECURITY_ATTRIBUTE_TYPE_FQBN = 0x04

        if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
            AUTHZ_SECURITY_ATTRIBUTE_TYPE_SID = 0x05
            AUTHZ_SECURITY_ATTRIBUTE_TYPE_BOOLEAN = 0x06
        # END IF   (_WIN32_WINNT >= _WIN32_WINNT_WIN8)


        class _AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE(ctypes.Structure):
            pass


        _AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE._fields_ = [
            ('pValue', PVOID), # Pointer is BYTE aligned.
            ('ValueLength', ULONG), # In bytes
        ]

        AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE = _AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE
        PAUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE = POINTER(_AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE)

        AUTHZ_SECURITY_ATTRIBUTE_TYPE_OCTET_STRING = 0x10


        class AUTHZ_SECURITY_ATTRIBUTE_OPERATION(ENUM):
            AUTHZ_SECURITY_ATTRIBUTE_OPERATION_NONE = 0
            AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL = 1
            AUTHZ_SECURITY_ATTRIBUTE_OPERATION_ADD = 2
            AUTHZ_SECURITY_ATTRIBUTE_OPERATION_DELETE = 3
            AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE = 4


        PAUTHZ_SECURITY_ATTRIBUTE_OPERATION = POINTER(AUTHZ_SECURITY_ATTRIBUTE_OPERATION)
        AUTHZ_SECURITY_ATTRIBUTE_OPERATION_NONE = AUTHZ_SECURITY_ATTRIBUTE_OPERATION.AUTHZ_SECURITY_ATTRIBUTE_OPERATION_NONE
        AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL = AUTHZ_SECURITY_ATTRIBUTE_OPERATION.AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL
        AUTHZ_SECURITY_ATTRIBUTE_OPERATION_ADD = AUTHZ_SECURITY_ATTRIBUTE_OPERATION.AUTHZ_SECURITY_ATTRIBUTE_OPERATION_ADD
        AUTHZ_SECURITY_ATTRIBUTE_OPERATION_DELETE = AUTHZ_SECURITY_ATTRIBUTE_OPERATION.AUTHZ_SECURITY_ATTRIBUTE_OPERATION_DELETE
        AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE = AUTHZ_SECURITY_ATTRIBUTE_OPERATION.AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE

        if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
            class AUTHZ_SID_OPERATION(ENUM):
                AUTHZ_SID_OPERATION_NONE = 0
                AUTHZ_SID_OPERATION_REPLACE_ALL = 1
                AUTHZ_SID_OPERATION_ADD = 2
                AUTHZ_SID_OPERATION_DELETE = 3
                AUTHZ_SID_OPERATION_REPLACE = 4


            PAUTHZ_SID_OPERATION = POINTER(AUTHZ_SID_OPERATION)
            AUTHZ_SID_OPERATION_NONE = AUTHZ_SID_OPERATION.AUTHZ_SID_OPERATION_NONE
            AUTHZ_SID_OPERATION_REPLACE_ALL = AUTHZ_SID_OPERATION.AUTHZ_SID_OPERATION_REPLACE_ALL
            AUTHZ_SID_OPERATION_ADD = AUTHZ_SID_OPERATION.AUTHZ_SID_OPERATION_ADD
            AUTHZ_SID_OPERATION_DELETE = AUTHZ_SID_OPERATION.AUTHZ_SID_OPERATION_DELETE
            AUTHZ_SID_OPERATION_REPLACE = AUTHZ_SID_OPERATION.AUTHZ_SID_OPERATION_REPLACE
        # END IF   (_WIN32_WINNT >= _WIN32_WINNT_WIN8)

        class _AUTHZ_SECURITY_ATTRIBUTE_V1(ctypes.Structure):
            pass


        class Values(ctypes.Union):
            pass


        Values._fields_ = [
            ('pInt64', PLONG64),
            ('pUint64', PULONG64),
            ('ppString', POINTER(PWSTR)),
            ('pFqbn', PAUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE),
            ('pOctetString', PAUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE),
        ]

        _AUTHZ_SECURITY_ATTRIBUTE_V1.Values = Values
        _AUTHZ_SECURITY_ATTRIBUTE_V1._fields_ = [
            ('pName', PWSTR), # Case insensitive Windows Unicode string.
            ('ValueType', USHORT), # Data type of attribute.
            ('Reserved', USHORT), # a get operation.

            # AUTHZ_SECURITY_ATTRIBUTE_TYPE_STRING and
            # AUTHZ_SECURITY_ATTRIBUTE_TYPE_FQBN.
            ('| AUTHZ_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE ) ULONG   Flags', AUTHZ_SECURITY_ATTRIBUTE_NON_INHERITABLE),
            ('ValueCount', ULONG), # Number of values.
            ('Values', _AUTHZ_SECURITY_ATTRIBUTE_V1.Values), # The actual value itself.
        ]

        AUTHZ_SECURITY_ATTRIBUTE_V1 = _AUTHZ_SECURITY_ATTRIBUTE_V1
        PAUTHZ_SECURITY_ATTRIBUTE_V1 = POINTER(_AUTHZ_SECURITY_ATTRIBUTE_V1)

        AUTHZ_SECURITY_ATTRIBUTE_NON_INHERITABLE = 0x0001
        AUTHZ_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE = 0x0002
        AUTHZ_SECURITY_ATTRIBUTE_VALID_FLAGS = (
            AUTHZ_SECURITY_ATTRIBUTE_NON_INHERITABLE  |
            AUTHZ_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE
        )


        class _AUTHZ_SECURITY_ATTRIBUTES_INFORMATION(ctypes.Structure):

            # Versioning. The interpretation of the pointers in the
            # Attribute field below is dependent on the version field.

            # Get operations return the version while the set operation
            # MUST specify the version of the data structure passed in.

            AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_VERSION_V1 = 1

            AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_VERSION = (
                AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_VERSION_V1
            )


        class Attribute(ctypes.Union):
            pass


        Attribute._fields_ = [
            ('pAttributeV1', PAUTHZ_SECURITY_ATTRIBUTE_V1),
        ]

        _AUTHZ_SECURITY_ATTRIBUTES_INFORMATION.Attribute = Attribute
        _AUTHZ_SECURITY_ATTRIBUTES_INFORMATION._fields_ = [
            ('Version', USHORT), # MUST BE first.
            ('Reserved', USHORT), # Pass 0 in set operations and ignore on get operations.
            ('AttributeCount', ULONG),
            ('Attribute', _AUTHZ_SECURITY_ATTRIBUTES_INFORMATION.Attribute),
        ]

        AUTHZ_SECURITY_ATTRIBUTES_INFORMATION = _AUTHZ_SECURITY_ATTRIBUTES_INFORMATION
        PAUTHZ_SECURITY_ATTRIBUTES_INFORMATION = POINTER \
            (_AUTHZ_SECURITY_ATTRIBUTES_INFORMATION)

        AUTHZ_ACCESS_CHECK_NO_DEEP_COPY_SD = 0x00000001

        authz = ctypes.windll.authz

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzAccessCheck(
        # _In_      DWORD                              Flags,
        # _In_      AUTHZ_CLIENT_CONTEXT_HANDLE        hAuthzClientContext,
        # _In_      PAUTHZ_ACCESS_REQUEST              pRequest,
        # _In_opt_  AUTHZ_AUDIT_EVENT_HANDLE           hAuditEvent,
        # _In_      PSECURITY_DESCRIPTOR               pSecurityDescriptor,
        # _In_reads_opt_(OptionalSecurityDescriptorCount)
        # PSECURITY_DESCRIPTOR               *OptionalSecurityDescriptorArray,
        # _In_      DWORD                              OptionalSecurityDescriptorCount,
        # _Inout_   PAUTHZ_ACCESS_REPLY                pReply,
        # _Out_opt_ PAUTHZ_ACCESS_CHECK_RESULTS_HANDLE phAccessCheckResults
        # );
        AuthzAccessCheck = authz.AuthzAccessCheck
        AuthzAccessCheck.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzCachedAccessCheck(
        # _In_     DWORD                             Flags,
        # _In_     AUTHZ_ACCESS_CHECK_RESULTS_HANDLE hAccessCheckResults,
        # _In_     PAUTHZ_ACCESS_REQUEST             pRequest,
        # _In_opt_ AUTHZ_AUDIT_EVENT_HANDLE          hAuditEvent,
        # _Inout_ PAUTHZ_ACCESS_REPLY               pReply
        # );
        AuthzCachedAccessCheck = authz.AuthzCachedAccessCheck
        AuthzCachedAccessCheck.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzOpenObjectAudit(
        # _In_     DWORD                       Flags,
        # _In_     AUTHZ_CLIENT_CONTEXT_HANDLE hAuthzClientContext,
        # _In_     PAUTHZ_ACCESS_REQUEST       pRequest,
        # _In_     AUTHZ_AUDIT_EVENT_HANDLE    hAuditEvent,
        # _In_     PSECURITY_DESCRIPTOR        pSecurityDescriptor,
        # _In_reads_opt_(OptionalSecurityDescriptorCount)
        # PSECURITY_DESCRIPTOR        *OptionalSecurityDescriptorArray OPTIONAL,
        # _In_     DWORD                       OptionalSecurityDescriptorCount,
        # _In_     PAUTHZ_ACCESS_REPLY         pReply
        # );
        AuthzOpenObjectAudit = authz.AuthzOpenObjectAudit
        AuthzOpenObjectAudit.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzFreeHandle(
        # _Inout_ AUTHZ_ACCESS_CHECK_RESULTS_HANDLE hAccessCheckResults
        # );
        AuthzFreeHandle = authz.AuthzFreeHandle
        AuthzFreeHandle.restype = BOOL

        AUTHZ_RM_FLAG_NO_AUDIT = 0x1
        AUTHZ_RM_FLAG_INITIALIZE_UNDER_IMPERSONATION = 0x2
        AUTHZ_RM_FLAG_NO_CENTRAL_ACCESS_POLICIES = 0x4
        AUTHZ_VALID_RM_INIT_FLAGS = (
            AUTHZ_RM_FLAG_NO_AUDIT  |
            AUTHZ_RM_FLAG_INITIALIZE_UNDER_IMPERSONATION  |
            AUTHZ_RM_FLAG_NO_CENTRAL_ACCESS_POLICIES
        )

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzInitializeResourceManager(
        # _In_     DWORD                            Flags,
        # _In_opt_ PFN_AUTHZ_DYNAMIC_ACCESS_CHECK   pfnDynamicAccessCheck,
        # _In_opt_ PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS pfnComputeDynamicGroups,
        # _In_opt_ PFN_AUTHZ_FREE_DYNAMIC_GROUPS    pfnFreeDynamicGroups,
        # _In_opt_ PCWSTR                           szResourceManagerName,
        # _Out_    PAUTHZ_RESOURCE_MANAGER_HANDLE   phAuthzResourceManager
        # );
        AuthzInitializeResourceManager = authz.AuthzInitializeResourceManager
        AuthzInitializeResourceManager.restype = BOOL

        if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
            AUTHZ_RPC_INIT_INFO_CLIENT_VERSION_V1 = 1


            class _AUTHZ_RPC_INIT_INFO_CLIENT(ctypes.Structure):
                pass


            _AUTHZ_RPC_INIT_INFO_CLIENT._fields_ = [
                ('version', USHORT),
                ('ObjectUuid', PWSTR),
                ('ProtSeq', PWSTR),
                ('NetworkAddr', PWSTR),
                ('Endpoint', PWSTR),
                ('Options', PWSTR),
                ('ServerSpn', PWSTR),
            ]

            AUTHZ_RPC_INIT_INFO_CLIENT = _AUTHZ_RPC_INIT_INFO_CLIENT
            PAUTHZ_RPC_INIT_INFO_CLIENT = POINTER(_AUTHZ_RPC_INIT_INFO_CLIENT)

            AUTHZ_INIT_INFO_VERSION_V1 = 1


            class _AUTHZ_INIT_INFO(ctypes.Structure):
                pass


            _AUTHZ_INIT_INFO._fields_ = [
                ('version', USHORT),
                ('szResourceManagerName', PCWSTR),
                ('pfnDynamicAccessCheck', PFN_AUTHZ_DYNAMIC_ACCESS_CHECK),
                ('pfnComputeDynamicGroups', PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS),
                ('pfnFreeDynamicGroups', PFN_AUTHZ_FREE_DYNAMIC_GROUPS),
                ('pfnGetCentralAccessPolicy', PFN_AUTHZ_GET_CENTRAL_ACCESS_POLICY),
                ('pfnFreeCentralAccessPolicy', PFN_AUTHZ_FREE_CENTRAL_ACCESS_POLICY),
            ]

            AUTHZ_INIT_INFO = _AUTHZ_INIT_INFO
            PAUTHZ_INIT_INFO = POINTER(_AUTHZ_INIT_INFO)

            # AUTHZAPI
            # BOOL
            # WINAPI
            # AuthzInitializeResourceManagerEx(
            # _In_opt_ DWORD                          Flags,
            # _In_opt_ PAUTHZ_INIT_INFO               pAuthzInitInfo,
            # _Out_    PAUTHZ_RESOURCE_MANAGER_HANDLE phAuthzResourceManager
            # );
            AuthzInitializeResourceManagerEx = authz.AuthzInitializeResourceManagerEx
            AuthzInitializeResourceManagerEx.restype = BOOL

            # AUTHZAPI
            # BOOL
            # WINAPI
            # AuthzInitializeRemoteResourceManager(
            # _In_  PAUTHZ_RPC_INIT_INFO_CLIENT    pRpcInitInfo,
            # _Out_ PAUTHZ_RESOURCE_MANAGER_HANDLE phAuthzResourceManager
            # );
            AuthzInitializeRemoteResourceManager = authz.AuthzInitializeRemoteResourceManager
            AuthzInitializeRemoteResourceManager.restype = BOOL

        # END IF   (_WIN32_WINNT >= _WIN32_WINNT_WIN8)

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzFreeResourceManager(
        # _In_ AUTHZ_RESOURCE_MANAGER_HANDLE hAuthzResourceManager
        # );
        AuthzFreeResourceManager = authz.AuthzFreeResourceManager
        AuthzFreeResourceManager.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzInitializeContextFromToken(
        # _In_      DWORD                         Flags,
        # _In_      HANDLE                        TokenHandle,
        # _In_      AUTHZ_RESOURCE_MANAGER_HANDLE hAuthzResourceManager,
        # _In_opt_  PLARGE_INTEGER                pExpirationTime,
        # _In_      LUID                          Identifier,
        # _In_opt_  PVOID                         DynamicGroupArgs,
        # _Out_     PAUTHZ_CLIENT_CONTEXT_HANDLE  phAuthzClientContext
        # );
        AuthzInitializeContextFromToken = authz.AuthzInitializeContextFromToken
        AuthzInitializeContextFromToken.restype = BOOL

        # AUTHZAPI
        # BOOL
        #  WINAPI
        # AuthzInitializeContextFromSid(
        # _In_      DWORD                         Flags,
        # _In_      PSID                          UserSid,
        # _In_      AUTHZ_RESOURCE_MANAGER_HANDLE hAuthzResourceManager,
        # _In_opt_  PLARGE_INTEGER                pExpirationTime,
        # _In_      LUID                          Identifier,
        # _In_opt_  PVOID                         DynamicGroup
        # Args,
        # _Out_     PAUTHZ_CLIENT_CONTEXT_HANDLE  phAuthzClientContext
        # );
        AuthzInitializeContextFromSid = authz.AuthzInitializeContextFromSid
        AuthzInitializeContextFromSid.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzInitializeContextFromAuthzContext(
        # _In_      DWORD                        Flags,
        # _In_      AUTHZ_CLIENT_CONTEXT_HANDLE  hAuthzClientContext,
        # _In_opt_  PLARGE_INTEGER               pExpirationTime,
        # _In_      LUID                         Identifier,
        # _In_      PVOID                        DynamicGroupArgs,
        # _Out_     PAUTHZ_CLIENT_CONTEXT_HANDLE phNewAuthzClientContext
        # );
        AuthzInitializeContextFromAuthzContext = authz.AuthzInitializeContextFromAuthzContext
        AuthzInitializeContextFromAuthzContext.restype = BOOL

        if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
            # AUTHZAPI
            # BOOL
            # WINAPI
            # AuthzInitializeCompoundContext(
            # _In_ AUTHZ_CLIENT_CONTEXT_HANDLE UserContext,
            # _In_ AUTHZ_CLIENT_CONTEXT_HANDLE DeviceContext,
            # _Out_ PAUTHZ_CLIENT_CONTEXT_HANDLE phCompoundContext
            # );
            AuthzInitializeCompoundContext = authz.AuthzInitializeCompoundContext
            AuthzInitializeCompoundContext.restype = BOOL

        # END IF   (_WIN32_WINNT >= _WIN32_WINNT_WIN8)
        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzAddSidsToContext(
        # _In_      AUTHZ_CLIENT_CONTEXT_HANDLE  hAuthzClientContext,
        # _In_opt_  PSID_AND_ATTRIBUTES          Sids,
        # _In_      DWORD                        SidCount,
        # _In_opt_  PSID_AND_ATTRIBUTES          RestrictedSids,
        # _In_      DWORD                        RestrictedSidCount,
        # _Out_     PAUTHZ_CLIENT_CONTEXT_HANDLE phNewAuthzClientContext
        # );
        AuthzAddSidsToContext = authz.AuthzAddSidsToContext
        AuthzAddSidsToContext.restype = BOOL

        # API to modify security attributes in AUTHZ client context.
        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzModifySecurityAttributes(
        # _In_     AUTHZ_CLIENT_CONTEXT_HANDLE             hAuthzClientContext,
        # _In_
        # _When_(pAttributes != NULL and *pOperations != AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL, _In_reads_(pAttributes - >AttributeCount))
        # PAUTHZ_SECURITY_ATTRIBUTE_OPERATION     pOperations,
        # _In_opt_ PAUTHZ_SECURITY_ATTRIBUTES_INFORMATION  pAttributes
        # );
        AuthzModifySecurityAttributes = authz.AuthzModifySecurityAttributes
        AuthzModifySecurityAttributes.restype = BOOL

        class _AUTHZ_CONTEXT_INFORMATION_CLASS(ENUM):
            AuthzContextInfoUserSid = 1
            AuthzContextInfoGroupsSids = 2
            AuthzContextInfoRestrictedSids = 3
            AuthzContextInfoPrivileges = 4
            AuthzContextInfoExpirationTime = 5
            AuthzContextInfoServerContext = 6
            AuthzContextInfoIdentifier = 7
            AuthzContextInfoSource = 8
            AuthzContextInfoAll = 9
            AuthzContextInfoAuthenticationId = 10
            AuthzContextInfoSecurityAttributes = 11
            AuthzContextInfoDeviceSids = 12
            AuthzContextInfoUserClaims = 13
            AuthzContextInfoDeviceClaims = 14
            AuthzContextInfoAppContainerSid = 15
            AuthzContextInfoCapabilitySids = 16


        AUTHZ_CONTEXT_INFORMATION_CLASS = _AUTHZ_CONTEXT_INFORMATION_CLASS

        if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
            # AUTHZAPI
            # BOOL
            # WINAPI
            # AuthzModifyClaims(
            # _In_     AUTHZ_CLIENT_CONTEXT_HANDLE            hAuthzClientContext,
            # _In_     AUTHZ_CONTEXT_INFORMATION_CLASS        ClaimClass,
            # _In_
            # _When_(pClaims != NULL && *pClaimOperations != AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL, _In_reads_(pClaims->AttributeCount))
            # PAUTHZ_SECURITY_ATTRIBUTE_OPERATION    pClaimOperations,
            # _In_opt_ PAUTHZ_SECURITY_ATTRIBUTES_INFORMATION pClaims
            # );
            AuthzModifyClaims = authz.AuthzModifyClaims
            AuthzModifyClaims.restype = BOOL

            # AUTHZAPI
            # BOOL
            # WINAPI
            # AuthzModifySids(
            # _In_     AUTHZ_CLIENT_CONTEXT_HANDLE            hAuthzClientContext,
            # _In_     AUTHZ_CONTEXT_INFORMATION_CLASS        SidClass,
            # _In_
            # _When_(pSids != NULL && *pSidOperations != AUTHZ_SID_OPERATION_REPLACE_ALL, _In_reads_(pSids->GroupCount))
            # PAUTHZ_SID_OPERATION                   pSidOperations,
            # _In_opt_ PTOKEN_GROUPS                          pSids
            # );
            AuthzModifySids = authz.AuthzModifySids
            AuthzModifySids.restype = BOOL

            # AUTHZAPI
            # BOOL
            # WINAPI
            # AuthzSetAppContainerInformation(
            # _In_     AUTHZ_CLIENT_CONTEXT_HANDLE            hAuthzClientContext,
            # _In_     PSID                                   pAppContainerSid,
            # _In_     DWORD                                  CapabilityCount,
            # _In_reads_opt_(CapabilityCount)
            # PSID_AND_ATTRIBUTES                    pCapabilitySids
            # );
            AuthzSetAppContainerInformation = authz.AuthzSetAppContainerInformation
            AuthzSetAppContainerInformation.restype = BOOL
        # END IF   (_WIN32_WINNT >= _WIN32_WINNT_WIN8)

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzGetInformationFromContext(
        # _In_  AUTHZ_CLIENT_CONTEXT_HANDLE     hAuthzClientContext,
        # _In_  AUTHZ_CONTEXT_INFORMATION_CLASS InfoClass,
        # _In_  DWORD                           BufferSize,
        # _Out_ PDWORD                          pSizeRequired,
        # _Out_ PVOID                           Buffer
        # );
        AuthzGetInformationFromContext = authz.AuthzGetInformationFromContext
        AuthzGetInformationFromContext.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzFreeContext(
        # _In_ AUTHZ_CLIENT_CONTEXT_HANDLE hAuthzClientContext
        # );
        AuthzFreeContext = authz.AuthzFreeContext
        AuthzFreeContext.restype = BOOL

        AUTHZ_NO_SUCCESS_AUDIT = 0x00000001
        AUTHZ_NO_FAILURE_AUDIT = 0x00000002
        AUTHZ_NO_ALLOC_STRINGS = 0x00000004
        AUTHZ_WPD_CATEGORY_FLAG = 0x00000010
        AUTHZ_VALID_OBJECT_ACCESS_AUDIT_FLAGS = (
            AUTHZ_NO_SUCCESS_AUDIT |
            AUTHZ_NO_FAILURE_AUDIT |
            AUTHZ_NO_ALLOC_STRINGS |
            AUTHZ_WPD_CATEGORY_FLAG
        )

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzInitializeObjectAccessAuditEvent(
        # _In_    DWORD                         Flags,
        # _In_    AUTHZ_AUDIT_EVENT_TYPE_HANDLE hAuditEventType,
        # _In_    PWSTR                         szOperationType,
        # _In_    PWSTR                         szObjectType,
        # _In_    PWSTR                         szObjectName,
        # _In_    PWSTR                         szAdditionalInfo,
        # _Out_   PAUTHZ_AUDIT_EVENT_HANDLE     phAuditEvent,
        # _In_    DWORD                         dwAdditionalParameterCount,
        # ...
        # );
        AuthzInitializeObjectAccessAuditEvent = authz.AuthzInitializeObjectAccessAuditEvent
        AuthzInitializeObjectAccessAuditEvent.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzInitializeObjectAccessAuditEvent2(
        # _In_    DWORD                         Flags,
        # _In_    AUTHZ_AUDIT_EVENT_TYPE_HANDLE hAuditEventType,
        # _In_    PWSTR                         szOperationType,
        # _In_    PWSTR                         szObjectType,
        # _In_    PWSTR                         szObjectName,
        # _In_    PWSTR                         szAdditionalInfo,
        # _In_    PWSTR                         szAdditionalInfo2,
        # _Out_   PAUTHZ_AUDIT_EVENT_HANDLE     phAuditEvent,
        # _In_    DWORD                         dwAdditionalParameterCount,
        # ...
        # );
        AuthzInitializeObjectAccessAuditEvent2 = authz.AuthzInitializeObjectAccessAuditEvent2
        AuthzInitializeObjectAccessAuditEvent2.restype = BOOL


        class _AUTHZ_AUDIT_EVENT_INFORMATION_CLASS(ENUM):
            AuthzAuditEventInfoFlags = 1
            AuthzAuditEventInfoOperationType = 2
            AuthzAuditEventInfoObjectType = 3
            AuthzAuditEventInfoObjectName = 4
            AuthzAuditEventInfoAdditionalInfo = 5


        AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = _AUTHZ_AUDIT_EVENT_INFORMATION_CLASS

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzFreeAuditEvent(
        # _In_ AUTHZ_AUDIT_EVENT_HANDLE hAuditEvent
        # );
        AuthzFreeAuditEvent = authz.AuthzFreeAuditEvent
        AuthzFreeAuditEvent.restype = BOOL

        # Support for SACL evaluation
        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzEvaluateSacl(
        # _In_  AUTHZ_CLIENT_CONTEXT_HANDLE AuthzClientContext,
        # _In_  PAUTHZ_ACCESS_REQUEST       pRequest,
        # _In_  PACL                        Sacl,
        # _In_  ACCESS_MASK                 GrantedAccess,
        # _In_  BOOL                        AccessGranted,
        # _Out_ PBOOL                       pbGenerateAudit
        # );
        AuthzEvaluateSacl = authz.AuthzEvaluateSacl
        AuthzEvaluateSacl.restype = BOOL


        class _AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET(ctypes.Structure):
            pass


        _AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET._fields_ = [
            ('szObjectTypeName', PWSTR),
            ('dwOffset', DWORD),
        ]

        AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET = _AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET
        PAUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET = POINTER \
            (_AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET)

        if _MSC_VER >= 1200:
            pass
        # END IF

        class _AUTHZ_SOURCE_SCHEMA_REGISTRATION(ctypes.Structure):
            pass


        class DUMMYUNIONNAME(ctypes.Union):
            pass


        DUMMYUNIONNAME._fields_ = [
            ('pReserved', PVOID),

            # Must be supplied when dwFlags contains
            # AUTHZ_MIGRATED_LEGACY_PUBLISHER
            ('pProviderGuid', POINTER(GUID)),
        ]

        _AUTHZ_SOURCE_SCHEMA_REGISTRATION.DUMMYUNIONNAME = DUMMYUNIONNAME
        _AUTHZ_SOURCE_SCHEMA_REGISTRATION._fields_ = [
            ('dwFlags', DWORD),
            ('szEventSourceName', PWSTR),
            ('szEventMessageFile', PWSTR),
            ('szEventSourceXmlSchemaFile', PWSTR),
            ('szEventAccessStringsFile', PWSTR),
            ('szExecutableImagePath', PWSTR),
            ('DUMMYUNIONNAME', _AUTHZ_SOURCE_SCHEMA_REGISTRATION.DUMMYUNIONNAME), # new types are pointers.
            ('dwObjectTypeNameCount', DWORD),
            ('ObjectTypeNames', AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET * ANYSIZE_ARRAY),
        ]

        AUTHZ_SOURCE_SCHEMA_REGISTRATION = _AUTHZ_SOURCE_SCHEMA_REGISTRATION
        PAUTHZ_SOURCE_SCHEMA_REGISTRATION = POINTER \
            (_AUTHZ_SOURCE_SCHEMA_REGISTRATION)

        if _MSC_VER >= 1200:
            pass
        # END IF

        AUTHZ_FLAG_ALLOW_MULTIPLE_SOURCE_INSTANCES = 0x1

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzInstallSecurityEventSource(
        # _In_ DWORD                             dwFlags,
        # _In_ PAUTHZ_SOURCE_SCHEMA_REGISTRATION pRegistration
        # );
        AuthzInstallSecurityEventSource = authz.AuthzInstallSecurityEventSource
        AuthzInstallSecurityEventSource.restype = WINAPI

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzUninstallSecurityEventSource(
        # _In_ DWORD  dwFlags,
        # _In_ PCWSTR szEventSourceName
        # );
        AuthzUninstallSecurityEventSource = authz.AuthzUninstallSecurityEventSource
        AuthzUninstallSecurityEventSource.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzEnumerateSecurityEventSources(
        # _In_     DWORD                             dwFlags,
        # _Out_    PAUTHZ_SOURCE_SCHEMA_REGISTRATION Buffer,
        # _Out_    PDWORD                            pdwCount,
        # _Inout_ PDWORD                            pdwLength
        # );
        AuthzEnumerateSecurityEventSources = authz.AuthzEnumerateSecurityEventSources
        AuthzEnumerateSecurityEventSources.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzRegisterSecurityEventSource(
        # _In_  DWORD                                 dwFlags,
        # _In_  PCWSTR                                szEventSourceName,
        # _Out_ PAUTHZ_SECURITY_EVENT_PROVIDER_HANDLE phEventProvider
        # );
        AuthzRegisterSecurityEventSource = authz.AuthzRegisterSecurityEventSource
        AuthzRegisterSecurityEventSource.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzUnregisterSecurityEventSource(
        # _In_     DWORD                                 dwFlags,
        # _Inout_ PAUTHZ_SECURITY_EVENT_PROVIDER_HANDLE phEventProvider
        # );
        AuthzUnregisterSecurityEventSource = authz.AuthzUnregisterSecurityEventSource
        AuthzUnregisterSecurityEventSource.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzReportSecurityEvent(
        # _In_     DWORD                                dwFlags,
        # _Inout_ AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE hEventProvider,
        # _In_     DWORD                                dwAuditId,
        # _In_opt_ PSID                                 pUserSid,
        # _In_     DWORD                                dwCount,
        # ...
        # );
        AuthzReportSecurityEvent = authz.AuthzReportSecurityEvent
        AuthzReportSecurityEvent.restype = BOOL

        # AUTHZAPI
        # BOOL
        # WINAPI
        # AuthzReportSecurityEventFromParams(
        # _In_     DWORD                                dwFlags,
        # _Inout_ AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE hEventProvider,
        # _In_     DWORD                                dwAuditId,
        # _In_opt_ PSID                                 pUserSid,
        # _In_     PAUDIT_PARAMS                        pParams
        # );
        AuthzReportSecurityEventFromParams = authz.AuthzReportSecurityEventFromParams
        AuthzReportSecurityEventFromParams.restype = BOOL

        if _WIN32_WINNT >= _WIN32_WINNT_WIN8:
            # AUTHZAPI
            # BOOL
            # WINAPI
            # AuthzRegisterCapChangeNotification(
            # _Out_ PAUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE phCapChangeSubscription,
            # _In_ LPTHREAD_START_ROUTINE pfnCapChangeCallback,
            # _In_opt_ PVOID pCallbackContext
            # );
            AuthzRegisterCapChangeNotification = authz.AuthzRegisterCapChangeNotification
            AuthzRegisterCapChangeNotification.restype = BOOL

            # AUTHZAPI
            # BOOL
            # WINAPI
            # AuthzUnregisterCapChangeNotification(
            # _In_ AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE hCapChangeSubscription
            # );
            AuthzUnregisterCapChangeNotification = authz.AuthzUnregisterCapChangeNotification
            AuthzUnregisterCapChangeNotification.restype = BOOL

            # AUTHZAPI
            # BOOL
            # WINAPI
            # AuthzFreeCentralAccessPolicyCache(
            # void
            # );
            AuthzFreeCentralAccessPolicyCache = authz.AuthzFreeCentralAccessPolicyCache
            AuthzFreeCentralAccessPolicyCache.restype = BOOL
        # END IF   (_WIN32_WINNT >= _WIN32_WINNT_WIN8)

        if _MSC_VER >= 1200:
            pass
        # END IF

        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

# END IF  __AUTHZ_H__

if _MSC_VER >= 1200:
    pass
# END IF
