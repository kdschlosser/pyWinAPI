__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
# from unknwn_h import * # NOQA
from .winapifamily_h import * # NOQA

from .wtypes_h import DWORD, HRESULT
from .guiddef_h import IID
import comtypes


ENDPOINT_FORMAT_RESET_MIX_ONLY = 0x00000001

COMMETHOD = comtypes.COMMETHOD


IID_IAudioEndpointFormatControl = IID(
    '{784CFD40-9F89-456E-A1A6-873B006A664E}'
)


class IAudioEndpointFormatControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpointFormatControl
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'ResetToDefault',
            (['in'], DWORD, 'ResetFlags')
        ),
    ]

__all__ = (
    'ENDPOINT_FORMAT_RESET_MIX_ONLY', 'IID_IAudioEndpointFormatControl',
    'IAudioEndpointFormatControl'
)
