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
    REFIID,
    VOID,
    LPWSTR,
    ULONG,
    PROPERTYKEY,
)
from .guiddef_h import (
    IID,
)
from .objidl_h import (
    IPersistStream
)

import comtypes


IID_IRichChunk = IID(
    '{4FDEF69C-DBC9-454e-9910-B34F3C64B510}'
)


class IRichChunk(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRichChunk
    _idlflags_ = []


IID_ICondition = IID(
    '{0FC988D4-C935-4b97-A973-46282EA175C8}'
)


class ICondition(IPersistStream):
    _case_insensitive_ = True
    _iid_ = IID_ICondition
    _idlflags_ = []


from .oaidl_h import *
# from .ocidl_h import *
from .propidl_h import *
from .winapifamily_h import *


class tagCONDITION_TYPE(ENUM):
    CT_AND_CONDITION = 0
    CT_OR_CONDITION = CT_AND_CONDITION + 1
    CT_NOT_CONDITION = CT_OR_CONDITION + 1
    CT_LEAF_CONDITION = CT_NOT_CONDITION + 1


CONDITION_TYPE = tagCONDITION_TYPE


class tagCONDITION_OPERATION(ENUM):
    COP_IMPLICIT = 0
    COP_EQUAL = COP_IMPLICIT + 1
    COP_NOTEQUAL = COP_EQUAL + 1
    COP_LESSTHAN = COP_NOTEQUAL + 1
    COP_GREATERTHAN = COP_LESSTHAN + 1
    COP_LESSTHANOREQUAL = COP_GREATERTHAN + 1
    COP_GREATERTHANOREQUAL = COP_LESSTHANOREQUAL + 1
    COP_VALUE_STARTSWITH = COP_GREATERTHANOREQUAL + 1
    COP_VALUE_ENDSWITH = COP_VALUE_STARTSWITH + 1
    COP_VALUE_CONTAINS = COP_VALUE_ENDSWITH + 1
    COP_VALUE_NOTCONTAINS = COP_VALUE_CONTAINS + 1
    COP_DOSWILDCARDS = COP_VALUE_NOTCONTAINS + 1
    COP_WORD_EQUAL = COP_DOSWILDCARDS + 1
    COP_WORD_STARTSWITH = COP_WORD_EQUAL + 1
    COP_APPLICATION_SPECIFIC = COP_WORD_STARTSWITH + 1


CONDITION_OPERATION = tagCONDITION_OPERATION


COMMETHOD = comtypes.COMMETHOD


IRichChunk._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetData',
        (['out'], POINTER(ULONG), 'pFirstPos'),
        (['out'], POINTER(ULONG), 'pLength'),
        (['out'], POINTER(LPWSTR), 'ppsz'),
        (['out'], POINTER(PROPVARIANT), 'pValue'),
    ),
]


ICondition._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetConditionType',
        (['out', 'retval'], POINTER(CONDITION_TYPE), 'pNodeType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSubConditions',
        (['in'], REFIID, 'riid'),
        (['out', 'retval'], POINTER(POINTER(VOID)), 'ppv'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetComparisonInfo',
        (['out'], POINTER(LPWSTR), 'ppszPropertyName'),
        (['out'], POINTER(CONDITION_OPERATION), 'pcop'),
        (['out'], POINTER(PROPVARIANT), 'ppropvar'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetValueType',
        (['out', 'retval'], POINTER(LPWSTR), 'ppszValueTypeName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetValueNormalization',
        (['out', 'retval'], POINTER(LPWSTR), 'ppszNormalization'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetInputTerms',
        (['out'], POINTER(POINTER(IRichChunk)), 'ppPropertyTerm'),
        (['out'], POINTER(POINTER(IRichChunk)), 'ppOperationTerm'),
        (['out'], POINTER(POINTER(IRichChunk)), 'ppValueTerm'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out', 'retval'], POINTER(POINTER(ICondition)), 'ppc'),
    ),
]


IID_ICondition2 = IID(
    '{0DB8851D-2E5B-47eb-9208-D28C325A01D7}'
)


class ICondition2(ICondition):
    _case_insensitive_ = True
    _iid_ = IID_ICondition2
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetLocale',
            (['out'], POINTER(LPWSTR), 'ppszLocaleName'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetLeafConditionInfo',
            (['out'], POINTER(PROPERTYKEY), 'ppropkey'),
            (['out'], POINTER(CONDITION_OPERATION), 'pcop'),
            (['out'], POINTER(PROPVARIANT), 'ppropvar'),
        ),
    ]


__all__ = (
    'IRichChunk', 'ICondition2', 'ICondition', 'CONDITION_OPERATION',
    '__REQUIRED_RPCSAL_H_VERSION__', '__REQUIRED_RPCNDR_H_VERSION__',
    'tagCONDITION_TYPE', 'CONDITION_TYPE', 'tagCONDITION_OPERATION',
)
