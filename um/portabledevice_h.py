import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


WPD_SERVICES_STRICT = None

class tagWPD_COMMAND_ACCESS_LOOKUP_ENTRY(ctypes.Structure):
    pass


WPD_COMMAND_ACCESS_LOOKUP_ENTRY = tagWPD_COMMAND_ACCESS_LOOKUP_ENTRY




# **************************************************************************
# Copyright (c) Microsoft Corporation. All rights reserved.
# *************************************************************************
# Windows XP SP2, Windows Vista, or later (excluding Windows Server 2003)
if (
    (NTDDI_VERSION >= NTDDI_WINXPSP2 and NTDDI_VERSION < NTDDI_WS03) or
     NTDDI_VERSION >= NTDDI_WINLH
):
    from pyWinAPI.um.propkeydef_h import * # NOQA
    from pyWinAPI.shared.devioctl_h import *  # NOQA

    # *************************************************************************
    # This section declares WPD guids used in PnP
    # *************************************************************************
    #
    # GUID_DEVINTERFACE_WPD
    # This GUID is used to identify devices / drivers that support the WPD DDI.
    # The WPD Class Extension component enables this device interface for WPD
    # Drivers that use it. Clients use this PnP interface when registering for
    # PnP device arrival messages for WPD devices.
    GUID_DEVINTERFACE_WPD = DEFINE_GUID(
        0x6AC27878,
        0xA6FA,
        0x4155,
        0xBA,
        0x85,
        0xF9,
        0x8F,
        0x49,
        0x1D,
        0x4F,
        0x33
    )

    # GUID_DEVINTERFACE_WPD_PRIVATE
    # This GUID is used to identify devices / drivers that can be used only by
    # a specialized WPD client and will not show up in normal WPD enumeration.
    # Devices identified with this interface cannot be used with normal WPD
    # applications. Generic WPD drivers and clients should not use this
    # interface.
    GUID_DEVINTERFACE_WPD_PRIVATE = DEFINE_GUID(
        0xBA0C718F,
        0x4DED,
        0x49B7,
        0xBD,
        0xD3,
        0xFA,
        0xBE,
        0x28,
        0x66,
        0x12,
        0x11
    )


    # GUID_DEVINTERFACE_WPD_SERVICE
    # This GUID is used to identify services that support the WPD Services DDI.
    # The WPD Class Extension component enables this device interface for WPD
    # Services that use it. Clients use this PnP interface when registering
    # for PnP device arrival messages for ALL WPD services. To register for
    # specific categories of services, client should use the service category
    # or service implements GUID.
    GUID_DEVINTERFACE_WPD_SERVICE = DEFINE_GUID(
        0x9EF44F80,
        0x3D64,
        0x4246,
        0xA6,
        0xAA,
        0x20,
        0x6F,
        0x32,
        0x8D,
        0x1E,
        0xDC
    )

    # ************************************************************************** This section declares WPD defines *************************************************************************
    #
    # WPD specific function number used to construct WPD I/O control codes.
    # Drivers should not use this define directly.
    WPD_CONTROL_FUNCTION_GENERIC_MESSAGE = 0x42

    # Defines WPD specific IOCTL number used by drivers to detect WPD requests
    # that may require READ and WRITE access to the device.
    IOCTL_WPD_MESSAGE_READWRITE_ACCESS = CTL_CODE(
        FILE_DEVICE_WPD,
        WPD_CONTROL_FUNCTION_GENERIC_MESSAGE,
        METHOD_BUFFERED,
        (FILE_READ_ACCESS | FILE_WRITE_ACCESS),
    )

    # Defines WPD specific IOCTL number used by drivers to detect WPD requests
    # that require READ-only access to the device.
    IOCTL_WPD_MESSAGE_READ_ACCESS = CTL_CODE(
        FILE_DEVICE_WPD,
        WPD_CONTROL_FUNCTION_GENERIC_MESSAGE,
        METHOD_BUFFERED,
        FILE_READ_ACCESS,
    )

    # Drivers can use this macro to detect whether the incoming IOCTL is a WPD
    # message or not.
    def IS_WPD_IOCTL(ControlCode):
        return ControlCode in (
            IOCTL_WPD_MESSAGE_READWRITE_ACCESS,
            IOCTL_WPD_MESSAGE_READ_ACCESS
        )

    # Pre-defined ObjectID for the DEVICE object.
    WPD_DEVICE_OBJECT_ID = "DEVICE"

    # Pre-defined IWMDMDevice for the IWMDRMDeviceApp license/metering APIs.
    WMDRMDEVICEAPP_USE_WPD_DEVICE_PTR = -1

    # Pre-defined name of a REG_DWORD value that defines the device type, used
    # for representation purposes only. Functional characteristics of the
    # device are decided through functional objects.
    # This value can be retrieved using
    # IPortableDeviceManager::GetDeviceProperty(...). See WPD_DEVICE_TYPES
    # enumeration for possible values.
    PORTABLE_DEVICE_TYPE = "PortableDeviceType"

    # Pre-defined name of a REG_SZ/REG_EXPAND_SZ/REG_MULTI_SZ value that
    # indicates the location of the device icon file or device icon resource.
    # This value can be retrieved using
    # IPortableDeviceManager::GetDeviceProperty(...). This
    # REG_SZ/REG_EXPAND_SZ/REG_MULTI_SZ value is either in the form
    # "file.dll, resourceID" or a full file path to an icon file. e.g.:
    # "x:\file.ico"
    PORTABLE_DEVICE_ICON = "Icons"

    # Pre-defined name of a REG_DWORD value that indicates the amount of time
    # in milliseconds the WPD Namespace Extension will keep its reference to
    # the device open under idle conditions.
    # This value can be retrieved using
    # IPortableDeviceManager::GetDeviceProperty(...).
    PORTABLE_DEVICE_NAMESPACE_TIMEOUT = "PortableDeviceNameSpaceTimeout"

    # Pre-defined name of a REG_DWORD value that is used as a flag to indicate
    # whether the device should, or should not, be shown in the Explorer view.
    # This value can be retrieved using
    # IPortableDeviceManager::GetDeviceProperty(...). Meaning of values are: 0
    # = include, 1 = exclude. 0 is assumed if this value doesn't exist.
    PORTABLE_DEVICE_NAMESPACE_EXCLUDE_FROM_SHELL = (
        "PortableDeviceNameSpaceExcludeFromShell"
    )

    # Pre-defined name of a REG_SZ or REG_MULTI_SZ value containing content
    # type guids that are used indicate for what content types the portable
    # device namespace should attempt to automatically generate a thumbnail
    # when placing new content on the device.
    # This value can be retrieved using
    # IPortableDeviceManager::GetDeviceProperty(...). Values should be a
    # string representation of a GUID, in the form
    # '{00000000-0000-0000-0000-000000000000}'. By default the portable device
    # namespace attempts to automatically generate thumbnails for
    # WPD_CONTENT_TYPE_IMAGE, if a device does not want this behavior it can
    # set this value to an empty string.
    PORTABLE_DEVICE_NAMESPACE_THUMBNAIL_CONTENT_TYPES = (
        "PortableDeviceNameSpaceThumbnailContentTypes"
    )

    # Pre-defined name of a REG_DWORD value that indicates whether a Portable
    # Device is a Mass Storage Class (MSC) device. This is used to avoid
    # duplication of the device in certain views and scenarios that include
    # both file system and Portable Devices.
    # This value can be retrieved using
    # IPortableDeviceManager::GetDeviceProperty(...). Meaning of values are: 0
    # = device is not mass storage, 1 = device is mass storage. 0 is assumed
    # if this value doesn't exist.
    PORTABLE_DEVICE_IS_MASS_STORAGE = "PortableDeviceIsMassStorage"

    # Pre-defined value identifying the
    # "Windows Media Digital Rights Management 10 for Portable Devices" scheme
    # for protecting content.
    # This value can be used by drivers to indicate they support WMDRM10-PD.
    # See WPD_DEVICE_SUPPORTED_DRM_SCHEMES.
    PORTABLE_DEVICE_DRM_SCHEME_WMDRM10_PD = "WMDRM10-PD"

    # Pre-defined value identifying the
    # "Portable Device Digital Rights Management" scheme for protecting
    # content.
    # This value can be used by drivers to indicate they support PDDRM. See
    # WPD_DEVICE_SUPPORTED_DRM_SCHEMES.
    PORTABLE_DEVICE_DRM_SCHEME_PDDRM = "PDDRM"

    # *************************************************************************
    # This section defines flags used in API arguments
    # *************************************************************************
    # Indicates whether the delete request should recursively delete any
    # children.
    class tagDELETE_OBJECT_OPTIONS(ENUM):
        PORTABLE_DEVICE_DELETE_NO_RECURSION = 0
        PORTABLE_DEVICE_DELETE_WITH_RECURSION = 1

    DELETE_OBJECT_OPTIONS = tagDELETE_OBJECT_OPTIONS

    # Possible values for PORTABLE_DEVICE_TYPE registry value.
    class tagWPD_DEVICE_TYPES(ENUM):
        WPD_DEVICE_TYPE_GENERIC = 0
        WPD_DEVICE_TYPE_CAMERA = 1
        WPD_DEVICE_TYPE_MEDIA_PLAYER = 2
        WPD_DEVICE_TYPE_PHONE = 3
        WPD_DEVICE_TYPE_VIDEO = 4
        WPD_DEVICE_TYPE_PERSONAL_INFORMATION_MANAGER = 5
        WPD_DEVICE_TYPE_AUDIO_RECORDER = 6

    WPD_DEVICE_TYPES = tagWPD_DEVICE_TYPES

    # Possible values for WPD_PROPERTY_ATTRIBUTE_FORM
    class tagWpdAttributeForm(ENUM):
        WPD_PROPERTY_ATTRIBUTE_FORM_UNSPECIFIED = 0
        WPD_PROPERTY_ATTRIBUTE_FORM_RANGE = 1
        WPD_PROPERTY_ATTRIBUTE_FORM_ENUMERATION = 2
        WPD_PROPERTY_ATTRIBUTE_FORM_REGULAR_EXPRESSION = 3
        WPD_PROPERTY_ATTRIBUTE_FORM_OBJECT_IDENTIFIER = 4

    WpdAttributeForm = tagWpdAttributeForm

    # Possible values for WPD_PARAMETER_ATTRIBUTE_FORM
    class tagWpdParameterAttributeForm(ENUM):
        WPD_PARAMETER_ATTRIBUTE_FORM_UNSPECIFIED = 0
        WPD_PARAMETER_ATTRIBUTE_FORM_RANGE = 1
        WPD_PARAMETER_ATTRIBUTE_FORM_ENUMERATION = 2
        WPD_PARAMETER_ATTRIBUTE_FORM_REGULAR_EXPRESSION = 3
        WPD_PARAMETER_ATTRIBUTE_FORM_OBJECT_IDENTIFIER = 4

    WpdParameterAttributeForm = tagWpdParameterAttributeForm

    # Possible values for WPD_DEVICE_TRANSPORT property.
    class tagWPD_DEVICE_TRANSPORTS(ENUM):
        WPD_DEVICE_TRANSPORT_UNSPECIFIED = 0
        WPD_DEVICE_TRANSPORT_USB = 1
        WPD_DEVICE_TRANSPORT_IP = 2
        WPD_DEVICE_TRANSPORT_BLUETOOTH = 3

    WPD_DEVICE_TRANSPORTS = tagWPD_DEVICE_TRANSPORTS

    # Indicates the type of storage.
    class tagWPD_STORAGE_TYPE_VALUES(ENUM):
        WPD_STORAGE_TYPE_UNDEFINED = 0
        WPD_STORAGE_TYPE_FIXED_ROM = 1
        WPD_STORAGE_TYPE_REMOVABLE_ROM = 2
        WPD_STORAGE_TYPE_FIXED_RAM = 3
        WPD_STORAGE_TYPE_REMOVABLE_RAM = 4

    WPD_STORAGE_TYPE_VALUES = tagWPD_STORAGE_TYPE_VALUES

    # Indicates write-protection that globally affects the storage.
    class tagWPD_STORAGE_ACCESS_CAPABILITY_VALUES(ENUM):
        WPD_STORAGE_ACCESS_CAPABILITY_READWRITE = 0
        WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITHOUT_OBJECT_DELETION = 1
        WPD_STORAGE_ACCESS_CAPABILITY_READ_ONLY_WITH_OBJECT_DELETION = 2

    WPD_STORAGE_ACCESS_CAPABILITY_VALUES = tagWPD_STORAGE_ACCESS_CAPABILITY_VALUES

    # Possible values for WPD_SMS_ENCODING
    class tagWPD_SMS_ENCODING_TYPES(ENUM):
        SMS_ENCODING_7_BIT = 0
        SMS_ENCODING_8_BIT = 1
        SMS_ENCODING_UTF_16 = 2

    WPD_SMS_ENCODING_TYPES = tagWPD_SMS_ENCODING_TYPES

    # Possible values for WPD_PROPERTY_SMS_MESSAGE_TYPE
    class tagSMS_MESSAGE_TYPES(ENUM):
        SMS_TEXT_MESSAGE = 0
        SMS_BINARY_MESSAGE = 1

    SMS_MESSAGE_TYPES = tagSMS_MESSAGE_TYPES

    # Indicates whether the device is on battery power or external power.
    class tagWPD_POWER_SOURCES(ENUM):
        WPD_POWER_SOURCE_BATTERY = 0
        WPD_POWER_SOURCE_EXTERNAL = 1

    WPD_POWER_SOURCES = tagWPD_POWER_SOURCES

    # Indicates the way the device weighs color channels.
    class tagWPD_WHITE_BALANCE_SETTINGS(ENUM):
        WPD_WHITE_BALANCE_UNDEFINED = 0
        WPD_WHITE_BALANCE_MANUAL = 1
        WPD_WHITE_BALANCE_AUTOMATIC = 2
        WPD_WHITE_BALANCE_ONE_PUSH_AUTOMATIC = 3
        WPD_WHITE_BALANCE_DAYLIGHT = 4
        WPD_WHITE_BALANCE_FLORESCENT = 5
        WPD_WHITE_BALANCE_TUNGSTEN = 6
        WPD_WHITE_BALANCE_FLASH = 7

    WPD_WHITE_BALANCE_SETTINGS = tagWPD_WHITE_BALANCE_SETTINGS

    # Indicates the focus mode of the device.
    class tagWPD_FOCUS_MODES(ENUM):
        WPD_FOCUS_UNDEFINED = 0
        WPD_FOCUS_MANUAL = 1
        WPD_FOCUS_AUTOMATIC = 2
        WPD_FOCUS_AUTOMATIC_MACRO = 3

    WPD_FOCUS_MODES = tagWPD_FOCUS_MODES

    # Indicates the metering mode of the device.
    class tagWPD_EXPOSURE_METERING_MODES(ENUM):
        WPD_EXPOSURE_METERING_MODE_UNDEFINED = 0
        WPD_EXPOSURE_METERING_MODE_AVERAGE = 1
        WPD_EXPOSURE_METERING_MODE_CENTER_WEIGHTED_AVERAGE = 2
        WPD_EXPOSURE_METERING_MODE_MULTI_SPOT = 3
        WPD_EXPOSURE_METERING_MODE_CENTER_SPOT = 4

    WPD_EXPOSURE_METERING_MODES = tagWPD_EXPOSURE_METERING_MODES

    # Indicates the flash mode of the device.
    class tagWPD_FLASH_MODES(ENUM):
        WPD_FLASH_MODE_UNDEFINED = 0
        WPD_FLASH_MODE_AUTO = 1
        WPD_FLASH_MODE_OFF = 2
        WPD_FLASH_MODE_FILL = 3
        WPD_FLASH_MODE_RED_EYE_AUTO = 4
        WPD_FLASH_MODE_RED_EYE_FILL = 5
        WPD_FLASH_MODE_EXTERNAL_SYNC = 6

    WPD_FLASH_MODES = tagWPD_FLASH_MODES

    # Indicates the exposure program mode of the device.
    class tagWPD_EXPOSURE_PROGRAM_MODES(ENUM):
        WPD_EXPOSURE_PROGRAM_MODE_UNDEFINED = 0
        WPD_EXPOSURE_PROGRAM_MODE_MANUAL = 1
        WPD_EXPOSURE_PROGRAM_MODE_AUTO = 2
        WPD_EXPOSURE_PROGRAM_MODE_APERTURE_PRIORITY = 3
        WPD_EXPOSURE_PROGRAM_MODE_SHUTTER_PRIORITY = 4
        WPD_EXPOSURE_PROGRAM_MODE_CREATIVE = 5
        WPD_EXPOSURE_PROGRAM_MODE_ACTION = 6
        WPD_EXPOSURE_PROGRAM_MODE_PORTRAIT = 7

    WPD_EXPOSURE_PROGRAM_MODES = tagWPD_EXPOSURE_PROGRAM_MODES

    # Indicates the capture mode of the device.
    class tagWPD_CAPTURE_MODES(ENUM):
        WPD_CAPTURE_MODE_UNDEFINED = 0
        WPD_CAPTURE_MODE_NORMAL = 1
        WPD_CAPTURE_MODE_BURST = 2
        WPD_CAPTURE_MODE_TIMELAPSE = 3

    WPD_CAPTURE_MODES = tagWPD_CAPTURE_MODES

    # Indicates the effect mode of the capture device.
    class tagWPD_EFFECT_MODES(ENUM):
        WPD_EFFECT_MODE_UNDEFINED = 0
        WPD_EFFECT_MODE_COLOR = 1
        WPD_EFFECT_MODE_BLACK_AND_WHITE = 2
        WPD_EFFECT_MODE_SEPIA = 3

    WPD_EFFECT_MODES = tagWPD_EFFECT_MODES

    # Indicates the metering mode of the capture device.
    class tagWPD_FOCUS_METERING_MODES(ENUM):
        WPD_FOCUS_METERING_MODE_UNDEFINED = 0
        WPD_FOCUS_METERING_MODE_CENTER_SPOT = 1
        WPD_FOCUS_METERING_MODE_MULTI_SPOT = 2

    WPD_FOCUS_METERING_MODES = tagWPD_FOCUS_METERING_MODES

    # Indicates the type of bitrate for the audio/video data.
    class tagWPD_BITRATE_TYPES(ENUM):
        WPD_BITRATE_TYPE_UNUSED = 0
        WPD_BITRATE_TYPE_DISCRETE = 1
        WPD_BITRATE_TYPE_VARIABLE = 2
        WPD_BITRATE_TYPE_FREE = 3

    WPD_BITRATE_TYPES = tagWPD_BITRATE_TYPES

    # Qualifies the object data in a contextual way.
    class tagWPD_META_GENRES(ENUM):
        WPD_META_GENRE_UNUSED = 0x0
        WPD_META_GENRE_GENERIC_MUSIC_AUDIO_FILE = 0x1
        WPD_META_GENRE_GENERIC_NON_MUSIC_AUDIO_FILE = 0x11
        WPD_META_GENRE_SPOKEN_WORD_AUDIO_BOOK_FILES = 0x12
        WPD_META_GENRE_SPOKEN_WORD_FILES_NON_AUDIO_BOOK = 0x13
        WPD_META_GENRE_SPOKEN_WORD_NEWS = 0x14
        WPD_META_GENRE_SPOKEN_WORD_TALK_SHOWS = 0x15
        WPD_META_GENRE_GENERIC_VIDEO_FILE = 0x21
        WPD_META_GENRE_NEWS_VIDEO_FILE = 0x22
        WPD_META_GENRE_MUSIC_VIDEO_FILE = 0x23
        WPD_META_GENRE_HOME_VIDEO_FILE = 0x24
        WPD_META_GENRE_FEATURE_FILM_VIDEO_FILE = 0x25
        WPD_META_GENRE_TELEVISION_VIDEO_FILE = 0x26
        WPD_META_GENRE_TRAINING_EDUCATIONAL_VIDEO_FILE = 0x27
        WPD_META_GENRE_PHOTO_MONTAGE_VIDEO_FILE = 0x28
        WPD_META_GENRE_GENERIC_NON_AUDIO_NON_VIDEO = 0x30
        WPD_META_GENRE_AUDIO_PODCAST = 0x40
        WPD_META_GENRE_VIDEO_PODCAST = 0x41
        WPD_META_GENRE_MIXED_PODCAST = 0x42

    WPD_META_GENRES = tagWPD_META_GENRES

    # Indicates the cropped status of an image.
    class tagWPD_CROPPED_STATUS_VALUES(ENUM):
        WPD_CROPPED_STATUS_NOT_CROPPED = 0
        WPD_CROPPED_STATUS_CROPPED = 1
        WPD_CROPPED_STATUS_SHOULD_NOT_BE_CROPPED = 2

    WPD_CROPPED_STATUS_VALUES = tagWPD_CROPPED_STATUS_VALUES

    # Indicates the color corrected status of an image.
    class tagWPD_COLOR_CORRECTED_STATUS_VALUES(ENUM):
        WPD_COLOR_CORRECTED_STATUS_NOT_CORRECTED = 0
        WPD_COLOR_CORRECTED_STATUS_CORRECTED = 1
        WPD_COLOR_CORRECTED_STATUS_SHOULD_NOT_BE_CORRECTED = 2

    WPD_COLOR_CORRECTED_STATUS_VALUES = tagWPD_COLOR_CORRECTED_STATUS_VALUES

    # Identifies the video scan-type information.
    class tagWPD_VIDEO_SCAN_TYPES(ENUM):
        WPD_VIDEO_SCAN_TYPE_UNUSED = 0
        WPD_VIDEO_SCAN_TYPE_PROGRESSIVE = 1
        WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_UPPER_FIRST = 2
        WPD_VIDEO_SCAN_TYPE_FIELD_INTERLEAVED_LOWER_FIRST = 3
        WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_UPPER_FIRST = 4
        WPD_VIDEO_SCAN_TYPE_FIELD_SINGLE_LOWER_FIRST = 5
        WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE = 6
        WPD_VIDEO_SCAN_TYPE_MIXED_INTERLACE_AND_PROGRESSIVE = 7

    WPD_VIDEO_SCAN_TYPES = tagWPD_VIDEO_SCAN_TYPES

    # Indicates the current state of the operation in progress.
    class tagWPD_OPERATION_STATES(ENUM):
        WPD_OPERATION_STATE_UNSPECIFIED = 0
        WPD_OPERATION_STATE_STARTED = 1
        WPD_OPERATION_STATE_RUNNING = 2
        WPD_OPERATION_STATE_PAUSED = 3
        WPD_OPERATION_STATE_CANCELLED = 4
        WPD_OPERATION_STATE_FINISHED = 5
        WPD_OPERATION_STATE_ABORTED = 6

    WPD_OPERATION_STATES = tagWPD_OPERATION_STATES

    # Indicates the units for a referenced section of data.
    class tagWPD_SECTION_DATA_UNITS_VALUES(ENUM):
        WPD_SECTION_DATA_UNITS_BYTES = 0
        WPD_SECTION_DATA_UNITS_MILLISECONDS = 1

    WPD_SECTION_DATA_UNITS_VALUES = tagWPD_SECTION_DATA_UNITS_VALUES

    # Indicates whether the rendering information profile entry corresponds to
    # an Object or a Resource.
    class tagWPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES(ENUM):
        WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_OBJECT = 0
        WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_RESOURCE = 1

    WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES = tagWPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES

    # Indicates the type of access the command requires. This is only used
    # internally by the command access lookup table. There is no need to use
    # these values directly.
    class tagWPD_COMMAND_ACCESS_TYPES(ENUM):
        WPD_COMMAND_ACCESS_READ = 1
        WPD_COMMAND_ACCESS_READWRITE = 3
        WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_STGM_ACCESS = 4
        WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_FILE_ACCESS = 8
        WPD_COMMAND_ACCESS_FROM_ATTRIBUTE_WITH_METHOD_ACCESS = 16

    WPD_COMMAND_ACCESS_TYPES = tagWPD_COMMAND_ACCESS_TYPES

    # Indicates the inheritance relationship to query for this service.
    class tagWPD_SERVICE_INHERITANCE_TYPES(ENUM):
        WPD_SERVICE_INHERITANCE_IMPLEMENTATION = 0

    WPD_SERVICE_INHERITANCE_TYPES = tagWPD_SERVICE_INHERITANCE_TYPES

    # Indicates the usage of a parameter.
    class tagWPD_PARAMETER_USAGE_TYPES(ENUM):
        WPD_PARAMETER_USAGE_RETURN = 0
        WPD_PARAMETER_USAGE_IN = 1
        WPD_PARAMETER_USAGE_OUT = 2
        WPD_PARAMETER_USAGE_INOUT = 3

    WPD_PARAMETER_USAGE_TYPES = tagWPD_PARAMETER_USAGE_TYPES

    # ************************************************************************** This section declares WPD specific Errors *************************************************************************
    #
    FACILITY_WPD = 42
    E_WPD_DEVICE_ALREADY_OPENED = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        1
    )
    # 0x802A0001
    E_WPD_DEVICE_NOT_OPEN = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        2
    )
    # 0x802A0002

    E_WPD_OBJECT_ALREADY_ATTACHED_TO_DEVICE = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        3
    )
    # 0x802A0003

    E_WPD_OBJECT_NOT_ATTACHED_TO_DEVICE = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        4
    )
    # 0x802A0004

    E_WPD_OBJECT_NOT_COMMITED = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        5
    )
    # 0x802A0005

    E_WPD_DEVICE_IS_HUNG = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        6
    )
    # 0x802A0006

    E_WPD_SMS_INVALID_RECIPIENT = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        100
    )
    # 0x802A0064

    E_WPD_SMS_INVALID_MESSAGE_BODY = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        101
    )
    # 0x802A0065

    E_WPD_SMS_SERVICE_UNAVAILABLE = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        102
    )
    # 0x802A0066

    E_WPD_SERVICE_ALREADY_OPENED = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        200
    )
    # 0x802A00C8

    E_WPD_SERVICE_NOT_OPEN = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        201
    )
    # 0x802A00C9

    E_WPD_OBJECT_ALREADY_ATTACHED_TO_SERVICE = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        202
    )
    # 0x802A00CA

    E_WPD_OBJECT_NOT_ATTACHED_TO_SERVICE = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        203
    )
    # 0x802A00CB

    E_WPD_SERVICE_BAD_PARAMETER_ORDER = MAKE_HRESULT(
        SEVERITY_ERROR,
        FACILITY_WPD,
        204
    )
    # 0x802A00CC


    # *************************************************************************
    # This section defines all WPD Events
    # *************************************************************************
    # WPD_EVENT_NOTIFICATION
    # This GUID is used to identify all WPD driver events to the event
    # sub-system. The driver uses this as the GUID identifier when it queues
    # an event with IWdfDevice::PostEvent(). Applications never use this value.
    WPD_EVENT_NOTIFICATION = DEFINE_GUID(
        0x2BA2E40A,
        0x6B4C,
        0x4295,
        0xBB,
        0x43,
        0x26,
        0x32,
        0x2B,
        0x99,
        0xAE,
        0xB2
    )

    # WPD_EVENT_OBJECT_ADDED
    # This event is sent after a new object is available on the device.
    WPD_EVENT_OBJECT_ADDED = DEFINE_GUID(
        0xA726DA95,
        0xE207,
        0x4B02,
        0x8D,
        0x44,
        0xBE,
        0xF2,
        0xE8,
        0x6C,
        0xBF,
        0xFC
    )

    # WPD_EVENT_OBJECT_REMOVED
    # This event is sent after a previously existing object has been removed
    # from the device.
    WPD_EVENT_OBJECT_REMOVED = DEFINE_GUID(
        0xBE82AB88,
        0xA52C,
        0x4823,
        0x96,
        0xE5,
        0xD0,
        0x27,
        0x26,
        0x71,
        0xFC,
        0x38
    )

    # WPD_EVENT_OBJECT_UPDATED
    # This event is sent after an object has been updated such that any
    # connected client should refresh its view of that object.
    WPD_EVENT_OBJECT_UPDATED = DEFINE_GUID(
        0x1445A759,
        0x2E01,
        0x485D,
        0x9F,
        0x27,
        0xFF,
        0x07,
        0xDA,
        0xE6,
        0x97,
        0xAB
    )

    # WPD_EVENT_DEVICE_RESET
    # This event indicates that the device is about to be reset, and all
    # connected clients should close their connection to the device.
    WPD_EVENT_DEVICE_RESET = DEFINE_GUID(
        0x7755CF53,
        0xC1ED,
        0x44F3,
        0xB5,
        0xA2,
        0x45,
        0x1E,
        0x2C,
        0x37,
        0x6B,
        0x27
    )

    # WPD_EVENT_DEVICE_CAPABILITIES_UPDATED
    # This event indicates that the device capabilities have changed. Clients
    # should re-query the device if they have made any decisions based on
    # device capabilities.
    WPD_EVENT_DEVICE_CAPABILITIES_UPDATED = DEFINE_GUID(
        0x36885AA1,
        0xCD54,
        0x4DAA,
        0xB3,
        0xD0,
        0xAF,
        0xB3,
        0xE0,
        0x3F,
        0x59,
        0x99
    )

    # WPD_EVENT_STORAGE_FORMAT
    # This event indicates the progress of a format operation on a storage
    # object.
    WPD_EVENT_STORAGE_FORMAT = DEFINE_GUID(
        0x3782616B,
        0x22BC,
        0x4474,
        0xA2,
        0x51,
        0x30,
        0x70,
        0xF8,
        0xD3,
        0x88,
        0x57
    )

    # WPD_EVENT_OBJECT_TRANSFER_REQUESTED
    # This event is sent to request an application to transfer a particular
    # object from the device.
    WPD_EVENT_OBJECT_TRANSFER_REQUESTED = DEFINE_GUID(
        0x8D16A0A1,
        0xF2C6,
        0x41DA,
        0x8F,
        0x19,
        0x5E,
        0x53,
        0x72,
        0x1A,
        0xDB,
        0xF2
    )

    # WPD_EVENT_DEVICE_REMOVED
    # This event is sent when a driver for a device is being unloaded. This is
    # typically a result of the device being unplugged.
    WPD_EVENT_DEVICE_REMOVED = DEFINE_GUID(
        0xE4CBCA1B,
        0x6918,
        0x48B9,
        0x85,
        0xEE,
        0x02,
        0xBE,
        0x7C,
        0x85,
        0x0A,
        0xF9
    )

    # WPD_EVENT_SERVICE_METHOD_COMPLETE
    # This event is sent when a driver has completed invoking a service
    # method. This event must be sent even when the method fails.
    WPD_EVENT_SERVICE_METHOD_COMPLETE = DEFINE_GUID(
        0x8A33F5F8,
        0x0ACC,
        0x4D9B,
        0x9C,
        0xC4,
        0x11,
        0x2D,
        0x35,
        0x3B,
        0x86,
        0xCA
    )

    # *************************************************************************
    # This section defines all WPD content types
    # *************************************************************************
    # WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT
    # Indicates this object represents a functional object, not content data
    # on the device.
    WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT = DEFINE_GUID(
        0x99ED0160,
        0x17FF,
        0x4C44,
        0x9D,
        0x98,
        0x1D,
        0x7A,
        0x6F,
        0x94,
        0x19,
        0x21
    )

    # WPD_CONTENT_TYPE_FOLDER
    # Indicates this object is a folder.
    WPD_CONTENT_TYPE_FOLDER = DEFINE_GUID(
        0x27E2E392,
        0xA111,
        0x48E0,
        0xAB,
        0x0C,
        0xE1,
        0x77,
        0x05,
        0xA0,
        0x5F,
        0x85
    )

    # WPD_CONTENT_TYPE_IMAGE
    # Indicates this object represents image data (e.g. a JPEG file)
    WPD_CONTENT_TYPE_IMAGE = DEFINE_GUID(
        0xEF2107D5,
        0xA52A,
        0x4243,
        0xA2,
        0x6B,
        0x62,
        0xD4,
        0x17,
        0x6D,
        0x76,
        0x03
    )

    # WPD_CONTENT_TYPE_DOCUMENT
    # Indicates this object represents document data
    # (e.g. a MS WORD file, TEXT file, etc.)
    WPD_CONTENT_TYPE_DOCUMENT = DEFINE_GUID(
        0x680ADF52,
        0x950A,
        0x4041,
        0x9B,
        0x41,
        0x65,
        0xE3,
        0x93,
        0x64,
        0x81,
        0x55
    )

    # WPD_CONTENT_TYPE_CONTACT
    # Indicates this object represents contact data
    # (e.g. name/number, or a VCARD file)
    WPD_CONTENT_TYPE_CONTACT = DEFINE_GUID(
        0xEABA8313,
        0x4525,
        0x4707,
        0x9F,
        0x0E,
        0x87,
        0xC6,
        0x80,
        0x8E,
        0x94,
        0x35
    )

    # WPD_CONTENT_TYPE_CONTACT_GROUP
    # Indicates this object represents a group of contacts.
    WPD_CONTENT_TYPE_CONTACT_GROUP = DEFINE_GUID(
        0x346B8932,
        0x4C36,
        0x40D8,
        0x94,
        0x15,
        0x18,
        0x28,
        0x29,
        0x1F,
        0x9D,
        0xE9
    )

    # WPD_CONTENT_TYPE_AUDIO
    # Indicates this object represents audio data (e.g. a WMA or MP3 file)
    WPD_CONTENT_TYPE_AUDIO = DEFINE_GUID(
        0x4AD2C85E,
        0x5E2D,
        0x45E5,
        0x88,
        0x64,
        0x4F,
        0x22,
        0x9E,
        0x3C,
        0x6C,
        0xF0
    )

    # WPD_CONTENT_TYPE_VIDEO
    # Indicates this object represents video data (e.g. a WMV or AVI file)
    WPD_CONTENT_TYPE_VIDEO = DEFINE_GUID(
        0x9261B03C,
        0x3D78,
        0x4519,
        0x85,
        0xE3,
        0x02,
        0xC5,
        0xE1,
        0xF5,
        0x0B,
        0xB9
    )

    # WPD_CONTENT_TYPE_TELEVISION
    # Indicates this object represents a television recording.
    WPD_CONTENT_TYPE_TELEVISION = DEFINE_GUID(
        0x60A169CF,
        0xF2AE,
        0x4E21,
        0x93,
        0x75,
        0x96,
        0x77,
        0xF1,
        0x1C,
        0x1C,
        0x6E
    )

    # WPD_CONTENT_TYPE_PLAYLIST
    # Indicates this object represents a playlist.
    WPD_CONTENT_TYPE_PLAYLIST = DEFINE_GUID(
        0x1A33F7E4,
        0xAF13,
        0x48F5,
        0x99,
        0x4E,
        0x77,
        0x36,
        0x9D,
        0xFE,
        0x04,
        0xA3
    )

    # WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM
    # Indicates this object represents an album, which may contain objects of
    # different content types (typically, MUSIC, IMAGE and VIDEO).
    WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM = DEFINE_GUID(
        0x00F0C3AC,
        0xA593,
        0x49AC,
        0x92,
        0x19,
        0x24,
        0xAB,
        0xCA,
        0x5A,
        0x25,
        0x63
    )

    # WPD_CONTENT_TYPE_AUDIO_ALBUM
    # Indicates this object represents an audio album.
    WPD_CONTENT_TYPE_AUDIO_ALBUM = DEFINE_GUID(
        0xAA18737E,
        0x5009,
        0x48FA,
        0xAE,
        0x21,
        0x85,
        0xF2,
        0x43,
        0x83,
        0xB4,
        0xE6
    )

    # WPD_CONTENT_TYPE_IMAGE_ALBUM
    # Indicates this object represents an image album.
    WPD_CONTENT_TYPE_IMAGE_ALBUM = DEFINE_GUID(
        0x75793148,
        0x15F5,
        0x4A30,
        0xA8,
        0x13,
        0x54,
        0xED,
        0x8A,
        0x37,
        0xE2,
        0x26
    )

    # WPD_CONTENT_TYPE_VIDEO_ALBUM
    # Indicates this object represents a video album.
    WPD_CONTENT_TYPE_VIDEO_ALBUM = DEFINE_GUID(
        0x012B0DB7,
        0xD4C1,
        0x45D6,
        0xB0,
        0x81,
        0x94,
        0xB8,
        0x77,
        0x79,
        0x61,
        0x4F
    )

    # WPD_CONTENT_TYPE_MEMO
    # Indicates this object represents memo data
    WPD_CONTENT_TYPE_MEMO = DEFINE_GUID(
        0x9CD20ECF,
        0x3B50,
        0x414F,
        0xA6,
        0x41,
        0xE4,
        0x73,
        0xFF,
        0xE4,
        0x57,
        0x51
    )

    # WPD_CONTENT_TYPE_EMAIL
    # Indicates this object represents e-mail data
    WPD_CONTENT_TYPE_EMAIL = DEFINE_GUID(
        0x8038044A,
        0x7E51,
        0x4F8F,
        0x88,
        0x3D,
        0x1D,
        0x06,
        0x23,
        0xD1,
        0x45,
        0x33
    )

    # WPD_CONTENT_TYPE_APPOINTMENT
    # Indicates this object represents an appointment in a calendar
    WPD_CONTENT_TYPE_APPOINTMENT = DEFINE_GUID(
        0x0FED060E,
        0x8793,
        0x4B1E,
        0x90,
        0xC9,
        0x48,
        0xAC,
        0x38,
        0x9A,
        0xC6,
        0x31
    )

    # WPD_CONTENT_TYPE_TASK
    # Indicates this object represents a task for tracking (e.g. a TODO list)
    WPD_CONTENT_TYPE_TASK = DEFINE_GUID(
        0x63252F2C,
        0x887F,
        0x4CB6,
        0xB1,
        0xAC,
        0xD2,
        0x98,
        0x55,
        0xDC,
        0xEF,
        0x6C
    )

    # WPD_CONTENT_TYPE_PROGRAM
    # Indicates this object represents a file that can be run. This could be a
    # script, executable and so on.
    WPD_CONTENT_TYPE_PROGRAM = DEFINE_GUID(
        0xD269F96A,
        0x247C,
        0x4BFF,
        0x98,
        0xFB,
        0x97,
        0xF3,
        0xC4,
        0x92,
        0x20,
        0xE6
    )

    # WPD_CONTENT_TYPE_GENERIC_FILE
    # Indicates this object represents a file that does not fall into any of
    # the other predefined WPD types for files.
    WPD_CONTENT_TYPE_GENERIC_FILE = DEFINE_GUID(
        0x0085E0A6,
        0x8D34,
        0x45D7,
        0xBC,
        0x5C,
        0x44,
        0x7E,
        0x59,
        0xC7,
        0x3D,
        0x48
    )

    # WPD_CONTENT_TYPE_CALENDAR
    # Indicates this object represents a calender
    WPD_CONTENT_TYPE_CALENDAR = DEFINE_GUID(
        0xA1FD5967,
        0x6023,
        0x49A0,
        0x9D,
        0xF1,
        0xF8,
        0x06,
        0x0B,
        0xE7,
        0x51,
        0xB0
    )

    # WPD_CONTENT_TYPE_GENERIC_MESSAGE
    # Indicates this object represents a message
    # (e.g. SMS message, E-Mail message, etc.)
    WPD_CONTENT_TYPE_GENERIC_MESSAGE = DEFINE_GUID(
        0xE80EAAF8,
        0xB2DB,
        0x4133,
        0xB6,
        0x7E,
        0x1B,
        0xEF,
        0x4B,
        0x4A,
        0x6E,
        0x5F
    )

    # WPD_CONTENT_TYPE_NETWORK_ASSOCIATION
    # Indicates this object represents an association between a host and a
    # device.
    WPD_CONTENT_TYPE_NETWORK_ASSOCIATION = DEFINE_GUID(
        0x031DA7EE,
        0x18C8,
        0x4205,
        0x84,
        0x7E,
        0x89,
        0xA1,
        0x12,
        0x61,
        0xD0,
        0xF3
    )

    # WPD_CONTENT_TYPE_CERTIFICATE
    # Indicates this object represents certificate used for authentication.
    WPD_CONTENT_TYPE_CERTIFICATE = DEFINE_GUID(
        0xDC3876E8,
        0xA948,
        0x4060,
        0x90,
        0x50,
        0xCB,
        0xD7,
        0x7E,
        0x8A,
        0x3D,
        0x87
    )

    # WPD_CONTENT_TYPE_WIRELESS_PROFILE
    # Indicates this object represents wireless network access information.
    WPD_CONTENT_TYPE_WIRELESS_PROFILE = DEFINE_GUID(
        0x0BAC070A,
        0x9F5F,
        0x4DA4,
        0xA8,
        0xF6,
        0x3D,
        0xE4,
        0x4D,
        0x68,
        0xFD,
        0x6C
    )

    # WPD_CONTENT_TYPE_MEDIA_CAST
    # Indicates this object represents a media cast. A media cast object can
    # be though of as a container object that groups related content, similar
    # to how a playlist groups songs to play. Often, a media cast object is
    # used to group media content originally published online.
    WPD_CONTENT_TYPE_MEDIA_CAST = DEFINE_GUID(
        0x5E88B3CC,
        0x3E65,
        0x4E62,
        0xBF,
        0xFF,
        0x22,
        0x94,
        0x95,
        0x25,
        0x3A,
        0xB0
    )

    # WPD_CONTENT_TYPE_SECTION
    # Indicates this object describes a section of data contained in another
    # object. The WPD_OBJECT_REFERENCES property indicates which object
    # contains the actual data.
    WPD_CONTENT_TYPE_SECTION = DEFINE_GUID(
        0x821089F5,
        0x1D91,
        0x4DC9,
        0xBE,
        0x3C,
        0xBB,
        0xB1,
        0xB3,
        0x5B,
        0x18,
        0xCE
    )

    # WPD_CONTENT_TYPE_UNSPECIFIED
    # Indicates this object doesn't fall into the predefined WPD content types
    WPD_CONTENT_TYPE_UNSPECIFIED = DEFINE_GUID(
        0x28D8D31E,
        0x249C,
        0x454E,
        0xAA,
        0xBC,
        0x34,
        0x88,
        0x31,
        0x68,
        0xE6,
        0x34
    )

    # WPD_CONTENT_TYPE_ALL
    # This content type is only valid as a parameter to API functions and
    # driver commands. It should not be reported as a supported content type
    # by the driver.
    WPD_CONTENT_TYPE_ALL = DEFINE_GUID(
        0x80E170D2,
        0x1055,
        0x4A3E,
        0xB9,
        0x52,
        0x82,
        0xCC,
        0x4F,
        0x8A,
        0x86,
        0x89
    )

    # *************************************************************************
    # This section defines all WPD Functional Categories
    # *************************************************************************
    # WPD_FUNCTIONAL_CATEGORY_DEVICE
    # Used for the device object, which is always the top-most object of the
    # device.
    WPD_FUNCTIONAL_CATEGORY_DEVICE = DEFINE_GUID(
        0x08EA466B,
        0xE3A4,
        0x4336,
        0xA1,
        0xF3,
        0xA4,
        0x4D,
        0x2B,
        0x5C,
        0x43,
        0x8C
    )

    # WPD_FUNCTIONAL_CATEGORY_STORAGE
    # Indicates this object encapsulates storage functionality on the device
    # (e.g. memory cards, internal memory)
    WPD_FUNCTIONAL_CATEGORY_STORAGE = DEFINE_GUID(
        0x23F05BBC,
        0x15DE,
        0x4C2A,
        0xA5,
        0x5B,
        0xA9,
        0xAF,
        0x5C,
        0xE4,
        0x12,
        0xEF
    )

    # WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE
    # Indicates this object encapsulates still image capture functionality on
    # the device (e.g. camera or camera attachment)
    WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE = DEFINE_GUID(
        0x613CA327,
        0xAB93,
        0x4900,
        0xB4,
        0xFA,
        0x89,
        0x5B,
        0xB5,
        0x87,
        0x4B,
        0x79
    )

    # WPD_FUNCTIONAL_CATEGORY_AUDIO_CAPTURE
    # Indicates this object encapsulates audio capture functionality on the
    # device (e.g. voice recorder or other audio recording component)
    WPD_FUNCTIONAL_CATEGORY_AUDIO_CAPTURE = DEFINE_GUID(
        0x3F2A1919,
        0xC7C2,
        0x4A00,
        0x85,
        0x5D,
        0xF5,
        0x7C,
        0xF0,
        0x6D,
        0xEB,
        0xBB
    )

    # WPD_FUNCTIONAL_CATEGORY_VIDEO_CAPTURE
    # Indicates this object encapsulates video capture functionality on the
    # device (e.g. video recorder or video recording component)
    WPD_FUNCTIONAL_CATEGORY_VIDEO_CAPTURE = DEFINE_GUID(
        0xE23E5F6B,
        0x7243,
        0x43AA,
        0x8D,
        0xF1,
        0x0E,
        0xB3,
        0xD9,
        0x68,
        0xA9,
        0x18
    )

    # WPD_FUNCTIONAL_CATEGORY_SMS
    # Indicates this object encapsulates SMS sending functionality on the
    # device
    # (not the receiving or saved SMS messages since those are represented as content objects on the )
    #
    WPD_FUNCTIONAL_CATEGORY_SMS = DEFINE_GUID(
        0x0044A0B1,
        0xC1E9,
        0x4AFD,
        0xB3,
        0x58,
        0xA6,
        0x2C,
        0x61,
        0x17,
        0xC9,
        0xCF
    )

    # WPD_FUNCTIONAL_CATEGORY_RENDERING_INFORMATION
    # Indicates this object provides information about the rendering
    # characteristics of the device.
    WPD_FUNCTIONAL_CATEGORY_RENDERING_INFORMATION = DEFINE_GUID(
        0x08600BA4,
        0xA7BA,
        0x4A01,
        0xAB,
        0x0E,
        0x00,
        0x65,
        0xD0,
        0xA3,
        0x56,
        0xD3
    )

    # WPD_FUNCTIONAL_CATEGORY_NETWORK_CONFIGURATION
    # Indicates this object encapsulates network configuration functionality
    # on the device (e.g. WiFi Profiles, Partnerships).
    WPD_FUNCTIONAL_CATEGORY_NETWORK_CONFIGURATION = DEFINE_GUID(
        0x48F4DB72,
        0x7C6A,
        0x4AB0,
        0x9E,
        0x1A,
        0x47,
        0x0E,
        0x3C,
        0xDB,
        0xF2,
        0x6A
    )

    # WPD_FUNCTIONAL_CATEGORY_ALL
    # This functional category is only valid as a parameter to API functions
    # and driver commands. It should not be reported as a supported functional
    # category by the driver.
    WPD_FUNCTIONAL_CATEGORY_ALL = DEFINE_GUID(
        0x2D8A6512,
        0xA74C,
        0x448E,
        0xBA,
        0x8A,
        0xF4,
        0xAC,
        0x07,
        0xC4,
        0x93,
        0x99
    )

    # *************************************************************************
    # This section defines all WPD Formats
    # *************************************************************************
    # WPD_OBJECT_FORMAT_ICON
    # Standard Windows ICON format
    WPD_OBJECT_FORMAT_ICON = DEFINE_GUID(
        0x077232ED,
        0x102C,
        0x4638,
        0x9C,
        0x22,
        0x83,
        0xF1,
        0x42,
        0xBF,
        0xC8,
        0x22
    )

    # WPD_OBJECT_FORMAT_M4A
    # Audio file format
    WPD_OBJECT_FORMAT_M4A = DEFINE_GUID(
        0x30ABA7AC,
        0x6FFD,
        0x4C23,
        0xA3,
        0x59,
        0x3E,
        0x9B,
        0x52,
        0xF3,
        0xF1,
        0xC8
    )

    # WPD_OBJECT_FORMAT_NETWORK_ASSOCIATION
    # Network Association file format.
    WPD_OBJECT_FORMAT_NETWORK_ASSOCIATION = DEFINE_GUID(
        0xB1020000,
        0xAE6C,
        0x4804,
        0x98,
        0xBA,
        0xC5,
        0x7B,
        0x46,
        0x96,
        0x5F,
        0xE7
    )

    # WPD_OBJECT_FORMAT_X509V3CERTIFICATE
    # X.509 V3 Certificate file format.
    WPD_OBJECT_FORMAT_X509V3CERTIFICATE = DEFINE_GUID(
        0xB1030000,
        0xAE6C,
        0x4804,
        0x98,
        0xBA,
        0xC5,
        0x7B,
        0x46,
        0x96,
        0x5F,
        0xE7
    )

    # WPD_OBJECT_FORMAT_MICROSOFT_WFC
    # Windows Connect Now file format.
    WPD_OBJECT_FORMAT_MICROSOFT_WFC = DEFINE_GUID(
        0xB1040000,
        0xAE6C,
        0x4804,
        0x98,
        0xBA,
        0xC5,
        0x7B,
        0x46,
        0x96,
        0x5F,
        0xE7
    )

    # WPD_OBJECT_FORMAT_3GPA
    # Audio file format
    WPD_OBJECT_FORMAT_3GPA = DEFINE_GUID(
        0xE5172730,
        0xF971,
        0x41EF,
        0xA1,
        0x0B,
        0x22,
        0x71,
        0xA0,
        0x01,
        0x9D,
        0x7A
    )

    # WPD_OBJECT_FORMAT_3G2A
    # Audio file format
    WPD_OBJECT_FORMAT_3G2A = DEFINE_GUID(
        0x1A11202D,
        0x8759,
        0x4E34,
        0xBA,
        0x5E,
        0xB1,
        0x21,
        0x10,
        0x87,
        0xEE,
        0xE4
    )

    # WPD_OBJECT_FORMAT_ALL
    # This format is only valid as a parameter to API functions and driver
    # commands. It should not be reported as a supported format by the driver.
    WPD_OBJECT_FORMAT_ALL = DEFINE_GUID(
        0xC1F62EB2,
        0x4BB3,
        0x479C,
        0x9C,
        0xFA,
        0x05,
        0xB5,
        0xF3,
        0xA5,
        0x7B,
        0x22
    )

    # *************************************************************************
    # This section defines all Commands,
    # Parameters and Options associated with:
    # WPD_CATEGORY_NULL This category is used exclusively for the NULL
    # property key define.
    # *************************************************************************
    WPD_CATEGORY_NULL = DEFINE_GUID(
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

    # WPD_PROPERTY_NULL
    # [ VT_EMPTY ] A NULL property key.
    WPD_PROPERTY_NULL = DEFINE_PROPERTYKEY(
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
        0x0
    )

    # *************************************************************************
    # This section defines all Commands,
    # Parameters and Options associated with:
    # WPD_OBJECT_PROPERTIES_V1 This category is for all common object
    #  properties.
    # *************************************************************************
    WPD_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
        0xEF6B490D,
        0x5CD8,
        0x437A,
        0xAF,
        0xFC,
        0xDA,
        0x8B,
        0x60,
        0xEE,
        0x4A,
        0x3C
    )

    # WPD_OBJECT_CONTENT_TYPE
    # [ VT_CLSID ] The abstract type for the object content, indicating the
    # kinds of properties and data that may be supported on the object.
    WPD_OBJECT_CONTENT_TYPE = DEFINE_PROPERTYKEY(
        0xEF6B490D,
        0x5CD8,
        0x437A,
        0xAF,
        0xFC,
        0xDA,
        0x8B,
        0x60,
        0xEE,
        0x4A,
        0x3C,
        0x7
    )

    # WPD_OBJECT_REFERENCES
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR
    # indicating a list of ObjectIDs.
    WPD_OBJECT_REFERENCES = DEFINE_PROPERTYKEY(
        0xEF6B490D,
        0x5CD8,
        0x437A,
        0xAF,
        0xFC,
        0xDA,
        0x8B,
        0x60,
        0xEE,
        0x4A,
        0x3C,
        0xE
    )

    # WPD_OBJECT_CONTAINER_FUNCTIONAL_OBJECT_ID
    # [ VT_LPWSTR ] Indicates the Object ID of the closest functional object
    # ancestor. For example, objects that represent files/folders under a
    # Storage functional object, will have this property set to the object ID
    # of the storage functional object.
    WPD_OBJECT_CONTAINER_FUNCTIONAL_OBJECT_ID = DEFINE_PROPERTYKEY(
        0xEF6B490D,
        0x5CD8,
        0x437A,
        0xAF,
        0xFC,
        0xDA,
        0x8B,
        0x60,
        0xEE,
        0x4A,
        0x3C,
        0x17
    )

    # WPD_OBJECT_GENERATE_THUMBNAIL_FROM_RESOURCE
    # [ VT_BOOL ] Indicates whether the thumbnail for this object should be
    # generated from the default resource.
    WPD_OBJECT_GENERATE_THUMBNAIL_FROM_RESOURCE = DEFINE_PROPERTYKEY(
        0xEF6B490D,
        0x5CD8,
        0x437A,
        0xAF,
        0xFC,
        0xDA,
        0x8B,
        0x60,
        0xEE,
        0x4A,
        0x3C,
        0x18
    )

    # WPD_OBJECT_HINT_LOCATION_DISPLAY_NAME
    # [ VT_LPWSTR ] If this object appears as a hint location, this property
    # indicates the hint-specific name to display instead of the object name.
    WPD_OBJECT_HINT_LOCATION_DISPLAY_NAME = DEFINE_PROPERTYKEY(
        0xEF6B490D,
        0x5CD8,
        0x437A,
        0xAF,
        0xFC,
        0xDA,
        0x8B,
        0x60,
        0xEE,
        0x4A,
        0x3C,
        0x19
    )

    # *************************************************************************
    # This section defines all Commands,
    # Parameters and Options associated with: WPD_OBJECT_PROPERTIES_V2
    # This category is for all common object properties.
    # *************************************************************************
    WPD_OBJECT_PROPERTIES_V2 = DEFINE_GUID(
        0x0373CD3D,
        0x4A46,
        0x40D7,
        0xB4,
        0xD8,
        0x73,
        0xE8,
        0xDA,
        0x74,
        0xE7,
        0x75
    )

    # WPD_OBJECT_SUPPORTED_UNITS
    # [ VT_UI4 ] Indicates the units supported on this object.
    WPD_OBJECT_SUPPORTED_UNITS = DEFINE_PROPERTYKEY(
        0x0373CD3D,
        0x4A46,
        0x40D7,
        0xB4,
        0xD8,
        0x73,
        0xE8,
        0xDA,
        0x74,
        0xE7,
        0x75,
        0x2
    )

    # *************************************************************************
    # This section defines all Commands,
    # Parameters and Options associated with: WPD_FUNCTIONAL_OBJECT_PROPERTIES_V1
    #  This category is for properties common to all functional objects.
    # *************************************************************************
    WPD_FUNCTIONAL_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
        0x8F052D93,
        0xABCA,
        0x4FC5,
        0xA5,
        0xAC,
        0xB0,
        0x1D,
        0xF4,
        0xDB,
        0xE5,
        0x98
    )

    # WPD_FUNCTIONAL_OBJECT_CATEGORY
    # [ VT_CLSID ] Indicates the object's functional category.
    WPD_FUNCTIONAL_OBJECT_CATEGORY = DEFINE_PROPERTYKEY(
        0x8F052D93,
        0xABCA,
        0x4FC5,
        0xA5,
        0xAC,
        0xB0,
        0x1D,
        0xF4,
        0xDB,
        0xE5,
        0x98,
        0x2
    )

    # *************************************************************************
    # This section defines all Commands,
    # Parameters and Options associated with: WPD_STORAGE_OBJECT_PROPERTIES_V1
    # This category is for properties common to all objects whose functional
    # category is WPD_FUNCTIONAL_CATEGORY_STORAGE.
    # *************************************************************************
    WPD_STORAGE_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
        0x01A3057A,
        0x74D6,
        0x4E80,
        0xBE,
        0xA7,
        0xDC,
        0x4C,
        0x21,
        0x2C,
        0xE5,
        0x0A
    )

    # WPD_STORAGE_TYPE
    # [ VT_UI4 ] Indicates the type of storage e.g. fixed, removable etc.
    WPD_STORAGE_TYPE = DEFINE_PROPERTYKEY(
        0x01A3057A,
        0x74D6,
        0x4E80,
        0xBE,
        0xA7,
        0xDC,
        0x4C,
        0x21,
        0x2C,
        0xE5,
        0x0A,
        0x2
    )

    # WPD_STORAGE_FILE_SYSTEM_TYPE
    # [ VT_LPWSTR ] Indicates the file system type e.g. "FAT32" or "NTFS" or
    # "My Special File System"
    WPD_STORAGE_FILE_SYSTEM_TYPE = DEFINE_PROPERTYKEY(
        0x01A3057A,
        0x74D6,
        0x4E80,
        0xBE,
        0xA7,
        0xDC,
        0x4C,
        0x21,
        0x2C,
        0xE5,
        0x0A,
        0x3
    )

    # WPD_STORAGE_CAPACITY
    # [ VT_UI8 ] Indicates the total storage capacity in bytes.
    WPD_STORAGE_CAPACITY = DEFINE_PROPERTYKEY(
        0x01A3057A,
        0x74D6,
        0x4E80,
        0xBE,
        0xA7,
        0xDC,
        0x4C,
        0x21,
        0x2C,
        0xE5,
        0x0A,
        0x4
    )

    # WPD_STORAGE_FREE_SPACE_IN_BYTES
    # [ VT_UI8 ] Indicates the available space in bytes.
    WPD_STORAGE_FREE_SPACE_IN_BYTES = DEFINE_PROPERTYKEY(
        0x01A3057A,
        0x74D6,
        0x4E80,
        0xBE,
        0xA7,
        0xDC,
        0x4C,
        0x21,
        0x2C,
        0xE5,
        0x0A,
        0x5
    )

    # WPD_STORAGE_FREE_SPACE_IN_OBJECTS
    # [ VT_UI8 ] Indicates the available space in objects e.g. available slots
    # on a SIM card.
    WPD_STORAGE_FREE_SPACE_IN_OBJECTS = DEFINE_PROPERTYKEY(
        0x01A3057A,
        0x74D6,
        0x4E80,
        0xBE,
        0xA7,
        0xDC,
        0x4C,
        0x21,
        0x2C,
        0xE5,
        0x0A,
        0x6
    )

    # WPD_STORAGE_DESCRIPTION
    # [ VT_LPWSTR ] Contains a description of the storage.
    WPD_STORAGE_DESCRIPTION = DEFINE_PROPERTYKEY(
        0x01A3057A,
        0x74D6,
        0x4E80,
        0xBE,
        0xA7,
        0xDC,
        0x4C,
        0x21,
        0x2C,
        0xE5,
        0x0A,
        0x7
    )

    # WPD_STORAGE_SERIAL_NUMBER
    # [ VT_LPWSTR ] Contains the serial number of the storage.
    WPD_STORAGE_SERIAL_NUMBER = DEFINE_PROPERTYKEY(
        0x01A3057A,
        0x74D6,
        0x4E80,
        0xBE,
        0xA7,
        0xDC,
        0x4C,
        0x21,
        0x2C,
        0xE5,
        0x0A,
        0x8
    )

    # WPD_STORAGE_MAX_OBJECT_SIZE
    # [ VT_UI8 ] Specifies the maximum size of a single object (in bytes) that
    # can be placed on this storage.
    WPD_STORAGE_MAX_OBJECT_SIZE = DEFINE_PROPERTYKEY(
        0x01A3057A,
        0x74D6,
        0x4E80,
        0xBE,
        0xA7,
        0xDC,
        0x4C,
        0x21,
        0x2C,
        0xE5,
        0x0A,
        0x9
    )

    # WPD_STORAGE_CAPACITY_IN_OBJECTS
    # [ VT_UI8 ] Indicates the total storage capacity in objects e.g.
    # available slots on a SIM card.
    WPD_STORAGE_CAPACITY_IN_OBJECTS = DEFINE_PROPERTYKEY(
        0x01A3057A,
        0x74D6,
        0x4E80,
        0xBE,
        0xA7,
        0xDC,
        0x4C,
        0x21,
        0x2C,
        0xE5,
        0x0A,
        0xA
    )

    # WPD_STORAGE_ACCESS_CAPABILITY
    # [ VT_UI4 ] This property identifies any write-protection that globally
    # affects this storage. This takes precedence over access specified on
    # individual objects.
    WPD_STORAGE_ACCESS_CAPABILITY = DEFINE_PROPERTYKEY(
        0x01A3057A,
        0x74D6,
        0x4E80,
        0xBE,
        0xA7,
        0xDC,
        0x4C,
        0x21,
        0x2C,
        0xE5,
        0x0A,
        0xB
    )

    # *************************************************************************
    # This section defines all Commands, Parameters and Options
    # associated with: WPD_NETWORK_ASSOCIATION_PROPERTIES_V1
    # This category is for properties common to all network association
    # objects.
    # *************************************************************************
    WPD_NETWORK_ASSOCIATION_PROPERTIES_V1 = DEFINE_GUID(
        0xE4C93C1F,
        0xB203,
        0x43F1,
        0xA1,
        0x00,
        0x5A,
        0x07,
        0xD1,
        0x1B,
        0x02,
        0x74
    )

    # WPD_NETWORK_ASSOCIATION_HOST_NETWORK_IDENTIFIERS
    # [ VT_VECTOR | VT_UI1 ] The list of EUI-64 host identifiers valid for
    # this association.
    WPD_NETWORK_ASSOCIATION_HOST_NETWORK_IDENTIFIERS = DEFINE_PROPERTYKEY(
        0xE4C93C1F,
        0xB203,
        0x43F1,
        0xA1,
        0x00,
        0x5A,
        0x07,
        0xD1,
        0x1B,
        0x02,
        0x74,
        0x2
    )

    # WPD_NETWORK_ASSOCIATION_X509V3SEQUENCE
    # [ VT_VECTOR | VT_UI1 ] The sequence of X.509 v3 certificates to be
    # provided for TLS server authentication.
    WPD_NETWORK_ASSOCIATION_X509V3SEQUENCE = DEFINE_PROPERTYKEY(
        0xE4C93C1F,
        0xB203,
        0x43F1,
        0xA1,
        0x00,
        0x5A,
        0x07,
        0xD1,
        0x1B,
        0x02,
        0x74,
        0x3
    )

    # *************************************************************************
    # This section defines all Commands, Parameters and Options
    # associated with: WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1
    # This category is for properties common to all objects whose functional
    # category is WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE
    # *************************************************************************
    WPD_STILL_IMAGE_CAPTURE_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60
    )

    # WPD_STILL_IMAGE_CAPTURE_RESOLUTION
    # [ VT_LPWSTR ] Controls the size of the image dimensions to capture in
    # pixel width and height.
    WPD_STILL_IMAGE_CAPTURE_RESOLUTION = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x2
    )

    # WPD_STILL_IMAGE_CAPTURE_FORMAT
    # [ VT_CLSID ] Controls the format of the image to capture.
    WPD_STILL_IMAGE_CAPTURE_FORMAT = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x3
    )

    # WPD_STILL_IMAGE_COMPRESSION_SETTING
    # [ VT_UI8 ] Controls the device-specific quality setting.
    WPD_STILL_IMAGE_COMPRESSION_SETTING = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x4
    )

    # WPD_STILL_IMAGE_WHITE_BALANCE
    # [ VT_UI4 ] Controls how the device weights color channels.
    WPD_STILL_IMAGE_WHITE_BALANCE = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x5
    )

    # WPD_STILL_IMAGE_RGB_GAIN
    # [ VT_LPWSTR ] Controls the RGB gain.
    WPD_STILL_IMAGE_RGB_GAIN = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x6
    )

    # WPD_STILL_IMAGE_FNUMBER
    # [ VT_UI4 ] Controls the aperture of the lens.
    WPD_STILL_IMAGE_FNUMBER = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x7
    )

    # WPD_STILL_IMAGE_FOCAL_LENGTH
    # [ VT_UI4 ] Controls the 35mm equivalent focal length.
    WPD_STILL_IMAGE_FOCAL_LENGTH = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x8
    )

    # WPD_STILL_IMAGE_FOCUS_DISTANCE
    # [ VT_UI4 ] This property corresponds to the focus distance in millimeters
    WPD_STILL_IMAGE_FOCUS_DISTANCE = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x9
    )

    # WPD_STILL_IMAGE_FOCUS_MODE
    # [ VT_UI4 ] Identifies the focusing mode used by the device for image
    # capture.
    WPD_STILL_IMAGE_FOCUS_MODE = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0xA
    )

    # WPD_STILL_IMAGE_EXPOSURE_METERING_MODE
    # [ VT_UI4 ] Identifies the exposure metering mode used by the device for
    # image capture.
    WPD_STILL_IMAGE_EXPOSURE_METERING_MODE = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0xB
    )

    # WPD_STILL_IMAGE_FLASH_MODE
    # [ VT_UI4 ]
    WPD_STILL_IMAGE_FLASH_MODE = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0xC
    )

    # WPD_STILL_IMAGE_EXPOSURE_TIME
    # [ VT_UI4 ] Controls the shutter speed of the device.
    WPD_STILL_IMAGE_EXPOSURE_TIME = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0xD
    )

    # WPD_STILL_IMAGE_EXPOSURE_PROGRAM_MODE
    # [ VT_UI4 ] Controls the exposure program mode of the device.
    WPD_STILL_IMAGE_EXPOSURE_PROGRAM_MODE = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0xE
    )

    # WPD_STILL_IMAGE_EXPOSURE_INDEX
    # [ VT_UI4 ] Controls the emulation of film speed settings.
    WPD_STILL_IMAGE_EXPOSURE_INDEX = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0xF
    )

    # WPD_STILL_IMAGE_EXPOSURE_BIAS_COMPENSATION
    # [ VT_I4 ] Controls the adjustment of the auto exposure control.
    WPD_STILL_IMAGE_EXPOSURE_BIAS_COMPENSATION = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x10
    )

    # WPD_STILL_IMAGE_CAPTURE_DELAY
    # [ VT_UI4 ] Controls the amount of time delay between the capture trigger
    # and the actual data capture (in milliseconds).
    WPD_STILL_IMAGE_CAPTURE_DELAY = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x11
    )

    # WPD_STILL_IMAGE_CAPTURE_MODE
    # [ VT_UI4 ] Controls the type of still image capture.
    WPD_STILL_IMAGE_CAPTURE_MODE = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x12
    )

    # WPD_STILL_IMAGE_CONTRAST
    # [ VT_UI4 ] Controls the perceived contrast of captured images.
    WPD_STILL_IMAGE_CONTRAST = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x13
    )

    # WPD_STILL_IMAGE_SHARPNESS
    # [ VT_UI4 ] Controls the perceived sharpness of the captured image.
    WPD_STILL_IMAGE_SHARPNESS = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x14
    )

    # WPD_STILL_IMAGE_DIGITAL_ZOOM
    # [ VT_UI4 ] Controls the effective zoom ratio of a digital camera's
    # acquired image scaled by a factor of 10.
    WPD_STILL_IMAGE_DIGITAL_ZOOM = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x15
    )

    # WPD_STILL_IMAGE_EFFECT_MODE
    # [ VT_UI4 ] Controls the special effect mode of the capture.
    WPD_STILL_IMAGE_EFFECT_MODE = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x16
    )

    # WPD_STILL_IMAGE_BURST_NUMBER
    # [ VT_UI4 ] Controls the number of images that the device will attempt to
    # capture upon initiation of a burst operation.
    WPD_STILL_IMAGE_BURST_NUMBER = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x17
    )

    # WPD_STILL_IMAGE_BURST_INTERVAL
    # [ VT_UI4 ] Controls the time delay between captures upon initiation of a
    # burst operation.
    WPD_STILL_IMAGE_BURST_INTERVAL = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x18
    )

    # WPD_STILL_IMAGE_TIMELAPSE_NUMBER
    # [ VT_UI4 ] Controls the number of images that the device will attempt to
    # capture upon initiation of a time-lapse capture.
    WPD_STILL_IMAGE_TIMELAPSE_NUMBER = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x19
    )

    # WPD_STILL_IMAGE_TIMELAPSE_INTERVAL
    # [ VT_UI4 ] Controls the time delay between captures upon initiation of a
    # time-lapse operation.
    WPD_STILL_IMAGE_TIMELAPSE_INTERVAL = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x1A
    )

    # WPD_STILL_IMAGE_FOCUS_METERING_MODE
    # [ VT_UI4 ] Controls which automatic focus mechanism is used by the
    # device.
    WPD_STILL_IMAGE_FOCUS_METERING_MODE = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x1B
    )

    # WPD_STILL_IMAGE_UPLOAD_URL
    # [ VT_LPWSTR ] Used to describe the URL that the device may use to upload
    # images upon capture.
    WPD_STILL_IMAGE_UPLOAD_URL = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x1C
    )

    # WPD_STILL_IMAGE_ARTIST
    # [ VT_LPWSTR ] Contains the owner/user of the device, which may be
    # inserted as meta-data into any images that are captured.
    WPD_STILL_IMAGE_ARTIST = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x1D
    )

    # WPD_STILL_IMAGE_CAMERA_MODEL
    # [ VT_LPWSTR ] Contains the model of the device
    WPD_STILL_IMAGE_CAMERA_MODEL = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x1E
    )

    # WPD_STILL_IMAGE_CAMERA_MANUFACTURER
    # [ VT_LPWSTR ] Contains the manufacturer of the device
    WPD_STILL_IMAGE_CAMERA_MANUFACTURER = DEFINE_PROPERTYKEY(
        0x58C571EC,
        0x1BCB,
        0x42A7,
        0x8A,
        0xC5,
        0xBB,
        0x29,
        0x15,
        0x73,
        0xA2,
        0x60,
        0x1F
    )

    # *************************************************************************
    # This section defines all Commands, Parameters and Options
    # associated with: WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1
    # This category is for properties common to all objects whose functional
    # category is WPD_FUNCTIONAL_CATEGORY_AUDIO_RENDERING_INFORMATION
    # *************************************************************************
    WPD_RENDERING_INFORMATION_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
        0xC53D039F,
        0xEE23,
        0x4A31,
        0x85,
        0x90,
        0x76,
        0x39,
        0x87,
        0x98,
        0x70,
        0xB4
    )

    # WPD_RENDERING_INFORMATION_PROFILES
    # [ VT_UNKNOWN ] IPortableDeviceValuesCollection, where each element
    # indicates the property settings for a supported profile.
    WPD_RENDERING_INFORMATION_PROFILES = DEFINE_PROPERTYKEY(
        0xC53D039F,
        0xEE23,
        0x4A31,
        0x85,
        0x90,
        0x76,
        0x39,
        0x87,
        0x98,
        0x70,
        0xB4,
        0x2
    )

    # WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE
    # [ VT_UI4 ] Indicates whether a given entry
    # (i.e. an IPortableDeviceValues) in WPD_RENDERING_INFORMATION_PROFILES
    # relates to an Object or a Resource.
    WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE = DEFINE_PROPERTYKEY(
        0xC53D039F,
        0xEE23,
        0x4A31,
        0x85,
        0x90,
        0x76,
        0x39,
        0x87,
        0x98,
        0x70,
        0xB4,
        0x3
    )

    # WPD_RENDERING_INFORMATION_PROFILE_ENTRY_CREATABLE_RESOURCES
    # [ VT_UNKNOWN ] This is an IPortableDeviceKeyCollection identifying the
    # resources that can be created on an object with this rendering profile.
    WPD_RENDERING_INFORMATION_PROFILE_ENTRY_CREATABLE_RESOURCES = DEFINE_PROPERTYKEY(
        0xC53D039F,
        0xEE23,
        0x4A31,
        0x85,
        0x90,
        0x76,
        0x39,
        0x87,
        0x98,
        0x70,
        0xB4,
        0x4
    )

    # *************************************************************************
    # This section defines all Commands, Parameters and Options
    # associated with: WPD_CLIENT_INFORMATION_PROPERTIES_V1
    # *************************************************************************
    WPD_CLIENT_INFORMATION_PROPERTIES_V1 = DEFINE_GUID(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59
    )

    # WPD_CLIENT_NAME
    # [ VT_LPWSTR ] Specifies the name the client uses to identify itself.
    WPD_CLIENT_NAME = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0x2
    )

    # WPD_CLIENT_MAJOR_VERSION
    # [ VT_UI4 ] Specifies the major version of the client.
    WPD_CLIENT_MAJOR_VERSION = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0x3
    )

    # WPD_CLIENT_MINOR_VERSION
    # [ VT_UI4 ] Specifies the major version of the client.
    WPD_CLIENT_MINOR_VERSION = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0x4
    )

    # WPD_CLIENT_REVISION
    # [ VT_UI4 ] Specifies the revision (or build number) of the client.
    WPD_CLIENT_REVISION = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0x5
    )

    # WPD_CLIENT_WMDRM_APPLICATION_PRIVATE_KEY
    # [ VT_VECTOR | VT_UI1 ] Specifies the Windows Media DRM application
    # private key of the client.
    WPD_CLIENT_WMDRM_APPLICATION_PRIVATE_KEY = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0x6
    )

    # WPD_CLIENT_WMDRM_APPLICATION_CERTIFICATE
    # [ VT_VECTOR | VT_UI1 ] Specifies the Windows Media DRM application
    # certificate of the client.
    WPD_CLIENT_WMDRM_APPLICATION_CERTIFICATE = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0x7
    )

    # WPD_CLIENT_SECURITY_QUALITY_OF_SERVICE
    # [ VT_UI4 ] Specifies the Security Quality of Service for the connection
    # to the driver. This relates to the Security Quality of Service flags for
    # CreateFile. For example, these allow or disallow a driver to impersonate
    # the client.
    WPD_CLIENT_SECURITY_QUALITY_OF_SERVICE = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0x8
    )

    # WPD_CLIENT_DESIRED_ACCESS
    # [ VT_UI4 ] Specifies the desired access the client is requesting to this
    # driver. The possible values are the same as for CreateFile
    # (e.g. GENERIC_READ, GENERIC_WRITE etc.).
    WPD_CLIENT_DESIRED_ACCESS = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0x9
    )

    # WPD_CLIENT_SHARE_MODE
    # [ VT_UI4 ] Specifies the share mode the client is requesting to this
    # driver. The possible values are the same as for CreateFile
    # (e.g. FILE_SHARE_READ, FILE_SHARE_WRITE etc.).
    WPD_CLIENT_SHARE_MODE = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0xA
    )

    # WPD_CLIENT_EVENT_COOKIE
    # [ VT_LPWSTR ] Client supplied cookie returned by the driver in events
    # posted as a direct result of operations issued by this client.
    WPD_CLIENT_EVENT_COOKIE = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0xB
    )

    # WPD_CLIENT_MINIMUM_RESULTS_BUFFER_SIZE
    # [ VT_UI4 ] Specifies the minimum buffer size (in bytes) used for sending
    # commands to the driver.
    WPD_CLIENT_MINIMUM_RESULTS_BUFFER_SIZE = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0xC
    )

    # WPD_CLIENT_MANUAL_CLOSE_ON_DISCONNECT
    # [ VT_BOOL ] An advanced option for clients that wish to manually call
    # IPortableDevice::Close or IPortableDeviceService::Close for each object
    # on device disconnect, instead of relying on the API to call Close on its
    # behalf.
    WPD_CLIENT_MANUAL_CLOSE_ON_DISCONNECT = DEFINE_PROPERTYKEY(
        0x204D9F0C,
        0x2292,
        0x4080,
        0x9F,
        0x42,
        0x40,
        0x66,
        0x4E,
        0x70,
        0xF8,
        0x59,
        0xD
    )

    # *************************************************************************
    # This section defines all Commands, Parameters and Options
    # associated with: WPD_PROPERTY_ATTRIBUTES_V1
    # *************************************************************************
    WPD_PROPERTY_ATTRIBUTES_V1 = DEFINE_GUID(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37
    )

    # WPD_PROPERTY_ATTRIBUTE_FORM
    # [ VT_UI4 ] Specifies the form of the valid values allowed for this
    # property.
    WPD_PROPERTY_ATTRIBUTE_FORM = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0x2
    )

    # WPD_PROPERTY_ATTRIBUTE_CAN_READ
    # [ VT_BOOL ] Indicates whether client applications have permission to
    # Read the property.
    WPD_PROPERTY_ATTRIBUTE_CAN_READ = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0x3
    )

    # WPD_PROPERTY_ATTRIBUTE_CAN_WRITE
    # [ VT_BOOL ] Indicates whether client applications have permission to
    # Write the property.
    WPD_PROPERTY_ATTRIBUTE_CAN_WRITE = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0x4
    )

    # WPD_PROPERTY_ATTRIBUTE_CAN_DELETE
    # [ VT_BOOL ] Indicates whether client applications have permission to
    # Delete the property.
    WPD_PROPERTY_ATTRIBUTE_CAN_DELETE = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0x5
    )

    # WPD_PROPERTY_ATTRIBUTE_DEFAULT_VALUE
    # [ VT_XXXX ] Specifies the default value for a write-able property.
    WPD_PROPERTY_ATTRIBUTE_DEFAULT_VALUE = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0x6
    )

    # WPD_PROPERTY_ATTRIBUTE_FAST_PROPERTY
    # [ VT_BOOL ] If True, then this property belongs to the
    # PORTABLE_DEVICE_FAST_PROPERTIES group.
    WPD_PROPERTY_ATTRIBUTE_FAST_PROPERTY = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0x7
    )

    # WPD_PROPERTY_ATTRIBUTE_RANGE_MIN
    # [ VT_XXXX ] The minimum value for a property whose form is of
    # WPD_PROPERTY_ATTRIBUTE_FORM_RANGE.
    WPD_PROPERTY_ATTRIBUTE_RANGE_MIN = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0x8
    )

    # WPD_PROPERTY_ATTRIBUTE_RANGE_MAX
    # [ VT_XXXX ] The maximum value for a property whose form is of
    # WPD_PROPERTY_ATTRIBUTE_FORM_RANGE.
    WPD_PROPERTY_ATTRIBUTE_RANGE_MAX = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0x9
    )

    # WPD_PROPERTY_ATTRIBUTE_RANGE_STEP
    # [ VT_XXXX ] The step value for a property whose form is of
    # WPD_PROPERTY_ATTRIBUTE_FORM_RANGE.
    WPD_PROPERTY_ATTRIBUTE_RANGE_STEP = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0xA
    )

    # WPD_PROPERTY_ATTRIBUTE_ENUMERATION_ELEMENTS
    # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection containing the
    # enumeration values.
    WPD_PROPERTY_ATTRIBUTE_ENUMERATION_ELEMENTS = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0xB
    )

    # WPD_PROPERTY_ATTRIBUTE_REGULAR_EXPRESSION
    # [ VT_LPWSTR ] A regular expression string indicating acceptable values
    # for properties whose form is
    # WPD_PROPERTY_ATTRIBUTE_FORM_REGULAR_EXPRESSION.
    WPD_PROPERTY_ATTRIBUTE_REGULAR_EXPRESSION = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0xC
    )

    # WPD_PROPERTY_ATTRIBUTE_MAX_SIZE
    # [ VT_UI8 ] This indicates the maximum size (in bytes) for the value of
    # this property.
    WPD_PROPERTY_ATTRIBUTE_MAX_SIZE = DEFINE_PROPERTYKEY(
        0xAB7943D8,
        0x6332,
        0x445F,
        0xA0,
        0x0D,
        0x8D,
        0x5E,
        0xF1,
        0xE9,
        0x6F,
        0x37,
        0xD
    )

    # *************************************************************************
    # This section defines all Commands, Parameters and Options
    # associated with: WPD_PROPERTY_ATTRIBUTES_V2
    # This category defines additional property attributes used by
    #  device services.
    # *************************************************************************
    WPD_PROPERTY_ATTRIBUTES_V2 = DEFINE_GUID(
        0x5D9DA160,
        0x74AE,
        0x43CC,
        0x85,
        0xA9,
        0xFE,
        0x55,
        0x5A,
        0x80,
        0x79,
        0x8E
    )

    # WPD_PROPERTY_ATTRIBUTE_NAME
    # [ VT_LPWSTR ] Contains the name of the property.
    WPD_PROPERTY_ATTRIBUTE_NAME = DEFINE_PROPERTYKEY(
        0x5D9DA160,
        0x74AE,
        0x43CC,
        0x85,
        0xA9,
        0xFE,
        0x55,
        0x5A,
        0x80,
        0x79,
        0x8E,
        0x2
    )

    # WPD_PROPERTY_ATTRIBUTE_VARTYPE
    # [ VT_UI4 ] Contains the VARTYPE of the property.
    WPD_PROPERTY_ATTRIBUTE_VARTYPE = DEFINE_PROPERTYKEY(
        0x5D9DA160,
        0x74AE,
        0x43CC,
        0x85,
        0xA9,
        0xFE,
        0x55,
        0x5A,
        0x80,
        0x79,
        0x8E,
        0x3
    )

    # *************************************************************************
    # This section defines all Commands, Parameters and Options
    # associated with: WPD_CLASS_EXTENSION_OPTIONS_V1
    # This category of properties relates to options used for the WPD
    # device class extension
    # *************************************************************************
    WPD_CLASS_EXTENSION_OPTIONS_V1 = DEFINE_GUID(
        0x6309FFEF,
        0xA87C,
        0x4CA7,
        0x84,
        0x34,
        0x79,
        0x75,
        0x76,
        0xE4,
        0x0A,
        0x96
    )

    # WPD_CLASS_EXTENSION_OPTIONS_SUPPORTED_CONTENT_TYPES
    # [ VT_UNKNOWN ] Indicates the (super-set) list of content types supported
    # by the driver
    # (similar to calling WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES on WPD_FUNCTIONAL_CATEGORY_ALL).
    #
    WPD_CLASS_EXTENSION_OPTIONS_SUPPORTED_CONTENT_TYPES = DEFINE_PROPERTYKEY(
        0x6309FFEF,
        0xA87C,
        0x4CA7,
        0x84,
        0x34,
        0x79,
        0x75,
        0x76,
        0xE4,
        0x0A,
        0x96,
        0x2
    )

    # WPD_CLASS_EXTENSION_OPTIONS_DONT_REGISTER_WPD_DEVICE_INTERFACE
    # [ VT_BOOL ] Indicates that the caller does not want the WPD class
    # extension library to register the WPD Device Class interface. The caller
    # will take responsibility for doing it.
    WPD_CLASS_EXTENSION_OPTIONS_DONT_REGISTER_WPD_DEVICE_INTERFACE = DEFINE_PROPERTYKEY(
        0x6309FFEF,
        0xA87C,
        0x4CA7,
        0x84,
        0x34,
        0x79,
        0x75,
        0x76,
        0xE4,
        0x0A,
        0x96,
        0x3
    )

    # WPD_CLASS_EXTENSION_OPTIONS_REGISTER_WPD_PRIVATE_DEVICE_INTERFACE
    # [ VT_BOOL ] Indicates that the caller wants the WPD class extension
    # library to register the private WPD Device Class interface.
    WPD_CLASS_EXTENSION_OPTIONS_REGISTER_WPD_PRIVATE_DEVICE_INTERFACE = DEFINE_PROPERTYKEY(
        0x6309FFEF,
        0xA87C,
        0x4CA7,
        0x84,
        0x34,
        0x79,
        0x75,
        0x76,
        0xE4,
        0x0A,
        0x96,
        0x4
    )

    # *************************************************************************
    # This section defines all Commands, Parameters and Options
    # associated with: WPD_CLASS_EXTENSION_OPTIONS_V2
    # This category of properties relates to options used for the WPD
    #  device class extension
    # *************************************************************************
    WPD_CLASS_EXTENSION_OPTIONS_V2 = DEFINE_GUID(
        0x3E3595DA,
        0x4D71,
        0x49FE,
        0xA0,
        0xB4,
        0xD4,
        0x40,
        0x6C,
        0x3A,
        0xE9,
        0x3F
    )

    # WPD_CLASS_EXTENSION_OPTIONS_MULTITRANSPORT_MODE
    # [ VT_BOOL ] Indicates that the caller wants the WPD class extension
    # library to go into Multi-Transport mode (if TRUE).
    WPD_CLASS_EXTENSION_OPTIONS_MULTITRANSPORT_MODE = DEFINE_PROPERTYKEY(
        0x3E3595DA,
        0x4D71,
        0x49FE,
        0xA0,
        0xB4,
        0xD4,
        0x40,
        0x6C,
        0x3A,
        0xE9,
        0x3F,
        0x2
    )

    # WPD_CLASS_EXTENSION_OPTIONS_DEVICE_IDENTIFICATION_VALUES
    # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the
    # device identification values
    # (WPD_DEVICE_MANUFACTURER, WPD_DEVICE_MODEL,
    # WPD_DEVICE_FIRMWARE_VERSION and WPD_DEVICE_FUNCTIONAL_UNIQUE_ID).
    # Include this with other Class Extension options when initializing.
    #
    WPD_CLASS_EXTENSION_OPTIONS_DEVICE_IDENTIFICATION_VALUES = DEFINE_PROPERTYKEY(
        0x3E3595DA,
        0x4D71,
        0x49FE,
        0xA0,
        0xB4,
        0xD4,
        0x40,
        0x6C,
        0x3A,
        0xE9,
        0x3F,
        0x3
    )

    # WPD_CLASS_EXTENSION_OPTIONS_TRANSPORT_BANDWIDTH
    # [ VT_UI4 ] Indicates the theoretical maximum bandwidth of the transport
    # in kilobits per second.
    WPD_CLASS_EXTENSION_OPTIONS_TRANSPORT_BANDWIDTH = DEFINE_PROPERTYKEY(
        0x3E3595DA,
        0x4D71,
        0x49FE,
        0xA0,
        0xB4,
        0xD4,
        0x40,
        0x6C,
        0x3A,
        0xE9,
        0x3F,
        0x4
    )

    # *************************************************************************
    # This section defines all Commands, Parameters and Options
    # associated with: WPD_CLASS_EXTENSION_OPTIONS_V3
    # This category of properties relates to options used for the WPD
    # device class extension
    # *************************************************************************
    WPD_CLASS_EXTENSION_OPTIONS_V3 = DEFINE_GUID(
        0x65C160F8,
        0x1367,
        0x4CE2,
        0x93,
        0x9D,
        0x83,
        0x10,
        0x83,
        0x9F,
        0x0D,
        0x30
    )

    # WPD_CLASS_EXTENSION_OPTIONS_SILENCE_AUTOPLAY
    # [ VT_BOOL ] Indicates that the caller wants Autoplay to be silent when
    # the device is connected (if TRUE).
    WPD_CLASS_EXTENSION_OPTIONS_SILENCE_AUTOPLAY = DEFINE_PROPERTYKEY(
        0x65C160F8,
        0x1367,
        0x4CE2,
        0x93,
        0x9D,
        0x83,
        0x10,
        0x83,
        0x9F,
        0x0D,
        0x30,
        0x2
    )

    # *************************************************************************
    # This section defines all Commands, Parameters and Options
    # associated with: WPD_RESOURCE_ATTRIBUTES_V1
    # *************************************************************************
    WPD_RESOURCE_ATTRIBUTES_V1 = DEFINE_GUID(
        0x1EB6F604,
        0x9278,
        0x429F,
        0x93,
        0xCC,
        0x5B,
        0xB8,
        0xC0,
        0x66,
        0x56,
        0xB6
    )

    # WPD_RESOURCE_ATTRIBUTE_TOTAL_SIZE
    # [ VT_UI8 ] Total size in bytes of the resource data.
    WPD_RESOURCE_ATTRIBUTE_TOTAL_SIZE = DEFINE_PROPERTYKEY(
        0x1EB6F604,
        0x9278,
        0x429F,
        0x93,
        0xCC,
        0x5B,
        0xB8,
        0xC0,
        0x66,
        0x56,
        0xB6,
        0x2
    )

    # WPD_RESOURCE_ATTRIBUTE_CAN_READ
    # [ VT_BOOL ] Indicates whether client applications have permission to
    # open the resource for Read access.
    WPD_RESOURCE_ATTRIBUTE_CAN_READ = DEFINE_PROPERTYKEY(
        0x1EB6F604,
        0x9278,
        0x429F,
        0x93,
        0xCC,
        0x5B,
        0xB8,
        0xC0,
        0x66,
        0x56,
        0xB6,
        0x3
    )

    # WPD_RESOURCE_ATTRIBUTE_CAN_WRITE
    # [ VT_BOOL ] Indicates whether client applications have permission to
    # open the resource for Write access.
    WPD_RESOURCE_ATTRIBUTE_CAN_WRITE = DEFINE_PROPERTYKEY(
        0x1EB6F604,
        0x9278,
        0x429F,
        0x93,
        0xCC,
        0x5B,
        0xB8,
        0xC0,
        0x66,
        0x56,
        0xB6,
        0x4
    )

    # WPD_RESOURCE_ATTRIBUTE_CAN_DELETE
    # [ VT_BOOL ] Indicates whether client applications have permission to
    # Delete a resource from the device.
    WPD_RESOURCE_ATTRIBUTE_CAN_DELETE = DEFINE_PROPERTYKEY(
        0x1EB6F604,
        0x9278,
        0x429F,
        0x93,
        0xCC,
        0x5B,
        0xB8,
        0xC0,
        0x66,
        0x56,
        0xB6,
        0x5
    )

    # WPD_RESOURCE_ATTRIBUTE_OPTIMAL_READ_BUFFER_SIZE
    # [ VT_UI4 ] The recommended buffer size a caller should use when doing
    # buffered reads on the resource.
    WPD_RESOURCE_ATTRIBUTE_OPTIMAL_READ_BUFFER_SIZE = DEFINE_PROPERTYKEY(
        0x1EB6F604,
        0x9278,
        0x429F,
        0x93,
        0xCC,
        0x5B,
        0xB8,
        0xC0,
        0x66,
        0x56,
        0xB6,
        0x6
    )

    # WPD_RESOURCE_ATTRIBUTE_OPTIMAL_WRITE_BUFFER_SIZE
    # [ VT_UI4 ] The recommended buffer size a caller should use when doing
    # buffered writes on the resource.
    WPD_RESOURCE_ATTRIBUTE_OPTIMAL_WRITE_BUFFER_SIZE = DEFINE_PROPERTYKEY(
        0x1EB6F604,
        0x9278,
        0x429F,
        0x93,
        0xCC,
        0x5B,
        0xB8,
        0xC0,
        0x66,
        0x56,
        0xB6,
        0x7
    )

    # WPD_RESOURCE_ATTRIBUTE_FORMAT
    # [ VT_CLSID ] Indicates the format of the resource data.
    WPD_RESOURCE_ATTRIBUTE_FORMAT = DEFINE_PROPERTYKEY(
        0x1EB6F604,
        0x9278,
        0x429F,
        0x93,
        0xCC,
        0x5B,
        0xB8,
        0xC0,
        0x66,
        0x56,
        0xB6,
        0x8
    )

    # WPD_RESOURCE_ATTRIBUTE_RESOURCE_KEY
    # [ VT_UNKNOWN ] This is an IPortableDeviceKeyCollection containing a
    # single value, which is the key identifying the resource.
    WPD_RESOURCE_ATTRIBUTE_RESOURCE_KEY = DEFINE_PROPERTYKEY(
        0x1EB6F604,
        0x9278,
        0x429F,
        0x93,
        0xCC,
        0x5B,
        0xB8,
        0xC0,
        0x66,
        0x56,
        0xB6,
        0x9
    )

    # *************************************************************************
    #  This section defines all Commands, Parameters and Options
    # associated with: WPD_DEVICE_PROPERTIES_V1
    # *************************************************************************
    WPD_DEVICE_PROPERTIES_V1 = DEFINE_GUID(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC
    )

    # WPD_DEVICE_SYNC_PARTNER
    # [ VT_LPWSTR ] Indicates a human-readable description of a
    # synchronization partner for the device.
    WPD_DEVICE_SYNC_PARTNER = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0x2
    )

    # WPD_DEVICE_FIRMWARE_VERSION
    # [ VT_LPWSTR ] Indicates the firmware version for the device.
    WPD_DEVICE_FIRMWARE_VERSION = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0x3
    )

    # WPD_DEVICE_POWER_LEVEL
    # [ VT_UI4 ] Indicates the power level of the device's battery.
    WPD_DEVICE_POWER_LEVEL = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0x4
    )


    # WPD_DEVICE_POWER_SOURCE
    # [ VT_UI4 ] Indicates the power source of the device e.g. whether it is
    # battery or external.
    WPD_DEVICE_POWER_SOURCE = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0x5
    )

    # WPD_DEVICE_PROTOCOL
    # [ VT_LPWSTR ] Identifies the device protocol being used.
    WPD_DEVICE_PROTOCOL = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0x6
    )


    # WPD_DEVICE_MANUFACTURER
    # [ VT_LPWSTR ] Identifies the device manufacturer.
    WPD_DEVICE_MANUFACTURER = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0x7
    )

    # WPD_DEVICE_MODEL
    # [ VT_LPWSTR ] Identifies the device model.
    WPD_DEVICE_MODEL = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0x8
    )


    # WPD_DEVICE_SERIAL_NUMBER
    # [ VT_LPWSTR ] Identifies the serial number of the device.
    WPD_DEVICE_SERIAL_NUMBER = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0x9
    )

    # WPD_DEVICE_SUPPORTS_NON_CONSUMABLE
    # [ VT_BOOL ] Indicates whether the device supports non-consumable objects.
    WPD_DEVICE_SUPPORTS_NON_CONSUMABLE = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0xA
    )


    # WPD_DEVICE_DATETIME
    # [ VT_DATE ] Represents the current date and time settings of the device.
    WPD_DEVICE_DATETIME = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0xB
    )

    # WPD_DEVICE_FRIENDLY_NAME
    # [ VT_LPWSTR ] Represents the friendly name set by the user on the device.
    WPD_DEVICE_FRIENDLY_NAME = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0xC
    )


    # WPD_DEVICE_SUPPORTED_DRM_SCHEMES
    # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of VT_LPWSTR
    # values indicating the Digital Rights Management schemes supported by the
    # driver.
    WPD_DEVICE_SUPPORTED_DRM_SCHEMES = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0xD
    )

    # WPD_DEVICE_SUPPORTED_FORMATS_ARE_ORDERED
    # [ VT_BOOL ] Indicates whether the supported formats returned from the
    # device are in a preferred order.
    # (First format in the list is most preferred by the device, while the last is the least preferred.)
    #
    WPD_DEVICE_SUPPORTED_FORMATS_ARE_ORDERED = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0xE
    )


    # WPD_DEVICE_TYPE
    # [ VT_UI4 ] Indicates the device type, used for representation purposes
    # only. Functional characteristics of the device are decided through
    # functional objects.
    WPD_DEVICE_TYPE = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0xF
    )

    # WPD_DEVICE_NETWORK_IDENTIFIER
    # [ VT_UI8 ] Indicates the EUI-64 network identifier of the device, used
    # for out-of-band Network Association operations.
    WPD_DEVICE_NETWORK_IDENTIFIER = DEFINE_PROPERTYKEY(
        0x26D4979A,
        0xE643,
        0x4626,
        0x9E,
        0x2B,
        0x73,
        0x6D,
        0xC0,
        0xC9,
        0x2F,
        0xDC,
        0x10
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_DEVICE_PROPERTIES_V2 *************************************************************************
    #
    WPD_DEVICE_PROPERTIES_V2 = DEFINE_GUID(
        0x463DD662,
        0x7FC4,
        0x4291,
        0x91,
        0x1C,
        0x7F,
        0x4C,
        0x9C,
        0xCA,
        0x97,
        0x99
    )


    # WPD_DEVICE_FUNCTIONAL_UNIQUE_ID
    # [ VT_VECTOR | VT_UI1 ] Indicates a unique 16 byte identifier common
    # across multiple transports supported by the device.
    WPD_DEVICE_FUNCTIONAL_UNIQUE_ID = DEFINE_PROPERTYKEY(
        0x463DD662,
        0x7FC4,
        0x4291,
        0x91,
        0x1C,
        0x7F,
        0x4C,
        0x9C,
        0xCA,
        0x97,
        0x99,
        0x2
    )

    # WPD_DEVICE_MODEL_UNIQUE_ID
    # [ VT_VECTOR | VT_UI1 ] Indicates a unique 16 byte identifier for
    # cosmetic differentiation among different models of the device.
    WPD_DEVICE_MODEL_UNIQUE_ID = DEFINE_PROPERTYKEY(
        0x463DD662,
        0x7FC4,
        0x4291,
        0x91,
        0x1C,
        0x7F,
        0x4C,
        0x9C,
        0xCA,
        0x97,
        0x99,
        0x3
    )


    # WPD_DEVICE_TRANSPORT
    # [ VT_UI4 ] Indicates the transport type (USB, IP, Bluetooth, etc.).
    WPD_DEVICE_TRANSPORT = DEFINE_PROPERTYKEY(
        0x463DD662,
        0x7FC4,
        0x4291,
        0x91,
        0x1C,
        0x7F,
        0x4C,
        0x9C,
        0xCA,
        0x97,
        0x99,
        0x4
    )

    # WPD_DEVICE_USE_DEVICE_STAGE
    # [ VT_BOOL ] If this property exists and is set to TRUE, the device can
    # be used with Device Stage.
    WPD_DEVICE_USE_DEVICE_STAGE = DEFINE_PROPERTYKEY(
        0x463DD662,
        0x7FC4,
        0x4291,
        0x91,
        0x1C,
        0x7F,
        0x4C,
        0x9C,
        0xCA,
        0x97,
        0x99,
        0x5
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_DEVICE_PROPERTIES_V3 *************************************************************************
    #
    WPD_DEVICE_PROPERTIES_V3 = DEFINE_GUID(
        0x6C2B878C,
        0xC2EC,
        0x490D,
        0xB4,
        0x25,
        0xD7,
        0xA7,
        0x5E,
        0x23,
        0xE5,
        0xED
    )


    # WPD_DEVICE_EDP_IDENTITY
    # [ VT_LPWSTR ] Represents EDP identity of the device.
    WPD_DEVICE_EDP_IDENTITY = DEFINE_PROPERTYKEY(
        0x6C2B878C,
        0xC2EC,
        0x490D,
        0xB4,
        0x25,
        0xD7,
        0xA7,
        0x5E,
        0x23,
        0xE5,
        0xED,
        0x1
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_SERVICE_PROPERTIES_V1 *************************************************************************
    #
    WPD_SERVICE_PROPERTIES_V1 = DEFINE_GUID(
        0x7510698A,
        0xCB54,
        0x481C,
        0xB8,
        0xDB,
        0x0D,
        0x75,
        0xC9,
        0x3F,
        0x1C,
        0x06
    )

    # WPD_SERVICE_VERSION
    # [ VT_LPWSTR ] Indicates the implementation version of a service.
    WPD_SERVICE_VERSION = DEFINE_PROPERTYKEY(
        0x7510698A,
        0xCB54,
        0x481C,
        0xB8,
        0xDB,
        0x0D,
        0x75,
        0xC9,
        0x3F,
        0x1C,
        0x06,
        0x2
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_EVENT_PROPERTIES_V1 The properties in this category are for properties that may be needed for event processing, but do not have object property equivalents (i.e. they are not exposed as object properties, but rather, used only as event parameters). *************************************************************************
    #
    WPD_EVENT_PROPERTIES_V1 = DEFINE_GUID(
        0x15AB1953,
        0xF817,
        0x4FEF,
        0xA9,
        0x21,
        0x56,
        0x76,
        0xE8,
        0x38,
        0xF6,
        0xE0
    )


    # WPD_EVENT_PARAMETER_PNP_DEVICE_ID
    # [ VT_LPWSTR ] Indicates the device that originated the event.
    WPD_EVENT_PARAMETER_PNP_DEVICE_ID = DEFINE_PROPERTYKEY(
        0x15AB1953,
        0xF817,
        0x4FEF,
        0xA9,
        0x21,
        0x56,
        0x76,
        0xE8,
        0x38,
        0xF6,
        0xE0,
        0x2
    )

    # WPD_EVENT_PARAMETER_EVENT_ID
    # [ VT_CLSID ] Indicates the event sent.
    WPD_EVENT_PARAMETER_EVENT_ID = DEFINE_PROPERTYKEY(
        0x15AB1953,
        0xF817,
        0x4FEF,
        0xA9,
        0x21,
        0x56,
        0x76,
        0xE8,
        0x38,
        0xF6,
        0xE0,
        0x3
    )


    # WPD_EVENT_PARAMETER_OPERATION_STATE
    # [ VT_UI4 ] Indicates the current state of the operation
    # (e.g. started, running, stopped etc.).
    WPD_EVENT_PARAMETER_OPERATION_STATE = DEFINE_PROPERTYKEY(
        0x15AB1953,
        0xF817,
        0x4FEF,
        0xA9,
        0x21,
        0x56,
        0x76,
        0xE8,
        0x38,
        0xF6,
        0xE0,
        0x4
    )

    # WPD_EVENT_PARAMETER_OPERATION_PROGRESS
    # [ VT_UI4 ] Indicates the progress of a currently executing operation.
    # Value is from 0 to 100, with 100 indicating that the operation is
    # complete.
    WPD_EVENT_PARAMETER_OPERATION_PROGRESS = DEFINE_PROPERTYKEY(
        0x15AB1953,
        0xF817,
        0x4FEF,
        0xA9,
        0x21,
        0x56,
        0x76,
        0xE8,
        0x38,
        0xF6,
        0xE0,
        0x5
    )


    # WPD_EVENT_PARAMETER_OBJECT_PARENT_PERSISTENT_UNIQUE_ID
    # [ VT_LPWSTR ] Uniquely identifies the parent object, similar to
    # WPD_OBJECT_PARENT_ID, but this ID will not change between sessions.
    WPD_EVENT_PARAMETER_OBJECT_PARENT_PERSISTENT_UNIQUE_ID = DEFINE_PROPERTYKEY(
        0x15AB1953,
        0xF817,
        0x4FEF,
        0xA9,
        0x21,
        0x56,
        0x76,
        0xE8,
        0x38,
        0xF6,
        0xE0,
        0x6
    )

    # WPD_EVENT_PARAMETER_OBJECT_CREATION_COOKIE
    # [ VT_LPWSTR ] This is the cookie handed back to a client when it
    # requested an object creation using the
    # IPortableDeviceContent::CreateObjectWithPropertiesAndData method.
    WPD_EVENT_PARAMETER_OBJECT_CREATION_COOKIE = DEFINE_PROPERTYKEY(
        0x15AB1953,
        0xF817,
        0x4FEF,
        0xA9,
        0x21,
        0x56,
        0x76,
        0xE8,
        0x38,
        0xF6,
        0xE0,
        0x7
    )


    # WPD_EVENT_PARAMETER_CHILD_HIERARCHY_CHANGED
    # [ VT_BOOL ] Indicates that the child hiearchy for the object has changed.
    WPD_EVENT_PARAMETER_CHILD_HIERARCHY_CHANGED = DEFINE_PROPERTYKEY(
        0x15AB1953,
        0xF817,
        0x4FEF,
        0xA9,
        0x21,
        0x56,
        0x76,
        0xE8,
        0x38,
        0xF6,
        0xE0,
        0x8
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_EVENT_PROPERTIES_V2 The properties in this category are for properties that may be needed for event processing, but do not have object property equivalents (i.e. they are not exposed as object properties, but rather, used only as event parameters). *************************************************************************
    #
    WPD_EVENT_PROPERTIES_V2 = DEFINE_GUID(
        0x52807B8A,
        0x4914,
        0x4323,
        0x9B,
        0x9A,
        0x74,
        0xF6,
        0x54,
        0xB2,
        0xB8,
        0x46
    )

    # WPD_EVENT_PARAMETER_SERVICE_METHOD_CONTEXT
    # [ VT_LPWSTR ] Indicates the service method invocation context.
    WPD_EVENT_PARAMETER_SERVICE_METHOD_CONTEXT = DEFINE_PROPERTYKEY(
        0x52807B8A,
        0x4914,
        0x4323,
        0x9B,
        0x9A,
        0x74,
        0xF6,
        0x54,
        0xB2,
        0xB8,
        0x46,
        0x2
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_EVENT_OPTIONS_V1 The properties in this category describe event options. *************************************************************************
    #
    WPD_EVENT_OPTIONS_V1 = DEFINE_GUID(
        0xB3D8DAD7,
        0xA361,
        0x4B83,
        0x8A,
        0x48,
        0x5B,
        0x02,
        0xCE,
        0x10,
        0x71,
        0x3B
    )


    # WPD_EVENT_OPTION_IS_BROADCAST_EVENT
    # [ VT_BOOL ] Indicates that the event is broadcast to all clients.
    WPD_EVENT_OPTION_IS_BROADCAST_EVENT = DEFINE_PROPERTYKEY(
        0xB3D8DAD7,
        0xA361,
        0x4B83,
        0x8A,
        0x48,
        0x5B,
        0x02,
        0xCE,
        0x10,
        0x71,
        0x3B,
        0x2
    )

    # WPD_EVENT_OPTION_IS_AUTOPLAY_EVENT
    # [ VT_BOOL ] Indicates that the event is sent to and handled by Autoplay.
    WPD_EVENT_OPTION_IS_AUTOPLAY_EVENT = DEFINE_PROPERTYKEY(
        0xB3D8DAD7,
        0xA361,
        0x4B83,
        0x8A,
        0x48,
        0x5B,
        0x02,
        0xCE,
        0x10,
        0x71,
        0x3B,
        0x3
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_EVENT_ATTRIBUTES_V1 The properties in this category describe event attributes. *************************************************************************
    #
    WPD_EVENT_ATTRIBUTES_V1 = DEFINE_GUID(
        0x10C96578,
        0x2E81,
        0x4111,
        0xAD,
        0xDE,
        0xE0,
        0x8C,
        0xA6,
        0x13,
        0x8F,
        0x6D
    )


    # WPD_EVENT_ATTRIBUTE_NAME
    # [ VT_LPWSTR ] Contains the name of the event.
    WPD_EVENT_ATTRIBUTE_NAME = DEFINE_PROPERTYKEY(
        0x10C96578,
        0x2E81,
        0x4111,
        0xAD,
        0xDE,
        0xE0,
        0x8C,
        0xA6,
        0x13,
        0x8F,
        0x6D,
        0x2
    )

    # WPD_EVENT_ATTRIBUTE_PARAMETERS
    # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing the event
    # parameters.
    WPD_EVENT_ATTRIBUTE_PARAMETERS = DEFINE_PROPERTYKEY(
        0x10C96578,
        0x2E81,
        0x4111,
        0xAD,
        0xDE,
        0xE0,
        0x8C,
        0xA6,
        0x13,
        0x8F,
        0x6D,
        0x3
    )


    # WPD_EVENT_ATTRIBUTE_OPTIONS
    # [ VT_UNKNOWN ] IPortableDeviceValues containing the event options.
    WPD_EVENT_ATTRIBUTE_OPTIONS = DEFINE_PROPERTYKEY(
        0x10C96578,
        0x2E81,
        0x4111,
        0xAD,
        0xDE,
        0xE0,
        0x8C,
        0xA6,
        0x13,
        0x8F,
        0x6D,
        0x4
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_API_OPTIONS_V1 The properties in this category describe API options. *************************************************************************
    #
    WPD_API_OPTIONS_V1 = DEFINE_GUID(
        0x10E54A3E,
        0x052D,
        0x4777,
        0xA1,
        0x3C,
        0xDE,
        0x76,
        0x14,
        0xBE,
        0x2B,
        0xC4
    )

    # WPD_API_OPTION_USE_CLEAR_DATA_STREAM
    # [ VT_BOOL ] Indicates that the data stream created for data transfer
    # will be clear only (i.e. No DRM will be involved).
    WPD_API_OPTION_USE_CLEAR_DATA_STREAM = DEFINE_PROPERTYKEY(
        0x10E54A3E,
        0x052D,
        0x4777,
        0xA1,
        0x3C,
        0xDE,
        0x76,
        0x14,
        0xBE,
        0x2B,
        0xC4,
        0x2
    )


    # WPD_API_OPTION_IOCTL_ACCESS
    # [ VT_UI4 ] An optional property that clients can add to the IN parameter
    # set of IPortableDevice::SendCommand to specify the access required for
    # the command. The Portable Device API uses this to identify whether the
    # IOCTL sent to the driver is sent with FILE_READ_ACCESS or
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS) access flags.
    WPD_API_OPTION_IOCTL_ACCESS = DEFINE_PROPERTYKEY(
        0x10E54A3E,
        0x052D,
        0x4777,
        0xA1,
        0x3C,
        0xDE,
        0x76,
        0x14,
        0xBE,
        0x2B,
        0xC4,
        0x3
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_FORMAT_ATTRIBUTES_V1 The properties in this category describe format attributes. *************************************************************************
    #
    WPD_FORMAT_ATTRIBUTES_V1 = DEFINE_GUID(
        0xA0A02000,
        0xBCAF,
        0x4BE8,
        0xB3,
        0xF5,
        0x23,
        0x3F,
        0x23,
        0x1C,
        0xF5,
        0x8F
    )

    # WPD_FORMAT_ATTRIBUTE_NAME
    # [ VT_LPWSTR ] Contains the name of the format.
    WPD_FORMAT_ATTRIBUTE_NAME = DEFINE_PROPERTYKEY(
        0xA0A02000,
        0xBCAF,
        0x4BE8,
        0xB3,
        0xF5,
        0x23,
        0x3F,
        0x23,
        0x1C,
        0xF5,
        0x8F,
        0x2
    )


    # WPD_FORMAT_ATTRIBUTE_MIMETYPE
    # [ VT_LPWSTR ] Contains the MIME type of the format.
    WPD_FORMAT_ATTRIBUTE_MIMETYPE = DEFINE_PROPERTYKEY(
        0xA0A02000,
        0xBCAF,
        0x4BE8,
        0xB3,
        0xF5,
        0x23,
        0x3F,
        0x23,
        0x1C,
        0xF5,
        0x8F,
        0x3
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_METHOD_ATTRIBUTES_V1 The properties in this category describe method attributes. *************************************************************************
    #
    WPD_METHOD_ATTRIBUTES_V1 = DEFINE_GUID(
        0xF17A5071,
        0xF039,
        0x44AF,
        0x8E,
        0xFE,
        0x43,
        0x2C,
        0xF3,
        0x2E,
        0x43,
        0x2A
    )

    # WPD_METHOD_ATTRIBUTE_NAME
    # [ VT_LPWSTR ] Contains the name of the method.
    WPD_METHOD_ATTRIBUTE_NAME = DEFINE_PROPERTYKEY(
        0xF17A5071,
        0xF039,
        0x44AF,
        0x8E,
        0xFE,
        0x43,
        0x2C,
        0xF3,
        0x2E,
        0x43,
        0x2A,
        0x2
    )


    # WPD_METHOD_ATTRIBUTE_ASSOCIATED_FORMAT
    # [ VT_CLSID ] Contains the format this method applies to. This is
    # GUID_NULL if the method does not apply to a format.
    WPD_METHOD_ATTRIBUTE_ASSOCIATED_FORMAT = DEFINE_PROPERTYKEY(
        0xF17A5071,
        0xF039,
        0x44AF,
        0x8E,
        0xFE,
        0x43,
        0x2C,
        0xF3,
        0x2E,
        0x43,
        0x2A,
        0x3
    )

    # WPD_METHOD_ATTRIBUTE_ACCESS
    # [ VT_UI4 ] Indicates the required access for a method.
    WPD_METHOD_ATTRIBUTE_ACCESS = DEFINE_PROPERTYKEY(
        0xF17A5071,
        0xF039,
        0x44AF,
        0x8E,
        0xFE,
        0x43,
        0x2C,
        0xF3,
        0x2E,
        0x43,
        0x2A,
        0x4
    )


    # WPD_METHOD_ATTRIBUTE_PARAMETERS
    # [ VT_UNKNOWN ] This is an IPortableDeviceKeyCollection containing the
    # method parameters.
    WPD_METHOD_ATTRIBUTE_PARAMETERS = DEFINE_PROPERTYKEY(
        0xF17A5071,
        0xF039,
        0x44AF,
        0x8E,
        0xFE,
        0x43,
        0x2C,
        0xF3,
        0x2E,
        0x43,
        0x2A,
        0x5
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_PARAMETER_ATTRIBUTES_V1 The properties in this category describe parameter attributes. *************************************************************************
    #
    WPD_PARAMETER_ATTRIBUTES_V1 = DEFINE_GUID(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58
    )

    # WPD_PARAMETER_ATTRIBUTE_ORDER
    # [ VT_UI4 ] The order (starting from 0) of a method parameter.
    WPD_PARAMETER_ATTRIBUTE_ORDER = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0x2
    )


    # WPD_PARAMETER_ATTRIBUTE_USAGE
    # [ VT_UI4 ] The usage of the method parameter.
    WPD_PARAMETER_ATTRIBUTE_USAGE = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0x3
    )

    # WPD_PARAMETER_ATTRIBUTE_FORM
    # [ VT_UI4 ] Specifies the form of the valid values allowed for this
    # parameter.
    WPD_PARAMETER_ATTRIBUTE_FORM = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0x4
    )


    # WPD_PARAMETER_ATTRIBUTE_DEFAULT_VALUE
    # [ VT_XXXX ] Specifies the default value for this parameter.
    WPD_PARAMETER_ATTRIBUTE_DEFAULT_VALUE = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0x5
    )

    # WPD_PARAMETER_ATTRIBUTE_RANGE_MIN
    # [ VT_XXXX ] The minimum value for a parameter whose form is of
    # WPD_PARAMETER_ATTRIBUTE_FORM_RANGE.
    WPD_PARAMETER_ATTRIBUTE_RANGE_MIN = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0x6
    )


    # WPD_PARAMETER_ATTRIBUTE_RANGE_MAX
    # [ VT_XXXX ] The maximum value for a parameter whose form is of
    # WPD_PARAMETER_ATTRIBUTE_FORM_RANGE.
    WPD_PARAMETER_ATTRIBUTE_RANGE_MAX = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0x7
    )

    # WPD_PARAMETER_ATTRIBUTE_RANGE_STEP
    # [ VT_XXXX ] The step value for a parameter whose form is of
    # WPD_PARAMETER_ATTRIBUTE_FORM_RANGE.
    WPD_PARAMETER_ATTRIBUTE_RANGE_STEP = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0x8
    )


    # WPD_PARAMETER_ATTRIBUTE_ENUMERATION_ELEMENTS
    # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection containing the
    # enumeration values.
    WPD_PARAMETER_ATTRIBUTE_ENUMERATION_ELEMENTS = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0x9
    )

    # WPD_PARAMETER_ATTRIBUTE_REGULAR_EXPRESSION
    # [ VT_LPWSTR ] A regular expression string indicating acceptable values
    # for parameters whose form is
    # WPD_PARAMETER_ATTRIBUTE_FORM_REGULAR_EXPRESSION.
    WPD_PARAMETER_ATTRIBUTE_REGULAR_EXPRESSION = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0xA
    )


    # WPD_PARAMETER_ATTRIBUTE_MAX_SIZE
    # [ VT_UI8 ] This indicates the maximum size (in bytes) for the value of
    # this parameter.
    WPD_PARAMETER_ATTRIBUTE_MAX_SIZE = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0xB
    )

    # WPD_PARAMETER_ATTRIBUTE_VARTYPE
    # [ VT_UI4 ] Contains the VARTYPE of the parameter.
    WPD_PARAMETER_ATTRIBUTE_VARTYPE = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0xC
    )


    # WPD_PARAMETER_ATTRIBUTE_NAME
    # [ VT_LPWSTR ] Contains the parameter name.
    WPD_PARAMETER_ATTRIBUTE_NAME = DEFINE_PROPERTYKEY(
        0xE6864DD7,
        0xF325,
        0x45EA,
        0xA1,
        0xD5,
        0x97,
        0xCF,
        0x73,
        0xB6,
        0xCA,
        0x58,
        0xD
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_COMMON *************************************************************************
    #
    WPD_CATEGORY_COMMON = DEFINE_GUID(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_COMMON_RESET_DEVICE
    # This command is sent by clients to reset the device.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # None
    # Results:
    # None
    WPD_COMMAND_COMMON_RESET_DEVICE = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x2
    )


    # WPD_COMMAND_COMMON_GET_OBJECT_IDS_FROM_PERSISTENT_UNIQUE_IDS
    # This command is sent when a client wants to get current ObjectIDs
    # representing objects specified by previously acquired Persistent Unique
    # IDs.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_COMMON_PERSISTENT_UNIQUE_IDS
    # Results:
    # [ Required ] WPD_PROPERTY_COMMON_OBJECT_IDS
    WPD_COMMAND_COMMON_GET_OBJECT_IDS_FROM_PERSISTENT_UNIQUE_IDS = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x3
    )

    # WPD_COMMAND_COMMON_SAVE_CLIENT_INFORMATION
    # This command is sent when a client first connects to a device.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_COMMON_CLIENT_INFORMATION
    # Results:
    # [ Optional ] WPD_PROPERTY_COMMON_CLIENT_INFORMATION_CONTEXT
    WPD_COMMAND_COMMON_SAVE_CLIENT_INFORMATION = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x4
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_COMMON_COMMAND_CATEGORY
    # [ VT_CLSID ] Specifies the command Category
    # (i.e. the GUID portion of the PROPERTYKEY indicating the command).
    WPD_PROPERTY_COMMON_COMMAND_CATEGORY = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x3E9
    )

    # WPD_PROPERTY_COMMON_COMMAND_ID
    # [ VT_UI4 ] Specifies the command ID, which is the PID portion of the
    # PROPERTYKEY indicating the command.
    WPD_PROPERTY_COMMON_COMMAND_ID = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x3EA
    )


    # WPD_PROPERTY_COMMON_HRESULT
    # [ VT_ERROR ] The driver sets this to be the HRESULT of the requested
    # operation.
    WPD_PROPERTY_COMMON_HRESULT = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x3EB
    )

    # WPD_PROPERTY_COMMON_DRIVER_ERROR_CODE
    # [ VT_UI4 ] Special driver specific code which driver may return on
    # error. Typically only for use with diagnostic tools or vertical
    # solutions.
    WPD_PROPERTY_COMMON_DRIVER_ERROR_CODE = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x3EC
    )


    # WPD_PROPERTY_COMMON_COMMAND_TARGET
    # [ VT_LPWSTR ] Identifies the object which the command is intended for.
    WPD_PROPERTY_COMMON_COMMAND_TARGET = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x3EE
    )

    # WPD_PROPERTY_COMMON_PERSISTENT_UNIQUE_IDS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR
    # specifying list of Persistent Unique IDs.
    WPD_PROPERTY_COMMON_PERSISTENT_UNIQUE_IDS = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x3EF
    )


    # WPD_PROPERTY_COMMON_OBJECT_IDS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR
    # specifying list of Objects IDs.
    WPD_PROPERTY_COMMON_OBJECT_IDS = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x3F0
    )

    # WPD_PROPERTY_COMMON_CLIENT_INFORMATION
    # [ VT_UNKNOWN ] IPortableDeviceValues used to identify itself to the
    # driver.
    WPD_PROPERTY_COMMON_CLIENT_INFORMATION = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x3F1
    )


    # WPD_PROPERTY_COMMON_CLIENT_INFORMATION_CONTEXT
    # [ VT_LPWSTR ] Driver specified context which will be sent for the
    # particular client on all subsequent operations.
    WPD_PROPERTY_COMMON_CLIENT_INFORMATION_CONTEXT = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x3F2
    )

    # WPD_PROPERTY_COMMON_ACTIVITY_ID
    # [ VT_CLSID ] An optional ActivityID set either by a client or by WPD
    # API, when ETW tracing is enabled.
    WPD_PROPERTY_COMMON_ACTIVITY_ID = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x3F3
    )

    # == == == == Command Options == == == ==
    # WPD_OPTION_VALID_OBJECT_IDS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR
    # specifying list of Objects IDs of the objects that support the command.
    WPD_OPTION_VALID_OBJECT_IDS = DEFINE_PROPERTYKEY(
        0xF0422A9C,
        0x5DC8,
        0x4440,
        0xB5,
        0xBD,
        0x5D,
        0xF2,
        0x88,
        0x35,
        0x65,
        0x8A,
        0x1389
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_OBJECT_ENUMERATION The commands in this category are used for basic object enumeration. *************************************************************************
    #
    WPD_CATEGORY_OBJECT_ENUMERATION = DEFINE_GUID(
        0xB7474E91,
        0xE7F8,
        0x4AD9,
        0xB4,
        0x00,
        0xAD,
        0x1A,
        0x4B,
        0x58,
        0xEE,
        0xEC
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_OBJECT_ENUMERATION_START_FIND
    # The driver receives this command when a client wishes to start
    # enumeration.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_ENUMERATION_PARENT_ID
    # [ Optional ] WPD_PROPERTY_OBJECT_ENUMERATION_FILTER
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_ENUMERATION_CONTEXT
    WPD_COMMAND_OBJECT_ENUMERATION_START_FIND = DEFINE_PROPERTYKEY(
        0xB7474E91,
        0xE7F8,
        0x4AD9,
        0xB4,
        0x00,
        0xAD,
        0x1A,
        0x4B,
        0x58,
        0xEE,
        0xEC,
        0x2
    )


    # WPD_COMMAND_OBJECT_ENUMERATION_FIND_NEXT
    # This command is used when the client requests the next batch of
    # ObjectIDs during enumeration. Only objects that match the constraints
    # set up in WPD_COMMAND_OBJECT_ENUMERATION_START_FIND should be returned.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_ENUMERATION_CONTEXT
    # [ Required ] WPD_PROPERTY_OBJECT_ENUMERATION_NUM_OBJECTS_REQUESTED
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_ENUMERATION_OBJECT_IDS
    WPD_COMMAND_OBJECT_ENUMERATION_FIND_NEXT = DEFINE_PROPERTYKEY(
        0xB7474E91,
        0xE7F8,
        0x4AD9,
        0xB4,
        0x00,
        0xAD,
        0x1A,
        0x4B,
        0x58,
        0xEE,
        0xEC,
        0x3
    )

    # WPD_COMMAND_OBJECT_ENUMERATION_END_FIND
    # The driver should destroy any resources associated with this enumeration
    # context.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_ENUMERATION_CONTEXT
    # Results:
    # None
    WPD_COMMAND_OBJECT_ENUMERATION_END_FIND = DEFINE_PROPERTYKEY(
        0xB7474E91,
        0xE7F8,
        0x4AD9,
        0xB4,
        0x00,
        0xAD,
        0x1A,
        0x4B,
        0x58,
        0xEE,
        0xEC,
        0x4
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_OBJECT_ENUMERATION_PARENT_ID
    # [ VT_LPWSTR ] The ObjectID specifying the parent object where
    # enumeration should start.
    WPD_PROPERTY_OBJECT_ENUMERATION_PARENT_ID = DEFINE_PROPERTYKEY(
        0xB7474E91,
        0xE7F8,
        0x4AD9,
        0xB4,
        0x00,
        0xAD,
        0x1A,
        0x4B,
        0x58,
        0xEE,
        0xEC,
        0x3E9
    )

    # WPD_PROPERTY_OBJECT_ENUMERATION_FILTER
    # [ VT_UNKNOWN ] This is an IPortableDeviceValues which specifies the
    # properties used to filter on. If the caller does not want filtering,
    # then this value will not be set.
    WPD_PROPERTY_OBJECT_ENUMERATION_FILTER = DEFINE_PROPERTYKEY(
        0xB7474E91,
        0xE7F8,
        0x4AD9,
        0xB4,
        0x00,
        0xAD,
        0x1A,
        0x4B,
        0x58,
        0xEE,
        0xEC,
        0x3EA
    )


    # WPD_PROPERTY_OBJECT_ENUMERATION_OBJECT_IDS
    # [ VT_UNKNOWN ] This is an IPortableDevicePropVariantCollection of
    # ObjectIDs (of type VT_LPWSTR). If 0 objects are returned, this should be
    # an empty collection, not NULL.
    WPD_PROPERTY_OBJECT_ENUMERATION_OBJECT_IDS = DEFINE_PROPERTYKEY(
        0xB7474E91,
        0xE7F8,
        0x4AD9,
        0xB4,
        0x00,
        0xAD,
        0x1A,
        0x4B,
        0x58,
        0xEE,
        0xEC,
        0x3EB
    )

    # WPD_PROPERTY_OBJECT_ENUMERATION_CONTEXT
    # [ VT_LPWSTR ] This is a driver-specified identifier for the context
    # associated with this enumeration.
    WPD_PROPERTY_OBJECT_ENUMERATION_CONTEXT = DEFINE_PROPERTYKEY(
        0xB7474E91,
        0xE7F8,
        0x4AD9,
        0xB4,
        0x00,
        0xAD,
        0x1A,
        0x4B,
        0x58,
        0xEE,
        0xEC,
        0x3EC
    )


    # WPD_PROPERTY_OBJECT_ENUMERATION_NUM_OBJECTS_REQUESTED
    # [ VT_UI4 ] The maximum number of ObjectIDs to return back to the client.
    WPD_PROPERTY_OBJECT_ENUMERATION_NUM_OBJECTS_REQUESTED = DEFINE_PROPERTYKEY(
        0xB7474E91,
        0xE7F8,
        0x4AD9,
        0xB4,
        0x00,
        0xAD,
        0x1A,
        0x4B,
        0x58,
        0xEE,
        0xEC,
        0x3ED
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_OBJECT_PROPERTIES This category of commands is used to perform basic property operations such as Reading/Writing values, listing supported values and so on. *************************************************************************
    #
    WPD_CATEGORY_OBJECT_PROPERTIES = DEFINE_GUID(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED
    # This command is used when the client requests the list of properties
    # supported by the specified object.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS
    WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x2
    )


    # WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES
    # This command is used when the client requests the property attributes
    # for the specified object properties.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES
    WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x3
    )

    # WPD_COMMAND_OBJECT_PROPERTIES_GET
    # This command is used when the client requests a set of property values
    # for the specified object.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES
    WPD_COMMAND_OBJECT_PROPERTIES_GET = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x4
    )


    # WPD_COMMAND_OBJECT_PROPERTIES_SET
    # This command is used when the client requests to write a set of property
    # values on the specified object.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS
    WPD_COMMAND_OBJECT_PROPERTIES_SET = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x5
    )

    # WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL
    # This command is used when the client requests all property values for
    # the specified object.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES
    WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x6
    )


    # WPD_COMMAND_OBJECT_PROPERTIES_DELETE
    # This command is sent when the caller wants to delete properties from the
    # specified object.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS
    # Results:
    # [ Optional ] WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_DELETE_RESULTS
    WPD_COMMAND_OBJECT_PROPERTIES_DELETE = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x7
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID
    # [ VT_LPWSTR ] The ObjectID specifying the object whose properties are
    # being queried/manipulated.
    WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x3E9
    )


    # WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS
    # [ VT_UNKNOWN ] An IPortableDeviceKeyCollection identifying which
    # specific property values we are querying/manipulating.
    WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x3EA
    )

    # WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES
    # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the
    # attributes for each property requested.
    WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x3EB
    )


    # WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES
    # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the
    # values read. For any property whose value could not be read, the type
    # must be set to VT_ERROR, and the 'scode' field must contain the failure
    # HRESULT.
    WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x3EC
    )

    # WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS
    # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the
    # result of each property write operation.
    WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x3ED
    )


    # WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_DELETE_RESULTS
    # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the
    # result of each property delete operation.
    WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_DELETE_RESULTS = DEFINE_PROPERTYKEY(
        0x9E5582E4,
        0x0814,
        0x44E6,
        0x98,
        0x1A,
        0xB2,
        0x99,
        0x8D,
        0x58,
        0x38,
        0x04,
        0x3EE
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_OBJECT_PROPERTIES_BULK This category contains commands and properties for property operations across multiple objects. *************************************************************************
    #
    WPD_CATEGORY_OBJECT_PROPERTIES_BULK = DEFINE_GUID(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_START
    # Initializes the operation to get the property values for all
    # caller-specified objects.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_IDS
    # [ Optional ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PROPERTY_KEYS
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT
    WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_START = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x2
    )


    # WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_NEXT
    # Get the next set of property values.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_VALUES
    WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_NEXT = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x3
    )

    # WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_END
    # Ends the bulk property operation for getting property values by object
    # list.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT
    # Results:
    # None
    WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_END = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x4
    )


    # WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_START
    # Initializes the operation to get the property values for objects of the
    # specified format
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_FORMAT
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PARENT_OBJECT_ID
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_DEPTH
    # [ Optional ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PROPERTY_KEYS
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT
    WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_START = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x5
    )

    # WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_NEXT
    # Get the next set of property values.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_VALUES
    WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_NEXT = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x6
    )


    # WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_END
    # Ends the bulk property operation for getting property values by object
    # format.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT
    # Results:
    # None
    WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_END = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x7
    )

    # WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_START
    # Initializes the operation to set the property values for specified
    # objects.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_VALUES
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT
    WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_START = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x8
    )


    # WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_NEXT
    # Set the next set of property values.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_WRITE_RESULTS
    WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_NEXT = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x9
    )

    # WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_END
    # Ends the bulk property operation for setting property values by object
    # list.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT
    # Results:
    # None
    WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_END = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0xA
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_IDS
    # [ VT_UNKNOWN ] A collection of ObjectIDs for which supported property
    # list must be returned.
    WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_IDS = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x3E9
    )

    # WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT
    # [ VT_LPWSTR ] The driver-specified context identifying this particular
    # bulk operation.
    WPD_PROPERTY_OBJECT_PROPERTIES_BULK_CONTEXT = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x3EA
    )


    # WPD_PROPERTY_OBJECT_PROPERTIES_BULK_VALUES
    # [ VT_UNKNOWN ] Contains an IPortableDeviceValuesCollection specifying
    # the next set of IPortableDeviceValues elements.
    WPD_PROPERTY_OBJECT_PROPERTIES_BULK_VALUES = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x3EB
    )

    # WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PROPERTY_KEYS
    # [ VT_UNKNOWN ] Contains an IPortableDeviceKeyCollection specifying which
    # properties the caller wants to return. May not exist, which indicates
    # caller wants ALL properties.
    WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PROPERTY_KEYS = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x3EC
    )


    # WPD_PROPERTY_OBJECT_PROPERTIES_BULK_DEPTH
    # [ VT_UI4 ] Contains a value specifying the hierarchical depth from the
    # parent to include in this operation.
    WPD_PROPERTY_OBJECT_PROPERTIES_BULK_DEPTH = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x3ED
    )

    # WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PARENT_OBJECT_ID
    # [ VT_LPWSTR ] Contains the ObjectID of the object to start the operation
    # from.
    WPD_PROPERTY_OBJECT_PROPERTIES_BULK_PARENT_OBJECT_ID = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x3EE
    )


    # WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_FORMAT
    # [ VT_CLSID ] Specifies the object format the client is interested in.
    WPD_PROPERTY_OBJECT_PROPERTIES_BULK_OBJECT_FORMAT = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x3EF
    )

    # WPD_PROPERTY_OBJECT_PROPERTIES_BULK_WRITE_RESULTS
    # [ VT_UNKNOWN ] Contains an IPortableDeviceValuesCollection specifying
    # the set of IPortableDeviceValues elements indicating the write results
    # for each property set.
    WPD_PROPERTY_OBJECT_PROPERTIES_BULK_WRITE_RESULTS = DEFINE_PROPERTYKEY(
        0x11C824DD,
        0x04CD,
        0x4E4E,
        0x8C,
        0x7B,
        0xF6,
        0xEF,
        0xB7,
        0x94,
        0xD8,
        0x4E,
        0x3F0
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_OBJECT_RESOURCES The commands in this category are used for basic object resource enumeration and transfer. *************************************************************************
    #
    WPD_CATEGORY_OBJECT_RESOURCES = DEFINE_GUID(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_OBJECT_RESOURCES_GET_SUPPORTED
    # This command is sent when a client wants to get the list of resources
    # supported on a particular object.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS
    WPD_COMMAND_OBJECT_RESOURCES_GET_SUPPORTED = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x2
    )

    # WPD_COMMAND_OBJECT_RESOURCES_GET_ATTRIBUTES
    # This command is used when the client requests the attributes for the
    # specified object resource.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_ATTRIBUTES
    WPD_COMMAND_OBJECT_RESOURCES_GET_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3
    )


    # WPD_COMMAND_OBJECT_RESOURCES_OPEN
    # This command is sent when a client wants to use a particular resource on
    # an object.
    # Access:
    # Dependent on the value of WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE.
    # STGM_READ will indicate FILE_READ_ACCESS for the command, anything else
    # will indicate (FILE_READ_ACCESS | FILE_WRITE_ACCESS).
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE
    # [ Optional ] WPD_PROPERTY_OBJECT_RESOURCES_SUPPORTS_UNITS
    WPD_COMMAND_OBJECT_RESOURCES_OPEN = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x4
    )

    # WPD_COMMAND_OBJECT_RESOURCES_READ
    # This command is sent when a client wants to read the next band of data
    # from a previously opened object resource.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_READ
    # [ Required except when the driver returns TRUE for the
    # WPD_OPTION_OBJECT_RESOURCES_NO_INPUT_BUFFER_ON_READ option. ]
    # WPD_PROPERTY_OBJECT_RESOURCES_DATA
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_READ
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_DATA
    WPD_COMMAND_OBJECT_RESOURCES_READ = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x5
    )


    # WPD_COMMAND_OBJECT_RESOURCES_WRITE
    # This command is sent when a client wants to write the next band of data
    # to a previously opened object resource.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_WRITE
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_DATA
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_WRITTEN
    WPD_COMMAND_OBJECT_RESOURCES_WRITE = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x6
    )

    # WPD_COMMAND_OBJECT_RESOURCES_CLOSE
    # This command is sent when a client is finished transferring data to a
    # previously opened object resource.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT
    # Results:
    # None
    WPD_COMMAND_OBJECT_RESOURCES_CLOSE = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x7
    )


    # WPD_COMMAND_OBJECT_RESOURCES_DELETE
    # This command is sent when the client wants to delete the data associated
    # with the specified resources from the specified object.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS
    # Results:
    # None
    WPD_COMMAND_OBJECT_RESOURCES_DELETE = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x8
    )

    # WPD_COMMAND_OBJECT_RESOURCES_CREATE_RESOURCE
    # This command is sent when a client wants to create a new object resource
    # on the device.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_ATTRIBUTES
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE
    WPD_COMMAND_OBJECT_RESOURCES_CREATE_RESOURCE = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x9
    )


    # WPD_COMMAND_OBJECT_RESOURCES_REVERT
    # This command is sent when a client wants to cancel the resource creation
    # request that is currently still in progress.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT
    # Results:
    # None
    WPD_COMMAND_OBJECT_RESOURCES_REVERT = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0xA
    )

    # WPD_COMMAND_OBJECT_RESOURCES_SEEK
    # This command is sent when a client wants to seek to a specific offset in
    # the data stream.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_SEEK_OFFSET
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START
    WPD_COMMAND_OBJECT_RESOURCES_SEEK = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0xB
    )


    # WPD_COMMAND_OBJECT_RESOURCES_COMMIT
    # This command is sent when a client wants to commit changes to a data
    # stream.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT
    # Results:
    # None
    WPD_COMMAND_OBJECT_RESOURCES_COMMIT = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0xC
    )

    # WPD_COMMAND_OBJECT_RESOURCES_SEEK_IN_UNITS
    # This command is sent when a client wants to seek to a specific offset in
    # the data stream using alternate units.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_SEEK_OFFSET
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_STREAM_UNITS
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START
    WPD_COMMAND_OBJECT_RESOURCES_SEEK_IN_UNITS = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0xD
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID
    # [ VT_LPWSTR ]
    WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3E9
    )

    # WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE
    # [ VT_UI4 ] Specifies the type of access the client is requesting for the
    # resource.
    WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3EA
    )


    # WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS
    # [ VT_UNKNOWN ]
    WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3EB
    )

    # WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_ATTRIBUTES
    # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the
    # attributes for the resource requested.
    WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3EC
    )


    # WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT
    # [ VT_LPWSTR ] This is a driver-specified identifier for the context
    # associated with the resource operation.
    WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3ED
    )

    # WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_READ
    # [ VT_UI4 ] Specifies the number of bytes the client is requesting to
    # read.
    WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_READ = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3EE
    )


    # WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_READ
    # [ VT_UI4 ] Specifies the number of bytes actually read from the resource.
    WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_READ = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3EF
    )

    # WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_WRITE
    # [ VT_UI4 ] Specifies the number of bytes the client is requesting to
    # write.
    WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_WRITE = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3F0
    )


    # WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_WRITTEN
    # [ VT_UI4 ] Driver sets this to let caller know how many bytes were
    # actually written.
    WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_WRITTEN = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3F1
    )

    # WPD_PROPERTY_OBJECT_RESOURCES_DATA
    # [ VT_VECTOR | VT_UI1 ]
    WPD_PROPERTY_OBJECT_RESOURCES_DATA = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3F2
    )


    # WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE
    # [ VT_UI4 ] Indicates the optimal transfer buffer size (in bytes) that
    # clients should use when reading/writing this resource.
    WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3F3
    )

    # WPD_PROPERTY_OBJECT_RESOURCES_SEEK_OFFSET
    # [ VT_I8 ] Displacement to be added to the location indicated by the
    # WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG parameter.
    WPD_PROPERTY_OBJECT_RESOURCES_SEEK_OFFSET = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3F4
    )


    # WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG
    # [ VT_UI4 ] Specifies the origin of the displacement for the seek
    # operation.
    WPD_PROPERTY_OBJECT_RESOURCES_SEEK_ORIGIN_FLAG = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3F5
    )

    # WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START
    # [ VT_UI8 ] Value of the new seek pointer from the beginning of the data
    # stream.
    WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3F6
    )


    # WPD_PROPERTY_OBJECT_RESOURCES_SUPPORTS_UNITS
    # [ VT_BOOL ] A Boolean value that specifies whether this resource
    # supports operations (such as seek) using alternate units. This occurs if
    # the driver can understand WPD_COMMAND_OBJECT_RESOURCES_SEEK_IN_UNITS.
    WPD_PROPERTY_OBJECT_RESOURCES_SUPPORTS_UNITS = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3F7
    )

    # WPD_PROPERTY_OBJECT_RESOURCES_STREAM_UNITS
    # [ VT_UI4 ] The units for the WPD_PROPERTY_OBJECT_SEEK_OFFSET parameter
    # and the WPD_PROPERTY_OBJECT_RESOURCES_POSITION_FROM_START result.
    WPD_PROPERTY_OBJECT_RESOURCES_STREAM_UNITS = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x3F8
    )

    # == == == == Command Options == == == ==
    # WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_READ_SUPPORTED
    # [ VT_BOOL ] Indicates whether the driver can Seek on a resource opened
    # for Read access.
    WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_READ_SUPPORTED = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x1389
    )

    # WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_WRITE_SUPPORTED
    # [ VT_BOOL ] Indicates whether the driver can Seek on a resource opened
    # for Write access.
    WPD_OPTION_OBJECT_RESOURCES_SEEK_ON_WRITE_SUPPORTED = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x138A
    )


    # WPD_OPTION_OBJECT_RESOURCES_NO_INPUT_BUFFER_ON_READ
    # [ VT_BOOL ] Indicates whether the driver requires an input buffer for
    # WPD_COMMAND_OBJECT_RESOURCES_READ. If not set, defaults to False.
    WPD_OPTION_OBJECT_RESOURCES_NO_INPUT_BUFFER_ON_READ = DEFINE_PROPERTYKEY(
        0xB3A2B22D,
        0xA595,
        0x4108,
        0xBE,
        0x0A,
        0xFC,
        0x3C,
        0x96,
        0x5F,
        0x3D,
        0x4A,
        0x138B
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_OBJECT_MANAGEMENT The commands specified in this category are used to Create/Delete objects on the device. *************************************************************************
    #
    WPD_CATEGORY_OBJECT_MANAGEMENT = DEFINE_GUID(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_ONLY
    # This command is sent when a client wants to create a new object on the
    # device, specified only by properties.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_CREATION_PROPERTIES
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_ID
    WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_ONLY = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x2
    )


    # WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_AND_DATA
    # This command is sent when a client wants to create a new object on the
    # device, specified by properties and data.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_CREATION_PROPERTIES
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT
    WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_AND_DATA = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3
    )

    # WPD_COMMAND_OBJECT_MANAGEMENT_WRITE_OBJECT_DATA
    # This command is sent when a client wants to write the next band of data
    # to a newly created object or an object being updated.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_TO_WRITE
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_DATA
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_WRITTEN
    WPD_COMMAND_OBJECT_MANAGEMENT_WRITE_OBJECT_DATA = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x4
    )


    # WPD_COMMAND_OBJECT_MANAGEMENT_COMMIT_OBJECT
    # This command is sent when a client has finished sending all the data
    # associated with an object creation or update request, and wishes to
    # ensure that the object is saved to the device.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_ID
    WPD_COMMAND_OBJECT_MANAGEMENT_COMMIT_OBJECT = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x5
    )

    # WPD_COMMAND_OBJECT_MANAGEMENT_REVERT_OBJECT
    # This command is sent when a client wants to cancel the object creation
    # or update request that is currently still in progress.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT
    # Results:
    # None
    WPD_COMMAND_OBJECT_MANAGEMENT_REVERT_OBJECT = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x6
    )


    # WPD_COMMAND_OBJECT_MANAGEMENT_DELETE_OBJECTS
    # This command is sent when the client wishes to remove a set of objects
    # from the device.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_OPTIONS
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_IDS
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_RESULTS
    WPD_COMMAND_OBJECT_MANAGEMENT_DELETE_OBJECTS = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x7
    )

    # WPD_COMMAND_OBJECT_MANAGEMENT_MOVE_OBJECTS
    # This command will move the specified objects to the destination folder.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_IDS
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_DESTINATION_FOLDER_OBJECT_ID
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_MOVE_RESULTS
    WPD_COMMAND_OBJECT_MANAGEMENT_MOVE_OBJECTS = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x8
    )


    # WPD_COMMAND_OBJECT_MANAGEMENT_COPY_OBJECTS
    # This command will copy the specified objects to the destination folder.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_IDS
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_DESTINATION_FOLDER_OBJECT_ID
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_COPY_RESULTS
    WPD_COMMAND_OBJECT_MANAGEMENT_COPY_OBJECTS = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x9
    )

    # WPD_COMMAND_OBJECT_MANAGEMENT_UPDATE_OBJECT_WITH_PROPERTIES_AND_DATA
    # This command is sent when a client wants to update the object's data and
    # dependent properties simultaneously.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_ID
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_UPDATE_PROPERTIES
    # Results:
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT
    # [ Required ] WPD_PROPERTY_OBJECT_MANAGEMENT_OPTIMAL_TRANSFER_BUFFER_SIZE
    WPD_COMMAND_OBJECT_MANAGEMENT_UPDATE_OBJECT_WITH_PROPERTIES_AND_DATA = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0xA
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_OBJECT_MANAGEMENT_CREATION_PROPERTIES
    # [ VT_UNKNOWN ] This is an IPortableDeviceValues which specifies the
    # properties used to create the new object.
    WPD_PROPERTY_OBJECT_MANAGEMENT_CREATION_PROPERTIES = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3E9
    )

    # WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT
    # [ VT_LPWSTR ] This is a driver-specified identifier for the context
    # associated with this 'create object' operation.
    WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3EA
    )


    # WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_TO_WRITE
    # [ VT_UI4 ] Specifies the number of bytes the client is requesting to
    # write.
    WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_TO_WRITE = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3EB
    )

    # WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_WRITTEN
    # [ VT_UI4 ] Indicates the number of bytes written for the object.
    WPD_PROPERTY_OBJECT_MANAGEMENT_NUM_BYTES_WRITTEN = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3EC
    )


    # WPD_PROPERTY_OBJECT_MANAGEMENT_DATA
    # [ VT_VECTOR | VT_UI1 ] Indicates binary data of the object being created
    # on the device.
    WPD_PROPERTY_OBJECT_MANAGEMENT_DATA = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3ED
    )

    # WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_ID
    # [ VT_LPWSTR ] Identifies a newly created object on the device.
    WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_ID = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3EE
    )


    # WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_OPTIONS
    # [ VT_UI4 ] Indicates if the delete operation should be recursive or not.
    WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_OPTIONS = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3EF
    )

    # WPD_PROPERTY_OBJECT_MANAGEMENT_OPTIMAL_TRANSFER_BUFFER_SIZE
    # [ VT_UI4 ] Indicates the optimal transfer buffer size (in bytes) that
    # clients should use when writing this object's data.
    WPD_PROPERTY_OBJECT_MANAGEMENT_OPTIMAL_TRANSFER_BUFFER_SIZE = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3F0
    )


    # WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_IDS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR,
    # containing the ObjectIDs to delete.
    WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_IDS = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3F1
    )

    # WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_RESULTS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_ERROR,
    # where each element is the HRESULT indicating the success or failure of
    # the operation.
    WPD_PROPERTY_OBJECT_MANAGEMENT_DELETE_RESULTS = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3F2
    )


    # WPD_PROPERTY_OBJECT_MANAGEMENT_DESTINATION_FOLDER_OBJECT_ID
    # [ VT_LPWSTR ] Indicates the destination folder for the move operation.
    WPD_PROPERTY_OBJECT_MANAGEMENT_DESTINATION_FOLDER_OBJECT_ID = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3F3
    )

    # WPD_PROPERTY_OBJECT_MANAGEMENT_MOVE_RESULTS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_ERROR,
    # where each element is the HRESULT indicating the success or failure of
    # the operation.
    WPD_PROPERTY_OBJECT_MANAGEMENT_MOVE_RESULTS = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3F4
    )


    # WPD_PROPERTY_OBJECT_MANAGEMENT_COPY_RESULTS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_ERROR,
    # where each element is the HRESULT indicating the success or failure of
    # the operation.
    WPD_PROPERTY_OBJECT_MANAGEMENT_COPY_RESULTS = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3F5
    )

    # WPD_PROPERTY_OBJECT_MANAGEMENT_UPDATE_PROPERTIES
    # [ VT_UNKNOWN ] IPortableDeviceValues containing the object properties to
    # update.
    WPD_PROPERTY_OBJECT_MANAGEMENT_UPDATE_PROPERTIES = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3F6
    )


    # WPD_PROPERTY_OBJECT_MANAGEMENT_PROPERTY_KEYS
    # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing the property keys
    # required to update this object.
    WPD_PROPERTY_OBJECT_MANAGEMENT_PROPERTY_KEYS = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3F7
    )

    # WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_FORMAT
    # [ VT_CLSID ] Indicates the object format the caller is interested in.
    WPD_PROPERTY_OBJECT_MANAGEMENT_OBJECT_FORMAT = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x3F8
    )

    # == == == == Command Options == == == ==
    # WPD_OPTION_OBJECT_MANAGEMENT_RECURSIVE_DELETE_SUPPORTED
    # [ VT_BOOL ] Indicates whether the driver supports recursive deletion.
    WPD_OPTION_OBJECT_MANAGEMENT_RECURSIVE_DELETE_SUPPORTED = DEFINE_PROPERTYKEY(
        0xEF1E43DD,
        0xA9ED,
        0x4341,
        0x8B,
        0xCC,
        0x18,
        0x61,
        0x92,
        0xAE,
        0xA0,
        0x89,
        0x1389
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_CAPABILITIES This command category is used to query capabilities of the device. *************************************************************************
    #
    WPD_CATEGORY_CAPABILITIES = DEFINE_GUID(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS
    # Return all commands supported by this driver. This includes custom
    # commands, if any.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # None
    # Results:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x2
    )


    # WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS
    # Returns the supported options for the specified command.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_COMMAND
    # Results:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS
    WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3
    )

    # WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES
    # This command is used by clients to query the functional categories
    # supported by the driver.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # None
    # Results:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x4
    )


    # WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS
    # Retrieves the ObjectIDs of the objects belonging to the specified
    # functional category.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY
    # Results:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS
    WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x5
    )

    # WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES
    # Retrieves the list of content types supported by this driver for the
    # specified functional category.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY
    # Results:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x6
    )


    # WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS
    # This command is used to query the possible formats supported by the
    # specified content type
    # (e.g. for image objects, the driver may choose to support JPEG and BMP files).
    #
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE
    # Results:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_FORMATS
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x7
    )

    # WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES
    # Get the list of properties that an object of the given format supports.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_FORMAT
    # Results:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x8
    )


    # WPD_COMMAND_CAPABILITIES_GET_FIXED_PROPERTY_ATTRIBUTES
    # Returns the property attributes that are the same for all objects of the
    # given format.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_FORMAT
    # [ Required ] WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS
    # Results:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES
    WPD_COMMAND_CAPABILITIES_GET_FIXED_PROPERTY_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x9
    )

    # WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS
    # Return all events supported by this driver. This includes custom events,
    # if any.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # None
    # Results:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0xA
    )


    # WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS
    # Return extra information about a specified event, such as whether the
    # event is for notification or action purposes.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_EVENT
    # Results:
    # [ Required ] WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS
    WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0xB
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS
    # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing all commands a
    # driver supports.
    WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3E9
    )


    # WPD_PROPERTY_CAPABILITIES_COMMAND
    # [ VT_UNKNOWN ] Indicates the command whose options the caller is
    # interested in.
    WPD_PROPERTY_CAPABILITIES_COMMAND = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3EA
    )

    # WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS
    # [ VT_UNKNOWN ] Contains an IPortableDeviceValues with the relevant
    # command options.
    WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3EB
    )


    # WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES
    # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of type VT_CLSID
    # which indicates the functional categories supported by the driver.
    WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3EC
    )

    # WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY
    # [ VT_CLSID ] The category the caller is interested in.
    WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3ED
    )


    # WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS
    # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection
    # (of type VT_LPWSTR) containing the ObjectIDs of the functional objects
    # who belong to the specified functional category.
    WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3EE
    )

    # WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES
    # [ VT_UNKNOWN ] Indicates list of content types supported for the
    # specified functional category.
    WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3EF
    )


    # WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE
    # [ VT_CLSID ] Indicates the content type whose formats the caller is
    # interested in.
    WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3F0
    )

    # WPD_PROPERTY_CAPABILITIES_FORMATS
    # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of VT_CLSID
    # values indicating the formats supported for the specified content type.
    WPD_PROPERTY_CAPABILITIES_FORMATS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3F1
    )


    # WPD_PROPERTY_CAPABILITIES_FORMAT
    # [ VT_CLSID ] Specifies the format the caller is interested in.
    WPD_PROPERTY_CAPABILITIES_FORMAT = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3F2
    )

    # WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS
    # [ VT_UNKNOWN ] An IPortableDeviceKeyCollection containing the property
    # keys.
    WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3F3
    )


    # WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES
    # [ VT_UNKNOWN ] An IPortableDeviceValues containing the property
    # attributes.
    WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3F4
    )

    # WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of VT_CLSID values
    # containing all events a driver supports.
    WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3F5
    )


    # WPD_PROPERTY_CAPABILITIES_EVENT
    # [ VT_CLSID ] Indicates the event the caller is interested in.
    WPD_PROPERTY_CAPABILITIES_EVENT = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3F6
    )

    # WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS
    # [ VT_UNKNOWN ] Contains an IPortableDeviceValues with the relevant event
    # options.
    WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS = DEFINE_PROPERTYKEY(
        0x0CABEC78,
        0x6B74,
        0x41C6,
        0x92,
        0x16,
        0x26,
        0x39,
        0xD1,
        0xFC,
        0xE3,
        0x56,
        0x3F7
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_STORAGE This category is for commands and parameters for storage functional objects. *************************************************************************
    #
    WPD_CATEGORY_STORAGE = DEFINE_GUID(
        0xD8F907A6,
        0x34CC,
        0x45FA,
        0x97,
        0xFB,
        0xD0,
        0x07,
        0xFA,
        0x47,
        0xEC,
        0x94
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_STORAGE_FORMAT
    # This command will format the storage.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_STORAGE_OBJECT_ID
    # Results:
    # None
    WPD_COMMAND_STORAGE_FORMAT = DEFINE_PROPERTYKEY(
        0xD8F907A6,
        0x34CC,
        0x45FA,
        0x97,
        0xFB,
        0xD0,
        0x07,
        0xFA,
        0x47,
        0xEC,
        0x94,
        0x2
    )

    # WPD_COMMAND_STORAGE_EJECT
    # This will eject the storage, if it is a removable store and is capable
    # of being ejected by the device.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_STORAGE_OBJECT_ID
    # Results:
    # None
    WPD_COMMAND_STORAGE_EJECT = DEFINE_PROPERTYKEY(
        0xD8F907A6,
        0x34CC,
        0x45FA,
        0x97,
        0xFB,
        0xD0,
        0x07,
        0xFA,
        0x47,
        0xEC,
        0x94,
        0x4
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_STORAGE_OBJECT_ID
    # [ VT_LPWSTR ] Indicates the object to format, move or eject.
    WPD_PROPERTY_STORAGE_OBJECT_ID = DEFINE_PROPERTYKEY(
        0xD8F907A6,
        0x34CC,
        0x45FA,
        0x97,
        0xFB,
        0xD0,
        0x07,
        0xFA,
        0x47,
        0xEC,
        0x94,
        0x3E9
    )

    # WPD_PROPERTY_STORAGE_DESTINATION_OBJECT_ID
    # [ VT_LPWSTR ] Indicates the (folder) object destination for a move
    # operation.
    WPD_PROPERTY_STORAGE_DESTINATION_OBJECT_ID = DEFINE_PROPERTYKEY(
        0xD8F907A6,
        0x34CC,
        0x45FA,
        0x97,
        0xFB,
        0xD0,
        0x07,
        0xFA,
        0x47,
        0xEC,
        0x94,
        0x3EA
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_SMS The commands in this category relate to Short-Message-Service functionality, typically exposed on mobile phones. *************************************************************************
    #
    WPD_CATEGORY_SMS = DEFINE_GUID(
        0xAFC25D66,
        0xFE0D,
        0x4114,
        0x90,
        0x97,
        0x97,
        0x0C,
        0x93,
        0xE9,
        0x20,
        0xD1
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_SMS_SEND
    # This command is used to initiate the sending of an SMS message.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_COMMON_COMMAND_TARGET
    # [ Required ] WPD_PROPERTY_SMS_RECIPIENT
    # [ Required ] WPD_PROPERTY_SMS_MESSAGE_TYPE
    # [ Optional ] WPD_PROPERTY_SMS_TEXT_MESSAGE
    # [ Optional ] WPD_PROPERTY_SMS_BINARY_MESSAGE
    # Results:
    # None
    WPD_COMMAND_SMS_SEND = DEFINE_PROPERTYKEY(
        0xAFC25D66,
        0xFE0D,
        0x4114,
        0x90,
        0x97,
        0x97,
        0x0C,
        0x93,
        0xE9,
        0x20,
        0xD1,
        0x2
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_SMS_RECIPIENT
    # [ VT_LPWSTR ] Indicates the recipient's address.
    WPD_PROPERTY_SMS_RECIPIENT = DEFINE_PROPERTYKEY(
        0xAFC25D66,
        0xFE0D,
        0x4114,
        0x90,
        0x97,
        0x97,
        0x0C,
        0x93,
        0xE9,
        0x20,
        0xD1,
        0x3E9
    )


    # WPD_PROPERTY_SMS_MESSAGE_TYPE
    # [ VT_UI4 ] Indicates whether the message is binary or text.
    WPD_PROPERTY_SMS_MESSAGE_TYPE = DEFINE_PROPERTYKEY(
        0xAFC25D66,
        0xFE0D,
        0x4114,
        0x90,
        0x97,
        0x97,
        0x0C,
        0x93,
        0xE9,
        0x20,
        0xD1,
        0x3EA
    )

    # WPD_PROPERTY_SMS_TEXT_MESSAGE
    # [ VT_LPWSTR ] if WPD_PROPERTY_SMS_MESSAGE_TYPE == SMS_TEXT_MESSAGE, then
    # this will contain the message body.
    WPD_PROPERTY_SMS_TEXT_MESSAGE = DEFINE_PROPERTYKEY(
        0xAFC25D66,
        0xFE0D,
        0x4114,
        0x90,
        0x97,
        0x97,
        0x0C,
        0x93,
        0xE9,
        0x20,
        0xD1,
        0x3EB
    )


    # WPD_PROPERTY_SMS_BINARY_MESSAGE
    # [ VT_VECTOR | VT_UI1 ] if WPD_PROPERTY_SMS_MESSAGE_TYPE ==
    # SMS_BINARY_MESSAGE, then this will contain the binary message body.
    WPD_PROPERTY_SMS_BINARY_MESSAGE = DEFINE_PROPERTYKEY(
        0xAFC25D66,
        0xFE0D,
        0x4114,
        0x90,
        0x97,
        0x97,
        0x0C,
        0x93,
        0xE9,
        0x20,
        0xD1,
        0x3EC
    )

    # == == == == Command Options == == == ==
    # WPD_OPTION_SMS_BINARY_MESSAGE_SUPPORTED
    # [ VT_BOOL ] Indicates whether the driver can support binary messages as
    # well as text messages.
    WPD_OPTION_SMS_BINARY_MESSAGE_SUPPORTED = DEFINE_PROPERTYKEY(
        0xAFC25D66,
        0xFE0D,
        0x4114,
        0x90,
        0x97,
        0x97,
        0x0C,
        0x93,
        0xE9,
        0x20,
        0xD1,
        0x1389
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_STILL_IMAGE_CAPTURE *************************************************************************
    #
    WPD_CATEGORY_STILL_IMAGE_CAPTURE = DEFINE_GUID(
        0x4FCD6982,
        0x22A2,
        0x4B05,
        0xA4,
        0x8B,
        0x62,
        0xD3,
        0x8B,
        0xF2,
        0x7B,
        0x32
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_STILL_IMAGE_CAPTURE_INITIATE
    # Initiates a still image capture. This is processed as a single command
    # i.e. there is no start or stop required.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_COMMON_COMMAND_TARGET
    # Results:
    # None
    WPD_COMMAND_STILL_IMAGE_CAPTURE_INITIATE = DEFINE_PROPERTYKEY(
        0x4FCD6982,
        0x22A2,
        0x4B05,
        0xA4,
        0x8B,
        0x62,
        0xD3,
        0x8B,
        0xF2,
        0x7B,
        0x32,
        0x2
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_MEDIA_CAPTURE *************************************************************************
    #
    WPD_CATEGORY_MEDIA_CAPTURE = DEFINE_GUID(
        0x59B433BA,
        0xFE44,
        0x4D8D,
        0x80,
        0x8C,
        0x6B,
        0xCB,
        0x9B,
        0x0F,
        0x15,
        0xE8
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_MEDIA_CAPTURE_START
    # Initiates a media capture operation that will only be ended by a
    # subsequent WPD_COMMAND_MEDIA_CAPTURE_STOP command. Typically used to
    # capture media streams such as audio and video.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_COMMON_COMMAND_TARGET
    # Results:
    # None
    WPD_COMMAND_MEDIA_CAPTURE_START = DEFINE_PROPERTYKEY(
        0x59B433BA,
        0xFE44,
        0x4D8D,
        0x80,
        0x8C,
        0x6B,
        0xCB,
        0x9B,
        0x0F,
        0x15,
        0xE8,
        0x2
    )


    # WPD_COMMAND_MEDIA_CAPTURE_STOP
    # Ends a media capture operation started by a
    # WPD_COMMAND_MEDIA_CAPTURE_START command. Typically used to end capture
    # of media streams such as audio and video.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_COMMON_COMMAND_TARGET
    # Results:
    # None
    WPD_COMMAND_MEDIA_CAPTURE_STOP = DEFINE_PROPERTYKEY(
        0x59B433BA,
        0xFE44,
        0x4D8D,
        0x80,
        0x8C,
        0x6B,
        0xCB,
        0x9B,
        0x0F,
        0x15,
        0xE8,
        0x3
    )

    # WPD_COMMAND_MEDIA_CAPTURE_PAUSE
    # Pauses a media capture operation started by a
    # WPD_COMMAND_MEDIA_CAPTURE_START command. Typically used to pause capture
    # of media streams such as audio and video.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_COMMON_COMMAND_TARGET
    # Results:
    # None
    WPD_COMMAND_MEDIA_CAPTURE_PAUSE = DEFINE_PROPERTYKEY(
        0x59B433BA,
        0xFE44,
        0x4D8D,
        0x80,
        0x8C,
        0x6B,
        0xCB,
        0x9B,
        0x0F,
        0x15,
        0xE8,
        0x4
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_DEVICE_HINTS The commands in this category relate to hints that a device can provide to improve end-user experience. *************************************************************************
    #
    WPD_CATEGORY_DEVICE_HINTS = DEFINE_GUID(
        0x0D5FB92B,
        0xCB46,
        0x4C4F,
        0x83,
        0x43,
        0x0B,
        0xC3,
        0xD3,
        0xF1,
        0x7C,
        0x84
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_DEVICE_HINTS_GET_CONTENT_LOCATION
    # This command is used to retrieve the ObjectIDs of folders that contain
    # the specified content type.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_DEVICE_HINTS_CONTENT_TYPE
    # Results:
    # [ Required ] WPD_PROPERTY_DEVICE_HINTS_CONTENT_LOCATIONS
    WPD_COMMAND_DEVICE_HINTS_GET_CONTENT_LOCATION = DEFINE_PROPERTYKEY(
        0x0D5FB92B,
        0xCB46,
        0x4C4F,
        0x83,
        0x43,
        0x0B,
        0xC3,
        0xD3,
        0xF1,
        0x7C,
        0x84,
        0x2
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_DEVICE_HINTS_CONTENT_TYPE
    # [ VT_CLSID ] Indicates the WPD content type that the caller is looking
    # for. For example, to get the top-level folder objects that contain
    # images, this parameter would be WPD_CONTENT_TYPE_IMAGE.
    WPD_PROPERTY_DEVICE_HINTS_CONTENT_TYPE = DEFINE_PROPERTYKEY(
        0x0D5FB92B,
        0xCB46,
        0x4C4F,
        0x83,
        0x43,
        0x0B,
        0xC3,
        0xD3,
        0xF1,
        0x7C,
        0x84,
        0x3E9
    )


    # WPD_PROPERTY_DEVICE_HINTS_CONTENT_LOCATIONS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type VT_LPWSTR
    # indicating a list of folder ObjectIDs.
    WPD_PROPERTY_DEVICE_HINTS_CONTENT_LOCATIONS = DEFINE_PROPERTYKEY(
        0x0D5FB92B,
        0xCB46,
        0x4C4F,
        0x83,
        0x43,
        0x0B,
        0xC3,
        0xD3,
        0xF1,
        0x7C,
        0x84,
        0x3EA
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CLASS_EXTENSION_V1 The commands in this category relate to the WPD device class extension. *************************************************************************
    #
    WPD_CLASS_EXTENSION_V1 = DEFINE_GUID(
        0x33FB0D11,
        0x64A3,
        0x4FAC,
        0xB4,
        0xC7,
        0x3D,
        0xFE,
        0xAA,
        0x99,
        0xB0,
        0x51
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_CLASS_EXTENSION_WRITE_DEVICE_INFORMATION
    # This command is used to update the a cache of device-specific
    # information.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_VALUES
    # Results:
    # [ Required ]
    # WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_WRITE_RESULTS
    WPD_COMMAND_CLASS_EXTENSION_WRITE_DEVICE_INFORMATION = DEFINE_PROPERTYKEY(
        0x33FB0D11,
        0x64A3,
        0x4FAC,
        0xB4,
        0xC7,
        0x3D,
        0xFE,
        0xAA,
        0x99,
        0xB0,
        0x51,
        0x2
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_VALUES
    # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the
    # values.
    WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_VALUES = DEFINE_PROPERTYKEY(
        0x33FB0D11,
        0x64A3,
        0x4FAC,
        0xB4,
        0xC7,
        0x3D,
        0xFE,
        0xAA,
        0x99,
        0xB0,
        0x51,
        0x3E9
    )

    # WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_WRITE_RESULTS
    # [ VT_UNKNOWN ] This is an IPortableDeviceValues which contains the
    # result of each value write operation.
    WPD_PROPERTY_CLASS_EXTENSION_DEVICE_INFORMATION_WRITE_RESULTS = DEFINE_PROPERTYKEY(
        0x33FB0D11,
        0x64A3,
        0x4FAC,
        0xB4,
        0xC7,
        0x3D,
        0xFE,
        0xAA,
        0x99,
        0xB0,
        0x51,
        0x3EA
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CLASS_EXTENSION_V2 The commands in this category relate to the WPD device class extension. *************************************************************************
    #
    WPD_CLASS_EXTENSION_V2 = DEFINE_GUID(
        0x7F0779B5,
        0xFA2B,
        0x4766,
        0x9C,
        0xB2,
        0xF7,
        0x3B,
        0xA3,
        0x0B,
        0x67,
        0x58
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_CLASS_EXTENSION_REGISTER_SERVICE_INTERFACES
    # This command is used to register a service's Plug and Play interfaces.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_CLASS_EXTENSION_SERVICE_OBJECT_ID
    # [ Required ] WPD_PROPERTY_CLASS_EXTENSION_SERVICE_INTERFACES
    # Results:
    # [ Required ] WPD_PROPERTY_CLASS_EXTENSION_SERVICE_REGISTRATION_RESULTS
    WPD_COMMAND_CLASS_EXTENSION_REGISTER_SERVICE_INTERFACES = DEFINE_PROPERTYKEY(
        0x7F0779B5,
        0xFA2B,
        0x4766,
        0x9C,
        0xB2,
        0xF7,
        0x3B,
        0xA3,
        0x0B,
        0x67,
        0x58,
        0x2
    )

    # WPD_COMMAND_CLASS_EXTENSION_UNREGISTER_SERVICE_INTERFACES
    # This command is used to unregister a service's Plug and Play interfaces.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_CLASS_EXTENSION_SERVICE_OBJECT_ID
    # [ Required ] WPD_PROPERTY_CLASS_EXTENSION_SERVICE_INTERFACES
    # Results:
    # [ Required ] WPD_PROPERTY_CLASS_EXTENSION_SERVICE_REGISTRATION_RESULTS
    WPD_COMMAND_CLASS_EXTENSION_UNREGISTER_SERVICE_INTERFACES = DEFINE_PROPERTYKEY(
        0x7F0779B5,
        0xFA2B,
        0x4766,
        0x9C,
        0xB2,
        0xF7,
        0x3B,
        0xA3,
        0x0B,
        0x67,
        0x58,
        0x3
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_CLASS_EXTENSION_SERVICE_OBJECT_ID
    # [ VT_LPWSTR ] The Object ID of the service.
    WPD_PROPERTY_CLASS_EXTENSION_SERVICE_OBJECT_ID = DEFINE_PROPERTYKEY(
        0x7F0779B5,
        0xFA2B,
        0x4766,
        0x9C,
        0xB2,
        0xF7,
        0x3B,
        0xA3,
        0x0B,
        0x67,
        0x58,
        0x3E9
    )

    # WPD_PROPERTY_CLASS_EXTENSION_SERVICE_INTERFACES
    # [ VT_UNKNOWN ] This is an IPortablePropVariantCollection of type
    # VT_CLSID which contains the interface GUIDs that this service
    # implements, including the service type GUID.
    WPD_PROPERTY_CLASS_EXTENSION_SERVICE_INTERFACES = DEFINE_PROPERTYKEY(
        0x7F0779B5,
        0xFA2B,
        0x4766,
        0x9C,
        0xB2,
        0xF7,
        0x3B,
        0xA3,
        0x0B,
        0x67,
        0x58,
        0x3EA
    )


    # WPD_PROPERTY_CLASS_EXTENSION_SERVICE_REGISTRATION_RESULTS
    # [ VT_UNKNOWN ] This is an IPortablePropVariantCollection of type
    # VT_ERROR, where each element is the HRESULT indicating the success or
    # failure of the operation.
    WPD_PROPERTY_CLASS_EXTENSION_SERVICE_REGISTRATION_RESULTS = DEFINE_PROPERTYKEY(
        0x7F0779B5,
        0xFA2B,
        0x4766,
        0x9C,
        0xB2,
        0xF7,
        0x3B,
        0xA3,
        0x0B,
        0x67,
        0x58,
        0x3EB
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_NETWORK_CONFIGURATION The commands in this category are used for Network Association and WiFi Configuration. *************************************************************************
    #
    WPD_CATEGORY_NETWORK_CONFIGURATION = DEFINE_GUID(
        0x78F9C6FC,
        0x79B8,
        0x473C,
        0x90,
        0x60,
        0x6B,
        0xD2,
        0x3D,
        0xD0,
        0x72,
        0xC4
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_GENERATE_KEYPAIR
    # Initiates the generation of a public/private key pair and returns the
    # public key.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # None
    # Results:
    # [ Required ] WPD_PROPERTY_PUBLIC_KEY
    WPD_COMMAND_GENERATE_KEYPAIR = DEFINE_PROPERTYKEY(
        0x78F9C6FC,
        0x79B8,
        0x473C,
        0x90,
        0x60,
        0x6B,
        0xD2,
        0x3D,
        0xD0,
        0x72,
        0xC4,
        0x2
    )


    # WPD_COMMAND_COMMIT_KEYPAIR
    # Commits a public/private key pair.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # None
    # Results:
    # None
    WPD_COMMAND_COMMIT_KEYPAIR = DEFINE_PROPERTYKEY(
        0x78F9C6FC,
        0x79B8,
        0x473C,
        0x90,
        0x60,
        0x6B,
        0xD2,
        0x3D,
        0xD0,
        0x72,
        0xC4,
        0x3
    )

    # WPD_COMMAND_PROCESS_WIRELESS_PROFILE
    # Initiates the processing of a Wireless Profile file.
    # Access:
    # (FILE_READ_ACCESS | FILE_WRITE_ACCESS)
    # Parameters:
    # [ Required ] WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID
    # Results:
    # None
    WPD_COMMAND_PROCESS_WIRELESS_PROFILE = DEFINE_PROPERTYKEY(
        0x78F9C6FC,
        0x79B8,
        0x473C,
        0x90,
        0x60,
        0x6B,
        0xD2,
        0x3D,
        0xD0,
        0x72,
        0xC4,
        0x4
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_PUBLIC_KEY
    # [ VT_VECTOR | VT_UI1 ] A public key generated for RSA key exchange.
    WPD_PROPERTY_PUBLIC_KEY = DEFINE_PROPERTYKEY(
        0x78F9C6FC,
        0x79B8,
        0x473C,
        0x90,
        0x60,
        0x6B,
        0xD2,
        0x3D,
        0xD0,
        0x72,
        0xC4,
        0x3E9
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_SERVICE_COMMON The commands in this category relate to a device service. *************************************************************************
    #
    WPD_CATEGORY_SERVICE_COMMON = DEFINE_GUID(
        0x322F071D,
        0x36EF,
        0x477F,
        0xB4,
        0xB5,
        0x6F,
        0x52,
        0xD7,
        0x34,
        0xBA,
        0xEE
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_SERVICE_COMMON_GET_SERVICE_OBJECT_ID
    # This command is used to get the service object identifier.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # None
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_OBJECT_ID
    WPD_COMMAND_SERVICE_COMMON_GET_SERVICE_OBJECT_ID = DEFINE_PROPERTYKEY(
        0x322F071D,
        0x36EF,
        0x477F,
        0xB4,
        0xB5,
        0x6F,
        0x52,
        0xD7,
        0x34,
        0xBA,
        0xEE,
        0x2
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_SERVICE_OBJECT_ID
    # [ VT_LPWSTR ] Contains the service object identifier.
    WPD_PROPERTY_SERVICE_OBJECT_ID = DEFINE_PROPERTYKEY(
        0x322F071D,
        0x36EF,
        0x477F,
        0xB4,
        0xB5,
        0x6F,
        0x52,
        0xD7,
        0x34,
        0xBA,
        0xEE,
        0x3E9
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_SERVICE_CAPABILITIES The commands in this category relate to capabilities of a device service. *************************************************************************
    #
    WPD_CATEGORY_SERVICE_CAPABILITIES = DEFINE_GUID(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS
    # This command is used to get the methods that apply to a service.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # None
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_METHODS
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x2
    )


    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS_BY_FORMAT
    # This command is used to get the methods that apply to a format of a
    # service.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_METHODS
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS_BY_FORMAT = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3
    )

    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_ATTRIBUTES
    # This command is used to get the attributes of a method.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD_ATTRIBUTES
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x4
    )


    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_PARAMETER_ATTRIBUTES
    # This command is used to get the attributes of a parameter used in a
    # method.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER_ATTRIBUTES
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_PARAMETER_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x5
    )

    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMATS
    # This command is used to get formats supported by this service.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # None
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_FORMATS
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMATS = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x6
    )


    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_ATTRIBUTES
    # This command is used to get attributes of a format, such as the format
    # name.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT_ATTRIBUTES
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x7
    )

    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES
    # This command is used to get supported properties of a format.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_KEYS
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x8
    )


    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_PROPERTY_ATTRIBUTES
    # This command is used to get the property attributes that are same for
    # all objects of a given format on the service.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_KEYS
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_ATTRIBUTES
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_PROPERTY_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x9
    )

    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_EVENTS
    # This command is used to get the supported events of the service.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # None
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_EVENTS
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_EVENTS = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0xA
    )


    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_ATTRIBUTES
    # This command is used to get the attributes of an event.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT_ATTRIBUTES
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0xB
    )

    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_PARAMETER_ATTRIBUTES
    # This command is used to get the attributes of a parameter used in an
    # event.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER_ATTRIBUTES
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_PARAMETER_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0xC
    )


    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_INHERITED_SERVICES
    # This command is used to get the inherited services.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITANCE_TYPE
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITED_SERVICES
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_INHERITED_SERVICES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0xD
    )

    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_RENDERING_PROFILES
    # This command is used to get the resource rendering profiles for a format.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_RENDERING_PROFILES
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_RENDERING_PROFILES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0xE
    )


    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_COMMANDS
    # Return all commands supported by this driver for a service. This
    # includes custom commands, if any.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # None
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_COMMANDS
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_COMMANDS = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0xF
    )

    # WPD_COMMAND_SERVICE_CAPABILITIES_GET_COMMAND_OPTIONS
    # Returns the supported options for the specified command.
    # Access:
    # FILE_READ_ACCESS
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND_OPTIONS
    WPD_COMMAND_SERVICE_CAPABILITIES_GET_COMMAND_OPTIONS = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x10
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_METHODS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection (of type VT_CLSID)
    # containing methods that apply to a service.
    WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_METHODS = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3E9
    )

    # WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT
    # [ VT_CLSID ] Indicates the format the caller is interested in.
    WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3EA
    )


    # WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD
    # [ VT_CLSID ] Indicates the method the caller is interested in.
    WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3EB
    )

    # WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD_ATTRIBUTES
    # [ VT_UNKNOWN ] IPortableDeviceValues containing the method attributes.
    WPD_PROPERTY_SERVICE_CAPABILITIES_METHOD_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3EC
    )


    # WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER
    # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing the parameter the
    # caller is interested in.
    WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3ED
    )

    # WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER_ATTRIBUTES
    # [ VT_UNKNOWN ] IPortableDeviceValues containing the parameter attributes.
    WPD_PROPERTY_SERVICE_CAPABILITIES_PARAMETER_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3EE
    )


    # WPD_PROPERTY_SERVICE_CAPABILITIES_FORMATS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection (of type VT_CLSID)
    # containing the formats.
    WPD_PROPERTY_SERVICE_CAPABILITIES_FORMATS = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3EF
    )

    # WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT_ATTRIBUTES
    # [ VT_UNKNOWN ] IPortableDeviceValues containing the format attributes,
    # such as the format name and MIME Type.
    WPD_PROPERTY_SERVICE_CAPABILITIES_FORMAT_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3F0
    )


    # WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_KEYS
    # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing the supported
    # property keys.
    WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_KEYS = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3F1
    )

    # WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_ATTRIBUTES
    # [ VT_UNKNOWN ] IPortableDeviceValues containing the property attributes.
    WPD_PROPERTY_SERVICE_CAPABILITIES_PROPERTY_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3F2
    )


    # WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_EVENTS
    # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection (of type VT_CLSID)
    # containing all events supported by the service.
    WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_EVENTS = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3F3
    )

    # WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT
    # [ VT_CLSID ] Indicates the event the caller is interested in.
    WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3F4
    )


    # WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT_ATTRIBUTES
    # [ VT_UNKNOWN ] IPortableDeviceValues containing the event attributes.
    WPD_PROPERTY_SERVICE_CAPABILITIES_EVENT_ATTRIBUTES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3F5
    )

    # WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITANCE_TYPE
    # [ VT_UI4 ] Indicates the inheritance type the caller is interested in.
    WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITANCE_TYPE = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3F6
    )


    # WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITED_SERVICES
    # [ VT_UNKNOWN ] Contains the list of inherited services.
    WPD_PROPERTY_SERVICE_CAPABILITIES_INHERITED_SERVICES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3F7
    )

    # WPD_PROPERTY_SERVICE_CAPABILITIES_RENDERING_PROFILES
    # [ VT_UNKNOWN ] Contains the list of format rendering profiles.
    WPD_PROPERTY_SERVICE_CAPABILITIES_RENDERING_PROFILES = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3F8
    )


    # WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_COMMANDS
    # [ VT_UNKNOWN ] IPortableDeviceKeyCollection containing all commands a
    # driver supports for a service.
    WPD_PROPERTY_SERVICE_CAPABILITIES_SUPPORTED_COMMANDS = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3F9
    )

    # WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND
    # [ VT_UNKNOWN ] Indicates the command whose options the caller is
    # interested in.
    WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3FA
    )


    # WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND_OPTIONS
    # [ VT_UNKNOWN ] Contains an IPortableDeviceValues with the relevant
    # command options.
    WPD_PROPERTY_SERVICE_CAPABILITIES_COMMAND_OPTIONS = DEFINE_PROPERTYKEY(
        0x24457E74,
        0x2E9F,
        0x44F9,
        0x8C,
        0x57,
        0x1D,
        0x1B,
        0xCB,
        0x17,
        0x0B,
        0x89,
        0x3FB
    )

    # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CATEGORY_SERVICE_METHODS The commands in this category relate to methods of a device service. *************************************************************************
    #
    WPD_CATEGORY_SERVICE_METHODS = DEFINE_GUID(
        0x2D521CA8,
        0xC1B0,
        0x4268,
        0xA3,
        0x42,
        0xCF,
        0x19,
        0x32,
        0x15,
        0x69,
        0xBC
    )

    # == == == == Commands == == == ==
    # WPD_COMMAND_SERVICE_METHODS_START_INVOKE
    # Invokes a service method.
    # Access:
    # Dependent on the value of WPD_METHOD_ATTRIBUTE_ACCESS.
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_METHOD
    # [ Required ] WPD_PROPERTY_SERVICE_METHOD_PARAMETER_VALUES
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_METHOD_CONTEXT
    WPD_COMMAND_SERVICE_METHODS_START_INVOKE = DEFINE_PROPERTYKEY(
        0x2D521CA8,
        0xC1B0,
        0x4268,
        0xA3,
        0x42,
        0xCF,
        0x19,
        0x32,
        0x15,
        0x69,
        0xBC,
        0x2
    )


    # WPD_COMMAND_SERVICE_METHODS_CANCEL_INVOKE
    # This command is sent when a client wants to cancel a method that is
    # currently still in progress.
    # Access:
    # Dependent on the value of WPD_METHOD_ATTRIBUTE_ACCESS.
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_METHOD_CONTEXT
    # Results:
    # None
    WPD_COMMAND_SERVICE_METHODS_CANCEL_INVOKE = DEFINE_PROPERTYKEY(
        0x2D521CA8,
        0xC1B0,
        0x4268,
        0xA3,
        0x42,
        0xCF,
        0x19,
        0x32,
        0x15,
        0x69,
        0xBC,
        0x3
    )

    # WPD_COMMAND_SERVICE_METHODS_END_INVOKE
    # This command is sent in response to a WPD_EVENT_SERVICE_METHOD_COMPLETE
    # event from the driver to retrieve the method results.
    # Access:
    # Dependent on the value of WPD_METHOD_ATTRIBUTE_ACCESS.
    # Parameters:
    # [ Required ] WPD_PROPERTY_SERVICE_METHOD_CONTEXT
    # Results:
    # [ Required ] WPD_PROPERTY_SERVICE_METHOD_RESULT_VALUES
    # [ Required ] WPD_PROPERTY_SERVICE_METHOD_HRESULT
    WPD_COMMAND_SERVICE_METHODS_END_INVOKE = DEFINE_PROPERTYKEY(
        0x2D521CA8,
        0xC1B0,
        0x4268,
        0xA3,
        0x42,
        0xCF,
        0x19,
        0x32,
        0x15,
        0x69,
        0xBC,
        0x4
    )

    # == == == == Command Parameters == == == ==
    # WPD_PROPERTY_SERVICE_METHOD
    # [ VT_CLSID ] Indicates the method to invoke.
    WPD_PROPERTY_SERVICE_METHOD = DEFINE_PROPERTYKEY(
        0x2D521CA8,
        0xC1B0,
        0x4268,
        0xA3,
        0x42,
        0xCF,
        0x19,
        0x32,
        0x15,
        0x69,
        0xBC,
        0x3E9
    )

    # WPD_PROPERTY_SERVICE_METHOD_PARAMETER_VALUES
    # [ VT_UNKNOWN ] IPortableDeviceValues containing the method parameters.
    WPD_PROPERTY_SERVICE_METHOD_PARAMETER_VALUES = DEFINE_PROPERTYKEY(
        0x2D521CA8,
        0xC1B0,
        0x4268,
        0xA3,
        0x42,
        0xCF,
        0x19,
        0x32,
        0x15,
        0x69,
        0xBC,
        0x3EA
    )


    # WPD_PROPERTY_SERVICE_METHOD_RESULT_VALUES
    # [ VT_UNKNOWN ] IPortableDeviceValues containing the method results.
    WPD_PROPERTY_SERVICE_METHOD_RESULT_VALUES = DEFINE_PROPERTYKEY(
        0x2D521CA8,
        0xC1B0,
        0x4268,
        0xA3,
        0x42,
        0xCF,
        0x19,
        0x32,
        0x15,
        0x69,
        0xBC,
        0x3EB
    )

    # WPD_PROPERTY_SERVICE_METHOD_CONTEXT
    # [ VT_LPWSTR ] The unique context identifying this method operation.
    WPD_PROPERTY_SERVICE_METHOD_CONTEXT = DEFINE_PROPERTYKEY(
        0x2D521CA8,
        0xC1B0,
        0x4268,
        0xA3,
        0x42,
        0xCF,
        0x19,
        0x32,
        0x15,
        0x69,
        0xBC,
        0x3EC
    )


    # WPD_PROPERTY_SERVICE_METHOD_HRESULT
    # [ VT_ERROR ] Contains the status HRESULT of this method invocation.
    WPD_PROPERTY_SERVICE_METHOD_HRESULT = DEFINE_PROPERTYKEY(
        0x2D521CA8,
        0xC1B0,
        0x4268,
        0xA3,
        0x42,
        0xCF,
        0x19,
        0x32,
        0x15,
        0x69,
        0xBC,
        0x3ED
    )

    # ************************************************************************** This section defines all Resource keys. Resources are place-holders for binary data. *************************************************************************
    #
    # WPD_RESOURCE_DEFAULT
    # Represents the entire object's data. There can be only one default
    # resource on an object.
    WPD_RESOURCE_DEFAULT = DEFINE_PROPERTYKEY(
        0xE81E79BE,
        0x34F0,
        0x41BF,
        0xB5,
        0x3F,
        0xF1,
        0xA0,
        0x6A,
        0xE8,
        0x78,
        0x42,
        0x0
    )


    # WPD_RESOURCE_CONTACT_PHOTO
    # Represents the contact's photo data.
    WPD_RESOURCE_CONTACT_PHOTO = DEFINE_PROPERTYKEY(
        0x2C4D6803,
        0x80EA,
        0x4580,
        0xAF,
        0x9A,
        0x5B,
        0xE1,
        0xA2,
        0x3E,
        0xDD,
        0xCB,
        0x0
    )

    # WPD_RESOURCE_THUMBNAIL
    # Represents the thumbnail data for an object.
    WPD_RESOURCE_THUMBNAIL = DEFINE_PROPERTYKEY(
        0xC7C407BA,
        0x98FA,
        0x46B5,
        0x99,
        0x60,
        0x23,
        0xFE,
        0xC1,
        0x24,
        0xCF,
        0xDE,
        0x0
    )


    # WPD_RESOURCE_ICON
    # Represents the icon data for an object.
    WPD_RESOURCE_ICON = DEFINE_PROPERTYKEY(
        0xF195FED8,
        0xAA28,
        0x4EE3,
        0xB1,
        0x53,
        0xE1,
        0x82,
        0xDD,
        0x5E,
        0xDC,
        0x39,
        0x0
    )

    # WPD_RESOURCE_AUDIO_CLIP
    # Represents an audio sample data for an object.
    WPD_RESOURCE_AUDIO_CLIP = DEFINE_PROPERTYKEY(
        0x3BC13982,
        0x85B1,
        0x48E0,
        0x95,
        0xA6,
        0x8D,
        0x3A,
        0xD0,
        0x6B,
        0xE1,
        0x17,
        0x0
    )


    # WPD_RESOURCE_ALBUM_ART
    # Represents the album artwork this media originated from.
    WPD_RESOURCE_ALBUM_ART = DEFINE_PROPERTYKEY(
        0xF02AA354,
        0x2300,
        0x4E2D,
        0xA1,
        0xB9,
        0x3B,
        0x67,
        0x30,
        0xF7,
        0xFA,
        0x21,
        0x0
    )

    # WPD_RESOURCE_GENERIC
    # Represents an arbitrary binary blob associated with this object.
    WPD_RESOURCE_GENERIC = DEFINE_PROPERTYKEY(
        0xB9B9F515,
        0xBA70,
        0x4647,
        0x94,
        0xDC,
        0xFA,
        0x49,
        0x25,
        0xE9,
        0x5A,
        0x07,
        0x0
    )


    # WPD_RESOURCE_VIDEO_CLIP
    # Represents a video sample for an object.
    WPD_RESOURCE_VIDEO_CLIP = DEFINE_PROPERTYKEY(
        0xB566EE42,
        0x6368,
        0x4290,
        0x86,
        0x62,
        0x70,
        0x18,
        0x2F,
        0xB7,
        0x9F,
        0x20,
        0x0
    )

    # WPD_RESOURCE_BRANDING_ART
    # Represents the product branding artwork or logo for an object. This
    # resource is typically found on, but not limited to the device object.
    WPD_RESOURCE_BRANDING_ART = DEFINE_PROPERTYKEY(
        0xB633B1AE,
        0x6CAF,
        0x4A87,
        0x95,
        0x89,
        0x22,
        0xDE,
        0xD6,
        0xDD,
        0x58,
        0x99,
        0x0
    )

    # ************************************************************************** This section defines the legacy WPD definitions When WPD_SERVICES_STRICT mode is defined, these definitions are removed from this header file. You may find replacements or equivalents in the Device Services headers (for example, BridgeDeviceService.h). *************************************************************************
    #
        # ************************************************************************** This section defines the legacy WPD Formats *************************************************************************
        #
    if not defined(WPD_SERVICES_STRICT):
        # WPD_OBJECT_FORMAT_PROPERTIES_ONLY
        # This object has no data stream and is completely specified by
        # properties only.
        # Device Services Format: FORMAT_Association
        WPD_OBJECT_FORMAT_PROPERTIES_ONLY = DEFINE_GUID(
            0x30010000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_UNSPECIFIED
        # An undefined object format on the device
        # (e.g. objects that can not be classified by the other defined WPD format codes)
        #
        # Device Services Format: FORMAT_Undefined
        WPD_OBJECT_FORMAT_UNSPECIFIED = DEFINE_GUID(
            0x30000000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_SCRIPT
        # A device model-specific script
        # Device Services Format: FORMAT_DeviceScript
        WPD_OBJECT_FORMAT_SCRIPT = DEFINE_GUID(
            0x30020000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_EXECUTABLE
        # A device model-specific binary executable
        # Device Services Format: FORMAT_DeviceExecutable
        WPD_OBJECT_FORMAT_EXECUTABLE = DEFINE_GUID(
            0x30030000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_TEXT
        # A text file
        # Device Services Format: FORMAT_TextDocument
        WPD_OBJECT_FORMAT_TEXT = DEFINE_GUID(
            0x30040000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_HTML
        # A HyperText Markup Language file (text)
        # Device Services Format: FORMAT_HTMLDocument
        WPD_OBJECT_FORMAT_HTML = DEFINE_GUID(
            0x30050000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_DPOF
        # A Digital Print Order File (text)
        # Device Services Format: FORMAT_DPOFDocument
        WPD_OBJECT_FORMAT_DPOF = DEFINE_GUID(
            0x30060000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_AIFF
        # Audio file format
        # Device Services Format: FORMAT_AIFFFile
        WPD_OBJECT_FORMAT_AIFF = DEFINE_GUID(
            0x30070000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_WAVE
        # Audio file format
        # Device Services Format: FORMAT_WAVFile
        WPD_OBJECT_FORMAT_WAVE = DEFINE_GUID(
            0x30080000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_MP3
        # Audio file format
        # Device Services Format: FORMAT_MP3File
        WPD_OBJECT_FORMAT_MP3 = DEFINE_GUID(
            0x30090000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_AVI
        # Video file format
        # Device Services Format: FORMAT_AVIFile
        WPD_OBJECT_FORMAT_AVI = DEFINE_GUID(
            0x300A0000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_MPEG
        # Video file format
        # Device Services Format: FORMAT_MPEGFile
        WPD_OBJECT_FORMAT_MPEG = DEFINE_GUID(
            0x300B0000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_ASF
        # Video file format (Microsoft Advanced Streaming Format)
        # Device Services Format: FORMAT_ASFFile
        WPD_OBJECT_FORMAT_ASF = DEFINE_GUID(
            0x300C0000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_EXIF
        # Image file format (Exchangeable File Format), JEIDA standard
        # Device Services Format: FORMAT_EXIFImage
        WPD_OBJECT_FORMAT_EXIF = DEFINE_GUID(
            0x38010000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_TIFFEP
        # Image file format (Tag Image File Format for Electronic Photography)
        # Device Services Format: FORMAT_TIFFEPImage
        WPD_OBJECT_FORMAT_TIFFEP = DEFINE_GUID(
            0x38020000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_FLASHPIX
        # Image file format (Structured Storage Image Format)
        # Device Services Format: FORMAT_FlashPixImage
        WPD_OBJECT_FORMAT_FLASHPIX = DEFINE_GUID(
            0x38030000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_BMP
        # Image file format (Microsoft Windows Bitmap file)
        # Device Services Format: FORMAT_BMPImage
        WPD_OBJECT_FORMAT_BMP = DEFINE_GUID(
            0x38040000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_CIFF
        # Image file format (Canon Camera Image File Format)
        # Device Services Format: FORMAT_CIFFImage
        WPD_OBJECT_FORMAT_CIFF = DEFINE_GUID(
            0x38050000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_GIF
        # Image file format (Graphics Interchange Format)
        # Device Services Format: FORMAT_GIFImage
        WPD_OBJECT_FORMAT_GIF = DEFINE_GUID(
            0x38070000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_JFIF
        # Image file format (JPEG Interchange Format)
        # Device Services Format: FORMAT_JFIFImage
        WPD_OBJECT_FORMAT_JFIF = DEFINE_GUID(
            0x38080000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_PCD
        # Image file format (PhotoCD Image Pac)
        # Device Services Format: FORMAT_PCDImage
        WPD_OBJECT_FORMAT_PCD = DEFINE_GUID(
            0x38090000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_PICT
        # Image file format (Quickdraw Image Format)
        # Device Services Format: FORMAT_PICTImage
        WPD_OBJECT_FORMAT_PICT = DEFINE_GUID(
            0x380A0000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_PNG
        # Image file format (Portable Network Graphics)
        # Device Services Format: FORMAT_PNGImage
        WPD_OBJECT_FORMAT_PNG = DEFINE_GUID(
            0x380B0000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_TIFF
        # Image file format (Tag Image File Format)
        # Device Services Format: FORMAT_TIFFImage
        WPD_OBJECT_FORMAT_TIFF = DEFINE_GUID(
            0x380D0000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_TIFFIT
        # Image file format
        # (Tag Image File Format for Informational Technology) Graphic Arts
        # Device Services Format: FORMAT_TIFFITImage
        WPD_OBJECT_FORMAT_TIFFIT = DEFINE_GUID(
            0x380E0000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_JP2
        # Image file format (JPEG2000 Baseline File Format)
        # Device Services Format: FORMAT_JP2Image
        WPD_OBJECT_FORMAT_JP2 = DEFINE_GUID(
            0x380F0000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_JPX
        # Image file format (JPEG2000 Extended File Format)
        # Device Services Format: FORMAT_JPXImage
        WPD_OBJECT_FORMAT_JPX = DEFINE_GUID(
            0x38100000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_WBMP
        # Image file format (Wireless Application Protocol Bitmap Format)
        # Device Services Format: FORMAT_WBMPImage
        WPD_OBJECT_FORMAT_WBMP = DEFINE_GUID(
            0xB8030000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_JPEGXR
        # Image file format (JPEG XR, also known as HD Photo)
        # Device Services Format: FORMAT_JPEGXRImage
        WPD_OBJECT_FORMAT_JPEGXR = DEFINE_GUID(
            0xB8040000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_WINDOWSIMAGEFORMAT
        # Image file format
        # Device Services Format: FORMAT_HDPhotoImage
        WPD_OBJECT_FORMAT_WINDOWSIMAGEFORMAT = DEFINE_GUID(
            0xB8810000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_WMA
        # Audio file format (Windows Media Audio)
        # Device Services Format: FORMAT_WMAFile
        WPD_OBJECT_FORMAT_WMA = DEFINE_GUID(
            0xB9010000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_WMV
        # Video file format (Windows Media Video)
        # Device Services Format: FORMAT_WMVFile
        WPD_OBJECT_FORMAT_WMV = DEFINE_GUID(
            0xB9810000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_WPLPLAYLIST
        # Playlist file format
        # Device Services Format: FORMAT_WPLPlaylist
        WPD_OBJECT_FORMAT_WPLPLAYLIST = DEFINE_GUID(
            0xBA100000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_M3UPLAYLIST
        # Playlist file format
        # Device Services Format: FORMAT_M3UPlaylist
        WPD_OBJECT_FORMAT_M3UPLAYLIST = DEFINE_GUID(
            0xBA110000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_MPLPLAYLIST
        # Playlist file format
        # Device Services Format: FORMAT_MPLPlaylist
        WPD_OBJECT_FORMAT_MPLPLAYLIST = DEFINE_GUID(
            0xBA120000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_ASXPLAYLIST
        # Playlist file format
        # Device Services Format: FORMAT_ASXPlaylist
        WPD_OBJECT_FORMAT_ASXPLAYLIST = DEFINE_GUID(
            0xBA130000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_PLSPLAYLIST
        # Playlist file format
        # Device Services Format: FORMAT_PSLPlaylist
        WPD_OBJECT_FORMAT_PLSPLAYLIST = DEFINE_GUID(
            0xBA140000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_ABSTRACT_CONTACT_GROUP
        # Generic format for contact group objects
        # Device Services Format: FORMAT_AbstractContactGroup
        WPD_OBJECT_FORMAT_ABSTRACT_CONTACT_GROUP = DEFINE_GUID(
            0xBA060000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_ABSTRACT_MEDIA_CAST
        # MediaCast file format
        # Device Services Format: FORMAT_AbstractMediacast
        WPD_OBJECT_FORMAT_ABSTRACT_MEDIA_CAST = DEFINE_GUID(
            0xBA0B0000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_VCALENDAR1
        # VCALENDAR file format (VCALENDAR Version 1)
        # Device Services Format: FORMAT_VCalendar1
        WPD_OBJECT_FORMAT_VCALENDAR1 = DEFINE_GUID(
            0xBE020000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_ICALENDAR
        # ICALENDAR file format (VCALENDAR Version 2)
        # Device Services Format: FORMAT_ICalendar
        WPD_OBJECT_FORMAT_ICALENDAR = DEFINE_GUID(
            0xBE030000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_ABSTRACT_CONTACT
        # Abstract contact file format
        # Device Services Format: FORMAT_AbstractContact
        WPD_OBJECT_FORMAT_ABSTRACT_CONTACT = DEFINE_GUID(
            0xBB810000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_VCARD2
        # VCARD file format (VCARD Version 2)
        # Device Services Format: FORMAT_VCard2Contact
        WPD_OBJECT_FORMAT_VCARD2 = DEFINE_GUID(
            0xBB820000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_VCARD3
        # VCARD file format (VCARD Version 3)
        # Device Services Format: FORMAT_VCard3Contact
        WPD_OBJECT_FORMAT_VCARD3 = DEFINE_GUID(
            0xBB830000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_XML
        # XML file format.
        # Device Services Format: FORMAT_XMLDocument
        WPD_OBJECT_FORMAT_XML = DEFINE_GUID(
            0xBA820000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_AAC
        # Audio file format
        # Device Services Format: FORMAT_AACFile
        WPD_OBJECT_FORMAT_AAC = DEFINE_GUID(
            0xB9030000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_AUDIBLE
        # Audio file format
        # Device Services Format: FORMAT_AudibleFile
        WPD_OBJECT_FORMAT_AUDIBLE = DEFINE_GUID(
            0xB9040000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_FLAC
        # Audio file format
        # Device Services Format: FORMAT_FLACFile
        WPD_OBJECT_FORMAT_FLAC = DEFINE_GUID(
            0xB9060000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_QCELP
        # Audio file format (Qualcomm Code Excited Linear Prediction)
        # Device Services Format: FORMAT_QCELPFile
        WPD_OBJECT_FORMAT_QCELP = DEFINE_GUID(
            0xB9070000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_AMR
        # Audio file format (Adaptive Multi-Rate audio codec)
        # Device Services Format: FORMAT_AMRFile
        WPD_OBJECT_FORMAT_AMR = DEFINE_GUID(
            0xB9080000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_OGG
        # Audio file format
        # Device Services Format: FORMAT_OGGFile
        WPD_OBJECT_FORMAT_OGG = DEFINE_GUID(
            0xB9020000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_MP4
        # Audio or Video file format
        # Device Services Format: FORMAT_MPEG4File
        WPD_OBJECT_FORMAT_MP4 = DEFINE_GUID(
            0xB9820000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_MP2
        # Audio or Video file format
        # Device Services Format: FORMAT_MPEG2File
        WPD_OBJECT_FORMAT_MP2 = DEFINE_GUID(
            0xB9830000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_MICROSOFT_WORD
        # Microsoft Office Word Document file format.
        # Device Services Format: FORMAT_WordDocument
        WPD_OBJECT_FORMAT_MICROSOFT_WORD = DEFINE_GUID(
            0xBA830000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_MHT_COMPILED_HTML
        # MHT Compiled HTML Document file format.
        # Device Services Format: FORMAT_MHTDocument
        WPD_OBJECT_FORMAT_MHT_COMPILED_HTML = DEFINE_GUID(
            0xBA840000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_MICROSOFT_EXCEL
        # Microsoft Office Excel Document file format.
        # Device Services Format: FORMAT_ExcelDocument
        WPD_OBJECT_FORMAT_MICROSOFT_EXCEL = DEFINE_GUID(
            0xBA850000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_MICROSOFT_POWERPOINT
        # Microsoft Office PowerPoint Document file format.
        # Device Services Format: FORMAT_PowerPointDocument
        WPD_OBJECT_FORMAT_MICROSOFT_POWERPOINT = DEFINE_GUID(
            0xBA860000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_3GP
        # Audio or Video file format
        # Device Services Format: FORMAT_3GPPFile
        WPD_OBJECT_FORMAT_3GP = DEFINE_GUID(
            0xB9840000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_3G2
        # Audio or Video file format
        # Device Services Format: FORMAT_3GPP2File
        WPD_OBJECT_FORMAT_3G2 = DEFINE_GUID(
            0xB9850000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_AVCHD
        # Audio or Video file format
        # Device Services Format: FORMAT_AVCHDFile
        WPD_OBJECT_FORMAT_AVCHD = DEFINE_GUID(
            0xB9860000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_ATSCTS
        # Audio or Video file format
        # Device Services Format: FORMAT_ATSCTSFile
        WPD_OBJECT_FORMAT_ATSCTS = DEFINE_GUID(
            0xB9870000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # WPD_OBJECT_FORMAT_DVBTS
        # Audio or Video file format
        # Device Services Format: FORMAT_DVBTSFile
        WPD_OBJECT_FORMAT_DVBTS = DEFINE_GUID(
            0xB9880000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )


        # WPD_OBJECT_FORMAT_MKV
        # Audio or Video file format
        # Device Services Format: FORMAT_MKVFile
        WPD_OBJECT_FORMAT_MKV = DEFINE_GUID(
            0xB9900000,
            0xAE6C,
            0x4804,
            0x98,
            0xBA,
            0xC5,
            0x7B,
            0x46,
            0x96,
            0x5F,
            0xE7
        )

        # ************************************************************************** This section defines the legacy WPD Properties *************************************************************************
        #
        # WPD_OBJECT_ID
        # [ VT_LPWSTR ] Uniquely identifies object on the Portable Device.
        # Recommended Device Services Property: PKEY_GenericObj_ObjectID
        WPD_OBJECT_ID = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x2
        )


        # WPD_OBJECT_PARENT_ID
        # [ VT_LPWSTR ] Object identifier indicating the parent object.
        # Recommended Device Services Property: PKEY_GenericObj_ParentID
        WPD_OBJECT_PARENT_ID = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x3
        )

        # WPD_OBJECT_NAME
        # [ VT_LPWSTR ] The display name for this object.
        # Recommended Device Services Property: PKEY_GenericObj_Name
        WPD_OBJECT_NAME = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x4
        )


        # WPD_OBJECT_PERSISTENT_UNIQUE_ID
        # [ VT_LPWSTR ] Uniquely identifies the object on the Portable Device,
        # similar to WPD_OBJECT_ID, but this ID will not change between
        # sessions.
        # Recommended Device Services Property: PKEY_GenericObj_PersistentUID
        WPD_OBJECT_PERSISTENT_UNIQUE_ID = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x5
        )

        # WPD_OBJECT_FORMAT
        # [ VT_CLSID ] Indicates the format of the object's data.
        # Recommended Device Services Property: PKEY_GenericObj_ObjectFormat
        WPD_OBJECT_FORMAT = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x6
        )


        # WPD_OBJECT_ISHIDDEN
        # [ VT_BOOL ] Indicates whether the object should be hidden.
        # Recommended Device Services Property: PKEY_GenericObj_Hidden
        WPD_OBJECT_ISHIDDEN = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x9
        )

        # WPD_OBJECT_ISSYSTEM
        # [ VT_BOOL ] Indicates whether the object represents system data.
        # Recommended Device Services Property: PKEY_GenericObj_SystemObject
        WPD_OBJECT_ISSYSTEM = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0xA
        )


        # WPD_OBJECT_SIZE
        # [ VT_UI8 ] The size of the object data.
        # Recommended Device Services Property: PKEY_GenericObj_ObjectSize
        WPD_OBJECT_SIZE = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0xB
        )

        # WPD_OBJECT_ORIGINAL_FILE_NAME
        # [ VT_LPWSTR ] Contains the name of the file this object represents.
        # Recommended Device Services Property: PKEY_GenericObj_ObjectFileName
        WPD_OBJECT_ORIGINAL_FILE_NAME = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0xC
        )


        # WPD_OBJECT_NON_CONSUMABLE
        # [ VT_BOOL ] This property determines whether or not this object is
        # intended to be understood by the device, or whether it has been
        # placed on the device just for storage.
        # Recommended Device Services Property: PKEY_GenericObj_NonConsumable
        WPD_OBJECT_NON_CONSUMABLE = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0xD
        )

        # WPD_OBJECT_KEYWORDS
        # [ VT_LPWSTR ] String containing a list of keywords associated with
        # this object.
        # Recommended Device Services Property: PKEY_GenericObj_Keywords
        WPD_OBJECT_KEYWORDS = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0xF
        )


        # WPD_OBJECT_SYNC_ID
        # [ VT_LPWSTR ] Opaque string set by client to retain state between
        # sessions without retaining a catalogue of connected device content.
        # Recommended Device Services Property: PKEY_GenericObj_SyncID
        WPD_OBJECT_SYNC_ID = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x10
        )

        # WPD_OBJECT_IS_DRM_PROTECTED
        # [ VT_BOOL ] Indicates whether the media data is DRM protected.
        # Recommended Device Services Property: PKEY_GenericObj_DRMStatus
        WPD_OBJECT_IS_DRM_PROTECTED = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x11
        )


        # WPD_OBJECT_DATE_CREATED
        # [ VT_DATE ] Indicates the date and time the object was created on
        # the device.
        # Recommended Device Services Property: PKEY_GenericObj_DateCreated
        WPD_OBJECT_DATE_CREATED = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x12
        )

        # WPD_OBJECT_DATE_MODIFIED
        # [ VT_DATE ] Indicates the date and time the object was modified on
        # the device.
        # Recommended Device Services Property: PKEY_GenericObj_DateModified
        WPD_OBJECT_DATE_MODIFIED = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x13
        )


        # WPD_OBJECT_DATE_AUTHORED
        # [ VT_DATE ] Indicates the date and time the object was authored
        # (e.g. for music, this would be the date the music was recorded).
        # Recommended Device Services Property: PKEY_GenericObj_DateAuthored
        WPD_OBJECT_DATE_AUTHORED = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x14
        )

        # WPD_OBJECT_BACK_REFERENCES
        # [ VT_UNKNOWN ] IPortableDevicePropVariantCollection of type
        # VT_LPWSTR indicating a list of ObjectIDs.
        # Recommended Device Services Property:
        # PKEY_GenericObj_ReferenceParentID
        WPD_OBJECT_BACK_REFERENCES = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x15
        )


        # WPD_OBJECT_CAN_DELETE
        # [ VT_BOOL ] Indicates whether the object can be deleted, or not.
        # Recommended Device Services Property:
        # PKEY_GenericObj_ProtectionStatus
        WPD_OBJECT_CAN_DELETE = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x1A
        )

        # WPD_OBJECT_LANGUAGE_LOCALE
        # [ VT_LPWSTR ] Identifies the language of this object. If multiple
        # languages are contained in this object, it should identify the
        # primary language (if any).
        # Recommended Device Services Property: PKEY_GenericObj_LanguageLocale
        WPD_OBJECT_LANGUAGE_LOCALE = DEFINE_PROPERTYKEY(
            0xEF6B490D,
            0x5CD8,
            0x437A,
            0xAF,
            0xFC,
            0xDA,
            0x8B,
            0x60,
            0xEE,
            0x4A,
            0x3C,
            0x1B
        )

        # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_FOLDER_OBJECT_PROPERTIES_V1 This category is for properties common to all folder objects. *************************************************************************
        #
        WPD_FOLDER_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0x7E9A7ABF,
            0xE568,
            0x4B34,
            0xAA,
            0x2F,
            0x13,
            0xBB,
            0x12,
            0xAB,
            0x17,
            0x7D
        )


        # WPD_FOLDER_CONTENT_TYPES_ALLOWED
        # [ VT_UNKNOWN ] Indicates the subset of content types that can be
        # created in this folder directly
        # (i.e. children may have different restrictions).
        # Recommended Device Services Property: None
        WPD_FOLDER_CONTENT_TYPES_ALLOWED = DEFINE_PROPERTYKEY(
            0x7E9A7ABF,
            0xE568,
            0x4B34,
            0xAA,
            0x2F,
            0x13,
            0xBB,
            0x12,
            0xAB,
            0x17,
            0x7D,
            0x2
        )

        # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_IMAGE_OBJECT_PROPERTIES_V1 This category is for properties common to all image objects. *************************************************************************
        #
        WPD_IMAGE_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0x63D64908,
            0x9FA1,
            0x479F,
            0x85,
            0xBA,
            0x99,
            0x52,
            0x21,
            0x64,
            0x47,
            0xDB
        )

        # WPD_IMAGE_BITDEPTH
        # [ VT_UI4 ] Indicates the bitdepth of an image
        # Recommended Device Services Property: PKEY_ImageObj_ImageBitDepth
        WPD_IMAGE_BITDEPTH = DEFINE_PROPERTYKEY(
            0x63D64908,
            0x9FA1,
            0x479F,
            0x85,
            0xBA,
            0x99,
            0x52,
            0x21,
            0x64,
            0x47,
            0xDB,
            0x3
        )


        # WPD_IMAGE_CROPPED_STATUS
        # [ VT_UI4 ] Signals whether the file has been cropped.
        # Recommended Device Services Property: PKEY_ImageObj_IsCropped
        WPD_IMAGE_CROPPED_STATUS = DEFINE_PROPERTYKEY(
            0x63D64908,
            0x9FA1,
            0x479F,
            0x85,
            0xBA,
            0x99,
            0x52,
            0x21,
            0x64,
            0x47,
            0xDB,
            0x4
        )

        # WPD_IMAGE_COLOR_CORRECTED_STATUS
        # [ VT_UI4 ] Signals whether the file has been color corrected.
        # Recommended Device Services Property: PKEY_ImageObj_IsColorCorrected
        WPD_IMAGE_COLOR_CORRECTED_STATUS = DEFINE_PROPERTYKEY(
            0x63D64908,
            0x9FA1,
            0x479F,
            0x85,
            0xBA,
            0x99,
            0x52,
            0x21,
            0x64,
            0x47,
            0xDB,
            0x5
        )


        # WPD_IMAGE_FNUMBER
        # [ VT_UI4 ] Identifies the aperture setting of the lens when this
        # image was captured.
        # Recommended Device Services Property: PKEY_ImageObj_Aperature
        WPD_IMAGE_FNUMBER = DEFINE_PROPERTYKEY(
            0x63D64908,
            0x9FA1,
            0x479F,
            0x85,
            0xBA,
            0x99,
            0x52,
            0x21,
            0x64,
            0x47,
            0xDB,
            0x6
        )

        # WPD_IMAGE_EXPOSURE_TIME
        # [ VT_UI4 ] Identifies the shutter speed of the device when this
        # image was captured.
        # Recommended Device Services Property: PKEY_ImageObj_Exposure
        WPD_IMAGE_EXPOSURE_TIME = DEFINE_PROPERTYKEY(
            0x63D64908,
            0x9FA1,
            0x479F,
            0x85,
            0xBA,
            0x99,
            0x52,
            0x21,
            0x64,
            0x47,
            0xDB,
            0x7
        )


        # WPD_IMAGE_EXPOSURE_INDEX
        # [ VT_UI4 ] Identifies the emulation of film speed settings when this
        # image was captured.
        # Recommended Device Services Property: PKEY_ImageObj_ISOSpeed
        WPD_IMAGE_EXPOSURE_INDEX = DEFINE_PROPERTYKEY(
            0x63D64908,
            0x9FA1,
            0x479F,
            0x85,
            0xBA,
            0x99,
            0x52,
            0x21,
            0x64,
            0x47,
            0xDB,
            0x8
        )

        # WPD_IMAGE_HORIZONTAL_RESOLUTION
        # [ VT_R8 ] Indicates the horizontal resolution (DPI) of an image
        # Recommended Device Services Property: None
        WPD_IMAGE_HORIZONTAL_RESOLUTION = DEFINE_PROPERTYKEY(
            0x63D64908,
            0x9FA1,
            0x479F,
            0x85,
            0xBA,
            0x99,
            0x52,
            0x21,
            0x64,
            0x47,
            0xDB,
            0x9
        )


        # WPD_IMAGE_VERTICAL_RESOLUTION
        # [ VT_R8 ] Indicates the vertical resolution (DPI) of an image
        # Recommended Device Services Property: None
        WPD_IMAGE_VERTICAL_RESOLUTION = DEFINE_PROPERTYKEY(
            0x63D64908,
            0x9FA1,
            0x479F,
            0x85,
            0xBA,
            0x99,
            0x52,
            0x21,
            0x64,
            0x47,
            0xDB,
            0xA
        )

        # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_DOCUMENT_OBJECT_PROPERTIES_V1 This category is for properties common to all document objects. *************************************************************************
        #
        WPD_DOCUMENT_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0x0B110203,
            0xEB95,
            0x4F02,
            0x93,
            0xE0,
            0x97,
            0xC6,
            0x31,
            0x49,
            0x3A,
            0xD5
        )

        # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_MEDIA_PROPERTIES_V1 This category is for properties common to media objects (e.g. audio and video). *************************************************************************
        #
        WPD_MEDIA_PROPERTIES_V1 = DEFINE_GUID(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8
        )

        # WPD_MEDIA_TOTAL_BITRATE
        # [ VT_UI4 ] The total number of bits that one second will consume.
        # Recommended Device Services Property: PKEY_MediaObj_TotalBitRate
        WPD_MEDIA_TOTAL_BITRATE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x2
        )


        # WPD_MEDIA_BITRATE_TYPE
        # [ VT_UI4 ] Further qualifies the bitrate of audio or video data.
        # Recommended Device Services Property: PKEY_MediaObj_BitRateType
        WPD_MEDIA_BITRATE_TYPE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x3
        )

        # WPD_MEDIA_COPYRIGHT
        # [ VT_LPWSTR ] Indicates the copyright information.
        # Recommended Device Services Property: PKEY_GenericObj_Copyright
        WPD_MEDIA_COPYRIGHT = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x4
        )


        # WPD_MEDIA_SUBSCRIPTION_CONTENT_ID
        # [ VT_LPWSTR ] Provides additional information to identify a piece of
        # content relative to an online subscription service.
        # Recommended Device Services Property:
        # PKEY_MediaObj_SubscriptionContentID
        WPD_MEDIA_SUBSCRIPTION_CONTENT_ID = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x5
        )

        # WPD_MEDIA_USE_COUNT
        # [ VT_UI4 ] Indicates the total number of times this media has been
        # played or viewed on the device.
        # Recommended Device Services Property: PKEY_MediaObj_UseCount
        WPD_MEDIA_USE_COUNT = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x6
        )


        # WPD_MEDIA_SKIP_COUNT
        # [ VT_UI4 ] Indicates the total number of times this media was setup
        # to be played or viewed but was manually skipped by the user.
        # Recommended Device Services Property: PKEY_MediaObj_SkipCount
        WPD_MEDIA_SKIP_COUNT = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x7
        )

        # WPD_MEDIA_LAST_ACCESSED_TIME
        # [ VT_DATE ] Indicates the date and time the media was last accessed
        # on the device.
        # Recommended Device Services Property: PKEY_GenericObj_DateAccessed
        WPD_MEDIA_LAST_ACCESSED_TIME = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x8
        )


        # WPD_MEDIA_PARENTAL_RATING
        # [ VT_LPWSTR ] Indicates the parental rating of the media file.
        # Recommended Device Services Property: PKEY_MediaObj_ParentalRating
        WPD_MEDIA_PARENTAL_RATING = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x9
        )

        # WPD_MEDIA_META_GENRE
        # [ VT_UI4 ] Further qualifies a piece of media in a contextual way.
        # Recommended Device Services Property: PKEY_MediaObj_MediaType
        WPD_MEDIA_META_GENRE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0xA
        )


        # WPD_MEDIA_COMPOSER
        # [ VT_LPWSTR ] Identifies the composer when the composer is not the
        # artist who performed it.
        # Recommended Device Services Property: PKEY_MediaObj_Composer
        WPD_MEDIA_COMPOSER = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0xB
        )

        # WPD_MEDIA_EFFECTIVE_RATING
        # [ VT_UI4 ] Contains an assigned rating for media not set by the
        # user, but is generated based upon usage statistics.
        # Recommended Device Services Property: PKEY_MediaObj_EffectiveRating
        WPD_MEDIA_EFFECTIVE_RATING = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0xC
        )


        # WPD_MEDIA_SUB_TITLE
        # [ VT_LPWSTR ] Further qualifies the title when the title is
        # ambiguous or general.
        # Recommended Device Services Property: PKEY_MediaObj_Subtitle
        WPD_MEDIA_SUB_TITLE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0xD
        )

        # WPD_MEDIA_RELEASE_DATE
        # [ VT_DATE ] Indicates when the media was released.
        # Recommended Device Services Property:
        # PKEY_MediaObj_DateOriginalRelease
        WPD_MEDIA_RELEASE_DATE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0xE
        )


        # WPD_MEDIA_SAMPLE_RATE
        # [ VT_UI4 ] Indicates the number of times media selection was sampled
        # per second during encoding.
        # Recommended Device Services Property: PKEY_MediaObj_SampleRate
        WPD_MEDIA_SAMPLE_RATE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0xF
        )

        # WPD_MEDIA_STAR_RATING
        # [ VT_UI4 ] Indicates the star rating for this media.
        # Recommended Device Services Property: None
        WPD_MEDIA_STAR_RATING = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x10
        )


        # WPD_MEDIA_USER_EFFECTIVE_RATING
        # [ VT_UI4 ] Indicates the rating for this media.
        # Recommended Device Services Property: PKEY_MediaObj_UserRating
        WPD_MEDIA_USER_EFFECTIVE_RATING = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x11
        )

        # WPD_MEDIA_TITLE
        # [ VT_LPWSTR ] Indicates the title of this media.
        # Recommended Device Services Property: None
        WPD_MEDIA_TITLE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x12
        )


        # WPD_MEDIA_DURATION
        # [ VT_UI8 ] Indicates the duration of this media in milliseconds.
        # Recommended Device Services Property: PKEY_MediaObj_Duration
        WPD_MEDIA_DURATION = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x13
        )

        # WPD_MEDIA_BUY_NOW
        # [ VT_BOOL ] TBD
        # Recommended Device Services Property: None
        WPD_MEDIA_BUY_NOW = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x14
        )


        # WPD_MEDIA_ENCODING_PROFILE
        # [ VT_LPWSTR ] Media codecs may be encoded in accordance with a
        # profile, which defines a particular encoding algorithm or
        # optimization process.
        # Recommended Device Services Property: PKEY_MediaObj_EncodingProfile
        WPD_MEDIA_ENCODING_PROFILE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x15
        )

        # WPD_MEDIA_WIDTH
        # [ VT_UI4 ] Indicates the width of an object in pixels
        # Recommended Device Services Property: PKEY_MediaObj_Width
        WPD_MEDIA_WIDTH = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x16
        )


        # WPD_MEDIA_HEIGHT
        # [ VT_UI4 ] Indicates the height of an object in pixels
        # Recommended Device Services Property: PKEY_MediaObj_Height
        WPD_MEDIA_HEIGHT = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x17
        )

        # WPD_MEDIA_ARTIST
        # [ VT_LPWSTR ] Indicates the artist for this media.
        # Recommended Device Services Property: PKEY_MediaObj_Artist
        WPD_MEDIA_ARTIST = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x18
        )


        # WPD_MEDIA_ALBUM_ARTIST
        # [ VT_LPWSTR ] Indicates the artist of the entire album rather than
        # for a particular track.
        # Recommended Device Services Property: PKEY_MediaObj_AlbumArtist
        WPD_MEDIA_ALBUM_ARTIST = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x19
        )

        # WPD_MEDIA_OWNER
        # [ VT_LPWSTR ] Indicates the e-mail address of the owner for this
        # media.
        # Recommended Device Services Property: PKEY_MediaObj_Owner
        WPD_MEDIA_OWNER = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x1A
        )


        # WPD_MEDIA_MANAGING_EDITOR
        # [ VT_LPWSTR ] Indicates the e-mail address of the managing editor
        # for this media.
        # Recommended Device Services Property: PKEY_MediaObj_Editor
        WPD_MEDIA_MANAGING_EDITOR = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x1B
        )

        # WPD_MEDIA_WEBMASTER
        # [ VT_LPWSTR ] Indicates the e-mail address of the Webmaster for this
        # media.
        # Recommended Device Services Property: PKEY_MediaObj_WebMaster
        WPD_MEDIA_WEBMASTER = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x1C
        )


        # WPD_MEDIA_SOURCE_URL
        # [ VT_LPWSTR ] Identifies the source URL for this object.
        # Recommended Device Services Property: PKEY_MediaObj_URLSource
        WPD_MEDIA_SOURCE_URL = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x1D
        )

        # WPD_MEDIA_DESTINATION_URL
        # [ VT_LPWSTR ] Identifies the URL that an object is linked to if a
        # user clicks on it.
        # Recommended Device Services Property: PKEY_MediaObj_URLLink
        WPD_MEDIA_DESTINATION_URL = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x1E
        )


        # WPD_MEDIA_DESCRIPTION
        # [ VT_LPWSTR ] Contains a description of the media content for this
        # object.
        # Recommended Device Services Property: PKEY_GenericObj_Description
        WPD_MEDIA_DESCRIPTION = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x1F
        )

        # WPD_MEDIA_GENRE
        # [ VT_LPWSTR ] A text field indicating the genre this media belongs
        # to.
        # Recommended Device Services Property: PKEY_MediaObj_Genre
        WPD_MEDIA_GENRE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x20
        )


        # WPD_MEDIA_TIME_BOOKMARK
        # [ VT_UI8 ] Indicates a bookmark (in milliseconds) of the last
        # position played or viewed on media that have duration.
        # Recommended Device Services Property: PKEY_MediaObj_BookmarkTime
        WPD_MEDIA_TIME_BOOKMARK = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x21
        )

        # WPD_MEDIA_OBJECT_BOOKMARK
        # [ VT_LPWSTR ] Indicates a WPD_OBJECT_ID of the last object viewed or
        # played for those objects that refer to a list of objects
        # (such as playlists or media casts).
        # Recommended Device Services Property: PKEY_MediaObj_BookmarkObject
        WPD_MEDIA_OBJECT_BOOKMARK = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x22
        )


        # WPD_MEDIA_LAST_BUILD_DATE
        # [ VT_DATE ] Indicates the last time a series in a media cast was
        # changed or edited.
        # Recommended Device Services Property: PKEY_GenericObj_DateRevised
        WPD_MEDIA_LAST_BUILD_DATE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x23
        )

        # WPD_MEDIA_BYTE_BOOKMARK
        # [ VT_UI8 ] Indicates a bookmark (as a zero-based byte offset) of the
        # last position played or viewed on this media object.
        # Recommended Device Services Property: PKEY_MediaObj_BookmarkByte
        WPD_MEDIA_BYTE_BOOKMARK = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x24
        )


        # WPD_MEDIA_TIME_TO_LIVE
        # [ VT_UI8 ] It is the number of minutes that indicates how LONG a
        # channel can be cached before refreshing from the source. Applies to
        # WPD_CONTENT_TYPE_MEDIA_CAST objects.
        # Recommended Device Services Property: PKEY_GenericObj_TimeToLive
        WPD_MEDIA_TIME_TO_LIVE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x25
        )

        # WPD_MEDIA_GUID
        # [ VT_LPWSTR ] A text field indicating the GUID of this media.
        # Recommended Device Services Property: PKEY_MediaObj_MediaUID
        WPD_MEDIA_GUID = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x26
        )


        # WPD_MEDIA_SUB_DESCRIPTION
        # [ VT_LPWSTR ] Contains a sub description of the media content for
        # this object.
        # Recommended Device Services Property: PKEY_GenericObj_SubDescription
        WPD_MEDIA_SUB_DESCRIPTION = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x27
        )

        # WPD_MEDIA_AUDIO_ENCODING_PROFILE
        # [ VT_LPWSTR ] Media codecs may be encoded in accordance with a
        # profile, which defines a particular encoding algorithm or
        # optimization process.
        # Recommended Device Services Property:
        # PKEY_MediaObj_AudioEncodingProfile
        WPD_MEDIA_AUDIO_ENCODING_PROFILE = DEFINE_PROPERTYKEY(
            0x2ED8BA05,
            0x0AD3,
            0x42DC,
            0xB0,
            0xD0,
            0xBC,
            0x95,
            0xAC,
            0x39,
            0x6A,
            0xC8,
            0x31
        )

        # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_CONTACT_OBJECT_PROPERTIES_V1 This category is for properties common to all contact objects. *************************************************************************
        #
        WPD_CONTACT_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B
        )


        # WPD_CONTACT_DISPLAY_NAME
        # [ VT_LPWSTR ] Indicates the display name of the contact
        # (e.g "John Doe")
        # Recommended Device Services Property: None
        WPD_CONTACT_DISPLAY_NAME = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x2
        )

        # WPD_CONTACT_FIRST_NAME
        # [ VT_LPWSTR ] Indicates the first name of the contact (e.g. "John")
        # Recommended Device Services Property: PKEY_ContactObj_GivenName
        WPD_CONTACT_FIRST_NAME = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x3
        )


        # WPD_CONTACT_MIDDLE_NAMES
        # [ VT_LPWSTR ] Indicates the middle name of the contact
        # Recommended Device Services Property: PKEY_ContactObj_MiddleNames
        WPD_CONTACT_MIDDLE_NAMES = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x4
        )

        # WPD_CONTACT_LAST_NAME
        # [ VT_LPWSTR ] Indicates the last name of the contact (e.g. "Doe")
        # Recommended Device Services Property: PKEY_ContactObj_FamilyName
        WPD_CONTACT_LAST_NAME = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x5
        )


        # WPD_CONTACT_PREFIX
        # [ VT_LPWSTR ] Indicates the prefix of the name of the contact
        # (e.g. "Mr.")
        # Recommended Device Services Property: PKEY_ContactObj_Title
        WPD_CONTACT_PREFIX = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x6
        )

        # WPD_CONTACT_SUFFIX
        # [ VT_LPWSTR ] Indicates the suffix of the name of the contact
        # (e.g. "Jr.")
        # Recommended Device Services Property: PKEY_ContactObj_Suffix
        WPD_CONTACT_SUFFIX = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x7
        )


        # WPD_CONTACT_PHONETIC_FIRST_NAME
        # [ VT_LPWSTR ] The phonetic guide for pronouncing the contact's first
        # name.
        # Recommended Device Services Property:
        # PKEY_ContactObj_PhoneticGivenName
        WPD_CONTACT_PHONETIC_FIRST_NAME = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x8
        )

        # WPD_CONTACT_PHONETIC_LAST_NAME
        # [ VT_LPWSTR ] The phonetic guide for pronouncing the contact's last
        # name.
        # Recommended Device Services Property:
        # PKEY_ContactObj_PhoneticFamilyName
        WPD_CONTACT_PHONETIC_LAST_NAME = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x9
        )


        # WPD_CONTACT_PERSONAL_FULL_POSTAL_ADDRESS
        # [ VT_LPWSTR ] Indicates the full postal address of the contact
        # (e.g. "555 Dial Drive, PhoneLand, WA 12345")
        # Recommended Device Services Property:
        # PKEY_ContactObj_PersonalAddressFull
        WPD_CONTACT_PERSONAL_FULL_POSTAL_ADDRESS = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0xA
        )

        # WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE1
        # [ VT_LPWSTR ] Indicates the first line of a postal address of the
        # contact (e.g. "555 Dial Drive")
        # Recommended Device Services Property:
        # PKEY_ContactObj_PersonalAddressStreet
        WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE1 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0xB
        )


        # WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE2
        # [ VT_LPWSTR ] Indicates the second line of a postal address of the
        # contact
        # Recommended Device Services Property:
        # PKEY_ContactObj_PersonalAddressLine2
        WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_LINE2 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0xC
        )

        # WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_CITY
        # [ VT_LPWSTR ] Indicates the city of a postal address of the contact
        # (e.g. "PhoneLand")
        # Recommended Device Services Property:
        # PKEY_ContactObj_PersonalAddressCity
        WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_CITY = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0xD
        )


        # WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_REGION
        # [ VT_LPWSTR ] Indicates the region of a postal address of the contact
        # Recommended Device Services Property:
        # PKEY_ContactObj_PersonalAddressRegion
        WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_REGION = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0xE
        )

        # WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_POSTAL_CODE
        # [ VT_LPWSTR ] Indicates the postal code of the address.
        # Recommended Device Services Property:
        # PKEY_ContactObj_PersonalAddressPostalCode
        WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_POSTAL_CODE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0xF
        )


        # WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_COUNTRY
        # [ VT_LPWSTR ]
        # Recommended Device Services Property:
        # PKEY_ContactObj_PersonalAddressCountry
        WPD_CONTACT_PERSONAL_POSTAL_ADDRESS_COUNTRY = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x10
        )

        # WPD_CONTACT_BUSINESS_FULL_POSTAL_ADDRESS
        # [ VT_LPWSTR ] Indicates the full postal address of the contact
        # (e.g. "555 Dial Drive, PhoneLand, WA 12345")
        # Recommended Device Services Property:
        # PKEY_ContactObj_BusinessAddressFull
        WPD_CONTACT_BUSINESS_FULL_POSTAL_ADDRESS = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x11
        )


        # WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE1
        # [ VT_LPWSTR ] Indicates the first line of a postal address of the
        # contact (e.g. "555 Dial Drive")
        # Recommended Device Services Property:
        # PKEY_ContactObj_BusinessAddressStreet
        WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE1 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x12
        )

        # WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE2
        # [ VT_LPWSTR ] Indicates the second line of a postal address of the
        # contact
        # Recommended Device Services Property:
        # PKEY_ContactObj_BusinessAddressLine2
        WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_LINE2 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x13
        )


        # WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_CITY
        # [ VT_LPWSTR ] Indicates the city of a postal address of the contact
        # (e.g. "PhoneLand")
        # Recommended Device Services Property:
        # PKEY_ContactObj_BusinessAddressCity
        WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_CITY = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x14
        )

        # WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_REGION
        # [ VT_LPWSTR ]
        # Recommended Device Services Property:
        # PKEY_ContactObj_BusinessAddressRegion
        WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_REGION = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x15
        )


        # WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_POSTAL_CODE
        # [ VT_LPWSTR ] Indicates the postal code of the address.
        # Recommended Device Services Property:
        # PKEY_ContactObj_BusinessAddressPostalCode
        WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_POSTAL_CODE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x16
        )

        # WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_COUNTRY
        # [ VT_LPWSTR ]
        # Recommended Device Services Property:
        # PKEY_ContactObj_BusinessAddressCountry
        WPD_CONTACT_BUSINESS_POSTAL_ADDRESS_COUNTRY = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x17
        )


        # WPD_CONTACT_OTHER_FULL_POSTAL_ADDRESS
        # [ VT_LPWSTR ] Indicates the full postal address of the contact
        # (e.g. "555 Dial Drive, PhoneLand, WA 12345").
        # Recommended Device Services Property:
        # PKEY_ContactObj_OtherAddressFull
        WPD_CONTACT_OTHER_FULL_POSTAL_ADDRESS = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x18
        )

        # WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE1
        # [ VT_LPWSTR ] Indicates the first line of a postal address of the
        # contact (e.g. "555 Dial Drive").
        # Recommended Device Services Property:
        # PKEY_ContactObj_OtherAddressStreet
        WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE1 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x19
        )


        # WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE2
        # [ VT_LPWSTR ] Indicates the second line of a postal address of the
        # contact.
        # Recommended Device Services Property:
        # PKEY_ContactObj_OtherAddressLine2
        WPD_CONTACT_OTHER_POSTAL_ADDRESS_LINE2 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x1A
        )

        # WPD_CONTACT_OTHER_POSTAL_ADDRESS_CITY
        # [ VT_LPWSTR ] Indicates the city of a postal address of the contact
        # (e.g. "PhoneLand").
        # Recommended Device Services Property:
        # PKEY_ContactObj_OtherAddressCity
        WPD_CONTACT_OTHER_POSTAL_ADDRESS_CITY = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x1B
        )


        # WPD_CONTACT_OTHER_POSTAL_ADDRESS_REGION
        # [ VT_LPWSTR ] Indicates the region of a postal address of the
        # contact.
        # Recommended Device Services Property:
        # PKEY_ContactObj_OtherAddressRegion
        WPD_CONTACT_OTHER_POSTAL_ADDRESS_REGION = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x1C
        )

        # WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_CODE
        # [ VT_LPWSTR ] Indicates the postal code of the address.
        # Recommended Device Services Property:
        # PKEY_ContactObj_OtherAddressPostalCode
        WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_CODE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x1D
        )


        # WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_COUNTRY
        # [ VT_LPWSTR ] Indicates the country/region of the postal address.
        # Recommended Device Services Property:
        # PKEY_ContactObj_OtherAddressCountry
        WPD_CONTACT_OTHER_POSTAL_ADDRESS_POSTAL_COUNTRY = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x1E
        )

        # WPD_CONTACT_PRIMARY_EMAIL_ADDRESS
        # [ VT_LPWSTR ] Indicates the primary email address for the contact
        # e.g. "someone@example.com"
        # Recommended Device Services Property: PKEY_ContactObj_Email
        WPD_CONTACT_PRIMARY_EMAIL_ADDRESS = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x1F
        )


        # WPD_CONTACT_PERSONAL_EMAIL
        # [ VT_LPWSTR ] Indicates the personal email address for the contact
        # e.g. "someone@example.com"
        # Recommended Device Services Property: PKEY_ContactObj_PersonalEmail
        WPD_CONTACT_PERSONAL_EMAIL = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x20
        )

        # WPD_CONTACT_PERSONAL_EMAIL2
        # [ VT_LPWSTR ] Indicates an alternate personal email address for the
        # contact e.g. "someone@example.com"
        # Recommended Device Services Property: PKEY_ContactObj_PersonalEmail2
        WPD_CONTACT_PERSONAL_EMAIL2 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x21
        )


        # WPD_CONTACT_BUSINESS_EMAIL
        # [ VT_LPWSTR ] Indicates the business email address for the contact
        # e.g. "someone@example.com"
        # Recommended Device Services Property: PKEY_ContactObj_BusinessEmail
        WPD_CONTACT_BUSINESS_EMAIL = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x22
        )

        # WPD_CONTACT_BUSINESS_EMAIL2
        # [ VT_LPWSTR ] Indicates an alternate business email address for the
        # contact e.g. "someone@example.com"
        # Recommended Device Services Property: PKEY_ContactObj_BusinessEmail2
        WPD_CONTACT_BUSINESS_EMAIL2 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x23
        )


        # WPD_CONTACT_OTHER_EMAILS
        # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of type
        # VT_LPWSTR, where each element is an alternate email addresses for
        # the contact.
        # Recommended Device Services Property: PKEY_ContactObj_OtherEmail
        WPD_CONTACT_OTHER_EMAILS = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x24
        )

        # WPD_CONTACT_PRIMARY_PHONE
        # [ VT_LPWSTR ] Indicates the primary phone number for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_Phone
        WPD_CONTACT_PRIMARY_PHONE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x25
        )


        # WPD_CONTACT_PERSONAL_PHONE
        # [ VT_LPWSTR ] Indicates the personal phone number for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_PersonalPhone
        WPD_CONTACT_PERSONAL_PHONE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x26
        )

        # WPD_CONTACT_PERSONAL_PHONE2
        # [ VT_LPWSTR ] Indicates an alternate personal phone number for the
        # contact.
        # Recommended Device Services Property: PKEY_ContactObj_PersonalPhone2
        WPD_CONTACT_PERSONAL_PHONE2 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x27
        )


        # WPD_CONTACT_BUSINESS_PHONE
        # [ VT_LPWSTR ] Indicates the business phone number for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_BusinessPhone
        WPD_CONTACT_BUSINESS_PHONE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x28
        )

        # WPD_CONTACT_BUSINESS_PHONE2
        # [ VT_LPWSTR ] Indicates an alternate business phone number for the
        # contact.
        # Recommended Device Services Property: PKEY_ContactObj_BusinessPhone2
        WPD_CONTACT_BUSINESS_PHONE2 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x29
        )


        # WPD_CONTACT_MOBILE_PHONE
        # [ VT_LPWSTR ] Indicates the mobile phone number for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_MobilePhone
        WPD_CONTACT_MOBILE_PHONE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x2A
        )

        # WPD_CONTACT_MOBILE_PHONE2
        # [ VT_LPWSTR ] Indicates an alternate mobile phone number for the
        # contact.
        # Recommended Device Services Property: PKEY_ContactObj_MobilePhone2
        WPD_CONTACT_MOBILE_PHONE2 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x2B
        )


        # WPD_CONTACT_PERSONAL_FAX
        # [ VT_LPWSTR ] Indicates the personal fax number for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_PersonalFax
        WPD_CONTACT_PERSONAL_FAX = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x2C
        )

        # WPD_CONTACT_BUSINESS_FAX
        # [ VT_LPWSTR ] Indicates the business fax number for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_BusinessFax
        WPD_CONTACT_BUSINESS_FAX = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x2D
        )


        # WPD_CONTACT_PAGER
        # [ VT_LPWSTR ]
        # Recommended Device Services Property: PKEY_ContactObj_Pager
        WPD_CONTACT_PAGER = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x2E
        )

        # WPD_CONTACT_OTHER_PHONES
        # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of type
        # VT_LPWSTR, where each element is an alternate phone number for the
        # contact.
        # Recommended Device Services Property: PKEY_ContactObj_OtherPhone
        WPD_CONTACT_OTHER_PHONES = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x2F
        )


        # WPD_CONTACT_PRIMARY_WEB_ADDRESS
        # [ VT_LPWSTR ] Indicates the primary web address for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_WebAddress
        WPD_CONTACT_PRIMARY_WEB_ADDRESS = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x30
        )

        # WPD_CONTACT_PERSONAL_WEB_ADDRESS
        # [ VT_LPWSTR ] Indicates the personal web address for the contact.
        # Recommended Device Services Property:
        # PKEY_ContactObj_PersonalWebAddress
        WPD_CONTACT_PERSONAL_WEB_ADDRESS = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x31
        )


        # WPD_CONTACT_BUSINESS_WEB_ADDRESS
        # [ VT_LPWSTR ] Indicates the business web address for the contact.
        # Recommended Device Services Property:
        # PKEY_ContactObj_BusinessWebAddress
        WPD_CONTACT_BUSINESS_WEB_ADDRESS = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x32
        )

        # WPD_CONTACT_INSTANT_MESSENGER
        # [ VT_LPWSTR ] Indicates the instant messenger address for the
        # contact.
        # Recommended Device Services Property: PKEY_ContactObj_IMAddress
        WPD_CONTACT_INSTANT_MESSENGER = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x33
        )


        # WPD_CONTACT_INSTANT_MESSENGER2
        # [ VT_LPWSTR ] Indicates an alternate instant messenger address for
        # the contact.
        # Recommended Device Services Property: PKEY_ContactObj_IMAddress2
        WPD_CONTACT_INSTANT_MESSENGER2 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x34
        )

        # WPD_CONTACT_INSTANT_MESSENGER3
        # [ VT_LPWSTR ] Indicates an alternate instant messenger address for
        # the contact.
        # Recommended Device Services Property: PKEY_ContactObj_IMAddress3
        WPD_CONTACT_INSTANT_MESSENGER3 = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x35
        )


        # WPD_CONTACT_COMPANY_NAME
        # [ VT_LPWSTR ] Indicates the company name for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_Organization
        WPD_CONTACT_COMPANY_NAME = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x36
        )

        # WPD_CONTACT_PHONETIC_COMPANY_NAME
        # [ VT_LPWSTR ] The phonetic guide for pronouncing the contact's
        # company name.
        # Recommended Device Services Property:
        # PKEY_ContactObj_PhoneticOrganization
        WPD_CONTACT_PHONETIC_COMPANY_NAME = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x37
        )


        # WPD_CONTACT_ROLE
        # [ VT_LPWSTR ] Indicates the role for the contact e.g.
        # "Software Engineer".
        # Recommended Device Services Property: PKEY_ContactObj_Role
        WPD_CONTACT_ROLE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x38
        )

        # WPD_CONTACT_BIRTHDATE
        # [ VT_DATE ] Indicates the birthdate for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_Birthdate
        WPD_CONTACT_BIRTHDATE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x39
        )


        # WPD_CONTACT_PRIMARY_FAX
        # [ VT_LPWSTR ] Indicates the primary fax number for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_Fax
        WPD_CONTACT_PRIMARY_FAX = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x3A
        )

        # WPD_CONTACT_SPOUSE
        # [ VT_LPWSTR ] Indicates the full name of the spouse/domestic partner
        # for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_Spouse
        WPD_CONTACT_SPOUSE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x3B
        )


        # WPD_CONTACT_CHILDREN
        # [ VT_UNKNOWN ] An IPortableDevicePropVariantCollection of type
        # VT_LPWSTR, where each element is the full name of a child of the
        # contact.
        # Recommended Device Services Property: PKEY_ContactObj_Children
        WPD_CONTACT_CHILDREN = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x3C
        )

        # WPD_CONTACT_ASSISTANT
        # [ VT_LPWSTR ] Indicates the full name of the assistant for the
        # contact.
        # Recommended Device Services Property: PKEY_ContactObj_Assistant
        WPD_CONTACT_ASSISTANT = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x3D
        )


        # WPD_CONTACT_ANNIVERSARY_DATE
        # [ VT_DATE ] Indicates the anniversary date for the contact.
        # Recommended Device Services Property: PKEY_ContactObj_AnniversaryDate
        WPD_CONTACT_ANNIVERSARY_DATE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x3E
        )

        # WPD_CONTACT_RINGTONE
        # [ VT_LPWSTR ] Indicates an object id of a ringtone file on the
        # device.
        # Recommended Device Services Property: PKEY_ContactObj_Ringtone
        WPD_CONTACT_RINGTONE = DEFINE_PROPERTYKEY(
            0xFBD4FDAB,
            0x987D,
            0x4777,
            0xB3,
            0xF9,
            0x72,
            0x61,
            0x85,
            0xA9,
            0x31,
            0x2B,
            0x3F
        )

        # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_MUSIC_OBJECT_PROPERTIES_V1 This category is for properties common to all music objects. *************************************************************************
        #
        WPD_MUSIC_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0xB324F56A,
            0xDC5D,
            0x46E5,
            0xB6,
            0xDF,
            0xD2,
            0xEA,
            0x41,
            0x48,
            0x88,
            0xC6
        )


        # WPD_MUSIC_ALBUM
        # [ VT_LPWSTR ] Indicates the album of the music file.
        # Recommended Device Services Property: PKEY_MediaObj_AlbumName
        WPD_MUSIC_ALBUM = DEFINE_PROPERTYKEY(
            0xB324F56A,
            0xDC5D,
            0x46E5,
            0xB6,
            0xDF,
            0xD2,
            0xEA,
            0x41,
            0x48,
            0x88,
            0xC6,
            0x3
        )

        # WPD_MUSIC_TRACK
        # [ VT_UI4 ] Indicates the track number for the music file.
        # Recommended Device Services Property: PKEY_MediaObj_Track
        WPD_MUSIC_TRACK = DEFINE_PROPERTYKEY(
            0xB324F56A,
            0xDC5D,
            0x46E5,
            0xB6,
            0xDF,
            0xD2,
            0xEA,
            0x41,
            0x48,
            0x88,
            0xC6,
            0x4
        )


        # WPD_MUSIC_LYRICS
        # [ VT_LPWSTR ] Indicates the lyrics for the music file.
        # Recommended Device Services Property: PKEY_AudioObj_Lyrics
        WPD_MUSIC_LYRICS = DEFINE_PROPERTYKEY(
            0xB324F56A,
            0xDC5D,
            0x46E5,
            0xB6,
            0xDF,
            0xD2,
            0xEA,
            0x41,
            0x48,
            0x88,
            0xC6,
            0x6
        )

        # WPD_MUSIC_MOOD
        # [ VT_LPWSTR ] Indicates the mood for the music file.
        # Recommended Device Services Property: PKEY_MediaObj_Mood
        WPD_MUSIC_MOOD = DEFINE_PROPERTYKEY(
            0xB324F56A,
            0xDC5D,
            0x46E5,
            0xB6,
            0xDF,
            0xD2,
            0xEA,
            0x41,
            0x48,
            0x88,
            0xC6,
            0x8
        )


        # WPD_AUDIO_BITRATE
        # [ VT_UI4 ] Indicates the bit rate for the audio data, specified in
        # bits per second.
        # Recommended Device Services Property: PKEY_AudioObj_AudioBitRate
        WPD_AUDIO_BITRATE = DEFINE_PROPERTYKEY(
            0xB324F56A,
            0xDC5D,
            0x46E5,
            0xB6,
            0xDF,
            0xD2,
            0xEA,
            0x41,
            0x48,
            0x88,
            0xC6,
            0x9
        )

        # WPD_AUDIO_CHANNEL_COUNT
        # [ VT_R4 ] Indicates the number of channels in this audio file e.g.
        # 1, 2, 5.1 etc.
        # Recommended Device Services Property: PKEY_AudioObj_Channels
        WPD_AUDIO_CHANNEL_COUNT = DEFINE_PROPERTYKEY(
            0xB324F56A,
            0xDC5D,
            0x46E5,
            0xB6,
            0xDF,
            0xD2,
            0xEA,
            0x41,
            0x48,
            0x88,
            0xC6,
            0xA
        )


        # WPD_AUDIO_FORMAT_CODE
        # [ VT_UI4 ] Indicates the registered WAVE format code.
        # Recommended Device Services Property: PKEY_AudioObj_AudioFormatCode
        WPD_AUDIO_FORMAT_CODE = DEFINE_PROPERTYKEY(
            0xB324F56A,
            0xDC5D,
            0x46E5,
            0xB6,
            0xDF,
            0xD2,
            0xEA,
            0x41,
            0x48,
            0x88,
            0xC6,
            0xB
        )

        # WPD_AUDIO_BIT_DEPTH
        # [ VT_UI4 ] This property identifies the bit-depth of the audio.
        # Recommended Device Services Property: PKEY_AudioObj_AudioBitDepth
        WPD_AUDIO_BIT_DEPTH = DEFINE_PROPERTYKEY(
            0xB324F56A,
            0xDC5D,
            0x46E5,
            0xB6,
            0xDF,
            0xD2,
            0xEA,
            0x41,
            0x48,
            0x88,
            0xC6,
            0xC
        )


        # WPD_AUDIO_BLOCK_ALIGNMENT
        # [ VT_UI4 ] This property identifies the audio block alignment
        # Recommended Device Services Property:
        # PKEY_AudioObj_AudioBlockAlignment
        WPD_AUDIO_BLOCK_ALIGNMENT = DEFINE_PROPERTYKEY(
            0xB324F56A,
            0xDC5D,
            0x46E5,
            0xB6,
            0xDF,
            0xD2,
            0xEA,
            0x41,
            0x48,
            0x88,
            0xC6,
            0xD
        )

        # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_VIDEO_OBJECT_PROPERTIES_V1 This category is for properties common to all video objects. *************************************************************************
        #
        WPD_VIDEO_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A
        )

        # WPD_VIDEO_AUTHOR
        # [ VT_LPWSTR ] Indicates the author of the video file.
        # Recommended Device Services Property: PKEY_MediaObj_Producer
        WPD_VIDEO_AUTHOR = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0x2
        )


        # WPD_VIDEO_RECORDEDTV_STATION_NAME
        # [ VT_LPWSTR ] Indicates the TV station the video was recorded from.
        # Recommended Device Services Property: PKEY_VideoObj_Source
        WPD_VIDEO_RECORDEDTV_STATION_NAME = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0x4
        )

        # WPD_VIDEO_RECORDEDTV_CHANNEL_NUMBER
        # [ VT_UI4 ] Indicates the TV channel number the video was recorded
        # from.
        # Recommended Device Services Property: None
        WPD_VIDEO_RECORDEDTV_CHANNEL_NUMBER = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0x5
        )


        # WPD_VIDEO_RECORDEDTV_REPEAT
        # [ VT_BOOL ] Indicates whether the recorded TV program was a repeat
        # showing.
        # Recommended Device Services Property: None
        WPD_VIDEO_RECORDEDTV_REPEAT = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0x7
        )

        # WPD_VIDEO_BUFFER_SIZE
        # [ VT_UI4 ] Indicates the video buffer size.
        # Recommended Device Services Property: PKEY_MediaObj_BufferSize
        WPD_VIDEO_BUFFER_SIZE = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0x8
        )


        # WPD_VIDEO_CREDITS
        # [ VT_LPWSTR ] Indicates the credit text for the video file.
        # Recommended Device Services Property: PKEY_MediaObj_Credits
        WPD_VIDEO_CREDITS = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0x9
        )

        # WPD_VIDEO_KEY_FRAME_DISTANCE
        # [ VT_UI4 ] Indicates the interval between key frames in milliseconds.
        # Recommended Device Services Property: PKEY_VideoObj_KeyFrameDistance
        WPD_VIDEO_KEY_FRAME_DISTANCE = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0xA
        )


        # WPD_VIDEO_QUALITY_SETTING
        # [ VT_UI4 ] Indicates the quality setting for the video file.
        # Recommended Device Services Property: PKEY_MediaObj_EncodingQuality
        WPD_VIDEO_QUALITY_SETTING = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0xB
        )

        # WPD_VIDEO_SCAN_TYPE
        # [ VT_UI4 ] This property identifies the video scan information.
        # Recommended Device Services Property: PKEY_VideoObj_ScanType
        WPD_VIDEO_SCAN_TYPE = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0xC
        )


        # WPD_VIDEO_BITRATE
        # [ VT_UI4 ] Indicates the bitrate for the video data.
        # Recommended Device Services Property: PKEY_VideoObj_VideoBitRate
        WPD_VIDEO_BITRATE = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0xD
        )

        # WPD_VIDEO_FOURCC_CODE
        # [ VT_UI4 ] The registered FourCC code indicating the codec used for
        # the video file.
        # Recommended Device Services Property: PKEY_VideoObj_VideoFormatCode
        WPD_VIDEO_FOURCC_CODE = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0xE
        )


        # WPD_VIDEO_FRAMERATE
        # [ VT_UI4 ] Indicates the frame rate for the video data.
        # Recommended Device Services Property: PKEY_VideoObj_VideoFrameRate
        WPD_VIDEO_FRAMERATE = DEFINE_PROPERTYKEY(
            0x346F2163,
            0xF998,
            0x4146,
            0x8B,
            0x01,
            0xD1,
            0x9B,
            0x4C,
            0x00,
            0xDE,
            0x9A,
            0xF
        )

        # *********************************************************************
        # This section defines all Commands,
        # Parameters and Options associated with:
        # WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1
        # This category is properties that pertain to informational objects
        # such as appointments, tasks, memos and even documents.
        # *********************************************************************
        #
        WPD_COMMON_INFORMATION_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0xB28AE94B,
            0x05A4,
            0x4E8E,
            0xBE,
            0x01,
            0x72,
            0xCC,
            0x7E,
            0x09,
            0x9D,
            0x8F
        )

        # WPD_COMMON_INFORMATION_SUBJECT
        # [ VT_LPWSTR ] Indicates the subject field of this object.
        # Recommended Device Services Property: PKEY_MessageObj_Subject
        WPD_COMMON_INFORMATION_SUBJECT = DEFINE_PROPERTYKEY(
            0xB28AE94B,
            0x05A4,
            0x4E8E,
            0xBE,
            0x01,
            0x72,
            0xCC,
            0x7E,
            0x09,
            0x9D,
            0x8F,
            0x2
        )


        # WPD_COMMON_INFORMATION_BODY_TEXT
        # [ VT_LPWSTR ] This property contains the body text of an object, in
        # plaintext or HTML format.
        # Recommended Device Services Property: PKEY_MessageObj_Body
        WPD_COMMON_INFORMATION_BODY_TEXT = DEFINE_PROPERTYKEY(
            0xB28AE94B,
            0x05A4,
            0x4E8E,
            0xBE,
            0x01,
            0x72,
            0xCC,
            0x7E,
            0x09,
            0x9D,
            0x8F,
            0x3
        )

        # WPD_COMMON_INFORMATION_PRIORITY
        # [ VT_UI4 ] Indicates the priority of this object.
        # Recommended Device Services Property: PKEY_MessageObj_Priority
        WPD_COMMON_INFORMATION_PRIORITY = DEFINE_PROPERTYKEY(
            0xB28AE94B,
            0x05A4,
            0x4E8E,
            0xBE,
            0x01,
            0x72,
            0xCC,
            0x7E,
            0x09,
            0x9D,
            0x8F,
            0x4
        )


        # WPD_COMMON_INFORMATION_START_DATETIME
        # [ VT_DATE ] For appointments, tasks and similar objects, this
        # indicates the date/time that this item is scheduled to start.
        # Recommended Device Services Property:
        # PKEY_MessageObj_PatternValidStartDate
        WPD_COMMON_INFORMATION_START_DATETIME = DEFINE_PROPERTYKEY(
            0xB28AE94B,
            0x05A4,
            0x4E8E,
            0xBE,
            0x01,
            0x72,
            0xCC,
            0x7E,
            0x09,
            0x9D,
            0x8F,
            0x5
        )

        # WPD_COMMON_INFORMATION_END_DATETIME
        # [ VT_DATE ] For appointments, tasks and similar objects, this
        # indicates the date/time that this item is scheduled to end.
        # Recommended Device Services Property:
        # PKEY_MessageObj_PatternValidEndDate
        WPD_COMMON_INFORMATION_END_DATETIME = DEFINE_PROPERTYKEY(
            0xB28AE94B,
            0x05A4,
            0x4E8E,
            0xBE,
            0x01,
            0x72,
            0xCC,
            0x7E,
            0x09,
            0x9D,
            0x8F,
            0x6
        )


        # WPD_COMMON_INFORMATION_NOTES
        # [ VT_LPWSTR ] For appointments, tasks and similar objects, this
        # indicates any notes for this object.
        # Recommended Device Services Property: None
        WPD_COMMON_INFORMATION_NOTES = DEFINE_PROPERTYKEY(
            0xB28AE94B,
            0x05A4,
            0x4E8E,
            0xBE,
            0x01,
            0x72,
            0xCC,
            0x7E,
            0x09,
            0x9D,
            0x8F,
            0x7
        )

        # *********************************************************************
        # This section defines all Commands,
        # Parameters and Options associated with: WPD_MEMO_OBJECT_PROPERTIES_V1
        # This category is for properties common to all memo objects.
        # *********************************************************************
        #
        WPD_MEMO_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0x5FFBFC7B,
            0x7483,
            0x41AD,
            0xAF,
            0xB9,
            0xDA,
            0x3F,
            0x4E,
            0x59,
            0x2B,
            0x8D
        )

        # *********************************************************************
        # This section defines all Commands,
        # Parameters and Options associated with: z
        # PD_EMAIL_OBJECT_PROPERTIES_V1
        # This category is for properties common to all email objects.
        # *********************************************************************
        #
        WPD_EMAIL_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0x41F8F65A,
            0x5484,
            0x4782,
            0xB1,
            0x3D,
            0x47,
            0x40,
            0xDD,
            0x7C,
            0x37,
            0xC5
        )

        # WPD_EMAIL_TO_LINE
        # [ VT_LPWSTR ] Indicates the normal recipients for the message.
        # Recommended Device Services Property: PKEY_MessageObj_To
        WPD_EMAIL_TO_LINE = DEFINE_PROPERTYKEY(
            0x41F8F65A,
            0x5484,
            0x4782,
            0xB1,
            0x3D,
            0x47,
            0x40,
            0xDD,
            0x7C,
            0x37,
            0xC5,
            0x2
        )


        # WPD_EMAIL_CC_LINE
        # [ VT_LPWSTR ] Indicates the copied recipients for the message.
        # Recommended Device Services Property: PKEY_MessageObj_CC
        WPD_EMAIL_CC_LINE = DEFINE_PROPERTYKEY(
            0x41F8F65A,
            0x5484,
            0x4782,
            0xB1,
            0x3D,
            0x47,
            0x40,
            0xDD,
            0x7C,
            0x37,
            0xC5,
            0x3
        )

        # WPD_EMAIL_BCC_LINE
        # [ VT_LPWSTR ] Indicates the recipients for the message who receive a
        # "blind copy".
        # Recommended Device Services Property: PKEY_MessageObj_BCC
        WPD_EMAIL_BCC_LINE = DEFINE_PROPERTYKEY(
            0x41F8F65A,
            0x5484,
            0x4782,
            0xB1,
            0x3D,
            0x47,
            0x40,
            0xDD,
            0x7C,
            0x37,
            0xC5,
            0x4
        )


        # WPD_EMAIL_HAS_BEEN_READ
        # [ VT_BOOL ] Indicates whether the user has read this message.
        # Recommended Device Services Property: PKEY_MessageObj_Read
        WPD_EMAIL_HAS_BEEN_READ = DEFINE_PROPERTYKEY(
            0x41F8F65A,
            0x5484,
            0x4782,
            0xB1,
            0x3D,
            0x47,
            0x40,
            0xDD,
            0x7C,
            0x37,
            0xC5,
            0x7
        )

        # WPD_EMAIL_RECEIVED_TIME
        # [ VT_DATE ] Indicates at what time the message was received.
        # Recommended Device Services Property: PKEY_MessageObj_ReceivedTime
        WPD_EMAIL_RECEIVED_TIME = DEFINE_PROPERTYKEY(
            0x41F8F65A,
            0x5484,
            0x4782,
            0xB1,
            0x3D,
            0x47,
            0x40,
            0xDD,
            0x7C,
            0x37,
            0xC5,
            0x8
        )


        # WPD_EMAIL_HAS_ATTACHMENTS
        # [ VT_BOOL ] Indicates whether this message has attachments.
        # Recommended Device Services Property: None
        WPD_EMAIL_HAS_ATTACHMENTS = DEFINE_PROPERTYKEY(
            0x41F8F65A,
            0x5484,
            0x4782,
            0xB1,
            0x3D,
            0x47,
            0x40,
            0xDD,
            0x7C,
            0x37,
            0xC5,
            0x9
        )

        # WPD_EMAIL_SENDER_ADDRESS
        # [ VT_LPWSTR ] Indicates who sent the message.
        # Recommended Device Services Property: PKEY_MessageObj_Sender
        WPD_EMAIL_SENDER_ADDRESS = DEFINE_PROPERTYKEY(
            0x41F8F65A,
            0x5484,
            0x4782,
            0xB1,
            0x3D,
            0x47,
            0x40,
            0xDD,
            0x7C,
            0x37,
            0xC5,
            0xA
        )

        # *********************************************************************
        # This section defines all Commands,
        # Parameters and Options associated with:
        # WPD_APPOINTMENT_OBJECT_PROPERTIES_V1
        # This category is for properties common to all appointment objects.
        # *********************************************************************
        #
        WPD_APPOINTMENT_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0xF99EFD03,
            0x431D,
            0x40D8,
            0xA1,
            0xC9,
            0x4E,
            0x22,
            0x0D,
            0x9C,
            0x88,
            0xD3
        )


        # WPD_APPOINTMENT_LOCATION
        # [ VT_LPWSTR ] Indicates the location of the appointment e.g.
        # "Building 5, Conf. room 7".
        # Recommended Device Services Property: PKEY_CalendarObj_Location
        WPD_APPOINTMENT_LOCATION = DEFINE_PROPERTYKEY(
            0xF99EFD03,
            0x431D,
            0x40D8,
            0xA1,
            0xC9,
            0x4E,
            0x22,
            0x0D,
            0x9C,
            0x88,
            0xD3,
            0x3
        )

        # WPD_APPOINTMENT_TYPE
        # [ VT_LPWSTR ] Indicates the type of appointment e.g. "Personal",
        # "Business" etc.
        # Recommended Device Services Property: None
        WPD_APPOINTMENT_TYPE = DEFINE_PROPERTYKEY(
            0xF99EFD03,
            0x431D,
            0x40D8,
            0xA1,
            0xC9,
            0x4E,
            0x22,
            0x0D,
            0x9C,
            0x88,
            0xD3,
            0x7
        )


        # WPD_APPOINTMENT_REQUIRED_ATTENDEES
        # [ VT_LPWSTR ] Semi-colon separated list of required attendees.
        # Recommended Device Services Property: None
        WPD_APPOINTMENT_REQUIRED_ATTENDEES = DEFINE_PROPERTYKEY(
            0xF99EFD03,
            0x431D,
            0x40D8,
            0xA1,
            0xC9,
            0x4E,
            0x22,
            0x0D,
            0x9C,
            0x88,
            0xD3,
            0x8
        )

        # WPD_APPOINTMENT_OPTIONAL_ATTENDEES
        # [ VT_LPWSTR ] Semi-colon separated list of optional attendees.
        # Recommended Device Services Property: None
        WPD_APPOINTMENT_OPTIONAL_ATTENDEES = DEFINE_PROPERTYKEY(
            0xF99EFD03,
            0x431D,
            0x40D8,
            0xA1,
            0xC9,
            0x4E,
            0x22,
            0x0D,
            0x9C,
            0x88,
            0xD3,
            0x9
        )


        # WPD_APPOINTMENT_ACCEPTED_ATTENDEES
        # [ VT_LPWSTR ] Semi-colon separated list of attendees who have
        # accepted the appointment.
        # Recommended Device Services Property: PKEY_CalendarObj_Accepted
        WPD_APPOINTMENT_ACCEPTED_ATTENDEES = DEFINE_PROPERTYKEY(
            0xF99EFD03,
            0x431D,
            0x40D8,
            0xA1,
            0xC9,
            0x4E,
            0x22,
            0x0D,
            0x9C,
            0x88,
            0xD3,
            0xA
        )

        # WPD_APPOINTMENT_RESOURCES
        # [ VT_LPWSTR ] Semi-colon separated list of resources needed for the
        # appointment.
        # Recommended Device Services Property: None
        WPD_APPOINTMENT_RESOURCES = DEFINE_PROPERTYKEY(
            0xF99EFD03,
            0x431D,
            0x40D8,
            0xA1,
            0xC9,
            0x4E,
            0x22,
            0x0D,
            0x9C,
            0x88,
            0xD3,
            0xB
        )


        # WPD_APPOINTMENT_TENTATIVE_ATTENDEES
        # [ VT_LPWSTR ] Semi-colon separated list of attendees who have
        # tentatively accepted the appointment.
        # Recommended Device Services Property: PKEY_CalendarObj_Tentative
        WPD_APPOINTMENT_TENTATIVE_ATTENDEES = DEFINE_PROPERTYKEY(
            0xF99EFD03,
            0x431D,
            0x40D8,
            0xA1,
            0xC9,
            0x4E,
            0x22,
            0x0D,
            0x9C,
            0x88,
            0xD3,
            0xC
        )

        # WPD_APPOINTMENT_DECLINED_ATTENDEES
        # [ VT_LPWSTR ] Semi-colon separated list of attendees who have
        # declined the appointment.
        # Recommended Device Services Property: PKEY_CalendarObj_Declined
        WPD_APPOINTMENT_DECLINED_ATTENDEES = DEFINE_PROPERTYKEY(
            0xF99EFD03,
            0x431D,
            0x40D8,
            0xA1,
            0xC9,
            0x4E,
            0x22,
            0x0D,
            0x9C,
            0x88,
            0xD3,
            0xD
        )

        # *********************************************************************
        # This section defines all Commands,
        # Parameters and Options associated with: WPD_TASK_OBJECT_PROPERTIES_V1
        # This category is for properties common to all task objects.
        # *********************************************************************
        #
        WPD_TASK_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0xE354E95E,
            0xD8A0,
            0x4637,
            0xA0,
            0x3A,
            0x0C,
            0xB2,
            0x68,
            0x38,
            0xDB,
            0xC7
        )


        # WPD_TASK_STATUS
        # [ VT_LPWSTR ] Indicates the status of the task e.g. "In Progress".
        # Recommended Device Services Property: None
        WPD_TASK_STATUS = DEFINE_PROPERTYKEY(
            0xE354E95E,
            0xD8A0,
            0x4637,
            0xA0,
            0x3A,
            0x0C,
            0xB2,
            0x68,
            0x38,
            0xDB,
            0xC7,
            0x6
        )

        # WPD_TASK_PERCENT_COMPLETE
        # [ VT_UI4 ] Indicates how much of the task has been completed.
        # Recommended Device Services Property: PKEY_TaskObj_Complete
        WPD_TASK_PERCENT_COMPLETE = DEFINE_PROPERTYKEY(
            0xE354E95E,
            0xD8A0,
            0x4637,
            0xA0,
            0x3A,
            0x0C,
            0xB2,
            0x68,
            0x38,
            0xDB,
            0xC7,
            0x8
        )


        # WPD_TASK_REMINDER_DATE
        # [ VT_DATE ] Indicates the date and time set for the reminder. If
        # this value is 0, then it is assumed that this task has no reminder.
        # Recommended Device Services Property: PKEY_TaskObj_ReminderDateTime
        WPD_TASK_REMINDER_DATE = DEFINE_PROPERTYKEY(
            0xE354E95E,
            0xD8A0,
            0x4637,
            0xA0,
            0x3A,
            0x0C,
            0xB2,
            0x68,
            0x38,
            0xDB,
            0xC7,
            0xA
        )

        # WPD_TASK_OWNER
        # [ VT_LPWSTR ] Indicates the owner of the task.
        # Recommended Device Services Property: None
        WPD_TASK_OWNER = DEFINE_PROPERTYKEY(
            0xE354E95E,
            0xD8A0,
            0x4637,
            0xA0,
            0x3A,
            0x0C,
            0xB2,
            0x68,
            0x38,
            0xDB,
            0xC7,
            0xB
        )

        # *********************************************************************
        # This section defines all Commands,
        # Parameters and Options associated with: WPD_SMS_OBJECT_PROPERTIES_V1
        # This category is for properties common to all objects whose
        # functional category is WPD_FUNCTIONAL_CATEGORY_SMS
        # *********************************************************************
        #
        WPD_SMS_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0x7E1074CC,
            0x50FF,
            0x4DD1,
            0xA7,
            0x42,
            0x53,
            0xBE,
            0x6F,
            0x09,
            0x3A,
            0x0D
        )


        # WPD_SMS_PROVIDER
        # [ VT_LPWSTR ] Indicates the service provider name.
        # Recommended Device Services Property: None
        WPD_SMS_PROVIDER = DEFINE_PROPERTYKEY(
            0x7E1074CC,
            0x50FF,
            0x4DD1,
            0xA7,
            0x42,
            0x53,
            0xBE,
            0x6F,
            0x09,
            0x3A,
            0x0D,
            0x2
        )

        # WPD_SMS_TIMEOUT
        # [ VT_UI4 ] Indicates the number of milliseconds until a timeout is
        # returned.
        # Recommended Device Services Property: None
        WPD_SMS_TIMEOUT = DEFINE_PROPERTYKEY(
            0x7E1074CC,
            0x50FF,
            0x4DD1,
            0xA7,
            0x42,
            0x53,
            0xBE,
            0x6F,
            0x09,
            0x3A,
            0x0D,
            0x3
        )


        # WPD_SMS_MAX_PAYLOAD
        # [ VT_UI4 ] Indicates the maximum number of bytes that can be
        # contained in a message.
        # Recommended Device Services Property: None
        WPD_SMS_MAX_PAYLOAD = DEFINE_PROPERTYKEY(
            0x7E1074CC,
            0x50FF,
            0x4DD1,
            0xA7,
            0x42,
            0x53,
            0xBE,
            0x6F,
            0x09,
            0x3A,
            0x0D,
            0x4
        )

        # WPD_SMS_ENCODING
        # [ VT_UI4 ] Indicates how the driver will encode the text message
        # sent by the client.
        # Recommended Device Services Property: None
        WPD_SMS_ENCODING = DEFINE_PROPERTYKEY(
            0x7E1074CC,
            0x50FF,
            0x4DD1,
            0xA7,
            0x42,
            0x53,
            0xBE,
            0x6F,
            0x09,
            0x3A,
            0x0D,
            0x5
        )

        # ************************************************************************** This section defines all Commands, Parameters and Options associated with: WPD_SECTION_OBJECT_PROPERTIES_V1 This category is for properties common to all objects whose content type is WPD_CONTENT_TYPE_SECTION *************************************************************************
        #
        WPD_SECTION_OBJECT_PROPERTIES_V1 = DEFINE_GUID(
            0x516AFD2B,
            0xC64E,
            0x44F0,
            0x98,
            0xDC,
            0xBE,
            0xE1,
            0xC8,
            0x8F,
            0x7D,
            0x66
        )


        # WPD_SECTION_DATA_OFFSET
        # [ VT_UI8 ] Indicates the zero-based offset of the data for the
        # referenced object.
        # Recommended Device Services Property: None
        WPD_SECTION_DATA_OFFSET = DEFINE_PROPERTYKEY(
            0x516AFD2B,
            0xC64E,
            0x44F0,
            0x98,
            0xDC,
            0xBE,
            0xE1,
            0xC8,
            0x8F,
            0x7D,
            0x66,
            0x2
        )

        # WPD_SECTION_DATA_LENGTH
        # [ VT_UI8 ] Indicates the length of data for the referenced object.
        # Recommended Device Services Property: None
        WPD_SECTION_DATA_LENGTH = DEFINE_PROPERTYKEY(
            0x516AFD2B,
            0xC64E,
            0x44F0,
            0x98,
            0xDC,
            0xBE,
            0xE1,
            0xC8,
            0x8F,
            0x7D,
            0x66,
            0x3
        )


        # WPD_SECTION_DATA_UNITS
        # [ VT_UI4 ] Indicates the units for WPD_SECTION_DATA_OFFSET and
        # WPD_SECTION_DATA_LENGTH properties on this object
        # (e.g. offset in bytes, offset in milliseconds etc.).
        # Recommended Device Services Property: None
        WPD_SECTION_DATA_UNITS = DEFINE_PROPERTYKEY(
            0x516AFD2B,
            0xC64E,
            0x44F0,
            0x98,
            0xDC,
            0xBE,
            0xE1,
            0xC8,
            0x8F,
            0x7D,
            0x66,
            0x4
        )

        # WPD_SECTION_DATA_REFERENCED_OBJECT_RESOURCE
        # [ VT_UNKNOWN ] This is an IPortableDeviceKeyCollection containing a
        # single value, which is the key identifying the resource on the
        # referenced object which the WPD_SECTION_DATA_OFFSET and
        # WPD_SECTION_DATA_LENGTH apply to.
        # Recommended Device Services Property: None
        WPD_SECTION_DATA_REFERENCED_OBJECT_RESOURCE = DEFINE_PROPERTYKEY(
            0x516AFD2B,
            0xC64E,
            0x44F0,
            0x98,
            0xDC,
            0xBE,
            0xE1,
            0xC8,
            0x8F,
            0x7D,
            0x66,
            0x5
        )
    # END IF   WPD_SERVICES_STRICT

    # ************************************************************************** This section defines Structures and Macros used by driver writers to simplify Wpd Command Access checks. Sample Usage: - Add table used to lookup the Access required for Wpd Commands BEGIN_WPD_COMMAND_ACCESS_MAP(g_WpdCommandAccessMap)  DECLARE_WPD_STANDARD_COMMAND_ACCESS_ENTRIES  - Add any custom commands here e.g.  WPD_COMMAND_ACCESS_ENTRY(MyCustomCommand, WPD_COMMAND_ACCESS_READWRITE) END_WPD_COMMAND_ACCESS_MAP - This enables the driver to use VERIFY_WPD_COMMAND_ACCESS to check command access function for us. DECLARE_VERIFY_WPD_COMMAND_ACCESS; ... - When the driver receives a WPD IOCTL, it can check that the IOCTL specified matches  the command payload with:  hr = VERIFY_WPD_COMMAND_ACCESS(ControlCode, pParams, g_WpdCommandAccessMap); *************************************************************************
    #
    # Structure used as an entry in the Command / Access lookup table.
    tagWPD_COMMAND_ACCESS_LOOKUP_ENTRY._fields_ = [
        ('Command', PROPERTYKEY),
        ('AccessType', DWORD),
        ('AccessProperty', PROPERTYKEY),
    ]

    # Used to start a declaration of a WPD Command Access Lookup Map. This
    # macro is usually followed by:
    # DECLARE_WPD_STANDARD_COMMAND_ACCESS_ENTRIES
    # Zero or more WPD_COMMAND_ACCESS_ENTRY or
    # WPD_COMMAND_ACCESS_PROPERTY_ENTRY macros (one for every custom command).
    # The Map is ended with END_WPD_COMMAND_ACCESS_MAP.
    def BEGIN_WPD_COMMAND_ACCESS_MAP(x):
        return WPD_COMMAND_ACCESS_LOOKUP_ENTRY(
            PD_PROPERTY_NULL,
            0,
            WPD_PROPERTY_NULL
        )
    # Ends a WPD Command Access Lookup Map started with
    # BEGIN_WPD_COMMAND_ACCESS_MAP
    END_WPD_COMMAND_ACCESS_MAP = [WPD_PROPERTY_NULL, 0, WPD_PROPERTY_NULL]

    # Adds a custom entry to a WPD Command Access Lookup Map started with
    # BEGIN_WPD_COMMAND_ACCESS_MAP
    def WPD_COMMAND_ACCESS_ENTRY(WpdCommand, WpdCommandAccessType):
        return [WpdCommand, WpdCommandAccessType, WPD_PROPERTY_NULL]

    # Adds a custom entry to a WPD Command Access Lookup Map started with
    # BEGIN_WPD_COMMAND_ACCESS_MAP
    def WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WpdCommand, WpdCommandAccessType, WpdAccessProperty):
        return [WpdCommand, WpdCommandAccessType, WpdAccessProperty]

    # Declares entries for all the WPD Commands contained in this header file.
    # Used after BEGIN_WPD_COMMAND_ACCESS_MAP.
    DECLARE_WPD_STANDARD_COMMAND_ACCESS_ENTRIES = (
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_COMMON_RESET_DEVICE, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_COMMON_GET_OBJECT_IDS_FROM_PERSISTENT_UNIQUE_IDS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_COMMON_SAVE_CLIENT_INFORMATION, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_ENUMERATION_START_FIND, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_ENUMERATION_FIND_NEXT, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_ENUMERATION_END_FIND, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_GET, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_SET, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_DELETE, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_START, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_NEXT, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_LIST_END, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_START, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_NEXT, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_BULK_GET_VALUES_BY_OBJECT_FORMAT_END, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_START, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_NEXT, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_PROPERTIES_BULK_SET_VALUES_BY_OBJECT_LIST_END, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_GET_SUPPORTED, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_GET_ATTRIBUTES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_OPEN, WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_STGM_ACCESS, WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_READ, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_WRITE, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_CLOSE, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_DELETE, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_CREATE_RESOURCE, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_REVERT, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_SEEK, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_COMMIT, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_RESOURCES_SEEK_IN_UNITS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_ONLY, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_AND_DATA, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_MANAGEMENT_WRITE_OBJECT_DATA, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_MANAGEMENT_COMMIT_OBJECT, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_MANAGEMENT_REVERT_OBJECT, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_MANAGEMENT_DELETE_OBJECTS, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_MANAGEMENT_MOVE_OBJECTS, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_MANAGEMENT_COPY_OBJECTS, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_OBJECT_MANAGEMENT_UPDATE_OBJECT_WITH_PROPERTIES_AND_DATA, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NUL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CAPABILITIES_GET_FIXED_PROPERTY_ATTRIBUTES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_STORAGE_FORMAT, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_STORAGE_EJECT, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SMS_SEND, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_STILL_IMAGE_CAPTURE_INITIATE, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_MEDIA_CAPTURE_START, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_MEDIA_CAPTURE_STOP, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_MEDIA_CAPTURE_PAUSE, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_DEVICE_HINTS_GET_CONTENT_LOCATION, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CLASS_EXTENSION_WRITE_DEVICE_INFORMATION, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CLASS_EXTENSION_REGISTER_SERVICE_INTERFACES, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_CLASS_EXTENSION_UNREGISTER_SERVICE_INTERFACES, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_GENERATE_KEYPAIR, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_COMMIT_KEYPAIR, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_PROCESS_WIRELESS_PROFILE, WPD_COMMAND_ACCESS_READWRITE, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_COMMON_GET_SERVICE_OBJECT_ID, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS_BY_FORMAT, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL)
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_ATTRIBUTES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL)
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_PARAMETER_ATTRIBUTES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMATS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_ATTRIBUTES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_PROPERTY_ATTRIBUTES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_EVENTS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_ATTRIBUTES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_PARAMETER_ATTRIBUTES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_INHERITED_SERVICES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_RENDERING_PROFILES, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_COMMANDS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_CAPABILITIES_GET_COMMAND_OPTIONS, WPD_COMMAND_ACCESS_READ, WPD_PROPERTY_NULL) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_METHODS_START_INVOKE, WPD_COMMAND_ACCESS_FROM_ATTRIBUTE_WITH_METHOD_ACCESS, WPD_METHOD_ATTRIBUTE_ACCESS) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_METHODS_CANCEL_INVOKE, WPD_COMMAND_ACCESS_FROM_ATTRIBUTE_WITH_METHOD_ACCESS, WPD_METHOD_ATTRIBUTE_ACCESS) +
        WPD_COMMAND_ACCESS_PROPERTY_ENTRY(WPD_COMMAND_SERVICE_METHODS_END_INVOKE, WPD_COMMAND_ACCESS_FROM_ATTRIBUTE_WITH_METHOD_ACCESS, WPD_METHOD_ATTRIBUTE_ACCESS)
    )

    # Declares an instance of the function used to check whether a WPD Command
    # is in the driver's WPD Command Access Map.
    # Driver writers should not call this function directly, but should
    # instead use the IS_COMMAND_IN_WPD_COMMAND_ACCESS_MAP alias.
    def DECLARE_IS_COMMAND_IN_WPD_COMMAND_ACCESS_MAP():
        return (
            BOOL IsCommandInWpdCommandAccessMap REFPROPERTYKEY WpdCommand,
            _In_ WPD_COMMAND_ACCESS_LOOKUP_ENTRY *pCommandAccessLookupMap { BOOL bRet = FALSE; if(,
                (pCommandParams == NULL) { return E_POINTER; } while(pCommandAccessLookupMap[dwMapIndex + + ].Command != WPD_PROPERTY_NULL) { if(IsEqualPropertyKeypCommandAccessLookupMap[dwMapIndex].Command,
                WpdCommand)
            ) { bRet = TRUE; break; } dwMapIndex + + ; } return bRet; };
        )

    # This macro is an alias for the function used to check whether a WPD
    # Command is in the driver's WPD Command Access Map
    # (see BEGIN_WPD_COMMAND_ACCESS_MAP)
    IS_COMMAND_IN_WPD_COMMAND_ACCESS_MAP = IsCommandInWpdCommandAccessMap

    # Declares an instance of the function used to verify that WPD Commands
    # are sent with the appropriate Access Flags in the IOCTL.
    # Driver writers should not call this function directly, but should
    # instead use the VERIFY_WPD_COMMAND_ACCESS alias.
    DECLARE_VERIFY_WPD_COMMAND_ACCESS = (
        HRESULT VerifyWpdCommandAccessFromMap( DWORD                          ControlCode,
        _In_ IPortableDeviceValues           *pCommandParams,
        _In_ WPD_COMMAND_ACCESS_LOOKUP_ENTRY *pCommandAccessLookupMap) [ HRESULT     hr                      = S_OK; DWORD       dwMapIndex              = 0; PROPERTYKEY WpdCommand              = WPD_PROPERTY_NULL; DWORD       dwExpectedControlCode   = IOCTL_WPD_MESSAGE_READWRITE_ACCESS; if((pCommandParams == NULL) or (pCommandAccessLookupMap == NULL)) [ return E_POINTER; ] if(ControlCode == IOCTL_WPD_MESSAGE_READWRITE_ACCESS) [ return S_OK; ] hr = pCommandParams.GetGuidValue(WPD_PROPERTY_COMMON_COMMAND_CATEGORY,
        & WpdCommand.fmtid); if(SUCCEEDED(hr)) [ hr = pCommandParams.GetUnsignedIntegerValue(WPD_PROPERTY_COMMON_COMMAND_ID,
        & WpdCommand.pid); if(SUCCEEDED(hr)) [ while(not IsEqualPropertyKey(pCommandAccessLookupMap[dwMapIndex].Command,
        WPD_PROPERTY_NULL)) [ if(IsEqualPropertyKey(pCommandAccessLookupMap[dwMapIndex].Command,
        WpdCommand)) [ switch(pCommandAccessLookupMap[dwMapIndex].AccessType) [ case WPD_COMMAND_ACCESS_READ: [ dwExpectedControlCode = IOCTL_WPD_MESSAGE_READ_ACCESS; ] break; case WPD_COMMAND_ACCESS_READWRITE: [ dwExpectedControlCode = IOCTL_WPD_MESSAGE_READWRITE_ACCESS; ] break; case WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_STGM_ACCESS: [ DWORD dwAccessPropVal = STGM_READWRITE; HRESULT hrTemp = S_OK; hrTemp = pCommandParams.GetUnsignedIntegerValue(pCommandAccessLookupMap[dwMapIndex].AccessProperty,
        & dwAccessPropVal); if(dwAccessPropVal == STGM_READ) [ dwExpectedControlCode = IOCTL_WPD_MESSAGE_READ_ACCESS; ] else [ dwExpectedControlCode = IOCTL_WPD_MESSAGE_READWRITE_ACCESS; ] ] break; case WPD_COMMAND_ACCESS_FROM_PROPERTY_WITH_FILE_ACCESS: [ DWORD dwAccessPropVal = FILE_READ_ACCESS; HRESULT hrTemp = S_OK; hrTemp = pCommandParams.GetUnsignedIntegerValue(pCommandAccessLookupMap[dwMapIndex].AccessProperty,
        & dwAccessPropVal); if(dwAccessPropVal == FILE_READ_ACCESS) [ dwExpectedControlCode = IOCTL_WPD_MESSAGE_READ_ACCESS; ] else [ dwExpectedControlCode = IOCTL_WPD_MESSAGE_READWRITE_ACCESS; ] ] break; default: [ dwExpectedControlCode = IOCTL_WPD_MESSAGE_READWRITE_ACCESS; ] break; ] break; ] dwMapIndex +  + ; ] ] ] if(SUCCEEDED(hr)) [ if(ControlCode != dwExpectedControlCode) [ return E_INVALIDARG; ] ] return hr; ];
    )

    # This macro is an alias for the function used to verify that WPD Commands
    # are sent with the appropriate Access Flags in the IOCTL
    VERIFY_WPD_COMMAND_ACCESS = VerifyWpdCommandAccessFromMap

    # ************************************************************************** This section defines the inline helper functions *************************************************************************
    #
    # This function can be used after IPortableDeviceManager::GetDevices(..)
    # and IPortableDeviceServiceManager::GetDeviceServices(..)
    # to free the elements of the pPnPIDs array. The caller is responsible for
    # freeing pPnPIDs when this function completes.# END IF   ((NTDDI_VERSION >= NTDDI_WINXPSP2 and NTDDI_VERSION < NTDDI_WS03) or (NTDDI_VERSION >= NTDDI_WINLH))
