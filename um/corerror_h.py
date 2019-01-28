import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__COMMON_LANGUAGE_RUNTIME_HRESULTS__ = None
FACILITY_URT = None
EMAKEHR = None

# == + + ==
# Copyright (c) Microsoft Corporation. All rights reserved.
# == -- ==
# ******************************************************************* *
# ** * CorError.h - lists the HResults used by the .NET Framework's ** *
# Common Language Runtime. ** * Created: September 3, 1999. ** * **
# ******************************************************************
if not defined(__COMMON_LANGUAGE_RUNTIME_HRESULTS__):
    __COMMON_LANGUAGE_RUNTIME_HRESULTS__ = VOID

    # *******************************************************************
    # These HRESULTs are used for mapping managed exceptions to COM error
    # codes and vice versa through COM Interop. For background on COM error
    # codes see
    # http://msdn.microsoft.com/library/default.asp?url=/library/en-us/com/error_9td2.asp.
    # FACILITY_URT is defined as 0x13 (0x8013xxxx). The facility range is
    # reserved for the .NET Framework SDK teams. Within that range, the
    # following subranges have been allocated for different
    # feature areas: 0x10yy for Execution Engine 0x11yy for Metadata,
    # TypeLib Export, and CLDB 0x12yy for MetaData Validator 0x13yy for
    #  Debugger and Profiler errors 0x14yy for Security 0x15yy for BCL
    # 0x1600 - 0x161F for Reflection
    # 0x1620 - 0x163F for System.IO
    # 0x1640 - 0x165F for Security
    # 0x1660 - 0x16FF for BCL
    # 0x17yy for shim 0x18yy for IL Verifier
    # 0x19yy for .NET Framework
    # 0x1Ayy for .NET Framework
    # 0x1Byy for MetaData Validator
    # 0x1Cyy for more debugger errors
    # 0x1Dyy for PE Format Validation
    # 0x1Eyy for CLR Optimization Service errors
    # 0x1Fyy for NGEN errors
    # 0x30yy for VSA errors
    #
    # Base class library HRESULTs are copied from this file into many
    # different files named __HResults.cs under the BCL directory.
    # Frameworks HRESULTs are defined in src/main/HResults.cs.
    # If you make any modifications to the range allocations described above,
    # please make sure the corerror.h file gets updated.
    # ******************************************************************

    from pyWinAPI.shared.winerror_h import * # NOQA
    if not defined(FACILITY_URT):
        FACILITY_URT = 0x13
    # END IF

    if not defined(EMAKEHR):
        def SMAKEHR(val):
            return MAKE_HRESULT(SEVERITY_SUCCESS, FACILITY_URT, val)


        def EMAKEHR(val):
            return MAKE_HRESULT(SEVERITY_ERROR, FACILITY_URT, val)
    # END IF


    # ******************
    # FACILITY_UTF
    # ******************
    # ******************
    # Metadata errors
    # ******************
    # *** ICeeFileGen errors.
    CEE_E_ENTRYPOINT = EMAKEHR(0x1000)    # The entry point info is invalid.
    CEE_E_CVTRES_NOT_FOUND = EMAKEHR(0x1001)    # cannot find cvtres.exe

    # *** EE errors
    MSEE_E_LOADLIBFAILED = EMAKEHR(0x1010)    # Failed to delay load library %s (Win32 error: %d).
    MSEE_E_GETPROCFAILED = EMAKEHR(0x1011)    # Failed to get entry point %s (Win32 error: %d).
    MSEE_E_MULTCOPIESLOADED = EMAKEHR(0x1012)    # Multiple copies of MSCOREE.dll have been loaded by the same process.

    # the following two are COR to match the name used in the library
    COR_E_APPDOMAINUNLOADED = EMAKEHR(0x1014)    # access unloaded appdomain
    COR_E_CANNOTUNLOADAPPDOMAIN = EMAKEHR(0x1015)    # Error while unloading an appdomain
    MSEE_E_ASSEMBLYLOADINPROGRESS = EMAKEHR(0x1016)    # Assembly is being currently being loaded
    MSEE_E_CANNOTCREATEAPPDOMAIN = EMAKEHR(0x1017)    # Attempt to create appdomain failed

    # Attempt to load an unverifiable exe with fixups
    # (IAT with more than 2 sections or a TLS section)
    COR_E_FIXUPSINEXE = EMAKEHR(0x1019)

    # Attempt to LoadLibrary a managed image in an improper way
    # (only assemblies with EAT's area allowed.)
    COR_E_NO_LOADLIBRARY_ALLOWED = EMAKEHR(0x101A)

    # The assembly is built by a runtime newer than the currently loaded
    # runtime, and cannot be loaded.
    COR_E_NEWER_RUNTIME = EMAKEHR(0x101B)

    # Unable to set app domain security policy after non-GAC domain neutral
    # assemblies are loaded
    COR_E_CANNOT_SET_POLICY = EMAKEHR(0x101C)

    # Unable to use assembly evidence after non-GAC domain neutral assemblies
    # are loaded
    COR_E_CANNOT_SPECIFY_EVIDENCE = EMAKEHR(0x101D)

    # The CLR hosting support reserves 0x1020-0x102F.
    HOST_E_DEADLOCK = EMAKEHR(0x1020)    # Host detects deadlock on a blocking operation
    HOST_E_INTERRUPTED = EMAKEHR(0x1021)    # Host interrupts a wait, similar to APC
    HOST_E_INVALIDOPERATION = EMAKEHR(0x1022)    # The operation is invalid
    HOST_E_CLRNOTAVAILABLE = EMAKEHR(0x1023)    # CLR has been disabled due to unrecoverable error
    HOST_E_TIMEOUT = EMAKEHR(0x1024)    # A wait times out
    HOST_E_NOT_OWNER = EMAKEHR(0x1025)
    HOST_E_ABANDONED = EMAKEHR(0x1026)    # An event is abandoned
    HOST_E_EXITPROCESS_THREADABORT = EMAKEHR(0x1027)    # ExitProcess due to ThreadAbort escalation
    HOST_E_EXITPROCESS_ADUNLOAD = EMAKEHR(0x1028)    # ExitProcess due to AD Unload escalation
    HOST_E_EXITPROCESS_TIMEOUT = EMAKEHR(0x1029)    # ExitProcess due to Timeout escalation
    HOST_E_EXITPROCESS_OUTOFMEMORY = EMAKEHR(0x102A)    # ExitProcess due to OutOfMemory escalation
    HOST_E_EXITPROCESS_STACKOVERFLOW = EMAKEHR(0x102B)    # ExitProcess due to StackOverflow escalation

    # *** Assembly Cache errors
    COR_E_MODULE_HASH_CHECK_FAILED = EMAKEHR(0x1039)    # The check of the module's hash failed.

    # The located assembly's manifest definition does not match the assembly
    # reference.
    FUSION_E_REF_DEF_MISMATCH = EMAKEHR(0x1040)
    FUSION_E_INVALID_PRIVATE_ASM_LOCATION = EMAKEHR(0x1041)    # The private assembly was located outside the appbase directory.
    FUSION_E_ASM_MODULE_MISSING = EMAKEHR(0x1042)    # A module specified in the manifest was not found.
    FUSION_E_UNEXPECTED_MODULE_FOUND = EMAKEHR(0x1043)    # Modules which are not in the manifest were streamed in.
    FUSION_E_PRIVATE_ASM_DISALLOWED = EMAKEHR(0x1044)    # A strongly-named assembly is required.
    FUSION_E_SIGNATURE_CHECK_FAILED = EMAKEHR(0x1045)    # The check of the signature failed.
    FUSION_E_DATABASE_ERROR = EMAKEHR(0x1046)    # An unexpected error was encountered in the Assembly Cache database.
    FUSION_E_INVALID_NAME = EMAKEHR(0x1047)    # The given assembly name or codebase was invalid.
    FUSION_E_CODE_DOWNLOAD_DISABLED = EMAKEHR(0x1048)    # HTTP download of assemblies has been disabled for this appdomain.
    FUSION_E_UNINSTALL_DISALLOWED = EMAKEHR(0x1049)    # Uninstall of given assembly is not allowed.
    FUSION_E_HOST_GAC_ASM_MISMATCH = EMAKEHR(0x1050)    # Assembly in host store has a different signature than assembly in GAC
    FUSION_E_LOADFROM_BLOCKED = EMAKEHR(0x1051)    # Hosted environment doesn't permit loading by location
    FUSION_E_CACHEFILE_FAILED = EMAKEHR(0x1052)    # Failed to add file to AppDomain cache

    # == == == == == == == == == == == == == == == == == == == == == == == ==
    # == == == == == == == == == == == == == == =
    # THE VALIDATOR IS CURRENTLY USING ERROR CODES STARTING WITH 0x1050
    # ONWARDS.
    # LOOK AT ERROR CODES STARTING FROM VLDTR_E_AS_NAMENULL. JUST A NOTE IN
    # CASE
    # THE EE EVER COMES TO THE POINT OF NEEDING THOSEnot not not
    # == == == == == == == == == == == == == == == == == == == == == == == ==
    # == == == == == == == == == == == == == == =
    # *** Generic errors.
    CLDB_E_FILE_BADREAD = EMAKEHR(0x1100)    # Error occured during a read.
    CLDB_E_FILE_BADWRITE = EMAKEHR(0x1101)    # Error occured during a write.
    CLDB_E_FILE_READONLY = EMAKEHR(0x1103)    # File is read only.
    CLDB_E_NAME_ERROR = EMAKEHR(0x1105)    # An ill-formed name was given.
    CLDB_S_TRUNCATION = SMAKEHR(0x1106)    # STATUS: Data value was truncated.
    CLDB_E_TRUNCATION = EMAKEHR(0x1106)    # ERROR: Data value was truncated.
    CLDB_E_FILE_OLDVER = EMAKEHR(0x1107)    # Old version error.
    CLDB_E_RELOCATED = EMAKEHR(0x1108)    # A shared mem open failed to open at the originally

    # assigned memory address.
    CLDB_S_NULL = SMAKEHR(0x1109)    # NULL data value.

    # Create of shared memory failed. A memory mapping of the same name
    # already exists.
    CLDB_E_SMDUPLICATE = EMAKEHR(0x110A)
    CLDB_E_NO_DATA = EMAKEHR(0x110B)    # There isn't .CLB data in the memory or stream.
    CLDB_E_READONLY = EMAKEHR(0x110C)    # Database is read only.
    CLDB_E_INCOMPATIBLE = EMAKEHR(0x110D)    # The importing scope is not comptabile with the emitting scope

    # *** Schema errors.
    CLDB_E_FILE_CORRUPT = EMAKEHR(0x110E)    # File is corrupt.
    CLDB_E_SCHEMA_VERNOTFOUND = EMAKEHR(0x110F)    # Version %d of schema '%s' not found.
    CLDB_E_BADUPDATEMODE = EMAKEHR(0x1110)    # cannot open a incrementally build scope for full update

    # *** Index errors.
    CLDB_E_INDEX_NONULLKEYS = EMAKEHR(0x1121)    # Null value not allowed in unique index or primary key.
    CLDB_E_INDEX_DUPLICATE = EMAKEHR(0x1122)    # Unique index %s has been violated.
    CLDB_E_INDEX_BADTYPE = EMAKEHR(0x1123)    # The columns data type is not allowed in an index.
    CLDB_E_INDEX_NOTFOUND = EMAKEHR(0x1124)    # Index %s not found.
    CLDB_S_INDEX_TABLESCANREQUIRED = SMAKEHR(0x1125)    # Table scan required to run query.

    # *** Record errors.
    CLDB_E_RECORD_NOTFOUND = EMAKEHR(0x1130)    # Record wasn't found on lookup.
    CLDB_E_RECORD_OVERFLOW = EMAKEHR(0x1131)    # Too many records were returned for criteria.
    CLDB_E_RECORD_DUPLICATE = EMAKEHR(0x1132)    # Record is a duplicate.
    CLDB_E_RECORD_PKREQUIRED = EMAKEHR(0x1133)    # Primary key value is required.
    CLDB_E_RECORD_DELETED = EMAKEHR(0x1134)    # Record is valid but deleted.
    CLDB_E_RECORD_OUTOFORDER = EMAKEHR(0x1135)    # Record is emitted out of order.

    # *** Column errors.
    CLDB_E_COLUMN_OVERFLOW = EMAKEHR(0x1140)    # Data too large.
    CLDB_E_COLUMN_READONLY = EMAKEHR(0x1141)    # Column cannot be changed.
    CLDB_E_COLUMN_SPECIALCOL = EMAKEHR(0x1142)    # Too many RID or primary key columns, 1 is max.
    CLDB_E_COLUMN_PKNONULLS = EMAKEHR(0x1143)    # Primary key column %s may not allow the null value.

    # *** Table errors.
    CLDB_E_TABLE_CANTDROP = EMAKEHR(0x1150)    # Can't auto-drop table while open.

    # *** Object errors.
    CLDB_E_OBJECT_NOTFOUND = EMAKEHR(0x1151)    # Object was not found in the database.
    CLDB_E_OBJECT_COLNOTFOUND = EMAKEHR(0x1152)    # The column was not found.

    # *** Vector errors.
    CLDB_E_VECTOR_BADINDEX = EMAKEHR(0x1153)    # The index given was invalid.

    # *** Heap errors;
    CLDB_E_TOO_BIG = EMAKEHR(0x1154)    # A blob or string was too big.

    # *** IMeta* errors.
    META_E_INVALID_TOKEN_TYPE = EMAKEHR(0x115F)    # A token of the wrong type passed to a metadata function.
    TLBX_E_INVALID_TYPEINFO = EMAKEHR(0x1160)    # Typelib import: invalid type, not converted.
    TLBX_E_INVALID_TYPEINFO_UNNAMED = EMAKEHR(0x1161)    # Typelib import: invalid type, not converted -- name unknown.
    TLBX_E_CTX_NESTED = EMAKEHR(0x1162)    # Typelib export: Format string for nested contexts.
    TLBX_E_ERROR_MESSAGE = EMAKEHR(0x1163)    # Typelib export: Error message wrapper.
    TLBX_E_CANT_SAVE = EMAKEHR(0x1164)    # Typelib export: cant "SaveAllChanges()"
    TLBX_W_LIBNOTREGISTERED = EMAKEHR(0x1165)    # Typelib export: type library is not registered.
    TLBX_E_CANTLOADLIBRARY = EMAKEHR(0x1166)    # Typelib export: type library cannot be loaded.
    TLBX_E_BAD_VT_TYPE = EMAKEHR(0x1167)    # Typelib import: invalid VT_*, not converted.
    TLBX_E_NO_MSCOREE_TLB = EMAKEHR(0x1168)    # Typelib export: can't load mscoree.tlb
    TLBX_E_BAD_MSCOREE_TLB = EMAKEHR(0x1169)    # Typelib export: can't get a required typeinfo from mscoree.tlb.
    TLBX_E_TLB_EXCEPTION = EMAKEHR(0x116A)    # Typelib import: fault reading a typelib.
    TLBX_E_MULTIPLE_LCIDS = EMAKEHR(0x116B)    # Typelib import: Multiple LCID's parameters on a method.
    TLBX_I_TYPEINFO_IMPORTED = SMAKEHR(0x116C)    # Typelib import: progress report.
    TLBX_E_AMBIGUOUS_RETURN = EMAKEHR(0x116D)    # Typelib import: duplicate or ambiguous return types.
    TLBX_E_DUPLICATE_TYPE_NAME = EMAKEHR(0x116E)    # Typelib import: duplicate name (due to user-defined name).
    TLBX_I_USEIUNKNOWN = SMAKEHR(0x116F)    # Typelib export: substituted IUnknown for type.
    TLBX_I_UNCONVERTABLE_ARGS = SMAKEHR(0x1170)    # Typelib import: signature can't be converted (eg, struct**)
    TLBX_I_UNCONVERTABLE_FIELD = SMAKEHR(0x1171)    # Typelib import: signature can't be converted (eg, struct**)
    TLBX_I_NONSEQUENTIALSTRUCT = EMAKEHR(0x1172)    # Typelib export: Can't convert non-sequential structs.
    TLBX_W_WARNING_MESSAGE = SMAKEHR(0x1173)    # Typelib export: Warning message wrapper.
    TLBX_I_RESOLVEREFFAILED = EMAKEHR(0x1174)    # Typelib import: The resolve ref call failed.
    TLBX_E_ASANY = EMAKEHR(0x1175)    # Typelib export: Encounterd "AsAny" -- ignored.
    TLBX_E_INVALIDLCIDPARAM = EMAKEHR(0x1176)    # Typelib export: Encounterd an LCID attribute set to an invalid param.
    TLBX_E_LCIDONDISPONLYITF = EMAKEHR(0x1177)    # Typelib export: Encounterd an LCID attribute on a disp only interface.
    TLBX_E_NONPUBLIC_FIELD = EMAKEHR(0x1178)    # Typelib export: Non-public field in public struct.
    TLBX_I_TYPE_EXPORTED = SMAKEHR(0x1179)    # Typelib export: type exported
    TLBX_I_DUPLICATE_DISPID = SMAKEHR(0x117A)    # Typelib export: duplicate dispid -- auto corrected.
    TLBX_E_BAD_NAMES = EMAKEHR(0x117B)    # Typelib export: bad names list.
    TLBX_I_REF_TYPE_AS_STRUCT = SMAKEHR(0x117C)    # Typelib export: referenct tyep had layout, exported as struct.
    TLBX_E_GENERICINST_SIGNATURE = EMAKEHR(0x117D)    # TypeLib export: generic type instance in signature.
    TLBX_E_GENERICPAR_SIGNATURE = EMAKEHR(0x117E)    # TypeLib export: generic type parameter in signature.
    TLBX_I_GENERIC_TYPE = SMAKEHR(0x117F)    # TypeLib export: generic type definition
    META_E_DUPLICATE = EMAKEHR(0x1180)    # Attempt to define an object that already exists.
    META_E_GUID_REQUIRED = EMAKEHR(0x1181)    # A guid was not provided where one was required.
    META_E_TYPEDEF_MISMATCH = EMAKEHR(0x1182)    # Merge: an import typedef matched ns.name, but not version and guid.
    META_E_MERGE_COLLISION = EMAKEHR(0x1183)    # Merge: conflict between import and emit

    # TypeLib import: Ignoring IDL custom attribute -- does not have an
    # integral value.
    TLBX_W_NON_INTEGRAL_CA_TYPE = SMAKEHR(0x1184)

    # TypeLib import: Ignoring IDL custom attribute -- using IEnum CA on an
    # IUnknown derived interface.
    TLBX_W_IENUM_CA_ON_IUNK = SMAKEHR(0x1185)
    TLBX_E_NO_SAFEHANDLE_ARRAYS = EMAKEHR(0x1186)    # TypeLib export: detected array of SafeHandles
    META_E_METHD_NOT_FOUND = EMAKEHR(0x1187)    # Merge: Class already in emit scope, but member not found
    META_E_FIELD_NOT_FOUND = EMAKEHR(0x1188)    # Merge: Class already in emit scope, but member not found
    META_S_PARAM_MISMATCH = SMAKEHR(0x1189)    # Merge: Parameter information mismatched.
    META_E_PARAM_MISMATCH = EMAKEHR(0x1189)    # Merge: Parameter information mismatched.
    META_E_BADMETADATA = EMAKEHR(0x118A)    # Merge: Inconsistency in meta data import scope
    META_E_INTFCEIMPL_NOT_FOUND = EMAKEHR(0x118B)    # Merge: Class already in emit scope, but interfaceimpl not found
    TLBX_E_NO_CRITICALHANDLE_ARRAYS = EMAKEHR(0x118C)    # TypeLib export: detected array of CriticalHandles
    META_E_CLASS_LAYOUT_INCONSISTENT = EMAKEHR(0x118D)    # Merge: Class is duplicated but class layout information is not consistent

    # Merge: Field is duplicated but we cannot find the matching FieldMarshal
    # information
    META_E_FIELD_MARSHAL_NOT_FOUND = EMAKEHR(0x118E)
    META_E_METHODSEM_NOT_FOUND = EMAKEHR(0x118F)    # Merge:
    META_E_EVENT_NOT_FOUND = EMAKEHR(0x1190)    # Merge: Method is duplicated but we cannot find the matching event info.
    META_E_PROP_NOT_FOUND = EMAKEHR(0x1191)    # Merge: Method is duplicated but we cannot find the maching property info.
    META_E_BAD_SIGNATURE = EMAKEHR(0x1192)    # Bad binary signature
    META_E_BAD_INPUT_PARAMETER = EMAKEHR(0x1193)    # Bad input parameters
    META_E_METHDIMPL_INCONSISTENT = EMAKEHR(0x1194)    # Merge: duplicated methods have inconsistent ImplFlags
    META_E_MD_INCONSISTENCY = EMAKEHR(0x1195)    # Merge: Inconsistency in meta data
    META_E_CANNOTRESOLVETYPEREF = EMAKEHR(0x1196)    # Cannot resolve typeref
    META_S_DUPLICATE = SMAKEHR(0x1197)    # Attempt to define an object that already exists in valid scenerios.
    META_E_STRINGSPACE_FULL = EMAKEHR(0x1198)    # No logical space left to create more user strings.
    META_E_UNEXPECTED_REMAP = EMAKEHR(0x1199)    # A TokenRemap occurred which we weren't prepared to handle.
    META_E_HAS_UNMARKALL = EMAKEHR(0x119A)    # Unmark all has been called already
    META_E_MUST_CALL_UNMARKALL = EMAKEHR(0x119B)    # Must call UnmarkAll first before marking.
    META_E_GENERICPARAM_INCONSISTENT = EMAKEHR(0x119C)    # Merge: duplicated types/methods have inconsistent GenericParams
    META_E_EVENT_COUNTS = EMAKEHR(0x119D)    # Merge: different event counts in import and emit scopes.
    META_E_PROPERTY_COUNTS = EMAKEHR(0x119E)    # Merge: different property counts in import and emit scopes.

    # Merge: An input scope has a TypeRef which should but doesn't have a
    # matching TypeDef.
    META_E_TYPEDEF_MISSING = EMAKEHR(0x119F)
    TLBX_E_CANT_LOAD_MODULE = EMAKEHR(0x11A0)    # TypeLib export: can't open the module to export.
    TLBX_E_CANT_LOAD_CLASS = EMAKEHR(0x11A1)    # TypeLib export: can't load a class.
    TLBX_E_NULL_MODULE = EMAKEHR(0x11A2)    # TypeLib export: the hMod of a loaded class is 0; can't export it.
    TLBX_E_NO_CLSID_KEY = EMAKEHR(0x11A3)    # TypeLib export: no CLSID or Interface subkey to HKCR.
    TLBX_E_CIRCULAR_EXPORT = EMAKEHR(0x11A4)    # TypeLib export: attempt to export a CLB imported from a TLB.
    TLBX_E_CIRCULAR_EXPORT2 = EMAKEHR(0x1B52)    # TypeLib export: attempt to export a CLB imported from a TLB.
    TLBX_E_CIRCULAR_IMPORT = EMAKEHR(0x11A5)    # TypeLib import: attempt to import a TLB exported from a CLB.
    TLBX_E_BAD_NATIVETYPE = EMAKEHR(0x11A6)    # TypeLib export: bad Native type in method signature.
    TLBX_E_BAD_VTABLE = EMAKEHR(0x11A7)    # TypeLib import: non-increasing vtable (duplicate slots).
    TLBX_E_CRM_NON_STATIC = EMAKEHR(0x11A8)    # TypeLib export: the COM register method is non static.

    # TypeLib export: the specified COM register method does not have the
    # correct signature.
    TLBX_E_CRM_INVALID_SIG = EMAKEHR(0x11A9)
    TLBX_E_CLASS_LOAD_EXCEPTION = EMAKEHR(0x11AA)    # TypeLib export: can't load, have the class load exception.
    TLBX_E_UNKNOWN_SIGNATURE = EMAKEHR(0x11AB)    # TypeLib export: unknown element in signature.
    TLBX_E_REFERENCED_TYPELIB = EMAKEHR(0x11AC)    # TypeLib import: reference to an external typelib.
    TLBX_S_REFERENCED_TYPELIB = SMAKEHR(0x11AC)    # TypeLib import: reference to an external typelib.
    TLBX_E_INVALID_NAMESPACE = EMAKEHR(0x11AD)    # TypeLib import: an imported typelib has an invalid namespace name.
    TLBX_E_LAYOUT_ERROR = EMAKEHR(0x11AE)    # Typelib export: an error on Layout()
    TLBX_E_NOTIUNKNOWN = EMAKEHR(0x11AF)    # Typelib import: Interface not derived from IUnknown.
    TLBX_E_NONVISIBLEVALUECLASS = EMAKEHR(0x11B0)    # Typelib export: Non COM visible value type in method signature.

    # Typelib export: Types which contain the native type NATIVE_TYPE_LPTSTR
    # are not allowed to be exported to COM.
    TLBX_E_LPTSTR_NOT_ALLOWED = EMAKEHR(0x11B1)

    # Typelib export: Types with a CHAR set of auto are not allowed to be
    # exported to COM.
    TLBX_E_AUTO_CS_NOT_ALLOWED = EMAKEHR(0x11B2)

    # Typelib export: Found an interface marked as IID_IDispatch or
    # IID_IUnknown.
    TLBX_S_NOSTDINTERFACE = SMAKEHR(0x11B3)
    TLBX_S_DUPLICATE_DISPID = SMAKEHR(0x11B4)    # Typelib export: duplicate dispid found; ignored.
    TLBX_E_ENUM_VALUE_INVALID = EMAKEHR(0x11B5)    # Typelib export: The enum value is not legal for a typelib.
    TLBX_E_DUPLICATE_IID = EMAKEHR(0x11B6)    # Typelib export: Duplicate IID
    TLBX_E_NO_NESTED_ARRAYS = EMAKEHR(0x11B7)    # Tyeplib export: detected nested arrays.
    TLBX_E_PARAM_ERROR_NAMED = EMAKEHR(0x11B8)    # Typelib import: param type couldn't be converted.
    TLBX_E_PARAM_ERROR_UNNAMED = EMAKEHR(0x11B9)    # Typelib import: param type couldn't be converted -- param name unknown.
    TLBX_E_AGNOST_SIGNATURE = EMAKEHR(0x11BA)    # TypeLib export: size agnostic element in signature.
    TLBX_E_CONVERT_FAIL = EMAKEHR(0x11BB)    # TypeLib export: exporter failed.
    TLBX_W_DUAL_NOT_DISPATCH = EMAKEHR(0x11BC)    # Typelib import: [dual] interface not derived from IDispatch.

    # Typelib export: unconvertable signature
    # (use specific error for reportingnot )
    TLBX_E_BAD_SIGNATURE = EMAKEHR(0x11BD)
    TLBX_E_ARRAY_NEEDS_NT_FIXED = EMAKEHR(0x11BE)    # Typelib export: non-fixed/non-safearray array in struct
    TLBX_E_CLASS_NEEDS_NT_INTF = EMAKEHR(0x11BF)    # Typelib export: non-interface class in struct
    META_E_CA_INVALID_TARGET = EMAKEHR(0x11C0)    # Known custom attribute on invalid target.
    META_E_CA_INVALID_VALUE = EMAKEHR(0x11C1)    # Known custom attribute had invalid value.
    META_E_CA_INVALID_BLOB = EMAKEHR(0x11C2)    # Known custom attribute blob is bad format.
    META_E_CA_REPEATED_ARG = EMAKEHR(0x11C3)    # Known custom attribute blob has repeated named argument.
    META_E_CA_UNKNOWN_ARGUMENT = EMAKEHR(0x11C4)    # Known custom attrubte named arg not recognized.
    META_E_CA_VARIANT_NYI = EMAKEHR(0x11C5)    # Known attribute named argument doesn't support variant.
    META_E_CA_ARRAY_NYI = EMAKEHR(0x11C6)    # Known attribute named argument doesn't support array.
    META_E_CA_UNEXPECTED_TYPE = EMAKEHR(0x11C7)    # Known attribute parser found unexpected type.
    META_E_CA_INVALID_ARGTYPE = EMAKEHR(0x11C8)    # Known attribute parser only handles fields -- no properties.

    # Known attribute parser found an argument that is invalid for the object
    # it is applied to.
    META_E_CA_INVALID_ARG_FOR_TYPE = EMAKEHR(0x11C9)
    META_E_CA_INVALID_UUID = EMAKEHR(0x11CA)    # The format of the UUID was invalid.

    # The MarshalAs attribute has fields set that are not valid for the
    # specified unmanaged type.
    META_E_CA_INVALID_MARSHALAS_FIELDS = EMAKEHR(0x11CB)
    META_E_CA_NT_FIELDONLY = EMAKEHR(0x11CC)    # The specified unmanaged type is only valid on fields.
    META_E_CA_NEGATIVE_PARAMINDEX = EMAKEHR(0x11CD)    # The parameter index cannot be negative.
    META_E_CA_NEGATIVE_MULTIPLIER = EMAKEHR(0x11CE)    # The multiplier cannot be negative.
    META_E_CA_NEGATIVE_CONSTSIZE = EMAKEHR(0x11CF)    # The constant size cannot be negative.
    META_E_CA_FIXEDSTR_SIZE_REQUIRED = EMAKEHR(0x11D0)    # A fixed string requires a size.
    META_E_CA_CUSTMARSH_TYPE_REQUIRED = EMAKEHR(0x11D1)    # A custom marshaler requires the custom marshaler type.
    META_E_CA_FILENAME_REQUIRED = EMAKEHR(0x11D2)    # A DllImport attribute requires a filename.
    TLBX_W_NO_PROPS_IN_EVENTS = EMAKEHR(0x11D3)    # TypeLib import: Detected properties in a source dispinterface.
    META_E_NOT_IN_ENC_MODE = EMAKEHR(0x11D4)    # SaveDelta was called without being in EnC mode
    TLBX_W_ENUM_VALUE_TOOBIG = SMAKEHR(0x11D5)    # Typelib export: The enum value is not legal for a typelib.
    META_E_METHOD_COUNTS = EMAKEHR(0x11D6)    # Merge: different method counts in import and emit scopes.
    META_E_FIELD_COUNTS = EMAKEHR(0x11D7)    # Merge: different field counts in import and emit scopes.
    META_E_PARAM_COUNTS = EMAKEHR(0x11D8)    # Merge: different param counts in import and emit scopes.
    TLBX_W_EXPORTING_AUTO_LAYOUT = SMAKEHR(0x11D9)    # TypeLib export: Exporting an auto-layout type.
    TLBX_E_TYPED_REF = EMAKEHR(0x11DA)    # TypeLib export: Exporting a TypedReference.
    TLBX_W_DEFAULT_INTF_NOT_VISIBLE = SMAKEHR(0x11DB)    # TypeLib export: ComDefaultInterface is not COMVisible.
    TLBX_W_BAD_SAFEARRAYFIELD_NO_ELEMENTVT = SMAKEHR(0x11DE)    # TypeLib export: System.Array SAFEARRAY field without a SafeArraySubType.

    # TypeLib export: Class with layout parameter of field marked with
    # UnmanagedType.Interface
    TLBX_W_LAYOUTCLASS_AS_INTERFACE = SMAKEHR(0x11DF)
    TLBX_I_GENERIC_BASE_TYPE = SMAKEHR(0x11E0)    # TypeLib export: type deriving from a generic type.

    # TypeLib export: bitness of assembly doesn't match bitness of output type
    # library
    TLBX_E_BITNESS_MISMATCH = EMAKEHR(0x11E1)
    TLBX_E_EVENT_WITH_NEWENUM = EMAKEHR(0x11E2)    # TypeLib import: source interface with NewEnum member.
    TLBX_E_PROPGET_WITHOUT_RETURN = EMAKEHR(0x11E3)    # TypeLib import: propget without return type
    META_E_MISMATCHED_VISIBLITY = EMAKEHR(0x11E4)    # Merge - Match found for type/method/etc but differs in visiblity

    # InternalsVisibileTo can't have a version, culture, or processor
    # architecture
    META_E_CA_BAD_FRIENDS_ARGS = EMAKEHR(0x11E5)

    # Strong-name INT assemblies can only grant friend access to strong
    # name-signed assemblies
    META_E_CA_FRIENDS_SN_REQUIRED = EMAKEHR(0x11E6)

    # Return values from validator functions.
    VLDTR_S_WRN = SMAKEHR(0x1200)    # Warnings found in the validator.
    VLDTR_S_ERR = SMAKEHR(0x1201)    # Errors found in the validator.
    VLDTR_S_WRNERR = SMAKEHR(0x1202)    # Warnings and errors found in the validator.

    # Validator structural errors.
    VLDTR_E_RID_OUTOFRANGE = EMAKEHR(0x1203)    # Rid is out of range.
    VLDTR_E_CDTKN_OUTOFRANGE = EMAKEHR(0x1204)    # Coded token type is out of range.
    VLDTR_E_CDRID_OUTOFRANGE = EMAKEHR(0x1205)    # Coded rid is out of range.
    VLDTR_E_STRING_INVALID = EMAKEHR(0x1206)    # String offset is invalid.
    VLDTR_E_GUID_INVALID = EMAKEHR(0x1207)    # GUID offset is invalid.
    VLDTR_E_BLOB_INVALID = EMAKEHR(0x1208)    # Blob offset if invalid.

    # Validator semantic errors.
    VLDTR_E_MOD_MULTI = EMAKEHR(0x1209)    # Multiple module records found.
    VLDTR_E_MOD_NULLMVID = EMAKEHR(0x120A)    # Module has null MVID.
    VLDTR_E_TR_NAMENULL = EMAKEHR(0x120B)    # TypeRef name is NULL.
    VLDTR_E_TR_DUP = EMAKEHR(0x120C)    # TypeRef has a dup.
    VLDTR_E_TD_NAMENULL = EMAKEHR(0x120D)    # TypeDef name is NULL.
    VLDTR_E_TD_DUPNAME = EMAKEHR(0x120E)    # TypeDef has a dup based on name + namespace.
    VLDTR_E_TD_DUPGUID = EMAKEHR(0x120F)    # TypeDef has a dup based on GUID.
    VLDTR_E_TD_NOTIFACEOBJEXTNULL = EMAKEHR(0x1210)    # TypeDef that's not an Interface and not System.Object extends nil parent.
    VLDTR_E_TD_OBJEXTENDSNONNULL = EMAKEHR(0x1211)    # System.Object extends a non-nil parent.
    VLDTR_E_TD_EXTENDSSEALED = EMAKEHR(0x1212)    # TypeDef extends sealed class.
    VLDTR_E_TD_DLTNORTSPCL = EMAKEHR(0x1213)    # TypeDef is Deleted but not marked with RTSpecialName.
    VLDTR_E_TD_RTSPCLNOTDLT = EMAKEHR(0x1214)    # TypeDef is marked RTSpecialName, but is not a Deleted record.
    VLDTR_E_MI_DECLPRIV = EMAKEHR(0x1215)    # MethodImpl's Decl is private
    VLDTR_E_AS_BADNAME = EMAKEHR(0x1216)    # Assembly [Ref] name has path and/or extension.
    VLDTR_E_FILE_SYSNAME = EMAKEHR(0x1217)    # File has a system name (con, com, aux, etc.).
    VLDTR_E_MI_BODYSTATIC = EMAKEHR(0x1218)    # MethodImpl's body is static.
    VLDTR_E_TD_IFACENOTABS = EMAKEHR(0x1219)    # TypeDef is marked Interface but not Abstract.
    VLDTR_E_TD_IFACEPARNOTNIL = EMAKEHR(0x121A)    # TypeDef is marked Interface but parent is not Nil.
    VLDTR_E_TD_IFACEGUIDNULL = EMAKEHR(0x121B)    # TypeDef is marked Interface but GUID is NULL.
    VLDTR_E_MI_DECLFINAL = EMAKEHR(0x121C)    # TMethodImpl's Decl is final.
    VLDTR_E_TD_VTNOTSEAL = EMAKEHR(0x121D)    # TypeDef is marked ValueType but not marked Sealed.
    VLDTR_E_PD_BADFLAGS = EMAKEHR(0x121E)    # Param has extra bits in flags.
    VLDTR_E_IFACE_DUP = EMAKEHR(0x121F)    # InterfaceImpl has a dup.
    VLDTR_E_MR_NAMENULL = EMAKEHR(0x1220)    # MemberRef name is NULL.
    VLDTR_E_MR_VTBLNAME = EMAKEHR(0x1221)    # MemberRef has an invalid name, _VtblGap*.
    VLDTR_E_MR_DELNAME = EMAKEHR(0x1222)    # MemberRef has an invalid name, _Deleted*.
    VLDTR_E_MR_PARNIL = EMAKEHR(0x1223)    # MemberRef parent Nil in a PE file.
    VLDTR_E_MR_BADCALLINGCONV = EMAKEHR(0x1224)    # MemberRef has invalid calling convention.
    VLDTR_E_MR_NOTVARARG = EMAKEHR(0x1225)    # MemberRef has Method parent but calling convention is not VARARG.
    VLDTR_E_MR_NAMEDIFF = EMAKEHR(0x1226)    # MemberRef name different from parent MethodDef.
    VLDTR_E_MR_SIGDIFF = EMAKEHR(0x1227)    # MemberRef signature different from parent MethodDef.
    VLDTR_E_MR_DUP = EMAKEHR(0x1228)    # MemberRef has a dup.
    VLDTR_E_CL_TDAUTO = EMAKEHR(0x1229)    # ClassLayout parent TypeDef is marked AutoLayout.
    VLDTR_E_CL_BADPCKSZ = EMAKEHR(0x122A)    # ClassLayout has bad PackingSize.
    VLDTR_E_CL_DUP = EMAKEHR(0x122B)    # ClassLayout has dup.
    VLDTR_E_FL_BADOFFSET = EMAKEHR(0x122C)    # FieldLayout2 has bad offset.
    VLDTR_E_FL_TDNIL = EMAKEHR(0x122D)    # FieldLayout2 has field with nil parent.
    VLDTR_E_FL_NOCL = EMAKEHR(0x122E)    # FieldLayout2 has no ClassLayout record.
    VLDTR_E_FL_TDNOTEXPLCT = EMAKEHR(0x122F)    # FieldLayout2 parent TypeDef is not marked with ExplicitLayout.
    VLDTR_E_FL_FLDSTATIC = EMAKEHR(0x1230)    # FieldLayout2 has field marked Static.
    VLDTR_E_FL_DUP = EMAKEHR(0x1231)    # FieldLayout2 has a dup.
    VLDTR_E_MODREF_NAMENULL = EMAKEHR(0x1232)    # ModuleRef name is NULL.
    VLDTR_E_MODREF_DUP = EMAKEHR(0x1233)    # ModuleRef has a dup.
    VLDTR_E_TR_BADSCOPE = EMAKEHR(0x1234)    # TypeRef has a bad resolution scope.
    VLDTR_E_TD_NESTEDNOENCL = EMAKEHR(0x1235)    # TypeDef marked nested has no encloser.
    VLDTR_E_TD_EXTTRRES = EMAKEHR(0x1236)    # TypeDef extends a TypeRef which resolves to a TypeDef in the same module.
    VLDTR_E_SIGNULL = EMAKEHR(0x1237)    # Signature specified is zero-sized.
    VLDTR_E_SIGNODATA = EMAKEHR(0x1238)    # Signature does not have enough data at specified byte.
    VLDTR_E_MD_BADCALLINGCONV = EMAKEHR(0x1239)    # Method signature has invalid calling convention.

    # Method is marked static but has HASTHIS/EXPLICITTHIS set on the calling
    # convention.
    VLDTR_E_MD_THISSTATIC = EMAKEHR(0x123A)
    VLDTR_E_MD_NOTTHISNOTSTATIC = EMAKEHR(0x123B)    # Method is not marked static but is not HASTHIS/EXPLICITTHIS.
    VLDTR_E_MD_NOARGCNT = EMAKEHR(0x123C)    # Method signature is missing the argument count.
    VLDTR_E_SIG_MISSELTYPE = EMAKEHR(0x123D)    # Signature missing element type.
    VLDTR_E_SIG_MISSTKN = EMAKEHR(0x123E)    # Signature missing token.
    VLDTR_E_SIG_TKNBAD = EMAKEHR(0x123F)    # Signature has bad token.
    VLDTR_E_SIG_MISSFPTR = EMAKEHR(0x1240)    # Signature is missing function pointer.
    VLDTR_E_SIG_MISSFPTRARGCNT = EMAKEHR(0x1241)    # Signature has function pointer missing argument count.
    VLDTR_E_SIG_MISSRANK = EMAKEHR(0x1242)    # Signature is missing rank specification.
    VLDTR_E_SIG_MISSNSIZE = EMAKEHR(0x1243)    # Signature is missing count of sized dimensions.
    VLDTR_E_SIG_MISSSIZE = EMAKEHR(0x1244)    # Signature is missing size of dimension.
    VLDTR_E_SIG_MISSNLBND = EMAKEHR(0x1245)    # Signature is missing count of lower bounds.
    VLDTR_E_SIG_MISSLBND = EMAKEHR(0x1246)    # Signature is missing a lower bound.
    VLDTR_E_SIG_BADELTYPE = EMAKEHR(0x1247)    # Signature has bad element type.
    VLDTR_E_SIG_MISSVASIZE = EMAKEHR(0x1248)    # Signature has value array missing size.
    VLDTR_E_FD_BADCALLINGCONV = EMAKEHR(0x1249)    # Field signature has invalid calling convention.
    VLDTR_E_MD_NAMENULL = EMAKEHR(0x124A)    # Method name is NULL.
    VLDTR_E_MD_PARNIL = EMAKEHR(0x124B)    # Method has parent NIL.
    VLDTR_E_MD_DUP = EMAKEHR(0x124C)    # Method has dup.
    VLDTR_E_FD_NAMENULL = EMAKEHR(0x124D)    # Field name is NULL.
    VLDTR_E_FD_PARNIL = EMAKEHR(0x124E)    # Field parent is Nil.
    VLDTR_E_FD_DUP = EMAKEHR(0x124F)    # Field has dup.
    VLDTR_E_AS_MULTI = EMAKEHR(0x1250)    # Multiple Assembly records found.
    VLDTR_E_AS_NAMENULL = EMAKEHR(0x1251)    # Assembly name is NULL.
    VLDTR_E_SIG_TOKTYPEMISMATCH = EMAKEHR(0x1252)    # E_T_VALUETYPE<class token> or E_T_CLASS<vtype token>.
    VLDTR_E_CL_TDINTF = EMAKEHR(0x1253)    # Class layout on an Interface.
    VLDTR_E_ASOS_OSPLTFRMIDINVAL = EMAKEHR(0x1254)    # AssemblyOS platform ID invalid.
    VLDTR_E_AR_NAMENULL = EMAKEHR(0x1255)    # AssemblyRef name is NULL.
    VLDTR_E_TD_ENCLNOTNESTED = EMAKEHR(0x1256)    # TypeDef not nested has encloser.
    VLDTR_E_AROS_OSPLTFRMIDINVAL = EMAKEHR(0x1257)    # AssemblyRefOS has invalid platform ID.
    VLDTR_E_FILE_NAMENULL = EMAKEHR(0x1258)    # File name is NULL.
    VLDTR_E_CT_NAMENULL = EMAKEHR(0x1259)    # ExportedType name is NULL.
    VLDTR_E_TD_EXTENDSCHILD = EMAKEHR(0x125A)    # TypeDef extends its own child.
    VLDTR_E_MAR_NAMENULL = EMAKEHR(0x125B)    # ManifestResource name is NULL.
    VLDTR_E_FILE_DUP = EMAKEHR(0x125C)    # File has dup.
    VLDTR_E_FILE_NAMEFULLQLFD = EMAKEHR(0x125D)    # File name is fully qualified.
    VLDTR_E_CT_DUP = EMAKEHR(0x125E)    # ExportedType has dup.
    VLDTR_E_MAR_DUP = EMAKEHR(0x125F)    # ManifestResource has dup.
    VLDTR_E_MAR_NOTPUBPRIV = EMAKEHR(0x1260)    # ManifestResource is neither Public not Private.
    VLDTR_E_TD_ENUMNOVALUE = EMAKEHR(0x1261)    # Enum has no "value__" field.
    VLDTR_E_TD_ENUMVALSTATIC = EMAKEHR(0x1262)    # Enum's "value__" field is static.
    VLDTR_E_TD_ENUMVALNOTSN = EMAKEHR(0x1263)    # Enum's "value__" field is not SpecialName.
    VLDTR_E_TD_ENUMFLDNOTST = EMAKEHR(0x1264)    # Enum's field is not static.
    VLDTR_E_TD_ENUMFLDNOTLIT = EMAKEHR(0x1265)    # Enum's field is not literal.
    VLDTR_E_TD_ENUMNOLITFLDS = EMAKEHR(0x1266)    # Enum has no literal fields.
    VLDTR_E_TD_ENUMFLDSIGMISMATCH = EMAKEHR(0x1267)    # Enum's field sig does not match value__ sig.
    VLDTR_E_TD_ENUMVALNOT1ST = EMAKEHR(0x1268)    # Enum's "value__" field is not first.
    VLDTR_E_FD_NOTVALUERTSN = EMAKEHR(0x1269)    # Field is RTSpecialName but name is not "value__".
    VLDTR_E_FD_VALUEPARNOTENUM = EMAKEHR(0x126A)    # Field "value__" in not Enum class.
    VLDTR_E_FD_INSTINIFACE = EMAKEHR(0x126B)    # Instance field in interface.
    VLDTR_E_FD_NOTPUBINIFACE = EMAKEHR(0x126C)    # Non-public field in interface.
    VLDTR_E_FMD_GLOBALNOTPUBPRIVSC = EMAKEHR(0x126D)    # Global field/method neither Public nor PrivateScope.
    VLDTR_E_FMD_GLOBALNOTSTATIC = EMAKEHR(0x126E)    # Global field/method not static.
    VLDTR_E_FD_GLOBALNORVA = EMAKEHR(0x126F)    # Global field has no RVA.
    VLDTR_E_MD_CTORZERORVA = EMAKEHR(0x1270)    # .ctor,.cctor has zero RVA.
    VLDTR_E_FD_MARKEDNOMARSHAL = EMAKEHR(0x1271)    # Field is marked marshaled but has no marshaling rec.
    VLDTR_E_FD_MARSHALNOTMARKED = EMAKEHR(0x1272)    # Field has marshaling rec but is not marked marshaled.
    VLDTR_E_FD_MARKEDNODEFLT = EMAKEHR(0x1273)    # Field is marked HasDefault but has no value.
    VLDTR_E_FD_DEFLTNOTMARKED = EMAKEHR(0x1274)    # Field has value rec but is not marked HasDefault.
    VLDTR_E_FMD_MARKEDNOSECUR = EMAKEHR(0x1275)    # Field/method is marked HasSecurity but has no security rec.
    VLDTR_E_FMD_SECURNOTMARKED = EMAKEHR(0x1276)    # Field/method has security rec but is not marked HasSecurity.
    VLDTR_E_FMD_PINVOKENOTSTATIC = EMAKEHR(0x1277)    # Field/method is PInvoke but is not marked Static.
    VLDTR_E_FMD_MARKEDNOPINVOKE = EMAKEHR(0x1278)    # Field/method is marked PInvoke but has no ImplMap.
    VLDTR_E_FMD_PINVOKENOTMARKED = EMAKEHR(0x1279)    # Field/method has ImplMap but is not marked PInvoke.
    VLDTR_E_FMD_BADIMPLMAP = EMAKEHR(0x127A)    # Field/method has invalid ImplMap
    VLDTR_E_IMAP_BADMODREF = EMAKEHR(0x127B)    # ImplMap has invalid ModuleRef
    VLDTR_E_IMAP_BADMEMBER = EMAKEHR(0x127C)    # ImplMap has invalid MemberForwarded
    VLDTR_E_IMAP_BADIMPORTNAME = EMAKEHR(0x127D)    # ImplMap has invalid ImportName
    VLDTR_E_IMAP_BADCALLCONV = EMAKEHR(0x127E)    # ImplMap has invalid call conv
    VLDTR_E_FMD_BADACCESSFLAG = EMAKEHR(0x127F)    # Field/method has invalid access flag
    VLDTR_E_FD_INITONLYANDLITERAL = EMAKEHR(0x1280)    # Field is InitOnly and Literal
    VLDTR_E_FD_LITERALNOTSTATIC = EMAKEHR(0x1281)    # Field is Literal but not Static
    VLDTR_E_FMD_RTSNNOTSN = EMAKEHR(0x1282)    # Field/method is RTSpec.Name but not Spec.Name
    VLDTR_E_MD_ABSTPARNOTABST = EMAKEHR(0x1283)    # Method is abstract, parent is not
    VLDTR_E_MD_NOTSTATABSTININTF = EMAKEHR(0x1284)    # Method not static or abstract in interface
    VLDTR_E_MD_NOTPUBININTF = EMAKEHR(0x1285)    # Method not public in interface
    VLDTR_E_MD_CTORININTF = EMAKEHR(0x1286)    # ctor in interface
    VLDTR_E_MD_GLOBALCTORCCTOR = EMAKEHR(0x1287)    # global ctor or cctor
    VLDTR_E_MD_CTORSTATIC = EMAKEHR(0x1288)    # static ctor
    VLDTR_E_MD_CTORNOTSNRTSN = EMAKEHR(0x1289)    # ctor,cctor not marked SpecialName,RTSpecialName
    VLDTR_E_MD_CTORVIRT = EMAKEHR(0x128A)    # virtual ctor,cctor
    VLDTR_E_MD_CTORABST = EMAKEHR(0x128B)    # abstract ctor,cctor
    VLDTR_E_MD_CCTORNOTSTATIC = EMAKEHR(0x128C)    # instance cctor
    VLDTR_E_MD_ZERORVA = EMAKEHR(0x128D)    # RVA=0, method not abstract or pinvoke or runtime, or reverse
    VLDTR_E_MD_FINNOTVIRT = EMAKEHR(0x128E)    # Method is final and not virtual
    VLDTR_E_MD_STATANDFINORVIRT = EMAKEHR(0x128F)    # Method is static and final or virtual
    VLDTR_E_MD_ABSTANDFINAL = EMAKEHR(0x1290)    # Method is abstract and final
    VLDTR_E_MD_ABSTANDIMPL = EMAKEHR(0x1291)    # Method is abstract and implemented
    VLDTR_E_MD_ABSTANDPINVOKE = EMAKEHR(0x1292)    # Method is abstract and pinvoke
    VLDTR_E_MD_ABSTNOTVIRT = EMAKEHR(0x1293)    # Method is abstract and not virtual
    VLDTR_E_MD_NOTABSTNOTIMPL = EMAKEHR(0x1294)    # Method is not abstract and not implemented
    VLDTR_E_MD_NOTABSTBADFLAGSRVA = EMAKEHR(0x1295)    # Method is not abstract and not (RVA != 0 or pinvoke or runtime)
    VLDTR_E_MD_PRIVSCOPENORVA = EMAKEHR(0x1296)    # Method is PrivateScope and has RVA == 0
    VLDTR_E_MD_GLOBALABSTORVIRT = EMAKEHR(0x1297)    # Global method is abstract or virtual
    VLDTR_E_SIG_LONGFORM = EMAKEHR(0x1298)    # Signature uses LONG form
    VLDTR_E_MD_MULTIPLESEMANTICS = EMAKEHR(0x1299)    # Method has multiple semantics (warning)
    VLDTR_E_MD_INVALIDSEMANTICS = EMAKEHR(0x129A)    # Method has invalid semantics (not event or prop)
    VLDTR_E_MD_SEMANTICSNOTEXIST = EMAKEHR(0x129B)    # Method has semantics assoc that does not exist
    VLDTR_E_MI_DECLNOTVIRT = EMAKEHR(0x129C)    # MethodImpl's Decl is not virtual
    VLDTR_E_FMD_GLOBALITEM = EMAKEHR(0x129D)    # Global field/method (warning,CLS)
    VLDTR_E_MD_MULTSEMANTICFLAGS = EMAKEHR(0x129E)    # Method has multiple semantic flags set
    VLDTR_E_MD_NOSEMANTICFLAGS = EMAKEHR(0x129F)    # Method has no semantic flags set
    VLDTR_E_FD_FLDINIFACE = EMAKEHR(0x12A0)    # Field in Interface (warning, CLS)
    VLDTR_E_AS_HASHALGID = EMAKEHR(0x12A1)    # Unrecognized Hash Alg ID (warning)
    VLDTR_E_AS_PROCID = EMAKEHR(0x12A2)    # Unrecognized Processor ID in Assembly(warning)
    VLDTR_E_AR_PROCID = EMAKEHR(0x12A3)    # Unrecognized Processor ID in AssemblyRef(warning)
    VLDTR_E_CN_PARENTRANGE = EMAKEHR(0x12A4)    # Constant: parent token out of range
    VLDTR_E_AS_BADFLAGS = EMAKEHR(0x12A5)    # Invalid flags in Assembly
    VLDTR_E_TR_HASTYPEDEF = EMAKEHR(0x12A6)    # There is TypeDef with same name as TypeRef (warning)
    VLDTR_E_IFACE_BADIMPL = EMAKEHR(0x12A7)    # In InterfaceImpl, the implementing token is not TypeDef
    VLDTR_E_IFACE_BADIFACE = EMAKEHR(0x12A8)    # In InterfaceImpl, the implemented token is not TypeDef or TypeRef
    VLDTR_E_TD_SECURNOTMARKED = EMAKEHR(0x12A9)    # TypeDef has security rec but not marked HasSecurity
    VLDTR_E_TD_MARKEDNOSECUR = EMAKEHR(0x12AA)    # TypeDef marked HasSecurity but has no security rec
    VLDTR_E_MD_CCTORHASARGS = EMAKEHR(0x12AB)    # .cctor has arguments
    VLDTR_E_CT_BADIMPL = EMAKEHR(0x12AC)    # ExportedType has invalid Implementation
    VLDTR_E_MI_ALIENBODY = EMAKEHR(0x12AD)    # MethodImpl has body from other class
    VLDTR_E_MD_CCTORCALLCONV = EMAKEHR(0x12AE)    # .cctor has invalid calling convention
    VLDTR_E_MI_BADCLASS = EMAKEHR(0x12AF)    # MethodImpl has invalid Class token
    VLDTR_E_MI_CLASSISINTF = EMAKEHR(0x12B0)    # MethodImpl declared in Interface
    VLDTR_E_MI_BADDECL = EMAKEHR(0x12B1)    # MethodImpl has invalid MethodDeclaration token
    VLDTR_E_MI_BADBODY = EMAKEHR(0x12B2)    # MethodImpl has invalid MethodBody token
    VLDTR_E_MI_DUP = EMAKEHR(0x12B3)    # MethodImpl has duplicate
    VLDTR_E_FD_BADPARENT = EMAKEHR(0x12B4)    # Bad field parent
    VLDTR_E_MD_PARAMOUTOFSEQ = EMAKEHR(0x12B5)    # Param out of sequence (warning)
    VLDTR_E_MD_PARASEQTOOBIG = EMAKEHR(0x12B6)    # Param's sequence num exceeds num of args
    VLDTR_E_MD_PARMMARKEDNOMARSHAL = EMAKEHR(0x12B7)    # Param marked HasMarshal, has no marshaling info
    VLDTR_E_MD_PARMMARSHALNOTMARKED = EMAKEHR(0x12B8)    # Param has marshaling info, not marked HasMarshal
    VLDTR_E_MD_PARMMARKEDNODEFLT = EMAKEHR(0x12BA)    # Param marked HasDefault, has no value
    VLDTR_E_MD_PARMDEFLTNOTMARKED = EMAKEHR(0x12BB)    # Param has value, not marked HasDefault
    VLDTR_E_PR_BADSCOPE = EMAKEHR(0x12BC)    # Prop has invalid scope
    VLDTR_E_PR_NONAME = EMAKEHR(0x12BD)    # Prop has no name
    VLDTR_E_PR_NOSIG = EMAKEHR(0x12BE)    # Prop has no signature
    VLDTR_E_PR_DUP = EMAKEHR(0x12BF)    # Prop has a duplicate
    VLDTR_E_PR_BADCALLINGCONV = EMAKEHR(0x12C0)    # Prop has bad calling convention
    VLDTR_E_PR_MARKEDNODEFLT = EMAKEHR(0x12C1)    # Prop marked HasDefault, has no value
    VLDTR_E_PR_DEFLTNOTMARKED = EMAKEHR(0x12C2)    # Prop has value, not marked HasDefault
    VLDTR_E_PR_BADSEMANTICS = EMAKEHR(0x12C3)    # Prop has method not (Setter,Getter, or Other)
    VLDTR_E_PR_BADMETHOD = EMAKEHR(0x12C4)    # Prop has method with invalid token
    VLDTR_E_PR_ALIENMETHOD = EMAKEHR(0x12C5)    # Prop has method from another class
    VLDTR_E_CN_BLOBNOTNULL = EMAKEHR(0x12C6)    # Const has non-null blob when it should not
    VLDTR_E_CN_BLOBNULL = EMAKEHR(0x12C7)    # Const has null value blob
    VLDTR_E_EV_BADSCOPE = EMAKEHR(0x12C8)    # Event has invalid scope
    VLDTR_E_EV_NONAME = EMAKEHR(0x12CA)    # Event has no name
    VLDTR_E_EV_DUP = EMAKEHR(0x12CB)    # Event has a duplicate
    VLDTR_E_EV_BADEVTYPE = EMAKEHR(0x12CC)    # Event has invalid EventType
    VLDTR_E_EV_EVTYPENOTCLASS = EMAKEHR(0x12CD)    # Event's EventType is not a class
    VLDTR_E_EV_BADSEMANTICS = EMAKEHR(0x12CE)    # Event has method not (AddOn,RemoveOn,Fire,Other)
    VLDTR_E_EV_BADMETHOD = EMAKEHR(0x12CF)    # Event has method with invalid token
    VLDTR_E_EV_ALIENMETHOD = EMAKEHR(0x12D0)    # Event has method from another class
    VLDTR_E_EV_NOADDON = EMAKEHR(0x12D1)    # Event has no AddOn method
    VLDTR_E_EV_NOREMOVEON = EMAKEHR(0x12D2)    # Event has no RemoveOn method
    VLDTR_E_CT_DUPTDNAME = EMAKEHR(0x12D3)    # ExportedType has same name as TypeDef
    VLDTR_E_MAR_BADOFFSET = EMAKEHR(0x12D4)    # MRes refers to non-PE file with offset != 0
    VLDTR_E_DS_BADOWNER = EMAKEHR(0x12D5)    # Decl.security has invalid owner token
    VLDTR_E_DS_BADFLAGS = EMAKEHR(0x12D6)    # Decl.security has invalid action flags
    VLDTR_E_DS_NOBLOB = EMAKEHR(0x12D7)    # Decl.security has no permission blob
    VLDTR_E_MAR_BADIMPL = EMAKEHR(0x12D8)    # Manifest resource has invalid Implementation
    VLDTR_E_MR_VARARGCALLINGCONV = EMAKEHR(0x12DA)    # MemberRef has VARARG calling conv. (CLS warning)
    VLDTR_E_MD_CTORNOTVOID = EMAKEHR(0x12DB)    # .ctor,.cctor returning not void
    VLDTR_E_EV_FIRENOTVOID = EMAKEHR(0x12DC)    # Fire method returning not void
    VLDTR_E_AS_BADLOCALE = EMAKEHR(0x12DD)    # Invalid locale
    VLDTR_E_CN_PARENTTYPE = EMAKEHR(0x12DE)    # Constant has parent of invalid type
    VLDTR_E_SIG_SENTINMETHODDEF = EMAKEHR(0x12DF)    # E_T_SENTINEL in MethodDef signature
    VLDTR_E_SIG_SENTMUSTVARARG = EMAKEHR(0x12E0)    # E_T_SENTINEL <= > VARARG
    VLDTR_E_SIG_MULTSENTINELS = EMAKEHR(0x12E1)    # Multiple E_T_SENTINELs
    VLDTR_E_SIG_LASTSENTINEL = EMAKEHR(0x12E2)    # E_T_SENTINEL not followed by type
    VLDTR_E_SIG_MISSARG = EMAKEHR(0x12E3)    # Signature missing argument
    VLDTR_E_SIG_BYREFINFIELD = EMAKEHR(0x12E4)    # Field of ByRef type
    VLDTR_E_MD_SYNCMETHODINVTYPE = EMAKEHR(0x12E5)    # Synchronized method in value class
    VLDTR_E_TD_NAMETOOLONG = EMAKEHR(0x12E6)    # TypeDef name too long
    VLDTR_E_AS_PROCDUP = EMAKEHR(0x12E7)    # Duplicate Assembly Processor
    VLDTR_E_ASOS_DUP = EMAKEHR(0x12E8)    # Duplicate Assembly OS (ID + ver.major + ver.minor)
    VLDTR_E_MAR_BADFLAGS = EMAKEHR(0x12E9)    # Manifest Resource has bad flags
    VLDTR_E_CT_NOTYPEDEFID = EMAKEHR(0x12EA)    # ExportedType has nil TypeDefId
    VLDTR_E_FILE_BADFLAGS = EMAKEHR(0x12EB)    # File has bad flags
    VLDTR_E_FILE_NULLHASH = EMAKEHR(0x12EC)    # File has no hash blob
    VLDTR_E_MOD_NONAME = EMAKEHR(0x12ED)    # Module has no name
    VLDTR_E_MOD_NAMEFULLQLFD = EMAKEHR(0x12EE)    # Module has fully-qualified name
    VLDTR_E_TD_RTSPCLNOTSPCL = EMAKEHR(0x12EF)    # TypeDef is tdRTSpecialName but not tdSpecialName
    VLDTR_E_TD_EXTENDSIFACE = EMAKEHR(0x12F0)    # TypeDef extends interface
    VLDTR_E_MD_CTORPINVOKE = EMAKEHR(0x12F1)    # .ctor,.cctor is PInvokeImpl
    VLDTR_E_TD_SYSENUMNOTCLASS = EMAKEHR(0x12F2)    # System.Enum is not a class
    VLDTR_E_TD_SYSENUMNOTEXTVTYPE = EMAKEHR(0x12F3)    # System.Enum extends not System.ValueType
    VLDTR_E_MI_SIGMISMATCH = EMAKEHR(0x12F4)    # MethodImpl's Decl and Body signatures mismatch
    VLDTR_E_TD_ENUMHASMETHODS = EMAKEHR(0x12F5)    # TypeDef extends System.Enum but has methods
    VLDTR_E_TD_ENUMIMPLIFACE = EMAKEHR(0x12F6)    # TypeDef extends System.Enum but impls interface(s)
    VLDTR_E_TD_ENUMHASPROP = EMAKEHR(0x12F7)    # TypeDef extends System.Enum but has prop(s)
    VLDTR_E_TD_ENUMHASEVENT = EMAKEHR(0x12F8)    # TypeDef extends System.Enum but has event(s)
    VLDTR_E_TD_BADMETHODLST = EMAKEHR(0x12F9)    # TypeDef has MethodList > Nmethods + 1
    VLDTR_E_TD_BADFIELDLST = EMAKEHR(0x12FA)    # TypeDef has FieldList > Nfields + 1
    VLDTR_E_CN_BADTYPE = EMAKEHR(0x12FB)    # Constant has wrong type
    VLDTR_E_TD_ENUMNOINSTFLD = EMAKEHR(0x12FC)    # Enum has no instance fields
    VLDTR_E_TD_ENUMMULINSTFLD = EMAKEHR(0x12FD)    # Enum has multiple instance fields
    VLDTR_E_INTERRUPTED = EMAKEHR(0x12FE)    # Validator has been interrupted by the VEHandler.
    VLDTR_E_NOTINIT = EMAKEHR(0x12FF)    # Validator failed to initialize correctly.
    VLDTR_E_IFACE_NOTIFACE = EMAKEHR(0x1B00)    # Interface in InterfaceImpl is not marked tdInterface
    VLDTR_E_FD_RVAHASNORVA = EMAKEHR(0x1B01)    # Field marked fdHasFieldRVA but has no RVA rec
    VLDTR_E_FD_RVAHASZERORVA = EMAKEHR(0x1B02)    # Field marked fdHasFieldRVA has RVA =0
    VLDTR_E_MD_RVAANDIMPLMAP = EMAKEHR(0x1B03)    # Method has both RVA != 0 and ImplMap
    VLDTR_E_TD_EXTRAFLAGS = EMAKEHR(0x1B04)    # TypeDef has extraneous bits in flags
    VLDTR_E_TD_EXTENDSITSELF = EMAKEHR(0x1B05)    # TypeDef extends itself
    VLDTR_E_TD_SYSVTNOTEXTOBJ = EMAKEHR(0x1B06)    # System.ValueType does not extend System.Object
    VLDTR_E_TD_EXTTYPESPEC = EMAKEHR(0x1B07)    # Class extends TypeSpec (warning)
    VLDTR_E_TD_VTNOSIZE = EMAKEHR(0x1B09)    # Value Class has zero size
    VLDTR_E_TD_IFACESEALED = EMAKEHR(0x1B0A)    # Interface is sealed
    VLDTR_E_NC_BADNESTED = EMAKEHR(0x1B0B)    # Bad "nested" token in NestedClass
    VLDTR_E_NC_BADENCLOSER = EMAKEHR(0x1B0C)    # Bad "enclosing" token in NestedClass
    VLDTR_E_NC_DUP = EMAKEHR(0x1B0D)    # Duplicate NestedClass record
    VLDTR_E_NC_DUPENCLOSER = EMAKEHR(0x1B0E)    # Duplicate NestedClass with different encloser
    VLDTR_E_FRVA_ZERORVA = EMAKEHR(0x1B0F)    # RVA=0 in FieldRVA record
    VLDTR_E_FRVA_BADFIELD = EMAKEHR(0x1B10)    # Invalid field token in FieldRVA record
    VLDTR_E_FRVA_DUPRVA = EMAKEHR(0x1B11)    # Duplicate RVA in FieldRVA record
    VLDTR_E_FRVA_DUPFIELD = EMAKEHR(0x1B12)    # Duplicate field in FieldRVA record
    VLDTR_E_EP_BADTOKEN = EMAKEHR(0x1B13)    # Bad token as entry point in CLR header
    VLDTR_E_EP_INSTANCE = EMAKEHR(0x1B14)    # Entry point in CLR header is a token of instance method
    VLDTR_E_TD_ENUMFLDBADTYPE = EMAKEHR(0x1B15)    # Enum has non-integral underlying type
    VLDTR_E_MD_BADRVA = EMAKEHR(0x1B16)    # Method has bogus RVA
    VLDTR_E_FD_LITERALNODEFAULT = EMAKEHR(0x1B17)    # Literal field has no value
    VLDTR_E_IFACE_METHNOTIMPL = EMAKEHR(0x1B18)    # Class implementing an interface doesn't impl.one of methods
    VLDTR_E_CA_BADPARENT = EMAKEHR(0x1B19)    # CA has invalid owner
    VLDTR_E_CA_BADTYPE = EMAKEHR(0x1B1A)    # CA has invalid type
    VLDTR_E_CA_NOTCTOR = EMAKEHR(0x1B1B)    # CA type is not .ctor
    VLDTR_E_CA_BADSIG = EMAKEHR(0x1B1C)    # CA type has bad signature
    VLDTR_E_CA_NOSIG = EMAKEHR(0x1B1D)    # CA type has no signature
    VLDTR_E_CA_BADPROLOG = EMAKEHR(0x1B1E)    # CA blob has bad prolog (not 0x01 0x00)
    VLDTR_E_MD_BADLOCALSIGTOK = EMAKEHR(0x1B1F)    # Method has invalid LocalSig token
    VLDTR_E_MD_BADHEADER = EMAKEHR(0x1B20)    # Method has invalid header
    VLDTR_E_EP_TOOMANYARGS = EMAKEHR(0x1B21)    # Entry point has more than one arg
    VLDTR_E_EP_BADRET = EMAKEHR(0x1B22)    # Entry point has bad return type
    VLDTR_E_EP_BADARG = EMAKEHR(0x1B23)    # Entry point has bad argument
    VLDTR_E_SIG_BADVOID = EMAKEHR(0x1B24)    # Illegal "void" in signature
    VLDTR_E_IFACE_METHMULTIMPL = EMAKEHR(0x1B25)    # Multiple implementation of method

    # @GENERICS
    VLDTR_E_GP_NAMENULL = EMAKEHR(0x1B26)    # GenericParam name is NULL
    VLDTR_E_GP_OWNERNIL = EMAKEHR(0x1B27)    # GenericParam has nil owner.
    VLDTR_E_GP_DUPNAME = EMAKEHR(0x1B28)    # GenericParam has duplicate by owner and name.
    VLDTR_E_GP_DUPNUMBER = EMAKEHR(0x1B29)    # GenericParam has duplicate by owner and number.
    VLDTR_E_GP_NONSEQ_BY_OWNER = EMAKEHR(0x1B2A)    # GenericParam is non sequential by owner
    VLDTR_E_GP_NONSEQ_BY_NUMBER = EMAKEHR(0x1B2B)    # GenericParam is non sequential by number
    VLDTR_E_GP_UNEXPECTED_OWNER_FOR_VARIANT_VAR = EMAKEHR(0x1B2C)    # GenericParam has variance but its owner is not an interface or delegate
    VLDTR_E_GP_ILLEGAL_VARIANT_MVAR = EMAKEHR(0x1B2D)    # GenericParam is a method type parameter and must be non-variant
    VLDTR_E_GP_ILLEGAL_VARIANCE_FLAGS = EMAKEHR(0x1B2E)    # GenericParam has illegal value for variance flags

    # GenericParam has incompatible special constraints reference type and
    # valuetype
    VLDTR_E_GP_REFANDVALUETYPE = EMAKEHR(0x1B2F)
    VLDTR_E_GPC_OWNERNIL = EMAKEHR(0x1B30)    # GenericParamConstraint has nil owner
    VLDTR_E_GPC_DUP = EMAKEHR(0x1B31)    # GenericParamConstraint has duplicate by owner and constraint

    # GenericParamConstraint is non-contiguous with preceeding constraints for
    # same owner
    VLDTR_E_GPC_NONCONTIGUOUS = EMAKEHR(0x1B32)
    VLDTR_E_MS_METHODNIL = EMAKEHR(0x1B33)    # MethodSpec has nil method
    VLDTR_E_MS_DUP = EMAKEHR(0x1B34)    # MethodSpec has duplicate based own method and instantiation
    VLDTR_E_MS_BADCALLINGCONV = EMAKEHR(0x1B35)    # MethodSpec signature has invalid calling convention
    VLDTR_E_MS_MISSARITY = EMAKEHR(0x1B36)    # MethodSpec signature is missing arity specification
    VLDTR_E_MS_MISSARG = EMAKEHR(0x1B37)    # MethodSpec signature is missing type argument
    VLDTR_E_MS_ARITYMISMATCH = EMAKEHR(0x1B38)    # MethodSpec arity of generic method and instantiation do not match
    VLDTR_E_MS_METHODNOTGENERIC = EMAKEHR(0x1B39)    # MethodSpec method is not generic
    VLDTR_E_SIG_MISSARITY = EMAKEHR(0x1B3A)    # Signature missing arity of instantiated generic type
    VLDTR_E_SIG_ARITYMISMATCH = EMAKEHR(0x1B3B)    # Signature has generic type of arity instantiated at different arity
    VLDTR_E_MD_GENERIC_CCTOR = EMAKEHR(0x1B3C)    # Method cannot be both generic and a class constructor
    VLDTR_E_MD_GENERIC_CTOR = EMAKEHR(0x1B3D)    # Method cannot be both generic and an instance constructor
    VLDTR_E_MD_GENERIC_IMPORT = EMAKEHR(0x1B3E)    # Method cannot be both generic and defined on an imported type
    VLDTR_E_MD_GENERIC_BADCALLCONV = EMAKEHR(0x1B3F)    # Method cannot be both generic and have non-default calling convention
    VLDTR_E_EP_GENERIC_METHOD = EMAKEHR(0x1B40)    # Entry point in CLR header is the token for a generic method
    VLDTR_E_MD_MISSARITY = EMAKEHR(0x1B41)    # Method signature is generic but is missing its arity
    VLDTR_E_MD_ARITYZERO = EMAKEHR(0x1B42)    # Method signature is generic but its arity is zero
    VLDTR_E_SIG_ARITYZERO = EMAKEHR(0x1B43)    # Signature has generic type instantiated at arity 0
    VLDTR_E_MS_ARITYZERO = EMAKEHR(0x1B44)    # MethodSpec signature has arity 0
    VLDTR_E_MD_GPMISMATCH = EMAKEHR(0x1B45)    # MethodDef signature has arity n but owns m GenericParams
    VLDTR_E_EP_GENERIC_TYPE = EMAKEHR(0x1B46)    # Entry point in CLR header is the token for a method in a generic type
    VLDTR_E_MI_DECLNOTGENERIC = EMAKEHR(0x1B47)    # MethodImpl overrides non-generic method with generic method
    VLDTR_E_MI_IMPLNOTGENERIC = EMAKEHR(0x1B48)    # MethodImpl overrides non-generic method with generic method

    # MethodImpl overrides generic method of arity n with generic method of
    # arity m
    VLDTR_E_MI_ARITYMISMATCH = EMAKEHR(0x1B49)
    VLDTR_E_TD_EXTBADTYPESPEC = EMAKEHR(0x1B4A)    # TypeDef extends a TypeSpec that is not an instantiated type
    VLDTR_E_SIG_BYREFINST = EMAKEHR(0x1B4B)    # Signature has type instantiated at byref at offset i
    VLDTR_E_MS_BYREFINST = EMAKEHR(0x1B4C)    # Signature has type instantiated at byref at offset i
    VLDTR_E_TS_EMPTY = EMAKEHR(0x1B4D)    # TypeSpec has empty signature
    VLDTR_E_TS_HASSENTINALS = EMAKEHR(0x1B4E)    # TypeSpec has signature containing one or more sentinals
    VLDTR_E_TD_GENERICHASEXPLAYOUT = EMAKEHR(0x1B4F)    # TypeDef is generic but has explicit layout

    # Signature has token following ELEMENT_TYPE_CLASS (_VALUETYPE) that is
    # not a TypeDef or TypeRef
    VLDTR_E_SIG_BADTOKTYPE = EMAKEHR(0x1B50)
    VLDTR_E_IFACE_METHNOTIMPLTHISMOD = EMAKEHR(0x1B51)    # Warn:Class doesn't implement interface method in this module

    # *** Common Language Runtime Debugging Services errors
    CORDBG_E_UNRECOVERABLE_ERROR = EMAKEHR(0x1300)    # Unrecoverable API error.
    CORDBG_E_PROCESS_TERMINATED = EMAKEHR(0x1301)    # Process was terminated.
    CORDBG_E_PROCESS_NOT_SYNCHRONIZED = EMAKEHR(0x1302)    # Process not synchronized.
    CORDBG_E_CLASS_NOT_LOADED = EMAKEHR(0x1303)    # A class is not loaded.
    CORDBG_E_IL_VAR_NOT_AVAILABLE = EMAKEHR(0x1304)    # An IL variable is not available at the

    # current native IP.
    CORDBG_E_BAD_REFERENCE_VALUE = EMAKEHR(0x1305)    # A reference value was found to be bad

    # during dereferencing.
    CORDBG_E_FIELD_NOT_AVAILABLE = EMAKEHR(0x1306)    # A field in a class is not available,

    # because the runtime optimized it away.
    CORDBG_E_NON_NATIVE_FRAME = EMAKEHR(0x1307)    # "Native frame only" operation on

    # non-native frame
    CORDBG_E_NONCONTINUABLE_EXCEPTION = EMAKEHR(0x1308)    # Continue on non-continuable exception
    CORDBG_E_CODE_NOT_AVAILABLE = EMAKEHR(0x1309)    # The code is currently unavailable
    CORDBG_E_FUNCTION_NOT_IL = EMAKEHR(0x130A)    # Attempt to get a ICorDebugFunction for

    # a function that is not IL.
    CORDBG_S_BAD_START_SEQUENCE_POINT = SMAKEHR(0x130B)    # Attempt to SetIP not at a sequence point
    CORDBG_S_BAD_END_SEQUENCE_POINT = SMAKEHR(0x130C)    # Attempt to SetIP when not going to a

    # sequence point. If both this and
    # CORDBG_E_BAD_START_SEQUENCE_POINT are
    # true, only CORDBG_E_BAD_START_SEQUENCE_POINT
    # will be reported.
    CORDBG_S_INSUFFICIENT_INFO_FOR_SET_IP = SMAKEHR(0x130D)    # SetIP is possible, but the debugger doesn't

    # have enough info to fix variable locations,
    # GC refs, or anything else. Use at your own
    # risk.
    CORDBG_E_CANT_SET_IP_INTO_FINALLY = EMAKEHR(0x130E)    # SetIP isn't possible, because SetIP would

    # move EIP from outside of an exception
    # handling finally clause to a point inside
    # of one.
    CORDBG_E_CANT_SET_IP_OUT_OF_FINALLY = EMAKEHR(0x130F)    # SetIP isn't possible because it would move

    # EIP from within an exception handling finally
    # clause to a point outside of one.
    CORDBG_E_CANT_SET_IP_INTO_CATCH = EMAKEHR(0x1310)    # SetIP isn't possible, because SetIP would

    # move EIP from outside of an exception
    # handling catch clause to a point inside of
    # one.
    CORDBG_E_SET_IP_NOT_ALLOWED_ON_NONLEAF_FRAME = EMAKEHR(0x1311)    # Setip cannot be done on any frame except

    # the leaf frame.
    CORDBG_E_SET_IP_IMPOSSIBLE = EMAKEHR(0x1312)    # SetIP isn't allowed. For example, there is

    # insufficient memory to perform SetIP.
    CORDBG_E_FUNC_EVAL_BAD_START_POINT = EMAKEHR(0x1313)    # Func eval can't work if we're, for example,

    # not stopped at a GC safe point.
    CORDBG_E_FUNC_EVAL_NOT_COMPLETE = EMAKEHR(0x1315)    # If you call CordbEval::GetResult before the

    # func eval has finished, you'll get this
    # result.
    CORDBG_S_FUNC_EVAL_HAS_NO_RESULT = SMAKEHR(0x1316)    # Some Func evals will lack a return value,

    # such as those whose return type is void.
    CORDBG_S_VALUE_POINTS_TO_VOID = SMAKEHR(0x1317)    # The Debugging API doesn't support

    # dereferencing pointers of type void.
    CORDBG_E_INPROC_NOT_IMPL = EMAKEHR(0x1318)    # The inproc version of the debugging API

    # doesn't implement this function,
    CORDBG_S_FUNC_EVAL_ABORTED = SMAKEHR(0x1319)    # The func eval completed, but was aborted.
    CORDBG_E_STATIC_VAR_NOT_AVAILABLE = EMAKEHR(0x131A)    # A static variable isn't available because

    # it hasn't been initialized yet.
    CORDBG_E_OBJECT_IS_NOT_COPYABLE_VALUE_CLASS = EMAKEHR(0x131B)    # Can't copy a VC with object refs in it.
    CORDBG_E_CANT_SETIP_INTO_OR_OUT_OF_FILTER = EMAKEHR(0x131C)    # SetIP can't leave or enter a filter
    CORDBG_E_CANT_CHANGE_JIT_SETTING_FOR_ZAP_MODULE = EMAKEHR(0x131D)    # You can't change JIT settings for ZAP

    # modules.
    CORDBG_E_CANT_SET_IP_OUT_OF_FINALLY_ON_WIN64 = EMAKEHR(0x131E)    # SetIP isn't possible because it would move

    # EIP from within a finally clause to a point
    # outside of one on WIN64 platforms.
    CORDBG_E_CANT_SET_IP_OUT_OF_CATCH_ON_WIN64 = EMAKEHR(0x131F)    # SetIP isn't possible because it would move

    # EIP from within a catch clause to a point
    # outside of one on WIN64 platforms.
    CORDBG_E_REMOTE_CONNECTION_CONN_RESET = EMAKEHR(0x1320)    # The remote device closed the connection.
    CORDBG_E_REMOTE_CONNECTION_KEEP_ALIVE = EMAKEHR(0x1321)    # The connection was closed due to akeep alive failure.

    # Generic error that the device connection has been broken with no chance
    # for recovery.
    CORDBG_E_REMOTE_CONNECTION_FATAL_ERROR = EMAKEHR(0x1322)
    CORDBG_E_CANT_SET_TO_JMC = EMAKEHR(0x1323)    # Can't use JMC on this code (likely wrong jit settings).
    CORDBG_E_BAD_THREAD_STATE = EMAKEHR(0x132D)    # The state of the thread is invalid.
    CORDBG_E_SUPERFLOUS_CONTINUE = EMAKEHR(0x132F)    # Returned from a call to Continue that was

    # Not matched with a stopping event.
    CORDBG_E_SET_VALUE_NOT_ALLOWED_ON_NONLEAF_FRAME = EMAKEHR(0x1330)    # Can't perfrom SetValue on non-leaf frames.
    CORDBG_E_ENC_EH_MAX_NESTING_LEVEL_CANT_INCREASE = EMAKEHR(0x1331)    # When doing EnC, some JITters don't let you

    # increase the maximum level to which
    # exception handling can be nested.
    CORDBG_E_ENC_MODULE_NOT_ENC_ENABLED = EMAKEHR(0x1332)    # Tried to do EnC on a module that wasn't

    # started in EnC mode.
    CORDBG_E_SET_IP_NOT_ALLOWED_ON_EXCEPTION = EMAKEHR(0x1333)    # Setip cannot be done on any exception
    CORDBG_E_VARIABLE_IS_ACTUALLY_LITERAL = EMAKEHR(0x1334)    # The 'variable' doesn't exist because it is a

    # literal optimized away by the compiler - ask
    # Metadata for it's default value, instead.
    CORDBG_E_PROCESS_DETACHED = EMAKEHR(0x1335)    # Process has been detached from
    CORDBG_E_ENC_METHOD_SIG_CHANGED = EMAKEHR(0x1336)    # Not allowed to change the signature of an

    # existing method - compiler should make new method
    # instead.
    CORDBG_E_ENC_METHOD_NO_LOCAL_SIG = EMAKEHR(0x1337)    # Can't get the local signature for the method

    # we're trying to EnC.
    CORDBG_E_ENC_CANT_ADD_FIELD_TO_VALUE_OR_LAYOUT_CLASS = EMAKEHR(0x1338)    # Adding a field to a value or layout class is prohibitted,

    # since we can't guarantee the new field is contiguous to
    # VC's on the stack, embedded in other objects, etc.
    CORDBG_E_ENC_CANT_CHANGE_FIELD = EMAKEHR(0x1339)    # Once you've got a field, you're not allowed to change

    # it, since that would change the size of the type it belongs to.
    CORDBG_E_ENC_CANT_ADD_NON_PRIVATE_MEMBER = EMAKEHR(0x133A)    # Only support addition of private members.
    CORDBG_E_FIELD_NOT_STATIC = EMAKEHR(0x133B)    # Returned if someone tries to call GetStaticFieldValue

    # on a non-static field
    CORDBG_E_FIELD_NOT_INSTANCE = EMAKEHR(0x133C)    # Returned if someone tries to call GetStaticFieldValue

    # on a non-instance field
    CORDBG_E_ENC_ZAPPED_WITHOUT_ENC = EMAKEHR(0x133D)    # If a zap file was created without the EnC flag set, then

    # we can't do EnC on it, no matter what.
    CORDBG_E_ENC_BAD_METHOD_INFO = EMAKEHR(0x133E)    # Lacking information about method.
    CORDBG_E_ENC_JIT_CANT_UPDATE = EMAKEHR(0x133F)    # The JIT is unable to update the method.
    CORDBG_E_ENC_MISSING_CLASS = EMAKEHR(0x1340)    # An internal structure about the class is missing
    CORDBG_E_ENC_INTERNAL_ERROR = EMAKEHR(0x1341)    # Generic message for "Something user doesn't control went wrong" message.
    CORDBG_E_ENC_HANGING_FIELD = EMAKEHR(0x1342)    # The field was added via enc after the class was loaded, and so instead of

    # the field being contiguous with the other fields, it's 'hanging' off the
    # instance, so the right side will have to go & get (instance-specific
    # info based on the particular object.
    CORDBG_E_MODULE_NOT_LOADED = EMAKEHR(0x1343)    # If the module isn't loaded, including if it's been unloaded.
    CORDBG_E_ENC_CANT_CHANGE_SUPERCLASS = EMAKEHR(0x1344)    # Not allowed to change which class something inherits from
    CORDBG_E_UNABLE_TO_SET_BREAKPOINT = EMAKEHR(0x1345)    # Can't set a breakpoint here.
    # Debugging isn't possible due to an incompatability within the CLR
    # implementation.
    CORDBG_E_DEBUGGING_NOT_POSSIBLE = EMAKEHR(0x1346)
    # Debugging isn't possible because a kernel debugger is enabled on the
    # system.
    CORDBG_E_KERNEL_DEBUGGER_ENABLED = EMAKEHR(0x1347)
    # Debugging isn't possible because a kernel debugger is present on the
    # system.
    CORDBG_E_KERNEL_DEBUGGER_PRESENT = EMAKEHR(0x1348)
    CORDBG_E_HELPER_THREAD_DEAD = EMAKEHR(0x1349)    # The debugger's internal helper thread is dead.
    CORDBG_E_INTERFACE_INHERITANCE_CANT_CHANGE = EMAKEHR(0x134A)    # Not allowed to change interface inheritance.
    CORDBG_E_INCOMPATIBLE_PROTOCOL = EMAKEHR(0x134B)    # The debugger's protocol is incompatible with the debuggee.
    CORDBG_E_TOO_MANY_PROCESSES = EMAKEHR(0x134C)    # The debugger can only handle a finite number of debuggees.
    CORDBG_E_INTEROP_NOT_SUPPORTED = EMAKEHR(0x134D)    # Interop is not allowed on a win9x platform
    CORDBG_E_NO_REMAP_BREAKPIONT = EMAKEHR(0x134E)    # Cannot call RemapFunction until have received RemapBreakpoint
    CORDBG_E_OBJECT_NEUTERED = EMAKEHR(0x134F)    # Object has been neutered (it's in a zombie state).
    # NOTEnot YOU CANNOT PUT MORE ERRORS HEREnot They run into the range for
    # profiling errors. All new
    # new error need to be added below (search for cordbg_e_ in your editor).
    # *** Common Language Runtime Profiling Services errors
    CORPROF_E_FUNCTION_NOT_COMPILED = EMAKEHR(0x1350)    # Function not yet compiled.
    CORPROF_E_DATAINCOMPLETE = EMAKEHR(0x1351)    # The ID is not fully loaded/defined yet.
    CORPROF_E_NOT_REJITABLE_METHODS = EMAKEHR(0x1352)    # The Module is not configured for updateable methods.
    CORPROF_E_CANNOT_UPDATE_METHOD = EMAKEHR(0x1353)    # The Method could not be updated for re-jit.
    CORPROF_E_FUNCTION_NOT_IL = EMAKEHR(0x1354)    # The Method has no associated IL
    CORPROF_E_NOT_MANAGED_THREAD = EMAKEHR(0x1355)    # The thread has never run managed code before
    CORPROF_E_CALL_ONLY_FROM_INIT = EMAKEHR(0x1356)    # The function may only be called during profiler init
    CORPROF_E_INPROC_NOT_ENABLED = EMAKEHR(0x1357)    # Inprocess debugging must be enabled during init
    # Also returned when BeginInprocDebugging not called
    # before using the inprocess debugging services
    CORPROF_E_JITMAPS_NOT_ENABLED = EMAKEHR(0x1358)    # Can't get a JIT map becuase they are not enabled
    CORPROF_E_INPROC_ALREADY_BEGUN = EMAKEHR(0x1359)    # If a profiler tries to call BeginInprocDebugging more than
    # once, it will get this error.
    CORPROF_E_INPROC_NOT_AVAILABLE = EMAKEHR(0x135A)    # States that inprocess debugging not allowed at this point
    # (for example during GC callbacks or RuntimeSuspention callbacks
    # requested is not yet available
    CORPROF_E_TYPE_IS_PARAMETERIZED = EMAKEHR(0x135C)    # The given type is a generic and cannot be used with this method.
    CORPROF_E_FUNCTION_IS_PARAMETERIZED = EMAKEHR(0x135D)    # The given function is a generic and cannot be used with this method.
    CORPROF_E_STACKSNAPSHOT_INVALID_TGT_THREAD = EMAKEHR(0x135E)    # A profiler tried to walk the stack of an invalid thread
    # A profiler can not walk a thread that is currently executing unmanaged
    # code
    CORPROF_E_STACKSNAPSHOT_UNMANAGED_CTX = EMAKEHR(0x135F)
    CORPROF_E_STACKSNAPSHOT_UNSAFE = EMAKEHR(0x1360)    # A stackwalk at this point may cause dead locks or data corruption
    CORPROF_E_STACKSNAPSHOT_ABORTED = EMAKEHR(0x1361)    # Stackwalking callback requested the walk to abort
    CORPROF_E_LITERALS_HAVE_NO_ADDRESS = EMAKEHR(0x1362)    # Returned when asked for the address of a static that is a literal.
    # A call was made at an unsupported time
    # (e.g., API illegally called asynchronously)
    CORPROF_E_UNSUPPORTED_CALL_SEQUENCE = EMAKEHR(0x1363)
    # A legal asynchronous call was made at an unsafe time
    # (e.g., CLR locks are held)
    CORPROF_E_ASYNCHRONOUS_UNSAFE = EMAKEHR(0x1364)
    # The specified ClassID cannot be inspected by this function because it is
    # an array
    CORPROF_E_CLASSID_IS_ARRAY = EMAKEHR(0x1365)
    # The specified ClassID is a non-array composite type (e.g., ref) and
    # cannot be inspected
    CORPROF_E_CLASSID_IS_COMPOSITE = EMAKEHR(0x1366)
    # *** Security errors
    SECURITY_E_XML_TO_ASN_ENCODING = EMAKEHR(0x1400)    # Failed to convert XML to ASN
    # Loading this assembly would produce a different grant set from other
    # instances
    SECURITY_E_INCOMPATIBLE_SHARE = EMAKEHR(0x1401)
    SECURITY_E_UNVERIFIABLE = EMAKEHR(0x1402)    # Unverifable code failed policy check
    SECURITY_E_INCOMPATIBLE_EVIDENCE = EMAKEHR(0x1403)    # Assembly already loaded without additional security evidence.
    # *** Reserved.
    CLDB_E_INTERNALERROR = EMAKEHR(0x1FFF)
    # ******************
    # Debugger & Profiler errors
    # ******************
    # ******************
    # Security errors
    # ******************
    CORSEC_E_DECODE_SET = EMAKEHR(0x1410)    # Failure decoding permission set
    CORSEC_E_ENCODE_SET = EMAKEHR(0x1411)    # Failure encoding permission set
    CORSEC_E_UNSUPPORTED_FORMAT = EMAKEHR(0x1412)    # Unrecognized encoding format
    SN_CRYPTOAPI_CALL_FAILED = EMAKEHR(0x1413)    # StrongName APIs not supported on system
    CORSEC_E_CRYPTOAPI_CALL_FAILED = EMAKEHR(0x1413)    # StrongName APIs not supported on system
    SN_NO_SUITABLE_CSP = EMAKEHR(0x1414)    # StrongName APIs couldn't locate a matching CSP
    CORSEC_E_NO_SUITABLE_CSP = EMAKEHR(0x1414)    # StrongName APIs couldn't locate a matching CSP
    CORSEC_E_INVALID_ATTR = EMAKEHR(0x1415)    # Invalid security custom attribute
    CORSEC_E_POLICY_EXCEPTION = EMAKEHR(0x1416)    # PolicyException thrown
    CORSEC_E_MIN_GRANT_FAIL = EMAKEHR(0x1417)    # Failed to grant minimum permission requests
    CORSEC_E_NO_EXEC_PERM = EMAKEHR(0x1418)    # Failed to grant permission to execute
    CORSEC_E_XMLSYNTAX = EMAKEHR(0x1419)    # XML Syntax error
    CORSEC_E_INVALID_STRONGNAME = EMAKEHR(0x141A)    # Strong name validation failed
    CORSEC_E_MISSING_STRONGNAME = EMAKEHR(0x141B)    # Assembly is not strong named
    CORSEC_E_CONTAINER_NOT_FOUND = EMAKEHR(0x141C)    # Strong name key container not found
    CORSEC_E_INVALID_IMAGE_FORMAT = EMAKEHR(0x141D)    # Invalid assembly file format
    CORSEC_E_INVALID_PUBLICKEY = EMAKEHR(0x141E)    # Invalid assembly public key
    CORSEC_E_SIGNATURE_MISMATCH = EMAKEHR(0x1420)    # Signature size mismatch
    # *** crypto errors 1430 -- 1439
    CORSEC_E_CRYPTO = EMAKEHR(0x1430)    # generic CryptographicException
    CORSEC_E_CRYPTO_UNEX_OPER = EMAKEHR(0x1431)    # generic CryptographicUnexpectedOperationException
    # *** security custom attribute errors 143a -- 144f
    CORSECATTR_E_BAD_ATTRIBUTE = EMAKEHR(0x143A)    # Generic problem with a custom attribute
    CORSECATTR_E_MISSING_CONSTRUCTOR = EMAKEHR(0x143B)    # Missing a required constructor
    CORSECATTR_E_FAILED_TO_CREATE_PERM = EMAKEHR(0x143C)    # Unable to create a permission for this attribute
    CORSECATTR_E_BAD_ACTION_ASM = EMAKEHR(0x143D)    # SecurityAction type invalid on assembly
    CORSECATTR_E_BAD_ACTION_OTHER = EMAKEHR(0x143E)    # SecurityAction type invalid on types and methods
    CORSECATTR_E_BAD_PARENT = EMAKEHR(0x143F)    # Security custom attribute attached to invalid parent
    CORSECATTR_E_TRUNCATED = EMAKEHR(0x1440)    # Bad custom attribute serialized blob
    CORSECATTR_E_BAD_VERSION = EMAKEHR(0x1441)    # Bad custom attribute serialized blob version
    CORSECATTR_E_BAD_ACTION = EMAKEHR(0x1442)    # Invalid security action code
    CORSECATTR_E_NO_SELF_REF = EMAKEHR(0x1443)    # CA ref to CA def'd in same assembly
    CORSECATTR_E_BAD_NONCAS = EMAKEHR(0x1444)    # Use of non-CAS perm with invalid action
    CORSECATTR_E_ASSEMBLY_LOAD_FAILED = EMAKEHR(0x1445)    # Failed to load assembly containing CA (or req'd CA type)
    CORSECATTR_E_ASSEMBLY_LOAD_FAILED_EX = EMAKEHR(0x1446)    # Failed to load assembly containing CA (or req'd CA type)
    CORSECATTR_E_TYPE_LOAD_FAILED = EMAKEHR(0x1447)    # Failed to load CA type (or reqd CA type)
    CORSECATTR_E_TYPE_LOAD_FAILED_EX = EMAKEHR(0x1448)    # Failed to load CA type (or reqd CA type)
    CORSECATTR_E_ABSTRACT = EMAKEHR(0x1449)    # CA type is abstract
    CORSECATTR_E_UNSUPPORTED_TYPE = EMAKEHR(0x144A)    # Unsupported type for field/property setter
    CORSECATTR_E_UNSUPPORTED_ENUM_TYPE = EMAKEHR(0x144B)    # Unsupported base type for enum field/property
    CORSECATTR_E_NO_FIELD = EMAKEHR(0x144C)    # Couldn't find a CA field
    CORSECATTR_E_NO_PROPERTY = EMAKEHR(0x144D)    # Couldn't find a CA property
    CORSECATTR_E_EXCEPTION = EMAKEHR(0x144E)    # Unexpected exception
    CORSECATTR_E_EXCEPTION_HR = EMAKEHR(0x144F)    # Unexpected exception
    # *** Isolated Storage Errors 1450 - 14FF
    ISS_E_ISOSTORE = EMAKEHR(0x1450)
    ISS_E_OPEN_STORE_FILE = EMAKEHR(0x1460)
    ISS_E_OPEN_FILE_MAPPING = EMAKEHR(0x1461)
    ISS_E_MAP_VIEW_OF_FILE = EMAKEHR(0x1462)
    ISS_E_GET_FILE_SIZE = EMAKEHR(0x1463)
    ISS_E_CREATE_MUTEX = EMAKEHR(0x1464)
    ISS_E_LOCK_FAILED = EMAKEHR(0x1465)
    ISS_E_FILE_WRITE = EMAKEHR(0x1466)
    ISS_E_SET_FILE_POINTER = EMAKEHR(0x1467)
    ISS_E_CREATE_DIR = EMAKEHR(0x1468)
    ISS_E_STORE_NOT_OPEN = EMAKEHR(0x1469)
    ISS_E_CORRUPTED_STORE_FILE = EMAKEHR(0x1480)
    ISS_E_STORE_VERSION = EMAKEHR(0x1481)
    ISS_E_FILE_NOT_MAPPED = EMAKEHR(0x1482)
    ISS_E_BLOCK_SIZE_TOO_SMALL = EMAKEHR(0x1483)
    ISS_E_ALLOC_TOO_LARGE = EMAKEHR(0x1484)
    ISS_E_USAGE_WILL_EXCEED_QUOTA = EMAKEHR(0x1485)
    ISS_E_TABLE_ROW_NOT_FOUND = EMAKEHR(0x1486)
    ISS_E_DEPRECATE = EMAKEHR(0x14A0)
    ISS_E_CALLER = EMAKEHR(0x14A1)
    ISS_E_PATH_LENGTH = EMAKEHR(0x14A2)
    ISS_E_MACHINE = EMAKEHR(0x14A3)
    ISS_E_MACHINE_DACL = EMAKEHR(0x14A4)
    ISS_E_ISOSTORE_START = EMAKEHR(0x1450)
    ISS_E_ISOSTORE_END = EMAKEHR(0x14FF)
    # ******************
    # Classlib errors
    # ******************
    # MessageId: COR_E_APPLICATION
    # MessageText:
    # The base class for all "less serious" exceptions.
    COR_E_APPLICATION = EMAKEHR(0x1600)
    # MessageId: COR_E_ARGUMENT
    # MessageText:
    # An argument does not meet the contract of the method.
    COR_E_ARGUMENT = E_INVALIDARG    # 0x80070057
    # MessageId: COR_E_ARGUMENTOUTOFRANGE
    # MessageText:
    # An argument was out of its legal range.
    COR_E_ARGUMENTOUTOFRANGE = EMAKEHR(0x1502)
    # MessageId: COR_E_ARITHMETIC
    # MessageText:
    # Overflow or underflow in mathematical operations.
    COR_E_ARITHMETIC = HRESULT_FROM_WIN32(ERROR_ARITHMETIC_OVERFLOW)    # 0x80070216
    # MessageId: COR_E_ARRAYTYPEMISMATCH
    # MessageText:
    # Attempted to store an object of the wrong type in an array
    COR_E_ARRAYTYPEMISMATCH = EMAKEHR(0x1503)
    # MessageId: COR_E_CONTEXTMARSHAL
    # MessageText:
    COR_E_CONTEXTMARSHAL = EMAKEHR(0x1504)
    # MessageId: COR_E_TIMEOUT
    # MessageText:
    COR_E_TIMEOUT = EMAKEHR(0x1505)
    # MessageId: COR_E_KEYNOTFOUND
    # MessageText:
    COR_E_KEYNOTFOUND = EMAKEHR(0x1577)
    # MessageId: COR_E_DEVICESNOTSUPPORTED
    # MessageText:
    COR_E_DEVICESNOTSUPPORTED = EMAKEHR(0x1540)
    # MessageId: COR_E_DIVIDEBYZERO
    # MessageText:
    # Attempted to divide a number by zero.
    COR_E_DIVIDEBYZERO = _HRESULT_TYPEDEF_(0x80020012)    # DISP_E_DIVBYZERO
    # MessageId: COR_E_EXCEPTION
    # MessageText:
    # Base class for all exceptions in the runtime
    COR_E_EXCEPTION = EMAKEHR(0x1500)
    # MessageId: COR_E_EXECUTIONENGINE
    # MessageText:
    # An internal error happened in the Common Language Runtime's Execution
    # Engine
    COR_E_EXECUTIONENGINE = EMAKEHR(0x1506)
    # MessageId: COR_E_FIELDACCESS
    # MessageText:
    # Access to this field is denied.
    COR_E_FIELDACCESS = EMAKEHR(0x1507)
    # MessageId: COR_E_FORMAT
    # MessageText:
    # The format of one arguments does not meet the contract of the method.
    COR_E_FORMAT = EMAKEHR(0x1537)
    # MessageId: COR_E_BADIMAGEFORMAT
    # MessageText:
    # The format of DLL or executable being loaded is invalid.
    COR_E_BADIMAGEFORMAT = _HRESULT_TYPEDEF_(0x8007000B)
    # MessageId: COR_E_ASSEMBLYEXPECTED
    # MessageText:
    # The module was expected to contain an assembly manifest.
    COR_E_ASSEMBLYEXPECTED = EMAKEHR(0x1018)
    # MessageId: COR_E_TYPEUNLOADED
    # MessageText:
    # The type had been unloaded.
    COR_E_TYPEUNLOADED = EMAKEHR(0x1013)
    # MessageId: COR_E_INDEXOUTOFRANGE
    # MessageText:
    # Attempted to access an element within an array by using an index that is
    # not within the bound of that array.
    COR_E_INDEXOUTOFRANGE = EMAKEHR(0x1508)
    # MessageId: COR_E_INSUFFICIENTMEMORY
    # MessageText:
    # Not enough memory was available for an operation.
    # This may not be potentially fatal (vs. an OutOfMemoryException).
    COR_E_INSUFFICIENTMEMORY = EMAKEHR(0x153D)
    # MessageId: COR_E_RUNTIMEWRAPPED
    # MessageText:
    # An object that does not derive from System.Exception has been wrapped in
    # a RuntimeWrappedException.
    COR_E_RUNTIMEWRAPPED = EMAKEHR(0x153E)
    # MessageId: COR_E_INVALIDCAST
    # MessageText:
    # Indicates a bad cast condition
    COR_E_INVALIDCAST = E_NOINTERFACE    # 0x80004002
    # MessageId: COR_E_INVALIDOPERATION
    # MessageText:
    # An operation is not legal in the current state.
    COR_E_INVALIDOPERATION = EMAKEHR(0x1509)
    # MessageId: COR_E_INVALIDPROGRAM
    # MessageText:
    # A program contained invalid IL or bad metadata. Usually this is a
    # compiler bug.
    COR_E_INVALIDPROGRAM = EMAKEHR(0x153A)
    # MessageId: COR_E_MEMBERACCESS
    # MessageText:
    # Access to this member is denied.
    COR_E_MEMBERACCESS = EMAKEHR(0x151A)
    # MessageId: COR_E_METHODACCESS
    # MessageText:
    # Access to this method is denied.
    COR_E_METHODACCESS = EMAKEHR(0x1510)
    # MessageId: COR_E_MISSINGFIELD
    # MessageText:
    # An attempt was made to dynamically access a field that does not exist.
    COR_E_MISSINGFIELD = EMAKEHR(0x1511)
    # MessageId: COR_E_MISSINGMANIFESTRESOURCE
    # MessageText:
    # An expected resource in the assembly manifest was missing.
    COR_E_MISSINGMANIFESTRESOURCE = EMAKEHR(0x1532)
    # MessageId: COR_E_MISSINGMEMBER
    # MessageText:
    # An attempt was made to dynamically invoke or access a field or method
    # that does not exist.
    COR_E_MISSINGMEMBER = EMAKEHR(0x1512)
    # MessageId: COR_E_MISSINGMETHOD
    # MessageText:
    # An attempt was made to dynamically invoke a method that does not exist
    COR_E_MISSINGMETHOD = EMAKEHR(0x1513)
    # MessageId: COR_E_MISSINGSATELLITEASSEMBLY
    # MessageText:
    # An expected satellite assembly containing the ultimate fallback resources
    # for a given culture was not found or couldn't be loaded. Setup problem?
    COR_E_MISSINGSATELLITEASSEMBLY = EMAKEHR(0x1536)
    # MessageId: COR_E_MULTICASTNOTSUPPORTED
    # MessageText:
    # Attempted to combine delegates that are not multicast
    COR_E_MULTICASTNOTSUPPORTED = EMAKEHR(0x1514)
    # MessageId: COR_E_NOTFINITENUMBER
    # MessageText:
    # Thrown if value (a floating point number) is either the not a number
    # value (NaN) or + - infinity value
    # VB needs this stuff
    COR_E_NOTFINITENUMBER = EMAKEHR(0x1528)
    # MessageId: COR_E_DUPLICATEWAITOBJECT
    # MessageText:
    # An object appears more than once in the wait objects array.
    COR_E_DUPLICATEWAITOBJECT = EMAKEHR(0x1529)
    # MessageId: COR_E_PLATFORMNOTSUPPORTED
    # MessageText:
    # The method is not supported on this platform
    COR_E_PLATFORMNOTSUPPORTED = EMAKEHR(0x1539)
    # MessageId: COR_E_NOTSUPPORTED
    # MessageText:
    # The operation is not supported
    COR_E_NOTSUPPORTED = EMAKEHR(0x1515)
    # MessageId: COR_E_NULLREFERENCE
    # MessageText:
    # Dereferencing a null reference. In general class libraries should not
    # throw this
    COR_E_NULLREFERENCE = E_POINTER    # 0x80004003
    # MessageId: COR_E_OUTOFMEMORY
    # MessageText:
    # The EE thows this exception when no more memory is avaible to continue
    # execution
    COR_E_OUTOFMEMORY = E_OUTOFMEMORY    # 0x8007000E
    # MessageId: COR_E_OVERFLOW
    # MessageText:
    # An arithmetic, casting, or conversion operation overflowed or
    # underflowed.
    COR_E_OVERFLOW = EMAKEHR(0x1516)
    # MessageId: COR_E_RANK
    # MessageText:
    # An array has the wrong number of dimensions for a particular operation.
    COR_E_RANK = EMAKEHR(0x1517)
    # MessageId: COR_E_REMOTING
    # MessageText:
    # An error relating to remoting occurred.
    COR_E_REMOTING = EMAKEHR(0x150B)
    COR_E_SERVER = EMAKEHR(0x150E)
    # MessageId: COR_E_SERVICEDCOMPONENT
    # MessageText:
    # An error relating to ServicedComponent occurred.
    COR_E_SERVICEDCOMPONENT = EMAKEHR(0x150F)
    # MessageId: COR_E_SECURITY
    # MessageText:
    # An error relating to security occured.
    COR_E_SECURITY = EMAKEHR(0x150A)
    # MessageID: COR_E_SERIALIZATION
    # MessageText:
    # An error relating to serialization has occurred.
    COR_E_SERIALIZATION = EMAKEHR(0x150C)
    # MessageId: COR_E_STACKOVERFLOW
    # MessageText:
    # Is raised by the EE when the execution stack overflows as it is
    # attempting to ex
    COR_E_STACKOVERFLOW = HRESULT_FROM_WIN32(ERROR_STACK_OVERFLOW)    # 0x800703E9
    # MessageId: COR_E_SYNCHRONIZATIONLOCK
    # MessageText:
    # Wait(), Notify() or NotifyAll() was called from an unsynchronized **
    # block of c
    COR_E_SYNCHRONIZATIONLOCK = EMAKEHR(0x1518)
    # MessageId: COR_E_SYSTEM
    # MessageText:
    # The base class for the runtime's "less serious" exceptions
    COR_E_SYSTEM = EMAKEHR(0x1501)
    # MessageId: COR_E_THREADABORTED
    # MessageText:
    # Thrown into a thread to cause it to abort. Not catchable.
    COR_E_THREADABORTED = EMAKEHR(0x1530)
    # MessageId: COR_E_OPERATIONCANCELED
    # MessageText:
    # The operation was cancelled.
    COR_E_OPERATIONCANCELED = EMAKEHR(0x153B)
    # MessageId: COR_E_THREADINTERRUPTED
    # MessageText:
    # Indicates that the thread was interrupted from a waiting state
    COR_E_THREADINTERRUPTED = EMAKEHR(0x1519)
    # MessageId: COR_E_THREADSTATE
    # MessageText:
    # Indicate that the Thread class is in an invalid state for the method call
    COR_E_THREADSTATE = EMAKEHR(0x1520)
    # MessageId: COR_E_THREADSTOP
    # MessageText:
    # Thrown into a thread to cause it to stop. This exception is typically
    # not caught
    COR_E_THREADSTOP = EMAKEHR(0x1521)
    # MessageId: COR_E_THREADSTART
    # MessageText:
    # Indicate that a user thread fails to start.
    COR_E_THREADSTART = EMAKEHR(0x1525)
    # MessageId: COR_E_TYPEINITIALIZATION
    # MessageText:
    # An exception was thrown by a type's initializer (.cctor).
    COR_E_TYPEINITIALIZATION = EMAKEHR(0x1534)
    # MessageId: COR_E_TYPELOAD
    # MessageText:
    # Could not find or load a specific type (class, enum, etc).
    COR_E_TYPELOAD = EMAKEHR(0x1522)
    # MessageId: COR_E_ENTRYPOINTNOTFOUND
    # MessageText:
    # Could not find the specified DllImport entry point
    COR_E_ENTRYPOINTNOTFOUND = EMAKEHR(0x1523)
    # MessageId: COR_E_DLLNOTFOUND
    # MessageText:
    # Could not find the specified DllImport DLL.
    COR_E_DLLNOTFOUND = EMAKEHR(0x1524)
    # MessageId: COR_E_UNAUTHORIZEDACCESS
    # MessageText:
    # Access is denied.
    COR_E_UNAUTHORIZEDACCESS = E_ACCESSDENIED    # 0x80070005
    # MessageId: COR_E_VERIFICATION
    # MessageText:
    # A verification failure occurred
    COR_E_VERIFICATION = EMAKEHR(0x150D)
    # MessageId: COR_E_INVALIDCOMOBJECT
    # MessageText:
    # An invalid __ComObject has been used.
    COR_E_INVALIDCOMOBJECT = EMAKEHR(0x1527)
    # MessageId: COR_E_SEMAPHOREFULL
    # MessageText:
    # Adding the given count to the semaphore would cause it to exceed its
    # maximum count.
    COR_E_SEMAPHOREFULL = EMAKEHR(0x152B)
    # MessageId: COR_E_WAITHANDLECANNOTBEOPENED
    # MessageText:
    # No Semaphore of the given name exists.
    COR_E_WAITHANDLECANNOTBEOPENED = EMAKEHR(0x152C)
    # MessageId: COR_E_ABANDONEDMUTEX
    # MessageText:
    # The wait completed due to an abandoned mutex.
    COR_E_ABANDONEDMUTEX = EMAKEHR(0x152D)
    # MessageId: COR_E_MARSHALDIRECTIVE
    # MessageText:
    # The marshaling directives are invalid.
    COR_E_MARSHALDIRECTIVE = EMAKEHR(0x1535)
    # MessageId: COR_E_INVALIDOLEVARIANTTYPE
    # MessageText:
    # The type of an OLE variant that was passed into the runtime is invalid.
    COR_E_INVALIDOLEVARIANTTYPE = EMAKEHR(0x1531)
    # MessageId: COR_E_SAFEARRAYTYPEMISMATCH
    # MessageText:
    # A mismatch has occured between the runtime type of the array and the
    # sub type recorded in the metadata.
    COR_E_SAFEARRAYTYPEMISMATCH = EMAKEHR(0x1533)
    # MessageId: COR_E_SAFEARRAYRANKMISMATCH
    # MessageText:
    # A mismatch has occured between the runtime rank of the array and the
    # rank recorded in the metadata.
    COR_E_SAFEARRAYRANKMISMATCH = EMAKEHR(0x1538)
    # MessageId: COR_E_DATAMISALIGNED
    # MessageText:
    # A datatype misalignment was detected in a load or store instruction.
    COR_E_DATAMISALIGNED = EMAKEHR(0x1541)
    # MessageId: COR_E_TARGETPARAMCOUNT
    # MessageText:
    # There was a mismatch between number of arguments provided and the number
    # expected
    COR_E_TARGETPARAMCOUNT = _HRESULT_TYPEDEF_(0x8002000E)    # DISP_E_BADPARAMCOUNT
    # MessageId: COR_E_AMBIGUOUSMATCH
    # MessageText:
    # While late binding to a method via reflection, could not resolve between
    # multiple overloads of a method.
    COR_E_AMBIGUOUSMATCH = _HRESULT_TYPEDEF_(0x8000211D)
    # MessageId: COR_E_INVALIDFILTERCRITERIA
    # MessageText:
    # The given filter criteria does not match the filter contract.
    COR_E_INVALIDFILTERCRITERIA = EMAKEHR(0x1601)
    # MessageId: COR_E_REFLECTIONTYPELOAD
    # MessageText:
    # Could not find or load a specific class that was requested through
    # Reflection
    COR_E_REFLECTIONTYPELOAD = EMAKEHR(0x1602)
    # MessageId: COR_E_TARGET
    # MessageText:
    # - If you attempt to invoke a non-static method with a null Object - If
    # you atte
    COR_E_TARGET = EMAKEHR(0x1603)
    # MessageId: COR_E_TARGETINVOCATION
    # MessageText:
    # If the method called throws an exception
    COR_E_TARGETINVOCATION = EMAKEHR(0x1604)
    # MessageId: COR_E_CUSTOMATTRIBUTEFORMAT
    # MessageText:
    # If the binary format of a custom attribute is invalid.
    COR_E_CUSTOMATTRIBUTEFORMAT = EMAKEHR(0x1605)
    # MessageId: COR_E_ENDOFSTREAM
    # MessageText:
    # Thrown when the End of file is reached
    COR_E_ENDOFSTREAM = HRESULT_FROM_WIN32(ERROR_HANDLE_EOF)
    # MessageId: COR_E_FILELOAD
    # MessageText:
    COR_E_FILELOAD = EMAKEHR(0x1621)
    # MessageId: COR_E_FILENOTFOUND
    # MessageText:
    COR_E_FILENOTFOUND = HRESULT_FROM_WIN32(ERROR_FILE_NOT_FOUND)
    # MessageId: ERROR_BAD_PATHNAME
    # MessageText:
    # The specified path is invalid.
    COR_E_BAD_PATHNAME = HRESULT_FROM_WIN32(ERROR_BAD_PATHNAME)
    # MessageId: COR_E_IO
    # MessageText:
    # Some sort of I/O error.
    COR_E_IO = EMAKEHR(0x1620)
    # MessageId: COR_E_DIRECTORYNOTFOUND
    # MessageText:
    # The specified path couldn't be found.
    COR_E_DIRECTORYNOTFOUND = HRESULT_FROM_WIN32(ERROR_PATH_NOT_FOUND)
    # MessageId: COR_E_PATHTOOLONG
    # MessageText:
    # The specified path was too long.
    COR_E_PATHTOOLONG = HRESULT_FROM_WIN32(ERROR_FILENAME_EXCED_RANGE)
    # MessageId: COR_E_OBJECTDISPOSED
    # MessageText:
    # The object has already been disposed.
    COR_E_OBJECTDISPOSED = EMAKEHR(0x1622)
    # MessageId: COR_E_FAILFAST
    # MessageText:
    # Runtime operation halted by call to System.Environment.FailFast().
    COR_E_FAILFAST = EMAKEHR(0x1623)
    # MessageId: COR_E_HOSTPROTECTION
    # MessageText:
    # Attempted to perform an operation that was forbidden by the host.
    COR_E_HOSTPROTECTION = EMAKEHR(0x1640)
    # MessageId: COR_E_ILLEGAL_REENTRANCY
    # MessageText:
    # Attempted to call into managed code when executing inside a low level
    # extensibility point.
    COR_E_ILLEGAL_REENTRANCY = EMAKEHR(0x1641)
    # *** Shim errors 1700 - 1750
    CLR_E_SHIM_RUNTIMELOAD = EMAKEHR(0x1700)    # Failed to load the runtime
    CLR_E_SHIM_RUNTIMEEXPORT = EMAKEHR(0x1701)    # Failed to find a required export in the runtime
    CLR_E_SHIM_INSTALLROOT = EMAKEHR(0x1702)    # Install root is not defined
    CLR_E_SHIM_INSTALLCOMP = EMAKEHR(0x1703)    # Expected component of the runtime is not available
    # *** Verifier Errors 1800 - 18FF
    # See src/dlls/mscorrc/mscorrc.rc for a description of each error
    VER_E_HRESULT = EMAKEHR(0x1801)
    VER_E_OFFSET = EMAKEHR(0x1802)
    VER_E_OPCODE = EMAKEHR(0x1803)
    VER_E_OPERAND = EMAKEHR(0x1804)
    VER_E_TOKEN = EMAKEHR(0x1805)
    VER_E_EXCEPT = EMAKEHR(0x1806)
    VER_E_STACK_SLOT = EMAKEHR(0x1807)
    VER_E_LOC = EMAKEHR(0x1808)
    VER_E_ARG = EMAKEHR(0x1809)
    VER_E_FOUND = EMAKEHR(0x180A)
    VER_E_EXPECTED = EMAKEHR(0x180B)
    VER_E_LOC_BYNAME = EMAKEHR(0x180C)
    VER_E_UNKNOWN_OPCODE = EMAKEHR(0x1810)
    VER_E_SIG_CALLCONV = EMAKEHR(0x1811)
    VER_E_SIG_ELEMTYPE = EMAKEHR(0x1812)
    VER_E_RET_SIG = EMAKEHR(0x1814)
    VER_E_FIELD_SIG = EMAKEHR(0x1815)
    VER_E_INTERNAL = EMAKEHR(0x1818)
    VER_E_STACK_TOO_LARGE = EMAKEHR(0x1819)
    VER_E_ARRAY_NAME_LONG = EMAKEHR(0x181A)
    VER_E_FALLTHRU = EMAKEHR(0x1820)
    VER_E_TRY_GTEQ_END = EMAKEHR(0x1821)
    VER_E_TRYEND_GT_CS = EMAKEHR(0x1822)
    VER_E_HND_GTEQ_END = EMAKEHR(0x1823)
    VER_E_HNDEND_GT_CS = EMAKEHR(0x1824)
    VER_E_FLT_GTEQ_CS = EMAKEHR(0x1825)
    VER_E_TRY_START = EMAKEHR(0x1826)
    VER_E_HND_START = EMAKEHR(0x1827)
    VER_E_FLT_START = EMAKEHR(0x1828)
    VER_E_TRY_OVERLAP = EMAKEHR(0x1829)
    VER_E_TRY_EQ_HND_FIL = EMAKEHR(0x182A)
    VER_E_TRY_SHARE_FIN_FAL = EMAKEHR(0x182B)
    VER_E_HND_OVERLAP = EMAKEHR(0x182C)
    VER_E_HND_EQ = EMAKEHR(0x182D)
    VER_E_FIL_OVERLAP = EMAKEHR(0x182E)
    VER_E_FIL_EQ = EMAKEHR(0x182F)
    VER_E_FIL_CONT_TRY = EMAKEHR(0x1830)
    VER_E_FIL_CONT_HND = EMAKEHR(0x1831)
    VER_E_FIL_CONT_FIL = EMAKEHR(0x1832)
    VER_E_FIL_GTEQ_CS = EMAKEHR(0x1833)
    VER_E_FIL_START = EMAKEHR(0x1834)
    VER_E_FALLTHRU_EXCEP = EMAKEHR(0x1835)
    VER_E_FALLTHRU_INTO_HND = EMAKEHR(0x1836)
    VER_E_FALLTHRU_INTO_FIL = EMAKEHR(0x1837)
    VER_E_LEAVE = EMAKEHR(0x1838)
    VER_E_RETHROW = EMAKEHR(0x1839)
    VER_E_ENDFINALLY = EMAKEHR(0x183A)
    VER_E_ENDFILTER = EMAKEHR(0x183B)
    VER_E_ENDFILTER_MISSING = EMAKEHR(0x183C)
    VER_E_BR_INTO_TRY = EMAKEHR(0x183D)
    VER_E_BR_INTO_HND = EMAKEHR(0x183E)
    VER_E_BR_INTO_FIL = EMAKEHR(0x183F)
    VER_E_BR_OUTOF_TRY = EMAKEHR(0x1840)
    VER_E_BR_OUTOF_HND = EMAKEHR(0x1841)
    VER_E_BR_OUTOF_FIL = EMAKEHR(0x1842)
    VER_E_BR_OUTOF_FIN = EMAKEHR(0x1843)
    VER_E_RET_FROM_TRY = EMAKEHR(0x1844)
    VER_E_RET_FROM_HND = EMAKEHR(0x1845)
    VER_E_RET_FROM_FIL = EMAKEHR(0x1846)
    VER_E_BAD_JMP_TARGET = EMAKEHR(0x1847)
    VER_E_PATH_LOC = EMAKEHR(0x1848)
    VER_E_PATH_THIS = EMAKEHR(0x1849)
    VER_E_PATH_STACK = EMAKEHR(0x184A)
    VER_E_PATH_STACK_DEPTH = EMAKEHR(0x184B)
    VER_E_THIS = EMAKEHR(0x184C)
    VER_E_THIS_UNINIT_EXCEP = EMAKEHR(0x184D)
    VER_E_THIS_UNINIT_STORE = EMAKEHR(0x184E)
    VER_E_THIS_UNINIT_RET = EMAKEHR(0x184F)
    VER_E_THIS_UNINIT_V_RET = EMAKEHR(0x1850)
    VER_E_THIS_UNINIT_BR = EMAKEHR(0x1851)
    VER_E_LDFTN_CTOR = EMAKEHR(0x1852)
    VER_E_STACK_NOT_EQ = EMAKEHR(0x1853)
    VER_E_STACK_UNEXPECTED = EMAKEHR(0x1854)
    VER_E_STACK_EXCEPTION = EMAKEHR(0x1855)
    VER_E_STACK_OVERFLOW = EMAKEHR(0x1856)
    VER_E_STACK_UNDERFLOW = EMAKEHR(0x1857)
    VER_E_STACK_EMPTY = EMAKEHR(0x1858)
    VER_E_STACK_UNINIT = EMAKEHR(0x1859)
    VER_E_STACK_I_I4_I8 = EMAKEHR(0x185A)
    VER_E_STACK_R_R4_R8 = EMAKEHR(0x185B)
    VER_E_STACK_NO_R_I8 = EMAKEHR(0x185C)
    VER_E_STACK_NUMERIC = EMAKEHR(0x185D)
    VER_E_STACK_OBJREF = EMAKEHR(0x185E)
    VER_E_STACK_P_OBJREF = EMAKEHR(0x185F)
    VER_E_STACK_BYREF = EMAKEHR(0x1860)
    VER_E_STACK_METHOD = EMAKEHR(0x1861)
    VER_E_STACK_ARRAY_SD = EMAKEHR(0x1862)
    VER_E_STACK_VALCLASS = EMAKEHR(0x1863)
    VER_E_STACK_P_VALCLASS = EMAKEHR(0x1864)
    VER_E_STACK_NO_VALCLASS = EMAKEHR(0x1865)
    VER_E_LOC_DEAD = EMAKEHR(0x1866)
    VER_E_LOC_NUM = EMAKEHR(0x1867)
    VER_E_ARG_NUM = EMAKEHR(0x1868)
    VER_E_TOKEN_RESOLVE = EMAKEHR(0x1869)
    VER_E_TOKEN_TYPE = EMAKEHR(0x186A)
    VER_E_TOKEN_TYPE_MEMBER = EMAKEHR(0x186B)
    VER_E_TOKEN_TYPE_FIELD = EMAKEHR(0x186C)
    VER_E_TOKEN_TYPE_SIG = EMAKEHR(0x186D)
    VER_E_UNVERIFIABLE = EMAKEHR(0x186E)
    VER_E_LDSTR_OPERAND = EMAKEHR(0x186F)
    VER_E_RET_PTR_TO_STACK = EMAKEHR(0x1870)
    VER_E_RET_VOID = EMAKEHR(0x1871)
    VER_E_RET_MISSING = EMAKEHR(0x1872)
    VER_E_RET_EMPTY = EMAKEHR(0x1873)
    VER_E_RET_UNINIT = EMAKEHR(0x1874)
    VER_E_ARRAY_ACCESS = EMAKEHR(0x1875)
    VER_E_ARRAY_V_STORE = EMAKEHR(0x1876)
    VER_E_ARRAY_SD = EMAKEHR(0x1877)
    VER_E_ARRAY_SD_PTR = EMAKEHR(0x1878)
    VER_E_ARRAY_FIELD = EMAKEHR(0x1879)
    VER_E_ARGLIST = EMAKEHR(0x187A)
    VER_E_VALCLASS = EMAKEHR(0x187B)
    VER_E_METHOD_ACCESS = EMAKEHR(0x187C)
    VER_E_FIELD_ACCESS = EMAKEHR(0x187D)
    VER_E_DEAD = EMAKEHR(0x187E)
    VER_E_FIELD_STATIC = EMAKEHR(0x187F)
    VER_E_FIELD_NO_STATIC = EMAKEHR(0x1880)
    VER_E_ADDR = EMAKEHR(0x1881)
    VER_E_ADDR_BYREF = EMAKEHR(0x1882)
    VER_E_ADDR_LITERAL = EMAKEHR(0x1883)
    VER_E_INITONLY = EMAKEHR(0x1884)
    VER_E_THROW = EMAKEHR(0x1885)
    VER_E_CALLVIRT_VALCLASS = EMAKEHR(0x1886)
    VER_E_CALL_SIG = EMAKEHR(0x1887)
    VER_E_CALL_STATIC = EMAKEHR(0x1888)
    VER_E_CTOR = EMAKEHR(0x1889)
    VER_E_CTOR_VIRT = EMAKEHR(0x188A)
    VER_E_CTOR_OR_SUPER = EMAKEHR(0x188B)
    VER_E_CTOR_MUL_INIT = EMAKEHR(0x188C)
    VER_E_SIG = EMAKEHR(0x188D)
    VER_E_SIG_ARRAY = EMAKEHR(0x188E)
    VER_E_SIG_ARRAY_PTR = EMAKEHR(0x188F)
    VER_E_SIG_ARRAY_BYREF = EMAKEHR(0x1890)
    VER_E_SIG_ELEM_PTR = EMAKEHR(0x1891)
    VER_E_SIG_VARARG = EMAKEHR(0x1892)
    VER_E_SIG_VOID = EMAKEHR(0x1893)
    VER_E_SIG_BYREF_BYREF = EMAKEHR(0x1894)
    VER_E_CODE_SIZE_ZERO = EMAKEHR(0x1896)
    VER_E_BAD_VARARG = EMAKEHR(0x1897)
    VER_E_TAIL_CALL = EMAKEHR(0x1898)
    VER_E_TAIL_BYREF = EMAKEHR(0x1899)
    VER_E_TAIL_RET = EMAKEHR(0x189A)
    VER_E_TAIL_RET_VOID = EMAKEHR(0x189B)
    VER_E_TAIL_RET_TYPE = EMAKEHR(0x189C)
    VER_E_TAIL_STACK_EMPTY = EMAKEHR(0x189D)
    VER_E_METHOD_END = EMAKEHR(0x189E)
    VER_E_BAD_BRANCH = EMAKEHR(0x189F)
    VER_E_FIN_OVERLAP = EMAKEHR(0x18A0)
    VER_E_LEXICAL_NESTING = EMAKEHR(0x18A1)
    VER_E_VOLATILE = EMAKEHR(0x18A2)
    VER_E_UNALIGNED = EMAKEHR(0x18A3)
    VER_E_INNERMOST_FIRST = EMAKEHR(0x18A4)
    VER_E_CALLI_VIRTUAL = EMAKEHR(0x18A5)
    VER_E_CALL_ABSTRACT = EMAKEHR(0x18A6)
    VER_E_STACK_UNEXP_ARRAY = EMAKEHR(0x18A7)
    VER_E_NOT_IN_GC_HEAP = EMAKEHR(0x18A8)
    VER_E_TRY_N_EMPTY_STACK = EMAKEHR(0x18A9)
    VER_E_DLGT_CTOR = EMAKEHR(0x18AA)
    VER_E_DLGT_BB = EMAKEHR(0x18AB)
    VER_E_DLGT_PATTERN = EMAKEHR(0x18AC)
    VER_E_DLGT_LDFTN = EMAKEHR(0x18AD)
    VER_E_FTN_ABSTRACT = EMAKEHR(0x18AE)
    VER_E_SIG_C_VC = EMAKEHR(0x18AF)
    VER_E_SIG_VC_C = EMAKEHR(0x18B0)
    VER_E_BOX_PTR_TO_STACK = EMAKEHR(0x18B1)
    VER_E_SIG_BYREF_TB_AH = EMAKEHR(0x18B2)
    VER_E_SIG_ARRAY_TB_AH = EMAKEHR(0x18B3)
    VER_E_ENDFILTER_STACK = EMAKEHR(0x18B4)
    VER_E_DLGT_SIG_I = EMAKEHR(0x18B5)
    VER_E_DLGT_SIG_O = EMAKEHR(0x18B6)
    VER_E_RA_PTR_TO_STACK = EMAKEHR(0x18B7)
    VER_E_CATCH_VALUE_TYPE = EMAKEHR(0x18B8)
    VER_E_CATCH_BYREF = EMAKEHR(0x18B9)
    VER_E_FIL_PRECEED_HND = EMAKEHR(0x18BA)
    VER_E_LDVIRTFTN_STATIC = EMAKEHR(0x18BB)
    VER_E_CALLVIRT_STATIC = EMAKEHR(0x18BC)
    VER_E_INITLOCALS = EMAKEHR(0x18BD)
    VER_E_BR_TO_EXCEPTION = EMAKEHR(0x18BE)
    VER_E_CALL_CTOR = EMAKEHR(0x18BF)
    # @GENERICSVER: new generics related error messages
    VER_E_VALCLASS_OBJREF_VAR = EMAKEHR(0x18C0)
    VER_E_STACK_P_VALCLASS_OBJREF_VAR = EMAKEHR(0x18C1)
    VER_E_SIG_VAR_PARAM = EMAKEHR(0x18C2)
    VER_E_SIG_MVAR_PARAM = EMAKEHR(0x18C3)
    VER_E_SIG_VAR_ARG = EMAKEHR(0x18C4)
    VER_E_SIG_MVAR_ARG = EMAKEHR(0x18C5)
    VER_E_SIG_GENERICINST = EMAKEHR(0x18C6)
    VER_E_SIG_METHOD_INST = EMAKEHR(0x18C7)
    VER_E_SIG_METHOD_PARENT_INST = EMAKEHR(0x18C8)
    VER_E_SIG_FIELD_PARENT_INST = EMAKEHR(0x18C9)
    VER_E_CALLCONV_NOT_GENERICINST = EMAKEHR(0x18CA)
    VER_E_TOKEN_BAD_METHOD_SPEC = EMAKEHR(0x18CB)
    VER_E_BAD_READONLY_PREFIX = EMAKEHR(0x18CC)
    VER_E_BAD_CONSTRAINED_PREFIX = EMAKEHR(0x18CD)
    # these two are actually raised by the EE - should they appear elsewhere?
    VER_E_CIRCULAR_VAR_CONSTRAINTS = EMAKEHR(0x18CE)
    VER_E_CIRCULAR_MVAR_CONSTRAINTS = EMAKEHR(0x18CF)
    # these are used by the new peverify
    VER_E_UNSATISFIED_METHOD_INST = EMAKEHR(0x18D0)
    VER_E_UNSATISFIED_METHOD_PARENT_INST = EMAKEHR(0x18D1)
    VER_E_UNSATISFIED_FIELD_PARENT_INST = EMAKEHR(0x18D2)
    VER_E_UNSATISFIED_BOX_OPERAND = EMAKEHR(0x18D3)
    VER_E_CONSTRAINED_CALL_WITH_NON_BYREF_THIS = EMAKEHR(0x18D4)
    VER_E_CONSTRAINED_OF_NON_VARIABLE_TYPE = EMAKEHR(0x18D5)
    VER_E_READONLY_UNEXPECTED_CALLEE = EMAKEHR(0x18D6)
    VER_E_READONLY_ILLEGAL_WRITE = EMAKEHR(0x18D7)
    VER_E_READONLY_IN_MKREFANY = EMAKEHR(0x18D8)
    VER_E_UNALIGNED_ALIGNMENT = EMAKEHR(0x18D9)
    VER_E_TAILCALL_INSIDE_EH = EMAKEHR(0x18DA)
    VER_E_BACKWARD_BRANCH = EMAKEHR(0x18DB)
    VER_E_CALL_TO_VTYPE_BASE = EMAKEHR(0x18DC)
    VER_E_NEWOBJ_OF_ABSTRACT_CLASS = EMAKEHR(0x18DD)
    VER_E_UNMANAGED_POINTER = EMAKEHR(0x18DE)
    VER_E_LDFTN_NON_FINAL_VIRTUAL = EMAKEHR(0x18DF)
    VER_E_FIELD_OVERLAP = EMAKEHR(0x18E0)
    VER_E_THIS_MISMATCH = EMAKEHR(0x18E1)
    VER_E_STACK_I_I4 = EMAKEHR(0x18E2)
    VER_E_BAD_PE = EMAKEHR(0x18F0)
    VER_E_BAD_MD = EMAKEHR(0x18F1)
    VER_E_BAD_APPDOMAIN = EMAKEHR(0x18F2)
    VER_E_TYPELOAD = EMAKEHR(0x18F3)
    VER_E_PE_LOAD = EMAKEHR(0x18F4)
    VER_E_WRITE_RVA_STATIC = EMAKEHR(0x18F5)
    # ATTENTION: Range 0x1900 - 0x1AFF is reserved for Framework errors
    # Range 0x1B00 - 0x1BFF is reserved for MD Validator errors
    # (see above VLDTR_E_...)
    # System.Xml
    COR_E_Xml = EMAKEHR(0x1940)
    COR_E_XmlSchema = EMAKEHR(0x1941)
    COR_E_XmlXslt = EMAKEHR(0x1942)
    COR_E_XmlXPath = EMAKEHR(0x1943)
    COR_E_XmlQuery = EMAKEHR(0x1944)
    # System.Data DataSet
    COR_E_Data = EMAKEHR(0x1920)
    COR_E_DataDeletedRowInaccessible = EMAKEHR(0x1921)
    COR_E_DataDuplicateName = EMAKEHR(0x1922)
    COR_E_DataInRowChangingEvent = EMAKEHR(0x1923)
    COR_E_DataInvalidConstraint = EMAKEHR(0x1924)
    COR_E_DataMissingPrimaryKey = EMAKEHR(0x1925)
    COR_E_DataNoNullAllowed = EMAKEHR(0x1926)
    COR_E_DataReadOnly = EMAKEHR(0x1927)
    COR_E_DataRowNotInTable = EMAKEHR(0x1928)
    COR_E_DataVersionNotFound = EMAKEHR(0x1929)
    COR_E_DataConstraint = EMAKEHR(0x192A)
    COR_E_StrongTyping = EMAKEHR(0x192B)
    # System.Data Managed Providers
    COR_E_SqlType = EMAKEHR(0x1930)
    COR_E_SqlNullValue = EMAKEHR(0x1931)
    COR_E_SqlTruncate = EMAKEHR(0x1932)
    COR_E_AdapterMapping = EMAKEHR(0x1933)
    COR_E_DataAdapter = EMAKEHR(0x1934)
    COR_E_DBConcurrency = EMAKEHR(0x1935)
    COR_E_OperationAborted = EMAKEHR(0x1936)
    COR_E_InvalidUdt = EMAKEHR(0x1937)
    COR_E_SqlException = EMAKEHR(0x1904)    # System.Data.SqlClient.SqlClientException
    COR_E_OdbcException = EMAKEHR(0x1937)    # System.Data.Odbc.OdbcException
    COR_E_OracleException = EMAKEHR(0x1938)    # System.Data.OracleClient.OracleException
    # *** More debugger error 1C00 - 1CFF
    # Thread is not scheduled. Thus we may not have OSThreadId, handle, or
    # context
    CORDBG_E_THREAD_NOT_SCHEDULED = EMAKEHR(0x1C00)
    CORDBG_E_HANDLE_HAS_BEEN_DISPOSED = EMAKEHR(0x1C01)    # Handle has been disposed.
    CORDBG_E_NONINTERCEPTABLE_EXCEPTION = EMAKEHR(0x1C02)    # Cant intercept this exception.
    CORDBG_E_CANT_UNWIND_ABOVE_CALLBACK = EMAKEHR(0x1C03)    # When intercepting an exception, cannot intercept above the current frame.
    CORDBG_E_INTERCEPT_FRAME_ALREADY_SET = EMAKEHR(0x1C04)    # The intercept frame for this exception has already been set.
    CORDBG_E_NO_NATIVE_PATCH_AT_ADDR = EMAKEHR(0x1C05)    # there's no native patch at the given address.
    CORDBG_E_NATIVE_PATCH_ALREADY_AT_ADDR = EMAKEHR(0x1C07)    # There's already a native patch at the address
    CORDBG_E_TIMEOUT = EMAKEHR(0x1C08)    # a wait timed out .. likely an indication of deadlock.
    CORDBG_E_CANT_CALL_ON_THIS_THREAD = EMAKEHR(0x1C09)    # Can't use the API on this thread.
    CORDBG_E_ENC_INFOLESS_METHOD = EMAKEHR(0x1C0A)    # Method was not JITed in EnC mode
    CORDBG_E_ENC_NESTED_HANLDERS = EMAKEHR(0x1C0B)    # Frame cant be updated due to change in max nesting of handlers
    CORDBG_E_ENC_IN_FUNCLET = EMAKEHR(0x1C0C)    # Method is in a callable handler/filter. Cant grow stack
    CORDBG_E_ENC_LOCALLOC = EMAKEHR(0x1C0D)    # Frame cant be updated due to localloc
    CORDBG_E_ENC_EDIT_NOT_SUPPORTED = EMAKEHR(0x1C0E)    # Attempt to perform unsupported edit
    CORDBG_E_FEABORT_DELAYED_UNTIL_THREAD_RESUMED = EMAKEHR(0x1C0F)    # Attempt to func eval abort on a suspended thread.
    CORDBG_E_NOTREADY = EMAKEHR(0x1C10)    # The LS is not in a good spot to perform the requested operation.
    # We failed to resolve assembly given an AssemblyRef token. Assembly may
    # be not loaded yet or not a valid token.
    CORDBG_E_CANNOT_RESOLVE_ASSEMBLY = EMAKEHR(0x1C11)
    CORDBG_E_MUST_BE_IN_LOAD_MODULE = EMAKEHR(0x1C12)    # Must be in context of LoadModule callback to perform requested operation
    CORDBG_E_CANNOT_BE_ON_ATTACH = EMAKEHR(0x1C13)    # Requested operation cannot be performed during an attach operation
    CORDBG_S_NOT_ALL_BITS_SET = SMAKEHR(0x1C13)    # Not all bits specified were successfully applied
    CORDBG_E_NGEN_NOT_SUPPORTED = EMAKEHR(0x1C14)    # NGEN must be supported to perform the requested operation
    CORDBG_E_ILLEGAL_SHUTDOWN_ORDER = EMAKEHR(0x1C15)    # Trying to shutdown out of order.
    CORDBG_E_CANNOT_DEBUG_FIBER_PROCESS = EMAKEHR(0x1C16)    # For Whidbey, we don't support debugging fiber mode managed process
    # Must be in context of CreateProcess callback to perform requested
    # operation
    CORDBG_E_MUST_BE_IN_CREATE_PROCESS = EMAKEHR(0x1C17)
    # All outstanding func-evals have not completed, detaching is not allowed
    # at this time.
    CORDBG_E_DETACH_FAILED_OUTSTANDING_EVALS = EMAKEHR(0x1C18)
    # All outstanding steppers have not been closed, detaching is not allowed
    # at this time.
    CORDBG_E_DETACH_FAILED_OUTSTANDING_STEPPERS = EMAKEHR(0x1C19)
    CORDBG_E_CANT_INTEROP_STEP_OUT = EMAKEHR(0x1C20)    # Can't have an ICorDebugStepper do a native step-out.
    # All outstanding breakpoints have not been closed, detaching is not
    # allowed at this time.
    CORDBG_E_DETACH_FAILED_OUTSTANDING_BREAKPOINTS = EMAKEHR(0x1C21)
    CORDBG_E_ILLEGAL_IN_STACK_OVERFLOW = EMAKEHR(0x1C22)    # the operation is illegal because of a stackoverflow.
    CORDBG_E_ILLEGAL_AT_GC_UNSAFE_POINT = EMAKEHR(0x1C23)    # The operation failed because it's a GC unsafe point.
    CORDBG_E_ILLEGAL_IN_PROLOG = EMAKEHR(0x1C24)    # The operation failed because the thread is in the prolog
    CORDBG_E_ILLEGAL_IN_NATIVE_CODE = EMAKEHR(0x1C25)    # The operation failed because the thread is in native code
    CORDBG_E_ILLEGAL_IN_OPTIMIZED_CODE = EMAKEHR(0x1C26)    # The operation failed because the thread is in optimized code.
    CORDBG_E_MINIDUMP_UNSUPPORTED = EMAKEHR(0x1C27)
    CORDBG_E_APPDOMAIN_MISMATCH = EMAKEHR(0x1C28)    # A supplied object or type belongs to the wrong AppDomain
    CORDBG_E_CONTEXT_UNVAILABLE = EMAKEHR(0x1C29)    # The thread's context is not available.
    # The operation failed because debuggee and debugger are on incompatible
    # platform
    CORDBG_E_UNCOMPATIBLE_PLATFORMS = EMAKEHR(0x1C30)
    CORDBG_E_DEBUGGING_DISABLED = EMAKEHR(0x1C31)    # The operation failed because the debugging has been disabled
    CORDBG_E_DETACH_FAILED_ON_ENC = EMAKEHR(0x1C32)    # Detach is illegal after a module has been EnCed.
    CORDBG_E_CURRENT_EXCEPTION_IS_OUTSIDE_CURRENT_EXECUTION_SCOPE = (
        EMAKEHR(0x1C33)
    )    # Interception of the current exception is not legal
    # Helper thread can not safely run code. The opereration may work at a
    # later time.
    CORDBG_E_HELPER_MAY_DEADLOCK = EMAKEHR(0x1C34)
    # *** PE Format validation errors 1D00 - 1DFF
    PEFMT_E_NO_CONTENTS = EMAKEHR(0x1D00)    # File is empty
    PEFMT_E_NO_NTHEADERS = EMAKEHR(0x1D01)    # File has no NT headers
    PEFMT_E_64BIT = EMAKEHR(0x1D02)    # File is PE32 +
    PEFMT_E_NO_CORHEADER = EMAKEHR(0x1D03)    # File has no COR header
    PEFMT_E_NOT_ILONLY = EMAKEHR(0x1D04)    # Flag IL_ONLY not set
    PEFMT_E_IMPORT_DLLS = EMAKEHR(0x1D05)    # Bad import DLLs
    PEFMT_E_EXE_NOENTRYPOINT = EMAKEHR(0x1D06)    # EXE file has no mgd entry point
    PEFMT_E_BASE_RELOCS = EMAKEHR(0x1D07)    # Bad base relocations
    PEFMT_E_ENTRYPOINT = EMAKEHR(0x1D08)    # Bad managed entry point
    PEFMT_E_ZERO_SIZEOFCODE = EMAKEHR(0x1D09)    # OptHeader.SizeOfCode == 0
    PEFMT_E_BAD_CORHEADER = EMAKEHR(0x1D0A)    # File has invalid COR header
    # *** CLR Optimization service 1E00 - 1EFF
    CLR_OPTSVC_E_CONTROLLER_INTERRUPT = EMAKEHR(0x1E00)    # Service controller interrupted work
    # *** CLR Optimization service 1F00 - 1FFF
    NGEN_FAILED_GET_DEPENDENCIES = EMAKEHR(0x1F00)    # Service manager failed to get ICorSvcDependencies interface
    NGEN_FAILED_NATIVE_IMAGE_DELETE = EMAKEHR(0x1F01)    # Failed to delete native image
# END IF   __COMMON_LANGUAGE_RUNTIME_HRESULTS__
