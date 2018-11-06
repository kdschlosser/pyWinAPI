

from wtypes_h import (
    LPCOLESTR,
    DWORD,
    POINTER,
    HRESULT,
    ULONG,
    REFGUID,
    BSTR,
    LONG,
    OLECHAR,
    BOOL,
    WORD
)
from guiddef_h import (
    DEFINE_GUID,
    IID,
)
import ntdef_h
import comtypes


__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
IID_IScriptNode = IID(
    '{0AEE2A94-BCBB-11d0-8C72-00C04FC2B085}'
)


class IScriptNode(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IScriptNode
    _idlflags_ = []


IID_IScriptEntry = IID(
    '{0AEE2A95-BCBB-11d0-8C72-00C04FC2B085}'
)


class IScriptEntry(IScriptNode):
    _case_insensitive_ = True
    _iid_ = IID_IScriptEntry
    _idlflags_ = []


IID_IScriptScriptlet = IID(
    '{0AEE2A96-BCBB-11d0-8C72-00C04FC2B085}'
)


class IScriptScriptlet(IScriptEntry):
    _case_insensitive_ = True
    _iid_ = IID_IScriptScriptlet
    _idlflags_ = []


IID_IActiveScriptAuthor = IID(
    '{9C109DA0-7006-11d1-B36C-00A0C911E8B2}'
)


class IActiveScriptAuthor(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptAuthor
    _idlflags_ = []


IID_IActiveScriptAuthorProcedure = IID(
    '{7E2D4B70-BD9A-11d0-9336-00A0C90DCAA9}'
)


class IActiveScriptAuthorProcedure(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptAuthorProcedure
    _idlflags_ = []


from ocidl_h import * # NOQA
from oaidl_h import ITypeInfo, IDispatch, MEMBERID
from winapifamily_h import * # NOQA
CATID_ActiveScriptAuthor = DEFINE_GUID(
    0xAEE2A92,
    0xBCBB,
    0x11D0,
    0x8C,
    0x72,
    0x0,
    0xC0,
    0x4F,
    0xC2,
    0xB0,
    0x85
)
STATIC_IID_IActiveScriptAuthor = DEFINE_GUID(
    0x9C109DA0,
    0x7006,
    0x11D1,
    0xB3,
    0x6C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0xE8,
    0xB2
)
STATIC_IID_IScriptNode = DEFINE_GUID(
    0xAEE2A94,
    0xBCBB,
    0x11D0,
    0x8C,
    0x72,
    0x0,
    0xC0,
    0x4F,
    0xC2,
    0xB0,
    0x85
)
STATIC_IID_IScriptEntry = DEFINE_GUID(
    0xAEE2A95,
    0xBCBB,
    0x11D0,
    0x8C,
    0x72,
    0x0,
    0xC0,
    0x4F,
    0xC2,
    0xB0,
    0x85
)
STATIC_IID_IScriptScriptlet = DEFINE_GUID(
    0xAEE2A96,
    0xBCBB,
    0x11D0,
    0x8C,
    0x72,
    0x0,
    0xC0,
    0x4F,
    0xC2,
    0xB0,
    0x85
)
STATIC_IID_IActiveScriptAuthorProcedure = DEFINE_GUID(
    0x7E2D4B70,
    0xBD9A,
    0x11D0,
    0x93,
    0x36,
    0x0,
    0xA0,
    0xC9,
    0xD,
    0xCA,
    0xA9
)
SOURCE_TEXT_ATTR = WORD
COMMETHOD = comtypes.COMMETHOD


IScriptNode._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetParent',
        ([], POINTER(POINTER(IScriptNode)), 'ppsnParent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetIndexInParent',
        ([], POINTER(ULONG), 'pisn'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCookie',
        ([], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNumberOfChildren',
        ([], POINTER(ULONG), 'pcsn'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetChild',
        ([], ULONG, 'isn'),
        ([], POINTER(POINTER(IScriptNode)), 'ppsn'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLanguage',
        ([], POINTER(BSTR), 'pbstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateChildEntry',
        ([], ULONG, 'isn'),
        ([], DWORD, 'dwCookie'),
        ([], LPCOLESTR, 'pszDelimiter'),
        ([], POINTER(POINTER(IScriptEntry)), 'ppse'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateChildHandler',
        ([], LPCOLESTR, 'pszDefaultName'),
        ([], POINTER(LPCOLESTR), 'prgpszNames'),
        ([], ULONG, 'cpszNames'),
        ([], LPCOLESTR, 'pszEvent'),
        ([], LPCOLESTR, 'pszDelimiter'),
        ([], POINTER(ITypeInfo), 'ptiSignature'),
        ([], ULONG, 'iMethodSignature'),
        ([], ULONG, 'isn'),
        ([], DWORD, 'dwCookie'),
        ([], POINTER(POINTER(IScriptEntry)), 'ppse'),
    ),
]


IScriptEntry._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetText',
        ([], POINTER(BSTR), 'pbstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetText',
        ([], LPCOLESTR, 'psz'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBody',
        ([], POINTER(BSTR), 'pbstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetBody',
        ([], LPCOLESTR, 'psz'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetName',
        ([], POINTER(BSTR), 'pbstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetName',
        ([], LPCOLESTR, 'psz'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetItemName',
        ([], POINTER(BSTR), 'pbstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetItemName',
        ([], LPCOLESTR, 'psz'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSignature',
        ([], POINTER(POINTER(ITypeInfo)), 'ppti'),
        ([], POINTER(ULONG), 'piMethod'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSignature',
        ([], POINTER(ITypeInfo), 'pti'),
        ([], ULONG, 'iMethod'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRange',
        ([], POINTER(ULONG), 'pichMin'),
        ([], POINTER(ULONG), 'pcch'),
    ),
]


IScriptScriptlet._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetSubItemName',
        ([], POINTER(BSTR), 'pbstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSubItemName',
        ([], LPCOLESTR, 'psz'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetEventName',
        ([], POINTER(BSTR), 'pbstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetEventName',
        ([], LPCOLESTR, 'psz'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSimpleEventName',
        ([], POINTER(BSTR), 'pbstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSimpleEventName',
        ([], LPCOLESTR, 'psz'),
    ),
]


IActiveScriptAuthor._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AddNamedItem',
        ([], LPCOLESTR, 'pszName'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(IDispatch), 'pdisp'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddScriptlet',
        ([], LPCOLESTR, 'pszDefaultName'),
        ([], LPCOLESTR, 'pszCode'),
        ([], LPCOLESTR, 'pszItemName'),
        ([], LPCOLESTR, 'pszSubItemName'),
        ([], LPCOLESTR, 'pszEventName'),
        ([], LPCOLESTR, 'pszDelimiter'),
        ([], DWORD, 'dwCookie'),
        ([], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ParseScriptText',
        ([], LPCOLESTR, 'pszCode'),
        ([], LPCOLESTR, 'pszItemName'),
        ([], LPCOLESTR, 'pszDelimiter'),
        ([], DWORD, 'dwCookie'),
        ([], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptTextAttributes',
        ([], LPCOLESTR, 'pszCode'),
        ([], ULONG, 'cch'),
        ([], LPCOLESTR, 'pszDelimiter'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(SOURCE_TEXT_ATTR), 'pattr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptletTextAttributes',
        ([], LPCOLESTR, 'pszCode'),
        ([], ULONG, 'cch'),
        ([], LPCOLESTR, 'pszDelimiter'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(SOURCE_TEXT_ATTR), 'pattr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRoot',
        ([], POINTER(POINTER(IScriptNode)), 'ppsp'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLanguageFlags',
        ([], POINTER(DWORD), 'pgrfasa'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetEventHandler',
        ([], POINTER(IDispatch), 'pdisp'),
        ([], LPCOLESTR, 'pszItem'),
        ([], LPCOLESTR, 'pszSubItem'),
        ([], LPCOLESTR, 'pszEvent'),
        ([], POINTER(POINTER(IScriptEntry)), 'ppse'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveNamedItem',
        ([], LPCOLESTR, 'pszName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddTypeLib',
        ([], REFGUID, 'rguidTypeLib'),
        ([], DWORD, 'dwMajor'),
        ([], DWORD, 'dwMinor'),
        ([], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveTypeLib',
        ([], REFGUID, 'rguidTypeLib'),
        ([], DWORD, 'dwMajor'),
        ([], DWORD, 'dwMinor'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetChars',
        ([], DWORD, 'fRequestedList'),
        ([], POINTER(BSTR), 'pbstrChars'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetInfoFromContext',
        ([], LPCOLESTR, 'pszCode'),
        ([], ULONG, 'cchCode'),
        ([], ULONG, 'ichCurrentPosition'),
        ([], DWORD, 'dwListTypesRequested'),
        ([], POINTER(DWORD), 'pdwListTypesProvided'),
        ([], POINTER(ULONG), 'pichListAnchorPosition'),
        ([], POINTER(ULONG), 'pichFuncAnchorPosition'),
        ([], POINTER(MEMBERID), 'pmemid'),
        ([], POINTER(LONG), 'piCurrentParameter'),
        ([], POINTER(POINTER(comtypes.IUnknown)), 'ppunk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsCommitChar',
        ([], OLECHAR, 'ch'),
        ([], POINTER(BOOL), 'pfcommit'),
    ),
]


IActiveScriptAuthorProcedure._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ParseProcedureText',
        ([], LPCOLESTR, 'pszCode'),
        ([], LPCOLESTR, 'pszFormalParams'),
        ([], LPCOLESTR, 'pszProcedureName'),
        ([], LPCOLESTR, 'pszItemName'),
        ([], LPCOLESTR, 'pszDelimiter'),
        ([], DWORD, 'dwCookie'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(IDispatch), 'pdispFor'),
    ),
]



__all__ = (
    'IScriptScriptlet', 'IScriptEntry', 'IScriptNode', 'IActiveScriptAuthor',
    'IActiveScriptAuthorProcedure', '__REQUIRED_RPCSAL_H_VERSION__',
    '__REQUIRED_RPCNDR_H_VERSION__', 'IID_IScriptEntry', 'IID_IScriptNode',
    'CATID_ActiveScriptAuthor', 'IID_IActiveScriptAuthorProcedure',
    'IID_IActiveScriptAuthor', 'IID_IScriptScriptlet', 'SOURCE_TEXT_ATTR',
)
