__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import * # NOQA
# from .rpcndr_h import * # NOQA
# from .windows_h import * # NOQA
# from .ole2_h import * # NOQA
# from .objidl_h import * # NOQA
# from .oaidl_h import * # NOQA
from .winapifamily_h import * # NOQA

from .wtypes_h import (
    POINTER,
    HRESULT,
    LPOLESTR,
    DWORD,
    REFCLSID,
    REFFMTID,
    CLSID,
    UCHAR,
    LONG,
    BYTE,
    FMTID,
    LPSTR,
    LPWSTR,
    WORD,
    BSTR,
    DATE,
    BSTRBLOB,
    DECIMAL,
    CHAR,
    UBYTE,
    SHORT,
    USHORT,
    INT,
    ULONG,
    UINT,
    LARGE_INTEGER,
    ULARGE_INTEGER,
    FLOAT,
    DOUBLE,
    VARIANT_BOOL,
    SCODE,
    LONGLONG,
    FILETIME,
    STRING,
    WSTRING,
    ULONGLONG,
    PROPID,
    FLAGGED_WORD_BLOB,
    HYPER_SIZEDARR,
    BYTE_SIZEDARR,
    SHORT_SIZEDARR,
    LONG_SIZEDARR,
    BLOB,
    CLIPDATA,
    VARTYPE
)
from .minwindef_h import (
    HIWORD,
    LOBYTE,
    LOWORD,
    HIBYTE
)
from .propkeydef_h import PROPERTYKEY
from .oaidl_h import VARIANT
from .guiddef_h import IID, GUID
import ctypes
import comtypes

from comtypes.automation import (
    IDispatch
)

from comtypes.typeinfo import (
    tagSAFEARRAYBOUND,
    tagTYPEDESC,
    tagARRAYDESC,
    IRecordInfo
)



ole32 = ctypes.windll.Ole32


# Flags for IPropertySetStorage::Create
PROPSETFLAG_DEFAULT = 0x0
PROPSETFLAG_NONSIMPLE = 0x1
PROPSETFLAG_ANSI = 0x2
# (This flag is only supported on StgCreatePropStg & StgOpenPropStg
PROPSETFLAG_UNBUFFERED = 0x4
# (This flag causes a version-1 property set to be created
PROPSETFLAG_CASE_SENSITIVE = 0x8
# Flags for the reserved PID_BEHAVIOR property
PROPSET_BEHAVIOR_CASE_SENSITIVE = 0x1

IID_IPropertyStore = IID(
    '{886D8EEB-8CF2-4446-8D02-CDBA1DBDCF99}'
)
IID_IPropertyStorage = IID(
    '{00000138-0000-0000-C000-000000000046}'
)
IID_IPropertySetStorage = IID(
    '{0000013A-0000-0000-C000-000000000046}'
)
IID_IEnumSTATPROPSTG = IID(
    '{00000139-0000-0000-C000-000000000046}'
)
IID_IEnumSTATPROPSETSTG = IID(
    '{0000013B-0000-0000-C000-000000000046}'
)
IID_ISequentialStream = IID(
    '{0C733A30-2A1C-11CE-ADE5-00AA0044773D}'
)
IID_IStream = IID(
    '{0000000C-0000-0000-C000-000000000046}'
)
IID_IStorage = IID(
    '{0000000B-0000-0000-C000-000000000046}'
)
IID_IEnumSTATSTG = IID(
    '{0000000D-0000-0000-C000-000000000046}'
)


class IPropertyStore(comtypes.IUnknown):
    _case_insensitive_ = True
    u'Simple Property Store Interface'
    _iid_ = IID_IPropertyStore
    _idlflags_ = []

    def GetValue(self, key):
        value = PROPVARIANT()
        self.__com_GetValue(key, ctypes.byref(value))

        # Types for vt defined here:
        # https://msdn.microsoft.com/en-us/library/windows/
        # desktop/aa380072%28v=vs.85%29.aspx

        vt = value.vt
        vc = getattr(value, '__MIDL____MIDL_itf_mmdeviceapi_0003_00850001')

        if vt in (0, 1):
            return None
        if vt == 14:
            return vc.decVal
        if vt == 73:
            return vc.pVersionedStream
        if vt in (69, 67):
            return vc.pStorage
        if vt in (68, 66):
            return vc.pStream
        if vt == 9:
            return vc.pdispVal
        if vt == 13:
            return vc.punkVal
        if vt == 31:
            return vc.pwszVal
        if vt == 30:
            return vc.pszVal
        if vt in (70, 65):
            return vc.blob
        if vt == 0xfff:
            return vc.bstrblobVal
        if vt == 8:
            return vc.bstrVal
        if vt == 71:
            return vc.pclipdata
        if vt == 72:
            return vc.puuid
        if vt == 64:
            return vc.filetime
        if vt == 7:
            return vc.date
        if vt == 6:
            return vc.cyVal
        if vt == 10:
            return vc.scode
        if vt == 11:
            return vc.boolVal
        if vt == 5:
            return vc.dblVal
        if vt == 4:
            return vc.fltVal
        if vt == 21:
            return vc.uhVal
        if vt == 20:
            return vc.hVal
        if vt == 23:
            return vc.uintVal
        if vt == 22:
            return vc.intVal
        if vt == 19:
            return vc.ulVal
        if vt == 3:
            return vc.lVal
        if vt == 18:
            return vc.uiVal
        if vt == 2:
            return vc.iVal
        if vt == 17:
            return vc.bVal
        if vt == 16:
            return vc.cVal


class IPropertyStorage(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyStorage
    _idlflags_ = []


class IPropertySetStorage(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertySetStorage
    _idlflags_ = []


class IEnumSTATPROPSTG(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumSTATPROPSTG
    _idlflags_ = []


class IEnumSTATPROPSETSTG(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumSTATPROPSETSTG
    _idlflags_ = []


class ISequentialStream(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISequentialStream
    _idlflags_ = []


class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = IID_IStream
    _idlflags_ = []


class IStorage(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IStorage
    _idlflags_ = []


class IEnumSTATSTG(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumSTATSTG
    _idlflags_ = []


LPPROPERTYSTORAGE = POINTER(IPropertyStorage)
LPPROPERTYSETSTORAGE = POINTER(IPropertySetStorage)
LPENUMSTATPROPSTG = POINTER(IEnumSTATPROPSTG)
LPENUMSTATPROPSETSTG = POINTER(IEnumSTATPROPSETSTG)


class tagVersionedStream(ctypes.Structure):
    _fields_ = [
        ('guidVersion', GUID),
        ('pStream', POINTER(IStream)),
    ]


VERSIONEDSTREAM = tagVersionedStream
LPVERSIONEDSTREAM = POINTER(tagVersionedStream)


class tagCAC(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(CHAR)),
    ]


CAC = tagCAC


class tagCAUB(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(UCHAR)),
    ]


CAUB = tagCAUB


class tagCAI(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(SHORT)),
    ]


CAI = tagCAI


class tagCAUI(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(USHORT)),
    ]


CAUI = tagCAUI


class tagCAL(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(LONG)),
    ]


CAL = tagCAL


class tagCAUL(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(ULONG)),
    ]


CAUL = tagCAUL


class tagCAFLT(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(FLOAT)),
    ]


CAFLT = tagCAFLT


class tagCADBL(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(DOUBLE)),
    ]


CADBL = tagCADBL


class tagCY(ctypes.Structure):
    _fields_ = [
        ('Lo', ULONG),
        ('Hi', LONG)
    ]


CY = tagCY


class tagCACY(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(CY)),
    ]


CACY = tagCACY


class tagCADATE(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(DATE)),
    ]


CADATE = tagCADATE


class tagCABSTR(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(BSTR)),
    ]


CABSTR = tagCABSTR


class tagCABSTRBLOB(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(BSTRBLOB)),
    ]


CABSTRBLOB = tagCABSTRBLOB


class tagCABOOL(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(VARIANT_BOOL)),
    ]


CABOOL = tagCABOOL


class tagCASCODE(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(SCODE)),
    ]


CASCODE = tagCASCODE


class tagPROPVARIANT(ctypes.Structure):
    pass


PROPVARIANT = tagPROPVARIANT


class tagCAPROPVARIANT(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(PROPVARIANT)),
    ]


CAPROPVARIANT = tagCAPROPVARIANT


class tagCAH(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(LARGE_INTEGER)),
    ]


CAH = tagCAH


class tagCAUH(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(ULARGE_INTEGER)),
    ]


CAUH = tagCAUH


class tagCALPSTR(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(LPSTR)),
    ]


CALPSTR = tagCALPSTR


class tagCALPWSTR(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(LPWSTR)),
    ]


CALPWSTR = tagCALPWSTR


class tagCAFILETIME(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(FILETIME)),
    ]


CAFILETIME = tagCAFILETIME


class tagCACLIPDATA(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(CLIPDATA)),
    ]


CACLIPDATA = tagCACLIPDATA


class tagCACLSID(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(CLSID)),
    ]


CACLSID = tagCACLSID

PROPVAR_PAD1 = WORD
PROPVAR_PAD2 = WORD
PROPVAR_PAD3 = WORD


class _wireSAFEARR_DISPATCH(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('apDispatch', POINTER(POINTER(IDispatch))),
    ]


class _wireSAFEARRAY(ctypes.Structure):
    pass


wirePSAFEARRAY = POINTER(POINTER(_wireSAFEARRAY))


class __MIDL_IOleAutomationTypes_0005(ctypes.Union):
    pass


__MIDL_IOleAutomationTypes_0005._fields_ = [
    ('lptdesc', POINTER(tagTYPEDESC)),
    ('lpadesc', POINTER(tagARRAYDESC)),
    ('hreftype', ULONG),
]


class _wireSAFEARR_UNKNOWN(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('apUnknown', POINTER(POINTER(comtypes.IUnknown))),
    ]


class _wireSAFEARR_VARIANT(ctypes.Structure):
    pass


class _wireVARIANT(ctypes.Structure):
    pass


_wireSAFEARR_VARIANT._fields_ = [
    ('Size', ULONG),
    ('aVariant', POINTER(POINTER(_wireVARIANT))),
]


class __MIDL_IOleAutomationTypes_0006(ctypes.Union):
    pass


__MIDL_IOleAutomationTypes_0006._fields_ = [
    ('oInst', ULONG),
    ('lpvarValue', POINTER(VARIANT)),
]


class __MIDL_IOleAutomationTypes_0004(ctypes.Union):
    pass


class _wireBRECORD(ctypes.Structure):
    pass


__MIDL_IOleAutomationTypes_0004._fields_ = [
    ('llVal', LONGLONG),
    ('lVal', INT),
    ('bVal', UBYTE),
    ('iVal', SHORT),
    ('fltVal', FLOAT),
    ('dblVal', DOUBLE),
    ('boolVal', VARIANT_BOOL),
    ('scode', SCODE),
    ('cyVal', CY),
    ('date', DOUBLE),
    ('bstrVal', POINTER(FLAGGED_WORD_BLOB)),
    ('punkVal', POINTER(comtypes.IUnknown)),
    ('pdispVal', POINTER(IDispatch)),
    ('parray', POINTER(POINTER(_wireSAFEARRAY))),
    ('brecVal', POINTER(_wireBRECORD)),
    ('pbVal', POINTER(UBYTE)),
    ('piVal', POINTER(SHORT)),
    ('plVal', POINTER(INT)),
    ('pllVal', POINTER(LONGLONG)),
    ('pfltVal', POINTER(FLOAT)),
    ('pdblVal', POINTER(DOUBLE)),
    ('pboolVal', POINTER(VARIANT_BOOL)),
    ('pscode', POINTER(SCODE)),
    ('pcyVal', POINTER(CY)),
    ('pdate', POINTER(DOUBLE)),
    ('pbstrVal', POINTER(POINTER(FLAGGED_WORD_BLOB))),
    ('ppunkVal', POINTER(POINTER(comtypes.IUnknown))),
    ('ppdispVal', POINTER(POINTER(IDispatch))),
    ('pparray', POINTER(POINTER(POINTER(_wireSAFEARRAY)))),
    ('pvarVal', POINTER(POINTER(_wireVARIANT))),
    ('cVal', CHAR),
    ('uiVal', USHORT),
    ('ulVal', ULONG),
    ('ullVal', ULONGLONG),
    ('intVal', INT),
    ('uintVal', UINT),
    ('decVal', DECIMAL),
    ('pdecVal', POINTER(DECIMAL)),
    ('pcVal', STRING),
    ('puiVal', POINTER(USHORT)),
    ('pulVal', POINTER(ULONG)),
    ('pullVal', POINTER(ULONGLONG)),
    ('pintVal', POINTER(INT)),
    ('puintVal', POINTER(UINT)),
]
_wireVARIANT._fields_ = [
    ('clSize', ULONG),
    ('rpcReserved', ULONG),
    ('vt', USHORT),
    ('wReserved1', USHORT),
    ('wReserved2', USHORT),
    ('wReserved3', USHORT),
    ('DUMMYUNIONNAME', __MIDL_IOleAutomationTypes_0004),
]


class __MIDL_IOleAutomationTypes_0001(ctypes.Union):
    pass


class _wireSAFEARR_BSTR(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('aBstr', POINTER(POINTER(FLAGGED_WORD_BLOB))),
    ]


class _wireSAFEARR_BRECORD(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('aRecord', POINTER(POINTER(_wireBRECORD))),
    ]


class _wireSAFEARR_HAVEIID(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('apUnknown', POINTER(POINTER(comtypes.IUnknown))),
        ('iid', GUID),
    ]


__MIDL_IOleAutomationTypes_0001._fields_ = [
    ('BstrStr', _wireSAFEARR_BSTR),
    ('UnknownStr', _wireSAFEARR_UNKNOWN),
    ('DispatchStr', _wireSAFEARR_DISPATCH),
    ('VariantStr', _wireSAFEARR_VARIANT),
    ('RecordStr', _wireSAFEARR_BRECORD),
    ('HaveIidStr', _wireSAFEARR_HAVEIID),
    ('ByteStr', BYTE_SIZEDARR),
    ('WordStr', SHORT_SIZEDARR),
    ('LongStr', LONG_SIZEDARR),
    ('HyperStr', HYPER_SIZEDARR),
]


class tagRemSNB(ctypes.Structure):
    _fields_ = [
        ('ulCntStr', ULONG),
        ('ulCntChar', ULONG),
        ('rgString', POINTER(USHORT)),
    ]


class _wireSAFEARRAY_UNION(ctypes.Structure):
    pass


_wireSAFEARRAY_UNION._fields_ = [
    ('sfType', ULONG),
    ('u', __MIDL_IOleAutomationTypes_0001),
]

_wireSAFEARRAY._fields_ = [
    ('cDims', USHORT),
    ('fFeatures', USHORT),
    ('cbElements', ULONG),
    ('cLocks', ULONG),
    ('uArrayStructs', _wireSAFEARRAY_UNION),
    ('rgsabound', POINTER(tagSAFEARRAYBOUND)),
]

_wireBRECORD._fields_ = [
    ('fFlags', ULONG),
    ('clSize', ULONG),
    ('pRecInfo', POINTER(IRecordInfo)),
    ('pRecord', POINTER(UBYTE)),
]


wireSNB = POINTER(tagRemSNB)


class __MIDL___MIDL_itf_mmdeviceapi_0003_0085_0001(ctypes.Union):
    _fields_ = [
        ('cVal', CHAR),
        ('bVal', UBYTE),
        ('iVal', SHORT),
        ('uiVal', USHORT),
        ('lVal', INT),
        ('ulVal', ULONG),
        ('intVal', INT),
        ('uintVal', UINT),
        ('hVal', LARGE_INTEGER),
        ('uhVal', ULARGE_INTEGER),
        ('fltVal', FLOAT),
        ('dblVal', DOUBLE),
        ('boolVal', VARIANT_BOOL),
        ('bool', VARIANT_BOOL),
        ('scode', SCODE),
        ('cyVal', CY),
        ('date', DOUBLE),
        ('filetime', FILETIME),
        ('puuid', POINTER(GUID)),
        ('pClipData', POINTER(CLIPDATA)),
        ('bstrVal', BSTR),
        ('bstrblobVal', BSTRBLOB),
        ('blob', BLOB),
        ('pszVal', STRING),
        ('pwszVal', WSTRING),
        ('punkVal', POINTER(comtypes.IUnknown)),
        ('pdispVal', POINTER(IDispatch)),
        ('pStream', POINTER(IStream)),
        ('pStorage', POINTER(IStorage)),
        ('pVersionedStream', POINTER(VERSIONEDSTREAM)),
        ('parray', wirePSAFEARRAY),
        ('cac', CAC),
        ('caub', CAUB),
        ('cai', CAI),
        ('caui', CAUI),
        ('cal', CAL),
        ('caul', CAUL),
        ('cah', CAH),
        ('cauh', CAUH),
        ('caflt', CAFLT),
        ('cadbl', CADBL),
        ('cabool', CABOOL),
        ('cascode', CASCODE),
        ('cacy', CACY),
        ('cadate', CADATE),
        ('cafiletime', CAFILETIME),
        ('cauuid', CACLSID),
        ('caclipdata', CACLIPDATA),
        ('cabstr', CABSTR),
        ('cabstrblob', CABSTRBLOB),
        ('calpstr', CALPSTR),
        ('calpwstr', CALPWSTR),
        ('capropvar', CAPROPVARIANT),
        ('pcVal', STRING),
        ('pbVal', POINTER(UBYTE)),
        ('piVal', POINTER(SHORT)),
        ('puiVal', POINTER(USHORT)),
        ('plVal', POINTER(INT)),
        ('pulVal', POINTER(ULONG)),
        ('pintVal', POINTER(INT)),
        ('puintVal', POINTER(UINT)),
        ('pfltVal', POINTER(FLOAT)),
        ('pdblVal', POINTER(DOUBLE)),
        ('pboolVal', POINTER(VARIANT_BOOL)),
        ('pdecVal', POINTER(DECIMAL)),
        ('pscode', POINTER(SCODE)),
        ('pcyVal', POINTER(CY)),
        ('pdate', POINTER(DOUBLE)),
        ('pbstrVal', POINTER(BSTR)),
        ('ppunkVal', POINTER(POINTER(comtypes.IUnknown))),
        ('ppdispVal', POINTER(POINTER(IDispatch))),
        ('pparray', POINTER(wirePSAFEARRAY)),
        ('pvarVal', POINTER(PROPVARIANT)),
    ]


tagPROPVARIANT._fields_ = [
    ('vt', USHORT),
    ('wReserved1', UBYTE),
    ('wReserved2', UBYTE),
    ('wReserved3', ULONG),
    (
        '__MIDL____MIDL_itf_mmdeviceapi_0003_00850001',
        __MIDL___MIDL_itf_mmdeviceapi_0003_0085_0001
    ),
]


PPROPVARIANT = POINTER(PROPVARIANT)
LPPROPVARIANT = POINTER(PROPVARIANT)
REFPROPVARIANT = POINTER(PROPVARIANT)
# MIDL_PASS
# Reserved global Property IDs
PID_DICTIONARY = 0x0
PID_CODEPAGE = 0x1
PID_FIRST_USABLE = 0x2
PID_FIRST_NAME_DEFAULT = 0xFFF
PID_LOCALE = 0x80000000
PID_MODIFY_TIME = 0x80000001
PID_SECURITY = 0x80000002
PID_BEHAVIOR = 0x80000003
PID_ILLEGAL = 0xFFFFFFFF
# Range which is read-only to downlevel implementations
PID_MIN_READONLY = 0x80000000
PID_MAX_READONLY = 0xBFFFFFFF
PRSPEC_INVALID = 0xFFFFFFFF
PRSPEC_LPWSTR = 0x0
PRSPEC_PROPID = 0x1


class tagPROPSPEC(ctypes.Structure):
    class DUMMYUNIONNAME(ctypes.Union):
        _fields_ = [
            ('propid', PROPID),
            ('lpwstr', LPOLESTR)
        ]

    _fields_ = [
        ('ulKind', ULONG),
        ('DUMMYUNIONNAME', DUMMYUNIONNAME)
    ]


PROPSPEC = tagPROPSPEC


class tagSTATPROPSTG(ctypes.Structure):
    _fields_ = [
        ('lpwstrName', LPOLESTR),
        ('propid', PROPID),
        ('vt', VARTYPE),
    ]


STATPROPSTG = tagSTATPROPSTG


def PROPSETHDR_OSVER_KIND(dwOSVer):
    return HIWORD(dwOSVer)


def PROPSETHDR_OSVER_MAJOR(dwOSVer):
    return LOBYTE(LOWORD(dwOSVer))


def PROPSETHDR_OSVER_MINOR(dwOSVer):
    return HIBYTE(LOWORD(dwOSVer))


PROPSETHDR_OSVERSION_UNKNOWN = 0xFFFFFFFF


class tagSTATPROPSETSTG(ctypes.Structure):
    _fields_ = [
        ('fmtid', FMTID),
        ('clsid', CLSID),
        ('grfFlags', DWORD),
        ('mtime', FILETIME),
        ('ctime', FILETIME),
        ('atime', FILETIME),
        ('dwOSVersion', DWORD),
    ]


STATPROPSETSTG = tagSTATPROPSETSTG


class tagSTATSTG(ctypes.Structure):
    _fields_ = [
        ('pwcsName', WSTRING),
        ('type', ULONG),
        ('cbSize', ULARGE_INTEGER),
        ('mtime', FILETIME),
        ('ctime', FILETIME),
        ('atime', FILETIME),
        ('grfMode', ULONG),
        ('grfLocksSupported', ULONG),
        ('clsid', GUID),
        ('grfStateBits', ULONG),
        ('reserved', ULONG),
    ]


STATSTG = tagSTATSTG


COMMETHOD = comtypes.COMMETHOD


IPropertyStore._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCount',
        (['out'], POINTER(ULONG), 'cProps')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAt',
        (['in'], ULONG, 'iProp'),
        (['out'], POINTER(PROPERTYKEY), 'pkey')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetValue',
        (['in'], POINTER(PROPERTYKEY), 'key'),
        (['out'], POINTER(PROPVARIANT), 'pv')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetValue',
        (['in'], POINTER(PROPERTYKEY), 'key'),
        (['in'], POINTER(PROPVARIANT), 'propvar')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Commit'
    ),
]


IPropertyStorage._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ReadMultiple',
        (['in'], ULONG, 'cpspec'),
        (['in'], PROPSPEC * 1, 'rgpspec'),
        (['out'], PROPVARIANT * 1, 'rgpropvar'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'WriteMultiple',
        (['in'], ULONG, 'cpspec'),
        (['in'], PROPSPEC * 1, 'rgpspec'),
        (['in'], PROPVARIANT * 1, 'rgpropvar'),
        (['in'], PROPID, 'propidNameFirst'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DeleteMultiple',
        (['in'], ULONG, 'cpspec'),
        (['in'], PROPSPEC * 1, 'rgpspec'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReadPropertyNames',
        (['in'], ULONG, 'cpropid'),
        (['in'], PROPID * 1, 'rgpropid'),
        (['out'], LPOLESTR * 1, 'rglpwstrName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'WritePropertyNames',
        (['in'], ULONG, 'cpropid'),
        (['in'], PROPID * 1, 'rgpropid'),
        (['in'], LPOLESTR * 1, 'rglpwstrName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DeletePropertyNames',
        (['in'], ULONG, 'cpropid'),
        (['in'], PROPID * 1, 'rgpropid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Commit',
        (['in'], DWORD, 'grfCommitFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Enum',
        (['out'], POINTER(POINTER(IEnumSTATPROPSTG)), 'ppenum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTimes',
        (['in'], POINTER(FILETIME), 'pctime'),
        (['in'], POINTER(FILETIME), 'patime'),
        (['in'], POINTER(FILETIME), 'pmtime'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetClass',
        (['in'], REFCLSID, 'clsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Stat',
        (['out'], POINTER(STATPROPSETSTG), 'pstatpsstg'),
    ),
]


IEnumSTATPROPSTG._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(STATPROPSTG), 'rgelt'),
        (['out'], POINTER(ULONG), 'pceltFetched'),
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
        (['out'], POINTER(POINTER(IEnumSTATPROPSTG)), 'ppenum'),
    ),
]


IEnumSTATPROPSETSTG._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(STATPROPSETSTG), 'rgelt'),
        (['out'], POINTER(ULONG), 'pceltFetched'),
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
        (['out'], POINTER(POINTER(IEnumSTATPROPSETSTG)), 'ppenum'),
    ),
]


IPropertySetStorage._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Create',
        (['in'], REFFMTID, 'rfmtid'),
        (['in'], POINTER(CLSID), 'pclsid'),
        (['in'], DWORD, 'grfFlags'),
        (['in'], DWORD, 'grfMode'),
        (['out'], POINTER(POINTER(IPropertyStorage)), 'ppprstg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Open',
        (['in'], REFFMTID, 'rfmtid'),
        (['in'], DWORD, 'grfMode'),
        (['out'], POINTER(POINTER(IPropertyStorage)), 'ppprstg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Delete',
        (['in'], REFFMTID, 'rfmtid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Enum',
        (['out'], POINTER(POINTER(IEnumSTATPROPSETSTG)), 'ppenum'),
    ),
]


ISequentialStream._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RemoteRead',
        (['out'], POINTER(UBYTE), 'pv'),
        (['in'], ULONG, 'cb'),
        (['out'], POINTER(ULONG), 'pcbRead')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoteWrite',
        (['in'], POINTER(UBYTE), 'pv'),
        (['in'], ULONG, 'cb'),
        (['out'], POINTER(ULONG), 'pcbWritten')
    ),
]


IStream._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RemoteSeek',
        (['in'], LARGE_INTEGER, 'dlibMove'),
        (['in'], ULONG, 'dwOrigin'),
        (['out'], POINTER(ULARGE_INTEGER), 'plibNewPosition')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSize',
        (['in'], ULARGE_INTEGER, 'libNewSize')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoteCopyTo',
        (['in'], POINTER(IStream), 'pstm'),
        (['in'], ULARGE_INTEGER, 'cb'),
        (['out'], POINTER(ULARGE_INTEGER), 'pcbRead'),
        (['out'], POINTER(ULARGE_INTEGER), 'pcbWritten')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Commit',
        (['in'], ULONG, 'grfCommitFlags')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Revert'
    ),
    COMMETHOD(
        [],
        HRESULT,
        'LockRegion',
        (['in'], ULARGE_INTEGER, 'libOffset'),
        (['in'], ULARGE_INTEGER, 'cb'),
        (['in'], ULONG, 'dwLockType')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnlockRegion',
        (['in'], ULARGE_INTEGER, 'libOffset'),
        (['in'], ULARGE_INTEGER, 'cb'),
        (['in'], ULONG, 'dwLockType')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Stat',
        (['out'], POINTER(STATSTG), 'pstatstg'),
        (['in'], ULONG, 'grfStatFlag')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IStream)), 'ppstm')
    ),
]


IEnumSTATSTG._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RemoteNext',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(tagSTATSTG), 'rgelt'),
        (['out'], POINTER(ULONG), 'pceltFetched')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'celt')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Reset'
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum')
    ),
]


IStorage._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateStream',
        (['in'], WSTRING, 'pwcsName'),
        (['in'], ULONG, 'grfMode'),
        (['in'], ULONG, 'reserved1'),
        (['in'], ULONG, 'reserved2'),
        (['out'], POINTER(POINTER(IStream)), 'ppstm')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoteOpenStream',
        (['in'], WSTRING, 'pwcsName'),
        (['in'], ULONG, 'cbReserved1'),
        (['in'], POINTER(UBYTE), 'reserved1'),
        (['in'], ULONG, 'grfMode'),
        (['in'], ULONG, 'reserved2'),
        (['out'], POINTER(POINTER(IStream)), 'ppstm')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateStorage',
        (['in'], WSTRING, 'pwcsName'),
        (['in'], ULONG, 'grfMode'),
        (['in'], ULONG, 'reserved1'),
        (['in'], ULONG, 'reserved2'),
        (['out'], POINTER(POINTER(IStorage)), 'ppstg')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OpenStorage',
        (['in'], WSTRING, 'pwcsName'),
        (['in'], POINTER(IStorage), 'pstgPriority'),
        (['in'], ULONG, 'grfMode'),
        (['in'], wireSNB, 'snbExclude'),
        (['in'], ULONG, 'reserved'),
        (['out'], POINTER(POINTER(IStorage)), 'ppstg')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoteCopyTo',
        (['in'], ULONG, 'ciidExclude'),
        (['in'], POINTER(GUID), 'rgiidExclude'),
        (['in'], wireSNB, 'snbExclude'),
        (['in'], POINTER(IStorage), 'pstgDest')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'MoveElementTo',
        (['in'], WSTRING, 'pwcsName'),
        (['in'], POINTER(IStorage), 'pstgDest'),
        (['in'], WSTRING, 'pwcsNewName'),
        (['in'], ULONG, 'grfFlags')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Commit',
        (['in'], ULONG, 'grfCommitFlags')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Revert'
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoteEnumElements',
        (['in'], ULONG, 'reserved1'),
        (['in'], ULONG, 'cbReserved2'),
        (['in'], POINTER(UBYTE), 'reserved2'),
        (['in'], ULONG, 'reserved3'),
        (['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DestroyElement',
        (['in'], WSTRING, 'pwcsName')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RenameElement',
        (['in'], WSTRING, 'pwcsOldName'),
        (['in'], WSTRING, 'pwcsNewName')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetElementTimes',
        (['in'], WSTRING, 'pwcsName'),
        (['in'], POINTER(FILETIME), 'pctime'),
        (['in'], POINTER(FILETIME), 'patime'),
        (['in'], POINTER(FILETIME), 'pmtime')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetClass',
        (['in'], POINTER(GUID), 'clsid')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetStateBits',
        (['in'], ULONG, 'grfStateBits'),
        (['in'], ULONG, 'grfMask')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Stat',
        (['out'], POINTER(tagSTATSTG), 'pstatstg'),
        (['in'], ULONG, 'grfStatFlag')
    ),
]


PIPropertyStore = POINTER(IPropertyStore)

# from .coml2api_h import * # NOQA
# Property IDs for the DiscardableInformation Property Set
# VT_BLOB
PIDDI_THUMBNAIL = 0x00000002
# Property IDs for the SummaryInformation Property Set
# VT_LPSTR
# VT_LPSTR
PIDSI_TITLE = 0x00000002
# VT_LPSTR
PIDSI_SUBJECT = 0x00000003
# VT_LPSTR
PIDSI_AUTHOR = 0x00000004
# VT_LPSTR
PIDSI_KEYWORDS = 0x00000005
# VT_LPSTR
PIDSI_COMMENTS = 0x00000006
# VT_LPSTR
PIDSI_TEMPLATE = 0x00000007
# VT_LPSTR
PIDSI_LASTAUTHOR = 0x00000008
# VT_FILETIME (UTC)
PIDSI_REVNUMBER = 0x00000009
# VT_FILETIME (UTC)
PIDSI_EDITTIME = 0x0000000a
# VT_FILETIME (UTC)
PIDSI_LASTPRINTED = 0x0000000b
# VT_FILETIME (UTC)
PIDSI_CREATE_DTM = 0x0000000c
# VT_I4
PIDSI_LASTSAVE_DTM = 0x0000000d
# VT_I4
PIDSI_PAGECOUNT = 0x0000000e
# VT_I4
PIDSI_WORDCOUNT = 0x0000000f
# VT_CF
PIDSI_CHARCOUNT = 0x00000010
# VT_LPSTR
PIDSI_THUMBNAIL = 0x00000011
# VT_I4
PIDSI_APPNAME = 0x00000012
PIDSI_DOC_SECURITY = 0x00000013
# Property IDs for the DocSummaryInformation Property Set
# VT_LPSTR
# VT_LPSTR
PIDDSI_CATEGORY = 0x00000002
# VT_I4
PIDDSI_PRESFORMAT = 0x00000003
# VT_I4
PIDDSI_BYTECOUNT = 0x00000004
# VT_I4
PIDDSI_LINECOUNT = 0x00000005
# VT_I4
PIDDSI_PARCOUNT = 0x00000006
# VT_I4
PIDDSI_SLIDECOUNT = 0x00000007
# VT_I4
PIDDSI_NOTECOUNT = 0x00000008
# VT_I4
PIDDSI_HIDDENCOUNT = 0x00000009
# VT_BOOL
PIDDSI_MMCLIPCOUNT = 0x0000000A
# VT_VARIANT | VT_VECTOR
PIDDSI_SCALE = 0x0000000B
# VT_LPSTR | VT_VECTOR
PIDDSI_HEADINGPAIR = 0x0000000C
# VT_LPSTR
PIDDSI_DOCPARTS = 0x0000000D
# VT_LPSTR
PIDDSI_MANAGER = 0x0000000E
# VT_BOOL
PIDDSI_COMPANY = 0x0000000F
PIDDSI_LINKSDIRTY = 0x00000010
# FMTID_MediaFileSummaryInfo - Property IDs
# VT_LPWSTR
# VT_LPWSTR
PIDMSI_EDITOR = 0x00000002
# VT_LPWSTR
PIDMSI_SUPPLIER = 0x00000003
# VT_LPWSTR
PIDMSI_SOURCE = 0x00000004
# VT_LPWSTR
PIDMSI_SEQUENCE_NO = 0x00000005
# VT_UI4
PIDMSI_PROJECT = 0x00000006
# VT_LPWSTR
PIDMSI_STATUS = 0x00000007
# VT_LPWSTR
PIDMSI_OWNER = 0x00000008
# VT_FILETIME (UTC)
PIDMSI_RATING = 0x00000009
# VT_LPWSTR
PIDMSI_PRODUCTION = 0x0000000A
PIDMSI_COPYRIGHT = 0x0000000B


class tagSERIALIZEDPROPERTYVALUE(ctypes.Structure):
    _fields_ = [
        ('dwType', DWORD),
        ('rgb', BYTE * 1),
    ]


SERIALIZEDPROPERTYVALUE = tagSERIALIZEDPROPERTYVALUE


__all__ = (
    'IEnumSTATPROPSTG', 'IEnumSTATPROPSETSTG', 'IPropertyStorage', 'tagCAUB',
    'IPropertySetStorage', 'PIDSI_TEMPLATE', 'PIDSI_LASTSAVE_DTM', 'tagCAUH',
    'PIDDSI_NOTECOUNT', 'PIDDSI_MANAGER', 'PIDDSI_LINKSDIRTY', 'PID_BEHAVIOR',
    'PIDSI_AUTHOR', 'PIDMSI_PROJECT', 'PIDDSI_PRESFORMAT', 'PRSPEC_LPWSTR',
    'PIDDSI_HIDDENCOUNT', 'PIDMSI_SUPPLIER', 'PIDMSI_RATING', 'PIDDSI_SCALE',
    'PID_SECURITY', 'PIDSI_DOC_SECURITY', 'PIDSI_TITLE', 'PIDMSI_OWNER',
    'PROPSETFLAG_ANSI', 'PID_CODEPAGE', 'PIDMSI_EDITOR', 'PID_DICTIONARY',
    'PIDSI_APPNAME', 'PIDSI_WORDCOUNT', 'PROPSETHDR_OSVER_MAJOR', 'tagCABSTR',
    'PIDSI_PAGECOUNT', 'PIDMSI_SOURCE', 'PIDDSI_MMCLIPCOUNT', 'PIDMSI_STATUS',
    'PIDDSI_SLIDECOUNT', 'PIDSI_COMMENTS', 'PID_ILLEGAL', 'PIDDI_THUMBNAIL',
    'PID_LOCALE', 'PIDDSI_LINECOUNT', 'PIDDSI_HEADINGPAIR', 'PIDSI_SUBJECT',
    '__REQUIRED_RPCNDR_H_VERSION__', 'PIDSI_REVNUMBER', 'PIDMSI_COPYRIGHT',
    'PROPSET_BEHAVIOR_CASE_SENSITIVE', 'PIDMSI_SEQUENCE_NO', 'PRSPEC_INVALID',
    'PRSPEC_PROPID', 'PIDSI_LASTPRINTED', 'PID_FIRST_USABLE', 'tagCASCODE',
    'PID_MIN_READONLY', 'PIDDSI_BYTECOUNT', 'PROPSETFLAG_CASE_SENSITIVE',
    'PROPSETHDR_OSVER_MINOR', 'PIDDSI_COMPANY', 'PIDSI_KEYWORDS', 'tagCAUI',
    'PROPSETFLAG_DEFAULT', 'PIDSI_THUMBNAIL', 'PIDSI_CHARCOUNT', 'tagCACLSID',
    'PROPSETHDR_OSVERSION_UNKNOWN', 'PIDSI_LASTAUTHOR', 'PIDDSI_PARCOUNT',
    'PIDMSI_PRODUCTION', 'PID_MAX_READONLY', 'REFPROPVARIANT', 'tagCALPWSTR',
    'PROPSETFLAG_NONSIMPLE', 'PIDSI_EDITTIME', 'PIDSI_CREATE_DTM', 'tagCAUL',
    'PIDDSI_DOCPARTS', '__REQUIRED_RPCSAL_H_VERSION__', 'PIDDSI_CATEGORY',
    'PROPSETFLAG_UNBUFFERED', 'PROPSETHDR_OSVER_KIND', 'PID_MODIFY_TIME',
    'PID_FIRST_NAME_DEFAULT', 'tagCALPSTR', 'tagCAFLT', 'tagCABSTRBLOB',
    'tagCAFILETIME', 'tagCADBL', 'tagCACLIPDATA', 'tagVersionedStream',
    'tagCAL', 'tagCAH', 'tagCAI', 'tagSTATPROPSETSTG', 'tagCAC', 'tagCABOOL',
    'tagSTATPROPSTG', 'tagSERIALIZEDPROPERTYVALUE', 'tagCAPROPVARIANT',
    'tagPROPSPEC', 'tagCADATE', 'tagCACY', 'LPPROPERTYSTORAGE',
    'LPPROPERTYSETSTORAGE', 'PROPVAR_PAD1', 'PROPVAR_PAD2', 'PROPVAR_PAD3',
    'LPENUMSTATPROPSTG', 'LPENUMSTATPROPSETSTG', 'PROPVARIANT'
)
