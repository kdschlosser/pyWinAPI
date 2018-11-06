__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import * # NOQA
# from .rpcndr_h import * # NOQA
# from .windows_h import * # NOQA
# from .ole2_h import * # NOQA
from .objidl_h import * # NOQA
from .oleidl_h import * # NOQA
from .ocidl_h import * # NOQA
from .shtypes_h import * # NOQA
from .structuredquerycondition_h import * # NOQA
from .winapifamily_h import * # NOQA

from .propidl_h import (
    PROPVARIANT,
    REFPROPVARIANT,
    VARTYPE,
    IID_IPropertyStore,
    IPropertyStore
)
from .shtypes_h import (
    SHCOLSTATEF
)
from .structuredquerycondition_h import (
    CONDITION_OPERATION
)
from .wtypes_h import (
    ENUM,
    REFIID,
    VOID,
    POINTER,
    HRESULT,
    DWORD,
    LPWSTR,
    UINT,
    LPCWSTR,
    BOOL,
    REFCLSID,
    INT,
    PROPERTYKEY,
    BSTR
)
from .guiddef_h import IID
import ctypes
import comtypes


propsys = ctypes.windll.Propsys

PSSTDAPI = HRESULT


REFPROPERTYKEY = POINTER(PROPERTYKEY)

from .propkeydef_h import * # NOQA

COMMETHOD = comtypes.COMMETHOD


IID_IInitializeWithFile = IID(
    '{b7d14566-0509-4cce-a71f-0a554233bd9b}'
)


class IInitializeWithFile(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInitializeWithFile
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Initialize',
            (['in'], LPCWSTR, 'pszFilePath'),
            (['in'], DWORD, 'grfMode'),
        ),
    ]


IID_IInitializeWithStream = IID(
    '{b824b49d-22ac-4161-ac8a-9916e8fa3f7f}'
)


class IInitializeWithStream(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInitializeWithStream
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Initialize',
            (['in'], POINTER(IStream), 'pstream'),
            (['in'], DWORD, 'grfMode'),
        ),
    ]


LPPROPERTYSTORE = POINTER(IPropertyStore)


# PSSTDAPI PropVariantToWinRTPropertyValue(
#   _In_ REFPROPVARIANT propvar,
#   _In_ REFIID riid,
#   _COM_Outptr_result_maybenull_ VOID **ppv
# );
# PropVariantToWinRTPropertyValue = propsys.PropVariantToWinRTPropertyValue
# PropVariantToWinRTPropertyValue.restype = PSSTDAPI


# PSSTDAPI WinRTPropertyValueToPropVariant(
#   _In_opt_ IUnknown *punkPropertyValue,
#   _Out_ PROPVARIANT *ppropvar
# );
# WinRTPropertyValueToPropVariant = propsys.WinRTPropertyValueToPropVariant
# WinRTPropertyValueToPropVariant.restype = PSSTDAPI

IID_INamedPropertyStore = IID(
    '{71604b0f-97b0-4764-8577-2f13e98a1422}'
)


class INamedPropertyStore(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_INamedPropertyStore
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetNamedValue',
            (['in'], LPCWSTR, 'pszName'),
            (['out'], POINTER(PROPVARIANT), 'ppropvar'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetNamedValue',
            (['in'], LPCWSTR, 'pszName'),
            (['in'], REFPROPVARIANT, 'propvar'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetNameCount',
            (['out'], POINTER(DWORD), 'pdwCount'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetNameAt',
            (['in'], DWORD, 'iProp'),
            (['out'], POINTER(BSTR), 'pbstrName'),
        ),
    ]


class GETPROPERTYSTOREFLAGS(ENUM):
    GPS_DEFAULT = 0
    GPS_HANDLERPROPERTIESONLY = 0x1
    GPS_READWRITE = 0x2
    GPS_TEMPORARY = 0x4
    GPS_FASTPROPERTIESONLY = 0x8
    GPS_OPENSLOWITEM = 0x10
    GPS_DELAYCREATION = 0x20
    GPS_BESTEFFORT = 0x40
    GPS_NO_OPLOCK = 0x80
    GPS_PREFERQUERYPROPERTIES = 0x100
    GPS_EXTRINSICPROPERTIES = 0x200
    GPS_EXTRINSICPROPERTIESONLY = 0x400
    GPS_VOLATILEPROPERTIES = 0x800
    GPS_VOLATILEPROPERTIESONLY = 0x1000
    GPS_MASK_VALID = 0x1FFF


IID_IObjectWithPropertyKey = IID(
    '{fc0ca0a7-c316-4fd2-9031-3e628e6d4f23}'
)


class IObjectWithPropertyKey(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IObjectWithPropertyKey
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetPropertyKey',
            (['in'], REFPROPERTYKEY, 'key'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetPropertyKey',
            (['out'], POINTER(PROPERTYKEY), 'pkey'),
        ),
    ]


class PKA_FLAGS(ENUM):
    PKA_SET = 0
    PKA_APPEND = PKA_SET + 1
    PKA_DELETE = PKA_APPEND + 1


IID_IPropertyChange = IID(
    '{f917bc8a-1bba-4478-a245-1bde03eb9431}'
)


class IPropertyChange(IObjectWithPropertyKey):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyChange
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'ApplyToPropVariant',
            (['in'], REFPROPVARIANT, 'propvarIn'),
            (['out'], POINTER(PROPVARIANT), 'ppropvarOut'),
        ),
    ]


IID_IPropertyChangeArray = IID(
    '{380f5cad-1b5e-42f2-805d-637fd392d31e}'
)


class IPropertyChangeArray(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyChangeArray
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetCount',
            (['out'], POINTER(UINT), 'pcOperations'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetAt',
            (['in'], UINT, 'iIndex'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'InsertAt',
            (['in'], UINT, 'iIndex'),
            (['in'], POINTER(IPropertyChange), 'ppropChange'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Append',
            (['in'], POINTER(IPropertyChange), 'ppropChange'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'AppendOrReplace',
            (['in'], POINTER(IPropertyChange), 'ppropChange'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'RemoveAt',
            (['in'], UINT, 'iIndex'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'IsKeyInArray',
            (['in'], REFPROPERTYKEY, 'key'),
        ),
    ]


IID_IPropertyStoreCapabilities = IID(
    '{c8e2d566-186e-4d49-bf41-6909ead56acc}'
)


class IPropertyStoreCapabilities(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyStoreCapabilities
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'IsPropertyWritable',
            (['in'], REFPROPERTYKEY, 'key'),
        ),
    ]


class PSC_STATE(ENUM):
    PSC_NORMAL = 0
    PSC_NOTINSOURCE = 1
    PSC_DIRTY = 2
    PSC_READONLY = 3


IID_IPropertyStoreCache = IID(
    '{3017056d-9a91-4e90-937d-746c72abbf4f}'
)


class IPropertyStoreCache(IPropertyStore):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyStoreCache
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetState',
            (['in'], REFPROPERTYKEY, 'key'),
            (['out'], POINTER(PSC_STATE), 'pstate'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetValueAndState',
            (['in'], REFPROPERTYKEY, 'key'),
            (['out'], POINTER(PROPVARIANT), 'ppropvar'),
            (['out'], POINTER(PSC_STATE), 'pstate'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetState',
            (['in'], REFPROPERTYKEY, 'key'),
            (['in'], PSC_STATE, 'state'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetValueAndState',
            (['in'], REFPROPERTYKEY, 'key'),
            (['in'], POINTER(PROPVARIANT), 'ppropvar'),
            (['in'], PSC_STATE, 'state'),
        ),
    ]


class PROPENUMTYPE(ENUM):
    PET_DISCRETEVALUE = 0
    PET_RANGEDVALUE = 1
    PET_DEFAULTVALUE = 2
    PET_ENDRANGE = 3


IID_IPropertyEnumType = IID(
    '{11e1fbf9-2d56-4a6b-8db3-7cd193a471f2}'
)


class IPropertyEnumType(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyEnumType
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetEnumType',
            (['out'], POINTER(PROPENUMTYPE), 'penumtype'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetValue',
            (['out'], POINTER(PROPVARIANT), 'ppropvar'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetRangeMinValue',
            (['out'], POINTER(PROPVARIANT), 'ppropvarMin'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetRangeSetValue',
            (['out'], POINTER(PROPVARIANT), 'ppropvarSet'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetDisplayText',
            (['out'], POINTER(LPWSTR), 'ppszDisplay'),
        ),
    ]


IID_IPropertyEnumType2 = IID(
    '{9b6e051c-5ddd-4321-9070-fe2acb55e794}'
)


class IPropertyEnumType2(IPropertyEnumType):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyEnumType2
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetImageReference',
            (['out'], POINTER(LPWSTR), 'ppszImageRes'),
        ),
    ]


IID_IPropertyEnumTypeList = IID(
    '{a99400f4-3d84-4557-94ba-1242fb2cc9a6}'
)


class IPropertyEnumTypeList(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyEnumTypeList
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetCount',
            (['out'], POINTER(UINT), 'pctypes'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetAt',
            (['in'], UINT, 'itype'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetConditionAt',
            (['in'], UINT, 'nIndex'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'FindMatchingIndex',
            (['in'], REFPROPVARIANT, 'propvarCmp'),
            (['out'], POINTER(UINT), 'pnIndex'),
        ),
    ]


class PROPDESC_TYPE_FLAGS(ENUM):
    PDTF_DEFAULT = 0
    PDTF_MULTIPLEVALUES = 0x1
    PDTF_ISINNATE = 0x2
    PDTF_ISGROUP = 0x4
    PDTF_CANGROUPBY = 0x8
    PDTF_CANSTACKBY = 0x10
    PDTF_ISTREEPROPERTY = 0x20
    PDTF_INCLUDEINFULLTEXTQUERY = 0x40
    PDTF_ISVIEWABLE = 0x80
    PDTF_ISQUERYABLE = 0x100
    PDTF_CANBEPURGED = 0x200
    PDTF_SEARCHRAWVALUE = 0x400
    PDTF_DONTCOERCEEMPTYSTRINGS = 0x800
    PDTF_ALWAYSINSUPPLEMENTALSTORE = 0x1000
    PDTF_ISSYSTEMPROPERTY = 0x80000000
    PDTF_MASK_ALL = 0x80001FFF


class PROPDESC_VIEW_FLAGS(ENUM):
    PDVF_DEFAULT = 0
    PDVF_CENTERALIGN = 0x1
    PDVF_RIGHTALIGN = 0x2
    PDVF_BEGINNEWGROUP = 0x4
    PDVF_FILLAREA = 0x8
    PDVF_SORTDESCENDING = 0x10
    PDVF_SHOWONLYIFPRESENT = 0x20
    PDVF_SHOWBYDEFAULT = 0x40
    PDVF_SHOWINPRIMARYLIST = 0x80
    PDVF_SHOWINSECONDARYLIST = 0x100
    PDVF_HIDELABEL = 0x200
    PDVF_HIDDEN = 0x800
    PDVF_CANWRAP = 0x1000
    PDVF_MASK_ALL = 0x1BFF


class PROPDESC_DISPLAYTYPE(ENUM):
    PDDT_STRING = 0
    PDDT_NUMBER = 1
    PDDT_BOOLEAN = 2
    PDDT_DATETIME = 3
    PDDT_ENUMERATED = 4


class PROPDESC_GROUPING_RANGE(ENUM):
    PDGR_DISCRETE = 0
    PDGR_ALPHANUMERIC = 1
    PDGR_SIZE = 2
    PDGR_DYNAMIC = 3
    PDGR_DATE = 4
    PDGR_PERCENT = 5
    PDGR_ENUMERATED = 6


class PROPDESC_FORMAT_FLAGS(ENUM):
    PDFF_DEFAULT = 0
    PDFF_PREFIXNAME = 0x1
    PDFF_FILENAME = 0x2
    PDFF_ALWAYSKB = 0x4
    PDFF_RESERVED_RIGHTTOLEFT = 0x8
    PDFF_SHORTTIME = 0x10
    PDFF_LONGTIME = 0x20
    PDFF_HIDETIME = 0x40
    PDFF_SHORTDATE = 0x80
    PDFF_LONGDATE = 0x100
    PDFF_HIDEDATE = 0x200
    PDFF_RELATIVEDATE = 0x400
    PDFF_USEEDITINVITATION = 0x800
    PDFF_READONLY = 0x1000
    PDFF_NOAUTOREADINGORDER = 0x2000


class PROPDESC_SORTDESCRIPTION(ENUM):
    PDSD_GENERAL = 0
    PDSD_A_Z = 1
    PDSD_LOWEST_HIGHEST = 2
    PDSD_SMALLEST_BIGGEST = 3
    PDSD_OLDEST_NEWEST = 4


class PROPDESC_RELATIVEDESCRIPTION_TYPE(ENUM):
    PDRDT_GENERAL = 0
    PDRDT_DATE = 1
    PDRDT_SIZE = 2
    PDRDT_COUNT = 3
    PDRDT_REVISION = 4
    PDRDT_LENGTH = 5
    PDRDT_DURATION = 6
    PDRDT_SPEED = 7
    PDRDT_RATE = 8
    PDRDT_RATING = 9
    PDRDT_PRIORITY = 10


class PROPDESC_AGGREGATION_TYPE(ENUM):
    PDAT_DEFAULT = 0
    PDAT_FIRST = 1
    PDAT_SUM = 2
    PDAT_AVERAGE = 3
    PDAT_DATERANGE = 4
    PDAT_UNION = 5
    PDAT_MAX = 6
    PDAT_MIN = 7


class PROPDESC_CONDITION_TYPE(ENUM):
    PDCOT_NONE = 0
    PDCOT_STRING = 1
    PDCOT_SIZE = 2
    PDCOT_DATETIME = 3
    PDCOT_BOOLEAN = 4
    PDCOT_NUMBER = 5


IID_IPropertyDescription = IID(
    '{6f79d558-3e96-4549-a1d1-7d75d2288814}'
)


class IPropertyDescription(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyDescription
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetPropertyKey',
            (['out'], POINTER(PROPERTYKEY), 'pkey'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetCanonicalName',
            (['out'], POINTER(LPWSTR), 'ppszName'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetPropertyType',
            (['out'], POINTER(VARTYPE), 'pvartype'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetDisplayName',
            (['out'], POINTER(LPWSTR), 'ppszName'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetEditInvitation',
            (['out'], POINTER(LPWSTR), 'ppszInvite'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetTypeFlags',
            (['in'], PROPDESC_TYPE_FLAGS, 'mask'),
            (['out'], POINTER(PROPDESC_TYPE_FLAGS), 'ppdtFlags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetViewFlags',
            (['out'], POINTER(PROPDESC_VIEW_FLAGS), 'ppdvFlags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetDefaultColumnWidth',
            (['out'], POINTER(UINT), 'pcxChars'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetDisplayType',
            (['out'], POINTER(PROPDESC_DISPLAYTYPE), 'pdisplaytype'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetColumnState',
            (['out'], POINTER(SHCOLSTATEF), 'pcsFlags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetGroupingRange',
            (['out'], POINTER(PROPDESC_GROUPING_RANGE), 'pgr'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetRelativeDescriptionType',
            (['out'], POINTER(PROPDESC_RELATIVEDESCRIPTION_TYPE), 'prdt'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetRelativeDescription',
            (['in'], REFPROPVARIANT, 'propvar1'),
            (['in'], REFPROPVARIANT, 'propvar2'),
            (['out'], POINTER(LPWSTR), 'ppszDesc1'),
            (['out'], POINTER(LPWSTR), 'ppszDesc2'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetSortDescription',
            (['out'], POINTER(PROPDESC_SORTDESCRIPTION), 'psd'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetSortDescriptionLabel',
            (['in'], BOOL, 'fDescending'),
            (['out'], POINTER(LPWSTR), 'ppszDescription'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetAggregationType',
            (['out'], POINTER(PROPDESC_AGGREGATION_TYPE), 'paggtype'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetConditionType',
            (['out'], POINTER(PROPDESC_CONDITION_TYPE), 'pcontype'),
            (['out'], POINTER(CONDITION_OPERATION), 'popDefault'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetEnumTypeList',
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CoerceToCanonicalValue',
            (['in', 'out'], POINTER(PROPVARIANT), 'ppropvar'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'FormatForDisplay',
            (['in'], REFPROPVARIANT, 'propvar'),
            (['in'], PROPDESC_FORMAT_FLAGS, 'pdfFlags'),
            (['out'], POINTER(LPWSTR), 'ppszDisplay'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'IsValueCanonical',
            (['in'], REFPROPVARIANT, 'propvar'),
        ),
    ]


IID_IPropertyDescription2 = IID(
    '{57d2eded-5062-400e-b107-5dae79fe57a6}'
)


class IPropertyDescription2(IPropertyDescription):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyDescription2
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetImageReferenceForValue',
            (['in'], REFPROPVARIANT, 'propvar'),
            (['out'], POINTER(LPWSTR), 'ppszImageRes'),
        ),
    ]


IID_IPropertyDescriptionAliasInfo = IID(
    '{f67104fc-2af9-46fd-b32d-243c1404f3d1}'
)


class IPropertyDescriptionAliasInfo(IPropertyDescription):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyDescriptionAliasInfo
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetSortByAlias',
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetAdditionalSortByAliases',
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
    ]


class PROPDESC_SEARCHINFO_FLAGS(ENUM):
    PDSIF_DEFAULT = 0
    PDSIF_ININVERTEDINDEX = 0x1
    PDSIF_ISCOLUMN = 0x2
    PDSIF_ISCOLUMNSPARSE = 0x4
    PDSIF_ALWAYSINCLUDE = 0x8
    PDSIF_USEFORTYPEAHEAD = 0x10


class PROPDESC_COLUMNINDEX_TYPE(ENUM):
    PDCIT_NONE = 0
    PDCIT_ONDISK = 1
    PDCIT_INMEMORY = 2
    PDCIT_ONDEMAND = 3
    PDCIT_ONDISKALL = 4
    PDCIT_ONDISKVECTOR = 5


IID_IPropertyDescriptionSearchInfo = IID(
    '{078f91bd-29a2-440f-924e-46a291524520}'
)


class IPropertyDescriptionSearchInfo(IPropertyDescription):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyDescriptionSearchInfo
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetSearchInfoFlags',
            (['out'], POINTER(PROPDESC_SEARCHINFO_FLAGS), 'ppdsiFlags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetColumnIndexType',
            (['out'], POINTER(PROPDESC_COLUMNINDEX_TYPE), 'ppdciType'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetProjectionString',
            (['out'], POINTER(LPWSTR), 'ppszProjection'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMaxSize',
            (['out'], POINTER(UINT), 'pcbMaxSize'),
        ),
    ]


IID_IPropertyDescriptionRelatedPropertyInfo = IID(
    '{507393f4-2a3d-4a60-b59e-d9c75716c2dd}'
)


class IPropertyDescriptionRelatedPropertyInfo(IPropertyDescription):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyDescriptionRelatedPropertyInfo
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetRelatedProperty',
            (['in'], LPCWSTR, 'pszRelationshipName'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
    ]


class PROPDESC_ENUMFILTER(ENUM):
    PDEF_ALL = 0
    PDEF_SYSTEM = 1
    PDEF_NONSYSTEM = 2
    PDEF_VIEWABLE = 3
    PDEF_QUERYABLE = 4
    PDEF_INFULLTEXTQUERY = 5
    PDEF_COLUMN = 6


IID_IPropertySystem = IID(
    '{ca724e8a-c3e6-442b-88a4-6fb0db8035a3}'
)


class IPropertySystem(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertySystem
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetPropertyDescription',
            (['in'], REFPROPERTYKEY, 'propkey'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetPropertyDescriptionByName',
            (['in'], LPCWSTR, 'pszCanonicalName'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetPropertyDescriptionListFromString',
            (['in'], LPCWSTR, 'pszPropList'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'EnumeratePropertyDescriptions',
            (['in'], PROPDESC_ENUMFILTER, 'filterOn'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'FormatForDisplay',
            (['in'], REFPROPERTYKEY, 'key'),
            (['in'], REFPROPVARIANT, 'propvar'),
            (['in'], PROPDESC_FORMAT_FLAGS, 'pdff'),
            (['out'], LPWSTR, 'pszText'),
            ([], DWORD, 'cchText'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'FormatForDisplayAlloc',
            (['in'], REFPROPERTYKEY, 'key'),
            (['in'], REFPROPVARIANT, 'propvar'),
            (['in'], PROPDESC_FORMAT_FLAGS, 'pdff'),
            (['out'], POINTER(LPWSTR), 'ppszDisplay'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'RegisterPropertySchema',
            (['in'], LPCWSTR, 'pszPath'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'UnregisterPropertySchema',
            (['in'], LPCWSTR, 'pszPath'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'RefreshPropertySchema'
        ),
    ]


IID_IPropertyDescriptionList = IID(
    '{1f9fc1d0-c39b-4b26-817f-011967d3440e}'
)


class IPropertyDescriptionList(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyDescriptionList
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetCount',
            (['out'], POINTER(UINT), 'pcElem'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetAt',
            (['in'], UINT, 'iElem'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
    ]


IID_IPropertyStoreFactory = IID(
    '{bc110b6d-57e8-4148-a9c6-91015ab2f3a5}'
)


class IPropertyStoreFactory(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyStoreFactory
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetPropertyStore',
            (['in'], GETPROPERTYSTOREFLAGS, 'flags'),
            (['in'], POINTER(comtypes.IUnknown), 'pUnkFactory'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetPropertyStoreForKeys',
            (['in'], POINTER(PROPERTYKEY), 'rgKeys'),
            (['in'], UINT, 'cKeys'),
            (['in'], GETPROPERTYSTOREFLAGS, 'flags'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
    ]


IID_IDelayedPropertyStoreFactory = IID(
    '{40d4577f-e237-4bdb-bd69-58f089431b6a}'
)


class IDelayedPropertyStoreFactory(IPropertyStoreFactory):
    _case_insensitive_ = True
    _iid_ = IID_IDelayedPropertyStoreFactory
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetDelayedPropertyStore',
            (['in'], GETPROPERTYSTOREFLAGS, 'flags'),
            (['in'], DWORD, 'dwStoreId'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
    ]


PERSIST_SPROPSTORE_FLAGS = INT
tagSERIALIZEDPROPSTORAGE = VOID
SERIALIZEDPROPSTORAGE = tagSERIALIZEDPROPSTORAGE
PUSERIALIZEDPROPSTORAGE = POINTER(SERIALIZEDPROPSTORAGE)
PCUSERIALIZEDPROPSTORAGE = POINTER(SERIALIZEDPROPSTORAGE)

IID_IPersistSerializedPropStorage = IID(
    '{e318ad57-0aa0-450f-aca5-6fab7103d917}'
)


class IPersistSerializedPropStorage(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPersistSerializedPropStorage
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetFlags',
            (['in'], PERSIST_SPROPSTORE_FLAGS, 'flags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetPropertyStorage',
            (['in'], PCUSERIALIZEDPROPSTORAGE, 'psps'),
            (['in'], DWORD, 'cb'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetPropertyStorage',
            (['out'], POINTER(POINTER(SERIALIZEDPROPSTORAGE)), 'ppsps'),
            (['out'], POINTER(DWORD), 'pcb'),
        ),
    ]


IID_IPersistSerializedPropStorage2 = IID(
    '{77effa68-4f98-4366-ba72-573b3d880571}'
)


class IPersistSerializedPropStorage2(IPersistSerializedPropStorage):
    _case_insensitive_ = True
    _iid_ = IID_IPersistSerializedPropStorage2
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetPropertyStorageSize',
            (['out'], POINTER(DWORD), 'pcb'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetPropertyStorageBuffer',
            ([], POINTER(SERIALIZEDPROPSTORAGE), 'psps'),
            (['in'], DWORD, 'cb'),
            (['out'], POINTER(DWORD), 'pcbWritten'),
        ),
    ]


IID_IPropertySystemChangeNotify = IID(
    '{fa955fd9-38be-4879-a6ce-824cf52d609f}'
)


class IPropertySystemChangeNotify(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertySystemChangeNotify
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SchemaRefreshed'
        ),
    ]


IID_ICreateObject = IID(
    '{75121952-e0d0-43e5-9380-1d80483acf72}'
)


class ICreateObject(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICreateObject
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'CreateObject',
            (['in'], REFCLSID, 'clsid'),
            (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
            (['in'], REFIID, 'riid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv'),
        ),
    ]


# PSSTDAPI PSFormatForDisplay(
#     _In_ REFPROPERTYKEY propkey,
#     _In_ REFPROPVARIANT propvar,
#     _In_ PROPDESC_FORMAT_FLAGS pdfFlags,
#     _Out_writes_(cchText) LPWSTR pwszText,
#     _In_ DWORD cchText);
PSFormatForDisplay = propsys.PSFormatForDisplay
PSFormatForDisplay.restype = PSSTDAPI


# PSSTDAPI PSFormatForDisplayAlloc(
#     _In_ REFPROPERTYKEY key,
#     _In_ REFPROPVARIANT propvar,
#     _In_ PROPDESC_FORMAT_FLAGS pdff,
#     _Outptr_ PWSTR *ppszDisplay);
PSFormatForDisplayAlloc = propsys.PSFormatForDisplayAlloc
PSFormatForDisplayAlloc.restype = PSSTDAPI


# PSSTDAPI PSFormatPropertyValue(
#     _In_ IPropertyStore *pps,
#     _In_ IPropertyDescription *ppd,
#     _In_ PROPDESC_FORMAT_FLAGS pdff,
#     _Outptr_ LPWSTR *ppszDisplay);
PSFormatPropertyValue = propsys.PSFormatPropertyValue
PSFormatPropertyValue.restype = PSSTDAPI

# Retrieve the image reference associated with a property value (if specified)

# PSSTDAPI PSGetImageReferenceForValue(
#     _In_ REFPROPERTYKEY propkey,
#     _In_ REFPROPVARIANT propvar,
#     _Outptr_ PWSTR *ppszImageRes);
PSGetImageReferenceForValue = propsys.PSGetImageReferenceForValue
PSGetImageReferenceForValue.restype = PSSTDAPI

# will take care of any LONG INTeger value
# "{12345678-1234-1234-1234-123456789012}"
PKEY_PIDSTR_MAX = 0xA
GUIDSTRING_MAX = 1 + 8 + 1 + 4 + 1 + 4 + 1 + 4 + 1 + 12 + 1 + 1
PKEYSTR_MAX = GUIDSTRING_MAX + 1 + PKEY_PIDSTR_MAX
# Convert a PROPERTYKEY to and from a PWSTR

# PSSTDAPI PSStringFromPropertyKey(
#     _In_ REFPROPERTYKEY pkey,
#     _Out_writes_(cch) LPWSTR psz,
#     _In_ UINT cch);
PSStringFromPropertyKey = propsys.PSStringFromPropertyKey
PSStringFromPropertyKey.restype = PSSTDAPI


# PSSTDAPI PSPropertyKeyFromString(
#     _In_ LPCWSTR pszString,
#     _Out_ PROPERTYKEY *pkey);
PSPropertyKeyFromString = propsys.PSPropertyKeyFromString
PSPropertyKeyFromString.restype = PSSTDAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# Creates an in-memory property store
# Returns an IPropertyStore, IPersistSerializedPropStorage, and related
# INTerfaces INTerface

# PSSTDAPI PSCreateMemoryPropertyStore(
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSCreateMemoryPropertyStore = propsys.PSCreateMemoryPropertyStore
PSCreateMemoryPropertyStore.restype = PSSTDAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
# Create a read-only, delay-bind multiplexing property store
# Returns an IPropertyStore INTerface or related INTerfaces

# PSSTDAPI PSCreateDelayedMultiplexPropertyStore(
#     _In_ GETPROPERTYSTOREFLAGS flags,
#     _In_ IDelayedPropertyStoreFactory *pdpsf,
#     _In_reads_(cStores) DWORD *rgStoreIds,
#     _In_ DWORD cStores,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSCreateDelayedMultiplexPropertyStore = (
    propsys.PSCreateDelayedMultiplexPropertyStore
)
PSCreateDelayedMultiplexPropertyStore.restype = PSSTDAPI

# Create a read-only property store from one or more sources (which each must
# support either IPropertyStore or IPropertySetStorage)
# Returns an IPropertyStore INTerface or related INTerfaces

# PSSTDAPI PSCreateMultiplexPropertyStore(
#     _In_reads_(cStores) IUnknown **prgpunkStores,
#     _In_ DWORD cStores,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSCreateMultiplexPropertyStore = propsys.PSCreateMultiplexPropertyStore
PSCreateMultiplexPropertyStore.restype = PSSTDAPI

# Create a container for IPropertyChanges
# Returns an IPropertyChangeArray INTerface

# PSSTDAPI PSCreatePropertyChangeArray(
#     _In_reads_opt_(cChanges) PROPERTYKEY *rgpropkey,
#     _In_reads_opt_(cChanges) PKA_FLAGS *rgflags,
#     _In_reads_opt_(cChanges) PROPVARIANT *rgpropvar,
#     _In_ UINT cChanges,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSCreatePropertyChangeArray = propsys.PSCreatePropertyChangeArray
PSCreatePropertyChangeArray.restype = PSSTDAPI

# Create a simple property change
# Returns an IPropertyChange INTerface

# PSSTDAPI PSCreateSimplePropertyChange(
#     _In_ PKA_FLAGS flags,
#     _In_ REFPROPERTYKEY key,
#     _In_ REFPROPVARIANT propvar,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSCreateSimplePropertyChange = propsys.PSCreateSimplePropertyChange
PSCreateSimplePropertyChange.restype = PSSTDAPI

# Get a property description
# Returns an IPropertyDescription INTerface

# PSSTDAPI PSGetPropertyDescription(
#     _In_ REFPROPERTYKEY propkey,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSGetPropertyDescription = propsys.PSGetPropertyDescription
PSGetPropertyDescription.restype = PSSTDAPI


# PSSTDAPI PSGetPropertyDescriptionByName(
#     _In_ LPCWSTR pszCanonicalName,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSGetPropertyDescriptionByName = propsys.PSGetPropertyDescriptionByName
PSGetPropertyDescriptionByName.restype = PSSTDAPI

# Lookup a per-machine registered file property handler

# PSSTDAPI PSLookupPropertyHandlerCLSID(
#     _In_ PCWSTR pszFilePath,
#     _Out_ CLSID *pclsid);
PSLookupPropertyHandlerCLSID = propsys.PSLookupPropertyHandlerCLSID
PSLookupPropertyHandlerCLSID.restype = PSSTDAPI

# Get a property handler, on Vista or downlevel to XP
# punkItem is a shell item created with an SHCreateItemXXX API
# Returns an IPropertyStore

# PSSTDAPI PSGetItemPropertyHandler(
#     _In_ IUnknown *punkItem,
#     _In_ BOOL fReadWrite,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSGetItemPropertyHandler = propsys.PSGetItemPropertyHandler
PSGetItemPropertyHandler.restype = PSSTDAPI

# Get a property handler, on Vista or downlevel to XP
# punkItem is a shell item created with an SHCreateItemXXX API
# punkCreateObject supports ICreateObject
# Returns an IPropertyStore

# PSSTDAPI PSGetItemPropertyHandlerWithCreateObject(
#     _In_ IUnknown *punkItem,
#     _In_ BOOL fReadWrite,
#     _In_ IUnknown *punkCreateObject,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSGetItemPropertyHandlerWithCreateObject = (
    propsys.PSGetItemPropertyHandlerWithCreateObject
)
PSGetItemPropertyHandlerWithCreateObject.restype = PSSTDAPI

# Get or set a property value from a store

# PSSTDAPI PSGetPropertyValue(
#     _In_ IPropertyStore *pps,
#     _In_ IPropertyDescription *ppd,
#     _Out_ PROPVARIANT *ppropvar);
PSGetPropertyValue = propsys.PSGetPropertyValue
PSGetPropertyValue.restype = PSSTDAPI


# PSSTDAPI PSSetPropertyValue(
#     _In_ IPropertyStore *pps,
#     _In_ IPropertyDescription *ppd,
#     _In_ REFPROPVARIANT propvar);
PSSetPropertyValue = propsys.PSSetPropertyValue
PSSetPropertyValue.restype = PSSTDAPI

# Interact with the set of property descriptions

# PSSTDAPI PSRegisterPropertySchema(
#     _In_ PCWSTR pszPath);
PSRegisterPropertySchema = propsys.PSRegisterPropertySchema
PSRegisterPropertySchema.restype = PSSTDAPI


# PSSTDAPI PSUnregisterPropertySchema(
#     _In_ PCWSTR pszPath);
PSUnregisterPropertySchema = propsys.PSUnregisterPropertySchema
PSUnregisterPropertySchema.restype = PSSTDAPI


# PSSTDAPI PSRefreshPropertySchema(VOID);
PSRefreshPropertySchema = propsys.PSRefreshPropertySchema
PSRefreshPropertySchema.restype = PSSTDAPI

# Returns either: IPropertyDescriptionList or IEnumUnknown INTerfaces

# PSSTDAPI PSEnumeratePropertyDescriptions(
#     _In_ PROPDESC_ENUMFILTER filterOn,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSEnumeratePropertyDescriptions = propsys.PSEnumeratePropertyDescriptions
PSEnumeratePropertyDescriptions.restype = PSSTDAPI

# Convert between a PROPERTYKEY and its canonical name

# PSSTDAPI PSGetPropertyKeyFromName(
#     _In_ PCWSTR pszName,
#     _Out_ PROPERTYKEY *ppropkey);
PSGetPropertyKeyFromName = propsys.PSGetPropertyKeyFromName
PSGetPropertyKeyFromName.restype = PSSTDAPI


# PSSTDAPI PSGetNameFromPropertyKey(
#     _In_ REFPROPERTYKEY propkey,
#     _Outptr_ PWSTR *ppszCanonicalName);
PSGetNameFromPropertyKey = propsys.PSGetNameFromPropertyKey
PSGetNameFromPropertyKey.restype = PSSTDAPI

# Coerce and canonicalize a property value

# PSSTDAPI PSCoerceToCanonicalValue(
#     _In_ REFPROPERTYKEY key,
#     _Inout_ PROPVARIANT *ppropvar);
PSCoerceToCanonicalValue = propsys.PSCoerceToCanonicalValue
PSCoerceToCanonicalValue.restype = PSSTDAPI

# Convert a 'prop:' string INTo a list of property descriptions
# Returns an IPropertyDescriptionList INTerface

# PSSTDAPI PSGetPropertyDescriptionListFromString(
#     _In_ LPCWSTR pszPropList,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSGetPropertyDescriptionListFromString = (
    propsys.PSGetPropertyDescriptionListFromString
)
PSGetPropertyDescriptionListFromString.restype = PSSTDAPI

# Wrap an IPropertySetStorage INTerface in an IPropertyStore INTerface
# Returns an IPropertyStore or related INTerface

# PSSTDAPI PSCreatePropertyStoreFromPropertySetStorage(
#     _In_ IPropertySetStorage *ppss,
#     _In_ DWORD grfMode,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSCreatePropertyStoreFromPropertySetStorage = (
    propsys.PSCreatePropertyStoreFromPropertySetStorage
)
PSCreatePropertyStoreFromPropertySetStorage.restype = PSSTDAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# punkSource must support IPropertyStore or IPropertySetStorage
# On success, the returned ppv is guaranteed to support IPropertyStore.
# If punkSource already supports IPropertyStore, no wrapper is created.

# PSSTDAPI PSCreatePropertyStoreFromObject(
#     _In_ IUnknown *punk,
#     _In_ DWORD grfMode,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSCreatePropertyStoreFromObject = propsys.PSCreatePropertyStoreFromObject
PSCreatePropertyStoreFromObject.restype = PSSTDAPI

# punkSource must support IPropertyStore
# riid may be IPropertyStore, IPropertySetStorage, IPropertyStoreCapabilities,
# or IObjectProvider

# PSSTDAPI PSCreateAdapterFromPropertyStore(
#     _In_ IPropertyStore *pps,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSCreateAdapterFromPropertyStore = propsys.PSCreateAdapterFromPropertyStore
PSCreateAdapterFromPropertyStore.restype = PSSTDAPI

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
# Talk to the property system using an INTerface
# Returns an IPropertySystem INTerface

# PSSTDAPI PSGetPropertySystem(
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSGetPropertySystem = propsys.PSGetPropertySystem
PSGetPropertySystem.restype = PSSTDAPI

# Obtain a value from serialized property storage

# PSSTDAPI PSGetPropertyFromPropertyStorage(
#     _In_reads_bytes_(cb) PCUSERIALIZEDPROPSTORAGE psps,
#     _In_ DWORD cb,
#     _In_ REFPROPERTYKEY rpkey,
#     _Out_ PROPVARIANT *ppropvar);
PSGetPropertyFromPropertyStorage = propsys.PSGetPropertyFromPropertyStorage
PSGetPropertyFromPropertyStorage.restype = PSSTDAPI

# Obtain a named value from serialized property storage

# PSSTDAPI PSGetNamedPropertyFromPropertyStorage(
#     _In_reads_bytes_(cb) PCUSERIALIZEDPROPSTORAGE psps,
#     _In_ DWORD cb,
#     _In_ LPCWSTR pszName,
#     _Out_ PROPVARIANT *ppropvar);
PSGetNamedPropertyFromPropertyStorage = (
    propsys.PSGetNamedPropertyFromPropertyStorage
)
PSGetNamedPropertyFromPropertyStorage.restype = PSSTDAPI

# Helper functions for reading and writing values from IPropertyBag's.

# PSSTDAPI PSPropertyBag_ReadType(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ VARIANT *var,
#     VARTYPE type);
PSPropertyBag_ReadType = propsys.PSPropertyBag_ReadType
PSPropertyBag_ReadType.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadStr(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_writes_(CHARacterCount) LPWSTR value,
#     INT CHARacterCount);
PSPropertyBag_ReadStr = propsys.PSPropertyBag_ReadStr
PSPropertyBag_ReadStr.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadStrAlloc(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Outptr_ PWSTR *value);
PSPropertyBag_ReadStrAlloc = propsys.PSPropertyBag_ReadStrAlloc
PSPropertyBag_ReadStrAlloc.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadBSTR(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Outptr_ BSTR *value);
PSPropertyBag_ReadBSTR = propsys.PSPropertyBag_ReadBSTR
PSPropertyBag_ReadBSTR.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteStr(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _In_ LPCWSTR value);
PSPropertyBag_WriteStr = propsys.PSPropertyBag_WriteStr
PSPropertyBag_WriteStr.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteBSTR(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _In_ BSTR value);
PSPropertyBag_WriteBSTR = propsys.PSPropertyBag_WriteBSTR
PSPropertyBag_WriteBSTR.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadInt(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ INT *value);
PSPropertyBag_ReadInt = propsys.PSPropertyBag_ReadInt
PSPropertyBag_ReadInt.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteInt(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     INT value);
PSPropertyBag_WriteInt = propsys.PSPropertyBag_WriteInt
PSPropertyBag_WriteInt.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadSHORT(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ SHORT *value);
PSPropertyBag_ReadSHORT = propsys.PSPropertyBag_ReadSHORT
PSPropertyBag_ReadSHORT.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteSHORT(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     SHORT value);
PSPropertyBag_WriteSHORT = propsys.PSPropertyBag_WriteSHORT
PSPropertyBag_WriteSHORT.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadLONG(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ LONG *value);
PSPropertyBag_ReadLONG = propsys.PSPropertyBag_ReadLONG
PSPropertyBag_ReadLONG.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteLONG(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     LONG value);
PSPropertyBag_WriteLONG = propsys.PSPropertyBag_WriteLONG
PSPropertyBag_WriteLONG.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadDWORD(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ DWORD *value);
PSPropertyBag_ReadDWORD = propsys.PSPropertyBag_ReadDWORD
PSPropertyBag_ReadDWORD.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteDWORD(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     DWORD value);
PSPropertyBag_WriteDWORD = propsys.PSPropertyBag_WriteDWORD
PSPropertyBag_WriteDWORD.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadBOOL(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ BOOL *value);
PSPropertyBag_ReadBOOL = propsys.PSPropertyBag_ReadBOOL
PSPropertyBag_ReadBOOL.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteBOOL(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     BOOL value);
PSPropertyBag_WriteBOOL = propsys.PSPropertyBag_WriteBOOL
PSPropertyBag_WriteBOOL.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadPOINTL(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ POINTL *value);
PSPropertyBag_ReadPOINTL = propsys.PSPropertyBag_ReadPOINTL
PSPropertyBag_ReadPOINTL.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WritePOINTL(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _In_ POINTL *value);
PSPropertyBag_WritePOINTL = propsys.PSPropertyBag_WritePOINTL
PSPropertyBag_WritePOINTL.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadPOINTS(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ POINTS *value);
PSPropertyBag_ReadPOINTS = propsys.PSPropertyBag_ReadPOINTS
PSPropertyBag_ReadPOINTS.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WritePOINTS(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _In_ POINTS *value);
PSPropertyBag_WritePOINTS = propsys.PSPropertyBag_WritePOINTS
PSPropertyBag_WritePOINTS.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadRECTL(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ RECTL *value);
PSPropertyBag_ReadRECTL = propsys.PSPropertyBag_ReadRECTL
PSPropertyBag_ReadRECTL.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteRECTL(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _In_ RECTL *value);
PSPropertyBag_WriteRECTL = propsys.PSPropertyBag_WriteRECTL
PSPropertyBag_WriteRECTL.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadStream(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Outptr_ IStream **value);
PSPropertyBag_ReadStream = propsys.PSPropertyBag_ReadStream
PSPropertyBag_ReadStream.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteStream(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _In_ IStream *value);
PSPropertyBag_WriteStream = propsys.PSPropertyBag_WriteStream
PSPropertyBag_WriteStream.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_Delete(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName);
PSPropertyBag_Delete = propsys.PSPropertyBag_Delete
PSPropertyBag_Delete.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadULONGLONG(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ ULONGLONG *value);
PSPropertyBag_ReadULONGLONG = propsys.PSPropertyBag_ReadULONGLONG
PSPropertyBag_ReadULONGLONG.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteULONGLONG(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     ULONGLONG value);
PSPropertyBag_WriteULONGLONG = propsys.PSPropertyBag_WriteULONGLONG
PSPropertyBag_WriteULONGLONG.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadUnknown(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _In_ REFIID riid,
#     _Outptr_ VOID **ppv);
PSPropertyBag_ReadUnknown = propsys.PSPropertyBag_ReadUnknown
PSPropertyBag_ReadUnknown.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteUnknown(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _In_ IUnknown *punk);
PSPropertyBag_WriteUnknown = propsys.PSPropertyBag_WriteUnknown
PSPropertyBag_WriteUnknown.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadGUID(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ GUID *value);
PSPropertyBag_ReadGUID = propsys.PSPropertyBag_ReadGUID
PSPropertyBag_ReadGUID.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WriteGUID(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _In_ GUID *value);
PSPropertyBag_WriteGUID = propsys.PSPropertyBag_WriteGUID
PSPropertyBag_WriteGUID.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_ReadPropertyKey(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _Out_ PROPERTYKEY *value);
PSPropertyBag_ReadPropertyKey = propsys.PSPropertyBag_ReadPropertyKey
PSPropertyBag_ReadPropertyKey.restype = PSSTDAPI


# PSSTDAPI PSPropertyBag_WritePropertyKey(
#     _In_ IPropertyBag *propBag,
#     _In_ LPCWSTR propName,
#     _In_ REFPROPERTYKEY value);
PSPropertyBag_WritePropertyKey = propsys.PSPropertyBag_WritePropertyKey
PSPropertyBag_WritePropertyKey.restype = PSSTDAPI

# library PropSysObjects
# [version][lcid][uuid]
# __PropSysObjects_LIBRARY_DEFINED__
# INTerface __MIDL_itf_propsys_0000_0026
# [local]
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# Additional Prototypes for ALL INTerfaces
# [local]
# [annotation][in]
# [annotation][in]
# [call_as]
# [in]
# [in]
# [local]
# [annotation][out][in]
# [call_as]
# [in]
# [out]
# end of Additional Prototypes

__all__ = (
    'INamedPropertyStore', 'IPropertyEnumType',
    'IPersistSerializedPropStorage', 'IPropertyStoreCache',
    'IPropertyDescriptionSearchInfo', 'ICreateObject',
    'IPropertyChangeArray', 'IPropertySystemChangeNotify',
    'IPropertySystem', 'IPropertyDescriptionAliasInfo',
    'IPropertyEnumType2', 'IPropertyEnumTypeList',
    'IInitializeWithStream', 'IPropertyDescription2',
    'IDelayedPropertyStoreFactory', 'IPropertyStore',
    'IPropertyStoreCapabilities', 'IPropertyDescription',
    'IPropertyChange', 'IObjectWithPropertyKey',
    'IPersistSerializedPropStorage2', 'IPropertyDescriptionList',
    'IPropertyStoreFactory', 'IInitializeWithFile',
    'IPropertyDescriptionRelatedPropertyInfo', 'PSSTDAPI',
    'PKEY_PIDSTR_MAX', '__REQUIRED_RPCNDR_H_VERSION__',
    'GUIDSTRING_MAX', '__REQUIRED_RPCSAL_H_VERSION__', 'PKEYSTR_MAX',
    'PROPDESC_AGGREGATION_TYPE', 'PROPDESC_FORMAT_FLAGS',
    'PROPDESC_TYPE_FLAGS', 'PKA_FLAGS', 'PROPDESC_GROUPING_RANGE',
    'PROPDESC_CONDITION_TYPE', 'PROPDESC_SORTDESCRIPTION',
    'GETPROPERTYSTOREFLAGS', 'PROPDESC_COLUMNINDEX_TYPE', 'PROPENUMTYPE',
    'PROPDESC_ENUMFILTER', 'PROPDESC_RELATIVEDESCRIPTION_TYPE',
    'PSC_STATE', 'PROPDESC_DISPLAYTYPE', 'PROPDESC_SEARCHINFO_FLAGS',
    'PROPDESC_VIEW_FLAGS',
    'PERSIST_SPROPSTORE_FLAGS', 'PUSERIALIZEDPROPSTORAGE',
    'LPPROPERTYSTORE',
    'PCUSERIALIZEDPROPSTORAGE', 'REFPROPERTYKEY',
)
