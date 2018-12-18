import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_INC_OLE = None
WIN16 = None
WINAPI = None
STRICT = None
OLE_INTERNAL = None
SERVERONLY = None

class _OLETARGETDEVICE(ctypes.Structure):
    pass


OLETARGETDEVICE = _OLETARGETDEVICE


class _OLEOBJECTVTBL(ctypes.Structure):
    pass


OLEOBJECTVTBL = _OLEOBJECTVTBL


class _OLEOBJECT(ctypes.Structure):
    pass


OLEOBJECT = _OLEOBJECT


class _OLECLIENTVTBL(ctypes.Structure):
    pass


OLECLIENTVTBL = _OLECLIENTVTBL


class _OLECLIENT(ctypes.Structure):
    pass


OLECLIENT = _OLECLIENT


class _OLESTREAMVTBL(ctypes.Structure):
    pass


OLESTREAMVTBL = _OLESTREAMVTBL


class _OLESTREAM(ctypes.Structure):
    pass


OLESTREAM = _OLESTREAM


class _OLESERVERVTBL(ctypes.Structure):
    pass


OLESERVERVTBL = _OLESERVERVTBL


class _OLESERVER(ctypes.Structure):
    pass


OLESERVER = _OLESERVER


class _OLESERVERDOCVTBL(ctypes.Structure):
    pass


OLESERVERDOCVTBL = _OLESERVERDOCVTBL


class _OLESERVERDOC(ctypes.Structure):
    pass


OLESERVERDOC = _OLESERVERDOC



from winapifamily_h import * # NOQA

# ***************************************************************************\
# * ole.h - Object Linking and Embedding functions, types, and definitions*
# * Version 1.0 * * NOTE: windows.h must be included first * * Copyright (c)
# Microsoft Corporation. All rights reserved. * *
# \***************************************************************************
if not defined(_INC_OLE):
    _INC_OLE = VOID
    if _MSC_VER > 1000:
        pass
    # END IF


    if defined(WIN16):
        # Assume byte packing throughout
        from pyWinAPI.shared.pshpack1_h import * # NOQA
    # END IF


    if defined(__cplusplus):
        # Assume C declarations for C + +    # END IF  __cplusplus
    if not defined(WINAPI):
        WINAPI = VOID
        CALLBACK = VOID
        LPCSTR = LPSTR
        LRESULT = LONG_PTR
        HGLOBAL = HANDLE
    # END IF  _INC_WINDOWS

    if defined(STRICT):
        OLE_LPCSTR = LPCSTR
        OLE_CONST = VOID
    else:
        OLE_LPCSTR = LPSTR
        OLE_CONST = VOID
    # END IF  not STRICT

    LRESULT = LONG_PTR
    HGLOBAL = HANDLE

    # Object types
    OT_LINK = 1
    OT_EMBEDDED = 2
    OT_STATIC = 3

    # activate verbs
    OLEVERB_PRIMARY = 0

    # target device info structure
    _OLETARGETDEVICE._fields_ = [
        ('otdDeviceNameOffset', USHORT),
        ('otdDriverNameOffset', USHORT),
        ('otdPortNameOffset', USHORT),
        ('otdExtDevmodeOffset', USHORT),
        ('otdExtDevmodeSize', USHORT),
        ('otdEnvironmentOffset', USHORT),
        ('otdEnvironmentSize', USHORT),
        ('otdData', BYTE * 1),
    ]
    LPOLETARGETDEVICE = POINTER(OLETARGETDEVICE)

    # flags used in some methods
    OF_SET = 0x0001
    OF_GET = 0x0002
    OF_HANDLER = 0x0004

    # return codes for OLE functions
    class OLESTATUS(ENUM):
        OLE_OK = 1
        OLE_WAIT_FOR_RELEASE = 2
        OLE_BUSY = 3
        OLE_ERROR_PROTECT_ONLY = 4
        OLE_ERROR_MEMORY = 5
        OLE_ERROR_STREAM = 6
        OLE_ERROR_STATIC = 7
        OLE_ERROR_BLANK = 8
        OLE_ERROR_DRAW = 9
        OLE_ERROR_METAFILE = 10
        OLE_ERROR_ABORT = 11
        OLE_ERROR_CLIPBOARD = 12
        OLE_ERROR_FORMAT = 13
        OLE_ERROR_OBJECT = 14
        OLE_ERROR_OPTION = 15
        OLE_ERROR_PROTOCOL = 16
        OLE_ERROR_ADDRESS = 17
        OLE_ERROR_NOT_EQUAL = 18
        OLE_ERROR_HANDLE = 19
        OLE_ERROR_GENERIC = 20
        OLE_ERROR_CLASS = 21
        OLE_ERROR_SYNTAX = 22
        OLE_ERROR_DATATYPE = 23
        OLE_ERROR_PALETTE = 24
        OLE_ERROR_NOT_LINK = 25
        OLE_ERROR_NOT_EMPTY = 26
        OLE_ERROR_SIZE = 27
        OLE_ERROR_DRIVE = 28
        OLE_ERROR_NETWORK = 29
        OLE_ERROR_NAME = 30
        OLE_ERROR_TEMPLATE = 31
        OLE_ERROR_NEW = 32
        OLE_ERROR_EDIT = 33
        OLE_ERROR_OPEN = 34
        OLE_ERROR_NOT_OPEN = 35
        OLE_ERROR_LAUNCH = 36
        OLE_ERROR_COMM = 37
        OLE_ERROR_TERMINATE = 38
        OLE_ERROR_COMMAND = 39
        OLE_ERROR_SHOW = 40
        OLE_ERROR_DOVERB = 41
        OLE_ERROR_ADVISE_NATIVE = 42
        OLE_ERROR_ADVISE_PICT = 43
        OLE_ERROR_ADVISE_RENAME = 44
        OLE_ERROR_POKE_NATIVE = 45
        OLE_ERROR_REQUEST_NATIVE = 46
        OLE_ERROR_REQUEST_PICT = 47
        OLE_ERROR_SERVER_BLOCKED = 48
        OLE_ERROR_REGISTRATION = 49
        OLE_ERROR_ALREADY_REGISTERED = 50
        OLE_ERROR_TASK = 51
        OLE_ERROR_OUTOFDATE = 52
        OLE_ERROR_CANT_UPDATE_CLIENT = 53
        OLE_ERROR_UPDATE = 54
        OLE_ERROR_SETDATA_FORMAT = 55
        OLE_ERROR_STATIC_FROM_OTHER_OS = 56
        OLE_ERROR_FILE_VER = 57
        OLE_WARN_DELETE_DATA = 1000

    OLE_OK = OLESTATUS.OLE_OK
    OLE_WAIT_FOR_RELEASE = OLESTATUS.OLE_WAIT_FOR_RELEASE
    OLE_BUSY = OLESTATUS.OLE_BUSY
    OLE_ERROR_PROTECT_ONLY = OLESTATUS.OLE_ERROR_PROTECT_ONLY
    OLE_ERROR_MEMORY = OLESTATUS.OLE_ERROR_MEMORY
    OLE_ERROR_STREAM = OLESTATUS.OLE_ERROR_STREAM
    OLE_ERROR_STATIC = OLESTATUS.OLE_ERROR_STATIC
    OLE_ERROR_BLANK = OLESTATUS.OLE_ERROR_BLANK
    OLE_ERROR_DRAW = OLESTATUS.OLE_ERROR_DRAW
    OLE_ERROR_METAFILE = OLESTATUS.OLE_ERROR_METAFILE
    OLE_ERROR_ABORT = OLESTATUS.OLE_ERROR_ABORT
    OLE_ERROR_CLIPBOARD = OLESTATUS.OLE_ERROR_CLIPBOARD
    OLE_ERROR_FORMAT = OLESTATUS.OLE_ERROR_FORMAT
    OLE_ERROR_OBJECT = OLESTATUS.OLE_ERROR_OBJECT
    OLE_ERROR_OPTION = OLESTATUS.OLE_ERROR_OPTION
    OLE_ERROR_PROTOCOL = OLESTATUS.OLE_ERROR_PROTOCOL
    OLE_ERROR_ADDRESS = OLESTATUS.OLE_ERROR_ADDRESS
    OLE_ERROR_NOT_EQUAL = OLESTATUS.OLE_ERROR_NOT_EQUAL
    OLE_ERROR_HANDLE = OLESTATUS.OLE_ERROR_HANDLE
    OLE_ERROR_GENERIC = OLESTATUS.OLE_ERROR_GENERIC
    OLE_ERROR_CLASS = OLESTATUS.OLE_ERROR_CLASS
    OLE_ERROR_SYNTAX = OLESTATUS.OLE_ERROR_SYNTAX
    OLE_ERROR_DATATYPE = OLESTATUS.OLE_ERROR_DATATYPE
    OLE_ERROR_PALETTE = OLESTATUS.OLE_ERROR_PALETTE
    OLE_ERROR_NOT_LINK = OLESTATUS.OLE_ERROR_NOT_LINK
    OLE_ERROR_NOT_EMPTY = OLESTATUS.OLE_ERROR_NOT_EMPTY
    OLE_ERROR_SIZE = OLESTATUS.OLE_ERROR_SIZE
    OLE_ERROR_DRIVE = OLESTATUS.OLE_ERROR_DRIVE
    OLE_ERROR_NETWORK = OLESTATUS.OLE_ERROR_NETWORK
    OLE_ERROR_NAME = OLESTATUS.OLE_ERROR_NAME
    OLE_ERROR_TEMPLATE = OLESTATUS.OLE_ERROR_TEMPLATE
    OLE_ERROR_NEW = OLESTATUS.OLE_ERROR_NEW
    OLE_ERROR_EDIT = OLESTATUS.OLE_ERROR_EDIT
    OLE_ERROR_OPEN = OLESTATUS.OLE_ERROR_OPEN
    OLE_ERROR_NOT_OPEN = OLESTATUS.OLE_ERROR_NOT_OPEN
    OLE_ERROR_LAUNCH = OLESTATUS.OLE_ERROR_LAUNCH
    OLE_ERROR_COMM = OLESTATUS.OLE_ERROR_COMM
    OLE_ERROR_TERMINATE = OLESTATUS.OLE_ERROR_TERMINATE
    OLE_ERROR_COMMAND = OLESTATUS.OLE_ERROR_COMMAND
    OLE_ERROR_SHOW = OLESTATUS.OLE_ERROR_SHOW
    OLE_ERROR_DOVERB = OLESTATUS.OLE_ERROR_DOVERB
    OLE_ERROR_ADVISE_NATIVE = OLESTATUS.OLE_ERROR_ADVISE_NATIVE
    OLE_ERROR_ADVISE_PICT = OLESTATUS.OLE_ERROR_ADVISE_PICT
    OLE_ERROR_ADVISE_RENAME = OLESTATUS.OLE_ERROR_ADVISE_RENAME
    OLE_ERROR_POKE_NATIVE = OLESTATUS.OLE_ERROR_POKE_NATIVE
    OLE_ERROR_REQUEST_NATIVE = OLESTATUS.OLE_ERROR_REQUEST_NATIVE
    OLE_ERROR_REQUEST_PICT = OLESTATUS.OLE_ERROR_REQUEST_PICT
    OLE_ERROR_SERVER_BLOCKED = OLESTATUS.OLE_ERROR_SERVER_BLOCKED
    OLE_ERROR_REGISTRATION = OLESTATUS.OLE_ERROR_REGISTRATION
    OLE_ERROR_ALREADY_REGISTERED = OLESTATUS.OLE_ERROR_ALREADY_REGISTERED
    OLE_ERROR_TASK = OLESTATUS.OLE_ERROR_TASK
    OLE_ERROR_OUTOFDATE = OLESTATUS.OLE_ERROR_OUTOFDATE
    OLE_ERROR_CANT_UPDATE_CLIENT = OLESTATUS.OLE_ERROR_CANT_UPDATE_CLIENT
    OLE_ERROR_UPDATE = OLESTATUS.OLE_ERROR_UPDATE
    OLE_ERROR_SETDATA_FORMAT = OLESTATUS.OLE_ERROR_SETDATA_FORMAT
    OLE_ERROR_STATIC_FROM_OTHER_OS = OLESTATUS.OLE_ERROR_STATIC_FROM_OTHER_OS
    OLE_ERROR_FILE_VER = OLESTATUS.OLE_ERROR_FILE_VER
    OLE_WARN_DELETE_DATA = OLESTATUS.OLE_WARN_DELETE_DATA

    # Codes for CallBack events
    class OLE_NOTIFICATION(ENUM):
        OLE_CHANGED = 1
        OLE_SAVED = 2
        OLE_CLOSED = 3
        OLE_RENAMED = 4
        OLE_QUERY_PAINT = 5
        OLE_RELEASE = 6
        OLE_QUERY_RETRY = 7

    OLE_CHANGED = OLE_NOTIFICATION.OLE_CHANGED
    OLE_SAVED = OLE_NOTIFICATION.OLE_SAVED
    OLE_CLOSED = OLE_NOTIFICATION.OLE_CLOSED
    OLE_RENAMED = OLE_NOTIFICATION.OLE_RENAMED
    OLE_QUERY_PAINT = OLE_NOTIFICATION.OLE_QUERY_PAINT
    OLE_RELEASE = OLE_NOTIFICATION.OLE_RELEASE
    OLE_QUERY_RETRY = OLE_NOTIFICATION.OLE_QUERY_RETRY


    class OLE_RELEASE_METHOD(ENUM):
        OLE_NONE = 1
        OLE_DELETE = 2
        OLE_LNKPASTE = 3
        OLE_EMBPASTE = 4
        OLE_SHOW = 5
        OLE_RUN = 6
        OLE_ACTIVATE = 7
        OLE_UPDATE = 8
        OLE_CLOSE = 9
        OLE_RECONNECT = 10
        OLE_SETUPDATEOPTIONS = 11
        OLE_SERVERUNLAUNCH = 12
        OLE_LOADFROMSTREAM = 13
        OLE_SETDATA = 14
        OLE_REQUESTDATA = 15
        OLE_OTHER = 16
        OLE_CREATE = 17
        OLE_CREATEFROMTEMPLATE = 18
        OLE_CREATELINKFROMFILE = 19
        OLE_COPYFROMLNK = 20
        OLE_CREATEFROMFILE = 21
        OLE_CREATEINVISIBLE = 22

    OLE_NONE = OLE_RELEASE_METHOD.OLE_NONE
    OLE_DELETE = OLE_RELEASE_METHOD.OLE_DELETE
    OLE_LNKPASTE = OLE_RELEASE_METHOD.OLE_LNKPASTE
    OLE_EMBPASTE = OLE_RELEASE_METHOD.OLE_EMBPASTE
    OLE_SHOW = OLE_RELEASE_METHOD.OLE_SHOW
    OLE_RUN = OLE_RELEASE_METHOD.OLE_RUN
    OLE_ACTIVATE = OLE_RELEASE_METHOD.OLE_ACTIVATE
    OLE_UPDATE = OLE_RELEASE_METHOD.OLE_UPDATE
    OLE_CLOSE = OLE_RELEASE_METHOD.OLE_CLOSE
    OLE_RECONNECT = OLE_RELEASE_METHOD.OLE_RECONNECT
    OLE_SETUPDATEOPTIONS = OLE_RELEASE_METHOD.OLE_SETUPDATEOPTIONS
    OLE_SERVERUNLAUNCH = OLE_RELEASE_METHOD.OLE_SERVERUNLAUNCH
    OLE_LOADFROMSTREAM = OLE_RELEASE_METHOD.OLE_LOADFROMSTREAM
    OLE_SETDATA = OLE_RELEASE_METHOD.OLE_SETDATA
    OLE_REQUESTDATA = OLE_RELEASE_METHOD.OLE_REQUESTDATA
    OLE_OTHER = OLE_RELEASE_METHOD.OLE_OTHER
    OLE_CREATE = OLE_RELEASE_METHOD.OLE_CREATE
    OLE_CREATEFROMTEMPLATE = OLE_RELEASE_METHOD.OLE_CREATEFROMTEMPLATE
    OLE_CREATELINKFROMFILE = OLE_RELEASE_METHOD.OLE_CREATELINKFROMFILE
    OLE_COPYFROMLNK = OLE_RELEASE_METHOD.OLE_COPYFROMLNK
    OLE_CREATEFROMFILE = OLE_RELEASE_METHOD.OLE_CREATEFROMFILE
    OLE_CREATEINVISIBLE = OLE_RELEASE_METHOD.OLE_CREATEINVISIBLE

    # rendering options
    class OLEOPT_RENDER(ENUM):
        olerender_none = 1
        olerender_draw = 2
        olerender_format = 3

    olerender_none = OLEOPT_RENDER.olerender_none
    olerender_draw = OLEOPT_RENDER.olerender_draw
    olerender_format = OLEOPT_RENDER.olerender_format

    # standard clipboard format type
    OLECLIPFORMAT = WORD

    # Link update options
    class OLEOPT_UPDATE(ENUM):
        oleupdate_always = 1
        oleupdate_onsave = 2
        if defined(OLE_INTERNAL):
            oleupdate_oncall = 3
            oleupdate_onclose = 4
            else:
                oleupdate_oncall = 5
            # END IF

    oleupdate_always = OLEOPT_UPDATE.oleupdate_always
    oleupdate_onsave = OLEOPT_UPDATE.oleupdate_onsave
    if defined(OLE_INTERNAL):
        oleupdate_oncall = OLEOPT_UPDATE.oleupdate_oncall
        oleupdate_onclose = OLEOPT_UPDATE.oleupdate_onclose
        else:
            oleupdate_oncall = OLEOPT_UPDATE.oleupdate_oncall
        # END IF

    HOBJECT = HANDLE
    LHSERVER = LONG_PTR
    LHCLIENTDOC = LONG_PTR
    LHSERVERDOC = LONG_PTR
    LPOLEOBJECT = POINTER(_OLEOBJECT)
    LPOLESTREAM = POINTER(_OLESTREAM)
    LPOLECLIENT = POINTER(_OLECLIENT)

    QueryProtocol = CALLBACK(VOID, LPOLEOBJECT, OLE_LPCSTR)
    Release = CALLBACK(OLESTATUS, LPOLEOBJECT)
    Show = CALLBACK(OLESTATUS, LPOLEOBJECT, BOOL)
    DoVerb = CALLBACK(OLESTATUS, LPOLEOBJECT, UINT, BOOL, BOOL)
    GetData = CALLBACK(OLESTATUS, LPOLEOBJECT, OLECLIPFORMAT, HANDLE)
    SetData = CALLBACK(OLESTATUS, LPOLEOBJECT, OLECLIPFORMAT, HANDLE)
    SetTargetDevice = CALLBACK(OLESTATUS, LPOLEOBJECT, HGLOBAL)
    SetBounds = CALLBACK(OLESTATUS, LPOLEOBJECT, RECT)
    EnumFormats = CALLBACK(OLESTATUS, LPOLEOBJECT, OLECLIPFORMAT)
    SetColorScheme = CALLBACK(OLESTATUS, LPOLEOBJECT, LOGPALETTE)

    # object method table definitions.
    _TEMP__OLEOBJECTVTBL = [
        ('QueryProtocol', QueryProtocol),
        ('Release', Release),
        ('Show', Show),
        ('DoVerb', DoVerb),
        ('GetData', GetData),
        ('SetData', SetData),
        ('SetTargetDevice', SetTargetDevice),
        ('SetBounds', SetBounds),
        ('EnumFormats', EnumFormats),
        ('SetColorScheme', SetColorScheme),
    ]
    if not defined(SERVERONLY):
        Delete = CALLBACK(OLESTATUS, LPOLEOBJECT)
        SetHostNames = CALLBACK(OLESTATUS, LPOLEOBJECT, OLE_LPCSTR, OLE_LPCSTR)
        SaveToStream = CALLBACK(OLESTATUS, LPOLEOBJECT, LPOLESTREAM)
        Clone = CALLBACK(OLESTATUS, LPOLEOBJECT, LPOLECLIENT, LHCLIENTDOC, OLE_LPCSTR, LPOLEOBJECT)
        CopyFromLink = CALLBACK(OLESTATUS, LPOLEOBJECT, LPOLECLIENT, LHCLIENTDOC, OLE_LPCSTR, LPOLEOBJECT)
        Equal = (OLESTATUS, LPOLEOBJECT, LPOLEOBJECT)
        CopyToClipboard = CALLBACK(OLESTATUS, LPOLEOBJECT)
        Draw = CALLBACK(OLESTATUS, LPOLEOBJECT, HDC, RECT, RECT, HDC)
        Activate = CALLBACK(LPOLEOBJECT, UINT, BOOL, BOOL, HWND, RECT)
        Execute = CALLBACK(OLESTATUS, LPOLEOBJECT, HGLOBAL, UINT)
        Close = CALLBACK(OLESTATUS, LPOLEOBJECT)
        Update = CALLBACK(OLESTATUS, LPOLEOBJECT)
        Reconnect = CALLBACK(OLESTATUS, LPOLEOBJECT)
        ObjectConvert = CALLBACK(OLESTATUS, LPOLEOBJECT, OLE_LPCSTR, LPOLECLIENT, LHCLIENTDOC, OLE_LPCSTR, LPOLEOBJECT)
        GetLinkUpdateOptions = CALLBACK(OLESTATUS, LPOLEOBJECT, OLEOPT_UPDATE)
        SetLinkUpdateOptions = CALLBACK(OLESTATUS, LPOLEOBJECT, OLEOPT_UPDATE)
        Rename = CALLBACK(OLESTATUS, LPOLEOBJECT, OLE_LPCSTR)
        QueryName = CALLBACK(OLESTATUS, LPOLEOBJECT, LPSTR, UINT)
        QueryType = CALLBACK(OLESTATUS, LPOLEOBJECT, LONG)
        QueryBounds = CALLBACK(OLESTATUS, LPOLEOBJECT, RECT)
        QuerySize = CALLBACK(OLESTATUS, LPOLEOBJECT, DWORD)
        QueryOpen = CALLBACK(OLESTATUS, LPOLEOBJECT)
        QueryOutOfDate = CALLBACK(OLESTATUS, LPOLEOBJECT)
        QueryReleaseStatus = CALLBACK(OLESTATUS, LPOLEOBJECT)
        QueryReleaseError = CALLBACK(OLESTATUS, LPOLEOBJECT)
        QueryReleaseMethod = CALLBACK(OLE_RELEASE_METHOD, LPOLEOBJECT)
        RequestData = CALLBACK(OLESTATUS, LPOLEOBJECT, OLECLIPFORMAT)
        ObjectLong = CALLBACK(OLESTATUS, LPOLEOBJECT, UINT, LONG)
        ChangeData = CALLBACK(OLESTATUS, LPOLEOBJECT, HANDLE, LPOLECLIENT, BOOL)

        _TEMP__OLEOBJECTVTBL += [
            # Extra methods required for client.
            ('Delete', Delete),
            ('SetHostNames', SetHostNames),
            ('SaveToStream', SaveToStream),
            ('Clone', Clone),
            ('CopyFromLink', CopyFromLink),
            ('Equal', Equal),
            ('CopyToClipboard', CopyToClipboard),
            ('Draw', Draw),
            ('Activate', Activate),
            ('Execute', Execute),
            ('Close', Close),
            ('Update', Update),
            ('Reconnect', Reconnect),
            ('ObjectConvert', ObjectConvert),
            ('GetLinkUpdateOptions', GetLinkUpdateOptions),
            ('SetLinkUpdateOptions', SetLinkUpdateOptions),
            ('Rename', Rename),
            ('QueryName', QueryName),
            ('QueryType', QueryType),
            ('QueryBounds', QueryBounds),
            ('QuerySize', QuerySize),
            ('QueryOpen', QueryOpen),
            ('QueryOutOfDate', QueryOutOfDate),
            ('QueryReleaseStatus', QueryReleaseStatus),
            ('QueryReleaseError', QueryReleaseError),
            ('QueryReleaseMethod', QueryReleaseMethod),
            ('RequestData', RequestData),
            ('ObjectLong', ObjectLong),
            # This method is internal only
            ('ChangeData', ChangeData),
        ]
        # END IF   not SERVERONLY


    _OLEOBJECTVTBL._fields_ = _TEMP__OLEOBJECTVTBL
    LPOLEOBJECTVTBL = POINTER(OLEOBJECTVTBL)

    if not defined(OLE_INTERNAL):
        _OLEOBJECT._fields_ = [
            ('lpvtbl', LPOLEOBJECTVTBL),
        ]
    # END IF


    # ole client definitions
    _OLECLIENTVTBL._fields_ = [
        ('(CALLBACK* CallBack)(LPOLECLIENT', INT),
        ('OLE_NOTIFICATION', INT),
        ('LPOLEOBJECT)', INT),
    ]
    LPOLECLIENTVTBL = POINTER(OLECLIENTVTBL)

    _OLECLIENT._fields_ = [
        ('lpvtbl', LPOLECLIENTVTBL),
    ]

    # Stream definitions
    _OLESTREAMVTBL._fields_ = [
        ('(CALLBACK* Get)(LPOLESTREAM', DWORD),
        ('VOID FAR*', DWORD),
        ('DWORD)', DWORD),
        ('(CALLBACK* Put)(LPOLESTREAM', DWORD),
        ('OLE_CONST VOID FAR*', DWORD),
        ('DWORD)', DWORD),
    ]
    LPOLESTREAMVTBL = POINTER(OLESTREAMVTBL)

    _OLESTREAM._fields_ = [
        ('lpstbl', LPOLESTREAMVTBL),
    ]
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Public Function Prototypes
        ole32 = ctypes.windll.OLE32


        # OLESTATUS   WINAPI  OleSaveToStream(LPOLEOBJECT, LPOLESTREAM);
        OleSaveToStream = ole32.OleSaveToStream
        OleSaveToStream.restype = WINAPI


        # OLESTATUS   WINAPI  OleDraw(LPOLEOBJECT, HDC, RECT FAR*, RECT FAR*, HDC);
        OleDraw = ole32.OleDraw
        OleDraw.restype = WINAPI


        # Routines related to asynchronous operations.
        # LOWORD is major version, HIWORD is minor version
        # Converting to format (as in clipboard):
        # Query apis for creation from clipboard
        # Object creation functions
        # OLESTATUS   WINAPI  OleCreateFromFile(LPCSTR, LPOLECLIENT, LPCSTR, LPCSTR, LHCLIENTDOC, LPCSTR, LPOLEOBJECT FAR*, OLEOPT_RENDER, OLECLIPFORMAT);
        OleCreateFromFile = ole32.OleCreateFromFile
        OleCreateFromFile.restype = WINAPI


        # OLESTATUS   WINAPI  OleLoadFromStream(LPOLESTREAM, LPCSTR, LPOLECLIENT, LHCLIENTDOC, LPCSTR, LPOLEOBJECT FAR*);
        OleLoadFromStream = ole32.OleLoadFromStream
        OleLoadFromStream.restype = WINAPI


        # OLESTATUS   WINAPI  OleCreate(LPCSTR, LPOLECLIENT, LPCSTR, LHCLIENTDOC, LPCSTR, LPOLEOBJECT FAR*, OLEOPT_RENDER, OLECLIPFORMAT);
        OleCreate = ole32.OleCreate
        OleCreate.restype = WINAPI


        # client document API
        # server usage definitions
        class OLE_SERVER_USE(ENUM):
            OLE_SERVER_MULTI = 1
            OLE_SERVER_SINGLE = 2

        OLE_SERVER_MULTI = OLE_SERVER_USE.OLE_SERVER_MULTI
        OLE_SERVER_SINGLE = OLE_SERVER_USE.OLE_SERVER_SINGLE

        # Server API
        LPOLESERVER = POINTER()


        # APIs to keep server open
        # Server document API
        LPOLESERVERDOC = POINTER()

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)


    _OLESERVERVTBL._fields_ = [
        ('(CALLBACK* Open)  (LPOLESERVER', OLESTATUS),
        ('LHSERVERDOC', OLESTATUS),
        ('OLE_LPCSTR', OLESTATUS),
        ('LPOLESERVERDOC FAR*)', OLESTATUS),
        # place holder for returning oledoc.
        ('(CALLBACK* Create)(LPOLESERVER', OLESTATUS),
        # place holder for returning oledoc.
        ('LHSERVERDOC', OLESTATUS),
        # place holder for returning oledoc.
        ('OLE_LPCSTR', OLESTATUS),
        # place holder for returning oledoc.
        ('OLE_LPCSTR', OLESTATUS),
        # place holder for returning oledoc.
        ('LPOLESERVERDOC FAR*)', OLESTATUS),
        # place holder for returning oledoc.
        ('(CALLBACK* CreateFromTemplate)(LPOLESERVER', OLESTATUS),
        # place holder for returning oledoc.
        ('LHSERVERDOC', OLESTATUS),
        # place holder for returning oledoc.
        ('OLE_LPCSTR', OLESTATUS),
        # place holder for returning oledoc.
        ('OLE_LPCSTR', OLESTATUS),
        # place holder for returning oledoc.
        ('OLE_LPCSTR', OLESTATUS),
        # place holder for returning oledoc.
        ('LPOLESERVERDOC FAR*)', OLESTATUS),
        # place holder for returning oledoc.
        ('(CALLBACK* Edit)  (LPOLESERVER', OLESTATUS),
        # place holder for returning oledoc.
        ('LHSERVERDOC', OLESTATUS),
        # place holder for returning oledoc.
        ('OLE_LPCSTR', OLESTATUS),
        # place holder for returning oledoc.
        ('OLE_LPCSTR', OLESTATUS),
        # place holder for returning oledoc.
        ('LPOLESERVERDOC FAR*)', OLESTATUS),
        # place holder for returning oledoc.
        ('(CALLBACK* Exit)  (LPOLESERVER)', OLESTATUS),
        # lp OLESERVER
        ('(CALLBACK* Release)  (LPOLESERVER)', OLESTATUS),
        # lp OLESERVER
        ('(CALLBACK* Execute)(LPOLESERVER', OLESTATUS),
        # lp OLESERVER
        ('HGLOBAL)', OLESTATUS),
    ]
    LPOLESERVERVTBL = POINTER(OLESERVERVTBL)

    _OLESERVER._fields_ = [
        ('lpvtbl', LPOLESERVERVTBL),
    ]

    _OLESERVERDOCVTBL._fields_ = [
        ('(CALLBACK* Save)      (LPOLESERVERDOC)', OLESTATUS),
        ('(CALLBACK* Close)     (LPOLESERVERDOC)', OLESTATUS),
        ('(CALLBACK* SetHostNames)(LPOLESERVERDOC', OLESTATUS),
        ('OLE_LPCSTR', OLESTATUS),
        ('OLE_LPCSTR)', OLESTATUS),
        ('(CALLBACK* SetDocDimensions)(LPOLESERVERDOC', OLESTATUS),
        ('OLE_CONST RECT FAR*)', OLESTATUS),
        ('(CALLBACK* GetObject) (LPOLESERVERDOC', OLESTATUS),
        ('OLE_LPCSTR', OLESTATUS),
        ('LPOLEOBJECT FAR*', OLESTATUS),
        ('LPOLECLIENT)', OLESTATUS),
        ('(CALLBACK* Release)   (LPOLESERVERDOC)', OLESTATUS),
        ('(CALLBACK* SetColorScheme)(LPOLESERVERDOC', OLESTATUS),
        ('OLE_CONST LOGPALETTE FAR*)', OLESTATUS),
        ('(CALLBACK* Execute)  (LPOLESERVERDOC', OLESTATUS),
        ('HGLOBAL)', OLESTATUS),
    ]
    FAR*  LPOLESERVERDOCVTBL = OLESERVERDOCVTBL

    _OLESERVERDOC._fields_ = [
        ('lpvtbl', LPOLESERVERDOCVTBL),
    ]
    if defined(__cplusplus):
        pass
    # END IF  __cplusplus

    if defined(WIN16):
        from poppack_h import * # NOQA
    # END IF

# END IF  not _INC_OLE


