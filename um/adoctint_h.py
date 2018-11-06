

from wtypes_h import (
    ENUM,
    POINTER,
    HRESULT,
    BSTR,
    VARIANT_BOOL,
    LONG,
    BYTE,
)
from guiddef_h import (
    IID,
)
import ctypes
import ntdef_h
import comtypes


from tchar_h import * # NOQA
__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA

from oaidl_h import * # NOQA
from ocidl_h import * # NOQA

class RuleEnum(ENUM):
    adRINone = 0
    adRICascade = 1
    adRISetNull = 2
    adRISetDefault = 3


class KeyTypeEnum(ENUM):
    adKeyPrimary = 1
    adKeyForeign = 2
    adKeyUnique = 3


class ActionEnum(ENUM):
    adAccessGrant = 1
    adAccessSet = 2
    adAccessDeny = 3
    adAccessRevoke = 4


class ColumnAttributesEnum(ENUM):
    adColFixed = 1
    adColNullable = 2


class SortOrderEnum(ENUM):
    adSortAscending = 1
    adSortDescending = 2


class RightsEnum(ENUM):
    adRightNone = 0
    adRightDrop = 0
    adRightExclusive = 1
    adRightReadDesign = 2
    adRightWriteDesign = 3
    adRightWithGrant = 4
    adRightReference = 5
    adRightCreate = 6
    adRightInsert = 7
    adRightDelete = 8
    adRightReadPermissions = 9
    adRightWritePermissions = 10
    adRightWriteOwner = 11
    adRightMaximumAllowed = 12
    adRightFull = 13
    adRightExecute = 14
    adRightUpdate = 15
    adRightRead = 16


class DataTypeEnum(ENUM):
    adEmpty = 0
    adTinyInt = 16
    adSmallInt = 2
    adInteger = 3
    adBigInt = 20
    adUnINTTinyInt = 17
    adUnINTSmallInt = 18
    adUnINTInt = 19
    adUnINTBigInt = 21
    adSingle = 4
    adDouble = 5
    adCurrency = 6
    adDecimal = 14
    adNumeric = 131
    adBoolean = 11
    adError = 10
    adUserDefined = 132
    adVariant = 12
    adIDispatch = 9
    adIUnknown = 13
    adGUID = 72
    adDate = 7
    adDBDate = 133
    adDBTime = 134
    adDBTimeStamp = 135
    adBSTR = 8
    adChar = 129
    adVarChar = 200
    adLongVarChar = 201
    adWChar = 130
    adVarWChar = 202
    adLongVarWChar = 203
    adBinary = 128
    adVarBinary = 204
    adLongVarBinary = 205
    adChapter = 136
    adFileTime = 64
    adPropVariant = 138
    adVarNumeric = 139


class AllowNullsEnum(ENUM):
    adIndexNullsAllow = 0
    adIndexNullsDisallow = 1
    adIndexNullsIgnore = 2
    adIndexNullsIgnoreAny = 4


class ObjectTypeEnum(ENUM):
    adPermObjProviderSpecific = - 1
    adPermObjTable = 1
    adPermObjColumn = 2
    adPermObjDatabase = 3
    adPermObjProcedure = 4
    adPermObjView = 5


class InheritTypeEnum(ENUM):
    adInheritNone = 0
    adInheritObjects = 1
    adInheritContainers = 2
    adInheritBoth = 3
    adInheritNoPropogate = 4


IID__ADOCollection = IID(
    '{00000512-0000-0010-8000-00AA006D2EA4}'
)


class _ADOCollection(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID__ADOCollection
    _idlflags_ = []


IID__ADODynaCollection = IID(
    '{00000513-0000-0010-8000-00AA006D2EA4}'
)


class _ADODynaCollection(_ADOCollection):
    _case_insensitive_ = True
    _iid_ = IID__ADODynaCollection
    _idlflags_ = []


IID__Group25 = IID(
    '{00000616-0000-0010-8000-00AA006D2EA4}'
)


class _Group25(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID__Group25
    _idlflags_ = []


IID__User25 = IID(
    '{00000619-0000-0010-8000-00AA006D2EA4}'
)


class _User25(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID__User25
    _idlflags_ = []


IID__ADOCatalog = IID(
    '{00000603-0000-0010-8000-00AA006D2EA4}'
)


class _ADOCatalog(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID__ADOCatalog
    _idlflags_ = []


IID__ADOTable = IID(
    '{00000610-0000-0010-8000-00AA006D2EA4}'
)


class _ADOTable(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID__ADOTable
    _idlflags_ = []


IID__ADOGroup = IID(
    '{00000628-0000-0010-8000-00AA006D2EA4}'
)


class _ADOGroup(_Group25):
    _case_insensitive_ = True
    _iid_ = IID__ADOGroup
    _idlflags_ = []


IID__ADOUser = IID(
    '{00000627-0000-0010-8000-00AA006D2EA4}'
)


class _ADOUser(_User25):
    _case_insensitive_ = True
    _iid_ = IID__ADOUser
    _idlflags_ = []


IID__ADOColumn = IID(
    '{0000061C-0000-0010-8000-00AA006D2EA4}'
)


class _ADOColumn(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID__ADOColumn
    _idlflags_ = []


IID__ADOIndex = IID(
    '{0000061F-0000-0010-8000-00AA006D2EA4}'
)


class _ADOIndex(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID__ADOIndex
    _idlflags_ = []


IID__ADOKey = IID(
    '{00000622-0000-0010-8000-00AA006D2EA4}'
)


class _ADOKey(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID__ADOKey
    _idlflags_ = []


IID_ADOView = IID(
    '{00000613-0000-0010-8000-00AA006D2EA4}'
)


class ADOView(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID_ADOView
    _idlflags_ = []


IID_ADOProcedure = IID(
    '{00000625-0000-0010-8000-00AA006D2EA4}'
)


class ADOProcedure(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID_ADOProcedure
    _idlflags_ = []


IID_ADOProperty = IID(
    '{00000503-0000-0010-8000-00AA006D2EA4}'
)


class ADOProperty(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID_ADOProperty
    _idlflags_ = []


IID_ADOTables = IID(
    '{00000611-0000-0010-8000-00AA006D2EA4}'
)


class ADOTables(_ADOCollection):
    _case_insensitive_ = True
    _iid_ = IID_ADOTables
    _idlflags_ = []


IID_ADOColumns = IID(
    '{0000061D-0000-0010-8000-00AA006D2EA4}'
)


class ADOColumns(_ADOCollection):
    _case_insensitive_ = True
    _iid_ = IID_ADOColumns
    _idlflags_ = []


IID_ADOProcedures = IID(
    '{00000626-0000-0010-8000-00AA006D2EA4}'
)


class ADOProcedures(_ADOCollection):
    _case_insensitive_ = True
    _iid_ = IID_ADOProcedures
    _idlflags_ = []


IID_ADOViews = IID(
    '{00000614-0000-0010-8000-00AA006D2EA4}'
)


class ADOViews(_ADOCollection):
    _case_insensitive_ = True
    _iid_ = IID_ADOViews
    _idlflags_ = []


IID_ADOIndexes = IID(
    '{00000620-0000-0010-8000-00AA006D2EA4}'
)


class ADOIndexes(_ADOCollection):
    _case_insensitive_ = True
    _iid_ = IID_ADOIndexes
    _idlflags_ = []


IID_ADOKeys = IID(
    '{00000623-0000-0010-8000-00AA006D2EA4}'
)


class ADOKeys(_ADOCollection):
    _case_insensitive_ = True
    _iid_ = IID_ADOKeys
    _idlflags_ = []


IID_ADOUsers = IID(
    '{0000061A-0000-0010-8000-00AA006D2EA4}'
)


class ADOUsers(_ADOCollection):
    _case_insensitive_ = True
    _iid_ = IID_ADOUsers
    _idlflags_ = []


IID_ADOGroups = IID(
    '{00000617-0000-0010-8000-00AA006D2EA4}'
)


class ADOGroups(_ADOCollection):
    _case_insensitive_ = True
    _iid_ = IID_ADOGroups
    _idlflags_ = []


IID_ADOProperties = IID(
    '{00000504-0000-0010-8000-00AA006D2EA4}'
)


class ADOProperties(_ADOCollection):
    _case_insensitive_ = True
    _iid_ = IID_ADOProperties
    _idlflags_ = []


COMMETHOD = comtypes.COMMETHOD

_ADOCollection._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Count',
            (['out', 'retval'], POINTER(LONG), 'c'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            '_NewEnum',
            (['out', 'retval'], POINTER(POINTER(comtypes.IUnknown)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Refresh',
        ),
    ]

_ADODynaCollection._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Append',
            (['in'], POINTER(IDispatch), 'Object'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Delete',
            (['in'], VARIANT, 'Item'),
        ),
    ]

_ADOCatalog._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Tables',
            (['out', 'retval'], POINTER(POINTER(ADOTables)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_ActiveConnection',
            (['out', 'retval'], POINTER(VARIANT), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_ActiveConnection',
            (['in'], VARIANT, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'putref_ActiveConnection',
            (['in'], POINTER(IDispatch), 'pCon'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Procedures',
            (['out', 'retval'], POINTER(POINTER(ADOProcedures)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Views',
            (['out', 'retval'], POINTER(POINTER(ADOViews)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Groups',
            (['out', 'retval'], POINTER(POINTER(ADOGroups)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Users',
            (['out', 'retval'], POINTER(POINTER(ADOUsers)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Create',
            (['in'], BSTR, 'ConnectString'),
            (['out', 'retval'], POINTER(VARIANT), 'Connection'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetObjectOwner',
            (['in'], BSTR, 'ObjectName'),
            (['in'], ObjectTypeEnum, 'ObjectType'),
            (['in'], VARIANT, 'ObjectTypeId'),
            (['out', 'retval'], POINTER(BSTR), 'OwnerName'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetObjectOwner',
            (['in'], BSTR, 'ObjectName'),
            (['in'], ObjectTypeEnum, 'ObjectType'),
            (['in'], BSTR, 'UserName'),
            (['in'], VARIANT, 'ObjectTypeId'),
        ),
    ]

_ADOTable._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Columns',
            (['out', 'retval'], POINTER(POINTER(ADOColumns)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Name',
            (['out', 'retval'], POINTER(BSTR), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Name',
            (['in'], BSTR, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Type',
            (['out', 'retval'], POINTER(BSTR), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Indexes',
            (['out', 'retval'], POINTER(POINTER(ADOIndexes)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Keys',
            (['out', 'retval'], POINTER(POINTER(ADOKeys)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Properties',
            (['out', 'retval'], POINTER(POINTER(ADOProperties)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_DateCreated',
            (['out', 'retval'], POINTER(VARIANT), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_DateModified',
            (['out', 'retval'], POINTER(VARIANT), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_ParentCatalog',
            (['out', 'retval'], POINTER(POINTER(_ADOCatalog)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_ParentCatalog',
            (['in'], POINTER(_ADOCatalog), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'putref_ParentCatalog',
            (['in'], POINTER(_ADOCatalog), 'ppvObject'),
        ),
    ]

_Group25._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_Name',
        (['out', 'retval'], POINTER(BSTR), 'pVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Name',
        (['in'], BSTR, 'newVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPermissions',
        (['in'], VARIANT, 'Name'),
        (['in'], ObjectTypeEnum, 'ObjectType'),
        (['in'], VARIANT, 'ObjectTypeId'),
        (['out', 'retval'], POINTER(RightsEnum), 'Rights'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPermissions',
        (['in'], VARIANT, 'Name'),
        (['in'], ObjectTypeEnum, 'ObjectType'),
        (['in'], ActionEnum, 'Action'),
        (['in'], RightsEnum, 'Rights'),
        (['in'], InheritTypeEnum, 'Inherit'),
        (['in'], VARIANT, 'ObjectTypeId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Users',
        (['out', 'retval'], POINTER(POINTER(ADOUsers)), 'ppvObject'),
    ),
]

_ADOGroup._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Properties',
            (['out', 'retval'], POINTER(POINTER(ADOProperties)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_ParentCatalog',
            (['out', 'retval'], POINTER(POINTER(_ADOCatalog)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_ParentCatalog',
            (['in'], POINTER(_ADOCatalog), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'putref_ParentCatalog',
            (['in'], POINTER(_ADOCatalog), 'ppvObject'),
        ),
    ]

_User25._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_Name',
        (['out', 'retval'], POINTER(BSTR), 'pVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Name',
        (['in'], BSTR, 'newVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPermissions',
        (['in'], VARIANT, 'Name'),
        (['in'], ObjectTypeEnum, 'ObjectType'),
        (['in'], VARIANT, 'ObjectTypeId'),
        (['out', 'retval'], POINTER(RightsEnum), 'Rights'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPermissions',
        (['in'], VARIANT, 'Name'),
        (['in'], ObjectTypeEnum, 'ObjectType'),
        (['in'], ActionEnum, 'Action'),
        (['in'], RightsEnum, 'Rights'),
        (['in'], InheritTypeEnum, 'Inherit'),
        (['in'], VARIANT, 'ObjectTypeId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ChangePassword',
        (['in'], BSTR, 'OldPassword'),
        (['in'], BSTR, 'NewPassword'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Groups',
        (['out', 'retval'], POINTER(POINTER(ADOGroups)), 'ppvObject'),
    ),
]

_ADOUser._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Properties',
            (['out', 'retval'], POINTER(POINTER(ADOProperties)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_ParentCatalog',
            (['out', 'retval'], POINTER(POINTER(_ADOCatalog)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_ParentCatalog',
            (['in'], POINTER(_ADOCatalog), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'putref_ParentCatalog',
            (['in'], POINTER(_ADOCatalog), 'ppvObject'),
        ),
    ]

_ADOColumn._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Name',
            (['out', 'retval'], POINTER(BSTR), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Name',
            (['in'], BSTR, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Attributes',
            (['out', 'retval'], POINTER(ColumnAttributesEnum), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Attributes',
            (['in'], ColumnAttributesEnum, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_DefinedSize',
            (['out', 'retval'], POINTER(LONG), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_DefinedSize',
            (['in'], LONG, 'DefinedSize'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_NumericScale',
            (['out', 'retval'], POINTER(BYTE), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_NumericScale',
            (['in'], BYTE, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Precision',
            (['out', 'retval'], POINTER(LONG), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Precision',
            (['in'], LONG, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_RelatedColumn',
            (['out', 'retval'], POINTER(BSTR), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_RelatedColumn',
            (['in'], BSTR, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_SortOrder',
            (['out', 'retval'], POINTER(SortOrderEnum), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_SortOrder',
            (['in'], SortOrderEnum, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Type',
            (['out', 'retval'], POINTER(DataTypeEnum), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Type',
            (['in'], DataTypeEnum, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Properties',
            (['out', 'retval'], POINTER(POINTER(ADOProperties)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_ParentCatalog',
            (['out', 'retval'], POINTER(POINTER(_ADOCatalog)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_ParentCatalog',
            (['in'], POINTER(_ADOCatalog), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'putref_ParentCatalog',
            (['in'], POINTER(_ADOCatalog), 'ppvObject'),
        ),
    ]

_ADOIndex._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Name',
            (['out', 'retval'], POINTER(BSTR), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Name',
            (['in'], BSTR, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Clustered',
            (['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Clustered',
            (['in'], VARIANT_BOOL, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_IndexNulls',
            (['out', 'retval'], POINTER(AllowNullsEnum), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_IndexNulls',
            (['in'], AllowNullsEnum, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_PrimaryKey',
            (['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_PrimaryKey',
            (['in'], VARIANT_BOOL, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Unique',
            (['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Unique',
            (['in'], VARIANT_BOOL, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Columns',
            (['out', 'retval'], POINTER(POINTER(ADOColumns)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Properties',
            (['out', 'retval'], POINTER(POINTER(ADOProperties)), 'ppvObject'),
        ),
    ]

_ADOKey._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Name',
            (['out', 'retval'], POINTER(BSTR), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Name',
            (['in'], BSTR, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_DeleteRule',
            (['out', 'retval'], POINTER(RuleEnum), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_DeleteRule',
            (['in'], RuleEnum, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Type',
            (['out', 'retval'], POINTER(KeyTypeEnum), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Type',
            (['in'], KeyTypeEnum, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_RelatedTable',
            (['out', 'retval'], POINTER(BSTR), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_RelatedTable',
            (['in'], BSTR, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_UpdateRule',
            (['out', 'retval'], POINTER(RuleEnum), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_UpdateRule',
            (['in'], RuleEnum, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Columns',
            (['out', 'retval'], POINTER(POINTER(ADOColumns)), 'ppvObject'),
        ),
    ]

ADOView._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Command',
            (['out', 'retval'], POINTER(VARIANT), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Command',
            (['in'], VARIANT, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'putref_Command',
            (['in'], POINTER(IDispatch), 'pComm'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Name',
            (['out', 'retval'], POINTER(BSTR), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_DateCreated',
            (['out', 'retval'], POINTER(VARIANT), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_DateModified',
            (['out', 'retval'], POINTER(VARIANT), 'pVal'),
        ),
    ]

ADOProcedure._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Command',
            (['out', 'retval'], POINTER(VARIANT), 'pVar'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Command',
            (['in'], VARIANT, 'newVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'putref_Command',
            (['in'], POINTER(IDispatch), 'pComm'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Name',
            (['out', 'retval'], POINTER(BSTR), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_DateCreated',
            (['out', 'retval'], POINTER(VARIANT), 'pVal'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_DateModified',
            (['out', 'retval'], POINTER(VARIANT), 'pVal'),
        ),
    ]

ADOProperty._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Value',
            (['out', 'retval'], POINTER(VARIANT), 'pval'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Value',
            (['in'], VARIANT, 'val'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Name',
            (['out', 'retval'], POINTER(BSTR), 'pbstr'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Type',
            (['out', 'retval'], POINTER(DataTypeEnum), 'ptype'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'get_Attributes',
            (['out', 'retval'], POINTER(LONG), 'plAttributes'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'put_Attributes',
            (['in'], LONG, 'lAttributes'),
        ),
    ]

ADOTables._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Item',
            (['in'], VARIANT, 'Item'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Append',
            (['in'], VARIANT, 'Item'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Delete',
            (['in'], VARIANT, 'Item'),
        ),
    ]

ADOColumns._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Item',
            (['in'], VARIANT, 'Item'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Append',
            (['in'], VARIANT, 'Item'),
            (['in'], DataTypeEnum, 'Type', DataTypeEnum.adVarWChar),
            (['in'], LONG, 'DefinedSize', 0),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Delete',
            (['in'], VARIANT, 'Item'),
        ),
    ]

ADOProcedures._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Item',
            (['in'], VARIANT, 'Item'),
            (['out', 'retval'], POINTER(POINTER(ADOProcedure)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Append',
            (['in'], BSTR, 'Name'),
            (['in'], POINTER(IDispatch), 'Command'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Delete',
            (['in'], VARIANT, 'Item'),
        ),
    ]

ADOViews._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Item',
            (['in'], VARIANT, 'Item'),
            (['out', 'retval'], POINTER(POINTER(ADOView)), 'ppvObject'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Append',
            (['in'], BSTR, 'Name'),
            (['in'], POINTER(IDispatch), 'Command'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Delete',
            (['in'], VARIANT, 'Item'),
        ),
    ]

ADOIndexes._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Item',
            (['in'], VARIANT, 'Item'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Append',
            (['in'], VARIANT, 'Item'),
            (['in'], VARIANT, 'columns'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Delete',
            (['in'], VARIANT, 'Item'),
        ),
    ]

ADOKeys._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Item',
            (['in'], VARIANT, 'Item'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Append',
            (['in'], VARIANT, 'Item'),
            (['in'], KeyTypeEnum, 'Type'),
            (['in'], VARIANT, 'Column'),
            (['in'], BSTR, 'RelatedADOTable', ''),
            (['in'], BSTR, 'RelatedADOColumn', ''),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Delete',
            (['in'], VARIANT, 'Item'),
        ),
    ]

ADOUsers._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Item',
            (['in'], VARIANT, 'Item'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Append',
            (['in'], VARIANT, 'Item'),
            (['in'], BSTR, 'Password', ''),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Delete',
            (['in'], VARIANT, 'Item'),
        ),
    ]


ADOGroups._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Item',
            (['in'], VARIANT, 'Item'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Append',
            (['in'], VARIANT, 'Item'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Delete',
            (['in'], VARIANT, 'Item'),
        ),
    ]



ADOProperties._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'get_Item',
            (['in'], VARIANT, 'Item'),
            (['out', 'retval'], POINTER(POINTER(ADOProperty)), 'ppvObject'),
        ),
    ]


ADOCatalog = _ADOCatalog
ADOTable = _ADOTable
ADOGroup = _ADOGroup
ADOUser = _ADOUser
ADOIndex = _ADOIndex
ADOColumn = _ADOColumn
ADOKey = _ADOKey
# ADOParameter = _ADOParameter
ADOCollection = _ADOCollection
ADODynaCollection = _ADODynaCollection

__all__ = (
    'ADOProperties', 'ADOUsers', '_Group25', 'ADOViews', '_ADOCatalog',
    '_ADOIndex', '_ADOKey', 'ADOIndexes', '_ADOUser', 'ADOProcedures',
    '_User25', 'ADOProperty', '_ADOTable', 'ADOKeys',
    'ADOView', 'ADOTables', '_ADOGroup', 'ADOProcedure', 'ADOGroups',
    'ADOColumns', '_ADOColumn', 'ADOKey', 'ADOGroup', 'ADOColumn', 'ADOTable',
    '__REQUIRED_RPCNDR_H_VERSION__', '__REQUIRED_RPCSAL_H_VERSION__',
    'ADODynaCollection', 'ADOUser', 'ADOCatalog', 'ADOIndex',
    'ADOCollection', 'InheritTypeEnum', 'DataTypeEnum', 'RightsEnum',
    'SortOrderEnum', 'KeyTypeEnum', 'AllowNullsEnum', 'ActionEnum',
    'ColumnAttributesEnum', 'ObjectTypeEnum', 'RuleEnum',
)
