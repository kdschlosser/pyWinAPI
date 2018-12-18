import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_MCE_ = None
_MSC_EXTENSIONS = None
_ARM64_ = None

class _MCI_ADDR(ctypes.Union):
    pass


MCI_ADDR = _MCI_ADDR
PMCI_ADDR = POINTER(_MCI_ADDR)


class _MCI_STATS(ctypes.Union):
    pass


MCI_STATS = _MCI_STATS
PMCI_STATS = POINTER(_MCI_STATS)


MCI_STATS = _MCI_STATS
PMCI_STATS = POINTER(_MCI_STATS)


MCI_STATS = _MCI_STATS
PMCI_STATS = POINTER(_MCI_STATS)


class _MCA_EXCEPTION(ctypes.Structure):
    pass


MCA_EXCEPTION = _MCA_EXCEPTION
PMCA_EXCEPTION = POINTER(_MCA_EXCEPTION)


MCA_EXCEPTION = _MCA_EXCEPTION
PMCA_EXCEPTION = POINTER(_MCA_EXCEPTION)


MCI_STATS = _MCI_STATS
PMCI_STATS = POINTER(_MCI_STATS)


class _ERROR_REVISION(ctypes.Union):
    pass


ERROR_REVISION = _ERROR_REVISION
PERROR_REVISION = POINTER(_ERROR_REVISION)


class _ERROR_TIMESTAMP(ctypes.Union):
    pass


ERROR_TIMESTAMP = _ERROR_TIMESTAMP
PERROR_TIMESTAMP = POINTER(_ERROR_TIMESTAMP)


class _ERROR_GUID(ctypes.Structure):
    pass


ERROR_GUID = _ERROR_GUID
PERROR_GUID = POINTER(_ERROR_GUID)


class _ERROR_RECORD_VALID(ctypes.Union):
    pass


ERROR_RECORD_VALID = _ERROR_RECORD_VALID
PERROR_RECORD_VALID = POINTER(_ERROR_RECORD_VALID)


class _ERROR_RECORD_HEADER(ctypes.Structure):
    pass


ERROR_RECORD_HEADER = _ERROR_RECORD_HEADER
PERROR_RECORD_HEADER = POINTER(_ERROR_RECORD_HEADER)


class _ERROR_RECOVERY_INFO(ctypes.Union):
    pass


ERROR_RECOVERY_INFO = _ERROR_RECOVERY_INFO
PERROR_RECOVERY_INFO = POINTER(_ERROR_RECOVERY_INFO)


class _ERROR_SECTION_HEADER(ctypes.Structure):
    pass


ERROR_SECTION_HEADER = _ERROR_SECTION_HEADER
PERROR_SECTION_HEADER = POINTER(_ERROR_SECTION_HEADER)


class _ERROR_MODINFO_VALID(ctypes.Union):
    pass


ERROR_MODINFO_VALID = _ERROR_MODINFO_VALID
PERROR_MODINFO_VALID = POINTER(_ERROR_MODINFO_VALID)


class _ERROR_CACHE_CHECK(ctypes.Union):
    pass


ERROR_CACHE_CHECK = _ERROR_CACHE_CHECK
PERROR_CACHE_CHECK = POINTER(_ERROR_CACHE_CHECK)


ERROR_CACHE_CHECK = _ERROR_CACHE_CHECK
PERROR_CACHE_CHECK = POINTER(_ERROR_CACHE_CHECK)


class _ERROR_TLB_CHECK(ctypes.Union):
    pass


ERROR_TLB_CHECK = _ERROR_TLB_CHECK
PERROR_TLB_CHECK = POINTER(_ERROR_TLB_CHECK)


class _ERROR_BUS_CHECK(ctypes.Union):
    pass


ERROR_BUS_CHECK = _ERROR_BUS_CHECK
PERROR_BUS_CHECK = POINTER(_ERROR_BUS_CHECK)


ERROR_BUS_CHECK = _ERROR_BUS_CHECK
PERROR_BUS_CHECK = POINTER(_ERROR_BUS_CHECK)


class _ERROR_REGFILE_CHECK(ctypes.Union):
    pass


ERROR_REGFILE_CHECK = _ERROR_REGFILE_CHECK
PERROR_REGFILE_CHECK = POINTER(_ERROR_REGFILE_CHECK)


class _ERROR_MS_CHECK(ctypes.Union):
    pass


ERROR_MS_CHECK = _ERROR_MS_CHECK
PERROR_MS_CHECK = POINTER(_ERROR_MS_CHECK)


class _ERROR_CHECK_INFO(ctypes.Union):
    pass


ERROR_CHECK_INFO = _ERROR_CHECK_INFO
PERROR_CHECK_INFO = POINTER(_ERROR_CHECK_INFO)


class _ERROR_MODINFO(ctypes.Structure):
    pass


ERROR_MODINFO = _ERROR_MODINFO
PERROR_MODINFO = POINTER(_ERROR_MODINFO)


class _ERROR_PROCESSOR_VALID(ctypes.Union):
    pass


ERROR_PROCESSOR_VALID = _ERROR_PROCESSOR_VALID
PERROR_PROCESSOR_VALID = POINTER(_ERROR_PROCESSOR_VALID)


class _ERROR_PROCESSOR_ERROR_MAP(ctypes.Union):
    pass


ERROR_PROCESSOR_ERROR_MAP = _ERROR_PROCESSOR_ERROR_MAP
PERROR_PROCESSOR_ERROR_MAP = POINTER(_ERROR_PROCESSOR_ERROR_MAP)


class _ERROR_PROCESSOR_STATE_PARAMETER(ctypes.Union):
    pass


ERROR_PROCESSOR_STATE_PARAMETER = _ERROR_PROCESSOR_STATE_PARAMETER
PERROR_PROCESSOR_STATE_PARAMETER = POINTER(_ERROR_PROCESSOR_STATE_PARAMETER)


class _PROCESSOR_LOCAL_ID(ctypes.Union):
    pass


PROCESSOR_LOCAL_ID = _PROCESSOR_LOCAL_ID
PPROCESSOR_LOCAL_ID = POINTER(_PROCESSOR_LOCAL_ID)


class _ERROR_PROCESSOR_MS(ctypes.Structure):
    pass


ERROR_PROCESSOR_MS = _ERROR_PROCESSOR_MS
PERROR_PROCESSOR_MS = POINTER(_ERROR_PROCESSOR_MS)


class _ERROR_PROCESSOR_CPUID_INFO(ctypes.Structure):
    pass


ERROR_PROCESSOR_CPUID_INFO = _ERROR_PROCESSOR_CPUID_INFO
PERROR_PROCESSOR_CPUID_INFO = POINTER(_ERROR_PROCESSOR_CPUID_INFO)


class _ERROR_PROCESSOR_STATIC_INFO_VALID(ctypes.Union):
    pass


ERROR_PROCESSOR_STATIC_INFO_VALID = _ERROR_PROCESSOR_STATIC_INFO_VALID
PERROR_PROCESSOR_STATIC_INFO_VALID = POINTER(_ERROR_PROCESSOR_STATIC_INFO_VALID)


class _ERROR_PROCESSOR_STATIC_INFO(ctypes.Structure):
    pass


ERROR_PROCESSOR_STATIC_INFO = _ERROR_PROCESSOR_STATIC_INFO
PERROR_PROCESSOR_STATIC_INFO = POINTER(_ERROR_PROCESSOR_STATIC_INFO)


class _ERROR_PROCESSOR(ctypes.Structure):
    pass


ERROR_PROCESSOR = _ERROR_PROCESSOR
PERROR_PROCESSOR = POINTER(_ERROR_PROCESSOR)


class _ERROR_STATUS(ctypes.Union):
    pass


ERROR_STATUS = _ERROR_STATUS
PERROR_STATUS = POINTER(_ERROR_STATUS)


class _ERROR_OEM_DATA(ctypes.Structure):
    pass


ERROR_OEM_DATA = _ERROR_OEM_DATA
PERROR_OEM_DATA = POINTER(_ERROR_OEM_DATA)


class _ERROR_BUS_SPECIFIC_DATA(ctypes.Union):
    pass


ERROR_BUS_SPECIFIC_DATA = _ERROR_BUS_SPECIFIC_DATA
PERROR_BUS_SPECIFIC_DATA = POINTER(_ERROR_BUS_SPECIFIC_DATA)


class _ERROR_MEMORY_VALID(ctypes.Union):
    pass


ERROR_MEMORY_VALID = _ERROR_MEMORY_VALID
PERROR_MEMORY_VALID = POINTER(_ERROR_MEMORY_VALID)


class _ERROR_MEMORY(ctypes.Structure):
    pass


ERROR_MEMORY = _ERROR_MEMORY
PERROR_MEMORY = POINTER(_ERROR_MEMORY)


class _ERROR_PCI_BUS_VALID(ctypes.Union):
    pass


ERROR_PCI_BUS_VALID = _ERROR_PCI_BUS_VALID
PERROR_PCI_BUS_VALID = POINTER(_ERROR_PCI_BUS_VALID)


class _ERROR_PCI_BUS_TYPE(ctypes.Structure):
    pass


ERROR_PCI_BUS_TYPE = _ERROR_PCI_BUS_TYPE
PERROR_PCI_BUS_TYPE = POINTER(_ERROR_PCI_BUS_TYPE)


class _ERROR_PCI_BUS_ID(ctypes.Structure):
    pass


ERROR_PCI_BUS_ID = _ERROR_PCI_BUS_ID
PERROR_PCI_BUS_ID = POINTER(_ERROR_PCI_BUS_ID)


class _ERROR_PCI_BUS(ctypes.Structure):
    pass


ERROR_PCI_BUS = _ERROR_PCI_BUS
PERROR_PCI_BUS = POINTER(_ERROR_PCI_BUS)


class _ERROR_PCI_COMPONENT_VALID(ctypes.Union):
    pass


ERROR_PCI_COMPONENT_VALID = _ERROR_PCI_COMPONENT_VALID
PERROR_PCI_COMPONENT_VALID = POINTER(_ERROR_PCI_COMPONENT_VALID)


class _ERROR_PCI_COMPONENT_INFO(ctypes.Structure):
    pass


ERROR_PCI_COMPONENT_INFO = _ERROR_PCI_COMPONENT_INFO
PERROR_PCI_COMPONENT_INFO = POINTER(_ERROR_PCI_COMPONENT_INFO)


class _ERROR_PCI_COMPONENT(ctypes.Structure):
    pass


ERROR_PCI_COMPONENT = _ERROR_PCI_COMPONENT
PERROR_PCI_COMPONENT = POINTER(_ERROR_PCI_COMPONENT)


class _ERROR_SYSTEM_EVENT_LOG_VALID(ctypes.Union):
    pass


ERROR_SYSTEM_EVENT_LOG_VALID = _ERROR_SYSTEM_EVENT_LOG_VALID
PSYSTEM_EVENT_LOG_VALID = POINTER(_ERROR_SYSTEM_EVENT_LOG_VALID)


class _ERROR_SYSTEM_EVENT_LOG(ctypes.Structure):
    pass


ERROR_SYSTEM_EVENT_LOG = _ERROR_SYSTEM_EVENT_LOG
PERROR_SYSTEM_EVENT_LOG = POINTER(_ERROR_SYSTEM_EVENT_LOG)


class _ERROR_SMBIOS_VALID(ctypes.Union):
    pass


ERROR_SMBIOS_VALID = _ERROR_SMBIOS_VALID
PERROR_SMBIOS_VALID = POINTER(_ERROR_SMBIOS_VALID)


class _ERROR_SMBIOS(ctypes.Structure):
    pass


ERROR_SMBIOS = _ERROR_SMBIOS
PERROR_SMBIOS = POINTER(_ERROR_SMBIOS)


class _ERROR_PLATFORM_SPECIFIC_VALID(ctypes.Union):
    pass


ERROR_PLATFORM_SPECIFIC_VALID = _ERROR_PLATFORM_SPECIFIC_VALID
PERROR_PLATFORM_SPECIFIC_VALID = POINTER(_ERROR_PLATFORM_SPECIFIC_VALID)


class _ERROR_PLATFORM_SPECIFIC(ctypes.Structure):
    pass


ERROR_PLATFORM_SPECIFIC = _ERROR_PLATFORM_SPECIFIC
PERROR_PLATFORM_SPECIFIC = POINTER(_ERROR_PLATFORM_SPECIFIC)


class _ERROR_PLATFORM_BUS_VALID(ctypes.Union):
    pass


ERROR_PLATFORM_BUS_VALID = _ERROR_PLATFORM_BUS_VALID
PERROR_PLATFORM_BUS_VALID = POINTER(_ERROR_PLATFORM_BUS_VALID)


class _ERROR_PLATFORM_BUS(ctypes.Structure):
    pass


ERROR_PLATFORM_BUS = _ERROR_PLATFORM_BUS
PERROR_PLATFORM_BUS = POINTER(_ERROR_PLATFORM_BUS)


class _ERROR_PLATFORM_HOST_CONTROLLER_VALID(ctypes.Union):
    pass


ERROR_PLATFORM_HOST_CONTROLLER_VALID = _ERROR_PLATFORM_HOST_CONTROLLER_VALID
PERROR_PLATFORM_HOST_CONTROLLER_VALID = POINTER(_ERROR_PLATFORM_HOST_CONTROLLER_VALID)


class _ERROR_PLATFORM_HOST_CONTROLLER(ctypes.Structure):
    pass


ERROR_PLATFORM_HOST_CONTROLLER = _ERROR_PLATFORM_HOST_CONTROLLER
PERROR_PLATFORM_HOST_CONTROLLER = POINTER(_ERROR_PLATFORM_HOST_CONTROLLER)


MCA_EXCEPTION = _MCA_EXCEPTION
PMCA_EXCEPTION = POINTER(_MCA_EXCEPTION)




# /* + + BUILD Version: 0011 // Increment this if a change has global effects
# Copyright (c) 1991-2001 Microsoft Corporation Module Name: mce.h Abstract:
# This header file defines the Machine Check Errors definitions. Author:
# Revision History: Creation: 04-Apr-2001 --
if not defined(_MCE_):
    # DEFINE ERROR:    #define _MCE_
    if _MSC_VER >= 1200:
        pass
    # END IF


    # HalMcaLogInformation
    class MCA_EXCEPTION_TYPE(ENUM):
        HAL_MCE_RECORD = 1
        HAL_MCA_RECORD = 2

    HAL_MCE_RECORD = MCA_EXCEPTION_TYPE.HAL_MCE_RECORD
    HAL_MCA_RECORD = MCA_EXCEPTION_TYPE.HAL_MCA_RECORD

    if defined(_X86_) or defined(_IA64_) or defined(_AMD64_):
        # ADDR register for each MCA bank
        class DUMMYSTRUCTNAME(ctypes.Structure):
            pass


        DUMMYSTRUCTNAME._fields_ = [
            ('Address', ULONG),
            ('Reserved', ULONG),
        ]
        _MCI_ADDR.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


        _MCI_ADDR._fields_ = [
            ('DUMMYSTRUCTNAME', _MCI_ADDR.DUMMYSTRUCTNAME),
            ('QuadPart', ULONGLONG),
        ]

        if defined(_AMD64_):
            # STATUS register for each MCA bank.
            if NTDDI_VERSION <= NTDDI_WINXP:
                class MciStatus(ctypes.Structure):
                    pass


                MciStatus._fields_ = [
                    ('McaCod', USHORT),
                    ('ModelErrorCode', USHORT),
                    ('OtherInfo', ULONG, 25),
                    ('Damage', ULONG, 1),
                    ('AddressValid', ULONG, 1),
                    ('MiscValid', ULONG, 1),
                    ('Enabled', ULONG, 1),
                    ('Uncorrected', ULONG, 1),
                    ('OverFlow', ULONG, 1),
                    ('Valid', ULONG, 1),
                ]
                _MCI_STATS.MciStatus = MciStatus


                _MCI_STATS._fields_ = [
                    ('MciStatus', _MCI_STATS.MciStatus),
                    ('QuadPart', ULONG64),
                ]
            else:
                class MciStatus(ctypes.Structure):
                    pass


                MciStatus._fields_ = [
                    ('McaErrorCode', USHORT),
                    ('ModelErrorCode', USHORT),
                    ('OtherInformation', ULONG, 25),
                    ('ContextCorrupt', ULONG, 1),
                    ('AddressValid', ULONG, 1),
                    ('MiscValid', ULONG, 1),
                    ('ErrorEnabled', ULONG, 1),
                    ('UncorrectedError', ULONG, 1),
                    ('StatusOverFlow', ULONG, 1),
                    ('Valid', ULONG, 1),
                ]
                _MCI_STATS.MciStatus = MciStatus


                _MCI_STATS._fields_ = [
                    ('MciStatus', _MCI_STATS.MciStatus),
                    ('QuadPart', ULONG64),
                ]
            # END IF

        # END IF   _AMD64_


        if defined(_X86_):
            # STATUS register for each MCA bank.
            class MciStats(ctypes.Structure):
                pass


            MciStats._fields_ = [
                ('McaCod', USHORT),
                ('MsCod', USHORT),
                ('OtherInfo', ULONG, 25),
                ('Damage', ULONG, 1),
                ('AddressValid', ULONG, 1),
                ('MiscValid', ULONG, 1),
                ('Enabled', ULONG, 1),
                ('UnCorrected', ULONG, 1),
                ('OverFlow', ULONG, 1),
                ('Valid', ULONG, 1),
            ]
            _MCI_STATS.MciStats = MciStats


            _MCI_STATS._fields_ = [
                ('MciStats', _MCI_STATS.MciStats),
                ('QuadPart', ULONGLONG),
            ]
        # END IF   _X86_


        # MCA exception log entry
        # Defined as a union to contain MCA specific log or Pentium style MCE
        # info.
        MCA_EXTREG_V2MAX = 24        # X86: Max. Number of extended registers

        if defined(_X86_) or defined(_AMD64_):
            if NTDDI_VERSION >= NTDDI_WINXP:
                class u(ctypes.Union):
                    pass


                class Mca(ctypes.Structure):
                    pass


                Mca._fields_ = [
                    ('BankNumber', UCHAR),
                    ('Reserved2', UCHAR * 7),
                    ('Status', MCI_STATS),
                    ('Address', MCI_ADDR),
                    ('Misc', ULONGLONG),
                ]
                u.Mca = Mca


                # physical addr of cycle causing the error
                class Mce(ctypes.Structure):
                    pass


                Mce._fields_ = [
                    ('Address', ULONGLONG),
                    # cycle specification causing the error
                    ('Type', ULONGLONG),
                ]
                u.Mce = Mce


                u._fields_ = [
                    ('Mca', u.Mca),
                    ('Mce', u.Mce),
                ]
                _MCA_EXCEPTION.u = u


                _MCA_EXCEPTION._fields_ = [
                    # Version number of this record type
                    ('VersionNumber', ULONG),
                    # MCA or MCE
                    ('ExceptionType', MCA_EXCEPTION_TYPE),
                    # exception recording timestamp
                    ('TimeStamp', LARGE_INTEGER),
                    ('ProcessorNumber', ULONG),
                    ('Reserved1', ULONG),
                    ('u', _MCA_EXCEPTION.u),
                    # Begin Version 2 stuff
                    ('ExtCnt', ULONG),
                    ('Reserved3', ULONG),
                    ('ExtReg', ULONGLONG * MCA_EXTREG_V2MAX),
                ]
            else:
                class u(ctypes.Union):
                    pass


                class Mca(ctypes.Structure):
                    pass


                Mca._fields_ = [
                    ('BankNumber', UCHAR),
                    ('Reserved2', UCHAR * 7),
                    ('Status', MCI_STATS),
                    ('Address', MCI_ADDR),
                    ('Misc', ULONGLONG),
                ]
                u.Mca = Mca


                # physical addr of cycle causing the error
                class Mce(ctypes.Structure):
                    pass


                Mce._fields_ = [
                    ('Address', ULONGLONG),
                    # cycle specification causing the error
                    ('Type', ULONGLONG),
                ]
                u.Mce = Mce


                u._fields_ = [
                    ('Mca', u.Mca),
                    ('Mce', u.Mce),
                ]
                _MCA_EXCEPTION.u = u


                _MCA_EXCEPTION._fields_ = [
                    # Version number of this record type
                    ('VersionNumber', ULONG),
                    # MCA or MCE
                    ('ExceptionType', MCA_EXCEPTION_TYPE),
                    # exception recording timestamp
                    ('TimeStamp', LARGE_INTEGER),
                    ('ProcessorNumber', ULONG),
                    ('Reserved1', ULONG),
                    ('u', _MCA_EXCEPTION.u),
                ]
            # END IF


            # Corrected Machine Check
            CMC_EXCEPTION = MCA_EXCEPTION
            PCMC_EXCEPTION = POINTER(MCA_EXCEPTION)

            # Corrected Platform Error
            CPE_EXCEPTION = MCA_EXCEPTION
            PCPE_EXCEPTION = POINTER(MCA_EXCEPTION)
            if NTDDI_VERSION >= NTDDI_WINXP:
                MCA_EXCEPTION_V1_SIZE = FIELD_OFFSET(MCA_EXCEPTION, 'ExtCnt')
                MCA_EXCEPTION_V2_SIZE = ctypes.sizeof(_MCA_EXCEPTION)
            # END IF
        # END IF   _X86_ or _AMD64_

        # ERRORS: ERROR_SEVERITY definitions
        # One day the MS compiler will support typed enums with type != INT so
        # this
        # type of enums (UCHAR, __int64) could be defined...
        if defined(_AMD64_) or defined(_IA64_):
            ERROR_SEVERITY = UCHAR
            PERROR_SEVERITY = POINTER(UCHAR)


            class _ERROR_SEVERITY_VALUE(ENUM):
                ErrorRecoverable = 0
                ErrorFatal = 1
                ErrorCorrected = 2
                ErrorOthers = 3

            ERROR_SEVERITY_VALUE = _ERROR_SEVERITY_VALUE
        # END IF


        if defined(_IA64_):
            _FIXFIX_ = 0
            if _FIXFIX_:
                # FIXFIX: This should not be required for IA64.
                # STATUS register for each MCA bank.
                class MciStats(ctypes.Structure):
                    pass


                MciStats._fields_ = [
                    ('McaCod', USHORT),
                    ('MsCod', USHORT),
                    ('OtherInfo', ULONG, 25),
                    ('Damage', ULONG, 1),
                    ('AddressValid', ULONG, 1),
                    ('MiscValid', ULONG, 1),
                    ('Enabled', ULONG, 1),
                    ('UnCorrected', ULONG, 1),
                    ('OverFlow', ULONG, 1),
                    ('Valid', ULONG, 1),
                ]
                _MCI_STATS.MciStats = MciStats


                _MCI_STATS._fields_ = [
                    ('MciStats', _MCI_STATS.MciStats),
                    ('QuadPart', ULONGLONG),
                ]
            # END IF   0

            # IA64 ERRORS: ERROR_REVISION definitions
            # Major and Minor revision number of the record:
            # Byte0: Minor.
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('Minor', UCHAR),
                # Byte1: Major.
                ('Major', UCHAR),
            ]
            _ERROR_REVISION.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_REVISION._fields_ = [
                ('Revision', USHORT),
                ('DUMMYSTRUCTNAME', _ERROR_REVISION.DUMMYSTRUCTNAME),
            ]

            # For Info:
            if NTDDI_VERSION > NTDDI_WINXP:
                ERROR_MAJOR_REVISION_SAL_03_00 = 0
                ERROR_MINOR_REVISION_SAL_03_00 = 2
                ERROR_REVISION_SAL_03_00 = [
                    ERROR_MINOR_REVISION_SAL_03_00,
                    ERROR_MAJOR_REVISION_SAL_03_00
                ]


                # Section Header revision is fixed at Major == 2 and Minor == 0
                ERROR_FIXED_SECTION_REVISION = [2, 0]
            else:
                ERROR_REVISION_SAL_03_00 = [2, 0]
            # END IF


            # IA64 ERRORS: ERROR_TIMESTAMP definitions
            # Byte0: Seconds
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('Seconds', UCHAR),
                # Byte1: Minutes
                ('Minutes', UCHAR),
                # Byte2: Hours
                ('Hours', UCHAR),
                # Byte3: Reserved
                ('Reserved', UCHAR),
                # Byte4: Day
                ('Day', UCHAR),
                # Byte5: Month
                ('Month', UCHAR),
                # Byte6: Year
                ('Year', UCHAR),
                # Byte7: Century
                ('Century', UCHAR),
            ]
            _ERROR_TIMESTAMP.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_TIMESTAMP._fields_ = [
                ('TimeStamp', ULONGLONG),
                ('DUMMYSTRUCTNAME', _ERROR_TIMESTAMP.DUMMYSTRUCTNAME),
            ]

            # IA64 ERRORS: ERROR_GUID definitions
            _ERROR_GUID._fields_ = [
                ('Data1', ULONG),
                ('Data2', USHORT),
                ('Data3', USHORT),
                ('Data4', UCHAR * 8),
            ]

            # IA64 ERRORS: ERROR GUIDs definitions
            _ERROR_DEVICE_GUID = ERROR_GUID
            ERROR_DEVICE_GUID = _ERROR_DEVICE_GUID
            PERROR_DEVICE_GUID = POINTER(_ERROR_DEVICE_GUID)
            _ERROR_PLATFORM_GUID = ERROR_GUID
            ERROR_PLATFORM_GUID = _ERROR_PLATFORM_GUID
            PERROR_PLATFORM_GUID = POINTER(_ERROR_PLATFORM_GUID)

            # IA64 ERRORS: ERROR_RECORD_HEADER definitions
            # 0: OEM Platform Id is present in the record header
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('OemPlatformID', UCHAR, 1),
                # 1-7: Reserved
                ('Reserved', UCHAR, 7),
            ]
            _ERROR_RECORD_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_RECORD_VALID._fields_ = [
                ('Valid', UCHAR),
                # Bits
                ('DUMMYSTRUCTNAME', _ERROR_RECORD_VALID.DUMMYSTRUCTNAME),
            ]

            # 0: Unique identifier
            _ERROR_RECORD_HEADER._fields_ = [
                ('Id', ULONGLONG),
                # 8: Major and Minor revision number of the record
                ('Revision', ERROR_REVISION),
                # 10: Error Severity
                ('ErrorSeverity', ERROR_SEVERITY),
                # 11: Validation bits
                ('Valid', ERROR_RECORD_VALID),
                # 12: Length of this record in bytes, including the header
                ('Length', ULONG),
                # 16: Timestamp recorded when event occurred
                ('TimeStamp', ERROR_TIMESTAMP),
                # 24: Unique platform identifier. OEM defined.
                ('OemPlatformId', UCHAR * 16),
            ]

            # IA64 ERRORS: ERROR_SECTION_HEADER definitions
            # 0: Corrected
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('Corrected', UCHAR, 1),
                # 1: Containment Warning
                ('NotContained', UCHAR, 1),
                # 2: Reset
                ('Reset', UCHAR, 1),
                # 6-3: Reserved
                ('Reserved', UCHAR, 4),
                # 7: Valid Recovery Information
                ('Valid', UCHAR, 1),
            ]
            _ERROR_RECOVERY_INFO.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_RECOVERY_INFO._fields_ = [
                ('RecoveryInfo', UCHAR),
                # Bits:
                ('DUMMYSTRUCTNAME', _ERROR_RECOVERY_INFO.DUMMYSTRUCTNAME),
            ]

            # Unique identifier
            _ERROR_SECTION_HEADER._fields_ = [
                ('Guid', ERROR_DEVICE_GUID),
                # Major and Minor revision number of the section
                ('Revision', ERROR_REVISION),
                # Recovery Information
                ('RecoveryInfo', ERROR_RECOVERY_INFO),
                ('Reserved', UCHAR),
                # Length of this error device section in bytes,
                ('Length', ULONG),
            ]

            # IA64 Machine Check Error Logs:
            # WMI requires processor LID being stored in the Log.
            # This LID corresponds to the processor on which the SAL_PROC was
            # executed on.
            # TEMPTEMP: Implementation is temporary, until we implement HAL SW
            # Error Section.
            # Note that the current FW builds do not update the
            # _ERROR_PROCESSOR.CRLid field,
            # assuming there is a _ERROR_PROCESSOR section in the record.
            if not defined(__midl) and defined(_MSC_EXTENSIONS):
                # GetFwMceLogProcessorNumber()
                pass
            # END IF   not __midl

            # IA64 ERRORS: ERROR_PROCESSOR device definitions
            # The MCA architecture supports five different types of error
            # reporting functional units
            # with the associated error records and its error severity.
            # At any point in time, a processor could encounter an MCA/CMC
            # event due to errors detected
            # in one or more of the following units:
            # - Cache Check
            # - TLB Check
            # - Bus Check
            # - Register File
            # - Micro Architectural
            # Terminology:
            # - Target Address:
            # 64-bit integer containing the physical address where the data
            # was to be delivered or
            # obtained. This could also be the incoming address for external
            # snoops and TLB shoot-downs.
            # - Requester Identifier:
            # 64-bit integer specifying the bus agent that generated the
            # transaction responsible for
            # the Machine Check event.
            # - Responder Identifier:
            # 64-bit integer specifying the bus agent that responded to a
            # transaction responsible for
            # the Machine Check event.
            # - Precise Instruction Pointer:
            # 64-bit integer specifying the virtual address that points to the
            # IA-64 bundle that
            # contained the instruction responsible for the Machine Check
            # event.
            ERROR_PROCESSOR_GUID = (
                0xE429FAF1,
                0x3CB7,
                0x11D4,
                [0xBC, 0xA7, 0x0, 0x80, 0xC7, 0x3C, 0x88, 0x81],
            )


            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('CheckInfo', ULONGLONG, 1),
                # 1:
                ('RequestorIdentifier', ULONGLONG, 1),
                # 2:
                ('ResponderIdentifier', ULONGLONG, 1),
                # 3:
                ('TargetIdentifier', ULONGLONG, 1),
                # 4:
                ('PreciseIP', ULONGLONG, 1),
                # 5-63:
                ('Reserved', ULONGLONG, 59),
            ]
            _ERROR_MODINFO_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_MODINFO_VALID._fields_ = [
                ('Valid', ULONGLONG),
                # Bits
                ('DUMMYSTRUCTNAME', _ERROR_MODINFO_VALID.DUMMYSTRUCTNAME),
            ]


            class _ERROR_CHECK_IS(ENUM):
                isIA64 = 0
                isIA32 = 1

            ERROR_CHECK_IS = _ERROR_CHECK_IS


            class _ERROR_CACHE_CHECK_OPERATION(ENUM):
                CacheUnknownOp = 0
                CacheLoad = 1
                CacheStore = 2
                CacheInstructionFetch = 3
                CacheDataPrefetch = 4
                CacheSnoop = 5
                CacheCastOut = 6
                CacheMoveIn = 7

            ERROR_CACHE_CHECK_OPERATION = _ERROR_CACHE_CHECK_OPERATION


            class _ERROR_CACHE_CHECK_MESI(ENUM):
                CacheInvalid = 0
                CacheHeldShared = 1
                CacheHeldExclusive = 2
                CacheModified = 3

            ERROR_CACHE_CHECK_MESI = _ERROR_CACHE_CHECK_MESI
            if NTDDI_VERSION >= NTDDI_VISTA:
                class DUMMYSTRUCTNAME(ctypes.Structure):
                    pass


                DUMMYSTRUCTNAME._fields_ = [
                    # bits 0- 3: Cache operation
                    ('Operation', ULONGLONG, 4),
                    # 4- 5: Cache Level
                    ('Level', ULONGLONG, 2),
                    # 6- 7
                    ('Reserved1', ULONGLONG, 2),
                    # 8 : Failure data part of cache line
                    ('DataLine', ULONGLONG, 1),
                    # 9 : Failure tag part of cache line
                    ('TagLine', ULONGLONG, 1),
                    # 10 : Failure in data cache
                    ('DataCache', ULONGLONG, 1),
                    # 11 : Failure in instruction cache
                    ('InstructionCache', ULONGLONG, 1),
                    # 12-14:
                    ('MESI', ULONGLONG, 3),
                    # 15 : MESI field is valid
                    ('MESIValid', ULONGLONG, 1),
                    # 16-20: Failure in Way of Cache
                    ('Way', ULONGLONG, 5),
                    # 21 : Way and Index fields valid
                    ('WayIndexValid', ULONGLONG, 1),
                    # 22
                    ('Reserved2', ULONGLONG, 1),
                    # 23 : 1 - error due to data poisoning
                    ('DP', ULONGLONG, 1),
                    # 24-31
                    ('Reserved3', ULONGLONG, 8),
                    # 32-51: Index of cache line
                    ('Index', ULONGLONG, 20),
                    # 52-53
                    ('Reserved4', ULONGLONG, 2),
                    # 54 : 0 - IA64 instruction, 1- IA32 instruction
                    ('InstructionSet', ULONGLONG, 1),
                    # 55 : InstructionSet field is valid
                    ('InstructionSetValid', ULONGLONG, 1),
                    # 56-57: Privilege level of instruction
                    ('PrivilegeLevel', ULONGLONG, 2),
                    # 58 : PrivilegeLevel field is Valid
                    ('PrivilegeLevelValid', ULONGLONG, 1),
                    # 59 : 1 - Machine Check Corrected
                    ('MachineCheckCorrected', ULONGLONG, 1),
                    # 60 : Target Address is valid
                    ('TargetAddressValid', ULONGLONG, 1),
                    # 61 : RequestId is valid
                    ('RequestIdValid', ULONGLONG, 1),
                    # 62 : ResponderId is valid
                    ('ResponderIdValid', ULONGLONG, 1),
                    # 63 : Precise Instruction Pointer is Valid
                    ('PreciseIPValid', ULONGLONG, 1),
                ]
                _ERROR_CACHE_CHECK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


                _ERROR_CACHE_CHECK._fields_ = [
                    ('CacheCheck', ULONGLONG),
                    ('DUMMYSTRUCTNAME', _ERROR_CACHE_CHECK.DUMMYSTRUCTNAME),
                ]
            else:
                class DUMMYSTRUCTNAME(ctypes.Structure):
                    pass


                DUMMYSTRUCTNAME._fields_ = [
                    # bits 0- 3: Cache operation
                    ('Operation', ULONGLONG, 4),
                    # 4- 5: Cache Level
                    ('Level', ULONGLONG, 2),
                    # 6- 7
                    ('Reserved1', ULONGLONG, 2),
                    # 8 : Failure data part of cache line
                    ('DataLine', ULONGLONG, 1),
                    # 9 : Failure tag part of cache line
                    ('TagLine', ULONGLONG, 1),
                    # 10 : Failure in data cache
                    ('DataCache', ULONGLONG, 1),
                    # 11 : Failure in instruction cache
                    ('InstructionCache', ULONGLONG, 1),
                    # 12-14:
                    ('MESI', ULONGLONG, 3),
                    # 15 : MESI field is valid
                    ('MESIValid', ULONGLONG, 1),
                    # 16-20: Failure in Way of Cache
                    ('Way', ULONGLONG, 5),
                    # 21 : Way and Index fields valid
                    ('WayIndexValid', ULONGLONG, 1),
                    # 22-31
                    ('Reserved2', ULONGLONG, 10),
                    # 32-51: Index of cache line
                    ('Index', ULONGLONG, 20),
                    # 52-53
                    ('Reserved3', ULONGLONG, 2),
                    # 54 : 0 - IA64 instruction, 1- IA32 instruction
                    ('InstructionSet', ULONGLONG, 1),
                    # 55 : InstructionSet field is valid
                    ('InstructionSetValid', ULONGLONG, 1),
                    # 56-57: Privilege level of instruction
                    ('PrivilegeLevel', ULONGLONG, 2),
                    # 58 : PrivilegeLevel field is Valid
                    ('PrivilegeLevelValid', ULONGLONG, 1),
                    # 59 : 1 - Machine Check Corrected
                    ('MachineCheckCorrected', ULONGLONG, 1),
                    # 60 : Target Address is valid
                    ('TargetAddressValid', ULONGLONG, 1),
                    # 61 : RequestId is valid
                    ('RequestIdValid', ULONGLONG, 1),
                    # 62 : ResponderId is valid
                    ('ResponderIdValid', ULONGLONG, 1),
                    # 63 : Precise Instruction Pointer is Valid
                    ('PreciseIPValid', ULONGLONG, 1),
                ]
                _ERROR_CACHE_CHECK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


                _ERROR_CACHE_CHECK._fields_ = [
                    ('CacheCheck', ULONGLONG),
                    ('DUMMYSTRUCTNAME', _ERROR_CACHE_CHECK.DUMMYSTRUCTNAME),
                ]
            # END IF


            class _ERROR_TLB_CHECK_OPERATION(ENUM):
                TlbUnknownOp = 0
                TlbAccessWithLoad = 1
                TlbAccessWithStore = 2
                TlbAccessWithInstructionFetch = 3
                TlbAccessWithDataPrefetch = 4
                TlbShootDown = 5
                TlbProbe = 6
                TlbVhptFill = 7
                TlbPurge = 8

            ERROR_TLB_CHECK_OPERATION = _ERROR_TLB_CHECK_OPERATION


            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                # bits 0- 7: Slot number of Translation Register
                ('TRSlot', ULONGLONG, 8),
                # 8 : TRSlot field is valid
                ('TRSlotValid', ULONGLONG, 1),
                # 9
                ('Reserved1', ULONGLONG, 1),
                # 10-11: TLB Level
                ('Level', ULONGLONG, 2),
                # 12-15
                ('Reserved2', ULONGLONG, 4),
                # 16 : Error in data translation register
                ('DataTransReg', ULONGLONG, 1),
                # 17 : Error in instruction translation register
                ('InstructionTransReg', ULONGLONG, 1),
                # 18 : Error in data translation cache
                ('DataTransCache', ULONGLONG, 1),
                # 19 : Error in instruction translation cache
                ('InstructionTransCache', ULONGLONG, 1),
                # 20-23: Operation
                ('Operation', ULONGLONG, 4),
                # 24-53
                ('Reserved3', ULONGLONG, 30),
                # 54 : 0 - IA64 instruction, 1- IA32 instruction
                ('InstructionSet', ULONGLONG, 1),
                # 55 : InstructionSet field is valid
                ('InstructionSetValid', ULONGLONG, 1),
                # 56-57: Privilege level of instruction
                ('PrivilegeLevel', ULONGLONG, 2),
                # 58 : PrivilegeLevel field is Valid
                ('PrivilegeLevelValid', ULONGLONG, 1),
                # 59 : 1 - Machine Check Corrected
                ('MachineCheckCorrected', ULONGLONG, 1),
                # 60 : Target Address is valid
                ('TargetAddressValid', ULONGLONG, 1),
                # 61 : RequestId is valid
                ('RequestIdValid', ULONGLONG, 1),
                # 62 : ResponderId is valid
                ('ResponderIdValid', ULONGLONG, 1),
                # 63 : Precise Instruction Pointer is Valid
                ('PreciseIPValid', ULONGLONG, 1),
            ]
            _ERROR_TLB_CHECK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_TLB_CHECK._fields_ = [
                ('TlbCheck', ULONGLONG),
                ('DUMMYSTRUCTNAME', _ERROR_TLB_CHECK.DUMMYSTRUCTNAME),
            ]


            class _ERROR_BUS_CHECK_OPERATION(ENUM):
                BusUnknownOp = 0
                BusPartialRead = 1
                BusPartialWrite = 2
                BusFullLineRead = 3
                BusFullLineWrite = 4
                BusWriteBack = 5
                BusSnoopProbe = 6
                BusIncomingPtcG = 7
                BusWriteCoalescing = 8

            ERROR_BUS_CHECK_OPERATION = _ERROR_BUS_CHECK_OPERATION
            if NTDDI_VERSION >= NTDDI_VISTA:
                class DUMMYSTRUCTNAME(ctypes.Structure):
                    pass


                DUMMYSTRUCTNAME._fields_ = [
                    # bits 0- 4: Transaction size
                    ('Size', ULONGLONG, 5),
                    # 5 : Internal bus error
                    ('Internal', ULONGLONG, 1),
                    # 6 : External bus error
                    ('External', ULONGLONG, 1),
                    # 7 : Error occurred in Cache to Cache Transfer
                    ('CacheTransfer', ULONGLONG, 1),
                    # 8-15: Transaction type
                    ('Type', ULONGLONG, 8),
                    # 16-20: Error severity - platform specific
                    ('Severity', ULONGLONG, 5),
                    # 21-22: Level or Bus hierarchy
                    ('Hierarchy', ULONGLONG, 2),
                    # 23 : 1 - error due to data poisoning
                    ('DP', ULONGLONG, 1),
                    # 24-31: Bus error status - processor bus specific
                    ('Status', ULONGLONG, 8),
                    # 32-53
                    ('Reserved1', ULONGLONG, 22),
                    # 54 : 0 - IA64 instruction, 1- IA32 instruction
                    ('InstructionSet', ULONGLONG, 1),
                    # 55 : InstructionSet field is valid
                    ('InstructionSetValid', ULONGLONG, 1),
                    # 56-57: Privilege level of instruction
                    ('PrivilegeLevel', ULONGLONG, 2),
                    # 58 : PrivilegeLevel field is Valid
                    ('PrivilegeLevelValid', ULONGLONG, 1),
                    # 59 : 1 - Machine Check Corrected
                    ('MachineCheckCorrected', ULONGLONG, 1),
                    # 60 : Target Address is valid
                    ('TargetAddressValid', ULONGLONG, 1),
                    # 61 : RequestId is valid
                    ('RequestIdValid', ULONGLONG, 1),
                    # 62 : ResponderId is valid
                    ('ResponderIdValid', ULONGLONG, 1),
                    # 63 : Precise Instruction Pointer is Valid
                    ('PreciseIPValid', ULONGLONG, 1),
                ]
                _ERROR_BUS_CHECK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


                _ERROR_BUS_CHECK._fields_ = [
                    ('BusCheck', ULONGLONG),
                    ('DUMMYSTRUCTNAME', _ERROR_BUS_CHECK.DUMMYSTRUCTNAME),
                ]
            else:
                class DUMMYSTRUCTNAME(ctypes.Structure):
                    pass


                DUMMYSTRUCTNAME._fields_ = [
                    # bits 0- 4: Transaction size
                    ('Size', ULONGLONG, 5),
                    # 5 : Internal bus error
                    ('Internal', ULONGLONG, 1),
                    # 6 : External bus error
                    ('External', ULONGLONG, 1),
                    # 7 : Error occurred in Cache to Cache Transfer
                    ('CacheTransfer', ULONGLONG, 1),
                    # 8-15: Transaction type
                    ('Type', ULONGLONG, 8),
                    # 16-20: Error severity - platform specific
                    ('Severity', ULONGLONG, 5),
                    # 21-22: Level or Bus hierarchy
                    ('Hierarchy', ULONGLONG, 2),
                    # 23
                    ('Reserved1', ULONGLONG, 1),
                    # 24-31: Bus error status - processor bus specific
                    ('Status', ULONGLONG, 8),
                    # 32-53
                    ('Reserved2', ULONGLONG, 22),
                    # 54 : 0 - IA64 instruction, 1- IA32 instruction
                    ('InstructionSet', ULONGLONG, 1),
                    # 55 : InstructionSet field is valid
                    ('InstructionSetValid', ULONGLONG, 1),
                    # 56-57: Privilege level of instruction
                    ('PrivilegeLevel', ULONGLONG, 2),
                    # 58 : PrivilegeLevel field is Valid
                    ('PrivilegeLevelValid', ULONGLONG, 1),
                    # 59 : 1 - Machine Check Corrected
                    ('MachineCheckCorrected', ULONGLONG, 1),
                    # 60 : Target Address is valid
                    ('TargetAddressValid', ULONGLONG, 1),
                    # 61 : RequestId is valid
                    ('RequestIdValid', ULONGLONG, 1),
                    # 62 : ResponderId is valid
                    ('ResponderIdValid', ULONGLONG, 1),
                    # 63 : Precise Instruction Pointer is Valid
                    ('PreciseIPValid', ULONGLONG, 1),
                ]
                _ERROR_BUS_CHECK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


                _ERROR_BUS_CHECK._fields_ = [
                    ('BusCheck', ULONGLONG),
                    ('DUMMYSTRUCTNAME', _ERROR_BUS_CHECK.DUMMYSTRUCTNAME),
                ]
            # END IF


            class _ERROR_REGFILE_CHECK_IDENTIFIER(ENUM):
                RegFileUnknownId = 0
                GeneralRegisterBank1 = 1
                GeneralRegisterBank0 = 2
                FloatingPointRegister = 3
                BranchRegister = 4
                PredicateRegister = 5
                ApplicationRegister = 6
                ControlRegister = 7
                RegionRegister = 8
                ProtectionKeyRegister = 9
                DataBreakPointRegister = 10
                InstructionBreakPointRegister = 11
                PerformanceMonitorControlRegister = 12
                PerformanceMonitorDataRegister = 13

            ERROR_REGFILE_CHECK_IDENTIFIER = _ERROR_REGFILE_CHECK_IDENTIFIER


            class _ERROR_REGFILE_CHECK_OPERATION(ENUM):
                RegFileUnknownOp = 0
                RegFileRead = 1
                RegFileWrite = 2

            ERROR_REGFILE_CHECK_OPERATION = _ERROR_REGFILE_CHECK_OPERATION


            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                # bits 0- 3: Register file identifier
                ('Identifier', ULONGLONG, 4),
                # 4- 7: Operation that causes the MC event
                ('Operation', ULONGLONG, 4),
                # 8-14: Register number responsible for MC event
                ('RegisterNumber', ULONGLONG, 7),
                # 15 : Register number field is valid
                ('RegisterNumberValid', ULONGLONG, 1),
                # 16-53
                ('Reserved1', ULONGLONG, 38),
                # 54 : 0 - IA64 instruction, 1- IA32 instruction
                ('InstructionSet', ULONGLONG, 1),
                # 55 : InstructionSet field is valid
                ('InstructionSetValid', ULONGLONG, 1),
                # 56-57: Privilege level of instruction
                ('PrivilegeLevel', ULONGLONG, 2),
                # 58 : PrivilegeLevel field is Valid
                ('PrivilegeLevelValid', ULONGLONG, 1),
                # 59 : 1 - Machine Check Corrected
                ('MachineCheckCorrected', ULONGLONG, 1),
                # 60-62
                ('Reserved2', ULONGLONG, 3),
                # 63 : Precise Instruction Pointer is Valid
                ('PreciseIPValid', ULONGLONG, 1),
            ]
            _ERROR_REGFILE_CHECK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_REGFILE_CHECK._fields_ = [
                ('RegFileCheck', ULONGLONG),
                ('DUMMYSTRUCTNAME', _ERROR_REGFILE_CHECK.DUMMYSTRUCTNAME),
            ]

            if NTDDI_VERSION <= NTDDI_WINXP:
                class _ERROR_MS_CHECK_OPERATION(ENUM):
                    MsUnknownOp = 0
                    MsReadOrLoad = 1
                    MsWriteOrStore = 2

                ERROR_MS_CHECK_OPERATION = _ERROR_MS_CHECK_OPERATION
            else:
                class _ERROR_MS_CHECK_OPERATION(ENUM):
                    MsUnknownOp = 0
                    MsReadOrLoad = 1
                    MsWriteOrStore = 2
                    MsOverTemperature = 3
                    MsNormalTemperature = 4

                ERROR_MS_CHECK_OPERATION = _ERROR_MS_CHECK_OPERATION
            # END IF


            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                # bits 0- 4: Structure Identifier - impl. specific
                ('StructureIdentifier', ULONGLONG, 5),
                # 5- 7: Structure Level where error was generated
                ('Level', ULONGLONG, 3),
                # 8-11: Identification of the array
                ('ArrayId', ULONGLONG, 4),
                # 12-15: Operation
                ('Operation', ULONGLONG, 4),
                # 16-21: Way where the error was located
                ('Way', ULONGLONG, 6),
                # 22 : Way field is valid
                ('WayValid', ULONGLONG, 1),
                # 23 : Index field is valid
                ('IndexValid', ULONGLONG, 1),
                # 24-31
                ('Reserved1', ULONGLONG, 8),
                # 32-39: Index where the error was located
                ('Index', ULONGLONG, 8),
                # 40-53
                ('Reserved2', ULONGLONG, 14),
                # 54 : 0 - IA64 instruction, 1- IA32 instruction
                ('InstructionSet', ULONGLONG, 1),
                # 55 : InstructionSet field is valid
                ('InstructionSetValid', ULONGLONG, 1),
                # 56-57: Privilege level of instruction
                ('PrivilegeLevel', ULONGLONG, 2),
                # 58 : PrivilegeLevel field is Valid
                ('PrivilegeLevelValid', ULONGLONG, 1),
                # 59 : 1 - Machine Check Corrected
                ('MachineCheckCorrected', ULONGLONG, 1),
                # 60 : Target Address is valid
                ('TargetAddressValid', ULONGLONG, 1),
                # 61 : RequestId is valid
                ('RequestIdValid', ULONGLONG, 1),
                # 62 : ResponderId is valid
                ('ResponderIdValid', ULONGLONG, 1),
                # 63 : Precise Instruction Pointer is Valid
                ('PreciseIPValid', ULONGLONG, 1),
            ]
            _ERROR_MS_CHECK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_MS_CHECK._fields_ = [
                ('MsCheck', ULONGLONG),
                ('DUMMYSTRUCTNAME', _ERROR_MS_CHECK.DUMMYSTRUCTNAME),
            ]

            _ERROR_CHECK_INFO._fields_ = [
                ('CheckInfo', ULONGLONG),
                ('CacheCheck', ERROR_CACHE_CHECK),
                ('TlbCheck', ERROR_TLB_CHECK),
                ('BusCheck', ERROR_BUS_CHECK),
                ('RegFileCheck', ERROR_REGFILE_CHECK),
                ('MsCheck', ERROR_MS_CHECK),
            ]

            # SAL Specs July 2000: The size of _ERROR_MODINFO will always be
            # 48 Bytes.
            _ERROR_MODINFO._fields_ = [
                ('Valid', ERROR_MODINFO_VALID),
                ('CheckInfo', ERROR_CHECK_INFO),
                ('RequestorId', ULONGLONG),
                ('ResponderId', ULONGLONG),
                ('TargetId', ULONGLONG),
                ('PreciseIP', ULONGLONG),
            ]

            # 0:
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('ErrorMap', ULONGLONG, 1),
                # 1:
                ('StateParameter', ULONGLONG, 1),
                # 2:
                ('CRLid', ULONGLONG, 1),
                # 3: Processor Static Info error.
                ('StaticStruct', ULONGLONG, 1),
                # 4-7: Cache errors.
                ('CacheCheckNum', ULONGLONG, 4),
                # 8-11: Tlb errors.
                ('TlbCheckNum', ULONGLONG, 4),
                # 12-15: Bus errors.
                ('BusCheckNum', ULONGLONG, 4),
                # 16-19: Registers file errors.
                ('RegFileCheckNum', ULONGLONG, 4),
                # 20-23: Micro-Architecture errors.
                ('MsCheckNum', ULONGLONG, 4),
                # 24: CPUID Info.
                ('CpuIdInfo', ULONGLONG, 1),
                # 25-63: Reserved.
                ('Reserved', ULONGLONG, 39),
            ]
            _ERROR_PROCESSOR_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_PROCESSOR_VALID._fields_ = [
                ('Valid', ULONGLONG),
                # Bits
                ('DUMMYSTRUCTNAME', _ERROR_PROCESSOR_VALID.DUMMYSTRUCTNAME),
            ]

            # bits 0- 3: Processor Core Identifier
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('Cid', ULONGLONG, 4),
                # 4- 7: Logical Thread Identifier
                ('Tid', ULONGLONG, 4),
                # 8-11: Instruction Caches Level Information
                ('Eic', ULONGLONG, 4),
                # 12-15: Data Caches Level Information
                ('Edc', ULONGLONG, 4),
                # 16-19: Instruction TLB Level Information
                ('Eit', ULONGLONG, 4),
                # 20-23: Data TLB Level Information
                ('Edt', ULONGLONG, 4),
                # 24-27: Processor Bus Level Information
                ('Ebh', ULONGLONG, 4),
                # 28-31: Register File Level Information
                ('Erf', ULONGLONG, 4),
                # 32-47: MicroArchitecture Level Information
                ('Ems', ULONGLONG, 16),
                ('Reserved', ULONGLONG, 16),
            ]
            _ERROR_PROCESSOR_ERROR_MAP.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_PROCESSOR_ERROR_MAP._fields_ = [
                ('ErrorMap', ULONGLONG),
                ('DUMMYSTRUCTNAME', _ERROR_PROCESSOR_ERROR_MAP.DUMMYSTRUCTNAME),
            ]
            _ERROR_PROCESSOR_LEVEL_INDEX = ERROR_PROCESSOR_ERROR_MAP
            ERROR_PROCESSOR_LEVEL_INDEX = _ERROR_PROCESSOR_LEVEL_INDEX
            PERROR_PROCESSOR_LEVEL_INDEX = POINTER(_ERROR_PROCESSOR_LEVEL_INDEX)

            # 0-1 : reserved
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('reserved0', ULONGLONG, 2),
                # 2 : Rendezvous successful
                ('rz', ULONGLONG, 1),
                # 3 : Rendezvous attempted
                ('ra', ULONGLONG, 1),
                # 4 : Distinct Multiple errors
                ('me', ULONGLONG, 1),
                # 5 : Min-state Save Area registered
                ('mn', ULONGLONG, 1),
                # 6 : Storage integrity synchronized
                ('sy', ULONGLONG, 1),
                # 7 : Continuable
                ('co', ULONGLONG, 1),
                # 8 : Machine Check isolated
                ('ci', ULONGLONG, 1),
                # 9 : Uncontained Storage damage
                ('us', ULONGLONG, 1),
                # 10 : Hardware damage
                ('hd', ULONGLONG, 1),
                # 11 : Trap lost
                ('tl', ULONGLONG, 1),
                # 12 : More Information
                ('mi', ULONGLONG, 1),
                # 13 : Precise Instruction pointer
                ('pi', ULONGLONG, 1),
                # 14 : Precise Min-state Save Area
                ('pm', ULONGLONG, 1),
                # 15 : Processor Dynamic State valid
                ('dy', ULONGLONG, 1),
                # 16 : INIT interruption
                ('in', ULONGLONG, 1),
                # 17 : RSE valid
                ('rs', ULONGLONG, 1),
                # 18 : Machine Check corrected
                ('cm', ULONGLONG, 1),
                # 19 : Machine Check expected
                ('ex', ULONGLONG, 1),
                # 20 : Control Registers valid
                ('cr', ULONGLONG, 1),
                # 21 : Performance Counters valid
                ('pc', ULONGLONG, 1),
                # 22 : Debug Registers valid
                ('dr', ULONGLONG, 1),
                # 23 : Translation Registers valid
                ('tr', ULONGLONG, 1),
                # 24 : Region Registers valid
                ('rr', ULONGLONG, 1),
                # 25 : Application Registers valid
                ('ar', ULONGLONG, 1),
                # 26 : Branch Registers valid
                ('br', ULONGLONG, 1),
                # 27 : Predicate Registers valid
                ('pr', ULONGLONG, 1),
                # 28 : Floating-Point Registers valid
                ('fp', ULONGLONG, 1),
                # 29 : Preserved Bank 1 General Registers valid
                ('b1', ULONGLONG, 1),
                # 30 : Preserved Bank 0 General Registers valid
                ('b0', ULONGLONG, 1),
                # 31 : General Registers valid
                ('gr', ULONGLONG, 1),
                # 47-32 : Processor Dynamic State size
                ('dsize', ULONGLONG, 16),
                # 48-58 : reserved
                ('reserved1', ULONGLONG, 11),
                # 59 : Cache Check
                ('cc', ULONGLONG, 1),
                # 60 : TLB Check
                ('tc', ULONGLONG, 1),
                # 61 : Bus Check
                ('bc', ULONGLONG, 1),
                # 62 : Register File Check
                ('rc', ULONGLONG, 1),
                # 63 : Micro-Architectural Check
                ('uc', ULONGLONG, 1),
            ]
            _ERROR_PROCESSOR_STATE_PARAMETER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_PROCESSOR_STATE_PARAMETER._fields_ = [
                ('StateParameter', ULONGLONG),
                ('DUMMYSTRUCTNAME', _ERROR_PROCESSOR_STATE_PARAMETER.DUMMYSTRUCTNAME),
            ]

            # 0-16 : reserved
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('reserved', ULONGLONG, 16),
                # 16-23 : Extended Id
                ('eid', ULONGLONG, 8),
                # 24-31 : Id
                ('id', ULONGLONG, 8),
                # 32-63 : ignored
                ('ignored', ULONGLONG, 32),
            ]
            _PROCESSOR_LOCAL_ID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _PROCESSOR_LOCAL_ID._fields_ = [
                ('LocalId', ULONGLONG),
                ('DUMMYSTRUCTNAME', _PROCESSOR_LOCAL_ID.DUMMYSTRUCTNAME),
            ]

            # pedef struct _ERROR_PROCESSOR_MS

            _ERROR_PROCESSOR_MS._fields_ = [
                ('MsError', ULONGLONG * 1) # 0 -> 15 registers file errors.
            ]

            _ERROR_PROCESSOR_CPUID_INFO._fields_ = [
                ('CpuId0', ULONGLONG),
                ('CpuId1', ULONGLONG),
                ('CpuId2', ULONGLONG),
                ('CpuId3', ULONGLONG),
                ('CpuId4', ULONGLONG),
                ('Reserved', ULONGLONG),
            ]

            # Warning: Match the VALID fields with the
            # _ERROR_PROCESSOR_STATIC_INFO members.
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                # 0: MinState valid.
                ('MinState', ULONGLONG, 1),
                # 1: Branch Registers valid.
                ('BR', ULONGLONG, 1),
                # 2: Control Registers valid.
                ('CR', ULONGLONG, 1),
                # 3: Application Registers valid.
                ('AR', ULONGLONG, 1),
                # 4: Registers valid.
                ('RR', ULONGLONG, 1),
                # 5: Registers valid.
                ('FR', ULONGLONG, 1),
                # 6-63: Reserved.
                ('Reserved', ULONGLONG, 58),
            ]
            _ERROR_PROCESSOR_STATIC_INFO_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_PROCESSOR_STATIC_INFO_VALID._fields_ = [
                ('Valid', ULONGLONG),
                # Bits
                ('DUMMYSTRUCTNAME', _ERROR_PROCESSOR_STATIC_INFO_VALID.DUMMYSTRUCTNAME),
            ]

            _ERROR_PROCESSOR_STATIC_INFO._fields_ = [
                ('Valid', ERROR_PROCESSOR_STATIC_INFO_VALID),
                # SAL Specs, July 2000 and Jan 2001 state approximatively:
                ('MinState', UCHAR * 1024),
                ('BR', ULONGLONG * 8),
                # SAL Specs, July 2000 states that it is processor dependent
                ('CR', ULONGLONG * 128),
                # SAL Specs, July 2000 states that it is processor dependent
                ('AR', ULONGLONG * 128),
                ('RR', ULONGLONG * 8),
                ('FR', ULONGLONG * 2 * 128),
            ]

            _TEMP__ERROR_PROCESSOR = [
                ('Header', ERROR_SECTION_HEADER),
                ('Valid', ERROR_PROCESSOR_VALID),
                ('ErrorMap', ERROR_PROCESSOR_ERROR_MAP),
                ('StateParameter', ERROR_PROCESSOR_STATE_PARAMETER),
                ('CRLid', PROCESSOR_LOCAL_ID),
            ]
            if _FIXFIX_:
                _TEMP__ERROR_PROCESSOR += [
                    # field will always be there but could be zero-padded.
                    ('CpuIdInfo', ERROR_PROCESSOR_CPUID_INFO),
                    # field will always be there but could be zero-padded.
                    ('StaticInfo', ERROR_PROCESSOR_STATIC_INFO),
                ]
            # END IF   0


            _ERROR_PROCESSOR._fields_ = _TEMP__ERROR_PROCESSOR


            # IA64 ERROR PROCESSOR State Parameter - GR18 - definitions.
            ERROR_PROCESSOR_STATE_PARAMETER_CACHE_CHECK_SHIFT = 59
            ERROR_PROCESSOR_STATE_PARAMETER_CACHE_CHECK_MASK = 0x1
            ERROR_PROCESSOR_STATE_PARAMETER_TLB_CHECK_SHIFT = 60
            ERROR_PROCESSOR_STATE_PARAMETER_TLB_CHECK_MASK = 0x1
            ERROR_PROCESSOR_STATE_PARAMETER_BUS_CHECK_SHIFT = 61
            ERROR_PROCESSOR_STATE_PARAMETER_BUS_CHECK_MASK = 0x1
            ERROR_PROCESSOR_STATE_PARAMETER_REG_CHECK_SHIFT = 62
            ERROR_PROCESSOR_STATE_PARAMETER_REG_CHECK_MASK = 0x1
            ERROR_PROCESSOR_STATE_PARAMETER_MICROARCH_CHECK_SHIFT = 63
            ERROR_PROCESSOR_STATE_PARAMETER_MICROARCH_CHECK_MASK = 0x1


            # For legacy consumers
            ERROR_PROCESSOR_STATE_PARAMETER_UNKNOWN_CHECK_SHIFT = (
                ERROR_PROCESSOR_STATE_PARAMETER_MICROARCH_CHECK_SHIFT
            )
            ERROR_PROCESSOR_STATE_PARAMETER_UNKNOWN_CHECK_MASK = (
                ERROR_PROCESSOR_STATE_PARAMETER_MICROARCH_CHECK_MASK
            )

            # //////////////////////////////////////////////////////////////////
            #
            # IA64 PLATFORM ERRORS Definitions
            # We tried to respect the order in which these error devices are
            # presented in the SAL specs.
            # IA64 ERRORS: _ERR_TYPE definitions
            # Warning 04/01/01: "ERR_TYPE" or "ERROR_TYPE" are already used in
            # the NT namespace.
            class _ERR_TYPES(ENUM):
                ERR_INTERNAL = 1
                ERR_BUS = 16
                ERR_MEM = 4
                ERR_TLB = 5
                ERR_CACHE = 6
                ERR_FUNCTION = 7
                ERR_SELFTEST = 8
                ERR_FLOW = 9
                ERR_MAP = 17
                ERR_IMPROPER = 18

                # Access to a memory address which is not mapped to any
                # component
                ERR_UNIMPL = 19
                ERR_LOL = 20
                ERR_RESPONSE = 21
                ERR_PARITY = 22
                ERR_PROTOCOL = 23
                ERR_ERROR = 24
                ERR_TIMEOUT = 25
                ERR_POISONED = 26

            _ERR_TYPE = _ERR_TYPES

            # IA64 ERRORS: ERROR_STATUS definitions
            # 7-0: Reserved
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('Reserved0', ULONGLONG, 8),
                # 15-8: Error Type - See _ERR_TYPE definitions.
                ('Type', ULONGLONG, 8),
                # 16: Error was detected on address signals or on address
                # portion of transaction
                ('Address', ULONGLONG, 1),
                # 17: Error was detected on control signals or in control
                # portion of transaction
                ('Control', ULONGLONG, 1),
                # 18: Error was detected on data signals or in data portion of
                # transaction
                ('Data', ULONGLONG, 1),
                # 19: Error was detected by responder of transaction
                ('Responder', ULONGLONG, 1),
                # 20: Error was detected by requester of transaction
                ('Requestor', ULONGLONG, 1),
                # 21: If multiple errors, this is the first error of the
                # highest severity that occurred
                ('FirstError', ULONGLONG, 1),
                # 22: Additional errors occurred which were not logged because
                # registers overflow
                ('Overflow', ULONGLONG, 1),
                # 63-23: Reserved
                ('Reserved1', ULONGLONG, 41),
            ]
            _ERROR_STATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_STATUS._fields_ = [
                ('Status', ULONGLONG),
                # Bits:
                ('DUMMYSTRUCTNAME', _ERROR_STATUS.DUMMYSTRUCTNAME),
            ]

            # IA64 ERRORS: Platform OEM_DATA definitions
            _TEMP__ERROR_OEM_DATA = [
                ('Length', USHORT),
            ]
            if _FIXFIX_:
                _TEMP__ERROR_OEM_DATA += [
                    # ERROR_OEM_DATA.Length
                    ('Data', UCHAR * 0),
                ]
            # END IF   0


            _ERROR_OEM_DATA._fields_ = _TEMP__ERROR_OEM_DATA

            # IA64 ERRORS: Platform BUS_SPECIFIC_DATA definitions
            # 0: LOCK Asserted during request phase
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('LockAsserted', ULONGLONG, 1),
                # 1: Defer phase is logged
                ('DeferLogged', ULONGLONG, 1),
                # 2: IOQ is empty
                ('IOQEmpty', ULONGLONG, 1),
                # 3: Component interface deferred transaction
                ('DeferredTransaction', ULONGLONG, 1),
                # 4: Component interface retried transaction
                ('RetriedTransaction', ULONGLONG, 1),
                # 5: memory claimed the transaction
                ('MemoryClaimedTransaction', ULONGLONG, 1),
                # 6: IO controller claimed the transaction
                ('IOClaimedTransaction', ULONGLONG, 1),
                # 7: Response parity signal
                ('ResponseParitySignal', ULONGLONG, 1),
                # 8: DEFER signal
                ('DeferSignal', ULONGLONG, 1),
                # 9: HITM signal
                ('HitMSignal', ULONGLONG, 1),
                # 10: HIT signal
                ('HitSignal', ULONGLONG, 1),
                # 16-11: First cycle of request bus
                ('RequestBusFirstCycle', ULONGLONG, 6),
                # 22-17: Second cycle of request bus
                ('RequestBusSecondCycle', ULONGLONG, 6),
                # 24-23: First cycle of address parity bus
                ('AddressParityBusFirstCycle', ULONGLONG, 2),
                # 26-25: Second cycle of address parity
                ('AddressParityBusSecondCycle', ULONGLONG, 2),
                # 29-27: Response bus
                ('ResponseBus', ULONGLONG, 3),
                # 30: First cycle of request parity signal
                ('RequestParitySignalFirstCycle', ULONGLONG, 1),
                # 31: Second cycle of request parity signal
                ('RequestParitySignalSecondCycle', ULONGLONG, 1),
                # 63-32: Reserved
                ('Reserved', ULONGLONG, 32),
            ]
            _ERROR_BUS_SPECIFIC_DATA.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_BUS_SPECIFIC_DATA._fields_ = [
                ('BusSpecificData', ULONGLONG),
                # Bits :
                ('DUMMYSTRUCTNAME', _ERROR_BUS_SPECIFIC_DATA.DUMMYSTRUCTNAME),
            ]

            # IA64 ERRORS: Platform ERROR_MEMORY device definitions
            # With reference to the ACPI Memory Device.
            ERROR_MEMORY_GUID = (
                0xE429FAF2,
                0x3CB7,
                0x11D4,
                [0xBC, 0xA7, 0x0, 0x80, 0xC7, 0x3C, 0x88, 0x81]
            )


            # 0: Error Status valid bit
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('ErrorStatus', ULONGLONG, 1),
                # 1: Physical Address valid bit
                ('PhysicalAddress', ULONGLONG, 1),
                # 2: Address Mask bit
                ('AddressMask', ULONGLONG, 1),
                # 3: Node valid bit
                ('Node', ULONGLONG, 1),
                # 4: Card valid bit
                ('Card', ULONGLONG, 1),
                # 5: Module valid bit
                ('Module', ULONGLONG, 1),
                # 6: Bank valid bit
                ('Bank', ULONGLONG, 1),
                # 7: Device valid bit
                ('Device', ULONGLONG, 1),
                # 8: Row valid bit
                ('Row', ULONGLONG, 1),
                # 9: Column valid bit
                ('Column', ULONGLONG, 1),
                # 10: Bit Position valid bit
                ('BitPosition', ULONGLONG, 1),
                # 11: Platform Requester Id valid bit
                ('RequestorId', ULONGLONG, 1),
                # 12: Platform Responder Id valid bit
                ('ResponderId', ULONGLONG, 1),
                # 13: Platform Target Id valid bit
                ('TargetId', ULONGLONG, 1),
                # 14: Platform Bus specific data valid bit
                ('BusSpecificData', ULONGLONG, 1),
                # 15: Platform OEM id valid bit
                ('OemId', ULONGLONG, 1),
                # 16: Platform OEM data valid bit
                ('OemData', ULONGLONG, 1),
                # 63-17: Reserved
                ('Reserved', ULONGLONG, 47),
            ]
            _ERROR_MEMORY_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_MEMORY_VALID._fields_ = [
                ('Valid', ULONGLONG),
                # Bits
                ('DUMMYSTRUCTNAME', _ERROR_MEMORY_VALID.DUMMYSTRUCTNAME),
            ]

            _ERROR_MEMORY._fields_ = [
                ('Header', ERROR_SECTION_HEADER),
                ('Valid', ERROR_MEMORY_VALID),
                # Memory device error status fields - See ERROR_STATUS defs.
                ('ErrorStatus', ERROR_STATUS),
                # Physical Address of the memory error
                ('PhysicalAddress', ULONGLONG),
                # Valid bits for Physical Address
                ('PhysicalAddressMask', ULONGLONG),
                # Node identifier in a multi-node system
                ('Node', USHORT),
                # Card number of the memory error location
                ('Card', USHORT),
                # Module number of the memory error location
                ('Module', USHORT),
                # Bank number of the memory error location
                ('Bank', USHORT),
                # Device number of the memory error location
                ('Device', USHORT),
                # Row number of the memory error location
                ('Row', USHORT),
                # Column number of the memory error location
                ('Column', USHORT),
                # Bit within the word that is in error
                ('BitPosition', USHORT),
                # Hardware address of the device or component initiating
                # transaction
                ('RequestorId', ULONGLONG),
                # Hardware address of the responder to transaction
                ('ResponderId', ULONGLONG),
                # Hardware address of intended target of transaction
                ('TargetId', ULONGLONG),
                # Bus dependent data of the on-board processor. It is a OEM
                # specific field.
                ('BusSpecificData', ULONGLONG),
                # OEM defined identification for memory controller
                ('OemId', UCHAR * 16),
                # OEM platform specific data.
                ('OemData', ERROR_OEM_DATA),
            ]


            # IA64 ERRORS: Platform ERROR_PCI_BUS device definitions
            # With reference to the PCI Specifications.
            ERROR_PCI_BUS_GUID = (
                0xE429FAF4,
                0x3CB7,
                0x11D4,
                [0xBC, 0xA7, 0x0, 0x80, 0xC7, 0x3C, 0x88, 0x81]
            )


            # 0: Error Status   valid bit
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('ErrorStatus', ULONGLONG, 1),
                # 1: Error Type valid bit
                ('ErrorType', ULONGLONG, 1),
                # 2: Identifier valid bit
                ('Id', ULONGLONG, 1),
                # 3: Address valid bit
                ('Address', ULONGLONG, 1),
                # 4: Data valid bit
                ('Data', ULONGLONG, 1),
                # 5: Command Type valid bit
                ('CmdType', ULONGLONG, 1),
                # 6: Requester Identifier valid bit
                ('RequestorId', ULONGLONG, 1),
                # 7: Responder Identifier valid bit
                ('ResponderId', ULONGLONG, 1),
                # 8: Target Identifier valid bit
                ('TargetId', ULONGLONG, 1),
                # 9: OEM Identification valid bit
                ('OemId', ULONGLONG, 1),
                # 10: OEM Data valid bit
                ('OemData', ULONGLONG, 1),
                # 11-63: Reserved
                ('Reserved', ULONGLONG, 53),
            ]
            _ERROR_PCI_BUS_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_PCI_BUS_VALID._fields_ = [
                ('Valid', ULONGLONG),
                # Bits
                ('DUMMYSTRUCTNAME', _ERROR_PCI_BUS_VALID.DUMMYSTRUCTNAME),
            ]

            _ERROR_PCI_BUS_TYPE._fields_ = [
                ('Type', UCHAR),
                ('Reserved', UCHAR),
            ]
            PciBusUnknownError = 0
            PciBusDataParityError = 1
            PciBusSystemError = 2
            PciBusMasterAbort = 3
            PciBusTimeOut = 4
            PciMasterDataParityError = 5
            PciAddressParityError = 6
            PciCommandParityError = 7

            # PciOtherErrors   Reserved
            # Bus  Number
            _ERROR_PCI_BUS_ID._fields_ = [
                ('BusNumber', UCHAR),
                # Segment Number
                ('SegmentNumber', UCHAR),
            ]

            _ERROR_PCI_BUS._fields_ = [
                ('Header', ERROR_SECTION_HEADER),
                ('Valid', ERROR_PCI_BUS_VALID),
                # PCI Bus Error Status - See ERROR_STATUS definitions.
                ('ErrorStatus', ERROR_STATUS),
                # PCI Bus Error Type
                ('Type', ERROR_PCI_BUS_TYPE),
                # PCI Bus Identifier
                ('Id', ERROR_PCI_BUS_ID),
                # Reserved
                ('Reserved', UCHAR * 4),
                # Memory or IO Address on the PCI bus at
                ('Address', ULONGLONG),
                # Data on the PCI bus at time of the event
                ('Data', ULONGLONG),
                # Bus Command or Operation at time of the event
                ('CmdType', ULONGLONG),
                # Bus Requester Identifier at time of the event
                ('RequestorId', ULONGLONG),
                # Bus Responder Identifier at time of the event
                ('ResponderId', ULONGLONG),
                # Intended Bus Target Identifier at time of the event
                ('TargetId', ULONGLONG),
                # OEM defined identification for pci bus
                ('OemId', UCHAR * 16),
                # OEM specific data.
                ('OemData', ERROR_OEM_DATA),
            ]

            # IA64 ERRORS: Platform ERROR_PCI_COMPONENT device definitions
            # With reference to the PCI Specifications.
            ERROR_PCI_COMPONENT_GUID = (
                0xE429FAF6,
                0x3CB7,
                0x11D4,
                [0xBC, 0xA7, 0x0, 0x80, 0xC7, 0x3C, 0x88, 0x81],

            )


            # 0: Error Status valid bit
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('ErrorStatus', ULONGLONG, 1),
                # 1: Information valid bit
                ('Info', ULONGLONG, 1),
                # 2: Number of Memory Mapped Registers Pairs valid bit
                ('MemoryMappedRegistersPairs', ULONGLONG, 1),
                # 3: Number of Programmed IO Registers Pairs valid bit
                ('ProgrammedIORegistersPairs', ULONGLONG, 1),
                # 4: Memory Mapped Registers Pairs valid bit
                ('RegistersDataPairs', ULONGLONG, 1),
                # 5: OEM Data valid bit.
                ('OemData', ULONGLONG, 1),
                # 63-6: Reserved
                ('Reserved', ULONGLONG, 58),
            ]
            _ERROR_PCI_COMPONENT_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_PCI_COMPONENT_VALID._fields_ = [
                ('Valid', ULONGLONG),
                # Bits:
                ('DUMMYSTRUCTNAME', _ERROR_PCI_COMPONENT_VALID.DUMMYSTRUCTNAME),
            ]

            # 0-1: Vendor Identifier
            _ERROR_PCI_COMPONENT_INFO._fields_ = [
                ('VendorId', USHORT),
                # 2-3: Device Identifier
                ('DeviceId', USHORT),
                # 4: Class Code.Interface field
                ('ClassCodeInterface', UCHAR),
                # 5: Class Code.SubClass field
                ('ClassCodeSubClass', UCHAR),
                # 6: Class Code.BaseClass field
                ('ClassCodeBaseClass', UCHAR),
                # 7: Function Number
                ('FunctionNumber', UCHAR),
                # 8: Device Number
                ('DeviceNumber', UCHAR),
                # 9: Bus Number
                ('BusNumber', UCHAR),
                # 10: Segment Number
                ('SegmentNumber', UCHAR),
                ('Reserved0', UCHAR),
                ('Reserved1', ULONG),
            ]

            _TEMP__ERROR_PCI_COMPONENT = [
                ('Header', ERROR_SECTION_HEADER),
                ('Valid', ERROR_PCI_COMPONENT_VALID),
                # Component Error Status
                ('ErrorStatus', ERROR_STATUS),
                # Component Information
                ('Info', ERROR_PCI_COMPONENT_INFO),
                # Number of Memory Mapped Registers Pairs
                ('MemoryMappedRegistersPairs', ULONG),
                # Number of Programmed IO Registers Pairs
                ('ProgrammedIORegistersPairs', ULONG),
            ]
            if _FIXFIX_:
                _TEMP__ERROR_PCI_COMPONENT += [
                    # 2 *
                    # (MemoryMappedRegistersPairs + ProgrammedIORegistersPairs)
                    ('RegistersPairs', ULONGLONG * 0),
                    ('OemData', ERROR_OEM_DATA),
                ]
            # END IF   0

            _ERROR_PCI_COMPONENT._fields_ = _TEMP__ERROR_PCI_COMPONENT


            # IA64 ERRORS: Platform ERROR_SYSTEM_EVENT_LOG device definitions
            # With reference to the IPMI System Event Log.
            ERROR_SYSTEM_EVENT_LOG_GUID = (
                0xE429FAF3,
                0x3CB7,
                0x11D4,
                [0xBC, 0xA7, 0x0, 0x80, 0xC7, 0x3C, 0x88, 0x81]
            )


            # 0: Record Identifier  valid bit
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('RecordId', ULONGLONG, 1),
                # 1: Record Type valid bit
                ('RecordType', ULONGLONG, 1),
                # 2: Generator Identifier valid bit
                ('GeneratorId', ULONGLONG, 1),
                # 3: Event Format Revision valid bit
                ('EVMRev', ULONGLONG, 1),
                # 4: Sensor Type valid bit
                ('SensorType', ULONGLONG, 1),
                # 5: Sensor Number valid bit
                ('SensorNum', ULONGLONG, 1),
                # 6: Event Dir valid bit
                ('EventDirType', ULONGLONG, 1),
                # 7: Event Data1 valid bit
                ('EventData1', ULONGLONG, 1),
                # 8: Event Data2 valid bit
                ('EventData2', ULONGLONG, 1),
                # 9: Event Data3 valid bit
                ('EventData3', ULONGLONG, 1),
                # 10-63:
                ('Reserved', ULONGLONG, 54),
            ]
            _ERROR_SYSTEM_EVENT_LOG_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_SYSTEM_EVENT_LOG_VALID._fields_ = [
                ('Valid', ULONGLONG),
                # Bits
                ('DUMMYSTRUCTNAME', _ERROR_SYSTEM_EVENT_LOG_VALID.DUMMYSTRUCTNAME),
            ]

            _ERROR_SYSTEM_EVENT_LOG._fields_ = [
                ('Header', ERROR_SECTION_HEADER),
                ('Valid', ERROR_SYSTEM_EVENT_LOG_VALID),
                # Record Identifier used for SEL record access
                ('RecordId', USHORT),
                # Record Type:
                ('RecordType', UCHAR),
                # Time stamp of the event log
                ('TimeStamp', ULONG),
                # Software ID if event was generated by software
                ('GeneratorId', USHORT),
                # Error message format version
                ('EVMRevision', UCHAR),
                # Sensor Type code of the sensor that generated event
                ('SensorType', UCHAR),
                # Number of the sensor that generated event
                ('SensorNumber', UCHAR),
                # Event Dir
                ('EventDir', UCHAR),
                # Event data field
                ('Data1', UCHAR),
                # Event data field
                ('Data2', UCHAR),
                # Event data field
                ('Data3', UCHAR),
            ]

            # IA64 ERRORS: Platform ERROR_SMBIOS device definitions
            # With reference to the SMBIOS Specifications.
            ERROR_SMBIOS_GUID = (
                0xE429FAF5,
                0x3CB7,
                0x11D4,
                [0xBC, 0xA7, 0x0, 0x80, 0xC7, 0x3C, 0x88, 0x81],
            )


            # 0: Event Type valid bit
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('EventType', ULONGLONG, 1),
                # 1: Length valid bit
                ('Length', ULONGLONG, 1),
                # 2: Time Stamp valid bit
                ('TimeStamp', ULONGLONG, 1),
                # 3: Data valid bit
                ('OemData', ULONGLONG, 1),
                # 4-63:
                ('Reserved', ULONGLONG, 60),
            ]
            _ERROR_SMBIOS_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_SMBIOS_VALID._fields_ = [
                ('Valid', ULONGLONG),
                # Bits
                ('DUMMYSTRUCTNAME', _ERROR_SMBIOS_VALID.DUMMYSTRUCTNAME),
            ]


            # ERROR_SMBIOS.Type definitions
            ERROR_SMBIOS_EVENT_TYPE = UCHAR
            PERROR_SMBIOS_EVENT_TYPE = POINTER(UCHAR)

            # enum values defined in SMBIOS 2.3 - 3.3.16.6.1
            _ERROR_SMBIOS._fields_ = [
                ('Header', ERROR_SECTION_HEADER),
                ('Valid', ERROR_SMBIOS_VALID),
                # Event Type
                ('EventType', ERROR_SMBIOS_EVENT_TYPE),
                # Length of the error information in bytes
                ('Length', UCHAR),
                # Event Time Stamp
                ('TimeStamp', ERROR_TIMESTAMP),
                # Optional data validated by SMBIOS.Valid.Data.
                ('OemData', ERROR_OEM_DATA),
            ]


            # IA64 ERRORS: Platform Specific error device definitions
            ERROR_PLATFORM_SPECIFIC_GUID = (
                0xE429FAF7,
                0x3CB7,
                0x11D4,
                [0xBC, 0xA7, 0x0, 0x80, 0xC7, 0x3C, 0x88, 0x81]
            )


            # 0: Error Status  valid bit
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('ErrorStatus', ULONGLONG, 1),
                # 1: Requester Identifier valid bit
                ('RequestorId', ULONGLONG, 1),
                # 2: Responder Identifier valid bit
                ('ResponderId', ULONGLONG, 1),
                # 3: Target Identifier valid bit
                ('TargetId', ULONGLONG, 1),
                # 4: Bus Specific Data valid bit
                ('BusSpecificData', ULONGLONG, 1),
                # 5: OEM Identification valid bit
                ('OemId', ULONGLONG, 1),
                # 6: OEM Data valid bit
                ('OemData', ULONGLONG, 1),
                # 7: OEM Device Path valid bit
                ('OemDevicePath', ULONGLONG, 1),
                # 63-8: Reserved
                ('Reserved', ULONGLONG, 56),
            ]
            _ERROR_PLATFORM_SPECIFIC_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_PLATFORM_SPECIFIC_VALID._fields_ = [
                ('Valid', ULONGLONG),
                # Bits:
                ('DUMMYSTRUCTNAME', _ERROR_PLATFORM_SPECIFIC_VALID.DUMMYSTRUCTNAME),
            ]

            _TEMP__ERROR_PLATFORM_SPECIFIC = [
                ('Header', ERROR_SECTION_HEADER),
                ('Valid', ERROR_PLATFORM_SPECIFIC_VALID),
                # Platform Generic Error Status
                ('ErrorStatus', ERROR_STATUS),
                # Bus Requester ID at the time of the event
                ('RequestorId', ULONGLONG),
                # Bus Responder ID at the time of the event
                ('ResponderId', ULONGLONG),
                # Bus intended Target ID at the time of the event
                ('TargetId', ULONGLONG),
                # OEM specific Bus dependent data
                ('BusSpecificData', ERROR_BUS_SPECIFIC_DATA),
                # OEM specific data for bus identification
                ('OemId', UCHAR * 16),
                # OEM specific data
                ('OemData', ERROR_OEM_DATA),
            ]

            _ERROR_PLATFORM_SPECIFIC._fields_ = _TEMP__ERROR_PLATFORM_SPECIFIC


            # IA64 ERRORS: Platform Bus error device definitions
            ERROR_PLATFORM_BUS_GUID = (
                0xE429FAF9,
                0x3CB7,
                0x11D4,
                [0xBC, 0xA7, 0x0, 0x80, 0xC7, 0x3C, 0x88, 0x81]
            )


            # 0: Error Status  valid bit
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('ErrorStatus', ULONGLONG, 1),
                # 1: Requester Identifier valid bit
                ('RequestorId', ULONGLONG, 1),
                # 2: Responder Identifier valid bit
                ('ResponderId', ULONGLONG, 1),
                # 3: Target Identifier valid bit
                ('TargetId', ULONGLONG, 1),
                # 4: Bus Specific Data valid bit
                ('BusSpecificData', ULONGLONG, 1),
                # 5: OEM Identification valid bit
                ('OemId', ULONGLONG, 1),
                # 6: OEM Data valid bit
                ('OemData', ULONGLONG, 1),
                # 7: OEM Device Path valid bit
                ('OemDevicePath', ULONGLONG, 1),
                # 63-8: Reserved
                ('Reserved', ULONGLONG, 56),
            ]
            _ERROR_PLATFORM_BUS_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_PLATFORM_BUS_VALID._fields_ = [
                ('Valid', ULONGLONG),
                # Bits:
                ('DUMMYSTRUCTNAME', _ERROR_PLATFORM_BUS_VALID.DUMMYSTRUCTNAME),
            ]

            _TEMP__ERROR_PLATFORM_BUS = [
                ('Header', ERROR_SECTION_HEADER),
                ('Valid', ERROR_PLATFORM_BUS_VALID),
                # Bus Error Status
                ('ErrorStatus', ERROR_STATUS),
                # Bus Requester ID at the time of the event
                ('RequestorId', ULONGLONG),
                # Bus Responder ID at the time of the event
                ('ResponderId', ULONGLONG),
                # Bus intended Target ID at the time of the event
                ('TargetId', ULONGLONG),
                # OEM specific Bus dependent data
                ('BusSpecificData', ERROR_BUS_SPECIFIC_DATA),
                # OEM specific data for bus identification
                ('OemId', UCHAR * 16),
                # OEM specific data
                ('OemData', ERROR_OEM_DATA),
            ]

            _ERROR_PLATFORM_BUS._fields_ = _TEMP__ERROR_PLATFORM_BUS


            # IA64 ERRORS: Platform Host Controller error device definitions
            ERROR_PLATFORM_HOST_CONTROLLER_GUID = (
                0xE429FAF8,
                0x3CB7,
                0x11D4,
                [0xBC, 0xA7, 0x0, 0x80, 0xC7, 0x3C, 0x88, 0x81]
            )


            # 0: Error Status  valid bit
            class DUMMYSTRUCTNAME(ctypes.Structure):
                pass


            DUMMYSTRUCTNAME._fields_ = [
                ('ErrorStatus', ULONGLONG, 1),
                # 1: Requester Identifier valid bit
                ('RequestorId', ULONGLONG, 1),
                # 2: Responder Identifier valid bit
                ('ResponderId', ULONGLONG, 1),
                # 3: Target Identifier valid bit
                ('TargetId', ULONGLONG, 1),
                # 4: Bus Specific Data valid bit
                ('BusSpecificData', ULONGLONG, 1),
                # 5: OEM Identification valid bit
                ('OemId', ULONGLONG, 1),
                # 6: OEM Data valid bit
                ('OemData', ULONGLONG, 1),
                # 7: OEM Device Path valid bit
                ('OemDevicePath', ULONGLONG, 1),
                # 63-8: Reserved
                ('Reserved', ULONGLONG, 56),
            ]
            _ERROR_PLATFORM_HOST_CONTROLLER_VALID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME


            _ERROR_PLATFORM_HOST_CONTROLLER_VALID._fields_ = [
                ('Valid', ULONGLONG),
                # Bits:
                ('DUMMYSTRUCTNAME', _ERROR_PLATFORM_HOST_CONTROLLER_VALID.DUMMYSTRUCTNAME),
            ]

            _TEMP__ERROR_PLATFORM_HOST_CONTROLLER = [
                ('Header', ERROR_SECTION_HEADER),
                ('Valid', ERROR_PCI_COMPONENT_VALID),
                # Host Controller Error Status
                ('ErrorStatus', ERROR_STATUS),
                # Host controller Requester ID at the time of the event
                ('RequestorId', ULONGLONG),
                # Host controller Responder ID at the time of the event
                ('ResponderId', ULONGLONG),
                # Host controller intended Target ID at the time of the event
                ('TargetId', ULONGLONG),
                # OEM specific Bus dependent data
                ('BusSpecificData', ERROR_BUS_SPECIFIC_DATA),
                # OEM specific data for bus identification
                ('OemId', UCHAR * 16),
                # OEM specific data
                ('OemData', ERROR_OEM_DATA),
            ]

            _ERROR_PLATFORM_HOST_CONTROLLER._fields_ = _TEMP__ERROR_PLATFORM_HOST_CONTROLLER


            # IA64 ERROR_LOGRECORDS definitions
            # MCA_EXCEPTION,
            # CMC_EXCEPTION,
            # CPE_EXCEPTION.
            # For compatibility with previous versions of the definitions:
            ERROR_LOGRECORD = ERROR_RECORD_HEADER
            PERROR_LOGRECORD = POINTER(ERROR_RECORD_HEADER)

            # Machine Check Abort
            MCA_EXCEPTION = ERROR_RECORD_HEADER
            PMCA_EXCEPTION = POINTER(ERROR_RECORD_HEADER)

            # Corrected Machine Check
            CMC_EXCEPTION = ERROR_RECORD_HEADER
            PCMC_EXCEPTION = POINTER(ERROR_RECORD_HEADER)

            # Corrected Platform Error
            CPE_EXCEPTION = ERROR_RECORD_HEADER
            PCPE_EXCEPTION = POINTER(ERROR_RECORD_HEADER)
            if NTDDI_VERSION > NTDDI_WINXP:
                # Init Event
                INIT_EXCEPTION = ERROR_RECORD_HEADER
                PINIT_EXCEPTION = POINTER(ERROR_RECORD_HEADER)
            # END IF

        # END IF   _IA64_

    elif defined(_ARM_) or defined(_ARM64_):
        # _ARM_WORKITEM_ MCE support
        _MCA_EXCEPTION._fields_ = [
            ('Dummy', ULONG),
        ]
    # END IF   defined(_X86_) or defined(_IA64_) or defined(_AMD64_)

    if _MSC_VER >= 1200:
        pass
    # END IF

# END IF   _MCE_


