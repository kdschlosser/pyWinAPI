
from wtypes_h import (
    ENUM,
    ULONG,
    POINTER,
    HRESULT,
    DWORD,
    UINT,
    GUID,
    LPCOLESTR,
    REFIID,
    BSTR,
    CLSID,
    LPOLESTR,
)
from guiddef_h import (
    IID,
)
import ctypes
import comtypes


__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
IID_IDebugProperty = IID(
    '{51973C50-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugProperty(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugProperty
    _idlflags_ = []


IID_IEnumDebugPropertyInfo = IID(
    '{51973C51-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IEnumDebugPropertyInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumDebugPropertyInfo
    _idlflags_ = []


IID_IDebugExtendedProperty = IID(
    '{51973C52-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugExtendedProperty(IDebugProperty):
    _case_insensitive_ = True
    _iid_ = IID_IDebugExtendedProperty
    _idlflags_ = []


IID_IEnumDebugExtendedPropertyInfo = IID(
    '{51973C53-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IEnumDebugExtendedPropertyInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumDebugExtendedPropertyInfo
    _idlflags_ = []


IID_IPerPropertyBrowsing2 = IID(
    '{51973C54-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IPerPropertyBrowsing2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPerPropertyBrowsing2
    _idlflags_ = []


IID_IDebugPropertyEnumType_All = IID(
    '{51973C55-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugPropertyEnumType_All(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugPropertyEnumType_All
    _idlflags_ = []


IID_IDebugPropertyEnumType_Locals = IID(
    '{51973C56-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugPropertyEnumType_Locals(IDebugPropertyEnumType_All):
    _case_insensitive_ = True
    _iid_ = IID_IDebugPropertyEnumType_Locals
    _idlflags_ = []


IID_IDebugPropertyEnumType_Arguments = IID(
    '{51973C57-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugPropertyEnumType_Arguments(IDebugPropertyEnumType_All):
    _case_insensitive_ = True
    _iid_ = IID_IDebugPropertyEnumType_Arguments
    _idlflags_ = []


IID_IDebugPropertyEnumType_LocalsPlusArgs = IID(
    '{51973C58-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugPropertyEnumType_LocalsPlusArgs(IDebugPropertyEnumType_All):
    _case_insensitive_ = True
    _iid_ = IID_IDebugPropertyEnumType_LocalsPlusArgs
    _idlflags_ = []


IID_IDebugPropertyEnumType_Registers = IID(
    '{51973C59-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugPropertyEnumType_Registers(IDebugPropertyEnumType_All):
    _case_insensitive_ = True
    _iid_ = IID_IDebugPropertyEnumType_Registers
    _idlflags_ = []


from ocidl_h import * # NOQA
from winapifamily_h import * # NOQA


class __MIDL___MIDL_itf_dbgprop_0000_0000_0001(ENUM):
    DBGPROP_ATTRIB_NO_ATTRIB = 0
    DBGPROP_ATTRIB_VALUE_IS_INVALID = 0x8
    DBGPROP_ATTRIB_VALUE_IS_EXPANDABLE = 0x10
    DBGPROP_ATTRIB_VALUE_IS_FAKE = 0x20
    DBGPROP_ATTRIB_VALUE_IS_METHOD = 0x100
    DBGPROP_ATTRIB_VALUE_IS_EVENT = 0x200
    DBGPROP_ATTRIB_VALUE_IS_RAW_STRING = 0x400
    DBGPROP_ATTRIB_VALUE_READONLY = 0x800
    DBGPROP_ATTRIB_ACCESS_PUBLIC = 0x1000
    DBGPROP_ATTRIB_ACCESS_PRIVATE = 0x2000
    DBGPROP_ATTRIB_ACCESS_PROTECTED = 0x4000
    DBGPROP_ATTRIB_ACCESS_FINAL = 0x8000
    DBGPROP_ATTRIB_STORAGE_GLOBAL = 0x10000
    DBGPROP_ATTRIB_STORAGE_STATIC = 0x20000
    DBGPROP_ATTRIB_STORAGE_FIELD = 0x40000
    DBGPROP_ATTRIB_STORAGE_VIRTUAL = 0x80000
    DBGPROP_ATTRIB_TYPE_IS_CONSTANT = 0x100000
    DBGPROP_ATTRIB_TYPE_IS_SYNCHRONIZED = 0x200000
    DBGPROP_ATTRIB_TYPE_IS_VOLATILE = 0x400000
    DBGPROP_ATTRIB_HAS_EXTENDED_ATTRIBS = 0x800000
    DBGPROP_ATTRIB_FRAME_INTRYBLOCK = 0x1000000
    DBGPROP_ATTRIB_FRAME_INCATCHBLOCK = 0x2000000
    DBGPROP_ATTRIB_FRAME_INFINALLYBLOCK = 0x4000000
    DBGPROP_ATTRIB_VALUE_IS_RETURN_VALUE = 0x8000000
    DBGPROP_ATTRIB_VALUE_PENDING_MUTATION = 0x10000000


DBGPROP_ATTRIB_FLAGS = DWORD


class __MIDL___MIDL_itf_dbgprop_0000_0000_0002(ENUM):
    DBGPROP_INFO_NAME = 0x1
    DBGPROP_INFO_TYPE = 0x2
    DBGPROP_INFO_VALUE = 0x4
    DBGPROP_INFO_FULLNAME = 0x20
    DBGPROP_INFO_ATTRIBUTES = 0x8
    DBGPROP_INFO_DEBUGPROP = 0x10
    DBGPROP_INFO_BEAUTIFY = 0x2000000
    DBGPROP_INFO_CALLTOSTRING = 0x4000000
    DBGPROP_INFO_AUTOEXPAND = 0x8000000



DBGPROP_INFO_FLAGS = DWORD
DBGPROP_INFO_STANDARD = (
    (
        (
            (
                __MIDL___MIDL_itf_dbgprop_0000_0000_0002.DBGPROP_INFO_NAME |
                __MIDL___MIDL_itf_dbgprop_0000_0000_0002.DBGPROP_INFO_TYPE
            ) |
            __MIDL___MIDL_itf_dbgprop_0000_0000_0002.DBGPROP_INFO_VALUE
        ) |
        __MIDL___MIDL_itf_dbgprop_0000_0000_0002.DBGPROP_INFO_ATTRIBUTES
    )
)
DBGPROP_INFO_ALL = (
    (
        (
            (
                (
                    (
                        __MIDL___MIDL_itf_dbgprop_0000_0000_0002.DBGPROP_INFO_NAME |
                        __MIDL___MIDL_itf_dbgprop_0000_0000_0002.DBGPROP_INFO_TYPE
                    ) |
                    __MIDL___MIDL_itf_dbgprop_0000_0000_0002.DBGPROP_INFO_VALUE
                ) |
                __MIDL___MIDL_itf_dbgprop_0000_0000_0002.DBGPROP_INFO_FULLNAME
            ) |
            __MIDL___MIDL_itf_dbgprop_0000_0000_0002.DBGPROP_INFO_ATTRIBUTES
        ) |
        __MIDL___MIDL_itf_dbgprop_0000_0000_0002.DBGPROP_INFO_DEBUGPROP
    )
)


class tagOBJECT_ATTRIB_FLAG(ENUM):
    OBJECT_ATTRIB_NO_ATTRIB = 0
    OBJECT_ATTRIB_NO_NAME = 0x1
    OBJECT_ATTRIB_NO_TYPE = 0x2
    OBJECT_ATTRIB_NO_VALUE = 0x4
    OBJECT_ATTRIB_VALUE_IS_INVALID = 0x8
    OBJECT_ATTRIB_VALUE_IS_OBJECT = 0x10
    OBJECT_ATTRIB_VALUE_IS_ENUM = 0x20
    OBJECT_ATTRIB_VALUE_IS_CUSTOM = 0x40
    OBJECT_ATTRIB_OBJECT_IS_EXPANDABLE = 0x70
    OBJECT_ATTRIB_VALUE_HAS_CODE = 0x80
    OBJECT_ATTRIB_TYPE_IS_OBJECT = 0x100
    OBJECT_ATTRIB_TYPE_HAS_CODE = 0x200
    OBJECT_ATTRIB_TYPE_IS_EXPANDABLE = 0x100
    OBJECT_ATTRIB_SLOT_IS_CATEGORY = 0x400
    OBJECT_ATTRIB_VALUE_READONLY = 0x800
    OBJECT_ATTRIB_ACCESS_PUBLIC = 0x1000
    OBJECT_ATTRIB_ACCESS_PRIVATE = 0x2000
    OBJECT_ATTRIB_ACCESS_PROTECTED = 0x4000
    OBJECT_ATTRIB_ACCESS_FINAL = 0x8000
    OBJECT_ATTRIB_STORAGE_GLOBAL = 0x10000
    OBJECT_ATTRIB_STORAGE_STATIC = 0x20000
    OBJECT_ATTRIB_STORAGE_FIELD = 0x40000
    OBJECT_ATTRIB_STORAGE_VIRTUAL = 0x80000
    OBJECT_ATTRIB_TYPE_IS_CONSTANT = 0x100000
    OBJECT_ATTRIB_TYPE_IS_SYNCHRONIZED = 0x200000
    OBJECT_ATTRIB_TYPE_IS_VOLATILE = 0x400000
    OBJECT_ATTRIB_HAS_EXTENDED_ATTRIBS = 0x800000
    OBJECT_ATTRIB_IS_CLASS = 0x1000000
    OBJECT_ATTRIB_IS_FUNCTION = 0x2000000
    OBJECT_ATTRIB_IS_VARIABLE = 0x4000000
    OBJECT_ATTRIB_IS_PROPERTY = 0x8000000
    OBJECT_ATTRIB_IS_MACRO = 0x10000000
    OBJECT_ATTRIB_IS_TYPE = 0x20000000
    OBJECT_ATTRIB_IS_INHERITED = 0x40000000
    OBJECT_ATTRIB_IS_INTERFACE = 0x80000000


OBJECT_ATTRIB_FLAGS = tagOBJECT_ATTRIB_FLAG


class tagPROP_INFO_FLAGS(ENUM):
    PROP_INFO_NAME = 0x1
    PROP_INFO_TYPE = 0x2
    PROP_INFO_VALUE = 0x4
    PROP_INFO_FULLNAME = 0x20
    PROP_INFO_ATTRIBUTES = 0x8
    PROP_INFO_DEBUGPROP = 0x10
    PROP_INFO_AUTOEXPAND = 0x8000000


PROP_INFO_FLAGS = tagPROP_INFO_FLAGS


PROP_INFO_STANDARD = (
    (
        (
            (PROP_INFO_FLAGS.PROP_INFO_NAME | PROP_INFO_FLAGS.PROP_INFO_TYPE) |
            PROP_INFO_FLAGS.PROP_INFO_VALUE
        ) |
        PROP_INFO_FLAGS.PROP_INFO_ATTRIBUTES
    )
)
PROP_INFO_ALL = (
    (
        (
            (
                (
                    (
                        PROP_INFO_FLAGS.PROP_INFO_NAME |
                        PROP_INFO_FLAGS.PROP_INFO_TYPE
                    ) |
                    PROP_INFO_FLAGS.PROP_INFO_VALUE
                ) |
                PROP_INFO_FLAGS.PROP_INFO_FULLNAME
            ) |
            PROP_INFO_FLAGS.PROP_INFO_ATTRIBUTES
        ) |
        PROP_INFO_FLAGS.PROP_INFO_DEBUGPROP
    )
)


class tagDebugPropertyInfo(ctypes.Structure):
    _fields_ = [
        ('m_dwValidFields', DWORD),
        ('m_bstrName', BSTR),
        ('m_bstrType', BSTR),
        ('m_bstrValue', BSTR),
        ('m_bstrFullName', BSTR),
        ('m_dwAttrib', DWORD),
        ('m_pDebugProp', POINTER(IDebugProperty)),
    ]


DebugPropertyInfo = tagDebugPropertyInfo


class tagEX_PROP_INFO_FLAGS(ENUM):
    EX_PROP_INFO_ID = 0x100
    EX_PROP_INFO_NTYPE = 0x200
    EX_PROP_INFO_NVALUE = 0x400
    EX_PROP_INFO_LOCKBYTES = 0x800
    EX_PROP_INFO_DEBUGEXTPROP = 0x1000


EX_PROP_INFO_FLAGS = tagEX_PROP_INFO_FLAGS

from propidl_h import VARIANT
from objidl_h import ILockBytes
from oaidl_h import DISPID


class tagExtendedDebugPropertyInfo(ctypes.Structure):
    _fields_ = [
        ('dwValidFields', DWORD),
        ('pszName', LPOLESTR),
        ('pszType', LPOLESTR),
        ('pszValue', LPOLESTR),
        ('pszFullName', LPOLESTR),
        ('dwAttrib', DWORD),
        ('pDebugProp', POINTER(IDebugProperty)),
        ('nDISPID', DWORD),
        ('nType', DWORD),
        ('varValue', VARIANT),
        ('plbValue', POINTER(ILockBytes)),
        ('pDebugExtProp', POINTER(IDebugExtendedProperty)),
    ]


ExtendedDebugPropertyInfo = tagExtendedDebugPropertyInfo


COMMETHOD = comtypes.COMMETHOD


IDebugProperty._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetPropertyInfo',
        (['in'], DWORD, 'dwFieldSpec'),
        (['in'], UINT, 'nRadix'),
        (['out'], POINTER(DebugPropertyInfo), 'pPropertyInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetExtendedInfo',
        (['in'], ULONG, 'cInfos'),
        (['in'], POINTER(GUID), 'rgguidExtendedInfo'),
        (['out'], POINTER(VARIANT), 'rgvar'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetValueAsString',
        (['in'], LPCOLESTR, 'pszValue'),
        (['in'], UINT, 'nRadix'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumMembers',
        (['in'], DWORD, 'dwFieldSpec'),
        (['in'], UINT, 'nRadix'),
        (['in'], REFIID, 'refiid'),
        (['out'], POINTER(POINTER(IEnumDebugPropertyInfo)), 'ppepi'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetParent',
        (['out'], POINTER(POINTER(IDebugProperty)), 'ppDebugProp'),
    ),
]


IEnumDebugPropertyInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(DebugPropertyInfo), 'pi'),
        (['out'], POINTER(ULONG), 'pcEltsfetched'),
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
        (['out'], POINTER(POINTER(IEnumDebugPropertyInfo)), 'ppepi'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCount',
        (['out'], POINTER(ULONG), 'pcelt'),
    ),
]


IDebugExtendedProperty._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetExtendedPropertyInfo',
        (['in'], DWORD, 'dwFieldSpec'),
        (['in'], UINT, 'nRadix'),
        (['out'], POINTER(ExtendedDebugPropertyInfo), 'pExtendedPropertyInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumExtendedMembers',
        (['in'], DWORD, 'dwFieldSpec'),
        (['in'], UINT, 'nRadix'),
        (['out'], POINTER(POINTER(IEnumDebugExtendedPropertyInfo)), 'ppeepi'),
    ),
]


IEnumDebugExtendedPropertyInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        ([], POINTER(ExtendedDebugPropertyInfo), 'rgExtendedPropertyInfo'),
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
        (['out'], POINTER(POINTER(IEnumDebugExtendedPropertyInfo)), 'pedpe'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCount',
        (['out'], POINTER(ULONG), 'pcelt'),
    ),
]


IPerPropertyBrowsing2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDisplayString',
        (['in'], DISPID, 'dispid'),
        (['out'], POINTER(BSTR), 'pBstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'MapPropertyToPage',
        (['in'], DISPID, 'dispid'),
        (['out'], POINTER(CLSID), 'pClsidPropPage'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPredefinedStrings',
        (['in'], DISPID, 'dispid'),
        (['out'], POINTER(CALPOLESTR), 'pCaStrings'),
        (['out'], POINTER(CADWORD), 'pCaCookies'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPredefinedValue',
        (['in'], DISPID, 'dispid'),
        (['in'], DWORD, 'dwCookie'),
    ),
]


IDebugPropertyEnumType_All._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetName',
        (['out'], POINTER(BSTR), '__MIDL__IDebugPropertyEnumType_All0000'),
    ),
]



__all__ = (
    'IDebugPropertyEnumType_LocalsPlusArgs', 'IEnumDebugExtendedPropertyInfo',
    'IDebugPropertyEnumType_Arguments', 'IDebugPropertyEnumType_Locals',
    'IDebugExtendedProperty', 'IDebugProperty', 'IDebugPropertyEnumType_All',
    'IDebugPropertyEnumType_Registers', 'IPerPropertyBrowsing2',
    'IEnumDebugPropertyInfo', 'PROP_INFO_STANDARD', 'DBGPROP_INFO_STANDARD',
    '__REQUIRED_RPCNDR_H_VERSION__', '__REQUIRED_RPCSAL_H_VERSION__',
    'PROP_INFO_ALL', 'DBGPROP_INFO_ALL', 'tagEX_PROP_INFO_FLAGS',
    '__MIDL___MIDL_itf_dbgprop_0000_0000_0001', 'EX_PROP_INFO_FLAGS',
    '__MIDL___MIDL_itf_dbgprop_0000_0000_0002', 'OBJECT_ATTRIB_FLAGS',
    'tagOBJECT_ATTRIB_FLAG', 'PROP_INFO_FLAGS', 'tagPROP_INFO_FLAGS',
    'tagExtendedDebugPropertyInfo', 'DebugPropertyInfo', 'DBGPROP_INFO_FLAGS',
    'ExtendedDebugPropertyInfo', 'tagDebugPropertyInfo',
    'DBGPROP_ATTRIB_FLAGS',
)
