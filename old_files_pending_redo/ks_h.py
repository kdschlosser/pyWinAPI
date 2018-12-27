import ctypes
from .wtypes_h import (
    ENUM,
    ULONG,
    POINTER,
    PVOID,
    LONGLONG,
    ULONGLONG,
    LONG,
    ULONG_PTR,
    HANDLE,
    LONG_PTR,
    USHORT,
    VOID,
    WCHAR,
    LIST_ENTRY,
    SINGLE_LIST_ENTRY,
    UCHAR,
    NULL,
    BOOL,
    INT,
    NTSTATUS
)
from .guiddef_h import (
    GUID,
    DEFINE_GUID,
    DEFINE_GUIDSTRUCT,
    DEFINE_GUIDNAMED
)
from .devioctl_h1 import (
    CTL_CODE,
    FILE_DEVICE_KS,
    METHOD_NEITHER,
    FILE_ANY_ACCESS,
    FILE_READ_ACCESS,
    FILE_WRITE_ACCESS
)

from .basetsd_h import (
    KAFFINITY
)

from .winapifamily_h import * # NOQA

KPRIORITY = LONG
_KS_NO_ANONYMOUS_STRUCTURES_ = 0x00000001

WORKER_THREAD_ROUTINE = VOID
PWORKER_THREAD_ROUTINE = POINTER(WORKER_THREAD_ROUTINE)


class _WORK_QUEUE_TYPE(ENUM):
    CriticalWorkQueue = 0
    DelayedWorkQueue = 1
    HyperCriticalWorkQueue = 2
    NormalWorkQueue = 3
    BackgroundWorkQueue = 4
    RealTimeWorkQueue = 5
    SuperCriticalWorkQueue = 6
    MaximumWorkQueue = 7
    CustomPriorityWorkQueue = 32


WORK_QUEUE_TYPE = _WORK_QUEUE_TYPE


class  _WORK_QUEUE_ITEM(ctypes.Structure):
    _fields_ = [
        ('List', LIST_ENTRY),
        ('WorkerRoutine', PWORKER_THREAD_ROUTINE),
        ('Parameter', PVOID)
    ]


WORK_QUEUE_ITEM = _WORK_QUEUE_ITEM
PWORK_QUEUE_ITEM = POINTER(_WORK_QUEUE_ITEM)

# ===========================================================================
STATIC_GUID_NULL = (
    0x00000000,
    0x0000,
    0x0000,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
)
GUID_NULL = DEFINE_GUIDSTRUCT(
    "00000000-0000-0000-0000-000000000000"
)
GUID_NULL = DEFINE_GUIDNAMED(GUID_NULL)
# ===========================================================================
IOCTL_KS_PROPERTY = CTL_CODE(
    FILE_DEVICE_KS,
    0x00000000,
    METHOD_NEITHER,
    FILE_ANY_ACCESS,
)
IOCTL_KS_ENABLE_EVENT = CTL_CODE(
    FILE_DEVICE_KS,
    0x00000001,
    METHOD_NEITHER,
    FILE_ANY_ACCESS,
)
IOCTL_KS_DISABLE_EVENT = CTL_CODE(
    FILE_DEVICE_KS,
    0x00000002,
    METHOD_NEITHER,
    FILE_ANY_ACCESS,
)
IOCTL_KS_METHOD = CTL_CODE(
    FILE_DEVICE_KS,
    0x00000003,
    METHOD_NEITHER,
    FILE_ANY_ACCESS,
)
IOCTL_KS_WRITE_STREAM = CTL_CODE(
    FILE_DEVICE_KS,
    0x00000004,
    METHOD_NEITHER,
    FILE_WRITE_ACCESS,
)
IOCTL_KS_READ_STREAM = CTL_CODE(
    FILE_DEVICE_KS,
    0x00000005,
    METHOD_NEITHER,
    FILE_READ_ACCESS,
)
IOCTL_KS_RESET_STATE = CTL_CODE(
    FILE_DEVICE_KS,
    0x00000006,
    METHOD_NEITHER,
    FILE_ANY_ACCESS,
)


# ===========================================================================
class KSRESET(ENUM):
    KSRESET_BEGIN = 0
    KSRESET_END = 1


class KSSTATE(ENUM):
    KSSTATE_STOP = 0
    KSSTATE_ACQUIRE = 1
    KSSTATE_PAUSE = 2
    KSSTATE_RUN = 3


PKSSTATE = POINTER(KSSTATE)


KSPRIORITY_LOW = 0x00000001
KSPRIORITY_NORMAL = 0x40000000
KSPRIORITY_HIGH = 0x80000000
KSPRIORITY_EXCLUSIVE = 0x00000000FFFFFFFF


class KSPRIORITY(ctypes.Structure):
    _fields_ = [
        ('PriorityClass', ULONG),
        ('PrioritySubClass', ULONG),
    ]


class _KDPC(ctypes.Structure):
    class DUMMYUNIONNAME(ctypes.Union):
        class DUMMYSTRUCTNAME(ctypes.Structure):
            _fields_ = [
                ('Type', UCHAR),
                ('Importance', UCHAR),
                ('Number', USHORT)
            ]

        _fields_ = [
            ('TargetInfoAsUlong', ULONG),
            ('DUMMYSTRUCTNAME', DUMMYSTRUCTNAME)
        ]

    _fields_ = [
        ('DUMMYUNIONNAME', DUMMYUNIONNAME),
        ('DpcListEntry', SINGLE_LIST_ENTRY),
        ('ProcessorHistory', KAFFINITY),
        ('DeferredRoutine', VOID), # PKDEFERRED_ROUTINE
        ('DeferredContext', PVOID),
        ('SystemArgument1', PVOID),
        ('SystemArgument2', PVOID),
        ('DpcData', PVOID)
    ]


KDPC = _KDPC
PKDPC = POINTER(_KDPC)
PRKDPC = POINTER(_KDPC)


class KSIDENTIFIER(ctypes.Structure):

    class _Union(ctypes.Union):

        class _Struct(ctypes.Structure):
            _fields_ = [
                ('Set', GUID),
                ('Id', ULONG),
                ('Flags', ULONG)
            ]

        _anonymous_ = ('_Struct',)
        _fields_ = [
            ('_Struct', _Struct),
            ('Alignment', LONGLONG)
        ]

    _anonymous_ = ('_Union', )
    _fields_ = [
        ('_Union', _Union)
    ]


PKSIDENTIFIER = POINTER(KSIDENTIFIER)
PKSPRIORITY = POINTER(KSPRIORITY)
KSPROPERTY = KSIDENTIFIER
PKSPROPERTY = POINTER(KSIDENTIFIER)
KSMETHOD = KSIDENTIFIER
PKSMETHOD = POINTER(KSIDENTIFIER)
KSEVENT = KSIDENTIFIER
PKSEVENT = POINTER(KSIDENTIFIER)
KSMETHOD_TYPE_NONE = 0x00000000
KSMETHOD_TYPE_READ = 0x00000001
KSMETHOD_TYPE_WRITE = 0x00000002
KSMETHOD_TYPE_MODIFY = 0x00000003
KSMETHOD_TYPE_SOURCE = 0x00000004
KSMETHOD_TYPE_SEND = 0x00000001
KSMETHOD_TYPE_SETSUPPORT = 0x00000100
KSMETHOD_TYPE_BASICSUPPORT = 0x00000200
KSMETHOD_TYPE_TOPOLOGY = 0x10000000
KSPROPERTY_TYPE_GET = 0x00000001
KSPROPERTY_TYPE_GETPAYLOADSIZE = 0x00000004
KSPROPERTY_TYPE_SET = 0x00000002
KSPROPERTY_TYPE_SETSUPPORT = 0x00000100
KSPROPERTY_TYPE_BASICSUPPORT = 0x00000200
KSPROPERTY_TYPE_RELATIONS = 0x00000400
KSPROPERTY_TYPE_SERIALIZESET = 0x00000800
KSPROPERTY_TYPE_UNSERIALIZESET = 0x00001000
KSPROPERTY_TYPE_SERIALIZERAW = 0x00002000
KSPROPERTY_TYPE_UNSERIALIZERAW = 0x00004000
KSPROPERTY_TYPE_SERIALIZESIZE = 0x00008000
KSPROPERTY_TYPE_DEFAULTVALUES = 0x00010000
KSPROPERTY_TYPE_TOPOLOGY = 0x10000000
KSPROPERTY_TYPE_HIGHPRIORITY = 0x08000000
KSPROPERTY_TYPE_FSFILTERSCOPE = 0x40000000
KSPROPERTY_TYPE_COPYPAYLOAD = 0x80000000


class KSP_NODE(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('NodeId', ULONG),
        ('Reserved', ULONG)
    ]


PKSP_NODE = POINTER(KSP_NODE)


class KSM_NODE(ctypes.Structure):
    _fields_ = [
        ('Method', KSMETHOD),
        ('NodeId', ULONG),
        ('Reserved', ULONG)
    ]


PKSM_NODE = POINTER(KSM_NODE)


class KSE_NODE(ctypes.Structure):
    _fields_ = [
        ('Event', KSEVENT),
        ('NodeId', ULONG),
        ('Reserved', ULONG)
    ]


PKSE_NODE = POINTER(KSE_NODE)



STATIC_KSPROPTYPESETID_General = (
    0x97E99BA0,
    0xBDEA,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSPROPTYPESETID_General = DEFINE_GUIDSTRUCT(
    "97E99BA0-BDEA-11CF-A5D6-28DB04C10000"
)
KSPROPTYPESETID_General = DEFINE_GUIDNAMED(KSPROPTYPESETID_General)


class KSMULTIPLE_ITEM(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('Count', ULONG)
    ]


PKSMULTIPLE_ITEM = POINTER(KSMULTIPLE_ITEM)


class KSPROPERTY_DESCRIPTION(ctypes.Structure):
    _fields_ = [
        ('AccessFlags', ULONG),
        ('DescriptionSize', ULONG),
        ('PropTypeSet', KSIDENTIFIER),
        ('MembersListCount', ULONG),
        ('Reserved', ULONG)
    ]


PKSPROPERTY_DESCRIPTION = POINTER(KSPROPERTY_DESCRIPTION)


KSPROPERTY_MEMBER_RANGES = 0x00000001
KSPROPERTY_MEMBER_STEPPEDRANGES = 0x00000002
KSPROPERTY_MEMBER_VALUES = 0x00000003
KSPROPERTY_MEMBER_FLAG_DEFAULT = 0x00000001
KSPROPERTY_MEMBER_FLAG_BASICSUPPORT_MULTICHANNEL = 0x00000002
KSPROPERTY_MEMBER_FLAG_BASICSUPPORT_UNIFORM = 0x00000004


class KSPROPERTY_MEMBERSHEADER(ctypes.Structure):
    _fields_ = [
        ('MembersFlags', ULONG),
        ('MembersSize', ULONG),
        ('MembersCount', ULONG),
        ('Flags', ULONG),
    ]


PKSPROPERTY_MEMBERSHEADER = POINTER(KSPROPERTY_MEMBERSHEADER)


class KSPROPERTY_BOUNDS_LONG(ctypes.Union):

    class _Struct_1(ctypes.Structure):
        _fields_ = [
            ('SignedMinimum', LONG),
            ('SignedMaximum', LONG),
        ]

    class _Struct_2(ctypes.Structure):
        _fields_ = [
            ('UnsignedMinimum', ULONG),
            ('UnsignedMaximum', ULONG),
        ]

    _anonymous_ = ('_Struct_1', '_Struct_2')

    _fields_ = [
        ('_Struct_1', _Struct_1),
        ('_Struct_2', _Struct_2),
    ]


PKSPROPERTY_BOUNDS_LONG = POINTER(KSPROPERTY_BOUNDS_LONG)


class KSPROPERTY_BOUNDS_LONGLONG(ctypes.Union):
    class _Struct_1(ctypes.Structure):
        _fields_ = [
            ('SignedMinimum', LONGLONG),
            ('SignedMaximum', LONGLONG),
        ]


    class _Struct_2(ctypes.Structure):
        _fields_ = [
            ('UnsignedMinimum', ULONGLONG),
            ('UnsignedMaximum', ULONGLONG),
        ]


    _anonymous_ = ('_Struct_1', '_Struct_2')

    _fields_ = [
        ('_Struct_1', _Struct_1),
        ('_Struct_2', _Struct_2),
    ]


PKSPROPERTY_BOUNDS_LONGLONG = POINTER(KSPROPERTY_BOUNDS_LONGLONG)


class KSPROPERTY_STEPPING_LONG(ctypes.Structure):
    _fields_ = [
        ('SteppingDelta', ULONG),
        ('Reserved', ULONG),
        ('Bounds', KSPROPERTY_BOUNDS_LONG),
    ]


PKSPROPERTY_STEPPING_LONG = POINTER(KSPROPERTY_STEPPING_LONG)


class KSPROPERTY_STEPPING_LONGLONG(ctypes.Structure):
    _fields_ = [
        ('SteppingDelta', ULONGLONG),
        ('Bounds', KSPROPERTY_BOUNDS_LONGLONG),
    ]


PKSPROPERTY_STEPPING_LONGLONG = POINTER(KSPROPERTY_STEPPING_LONGLONG)
PKSWORKER = PVOID


class KSEVENTDATA(ctypes.Structure):
    class _Union(ctypes.Union):

        class EventHandle(ctypes.Structure):
            _fields_ = [
                ('Event', HANDLE),
                ('Reserved', ULONG_PTR * 2)
            ]

        class SemaphoreHandle(ctypes.Structure):
            _fields_ = [
                ('Semaphore', HANDLE),
                ('Reserved', ULONG),
                ('Adjustment', LONG)
            ]

        class EventObject(ctypes.Structure):
            _fields_ = [
                ('Event', PVOID),
                ('Increment', KPRIORITY),
                ('Reserved', ULONG_PTR)
            ]

        class SemaphoreObject(ctypes.Structure):
            _fields_ = [
                ('Semaphore', PVOID),
                ('Increment', KPRIORITY),
                ('Adjustment', LONG)
            ]

        class Dpc(ctypes.Structure):
            _fields_ = [
                ('Dpc', PKDPC),
                ('ReferenceCount', ULONG),
                ('Reserved', ULONG_PTR)
            ]

        class WorkItem(ctypes.Structure):
            _fields_ = [
                ('WorkQueueItem', PWORK_QUEUE_ITEM),
                ('WorkQueueType', WORK_QUEUE_TYPE),
                ('Reserved', ULONG_PTR)
            ]

        class KsWorkItem(ctypes.Structure):
            _fields_ = [
                ('WorkQueueItem', PWORK_QUEUE_ITEM),
                ('KsWorkerObject', PKSWORKER),
                ('Reserved', ULONG_PTR)
            ]

        class Alignment(ctypes.Structure):
            _fields_ = [
                ('Unused', PVOID),
                ('Alignment', LONG_PTR * 2),
            ]

        _fields_ = [
            ('EventHandle', EventHandle),
            ('SemaphoreHandle', SemaphoreHandle),
            ('EventObject', EventObject),
            ('SemaphoreObject', SemaphoreObject),
            ('Dpc', Dpc),
            ('WorkItem', WorkItem),
            ('KsWorkItem', KsWorkItem),
            ('Alignment', Alignment),
        ]

    _anonymous_ = ('_Union',)
    _fields_ = [
        ('NotificationType', ULONG),
        ('_Union', _Union)
    ]


PKSEVENTDATA = POINTER(KSEVENTDATA)


KSEVENTF_EVENT_HANDLE = 0x00000001
KSEVENTF_SEMAPHORE_HANDLE = 0x00000002
KSEVENTF_EVENT_OBJECT = 0x00000004
KSEVENTF_SEMAPHORE_OBJECT = 0x00000008
KSEVENTF_DPC = 0x00000010
KSEVENTF_WORKITEM = 0x00000020
KSEVENTF_KSWORKITEM = 0x00000080
KSEVENT_TYPE_ENABLE = 0x00000001
KSEVENT_TYPE_ONESHOT = 0x00000002
KSEVENT_TYPE_ENABLEBUFFERED = 0x00000004
KSEVENT_TYPE_SETSUPPORT = 0x00000100
KSEVENT_TYPE_BASICSUPPORT = 0x00000200
KSEVENT_TYPE_QUERYBUFFER = 0x00000400
KSEVENT_TYPE_TOPOLOGY = 0x10000000


class KSQUERYBUFFER(ctypes.Structure):
    _fields_ = [
        ('Event', KSEVENT),
        ('EventData', PKSEVENTDATA),
        ('Reserved', PVOID),
    ]


PKSQUERYBUFFER = POINTER(KSQUERYBUFFER)


class KSRELATIVEEVENT(ctypes.Structure):
    class _Union(ctypes.Union):
        _fields_ = [
            ('ObjectHandle', HANDLE),
            ('ObjectPointer', PVOID),
        ]

    _anonymous_ = ('_Union',)
    _fields_ = [
        ('Size', ULONG),
        ('Flags', ULONG),
        ('_Union', _Union),
        ('Reserved', PVOID),
        ('Event', KSEVENT),
        ('EventData', KSEVENTDATA),
    ]


PKSRELATIVEEVENT = POINTER(KSRELATIVEEVENT)


class KSEVENT_TIME_MARK(ctypes.Structure):
    _fields_ = [
        ('EventData', KSEVENTDATA),
        ('MarkTime', LONGLONG),
    ]


PKSEVENT_TIME_MARK = POINTER(KSEVENT_TIME_MARK)


class KSEVENT_TIME_INTERVAL(ctypes.Structure):
    _fields_ = [
        ('EventData', PKSEVENTDATA),
        ('TimeBase', LONGLONG),
        ('Interval', LONGLONG),
    ]


PKSEVENT_TIME_INTERVAL = POINTER(KSEVENT_TIME_INTERVAL)


class KSINTERVAL(ctypes.Structure):
    _fields_ = [
        ('TimeBase', LONGLONG),
        ('Interval', LONGLONG),
    ]


PKSINTERVAL = POINTER(KSINTERVAL)


KSRELATIVEEVENT_FLAG_HANDLE = 0x00000001
KSRELATIVEEVENT_FLAG_POINTER = 0x00000002
# ===========================================================================
STATIC_KSPROPSETID_General = (
    0x1464EDA5,
    0x6A8F,
    0x11D1,
    0x9A,
    0xA7,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSPROPSETID_General = DEFINE_GUIDSTRUCT(
    "1464EDA5-6A8F-11D1-9AA7-00A0C9223196"
)
KSPROPSETID_General = DEFINE_GUIDNAMED(KSPROPSETID_General)


class KSPROPERTY_GENERAL(ENUM):
    KSPROPERTY_GENERAL_COMPONENTID = 0

PFNKSHANDLER = VOID

def DEFINE_KSPROPERTY_ITEM(
    PropertyId,
    GetHandler,
    MinProperty,
    MinData,
    SetHandler,
    Values,
    RelationsCount,
    Relations,
    SupportHandler,
    SerializedSize
):
    return (
        PropertyId,
        PFNKSHANDLER(GetHandler),
        MinProperty,
        MinData,
        PFNKSHANDLER(SetHandler),
        PKSPROPERTY_VALUES(Values),
        RelationsCount,
        PKSPROPERTY(Relations),
        PFNKSHANDLER(SupportHandler),
        ULONG(SerializedSize)
    )



def DEFINE_KSPROPERTY_ITEM_GENERAL_COMPONENTID(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_GENERAL.KSPROPERTY_GENERAL_COMPONENTID,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSCOMPONENTID),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


class KSCOMPONENTID(ctypes.Structure):
    _fields_ = [
        ('Manufacturer', GUID),
        ('Product', GUID),
        ('Component', GUID),
        ('Name', GUID),
        ('Version', ULONG),
        ('Revision', ULONG),
    ]


PKSCOMPONENTID = POINTER(KSCOMPONENTID)


STATIC_KSMETHODSETID_StreamIo = (
    0x65D003CA,
    0x1523,
    0x11D2,
    0xB2,
    0x7A,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSMETHODSETID_StreamIo = DEFINE_GUIDSTRUCT(
    "65D003CA-1523-11D2-B27A-00A0C9223196"
)
KSMETHODSETID_StreamIo = DEFINE_GUIDNAMED(KSMETHODSETID_StreamIo)


class KSMETHOD_STREAMIO(ENUM):
    KSMETHOD_STREAMIO_READ = 0
    KSMETHOD_STREAMIO_WRITE = 1


def DEFINE_KSMETHOD_ITEM_STREAMIO_READ(Handler):
    return DEFINE_KSMETHOD_ITEM(
        KSMETHOD_STREAMIO.KSMETHOD_STREAMIO_READ,
        KSMETHOD_TYPE_WRITE,
        Handler,
        ctypes.sizeof(KSMETHOD),
        0,
        NULL
    )


def DEFINE_KSMETHOD_ITEM_STREAMIO_WRITE(Handler):
    return DEFINE_KSMETHOD_ITEM(
        KSMETHOD_STREAMIO.KSMETHOD_STREAMIO_WRITE,
        KSMETHOD_TYPE_READ,
        Handler,
        ctypes.sizeof(KSMETHOD),
        0,
        NULL
    )


STATIC_KSPROPSETID_MediaSeeking = (
    0xEE904F0C,
    0xD09B,
    0x11D0,
    0xAB,
    0xE9,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSPROPSETID_MediaSeeking = DEFINE_GUIDSTRUCT(
    "EE904F0C-D09B-11D0-ABE9-00A0C9223196"
)
KSPROPSETID_MediaSeeking = DEFINE_GUIDNAMED(KSPROPSETID_MediaSeeking)


class KSPROPERTY_MEDIASEEKING(ENUM):
    KSPROPERTY_MEDIASEEKING_CAPABILITIES = 0
    KSPROPERTY_MEDIASEEKING_FORMATS = 1
    KSPROPERTY_MEDIASEEKING_TIMEFORMAT = 2
    KSPROPERTY_MEDIASEEKING_POSITION = 3
    KSPROPERTY_MEDIASEEKING_STOPPOSITION = 4
    KSPROPERTY_MEDIASEEKING_POSITIONS = 5
    KSPROPERTY_MEDIASEEKING_DURATION = 6
    KSPROPERTY_MEDIASEEKING_AVAILABLE = 7
    KSPROPERTY_MEDIASEEKING_PREROLL = 8
    KSPROPERTY_MEDIASEEKING_CONVERTTIMEFORMAT = 9


class KS_SEEKING_FLAGS(ENUM):
    KS_SEEKING_NoPositioning = 0
    KS_SEEKING_AbsolutePositioning = 1
    KS_SEEKING_RelativePositioning = 2
    KS_SEEKING_IncrementalPositioning = 3
    KS_SEEKING_PositioningBitsMask = 0x3
    KS_SEEKING_SeekToKeyFrame = 4
    KS_SEEKING_ReturnTime = 0x8


class KS_SEEKING_CAPABILITIES(ENUM):
    KS_SEEKING_CanSeekAbsolute = 0x1
    KS_SEEKING_CanSeekForwards = 0x2
    KS_SEEKING_CanSeekBackwards = 0x4
    KS_SEEKING_CanGetCurrentPos = 0x8
    KS_SEEKING_CanGetStopPos = 0x10
    KS_SEEKING_CanGetDuration = 0x20
    KS_SEEKING_CanPlayBackwards = 0x40



def DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_CAPABILITIES(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_CAPABILITIES,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KS_SEEKING_CAPABILITIES),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_FORMATS(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_FORMATS,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_TIMEFORMAT(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_TIMEFORMAT,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(GUID),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_POSITION(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_POSITION,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(LONGLONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_STOPPOSITION(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_STOPPOSITION,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(LONGLONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_POSITIONS(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_POSITIONS,
        NULL,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSPROPERTY_POSITIONS),
        Handler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_DURATION(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_DURATION,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(LONGLONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_AVAILABLE(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_AVAILABLE,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSPROPERTY_MEDIAAVAILABLE),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_PREROLL(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_PREROLL,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(LONGLONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_CONVERTTIMEFORMAT(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_CONVERTTIMEFORMAT,
        Handler,
        ctypes.sizeof(KSP_TIMEFORMAT),
        ctypes.sizeof(LONGLONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


class KSPROPERTY_POSITIONS(ctypes.Structure):
    _fields_ = [
        ('Current', LONGLONG),
        ('Stop', LONGLONG),
        ('CurrentFlags', KS_SEEKING_FLAGS),
        ('StopFlags', KS_SEEKING_FLAGS),
    ]


PKSPROPERTY_POSITIONS = POINTER(KSPROPERTY_POSITIONS)


class KSPROPERTY_MEDIAAVAILABLE(ctypes.Structure):
    _fields_ = [
        ('Earliest', LONGLONG),
        ('Latest', LONGLONG),

    ]


PKSPROPERTY_MEDIAAVAILABLE = POINTER(KSPROPERTY_MEDIAAVAILABLE)


class KSP_TIMEFORMAT(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('SourceFormat', GUID),
        ('TargetFormat', GUID),
        ('Time', LONGLONG),
    ]


PKSP_TIMEFORMAT = POINTER(KSP_TIMEFORMAT)


# ===========================================================================
STATIC_KSPROPSETID_Topology = (
    0x720D4AC0,
    0x7533,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSPROPSETID_Topology = DEFINE_GUIDSTRUCT(
    "720D4AC0-7533-11D0-A5D6-28DB04C10000"
)
KSPROPSETID_Topology = DEFINE_GUIDNAMED(KSPROPSETID_Topology)


class KSPROPERTY_TOPOLOGY(ENUM):
    KSPROPERTY_TOPOLOGY_CATEGORIES = 0
    KSPROPERTY_TOPOLOGY_NODES = 1
    KSPROPERTY_TOPOLOGY_CONNECTIONS = 2
    KSPROPERTY_TOPOLOGY_NAME = 3


def DEFINE_KSPROPERTY_ITEM_TOPOLOGY_CATEGORIES(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_TOPOLOGY.KSPROPERTY_TOPOLOGY_CATEGORIES,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_TOPOLOGY_NODES(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_TOPOLOGY.KSPROPERTY_TOPOLOGY_NODES,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_TOPOLOGY_CONNECTIONS(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_TOPOLOGY.KSPROPERTY_TOPOLOGY_CONNECTIONS,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_TOPOLOGY_NAME(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_TOPOLOGY.KSPROPERTY_TOPOLOGY_NAME,
        Handler,
        ctypes.sizeof(KSP_NODE),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )




# =============================================================================

# properties used by graph manager to talk to particular filters

STATIC_KSPROPSETID_GM = (
    0xAF627536,
    0xE719,
    0x11D2,
    0x8A,
    0x1D,
    0x00,
    0x60,
    0x97,
    0xD2,
    0xDF,
    0x5D,
)
KSPROPSETID_GM = DEFINE_GUIDSTRUCT(
    "AF627536-E719-11D2-8A1D-006097D2DF5D"
)
KSPROPSETID_GM = DEFINE_GUIDNAMED(KSPROPSETID_GM)


class KSPROPERTY_GM(ENUM):
    KSPROPERTY_GM_GRAPHMANAGER = 0
    KSPROPERTY_GM_TIMESTAMP_CLOCK = 1
    KSPROPERTY_GM_RATEMATCH = 2
    KSPROPERTY_GM_RENDER_CLOCK = 3


# ===========================================================================
STATIC_KSCATEGORY_BRIDGE = (
    0x085AFF00,
    0x62CE,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSCATEGORY_BRIDGE = DEFINE_GUIDSTRUCT(
    "085AFF00-62CE-11CF-A5D6-28DB04C10000"
)
KSCATEGORY_BRIDGE = DEFINE_GUIDNAMED(KSCATEGORY_BRIDGE)
STATIC_KSCATEGORY_CAPTURE = (
    0x65E8773D,
    0x8F56,
    0x11D0,
    0xA3,
    0xB9,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_CAPTURE = DEFINE_GUIDSTRUCT(
    "65E8773D-8F56-11D0-A3B9-00A0C9223196"
)
KSCATEGORY_CAPTURE = DEFINE_GUIDNAMED(KSCATEGORY_CAPTURE)
STATIC_KSCATEGORY_VIDEO_CAMERA = (
    0xE5323777,
    0xF976,
    0x4F5B,
    0x9B,
    0x55,
    0xB9,
    0x46,
    0x99,
    0xC4,
    0x6E,
    0x44,
)
KSCATEGORY_VIDEO_CAMERA = DEFINE_GUIDSTRUCT(
    "E5323777-F976-4f5b-9B55-B94699C46E44"
)
KSCATEGORY_VIDEO_CAMERA = DEFINE_GUIDNAMED(KSCATEGORY_VIDEO_CAMERA)
STATIC_KSCATEGORY_SENSOR_CAMERA = (
    0x24E552D7,
    0x6523,
    0x47F7,
    0xA6,
    0x47,
    0xD3,
    0x46,
    0x5B,
    0xF1,
    0xF5,
    0xCA,
)
KSCATEGORY_SENSOR_CAMERA = DEFINE_GUIDSTRUCT(
    "24E552D7-6523-47F7-A647-D3465BF1F5CA"
)
KSCATEGORY_SENSOR_CAMERA = DEFINE_GUIDNAMED(KSCATEGORY_SENSOR_CAMERA)
STATIC_KSCATEGORY_SENSOR_GROUP = (
    0x669C7214,
    0x0A88,
    0x4311,
    0xA7,
    0xF3,
    0x4E,
    0x79,
    0x82,
    0x0E,
    0x33,
    0xBD,
)
KSCATEGORY_SENSOR_GROUP = DEFINE_GUIDSTRUCT(
    "669C7214-0A88-4311-A7F3-4E79820E33BD"
)
KSCATEGORY_SENSOR_GROUP = DEFINE_GUIDNAMED(KSCATEGORY_SENSOR_GROUP)
STATIC_KSCATEGORY_RENDER = (
    0x65E8773E,
    0x8F56,
    0x11D0,
    0xA3,
    0xB9,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_RENDER = DEFINE_GUIDSTRUCT(
    "65E8773E-8F56-11D0-A3B9-00A0C9223196"
)
KSCATEGORY_RENDER = DEFINE_GUIDNAMED(KSCATEGORY_RENDER)
STATIC_KSCATEGORY_MIXER = (
    0xAD809C00,
    0x7B88,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSCATEGORY_MIXER = DEFINE_GUIDSTRUCT(
    "AD809C00-7B88-11D0-A5D6-28DB04C10000"
)
KSCATEGORY_MIXER = DEFINE_GUIDNAMED(KSCATEGORY_MIXER)
STATIC_KSCATEGORY_SPLITTER = (
    0x0A4252A0,
    0x7E70,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSCATEGORY_SPLITTER = DEFINE_GUIDSTRUCT(
    "0A4252A0-7E70-11D0-A5D6-28DB04C10000"
)
KSCATEGORY_SPLITTER = DEFINE_GUIDNAMED(KSCATEGORY_SPLITTER)
STATIC_KSCATEGORY_DATACOMPRESSOR = (
    0x1E84C900,
    0x7E70,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSCATEGORY_DATACOMPRESSOR = DEFINE_GUIDSTRUCT(
    "1E84C900-7E70-11D0-A5D6-28DB04C10000"
)
KSCATEGORY_DATACOMPRESSOR = DEFINE_GUIDNAMED(KSCATEGORY_DATACOMPRESSOR)
STATIC_KSCATEGORY_DATADECOMPRESSOR = (
    0x2721AE20,
    0x7E70,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSCATEGORY_DATADECOMPRESSOR = DEFINE_GUIDSTRUCT(
    "2721AE20-7E70-11D0-A5D6-28DB04C10000"
)
KSCATEGORY_DATADECOMPRESSOR = DEFINE_GUIDNAMED(KSCATEGORY_DATADECOMPRESSOR)
STATIC_KSCATEGORY_DATATRANSFORM = (
    0x2EB07EA0,
    0x7E70,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSCATEGORY_DATATRANSFORM = DEFINE_GUIDSTRUCT(
    "2EB07EA0-7E70-11D0-A5D6-28DB04C10000"
)
KSCATEGORY_DATATRANSFORM = DEFINE_GUIDNAMED(KSCATEGORY_DATATRANSFORM)

# KSMFT_CATEGORY_XXX are MF Transform category guids redefined in ks.h
# to facilitate KS Mini drivers to register KS Filters under MF Transform
# categories.

STATIC_KSMFT_CATEGORY_VIDEO_DECODER = (
    0xD6C02D4B,
    0x6833,
    0x45B4,
    0x97,
    0x1A,
    0x05,
    0xA4,
    0xB0,
    0x4B,
    0xAB,
    0x91,
)
KSMFT_CATEGORY_VIDEO_DECODER = DEFINE_GUIDSTRUCT(
    "d6c02d4b-6833-45b4-971a-05a4b04bab91"
)
KSMFT_CATEGORY_VIDEO_DECODER = DEFINE_GUIDNAMED(KSMFT_CATEGORY_VIDEO_DECODER)
STATIC_KSMFT_CATEGORY_VIDEO_ENCODER = (
    0xF79EAC7D,
    0xE545,
    0x4387,
    0xBD,
    0xEE,
    0xD6,
    0x47,
    0xD7,
    0xBD,
    0xE4,
    0x2A,
)
KSMFT_CATEGORY_VIDEO_ENCODER = DEFINE_GUIDSTRUCT(
    "f79eac7d-e545-4387-bdee-d647d7bde42a"
)
KSMFT_CATEGORY_VIDEO_ENCODER = DEFINE_GUIDNAMED(KSMFT_CATEGORY_VIDEO_ENCODER)
STATIC_KSMFT_CATEGORY_VIDEO_EFFECT = (
    0x12E17C21,
    0x532C,
    0x4A6E,
    0x8A,
    0x1C,
    0x40,
    0x82,
    0x5A,
    0x73,
    0x63,
    0x97,
)
KSMFT_CATEGORY_VIDEO_EFFECT = DEFINE_GUIDSTRUCT(
    "12e17c21-532c-4a6e-8a1c-40825a736397"
)
KSMFT_CATEGORY_VIDEO_EFFECT = DEFINE_GUIDNAMED(KSMFT_CATEGORY_VIDEO_EFFECT)
STATIC_KSMFT_CATEGORY_MULTIPLEXER = (
    0x059C561E,
    0x05AE,
    0x4B61,
    0xB6,
    0x9D,
    0x55,
    0xB6,
    0x1E,
    0xE5,
    0x4A,
    0x7B,
)
KSMFT_CATEGORY_MULTIPLEXER = DEFINE_GUIDSTRUCT(
    "059c561e-05ae-4b61-b69d-55b61ee54a7b"
)
KSMFT_CATEGORY_MULTIPLEXER = DEFINE_GUIDNAMED(KSMFT_CATEGORY_MULTIPLEXER)
STATIC_KSMFT_CATEGORY_DEMULTIPLEXER = (
    0xA8700A7A,
    0x939B,
    0x44C5,
    0x99,
    0xD7,
    0x76,
    0x22,
    0x6B,
    0x23,
    0xB3,
    0xF1,
)
KSMFT_CATEGORY_DEMULTIPLEXER = DEFINE_GUIDSTRUCT(
    "a8700a7a-939b-44c5-99d7-76226b23b3f1"
)
KSMFT_CATEGORY_DEMULTIPLEXER = DEFINE_GUIDNAMED(KSMFT_CATEGORY_DEMULTIPLEXER)
STATIC_KSMFT_CATEGORY_AUDIO_DECODER = (
    0x9EA73FB4,
    0xEF7A,
    0x4559,
    0x8D,
    0x5D,
    0x71,
    0x9D,
    0x8F,
    0x04,
    0x26,
    0xC7,
)
KSMFT_CATEGORY_AUDIO_DECODER = DEFINE_GUIDSTRUCT(
    "9ea73fb4-ef7a-4559-8d5d-719d8f0426c7"
)
KSMFT_CATEGORY_AUDIO_DECODER = DEFINE_GUIDNAMED(KSMFT_CATEGORY_AUDIO_DECODER)
STATIC_KSMFT_CATEGORY_AUDIO_ENCODER = (
    0x91C64BD0,
    0xF91E,
    0x4D8C,
    0x92,
    0x76,
    0xDB,
    0x24,
    0x82,
    0x79,
    0xD9,
    0x75,
)
KSMFT_CATEGORY_AUDIO_ENCODER = DEFINE_GUIDSTRUCT(
    "91c64bd0-f91e-4d8c-9276-db248279d975"
)
KSMFT_CATEGORY_AUDIO_ENCODER = DEFINE_GUIDNAMED(KSMFT_CATEGORY_AUDIO_ENCODER)
STATIC_KSMFT_CATEGORY_AUDIO_EFFECT = (
    0x11064C48,
    0x3648,
    0x4ED0,
    0x93,
    0x2E,
    0x05,
    0xCE,
    0x8A,
    0xC8,
    0x11,
    0xB7,
)
KSMFT_CATEGORY_AUDIO_EFFECT = DEFINE_GUIDSTRUCT(
    "11064c48-3648-4ed0-932e-05ce8ac811b7"
)
KSMFT_CATEGORY_AUDIO_EFFECT = DEFINE_GUIDNAMED(KSMFT_CATEGORY_AUDIO_EFFECT)
STATIC_KSMFT_CATEGORY_VIDEO_PROCESSOR = (
    0x302EA3FC,
    0xAA5F,
    0x47F9,
    0x9F,
    0x7A,
    0xC2,
    0x18,
    0x8B,
    0xB1,
    0x63,
    0x2,
)
KSMFT_CATEGORY_VIDEO_PROCESSOR = DEFINE_GUIDSTRUCT(
    "302ea3fc-aa5f-47f9-9f7a-c2188bb16302"
)
KSMFT_CATEGORY_VIDEO_PROCESSOR = DEFINE_GUIDNAMED(
    KSMFT_CATEGORY_VIDEO_PROCESSOR
)
STATIC_KSMFT_CATEGORY_OTHER = (
    0x90175D57,
    0xB7EA,
    0x4901,
    0xAE,
    0xB3,
    0x93,
    0x3A,
    0x87,
    0x47,
    0x75,
    0x6F,
)
KSMFT_CATEGORY_OTHER = DEFINE_GUIDSTRUCT(
    "90175d57-b7ea-4901-aeb3-933a8747756f"
)
KSMFT_CATEGORY_OTHER = DEFINE_GUIDNAMED(KSMFT_CATEGORY_OTHER)
STATIC_KSCATEGORY_COMMUNICATIONSTRANSFORM = (
    0xCF1DDA2C,
    0x9743,
    0x11D0,
    0xA3,
    0xEE,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_COMMUNICATIONSTRANSFORM = DEFINE_GUIDSTRUCT(
    "CF1DDA2C-9743-11D0-A3EE-00A0C9223196"
)
KSCATEGORY_COMMUNICATIONSTRANSFORM = DEFINE_GUIDNAMED(
    KSCATEGORY_COMMUNICATIONSTRANSFORM
)
STATIC_KSCATEGORY_INTERFACETRANSFORM = (
    0xCF1DDA2D,
    0x9743,
    0x11D0,
    0xA3,
    0xEE,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_INTERFACETRANSFORM = DEFINE_GUIDSTRUCT(
    "CF1DDA2D-9743-11D0-A3EE-00A0C9223196"
)
KSCATEGORY_INTERFACETRANSFORM = DEFINE_GUIDNAMED(KSCATEGORY_INTERFACETRANSFORM)
STATIC_KSCATEGORY_MEDIUMTRANSFORM = (
    0xCF1DDA2E,
    0x9743,
    0x11D0,
    0xA3,
    0xEE,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_MEDIUMTRANSFORM = DEFINE_GUIDSTRUCT(
    "CF1DDA2E-9743-11D0-A3EE-00A0C9223196"
)
KSCATEGORY_MEDIUMTRANSFORM = DEFINE_GUIDNAMED(KSCATEGORY_MEDIUMTRANSFORM)
STATIC_KSCATEGORY_FILESYSTEM = (
    0x760FED5E,
    0x9357,
    0x11D0,
    0xA3,
    0xCC,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_FILESYSTEM = DEFINE_GUIDSTRUCT(
    "760FED5E-9357-11D0-A3CC-00A0C9223196"
)
KSCATEGORY_FILESYSTEM = DEFINE_GUIDNAMED(KSCATEGORY_FILESYSTEM)
# KSNAME_Clock
STATIC_KSCATEGORY_CLOCK = (
    0x53172480,
    0x4791,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSCATEGORY_CLOCK = DEFINE_GUIDSTRUCT(
    "53172480-4791-11D0-A5D6-28DB04C10000"
)
KSCATEGORY_CLOCK = DEFINE_GUIDNAMED(KSCATEGORY_CLOCK)
STATIC_KSCATEGORY_PROXY = (
    0x97EBAACA,
    0x95BD,
    0x11D0,
    0xA3,
    0xEA,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_PROXY = DEFINE_GUIDSTRUCT(
    "97EBAACA-95BD-11D0-A3EA-00A0C9223196"
)
KSCATEGORY_PROXY = DEFINE_GUIDNAMED(KSCATEGORY_PROXY)
STATIC_KSCATEGORY_QUALITY = (
    0x97EBAACB,
    0x95BD,
    0x11D0,
    0xA3,
    0xEA,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_QUALITY = DEFINE_GUIDSTRUCT(
    "97EBAACB-95BD-11D0-A3EA-00A0C9223196"
)
KSCATEGORY_QUALITY = DEFINE_GUIDNAMED(KSCATEGORY_QUALITY)


class KSTOPOLOGY_CONNECTION(ctypes.Structure):
    _fields_ = [
        ('FromNode', ULONG),
        ('FromNodePin', ULONG),
        ('ToNode', ULONG),
        ('ToNodePin', ULONG),
    ]


PKSTOPOLOGY_CONNECTION = POINTER(KSTOPOLOGY_CONNECTION)


class KSTOPOLOGY(ctypes.Structure):
    _fields_ = [
        ('CategoriesCount', ULONG),
        ('Categories', POINTER(GUID)),
        ('TopologyNodesCount', ULONG),
        ('TopologyNodes', POINTER(GUID)),
        ('TopologyConnectionsCount', ULONG),
        ('TopologyConnections', POINTER(KSTOPOLOGY_CONNECTION)),
        ('TopologyNodesNames', POINTER(GUID)),
        ('Reserved', ULONG),

    ]


PKSTOPOLOGY = POINTER(KSTOPOLOGY)


KSFILTER_NODE = -1
KSALL_NODES = -1


class KSNODE_CREATE(ctypes.Structure):
    _fields_ = [
        ('CreateFlags', ULONG),
        ('Node', ULONG),

    ]


PKSNODE_CREATE = POINTER(KSNODE_CREATE)


# ===========================================================================
# TIME_FORMAT_NONE
STATIC_KSTIME_FORMAT_NONE = STATIC_GUID_NULL
KSTIME_FORMAT_NONE = GUID_NULL
# TIME_FORMAT_FRAME
STATIC_KSTIME_FORMAT_FRAME = (
    0x7B785570,
    0x8C82,
    0x11CF,
    0xBC,
    0x0C,
    0x00,
    0xAA,
    0x00,
    0xAC,
    0x74,
    0xF6,
)
KSTIME_FORMAT_FRAME = DEFINE_GUIDSTRUCT(
    "7b785570-8c82-11cf-bc0c-00aa00ac74f6"
)
KSTIME_FORMAT_FRAME = DEFINE_GUIDNAMED(KSTIME_FORMAT_FRAME)
# TIME_FORMAT_BYTE
STATIC_KSTIME_FORMAT_BYTE = (
    0x7B785571,
    0x8C82,
    0x11CF,
    0xBC,
    0x0C,
    0x00,
    0xAA,
    0x00,
    0xAC,
    0x74,
    0xF6,
)
KSTIME_FORMAT_BYTE = DEFINE_GUIDSTRUCT(
    "7b785571-8c82-11cf-bc0c-00aa00ac74f6"
)
KSTIME_FORMAT_BYTE = DEFINE_GUIDNAMED(KSTIME_FORMAT_BYTE)
# TIME_FORMAT_SAMPLE
STATIC_KSTIME_FORMAT_SAMPLE = (
    0x7B785572,
    0x8C82,
    0x11CF,
    0xBC,
    0x0C,
    0x00,
    0xAA,
    0x00,
    0xAC,
    0x74,
    0xF6,
)
KSTIME_FORMAT_SAMPLE = DEFINE_GUIDSTRUCT(
    "7b785572-8c82-11cf-bc0c-00aa00ac74f6"
)
KSTIME_FORMAT_SAMPLE = DEFINE_GUIDNAMED(KSTIME_FORMAT_SAMPLE)
# TIME_FORMAT_FIELD
STATIC_KSTIME_FORMAT_FIELD = (
    0x7B785573,
    0x8C82,
    0x11CF,
    0xBC,
    0x0C,
    0x00,
    0xAA,
    0x00,
    0xAC,
    0x74,
    0xF6,
)
KSTIME_FORMAT_FIELD = DEFINE_GUIDSTRUCT(
    "7b785573-8c82-11cf-bc0c-00aa00ac74f6"
)
KSTIME_FORMAT_FIELD = DEFINE_GUIDNAMED(KSTIME_FORMAT_FIELD)
# TIME_FORMAT_MEDIA_TIME
STATIC_KSTIME_FORMAT_MEDIA_TIME = (
    0x7B785574,
    0x8C82,
    0x11CF,
    0xBC,
    0x0C,
    0x00,
    0xAA,
    0x00,
    0xAC,
    0x74,
    0xF6,
)
KSTIME_FORMAT_MEDIA_TIME = DEFINE_GUIDSTRUCT(
    "7b785574-8c82-11cf-bc0c-00aa00ac74f6"
)
KSTIME_FORMAT_MEDIA_TIME = DEFINE_GUIDNAMED(KSTIME_FORMAT_MEDIA_TIME)
# ===========================================================================
KSPIN_INTERFACE = KSIDENTIFIER
PKSPIN_INTERFACE = POINTER(KSIDENTIFIER)
STATIC_KSINTERFACESETID_Standard = (
    0x1A8766A0,
    0x62CE,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSINTERFACESETID_Standard = DEFINE_GUIDSTRUCT(
    "1A8766A0-62CE-11CF-A5D6-28DB04C10000"
)
KSINTERFACESETID_Standard = DEFINE_GUIDNAMED(KSINTERFACESETID_Standard)


class KSINTERFACE_STANDARD(ENUM):
    KSINTERFACE_STANDARD_STREAMING = 0
    KSINTERFACE_STANDARD_LOOPED_STREAMING = 1
    KSINTERFACE_STANDARD_CONTROL = 2


# Reserved for system use
STATIC_KSINTERFACESETID_FileIo = (
    0x8C6F932C,
    0xE771,
    0x11D0,
    0xB8,
    0xFF,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSINTERFACESETID_FileIo = DEFINE_GUIDSTRUCT(
    "8C6F932C-E771-11D0-B8FF-00A0C9223196"
)
KSINTERFACESETID_FileIo = DEFINE_GUIDNAMED(KSINTERFACESETID_FileIo)


class KSINTERFACE_FILEIO(ENUM):
    KSINTERFACE_FILEIO_STREAMING = 0


# ===========================================================================
KSMEDIUM_TYPE_ANYINSTANCE = 0x00000000
STATIC_KSMEDIUMSETID_Standard = (
    0x4747B320,
    0x62CE,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSMEDIUMSETID_Standard = DEFINE_GUIDSTRUCT(
    "4747B320-62CE-11CF-A5D6-28DB04C10000"
)
KSMEDIUMSETID_Standard = DEFINE_GUIDNAMED(KSMEDIUMSETID_Standard)
# For compatibility only
KSMEDIUM_STANDARD_DEVIO = KSMEDIUM_TYPE_ANYINSTANCE
# ===========================================================================
STATIC_KSPROPSETID_Pin = (
    0x8C134960,
    0x51AD,
    0x11CF,
    0x87,
    0x8A,
    0x94,
    0xF8,
    0x01,
    0xC1,
    0x00,
    0x00,
)
KSPROPSETID_Pin = DEFINE_GUIDSTRUCT(
    "8C134960-51AD-11CF-878A-94F801C10000"
)
KSPROPSETID_Pin = DEFINE_GUIDNAMED(KSPROPSETID_Pin)


class KSPROPERTY_PIN(ENUM):
    KSPROPERTY_PIN_CINSTANCES = 0
    KSPROPERTY_PIN_CTYPES = 1
    KSPROPERTY_PIN_DATAFLOW = 2
    KSPROPERTY_PIN_DATARANGES = 3
    KSPROPERTY_PIN_DATAINTERSECTION = 4
    KSPROPERTY_PIN_INTERFACES = 5
    KSPROPERTY_PIN_MEDIUMS = 6
    KSPROPERTY_PIN_COMMUNICATION = 7
    KSPROPERTY_PIN_GLOBALCINSTANCES = 8
    KSPROPERTY_PIN_NECESSARYINSTANCES = 9
    KSPROPERTY_PIN_PHYSICALCONNECTION = 10
    KSPROPERTY_PIN_CATEGORY = 11
    KSPROPERTY_PIN_NAME = 12
    KSPROPERTY_PIN_CONSTRAINEDDATARANGES = 13
    KSPROPERTY_PIN_PROPOSEDATAFORMAT = 14
    KSPROPERTY_PIN_PROPOSEDATAFORMAT2 = 15


KSPROPERTY_PIN_FLAGS_ATTRIBUTE_RANGE_AWARE = 0x00000001
KSPROPERTY_PIN_FLAGS_MASK = KSPROPERTY_PIN_FLAGS_ATTRIBUTE_RANGE_AWARE


class KSP_PIN(ctypes.Structure):

    class _Union(ctypes.Union):
        _fields_ = [
            ('Reserved', ULONG),
            ('Flags', ULONG),
        ]

    _anonymous_ = ('_Union',)
    _fields_ = [
        ('Property', KSPROPERTY),
        ('PinId', ULONG),
        ('_Union', _Union)

    ]


PKSP_PIN = POINTER(KSP_PIN)


class KSE_PIN(ctypes.Structure):
    _fields_ = [
        ('Event', KSEVENT),
        ('PinId', ULONG),
        ('Reserved', ULONG),
    ]


PKSE_PIN = POINTER(KSE_PIN)

KSINSTANCE_INDETERMINATE = -1


class KSPIN_CINSTANCES(ctypes.Structure):
    _fields_ = [
        ('PossibleCount', ULONG),
        ('CurrentCount', ULONG),
    ]


PKSPIN_CINSTANCES = POINTER(KSPIN_CINSTANCES)


class KSPIN_DATAFLOW(ENUM):
    KSPIN_DATAFLOW_IN = 1
    KSPIN_DATAFLOW_OUT = 2


PKSPIN_DATAFLOW = POINTER(KSPIN_DATAFLOW)


KSDATAFORMAT_BIT_TEMPORAL_COMPRESSION = 0x00000000
KSDATAFORMAT_TEMPORAL_COMPRESSION = 1 << KSDATAFORMAT_BIT_TEMPORAL_COMPRESSION
KSDATAFORMAT_BIT_ATTRIBUTES = 0x00000001
KSDATAFORMAT_ATTRIBUTES = 1 << KSDATAFORMAT_BIT_ATTRIBUTES
KSDATARANGE_BIT_ATTRIBUTES = 0x00000001
KSDATARANGE_ATTRIBUTES = 1 << KSDATARANGE_BIT_ATTRIBUTES
KSDATARANGE_BIT_REQUIRED_ATTRIBUTES = 0x00000002
KSDATARANGE_REQUIRED_ATTRIBUTES = 1 << KSDATARANGE_BIT_REQUIRED_ATTRIBUTES
KSATTRIBUTE_REQUIRED = 0x00000001


class KSDATAFORMAT(ctypes.Structure):
    _fields_ = [
        ('FormatSize', ULONG),
        ('Flags', ULONG),
        ('SampleSize', ULONG),
        ('Reserved', ULONG),
        ('MajorFormat', GUID),
        ('SubFormat', GUID),
        ('Specifier', GUID)
    ]


PKSDATAFORMAT = POINTER(KSDATAFORMAT)
KSDATARANGE = KSDATAFORMAT
PKSDATARANGE = POINTER(KSDATAFORMAT)


class KSATTRIBUTE(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('Flags', ULONG),
        ('Attribute', GUID)
    ]


PKSATTRIBUTE = POINTER(KSATTRIBUTE)


class KSATTRIBUTE_LIST(ctypes.Structure):
    _fields_ = [
        ('Count', ULONG),
        ('Attributes', POINTER(KSATTRIBUTE))
    ]


PKSATTRIBUTE_LIST = POINTER(KSATTRIBUTE_LIST)


class KSPIN_COMMUNICATION(ENUM):
    KSPIN_COMMUNICATION_NONE = 0
    KSPIN_COMMUNICATION_SINK = 1
    KSPIN_COMMUNICATION_SOURCE = 2
    KSPIN_COMMUNICATION_BOTH = 3
    KSPIN_COMMUNICATION_BRIDGE = 4


PKSPIN_COMMUNICATION = POINTER(KSPIN_COMMUNICATION)


KSPIN_MEDIUM = KSIDENTIFIER
PKSPIN_MEDIUM = POINTER(KSIDENTIFIER)



def DEFINE_KSPROPERTY_ITEM_PIN_CINSTANCES(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_CINSTANCES,
        Handler,
        ctypes.sizeof(KSP_PIN),
        ctypes.sizeof(KSPIN_CINSTANCES),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_CTYPES(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_CTYPES,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(ULONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_DATAFLOW(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_DATAFLOW,
        Handler,
        ctypes.sizeof(KSP_PIN),
        ctypes.sizeof(KSPIN_DATAFLOW),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_DATARANGES(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_DATARANGES,
        Handler,
        ctypes.sizeof(KSP_PIN),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_DATAINTERSECTION(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_DATAINTERSECTION,
        Handler,
        ctypes.sizeof(KSP_PIN) + ctypes.sizeof(KSMULTIPLE_ITEM),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_INTERFACES(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_INTERFACES,
        Handler,
        ctypes.sizeof(KSP_PIN),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_MEDIUMS(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_MEDIUMS,
        Handler,
        ctypes.sizeof(KSP_PIN),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_COMMUNICATION(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_COMMUNICATION,
        Handler,
        ctypes.sizeof(KSP_PIN),
        ctypes.sizeof(KSPIN_COMMUNICATION),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_GLOBALCINSTANCES(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_GLOBALCINSTANCES,
        Handler,
        ctypes.sizeof(KSP_PIN),
        ctypes.sizeof(KSPIN_CINSTANCES),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_NECESSARYINSTANCES(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_NECESSARYINSTANCES,
        Handler,
        ctypes.sizeof(KSP_PIN),
        ctypes.sizeof(ULONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_PHYSICALCONNECTION(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_PHYSICALCONNECTION,
        Handler,
        ctypes.sizeof(KSP_PIN),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_CATEGORY(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_CATEGORY,
        Handler,
        ctypes.sizeof(KSP_PIN),
        ctypes.sizeof(GUID),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_NAME(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_NAME,
        Handler,
        ctypes.sizeof(KSP_PIN),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_CONSTRAINEDDATARANGES(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_CONSTRAINEDDATARANGES,
        Handler,
        ctypes.sizeof(KSP_PIN),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_PIN_PROPOSEDATAFORMAT(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_PIN.KSPROPERTY_PIN_PROPOSEDATAFORMAT,
        NULL,
        ctypes.sizeof(KSP_PIN),
        ctypes.sizeof(KSDATAFORMAT),
        Handler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )



class KSPIN_CONNECT(ctypes.Structure):
    _fields_ = [
        ('Interface', KSPIN_INTERFACE),
        ('Medium', KSPIN_MEDIUM),
        ('PinId', ULONG),
        ('PinToHandle', HANDLE),
        ('Priority', KSPRIORITY),
    ]


PKSPIN_CONNECT = POINTER(KSPIN_CONNECT)


class KSPIN_PHYSICALCONNECTION(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('Pin', ULONG),
        ('SymbolicLinkName', WCHAR * 1)
    ]


PKSPIN_PHYSICALCONNECTION = POINTER(KSPIN_PHYSICALCONNECTION)


STATIC_KSEVENTSETID_PinCapsChange = (
    0xDD4F192E,
    0x3B78,
    0x49AD,
    0xA5,
    0x34,
    0x2C,
    0x31,
    0x5B,
    0x82,
    0x20,
    0x00,
)
KSEVENTSETID_PinCapsChange = DEFINE_GUIDSTRUCT(
    "DD4F192E-3B78-49AD-A534-2C315B822000"
)
KSEVENTSETID_PinCapsChange = DEFINE_GUIDNAMED(KSEVENTSETID_PinCapsChange)


class KSEVENT_PINCAPS_CHANGENOTIFICATIONS(ENUM):
    KSEVENT_PINCAPS_FORMATCHANGE = 0
    KSEVENT_PINCAPS_JACKINFOCHANGE = 1


STATIC_KSEVENTSETID_VolumeLimit = (
    0xDA168465,
    0x3A7C,
    0x4858,
    0x9D,
    0x4A,
    0x3E,
    0x8E,
    0x24,
    0x70,
    0x1A,
    0xEF,
)
KSEVENTSETID_VolumeLimit = DEFINE_GUIDSTRUCT(
    "DA168465-3A7C-4858-9D4A-3E8E24701AEF"
)
KSEVENTSETID_VolumeLimit = DEFINE_GUIDNAMED(KSEVENTSETID_VolumeLimit)


class KSEVENT_VOLUMELIMIT(ENUM):
    KSEVENT_VOLUMELIMIT_CHANGED = 0


STATIC_KSNAME_Filter = (
    0x9B365890,
    0x165F,
    0x11D0,
    0xA1,
    0x95,
    0x00,
    0x20,
    0xAF,
    0xD1,
    0x56,
    0xE4,
)
KSNAME_Filter = DEFINE_GUIDSTRUCT(
    "9b365890-165f-11d0-a195-0020afd156e4"
)
KSNAME_Filter = DEFINE_GUIDNAMED(KSNAME_Filter)
KSSTRING_Filter = "[9B365890-165F-11D0-A195-0020AFD156E4]"
STATIC_KSNAME_Pin = (
    0x146F1A80,
    0x4791,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSNAME_Pin = DEFINE_GUIDSTRUCT(
    "146F1A80-4791-11D0-A5D6-28DB04C10000"
)
KSNAME_Pin = DEFINE_GUIDNAMED(KSNAME_Pin)
KSSTRING_Pin = "[146F1A80-4791-11D0-A5D6-28DB04C10000]"
STATIC_KSNAME_Clock = (
    0x53172480,
    0x4791,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSNAME_Clock = DEFINE_GUIDSTRUCT(
    "53172480-4791-11D0-A5D6-28DB04C10000"
)
KSNAME_Clock = DEFINE_GUIDNAMED(KSNAME_Clock)
KSSTRING_Clock = "[53172480-4791-11D0-A5D6-28DB04C10000]"
STATIC_KSNAME_Allocator = (
    0x642F5D00,
    0x4791,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSNAME_Allocator = DEFINE_GUIDSTRUCT(
    "642F5D00-4791-11D0-A5D6-28DB04C10000"
)
KSNAME_Allocator = DEFINE_GUIDNAMED(KSNAME_Allocator)
KSSTRING_Allocator = "[642F5D00-4791-11D0-A5D6-28DB04C10000]"
KSSTRING_AllocatorEx = "[091BB63B-603F-11D1-B067-00A0C9062802]"
STATIC_KSNAME_TopologyNode = (
    0x0621061A,
    0xEE75,
    0x11D0,
    0xB9,
    0x15,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSNAME_TopologyNode = DEFINE_GUIDSTRUCT(
    "0621061A-EE75-11D0-B915-00A0C9223196"
)
KSNAME_TopologyNode = DEFINE_GUIDNAMED(KSNAME_TopologyNode)
KSSTRING_TopologyNode = "[0621061A-EE75-11D0-B915-00A0C9223196]"


class KSPIN_DESCRIPTOR(ctypes.Structure):
    class _Union(ctypes.Union):

        class _Struct(ctypes.Structure):
            _fields_ = [
                ('ConstrainedDataRangesCount', ULONG),
                ('ConstrainedDataRanges', PKSDATARANGE)
            ]

        _anonymous = ('_Struct',)
        _fields_ = [
            ('Reserved', LONGLONG),
            ('_Struct', _Struct)
        ]

    _anonymous_ = ('_Union',)

    _fields_ = [
        ('InterfacesCount', ULONG),
        ('Interfaces', POINTER(KSPIN_INTERFACE)),
        ('MediumsCount', ULONG),
        ('Mediums', POINTER(KSPIN_MEDIUM)),
        ('DataRangesCount', ULONG),
        ('DataRanges', POINTER(PKSDATARANGE)),
        ('DataFlow', KSPIN_DATAFLOW),
        ('Communication', KSPIN_COMMUNICATION),
        ('Category', POINTER(GUID)),
        ('Name', POINTER(GUID)),
        ('_Union', _Union)
    ]


PKSPIN_DESCRIPTOR = POINTER(KSPIN_DESCRIPTOR)
PCKSPIN_DESCRIPTOR = POINTER(KSPIN_DESCRIPTOR)



def DEFINE_KSPIN_DESCRIPTOR_ITEM(
    InterfacesCount,
    Interfaces,
    MediumsCount,
    Mediums,
    DataRangesCount,
    DataRanges,
    DataFlow,
    Communication
):
    return (
        InterfacesCount,
        Interfaces,
        MediumsCount,
        Mediums,
        DataRangesCount,
        DataRanges,
        DataFlow,
        Communication,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPIN_DESCRIPTOR_ITEMEX(
    InterfacesCount,
    Interfaces,
    MediumsCount,
    Mediums,
    DataRangesCount,
    DataRanges,
    DataFlow,
    Communication,
    Category,
    Name
):
    return (
        InterfacesCount,
        Interfaces,
        MediumsCount,
        Mediums,
        DataRangesCount,
        DataRanges,
        DataFlow,
        Communication,
        Category,
        Name,
        0
    )

# ===========================================================================
STATIC_KSDATAFORMAT_TYPE_WILDCARD = STATIC_GUID_NULL
KSDATAFORMAT_TYPE_WILDCARD = GUID_NULL
STATIC_KSDATAFORMAT_SUBTYPE_WILDCARD = STATIC_GUID_NULL
KSDATAFORMAT_SUBTYPE_WILDCARD = GUID_NULL
STATIC_KSDATAFORMAT_TYPE_STREAM = (
    0xE436EB83,
    0x524F,
    0x11CE,
    0x9F,
    0x53,
    0x00,
    0x20,
    0xAF,
    0x0B,
    0xA7,
    0x70,
)
KSDATAFORMAT_TYPE_STREAM = DEFINE_GUIDSTRUCT(
    "E436EB83-524F-11CE-9F53-0020AF0BA770"
)
KSDATAFORMAT_TYPE_STREAM = DEFINE_GUIDNAMED(KSDATAFORMAT_TYPE_STREAM)
STATIC_KSDATAFORMAT_SUBTYPE_NONE = (
    0xE436EB8E,
    0x524F,
    0x11CE,
    0x9F,
    0x53,
    0x00,
    0x20,
    0xAF,
    0x0B,
    0xA7,
    0x70,
)
KSDATAFORMAT_SUBTYPE_NONE = DEFINE_GUIDSTRUCT(
    "E436EB8E-524F-11CE-9F53-0020AF0BA770"
)
KSDATAFORMAT_SUBTYPE_NONE = DEFINE_GUIDNAMED(KSDATAFORMAT_SUBTYPE_NONE)
STATIC_KSDATAFORMAT_SPECIFIER_WILDCARD = STATIC_GUID_NULL
KSDATAFORMAT_SPECIFIER_WILDCARD = GUID_NULL
STATIC_KSDATAFORMAT_SPECIFIER_FILENAME = (
    0xAA797B40,
    0xE974,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSDATAFORMAT_SPECIFIER_FILENAME = DEFINE_GUIDSTRUCT(
    "AA797B40-E974-11CF-A5D6-28DB04C10000"
)
KSDATAFORMAT_SPECIFIER_FILENAME = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_FILENAME
)
STATIC_KSDATAFORMAT_SPECIFIER_FILEHANDLE = (
    0x65E8773C,
    0x8F56,
    0x11D0,
    0xA3,
    0xB9,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSDATAFORMAT_SPECIFIER_FILEHANDLE = DEFINE_GUIDSTRUCT(
    "65E8773C-8F56-11D0-A3B9-00A0C9223196"
)
KSDATAFORMAT_SPECIFIER_FILEHANDLE = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_FILEHANDLE
)
# FORMAT_None
STATIC_KSDATAFORMAT_SPECIFIER_NONE = (
    0x0F6417D6,
    0xC318,
    0x11D0,
    0xA4,
    0x3F,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSDATAFORMAT_SPECIFIER_NONE = DEFINE_GUIDSTRUCT(
    "0F6417D6-C318-11D0-A43F-00A0C9223196"
)
KSDATAFORMAT_SPECIFIER_NONE = DEFINE_GUIDNAMED(KSDATAFORMAT_SPECIFIER_NONE)
# ===========================================================================
STATIC_KSPROPSETID_Quality = (
    0xD16AD380,
    0xAC1A,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSPROPSETID_Quality = DEFINE_GUIDSTRUCT(
    "D16AD380-AC1A-11CF-A5D6-28DB04C10000"
)
KSPROPSETID_Quality = DEFINE_GUIDNAMED(KSPROPSETID_Quality)


class KSPROPERTY_QUALITY(ENUM):
    KSPROPERTY_QUALITY_REPORT = 0
    KSPROPERTY_QUALITY_ERROR = 1



def DEFINE_KSPROPERTY_ITEM_QUALITY_REPORT(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_QUALITY.KSPROPERTY_QUALITY_REPORT,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSQUALITY),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_QUALITY_ERROR(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_QUALITY.KSPROPERTY_QUALITY_ERROR,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSERROR),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )

# ===========================================================================
STATIC_KSPROPSETID_Connection = (
    0x1D58C920,
    0xAC9B,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSPROPSETID_Connection = DEFINE_GUIDSTRUCT(
    "1D58C920-AC9B-11CF-A5D6-28DB04C10000"
)
KSPROPSETID_Connection = DEFINE_GUIDNAMED(KSPROPSETID_Connection)


class KSPROPERTY_CONNECTION(ENUM):
    KSPROPERTY_CONNECTION_STATE = 0
    KSPROPERTY_CONNECTION_PRIORITY = 1
    KSPROPERTY_CONNECTION_DATAFORMAT = 2
    KSPROPERTY_CONNECTION_ALLOCATORFRAMING = 3
    KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT = 4
    KSPROPERTY_CONNECTION_ACQUIREORDERING = 5
    KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX = 6
    KSPROPERTY_CONNECTION_STARTAT = 7



def DEFINE_KSPROPERTY_ITEM_CONNECTION_STATE(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_STATE,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSSTATE),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CONNECTION_PRIORITY(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_PRIORITY,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSPRIORITY),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CONNECTION_DATAFORMAT(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_DATAFORMAT,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        0,
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CONNECTION_ALLOCATORFRAMING(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_ALLOCATORFRAMING,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSALLOCATOR_FRAMING),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CONNECTION_ALLOCATORFRAMING_EX(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        0,
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CONNECTION_PROPOSEDATAFORMAT(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT,
        NULL,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSDATAFORMAT),
        Handler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CONNECTION_ACQUIREORDERING(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_ACQUIREORDERING,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(INT),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CONNECTION_STARTAT(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_STARTAT,
        NULL,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSRELATIVEEVENT),
        Handler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )

# ===========================================================================
# VRAM transport related propset
# ===========================================================================
STATIC_KSPROPSETID_MemoryTransport = (
    0xA3D1C5D,
    0x5243,
    0x4819,
    0x9E,
    0xD0,
    0xAE,
    0xE8,
    0x4,
    0x4C,
    0xEE,
    0x2B,
)
KSPROPSETID_MemoryTransport = DEFINE_GUIDSTRUCT(
    "0A3D1C5D-5243-4819-9ED0-AEE8044CEE2B"
)
KSPROPSETID_MemoryTransport = DEFINE_GUIDNAMED(KSPROPSETID_MemoryTransport)
# a value of zero is ignored
# Sets pin's memory transport mechanism e.g. VRAM or SYSMEM

KSPROPERTY_MEMORY_TRANSPORT = 1


def DEFINE_KSPROPERTY_ITEM_MEMORY_TRANSPORT(SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_MEMORY_TRANSPORT,
        NULL,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(BOOL),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )

# ===========================================================================

# pins flags

KSALLOCATOR_REQUIREMENTF_INPLACE_MODIFIER = 0x00000001
KSALLOCATOR_REQUIREMENTF_SYSTEM_MEMORY = 0x00000002
KSALLOCATOR_REQUIREMENTF_FRAME_INTEGRITY = 0x00000004
KSALLOCATOR_REQUIREMENTF_MUST_ALLOCATE = 0x00000008
KSALLOCATOR_REQUIREMENTF_SYSTEM_MEMORY_CUSTOM_ALLOCATION = 0x00000010
KSALLOCATOR_REQUIREMENTF_PREFERENCES_ONLY = 0x80000000
KSALLOCATOR_OPTIONF_COMPATIBLE = 0x00000001
KSALLOCATOR_OPTIONF_SYSTEM_MEMORY = 0x00000002

KSALLOCATOR_OPTIONF_VALID = 0x00000003
# pins extended framing flags

KSALLOCATOR_FLAG_PARTIAL_READ_SUPPORT = 0x00000010
KSALLOCATOR_FLAG_DEVICE_SPECIFIC = 0x00000020
KSALLOCATOR_FLAG_CAN_ALLOCATE = 0x00000040
KSALLOCATOR_FLAG_INSIST_ON_FRAMESIZE_RATIO = 0x00000080

# allocator pipes flags

# there is at least one data modification in a pipe
KSALLOCATOR_FLAG_NO_FRAME_INTEGRITY = 0x00000100
KSALLOCATOR_FLAG_MULTIPLE_OUTPUT = 0x00000200
KSALLOCATOR_FLAG_CYCLE = 0x00000400
# there is no framing dependency between neighbouring pipes.
KSALLOCATOR_FLAG_ALLOCATOR_EXISTS = 0x00000800
KSALLOCATOR_FLAG_INDEPENDENT_RANGES = 0x00001000
KSALLOCATOR_FLAG_ATTENTION_STEPPING = 0x00002000
KSALLOCATOR_FLAG_ENABLE_CACHED_MDL = 0x00004000
KSALLOCATOR_FLAG_2D_BUFFER_REQUIRED = 0x00008000


class KSALLOCATOR_FRAMING(ctypes.Structure):
    class _Union_1(ctypes.Union):
        _fields_ = [
            ('OptionsFlags', ULONG),
            ('RequirementsFlags', ULONG)
        ]

    class _Union_2(ctypes.Union):
        _fields_ = [
            ('FileAlignment', ULONG),
            ('FramePitch', LONG)
        ]

    _anonymous_ = ('_Union_1', '_Union_2')

    _fields_ = [
        ('_Union_1', _Union_1),
        ('PoolType', ULONG),
        ('Frames', ULONG),
        ('FrameSize', ULONG),
        ('_Union_2', _Union_2),
        ('Reserved', ULONG),


    ]


PKSALLOCATOR_FRAMING = POINTER(KSALLOCATOR_FRAMING)


class KS_FRAMING_RANGE(ctypes.Structure):
    _fields_ = [
        ('MinFrameSize', ULONG),
        ('MaxFrameSize', ULONG),
        ('Stepping', ULONG),
    ]


PKS_FRAMING_RANGE = POINTER(KS_FRAMING_RANGE)


class KS_FRAMING_RANGE_WEIGHTED(ctypes.Structure):
    _fields_ = [
        ('Range', KS_FRAMING_RANGE),
        ('InPlaceWeight', ULONG),
        ('NotInPlaceWeight', ULONG),
    ]


PKS_FRAMING_RANGE_WEIGHTED = POINTER(KS_FRAMING_RANGE_WEIGHTED)


class KS_COMPRESSION(ctypes.Structure):
    _fields_ = [
        ('RatioNumerator', ULONG),
        ('RatioDenominator', ULONG),
        ('RatioConstantMargin', ULONG),
    ]


PKS_COMPRESSION = POINTER(KS_COMPRESSION)


class KS_FRAMING_ITEM(ctypes.Structure):
    class _Union(ctypes.Union):
        _fields_ = [
            ('FileAlignment', ULONG),
            ('FramePitch', LONG)
        ]

    _anonymous_ = ('_Union',)
    _fields_ = [
        ('MemoryType', GUID),
        ('BusType', GUID),
        ('MemoryFlags', ULONG),
        ('BusFlags', ULONG),
        ('Flags', ULONG),
        ('Frames', ULONG),
        ('_Union', _Union),
        ('MemoryTypeWeight', ULONG),
        ('PhysicalRange', KS_FRAMING_RANGE),
        ('FramingRange', KS_FRAMING_RANGE_WEIGHTED),
    ]


PKS_FRAMING_ITEM = POINTER(KS_FRAMING_ITEM)



class KSALLOCATOR_FRAMING_EX(ctypes.Structure):
    _fields_ = [
        ('CountItems', ULONG),
        ('PinFlags', ULONG),
        ('OutputCompression', KS_COMPRESSION),
        ('PinWeight', ULONG),
        ('FramingItem', KS_FRAMING_ITEM * 1),
    ]


PKSALLOCATOR_FRAMING_EX = POINTER(KSALLOCATOR_FRAMING_EX)


KSMEMORY_TYPE_WILDCARD = GUID_NULL
STATIC_KSMEMORY_TYPE_WILDCARD = STATIC_GUID_NULL
KSMEMORY_TYPE_DONT_CARE = GUID_NULL
STATIC_KSMEMORY_TYPE_DONT_CARE = STATIC_GUID_NULL
KS_TYPE_DONT_CARE = GUID_NULL
STATIC_KS_TYPE_DONT_CARE = STATIC_GUID_NULL
STATIC_KSMEMORY_TYPE_SYSTEM = (
    0x091BB638,
    0x603F,
    0x11D1,
    0xB0,
    0x67,
    0x00,
    0xA0,
    0xC9,
    0x06,
    0x28,
    0x02,
)
KSMEMORY_TYPE_SYSTEM = DEFINE_GUIDSTRUCT(
    "091bb638-603f-11d1-b067-00a0c9062802"
)
KSMEMORY_TYPE_SYSTEM = DEFINE_GUIDNAMED(KSMEMORY_TYPE_SYSTEM)
STATIC_KSMEMORY_TYPE_USER = (
    0x8CB0FC28,
    0x7893,
    0x11D1,
    0xB0,
    0x69,
    0x00,
    0xA0,
    0xC9,
    0x06,
    0x28,
    0x02,
)
KSMEMORY_TYPE_USER = DEFINE_GUIDSTRUCT(
    "8cb0fc28-7893-11d1-b069-00a0c9062802"
)
KSMEMORY_TYPE_USER = DEFINE_GUIDNAMED(KSMEMORY_TYPE_USER)
STATIC_KSMEMORY_TYPE_KERNEL_PAGED = (
    0xD833F8F8,
    0x7894,
    0x11D1,
    0xB0,
    0x69,
    0x00,
    0xA0,
    0xC9,
    0x06,
    0x28,
    0x02,
)
KSMEMORY_TYPE_KERNEL_PAGED = DEFINE_GUIDSTRUCT(
    "d833f8f8-7894-11d1-b069-00a0c9062802"
)
KSMEMORY_TYPE_KERNEL_PAGED = DEFINE_GUIDNAMED(KSMEMORY_TYPE_KERNEL_PAGED)
STATIC_KSMEMORY_TYPE_KERNEL_NONPAGED = (
    0x4A6D5FC4,
    0x7895,
    0x11D1,
    0xB0,
    0x69,
    0x00,
    0xA0,
    0xC9,
    0x06,
    0x28,
    0x02,
)
KSMEMORY_TYPE_KERNEL_NONPAGED = DEFINE_GUIDSTRUCT(
    "4a6d5fc4-7895-11d1-b069-00a0c9062802"
)
KSMEMORY_TYPE_KERNEL_NONPAGED = DEFINE_GUIDNAMED(KSMEMORY_TYPE_KERNEL_NONPAGED)
# old KS clients did not specify the device memory type
STATIC_KSMEMORY_TYPE_DEVICE_UNKNOWN = (
    0x091BB639,
    0x603F,
    0x11D1,
    0xB0,
    0x67,
    0x00,
    0xA0,
    0xC9,
    0x06,
    0x28,
    0x02,
)
KSMEMORY_TYPE_DEVICE_UNKNOWN = DEFINE_GUIDSTRUCT(
    "091bb639-603f-11d1-b067-00a0c9062802"
)
KSMEMORY_TYPE_DEVICE_UNKNOWN = DEFINE_GUIDNAMED(KSMEMORY_TYPE_DEVICE_UNKNOWN)

# Helper framing macros.


STATIC_KSEVENTSETID_StreamAllocator = (
    0x75D95571,
    0x073C,
    0x11D0,
    0xA1,
    0x61,
    0x00,
    0x20,
    0xAF,
    0xD1,
    0x56,
    0xE4,
)
KSEVENTSETID_StreamAllocator = DEFINE_GUIDSTRUCT(
    "75d95571-073c-11d0-a161-0020afd156e4"
)
KSEVENTSETID_StreamAllocator = DEFINE_GUIDNAMED(KSEVENTSETID_StreamAllocator)


class KSEVENT_STREAMALLOCATOR(ENUM):
    KSEVENT_STREAMALLOCATOR_INTERNAL_FREEFRAME = 0
    KSEVENT_STREAMALLOCATOR_FREEFRAME = 1


STATIC_KSMETHODSETID_StreamAllocator = (
    0xCF6E4341,
    0xEC87,
    0x11CF,
    0xA1,
    0x30,
    0x00,
    0x20,
    0xAF,
    0xD1,
    0x56,
    0xE4,
)
KSMETHODSETID_StreamAllocator = DEFINE_GUIDSTRUCT(
    "cf6e4341-ec87-11cf-a130-0020afd156e4"
)
KSMETHODSETID_StreamAllocator = DEFINE_GUIDNAMED(KSMETHODSETID_StreamAllocator)


class KSMETHOD_STREAMALLOCATOR(ENUM):
    KSMETHOD_STREAMALLOCATOR_ALLOC = 0
    KSMETHOD_STREAMALLOCATOR_FREE = 1


def DEFINE_KSMETHOD_ITEM_STREAMALLOCATOR_ALLOC(Handler):
    return DEFINE_KSMETHOD_ITEM(
        KSMETHOD_STREAMALLOCATOR.KSMETHOD_STREAMALLOCATOR_ALLOC,
        KSMETHOD_TYPE_WRITE,
        Handler,
        ctypes.sizeof(KSMETHOD),
        ctypes.sizeof(PVOID),
        NULL,
    )


def DEFINE_KSMETHOD_ITEM_STREAMALLOCATOR_FREE(Handler):
    return DEFINE_KSMETHOD_ITEM(
        KSMETHOD_STREAMALLOCATOR.KSMETHOD_STREAMALLOCATOR_FREE,
        KSMETHOD_TYPE_READ,
        Handler,
        ctypes.sizeof(KSMETHOD),
        ctypes.sizeof(PVOID),
        NULL,
    )


STATIC_KSPROPSETID_StreamAllocator = (
    0xCF6E4342,
    0xEC87,
    0x11CF,
    0xA1,
    0x30,
    0x00,
    0x20,
    0xAF,
    0xD1,
    0x56,
    0xE4,
)
KSPROPSETID_StreamAllocator = DEFINE_GUIDSTRUCT(
    "cf6e4342-ec87-11cf-a130-0020afd156e4"
)
KSPROPSETID_StreamAllocator = DEFINE_GUIDNAMED(KSPROPSETID_StreamAllocator)


class KSPROPERTY_STREAMALLOCATOR(ENUM):
    KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE = 0
    KSPROPERTY_STREAMALLOCATOR_STATUS = 1


PFNALLOCATOR_ALLOCATEFRAME = POINTER(NTSTATUS)
PFNALLOCATOR_FREEFRAME = POINTER(VOID)


class  KSSTREAMALLOCATOR_FUNCTIONTABLE(ctypes.Structure):
    _fields_ = [
        ('AllocateFrame', PFNALLOCATOR_ALLOCATEFRAME),
        ('FreeFrame', PFNALLOCATOR_FREEFRAME)
    ]


PKSSTREAMALLOCATOR_FUNCTIONTABLE = POINTER(KSSTREAMALLOCATOR_FUNCTIONTABLE)


def DEFINE_KSPROPERTY_ITEM_STREAMALLOCATOR_FUNCTIONTABLE(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAMALLOCATOR.KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSSTREAMALLOCATOR_FUNCTIONTABLE),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_STREAMALLOCATOR_STATUS(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAMALLOCATOR.KSPROPERTY_STREAMALLOCATOR_STATUS,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSSTREAMALLOCATOR_STATUS),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


class KSSTREAMALLOCATOR_STATUS(ctypes.Structure):
    _fields_ = [
        ('Framing', KSALLOCATOR_FRAMING),
        ('AllocatedFrames', ULONG),
        ('Reserved', ULONG),
    ]


PKSSTREAMALLOCATOR_STATUS = POINTER(KSSTREAMALLOCATOR_STATUS)


class KSSTREAMALLOCATOR_STATUS_EX(ctypes.Structure):
    _fields_ = [
        ('Framing', KSALLOCATOR_FRAMING_EX),
        ('AllocatedFrames', ULONG),
        ('Reserved', ULONG),
    ]


PKSSTREAMALLOCATOR_STATUS_EX = POINTER(KSSTREAMALLOCATOR_STATUS_EX)


KSSTREAM_HEADER_OPTIONSF_SPLICEPOINT = 0x00000001
KSSTREAM_HEADER_OPTIONSF_PREROLL = 0x00000002
KSSTREAM_HEADER_OPTIONSF_DATADISCONTINUITY = 0x00000004
KSSTREAM_HEADER_OPTIONSF_TYPECHANGED = 0x00000008
KSSTREAM_HEADER_OPTIONSF_TIMEVALID = 0x00000010
KSSTREAM_HEADER_OPTIONSF_TIMEDISCONTINUITY = 0x00000040
KSSTREAM_HEADER_OPTIONSF_FLUSHONPAUSE = 0x00000080
KSSTREAM_HEADER_OPTIONSF_DURATIONVALID = 0x00000100
KSSTREAM_HEADER_OPTIONSF_ENDOFSTREAM = 0x00000200
KSSTREAM_HEADER_OPTIONSF_BUFFEREDTRANSFER = 0x00000400
KSSTREAM_HEADER_OPTIONSF_VRAM_DATA_TRANSFER = 0x00000800
KSSTREAM_HEADER_OPTIONSF_METADATA = 0x00001000
KSSTREAM_HEADER_OPTIONSF_ENDOFPHOTOSEQUENCE = 0x00002000

KSSTREAM_HEADER_OPTIONSF_FRAMEINFO = 0x00004000
# Start of MDL caching related definitions

KSSTREAM_HEADER_OPTIONSF_PERSIST_SAMPLE = 0x00008000
KSSTREAM_HEADER_OPTIONSF_SAMPLE_PERSISTED = 0x00010000

# This flag tells the user mode to look at frame completion numbers

KSSTREAM_HEADER_TRACK_COMPLETION_NUMBERS = 0x00020000

# End of MDL caching related definitions
KSSTREAM_HEADER_OPTIONSF_SECUREBUFFERTRANSFER = 0x00040000
KSSTREAM_HEADER_OPTIONSF_LOOPEDDATA = 0x80000000
# Metadata buffer passed down by user mode (mapped to SystemVa)
# Metadata buffer that driver will fill metadata to

# Additional space for UVC Attribute data to be stamped in the payload by the
# Inbox UVC driver


class KSTIME(ctypes.Structure):
    _fields_ = [
        ('Time', LONGLONG),
        ('Numerator', ULONG),
        ('Denominator', ULONG),
    ]


PKSTIME = POINTER(KSTIME)


class KSSTREAM_HEADER(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('TypeSpecificFlags', ULONG),
        ('PresentationTime', KSTIME),
        ('Duration', LONGLONG),
        ('FrameExtent', ULONG),
        ('DataUsed', ULONG),
        ('Data', PVOID),
        ('OptionsFlags', ULONG),
        ('Reserved', ULONG),
    ]


PKSSTREAM_HEADER = POINTER(KSSTREAM_HEADER)


class KSSTREAM_METADATA_INFO(ctypes.Structure):
    _fields_ = [
        ('BufferSize', ULONG),
        ('UsedSize', ULONG),
        ('Data', PVOID),
        ('SystemVa', PVOID),
        ('Flags', ULONG),
        ('Reserved', ULONG),
    ]


PKSSTREAM_METADATA_INFO = POINTER(KSSTREAM_METADATA_INFO)


class KSSTREAM_UVC_METADATATYPE_TIMESTAMP(ctypes.Structure):
    class _Union(ctypes.Union):
        class _Struct(ctypes.Structure):
            _fields_ = [
                ('Counter', USHORT, 11),
                ('Reserved', USHORT, 5)
            ]

        _anonymous = ('_Struct',)
        _fields_ = [
            ('_Struct', _Struct),
            ('SCRToken', USHORT),
        ]

    _anonymous_ = ('_Union',)
    _fields_ = [
        ('PresentationTimeStamp', ULONG),
        ('SourceClockReference', ULONG),
        ('_Union', _Union),

        ('Reserved0', USHORT),
        ('Reserved1', ULONG),
    ]


PKSSTREAM_UVC_METADATATYPE_TIMESTAMP = POINTER(
    KSSTREAM_UVC_METADATATYPE_TIMESTAMP
)


class KSSTREAM_UVC_METADATA(ctypes.Structure):
    _fields_ = [
        ('StartOfFrameTimestamp', KSSTREAM_UVC_METADATATYPE_TIMESTAMP),
        ('EndOfFrameTimestamp', KSSTREAM_UVC_METADATATYPE_TIMESTAMP),
    ]


PKSSTREAM_UVC_METADATA = POINTER(KSSTREAM_UVC_METADATA)

KSSTREAM_UVC_SECURE_ATTRIBUTE_SIZE = 0x00002000


class KSPIN_MDL_CACHING_EVENT(ENUM):
    KSPIN_MDL_CACHING_NOTIFY_CLEANUP = 0
    KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT = 1
    KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT = 2
    KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE = 3


class KSPIN_MDL_CACHING_NOTIFICATION(ctypes.Structure):
    _fields_ = [
        ('Event', KSPIN_MDL_CACHING_EVENT),
        ('Buffer', PVOID),
    ]


PKSPIN_MDL_CACHING_NOTIFICATION = POINTER(KSPIN_MDL_CACHING_NOTIFICATION)


class KSPIN_MDL_CACHING_NOTIFICATION32(ctypes.Structure):
    _fields_ = [
        ('Event', KSPIN_MDL_CACHING_EVENT),
        ('Buffer', ULONG),
    ]


PKSPIN_MDL_CACHING_NOTIFICATION32 = POINTER(KSPIN_MDL_CACHING_NOTIFICATION32)


STATIC_KSPROPSETID_StreamInterface = (
    0x1FDD8EE1,
    0x9CD3,
    0x11D0,
    0x82,
    0xAA,
    0x00,
    0x00,
    0xF8,
    0x22,
    0xFE,
    0x8A,
)
KSPROPSETID_StreamInterface = DEFINE_GUIDSTRUCT(
    "1fdd8ee1-9cd3-11d0-82aa-0000f822fe8a"
)
KSPROPSETID_StreamInterface = DEFINE_GUIDNAMED(KSPROPSETID_StreamInterface)
STATIC_KSPROPSETID_Stream = (
    0x65AABA60,
    0x98AE,
    0x11CF,
    0xA1,
    0x0D,
    0x00,
    0x20,
    0xAF,
    0xD1,
    0x56,
    0xE4,
)
KSPROPSETID_Stream = DEFINE_GUIDSTRUCT(
    "65aaba60-98ae-11cf-a10d-0020afd156e4"
)
KSPROPSETID_Stream = DEFINE_GUIDNAMED(KSPROPSETID_Stream)


class KSPROPERTY_STREAMINTERFACE(ENUM):
    KSPROPERTY_STREAMINTERFACE_HEADERSIZE = 0


def DEFINE_KSPROPERTY_ITEM_STREAMINTERFACE_HEADERSIZE(GetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAMINTERFACE.KSPROPERTY_STREAMINTERFACE_HEADERSIZE,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(ULONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


class KSPROPERTY_STREAM(ENUM):
    KSPROPERTY_STREAM_ALLOCATOR = 0
    KSPROPERTY_STREAM_QUALITY = 1
    KSPROPERTY_STREAM_DEGRADATION = 2
    KSPROPERTY_STREAM_MASTERCLOCK = 3
    KSPROPERTY_STREAM_TIMEFORMAT = 4
    KSPROPERTY_STREAM_PRESENTATIONTIME = 5
    KSPROPERTY_STREAM_PRESENTATIONEXTENT = 6
    KSPROPERTY_STREAM_FRAMETIME = 7
    KSPROPERTY_STREAM_RATECAPABILITY = 8
    KSPROPERTY_STREAM_RATE = 9
    KSPROPERTY_STREAM_PIPE_ID = 10


def DEFINE_KSPROPERTY_ITEM_STREAM_ALLOCATOR(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAM.KSPROPERTY_STREAM_ALLOCATOR,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(HANDLE),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_STREAM_QUALITY(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAM.KSPROPERTY_STREAM_QUALITY,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSQUALITY_MANAGER),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_STREAM_DEGRADATION(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAM.KSPROPERTY_STREAM_DEGRADATION,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        0,
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_STREAM_MASTERCLOCK(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAM.KSPROPERTY_STREAM_MASTERCLOCK,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(HANDLE),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_STREAM_TIMEFORMAT(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAM.KSPROPERTY_STREAM_TIMEFORMAT,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(GUID),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_STREAM_PRESENTATIONTIME(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAM.KSPROPERTY_STREAM_PRESENTATIONTIME,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSTIME),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_STREAM_PRESENTATIONEXTENT(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAM.KSPROPERTY_STREAM_PRESENTATIONEXTENT,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(LONGLONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_STREAM_FRAMETIME(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAM.KSPROPERTY_STREAM_FRAMETIME,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSFRAMETIME),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_STREAM_RATECAPABILITY(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAM.KSPROPERTY_STREAM_RATECAPABILITY,
        Handler,
        ctypes.sizeof(KSRATE_CAPABILITY),
        ctypes.sizeof(KSRATE),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_STREAM_RATE(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAM.KSPROPERTY_STREAM_RATE,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSRATE),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_STREAM_PIPE_ID(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_STREAM.KSPROPERTY_STREAM_PIPE_ID,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(HANDLE),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


class KSPPROPERTY_ALLOCATOR_MDLCACHING(ENUM):
    KSPROPERTY_ALLOCATOR_CLEANUP_CACHEDMDLPAGES = 1


def DEFINE_KSPROPERTY_ITEM_CONNECTION_MDLCACHING(SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPPROPERTY_ALLOCATOR_MDLCACHING.KSPROPERTY_ALLOCATOR_CLEANUP_CACHEDMDLPAGES,
        NULL,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSPIN_MDL_CACHING_NOTIFICATION),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


STATIC_KSPROPSETID_PinMDLCacheClearProp = (
    0xBD718A7B,
    0x97FC,
    0x40C7,
    0x88,
    0xCE,
    0xD3,
    0xFF,
    0x6,
    0xF5,
    0x5B,
    0x16,
)
KSPROPSETID_PinMDLCacheClearProp = DEFINE_GUIDSTRUCT(
    "BD718A7B-97FC-40C7-88CE-D3FF06F55B16"
)
KSPROPSETID_PinMDLCacheClearProp = DEFINE_GUIDNAMED(
    KSPROPSETID_PinMDLCacheClearProp
)


class KSQUALITY_MANAGER(ctypes.Structure):
    _fields_ = [
        ('QualityManager', HANDLE),
        ('Context', PVOID),
    ]


PKSQUALITY_MANAGER = POINTER(KSQUALITY_MANAGER)


class KSFRAMETIME(ctypes.Structure):
    _fields_ = [
        ('Duration', LONGLONG),
        ('FrameFlags', ULONG),
        ('Reserved', ULONG),
    ]


PKSFRAMETIME = POINTER(KSFRAMETIME)

KSFRAMETIME_VARIABLESIZE = 0x00000001


class KSRATE(ctypes.Structure):
    _fields_ = [
        ('PresentationStart', LONGLONG),
        ('Duration', LONGLONG),
        ('Interface', KSPIN_INTERFACE),
        ('Rate', LONG),
        ('Flags', ULONG),
    ]


PKSRATE = POINTER(KSRATE)

KSRATE_NOPRESENTATIONSTART = 0x00000001
KSRATE_NOPRESENTATIONDURATION = 0x00000002


class KSRATE_CAPABILITY(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Rate', KSRATE),
    ]


PKSRATE_CAPABILITY = POINTER(KSRATE_CAPABILITY)


STATIC_KSPROPSETID_Clock = (
    0xDF12A4C0,
    0xAC17,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSPROPSETID_Clock = DEFINE_GUIDSTRUCT(
    "DF12A4C0-AC17-11CF-A5D6-28DB04C10000"
)
KSPROPSETID_Clock = DEFINE_GUIDNAMED(KSPROPSETID_Clock)

NANOSECONDS = 0x00989680


class KSCLOCK_CREATE(ctypes.Structure):
    _fields_ = [
        ('CreateFlags', ULONG),
    ]


PKSCLOCK_CREATE = POINTER(KSCLOCK_CREATE)


class KSCORRELATED_TIME(ctypes.Structure):
    _fields_ = [
        ('Time', LONGLONG),
        ('SystemTime', LONGLONG),
    ]


PKSCORRELATED_TIME = POINTER(KSCORRELATED_TIME)


class KSRESOLUTION(ctypes.Structure):
    _fields_ = [
        ('Granularity', LONGLONG),
        ('Error', LONGLONG),
    ]


PKSRESOLUTION = POINTER(KSRESOLUTION)


class KSPROPERTY_CLOCK(ENUM):
    KSPROPERTY_CLOCK_TIME = 0
    KSPROPERTY_CLOCK_PHYSICALTIME = 1
    KSPROPERTY_CLOCK_CORRELATEDTIME = 2
    KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME = 3
    KSPROPERTY_CLOCK_RESOLUTION = 4
    KSPROPERTY_CLOCK_STATE = 5
    KSPROPERTY_CLOCK_FUNCTIONTABLE = 7


PKSDEFAULTCLOCK = PVOID


def DEFINE_KSPROPERTY_ITEM_CLOCK_TIME(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_TIME,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(LONGLONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CLOCK_PHYSICALTIME(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_PHYSICALTIME,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(LONGLONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CLOCK_CORRELATEDTIME(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_CORRELATEDTIME,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSCORRELATED_TIME),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CLOCK_CORRELATEDPHYSICALTIME(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSCORRELATED_TIME),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CLOCK_RESOLUTION(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_RESOLUTION,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSRESOLUTION),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_CLOCK_STATE(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_STATE,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSSTATE),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )

PFNKSCLOCK_GETTIME = POINTER(LONGLONG)
PFNKSCLOCK_CORRELATEDTIME = POINTER(LONGLONG)


class KSCLOCK_FUNCTIONTABLE(ctypes.Structure):
    _fields_ = [
        ('GetTime', PFNKSCLOCK_GETTIME),
        ('GetPhysicalTime', PFNKSCLOCK_GETTIME),
        ('GetCorrelatedTime', PFNKSCLOCK_CORRELATEDTIME),
        ('GetCorrelatedPhysicalTime', PFNKSCLOCK_CORRELATEDTIME)
    ]


PKSCLOCK_FUNCTIONTABLE = POINTER(KSCLOCK_FUNCTIONTABLE)


def DEFINE_KSPROPERTY_ITEM_CLOCK_FUNCTIONTABLE(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_FUNCTIONTABLE,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSCLOCK_FUNCTIONTABLE),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


STATIC_KSEVENTSETID_Clock = (
    0x364D8E20,
    0x62C7,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSEVENTSETID_Clock = DEFINE_GUIDSTRUCT(
    "364D8E20-62C7-11CF-A5D6-28DB04C10000"
)
KSEVENTSETID_Clock = DEFINE_GUIDNAMED(KSEVENTSETID_Clock)


class KSEVENT_CLOCK_POSITION(ENUM):
    KSEVENT_CLOCK_INTERVAL_MARK = 0
    KSEVENT_CLOCK_POSITION_MARK = 1


STATIC_KSEVENTSETID_Connection = (
    0x7F4BCBE0,
    0x9EA5,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSEVENTSETID_Connection = DEFINE_GUIDSTRUCT(
    "7f4bcbe0-9ea5-11cf-a5d6-28db04c10000"
)
KSEVENTSETID_Connection = DEFINE_GUIDNAMED(KSEVENTSETID_Connection)


class KSEVENT_CONNECTION(ENUM):
    KSEVENT_CONNECTION_POSITIONUPDATE = 0
    KSEVENT_CONNECTION_DATADISCONTINUITY = 1
    KSEVENT_CONNECTION_TIMEDISCONTINUITY = 2
    KSEVENT_CONNECTION_PRIORITY = 3
    KSEVENT_CONNECTION_ENDOFSTREAM = 4


class KSQUALITY(ctypes.Structure):
    _fields_ = [
        ('Context', PVOID),
        ('Proportion', ULONG),
        ('DeltaTime', LONGLONG),
    ]


PKSQUALITY = POINTER(KSQUALITY)


class KSERROR(ctypes.Structure):
    _fields_ = [
        ('Context', PVOID),
        ('Status', ULONG),
    ]


PKSERROR = POINTER(KSERROR)


class KSDEVICE_THERMAL_STATE(ENUM):
    KSDEVICE_THERMAL_STATE_LOW = 0
    KSDEVICE_THERMAL_STATE_HIGH = 1


STATIC_KSEVENTSETID_Device = (
    0x288296EC,
    0x9F94,
    0x41B4,
    0xA1,
    0x53,
    0xAA,
    0x31,
    0xAE,
    0xEC,
    0xB3,
    0x3F,
)
KSEVENTSETID_Device = DEFINE_GUIDSTRUCT(
    "288296EC-9F94-41b4-A153-AA31AEECB33F"
)
KSEVENTSETID_Device = DEFINE_GUIDNAMED(KSEVENTSETID_Device)


class KSEVENT_DEVICE(ENUM):
    KSEVENT_DEVICE_LOST = 0
    KSEVENT_DEVICE_PREEMPTED = 1
    KSEVENT_DEVICE_THERMAL_HIGH = 2
    KSEVENT_DEVICE_THERMAL_LOW = 3


KSDEGRADE = KSIDENTIFIER
PKSDEGRADE = POINTER(KSIDENTIFIER)
STATIC_KSDEGRADESETID_Standard = (
    0x9F564180,
    0x704C,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSDEGRADESETID_Standard = DEFINE_GUIDSTRUCT(
    "9F564180-704C-11D0-A5D6-28DB04C10000"
)
KSDEGRADESETID_Standard = DEFINE_GUIDNAMED(KSDEGRADESETID_Standard)


class KSDEGRADE_STANDARD(ENUM):
    KSDEGRADE_STANDARD_SAMPLE = 0
    KSDEGRADE_STANDARD_QUALITY = 1
    KSDEGRADE_STANDARD_COMPUTATION = 2
    KSDEGRADE_STANDARD_SKIP = 3


def DEFINE_KSMETHOD_ITEM(
    MethodId,
    Flags,
    MethodHandler,
    MinMethod,
    MinData,
    SupportHandler
):
    return (
        MethodId,
        PFNKSHANDLER(MethodHandler),
        MinMethod,
        MinData,
        SupportHandler,
        Flags
    )


KSPROBE_STREAMREAD = 0x00000000
KSPROBE_STREAMWRITE = 0x00000001
KSPROBE_ALLOCATEMDL = 0x00000010
KSPROBE_PROBEANDLOCK = 0x00000020
KSPROBE_SYSTEMADDRESS = 0x00000040
KSPROBE_MODIFY = 0x00000200
KSPROBE_STREAMWRITEMODIFY = KSPROBE_MODIFY | KSPROBE_STREAMWRITE
KSPROBE_ALLOWFORMATCHANGE = 0x00000080
KSSTREAM_READ = KSPROBE_STREAMREAD
KSSTREAM_WRITE = KSPROBE_STREAMWRITE
KSSTREAM_PAGED_DATA = 0x00000000
KSSTREAM_NONPAGED_DATA = 0x00000100
KSSTREAM_SYNCHRONOUS = 0x00001000
KSSTREAM_FAILUREEXCEPTION = 0x00002000


class KSPROPERTY_MEMBERSLIST(ctypes.Structure):
    _fields_ = [
        ('MembersHeader', KSPROPERTY_MEMBERSHEADER),
        ('Members', POINTER(VOID)),
    ]


PKSPROPERTY_MEMBERSLIST = POINTER(KSPROPERTY_MEMBERSLIST)


class KSPROPERTY_VALUES(ctypes.Structure):
    _fields_ = [
        ('PropTypeSet', KSIDENTIFIER),
        ('MembersListCount', ULONG),
        ('MembersList', POINTER(KSPROPERTY_MEMBERSLIST)),
    ]


PKSPROPERTY_VALUES = POINTER(KSPROPERTY_VALUES)


KSEVENT_ENTRY_DELETED = 0x00000001
KSEVENT_ENTRY_ONESHOT = 0x00000002
KSEVENT_ENTRY_BUFFERED = 0x00000004


class KSEVENTS_LOCKTYPE(ENUM):
    KSEVENTS_NONE = 0
    KSEVENTS_SPINLOCK = 1
    KSEVENTS_MUTEX = 2
    KSEVENTS_FMUTEX = 3
    KSEVENTS_FMUTEXUNSAFE = 4
    KSEVENTS_INTERRUPT = 5
    KSEVENTS_ERESOURCE = 6


KSDISPATCH_FASTIO = 0x80000000
KSCREATE_ITEM_SECURITYCHANGED = 0x00000001
KSCREATE_ITEM_WILDCARD = 0x00000002
KSCREATE_ITEM_NOPARAMETERS = 0x00000004
KSCREATE_ITEM_FREEONSTOP = 0x00000008
KSDEVICE_HEADER = PVOID
KSOBJECT_HEADER = PVOID


class KSCOMPLETION_INVOCATION(ENUM):
    KsInvokeOnSuccess = 1
    KsInvokeOnError = 2
    KsInvokeOnCancel = 4


class KSLIST_ENTRY_LOCATION(ENUM):
    KsListEntryTail = 0
    KsListEntryHead = 1


class KSIRP_REMOVAL_OPERATION(ENUM):
    KsAcquireOnly = 0
    KsAcquireAndRemove = 1
    KsAcquireOnlySingleItem = 2
    KsAcquireAndRemoveOnlySingleItem = 3


class KSSTACK_USE(ENUM):
    KsStackCopyToNewLocation = 0
    KsStackReuseCurrentLocation = 1
    KsStackUseNewLocation = 2


class KSTARGET_STATE(ENUM):
    KSTARGET_STATE_DISABLED = 0
    KSTARGET_STATE_ENABLED = 1


BUS_INTERFACE_REFERENCE_VERSION = 0x00000100

STATIC_REFERENCE_BUS_INTERFACE = STATIC_KSMEDIUMSETID_Standard
REFERENCE_BUS_INTERFACE = KSMEDIUMSETID_Standard


STATIC_GUID_BUS_INTERFACE_MEDIUMS = (
    0x4EC35C3E,
    0x201B,
    0x11D2,
    0x87,
    0x45,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
GUID_BUS_INTERFACE_MEDIUMS = DEFINE_GUIDSTRUCT(
    "4EC35C3E-201B-11D2-8745-00A0C9223196"
)
GUID_BUS_INTERFACE_MEDIUMS = DEFINE_GUIDNAMED(GUID_BUS_INTERFACE_MEDIUMS)


class KSPROPERTY_SERIALHDR(ctypes.Structure):
    _fields_ = [
        ('PropertySet', GUID),
        ('Count', ULONG),
    ]


PKSPROPERTY_SERIALHDR = POINTER(KSPROPERTY_SERIALHDR)


class KSPROPERTY_SERIAL(ctypes.Structure):
    _fields_ = [
        ('PropTypeSet', KSIDENTIFIER),
        ('Id', ULONG),
        ('PropertyLength', ULONG),
    ]


PKSPROPERTY_SERIAL = POINTER(KSPROPERTY_SERIAL)


IOCTL_KS_HANDSHAKE = CTL_CODE(
    FILE_DEVICE_KS,
    0x00000007,
    METHOD_NEITHER,
    FILE_ANY_ACCESS,
)


class KSHANDSHAKE(ctypes.Structure):
    _fields_ = [
        ('ProtocolId', GUID),
        ('Argument1', PVOID),
        ('Argument2', PVOID),
    ]


PKSHANDSHAKE = POINTER(KSHANDSHAKE)


class _KSGATE(ctypes.Structure):
    pass


KSGATE = _KSGATE
PKSGATE = POINTER(_KSGATE)

_KSGATE._fields_ = [
    ('Count', LONG),
    ('NextGate', PKSGATE),
]

KSOBJECT_BAG = PVOID

MIN_DEV_VER_FOR_QI = 0x00000100

KSDEVICE_DESCRIPTOR_VERSION = 0x00000100

KSDEVICE_DESCRIPTOR_VERSION_2 = 0x00000110
MIN_DEV_VER_FOR_FLAGS = 0x00000110
KSDEVICE_FLAG_ENABLE_REMOTE_WAKEUP = 0x00000001
KSDEVICE_FLAG_LOWPOWER_PASSTHROUGH = 0x00000002
KSDEVICE_FLAG_ENABLE_QUERYINTERFACE = 0x00000004
KSFILTER_DESCRIPTOR_VERSION = -1
KSFILTER_FLAG_DISPATCH_LEVEL_PROCESSING = 0x00000001
KSFILTER_FLAG_CRITICAL_PROCESSING = 0x00000002
KSFILTER_FLAG_HYPERCRITICAL_PROCESSING = 0x00000004
KSFILTER_FLAG_RECEIVE_ZERO_LENGTH_SAMPLES = 0x00000008
KSFILTER_FLAG_DENY_USERMODE_ACCESS = 0x80000000
KSFILTER_FLAG_PRIORITIZE_REFERENCEGUID = 0x00000010


KSPIN_FLAG_DISPATCH_LEVEL_PROCESSING = KSFILTER_FLAG_DISPATCH_LEVEL_PROCESSING
KSPIN_FLAG_CRITICAL_PROCESSING = KSFILTER_FLAG_CRITICAL_PROCESSING
KSPIN_FLAG_HYPERCRITICAL_PROCESSING = KSFILTER_FLAG_HYPERCRITICAL_PROCESSING
KSPIN_FLAG_ASYNCHRONOUS_PROCESSING = 0x00000008
KSPIN_FLAG_DO_NOT_INITIATE_PROCESSING = 0x00000010
KSPIN_FLAG_INITIATE_PROCESSING_ON_EVERY_ARRIVAL = 0x00000020
KSPIN_FLAG_FRAMES_NOT_REQUIRED_FOR_PROCESSING = 0x00000040
KSPIN_FLAG_ENFORCE_FIFO = 0x00000080
KSPIN_FLAG_GENERATE_MAPPINGS = 0x00000100
KSPIN_FLAG_DISTINCT_TRAILING_EDGE = 0x00000200
KSPIN_FLAG_PROCESS_IN_RUN_STATE_ONLY = 0x00010000
KSPIN_FLAG_SPLITTER = 0x00020000
KSPIN_FLAG_USE_STANDARD_TRANSPORT = 0x00040000
KSPIN_FLAG_DO_NOT_USE_STANDARD_TRANSPORT = 0x00080000
KSPIN_FLAG_FIXED_FORMAT = 0x00100000
KSPIN_FLAG_GENERATE_EOS_EVENTS = 0x00200000
KSPIN_FLAG_RENDERER = (
    KSPIN_FLAG_PROCESS_IN_RUN_STATE_ONLY |
    KSPIN_FLAG_GENERATE_EOS_EVENTS
)
KSPIN_FLAG_IMPLEMENT_CLOCK = 0x00400000
KSPIN_FLAG_SOME_FRAMES_REQUIRED_FOR_PROCESSING = 0x00800000
KSPIN_FLAG_PROCESS_IF_ANY_IN_RUN_STATE = 0x01000000
KSPIN_FLAG_DENY_USERMODE_ACCESS = 0x80000000


class KSOBJECTTYPE(ENUM):
    KsObjectTypeDevice = 0
    KsObjectTypeFilterFactory = 1
    KsObjectTypeFilter = 2
    KsObjectTypePin = 3


STATIC_IID_IKsControl = (
    0x28F54685,
    0x06FD,
    0x11D2,
    0xB2,
    0x7A,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
IID_IKsControl = DEFINE_GUID(
    0x28F54685,
    0x06FD,
    0x11D2,
    0xB2,
    0x7A,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96
)
STATIC_IID_IKsFastClock = (
    0xC9902485,
    0xC180,
    0x11D2,
    0x84,
    0x73,
    0xD4,
    0x23,
    0x94,
    0x45,
    0x9E,
    0x5E,
)
IID_IKsFastClock = DEFINE_GUID(
    0xC9902485,
    0xC180,
    0x11D2,
    0x84,
    0x73,
    0xD4,
    0x23,
    0x94,
    0x45,
    0x9E,
    0x5E
)
STATIC_IID_IKsDeviceFunctions = (
    0xE234F2E2,
    0xBD69,
    0x4F8C,
    0xB3,
    0xF2,
    0x7C,
    0xD7,
    0x9E,
    0xD4,
    0x66,
    0xBD,
)
IID_IKsDeviceFunctions = DEFINE_GUID(
    0xE234F2E2,
    0xBD69,
    0x4F8C,
    0xB3,
    0xF2,
    0x7C,
    0xD7,
    0x9E,
    0xD4,
    0x66,
    0xBD
)


def MAKEINTRESOURCE(res):
    return res


RT_STRING = MAKEINTRESOURCE(6)
RT_RCDATA = MAKEINTRESOURCE(10)


class KSSTREAM_POINTER_STATE(ENUM):
    KSSTREAM_POINTER_STATE_UNLOCKED = 0
    KSSTREAM_POINTER_STATE_LOCKED = 1


__all__ = (
    'KSEVENTF_SEMAPHORE_OBJECT', 'KSCATEGORY_MIXER', 'KSPROPSETID_Clock',
    'DEFINE_KSPROPERTY_ITEM_PIN_PROPOSEDATAFORMAT', 'KSMETHOD_TYPE_SEND',
    'KSPIN_FLAG_USE_STANDARD_TRANSPORT', 'KSPIN_FLAG_GENERATE_MAPPINGS',
    'KSSTREAM_FAILUREEXCEPTION', 'KSEVENTDATA',
    'DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_AVAILABLE', 'KSPROPERTY_TYPE_SET',
    'KSPIN_FLAG_PROCESS_IN_RUN_STATE_ONLY',
    'KSPIN_FLAG_IMPLEMENT_CLOCK', 'KSPROPERTY_TYPE_FSFILTERSCOPE',
    'KSFILTER_FLAG_DISPATCH_LEVEL_PROCESSING', 'KSMFT_CATEGORY_VIDEO_DECODER',
    'KSDATAFORMAT_SPECIFIER_WILDCARD', 'KS_TYPE_DONT_CARE', 'KSSTRING_Filter',
    'STATIC_KSPROPSETID_MediaSeeking', 'IOCTL_KS_ENABLE_EVENT',
    'STATIC_KSNAME_TopologyNode', 'KSALLOCATOR_REQUIREMENTF_FRAME_INTEGRITY',
    'DEFINE_KSPROPERTY_ITEM_STREAM_PRESENTATIONTIME', 'KSPROBE_SYSTEMADDRESS',
    'KSDATAFORMAT_SUBTYPE_NONE', 'KSEVENTSETID_Connection', 'KSSTREAM_WRITE',
    'DEFINE_KSPROPERTY_ITEM_CONNECTION_ALLOCATORFRAMING_EX', 'KSPROBE_MODIFY',
    'DEFINE_KSPROPERTY_ITEM_CLOCK_STATE',
    'DEFINE_KSPROPERTY_ITEM_STREAM_RATE',  'KSNAME_Pin',
    'KSSTREAM_HEADER_OPTIONSF_DURATIONVALID',
    'KSPIN_FLAG_DENY_USERMODE_ACCESS', 'STATIC_KSEVENTSETID_Connection',
    'DEFINE_KSPROPERTY_ITEM_TOPOLOGY_NODES', 'KSPROPERTY_TYPE_DEFAULTVALUES',
    'KSPIN_FLAG_HYPERCRITICAL_PROCESSING', 'KSEVENTSETID_PinCapsChange',
    'KSPROPERTY_TYPE_UNSERIALIZESET', 'KSEVENTF_KSWORKITEM',
    'DEFINE_KSPROPERTY_ITEM_CONNECTION_PROPOSEDATAFORMAT', 'KSPRIORITY_HIGH',
    'DEFINE_KSPROPERTY_ITEM_STREAMINTERFACE_HEADERSIZE', 'DEFINE_GUIDSTRUCT',
    'KSPROPSETID_StreamAllocator',
    'DEFINE_KSMETHOD_ITEM_STREAMIO_READ',
    'KSPROPERTY_PIN_FLAGS_MASK',  'KSFILTER_NODE',
    'DEFINE_KSPROPERTY_ITEM_CONNECTION_STATE', 'STATIC_KSTIME_FORMAT_SAMPLE',
    'GUID_BUS_INTERFACE_MEDIUMS', 'KSFILTER_FLAG_DENY_USERMODE_ACCESS',
    'KSPIN_FLAG_DO_NOT_USE_STANDARD_TRANSPORT',
    'DEFINE_KSMETHOD_ITEM_STREAMIO_WRITE', 'KSPROPSETID_Connection',
    'KSSTREAM_HEADER_OPTIONSF_SECUREBUFFERTRANSFER', 'KSCATEGORY_CAPTURE',
    'STATIC_KSCATEGORY_CAPTURE', 'KSPROBE_STREAMWRITE', 'KSPIN_FLAG_SPLITTER',
    'KSPROPSETID_PinMDLCacheClearProp', 'KSMFT_CATEGORY_AUDIO_EFFECT',
    'DEFINE_KSPROPERTY_ITEM_CLOCK_RESOLUTION', 'MIN_DEV_VER_FOR_FLAGS',
    'KSDATAFORMAT_BIT_TEMPORAL_COMPRESSION', 'KSDATAFORMAT_SPECIFIER_NONE',
    'KSEVENT_TYPE_QUERYBUFFER',  'RT_STRING',
    'KSINTERFACESETID_FileIo', 'DEFINE_KSPROPERTY_ITEM_STREAM_RATECAPABILITY',
    'DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_STOPPOSITION', 'KSEVENTSETID_Device',
    'KSSTREAM_HEADER_OPTIONSF_ENDOFSTREAM', 'STATIC_KSNAME_Filter', 'KSSTATE',
    'DEFINE_KSPROPERTY_ITEM_STREAM_DEGRADATION',
    'KSPROPERTY_TYPE_COPYPAYLOAD', 'STATIC_KSMFT_CATEGORY_AUDIO_ENCODER',
    'STATIC_KSMFT_CATEGORY_DEMULTIPLEXER', 'STATIC_KSPROPSETID_Clock',
    'DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_POSITIONS', 'KSTIME_FORMAT_BYTE',
    'KSPIN_FLAG_DO_NOT_INITIATE_PROCESSING', 'KSINSTANCE_INDETERMINATE',
    'DEFINE_KSPROPERTY_ITEM_QUALITY_REPORT',
    'STATIC_KSMFT_CATEGORY_AUDIO_DECODER',
    'KSALLOCATOR_REQUIREMENTF_PREFERENCES_ONLY',
    'KSPROPERTY_MEMBER_FLAG_BASICSUPPORT_UNIFORM',
    'KSFILTER_FLAG_PRIORITIZE_REFERENCEGUID', 'KSMFT_CATEGORY_VIDEO_EFFECT',
    'KSALLOCATOR_OPTIONF_SYSTEM_MEMORY', 'KSDATAFORMAT_TEMPORAL_COMPRESSION',
    'STATIC_KSDEGRADESETID_Standard', 'KSSTREAM_HEADER_OPTIONSF_TIMEVALID',
    'KSPROPERTY_MEMBER_STEPPEDRANGES', 'STATIC_KSMEDIUMSETID_Standard',
    'KSSTREAM_PAGED_DATA', 'DEFINE_KSPROPERTY_ITEM_CONNECTION_MDLCACHING',
    'KSMETHOD_TYPE_MODIFY', 'KSCATEGORY_BRIDGE',
    'KSMEMORY_TYPE_USER', 'KSFILTER_FLAG_CRITICAL_PROCESSING', 'KSNAME_Clock',
    'KSDATAFORMAT_ATTRIBUTES', 'KSMETHOD_TYPE_TOPOLOGY', 'KSEVENTSETID_Clock',
    'DEFINE_KSPROPERTY_ITEM_CLOCK_PHYSICALTIME', 'KSMEMORY_TYPE_SYSTEM',
    'DEFINE_KSPROPERTY_ITEM_PIN_CATEGORY',
    'DEFINE_KSPROPERTY_ITEM_PIN_CTYPES', 'STATIC_KSMETHODSETID_StreamIo',
    'STATIC_KSNAME_Clock', 'RT_RCDATA',
    'DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_TIMEFORMAT',
    'KSPROPERTY_MEMBER_FLAG_BASICSUPPORT_MULTICHANNEL', 'KSPROPSETID_Quality',
    'KSPROPERTY_TYPE_BASICSUPPORT',
    'DEFINE_KSPROPERTY_ITEM_STREAMALLOCATOR_STATUS', 'KSPRIORITY_EXCLUSIVE',
    'DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_CONVERTTIMEFORMAT', 'KSPRIORITY_LOW',
    'KSALLOCATOR_FLAG_INSIST_ON_FRAMESIZE_RATIO',
    'DEFINE_KSPROPERTY_ITEM_PIN_DATAINTERSECTION', 'KSTIME_FORMAT_MEDIA_TIME',
    'DEFINE_KSPROPERTY_ITEM_CLOCK_CORRELATEDPHYSICALTIME', 'KSPROPSETID_GM',
    'DEFINE_KSPROPERTY_ITEM_STREAM_PRESENTATIONEXTENT', 'KSMETHOD_TYPE_WRITE',
    'KSPROBE_ALLOWFORMATCHANGE',
    'KSSTREAM_HEADER_OPTIONSF_ENDOFPHOTOSEQUENCE', 'KSSTRING_TopologyNode',
    'STATIC_KSCATEGORY_QUALITY', 'DEFINE_KSPROPERTY_ITEM_PIN_COMMUNICATION',
    'KSDEVICE_DESCRIPTOR_VERSION',
    'KSSTREAM_HEADER_OPTIONSF_TIMEDISCONTINUITY',
    'DEFINE_KSPIN_DESCRIPTOR_ITEMEX',
    'DEFINE_KSPROPERTY_ITEM_PIN_PHYSICALCONNECTION',
    'DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_PREROLL', 'KSPROPSETID_MediaSeeking',
    'KSRATE_NOPRESENTATIONDURATION', 'KSDATARANGE_BIT_ATTRIBUTES', 'PKSSTATE',
    'KSALLOCATOR_FLAG_ENABLE_CACHED_MDL',
    'DEFINE_KSPROPERTY_ITEM_STREAM_PIPE_ID',
    'KSALLOCATOR_FLAG_ATTENTION_STEPPING', 'STATIC_KSTIME_FORMAT_MEDIA_TIME',
    'STATIC_KSMFT_CATEGORY_VIDEO_EFFECT', 'KSPROPERTY_TYPE_SERIALIZESET',
    'STATIC_KSMFT_CATEGORY_VIDEO_DECODER', 'KSCREATE_ITEM_SECURITYCHANGED',
    'DEFINE_KSPROPERTY_ITEM_GENERAL_COMPONENTID',
    'DEFINE_KSPROPERTY_ITEM_CLOCK_TIME', 'STATIC_KSDATAFORMAT_TYPE_STREAM',
    'DEFINE_KSPROPERTY_ITEM_TOPOLOGY_NAME', 'STATIC_KSCATEGORY_CLOCK',
    'DEFINE_KSPROPERTY_ITEM_CONNECTION_DATAFORMAT', 'IOCTL_KS_RESET_STATE',
    'KSPIN_FLAG_INITIATE_PROCESSING_ON_EVERY_ARRIVAL', 'IOCTL_KS_PROPERTY',
    'STATIC_KSPROPSETID_General',
    'KSCATEGORY_FILESYSTEM', 'KSCATEGORY_RENDER',
    'DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_CAPABILITIES', 'KSEVENT_TYPE_ENABLE',
    'KSALLOCATOR_FLAG_PARTIAL_READ_SUPPORT', 'KSINTERFACESETID_Standard',
    'DEFINE_KSPROPERTY_ITEM_STREAM_QUALITY', 'STATIC_KSCATEGORY_SENSOR_GROUP',
    'DEFINE_KSPROPERTY_ITEM_PIN_DATARANGES',
    'KSALLOCATOR_FLAG_ALLOCATOR_EXISTS', 'KSTIME_FORMAT_SAMPLE', 'GUID_NULL',
    'KSALLOCATOR_OPTIONF_VALID',
    'STATIC_KSMEMORY_TYPE_DONT_CARE', 'KSPIN_FLAG_GENERATE_EOS_EVENTS',
    'KSMFT_CATEGORY_VIDEO_PROCESSOR', 'KSDATAFORMAT_SPECIFIER_FILEHANDLE',
    'STATIC_KSMFT_CATEGORY_OTHER', 'KSSTREAM_NONPAGED_DATA', 'KSSTRING_Clock',
    'DEFINE_KSPROPERTY_ITEM_PIN_GLOBALCINSTANCES', 'STATIC_KSPROPSETID_Pin',
    'STATIC_KSPROPSETID_MemoryTransport', 'KSDATAFORMAT_SPECIFIER_FILENAME',
    'KSSTREAM_HEADER_OPTIONSF_VRAM_DATA_TRANSFER',
    'KSSTREAM_HEADER_OPTIONSF_SAMPLE_PERSISTED', 'STATIC_KSTIME_FORMAT_FIELD',
    'STATIC_KSCATEGORY_DATADECOMPRESSOR', 'KSCATEGORY_INTERFACETRANSFORM',
    'STATIC_KSCATEGORY_INTERFACETRANSFORM', 'KSPROPERTY_TYPE_SERIALIZESIZE',
    'KSDATARANGE_BIT_REQUIRED_ATTRIBUTES', 'KSPROPERTY_TYPE_GET', 'KSRESET',
    'DEFINE_KSPROPERTY_ITEM_CONNECTION_PRIORITY', 'STATIC_KSTIME_FORMAT_BYTE',
    'KSALLOCATOR_FLAG_CAN_ALLOCATE', 'STATIC_REFERENCE_BUS_INTERFACE',
    'KSDATAFORMAT_TYPE_WILDCARD', 'KSPIN_FLAG_FIXED_FORMAT', 'KSNAME_Filter',
    'KSALLOCATOR_FLAG_INDEPENDENT_RANGES', 'KSMEDIUM_TYPE_ANYINSTANCE',
    'DEFINE_KSPROPERTY_ITEM_PIN_DATAFLOW',
    'KSPIN_FLAG_CRITICAL_PROCESSING', 'KSDATAFORMAT_SUBTYPE_WILDCARD',
    'BUS_INTERFACE_REFERENCE_VERSION', 'KSMETHOD',
    'KSPROPERTY_TYPE_RELATIONS', 'KSALLOCATOR_REQUIREMENTF_SYSTEM_MEMORY',
    'STATIC_KSDATAFORMAT_SPECIFIER_FILENAME', 'KSEVENT_ENTRY_BUFFERED',
    'KSDATAFORMAT_TYPE_STREAM', 'KSMEMORY_TYPE_DONT_CARE', 'KSCATEGORY_CLOCK',
    'DEFINE_KSPROPERTY_ITEM_CONNECTION_ALLOCATORFRAMING', 'STATIC_KSNAME_Pin',
    'KSPROPERTY_TYPE_SERIALIZERAW',
    'DEFINE_KSPROPERTY_ITEM_PIN_CINSTANCES', 'KSMFT_CATEGORY_AUDIO_ENCODER',
    'KSMETHOD_TYPE_SOURCE',  'KSEVENTF_WORKITEM',
    'KSSTREAM_HEADER_TRACK_COMPLETION_NUMBERS',
    'STATIC_KSCATEGORY_DATACOMPRESSOR', 'KSCREATE_ITEM_WILDCARD', 'PKSMETHOD',
    'KSMETHOD_TYPE_NONE', 'STATIC_KSDATAFORMAT_SPECIFIER_NONE', 'KSALL_NODES',
    'KSPROBE_PROBEANDLOCK',  'STATIC_GUID_NULL',
    'STATIC_KSMFT_CATEGORY_AUDIO_EFFECT', 'KSMFT_CATEGORY_OTHER', 'KSDEGRADE',
    'DEFINE_KSPROPERTY_ITEM_STREAM_TIMEFORMAT', 'KSMETHOD_TYPE_READ',
    'KSEVENT_TYPE_TOPOLOGY', 'DEFINE_KSPROPERTY_ITEM_STREAM_MASTERCLOCK',
    'KSSTREAM_HEADER_OPTIONSF_PERSIST_SAMPLE',
    'KSSTREAM_HEADER_OPTIONSF_DATADISCONTINUITY', 'IOCTL_KS_HANDSHAKE',
    'STATIC_KSDATAFORMAT_SPECIFIER_FILEHANDLE', 'KSMEDIUMSETID_Standard',
    'KSPROPERTY_TYPE_GETPAYLOADSIZE', 'STATIC_KSPROPSETID_StreamAllocator',
    'KSFILTER_FLAG_RECEIVE_ZERO_LENGTH_SAMPLES',
    'DEFINE_KSPROPERTY_ITEM_PIN_NECESSARYINSTANCES', 'DEFINE_KSMETHOD_ITEM',
    'DEFINE_KSPROPERTY_ITEM_CONNECTION_STARTAT',
    'STATIC_KSMEMORY_TYPE_DEVICE_UNKNOWN', 'KSEVENTF_EVENT_OBJECT', 'KSEVENT',
    'KSPROBE_STREAMREAD', 'KSSTREAM_HEADER_OPTIONSF_LOOPEDDATA', 'KSPRIORITY',
    'KSALLOCATOR_FLAG_NO_FRAME_INTEGRITY',
    'DEFINE_KSPROPERTY_ITEM_CLOCK_FUNCTIONTABLE', 'IOCTL_KS_READ_STREAM',
    'STATIC_KSDATAFORMAT_TYPE_WILDCARD', 'KSMEMORY_TYPE_DEVICE_UNKNOWN',
    'DEFINE_KSPROPERTY_ITEM_STREAM_ALLOCATOR', 'KSPROPERTY_TYPE_SETSUPPORT',
    'KSMETHODSETID_StreamAllocator', 'KSFILTER_FLAG_HYPERCRITICAL_PROCESSING',
    'DEFINE_KSPROPERTY_ITEM_TOPOLOGY_CATEGORIES', 'KSCATEGORY_SENSOR_GROUP',
    'DEFINE_KSPROPERTY_ITEM_CLOCK_CORRELATEDTIME', 'STATIC_IID_IKsFastClock',
    'DEFINE_KSMETHOD_ITEM_STREAMALLOCATOR_ALLOC', 'KSPIN_FLAG_RENDERER',
    'KSPROPSETID_General', 'KSALLOCATOR_FLAG_CYCLE', 'KSSTRING_Allocator',
    'KSSTREAM_HEADER_OPTIONSF_METADATA', 'STATIC_KSPROPSETID_StreamInterface',
    'KSSTREAM_HEADER_OPTIONSF_TYPECHANGED', 'PKSEVENT',
    'STATIC_KSNAME_Allocator', 'KSALLOCATOR_FLAG_DEVICE_SPECIFIC',
    'KSEVENTF_SEMAPHORE_HANDLE', 'KSDEVICE_DESCRIPTOR_VERSION_2', 'PKSWORKER',
    'MAKEINTRESOURCE', 'DEFINE_KSPROPERTY_ITEM_STREAM_FRAMETIME',
    'IOCTL_KS_DISABLE_EVENT',  'NANOSECONDS',
    'STATIC_KSPROPSETID_Quality', 'DEFINE_KSPIN_DESCRIPTOR_ITEM',
    'KSPROPSETID_Stream', 'KSRELATIVEEVENT_FLAG_HANDLE', 'KSDISPATCH_FASTIO',
    'KSTIME_FORMAT_FRAME', 'KSCATEGORY_COMMUNICATIONSTRANSFORM',
    'STATIC_KSCATEGORY_RENDER', 'KSTIME_FORMAT_NONE',
    'STATIC_KSCATEGORY_VIDEO_CAMERA',
    'DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_POSITION',
    'DEFINE_KSPROPERTY_ITEM_PIN_INTERFACES', 'STATIC_KSEVENTSETID_Device',
    'KSSTRING_Pin', 'STATIC_GUID_BUS_INTERFACE_MEDIUMS', 'DEFINE_GUIDNAMED',
    'KSALLOCATOR_REQUIREMENTF_INPLACE_MODIFIER',
    'KSSTREAM_READ', 'KSATTRIBUTE', 'KSP_NODE',
    'KSPROPTYPESETID_General', 'KSPROPSETID_StreamInterface', 'KSEVENTF_DPC',
    'DEFINE_KSPROPERTY_ITEM_CONNECTION_ACQUIREORDERING',
    'KSALLOCATOR_OPTIONF_COMPATIBLE', 'KSIDENTIFIER',
    'KSSTREAM_HEADER_OPTIONSF_BUFFEREDTRANSFER', 'STATIC_KSPROPSETID_Stream',
    'STATIC_KSEVENTSETID_StreamAllocator', 'KSATTRIBUTE_REQUIRED',
    'KSPROPSETID_Pin', 'KSALLOCATOR_REQUIREMENTF_MUST_ALLOCATE', 'PKSDEGRADE',
    'KSPIN_FLAG_PROCESS_IF_ANY_IN_RUN_STATE', 'KSCATEGORY_SENSOR_CAMERA',
    'KSCATEGORY_DATACOMPRESSOR', 'KSSTACK_USE',
    'KSDEVICE_FLAG_LOWPOWER_PASSTHROUGH', 'KSPROPERTY_MEMBER_FLAG_DEFAULT',
    'KSDEVICE_FLAG_ENABLE_REMOTE_WAKEUP', 'KSALLOCATOR_FLAG_MULTIPLE_OUTPUT',
    'KSMFT_CATEGORY_VIDEO_ENCODER', 'STATIC_KSMFT_CATEGORY_VIDEO_PROCESSOR',
    'KSMEMORY_TYPE_WILDCARD', 'KSPROPERTY',
    'KSCATEGORY_DATADECOMPRESSOR',
    'KSCATEGORY_PROXY', 'STATIC_KSCATEGORY_DATATRANSFORM', 'KSNAME_Allocator',
    'STATIC_KSPROPTYPESETID_General', 'STATIC_KSCATEGORY_SPLITTER',
    'STATIC_KSMEMORY_TYPE_WILDCARD',
    'DEFINE_KSPROPERTY_ITEM_TOPOLOGY_CONNECTIONS', 'KSFRAMETIME_VARIABLESIZE',
    'KSEVENT_TYPE_SETSUPPORT', 'REFERENCE_BUS_INTERFACE', 'IOCTL_KS_METHOD',
    'STATIC_KSCATEGORY_COMMUNICATIONSTRANSFORM', 'KSSTRING_AllocatorEx',
    'KSEVENT_TYPE_ENABLEBUFFERED', 'DEFINE_KSPROPERTY_ITEM_PIN_NAME',
    'STATIC_KSMFT_CATEGORY_VIDEO_ENCODER',
    'STATIC_KSMETHODSETID_StreamAllocator', 'DEFINE_KSPROPERTY_ITEM',
    'STATIC_IID_IKsDeviceFunctions', 'KSPROPERTY_MEMBER_RANGES',
    'KSMETHODSETID_StreamIo', 'KSPIN_FLAG_ASYNCHRONOUS_PROCESSING',
    'STATIC_KSMFT_CATEGORY_MULTIPLEXER', 'KSFILTER_DESCRIPTOR_VERSION',
    'KSSTREAM_HEADER_OPTIONSF_FLUSHONPAUSE', 'KSPIN_FLAG_ENFORCE_FIFO',
    'KSDATARANGE_REQUIRED_ATTRIBUTES', 'KSRATE_NOPRESENTATIONSTART',
    'DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_DURATION', 'KSMEDIUM_STANDARD_DEVIO',
    'KSPROBE_STREAMWRITEMODIFY', 'KSPIN_FLAG_DISPATCH_LEVEL_PROCESSING',
    'KSCATEGORY_MEDIUMTRANSFORM', 'KSPIN_DATAFLOW',
    'KSDATAFORMAT_BIT_ATTRIBUTES', 'PKSPRIORITY',
    'KSMFT_CATEGORY_AUDIO_DECODER', 'KSEVENT_ENTRY_DELETED', 'KSEVENT_DEVICE',
    'KSTIME_FORMAT_FIELD', 'KSEVENTSETID_VolumeLimit',
    'DEFINE_KSPROPERTY_ITEM_STREAMALLOCATOR_FUNCTIONTABLE', 'PKSPIN_DATAFLOW',
    'KSEVENTSETID_StreamAllocator', 'DEFINE_KSPROPERTY_ITEM_MEMORY_TRANSPORT',
    'KSSTREAM_HEADER_OPTIONSF_PREROLL',
    'KSPROPSETID_Topology', 'STATIC_KSINTERFACESETID_Standard', 'PKSPROPERTY',
    'KSSTREAM_HEADER_OPTIONSF_SPLICEPOINT', 'KSNAME_TopologyNode',
    'KSPROPERTY_PIN_FLAGS_ATTRIBUTE_RANGE_AWARE', 'KSCATEGORY_QUALITY',
    '_KS_NO_ANONYMOUS_STRUCTURES_', 'IOCTL_KS_WRITE_STREAM', 'KSPROPERTY_PIN',
    'STATIC_KSDATAFORMAT_SUBTYPE_NONE', 'STATIC_KSPROPSETID_Connection',
    'KSMEMORY_TYPE_KERNEL_PAGED', 'KSCREATE_ITEM_FREEONSTOP', 'KSPROPERTY_GM',
    'DEFINE_KSMETHOD_ITEM_STREAMALLOCATOR_FREE', 'KSEVENT_TYPE_ONESHOT',
    'STATIC_KSINTERFACESETID_FileIo',
    'KSALLOCATOR_REQUIREMENTF_SYSTEM_MEMORY_CUSTOM_ALLOCATION',
    'STATIC_KSPROPSETID_PinMDLCacheClearProp', 'KSSTREAM_SYNCHRONOUS',
    'DEFINE_KSPROPERTY_ITEM_PIN_MEDIUMS', 'KSPIN_FLAG_DISTINCT_TRAILING_EDGE',
    'DEFINE_KSPROPERTY_ITEM_PIN_CONSTRAINEDDATARANGES', 'KSCATEGORY_SPLITTER',
    'STATIC_KSMEMORY_TYPE_KERNEL_NONPAGED', 'STATIC_KSCATEGORY_BRIDGE',
    'KSSTREAM_UVC_SECURE_ATTRIBUTE_SIZE', 'STATIC_IID_IKsControl',
    'KSSTREAM_HEADER_OPTIONSF_FRAMEINFO',
    'STATIC_KSCATEGORY_SENSOR_CAMERA', 'KSDATARANGE',
    'STATIC_KS_TYPE_DONT_CARE', 'KSOBJECTTYPE',
    'KSEVENT_ENTRY_ONESHOT', 'KSMEMORY_TYPE_KERNEL_NONPAGED',
    'STATIC_KSTIME_FORMAT_NONE', 'KSDATARANGE_ATTRIBUTES', 'KSTARGET_STATE',
    'DEFINE_KSPROPERTY_ITEM_QUALITY_ERROR',
    'KSPROPSETID_MemoryTransport', 'STATIC_KSEVENTSETID_Clock',
    'KSCREATE_ITEM_NOPARAMETERS', 'KSMFT_CATEGORY_MULTIPLEXER',
    'KSPROBE_ALLOCATEMDL', 'KSPROPERTY_TYPE_UNSERIALIZERAW', 'IID_IKsControl',
    'STATIC_KSEVENTSETID_PinCapsChange', 'STATIC_KSPROPSETID_Topology',
    'KSPROPERTY_TYPE_TOPOLOGY', 'MIN_DEV_VER_FOR_QI', 'KSEVENTF_EVENT_HANDLE',
    'STATIC_KSCATEGORY_FILESYSTEM',
    'STATIC_KSTIME_FORMAT_FRAME', 'STATIC_KSMEMORY_TYPE_USER', 'KSOBJECT_BAG',
    'STATIC_KSDATAFORMAT_SUBTYPE_WILDCARD', 'KSMFT_CATEGORY_DEMULTIPLEXER',
    'KSDEVICE_FLAG_ENABLE_QUERYINTERFACE', 'KSCATEGORY_DATATRANSFORM',
    'KSPIN_FLAG_SOME_FRAMES_REQUIRED_FOR_PROCESSING', 'KSPRIORITY_NORMAL',
    'KSEVENT_TYPE_BASICSUPPORT', 'KSPROPERTY_MEMBER_VALUES', 'PKSPIN_MEDIUM',
    'KSRELATIVEEVENT_FLAG_POINTER', 'STATIC_KSDATAFORMAT_SPECIFIER_WILDCARD',
    'KSALLOCATOR_FLAG_2D_BUFFER_REQUIRED', 'STATIC_KSCATEGORY_PROXY',
    'STATIC_KSCATEGORY_MIXER', 'KSMETHOD_TYPE_BASICSUPPORT', 'KSPIN_MEDIUM',
    'STATIC_KSMEMORY_TYPE_SYSTEM', 'KSCATEGORY_VIDEO_CAMERA',
    'STATIC_KSCATEGORY_MEDIUMTRANSFORM', 'STATIC_KSEVENTSETID_VolumeLimit',
    'STATIC_KSPROPSETID_GM', 'KSMULTIPLE_ITEM',
    'STATIC_KSMEMORY_TYPE_KERNEL_PAGED', 'KSDEGRADESETID_Standard',
    'DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_FORMATS', 'KSMETHOD_TYPE_SETSUPPORT',
    'KSPROPERTY_TYPE_HIGHPRIORITY', 'KSEVENTS_LOCKTYPE', 'KSEVENT_CONNECTION',
    'KSPIN_FLAG_FRAMES_NOT_REQUIRED_FOR_PROCESSING', 'PKSPIN_COMMUNICATION',
    'KSPPROPERTY_ALLOCATOR_MDLCACHING', 'KSPROPERTY_TOPOLOGY',
    'KSEVENT_PINCAPS_CHANGENOTIFICATIONS', 'KSMETHOD_STREAMIO',
    'KSPIN_COMMUNICATION', 'KSPIN_MDL_CACHING_EVENT', 'KSPROPERTY_STREAM',
    'KSEVENT_VOLUMELIMIT', 'KS_SEEKING_CAPABILITIES', 'KSLIST_ENTRY_LOCATION',
    'KSPROPERTY_STREAMALLOCATOR', 'KSPROPERTY_QUALITY', 'KSPROPERTY_GENERAL',
    'KSSTREAM_POINTER_STATE', 'KSIRP_REMOVAL_OPERATION', 'KS_SEEKING_FLAGS',
    'KSEVENT_STREAMALLOCATOR', 'KSCOMPLETION_INVOCATION', 'KSPROPERTY_CLOCK',
    'KSPROPERTY_CONNECTION', 'KSINTERFACE_STANDARD', 'KSDEVICE_THERMAL_STATE',
    'KSPROPERTY_STREAMINTERFACE', 'KSDEGRADE_STANDARD', 'KSINTERFACE_FILEIO',
    'KSMETHOD_STREAMALLOCATOR', 'KSPROPERTY_MEDIASEEKING', 'IID_IKsFastClock',
    'KSEVENT_CLOCK_POSITION', 'IID_IKsDeviceFunctions', 'KSDATAFORMAT',
    'KSOBJECT_HEADER', 'KSDEVICE_HEADER', 'KSPIN_INTERFACE',
    'PKSDEFAULTCLOCK', 'PCKSPIN_DESCRIPTOR', 'PKSPIN_INTERFACE',
)

NOT_USED = (
    'DEFINE_KSAUTOMATION_EVENTS_NULL', 'KSEVENT_ITEM_IRP_STORAGE',
    'DEFINE_KSMETHOD_SET_TABLE', 'DEFINE_KSAUTOMATION_METHODS_NULL',
    'DEFINE_KSAUTOMATION_METHODS', 'DEFINE_KSDISPATCH_TABLE',
    'KSMETHOD_TYPE_IRP_STORAGE', 'KSMETHOD_SET_IRP_STORAGE',
    'DEFINE_KSCREATE_DISPATCH_TABLE', 'SetKsFramingRangeWeighted',
    'DEFINE_KSFILTER_DESCRIPTOR_TABLE', 'DEFINE_KSEVENT_SET',
    'DEFINE_KSFILTER_CATEGORIES', 'DEFINE_KSAUTOMATION_PROPERTIES',
    'DEFINE_KSPIN_INTERFACE_ITEM', 'DEFINE_KSFILTER_CONNECTIONS',
    'DEFINE_KSCREATE_ITEMEX', 'DEFINE_KSFASTPROPERTY_ITEM',
    'DENY_USERMODE_ACCESS', 'DEFINE_KSPROPERTY_CLOCKSET',
    'IKsControl', 'DEFINE_KSPROPERTY_SET', 'DEFINE_KSPROPERTY_PINSET',
    'KSEVENT_ENTRY_IRP_STORAGE', 'KsDeleteFilterFactory',
    'DEFINE_KSEVENT_SET_TABLE', 'DEFINE_KSAUTOMATION_TABLE',
    'DEFINE_KSPROPERTY_TABLE', 'DEFINE_KSMETHOD_ALLOCATORSET',
    'DEFINE_KSCREATE_ITEM', 'KSCREATE_ITEM_IRP_STORAGE',
    'SetKsFramingRange', 'DEFINE_KSPROPERTY_ALLOCATORSET',
    'SetDontCareKsFramingRange', 'DEFINE_KSFILTER_CATEGORIES_NULL',
    'DEFINE_KSPIN_DEFAULT_INTERFACES', 'DEFINE_KSFILTER_DEFAULT_CONNECTIONS',
    'DEFINE_KSEVENT_ITEM', 'DEFINE_KSAUTOMATION_PROPERTIES_NULL',
    'IKsFastClock', 'DEFINE_NODE_DESCRIPTOR', 'DEFINE_KSPIN_MEDIUM_ITEM',
    'KSPROPERTY_ITEM_IRP_STORAGE', 'DEFINE_KSMETHOD_TABLE',
    'DEFINE_KSPROPERTY_PINSETCONSTRAINED', 'KSPROPERTY_ATTRIBUTES_IRP_STORAGE',
    'DECLARE_SIMPLE_FRAMING_EX', 'INITIALIZE_SIMPLE_FRAMING_EX',
    'INTERFACE', 'KSEVENT_SET_IRP_STORAGE', 'DEFINE_KSEVENT_TABLE',
    'DEFINE_KSPIN_MEDIUM_TABLE', 'DEFINE_KSFILTER_DESCRIPTOR',
    'DEFINE_KSFILTER_NODE_DESCRIPTORS_NULL', 'DEFINE_KSFILTER_PIN_DESCRIPTORS',
    'KsEditSized', 'DEFINE_KSPROPERTY_STREAMINTERFACESET',
    'DEFINE_KSPROPERTY_TOPOLOGYSET', 'KSMETHOD_ITEM_IRP_STORAGE',
    'KSPROPERTY_SET_IRP_STORAGE', 'KSCONVERT_PERFORMANCE_TIME',
    'KsEdit', 'DEFINE_KSFILTER_NODE_DESCRIPTORS',
    'DEFINE_KSPIN_DEFAULT_MEDIUMS', 'KSDDKAPI', 'KsDiscard',
    'DEFINE_KSPIN_DESCRIPTOR_TABLE', 'DEFINE_KSMETHOD_SET',
    'SetDefaultKsCompression', 'DEFINE_KSFILTER_CATEGORY',
    'DEFINE_KSAUTOMATION_EVENTS','KSQUEUE_SPINLOCK_IRP_STORAGE',
    'DEFINE_KSPROPERTY_SET_TABLE', 'DEFINE_ABSTRACT_UNKNOWN',
    'MF_SET_SHARED_MDLHANDLE', 'DEFINE_KSCREATE_ITEMNULL',
    'IKsDeviceFunctions', 'DEFINE_KSPIN_INTERFACE_TABLE',
    'DEFINE_KSFASTMETHOD_ITEM', 'KsDispatchFastWriteFailure',

)
