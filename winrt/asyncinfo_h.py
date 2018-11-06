

from wtypes_h import (
    ENUM,
    POINTER,
    HRESULT,
    INT32
)
from guiddef_h import (
    IID,
)
import comtypes


__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064

IID_IAsyncInfo = IID(
    '{00000036-0000-0000-C000-000000000046}'
)

from inspectable_h import * # NOQA


class IAsyncInfo(IInspectable):
    _case_insensitive_ = True
    _iid_ = IID_IAsyncInfo
    _idlflags_ = []


class AsyncStatus(ENUM):
    Started = 0
    Completed = 1
    Canceled = 2
    Error = 3


COMMETHOD = comtypes.COMMETHOD


IAsyncInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_Id',
        (['out', 'retval'], POINTER(INT32), 'id'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Status',
        (['out', 'retval'], POINTER(AsyncStatus), 'status'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_ErrorCode',
        (['out', 'retval'], POINTER(HRESULT), 'errorCode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Close'
    ),
]

__all__ = (
    'IAsyncInfo', '__REQUIRED_RPCSAL_H_VERSION__', '', 'AsyncStatus',
    '__REQUIRED_RPCNDR_H_VERSION__',
)
