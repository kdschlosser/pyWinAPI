
__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA

from shared.guiddef_h import (
    IID,
    REFIID
)
import comtypes
from shared.wtypes_h import (
    VOID,
    HWND,
    HRESULT,
    POINTER

)

from winrt.inspectable_h import * # NOQA
from winrt.asyncinfo_h import * # NOQA
from shared.winapifamily_h import * # NOQA


IID_IAccountsSettingsPaneInterop = IID(
    '{D3EE12AD-3865-4362-9746-B75A682DF0E6}'
)


class IAccountsSettingsPaneInterop(IInspectable):
    _case_insensitive_ = True
    _iid_ = IID_IAccountsSettingsPaneInterop
    _idlflags_ = []


COMMETHOD = comtypes.COMMETHOD


IAccountsSettingsPaneInterop._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetForWindow',
        (['in'], HWND, 'appWindow'),
        (['in'], REFIID, 'riid'),
        (['retval', 'out'], POINTER(POINTER(VOID)), 'accountsSettingsPane'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ShowManageAccountsForWindowAsync',
        (['in'], HWND, 'appWindow'),
        (['in'], REFIID, 'riid'),
        (['retval', 'out'], POINTER(POINTER(VOID)), 'asyncAction'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ShowAddAccountForWindowAsync',
        (['in'], HWND, 'appWindow'),
        (['in'], REFIID, 'riid'),
        (['retval', 'out'], POINTER(POINTER(VOID)), 'asyncAction'),
    ),
]


__all__ = (
    'IAccountsSettingsPaneInterop', '__REQUIRED_RPCSAL_H_VERSION__',
    '__REQUIRED_RPCNDR_H_VERSION__',
)
