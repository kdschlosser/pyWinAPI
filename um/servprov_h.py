__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import * # NOQA
# from .rpcndr_h import * # NOQA
# from .windows_h import * # NOQA
# from .ole2_h import * # NOQA

from .wtypes_h import (
    POINTER,
    HRESULT,
    VOID,
)
from .guiddef_h import (
    REFGUID,
    REFIID,
    IID
)

import comtypes


IID_IServiceProvider = IID(
    '{6d5140c1-7436-11ce-8034-00aa006009fa}'
)


class IServiceProvider(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IServiceProvider
    _idlflags_ = []


from .objidl_h import * # NOQA
from .winapifamily_h import * # NOQA

LPSERVICEPROVIDER = POINTER(IServiceProvider)
COMMETHOD = comtypes.COMMETHOD


IServiceProvider._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryService',
        (['in'], REFGUID, 'guidService'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvObject'),
    ),
]


__all__ = (
    'IServiceProvider', '__REQUIRED_RPCSAL_H_VERSION__', 'LPSERVICEPROVIDER',
    '__REQUIRED_RPCNDR_H_VERSION__',
)
