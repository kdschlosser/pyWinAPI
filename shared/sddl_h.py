import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *

# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: sddl.w Abstract: This module defines the support and conversions
# routines necessary for SDDL. Revision History: - -
if defined(_MSC_VER):
    pass
# END IF   _MSC_VER

__SDDL_H__ = None


if not defined(__SDDL_H__):
    __SDDL_H__ = 1
    from pyWinAPI.shared.apiset_h import * # NOQA
    from pyWinAPI.shared.apisetcconv_h import * # NOQA
    from pyWinAPI.shared.winapifamily_h import *  # NOQA

    _CONTRACT_GEN = 1
    if defined(_CONTRACT_GEN):
        from pyWinAPI.shared.minwindef_h import * # NOQA
    # END IF

    advapi32 = ctypes.windll.ADVAPI32

    if defined(__cplusplus):
        pass
        # extern "C" {
    # END IF
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # SDDL Version information
        blash = 1
        SDDL_REVISION_1 = 1
        SDDL_REVISION = SDDL_REVISION_1

        # SDDL Component tags
        SDDL_OWNER = TEXT("O")  # Owner tag
        SDDL_GROUP = TEXT("G")  # Group tag
        SDDL_DACL = TEXT("D")  # DACL tag
        SDDL_SACL = TEXT("S")  # SACL tag

        # SDDL Security descriptor controls
        SDDL_PROTECTED = TEXT("P")  # DACL or SACL Protected
        SDDL_AUTO_INHERIT_REQ = TEXT("AR")  # Auto inherit request
        SDDL_AUTO_INHERITED = TEXT("AI")  # DACL/SACL are auto inherited
        SDDL_NULL_ACL = TEXT("NO_ACCESS_CONTROL")  # Null ACL

        # SDDL Ace types
        SDDL_ACCESS_ALLOWED = TEXT("A")  # Access allowed
        SDDL_ACCESS_DENIED = TEXT("D")  # Access denied
        SDDL_OBJECT_ACCESS_ALLOWED = TEXT("OA")  # Object access allowed
        SDDL_OBJECT_ACCESS_DENIED = TEXT("OD")  # Object access denied
        SDDL_AUDIT = TEXT("AU")  # Audit
        SDDL_ALARM = TEXT("AL")  # Alarm
        SDDL_OBJECT_AUDIT = TEXT("OU")  # Object audit
        SDDL_OBJECT_ALARM = TEXT("OL")  # Object alarm
        SDDL_MANDATORY_LABEL = TEXT("ML")  # Integrity label
        SDDL_PROCESS_TRUST_LABEL = TEXT("TL")  # Process trust label
        SDDL_CALLBACK_ACCESS_ALLOWED = TEXT("XA")  # Callback access allowed
        SDDL_CALLBACK_ACCESS_DENIED = TEXT("XD")  # Callback access denied
        SDDL_RESOURCE_ATTRIBUTE = TEXT("RA")  # Resource attribute
        SDDL_SCOPED_POLICY_ID = TEXT("SP")  # Scoped policy
        SDDL_CALLBACK_AUDIT = TEXT("XU")  # Callback audit
        SDDL_CALLBACK_OBJECT_ACCESS_ALLOWED = TEXT("ZA")  # Callback object access allowed
        SDDL_ACCESS_FILTER = TEXT("FL")  # Access Filter

        # SDDL Resource attribute ace data types
        SDDL_INT = TEXT("TI")  # Signed integer
        SDDL_UINT = TEXT("TU")  # Unsigned integer
        SDDL_WSTRING = TEXT("TS")  # Wide string
        SDDL_SID = TEXT("TD")  # SID
        SDDL_BLOB = TEXT("TX")  # Octet String
        SDDL_BOOLEAN = TEXT("TB")  # Boolean

        # SDDL Ace flags
        SDDL_CONTAINER_INHERIT = TEXT("CI")  # Container inherit
        SDDL_OBJECT_INHERIT = TEXT("OI")  # Object inherit
        SDDL_NO_PROPAGATE = TEXT("NP")  # Inherit no propagate
        SDDL_INHERIT_ONLY = TEXT("IO")  # Inherit only
        SDDL_INHERITED = TEXT("ID")  # Inherited
        SDDL_TRUST_PROTECTED_FILTER = TEXT("TP")  # Trust Protected Filter
        SDDL_AUDIT_SUCCESS = TEXT("SA")  # Audit success
        SDDL_AUDIT_FAILURE = TEXT("FA")  # Audit failure

        # SDDL Rights
        SDDL_READ_PROPERTY = TEXT("RP")
        SDDL_WRITE_PROPERTY = TEXT("WP")
        SDDL_CREATE_CHILD = TEXT("CC")
        SDDL_DELETE_CHILD = TEXT("DC")
        SDDL_LIST_CHILDREN = TEXT("LC")
        SDDL_SELF_WRITE = TEXT("SW")
        SDDL_LIST_OBJECT = TEXT("LO")
        SDDL_DELETE_TREE = TEXT("DT")
        SDDL_CONTROL_ACCESS = TEXT("CR")
        SDDL_READ_CONTROL = TEXT("RC")
        SDDL_WRITE_DAC = TEXT("WD")
        SDDL_WRITE_OWNER = TEXT("WO")
        SDDL_STANDARD_DELETE = TEXT("SD")
        SDDL_GENERIC_ALL = TEXT("GA")
        SDDL_GENERIC_READ = TEXT("GR")
        SDDL_GENERIC_WRITE = TEXT("GW")
        SDDL_GENERIC_EXECUTE = TEXT("GX")
        SDDL_FILE_ALL = TEXT("FA")
        SDDL_FILE_READ = TEXT("FR")
        SDDL_FILE_WRITE = TEXT("FW")
        SDDL_FILE_EXECUTE = TEXT("FX")
        SDDL_KEY_ALL = TEXT("KA")
        SDDL_KEY_READ = TEXT("KR")
        SDDL_KEY_WRITE = TEXT("KW")
        SDDL_KEY_EXECUTE = TEXT("KX")
        SDDL_NO_WRITE_UP = TEXT("NW")
        SDDL_NO_READ_UP = TEXT("NR")
        SDDL_NO_EXECUTE_UP = TEXT("NX")

        # SDDL User alias max size
        # - currently, upto two supported eg. "DA"
        # - modify this if more WCHARs need to be there in future e.g. "DAX"
        SDDL_ALIAS_SIZE = 2

        # SDDL User aliases
        SDDL_DOMAIN_ADMINISTRATORS = TEXT("DA")  # Domain admins
        SDDL_DOMAIN_GUESTS = TEXT("DG")  # Domain guests
        SDDL_DOMAIN_USERS = TEXT("DU")  # Domain users
        SDDL_ENTERPRISE_DOMAIN_CONTROLLERS = TEXT("ED")  # Enterprise domain controllers
        SDDL_DOMAIN_DOMAIN_CONTROLLERS = TEXT("DD")  # Domain domain controllers
        SDDL_DOMAIN_COMPUTERS = TEXT("DC")  # Domain computers
        SDDL_BUILTIN_ADMINISTRATORS = TEXT("BA")  # Builtin (local ) administrators
        SDDL_BUILTIN_GUESTS = TEXT("BG")  # Builtin (local ) guests
        SDDL_BUILTIN_USERS = TEXT("BU")  # Builtin (local ) users
        SDDL_LOCAL_ADMIN = TEXT("LA")  # Local administrator account
        SDDL_LOCAL_GUEST = TEXT("LG")  # Local group account
        SDDL_ACCOUNT_OPERATORS = TEXT("AO")  # Account operators
        SDDL_BACKUP_OPERATORS = TEXT("BO")  # Backup operators
        SDDL_PRINTER_OPERATORS = TEXT("PO")  # Printer operators
        SDDL_SERVER_OPERATORS = TEXT("SO")  # Server operators
        SDDL_AUTHENTICATED_USERS = TEXT("AU")  # Authenticated users
        SDDL_PERSONAL_SELF = TEXT("PS")  # Personal self
        SDDL_CREATOR_OWNER = TEXT("CO")  # Creator owner
        SDDL_CREATOR_GROUP = TEXT("CG")  # Creator group
        SDDL_LOCAL_SYSTEM = TEXT("SY")  # Local system
        SDDL_POWER_USERS = TEXT("PU")  # Power users
        SDDL_EVERYONE = TEXT("WD")  # Everyone ( World )
        SDDL_REPLICATOR = TEXT("RE")  # Replicator
        SDDL_INTERACTIVE = TEXT("IU")  # Interactive logon user
        SDDL_NETWORK = TEXT("NU")  # Nework logon user
        SDDL_SERVICE = TEXT("SU")  # Service logon user
        SDDL_RESTRICTED_CODE = TEXT("RC")  # Restricted code
        SDDL_WRITE_RESTRICTED_CODE = TEXT("WR")  # Write Restricted code
        SDDL_ANONYMOUS = TEXT("AN")  # Anonymous Logon
        SDDL_SCHEMA_ADMINISTRATORS = TEXT("SA")  # Schema Administrators
        SDDL_CERT_SERV_ADMINISTRATORS = TEXT("CA")  # Certificate Server Administrators
        SDDL_RAS_SERVERS = TEXT("RS")  # RAS servers group
        SDDL_ENTERPRISE_ADMINS = TEXT("EA")  # Enterprise administrators
        SDDL_GROUP_POLICY_ADMINS = TEXT("PA")  # Group Policy administrators
        SDDL_ALIAS_PREW2KCOMPACC = TEXT("RU")  # alias to allow previous windows 2000
        SDDL_LOCAL_SERVICE = TEXT("LS")  # Local service account (for services)
        SDDL_NETWORK_SERVICE = TEXT("NS")  # Network service account (for services)
        SDDL_REMOTE_DESKTOP = TEXT("RD")  # Remote desktop users (for terminal server)

        # Network configuration operators
        # ( to manage configuration of networking features)
        SDDL_NETWORK_CONFIGURATION_OPS = TEXT("NO")
        SDDL_PERFMON_USERS = TEXT("MU")  # Performance Monitor Users
        SDDL_PERFLOG_USERS = TEXT("LU")  # Performance Log Users
        SDDL_IIS_USERS = TEXT("IS")  # Anonymous Internet Users
        SDDL_CRYPTO_OPERATORS = TEXT("CY")  # Crypto Operators
        SDDL_OWNER_RIGHTS = TEXT("OW")  # Owner Rights SID
        SDDL_EVENT_LOG_READERS = TEXT("ER")  # Event log readers
        SDDL_ENTERPRISE_RO_DCs = TEXT("RO")  # Enterprise Read - only domain controllers
        SDDL_CERTSVC_DCOM_ACCESS = TEXT("CD")  # Users who can connect to certification authorities using DCOM
        SDDL_ALL_APP_PACKAGES = TEXT("AC")  # All applications running in an app package context

        # Servers in this group enable users of RemoteApp programs and personal
        # virtual desktops access to these resources.
        SDDL_RDS_REMOTE_ACCESS_SERVERS = TEXT("RA")

        # Servers in this group run virtual machines and host sessions where users
        # RemoteApp programs and personal virtual desktops run.
        SDDL_RDS_ENDPOINT_SERVERS = TEXT("ES")

        # Servers in this group can perform routine administrative actions on
        # servers running Remote Desktop Services.
        SDDL_RDS_MANAGEMENT_SERVERS = TEXT("MS")
        SDDL_USER_MODE_DRIVERS = TEXT("UD")  # UserMode driver

        # Members of this group have complete and unrestricted access to all
        # features of Hyper - V.
        SDDL_HYPER_V_ADMINS = TEXT("HA")
        SDDL_CLONEABLE_CONTROLLERS = TEXT("CN")  # Members of this group that are domain controllers may be cloned.

        # Members of this group can remotely query authorization attributes and
        # permissions for resources on this computer.
        SDDL_ACCESS_CONTROL_ASSISTANCE_OPS = TEXT("AA")
        SDDL_AUTHORITY_ASSERTED = TEXT("AS")  # Authentication Authority Asserted
        SDDL_SERVICE_ASSERTED = TEXT("SS")  # Authentication Service Asserted

        # Members of this group are afforded additional protections against
        # authentication security threats.
        SDDL_PROTECTED_USERS = TEXT("AP")

        # Members of this group have full control over all key credential objects
        # in the domain
        SDDL_KEY_ADMINS = TEXT("KA")

        # Members of this group have full control over all key credential objects
        # in the forest
        SDDL_ENTERPRISE_KEY_ADMINS = TEXT("EK")

        # Note not not While making the above changes check if
        # ScepReplaceNewAcronymsInSDDL
        # needs to be updated to allow the new SIDs to be translated on downlevel
        # OS.
        # Integrity Labels
        SDDL_ML_LOW = TEXT("LW")  # Low mandatory level
        SDDL_ML_MEDIUM = TEXT("ME")  # Medium mandatory level
        SDDL_ML_MEDIUM_PLUS = TEXT("MP")  # Medium Plus mandatory level
        SDDL_ML_HIGH = TEXT("HI")  # High mandatory level
        SDDL_ML_SYSTEM = TEXT("SI")  # System mandatory level

        # SDDL Seperators - character version
        SDDL_SEPERATORC = TEXT(';')
        SDDL_DELIMINATORC = TEXT(':')
        SDDL_ACE_BEGINC = TEXT('(')
        SDDL_ACE_ENDC = TEXT(')')
        SDDL_SPACEC = TEXT(' ')
        SDDL_ACE_COND_BEGINC = TEXT('(')
        SDDL_ACE_COND_ENDC = TEXT(')')
        SDDL_ACE_COND_STRING_BEGINC = TEXT('"')
        SDDL_ACE_COND_STRING_ENDC = TEXT('"')
        SDDL_ACE_COND_COMPOSITEVALUE_BEGINC = TEXT('{')
        SDDL_ACE_COND_COMPOSITEVALUE_ENDC = TEXT('}')
        SDDL_ACE_COND_COMPOSITEVALUE_SEPERATORC = TEXT(',')
        SDDL_ACE_COND_BLOB_PREFIXC = TEXT('#')
        SDDL_ACE_COND_SID_BEGINC = TEXT('(')
        SDDL_ACE_COND_SID_ENDC = TEXT(')')

        # SDDL Seperators - string version
        SDDL_SEPERATOR = TEXT(";")
        SDDL_DELIMINATOR = TEXT(":")
        SDDL_ACE_BEGIN = TEXT("(")
        SDDL_ACE_END = TEXT(")")
        SDDL_ACE_COND_BEGIN = TEXT("(")
        SDDL_ACE_COND_END = TEXT(")")
        SDDL_SPACE = TEXT(" ")
        SDDL_ACE_COND_BLOB_PREFIX = TEXT("#")
        SDDL_ACE_COND_SID_PREFIX = TEXT("SID")
        SDDL_ACE_COND_ATTRIBUTE_PREFIX = TEXT("@")
        SDDL_ACE_COND_USER_ATTRIBUTE_PREFIX = TEXT("@USER.")
        SDDL_ACE_COND_RESOURCE_ATTRIBUTE_PREFIX = TEXT("@RESOURCE.")
        SDDL_ACE_COND_DEVICE_ATTRIBUTE_PREFIX = TEXT("@DEVICE.")
        SDDL_ACE_COND_TOKEN_ATTRIBUTE_PREFIX = TEXT("@TOKEN.")
        #
        if not defined(_NTDDK_):

            if _WIN32_WINNT >= 0x0500:
                # _Success_(return != FALSE)
                # BOOL
                # WINAPI
                # ConvertSidToStringSidA(
                # _In_  PSID     Sid,
                # _Outptr_ LPSTR  *StringSid
                # );
                ConvertSidToStringSidA = advapi32.ConvertSidToStringSidA
                ConvertSidToStringSidA.restype = BOOL
                # _Success_(return != FALSE)
                # BOOL
                # WINAPI
                # ConvertSidToStringSidW(
                # _In_ PSID Sid,
                # _Outptr_ LPWSTR* StringSid
                # );
                ConvertSidToStringSidW = advapi32.ConvertSidToStringSidW
                ConvertSidToStringSidW.restype = BOOL
                if defined(UNICODE):
                    ConvertSidToStringSid = ConvertSidToStringSidW
                else:
                    ConvertSidToStringSid = ConvertSidToStringSidA
                # END IF   not UNICODE
                # _Success_(return != FALSE)
                # BOOL
                # WINAPI
                # ConvertStringSidToSidA(
                # _In_ LPCSTR   StringSid,
                # _Outptr_ PSID   *Sid
                # );
                ConvertStringSidToSidA = advapi32.ConvertStringSidToSidA
                ConvertStringSidToSidA.restype = BOOL


                # _Success_(return != FALSE)
                # BOOL
                # WINAPI
                # ConvertStringSidToSidW(
                # _In_ LPCWSTR StringSid,
                # _Outptr_ PSID* Sid
                # );
                ConvertStringSidToSidW = advapi32.ConvertStringSidToSidW
                ConvertStringSidToSidW.restype = BOOL

                if defined(UNICODE):
                    ConvertStringSidToSid = ConvertStringSidToSidW
                else:
                    ConvertStringSidToSid = ConvertStringSidToSidA
                # END IF   not UNICODE

                # _Success_(return != FALSE)
                # BOOL
                # WINAPI
                # ConvertStringSecurityDescriptorToSecurityDescriptorA(
                # _In_  LPCSTR StringSecurityDescriptor,
                # _In_  DWORD StringSDRevision,
                # _Outptr_ PSECURITY_DESCRIPTOR  *SecurityDescriptor,
                # _Out_opt_ PULONG  SecurityDescriptorSize
                # );
                ConvertStringSecurityDescriptorToSecurityDescriptorA = (
                    advapi32.ConvertStringSecurityDescriptorToSecurityDescriptorA
                )
                ConvertStringSecurityDescriptorToSecurityDescriptorA.restype = BOOL

                # _Success_(return != FALSE)
                # BOOL
                # WINAPI
                # ConvertStringSecurityDescriptorToSecurityDescriptorW(
                # _In_ LPCWSTR StringSecurityDescriptor,
                # _In_ DWORD StringSDRevision,
                # _Outptr_ PSECURITY_DESCRIPTOR* SecurityDescriptor,
                # _Out_opt_ PULONG SecurityDescriptorSize
                # );
                ConvertStringSecurityDescriptorToSecurityDescriptorW = (
                    advapi32.ConvertStringSecurityDescriptorToSecurityDescriptorW
                )
                ConvertStringSecurityDescriptorToSecurityDescriptorW.restype = BOOL

                if defined(UNICODE):
                    ConvertStringSecurityDescriptorToSecurityDescriptor = (
                        ConvertStringSecurityDescriptorToSecurityDescriptorW
                    )
                else:
                    ConvertStringSecurityDescriptorToSecurityDescriptor = (
                        ConvertStringSecurityDescriptorToSecurityDescriptorA
                    )
                # END IF   not UNICODE

                # _Success_(return != FALSE)
                # BOOL
                # WINAPI
                # ConvertSecurityDescriptorToStringSecurityDescriptorA(
                # _In_  PSECURITY_DESCRIPTOR  SecurityDescriptor,
                # _In_  DWORD RequestedStringSDRevision,
                # _In_  SECURITY_INFORMATION SecurityInformation,
                # _Outptr_ LPSTR  *StringSecurityDescriptor,
                # _Out_opt_ PULONG StringSecurityDescriptorLen
                # );
                ConvertSecurityDescriptorToStringSecurityDescriptorA = (
                    advapi32.ConvertSecurityDescriptorToStringSecurityDescriptorA
                )
                ConvertSecurityDescriptorToStringSecurityDescriptorA.restype = BOOL

                # _Success_(return != FALSE)
                # BOOL
                # WINAPI
                # ConvertSecurityDescriptorToStringSecurityDescriptorW(
                # _In_ PSECURITY_DESCRIPTOR SecurityDescriptor,
                # _In_ DWORD RequestedStringSDRevision,
                # _In_ SECURITY_INFORMATION SecurityInformation,
                # _Outptr_ LPWSTR* StringSecurityDescriptor,
                # _Out_opt_ PULONG StringSecurityDescriptorLen
                # );
                ConvertSecurityDescriptorToStringSecurityDescriptorW = (
                    advapi32.ConvertSecurityDescriptorToStringSecurityDescriptorW
                )
                ConvertSecurityDescriptorToStringSecurityDescriptorW.restype = BOOL

                if defined(UNICODE):
                    ConvertSecurityDescriptorToStringSecurityDescriptor = (
                        ConvertSecurityDescriptorToStringSecurityDescriptorW
                    )
                else:
                    ConvertSecurityDescriptorToStringSecurityDescriptor = (
                        ConvertSecurityDescriptorToStringSecurityDescriptorA
                    )
                # END IF   not UNICODE

            # END IF  _WIN32_WINNT >=  0x0500
        # END IF  not defined(_NTDDK_)
    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if defined(__cplusplus):
        pass
    # END IF
# END IF   endif __SDDL_H__
