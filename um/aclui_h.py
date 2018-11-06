import comtypes
import ctypes

__cplusplus = None
CINTERFACE = 1

STDMETHOD = comtypes.STDMETHOD


from pyWinAPI import *
from shared.sdkddkver_h import *
from shared.wtypes_h import *
from shared.winapifamily_h import *
from shared.guiddef_h import EXTERN_GUID


_ACLUI_
_ACLUI_H_

# + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Microsoft Windows Copyright (c) Microsoft Corporation. All rights reserved.
# File: aclui.h Contents: Definitions and prototypes for the ACLUI.DLL -

if _MSC_VER >= 800:
    if _MSC_VER >= 1200:
       pass
    # END IF
# END IF

if not defined(_ACLUI_H_):
    _ACLUI_H_ = 1

    if _MSC_VER > 1000:
        pass
    # END IF
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        from um.objbase_h import *
        from um.commctrl_h import *   # for HPROPSHEETPAGE
        from um.accctrl_h import *   # for SE_OBJECT_TYPE
        from um.authz_h import *
        from um.objidl_h import LPDATAOBJECT
        from um.winnt_h import (
            ACCESS_MASK,
            PACCESS_MASK,
            SECURITY_INFORMATION,
            PSECURITY_DESCRIPTOR,
            POBJECT_TYPE_LIST,
            OBJECT_TYPE_LIST,
            PTOKEN_GROUPS,
        )

        if not defined(_ACLUI_):
            ACLUIAPI = WINAPI
        else:
            ACLUIAPI = WINAPI
        # END IF

        if defined(__cplusplus):
            pass
        # END IF  __cplusplus

        class _SI_OBJECT_INFO(ctypes.Structure):
            pass


        _SI_OBJECT_INFO._fields_ = [
            ('dwFlags', DWORD),
            ('hInstance', HINSTANCE), # resources (e.g. strings) reside here
            ('pszServerName', LPWSTR), # must be present
            ('pszObjectName', LPWSTR), # must be present
            ('pszPageTitle', LPWSTR), # only valid if SI_PAGE_TITLE is set
            ('guidObjectType', GUID), # only valid if SI_OBJECT_GUID is set
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

        if NTDDI_VERSION >= NTDDI_VISTA:
            SI_VIEW_ONLY = 0x00400000
            SI_PERMS_ELEVATION_REQUIRED = 0x01000000
            SI_AUDITS_ELEVATION_REQUIRED = 0x02000000
            SI_OWNER_ELEVATION_REQUIRED = 0x04000000

            if NTDDI_VERSION >= NTDDI_WIN8:
                SI_SCOPE_ELEVATION_REQUIRED = 0x08000000
            # END IF   NTDDI_VERSION >= NTDDI_WIN8

        # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

        SI_MAY_WRITE = 0x10000000

        if NTDDI_VERSION >= NTDDI_WIN8:
            SI_ENABLE_EDIT_ATTRIBUTE_CONDITION = 0x20000000
            SI_ENABLE_CENTRAL_POLICY = 0x40000000
            SI_DISABLE_DENY_ACE = 0x80000000
        # END IF   NTDDI_VERSION >= NTDDI_WIN8

        SI_EDIT_ALL = SI_EDIT_PERMS | SI_EDIT_OWNER | SI_EDIT_AUDITS


        class _SI_ACCESS(ctypes.Structure):
            pass


        _SI_ACCESS._fields_ = [
            ('pguid', POINTER(GUID)),
            ('mask', ACCESS_MASK),
            ('pszName', LPCWSTR), # may be resource ID
            ('dwFlags', DWORD),
        ]

        SI_ACCESS = _SI_ACCESS
        PSI_ACCESS = POINTER(_SI_ACCESS)

        SI_ACCESS_SPECIFIC = 0x00010000
        SI_ACCESS_GENERAL = 0x00020000
        SI_ACCESS_CONTAINER = 0x00040000
        SI_ACCESS_PROPERTY = 0x00080000


        class _SI_INHERIT_TYPE(ctypes.Structure):
            pass


        _SI_INHERIT_TYPE._fields_ = [
            ('pguid', POINTER(GUID)),
            ('dwFlags', ULONG),
            ('pszName', LPCWSTR), # may be resource ID
        ]

        SI_INHERIT_TYPE = _SI_INHERIT_TYPE
        PSI_INHERIT_TYPE = POINTER(_SI_INHERIT_TYPE)

        class _SI_PAGE_TYPE(ENUM):
            SI_PAGE_PERM = 0
            SI_PAGE_ADVPERM = 1
            SI_PAGE_AUDIT = 2
            SI_PAGE_OWNER = 3
            SI_PAGE_EFFECTIVE = 4

            if NTDDI_VERSION >= NTDDI_VISTA:
                SI_PAGE_TAKEOWNERSHIP = 5
            # END IF

            if NTDDI_VERSION >= NTDDI_WIN8:
                SI_PAGE_SHARE = 6
            # END IF


        SI_PAGE_TYPE = _SI_PAGE_TYPE
        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

        if NTDDI_VERSION >= NTDDI_WIN8:
            pass
        # END IF

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
            return UINT(X & 0x0000FFFF).value


        def GET_ACTIVATION_TYPE(Y):
            return UINT((Y >> 16) & 0x0000FFFF).value


        def COMBINE_PAGE_ACTIVATION(X, Y):
            return UINT((Y << 16) | X).value


        IID_ISecurityInformation = IID(
            '{965FC360-16FF-11d0-91CB-00AA00BBB723}'
        )


        class ISecurityInformation(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = IID_ISecurityInformation
            _idlflags_ = []
            _methods_ = [
                STDMETHOD(
                    None,
                    'GetObjectInformation',
                    (PSI_OBJECT_INFO,),
                ),
                STDMETHOD(
                    None,
                    'GetSecurity',
                    (SECURITY_INFORMATION, PSECURITY_DESCRIPTOR, BOOL),
                ),
                STDMETHOD(
                    None,
                    'GetAccessRights',
                    (
                        POINTER(GUID),
                        DWORD,
                        POINTER(PSI_ACCESS),
                        POINTER(ULONG),
                        POINTER(ULONG)
                    ),
                ),
                STDMETHOD(
                    None,
                    'MapGeneric',
                    (POINTER(GUID), POINTER(UCHAR), POINTER(ACCESS_MASK)),
                ),
                STDMETHOD(
                    None,
                    'GetInheritTypes',
                    (POINTER(PSI_INHERIT_TYPE), POINTER(ULONG)),
                ),
                STDMETHOD(
                    None,
                    'PropertySheetPageCallback',
                    (HWND, UINT, SI_PAGE_TYPE),
                ),

            ]

        LPSECURITYINFO = POINTER(ISecurityInformation)

        IID_ISecurityInformation2 = IID(
            '{c3ccfdb4-6f88-11d2-a3ce-00c04fb1782a}'
        )


        class ISecurityInformation2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = IID_ISecurityInformation2
            _idlflags_ = []
            _methods_ = [
                STDMETHOD(
                    BOOL,
                    'IsDaclCanonical',
                    (PACL,),
                ),
                STDMETHOD(
                    None,
                    'LookupSids',
                    (ULONG, POINTER(PSID), POINTER(LPDATAOBJECT))
                ),
            ]
        LPSECURITYINFO2 = POINTER(ISecurityInformation2)

        # HGLOBAL containing SID_INFO_LIST returned by
        # ISecurityInformation2::LookupSids
        CFSTR_ACLUI_SID_INFO_LIST = TEXT("CFSTR_ACLUI_SID_INFO_LIST")

        # Data structures corresponding to CFSTR_ACLUI_SID_INFO_LIST
        class _SID_INFO(ctypes.Structure):
            pass


        _SID_INFO._fields_ = [
            ('pSid', PSID),
            ('pwzCommonName', PWSTR),
            # Used for selecting icon, e.g. "User" or "Group"
            ('pwzClass', PWSTR),
            ('pwzUPN', PWSTR), # Optional, may be NULL
        ]

        SID_INFO = _SID_INFO
        PSID_INFO = POINTER(_SID_INFO)


        class _SID_INFO_LIST(ctypes.Structure):
            pass


        _SID_INFO_LIST._fields_ = [
            ('cItems', ULONG),
            ('aSidInfo', SID_INFO * ANYSIZE_ARRAY),
        ]

        SID_INFO_LIST = _SID_INFO_LIST
        PSID_INFO_LIST = POINTER(_SID_INFO_LIST)

        IID_IEffectivePermission = IID(
            '{3853DC76-9F35-407c-88A1-D19344365FBC}'
        )


        class IEffectivePermission(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = IID_IEffectivePermission
            _idlflags_ = []
            _methods_ = [
                STDMETHOD(
                    None,
                    'GetEffectivePermission',
                    (
                        GUID,
                        PSID,
                        LPCWSTR,
                        PSECURITY_DESCRIPTOR,
                        POINTER(POBJECT_TYPE_LIST),
                        POINTER(ULONG),
                        POINTER(PACCESS_MASK),
                        POINTER(ULONG),
                    )
                ),
            ]

        LPEFFECTIVEPERMISSION = POINTER(IEffectivePermission)

        IID_ISecurityObjectTypeInfo = IID(
            '{FC3066EB-79EF-444b-9111-D18A75EBF2FA}'
        )


        class ISecurityObjectTypeInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = IID_ISecurityObjectTypeInfo
            _idlflags_ = []
            _methods_ = [
                STDMETHOD(
                    None,
                    'GetInheritSource',
                    (
                        SECURITY_INFORMATION,
                        PACL,
                        POINTER(PINHERITED_FROM),
                    )
                ),
            ]

        LPSecurityObjectTypeInfo = POINTER(ISecurityObjectTypeInfo)

        if NTDDI_VERSION >= NTDDI_VISTA:
            # Support for separation or read-only ACL viewer and
            # elevated ACL editor

            IID_ISecurityInformation3 = IID(
                '{E2CDC9CC-31BD-4f8f-8C8B-B641AF516A1A}'
            )


            class ISecurityInformation3(comtypes.IUnknown):
                _case_insensitive_ = True
                _iid_ = IID_ISecurityInformation3
                _idlflags_ = []
                _methods_ = [
                    STDMETHOD(
                        None,
                        'GetFullResourceName',
                        (POINTER(LPWSTR),)
                    ),
                    STDMETHOD(
                        None,
                        'OpenElevatedEditor',
                        (HWND, SI_PAGE_TYPE)
                    ),
                ]

            LPSECURITYINFO3 = POINTER(ISecurityInformation3)

        # END IF (NTDDI_VERSION >= NTDDI_VISTA)

        if NTDDI_VERSION >= NTDDI_WIN8:

            class _SECURITY_OBJECT(ctypes.Structure):
                pass


            _SECURITY_OBJECT._fields_ = [
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

            SECURITY_OBJECT_ID_OBJECT_SD = 1
            SECURITY_OBJECT_ID_SHARE = 2
            SECURITY_OBJECT_ID_CENTRAL_POLICY = 3
            SECURITY_OBJECT_ID_CENTRAL_ACCESS_RULE = 4


            class _EFFPERM_RESULT_LIST(ctypes.Structure):
                pass


            _EFFPERM_RESULT_LIST._fields_ = [
                ('fEvaluated', BOOLEAN),
                ('cObjectTypeListLength', ULONG),
                ('pObjectTypeList', POINTER(OBJECT_TYPE_LIST)),
                ('pGrantedAccessList', POINTER(ACCESS_MASK)),
            ]

            EFFPERM_RESULT_LIST = _EFFPERM_RESULT_LIST
            PEFFPERM_RESULT_LIST = POINTER(_EFFPERM_RESULT_LIST)

            IID_ISecurityInformation4 = IID(
                '{EA961070-CD14-4621-ACE4-F63C03E583E4}'
            )


            class ISecurityInformation4(comtypes.IUnknown):
                _case_insensitive_ = True
                _iid_ = IID_ISecurityInformation4
                _idlflags_ = []
                _methods_ = [
                    STDMETHOD(
                        None,
                        'GetSecondarySecurity',
                        (POINTER(PSECURITY_OBJECT), PULONG)
                    ),
                ]
            LPSECURITYINFO4 = POINTER(ISecurityInformation4)

            IID_IEffectivePermission2 = IID(
                '{941FABCA-DD47-4FCA-90BB-B0E10255F20D}'
            )


            class IEffectivePermission2(comtypes.IUnknown):
                _case_insensitive_ = True
                _iid_ = IID_IEffectivePermission2
                _idlflags_ = []
                _methods_ = [
                    STDMETHOD(
                        None,
                        'ComputeEffectivePermissionWithSecondarySecurity',
                        (
                            PSID,
                            PSID,
                            PCWSTR,
                            PSECURITY_OBJECT,
                            DWORD,
                            PTOKEN_GROUPS,
                            PAUTHZ_SID_OPERATION,
                            PAUTHZ_SID_OPERATION,
                            PAUTHZ_SECURITY_ATTRIBUTES_INFORMATION,
                            PAUTHZ_SECURITY_ATTRIBUTE_OPERATION,
                            PAUTHZ_SECURITY_ATTRIBUTES_INFORMATION,
                            PAUTHZ_SECURITY_ATTRIBUTE_OPERATION,
                            PEFFPERM_RESULT_LIST,
                        )
                    ),
                ]
            LPEFFECTIVEPERMISSION2 = POINTER(IEffectivePermission2)

        # END IF (NTDDI_VERSION >= NTDDI_WIN8)

        # {965FC360-16FF-11d0-91CB-00AA00BBB723}
        IID_ISecurityInformation = EXTERN_GUID(
            0x965fc360,
            0x16ff,
            0x11d0,
            0x91,
            0xcb,
            0x0,
            0xaa,
            0x0,
            0xbb,
            0xb7,
            0x23
        )

        # {c3ccfdb4-6f88-11d2-a3ce-00c04fb1782a}
        IID_ISecurityInformation2 = EXTERN_GUID(
            0xc3ccfdb4,
            0x6f88,
            0x11d2,
            0xa3,
            0xce,
            0x0,
            0xc0,
            0x4f,
            0xb1,
            0x78,
            0x2a
        )

        # {3853DC76-9F35-407c-88A1-D19344365FBC}
        IID_IEffectivePermission = EXTERN_GUID(
            0x3853dc76,
            0x9f35,
            0x407c,
            0x88,
            0xa1,
            0xd1,
            0x93,
            0x44,
            0x36,
            0x5f,
            0xbc
        )

        # {FC3066EB-79EF-444b-9111-D18A75EBF2FA}
        IID_ISecurityObjectTypeInfo = EXTERN_GUID(
            0xfc3066eb,
            0x79ef,
            0x444b,
            0x91,
            0x11,
            0xd1,
            0x8a,
            0x75,
            0xeb,
            0xf2,
            0xfa
        )

        if NTDDI_VERSION >= NTDDI_VISTA:
            # {E2CDC9CC-31BD-4f8f-8C8B-B641AF516A1A}
            IID_ISecurityInformation3 = EXTERN_GUID(
                0xe2cdc9cc,
                0x31bd,
                0x4f8f,
                0x8c,
                0x8b,
                0xb6,
                0x41,
                0xaf,
                0x51,
                0x6a,
                0x1a
            )

        # END IF (NTDDI_VERSION >= NTDDI_VISTA)

        if NTDDI_VERSION >= NTDDI_WIN8:
            # {EA961070-CD14-4621-ACE4-F63C03E583E4}
            IID_ISecurityInformation4 = EXTERN_GUID(
                0xea961070,
                0xcd14,
                0x4621,
                0xac,
                0xe4,
                0xf6,
                0x3c,
                0x3,
                0xe5,
                0x83,
                0xe4
            )

            # {941FABCA-DD47-4FCA-90BB-B0E10255F20D}
            IID_IEffectivePermission2 = EXTERN_GUID(
                0x941fabca,
                0xdd47,
                0x4fca,
                0x90,
                0xbb,
                0xb0,
                0xe1,
                0x2,
                0x55,
                0xf2,
                0xd
            )
            # END IF (NTDDI_VERSION >= NTDDI_WIN8)

        if defined(__cplusplus):
            pass
        # END IF  __cplusplus

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF  _ACLUI_H_

if _MSC_VER >= 1200:
    pass
else:
     pass
# END IF

if _MSC_VER >= 800:
    pass
# END IF
