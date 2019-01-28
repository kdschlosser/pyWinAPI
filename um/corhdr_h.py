import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__CORHDR_H__ = None
MACROS_NOT_SUPPORTED = None
IMAGE_DIRECTORY_ENTRY_COMHEADER = None
__IMAGE_COR20_HEADER_DEFINED__ = None
_COR_FIELD_OFFSET_ = None
IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS = None
_CORSAVESIZE_DEFINED_ = None

class IMAGE_COR20_HEADER(ctypes.Structure):
    pass


PIMAGE_COR20_HEADER = POINTER(IMAGE_COR20_HEADER)


class IMAGE_COR_ILMETHOD_SECT_SMALL(ctypes.Structure):
    pass


class IMAGE_COR_ILMETHOD_SECT_FAT(ctypes.Structure):
    pass


class IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT(ctypes.Structure):
    pass


class IMAGE_COR_ILMETHOD_SECT_EH_FAT(ctypes.Structure):
    pass


class IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL(ctypes.Structure):
    pass


class IMAGE_COR_ILMETHOD_SECT_EH_SMALL(ctypes.Structure):
    pass


class IMAGE_COR_ILMETHOD_SECT_EH(ctypes.Union):
    pass


class IMAGE_COR_ILMETHOD_TINY(ctypes.Structure):
    pass


class IMAGE_COR_ILMETHOD_FAT(ctypes.Structure):
    pass


class IMAGE_COR_ILMETHOD(ctypes.Union):
    pass


class IMAGE_COR_NATIVE_DESCRIPTOR(ctypes.Structure):
    pass


class IMAGE_COR_X86_RUNTIME_FUNCTION_ENTRY(ctypes.Structure):
    pass


class IMAGE_COR_MIH_ENTRY(ctypes.Structure):
    pass


class IMAGE_COR_VTABLEFIXUP(ctypes.Structure):
    pass


class COR_FIELD_OFFSET(ctypes.Structure):
    pass


class IMAGE_COR_FIXUPENTRY(ctypes.Structure):
    pass


class COR_SECATTR(ctypes.Structure):
    pass


# == + + ==
# Copyright (c) Microsoft Corporation. All rights reserved.
# == -- ==
# ***************************************************************************
# *   ** * CorHdr.h - contains definitions for the Runtime structures, ** *
# needed to work with metadata. ** * **
# **************************************************************************
if not defined(__CORHDR_H__):
    __CORHDR_H__ = VOID
    FRAMEWORK_REGISTRY_KEY = "Software\\Microsoft\\.NETFramework"
    FRAMEWORK_REGISTRY_KEY_W = "Software\\Microsoft\\.NETFramework"
    if defined(_MSC_VER):
        pass
    # END IF

    # Obsolete; not used in the runtime.
    mdScope = LPVOID

    # Generic token
    mdToken = ULONG32

    # Token definitions
    # Module token (roughly, a scope)
    mdModule = mdToken

    # TypeRef reference (this or other scope)
    mdTypeRef = mdToken

    # TypeDef in this scope
    mdTypeDef = mdToken

    # Field in this scope
    mdFieldDef = mdToken

    # Method in this scope
    mdMethodDef = mdToken

    # param token
    mdParamDef = mdToken

    # interface implementation token
    mdInterfaceImpl = mdToken

    # MemberRef (this or other scope)
    mdMemberRef = mdToken

    # attribute token
    mdCustomAttribute = mdToken

    # DeclSecurity
    mdPermission = mdToken

    # Signature object
    mdSignature = mdToken

    # event token
    mdEvent = mdToken

    # property token
    mdProperty = mdToken

    # Module reference (for the imported modules)
    mdModuleRef = mdToken

    # Assembly tokens.
    # Assembly token.
    mdAssembly = mdToken

    # AssemblyRef token.
    mdAssemblyRef = mdToken

    # File token.
    mdFile = mdToken

    # ExportedType token.
    mdExportedType = mdToken

    # ManifestResource token.
    mdManifestResource = mdToken

    # TypeSpec object
    mdTypeSpec = mdToken

    # formal parameter to generic type or method
    mdGenericParam = mdToken

    # instantiation of a generic method
    mdMethodSpec = mdToken

    # constraint on a formal generic parameter
    mdGenericParamConstraint = mdToken

    # Application string.
    # User literal string token.
    mdString = mdToken

    # constantpool token
    mdCPToken = mdToken
    if not defined(MACROS_NOT_SUPPORTED):
        RID = ULONG
    else:
        RID = UINT
    # END IF   MACROS_NOT_SUPPORTED


    class ReplacesGeneralNumericDefines(ENUM):
            if not defined(IMAGE_DIRECTORY_ENTRY_COMHEADER):
                IMAGE_DIRECTORY_ENTRY_COMHEADER = 14
            # END IF

            _NEW_FLAGS_IMPLEMENTED = 1
            __NEW_FLAGS_IMPLEMENTED = 1

    if not defined(__IMAGE_COR20_HEADER_DEFINED__):
        __IMAGE_COR20_HEADER_DEFINED__ = VOID


        class ReplacesCorHdrNumericDefines(ENUM):
            COMIMAGE_FLAGS_ILONLY = 0x00000001
            COMIMAGE_FLAGS_32BITREQUIRED = 0x00000002
            COMIMAGE_FLAGS_IL_LIBRARY = 0x00000004
            COMIMAGE_FLAGS_STRONGNAMESIGNED = 0x00000008
            COMIMAGE_FLAGS_NATIVE_ENTRYPOINT = 0x00000010
            COMIMAGE_FLAGS_TRACKDEBUGDATA = 0x00010000
            COR_VERSION_MAJOR_V2 = 2
            COR_VERSION_MAJOR = COR_VERSION_MAJOR_V2
            COR_VERSION_MINOR = 5
            COR_DELETED_NAME_LENGTH = 8
            COR_VTABLEGAP_NAME_LENGTH = 8
            NATIVE_TYPE_MAX_CB = 1
            COR_ILMETHOD_SECT_SMALL_MAX_DATASIZE = 0xFF
            IMAGE_COR_MIH_METHODRVA = 0x01
            IMAGE_COR_MIH_EHRVA = 0x02
            IMAGE_COR_MIH_BASICBLOCK = 0x08
            COR_VTABLE_32BIT = 0x01
            COR_VTABLE_64BIT = 0x02
            COR_VTABLE_FROM_UNMANAGED = 0x04
            COR_VTABLE_CALL_MOST_DERIVED = 0x10
            IMAGE_COR_EATJ_THUNK_SIZE = 32
            MAX_CLASS_NAME = 1024
            MAX_PACKAGE_NAME = 1024

        # COM+ 2.0 header structure.
        class _Union_1(ctypes.Union):
            pass


        _Union_1._fields_ = [
            ('EntryPointToken', DWORD),
            ('EntryPointRVA', DWORD),
        ]
        IMAGE_COR20_HEADER._Union_1 = _Union_1

        IMAGE_COR20_HEADER._anonymous_ = (
            '_Union_1',
        )

        IMAGE_COR20_HEADER._fields_ = [
            # Header versioning
            ('cb', DWORD),
            ('MajorRuntimeVersion', WORD),
            ('MinorRuntimeVersion', WORD),
            # Symbol table and startup information
            ('MetaData', IMAGE_DATA_DIRECTORY),
            ('Flags', DWORD),
            # If COMIMAGE_FLAGS_NATIVE_ENTRYPOINT is set, EntryPointRVA
            # represents an RVA to a native entrypoint.
            ('_Union_1', IMAGE_COR20_HEADER._Union_1),
            # Binding information
            ('Resources', IMAGE_DATA_DIRECTORY),
            ('StrongNameSignature', IMAGE_DATA_DIRECTORY),
            # Regular fixup and binding information
            ('CodeManagerTable', IMAGE_DATA_DIRECTORY),
            ('VTableFixups', IMAGE_DATA_DIRECTORY),
            ('ExportAddressTableJumps', IMAGE_DATA_DIRECTORY),
            # Precompiled image info (internal use only - set to zero)
            ('ManagedNativeHeader', IMAGE_DATA_DIRECTORY),
        ]
    else:
        # <TODO>@TODO: This hack is required because we pull in the COM+ 2.0
        # PE header
        # definition from winnt.h, and the constant below hasn't propogated
        # yet.</TODO>
        COR_VTABLE_FROM_UNMANAGED_RETAIN_APPDOMAIN = 0x08
    # END IF   __IMAGE_COR20_HEADER_DEFINED__

    # The most recent version.
    COR_CTOR_METHOD_NAME = ".ctor"
    COR_CTOR_METHOD_NAME_W = ".ctor"
    COR_CCTOR_METHOD_NAME = ".cctor"
    COR_CCTOR_METHOD_NAME_W = ".cctor"
    COR_ENUM_FIELD_NAME = "value__"
    COR_ENUM_FIELD_NAME_W = "value__"

    # The predefined name for deleting a typeDef,MethodDef, FieldDef, Property
    # and Event
    COR_DELETED_NAME_A = "_Deleted"
    COR_DELETED_NAME_W = "_Deleted"
    COR_VTABLEGAP_NAME_A = "_VtblGap"
    COR_VTABLEGAP_NAME_W = "_VtblGap"

    # We intentionally use strncmp so that we will ignore any suffix
    def IsDeletedName(strName):
        return COR_DELETED_NAME_A == strName[:COR_DELETED_NAME_LENGTH]

    def IsVtblGapName(strName):
        return COR_VTABLEGAP_NAME_A == strName[:COR_VTABLEGAP_NAME_LENGTH]

    # TypeDef/ExportedType attr bits, used by DefineTypeDef.
    class CorTypeAttr(ENUM):
        tdVisibilityMask = 0x00000007
        tdNotPublic = 0x00000000
        tdPublic = 0x00000001
        tdNestedPublic = 0x00000002
        tdNestedPrivate = 0x00000003
        tdNestedFamily = 0x00000004
        tdNestedAssembly = 0x00000005
        tdNestedFamANDAssem = 0x00000006
        tdNestedFamORAssem = 0x00000007
        tdLayoutMask = 0x00000018
        tdAutoLayout = 0x00000000
        tdSequentialLayout = 0x00000008
        tdExplicitLayout = 0x00000010
        tdClassSemanticsMask = 0x00000060
        tdClass = 0x00000000
        tdInterface = 0x00000020
        tdAbstract = 0x00000080
        tdSealed = 0x00000100
        tdSpecialName = 0x00000400
        tdImport = 0x00001000
        tdSerializable = 0x00002000
        tdStringFormatMask = 0x00030000
        tdAnsiClass = 0x00000000
        tdUnicodeClass = 0x00010000
        tdAutoClass = 0x00020000
        tdCustomFormatClass = 0x00030000

        # Use this mask to retrieve non-standard encoding information for
        # native interop. The meaning of the values of these 2 bits is
        # unspecified.
        tdCustomFormatMask = 0x00C00000
        tdBeforeFieldInit = 0x00100000
        tdForwarder = 0x00200000
        tdReservedMask = 0x00040800
        tdRTSpecialName = 0x00000800
        tdHasSecurity = 0x00040000

    # Macros for accessing the members of the CorTypeAttr.
    def IsTdNotPublic(x):
        return ((x & tdVisibilityMask) == tdNotPublic)


    def IsTdPublic(x):
        return ((x & tdVisibilityMask) == tdPublic)


    def IsTdNestedPublic(x):
        return ((x & tdVisibilityMask) == tdNestedPublic)


    def IsTdNestedPrivate(x):
        return ((x & tdVisibilityMask) == tdNestedPrivate)


    def IsTdNestedFamily(x):
        return ((x & tdVisibilityMask) == tdNestedFamily)


    def IsTdNestedAssembly(x):
        return ((x & tdVisibilityMask) == tdNestedAssembly)


    def IsTdNestedFamANDAssem(x):
        return ((x & tdVisibilityMask) == tdNestedFamANDAssem)


    def IsTdNestedFamORAssem(x):
        return ((x & tdVisibilityMask) == tdNestedFamORAssem)


    def IsTdNested(x):
        return ((x & tdVisibilityMask) >= tdNestedPublic)


    def IsTdAutoLayout(x):
        return ((x & tdLayoutMask) == tdAutoLayout)


    def IsTdSequentialLayout(x):
        return ((x & tdLayoutMask) == tdSequentialLayout)


    def IsTdExplicitLayout(x):
        return ((x & tdLayoutMask) == tdExplicitLayout)


    def IsTdClass(x):
        return ((x & tdClassSemanticsMask) == tdClass)


    def IsTdInterface(x):
        return ((x & tdClassSemanticsMask) == tdInterface)


    def IsTdAbstract(x):
        return x & tdAbstract


    def IsTdSealed(x):
        return x & tdSealed


    def IsTdSpecialName(x):
        return x & tdSpecialName


    def IsTdImport(x):
        return x & tdImport


    def IsTdSerializable(x):
        return x & tdSerializable


    def IsTdAnsiClass(x):
        return ((x & tdStringFormatMask) == tdAnsiClass)


    def IsTdUnicodeClass(x):
        return ((x & tdStringFormatMask) == tdUnicodeClass)


    def IsTdAutoClass(x):
        return ((x & tdStringFormatMask) == tdAutoClass)


    def IsTdCustomFormatClass(x):
        return ((x & tdStringFormatMask) == tdCustomFormatClass)


    def IsTdBeforeFieldInit(x):
        return x & tdBeforeFieldInit


    def IsTdForwarder(x):
        return x & tdForwarder


    def IsTdRTSpecialName(x):
        return x & tdRTSpecialName


    def IsTdHasSecurity(x):
        return x & tdHasSecurity

    # MethodDef attr bits, Used by DefineMethod.
    class CorMethodAttr(ENUM):
        mdMemberAccessMask = 0x0007
        mdPrivateScope = 0x0000
        mdPrivate = 0x0001
        mdFamANDAssem = 0x0002
        mdAssem = 0x0003
        mdFamily = 0x0004
        mdFamORAssem = 0x0005
        mdPublic = 0x0006
        mdStatic = 0x0010
        mdFinal = 0x0020
        mdVirtual = 0x0040
        mdHideBySig = 0x0080
        mdVtableLayoutMask = 0x0100
        mdReuseSlot = 0x0000
        mdNewSlot = 0x0100
        mdCheckAccessOnOverride = 0x0200
        mdAbstract = 0x0400
        mdSpecialName = 0x0800
        mdPinvokeImpl = 0x2000
        mdUnmanagedExport = 0x0008
        mdReservedMask = 0xD000
        mdRTSpecialName = 0x1000
        mdHasSecurity = 0x4000
        mdRequireSecObject = 0x8000

    # Macros for accessing the members of CorMethodAttr.
    def IsMdPrivateScope(x):
        return ((x & mdMemberAccessMask) == mdPrivateScope)


    def IsMdPrivate(x):
        return ((x & mdMemberAccessMask) == mdPrivate)


    def IsMdFamANDAssem(x):
        return ((x & mdMemberAccessMask) == mdFamANDAssem)


    def IsMdAssem(x):
        return ((x & mdMemberAccessMask) == mdAssem)


    def IsMdFamily(x):
        return ((x & mdMemberAccessMask) == mdFamily)


    def IsMdFamORAssem(x):
        return ((x & mdMemberAccessMask) == mdFamORAssem)


    def IsMdPublic(x):
        return ((x & mdMemberAccessMask) == mdPublic)


    def IsMdStatic(x):
        return x & mdStatic


    def IsMdFinal(x):
        return x & mdFinal


    def IsMdVirtual(x):
        return x & mdVirtual


    def IsMdHideBySig(x):
        return x & mdHideBySig


    def IsMdReuseSlot(x):
        return ((x & mdVtableLayoutMask) == mdReuseSlot)


    def IsMdNewSlot(x):
        return ((x & mdVtableLayoutMask) == mdNewSlot)


    def IsMdCheckAccessOnOverride(x):
        return x & mdCheckAccessOnOverride


    def IsMdAbstract(x):
        return x & mdAbstract


    def IsMdSpecialName(x):
        return x & mdSpecialName


    def IsMdPinvokeImpl(x):
        return x & mdPinvokeImpl


    def IsMdUnmanagedExport(x):
        return x & mdUnmanagedExport


    def IsMdRTSpecialName(x):
        return x & mdRTSpecialName


    def IsMdInstanceInitializer(x, str):
        return (x & mdRTSpecialName) and not strcmp(str, COR_CTOR_METHOD_NAME)


    def IsMdInstanceInitializerW(x, str):
        return (
            (x & mdRTSpecialName) and
            not wcscmp(str, COR_CTOR_METHOD_NAME_W)
        )


    def IsMdClassConstructor(x, str):
        return (x & mdRTSpecialName) and not strcmp(str, COR_CCTOR_METHOD_NAME)


    def IsMdClassConstructorW(x, str):
        return (
            (x & mdRTSpecialName) and
            not wcscmp(str, COR_CCTOR_METHOD_NAME_W)
        )


    def IsMdHasSecurity(x):
        return x & mdHasSecurity


    def IsMdRequireSecObject(x):
        return x & mdRequireSecObject

    # FieldDef attr bits, used by DefineField.
    class CorFieldAttr(ENUM):
        fdFieldAccessMask = 0x0007
        fdPrivateScope = 0x0000
        fdPrivate = 0x0001
        fdFamANDAssem = 0x0002
        fdAssembly = 0x0003
        fdFamily = 0x0004
        fdFamORAssem = 0x0005
        fdPublic = 0x0006
        fdStatic = 0x0010
        fdInitOnly = 0x0020
        fdLiteral = 0x0040
        fdNotSerialized = 0x0080
        fdSpecialName = 0x0200
        fdPinvokeImpl = 0x2000
        fdReservedMask = 0x9500
        fdRTSpecialName = 0x0400
        fdHasFieldMarshal = 0x1000
        fdHasDefault = 0x8000
        fdHasFieldRVA = 0x0100

    # Macros for accessing the members of CorFieldAttr.
    def IsFdPrivateScope(x):
        return ((x & fdFieldAccessMask) == fdPrivateScope)


    def IsFdPrivate(x):
        return ((x & fdFieldAccessMask) == fdPrivate)


    def IsFdFamANDAssem(x):
        return ((x & fdFieldAccessMask) == fdFamANDAssem)


    def IsFdAssembly(x):
        return ((x & fdFieldAccessMask) == fdAssembly)


    def IsFdFamily(x):
        return ((x & fdFieldAccessMask) == fdFamily)


    def IsFdFamORAssem(x):
        return ((x & fdFieldAccessMask) == fdFamORAssem)


    def IsFdPublic(x):
        return ((x & fdFieldAccessMask) == fdPublic)


    def IsFdStatic(x):
        return x & fdStatic


    def IsFdInitOnly(x):
        return x & fdInitOnly


    def IsFdLiteral(x):
        return x & fdLiteral


    def IsFdNotSerialized(x):
        return x & fdNotSerialized


    def IsFdPinvokeImpl(x):
        return x & fdPinvokeImpl


    def IsFdSpecialName(x):
        return x & fdSpecialName


    def IsFdHasFieldRVA(x):
        return x & fdHasFieldRVA


    def IsFdRTSpecialName(x):
        return x & fdRTSpecialName


    def IsFdHasFieldMarshal(x):
        return x & fdHasFieldMarshal


    def IsFdHasDefault(x):
        return x & fdHasDefault

    # Param attr bits, used by DefineParam.
    class CorParamAttr(ENUM):
        pdIn = 0x0001
        pdOut = 0x0002
        pdOptional = 0x0010
        pdReservedMask = 0xF000
        pdHasDefault = 0x1000
        pdHasFieldMarshal = 0x2000
        pdUnused = 0xCFE0

    # Macros for accessing the members of CorParamAttr.
    def IsPdIn(x):
        return x & pdIn


    def IsPdOut(x):
        return x & pdOut


    def IsPdOptional(x):
        return x & pdOptional


    def IsPdHasDefault(x):
        return x & pdHasDefault


    def IsPdHasFieldMarshal(x):
        return x & pdHasFieldMarshal

    # Property attr bits, used by DefineProperty.
    class CorPropertyAttr(ENUM):
        prSpecialName = 0x0200
        prReservedMask = 0xF400
        prRTSpecialName = 0x0400
        prHasDefault = 0x1000
        prUnused = 0xE9FF

    # Macros for accessing the members of CorPropertyAttr.
    def IsPrSpecialName(x):
        return x & prSpecialName


    def IsPrRTSpecialName(x):
        return x & prRTSpecialName


    def IsPrHasDefault(x):
        return x & prHasDefault

    # Event attr bits, used by DefineEvent.
    class CorEventAttr(ENUM):
        evSpecialName = 0x0200
        evReservedMask = 0x0400
        evRTSpecialName = 0x0400

    # Macros for accessing the members of CorEventAttr.
    def IsEvSpecialName(x):
        return x & evSpecialName


    def IsEvRTSpecialName(x):
        return x & evRTSpecialName

    # MethodSemantic attr bits, used by DefineProperty, DefineEvent.
    class CorMethodSemanticsAttr(ENUM):
        msSetter = 0x0001
        msGetter = 0x0002
        msOther = 0x0004
        msAddOn = 0x0008
        msRemoveOn = 0x0010
        msFire = 0x0020

    # Macros for accessing the members of CorMethodSemanticsAttr.
    def IsMsSetter(x):
        return x & msSetter


    def IsMsGetter(x):
        return x & msGetter


    def IsMsOther(x):
        return x & msOther


    def IsMsAddOn(x):
        return x & msAddOn


    def IsMsRemoveOn(x):
        return x & msRemoveOn


    def IsMsFire(x):
        return x & msFire

    # DeclSecurity attr bits, used by DefinePermissionSet.
    class CorDeclSecurity(ENUM):
        dclActionMask = 0x001F
        dclActionNil = 0x0000
        dclRequest = 0x0001
        dclDemand = 0x0002
        dclAssert = 0x0003
        dclDeny = 0x0004
        dclPermitOnly = 0x0005
        dclLinktimeCheck = 0x0006
        dclInheritanceCheck = 0x0007
        dclRequestMinimum = 0x0008
        dclRequestOptional = 0x0009
        dclRequestRefuse = 0x000A
        dclPrejitGrant = 0x000B
        dclPrejitDenied = 0x000C
        dclNonCasDemand = 0x000D
        dclNonCasLinkDemand = 0x000E
        dclNonCasInheritance = 0x000F
        dclMaximumValue = 0x000F

    # Macros for accessing the members of CorDeclSecurity.
    def IsDclActionNil(x):
        return ((x & dclActionMask) == dclActionNil)

    # Is this a demand that can trigger a stackwalk?
    def IsDclActionAnyStackModifier(x):
        return (
            ((x & dclActionMask) == dclAssert) or
            ((x & dclActionMask) == dclDeny) or
            ((x & dclActionMask) == dclPermitOnly)
        )

    # MethodImpl attr bits, used by DefineMethodImpl.
    class CorMethodImpl(ENUM):
        miCodeTypeMask = 0x0003
        miIL = 0x0000
        miNative = 0x0001
        miOPTIL = 0x0002
        miRuntime = 0x0003
        miManagedMask = 0x0004
        miUnmanaged = 0x0004
        miManaged = 0x0000
        miForwardRef = 0x0010
        miPreserveSig = 0x0080
        miInternalCall = 0x1000
        miSynchronized = 0x0020
        miNoInlining = 0x0008
        miMaxMethodImplVal = 0xFFFF

    # Macros for accesing the members of CorMethodImpl.
    def IsMiIL(x):
        return ((x & miCodeTypeMask) == miIL)


    def IsMiNative(x):
        return ((x & miCodeTypeMask) == miNative)


    def IsMiOPTIL(x):
        return ((x & miCodeTypeMask) == miOPTIL)


    def IsMiRuntime(x):
        return ((x & miCodeTypeMask) == miRuntime)


    def IsMiUnmanaged(x):
        return ((x & miManagedMask) == miUnmanaged)


    def IsMiManaged(x):
        return ((x & miManagedMask) == miManaged)


    def IsMiForwardRef(x):
        return x & miForwardRef


    def IsMiPreserveSig(x):
        return x & miPreserveSig


    def IsMiInternalCall(x):
        return x & miInternalCall


    def IsMiSynchronized(x):
        return x & miSynchronized


    def IsMiNoInlining(x):
        return x & miNoInlining

    # PinvokeMap attr bits, used by DefinePinvokeMap.
    class CorPinvokeMap(ENUM):
        pmNoMangle = 0x0001
        pmCharSetMask = 0x0006
        pmCharSetNotSpec = 0x0000
        pmCharSetAnsi = 0x0002
        pmCharSetUnicode = 0x0004
        pmCharSetAuto = 0x0006
        pmBestFitUseAssem = 0x0000
        pmBestFitEnabled = 0x0010
        pmBestFitDisabled = 0x0020
        pmBestFitMask = 0x0030
        pmThrowOnUnmappableCharUseAssem = 0x0000
        pmThrowOnUnmappableCharEnabled = 0x1000
        pmThrowOnUnmappableCharDisabled = 0x2000
        pmThrowOnUnmappableCharMask = 0x3000
        pmSupportsLastError = 0x0040
        pmCallConvMask = 0x0700

        # Pinvoke will use native callconv appropriate to target windows
        # platform.
        pmCallConvWinapi = 0x0100
        pmCallConvCdecl = 0x0200
        pmCallConvStdcall = 0x0300
        pmCallConvThiscall = 0x0400
        pmCallConvFastcall = 0x0500
        pmMaxValue = 0xFFFF

    # Macros for accessing the members of CorPinvokeMap
    def IsPmNoMangle(x):
        return x & pmNoMangle


    def IsPmCharSetNotSpec(x):
        return ((x & pmCharSetMask) == pmCharSetNotSpec)


    def IsPmCharSetAnsi(x):
        return ((x & pmCharSetMask) == pmCharSetAnsi)


    def IsPmCharSetUnicode(x):
        return ((x & pmCharSetMask) == pmCharSetUnicode)


    def IsPmCharSetAuto(x):
        return ((x & pmCharSetMask) == pmCharSetAuto)


    def IsPmSupportsLastError(x):
        return x & pmSupportsLastError


    def IsPmCallConvWinapi(x):
        return ((x & pmCallConvMask) == pmCallConvWinapi)


    def IsPmCallConvCdecl(x):
        return ((x & pmCallConvMask) == pmCallConvCdecl)


    def IsPmCallConvStdcall(x):
        return ((x & pmCallConvMask) == pmCallConvStdcall)


    def IsPmCallConvFastcall(x):
        return ((x & pmCallConvMask) == pmCallConvFastcall)


    def IsPmBestFitEnabled(x):
        return ((x & pmBestFitMask) == pmBestFitEnabled)


    def IsPmBestFitDisabled(x):
        return ((x & pmBestFitMask) == pmBestFitDisabled)


    def IsPmBestFitUseAssem(x):
        return ((x & pmBestFitMask) == pmBestFitUseAssem)


    def IsPmThrowOnUnmappableCharEnabled(x):
        return ((x & pmThrowOnUnmappableCharMask) == pmThrowOnUnmappableCharEnabled)


    def IsPmThrowOnUnmappableCharDisabled(x):
        return ((x & pmThrowOnUnmappableCharMask) == pmThrowOnUnmappableCharDisabled)


    def IsPmThrowOnUnmappableCharUseAssem(x):
        return ((x & pmThrowOnUnmappableCharMask) == pmThrowOnUnmappableCharUseAssem)

    # Assembly attr bits, used by DefineAssembly.
    class CorAssemblyFlags(ENUM):
        afPublicKey = 0x0001
        afPA_None = 0x0000
        afPA_MSIL = 0x0010
        afPA_x86 = 0x0020
        afPA_IA64 = 0x0030
        afPA_AMD64 = 0x0040
        afPA_Specified = 0x0080
        afPA_Mask = 0x0070
        afPA_FullMask = 0x00F0
        afPA_Shift = 0x0004
        afEnableJITcompileTracking = 0x8000
        afDisableJITcompileOptimizer = 0x4000
        afRetargetable = 0x0100

    # Macros for accessing the members of CorAssemblyFlags.
    def IsAfRetargetable(x):
        return x & afRetargetable

    # Macros for accessing the Processor Architecture flags of
    # CorAssemblyFlags.
    def IsAfPA_MSIL(x):
        return ((x & afPA_Mask) == afPA_MSIL)


    def IsAfPA_x86(x):
        return ((x & afPA_Mask) == afPA_x86)


    def IsAfPA_IA64(x):
        return ((x & afPA_Mask) == afPA_IA64)


    def IsAfPA_AMD64(x):
        return ((x & afPA_Mask) == afPA_AMD64)


    def IsAfPA_Specified(x):
        return x & afPA_Specified


    def PAIndex(x):
        return ((x & afPA_Mask) >> afPA_Shift)


    def PAFlag(x):
        return ((x << afPA_Shift) & afPA_Mask)


    def PrepareForSaving(x):
        if x & (x & afPA_Specified):
            return  ~afPA_Specified
        else:
            return  ~afPA_FullMask

    def IsAfEnableJITcompileTracking(x):
        return x & afEnableJITcompileTracking


    def IsAfDisableJITcompileOptimizer(x):
        return x & afDisableJITcompileOptimizer


    # Macros for accessing the public key flags of CorAssemblyFlags.
    def IsAfPublicKey(x):
        return x & afPublicKey


    def IsAfPublicKeyToken(x):
        return (x & afPublicKey) == 0


    # ManifestResource attr bits, used by DefineManifestResource.
    class CorManifestResourceFlags(ENUM):
        mrVisibilityMask = 0x0007
        mrPublic = 0x0001
        mrPrivate = 0x0002

    # Macros for accessing the members of CorManifestResourceFlags.
    def IsMrPublic(x):
        return ((x & mrVisibilityMask) == mrPublic)


    def IsMrPrivate(x):
        return ((x & mrVisibilityMask) == mrPrivate)

    # File attr bits, used by DefineFile.
    class CorFileFlags(ENUM):
        ffContainsMetaData = 0x0000
        ffContainsNoMetaData = 0x0001

    # Macros for accessing the members of CorFileFlags.
    def IsFfContainsMetaData(x):
        return (not (x & ffContainsNoMetaData))


    def IsFfContainsNoMetaData(x):
        return x & ffContainsNoMetaData

    # PE file kind bits, returned by IMetaDataImport2::GetPEKind()
    class CorPEKind(ENUM):
        peNot = 0x00000000
        peILonly = 0x00000001
        pe32BitRequired = 0x00000002
        pe32Plus = 0x00000004
        pe32Unmanaged = 0x00000008

    # GenericParam bits, used by DefineGenericParam.
    class CorGenericParamAttr(ENUM):
        gpVarianceMask = 0x0003
        gpNonVariant = 0x0000
        gpCovariant = 0x0001
        gpContravariant = 0x0002
        gpSpecialConstraintMask = 0x001C
        gpNoSpecialConstraint = 0x0000
        gpReferenceTypeConstraint = 0x0004
        gpNotNullableValueTypeConstraint = 0x0008
        gpDefaultConstructorConstraint = 0x0010

    # structures and enums moved from COR.H
    COR_SIGNATURE = UINT8

    # pointer to a cor sig.  Not void* so that
    PCOR_SIGNATURE = POINTER(COR_SIGNATURE)

    # the bytes can be incremented easily
    PCCOR_SIGNATURE = POINTER(COR_SIGNATURE)
    MDUTF8CSTR = POINTER(CHAR)
    MDUTF8STR = POINTER(CHAR)

    # **********************************************************************
    # Element type for Cor signature
    # **********************************************************************
    class CorElementType(ENUM):
        ELEMENT_TYPE_END = 0x0
        ELEMENT_TYPE_VOID = 0x1
        ELEMENT_TYPE_BOOLEAN = 0x2
        ELEMENT_TYPE_CHAR = 0x3
        ELEMENT_TYPE_I1 = 0x4
        ELEMENT_TYPE_U1 = 0x5
        ELEMENT_TYPE_I2 = 0x6
        ELEMENT_TYPE_U2 = 0x7
        ELEMENT_TYPE_I4 = 0x8
        ELEMENT_TYPE_U4 = 0x9
        ELEMENT_TYPE_I8 = 0xA
        ELEMENT_TYPE_U8 = 0xB
        ELEMENT_TYPE_R4 = 0xC
        ELEMENT_TYPE_R8 = 0xD
        ELEMENT_TYPE_STRING = 0xE
        ELEMENT_TYPE_PTR = 0xF
        ELEMENT_TYPE_BYREF = 0x10
        ELEMENT_TYPE_VALUETYPE = 0x11
        ELEMENT_TYPE_CLASS = 0x12
        ELEMENT_TYPE_VAR = 0x13
        ELEMENT_TYPE_ARRAY = 0x14
        ELEMENT_TYPE_GENERICINST = 0x15
        ELEMENT_TYPE_TYPEDBYREF = 0x16
        ELEMENT_TYPE_I = 0x18
        ELEMENT_TYPE_U = 0x19
        ELEMENT_TYPE_FNPTR = 0x1B
        ELEMENT_TYPE_OBJECT = 0x1C
        ELEMENT_TYPE_SZARRAY = 0x1D
        ELEMENT_TYPE_MVAR = 0x1E
        ELEMENT_TYPE_CMOD_REQD = 0x1F
        ELEMENT_TYPE_CMOD_OPT = 0x20
        ELEMENT_TYPE_INTERNAL = 0x21
        ELEMENT_TYPE_MAX = 0x22
        ELEMENT_TYPE_MODIFIER = 0x40
        ELEMENT_TYPE_SENTINEL = 0x01 | ELEMENT_TYPE_MODIFIER
        ELEMENT_TYPE_PINNED = 0x05 | ELEMENT_TYPE_MODIFIER
        ELEMENT_TYPE_R4_HFA = 0x06 | ELEMENT_TYPE_MODIFIER
        ELEMENT_TYPE_R8_HFA = 0x07 | ELEMENT_TYPE_MODIFIER

    # **********************************************************************
    # Serialization types for Custom attribute support
    # **********************************************************************
    class CorSerializationType(ENUM):
        SERIALIZATION_TYPE_UNDEFINED = 0
        SERIALIZATION_TYPE_BOOLEAN = ELEMENT_TYPE_BOOLEAN
        SERIALIZATION_TYPE_CHAR = ELEMENT_TYPE_CHAR
        SERIALIZATION_TYPE_I1 = ELEMENT_TYPE_I1
        SERIALIZATION_TYPE_U1 = ELEMENT_TYPE_U1
        SERIALIZATION_TYPE_I2 = ELEMENT_TYPE_I2
        SERIALIZATION_TYPE_U2 = ELEMENT_TYPE_U2
        SERIALIZATION_TYPE_I4 = ELEMENT_TYPE_I4
        SERIALIZATION_TYPE_U4 = ELEMENT_TYPE_U4
        SERIALIZATION_TYPE_I8 = ELEMENT_TYPE_I8
        SERIALIZATION_TYPE_U8 = ELEMENT_TYPE_U8
        SERIALIZATION_TYPE_R4 = ELEMENT_TYPE_R4
        SERIALIZATION_TYPE_R8 = ELEMENT_TYPE_R8
        SERIALIZATION_TYPE_STRING = ELEMENT_TYPE_STRING
        SERIALIZATION_TYPE_SZARRAY = ELEMENT_TYPE_SZARRAY
        SERIALIZATION_TYPE_TYPE = 0x50
        SERIALIZATION_TYPE_TAGGED_OBJECT = 0x51
        SERIALIZATION_TYPE_FIELD = 0x53
        SERIALIZATION_TYPE_PROPERTY = 0x54
        SERIALIZATION_TYPE_ENUM = 0x55

    # Calling convention flags.
    class CorCallingConvention(ENUM):
        IMAGE_CEE_CS_CALLCONV_DEFAULT = 0x0
        IMAGE_CEE_CS_CALLCONV_VARARG = 0x5
        IMAGE_CEE_CS_CALLCONV_FIELD = 0x6
        IMAGE_CEE_CS_CALLCONV_LOCAL_SIG = 0x7
        IMAGE_CEE_CS_CALLCONV_PROPERTY = 0x8
        IMAGE_CEE_CS_CALLCONV_UNMGD = 0x9
        IMAGE_CEE_CS_CALLCONV_GENERICINST = 0xA
        IMAGE_CEE_CS_CALLCONV_NATIVEVARARG = 0xB
        IMAGE_CEE_CS_CALLCONV_MAX = 0xC
        IMAGE_CEE_CS_CALLCONV_MASK = 0x0F
        IMAGE_CEE_CS_CALLCONV_HASTHIS = 0x20
        IMAGE_CEE_CS_CALLCONV_EXPLICITTHIS = 0x40

        # Generic method sig with explicit number of type arguments
        # (precedes ordinary parameter count)
        IMAGE_CEE_CS_CALLCONV_GENERIC = 0x10

    IMAGE_CEE_CS_CALLCONV_INSTANTIATION = IMAGE_CEE_CS_CALLCONV_GENERICINST


    class CorUnmanagedCallingConvention(ENUM):
        IMAGE_CEE_UNMANAGED_CALLCONV_C = 0x1
        IMAGE_CEE_UNMANAGED_CALLCONV_STDCALL = 0x2
        IMAGE_CEE_UNMANAGED_CALLCONV_THISCALL = 0x3
        IMAGE_CEE_UNMANAGED_CALLCONV_FASTCALL = 0x4
        IMAGE_CEE_CS_CALLCONV_C = IMAGE_CEE_UNMANAGED_CALLCONV_C
        IMAGE_CEE_CS_CALLCONV_STDCALL = IMAGE_CEE_UNMANAGED_CALLCONV_STDCALL
        IMAGE_CEE_CS_CALLCONV_THISCALL = IMAGE_CEE_UNMANAGED_CALLCONV_THISCALL
        IMAGE_CEE_CS_CALLCONV_FASTCALL = IMAGE_CEE_UNMANAGED_CALLCONV_FASTCALL


    class CorArgType(ENUM):
        IMAGE_CEE_CS_END = 0x0
        IMAGE_CEE_CS_VOID = 0x1
        IMAGE_CEE_CS_I4 = 0x2
        IMAGE_CEE_CS_I8 = 0x3
        IMAGE_CEE_CS_R4 = 0x4
        IMAGE_CEE_CS_R8 = 0x5
        IMAGE_CEE_CS_PTR = 0x6
        IMAGE_CEE_CS_OBJECT = 0x7
        IMAGE_CEE_CS_STRUCT4 = 0x8
        IMAGE_CEE_CS_STRUCT32 = 0x9
        IMAGE_CEE_CS_BYVALUE = 0xA

    # **********************************************************************
    # Native type for N-Direct
    # **********************************************************************
    class CorNativeType(ENUM):
        NATIVE_TYPE_END = 0x0
        NATIVE_TYPE_VOID = 0x1
        NATIVE_TYPE_BOOLEAN = 0x2
        NATIVE_TYPE_I1 = 0x3
        NATIVE_TYPE_U1 = 0x4
        NATIVE_TYPE_I2 = 0x5
        NATIVE_TYPE_U2 = 0x6
        NATIVE_TYPE_I4 = 0x7
        NATIVE_TYPE_U4 = 0x8
        NATIVE_TYPE_I8 = 0x9
        NATIVE_TYPE_U8 = 0xA
        NATIVE_TYPE_R4 = 0xB
        NATIVE_TYPE_R8 = 0xC
        NATIVE_TYPE_SYSCHAR = 0xD
        NATIVE_TYPE_VARIANT = 0xE
        NATIVE_TYPE_CURRENCY = 0xF
        NATIVE_TYPE_PTR = 0x10
        NATIVE_TYPE_DECIMAL = 0x11
        NATIVE_TYPE_DATE = 0x12
        NATIVE_TYPE_BSTR = 0x13
        NATIVE_TYPE_LPSTR = 0x14
        NATIVE_TYPE_LPWSTR = 0x15
        NATIVE_TYPE_LPTSTR = 0x16
        NATIVE_TYPE_FIXEDSYSSTRING = 0x17
        NATIVE_TYPE_OBJECTREF = 0x18
        NATIVE_TYPE_IUNKNOWN = 0x19
        NATIVE_TYPE_IDISPATCH = 0x1A
        NATIVE_TYPE_STRUCT = 0x1B
        NATIVE_TYPE_INTF = 0x1C
        NATIVE_TYPE_SAFEARRAY = 0x1D
        NATIVE_TYPE_FIXEDARRAY = 0x1E
        NATIVE_TYPE_INT = 0x1F
        NATIVE_TYPE_UINT = 0x20
        NATIVE_TYPE_NESTEDSTRUCT = 0x21
        NATIVE_TYPE_BYVALSTR = 0x22
        NATIVE_TYPE_ANSIBSTR = 0x23
        NATIVE_TYPE_TBSTR = 0x24
        NATIVE_TYPE_VARIANTBOOL = 0x25
        NATIVE_TYPE_FUNC = 0x26
        NATIVE_TYPE_ASANY = 0x28
        NATIVE_TYPE_ARRAY = 0x2A
        NATIVE_TYPE_LPSTRUCT = 0x2B
        NATIVE_TYPE_CUSTOMMARSHALER = 0x2C
        NATIVE_TYPE_ERROR = 0x2D
        NATIVE_TYPE_MAX = 0x50

    DESCR_GROUP_METHODDEF = 0
    DESCR_GROUP_METHODIMPL = 1

    # *************************************************************************
    # a COR_ILMETHOD_SECT is a generic container for attributes that are
    # private
    # to a particular method. The COR_ILMETHOD structure points to one of these
    # (see GetSect()). COR_ILMETHOD_SECT can decode the Kind of attribute
    # (but not
    # its internal data layout, and can skip past the current attibute to find
    # the
    # Next one. The overhead for COR_ILMETHOD_SECT is a minimum of 2 bytes.
    class CorILMethodSect(ENUM): # codes that identify attributes{
        CorILMethod_Sect_Reserved = 0
        CorILMethod_Sect_EHTable = 1
        CorILMethod_Sect_OptILTable = 2
        CorILMethod_Sect_KindMask = 0x3F
        CorILMethod_Sect_FatFormat = 0x40
        CorILMethod_Sect_MoreSects = 0x80

    # ********************************
    # NOTE this structure must be DWORD alignednot not
    IMAGE_COR_ILMETHOD_SECT_SMALL._fields_ = [
        ('Kind', BYTE),
        ('DataSize', BYTE),
    ]

    # ********************************
    # NOTE this structure must be DWORD alignednot not
    IMAGE_COR_ILMETHOD_SECT_FAT._fields_ = [
        ('Kind', UINT, 8),
        ('DataSize', UINT, 24),
    ]

    # *************************************************************************
    # /* If COR_ILMETHOD_SECT_HEADER::Kind() = CorILMethod_Sect_EHTable then
    # the attribute is a list of exception handling clauses. There are two
    # formats, fat or small
    class CorExceptionFlag(ENUM): # defintitions for the Flags field below (for both big and small){
        COR_ILEXCEPTION_CLAUSE_NONE = 1
        COR_ILEXCEPTION_CLAUSE_OFFSETLEN = 0x0000
        COR_ILEXCEPTION_CLAUSE_DEPRECATED = 0x0000
        COR_ILEXCEPTION_CLAUSE_FILTER = 0x0001
        COR_ILEXCEPTION_CLAUSE_FINALLY = 0x0002
        COR_ILEXCEPTION_CLAUSE_FAULT = 0x0004

        # duplicated clase.. this clause was duplicated down to a funclet
        # which was pulled out of line
        COR_ILEXCEPTION_CLAUSE_DUPLICATED = 0x0008

    # *******************************
    # NOTE not not not NOTE
    # This structure should line up with EE_ILEXCEPTION_CLAUSE,
    # otherwise you'll have to adjust code in Excep.cpp, re: EHRangeTree
    # NOTE not not not NOTE
    # use for type-based exception handlers
    class _Union_2(ctypes.Union):
        pass


    _Union_2._fields_ = [
        ('ClassToken', DWORD),
        # use for filter-based exception handlers
        # (COR_ILEXCEPTION_FILTER is set)
        ('FilterOffset', DWORD),
    ]
    IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT._Union_2 = _Union_2

    IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT._anonymous_ = (
        '_Union_2',
    )

    IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT._fields_ = [
        ('Flags', CorExceptionFlag),
        ('TryOffset', DWORD),
        # relative to start of try block
        ('TryLength', DWORD),
        ('HandlerOffset', DWORD),
        # relative to start of handler
        ('HandlerLength', DWORD),
        ('_Union_2', IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT._Union_2),
    ]

    IMAGE_COR_ILMETHOD_SECT_EH_FAT._fields_ = [
        ('SectFat', IMAGE_COR_ILMETHOD_SECT_FAT),
        # actually variable size
        ('Clauses', IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT * 1),
    ]

    # *******************************
    class _Union_3(ctypes.Union):
        pass


    _Union_3._fields_ = [
        ('ClassToken', DWORD),
        ('FilterOffset', DWORD),
    ]
    IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL._Union_3 = _Union_3

    IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL._anonymous_ = (
        '_Union_3',
    )

    _TEMP_IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL = [
    ]
    if defined(_WIN64):
        _TEMP_IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL += [
            ('Flags', UINT, 16),
        ]
    else: #  not _WIN64
        _TEMP_IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL += [
            ('Flags', CorExceptionFlag, 16),
        ]
    # END IF


    _TEMP_IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL += [
        ('TryOffset', UINT, 16),
        # relative to start of try block
        ('TryLength', UINT, 8),
        ('HandlerOffset', UINT, 16),
        # relative to start of handler
        ('HandlerLength', UINT, 8),
        ('_Union_3', IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL._Union_3),
    ]

    IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL._fields_ = _TEMP_IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL

    # *******************************
    IMAGE_COR_ILMETHOD_SECT_EH_SMALL._fields_ = [
        ('SectSmall', IMAGE_COR_ILMETHOD_SECT_SMALL),
        ('Reserved', WORD),
        # actually variable size
        ('Clauses', IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL * 1),
    ]

    IMAGE_COR_ILMETHOD_SECT_EH._fields_ = [
        ('Small', IMAGE_COR_ILMETHOD_SECT_EH_SMALL),
        ('Fat', IMAGE_COR_ILMETHOD_SECT_EH_FAT),
    ]

    # *************************************************************************
    class CorILMethodFlags(ENUM):
        CorILMethod_InitLocals = 0x0010
        CorILMethod_MoreSects = 0x0008
        CorILMethod_CompressedIL = 0x0040
        CorILMethod_FormatShift = 3
        CorILMethod_FormatMask = (1 << CorILMethod_FormatShift) - 1
        CorILMethod_TinyFormat = 0x0002
        CorILMethod_SmallFormat = 0x0000
        CorILMethod_FatFormat = 0x0003
        CorILMethod_TinyFormat1 = 0x0006
    # ***********************************************************************
    # Used when the method is tiny (< 64 bytes), and there are no local vars
    IMAGE_COR_ILMETHOD_TINY._fields_ = [
        ('Flags_CodeSize', BYTE),
    ]
    # ********************************
    # This strucuture is the 'fat' layout, where no compression is attempted.
    # Note that this structure can be added on at the end, thus making it
    # extensible
    IMAGE_COR_ILMETHOD_FAT._fields_ = [
        # Flags
        ('Flags', UINT, 12),
        # size in DWords of this structure (currently 3)
        ('Size', UINT, 4),
        # maximum number of items (I4, I, I8, obj ...), on the operand stack
        ('MaxStack', UINT, 16),
        # size of the code
        ('CodeSize', DWORD),
        # token that indicates the signature of the local vars (0 means none)
        ('LocalVarSigTok', mdSignature),
    ]
    IMAGE_COR_ILMETHOD._fields_ = [
        ('Tiny', IMAGE_COR_ILMETHOD_TINY),
        ('Fat', IMAGE_COR_ILMETHOD_FAT),
    ]
    # Native method descriptor.
    IMAGE_COR_NATIVE_DESCRIPTOR._fields_ = [
        ('GCInfo', DWORD),
        ('EHInfo', DWORD),
    ]
    IMAGE_COR_X86_RUNTIME_FUNCTION_ENTRY._fields_ = [
        # RVA of start of function
        ('BeginAddress', ULONG),
        # RVA of end of function
        ('EndAddress', ULONG),
        # Associated MIH
        ('MIH', ULONG),
    ]
    IMAGE_COR_MIH_ENTRY._fields_ = [
        ('EHRVA', ULONG),
        ('MethodRVA', ULONG),
        ('Token', mdToken),
        ('Flags', BYTE),
        ('CodeManager', BYTE),
        ('MIHData', BYTE * 0),
    ]
    # **********************************************************************
    # Non VOS v-table entries. Define an array of these pointed to by
    # IMAGE_COR20_HEADER.VTableFixups. Each entry describes a contiguous array
    # of
    # v-table slots. The slots start out initialized to the meta data token
    # value
    # for the method they need to call. At image load time, the CLR Loader will
    # turn each entry into a pointer to machine code for the CPU and can be
    # called directly.
    # **********************************************************************
    IMAGE_COR_VTABLEFIXUP._fields_ = [
        # Offset of v-table array in image.
        ('RVA', ULONG),
        # How many entries at location.
        ('Count', USHORT),
        # COR_VTABLE_xxx type of entries.
        ('Type', USHORT),
    ]
    # **********************************************************************
    # **********************************************************************
    # M E T A - D A T A D E C L A R A T I O N S
    # **********************************************************************
    # **********************************************************************
    # **********************************************************************
    # Enums for SetOption API.
    # **********************************************************************
    # flags for MetaDataCheckDuplicatesFor
    class CorCheckDuplicatesFor(ENUM):
        MDDupAll = 0xFFFFFFFF
        MDDupENC = MDDupAll
        MDNoDupChecks = 0x00000000
        MDDupTypeDef = 0x00000001
        MDDupInterfaceImpl = 0x00000002
        MDDupMethodDef = 0x00000004
        MDDupTypeRef = 0x00000008
        MDDupMemberRef = 0x00000010
        MDDupCustomAttribute = 0x00000020
        MDDupParamDef = 0x00000040
        MDDupPermission = 0x00000080
        MDDupProperty = 0x00000100
        MDDupEvent = 0x00000200
        MDDupFieldDef = 0x00000400
        MDDupSignature = 0x00000800
        MDDupModuleRef = 0x00001000
        MDDupTypeSpec = 0x00002000
        MDDupImplMap = 0x00004000
        MDDupAssemblyRef = 0x00008000
        MDDupFile = 0x00010000
        MDDupExportedType = 0x00020000
        MDDupManifestResource = 0x00040000
        MDDupGenericParam = 0x00080000
        MDDupMethodSpec = 0x00100000
        MDDupGenericParamConstraint = 0x00200000
        MDDupAssembly = 0x10000000
        MDDupDefault = (
            MDNoDupChecks |
            MDDupTypeRef |
            MDDupMemberRef |
            MDDupSignature |
            MDDupTypeSpec |
            MDDupMethodSpec
        )

    # flags for MetaDataRefToDefCheck
    class CorRefToDefCheck(ENUM):
        MDRefToDefDefault = 0x00000003
        MDRefToDefAll = 0xFFFFFFFF
        MDRefToDefNone = 0x00000000
        MDTypeRefToDef = 0x00000001
        MDMemberRefToDef = 0x00000002

    # MetaDataNotificationForTokenMovement
    class CorNotificationForTokenMovement(ENUM):
        MDNotifyDefault = 0x0000000F
        MDNotifyAll = 0xFFFFFFFF
        MDNotifyNone = 0x00000000
        MDNotifyMethodDef = 0x00000001
        MDNotifyMemberRef = 0x00000002
        MDNotifyFieldDef = 0x00000004
        MDNotifyTypeRef = 0x00000008
        MDNotifyTypeDef = 0x00000010
        MDNotifyParamDef = 0x00000020
        MDNotifyInterfaceImpl = 0x00000040
        MDNotifyProperty = 0x00000080
        MDNotifyEvent = 0x00000100
        MDNotifySignature = 0x00000200
        MDNotifyTypeSpec = 0x00000400
        MDNotifyCustomAttribute = 0x00000800
        MDNotifySecurityValue = 0x00001000
        MDNotifyPermission = 0x00002000
        MDNotifyModuleRef = 0x00004000
        MDNotifyNameSpace = 0x00008000
        MDNotifyAssemblyRef = 0x01000000
        MDNotifyFile = 0x02000000
        MDNotifyExportedType = 0x04000000
        MDNotifyResource = 0x08000000


    class CorSetENC(ENUM):
        MDSetENCOn = 0x00000001
        MDSetENCOff = 0x00000002
        MDUpdateENC = 0x00000001
        MDUpdateFull = 0x00000002
        MDUpdateExtension = 0x00000003
        MDUpdateIncremental = 0x00000004
        MDUpdateDelta = 0x00000005
        MDUpdateMask = 0x00000007

    def IsENCDelta(x):
        return ((x & MDUpdateMask) == MDUpdateDelta)

    # flags used in SetOption when pair with MetaDataErrorIfEmitOutOfOrder guid
    class CorErrorIfEmitOutOfOrder(ENUM):
        MDErrorOutOfOrderDefault = 0x00000000
        MDErrorOutOfOrderNone = 0x00000000

        # generate out of order emit for method, field, param, property, and
        # event
        MDErrorOutOfOrderAll = 0xFFFFFFFF
        MDMethodOutOfOrder = 0x00000001
        MDFieldOutOfOrder = 0x00000002
        MDParamOutOfOrder = 0x00000004
        MDPropertyOutOfOrder = 0x00000008
        MDEventOutOfOrder = 0x00000010

    # flags used in SetOption when pair with MetaDataImportOption guid
    class CorImportOptions(ENUM):
        MDImportOptionDefault = 0x00000000
        MDImportOptionAll = 0xFFFFFFFF
        MDImportOptionAllTypeDefs = 0x00000001
        MDImportOptionAllMethodDefs = 0x00000002
        MDImportOptionAllFieldDefs = 0x00000004
        MDImportOptionAllProperties = 0x00000008
        MDImportOptionAllEvents = 0x00000010
        MDImportOptionAllCustomAttributes = 0x00000020
        MDImportOptionAllExportedTypes = 0x00000040

    # flags for MetaDataThreadSafetyOptions
    class CorThreadSafetyOptions(ENUM):
        MDThreadSafetyDefault = 0x00000000
        MDThreadSafetyOff = 0x00000000
        MDThreadSafetyOn = 0x00000001

    # flags for MetaDataLinkerOptions
    class CorLinkerOptions(ENUM):
        MDAssembly = 0x00000000
        MDNetModule = 0x00000001

    # flags for MetaDataMergeOptions
    class MergeFlags(ENUM):
        MergeFlagsNone = 0
        MergeManifest = 0x00000001
        DropMemberRefCAs = 0x00000002
        NoDupCheck = 0x00000004
        MergeExportedTypes = 0x00000008

    # struct used to retrieve field offset
    # used by GetClassLayout and SetClassLayout
    if not defined(_COR_FIELD_OFFSET_):
        _COR_FIELD_OFFSET_ = VOID


        COR_FIELD_OFFSET._fields_ = [
            ('ridOfField', mdFieldDef),
            ('ulOffset', ULONG),
        ]
    # END IF


    IMAGE_COR_FIXUPENTRY._fields_ = [
        ('ulRVA', ULONG),
        ('Count', ULONG),
    ]


    # Token tags.
    class CorTokenType(ENUM):
        mdtModule = 0x00000000
        mdtTypeRef = 0x01000000
        mdtTypeDef = 0x02000000
        mdtFieldDef = 0x04000000
        mdtMethodDef = 0x06000000
        mdtParamDef = 0x08000000
        mdtInterfaceImpl = 0x09000000
        mdtMemberRef = 0x0A000000
        mdtCustomAttribute = 0x0C000000
        mdtPermission = 0x0E000000
        mdtSignature = 0x11000000
        mdtEvent = 0x14000000
        mdtProperty = 0x17000000
        mdtModuleRef = 0x1A000000
        mdtTypeSpec = 0x1B000000
        mdtAssembly = 0x20000000
        mdtAssemblyRef = 0x23000000
        mdtFile = 0x26000000
        mdtExportedType = 0x27000000
        mdtManifestResource = 0x28000000
        mdtGenericParam = 0x2A000000
        mdtMethodSpec = 0x2B000000
        mdtGenericParamConstraint = 0x2C000000
        mdtString = 0x70000000
        mdtName = 0x71000000

        # Leave this on the high end value. This does not correspond to
        # metadata table
        mdtBaseType = 0x72000000

    # Build / decompose tokens.
    def RidToToken(rid, tktype):
        rid |= tktype
        return rid

    def TokenFromRid(rid, tktype):
        return rid | tktype


    def RidFromToken(tk):
        return tk & 0x00FFFFFF


    def TypeFromToken(tk):
        return tk & 0xFF000000


    def IsNilToken(tk):
        return RidFromToken(tk) == 0


    # Nil tokens
    mdTokenNil = 0
    mdModuleNil = mdtModule
    mdTypeRefNil = mdtTypeRef
    mdTypeDefNil = mdtTypeDef
    mdFieldDefNil = mdtFieldDef
    mdMethodDefNil = mdtMethodDef
    mdParamDefNil = mdtParamDef
    mdInterfaceImplNil = mdtInterfaceImpl
    mdMemberRefNil = mdtMemberRef
    mdCustomAttributeNil = mdtCustomAttribute
    mdPermissionNil = mdtPermission
    mdSignatureNil = mdtSignature
    mdEventNil = mdtEvent
    mdPropertyNil = mdtProperty
    mdModuleRefNil = mdtModuleRef
    mdTypeSpecNil = mdtTypeSpec
    mdAssemblyNil = mdtAssembly
    mdAssemblyRefNil = mdtAssemblyRef
    mdFileNil = mdtFile
    mdExportedTypeNil = mdtExportedType
    mdManifestResourceNil = mdtManifestResource
    mdGenericParamNil = mdtGenericParam
    mdGenericParamConstraintNil = mdtGenericParamConstraint
    mdMethodSpecNil = mdtMethodSpec
    mdStringNil = mdtString


    # Open bits.
    class CorOpenFlags(ENUM):
        ofRead = 0x00000000
        ofWrite = 0x00000001
        ofReadWriteMask = 0x00000001

        # Open scope with memory. Ask metadata to maintain its own copy of
        # memory.
        ofCopyMemory = 0x00000002

        # Open scope on ngen image, return the manifest metadata instead of
        # the IL metadata
        ofManifestMetadata = 0x00000008

        # Open scope for read. Will be unable to QI for a IMetadataEmit*
        # interface
        ofReadOnly = 0x00000010

        # The memory was allocated with CoTaskMemAlloc and will be freed by
        # the metadata
        ofTakeOwnership = 0x00000020
        ofCacheImage = 0x00000004
        ofNoTypeLib = 0x00000080
        ofReserved1 = 0x00000100
        ofReserved2 = 0x00000200
        ofReserved = 0xFFFFFF40

    def IsOfRead(x):
        return ((x & ofReadWriteMask) == ofRead)


    def IsOfReadWrite(x):
        return ((x & ofReadWriteMask) == ofWrite)


    def IsOfCopyMemory(x):
        return x & ofCopyMemory


    def IsOfManifestMetadata(x):
        return x & ofManifestMetadata


    def IsOfReadOnly(x):
        return x & ofReadOnly


    def IsOfTakeOwnership(x):
        return x & ofTakeOwnership


    def IsOfReserved(x):
        return ((x & ofReserved) != 0)
    CorRegTypeAttr = CorTypeAttr


    # Opaque type for an enumeration handle.
    HCORENUM = POINTER(VOID)

    # Note that this must be kept in sync with System.AttributeTargets.
    class CorAttributeTargets(ENUM):
        catAssembly = 0x0001
        catModule = 0x0002
        catClass = 0x0004
        catStruct = 0x0008
        catEnum = 0x0010
        catConstructor = 0x0020
        catMethod = 0x0040
        catProperty = 0x0080
        catField = 0x0100
        catEvent = 0x0200
        catInterface = 0x0400
        catParameter = 0x0800
        catDelegate = 0x1000
        catGenericParameter = 0x4000
        catAll = (
            catAssembly |
            catModule |
            catClass |
            catStruct |
            catEnum |
            catConstructor |
            catMethod |
            catProperty |
            catField |
            catEvent |
            catInterface |
            catParameter |
            catDelegate |
            catGenericParameter
        )
        catClassMembers = (
            catClass |
            catStruct |
            catEnum |
            catConstructor |
            catMethod |
            catProperty |
            catField |
            catEvent |
            catDelegate |
            catInterface
        )

    if not defined(MACROS_NOT_SUPPORTED):
        # Some well-known custom attributes
        if not defined(IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS):
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS = (
                IMAGE_CEE_CS_CALLCONV_DEFAULT |
                IMAGE_CEE_CS_CALLCONV_HASTHIS
            )
        # END IF

        INTEROP_DISPID_TYPE_W = (
            "System.Runtime.InteropServices.DispIdAttribute"
        )
        INTEROP_DISPID_TYPE = "System.Runtime.InteropServices.DispIdAttribute"
        INTEROP_DISPID_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I4
        ]
        INTEROP_INTERFACETYPE_TYPE_W = (
            "System.Runtime.InteropServices.InterfaceTypeAttribute"
        )
        INTEROP_INTERFACETYPE_TYPE = (
            "System.Runtime.InteropServices.InterfaceTypeAttribute"
        )
        INTEROP_INTERFACETYPE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I2
        ]

        INTEROP_CLASSINTERFACE_TYPE_W = (
            "System.Runtime.InteropServices.ClassInterfaceAttribute"
        )
        INTEROP_CLASSINTERFACE_TYPE = (
            "System.Runtime.InteropServices.ClassInterfaceAttribute"
        )
        INTEROP_CLASSINTERFACE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I2
        ]

        INTEROP_COMVISIBLE_TYPE_W = (
            "System.Runtime.InteropServices.ComVisibleAttribute"
        )
        INTEROP_COMVISIBLE_TYPE = (
            "System.Runtime.InteropServices.ComVisibleAttribute"
        )
        INTEROP_COMVISIBLE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_BOOLEAN
        ]

        INTEROP_COMREGISTERFUNCTION_TYPE_W = (
            "System.Runtime.InteropServices.ComRegisterFunctionAttribute"
        )
        INTEROP_COMREGISTERFUNCTION_TYPE = (
            "System.Runtime.InteropServices.ComRegisterFunctionAttribute"
        )
        INTEROP_COMREGISTERFUNCTION_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        INTEROP_COMUNREGISTERFUNCTION_TYPE_W = (
            "System.Runtime.InteropServices.ComUnregisterFunctionAttribute"
        )
        INTEROP_COMUNREGISTERFUNCTION_TYPE = (
            "System.Runtime.InteropServices.ComUnregisterFunctionAttribute"
        )
        INTEROP_COMUNREGISTERFUNCTION_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        INTEROP_IMPORTEDFROMTYPELIB_TYPE_W = (
            "System.Runtime.InteropServices.ImportedFromTypeLibAttribute"
        )
        INTEROP_IMPORTEDFROMTYPELIB_TYPE = (
            "System.Runtime.InteropServices.ImportedFromTypeLibAttribute"
        )
        INTEROP_IMPORTEDFROMTYPELIB_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_STRING
        ]

        INTEROP_IDISPATCHIMPL_TYPE_W = (
            "System.Runtime.InteropServices.IDispatchImplAttribute"
        )
        INTEROP_IDISPATCHIMPL_TYPE = (
            "System.Runtime.InteropServices.IDispatchImplAttribute"
        )
        INTEROP_IDISPATCHIMPL_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I2
        ]

        INTEROP_COMSOURCEINTERFACES_TYPE_W = (
            "System.Runtime.InteropServices.ComSourceInterfacesAttribute"
        )
        INTEROP_COMSOURCEINTERFACES_TYPE = (
            "System.Runtime.InteropServices.ComSourceInterfacesAttribute"
        )
        INTEROP_COMSOURCEINTERFACES_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_STRING
        ]

        INTEROP_COMDEFAULTINTERFACE_TYPE_W = (
            "System.Runtime.InteropServices.ComDefaultInterfaceAttribute"
        )
        INTEROP_COMDEFAULTINTERFACE_TYPE = (
            "System.Runtime.InteropServices.ComDefaultInterfaceAttribute"
        )
        INTEROP_COMCONVERSIONLOSS_TYPE_W = (
            "System.Runtime.InteropServices.ComConversionLossAttribute"
        )
        INTEROP_COMCONVERSIONLOSS_TYPE = (
            "System.Runtime.InteropServices.ComConversionLossAttribute"
        )
        INTEROP_COMCONVERSIONLOSS_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        INTEROP_BESTFITMAPPING_TYPE_W = (
            "System.Runtime.InteropServices.BestFitMappingAttribute"
        )
        INTEROP_BESTFITMAPPING_TYPE = (
            "System.Runtime.InteropServices.BestFitMappingAttribute"
        )
        INTEROP_BESTFITMAPPING_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            2,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_BOOLEAN,
            ELEMENT_TYPE_BOOLEAN
        ]

        INTEROP_TYPELIBTYPE_TYPE_W = (
            "System.Runtime.InteropServices.TypeLibTypeAttribute"
        )
        INTEROP_TYPELIBTYPE_TYPE = (
            "System.Runtime.InteropServices.TypeLibTypeAttribute"
        )
        INTEROP_TYPELIBTYPE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I2
        ]

        INTEROP_TYPELIBFUNC_TYPE_W = (
            "System.Runtime.InteropServices.TypeLibFuncAttribute"
        )
        INTEROP_TYPELIBFUNC_TYPE = (
            "System.Runtime.InteropServices.TypeLibFuncAttribute"
        )
        INTEROP_TYPELIBFUNC_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I2
        ]

        INTEROP_TYPELIBVAR_TYPE_W = (
            "System.Runtime.InteropServices.TypeLibVarAttribute"
        )
        INTEROP_TYPELIBVAR_TYPE = (
            "System.Runtime.InteropServices.TypeLibVarAttribute"
        )
        INTEROP_TYPELIBVAR_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I2
        ]

        INTEROP_MARSHALAS_TYPE_W = (
            "System.Runtime.InteropServices.MarshalAsAttribute"
        )
        INTEROP_MARSHALAS_TYPE = (
            "System.Runtime.InteropServices.MarshalAsAttribute"
        )
        INTEROP_MARSHALAS_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I2
        ]

        INTEROP_COMIMPORT_TYPE_W = (
            "System.Runtime.InteropServices.ComImportAttribute"
        )
        INTEROP_COMIMPORT_TYPE = (
            "System.Runtime.InteropServices.ComImportAttribute"
        )
        INTEROP_COMIMPORT_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        INTEROP_GUID_TYPE_W = "System.Runtime.InteropServices.GuidAttribute"
        INTEROP_GUID_TYPE = "System.Runtime.InteropServices.GuidAttribute"
        INTEROP_GUID_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_STRING
        ]

        INTEROP_DEFAULTMEMBER_TYPE_W = (
            "System.Reflection.DefaultMemberAttribute"
        )
        INTEROP_DEFAULTMEMBER_TYPE = "System.Reflection.DefaultMemberAttribute"
        INTEROP_DEFAULTMEMBER_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_STRING
        ]

        INTEROP_COMEMULATE_TYPE_W = (
            "System.Runtime.InteropServices.ComEmulateAttribute"
        )
        INTEROP_COMEMULATE_TYPE = (
            "System.Runtime.InteropServices.ComEmulateAttribute"
        )
        INTEROP_COMEMULATE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_STRING
        ]

        INTEROP_PRESERVESIG_TYPE_W = (
            "System.Runtime.InteropServices.PreserveSigAttribure"
        )
        INTEROP_PRESERVESIG_TYPE = (
            "System.Runtime.InteropServices.PreserveSigAttribure"
        )
        INTEROP_PRESERVESIG_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_BOOLEAN
        ]

        INTEROP_IN_TYPE_W = "System.Runtime.InteropServices.InAttribute"
        INTEROP_IN_TYPE = "System.Runtime.InteropServices.InAttribute"
        INTEROP_IN_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        INTEROP_OUT_TYPE_W = "System.Runtime.InteropServices.OutAttribute"
        INTEROP_OUT_TYPE = "System.Runtime.InteropServices.OutAttribute"
        INTEROP_OUT_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        INTEROP_COMALIASNAME_TYPE_W = (
            "System.Runtime.InteropServices.ComAliasNameAttribute"
        )
        INTEROP_COMALIASNAME_TYPE = (
            "System.Runtime.InteropServices.ComAliasNameAttribute"
        )
        INTEROP_COMALIASNAME_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_STRING
        ]

        INTEROP_PARAMARRAY_TYPE_W = "System.ParamArrayAttribute"
        INTEROP_PARAMARRAY_TYPE = "System.ParamArrayAttribute"
        INTEROP_PARAMARRAY_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        INTEROP_LCIDCONVERSION_TYPE_W = (
            "System.Runtime.InteropServices.LCIDConversionAttribute"
        )
        INTEROP_LCIDCONVERSION_TYPE = (
            "System.Runtime.InteropServices.LCIDConversionAttribute"
        )
        INTEROP_LCIDCONVERSION_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I4
        ]

        INTEROP_COMSUBSTITUTABLEINTERFACE_TYPE_W = (
            "System.Runtime.InteropServices.ComSubstitutableInterfaceAttribute"
        )
        INTEROP_COMSUBSTITUTABLEINTERFACE_TYPE = (
            "System.Runtime.InteropServices.ComSubstitutableInterfaceAttribute"
        )
        INTEROP_COMSUBSTITUTABLEINTERFACE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        INTEROP_DECIMALVALUE_TYPE_W = (
            "System.Runtime.CompilerServices.DecimalConstantAttribute"
        )
        INTEROP_DECIMALVALUE_TYPE = (
            "System.Runtime.CompilerServices.DecimalConstantAttribute"
        )
        INTEROP_DECIMALVALUE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            5,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_U1,
            ELEMENT_TYPE_U1,
            ELEMENT_TYPE_U4,
            ELEMENT_TYPE_U4,
            ELEMENT_TYPE_U4
        ]

        INTEROP_DATETIMEVALUE_TYPE_W = (
            "System.Runtime.CompilerServices.DateTimeConstantAttribute"
        )
        INTEROP_DATETIMEVALUE_TYPE = (
            "System.Runtime.CompilerServices.DateTimeConstantAttribute"
        )
        INTEROP_DATETIMEVALUE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I8
        ]

        INTEROP_IUNKNOWNVALUE_TYPE_W = (
            "System.Runtime.CompilerServices.IUnknownConstantAttribute"
        )
        INTEROP_IUNKNOWNVALUE_TYPE = (
            "System.Runtime.CompilerServices.IUnknownConstantAttribute"
        )
        INTEROP_IUNKNOWNVALUE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        INTEROP_IDISPATCHVALUE_TYPE_W = (
            "System.Runtime.CompilerServices.IDispatchConstantAttribute"
        )
        INTEROP_IDISPATCHVALUE_TYPE = (
            "System.Runtime.CompilerServices.IDispatchConstantAttribute"
        )
        INTEROP_IDISPATCHVALUE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        INTEROP_AUTOPROXY_TYPE_W = (
            "System.Runtime.InteropServices.AutomationProxyAttribute"
        )
        INTEROP_AUTOPROXY_TYPE = (
            "System.Runtime.InteropServices.AutomationProxyAttribute"
        )
        INTEROP_AUTOPROXY_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_BOOLEAN
        ]

        INTEROP_TYPELIBIMPORTCLASS_TYPE_W = (
            "System.Runtime.InteropServices.TypeLibImportClassAttribute"
        )
        INTEROP_TYPELIBIMPORTCLASS_TYPE = (
            "System.Runtime.InteropServices.TypeLibImportClassAttribute"
        )
        INTEROP_TYPELIBVERSION_TYPE_W = (
            "System.Runtime.InteropServices.TypeLibVersionAttribute"
        )
        INTEROP_TYPELIBVERSION_TYPE = (
            "System.Runtime.InteropServices.TypeLibVersionAttribute"
        )
        INTEROP_TYPELIBVERSION_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            2,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I2,
            ELEMENT_TYPE_I2
        ]

        INTEROP_COMCOMPATIBLEVERSION_TYPE_W = (
            "System.Runtime.InteropServices.ComCompatibleVersionAttribute"
        )
        INTEROP_COMCOMPATIBLEVERSION_TYPE = (
            "System.Runtime.InteropServices.ComCompatibleVersionAttribute"
        )
        INTEROP_COMCOMPATIBLEVERSION_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            4,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I2,
            ELEMENT_TYPE_I2,
            ELEMENT_TYPE_I2,
            ELEMENT_TYPE_I2
        ]

        INTEROP_COMEVENTINTERFACE_TYPE_W = (
            "System.Runtime.InteropServices.ComEventInterfaceAttribute"
        )
        INTEROP_COMEVENTINTERFACE_TYPE = (
            "System.Runtime.InteropServices.ComEventInterfaceAttribute"
        )
        INTEROP_COCLASS_TYPE_W = (
            "System.Runtime.InteropServices.CoClassAttribute"
        )
        INTEROP_COCLASS_TYPE = (
            "System.Runtime.InteropServices.CoClassAttribute"
        )
        INTEROP_SERIALIZABLE_TYPE_W = "System.SerializableAttribute"
        INTEROP_SERIALIZABLE_TYPE = "System.SerializableAttribute"
        INTEROP_SERIALIZABLE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        INTEROP_SETWIN32CONTEXTINIDISPATCHATTRIBUTE_TYPE_W = (
            "System.Runtime.InteropServices.SetWin32ContextInIDispatchAttribute"
        )
        INTEROP_SETWIN32CONTEXTINIDISPATCHATTRIBUTE_TYPE = (
            "System.Runtime.InteropServices.SetWin32ContextInIDispatchAttribute"
        )
        INTEROP_SETWIN32CONTEXTINIDISPATCHATTRIBUTE_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        FRIEND_ASSEMBLY_TYPE_W = (
            "System.Runtime.CompilerServices.InternalsVisibleToAttribute"
        )
        FRIEND_ASSEMBLY_TYPE = (
            "System.Runtime.CompilerServices.InternalsVisibleToAttribute"
        )
        FRIEND_ASSEMBLY_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_STRING
        ]

        DEFAULTDOMAIN_STA_TYPE_W = "System.STAThreadAttribute"
        DEFAULTDOMAIN_STA_TYPE = "System.STAThreadAttribute"
        DEFAULTDOMAIN_STA_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        DEFAULTDOMAIN_MTA_TYPE_W = "System.MTAThreadAttribute"
        DEFAULTDOMAIN_MTA_TYPE = "System.MTAThreadAttribute"
        DEFAULTDOMAIN_MTA_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            0,
            ELEMENT_TYPE_VOID
        ]

        DEFAULTDOMAIN_LOADEROPTIMIZATION_TYPE_W = (
            "System.LoaderOptimizationAttribute"
        )
        DEFAULTDOMAIN_LOADEROPTIMIZATION_TYPE = (
            "System.LoaderOptimizationAttribute"
        )
        DEFAULTDOMAIN_LOADEROPTIMIZATION_SIG = [
            IMAGE_CEE_CS_CALLCONV_DEFAULT_HASTHIS,
            1,
            ELEMENT_TYPE_VOID,
            ELEMENT_TYPE_I1
        ]


        # Keep in sync with CompilationRelaxations.cs
        class CompilationRelaxationsEnum(ENUM):
            CompilationRelaxations_NoStringInterning = 0x0008

        CompilationRelaxationEnum = CompilationRelaxationsEnum
        COMPILATIONRELAXATIONS_TYPE_W = (
            "System.Runtime.CompilerServices.CompilationRelaxationsAttribute"
        )
        COMPILATIONRELAXATIONS_TYPE = (
            "System.Runtime.CompilerServices.CompilationRelaxationsAttribute"
        )

        # Keep in sync with RuntimeCompatibilityAttribute.cs
        RUNTIMECOMPATIBILITY_TYPE_W = (
            "System.Runtime.CompilerServices.RuntimeCompatibilityAttribute"
        )
        RUNTIMECOMPATIBILITY_TYPE = (
            "System.Runtime.CompilerServices.RuntimeCompatibilityAttribute"
        )

        # Keep in sync with AssemblySettingAttributes.cs
        class NGenHintEnum(ENUM):
            NGenDefault = 0x0000
            NGenEager = 0x0001
            NGenLazy = 0x0002
            NGenNever = 0x0003


        class LoadHintEnum(ENUM):
            LoadDefault = 0x0000
            LoadAlways = 0x0001
            LoadSometimes = 0x0002
            LoadNever = 0x0003

        NGEN_TYPE_W = "System.Runtime.CompilerServices.NGenAttribute"
        NGEN_TYPE = "System.Runtime.CompilerServices.NGenAttribute"
        DEFAULTDEPENDENCY_TYPE_W = (
            "System.Runtime.CompilerServices.DefaultDependencyAttribute"
        )
        DEFAULTDEPENDENCY_TYPE = (
            "System.Runtime.CompilerServices.DefaultDependencyAttribute"
        )
        DEPENDENCY_TYPE_W = (
            "System.Runtime.CompilerServices.DependencyAttribute"
        )
        DEPENDENCY_TYPE = "System.Runtime.CompilerServices.DependencyAttribute"
        CMOD_CALLCONV_NAMESPACE_OLD = "System.Runtime.InteropServices"
        CMOD_CALLCONV_NAMESPACE = "System.Runtime.CompilerServices"
        CMOD_CALLCONV_NAME_CDECL = "CallConvCdecl"
        CMOD_CALLCONV_NAME_STDCALL = "CallConvStdcall"
        CMOD_CALLCONV_NAME_FASTCALL = "CallConvFastcall"
    # END IF   MACROS_NOT_SUPPORTED


    # GetSaveSize accuracy
    if not defined(_CORSAVESIZE_DEFINED_):
        _CORSAVESIZE_DEFINED_ = VOID


        class CorSaveSize(ENUM):
            cssAccurate = 0x0000
            cssQuick = 0x0001
            cssDiscardTransientCAs = 0x0002

    # END IF


    def COR_IS_METHOD_MANAGED_IL(flags):
        return (flags & 0xF) == (miIL | miManaged)


    def COR_IS_METHOD_MANAGED_OPTIL(flags):
        return (flags & 0xF) == (miOPTIL | miManaged)


    def COR_IS_METHOD_MANAGED_NATIVE(flags):
        return (flags & 0xF) == (miNative | miManaged)


    def COR_IS_METHOD_UNMANAGED_NATIVE(flags):
        return (flags & 0xF) == (miNative | miUnmanaged)


    # Enum used with NATIVE_TYPE_ARRAY.
    class NativeTypeArrayFlags(ENUM):
        ntaSizeParamIndexSpecified = 0x0001
        ntaReserved = 0xFFFE

    # Opaque types for security properties and values.
    PSECURITY_PROPS = POINTER(VOID)
    PSECURITY_VALUE = POINTER(VOID)
    PPSECURITY_PROPS = POINTER(POINTER(VOID))
    PPSECURITY_VALUE = POINTER(POINTER(VOID))

    # -------------------------------------
    # --- Security data structures
    # -------------------------------------
    # Descriptor for a single security custom attribute.
    # Ref to constructor of security attribute.
    COR_SECATTR._fields_ = [
        ('tkCtor', mdMemberRef),
        # Blob describing ctor args and field/property values.
        ('pCustomAttribute', POINTER(VOID)),
        # Length of the above blob.
        ('cbCustomAttribute', ULONG),
    ]
# END IF   __CORHDR_H__


