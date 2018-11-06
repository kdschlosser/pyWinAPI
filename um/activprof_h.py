

from wtypes_h import (
    ENUM,
    REFCLSID,
    DWORD,
    HRESULT,
    WCHAR,
    POINTER,
    ULONG,
    LPCWSTR,
    UINT,
    DOUBLE,
    BSTR,
    USHORT,
    LONG,
    DWORD_PTR,
    VOID
)
from guiddef_h import (
    DEFINE_GUID,
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
IID_IActiveScriptProfilerControl = IID(
    '{784b5ff0-69b0-47d1-a7dc-2518f4230e90}'
)


class IActiveScriptProfilerControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptProfilerControl
    _idlflags_ = []


IID_IActiveScriptProfilerControl2 = IID(
    '{47810165-498F-40be-94F1-653557E9E7DA}'
)


class IActiveScriptProfilerControl2(IActiveScriptProfilerControl):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptProfilerControl2
    _idlflags_ = []


IID_IActiveScriptProfilerHeapEnum = IID(
    '{32E4694E-0D37-419B-B93D-FA20DED6E8EA}'
)


class IActiveScriptProfilerHeapEnum(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptProfilerHeapEnum
    _idlflags_ = []


IID_IActiveScriptProfilerControl3 = IID(
    '{0B403015-F381-4023-A5D0-6FED076DE716}'
)


class IActiveScriptProfilerControl3(IActiveScriptProfilerControl2):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptProfilerControl3
    _idlflags_ = []


IID_IActiveScriptProfilerControl4 = IID(
    '{160F94FD-9DBC-40D4-9EAC-2B71DB3132F4}'
)


class IActiveScriptProfilerControl4(IActiveScriptProfilerControl3):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptProfilerControl4
    _idlflags_ = []


IID_IActiveScriptProfilerControl5 = IID(
    '{1C01A2D1-8F0F-46A5-9720-0D7ED2C62F0A}'
)


class IActiveScriptProfilerControl5(IActiveScriptProfilerControl4):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptProfilerControl5
    _idlflags_ = []


IID_IActiveScriptProfilerCallback = IID(
    '{740eca23-7d9d-42e5-ba9d-f8b24b1c7a9b}'
)


class IActiveScriptProfilerCallback(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptProfilerCallback
    _idlflags_ = []


IID_IActiveScriptProfilerCallback2 = IID(
    '{31B7F8AD-A637-409C-B22F-040995B6103D}'
)


class IActiveScriptProfilerCallback2(IActiveScriptProfilerCallback):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptProfilerCallback2
    _idlflags_ = []


IID_IActiveScriptProfilerCallback3 = IID(
    '{6ac5ad25-2037-4687-91df-b59979d93d73}'
)


class IActiveScriptProfilerCallback3(IActiveScriptProfilerCallback2):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptProfilerCallback3
    _idlflags_ = []


from unknwn_h import * # NOQA
from winapifamily_h import * # NOQA
STATIC_IID_IActiveScriptProfilerHeapEnum = DEFINE_GUID(
    0x32E4694E,
    0xD37,
    0x419B,
    0xB9,
    0x3D,
    0xFA,
    0x20,
    0xDE,
    0xD6,
    0xE8,
    0xEA
)
STATIC_IID_IActiveScriptProfilerControl3 = DEFINE_GUID(
    0xB403015,
    0xF381,
    0x4023,
    0xA5,
    0xD0,
    0x6F,
    0xED,
    0x7,
    0x6D,
    0xE7,
    0x16
)


class __MIDL___MIDL_itf_activprof_0000_0000_0001(ENUM):
    PROFILER_SCRIPT_TYPE_USER = 0
    PROFILER_SCRIPT_TYPE_DYNAMIC = PROFILER_SCRIPT_TYPE_USER + 1
    PROFILER_SCRIPT_TYPE_NATIVE = PROFILER_SCRIPT_TYPE_DYNAMIC + 1
    PROFILER_SCRIPT_TYPE_DOM = PROFILER_SCRIPT_TYPE_NATIVE + 1


PROFILER_SCRIPT_TYPE = __MIDL___MIDL_itf_activprof_0000_0000_0001


class __MIDL___MIDL_itf_activprof_0000_0000_0002(ENUM):
    PROFILER_EVENT_MASK_TRACE_SCRIPT_FUNCTION_CALL = 0x1
    PROFILER_EVENT_MASK_TRACE_NATIVE_FUNCTION_CALL = 0x2
    PROFILER_EVENT_MASK_TRACE_DOM_FUNCTION_CALL = 0x4
    PROFILER_EVENT_MASK_TRACE_ALL = (
        PROFILER_EVENT_MASK_TRACE_SCRIPT_FUNCTION_CALL |
        PROFILER_EVENT_MASK_TRACE_NATIVE_FUNCTION_CALL
    )
    PROFILER_EVENT_MASK_TRACE_ALL_WITH_DOM = (
        PROFILER_EVENT_MASK_TRACE_ALL |
        PROFILER_EVENT_MASK_TRACE_DOM_FUNCTION_CALL
    )


PROFILER_EVENT_MASK = __MIDL___MIDL_itf_activprof_0000_0000_0002


PROFILER_TOKEN = LONG
COMMETHOD = comtypes.COMMETHOD


IActiveScriptProfilerControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'StartProfiling',
        ([], REFCLSID, 'clsidProfilerObject'),
        ([], DWORD, 'dwEventMask'),
        ([], DWORD, 'dwContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetProfilerEventMask',
        ([], DWORD, 'dwEventMask'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'StopProfiling',
        ([], HRESULT, 'hrShutdownReason'),
    ),
]


IActiveScriptProfilerControl2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'PrepareProfilerStop'
    ),
]


PROFILER_HEAP_OBJECT_ID = DWORD_PTR
PROFILER_HEAP_OBJECT_NAME_ID = UINT
PROFILER_EXTERNAL_OBJECT_ADDRESS = POINTER(VOID)


class __MIDL___MIDL_itf_activprof_0000_0002_0001(ENUM):
    PROFILER_HEAP_OBJECT_FLAGS_NEW_OBJECT = 0x1
    PROFILER_HEAP_OBJECT_FLAGS_IS_ROOT = 0x2
    PROFILER_HEAP_OBJECT_FLAGS_SITE_CLOSED = 0x4
    PROFILER_HEAP_OBJECT_FLAGS_EXTERNAL = 0x8
    PROFILER_HEAP_OBJECT_FLAGS_EXTERNAL_UNKNOWN = 0x10
    PROFILER_HEAP_OBJECT_FLAGS_EXTERNAL_DISPATCH = 0x20
    PROFILER_HEAP_OBJECT_FLAGS_SIZE_APPROXIMATE = 0x40
    PROFILER_HEAP_OBJECT_FLAGS_SIZE_UNAVAILABLE = 0x80
    PROFILER_HEAP_OBJECT_FLAGS_NEW_STATE_UNAVAILABLE = 0x100
    PROFILER_HEAP_OBJECT_FLAGS_WINRT_INSTANCE = 0x200
    PROFILER_HEAP_OBJECT_FLAGS_WINRT_RUNTIMECLASS = 0x400
    PROFILER_HEAP_OBJECT_FLAGS_WINRT_DELEGATE = 0x800
    PROFILER_HEAP_OBJECT_FLAGS_WINRT_NAMESPACE = 0x1000


PROFILER_HEAP_OBJECT_FLAGS = __MIDL___MIDL_itf_activprof_0000_0002_0001


class __MIDL___MIDL_itf_activprof_0000_0002_0002(ENUM):
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_PROTOTYPE = 0x1
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_FUNCTION_NAME = 0x2
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_SCOPE_LIST = 0x3
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_INTERNAL_PROPERTY = 0x4
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_NAME_PROPERTIES = 0x5
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_INDEX_PROPERTIES = 0x6
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_ELEMENT_ATTRIBUTES_SIZE = 0x7
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_ELEMENT_TEXT_CHILDREN_SIZE = 0x8
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_RELATIONSHIPS = 0x9
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_WINRTEVENTS = 0xA
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_WEAKMAP_COLLECTION_LIST = 0xB
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_MAP_COLLECTION_LIST = 0xC
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_SET_COLLECTION_LIST = 0xD
    PROFILER_HEAP_OBJECT_OPTIONAL_INFO_MAX_VALUE = (
        PROFILER_HEAP_OBJECT_OPTIONAL_INFO_SET_COLLECTION_LIST
    )


PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = __MIDL___MIDL_itf_activprof_0000_0002_0002


class __MIDL___MIDL_itf_activprof_0000_0002_0003(ENUM):
    PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS_NONE = 0
    PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS_IS_GET_ACCESSOR = 0x10000
    PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS_IS_SET_ACCESSOR = 0x20000
    PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS_LET_VARIABLE = 0x40000
    PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS_CONST_VARIABLE = 0x80000


PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS = __MIDL___MIDL_itf_activprof_0000_0002_0003


class __MIDL___MIDL_itf_activprof_0000_0002_0004(ENUM):
    PROFILER_HEAP_ENUM_FLAGS_NONE = 0
    PROFILER_HEAP_ENUM_FLAGS_STORE_RELATIONSHIP_FLAGS = 0x1
    PROFILER_HEAP_ENUM_FLAGS_SUBSTRINGS = 0x2
    PROFILER_HEAP_ENUM_FLAGS_RELATIONSHIP_SUBSTRINGS = (
        PROFILER_HEAP_ENUM_FLAGS_STORE_RELATIONSHIP_FLAGS |
PROFILER_HEAP_ENUM_FLAGS_SUBSTRINGS
    )


PROFILER_HEAP_ENUM_FLAGS = __MIDL___MIDL_itf_activprof_0000_0002_0004



class _PROFILER_HEAP_OBJECT_SCOPE_LIST(ctypes.Structure):
    _fields_ = [
        ('count', UINT),
        ('scopes', PROFILER_HEAP_OBJECT_ID * 1),
    ]


PROFILER_HEAP_OBJECT_SCOPE_LIST = _PROFILER_HEAP_OBJECT_SCOPE_LIST


class __MIDL___MIDL_itf_activprof_0000_0002_0005(ENUM):
    PROFILER_PROPERTY_TYPE_NUMBER = 0x1
    PROFILER_PROPERTY_TYPE_STRING = 0x2
    PROFILER_PROPERTY_TYPE_HEAP_OBJECT = 0x3
    PROFILER_PROPERTY_TYPE_EXTERNAL_OBJECT = 0x4
    PROFILER_PROPERTY_TYPE_BSTR = 0x5
    PROFILER_PROPERTY_TYPE_SUBSTRING = 0x6


PROFILER_RELATIONSHIP_INFO = __MIDL___MIDL_itf_activprof_0000_0002_0005



class _PROFILER_PROPERTY_TYPE_SUBSTRING_INFO(ctypes.Structure):
    _fields_ = [
        ('length', UINT),
        ('value', LPCWSTR),
    ]


PROFILER_PROPERTY_TYPE_SUBSTRING_INFO = _PROFILER_PROPERTY_TYPE_SUBSTRING_INFO



class _PROFILER_HEAP_OBJECT_RELATIONSHIP(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('numberValue', DOUBLE),
            ('stringValue', LPCWSTR),
            ('bstrValue', BSTR),
            ('objectId', PROFILER_HEAP_OBJECT_ID),
            ('externalObjectAddress', PROFILER_EXTERNAL_OBJECT_ADDRESS),
            ('subString', POINTER(PROFILER_PROPERTY_TYPE_SUBSTRING_INFO)),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('relationshipId', PROFILER_HEAP_OBJECT_NAME_ID),
        ('relationshipInfo', PROFILER_RELATIONSHIP_INFO),
        ('_Union_0', _Union_0),
    ]


PROFILER_HEAP_OBJECT_RELATIONSHIP = _PROFILER_HEAP_OBJECT_RELATIONSHIP



class _PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST(ctypes.Structure):
    _fields_ = [
        ('count', UINT),
        ('elements', PROFILER_HEAP_OBJECT_RELATIONSHIP * 1),
    ]


PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST = _PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST



class _PROFILER_HEAP_OBJECT_OPTIONAL_INFO(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('prototype', PROFILER_HEAP_OBJECT_ID),
            ('functionName', LPCWSTR),
            ('elementAttributesSize', UINT),
            ('elementTextChildrenSize', UINT),
            ('scopeList', POINTER(PROFILER_HEAP_OBJECT_SCOPE_LIST)),
            ('INTernalProperty', POINTER(PROFILER_HEAP_OBJECT_RELATIONSHIP)),
            ('namePropertyList', POINTER(PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)),
            ('indexPropertyList', POINTER(PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)),
            ('relationshipList', POINTER(PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)),
            ('eventList', POINTER(PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)),
            ('weakMapCollectionList', POINTER(PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)),
            ('mapCollectionList', POINTER(PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)),
            ('setCollectionList', POINTER(PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('_Union_0', _Union_0),
    ]


PROFILER_HEAP_OBJECT_OPTIONAL_INFO = _PROFILER_HEAP_OBJECT_OPTIONAL_INFO



class _PROFILER_HEAP_OBJECT(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('objectId', PROFILER_HEAP_OBJECT_ID),
            ('externalObjectAddress', PROFILER_EXTERNAL_OBJECT_ADDRESS),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('size', UINT),
        ('_Union_0', _Union_0),
        ('typeNameId', PROFILER_HEAP_OBJECT_NAME_ID),
        ('flags', ULONG),
        ('unused', USHORT),
        ('optionalInfoCount', USHORT),
    ]


PROFILER_HEAP_OBJECT = _PROFILER_HEAP_OBJECT


IActiveScriptProfilerHeapEnum._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        ([], ULONG, 'celt'),
        ([], POINTER(POINTER(PROFILER_HEAP_OBJECT)), 'heapObjects'),
        ([], POINTER(ULONG), 'pceltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetOptionalInfo',
        ([], POINTER(PROFILER_HEAP_OBJECT), 'heapObject'),
        ([], ULONG, 'celt'),
        ([], POINTER(PROFILER_HEAP_OBJECT_OPTIONAL_INFO), 'optionalInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FreeObjectAndOptionalInfo',
        ([], ULONG, 'celt'),
        ([], POINTER(POINTER(PROFILER_HEAP_OBJECT)), 'heapObjects'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNameIdMap',
        ([], POINTER(LPCWSTR), 'pNameList[]'),
        ([], POINTER(UINT), 'pcelt'),
    ),
]


IActiveScriptProfilerControl3._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumHeap',
        ([], POINTER(POINTER(IActiveScriptProfilerHeapEnum)), 'ppEnum'),
    ),
]


class __MIDL___MIDL_itf_activprof_0000_0004_0001(ENUM):
    PROFILER_HEAP_SUMMARY_VERSION_1 = 0x1


PROFILER_HEAP_SUMMARY_VERSION = __MIDL___MIDL_itf_activprof_0000_0004_0001



class _PROFILER_HEAP_SUMMARY(ctypes.Structure):
    _fields_ = [
        ('version', PROFILER_HEAP_SUMMARY_VERSION),
        ('totalHeapSize', UINT),
    ]


PROFILER_HEAP_SUMMARY = _PROFILER_HEAP_SUMMARY


IActiveScriptProfilerControl4._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SummarizeHeap',
        ([], POINTER(PROFILER_HEAP_SUMMARY), 'heapSummary'),
    ),
]


IActiveScriptProfilerControl5._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumHeap2',
        ([], PROFILER_HEAP_ENUM_FLAGS, 'enumFlags'),
        ([], POINTER(POINTER(IActiveScriptProfilerHeapEnum)), 'ppEnum'),
    ),
]


IActiveScriptProfilerCallback._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Initialize',
        ([], DWORD, 'dwContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Shutdown',
        ([], HRESULT, 'hrReason'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ScriptCompiled',
        ([], PROFILER_TOKEN, 'scriptId'),
        ([], PROFILER_SCRIPT_TYPE, 'type'),
        ([], POINTER(comtypes.IUnknown), 'pIDebugDocumentContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FunctionCompiled',
        ([], PROFILER_TOKEN, 'functionId'),
        ([], PROFILER_TOKEN, 'scriptId'),
        ([], POINTER(WCHAR), 'pwszFunctionName'),
        ([], POINTER(WCHAR), 'pwszFunctionNameHINT'),
        ([], POINTER(comtypes.IUnknown), 'pIDebugDocumentContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnFunctionEnter',
        ([], PROFILER_TOKEN, 'scriptId'),
        ([], PROFILER_TOKEN, 'functionId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnFunctionExit',
        ([], PROFILER_TOKEN, 'scriptId'),
        ([], PROFILER_TOKEN, 'functionId'),
    ),
]


IActiveScriptProfilerCallback2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnFunctionEnterByName',
        ([], POINTER(WCHAR), 'pwszFunctionName'),
        ([], PROFILER_SCRIPT_TYPE, 'type'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnFunctionExitByName',
        ([], POINTER(WCHAR), 'pwszFunctionName'),
        ([], PROFILER_SCRIPT_TYPE, 'type'),
    ),
]


IActiveScriptProfilerCallback3._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetWebWorkerId',
        ([], DWORD, 'webWorkerId'),
    ),
]



__all__ = (
    'IActiveScriptProfilerCallback2', 'IActiveScriptProfilerCallback',
    'IActiveScriptProfilerControl5', 'IActiveScriptProfilerControl4',
    'IActiveScriptProfilerControl3', 'IActiveScriptProfilerControl2',
    'IActiveScriptProfilerHeapEnum', 'IActiveScriptProfilerControl',
    'IActiveScriptProfilerCallback3', '__REQUIRED_RPCSAL_H_VERSION__',
    '__REQUIRED_RPCNDR_H_VERSION__', 'PROFILER_HEAP_SUMMARY_VERSION',
    'PROFILER_RELATIONSHIP_INFO', 'PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS',
    '__MIDL___MIDL_itf_activprof_0000_0002_0005', 'PROFILER_SCRIPT_TYPE',
    '__MIDL___MIDL_itf_activprof_0000_0002_0004', 'PROFILER_HEAP_ENUM_FLAGS',
    '__MIDL___MIDL_itf_activprof_0000_0000_0001', 'PROFILER_EVENT_MASK',
    '__MIDL___MIDL_itf_activprof_0000_0002_0001', 'PROFILER_HEAP_SUMMARY',
    '__MIDL___MIDL_itf_activprof_0000_0002_0003', '_PROFILER_HEAP_SUMMARY',
    '__MIDL___MIDL_itf_activprof_0000_0002_0002', '_PROFILER_HEAP_OBJECT',
    'PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE', 'PROFILER_HEAP_OBJECT_FLAGS',
    '__MIDL___MIDL_itf_activprof_0000_0000_0002', 'PROFILER_HEAP_OBJECT',
    '__MIDL___MIDL_itf_activprof_0000_0004_0001', 'PROFILER_HEAP_OBJECT_ID',
    'IID_IActiveScriptProfilerControl3', 'IID_IActiveScriptProfilerHeapEnum',
    '_PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST', 'PROFILER_HEAP_OBJECT_NAME_ID',
    '_PROFILER_HEAP_OBJECT_OPTIONAL_INFO', 'PROFILER_HEAP_OBJECT_SCOPE_LIST',
    'PROFILER_PROPERTY_TYPE_SUBSTRING_INFO', 'PROFILER_TOKEN',
    '_PROFILER_HEAP_OBJECT_RELATIONSHIP', 'PROFILER_HEAP_OBJECT_RELATIONSHIP',
    '_PROFILER_PROPERTY_TYPE_SUBSTRING_INFO',
    'PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST',
    '_PROFILER_HEAP_OBJECT_SCOPE_LIST', 'PROFILER_HEAP_OBJECT_OPTIONAL_INFO',
    'PROFILER_EXTERNAL_OBJECT_ADDRESS',
)
