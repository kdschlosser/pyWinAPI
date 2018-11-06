__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import *
# from .rpcndr_h import *
# from .windows_h import *
# from .ole2_h import *
from .oleidl_h import *
from .oaidl_h import *
from .servprov_h import *
from .winapifamily_h import *


from .unknwn_h import (
    IClassFactory,
)

from .objidl_h import (
    IPersist,
    IAdviseSink,
    LPSTREAM,
    DVTARGETDEVICE,
)

from .wtypes_h import (
    ENUM,
    HRESULT,
    ULONG,
    POINTER,
    LPCOLESTR,
    DWORD,
    LPCRECT,
    LONG,
    BOOL,
    SHORT,
    HDC,
    LPSIZEL,
    LCID,
    MSG,
    POINTL,
    VOID,
    LPRECTL,
    POINT,
    BSTR,
    CLSID,
    HRGN,
    INT,
    LPRECT,
    UINT,
    WPARAM,
    LPARAM,
    LRESULT,
    HWND,
    REFIID,
    PVOID,
    LPVOID,
    CY,
    HFONT,
    ULARGE_INTEGER,
    VARTYPE,
    CLIPFORMAT,
    LPOLESTR,
    SIZEL,
    HACCEL,
    USHORT,
    FLOAT,
    SIZE,
    HPALETTE,
    UINT_PTR,
    TEXTMETRICW,
)
from .guiddef_h import (
    IID,
    GUID,
)
from .oaidl_h import VARIANT
import ctypes
import comtypes


IID_IEnumConnections = IID(
    '{B196B287-BAB4-101A-B69C-00AA00341D07}'
)


class IEnumConnections(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumConnections
    _idlflags_ = []


IID_IConnectionPoint = IID(
    '{B196B286-BAB4-101A-B69C-00AA00341D07}'
)


class IConnectionPoint(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IConnectionPoint
    _idlflags_ = []


IID_IEnumConnectionPoints = IID(
    '{B196B285-BAB4-101A-B69C-00AA00341D07}'
)


class IEnumConnectionPoints(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumConnectionPoints
    _idlflags_ = []


IID_IConnectionPointContainer = IID(
    '{B196B284-BAB4-101A-B69C-00AA00341D07}'
)


class IConnectionPointContainer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IConnectionPointContainer
    _idlflags_ = []


IID_IProvideClassInfo = IID(
    '{B196B283-BAB4-101A-B69C-00AA00341D07}'
)


class IProvideClassInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IProvideClassInfo
    _idlflags_ = []


IID_IProvideClassInfo2 = IID(
    '{A6BC3AC0-DBAA-11CE-9DE3-00AA004BB851}'
)


class IProvideClassInfo2(IProvideClassInfo):
    _case_insensitive_ = True
    _iid_ = IID_IProvideClassInfo2
    _idlflags_ = []


IID_IProvideMultipleClassInfo = IID(
    '{A7ABA9C1-8983-11cf-8F20-00805F2CD064}'
)


class IProvideMultipleClassInfo(IProvideClassInfo2):
    _case_insensitive_ = True
    _iid_ = IID_IProvideMultipleClassInfo
    _idlflags_ = []


IID_IOleControl = IID(
    '{B196B288-BAB4-101A-B69C-00AA00341D07}'
)


class IOleControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOleControl
    _idlflags_ = []


IID_IOleControlSite = IID(
    '{B196B289-BAB4-101A-B69C-00AA00341D07}'
)


class IOleControlSite(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOleControlSite
    _idlflags_ = []


IID_IPropertyPage = IID(
    '{B196B28D-BAB4-101A-B69C-00AA00341D07}'
)


class IPropertyPage(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyPage
    _idlflags_ = []


IID_IPropertyPage2 = IID(
    '{01E44665-24AC-101B-84ED-08002B2EC713}'
)


class IPropertyPage2(IPropertyPage):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyPage2
    _idlflags_ = []


IID_IPropertyPageSite = IID(
    '{B196B28C-BAB4-101A-B69C-00AA00341D07}'
)


class IPropertyPageSite(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyPageSite
    _idlflags_ = []


IID_IPropertyNotifySink = IID(
    '{9BFBBC02-EFF1-101A-84ED-00AA00341D07}'
)


class IPropertyNotifySink(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyNotifySink
    _idlflags_ = []


IID_ISpecifyPropertyPages = IID(
    '{B196B28B-BAB4-101A-B69C-00AA00341D07}'
)


class ISpecifyPropertyPages(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISpecifyPropertyPages
    _idlflags_ = []


IID_IPersistMemory = IID(
    '{BD1AE5E0-A6AE-11CE-BD37-504200C10000}'
)


class IPersistMemory(IPersist):
    _case_insensitive_ = True
    _iid_ = IID_IPersistMemory
    _idlflags_ = []


IID_IPersistStreamInit = IID(
    '{7FD52380-4E07-101B-AE2D-08002B2EC713}'
)


class IPersistStreamInit(IPersist):
    _case_insensitive_ = True
    _iid_ = IID_IPersistStreamInit
    _idlflags_ = []


IID_IPersistPropertyBag = IID(
    '{37D84F60-42CB-11CE-8135-00AA004BB851}'
)


class IPersistPropertyBag(IPersist):
    _case_insensitive_ = True
    _iid_ = IID_IPersistPropertyBag
    _idlflags_ = []


IID_ISimpleFrameSite = IID(
    '{742B0E01-14E6-101B-914E-00AA00300CAB}'
)


class ISimpleFrameSite(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISimpleFrameSite
    _idlflags_ = []


IID_IFont = IID(
    '{BEF6E002-A874-101A-8BBA-00AA00300CAB}'
)


class IFont(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IFont
    _idlflags_ = []


IID_IPicture = IID(
    '{7BF80980-BF32-101A-8BBB-00AA00300CAB}'
)


class IPicture(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPicture
    _idlflags_ = []


IID_IPicture2 = IID(
    '{F5185DD8-2012-4b0b-AAD9-F052C6BD482B}'
)


class IPicture2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPicture2
    _idlflags_ = []


IID_IFontEventsDisp = IID(
    '{4EF6100A-AF88-11D0-9846-00C04FC29993}'
)


class IFontEventsDisp(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID_IFontEventsDisp
    _idlflags_ = []


IID_IFontDisp = IID(
    '{BEF6E003-A874-101A-8BBA-00AA00300CAB}'
)


class IFontDisp(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID_IFontDisp
    _idlflags_ = []


IID_IPictureDisp = IID(
    '{7BF80981-BF32-101A-8BBB-00AA00300CAB}'
)


class IPictureDisp(IDispatch):
    _case_insensitive_ = True
    _iid_ = IID_IPictureDisp
    _idlflags_ = []


IID_IOleInPlaceObjectWindowless = IID(
    '{1C2056CC-5EF4-101B-8BC8-00AA003E3B29}'
)


class IOleInPlaceObjectWindowless(IOleInPlaceObject):
    _case_insensitive_ = True
    _iid_ = IID_IOleInPlaceObjectWindowless
    _idlflags_ = []


IID_IOleInPlaceSiteEx = IID(
    '{9C2CAD80-3424-11CF-B670-00AA004CD6D8}'
)


class IOleInPlaceSiteEx(IOleInPlaceSite):
    _case_insensitive_ = True
    _iid_ = IID_IOleInPlaceSiteEx
    _idlflags_ = []


IID_IOleInPlaceSiteWindowless = IID(
    '{922EADA0-3424-11CF-B670-00AA004CD6D8}'
)


class IOleInPlaceSiteWindowless(IOleInPlaceSiteEx):
    _case_insensitive_ = True
    _iid_ = IID_IOleInPlaceSiteWindowless
    _idlflags_ = []


IID_IViewObjectEx = IID(
    '{3AF24292-0C96-11CE-A0CF-00AA00600AB8}'
)


class IViewObjectEx(IViewObject2):
    _case_insensitive_ = True
    _iid_ = IID_IViewObjectEx
    _idlflags_ = []


IID_IOleUndoUnit = IID(
    '{894AD3B0-EF97-11CE-9BC9-00AA00608E01}'
)


class IOleUndoUnit(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOleUndoUnit
    _idlflags_ = []


IID_IOleParentUndoUnit = IID(
    '{A1FAF330-EF97-11CE-9BC9-00AA00608E01}'
)


class IOleParentUndoUnit(IOleUndoUnit):
    _case_insensitive_ = True
    _iid_ = IID_IOleParentUndoUnit
    _idlflags_ = []


IID_IEnumOleUndoUnits = IID(
    '{B3E7C340-EF97-11CE-9BC9-00AA00608E01}'
)


class IEnumOleUndoUnits(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumOleUndoUnits
    _idlflags_ = []


IID_IOleUndoManager = IID(
    '{D001F200-EF97-11CE-9BC9-00AA00608E01}'
)


class IOleUndoManager(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOleUndoManager
    _idlflags_ = []


IID_IPointerInactive = IID(
    '{55980BA0-35AA-11CF-B671-00AA004CD6D8}'
)


class IPointerInactive(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPointerInactive
    _idlflags_ = []


IID_IObjectWithSite = IID(
    '{FC4801A3-2BA9-11CF-A229-00AA003D7352}'
)


class IObjectWithSite(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IObjectWithSite
    _idlflags_ = []


IID_IPerPropertyBrowsing = IID(
    '{376BD3AA-3845-101B-84ED-08002B2EC713}'
)


class IPerPropertyBrowsing(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPerPropertyBrowsing
    _idlflags_ = []


IID_IPropertyBag2 = IID(
    '{22F55882-280B-11d0-A8A9-00A0C90C2004}'
)


class IPropertyBag2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPropertyBag2
    _idlflags_ = []


IID_IPersistPropertyBag2 = IID(
    '{22F55881-280B-11d0-A8A9-00A0C90C2004}'
)


class IPersistPropertyBag2(IPersist):
    _case_insensitive_ = True
    _iid_ = IID_IPersistPropertyBag2
    _idlflags_ = []



IID_IAdviseSinkEx = IID(
    '{3AF24290-0C96-11CE-A0CF-00AA00600AB8}'
)


class IAdviseSinkEx(IAdviseSink):
    _case_insensitive_ = True
    _iid_ = IID_IAdviseSinkEx
    _idlflags_ = []


IID_IQuickActivate = IID(
    '{CF51ED10-62FE-11CF-BF86-00A0C9034836}'
)


class IQuickActivate(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IQuickActivate
    _idlflags_ = []


IID_IClassFactory2 = IID(
    '{B196B28F-BAB4-101A-B69C-00AA00341D07}'
)


class IClassFactory2(IClassFactory):
    _case_insensitive_ = True
    _iid_ = IID_IClassFactory2
    _idlflags_ = []


class tagUASFLAGS(ENUM):
    UAS_NORMAL = 0
    UAS_BLOCKED = 0x1
    UAS_NOPARENTENABLE = 0x2
    UAS_MASK = 0x3


UASFLAGS = tagUASFLAGS


class tagREADYSTATE(ENUM):
    READYSTATE_UNINITIALIZED = 0
    READYSTATE_LOADING = 1
    READYSTATE_LOADED = 2
    READYSTATE_INTERACTIVE = 3
    READYSTATE_COMPLETE = 4


READYSTATE = tagREADYSTATE


PENUMCONNECTIONS = POINTER(IEnumConnections)
LPENUMCONNECTIONS = POINTER(IEnumConnections)


class tagCONNECTDATA(ctypes.Structure):
    _fields_ = [
        ('pUnk', POINTER(comtypes.IUnknown)),
        ('dwCookie', DWORD),
    ]


CONNECTDATA = tagCONNECTDATA
PCONNECTDATA = POINTER(tagCONNECTDATA)
LPCONNECTDATA = POINTER(tagCONNECTDATA)


COMMETHOD = comtypes.COMMETHOD


IEnumConnections._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'cConnections'),
        (['out'], LPCONNECTDATA, 'rgcd'),
        (['out'], POINTER(ULONG), 'pcFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'cConnections'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumConnections)), 'ppEnum'),
    ),
]


PCONNECTIONPOINT = POINTER(IConnectionPoint)
LPCONNECTIONPOINT = POINTER(IConnectionPoint)


IConnectionPoint._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetConnectionInterface',
        (['out'], POINTER(IID), 'pIID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetConnectionPointContainer',
        (['out'], POINTER(POINTER(IConnectionPointContainer)), 'ppCPC'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Advise',
        (['in'], POINTER(comtypes.IUnknown), 'pUnkSink'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Unadvise',
        (['in'], DWORD, 'dwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumConnections',
        (['out'], POINTER(POINTER(IEnumConnections)), 'ppEnum'),
    ),
]


PENUMCONNECTIONPOINTS = POINTER(IEnumConnectionPoints)
LPENUMCONNECTIONPOINTS = POINTER(IEnumConnectionPoints)


IEnumConnectionPoints._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'cConnections'),
        (['out'], POINTER(LPCONNECTIONPOINT), 'ppCP'),
        (['out'], POINTER(ULONG), 'pcFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'cConnections'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumConnectionPoints)), 'ppEnum'),
    ),
]


PCONNECTIONPOINTCONTAINER = POINTER(IConnectionPointContainer)
LPCONNECTIONPOINTCONTAINER = POINTER(IConnectionPointContainer)


IConnectionPointContainer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumConnectionPoints',
        (['out'], POINTER(POINTER(IEnumConnectionPoints)), 'ppEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FindConnectionPoint',
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(IConnectionPoint)), 'ppCP'),
    ),
]


LPCLASSFACTORY2 = POINTER(IClassFactory2)


class tagLICINFO(ctypes.Structure):
    _fields_ = [
        ('cbLicInfo', LONG),
        ('fRuntimeKeyAvail', BOOL),
        ('fLicVerified', BOOL),
    ]


LICINFO = tagLICINFO
LPLICINFO = POINTER(tagLICINFO)


IClassFactory2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetLicInfo',
        (['in', 'out'], POINTER(LICINFO), 'pLicInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RequestLicKey',
        (['in'], DWORD, 'dwReserved'),
        (['out'], POINTER(BSTR), 'pBstrKey'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateInstanceLic',
        (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
        (['in'], POINTER(comtypes.IUnknown), 'pUnkReserved'),
        (['in'], REFIID, 'riid'),
        (['in'], BSTR, 'bstrKey'),
        (['out'], POINTER(PVOID), 'ppvObj'),
    ),
]


LPPROVIDECLASSINFO = POINTER(IProvideClassInfo)


IProvideClassInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetClassInfo',
        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTI'),
    ),
]


LPPROVIDECLASSINFO2 = POINTER(IProvideClassInfo2)


class tagGUIDKIND(ENUM):
    GUIDKIND_DEFAULT_SOURCE_DISP_IID = 1


GUIDKIND = tagGUIDKIND


IProvideClassInfo2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetGUID',
        (['in'], DWORD, 'dwGuidKind'),
        (['out'], POINTER(GUID), 'pGUID'),
    ),
]


MULTICLASSINFO_GETTYPEINFO = 0x00000001
MULTICLASSINFO_GETNUMRESERVEDDISPIDS = 0x00000002
MULTICLASSINFO_GETIIDPRIMARY = 0x00000004
MULTICLASSINFO_GETIIDSOURCE = 0x00000008
TIFLAGS_EXTENDDISPATCHONLY = 0x00000001

LPPROVIDEMULTIPLECLASSINFO = POINTER(IProvideMultipleClassInfo)


IProvideMultipleClassInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetMultiTypeInfoCount',
        (['out'], POINTER(ULONG), 'pcti'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetInfoOfIndex',
        (['in'], ULONG, 'iti'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(ITypeInfo)), 'pptiCoClass'),
        (['out'], POINTER(DWORD), 'pdwTIFlags'),
        (['out'], POINTER(ULONG), 'pcdispidReserved'),
        (['out'], POINTER(IID), 'piidPrimary'),
        (['out'], POINTER(IID), 'piidSource'),
    ),
]


LPOLECONTROL = POINTER(IOleControl)


class tagCONTROLINFO(ctypes.Structure):
    _fields_ = [
        ('cb', ULONG),
        ('hAccel', HACCEL),
        ('cAccel', USHORT),
        ('dwFlags', DWORD),
    ]


CONTROLINFO = tagCONTROLINFO
LPCONTROLINFO = POINTER(tagCONTROLINFO)


class tagCTRLINFO(ENUM):
    CTRLINFO_EATS_RETURN = 1
    CTRLINFO_EATS_ESCAPE = 2


CTRLINFO = tagCTRLINFO


IOleControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetControlInfo',
        (['in', 'out'], POINTER(CONTROLINFO), 'pCI'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnMnemonic',
        (['in'], POINTER(MSG), 'pMsg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnAmbientPropertyChange',
        (['in'], DISPID, 'dispID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FreezeEvents',
        (['in'], BOOL, 'bFreeze'),
    ),
]


LPOLECONTROLSITE = POINTER(IOleControlSite)


class tagPOINTF(ctypes.Structure):
    _fields_ = [
        ('x', FLOAT),
        ('y', FLOAT),
    ]


POINTF = tagPOINTF


LPPOINTF = POINTER(tagPOINTF)


class tagXFORMCOORDS(ENUM):
    XFORMCOORDS_POSITION = 0x1
    XFORMCOORDS_SIZE = 0x2
    XFORMCOORDS_HIMETRICTOCONTAINER = 0x4
    XFORMCOORDS_CONTAINERTOHIMETRIC = 0x8
    XFORMCOORDS_EVENTCOMPAT = 0x10


XFORMCOORDS = tagXFORMCOORDS


IOleControlSite._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'LockInPlaceActive',
        (['in'], BOOL, 'fLock'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetExtendedControl',
        (['out'], POINTER(POINTER(IDispatch)), 'ppDisp'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'TransformCoords',
        (['in', 'out'], POINTER(POINTL), 'pPtlHimetric'),
        (['in', 'out'], POINTER(POINTF), 'pPtfContainer'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'TranslateAccelerator',
        (['in'], POINTER(MSG), 'pMsg'),
        (['in'], DWORD, 'grfModifiers'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnFocus',
        (['in'], BOOL, 'fGotFocus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ShowPropertyFrame'
    ),
]


LPPROPERTYPAGE = POINTER(IPropertyPage)


class tagPROPPAGEINFO(ctypes.Structure):
    _fields_ = [
        ('cb', ULONG),
        ('pszTitle', LPOLESTR),
        ('size', SIZE),
        ('pszDocString', LPOLESTR),
        ('pszHelpFile', LPOLESTR),
        ('dwHelpContext', DWORD),
    ]


PROPPAGEINFO = tagPROPPAGEINFO
LPPROPPAGEINFO = POINTER(tagPROPPAGEINFO)


IPropertyPage._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetPageSite',
        (['in'], POINTER(IPropertyPageSite), 'pPageSite'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Activate',
        (['in'], HWND, 'hWndParent'),
        (['in'], LPCRECT, 'pRect'),
        (['in'], BOOL, 'bModal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPageInfo',
        (['out'], POINTER(PROPPAGEINFO), 'pPageInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetObjects',
        (['in'], ULONG, 'cObjects'),
        (['in'], POINTER(POINTER(comtypes.IUnknown)), 'ppUnk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Show',
        (['in'], UINT, 'nCmdShow'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Move',
        (['in'], LPCRECT, 'pRect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Help',
        (['in'], LPCOLESTR, 'pszHelpDir'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'TranslateAccelerator',
        (['in'], POINTER(MSG), 'pMsg'),
    ),
]


LPPROPERTYPAGE2 = POINTER(IPropertyPage2)

IPropertyPage2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EditProperty',
        (['in'], DISPID, 'dispID'),
    ),
]


LPPROPERTYPAGESITE = POINTER(IPropertyPageSite)


class tagPROPPAGESTATUS(ENUM):
    PROPPAGESTATUS_DIRTY = 0x1
    PROPPAGESTATUS_VALIDATE = 0x2
    PROPPAGESTATUS_CLEAN = 0x4


PROPPAGESTATUS = tagPROPPAGESTATUS


IPropertyPageSite._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnStatusChange',
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLocaleID',
        (['out'], POINTER(LCID), 'pLocaleID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPageContainer',
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppUnk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'TranslateAccelerator',
        (['in'], POINTER(MSG), 'pMsg'),
    ),
]


LPPROPERTYNOTIFYSINK = POINTER(IPropertyNotifySink)


IPropertyNotifySink._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnChanged',
        (['in'], DISPID, 'dispID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnRequestEdit',
        (['in'], DISPID, 'dispID'),
    ),
]


LPSPECIFYPROPERTYPAGES = POINTER(ISpecifyPropertyPages)


class tagCAUUID(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(GUID)),
    ]


CAUUID = tagCAUUID
LPCAUUID = POINTER(tagCAUUID)


ISpecifyPropertyPages._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetPages',
        (['out'], POINTER(CAUUID), 'pPages'),
    ),
]


LPPERSISTMEMORY = POINTER(IPersistMemory)


IPersistMemory._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Load',
        (['in'], LPVOID, 'pMem'),
        (['in'], ULONG, 'cbSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Save',
        (['out'], LPVOID, 'pMem'),
        (['in'], BOOL, 'fClearDirty'),
        (['in'], ULONG, 'cbSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSizeMax',
        (['out'], POINTER(ULONG), 'pCbSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'InitNew'
    ),
]


LPPERSISTSTREAMINIT = POINTER(IPersistStreamInit)


IPersistStreamInit._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Load',
        (['in'], LPSTREAM, 'pStm'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Save',
        (['in'], LPSTREAM, 'pStm'),
        (['in'], BOOL, 'fClearDirty'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSizeMax',
        (['out'], POINTER(ULARGE_INTEGER), 'pCbSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'InitNew'
    ),
]


LPPERSISTPROPERTYBAG = POINTER(IPersistPropertyBag)


IPersistPropertyBag._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Load',
        (['in'], POINTER(IPropertyBag), 'pPropBag'),
        (['in'], POINTER(IErrorLog), 'pErrorLog'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Save',
        (['in'], POINTER(IPropertyBag), 'pPropBag'),
        (['in'], BOOL, 'fClearDirty'),
        (['in'], BOOL, 'fSaveAllProperties'),
    ),
]


LPSIMPLEFRAMESITE = POINTER(ISimpleFrameSite)


ISimpleFrameSite._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'PreMessageFilter',
        (['in'], HWND, 'hWnd'),
        (['in'], UINT, 'msg'),
        (['in'], WPARAM, 'wp'),
        (['in'], LPARAM, 'lp'),
        (['out'], POINTER(LRESULT), 'plResult'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PostMessageFilter',
        (['in'], HWND, 'hWnd'),
        (['in'], UINT, 'msg'),
        (['in'], WPARAM, 'wp'),
        (['in'], LPARAM, 'lp'),
        (['out'], POINTER(LRESULT), 'plResult'),
        (['in'], DWORD, 'dwCookie'),
    ),
]


LPFONT = POINTER(IFont)
TEXTMETRICOLE = TEXTMETRICW
LPTEXTMETRICOLE = POINTER(TEXTMETRICOLE)


IFont._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_Name',
        (['out'], POINTER(BSTR), 'pName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Name',
        (['in'], BSTR, 'name'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Size',
        (['out'], POINTER(CY), 'pSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Size',
        (['in'], CY, 'size'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Bold',
        (['out'], POINTER(BOOL), 'pBold'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Bold',
        (['in'], BOOL, 'bold'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Italic',
        (['out'], POINTER(BOOL), 'pItalic'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Italic',
        (['in'], BOOL, 'italic'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Underline',
        (['out'], POINTER(BOOL), 'pUnderline'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Underline',
        (['in'], BOOL, 'underline'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Strikethrough',
        (['out'], POINTER(BOOL), 'pStrikethrough'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Strikethrough',
        (['in'], BOOL, 'strikethrough'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Weight',
        (['out'], POINTER(SHORT), 'pWeight'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Weight',
        (['in'], SHORT, 'weight'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Charset',
        (['out'], POINTER(SHORT), 'pCharset'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Charset',
        (['in'], SHORT, 'CHARset'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_hFont',
        (['out'], POINTER(HFONT), 'phFont'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IFont)), 'ppFont'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsEqual',
        (['in'], POINTER(IFont), 'pFontOther'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetRatio',
        (['in'], LONG, 'cyLogical'),
        (['in'], LONG, 'cyHimetric'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryTextMetrics',
        (['out'], POINTER(TEXTMETRICOLE), 'pTM'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddRefHfont',
        (['in'], HFONT, 'hFont'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReleaseHfont',
        (['in'], HFONT, 'hFont'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetHdc',
        (['in'], HDC, 'hDC'),
    ),
]


LPPICTURE = POINTER(IPicture)


class tagPictureAttributes(ENUM):
    PICTURE_SCALABLE = 0x1
    PICTURE_TRANSPARENT = 0x2


PICTUREATTRIBUTES = tagPictureAttributes

OLE_HANDLE = UINT
OLE_XPOS_HIMETRIC = LONG
OLE_YPOS_HIMETRIC = LONG
OLE_XSIZE_HIMETRIC = LONG
OLE_YSIZE_HIMETRIC = LONG


IPicture._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_Handle',
        (['out'], POINTER(OLE_HANDLE), 'pHandle'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_hPal',
        (['out'], POINTER(OLE_HANDLE), 'phPal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Type',
        (['out'], POINTER(SHORT), 'pType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Width',
        (['out'], POINTER(OLE_XSIZE_HIMETRIC), 'pWidth'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Height',
        (['out'], POINTER(OLE_YSIZE_HIMETRIC), 'pHeight'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Render',
        (['in'], HDC, 'hDC'),
        (['in'], LONG, 'x'),
        (['in'], LONG, 'y'),
        (['in'], LONG, 'cx'),
        (['in'], LONG, 'cy'),
        (['in'], OLE_XPOS_HIMETRIC, 'xSrc'),
        (['in'], OLE_YPOS_HIMETRIC, 'ySrc'),
        (['in'], OLE_XSIZE_HIMETRIC, 'cxSrc'),
        (['in'], OLE_YSIZE_HIMETRIC, 'cySrc'),
        (['in'], LPCRECT, 'pRcWBounds'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'set_hPal',
        (['in'], OLE_HANDLE, 'hPal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_CurDC',
        (['out'], POINTER(HDC), 'phDC'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectPicture',
        (['in'], HDC, 'hDCIn'),
        (['out'], POINTER(HDC), 'phDCOut'),
        (['out'], POINTER(OLE_HANDLE), 'phBmpOut'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_KeepOriginalFormat',
        (['out'], POINTER(BOOL), 'pKeep'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_KeepOriginalFormat',
        (['in'], BOOL, 'keep'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SaveAsFile',
        (['in'], LPSTREAM, 'pStream'),
        (['in'], BOOL, 'fSaveMemCopy'),
        (['out'], POINTER(LONG), 'pCbSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Attributes',
        (['out'], POINTER(DWORD), 'pDwAttr'),
    ),
]


LPPICTURE2 = POINTER(IPicture2)
HHANDLE = UINT_PTR


IPicture2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_Handle',
        (['out'], POINTER(HHANDLE), 'pHandle'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_hPal',
        (['out'], POINTER(HHANDLE), 'phPal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Type',
        (['out'], POINTER(SHORT), 'pType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Width',
        (['out'], POINTER(OLE_XSIZE_HIMETRIC), 'pWidth'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Height',
        (['out'], POINTER(OLE_YSIZE_HIMETRIC), 'pHeight'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Render',
        (['in'], HDC, 'hDC'),
        (['in'], LONG, 'x'),
        (['in'], LONG, 'y'),
        (['in'], LONG, 'cx'),
        (['in'], LONG, 'cy'),
        (['in'], OLE_XPOS_HIMETRIC, 'xSrc'),
        (['in'], OLE_YPOS_HIMETRIC, 'ySrc'),
        (['in'], OLE_XSIZE_HIMETRIC, 'cxSrc'),
        (['in'], OLE_YSIZE_HIMETRIC, 'cySrc'),
        (['in'], LPCRECT, 'pRcWBounds'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'set_hPal',
        (['in'], HHANDLE, 'hPal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_CurDC',
        (['out'], POINTER(HDC), 'phDC'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectPicture',
        (['in'], HDC, 'hDCIn'),
        (['out'], POINTER(HDC), 'phDCOut'),
        (['out'], POINTER(HHANDLE), 'phBmpOut'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_KeepOriginalFormat',
        (['out'], POINTER(BOOL), 'pKeep'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_KeepOriginalFormat',
        (['in'], BOOL, 'keep'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SaveAsFile',
        (['in'], LPSTREAM, 'pStream'),
        (['in'], BOOL, 'fSaveMemCopy'),
        (['out'], POINTER(LONG), 'pCbSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Attributes',
        (['out'], POINTER(DWORD), 'pDwAttr'),
    ),
]


LPFONTEVENTS = POINTER(IFontEventsDisp)
LPFONTDISP = POINTER(IFontDisp)
LPPICTUREDISP = POINTER(IPictureDisp)
LPOLEINPLACEOBJECTWINDOWLESS = POINTER(IOleInPlaceObjectWindowless)


IOleInPlaceObjectWindowless._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnWindowMessage',
        (['in'], UINT, 'msg'),
        (['in'], WPARAM, 'wParam'),
        (['in'], LPARAM, 'lParam'),
        (['out'], POINTER(LRESULT), 'plResult'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDropTarget',
        (['out'], POINTER(POINTER(IDropTarget)), 'ppDropTarget'),
    ),
]


LPOLEINPLACESITEEX = POINTER(IOleInPlaceSiteEx)


class tagACTIVATEFLAGS(ENUM):
    ACTIVATE_WINDOWLESS = 1


ACTIVATEFLAGS = tagACTIVATEFLAGS


IOleInPlaceSiteEx._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnInPlaceActivateEx',
        (['out'], POINTER(BOOL), 'pfNoRedraw'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnInPlaceDeactivateEx',
        (['in'], BOOL, 'fNoRedraw'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RequestUIActivate'
    ),
]


LPOLEINPLACESITEWINDOWLESS = POINTER(IOleInPlaceSiteWindowless)


class tagOLEDCFLAGS(ENUM):
    OLEDC_NODRAW = 0x1
    OLEDC_PAINTBKGND = 0x2
    OLEDC_OFFSCREEN = 0x4


OLEDCFLAGS = tagOLEDCFLAGS


IOleInPlaceSiteWindowless._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetCapture',
        (['in'], BOOL, 'fCapture'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFocus',
        (['in'], BOOL, 'fFocus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDC',
        (['in'], LPCRECT, 'pRect'),
        (['in'], DWORD, 'grfFlags'),
        (['out'], POINTER(HDC), 'phDC'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReleaseDC',
        (['in'], HDC, 'hDC'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'InvalidateRect',
        (['in'], LPCRECT, 'pRect'),
        (['in'], BOOL, 'fErase'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'InvalidateRgn',
        (['in'], HRGN, 'hRGN'),
        (['in'], BOOL, 'fErase'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ScrollRect',
        (['in'], INT, 'dx'),
        (['in'], INT, 'dy'),
        (['in'], LPCRECT, 'pRectScroll'),
        (['in'], LPCRECT, 'pRectClip'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AdjustRect',
        (['in', 'out'], LPRECT, 'prc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnDefWindowMessage',
        (['in'], UINT, 'msg'),
        (['in'], WPARAM, 'wParam'),
        (['in'], LPARAM, 'lParam'),
        (['out'], POINTER(LRESULT), 'plResult'),
    ),
]


LPVIEWOBJECTEX = POINTER(IViewObjectEx)


class tagVIEWSTATUS(ENUM):
    VIEWSTATUS_OPAQUE = 1
    VIEWSTATUS_SOLIDBKGND = 2
    VIEWSTATUS_DVASPECTOPAQUE = 4
    VIEWSTATUS_DVASPECTTRANSPARENT = 8
    VIEWSTATUS_SURFACE = 16
    VIEWSTATUS_3DSURFACE = 32


VIEWSTATUS = tagVIEWSTATUS


class tagHITRESULT(ENUM):
    HITRESULT_OUTSIDE = 0
    HITRESULT_TRANSPARENT = 1
    HITRESULT_CLOSE = 2
    HITRESULT_HIT = 3


HITRESULT = tagHITRESULT


class tagDVASPECT2(ENUM):
    DVASPECT_OPAQUE = 16
    DVASPECT_TRANSPARENT = 32


DVASPECT2 = tagDVASPECT2


class tagExtentInfo(ctypes.Structure):
    _fields_ = [
        ('cb', ULONG),
        ('dwExtentMode', DWORD),
        ('sizelProposed', SIZEL),
    ]


DVEXTENTINFO = tagExtentInfo


class tagExtentMode(ENUM):
    DVEXTENT_CONTENT = 0
    DVEXTENT_INTEGRAL = DVEXTENT_CONTENT + 1


DVEXTENTMODE = tagExtentMode


class tagAspectInfoFlag(ENUM):
    DVASPECTINFOFLAG_CANOPTIMIZE = 1


DVASPECTINFOFLAG = tagAspectInfoFlag


class tagAspectInfo(ctypes.Structure):
    _fields_ = [
        ('cb', ULONG),
        ('dwFlags', DWORD),
    ]


DVASPECTINFO = tagAspectInfo


IViewObjectEx._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetRect',
        (['in'], DWORD, 'dwAspect'),
        (['out'], LPRECTL, 'pRect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetViewStatus',
        (['out'], POINTER(DWORD), 'pdwStatus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryHitPoint',
        (['in'], DWORD, 'dwAspect'),
        (['in'], LPCRECT, 'pRectBounds'),
        (['in'], POINT, 'ptlLoc'),
        (['in'], LONG, 'lCloseHINT'),
        (['out'], POINTER(DWORD), 'pHitResult'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryHitRect',
        (['in'], DWORD, 'dwAspect'),
        (['in'], LPCRECT, 'pRectBounds'),
        (['in'], LPCRECT, 'pRectLoc'),
        (['in'], LONG, 'lCloseHINT'),
        (['out'], POINTER(DWORD), 'pHitResult'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNaturalExtent',
        (['in'], DWORD, 'dwAspect'),
        (['in'], LONG, 'lindex'),
        (['in'], POINTER(DVTARGETDEVICE), 'ptd'),
        (['in'], HDC, 'hicTargetDev'),
        (['in'], POINTER(DVEXTENTINFO), 'pExtentInfo'),
        (['out'], LPSIZEL, 'pSizel'),
    ),
]


LPOLEUNDOUNIT = POINTER(IOleUndoUnit)


IOleUndoUnit._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Do',
        (['in'], POINTER(IOleUndoManager), 'pUndoManager'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDescription',
        (['out'], POINTER(BSTR), 'pBstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetUnitType',
        (['out'], POINTER(CLSID), 'pClsid'),
        (['out'], POINTER(LONG), 'plID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnNextAdd'
    ),
]


LPOLEPARENTUNDOUNIT = POINTER(IOleParentUndoUnit)


IOleParentUndoUnit._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Open',
        (['in'], POINTER(IOleParentUndoUnit), 'pPUU'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Close',
        (['in'], POINTER(IOleParentUndoUnit), 'pPUU'),
        (['in'], BOOL, 'fCommit'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Add',
        (['in'], POINTER(IOleUndoUnit), 'pUU'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FindUnit',
        (['in'], POINTER(IOleUndoUnit), 'pUU'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetParentState',
        (['out'], POINTER(DWORD), 'pdwState'),
    ),
]


LPENUMOLEUNDOUNITS = POINTER(IEnumOleUndoUnits)


IEnumOleUndoUnits._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'cElt'),
        (['out'], POINTER(POINTER(IOleUndoUnit)), 'rgElt'),
        (['out'], POINTER(ULONG), 'pcEltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'cElt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumOleUndoUnits)), 'ppEnum'),
    ),
]


SID_SOleUndoManager = IID_IOleUndoManager
LPOLEUNDOMANAGER = POINTER(IOleUndoManager)


IOleUndoManager._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Open',
        (['in'], POINTER(IOleParentUndoUnit), 'pPUU'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Close',
        (['in'], POINTER(IOleParentUndoUnit), 'pPUU'),
        (['in'], BOOL, 'fCommit'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Add',
        (['in'], POINTER(IOleUndoUnit), 'pUU'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetOpenParentState',
        (['out'], POINTER(DWORD), 'pdwState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DiscardFrom',
        (['in'], POINTER(IOleUndoUnit), 'pUU'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UndoTo',
        (['in'], POINTER(IOleUndoUnit), 'pUU'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RedoTo',
        (['in'], POINTER(IOleUndoUnit), 'pUU'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumUndoable',
        (['out'], POINTER(POINTER(IEnumOleUndoUnits)), 'ppEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumRedoable',
        (['out'], POINTER(POINTER(IEnumOleUndoUnits)), 'ppEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLastUndoDescription',
        (['out'], POINTER(BSTR), 'pBstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLastRedoDescription',
        (['out'], POINTER(BSTR), 'pBstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Enable',
        (['in'], BOOL, 'fEnable'),
    ),
]


LPPOINTERINACTIVE = POINTER(IPointerInactive)


class tagPOINTERINACTIVE(ENUM):
    POINTERINACTIVE_ACTIVATEONENTRY = 1
    POINTERINACTIVE_DEACTIVATEONLEAVE = 2
    POINTERINACTIVE_ACTIVATEONDRAG = 4


POINTERINACTIVE = tagPOINTERINACTIVE


IPointerInactive._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetActivationPolicy',
        (['out'], POINTER(DWORD), 'pdwPolicy'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnInactiveMouseMove',
        (['in'], LPCRECT, 'pRectBounds'),
        (['in'], LONG, 'x'),
        (['in'], LONG, 'y'),
        (['in'], DWORD, 'grfKeyState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnInactiveSetCursor',
        (['in'], LPCRECT, 'pRectBounds'),
        (['in'], LONG, 'x'),
        (['in'], LONG, 'y'),
        (['in'], DWORD, 'dwMouseMsg'),
        (['in'], BOOL, 'fSetAlways'),
    ),
]


LPOBJECTWITHSITE = POINTER(IObjectWithSite)


IObjectWithSite._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetSite',
        (['in'], POINTER(comtypes.IUnknown), 'pUnkSite'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSite',
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvSite'),
    ),
]


LPPERPROPERTYBROWSING = POINTER(IPerPropertyBrowsing)


class tagCALPOLESTR(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(LPOLESTR)),
    ]


CALPOLESTR = tagCALPOLESTR


LPCALPOLESTR = POINTER(tagCALPOLESTR)


class tagCADWORD(ctypes.Structure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', POINTER(DWORD)),
    ]


CADWORD = tagCADWORD


LPCADWORD = POINTER(tagCADWORD)


IPerPropertyBrowsing._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDisplayString',
        (['in'], DISPID, 'dispID'),
        (['out'], POINTER(BSTR), 'pBstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'MapPropertyToPage',
        (['in'], DISPID, 'dispID'),
        (['out'], POINTER(CLSID), 'pClsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPredefinedStrings',
        (['in'], DISPID, 'dispID'),
        (['out'], POINTER(CALPOLESTR), 'pCaStringsOut'),
        (['out'], POINTER(CADWORD), 'pCaCookiesOut'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPredefinedValue',
        (['in'], DISPID, 'dispID'),
        (['in'], DWORD, 'dwCookie'),
        (['out'], POINTER(VARIANT), 'pVarOut'),
    ),
]


LPPROPERTYBAG2 = POINTER(IPropertyBag2)


class tagPROPBAG2_TYPE(ENUM):
    PROPBAG2_TYPE_UNDEFINED = 0
    PROPBAG2_TYPE_DATA = 1
    PROPBAG2_TYPE_URL = 2
    PROPBAG2_TYPE_OBJECT = 3
    PROPBAG2_TYPE_STREAM = 4
    PROPBAG2_TYPE_STORAGE = 5
    PROPBAG2_TYPE_MONIKER = 6


PROPBAG2_TYPE = tagPROPBAG2_TYPE


class tagPROPBAG2(ctypes.Structure):
    _fields_ = [
        ('dwType', DWORD),
        ('vt', VARTYPE),
        ('cfType', CLIPFORMAT),
        ('dwHINT', DWORD),
        ('pstrName', LPOLESTR),
        ('clsid', CLSID),
    ]


PROPBAG2 = tagPROPBAG2


IPropertyBag2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Read',
        (['in'], ULONG, 'cProperties'),
        (['in'], POINTER(PROPBAG2), 'pPropBag'),
        (['in'], POINTER(IErrorLog), 'pErrLog'),
        (['out'], POINTER(VARIANT), 'pvarValue'),
        (['in', 'out'], POINTER(HRESULT), 'phrError'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Write',
        (['in'], ULONG, 'cProperties'),
        (['in'], POINTER(PROPBAG2), 'pPropBag'),
        (['in'], POINTER(VARIANT), 'pvarValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CountProperties',
        (['out'], POINTER(ULONG), 'pcProperties'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPropertyInfo',
        (['in'], ULONG, 'iProperty'),
        (['in'], ULONG, 'cProperties'),
        (['out'], POINTER(PROPBAG2), 'pPropBag'),
        (['out'], POINTER(ULONG), 'pcProperties'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'LoadObject',
        (['in'], LPCOLESTR, 'pstrName'),
        (['in'], DWORD, 'dwHINT'),
        (['in'], POINTER(comtypes.IUnknown), 'pUnkObject'),
        (['in'], POINTER(IErrorLog), 'pErrLog'),
    ),
]


LPPERSISTPROPERTYBAG2 = POINTER(IPersistPropertyBag2)


IPersistPropertyBag2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Load',
        (['in'], POINTER(IPropertyBag2), 'pPropBag'),
        (['in'], POINTER(IErrorLog), 'pErrLog'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Save',
        (['in'], POINTER(IPropertyBag2), 'pPropBag'),
        (['in'], BOOL, 'fClearDirty'),
        (['in'], BOOL, 'fSaveAllProperties'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsDirty'
    ),
]


LPADVISESINKEX = POINTER(IAdviseSinkEx)


IAdviseSinkEx._methods_ = [
    COMMETHOD(
        [],
        VOID,
        'OnViewStatusChange',
        (['in'], DWORD, 'dwViewStatus'),
    ),
]


LPQUICKACTIVATE = POINTER(IQuickActivate)


class tagQACONTAINERFLAGS(ENUM):
    QACONTAINER_SHOWHATCHING = 0x1
    QACONTAINER_SHOWGRABHANDLES = 0x2
    QACONTAINER_USERMODE = 0x4
    QACONTAINER_DISPLAYASDEFAULT = 0x8
    QACONTAINER_UIDEAD = 0x10
    QACONTAINER_AUTOCLIP = 0x20
    QACONTAINER_MESSAGEREFLECT = 0x40
    QACONTAINER_SUPPORTSMNEMONICS = 0x80


QACONTAINERFLAGS = tagQACONTAINERFLAGS


OLE_COLOR = DWORD
# from .urlmon_h import IBindHost

IBindHost = VOID


class tagQACONTAINER(ctypes.Structure):
    _fields_ = [
        ('cbSize', ULONG),
        ('pClientSite', POINTER(IOleClientSite)),
        ('pAdviseSink', POINTER(IAdviseSinkEx)),
        ('pPropertyNotifySink', POINTER(IPropertyNotifySink)),
        ('pUnkEventSink', POINTER(comtypes.IUnknown)),
        ('dwAmbientFlags', DWORD),
        ('colorFore', OLE_COLOR),
        ('colorBack', OLE_COLOR),
        ('pFont', POINTER(IFont)),
        ('pUndoMgr', POINTER(IOleUndoManager)),
        ('dwAppearance', DWORD),
        ('lcid', LONG),
        ('hpal', HPALETTE),
        ('pBindHost', POINTER(IBindHost)),
        ('pOleControlSite', POINTER(IOleControlSite)),
        ('pServiceProvider', POINTER(IServiceProvider)),
    ]


QACONTAINER = tagQACONTAINER


class tagQACONTROL(ctypes.Structure):
    _fields_ = [
        ('cbSize', ULONG),
        ('dwMiscStatus', DWORD),
        ('dwViewStatus', DWORD),
        ('dwEventCookie', DWORD),
        ('dwPropNotifyCookie', DWORD),
        ('dwPointerActivationPolicy', DWORD),
    ]


QACONTROL = tagQACONTROL


IQuickActivate._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QuickActivate',
        (['in'], POINTER(QACONTAINER), 'pQaContainer'),
        (['in', 'out'], POINTER(QACONTROL), 'pQaControl'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetContentExtent',
        (['in'], LPSIZEL, 'pSizel'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetContentExtent',
        (['out'], LPSIZEL, 'pSizel'),
    ),
]


__all__ = (
    'IPersistPropertyBag', 'IPropertyPageSite', 'IPersistStreamInit', 'IFont',
    'IPropertyNotifySink', 'ISpecifyPropertyPages', 'IAdviseSinkEx', 'CAUUID',
    'IQuickActivate', 'IViewObjectEx', 'IObjectWithSite', 'IPropertyPage2',
    'IConnectionPoint', 'IPicture2', 'ISimpleFrameSite', 'IProvideClassInfo',
    'IFontDisp', 'IProvideMultipleClassInfo', 'IPointerInactive', 'IPicture',
    'IEnumConnectionPoints', 'IPersistMemory', 'IOleParentUndoUnit', 'POINTF',
    'IFontEventsDisp', 'IProvideClassInfo2', 'IPictureDisp', 'IOleControl',
    'IOleInPlaceSiteEx', 'IPerPropertyBrowsing', 'IPropertyBag2', 'DVASPECT2',
    'IPersistPropertyBag2', 'IEnumOleUndoUnits', 'IOleInPlaceSiteWindowless',
    'IOleInPlaceObjectWindowless', 'IConnectionPointContainer', 'tagCTRLINFO',
    'IEnumConnections', 'IOleControlSite', 'IOleUndoManager', 'IOleUndoUnit',
    'IClassFactory2', 'IPropertyPage', 'MULTICLASSINFO_GETNUMRESERVEDDISPIDS',
    '__REQUIRED_RPCNDR_H_VERSION__', 'MULTICLASSINFO_GETTYPEINFO', 'GUIDKIND',
    'SID_SOleUndoManager', '__REQUIRED_RPCSAL_H_VERSION__', 'POINTERINACTIVE',
    'TIFLAGS_EXTENDDISPATCHONLY', 'MULTICLASSINFO_GETIIDPRIMARY', 'CTRLINFO',
    'MULTICLASSINFO_GETIIDSOURCE', 'tagPOINTERINACTIVE', 'QACONTAINERFLAGS',
    'PROPPAGESTATUS', 'tagVIEWSTATUS', 'tagHITRESULT', 'OLEDCFLAGS', 'LPFONT',
    'tagAspectInfoFlag', 'ACTIVATEFLAGS', 'DVASPECTINFOFLAG', 'tagREADYSTATE',
    'PICTUREATTRIBUTES', 'READYSTATE', 'tagQACONTAINERFLAGS', 'tagDVASPECT2',
    'tagExtentMode', 'tagUASFLAGS', 'tagXFORMCOORDS', 'PROPBAG2_TYPE',
    'tagACTIVATEFLAGS', 'tagOLEDCFLAGS', 'HITRESULT', 'XFORMCOORDS',
    'UASFLAGS', 'tagPROPBAG2_TYPE', 'tagPictureAttributes', 'VIEWSTATUS',
    'tagGUIDKIND', 'tagPROPPAGESTATUS', 'DVEXTENTMODE', 'CADWORD', 'PROPBAG2',
    'tagQACONTROL', 'DVASPECTINFO', 'QACONTAINER', 'CALPOLESTR', 'LPCAUUID',
    'CONNECTDATA', 'LPCALPOLESTR', 'tagAspectInfo', 'tagCALPOLESTR',
    'QACONTROL', 'tagPROPBAG2', 'tagPOINTF', 'LPCONNECTDATA', 'PROPPAGEINFO',
    'LICINFO', 'tagCONNECTDATA', 'LPPOINTF', 'tagPROPPAGEINFO', 'LPCADWORD',
    'PCONNECTDATA', 'tagQACONTAINER', 'CONTROLINFO', 'LPCONTROLINFO',
    'tagCAUUID', 'tagCONTROLINFO', 'DVEXTENTINFO', 'LPLICINFO', 'tagLICINFO',
    'tagExtentInfo', 'LPPROPPAGEINFO', 'tagCADWORD', 'LPFONTDISP', 'HHANDLE',
    'OLE_XPOS_HIMETRIC', 'LPPICTURE', 'LPPERPROPERTYBROWSING', 'LPFONTEVENTS',
    'LPTEXTMETRICOLE', 'LPCONNECTIONPOINT', 'LPPERSISTSTREAMINIT',
    'LPPROVIDEMULTIPLECLASSINFO', 'LPPICTUREDISP', 'LPVIEWOBJECTEX',
    'LPOLECONTROLSITE', 'LPPOINTERINACTIVE', 'OLE_YSIZE_HIMETRIC',
    'LPPROPERTYPAGESITE', 'LPOLEINPLACESITEEX', 'LPOLEUNDOMANAGER',
    'PENUMCONNECTIONS', 'OLE_COLOR', 'LPENUMCONNECTIONPOINTS', 'LPPICTURE2',
    'LPPROPERTYBAG2', 'TEXTMETRICOLE', 'OLE_YPOS_HIMETRIC', 'LPQUICKACTIVATE',
    'LPENUMOLEUNDOUNITS', 'LPPERSISTPROPERTYBAG2', 'LPENUMCONNECTIONS',
    'LPPROPERTYPAGE', 'LPADVISESINKEX', 'LPSPECIFYPROPERTYPAGES',
    'LPPROPERTYNOTIFYSINK', 'OLE_HANDLE', 'LPOLEUNDOUNIT', 'LPPERSISTMEMORY',
    'LPSIMPLEFRAMESITE', 'LPPROVIDECLASSINFO2', 'LPCONNECTIONPOINTCONTAINER',
    'LPPROPERTYPAGE2', 'PCONNECTIONPOINTCONTAINER', 'PCONNECTIONPOINT',
    'LPOLEINPLACESITEWINDOWLESS', 'PENUMCONNECTIONPOINTS', 'LPOLECONTROL',
    'LPCLASSFACTORY2', 'LPOLEPARENTUNDOUNIT', 'LPOLEINPLACEOBJECTWINDOWLESS',
    'OLE_XSIZE_HIMETRIC', 'LPPROVIDECLASSINFO', 'LPOBJECTWITHSITE',
    'LPPERSISTPROPERTYBAG',
)
