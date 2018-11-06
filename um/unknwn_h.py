__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import * # NOQA
# from .rpcndr_h import * # NOQA
# from .windows_h import * # NOQA
# from .ole2_h import * # NOQA
from .winapifamily_h import * # NOQA


from .wtypes_h import (
    REFIID,
    VOID,
    POINTER,
    HRESULT,
    ULONG,
    BOOL,
)
from .guiddef_h import (
    IID,
)
import comtypes


IID_AsyncIUnknown = IID(
    '{000e0000-0000-0000-C000-000000000046}'
)


class AsyncIUnknown(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_AsyncIUnknown
    _idlflags_ = []


IID_IClassFactory = IID(
    '{00000001-0000-0000-C000-000000000046}'
)


class IClassFactory(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IClassFactory
    _idlflags_ = []


IUnknown = comtypes.IUnknown
LPUNKNOWN = POINTER(IUnknown)


COMMETHOD = comtypes.COMMETHOD

AsyncIUnknown._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Begin_QueryInterface',
        (['in'], REFIID, 'riid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Finish_QueryInterface',
        (['out'], POINTER(POINTER(VOID)), 'ppvObject'),
    ),
    COMMETHOD(
        [],
        ULONG,
        'Finish_Release'
    ),
]


LPCLASSFACTORY = POINTER(IClassFactory)


IClassFactory._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateInstance',
        (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'LockServer',
        (['in'], BOOL, 'fLock'),
    ),
]


__all__ = (
    'AsyncIUnknown', 'IClassFactory', 'LPCLASSFACTORY', 'IUnknown',
    '__REQUIRED_RPCSAL_H_VERSION__', '__REQUIRED_RPCNDR_H_VERSION__',
    'LPUNKNOWN',
)
