__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import * # NOQA
# from .rpcndr_h import * # NOQA
# from .windows_h import * # NOQA
# from .ole2_h import * # NOQA

from .wtypes_h import (
    ENUM,
    POINTER,
    DWORD,
    HRESULT,
    ULONG,
    REFCLSID,
    LPCOLESTR,
    LPOLESTR,
    LPCWSTR,
    BOOL,
    HWND,
    HMENU,
    LPMSG,
    WORD,
    LONG,
    LPCRECT,
    CLSID,
    SIZEL,
    LOGPALETTE,
    LPVOID,
    POINTL,
    REFIID,
    VOID,
    LPRECT,
    SIZE,
    HDC,
    LPCRECTL,
    ULONG_PTR,
    LPSIZEL,
    UINT,
    HACCEL,
    HGLOBAL,
    RECT,
    TEXT
)
from .guiddef_h import (
    IID,
)
import ctypes
import comtypes


# Forward Declarations
IID_IOleAdviseHolder = IID(
    '{00000111-0000-0000-C000-000000000046}'
)


class IOleAdviseHolder(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOleAdviseHolder
    _idlflags_ = []


# __IOleAdviseHolder_FWD_DEFINED__
IID_IOleCache = IID(
    '{0000011e-0000-0000-C000-000000000046}'
)


class IOleCache(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOleCache
    _idlflags_ = []


# __IOleCache_FWD_DEFINED__
IID_IOleCache2 = IID(
    '{00000128-0000-0000-C000-000000000046}'
)


class IOleCache2(IOleCache):
    _case_insensitive_ = True
    _iid_ = IID_IOleCache2
    _idlflags_ = []


# __IOleCache2_FWD_DEFINED__
IID_IOleCacheControl = IID(
    '{00000129-0000-0000-C000-000000000046}'
)


class IOleCacheControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOleCacheControl
    _idlflags_ = []


# __IOleCacheControl_FWD_DEFINED__
IID_IParseDisplayName = IID(
    '{0000011a-0000-0000-C000-000000000046}'
)


class IParseDisplayName(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IParseDisplayName
    _idlflags_ = []


# __IParseDisplayName_FWD_DEFINED__
IID_IOleContainer = IID(
    '{0000011b-0000-0000-C000-000000000046}'
)


class IOleContainer(IParseDisplayName):
    _case_insensitive_ = True
    _iid_ = IID_IOleContainer
    _idlflags_ = []


# __IOleContainer_FWD_DEFINED__
IID_IOleClientSite = IID(
    '{00000118-0000-0000-C000-000000000046}'
)


class IOleClientSite(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOleClientSite
    _idlflags_ = []


# __IOleClientSite_FWD_DEFINED__
IID_IOleObject = IID(
    '{00000112-0000-0000-C000-000000000046}'
)


class IOleObject(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOleObject
    _idlflags_ = []


# __IOleObject_FWD_DEFINED__
IID_IOleWindow = IID(
    '{00000114-0000-0000-C000-000000000046}'
)


class IOleWindow(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOleWindow
    _idlflags_ = []


# __IOleWindow_FWD_DEFINED__
IID_IOleLink = IID(
    '{0000011d-0000-0000-C000-000000000046}'
)


class IOleLink(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOleLink
    _idlflags_ = []


# __IOleLink_FWD_DEFINED__
IID_IOleItemContainer = IID(
    '{0000011c-0000-0000-C000-000000000046}'
)


class IOleItemContainer(IOleContainer):
    _case_insensitive_ = True
    _iid_ = IID_IOleItemContainer
    _idlflags_ = []


# __IOleItemContainer_FWD_DEFINED__
IID_IOleInPlaceUIWindow = IID(
    '{00000115-0000-0000-C000-000000000046}'
)


class IOleInPlaceUIWindow(IOleWindow):
    _case_insensitive_ = True
    _iid_ = IID_IOleInPlaceUIWindow
    _idlflags_ = []


# __IOleInPlaceUIWindow_FWD_DEFINED__
IID_IOleInPlaceActiveObject = IID(
    '{00000117-0000-0000-C000-000000000046}'
)


class IOleInPlaceActiveObject(IOleWindow):
    _case_insensitive_ = True
    _iid_ = IID_IOleInPlaceActiveObject
    _idlflags_ = []


# __IOleInPlaceActiveObject_FWD_DEFINED__
IID_IOleInPlaceFrame = IID(
    '{00000116-0000-0000-C000-000000000046}'
)


class IOleInPlaceFrame(IOleInPlaceUIWindow):
    _case_insensitive_ = True
    _iid_ = IID_IOleInPlaceFrame
    _idlflags_ = []


# __IOleInPlaceFrame_FWD_DEFINED__
IID_IOleInPlaceObject = IID(
    '{00000113-0000-0000-C000-000000000046}'
)


class IOleInPlaceObject(IOleWindow):
    _case_insensitive_ = True
    _iid_ = IID_IOleInPlaceObject
    _idlflags_ = []


# __IOleInPlaceObject_FWD_DEFINED__
IID_IOleInPlaceSite = IID(
    '{00000119-0000-0000-C000-000000000046}'
)


class IOleInPlaceSite(IOleWindow):
    _case_insensitive_ = True
    _iid_ = IID_IOleInPlaceSite
    _idlflags_ = []


# __IOleInPlaceSite_FWD_DEFINED__
IID_IContinue = IID(
    '{0000012a-0000-0000-C000-000000000046}'
)


class IContinue(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IContinue
    _idlflags_ = []


# __IContinue_FWD_DEFINED__
IID_IViewObject = IID(
    '{0000010d-0000-0000-C000-000000000046}'
)


class IViewObject(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IViewObject
    _idlflags_ = []


# __IViewObject_FWD_DEFINED__
IID_IViewObject2 = IID(
    '{00000127-0000-0000-C000-000000000046}'
)


class IViewObject2(IViewObject):
    _case_insensitive_ = True
    _iid_ = IID_IViewObject2
    _idlflags_ = []


# __IViewObject2_FWD_DEFINED__
IID_IDropSource = IID(
    '{00000121-0000-0000-C000-000000000046}'
)


class IDropSource(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDropSource
    _idlflags_ = []


# __IDropSource_FWD_DEFINED__
IID_IDropTarget = IID(
    '{00000122-0000-0000-C000-000000000046}'
)


class IDropTarget(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDropTarget
    _idlflags_ = []


# __IDropTarget_FWD_DEFINED__
IID_IDropSourceNotify = IID(
    '{0000012B-0000-0000-C000-000000000046}'
)


class IDropSourceNotify(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDropSourceNotify
    _idlflags_ = []


# __IDropSourceNotify_FWD_DEFINED__
IID_IEnterpriseDropTarget = IID(
    '{390E3878-FD55-4E18-819D-4682081C0CFD}'
)


class IEnterpriseDropTarget(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnterpriseDropTarget
    _idlflags_ = []


IID_IEnumOLEVERB = IID(
    '{00000104-0000-0000-C000-000000000046}'
)


class IEnumOLEVERB(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumOLEVERB
    _idlflags_ = []


# header files for imported files
from .objidl_h import * # NOQA


LPOLEADVISEHOLDER = POINTER(IOleAdviseHolder)
COMMETHOD = comtypes.COMMETHOD


IOleAdviseHolder._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Advise',
        (['in'], POINTER(IAdviseSink), 'pAdvise'),
        (['out'], POINTER(DWORD), 'pdwConnection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Unadvise',
        (['in'], DWORD, 'dwConnection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumAdvise',
        (['out'], POINTER(POINTER(IEnumSTATDATA)), 'ppenumAdvise'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SendOnRename',
        (['in'], POINTER(IMoniker), 'pmk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SendOnClose'
    ),
]


from .objidl_h import DVTARGETDEVICE, FORMATETC, STGMEDIUM


LPOLECACHE = POINTER(IOleCache)
IOleCache._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Cache',
        (['in'], POINTER(FORMATETC), 'pformatetc'),
        (['in'], DWORD, 'advf'),
        (['out'], POINTER(DWORD), 'pdwConnection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Uncache',
        (['in'], DWORD, 'dwConnection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumCache',
        (['out'], POINTER(POINTER(IEnumSTATDATA)), 'ppenumSTATDATA'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'InitCache',
        (['in'], POINTER(IDataObject), 'pDataObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetData',
        (['in'], POINTER(FORMATETC), 'pformatetc'),
        (['in'], POINTER(STGMEDIUM), 'pmedium'),
        (['in'], BOOL, 'fRelease'),
    ),
]


LPOLECACHE2 = POINTER(IOleCache2)
UPDFCACHE_NODATACACHE = 0x1
UPDFCACHE_ONSAVECACHE = 0x2
UPDFCACHE_ONSTOPCACHE = 0x4
UPDFCACHE_NORMALCACHE = 0x8
UPDFCACHE_IFBLANK = 0x10
UPDFCACHE_ONLYIFBLANK = 0x80000000
UPDFCACHE_IFBLANKORONSAVECACHE = UPDFCACHE_IFBLANK | UPDFCACHE_ONSAVECACHE
UPDFCACHE_ALL = ~UPDFCACHE_ONLYIFBLANK
UPDFCACHE_ALLBUTNODATACACHE = UPDFCACHE_ALL & ~UPDFCACHE_NODATACACHE


class tagDISCARDCACHE(ENUM):
    DISCARDCACHE_SAVEIFDIRTY = 0
    DISCARDCACHE_NOSAVE = 1


DISCARDCACHE = tagDISCARDCACHE


IOleCache2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'UpdateCache',
        (['in'], LPDATAOBJECT, 'pDataObject'),
        (['in'], DWORD, 'grfUpdf'),
        (['in'], LPVOID, 'pReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DiscardCache',
        (['in'], DWORD, 'dwDiscardOptions'),
    ),
]


LPOLECACHECONTROL = POINTER(IOleCacheControl)


IOleCacheControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnRun',
        ([], LPDATAOBJECT, 'pDataObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnStop'
    ),
]


LPPARSEDISPLAYNAME = POINTER(IParseDisplayName)


IParseDisplayName._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ParseDisplayName',
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], LPOLESTR, 'pszDisplayName'),
        (['out'], POINTER(ULONG), 'pchEaten'),
        (['out'], POINTER(POINTER(IMoniker)), 'ppmkOut'),
    ),
]


LPOLECONTAINER = POINTER(IOleContainer)


IOleContainer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumObjects',
        (['in'], DWORD, 'grfFlags'),
        (['out'], POINTER(POINTER(IEnumUnknown)), 'ppenum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'LockContainer',
        (['in'], BOOL, 'fLock'),
    ),
]

LPOLECLIENTSITE = POINTER(IOleClientSite)


IOleClientSite._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetMoniker',
        (['in'], DWORD, 'dwAssign'),
        (['in'], DWORD, 'dwWhichMoniker'),
        (['out'], POINTER(POINTER(IMoniker)), 'ppmk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetContainer',
        (['out'], POINTER(POINTER(IOleContainer)), 'ppContainer'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnShowWindow',
        (['in'], BOOL, 'fShow'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RequestNewObjectLayout'
    ),
]


LPOLEOBJECT = POINTER(IOleObject)


class tagOLEGETMONIKER(ENUM):
    OLEGETMONIKER_ONLYIFTHERE = 1
    OLEGETMONIKER_FORCEASSIGN = 2
    OLEGETMONIKER_UNASSIGN = 3
    OLEGETMONIKER_TEMPFORUSER = 4


OLEGETMONIKER = tagOLEGETMONIKER


class tagOLEWHICHMK(ENUM):
    OLEWHICHMK_CONTAINER = 1
    OLEWHICHMK_OBJREL = 2
    OLEWHICHMK_OBJFULL = 3


OLEWHICHMK = tagOLEWHICHMK


class tagUSERCLASSTYPE(ENUM):
    USERCLASSTYPE_FULL = 1
    USERCLASSTYPE_SHORT = 2
    USERCLASSTYPE_APPNAME = 3


USERCLASSTYPE = tagUSERCLASSTYPE


class tagOLEMISC(ENUM):
    OLEMISC_RECOMPOSEONRESIZE = 0x1
    OLEMISC_ONLYICONIC = 0x2
    OLEMISC_INSERTNOTREPLACE = 0x4
    OLEMISC_STATIC = 0x8
    OLEMISC_CANTLINKINSIDE = 0x10
    OLEMISC_CANLINKBYOLE1 = 0x20
    OLEMISC_ISLINKOBJECT = 0x40
    OLEMISC_INSIDEOUT = 0x80
    OLEMISC_ACTIVATEWHENVISIBLE = 0x100
    OLEMISC_RENDERINGISDEVICEINDEPENDENT = 0x200
    OLEMISC_INVISIBLEATRUNTIME = 0x400
    OLEMISC_ALWAYSRUN = 0x800
    OLEMISC_ACTSLIKEBUTTON = 0x1000
    OLEMISC_ACTSLIKELABEL = 0x2000
    OLEMISC_NOUIACTIVATE = 0x4000
    OLEMISC_ALIGNABLE = 0x8000
    OLEMISC_SIMPLEFRAME = 0x10000
    OLEMISC_SETCLIENTSITEFIRST = 0x20000
    OLEMISC_IMEMODE = 0x40000
    OLEMISC_IGNOREACTIVATEWHENVISIBLE = 0x80000
    OLEMISC_WANTSTOMENUMERGE = 0x100000
    OLEMISC_SUPPORTSMULTILEVELUNDO = 0x200000


OLEMISC = tagOLEMISC


class tagOLECLOSE(ENUM):
    OLECLOSE_SAVEIFDIRTY = 0
    OLECLOSE_NOSAVE = 1
    OLECLOSE_PROMPTSAVE = 2


OLECLOSE = tagOLECLOSE


IOleObject._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetClientSite',
        (['in'], POINTER(IOleClientSite), 'pClientSite'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetClientSite',
        (['out'], POINTER(POINTER(IOleClientSite)), 'ppClientSite'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetHostNames',
        (['in'], LPCOLESTR, 'szContainerApp'),
        (['in'], LPCOLESTR, 'szContainerObj'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Close',
        (['in'], DWORD, 'dwSaveOption'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMoniker',
        (['in'], DWORD, 'dwWhichMoniker'),
        (['in'], POINTER(IMoniker), 'pmk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMoniker',
        (['in'], DWORD, 'dwAssign'),
        (['in'], DWORD, 'dwWhichMoniker'),
        (['out'], POINTER(POINTER(IMoniker)), 'ppmk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'InitFromData',
        (['in'], POINTER(IDataObject), 'pDataObject'),
        (['in'], BOOL, 'fCreation'),
        (['in'], DWORD, 'dwReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetClipboardData',
        (['in'], DWORD, 'dwReserved'),
        (['out'], POINTER(POINTER(IDataObject)), 'ppDataObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DoVerb',
        (['in'], LONG, 'iVerb'),
        (['in'], LPMSG, 'lpmsg'),
        (['in'], POINTER(IOleClientSite), 'pActiveSite'),
        (['in'], LONG, 'lindex'),
        (['in'], HWND, 'hwndParent'),
        (['in'], LPCRECT, 'lprcPosRect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumVerbs',
        (['out'], POINTER(POINTER(IEnumOLEVERB)), 'ppEnumOleVerb'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetUserClassID',
        (['out'], POINTER(CLSID), 'pClsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetUserType',
        (['in'], DWORD, 'dwFormOfType'),
        (['out'], POINTER(LPOLESTR), 'pszUserType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetExtent',
        (['in'], DWORD, 'dwDrawAspect'),
        (['in'], POINTER(SIZEL), 'psizel'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetExtent',
        (['in'], DWORD, 'dwDrawAspect'),
        (['out'], POINTER(SIZEL), 'psizel'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Advise',
        (['in'], POINTER(IAdviseSink), 'pAdvSink'),
        (['out'], POINTER(DWORD), 'pdwConnection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Unadvise',
        (['in'], DWORD, 'dwConnection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumAdvise',
        (['out'], POINTER(POINTER(IEnumSTATDATA)), 'ppenumAdvise'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMiscStatus',
        (['in'], DWORD, 'dwAspect'),
        (['out'], POINTER(DWORD), 'pdwStatus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetColorScheme',
        (['in'], POINTER(LOGPALETTE), 'pLogpal'),
    ),
]


class tagOLERENDER(ENUM):
    OLERENDER_NONE = 0
    OLERENDER_DRAW = 1
    OLERENDER_FORMAT = 2
    OLERENDER_ASIS = 3


OLERENDER = tagOLERENDER
LPOLERENDER = POINTER(OLERENDER)


class tagOBJECTDESCRIPTOR(ctypes.Structure):
    _fields_ = [
        ('cbSize', ULONG),
        ('clsid', CLSID),
        ('dwDrawAspect', DWORD),
        ('sizel', SIZEL),
        ('poINTl', POINTL),
        ('dwStatus', DWORD),
        ('dwFullUserTypeName', DWORD),
        ('dwSrcOfCopy', DWORD),
    ]


OBJECTDESCRIPTOR = tagOBJECTDESCRIPTOR
POBJECTDESCRIPTOR = POINTER(tagOBJECTDESCRIPTOR)
LPOBJECTDESCRIPTOR = POINTER(tagOBJECTDESCRIPTOR)
LINKSRCDESCRIPTOR = tagOBJECTDESCRIPTOR
PLINKSRCDESCRIPTOR = POINTER(tagOBJECTDESCRIPTOR)
LPLINKSRCDESCRIPTOR = POINTER(tagOBJECTDESCRIPTOR)


LPOLEWINDOW = POINTER(IOleWindow)


IOleWindow._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetWindow',
        (['out'], POINTER(HWND), 'phwnd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ContextSensitiveHelp',
        (['in'], BOOL, 'fEnterMode'),
    ),
]


LPOLELINK = POINTER(IOleLink)


class tagOLEUPDATE(ENUM):
    OLEUPDATE_ALWAYS = 1
    OLEUPDATE_ONCALL = 3


OLEUPDATE = tagOLEUPDATE
LPOLEUPDATE = POINTER(OLEUPDATE)
POLEUPDATE = POINTER(OLEUPDATE)


class tagOLELINKBIND(ENUM):
    OLELINKBIND_EVENIFCLASSDIFF = 1


OLELINKBIND = tagOLELINKBIND


IOleLink._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetUpdateOptions',
        (['in'], DWORD, 'dwUpdateOpt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetUpdateOptions',
        (['out'], POINTER(DWORD), 'pdwUpdateOpt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSourceMoniker',
        (['in'], POINTER(IMoniker), 'pmk'),
        (['in'], REFCLSID, 'rclsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSourceMoniker',
        (['out'], POINTER(POINTER(IMoniker)), 'ppmk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSourceDisplayName',
        (['in'], LPCOLESTR, 'pszStatusText'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSourceDisplayName',
        (['out'], POINTER(LPOLESTR), 'ppszDisplayName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'BindToSource',
        (['in'], DWORD, 'bindflags'),
        (['in'], POINTER(IBindCtx), 'pbc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBoundSource',
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppunk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Update',
        (['in'], POINTER(IBindCtx), 'pbc'),
    ),
]


LPOLEITEMCONTAINER = POINTER(IOleItemContainer)


class tagBINDSPEED(ENUM):
    BINDSPEED_INDEFINITE = 1
    BINDSPEED_MODERATE = 2
    BINDSPEED_IMMEDIATE = 3


BINDSPEED = tagBINDSPEED


class tagOLECONTF(ENUM):
    OLECONTF_EMBEDDINGS = 1
    OLECONTF_LINKS = 2
    OLECONTF_OTHERS = 4
    OLECONTF_ONLYUSER = 8
    OLECONTF_ONLYIFRUNNING = 16


OLECONTF = tagOLECONTF


IOleItemContainer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetObject',
        (['in'], LPOLESTR, 'pszItem'),
        (['in'], DWORD, 'dwSpeedNeeded'),
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetObjectStorage',
        (['in'], LPOLESTR, 'pszItem'),
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvStorage'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsRunning',
        (['in'], LPOLESTR, 'pszItem'),
    ),
]


LPOLEINPLACEUIWINDOW = POINTER(IOleInPlaceUIWindow)
BORDERWIDTHS = RECT
LPBORDERWIDTHS = LPRECT
LPCBORDERWIDTHS = LPCRECT


IOleInPlaceUIWindow._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetBorder',
        (['out'], LPRECT, 'lprectBorder'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RequestBorderSpace',
        (['in'], LPCBORDERWIDTHS, 'pborderwidths'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetBorderSpace',
        (['in'], LPCBORDERWIDTHS, 'pborderwidths'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetActiveObject',
        (['in'], POINTER(IOleInPlaceActiveObject), 'pActiveObject'),
        (['in'], LPCOLESTR, 'pszObjName'),
    ),
]


LPOLEINPLACEACTIVEOBJECT = POINTER(IOleInPlaceActiveObject)


IOleInPlaceActiveObject._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'TranslateAccelerator',
        (['in'], LPMSG, 'lpmsg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnFrameWindowActivate',
        (['in'], BOOL, 'fActivate'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnDocWindowActivate',
        (['in'], BOOL, 'fActivate'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ResizeBorder',
        (['in'], LPCRECT, 'prcBorder'),
        (['in'], POINTER(IOleInPlaceUIWindow), 'pUIWindow'),
        (['in'], BOOL, 'fFrameWindow'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnableModeless',
        (['in'], BOOL, 'fEnable'),
    ),
]


LPOLEINPLACEFRAME = POINTER(IOleInPlaceFrame)



class tagOIFI(ctypes.Structure):
    _fields_ = [
        ('cb', UINT),
        ('fMDIApp', BOOL),
        ('hwndFrame', HWND),
        ('haccel', HACCEL),
        ('cAccelEntries', UINT),
    ]


OLEINPLACEFRAMEINFO = tagOIFI
LPOLEINPLACEFRAMEINFO = POINTER(tagOIFI)


class tagOleMenuGroupWidths(ctypes.Structure):
    _fields_ = [
        ('width', LONG * 6),
    ]


OLEMENUGROUPWIDTHS = tagOleMenuGroupWidths
LPOLEMENUGROUPWIDTHS = POINTER(tagOleMenuGroupWidths)

HOLEMENU = HGLOBAL


IOleInPlaceFrame._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'InsertMenus',
        (['in'], HMENU, 'hmenuShared'),
        (['in', 'out'], LPOLEMENUGROUPWIDTHS, 'lpMenuWidths'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMenu',
        (['in'], HMENU, 'hmenuShared'),
        (['in'], HOLEMENU, 'holemenu'),
        (['in'], HWND, 'hwndActiveObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveMenus',
        (['in'], HMENU, 'hmenuShared'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetStatusText',
        (['in'], LPCOLESTR, 'pszStatusText'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnableModeless',
        (['in'], BOOL, 'fEnable'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'TranslateAccelerator',
        (['in'], LPMSG, 'lpmsg'),
        (['in'], WORD, 'wID'),
    ),
]


LPOLEINPLACEOBJECT = POINTER(IOleInPlaceObject)


IOleInPlaceObject._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetObjectRects',
        (['in'], LPCRECT, 'lprcPosRect'),
        (['in'], LPCRECT, 'lprcClipRect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReactivateAndUndo'
    ),
]


LPOLEINPLACESITE = POINTER(IOleInPlaceSite)


IOleInPlaceSite._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetWindowContext',
        (['out'], POINTER(POINTER(IOleInPlaceFrame)), 'ppFrame'),
        (['out'], POINTER(POINTER(IOleInPlaceUIWindow)), 'ppDoc'),
        (['out'], LPRECT, 'lprcPosRect'),
        (['out'], LPRECT, 'lprcClipRect'),
        (['in', 'out'], LPOLEINPLACEFRAMEINFO, 'lpFrameInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Scroll',
        (['in'], SIZE, 'scrollExtant'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnUIDeactivate',
        (['in'], BOOL, 'fUndoable'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnPosRectChange',
        (['in'], LPCRECT, 'lprcPosRect'),
    ),
]


IContinue._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'FContinue'
    ),
]


LPVIEWOBJECT = POINTER(IViewObject)


IViewObject._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Draw',
        (['in'], DWORD, 'dwDrawAspect'),
        (['in'], LONG, 'lindex'),
        (['in'], POINTER(VOID), 'pvAspect'),
        (['in'], POINTER(DVTARGETDEVICE), 'ptd'),
        (['in'], HDC, 'hdcTargetDev'),
        (['in'], HDC, 'hdcDraw'),
        (['in'], LPCRECTL, 'lprcBounds'),
        (['in'], LPCRECTL, 'lprcWBounds'),
        (['in'], ULONG_PTR, 'dwContinue)'),
        (['in'], ULONG_PTR, 'dwContinue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetColorSet',
        (['in'], DWORD, 'dwDrawAspect'),
        (['in'], LONG, 'lindex'),
        (['in'], POINTER(VOID), 'pvAspect'),
        (['in'], POINTER(DVTARGETDEVICE), 'ptd'),
        (['in'], HDC, 'hicTargetDev'),
        (['out'], POINTER(POINTER(LOGPALETTE)), 'ppColorSet'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Freeze',
        (['in'], DWORD, 'dwDrawAspect'),
        (['in'], LONG, 'lindex'),
        (['in'], POINTER(VOID), 'pvAspect'),
        (['out'], POINTER(DWORD), 'pdwFreeze'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Unfreeze',
        (['in'], DWORD, 'dwFreeze'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetAdvise',
        (['in'], DWORD, 'aspects'),
        (['in'], DWORD, 'advf'),
        (['in'], POINTER(IAdviseSink), 'pAdvSink'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAdvise',
        (['out'], POINTER(DWORD), 'pAspects'),
        (['out'], POINTER(DWORD), 'pAdvf'),
        (['out'], POINTER(POINTER(IAdviseSink)), 'ppAdvSink'),
    ),
]


LPVIEWOBJECT2 = POINTER(IViewObject2)


IViewObject2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetExtent',
        (['in'], DWORD, 'dwDrawAspect'),
        (['in'], LONG, 'lindex'),
        (['in'], POINTER(DVTARGETDEVICE), 'ptd'),
        (['out'], LPSIZEL, 'lpsizel'),
    ),
]


LPDROPSOURCE = POINTER(IDropSource)


IDropSource._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryContinueDrag',
        (['in'], BOOL, 'fEscapePressed'),
        (['in'], DWORD, 'grfKeyState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GiveFeedback',
        (['in'], DWORD, 'dwEffect'),
    ),
]


LPDROPTARGET = POINTER(IDropTarget)
MK_ALT = 0x20
DROPEFFECT_NONE = 0x0
DROPEFFECT_COPY = 0x1
DROPEFFECT_MOVE = 0x2
DROPEFFECT_LINK = 0x4
DROPEFFECT_SCROLL = 0x80000000
# default inset-width of the hot zone, in pixels
# typical use: GetProfileInt("windows","DragScrollInset",DD_DEFSCROLLINSET)
DD_DEFSCROLLINSET = 0xB
# default delay before scrolling, in milliseconds
# typical use: GetProfileInt("windows","DragScrollDelay",DD_DEFSCROLLDELAY)
DD_DEFSCROLLDELAY = 0x32
# default scroll INTerval, in milliseconds
# typical use: GetProfileInt("windows","DragScrollInterval",
# DD_DEFSCROLLINTERVAL)
DD_DEFSCROLLINTERVAL = 0x32
# default delay before dragging should start, in milliseconds
# typical use: GetProfileInt("windows", "DragDelay", DD_DEFDRAGDELAY)
DD_DEFDRAGDELAY = 0xC8
# default minimum distance (radius) before dragging should start, in pixels
# typical use: GetProfileInt("windows", "DragMinDist", DD_DEFDRAGMINDIST)
DD_DEFDRAGMINDIST = 0x2


IDropTarget._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DragEnter',
        (['in'], POINTER(IDataObject), 'pDataObj'),
        (['in'], DWORD, 'grfKeyState'),
        (['in'], POINTL, 'pt'),
        (['in', 'out'], POINTER(DWORD), 'pdwEffect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DragOver',
        (['in'], DWORD, 'grfKeyState'),
        (['in'], POINTL, 'pt'),
        (['in', 'out'], POINTER(DWORD), 'pdwEffect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Drop',
        (['in'], POINTER(IDataObject), 'pDataObj'),
        (['in'], DWORD, 'grfKeyState'),
        (['in'], POINTL, 'pt'),
        (['in', 'out'], POINTER(DWORD), 'pdwEffect'),
    ),
]


IDropSourceNotify._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DragEnterTarget',
        (['in'], HWND, 'hwndTarget'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DragLeaveTarget'
    ),
]


IEnterpriseDropTarget._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetDropSourceEnterpriseId',
        (['in'], LPCWSTR, 'identity'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsEvaluatingEdpPolicy',
        (['out', 'retval'], POINTER(BOOL), 'value'),
    ),
]


CFSTR_ENTERPRISE_ID = TEXT("EnterpriseDataProtectionId")


class tagOLEVERB(ctypes.Structure):
    _fields_ = [
        ('lVerb', LONG),
        ('lpszVerbName', LPOLESTR),
        ('fuFlags', DWORD),
        ('grfAttribs', DWORD),
    ]


OLEVERB = tagOLEVERB
LPOLEVERB = POINTER(tagOLEVERB)


class tagOLEVERBATTRIB(ENUM):
    OLEVERBATTRIB_NEVERDIRTIES = 1
    OLEVERBATTRIB_ONCONTAINERMENU = 2


OLEVERBATTRIB = tagOLEVERBATTRIB

LPENUMOLEVERB = POINTER(IEnumOLEVERB)


IEnumOLEVERB._methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Next',
            (['in'], ULONG, 'celt'),
            ([], LPOLEVERB, 'rgelt'),
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
            (['out'], POINTER(POINTER(IEnumOLEVERB)), 'ppenum'),
        ),
    ]


__all__ = (
    'IViewObject2', 'IOleItemContainer', 'IOleInPlaceUIWindow', 'IOleCache2',
    'IEnterpriseDropTarget', 'IEnumOLEVERB', 'IDropSource', 'IOleClientSite',
    'IOleInPlaceFrame', 'IContinue', 'IOleAdviseHolder', 'IDropSourceNotify',
    'IOleContainer', 'IOleCacheControl', 'IOleObject', 'IOleInPlaceSite',
    'IOleCache', 'IOleLink', 'IOleWindow', 'IDropTarget', 'IViewObject',
    'IOleInPlaceObject', 'IParseDisplayName', 'IOleInPlaceActiveObject',
    'UPDFCACHE_NORMALCACHE', 'DROPEFFECT_MOVE', 'UPDFCACHE_ALL', 'MK_ALT',
    'UPDFCACHE_ONSAVECACHE', 'DROPEFFECT_NONE', 'DROPEFFECT_LINK', 'tagOIFI',
    'DD_DEFSCROLLINSET', 'UPDFCACHE_ALLBUTNODATACACHE', 'DD_DEFDRAGMINDIST',
    'DD_DEFDRAGDELAY', 'DD_DEFSCROLLDELAY', '__REQUIRED_RPCNDR_H_VERSION__',
    'DD_DEFSCROLLINTERVAL', 'DROPEFFECT_COPY', 'UPDFCACHE_ONLYIFBLANK',
    'UPDFCACHE_NODATACACHE', 'DROPEFFECT_SCROLL', 'CFSTR_ENTERPRISE_ID',
    'UPDFCACHE_ONSTOPCACHE', 'UPDFCACHE_IFBLANKORONSAVECACHE', 'tagOLEUPDATE',
    '__REQUIRED_RPCSAL_H_VERSION__', 'UPDFCACHE_IFBLANK', 'tagOLEGETMONIKER',
    'tagDISCARDCACHE', 'tagOLEWHICHMK', 'tagBINDSPEED', 'tagOLELINKBIND',
    'tagUSERCLASSTYPE', 'tagOLECLOSE', 'tagOLECONTF', 'tagOLEMISC',
    'tagOLERENDER', 'tagOLEVERBATTRIB', 'tagOBJECTDESCRIPTOR', 'tagOLEVERB',
    'tagOleMenuGroupWidths', 'LPOLEINPLACEACTIVEOBJECT', 'LPOLECACHE2',
    'LPOLEINPLACESITE', 'LPOLECACHECONTROL', 'LPOLEOBJECT', 'LPOLECACHE',
    'BORDERWIDTHS', 'LPDROPTARGET', 'HOLEMENU', 'LPDROPSOURCE', 'POLEUPDATE',
    'LPVIEWOBJECT', 'LPOLERENDER', 'LPOLEWINDOW', 'LPOLEADVISEHOLDER',
    'LPBORDERWIDTHS', 'LPVIEWOBJECT2', 'LPCBORDERWIDTHS', 'LPOLELINK',
    'LPOLEINPLACEUIWINDOW', 'LPOLEITEMCONTAINER', 'LPOLEINPLACEFRAME',
    'LPOLEINPLACEOBJECT', 'LPOLECONTAINER', 'LPPARSEDISPLAYNAME',
    'LPENUMOLEVERB', 'LPOLEUPDATE', 'LPOLECLIENTSITE',
)
