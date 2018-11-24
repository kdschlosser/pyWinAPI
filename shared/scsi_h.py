import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _CDB(ctypes.Union):
    pass


CDB = _CDB
PCDB = POINTER(_CDB)


class _CDB32(ctypes.Union):
    pass


CDB32 = _CDB32
PCDB32 = POINTER(_CDB32)


class _NOTIFICATION_EVENT_STATUS_HEADER(ctypes.Structure):
    pass


NOTIFICATION_EVENT_STATUS_HEADER = _NOTIFICATION_EVENT_STATUS_HEADER
PNOTIFICATION_EVENT_STATUS_HEADER = POINTER(_NOTIFICATION_EVENT_STATUS_HEADER)


class _NOTIFICATION_OPERATIONAL_STATUS(ctypes.Structure):
    pass


NOTIFICATION_OPERATIONAL_STATUS = _NOTIFICATION_OPERATIONAL_STATUS
PNOTIFICATION_OPERATIONAL_STATUS = POINTER(_NOTIFICATION_OPERATIONAL_STATUS)


class _NOTIFICATION_POWER_STATUS(ctypes.Structure):
    pass


NOTIFICATION_POWER_STATUS = _NOTIFICATION_POWER_STATUS
PNOTIFICATION_POWER_STATUS = POINTER(_NOTIFICATION_POWER_STATUS)


class _NOTIFICATION_EXTERNAL_STATUS(ctypes.Structure):
    pass


NOTIFICATION_EXTERNAL_STATUS = _NOTIFICATION_EXTERNAL_STATUS
PNOTIFICATION_EXTERNAL_STATUS = POINTER(_NOTIFICATION_EXTERNAL_STATUS)


class _NOTIFICATION_MEDIA_STATUS(ctypes.Structure):
    pass


NOTIFICATION_MEDIA_STATUS = _NOTIFICATION_MEDIA_STATUS
PNOTIFICATION_MEDIA_STATUS = POINTER(_NOTIFICATION_MEDIA_STATUS)


class _NOTIFICATION_MULTI_HOST_STATUS(ctypes.Structure):
    pass


NOTIFICATION_MULTI_HOST_STATUS = _NOTIFICATION_MULTI_HOST_STATUS
PNOTIFICATION_MULTI_HOST_STATUS = POINTER(_NOTIFICATION_MULTI_HOST_STATUS)


class _NOTIFICATION_BUSY_STATUS(ctypes.Structure):
    pass


NOTIFICATION_BUSY_STATUS = _NOTIFICATION_BUSY_STATUS
PNOTIFICATION_BUSY_STATUS = POINTER(_NOTIFICATION_BUSY_STATUS)


class _SUPPORTED_SECURITY_PROTOCOLS_PARAMETER_DATA(ctypes.Structure):
    pass


SUPPORTED_SECURITY_PROTOCOLS_PARAMETER_DATA = _SUPPORTED_SECURITY_PROTOCOLS_PARAMETER_DATA
PSUPPORTED_SECURITY_PROTOCOLS_PARAMETER_DATA = POINTER(_SUPPORTED_SECURITY_PROTOCOLS_PARAMETER_DATA)


class _READ_DVD_STRUCTURES_HEADER(ctypes.Structure):
    pass


READ_DVD_STRUCTURES_HEADER = _READ_DVD_STRUCTURES_HEADER
PREAD_DVD_STRUCTURES_HEADER = POINTER(_READ_DVD_STRUCTURES_HEADER)


class _CDVD_KEY_HEADER(ctypes.Structure):
    pass


CDVD_KEY_HEADER = _CDVD_KEY_HEADER
PCDVD_KEY_HEADER = POINTER(_CDVD_KEY_HEADER)


class _CDVD_REPORT_AGID_DATA(ctypes.Structure):
    pass


CDVD_REPORT_AGID_DATA = _CDVD_REPORT_AGID_DATA
PCDVD_REPORT_AGID_DATA = POINTER(_CDVD_REPORT_AGID_DATA)


class _CDVD_CHALLENGE_KEY_DATA(ctypes.Structure):
    pass


CDVD_CHALLENGE_KEY_DATA = _CDVD_CHALLENGE_KEY_DATA
PCDVD_CHALLENGE_KEY_DATA = POINTER(_CDVD_CHALLENGE_KEY_DATA)


class _CDVD_KEY_DATA(ctypes.Structure):
    pass


CDVD_KEY_DATA = _CDVD_KEY_DATA
PCDVD_KEY_DATA = POINTER(_CDVD_KEY_DATA)


class _CDVD_REPORT_ASF_DATA(ctypes.Structure):
    pass


CDVD_REPORT_ASF_DATA = _CDVD_REPORT_ASF_DATA
PCDVD_REPORT_ASF_DATA = POINTER(_CDVD_REPORT_ASF_DATA)


class _CDVD_TITLE_KEY_HEADER(ctypes.Structure):
    pass


CDVD_TITLE_KEY_HEADER = _CDVD_TITLE_KEY_HEADER
PCDVD_TITLE_KEY_HEADER = POINTER(_CDVD_TITLE_KEY_HEADER)


class _FORMAT_DESCRIPTOR(ctypes.Structure):
    pass


FORMAT_DESCRIPTOR = _FORMAT_DESCRIPTOR
PFORMAT_DESCRIPTOR = POINTER(_FORMAT_DESCRIPTOR)


class _FORMAT_LIST_HEADER(ctypes.Structure):
    pass


FORMAT_LIST_HEADER = _FORMAT_LIST_HEADER
PFORMAT_LIST_HEADER = POINTER(_FORMAT_LIST_HEADER)


class _FORMATTED_CAPACITY_DESCRIPTOR(ctypes.Structure):
    pass


FORMATTED_CAPACITY_DESCRIPTOR = _FORMATTED_CAPACITY_DESCRIPTOR
PFORMATTED_CAPACITY_DESCRIPTOR = POINTER(_FORMATTED_CAPACITY_DESCRIPTOR)


class _FORMATTED_CAPACITY_LIST(ctypes.Structure):
    pass


FORMATTED_CAPACITY_LIST = _FORMATTED_CAPACITY_LIST
PFORMATTED_CAPACITY_LIST = POINTER(_FORMATTED_CAPACITY_LIST)


class _OPC_TABLE_ENTRY(ctypes.Structure):
    pass


OPC_TABLE_ENTRY = _OPC_TABLE_ENTRY
POPC_TABLE_ENTRY = POINTER(_OPC_TABLE_ENTRY)


class _DISC_INFORMATION(ctypes.Structure):
    pass


DISC_INFORMATION = _DISC_INFORMATION
PDISC_INFORMATION = POINTER(_DISC_INFORMATION)


class _DISK_INFORMATION(ctypes.Structure):
    pass


DISK_INFORMATION = _DISK_INFORMATION
PDISK_INFORMATION = POINTER(_DISK_INFORMATION)


class _DATA_BLOCK_HEADER(ctypes.Structure):
    pass


DATA_BLOCK_HEADER = _DATA_BLOCK_HEADER
PDATA_BLOCK_HEADER = POINTER(_DATA_BLOCK_HEADER)


class _TRACK_INFORMATION(ctypes.Structure):
    pass


TRACK_INFORMATION = _TRACK_INFORMATION
PTRACK_INFORMATION = POINTER(_TRACK_INFORMATION)


class _TRACK_INFORMATION2(ctypes.Structure):
    pass


TRACK_INFORMATION2 = _TRACK_INFORMATION2
PTRACK_INFORMATION2 = POINTER(_TRACK_INFORMATION2)


class _TRACK_INFORMATION3(ctypes.Structure):
    pass


TRACK_INFORMATION3 = _TRACK_INFORMATION3
PTRACK_INFORMATION3 = POINTER(_TRACK_INFORMATION3)


class _PERFORMANCE_DESCRIPTOR(ctypes.Structure):
    pass


PERFORMANCE_DESCRIPTOR = _PERFORMANCE_DESCRIPTOR
PPERFORMANCE_DESCRIPTOR = POINTER(_PERFORMANCE_DESCRIPTOR)


class _SCSI_EXTENDED_MESSAGE(ctypes.Structure):
    pass


SCSI_EXTENDED_MESSAGE = _SCSI_EXTENDED_MESSAGE
PSCSI_EXTENDED_MESSAGE = POINTER(_SCSI_EXTENDED_MESSAGE)


class _INQUIRYDATA(ctypes.Structure):
    pass


INQUIRYDATA = _INQUIRYDATA
PINQUIRYDATA = POINTER(_INQUIRYDATA)


class _VPD_MEDIA_SERIAL_NUMBER_PAGE(ctypes.Structure):
    pass


VPD_MEDIA_SERIAL_NUMBER_PAGE = _VPD_MEDIA_SERIAL_NUMBER_PAGE
PVPD_MEDIA_SERIAL_NUMBER_PAGE = POINTER(_VPD_MEDIA_SERIAL_NUMBER_PAGE)


class _VPD_SERIAL_NUMBER_PAGE(ctypes.Structure):
    pass


VPD_SERIAL_NUMBER_PAGE = _VPD_SERIAL_NUMBER_PAGE
PVPD_SERIAL_NUMBER_PAGE = POINTER(_VPD_SERIAL_NUMBER_PAGE)


class _VPD_IDENTIFICATION_DESCRIPTOR(ctypes.Structure):
    pass


VPD_IDENTIFICATION_DESCRIPTOR = _VPD_IDENTIFICATION_DESCRIPTOR
PVPD_IDENTIFICATION_DESCRIPTOR = POINTER(_VPD_IDENTIFICATION_DESCRIPTOR)


class _VPD_IDENTIFICATION_PAGE(ctypes.Structure):
    pass


VPD_IDENTIFICATION_PAGE = _VPD_IDENTIFICATION_PAGE
PVPD_IDENTIFICATION_PAGE = POINTER(_VPD_IDENTIFICATION_PAGE)


class _VPD_EXTENDED_INQUIRY_DATA_PAGE(ctypes.Structure):
    pass


VPD_EXTENDED_INQUIRY_DATA_PAGE = _VPD_EXTENDED_INQUIRY_DATA_PAGE
PVPD_EXTENDED_INQUIRY_DATA_PAGE = POINTER(_VPD_EXTENDED_INQUIRY_DATA_PAGE)


class _VPD_ATA_INFORMATION_PAGE(ctypes.Structure):
    pass


VPD_ATA_INFORMATION_PAGE = _VPD_ATA_INFORMATION_PAGE
PVPD_ATA_INFORMATION_PAGE = POINTER(_VPD_ATA_INFORMATION_PAGE)


class _VPD_THIRD_PARTY_COPY_PAGE(ctypes.Structure):
    pass


VPD_THIRD_PARTY_COPY_PAGE = _VPD_THIRD_PARTY_COPY_PAGE
PVPD_THIRD_PARTY_COPY_PAGE = POINTER(_VPD_THIRD_PARTY_COPY_PAGE)


class _WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR(ctypes.Structure):
    pass


WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR = _WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR
PWINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR = POINTER(_WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR)


class _VPD_BLOCK_LIMITS_PAGE(ctypes.Structure):
    pass


VPD_BLOCK_LIMITS_PAGE = _VPD_BLOCK_LIMITS_PAGE
PVPD_BLOCK_LIMITS_PAGE = POINTER(_VPD_BLOCK_LIMITS_PAGE)


class _VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE(ctypes.Structure):
    pass


VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE = _VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE
PVPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE = POINTER(_VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE)


class _VPD_LOGICAL_BLOCK_PROVISIONING_PAGE(ctypes.Structure):
    pass


VPD_LOGICAL_BLOCK_PROVISIONING_PAGE = _VPD_LOGICAL_BLOCK_PROVISIONING_PAGE
PVPD_LOGICAL_BLOCK_PROVISIONING_PAGE = POINTER(_VPD_LOGICAL_BLOCK_PROVISIONING_PAGE)


class _VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE(ctypes.Structure):
    pass


VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE = _VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE
PVPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE = POINTER(_VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE)


class _VPD_SUPPORTED_PAGES_PAGE(ctypes.Structure):
    pass


VPD_SUPPORTED_PAGES_PAGE = _VPD_SUPPORTED_PAGES_PAGE
PVPD_SUPPORTED_PAGES_PAGE = POINTER(_VPD_SUPPORTED_PAGES_PAGE)


class _LOG_PARAMETER_HEADER(ctypes.Structure):
    pass


LOG_PARAMETER_HEADER = _LOG_PARAMETER_HEADER
PLOG_PARAMETER_HEADER = POINTER(_LOG_PARAMETER_HEADER)


class _LOG_PARAMETER(ctypes.Structure):
    pass


LOG_PARAMETER = _LOG_PARAMETER
PLOG_PARAMETER = POINTER(_LOG_PARAMETER)


class _LOG_PAGE(ctypes.Structure):
    pass


LOG_PAGE = _LOG_PAGE
PLOG_PAGE = POINTER(_LOG_PAGE)


class _LOG_PARAMETER_THRESHOLD_RESOURCE_COUNT(ctypes.Structure):
    pass


LOG_PARAMETER_THRESHOLD_RESOURCE_COUNT = _LOG_PARAMETER_THRESHOLD_RESOURCE_COUNT
PLOG_PARAMETER_THRESHOLD_RESOURCE_COUNT = POINTER(_LOG_PARAMETER_THRESHOLD_RESOURCE_COUNT)


class _LOG_PAGE_LOGICAL_BLOCK_PROVISIONING(ctypes.Structure):
    pass


LOG_PAGE_LOGICAL_BLOCK_PROVISIONING = _LOG_PAGE_LOGICAL_BLOCK_PROVISIONING
PLOG_PAGE_LOGICAL_BLOCK_PROVISIONING = POINTER(_LOG_PAGE_LOGICAL_BLOCK_PROVISIONING)


class PRI_REGISTRATION_LIST(ctypes.Structure):
    pass


PPRI_REGISTRATION_LIST = POINTER(PRI_REGISTRATION_LIST)


class PRI_RESERVATION_DESCRIPTOR(ctypes.Structure):
    pass


PPRI_RESERVATION_DESCRIPTOR = POINTER(PRI_RESERVATION_DESCRIPTOR)


class PRI_RESERVATION_LIST(ctypes.Structure):
    pass


PPRI_RESERVATION_LIST = POINTER(PRI_RESERVATION_LIST)


class PRO_PARAMETER_LIST(ctypes.Structure):
    pass


PPRO_PARAMETER_LIST = POINTER(PRO_PARAMETER_LIST)


class RT_PARAMETER_DATA(ctypes.Structure):
    pass


PRT_PARAMETER_DATA = POINTER(RT_PARAMETER_DATA)


class ST_PARAMETER_DATA(ctypes.Structure):
    pass


PST_PARAMETER_DATA = POINTER(ST_PARAMETER_DATA)


class BLOCK_DEVICE_RANGE_DESCRIPTOR(ctypes.Structure):
    pass


PBLOCK_DEVICE_RANGE_DESCRIPTOR = POINTER(BLOCK_DEVICE_RANGE_DESCRIPTOR)


class POPULATE_TOKEN_HEADER(ctypes.Structure):
    pass


PPOPULATE_TOKEN_HEADER = POINTER(POPULATE_TOKEN_HEADER)


class WRITE_USING_TOKEN_HEADER(ctypes.Structure):
    pass


PWRITE_USING_TOKEN_HEADER = POINTER(WRITE_USING_TOKEN_HEADER)


class RECEIVE_TOKEN_INFORMATION_HEADER(ctypes.Structure):
    pass


PRECEIVE_TOKEN_INFORMATION_HEADER = POINTER(RECEIVE_TOKEN_INFORMATION_HEADER)


class RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER(ctypes.Structure):
    pass


PRECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER = POINTER(RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER)


class BLOCK_DEVICE_TOKEN_DESCRIPTOR(ctypes.Structure):
    pass

PBLOCK_DEVICE_TOKEN_DESCRIPTOR = POINTER(BLOCK_DEVICE_TOKEN_DESCRIPTOR)


class _OVERWRITE_PARAMETER_LIST(ctypes.Structure):
    pass


OVERWRITE_PARAMETER_LIST = _OVERWRITE_PARAMETER_LIST
POVERWRITE_PARAMETER_LIST = POINTER(_OVERWRITE_PARAMETER_LIST)


class _SENSE_DATA(ctypes.Structure):
    pass


SENSE_DATA = _SENSE_DATA
PSENSE_DATA = POINTER(_SENSE_DATA)


class _SCSI_SENSE_DESCRIPTOR_HEADER(ctypes.Structure):
    pass


SCSI_SENSE_DESCRIPTOR_HEADER = _SCSI_SENSE_DESCRIPTOR_HEADER
PSCSI_SENSE_DESCRIPTOR_HEADER = POINTER(_SCSI_SENSE_DESCRIPTOR_HEADER)


class _SCSI_SENSE_DESCRIPTOR_INFORMATION(ctypes.Structure):
    pass


SCSI_SENSE_DESCRIPTOR_INFORMATION = _SCSI_SENSE_DESCRIPTOR_INFORMATION
PSCSI_SENSE_DESCRIPTOR_INFORMATION = POINTER(_SCSI_SENSE_DESCRIPTOR_INFORMATION)


class _SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND(ctypes.Structure):
    pass


SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND = _SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND
PSCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND = POINTER(_SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND)


class _SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN(ctypes.Structure):
    pass


SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN = _SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN
PSCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN = POINTER(_SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN)


class _DESCRIPTOR_SENSE_DATA(ctypes.Structure):
    pass


DESCRIPTOR_SENSE_DATA = _DESCRIPTOR_SENSE_DATA
PDESCRIPTOR_SENSE_DATA = POINTER(_DESCRIPTOR_SENSE_DATA)


class _SENSE_DATA_EX(ctypes.Union):
    pass


SENSE_DATA_EX = _SENSE_DATA_EX
PSENSE_DATA_EX = POINTER(_SENSE_DATA_EX)


class _READ_CAPACITY_DATA(ctypes.Structure):
    pass


READ_CAPACITY_DATA = _READ_CAPACITY_DATA
PREAD_CAPACITY_DATA = POINTER(_READ_CAPACITY_DATA)


class _READ_CAPACITY_DATA_EX(ctypes.Structure):
    pass


READ_CAPACITY_DATA_EX = _READ_CAPACITY_DATA_EX
PREAD_CAPACITY_DATA_EX = POINTER(_READ_CAPACITY_DATA_EX)


class _READ_CAPACITY16_DATA(ctypes.Structure):
    pass


READ_CAPACITY16_DATA = _READ_CAPACITY16_DATA
PREAD_CAPACITY16_DATA = POINTER(_READ_CAPACITY16_DATA)


class _LBA_STATUS_DESCRIPTOR(ctypes.Structure):
    pass


LBA_STATUS_DESCRIPTOR = _LBA_STATUS_DESCRIPTOR
PLBA_STATUS_DESCRIPTOR = POINTER(_LBA_STATUS_DESCRIPTOR)


class _LBA_STATUS_LIST_HEADER(ctypes.Structure):
    pass


LBA_STATUS_LIST_HEADER = _LBA_STATUS_LIST_HEADER
PLBA_STATUS_LIST_HEADER = POINTER(_LBA_STATUS_LIST_HEADER)


class _READ_BLOCK_LIMITS(ctypes.Structure):
    pass


READ_BLOCK_LIMITS_DATA = _READ_BLOCK_LIMITS
PREAD_BLOCK_LIMITS_DATA = POINTER(_READ_BLOCK_LIMITS)


class _READ_BUFFER_CAPACITY_DATA(ctypes.Structure):
    pass


READ_BUFFER_CAPACITY_DATA = _READ_BUFFER_CAPACITY_DATA
PREAD_BUFFER_CAPACITY_DATA = POINTER(_READ_BUFFER_CAPACITY_DATA)


class _ZONE_DESCRIPTIOR(ctypes.Structure):
    pass


ZONE_DESCRIPTIOR = _ZONE_DESCRIPTIOR
PZONE_DESCRIPTIOR = POINTER(_ZONE_DESCRIPTIOR)


class _REPORT_ZONES_DATA(ctypes.Structure):
    pass


REPORT_ZONES_DATA = _REPORT_ZONES_DATA
PREPORT_ZONES_DATA = POINTER(_REPORT_ZONES_DATA)


class _MODE_PARAMETER_HEADER(ctypes.Structure):
    pass


MODE_PARAMETER_HEADER = _MODE_PARAMETER_HEADER
PMODE_PARAMETER_HEADER = POINTER(_MODE_PARAMETER_HEADER)


class _MODE_PARAMETER_HEADER10(ctypes.Structure):
    pass


MODE_PARAMETER_HEADER10 = _MODE_PARAMETER_HEADER10
PMODE_PARAMETER_HEADER10 = POINTER(_MODE_PARAMETER_HEADER10)


class _MODE_PARAMETER_BLOCK(ctypes.Structure):
    pass


MODE_PARAMETER_BLOCK = _MODE_PARAMETER_BLOCK
PMODE_PARAMETER_BLOCK = POINTER(_MODE_PARAMETER_BLOCK)


class _MODE_DISCONNECT_PAGE(ctypes.Structure):
    pass


MODE_DISCONNECT_PAGE = _MODE_DISCONNECT_PAGE
PMODE_DISCONNECT_PAGE = POINTER(_MODE_DISCONNECT_PAGE)


class _MODE_CACHING_PAGE(ctypes.Structure):
    pass


MODE_CACHING_PAGE = _MODE_CACHING_PAGE
PMODE_CACHING_PAGE = POINTER(_MODE_CACHING_PAGE)


class _MODE_CACHING_PAGE_EX(ctypes.Structure):
    pass


MODE_CACHING_PAGE_EX = _MODE_CACHING_PAGE_EX
PMODE_CACHING_PAGE_EX = POINTER(_MODE_CACHING_PAGE_EX)


class _MODE_CONTROL_PAGE(ctypes.Structure):
    pass


MODE_CONTROL_PAGE = _MODE_CONTROL_PAGE
PMODE_CONTROL_PAGE = POINTER(_MODE_CONTROL_PAGE)


class _MODE_CDROM_WRITE_PARAMETERS_PAGE2(ctypes.Structure):
    pass


MODE_CDROM_WRITE_PARAMETERS_PAGE2 = _MODE_CDROM_WRITE_PARAMETERS_PAGE2
PMODE_CDROM_WRITE_PARAMETERS_PAGE2 = POINTER(_MODE_CDROM_WRITE_PARAMETERS_PAGE2)


class _MODE_CDROM_WRITE_PARAMETERS_PAGE(ctypes.Structure):
    pass


MODE_CDROM_WRITE_PARAMETERS_PAGE = _MODE_CDROM_WRITE_PARAMETERS_PAGE
PMODE_CDROM_WRITE_PARAMETERS_PAGE = POINTER(_MODE_CDROM_WRITE_PARAMETERS_PAGE)


class _MODE_MRW_PAGE(ctypes.Structure):
    pass


MODE_MRW_PAGE = _MODE_MRW_PAGE
PMODE_MRW_PAGE = POINTER(_MODE_MRW_PAGE)


class _MODE_FLEXIBLE_DISK_PAGE(ctypes.Structure):
    pass


MODE_FLEXIBLE_DISK_PAGE = _MODE_FLEXIBLE_DISK_PAGE
PMODE_FLEXIBLE_DISK_PAGE = POINTER(_MODE_FLEXIBLE_DISK_PAGE)


class _MODE_FORMAT_PAGE(ctypes.Structure):
    pass


MODE_FORMAT_PAGE = _MODE_FORMAT_PAGE
PMODE_FORMAT_PAGE = POINTER(_MODE_FORMAT_PAGE)


class _MODE_RIGID_GEOMETRY_PAGE(ctypes.Structure):
    pass


MODE_RIGID_GEOMETRY_PAGE = _MODE_RIGID_GEOMETRY_PAGE
PMODE_RIGID_GEOMETRY_PAGE = POINTER(_MODE_RIGID_GEOMETRY_PAGE)


class _MODE_READ_WRITE_RECOVERY_PAGE(ctypes.Structure):
    pass


MODE_READ_WRITE_RECOVERY_PAGE = _MODE_READ_WRITE_RECOVERY_PAGE
PMODE_READ_WRITE_RECOVERY_PAGE = POINTER(_MODE_READ_WRITE_RECOVERY_PAGE)


class _MODE_READ_RECOVERY_PAGE(ctypes.Structure):
    pass


MODE_READ_RECOVERY_PAGE = _MODE_READ_RECOVERY_PAGE
PMODE_READ_RECOVERY_PAGE = POINTER(_MODE_READ_RECOVERY_PAGE)


class _MODE_INFO_EXCEPTIONS(ctypes.Structure):
    pass


MODE_INFO_EXCEPTIONS = _MODE_INFO_EXCEPTIONS
PMODE_INFO_EXCEPTIONS = POINTER(_MODE_INFO_EXCEPTIONS)


class _POWER_CONDITION_PAGE(ctypes.Structure):
    pass


POWER_CONDITION_PAGE = _POWER_CONDITION_PAGE
PPOWER_CONDITION_PAGE = POINTER(_POWER_CONDITION_PAGE)


class _CDDA_OUTPUT_PORT(ctypes.Structure):
    pass


CDDA_OUTPUT_PORT = _CDDA_OUTPUT_PORT
PCDDA_OUTPUT_PORT = POINTER(_CDDA_OUTPUT_PORT)


class _CDAUDIO_CONTROL_PAGE(ctypes.Structure):
    pass


CDAUDIO_CONTROL_PAGE = _CDAUDIO_CONTROL_PAGE
PCDAUDIO_CONTROL_PAGE = POINTER(_CDAUDIO_CONTROL_PAGE)


class _CDVD_FEATURE_SET_PAGE(ctypes.Structure):
    pass


CDVD_FEATURE_SET_PAGE = _CDVD_FEATURE_SET_PAGE
PCDVD_FEATURE_SET_PAGE = POINTER(_CDVD_FEATURE_SET_PAGE)


class _CDVD_INACTIVITY_TIMEOUT_PAGE(ctypes.Structure):
    pass


CDVD_INACTIVITY_TIMEOUT_PAGE = _CDVD_INACTIVITY_TIMEOUT_PAGE
PCDVD_INACTIVITY_TIMEOUT_PAGE = POINTER(_CDVD_INACTIVITY_TIMEOUT_PAGE)


class _CDVD_CAPABILITIES_PAGE(ctypes.Structure):
    pass


CDVD_CAPABILITIES_PAGE = _CDVD_CAPABILITIES_PAGE
PCDVD_CAPABILITIES_PAGE = POINTER(_CDVD_CAPABILITIES_PAGE)


class _LUN_LIST(ctypes.Structure):
    pass


LUN_LIST = _LUN_LIST
PLUN_LIST = POINTER(_LUN_LIST)


class _MODE_PARM_READ_WRITE(ctypes.Structure):
    pass


MODE_PARM_READ_WRITE_DATA = _MODE_PARM_READ_WRITE
PMODE_PARM_READ_WRITE_DATA = POINTER(_MODE_PARM_READ_WRITE)


class _PORT_OUTPUT(ctypes.Structure):
    pass


PORT_OUTPUT = _PORT_OUTPUT
PPORT_OUTPUT = POINTER(_PORT_OUTPUT)


class _AUDIO_OUTPUT(ctypes.Structure):
    pass


AUDIO_OUTPUT = _AUDIO_OUTPUT
PAUDIO_OUTPUT = POINTER(_AUDIO_OUTPUT)


class _MECHANICAL_STATUS_INFORMATION_HEADER(ctypes.Structure):
    pass


MECHANICAL_STATUS_INFORMATION_HEADER = _MECHANICAL_STATUS_INFORMATION_HEADER
PMECHANICAL_STATUS_INFORMATION_HEADER = POINTER(_MECHANICAL_STATUS_INFORMATION_HEADER)


class _SLOT_TABLE_INFORMATION(ctypes.Structure):
    pass


SLOT_TABLE_INFORMATION = _SLOT_TABLE_INFORMATION
PSLOT_TABLE_INFORMATION = POINTER(_SLOT_TABLE_INFORMATION)


class _MECHANICAL_STATUS(ctypes.Structure):
    pass


MECHANICAL_STATUS = _MECHANICAL_STATUS
PMECHANICAL_STATUS = POINTER(_MECHANICAL_STATUS)


class _UNMAP_BLOCK_DESCRIPTOR(ctypes.Structure):
    pass


UNMAP_BLOCK_DESCRIPTOR = _UNMAP_BLOCK_DESCRIPTOR
PUNMAP_BLOCK_DESCRIPTOR = POINTER(_UNMAP_BLOCK_DESCRIPTOR)


class _UNMAP_LIST_HEADER(ctypes.Structure):
    pass


UNMAP_LIST_HEADER = _UNMAP_LIST_HEADER
PUNMAP_LIST_HEADER = POINTER(_UNMAP_LIST_HEADER)


class _TAPE_POSITION_DATA(ctypes.Structure):
    pass


TAPE_POSITION_DATA = _TAPE_POSITION_DATA
PTAPE_POSITION_DATA = POINTER(_TAPE_POSITION_DATA)


class _EIGHT_BYTE(ctypes.Union):
    pass


EIGHT_BYTE = _EIGHT_BYTE
PEIGHT_BYTE = POINTER(_EIGHT_BYTE)


class _FOUR_BYTE(ctypes.Union):
    pass


FOUR_BYTE = _FOUR_BYTE
PFOUR_BYTE = POINTER(_FOUR_BYTE)


class _TWO_BYTE(ctypes.Union):
    pass


TWO_BYTE = _TWO_BYTE
PTWO_BYTE = POINTER(_TWO_BYTE)

STOR_ADDRESS_ALIGN = ctypes.Structure


class _STOR_ADDRESS(STOR_ADDRESS_ALIGN):
    pass


STOR_ADDRESS = _STOR_ADDRESS
PSTOR_ADDRESS = POINTER(_STOR_ADDRESS)


class _STOR_ADDR_BTL8(STOR_ADDRESS_ALIGN):
    pass


STOR_ADDR_BTL8 = _STOR_ADDR_BTL8
PSTOR_ADDR_BTL8 = POINTER(_STOR_ADDR_BTL8)


class _SES_DIAGNOSTIC_PAGE(ctypes.Structure):
    pass


SES_DIAGNOSTIC_PAGE = _SES_DIAGNOSTIC_PAGE
PSES_DIAGNOSTIC_PAGE = POINTER(_SES_DIAGNOSTIC_PAGE)


class _SES_TYPE_DESCRIPTOR_HEADER(ctypes.Structure):
    pass


SES_TYPE_DESCRIPTOR_HEADER = _SES_TYPE_DESCRIPTOR_HEADER
PSES_TYPE_DESCRIPTOR_HEADER = POINTER(_SES_TYPE_DESCRIPTOR_HEADER)


class _SES_ENCLOSURE_DESCRIPTOR(ctypes.Structure):
    pass


SES_ENCLOSURE_DESCRIPTOR = _SES_ENCLOSURE_DESCRIPTOR
PSES_ENCLOSURE_DESCRIPTOR = POINTER(_SES_ENCLOSURE_DESCRIPTOR)


class _SES_CONFIGURATION_DIAGNOSTIC_PAGE(ctypes.Structure):
    pass


SES_CONFIGURATION_DIAGNOSTIC_PAGE = _SES_CONFIGURATION_DIAGNOSTIC_PAGE
PSES_CONFIGURATION_DIAGNOSTIC_PAGE = POINTER(_SES_CONFIGURATION_DIAGNOSTIC_PAGE)


class _SES_CONTROL_DESCRIPTOR(ctypes.Structure):
    pass


SES_CONTROL_DESCRIPTOR = _SES_CONTROL_DESCRIPTOR
PSES_CONTROL_DESCRIPTOR = POINTER(_SES_CONTROL_DESCRIPTOR)


class _SES_CONTROL_DIAGNOSTIC_PAGE(ctypes.Structure):
    pass


SES_CONTROL_DIAGNOSTIC_PAGE = _SES_CONTROL_DIAGNOSTIC_PAGE
PSES_CONTROL_DIAGNOSTIC_PAGE = POINTER(_SES_CONTROL_DIAGNOSTIC_PAGE)


class _SES_STATUS_DESCRIPTOR(ctypes.Structure):
    pass


SES_STATUS_DESCRIPTOR = _SES_STATUS_DESCRIPTOR
PSES_STATUS_DESCRIPTOR = POINTER(_SES_STATUS_DESCRIPTOR)


class _SES_STATUS_DIAGNOSTIC_PAGE(ctypes.Structure):
    pass


SES_STATUS_DIAGNOSTIC_PAGE = _SES_STATUS_DIAGNOSTIC_PAGE
PSES_STATUS_DIAGNOSTIC_PAGE = POINTER(_SES_STATUS_DIAGNOSTIC_PAGE)


class _SES_PHY_DESCRIPTOR(ctypes.Structure):
    pass


SES_PHY_DESCRIPTOR = _SES_PHY_DESCRIPTOR
PSES_PHY_DESCRIPTOR = POINTER(_SES_PHY_DESCRIPTOR)


class _SES_SAS_SLOT_INFORMATION(ctypes.Structure):
    pass


SES_SAS_SLOT_INFORMATION = _SES_SAS_SLOT_INFORMATION
PSES_SAS_SLOT_INFORMATION = POINTER(_SES_SAS_SLOT_INFORMATION)


class _SES_PROTOCOL_INFORMATION(ctypes.Union):
    pass


SES_PROTOCOL_INFORMATION = _SES_PROTOCOL_INFORMATION
PSES_PROTOCOL_INFORMATION = POINTER(_SES_PROTOCOL_INFORMATION)


class _SES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR(ctypes.Structure):
    pass


SES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR = _SES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR
PSES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR = POINTER(_SES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR)


class _SES_ADDITIONAL_ELEMENT_STATUS_DIAGNOSTIC_PAGE(ctypes.Structure):
    pass


SES_ADDITIONAL_ELEMENT_STATUS_DIAGNOSTIC_PAGE = _SES_ADDITIONAL_ELEMENT_STATUS_DIAGNOSTIC_PAGE
PSES_ADDITIONAL_ELEMENT_STATUS_DIAGNOSTIC_PAGE = POINTER(_SES_ADDITIONAL_ELEMENT_STATUS_DIAGNOSTIC_PAGE)


class _SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR(ctypes.Structure):
    pass


SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR = _SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR
PSES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR = POINTER(_SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR)


class _SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE(ctypes.Structure):
    pass


SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE = _SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE
PSES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE = POINTER(_SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE)


class _SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE(ctypes.Structure):
    pass


SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE = _SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE
PSES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE = POINTER(_SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE)


class _PHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR(ctypes.Structure):
    pass


PHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR = _PHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR
PPHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR = POINTER(_PHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR)


class _PHYSICAL_ELEMENT_STATUS_PARAMETER_DATA(ctypes.Structure):
    pass


PHYSICAL_ELEMENT_STATUS_PARAMETER_DATA = _PHYSICAL_ELEMENT_STATUS_PARAMETER_DATA
PPHYSICAL_ELEMENT_STATUS_PARAMETER_DATA = POINTER(_PHYSICAL_ELEMENT_STATUS_PARAMETER_DATA)


class _ERROR_HISTORY_DIRECTORY_ENTRY(ctypes.Structure):
    pass


ERROR_HISTORY_DIRECTORY_ENTRY = _ERROR_HISTORY_DIRECTORY_ENTRY
PERROR_HISTORY_DIRECTORY_ENTRY = POINTER(_ERROR_HISTORY_DIRECTORY_ENTRY)


class _ERROR_HISTORY_DIRECTORY(ctypes.Structure):
    pass


ERROR_HISTORY_DIRECTORY = _ERROR_HISTORY_DIRECTORY
PERROR_HISTORY_DIRECTORY = POINTER(_ERROR_HISTORY_DIRECTORY)


class _CURRENT_INTERNAL_STATUS_PARAMETER_DATA(ctypes.Structure):
    pass


CURRENT_INTERNAL_STATUS_PARAMETER_DATA = _CURRENT_INTERNAL_STATUS_PARAMETER_DATA
PCURRENT_INTERNAL_STATUS_PARAMETER_DATA = POINTER(_CURRENT_INTERNAL_STATUS_PARAMETER_DATA)


class _SAVED_INTERNAL_STATUS_PARAMETER_DATA(ctypes.Structure):
    pass


SAVED_INTERNAL_STATUS_PARAMETER_DATA = _SAVED_INTERNAL_STATUS_PARAMETER_DATA
PSAVED_INTERNAL_STATUS_PARAMETER_DATA = POINTER(_SAVED_INTERNAL_STATUS_PARAMETER_DATA)


# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: scsi.h Abstract: These are the structures and defines that are used in
# the SCSI port and class drivers. Authors: Revision History: - -

_NTSCSI_ = None
if not defined(_NTSCSI_):
    _NTSCSI_ = 1
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.shared.winpackagefamily_h import *  # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PKG_STORAGE):
        if not defined(_NTSCSI_USER_MODE_):
            _NTSRB_ = None

            if not defined(_NTSRB_):
                _MINIPORT_ = None

                if not defined(_MINIPORT_):
                    if not defined(_NTDDK_):
                        # For user - mode application development, make sure
                        # to add the line "define _NTSCSI_USER_MODE_" prior to
                        # "include <scsi.h>"
                        # For example,
                        # define _NTSCSI_USER_MODE_
                        # include <scsi.h>
                        # undef _NTSCSI_USER_MODE_
                        # Also see the SPTI sample
                        # (located in src\storage\tools\spti directory under the Windows Kits root directory)
                        #
                        raise RuntimeError(
                            "For user-mode application development, "
                            "make sure to set pyWinAPI._NTSCSI_USER_MODE_ = 1 "
                            "prior to import"
                        )
                    # END IF   not defined _NTDDK_
                # END IF   not defined _MINIPORT_
                from pyWinAPI.shared.srb_h import * # NOQA
            # END IF   not defined _NTSRB_
        # END IF   not defined _NTSCSI_USER_MODE_

        # begin_ntminitape
        # begin_storport begin_storportp
        # Calculate the byte offset of a field in a structure of type type.
        if not defined(FIELD_OFFSET):
            def FIELD_OFFSET(type, field):
                return getattr(type, field)
        # END IF
        # Calculate the size of a field in a structure of type type, without
        # knowing or stating the type of the field.
        if not defined(RTL_FIELD_SIZE):
            def RTL_FIELD_SIZE(type, field):
                return 1
        # END IF

        # Calculate the size of a structure of type type up through and
        # including a field.
        if not defined(RTL_SIZEOF_THROUGH_FIELD):
            def RTL_SIZEOF_THROUGH_FIELD(type, field):
                return FIELD_OFFSET(type, field) + RTL_FIELD_SIZE(type, field)
        # END IF

        # RTL_CONTAINS_FIELD usage:
        # if (RTL_CONTAINS_FIELD(pBlock, pBlock - >cbSize, dwMumble))
        # { // safe to use pBlock - >dwMumble
        if not defined(RTL_CONTAINS_FIELD):
            def RTL_CONTAINS_FIELD(Struct, Size, Field):
                return 1
        # END IF

        if not defined(RtlZeroMemory):
            def RtlZeroMemory(Destination, Length):
                return 1
        # END IF
        # Command Descriptor Block. Passed by SCSI controller chip over the
        # SCSI bus
        class _CDB6GENERIC(ctypes.Structure):
            pass


        _CDB6GENERIC._fields_ = [
            ('OperationCode', UCHAR),
            ('Immediate', UCHAR, 1),
            ('CommandUniqueBits', UCHAR, 4),
            ('LogicalUnitNumber', UCHAR, 3),
            ('CommandUniqueBytes', UCHAR * 3),
            ('Link', UCHAR, 1),
            ('Flag', UCHAR, 1),
            ('Reserved', UCHAR, 4),
            ('VendorUnique', UCHAR, 2),
        ]
        CDB6GENERIC = _CDB6GENERIC
        _CDB.CDB6GENERIC = CDB6GENERIC


        class _CDB6READWRITE(ctypes.Structure):
            pass


        _CDB6READWRITE._fields_ = [
            # 0x08, 0x0A - SCSIOP_READ, SCSIOP_WRITE
            ('OperationCode', UCHAR),
            ('LogicalBlockMsb1', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('LogicalBlockMsb0', UCHAR),
            ('LogicalBlockLsb', UCHAR),
            ('TransferBlocks', UCHAR),
            ('Control', UCHAR),
        ]
        CDB6READWRITE = _CDB6READWRITE
        _CDB.CDB6READWRITE = CDB6READWRITE


        class _CDB6INQUIRY(ctypes.Structure):
            pass


        _CDB6INQUIRY._fields_ = [
            # 0x12 - SCSIOP_INQUIRY
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('PageCode', UCHAR),
            ('IReserved', UCHAR),
            ('AllocationLength', UCHAR),
            ('Control', UCHAR),
        ]
        CDB6INQUIRY = _CDB6INQUIRY
        _CDB.CDB6INQUIRY = CDB6INQUIRY


        class _CDB6INQUIRY3(ctypes.Structure):
            pass


        _CDB6INQUIRY3._fields_ = [
            # 0x12 - SCSIOP_INQUIRY
            ('OperationCode', UCHAR),
            ('EnableVitalProductData', UCHAR, 1),
            ('CommandSupportData', UCHAR, 1),
            ('Reserved1', UCHAR, 6),
            ('PageCode', UCHAR),
            ('Reserved2', UCHAR),
            ('AllocationLength', UCHAR),
            ('Control', UCHAR),
        ]
        CDB6INQUIRY3 = _CDB6INQUIRY3
        _CDB.CDB6INQUIRY3 = CDB6INQUIRY3


        class _CDB6VERIFY(ctypes.Structure):
            pass


        _CDB6VERIFY._fields_ = [
            # 0x13 - SCSIOP_VERIFY
            ('OperationCode', UCHAR),
            ('Fixed', UCHAR, 1),
            ('ByteCompare', UCHAR, 1),
            ('Immediate', UCHAR, 1),
            ('Reserved', UCHAR, 2),
            ('LogicalUnitNumber', UCHAR, 3),
            ('VerificationLength', UCHAR * 3),
            ('Control', UCHAR),
        ]
        CDB6VERIFY = _CDB6VERIFY
        _CDB.CDB6VERIFY = CDB6VERIFY


        class _RECEIVE_DIAGNOSTIC(ctypes.Structure):
            pass


        _RECEIVE_DIAGNOSTIC._fields_ = [
            # 0x1C - SCSIOP_RECEIVE_DIAGNOSTIC
            ('OperationCode', UCHAR),
            ('PageCodeValid', UCHAR, 1),
            ('Reserved', UCHAR, 7),
            ('PageCode', UCHAR),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        RECEIVE_DIAGNOSTIC = _RECEIVE_DIAGNOSTIC
        _CDB.RECEIVE_DIAGNOSTIC = RECEIVE_DIAGNOSTIC


        class _SEND_DIAGNOSTIC(ctypes.Structure):
            pass


        _SEND_DIAGNOSTIC._fields_ = [
            # 0x1D - SCSIOP_SEND_DIAGNOSTIC
            ('OperationCode', UCHAR),
            ('UnitOffline', UCHAR, 1),
            ('DeviceOffline', UCHAR, 1),
            ('SelfTest', UCHAR, 1),
            ('Reserved1', UCHAR, 1),
            ('PageFormat', UCHAR, 1),
            ('SelfTestCode', UCHAR, 3),
            ('Reserved2', UCHAR),
            ('ParameterListLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        SEND_DIAGNOSTIC = _SEND_DIAGNOSTIC
        _CDB.SEND_DIAGNOSTIC = SEND_DIAGNOSTIC


        class _CDB6FORMAT(ctypes.Structure):
            pass


        _CDB6FORMAT._fields_ = [
            # 0x04 - SCSIOP_FORMAT_UNIT
            ('OperationCode', UCHAR),
            ('FormatControl', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('FReserved1', UCHAR),
            ('InterleaveMsb', UCHAR),
            ('InterleaveLsb', UCHAR),
            ('FReserved2', UCHAR),
        ]
        CDB6FORMAT = _CDB6FORMAT
        _CDB.CDB6FORMAT = CDB6FORMAT


        class _CDB10(ctypes.Structure):
            pass


        _CDB10._fields_ = [
            ('OperationCode', UCHAR),
            ('RelativeAddress', UCHAR, 1),
            ('Reserved1', UCHAR, 2),
            ('ForceUnitAccess', UCHAR, 1),
            ('DisablePageOut', UCHAR, 1),
            ('LogicalUnitNumber', UCHAR, 3),
            ('LogicalBlockByte0', UCHAR),
            ('LogicalBlockByte1', UCHAR),
            ('LogicalBlockByte2', UCHAR),
            ('LogicalBlockByte3', UCHAR),
            ('Reserved2', UCHAR),
            ('TransferBlocksMsb', UCHAR),
            ('TransferBlocksLsb', UCHAR),
            ('Control', UCHAR),
        ]
        CDB10 = _CDB10
        _CDB.CDB10 = CDB10


        class _CDB12(ctypes.Structure):
            pass


        _CDB12._fields_ = [
            ('OperationCode', UCHAR),
            ('RelativeAddress', UCHAR, 1),
            ('Reserved1', UCHAR, 2),
            ('ForceUnitAccess', UCHAR, 1),
            ('DisablePageOut', UCHAR, 1),
            ('LogicalUnitNumber', UCHAR, 3),
            ('LogicalBlock', UCHAR * 4),
            ('TransferLength', UCHAR * 4),
            ('Reserved2', UCHAR),
            ('Control', UCHAR),
        ]
        CDB12 = _CDB12
        _CDB.CDB12 = CDB12


        class _CDB16(ctypes.Structure):
            pass


        _CDB16._fields_ = [
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 3),
            ('ForceUnitAccess', UCHAR, 1),
            ('DisablePageOut', UCHAR, 1),
            ('Protection', UCHAR, 3),
            ('LogicalBlock', UCHAR * 8),
            ('TransferLength', UCHAR * 4),
            ('Reserved2', UCHAR),
            ('Control', UCHAR),
        ]
        CDB16 = _CDB16
        _CDB.CDB16 = CDB16


        class _READ_BUFFER_10(ctypes.Structure):
            pass


        _READ_BUFFER_10._fields_ = [
            # 0x3c - SCSIOP_READ_DATA_BUFF
            ('OperationCode', UCHAR),
            ('Mode', UCHAR, 5),
            ('ModeSpecific', UCHAR, 3),
            ('BufferId', UCHAR),
            ('BufferOffset', UCHAR * 3),
            ('AllocationLength', UCHAR * 3),
            ('Control', UCHAR),
        ]
        READ_BUFFER_10 = _READ_BUFFER_10
        _CDB.READ_BUFFER_10 = READ_BUFFER_10


        class _SECURITY_PROTOCOL_IN(ctypes.Structure):
            pass


        _SECURITY_PROTOCOL_IN._fields_ = [
            ('OperationCode', UCHAR),
            ('SecurityProtocol', UCHAR),
            ('SecurityProtocolSpecific', UCHAR * 2),
            ('Reserved1', UCHAR, 7),
            ('INC_512', UCHAR, 1),
            ('Reserved2', UCHAR),
            ('AllocationLength', UCHAR * 4),
            ('Reserved3', UCHAR),
            ('Control', UCHAR),
        ]
        SECURITY_PROTOCOL_IN = _SECURITY_PROTOCOL_IN
        _CDB.SECURITY_PROTOCOL_IN = SECURITY_PROTOCOL_IN


        class _SECURITY_PROTOCOL_OUT(ctypes.Structure):
            pass


        _SECURITY_PROTOCOL_OUT._fields_ = [
            ('OperationCode', UCHAR),
            ('SecurityProtocol', UCHAR),
            ('SecurityProtocolSpecific', UCHAR * 2),
            ('Reserved1', UCHAR, 7),
            ('INC_512', UCHAR, 1),
            ('Reserved2', UCHAR),
            ('AllocationLength', UCHAR * 4),
            ('Reserved3', UCHAR),
            ('Control', UCHAR),
        ]
        SECURITY_PROTOCOL_OUT = _SECURITY_PROTOCOL_OUT
        _CDB.SECURITY_PROTOCOL_OUT = SECURITY_PROTOCOL_OUT


        class _UNMAP(ctypes.Structure):
            pass


        _UNMAP._fields_ = [
            # 0x42 - SCSIOP_UNMAP
            ('OperationCode', UCHAR),
            ('Anchor', UCHAR, 1),
            ('Reserved1', UCHAR, 7),
            ('Reserved2', UCHAR * 4),
            ('GroupNumber', UCHAR, 5),
            ('Reserved3', UCHAR, 3),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        UNMAP = _UNMAP
        _CDB.UNMAP = UNMAP


        class _SANITIZE(ctypes.Structure):
            pass


        _SANITIZE._fields_ = [
            # 0x48 - SCSIOP_SANITIZE
            ('OperationCode', UCHAR),
            ('ServiceAction', UCHAR, 5),
            ('AUSE', UCHAR, 1),
            ('Reserved1', UCHAR, 1),
            ('Immediate', UCHAR, 1),
            ('Reserved2', UCHAR * 5),
            ('ParameterListLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        SANITIZE = _SANITIZE
        _CDB.SANITIZE = SANITIZE


        class _PAUSE_RESUME(ctypes.Structure):
            pass


        _PAUSE_RESUME._fields_ = [
            # 0x4B - SCSIOP_PAUSE_RESUME
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('Reserved2', UCHAR * 6),
            ('Action', UCHAR),
            ('Control', UCHAR),
        ]
        PAUSE_RESUME = _PAUSE_RESUME
        _CDB.PAUSE_RESUME = PAUSE_RESUME


        class _READ_TOC(ctypes.Structure):
            pass


        _READ_TOC._fields_ = [
            # 0x43 - SCSIOP_READ_TOC
            ('OperationCode', UCHAR),
            ('Reserved0', UCHAR, 1),
            ('Msf', UCHAR, 1),
            ('Reserved1', UCHAR, 3),
            ('LogicalUnitNumber', UCHAR, 3),
            ('Format2', UCHAR, 4),
            ('Reserved2', UCHAR, 4),
            ('Reserved3', UCHAR * 3),
            ('StartingTrack', UCHAR),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR, 6),
            ('Format', UCHAR, 2),
        ]
        READ_TOC = _READ_TOC
        _CDB.READ_TOC = READ_TOC


        class _READ_DISK_INFORMATION(ctypes.Structure):
            pass


        _READ_DISK_INFORMATION._fields_ = [
            # 0x51 - SCSIOP_READ_DISC_INFORMATION
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('Lun', UCHAR, 3),
            ('Reserved2', UCHAR * 5),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        READ_DISK_INFORMATION = _READ_DISK_INFORMATION
        _CDB.READ_DISK_INFORMATION = READ_DISK_INFORMATION


        class _READ_TRACK_INFORMATION(ctypes.Structure):
            pass


        _READ_TRACK_INFORMATION._fields_ = [
            # 0x52 - SCSIOP_READ_TRACK_INFORMATION
            ('OperationCode', UCHAR),
            ('Track', UCHAR, 2),
            ('Reserved4', UCHAR, 3),
            ('Lun', UCHAR, 3),
            # or Track Number
            ('BlockAddress', UCHAR * 4),
            ('Reserved3', UCHAR),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        READ_TRACK_INFORMATION = _READ_TRACK_INFORMATION
        _CDB.READ_TRACK_INFORMATION = READ_TRACK_INFORMATION


        class _RESERVE_TRACK_RZONE(ctypes.Structure):
            pass


        _RESERVE_TRACK_RZONE._fields_ = [
            # 0x53 - SCSIOP_RESERVE_TRACK_RZONE
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR * 4),
            ('ReservationSize', UCHAR * 4),
            ('Control', UCHAR),
        ]
        RESERVE_TRACK_RZONE = _RESERVE_TRACK_RZONE
        _CDB.RESERVE_TRACK_RZONE = RESERVE_TRACK_RZONE


        class _SEND_OPC_INFORMATION(ctypes.Structure):
            pass


        _SEND_OPC_INFORMATION._fields_ = [
            # 0x54 - SCSIOP_SEND_OPC_INFORMATION
            ('OperationCode', UCHAR),
            # perform OPC
            ('DoOpc', UCHAR, 1),
            ('Reserved1', UCHAR, 7),
            # exclude layer 0
            ('Exclude0', UCHAR, 1),
            # exclude layer 1
            ('Exclude1', UCHAR, 1),
            ('Reserved2', UCHAR, 6),
            ('Reserved3', UCHAR * 4),
            ('ParameterListLength', UCHAR * 2),
            ('Reserved4', UCHAR),
        ]
        SEND_OPC_INFORMATION = _SEND_OPC_INFORMATION
        _CDB.SEND_OPC_INFORMATION = SEND_OPC_INFORMATION


        class _REPAIR_TRACK(ctypes.Structure):
            pass


        _REPAIR_TRACK._fields_ = [
            # 0x58 - SCSIOP_REPAIR_TRACK
            ('OperationCode', UCHAR),
            ('Immediate', UCHAR, 1),
            ('Reserved1', UCHAR, 7),
            ('Reserved2', UCHAR * 2),
            ('TrackNumber', UCHAR * 2),
            ('Reserved3', UCHAR * 3),
            ('Control', UCHAR),
        ]
        REPAIR_TRACK = _REPAIR_TRACK
        _CDB.REPAIR_TRACK = REPAIR_TRACK


        class _CLOSE_TRACK(ctypes.Structure):
            pass


        _CLOSE_TRACK._fields_ = [
            # 0x5B - SCSIOP_CLOSE_TRACK_SESSION
            ('OperationCode', UCHAR),
            ('Immediate', UCHAR, 1),
            ('Reserved1', UCHAR, 7),
            ('Track', UCHAR, 1),
            ('Session', UCHAR, 1),
            ('Reserved2', UCHAR, 6),
            ('Reserved3', UCHAR),
            ('TrackNumber', UCHAR * 2),
            ('Reserved4', UCHAR * 3),
            ('Control', UCHAR),
        ]
        CLOSE_TRACK = _CLOSE_TRACK
        _CDB.CLOSE_TRACK = CLOSE_TRACK


        class _READ_BUFFER_CAPACITY(ctypes.Structure):
            pass


        _READ_BUFFER_CAPACITY._fields_ = [
            # 0x5C - SCSIOP_READ_BUFFER_CAPACITY
            ('OperationCode', UCHAR),
            ('BlockInfo', UCHAR, 1),
            ('Reserved1', UCHAR, 7),
            ('Reserved2', UCHAR * 5),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        READ_BUFFER_CAPACITY = _READ_BUFFER_CAPACITY
        _CDB.READ_BUFFER_CAPACITY = READ_BUFFER_CAPACITY


        class _SEND_CUE_SHEET(ctypes.Structure):
            pass


        _SEND_CUE_SHEET._fields_ = [
            # 0x5D - SCSIOP_SEND_CUE_SHEET
            ('OperationCode', UCHAR),
            ('Reserved', UCHAR * 5),
            ('CueSheetSize', UCHAR * 3),
            ('Control', UCHAR),
        ]
        SEND_CUE_SHEET = _SEND_CUE_SHEET
        _CDB.SEND_CUE_SHEET = SEND_CUE_SHEET


        class _READ_HEADER(ctypes.Structure):
            pass


        _READ_HEADER._fields_ = [
            # 0x44 - SCSIOP_READ_HEADER
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 1),
            ('Msf', UCHAR, 1),
            ('Reserved2', UCHAR, 3),
            ('Lun', UCHAR, 3),
            ('LogicalBlockAddress', UCHAR * 4),
            ('Reserved3', UCHAR),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        READ_HEADER = _READ_HEADER
        _CDB.READ_HEADER = READ_HEADER


        class _PLAY_AUDIO(ctypes.Structure):
            pass


        _PLAY_AUDIO._fields_ = [
            # 0x45 - SCSIOP_PLAY_AUDIO
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('StartingBlockAddress', UCHAR * 4),
            ('Reserved2', UCHAR),
            ('PlayLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        PLAY_AUDIO = _PLAY_AUDIO
        _CDB.PLAY_AUDIO = PLAY_AUDIO


        class _PLAY_AUDIO_MSF(ctypes.Structure):
            pass


        _PLAY_AUDIO_MSF._fields_ = [
            # 0x47 - SCSIOP_PLAY_AUDIO_MSF
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('Reserved2', UCHAR),
            ('StartingM', UCHAR),
            ('StartingS', UCHAR),
            ('StartingF', UCHAR),
            ('EndingM', UCHAR),
            ('EndingS', UCHAR),
            ('EndingF', UCHAR),
            ('Control', UCHAR),
        ]
        PLAY_AUDIO_MSF = _PLAY_AUDIO_MSF
        _CDB.PLAY_AUDIO_MSF = PLAY_AUDIO_MSF


        class _BLANK_MEDIA(ctypes.Structure):
            pass


        _BLANK_MEDIA._fields_ = [
            # 0xA1 - SCSIOP_BLANK
            ('OperationCode', UCHAR),
            ('BlankType', UCHAR, 3),
            ('Reserved1', UCHAR, 1),
            ('Immediate', UCHAR, 1),
            ('Reserved2', UCHAR, 3),
            ('AddressOrTrack', UCHAR * 4),
            ('Reserved3', UCHAR * 5),
            ('Control', UCHAR),
        ]
        BLANK_MEDIA = _BLANK_MEDIA
        _CDB.BLANK_MEDIA = BLANK_MEDIA


        class _PLAY_CD(ctypes.Structure):
            pass


        class _Union_1(ctypes.Union):
            pass


        class _LBA(ctypes.Structure):
            pass


        _LBA._fields_ = [
            ('StartingBlockAddress', UCHAR * 4),
            ('PlayLength', UCHAR * 4),
        ]
        LBA = _LBA
        _Union_1.LBA = LBA


        class _MSF(ctypes.Structure):
            pass


        _MSF._fields_ = [
            ('Reserved1', UCHAR),
            ('StartingM', UCHAR),
            ('StartingS', UCHAR),
            ('StartingF', UCHAR),
            ('EndingM', UCHAR),
            ('EndingS', UCHAR),
            ('EndingF', UCHAR),
            ('Reserved2', UCHAR),
        ]
        MSF = _MSF
        _Union_1.MSF = MSF


        _Union_1._fields_ = [
            ('LBA', _Union_1.LBA),
            ('MSF', _Union_1.MSF),
        ]
        _PLAY_CD._Union_1 = _Union_1

        _PLAY_CD._anonymous_ = (
            '_Union_1',
        )

        _PLAY_CD._fields_ = [
            # 0xBC - SCSIOP_PLAY_CD
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 1),
            # LBA = 0, MSF = 1
            ('CMSF', UCHAR, 1),
            ('ExpectedSectorType', UCHAR, 3),
            ('Lun', UCHAR, 3),
            ('_Union_1', _PLAY_CD._Union_1),
            ('Audio', UCHAR, 1),
            ('Composite', UCHAR, 1),
            ('Port1', UCHAR, 1),
            ('Port2', UCHAR, 1),
            ('Reserved2', UCHAR, 3),
            ('Speed', UCHAR, 1),
            ('Control', UCHAR),
        ]
        PLAY_CD = _PLAY_CD
        _CDB.PLAY_CD = PLAY_CD


        class _SCAN_CD(ctypes.Structure):
            pass


        _SCAN_CD._fields_ = [
            # 0xBA - SCSIOP_SCAN_CD
            ('OperationCode', UCHAR),
            ('RelativeAddress', UCHAR, 1),
            ('Reserved1', UCHAR, 3),
            ('Direct', UCHAR, 1),
            ('Lun', UCHAR, 3),
            ('StartingAddress', UCHAR * 4),
            ('Reserved2', UCHAR * 3),
            ('Reserved3', UCHAR, 6),
            ('Type', UCHAR, 2),
            ('Reserved4', UCHAR),
            ('Control', UCHAR),
        ]
        SCAN_CD = _SCAN_CD
        _CDB.SCAN_CD = SCAN_CD


        class _STOP_PLAY_SCAN(ctypes.Structure):
            pass


        _STOP_PLAY_SCAN._fields_ = [
            # 0x4E - SCSIOP_STOP_PLAY_SCAN
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('Lun', UCHAR, 3),
            ('Reserved2', UCHAR * 7),
            ('Control', UCHAR),
        ]
        STOP_PLAY_SCAN = _STOP_PLAY_SCAN
        _CDB.STOP_PLAY_SCAN = STOP_PLAY_SCAN


        class _SUBCHANNEL(ctypes.Structure):
            pass


        _SUBCHANNEL._fields_ = [
            # 0x42 - SCSIOP_READ_SUB_CHANNEL
            ('OperationCode', UCHAR),
            ('Reserved0', UCHAR, 1),
            ('Msf', UCHAR, 1),
            ('Reserved1', UCHAR, 3),
            ('LogicalUnitNumber', UCHAR, 3),
            ('Reserved2', UCHAR, 6),
            ('SubQ', UCHAR, 1),
            ('Reserved3', UCHAR, 1),
            ('Format', UCHAR),
            ('Reserved4', UCHAR * 2),
            ('TrackNumber', UCHAR),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        SUBCHANNEL = _SUBCHANNEL
        _CDB.SUBCHANNEL = SUBCHANNEL


        class _READ_CD(ctypes.Structure):
            pass


        _READ_CD._fields_ = [
            # 0xBE - SCSIOP_READ_CD
            ('OperationCode', UCHAR),
            ('RelativeAddress', UCHAR, 1),
            ('Reserved0', UCHAR, 1),
            ('ExpectedSectorType', UCHAR, 3),
            ('Lun', UCHAR, 3),
            ('StartingLBA', UCHAR * 4),
            ('TransferBlocks', UCHAR * 3),
            ('Reserved2', UCHAR, 1),
            ('ErrorFlags', UCHAR, 2),
            ('IncludeEDC', UCHAR, 1),
            ('IncludeUserData', UCHAR, 1),
            ('HeaderCode', UCHAR, 2),
            ('IncludeSyncData', UCHAR, 1),
            ('SubChannelSelection', UCHAR, 3),
            ('Reserved3', UCHAR, 5),
            ('Control', UCHAR),
        ]
        READ_CD = _READ_CD
        _CDB.READ_CD = READ_CD


        class _READ_CD_MSF(ctypes.Structure):
            pass


        _READ_CD_MSF._fields_ = [
            # 0xB9 - SCSIOP_READ_CD_MSF
            ('OperationCode', UCHAR),
            ('RelativeAddress', UCHAR, 1),
            ('Reserved1', UCHAR, 1),
            ('ExpectedSectorType', UCHAR, 3),
            ('Lun', UCHAR, 3),
            ('Reserved2', UCHAR),
            ('StartingM', UCHAR),
            ('StartingS', UCHAR),
            ('StartingF', UCHAR),
            ('EndingM', UCHAR),
            ('EndingS', UCHAR),
            ('EndingF', UCHAR),
            ('Reserved4', UCHAR, 1),
            ('ErrorFlags', UCHAR, 2),
            ('IncludeEDC', UCHAR, 1),
            ('IncludeUserData', UCHAR, 1),
            ('HeaderCode', UCHAR, 2),
            ('IncludeSyncData', UCHAR, 1),
            ('SubChannelSelection', UCHAR, 3),
            ('Reserved5', UCHAR, 5),
            ('Control', UCHAR),
        ]
        READ_CD_MSF = _READ_CD_MSF
        _CDB.READ_CD_MSF = READ_CD_MSF


        class _PLXTR_READ_CDDA(ctypes.Structure):
            pass


        _PLXTR_READ_CDDA._fields_ = [
            # Unknown - - vendor - unique?
            ('OperationCode', UCHAR),
            ('Reserved0', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('LogicalBlockByte0', UCHAR),
            ('LogicalBlockByte1', UCHAR),
            ('LogicalBlockByte2', UCHAR),
            ('LogicalBlockByte3', UCHAR),
            ('TransferBlockByte0', UCHAR),
            ('TransferBlockByte1', UCHAR),
            ('TransferBlockByte2', UCHAR),
            ('TransferBlockByte3', UCHAR),
            ('SubCode', UCHAR),
            ('Control', UCHAR),
        ]
        PLXTR_READ_CDDA = _PLXTR_READ_CDDA
        _CDB.PLXTR_READ_CDDA = PLXTR_READ_CDDA


        class _NEC_READ_CDDA(ctypes.Structure):
            pass


        _NEC_READ_CDDA._fields_ = [
            # Unknown - - vendor - unique?
            ('OperationCode', UCHAR),
            ('Reserved0', UCHAR),
            ('LogicalBlockByte0', UCHAR),
            ('LogicalBlockByte1', UCHAR),
            ('LogicalBlockByte2', UCHAR),
            ('LogicalBlockByte3', UCHAR),
            ('Reserved1', UCHAR),
            ('TransferBlockByte0', UCHAR),
            ('TransferBlockByte1', UCHAR),
            ('Control', UCHAR),
        ]
        NEC_READ_CDDA = _NEC_READ_CDDA
        _CDB.NEC_READ_CDDA = NEC_READ_CDDA

        if NTDDI_VERSION >= NTDDI_WIN8:
            class _MODE_SENSE(ctypes.Structure):
                pass


            _MODE_SENSE._fields_ = [
                # 0x1A - SCSIOP_MODE_SENSE
                ('OperationCode', UCHAR),
                ('Reserved1', UCHAR, 3),
                ('Dbd', UCHAR, 1),
                ('Reserved2', UCHAR, 4),
                ('PageCode', UCHAR, 6),
                ('Pc', UCHAR, 2),
                ('SubPageCode', UCHAR),
                ('AllocationLength', UCHAR),
                ('Control', UCHAR),
            ]
            MODE_SENSE = _MODE_SENSE
            _CDB.MODE_SENSE = MODE_SENSE


            class _MODE_SENSE10(ctypes.Structure):
                pass


            _MODE_SENSE10._fields_ = [
                # 0x5A - SCSIOP_MODE_SENSE10
                ('OperationCode', UCHAR),
                ('Reserved1', UCHAR, 3),
                ('Dbd', UCHAR, 1),
                ('LongLBAAccepted', UCHAR, 1),
                ('Reserved2', UCHAR, 3),
                ('PageCode', UCHAR, 6),
                ('Pc', UCHAR, 2),
                ('SubPageCode', UCHAR),
                ('Reserved3', UCHAR * 3),
                ('AllocationLength', UCHAR * 2),
                ('Control', UCHAR),
            ]
            MODE_SENSE10 = _MODE_SENSE10
            _CDB.MODE_SENSE10 = MODE_SENSE10

        else:
            class _MODE_SENSE(ctypes.Structure):
                pass


            _MODE_SENSE._fields_ = [
                # 0x1A - SCSIOP_MODE_SENSE
                ('OperationCode', UCHAR),
                ('Reserved1', UCHAR, 3),
                ('Dbd', UCHAR, 1),
                ('Reserved2', UCHAR, 1),
                ('LogicalUnitNumber', UCHAR, 3),
                ('PageCode', UCHAR, 6),
                ('Pc', UCHAR, 2),
                ('Reserved3', UCHAR),
                ('AllocationLength', UCHAR),
                ('Control', UCHAR),
            ]
            MODE_SENSE = _MODE_SENSE
            _CDB.MODE_SENSE = MODE_SENSE


            class _MODE_SENSE10(ctypes.Structure):
                pass


            _MODE_SENSE10._fields_ = [
                # 0x5A - SCSIOP_MODE_SENSE10
                ('OperationCode', UCHAR),
                ('Reserved1', UCHAR, 3),
                ('Dbd', UCHAR, 1),
                ('Reserved2', UCHAR, 1),
                ('LogicalUnitNumber', UCHAR, 3),
                ('PageCode', UCHAR, 6),
                ('Pc', UCHAR, 2),
                ('Reserved3', UCHAR * 4),
                ('AllocationLength', UCHAR * 2),
                ('Control', UCHAR),
            ]
            MODE_SENSE10 = _MODE_SENSE10
            _CDB.MODE_SENSE10 = MODE_SENSE10

        # END IF

        class _MODE_SELECT(ctypes.Structure):
            pass


        _MODE_SELECT._fields_ = [
            # 0x15 - SCSIOP_MODE_SELECT
            ('OperationCode', UCHAR),
            ('SPBit', UCHAR, 1),
            ('Reserved1', UCHAR, 3),
            ('PFBit', UCHAR, 1),
            ('LogicalUnitNumber', UCHAR, 3),
            ('Reserved2', UCHAR * 2),
            ('ParameterListLength', UCHAR),
            ('Control', UCHAR),
        ]
        MODE_SELECT = _MODE_SELECT
        _CDB.MODE_SELECT = MODE_SELECT


        class _MODE_SELECT10(ctypes.Structure):
            pass


        _MODE_SELECT10._fields_ = [
            # 0x55 - SCSIOP_MODE_SELECT10
            ('OperationCode', UCHAR),
            ('SPBit', UCHAR, 1),
            ('Reserved1', UCHAR, 3),
            ('PFBit', UCHAR, 1),
            ('LogicalUnitNumber', UCHAR, 3),
            ('Reserved2', UCHAR * 5),
            ('ParameterListLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        MODE_SELECT10 = _MODE_SELECT10
        _CDB.MODE_SELECT10 = MODE_SELECT10


        class _LOCATE(ctypes.Structure):
            pass


        _LOCATE._fields_ = [
            # 0x2B - SCSIOP_LOCATE
            ('OperationCode', UCHAR),
            ('Immediate', UCHAR, 1),
            ('CPBit', UCHAR, 1),
            ('BTBit', UCHAR, 1),
            ('Reserved1', UCHAR, 2),
            ('LogicalUnitNumber', UCHAR, 3),
            ('Reserved3', UCHAR),
            ('LogicalBlockAddress', UCHAR * 4),
            ('Reserved4', UCHAR),
            ('Partition', UCHAR),
            ('Control', UCHAR),
        ]
        LOCATE = _LOCATE
        _CDB.LOCATE = LOCATE


        class _LOGSENSE(ctypes.Structure):
            pass


        class _Union_1(ctypes.Union):
            pass


        _Union_1._fields_ = [
            ('SubPageCode', UCHAR),
            ('Reserved2', UCHAR),
        ]
        _LOGSENSE._Union_1 = _Union_1

        _LOGSENSE._anonymous_ = (
            '_Union_1',
        )

        _LOGSENSE._fields_ = [
            # 0x4D - SCSIOP_LOG_SENSE
            ('OperationCode', UCHAR),
            ('SPBit', UCHAR, 1),
            ('PPCBit', UCHAR, 1),
            ('Reserved1', UCHAR, 3),
            ('LogicalUnitNumber', UCHAR, 3),
            ('PageCode', UCHAR, 6),
            ('PCBit', UCHAR, 2),
            ('_Union_1', _LOGSENSE._Union_1),
            ('Reserved3', UCHAR),
            ('ParameterPointer', UCHAR * 2),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        LOGSENSE = _LOGSENSE
        _CDB.LOGSENSE = LOGSENSE


        class _LOGSELECT(ctypes.Structure):
            pass


        _LOGSELECT._fields_ = [
            # 0x4C - SCSIOP_LOG_SELECT
            ('OperationCode', UCHAR),
            ('SPBit', UCHAR, 1),
            ('PCRBit', UCHAR, 1),
            ('Reserved1', UCHAR, 3),
            ('LogicalUnitNumber', UCHAR, 3),
            ('Reserved', UCHAR, 6),
            ('PCBit', UCHAR, 2),
            ('Reserved2', UCHAR * 4),
            ('ParameterListLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        LOGSELECT = _LOGSELECT
        _CDB.LOGSELECT = LOGSELECT


        class _PRINT(ctypes.Structure):
            pass


        _PRINT._fields_ = [
            # 0x0A - SCSIOP_PRINT
            ('OperationCode', UCHAR),
            ('Reserved', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('TransferLength', UCHAR * 3),
            ('Control', UCHAR),
        ]
        PRINT = _PRINT
        _CDB.PRINT = PRINT


        class _SEEK(ctypes.Structure):
            pass


        _SEEK._fields_ = [
            # 0x2B - SCSIOP_SEEK
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('LogicalBlockAddress', UCHAR * 4),
            ('Reserved2', UCHAR * 3),
            ('Control', UCHAR),
        ]
        SEEK = _SEEK
        _CDB.SEEK = SEEK


        class _ERASE(ctypes.Structure):
            pass


        _ERASE._fields_ = [
            # 0x19 - SCSIOP_ERASE
            ('OperationCode', UCHAR),
            ('Long', UCHAR, 1),
            ('Immediate', UCHAR, 1),
            ('Reserved1', UCHAR, 3),
            ('LogicalUnitNumber', UCHAR, 3),
            ('Reserved2', UCHAR * 3),
            ('Control', UCHAR),
        ]
        ERASE = _ERASE
        _CDB.ERASE = ERASE


        class _START_STOP(ctypes.Structure):
            pass


        _START_STOP._fields_ = [
            # 0x1B - SCSIOP_START_STOP_UNIT
            ('OperationCode', UCHAR),
            ('Immediate', UCHAR, 1),
            ('Reserved1', UCHAR, 4),
            ('LogicalUnitNumber', UCHAR, 3),
            ('Reserved2', UCHAR * 2),
            ('Start', UCHAR, 1),
            ('LoadEject', UCHAR, 1),
            ('Reserved3', UCHAR, 6),
            ('Control', UCHAR),
        ]
        START_STOP = _START_STOP
        _CDB.START_STOP = START_STOP


        class _MEDIA_REMOVAL(ctypes.Structure):
            pass


        _MEDIA_REMOVAL._fields_ = [
            # 0x1E - SCSIOP_MEDIUM_REMOVAL
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('Reserved2', UCHAR * 2),
            ('Prevent', UCHAR, 1),
            ('Persistant', UCHAR, 1),
            ('Reserved3', UCHAR, 6),
            ('Control', UCHAR),
        ]
        MEDIA_REMOVAL = _MEDIA_REMOVAL
        _CDB.MEDIA_REMOVAL = MEDIA_REMOVAL


        class _SEEK_BLOCK(ctypes.Structure):
            pass


        _SEEK_BLOCK._fields_ = [
            # 0x0C - SCSIOP_SEEK_BLOCK
            ('OperationCode', UCHAR),
            ('Immediate', UCHAR, 1),
            ('Reserved1', UCHAR, 7),
            ('BlockAddress', UCHAR * 3),
            ('Link', UCHAR, 1),
            ('Flag', UCHAR, 1),
            ('Reserved2', UCHAR, 4),
            ('VendorUnique', UCHAR, 2),
        ]
        SEEK_BLOCK = _SEEK_BLOCK
        _CDB.SEEK_BLOCK = SEEK_BLOCK


        class _REQUEST_BLOCK_ADDRESS(ctypes.Structure):
            pass


        _REQUEST_BLOCK_ADDRESS._fields_ = [
            # 0x02 - SCSIOP_REQUEST_BLOCK_ADDR
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR * 3),
            ('AllocationLength', UCHAR),
            ('Link', UCHAR, 1),
            ('Flag', UCHAR, 1),
            ('Reserved2', UCHAR, 4),
            ('VendorUnique', UCHAR, 2),
        ]
        REQUEST_BLOCK_ADDRESS = _REQUEST_BLOCK_ADDRESS
        _CDB.REQUEST_BLOCK_ADDRESS = REQUEST_BLOCK_ADDRESS


        class _PARTITION(ctypes.Structure):
            pass


        _PARTITION._fields_ = [
            # 0x0D - SCSIOP_PARTITION
            ('OperationCode', UCHAR),
            ('Immediate', UCHAR, 1),
            ('Sel', UCHAR, 1),
            ('PartitionSelect', UCHAR, 6),
            ('Reserved1', UCHAR * 3),
            ('Control', UCHAR),
        ]
        PARTITION = _PARTITION
        _CDB.PARTITION = PARTITION


        class _WRITE_TAPE_MARKS(ctypes.Structure):
            pass


        _WRITE_TAPE_MARKS._fields_ = [
            # Unknown - - vendor - unique?
            ('OperationCode', UCHAR),
            ('Immediate', UCHAR, 1),
            ('WriteSetMarks', UCHAR, 1),
            ('Reserved', UCHAR, 3),
            ('LogicalUnitNumber', UCHAR, 3),
            ('TransferLength', UCHAR * 3),
            ('Control', UCHAR),
        ]
        WRITE_TAPE_MARKS = _WRITE_TAPE_MARKS
        _CDB.WRITE_TAPE_MARKS = WRITE_TAPE_MARKS


        class _SPACE_TAPE_MARKS(ctypes.Structure):
            pass


        class Byte6(ctypes.Union):
            pass


        class Fields(ctypes.Structure):
            pass


        Fields._fields_ = [
            ('Link', UCHAR, 1),
            ('Flag', UCHAR, 1),
            ('Reserved', UCHAR, 4),
            ('VendorUnique', UCHAR, 2),
        ]
        Byte6.Fields = Fields


        Byte6._fields_ = [
            ('value', UCHAR),
            ('Fields', Byte6.Fields),
        ]
        _SPACE_TAPE_MARKS.Byte6 = Byte6


        _SPACE_TAPE_MARKS._fields_ = [
            # Unknown - - vendor - unique?
            ('OperationCode', UCHAR),
            ('Code', UCHAR, 3),
            ('Reserved', UCHAR, 2),
            ('LogicalUnitNumber', UCHAR, 3),
            ('NumMarksMSB', UCHAR),
            ('NumMarks', UCHAR),
            ('NumMarksLSB', UCHAR),
            ('Byte6', _SPACE_TAPE_MARKS.Byte6),
        ]
        SPACE_TAPE_MARKS = _SPACE_TAPE_MARKS
        _CDB.SPACE_TAPE_MARKS = SPACE_TAPE_MARKS


        class _READ_POSITION(ctypes.Structure):
            pass


        _READ_POSITION._fields_ = [
            # 0x43 - SCSIOP_READ_POSITION
            ('Operation', UCHAR),
            ('BlockType', UCHAR, 1),
            ('Reserved1', UCHAR, 4),
            ('Lun', UCHAR, 3),
            ('Reserved2', UCHAR * 7),
            ('Control', UCHAR),
        ]
        READ_POSITION = _READ_POSITION
        _CDB.READ_POSITION = READ_POSITION


        class _CDB6READWRITETAPE(ctypes.Structure):
            pass


        _CDB6READWRITETAPE._fields_ = [
            # Unknown - - vendor - unique?
            ('OperationCode', UCHAR),
            ('VendorSpecific', UCHAR, 5),
            ('Reserved', UCHAR, 3),
            ('TransferLenMSB', UCHAR),
            ('TransferLen', UCHAR),
            ('TransferLenLSB', UCHAR),
            ('Link', UCHAR, 1),
            ('Flag', UCHAR, 1),
            ('Reserved1', UCHAR, 4),
            ('VendorUnique', UCHAR, 2),
        ]
        CDB6READWRITETAPE = _CDB6READWRITETAPE
        _CDB.CDB6READWRITETAPE = CDB6READWRITETAPE


        class _INIT_ELEMENT_STATUS(ctypes.Structure):
            pass


        _INIT_ELEMENT_STATUS._fields_ = [
            # 0x07 - SCSIOP_INIT_ELEMENT_STATUS
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('LogicalUnitNubmer', UCHAR, 3),
            ('Reserved2', UCHAR * 3),
            ('Reserved3', UCHAR, 7),
            ('NoBarCode', UCHAR, 1),
        ]
        INIT_ELEMENT_STATUS = _INIT_ELEMENT_STATUS
        _CDB.INIT_ELEMENT_STATUS = INIT_ELEMENT_STATUS


        class _INITIALIZE_ELEMENT_RANGE(ctypes.Structure):
            pass


        _INITIALIZE_ELEMENT_RANGE._fields_ = [
            # 0xE7 - SCSIOP_INIT_ELEMENT_RANGE
            ('OperationCode', UCHAR),
            ('Range', UCHAR, 1),
            ('Reserved1', UCHAR, 4),
            ('LogicalUnitNubmer', UCHAR, 3),
            ('FirstElementAddress', UCHAR * 2),
            ('Reserved2', UCHAR * 2),
            ('NumberOfElements', UCHAR * 2),
            ('Reserved3', UCHAR),
            ('Reserved4', UCHAR, 7),
            ('NoBarCode', UCHAR, 1),
        ]
        INITIALIZE_ELEMENT_RANGE = _INITIALIZE_ELEMENT_RANGE
        _CDB.INITIALIZE_ELEMENT_RANGE = INITIALIZE_ELEMENT_RANGE


        class _POSITION_TO_ELEMENT(ctypes.Structure):
            pass


        _POSITION_TO_ELEMENT._fields_ = [
            # 0x2B - SCSIOP_POSITION_TO_ELEMENT
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('TransportElementAddress', UCHAR * 2),
            ('DestinationElementAddress', UCHAR * 2),
            ('Reserved2', UCHAR * 2),
            ('Flip', UCHAR, 1),
            ('Reserved3', UCHAR, 7),
            ('Control', UCHAR),
        ]
        POSITION_TO_ELEMENT = _POSITION_TO_ELEMENT
        _CDB.POSITION_TO_ELEMENT = POSITION_TO_ELEMENT


        class _MOVE_MEDIUM(ctypes.Structure):
            pass


        _MOVE_MEDIUM._fields_ = [
            # 0xA5 - SCSIOP_MOVE_MEDIUM
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('TransportElementAddress', UCHAR * 2),
            ('SourceElementAddress', UCHAR * 2),
            ('DestinationElementAddress', UCHAR * 2),
            ('Reserved2', UCHAR * 2),
            ('Flip', UCHAR, 1),
            ('Reserved3', UCHAR, 7),
            ('Control', UCHAR),
        ]
        MOVE_MEDIUM = _MOVE_MEDIUM
        _CDB.MOVE_MEDIUM = MOVE_MEDIUM


        class _EXCHANGE_MEDIUM(ctypes.Structure):
            pass


        _EXCHANGE_MEDIUM._fields_ = [
            # 0xA6 - SCSIOP_EXCHANGE_MEDIUM
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('LogicalUnitNumber', UCHAR, 3),
            ('TransportElementAddress', UCHAR * 2),
            ('SourceElementAddress', UCHAR * 2),
            ('Destination1ElementAddress', UCHAR * 2),
            ('Destination2ElementAddress', UCHAR * 2),
            ('Flip1', UCHAR, 1),
            ('Flip2', UCHAR, 1),
            ('Reserved3', UCHAR, 6),
            ('Control', UCHAR),
        ]
        EXCHANGE_MEDIUM = _EXCHANGE_MEDIUM
        _CDB.EXCHANGE_MEDIUM = EXCHANGE_MEDIUM


        class _READ_ELEMENT_STATUS(ctypes.Structure):
            pass


        _READ_ELEMENT_STATUS._fields_ = [
            # 0xB8 - SCSIOP_READ_ELEMENT_STATUS
            ('OperationCode', UCHAR),
            ('ElementType', UCHAR, 4),
            ('VolTag', UCHAR, 1),
            ('LogicalUnitNumber', UCHAR, 3),
            ('StartingElementAddress', UCHAR * 2),
            ('NumberOfElements', UCHAR * 2),
            ('Reserved1', UCHAR),
            ('AllocationLength', UCHAR * 3),
            ('Reserved2', UCHAR),
            ('Control', UCHAR),
        ]
        READ_ELEMENT_STATUS = _READ_ELEMENT_STATUS
        _CDB.READ_ELEMENT_STATUS = READ_ELEMENT_STATUS


        class _SEND_VOLUME_TAG(ctypes.Structure):
            pass


        _SEND_VOLUME_TAG._fields_ = [
            # 0xB6 - SCSIOP_SEND_VOLUME_TAG
            ('OperationCode', UCHAR),
            ('ElementType', UCHAR, 4),
            ('Reserved1', UCHAR, 1),
            ('LogicalUnitNumber', UCHAR, 3),
            ('StartingElementAddress', UCHAR * 2),
            ('Reserved2', UCHAR),
            ('ActionCode', UCHAR, 5),
            ('Reserved3', UCHAR, 3),
            ('Reserved4', UCHAR * 2),
            ('ParameterListLength', UCHAR * 2),
            ('Reserved5', UCHAR),
            ('Control', UCHAR),
        ]
        SEND_VOLUME_TAG = _SEND_VOLUME_TAG
        _CDB.SEND_VOLUME_TAG = SEND_VOLUME_TAG


        class _REQUEST_VOLUME_ELEMENT_ADDRESS(ctypes.Structure):
            pass


        _REQUEST_VOLUME_ELEMENT_ADDRESS._fields_ = [
            # Unknown - - vendor - unique?
            ('OperationCode', UCHAR),
            ('ElementType', UCHAR, 4),
            ('VolTag', UCHAR, 1),
            ('LogicalUnitNumber', UCHAR, 3),
            ('StartingElementAddress', UCHAR * 2),
            ('NumberElements', UCHAR * 2),
            ('Reserved1', UCHAR),
            ('AllocationLength', UCHAR * 3),
            ('Reserved2', UCHAR),
            ('Control', UCHAR),
        ]
        REQUEST_VOLUME_ELEMENT_ADDRESS = _REQUEST_VOLUME_ELEMENT_ADDRESS
        _CDB.REQUEST_VOLUME_ELEMENT_ADDRESS = REQUEST_VOLUME_ELEMENT_ADDRESS


        class _LOAD_UNLOAD(ctypes.Structure):
            pass


        _LOAD_UNLOAD._fields_ = [
            # 0xA6 - SCSIOP_LOAD_UNLOAD_SLOT
            ('OperationCode', UCHAR),
            ('Immediate', UCHAR, 1),
            ('Reserved1', UCHAR, 4),
            ('Lun', UCHAR, 3),
            ('Reserved2', UCHAR * 2),
            ('Start', UCHAR, 1),
            ('LoadEject', UCHAR, 1),
            ('Reserved3', UCHAR, 6),
            ('Reserved4', UCHAR * 3),
            ('Slot', UCHAR),
            ('Reserved5', UCHAR * 3),
        ]
        LOAD_UNLOAD = _LOAD_UNLOAD
        _CDB.LOAD_UNLOAD = LOAD_UNLOAD


        class _MECH_STATUS(ctypes.Structure):
            pass


        _MECH_STATUS._fields_ = [
            # 0xBD - SCSIOP_MECHANISM_STATUS
            ('OperationCode', UCHAR),
            ('Reserved', UCHAR, 5),
            ('Lun', UCHAR, 3),
            ('Reserved1', UCHAR * 6),
            ('AllocationLength', UCHAR * 2),
            ('Reserved2', UCHAR * 1),
            ('Control', UCHAR),
        ]
        MECH_STATUS = _MECH_STATUS
        _CDB.MECH_STATUS = MECH_STATUS


        class _SYNCHRONIZE_CACHE10(ctypes.Structure):
            pass


        _SYNCHRONIZE_CACHE10._fields_ = [
            # 0x35 - SCSIOP_SYNCHRONIZE_CACHE
            ('OperationCode', UCHAR),
            ('RelAddr', UCHAR, 1),
            ('Immediate', UCHAR, 1),
            ('Reserved', UCHAR, 3),
            ('Lun', UCHAR, 3),
            # Unused - set to zero
            ('LogicalBlockAddress', UCHAR * 4),
            ('Reserved2', UCHAR),
            # Unused - set to zero
            ('BlockCount', UCHAR * 2),
            ('Control', UCHAR),
        ]
        SYNCHRONIZE_CACHE10 = _SYNCHRONIZE_CACHE10
        _CDB.SYNCHRONIZE_CACHE10 = SYNCHRONIZE_CACHE10


        class _GET_EVENT_STATUS_NOTIFICATION(ctypes.Structure):
            pass


        _GET_EVENT_STATUS_NOTIFICATION._fields_ = [
            # 0x4A - SCSIOP_GET_EVENT_STATUS_NOTIFICATION
            ('OperationCode', UCHAR),
            ('Immediate', UCHAR, 1),
            ('Reserved', UCHAR, 4),
            ('Lun', UCHAR, 3),
            ('Reserved2', UCHAR * 2),
            ('NotificationClassRequest', UCHAR),
            ('Reserved3', UCHAR * 2),
            ('EventListLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        GET_EVENT_STATUS_NOTIFICATION = _GET_EVENT_STATUS_NOTIFICATION
        _CDB.GET_EVENT_STATUS_NOTIFICATION = GET_EVENT_STATUS_NOTIFICATION


        class _GET_PERFORMANCE(ctypes.Structure):
            pass


        _GET_PERFORMANCE._fields_ = [
            # 0xAC - SCSIOP_GET_PERFORMANCE
            ('OperationCode', UCHAR),
            ('Except', UCHAR, 2),
            ('Write', UCHAR, 1),
            ('Tolerance', UCHAR, 2),
            ('Reserved0', UCHAR, 3),
            ('StartingLBA', UCHAR * 4),
            ('Reserved1', UCHAR * 2),
            ('MaximumNumberOfDescriptors', UCHAR * 2),
            ('Type', UCHAR),
            ('Control', UCHAR),
        ]
        GET_PERFORMANCE = _GET_PERFORMANCE
        _CDB.GET_PERFORMANCE = GET_PERFORMANCE


        class _READ_DVD_STRUCTURE(ctypes.Structure):
            pass


        _READ_DVD_STRUCTURE._fields_ = [
            # 0xAD - SCSIOP_READ_DVD_STRUCTURE
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('Lun', UCHAR, 3),
            ('RMDBlockNumber', UCHAR * 4),
            ('LayerNumber', UCHAR),
            ('Format', UCHAR),
            ('AllocationLength', UCHAR * 2),
            ('Reserved3', UCHAR, 6),
            ('AGID', UCHAR, 2),
            ('Control', UCHAR),
        ]
        READ_DVD_STRUCTURE = _READ_DVD_STRUCTURE
        _CDB.READ_DVD_STRUCTURE = READ_DVD_STRUCTURE


        class _SET_STREAMING(ctypes.Structure):
            pass


        _SET_STREAMING._fields_ = [
            # 0xB6 - SCSIOP_SET_STREAMING
            ('OperationCode', UCHAR),
            ('Reserved', UCHAR * 8),
            ('ParameterListLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        SET_STREAMING = _SET_STREAMING
        _CDB.SET_STREAMING = SET_STREAMING


        class _SEND_DVD_STRUCTURE(ctypes.Structure):
            pass


        _SEND_DVD_STRUCTURE._fields_ = [
            # 0xBF - SCSIOP_SEND_DVD_STRUCTURE
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('Lun', UCHAR, 3),
            ('Reserved2', UCHAR * 5),
            ('Format', UCHAR),
            ('ParameterListLength', UCHAR * 2),
            ('Reserved3', UCHAR),
            ('Control', UCHAR),
        ]
        SEND_DVD_STRUCTURE = _SEND_DVD_STRUCTURE
        _CDB.SEND_DVD_STRUCTURE = SEND_DVD_STRUCTURE


        class _SEND_KEY(ctypes.Structure):
            pass


        _SEND_KEY._fields_ = [
            # 0xA3 - SCSIOP_SEND_KEY
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('Lun', UCHAR, 3),
            ('Reserved2', UCHAR * 6),
            ('ParameterListLength', UCHAR * 2),
            ('KeyFormat', UCHAR, 6),
            ('AGID', UCHAR, 2),
            ('Control', UCHAR),
        ]
        SEND_KEY = _SEND_KEY
        _CDB.SEND_KEY = SEND_KEY


        class _REPORT_KEY(ctypes.Structure):
            pass


        _REPORT_KEY._fields_ = [
            # 0xA4 - SCSIOP_REPORT_KEY
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('Lun', UCHAR, 3),
            # for title key
            ('LogicalBlockAddress', UCHAR * 4),
            ('Reserved2', UCHAR * 2),
            ('AllocationLength', UCHAR * 2),
            ('KeyFormat', UCHAR, 6),
            ('AGID', UCHAR, 2),
            ('Control', UCHAR),
        ]
        REPORT_KEY = _REPORT_KEY
        _CDB.REPORT_KEY = REPORT_KEY


        class _SET_READ_AHEAD(ctypes.Structure):
            pass


        _SET_READ_AHEAD._fields_ = [
            # 0xA7 - SCSIOP_SET_READ_AHEAD
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('Lun', UCHAR, 3),
            ('TriggerLBA', UCHAR * 4),
            ('ReadAheadLBA', UCHAR * 4),
            ('Reserved2', UCHAR),
            ('Control', UCHAR),
        ]
        SET_READ_AHEAD = _SET_READ_AHEAD
        _CDB.SET_READ_AHEAD = SET_READ_AHEAD


        class _READ_FORMATTED_CAPACITIES(ctypes.Structure):
            pass


        _READ_FORMATTED_CAPACITIES._fields_ = [
            # 0x23 - SCSIOP_READ_FORMATTED_CAPACITY
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 5),
            ('Lun', UCHAR, 3),
            ('Reserved2', UCHAR * 5),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        READ_FORMATTED_CAPACITIES = _READ_FORMATTED_CAPACITIES
        _CDB.READ_FORMATTED_CAPACITIES = READ_FORMATTED_CAPACITIES


        class _REPORT_LUNS(ctypes.Structure):
            pass


        _REPORT_LUNS._fields_ = [
            # 0xA0 - SCSIOP_REPORT_LUNS
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR * 5),
            ('AllocationLength', UCHAR * 4),
            ('Reserved2', UCHAR * 1),
            ('Control', UCHAR),
        ]
        REPORT_LUNS = _REPORT_LUNS
        _CDB.REPORT_LUNS = REPORT_LUNS


        class _PERSISTENT_RESERVE_IN(ctypes.Structure):
            pass


        _PERSISTENT_RESERVE_IN._fields_ = [
            # 0x5E - SCSIOP_PERSISTENT_RESERVE_IN
            ('OperationCode', UCHAR),
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('Reserved2', UCHAR * 5),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        PERSISTENT_RESERVE_IN = _PERSISTENT_RESERVE_IN
        _CDB.PERSISTENT_RESERVE_IN = PERSISTENT_RESERVE_IN


        class _PERSISTENT_RESERVE_OUT(ctypes.Structure):
            pass


        _PERSISTENT_RESERVE_OUT._fields_ = [
            # 0x5F - SCSIOP_PERSISTENT_RESERVE_OUT
            ('OperationCode', UCHAR),
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('Type', UCHAR, 4),
            ('Scope', UCHAR, 4),
            ('Reserved2', UCHAR * 4),
            # 0x18
            ('ParameterListLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        PERSISTENT_RESERVE_OUT = _PERSISTENT_RESERVE_OUT
        _CDB.PERSISTENT_RESERVE_OUT = PERSISTENT_RESERVE_OUT


        class _REPORT_TIMESTAMP(ctypes.Structure):
            pass


        _REPORT_TIMESTAMP._fields_ = [
            # Byte 0 : SCSIOP_MAINTENANCE_IN
            ('OperationCode', UCHAR),
            # Byte 1, bit 0 - 4 : SERVICE_ACTION_REPORT_TIMESTAMP
            ('ServiceAction', UCHAR, 5),
            # Byte 1, bit 5 - 7
            ('Reserved1', UCHAR, 3),
            # Byte 2 - 5
            ('Reserved2', UCHAR * 4),
            # Byte 6 - 9
            ('AllocationLength', UCHAR * 4),
            # Byte 10
            ('Reserved3', UCHAR),
            # Byte 11
            ('Control', UCHAR),
        ]
        REPORT_TIMESTAMP = _REPORT_TIMESTAMP
        _CDB.REPORT_TIMESTAMP = REPORT_TIMESTAMP


        class _SET_TIMESTAMP(ctypes.Structure):
            pass


        _SET_TIMESTAMP._fields_ = [
            # Byte 0 : SCSIOP_MAINTENANCE_OUT
            ('OperationCode', UCHAR),
            # Byte 1, bit 0 - 4 : SERVICE_ACTION_SET_TIMESTAMP
            ('ServiceAction', UCHAR, 5),
            # Byte 1, bit 5 - 7
            ('Reserved1', UCHAR, 3),
            # Byte 2 - 5
            ('Reserved2', UCHAR * 4),
            # Byte 6 - 9
            ('ParameterListLength', UCHAR * 4),
            # Byte 10
            ('Reserved3', UCHAR),
            # Byte 11
            ('Control', UCHAR),
        ]
        SET_TIMESTAMP = _SET_TIMESTAMP
        _CDB.SET_TIMESTAMP = SET_TIMESTAMP


        class _GET_CONFIGURATION(ctypes.Structure):
            pass


        _GET_CONFIGURATION._fields_ = [
            # 0x46 - SCSIOP_GET_CONFIGURATION
            ('OperationCode', UCHAR),
            # SCSI_GET_CONFIGURATION_REQUEST_TYPE_*
            ('RequestType', UCHAR, 2),
            # includes obsolete LUN field
            ('Reserved1', UCHAR, 6),
            ('StartingFeature', UCHAR * 2),
            ('Reserved2', UCHAR * 3),
            ('AllocationLength', UCHAR * 2),
            ('Control', UCHAR),
        ]
        GET_CONFIGURATION = _GET_CONFIGURATION
        _CDB.GET_CONFIGURATION = GET_CONFIGURATION


        class _SET_CD_SPEED(ctypes.Structure):
            pass


        class _Union_1(ctypes.Union):
            pass


        class _Struct_1(ctypes.Structure):
            pass


        _Struct_1._fields_ = [
            ('RotationControl', UCHAR, 2),
            ('Reserved3', UCHAR, 6),
        ]
        _Union_1._Struct_1 = _Struct_1

        _Union_1._anonymous_ = (
            '_Struct_1',
        )

        _Union_1._fields_ = [
            ('Reserved1', UCHAR),
            ('_Struct_1', _Union_1._Struct_1),
        ]
        _SET_CD_SPEED._Union_1 = _Union_1

        _SET_CD_SPEED._anonymous_ = (
            '_Union_1',
        )

        _SET_CD_SPEED._fields_ = [
            # 0xB8 - SCSIOP_SET_CD_SPEED
            ('OperationCode', UCHAR),
            ('_Union_1', _SET_CD_SPEED._Union_1),
            # 1x == (75 * 2352)
            ('ReadSpeed', UCHAR * 2),
            # 1x == (75 * 2352)
            ('WriteSpeed', UCHAR * 2),
            ('Reserved2', UCHAR * 5),
            ('Control', UCHAR),
        ]
        SET_CD_SPEED = _SET_CD_SPEED
        _CDB.SET_CD_SPEED = SET_CD_SPEED


        class _READ12(ctypes.Structure):
            pass


        _READ12._fields_ = [
            # 0xA8 - SCSIOP_READ12
            ('OperationCode', UCHAR),
            ('RelativeAddress', UCHAR, 1),
            ('Reserved1', UCHAR, 2),
            ('ForceUnitAccess', UCHAR, 1),
            ('DisablePageOut', UCHAR, 1),
            ('LogicalUnitNumber', UCHAR, 3),
            ('LogicalBlock', UCHAR * 4),
            ('TransferLength', UCHAR * 4),
            ('Reserved2', UCHAR, 7),
            ('Streaming', UCHAR, 1),
            ('Control', UCHAR),
        ]
        READ12 = _READ12
        _CDB.READ12 = READ12


        class _WRITE12(ctypes.Structure):
            pass


        _WRITE12._fields_ = [
            # 0xAA - SCSIOP_WRITE12
            ('OperationCode', UCHAR),
            ('RelativeAddress', UCHAR, 1),
            ('Reserved1', UCHAR, 1),
            ('EBP', UCHAR, 1),
            ('ForceUnitAccess', UCHAR, 1),
            ('DisablePageOut', UCHAR, 1),
            ('LogicalUnitNumber', UCHAR, 3),
            ('LogicalBlock', UCHAR * 4),
            ('TransferLength', UCHAR * 4),
            ('Reserved2', UCHAR, 7),
            ('Streaming', UCHAR, 1),
            ('Control', UCHAR),
        ]
        WRITE12 = _WRITE12
        _CDB.WRITE12 = WRITE12


        class _ATA_PASSTHROUGH12(ctypes.Structure):
            pass


        _ATA_PASSTHROUGH12._fields_ = [
            # 0xA1 - SCSIOP_ATA_PASSTHROUGH12
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 1),
            ('Protocol', UCHAR, 4),
            ('MultipleCount', UCHAR, 3),
            ('TLength', UCHAR, 2),
            ('ByteBlock', UCHAR, 1),
            ('TDir', UCHAR, 1),
            ('Reserved2', UCHAR, 1),
            ('CkCond', UCHAR, 1),
            ('Offline', UCHAR, 2),
            ('Features', UCHAR),
            ('SectorCount', UCHAR),
            ('LbaLow', UCHAR),
            ('LbaMid', UCHAR),
            ('LbaHigh', UCHAR),
            ('Device', UCHAR),
            ('Command', UCHAR),
            ('Reserved3', UCHAR),
            ('Control', UCHAR),
        ]
        ATA_PASSTHROUGH12 = _ATA_PASSTHROUGH12
        _CDB.ATA_PASSTHROUGH12 = ATA_PASSTHROUGH12


        class _READ16(ctypes.Structure):
            pass


        _READ16._fields_ = [
            # 0x88 - SCSIOP_READ16
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 3),
            ('ForceUnitAccess', UCHAR, 1),
            ('DisablePageOut', UCHAR, 1),
            ('ReadProtect', UCHAR, 3),
            ('LogicalBlock', UCHAR * 8),
            ('TransferLength', UCHAR * 4),
            ('Reserved2', UCHAR, 7),
            ('Streaming', UCHAR, 1),
            ('Control', UCHAR),
        ]
        READ16 = _READ16
        _CDB.READ16 = READ16


        class _WRITE16(ctypes.Structure):
            pass


        _WRITE16._fields_ = [
            # 0x8A - SCSIOP_WRITE16
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 3),
            ('ForceUnitAccess', UCHAR, 1),
            ('DisablePageOut', UCHAR, 1),
            ('WriteProtect', UCHAR, 3),
            ('LogicalBlock', UCHAR * 8),
            ('TransferLength', UCHAR * 4),
            ('Reserved2', UCHAR, 7),
            ('Streaming', UCHAR, 1),
            ('Control', UCHAR),
        ]
        WRITE16 = _WRITE16
        _CDB.WRITE16 = WRITE16


        class _VERIFY16(ctypes.Structure):
            pass


        _VERIFY16._fields_ = [
            # 0x8F - SCSIOP_VERIFY16
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 1),
            ('ByteCheck', UCHAR, 1),
            ('BlockVerify', UCHAR, 1),
            ('Reserved2', UCHAR, 1),
            ('DisablePageOut', UCHAR, 1),
            ('VerifyProtect', UCHAR, 3),
            ('LogicalBlock', UCHAR * 8),
            ('VerificationLength', UCHAR * 4),
            ('Reserved3', UCHAR, 7),
            ('Streaming', UCHAR, 1),
            ('Control', UCHAR),
        ]
        VERIFY16 = _VERIFY16
        _CDB.VERIFY16 = VERIFY16


        class _SYNCHRONIZE_CACHE16(ctypes.Structure):
            pass


        _SYNCHRONIZE_CACHE16._fields_ = [
            # 0x91 - SCSIOP_SYNCHRONIZE_CACHE16
            ('OperationCode', UCHAR),
            ('Reserved1', UCHAR, 1),
            ('Immediate', UCHAR, 1),
            ('Reserved2', UCHAR, 6),
            ('LogicalBlock', UCHAR * 8),
            ('BlockCount', UCHAR * 4),
            ('Reserved3', UCHAR),
            ('Control', UCHAR),
        ]
        SYNCHRONIZE_CACHE16 = _SYNCHRONIZE_CACHE16
        _CDB.SYNCHRONIZE_CACHE16 = SYNCHRONIZE_CACHE16


        class _READ_CAPACITY16(ctypes.Structure):
            pass


        _READ_CAPACITY16._fields_ = [
            # 0x9E - SCSIOP_READ_CAPACITY16
            ('OperationCode', UCHAR),
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('LogicalBlock', UCHAR * 8),
            ('AllocationLength', UCHAR * 4),
            ('PMI', UCHAR, 1),
            ('Reserved2', UCHAR, 7),
            ('Control', UCHAR),
        ]
        READ_CAPACITY16 = _READ_CAPACITY16
        _CDB.READ_CAPACITY16 = READ_CAPACITY16


        class _ATA_PASSTHROUGH16(ctypes.Structure):
            pass


        _ATA_PASSTHROUGH16._fields_ = [
            # 0x85 - SCSIOP_ATA_PASSTHROUGH16
            ('OperationCode', UCHAR),
            ('Extend', UCHAR, 1),
            ('Protocol', UCHAR, 4),
            ('MultipleCount', UCHAR, 3),
            ('TLength', UCHAR, 2),
            ('ByteBlock', UCHAR, 1),
            ('TDir', UCHAR, 1),
            ('Reserved1', UCHAR, 1),
            ('CkCond', UCHAR, 1),
            ('Offline', UCHAR, 2),
            ('Features15_8', UCHAR),
            ('Features7_0', UCHAR),
            ('SectorCount15_8', UCHAR),
            ('SectorCount7_0', UCHAR),
            ('LbaLow15_8', UCHAR),
            ('LbaLow7_0', UCHAR),
            ('LbaMid15_8', UCHAR),
            ('LbaMid7_0', UCHAR),
            ('LbaHigh15_8', UCHAR),
            ('LbaHigh7_0', UCHAR),
            ('Device', UCHAR),
            ('Command', UCHAR),
            ('Control', UCHAR),
        ]
        ATA_PASSTHROUGH16 = _ATA_PASSTHROUGH16
        _CDB.ATA_PASSTHROUGH16 = ATA_PASSTHROUGH16


        class _GET_LBA_STATUS(ctypes.Structure):
            pass


        _GET_LBA_STATUS._fields_ = [
            # 0x9E SCSIOP_GET_LBA_STATUS
            ('OperationCode', UCHAR),
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('StartingLBA', UCHAR * 8),
            ('AllocationLength', UCHAR * 4),
            ('Reserved2', UCHAR),
            ('Control', UCHAR),
        ]
        GET_LBA_STATUS = _GET_LBA_STATUS
        _CDB.GET_LBA_STATUS = GET_LBA_STATUS


        class _TOKEN_OPERATION(ctypes.Structure):
            pass


        _TOKEN_OPERATION._fields_ = [
            # 0x83 SCSIOP_POPULATE_TOKEN, SCSIOP_WRITE_USING_TOKEN
            ('OperationCode', UCHAR),
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('Reserved2', UCHAR * 4),
            ('ListIdentifier', UCHAR * 4),
            ('ParameterListLength', UCHAR * 4),
            ('GroupNumber', UCHAR, 5),
            ('Reserved3', UCHAR, 3),
            ('Control', UCHAR),
        ]
        TOKEN_OPERATION = _TOKEN_OPERATION
        _CDB.TOKEN_OPERATION = TOKEN_OPERATION


        class _RECEIVE_TOKEN_INFORMATION(ctypes.Structure):
            pass


        _RECEIVE_TOKEN_INFORMATION._fields_ = [
            # 0x84 SCSIOP_RECEIVE_ROD_TOKEN_INFORMATION
            ('OperationCode', UCHAR),
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('ListIdentifier', UCHAR * 4),
            ('Reserved2', UCHAR * 4),
            ('AllocationLength', UCHAR * 4),
            ('Reserved3', UCHAR),
            ('Control', UCHAR),
        ]
        RECEIVE_TOKEN_INFORMATION = _RECEIVE_TOKEN_INFORMATION
        _CDB.RECEIVE_TOKEN_INFORMATION = RECEIVE_TOKEN_INFORMATION


        class _WRITE_BUFFER(ctypes.Structure):
            pass


        _WRITE_BUFFER._fields_ = [
            # 0x3B SCSIOP_WRITE_DATA_BUFF
            ('OperationCode', UCHAR),
            ('Mode', UCHAR, 5),
            ('ModeSpecific', UCHAR, 3),
            ('BufferID', UCHAR),
            ('BufferOffset', UCHAR * 3),
            ('ParameterListLength', UCHAR * 3),
            ('Control', UCHAR),
        ]
        WRITE_BUFFER = _WRITE_BUFFER
        _CDB.WRITE_BUFFER = WRITE_BUFFER


        class _CLOSE_ZONE(ctypes.Structure):
            pass


        _CLOSE_ZONE._fields_ = [
            # 0x94 - SCSIOP_ZBC_OUT
            ('OperationCode', UCHAR),
            # 0x01 - SERVICE_ACTION_CLOSE_ZONE
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('ZoneId', UCHAR * 8),
            ('Reserved2', UCHAR * 4),
            ('All', UCHAR, 1),
            ('Reserved3', UCHAR, 7),
            ('Control', UCHAR),
        ]
        CLOSE_ZONE = _CLOSE_ZONE
        _CDB.CLOSE_ZONE = CLOSE_ZONE


        class _FINISH_ZONE(ctypes.Structure):
            pass


        _FINISH_ZONE._fields_ = [
            # 0x94 - SCSIOP_ZBC_OUT
            ('OperationCode', UCHAR),
            # 0x02 - SERVICE_ACTION_FINISH_ZONE
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('ZoneId', UCHAR * 8),
            ('Reserved2', UCHAR * 4),
            ('All', UCHAR, 1),
            ('Reserved3', UCHAR, 7),
            ('Control', UCHAR),
        ]
        FINISH_ZONE = _FINISH_ZONE
        _CDB.FINISH_ZONE = FINISH_ZONE


        class _OPEN_ZONE(ctypes.Structure):
            pass


        _OPEN_ZONE._fields_ = [
            # 0x94 - SCSIOP_ZBC_OUT
            ('OperationCode', UCHAR),
            # 0x03 - SERVICE_ACTION_OPEN_ZONE
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('ZoneId', UCHAR * 8),
            ('Reserved2', UCHAR * 4),
            ('All', UCHAR, 1),
            ('Reserved3', UCHAR, 7),
            ('Control', UCHAR),
        ]
        OPEN_ZONE = _OPEN_ZONE
        _CDB.OPEN_ZONE = OPEN_ZONE


        class _RESET_WRITE_POINTER(ctypes.Structure):
            pass


        _RESET_WRITE_POINTER._fields_ = [
            # 0x94 - SCSIOP_ZBC_OUT
            ('OperationCode', UCHAR),
            # 0x04 - SERVICE_ACTION_RESET_WRITE_POINTER
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('ZoneId', UCHAR * 8),
            ('Reserved2', UCHAR * 4),
            ('All', UCHAR, 1),
            ('Reserved3', UCHAR, 7),
            ('Control', UCHAR),
        ]
        RESET_WRITE_POINTER = _RESET_WRITE_POINTER
        _CDB.RESET_WRITE_POINTER = RESET_WRITE_POINTER


        class _REPORT_ZONES(ctypes.Structure):
            pass


        _REPORT_ZONES._fields_ = [
            # 0x95 - SCSIOP_ZBC_IN
            ('OperationCode', UCHAR),
            # 0x00 - SERVICE_ACTION_REPORT_ZONES
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('ZoneStartLBA', UCHAR * 8),
            ('AllocationLength', UCHAR * 4),
            ('ReportingOptions', UCHAR, 6),
            ('Reserved3', UCHAR, 1),
            ('Partial', UCHAR, 1),
            ('Control', UCHAR),
        ]
        REPORT_ZONES = _REPORT_ZONES
        _CDB.REPORT_ZONES = REPORT_ZONES


        class _GET_PHYSICAL_ELEMENT_STATUS(ctypes.Structure):
            pass


        _GET_PHYSICAL_ELEMENT_STATUS._fields_ = [
            # 0x9E - SCSIOP_GET_PHYSICAL_ELEMENT_STATUS
            ('OperationCode', UCHAR),
            # 0x17 - SERVICE_ACTION_GET_PHYSICAL_ELEMENT_STATUS
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('Reserved2', UCHAR * 4),
            ('StartingElement', UCHAR * 4),
            ('AllocationLength', UCHAR * 4),
            ('ReportType', UCHAR, 4),
            ('Reserved3', UCHAR, 2),
            ('Filter', UCHAR, 2),
            ('Control', UCHAR),
        ]
        GET_PHYSICAL_ELEMENT_STATUS = _GET_PHYSICAL_ELEMENT_STATUS
        _CDB.GET_PHYSICAL_ELEMENT_STATUS = GET_PHYSICAL_ELEMENT_STATUS


        class _REMOVE_ELEMENT_AND_TRUNCATE(ctypes.Structure):
            pass


        _REMOVE_ELEMENT_AND_TRUNCATE._fields_ = [
            # 0x9E - SCSIOP_REMOVE_ELEMENT_AND_TRUNCATE
            ('OperationCode', UCHAR),
            # 0x18 - SERVICE_ACTION_REMOVE_ELEMENT_AND_TRUNCATE
            ('ServiceAction', UCHAR, 5),
            ('Reserved1', UCHAR, 3),
            ('RequestedCapacity', UCHAR * 8),
            ('ElementIdentifier', UCHAR * 4),
            ('Reserved2', UCHAR),
            ('Control', UCHAR),
        ]
        REMOVE_ELEMENT_AND_TRUNCATE = _REMOVE_ELEMENT_AND_TRUNCATE
        _CDB.REMOVE_ELEMENT_AND_TRUNCATE = REMOVE_ELEMENT_AND_TRUNCATE


        _TEMP__CDB = [
            # Generic 6 - Byte CDB
            ('CDB6GENERIC', _CDB.CDB6GENERIC),
            # Standard 6 - byte CDB
            ('CDB6READWRITE', _CDB.CDB6READWRITE),
            # SCSI - 1 Inquiry CDB
            ('CDB6INQUIRY', _CDB.CDB6INQUIRY),
            # SCSI - 3 Inquiry CDB
            ('CDB6INQUIRY3', _CDB.CDB6INQUIRY3),
            ('CDB6VERIFY', _CDB.CDB6VERIFY),
            ('RECEIVE_DIAGNOSTIC', _CDB.RECEIVE_DIAGNOSTIC),
            ('SEND_DIAGNOSTIC', _CDB.SEND_DIAGNOSTIC),
            # SCSI Format CDB
            ('CDB6FORMAT', _CDB.CDB6FORMAT),
            # Standard 10 - byte CDB
            ('CDB10', _CDB.CDB10),
            # Standard 12 - byte CDB
            ('CDB12', _CDB.CDB12),
            # Standard 16 - byte CDB
            ('CDB16', _CDB.CDB16),
            # Read Buffer(10) command from SPC - 5
            ('READ_BUFFER_10', _CDB.READ_BUFFER_10),
            # Security - related commands from SPC - 4
            ('SECURITY_PROTOCOL_IN', _CDB.SECURITY_PROTOCOL_IN),
            ('SECURITY_PROTOCOL_OUT', _CDB.SECURITY_PROTOCOL_OUT),
            # Block Device UNMAP CDB
            ('UNMAP', _CDB.UNMAP),
            # Block Device SANITIZE CDB (SBC - 4)
            ('SANITIZE', _CDB.SANITIZE),
            # CD Rom Audio CDBs
            ('PAUSE_RESUME', _CDB.PAUSE_RESUME),
            # Read Table of Contents
            ('READ_TOC', _CDB.READ_TOC),
            ('READ_DISK_INFORMATION', _CDB.READ_DISK_INFORMATION),
            ('READ_TRACK_INFORMATION', _CDB.READ_TRACK_INFORMATION),
            ('RESERVE_TRACK_RZONE', _CDB.RESERVE_TRACK_RZONE),
            ('SEND_OPC_INFORMATION', _CDB.SEND_OPC_INFORMATION),
            ('REPAIR_TRACK', _CDB.REPAIR_TRACK),
            ('CLOSE_TRACK', _CDB.CLOSE_TRACK),
            ('READ_BUFFER_CAPACITY', _CDB.READ_BUFFER_CAPACITY),
            ('SEND_CUE_SHEET', _CDB.SEND_CUE_SHEET),
            ('READ_HEADER', _CDB.READ_HEADER),
            ('PLAY_AUDIO', _CDB.PLAY_AUDIO),
            ('PLAY_AUDIO_MSF', _CDB.PLAY_AUDIO_MSF),
            ('BLANK_MEDIA', _CDB.BLANK_MEDIA),
            ('PLAY_CD', _CDB.PLAY_CD),
            ('SCAN_CD', _CDB.SCAN_CD),
            ('STOP_PLAY_SCAN', _CDB.STOP_PLAY_SCAN),
            # Read SubChannel Data
            ('SUBCHANNEL', _CDB.SUBCHANNEL),
            # Read CD. Used by Atapi for raw sector reads.
            ('READ_CD', _CDB.READ_CD),
            ('READ_CD_MSF', _CDB.READ_CD_MSF),
            # Plextor Read CD - DA
            ('PLXTR_READ_CDDA', _CDB.PLXTR_READ_CDDA),
            # NEC Read CD - DA
            ('NEC_READ_CDDA', _CDB.NEC_READ_CDDA),
        ]
        if NTDDI_VERSION >= NTDDI_WIN8:
            _TEMP__CDB += [
                # Mode sense
                ('MODE_SENSE', _CDB.MODE_SENSE),
                ('MODE_SENSE10', _CDB.MODE_SENSE10),
            ]
        else:
            _TEMP__CDB += [
                ('MODE_SENSE', _CDB.MODE_SENSE),
                ('MODE_SENSE10', _CDB.MODE_SENSE10),
            ]
        # END IF
        _TEMP__CDB += [
            # Mode select
            ('MODE_SELECT', _CDB.MODE_SELECT),
            ('MODE_SELECT10', _CDB.MODE_SELECT10),
            ('LOCATE', _CDB.LOCATE),
            ('LOGSENSE', _CDB.LOGSENSE),
            ('LOGSELECT', _CDB.LOGSELECT),
            ('PRINT', _CDB.PRINT),
            ('SEEK', _CDB.SEEK),
            ('ERASE', _CDB.ERASE),
            ('START_STOP', _CDB.START_STOP),
            ('MEDIA_REMOVAL', _CDB.MEDIA_REMOVAL),
            # Tape CDBs
            ('SEEK_BLOCK', _CDB.SEEK_BLOCK),
            ('REQUEST_BLOCK_ADDRESS', _CDB.REQUEST_BLOCK_ADDRESS),
            ('PARTITION', _CDB.PARTITION),
            ('WRITE_TAPE_MARKS', _CDB.WRITE_TAPE_MARKS),
            ('SPACE_TAPE_MARKS', _CDB.SPACE_TAPE_MARKS),
            # Read tape position
            ('READ_POSITION', _CDB.READ_POSITION),
            # ReadWrite for Tape
            ('CDB6READWRITETAPE', _CDB.CDB6READWRITETAPE),
            # Medium changer CDB's
            ('INIT_ELEMENT_STATUS', _CDB.INIT_ELEMENT_STATUS),
            ('INITIALIZE_ELEMENT_RANGE', _CDB.INITIALIZE_ELEMENT_RANGE),
            ('POSITION_TO_ELEMENT', _CDB.POSITION_TO_ELEMENT),
            ('MOVE_MEDIUM', _CDB.MOVE_MEDIUM),
            ('EXCHANGE_MEDIUM', _CDB.EXCHANGE_MEDIUM),
            ('READ_ELEMENT_STATUS', _CDB.READ_ELEMENT_STATUS),
            ('SEND_VOLUME_TAG', _CDB.SEND_VOLUME_TAG),
            ('REQUEST_VOLUME_ELEMENT_ADDRESS', _CDB.REQUEST_VOLUME_ELEMENT_ADDRESS),
            # Atapi 2.5 Changer 12 - byte CDBs
            ('LOAD_UNLOAD', _CDB.LOAD_UNLOAD),
            ('MECH_STATUS', _CDB.MECH_STATUS),
            # C/DVD 0.9 CDBs
            ('SYNCHRONIZE_CACHE10', _CDB.SYNCHRONIZE_CACHE10),
            ('GET_EVENT_STATUS_NOTIFICATION', _CDB.GET_EVENT_STATUS_NOTIFICATION),
            ('GET_PERFORMANCE', _CDB.GET_PERFORMANCE),
            ('READ_DVD_STRUCTURE', _CDB.READ_DVD_STRUCTURE),
            ('SET_STREAMING', _CDB.SET_STREAMING),
            ('SEND_DVD_STRUCTURE', _CDB.SEND_DVD_STRUCTURE),
            ('SEND_KEY', _CDB.SEND_KEY),
            ('REPORT_KEY', _CDB.REPORT_KEY),
            ('SET_READ_AHEAD', _CDB.SET_READ_AHEAD),
            ('READ_FORMATTED_CAPACITIES', _CDB.READ_FORMATTED_CAPACITIES),
            # SCSI - 3
            ('REPORT_LUNS', _CDB.REPORT_LUNS),
            ('PERSISTENT_RESERVE_IN', _CDB.PERSISTENT_RESERVE_IN),
            ('PERSISTENT_RESERVE_OUT', _CDB.PERSISTENT_RESERVE_OUT),
            ('REPORT_TIMESTAMP', _CDB.REPORT_TIMESTAMP),
            ('SET_TIMESTAMP', _CDB.SET_TIMESTAMP),
            # MMC / SFF - 8090 commands
            ('GET_CONFIGURATION', _CDB.GET_CONFIGURATION),
            ('SET_CD_SPEED', _CDB.SET_CD_SPEED),
            ('READ12', _CDB.READ12),
            ('WRITE12', _CDB.WRITE12),
            ('ATA_PASSTHROUGH12', _CDB.ATA_PASSTHROUGH12),
            # 16 - byte CDBs
            ('READ16', _CDB.READ16),
            ('WRITE16', _CDB.WRITE16),
            ('VERIFY16', _CDB.VERIFY16),
            ('SYNCHRONIZE_CACHE16', _CDB.SYNCHRONIZE_CACHE16),
            ('READ_CAPACITY16', _CDB.READ_CAPACITY16),
            ('ATA_PASSTHROUGH16', _CDB.ATA_PASSTHROUGH16),
            ('GET_LBA_STATUS', _CDB.GET_LBA_STATUS),
            ('TOKEN_OPERATION', _CDB.TOKEN_OPERATION),
            ('RECEIVE_TOKEN_INFORMATION', _CDB.RECEIVE_TOKEN_INFORMATION),
            ('WRITE_BUFFER', _CDB.WRITE_BUFFER),
            ('CLOSE_ZONE', _CDB.CLOSE_ZONE),
            ('FINISH_ZONE', _CDB.FINISH_ZONE),
            ('OPEN_ZONE', _CDB.OPEN_ZONE),
            ('RESET_WRITE_POINTER', _CDB.RESET_WRITE_POINTER),
            ('REPORT_ZONES', _CDB.REPORT_ZONES),
            ('GET_PHYSICAL_ELEMENT_STATUS', _CDB.GET_PHYSICAL_ELEMENT_STATUS),
            ('REMOVE_ELEMENT_AND_TRUNCATE', _CDB.REMOVE_ELEMENT_AND_TRUNCATE),
            ('AsUlong', ULONG * 4),
            ('AsByte', UCHAR * 16),
        ]
        _CDB._fields_ = _TEMP__CDB


        class _CDB32GENERIC(ctypes.Structure):
            pass


        _CDB32GENERIC._fields_ = [
            ('OperationCode', UCHAR),
            ('Control', UCHAR),
            ('Reserved1', UCHAR * 4),
            ('Group', UCHAR, 5),
            ('Reserved2', UCHAR, 3),
            ('AdditionalCDBLength', UCHAR),
            ('ServiceAction', UCHAR * 2),
            ('Reserved3', UCHAR * 2),
            ('LogicalBlock', UCHAR * 8),
            ('Reserved4', UCHAR * 8),
            ('TransferLength', UCHAR * 4),
        ]
        CDB32GENERIC = _CDB32GENERIC
        _CDB32.CDB32GENERIC = CDB32GENERIC


        _CDB32._fields_ = [
            # Standard 32 - byte CDB
            ('CDB32GENERIC', _CDB32.CDB32GENERIC),
            ('AsUlong', ULONG * 8),
            ('AsByte', UCHAR * 32),
        ]

        # //////////////////////////////////////////////////////////////////////////////
        #
        # GET_EVENT_STATUS_NOTIFICATION
        NOTIFICATION_OPERATIONAL_CHANGE_CLASS_MASK = 0x02
        NOTIFICATION_POWER_MANAGEMENT_CLASS_MASK = 0x04
        NOTIFICATION_EXTERNAL_REQUEST_CLASS_MASK = 0x08
        NOTIFICATION_MEDIA_STATUS_CLASS_MASK = 0x10
        NOTIFICATION_MULTI_HOST_CLASS_MASK = 0x20
        NOTIFICATION_DEVICE_BUSY_CLASS_MASK = 0x40
        NOTIFICATION_NO_CLASS_EVENTS = 0x0
        NOTIFICATION_OPERATIONAL_CHANGE_CLASS_EVENTS = 0x1
        NOTIFICATION_POWER_MANAGEMENT_CLASS_EVENTS = 0x2
        NOTIFICATION_EXTERNAL_REQUEST_CLASS_EVENTS = 0x3
        NOTIFICATION_MEDIA_STATUS_CLASS_EVENTS = 0x4
        NOTIFICATION_MULTI_HOST_CLASS_EVENTS = 0x5
        NOTIFICATION_DEVICE_BUSY_CLASS_EVENTS = 0x6


        _TEMP__NOTIFICATION_EVENT_STATUS_HEADER = [
            ('EventDataLength', UCHAR * 2),
            ('NotificationClass', UCHAR, 3),
            ('Reserved', UCHAR, 4),
            ('NEA', UCHAR, 1),
            ('SupportedEventClasses', UCHAR),
        ]
        if not defined(__midl):
            _TEMP__NOTIFICATION_EVENT_STATUS_HEADER += [
                ('ClassEventData', UCHAR * 0),
            ]
        # END IF
        _NOTIFICATION_EVENT_STATUS_HEADER._fields_ = _TEMP__NOTIFICATION_EVENT_STATUS_HEADER
        NOTIFICATION_OPERATIONAL_EVENT_NO_CHANGE = 0x0
        NOTIFICATION_OPERATIONAL_EVENT_CHANGE_REQUESTED = 0x1
        NOTIFICATION_OPERATIONAL_EVENT_CHANGE_OCCURRED = 0x2
        NOTIFICATION_OPERATIONAL_STATUS_AVAILABLE = 0x0
        NOTIFICATION_OPERATIONAL_STATUS_TEMPORARY_BUSY = 0x1
        NOTIFICATION_OPERATIONAL_STATUS_EXTENDED_BUSY = 0x2
        NOTIFICATION_OPERATIONAL_OPCODE_NONE = 0x0
        NOTIFICATION_OPERATIONAL_OPCODE_FEATURE_CHANGE = 0x1
        NOTIFICATION_OPERATIONAL_OPCODE_FEATURE_ADDED = 0x2
        NOTIFICATION_OPERATIONAL_OPCODE_UNIT_RESET = 0x3
        NOTIFICATION_OPERATIONAL_OPCODE_FIRMWARE_CHANGED = 0x4
        NOTIFICATION_OPERATIONAL_OPCODE_INQUIRY_CHANGED = 0x5


        # Class event data may be one (or none) of the following:
        _NOTIFICATION_OPERATIONAL_STATUS._fields_ = [
            # event class == 0x1 UCHAR OperationalEvent : 4;
            ('Reserved1', UCHAR, 4),
            ('OperationalStatus', UCHAR, 4),
            ('Reserved2', UCHAR, 3),
            ('PersistentPrevented', UCHAR, 1),
            ('Operation', UCHAR * 2),
        ]
        NOTIFICATION_POWER_EVENT_NO_CHANGE = 0x0
        NOTIFICATION_POWER_EVENT_CHANGE_SUCCEEDED = 0x1
        NOTIFICATION_POWER_EVENT_CHANGE_FAILED = 0x2
        NOTIFICATION_POWER_STATUS_ACTIVE = 0x1
        NOTIFICATION_POWER_STATUS_IDLE = 0x2
        NOTIFICATION_POWER_STATUS_STANDBY = 0x3
        NOTIFICATION_POWER_STATUS_SLEEP = 0x4


        _NOTIFICATION_POWER_STATUS._fields_ = [
            # event class == 0x2 UCHAR PowerEvent : 4;
            ('Reserved', UCHAR, 4),
            ('PowerStatus', UCHAR),
            ('Reserved2', UCHAR * 2),
        ]
        NOTIFICATION_MEDIA_EVENT_NO_EVENT = 0x0
        NOTIFICATION_EXTERNAL_EVENT_NO_CHANGE = 0x0
        NOTIFICATION_EXTERNAL_EVENT_BUTTON_DOWN = 0x1
        NOTIFICATION_EXTERNAL_EVENT_BUTTON_UP = 0x2
        NOTIFICATION_EXTERNAL_EVENT_EXTERNAL = 0x3        # respond with GET_CONFIGURATION?
        NOTIFICATION_EXTERNAL_STATUS_READY = 0x0
        NOTIFICATION_EXTERNAL_STATUS_PREVENT = 0x1
        NOTIFICATION_EXTERNAL_REQUEST_NONE = 0x0000
        NOTIFICATION_EXTERNAL_REQUEST_QUEUE_OVERRUN = 0x0001
        NOTIFICATION_EXTERNAL_REQUEST_PLAY = 0x0101
        NOTIFICATION_EXTERNAL_REQUEST_REWIND_BACK = 0x0102
        NOTIFICATION_EXTERNAL_REQUEST_FAST_FORWARD = 0x0103
        NOTIFICATION_EXTERNAL_REQUEST_PAUSE = 0x0104
        NOTIFICATION_EXTERNAL_REQUEST_STOP = 0x0106
        NOTIFICATION_EXTERNAL_REQUEST_ASCII_LOW = 0x0200
        NOTIFICATION_EXTERNAL_REQUEST_ASCII_HIGH = 0x02FF


        _NOTIFICATION_EXTERNAL_STATUS._fields_ = [
            # event class == 0x3 UCHAR ExternalEvent : 4;
            ('Reserved1', UCHAR, 4),
            ('ExternalStatus', UCHAR, 4),
            ('Reserved2', UCHAR, 3),
            ('PersistentPrevented', UCHAR, 1),
            ('Request', UCHAR * 2),
        ]
        NOTIFICATION_MEDIA_EVENT_NO_CHANGE = 0x0
        NOTIFICATION_MEDIA_EVENT_EJECT_REQUEST = 0x1
        NOTIFICATION_MEDIA_EVENT_NEW_MEDIA = 0x2
        NOTIFICATION_MEDIA_EVENT_MEDIA_REMOVAL = 0x3
        NOTIFICATION_MEDIA_EVENT_MEDIA_CHANGE = 0x4


        class _Union_1(ctypes.Union):
            pass


        class _Struct_1(ctypes.Structure):
            pass


        _Struct_1._fields_ = [
            ('DoorTrayOpen', UCHAR, 1),
            ('MediaPresent', UCHAR, 1),
            # do not reference this directlynot
            ('ReservedX', UCHAR, 6),
        ]
        _Union_1._Struct_1 = _Struct_1

        _Union_1._anonymous_ = (
            '_Struct_1',
        )

        _Union_1._fields_ = [
            # OBSOLETE - - was improperly named in NT5 headers
            ('PowerStatus', UCHAR),
            # Use this for currently reserved fields
            ('MediaStatus', UCHAR),
            ('_Struct_1', _Union_1._Struct_1),
        ]
        _NOTIFICATION_MEDIA_STATUS._Union_1 = _Union_1

        _NOTIFICATION_MEDIA_STATUS._anonymous_ = (
            '_Union_1',
        )

        _NOTIFICATION_MEDIA_STATUS._fields_ = [
            # event class == 0x4 UCHAR MediaEvent : 4;
            ('Reserved', UCHAR, 4),
            ('_Union_1', _NOTIFICATION_MEDIA_STATUS._Union_1),
            ('StartSlot', UCHAR),
            ('EndSlot', UCHAR),
        ]
        NOTIFICATION_BUSY_EVENT_NO_EVENT = 0x0
        NOTIFICATION_MULTI_HOST_EVENT_NO_CHANGE = 0x0
        NOTIFICATION_MULTI_HOST_EVENT_CONTROL_REQUEST = 0x1
        NOTIFICATION_MULTI_HOST_EVENT_CONTROL_GRANT = 0x2
        NOTIFICATION_MULTI_HOST_EVENT_CONTROL_RELEASE = 0x3
        NOTIFICATION_MULTI_HOST_STATUS_READY = 0x0
        NOTIFICATION_MULTI_HOST_STATUS_PREVENT = 0x1
        NOTIFICATION_MULTI_HOST_PRIORITY_NO_REQUESTS = 0x0
        NOTIFICATION_MULTI_HOST_PRIORITY_LOW = 0x1
        NOTIFICATION_MULTI_HOST_PRIORITY_MEDIUM = 0x2
        NOTIFICATION_MULTI_HOST_PRIORITY_HIGH = 0x3


        _NOTIFICATION_MULTI_HOST_STATUS._fields_ = [
            # event class == 0x5 UCHAR MultiHostEvent : 4;
            ('Reserved1', UCHAR, 4),
            ('MultiHostStatus', UCHAR, 4),
            ('Reserved2', UCHAR, 3),
            ('PersistentPrevented', UCHAR, 1),
            ('Priority', UCHAR * 2),
        ]
        NOTIFICATION_BUSY_EVENT_NO_CHANGE = 0x0
        NOTIFICATION_BUSY_EVENT_BUSY = 0x1
        NOTIFICATION_BUSY_EVENT_LO_CHANGE = 0x2
        NOTIFICATION_BUSY_STATUS_NO_EVENT = 0x0
        NOTIFICATION_BUSY_STATUS_POWER = 0x1
        NOTIFICATION_BUSY_STATUS_IMMEDIATE = 0x2
        NOTIFICATION_BUSY_STATUS_DEFERRED = 0x3


        _NOTIFICATION_BUSY_STATUS._fields_ = [
            # event class == 0x6 UCHAR DeviceBusyEvent : 4;
            ('Reserved', UCHAR, 4),
            ('DeviceBusyStatus', UCHAR),
            ('Time', UCHAR * 2),
        ]

        # //////////////////////////////////////////////////////////////////////////////
        #
        # SECURITY PROTOCOL IN/OUT definitions (SPC - 4, 6.29/6.30)
        _SUPPORTED_SECURITY_PROTOCOLS_PARAMETER_DATA._fields_ = [
            ('Reserved1', UCHAR * 6),
            ('SupportedSecurityListLength', UCHAR * 2),
            ('SupportedSecurityProtocol', UCHAR * 0),
        ]

        # Security protocols
        SECURITY_PROTOCOL_IEEE1667 = 0xEE

        # //////////////////////////////////////////////////////////////////////////////
        #
        # Read DVD Structure Definitions and Constants
        DVD_FORMAT_LEAD_IN = 0x00
        DVD_FORMAT_COPYRIGHT = 0x01
        DVD_FORMAT_DISK_KEY = 0x02
        DVD_FORMAT_BCA = 0x03
        DVD_FORMAT_MANUFACTURING = 0x04


        _TEMP__READ_DVD_STRUCTURES_HEADER = [
            ('Length', UCHAR * 2),
            ('Reserved', UCHAR * 2),
        ]
        if not defined(__midl):
            _TEMP__READ_DVD_STRUCTURES_HEADER += [
                ('Data', UCHAR * 0),
            ]
        # END IF
        _READ_DVD_STRUCTURES_HEADER._fields_ = _TEMP__READ_DVD_STRUCTURES_HEADER


        # DiskKey, BCA & Manufacturer information will provide byte arrays as
        # their
        # data.
        # CDVD 0.9 Send & Report Key Definitions and Structures
        DVD_REPORT_AGID = 0x00
        DVD_CHALLENGE_KEY = 0x01
        DVD_KEY_1 = 0x02
        DVD_KEY_2 = 0x03
        DVD_TITLE_KEY = 0x04
        DVD_REPORT_ASF = 0x05
        DVD_INVALIDATE_AGID = 0x3F


        _TEMP__CDVD_KEY_HEADER = [
            ('DataLength', UCHAR * 2),
            ('Reserved', UCHAR * 2),
        ]
        if not defined(__midl):
            _TEMP__CDVD_KEY_HEADER += [
                ('Data', UCHAR * 0),
            ]
        # END IF
        _CDVD_KEY_HEADER._fields_ = _TEMP__CDVD_KEY_HEADER

        _CDVD_REPORT_AGID_DATA._fields_ = [
            ('Reserved1', UCHAR * 3),
            ('Reserved2', UCHAR, 6),
            ('AGID', UCHAR, 2),
        ]

        _CDVD_CHALLENGE_KEY_DATA._fields_ = [
            ('ChallengeKeyValue', UCHAR * 10),
            ('Reserved', UCHAR * 2),
        ]

        _CDVD_KEY_DATA._fields_ = [
            ('Key', UCHAR * 5),
            ('Reserved', UCHAR * 3),
        ]

        _CDVD_REPORT_ASF_DATA._fields_ = [
            ('Reserved1', UCHAR * 3),
            ('Success', UCHAR, 1),
            ('Reserved2', UCHAR, 7),
        ]

        _CDVD_TITLE_KEY_HEADER._fields_ = [
            ('DataLength', UCHAR * 2),
            ('Reserved1', UCHAR * 1),
            ('Reserved2', UCHAR, 3),
            ('CGMS', UCHAR, 2),
            ('CP_SEC', UCHAR, 1),
            ('CPM', UCHAR, 1),
            ('Zero', UCHAR, 1),
            ('TitleKey', CDVD_KEY_DATA),
        ]


        # Format Unit Data definitions and structures
        _FORMAT_DESCRIPTOR._fields_ = [
            ('NumberOfBlocks', UCHAR * 4),
            ('FormatSubType', UCHAR, 2),
            ('FormatType', UCHAR, 6),
            ('BlockLength', UCHAR * 3),
        ]

        _TEMP__FORMAT_LIST_HEADER = [
            ('Reserved', UCHAR),
            ('VendorSpecific', UCHAR, 1),
            ('Immediate', UCHAR, 1),
            ('TryOut', UCHAR, 1),
            ('IP', UCHAR, 1),
            ('STPF', UCHAR, 1),
            ('DCRT', UCHAR, 1),
            ('DPRY', UCHAR, 1),
            ('FOV', UCHAR, 1),
            ('FormatDescriptorLength', UCHAR * 2),
        ]
        if not defined(__midl):
            _TEMP__FORMAT_LIST_HEADER += [
                ('Descriptors', FORMAT_DESCRIPTOR * 0),
            ]
        # END IF
        _FORMAT_LIST_HEADER._fields_ = _TEMP__FORMAT_LIST_HEADER


        # Read Formatted Capacity Data - returned in Big Endian Format
        _FORMATTED_CAPACITY_DESCRIPTOR._fields_ = [
            ('NumberOfBlocks', UCHAR * 4),
            ('Maximum', UCHAR, 1),
            ('Valid', UCHAR, 1),
            ('FormatType', UCHAR, 6),
            ('BlockLength', UCHAR * 3),
        ]

        _TEMP__FORMATTED_CAPACITY_LIST = [
            ('Reserved', UCHAR * 3),
            ('CapacityListLength', UCHAR),
        ]
        if not defined(__midl):
            _TEMP__FORMATTED_CAPACITY_LIST += [
                ('Descriptors', FORMATTED_CAPACITY_DESCRIPTOR * 0),
            ]
        # END IF
        _FORMATTED_CAPACITY_LIST._fields_ = _TEMP__FORMATTED_CAPACITY_LIST


        # BLANK command blanking type codes
        BLANK_FULL = 0x0
        BLANK_MINIMAL = 0x1
        BLANK_TRACK = 0x2
        BLANK_UNRESERVE_TRACK = 0x3
        BLANK_TAIL = 0x4
        BLANK_UNCLOSE_SESSION = 0x5
        BLANK_SESSION = 0x6


        # PLAY_CD definitions and constants
        CD_EXPECTED_SECTOR_ANY = 0x0
        CD_EXPECTED_SECTOR_CDDA = 0x1
        CD_EXPECTED_SECTOR_MODE1 = 0x2
        CD_EXPECTED_SECTOR_MODE2 = 0x3
        CD_EXPECTED_SECTOR_MODE2_FORM1 = 0x4
        CD_EXPECTED_SECTOR_MODE2_FORM2 = 0x5


        # Read Disk Information Definitions and Capabilities
        DISK_STATUS_EMPTY = 0x00
        DISK_STATUS_INCOMPLETE = 0x01
        DISK_STATUS_COMPLETE = 0x02
        DISK_STATUS_OTHERS = 0x03
        LAST_SESSION_EMPTY = 0x00
        LAST_SESSION_INCOMPLETE = 0x01
        LAST_SESSION_RESERVED_DAMAGED = 0x02
        LAST_SESSION_COMPLETE = 0x03
        DISK_TYPE_CDDA = 0x00
        DISK_TYPE_CDI = 0x10
        DISK_TYPE_XA = 0x20
        DISK_TYPE_UNDEFINED = 0xFF


        # Values for MrwStatus field.
        DISC_BGFORMAT_STATE_NONE = 0x0
        DISC_BGFORMAT_STATE_INCOMPLETE = 0x1
        DISC_BGFORMAT_STATE_RUNNING = 0x2
        DISC_BGFORMAT_STATE_COMPLETE = 0x3


        _OPC_TABLE_ENTRY._fields_ = [
            ('Speed', UCHAR * 2),
            ('OPCValue', UCHAR * 6),
        ]

        _DISC_INFORMATION._fields_ = [
            ('Length', UCHAR * 2),
            ('DiscStatus', UCHAR, 2),
            ('LastSessionStatus', UCHAR, 2),
            ('Erasable', UCHAR, 1),
            ('Reserved1', UCHAR, 3),
            ('FirstTrackNumber', UCHAR),
            ('NumberOfSessionsLsb', UCHAR),
            ('LastSessionFirstTrackLsb', UCHAR),
            ('LastSessionLastTrackLsb', UCHAR),
            ('MrwStatus', UCHAR, 2),
            ('MrwDirtyBit', UCHAR, 1),
            ('Reserved2', UCHAR, 2),
            ('URU', UCHAR, 1),
            ('DBC_V', UCHAR, 1),
            ('DID_V', UCHAR, 1),
            ('DiscType', UCHAR),
            ('NumberOfSessionsMsb', UCHAR),
            ('LastSessionFirstTrackMsb', UCHAR),
            ('LastSessionLastTrackMsb', UCHAR),
            ('DiskIdentification', UCHAR * 4),
            # HMSF
            ('LastSessionLeadIn', UCHAR * 4),
            # HMSF
            ('LastPossibleLeadOutStartTime', UCHAR * 4),
            ('DiskBarCode', UCHAR * 8),
            ('Reserved4', UCHAR),
            ('NumberOPCEntries', UCHAR),
            # can be many of these here....
            ('OPCTable', OPC_TABLE_ENTRY * 1),
        ]

        # TODO: Deprecate DISK_INFORMATION
        # if PRAGMA_DEPRECATED_DDK
        # pragma deprecated(_DISK_INFORMATION) // Use DISC_INFORMATION, note
        # size change
        # pragma deprecated( DISK_INFORMATION) // Use DISC_INFORMATION, note
        # size change
        # pragma deprecated(PDISK_INFORMATION) // Use DISC_INFORMATION, note
        # size change
        # endif
        _TEMP__DISK_INFORMATION = [
            ('Length', UCHAR * 2),
            ('DiskStatus', UCHAR, 2),
            ('LastSessionStatus', UCHAR, 2),
            ('Erasable', UCHAR, 1),
            ('Reserved1', UCHAR, 3),
            ('FirstTrackNumber', UCHAR),
            ('NumberOfSessions', UCHAR),
            ('LastSessionFirstTrack', UCHAR),
            ('LastSessionLastTrack', UCHAR),
            ('Reserved2', UCHAR, 5),
            ('GEN', UCHAR, 1),
            ('DBC_V', UCHAR, 1),
            ('DID_V', UCHAR, 1),
            ('DiskType', UCHAR),
            ('Reserved3', UCHAR * 3),
            ('DiskIdentification', UCHAR * 4),
            # MSF
            ('LastSessionLeadIn', UCHAR * 4),
            # MSF
            ('LastPossibleStartTime', UCHAR * 4),
            ('DiskBarCode', UCHAR * 8),
            ('Reserved4', UCHAR),
            ('NumberOPCEntries', UCHAR),
        ]
        if not defined(__midl):
            _TEMP__DISK_INFORMATION += [
                ('OPCTable', OPC_TABLE_ENTRY * 0),
            ]
        # END IF
        _DISK_INFORMATION._fields_ = _TEMP__DISK_INFORMATION


        # Read Header definitions and structures
        class _Union_2(ctypes.Union):
            pass


        class MSF(ctypes.Structure):
            pass


        MSF._fields_ = [
            ('Reserved', UCHAR),
            ('M', UCHAR),
            ('S', UCHAR),
            ('F', UCHAR),
        ]
        _Union_2.MSF = MSF


        _Union_2._fields_ = [
            ('LogicalBlockAddress', UCHAR * 4),
            ('MSF', _Union_2.MSF),
        ]
        _DATA_BLOCK_HEADER._Union_2 = _Union_2

        _DATA_BLOCK_HEADER._anonymous_ = (
            '_Union_2',
        )

        _DATA_BLOCK_HEADER._fields_ = [
            ('DataMode', UCHAR),
            ('Reserved', UCHAR * 4),
            ('_Union_2', _DATA_BLOCK_HEADER._Union_2),
        ]
        DATA_BLOCK_MODE0 = 0x0
        DATA_BLOCK_MODE1 = 0x1
        DATA_BLOCK_MODE2 = 0x2


        # Read TOC Format Codes
        READ_TOC_FORMAT_TOC = 0x00
        READ_TOC_FORMAT_SESSION = 0x01
        READ_TOC_FORMAT_FULL_TOC = 0x02
        READ_TOC_FORMAT_PMA = 0x03
        READ_TOC_FORMAT_ATIP = 0x04

        # TODO: Deprecate TRACK_INFORMATION structure, use TRACK_INFORMATION2
        # instead
        _TRACK_INFORMATION._fields_ = [
            ('Length', UCHAR * 2),
            ('TrackNumber', UCHAR),
            ('SessionNumber', UCHAR),
            ('Reserved1', UCHAR),
            ('TrackMode', UCHAR, 4),
            ('Copy', UCHAR, 1),
            ('Damage', UCHAR, 1),
            ('Reserved2', UCHAR, 2),
            ('DataMode', UCHAR, 4),
            ('FP', UCHAR, 1),
            ('Packet', UCHAR, 1),
            ('Blank', UCHAR, 1),
            ('RT', UCHAR, 1),
            ('NWA_V', UCHAR, 1),
            ('Reserved3', UCHAR, 7),
            ('TrackStartAddress', UCHAR * 4),
            ('NextWritableAddress', UCHAR * 4),
            ('FreeBlocks', UCHAR * 4),
            ('FixedPacketSize', UCHAR * 4),
        ]

        # Second Revision Modifies:
        # * Longer names for some fields
        # * LSB to track/session number fields
        # * LRA_V bit
        # Second Revision Adds:
        # * TrackSize
        # * LastRecordedAddress
        # * MSB to track/session
        # * Two reserved bytes
        # Total structure size increased by 12 (0x0C) bytes
        _TRACK_INFORMATION2._fields_ = [
            ('Length', UCHAR * 2),
            ('TrackNumberLsb', UCHAR),
            ('SessionNumberLsb', UCHAR),
            ('Reserved4', UCHAR),
            ('TrackMode', UCHAR, 4),
            ('Copy', UCHAR, 1),
            ('Damage', UCHAR, 1),
            ('Reserved5', UCHAR, 2),
            ('DataMode', UCHAR, 4),
            ('FixedPacket', UCHAR, 1),
            ('Packet', UCHAR, 1),
            ('Blank', UCHAR, 1),
            ('ReservedTrack', UCHAR, 1),
            ('NWA_V', UCHAR, 1),
            ('LRA_V', UCHAR, 1),
            ('Reserved6', UCHAR, 6),
            ('TrackStartAddress', UCHAR * 4),
            ('NextWritableAddress', UCHAR * 4),
            ('FreeBlocks', UCHAR * 4),
            # blocking factor
            ('FixedPacketSize', UCHAR * 4),
            ('TrackSize', UCHAR * 4),
            ('LastRecordedAddress', UCHAR * 4),
            ('TrackNumberMsb', UCHAR),
            ('SessionNumberMsb', UCHAR),
            ('Reserved7', UCHAR * 2),
        ]

        # Third Revision Adds
        # * ReadCompatibilityLBA
        # Total structure size increased by 4 bytes
        _TRACK_INFORMATION3._fields_ = [
            ('Length', UCHAR * 2),
            ('TrackNumberLsb', UCHAR),
            ('SessionNumberLsb', UCHAR),
            ('Reserved4', UCHAR),
            ('TrackMode', UCHAR, 4),
            ('Copy', UCHAR, 1),
            ('Damage', UCHAR, 1),
            ('Reserved5', UCHAR, 2),
            ('DataMode', UCHAR, 4),
            ('FixedPacket', UCHAR, 1),
            ('Packet', UCHAR, 1),
            ('Blank', UCHAR, 1),
            ('ReservedTrack', UCHAR, 1),
            ('NWA_V', UCHAR, 1),
            ('LRA_V', UCHAR, 1),
            ('Reserved6', UCHAR, 6),
            ('TrackStartAddress', UCHAR * 4),
            ('NextWritableAddress', UCHAR * 4),
            ('FreeBlocks', UCHAR * 4),
            # blocking factor
            ('FixedPacketSize', UCHAR * 4),
            ('TrackSize', UCHAR * 4),
            ('LastRecordedAddress', UCHAR * 4),
            ('TrackNumberMsb', UCHAR),
            ('SessionNumberMsb', UCHAR),
            ('Reserved7', UCHAR * 2),
            ('ReadCompatibilityLba', UCHAR * 4),
        ]

        _PERFORMANCE_DESCRIPTOR._fields_ = [
            ('RandomAccess', UCHAR, 1),
            ('Exact', UCHAR, 1),
            ('RestoreDefaults', UCHAR, 1),
            ('WriteRotationControl', UCHAR, 2),
            ('Reserved1', UCHAR, 3),
            ('Reserved', UCHAR * 3),
            ('StartLba', UCHAR * 4),
            ('EndLba', UCHAR * 4),
            ('ReadSize', UCHAR * 4),
            ('ReadTime', UCHAR * 4),
            ('WriteSize', UCHAR * 4),
            ('WriteTime', UCHAR * 4),
        ]


        # Command Descriptor Block constants.
        CDB6GENERIC_LENGTH = 6
        CDB10GENERIC_LENGTH = 10
        CDB12GENERIC_LENGTH = 12
        SETBITON = 1
        SETBITOFF = 0


        # Mode Sense/Select page constants.
        MODE_PAGE_VENDOR_SPECIFIC = 0x00
        MODE_PAGE_ERROR_RECOVERY = 0x01
        MODE_PAGE_DISCONNECT = 0x02
        MODE_PAGE_FORMAT_DEVICE = 0x03        # disk
        MODE_PAGE_MRW = 0x03        # cdrom
        MODE_PAGE_RIGID_GEOMETRY = 0x04
        MODE_PAGE_FLEXIBILE = 0x05        # disk
        MODE_PAGE_WRITE_PARAMETERS = 0x05        # cdrom
        MODE_PAGE_VERIFY_ERROR = 0x07
        MODE_PAGE_CACHING = 0x08
        MODE_PAGE_PERIPHERAL = 0x09
        MODE_PAGE_CONTROL = 0x0A
        MODE_PAGE_MEDIUM_TYPES = 0x0B
        MODE_PAGE_NOTCH_PARTITION = 0x0C
        MODE_PAGE_CD_AUDIO_CONTROL = 0x0E
        MODE_PAGE_DATA_COMPRESS = 0x0F
        MODE_PAGE_DEVICE_CONFIG = 0x10
        MODE_PAGE_XOR_CONTROL = 0x10        # disk
        MODE_PAGE_MEDIUM_PARTITION = 0x11
        MODE_PAGE_ENCLOSURE_SERVICES_MANAGEMENT = 0x14
        MODE_PAGE_EXTENDED = 0x15
        MODE_PAGE_EXTENDED_DEVICE_SPECIFIC = 0x16
        MODE_PAGE_CDVD_FEATURE_SET = 0x18
        MODE_PAGE_PROTOCOL_SPECIFIC_LUN = 0x18
        MODE_PAGE_PROTOCOL_SPECIFIC_PORT = 0x19
        MODE_PAGE_POWER_CONDITION = 0x1A
        MODE_PAGE_LUN_MAPPING = 0x1B
        MODE_PAGE_FAULT_REPORTING = 0x1C
        MODE_PAGE_CDVD_INACTIVITY = 0x1D        # cdrom
        MODE_PAGE_ELEMENT_ADDRESS = 0x1D
        MODE_PAGE_TRANSPORT_GEOMETRY = 0x1E
        MODE_PAGE_DEVICE_CAPABILITIES = 0x1F
        MODE_PAGE_CAPABILITIES = 0x2A        # cdrom
        MODE_SENSE_RETURN_ALL = 0x3F
        MODE_SENSE_CURRENT_VALUES = 0x00
        MODE_SENSE_CHANGEABLE_VALUES = 0x40
        MODE_SENSE_DEFAULT_VAULES = 0x80
        MODE_SENSE_SAVED_VALUES = 0xC0


        # SCSI CDB operation codes
        # 6 - byte commands:
        SCSIOP_TEST_UNIT_READY = 0x00
        SCSIOP_REZERO_UNIT = 0x01
        SCSIOP_REWIND = 0x01
        SCSIOP_REQUEST_BLOCK_ADDR = 0x02
        SCSIOP_REQUEST_SENSE = 0x03
        SCSIOP_FORMAT_UNIT = 0x04
        SCSIOP_READ_BLOCK_LIMITS = 0x05
        SCSIOP_REASSIGN_BLOCKS = 0x07
        SCSIOP_INIT_ELEMENT_STATUS = 0x07
        SCSIOP_READ6 = 0x08
        SCSIOP_RECEIVE = 0x08
        SCSIOP_WRITE6 = 0x0A
        SCSIOP_PRINT = 0x0A
        SCSIOP_SEND = 0x0A
        SCSIOP_SEEK6 = 0x0B
        SCSIOP_TRACK_SELECT = 0x0B
        SCSIOP_SLEW_PRINT = 0x0B
        SCSIOP_SET_CAPACITY = 0x0B        # tape
        SCSIOP_SEEK_BLOCK = 0x0C
        SCSIOP_PARTITION = 0x0D
        SCSIOP_READ_REVERSE = 0x0F
        SCSIOP_WRITE_FILEMARKS = 0x10
        SCSIOP_FLUSH_BUFFER = 0x10
        SCSIOP_SPACE = 0x11
        SCSIOP_INQUIRY = 0x12
        SCSIOP_VERIFY6 = 0x13
        SCSIOP_RECOVER_BUF_DATA = 0x14
        SCSIOP_MODE_SELECT = 0x15
        SCSIOP_RESERVE_UNIT = 0x16
        SCSIOP_RELEASE_UNIT = 0x17
        SCSIOP_COPY = 0x18
        SCSIOP_ERASE = 0x19
        SCSIOP_MODE_SENSE = 0x1A
        SCSIOP_START_STOP_UNIT = 0x1B
        SCSIOP_STOP_PRINT = 0x1B
        SCSIOP_LOAD_UNLOAD = 0x1B
        SCSIOP_RECEIVE_DIAGNOSTIC = 0x1C
        SCSIOP_SEND_DIAGNOSTIC = 0x1D
        SCSIOP_MEDIUM_REMOVAL = 0x1E

        # 10 - byte commands
        SCSIOP_READ_FORMATTED_CAPACITY = 0x23
        SCSIOP_READ_CAPACITY = 0x25
        SCSIOP_READ = 0x28
        SCSIOP_WRITE = 0x2A
        SCSIOP_SEEK = 0x2B
        SCSIOP_LOCATE = 0x2B
        SCSIOP_POSITION_TO_ELEMENT = 0x2B
        SCSIOP_WRITE_VERIFY = 0x2E
        SCSIOP_VERIFY = 0x2F
        SCSIOP_SEARCH_DATA_HIGH = 0x30
        SCSIOP_SEARCH_DATA_EQUAL = 0x31
        SCSIOP_SEARCH_DATA_LOW = 0x32
        SCSIOP_SET_LIMITS = 0x33
        SCSIOP_READ_POSITION = 0x34
        SCSIOP_SYNCHRONIZE_CACHE = 0x35
        SCSIOP_COMPARE = 0x39
        SCSIOP_COPY_COMPARE = 0x3A
        SCSIOP_WRITE_DATA_BUFF = 0x3B
        SCSIOP_READ_DATA_BUFF = 0x3C
        SCSIOP_WRITE_LONG = 0x3F
        SCSIOP_CHANGE_DEFINITION = 0x40
        SCSIOP_WRITE_SAME = 0x41
        SCSIOP_READ_SUB_CHANNEL = 0x42
        SCSIOP_UNMAP = 0x42        # block device
        SCSIOP_READ_TOC = 0x43
        SCSIOP_READ_HEADER = 0x44
        SCSIOP_REPORT_DENSITY_SUPPORT = 0x44        # tape
        SCSIOP_PLAY_AUDIO = 0x45
        SCSIOP_GET_CONFIGURATION = 0x46
        SCSIOP_PLAY_AUDIO_MSF = 0x47
        SCSIOP_PLAY_TRACK_INDEX = 0x48
        SCSIOP_SANITIZE = 0x48        # block device
        SCSIOP_PLAY_TRACK_RELATIVE = 0x49
        SCSIOP_GET_EVENT_STATUS = 0x4A
        SCSIOP_PAUSE_RESUME = 0x4B
        SCSIOP_LOG_SELECT = 0x4C
        SCSIOP_LOG_SENSE = 0x4D
        SCSIOP_STOP_PLAY_SCAN = 0x4E
        SCSIOP_XDWRITE = 0x50
        SCSIOP_XPWRITE = 0x51
        SCSIOP_READ_DISK_INFORMATION = 0x51
        SCSIOP_READ_DISC_INFORMATION = 0x51        # proper use of disc over disk
        SCSIOP_READ_TRACK_INFORMATION = 0x52
        SCSIOP_XDWRITE_READ = 0x53
        SCSIOP_RESERVE_TRACK_RZONE = 0x53
        SCSIOP_SEND_OPC_INFORMATION = 0x54        # optimum power calibration
        SCSIOP_MODE_SELECT10 = 0x55
        SCSIOP_RESERVE_UNIT10 = 0x56
        SCSIOP_RESERVE_ELEMENT = 0x56
        SCSIOP_RELEASE_UNIT10 = 0x57
        SCSIOP_RELEASE_ELEMENT = 0x57
        SCSIOP_REPAIR_TRACK = 0x58
        SCSIOP_MODE_SENSE10 = 0x5A
        SCSIOP_CLOSE_TRACK_SESSION = 0x5B
        SCSIOP_READ_BUFFER_CAPACITY = 0x5C
        SCSIOP_SEND_CUE_SHEET = 0x5D
        SCSIOP_PERSISTENT_RESERVE_IN = 0x5E
        SCSIOP_PERSISTENT_RESERVE_OUT = 0x5F

        # 12 - byte commands
        SCSIOP_REPORT_LUNS = 0xA0
        SCSIOP_BLANK = 0xA1
        SCSIOP_ATA_PASSTHROUGH12 = 0xA1
        SCSIOP_SEND_EVENT = 0xA2
        SCSIOP_SECURITY_PROTOCOL_IN = 0xA2
        SCSIOP_SEND_KEY = 0xA3
        SCSIOP_MAINTENANCE_IN = 0xA3
        SCSIOP_REPORT_KEY = 0xA4
        SCSIOP_MAINTENANCE_OUT = 0xA4
        SCSIOP_MOVE_MEDIUM = 0xA5
        SCSIOP_LOAD_UNLOAD_SLOT = 0xA6
        SCSIOP_EXCHANGE_MEDIUM = 0xA6
        SCSIOP_SET_READ_AHEAD = 0xA7
        SCSIOP_MOVE_MEDIUM_ATTACHED = 0xA7
        SCSIOP_READ12 = 0xA8
        SCSIOP_GET_MESSAGE = 0xA8
        SCSIOP_SERVICE_ACTION_OUT12 = 0xA9
        SCSIOP_WRITE12 = 0xAA
        SCSIOP_SEND_MESSAGE = 0xAB
        SCSIOP_SERVICE_ACTION_IN12 = 0xAB
        SCSIOP_GET_PERFORMANCE = 0xAC
        SCSIOP_READ_DVD_STRUCTURE = 0xAD
        SCSIOP_WRITE_VERIFY12 = 0xAE
        SCSIOP_VERIFY12 = 0xAF
        SCSIOP_SEARCH_DATA_HIGH12 = 0xB0
        SCSIOP_SEARCH_DATA_EQUAL12 = 0xB1
        SCSIOP_SEARCH_DATA_LOW12 = 0xB2
        SCSIOP_SET_LIMITS12 = 0xB3
        SCSIOP_READ_ELEMENT_STATUS_ATTACHED = 0xB4
        SCSIOP_REQUEST_VOL_ELEMENT = 0xB5
        SCSIOP_SECURITY_PROTOCOL_OUT = 0xB5
        SCSIOP_SEND_VOLUME_TAG = 0xB6
        SCSIOP_SET_STREAMING = 0xB6        # C/DVD
        SCSIOP_READ_DEFECT_DATA = 0xB7
        SCSIOP_READ_ELEMENT_STATUS = 0xB8
        SCSIOP_READ_CD_MSF = 0xB9
        SCSIOP_SCAN_CD = 0xBA
        SCSIOP_REDUNDANCY_GROUP_IN = 0xBA
        SCSIOP_SET_CD_SPEED = 0xBB
        SCSIOP_REDUNDANCY_GROUP_OUT = 0xBB
        SCSIOP_PLAY_CD = 0xBC
        SCSIOP_SPARE_IN = 0xBC
        SCSIOP_MECHANISM_STATUS = 0xBD
        SCSIOP_SPARE_OUT = 0xBD
        SCSIOP_READ_CD = 0xBE
        SCSIOP_VOLUME_SET_IN = 0xBE
        SCSIOP_SEND_DVD_STRUCTURE = 0xBF
        SCSIOP_VOLUME_SET_OUT = 0xBF
        SCSIOP_INIT_ELEMENT_RANGE = 0xE7

        # 16 - byte commands
        SCSIOP_XDWRITE_EXTENDED16 = 0x80        # disk
        SCSIOP_WRITE_FILEMARKS16 = 0x80        # tape
        SCSIOP_REBUILD16 = 0x81        # disk
        SCSIOP_READ_REVERSE16 = 0x81        # tape
        SCSIOP_REGENERATE16 = 0x82        # disk
        SCSIOP_EXTENDED_COPY = 0x83
        SCSIOP_POPULATE_TOKEN = 0x83        # disk
        SCSIOP_WRITE_USING_TOKEN = 0x83        # disk
        SCSIOP_RECEIVE_COPY_RESULTS = 0x84
        SCSIOP_RECEIVE_ROD_TOKEN_INFORMATION = 0x84        # disk
        SCSIOP_ATA_PASSTHROUGH16 = 0x85
        SCSIOP_ACCESS_CONTROL_IN = 0x86
        SCSIOP_ACCESS_CONTROL_OUT = 0x87
        SCSIOP_READ16 = 0x88
        SCSIOP_COMPARE_AND_WRITE = 0x89
        SCSIOP_WRITE16 = 0x8A
        SCSIOP_READ_ATTRIBUTES = 0x8C
        SCSIOP_WRITE_ATTRIBUTES = 0x8D
        SCSIOP_WRITE_VERIFY16 = 0x8E
        SCSIOP_VERIFY16 = 0x8F
        SCSIOP_PREFETCH16 = 0x90
        SCSIOP_SYNCHRONIZE_CACHE16 = 0x91
        SCSIOP_SPACE16 = 0x91        # tape
        SCSIOP_LOCK_UNLOCK_CACHE16 = 0x92
        SCSIOP_LOCATE16 = 0x92        # tape
        SCSIOP_WRITE_SAME16 = 0x93
        SCSIOP_ERASE16 = 0x93        # tape
        SCSIOP_ZBC_OUT = 0x94        # Close Zone, Finish Zone, Open Zone, Reset Write Pointer, etc.
        SCSIOP_ZBC_IN = 0x95        # Report Zones, etc.
        SCSIOP_READ_CAPACITY16 = 0x9E
        SCSIOP_GET_LBA_STATUS = 0x9E
        SCSIOP_GET_PHYSICAL_ELEMENT_STATUS = 0x9E
        SCSIOP_REMOVE_ELEMENT_AND_TRUNCATE = 0x9E
        SCSIOP_SERVICE_ACTION_IN16 = 0x9E
        SCSIOP_SERVICE_ACTION_OUT16 = 0x9F

        # 32 - byte commands
        SCSIOP_OPERATION32 = 0x7F


        # SCSIOP_SANITIZE - 0x48
        SERVICE_ACTION_OVERWRITE = 0x01
        SERVICE_ACTION_BLOCK_ERASE = 0x02
        SERVICE_ACTION_CRYPTO_ERASE = 0x03
        SERVICE_ACTION_EXIT_FAILURE = 0x1F


        # SCSIOP_OPERATION32 - 0x7F
        SERVICE_ACTION_XDWRITE = 0x0004
        SERVICE_ACTION_XPWRITE = 0x0006
        SERVICE_ACTION_XDWRITEREAD = 0x0007
        SERVICE_ACTION_WRITE = 0x000B
        SERVICE_ACTION_WRITE_VERIFY = 0x000C
        SERVICE_ACTION_WRITE_SAME = 0x000D
        SERVICE_ACTION_ORWRITE = 0x000E


        # SCSIOP_POPULATE_TOKEN, SCSIOP_WRITE_USING_TOKEN - 0x83
        SERVICE_ACTION_POPULATE_TOKEN = 0x10
        SERVICE_ACTION_WRITE_USING_TOKEN = 0x11


        # SCSIOP_RECEIVE_ROD_TOKEN_INFORMATION - 0x84
        SERVICE_ACTION_RECEIVE_TOKEN_INFORMATION = 0x07


        # SCSIOP_ZBC_OUT - 0x94
        SERVICE_ACTION_CLOSE_ZONE = 0x01
        SERVICE_ACTION_FINISH_ZONE = 0x02
        SERVICE_ACTION_OPEN_ZONE = 0x03
        SERVICE_ACTION_RESET_WRITE_POINTER = 0x04


        # SCSIOP_ZBC_IN - 0x95
        SERVICE_ACTION_REPORT_ZONES = 0x00
        REPORT_ZONES_OPTION_LIST_ALL_ZONES = 0x00
        REPORT_ZONES_OPTION_LIST_EMPTY_ZONES = 0x01
        REPORT_ZONES_OPTION_LIST_IMPLICITLY_OPENED_ZONES = 0x02
        REPORT_ZONES_OPTION_LIST_EXPLICITLY_OPENED_ZONES = 0x03
        REPORT_ZONES_OPTION_LIST_CLOSED_ZONES = 0x04
        REPORT_ZONES_OPTION_LIST_FULL_ZONES = 0x05
        REPORT_ZONES_OPTION_LIST_READ_ONLY_ZONES = 0x06
        REPORT_ZONES_OPTION_LIST_OFFLINE_ZONES = 0x07
        REPORT_ZONES_OPTION_LIST_RWP_ZONES = 0x10
        REPORT_ZONES_OPTION_LIST_NON_SEQUENTIAL_WRITE_RESOURCES_ACTIVE_ZONES = (
            0x11
        )
        REPORT_ZONES_OPTION_LIST_NOT_WRITE_POINTER_ZONES = 0x3F


        # SCSIOP_SERVICE_ACTION_IN16 - 0x9E
        SERVICE_ACTION_READ_CAPACITY16 = 0x10
        SERVICE_ACTION_GET_LBA_STATUS = 0x12
        SERVICE_ACTION_GET_PHYSICAL_ELEMENT_STATUS = 0x17
        SERVICE_ACTION_REMOVE_ELEMENT_AND_TRUNCATE = 0x18


        # SCSIOP_MAINTENANCE_IN - 0xA3
        SERVICE_ACTION_REPORT_TIMESTAMP = 0x0F


        # SCSIOP_MAINTENANCE_OUT - 0xA4
        SERVICE_ACTION_SET_TIMESTAMP = 0x0F


        # If the IMMED bit is 1, status is returned as soon
        # as the operation is initiated. If the IMMED bit
        # is 0, status is not returned until the operation
        # is completed.
        CDB_RETURN_ON_COMPLETION = 0
        CDB_RETURN_IMMEDIATE = 1

        # end_ntminitape
        # CDB Force media access used in extended read and write commands.
        CDB_FORCE_MEDIA_ACCESS = 0x08


        # Denon CD ROM operation codes
        SCSIOP_DENON_EJECT_DISC = 0xE6
        SCSIOP_DENON_STOP_AUDIO = 0xE7
        SCSIOP_DENON_PLAY_AUDIO = 0xE8
        SCSIOP_DENON_READ_TOC = 0xE9
        SCSIOP_DENON_READ_SUBCODE = 0xEB


        # SCSI Bus Messages
        SCSIMESS_ABORT = 0x06
        SCSIMESS_ABORT_WITH_TAG = 0x0D
        SCSIMESS_BUS_DEVICE_RESET = 0x0C
        SCSIMESS_CLEAR_QUEUE = 0x0E
        SCSIMESS_COMMAND_COMPLETE = 0x00
        SCSIMESS_DISCONNECT = 0x04
        SCSIMESS_EXTENDED_MESSAGE = 0x01
        SCSIMESS_IDENTIFY = 0x80
        SCSIMESS_IDENTIFY_WITH_DISCON = 0xC0
        SCSIMESS_IGNORE_WIDE_RESIDUE = 0x23
        SCSIMESS_INITIATE_RECOVERY = 0x0F
        SCSIMESS_INIT_DETECTED_ERROR = 0x05
        SCSIMESS_LINK_CMD_COMP = 0x0A
        SCSIMESS_LINK_CMD_COMP_W_FLAG = 0x0B
        SCSIMESS_MESS_PARITY_ERROR = 0x09
        SCSIMESS_MESSAGE_REJECT = 0x07
        SCSIMESS_NO_OPERATION = 0x08
        SCSIMESS_HEAD_OF_QUEUE_TAG = 0x21
        SCSIMESS_ORDERED_QUEUE_TAG = 0x22
        SCSIMESS_SIMPLE_QUEUE_TAG = 0x20
        SCSIMESS_RELEASE_RECOVERY = 0x10
        SCSIMESS_RESTORE_POINTERS = 0x03
        SCSIMESS_SAVE_DATA_POINTER = 0x02
        SCSIMESS_TERMINATE_IO_PROCESS = 0x11


        # SCSI Extended Message operation codes
        SCSIMESS_MODIFY_DATA_POINTER = 0x00
        SCSIMESS_SYNCHRONOUS_DATA_REQ = 0x01
        SCSIMESS_WIDE_DATA_REQUEST = 0x03


        # SCSI Extended Message Lengths
        SCSIMESS_MODIFY_DATA_LENGTH = 5
        SCSIMESS_SYNCH_DATA_LENGTH = 3
        SCSIMESS_WIDE_DATA_LENGTH = 2


        # SCSI extended message structure
        class _EXTENDED_ARGUMENTS(ctypes.Union):
            pass


        class Modify(ctypes.Structure):
            pass


        Modify._fields_ = [
            ('Modifier', UCHAR * 4),
        ]
        _EXTENDED_ARGUMENTS.Modify = Modify


        class Synchronous(ctypes.Structure):
            pass


        Synchronous._fields_ = [
            ('TransferPeriod', UCHAR),
            ('ReqAckOffset', UCHAR),
        ]
        _EXTENDED_ARGUMENTS.Synchronous = Synchronous


        class Wide(ctypes.Structure):
            pass


        Wide._fields_ = [
            ('Width', UCHAR),
        ]

        _EXTENDED_ARGUMENTS.Wide = Wide

        _EXTENDED_ARGUMENTS._fields_ = [
            ('Modify', _EXTENDED_ARGUMENTS.Modify),
            ('Synchronous', _EXTENDED_ARGUMENTS.Synchronous),
            ('Wide', _EXTENDED_ARGUMENTS.Wide),
        ]
        ExtendedArguments = _EXTENDED_ARGUMENTS

        _SCSI_EXTENDED_MESSAGE.ExtendedArguments = ExtendedArguments
        _SCSI_EXTENDED_MESSAGE._fields_ = [
            ('InitialMessageCode', UCHAR),
            ('MessageLength', UCHAR),
            ('MessageType', UCHAR),
            ('ExtendedArguments', _SCSI_EXTENDED_MESSAGE.ExtendedArguments),
        ]
        # SCSI bus status codes.
        SCSISTAT_GOOD = 0x00
        SCSISTAT_CHECK_CONDITION = 0x02
        SCSISTAT_CONDITION_MET = 0x04
        SCSISTAT_BUSY = 0x08
        SCSISTAT_INTERMEDIATE = 0x10
        SCSISTAT_INTERMEDIATE_COND_MET = 0x14
        SCSISTAT_RESERVATION_CONFLICT = 0x18
        SCSISTAT_COMMAND_TERMINATED = 0x22
        SCSISTAT_QUEUE_FULL = 0x28
        # Enable Vital Product Data Flag (EVPD)
        # used with INQUIRY command.
        CDB_INQUIRY_EVPD = 0x01
        # Defines for format CDB
        LUN0_FORMAT_SAVING_DEFECT_LIST = 0
        USE_DEFAULTMSB = 0
        USE_DEFAULTLSB = 0
        START_UNIT_CODE = 0x01
        STOP_UNIT_CODE = 0x00
        # begin_ntminitape
        # Inquiry buffer structure. This is the data returned from the target
        # after it receives an inquiry.
        # This structure may be extended by the number of bytes specified
        # in the field AdditionalLength. The defined size constant only
        # includes fields through ProductRevisionLevel.
        # The NT SCSI drivers are only interested in the first 36 bytes of
        # data.
        INQUIRYDATABUFFERSIZE = 36
        VERSION_DESCRIPTOR = USHORT
        PVERSION_DESCRIPTOR = POINTER(USHORT)

        if NTDDI_VERSION < NTDDI_WINXP:
            _INQUIRYDATA._fields_ = [
                ('DeviceType', UCHAR, 5),
                ('DeviceTypeQualifier', UCHAR, 3),
                ('DeviceTypeModifier', UCHAR, 7),
                ('RemovableMedia', UCHAR, 1),
                ('Versions', UCHAR),
                ('ResponseDataFormat', UCHAR, 4),
                ('HiSupport', UCHAR, 1),
                ('NormACA', UCHAR, 1),
                ('ReservedBit', UCHAR, 1),
                ('AERC', UCHAR, 1),
                ('AdditionalLength', UCHAR),
                ('Reserved', UCHAR * 2),
                ('SoftReset', UCHAR, 1),
                ('CommandQueue', UCHAR, 1),
                ('Reserved2', UCHAR, 1),
                ('LinkedCommands', UCHAR, 1),
                ('Synchronous', UCHAR, 1),
                ('Wide16Bit', UCHAR, 1),
                ('Wide32Bit', UCHAR, 1),
                ('RelativeAddressing', UCHAR, 1),
                ('VendorId', UCHAR * 8),
                ('ProductId', UCHAR * 16),
                ('ProductRevisionLevel', UCHAR * 4),
                ('VendorSpecific', UCHAR * 20),
                ('Reserved3', UCHAR * 2),
                ('VersionDescriptors', VERSION_DESCRIPTOR * 8),
                ('Reserved4', UCHAR * 30),
            ]
        else:

            class _Union_13(ctypes.Union):
                pass


            class _Struct_5(ctypes.Structure):
                pass


            _Struct_5._fields_ = [
                ('ANSIVersion', UCHAR, 3),
                ('ECMAVersion', UCHAR, 3),
                ('ISOVersion', UCHAR, 2),
            ]
            _Union_13._Struct_5 = _Struct_5

            _Union_13._anonymous_ = (
                '_Struct_5',
            )

            _Union_13._fields_ = [
                ('Versions', UCHAR),
                ('_Struct_5', _Union_13._Struct_5),
            ]
            _INQUIRYDATA._Union_13 = _Union_13


            class _Union_14(ctypes.Union):
                pass


            class _Struct_6(ctypes.Structure):
                pass


            _Struct_6._fields_ = [
                ('PROTECT', UCHAR, 1),
                ('Reserved_1', UCHAR, 2),
                ('ThirdPartyCoppy', UCHAR, 1),
                ('TPGS', UCHAR, 2),
                ('ACC', UCHAR, 1),
                ('SCCS', UCHAR, 1),
            ]
            _Union_14._Struct_6 = _Struct_6

            _Union_14._anonymous_ = (
                '_Struct_6',
            )

            _Union_2._fields_ = [
                ('Reserved', UCHAR),
                ('_Struct_6', _Union_14._Struct_6),
            ]
            _INQUIRYDATA._Union_14 = _Union_14

            _INQUIRYDATA._anonymous_ = (
                '_Union_13',
                '_Union_14',
            )

            _INQUIRYDATA._fields_ = [
                ('DeviceType', UCHAR, 5),
                ('DeviceTypeQualifier', UCHAR, 3),
                ('DeviceTypeModifier', UCHAR, 7),
                ('RemovableMedia', UCHAR, 1),
                ('_Union_13', _INQUIRYDATA._Union_13),
                ('ResponseDataFormat', UCHAR, 4),
                ('HiSupport', UCHAR, 1),
                ('NormACA', UCHAR, 1),
                ('TerminateTask', UCHAR, 1),
                ('AERC', UCHAR, 1),
                ('AdditionalLength', UCHAR),
                ('_Union_14', _INQUIRYDATA._Union_14),
                # defined only for SIP devices.
                ('Addr16', UCHAR, 1),
                # defined only for SIP devices.
                ('Addr32', UCHAR, 1),
                # defined only for SIP devices.
                ('AckReqQ', UCHAR, 1),
                ('MediumChanger', UCHAR, 1),
                ('MultiPort', UCHAR, 1),
                ('ReservedBit2', UCHAR, 1),
                ('EnclosureServices', UCHAR, 1),
                ('ReservedBit3', UCHAR, 1),
                ('SoftReset', UCHAR, 1),
                ('CommandQueue', UCHAR, 1),
                # defined only for SIP devices.
                ('TransferDisable', UCHAR, 1),
                ('LinkedCommands', UCHAR, 1),
                # defined only for SIP devices.
                ('Synchronous', UCHAR, 1),
                # defined only for SIP devices.
                ('Wide16Bit', UCHAR, 1),
                # defined only for SIP devices.
                ('Wide32Bit', UCHAR, 1),
                ('RelativeAddressing', UCHAR, 1),
                ('VendorId', UCHAR * 8),
                ('ProductId', UCHAR * 16),
                ('ProductRevisionLevel', UCHAR * 4),
                ('VendorSpecific', UCHAR * 20),
                ('Reserved3', UCHAR * 2),
                ('VersionDescriptors', VERSION_DESCRIPTOR * 8),
                ('Reserved4', UCHAR * 30),
            ]

        # END IF
        OFFSET_VER_DESCRIPTOR_ONE = (
            FIELD_OFFSET(INQUIRYDATA, 'VersionDescriptors[0]')
        )
        OFFSET_VER_DESCRIPTOR_EIGHT = (
            FIELD_OFFSET(INQUIRYDATA, 'VersionDescriptors[8]')
        )


        # Inquiry defines. Used to interpret data returned from target as
        # result
        # of inquiry command.
        # DeviceType field
        DIRECT_ACCESS_DEVICE = 0x00        # disks
        SEQUENTIAL_ACCESS_DEVICE = 0x01        # tapes
        PRINTER_DEVICE = 0x02        # printers
        PROCESSOR_DEVICE = 0x03        # scanners, printers, etc
        WRITE_ONCE_READ_MULTIPLE_DEVICE = 0x04        # worms
        READ_ONLY_DIRECT_ACCESS_DEVICE = 0x05        # cdroms
        SCANNER_DEVICE = 0x06        # scanners
        OPTICAL_DEVICE = 0x07        # optical disks
        MEDIUM_CHANGER = 0x08        # jukebox
        COMMUNICATION_DEVICE = 0x09        # network

        # 0xA and 0xB are obsolete
        ARRAY_CONTROLLER_DEVICE = 0x0C
        SCSI_ENCLOSURE_DEVICE = 0x0D
        REDUCED_BLOCK_DEVICE = 0x0E        # e.g., 1394 disk
        OPTICAL_CARD_READER_WRITER_DEVICE = 0x0F
        BRIDGE_CONTROLLER_DEVICE = 0x10
        OBJECT_BASED_STORAGE_DEVICE = 0x11        # OSD
        HOST_MANAGED_ZONED_BLOCK_DEVICE = 0x14        # Host managed zoned block device
        UNKNOWN_OR_NO_DEVICE = 0x1F        # Unknown or no device type
        LOGICAL_UNIT_NOT_PRESENT_DEVICE = 0x7F
        DEVICE_QUALIFIER_ACTIVE = 0x00
        DEVICE_QUALIFIER_NOT_ACTIVE = 0x01
        DEVICE_QUALIFIER_NOT_SUPPORTED = 0x03

        # DeviceTypeQualifier field
        DEVICE_CONNECTED = 0x00

        # Vital Product Data Pages
        # Unit Serial Number Page (page code 0x80)
        # Provides a product serial number for the target or the logical unit.
        _TEMP__VPD_MEDIA_SERIAL_NUMBER_PAGE = [
            ('DeviceType', UCHAR, 5),
            ('DeviceTypeQualifier', UCHAR, 3),
            ('PageCode', UCHAR),
            ('Reserved', UCHAR),
            ('PageLength', UCHAR),
        ]
        if not defined(__midl):
            _TEMP__VPD_MEDIA_SERIAL_NUMBER_PAGE += [
                ('SerialNumber', UCHAR * 0),
            ]
        # END IF
        _VPD_MEDIA_SERIAL_NUMBER_PAGE._fields_ = _TEMP__VPD_MEDIA_SERIAL_NUMBER_PAGE

        _TEMP__VPD_SERIAL_NUMBER_PAGE = [
            ('DeviceType', UCHAR, 5),
            ('DeviceTypeQualifier', UCHAR, 3),
            ('PageCode', UCHAR),
            ('Reserved', UCHAR),
            ('PageLength', UCHAR),
        ]
        if not defined(__midl):
            _TEMP__VPD_SERIAL_NUMBER_PAGE += [
                ('SerialNumber', UCHAR * 0),
            ]
        # END IF
        _VPD_SERIAL_NUMBER_PAGE._fields_ = _TEMP__VPD_SERIAL_NUMBER_PAGE


        # Device Identification Page (page code 0x83)
        # Provides the means to retrieve zero or more identification
        # descriptors
        # applying to the logical unit.
        class _VPD_CODE_SET(ENUM):
            VpdCodeSetReserved = 0
            VpdCodeSetBinary = 1
            VpdCodeSetAscii = 2
            VpdCodeSetUTF8 = 3

        VPD_CODE_SET = _VPD_CODE_SET
        PVPD_CODE_SET = POINTER(_VPD_CODE_SET)


        class _VPD_ASSOCIATION(ENUM):
            VpdAssocDevice = 0
            VpdAssocPort = 1
            VpdAssocTarget = 2
            VpdAssocReserved1 = 3
            VpdAssocReserved2 = 4

        VPD_ASSOCIATION = _VPD_ASSOCIATION
        PVPD_ASSOCIATION = POINTER(_VPD_ASSOCIATION)


        class _VPD_IDENTIFIER_TYPE(ENUM):
            VpdIdentifierTypeVendorSpecific = 0
            VpdIdentifierTypeVendorId = 1
            VpdIdentifierTypeEUI64 = 2
            VpdIdentifierTypeFCPHName = 3
            VpdIdentifierTypePortRelative = 4
            VpdIdentifierTypeTargetPortGroup = 5
            VpdIdentifierTypeLogicalUnitGroup = 6
            VpdIdentifierTypeMD5LogicalUnitId = 7
            VpdIdentifierTypeSCSINameString = 8

        VPD_IDENTIFIER_TYPE = _VPD_IDENTIFIER_TYPE
        PVPD_IDENTIFIER_TYPE = POINTER(_VPD_IDENTIFIER_TYPE)

        _TEMP__VPD_IDENTIFICATION_DESCRIPTOR = [
            # VPD_CODE_SET
            ('CodeSet', UCHAR, 4),
            ('Reserved', UCHAR, 4),
            # VPD_IDENTIFIER_TYPE
            ('IdentifierType', UCHAR, 4),
            ('Association', UCHAR, 2),
            ('Reserved2', UCHAR, 2),
            ('Reserved3', UCHAR),
            ('IdentifierLength', UCHAR),
        ]
        if not defined(__midl):
            _TEMP__VPD_IDENTIFICATION_DESCRIPTOR += [
                ('Identifier', UCHAR * 0),
            ]
        # END IF
        _VPD_IDENTIFICATION_DESCRIPTOR._fields_ = _TEMP__VPD_IDENTIFICATION_DESCRIPTOR

        _TEMP__VPD_IDENTIFICATION_PAGE = [
            ('DeviceType', UCHAR, 5),
            ('DeviceTypeQualifier', UCHAR, 3),
            ('PageCode', UCHAR),
            ('Reserved', UCHAR),
            ('PageLength', UCHAR),
        ]
        if not defined(__midl):
            _TEMP__VPD_IDENTIFICATION_PAGE += [
                # VPD_IDENTIFICATION_DESCRIPTOR Descriptors[0];
                ('Descriptors', UCHAR * 0),
            ]
        # END IF
        _VPD_IDENTIFICATION_PAGE._fields_ = _TEMP__VPD_IDENTIFICATION_PAGE


        # VPD Page 0x86, Extended INQUIRY Data
        _VPD_EXTENDED_INQUIRY_DATA_PAGE._fields_ = [
            ('DeviceType', UCHAR, 5),
            ('DeviceTypeQualifier', UCHAR, 3),
            # 86h
            ('PageCode', UCHAR),
            # [0] - 00h, [1] - 3Ch
            ('PageLength', UCHAR * 2),
            # byte 4 bit 0
            ('RefChk', UCHAR, 1),
            ('AppChk', UCHAR, 1),
            ('GrdChk', UCHAR, 1),
            ('Spt', UCHAR, 3),
            ('ActivateMicrocode', UCHAR, 2),
            # byte 5 bit 0
            ('SimpSup', UCHAR, 1),
            ('OrdSup', UCHAR, 1),
            ('HeadSup', UCHAR, 1),
            ('PriorSup', UCHAR, 1),
            ('GroupSup', UCHAR, 1),
            ('UaskSup', UCHAR, 1),
            ('Reserved0', UCHAR, 2),
            # byte 6 bit 0
            ('VSup', UCHAR, 1),
            ('NvSup', UCHAR, 1),
            ('Obsolete0', UCHAR, 1),
            ('WuSup', UCHAR, 1),
            ('Reserved1', UCHAR, 4),
            # byte 7 bit 0
            ('LuiClr', UCHAR, 1),
            ('Reserved2', UCHAR, 3),
            ('PiiSup', UCHAR, 1),
            ('NoPiChk', UCHAR, 1),
            ('Reserved3', UCHAR, 2),
            # byte 8 bit 0
            ('Obsolete1', UCHAR, 1),
            ('HssRelef', UCHAR, 1),
            ('Reserved4', UCHAR, 1),
            ('RtdSup', UCHAR, 1),
            ('RSup', UCHAR, 1),
            ('LuCollectionType', UCHAR, 3),
            # byte 9 bit 0
            ('Multi_i_t_Nexus_Microcode_Download', UCHAR, 4),
            ('Reserved5', UCHAR, 4),
            ('ExtendedSelfTestCompletionMinutes', UCHAR * 2),
            # byte 12 bit 0
            ('Reserved6', UCHAR, 5),
            ('VsaSup', UCHAR, 1),
            ('HraSup', UCHAR, 1),
            ('PoaSup', UCHAR, 1),
            ('MaxSupportedSenseDataLength', UCHAR),
            # byte 14 bit 0
            ('Nrd0', UCHAR, 1),
            ('Nrd1', UCHAR, 1),
            ('Sac', UCHAR, 1),
            ('Reserved7', UCHAR, 3),
            ('Ias', UCHAR, 1),
            ('Ibs', UCHAR, 1),
            ('MaxInquiryChangeLogs', UCHAR * 2),
            ('MaxModePageChangeLogs', UCHAR * 2),
            ('Reserved8', UCHAR * 45),
        ]


        # VPD Page 0x89, ATA Information
        _VPD_ATA_INFORMATION_PAGE._fields_ = [
            ('DeviceType', UCHAR, 5),
            ('DeviceTypeQualifier', UCHAR, 3),
            # 0x89
            ('PageCode', UCHAR),
            # 0x238 fixed size
            ('PageLength', UCHAR * 2),
            ('Reserved0', UCHAR * 4),
            ('VendorId', UCHAR * 8),
            ('ProductId', UCHAR * 16),
            ('ProductRevisionLevel', UCHAR * 4),
            ('DeviceSignature', UCHAR * 20),
            ('CommandCode', UCHAR),
            ('Reserved1', UCHAR * 3),
            ('IdentifyDeviceData', UCHAR * 512),
        ]

        if NTDDI_VERSION >= NTDDI_WIN8:
            # VPD Page 0x8F, Third Party Copy
            _TEMP__VPD_THIRD_PARTY_COPY_PAGE = [
                ('DeviceType', UCHAR, 5),
                ('DeviceTypeQualifier', UCHAR, 3),
                # 0x8F
                ('PageCode', UCHAR),
                # at least 0x24 if target supports Windows Offload Data
                # Transfers
                ('PageLength', UCHAR * 2),
            ]
            if not defined(__midl):
                _TEMP__VPD_THIRD_PARTY_COPY_PAGE += [
                    ('ThirdPartyCopyDescriptors', UCHAR * ANYSIZE_ARRAY),
                ]
            # END IF
            _VPD_THIRD_PARTY_COPY_PAGE._fields_ = _TEMP__VPD_THIRD_PARTY_COPY_PAGE

            _WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR._fields_ = [
                # 0x00
                ('DescriptorType', UCHAR * 2),
                # 0x20
                ('DescriptorLength', UCHAR * 2),
                ('VendorSpecific', UCHAR * 6),
                ('MaximumRangeDescriptors', UCHAR * 2),
                ('MaximumInactivityTimer', UCHAR * 4),
                ('DefaultInactivityTimer', UCHAR * 4),
                ('MaximumTokenTransferSize', UCHAR * 8),
                ('OptimalTransferCount', UCHAR * 8),
            ]
            BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR_TYPE_WINDOWS = 0x00
        # END IF  (NTDDI_VERSION >= NTDDI_WIN8)

        # VPD Page 0xB0, Block Limits
        class _Union_3(ctypes.Union):
            pass


        class _Struct_1(ctypes.Structure):
            pass


        class _Union_4(ctypes.Union):
            pass


        class _Struct_2(ctypes.Structure):
            pass


        _Struct_2._fields_ = [
            ('UnmapGranularityAlignmentByte3', UCHAR, 7),
            ('UGAValid', UCHAR, 1),
            ('UnmapGranularityAlignmentByte2', UCHAR),
            ('UnmapGranularityAlignmentByte1', UCHAR),
            ('UnmapGranularityAlignmentByte0', UCHAR),
        ]
        _Union_4._Struct_2 = _Struct_2

        _Union_4._anonymous_ = (
            '_Struct_2',
        )

        _Union_4._fields_ = [
            ('_Struct_2', _Union_4._Struct_2),
            ('UnmapGranularityAlignment', UCHAR * 4),
        ]
        _Struct_1._Union_4 = _Union_4

        _Struct_1._anonymous_ = (
            '_Union_4',
        )

        _Struct_1._fields_ = [
            ('Reserved0', UCHAR),
            ('MaximumCompareAndWriteLength', UCHAR),
            ('OptimalTransferLengthGranularity', UCHAR * 2),
            ('MaximumTransferLength', UCHAR * 4),
            ('OptimalTransferLength', UCHAR * 4),
            ('MaxPrefetchXDReadXDWriteTransferLength', UCHAR * 4),
            ('MaximumUnmapLBACount', UCHAR * 4),
            ('MaximumUnmapBlockDescriptorCount', UCHAR * 4),
            ('OptimalUnmapGranularity', UCHAR * 4),
            ('_Union_4', _Struct_1._Union_4),
            ('Reserved1', UCHAR * 28),
        ]
        _Union_3._Struct_1 = _Struct_1

        _Union_3._anonymous_ = (
            '_Struct_1',
        )

        _TEMP__Union_3 = [
            ('_Struct_1', _Union_3._Struct_1),
        ]
        if not defined(__midl):
            _TEMP__Union_3 += [
                ('Descriptors', UCHAR * 0),
            ]
        # END IF
        _Union_3._fields_ = _TEMP__Union_3
        _VPD_BLOCK_LIMITS_PAGE._Union_3 = _Union_3

        _VPD_BLOCK_LIMITS_PAGE._anonymous_ = (
            '_Union_3',
        )

        _VPD_BLOCK_LIMITS_PAGE._fields_ = [
            ('DeviceType', UCHAR, 5),
            ('DeviceTypeQualifier', UCHAR, 3),
            # 0xB0
            ('PageCode', UCHAR),
            # 0x3C if device supports logical block provisioning, otherwise
            # the value may be 0x10.
            ('PageLength', UCHAR * 2),
            ('_Union_3', _VPD_BLOCK_LIMITS_PAGE._Union_3),
        ]


        # VPD Page 0xB1, Block Device Characteristics
        ZONED_CAPABILITIES_NOT_REPORTED = 0x0
        ZONED_CAPABILITIES_HOST_AWARE = 0x1
        ZONED_CAPABILITIES_DEVICE_MANAGED = 0x2


        _VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE._fields_ = [
            ('DeviceType', UCHAR, 5),
            ('DeviceTypeQualifier', UCHAR, 3),
            # 0xB1
            ('PageCode', UCHAR),
            ('Reserved0', UCHAR),
            # 0x3C
            ('PageLength', UCHAR),
            ('MediumRotationRateMsb', UCHAR),
            ('MediumRotationRateLsb', UCHAR),
            ('MediumProductType', UCHAR),
            ('NominalFormFactor', UCHAR, 4),
            ('WACEREQ', UCHAR, 2),
            ('WABEREQ', UCHAR, 2),
            ('VBULS', UCHAR, 1),
            ('FUAB', UCHAR, 1),
            ('BOCS', UCHAR, 1),
            ('Reserved1', UCHAR, 1),
            ('ZONED', UCHAR, 2),
            ('Reserved2', UCHAR, 2),
            ('Reserved3', UCHAR * 3),
            ('DepopulationTime', UCHAR * 4),
            ('Reserved4', UCHAR * 48),
        ]


        # VPD Page 0xB2, Logical Block Provisioning
        PROVISIONING_TYPE_UNKNOWN = 0x0
        PROVISIONING_TYPE_RESOURCE = 0x1
        PROVISIONING_TYPE_THIN = 0x2


        _TEMP__VPD_LOGICAL_BLOCK_PROVISIONING_PAGE = [
            ('DeviceType', UCHAR, 5),
            ('DeviceTypeQualifier', UCHAR, 3),
            # 0xB2
            ('PageCode', UCHAR),
            ('PageLength', UCHAR * 2),
            ('ThresholdExponent', UCHAR),
            ('DP', UCHAR, 1),
            ('ANC_SUP', UCHAR, 1),
            ('LBPRZ', UCHAR, 1),
            ('Reserved0', UCHAR, 2),
            ('LBPWS10', UCHAR, 1),
            ('LBPWS', UCHAR, 1),
            ('LBPU', UCHAR, 1),
            ('ProvisioningType', UCHAR, 3),
            ('Reserved1', UCHAR, 5),
            ('Reserved2', UCHAR),
        ]
        if not defined(__midl):
            _TEMP__VPD_LOGICAL_BLOCK_PROVISIONING_PAGE += [
                ('ProvisioningGroupDescr', UCHAR * 0),
            ]
        # END IF
        _VPD_LOGICAL_BLOCK_PROVISIONING_PAGE._fields_ = _TEMP__VPD_LOGICAL_BLOCK_PROVISIONING_PAGE


        # VPD Page 0xB6, Zoned Block Device Characteristics
        _VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE._fields_ = [
            ('DeviceType', UCHAR, 5),
            ('DeviceTypeQualifier', UCHAR, 3),
            # 0xB6
            ('PageCode', UCHAR),
            # 0x3C
            ('PageLength', UCHAR * 2),
            # Unrestricted Read in Sequential Write Required Zone
            ('URSWRZ', UCHAR, 1),
            ('Reserved1', UCHAR, 7),
            ('Reserved2', UCHAR * 3),
            ('OptimalNumberOfOpenSequentialWritePreferredZone', UCHAR * 4),
            ('OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZone', UCHAR * 4),
            ('MaxNumberOfOpenSequentialWriteRequiredZone', UCHAR * 4),
            ('Reserved3', UCHAR * 44),
        ]


        # Supported Vital Product Data Pages Page (page code 0x00)
        # Contains a list of the vital product data page cods supported by the
        # target
        # or logical unit.
        _TEMP__VPD_SUPPORTED_PAGES_PAGE = [
            ('DeviceType', UCHAR, 5),
            ('DeviceTypeQualifier', UCHAR, 3),
            ('PageCode', UCHAR),
            ('Reserved', UCHAR),
            ('PageLength', UCHAR),
        ]
        if not defined(__midl):
            _TEMP__VPD_SUPPORTED_PAGES_PAGE += [
                ('SupportedPageList', UCHAR * 0),
            ]
        # END IF
        _VPD_SUPPORTED_PAGES_PAGE._fields_ = _TEMP__VPD_SUPPORTED_PAGES_PAGE
        VPD_MAX_BUFFER_SIZE = 0xFF
        VPD_SUPPORTED_PAGES = 0x00
        VPD_SERIAL_NUMBER = 0x80
        VPD_DEVICE_IDENTIFIERS = 0x83
        VPD_MEDIA_SERIAL_NUMBER = 0x84
        VPD_SOFTWARE_INTERFACE_IDENTIFIERS = 0x84
        VPD_NETWORK_MANAGEMENT_ADDRESSES = 0x85
        VPD_EXTENDED_INQUIRY_DATA = 0x86
        VPD_MODE_PAGE_POLICY = 0x87
        VPD_SCSI_PORTS = 0x88
        VPD_ATA_INFORMATION = 0x89
        VPD_THIRD_PARTY_COPY = 0x8F
        VPD_BLOCK_LIMITS = 0xB0
        VPD_BLOCK_DEVICE_CHARACTERISTICS = 0xB1
        VPD_LOGICAL_BLOCK_PROVISIONING = 0xB2
        VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS = 0xB6

        # //////////////////////////////////////////////////////////////////////////////
        #
        # Log page definitions
        LOG_PAGE_CODE_SUPPORTED_LOG_PAGES = 0x00
        LOG_PAGE_CODE_WRITE_ERROR_COUNTERS = 0x02
        LOG_PAGE_CODE_READ_ERROR_COUNTERS = 0x03
        LOG_PAGE_CODE_LOGICAL_BLOCK_PROVISIONING = 0x0C
        LOG_PAGE_CODE_TEMPERATURE = 0x0D
        LOG_PAGE_CODE_STARTSTOP_CYCLE_COUNTERS = 0x0E
        LOG_PAGE_CODE_SELFTEST_RESULTS = 0x10
        LOG_PAGE_CODE_SOLID_STATE_MEDIA = 0x11
        LOG_PAGE_CODE_BACKGROUND_SCAN_RESULTS = 0x15
        LOG_PAGE_CODE_INFORMATIONAL_EXCEPTIONS = 0x2F


        class _Union_4(ctypes.Union):
            pass


        class _Struct_1(ctypes.Structure):
            pass


        _Struct_1._fields_ = [
            # Byte 2, bit 0 - 1
            ('FormatAndLinking', UCHAR, 2),
            # Byte 2, bit 2 - 3
            ('TMC', UCHAR, 2),
            # Byte 2, bit 4
            ('ETC', UCHAR, 1),
            # Byte 2, bit 5
            ('TSD', UCHAR, 1),
            # Byte 2, bit 6
            ('Obsolete', UCHAR, 1),
            # Byte 2, bit 7
            ('DU', UCHAR, 1),
        ]
        _Union_4._Struct_1 = _Struct_1

        _Union_4._anonymous_ = (
            '_Struct_1',
        )

        _Union_4._fields_ = [
            # Byte 2
            ('ControlByte', UCHAR),
            ('_Struct_1', _Union_4._Struct_1),
        ]
        _LOG_PARAMETER_HEADER._Union_4 = _Union_4

        _LOG_PARAMETER_HEADER._anonymous_ = (
            '_Union_4',
        )

        _LOG_PARAMETER_HEADER._fields_ = [
            # Bytes 0 - 1
            ('ParameterCode', UCHAR * 2),
            ('_Union_4', _LOG_PARAMETER_HEADER._Union_4),
            # Byte 3
            ('ParameterLength', UCHAR),
        ]


        class _Union_5(ctypes.Union):
            pass


        class _THRESHOLD_RESOURCE_COUNT(ctypes.Structure):
            pass


        _THRESHOLD_RESOURCE_COUNT._fields_ = [
            # Bytes 4 - 7
            ('ResourceCount', UCHAR * 4),
            # Byte 5, bit 0 - 1
            ('Scope', UCHAR, 2),
            # Byte 5, bit 2 - 7
            ('Reserved1', UCHAR, 6),
            # Byte 6
            ('Reserved2', UCHAR * 3),
        ]
        THRESHOLD_RESOURCE_COUNT = _THRESHOLD_RESOURCE_COUNT
        _Union_5.THRESHOLD_RESOURCE_COUNT = THRESHOLD_RESOURCE_COUNT


        class _TEMPERATURE(ctypes.Structure):
            pass


        _TEMPERATURE._fields_ = [
            # Byte 4
            ('Reserved', UCHAR),
            # Byte 5
            ('Temperature', UCHAR),
        ]
        TEMPERATURE = _TEMPERATURE
        _Union_5.TEMPERATURE = TEMPERATURE


        class _DATE_OF_MANUFACTURE(ctypes.Structure):
            pass


        _DATE_OF_MANUFACTURE._fields_ = [
            # Bytes 4 - 7
            ('Year', UCHAR * 4),
            # Bytes 8 - 9
            ('Week', UCHAR * 2),
        ]
        DATE_OF_MANUFACTURE = _DATE_OF_MANUFACTURE
        _Union_5.DATE_OF_MANUFACTURE = DATE_OF_MANUFACTURE


        class _SELF_TEST_RESULTS(ctypes.Structure):
            pass


        _SELF_TEST_RESULTS._fields_ = [
            # Byte 4, bit 0 - 3
            ('SelfTestResults', UCHAR, 4),
            # Byte 4, bit 4
            ('Reserved1', UCHAR, 1),
            # Byte 4, bit 5 - 7
            ('SelfTestCode', UCHAR, 3),
            # Byte 5
            ('SelfTestNumber', UCHAR),
            # Bytes 6 - 7
            ('PowerOnHours', UCHAR * 2),
            # Bytes 8 - 15
            ('AddressOfFirstFailure', UCHAR * 8),
            # Byte 16, bit 0 - 3
            ('SenseKey', UCHAR, 4),
            # Byte 16, bit 4 - 7
            ('Reserved2', UCHAR, 4),
            # Byte 17
            ('AdditionalSenseCode', UCHAR),
            # Byte 18
            ('AdditionalSenseCodeQualifier', UCHAR),
            # Byte 19
            ('VendorSpecific', UCHAR),
        ]
        SELF_TEST_RESULTS = _SELF_TEST_RESULTS
        _Union_5.SELF_TEST_RESULTS = SELF_TEST_RESULTS


        class _SOLID_STATE_MEDIA(ctypes.Structure):
            pass


        _SOLID_STATE_MEDIA._fields_ = [
            # Bytes 4 - 6
            ('Reserved', UCHAR * 3),
            # Byte 7
            ('PercentageUsed', UCHAR),
        ]
        SOLID_STATE_MEDIA = _SOLID_STATE_MEDIA
        _Union_5.SOLID_STATE_MEDIA = SOLID_STATE_MEDIA


        class _BACKGROUND_SCAN_STATUS(ctypes.Structure):
            pass


        _BACKGROUND_SCAN_STATUS._fields_ = [
            # Bytes 4 - 7
            ('PowerOnMinutes', UCHAR * 4),
            # Byte 8
            ('Reserved', UCHAR),
            # Byte 9
            ('ScanStatus', UCHAR),
            # Bytes 10 - 11
            ('ScansPerformed', UCHAR * 2),
            # Bytes 12 - 13
            ('ScanProgress', UCHAR * 2),
            # Bytes 14 - 15
            ('MediumScansPerformed', UCHAR * 2),
        ]
        BACKGROUND_SCAN_STATUS = _BACKGROUND_SCAN_STATUS
        _Union_5.BACKGROUND_SCAN_STATUS = BACKGROUND_SCAN_STATUS


        class _INFORMATIONAL_EXCEPTIONS(ctypes.Structure):
            pass


        _INFORMATIONAL_EXCEPTIONS._fields_ = [
            # Byte 4
            ('ASC', UCHAR),
            # Byte 5
            ('ASCQ', UCHAR),
            # Byte 6
            ('MostRecentTemperature', UCHAR),
            # Bytes 7 - N
            ('VendorSpecific', UCHAR * ANYSIZE_ARRAY),
        ]
        INFORMATIONAL_EXCEPTIONS = _INFORMATIONAL_EXCEPTIONS
        _Union_5.INFORMATIONAL_EXCEPTIONS = INFORMATIONAL_EXCEPTIONS


        _TEMP__Union_5 = [
        ]
        if not defined(__midl):
            _TEMP__Union_5 += [
                # Bytes 4 - N
                ('AsByte', UCHAR * 0),
            ]
        # END IF
        _TEMP__Union_5 += [
            ('THRESHOLD_RESOURCE_COUNT', _Union_5.THRESHOLD_RESOURCE_COUNT),
            ('TEMPERATURE', _Union_5.TEMPERATURE),
            ('DATE_OF_MANUFACTURE', _Union_5.DATE_OF_MANUFACTURE),
            ('SELF_TEST_RESULTS', _Union_5.SELF_TEST_RESULTS),
            ('SOLID_STATE_MEDIA', _Union_5.SOLID_STATE_MEDIA),
            ('BACKGROUND_SCAN_STATUS', _Union_5.BACKGROUND_SCAN_STATUS),
            ('INFORMATIONAL_EXCEPTIONS', _Union_5.INFORMATIONAL_EXCEPTIONS),
        ]
        _Union_5._fields_ = _TEMP__Union_5
        _LOG_PARAMETER._Union_5 = _Union_5

        _LOG_PARAMETER._anonymous_ = (
            '_Union_5',
        )

        _LOG_PARAMETER._fields_ = [
            # Bytes 0 - 3
            ('Header', LOG_PARAMETER_HEADER),
            ('_Union_5', _LOG_PARAMETER._Union_5),
        ]

        _TEMP__LOG_PAGE = [
            # Byte 0, bit 0 - 5
            ('PageCode', UCHAR, 6),
            # Byte 0, bit 6
            ('SPF', UCHAR, 1),
            # Byte 0, bit 7
            ('DS', UCHAR, 1),
            # Byte 1
            ('SubPageCode', UCHAR),
            # Bytes 2 - 3
            ('PageLength', UCHAR * 2),
        ]
        if not defined(__midl):
            _TEMP__LOG_PAGE += [
                ('Parameters', LOG_PARAMETER * 0),
            ]
        # END IF
        _LOG_PAGE._fields_ = _TEMP__LOG_PAGE


        # Logical Block Provisioning resource count parameter codes.
        LOG_PAGE_LBP_PARAMETER_CODE_AVAILABLE = 0x1
        LOG_PAGE_LBP_PARAMETER_CODE_USED = 0x2


        # Logical Block Provisioning resource count scope codes.
        LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_REPORTED = 0x0
        LOG_PAGE_LBP_RESOURCE_SCOPE_DEDICATED_TO_LUN = 0x1
        LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_DEDICATED_TO_LUN = 0x2


        # Logical Block Provisioning threshold resource count log page
        # parameter.
        _LOG_PARAMETER_THRESHOLD_RESOURCE_COUNT._fields_ = [
            ('Header', LOG_PARAMETER_HEADER),
            ('ResourceCount', UCHAR * 4),
            ('Scope', UCHAR, 2),
            ('Reserved0', UCHAR, 6),
            ('Reserved1', UCHAR * 3),
        ]


        # Logical Block Provisioning log page.
        _TEMP__LOG_PAGE_LOGICAL_BLOCK_PROVISIONING = [
            # 0x0C
            ('PageCode', UCHAR, 6),
            # 0
            ('SPF', UCHAR, 1),
            # 1
            ('DS', UCHAR, 1),
            # 0x00
            ('SubPageCode', UCHAR),
            ('PageLength', UCHAR * 2),
        ]
        if not defined(__midl):
            _TEMP__LOG_PAGE_LOGICAL_BLOCK_PROVISIONING += [
                ('Parameters', LOG_PARAMETER_HEADER * 0),
            ]
        # END IF
        _LOG_PAGE_LOGICAL_BLOCK_PROVISIONING._fields_ = _TEMP__LOG_PAGE_LOGICAL_BLOCK_PROVISIONING


        # Optional VERSION DESCRIPTOR fields provide the opportunity for SCSI
        # targets to
        # claim conformance with a number of standards. The INQUIRY response
        # can contain
        # any number of version descriptors between one and eight. Below
        # values are
        VER_DESCRIPTOR_SPC4_NOVERSION = 0x0460
        VER_DESCRIPTOR_SPC4_T10_1731D_R16 = 0x0461
        VER_DESCRIPTOR_SPC4_T10_1731D_R18 = 0x0462
        VER_DESCRIPTOR_SPC4_T10_1731D_R23 = 0x0463
        VER_DESCRIPTOR_SBC3 = 0x04C0
        VER_DESCRIPTOR_1667_NOVERSION = 0xFFC0
        VER_DESCRIPTOR_1667_2006 = 0xFFC1
        VER_DESCRIPTOR_1667_2009 = 0xFFC2


        # Persistent Reservation Definitions.
        # PERSISTENT_RESERVE_* definitions
        RESERVATION_ACTION_READ_KEYS = 0x00
        RESERVATION_ACTION_READ_RESERVATIONS = 0x01
        RESERVATION_ACTION_REGISTER = 0x00
        RESERVATION_ACTION_RESERVE = 0x01
        RESERVATION_ACTION_RELEASE = 0x02
        RESERVATION_ACTION_CLEAR = 0x03
        RESERVATION_ACTION_PREEMPT = 0x04
        RESERVATION_ACTION_PREEMPT_ABORT = 0x05
        RESERVATION_ACTION_REGISTER_IGNORE_EXISTING = 0x06
        RESERVATION_SCOPE_LU = 0x00
        RESERVATION_SCOPE_ELEMENT = 0x02
        RESERVATION_TYPE_WRITE_EXCLUSIVE = 0x01
        RESERVATION_TYPE_EXCLUSIVE = 0x03
        RESERVATION_TYPE_WRITE_EXCLUSIVE_REGISTRANTS = 0x05
        RESERVATION_TYPE_EXCLUSIVE_REGISTRANTS = 0x06


        # Structures for reserve in command.
        _TEMP_PRI_REGISTRATION_LIST = [
            ('Generation', UCHAR * 4),
            ('AdditionalLength', UCHAR * 4),
        ]
        if not defined(__midl):
            _TEMP_PRI_REGISTRATION_LIST += [
                ('ReservationKeyList', (UCHAR * 0)(UCHAR * 8)),
            ]
        # END IF
        PRI_REGISTRATION_LIST._fields_ = _TEMP_PRI_REGISTRATION_LIST

        PRI_RESERVATION_DESCRIPTOR._fields_ = [
            ('ReservationKey', UCHAR * 8),
            ('ScopeSpecificAddress', UCHAR * 4),
            ('Reserved', UCHAR),
            ('Type', UCHAR, 4),
            ('Scope', UCHAR, 4),
            ('Obsolete', UCHAR * 2),
        ]

        _TEMP_PRI_RESERVATION_LIST = [
            ('Generation', UCHAR * 4),
            ('AdditionalLength', UCHAR * 4),
        ]
        if not defined(__midl):
            _TEMP_PRI_RESERVATION_LIST += [
                ('Reservations', PRI_RESERVATION_DESCRIPTOR * 0),
            ]
        # END IF
        PRI_RESERVATION_LIST._fields_ = _TEMP_PRI_RESERVATION_LIST


        # Structures for reserve out command.
        PRO_PARAMETER_LIST._fields_ = [
            ('ReservationKey', UCHAR * 8),
            ('ServiceActionReservationKey', UCHAR * 8),
            ('ScopeSpecificAddress', UCHAR * 4),
            ('ActivatePersistThroughPowerLoss', UCHAR, 1),
            ('Reserved1', UCHAR, 7),
            ('Reserved2', UCHAR),
            ('Obsolete', UCHAR * 2),
        ]


        # Structure for report timestamp command.
        RT_PARAMETER_DATA._fields_ = [
            # Byte 0 - 1
            ('ParameterDataLength', UCHAR * 2),
            # Byte 2, bit 0 - 2
            ('Origin', UCHAR, 3),
            # Byte 2, bit 3 - 7
            ('Reserved1', UCHAR, 5),
            # Byte 3
            ('Reserved2', UCHAR),
            # Byte 4 - 9
            ('Timestamp', UCHAR * 6),
            # Byte 10 - 11
            ('Reserved3', UCHAR * 2),
        ]


        # Structure for set timestamp command.
        ST_PARAMETER_DATA._fields_ = [
            # Byte 0 - 3
            ('Reserved1', UCHAR * 4),
            # Byte 4 - 9
            ('Timestamp', UCHAR * 6),
            # Byte 10 - 11
            ('Reserved2', UCHAR * 2),
        ]
        if NTDDI_VERSION >= NTDDI_WIN8:
            BLOCK_DEVICE_TOKEN_SIZE = 512


            # Stuctures for Token Operation and Receive Token Information
            # commands
            BLOCK_DEVICE_RANGE_DESCRIPTOR._fields_ = [
                ('LogicalBlockAddress', UCHAR * 8),
                ('TransferLength', UCHAR * 4),
                ('Reserved', UCHAR * 4),
            ]

            _TEMP_POPULATE_TOKEN_HEADER = [
                ('PopulateTokenDataLength', UCHAR * 2),
                ('Immediate', UCHAR, 1),
                ('Reserved1', UCHAR, 7),
                ('Reserved2', UCHAR),
                ('InactivityTimeout', UCHAR * 4),
                ('Reserved3', UCHAR * 6),
                ('BlockDeviceRangeDescriptorListLength', UCHAR * 2),
            ]
            if not defined(__midl):
                _TEMP_POPULATE_TOKEN_HEADER += [
                    ('BlockDeviceRangeDescriptor', UCHAR * ANYSIZE_ARRAY),
                ]
            # END IF
            POPULATE_TOKEN_HEADER._fields_ = _TEMP_POPULATE_TOKEN_HEADER

            _TEMP_WRITE_USING_TOKEN_HEADER = [
                ('WriteUsingTokenDataLength', UCHAR * 2),
                ('Immediate', UCHAR, 1),
                ('Reserved1', UCHAR, 7),
                ('Reserved2', UCHAR * 5),
                ('BlockOffsetIntoToken', UCHAR * 8),
                ('Token', UCHAR * BLOCK_DEVICE_TOKEN_SIZE),
                ('Reserved3', UCHAR * 6),
                ('BlockDeviceRangeDescriptorListLength', UCHAR * 2),
            ]
            if not defined(__midl):
                _TEMP_WRITE_USING_TOKEN_HEADER += [
                    ('BlockDeviceRangeDescriptor', UCHAR * ANYSIZE_ARRAY),
                ]
            # END IF
            WRITE_USING_TOKEN_HEADER._fields_ = _TEMP_WRITE_USING_TOKEN_HEADER

            _TEMP_RECEIVE_TOKEN_INFORMATION_HEADER = [
                ('AvailableData', UCHAR * 4),
                ('ResponseToServiceAction', UCHAR, 5),
                ('Reserved1', UCHAR, 3),
                ('OperationStatus', UCHAR, 7),
                ('Reserved2', UCHAR, 1),
                ('OperationCounter', UCHAR * 2),
                ('EstimatedStatusUpdateDelay', UCHAR * 4),
                ('CompletionStatus', UCHAR),
                ('SenseDataFieldLength', UCHAR),
                ('SenseDataLength', UCHAR),
                ('TransferCountUnits', UCHAR),
                ('TransferCount', UCHAR * 8),
                ('SegmentsProcessed', UCHAR * 2),
                ('Reserved3', UCHAR * 6),
            ]
            if not defined(__midl):
                _TEMP_RECEIVE_TOKEN_INFORMATION_HEADER += [
                    ('SenseData', UCHAR * ANYSIZE_ARRAY),
                ]
            # END IF
            RECEIVE_TOKEN_INFORMATION_HEADER._fields_ = _TEMP_RECEIVE_TOKEN_INFORMATION_HEADER

            _TEMP_RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER = [
                ('TokenDescriptorsLength', UCHAR * 4),
            ]
            if not defined(__midl):
                _TEMP_RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER += [
                    ('TokenDescriptor', UCHAR * ANYSIZE_ARRAY),
                ]
            # END IF
            RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER._fields_ = _TEMP_RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER

            BLOCK_DEVICE_TOKEN_DESCRIPTOR._fields_ = [
                ('TokenIdentifier', UCHAR * 2),
                ('Token', UCHAR * BLOCK_DEVICE_TOKEN_SIZE),
            ]


            class _OPERATION_STATUS(ENUM):
                OPERATION_COMPLETED_WITH_SUCCESS = 0x01
                OPERATION_COMPLETED_WITH_ERROR = 0x02
                OPERATION_COMPLETED_WITH_RESIDUAL_DATA = 0x03
                OPERATION_IN_PROGRESS_IN_FOREGROUND = 0x11
                OPERATION_IN_PROGRESS_IN_BACKGROUND = 0x12
                OPERATION_TERMINATED = 0x60

            OPERATION_STATUS = _OPERATION_STATUS
            POPERATION_STATUS = POINTER(_OPERATION_STATUS)


            class _TRANSFER_COUNT_UNITS(ENUM): # Multiplier to convert a Transfer Count field to bytes
                TRANSFER_COUNT_UNITS_BYTES = 0
                TRANSFER_COUNT_UNITS_KIBIBYTES = 1
                TRANSFER_COUNT_UNITS_MEBIBYTES = 2
                TRANSFER_COUNT_UNITS_GIBIBYTES = 3
                TRANSFER_COUNT_UNITS_TEBIBYTES = 4
                TRANSFER_COUNT_UNITS_PEBIBYTES = 5
                TRANSFER_COUNT_UNITS_EXBIBYTES = 6
                TRANSFER_COUNT_UNITS_NUMBER_BLOCKS = 0xF1

            TRANSFER_COUNT_UNITS = _TRANSFER_COUNT_UNITS
            PTRANSFER_COUNT_UNITS = POINTER(_TRANSFER_COUNT_UNITS)
        # END IF  (NTDDI_VERSION >= NTDDI_WIN8)

        # SANITIZE related definition
        _TEMP__OVERWRITE_PARAMETER_LIST = [
            ('OverWriteCount', UCHAR, 5),
            ('Test', UCHAR, 2),
            ('Invert', UCHAR, 1),
            ('Reserved1', UCHAR),
            ('InitializationPatternLength', UCHAR * 2),
        ]
        if not defined(__midl):
            _TEMP__OVERWRITE_PARAMETER_LIST += [
                ('InitializationPattern', UCHAR * ANYSIZE_ARRAY),
            ]
        # END IF
        _OVERWRITE_PARAMETER_LIST._fields_ = _TEMP__OVERWRITE_PARAMETER_LIST


        # SCSIOP_WRITE_DATA_BUFF related definition
        SCSI_WRITE_BUFFER_MODE_DOWNLOAD_MICROCODE_WITH_OFFSETS_SAVE_DEFER_ACTIVATE = (
            0x0E
        )
        SCSI_WRITE_BUFFER_MODE_ACTIVATE_DEFERRED_MICROCODE = 0x0F
        SCSI_WRITE_BUFFER_MODE_0D_MODE_SPECIFIC_VSE_ACT = 0x01
        SCSI_WRITE_BUFFER_MODE_0D_MODE_SPECIFIC_HR_ACT = 0x02
        SCSI_WRITE_BUFFER_MODE_0D_MODE_SPECIFIC_PO_ACT = 0x04


        # Sense Data Format
        _SENSE_DATA._fields_ = [
            ('ErrorCode', UCHAR, 7),
            ('Valid', UCHAR, 1),
            ('SegmentNumber', UCHAR),
            ('SenseKey', UCHAR, 4),
            ('Reserved', UCHAR, 1),
            ('IncorrectLength', UCHAR, 1),
            ('EndOfMedia', UCHAR, 1),
            ('FileMark', UCHAR, 1),
            ('Information', UCHAR * 4),
            ('AdditionalSenseLength', UCHAR),
            ('CommandSpecificInformation', UCHAR * 4),
            ('AdditionalSenseCode', UCHAR),
            ('AdditionalSenseCodeQualifier', UCHAR),
            ('FieldReplaceableUnitCode', UCHAR),
            ('SenseKeySpecific', UCHAR * 3),
        ]


        # NOTE: Sense Data Descriptor Format is supported only in Windows 8
        # and later
        _SCSI_SENSE_DESCRIPTOR_HEADER._fields_ = [
            ('DescriptorType', UCHAR),
            ('AdditionalLength', UCHAR),
        ]


        # Information Sense Data Descriptor Format
        _SCSI_SENSE_DESCRIPTOR_INFORMATION._fields_ = [
            ('Header', SCSI_SENSE_DESCRIPTOR_HEADER),
            ('Valid', UCHAR, 1),
            ('Reserved1', UCHAR, 7),
            ('Reserved2', UCHAR),
            ('Information', UCHAR * 8),
        ]


        # Block Command Sense Data Descriptor Format
        _SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND._fields_ = [
            ('Header', SCSI_SENSE_DESCRIPTOR_HEADER),
            ('Reserved1', UCHAR),
            ('Reserved2', UCHAR, 5),
            ('IncorrectLength', UCHAR, 1),
            ('Reserved3', UCHAR, 2),
        ]


        # ATA Status Return Descriptor Format
        _SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN._fields_ = [
            ('Header', SCSI_SENSE_DESCRIPTOR_HEADER),
            ('Extend', UCHAR, 1),
            ('Reserved1', UCHAR, 7),
            ('Error', UCHAR),
            ('SectorCount15_8', UCHAR),
            ('SectorCount7_0', UCHAR),
            ('LbaLow15_8', UCHAR),
            ('LbaLow7_0', UCHAR),
            ('LbaMid15_8', UCHAR),
            ('LbaMid7_0', UCHAR),
            ('LbaHigh15_8', UCHAR),
            ('LbaHigh7_0', UCHAR),
            ('Device', UCHAR),
            ('Status', UCHAR),
        ]


        # Fixed Sense Data Format
        FIXED_SENSE_DATA = _SENSE_DATA
        PFIXED_SENSE_DATA = POINTER(_SENSE_DATA)


        # Descriptor Sense Data Format
        _DESCRIPTOR_SENSE_DATA._fields_ = [
            ('ErrorCode', UCHAR, 7),
            ('Reserved1', UCHAR, 1),
            ('SenseKey', UCHAR, 4),
            ('Reserved2', UCHAR, 4),
            ('AdditionalSenseCode', UCHAR),
            ('AdditionalSenseCodeQualifier', UCHAR),
            ('Reserved3', UCHAR * 3),
            ('AdditionalSenseLength', UCHAR),
            ('DescriptorBuffer', UCHAR * ANYSIZE_ARRAY),
        ]

        _SENSE_DATA_EX._fields_ = [
            # Sense data in fixed format
            ('FixedData', FIXED_SENSE_DATA),
            # Sense data in descriptor format
            ('DescriptorData', DESCRIPTOR_SENSE_DATA),
        ]


        # Default request sense buffer size
        SENSE_BUFFER_SIZE = ctypes.sizeof(SENSE_DATA)
        SENSE_BUFFER_SIZE_EX = ctypes.sizeof(SENSE_DATA_EX)
        # Maximum request sense buffer size
        MAX_SENSE_BUFFER_SIZE = 255
        # Maximum number of additional sense bytes.
        MAX_ADDITIONAL_SENSE_BYTES = MAX_SENSE_BUFFER_SIZE - SENSE_BUFFER_SIZE
        MAX_ADDITIONAL_SENSE_BYTES_EX = (
            MAX_SENSE_BUFFER_SIZE - SENSE_BUFFER_SIZE_EX
        )
        # Sense Data Error Codes
        SCSI_SENSE_ERRORCODE_FIXED_CURRENT = 0x70
        SCSI_SENSE_ERRORCODE_FIXED_DEFERRED = 0x71
        SCSI_SENSE_ERRORCODE_DESCRIPTOR_CURRENT = 0x72
        SCSI_SENSE_ERRORCODE_DESCRIPTOR_DEFERRED = 0x73
        # Sense Data Descriptor Types
        SCSI_SENSE_DESCRIPTOR_TYPE_INFORMATION = 0x00
        SCSI_SENSE_DESCRIPTOR_TYPE_COMMAND_SPECIFIC = 0x01
        SCSI_SENSE_DESCRIPTOR_TYPE_SENSE_KEY_SPECIFIC = 0x02
        SCSI_SENSE_DESCRIPTOR_TYPE_FIELD_REPLACEABLE_UNIT = 0x03
        SCSI_SENSE_DESCRIPTOR_TYPE_STREAM_COMMAND = 0x04
        SCSI_SENSE_DESCRIPTOR_TYPE_BLOCK_COMMAND = 0x05
        SCSI_SENSE_DESCRIPTOR_TYPE_OSD_OBJECT_IDENTIFICATION = 0x06
        SCSI_SENSE_DESCRIPTOR_TYPE_OSD_RESPONSE_INTEGRITY_CHECK = 0x07
        SCSI_SENSE_DESCRIPTOR_TYPE_OSD_ATTRIBUTE_IDENTIFICATION = 0x08
        SCSI_SENSE_DESCRIPTOR_TYPE_ATA_STATUS_RETURN = 0x09
        SCSI_SENSE_DESCRIPTOR_TYPE_PROGRESS_INDICATION = 0x0A
        SCSI_SENSE_DESCRIPTOR_TYPE_USER_DATA_SEGMENT_REFERRAL = 0x0B
        SCSI_SENSE_DESCRIPTOR_TYPE_FORWARDED_SENSE_DATA = 0x0C
        # Sense Keys
        SCSI_SENSE_NO_SENSE = 0x00
        SCSI_SENSE_RECOVERED_ERROR = 0x01
        SCSI_SENSE_NOT_READY = 0x02
        SCSI_SENSE_MEDIUM_ERROR = 0x03
        SCSI_SENSE_HARDWARE_ERROR = 0x04
        SCSI_SENSE_ILLEGAL_REQUEST = 0x05
        SCSI_SENSE_UNIT_ATTENTION = 0x06
        SCSI_SENSE_DATA_PROTECT = 0x07
        SCSI_SENSE_BLANK_CHECK = 0x08
        SCSI_SENSE_UNIQUE = 0x09
        SCSI_SENSE_COPY_ABORTED = 0x0A
        SCSI_SENSE_ABORTED_COMMAND = 0x0B
        SCSI_SENSE_EQUAL = 0x0C
        SCSI_SENSE_VOL_OVERFLOW = 0x0D
        SCSI_SENSE_MISCOMPARE = 0x0E
        SCSI_SENSE_RESERVED = 0x0F
        # Additional tape bit
        SCSI_ILLEGAL_LENGTH = 0x20
        SCSI_EOM = 0x40
        SCSI_FILE_MARK = 0x80
        # Additional Sense codes
        SCSI_ADSENSE_NO_SENSE = 0x00
        SCSI_ADSENSE_NO_SEEK_COMPLETE = 0x02
        SCSI_ADSENSE_WRITE = 0x03
        SCSI_ADSENSE_LUN_NOT_READY = 0x04
        SCSI_ADSENSE_LUN_COMMUNICATION = 0x08
        SCSI_ADSENSE_SERVO_ERROR = 0x09
        SCSI_ADSENSE_WARNING = 0x0B
        SCSI_ADSENSE_WRITE_ERROR = 0x0C
        SCSI_ADSENSE_COPY_TARGET_DEVICE_ERROR = 0x0D
        SCSI_ADSENSE_UNRECOVERED_ERROR = 0x11
        SCSI_ADSENSE_TRACK_ERROR = 0x14
        SCSI_ADSENSE_SEEK_ERROR = 0x15
        SCSI_ADSENSE_REC_DATA_NOECC = 0x17
        SCSI_ADSENSE_REC_DATA_ECC = 0x18
        SCSI_ADSENSE_DEFECT_LIST_ERROR = 0x19
        SCSI_ADSENSE_PARAMETER_LIST_LENGTH = 0x1A
        SCSI_ADSENSE_MISCOMPARE_DURING_VERIFY_OPERATION = 0x1D
        SCSI_ADSENSE_ILLEGAL_COMMAND = 0x20
        SCSI_ADSENSE_ACCESS_DENIED = 0x20
        SCSI_ADSENSE_ILLEGAL_BLOCK = 0x21
        SCSI_ADSENSE_INVALID_TOKEN = 0x23
        SCSI_ADSENSE_INVALID_CDB = 0x24
        SCSI_ADSENSE_INVALID_LUN = 0x25
        SCSI_ADSENSE_INVALID_FIELD_PARAMETER_LIST = 0x26
        SCSI_ADSENSE_WRITE_PROTECT = 0x27
        SCSI_ADSENSE_MEDIUM_CHANGED = 0x28
        SCSI_ADSENSE_BUS_RESET = 0x29
        SCSI_ADSENSE_PARAMETERS_CHANGED = 0x2A
        SCSI_ADSENSE_INSUFFICIENT_TIME_FOR_OPERATION = 0x2E
        SCSI_ADSENSE_INVALID_MEDIA = 0x30
        SCSI_ADSENSE_DEFECT_LIST = 0x32
        SCSI_ADSENSE_LB_PROVISIONING = 0x38
        SCSI_ADSENSE_NO_MEDIA_IN_DEVICE = 0x3A
        SCSI_ADSENSE_POSITION_ERROR = 0x3B
        SCSI_ADSENSE_LOGICAL_UNIT_ERROR = 0x3E
        SCSI_ADSENSE_OPERATING_CONDITIONS_CHANGED = 0x3F
        SCSI_ADSENSE_DATA_PATH_FAILURE = 0x41
        SCSI_ADSENSE_POWER_ON_SELF_TEST_FAILURE = 0x42
        SCSI_ADSENSE_INTERNAL_TARGET_FAILURE = 0x44
        SCSI_ADSENSE_DATA_TRANSFER_ERROR = 0x4B
        SCSI_ADSENSE_LUN_FAILED_SELF_CONFIGURATION = 0x4C
        SCSI_ADSENSE_RESOURCE_FAILURE = 0x55
        SCSI_ADSENSE_OPERATOR_REQUEST = 0x5A        # see below
        SCSI_ADSENSE_FAILURE_PREDICTION_THRESHOLD_EXCEEDED = 0x5D
        SCSI_ADSENSE_ILLEGAL_MODE_FOR_THIS_TRACK = 0x64
        SCSI_ADSENSE_COPY_PROTECTION_FAILURE = 0x6F
        SCSI_ADSENSE_POWER_CALIBRATION_ERROR = 0x73
        SCSI_ADSENSE_VENDOR_UNIQUE = 0x80        # and higher
        SCSI_ADSENSE_MUSIC_AREA = 0xA0
        SCSI_ADSENSE_DATA_AREA = 0xA1
        SCSI_ADSENSE_VOLUME_OVERFLOW = 0xA7
        # for legacy apps:
        SCSI_ADWRITE_PROTECT = SCSI_ADSENSE_WRITE_PROTECT
        SCSI_FAILURE_PREDICTION_THRESHOLD_EXCEEDED = (
            SCSI_ADSENSE_FAILURE_PREDICTION_THRESHOLD_EXCEEDED
        )
        # SCSI_ADSENSE_NO_SENSE (0x00) qualifiers
        SCSI_SENSEQ_OPERATION_IS_IN_PROGRESS = 0x16
        # SCSI_ADSENSE_WRITE (0x03) qualifiers
        SCSI_SENSEQ_PERIPHERAL_DEVICE_WRITE_FAULT = 0x00
        SCSI_SENSEQ_NO_WRITE_CURRENT = 0x01
        SCSI_SENSEQ_EXCESSIVE_WRITE_ERRORS = 0x02
        # SCSI_ADSENSE_LUN_NOT_READY (0x04) qualifiers
        SCSI_SENSEQ_CAUSE_NOT_REPORTABLE = 0x00
        SCSI_SENSEQ_BECOMING_READY = 0x01
        SCSI_SENSEQ_INIT_COMMAND_REQUIRED = 0x02
        SCSI_SENSEQ_MANUAL_INTERVENTION_REQUIRED = 0x03
        SCSI_SENSEQ_FORMAT_IN_PROGRESS = 0x04
        SCSI_SENSEQ_REBUILD_IN_PROGRESS = 0x05
        SCSI_SENSEQ_RECALCULATION_IN_PROGRESS = 0x06
        SCSI_SENSEQ_OPERATION_IN_PROGRESS = 0x07
        SCSI_SENSEQ_LONG_WRITE_IN_PROGRESS = 0x08
        SCSI_SENSEQ_SPACE_ALLOC_IN_PROGRESS = 0x14
        # SCSI_ADSENSE_LUN_COMMUNICATION (0x08) qualifiers
        SCSI_SENSEQ_COMM_FAILURE = 0x00
        SCSI_SENSEQ_COMM_TIMEOUT = 0x01
        SCSI_SENSEQ_COMM_PARITY_ERROR = 0x02
        SCSI_SESNEQ_COMM_CRC_ERROR = 0x03
        SCSI_SENSEQ_UNREACHABLE_TARGET = 0x04
        # SCSI_ADSENSE_SERVO_ERROR (0x09) qualifiers
        SCSI_SENSEQ_TRACK_FOLLOWING_ERROR = 0x00
        SCSI_SENSEQ_TRACKING_SERVO_FAILURE = 0x01
        SCSI_SENSEQ_FOCUS_SERVO_FAILURE = 0x02
        SCSI_SENSEQ_SPINDLE_SERVO_FAILURE = 0x03
        SCSI_SENSEQ_HEAD_SELECT_FAULT = 0x04
        # SCSI_ADSENSE_WARNING (0x0B) qualifiers
        SCSI_SENSEQ_POWER_LOSS_EXPECTED = 0x08
        # SCSI_ADSENSE_WRITE_ERROR (0x0C) qualifiers
        SCSI_SENSEQ_LOSS_OF_STREAMING = 0x09
        SCSI_SENSEQ_PADDING_BLOCKS_ADDED = 0x0A
        # SCSI_ADSENSE_COPY_TARGET_DEVICE_ERROR (0x0D) qualifiers
        SCSI_SENSEQ_NOT_REACHABLE = 0x02
        SCSI_SENSEQ_DATA_UNDERRUN = 0x04
        # SCSI_ADSENSE_UNRECOVERED_ERROR (0x11) qualifiers
        SCSI_SENSEQ_UNRECOVERED_READ_ERROR = 0x00
        # SCSI_ADSENSE_SEEK_ERROR (0x15) qualifiers
        SCSI_SENSEQ_RANDOM_POSITIONING_ERROR = 0x00
        SCSI_SENSEQ_MECHANICAL_POSITIONING_ERROR = 0x01
        SCSI_SENSEQ_POSITIONING_ERROR_DETECTED_BY_READ_OF_MEDIUM = 0x02
        # SCSI_ADSENSE_DEFECT_LIST_ERROR (0x19) qualifiers
        SCSI_SENSEQ_DEFECT_LIST_ERROR = 0x00
        SCSI_SENSEQ_DEFECT_LIST_NOT_AVAILABLE = 0x01
        SCSI_SENSEQ_DEFECT_LIST_ERROR_IN_PRIMARY_LIST = 0x02
        SCSI_SENSEQ_DEFECT_LIST_ERROR_IN_GROWN_LIST = 0x03
        # SCSI_ADSENSE_NO_SENSE (0x00) qualifiers
        SCSI_SENSEQ_FILEMARK_DETECTED = 0x01
        SCSI_SENSEQ_END_OF_MEDIA_DETECTED = 0x02
        SCSI_SENSEQ_SETMARK_DETECTED = 0x03
        SCSI_SENSEQ_BEGINNING_OF_MEDIA_DETECTED = 0x04
        # SCSI_ADSENSE_ACCESS_DENIED (0x20) qualifiers
        SCSI_SENSEQ_NO_ACCESS_RIGHTS = 0x02
        # SCSI_ADSENSE_ILLEGAL_BLOCK (0x21) qualifiers
        SCSI_SENSEQ_ILLEGAL_ELEMENT_ADDR = 0x01
        # SCSI_ADSENSE_INVALID_FIELD_PARAMETER_LIST (0x26) qualifiers
        SCSI_SENSEQ_INVALID_RELEASE_OF_PERSISTENT_RESERVATION = 0x04
        SCSI_SENSEQ_TOO_MANY_SEGMENT_DESCRIPTORS = 0x08
        # SCSI_ADSENSE_WRITE_PROTECT (0x27) qualifiers
        SCSI_SENSEQ_SPACE_ALLOC_FAILED_WRITE_PROTECT = 0x07
        # SCSI_ADSENSE_PARAMETERS_CHANGED (0x2A) qualifiers
        SCSI_SENSEQ_CAPACITY_DATA_CHANGED = 0x09
        # SCSI_ADSENSE_POSITION_ERROR (0x3b) qualifiers
        SCSI_SENSEQ_DESTINATION_FULL = 0x0D
        SCSI_SENSEQ_SOURCE_EMPTY = 0x0E
        # SCSI_ADSENSE_INVALID_MEDIA (0x30) qualifiers
        SCSI_SENSEQ_INCOMPATIBLE_MEDIA_INSTALLED = 0x00
        SCSI_SENSEQ_UNKNOWN_FORMAT = 0x01
        SCSI_SENSEQ_INCOMPATIBLE_FORMAT = 0x02
        SCSI_SENSEQ_CLEANING_CARTRIDGE_INSTALLED = 0x03
        # SCSI_ADSENSE_DEFECT_LIST (0x32) qualifiers
        SCSI_SENSEQ_NO_DEFECT_SPARE_LOCATION_AVAILABLE = 0x00
        SCSI_SENSEQ_DEFECT_LIST_UPDATE_FAILURE = 0x01
        # SCSI_ADSENSE_LB_PROVISIONING (0x38) qualifiers
        SCSI_SENSEQ_SOFT_THRESHOLD_REACHED = 0x07
        # SCSI_ADSENSE_LOGICAL_UNIT_ERROR (0x3e) qualifiers
        SCSI_SENSEQ_LOGICAL_UNIT_HAS_NOT_SELF_CONFIGURED_YET = 0x00
        SCSI_SENSEQ_LOGICAL_UNIT_FAILURE = 0x01
        SCSI_SENSEQ_TIMEOUT_ON_LOGICAL_UNIT = 0x02
        SCSI_SENSEQ_LOGICAL_UNIT_FAILED_SELF_TEST = 0x03
        SCSI_SENSEQ_LOGICAL_UNIT_FAILED_TO_UPDATE_SELF_TEST_LOG = 0x04
        # SCSI_ADSENSE_OPERATING_CONDITIONS_CHANGED (0x3f) qualifiers
        SCSI_SENSEQ_TARGET_OPERATING_CONDITIONS_CHANGED = 0x00
        SCSI_SENSEQ_MICROCODE_CHANGED = 0x01
        SCSI_SENSEQ_OPERATING_DEFINITION_CHANGED = 0x02
        SCSI_SENSEQ_INQUIRY_DATA_CHANGED = 0x03
        SCSI_SENSEQ_COMPONENT_DEVICE_ATTACHED = 0x04
        SCSI_SENSEQ_DEVICE_IDENTIFIER_CHANGED = 0x05
        SCSI_SENSEQ_REDUNDANCY_GROUP_MODIFIED = 0x06
        SCSI_SENSEQ_REDUNDANCY_GROUP_DELETED = 0x07
        SCSI_SENSEQ_SPARE_MODIFIED = 0x08
        SCSI_SENSEQ_SPARE_DELETED = 0x09
        SCSI_SENSEQ_VOLUME_SET_MODIFIED = 0x0A
        SCSI_SENSEQ_VOLUME_SET_DELETED = 0x0B
        SCSI_SENSEQ_VOLUME_SET_DEASSIGNED = 0x0C
        SCSI_SENSEQ_VOLUME_SET_REASSIGNED = 0x0D
        SCSI_SENSEQ_REPORTED_LUNS_DATA_CHANGED = 0x0E
        SCSI_SENSEQ_ECHO_BUFFER_OVERWRITTEN = 0x0F
        SCSI_SENSEQ_MEDIUM_LOADABLE = 0x10
        SCSI_SENSEQ_MEDIUM_AUXILIARY_MEMORY_ACCESSIBLE = 0x11
        # SCSI_ADSENSE_INTERNAL_TARGET_FAILURE (0x44) qualifiers
        SCSI_SENSEQ_INTERNAL_TARGET_FAILURE = 0x00
        SCSI_SENSEQ_PRESISTENT_RESERVATION_INFORMATION_LOST = 0x01
        SCSI_SENSEQ_ATA_DEVICE_FAILED_SET_FEATURES = 0x71
        # SCSI_ADSENSE_DATA_TRANSFER_ERROR (0x4b) qualifiers
        SCSI_SENSEQ_INITIATOR_RESPONSE_TIMEOUT = 0x06
        # SCSI_ADSENSE_RESOURCE_FAILURE (0x55) qualifiers
        SCSI_SENSEQ_SYSTEM_RESOURCE_FAILURE = 0x00
        SCSI_SENSEQ_SYSTEM_BUFFER_FULL = 0x01
        SCSI_SENSEQ_INSUFFICIENT_RESERVATION_RESOURCES = 0x02
        SCSI_SENSEQ_INSUFFICIENT_RESOURCES = 0x03
        # SCSI_ADSENSE_OPERATOR_REQUEST (0x5a) qualifiers
        SCSI_SENSEQ_STATE_CHANGE_INPUT = 0x00        # generic request
        SCSI_SENSEQ_MEDIUM_REMOVAL = 0x01
        SCSI_SENSEQ_WRITE_PROTECT_ENABLE = 0x02
        SCSI_SENSEQ_WRITE_PROTECT_DISABLE = 0x03
        # SCSI_ADSENSE_FAILURE_PREDICTION_THRESHOLD_EXCEEDED (0x5d) qualifiers
        SCSI_SENSEQ_FAILURE_PREDICTION_THRESHOLD_EXCEEDED = 0x00
        SCSI_SENSEQ_MEDIA_FAILURE_PREDICTION_THRESHOLD_EXCEEDED = 0x01
        SCSI_SENSEQ_LUN_FAILURE_PREDICTION_THRESHOLD_EXCEEDED = 0x02
        SCSI_SENSEQ_SPARE_AREA_EXHAUSTION_PREDICTION_THRESHOLD_EXCEEDED = 0x03
        SCSI_SENSEQ_GENERAL_HARD_DRIVE_FAILURE = 0x10
        SCSI_SENSEQ_DRIVE_ERROR_RATE_TOO_HIGH = 0x11
        SCSI_SENSEQ_DATA_ERROR_RATE_TOO_HIGH = 0x12
        SCSI_SENSEQ_SEEK_ERROR_RATE_TOO_HIGH = 0x13
        SCSI_SENSEQ_TOO_MANY_BLOCK_REASSIGNS = 0x14
        SCSI_SENSEQ_ACCESS_TIMES_TOO_HIGH = 0x15
        SCSI_SENSEQ_START_UNIT_TIMES_TOO_HIGH = 0x16
        SCSI_SENSEQ_CHANNEL_PARAMETRICS = 0x17
        SCSI_SENSEQ_CONTROLLER_DETECTED = 0x18
        SCSI_SENSEQ_THROUGHPUT_PERFORMANCE = 0x19
        SCSI_SENSEQ_SEEK_TIME_PERFORMANCE = 0x1A
        SCSI_SENSEQ_SPIN_UP_RETRY_COUNT = 0x1B
        SCSI_SENSEQ_DRIVE_CALIBRATION_RETRY_COUNT = 0x1C
        SCSI_SENSEQ_DATA_CHANNEL_DATA_ERROR_RATE_TOO_HIGH = 0x32
        SCSI_SENSEQ_SERVO_DATA_ERROR_RATE_TOO_HIGH = 0x42
        SCSI_SENSEQ_SERVER_SEEK_ERROR_RATE_TOO_HIGH = 0x43
        SCSI_SENSEQ_FAILURE_PREDICTION_THRESHOLD_EXCEEDED_FALSE = 0xFF
        # SCSI_ADSENSE_COPY_PROTECTION_FAILURE (0x6f) qualifiers
        SCSI_SENSEQ_AUTHENTICATION_FAILURE = 0x00
        SCSI_SENSEQ_KEY_NOT_PRESENT = 0x01
        SCSI_SENSEQ_KEY_NOT_ESTABLISHED = 0x02
        SCSI_SENSEQ_READ_OF_SCRAMBLED_SECTOR_WITHOUT_AUTHENTICATION = 0x03
        SCSI_SENSEQ_MEDIA_CODE_MISMATCHED_TO_LOGICAL_UNIT = 0x04
        SCSI_SENSEQ_LOGICAL_UNIT_RESET_COUNT_ERROR = 0x05
        # SCSI_ADSENSE_POWER_CALIBRATION_ERROR (0x73) qualifiers
        SCSI_SENSEQ_POWER_CALIBRATION_AREA_ALMOST_FULL = 0x01
        SCSI_SENSEQ_POWER_CALIBRATION_AREA_FULL = 0x02
        SCSI_SENSEQ_POWER_CALIBRATION_AREA_ERROR = 0x03
        SCSI_SENSEQ_PMA_RMA_UPDATE_FAILURE = 0x04
        SCSI_SENSEQ_PMA_RMA_IS_FULL = 0x05
        SCSI_SENSEQ_PMA_RMA_ALMOST_FULL = 0x06
        # end_ntminitape
        # SCSI IO Device Control Codes
        FILE_DEVICE_SCSI = 0x0000001B
        IOCTL_SCSI_EXECUTE_IN = (FILE_DEVICE_SCSI << 16) + 0x0011
        IOCTL_SCSI_EXECUTE_OUT = (FILE_DEVICE_SCSI << 16) + 0x0012
        IOCTL_SCSI_EXECUTE_NONE = (FILE_DEVICE_SCSI << 16) + 0x0013
        # SMART support in atapi
        IOCTL_SCSI_MINIPORT_SMART_VERSION = (FILE_DEVICE_SCSI << 16) + 0x0500
        IOCTL_SCSI_MINIPORT_IDENTIFY = (FILE_DEVICE_SCSI << 16) + 0x0501
        IOCTL_SCSI_MINIPORT_READ_SMART_ATTRIBS = (
            (FILE_DEVICE_SCSI << 16) + 0x0502
        )
        IOCTL_SCSI_MINIPORT_READ_SMART_THRESHOLDS = (
            (FILE_DEVICE_SCSI << 16) + 0x0503
        )
        IOCTL_SCSI_MINIPORT_ENABLE_SMART = (FILE_DEVICE_SCSI << 16) + 0x0504
        IOCTL_SCSI_MINIPORT_DISABLE_SMART = (FILE_DEVICE_SCSI << 16) + 0x0505
        IOCTL_SCSI_MINIPORT_RETURN_STATUS = (FILE_DEVICE_SCSI << 16) + 0x0506
        IOCTL_SCSI_MINIPORT_ENABLE_DISABLE_AUTOSAVE = (
            (FILE_DEVICE_SCSI << 16) + 0x0507
        )
        IOCTL_SCSI_MINIPORT_SAVE_ATTRIBUTE_VALUES = (
            (FILE_DEVICE_SCSI << 16) + 0x0508
        )
        IOCTL_SCSI_MINIPORT_EXECUTE_OFFLINE_DIAGS = (
            (FILE_DEVICE_SCSI << 16) + 0x0509
        )
        IOCTL_SCSI_MINIPORT_ENABLE_DISABLE_AUTO_OFFLINE = (
            (FILE_DEVICE_SCSI << 16) + 0x050A
        )
        IOCTL_SCSI_MINIPORT_READ_SMART_LOG = (FILE_DEVICE_SCSI << 16) + 0x050B
        IOCTL_SCSI_MINIPORT_WRITE_SMART_LOG = (FILE_DEVICE_SCSI << 16) + 0x050C
        # Data set management IOCTL to match DSM notifications. Lba Ranges
        # carried by this IOCTL belong to the same file.
        # This IOCTL carries SRB_IO_CONTROL and DSM_NOTIFICATION_REQUEST_BLOCK
        # as part of input parameters.
        IOCTL_SCSI_MINIPORT_DSM = (FILE_DEVICE_SCSI << 16) + 0x0720
        # Data set management IOCTL sent to miniport driver. Lba Ranges
        # carried by this IOCTL may cross different files or do not belong to
        # file.
        # This IOCTL carries SRB_IO_CONTROL and
        # DEVICE_MANAGE_DATA_SET_ATTRIBUTES as part of input parameters.
        # NOTE that when construct input buffer, padding place may be needed
        # between SRB_IO_CONTROL and DEVICE_MANAGE_DATA_SET_ATTRIBUTES to make
        # sure
        # DEVICE_MANAGE_DATA_SET_ATTRIBUTES is pointer safe.
        # e.g. input buffer layout should be:
        # ALIGN_UP((ctypes.sizeof(SRB_IO_CONTROL), PVOID) + DEVICE_MANAGE_DATA_SET_ATTRIBUTES.
        #
        # (Parameter Block and DataSet Ranges will be indicated by fields in DEVICE_MANAGE_DATA_SET_ATTRIBUTES)
        #
        IOCTL_SCSI_MINIPORT_DSM_GENERAL = (FILE_DEVICE_SCSI << 16) + 0x0721
        # CLUSTER support
        # deliberately skipped some values to allow for expansion above.
        IOCTL_SCSI_MINIPORT_NOT_QUORUM_CAPABLE = (
            (FILE_DEVICE_SCSI << 16) + 0x0520
        )
        IOCTL_SCSI_MINIPORT_NOT_CLUSTER_CAPABLE = (
            (FILE_DEVICE_SCSI << 16) + 0x0521
        )
        # begin_ntminitape
        # Read Capacity Data - returned in Big Endian format
        _READ_CAPACITY_DATA._fields_ = [
            ('LogicalBlockAddress', ULONG),
            ('BytesPerBlock', ULONG),
        ]
        _READ_CAPACITY_DATA_EX._fields_ = [
            ('LogicalBlockAddress', LARGE_INTEGER),
            ('BytesPerBlock', ULONG),
        ]
        RC_BASIS_LAST_LBA_NOT_SEQUENTIAL_WRITE_REQUIRED_ZONES = 0x0
        RC_BASIS_LAST_LBA_ON_LOGICAL_UNIT = 0x1
        _READ_CAPACITY16_DATA._fields_ = [
            ('LogicalBlockAddress', LARGE_INTEGER),
            ('BytesPerBlock', ULONG),
            ('ProtectionEnable', UCHAR, 1),
            ('ProtectionType', UCHAR, 3),
            ('RcBasis', UCHAR, 2),
            ('Reserved', UCHAR, 2),
            ('LogicalPerPhysicalExponent', UCHAR, 4),
            ('ProtectionInfoExponent', UCHAR, 4),
            ('LowestAlignedBlock_MSB', UCHAR, 6),
            ('LBPRZ', UCHAR, 1),
            ('LBPME', UCHAR, 1),
            ('LowestAlignedBlock_LSB', UCHAR),
            ('Reserved3', UCHAR * 16),
        ]
        # Get LBA Status structures, returned in Big Endian format.
        _LBA_STATUS_DESCRIPTOR._fields_ = [
            ('StartingLBA', ULONGLONG),
            ('LogicalBlockCount', ULONG),
            ('ProvisioningStatus', UCHAR, 4),
            ('Reserved1', UCHAR, 4),
            ('Reserved2', UCHAR * 3),
        ]
        _TEMP__LBA_STATUS_LIST_HEADER = [
            ('ParameterLength', ULONG),
            ('Reserved', ULONG),
        ]
        if not defined(__midl):
            _TEMP__LBA_STATUS_LIST_HEADER += [
                ('Descriptors', LBA_STATUS_DESCRIPTOR * 0),
            ]
        # END IF
        _LBA_STATUS_LIST_HEADER._fields_ = _TEMP__LBA_STATUS_LIST_HEADER
        LBA_STATUS_MAPPED = 0x0
        LBA_STATUS_DEALLOCATED = 0x1
        LBA_STATUS_ANCHORED = 0x2


        # Read Block Limits Data - returned in Big Endian format
        # This structure returns the maximum and minimum block
        # size for a TAPE device.
        _READ_BLOCK_LIMITS._fields_ = [
            ('Reserved', UCHAR),
            ('BlockMaximumSize', UCHAR * 3),
            ('BlockMinimumSize', UCHAR * 2),
        ]

        _READ_BUFFER_CAPACITY_DATA._fields_ = [
            ('DataLength', UCHAR * 2),
            ('Reserved1', UCHAR),
            ('BlockDataReturned', UCHAR, 1),
            ('Reserved4', UCHAR, 7),
            ('TotalBufferSize', UCHAR * 4),
            ('AvailableBufferSize', UCHAR * 4),
        ]


        # Report Zones data structures.
        # Returned data contains REPORT_ZONES_DATA as header,
        # and ZONE_DESCRIPTIOR(s)
        ZONE_TYPE_CONVENTIONAL = 0x1
        ZONE_TYPE_SEQUENTIAL_WRITE_REQUIRED = 0x2
        ZONE_TYPE_SEQUENTIAL_WRITE_PREFERRED = 0x3
        ZONE_CONDITION_NOT_WRITE_POINTER = 0x0
        ZONE_CONDITION_EMPTY = 0x1
        ZONE_CONDITION_IMPLICITLY_OPENED = 0x2
        ZONE_CONDITION_EXPLICITLY_OPENED = 0x3
        ZONE_CONDITION_CLOSED = 0x4
        ZONE_CONDITION_READ_ONLY = 0xD
        ZONE_CONDITION_FULL = 0xE
        ZONE_CONDITION_OFFLINE = 0xF


        _ZONE_DESCRIPTIOR._fields_ = [
            ('ZoneType', UCHAR, 4),
            ('Reserved1', UCHAR, 4),
            ('Reset', UCHAR, 1),
            ('Non_Seq', UCHAR, 1),
            ('Reserved2', UCHAR, 2),
            ('ZoneCondition', UCHAR, 4),
            ('Reserved3', UCHAR * 6),
            ('ZoneLength', UCHAR * 8),
            ('ZoneStartLBA', UCHAR * 8),
            ('WritePointerLBA', UCHAR * 8),
            ('Reserved4', UCHAR * 32),
        ]
        ZONES_TYPE_AND_LENGTH_MAY_DIFFERENT = 0x0
        ZONES_TYPE_SAME_LENGTH_SAME = 0x1
        ZONES_TYPE_SAME_LAST_ZONE_LENGTH_DIFFERENT = 0x2
        ZONES_TYPE_MAY_DIFFERENT_LENGTH_SAME = 0x3


        _TEMP__REPORT_ZONES_DATA = [
            ('ZoneListLength', UCHAR * 4),
            ('Same', UCHAR, 4),
            ('Reserved1', UCHAR, 4),
            ('Reserved2', UCHAR * 3),
            ('MaxLBA', UCHAR * 8),
            ('Reserved3', UCHAR * 48),
        ]
        if not defined(__midl):
            _TEMP__REPORT_ZONES_DATA += [
                ('ZoneDescriptors', ZONE_DESCRIPTIOR * ANYSIZE_ARRAY),
            ]
        # END IF
        _REPORT_ZONES_DATA._fields_ = _TEMP__REPORT_ZONES_DATA


        # Mode data structures.
        # Define Mode parameter header.
        _MODE_PARAMETER_HEADER._fields_ = [
            ('ModeDataLength', UCHAR),
            ('MediumType', UCHAR),
            ('DeviceSpecificParameter', UCHAR),
            ('BlockDescriptorLength', UCHAR),
        ]

        _MODE_PARAMETER_HEADER10._fields_ = [
            ('ModeDataLength', UCHAR * 2),
            ('MediumType', UCHAR),
            ('DeviceSpecificParameter', UCHAR),
            ('Reserved', UCHAR * 2),
            ('BlockDescriptorLength', UCHAR * 2),
        ]
        MODE_FD_SINGLE_SIDE = 0x01
        MODE_FD_DOUBLE_SIDE = 0x02
        MODE_FD_MAXIMUM_TYPE = 0x1E
        MODE_DSP_FUA_SUPPORTED = 0x10
        MODE_DSP_WRITE_PROTECT = 0x80


        # Define the mode parameter block.
        _MODE_PARAMETER_BLOCK._fields_ = [
            ('DensityCode', UCHAR),
            ('NumberOfBlocks', UCHAR * 3),
            ('Reserved', UCHAR),
            ('BlockLength', UCHAR * 3),
        ]


        # Define Disconnect - Reconnect page.
        _MODE_DISCONNECT_PAGE._fields_ = [
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            ('PageSavable', UCHAR, 1),
            ('PageLength', UCHAR),
            ('BufferFullRatio', UCHAR),
            ('BufferEmptyRatio', UCHAR),
            ('BusInactivityLimit', UCHAR * 2),
            ('BusDisconnectTime', UCHAR * 2),
            ('BusConnectTime', UCHAR * 2),
            ('MaximumBurstSize', UCHAR * 2),
            ('DataTransferDisconnect', UCHAR, 2),
            ('Reserved2', UCHAR * 3),
        ]


        # Define mode caching page.
        _MODE_CACHING_PAGE._fields_ = [
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            ('PageSavable', UCHAR, 1),
            ('PageLength', UCHAR),
            ('ReadDisableCache', UCHAR, 1),
            ('MultiplicationFactor', UCHAR, 1),
            ('WriteCacheEnable', UCHAR, 1),
            ('Reserved2', UCHAR, 5),
            ('WriteRetensionPriority', UCHAR, 4),
            ('ReadRetensionPriority', UCHAR, 4),
            ('DisablePrefetchTransfer', UCHAR * 2),
            ('MinimumPrefetch', UCHAR * 2),
            ('MaximumPrefetch', UCHAR * 2),
            ('MaximumPrefetchCeiling', UCHAR * 2),
        ]

        _MODE_CACHING_PAGE_EX._fields_ = [
            # 0x08
            ('PageCode', UCHAR, 6),
            ('SubPageFormat', UCHAR, 1),
            ('PageSavable', UCHAR, 1),
            ('PageLength', UCHAR),
            ('ReadDisableCache', UCHAR, 1),
            ('MultiplicationFactor', UCHAR, 1),
            ('WriteCacheEnable', UCHAR, 1),
            ('SizeEnable', UCHAR, 1),
            ('Discontinuity', UCHAR, 1),
            ('CachingAnalysisPermitted', UCHAR, 1),
            ('AbortPreFetch', UCHAR, 1),
            ('InitiatorControl', UCHAR, 1),
            ('WriteRetensionPriority', UCHAR, 4),
            ('ReadRetensionPriority', UCHAR, 4),
            ('DisablePrefetchTransfer', UCHAR * 2),
            ('MinimumPrefetch', UCHAR * 2),
            ('MaximumPrefetch', UCHAR * 2),
            ('MaximumPrefetchCeiling', UCHAR * 2),
            ('NvCacheDisable', UCHAR, 1),
            ('SyncCacheProgress', UCHAR, 2),
            ('VendorSpecific', UCHAR, 2),
            ('DisableReadAhead', UCHAR, 1),
            ('LogicalBlockCacheSegmentSize', UCHAR, 1),
            ('ForceSequentialWrite', UCHAR, 1),
            ('NumberOfCacheSegments', UCHAR),
            ('CacheSegmentSize', UCHAR * 2),
            ('Reserved', UCHAR * 4),
        ]

        _MODE_CONTROL_PAGE._fields_ = [
            # 0x0A
            ('PageCode', UCHAR, 6),
            ('Reserved1', UCHAR, 1),
            ('PageSavable', UCHAR, 1),
            ('PageLength', UCHAR),
            ('RLEC', UCHAR, 1),
            ('GLTSD', UCHAR, 1),
            ('D_SENSE', UCHAR, 1),
            ('DPICZ', UCHAR, 1),
            ('TMF_ONLY', UCHAR, 1),
            ('TST', UCHAR, 3),
            ('Obsolete1', UCHAR, 1),
            ('QERR', UCHAR, 2),
            ('NUAR', UCHAR, 1),
            ('QueueAlgorithmModifier', UCHAR, 4),
            ('Obsolete2', UCHAR, 3),
            ('SWP', UCHAR, 1),
            ('UA_INTLCK_CTRL', UCHAR, 2),
            ('RAC', UCHAR, 1),
            ('VS', UCHAR, 1),
            ('AutoloadMode', UCHAR, 3),
            ('Reserved2', UCHAR, 1),
            ('RWWP', UCHAR, 1),
            ('ATMPE', UCHAR, 1),
            ('TAS', UCHAR, 1),
            ('ATO', UCHAR, 1),
            ('Obsolete3', UCHAR * 2),
            ('BusyTimeoutPeriod', UCHAR * 2),
            ('ExtendeSelfTestCompletionTime', UCHAR * 2),
        ]


        # Define write parameters cdrom page
        _MODE_CDROM_WRITE_PARAMETERS_PAGE2._fields_ = [
            # 0x05
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            ('PageSavable', UCHAR, 1),
            # 0x32 ??
            ('PageLength', UCHAR),
            ('WriteType', UCHAR, 4),
            ('TestWrite', UCHAR, 1),
            ('LinkSizeValid', UCHAR, 1),
            ('BufferUnderrunFreeEnabled', UCHAR, 1),
            ('Reserved2', UCHAR, 1),
            ('TrackMode', UCHAR, 4),
            ('Copy', UCHAR, 1),
            ('FixedPacket', UCHAR, 1),
            ('MultiSession', UCHAR, 2),
            ('DataBlockType', UCHAR, 4),
            ('Reserved3', UCHAR, 4),
            ('LinkSize', UCHAR),
            ('Reserved4', UCHAR),
            ('HostApplicationCode', UCHAR, 6),
            ('Reserved5', UCHAR, 2),
            ('SessionFormat', UCHAR),
            ('Reserved6', UCHAR),
            ('PacketSize', UCHAR * 4),
            ('AudioPauseLength', UCHAR * 2),
            ('MediaCatalogNumber', UCHAR * 16),
            ('ISRC', UCHAR * 16),
            ('SubHeaderData', UCHAR * 4),
        ]

        DEPRECATE_DDK_FUNCTIONS = None

        if not defined(DEPRECATE_DDK_FUNCTIONS):
            # this structure is being retired due to missing fields and overly
            # complex data definitions for the MCN and ISRC.
            _MODE_CDROM_WRITE_PARAMETERS_PAGE._fields_ = [
                # 0x32 ??
                ('PageLength', UCHAR),
                ('WriteType', UCHAR, 4),
                ('TestWrite', UCHAR, 1),
                ('LinkSizeValid', UCHAR, 1),
                ('BufferUnderrunFreeEnabled', UCHAR, 1),
                ('Reserved2', UCHAR, 1),
                ('TrackMode', UCHAR, 4),
                ('Copy', UCHAR, 1),
                ('FixedPacket', UCHAR, 1),
                ('MultiSession', UCHAR, 2),
                ('DataBlockType', UCHAR, 4),
                ('Reserved3', UCHAR, 4),
                ('LinkSize', UCHAR),
                ('Reserved4', UCHAR),
                ('HostApplicationCode', UCHAR, 6),
                ('Reserved5', UCHAR, 2),
                ('SessionFormat', UCHAR),
                ('Reserved6', UCHAR),
                ('PacketSize', UCHAR * 4),
                ('AudioPauseLength', UCHAR * 2),
                ('Reserved7', UCHAR, 7),
                ('MediaCatalogNumberValid', UCHAR, 1),
                ('MediaCatalogNumber', UCHAR * 13),
                ('MediaCatalogNumberZero', UCHAR),
                ('MediaCatalogNumberAFrame', UCHAR),
                ('Reserved8', UCHAR, 7),
                ('ISRCValid', UCHAR, 1),
                ('ISRCCountry', UCHAR * 2),
                ('ISRCOwner', UCHAR * 3),
                ('ISRCRecordingYear', UCHAR * 2),
                ('ISRCSerialNumber', UCHAR * 5),
                ('ISRCZero', UCHAR),
                ('ISRCAFrame', UCHAR),
                ('ISRCReserved', UCHAR),
                ('SubHeaderData', UCHAR * 4),
            ]
        # END IF  ifndef DEPRECATE_DDK_FUNCTIONS

        # Define the MRW mode page for CDROM device types
        _MODE_MRW_PAGE._fields_ = [
            # 0x03
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            ('PageSavable', UCHAR, 1),
            # 0x06
            ('PageLength', UCHAR),
            ('Reserved1', UCHAR),
            ('LbaSpace', UCHAR, 1),
            ('Reserved2', UCHAR, 7),
            ('Reserved3', UCHAR * 4),
        ]


        # Define mode flexible disk page.
        _MODE_FLEXIBLE_DISK_PAGE._fields_ = [
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            ('PageSavable', UCHAR, 1),
            ('PageLength', UCHAR),
            ('TransferRate', UCHAR * 2),
            ('NumberOfHeads', UCHAR),
            ('SectorsPerTrack', UCHAR),
            ('BytesPerSector', UCHAR * 2),
            ('NumberOfCylinders', UCHAR * 2),
            ('StartWritePrecom', UCHAR * 2),
            ('StartReducedCurrent', UCHAR * 2),
            ('StepRate', UCHAR * 2),
            ('StepPluseWidth', UCHAR),
            ('HeadSettleDelay', UCHAR * 2),
            ('MotorOnDelay', UCHAR),
            ('MotorOffDelay', UCHAR),
            ('Reserved2', UCHAR, 5),
            ('MotorOnAsserted', UCHAR, 1),
            ('StartSectorNumber', UCHAR, 1),
            ('TrueReadySignal', UCHAR, 1),
            ('StepPlusePerCyclynder', UCHAR, 4),
            ('Reserved3', UCHAR, 4),
            ('WriteCompenstation', UCHAR),
            ('HeadLoadDelay', UCHAR),
            ('HeadUnloadDelay', UCHAR),
            ('Pin2Usage', UCHAR, 4),
            ('Pin34Usage', UCHAR, 4),
            ('Pin1Usage', UCHAR, 4),
            ('Pin4Usage', UCHAR, 4),
            ('MediumRotationRate', UCHAR * 2),
            ('Reserved4', UCHAR * 2),
        ]


        # Define mode format page.
        _MODE_FORMAT_PAGE._fields_ = [
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            ('PageSavable', UCHAR, 1),
            ('PageLength', UCHAR),
            ('TracksPerZone', UCHAR * 2),
            ('AlternateSectorsPerZone', UCHAR * 2),
            ('AlternateTracksPerZone', UCHAR * 2),
            ('AlternateTracksPerLogicalUnit', UCHAR * 2),
            ('SectorsPerTrack', UCHAR * 2),
            ('BytesPerPhysicalSector', UCHAR * 2),
            ('Interleave', UCHAR * 2),
            ('TrackSkewFactor', UCHAR * 2),
            ('CylinderSkewFactor', UCHAR * 2),
            ('Reserved2', UCHAR, 4),
            ('SurfaceFirst', UCHAR, 1),
            ('RemovableMedia', UCHAR, 1),
            ('HardSectorFormating', UCHAR, 1),
            ('SoftSectorFormating', UCHAR, 1),
            ('Reserved3', UCHAR * 3),
        ]


        # Define rigid disk driver geometry page.
        _MODE_RIGID_GEOMETRY_PAGE._fields_ = [
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            ('PageSavable', UCHAR, 1),
            ('PageLength', UCHAR),
            ('NumberOfCylinders', UCHAR * 3),
            ('NumberOfHeads', UCHAR),
            ('StartWritePrecom', UCHAR * 3),
            ('StartReducedCurrent', UCHAR * 3),
            ('DriveStepRate', UCHAR * 2),
            ('LandZoneCyclinder', UCHAR * 3),
            ('RotationalPositionLock', UCHAR, 2),
            ('Reserved2', UCHAR, 6),
            ('RotationOffset', UCHAR),
            ('Reserved3', UCHAR),
            ('RoataionRate', UCHAR * 2),
            ('Reserved4', UCHAR * 2),
        ]


        # Define read write recovery page
        _MODE_READ_WRITE_RECOVERY_PAGE._fields_ = [
            ('PageCode', UCHAR, 6),
            ('Reserved1', UCHAR, 1),
            ('PSBit', UCHAR, 1),
            ('PageLength', UCHAR),
            ('DCRBit', UCHAR, 1),
            ('DTEBit', UCHAR, 1),
            ('PERBit', UCHAR, 1),
            ('EERBit', UCHAR, 1),
            ('RCBit', UCHAR, 1),
            ('TBBit', UCHAR, 1),
            ('ARRE', UCHAR, 1),
            ('AWRE', UCHAR, 1),
            ('ReadRetryCount', UCHAR),
            ('Reserved4', UCHAR * 4),
            ('WriteRetryCount', UCHAR),
            ('Reserved5', UCHAR * 3),
        ]


        # Define read recovery page - cdrom
        _MODE_READ_RECOVERY_PAGE._fields_ = [
            ('PageCode', UCHAR, 6),
            ('Reserved1', UCHAR, 1),
            ('PSBit', UCHAR, 1),
            ('PageLength', UCHAR),
            ('DCRBit', UCHAR, 1),
            ('DTEBit', UCHAR, 1),
            ('PERBit', UCHAR, 1),
            ('Reserved2', UCHAR, 1),
            ('RCBit', UCHAR, 1),
            ('TBBit', UCHAR, 1),
            ('Reserved3', UCHAR, 2),
            ('ReadRetryCount', UCHAR),
            ('Reserved4', UCHAR * 4),
        ]


        # Define Informational Exception Control Page. Used for failure
        # prediction
        _MODE_INFO_EXCEPTIONS._fields_ = [
            ('PageCode', UCHAR, 6),
            ('Reserved1', UCHAR, 1),
            ('PSBit', UCHAR, 1),
            ('PageLength', UCHAR),
            ('Flags', UCHAR),
            ('LogErr', UCHAR, 1),
            ('Reserved2', UCHAR, 1),
            ('Test', UCHAR, 1),
            ('Dexcpt', UCHAR, 1),
            ('Reserved3', UCHAR, 3),
            ('Perf', UCHAR, 1),
            ('ReportMethod', UCHAR, 4),
            ('Reserved4', UCHAR, 4),
            ('IntervalTimer', UCHAR * 4),
            ('ReportCount', UCHAR * 4),
        ]


        # Begin C/DVD 0.9 definitions
        # Power Condition Mode Page Format
        _POWER_CONDITION_PAGE._fields_ = [
            # 0x1A
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            ('PSBit', UCHAR, 1),
            # 0x0A
            ('PageLength', UCHAR),
            ('Reserved2', UCHAR),
            ('Standby', UCHAR, 1),
            ('Idle', UCHAR, 1),
            ('Reserved3', UCHAR, 6),
            ('IdleTimer', UCHAR * 4),
            ('StandbyTimer', UCHAR * 4),
        ]


        # CD - Audio Control Mode Page Format
        _CDDA_OUTPUT_PORT._fields_ = [
            ('ChannelSelection', UCHAR, 4),
            ('Reserved', UCHAR, 4),
            ('Volume', UCHAR),
        ]

        _CDAUDIO_CONTROL_PAGE._fields_ = [
            # 0x0E
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            ('PSBit', UCHAR, 1),
            # 0x0E
            ('PageLength', UCHAR),
            ('Reserved2', UCHAR, 1),
            # Default 0
            ('StopOnTrackCrossing', UCHAR, 1),
            # Always 1
            ('Immediate', UCHAR, 1),
            ('Reserved3', UCHAR, 5),
            ('Reserved4', UCHAR * 3),
            ('Obsolete', UCHAR * 2),
            ('CDDAOutputPorts', CDDA_OUTPUT_PORT * 4),
        ]
        CDDA_CHANNEL_MUTED = 0x0
        CDDA_CHANNEL_ZERO = 0x1
        CDDA_CHANNEL_ONE = 0x2
        CDDA_CHANNEL_TWO = 0x4
        CDDA_CHANNEL_THREE = 0x8


        # C/DVD Feature Set Support & Version Page
        _CDVD_FEATURE_SET_PAGE._fields_ = [
            # 0x18
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            ('PSBit', UCHAR, 1),
            # 0x16
            ('PageLength', UCHAR),
            ('CDAudio', UCHAR * 2),
            ('EmbeddedChanger', UCHAR * 2),
            ('PacketSMART', UCHAR * 2),
            ('PersistantPrevent', UCHAR * 2),
            ('EventStatusNotification', UCHAR * 2),
            ('DigitalOutput', UCHAR * 2),
            ('CDSequentialRecordable', UCHAR * 2),
            ('DVDSequentialRecordable', UCHAR * 2),
            ('RandomRecordable', UCHAR * 2),
            ('KeyExchange', UCHAR * 2),
            ('Reserved2', UCHAR * 2),
        ]


        # CDVD Inactivity Time - out Page Format
        _CDVD_INACTIVITY_TIMEOUT_PAGE._fields_ = [
            # 0x1D
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            ('PSBit', UCHAR, 1),
            # 0x08
            ('PageLength', UCHAR),
            ('Reserved2', UCHAR * 2),
            ('SWPP', UCHAR, 1),
            ('DISP', UCHAR, 1),
            ('Reserved3', UCHAR, 6),
            ('Reserved4', UCHAR),
            ('GroupOneMinimumTimeout', UCHAR * 2),
            ('GroupTwoMinimumTimeout', UCHAR * 2),
        ]


        # CDVD Capabilities & Mechanism Status Page
        CDVD_LMT_CADDY = 0
        CDVD_LMT_TRAY = 1
        CDVD_LMT_POPUP = 2
        CDVD_LMT_RESERVED1 = 3
        CDVD_LMT_CHANGER_INDIVIDUAL = 4
        CDVD_LMT_CHANGER_CARTRIDGE = 5
        CDVD_LMT_RESERVED2 = 6
        CDVD_LMT_RESERVED3 = 7


        class _Union_6(ctypes.Union):
            pass


        _Union_6._fields_ = [
            ('ReadSpeedMaximum', UCHAR * 2),
            # offset 8
            ('ObsoleteReserved', UCHAR * 2),
        ]
        _CDVD_CAPABILITIES_PAGE._Union_6 = _Union_6


        class _Union_7(ctypes.Union):
            pass


        _Union_7._fields_ = [
            ('ReadSpeedCurrent', UCHAR * 2),
            # offset 14
            ('ObsoleteReserved2', UCHAR * 2),
        ]
        _CDVD_CAPABILITIES_PAGE._Union_7 = _Union_7


        class _Union_8(ctypes.Union):
            pass


        _Union_8._fields_ = [
            ('WriteSpeedMaximum', UCHAR * 2),
            # offset 18
            ('ObsoleteReserved4', UCHAR * 2),
        ]
        _CDVD_CAPABILITIES_PAGE._Union_8 = _Union_8


        class _Union_9(ctypes.Union):
            pass


        _Union_9._fields_ = [
            ('WriteSpeedCurrent', UCHAR * 2),
            # offset 20
            ('ObsoleteReserved11', UCHAR * 2),
        ]
        _CDVD_CAPABILITIES_PAGE._Union_9 = _Union_9


        class _Union_10(ctypes.Union):
            pass


        _Union_10._fields_ = [
            # offset 22
            ('CopyManagementRevision', UCHAR * 2),
            ('Reserved10', UCHAR * 2),
        ]
        _CDVD_CAPABILITIES_PAGE._Union_10 = _Union_10

        _CDVD_CAPABILITIES_PAGE._anonymous_ = (
            '_Union_6',
            '_Union_7',
            '_Union_8',
            '_Union_9',
            '_Union_10',
        )

        _CDVD_CAPABILITIES_PAGE._fields_ = [
            # 0x2A
            ('PageCode', UCHAR, 6),
            ('Reserved', UCHAR, 1),
            # offset 0
            ('PSBit', UCHAR, 1),
            # HAR PageLength; // >= 0x18 // offset 1
            ('CDRRead', UCHAR, 1),
            ('CDERead', UCHAR, 1),
            ('Method2', UCHAR, 1),
            ('DVDROMRead', UCHAR, 1),
            ('DVDRRead', UCHAR, 1),
            ('DVDRAMRead', UCHAR, 1),
            # offset 2
            ('Reserved2', UCHAR, 2),
            ('CDRWrite', UCHAR, 1),
            ('CDEWrite', UCHAR, 1),
            ('TestWrite', UCHAR, 1),
            ('Reserved3', UCHAR, 1),
            ('DVDRWrite', UCHAR, 1),
            ('DVDRAMWrite', UCHAR, 1),
            # offset 3
            ('Reserved4', UCHAR, 2),
            ('AudioPlay', UCHAR, 1),
            ('Composite', UCHAR, 1),
            ('DigitalPortOne', UCHAR, 1),
            ('DigitalPortTwo', UCHAR, 1),
            ('Mode2Form1', UCHAR, 1),
            ('Mode2Form2', UCHAR, 1),
            ('MultiSession', UCHAR, 1),
            # offset 4
            ('BufferUnderrunFree', UCHAR, 1),
            ('CDDA', UCHAR, 1),
            ('CDDAAccurate', UCHAR, 1),
            ('RWSupported', UCHAR, 1),
            ('RWDeinterleaved', UCHAR, 1),
            ('C2Pointers', UCHAR, 1),
            ('ISRC', UCHAR, 1),
            ('UPC', UCHAR, 1),
            # offset 5
            ('ReadBarCodeCapable', UCHAR, 1),
            ('Lock', UCHAR, 1),
            ('LockState', UCHAR, 1),
            ('PreventJumper', UCHAR, 1),
            ('Eject', UCHAR, 1),
            ('Reserved6', UCHAR, 1),
            # offset 6
            ('LoadingMechanismType', UCHAR, 3),
            ('SeparateVolume', UCHAR, 1),
            ('SeperateChannelMute', UCHAR, 1),
            ('SupportsDiskPresent', UCHAR, 1),
            ('SWSlotSelection', UCHAR, 1),
            ('SideChangeCapable', UCHAR, 1),
            ('RWInLeadInReadable', UCHAR, 1),
            # offset 7
            ('Reserved7', UCHAR, 2),
            ('_Union_6', _CDVD_CAPABILITIES_PAGE._Union_6),
            # offset 10
            ('NumberVolumeLevels', UCHAR * 2),
            # offset 12
            ('BufferSize', UCHAR * 2),
            ('_Union_7', _CDVD_CAPABILITIES_PAGE._Union_7),
            # offset 16
            ('ObsoleteReserved3', UCHAR),
            ('Reserved8', UCHAR, 1),
            ('BCK', UCHAR, 1),
            ('RCK', UCHAR, 1),
            ('LSBF', UCHAR, 1),
            ('Length', UCHAR, 2),
            # offset 17
            ('Reserved9', UCHAR, 2),
            ('_Union_8', _CDVD_CAPABILITIES_PAGE._Union_8),
            ('_Union_9', _CDVD_CAPABILITIES_PAGE._Union_9),
            # their own by looking at Reserved10[]).
            ('_Union_10', _CDVD_CAPABILITIES_PAGE._Union_10),
        ]
        _TEMP__LUN_LIST = [

            # (ctypes.sizeof LunSize * 8
            ('LunListLength', UCHAR * 4),
            ('Reserved', UCHAR * 4),
        ]
        if not defined(__midl):
            _TEMP__LUN_LIST += [
                # 4 level of addressing. 2 bytes each.
                ('Lun', (UCHAR * 0)(UCHAR * 8)),
            ]
        # END IF
        _LUN_LIST._fields_ = _TEMP__LUN_LIST
        LOADING_MECHANISM_CADDY = 0x00
        LOADING_MECHANISM_TRAY = 0x01
        LOADING_MECHANISM_POPUP = 0x02
        LOADING_MECHANISM_INDIVIDUAL_CHANGER = 0x04
        LOADING_MECHANISM_CARTRIDGE_CHANGER = 0x05


        # end C/DVD 0.9 mode page definitions
        # Mode parameter list block descriptor -
        # set the block length for reading/writing
        MODE_BLOCK_DESC_LENGTH = 8
        MODE_HEADER_LENGTH = 4
        MODE_HEADER_LENGTH10 = 8


        _MODE_PARM_READ_WRITE._fields_ = [
            # List Header Format
            ('ParameterListHeader', MODE_PARAMETER_HEADER),
            # List Block Descriptor
            ('ParameterListBlock', MODE_PARAMETER_BLOCK),
        ]

        # end_ntminitape
        # CDROM audio control (0x0E)
        CDB_AUDIO_PAUSE = 0
        CDB_AUDIO_RESUME = 1
        CDB_DEVICE_START = 0x11
        CDB_DEVICE_STOP = 0x10
        CDB_EJECT_MEDIA = 0x10
        CDB_LOAD_MEDIA = 0x01
        CDB_SUBCHANNEL_HEADER = 0x00
        CDB_SUBCHANNEL_BLOCK = 0x01
        CDROM_AUDIO_CONTROL_PAGE = 0x0E
        MODE_SELECT_IMMEDIATE = 0x04
        MODE_SELECT_PFBIT = 0x10
        CDB_USE_MSF = 0x01


        _PORT_OUTPUT._fields_ = [
            ('ChannelSelection', UCHAR),
            ('Volume', UCHAR),
        ]

        _AUDIO_OUTPUT._fields_ = [
            ('CodePage', UCHAR),
            ('ParameterLength', UCHAR),
            ('Immediate', UCHAR),
            ('Reserved', UCHAR * 2),
            ('LbaFormat', UCHAR),
            ('LogicalBlocksPerSecond', UCHAR * 2),
            ('PortOutput', PORT_OUTPUT * 4),
        ]


        # Multisession CDROM
        GET_LAST_SESSION = 0x01
        GET_SESSION_DATA = 0x02;


        # Atapi 2.5 changer
        _MECHANICAL_STATUS_INFORMATION_HEADER._fields_ = [
            ('CurrentSlot', UCHAR, 5),
            ('ChangerState', UCHAR, 2),
            ('Fault', UCHAR, 1),
            ('Reserved', UCHAR, 5),
            ('MechanismState', UCHAR, 3),
            ('CurrentLogicalBlockAddress', UCHAR * 3),
            ('NumberAvailableSlots', UCHAR),
            ('SlotTableLength', UCHAR * 2),
        ]

        _SLOT_TABLE_INFORMATION._fields_ = [
            ('DiscChanged', UCHAR, 1),
            ('Reserved', UCHAR, 6),
            ('DiscPresent', UCHAR, 1),
            ('Reserved2', UCHAR * 3),
        ]

        _MECHANICAL_STATUS._fields_ = [
            ('MechanicalStatusHeader', MECHANICAL_STATUS_INFORMATION_HEADER),
            ('SlotTableInfo', SLOT_TABLE_INFORMATION * 1),
        ]


        # Structure related to 0x42 - SCSIOP_UNMAP
        _UNMAP_BLOCK_DESCRIPTOR._fields_ = [
            ('StartingLba', UCHAR * 8),
            ('LbaCount', UCHAR * 4),
            ('Reserved', UCHAR * 4),
        ]

        _TEMP__UNMAP_LIST_HEADER = [
            ('DataLength', UCHAR * 2),
            ('BlockDescrDataLength', UCHAR * 2),
            ('Reserved', UCHAR * 4),
        ]
        if not defined(__midl):
            _TEMP__UNMAP_LIST_HEADER += [
                ('Descriptors', UNMAP_BLOCK_DESCRIPTOR * 0),
            ]
        # END IF
        _UNMAP_LIST_HEADER._fields_ = _TEMP__UNMAP_LIST_HEADER

        # begin_ntminitape
        # Tape definitions
        _TAPE_POSITION_DATA._fields_ = [
            ('Reserved1', UCHAR, 2),
            ('BlockPositionUnsupported', UCHAR, 1),
            ('Reserved2', UCHAR, 3),
            ('EndOfPartition', UCHAR, 1),
            ('BeginningOfPartition', UCHAR, 1),
            ('PartitionNumber', UCHAR),
            ('Reserved3', USHORT),
            ('FirstBlock', UCHAR * 4),
            ('LastBlock', UCHAR * 4),
            ('Reserved4', UCHAR),
            ('NumberOfBlocks', UCHAR * 3),
            ('NumberOfBytes', UCHAR * 4),
        ]


        # This structure is used to convert little endian
        # ULONGs to SCSI CDB big endians values.
        class _Struct_1(ctypes.Structure):
            pass


        _Struct_1._fields_ = [
            ('Byte0', UCHAR),
            ('Byte1', UCHAR),
            ('Byte2', UCHAR),
            ('Byte3', UCHAR),
            ('Byte4', UCHAR),
            ('Byte5', UCHAR),
            ('Byte6', UCHAR),
            ('Byte7', UCHAR),
        ]
        _EIGHT_BYTE._Struct_1 = _Struct_1

        _EIGHT_BYTE._anonymous_ = (
            '_Struct_1',
        )

        _EIGHT_BYTE._fields_ = [
            ('_Struct_1', _EIGHT_BYTE._Struct_1),
            ('AsULongLong', ULONGLONG),
        ]


        class _Struct_2(ctypes.Structure):
            pass


        _Struct_2._fields_ = [
            ('Byte0', UCHAR),
            ('Byte1', UCHAR),
            ('Byte2', UCHAR),
            ('Byte3', UCHAR),
        ]
        _FOUR_BYTE._Struct_2 = _Struct_2

        _FOUR_BYTE._anonymous_ = (
            '_Struct_2',
        )

        _FOUR_BYTE._fields_ = [
            ('_Struct_2', _FOUR_BYTE._Struct_2),
            ('AsULong', ULONG),
        ]


        class _Struct_3(ctypes.Structure):
            pass


        _Struct_3._fields_ = [
            ('Byte0', UCHAR),
            ('Byte1', UCHAR),
        ]
        _TWO_BYTE._Struct_3 = _Struct_3

        _TWO_BYTE._anonymous_ = (
            '_Struct_3',
        )

        _TWO_BYTE._fields_ = [
            ('_Struct_3', _TWO_BYTE._Struct_3),
            ('AsUShort', USHORT),
        ]


        # This structure is used to convert little endian
        # ULONGs to SCSI CDB big endians values.
        # Byte reversing macro for converting
        # between big- and little - endian formats

        def REVERSE_BYTES_8(Destination, Source):
            d = PEIGHT_BYTE(Destination)
            s = PEIGHT_BYTE(Source)
            d.Byte7 = s.Byte0
            d.Byte6 = s.Byte1
            d.Byte5 = s.Byte2
            d.Byte4 = s.Byte3
            d.Byte3 = s.Byte4
            d.Byte2 = s.Byte5
            d.Byte1 = s.Byte6
            d.Byte0 = s.Byte7
            return d


        REVERSE_BYTES_QUAD = REVERSE_BYTES_8


        def REVERSE_BYTES_6(Destination, Source):
            d = PEIGHT_BYTE(Destination)
            s = PEIGHT_BYTE(Source)
            d.Byte5 = s.Byte0
            d.Byte4 = s.Byte1
            d.Byte3 = s.Byte2
            d.Byte2 = s.Byte3
            d.Byte1 = s.Byte4
            d.Byte0 = s.Byte5
            return d


        def REVERSE_BYTES_4(Destination, Source):
            d = PEIGHT_BYTE(Destination)
            s = PEIGHT_BYTE(Source)
            d.Byte3 = s.Byte0
            d.Byte2 = s.Byte1
            d.Byte1 = s.Byte2
            d.Byte0 = s.Byte3
            return d


        REVERSE_BYTES = REVERSE_BYTES_4


        def REVERSE_BYTES_2(Destination, Source):
            d = PEIGHT_BYTE(Destination)
            s = PEIGHT_BYTE(Source)
            d.Byte1 = s.Byte0
            d.Byte0 = s.Byte1
            return d


        REVERSE_BYTES_SHORT = REVERSE_BYTES_2


        # Byte reversing macro for converting
        # USHORTS from big to little endian in place
        def REVERSE_SHORT(Short):
            w = PTWO_BYTE(Short)
            tmp = w.Byte0
            w.Byte0 = w.Byte1
            w.Byte1 = tmp

            return w


        # Byte reversing macro for converting
        # ULONGS between big & little endian in place
        def REVERSE_LONG(Long):
            l = PFOUR_BYTE(Long)
            tmp = l.Byte3
            l.Byte3 = l.Byte0
            l.Byte0 = tmp
            tmp = l.Byte2
            l.Byte2 = l.Byte1
            l.Byte1 = tmp
            return l


        # Byte reversing macro for converting
        # ULONGLONGS between big & little endian in place
        def REVERSE_LONGLONG(Longlong):
            q = PEIGHT_BYTE(Longlong)
            tmp = q.Byte7
            q.Byte7 = q.Byte0
            q.Byte0 = tmp
            tmp = q.Byte6
            q.Byte6 = q.Byte1
            q.Byte1 = tmp
            tmp = q.Byte5
            q.Byte5 = q.Byte2
            q.Byte2 = tmp
            tmp = q.Byte4
            q.Byte4 = q.Byte3
            q.Byte3 = tmp

            return q


        # This macro has the effect of Bit = log2(Data)

        from pyWinAPI.km.crt import intrin_h  # NOQA


        def BitScanReverse(*args):
            pass


        def WHICH_BIT(Data, Bit):
            idx = ULONG()
            BitScanReverse(ctypes.byref(idx), Data)
            Bit = UCHAR(idx.value)

            return Bit


        # Define alignment requirements for variable length components in
        # extended SRB.
        # For Win64, need to ensure all variable length components are 8 bytes
        # align
        # so the pointer fields within the variable length components are 8
        # bytes align.
        if defined(_WIN64) or defined(_M_ALPHA):
            STOR_ADDRESS_ALIGN = ctypes.Structure
        else:
            STOR_ADDRESS_ALIGN = ctypes.Structure
        # END IF

        # Generic structure definition for accessing any STOR_ADDRESS. All
        # STOR_ADDRESS must begin with a Type, Port and AddressLength field.
        _STOR_ADDRESS._fields_ = [
            ('Type', USHORT),
            ('Port', USHORT),
            ('AddressLength', ULONG),
            ('AddressData', UCHAR * ANYSIZE_ARRAY),
        ]

        # Define different storage address types
        STOR_ADDRESS_TYPE_UNKNOWN = 0x0
        STOR_ADDRESS_TYPE_BTL8 = 0x1
        STOR_ADDRESS_TYPE_MAX = 0xFFFF

        # Define 8 bit bus, target and LUN address scheme
        STOR_ADDR_BTL8_ADDRESS_LENGTH = 4


        _STOR_ADDR_BTL8._fields_ = [
            ('Type', USHORT),
            ('Port', USHORT),
            ('AddressLength', ULONG),
            ('Path', UCHAR),
            ('Target', UCHAR),
            ('Lun', UCHAR),
            ('Reserved', UCHAR),
        ]
        if NTDDI_VERSION >= NTDDI_WIN8:
            # /////////////////////////////////////////////////////////////////
            #
            # Ses definitions
            SES_DIAGNOSTIC_PAGE_CONFIGURATION = 0x01
            SES_DIAGNOSTIC_PAGE_CONTROL = 0x02
            SES_DIAGNOSTIC_PAGE_STATUS = 0x02
            SES_DIAGNOSTIC_PAGE_STRING_IN = 0x04
            SES_DIAGNOSTIC_PAGE_ADDITIONAL_ELEMENT_STATUS = 0x0A
            SES_DIAGNOSTIC_PAGE_DOWNLOAD_MICROCODE = 0x0E
            SES_SAS_PROTOCOL_IDENTIFIER = 6


            class _SES_ELEMENT_TYPE(ENUM):
                SesElementTypeUnknown = 0
                SesElementTypeDeviceSlot = 1
                SesElementTypePowerSupply = 2
                SesElementTypeCooling = 3
                SesElementTypeTemperatureSensor = 4
                SesElementTypeDoor = 5
                SesElementTypeAudibleAlarm = 6
                SesElementTypeController = 7
                SesElementTypeScsiController = 8
                SesElementTypeNonVolatileCache = 9
                SesElementTypeInvalidOperationReason = 10
                SesElementTypeUps = 11
                SesElementTypeDisplay = 12
                SesElementTypeKeypad = 13
                SesElementTypeEnclosure = 14
                SesElementTypeScsiPort = 15
                SesElementTypeLanguage = 16
                SesElementTypeCommunicationPort = 17
                SesElementTypeVoltageSensor = 18
                SesElementTypeCurrentSensor = 19
                SesElementTypeScsiTargetPort = 20
                SesElementTypeScsiInitiatorPort = 21
                SesElementTypeSubEnclosure = 22
                SesElementTypeArrayDeviceSlot = 23
                SesElementTypeSasExpander = 24
                SesElementTypeSasConnector = 25
                SesElementTypeMax = 26

            SES_ELEMENT_TYPE = _SES_ELEMENT_TYPE
            PSES_ELEMENT_TYPE = POINTER(_SES_ELEMENT_TYPE)


            class _SES_ELEMENT_STATE(ENUM):
                SesElementStateNotReported = 0
                SesElementStateOkay = 1
                SesElementStateCritical = 2
                SesElementStateNonCritical = 3
                SesElementStateUnrecoverable = 4
                SesElementStateNotInstalled = 5
                SesElementStateUnknown = 6
                SesElementStateNotAvailable = 7
                SesElementStateNoAccessAllowed = 8
                SesElementStateMax = 9

            SES_ELEMENT_STATE = _SES_ELEMENT_STATE
            PSES_ELEMENT_STATE = POINTER(_SES_ELEMENT_STATE)


            class _SES_DOWNLOAD_MICROCODE_STATE(ENUM):
                SesDownloadMcStateNoneInProgress = 0x00
                SesDownloadMcStateInProgress = 0x01
                SesDownloadMcStateCompletedPendingReset = 0x11
                SesDownloadMcStateCompletedPendingPowerOn = 0x12
                SesDownloadMcStateCompletedPendingActivation = 0x13

            SES_DOWNLOAD_MICROCODE_STATE = _SES_DOWNLOAD_MICROCODE_STATE
            PSES_DOWNLOAD_MICROCODE_STATE = POINTER(_SES_DOWNLOAD_MICROCODE_STATE)

            _SES_DIAGNOSTIC_PAGE._fields_ = [
                # Byte 0
                ('PageCode', UCHAR),
                # Byte 1
                ('Reserved', UCHAR),
                # Bytes 2 - 3
                ('PageLength', UCHAR * 2),
                ('PageData', UCHAR * ANYSIZE_ARRAY),
            ]

            _SES_TYPE_DESCRIPTOR_HEADER._fields_ = [
                # Byte 0
                ('ElementType', UCHAR),
                # Byte 1
                ('NumberOfPossibleElements', UCHAR),
                # Byte 2
                ('SubEnclosureId', UCHAR),
                # Byte 3
                ('TypeDescriptorTextLength', UCHAR),
            ]

            _SES_ENCLOSURE_DESCRIPTOR._fields_ = [
                # Byte 0, bit 0 - 2
                ('NumberOfEnclosureServices', UCHAR, 3),
                # Byte 0, bit 3
                ('Reserved1', UCHAR, 1),
                # Byte 0, bit 4 - 6
                ('RelativeEnclosureServicesId', UCHAR, 3),
                # Byte 0, bit 7
                ('Reserved2', UCHAR, 1),
                # Byte 1
                ('SubEnclosureId', UCHAR),
                # Byte 2
                ('NumberOfTypeDescriptorHeaders', UCHAR),
                # Byte 3
                ('EnclosureDescriptorLength', UCHAR),
                # Byte 4 - 11
                ('Identifier', UCHAR * 8),
                # Byte 12 - 19
                ('VendorId', UCHAR * 8),
                # Byte 20 - 35
                ('ProductId', UCHAR * 16),
                # Byte 36 - 39
                ('ProductRevisionLevel', UCHAR * 4),
                ('VendorSpecific', UCHAR * ANYSIZE_ARRAY),
            ]

            _SES_CONFIGURATION_DIAGNOSTIC_PAGE._fields_ = [
                # Byte 0
                ('PageCode', UCHAR),
                # Byte 1
                ('NumberOfSecondarySubEnclosures', UCHAR),
                # Bytes 2 - 3
                ('PageLength', UCHAR * 2),
                # Bytes 4 - 7
                ('GenerationCode', UCHAR * 4),
                ('Descriptors', SES_ENCLOSURE_DESCRIPTOR * ANYSIZE_ARRAY),
            ]


            class _Union_11(ctypes.Union):
                pass


            class DeviceSlot(ctypes.Structure):
                pass


            DeviceSlot._fields_ = [
                # Byte 1
                ('Reserved1', UCHAR),
                # Byte 2, bit 0
                ('Reserved2', UCHAR, 1),
                # Byte 2, bit 1
                ('RequestIdentify', UCHAR, 1),
                # Byte 2, bit 2
                ('RequestRemove', UCHAR, 1),
                # Byte 2, bit 3
                ('RequestInsert', UCHAR, 1),
                # Byte 2, bit 4
                ('RequestMissing', UCHAR, 1),
                # Byte 2, bit 5
                ('Reserved3', UCHAR, 1),
                # Byte 2, bit 6
                ('DoNotRemove', UCHAR, 1),
                # Byte 2, bit 7
                ('RequestActive', UCHAR, 1),
                # Byte 3, bit 0 - 1
                ('Reserved4', UCHAR, 2),
                # Byte 3, bit 2
                ('EnableBypassB', UCHAR, 1),
                # Byte 3, bit 3
                ('EnableBypassA', UCHAR, 1),
                # Byte 3, bit 4
                ('DeviceOff', UCHAR, 1),
                # Byte 3, bit 5
                ('RequestFault', UCHAR, 1),
                # Byte 3, bit 6 - 7
                ('Reserved5', UCHAR, 2),
            ]
            _Union_11.DeviceSlot = DeviceSlot


            class PowerSupply(ctypes.Structure):
                pass


            PowerSupply._fields_ = [
                # Byte 1, bit 0 - 6
                ('Reserved1', UCHAR, 7),
                # Byte 1, bit 7
                ('RequestIdentify', UCHAR, 1),
                # Byte 2
                ('Reserved2', UCHAR),
                # Byte 3, bit 0 - 4
                ('Reserved3', UCHAR, 5),
                # Byte 3, bit 5
                ('RequestOn', UCHAR, 1),
                # Byte 3, bit 6
                ('RequestFail', UCHAR, 1),
                # Byte 3, bit 7
                ('Reserved4', UCHAR, 1),
            ]
            _Union_11.PowerSupply = PowerSupply


            class Cooling(ctypes.Structure):
                pass


            Cooling._fields_ = [
                # Byte 1, bit 0 - 6
                ('Reserved1', UCHAR, 7),
                # Byte 1, bit 7
                ('RequestIdentify', UCHAR, 1),
                # Byte 2
                ('Reserved2', UCHAR),
                # Byte 3, bit 0 - 2
                ('RequestSpeedCode', UCHAR, 3),
                # Byte 3, bit 3 - 4
                ('Reserved3', UCHAR, 2),
                # Byte 3, bit 5
                ('RequestOn', UCHAR, 1),
                # Byte 3, bit 6
                ('RequestFail', UCHAR, 1),
                # Byte 3, bit 7
                ('Reserved4', UCHAR, 1),
            ]
            _Union_11.Cooling = Cooling


            class TemperatureSensor(ctypes.Structure):
                pass


            TemperatureSensor._fields_ = [
                # Byte 1, bit 0 - 5
                ('Reserved1', UCHAR, 6),
                # Byte 1, bit 6
                ('RequestFail', UCHAR, 1),
                # Byte 1, bit 7
                ('RequestIdentify', UCHAR, 1),
                # Byte 2
                ('Reserved2', UCHAR),
                # Byte 3
                ('Reserved3', UCHAR),
            ]
            _Union_11.TemperatureSensor = TemperatureSensor


            class VoltageSensor(ctypes.Structure):
                pass


            VoltageSensor._fields_ = [
                # Byte 1, bit 0 - 5
                ('Reserved1', UCHAR, 6),
                # Byte 1, bit 6
                ('RequestFail', UCHAR, 1),
                # Byte 1, bit 7
                ('RequestIdentify', UCHAR, 1),
                # Byte 2
                ('Reserved2', UCHAR),
                # Byte 3
                ('Reserved3', UCHAR),
            ]
            _Union_11.VoltageSensor = VoltageSensor


            class CurrentSensor(ctypes.Structure):
                pass


            CurrentSensor._fields_ = [
                # Byte 1, bit 0 - 5
                ('Reserved1', UCHAR, 6),
                # Byte 1, bit 6
                ('RequestFail', UCHAR, 1),
                # Byte 1, bit 7
                ('RequestIdentify', UCHAR, 1),
                # Byte 2
                ('Reserved2', UCHAR),
                # Byte 3
                ('Reserved3', UCHAR),
            ]
            _Union_11.CurrentSensor = CurrentSensor


            class Enclosure(ctypes.Structure):
                pass


            Enclosure._fields_ = [
                # Byte 1, bit 0 - 6
                ('Reserved1', UCHAR, 7),
                # Byte 1, bit 7
                ('RequestIdentify', UCHAR, 1),
                # Byte 2, bit 0 - 5
                ('PowerCycleDelay', UCHAR, 6),
                # Byte 2, bit 6 - 7
                ('PowerCycleRequest', UCHAR, 2),
                # Byte 3, bit 0
                ('RequestWarning', UCHAR, 1),
                # Byte 3, bit 1
                ('RequestFailure', UCHAR, 1),
                # Byte 3, bit 2 - 7
                ('PowerOffDuration', UCHAR, 6),
            ]
            _Union_11.Enclosure = Enclosure


            class ArrayDeviceSlot(ctypes.Structure):
                pass


            ArrayDeviceSlot._fields_ = [
                # Byte 1, bit 0
                ('RequestRebuildAbort', UCHAR, 1),
                # Byte 1, bit 1
                ('RequestRebuild', UCHAR, 1),
                # Byte 1, bit 2
                ('RequestInFailedArray', UCHAR, 1),
                # Byte 1, bit 3
                ('RequestInCriticalArray', UCHAR, 1),
                # Byte 1, bit 4
                ('RequestConsistencyArray', UCHAR, 1),
                # Byte 1, bit 5
                ('RequestHotSpare', UCHAR, 1),
                # Byte 1, bit 6
                ('RequestReservedDevice', UCHAR, 1),
                # Byte 1, bit 7
                ('RequestOK', UCHAR, 1),
                # Byte 2, bit 0
                ('Reserved1', UCHAR, 1),
                # Byte 2, bit 1
                ('RequestIdentify', UCHAR, 1),
                # Byte 2, bit 2
                ('RequestRemove', UCHAR, 1),
                # Byte 2, bit 3
                ('RequestInsert', UCHAR, 1),
                # Byte 2, bit 4
                ('RequestMissing', UCHAR, 1),
                # Byte 2, bit 5
                ('Reserved2', UCHAR, 1),
                # Byte 2, bit 6
                ('DoNotRemove', UCHAR, 1),
                # Byte 2, bit 7
                ('RequestActive', UCHAR, 1),
                # Byte 3, bit 0 - 1
                ('Reserved3', UCHAR, 2),
                # Byte 3, bit 2
                ('EnableBypassB', UCHAR, 1),
                # Byte 3, bit 3
                ('EnableBypassA', UCHAR, 1),
                # Byte 3, bit 4
                ('DeviceOff', UCHAR, 1),
                # Byte 3, bit 5
                ('RequestFault', UCHAR, 1),
                # Byte 3, bit 6 - 7
                ('Reserved4', UCHAR, 2),
            ]
            _Union_11.ArrayDeviceSlot = ArrayDeviceSlot


            _Union_11._fields_ = [
                ('DeviceSlot', _Union_11.DeviceSlot),
                ('PowerSupply', _Union_11.PowerSupply),
                ('Cooling', _Union_11.Cooling),
                ('TemperatureSensor', _Union_11.TemperatureSensor),
                ('VoltageSensor', _Union_11.VoltageSensor),
                ('CurrentSensor', _Union_11.CurrentSensor),
                ('Enclosure', _Union_11.Enclosure),
                ('ArrayDeviceSlot', _Union_11.ArrayDeviceSlot),
            ]
            _SES_CONTROL_DESCRIPTOR._Union_11 = _Union_11

            _SES_CONTROL_DESCRIPTOR._anonymous_ = (
                '_Union_11',
            )

            _SES_CONTROL_DESCRIPTOR._fields_ = [
                # Byte 0, bit 0 - 3
                ('Reserved', UCHAR, 4),
                # Byte 0, bit 4
                ('ResetSwap', UCHAR, 1),
                # Byte 0, bit 5
                ('Disable', UCHAR, 1),
                # Byte 0, bit 6
                ('PredictFailure', UCHAR, 1),
                # Byte 0, bit 7
                ('Select', UCHAR, 1),
                ('_Union_11', _SES_CONTROL_DESCRIPTOR._Union_11),
            ]

            _SES_CONTROL_DIAGNOSTIC_PAGE._fields_ = [
                # Byte 0
                ('PageCode', UCHAR),
                # Byte 1, bit 0
                ('Unrecoverable', UCHAR, 1),
                # Byte 1, bit 1
                ('Critical', UCHAR, 1),
                # Byte 1, bit 2
                ('NonCritical', UCHAR, 1),
                # Byte 1, bit 3
                ('Informational', UCHAR, 1),
                # Byte 1, bit 4 - 7
                ('Reserved', UCHAR, 4),
                # Bytes 2 - 3
                ('PageLength', UCHAR * 2),
                # Bytes 4 - 7
                ('ExpectedGenerationCode', UCHAR * 4),
                ('Descriptors', SES_CONTROL_DESCRIPTOR * ANYSIZE_ARRAY),
            ]


            class _Union_12(ctypes.Union):
                pass


            class DeviceSlot(ctypes.Structure):
                pass


            DeviceSlot._fields_ = [
                # Byte 1
                ('SlotAddress', UCHAR),
                # Byte 2, bit 0
                ('Report', UCHAR, 1),
                # Byte 2, bit 1
                ('Identify', UCHAR, 1),
                # Byte 2, bit 2
                ('Remove', UCHAR, 1),
                # Byte 2, bit 3
                ('ReadyToInsert', UCHAR, 1),
                # Byte 2, bit 4
                ('EnclosureBypassedB', UCHAR, 1),
                # Byte 2, bit 5
                ('EnclosureBypassedA', UCHAR, 1),
                # Byte 2, bit 6
                ('DoNotRemove', UCHAR, 1),
                # Byte 2, bit 7
                ('AppBypassedA', UCHAR, 1),
                # Byte 3, bit 0
                ('DeviceBypassedB', UCHAR, 1),
                # Byte 3, bit 1
                ('DeviceBypassedA', UCHAR, 1),
                # Byte 3, bit 2
                ('BypassedB', UCHAR, 1),
                # Byte 3, bit 3
                ('BypassedA', UCHAR, 1),
                # Byte 3, bit 4
                ('DeviceOff', UCHAR, 1),
                # Byte 3, bit 5
                ('FaultRequested', UCHAR, 1),
                # Byte 3, bit 6
                ('FaultSensed', UCHAR, 1),
                # Byte 3, bit 7
                ('AppBypassedB', UCHAR, 1),
            ]
            _Union_12.DeviceSlot = DeviceSlot


            class PowerSupply(ctypes.Structure):
                pass


            PowerSupply._fields_ = [
                # Byte 1, bit 0 - 6
                ('Reserved1', UCHAR, 7),
                # Byte 1, bit 7
                ('Identify', UCHAR, 1),
                # Byte 2, bit 0
                ('Reserved2', UCHAR, 1),
                # Byte 2, bit 1
                ('DCOverCurrent', UCHAR, 1),
                # Byte 2, bit 2
                ('DCUnderVoltage', UCHAR, 1),
                # Byte 2, bit 3
                ('DCOverVoltage', UCHAR, 1),
                # Byte 2, bit 4 - 7
                ('Reserved3', UCHAR, 4),
                # Byte 3, bit 0
                ('DCFail', UCHAR, 1),
                # Byte 3, bit 1
                ('ACFail', UCHAR, 1),
                # Byte 3, bit 2
                ('TemperatureWarning', UCHAR, 1),
                # Byte 3, bit 3
                ('OverTemperatureFail', UCHAR, 1),
                # Byte 3, bit 4
                ('Off', UCHAR, 1),
                # Byte 3, bit 5
                ('RequestedOn', UCHAR, 1),
                # Byte 3, bit 6
                ('Fail', UCHAR, 1),
                # Byte 3, bit 7
                ('HotSwap', UCHAR, 1),
            ]
            _Union_12.PowerSupply = PowerSupply


            class Cooling(ctypes.Structure):
                pass


            Cooling._fields_ = [
                # Byte 1, bit 0 - 2
                ('ActualFanSpeedMSB', UCHAR, 3),
                # Byte 1, bit 3 - 6
                ('Reserved1', UCHAR, 4),
                # Byte 1, bit 7
                ('Identify', UCHAR, 1),
                # Byte 2
                ('ActualFanSpeedLSB', UCHAR),
                # Byte 3, bit 0 - 2
                ('ActualSpeedCode', UCHAR, 3),
                # Byte 3, bit 3
                ('Reserved2', UCHAR, 1),
                # Byte 3, bit 4
                ('Off', UCHAR, 1),
                # Byte 3, bit 5
                ('RequestedOn', UCHAR, 1),
                # Byte 3, bit 6
                ('Fail', UCHAR, 1),
                # Byte 3, bit 7
                ('HotSwap', UCHAR, 1),
            ]
            _Union_12.Cooling = Cooling


            class TemperatureSensor(ctypes.Structure):
                pass


            TemperatureSensor._fields_ = [
                # Byte 1, bit 0 - 5
                ('Reserved1', UCHAR, 6),
                # Byte 1, bit 6
                ('Fail', UCHAR, 1),
                # Byte 1, bit 7
                ('Identify', UCHAR, 1),
                # Byte 2
                ('Temperature', UCHAR),
                # Byte 3, bit 0
                ('UnderTemperatureWarning', UCHAR, 1),
                # Byte 3, bit 1
                ('UnderTemperatureFailure', UCHAR, 1),
                # Byte 3, bit 2
                ('OverTemperatureWarning', UCHAR, 1),
                # Byte 3, bit 3
                ('OverTemperatureFailure', UCHAR, 1),
                # Byte 3, bit 4 - 7
                ('Reserved2', UCHAR, 4),
            ]
            _Union_12.TemperatureSensor = TemperatureSensor


            class VoltageSensor(ctypes.Structure):
                pass


            VoltageSensor._fields_ = [
                # Byte 1, bit 0
                ('CritUnder', UCHAR, 1),
                # Byte 1, bit 1
                ('CritOver', UCHAR, 1),
                # Byte 1, bit 2
                ('WarnUnder', UCHAR, 1),
                # Byte 1, bit 3
                ('WarnOver', UCHAR, 1),
                # Byte 1, bit 4 - 5
                ('Reserved1', UCHAR, 2),
                # Byte 1, bit 6
                ('Fail', UCHAR, 1),
                # Byte 1, bit 7
                ('Identify', UCHAR, 1),
                # Byte 2
                ('VoltageMSB', UCHAR),
                # Byte 3
                ('VoltageLSB', UCHAR),
            ]
            _Union_12.VoltageSensor = VoltageSensor


            class CurrentSensor(ctypes.Structure):
                pass


            CurrentSensor._fields_ = [
                # Byte 1, bit 0
                ('Reserved1', UCHAR, 1),
                # Byte 1, bit 1
                ('CritOver', UCHAR, 1),
                # Byte 1, bit 2
                ('Reserved2', UCHAR, 1),
                # Byte 1, bit 3
                ('WarnOver', UCHAR, 1),
                # Byte 1, bit 4 - 5
                ('Reserved3', UCHAR, 2),
                # Byte 1, bit 6
                ('Fail', UCHAR, 1),
                # Byte 1, bit 7
                ('Identify', UCHAR, 1),
                # Byte 2
                ('CurrentMSB', UCHAR),
                # Byte 3
                ('CurrentLSB', UCHAR),
            ]
            _Union_12.CurrentSensor = CurrentSensor


            class Enclosure(ctypes.Structure):
                pass


            Enclosure._fields_ = [
                # Byte 1, bit 0 - 6
                ('Reserved1', UCHAR, 7),
                # Byte 1, bit 7
                ('Identify', UCHAR, 1),
                # Byte 2, bit 0
                ('WarningIndication', UCHAR, 1),
                # Byte 2, bit 1
                ('FailureIndication', UCHAR, 1),
                # Byte 2, bit 6
                ('TimeUntilPowerCycle', UCHAR, 6),
                # Byte 3, bit 0
                ('WarningRequested', UCHAR, 1),
                # Byte 3, bit 1
                ('FailureRequested', UCHAR, 1),
                # Byte 3, bit 6
                ('RequestedPowerOffTime', UCHAR, 6),
            ]
            _Union_12.Enclosure = Enclosure


            class ArrayDeviceSlot(ctypes.Structure):
                pass


            ArrayDeviceSlot._fields_ = [
                # Byte 1, bit 0
                ('RebuildAbort', UCHAR, 1),
                # Byte 1, bit 1
                ('Rebuild', UCHAR, 1),
                # Byte 1, bit 2
                ('InFailedArray', UCHAR, 1),
                # Byte 1, bit 3
                ('InCriticalArray', UCHAR, 1),
                # Byte 1, bit 4
                ('ConsistencyCheck', UCHAR, 1),
                # Byte 1, bit 5
                ('HotSpare', UCHAR, 1),
                # Byte 1, bit 6
                ('ReservedDevice', UCHAR, 1),
                # Byte 1, bit 7
                ('OK', UCHAR, 1),
                # Byte 2, bit 0
                ('Report', UCHAR, 1),
                # Byte 2, bit 1
                ('Identify', UCHAR, 1),
                # Byte 2, bit 2
                ('Remove', UCHAR, 1),
                # Byte 2, bit 3
                ('ReadyToInsert', UCHAR, 1),
                # Byte 2, bit 4
                ('EnclosureBypassedB', UCHAR, 1),
                # Byte 2, bit 5
                ('EnclosureBypassedA', UCHAR, 1),
                # Byte 2, bit 6
                ('DoNotRemove', UCHAR, 1),
                # Byte 2, bit 7
                ('AppBypassedA', UCHAR, 1),
                # Byte 3, bit 0
                ('DeviceBypassedB', UCHAR, 1),
                # Byte 3, bit 1
                ('DeviceBypassedA', UCHAR, 1),
                # Byte 3, bit 2
                ('BypassedB', UCHAR, 1),
                # Byte 3, bit 3
                ('BypassedA', UCHAR, 1),
                # Byte 3, bit 4
                ('DeviceOff', UCHAR, 1),
                # Byte 3, bit 5
                ('FaultRequested', UCHAR, 1),
                # Byte 3, bit 6
                ('FaultSensed', UCHAR, 1),
                # Byte 3, bit 7
                ('AppBypassedB', UCHAR, 1),
            ]
            _Union_12.ArrayDeviceSlot = ArrayDeviceSlot


            _Union_12._fields_ = [
                ('DeviceSlot', _Union_12.DeviceSlot),
                ('PowerSupply', _Union_12.PowerSupply),
                ('Cooling', _Union_12.Cooling),
                ('TemperatureSensor', _Union_12.TemperatureSensor),
                ('VoltageSensor', _Union_12.VoltageSensor),
                ('CurrentSensor', _Union_12.CurrentSensor),
                ('Enclosure', _Union_12.Enclosure),
                ('ArrayDeviceSlot', _Union_12.ArrayDeviceSlot),
            ]
            _SES_STATUS_DESCRIPTOR._Union_12 = _Union_12

            _SES_STATUS_DESCRIPTOR._anonymous_ = (
                '_Union_12',
            )

            _SES_STATUS_DESCRIPTOR._fields_ = [
                # Byte 0, bit 0 - 3
                ('ElementStatus', UCHAR, 4),
                # Byte 0, bit 4
                ('Swap', UCHAR, 1),
                # Byte 0, bit 5
                ('Disabled', UCHAR, 1),
                # Byte 0, bit 6
                ('PredictedFailure', UCHAR, 1),
                # Byte 0, bit 7
                ('Reserved1', UCHAR, 1),
                ('_Union_12', _SES_STATUS_DESCRIPTOR._Union_12),
            ]

            _SES_STATUS_DIAGNOSTIC_PAGE._fields_ = [
                # Byte 0
                ('PageCode', UCHAR),
                # Byte 1, bit 0
                ('Unrecoverable', UCHAR, 1),
                # Byte 1, bit 1
                ('Critical', UCHAR, 1),
                # Byte 1, bit 2
                ('NonCritical', UCHAR, 1),
                # Byte 1, bit 3
                ('Informational', UCHAR, 1),
                # Byte 1, bit 4
                ('InvalidOperation', UCHAR, 1),
                # Byte 1, bit 5 - 7
                ('Reserved', UCHAR, 3),
                # Bytes 2 - 3
                ('PageLength', UCHAR * 2),
                # Bytes 4 - 7
                ('GenerationCode', UCHAR * 4),
                ('Descriptors', SES_STATUS_DESCRIPTOR * ANYSIZE_ARRAY),
            ]

            _SES_PHY_DESCRIPTOR._fields_ = [
                # Byte 0, bit 0 - 3
                ('Reserved1', UCHAR, 4),
                # Byte 0, bit 4 - 6
                ('DeviceType', UCHAR, 3),
                # Byte 0, bit 7
                ('Reserved3', UCHAR, 1),
                # Byte 1
                ('Reserved4', UCHAR),
                # Byte 2, bit 0
                ('Reserved5', UCHAR, 1),
                # Byte 2, bit 1
                ('SmpInitiatorPort', UCHAR, 1),
                # Byte 2, bit 2
                ('StpInitiatorPort', UCHAR, 1),
                # Byte 2, bit 3
                ('SspInitiatorPort', UCHAR, 1),
                # Byte 2, bit 4 - 7
                ('Reserved6', UCHAR, 4),
                # Byte 3, bit 0
                ('SataDevice', UCHAR, 1),
                # Byte 3, bit 1
                ('SmpTargetPort', UCHAR, 1),
                # Byte 3, bit 2
                ('StpTargetPort', UCHAR, 1),
                # Byte 3, bit 3
                ('SspTargetPort', UCHAR, 1),
                # Byte 3, bit 4 - 6
                ('Reserved7', UCHAR, 3),
                # Byte 3, bit 7
                ('SataPortSelector', UCHAR, 1),
                # Bytes 4 - 11
                ('AttachedSASAddress', UCHAR * 8),
                # Bytes 12 - 19
                ('SASAddress', UCHAR * 8),
                # Byte 20
                ('PhyIdentifier', UCHAR),
                # Bytes 21 - 27
                ('Reserved2', UCHAR * 7),
            ]

            _SES_SAS_SLOT_INFORMATION._fields_ = [
                # Byte 0
                ('NumberOfPhyDescriptors', UCHAR),
                # Byte 1, bit 0
                ('NotAllPhys', UCHAR, 1),
                # Byte 1, bit 1 - 5
                ('Reserved1', UCHAR, 5),
                # Byte 1, bit 6 - 7
                ('Type', UCHAR, 2),
                # Byte 2
                ('Reserved2', UCHAR),
                # Byte 3
                ('DeviceSlotNumber', UCHAR),
                ('PhyDescriptors', SES_PHY_DESCRIPTOR * ANYSIZE_ARRAY),
            ]

            _SES_PROTOCOL_INFORMATION._fields_ = [
                # as needed
                ('SasSlot', SES_SAS_SLOT_INFORMATION),
            ]

            _SES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR._fields_ = [
                # Byte 0, bit 0 - 3
                ('ProtocolIdentifier', UCHAR, 4),
                # Byte 0, bit 4
                ('EIP', UCHAR, 1),
                # Byte 0, bit 5 - 6
                ('Reserved1', UCHAR, 2),
                # Byte 0, bit 7
                ('Invalid', UCHAR, 1),
                # Byte 1
                ('Length', UCHAR),
                # Byte 2
                ('Reserved2', UCHAR),
                # Byte 3
                ('ElementIndex', UCHAR),
                ('ProtocolInfo', SES_PROTOCOL_INFORMATION),
            ]

            _SES_ADDITIONAL_ELEMENT_STATUS_DIAGNOSTIC_PAGE._fields_ = [
                # Byte 0
                ('PageCode', UCHAR),
                # Byte 1
                ('Reserved', UCHAR),
                # Bytes 2 - 3
                ('PageLength', UCHAR * 2),
                # Bytes 4 - 7
                ('GenerationCode', UCHAR * 4),
                ('Descriptors', SES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR * ANYSIZE_ARRAY),
            ]

            _SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR._fields_ = [
                # Byte 0
                ('Reserved1', UCHAR),
                # Byte 1
                ('SubEnclosureId', UCHAR),
                # Byte 2
                ('Status', UCHAR),
                # Byte 3
                ('AdditionalStatus', UCHAR),
                # Bytes 4 - 7
                ('MaximumImageSize', UCHAR * 4),
                # Bytes 8 - 10
                ('Reserved2', UCHAR * 3),
                # Byte 11
                ('ExpectedBufferId', UCHAR),
                # Bytes 12 - 15
                ('ExpectedBufferOffset', UCHAR),
            ]

            _SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE._fields_ = [
                # Byte 0
                ('PageCode', UCHAR),
                # Byte 1
                ('NumberOfSecondarySubEnclosures', UCHAR),
                # Bytes 2 - 3
                ('PageLength', UCHAR * 2),
                # Bytes 4 - 7
                ('GenerationCode', UCHAR * 4),
                ('Descriptors', SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR * ANYSIZE_ARRAY),
            ]

            _SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE._fields_ = [
                # Byte 0
                ('PageCode', UCHAR),
                # Byte 1
                ('SubEnclosureId', UCHAR),
                # Bytes 2 - 3
                ('PageLength', UCHAR * 2),
                # Bytes 4 - 7
                ('ExpectedGenerationCode', UCHAR * 4),
                # Byte 8
                ('Mode', UCHAR),
                # Bytes 9 - 10
                ('Reserved', UCHAR * 2),
                # Byte 11
                ('BufferID', UCHAR),
                # Bytes 12 - 15
                ('BufferOffset', UCHAR * 4),
                # Bytes 16 - 19
                ('ImageLength', UCHAR * 4),
                # Bytes 20 - 23
                ('DataLength', UCHAR * 4),
                ('Data', UCHAR * ANYSIZE_ARRAY),
            ]
        # END IF
        # Definitions related to 0x9E - SCSIOP_GET_PHYSICAL_ELEMENT_STATUS
        # Input: Report type
        GET_PHYSICAL_ELEMENT_STATUS_REPORT_TYPE_PHYSICAL_ELEMENT = 0x0
        GET_PHYSICAL_ELEMENT_STATUS_REPORT_TYPE_STORAGE_ELEMENT = 0x1


        # Input: Filter
        GET_PHYSICAL_ELEMENT_STATUS_ALL = 0x0
        GET_PHYSICAL_ELEMENT_STATUS_FILTER_NEED_ATTENTION = 0x1


        # Output: Physical element type
        PHYSICAL_ELEMENT_TYPE_STORAGE_ELEMENT = 0x01


        # Output: Physical element health
        PHYSICAL_ELEMENT_HEALTH_NOT_REPORTED = 0x00
        PHYSICAL_ELEMENT_HEALTH_MANUFACTURER_SPECIFICATION_LIMIT = 0x64
        PHYSICAL_ELEMENT_HEALTH_RESERVED_LOWER_BOUNDARY = 0xD0
        PHYSICAL_ELEMENT_HEALTH_RESERVED_UPPER_BOUNDARY = 0xFC
        PHYSICAL_ELEMENT_HEALTH_DEPOPULATION_COMPLETED_WITH_ERROR = 0xFD
        PHYSICAL_ELEMENT_HEALTH_DEPOPULATION_IN_PROGRESS = 0xFE
        PHYSICAL_ELEMENT_HEALTH_DEPOPULATION_COMPLETED_SUCCESS = 0xFF


        _PHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR._fields_ = [
            ('Reserved1', UCHAR * 4),
            ('ElementIdentifier', UCHAR * 4),
            ('Reserved2', UCHAR * 6),
            ('PhysicalElementType', UCHAR),
            ('PhysicalElementHealth', UCHAR),
            ('AssociatedCapacity', UCHAR * 8),
            ('Reserved3', UCHAR * 8),
        ]

        _PHYSICAL_ELEMENT_STATUS_PARAMETER_DATA._fields_ = [
            ('DescriptorCount', UCHAR * 4),
            ('ReturnedDescriptorCount', UCHAR * 4),
            ('ElementIdentifierBeingDepoped', UCHAR * 4),
            ('Reserved', UCHAR * 20),
            ('Descriptors', PHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR * ANYSIZE_ARRAY),
        ]


        # Definitions related to 0x3C -
        # SCSIOP_READ_DATA_BUFF(Mode 0x1C: Error History)
        # Input: Mode field for Read buffer command
        READ_BUFFER_MODE_ERROR_HISTORY = 0x1C


        # Input: Mode specific field for Read buffer command
        MODE_SPECIFIC_CREATE_VENDOR_SPECIFIC_DATA = 0x0
        MODE_SPECIFIC_CREATE_CURRENT_INTERNAL_STATUS_DATA = 0x1


        # Input: Buffer ID field for Read buffer command
        # Return error history directory.
        BUFFER_ID_RETURN_ERROR_HISTORY_DIRECTORY = 0x0


        # Return error history directory and create new error history snapshot.
        BUFFER_ID_RETURN_ERROR_HISTORY_DIRECTORY_CREATE_NEW_ERROR_HISTORY_SNAPSHOT = (
            0x1
        )


        # Return error history directory and establish new error history I_T
        # nexus.
        BUFFER_ID_RETURN_ERROR_HISTORY_DIRECTORY_ESTABLISH_NEW_NEXUS = 0x2


        # Return error history directory, establish new error history I_T
        # nexus,
        # and create new error history snapshot.
        BUFFER_ID_RETURN_ERROR_HISTORY_DIRECTORY_ESTABLISH_NEW_NEXUS_AND_SNAPSHOT = (
            0x3
        )


        # 0x04h - 0x0Fh Reserved.
        # 0x10h - 0xEFh Return error history.
        BUFFER_ID_RETURN_ERROR_HISTORY_MINIMUM_THRESHOLD = 0x10
        BUFFER_ID_RETURN_ERROR_HISTORY_MAXIMUM_THRESHOLD = 0xEF


        # 0xF0h - 0xFDh Reserved.
        # Clear error history I_T nexus.
        BUFFER_ID_CLEAR_ERROR_HISTORY_NEXUS = 0xFE


        # Clear error history I_T nexus and release any error history
        # snapshots.
        BUFFER_ID_CLEAR_ERROR_HISTORY_AND_RELEASE_ANY_SNAPSHOT = 0xFF


        # Output: Error history source field
        ERROR_HISTORY_SOURCE_CREATED_BY_DEVICE_SERVER = 0x0
        ERROR_HISTORY_SOURCE_CREATED_DUE_TO_CURRENT_READ_BUFFER_COMMAND = 0x1
        ERROR_HISTORY_SOURCE_CREATED_DUE_TO_PREVIOUS_READ_BUFFER_COMMAND = 0x2
        ERROR_HISTORY_SOURCE_INDICATED_IN_BUFFER_SOURCE_FIELD = 0x3


        # Output: Error history retrieved field
        ERROR_HISTORY_RETRIEVED_NO_INFORMATION = 0x0


        # The error history I_T nexus has requested buffer ID FEh
        # (i.e., clear error history I_T nexus) or buffer ID FFh
        # (i.e., clear error history I_T nexus and release snapshot) for the
        # current error history snapshot.
        ERROR_HISTORY_RETRIEVED_BUFFER_ID_FE_OR_FF = 0x1


        # An error history I_T nexus has not requested buffer ID FEh
        # (i.e., clear error history I_T nexus) or buffer ID FFh
        # (i.e., clear error history I_T nexus and release snapshot) for the
        # current error history snapshot.
        ERROR_HISTORY_RETRIEVED_NOT_BUFFER_ID_FE_OR_FF = 0x2
        ERROR_HISTORY_RETRIEVED_RESERVED = 0x3


        # Output: Buffer format
        BUFFER_FORMAT_VENDOR_SPECIFIC = 0x0
        BUFFER_FORMAT_CURRENT_INTERNAL_STATUS_DATA = 0x1
        BUFFER_FORMAT_SAVED_INTERNAL_STATUS_DATA = 0x2


        # Output: Buffer source
        BUFFER_SOURCE_INDICATED_IN_EHS_SOURCE_FIELD = 0x0
        BUFFER_SOURCE_UNKNOWN = 0x1
        BUFFER_SOURCE_CREATED_BY_DEVICE_SERVER = 0x2
        BUFFER_SOURCE_CREATED_DUE_TO_CURRENT_COMMAND = 0x3
        BUFFER_SOURCE_CREATED_DUE_TO_PREVIOUS_COMMAND = 0x4
        STATUS_DATA_SET_SIZE_INCREMENT_IN_BYTES = 0x200


        _ERROR_HISTORY_DIRECTORY_ENTRY._fields_ = [
            ('SupportedBufferId', UCHAR),
            ('BufferFormat', UCHAR),
            ('BufferSource', UCHAR, 4),
            ('Reserved0', UCHAR, 4),
            ('Reserved1', UCHAR),
            ('MaxAvailableLength', UCHAR * 4),
        ]

        _ERROR_HISTORY_DIRECTORY._fields_ = [
            ('T10VendorId', UCHAR * 8),
            ('ErrorHistoryVersion', UCHAR),
            ('ClearSupport', UCHAR, 1),
            ('ErrorHistorySource', UCHAR, 2),
            ('ErrorHistoryRetrieved', UCHAR, 2),
            ('Reserved0', UCHAR, 3),
            ('Reserved1', UCHAR * 20),
            ('DirectoryLength', UCHAR * 2),
            ('ErrorHistoryDirectoryList', ERROR_HISTORY_DIRECTORY_ENTRY * ANYSIZE_ARRAY),
        ]

        _CURRENT_INTERNAL_STATUS_PARAMETER_DATA._fields_ = [
            ('Reserved0', UCHAR * 4),
            ('IEEECompanyId', UCHAR * 4),
            ('CurrentInternalStatusDataSetOneLength', UCHAR * 2),
            ('CurrentInternalStatusDataSetTwoLength', UCHAR * 2),
            ('CurrentInternalStatusDataSetThreeLength', UCHAR * 2),
            ('CurrentInternalStatusDataSetFourLength', UCHAR * 4),
            ('Reserved1', UCHAR * 364),
            ('NewSavedDataAvailable', UCHAR),
            ('SavedDataGenerationNumber', UCHAR),
            ('CurrentReasonIdentifier', UCHAR * 128),
            ('CurrentInternalStatusData', UCHAR * ANYSIZE_ARRAY),
        ]

        _SAVED_INTERNAL_STATUS_PARAMETER_DATA._fields_ = [
            ('Reserved0', UCHAR * 4),
            ('IEEECompanyId', UCHAR * 4),
            ('SavedInternalStatusDataSetOneLength', UCHAR * 2),
            ('SavedInternalStatusDataSetTwoLength', UCHAR * 2),
            ('SavedInternalStatusDataSetThreeLength', UCHAR * 2),
            ('SavedInternalStatusDataSetFourLength', UCHAR * 4),
            ('Reserved1', UCHAR * 364),
            ('NewSavedDataAvailable', UCHAR),
            ('SavedDataGenerationNumber', UCHAR),
            ('SavedReasonIdentifier', UCHAR * 128),
            ('SavedInternalStatusData', UCHAR * ANYSIZE_ARRAY),
        ]


        # Collections of SCSI utility functions
        # SCSI sense data related functions
        # NOTE: Sense Data Descriptor Format is supported only in Windows 8
        # and later
        # Obtain Error Code from the sense info buffer.
        # Note: Error Code is same as "Response Code" defined in SPC
        # Specification.
        def ScsiGetSenseErrorCode(SenseInfoBuffer):
            return PUCHAR(SenseInfoBuffer)[0].value & 0x7F


        # Determine the buffer length of a descriptor
        def ScsiGetSenseDescriptorLength(DescriptorBuffer):
            return (
                ctypes.sizeof(SCSI_SENSE_DESCRIPTOR_HEADER) +
                PSCSI_SENSE_DESCRIPTOR_HEADER(
                    DescriptorBuffer).AdditionalLength
            )


        # Determine if sense data is in Fixed format
        def IsFixedSenseDataFormat(SenseInfoBuffer):
            return (
                ScsiGetSenseErrorCode(SenseInfoBuffer) in
                (
                    SCSI_SENSE_ERRORCODE_FIXED_CURRENT,
                    SCSI_SENSE_ERRORCODE_FIXED_DEFERRED
                )
            )


        # Determine if sense data is in Descriptor format
        def IsDescriptorSenseDataFormat(SenseInfoBuffer):
            return (
                ScsiGetSenseErrorCode(SenseInfoBuffer) in
                (
                    SCSI_SENSE_ERRORCODE_DESCRIPTOR_CURRENT,
                    SCSI_SENSE_ERRORCODE_DESCRIPTOR_DEFERRED
                )
            )


        # Determine if sense data is Current error type
        def IsSenseDataCurrentError(SenseInfoBuffer):
            return (
                ScsiGetSenseErrorCode(SenseInfoBuffer) in
                (
                    SCSI_SENSE_ERRORCODE_FIXED_CURRENT,
                    SCSI_SENSE_ERRORCODE_DESCRIPTOR_CURRENT
                )
            )


        # Determine if sense data is Deferred error type
        def IsSenseDataDeferredError(SenseInfoBuffer):
            return (
                ScsiGetSenseErrorCode(SenseInfoBuffer) in
                (
                    SCSI_SENSE_ERRORCODE_FIXED_DEFERRED,
                    SCSI_SENSE_ERRORCODE_DESCRIPTOR_DEFERRED
                )
            )


        # Determine if sense data format indicated in sense data payload is a
        # valid value
        def IsSenseDataFormatValueValid(SenseInfoBuffer):
            return (
                IsFixedSenseDataFormat(SenseInfoBuffer) or
                IsDescriptorSenseDataFormat(SenseInfoBuffer)
            )


        # _Success_(return != FALSE)
        # FORCEINLINE BOOLEAN
        # ScsiGetTotalSenseByteCountIndicated (
        # _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
        # _In_  UCHAR SenseInfoBufferLength,
        # _Out_ UCHAR *TotalByteCountIndicated
        # )
        #
        # Description:
        #
        # This function returns size of available sense data. This is based on
        # AdditionalSenseLength field in the sense data payload as indicated
        # by the device.
        #
        # This function handles both Fixed and Desciptor format.
        #
        # Arguments:
        #
        # SenseInfoBuffer
        # - A pointer to sense info buffer
        #
        # SenseInfoBufferLength
        # - Size of the buffer SenseInfoBuffer points to.
        #
        # TotalByteCountIndicated
        # - On output, it contains total byte counts of available sense data
        #
        # Returns:
        #
        # TRUE if the function is able to determine size of available sense data
        #
        # Otherwise, FALSE
        #
        # Note: The routine returns FALSE when available sense data amount is
        # greater than MAX_SENSE_BUFFER_SIZE
        #
        # {
        # BOOLEAN succeed = FALSE;
        # UCHAR byteCount = 0;
        # PFIXED_SENSE_DATA senseInfoBuffer = NULL;
        #
        # if (SenseInfoBuffer == NULL ||
        # SenseInfoBufferLength == 0 ||
        # TotalByteCountIndicated == NULL) {
        #
        # return FALSE;
        # }
        #
        #
        # Offset to AdditionalSenseLength field is same between
        # Fixed and Descriptor format.
        # senseInfoBuffer = (PFIXED_SENSE_DATA)SenseInfoBuffer;
        #
        # if (RTL_CONTAINS_FIELD(senseInfoBuffer,
        # SenseInfoBufferLength,
        # AdditionalSenseLength)) {
        #
        # if (senseInfoBuffer->AdditionalSenseLength <=
        # (MAX_SENSE_BUFFER_SIZE - RTL_SIZEOF_THROUGH_FIELD(FIXED_SENSE_DATA, AdditionalSenseLength))) {
        #
        # byteCount = senseInfoBuffer->AdditionalSenseLength
        # + RTL_SIZEOF_THROUGH_FIELD(FIXED_SENSE_DATA, AdditionalSenseLength);
        #
        # *TotalByteCountIndicated = byteCount;
        #
        # succeed = TRUE;
        # }
        # }
        #
        # return succeed;
        # }
        #
        # _Success_(return != FALSE)
        # FORCEINLINE BOOLEAN
        # ScsiGetFixedSenseKeyAndCodes (
        # _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
        # _In_ UCHAR SenseInfoBufferLength,
        # _Out_opt_ PUCHAR SenseKey,
        # _Out_opt_ PUCHAR AdditionalSenseCode,
        # _Out_opt_ PUCHAR AdditionalSenseCodeQualifier
        # )
        #
        # Description:
        #
        # This function retrieves the following information from sense data
        # in Fixed format:
        #
        # 1. Sense key
        # 2. Additional Sense Code
        # 3. Additional Sense Code Qualifier
        #
        # If Additional Sense Code or Additional Sense Code Qualifer is not available,
        # it is set to 0 when the function returns.
        #
        # Arguments:
        #
        # SenseInfoBuffer
        # - A pointer to sense info buffer
        #
        # SenseInfoBufferLength
        # - Size of the buffer SenseInfoBuffer points to.
        #
        # SenseKey
        # - On output, buffer contains the sense key.
        # If null is specified, the function will not retrieve the sense key
        #
        # AdditionalSenseCode
        # - On output, buffer contains the additional sense code.
        # If null is specified, the function will not retrieve the additional sense code.
        #
        # AdditionalSenseCodeQualifier
        # - On output, buffer contains the additional sense code qualifier.
        # If null is specified, the function will not retrieve the additional sense code qualifier.
        #
        # Returns:
        #
        # TRUE if the function is able to retrieve the requested information.
        #
        # Otherwise, FALSE
        #
        # {
        # PFIXED_SENSE_DATA fixedSenseData = (PFIXED_SENSE_DATA)SenseInfoBuffer;
        # BOOLEAN succeed = FALSE;
        # ULONG dataLength = 0;
        #
        # if (SenseInfoBuffer == NULL || SenseInfoBufferLength == 0) {
        # return FALSE;
        # }
        #
        # if (RTL_CONTAINS_FIELD(fixedSenseData, SenseInfoBufferLength, AdditionalSenseLength)) {
        #
        # dataLength = fixedSenseData->AdditionalSenseLength + RTL_SIZEOF_THROUGH_FIELD(FIXED_SENSE_DATA, AdditionalSenseLength);
        #
        # if (dataLength > SenseInfoBufferLength) {
        # dataLength = SenseInfoBufferLength;
        # }
        #
        # if (SenseKey != NULL) {
        # *SenseKey = fixedSenseData->SenseKey;
        # }
        #
        # if (AdditionalSenseCode != NULL) {
        # *AdditionalSenseCode = RTL_CONTAINS_FIELD(fixedSenseData, dataLength, AdditionalSenseCode) ?
        # fixedSenseData->AdditionalSenseCode : 0;
        # }
        #
        # if (AdditionalSenseCodeQualifier != NULL) {
        # *AdditionalSenseCodeQualifier = RTL_CONTAINS_FIELD(fixedSenseData, dataLength, AdditionalSenseCodeQualifier) ?
        # fixedSenseData->AdditionalSenseCodeQualifier : 0;
        # }
        #
        # succeed = TRUE;
        # }
        #
        # return succeed;
        # }
        #
        # _Success_(return != FALSE)
        # FORCEINLINE BOOLEAN
        # ScsiGetDescriptorSenseKeyAndCodes (
        # _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
        # _In_ UCHAR SenseInfoBufferLength,
        # _Out_opt_ PUCHAR SenseKey,
        # _Out_opt_ PUCHAR AdditionalSenseCode,
        # _Out_opt_ PUCHAR AdditionalSenseCodeQualifier
        # )
        #
        # Description:
        #
        # This function retrieves the following information from sense data
        # in Descriptor format:
        #
        # 1. Sense key
        # 2. Additional Sense Code
        # 3. Additional Sense Code Qualifier
        #
        # Arguments:
        #
        # SenseInfoBuffer
        # - A pointer to sense info buffer
        #
        # SenseInfoBufferLength
        # - Size of the buffer SenseInfoBuffer points to.
        #
        # SenseKey
        # - On output, buffer contains the sense key.
        # Note: If null is specified, the function will not retrieve the sense key
        #
        # AdditionalSenseCode
        # - On output, buffer contains the additional sense code.
        # Note: If null is specified, the function will not retrieve the additional sense code.
        #
        # AdditionalSenseCodeQualifier
        # - On output, buffer contains the additional sense code qualifier.
        # Note: If null is specified, the function will not retrieve the additional sense code qualifier.
        #
        # Returns:
        #
        # TRUE if the function is able to retrieve the requested information.
        #
        # Otherwise, FALSE
        #
        # {
        # PDESCRIPTOR_SENSE_DATA descriptorSenseData = (PDESCRIPTOR_SENSE_DATA)SenseInfoBuffer;
        # BOOLEAN succeed = FALSE;
        #
        # if (SenseInfoBuffer == NULL || SenseInfoBufferLength == 0) {
        # return FALSE;
        # }
        # if (RTL_CONTAINS_FIELD(descriptorSenseData, SenseInfoBufferLength, AdditionalSenseLength)) {
        #
        # if (SenseKey) {
        # *SenseKey = descriptorSenseData->SenseKey;
        # }
        #
        # if (AdditionalSenseCode != NULL) {
        # *AdditionalSenseCode = descriptorSenseData->AdditionalSenseCode;
        # }
        #
        # if (AdditionalSenseCodeQualifier != NULL) {
        # *AdditionalSenseCodeQualifier = descriptorSenseData->AdditionalSenseCodeQualifier;
        # }
        #
        # succeed = TRUE;
        # }
        #
        # return succeed;
        # }
        #
        # SCSI_SENSE_OPTIONS
        #
        SCSI_SENSE_OPTIONS = ULONG
        #
        # No options is specified
        SCSI_SENSE_OPTIONS_NONE = 0x00000000
        #
        # If no known format is indicated in the sense buffer, interpret
        # the sense buffer as Fixed format.
        SCSI_SENSE_OPTIONS_FIXED_FORMAT_IF_UNKNOWN_FORMAT_INDICATED = (
            0x00000001
        )
        #
        # _Success_(return != FALSE)
        # FORCEINLINE BOOLEAN
        # ScsiGetSenseKeyAndCodes (
        # _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
        # _In_ UCHAR SenseInfoBufferLength,
        # _In_ SCSI_SENSE_OPTIONS Options,
        # _Out_opt_ PUCHAR SenseKey,
        # _Out_opt_ PUCHAR AdditionalSenseCode,
        # _Out_opt_ PUCHAR AdditionalSenseCodeQualifier
        # )
        #
        # Description:
        #
        # This function retrieves the following information from sense data
        #
        # 1. Sense key
        # 2. Additional Sense Code
        # 3. Additional Sense Code Qualifier
        #
        # This function handles both Fixed and Descriptor format.
        #
        # Arguments:
        #
        # SenseInfoBuffer
        # - A pointer to sense info buffer
        #
        # SenseInfoBufferLength
        # - Size of the buffer SenseInfoBuffer points to.
        #
        # Options
        # - Options used by this routine. It is a bit-field value. See defintions
        # of list of #define SCSI_SENSE_OPTIONS above in this file.
        #
        # SenseKey
        # - On output, buffer contains the sense key.
        # Note: If null is specified, the function will not retrieve the sense key
        #
        # AdditionalSenseCode
        # - On output, buffer contains the additional sense code.
        # Note: If null is specified, the function will not retrieve the additional sense code.
        #
        # AdditionalSenseCodeQualifier
        # - On output, buffer contains the additional sense code qualifier.
        # Note: If null is specified, the function will not retrieve the additional sense code qualifier.
        #
        # Returns:
        #
        # TRUE if the function is able to retrieve the requested information.
        #
        # Otherwise, FALSE
        #
        # {
        # BOOLEAN succeed = FALSE;
        #
        # if (SenseInfoBuffer == NULL || SenseInfoBufferLength == 0) {
        # return FALSE;
        # }
        #
        # if (IsDescriptorSenseDataFormat(SenseInfoBuffer)) {
        #
        # succeed = ScsiGetDescriptorSenseKeyAndCodes( SenseInfoBuffer,
        # SenseInfoBufferLength,
        # SenseKey,
        # AdditionalSenseCode,
        # AdditionalSenseCodeQualifier );
        # } else {
        #
        # if ((Options & SCSI_SENSE_OPTIONS_FIXED_FORMAT_IF_UNKNOWN_FORMAT_INDICATED) ||
        # IsFixedSenseDataFormat(SenseInfoBuffer)) {
        #
        # succeed = ScsiGetFixedSenseKeyAndCodes( SenseInfoBuffer,
        # SenseInfoBufferLength,
        # SenseKey,
        # AdditionalSenseCode,
        # AdditionalSenseCodeQualifier );
        # }
        # }
        #
        # return succeed;
        # }
        #
        # _Success_(return != FALSE)
        # FORCEINLINE BOOLEAN
        # ScsiGetSenseDescriptor(
        # _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
        # _In_ UCHAR SenseInfoBufferLength,
        # _Outptr_result_bytebuffer_(*DescriptorBufferLength) PVOID *DescriptorBuffer,
        # _Out_ UCHAR *DescriptorBufferLength
        # )
        #
        # Description:
        #
        # This function calculates available amount of descriptors information
        # within sense data in Descriptor format.  Then, it returns the starting
        # address of descriptors and amount of descriptor data available.
        #
        # Arguments:
        #
        # SenseInfoBuffer
        # - A pointer to sense info buffer
        #
        # SenseInfoBufferLength
        # - Size of the buffer SenseInfoBuffer points to.
        #
        # DescriptorBuffer
        # - On output, it contains pointer to the starting address of descriptor
        #
        # DescriptorBufferLength
        # - On output, it contains number of bytes of available descriptor data
        #
        # Returns:
        #
        # TRUE if the function succeeds
        #
        # Otherwise, FALSE
        #
        # Note: FALSE if no descriptor data are available.
        #
        # {
        # PDESCRIPTOR_SENSE_DATA descriptorSenseData;
        # BOOLEAN succeed = FALSE;
        # UCHAR dataLength = 0;
        #
        # if (SenseInfoBuffer == NULL    ||
        # SenseInfoBufferLength == 0 ||
        # DescriptorBuffer == NULL   ||
        # DescriptorBufferLength == NULL) {
        # return FALSE;
        # }
        #
        # *DescriptorBuffer = NULL;
        # *DescriptorBufferLength = 0;
        #
        # if (!IsDescriptorSenseDataFormat(SenseInfoBuffer)) {
        # return FALSE;
        # }
        #
        # descriptorSenseData = (PDESCRIPTOR_SENSE_DATA)SenseInfoBuffer;
        #
        # if (RTL_CONTAINS_FIELD(descriptorSenseData, SenseInfoBufferLength, AdditionalSenseLength)) {
        #
        # if (descriptorSenseData->AdditionalSenseLength <= (MAX_SENSE_BUFFER_SIZE - RTL_SIZEOF_THROUGH_FIELD(DESCRIPTOR_SENSE_DATA, AdditionalSenseLength))) {
        #
        # dataLength = descriptorSenseData->AdditionalSenseLength + RTL_SIZEOF_THROUGH_FIELD(DESCRIPTOR_SENSE_DATA, AdditionalSenseLength);
        #
        # if (dataLength > SenseInfoBufferLength) {
        # dataLength = SenseInfoBufferLength;
        # }
        #
        # *DescriptorBufferLength = dataLength - RTL_SIZEOF_THROUGH_FIELD(DESCRIPTOR_SENSE_DATA, AdditionalSenseLength);
        #
        # if (*DescriptorBufferLength > 0) {
        # *DescriptorBuffer = (PVOID)(descriptorSenseData->DescriptorBuffer);
        # succeed = TRUE;
        # }
        # }
        # }
        #
        # return succeed;
        # }
        #
        # _Success_(return != FALSE)
        # FORCEINLINE BOOLEAN
        # ScsiValidateInformationSenseDescriptor(
        # _In_reads_bytes_(DescriptorBufferLength) PVOID DescriptorBuffer,
        # _In_ UCHAR DescriptorBufferLength
        # )
        #
        # Description:
        #
        # This function validates if buffer contains a valid payload for descriptor of Information type
        #
        # Arguments:
        #
        # DescriptorBuffer
        # - Pointer to the starting address of descriptor payload
        #
        # DescriptorBufferLength
        # - Size of the buffer that DescriptorBuffer points to.
        #
        # Returns:
        #
        # TRUE if DescriptorBuffer contains valid payload for Information type descriptor.
        #
        # Otherwise, FALSE
        #
        # {
        # PSCSI_SENSE_DESCRIPTOR_INFORMATION descriptor;
        # UCHAR additionalLength;
        #
        # if (DescriptorBuffer == NULL || DescriptorBufferLength < sizeof(SCSI_SENSE_DESCRIPTOR_INFORMATION)) {
        # return FALSE;
        # }
        #
        # descriptor = (PSCSI_SENSE_DESCRIPTOR_INFORMATION)DescriptorBuffer;
        #
        # if (descriptor->Header.DescriptorType != SCSI_SENSE_DESCRIPTOR_TYPE_INFORMATION) {
        # return FALSE;
        # }
        #
        # additionalLength = sizeof(SCSI_SENSE_DESCRIPTOR_INFORMATION) - RTL_SIZEOF_THROUGH_FIELD(SCSI_SENSE_DESCRIPTOR_INFORMATION, Header);
        #
        # if (descriptor->Header.AdditionalLength != additionalLength) {
        # return FALSE;
        # }
        #
        # if (descriptor->Valid == 0) {
        # return FALSE;
        # }
        #
        # return TRUE;
        # }
        #
        # _Success_(return != FALSE)
        # FORCEINLINE BOOLEAN
        # ScsiValidateBlockCommandSenseDescriptor(
        # _In_reads_bytes_(DescriptorBufferLength) PVOID DescriptorBuffer,
        # _In_ UCHAR DescriptorBufferLength
        # )
        #
        # Description:
        #
        # This function validates if buffer contains a valid payload for Block Command type descriptor
        #
        # Arguments:
        #
        # DescriptorBuffer
        # - Pointer to the starting address of descriptor payload
        #
        # DescriptorBufferLength
        # - Size of the buffer that DescriptorBuffer points to
        #
        # Returns:
        #
        # TRUE if DescriptorBuffer contains a valid payload for descriptor of Block Command type
        #
        # Otherwise, FALSE
        #
        # {
        # PSCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND descriptor;
        # UCHAR additionalLength;
        #
        # if (DescriptorBuffer == NULL || DescriptorBufferLength < sizeof(SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND)) {
        # return FALSE;
        # }
        #
        # descriptor = (PSCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND)DescriptorBuffer;
        #
        # if (descriptor->Header.DescriptorType != SCSI_SENSE_DESCRIPTOR_TYPE_BLOCK_COMMAND) {
        # return FALSE;
        # }
        #
        # additionalLength = sizeof(SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND) - RTL_SIZEOF_THROUGH_FIELD(SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND, Header);
        #
        # if (descriptor->Header.AdditionalLength != additionalLength) {
        # return FALSE;
        # }
        #
        # return TRUE;
        # }
        #
        # _Success_(return != FALSE)
        # FORCEINLINE BOOLEAN
        # ScsiConvertToFixedSenseFormat(
        # _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
        # _In_ UCHAR SenseInfoBufferLength,
        # _Out_writes_bytes_(OutBufferLength) PVOID OutBuffer,
        # _In_ UCHAR OutBufferLength
        # )
        #
        # Description:
        #
        # This routine converts descriptor format sense data to fixed format sense data.
        #
        # Due to differences between two formats, the conversion is only based on Sense Key,
        # Additional Sense Code, and Additional Sense Code Qualififer.
        #
        # Arguments:
        #
        # SenseInfoBuffer
        # - A pointer to sense data buffer
        #
        # SenseInfoBufferLength
        # - Size of the buffer SenseInfoBuffer points to.
        #
        # OutBuffer
        # - On output, OutBuffer contains the fixed sense data as result of conversion.
        #
        # OutBufferLength
        # - Size of the buffer that OutBuffer points to.
        #
        # Returns:
        #
        # TRUE if conversion to Fixed format is successful.
        #
        # Otherwise, FALSE.
        #
        # {
        # BOOLEAN succeed = FALSE;
        # BOOLEAN validSense  = FALSE;
        # UCHAR senseKey = 0;
        # UCHAR additionalSenseCode = 0;
        # UCHAR additionalSenseCodeQualifier = 0;
        # PFIXED_SENSE_DATA outBuffer = (PFIXED_SENSE_DATA)OutBuffer;
        #
        # if (SenseInfoBuffer == NULL ||
        # SenseInfoBufferLength == 0 ||
        # OutBuffer == NULL ||
        # OutBufferLength < sizeof(FIXED_SENSE_DATA)) {
        # return FALSE;
        # }
        #
        # if (IsDescriptorSenseDataFormat(SenseInfoBuffer)) {
        #
        # RtlZeroMemory(OutBuffer, OutBufferLength);
        #
        # validSense = ScsiGetSenseKeyAndCodes(SenseInfoBuffer,
        # SenseInfoBufferLength,
        # SCSI_SENSE_OPTIONS_NONE,
        # &senseKey,
        # &additionalSenseCode,
        # &additionalSenseCodeQualifier);
        # if (validSense) {
        #
        # if (IsSenseDataCurrentError(SenseInfoBuffer)) {
        # outBuffer->ErrorCode = SCSI_SENSE_ERRORCODE_FIXED_CURRENT;
        # } else {
        # outBuffer->ErrorCode = SCSI_SENSE_ERRORCODE_FIXED_DEFERRED;
        # }
        # outBuffer->AdditionalSenseLength = sizeof(FIXED_SENSE_DATA) - RTL_SIZEOF_THROUGH_FIELD(FIXED_SENSE_DATA, AdditionalSenseLength);
        # outBuffer->SenseKey = senseKey;
        # outBuffer->AdditionalSenseCode = additionalSenseCode;
        # outBuffer->AdditionalSenseCodeQualifier = additionalSenseCodeQualifier;
        #
        # succeed = TRUE;
        # }
        # }
        #
        # return succeed;
        # }
        #
        # _Success_(return != FALSE)
        # FORCEINLINE BOOLEAN
        # ScsiGetNextSenseDescriptorByType (
        # _In_reads_bytes_(BufferLength) PVOID Buffer,
        # _In_ UCHAR BufferLength,
        # _In_reads_(TypeListCount) PUCHAR TypeList,
        # _In_ ULONG TypeListCount,
        # _Out_ PUCHAR OutType,
        # _Outptr_result_bytebuffer_(*OutBufferLength) PVOID *OutBuffer,
        # _Out_ UCHAR *OutBufferLength
        # )
        #
        # Description:
        #
        # This routine locates the next descriptor with type equals to one of the
        # types specified by caller.
        #
        # Arguments:
        #
        # Buffer - pointer to buffer to be searched.
        #
        # BufferLength - Size of the buffer that Buffer points to.
        #
        # TypeList - Pointer to array of descriptor types to be searched
        #
        # TypeListCount - Number of element in TypeList array
        #
        # OutType - Upon return, if a descriptor is found,
        # it contains the type of the descriptor.
        #
        # OutBuffer - Upon return, if a descriptor is found,
        # it points to start address of the descriptor buffer
        #
        # OutBufferLength - Upon return, if a descriptor is found,
        # it contains the number of bytes available starting at
        # OutBuffer. i.e. This is the buffer available between
        # OutBuffer pointer and end of Buffer.
        #
        # Returns:
        #
        # TRUE if descriptor of specified type is found.
        #
        # Otherwise, FALSE.
        #
        # {
        # PUCHAR remainingBuffer;
        # UCHAR remainingBufferLength;
        # UCHAR type;
        # ULONG i;
        # UCHAR descriptorLength;
        #
        # if (Buffer          == NULL ||
        # BufferLength    == 0    ||
        # TypeList        == NULL ||
        # TypeListCount   == 0    ||
        # OutType         == NULL ||
        # OutBuffer       == NULL ||
        # OutBufferLength == NULL) {
        #
        # return FALSE;
        # }
        #
        # *OutBuffer = NULL;
        # *OutBufferLength = 0;
        # *OutType = 0;
        #
        # remainingBuffer = (PUCHAR)Buffer;
        # remainingBufferLength = BufferLength;
        #
        # while (remainingBufferLength >= sizeof(SCSI_SENSE_DESCRIPTOR_HEADER)) {
        #
        # for (i = 0; i < TypeListCount; i++) {
        #
        # type = TypeList[i];
        #
        # if (((PSCSI_SENSE_DESCRIPTOR_HEADER)remainingBuffer)->DescriptorType == type) {
        # *OutBuffer = (PVOID)remainingBuffer;
        # *OutBufferLength = remainingBufferLength;
        # *OutType = type;
        # return TRUE;
        # }
        # }
        #
        # descriptorLength = ScsiGetSenseDescriptorLength(remainingBuffer);
        #
        # if (remainingBufferLength > descriptorLength) {
        #
        # Advance to start address of next descriptor
        # remainingBuffer += descriptorLength;
        # remainingBufferLength -= descriptorLength;
        #
        # } else {
        #
        # Search is completed.
        # break;
        # }
        #
        # }
        #
        # return FALSE;
        # }
        #
        # [END] Collections of SCSI utiltiy functions
        #
        # end_storport end_storportp
        #
        # end_ntminitape
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PKG_STORAGE)
# END IF   not defined _NTSCSI_
