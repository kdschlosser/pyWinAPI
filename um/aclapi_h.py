
import ctypes
from shared.wtypes_h import (
    LPWSTR,
    VOID,
    DWORD,
    LPSTR
)
from shared.winapifamily_h import * # NOQA
from um.accctrl_h import * # NOQA

advapi32 = ctypes.windll.Advapi32

SetEntriesInAclW = advapi32.SetEntriesInAclW
SetEntriesInAclW.restype = DWORD
SetEntriesInAcl = advapi32.SetEntriesInAclA
SetEntriesInAcl.restype = DWORD

GetExplicitEntriesFromAclW = advapi32.GetExplicitEntriesFromAclW
GetExplicitEntriesFromAclW.restype = DWORD
GetExplicitEntriesFromAclA = advapi32.GetExplicitEntriesFromAclA
GetExplicitEntriesFromAclA.restype = DWORD
GetExplicitEntriesFromAcl = GetExplicitEntriesFromAclW

GetEffectiveRightsFromAclW = advapi32.GetEffectiveRightsFromAclW
GetEffectiveRightsFromAclW.restype = DWORD
GetEffectiveRightsFromAclA = advapi32.GetEffectiveRightsFromAclA
GetEffectiveRightsFromAclA.restype = DWORD
GetEffectiveRightsFromAcl = GetEffectiveRightsFromAclW

GetAuditedPermissionsFromAclW = advapi32.GetAuditedPermissionsFromAclW
GetAuditedPermissionsFromAclW.restype = DWORD
GetAuditedPermissionsFromAclA = advapi32.GetAuditedPermissionsFromAclA
GetAuditedPermissionsFromAclA.restype = DWORD
GetAuditedPermissionsFromAcl = GetAuditedPermissionsFromAclW

GetNamedSecurityInfoW = advapi32.GetNamedSecurityInfoW
GetNamedSecurityInfoW.restype = DWORD
GetNamedSecurityInfoA = advapi32.GetNamedSecurityInfoA
GetNamedSecurityInfoA.restype = DWORD
GetNamedSecurityInfo = GetNamedSecurityInfoW

SetNamedSecurityInfoW = advapi32.SetNamedSecurityInfoW
SetNamedSecurityInfoW.restype = DWORD
SetNamedSecurityInfoA = advapi32.SetNamedSecurityInfoA
SetNamedSecurityInfoA.restype = DWORD
SetNamedSecurityInfo = SetNamedSecurityInfoW

GetInheritanceSourceW = advapi32.GetInheritanceSourceW
GetInheritanceSourceW.restype = DWORD
GetInheritanceSourceA = advapi32.GetInheritanceSourceA
GetInheritanceSourceA.restype = DWORD
GetInheritanceSource = GetInheritanceSourceW

TreeResetNamedSecurityInfoW = advapi32.TreeResetNamedSecurityInfoW
TreeResetNamedSecurityInfoW.restype = DWORD
TreeResetNamedSecurityInfoA = advapi32.TreeResetNamedSecurityInfoA
TreeResetNamedSecurityInfoA.restype = DWORD
TreeResetNamedSecurityInfo = TreeResetNamedSecurityInfoW

TreeSetNamedSecurityInfoW = advapi32.TreeSetNamedSecurityInfoW
TreeSetNamedSecurityInfoW.restype = DWORD
TreeSetNamedSecurityInfoA = advapi32.TreeSetNamedSecurityInfoA
TreeSetNamedSecurityInfoA.restype = DWORD
TreeSetNamedSecurityInfo = TreeSetNamedSecurityInfoW

BuildSecurityDescriptorW = advapi32.BuildSecurityDescriptorW
BuildSecurityDescriptorW.restype = DWORD
BuildSecurityDescriptorA = advapi32.BuildSecurityDescriptorA
BuildSecurityDescriptorA.restype = DWORD
BuildSecurityDescriptor = BuildSecurityDescriptorW

LookupSecurityDescriptorPartsW = advapi32.LookupSecurityDescriptorPartsW
LookupSecurityDescriptorPartsW.restype = DWORD
LookupSecurityDescriptorPartsA = advapi32.LookupSecurityDescriptorPartsA
LookupSecurityDescriptorPartsA.restype = DWORD
LookupSecurityDescriptorParts = LookupSecurityDescriptorPartsW

BuildExplicitAccessWithNameW = advapi32.BuildExplicitAccessWithNameW
BuildExplicitAccessWithNameW.restype = VOID
BuildExplicitAccessWithNameA = advapi32.BuildExplicitAccessWithNameA
BuildExplicitAccessWithNameA.restype = VOID
BuildExplicitAccessWithName = BuildExplicitAccessWithNameW

BuildImpersonateExplicitAccessWithNameW = (
    advapi32.BuildImpersonateExplicitAccessWithNameW
)
BuildImpersonateExplicitAccessWithNameW.restype = VOID
BuildImpersonateExplicitAccessWithNameA = (
    advapi32.BuildImpersonateExplicitAccessWithNameA
)
BuildImpersonateExplicitAccessWithNameA.restype = VOID
BuildImpersonateExplicitAccessWithName = (
    BuildImpersonateExplicitAccessWithNameW
)

BuildTrusteeWithNameW = advapi32.BuildTrusteeWithNameW
BuildTrusteeWithNameW.restype = VOID
BuildTrusteeWithNameA = advapi32.BuildTrusteeWithNameA
BuildTrusteeWithNameA.restype = VOID
BuildTrusteeWithName = BuildTrusteeWithNameW

BuildImpersonateTrusteeW = advapi32.BuildImpersonateTrusteeW
BuildImpersonateTrusteeW.restype = VOID
BuildImpersonateTrusteeA = advapi32.BuildImpersonateTrusteeA
BuildImpersonateTrusteeA.restype = VOID
BuildImpersonateTrustee = BuildImpersonateTrusteeW

BuildTrusteeWithSidW = advapi32.BuildTrusteeWithSidW
BuildTrusteeWithSidW.restype = VOID
BuildTrusteeWithSidA = advapi32.BuildTrusteeWithSidA
BuildTrusteeWithSidA.restype = VOID
BuildTrusteeWithSid = BuildTrusteeWithSidW

BuildTrusteeWithObjectsAndSidW = advapi32.BuildTrusteeWithObjectsAndSidW
BuildTrusteeWithObjectsAndSidW.restype = VOID
BuildTrusteeWithObjectsAndSidA = advapi32.BuildTrusteeWithObjectsAndSidA
BuildTrusteeWithObjectsAndSidA.restype = VOID
BuildTrusteeWithObjectsAndSid = BuildTrusteeWithObjectsAndSidW

BuildTrusteeWithObjectsAndNameW = advapi32.BuildTrusteeWithObjectsAndNameW
BuildTrusteeWithObjectsAndNameW.restype = VOID
BuildTrusteeWithObjectsAndNameA = advapi32.BuildTrusteeWithObjectsAndNameA
BuildTrusteeWithObjectsAndNameA.restype = VOID
BuildTrusteeWithObjectsAndName = BuildTrusteeWithObjectsAndNameW

GetTrusteeNameW = advapi32.GetTrusteeNameW
GetTrusteeNameW.restype = LPSTR
GetTrusteeNameA = advapi32.GetTrusteeNameA
GetTrusteeNameA.restype = LPWSTR
GetTrusteeName = GetTrusteeNameW

GetTrusteeTypeW = advapi32.GetTrusteeTypeW
GetTrusteeTypeW.restype = TRUSTEE_TYPE
GetTrusteeTypeA = advapi32.GetTrusteeTypeA
GetTrusteeTypeA.restype = TRUSTEE_TYPE
GetTrusteeType = GetTrusteeTypeW

GetTrusteeFormW = advapi32.GetTrusteeFormW
GetTrusteeFormW.restype = TRUSTEE_FORM
GetTrusteeFormA = advapi32.GetTrusteeFormA
GetTrusteeFormA.restype = TRUSTEE_FORM
GetTrusteeForm = GetTrusteeFormW

GetMultipleTrusteeOperationW = advapi32.GetMultipleTrusteeOperationW
GetMultipleTrusteeOperationW.restype = MULTIPLE_TRUSTEE_OPERATION
GetMultipleTrusteeOperationA = advapi32.GetMultipleTrusteeOperationA
GetMultipleTrusteeOperationA.restype = MULTIPLE_TRUSTEE_OPERATION
GetMultipleTrusteeOperation = GetMultipleTrusteeOperationW

GetMultipleTrusteeW = advapi32.GetMultipleTrusteeW
GetMultipleTrusteeW.restype = PTRUSTEE_A
GetMultipleTrusteeA = advapi32.GetMultipleTrusteeA
GetMultipleTrusteeA.restype = PTRUSTEE_A
GetMultipleTrustee = GetMultipleTrusteeW

__all__ = (
    'GetMultipleTrusteeOperation', 'BuildTrusteeWithSid', 'GetTrusteeForm',
    'GetEffectiveRightsFromAcl', 'BuildImpersonateExplicitAccessWithName',
    'BuildTrusteeWithObjectsAndName', 'GetMultipleTrustee', 'GetTrusteeName',
    'LookupSecurityDescriptorParts', 'TreeSetNamedSecurityInfo',
    'GetNamedSecurityInfo', 'BuildTrusteeWithObjectsAndSid', 'GetTrusteeType',
    'SetNamedSecurityInfo', 'GetInheritanceSource', 'BuildTrusteeWithName',
    'GetAuditedPermissionsFromAcl', 'TreeResetNamedSecurityInfo',
    'BuildSecurityDescriptor', 'BuildExplicitAccessWithName',
    'GetExplicitEntriesFromAcl', 'SetEntriesInAcl', 'BuildImpersonateTrustee',
)
