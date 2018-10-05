__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import *
# from .rpcndr_h import *
# from .windows_h import *
# from .ole2_h import *

from .wtypes_h import (
    ENUM,
    POINTER,
    HRESULT,
    ULONG,
    UINT,
    REFGUID,
    LCID,
    BSTR,
    DWORD,
    REFIID,
    LPOLESTR,
    GUID,
    LPCOLESTR,
    WORD,
    INT,
    PVOID,
    BYTE,
    BOOL,
    USHORT,
    VOID,
    ULONG_PTR,
    SCODE,
    VARTYPE,
    LONG,
    wireBSTR,
    LONGLONG,
    SHORT,
    FLOAT,
    DOUBLE,
    VARIANT_BOOL,
    CY,
    DATE,
    CHAR,
    ULONGLONG,
    DECIMAL,
    BYTE_SIZEDARR,
    HYPER_SIZEDARR,
    VARENUM,
    _VARIANT_BOOL,
    WORD_SIZEDARR,
    DWORD_SIZEDARR
)
from .guiddef_h import (
    IID,
)
import ctypes
import comtypes


IID_ICreateTypeInfo = IID(
    '{00020405-0000-0000-C000-000000000046}'
)


class ICreateTypeInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICreateTypeInfo
    _idlflags_ = []


IID_ICreateTypeInfo2 = IID(
    '{0002040E-0000-0000-C000-000000000046}'
)


class ICreateTypeInfo2(ICreateTypeInfo):
    _case_insensitive_ = True
    _iid_ = IID_ICreateTypeInfo2
    _idlflags_ = []


IID_ICreateTypeLib = IID(
    '{00020406-0000-0000-C000-000000000046}'
)


class ICreateTypeLib(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICreateTypeLib
    _idlflags_ = []


IID_ICreateTypeLib2 = IID(
    '{0002040F-0000-0000-C000-000000000046}'
)


class ICreateTypeLib2(ICreateTypeLib):
    _case_insensitive_ = True
    _iid_ = IID_ICreateTypeLib2
    _idlflags_ = []


IID_IDispatch = IID(
    '{00020400-0000-0000-C000-000000000046}'
)


class IDispatch(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDispatch
    _idlflags_ = []


IID_IEnumVARIANT = IID(
    '{00020404-0000-0000-C000-000000000046}'
)


class IEnumVARIANT(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumVARIANT
    _idlflags_ = []


IID_ITypeComp = IID(
    '{00020403-0000-0000-C000-000000000046}'
)


class ITypeComp(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITypeComp
    _idlflags_ = []


IID_ITypeInfo = IID(
    '{00020401-0000-0000-C000-000000000046}'
)


class ITypeInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITypeInfo
    _idlflags_ = []


IID_ITypeInfo2 = IID(
    '{00020412-0000-0000-C000-000000000046}'
)


class ITypeInfo2(ITypeInfo):
    _case_insensitive_ = True
    _iid_ = IID_ITypeInfo2
    _idlflags_ = []


IID_ITypeLib = IID(
    '{00020402-0000-0000-C000-000000000046}'
)


class ITypeLib(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITypeLib
    _idlflags_ = []


IID_ITypeLib2 = IID(
    '{00020411-0000-0000-C000-000000000046}'
)


class ITypeLib2(ITypeLib):
    _case_insensitive_ = True
    _iid_ = IID_ITypeLib2
    _idlflags_ = []


IID_ITypeChangeEvents = IID(
    '{00020410-0000-0000-C000-000000000046}'
)


class ITypeChangeEvents(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITypeChangeEvents
    _idlflags_ = []


IID_IErrorInfo = IID(
    '{1CF2B120-547D-101B-8E65-08002B2BD119}'
)


class IErrorInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IErrorInfo
    _idlflags_ = []


IID_ICreateErrorInfo = IID(
    '{22F03340-547D-101B-8E65-08002B2BD119}'
)


class ICreateErrorInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICreateErrorInfo
    _idlflags_ = []


IID_ISupportErrorInfo = IID(
    '{DF0B3D60-548F-101B-8E65-08002B2BD119}'
)


class ISupportErrorInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISupportErrorInfo
    _idlflags_ = []


IID_ITypeFactory = IID(
    '{0000002E-0000-0000-C000-000000000046}'
)


class ITypeFactory(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITypeFactory
    _idlflags_ = []


IID_ITypeMarshal = IID(
    '{0000002D-0000-0000-C000-000000000046}'
)


class ITypeMarshal(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITypeMarshal
    _idlflags_ = []


IID_IRecordInfo = IID(
    '{0000002F-0000-0000-C000-000000000046}'
)


class IRecordInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRecordInfo
    _idlflags_ = []


IID_IErrorLog = IID(
    '{3127CA40-446E-11CE-8135-00AA004BB851}'
)


class IErrorLog(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IErrorLog
    _idlflags_ = []


IID_IPropertyBag = IID(
    '{55272A00-42CB-11CE-8135-00AA004BB851}'
)


class IPropertyBag(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyBag
    _idlflags_ = []


IID_ITypeLibRegistrationReader = IID(
    '{ED6A8A2A-B160-4E77-8F73-AA7435CD5C27}'
)


class ITypeLibRegistrationReader(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITypeLibRegistrationReader
    _idlflags_ = []


from .objidl_h import *
from .winapifamily_h import *


CURRENCY = CY

class tagSAFEARRAYBOUND(ctypes.Structure):
    _fields_ = [
        ('cElements', ULONG),
        ('lLbound', LONG),
    ]


SAFEARRAYBOUND = tagSAFEARRAYBOUND
LPSAFEARRAYBOUND = POINTER(tagSAFEARRAYBOUND)


class _wireSAFEARR_BSTR(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('aBstr', POINTER(wireBSTR)),
    ]


SAFEARR_BSTR = _wireSAFEARR_BSTR


class _wireSAFEARR_UNKNOWN(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('apUnknown', POINTER(POINTER(comtypes.IUnknown))),
    ]


SAFEARR_UNKNOWN = _wireSAFEARR_UNKNOWN


class _wireSAFEARR_DISPATCH(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('apDispatch', POINTER(POINTER(IDispatch))),
    ]


SAFEARR_DISPATCH = _wireSAFEARR_DISPATCH





class _wireBRECORD(ctypes.Structure):
    _fields_ = [
        ('fFlags', ULONG),
        ('clSize', ULONG),
        ('pRecInfo', POINTER(IRecordInfo)),
        ('pRecord', POINTER(BYTE)),
    ]


wireBRECORD = POINTER(_wireBRECORD)


class _wireSAFEARR_BRECORD(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('aRecord', POINTER(wireBRECORD)),
    ]


SAFEARR_BRECORD = _wireSAFEARR_BRECORD


class _wireSAFEARR_HAVEIID(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('apUnknown', POINTER(POINTER(comtypes.IUnknown))),
        ('iid', IID),
    ]


SAFEARR_HAVEIID = _wireSAFEARR_HAVEIID


class tagSF_TYPE(ENUM):
    SF_ERROR = VARENUM.VT_ERROR
    SF_I1 = VARENUM.VT_I1
    SF_I2 = VARENUM.VT_I2
    SF_I4 = VARENUM.VT_I4
    SF_I8 = VARENUM.VT_I8
    SF_BSTR = VARENUM.VT_BSTR
    SF_UNKNOWN = VARENUM.VT_UNKNOWN
    SF_DISPATCH = VARENUM.VT_DISPATCH
    SF_VARIANT = VARENUM.VT_VARIANT
    SF_RECORD = VARENUM.VT_RECORD
    SF_HAVEIID = VARENUM.VT_UNKNOWN | VARENUM.VT_RESERVED


SF_TYPE = tagSF_TYPE


class _wireSAFEARR_VARIANT(ctypes.Structure):
    pass


SAFEARR_VARIANT = _wireSAFEARR_VARIANT


class _wireSAFEARRAY_UNION(ctypes.Structure):
    class __MIDL_IOleAutomationTypes_0001(ctypes.Union):
        _fields_ = [
            ('BstrStr', SAFEARR_BSTR),
            ('UnknownStr', SAFEARR_UNKNOWN),
            ('DispatchStr', SAFEARR_DISPATCH),
            ('VariantStr', SAFEARR_VARIANT),
            ('RecordStr', SAFEARR_BRECORD),
            ('HaveIidStr', SAFEARR_HAVEIID),
            ('ByteStr', BYTE_SIZEDARR),
            ('WordStr', WORD_SIZEDARR),
            ('LongStr', DWORD_SIZEDARR),
            ('HyperStr', HYPER_SIZEDARR),
        ]

    _fields_ = [
        ('sfType', ULONG),
        ('u', __MIDL_IOleAutomationTypes_0001),
    ]


SAFEARRAYUNION = _wireSAFEARRAY_UNION


class _wireSAFEARRAY(ctypes.Structure):
    _fields_ = [
        ('cDims', USHORT),
        ('fFeatures', USHORT),
        ('cbElements', ULONG),
        ('cLocks', ULONG),
        ('uArrayStructs', SAFEARRAYUNION),
        ('rgsabound', SAFEARRAYBOUND * 1),
    ]


wireSAFEARRAY = POINTER(_wireSAFEARRAY)
wirePSAFEARRAY = POINTER(wireSAFEARRAY)


class tagSAFEARRAY(ctypes.Structure):
    _fields_ = [
        ('cDims', USHORT),
        ('fFeatures', USHORT),
        ('cbElements', ULONG),
        ('cLocks', ULONG),
        ('pvData', PVOID),
        ('rgsabound', SAFEARRAYBOUND * 1),
    ]


SAFEARRAY = tagSAFEARRAY


LPSAFEARRAY = POINTER(SAFEARRAY)
FADF_AUTO = 0x1
FADF_STATIC = 0x2
FADF_EMBEDDED = 0x4
FADF_FIXEDSIZE = 0x10
FADF_RECORD = 0x20
FADF_HAVEIID = 0x40
FADF_HAVEVARTYPE = 0x80
FADF_BSTR = 0x100
FADF_UNKNOWN = 0x200
FADF_DISPATCH = 0x400
FADF_VARIANT = 0x800
FADF_RESERVED = 0xF008


class tagVARIANT(ctypes.Structure):
    pass


VARIANT = tagVARIANT
LPVARIANT = POINTER(VARIANT)
VARIANTARG = VARIANT
LPVARIANTARG = POINTER(VARIANT)
REFVARIANT = POINTER(VARIANT)


class __VARIANT_NAME_1(ctypes.Union):

    class __VARIANT_NAME_2(ctypes.Structure):

        class __VARIANT_NAME_3(ctypes.Union):

            class __VARIANT_NAME_4(ctypes.Structure):
                _fields_ = [
                    ('pvRecord', PVOID),
                    ('pRecInfo', POINTER(IRecordInfo)),
                ]

            _fields_ = [
                ('llVal', LONGLONG),
                ('lVal', LONG),
                ('bVal', BYTE),
                ('iVal', SHORT),
                ('fltVal', FLOAT),
                ('dblVal', DOUBLE),
                ('BOOLVal', VARIANT_BOOL),
                ('BOOL', _VARIANT_BOOL),
                ('scode', SCODE),
                ('cyVal', CY),
                ('date', DATE),
                ('bstrVal', BSTR),
                ('punkVal', POINTER(comtypes.IUnknown)),
                ('pdispVal', POINTER(IDispatch)),
                ('parray', POINTER(SAFEARRAY)),
                ('pbVal', POINTER(BYTE)),
                ('piVal', POINTER(SHORT)),
                ('plVal', POINTER(LONG)),
                ('pllVal', POINTER(LONGLONG)),
                ('pfltVal', POINTER(FLOAT)),
                ('pdblVal', POINTER(DOUBLE)),
                ('pBOOLVal', POINTER(VARIANT_BOOL)),
                ('pBOOL', POINTER(_VARIANT_BOOL)),
                ('pscode', POINTER(SCODE)),
                ('pcyVal', POINTER(CY)),
                ('pdate', POINTER(DATE)),
                ('pbstrVal', POINTER(BSTR)),
                ('ppunkVal', POINTER(POINTER(comtypes.IUnknown))),
                ('ppdispVal', POINTER(POINTER(IDispatch))),
                ('pparray', POINTER(POINTER(SAFEARRAY))),
                ('pvarVal', POINTER(VARIANT)),
                ('byref', PVOID),
                ('cVal', CHAR),
                ('uiVal', USHORT),
                ('ulVal', ULONG),
                ('ullVal', ULONGLONG),
                ('INTVal', INT),
                ('uINTVal', UINT),
                ('pdecVal', POINTER(DECIMAL)),
                ('pcVal', POINTER(CHAR)),
                ('puiVal', POINTER(USHORT)),
                ('pulVal', POINTER(ULONG)),
                ('pullVal', POINTER(ULONGLONG)),
                ('pINTVal', POINTER(INT)),
                ('puINTVal', POINTER(UINT)),
                ('__VARIANT_NAME_4', __VARIANT_NAME_4),
            ]


        _fields_ = [
            ('vt', VARTYPE),
            ('wReserved1', WORD),
            ('wReserved2', WORD),
            ('wReserved3', WORD),
            ('__VARIANT_NAME_3', __VARIANT_NAME_3),
        ]


    _fields_ = [
        ('__VARIANT_NAME_2', __VARIANT_NAME_2),
        ('decVal', DECIMAL),
    ]


tagVARIANT._fields_ = [
    ('__VARIANT_NAME_1', __VARIANT_NAME_1),
]


class _wireVARIANT(ctypes.Structure):
    pass


wireVARIANT = POINTER(_wireVARIANT)

try:
    _wireSAFEARR_VARIANT._fields_ = [
        ('Size', ULONG),
        ('aVariant', POINTER(wireVARIANT)),
    ]
except AttributeError:
    pass


class DUMMYUNIONNAME(ctypes.Union):
    _fields_ = [
        ('llVal', LONGLONG),
        ('lVal', LONG),
        ('bVal', BYTE),
        ('iVal', SHORT),
        ('fltVal', FLOAT),
        ('dblVal', DOUBLE),
        ('BOOLVal', VARIANT_BOOL),
        ('scode', SCODE),
        ('cyVal', CY),
        ('date', DATE),
        ('bstrVal', wireBSTR),
        ('punkVal', POINTER(comtypes.IUnknown)),
        ('pdispVal', POINTER(IDispatch)),
        ('parray', wirePSAFEARRAY),
        ('brecVal', wireBRECORD),
        ('pbVal', POINTER(BYTE)),
        ('piVal', POINTER(SHORT)),
        ('plVal', POINTER(LONG)),
        ('pllVal', POINTER(LONGLONG)),
        ('pfltVal', POINTER(FLOAT)),
        ('pdblVal', POINTER(DOUBLE)),
        ('pBOOLVal', POINTER(VARIANT_BOOL)),
        ('pscode', POINTER(SCODE)),
        ('pcyVal', POINTER(CY)),
        ('pdate', POINTER(DATE)),
        ('pbstrVal', POINTER(wireBSTR)),
        ('ppunkVal', POINTER(POINTER(comtypes.IUnknown))),
        ('ppdispVal', POINTER(POINTER(IDispatch))),
        ('pparray', POINTER(wirePSAFEARRAY)),
        ('pvarVal', POINTER(wireVARIANT)),
        ('cVal', CHAR),
        ('uiVal', USHORT),
        ('ulVal', ULONG),
        ('ullVal', ULONGLONG),
        ('INTVal', INT),
        ('uINTVal', UINT),
        ('decVal', DECIMAL),
        ('pdecVal', POINTER(DECIMAL)),
        ('pcVal', POINTER(CHAR)),
        ('puiVal', POINTER(USHORT)),
        ('pulVal', POINTER(ULONG)),
        ('pullVal', POINTER(ULONGLONG)),
        ('pINTVal', POINTER(INT)),
        ('puINTVal', POINTER(UINT)),
    ]


_wireVARIANT._fields_ = [
    ('clSize', DWORD),
    ('rpcReserved', DWORD),
    ('vt', USHORT),
    ('wReserved1', USHORT),
    ('wReserved2', USHORT),
    ('wReserved3', USHORT),
    ('DUMMYUNIONNAME', DUMMYUNIONNAME),
]

DISPID = LONG
MEMBERID = DISPID
HREFTYPE = DWORD


class tagTYPEKIND(ENUM):
    TKIND_ENUM = 0
    TKIND_RECORD = TKIND_ENUM + 1
    TKIND_MODULE = TKIND_RECORD + 1
    TKIND_INTERFACE = TKIND_MODULE + 1
    TKIND_DISPATCH = TKIND_INTERFACE + 1
    TKIND_COCLASS = TKIND_DISPATCH + 1
    TKIND_ALIAS = TKIND_COCLASS + 1
    TKIND_UNION = TKIND_ALIAS + 1
    TKIND_MAX = TKIND_UNION + 1


TYPEKIND = tagTYPEKIND


class tagTYPEDESC(ctypes.Structure):
    pass


TYPEDESC = tagTYPEDESC



class tagARRAYDESC(ctypes.Structure):
    _fields_ = [
        ('tdescElem', TYPEDESC),
        ('cDims', USHORT),
        ('rgbounds', SAFEARRAYBOUND * 1),
    ]


ARRAYDESC = tagARRAYDESC


class DUMMYUNIONNAME(ctypes.Union):
    _fields_ = [
        ('lptdesc', POINTER(tagTYPEDESC)),
        ('lpadesc', POINTER(tagARRAYDESC)),
        ('hreftype', HREFTYPE),
    ]

try:
    tagTYPEDESC._fields_ = [
        ('DUMMYUNIONNAME', DUMMYUNIONNAME),
        ('vt', VARTYPE),
    ]
except AttributeError:
    pass


class tagPARAMDESCEX(ctypes.Structure):
    _fields_ = [
        ('cBytes', ULONG),
        ('varDefaultValue', VARIANTARG),
    ]


PARAMDESCEX = tagPARAMDESCEX
LPPARAMDESCEX = POINTER(tagPARAMDESCEX)


class tagPARAMDESC(ctypes.Structure):
    _fields_ = [
        ('pparamdescex', LPPARAMDESCEX),
        ('wParamFlags', USHORT),
    ]


PARAMDESC = tagPARAMDESC
LPPARAMDESC = POINTER(tagPARAMDESC)


PARAMFLAG_NONE = 0x0
PARAMFLAG_FIN = 0x1
PARAMFLAG_FOUT = 0x2
PARAMFLAG_FLCID = 0x4
PARAMFLAG_FRETVAL = 0x8
PARAMFLAG_FOPT = 0x10
PARAMFLAG_FHASDEFAULT = 0x20
PARAMFLAG_FHASCUSTDATA = 0x40


class tagIDLDESC(ctypes.Structure):
    _fields_ = [
        ('dwReserved', ULONG_PTR),
        ('wIDLFlags', USHORT),
    ]


IDLDESC = tagIDLDESC
LPIDLDESC = POINTER(tagIDLDESC)


IDLFLAG_NONE = PARAMFLAG_NONE
IDLFLAG_FIN = PARAMFLAG_FIN
IDLFLAG_FOUT = PARAMFLAG_FOUT
IDLFLAG_FLCID = PARAMFLAG_FLCID
IDLFLAG_FRETVAL = PARAMFLAG_FRETVAL


class tagELEMDESC(ctypes.Structure):

    class DUMMYUNIONNAME(ctypes.Union):
        _fields_ = [
            ('idldesc', IDLDESC),
            ('paramdesc', PARAMDESC),
        ]

    _fields_ = [
        ('tdesc', TYPEDESC),
        ('DUMMYUNIONNAME', DUMMYUNIONNAME),
    ]


ELEMDESC = tagELEMDESC
LPELEMDESC = POINTER(tagELEMDESC)


class tagTYPEATTR(ctypes.Structure):
    _fields_ = [
        ('guid', GUID),
        ('lcid', LCID),
        ('dwReserved', DWORD),
        ('memidConstructor', MEMBERID),
        ('memidDestructor', MEMBERID),
        ('lpstrSchema', LPOLESTR),
        ('cbSizeInstance', ULONG),
        ('typekind', TYPEKIND),
        ('cFuncs', WORD),
        ('cVars', WORD),
        ('cImplTypes', WORD),
        ('cbSizeVft', WORD),
        ('cbAlignment', WORD),
        ('wTypeFlags', WORD),
        ('wMajorVerNum', WORD),
        ('wMinorVerNum', WORD),
        ('tdescAlias', TYPEDESC),
        ('idldescType', IDLDESC),
    ]


TYPEATTR = tagTYPEATTR
LPTYPEATTR = POINTER(tagTYPEATTR)


class tagDISPPARAMS(ctypes.Structure):
    _fields_ = [
        ('rgvarg', POINTER(VARIANTARG)),
        ('rgdispidNamedArgs', POINTER(DISPID)),
        ('cArgs', UINT),
        ('cNamedArgs', UINT),
    ]


DISPPARAMS = tagDISPPARAMS


class tagEXCEPINFO(ctypes.Structure):
    _fields_ = [
        ('wCode', WORD),
        ('wReserved', WORD),
        ('bstrSource', BSTR),
        ('bstrDescription', BSTR),
        ('bstrHelpFile', BSTR),
        ('dwHelpContext', DWORD),
        ('pvReserved', PVOID),
        ('pfnDeferredFillIn', HRESULT),
        ('scode', SCODE),
    ]


EXCEPINFO = tagEXCEPINFO
LPEXCEPINFO = POINTER(tagEXCEPINFO)


class tagCALLCONV(ENUM):
    CC_FASTCALL = 0
    CC_CDECL = 1
    CC_MSCPASCAL = CC_CDECL + 1
    CC_PASCAL = CC_MSCPASCAL
    CC_MACPASCAL = CC_PASCAL + 1
    CC_STDCALL = CC_MACPASCAL + 1
    CC_FPFASTCALL = CC_STDCALL + 1
    CC_SYSCALL = CC_FPFASTCALL + 1
    CC_MPWCDECL = CC_SYSCALL + 1
    CC_MPWPASCAL = CC_MPWCDECL + 1
    CC_MAX = CC_MPWPASCAL + 1


CALLCONV = tagCALLCONV


class tagFUNCKIND(ENUM):
    FUNC_VIRTUAL = 0
    FUNC_PUREVIRTUAL = FUNC_VIRTUAL + 1
    FUNC_NONVIRTUAL = FUNC_PUREVIRTUAL + 1
    FUNC_STATIC = FUNC_NONVIRTUAL + 1
    FUNC_DISPATCH = FUNC_STATIC + 1


FUNCKIND = tagFUNCKIND


class tagINVOKEKIND(ENUM):
    INVOKE_FUNC = 1
    INVOKE_PROPERTYGET = 2
    INVOKE_PROPERTYPUT = 4
    INVOKE_PROPERTYPUTREF = 8


INVOKEKIND = tagINVOKEKIND


class tagFUNCDESC(ctypes.Structure):
    _fields_ = [
        ('memid', MEMBERID),
        ('lprgscode', POINTER(SCODE)),
        ('lprgelemdescParam', POINTER(ELEMDESC)),
        ('funckind', FUNCKIND),
        ('invkind', INVOKEKIND),
        ('callconv', CALLCONV),
        ('cParams', SHORT),
        ('cParamsOpt', SHORT),
        ('oVft', SHORT),
        ('cScodes', SHORT),
        ('elemdescFunc', ELEMDESC),
        ('wFuncFlags', WORD),
    ]


FUNCDESC = tagFUNCDESC
LPFUNCDESC = POINTER(tagFUNCDESC)


class tagVARKIND(ENUM):
    VAR_PERINSTANCE = 0
    VAR_STATIC = VAR_PERINSTANCE + 1
    VAR_CONST = VAR_STATIC + 1
    VAR_DISPATCH = VAR_CONST + 1


VARKIND = tagVARKIND


IMPLTYPEFLAG_FDEFAULT = 0x1
IMPLTYPEFLAG_FSOURCE = 0x2
IMPLTYPEFLAG_FRESTRICTED = 0x4
IMPLTYPEFLAG_FDEFAULTVTABLE = 0x8


class tagVARDESC(ctypes.Structure):

    class DUMMYUNIONNAME(ctypes.Union):
        _fields_ = [
            ('oInst', ULONG),
            ('lpvarValue', POINTER(VARIANT)),
        ]

    _fields_ = [
        ('memid', MEMBERID),
        ('lpstrSchema', LPOLESTR),
        ('DUMMYUNIONNAME', DUMMYUNIONNAME),
        ('elemdescVar', ELEMDESC),
        ('wVarFlags', WORD),
        ('varkind', VARKIND),
    ]


VARDESC = tagVARDESC
LPVARDESC = POINTER(tagVARDESC)


class tagTYPEFLAGS(ENUM):
    TYPEFLAG_FAPPOBJECT = 0x1
    TYPEFLAG_FCANCREATE = 0x2
    TYPEFLAG_FLICENSED = 0x4
    TYPEFLAG_FPREDECLID = 0x8
    TYPEFLAG_FHIDDEN = 0x10
    TYPEFLAG_FCONTROL = 0x20
    TYPEFLAG_FDUAL = 0x40
    TYPEFLAG_FNONEXTENSIBLE = 0x80
    TYPEFLAG_FOLEAUTOMATION = 0x100
    TYPEFLAG_FRESTRICTED = 0x200
    TYPEFLAG_FAGGREGATABLE = 0x400
    TYPEFLAG_FREPLACEABLE = 0x800
    TYPEFLAG_FDISPATCHABLE = 0x1000
    TYPEFLAG_FREVERSEBIND = 0x2000
    TYPEFLAG_FPROXY = 0x4000


TYPEFLAGS = tagTYPEFLAGS


class tagFUNCFLAGS(ENUM):
    FUNCFLAG_FRESTRICTED = 0x1
    FUNCFLAG_FSOURCE = 0x2
    FUNCFLAG_FBINDABLE = 0x4
    FUNCFLAG_FREQUESTEDIT = 0x8
    FUNCFLAG_FDISPLAYBIND = 0x10
    FUNCFLAG_FDEFAULTBIND = 0x20
    FUNCFLAG_FHIDDEN = 0x40
    FUNCFLAG_FUSESGETLASTERROR = 0x80
    FUNCFLAG_FDEFAULTCOLLELEM = 0x100
    FUNCFLAG_FUIDEFAULT = 0x200
    FUNCFLAG_FNONBROWSABLE = 0x400
    FUNCFLAG_FREPLACEABLE = 0x800
    FUNCFLAG_FIMMEDIATEBIND = 0x1000


FUNCFLAGS = tagFUNCFLAGS


class tagVARFLAGS(ENUM):
    VARFLAG_FREADONLY = 0x1
    VARFLAG_FSOURCE = 0x2
    VARFLAG_FBINDABLE = 0x4
    VARFLAG_FREQUESTEDIT = 0x8
    VARFLAG_FDISPLAYBIND = 0x10
    VARFLAG_FDEFAULTBIND = 0x20
    VARFLAG_FHIDDEN = 0x40
    VARFLAG_FRESTRICTED = 0x80
    VARFLAG_FDEFAULTCOLLELEM = 0x100
    VARFLAG_FUIDEFAULT = 0x200
    VARFLAG_FNONBROWSABLE = 0x400
    VARFLAG_FREPLACEABLE = 0x800
    VARFLAG_FIMMEDIATEBIND = 0x1000


VARFLAGS = tagVARFLAGS


class tagCLEANLOCALSTORAGE(ctypes.Structure):
    _fields_ = [
        ('pInterface', POINTER(comtypes.IUnknown)),
        ('pStorage', PVOID),
        ('flags', DWORD),
    ]


CLEANLOCALSTORAGE = tagCLEANLOCALSTORAGE


class tagCUSTDATAITEM(ctypes.Structure):
    _fields_ = [
        ('guid', GUID),
        ('varValue', VARIANTARG),
    ]


CUSTDATAITEM = tagCUSTDATAITEM
LPCUSTDATAITEM = POINTER(tagCUSTDATAITEM)


class tagCUSTDATA(ctypes.Structure):
    _fields_ = [
        ('cCustData', DWORD),
        ('prgCustData', LPCUSTDATAITEM),
    ]


CUSTDATA = tagCUSTDATA
LPCUSTDATA = POINTER(tagCUSTDATA)


LPCREATETYPEINFO = POINTER(ICreateTypeInfo)
COMMETHOD = comtypes.COMMETHOD


ICreateTypeInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetGuid',
        (['in'], REFGUID, 'guid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTypeFlags',
        (['in'], UINT, 'uTypeFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDocString',
        (['in'], LPOLESTR, 'pStrDoc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetHelpContext',
        (['in'], DWORD, 'dwHelpContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetVersion',
        (['in'], WORD, 'wMajorVerNum'),
        (['in'], WORD, 'wMinorVerNum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddRefTypeInfo',
        (['in'], POINTER(ITypeInfo), 'pTInfo'),
        (['in'], POINTER(HREFTYPE), 'phRefType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddFuncDesc',
        (['in'], UINT, 'index'),
        (['in'], POINTER(FUNCDESC), 'pFuncDesc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddImplType',
        (['in'], UINT, 'index'),
        (['in'], HREFTYPE, 'hRefType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetImplTypeFlags',
        (['in'], UINT, 'index'),
        (['in'], INT, 'implTypeFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetAlignment',
        (['in'], WORD, 'cbAlignment'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSchema',
        (['in'], LPOLESTR, 'pStrSchema'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddVarDesc',
        (['in'], UINT, 'index'),
        (['in'], POINTER(VARDESC), 'pVarDesc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFuncAndParamNames',
        (['in'], UINT, 'index'),
        (['in'], POINTER(LPOLESTR), 'rgszNames'),
        (['in'], UINT, 'cNames'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetVarName',
        (['in'], UINT, 'index'),
        (['in'], LPOLESTR, 'szName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTypeDescAlias',
        (['in'], POINTER(TYPEDESC), 'pTDescAlias'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DefineFuncAsDllEntry',
        (['in'], UINT, 'index'),
        (['in'], LPOLESTR, 'szDllName'),
        (['in'], LPOLESTR, 'szProcName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFuncDocString',
        (['in'], UINT, 'index'),
        (['in'], LPOLESTR, 'szDocString'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetVarDocString',
        (['in'], UINT, 'index'),
        (['in'], LPOLESTR, 'szDocString'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFuncHelpContext',
        (['in'], UINT, 'index'),
        (['in'], DWORD, 'dwHelpContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetVarHelpContext',
        (['in'], UINT, 'index'),
        (['in'], DWORD, 'dwHelpContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMops',
        (['in'], UINT, 'index'),
        (['in'], BSTR, 'bstrMops'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTypeIdldesc',
        (['in'], POINTER(IDLDESC), 'pIdlDesc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'LayOut'
    ),
]


LPCREATETYPEINFO2 = POINTER(ICreateTypeInfo2)


ICreateTypeInfo2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DeleteFuncDesc',
        (['in'], UINT, 'index'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DeleteFuncDescByMemId',
        (['in'], MEMBERID, 'memid'),
        (['in'], INVOKEKIND, 'invKind'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DeleteVarDesc',
        (['in'], UINT, 'index'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DeleteVarDescByMemId',
        (['in'], MEMBERID, 'memid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DeleteImplType',
        (['in'], UINT, 'index'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetCustData',
        (['in'], REFGUID, 'guid'),
        (['in'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFuncCustData',
        (['in'], UINT, 'index'),
        (['in'], REFGUID, 'guid'),
        (['in'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetParamCustData',
        (['in'], UINT, 'indexFunc'),
        (['in'], UINT, 'indexParam'),
        (['in'], REFGUID, 'guid'),
        (['in'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetVarCustData',
        (['in'], UINT, 'index'),
        (['in'], REFGUID, 'guid'),
        (['in'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetImplTypeCustData',
        (['in'], UINT, 'index'),
        (['in'], REFGUID, 'guid'),
        (['in'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetHelpStringContext',
        (['in'], ULONG, 'dwHelpStringContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFuncHelpStringContext',
        (['in'], UINT, 'index'),
        (['in'], ULONG, 'dwHelpStringContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetVarHelpStringContext',
        (['in'], UINT, 'index'),
        (['in'], ULONG, 'dwHelpStringContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetName',
        (['in'], LPOLESTR, 'szName'),
    ),
]


LPCREATETYPELIB = POINTER(ICreateTypeLib)


ICreateTypeLib._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateTypeInfo',
        (['in'], LPOLESTR, 'szName'),
        (['in'], TYPEKIND, 'tkind'),
        (['out'], POINTER(POINTER(ICreateTypeInfo)), 'ppCTInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetName',
        (['in'], LPOLESTR, 'szName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetVersion',
        (['in'], WORD, 'wMajorVerNum'),
        (['in'], WORD, 'wMinorVerNum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetGuid',
        (['in'], REFGUID, 'guid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDocString',
        (['in'], LPOLESTR, 'szDoc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetHelpFileName',
        (['in'], LPOLESTR, 'szHelpFileName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetHelpContext',
        (['in'], DWORD, 'dwHelpContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetLcid',
        (['in'], LCID, 'lcid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetLibFlags',
        (['in'], UINT, 'uLibFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SaveAllChanges'
    ),
]


LPCREATETYPELIB2 = POINTER(ICreateTypeLib2)


ICreateTypeLib2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DeleteTypeInfo',
        (['in'], LPOLESTR, 'szName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetCustData',
        (['in'], REFGUID, 'guid'),
        (['in'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetHelpStringContext',
        (['in'], ULONG, 'dwHelpStringContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetHelpStringDll',
        (['in'], LPOLESTR, 'szFileName'),
    ),
]


LPDISPATCH = POINTER(IDispatch)


DISPID_UNKNOWN = -1
DISPID_VALUE = 0x0
DISPID_PROPERTYPUT = -3
DISPID_NEWENUM = -4
DISPID_EVALUATE = -5
DISPID_CONSTRUCTOR = -6
DISPID_DESTRUCTOR = -7
DISPID_COLLECT = -8


IDispatch._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeInfoCount',
        (['out'], POINTER(UINT), 'pctinfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeInfo',
        (['in'], UINT, 'iTInfo'),
        (['in'], LCID, 'lcid'),
        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetIDsOfNames',
        (['in'], REFIID, 'riid'),
        (['in'], POINTER(LPOLESTR), 'rgszNames'),
        ([], UINT, 'cNames'),
        (['in'], LCID, 'lcid'),
        (['out'], POINTER(DISPID), 'rgDispId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Invoke',
        (['in'], DISPID, 'dispIdMember'),
        (['in'], REFIID, 'riid'),
        (['in'], LCID, 'lcid'),
        (['in'], WORD, 'wFlags'),
        (['in', 'out'], POINTER(DISPPARAMS), 'pDispParams'),
        (['out'], POINTER(VARIANT), 'pVarResult'),
        (['out'], POINTER(EXCEPINFO), 'pExcepInfo'),
        (['out'], POINTER(UINT), 'puArgErr'),
    ),
]


LPENUMVARIANT = POINTER(IEnumVARIANT)


IEnumVARIANT._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(VARIANT), 'rgVar'),
        (['out'], POINTER(ULONG), 'pCeltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'celt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumVARIANT)), 'ppEnum'),
    ),
]


LPTYPECOMP = POINTER(ITypeComp)


class tagDESCKIND(ENUM):
    DESCKIND_NONE = 0
    DESCKIND_FUNCDESC = DESCKIND_NONE + 1
    DESCKIND_VARDESC = DESCKIND_FUNCDESC + 1
    DESCKIND_TYPECOMP = DESCKIND_VARDESC + 1
    DESCKIND_IMPLICITAPPOBJ = DESCKIND_TYPECOMP + 1
    DESCKIND_MAX = DESCKIND_IMPLICITAPPOBJ + 1


DESCKIND = tagDESCKIND


class tagBINDPTR(ctypes.Union):
    _fields_ = [
        ('lpfuncdesc', POINTER(FUNCDESC)),
        ('lpvardesc', POINTER(VARDESC)),
        ('lptcomp', POINTER(ITypeComp)),
    ]


BINDPTR = tagBINDPTR
LPBINDPTR = POINTER(tagBINDPTR)


ITypeComp._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Bind',
        (['in'], LPOLESTR, 'szName'),
        (['in'], ULONG, 'lHashVal'),
        (['in'], WORD, 'wFlags'),
        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
        (['out'], POINTER(DESCKIND), 'pDescKind'),
        (['out'], POINTER(BINDPTR), 'pBindPtr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'BindType',
        (['in'], LPOLESTR, 'szName'),
        (['in'], ULONG, 'lHashVal'),
        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
        (['out'], POINTER(POINTER(ITypeComp)), 'ppTComp'),
    ),
]


LPTYPEINFO = POINTER(ITypeInfo)


ITypeInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeAttr',
        (['out'], POINTER(POINTER(TYPEATTR)), 'ppTypeAttr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeComp',
        (['out'], POINTER(POINTER(ITypeComp)), 'ppTComp'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFuncDesc',
        (['in'], UINT, 'index'),
        (['out'], POINTER(POINTER(FUNCDESC)), 'ppFuncDesc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetVarDesc',
        (['in'], UINT, 'index'),
        (['out'], POINTER(POINTER(VARDESC)), 'ppVarDesc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNames',
        (['in'], MEMBERID, 'memid'),
        ([], POINTER(BSTR), 'rgBstrNames'),
        (['in'], UINT, 'cMaxNames'),
        (['out'], POINTER(UINT), 'pcNames'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRefTypeOfImplType',
        (['in'], UINT, 'index'),
        (['out'], POINTER(HREFTYPE), 'pRefType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetImplTypeFlags',
        (['in'], UINT, 'index'),
        (['out'], POINTER(INT), 'pImplTypeFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetIDsOfNames',
        (['in'], POINTER(LPOLESTR), 'rgszNames'),
        (['in'], UINT, 'cNames'),
        (['out'], POINTER(MEMBERID), 'pMemId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Invoke',
        (['in'], PVOID, 'pvInstance'),
        (['in'], MEMBERID, 'memid'),
        (['in'], WORD, 'wFlags'),
        (['in', 'out'], POINTER(DISPPARAMS), 'pDispParams'),
        (['out'], POINTER(VARIANT), 'pVarResult'),
        (['out'], POINTER(EXCEPINFO), 'pExcepInfo'),
        (['out'], POINTER(UINT), 'puArgErr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDocumentation',
        (['in'], MEMBERID, 'memid'),
        (['out'], POINTER(BSTR), 'pBstrName'),
        (['out'], POINTER(BSTR), 'pBstrDocString'),
        (['out'], POINTER(DWORD), 'pdwHelpContext'),
        (['out'], POINTER(BSTR), 'pBstrHelpFile'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDllEntry',
        (['in'], MEMBERID, 'memid'),
        (['in'], INVOKEKIND, 'invKind'),
        (['out'], POINTER(BSTR), 'pBstrDllName'),
        (['out'], POINTER(BSTR), 'pBstrName'),
        (['out'], POINTER(WORD), 'pwOrdinal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRefTypeInfo',
        (['in'], HREFTYPE, 'hRefType'),
        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddressOfMember',
        (['in'], MEMBERID, 'memid'),
        (['in'], INVOKEKIND, 'invKind'),
        (['out'], POINTER(PVOID), 'ppv'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateInstance',
        (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(PVOID), 'ppvObj'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMops',
        (['in'], MEMBERID, 'memid'),
        (['out'], POINTER(BSTR), 'pBstrMops'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetContainingTypeLib',
        (['out'], POINTER(POINTER(ITypeLib)), 'ppTLib'),
        (['out'], POINTER(UINT), 'pIndex'),
    ),
    COMMETHOD(
        [],
        VOID,
        'ReleaseTypeAttr',
        (['in'], POINTER(TYPEATTR), 'pTypeAttr'),
    ),
    COMMETHOD(
        [],
        VOID,
        'ReleaseFuncDesc',
        (['in'], POINTER(FUNCDESC), 'pFuncDesc'),
    ),
    COMMETHOD(
        [],
        VOID,
        'ReleaseVarDesc',
        (['in'], POINTER(VARDESC), 'pVarDesc'),
    ),
]


LPTYPEINFO2 = POINTER(ITypeInfo2)


ITypeInfo2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeKind',
        (['out'], POINTER(TYPEKIND), 'pTypeKind'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeFlags',
        (['out'], POINTER(ULONG), 'pTypeFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFuncIndexOfMemId',
        (['in'], MEMBERID, 'memid'),
        (['in'], INVOKEKIND, 'invKind'),
        (['out'], POINTER(UINT), 'pFuncIndex'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetVarIndexOfMemId',
        (['in'], MEMBERID, 'memid'),
        (['out'], POINTER(UINT), 'pVarIndex'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCustData',
        (['in'], REFGUID, 'guid'),
        (['out'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFuncCustData',
        (['in'], UINT, 'index'),
        (['in'], REFGUID, 'guid'),
        (['out'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetParamCustData',
        (['in'], UINT, 'indexFunc'),
        (['in'], UINT, 'indexParam'),
        (['in'], REFGUID, 'guid'),
        (['out'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetVarCustData',
        (['in'], UINT, 'index'),
        (['in'], REFGUID, 'guid'),
        (['out'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetImplTypeCustData',
        (['in'], UINT, 'index'),
        (['in'], REFGUID, 'guid'),
        (['out'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDocumentation2',
        (['in'], MEMBERID, 'memid'),
        (['in'], LCID, 'lcid'),
        (['out'], POINTER(BSTR), 'pbstrHelpString'),
        (['out'], POINTER(DWORD), 'pdwHelpStringContext'),
        (['out'], POINTER(BSTR), 'pbstrHelpStringDll'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllCustData',
        (['out'], POINTER(CUSTDATA), 'pCustData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllFuncCustData',
        (['in'], UINT, 'index'),
        (['out'], POINTER(CUSTDATA), 'pCustData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllParamCustData',
        (['in'], UINT, 'indexFunc'),
        (['in'], UINT, 'indexParam'),
        (['out'], POINTER(CUSTDATA), 'pCustData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllVarCustData',
        (['in'], UINT, 'index'),
        (['out'], POINTER(CUSTDATA), 'pCustData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllImplTypeCustData',
        (['in'], UINT, 'index'),
        (['out'], POINTER(CUSTDATA), 'pCustData'),
    ),
]


class tagSYSKIND(ENUM):
    SYS_WIN16 = 0
    SYS_WIN32 = SYS_WIN16 + 1
    SYS_MAC = SYS_WIN32 + 1
    SYS_WIN64 = SYS_MAC + 1


SYSKIND = tagSYSKIND


class tagLIBFLAGS(ENUM):
    LIBFLAG_FRESTRICTED = 0x1
    LIBFLAG_FCONTROL = 0x2
    LIBFLAG_FHIDDEN = 0x4
    LIBFLAG_FHASDISKIMAGE = 0x8


LIBFLAGS = tagLIBFLAGS
LPTYPELIB = POINTER(ITypeLib)


class tagTLIBATTR(ctypes.Structure):
    _fields_ = [
        ('guid', GUID),
        ('lcid', LCID),
        ('syskind', SYSKIND),
        ('wMajorVerNum', WORD),
        ('wMinorVerNum', WORD),
        ('wLibFlags', WORD),
    ]


TLIBATTR = tagTLIBATTR
LPTLIBATTR = POINTER(tagTLIBATTR)


ITypeLib._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeInfo',
        (['in'], UINT, 'index'),
        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeInfoType',
        (['in'], UINT, 'index'),
        (['out'], POINTER(TYPEKIND), 'pTKind'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeInfoOfGuid',
        (['in'], REFGUID, 'guid'),
        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTinfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLibAttr',
        (['out'], POINTER(POINTER(TLIBATTR)), 'ppTLibAttr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeComp',
        (['out'], POINTER(POINTER(ITypeComp)), 'ppTComp'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDocumentation',
        (['in'], INT, 'index'),
        (['out'], POINTER(BSTR), 'pBstrName'),
        (['out'], POINTER(BSTR), 'pBstrDocString'),
        (['out'], POINTER(DWORD), 'pdwHelpContext'),
        (['out'], POINTER(BSTR), 'pBstrHelpFile'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsName',
        (['in', 'out'], LPOLESTR, 'szNameBuf'),
        (['in'], ULONG, 'lHashVal'),
        (['out'], POINTER(BOOL), 'pfName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FindName',
        (['in', 'out'], LPOLESTR, 'szNameBuf'),
        (['in'], ULONG, 'lHashVal'),
        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
        (['out'], POINTER(MEMBERID), 'rgMemId'),
        (['in', 'out'], POINTER(USHORT), 'pcFound'),
    ),
    COMMETHOD(
        [],
        VOID,
        'ReleaseTLibAttr',
        (['in'], POINTER(TLIBATTR), 'pTLibAttr'),
    ),
]


LPTYPELIB2 = POINTER(ITypeLib2)


ITypeLib2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCustData',
        (['in'], REFGUID, 'guid'),
        (['out'], POINTER(VARIANT), 'pVarVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLibStatistics',
        (['out'], POINTER(ULONG), 'pcUniqueNames'),
        (['out'], POINTER(ULONG), 'pcchUniqueNames'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDocumentation2',
        (['in'], INT, 'index'),
        (['in'], LCID, 'lcid'),
        (['out'], POINTER(BSTR), 'pbstrHelpString'),
        (['out'], POINTER(DWORD), 'pdwHelpStringContext'),
        (['out'], POINTER(BSTR), 'pbstrHelpStringDll'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllCustData',
        (['out'], POINTER(CUSTDATA), 'pCustData'),
    ),
]


LPTYPECHANGEEVENTS = POINTER(ITypeChangeEvents)


class tagCHANGEKIND(ENUM):
    CHANGEKIND_ADDMEMBER = 0
    CHANGEKIND_DELETEMEMBER = CHANGEKIND_ADDMEMBER + 1
    CHANGEKIND_SETNAMES = CHANGEKIND_DELETEMEMBER + 1
    CHANGEKIND_SETDOCUMENTATION = CHANGEKIND_SETNAMES + 1
    CHANGEKIND_GENERAL = CHANGEKIND_SETDOCUMENTATION + 1
    CHANGEKIND_INVALIDATE = CHANGEKIND_GENERAL + 1
    CHANGEKIND_CHANGEFAILED = CHANGEKIND_INVALIDATE + 1
    CHANGEKIND_MAX = CHANGEKIND_CHANGEFAILED + 1


CHANGEKIND = tagCHANGEKIND


ITypeChangeEvents._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RequestTypeChange',
        (['in'], CHANGEKIND, 'changeKind'),
        (['in'], POINTER(ITypeInfo), 'pTInfoBefore'),
        (['in'], LPOLESTR, 'pStrName'),
        (['out'], POINTER(INT), 'pfCancel'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AfterTypeChange',
        (['in'], CHANGEKIND, 'changeKind'),
        (['in'], POINTER(ITypeInfo), 'pTInfoAfter'),
        (['in'], LPOLESTR, 'pStrName'),
    ),
]


LPERRORINFO = POINTER(IErrorInfo)


IErrorInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetGUID',
        (['out'], POINTER(GUID), 'pGUID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSource',
        (['out'], POINTER(BSTR), 'pBstrSource'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDescription',
        (['out'], POINTER(BSTR), 'pBstrDescription'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetHelpFile',
        (['out'], POINTER(BSTR), 'pBstrHelpFile'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetHelpContext',
        (['out'], POINTER(DWORD), 'pdwHelpContext'),
    ),
]


LPCREATEERRORINFO = POINTER(ICreateErrorInfo)


ICreateErrorInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetGUID',
        (['in'], REFGUID, 'rguid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSource',
        (['in'], LPOLESTR, 'szSource'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDescription',
        (['in'], LPOLESTR, 'szDescription'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetHelpFile',
        (['in'], LPOLESTR, 'szHelpFile'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetHelpContext',
        (['in'], DWORD, 'dwHelpContext'),
    ),
]


LPSUPPORTERRORINFO = POINTER(ISupportErrorInfo)


ISupportErrorInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'InterfaceSupportsErrorInfo',
        (['in'], REFIID, 'riid'),
    ),
]


ITypeFactory._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateFromTypeInfo',
        (['in'], POINTER(ITypeInfo), 'pTypeInfo'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppv'),
    ),
]


ITypeMarshal._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Size',
        (['in'], PVOID, 'pvType'),
        (['in'], DWORD, 'dwDestContext'),
        (['in'], PVOID, 'pvDestContext'),
        (['out'], POINTER(ULONG), 'pSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Marshal',
        (['in'], PVOID, 'pvType'),
        (['in'], DWORD, 'dwDestContext'),
        (['in'], PVOID, 'pvDestContext'),
        (['in'], ULONG, 'cbBufferLength'),
        ([], POINTER(BYTE), 'pBuffer'),
        (['out'], POINTER(ULONG), 'pcbWritten'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Unmarshal',
        (['out'], PVOID, 'pvType'),
        (['in'], DWORD, 'dwFlags'),
        (['in'], ULONG, 'cbBufferLength'),
        (['in'], POINTER(BYTE), 'pBuffer'),
        (['out'], POINTER(ULONG), 'pcbRead'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Free',
        (['in'], PVOID, 'pvType'),
    ),
]


LPRECORDINFO = POINTER(IRecordInfo)


IRecordInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RecordInit',
        (['out'], PVOID, 'pvNew'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RecordClear',
        (['in'], PVOID, 'pvExisting'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RecordCopy',
        (['in'], PVOID, 'pvExisting'),
        (['out'], PVOID, 'pvNew'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetGuid',
        (['out'], POINTER(GUID), 'pguid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetName',
        (['out'], POINTER(BSTR), 'pbstrName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSize',
        (['out'], POINTER(ULONG), 'pcbSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTypeInfo',
        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTypeInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetField',
        (['in'], PVOID, 'pvData'),
        (['in'], LPCOLESTR, 'szFieldName'),
        (['out'], POINTER(VARIANT), 'pvarField'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFieldNoCopy',
        (['in'], PVOID, 'pvData'),
        (['in'], LPCOLESTR, 'szFieldName'),
        (['out'], POINTER(VARIANT), 'pvarField'),
        (['out'], POINTER(PVOID), 'ppvDataCArray'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PutField',
        (['in'], ULONG, 'wFlags'),
        (['in', 'out'], PVOID, 'pvData'),
        (['in'], LPCOLESTR, 'szFieldName'),
        (['in'], POINTER(VARIANT), 'pvarField'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PutFieldNoCopy',
        (['in'], ULONG, 'wFlags'),
        (['in', 'out'], PVOID, 'pvData'),
        (['in'], LPCOLESTR, 'szFieldName'),
        (['in'], POINTER(VARIANT), 'pvarField'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFieldNames',
        (['in', 'out'], POINTER(ULONG), 'pcNames'),
        ([], POINTER(BSTR), 'rgBstrNames'),
    ),
    COMMETHOD(
        [],
        BOOL,
        'IsMatchingType',
        (['in'], POINTER(IRecordInfo), 'pRecordInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RecordCreateCopy',
        (['in'], PVOID, 'pvSource'),
        (['out'], POINTER(PVOID), 'ppvDest'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RecordDestroy',
        (['in'], PVOID, 'pvRecord'),
    ),
]


LPERRORLOG = POINTER(IErrorLog)


IErrorLog._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AddError',
        (['in'], LPCOLESTR, 'pszPropName'),
        (['in'], POINTER(EXCEPINFO), 'pExcepInfo'),
    ),
]


LPPROPERTYBAG = POINTER(IPropertyBag)


IPropertyBag._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Read',
        (['in'], LPCOLESTR, 'pszPropName'),
        (['in', 'out'], POINTER(VARIANT), 'pVar'),
        (['in'], POINTER(IErrorLog), 'pErrorLog'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Write',
        (['in'], LPCOLESTR, 'pszPropName'),
        (['in'], POINTER(VARIANT), 'pVar'),
    ),
]


ITypeLibRegistrationReader._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumTypeLibRegistrations',
        (['out'], POINTER(POINTER(IEnumUnknown)), 'ppEnumUnknown'),
    ),
]


IID_ITypeLibRegistration = IID(
    '{76A3E735-02DF-4A12-98EB-043AD3600AF3}'
)


class ITypeLibRegistration(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITypeLibRegistration
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetGuid',
            (['out'], POINTER(GUID), 'pGuid'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetVersion',
            (['out'], POINTER(BSTR), 'pVersion'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetLcid',
            (['out'], POINTER(LCID), 'pLcid'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetWin32Path',
            (['out'], POINTER(BSTR), 'pWin32Path'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetWin64Path',
            (['out'], POINTER(BSTR), 'pWin64Path'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetDisplayName',
            (['out'], POINTER(BSTR), 'pDisplayName'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetFlags',
            (['out'], POINTER(DWORD), 'pFlags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetHelpDir',
            (['out'], POINTER(BSTR), 'pHelpDir'),
        ),
    ]



__all__ = (
    'ITypeInfo', 'ICreateTypeInfo', 'ITypeComp', 'IEnumVARIANT', 'IDispatch',
    'ITypeLibRegistrationReader', 'ISupportErrorInfo', 'ITypeLib', 'HREFTYPE',
    'IErrorInfo', 'ITypeMarshal', 'IRecordInfo', 'ITypeLib2', 'IErrorLog',
    'ICreateTypeInfo2', 'ITypeLibRegistration', 'ICreateErrorInfo', 'DISPID',
    'ICreateTypeLib', 'ITypeInfo2', 'ITypeFactory', 'ITypeChangeEvents',
    'ICreateTypeLib2', 'IPropertyBag', 'DISPID_CONSTRUCTOR', 'IDLFLAG_FIN',
    'IDLFLAG_FRETVAL', 'IMPLTYPEFLAG_FRESTRICTED', 'PARAMFLAG_FHASCUSTDATA',
    'PARAMFLAG_FLCID', 'DISPID_COLLECT', 'FADF_FIXEDSIZE', 'FADF_STATIC',
    'DISPID_NEWENUM', 'FADF_AUTO', 'IMPLTYPEFLAG_FDEFAULTVTABLE', 'FADF_BSTR',
    'FADF_RESERVED', 'FADF_RECORD', 'DISPID_UNKNOWN', 'IDLFLAG_NONE',
    'FADF_EMBEDDED', 'IDLFLAG_FOUT', 'PARAMFLAG_FHASDEFAULT', 'REFVARIANT',
    '__REQUIRED_RPCNDR_H_VERSION__', 'PARAMFLAG_FIN', 'PARAMFLAG_FOUT',
    'DISPID_VALUE', 'FADF_HAVEVARTYPE', 'IMPLTYPEFLAG_FSOURCE', 'tagFUNCKIND',
    'PARAMFLAG_FOPT', 'PARAMFLAG_NONE', 'PARAMFLAG_FRETVAL', 'FADF_HAVEIID',
    '__VARIANT_NAME_1', 'DISPID_EVALUATE', 'IDLFLAG_FLCID', 'FADF_VARIANT',
    'DISPID_PROPERTYPUT', 'IMPLTYPEFLAG_FDEFAULT', 'DISPID_DESTRUCTOR',
    '__REQUIRED_RPCSAL_H_VERSION__', 'FADF_UNKNOWN', 'FADF_DISPATCH',
    'tagSYSKIND', 'tagSF_TYPE', 'tagLIBFLAGS', 'tagFUNCFLAGS', 'tagDESCKIND',
    'tagVARKIND', 'tagCHANGEKIND', 'tagTYPEFLAGS', 'tagCALLCONV', 'CURRENCY',
    'tagINVOKEKIND', 'tagVARFLAGS', 'tagTYPEKIND', 'tagCUSTDATA', 'LPVARIANT',
    '_wireSAFEARRAY', '_wireSAFEARR_HAVEIID', 'tagFUNCDESC', 'tagVARDESC',
    '_wireSAFEARR_BSTR', 'tagCLEANLOCALSTORAGE', 'tagPARAMDESC', 'tagVARIANT',
    '_wireSAFEARR_UNKNOWN', 'tagTYPEATTR', 'tagTLIBATTR', 'tagCUSTDATAITEM',
    '_wireBRECORD', 'tagDISPPARAMS', '_wireSAFEARR_DISPATCH', 'tagTYPEDESC',
    '_wireSAFEARRAY_UNION', 'tagIDLDESC', 'tagSAFEARRAYBOUND', '_wireVARIANT',
    'tagELEMDESC', 'tagARRAYDESC', 'tagEXCEPINFO', 'tagSAFEARRAY', 'MEMBERID',
    '_wireSAFEARR_BRECORD', 'tagPARAMDESCEX', '_wireSAFEARR_VARIANT',
    'tagBINDPTR', 'LPVARIANTARG', 'LPERRORINFO', 'wirePSAFEARRAY',
    'LPSUPPORTERRORINFO', 'LPCREATETYPELIB2', 'LPCREATETYPEINFO', 'LPTYPELIB',
    'VARIANTARG', 'LPTYPEINFO', 'LPTYPECOMP', 'LPCREATETYPELIB', 'LPTYPELIB2',
    'LPCREATETYPEINFO2', 'LPTYPEINFO2', 'LPENUMVARIANT', 'LPERRORLOG',
    'LPCREATEERRORINFO', 'LPTYPECHANGEEVENTS', 'LPDISPATCH', 'LPRECORDINFO',
    'LPSAFEARRAY', 'LPPROPERTYBAG', 'VARIANT',
)
