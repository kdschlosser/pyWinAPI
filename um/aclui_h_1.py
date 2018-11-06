

from shared.wtypes_h import (
    ENUM,
    ANYSIZE_ARRAY,
    PSID,
    PWSTR,
    POINTER,
    GUID,
    LPCWSTR,
    DWORD,
    PVOID,
    BOOLEAN,
    ULONG,
    HINSTANCE,
    LPWSTR,
    WINAPI,
    HRESULT,
    BOOL,
    UCHAR,
    HWND,
    UINT,
    PULONG,
    PCWSTR,
    WORD,
    TEXT
)
from um.commctrl_h import WM_USER
from shared.guiddef_h import (
    EXTERN_GUID,
)
import ctypes
import shared.ntdef_h
from shared.winapifamily_h import * # NOQA
from objbase_h import * # NOQA
from um.commctrl_h import * # NOQA
from um.accctrl_h import * # NOQA
from um.authz_h import * # NOQA
from um.objidl_h import (
    LPDATAOBJECT,
)
import comtypes

COMMETHOD = comtypes.COMMETHOD

from wtypesbase_h import (
    PACL,
)

from um.dssec_h import (
    SECURITY_INFORMATION,
    PSECURITY_DESCRIPTOR,
)

ACCESS_MASK = DWORD
PACCESS_MASK = POINTER(ACCESS_MASK)

ACLUIAPI = WINAPI


class _SID_AND_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ('Sid', PSID),
        ('Attributes',DWORD)
    ]


SID_AND_ATTRIBUTES = _SID_AND_ATTRIBUTES
PSID_AND_ATTRIBUTES = POINTER(_SID_AND_ATTRIBUTES)



class _TOKEN_GROUPS(ctypes.Structure):
    _fields_ = [
        ('GroupCount;', DWORD),
        ('Groups', SID_AND_ATTRIBUTES * ANYSIZE_ARRAY)
    ]


TOKEN_GROUPS = _TOKEN_GROUPS
PTOKEN_GROUPS = POINTER(_TOKEN_GROUPS)


class _SI_OBJECT_INFO(ctypes.Structure):
    _fields_ = [
        ('dwFlags', DWORD),
        ('hInstance', HINSTANCE),
        ('pszServerName', LPWSTR),
        ('pszObjectName', LPWSTR),
        ('pszPageTitle', LPWSTR),
        ('guidObjectType', GUID),
    ]


SI_OBJECT_INFO = _SI_OBJECT_INFO
PSI_OBJECT_INFO = POINTER(_SI_OBJECT_INFO)


SI_EDIT_PERMS = 0x00000000
SI_EDIT_OWNER = 0x00000001
SI_EDIT_AUDITS = 0x00000002
SI_CONTAINER = 0x00000004
SI_READONLY = 0x00000008
SI_ADVANCED = 0x00000010
SI_RESET = 0x00000020
SI_OWNER_READONLY = 0x00000040
SI_EDIT_PROPERTIES = 0x00000080
SI_OWNER_RECURSE = 0x00000100
SI_NO_ACL_PROTECT = 0x00000200
SI_NO_TREE_APPLY = 0x00000400
SI_PAGE_TITLE = 0x00000800
SI_SERVER_IS_DC = 0x00001000
SI_RESET_DACL_TREE = 0x00004000
SI_RESET_SACL_TREE = 0x00008000
SI_OBJECT_GUID = 0x00010000
SI_EDIT_EFFECTIVE = 0x00020000
SI_RESET_DACL = 0x00040000
SI_RESET_SACL = 0x00080000
SI_RESET_OWNER = 0x00100000
SI_NO_ADDITIONAL_PERMISSION = 0x00200000
SI_VIEW_ONLY = 0x00400000
SI_PERMS_ELEVATION_REQUIRED = 0x01000000
SI_AUDITS_ELEVATION_REQUIRED = 0x02000000
SI_OWNER_ELEVATION_REQUIRED = 0x04000000
SI_SCOPE_ELEVATION_REQUIRED = 0x08000000
SI_MAY_WRITE = 0x10000000
SI_ENABLE_EDIT_ATTRIBUTE_CONDITION = 0x20000000
SI_ENABLE_CENTRAL_POLICY = 0x40000000
SI_DISABLE_DENY_ACE = 0x80000000
SI_EDIT_ALL = SI_EDIT_PERMS | SI_EDIT_OWNER | SI_EDIT_AUDITS


class _SI_ACCESS(ctypes.Structure):
    _fields_ = [
        ('pguid', POINTER(GUID)),
        ('mask', ACCESS_MASK),
        ('pszName', LPCWSTR),
        ('dwFlags', DWORD),
    ]


SI_ACCESS = _SI_ACCESS
PSI_ACCESS = POINTER(_SI_ACCESS)


SI_ACCESS_SPECIFIC = 0x00010000
SI_ACCESS_GENERAL = 0x00020000
SI_ACCESS_CONTAINER = 0x00040000
SI_ACCESS_PROPERTY = 0x00080000


class _SI_INHERIT_TYPE(ctypes.Structure):
    _fields_ = [
        ('pguid', POINTER(GUID)),
        ('dwFlags', ULONG),
        ('pszName', LPCWSTR),
    ]


SI_INHERIT_TYPE = _SI_INHERIT_TYPE
PSI_INHERIT_TYPE = POINTER(_SI_INHERIT_TYPE)


class _SI_PAGE_TYPE(ENUM):
    SI_PAGE_PERM = 0
    SI_PAGE_ADVPERM = 1
    SI_PAGE_AUDIT = 2
    SI_PAGE_OWNER = 3
    SI_PAGE_EFFECTIVE = 4
    SI_PAGE_TAKEOWNERSHIP = 5
    SI_PAGE_SHARE = 7


SI_PAGE_TYPE = _SI_PAGE_TYPE


class _SI_PAGE_ACTIVATED(ENUM):
    SI_SHOW_DEFAULT = 0
    SI_SHOW_PERM_ACTIVATED = 1
    SI_SHOW_AUDIT_ACTIVATED = 2
    SI_SHOW_OWNER_ACTIVATED = 3
    SI_SHOW_EFFECTIVE_ACTIVATED = 4
    SI_SHOW_SHARE_ACTIVATED = 5
    SI_SHOW_CENTRAL_POLICY_ACTIVATED = 6


SI_PAGE_ACTIVATED = _SI_PAGE_ACTIVATED


def GET_PAGE_TYPE(X):
    return X & 0x0000ffff


def GET_ACTIVATION_TYPE(Y):
    return (Y >> 16) & 0x0000ffff


def COMBINE_PAGE_ACTIVATION(X, Y):
    return (Y << 16) | X


DOBJ_RES_CONT = 0x00000001
DOBJ_RES_ROOT = 0x00000002
DOBJ_VOL_NTACLS = 0x00000004
DOBJ_COND_NTACLS = 0x00000008
DOBJ_RIBBON_LAUNCH = 0x00000010
PSPCB_SI_INITDIALOG = WM_USER + 1
CFSTR_ACLUI_SID_INFO_LIST = TEXT("CFSTR_ACLUI_SID_INFO_LIST\n")


class _OBJECT_TYPE_LIST(ctypes.Structure):
    _fields_ = (
        ('Level', WORD),
        ('Sbz', WORD),
        ('ObjectType', POINTER(GUID))
    )

OBJECT_TYPE_LIST = _OBJECT_TYPE_LIST
POBJECT_TYPE_LIST = POINTER(_OBJECT_TYPE_LIST)



class _SID_INFO(ctypes.Structure):
    _fields_ = [
        ('pSid', PSID),
        ('pwzCommonName', PWSTR),
        ('pwzClass', PWSTR),
        ('pwzUPN', PWSTR),
    ]


SID_INFO = _SID_INFO
PSID_INFO = POINTER(_SID_INFO)


class _SID_INFO_LIST(ctypes.Structure):
    _fields_ = [
        ('cItems', ULONG),
        ('aSidInfo', SID_INFO * ANYSIZE_ARRAY),
    ]


SID_INFO_LIST = _SID_INFO_LIST
PSID_INFO_LIST = POINTER(_SID_INFO_LIST)


class _SECURITY_OBJECT(ctypes.Structure):
    _fields_ = [
        ('pwszName', PWSTR),
        ('pData', PVOID),
        ('cbData', DWORD),
        ('pData2', PVOID),
        ('cbData2', DWORD),
        ('Id', DWORD),
        ('fWellKnown', BOOLEAN),
    ]


SECURITY_OBJECT = _SECURITY_OBJECT
PSECURITY_OBJECT = POINTER(_SECURITY_OBJECT)


SECURITY_OBJECT_ID_OBJECT_SD = 0x00000001
SECURITY_OBJECT_ID_SHARE = 0x00000002
SECURITY_OBJECT_ID_CENTRAL_POLICY = 0x00000003
SECURITY_OBJECT_ID_CENTRAL_ACCESS_RULE = 0x00000004


class _EFFPERM_RESULT_LIST(ctypes.Structure):
    _fields_ = [
        ('fEvaluated', BOOLEAN),
        ('cObjectTypeListLength', ULONG),
        ('pObjectTypeList', POINTER(OBJECT_TYPE_LIST)),
        ('pGrantedAccessList', POINTER(ACCESS_MASK)),
    ]


EFFPERM_RESULT_LIST = _EFFPERM_RESULT_LIST
PEFFPERM_RESULT_LIST = POINTER(_EFFPERM_RESULT_LIST)


IID_ISecurityInformation = EXTERN_GUID(
    0x965FC360,
    0x16FF,
    0x11D0,
    0x91,
    0xCB,
    0x0,
    0xAA,
    0x0,
    0xBB,
    0xB7,
    0x23
)
IID_ISecurityInformation2 = EXTERN_GUID(
    0xC3CCFDB4,
    0x6F88,
    0x11D2,
    0xA3,
    0xCE,
    0x0,
    0xC0,
    0x4F,
    0xB1,
    0x78,
    0x2A
)
IID_IEffectivePermission = EXTERN_GUID(
    0x3853DC76,
    0x9F35,
    0x407C,
    0x88,
    0xA1,
    0xD1,
    0x93,
    0x44,
    0x36,
    0x5F,
    0xBC
)
IID_ISecurityObjectTypeInfo = EXTERN_GUID(
    0xFC3066EB,
    0x79EF,
    0x444B,
    0x91,
    0x11,
    0xD1,
    0x8A,
    0x75,
    0xEB,
    0xF2,
    0xFA
)
IID_ISecurityInformation3 = EXTERN_GUID(
    0xE2CDC9CC,
    0x31BD,
    0x4F8F,
    0x8C,
    0x8B,
    0xB6,
    0x41,
    0xAF,
    0x51,
    0x6A,
    0x1A
)
IID_ISecurityInformation4 = EXTERN_GUID(
    0xEA961070,
    0xCD14,
    0x4621,
    0xAC,
    0xE4,
    0xF6,
    0x3C,
    0x3,
    0xE5,
    0x83,
    0xE4
)
IID_IEffectivePermission2 = EXTERN_GUID(
    0x941FABCA,
    0xDD47,
    0x4FCA,
    0x90,
    0xBB,
    0xB0,
    0xE1,
    0x2,
    0x55,
    0xF2,
    0xD
)


class ISecurityInformation(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISecurityInformation
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetObjectInformation',
            (['out'], PSI_OBJECT_INFO, 'pObjectInfo'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetSecurity',
            (['in'], SECURITY_INFORMATION, 'RequestedInformation'),
            (['out'], POINTER(PSECURITY_DESCRIPTOR), 'ppSecurityDescriptor'),
            (['out'], BOOL, 'fDefault'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetSecurity',
            (['in'], SECURITY_INFORMATION,'SecurityInformation'),
            (['in'], PSECURITY_DESCRIPTOR, 'pSecurityDescriptor'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetAccessRights',
            (['in'], POINTER(GUID), 'pguidObjectType'),
            (['in'], DWORD, 'dwFlags'),
            (['out'], POINTER(PSI_ACCESS), 'ppAccess'),
            (['out'], POINTER(ULONG), 'pguidObjectType'),
            (['out'], POINTER(ULONG), 'piDefaultAccess'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'MapGeneric',
            (['in'], POINTER(GUID), 'pguidObjectType'),
            (['in'], POINTER(UCHAR), 'pAceFlags'),
            (['in'], POINTER(ACCESS_MASK), 'pMask'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetInheritTypes',
            (['in'], POINTER(PSI_INHERIT_TYPE), 'ppInheritTypes'),
            (['in'], POINTER(ULONG), 'pcInheritTypes'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'PropertySheetPageCallback',
            (['in'], HWND, 'hwnd'),
            (['in'], UINT, 'uMsg'),
            (['in'], SI_PAGE_TYPE, 'uPage'),
        ),

    ]


LPSECURITYINFO = POINTER(ISecurityInformation)


class ISecurityInformation2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISecurityInformation2
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            BOOL,
            'IsDaclCanonical',
            (['in'], PACL, 'pDacl'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'LookupSids',
            (['in'], ULONG, 'cSids'),
            (['in'], POINTER(PSID), 'rgpSids'),
            (['out'], POINTER(LPDATAOBJECT), 'ppdo'),
        ),


    ]


LPSECURITYINFO2 = POINTER(ISecurityInformation2)


class IEffectivePermission(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEffectivePermission
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetEffectivePermission',
            (['in'], POINTER(GUID), 'pguidObjectType'),
            (['in'], PSID, 'pUserSid'),
            (['in'], LPCWSTR, 'pszServerName'),
            (['in'], PSECURITY_DESCRIPTOR, 'pSD'),
            (['out'], POINTER(POBJECT_TYPE_LIST), 'ppObjectTypeList'),
            (['out'], POINTER(ULONG), 'pcObjectTypeListLength'),
            (['out'], POINTER(PACCESS_MASK), 'ppGrantedAccessList'),
            (['out'], POINTER(ULONG), 'pcGrantedAccessListLength'),
        ),

    ]


LPEFFECTIVEPERMISSION = POINTER(IEffectivePermission)


class ISecurityObjectTypeInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISecurityObjectTypeInfo
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetInheritSource',
            (['in'], SECURITY_INFORMATION, 'si'),
            (['in'], PACL, 'pACL'),
            (['out'], POINTER(PINHERITED_FROM), 'ppInheritArray'),

        ),

    ]


LPSecurityObjectTypeInfo = POINTER(ISecurityObjectTypeInfo)


class ISecurityInformation3(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISecurityInformation3
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetFullResourceName',
            (['out'], LPWSTR, 'ppszResourceName'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'OpenElevatedEditor',
            (['in'], HWND, 'hWnd'),
            (['in'], SI_PAGE_TYPE, 'uPage'),

        ),
    ]


LPSECURITYINFO3 = POINTER(ISecurityInformation3)


class ISecurityInformation3(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISecurityInformation3
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetSecondarySecurity',
            (['out'], POINTER(PSECURITY_OBJECT), 'pSecurityObjects'),
            (['out'], PULONG, 'pSecurityObjectCount'),

        ),
    ]

class IEffectivePermission2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEffectivePermission2
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetEffectiveScopePermission',
        ),
        COMMETHOD(
            [],
            HRESULT,
            'ComputeEffectivePermissionWithSecondarySecurity',
            (['in'], PSID, 'pSid'),
            (['in'], PSID, 'pDeviceSid'),
            (['in'], PCWSTR, 'pszServerName'),
            (['in'], PSECURITY_OBJECT, 'pSecurityObjects'),
            (['in'], DWORD, 'dwSecurityObjectCount'),
            (['in'], PTOKEN_GROUPS, 'pUserGroups'),
            (['in'], PAUTHZ_SID_OPERATION, 'pAuthzUserGroupsOperations'),
            (['in'], PTOKEN_GROUPS, 'pDeviceGroups'),
            (['in'], PAUTHZ_SID_OPERATION, 'pAuthzDeviceGroupsOperations'),
            (['in'], PAUTHZ_SECURITY_ATTRIBUTES_INFORMATION, 'pAuthzUserClaims'),
            (['in'], PAUTHZ_SECURITY_ATTRIBUTE_OPERATION, 'pAuthzUserClaimsOperations'),
            (['in'], PAUTHZ_SECURITY_ATTRIBUTES_INFORMATION, 'pAuthzDeviceClaims'),
            (['in'], PAUTHZ_SECURITY_ATTRIBUTE_OPERATION, 'pAuthzDeviceClaimsOperations'),
            (['in'], PEFFPERM_RESULT_LIST, 'pEffpermResultLists'),
        ),

    ]

LPSECURITYINFO4 = POINTER(ISecurityInformation4)

LPEFFECTIVEPERMISSION2 = POINTER(IEffectivePermission2)


__all__ = (
    'SI_EDIT_AUDITS', 'SI_RESET', 'SI_DISABLE_DENY_ACE', 'SI_CONTAINER',
    'SI_SCOPE_ELEVATION_REQUIRED', 'SI_PERMS_ELEVATION_REQUIRED', 'ACLUIAPI',
    'SI_RESET_OWNER', 'SI_NO_ACL_PROTECT', 'SI_RESET_SACL_TREE',
    'COMBINE_PAGE_ACTIVATION', 'SI_ACCESS_PROPERTY', 'SI_EDIT_PROPERTIES',
    'SI_MAY_WRITE', 'SI_ADVANCED', 'GET_ACTIVATION_TYPE', 'SI_READONLY',
    'CFSTR_ACLUI_SID_INFO_LIST', 'SI_OBJECT_GUID', 'SI_SERVER_IS_DC',
    'SI_ENABLE_CENTRAL_POLICY', 'DOBJ_RIBBON_LAUNCH', 'SI_PAGE_TITLE',
    'SECURITY_OBJECT_ID_CENTRAL_POLICY', 'SI_AUDITS_ELEVATION_REQUIRED',
    'SI_RESET_DACL', 'SI_OWNER_READONLY', 'SI_OWNER_RECURSE', 'GET_PAGE_TYPE',
    'SI_ACCESS_SPECIFIC', 'PSPCB_SI_INITDIALOG', 'SI_NO_TREE_APPLY',
    'SI_ENABLE_EDIT_ATTRIBUTE_CONDITION', 'SI_RESET_DACL_TREE', 'SI_EDIT_ALL',
    'SECURITY_OBJECT_ID_CENTRAL_ACCESS_RULE', 'DOBJ_VOL_NTACLS', 'SID_INFO',
    'SI_EDIT_PERMS', 'DOBJ_RES_CONT', 'SI_EDIT_OWNER', 'DOBJ_COND_NTACLS',
    'SI_OWNER_ELEVATION_REQUIRED', 'SI_RESET_SACL', 'SI_EDIT_EFFECTIVE',
    'SECURITY_OBJECT_ID_SHARE', 'SI_ACCESS_GENERAL', 'DOBJ_RES_ROOT',
    'SI_VIEW_ONLY', 'SI_ACCESS_CONTAINER', 'SECURITY_OBJECT_ID_OBJECT_SD',
    'SI_NO_ADDITIONAL_PERMISSION', '_SI_PAGE_TYPE', 'SI_PAGE_TYPE',
    '_SI_PAGE_ACTIVATED', 'SI_PAGE_ACTIVATED', 'IID_IEffectivePermission',
    'IID_ISecurityInformation4', 'IID_ISecurityInformation3', '_SID_INFO',
    'IID_ISecurityInformation2', 'IID_ISecurityInformation', '_SID_INFO_LIST',
    'IID_IEffectivePermission2', 'IID_ISecurityObjectTypeInfo', 'SI_ACCESS',
    'PSECURITY_OBJECT', 'PEFFPERM_RESULT_LIST', '_SI_INHERIT_TYPE',
    '_SI_OBJECT_INFO', 'PSI_INHERIT_TYPE', 'SID_INFO_LIST', 'SECURITY_OBJECT',
    'SI_INHERIT_TYPE', '_SECURITY_OBJECT', 'PSID_INFO', 'PSI_OBJECT_INFO',
    '_SI_ACCESS', 'EFFPERM_RESULT_LIST', 'PSI_ACCESS', 'PSID_INFO_LIST',
    '_EFFPERM_RESULT_LIST', 'SI_OBJECT_INFO', 'LPEFFECTIVEPERMISSION2',
    'LPSECURITYINFO', 'LPSECURITYINFO4', 'LPSECURITYINFO3', 'LPSECURITYINFO2',
    'LPSecurityObjectTypeInfo', 'LPEFFECTIVEPERMISSION',
)
