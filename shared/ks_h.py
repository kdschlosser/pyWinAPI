import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

COMMETHOD = comtypes.COMMETHOD

_KS_ = None
__TCS__ = None
_NTRTL_ = None
DEFINE_GUIDEX = None
STATICGUIDOF = None
SIZEOF_ARRAY = None
__wtypes_h__ = None
PACK_PRAGMAS_NOT_SUPPORTED = None
_NTOS_ = None
_UNKNOWN_H_ = None
__IUnknown_INTERFACE_DEFINED__ = None
_IKsControl_ = None
DEFINE_ABSTRACT_UNKNOWN = None
MAKEINTRESOURCE = None
RT_STRING = None

class KSPRIORITY(ctypes.Structure):
    pass


PKSPRIORITY = POINTER(KSPRIORITY)


class KSIDENTIFIER(ctypes.Structure):
    pass


PKSIDENTIFIER = POINTER(KSIDENTIFIER)


class KSP_NODE(ctypes.Structure):
    pass


PKSP_NODE = POINTER(KSP_NODE)


class KSM_NODE(ctypes.Structure):
    pass


PKSM_NODE = POINTER(KSM_NODE)


class KSE_NODE(ctypes.Structure):
    pass


PKSE_NODE = POINTER(KSE_NODE)


class KSMULTIPLE_ITEM(ctypes.Structure):
    pass


PKSMULTIPLE_ITEM = POINTER(KSMULTIPLE_ITEM)


class KSPROPERTY_DESCRIPTION(ctypes.Structure):
    pass


PKSPROPERTY_DESCRIPTION = POINTER(KSPROPERTY_DESCRIPTION)


class KSPROPERTY_MEMBERSHEADER(ctypes.Structure):
    pass


PKSPROPERTY_MEMBERSHEADER = POINTER(KSPROPERTY_MEMBERSHEADER)


class KSPROPERTY_BOUNDS_LONG(ctypes.Union):
    pass


PKSPROPERTY_BOUNDS_LONG = POINTER(KSPROPERTY_BOUNDS_LONG)


class KSPROPERTY_BOUNDS_LONGLONG(ctypes.Union):
    pass


PKSPROPERTY_BOUNDS_LONGLONG = POINTER(KSPROPERTY_BOUNDS_LONGLONG)


class KSPROPERTY_STEPPING_LONG(ctypes.Structure):
    pass


PKSPROPERTY_STEPPING_LONG = POINTER(KSPROPERTY_STEPPING_LONG)


class KSPROPERTY_STEPPING_LONGLONG(ctypes.Structure):
    pass


PKSPROPERTY_STEPPING_LONGLONG = POINTER(KSPROPERTY_STEPPING_LONGLONG)


class KSEVENTDATA(ctypes.Structure):
    pass


PKSEVENTDATA = POINTER(KSEVENTDATA)


class KSQUERYBUFFER(ctypes.Structure):
    pass


PKSQUERYBUFFER = POINTER(KSQUERYBUFFER)


class KSRELATIVEEVENT(ctypes.Structure):
    pass





class KSEVENT_TIME_MARK(ctypes.Structure):
    pass


PKSEVENT_TIME_MARK = POINTER(KSEVENT_TIME_MARK)


class KSEVENT_TIME_INTERVAL(ctypes.Structure):
    pass


PKSEVENT_TIME_INTERVAL = POINTER(KSEVENT_TIME_INTERVAL)


class KSINTERVAL(ctypes.Structure):
    pass


PKSINTERVAL = POINTER(KSINTERVAL)


class KSCOMPONENTID(ctypes.Structure):
    pass


PKSCOMPONENTID = POINTER(KSCOMPONENTID)


class KSPROPERTY_POSITIONS(ctypes.Structure):
    pass


PKSPROPERTY_POSITIONS = POINTER(KSPROPERTY_POSITIONS)


class KSPROPERTY_MEDIAAVAILABLE(ctypes.Structure):
    pass


PKSPROPERTY_MEDIAAVAILABLE = POINTER(KSPROPERTY_MEDIAAVAILABLE)


class KSP_TIMEFORMAT(ctypes.Structure):
    pass


PKSP_TIMEFORMAT = POINTER(KSP_TIMEFORMAT)


class KSGRAPHMANAGER_FUNCTIONTABLE(ctypes.Structure):
    pass


PKSGRAPHMANAGER_FUNCTIONTABLE = KSGRAPHMANAGER_FUNCTIONTABLE


class _KSPROPERTY_GRAPHMANAGER_INTERFACE(ctypes.Structure):
    pass


KSPROPERTY_GRAPHMANAGER_INTERFACE = _KSPROPERTY_GRAPHMANAGER_INTERFACE
PKSPROPERTY_GRAPHMANAGER_INTERFACE = POINTER(_KSPROPERTY_GRAPHMANAGER_INTERFACE)


class KSTOPOLOGY_CONNECTION(ctypes.Structure):
    pass


PKSTOPOLOGY_CONNECTION = POINTER(KSTOPOLOGY_CONNECTION)


class KSTOPOLOGY(ctypes.Structure):
    pass


PKSTOPOLOGY = POINTER(KSTOPOLOGY)


class KSNODE_CREATE(ctypes.Structure):
    pass


PKSNODE_CREATE = POINTER(KSNODE_CREATE)


class KSP_PIN(ctypes.Structure):
    pass


PKSP_PIN = POINTER(KSP_PIN)


class KSE_PIN(ctypes.Structure):
    pass


PKSE_PIN = POINTER(KSE_PIN)


class KSPIN_CINSTANCES(ctypes.Structure):
    pass


PKSPIN_CINSTANCES = POINTER(KSPIN_CINSTANCES)


class KSDATAFORMAT(ctypes.Structure):
    pass


PKSDATAFORMAT = POINTER(KSDATAFORMAT)
KSDATARANGE = KSDATAFORMAT
PKSDATARANGE = POINTER(KSDATAFORMAT)


PKSDATAFORMAT = POINTER(KSDATAFORMAT)
KSDATARANGE = KSDATAFORMAT
PKSDATARANGE = POINTER(KSDATAFORMAT)


class KSATTRIBUTE(ctypes.Structure):
    pass


PKSATTRIBUTE = POINTER(KSATTRIBUTE)


class KSATTRIBUTE_LIST(ctypes.Structure):
    pass


PKSATTRIBUTE_LIST = POINTER(KSATTRIBUTE_LIST)


class KSPIN_CONNECT(ctypes.Structure):
    pass


PKSPIN_CONNECT = POINTER(KSPIN_CONNECT)


class KSPIN_PHYSICALCONNECTION(ctypes.Structure):
    pass


PKSPIN_PHYSICALCONNECTION = POINTER(KSPIN_PHYSICALCONNECTION)


class KSPIN_DESCRIPTOR(ctypes.Structure):
    pass


PKSPIN_DESCRIPTOR = POINTER(KSPIN_DESCRIPTOR)


class KSALLOCATOR_FRAMING(ctypes.Structure):
    pass


PKSALLOCATOR_FRAMING = POINTER(KSALLOCATOR_FRAMING)


class KS_FRAMING_RANGE(ctypes.Structure):
    pass


PKS_FRAMING_RANGE = POINTER(KS_FRAMING_RANGE)


class KS_FRAMING_RANGE_WEIGHTED(ctypes.Structure):
    pass


PKS_FRAMING_RANGE_WEIGHTED = POINTER(KS_FRAMING_RANGE_WEIGHTED)


class KS_COMPRESSION(ctypes.Structure):
    pass


PKS_COMPRESSION = POINTER(KS_COMPRESSION)


class KS_FRAMING_ITEM(ctypes.Structure):
    pass


PKS_FRAMING_ITEM = POINTER(KS_FRAMING_ITEM)


class KSALLOCATOR_FRAMING_EX(ctypes.Structure):
    pass


PKSALLOCATOR_FRAMING_EX = POINTER(KSALLOCATOR_FRAMING_EX)


class KSSTREAMALLOCATOR_FUNCTIONTABLE(ctypes.Structure):
    pass


PKSSTREAMALLOCATOR_FUNCTIONTABLE = POINTER(KSSTREAMALLOCATOR_FUNCTIONTABLE)


class KSSTREAMALLOCATOR_STATUS(ctypes.Structure):
    pass


PKSSTREAMALLOCATOR_STATUS = POINTER(KSSTREAMALLOCATOR_STATUS)


class KSSTREAMALLOCATOR_STATUS_EX(ctypes.Structure):
    pass


PKSSTREAMALLOCATOR_STATUS_EX = POINTER(KSSTREAMALLOCATOR_STATUS_EX)


class KSTIME(ctypes.Structure):
    pass


PKSTIME = POINTER(KSTIME)


class KSSTREAM_HEADER(ctypes.Structure):
    pass


PKSSTREAM_HEADER = POINTER(KSSTREAM_HEADER)


class KSSTREAM_METADATA_INFO(ctypes.Structure):
    pass


PKSSTREAM_METADATA_INFO = POINTER(KSSTREAM_METADATA_INFO)


class KSSTREAM_UVC_METADATATYPE_TIMESTAMP(ctypes.Structure):
    pass


PKSSTREAM_UVC_METADATATYPE_TIMESTAMP = POINTER(KSSTREAM_UVC_METADATATYPE_TIMESTAMP)


class KSSTREAM_UVC_METADATA(ctypes.Structure):
    pass


PKSSTREAM_UVC_METADATA = POINTER(KSSTREAM_UVC_METADATA)


class KSPIN_MDL_CACHING_NOTIFICATION(ctypes.Structure):
    pass


PKSPIN_MDL_CACHING_NOTIFICATION = POINTER(KSPIN_MDL_CACHING_NOTIFICATION)


class KSPIN_MDL_CACHING_NOTIFICATION32(ctypes.Structure):
    pass


PKSPIN_MDL_CACHING_NOTIFICATION32 = POINTER(KSPIN_MDL_CACHING_NOTIFICATION32)


class KSQUALITY_MANAGER(ctypes.Structure):
    pass


PKSQUALITY_MANAGER = POINTER(KSQUALITY_MANAGER)


class KSFRAMETIME(ctypes.Structure):
    pass


PKSFRAMETIME = POINTER(KSFRAMETIME)


class KSRATE(ctypes.Structure):
    pass


PKSRATE = POINTER(KSRATE)


class KSRATE_CAPABILITY(ctypes.Structure):
    pass


PKSRATE_CAPABILITY = POINTER(KSRATE_CAPABILITY)


class KSCLOCK_CREATE(ctypes.Structure):
    pass


PKSCLOCK_CREATE = POINTER(KSCLOCK_CREATE)


class KSCORRELATED_TIME(ctypes.Structure):
    pass


PKSCORRELATED_TIME = POINTER(KSCORRELATED_TIME)


class KSRESOLUTION(ctypes.Structure):
    pass


PKSRESOLUTION = POINTER(KSRESOLUTION)


class KSCLOCK_FUNCTIONTABLE(ctypes.Structure):
    pass


PKSCLOCK_FUNCTIONTABLE = POINTER(KSCLOCK_FUNCTIONTABLE)


class KSQUALITY(ctypes.Structure):
    pass


PKSQUALITY = POINTER(KSQUALITY)


class KSERROR(ctypes.Structure):
    pass


PKSERROR = POINTER(KSERROR)


class KSPROPERTY_MEMBERSLIST(ctypes.Structure):
    pass


PKSPROPERTY_MEMBERSLIST = POINTER(KSPROPERTY_MEMBERSLIST)


class KSPROPERTY_VALUES(ctypes.Structure):
    pass


PKSPROPERTY_VALUES = POINTER(KSPROPERTY_VALUES)


class KSPROPERTY_ITEM(ctypes.Structure):
    pass


PKSPROPERTY_ITEM = POINTER(KSPROPERTY_ITEM)


class KSFASTPROPERTY_ITEM(ctypes.Structure):
    pass


PKSFASTPROPERTY_ITEM = POINTER(KSFASTPROPERTY_ITEM)


class KSPROPERTY_SET(ctypes.Structure):
    pass


PKSPROPERTY_SET = POINTER(KSPROPERTY_SET)


class KSMETHOD_ITEM(ctypes.Structure):
    pass


PKSMETHOD_ITEM = POINTER(KSMETHOD_ITEM)


class KSFASTMETHOD_ITEM(ctypes.Structure):
    pass


PKSFASTMETHOD_ITEM = POINTER(KSFASTMETHOD_ITEM)


class KSMETHOD_SET(ctypes.Structure):
    pass


PKSMETHOD_SET = POINTER(KSMETHOD_SET)


class KSEVENT_ITEM(ctypes.Structure):
    pass


PKSEVENT_ITEM = POINTER(KSEVENT_ITEM)


class KSEVENT_SET(ctypes.Structure):
    pass


PKSEVENT_SET = POINTER(KSEVENT_SET)


class KSDPC_ITEM(ctypes.Structure):
    pass


PKSDPC_ITEM = POINTER(KSDPC_ITEM)


class KSBUFFER_ITEM(ctypes.Structure):
    pass


PKSBUFFER_ITEM = POINTER(KSBUFFER_ITEM)


class _KSEVENT_ENTRY(ctypes.Structure):
    pass


KSEVENT_ENTRY = _KSEVENT_ENTRY
PKSEVENT_ENTRY = POINTER(_KSEVENT_ENTRY)


class KSOBJECT_CREATE_ITEM(ctypes.Structure):
    pass


PKSOBJECT_CREATE_ITEM = POINTER(KSOBJECT_CREATE_ITEM)


class KSOBJECT_CREATE(ctypes.Structure):
    pass


PKSOBJECT_CREATE = POINTER(KSOBJECT_CREATE)


class KSDISPATCH_TABLE(ctypes.Structure):
    pass


PKSDISPATCH_TABLE = POINTER(KSDISPATCH_TABLE)


class BUS_INTERFACE_REFERENCE(ctypes.Structure):
    pass


PBUS_INTERFACE_REFERENCE = POINTER(BUS_INTERFACE_REFERENCE)


class BUS_INTERFACE_MEDIUMS(ctypes.Structure):
    pass


PBUS_INTERFACE_MEDIUMS = POINTER(BUS_INTERFACE_MEDIUMS)


class KSPROPERTY_SERIALHDR(ctypes.Structure):
    pass


PKSPROPERTY_SERIALHDR = POINTER(KSPROPERTY_SERIALHDR)


class KSPROPERTY_SERIAL(ctypes.Structure):
    pass


PKSPROPERTY_SERIAL = POINTER(KSPROPERTY_SERIAL)


class KSHANDSHAKE(ctypes.Structure):
    pass


PKSHANDSHAKE = POINTER(KSHANDSHAKE)


class _KSGATE(ctypes.Structure):
    pass


KSGATE = _KSGATE
PKSGATE = POINTER(_KSGATE)

class KSAUTOMATION_TABLE_(ctypes.Structure):
    pass


KSAUTOMATION_TABLE = KSAUTOMATION_TABLE_
PKSAUTOMATION_TABLE = POINTER(KSAUTOMATION_TABLE_)


class _KSDEVICE_DISPATCH(ctypes.Structure):
    pass


KSDEVICE_DISPATCH = _KSDEVICE_DISPATCH
PKSDEVICE_DISPATCH = POINTER(_KSDEVICE_DISPATCH)


class _KSFILTER_DISPATCH(ctypes.Structure):
    pass


KSFILTER_DISPATCH = _KSFILTER_DISPATCH
PKSFILTER_DISPATCH = POINTER(_KSFILTER_DISPATCH)


class _KSPIN_DISPATCH(ctypes.Structure):
    pass


KSPIN_DISPATCH = _KSPIN_DISPATCH
PKSPIN_DISPATCH = POINTER(_KSPIN_DISPATCH)



class _KSCLOCK_DISPATCH(ctypes.Structure):
    pass


KSCLOCK_DISPATCH = _KSCLOCK_DISPATCH
PKSCLOCK_DISPATCH = POINTER(_KSCLOCK_DISPATCH)


class _KSALLOCATOR_DISPATCH(ctypes.Structure):
    pass


KSALLOCATOR_DISPATCH = _KSALLOCATOR_DISPATCH
PKSALLOCATOR_DISPATCH = POINTER(_KSALLOCATOR_DISPATCH)


class _KSDEVICE_DESCRIPTOR(ctypes.Structure):
    pass



KSDEVICE_DESCRIPTOR = _KSDEVICE_DESCRIPTOR
PKSDEVICE_DESCRIPTOR = POINTER(_KSDEVICE_DESCRIPTOR)


class _KSFILTER_DESCRIPTOR(ctypes.Structure):
    pass


KSFILTER_DESCRIPTOR = _KSFILTER_DESCRIPTOR
PKSFILTER_DESCRIPTOR = POINTER(_KSFILTER_DESCRIPTOR)


class _KSPIN_DESCRIPTOR_EX(ctypes.Structure):
    pass


KSPIN_DESCRIPTOR_EX = _KSPIN_DESCRIPTOR_EX
PKSPIN_DESCRIPTOR_EX = POINTER(_KSPIN_DESCRIPTOR_EX)


class _KSNODE_DESCRIPTOR(ctypes.Structure):
    pass


KSNODE_DESCRIPTOR = _KSNODE_DESCRIPTOR
PKSNODE_DESCRIPTOR = POINTER(_KSNODE_DESCRIPTOR)


class _KSDEVICE(ctypes.Structure):
    pass


KSDEVICE = _KSDEVICE
PKSDEVICE = POINTER(_KSDEVICE)


class _KSFILTERFACTORY(ctypes.Structure):
    pass


KSFILTERFACTORY = _KSFILTERFACTORY
PKSFILTERFACTORY = POINTER(_KSFILTERFACTORY)


class _KSFILTER(ctypes.Structure):
    pass


KSFILTER = _KSFILTER
PKSFILTER = POINTER(_KSFILTER)


class _KSPIN(ctypes.Structure):
    pass


KSPIN = _KSPIN
PKSPIN = POINTER(_KSPIN)


class _KSMAPPING(ctypes.Structure):
    pass


KSMAPPING = _KSMAPPING
PKSMAPPING = POINTER(_KSMAPPING)


class _KSSTREAM_POINTER_OFFSET(ctypes.Structure):
    pass


KSSTREAM_POINTER_OFFSET = _KSSTREAM_POINTER_OFFSET
PKSSTREAM_POINTER_OFFSET = POINTER(_KSSTREAM_POINTER_OFFSET)


class _KSSTREAM_POINTER(ctypes.Structure):
    pass


KSSTREAM_POINTER = _KSSTREAM_POINTER
PKSSTREAM_POINTER = POINTER(_KSSTREAM_POINTER)


class _KSPROCESSPIN(ctypes.Structure):
    pass


KSPROCESSPIN = _KSPROCESSPIN
PKSPROCESSPIN = POINTER(_KSPROCESSPIN)


class _KSPROCESSPIN_INDEXENTRY(ctypes.Structure):
    pass


KSPROCESSPIN_INDEXENTRY = _KSPROCESSPIN_INDEXENTRY
PKSPROCESSPIN_INDEXENTRY = POINTER(_KSPROCESSPIN_INDEXENTRY)


class _KSDEVICE_THERMAL_DISPATCH(ctypes.Structure):
    pass


KSDEVICE_THERMAL_DISPATCH = _KSDEVICE_THERMAL_DISPATCH
PKSDEVICE_THERMAL_DISPATCH = POINTER(_KSDEVICE_THERMAL_DISPATCH)


class _MF_MDL_SHARED_PAYLOAD_KEY(ctypes.Union):
    pass


MF_MDL_SHARED_PAYLOAD_KEY = _MF_MDL_SHARED_PAYLOAD_KEY
PMF_MDL_SHARED_PAYLOAD_KEY = POINTER(_MF_MDL_SHARED_PAYLOAD_KEY)




# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: ks.h Abstract: Windows Driver Model/Connection and Streaming
# Architecture (WDM-CSA) core definitions. --
if not defined(_KS_):
    # DEFINE ERROR:    #define _KS_
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.missing_structures_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if defined(__TCS__):
            _KS_NO_ANONYMOUS_STRUCTURES_ = 1
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(_NTRTL_):
            if not defined(DEFINE_GUIDEX):
                def DEFINE_GUIDEX(name):
                    return GUID
            # END IF   not defined(DEFINE_GUIDEX)

            if not defined(STATICGUIDOF):
                def STATICGUIDOF(guid):
                    return guid
            # END IF   not defined(STATICGUIDOF)

        # END IF   not defined(_NTRTL_)

        if not defined(SIZEOF_ARRAY):
            def SIZEOF_ARRAY(ar):
                return ctypes.sizeof(ar) / ctypes.sizeof(ar[0])
        # END IF   not defined(SIZEOF_ARRAY)

        if defined(__cplusplus) and _MSC_VER >= 1100:
            def DEFINE_GUIDSTRUCT(g):
                return GUID(g)


            def DEFINE_GUIDNAMED(n):
                return GUID(n)
        else:
            def DEFINE_GUIDSTRUCT(n):
                return DEFINE_GUIDEX(n)


            def DEFINE_GUIDNAMED(n):
                return n
        # END IF   not defined(__cplusplus)

        # == == == == == == == == == == == == == == == == == == == == == == ==
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
            0x00
        )
        GUID_NULL = DEFINE_GUIDSTRUCT(
            "00000000-0000-0000-0000-000000000000"
        )
        GUID_NULL = DEFINE_GUIDNAMED(GUID_NULL)

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

        from pyWinAPI.shared.devioctl_h import *
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        IOCTL_KS_PROPERTY = CTL_CODE(
            FILE_DEVICE_KS,
            0x000,
            METHOD_NEITHER,
            FILE_ANY_ACCESS
        )
        IOCTL_KS_ENABLE_EVENT = CTL_CODE(
            FILE_DEVICE_KS,
            0x001,
            METHOD_NEITHER,
            FILE_ANY_ACCESS,
        )
        IOCTL_KS_DISABLE_EVENT = CTL_CODE(
            FILE_DEVICE_KS,
            0x002,
            METHOD_NEITHER,
            FILE_ANY_ACCESS,
        )
        IOCTL_KS_METHOD = CTL_CODE(
            FILE_DEVICE_KS,
            0x003,
            METHOD_NEITHER,
            FILE_ANY_ACCESS,
        )
        IOCTL_KS_WRITE_STREAM = CTL_CODE(
            FILE_DEVICE_KS,
            0x004,
            METHOD_NEITHER,
            FILE_WRITE_ACCESS,
        )
        IOCTL_KS_READ_STREAM = CTL_CODE(
            FILE_DEVICE_KS,
            0x005,
            METHOD_NEITHER,
            FILE_READ_ACCESS,
        )
        IOCTL_KS_RESET_STATE = CTL_CODE(
            FILE_DEVICE_KS,
            0x006,
            METHOD_NEITHER,
            FILE_ANY_ACCESS,
        )

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        class KSRESET(ENUM):
            KSRESET_BEGIN = 1
            KSRESET_END = 2

        KSRESET_BEGIN = KSRESET.KSRESET_BEGIN
        KSRESET_END = KSRESET.KSRESET_END


        class KSSTATE(ENUM):
            KSSTATE_STOP = 1
            KSSTATE_ACQUIRE = 2
            KSSTATE_PAUSE = 3
            KSSTATE_RUN = 4

        PKSSTATE = POINTER(KSSTATE)


        KSSTATE_STOP = KSSTATE.KSSTATE_STOP
        KSSTATE_ACQUIRE = KSSTATE.KSSTATE_ACQUIRE
        KSSTATE_PAUSE = KSSTATE.KSSTATE_PAUSE
        KSSTATE_RUN = KSSTATE.KSSTATE_RUN
        KSPRIORITY_LOW = 0x00000001
        KSPRIORITY_NORMAL = 0x40000000
        KSPRIORITY_HIGH = 0x80000000
        KSPRIORITY_EXCLUSIVE = 0xFFFFFFFF


        KSPRIORITY._fields_ = [
            ('PriorityClass', ULONG),
            ('PrioritySubClass', ULONG),
        ]


        class _Union_1(ctypes.Union):
            pass


        class _IDENTIFIER(ctypes.Structure):
            pass


        _IDENTIFIER._fields_ = [
            ('Set', GUID),
            ('Id', ULONG),
            ('Flags', ULONG),
        ]
        _Struct_1 = _IDENTIFIER
        _Union_1._Struct_1 = _Struct_1

        _Union_1._anonymous_ = (
            '_Struct_1',
        )

        _Union_1._fields_ = [
            ('_Struct_1', _Union_1._Struct_1),
            ('Alignment', LONGLONG),
        ]
        KSIDENTIFIER._Union_1 = _Union_1

        KSIDENTIFIER._anonymous_ = (
            '_Union_1',
        )

        KSIDENTIFIER._fields_ = [
            ('_Union_1', KSIDENTIFIER._Union_1),
        ]

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
        KSPROPERTY_TYPE_GETPAYLOADSIZE = 0x00000004
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


        KSP_NODE._fields_ = [
            ('Property', KSPROPERTY),
            ('NodeId', ULONG),
            ('Reserved', ULONG),
        ]

        KSM_NODE._fields_ = [
            ('Method', KSMETHOD),
            ('NodeId', ULONG),
            ('Reserved', ULONG),
        ]

        KSE_NODE._fields_ = [
            ('Event', KSEVENT),
            ('NodeId', ULONG),
            ('Reserved', ULONG),
        ]
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
            0x00
        )
        KSPROPTYPESETID_General = DEFINE_GUIDSTRUCT(
            "97E99BA0-BDEA-11CF-A5D6-28DB04C10000"
        )
        KSPROPTYPESETID_General = DEFINE_GUIDNAMED(KSPROPTYPESETID_General)

        if defined(_NTDDK_) and not defined(__wtypes_h__):
            class VARENUM(ENUM):
                VT_EMPTY = 0
                VT_NULL = 1
                VT_I2 = 2
                VT_I4 = 3
                VT_R4 = 4
                VT_R8 = 5
                VT_CY = 6
                VT_DATE = 7
                VT_BSTR = 8
                VT_DISPATCH = 9
                VT_ERROR = 10
                VT_BOOL = 11
                VT_VARIANT = 12
                VT_UNKNOWN = 13
                VT_DECIMAL = 14
                VT_I1 = 16
                VT_UI1 = 17
                VT_UI2 = 18
                VT_UI4 = 19
                VT_I8 = 20
                VT_UI8 = 21
                VT_INT = 22
                VT_UINT = 23
                VT_VOID = 24
                VT_HRESULT = 25
                VT_PTR = 26
                VT_SAFEARRAY = 27
                VT_CARRAY = 28
                VT_USERDEFINED = 29
                VT_LPSTR = 30
                VT_LPWSTR = 31
                VT_FILETIME = 64
                VT_BLOB = 65
                VT_STREAM = 66
                VT_STORAGE = 67
                VT_STREAMED_OBJECT = 68
                VT_STORED_OBJECT = 69
                VT_BLOB_OBJECT = 70
                VT_CF = 71
                VT_CLSID = 72
                VT_VECTOR = 0x1000
                VT_ARRAY = 0x2000
                VT_BYREF = 0x4000
                VT_RESERVED = 0x8000
                VT_ILLEGAL = 0xFFFF
                VT_ILLEGALMASKED = 0xFFF
                VT_TYPEMASK = 0xFFF

            VT_EMPTY = VARENUM.VT_EMPTY
            VT_NULL = VARENUM.VT_NULL
            VT_I2 = VARENUM.VT_I2
            VT_I4 = VARENUM.VT_I4
            VT_R4 = VARENUM.VT_R4
            VT_R8 = VARENUM.VT_R8
            VT_CY = VARENUM.VT_CY
            VT_DATE = VARENUM.VT_DATE
            VT_BSTR = VARENUM.VT_BSTR
            VT_DISPATCH = VARENUM.VT_DISPATCH
            VT_ERROR = VARENUM.VT_ERROR
            VT_BOOL = VARENUM.VT_BOOL
            VT_VARIANT = VARENUM.VT_VARIANT
            VT_UNKNOWN = VARENUM.VT_UNKNOWN
            VT_DECIMAL = VARENUM.VT_DECIMAL
            VT_I1 = VARENUM.VT_I1
            VT_UI1 = VARENUM.VT_UI1
            VT_UI2 = VARENUM.VT_UI2
            VT_UI4 = VARENUM.VT_UI4
            VT_I8 = VARENUM.VT_I8
            VT_UI8 = VARENUM.VT_UI8
            VT_INT = VARENUM.VT_INT
            VT_UINT = VARENUM.VT_UINT
            VT_VOID = VARENUM.VT_VOID
            VT_HRESULT = VARENUM.VT_HRESULT
            VT_PTR = VARENUM.VT_PTR
            VT_SAFEARRAY = VARENUM.VT_SAFEARRAY
            VT_CARRAY = VARENUM.VT_CARRAY
            VT_USERDEFINED = VARENUM.VT_USERDEFINED
            VT_LPSTR = VARENUM.VT_LPSTR
            VT_LPWSTR = VARENUM.VT_LPWSTR
            VT_FILETIME = VARENUM.VT_FILETIME
            VT_BLOB = VARENUM.VT_BLOB
            VT_STREAM = VARENUM.VT_STREAM
            VT_STORAGE = VARENUM.VT_STORAGE
            VT_STREAMED_OBJECT = VARENUM.VT_STREAMED_OBJECT
            VT_STORED_OBJECT = VARENUM.VT_STORED_OBJECT
            VT_BLOB_OBJECT = VARENUM.VT_BLOB_OBJECT
            VT_CF = VARENUM.VT_CF
            VT_CLSID = VARENUM.VT_CLSID
            VT_VECTOR = VARENUM.VT_VECTOR
            VT_ARRAY = VARENUM.VT_ARRAY
            VT_BYREF = VARENUM.VT_BYREF
            VT_RESERVED = VARENUM.VT_RESERVED
            VT_ILLEGAL = VARENUM.VT_ILLEGAL
            VT_ILLEGALMASKED = VARENUM.VT_ILLEGALMASKED
            VT_TYPEMASK = VARENUM.VT_TYPEMASK
        # END IF   _NTDDK_ and not __wtypes_h__


        KSMULTIPLE_ITEM._fields_ = [
            ('Size', ULONG),
            ('Count', ULONG),
        ]

        KSPROPERTY_DESCRIPTION._fields_ = [
            ('AccessFlags', ULONG),
            ('DescriptionSize', ULONG),
            ('PropTypeSet', KSIDENTIFIER),
            ('MembersListCount', ULONG),
            ('Reserved', ULONG),
        ]
        KSPROPERTY_MEMBER_RANGES = 0x00000001
        KSPROPERTY_MEMBER_STEPPEDRANGES = 0x00000002
        KSPROPERTY_MEMBER_VALUES = 0x00000003
        KSPROPERTY_MEMBER_FLAG_DEFAULT = 0x00000001

        if NTDDI_VERSION >= NTDDI_WINXP:
            KSPROPERTY_MEMBER_FLAG_BASICSUPPORT_MULTICHANNEL = 0x00000002
            KSPROPERTY_MEMBER_FLAG_BASICSUPPORT_UNIFORM = 0x00000004
        # END IF   (NTDDI_VERSION >= NTDDI_WINXP)


        KSPROPERTY_MEMBERSHEADER._fields_ = [
            ('MembersFlags', ULONG),
            ('MembersSize', ULONG),
            ('MembersCount', ULONG),
            ('Flags', ULONG),
        ]


        class _SIGNED(ctypes.Structure):
            pass


        _SIGNED._fields_ = [
            ('SignedMinimum', LONG),
            ('SignedMaximum', LONG),
        ]
        _Struct_1 = _SIGNED
        KSPROPERTY_BOUNDS_LONG._Struct_1 = _Struct_1


        class _UNSIGNED(ctypes.Structure):
            pass


        _UNSIGNED._fields_ = [
            ('UnsignedMinimum', ULONG),
            ('UnsignedMaximum', ULONG),
        ]
        _Struct_2 = _UNSIGNED
        KSPROPERTY_BOUNDS_LONG._Struct_2 = _Struct_2

        KSPROPERTY_BOUNDS_LONG._anonymous_ = (
            '_Struct_1',
            '_Struct_2',
        )

        KSPROPERTY_BOUNDS_LONG._fields_ = [
            ('_Struct_1', KSPROPERTY_BOUNDS_LONG._Struct_1),
            ('_Struct_2', KSPROPERTY_BOUNDS_LONG._Struct_2),
        ]


        class _SIGNED64(ctypes.Structure):
            pass


        _SIGNED64._fields_ = [
            ('SignedMinimum', LONGLONG),
            ('SignedMaximum', LONGLONG),
        ]
        _Struct_3 = _SIGNED64
        KSPROPERTY_BOUNDS_LONGLONG._Struct_3 = _Struct_3


        class _UNSIGNED64(ctypes.Structure):
            pass

        _TEMP__UNSIGNED64 = [
        ]

        if defined(_NTDDK_):
             _TEMP__UNSIGNED64 += [
                ('UnsignedMinimum', ULONGLONG),
                ('UnsignedMaximum', ULONGLONG),
            ]
        else: #  not _NTDDK_
            _TEMP__UNSIGNED64 += [
                ('UnsignedMinimum', DWORDLONG),
                ('UnsignedMaximum', DWORDLONG),
            ]
        # END IF   not _NTDDK_


        _UNSIGNED64._fields_ = _TEMP__UNSIGNED64
        _Struct_4 = _UNSIGNED64
        KSPROPERTY_BOUNDS_LONGLONG._Struct_4 = _Struct_4

        KSPROPERTY_BOUNDS_LONGLONG._anonymous_ = (
            '_Struct_3',
            '_Struct_4',
        )

        KSPROPERTY_BOUNDS_LONGLONG._fields_ = [
            ('_Struct_3', KSPROPERTY_BOUNDS_LONGLONG._Struct_3),
            ('_Struct_4', KSPROPERTY_BOUNDS_LONGLONG._Struct_4),
        ]

        KSPROPERTY_STEPPING_LONG._fields_ = [
            ('SteppingDelta', ULONG),
            ('Reserved', ULONG),
            ('Bounds', KSPROPERTY_BOUNDS_LONG),
        ]

        _TEMP_KSPROPERTY_STEPPING_LONGLONG = [
        ]

        if defined(_NTDDK_):
            _TEMP_KSPROPERTY_STEPPING_LONGLONG += [
                ('SteppingDelta', ULONGLONG),
            ]
        else: #  not _NTDDK_
            _TEMP_KSPROPERTY_STEPPING_LONGLONG += [
                ('SteppingDelta', DWORDLONG),
            ]
        # END IF   not _NTDDK_


        _TEMP_KSPROPERTY_STEPPING_LONGLONG += [
            ('Bounds', KSPROPERTY_BOUNDS_LONGLONG),
        ]
        KSPROPERTY_STEPPING_LONGLONG._fields_ = _TEMP_KSPROPERTY_STEPPING_LONGLONG

        # == == == == == == == == == == == == == == == == == == == == == == ==
        if NTDDI_VERSION >= NTDDI_WINXP:
            if defined(_NTDDK_):
                # Structure forward declarations.
                KSDEVICE_DESCRIPTOR = _KSDEVICE_DESCRIPTOR
                PKSDEVICE_DESCRIPTOR = POINTER(_KSDEVICE_DESCRIPTOR)

                KSDEVICE_DISPATCH = _KSDEVICE_DISPATCH
                PKSDEVICE_DISPATCH = POINTER(_KSDEVICE_DISPATCH)

                KSDEVICE = _KSDEVICE
                PKSDEVICE = POINTER(_KSDEVICE)

                KSFILTERFACTORY = _KSFILTERFACTORY
                PKSFILTERFACTORY = POINTER(_KSFILTERFACTORY)

                KSFILTER_DESCRIPTOR = _KSFILTER_DESCRIPTOR
                PKSFILTER_DESCRIPTOR = POINTER(_KSFILTER_DESCRIPTOR)

                KSFILTER_DISPATCH = _KSFILTER_DISPATCH
                PKSFILTER_DISPATCH = POINTER(_KSFILTER_DISPATCH)

                KSFILTER = _KSFILTER
                PKSFILTER = POINTER(_KSFILTER )

                KSPIN_DESCRIPTOR_EX = _KSPIN_DESCRIPTOR_EX
                PKSPIN_DESCRIPTOR_EX = POINTER(_KSPIN_DESCRIPTOR_EX)

                KSPIN_DISPATCH = _KSPIN_DISPATCH
                PKSPIN_DISPATCH = POINTER(_KSPIN_DISPATCH)

                KSCLOCK_DISPATCH = _KSCLOCK_DISPATCH
                PKSCLOCK_DISPATCH = POINTER(_KSCLOCK_DISPATCH)

                KSALLOCATOR_DISPATCH = _KSALLOCATOR_DISPATCH
                PKSALLOCATOR_DISPATCH = POINTER(_KSALLOCATOR_DISPATCH)

                KSPIN = _KSPIN
                PKSPIN = POINTER(_KSPIN)

                KSNODE_DESCRIPTOR = _KSNODE_DESCRIPTOR
                PKSNODE_DESCRIPTOR = POINTER(_KSNODE_DESCRIPTOR)

                KSSTREAM_POINTER_OFFSET = _KSSTREAM_POINTER_OFFSET
                PKSSTREAM_POINTER_OFFSET = POINTER(_KSSTREAM_POINTER_OFFSET)

                KSSTREAM_POINTER = _KSSTREAM_POINTER
                PKSSTREAM_POINTER = POINTER(_KSSTREAM_POINTER)

                KSMAPPING = _KSMAPPING
                PKSMAPPING = POINTER(_KSMAPPING)

                KSPROCESSPIN = _KSPROCESSPIN
                PKSPROCESSPIN = POINTER(_KSPROCESSPIN)

                KSPROCESSPIN_INDEXENTRY = _KSPROCESSPIN_INDEXENTRY
                PKSPROCESSPIN_INDEXENTRY = POINTER(_KSPROCESSPIN_INDEXENTRY)
            # END IF   _NTDDK_
        # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

        PKSWORKER = PVOID

        class _Union_2(ctypes.Union):
            pass


        class EventHandle(ctypes.Structure):
            pass


        EventHandle._fields_ = [
            ('Event', HANDLE),
            ('Reserved', ULONG_PTR * 2),
        ]
        _Union_2.EventHandle = EventHandle


        class SemaphoreHandle(ctypes.Structure):
            pass


        SemaphoreHandle._fields_ = [
            ('Semaphore', HANDLE),
            ('Reserved', ULONG),
            ('Adjustment', LONG),
        ]
        _Union_2.SemaphoreHandle = SemaphoreHandle

        if defined(_NTDDK_):
            from pyWinAPI.km.wdm_h import * # NOQA

            class EventObject(ctypes.Structure):
                pass


            EventObject._fields_ = [
                ('Event', PVOID),
                ('Increment', KPRIORITY),
                ('Reserved', ULONG_PTR),
            ]
            _Union_2.EventObject = EventObject


            class SemaphoreObject(ctypes.Structure):
                pass


            SemaphoreObject._fields_ = [
                ('Semaphore', PVOID),
                ('Increment', KPRIORITY),
                ('Adjustment', LONG),
            ]
            _Union_2.SemaphoreObject = SemaphoreObject


            class Dpc(ctypes.Structure):
                pass


            Dpc._fields_ = [
                ('Dpc', PKDPC),
                ('ReferenceCount', ULONG),
                ('Reserved', ULONG_PTR),
            ]
            _Union_2.Dpc = Dpc


            class WorkItem(ctypes.Structure):
                pass


            WorkItem._fields_ = [
                ('WorkQueueItem', PWORK_QUEUE_ITEM),
                ('WorkQueueType', WORK_QUEUE_TYPE),
                ('Reserved', ULONG_PTR),
            ]
            _Union_2.WorkItem = WorkItem


            class KsWorkItem(ctypes.Structure):
                pass


            KsWorkItem._fields_ = [
                ('WorkQueueItem', PWORK_QUEUE_ITEM),
                ('KsWorkerObject', PKSWORKER),
                ('Reserved', ULONG_PTR),
            ]
            _Union_2.KsWorkItem = KsWorkItem


        class Alignment(ctypes.Structure):
            pass


        Alignment._fields_ = [
            ('Unused', PVOID),
            ('Alignment', LONG_PTR * 2),
        ]
        _Union_2.Alignment = Alignment


        _TEMP__Union_2 = [
            ('EventHandle', _Union_2.EventHandle),
            ('SemaphoreHandle', _Union_2.SemaphoreHandle),
        ]
        if defined(_NTDDK_):
            _TEMP__Union_2 += [
                ('EventObject', _Union_2.EventObject),
                ('SemaphoreObject', _Union_2.SemaphoreObject),
                ('Dpc', _Union_2.Dpc),
                ('WorkItem', _Union_2.WorkItem),
                ('KsWorkItem', _Union_2.KsWorkItem),
            ]
        # END IF   defined(_NTDDK_)


        _TEMP__Union_2 += [
            ('Alignment', _Union_2.Alignment),
        ]
        _Union_2._fields_ = _TEMP__Union_2
        KSEVENTDATA._Union_2 = _Union_2

        KSEVENTDATA._anonymous_ = (
            '_Union_2',
        )

        KSEVENTDATA._fields_ = [
            ('NotificationType', ULONG),
            ('_Union_2', KSEVENTDATA._Union_2),
        ]
        KSEVENTF_EVENT_HANDLE = 0x00000001
        KSEVENTF_SEMAPHORE_HANDLE = 0x00000002

        if defined(_NTDDK_):
            KSEVENTF_EVENT_OBJECT = 0x00000004
            KSEVENTF_SEMAPHORE_OBJECT = 0x00000008
            KSEVENTF_DPC = 0x00000010
            KSEVENTF_WORKITEM = 0x00000020
            KSEVENTF_KSWORKITEM = 0x00000080
        # END IF   defined(_NTDDK_)

        KSEVENT_TYPE_ENABLE = 0x00000001
        KSEVENT_TYPE_ONESHOT = 0x00000002
        KSEVENT_TYPE_ENABLEBUFFERED = 0x00000004
        KSEVENT_TYPE_SETSUPPORT = 0x00000100
        KSEVENT_TYPE_BASICSUPPORT = 0x00000200
        KSEVENT_TYPE_QUERYBUFFER = 0x00000400
        KSEVENT_TYPE_TOPOLOGY = 0x10000000


        KSQUERYBUFFER._fields_ = [
            ('Event', KSEVENT),
            ('EventData', PKSEVENTDATA),
            ('Reserved', PVOID),
        ]


        class _Union_3(ctypes.Union):
            pass


        _Union_3._fields_ = [
            ('ObjectHandle', HANDLE),
            ('ObjectPointer', PVOID),
        ]
        KSRELATIVEEVENT._Union_3 = _Union_3

        KSRELATIVEEVENT._anonymous_ = (
            '_Union_3',
        )

        KSRELATIVEEVENT._fields_ = [
            ('Size', ULONG),
            ('Flags', ULONG),
            ('_Union_3', KSRELATIVEEVENT._Union_3),
            ('Reserved', PVOID),
            ('Event', KSEVENT),
            ('EventData', KSEVENTDATA),
        ]
        KSRELATIVEEVENT_FLAG_HANDLE = 0x00000001
        KSRELATIVEEVENT_FLAG_POINTER = 0x00000002

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        KSEVENT_TIME_MARK._fields_ = [
            ('EventData', KSEVENTDATA),
            ('MarkTime', LONGLONG),
        ]

        KSEVENT_TIME_INTERVAL._fields_ = [
            ('EventData', KSEVENTDATA),
            ('TimeBase', LONGLONG),
            ('Interval', LONGLONG),
        ]

        KSINTERVAL._fields_ = [
            ('TimeBase', LONGLONG),
            ('Interval', LONGLONG),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
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
            0x96
        )
        KSPROPSETID_General = DEFINE_GUIDSTRUCT(
            "1464EDA5-6A8F-11D1-9AA7-00A0C9223196"
        )
        KSPROPSETID_General = DEFINE_GUIDNAMED(KSPROPSETID_General)


        class KSPROPERTY_GENERAL(ENUM):
            KSPROPERTY_GENERAL_COMPONENTID = 1

        KSPROPERTY_GENERAL_COMPONENTID = KSPROPERTY_GENERAL.KSPROPERTY_GENERAL_COMPONENTID

        KSCOMPONENTID._fields_ = [
            ('Manufacturer', GUID),
            ('Product', GUID),
            ('Component', GUID),
            ('Name', GUID),
            ('Version', ULONG),
            ('Revision', ULONG),
        ]


        def DEFINE_KSPROPERTY_ITEM_GENERAL_COMPONENTID(Handler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_GENERAL_COMPONENTID,
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
            0x96
        )
        KSMETHODSETID_StreamIo = DEFINE_GUIDSTRUCT(
            "65D003CA-1523-11D2-B27A-00A0C9223196"
        )
        KSMETHODSETID_StreamIo = DEFINE_GUIDNAMED(KSMETHODSETID_StreamIo)


        class KSMETHOD_STREAMIO(ENUM):
            KSMETHOD_STREAMIO_READ = 1
            KSMETHOD_STREAMIO_WRITE = 2

        KSMETHOD_STREAMIO_READ = KSMETHOD_STREAMIO.KSMETHOD_STREAMIO_READ
        KSMETHOD_STREAMIO_WRITE = KSMETHOD_STREAMIO.KSMETHOD_STREAMIO_WRITE


        def DEFINE_KSMETHOD_ITEM_STREAMIO_READ(Handler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_STREAMIO_READ,
                KSMETHOD_TYPE_WRITE,
                Handler,
                ctypes.sizeof(KSMETHOD),
                0,
                NULL
            )


        def DEFINE_KSMETHOD_ITEM_STREAMIO_WRITE(Handler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_STREAMIO_WRITE,
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
            0x96
        )
        KSPROPSETID_MediaSeeking = DEFINE_GUIDSTRUCT(
            "EE904F0C-D09B-11D0-ABE9-00A0C9223196"
        )
        KSPROPSETID_MediaSeeking = DEFINE_GUIDNAMED(KSPROPSETID_MediaSeeking)


        class KSPROPERTY_MEDIASEEKING(ENUM):
            KSPROPERTY_MEDIASEEKING_CAPABILITIES = 1
            KSPROPERTY_MEDIASEEKING_FORMATS = 2
            KSPROPERTY_MEDIASEEKING_TIMEFORMAT = 3
            KSPROPERTY_MEDIASEEKING_POSITION = 4
            KSPROPERTY_MEDIASEEKING_STOPPOSITION = 5
            KSPROPERTY_MEDIASEEKING_POSITIONS = 6
            KSPROPERTY_MEDIASEEKING_DURATION = 7
            KSPROPERTY_MEDIASEEKING_AVAILABLE = 8
            KSPROPERTY_MEDIASEEKING_PREROLL = 9
            KSPROPERTY_MEDIASEEKING_CONVERTTIMEFORMAT = 10

        KSPROPERTY_MEDIASEEKING_CAPABILITIES = KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_CAPABILITIES
        KSPROPERTY_MEDIASEEKING_FORMATS = KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_FORMATS
        KSPROPERTY_MEDIASEEKING_TIMEFORMAT = KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_TIMEFORMAT
        KSPROPERTY_MEDIASEEKING_POSITION = KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_POSITION
        KSPROPERTY_MEDIASEEKING_STOPPOSITION = KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_STOPPOSITION
        KSPROPERTY_MEDIASEEKING_POSITIONS = KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_POSITIONS
        KSPROPERTY_MEDIASEEKING_DURATION = KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_DURATION
        KSPROPERTY_MEDIASEEKING_AVAILABLE = KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_AVAILABLE
        KSPROPERTY_MEDIASEEKING_PREROLL = KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_PREROLL
        KSPROPERTY_MEDIASEEKING_CONVERTTIMEFORMAT = KSPROPERTY_MEDIASEEKING.KSPROPERTY_MEDIASEEKING_CONVERTTIMEFORMAT


        class KS_SEEKING_FLAGS(ENUM):
            KS_SEEKING_NoPositioning = 1
            KS_SEEKING_AbsolutePositioning = 2
            KS_SEEKING_RelativePositioning = 3
            KS_SEEKING_IncrementalPositioning = 4
            KS_SEEKING_PositioningBitsMask = 0x3
            KS_SEEKING_SeekToKeyFrame = 4
            KS_SEEKING_ReturnTime = 0x8

        KS_SEEKING_NoPositioning = KS_SEEKING_FLAGS.KS_SEEKING_NoPositioning
        KS_SEEKING_AbsolutePositioning = KS_SEEKING_FLAGS.KS_SEEKING_AbsolutePositioning
        KS_SEEKING_RelativePositioning = KS_SEEKING_FLAGS.KS_SEEKING_RelativePositioning
        KS_SEEKING_IncrementalPositioning = KS_SEEKING_FLAGS.KS_SEEKING_IncrementalPositioning
        KS_SEEKING_PositioningBitsMask = KS_SEEKING_FLAGS.KS_SEEKING_PositioningBitsMask
        KS_SEEKING_SeekToKeyFrame = KS_SEEKING_FLAGS.KS_SEEKING_SeekToKeyFrame
        KS_SEEKING_ReturnTime = KS_SEEKING_FLAGS.KS_SEEKING_ReturnTime


        class KS_SEEKING_CAPABILITIES(ENUM):
            KS_SEEKING_CanSeekAbsolute = 0x1
            KS_SEEKING_CanSeekForwards = 0x2
            KS_SEEKING_CanSeekBackwards = 0x4
            KS_SEEKING_CanGetCurrentPos = 0x8
            KS_SEEKING_CanGetStopPos = 0x10
            KS_SEEKING_CanGetDuration = 0x20
            KS_SEEKING_CanPlayBackwards = 0x40

        KS_SEEKING_CanSeekAbsolute = KS_SEEKING_CAPABILITIES.KS_SEEKING_CanSeekAbsolute
        KS_SEEKING_CanSeekForwards = KS_SEEKING_CAPABILITIES.KS_SEEKING_CanSeekForwards
        KS_SEEKING_CanSeekBackwards = KS_SEEKING_CAPABILITIES.KS_SEEKING_CanSeekBackwards
        KS_SEEKING_CanGetCurrentPos = KS_SEEKING_CAPABILITIES.KS_SEEKING_CanGetCurrentPos
        KS_SEEKING_CanGetStopPos = KS_SEEKING_CAPABILITIES.KS_SEEKING_CanGetStopPos
        KS_SEEKING_CanGetDuration = KS_SEEKING_CAPABILITIES.KS_SEEKING_CanGetDuration
        KS_SEEKING_CanPlayBackwards = KS_SEEKING_CAPABILITIES.KS_SEEKING_CanPlayBackwards

        KSPROPERTY_POSITIONS._fields_ = [
            ('Current', LONGLONG),
            ('Stop', LONGLONG),
            ('CurrentFlags', KS_SEEKING_FLAGS),
            ('StopFlags', KS_SEEKING_FLAGS),
        ]

        KSPROPERTY_MEDIAAVAILABLE._fields_ = [
            ('Earliest', LONGLONG),
            ('Latest', LONGLONG),
        ]

        KSP_TIMEFORMAT._fields_ = [
            ('Property', KSPROPERTY),
            ('SourceFormat', GUID),
            ('TargetFormat', GUID),
            ('Time', LONGLONG),
        ]


        def DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_CAPABILITIES(Handler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_MEDIASEEKING_CAPABILITIES,
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
                KSPROPERTY_MEDIASEEKING_FORMATS,
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
                KSPROPERTY_MEDIASEEKING_TIMEFORMAT,
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
                KSPROPERTY_MEDIASEEKING_POSITION,
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
                KSPROPERTY_MEDIASEEKING_STOPPOSITION,
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
                KSPROPERTY_MEDIASEEKING_POSITIONS,
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
                KSPROPERTY_MEDIASEEKING_DURATION,
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
                KSPROPERTY_MEDIASEEKING_AVAILABLE,
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
                KSPROPERTY_MEDIASEEKING_PREROLL,
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
                KSPROPERTY_MEDIASEEKING_CONVERTTIMEFORMAT,
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


        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
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
            0x00
        )
        KSPROPSETID_Topology = DEFINE_GUIDSTRUCT(
            "720D4AC0-7533-11D0-A5D6-28DB04C10000"
        )
        KSPROPSETID_Topology = DEFINE_GUIDNAMED(KSPROPSETID_Topology)


        class KSPROPERTY_TOPOLOGY(ENUM):
            KSPROPERTY_TOPOLOGY_CATEGORIES = 1
            KSPROPERTY_TOPOLOGY_NODES = 2
            KSPROPERTY_TOPOLOGY_CONNECTIONS = 3
            KSPROPERTY_TOPOLOGY_NAME = 4

        KSPROPERTY_TOPOLOGY_CATEGORIES = KSPROPERTY_TOPOLOGY.KSPROPERTY_TOPOLOGY_CATEGORIES
        KSPROPERTY_TOPOLOGY_NODES = KSPROPERTY_TOPOLOGY.KSPROPERTY_TOPOLOGY_NODES
        KSPROPERTY_TOPOLOGY_CONNECTIONS = KSPROPERTY_TOPOLOGY.KSPROPERTY_TOPOLOGY_CONNECTIONS
        KSPROPERTY_TOPOLOGY_NAME = KSPROPERTY_TOPOLOGY.KSPROPERTY_TOPOLOGY_NAME


        def DEFINE_KSPROPERTY_ITEM_TOPOLOGY_CATEGORIES(Handler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_TOPOLOGY_CATEGORIES,
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
                KSPROPERTY_TOPOLOGY_NODES,
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
                KSPROPERTY_TOPOLOGY_CONNECTIONS,
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
                KSPROPERTY_TOPOLOGY_NAME,
                (Handler),
                ctypes.sizeof(KSP_NODE),
                0,
                NULL,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_TOPOLOGYSET(TopologySet, Handler):
                DEFINE_KSPROPERTY_TABLE(TopologySet)
                DEFINE_KSPROPERTY_ITEM_TOPOLOGY_CATEGORIES(Handler),
                DEFINE_KSPROPERTY_ITEM_TOPOLOGY_NODES(Handler),
                DEFINE_KSPROPERTY_ITEM_TOPOLOGY_CONNECTIONS(Handler),
                DEFINE_KSPROPERTY_ITEM_TOPOLOGY_NAME(Handler)


        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == == =
        # properties used by graph manager to talk to particular filters
        if defined(_NTDDK_):
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
                0x5D
            )
            KSPROPSETID_GM = DEFINE_GUIDSTRUCT(
                "AF627536-E719-11D2-8A1D-006097D2DF5D"
            )
            KSPROPSETID_GM = DEFINE_GUIDNAMED(KSPROPSETID_GM)

            # typedef VOID (*PFNKSGRAPHMANAGER_NOTIFY)(_In_ PFILE_OBJECT GraphManager,
            # _In_ ULONG EventId,
            # _In_ PVOID Filter,
            # _In_ PVOID Pin,
            # _In_ PVOID Frame,
            # _In_ ULONG Duration);
            PFNKSGRAPHMANAGER_NOTIFY = CALLBACK(
                VOID,
                ULONG,
                PVOID,
                PVOID,
                PVOID,
                ULONG,
            )


            KSGRAPHMANAGER_FUNCTIONTABLE._fields_ = [
                ('NotifyEvent', PFNKSGRAPHMANAGER_NOTIFY),
            ]

            _KSPROPERTY_GRAPHMANAGER_INTERFACE._fields_ = [
                ('GraphManager', PFILE_OBJECT),
                ('FunctionTable', KSGRAPHMANAGER_FUNCTIONTABLE),
            ]


            # Commands
            class KSPROPERTY_GM(ENUM):
                KSPROPERTY_GM_GRAPHMANAGER = 1
                KSPROPERTY_GM_TIMESTAMP_CLOCK = 2
                KSPROPERTY_GM_RATEMATCH = 3
                KSPROPERTY_GM_RENDER_CLOCK = 4

            KSPROPERTY_GM_GRAPHMANAGER = KSPROPERTY_GM.KSPROPERTY_GM_GRAPHMANAGER
            KSPROPERTY_GM_TIMESTAMP_CLOCK = KSPROPERTY_GM.KSPROPERTY_GM_TIMESTAMP_CLOCK
            KSPROPERTY_GM_RATEMATCH = KSPROPERTY_GM.KSPROPERTY_GM_RATEMATCH
            KSPROPERTY_GM_RENDER_CLOCK = KSPROPERTY_GM.KSPROPERTY_GM_RENDER_CLOCK
        # END IF


        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
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
            0x00
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
            0x96
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
            0x44
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
            0xCA
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
            0xBD
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
            0x96
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
            0x00
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
            0x00
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
            0x00
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
            0x00
        )
        KSCATEGORY_DATADECOMPRESSOR = DEFINE_GUIDSTRUCT(
            "2721AE20-7E70-11D0-A5D6-28DB04C10000"
        )
        KSCATEGORY_DATADECOMPRESSOR = (
            DEFINE_GUIDNAMED(KSCATEGORY_DATADECOMPRESSOR)
        )
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
            0x00
        )
        KSCATEGORY_DATATRANSFORM = DEFINE_GUIDSTRUCT(
            "2EB07EA0-7E70-11D0-A5D6-28DB04C10000"
        )
        KSCATEGORY_DATATRANSFORM = DEFINE_GUIDNAMED(KSCATEGORY_DATATRANSFORM)


        # KSMFT_CATEGORY_XXX are MF Transform category guids redefined in ks.h
        # to facilitate KS Mini drivers to register KS Filters under MF
        # Transform categories.
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
            0x91
        )
        KSMFT_CATEGORY_VIDEO_DECODER = DEFINE_GUIDSTRUCT(
            "d6c02d4b-6833-45b4-971a-05a4b04bab91"
        )
        KSMFT_CATEGORY_VIDEO_DECODER = (
            DEFINE_GUIDNAMED(KSMFT_CATEGORY_VIDEO_DECODER)
        )
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
            0x2A
        )
        KSMFT_CATEGORY_VIDEO_ENCODER = DEFINE_GUIDSTRUCT(
            "f79eac7d-e545-4387-bdee-d647d7bde42a"
        )
        KSMFT_CATEGORY_VIDEO_ENCODER = (
            DEFINE_GUIDNAMED(KSMFT_CATEGORY_VIDEO_ENCODER)
        )
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
            0x97
        )
        KSMFT_CATEGORY_VIDEO_EFFECT = DEFINE_GUIDSTRUCT(
            "12e17c21-532c-4a6e-8a1c-40825a736397"
        )
        KSMFT_CATEGORY_VIDEO_EFFECT = (
            DEFINE_GUIDNAMED(KSMFT_CATEGORY_VIDEO_EFFECT)
        )
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
            0x7B
        )
        KSMFT_CATEGORY_MULTIPLEXER = DEFINE_GUIDSTRUCT(
            "059c561e-05ae-4b61-b69d-55b61ee54a7b"
        )
        KSMFT_CATEGORY_MULTIPLEXER = (
            DEFINE_GUIDNAMED(KSMFT_CATEGORY_MULTIPLEXER)
        )
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
            0xF1
        )
        KSMFT_CATEGORY_DEMULTIPLEXER = DEFINE_GUIDSTRUCT(
            "a8700a7a-939b-44c5-99d7-76226b23b3f1"
        )
        KSMFT_CATEGORY_DEMULTIPLEXER = (
            DEFINE_GUIDNAMED(KSMFT_CATEGORY_DEMULTIPLEXER)
        )
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
            0xC7
        )
        KSMFT_CATEGORY_AUDIO_DECODER = DEFINE_GUIDSTRUCT(
            "9ea73fb4-ef7a-4559-8d5d-719d8f0426c7"
        )
        KSMFT_CATEGORY_AUDIO_DECODER = (
            DEFINE_GUIDNAMED(KSMFT_CATEGORY_AUDIO_DECODER)
        )
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
            0x75
        )
        KSMFT_CATEGORY_AUDIO_ENCODER = DEFINE_GUIDSTRUCT(
            "91c64bd0-f91e-4d8c-9276-db248279d975"
        )
        KSMFT_CATEGORY_AUDIO_ENCODER = (
            DEFINE_GUIDNAMED(KSMFT_CATEGORY_AUDIO_ENCODER)
        )
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
            0xB7
        )
        KSMFT_CATEGORY_AUDIO_EFFECT = DEFINE_GUIDSTRUCT(
            "11064c48-3648-4ed0-932e-05ce8ac811b7"
        )
        KSMFT_CATEGORY_AUDIO_EFFECT = (
            DEFINE_GUIDNAMED(KSMFT_CATEGORY_AUDIO_EFFECT)
        )
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
            0x2
        )
        KSMFT_CATEGORY_VIDEO_PROCESSOR = DEFINE_GUIDSTRUCT(
            "302ea3fc-aa5f-47f9-9f7a-c2188bb16302"
        )
        KSMFT_CATEGORY_VIDEO_PROCESSOR = (
            DEFINE_GUIDNAMED(KSMFT_CATEGORY_VIDEO_PROCESSOR)
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
            0x6F
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
            0x96
        )
        KSCATEGORY_COMMUNICATIONSTRANSFORM = DEFINE_GUIDSTRUCT(
            "CF1DDA2C-9743-11D0-A3EE-00A0C9223196"
        )
        KSCATEGORY_COMMUNICATIONSTRANSFORM = (
            DEFINE_GUIDNAMED(KSCATEGORY_COMMUNICATIONSTRANSFORM)
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
            0x96
        )
        KSCATEGORY_INTERFACETRANSFORM = DEFINE_GUIDSTRUCT(
            "CF1DDA2D-9743-11D0-A3EE-00A0C9223196"
        )
        KSCATEGORY_INTERFACETRANSFORM = (
            DEFINE_GUIDNAMED(KSCATEGORY_INTERFACETRANSFORM)
        )
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
            0x96
        )
        KSCATEGORY_MEDIUMTRANSFORM = DEFINE_GUIDSTRUCT(
            "CF1DDA2E-9743-11D0-A3EE-00A0C9223196"
        )
        KSCATEGORY_MEDIUMTRANSFORM = (
            DEFINE_GUIDNAMED(KSCATEGORY_MEDIUMTRANSFORM)
        )
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
            0x96
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
            0x00
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
            0x96
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
            0x96
        )
        KSCATEGORY_QUALITY = DEFINE_GUIDSTRUCT(
            "97EBAACB-95BD-11D0-A3EA-00A0C9223196"
        )
        KSCATEGORY_QUALITY = DEFINE_GUIDNAMED(KSCATEGORY_QUALITY)


        KSTOPOLOGY_CONNECTION._fields_ = [
            ('FromNode', ULONG),
            ('FromNodePin', ULONG),
            ('ToNode', ULONG),
            ('ToNodePin', ULONG),
        ]

        KSTOPOLOGY._fields_ = [
            ('CategoriesCount', ULONG),
            ('Categories', POINTER(GUID)),
            ('TopologyNodesCount', ULONG),
            ('TopologyNodes', POINTER(GUID)),
            ('TopologyConnectionsCount', ULONG),
            ('TopologyConnections', POINTER(KSTOPOLOGY_CONNECTION)),
            ('TopologyNodesNames', POINTER(GUID)),
            ('Reserved', ULONG),
        ]
        KSFILTER_NODE = -1
        KSALL_NODES = -1


        KSNODE_CREATE._fields_ = [
            ('CreateFlags', ULONG),
            ('Node', ULONG),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
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
            0xF6
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
            0xF6
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
            0xF6
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
            0xF6
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
            0xF6
        )
        KSTIME_FORMAT_MEDIA_TIME = DEFINE_GUIDSTRUCT(
            "7b785574-8c82-11cf-bc0c-00aa00ac74f6"
        )
        KSTIME_FORMAT_MEDIA_TIME = DEFINE_GUIDNAMED(KSTIME_FORMAT_MEDIA_TIME)

        # == == == == == == == == == == == == == == == == == == == == == == ==
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
            0x00
        )
        KSINTERFACESETID_Standard = DEFINE_GUIDSTRUCT(
            "1A8766A0-62CE-11CF-A5D6-28DB04C10000"
        )
        KSINTERFACESETID_Standard = DEFINE_GUIDNAMED(KSINTERFACESETID_Standard)


        class KSINTERFACE_STANDARD(ENUM):
            KSINTERFACE_STANDARD_STREAMING = 1
            KSINTERFACE_STANDARD_LOOPED_STREAMING = 2
            KSINTERFACE_STANDARD_CONTROL = 3

        KSINTERFACE_STANDARD_STREAMING = KSINTERFACE_STANDARD.KSINTERFACE_STANDARD_STREAMING
        KSINTERFACE_STANDARD_LOOPED_STREAMING = KSINTERFACE_STANDARD.KSINTERFACE_STANDARD_LOOPED_STREAMING
        KSINTERFACE_STANDARD_CONTROL = KSINTERFACE_STANDARD.KSINTERFACE_STANDARD_CONTROL
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
            0x96
        )
        KSINTERFACESETID_FileIo = DEFINE_GUIDSTRUCT(
            "8C6F932C-E771-11D0-B8FF-00A0C9223196"
        )
        KSINTERFACESETID_FileIo = DEFINE_GUIDNAMED(KSINTERFACESETID_FileIo)


        class KSINTERFACE_FILEIO(ENUM):
            KSINTERFACE_FILEIO_STREAMING = 1

        KSINTERFACE_FILEIO_STREAMING = KSINTERFACE_FILEIO.KSINTERFACE_FILEIO_STREAMING

        # == == == == == == == == == == == == == == == == == == == == == == ==
        KSMEDIUM_TYPE_ANYINSTANCE = 0
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
            0x00
        )
        KSMEDIUMSETID_Standard = DEFINE_GUIDSTRUCT(
            "4747B320-62CE-11CF-A5D6-28DB04C10000"
        )
        KSMEDIUMSETID_Standard = DEFINE_GUIDNAMED(KSMEDIUMSETID_Standard)

        # For compatibility only
        KSMEDIUM_STANDARD_DEVIO = KSMEDIUM_TYPE_ANYINSTANCE

        # == == == == == == == == == == == == == == == == == == == == == == ==
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
            0x00
        )
        KSPROPSETID_Pin = DEFINE_GUIDSTRUCT(
            "8C134960-51AD-11CF-878A-94F801C10000"
        )
        KSPROPSETID_Pin = DEFINE_GUIDNAMED(KSPROPSETID_Pin)


        class KSPROPERTY_PIN(ENUM):
            KSPROPERTY_PIN_CINSTANCES = 1
            KSPROPERTY_PIN_CTYPES = 2
            KSPROPERTY_PIN_DATAFLOW = 3
            KSPROPERTY_PIN_DATARANGES = 4
            KSPROPERTY_PIN_DATAINTERSECTION = 5
            KSPROPERTY_PIN_INTERFACES = 6
            KSPROPERTY_PIN_MEDIUMS = 7
            KSPROPERTY_PIN_COMMUNICATION = 8
            KSPROPERTY_PIN_GLOBALCINSTANCES = 9
            KSPROPERTY_PIN_NECESSARYINSTANCES = 10
            KSPROPERTY_PIN_PHYSICALCONNECTION = 11
            KSPROPERTY_PIN_CATEGORY = 12
            KSPROPERTY_PIN_NAME = 13
            KSPROPERTY_PIN_CONSTRAINEDDATARANGES = 14
            KSPROPERTY_PIN_PROPOSEDATAFORMAT = 15
            KSPROPERTY_PIN_PROPOSEDATAFORMAT2 = 16

        KSPROPERTY_PIN_CINSTANCES = KSPROPERTY_PIN.KSPROPERTY_PIN_CINSTANCES
        KSPROPERTY_PIN_CTYPES = KSPROPERTY_PIN.KSPROPERTY_PIN_CTYPES
        KSPROPERTY_PIN_DATAFLOW = KSPROPERTY_PIN.KSPROPERTY_PIN_DATAFLOW
        KSPROPERTY_PIN_DATARANGES = KSPROPERTY_PIN.KSPROPERTY_PIN_DATARANGES
        KSPROPERTY_PIN_DATAINTERSECTION = KSPROPERTY_PIN.KSPROPERTY_PIN_DATAINTERSECTION
        KSPROPERTY_PIN_INTERFACES = KSPROPERTY_PIN.KSPROPERTY_PIN_INTERFACES
        KSPROPERTY_PIN_MEDIUMS = KSPROPERTY_PIN.KSPROPERTY_PIN_MEDIUMS
        KSPROPERTY_PIN_COMMUNICATION = KSPROPERTY_PIN.KSPROPERTY_PIN_COMMUNICATION
        KSPROPERTY_PIN_GLOBALCINSTANCES = KSPROPERTY_PIN.KSPROPERTY_PIN_GLOBALCINSTANCES
        KSPROPERTY_PIN_NECESSARYINSTANCES = KSPROPERTY_PIN.KSPROPERTY_PIN_NECESSARYINSTANCES
        KSPROPERTY_PIN_PHYSICALCONNECTION = KSPROPERTY_PIN.KSPROPERTY_PIN_PHYSICALCONNECTION
        KSPROPERTY_PIN_CATEGORY = KSPROPERTY_PIN.KSPROPERTY_PIN_CATEGORY
        KSPROPERTY_PIN_NAME = KSPROPERTY_PIN.KSPROPERTY_PIN_NAME
        KSPROPERTY_PIN_CONSTRAINEDDATARANGES = KSPROPERTY_PIN.KSPROPERTY_PIN_CONSTRAINEDDATARANGES
        KSPROPERTY_PIN_PROPOSEDATAFORMAT = KSPROPERTY_PIN.KSPROPERTY_PIN_PROPOSEDATAFORMAT
        KSPROPERTY_PIN_PROPOSEDATAFORMAT2 = KSPROPERTY_PIN.KSPROPERTY_PIN_PROPOSEDATAFORMAT2
        KSPROPERTY_PIN_FLAGS_ATTRIBUTE_RANGE_AWARE = 0x00000001
        KSPROPERTY_PIN_FLAGS_MASK = KSPROPERTY_PIN_FLAGS_ATTRIBUTE_RANGE_AWARE


        class _Union_4(ctypes.Union):
            pass


        _Union_4._fields_ = [
            ('Reserved', ULONG),
            ('Flags', ULONG),
        ]
        KSP_PIN._Union_4 = _Union_4

        KSP_PIN._anonymous_ = (
            '_Union_4',
        )

        KSP_PIN._fields_ = [
            ('Property', KSPROPERTY),
            ('PinId', ULONG),
            ('_Union_4', KSP_PIN._Union_4),
        ]

        KSE_PIN._fields_ = [
            ('Event', KSEVENT),
            ('PinId', ULONG),
            ('Reserved', ULONG),
        ]
        KSINSTANCE_INDETERMINATE = -1


        KSPIN_CINSTANCES._fields_ = [
            ('PossibleCount', ULONG),
            ('CurrentCount', ULONG),
        ]


        class KSPIN_DATAFLOW(ENUM):
            KSPIN_DATAFLOW_IN = 1
            KSPIN_DATAFLOW_OUT = 2

        PKSPIN_DATAFLOW = POINTER(KSPIN_DATAFLOW)


        KSPIN_DATAFLOW_IN = KSPIN_DATAFLOW.KSPIN_DATAFLOW_IN
        KSPIN_DATAFLOW_OUT = KSPIN_DATAFLOW.KSPIN_DATAFLOW_OUT
        KSDATAFORMAT_BIT_TEMPORAL_COMPRESSION = 0
        KSDATAFORMAT_TEMPORAL_COMPRESSION = (
            1 << KSDATAFORMAT_BIT_TEMPORAL_COMPRESSION
        )
        KSDATAFORMAT_BIT_ATTRIBUTES = 1
        KSDATAFORMAT_ATTRIBUTES = 1 << KSDATAFORMAT_BIT_ATTRIBUTES
        KSDATARANGE_BIT_ATTRIBUTES = 1
        KSDATARANGE_ATTRIBUTES = 1 << KSDATARANGE_BIT_ATTRIBUTES
        KSDATARANGE_BIT_REQUIRED_ATTRIBUTES = 2
        KSDATARANGE_REQUIRED_ATTRIBUTES = (
            1 << KSDATARANGE_BIT_REQUIRED_ATTRIBUTES
        )

        if not defined(_MSC_VER):
            KSDATAFORMAT._fields_ = [
                ('FormatSize', ULONG),
                ('Flags', ULONG),
                ('SampleSize', ULONG),
                ('Reserved', ULONG),
                ('MajorFormat', GUID),
                ('SubFormat', GUID),
                ('Specifier', GUID),
            ]
        else:
            class _Struct_5(ctypes.Structure):
                pass


            _Struct_5._fields_ = [
                ('FormatSize', ULONG),
                ('Flags', ULONG),
                ('SampleSize', ULONG),
                ('Reserved', ULONG),
                ('MajorFormat', GUID),
                ('SubFormat', GUID),
                ('Specifier', GUID),
            ]
            KSDATAFORMAT._Struct_5 = _Struct_5

            KSDATAFORMAT._anonymous_ = (
                '_Struct_5',
            )

            KSDATAFORMAT._fields_ = [
                ('_Struct_5', KSDATAFORMAT._Struct_5),
                ('Alignment', LONGLONG),
            ]
        # END IF


        KSATTRIBUTE_REQUIRED = 0x00000001


        KSATTRIBUTE._fields_ = [
            ('Size', ULONG),
            ('Flags', ULONG),
            ('Attribute', GUID),
        ]
        if defined(_NTDDK_):
            KSATTRIBUTE_LIST._fields_ = [
                ('Count', ULONG),
                ('Attributes', POINTER(PKSATTRIBUTE)),
            ]
        # END IF   _NTDDK_


        class KSPIN_COMMUNICATION(ENUM):
            KSPIN_COMMUNICATION_NONE = 1
            KSPIN_COMMUNICATION_SINK = 2
            KSPIN_COMMUNICATION_SOURCE = 3
            KSPIN_COMMUNICATION_BOTH = 4
            KSPIN_COMMUNICATION_BRIDGE = 5

        PKSPIN_COMMUNICATION = POINTER(KSPIN_COMMUNICATION)


        KSPIN_COMMUNICATION_NONE = KSPIN_COMMUNICATION.KSPIN_COMMUNICATION_NONE
        KSPIN_COMMUNICATION_SINK = KSPIN_COMMUNICATION.KSPIN_COMMUNICATION_SINK
        KSPIN_COMMUNICATION_SOURCE = KSPIN_COMMUNICATION.KSPIN_COMMUNICATION_SOURCE
        KSPIN_COMMUNICATION_BOTH = KSPIN_COMMUNICATION.KSPIN_COMMUNICATION_BOTH
        KSPIN_COMMUNICATION_BRIDGE = KSPIN_COMMUNICATION.KSPIN_COMMUNICATION_BRIDGE

        KSPIN_MEDIUM = KSIDENTIFIER
        PKSPIN_MEDIUM = POINTER(KSIDENTIFIER)


        KSPIN_CONNECT._fields_ = [
            ('Interface', KSPIN_INTERFACE),
            ('Medium', KSPIN_MEDIUM),
            ('PinId', ULONG),
            ('PinToHandle', HANDLE),
            ('Priority', KSPRIORITY),
        ]

        KSPIN_PHYSICALCONNECTION._fields_ = [
            ('Size', ULONG),
            ('Pin', ULONG),
            ('SymbolicLinkName', WCHAR * 1),
        ]
        if defined(_NTDDK_):
            # NTSTATUS
            # (*PFNKSINTERSECTHANDLER)(
            # _In_ PIRP Irp,
            # _In_ PKSP_PIN Pin,
            # _In_ PKSDATARANGE DataRange,
            # _Out_opt_ PVOID Data
            # );
            PFNKSINTERSECTHANDLER = CALLBACK(
                NTSTATUS,
                PIRP,
                PKSP_PIN,
                PKSDATARANGE,
                PVOID,
            )


            # _Must_inspect_result_
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # typedef
            # NTSTATUS
            # (*PFNKSINTERSECTHANDLEREX)(
            # _In_ PVOID Context,
            # _In_ PIRP Irp,
            # _In_ PKSP_PIN Pin,
            # _In_ PKSDATARANGE DataRange,
            # _In_ PKSDATARANGE MatchingDataRange,
            # _In_ ULONG DataBufferSize,
            # _Out_writes_bytes_to_opt_(DataBufferSize, *DataSize) PVOID Data,
            # _Out_ PULONG DataSize
            # );
            PFNKSINTERSECTHANDLEREX = CALLBACK(
                NTSTATUS,
                PVOID,
                PIRP,
                PKSP_PIN,
                PKSDATARANGE,
                PKSDATARANGE,
                ULONG,
                PVOID,
                PULONG,
            )


        # END IF   _NTDDK_


        def DEFINE_KSPIN_INTERFACE_TABLE(tablename):
            return  KSPIN_INTERFACE * 0


        def DEFINE_KSPIN_INTERFACE_ITEM(guid, interface):
            return STATICGUIDOF(guid) # , interface, 0)


        def DEFINE_KSPIN_MEDIUM_TABLE(tablename):
            return KSPIN_MEDIUM * 0


        def DEFINE_KSPIN_MEDIUM_ITEM(guid, medium):
            return DEFINE_KSPIN_INTERFACE_ITEM(guid, medium)


        def DEFINE_KSPROPERTY_ITEM_PIN_CINSTANCES(Handler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_PIN_CINSTANCES,
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
                KSPROPERTY_PIN_CTYPES,
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
                KSPROPERTY_PIN_DATAFLOW,
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
                KSPROPERTY_PIN_DATARANGES,
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
                KSPROPERTY_PIN_DATAINTERSECTION,
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
                KSPROPERTY_PIN_INTERFACES,
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
                KSPROPERTY_PIN_MEDIUMS,
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
                KSPROPERTY_PIN_COMMUNICATION,
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
                KSPROPERTY_PIN_GLOBALCINSTANCES,
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
                KSPROPERTY_PIN_NECESSARYINSTANCES,
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
                KSPROPERTY_PIN_PHYSICALCONNECTION,
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
                KSPROPERTY_PIN_CATEGORY,
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
                KSPROPERTY_PIN_NAME,
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
                KSPROPERTY_PIN_CONSTRAINEDDATARANGES,
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
                KSPROPERTY_PIN_PROPOSEDATAFORMAT,
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
        def DEFINE_KSPROPERTY_PINSET(PinSet, PropGeneral, PropInstances, PropIntersection):
            DEFINE_KSPROPERTY_TABLE(PinSet)
            DEFINE_KSPROPERTY_ITEM_PIN_CINSTANCES(PropInstances)
            DEFINE_KSPROPERTY_ITEM_PIN_CTYPES(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_DATAFLOW(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_DATARANGES(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_DATAINTERSECTION(PropIntersection)
            DEFINE_KSPROPERTY_ITEM_PIN_INTERFACES(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_MEDIUMS(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_COMMUNICATION(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_CATEGORY(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_NAME(PropGeneral)


        def DEFINE_KSPROPERTY_PINSETCONSTRAINED(PinSet, PropGeneral, PropInstances, PropIntersection):
            DEFINE_KSPROPERTY_TABLE(PinSet)
            DEFINE_KSPROPERTY_ITEM_PIN_CINSTANCES(PropInstances)
            DEFINE_KSPROPERTY_ITEM_PIN_CTYPES(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_DATAFLOW(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_DATARANGES(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_DATAINTERSECTION(PropIntersection)
            DEFINE_KSPROPERTY_ITEM_PIN_INTERFACES(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_MEDIUMS(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_COMMUNICATION(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_CATEGORY(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_NAME(PropGeneral)
            DEFINE_KSPROPERTY_ITEM_PIN_CONSTRAINEDDATARANGES(PropGeneral)


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
            0x00
        )
        KSEVENTSETID_PinCapsChange = DEFINE_GUIDSTRUCT(
            "DD4F192E-3B78-49AD-A534-2C315B822000"
        )
        KSEVENTSETID_PinCapsChange = (
            DEFINE_GUIDNAMED(KSEVENTSETID_PinCapsChange)
        )


        class KSEVENT_PINCAPS_CHANGENOTIFICATIONS(ENUM):
            KSEVENT_PINCAPS_FORMATCHANGE = 1
            KSEVENT_PINCAPS_JACKINFOCHANGE = 2

        KSEVENT_PINCAPS_FORMATCHANGE = KSEVENT_PINCAPS_CHANGENOTIFICATIONS.KSEVENT_PINCAPS_FORMATCHANGE
        KSEVENT_PINCAPS_JACKINFOCHANGE = KSEVENT_PINCAPS_CHANGENOTIFICATIONS.KSEVENT_PINCAPS_JACKINFOCHANGE
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
            0xEF
        )
        KSEVENTSETID_VolumeLimit = DEFINE_GUIDSTRUCT(
            "DA168465-3A7C-4858-9D4A-3E8E24701AEF"
        )
        KSEVENTSETID_VolumeLimit = DEFINE_GUIDNAMED(KSEVENTSETID_VolumeLimit)


        class KSEVENT_VOLUMELIMIT(ENUM):
            KSEVENT_VOLUMELIMIT_CHANGED = 1

        KSEVENT_VOLUMELIMIT_CHANGED = KSEVENT_VOLUMELIMIT.KSEVENT_VOLUMELIMIT_CHANGED
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
            0xE4
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
            0x00
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
            0x00
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
            0x00
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
            0x96
        )
        KSNAME_TopologyNode = DEFINE_GUIDSTRUCT(
            "0621061A-EE75-11D0-B915-00A0C9223196"
        )
        KSNAME_TopologyNode = DEFINE_GUIDNAMED(KSNAME_TopologyNode)
        KSSTRING_TopologyNode = "[0621061A-EE75-11D0-B915-00A0C9223196]"

        if defined(_NTDDK_):
            class _Union_5(ctypes.Union):
                pass


            class _Struct_6(ctypes.Structure):
                pass


            _Struct_6._fields_ = [
                ('ConstrainedDataRangesCount', ULONG),
                ('ConstrainedDataRanges', POINTER(PKSDATARANGE)),
            ]
            _Union_5._Struct_6 = _Struct_6

            _Union_5._anonymous_ = (
                '_Struct_6',
            )

            _Union_5._fields_ = [
                ('Reserved', LONGLONG),
                ('_Struct_6', _Union_5._Struct_6),
            ]
            KSPIN_DESCRIPTOR._Union_5 = _Union_5

            KSPIN_DESCRIPTOR._anonymous_ = (
                '_Union_5',
            )

            KSPIN_DESCRIPTOR._fields_ = [
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
                ('_Union_5', KSPIN_DESCRIPTOR._Union_5),
            ]

            PCKSPIN_DESCRIPTOR = POINTER(KSPIN_DESCRIPTOR)

            def DEFINE_KSPIN_DESCRIPTOR_TABLE(tablename):
                return KSPIN_DESCRIPTOR * 0


            def DEFINE_KSPIN_DESCRIPTOR_ITEM(InterfacesCount, Interfaces, MediumsCount, Mediums, DataRangesCount, DataRanges, DataFlow, Communication):
                return InterfacesCount, Interfaces, MediumsCount, Mediums, DataRangesCount, DataRanges, DataFlow, Communication, NULL, NULL, 0


            def DEFINE_KSPIN_DESCRIPTOR_ITEMEX(InterfacesCount, Interfaces, MediumsCount, Mediums, DataRangesCount, DataRanges, DataFlow, Communication, Category, Name):
                return InterfacesCount, Interfaces, MediumsCount, Mediums, DataRangesCount, DataRanges, DataFlow, Communication, Category, Name, 0
        # END IF   defined(_NTDDK_)

        # == == == == == == == == == == == == == == == == == == == == == == ==

        # MEDIATYPE_NULL
        STATIC_KSDATAFORMAT_TYPE_WILDCARD = STATIC_GUID_NULL
        KSDATAFORMAT_TYPE_WILDCARD = GUID_NULL

        # MEDIASUBTYPE_NULL
        STATIC_KSDATAFORMAT_SUBTYPE_WILDCARD = STATIC_GUID_NULL
        KSDATAFORMAT_SUBTYPE_WILDCARD = GUID_NULL

        # MEDIATYPE_Stream
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
            0x70
        )
        KSDATAFORMAT_TYPE_STREAM = DEFINE_GUIDSTRUCT(
            "E436EB83-524F-11CE-9F53-0020AF0BA770"
        )
        KSDATAFORMAT_TYPE_STREAM = DEFINE_GUIDNAMED(KSDATAFORMAT_TYPE_STREAM)

        # MEDIASUBTYPE_None
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
            0x70
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
            0x00
        )
        KSDATAFORMAT_SPECIFIER_FILENAME = DEFINE_GUIDSTRUCT(
            "AA797B40-E974-11CF-A5D6-28DB04C10000"
        )
        KSDATAFORMAT_SPECIFIER_FILENAME = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SPECIFIER_FILENAME)
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
            0x96
        )
        KSDATAFORMAT_SPECIFIER_FILEHANDLE = DEFINE_GUIDSTRUCT(
            "65E8773C-8F56-11D0-A3B9-00A0C9223196"
        )
        KSDATAFORMAT_SPECIFIER_FILEHANDLE = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SPECIFIER_FILEHANDLE)
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
            0x96
        )
        KSDATAFORMAT_SPECIFIER_NONE = DEFINE_GUIDSTRUCT(
            "0F6417D6-C318-11D0-A43F-00A0C9223196"
        )
        KSDATAFORMAT_SPECIFIER_NONE = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SPECIFIER_NONE)
        )

        # == == == == == == == == == == == == == == == == == == == == == == ==
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
            0x00
        )
        KSPROPSETID_Quality = DEFINE_GUIDSTRUCT(
            "D16AD380-AC1A-11CF-A5D6-28DB04C10000"
        )
        KSPROPSETID_Quality = DEFINE_GUIDNAMED(KSPROPSETID_Quality)


        class KSPROPERTY_QUALITY(ENUM):
            KSPROPERTY_QUALITY_REPORT = 1
            KSPROPERTY_QUALITY_ERROR = 2

        KSPROPERTY_QUALITY_REPORT = KSPROPERTY_QUALITY.KSPROPERTY_QUALITY_REPORT
        KSPROPERTY_QUALITY_ERROR = KSPROPERTY_QUALITY.KSPROPERTY_QUALITY_ERROR


        def DEFINE_KSPROPERTY_ITEM_QUALITY_REPORT(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_QUALITY_REPORT,
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
                KSPROPERTY_QUALITY_ERROR,
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


        # == == == == == == == == == == == == == == == == == == == == == == ==
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
            0x00
        )
        KSPROPSETID_Connection = DEFINE_GUIDSTRUCT(
            "1D58C920-AC9B-11CF-A5D6-28DB04C10000"
        )
        KSPROPSETID_Connection = DEFINE_GUIDNAMED(KSPROPSETID_Connection)


        class KSPROPERTY_CONNECTION(ENUM):
            KSPROPERTY_CONNECTION_STATE = 1
            KSPROPERTY_CONNECTION_PRIORITY = 2
            KSPROPERTY_CONNECTION_DATAFORMAT = 3
            KSPROPERTY_CONNECTION_ALLOCATORFRAMING = 4
            KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT = 5
            KSPROPERTY_CONNECTION_ACQUIREORDERING = 6
            KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX = 7
            KSPROPERTY_CONNECTION_STARTAT = 8

        KSPROPERTY_CONNECTION_STATE = KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_STATE
        KSPROPERTY_CONNECTION_PRIORITY = KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_PRIORITY
        KSPROPERTY_CONNECTION_DATAFORMAT = KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_DATAFORMAT
        KSPROPERTY_CONNECTION_ALLOCATORFRAMING = KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_ALLOCATORFRAMING
        KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT = KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT
        KSPROPERTY_CONNECTION_ACQUIREORDERING = KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_ACQUIREORDERING
        KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX = KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX
        KSPROPERTY_CONNECTION_STARTAT = KSPROPERTY_CONNECTION.KSPROPERTY_CONNECTION_STARTAT


        def DEFINE_KSPROPERTY_ITEM_CONNECTION_STATE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_CONNECTION_STATE,
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
                KSPROPERTY_CONNECTION_PRIORITY,
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
                KSPROPERTY_CONNECTION_DATAFORMAT,
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
                KSPROPERTY_CONNECTION_ALLOCATORFRAMING,
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
                KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX,
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
                KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT,
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
                KSPROPERTY_CONNECTION_ACQUIREORDERING,
                Handler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(int),
                NULL,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_CONNECTION_STARTAT(Handler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_CONNECTION_STARTAT,
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


        # == == == == == == == == == == == == == == == == == == == == == == ==
        # VRAM transport related propset
        # == == == == == == == == == == == == == == == == == == == == == == ==
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
            0x2B
        )
        KSPROPSETID_MemoryTransport = DEFINE_GUIDSTRUCT(
            "0A3D1C5D-5243-4819-9ED0-AEE8044CEE2B"
        )
        KSPROPSETID_MemoryTransport = (
            DEFINE_GUIDNAMED(KSPROPSETID_MemoryTransport)
        )
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


        # == == == == == == == == == == == == == == == == == == == == == == ==
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
        KSALLOCATOR_FLAG_ALLOCATOR_EXISTS = 0x00000800
        # there is no framing dependency between neighbouring pipes.
        KSALLOCATOR_FLAG_INDEPENDENT_RANGES = 0x00001000
        KSALLOCATOR_FLAG_ATTENTION_STEPPING = 0x00002000
        KSALLOCATOR_FLAG_ENABLE_CACHED_MDL = 0x00004000
        KSALLOCATOR_FLAG_2D_BUFFER_REQUIRED = 0x00008000
        # old Framing structure
        # allocator options (create)
        class _Union_6(ctypes.Union):
            pass


        _Union_6._fields_ = [
            ('OptionsFlags', ULONG),
            # allocation requirements (query)
            ('RequirementsFlags', ULONG),
        ]
        KSALLOCATOR_FRAMING._Union_6 = _Union_6


        class _Union_7(ctypes.Union):
            pass


        _Union_7._fields_ = [
            ('FileAlignment', ULONG),
            # When KSALLOCATOR_FLAG_2D_BUFFER_REQUIRED is set this field
            # specifies the required 2d pitch for the buffer i.e. the width +
            # stride
            ('FramePitch', LONG),
        ]
        KSALLOCATOR_FRAMING._Union_7 = _Union_7

        KSALLOCATOR_FRAMING._anonymous_ = (
            '_Union_6',
            '_Union_7',
        )

        _TEMP_KSALLOCATOR_FRAMING = [
            ('_Union_6', KSALLOCATOR_FRAMING._Union_6),
        ]
        if defined(_NTDDK_):
            _TEMP_KSALLOCATOR_FRAMING += [
                ('PoolType', POOL_TYPE),
            ]
        else: #  not _NTDDK_
            _TEMP_KSALLOCATOR_FRAMING += [
                ('PoolType', ULONG),
            ]
        # END IF   not _NTDDK_


        _TEMP_KSALLOCATOR_FRAMING += [
            # total number of allowable outstanding frames
            ('Frames', ULONG),
            # total size of frame
            ('FrameSize', ULONG),
            ('_Union_7', KSALLOCATOR_FRAMING._Union_7),
            ('Reserved', ULONG),
        ]
        KSALLOCATOR_FRAMING._fields_ = _TEMP_KSALLOCATOR_FRAMING
        if defined(_NTDDK_):
            # PVOID
            # (*PFNKSDEFAULTALLOCATE)(
            # _In_ PVOID Context
            # );
            PFNKSDEFAULTALLOCATE = CALLBACK(
                PVOID,
                PVOID,
            )


            # VOID
            # (*PFNKSDEFAULTFREE)(
            # _In_ PVOID Context,
            # _In_ PVOID Buffer
            # );
            PFNKSDEFAULTFREE = CALLBACK(
                VOID,
                PVOID,
                PVOID,
            )


            # NTSTATUS
            # (*PFNKSINITIALIZEALLOCATOR)(
            # _In_ PVOID InitialContext,
            # _In_ PKSALLOCATOR_FRAMING AllocatorFraming,
            # _Outptr_ PVOID* Context
            # );
            PFNKSINITIALIZEALLOCATOR = CALLBACK(
                NTSTATUS,
                PVOID,
                PKSALLOCATOR_FRAMING,
                POINTER(PVOID),
            )


            # VOID
            # (*PFNKSDELETEALLOCATOR)(
            # _In_ PVOID Context
            # );
            PFNKSDELETEALLOCATOR = CALLBACK(
                VOID,
                PVOID,
            )


        # END IF   not _NTDDK_


        # new Framing structure, eventually will replace KSALLOCATOR_FRAMING.
        KS_FRAMING_RANGE._fields_ = [
            ('MinFrameSize', ULONG),
            ('MaxFrameSize', ULONG),
            ('Stepping', ULONG),
        ]

        KS_FRAMING_RANGE_WEIGHTED._fields_ = [
            ('Range', KS_FRAMING_RANGE),
            ('InPlaceWeight', ULONG),
            ('NotInPlaceWeight', ULONG),
        ]

        # compression/expansion ratio
        KS_COMPRESSION._fields_ = [
            ('RatioNumerator', ULONG),
            ('RatioDenominator', ULONG),
            ('RatioConstantMargin', ULONG),
        ]


        # Memory Types and Buses are repeated in each entry.
        # Easiest to use but takes a little more memory than the varsize
        # layout Pin\Memories\Buses\Ranges.
        class _Union_8(ctypes.Union):
            pass


        _Union_8._fields_ = [
            ('FileAlignment', ULONG),
            # When KSALLOCATOR_FLAG_2D_BUFFER_REQUIRED is set this field
            # specifies the required 2d pitch for the buffer i.e. the width +
            # stride
            ('FramePitch', LONG),
        ]
        KS_FRAMING_ITEM._Union_8 = _Union_8

        KS_FRAMING_ITEM._anonymous_ = (
            '_Union_8',
        )

        KS_FRAMING_ITEM._fields_ = [
            ('MemoryType', GUID),
            ('BusType', GUID),
            ('MemoryFlags', ULONG),
            ('BusFlags', ULONG),
            ('Flags', ULONG),
            # total number of allowable outstanding frames
            ('Frames', ULONG),
            ('_Union_8', KS_FRAMING_ITEM._Union_8),
            # this memory type Weight pin-wide
            ('MemoryTypeWeight', ULONG),
            ('PhysicalRange', KS_FRAMING_RANGE),
            ('FramingRange', KS_FRAMING_RANGE_WEIGHTED),
        ]

        # count of FramingItem-s below.
        KSALLOCATOR_FRAMING_EX._fields_ = [
            ('CountItems', ULONG),
            ('PinFlags', ULONG),
            ('OutputCompression', KS_COMPRESSION),
            # this pin framing's Weight graph-wide
            ('PinWeight', ULONG),
            ('FramingItem', KS_FRAMING_ITEM * 1),
        ]


        # define memory type GUIDs
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
            0x02
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
            0x02
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
            0x02
        )
        KSMEMORY_TYPE_KERNEL_PAGED = DEFINE_GUIDSTRUCT(
            "d833f8f8-7894-11d1-b069-00a0c9062802"
        )
        KSMEMORY_TYPE_KERNEL_PAGED = (
            DEFINE_GUIDNAMED(KSMEMORY_TYPE_KERNEL_PAGED)
        )
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
            0x02
        )
        KSMEMORY_TYPE_KERNEL_NONPAGED = DEFINE_GUIDSTRUCT(
            "4a6d5fc4-7895-11d1-b069-00a0c9062802"
        )
        KSMEMORY_TYPE_KERNEL_NONPAGED = (
            DEFINE_GUIDNAMED(KSMEMORY_TYPE_KERNEL_NONPAGED)
        )

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
            0x02
        )
        KSMEMORY_TYPE_DEVICE_UNKNOWN = DEFINE_GUIDSTRUCT(
            "091bb639-603f-11d1-b067-00a0c9062802"
        )
        KSMEMORY_TYPE_DEVICE_UNKNOWN = (
            DEFINE_GUIDNAMED(KSMEMORY_TYPE_DEVICE_UNKNOWN)
        )


        # Helper framing macros.
        def DECLARE_SIMPLE_FRAMING_EX(FramingExName, MemoryType, Flags, Frames, Alignment, MinFrameSize, MaxFrameSize):
            return KSALLOCATOR_FRAMING_EX(
                [
                    1,
                    0,
                    [1, 1, 0],
                    0,
                    [
                        [
                            MemoryType,
                            STATIC_KS_TYPE_DONT_CARE,
                            0,
                            0,
                            Flags,
                            Frames,
                            Alignment,
                            0,
                            [0, -1, 1],
                            [[MinFrameSize, MaxFrameSize, 1], 0, 0]
                        ]
                    ]
                ]
            )


        def SetDefaultKsCompression(KsCompressionPointer):
            KsCompressionPointer.RatioNumerator = 1
            KsCompressionPointer.RatioDenominator = 1
            KsCompressionPointer.RatioConstantMargin = 0


        def SetDontCareKsFramingRange(KsFramingRangePointer):
            KsFramingRangePointer.MinFrameSize = 0
            KsFramingRangePointer.MaxFrameSize = -1
            KsFramingRangePointer.Stepping = 1


        def SetKsFramingRange(KsFramingRangePointer, P_MinFrameSize, P_MaxFrameSize):
            KsFramingRangePointer.MinFrameSize = P_MinFrameSize
            KsFramingRangePointer.MaxFrameSize = P_MaxFrameSize
            KsFramingRangePointer.Stepping = 1


        def SetKsFramingRangeWeighted(KsFramingRangeWeightedPointer, P_MinFrameSize, P_MaxFrameSize):
            KsFramingRange = POINTER(KS_FRAMING_RANGE)(ctypes.byref(KsFramingRangeWeightedPointer.Range))
            SetKsFramingRange(KsFramingRange, P_MinFrameSize, P_MaxFrameSize)
            KsFramingRangeWeightedPointer.InPlaceWeight = 0
            KsFramingRangeWeightedPointer.NotInPlaceWeight = 0


        def INITIALIZE_SIMPLE_FRAMING_EX(FramingExPointer, P_MemoryType, P_Flags, P_Frames, P_Alignment, P_MinFrameSize, P_MaxFrameSize):

            KsCompression = POINTER(KS_COMPRESSION)(ctypes.byref(FramingExPointer.OutputCompression))
            KsFramingRange = POINTER(KS_FRAMING_RANGE)(ctypes.byref(FramingExPointer.FramingItem[0].PhysicalRange))
            KsFramingRangeWeighted = POINTER(KS_FRAMING_RANGE_WEIGHTED)(ctypes.byref(FramingExPointer.FramingItem[0].FramingRange))
            FramingExPointer.CountItems = 1
            FramingExPointer.PinFlags = 0
            SetDefaultKsCompression(KsCompression)
            FramingExPointer.PinWeight = 0
            FramingExPointer.FramingItem[0].MemoryType = P_MemoryType
            FramingExPointer.FramingItem[0].BusType = KS_TYPE_DONT_CARE
            FramingExPointer.FramingItem[0].MemoryFlags = 0
            FramingExPointer.FramingItem[0].BusFlags = 0
            FramingExPointer.FramingItem[0].Flags = P_Flags
            FramingExPointer.FramingItem[0].Frames = P_Frames
            FramingExPointer.FramingItem[0].FileAlignment = P_Alignment
            FramingExPointer.FramingItem[0].MemoryTypeWeight = 0
            SetDontCareKsFramingRange(KsFramingRange)
            SetKsFramingRangeWeighted(KsFramingRangeWeighted, P_MinFrameSize, P_MaxFrameSize)


        # KSEVENTSETID_StreamAllocator: {75D95571-073C-11d0-A161-0020AFD156E4}
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
            0xE4
        )
        KSEVENTSETID_StreamAllocator = DEFINE_GUIDSTRUCT(
            "75d95571-073c-11d0-a161-0020afd156e4"
        )
        KSEVENTSETID_StreamAllocator = (
            DEFINE_GUIDNAMED(KSEVENTSETID_StreamAllocator)
        )


        class KSEVENT_STREAMALLOCATOR(ENUM):
            KSEVENT_STREAMALLOCATOR_INTERNAL_FREEFRAME = 1
            KSEVENT_STREAMALLOCATOR_FREEFRAME = 2

        KSEVENT_STREAMALLOCATOR_INTERNAL_FREEFRAME = KSEVENT_STREAMALLOCATOR.KSEVENT_STREAMALLOCATOR_INTERNAL_FREEFRAME
        KSEVENT_STREAMALLOCATOR_FREEFRAME = KSEVENT_STREAMALLOCATOR.KSEVENT_STREAMALLOCATOR_FREEFRAME
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
            0xE4
        )
        KSMETHODSETID_StreamAllocator = DEFINE_GUIDSTRUCT(
            "cf6e4341-ec87-11cf-a130-0020afd156e4"
        )
        KSMETHODSETID_StreamAllocator = (
            DEFINE_GUIDNAMED(KSMETHODSETID_StreamAllocator)
        )


        class KSMETHOD_STREAMALLOCATOR(ENUM):
            KSMETHOD_STREAMALLOCATOR_ALLOC = 1
            KSMETHOD_STREAMALLOCATOR_FREE = 2

        KSMETHOD_STREAMALLOCATOR_ALLOC = KSMETHOD_STREAMALLOCATOR.KSMETHOD_STREAMALLOCATOR_ALLOC
        KSMETHOD_STREAMALLOCATOR_FREE = KSMETHOD_STREAMALLOCATOR.KSMETHOD_STREAMALLOCATOR_FREE


        def DEFINE_KSMETHOD_ITEM_STREAMALLOCATOR_ALLOC(Handler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_STREAMALLOCATOR_ALLOC,
                KSMETHOD_TYPE_WRITE,
                Handler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(PVOID),
                NULL
            )


        def DEFINE_KSMETHOD_ITEM_STREAMALLOCATOR_FREE(Handler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_STREAMALLOCATOR_FREE,
                KSMETHOD_TYPE_READ,
                Handler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(PVOID),
                NULL
            )


        def DEFINE_KSMETHOD_ALLOCATORSET(AllocatorSet, MethodAlloc, MethodFree):
            DEFINE_KSMETHOD_TABLE(AllocatorSet)
            DEFINE_KSMETHOD_ITEM_STREAMALLOCATOR_ALLOC(MethodAlloc)
            DEFINE_KSMETHOD_ITEM_STREAMALLOCATOR_FREE(MethodFree)


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
            0xE4
        )
        KSPROPSETID_StreamAllocator = DEFINE_GUIDSTRUCT(
            "cf6e4342-ec87-11cf-a130-0020afd156e4"
        )
        KSPROPSETID_StreamAllocator = (
            DEFINE_GUIDNAMED(KSPROPSETID_StreamAllocator)
        )
        if defined(_NTDDK_):
            class KSPROPERTY_STREAMALLOCATOR(ENUM):
                KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE = 1
                KSPROPERTY_STREAMALLOCATOR_STATUS = 2

            KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE = KSPROPERTY_STREAMALLOCATOR.KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE
            KSPROPERTY_STREAMALLOCATOR_STATUS = KSPROPERTY_STREAMALLOCATOR.KSPROPERTY_STREAMALLOCATOR_STATUS


            def DEFINE_KSPROPERTY_ITEM_STREAMALLOCATOR_FUNCTIONTABLE(Handler):
                return DEFINE_KSPROPERTY_ITEM(
                    KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE,
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
                    KSPROPERTY_STREAMALLOCATOR_STATUS,
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


            def DEFINE_KSPROPERTY_ALLOCATORSET(AllocatorSet, PropFunctionTable, PropStatus):
                DEFINE_KSPROPERTY_TABLE(AllocatorSet)
                DEFINE_KSPROPERTY_ITEM_STREAMALLOCATOR_STATUS(PropStatus),
                DEFINE_KSPROPERTY_ITEM_STREAMALLOCATOR_FUNCTIONTABLE(PropFunctionTable)


            # NTSTATUS
            # (*PFNALLOCATOR_ALLOCATEFRAME)(
            # _In_ PFILE_OBJECT FileObject,
            # _Outptr_ PVOID *Frame
            # );
            PFNALLOCATOR_ALLOCATEFRAME = CALLBACK(
                NTSTATUS,
                PFILE_OBJECT,
                POINTER(PVOID),
            )
            # VOID
            # (*PFNALLOCATOR_FREEFRAME)(
            # _In_ PFILE_OBJECT FileObject,
            # _In_ PVOID Frame
            # );
            PFNALLOCATOR_FREEFRAME = CALLBACK(
                VOID,
                PFILE_OBJECT,
                PVOID,
            )
            KSSTREAMALLOCATOR_FUNCTIONTABLE._fields_ = [
                ('AllocateFrame', PFNALLOCATOR_ALLOCATEFRAME),
                ('FreeFrame', PFNALLOCATOR_FREEFRAME),
            ]
        # END IF   defined(_NTDDK_)

        KSSTREAMALLOCATOR_STATUS._fields_ = [
            ('Framing', KSALLOCATOR_FRAMING),
            ('AllocatedFrames', ULONG),
            ('Reserved', ULONG),
        ]
        KSSTREAMALLOCATOR_STATUS_EX._fields_ = [
            ('Framing', KSALLOCATOR_FRAMING_EX),
            ('AllocatedFrames', ULONG),
            ('Reserved', ULONG),
        ]
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
        KSTIME._fields_ = [
            ('Time', LONGLONG),
            ('Numerator', ULONG),
            ('Denominator', ULONG),
        ]
        _TEMP_KSSTREAM_HEADER = [
            ('Size', ULONG),
            ('TypeSpecificFlags', ULONG),
            ('PresentationTime', KSTIME),
            ('Duration', LONGLONG),
            ('FrameExtent', ULONG),
            ('DataUsed', ULONG),
            ('Data', PVOID),
            ('OptionsFlags', ULONG),
        ]
        if _WIN64:
            _TEMP_KSSTREAM_HEADER += [
                ('Reserved', ULONG),
            ]
        # END IF


        KSSTREAM_HEADER._fields_ = _TEMP_KSSTREAM_HEADER

        KSSTREAM_METADATA_INFO._fields_ = [
            ('BufferSize', ULONG),
            ('UsedSize', ULONG),
            # Metadata buffer passed down by user mode (mapped to SystemVa)
            ('Data', PVOID),
            # Metadata buffer that driver will fill metadata to
            ('SystemVa', PVOID),
            ('Flags', ULONG),
            ('Reserved', ULONG),
        ]

        KSSTREAM_UVC_METADATATYPE_TIMESTAMP._fields_ = [
            ('PresentationTimeStamp', ULONG),
            ('SourceClockReference', ULONG),
            ('Counter', USHORT, 11),
            ('Reserved', USHORT, 5),
            ('SCRToken', USHORT),
            ('Reserved0', USHORT),
            ('Reserved1', ULONG),
        ]

        KSSTREAM_UVC_METADATA._fields_ = [
            ('StartOfFrameTimestamp', KSSTREAM_UVC_METADATATYPE_TIMESTAMP),
            ('EndOfFrameTimestamp', KSSTREAM_UVC_METADATATYPE_TIMESTAMP),
        ]

        # Additional space for UVC Attribute data to be stamped in the payload
        # by the
        # Inbox UVC driver
        KSSTREAM_UVC_SECURE_ATTRIBUTE_SIZE = 0x2000


        class KSPIN_MDL_CACHING_EVENT(ENUM):
            KSPIN_MDL_CACHING_NOTIFY_CLEANUP = 1
            KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT = 2
            KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT = 3
            KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE = 4

        KSPIN_MDL_CACHING_NOTIFY_CLEANUP = KSPIN_MDL_CACHING_EVENT.KSPIN_MDL_CACHING_NOTIFY_CLEANUP
        KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT = KSPIN_MDL_CACHING_EVENT.KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT
        KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT = KSPIN_MDL_CACHING_EVENT.KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT
        KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE = KSPIN_MDL_CACHING_EVENT.KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE

        KSPIN_MDL_CACHING_NOTIFICATION._fields_ = [
            ('Event', KSPIN_MDL_CACHING_EVENT),
            ('Buffer', PVOID),
        ]

        KSPIN_MDL_CACHING_NOTIFICATION32._fields_ = [
            ('Event', KSPIN_MDL_CACHING_EVENT),
            ('Buffer', ULONG),
        ]
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
            0x8A
        )
        KSPROPSETID_StreamInterface = DEFINE_GUIDSTRUCT(
            "1fdd8ee1-9cd3-11d0-82aa-0000f822fe8a"
        )
        KSPROPSETID_StreamInterface = (
            DEFINE_GUIDNAMED(KSPROPSETID_StreamInterface)
        )


        class KSPROPERTY_STREAMINTERFACE(ENUM):
            KSPROPERTY_STREAMINTERFACE_HEADERSIZE = 1

        KSPROPERTY_STREAMINTERFACE_HEADERSIZE = KSPROPERTY_STREAMINTERFACE.KSPROPERTY_STREAMINTERFACE_HEADERSIZE


        def DEFINE_KSPROPERTY_ITEM_STREAMINTERFACE_HEADERSIZE(GetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_STREAMINTERFACE_HEADERSIZE,
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


        def DEFINE_KSPROPERTY_STREAMINTERFACESET(StreamInterfaceSet, HeaderSizeHandler):
            DEFINE_KSPROPERTY_TABLE(StreamInterfaceSet)
            DEFINE_KSPROPERTY_ITEM_STREAMINTERFACE_HEADERSIZE(HeaderSizeHandler)


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
            0xE4
        )
        KSPROPSETID_Stream = DEFINE_GUIDSTRUCT(
            "65aaba60-98ae-11cf-a10d-0020afd156e4"
        )
        KSPROPSETID_Stream = DEFINE_GUIDNAMED(KSPROPSETID_Stream)


        class KSPROPERTY_STREAM(ENUM):
            KSPROPERTY_STREAM_ALLOCATOR = 1
            KSPROPERTY_STREAM_QUALITY = 2
            KSPROPERTY_STREAM_DEGRADATION = 3
            KSPROPERTY_STREAM_MASTERCLOCK = 4
            KSPROPERTY_STREAM_TIMEFORMAT = 5
            KSPROPERTY_STREAM_PRESENTATIONTIME = 6
            KSPROPERTY_STREAM_PRESENTATIONEXTENT = 7
            KSPROPERTY_STREAM_FRAMETIME = 8
            KSPROPERTY_STREAM_RATECAPABILITY = 9
            KSPROPERTY_STREAM_RATE = 10
            KSPROPERTY_STREAM_PIPE_ID = 11

        KSPROPERTY_STREAM_ALLOCATOR = KSPROPERTY_STREAM.KSPROPERTY_STREAM_ALLOCATOR
        KSPROPERTY_STREAM_QUALITY = KSPROPERTY_STREAM.KSPROPERTY_STREAM_QUALITY
        KSPROPERTY_STREAM_DEGRADATION = KSPROPERTY_STREAM.KSPROPERTY_STREAM_DEGRADATION
        KSPROPERTY_STREAM_MASTERCLOCK = KSPROPERTY_STREAM.KSPROPERTY_STREAM_MASTERCLOCK
        KSPROPERTY_STREAM_TIMEFORMAT = KSPROPERTY_STREAM.KSPROPERTY_STREAM_TIMEFORMAT
        KSPROPERTY_STREAM_PRESENTATIONTIME = KSPROPERTY_STREAM.KSPROPERTY_STREAM_PRESENTATIONTIME
        KSPROPERTY_STREAM_PRESENTATIONEXTENT = KSPROPERTY_STREAM.KSPROPERTY_STREAM_PRESENTATIONEXTENT
        KSPROPERTY_STREAM_FRAMETIME = KSPROPERTY_STREAM.KSPROPERTY_STREAM_FRAMETIME
        KSPROPERTY_STREAM_RATECAPABILITY = KSPROPERTY_STREAM.KSPROPERTY_STREAM_RATECAPABILITY
        KSPROPERTY_STREAM_RATE = KSPROPERTY_STREAM.KSPROPERTY_STREAM_RATE
        KSPROPERTY_STREAM_PIPE_ID = KSPROPERTY_STREAM.KSPROPERTY_STREAM_PIPE_ID


        def DEFINE_KSPROPERTY_ITEM_STREAM_ALLOCATOR(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_STREAM_ALLOCATOR,
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
                KSPROPERTY_STREAM_QUALITY,
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
                KSPROPERTY_STREAM_DEGRADATION,
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
                KSPROPERTY_STREAM_MASTERCLOCK,
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
                KSPROPERTY_STREAM_TIMEFORMAT,
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
                KSPROPERTY_STREAM_PRESENTATIONTIME,
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
                KSPROPERTY_STREAM_PRESENTATIONEXTENT,
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
                KSPROPERTY_STREAM_FRAMETIME,
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
                KSPROPERTY_STREAM_RATECAPABILITY,
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
                KSPROPERTY_STREAM_RATE,
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
                KSPROPERTY_STREAM_PIPE_ID,
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

        KSPROPERTY_ALLOCATOR_CLEANUP_CACHEDMDLPAGES = KSPPROPERTY_ALLOCATOR_MDLCACHING.KSPROPERTY_ALLOCATOR_CLEANUP_CACHEDMDLPAGES


        def DEFINE_KSPROPERTY_ITEM_CONNECTION_MDLCACHING(SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_ALLOCATOR_CLEANUP_CACHEDMDLPAGES,
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
            0x16
        )
        KSPROPSETID_PinMDLCacheClearProp = DEFINE_GUIDSTRUCT(
            "BD718A7B-97FC-40C7-88CE-D3FF06F55B16"
        )
        KSPROPSETID_PinMDLCacheClearProp = (
            DEFINE_GUIDNAMED(KSPROPSETID_PinMDLCacheClearProp)
        )
        KSQUALITY_MANAGER._fields_ = [
            ('QualityManager', HANDLE),
            ('Context', PVOID),
        ]
        KSFRAMETIME._fields_ = [
            ('Duration', LONGLONG),
            ('FrameFlags', ULONG),
            ('Reserved', ULONG),
        ]
        KSFRAMETIME_VARIABLESIZE = 0x00000001
        KSRATE._fields_ = [
            ('PresentationStart', LONGLONG),
            ('Duration', LONGLONG),
            ('Interface', KSPIN_INTERFACE),
            ('Rate', LONG),
            ('Flags', ULONG),
        ]
        KSRATE_NOPRESENTATIONSTART = 0x00000001
        KSRATE_NOPRESENTATIONDURATION = 0x00000002
        KSRATE_CAPABILITY._fields_ = [
            ('Property', KSPROPERTY),
            ('Rate', KSRATE),
        ]
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
            0x00
        )
        KSPROPSETID_Clock = DEFINE_GUIDSTRUCT(
            "DF12A4C0-AC17-11CF-A5D6-28DB04C10000"
        )
        KSPROPSETID_Clock = DEFINE_GUIDNAMED(KSPROPSETID_Clock)
        # Performs a x*y/z operation on 64 bit quantities by splitting the
        # operation. The equation
        # is simplified with respect to adding in the remainder for the upper
        # 32 bits.
        # (xh * 10000000 / Frequency) * 2^32 +
        # ((((xh * 10000000) % Frequency) * 2^32 + (xl * 10000000)) / Frequency)
        #
        NANOSECONDS = 10000000
        def KSCONVERT_PERFORMANCE_TIME(Frequency, PerformanceTime):
            return (
                ((PerformanceTime.HighPart * NANOSECONDS / Frequency) << 32) +
                (
                    ((((PerformanceTime.HighPart * NANOSECONDS) % Frequency) << 32) +
                    (PerformanceTime.LowPart * NANOSECONDS)) / Frequency
                )
            )


        KSCLOCK_CREATE._fields_ = [
            ('CreateFlags', ULONG),
        ]
        KSCORRELATED_TIME._fields_ = [
            ('Time', LONGLONG),
            ('SystemTime', LONGLONG),
        ]
        KSRESOLUTION._fields_ = [
            ('Granularity', LONGLONG),
            ('Error', LONGLONG),
        ]


        class KSPROPERTY_CLOCK(ENUM):
            KSPROPERTY_CLOCK_TIME = 1
            KSPROPERTY_CLOCK_PHYSICALTIME = 2
            KSPROPERTY_CLOCK_CORRELATEDTIME = 3
            KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME = 4
            KSPROPERTY_CLOCK_RESOLUTION = 5
            KSPROPERTY_CLOCK_STATE = 6
            if defined(_NTDDK_):
                KSPROPERTY_CLOCK_FUNCTIONTABLE = 7
            # END IF

        KSPROPERTY_CLOCK_TIME = KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_TIME
        KSPROPERTY_CLOCK_PHYSICALTIME = KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_PHYSICALTIME
        KSPROPERTY_CLOCK_CORRELATEDTIME = KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_CORRELATEDTIME
        KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME = KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME
        KSPROPERTY_CLOCK_RESOLUTION = KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_RESOLUTION
        KSPROPERTY_CLOCK_STATE = KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_STATE
        if defined(_NTDDK_):
            KSPROPERTY_CLOCK_FUNCTIONTABLE = KSPROPERTY_CLOCK.KSPROPERTY_CLOCK_FUNCTIONTABLE
        # END IF

        if defined(_NTDDK_):
            # LONGLONG
            # (FASTCALL *PFNKSCLOCK_GETTIME)(
            # _In_ PFILE_OBJECT FileObject
            # );
            PFNKSCLOCK_GETTIME = FASTCALL(
                LONGLONG,
                PFILE_OBJECT,
            )


            # LONGLONG
            # (FASTCALL *PFNKSCLOCK_CORRELATEDTIME)(
            # _In_ PFILE_OBJECT FileObject,
            # _Out_ PLONGLONG SystemTime);
            PFNKSCLOCK_CORRELATEDTIME = FASTCALL(
                LONGLONG,
                PFILE_OBJECT,
                PLONGLONG,
            )


            KSCLOCK_FUNCTIONTABLE._fields_ = [
                ('GetTime', PFNKSCLOCK_GETTIME),
                ('GetPhysicalTime', PFNKSCLOCK_GETTIME),
                ('GetCorrelatedTime', PFNKSCLOCK_CORRELATEDTIME),
                ('GetCorrelatedPhysicalTime', PFNKSCLOCK_CORRELATEDTIME),
            ]
            if NTDDI_VERSION >= NTDDI_WINXP:
                # BOOLEAN
                # (*PFNKSSETTIMER)(
                # _In_ PVOID Context,
                # _In_ PKTIMER Timer,
                # _In_ LARGE_INTEGER DueTime,
                # _In_ PKDPC Dpc
                # );
                PFNKSSETTIMER = CALLBACK(
                    BOOLEAN,
                    PVOID,
                    PKTIMER,
                    LARGE_INTEGER,
                    PKDPC,
                )


                # BOOLEAN
                # (*PFNKSCANCELTIMER)(
                # _In_ PVOID Context,
                # _In_ PKTIMER Timer
                # );
                PFNKSCANCELTIMER = CALLBACK(
                    BOOLEAN,
                    PVOID,
                    PKTIMER,
                )


                # LONGLONG
                # (FASTCALL *PFNKSCORRELATEDTIME)(
                # _In_ PVOID Context,
                # _Out_  PLONGLONG SystemTime);
                PFNKSCORRELATEDTIME = FASTCALL(
                    LONGLONG,
                    PVOID,
                    PLONGLONG,
                )


            # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

            PKSDEFAULTCLOCK = PVOID

            def DEFINE_KSPROPERTY_ITEM_CLOCK_TIME(Handler):
                return DEFINE_KSPROPERTY_ITEM(
                    KSPROPERTY_CLOCK_TIME,
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
                    KSPROPERTY_CLOCK_PHYSICALTIME,
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
                    KSPROPERTY_CLOCK_CORRELATEDTIME,
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
                    KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME,
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
                    KSPROPERTY_CLOCK_RESOLUTION,
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
                    KSPROPERTY_CLOCK_STATE,
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


            def DEFINE_KSPROPERTY_ITEM_CLOCK_FUNCTIONTABLE(Handler):
                return DEFINE_KSPROPERTY_ITEM(
                    KSPROPERTY_CLOCK_FUNCTIONTABLE,
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


            def DEFINE_KSPROPERTY_CLOCKSET(
                ClockSet,
                PropTime,
                PropPhysicalTime,
                PropCorrelatedTime,
                PropCorrelatedPhysicalTime,
                PropResolution,
                PropState,
                PropFunctionTable
            ):
                DEFINE_KSPROPERTY_TABLE(ClockSet)
                DEFINE_KSPROPERTY_ITEM_CLOCK_TIME(PropTime)
                DEFINE_KSPROPERTY_ITEM_CLOCK_PHYSICALTIME(PropPhysicalTime)
                DEFINE_KSPROPERTY_ITEM_CLOCK_CORRELATEDTIME(PropCorrelatedTime)
                DEFINE_KSPROPERTY_ITEM_CLOCK_CORRELATEDPHYSICALTIME(
                    PropCorrelatedPhysicalTime
                )
                DEFINE_KSPROPERTY_ITEM_CLOCK_RESOLUTION(PropResolution)
                DEFINE_KSPROPERTY_ITEM_CLOCK_STATE(PropState)
                DEFINE_KSPROPERTY_ITEM_CLOCK_FUNCTIONTABLE(PropFunctionTable)


        # END IF   defined(_NTDDK_)

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
            0x00
        )
        KSEVENTSETID_Clock = DEFINE_GUIDSTRUCT(
            "364D8E20-62C7-11CF-A5D6-28DB04C10000"
        )
        KSEVENTSETID_Clock = DEFINE_GUIDNAMED(KSEVENTSETID_Clock)


        class KSEVENT_CLOCK_POSITION(ENUM):
            KSEVENT_CLOCK_INTERVAL_MARK = 1
            KSEVENT_CLOCK_POSITION_MARK = 2

        KSEVENT_CLOCK_INTERVAL_MARK = KSEVENT_CLOCK_POSITION.KSEVENT_CLOCK_INTERVAL_MARK
        KSEVENT_CLOCK_POSITION_MARK = KSEVENT_CLOCK_POSITION.KSEVENT_CLOCK_POSITION_MARK
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
            0x00
        )
        KSEVENTSETID_Connection = DEFINE_GUIDSTRUCT(
            "7f4bcbe0-9ea5-11cf-a5d6-28db04c10000"
        )
        KSEVENTSETID_Connection = DEFINE_GUIDNAMED(KSEVENTSETID_Connection)


        class KSEVENT_CONNECTION(ENUM):
            KSEVENT_CONNECTION_POSITIONUPDATE = 1
            KSEVENT_CONNECTION_DATADISCONTINUITY = 2
            KSEVENT_CONNECTION_TIMEDISCONTINUITY = 3
            KSEVENT_CONNECTION_PRIORITY = 4
            KSEVENT_CONNECTION_ENDOFSTREAM = 5

        KSEVENT_CONNECTION_POSITIONUPDATE = KSEVENT_CONNECTION.KSEVENT_CONNECTION_POSITIONUPDATE
        KSEVENT_CONNECTION_DATADISCONTINUITY = KSEVENT_CONNECTION.KSEVENT_CONNECTION_DATADISCONTINUITY
        KSEVENT_CONNECTION_TIMEDISCONTINUITY = KSEVENT_CONNECTION.KSEVENT_CONNECTION_TIMEDISCONTINUITY
        KSEVENT_CONNECTION_PRIORITY = KSEVENT_CONNECTION.KSEVENT_CONNECTION_PRIORITY
        KSEVENT_CONNECTION_ENDOFSTREAM = KSEVENT_CONNECTION.KSEVENT_CONNECTION_ENDOFSTREAM

        KSQUALITY._fields_ = [
            ('Context', PVOID),
            ('Proportion', ULONG),
            ('DeltaTime', LONGLONG),
        ]

        KSERROR._fields_ = [
            ('Context', PVOID),
            ('Status', ULONG),
        ]


        class KSDEVICE_THERMAL_STATE(ENUM):
            KSDEVICE_THERMAL_STATE_LOW = 1
            KSDEVICE_THERMAL_STATE_HIGH = 2

        KSDEVICE_THERMAL_STATE_LOW = KSDEVICE_THERMAL_STATE.KSDEVICE_THERMAL_STATE_LOW
        KSDEVICE_THERMAL_STATE_HIGH = KSDEVICE_THERMAL_STATE.KSDEVICE_THERMAL_STATE_HIGH
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
            0x3F
        )
        KSEVENTSETID_Device = DEFINE_GUIDSTRUCT(
            "288296EC-9F94-41b4-A153-AA31AEECB33F"
        )
        KSEVENTSETID_Device = DEFINE_GUIDNAMED(KSEVENTSETID_Device)


        class KSEVENT_DEVICE(ENUM):
            KSEVENT_DEVICE_LOST = 1
            KSEVENT_DEVICE_PREEMPTED = 2
            KSEVENT_DEVICE_THERMAL_HIGH = 3
            KSEVENT_DEVICE_THERMAL_LOW = 4

        KSEVENT_DEVICE_LOST = KSEVENT_DEVICE.KSEVENT_DEVICE_LOST
        KSEVENT_DEVICE_PREEMPTED = KSEVENT_DEVICE.KSEVENT_DEVICE_PREEMPTED
        KSEVENT_DEVICE_THERMAL_HIGH = KSEVENT_DEVICE.KSEVENT_DEVICE_THERMAL_HIGH
        KSEVENT_DEVICE_THERMAL_LOW = KSEVENT_DEVICE.KSEVENT_DEVICE_THERMAL_LOW

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
            0x00
        )
        KSDEGRADESETID_Standard = DEFINE_GUIDSTRUCT(
            "9F564180-704C-11D0-A5D6-28DB04C10000"
        )
        KSDEGRADESETID_Standard = DEFINE_GUIDNAMED(KSDEGRADESETID_Standard)


        class KSDEGRADE_STANDARD(ENUM):
            KSDEGRADE_STANDARD_SAMPLE = 1
            KSDEGRADE_STANDARD_QUALITY = 2
            KSDEGRADE_STANDARD_COMPUTATION = 3
            KSDEGRADE_STANDARD_SKIP = 4

        KSDEGRADE_STANDARD_SAMPLE = KSDEGRADE_STANDARD.KSDEGRADE_STANDARD_SAMPLE
        KSDEGRADE_STANDARD_QUALITY = KSDEGRADE_STANDARD.KSDEGRADE_STANDARD_QUALITY
        KSDEGRADE_STANDARD_COMPUTATION = KSDEGRADE_STANDARD.KSDEGRADE_STANDARD_COMPUTATION
        KSDEGRADE_STANDARD_SKIP = KSDEGRADE_STANDARD.KSDEGRADE_STANDARD_SKIP

        if defined(_NTDDK_):
            from pyWinAPI.km.wdm_h import * # NOQA

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

            # NTSTATUS
            # (*PFNKSCONTEXT_DISPATCH)(
            # _In_ PVOID Context,
            # _In_ PIRP Irp
            # );
            PFNKSCONTEXT_DISPATCH = CALLBACK(
                NTSTATUS,
                PVOID,
                PIRP,
            )

            # NTSTATUS
            # (*PFNKSHANDLER)(
            # _In_ PIRP Irp,
            # _In_ PKSIDENTIFIER Request,
            # _Inout_ PVOID Data
            # );
            PFNKSHANDLER = CALLBACK(
                NTSTATUS,
                PIRP,
                PKSIDENTIFIER,
                PVOID,
            )

            # BOOLEAN
            # (*PFNKSFASTHANDLER)(
            # _In_ PFILE_OBJECT FileObject,
            # _In_reads_bytes_(RequestLength) PKSIDENTIFIER Request,
            # _In_ ULONG RequestLength,
            # _Inout_updates_bytes_(DataLength) PVOID Data,
            # _In_ ULONG DataLength,
            # _Out_ PIO_STATUS_BLOCK IoStatus
            # );
            PFNKSFASTHANDLER = CALLBACK(
                BOOLEAN,
                PFILE_OBJECT,
                PKSIDENTIFIER,
                ULONG,
                PVOID,
                ULONG,
                PIO_STATUS_BLOCK,
            )

            # NTSTATUS
            # (*PFNKSALLOCATOR)(
            # _In_ PIRP Irp,
            # _In_ ULONG BufferSize,
            # _In_ BOOLEAN InputOperation
            # );
            PFNKSALLOCATOR = CALLBACK(
                NTSTATUS,
                PIRP,
                ULONG,
                BOOLEAN,
            )

            KSPROPERTY_MEMBERSLIST._fields_ = [
                ('MembersHeader', KSPROPERTY_MEMBERSHEADER),
                ('Members', POINTER(VOID)),
            ]

            KSPROPERTY_VALUES._fields_ = [
                ('PropTypeSet', KSIDENTIFIER),
                ('MembersListCount', ULONG),
                ('MembersList', POINTER(KSPROPERTY_MEMBERSLIST)),
            ]


            def DEFINE_KSPROPERTY_TABLE(tablename):
                return KSPROPERTY_ITEM * 0


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
                    SerializedSize
                )


            class _Union_9(ctypes.Union):
                pass


            _Union_9._fields_ = [
                ('GetPropertyHandler', PFNKSHANDLER),
                ('GetSupported', BOOLEAN),
            ]
            KSPROPERTY_ITEM._Union_9 = _Union_9


            class _Union_10(ctypes.Union):
                pass


            _Union_10._fields_ = [
                ('SetPropertyHandler', PFNKSHANDLER),
                ('SetSupported', BOOLEAN),
            ]
            KSPROPERTY_ITEM._Union_10 = _Union_10

            KSPROPERTY_ITEM._anonymous_ = (
                '_Union_9',
                '_Union_10',
            )

            KSPROPERTY_ITEM._fields_ = [
                ('PropertyId', ULONG),
                ('_Union_9', KSPROPERTY_ITEM._Union_9),
                ('MinProperty', ULONG),
                ('MinData', ULONG),
                ('_Union_10', KSPROPERTY_ITEM._Union_10),
                ('RelationsCount', ULONG),
                ('Relations', POINTER(KSPROPERTY)),
                ('SupportHandler', PFNKSHANDLER),
                ('SerializedSize', ULONG),
            ]


            def DEFINE_KSFASTPROPERTY_ITEM(PropertyId, GetHandler, SetHandler):
                return (
                    PropertyId,
                    PFNKSFASTHANDLER(GetHandler),
                    PFNKSFASTHANDLER(SetHandler),
                    0
                )


            class _Union_11(ctypes.Union):
                pass


            _Union_11._fields_ = [
                ('GetPropertyHandler', PFNKSFASTHANDLER),
                ('GetSupported', BOOLEAN),
            ]
            KSFASTPROPERTY_ITEM._Union_11 = _Union_11


            class _Union_12(ctypes.Union):
                pass


            _Union_12._fields_ = [
                ('SetPropertyHandler', PFNKSFASTHANDLER),
                ('SetSupported', BOOLEAN),
            ]
            KSFASTPROPERTY_ITEM._Union_12 = _Union_12

            KSFASTPROPERTY_ITEM._anonymous_ = (
                '_Union_11',
                '_Union_12',
            )

            KSFASTPROPERTY_ITEM._fields_ = [
                ('PropertyId', ULONG),
                ('_Union_11', KSFASTPROPERTY_ITEM._Union_11),
                ('_Union_12', KSFASTPROPERTY_ITEM._Union_12),
                ('Reserved', ULONG),
            ]


            def DEFINE_KSPROPERTY_SET(Set, PropertiesCount, PropertyItem, FastIoCount, FastIoTable):
                Set, PropertiesCount, PropertyItem, FastIoCount, FastIoTable


            def DEFINE_KSPROPERTY_SET_TABLE(tablename):
                return KSPROPERTY_SET * 0


            KSPROPERTY_SET._fields_ = [
                ('Set', POINTER(GUID)),
                ('PropertiesCount', ULONG),
                ('PropertyItem', POINTER(KSPROPERTY_ITEM)),
                ('FastIoCount', ULONG),
                ('FastIoTable', POINTER(KSFASTPROPERTY_ITEM)),
            ]


            def DEFINE_KSMETHOD_TABLE(tablename):
                return KSMETHOD_ITEM * 0


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


            class _Union_13(ctypes.Union):
                pass


            _Union_13._fields_ = [
                ('MethodHandler', PFNKSHANDLER),
                ('MethodSupported', BOOLEAN),
            ]
            KSMETHOD_ITEM._Union_13 = _Union_13

            KSMETHOD_ITEM._anonymous_ = (
                '_Union_13',
            )

            KSMETHOD_ITEM._fields_ = [
                ('MethodId', ULONG),
                ('_Union_13', KSMETHOD_ITEM._Union_13),
                ('MinMethod', ULONG),
                ('MinData', ULONG),
                ('SupportHandler', PFNKSHANDLER),
                ('Flags', ULONG),
            ]


            def DEFINE_KSFASTMETHOD_ITEM(MethodId, MethodHandler):
                return MethodId, PFNKSFASTHANDLER(MethodHandler)


            class _Union_14(ctypes.Union):
                pass


            _Union_14._fields_ = [
                ('MethodHandler', PFNKSFASTHANDLER),
                ('MethodSupported', BOOLEAN),
            ]
            KSFASTMETHOD_ITEM._Union_14 = _Union_14

            KSFASTMETHOD_ITEM._anonymous_ = (
                '_Union_14',
            )

            KSFASTMETHOD_ITEM._fields_ = [
                ('MethodId', ULONG),
                ('_Union_14', KSFASTMETHOD_ITEM._Union_14),
            ]


            def DEFINE_KSMETHOD_SET(
                Set,
                MethodsCount,
                MethodItem,
                FastIoCount,
                FastIoTable
            ):
                return Set, MethodsCount, MethodItem, FastIoCount, FastIoTable


            def DEFINE_KSMETHOD_SET_TABLE(tablename):
                return KSMETHOD_SET * 0


            KSMETHOD_SET._fields_ = [
                ('Set', POINTER(GUID)),
                ('MethodsCount', ULONG),
                ('MethodItem', POINTER(KSMETHOD_ITEM)),
                ('FastIoCount', ULONG),
            ]

            KSEVENT_ENTRY = _KSEVENT_ENTRY
            PKSEVENT_ENTRY = POINTER(_KSEVENT_ENTRY)

            # NTSTATUS
            # (*PFNKSADDEVENT)(
            # _In_ PIRP Irp,
            # _In_ PKSEVENTDATA EventData,
            # _In_ struct _KSEVENT_ENTRY* EventEntry
            # );
            PFNKSADDEVENT = CALLBACK(
                NTSTATUS,
                PIRP,
                PKSEVENTDATA,
                POINTER(_KSEVENT_ENTRY),
            )


            # VOID
            # (*PFNKSREMOVEEVENT)(
            # _In_ PFILE_OBJECT FileObject,
            # _In_ struct _KSEVENT_ENTRY* EventEntry
            # );
            PFNKSREMOVEEVENT = CALLBACK(
                VOID,
                PFILE_OBJECT,
                POINTER(_KSEVENT_ENTRY),
            )


            def DEFINE_KSEVENT_TABLE(tablename):
                return KSEVENT_ITEM * 0


            def DEFINE_KSEVENT_ITEM(
                EventId,
                DataInput,
                ExtraEntryData,
                AddHandler,
                RemoveHandler,
                SupportHandler
            ):
                return (
                    EventId,
                    DataInput,
                    ExtraEntryData,
                    AddHandler,
                    RemoveHandler,
                    SupportHandler
                )


            KSEVENT_ITEM._fields_ = [
                ('EventId', ULONG),
                ('DataInput', ULONG),
                ('ExtraEntryData', ULONG),
                ('AddHandler', PFNKSADDEVENT),
                ('RemoveHandler', PFNKSREMOVEEVENT),
                ('SupportHandler', PFNKSHANDLER),
            ]


            def DEFINE_KSEVENT_SET(Set, EventsCount, EventItem):
                return Set, EventsCount, EventItem


            def DEFINE_KSEVENT_SET_TABLE(tablename):
                return KSEVENT_SET * 0


            KSEVENT_SET._fields_ = [
                ('Set', POINTER(GUID)),
                ('EventsCount', ULONG),
                ('EventItem', POINTER(KSEVENT_ITEM)),
            ]

            KSDPC_ITEM._fields_ = [
                ('Dpc', KDPC),
                ('ReferenceCount', ULONG),
                ('AccessLock', KSPIN_LOCK),
            ]

            KSBUFFER_ITEM._fields_ = [
                ('DpcItem', KSDPC_ITEM),
                ('BufferList', LIST_ENTRY),
            ]
            KSEVENT_ENTRY_DELETED = 1
            KSEVENT_ENTRY_ONESHOT = 2
            KSEVENT_ENTRY_BUFFERED = 4


            class _Union_15(ctypes.Union):
                pass


            _Union_15._fields_ = [
                ('DpcItem', PKSDPC_ITEM),
                ('BufferItem', PKSBUFFER_ITEM),
            ]
            _KSEVENT_ENTRY._Union_15 = _Union_15

            _KSEVENT_ENTRY._anonymous_ = (
                '_Union_15',
            )

            _KSEVENT_ENTRY._fields_ = [
                ('ListEntry', LIST_ENTRY),
                ('Object', PVOID),
                ('_Union_15', _KSEVENT_ENTRY._Union_15),
                ('EventData', PKSEVENTDATA),
                ('NotificationType', ULONG),
                ('EventSet', POINTER(KSEVENT_SET)),
                ('EventItem', POINTER(KSEVENT_ITEM)),
                ('FileObject', PFILE_OBJECT),
                ('SemaphoreAdjustment', ULONG),
                ('Reserved', ULONG),
                ('Flags', ULONG),
            ]


            class KSEVENTS_LOCKTYPE(ENUM):
                KSEVENTS_NONE = 1
                KSEVENTS_SPINLOCK = 2
                KSEVENTS_MUTEX = 3
                KSEVENTS_FMUTEX = 4
                KSEVENTS_FMUTEXUNSAFE = 5
                KSEVENTS_INTERRUPT = 6
                KSEVENTS_ERESOURCE = 7

            KSEVENTS_NONE = KSEVENTS_LOCKTYPE.KSEVENTS_NONE
            KSEVENTS_SPINLOCK = KSEVENTS_LOCKTYPE.KSEVENTS_SPINLOCK
            KSEVENTS_MUTEX = KSEVENTS_LOCKTYPE.KSEVENTS_MUTEX
            KSEVENTS_FMUTEX = KSEVENTS_LOCKTYPE.KSEVENTS_FMUTEX
            KSEVENTS_FMUTEXUNSAFE = KSEVENTS_LOCKTYPE.KSEVENTS_FMUTEXUNSAFE
            KSEVENTS_INTERRUPT = KSEVENTS_LOCKTYPE.KSEVENTS_INTERRUPT
            KSEVENTS_ERESOURCE = KSEVENTS_LOCKTYPE.KSEVENTS_ERESOURCE
            KSDISPATCH_FASTIO = 0x80000000


            KSOBJECT_CREATE_ITEM._fields_ = [
                ('Create', PDRIVER_DISPATCH),
                ('Context', PVOID),
                ('ObjectClass', UNICODE_STRING),
                ('SecurityDescriptor', PSECURITY_DESCRIPTOR),
                ('Flags', ULONG),
            ]

            # VOID
            # (*PFNKSITEMFREECALLBACK)(
            # _In_ PKSOBJECT_CREATE_ITEM CreateItem
            # );
            PFNKSITEMFREECALLBACK = CALLBACK(
                VOID,
                PKSOBJECT_CREATE_ITEM,
            )


            KSCREATE_ITEM_SECURITYCHANGED = 0x00000001
            KSCREATE_ITEM_WILDCARD = 0x00000002
            KSCREATE_ITEM_NOPARAMETERS = 0x00000004
            KSCREATE_ITEM_FREEONSTOP = 0x00000008


            def DEFINE_KSCREATE_DISPATCH_TABLE(tablename):
                return KSOBJECT_CREATE_ITEM * 0


            def DEFINE_KSCREATE_ITEM(DispatchCreate, TypeName, Context):
                return (
                    DispatchCreate,
                    PVOID(Context), (
                        ctypes.sizeof(TypeName) - ctypes.sizeof(UNICODE_NULL),
                        ctypes.sizeof(TypeName),
                        PWCHAR(TypeName)
                    ),
                    NULL,
                    0
                )

            def DEFINE_KSCREATE_ITEMEX(DispatchCreate, TypeName, Context, Flags):
                return (
                    DispatchCreate,
                    PVOID(Context),
                    (
                        ctypes.sizeof(TypeName) - ctypes.sizeof(UNICODE_NULL),
                        ctypes.sizeof(TypeName),
                        PWCHAR(TypeName)
                    ),
                    NULL,
                    Flags
                )


            def DEFINE_KSCREATE_ITEMNULL(DispatchCreate, Context):
                return DispatchCreate, Context, (0, 0, NULL), NULL, 0


            KSOBJECT_CREATE._fields_ = [
                ('CreateItemsCount', ULONG),
                ('CreateItemsList', PKSOBJECT_CREATE_ITEM),
            ]
            KSDISPATCH_TABLE._fields_ = [
                ('DeviceIoControl', PDRIVER_DISPATCH),
                ('Read', PDRIVER_DISPATCH),
                ('Write', PDRIVER_DISPATCH),
                ('Flush', PDRIVER_DISPATCH),
                ('Close', PDRIVER_DISPATCH),
                ('QuerySecurity', PDRIVER_DISPATCH),
                ('SetSecurity', PDRIVER_DISPATCH),
                ('FastDeviceIoControl', PFAST_IO_DEVICE_CONTROL),
                ('FastRead', PFAST_IO_READ),
                ('FastWrite', PFAST_IO_WRITE),
            ]
            def DEFINE_KSDISPATCH_TABLE(tablename, DeviceIoControl, Read, Write, Flush, Close, QuerySecurity, SetSecurity, FastDeviceIoControl, FastRead, FastWrite):
                return KSDISPATCH_TABLE(
                    DeviceIoControl,
                    Read,
                    Write,
                    Flush,
                    Close,
                    QuerySecurity,
                    SetSecurity,
                    FastDeviceIoControl,
                    FastRead,
                    FastWrite
                )

            def KSCREATE_ITEM_IRP_STORAGE(Irp):
                return POINTER(PKSOBJECT_CREATE_ITEM)(ctypes.byref(Irp.Tail.Overlay.DriverContext[0]))


            def KSEVENT_SET_IRP_STORAGE(Irp):
                return POINTER(KSEVENT_SET)(ctypes.byref(Irp.Tail.Overlay.DriverContext[0]))


            def KSEVENT_ITEM_IRP_STORAGE(Irp):
                return POINTER(KSEVENT_ITEM)(ctypes.byref(Irp.Tail.Overlay.DriverContext[3]))


            def KSEVENT_ENTRY_IRP_STORAGE(Irp):
                return POINTER(PKSEVENT_ENTRY)(ctypes.byref(Irp.Tail.Overlay.DriverContext[0]))


            def KSMETHOD_SET_IRP_STORAGE(Irp):
                return POINTER(KSMETHOD_SET)(ctypes.byref(Irp.Tail.Overlay.DriverContext[0]))


            def KSMETHOD_ITEM_IRP_STORAGE(Irp):
                return POINTER(KSMETHOD_ITEM)(ctypes.byref(Irp.Tail.Overlay.DriverContext[3]))


            def KSMETHOD_TYPE_IRP_STORAGE(Irp):
                return POINTER(ULONG_PTR)(ctypes.byref(Irp.Tail.Overlay.DriverContext[2]))


            def KSQUEUE_SPINLOCK_IRP_STORAGE(Irp):
                return POINTER(PKSPIN_LOCK)(ctypes.byref(Irp.Tail.Overlay.DriverContext[1]))


            def KSPROPERTY_SET_IRP_STORAGE(Irp):
                return POINTER(KSPROPERTY_SET)(ctypes.byref(Irp.Tail.Overlay.DriverContext[0]))


            def KSPROPERTY_ITEM_IRP_STORAGE(Irp):
                return POINTER(KSPROPERTY_ITEM)(ctypes.byref(Irp.Tail.Overlay.DriverContext[3]))


            def KSPROPERTY_ATTRIBUTES_IRP_STORAGE(Irp):
                return POINTER(PKSATTRIBUTE_LIST)(ctypes.byref(Irp.Tail.Overlay.DriverContext[2]))


            KSDEVICE_HEADER = PVOID
            KSOBJECT_HEADER = PVOID

            class KSCOMPLETION_INVOCATION(ENUM):
                KsInvokeOnSuccess = 1
                KsInvokeOnError = 2
                KsInvokeOnCancel = 4

            KsInvokeOnSuccess = KSCOMPLETION_INVOCATION.KsInvokeOnSuccess
            KsInvokeOnError = KSCOMPLETION_INVOCATION.KsInvokeOnError
            KsInvokeOnCancel = KSCOMPLETION_INVOCATION.KsInvokeOnCancel


            class KSLIST_ENTRY_LOCATION(ENUM):
                KsListEntryTail = 1
                KsListEntryHead = 2

            KsListEntryTail = KSLIST_ENTRY_LOCATION.KsListEntryTail
            KsListEntryHead = KSLIST_ENTRY_LOCATION.KsListEntryHead


            class KSIRP_REMOVAL_OPERATION(ENUM):
                KsAcquireOnly = 1
                KsAcquireAndRemove = 2
                KsAcquireOnlySingleItem = 3
                KsAcquireAndRemoveOnlySingleItem = 4

            KsAcquireOnly = KSIRP_REMOVAL_OPERATION.KsAcquireOnly
            KsAcquireAndRemove = KSIRP_REMOVAL_OPERATION.KsAcquireAndRemove
            KsAcquireOnlySingleItem = KSIRP_REMOVAL_OPERATION.KsAcquireOnlySingleItem
            KsAcquireAndRemoveOnlySingleItem = KSIRP_REMOVAL_OPERATION.KsAcquireAndRemoveOnlySingleItem


            class KSSTACK_USE(ENUM):
                KsStackCopyToNewLocation = 1
                KsStackReuseCurrentLocation = 2
                KsStackUseNewLocation = 3

            KsStackCopyToNewLocation = KSSTACK_USE.KsStackCopyToNewLocation
            KsStackReuseCurrentLocation = KSSTACK_USE.KsStackReuseCurrentLocation
            KsStackUseNewLocation = KSSTACK_USE.KsStackUseNewLocation


            class KSTARGET_STATE(ENUM):
                KSTARGET_STATE_DISABLED = 1
                KSTARGET_STATE_ENABLED = 2

            KSTARGET_STATE_DISABLED = KSTARGET_STATE.KSTARGET_STATE_DISABLED
            KSTARGET_STATE_ENABLED = KSTARGET_STATE.KSTARGET_STATE_ENABLED

            # NTSTATUS
            # (*PFNKSIRPLISTCALLBACK)(
            # _In_ PIRP Irp,
            # _In_ PVOID Context
            # );
            PFNKSIRPLISTCALLBACK = CALLBACK(
                NTSTATUS,
                PIRP,
                PVOID,
            )


            # VOID
            # (*PFNREFERENCEDEVICEOBJECT)(
            # _In_ PVOID Context
            # );
            PFNREFERENCEDEVICEOBJECT = CALLBACK(
                VOID,
                PVOID,
            )


            # VOID
            # (*PFNDEREFERENCEDEVICEOBJECT)(
            # _In_ PVOID Context
            # );
            PFNDEREFERENCEDEVICEOBJECT = CALLBACK(
                VOID,
                PVOID,
            )


            # NTSTATUS
            # (*PFNQUERYREFERENCESTRING)(
            # _In_ PVOID Context,
            # _Inout_ PWCHAR *String
            # );
            PFNQUERYREFERENCESTRING = CALLBACK(
                NTSTATUS,
                PVOID,
                POINTER(PWCHAR),
            )


            BUS_INTERFACE_REFERENCE_VERSION = 0x100


            BUS_INTERFACE_REFERENCE._fields_ = [
                # Standard interface header
                ('Interface', INTERFACE),
                # Standard bus interfaces
                ('ReferenceDeviceObject', PFNREFERENCEDEVICEOBJECT),
                ('DereferenceDeviceObject', PFNDEREFERENCEDEVICEOBJECT),
                ('QueryReferenceString', PFNQUERYREFERENCESTRING),
            ]
            STATIC_REFERENCE_BUS_INTERFACE = STATIC_KSMEDIUMSETID_Standard
            REFERENCE_BUS_INTERFACE = KSMEDIUMSETID_Standard

            # NTSTATUS
            # (*PFNQUERYMEDIUMSLIST)(
            # _In_ PVOID Context,
            # _Out_ ULONG* MediumsCount,
            # _Out_writes_(MediumsCount) PKSPIN_MEDIUM* MediumList
            # );
            PFNQUERYMEDIUMSLIST = CALLBACK(
                NTSTATUS,
                PVOID,
                POINTER(ULONG),
                POINTER(PKSPIN_MEDIUM),
            )


            BUS_INTERFACE_MEDIUMS._fields_ = [
                # Standard interface header
                ('Interface', INTERFACE),
                # Interface definition
                ('QueryMediumsList', PFNQUERYMEDIUMSLIST),
            ]
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
                0x96
            )
            GUID_BUS_INTERFACE_MEDIUMS = DEFINE_GUIDSTRUCT(
                "4EC35C3E-201B-11D2-8745-00A0C9223196"
            )
            GUID_BUS_INTERFACE_MEDIUMS = (
                DEFINE_GUIDNAMED(GUID_BUS_INTERFACE_MEDIUMS)
            )
        # END IF   defined(_NTDDK_)

        if not defined(PACK_PRAGMAS_NOT_SUPPORTED):
            from pshpack1_h import * # NOQA
        # END IF


        KSPROPERTY_SERIALHDR._fields_ = [
            ('PropertySet', GUID),
            ('Count', ULONG),
        ]

        if not defined(PACK_PRAGMAS_NOT_SUPPORTED):
            from poppack_h import * # NOQA
        # END IF


        KSPROPERTY_SERIAL._fields_ = [
            ('PropTypeSet', KSIDENTIFIER),
            ('Id', ULONG),
            ('PropertyLength', ULONG),
        ]
        if NTDDI_VERSION >= NTDDI_WINXP:
            if defined(_NTDDK_):
                IOCTL_KS_HANDSHAKE = CTL_CODE(
                    FILE_DEVICE_KS,
                    0x007,
                    METHOD_NEITHER,
                    FILE_ANY_ACCESS,
                )


                KSHANDSHAKE._fields_ = [
                    ('ProtocolId', GUID),
                    ('Argument1', PVOID),
                    ('Argument2', PVOID),
                ]

                _KSGATE._fields_ = [
                    ('Count', LONG),
                    ('NextGate', PKSGATE),
                ]

                if not defined(_NTOS_):
                    # If we made a transition, it must be propagated.
                    # We return whatever the state was prior to the
                    # compare/exchange. If
                    # the state was on, the state is now off.                    # _In_ BOOLEAN NextGateIsAnOrGate
                    pass
                # END IF   not _NTOS_

                KSOBJECT_BAG = PVOID

                # BOOLEAN
                # (*PFNKSGENERATEEVENTCALLBACK)(
                # _In_ PVOID Context,
                # _In_ PKSEVENT_ENTRY EventEntry
                # );
                PFNKSGENERATEEVENTCALLBACK = CALLBACK(
                    BOOLEAN,
                    PVOID,
                    PKSEVENT_ENTRY,
                )


                # NTSTATUS
                # (*PFNKSDEVICECREATE)(
                # _In_ PKSDEVICE Device
                # );
                PFNKSDEVICECREATE = CALLBACK(
                    NTSTATUS,
                    PKSDEVICE,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSDEVICEPNPSTART)(
                # _In_ PKSDEVICE Device,
                # _In_ PIRP Irp,
                # _In_opt_ PCM_RESOURCE_LIST TranslatedResourceList,
                # _In_opt_ PCM_RESOURCE_LIST UntranslatedResourceList
                # );
                PFNKSDEVICEPNPSTART = CALLBACK(
                    NTSTATUS,
                    PKSDEVICE,
                    PIRP,
                    PCM_RESOURCE_LIST,
                    PCM_RESOURCE_LIST,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSDEVICE)(
                # _In_ PKSDEVICE Device
                # );
                PFNKSDEVICE = CALLBACK(
                    NTSTATUS,
                    PKSDEVICE,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSDEVICEIRP)(
                # _In_ PKSDEVICE Device,
                # _In_ PIRP Irp
                # );
                PFNKSDEVICEIRP = CALLBACK(
                    NTSTATUS,
                    PKSDEVICE,
                    PIRP,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # void
                # (*PFNKSDEVICEIRPVOID)(
                # _In_ PKSDEVICE Device,
                # _In_ PIRP Irp
                # );
                PFNKSDEVICEIRPVOID = CALLBACK(
                    VOID,
                    PKSDEVICE,
                    PIRP,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSDEVICEQUERYCAPABILITIES)(
                # _In_ PKSDEVICE Device,
                # _In_ PIRP Irp,
                # _Inout_ PDEVICE_CAPABILITIES Capabilities
                # );
                PFNKSDEVICEQUERYCAPABILITIES = CALLBACK(
                    NTSTATUS,
                    PKSDEVICE,
                    PIRP,
                    PDEVICE_CAPABILITIES,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSDEVICEQUERYPOWER)(
                # _In_ PKSDEVICE Device,
                # _In_ PIRP Irp,
                # _In_ DEVICE_POWER_STATE DeviceTo,
                # _In_ DEVICE_POWER_STATE DeviceFrom,
                # _In_ SYSTEM_POWER_STATE SystemTo,
                # _In_ SYSTEM_POWER_STATE SystemFrom,
                # _In_ POWER_ACTION Action
                # );
                PFNKSDEVICEQUERYPOWER = CALLBACK(
                    NTSTATUS,
                    PKSDEVICE,
                    PIRP,
                    DEVICE_POWER_STATE,
                    DEVICE_POWER_STATE,
                    SYSTEM_POWER_STATE,
                    SYSTEM_POWER_STATE,
                    POWER_ACTION,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # void
                # (*PFNKSDEVICESETPOWER)(
                # _In_ PKSDEVICE Device,
                # _In_ PIRP Irp,
                # _In_ DEVICE_POWER_STATE To,
                # _In_ DEVICE_POWER_STATE From
                # );
                PFNKSDEVICESETPOWER = CALLBACK(
                    VOID,
                    PKSDEVICE,
                    PIRP,
                    DEVICE_POWER_STATE,
                    DEVICE_POWER_STATE,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSFILTERFACTORYVOID)(
                # _In_ PKSFILTERFACTORY FilterFactory
                # );
                PFNKSFILTERFACTORYVOID = CALLBACK(
                    NTSTATUS,
                    PKSFILTERFACTORY,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # void
                # (*PFNKSFILTERFACTORYPOWER)(
                # _In_ PKSFILTERFACTORY FilterFactory,
                # _In_ DEVICE_POWER_STATE State
                # );
                PFNKSFILTERFACTORYPOWER = CALLBACK(
                    VOID,
                    PKSFILTERFACTORY,
                    DEVICE_POWER_STATE,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSFILTERIRP)(
                # _In_ PKSFILTER Filter,
                # _In_ PIRP Irp
                # );
                PFNKSFILTERIRP = CALLBACK(
                    NTSTATUS,
                    PKSFILTER,
                    PIRP,
                )


                # NTSTATUS
                # (*PFNKSFILTERPROCESS)(
                # _In_ PKSFILTER Filter,
                # _In_ PKSPROCESSPIN_INDEXENTRY Index
                # );
                PFNKSFILTERPROCESS = CALLBACK(
                    NTSTATUS,
                    PKSFILTER,
                    PKSPROCESSPIN_INDEXENTRY,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSFILTERVOID)(
                # _In_ PKSFILTER Filter
                # );
                PFNKSFILTERVOID = CALLBACK(
                    NTSTATUS,
                    PKSFILTER,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # void
                # (*PFNKSFILTERPOWER)(
                # _In_ PKSFILTER Filter,
                # _In_ DEVICE_POWER_STATE State
                # );
                PFNKSFILTERPOWER = CALLBACK(
                    VOID,
                    PKSFILTER,
                    DEVICE_POWER_STATE,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSPINIRP)(
                # _In_ PKSPIN Pin,
                # _In_ PIRP Irp
                # );
                PFNKSPINIRP = CALLBACK(
                    NTSTATUS,
                    PKSPIN,
                    PIRP,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSPINSETDEVICESTATE)(
                # _In_ PKSPIN Pin,
                # _In_ KSSTATE ToState,
                # _In_ KSSTATE FromState
                # );
                PFNKSPINSETDEVICESTATE = CALLBACK(
                    NTSTATUS,
                    PKSPIN,
                    KSSTATE,
                    KSSTATE,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSPINSETDATAFORMAT)(
                # _In_ PKSPIN Pin,
                # _In_opt_ PKSDATAFORMAT OldFormat,
                # _In_opt_ PKSMULTIPLE_ITEM OldAttributeList,
                # _In_ KSDATARANGE* DataRange,
                # _In_opt_ KSATTRIBUTE_LIST* AttributeRange
                # );
                PFNKSPINSETDATAFORMAT = CALLBACK(
                    NTSTATUS,
                    PKSPIN,
                    PKSDATAFORMAT,
                    PKSMULTIPLE_ITEM,
                    POINTER(KSDATARANGE),
                    POINTER(KSATTRIBUTE_LIST)
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSPINHANDSHAKE)(
                # _In_ PKSPIN Pin,
                # _In_ PKSHANDSHAKE In,
                # _In_ PKSHANDSHAKE Out
                # );
                PFNKSPINHANDSHAKE = CALLBACK(
                    NTSTATUS,
                    PKSPIN,
                    PKSHANDSHAKE,
                    PKSHANDSHAKE,
                )


                # NTSTATUS
                # (*PFNKSPIN)(
                # _In_ PKSPIN Pin
                # );
                PFNKSPIN = CALLBACK(
                    NTSTATUS,
                    PKSPIN,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # void
                # (*PFNKSPINVOID)(
                # _In_ PKSPIN Pin
                # );
                PFNKSPINVOID = CALLBACK(
                    VOID,
                    PKSPIN,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # void
                # (*PFNKSPINPOWER)(
                # _In_ PKSPIN Pin,
                # _In_ DEVICE_POWER_STATE State
                # );
                PFNKSPINPOWER = CALLBACK(
                    VOID,
                    PKSPIN,
                    DEVICE_POWER_STATE,
                )


                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # typedef
                # BOOLEAN
                # (*PFNKSPINSETTIMER)(
                # _In_ PKSPIN Pin,
                # _In_ PKTIMER Timer,
                # _In_ LARGE_INTEGER DueTime,
                # _In_ PKDPC Dpc
                # );
                PFNKSPINSETTIMER = CALLBACK(
                    BOOLEAN,
                    PKSPIN,
                    PKTIMER,
                    LARGE_INTEGER,
                    PKDPC,
                )


                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # typedef
                # BOOLEAN
                # (*PFNKSPINCANCELTIMER)(
                # _In_ PKSPIN Pin,
                # _In_ PKTIMER Timer
                # );
                PFNKSPINCANCELTIMER = CALLBACK(
                    BOOLEAN,
                    PKSPIN,
                    PKTIMER,
                )


                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # typedef
                # LONGLONG
                # (FASTCALL *PFNKSPINCORRELATEDTIME)(
                # _In_ PKSPIN Pin,
                # _Out_ PLONGLONG SystemTime
                # );
                PFNKSPINCORRELATEDTIME = FASTCALL(
                    LONGLONG,
                    PKSPIN,
                    PLONGLONG,
                )


                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # typedef
                # void
                # (*PFNKSPINRESOLUTION)(
                # _In_ PKSPIN Pin,
                # _Out_ PKSRESOLUTION Resolution
                # );
                PFNKSPINRESOLUTION = CALLBACK(
                    VOID,
                    PKSPIN,
                    PKSRESOLUTION,
                )


                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # typedef
                # NTSTATUS
                # (*PFNKSPININITIALIZEALLOCATOR)(
                # _In_ PKSPIN Pin,
                # _In_ PKSALLOCATOR_FRAMING AllocatorFraming,
                # _Out_ PVOID* Context
                # );
                PFNKSPININITIALIZEALLOCATOR = CALLBACK(
                    NTSTATUS,
                    PKSPIN,
                    PKSALLOCATOR_FRAMING,
                    POINTER(PVOID),
                )


                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # typedef
                # void
                # (*PFNKSSTREAMPOINTER)(
                # _In_ PKSSTREAM_POINTER StreamPointer
                # );
                PFNKSSTREAMPOINTER = CALLBACK(
                    VOID,
                    PKSSTREAM_POINTER,
                )

                _TEMP_KSAUTOMATION_TABLE_ = [
                    ('PropertySetsCount', ULONG),
                    ('PropertyItemSize', ULONG),
                    ('PropertySets', POINTER(KSPROPERTY_SET)),
                    ('MethodSetsCount', ULONG),
                    ('MethodItemSize', ULONG),
                    ('MethodSets', POINTER(KSMETHOD_SET)),
                    ('EventSetsCount', ULONG),
                    ('EventItemSize', ULONG),
                    ('EventSets', POINTER(KSEVENT_SET)),
                ]
                if not defined(_WIN64):
                    _TEMP_KSAUTOMATION_TABLE_ += [
                        ('Alignment', PVOID),
                    ]
                # END IF   not defined(_WIN64)


                KSAUTOMATION_TABLE_._fields_ = _TEMP_KSAUTOMATION_TABLE_


                def DEFINE_KSAUTOMATION_TABLE(table):
                    return KSAUTOMATION_TABLE


                def DEFINE_KSAUTOMATION_PROPERTIES(table):
                    return SIZEOF_ARRAY(table), ctypes.sizeof(KSPROPERTY_ITEM), table



                def DEFINE_KSAUTOMATION_METHODS(table):
                    return SIZEOF_ARRAY(table), ctypes.sizeof(KSMETHOD_ITEM), table


                def DEFINE_KSAUTOMATION_EVENTS(table):
                    return SIZEOF_ARRAY(table), ctypes.sizeof(KSEVENT_ITEM), table


                DEFINE_KSAUTOMATION_PROPERTIES_NULL = (
                    0,
                    ctypes.sizeof(KSPROPERTY_ITEM),
                    NULL
                )

                DEFINE_KSAUTOMATION_METHODS_NULL = (
                    0,
                    ctypes.sizeof(KSMETHOD_ITEM),
                    NULL

                )

                DEFINE_KSAUTOMATION_EVENTS_NULL = (
                    0,
                    ctypes.sizeof(KSEVENT_ITEM),
                    NULL
                )


                MIN_DEV_VER_FOR_QI = 0x100
                _KSDEVICE_DISPATCH._fields_ = [
                    ('Add', PFNKSDEVICECREATE),
                    ('Start', PFNKSDEVICEPNPSTART),
                    ('PostStart', PFNKSDEVICE),
                    ('QueryStop', PFNKSDEVICEIRP),
                    ('CancelStop', PFNKSDEVICEIRPVOID),
                    ('Stop', PFNKSDEVICEIRPVOID),
                    ('QueryRemove', PFNKSDEVICEIRP),
                    ('CancelRemove', PFNKSDEVICEIRPVOID),
                    ('Remove', PFNKSDEVICEIRPVOID),
                    ('QueryCapabilities', PFNKSDEVICEQUERYCAPABILITIES),
                    ('SurpriseRemoval', PFNKSDEVICEIRPVOID),
                    ('QueryPower', PFNKSDEVICEQUERYPOWER),
                    ('SetPower', PFNKSDEVICESETPOWER),
                    # added in version 0x100
                    ('QueryInterface', PFNKSDEVICEIRP),
                ]
                _KSFILTER_DISPATCH._fields_ = [
                    ('Create', PFNKSFILTERIRP),
                    ('Close', PFNKSFILTERIRP),
                    ('Process', PFNKSFILTERPROCESS),
                    ('Reset', PFNKSFILTERVOID),
                ]
                _KSPIN_DISPATCH._fields_ = [
                    ('Create', PFNKSPINIRP),
                    ('Close', PFNKSPINIRP),
                    ('Process', PFNKSPIN),
                    ('Reset', PFNKSPINVOID),
                    ('SetDataFormat', PFNKSPINSETDATAFORMAT),
                    ('SetDeviceState', PFNKSPINSETDEVICESTATE),
                    ('Connect', PFNKSPIN),
                    ('Disconnect', PFNKSPINVOID),
                    ('Clock', POINTER(KSCLOCK_DISPATCH)),
                    ('Allocator', POINTER(KSALLOCATOR_DISPATCH)),
                ]
                _KSCLOCK_DISPATCH._fields_ = [
                    ('SetTimer', PFNKSPINSETTIMER),
                    ('CancelTimer', PFNKSPINCANCELTIMER),
                    ('CorrelatedTime', PFNKSPINCORRELATEDTIME),
                    ('Resolution', PFNKSPINRESOLUTION),
                ]
                _KSALLOCATOR_DISPATCH._fields_ = [
                    ('InitializeAllocator', PFNKSPININITIALIZEALLOCATOR),
                    ('DeleteAllocator', PFNKSDELETEALLOCATOR),
                    ('Allocate', PFNKSDEFAULTALLOCATE),
                    ('Free', PFNKSDEFAULTFREE),
                ]
                # VERSION indicates support of the following:
                # - QueryInterface dispatch of KSDEVICE_DISPATCH
                KSDEVICE_DESCRIPTOR_VERSION = 0x100
                if NTDDI_VERSION >= NTDDI_VISTA:
                    # VERSION_2 indicates support of the following:
                    # - Flags field of KSDEVICE_DESCRIPTOR
                    # - Loading a VERSION_2 descriptor on earlier versions of
                    # AVStream
                    # will work; however, all flags will be considered to be
                    # zero.
                    # - Using an earlier version descriptor on later versions
                    # of
                    # AVStream causes no flags to be specificed.
                    KSDEVICE_DESCRIPTOR_VERSION_2 = 0x110
                    MIN_DEV_VER_FOR_FLAGS = 0x110
                # END IF   (NTDDI_VERSION >= NTDDI_VISTA)


                _TEMP__KSDEVICE_DESCRIPTOR = [
                    ('Dispatch', POINTER(KSDEVICE_DISPATCH)),
                    ('FilterDescriptorsCount', ULONG),
                    ('FilterDescriptors', POINTER(KSFILTER_DESCRIPTOR)),
                    # this is 0 for pre-version 100 driver
                    ('Version', ULONG),
                ]

                if NTDDI_VERSION >= NTDDI_VISTA:
                    KSDEVICE_FLAG_ENABLE_REMOTE_WAKEUP = 0x00000001
                    KSDEVICE_FLAG_LOWPOWER_PASSTHROUGH = 0x00000002
                    _TEMP__KSDEVICE_DESCRIPTOR += [
                        ('Flags', ULONG),
                    ]

                    if not defined(_WIN64):
                        KSDEVICE_FLAG_ENABLE_QUERYINTERFACE = 0x00000004
                        _TEMP__KSDEVICE_DESCRIPTOR += [
                            ('Alignment', PVOID),
                        ]
                    # END IF   not defined(_WIN64)

                # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

                _KSDEVICE_DESCRIPTOR._fields_ = _TEMP__KSDEVICE_DESCRIPTOR
                KSFILTER_DESCRIPTOR_VERSION = -1
                KSFILTER_FLAG_DISPATCH_LEVEL_PROCESSING = 0x00000001
                KSFILTER_FLAG_CRITICAL_PROCESSING = 0x00000002
                KSFILTER_FLAG_HYPERCRITICAL_PROCESSING = 0x00000004
                KSFILTER_FLAG_RECEIVE_ZERO_LENGTH_SAMPLES = 0x00000008

                if NTDDI_VERSION >= NTDDI_WINXPSP2:
                    KSFILTER_FLAG_DENY_USERMODE_ACCESS = 0x80000000
                # END IF   (NTDDI_VERSION >= NTDDI_WINXPSP2)

                KSFILTER_FLAG_PRIORITIZE_REFERENCEGUID = 0x00000010

                _TEMP__KSFILTER_DESCRIPTOR = [
                    ('Dispatch', POINTER(KSFILTER_DISPATCH)),
                    ('AutomationTable', POINTER(KSAUTOMATION_TABLE)),
                    ('Version', ULONG),
                    ('Flags', ULONG),
                ]

                _TEMP__KSFILTER_DESCRIPTOR += [
                    # camera profiles must set this flag.
                    ('ReferenceGuid', POINTER(GUID)),
                    ('PinDescriptorsCount', ULONG),
                    ('PinDescriptorSize', ULONG),
                    ('PinDescriptors', POINTER(KSPIN_DESCRIPTOR_EX)),
                    ('CategoriesCount', ULONG),
                    ('Categories', POINTER(GUID)),
                    ('NodeDescriptorsCount', ULONG),
                    ('NodeDescriptorSize', ULONG),
                    ('NodeDescriptors', POINTER(KSNODE_DESCRIPTOR)),
                    ('ConnectionsCount', ULONG),
                    ('Connections', POINTER(KSTOPOLOGY_CONNECTION)),
                    ('ComponentId', POINTER(KSCOMPONENTID)),
                ]
                _KSFILTER_DESCRIPTOR._fields_ = _TEMP__KSFILTER_DESCRIPTOR

                def DEFINE_KSFILTER_DESCRIPTOR(descriptor):
                    return KSFILTER_DESCRIPTOR


                def DEFINE_KSFILTER_PIN_DESCRIPTORS(table):
                    return SIZEOF_ARRAY(table), ctypes.sizeof(table[0]), table


                def DEFINE_KSFILTER_CATEGORIES(table):
                    return SIZEOF_ARRAY(table), table


                def DEFINE_KSFILTER_CATEGORY(category):
                    return 1 & category


                DEFINE_KSFILTER_CATEGORIES_NULL = 0,NULL
                def DEFINE_KSFILTER_NODE_DESCRIPTORS(table):
                    return SIZEOF_ARRAY(table), ctypes.sizeof(table[0]), table


                DEFINE_KSFILTER_NODE_DESCRIPTORS_NULL = (
                    0,
                    ctypes.sizeof(KSNODE_DESCRIPTOR),
                    NULL
                )


                def DEFINE_KSFILTER_CONNECTIONS(table):
                    return SIZEOF_ARRAY(table), table


                DEFINE_KSFILTER_DEFAULT_CONNECTIONS = (0, NULL)

                def DEFINE_KSFILTER_DESCRIPTOR_TABLE(table):
                    return KSFILTER_DESCRIPTOR * 0


                KSPIN_FLAG_DISPATCH_LEVEL_PROCESSING = (
                    KSFILTER_FLAG_DISPATCH_LEVEL_PROCESSING
                )
                KSPIN_FLAG_CRITICAL_PROCESSING = (
                    KSFILTER_FLAG_CRITICAL_PROCESSING
                )
                KSPIN_FLAG_HYPERCRITICAL_PROCESSING = (
                    KSFILTER_FLAG_HYPERCRITICAL_PROCESSING
                )
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
                    KSPIN_FLAG_PROCESS_IN_RUN_STATE_ONLY | KSPIN_FLAG_GENERATE_EOS_EVENTS
                )
                KSPIN_FLAG_IMPLEMENT_CLOCK = 0x00400000
                KSPIN_FLAG_SOME_FRAMES_REQUIRED_FOR_PROCESSING = 0x00800000
                KSPIN_FLAG_PROCESS_IF_ANY_IN_RUN_STATE = 0x01000000

                if NTDDI_VERSION >= NTDDI_WINXPSP2:
                    KSPIN_FLAG_DENY_USERMODE_ACCESS = 0x80000000
                # END IF   (NTDDI_VERSION >= NTDDI_WINXPSP2)


                _TEMP__KSPIN_DESCRIPTOR_EX = [
                    ('Dispatch', POINTER(KSPIN_DISPATCH)),
                    ('AutomationTable', POINTER(KSAUTOMATION_TABLE)),
                    ('PinDescriptor', KSPIN_DESCRIPTOR),
                    ('Flags', ULONG),
                ]

                _TEMP__KSPIN_DESCRIPTOR_EX += [
                    ('InstancesPossible', ULONG),
                    ('InstancesNecessary', ULONG),
                    ('AllocatorFraming', POINTER(KSALLOCATOR_FRAMING_EX)),
                    ('IntersectHandler', PFNKSINTERSECTHANDLEREX),
                ]

                _KSPIN_DESCRIPTOR_EX._fields_ = _TEMP__KSPIN_DESCRIPTOR_EX
                DEFINE_KSPIN_DEFAULT_INTERFACES = 0,NULL
                DEFINE_KSPIN_DEFAULT_MEDIUMS = 0,NULL


                _TEMP__KSNODE_DESCRIPTOR = [
                    ('AutomationTable', POINTER(KSAUTOMATION_TABLE)),
                    ('Type', POINTER(GUID)),
                    ('Name', POINTER(GUID)),
                ]
                if not defined(_WIN64):
                    _TEMP__KSNODE_DESCRIPTOR += [
                        ('Alignment', PVOID),
                    ]
                # END IF   not defined(_WIN64)


                _KSNODE_DESCRIPTOR._fields_ = _TEMP__KSNODE_DESCRIPTOR


                if not defined(_WIN64):
                    def DEFINE_NODE_DESCRIPTOR(automation, type, name):
                        return automation, type, name, NULL
                else:
                    def DEFINE_NODE_DESCRIPTOR(automation, type, name):
                        return automation, type, name
                # END IF   not defined(_WIN64)


                _KSDEVICE._fields_ = [
                    ('Descriptor', POINTER(KSDEVICE_DESCRIPTOR)),
                    ('Bag', KSOBJECT_BAG),
                    ('Context', PVOID),
                    ('FunctionalDeviceObject', PDEVICE_OBJECT),
                    ('PhysicalDeviceObject', PDEVICE_OBJECT),
                    ('NextDeviceObject', PDEVICE_OBJECT),
                    ('Started', BOOLEAN),
                    ('SystemPowerState', SYSTEM_POWER_STATE),
                    ('DevicePowerState', DEVICE_POWER_STATE),
                ]

                _KSFILTERFACTORY._fields_ = [
                    ('FilterDescriptor', POINTER(KSFILTER_DESCRIPTOR)),
                    ('Bag', KSOBJECT_BAG),
                    ('Context', PVOID),
                ]

                _KSFILTER._fields_ = [
                    ('Descriptor', POINTER(KSFILTER_DESCRIPTOR)),
                    ('Bag', KSOBJECT_BAG),
                    ('Context', PVOID),
                ]

                _KSPIN._fields_ = [
                    ('Descriptor', POINTER(KSPIN_DESCRIPTOR_EX)),
                    ('Bag', KSOBJECT_BAG),
                    ('Context', PVOID),
                    ('Id', ULONG),
                    ('Communication', KSPIN_COMMUNICATION),
                    ('ConnectionIsExternal', BOOLEAN),
                    ('ConnectionInterface', KSPIN_INTERFACE),
                    ('ConnectionMedium', KSPIN_MEDIUM),
                    ('ConnectionPriority', KSPRIORITY),
                    ('ConnectionFormat', PKSDATAFORMAT),
                    ('AttributeList', PKSMULTIPLE_ITEM),
                    ('StreamHeaderSize', ULONG),
                    ('DataFlow', KSPIN_DATAFLOW),
                    ('DeviceState', KSSTATE),
                    ('ResetState', KSRESET),
                    ('ClientState', KSSTATE),
                ]

                _KSMAPPING._fields_ = [
                    ('PhysicalAddress', PHYSICAL_ADDRESS),
                    ('ByteCount', ULONG),
                    ('Alignment', ULONG),
                ]

                if defined(_NTDDK_):
                    class _Union_16(ctypes.Union):
                        pass


                    _Union_16._fields_ = [
                        ('Data', PUCHAR),
                        ('Mappings', PKSMAPPING),
                    ]
                    _KSSTREAM_POINTER_OFFSET._Union_16 = _Union_16

                _KSSTREAM_POINTER_OFFSET._anonymous_ = (
                    '_Union_16',
                )

                _TEMP__KSSTREAM_POINTER_OFFSET = [
                ]

                if defined(_NTDDK_):
                    _TEMP__KSSTREAM_POINTER_OFFSET += [
                        ('_Union_16', _KSSTREAM_POINTER_OFFSET._Union_16),
                    ]
                else: #  not defined(_NTDDK_)
                    _TEMP__KSSTREAM_POINTER_OFFSET += [
                        ('Data', PUCHAR),
                    ]
                # END IF   not defined(_NTDDK_)


                if not defined(_WIN64):
                    _TEMP__KSSTREAM_POINTER_OFFSET += [
                        ('Alignment', PVOID),
                    ]
                # END IF   not defined(_WIN64)


                _TEMP__KSSTREAM_POINTER_OFFSET += [
                    ('Count', ULONG),
                    ('Remaining', ULONG),
                ]
                _KSSTREAM_POINTER_OFFSET._fields_ = _TEMP__KSSTREAM_POINTER_OFFSET

                _KSSTREAM_POINTER._fields_ = [
                    ('Context', PVOID),
                    ('Pin', PKSPIN),
                    ('StreamHeader', PKSSTREAM_HEADER),
                    ('Offset', PKSSTREAM_POINTER_OFFSET),
                    ('OffsetIn', KSSTREAM_POINTER_OFFSET),
                    ('OffsetOut', KSSTREAM_POINTER_OFFSET),
                ]

                _KSPROCESSPIN._fields_ = [
                    ('Pin', PKSPIN),
                    ('StreamPointer', PKSSTREAM_POINTER),
                    ('InPlaceCounterpart', PKSPROCESSPIN),
                    ('DelegateBranch', PKSPROCESSPIN),
                    ('CopySource', PKSPROCESSPIN),
                    ('Data', PVOID),
                    ('BytesAvailable', ULONG),
                    ('BytesUsed', ULONG),
                    ('Flags', ULONG),
                    ('Terminate', BOOLEAN),
                ]

                _KSPROCESSPIN_INDEXENTRY._fields_ = [
                    ('Pins', POINTER(PKSPROCESSPIN)),
                    ('Count', ULONG),
                ]


                class KSOBJECTTYPE(ENUM):
                    KsObjectTypeDevice = 1
                    KsObjectTypeFilterFactory = 2
                    KsObjectTypeFilter = 3
                    KsObjectTypePin = 4

                KsObjectTypeDevice = KSOBJECTTYPE.KsObjectTypeDevice
                KsObjectTypeFilterFactory = KSOBJECTTYPE.KsObjectTypeFilterFactory
                KsObjectTypeFilter = KSOBJECTTYPE.KsObjectTypeFilter
                KsObjectTypePin = KSOBJECTTYPE.KsObjectTypePin

                # void
                # (*PFNKSFREE)(
                # _In_ PVOID Data
                # );
                PFNKSFREE = CALLBACK(
                    VOID,
                    PVOID,
                )


                # void
                # (*PFNKSPINFRAMERETURN)(
                # _In_ PKSPIN Pin,
                # _In_reads_bytes_opt_(Size) PVOID Data,
                # _In_ ULONG Size OPTIONAL,
                # _In_opt_ PMDL Mdl,
                # _In_opt_ PVOID Context,
                # _In_ NTSTATUS Status
                # );
                PFNKSPINFRAMERETURN = CALLBACK(
                    VOID,
                    PKSPIN,
                    PVOID,
                    Size,
                    PMDL,
                    PVOID,
                    NTSTATUS,
                )


                # void
                # (*PFNKSPINIRPCOMPLETION)(
                # _In_ PKSPIN Pin,
                # _In_ PIRP Irp
                # );
                PFNKSPINIRPCOMPLETION = CALLBACK(
                    VOID,
                    PKSPIN,
                    PIRP,
                )


                if defined(_UNKNOWN_H_) or defined(__IUnknown_INTERFACE_DEFINED__):
                    if not defined(_IKsControl_):
                        _IKsControl_ = 1


                        class IKsControl(comtypes.IUnknown):
                            _case_insensitive_ = True
                            _idlflags_ = []


                        PIKSCONTROL = POINTER(IKsControl)

                        if not defined(DEFINE_ABSTRACT_UNKNOWN):

                            def DEFINE_ABSTRACT_UNKNOWN():
                                pass
                                # return (
                                #     STDMETHOD_NTSTATUS,
                                #     QueryInterfaceTHIS_ _In_ REFIID InterfaceId,
                                #     _COM_Outptr_ PVOID* Interface PURE; STDMETHOD_ULONG,
                                #     AddRefTHIS PURE; STDMETHOD_ULONG,
                                #     ReleaseTHIS PURE;
                                # )
                        # END IF  not defined(DEFINE_ABSTRACT_UNKNOWN)

                        IKsControl._methods_ = [
                            COMMETHOD(
                                [],
                                NTSTATUS,
                                'KsProperty',
                                (['in'], PKSPROPERTY, 'Property'),
                                (['in'], ULONG, 'PropertyLength'),
                                (['in', 'out'], PVOID, 'PropertyData'),
                                (['in'], ULONG, 'DataLength'),
                                (['out'], POINTER(ULONG), 'BytesReturned'),
                            ),
                            COMMETHOD(
                                [],
                                NTSTATUS,
                                'KsMethod',
                                (['in'], PKSMETHOD, 'Method'),
                                (['in'], ULONG, 'MethodLength'),
                                (['in', 'out'], PVOID, 'MethodData'),
                                (['in'], ULONG, 'DataLength'),
                                (['out'], POINTER(ULONG), 'BytesReturned'),
                            ),
                            COMMETHOD(
                                [],
                                NTSTATUS,
                                'KsEvent',
                                (['in'], PKSEVENT, 'Event'),
                                (['in'], ULONG, 'EventLength'),
                                (['in', 'out'], PVOID, 'EventData'),
                                (['in'], ULONG, 'DataLength'),
                                (['out'], POINTER(ULONG), 'BytesReturned'),
                            ),
                        ]

                        class IKsReferenceClock(comtypes.IUnknown):
                            _case_insensitive_ = True
                            _idlflags_ = []


                        IKsReferenceClock._methods_ = [
                            COMMETHOD(
                                [],
                                LONGLONG,
                                'GetTime',
                            ),
                            COMMETHOD(
                                [],
                                LONGLONG,
                                'GetPhysicalTime',
                            ),
                            COMMETHOD(
                                [],
                                LONGLONG,
                                'GetCorrelatedTime',
                                (['out'], PLONGLONG, 'SystemTime'),
                            ),
                            COMMETHOD(
                                [],
                                LONGLONG,
                                'GetCorrelatedPhysicalTime',
                                (['out'], PLONGLONG, 'SystemTime'),
                            ),
                            COMMETHOD(
                                [],
                                NTSTATUS,
                                'GetResolution',
                                (['out'], PKSRESOLUTION, 'Resolution'),
                            ),
                            COMMETHOD(
                                [],
                                NTSTATUS,
                                'GetState',
                                (['out'], PKSSTATE, 'State'),
                            ),
                        ]

                        if NTDDI_VERSION >= NTDDI_WS03SP1:
                            class IKsDeviceFunctions(comtypes.IUnknown):
                                _case_insensitive_ = True
                                _idlflags_ = []

                            IKsDeviceFunctions._methods_ = [
                                COMMETHOD(
                                    [],
                                    LONGLONG,
                                    'RegisterAdapterObjectEx',
                                    (['in'], PADAPTER_OBJECT, 'AdapterObject'),
                                    (['in'], PDEVICE_DESCRIPTION, 'DeviceDescription'),
                                    (['in'], ULONG, 'NumberOfMapRegisters'),
                                    (['in'], ULONG, 'MaxMappingsByteCount'),
                                    (['in'], ULONG, 'MappingTableStride'),
                                ),
                            ]


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
                            0x96
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

                        IKsControl._iid_ = IID_IKsControl

                        if defined(__cplusplus) and _MSC_VER >= 1100:
                            pass
                            # IKsControl = UUID("28F54685-06FD-11D2-B27A-00A0C9223196")

                        # END IF


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
                            0x5E
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

                        IKsReferenceClock._iid_ = IID_IKsFastClock


                        if defined(__cplusplus) and _MSC_VER >= 1100:
                            pass
                            # IKsFastClock = UUID("C9902485-C180-11d2-8473-D42394459E5E")

                        # END IF


                        if NTDDI_VERSION >= NTDDI_WS03SP1:
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
                                0xBD
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

                            if defined(__cplusplus) and _MSC_VER >= 1100:
                                pass
                                # IKsDeviceFunctions = UUID("E234F2E2-BD69-4F8C-B3F2-7CD79ED466BD")
                            # END IF
                            IKsDeviceFunctions._iid_ = IID_IKsDeviceFunctions

                        # END IF   (NTDDI_VERSION >= NTDDI_WS03SP1)
                    # END IF   not defined(_IKsControl_)
                # END IF   defined(_UNKNOWN_H_) or defined(__IUnknown_INTERFACE_DEFINED__)
            # END IF   defined(_NTDDK_)
        # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

        # == == == == == == == == == == == == == == == == == == == == == == ==

        if defined(__cplusplus):
            ks = ctypes.windll.KS
            # extern "C" {
            # #endif // defined(__cplusplus)
            #
            #
            # // exported prototypes
            #
            #
            # #ifdef _KSDDK_
            # #define KSDDKAPI
            # #else // not _KSDDK_
            # #define KSDDKAPI DECLSPEC_IMPORT
            # #endif // _KSDDK_
            #
            # #if defined(_NTDDK_)
            #
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsEnableEvent(
            # _In_ PIRP Irp,
            # _In_ ULONG EventSetsCount,
            # _In_reads_(EventSetsCount) KSEVENT_SET* EventSet,
            # _Inout_opt_ PLIST_ENTRY EventsList,
            # _In_opt_ KSEVENTS_LOCKTYPE EventsFlags,
            # _In_opt_ PVOID EventsLock
            # );
            KsEnableEvent = ks.KsEnableEvent
            KsEnableEvent.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsEnableEventWithAllocator(
            # _In_ PIRP Irp,
            # _In_ ULONG EventSetsCount,
            # _In_reads_(EventSetsCount) KSEVENT_SET* EventSet,
            # _Inout_opt_ PLIST_ENTRY EventsList,
            # _In_ KSEVENTS_LOCKTYPE EventsFlags OPTIONAL,
            # _In_opt_ PVOID EventsLock,
            # _In_opt_ PFNKSALLOCATOR Allocator,
            # _In_opt_ ULONG EventItemSize
            # );
            KsEnableEventWithAllocator = ks.KsEnableEventWithAllocator
            KsEnableEventWithAllocator.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsDisableEvent(
            # _In_ PIRP Irp,
            # _Inout_ PLIST_ENTRY EventsList,
            # _In_ KSEVENTS_LOCKTYPE EventsFlags,
            # _In_ PVOID EventsLock
            # );
            KsDisableEvent = ks.KsDisableEvent
            KsDisableEvent.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsDiscardEvent(
            # _In_ PKSEVENT_ENTRY EventEntry
            # );
            KsDiscardEvent = ks.KsDiscardEvent
            KsDiscardEvent.restype = VOID

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsFreeEventList(
            # _In_ PFILE_OBJECT FileObject,
            # _Inout_ PLIST_ENTRY EventsList,
            # _In_ KSEVENTS_LOCKTYPE EventsFlags,
            # _In_ PVOID EventsLock
            # );
            KsFreeEventList = ks.KsFreeEventList
            KsFreeEventList.restype = VOID

            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsGenerateEvent(
            # _In_ PKSEVENT_ENTRY EventEntry
            # );
            KsGenerateEvent = ks.KsGenerateEvent
            KsGenerateEvent.restype = NTSTATUS

            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsGenerateDataEvent(
            # _In_ PKSEVENT_ENTRY EventEntry,
            # _In_ ULONG DataSize,
            # _In_reads_bytes_(DataSize) PVOID Data
            # );
            KsGenerateDataEvent = ks.KsGenerateDataEvent
            KsGenerateDataEvent.restype = NTSTATUS

            # KSDDKAPI
            # VOID
            # NTAPI
            # KsGenerateEventList(
            # _In_opt_ GUID* Set,
            # _In_ ULONG EventId,
            # _In_ PLIST_ENTRY EventsList,
            # _In_ KSEVENTS_LOCKTYPE EventsFlags,
            # _In_ PVOID EventsLock
            # );
            KsGenerateEventList = ks.KsGenerateEventList
            KsGenerateEventList.restype = VOID

            # Independent KS Thermal notifications..
            # void
            # (* PFNKSDEVICETHERMALACTIVECOOLING)(
            # _In_ PKSDEVICE KsDevice,
            # _In_ BOOLEAN Engaged,
            # _Out_ KSDEVICE_THERMAL_STATE* DeviceThermalState
            # );
            PFNKSDEVICETHERMALACTIVECOOLING = CALLBACK(
                VOID,
                PKSDEVICE,
                BOOLEAN,
                POINTER(KSDEVICE_THERMAL_STATE),
            )
            # void
            # (*PFNKSDEVICETHERMALPASSIVECOOLING)(
            # _In_ PKSDEVICE KsDevice,
            # _In_ ULONG Percentage,
            # _Out_ KSDEVICE_THERMAL_STATE* DeviceThermalState
            # );
            PFNKSDEVICETHERMALPASSIVECOOLING = CALLBACK(
                VOID,
                PKSDEVICE,
                ULONG,
                POINTER(KSDEVICE_THERMAL_STATE),
            )
            _KSDEVICE_THERMAL_DISPATCH._fields_ = [
                ('ActiveCooling', PFNKSDEVICETHERMALACTIVECOOLING),
                ('PassiveCooling', PFNKSDEVICETHERMALPASSIVECOOLING),
            ]
            # property.c:
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsPropertyHandler(
            # _In_ PIRP Irp,
            # _In_ ULONG PropertySetsCount,
            # _In_reads_(PropertySetsCount) KSPROPERTY_SET* PropertySet
            # );
            KsPropertyHandler = ks.KsPropertyHandler
            KsPropertyHandler.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsPropertyHandlerWithAllocator(
            # _In_ PIRP Irp,
            # _In_ ULONG PropertySetsCount,
            # _In_reads_(PropertySetsCount) KSPROPERTY_SET* PropertySet,
            # _In_opt_ PFNKSALLOCATOR Allocator,
            # _In_ ULONG PropertyItemSize OPTIONAL
            # );
            KsPropertyHandlerWithAllocator = ks.KsPropertyHandlerWithAllocator
            KsPropertyHandlerWithAllocator.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # BOOLEAN
            # NTAPI
            # KsFastPropertyHandler(
            # _In_ PFILE_OBJECT FileObject,
            # _In_reads_bytes_(PropertyLength) PKSPROPERTY Property,
            # _In_ ULONG PropertyLength,
            # _In_reads_bytes_(DataLength)PVOID Data,
            # _In_ ULONG DataLength,
            # _Out_ PIO_STATUS_BLOCK IoStatus,
            # _In_ ULONG PropertySetsCount,
            # _In_reads_(PropertySetsCount) KSPROPERTY_SET* PropertySet
            # );
            KsFastPropertyHandler = ks.KsFastPropertyHandler
            KsFastPropertyHandler.restype = BOOLEAN

            # method.c:
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsMethodHandler(
            # _In_ PIRP Irp,
            # _In_ ULONG MethodSetsCount,
            # _In_reads_(MethodSetsCount) KSMETHOD_SET* MethodSet
            # );
            KsMethodHandler = ks.KsMethodHandler
            KsMethodHandler.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsMethodHandlerWithAllocator(
            # _In_ PIRP Irp,
            # _In_ ULONG MethodSetsCount,
            # _In_reads_(MethodSetsCount) KSMETHOD_SET* MethodSet,
            # _In_opt_ PFNKSALLOCATOR Allocator,
            # _In_ ULONG MethodItemSize OPTIONAL
            # );
            KsMethodHandlerWithAllocator = ks.KsMethodHandlerWithAllocator
            KsMethodHandlerWithAllocator.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # BOOLEAN
            # NTAPI
            # KsFastMethodHandler(
            # _In_ PFILE_OBJECT FileObject,
            # _In_reads_bytes_(MethodLength) PKSMETHOD Method,
            # _In_ ULONG MethodLength,
            # _Inout_updates_bytes_(DataLength) PVOID Data,
            # _In_ ULONG DataLength,
            # _Out_ PIO_STATUS_BLOCK IoStatus,
            # _In_ ULONG MethodSetsCount,
            # _In_reads_(MethodSetsCount) KSMETHOD_SET* MethodSet
            # );
            KsFastMethodHandler = ks.KsFastMethodHandler
            KsFastMethodHandler.restype = BOOLEAN

            # alloc.c:
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsCreateDefaultAllocator(
            # _In_ PIRP Irp
            # );
            KsCreateDefaultAllocator = ks.KsCreateDefaultAllocator
            KsCreateDefaultAllocator.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsCreateDefaultAllocatorEx(
            # _In_ PIRP Irp,
            # _In_opt_ PVOID InitializeContext,
            # _In_opt_ PFNKSDEFAULTALLOCATE DefaultAllocate,
            # _In_opt_ PFNKSDEFAULTFREE DefaultFree,
            # _In_opt_ PFNKSINITIALIZEALLOCATOR InitializeAllocator,
            # _In_opt_ PFNKSDELETEALLOCATOR DeleteAllocator
            # );
            KsCreateDefaultAllocatorEx = ks.KsCreateDefaultAllocatorEx
            KsCreateDefaultAllocatorEx.restype = NTSTATUS

            ksuser = ctypes.windll.KSUSER
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsCreateAllocator(
            # _In_ HANDLE ConnectionHandle,
            # _In_ PKSALLOCATOR_FRAMING AllocatorFraming,
            # _Out_ PHANDLE AllocatorHandle
            # );
            KsCreateAllocator = ksuser.KsCreateAllocator
            KsCreateAllocator.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsValidateAllocatorCreateRequest(
            # _In_ PIRP Irp,
            # _Out_ PKSALLOCATOR_FRAMING* AllocatorFraming
            # );
            KsValidateAllocatorCreateRequest = (
                ks.KsValidateAllocatorCreateRequest
            )
            KsValidateAllocatorCreateRequest.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsValidateAllocatorFramingEx(
            # _In_ PKSALLOCATOR_FRAMING_EX Framing,
            # _In_ ULONG BufferSize,
            # _In_ KSALLOCATOR_FRAMING_EX *PinFraming
            # );
            KsValidateAllocatorFramingEx = ks.KsValidateAllocatorFramingEx
            KsValidateAllocatorFramingEx.restype = NTSTATUS

            # clock.c:
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsAllocateDefaultClock(
            # _Out_ PKSDEFAULTCLOCK* DefaultClock
            # );
            KsAllocateDefaultClock = ks.KsAllocateDefaultClock
            KsAllocateDefaultClock.restype = NTSTATUS

            if NTDDI_VERSION >= NTDDI_WINXP:
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsAllocateDefaultClockEx(
                # _Out_ PKSDEFAULTCLOCK* DefaultClock,
                # _In_opt_ PVOID Context,
                # _In_opt_ PFNKSSETTIMER SetTimer,
                # _In_opt_ PFNKSCANCELTIMER CancelTimer,
                # _In_opt_ PFNKSCORRELATEDTIME CorrelatedTime,
                # _In_opt_ KSRESOLUTION* Resolution,
                # _In_ ULONG Flags
                # );
                KsAllocateDefaultClockEx = ks.KsAllocateDefaultClockEx
                KsAllocateDefaultClockEx.restype = NTSTATUS

            # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsFreeDefaultClock(
            # _In_ PKSDEFAULTCLOCK DefaultClock
            # );
            KsFreeDefaultClock = ks.KsFreeDefaultClock
            KsFreeDefaultClock.restype = VOID

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsCreateDefaultClock(
            # _In_ PIRP Irp,
            # _In_ PKSDEFAULTCLOCK DefaultClock
            # );
            KsCreateDefaultClock = ks.KsCreateDefaultClock
            KsCreateDefaultClock.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsCreateClock(
            # _In_ HANDLE ConnectionHandle,
            # _In_ PKSCLOCK_CREATE ClockCreate,
            # _Out_ PHANDLE ClockHandle
            # );
            KsCreateClock = ksuser.KsCreateClock
            KsCreateClock.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsValidateClockCreateRequest(
            # _In_ PIRP Irp,
            # _Outptr_ PKSCLOCK_CREATE* ClockCreate
            # );
            KsValidateClockCreateRequest = ks.KsValidateClockCreateRequest
            KsValidateClockCreateRequest.restype = NTSTATUS

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # KSSTATE
            # NTAPI
            # KsGetDefaultClockState(
            # _In_ PKSDEFAULTCLOCK DefaultClock
            # );
            KsGetDefaultClockState = ks.KsGetDefaultClockState
            KsGetDefaultClockState.restype = KSSTATE

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsSetDefaultClockState(
            # _In_ PKSDEFAULTCLOCK DefaultClock,
            # _In_ KSSTATE State
            # );
            KsSetDefaultClockState = ks.KsSetDefaultClockState
            KsSetDefaultClockState.restype = VOID

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # LONGLONG
            # NTAPI
            # KsGetDefaultClockTime(
            # _In_ PKSDEFAULTCLOCK DefaultClock
            # );
            KsGetDefaultClockTime = ks.KsGetDefaultClockTime
            KsGetDefaultClockTime.restype = LONGLONG

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsSetDefaultClockTime(
            # _In_ PKSDEFAULTCLOCK DefaultClock,
            # _In_ LONGLONG Time
            # );
            KsSetDefaultClockTime = ks.KsSetDefaultClockTime
            KsSetDefaultClockTime.restype = VOID

            # connect.c:
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsCreatePin(
            # _In_ HANDLE FilterHandle,
            # _In_ PKSPIN_CONNECT Connect,
            # _In_ ACCESS_MASK DesiredAccess,
            # _Out_ PHANDLE ConnectionHandle
            # );
            KsCreatePin = ksuser.KsCreatePin
            KsCreatePin.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsValidateConnectRequest(
            # _In_ PIRP Irp,
            # _In_ ULONG DescriptorsCount,
            # _In_reads_(DescriptorsCount) KSPIN_DESCRIPTOR* Descriptor,
            # _Out_ PKSPIN_CONNECT* Connect
            # );
            KsValidateConnectRequest = ks.KsValidateConnectRequest
            KsValidateConnectRequest.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsPinPropertyHandler(
            # _In_ PIRP Irp,
            # _In_ PKSPROPERTY Property,
            # _Inout_ PVOID Data,
            # _In_ ULONG DescriptorsCount,
            # _In_reads_(DescriptorsCount) KSPIN_DESCRIPTOR* Descriptor
            # );
            KsPinPropertyHandler = ks.KsPinPropertyHandler
            KsPinPropertyHandler.restype = NTSTATUS

            # _Must_inspect_result_
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsPinDataIntersection(
            # _In_ PIRP Irp,
            # _In_ PKSP_PIN Pin,
            # _Out_opt_ PVOID Data,
            # _In_ ULONG DescriptorsCount,
            # _In_reads_(DescriptorsCount) KSPIN_DESCRIPTOR* Descriptor,
            # _In_ PFNKSINTERSECTHANDLER IntersectHandler
            # );
            KsPinDataIntersection = ks.KsPinDataIntersection
            KsPinDataIntersection.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsHandleSizedListQuery(
            # _In_ PIRP Irp,
            # _In_ ULONG DataItemsCount,
            # _In_ ULONG DataItemSize,
            # _In_reads_bytes_(DataItemsCount * DataItemSize) VOID* DataItems
            # );
            KsHandleSizedListQuery = ks.KsHandleSizedListQuery
            KsHandleSizedListQuery.restype = NTSTATUS

            # image.c:
            if not defined(MAKEINTRESOURCE):
                def MAKEINTRESOURCE(res):
                    return ULONG_PTR(res).value

            # END IF


            if not defined(RT_STRING):
                RT_STRING = MAKEINTRESOURCE(6)
                RT_RCDATA = MAKEINTRESOURCE(10)
            # END IF


            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsLoadResource(
            # _In_ PVOID ImageBase,
            # _In_ POOL_TYPE PoolType,
            # _In_ ULONG_PTR ResourceName,
            # _In_ ULONG ResourceType,
            # _Outptr_result_bytebuffer_(*ResourceSize) PVOID *Resource,
            # _Out_opt_ PULONG ResourceSize
            # );
            KsLoadResource = ks.KsLoadResource
            KsLoadResource.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsGetImageNameAndResourceId(
            # _In_ HANDLE RegKey,
            # _Out_ PUNICODE_STRING ImageName,
            # _Out_ PULONG_PTR ResourceId,
            # _Out_ PULONG ValueType
            # );
            KsGetImageNameAndResourceId = ks.KsGetImageNameAndResourceId
            KsGetImageNameAndResourceId.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsMapModuleName(
            # _In_ PDEVICE_OBJECT PhysicalDeviceObject,
            # _In_ PUNICODE_STRING ModuleName,
            # _Out_ PUNICODE_STRING ImageName,
            # _Out_ PULONG_PTR ResourceId,
            # _Out_ PULONG ValueType
            # );
            KsMapModuleName = ks.KsMapModuleName
            KsMapModuleName.restype = NTSTATUS

            # irp.c:
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsReferenceBusObject(
            # _In_ KSDEVICE_HEADER  Header
            # );
            KsReferenceBusObject = ks.KsReferenceBusObject
            KsReferenceBusObject.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsDereferenceBusObject(
            # _In_ KSDEVICE_HEADER  Header
            # );
            KsDereferenceBusObject = ks.KsDereferenceBusObject
            KsDereferenceBusObject.restype = VOID

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsDispatchQuerySecurity(
            # _In_ PDEVICE_OBJECT DeviceObject,
            # _In_ PIRP Irp
            # );
            KsDispatchQuerySecurity = ks.KsDispatchQuerySecurity
            KsDispatchQuerySecurity.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsDispatchSetSecurity(
            # _In_ PDEVICE_OBJECT DeviceObject,
            # _In_ PIRP Irp
            # );
            KsDispatchSetSecurity = ks.KsDispatchSetSecurity
            KsDispatchSetSecurity.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsDispatchSpecificProperty(
            # _In_ PIRP Irp,
            # _In_ PFNKSHANDLER Handler
            # );
            KsDispatchSpecificProperty = ks.KsDispatchSpecificProperty
            KsDispatchSpecificProperty.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsDispatchSpecificMethod(
            # _In_ PIRP Irp,
            # _In_ PFNKSHANDLER Handler
            # );
            KsDispatchSpecificMethod = ks.KsDispatchSpecificMethod
            KsDispatchSpecificMethod.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsReadFile(
            # _In_ PFILE_OBJECT FileObject,
            # _In_opt_ PKEVENT Event,
            # _In_opt_ PVOID PortContext,
            # _Out_ PIO_STATUS_BLOCK IoStatusBlock,
            # _Out_writes_bytes_(Length) PVOID Buffer,
            # _In_ ULONG Length,
            # _In_ ULONG Key OPTIONAL,
            # _In_ KPROCESSOR_MODE RequestorMode
            # );
            KsReadFile = ks.KsReadFile
            KsReadFile.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsWriteFile(
            # _In_ PFILE_OBJECT FileObject,
            # _In_opt_ PKEVENT Event,
            # _In_opt_ PVOID PortContext,
            # _Out_ PIO_STATUS_BLOCK IoStatusBlock,
            # _In_reads_bytes_(Length) PVOID Buffer,
            # _In_ ULONG Length,
            # _In_ ULONG Key OPTIONAL,
            # _In_ KPROCESSOR_MODE RequestorMode
            # );
            KsWriteFile = ks.KsWriteFile
            KsWriteFile.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsQueryInformationFile(
            # _In_ PFILE_OBJECT FileObject,
            # _Out_writes_bytes_(Length) PVOID FileInformation,
            # _In_ ULONG Length,
            # _In_ FILE_INFORMATION_CLASS FileInformationClass
            # );
            KsQueryInformationFile = ks.KsQueryInformationFile
            KsQueryInformationFile.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsSetInformationFile(
            # _In_ PFILE_OBJECT FileObject,
            # _In_reads_bytes_(Length) PVOID FileInformation,
            # _In_ ULONG Length,
            # _In_ FILE_INFORMATION_CLASS FileInformationClass
            # );
            KsSetInformationFile = ks.KsSetInformationFile
            KsSetInformationFile.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsStreamIo(
            # _In_ PFILE_OBJECT FileObject,
            # _In_opt_ PKEVENT Event,
            # _In_opt_ PVOID PortContext,
            # _In_opt_ PIO_COMPLETION_ROUTINE CompletionRoutine,
            # _In_opt_ PVOID CompletionContext,
            # _In_ KSCOMPLETION_INVOCATION CompletionInvocationFlags OPTIONAL,
            # _Out_ PIO_STATUS_BLOCK IoStatusBlock,
            # _Inout_updates_bytes_(Length) PVOID StreamHeaders,
            # _In_ ULONG Length,
            # _In_ ULONG Flags,
            # _In_ KPROCESSOR_MODE RequestorMode
            # );
            KsStreamIo = ks.KsStreamIo
            KsStreamIo.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsProbeStreamIrp(
            # _Inout_ PIRP Irp,
            # _In_ ULONG ProbeFlags,
            # _In_ ULONG HeaderSize OPTIONAL
            # );
            KsProbeStreamIrp = ks.KsProbeStreamIrp
            KsProbeStreamIrp.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsAllocateExtraData(
            # _Inout_ PIRP Irp,
            # _In_ ULONG ExtraSize,
            # _Out_ PVOID* ExtraBuffer
            # );
            KsAllocateExtraData = ks.KsAllocateExtraData
            KsAllocateExtraData.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsNullDriverUnload(
            # _In_ PDRIVER_OBJECT DriverObject
            # );
            KsNullDriverUnload = ks.KsNullDriverUnload
            KsNullDriverUnload.restype = VOID

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsSetMajorFunctionHandler(
            # _In_ PDRIVER_OBJECT DriverObject,
            # _In_ ULONG MajorFunction
            # );
            KsSetMajorFunctionHandler = ks.KsSetMajorFunctionHandler
            KsSetMajorFunctionHandler.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsDispatchInvalidDeviceRequest(
            # _In_ PDEVICE_OBJECT DeviceObject,
            # _In_ PIRP Irp
            # );
            KsDispatchInvalidDeviceRequest = ks.KsDispatchInvalidDeviceRequest
            KsDispatchInvalidDeviceRequest.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsDefaultDeviceIoCompletion(
            # _In_ PDEVICE_OBJECT DeviceObject,
            # _In_ PIRP Irp
            # );
            KsDefaultDeviceIoCompletion = ks.KsDefaultDeviceIoCompletion
            KsDefaultDeviceIoCompletion.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsDispatchIrp(
            # _In_ PDEVICE_OBJECT DeviceObject,
            # _In_ PIRP Irp
            # );
            KsDispatchIrp = ks.KsDispatchIrp
            KsDispatchIrp.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # BOOLEAN
            # NTAPI
            # KsDispatchFastIoDeviceControlFailure(
            # _In_ PFILE_OBJECT FileObject,
            # _In_ BOOLEAN Wait,
            # _In_reads_bytes_opt_(InputBufferLength) PVOID InputBuffer,
            # _In_ ULONG InputBufferLength,
            # _Out_writes_bytes_opt_(OutputBufferLength) PVOID OutputBuffer,
            # _In_ ULONG OutputBufferLength,
            # _In_ ULONG IoControlCode,
            # _Out_ PIO_STATUS_BLOCK IoStatus,
            # _In_ PDEVICE_OBJECT DeviceObject
            # );
            KsDispatchFastIoDeviceControlFailure = (
                ks.KsDispatchFastIoDeviceControlFailure
            )
            KsDispatchFastIoDeviceControlFailure.restype = BOOLEAN

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # BOOLEAN
            # NTAPI
            # KsDispatchFastReadFailure(
            # _In_ PFILE_OBJECT FileObject,
            # _In_ PLARGE_INTEGER FileOffset,
            # _In_ ULONG Length,
            # _In_ BOOLEAN Wait,
            # _In_ ULONG LockKey,
            # _Out_ PVOID Buffer,
            # _Out_ PIO_STATUS_BLOCK IoStatus,
            # _In_ PDEVICE_OBJECT DeviceObject
            # );
            KsDispatchFastReadFailure = ks.KsDispatchFastReadFailure
            KsDispatchFastReadFailure.restype = BOOLEAN

            KsDispatchFastWriteFailure = KsDispatchFastReadFailure

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsCancelIo(
            # _Inout_ PLIST_ENTRY  QueueHead,
            # _In_ PKSPIN_LOCK SpinLock
            # );
            KsCancelIo = ks.KsCancelIo
            KsCancelIo.restype = VOID

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsReleaseIrpOnCancelableQueue(
            # _In_ PIRP Irp,
            # _In_opt_ PDRIVER_CANCEL DriverCancel
            # );
            KsReleaseIrpOnCancelableQueue = ks.KsReleaseIrpOnCancelableQueue
            KsReleaseIrpOnCancelableQueue.restype = VOID

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # PIRP
            # NTAPI
            # KsRemoveIrpFromCancelableQueue(
            # _Inout_ PLIST_ENTRY QueueHead,
            # _In_ PKSPIN_LOCK SpinLock,
            # _In_ KSLIST_ENTRY_LOCATION ListLocation,
            # _In_ KSIRP_REMOVAL_OPERATION RemovalOperation
            # );
            KsRemoveIrpFromCancelableQueue = ks.KsRemoveIrpFromCancelableQueue
            KsRemoveIrpFromCancelableQueue.restype = PIRP

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsMoveIrpsOnCancelableQueue(
            # _Inout_ PLIST_ENTRY SourceList,
            # _In_ PKSPIN_LOCK SourceLock,
            # _Inout_ PLIST_ENTRY DestinationList,
            # _In_opt_ PKSPIN_LOCK DestinationLock,
            # _In_ KSLIST_ENTRY_LOCATION ListLocation,
            # _In_ PFNKSIRPLISTCALLBACK ListCallback,
            # _In_ PVOID Context
            # );
            KsMoveIrpsOnCancelableQueue = ks.KsMoveIrpsOnCancelableQueue
            KsMoveIrpsOnCancelableQueue.restype = NTSTATUS

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsRemoveSpecificIrpFromCancelableQueue(
            # _In_ PIRP Irp
            # );
            KsRemoveSpecificIrpFromCancelableQueue = (
                ks.KsRemoveSpecificIrpFromCancelableQueue
            )
            KsRemoveSpecificIrpFromCancelableQueue.restype = VOID

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsAddIrpToCancelableQueue(
            # _Inout_ PLIST_ENTRY QueueHead,
            # _In_ PKSPIN_LOCK SpinLock,
            # _In_ PIRP Irp,
            # _In_ KSLIST_ENTRY_LOCATION ListLocation,
            # _In_opt_ PDRIVER_CANCEL DriverCancel
            # );
            KsAddIrpToCancelableQueue = ks.KsAddIrpToCancelableQueue
            KsAddIrpToCancelableQueue.restype = VOID

            # api.c:
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsAcquireResetValue(
            # _In_ PIRP Irp,
            # _Out_ KSRESET* ResetValue
            # );
            KsAcquireResetValue = ks.KsAcquireResetValue
            KsAcquireResetValue.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsTopologyPropertyHandler(
            # _In_ PIRP Irp,
            # _In_ PKSPROPERTY Property,
            # _Inout_ PVOID Data,
            # _In_ KSTOPOLOGY* Topology
            # );
            KsTopologyPropertyHandler = ks.KsTopologyPropertyHandler
            KsTopologyPropertyHandler.restype = NTSTATUS

            # _IRQL_requires_max_(APC_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsAcquireDeviceSecurityLock(
            # _In_ KSDEVICE_HEADER Header,
            # _In_ BOOLEAN Exclusive
            # );
            KsAcquireDeviceSecurityLock = ks.KsAcquireDeviceSecurityLock
            KsAcquireDeviceSecurityLock.restype = VOID

            # _IRQL_requires_max_(APC_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsReleaseDeviceSecurityLock(
            # _In_ KSDEVICE_HEADER Header
            # );
            KsReleaseDeviceSecurityLock = ks.KsReleaseDeviceSecurityLock
            KsReleaseDeviceSecurityLock.restype = VOID

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsSetDevicePnpAndBaseObject(
            # _In_ KSDEVICE_HEADER Header,
            # _In_ PDEVICE_OBJECT PnpDeviceObject,
            # _In_ PDEVICE_OBJECT BaseObject
            # );
            KsSetDevicePnpAndBaseObject = ks.KsSetDevicePnpAndBaseObject
            KsSetDevicePnpAndBaseObject.restype = VOID

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # PDEVICE_OBJECT
            # NTAPI
            # KsQueryDevicePnpObject(
            # _In_ KSDEVICE_HEADER Header
            # );
            KsQueryDevicePnpObject = ks.KsQueryDevicePnpObject
            KsQueryDevicePnpObject.restype = PDEVICE_OBJECT

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # ACCESS_MASK
            # NTAPI
            # KsQueryObjectAccessMask(
            # _In_ KSOBJECT_HEADER Header
            # );
            KsQueryObjectAccessMask = ks.KsQueryObjectAccessMask
            KsQueryObjectAccessMask.restype = ACCESS_MASK

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsRecalculateStackDepth(
            # _In_ KSDEVICE_HEADER Header,
            # _In_ BOOLEAN ReuseStackLocation
            # );
            KsRecalculateStackDepth = ks.KsRecalculateStackDepth
            KsRecalculateStackDepth.restype = VOID

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsSetTargetState(
            # _In_ KSOBJECT_HEADER Header,
            # _In_ KSTARGET_STATE TargetState
            # );
            KsSetTargetState = ks.KsSetTargetState
            KsSetTargetState.restype = VOID

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsSetTargetDeviceObject(
            # _In_ KSOBJECT_HEADER Header,
            # _In_opt_ PDEVICE_OBJECT TargetDevice
            # );
            KsSetTargetDeviceObject = ks.KsSetTargetDeviceObject
            KsSetTargetDeviceObject.restype = VOID

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsSetPowerDispatch(
            # _In_ KSOBJECT_HEADER Header,
            # _In_opt_ PFNKSCONTEXT_DISPATCH PowerDispatch,
            # _In_opt_ PVOID PowerContext
            # );
            KsSetPowerDispatch = ks.KsSetPowerDispatch
            KsSetPowerDispatch.restype = VOID

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # PKSOBJECT_CREATE_ITEM
            # NTAPI
            # KsQueryObjectCreateItem(
            # _In_ KSOBJECT_HEADER Header
            # );
            KsQueryObjectCreateItem = ks.KsQueryObjectCreateItem
            KsQueryObjectCreateItem.restype = PKSOBJECT_CREATE_ITEM

            # _IRQL_requires_max_(APC_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsAllocateDeviceHeader(
            # _Out_ KSDEVICE_HEADER* Header,
            # _In_ ULONG ItemsCount,
            # _In_reads_opt_(ItemsCount) PKSOBJECT_CREATE_ITEM ItemsList
            # );
            KsAllocateDeviceHeader = ks.KsAllocateDeviceHeader
            KsAllocateDeviceHeader.restype = NTSTATUS

            # _IRQL_requires_max_(APC_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsFreeDeviceHeader(
            # _In_ KSDEVICE_HEADER Header
            # );
            KsFreeDeviceHeader = ks.KsFreeDeviceHeader
            KsFreeDeviceHeader.restype = VOID

            # _IRQL_requires_max_(APC_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsAllocateObjectHeader(
            # _Out_ KSOBJECT_HEADER* Header,
            # _In_ ULONG ItemsCount,
            # _In_reads_opt_(ItemsCount) PKSOBJECT_CREATE_ITEM ItemsList,
            # _In_ PIRP Irp,
            # _In_ KSDISPATCH_TABLE* Table
            # );
            KsAllocateObjectHeader = ks.KsAllocateObjectHeader
            KsAllocateObjectHeader.restype = NTSTATUS

            # _IRQL_requires_max_(APC_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsFreeObjectHeader(
            # _In_ KSOBJECT_HEADER Header
            # );
            KsFreeObjectHeader = ks.KsFreeObjectHeader
            KsFreeObjectHeader.restype = VOID

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsAddObjectCreateItemToDeviceHeader(
            # _In_ KSDEVICE_HEADER Header,
            # _In_ PDRIVER_DISPATCH Create,
            # _In_ PVOID Context,
            # _In_ PWSTR ObjectClass,
            # _In_opt_ PSECURITY_DESCRIPTOR SecurityDescriptor
            # );
            KsAddObjectCreateItemToDeviceHeader = (
                ks.KsAddObjectCreateItemToDeviceHeader
            )
            KsAddObjectCreateItemToDeviceHeader.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsAddObjectCreateItemToObjectHeader(
            # _In_ KSOBJECT_HEADER Header,
            # _In_ PDRIVER_DISPATCH Create,
            # _In_ PVOID Context,
            # _In_ PWSTR ObjectClass,
            # _In_opt_ PSECURITY_DESCRIPTOR SecurityDescriptor
            # );
            KsAddObjectCreateItemToObjectHeader = (
                ks.KsAddObjectCreateItemToObjectHeader
            )
            KsAddObjectCreateItemToObjectHeader.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsAllocateObjectCreateItem(
            # _In_ KSDEVICE_HEADER Header,
            # _In_ PKSOBJECT_CREATE_ITEM CreateItem,
            # _In_ BOOLEAN AllocateEntry,
            # _In_opt_ PFNKSITEMFREECALLBACK ItemFreeCallback
            # );
            KsAllocateObjectCreateItem = ks.KsAllocateObjectCreateItem
            KsAllocateObjectCreateItem.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsFreeObjectCreateItem(
            # _In_ KSDEVICE_HEADER Header,
            # _In_ PUNICODE_STRING CreateItem
            # );
            KsFreeObjectCreateItem = ks.KsFreeObjectCreateItem
            KsFreeObjectCreateItem.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsFreeObjectCreateItemsByContext(
            # _In_ KSDEVICE_HEADER Header,
            # _In_ PVOID Context
            # );
            KsFreeObjectCreateItemsByContext = (
                ks.KsFreeObjectCreateItemsByContext
            )
            KsFreeObjectCreateItemsByContext.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsCreateDefaultSecurity(
            # _In_opt_ PSECURITY_DESCRIPTOR ParentSecurity,
            # _Out_ PSECURITY_DESCRIPTOR* DefaultSecurity
            # );
            KsCreateDefaultSecurity = ks.KsCreateDefaultSecurity
            KsCreateDefaultSecurity.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsForwardIrp(
            # _In_ PIRP Irp,
            # _In_ PFILE_OBJECT FileObject,
            # _In_ BOOLEAN ReuseStackLocation
            # );
            KsForwardIrp = ks.KsForwardIrp
            KsForwardIrp.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsForwardAndCatchIrp(
            # _In_ PDEVICE_OBJECT DeviceObject,
            # _In_ PIRP Irp,
            # _In_ PFILE_OBJECT FileObject,
            # _In_ KSSTACK_USE StackUse
            # );
            KsForwardAndCatchIrp = ks.KsForwardAndCatchIrp
            KsForwardAndCatchIrp.restype = NTSTATUS

            # _Must_inspect_result_
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsSynchronousIoControlDevice(
            # _In_ PFILE_OBJECT FileObject,
            # _In_ KPROCESSOR_MODE RequestorMode,
            # _In_ ULONG IoControl,
            # _In_reads_bytes_(InSize) PVOID InBuffer,
            # _In_ ULONG InSize,
            # _Out_writes_bytes_to_(OutSize, *BytesReturned) PVOID OutBuffer,
            # _In_ ULONG OutSize,
            # _Out_ PULONG BytesReturned
            # );
            KsSynchronousIoControlDevice = ks.KsSynchronousIoControlDevice
            KsSynchronousIoControlDevice.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsUnserializeObjectPropertiesFromRegistry(
            # _In_ PFILE_OBJECT FileObject,
            # _In_opt_ HANDLE ParentKey,
            # _In_opt_ PUNICODE_STRING RegistryPath
            # );
            KsUnserializeObjectPropertiesFromRegistry = (
                ks.KsUnserializeObjectPropertiesFromRegistry
            )
            KsUnserializeObjectPropertiesFromRegistry.restype = NTSTATUS

            if NTDDI_VERSION >= NTDDI_WINXP:
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsCacheMedium(
                # _In_ PUNICODE_STRING SymbolicLink,
                # _In_ PKSPIN_MEDIUM Medium,
                # _In_ ULONG PinDirection
                # );
                KsCacheMedium = ks.KsCacheMedium
                KsCacheMedium.restype = NTSTATUS

            # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

            # thread.c:
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsRegisterWorker(
            # _In_ WORK_QUEUE_TYPE WorkQueueType,
            # _Out_ PKSWORKER* Worker
            # );
            KsRegisterWorker = ks.KsRegisterWorker
            KsRegisterWorker.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsRegisterCountedWorker(
            # _In_ WORK_QUEUE_TYPE WorkQueueType,
            # _Inout_ PWORK_QUEUE_ITEM CountedWorkItem,
            # _Out_ PKSWORKER* Worker
            # );
            KsRegisterCountedWorker = ks.KsRegisterCountedWorker
            KsRegisterCountedWorker.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # VOID
            # NTAPI
            # KsUnregisterWorker(
            # _Inout_ PKSWORKER Worker
            # );
            KsUnregisterWorker = ks.KsUnregisterWorker
            KsUnregisterWorker.restype = VOID

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsQueueWorkItem(
            # _Inout_ PKSWORKER Worker,
            # _Inout_ PWORK_QUEUE_ITEM WorkItem
            # );
            KsQueueWorkItem = ks.KsQueueWorkItem
            KsQueueWorkItem.restype = NTSTATUS

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # ULONG
            # NTAPI
            # KsIncrementCountedWorker(
            # _Inout_ PKSWORKER Worker
            # );
            KsIncrementCountedWorker = ks.KsIncrementCountedWorker
            KsIncrementCountedWorker.restype = ULONG

            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # KSDDKAPI
            # ULONG
            # NTAPI
            # KsDecrementCountedWorker(
            # _Inout_ PKSWORKER Worker
            # );
            KsDecrementCountedWorker = ks.KsDecrementCountedWorker
            KsDecrementCountedWorker.restype = ULONG

            # topology.c:
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsCreateTopologyNode(
            # _In_ HANDLE ParentHandle,
            # _In_ PKSNODE_CREATE NodeCreate,
            # _In_ ACCESS_MASK DesiredAccess,
            # _Out_ PHANDLE NodeHandle
            # );
            KsCreateTopologyNode = ks.KsCreateTopologyNode
            KsCreateTopologyNode.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # NTAPI
            # KsValidateTopologyNodeCreateRequest(
            # _In_ PIRP Irp,
            # _In_ PKSTOPOLOGY Topology,
            # _Out_ PKSNODE_CREATE* NodeCreate
            # );
            KsValidateTopologyNodeCreateRequest = (
                ks.KsValidateTopologyNodeCreateRequest
            )
            KsValidateTopologyNodeCreateRequest.restype = NTSTATUS

            if NTDDI_VERSION >= NTDDI_WINXP:
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsMergeAutomationTables(
                # _Out_ PKSAUTOMATION_TABLE* AutomationTableAB,
                # _In_opt_ PKSAUTOMATION_TABLE AutomationTableA,
                # _In_opt_ PKSAUTOMATION_TABLE AutomationTableB,
                # _In_opt_ KSOBJECT_BAG Bag
                # );
                KsMergeAutomationTables = ks.KsMergeAutomationTables
                KsMergeAutomationTables.restype = NTSTATUS

                # _Must_inspect_result_
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsInitializeDriver(
                # _In_ PDRIVER_OBJECT DriverObject,
                # _In_ PUNICODE_STRING RegistryPathName,
                # _In_opt_ KSDEVICE_DESCRIPTOR* Descriptor
                # );
                KsInitializeDriver = ks.KsInitializeDriver
                KsInitializeDriver.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsAddDevice(
                # _In_ PDRIVER_OBJECT DriverObject,
                # _In_ PDEVICE_OBJECT PhysicalDeviceObject
                # );
                KsAddDevice = ks.KsAddDevice
                KsAddDevice.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsCreateDevice(
                # _In_ PDRIVER_OBJECT DriverObject,
                # _In_ PDEVICE_OBJECT PhysicalDeviceObject,
                # _In_opt_ KSDEVICE_DESCRIPTOR* Descriptor,
                # _In_ ULONG ExtensionSize,
                # _Out_opt_ PKSDEVICE* Device
                # );
                KsCreateDevice = ks.KsCreateDevice
                KsCreateDevice.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsInitializeDevice(
                # _In_ PDEVICE_OBJECT FunctionalDeviceObject,
                # _In_ PDEVICE_OBJECT PhysicalDeviceObject,
                # _In_ PDEVICE_OBJECT NextDeviceObject,
                # _In_opt_ KSDEVICE_DESCRIPTOR* Descriptor
                # );
                KsInitializeDevice = ks.KsInitializeDevice
                KsInitializeDevice.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsTerminateDevice(
                # _In_ PDEVICE_OBJECT DeviceObject
                # );
                KsTerminateDevice = ks.KsTerminateDevice
                KsTerminateDevice.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # PKSDEVICE
                # NTAPI
                # KsGetDeviceForDeviceObject(
                # _In_ PDEVICE_OBJECT FunctionalDeviceObject
                # );
                KsGetDeviceForDeviceObject = ks.KsGetDeviceForDeviceObject
                KsGetDeviceForDeviceObject.restype = PKSDEVICE

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsAcquireDevice(
                # _In_ PKSDEVICE Device
                # );
                KsAcquireDevice = ks.KsAcquireDevice
                KsAcquireDevice.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsReleaseDevice(
                # _In_ PKSDEVICE Device
                # );
                KsReleaseDevice = ks.KsReleaseDevice
                KsReleaseDevice.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsDeviceRegisterAdapterObject(
                # _In_ PKSDEVICE Device,
                # _In_ PADAPTER_OBJECT AdapterObject,
                # _In_ ULONG MaxMappingsByteCount,
                # _In_ ULONG MappingTableStride
                # );
                KsDeviceRegisterAdapterObject = (
                    ks.KsDeviceRegisterAdapterObject
                )
                KsDeviceRegisterAdapterObject.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # ULONG
                # NTAPI
                # KsDeviceGetBusData(
                # _In_ PKSDEVICE Device,
                # _In_ ULONG DataType,
                # _In_reads_bytes_(Length) PVOID Buffer,
                # _In_ ULONG Offset,
                # _In_ ULONG Length
                # );
                KsDeviceGetBusData = ks.KsDeviceGetBusData
                KsDeviceGetBusData.restype = ULONG

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # ULONG
                # NTAPI
                # KsDeviceSetBusData(
                # _In_ PKSDEVICE Device,
                # _In_ ULONG DataType,
                # _In_reads_bytes_(Length) PVOID Buffer,
                # _In_ ULONG Offset,
                # _In_ ULONG Length
                # );
                KsDeviceSetBusData = ks.KsDeviceSetBusData
                KsDeviceSetBusData.restype = ULONG

                # _Must_inspect_result_
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsCreateFilterFactory(
                # _In_ PDEVICE_OBJECT DeviceObject,
                # _In_ KSFILTER_DESCRIPTOR *Descriptor,
                # _In_opt_ PWSTR RefString,
                # _In_opt_ PSECURITY_DESCRIPTOR SecurityDescriptor,
                # _In_ ULONG CreateItemFlags,
                # _In_opt_ PFNKSFILTERFACTORYPOWER SleepCallback,
                # _In_opt_ PFNKSFILTERFACTORYPOWER WakeCallback,
                # _Out_opt_ PKSFILTERFACTORY *FilterFactory
                # );
                KsCreateFilterFactory = ks.KsCreateFilterFactory
                KsCreateFilterFactory.restype = NTSTATUS

                def KsDeleteFilterFactory(FilterFactory):
                    KsFreeObjectCreateItemsByContext(
                        POINTER(KSDEVICE_HEADER)(
                            KsFilterFactoryGetParentDevice(
                                FilterFactory
                            ).FunctionalDeviceObject.DeviceExtension
                        ),
                        FilterFactory
                    )

                # _Must_inspect_result_
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsFilterFactoryUpdateCacheData(
                # _In_ PKSFILTERFACTORY FilterFactory,
                # _In_opt_ KSFILTER_DESCRIPTOR *FilterDescriptor
                # );
                KsFilterFactoryUpdateCacheData = (
                    ks.KsFilterFactoryUpdateCacheData
                )
                KsFilterFactoryUpdateCacheData.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsFilterFactoryAddCreateItem(
                # _In_ PKSFILTERFACTORY FilterFactory,
                # _In_ PWSTR RefString,
                # _In_opt_ PSECURITY_DESCRIPTOR SecurityDescriptor,
                # _In_ ULONG CreateItemFlags
                # );
                KsFilterFactoryAddCreateItem = ks.KsFilterFactoryAddCreateItem
                KsFilterFactoryAddCreateItem.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsFilterFactorySetDeviceClassesState(
                # _In_ PKSFILTERFACTORY FilterFactory,
                # _In_ BOOLEAN NewState
                # );
                KsFilterFactorySetDeviceClassesState = (
                    ks.KsFilterFactorySetDeviceClassesState
                )
                KsFilterFactorySetDeviceClassesState.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # PUNICODE_STRING
                # NTAPI
                # KsFilterFactoryGetSymbolicLink(
                # _In_ PKSFILTERFACTORY FilterFactory
                # );
                KsFilterFactoryGetSymbolicLink = (
                    ks.KsFilterFactoryGetSymbolicLink
                )
                KsFilterFactoryGetSymbolicLink.restype = PUNICODE_STRING

                if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
                    # Forward decl.

                    class _KSDEVICE_PROFILE_INFO(ctypes.Structure):
                        pass


                    KSDEVICE_PROFILE_INFO = _KSDEVICE_PROFILE_INFO
                    PKSDEVICE_PROFILE_INFO = POINTER(_KSDEVICE_PROFILE_INFO)
                # END IF   NTDDI_WINTHRESHOLD

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsAddEvent(
                # _In_ PVOID Object,
                # _In_ PKSEVENT_ENTRY EventEntry
                # );
                KsAddEvent = ks.KsAddEvent
                KsAddEvent.restype = VOID

                # }
                #
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsDefaultAddEventHandler(
                # _In_ PIRP Irp,
                # _In_ PKSEVENTDATA EventData,
                # _Inout_ PKSEVENT_ENTRY EventEntry
                # );
                KsDefaultAddEventHandler = ks.KsDefaultAddEventHandler
                KsDefaultAddEventHandler.restype = NTSTATUS

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsGenerateEvents(
                # _In_ PVOID Object,
                # _In_opt_ GUID* EventSet,
                # _In_ ULONG EventId,
                # _In_ ULONG DataSize,
                # _In_reads_bytes_opt_(DataSize) PVOID Data,
                # _In_opt_ PFNKSGENERATEEVENTCALLBACK CallBack,
                # _In_opt_ PVOID CallBackContext
                # );
                KsGenerateEvents = ks.KsGenerateEvents
                KsGenerateEvents.restype = VOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # VOID _inline
                # KsFilterGenerateEvents(
                # _In_ PKSFILTER Filter,
                # _In_opt_ GUID* EventSet,
                # _In_ ULONG EventId,
                # _In_ ULONG DataSize,
                # _In_reads_bytes_(DataSize) PVOID Data,
                # _In_opt_ PFNKSGENERATEEVENTCALLBACK CallBack,
                # _In_opt_ PVOID CallBackContext
                # )
                # {
                # KsGenerateEvents(
                # Filter,
                # EventSet,
                # EventId,
                # DataSize,
                # Data,
                # CallBack,
                # CallBackContext);
                KsFilterGenerateEvents = ks.KsFilterGenerateEvents
                KsFilterGenerateEvents.restype = VOID

                # }
                #
                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # VOID _inline
                # KsPinGenerateEvents(
                # _In_ PKSPIN Pin,
                # _In_opt_ GUID* EventSet,
                # _In_ ULONG EventId,
                # _In_ ULONG DataSize,
                # _In_reads_bytes_opt_(DataSize) PVOID Data,
                # _In_opt_ PFNKSGENERATEEVENTCALLBACK CallBack,
                # _In_opt_ PVOID CallBackContext
                # )
                # {
                # KsGenerateEvents(
                # Pin,
                # EventSet,
                # EventId,
                # DataSize,
                # Data,
                # CallBack,
                # CallBackContext);
                KsPinGenerateEvents = ks.KsPinGenerateEvents
                KsPinGenerateEvents.restype = VOID


                class KSSTREAM_POINTER_STATE(ENUM):
                    KSSTREAM_POINTER_STATE_UNLOCKED = 0
                    KSSTREAM_POINTER_STATE_LOCKED = 1

                KSSTREAM_POINTER_STATE_UNLOCKED = KSSTREAM_POINTER_STATE.KSSTREAM_POINTER_STATE_UNLOCKED
                KSSTREAM_POINTER_STATE_LOCKED = KSSTREAM_POINTER_STATE.KSSTREAM_POINTER_STATE_LOCKED

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsPinGetAvailableByteCount(
                # _In_ PKSPIN Pin,
                # _Out_opt_ PLONG InputDataBytes,
                # _Out_opt_ PLONG OutputBufferBytes
                # );
                KsPinGetAvailableByteCount = ks.KsPinGetAvailableByteCount
                KsPinGetAvailableByteCount.restype = NTSTATUS

                # _Must_inspect_result_
                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # PKSSTREAM_POINTER
                # NTAPI
                # KsPinGetLeadingEdgeStreamPointer(
                # _In_ PKSPIN Pin,
                # _In_ KSSTREAM_POINTER_STATE State
                # );
                KsPinGetLeadingEdgeStreamPointer = (
                    ks.KsPinGetLeadingEdgeStreamPointer
                )
                KsPinGetLeadingEdgeStreamPointer.restype = PKSSTREAM_POINTER

                # _Must_inspect_result_
                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # PKSSTREAM_POINTER
                # NTAPI
                # KsPinGetTrailingEdgeStreamPointer(
                # _In_ PKSPIN Pin,
                # _In_ KSSTREAM_POINTER_STATE State
                # );
                KsPinGetTrailingEdgeStreamPointer = (
                    ks.KsPinGetTrailingEdgeStreamPointer
                )
                KsPinGetTrailingEdgeStreamPointer.restype = PKSSTREAM_POINTER

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsStreamPointerSetStatusCode(
                # _In_ PKSSTREAM_POINTER StreamPointer,
                # _In_ NTSTATUS Status
                # );
                KsStreamPointerSetStatusCode = ks.KsStreamPointerSetStatusCode
                KsStreamPointerSetStatusCode.restype = NTSTATUS

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsStreamPointerLock(
                # _In_ PKSSTREAM_POINTER StreamPointer
                # );
                KsStreamPointerLock = ks.KsStreamPointerLock
                KsStreamPointerLock.restype = NTSTATUS

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsStreamPointerUnlock(
                # _In_ PKSSTREAM_POINTER StreamPointer,
                # _In_ BOOLEAN Eject
                # );
                KsStreamPointerUnlock = ks.KsStreamPointerUnlock
                KsStreamPointerUnlock.restype = VOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsStreamPointerAdvanceOffsetsAndUnlock(
                # _In_ PKSSTREAM_POINTER StreamPointer,
                # _In_ ULONG InUsed,
                # _In_ ULONG OutUsed,
                # _In_ BOOLEAN Eject
                # );
                KsStreamPointerAdvanceOffsetsAndUnlock = (
                    ks.KsStreamPointerAdvanceOffsetsAndUnlock
                )
                KsStreamPointerAdvanceOffsetsAndUnlock.restype = VOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsStreamPointerDelete(
                # _In_ PKSSTREAM_POINTER StreamPointer
                # );
                KsStreamPointerDelete = ks.KsStreamPointerDelete
                KsStreamPointerDelete.restype = VOID

                # _Must_inspect_result_
                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsStreamPointerClone(
                # _In_ PKSSTREAM_POINTER StreamPointer,
                # _In_opt_ PFNKSSTREAMPOINTER CancelCallback,
                # _In_ ULONG ContextSize,
                # _Out_ PKSSTREAM_POINTER* CloneStreamPointer
                # );
                KsStreamPointerClone = ks.KsStreamPointerClone
                KsStreamPointerClone.restype = NTSTATUS

                # _Must_inspect_result_
                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsStreamPointerAdvanceOffsets(
                # _In_ PKSSTREAM_POINTER StreamPointer,
                # _In_ ULONG InUsed,
                # _In_ ULONG OutUsed,
                # _In_ BOOLEAN Eject
                # );
                KsStreamPointerAdvanceOffsets = (
                    ks.KsStreamPointerAdvanceOffsets
                )
                KsStreamPointerAdvanceOffsets.restype = NTSTATUS

                # _Must_inspect_result_
                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsStreamPointerAdvance(
                # _In_ PKSSTREAM_POINTER StreamPointer
                # );
                KsStreamPointerAdvance = ks.KsStreamPointerAdvance
                KsStreamPointerAdvance.restype = NTSTATUS

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # PMDL
                # NTAPI
                # KsStreamPointerGetMdl(
                # _In_ PKSSTREAM_POINTER StreamPointer
                # );
                KsStreamPointerGetMdl = ks.KsStreamPointerGetMdl
                KsStreamPointerGetMdl.restype = PMDL

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # PIRP
                # NTAPI
                # KsStreamPointerGetIrp(
                # _In_ PKSSTREAM_POINTER StreamPointer,
                # _Out_opt_ PBOOLEAN FirstFrameInIrp,
                # _Out_opt_ PBOOLEAN LastFrameInIrp
                # );
                KsStreamPointerGetIrp = ks.KsStreamPointerGetIrp
                KsStreamPointerGetIrp.restype = PIRP

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsStreamPointerScheduleTimeout(
                # _In_ PKSSTREAM_POINTER StreamPointer,
                # _In_ PFNKSSTREAMPOINTER Callback,
                # _In_ ULONGLONG Interval
                # );
                KsStreamPointerScheduleTimeout = (
                    ks.KsStreamPointerScheduleTimeout
                )
                KsStreamPointerScheduleTimeout.restype = VOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsStreamPointerCancelTimeout(
                # _In_ PKSSTREAM_POINTER StreamPointer
                # );
                KsStreamPointerCancelTimeout = ks.KsStreamPointerCancelTimeout
                KsStreamPointerCancelTimeout.restype = VOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # PKSSTREAM_POINTER
                # NTAPI
                # KsPinGetFirstCloneStreamPointer(
                # _In_ PKSPIN Pin
                # );
                KsPinGetFirstCloneStreamPointer = (
                    ks.KsPinGetFirstCloneStreamPointer
                )
                KsPinGetFirstCloneStreamPointer.restype = PKSSTREAM_POINTER

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # PKSSTREAM_POINTER
                # NTAPI
                # KsStreamPointerGetNextClone(
                # _In_ PKSSTREAM_POINTER StreamPointer
                # );
                KsStreamPointerGetNextClone = ks.KsStreamPointerGetNextClone
                KsStreamPointerGetNextClone.restype = PKSSTREAM_POINTER

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsCompletePendingRequest(
                # _In_ PIRP Irp
                # );
                KsCompletePendingRequest = ks.KsCompletePendingRequest
                KsCompletePendingRequest.restype = VOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # KSOBJECTTYPE
                # NTAPI
                # KsGetObjectTypeFromIrp(
                # _In_ PIRP Irp
                # );
                KsGetObjectTypeFromIrp = ks.KsGetObjectTypeFromIrp
                KsGetObjectTypeFromIrp.restype = KSOBJECTTYPE

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # PVOID
                # NTAPI
                # KsGetObjectFromFileObject(
                # _In_ PFILE_OBJECT FileObject
                # );
                KsGetObjectFromFileObject = ks.KsGetObjectFromFileObject
                KsGetObjectFromFileObject.restype = PVOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # KSOBJECTTYPE
                # NTAPI
                # KsGetObjectTypeFromFileObject(
                # _In_ PFILE_OBJECT FileObject
                # );
                KsGetObjectTypeFromFileObject = (
                    ks.KsGetObjectTypeFromFileObject
                )
                KsGetObjectTypeFromFileObject.restype = KSOBJECTTYPE

                # }
                #
                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # PKSGATE
                # NTAPI
                # KsFilterGetAndGate(
                # _In_ PKSFILTER Filter
                # );
                KsFilterGetAndGate = ks.KsFilterGetAndGate
                KsFilterGetAndGate.restype = PKSGATE

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsFilterAcquireProcessingMutex(
                # _In_ PKSFILTER Filter
                # );
                KsFilterAcquireProcessingMutex = (
                    ks.KsFilterAcquireProcessingMutex
                )
                KsFilterAcquireProcessingMutex.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsFilterReleaseProcessingMutex(
                # _In_ PKSFILTER Filter
                # );
                KsFilterReleaseProcessingMutex = (
                    ks.KsFilterReleaseProcessingMutex
                )
                KsFilterReleaseProcessingMutex.restype = VOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsFilterAttemptProcessing(
                # _In_ PKSFILTER Filter,
                # _In_ BOOLEAN Asynchronous
                # );
                KsFilterAttemptProcessing = ks.KsFilterAttemptProcessing
                KsFilterAttemptProcessing.restype = VOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # PKSGATE
                # NTAPI
                # KsPinGetAndGate(
                # _In_ PKSPIN Pin
                # );
                KsPinGetAndGate = ks.KsPinGetAndGate
                KsPinGetAndGate.restype = PKSGATE

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsPinAttachAndGate(
                # _In_ PKSPIN Pin,
                # _In_opt_ PKSGATE AndGate
                # );
                KsPinAttachAndGate = ks.KsPinAttachAndGate
                KsPinAttachAndGate.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsPinAttachOrGate(
                # _In_ PKSPIN Pin,
                # _In_opt_ PKSGATE OrGate
                # );
                KsPinAttachOrGate = ks.KsPinAttachOrGate
                KsPinAttachOrGate.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsPinAcquireProcessingMutex(
                # _In_ PKSPIN Pin
                # );
                KsPinAcquireProcessingMutex = ks.KsPinAcquireProcessingMutex
                KsPinAcquireProcessingMutex.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsPinReleaseProcessingMutex(
                # _In_ PKSPIN Pin
                # );
                KsPinReleaseProcessingMutex = ks.KsPinReleaseProcessingMutex
                KsPinReleaseProcessingMutex.restype = VOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # BOOLEAN
                # NTAPI
                # KsProcessPinUpdate(
                # _In_ PKSPROCESSPIN ProcessPin
                # );
                KsProcessPinUpdate = ks.KsProcessPinUpdate
                KsProcessPinUpdate.restype = BOOLEAN

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsPinGetCopyRelationships(
                # _In_ PKSPIN Pin,
                # _Out_ PKSPIN* CopySource,
                # _Out_ PKSPIN* DelegateBranch
                # );
                KsPinGetCopyRelationships = ks.KsPinGetCopyRelationships
                KsPinGetCopyRelationships.restype = VOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsPinAttemptProcessing(
                # _In_ PKSPIN Pin,
                # _In_ BOOLEAN Asynchronous
                # );
                KsPinAttemptProcessing = ks.KsPinAttemptProcessing
                KsPinAttemptProcessing.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # PVOID
                # NTAPI
                # KsGetParent(
                # _In_ PVOID Object
                # );
                KsGetParent = ks.KsGetParent
                KsGetParent.restype = PVOID

                # }
                #
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # PKSFILTER
                # NTAPI
                # KsPinGetParentFilter(
                # _In_ PKSPIN Pin
                # );
                KsPinGetParentFilter = ks.KsPinGetParentFilter
                KsPinGetParentFilter.restype = PKSFILTER

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # PVOID
                # NTAPI
                # KsGetFirstChild(
                # _In_ PVOID Object
                # );
                KsGetFirstChild = ks.KsGetFirstChild
                KsGetFirstChild.restype = PVOID

                # }
                #
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # ULONG
                # NTAPI
                # KsFilterGetChildPinCount(
                # _In_ PKSFILTER Filter,
                # _In_ ULONG PinId
                # );
                KsFilterGetChildPinCount = ks.KsFilterGetChildPinCount
                KsFilterGetChildPinCount.restype = ULONG

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # PKSPIN
                # NTAPI
                # KsFilterGetFirstChildPin(
                # _In_ PKSFILTER Filter,
                # _In_ ULONG PinId
                # );
                KsFilterGetFirstChildPin = ks.KsFilterGetFirstChildPin
                KsFilterGetFirstChildPin.restype = PKSPIN

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # PVOID
                # NTAPI
                # KsGetNextSibling(
                # _In_ PVOID Object
                # );
                KsGetNextSibling = ks.KsGetNextSibling
                KsGetNextSibling.restype = PVOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # PKSPIN
                # NTAPI
                # KsPinGetNextSiblingPin(
                # _In_ PKSPIN Pin
                # );
                KsPinGetNextSiblingPin = ks.KsPinGetNextSiblingPin
                KsPinGetNextSiblingPin.restype = PKSPIN

                # }
                #
                #
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # PKSDEVICE
                # NTAPI
                # KsGetDevice(
                # _In_ PVOID Object
                # );
                KsGetDevice = ks.KsGetDevice
                KsGetDevice.restype = PKSDEVICE

                # }
                #
                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # PKSFILTER
                # NTAPI
                # KsGetFilterFromIrp(
                # _In_ PIRP Irp
                # );
                KsGetFilterFromIrp = ks.KsGetFilterFromIrp
                KsGetFilterFromIrp.restype = PKSFILTER

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # PKSPIN
                # NTAPI
                # KsGetPinFromIrp(
                # _In_ PIRP Irp
                # );
                KsGetPinFromIrp = ks.KsGetPinFromIrp
                KsGetPinFromIrp.restype = PKSPIN

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # ULONG
                # NTAPI
                # KsGetNodeIdFromIrp(
                # _In_ PIRP Irp
                # );
                KsGetNodeIdFromIrp = ks.KsGetNodeIdFromIrp
                KsGetNodeIdFromIrp.restype = ULONG

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsAcquireControl(
                # _In_ PVOID Object
                # );
                KsAcquireControl = ks.KsAcquireControl
                KsAcquireControl.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsReleaseControl(
                # _In_ PVOID Object
                # );
                KsReleaseControl = ks.KsReleaseControl
                KsReleaseControl.restype = VOID

                # }
                #
                # _Must_inspect_result_
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsAddItemToObjectBag(
                # _In_ KSOBJECT_BAG ObjectBag,
                # _In_ __drv_aliasesMem PVOID Item,
                # _In_opt_ PFNKSFREE Free
                # );
                KsAddItemToObjectBag = ks.KsAddItemToObjectBag
                KsAddItemToObjectBag.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # ULONG
                # NTAPI
                # KsRemoveItemFromObjectBag(
                # _In_ KSOBJECT_BAG ObjectBag,
                # _In_ PVOID Item,
                # _In_ BOOLEAN Free
                # );
                KsRemoveItemFromObjectBag = ks.KsRemoveItemFromObjectBag
                KsRemoveItemFromObjectBag.restype = ULONG

                def KsDiscard(Object, Pointer):
                    return (
                        KsRemoveItemFromObjectBag(
                            Object.Bag,
                            PVOID(Pointer),
                            TRUE
                        )
                    )

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsAllocateObjectBag(
                # _In_ PKSDEVICE Device,
                # _Out_ KSOBJECT_BAG* ObjectBag
                # );
                KsAllocateObjectBag = ks.KsAllocateObjectBag
                KsAllocateObjectBag.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsFreeObjectBag(
                # _In_ KSOBJECT_BAG ObjectBag
                # );
                KsFreeObjectBag = ks.KsFreeObjectBag
                KsFreeObjectBag.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsCopyObjectBagItems(
                # _In_ KSOBJECT_BAG ObjectBagDestination,
                # _In_ KSOBJECT_BAG ObjectBagSource
                # );
                KsCopyObjectBagItems = ks.KsCopyObjectBagItems
                KsCopyObjectBagItems.restype = NTSTATUS

                # _Must_inspect_result_
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # _KsEdit(
                # _In_ KSOBJECT_BAG ObjectBag,
                # _At_(*PointerToPointerToItem, _Pre_maybenull_  _Pre_readable_byte_size_(OldSize)) _Outptr_result_bytebuffer_(NewSize) PVOID* PointerToPointerToItem,
                # _In_ ULONG NewSize,
                # _In_ ULONG OldSize,
                # _In_ ULONG Tag
                # );
                _KsEdit = ks._KsEdit
                _KsEdit.restype = NTSTATUS

                def KsEdit(Object, PointerToPointer, Tag):
                    return _KsEdit(
                        Object.Bag,
                        PVOID(POINTER(PointerToPointer)),
                        ctypes.sizeof(POINTER(POINTER(PointerToPointer))),
                        ctypes.sizeof(POINTER(POINTER(PointerToPointer))),
                        Tag
                    )


                def KsEditSized(Object, PointerToPointer, NewSize, OldSize, Tag):
                    return _KsEdit(
                        Object.Bag,
                        PVOID(POINTER(PointerToPointer)),
                        NewSize,
                        OldSize,
                        Tag
                    )


                # _Must_inspect_result_
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsRegisterFilterWithNoKSPins(
                # _In_ PDEVICE_OBJECT DeviceObject,
                # _In_ GUID * InterfaceClassGUID,
                # _In_ ULONG PinCount,
                # _In_reads_(PinCount) BOOL * PinDirection,
                # _In_reads_(PinCount) KSPIN_MEDIUM * MediumList,
                # _In_reads_opt_(PinCount) GUID * CategoryList
                # );
                KsRegisterFilterWithNoKSPins = ks.KsRegisterFilterWithNoKSPins
                KsRegisterFilterWithNoKSPins.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsFilterCreatePinFactory(
                # _In_ PKSFILTER Filter,
                # _In_ KSPIN_DESCRIPTOR_EX *const PinDescriptor,
                # _Out_ PULONG PinID
                # );
                KsFilterCreatePinFactory = ks.KsFilterCreatePinFactory
                KsFilterCreatePinFactory.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsFilterCreateNode(
                # _In_ PKSFILTER Filter,
                # _In_ KSNODE_DESCRIPTOR *const NodeDescriptor,
                # _Out_ PULONG NodeID
                # );
                KsFilterCreateNode = ks.KsFilterCreateNode
                KsFilterCreateNode.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsFilterAddTopologyConnections(
                # _In_ PKSFILTER Filter,
                # _In_ ULONG NewConnectionsCount,
                # _In_reads_(NewConnectionsCount) KSTOPOLOGY_CONNECTION *const NewTopologyConnections
                # );
                KsFilterAddTopologyConnections = (
                    ks.KsFilterAddTopologyConnections
                )
                KsFilterAddTopologyConnections.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsPinGetConnectedPinInterface(
                # _In_ PKSPIN Pin,
                # _In_ GUID* InterfaceId,
                # _Out_ PVOID* Interface
                # );
                KsPinGetConnectedPinInterface = (
                    ks.KsPinGetConnectedPinInterface
                )
                KsPinGetConnectedPinInterface.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # PFILE_OBJECT
                # NTAPI
                # KsPinGetConnectedPinFileObject(
                # _In_ PKSPIN Pin
                # );
                KsPinGetConnectedPinFileObject = (
                    ks.KsPinGetConnectedPinFileObject
                )
                KsPinGetConnectedPinFileObject.restype = PFILE_OBJECT

                # KSDDKAPI
                # PDEVICE_OBJECT
                # NTAPI
                # KsPinGetConnectedPinDeviceObject(
                # _In_ PKSPIN Pin
                # );
                KsPinGetConnectedPinDeviceObject = (
                    ks.KsPinGetConnectedPinDeviceObject
                )
                KsPinGetConnectedPinDeviceObject.restype = PDEVICE_OBJECT

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsPinGetConnectedFilterInterface(
                # _In_ PKSPIN Pin,
                # _In_ GUID* InterfaceId,
                # _Out_ PVOID* Interface
                # );
                KsPinGetConnectedFilterInterface = (
                    ks.KsPinGetConnectedFilterInterface
                )
                KsPinGetConnectedFilterInterface.restype = NTSTATUS

                if defined(_UNKNOWN_H_) or defined(__IUnknown_INTERFACE_DEFINED__):
                    # _IRQL_requires_max_(PASSIVE_LEVEL)
                    # KSDDKAPI
                    # NTSTATUS
                    # NTAPI
                    # KsPinGetReferenceClockInterface(
                    # _In_ PKSPIN Pin,
                    # _Out_ PIKSREFERENCECLOCK* Interface
                    # );
                    KsPinGetReferenceClockInterface = (
                        ks.KsPinGetReferenceClockInterface
                    )
                    KsPinGetReferenceClockInterface.restype = NTSTATUS

                # END IF  defined(_UNKNOWN_H_) or defined(__IUnknown_INTERFACE_DEFINED__)

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # VOID
                # NTAPI
                # KsPinSetPinClockTime(
                # _In_ PKSPIN Pin,
                # _In_ LONGLONG Time
                # );
                KsPinSetPinClockTime = ks.KsPinSetPinClockTime
                KsPinSetPinClockTime.restype = VOID

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsPinSubmitFrame(
                # _In_ PKSPIN Pin,
                # _In_reads_bytes_opt_(Size) PVOID Data,
                # _In_ ULONG Size OPTIONAL,
                # _In_opt_ PKSSTREAM_HEADER StreamHeader,
                # _In_opt_ PVOID Context
                # );
                KsPinSubmitFrame = ks.KsPinSubmitFrame
                KsPinSubmitFrame.restype = NTSTATUS

                # _IRQL_requires_max_(DISPATCH_LEVEL)
                # KSDDKAPI
                # NTSTATUS
                # NTAPI
                # KsPinSubmitFrameMdl(
                # _In_ PKSPIN Pin,
                # _In_opt_ PMDL Mdl,
                # _In_opt_ PKSSTREAM_HEADER StreamHeader,
                # _In_opt_ PVOID Context
                # );
                KsPinSubmitFrameMdl = ks.KsPinSubmitFrameMdl
                KsPinSubmitFrameMdl.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsPinRegisterFrameReturnCallback(
                # _In_ PKSPIN Pin,
                # _In_ PFNKSPINFRAMERETURN FrameReturn
                # );
                KsPinRegisterFrameReturnCallback = (
                    ks.KsPinRegisterFrameReturnCallback
                )
                KsPinRegisterFrameReturnCallback.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsPinRegisterIrpCompletionCallback(
                # _In_ PKSPIN Pin,
                # _In_ PFNKSPINIRPCOMPLETION IrpCompletion
                # );
                KsPinRegisterIrpCompletionCallback = (
                    ks.KsPinRegisterIrpCompletionCallback
                )
                KsPinRegisterIrpCompletionCallback.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsPinRegisterHandshakeCallback(
                # _In_ PKSPIN Pin,
                # _In_ PFNKSPINHANDSHAKE Handshake
                # );
                KsPinRegisterHandshakeCallback = (
                    ks.KsPinRegisterHandshakeCallback
                )
                KsPinRegisterHandshakeCallback.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsFilterRegisterPowerCallbacks(
                # _In_ PKSFILTER Filter,
                # _In_opt_ PFNKSFILTERPOWER Sleep,
                # _In_opt_ PFNKSFILTERPOWER Wake
                # );
                KsFilterRegisterPowerCallbacks = (
                    ks.KsFilterRegisterPowerCallbacks
                )
                KsFilterRegisterPowerCallbacks.restype = VOID

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # void
                # NTAPI
                # KsPinRegisterPowerCallbacks(
                # _In_ PKSPIN Pin,
                # _In_opt_ PFNKSPINPOWER Sleep,
                # _In_opt_ PFNKSPINPOWER Wake
                # );
                KsPinRegisterPowerCallbacks = ks.KsPinRegisterPowerCallbacks
                KsPinRegisterPowerCallbacks.restype = VOID

                if defined(_UNKNOWN_H_) or defined(__IUnknown_INTERFACE_DEFINED__):
                    # _IRQL_requires_max_(PASSIVE_LEVEL)
                    # KSDDKAPI
                    # PUNKNOWN
                    # NTAPI
                    # KsRegisterAggregatedClientUnknown(
                    # _In_ PVOID Object,
                    # _In_ PUNKNOWN ClientUnknown
                    # );
                    KsRegisterAggregatedClientUnknown = (
                        ks.KsRegisterAggregatedClientUnknown
                    )
                    KsRegisterAggregatedClientUnknown.restype = PUNKNOWN

                    # _IRQL_requires_max_(PASSIVE_LEVEL)
                    # KSDDKAPI
                    # PUNKNOWN
                    # NTAPI
                    # KsGetOuterUnknown(
                    # _In_ PVOID Object
                    # );
                    KsGetOuterUnknown = ks.KsGetOuterUnknown
                    KsGetOuterUnknown.restype = PUNKNOWN

                    # _IRQL_requires_max_(PASSIVE_LEVEL)
                    #                     PUNKNOWN __inline
                    #                     KsDeviceGetOuterUnknown(
                    #                         _In_ PKSDEVICE Device
                    #                         )
                    #                     {
                    #                         return KsGetOuterUnknown((PVOID) Device);
                    #                     }
                    #
                    #                     _IRQL_requires_max_(PASSIVE_LEVEL)
                    #                     PUNKNOWN __inline
                    #                     KsFilterFactoryRegisterAggregatedClientUnknown(
                    #                         _In_ PKSFILTERFACTORY FilterFactory,
                    #                         _In_ PUNKNOWN ClientUnknown
                    #                         )
                    #                     {
                    #                         return KsRegisterAggregatedClientUnknown((PVOID) FilterFactory,ClientUnknown);
                    #                     }
                    #
                    #                     _IRQL_requires_max_(PASSIVE_LEVEL)
                    #                     PUNKNOWN __inline
                    #                     KsFilterFactoryGetOuterUnknown(
                    #                         _In_ PKSFILTERFACTORY FilterFactory
                    #                         )
                    #                     {
                    #                         return KsGetOuterUnknown((PVOID) FilterFactory);
                    #                     }
                    #
                    #                     _IRQL_requires_max_(PASSIVE_LEVEL)
                    #                     PUNKNOWN __inline
                    #                     KsFilterRegisterAggregatedClientUnknown(
                    #                         _In_ PKSFILTER Filter,
                    #                         _In_ PUNKNOWN ClientUnknown
                    #                         )
                    #                     {
                    #                         return KsRegisterAggregatedClientUnknown((PVOID) Filter,ClientUnknown);
                    #                     }
                    #
                    #                     _IRQL_requires_max_(PASSIVE_LEVEL)
                    #                     PUNKNOWN __inline
                    #                     KsFilterGetOuterUnknown(
                    #                         _In_ PKSFILTER Filter
                    #                         )
                    #                     {
                    #                         return KsGetOuterUnknown((PVOID) Filter);
                    #                     }
                    #
                    #                     _IRQL_requires_max_(PASSIVE_LEVEL)
                    #                     PUNKNOWN __inline
                    #                     KsPinRegisterAggregatedClientUnknown(
                    #                         _In_ PKSPIN Pin,
                    #                         _In_ PUNKNOWN ClientUnknown
                    #                         )
                    #                     {
                    #                         return KsRegisterAggregatedClientUnknown((PVOID) Pin,ClientUnknown);
                    #                     }
                    #
                    #                     _IRQL_requires_max_(PASSIVE_LEVEL)
                    #                     PUNKNOWN __inline
                    #                     KsPinGetOuterUnknown(
                    #                         _In_ PKSPIN Pin
                    #                         )
                    #                     {
                    #                         return KsGetOuterUnknown((PVOID) Pin);
                    #                     }
                # END IF defined(_UNKNOWN_H_) or defined(__IUnknown_INTERFACE_DEFINED__)

            # END IF (NTDDI_VERSION >= NTDDI_WINXP)

        else: #  // not defined(_NTDDK_)

            ksuser = ctypes.windll.KsUser

            KS_NO_CREATE_FUNCTIONS = None
            if not defined(KS_NO_CREATE_FUNCTIONS):

                #
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # DWORD
                # WINAPI
                # KsCreateAllocator(
                # _In_ HANDLE ConnectionHandle,
                # _In_ PKSALLOCATOR_FRAMING AllocatorFraming,
                # _Out_ PHANDLE AllocatorHandle
                # );
                KsCreateAllocator = ksuser.KsCreateAllocator
                KsCreateAllocator.restype = DWORD
                # _IRQL_requires_max_(PASSIV_LEVEL)
                # KSDDKAP
                # DWORD
                # NTAPI
                # KsCreateClock(
                # _In_ HANDLE ConnectionHandle,
                # _In_ PKSCLOCK_CREATE ClockCreate,
                # _Out_ PHANDLE ClockHandle
                # );
                KsCreateClock = ksuser.KsCreateClock
                KsCreateClock.restype = DWORD

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # DWORD
                # WINAPI
                # KsCreatePin(
                # _In_ HANDLE FilterHandle,
                # _In_ PKSPIN_CONNECT Connect,
                # _In_ ACCESS_MASK DesiredAccess,
                # _Out_ PHANDLE ConnectionHandle
                # );
                KsCreatePin = ksuser.KsCreatePin
                KsCreatePin.restype = DWORD
                # _IRQL_requires_max_(ASSIVE_LEVEL)
                # KSDDKAPI
                # DWORD
                # WINAPI
                # KsCreateTopologyNode(
                # _In_ HANDLE ParentHandle,
                # _In_ PKSNODE_CREATE NodeCreate,
                # _In_ ACCESS_MASK DesiredAccess,
                # _Out_ PHANDLE NodeHandle
                # );
                KsCreateTopologyNode = ksuser.KsCreateTopologyNode
                KsCreateTopologyNode.restype = DWORD

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # HRESULT
                # WINAPI
                # KsCreateAllocator2(
                # _In_ HANDLE ConnectionHandle,
                # _In_ PKSALLOCATOR_FRAMING AllocatorFraming,
                #  _Out_ PHANDLE AllocatorHandle
                # );
                #
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # HRESULT
                # NTAPI
                # KsCreateClock2(
                # _In_ HANDLE ConnectionHandle,
                # _In_ PKSCLOCK_CREATE ClockCreate,
                # _Out_ PHANDLE ClockHandle
                # );
                #
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # HRESULT
                # WINAPI
                # KsCreatePin2(
                # _In_ HANDLE FilterHandle,
                # _In_ PKSPIN_CONNECT Connect,
                # _In_ ACCESS_MASK DesiredAccess,
                # _Out_ PHANDLE ConnectionHandle
                # );
                #
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # KSDDKAPI
                # HRESULT
                # WINAPI
                # KsCreateTopologyNode2(
                # _In_ HANDLE ParentHandle,
                # _In_ PKSNODE_CREATE NodeCreate,
                # _In_ ACCESS_MASK DesiredAccess,
                # _Out_ PHANDLE NodeHandle
                # );
                # KS create function that needs to be called after
                # initializing COM
            # END IF
        # END IF   not defined(_NTDDK_)

        if defined(__cplusplus):
            pass
        # END IF   defined(__cplusplus)

        # Start of MDL caching related decisions
        if defined(__cplusplus):
            pass
        # END IF   defined(__cplusplus)

        # MDL sharing related definitions
        # The Handle which represents the user mode Pin Handle
        class combined(ctypes.Structure):
            pass

        combined._fields_ = [
            ('pHandle', ULONG),
            ('fHandle', ULONG),                # The PayLoad from Sample, which is the Buffer attached
            ('uPayload', ULONG64),
        ]
        _MF_MDL_SHARED_PAYLOAD_KEY.combined = combined

        _MF_MDL_SHARED_PAYLOAD_KEY._fields_ = [
            ('combined', _MF_MDL_SHARED_PAYLOAD_KEY.combined),
            ('GMDLHandle', GUID),
        ]


        # We need the handle and upayload to be ULONG64
        # to adjust for 64 bit systems and 32 bit systems
        def MF_SET_SHARED_MDLHANDLE(a, b, c, d):
            d.combined.phandle = ULONG32(a)
            d.combined.fhandle = ULONG32(b)
            d.combined.upayload = ULONG64(c)
            return d


        if defined(_NTDDK_):
            # VOID
            # (*PFNKSCANCELPINNEDMDL)(
            #  _In_ GUID,
            # _In_ PVOID,
            # _In_ PVOID
            # );
            PFNKSCANCELPINNEDMDL = CALLBACK(
                VOID,
                GUID,
                PVOID,
                PVOID,
            )

            # _Must_inspect_result_
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # WINAPI
            # KsAcquireCachedMdl(
            # _In_  PIRP                 Irp,
            # _In_  REFGUID              Guid,
            # _In_  PFNKSCANCELPINNEDMDL CancelRoutine,
            # _In_  PVOID                CancelContext,
            # _Outptr_result_maybenull_ PMDL   *MdlAddr,
            # _Outptr_result_maybenull_ PVOID*  ReleaseContext
            # );
            KsAcquireCachedMdl = ks.KsAcquireCachedMdl
            KsAcquireCachedMdl.restype = NTSTATUS

            # _Must_inspect_result_
            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # KSDDKAPI
            # NTSTATUS
            # WINAPI
            # KsReleaseCachedMdl (
            # _In_     REFGUID                Guid,
            # _In_     PMDL                  MdlAddr,
            # _In_     HANDLE                 ReleaseContext
            # );
            KsReleaseCachedMdl = ks.KsReleaseCachedMdl
            KsReleaseCachedMdl.restype = NTSTATUS

        # END IF

        if defined(__cplusplus):
            pass
        # END IF   defined(__cplusplus)


        # End of MDL sharing related definitions
        def DENY_USERMODE_ACCESS(pIrp, CompleteRequest):
            if pIrp.RequestorMode != KernelMode:
                pIrp.IoStatus.Information = 0
                pIrp.IoStatus.Status = STATUS_INVALID_DEVICE_REQUEST
                if CompleteRequest(IoCompleteRequest(pIrp, IO_NO_INCREMENT)):
                    return STATUS_INVALID_DEVICE_REQUEST


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   not _KS_
