import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_NTIOLOGC_ = None



# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) 1991 Microsoft Corporation Module Name: ntiologc.h Abstract:
# Constant definitions for the I/O error code log values. Author: Revision
# History: --
if not defined(_NTIOLOGC_):
    _NTIOLOGC_ = 1
    # Status values are 32 bit values layed out as follows:
    # 3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
    # 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
    # + --- + - + ------------------------- + ------------------------------- +
    # | Sev | C|  Facility  |   Code   |
    # + --- + - + ------------------------- + ------------------------------- +
    # where
    # Sev - is the severity code
    # 00 - Success
    # 01 - Informational
    # 10 - Warning
    # 11 - Error
    # C - is the Customer code flag
    # Facility - is the facility code
    # Code - is the facility's status code
    # Values are 32 bit values laid out as follows:
    # 3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
    # 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
    # + --- + - + - + ----------------------- +
    # ------------------------------- +
    # | Sev | C | R|  Facility  |   Code   |
    # + --- + - + - + ----------------------- +
    # ------------------------------- +
    # where
    # Sev - is the severity code
    # 00 - Success
    # 01 - Informational
    # 10 - Warning
    # 11 - Error
    # C - is the Customer code flag
    # R - is a reserved bit
    # Facility - is the facility code
    # Code - is the facility's status code
    # Define the facility codes
    FACILITY_RPC_RUNTIME = 0x2
    FACILITY_RPC_STUBS = 0x3
    FACILITY_IO_ERROR_CODE = 0x4
    FACILITY_MCA_ERROR_CODE = 0x5

    # Define the severity codes
    STATUS_SEVERITY_SUCCESS = 0x0
    STATUS_SEVERITY_INFORMATIONAL = 0x1
    STATUS_SEVERITY_WARNING = 0x2
    STATUS_SEVERITY_ERROR = 0x3

    # MessageId: IO_ERR_INSUFFICIENT_RESOURCES
    # MessageText:
    # The driver could not allocate something necessary for the request for %1.
    IO_ERR_INSUFFICIENT_RESOURCES = 0xC0040002

    # MessageId: IO_ERR_DRIVER_ERROR
    # MessageText:
    # Driver detected an internal error in its data structures for %1.
    IO_ERR_DRIVER_ERROR = 0xC0040004

    # MessageId: IO_ERR_SEEK_ERROR
    # MessageText:
    # The device, %1, had a seek error.
    IO_ERR_SEEK_ERROR = 0xC0040006

    # MessageId: IO_ERR_BAD_BLOCK
    # MessageText:
    # The device, %1, has a bad block.
    IO_ERR_BAD_BLOCK = 0xC0040007

    # MessageId: IO_ERR_TIMEOUT
    # MessageText:
    # The device, %1, did not respond within the timeout period.
    IO_ERR_TIMEOUT = 0xC0040009

    # MessageId: IO_ERR_CONTROLLER_ERROR
    # MessageText:
    # The driver detected a controller error on %1.
    IO_ERR_CONTROLLER_ERROR = 0xC004000B

    # MessageId: IO_ERR_NOT_READY
    # MessageText:
    # The device, %1, is not ready for access yet.
    IO_ERR_NOT_READY = 0xC004000F

    # MessageId: IO_ERR_INVALID_REQUEST
    # MessageText:
    # The request is incorrectly formatted for %1.
    IO_ERR_INVALID_REQUEST = 0xC0040010

    # MessageId: IO_ERR_RESET
    # MessageText:
    # The device, %1, has been reset.
    IO_ERR_RESET = 0xC0040013

    # MessageId: IO_ERR_BAD_FIRMWARE
    # MessageText:
    # The driver has detected a device with old or out-of-date firmware. The
    # device will not be used.
    IO_ERR_BAD_FIRMWARE = 0xC0040019

    # MessageId: IO_WRN_BAD_FIRMWARE
    # MessageText:
    # The driver has detected that device %1 has old or out-of-date firmware.
    # Reduced performance may result.
    IO_WRN_BAD_FIRMWARE = 0x8004001A

    # MessageId: IO_WRITE_CACHE_ENABLED
    # MessageText:
    # The driver detected that the device %1 has its write cache enabled. Data
    # corruption
    # may occur.
    IO_WRITE_CACHE_ENABLED = 0x80040020

    # MessageId: IO_RECOVERED_VIA_ECC
    # MessageText:
    # Data was recovered using error correction code on device %1.
    IO_RECOVERED_VIA_ECC = 0x80040021

    # MessageId: IO_WRITE_CACHE_DISABLED
    # MessageText:
    # The driver disabled the write cache on device %1.
    IO_WRITE_CACHE_DISABLED = 0x80040022

    # MessageId: IO_WARNING_PAGING_FAILURE
    # MessageText:
    # An error was detected on device %1 during a paging operation.
    IO_WARNING_PAGING_FAILURE = 0x80040033

    # MessageId: IO_WRN_FAILURE_PREDICTED
    # MessageText:
    # The driver has detected that device %1 has predicted that it will fail.
    # Immediately back up your data and replace your hard disk drive. A failure
    # may be imminent.
    IO_WRN_FAILURE_PREDICTED = 0x80040034

    # MessageId: IO_WARNING_ALLOCATION_FAILED
    # MessageText:
    # The driver failed to allocate memory.
    IO_WARNING_ALLOCATION_FAILED = 0x80040038

    # MessageId: IO_WARNING_DUPLICATE_SIGNATURE
    # MessageText:
    # The disk signature of disk %2 is equal to the disk signature of disk %3.
    IO_WARNING_DUPLICATE_SIGNATURE = 0x8004003A

    # MessageId: IO_WARNING_DUPLICATE_PATH
    # MessageText:
    # Disk %2 will not be used because it is a redundant path for disk %3.
    IO_WARNING_DUPLICATE_PATH = 0x8004003B

    # MessageId: IO_WARNING_WRITE_FUA_PROBLEM
    # MessageText:
    # Device %1 is not correctly processing some write requests. In Device
    # Manager, ensure that the Write Cache option is disabled for this device
    # or data corruption may occur.
    IO_WARNING_WRITE_FUA_PROBLEM = 0x80040084

    # MessageId: IO_WARNING_VOLUME_LOST_DISK_EXTENT
    # MessageText:
    # Extent %4 on disk %3 that is part of the fault-tolerant volume %2 is no
    # longer accessible.
    IO_WARNING_VOLUME_LOST_DISK_EXTENT = 0x8004008E

    # MessageId: IO_WARNING_DEVICE_HAS_INTERNAL_DUMP
    # MessageText:
    # The storage device produced an internal dump.
    IO_WARNING_DEVICE_HAS_INTERNAL_DUMP = 0x8004008F

    # MessageId: IO_WARNING_SOFT_THRESHOLD_REACHED
    # MessageText:
    # Disk %2 has crossed a capacity utilization threshold.
    IO_WARNING_SOFT_THRESHOLD_REACHED = 0x80040090

    # MessageId: IO_WARNING_SOFT_THRESHOLD_REACHED_EX
    # MessageText:
    # Disk %2 has crossed a capacity utilization threshold and used %3 bytes.
    # When the threshold was crossed, there were %4 bytes of remaining
    # capacity.
    IO_WARNING_SOFT_THRESHOLD_REACHED_EX = 0x80040091

    # MessageId: IO_WARNING_SOFT_THRESHOLD_REACHED_EX_LUN_LUN
    # MessageText:
    # Disk %2 has crossed a capacity utilization threshold and used %3 bytes.
    # When the threshold was crossed, the disk had %4 bytes of remaining
    # capacity.
    IO_WARNING_SOFT_THRESHOLD_REACHED_EX_LUN_LUN = 0x80040092

    # MessageId: IO_WARNING_SOFT_THRESHOLD_REACHED_EX_LUN_POOL
    # MessageText:
    # Disk %2 has crossed a capacity utilization threshold and used %3 bytes.
    # When the threshold was crossed, the pool had %4 bytes of remaining
    # capacity.
    IO_WARNING_SOFT_THRESHOLD_REACHED_EX_LUN_POOL = 0x80040093

    # MessageId: IO_WARNING_SOFT_THRESHOLD_REACHED_EX_POOL_LUN
    # MessageText:
    # Disk %2 has crossed a capacity utilization threshold. When the threshold
    # was crossed, %3 bytes from the pool were used and the disk had %4 bytes
    # of remaining capacity.
    IO_WARNING_SOFT_THRESHOLD_REACHED_EX_POOL_LUN = 0x80040094

    # MessageId: IO_WARNING_SOFT_THRESHOLD_REACHED_EX_POOL_POOL
    # MessageText:
    # Disk %2 has crossed a capacity utilization threshold. When the threshold
    # was crossed, %3 bytes from the pool were used and the pool had %4 bytes
    # of remaining capacity.
    IO_WARNING_SOFT_THRESHOLD_REACHED_EX_POOL_POOL = 0x80040095

    # MessageId: IO_ERROR_DISK_RESOURCES_EXHAUSTED
    # MessageText:
    # Disk %2 has reached a logical block provisioning permanent resource
    # exhaustion condition.
    IO_ERROR_DISK_RESOURCES_EXHAUSTED = 0xC0040096

    # MessageId: IO_WARNING_DISK_CAPACITY_CHANGED
    # MessageText:
    # The capacity of Disk %2 has changed.
    IO_WARNING_DISK_CAPACITY_CHANGED = 0x80040097

    # MessageId: IO_WARNING_DISK_PROVISIONING_TYPE_CHANGED
    # MessageText:
    # The logical block provisioning type for Disk %2 has changed.
    IO_WARNING_DISK_PROVISIONING_TYPE_CHANGED = 0x80040098

    # MessageId: IO_WARNING_IO_OPERATION_RETRIED
    # MessageText:
    # The IO operation at logical block address %2 for Disk %3 (PDO name: %4)
    # was retried.
    IO_WARNING_IO_OPERATION_RETRIED = 0x80040099

    # MessageId: IO_ERROR_IO_HARDWARE_ERROR
    # MessageText:
    # The IO operation at logical block address %2 for Disk %3 (PDO name: %4)
    # failed due to a hardware error.
    IO_ERROR_IO_HARDWARE_ERROR = 0xC004009A

    # MessageId: IO_WARNING_COMPLETION_TIME
    # MessageText:
    # The IO operation at logical block address %2 for Disk %3 took %4
    # milliseconds. This was longer than the maximum expected time of %5
    # milliseconds.
    IO_WARNING_COMPLETION_TIME = 0x8004009B

    # MessageId: IO_WARNING_DISK_SURPRISE_REMOVED
    # MessageText:
    # Disk %2 has been surprise removed.
    IO_WARNING_DISK_SURPRISE_REMOVED = 0x8004009D

    # MessageId: IO_WARNING_REPEATED_DISK_GUID
    # MessageText:
    IO_WARNING_REPEATED_DISK_GUID = 0x8004009E

    # MessageId: IO_WARNING_DISK_FIRMWARE_UPDATED
    # MessageText:
    # Firmware update for Disk %2 is completed.
    IO_WARNING_DISK_FIRMWARE_UPDATED = 0x4004009F

    # MessageId: IO_ERR_RETRY_SUCCEEDED
    # MessageText:
    # A retry was successful on %1.
    IO_ERR_RETRY_SUCCEEDED = 0x00040001

    # MessageId: IO_ERR_CONFIGURATION_ERROR
    # MessageText:
    # Driver or device is incorrectly configured for %1.
    IO_ERR_CONFIGURATION_ERROR = 0xC0040003

    # MessageId: IO_ERR_PARITY
    # MessageText:
    # A parity error was detected on %1.
    IO_ERR_PARITY = 0xC0040005

    # MessageId: IO_ERR_OVERRUN_ERROR
    # MessageText:
    # An overrun occurred on %1.
    IO_ERR_OVERRUN_ERROR = 0xC0040008

    # MessageId: IO_ERR_SEQUENCE
    # MessageText:
    # The driver detected an unexpected sequence by the device, %1.
    IO_ERR_SEQUENCE = 0xC004000A

    # MessageId: IO_ERR_INTERNAL_ERROR
    # MessageText:
    # The driver detected an internal driver error on %1.
    IO_ERR_INTERNAL_ERROR = 0xC004000C

    # MessageId: IO_ERR_INCORRECT_IRQL
    # MessageText:
    # The driver was configured with an incorrect interrupt for %1.
    IO_ERR_INCORRECT_IRQL = 0xC004000D

    # MessageId: IO_ERR_INVALID_IOBASE
    # MessageText:
    # The driver was configured with an invalid I/O base address for %1.
    IO_ERR_INVALID_IOBASE = 0xC004000E

    # MessageId: IO_ERR_VERSION
    # MessageText:
    # The wrong version of the driver has been loaded.
    IO_ERR_VERSION = 0xC0040011

    # MessageId: IO_ERR_LAYERED_FAILURE
    # MessageText:
    # The driver beneath this one has failed in some way for %1.
    IO_ERR_LAYERED_FAILURE = 0xC0040012

    # MessageId: IO_ERR_PROTOCOL
    # MessageText:
    # A transport driver received a frame which violated the protocol.
    IO_ERR_PROTOCOL = 0xC0040014

    # MessageId: IO_ERR_MEMORY_CONFLICT_DETECTED
    # MessageText:
    # A conflict has been detected between two drivers which claimed two
    # overlapping
    # memory regions.
    # Driver %2, with device {3>, claimed a memory range with starting address
    # in data address 0x28 and 0x2c, and length in data address 0x30.
    IO_ERR_MEMORY_CONFLICT_DETECTED = 0xC0040015
    # MessageId: IO_ERR_PORT_CONFLICT_DETECTED
    # MessageText:
    # A conflict has been detected between two drivers which claimed two
    # overlapping
    # Io port regions.
    # Driver %2, with device
    # {3>, claimed an IO port range with starting address
    # in data address 0x28 and 0x2c, and length in data address 0x30.
    IO_ERR_PORT_CONFLICT_DETECTED = 0xC0040016
    # MessageId: IO_ERR_DMA_CONFLICT_DETECTED
    # MessageText:
    # A conflict has been detected between two drivers which claimed
    # equivalent DMA
    # channels.
    # Driver %2, with device
    # {3>, claimed the DMA Channel in data address 0x28, with
    # optinal port in data address 0x2c.
    IO_ERR_DMA_CONFLICT_DETECTED = 0xC0040017
    # MessageId: IO_ERR_IRQ_CONFLICT_DETECTED
    # MessageText:
    # A conflict has been detected between two drivers which claimed
    # equivalent IRQs.
    # Driver %2, with device
    # {3>, claimed an interrupt with Level in data address
    # 0x28, vector in data address 0x2c and Affinity in data address 0x30.
    IO_ERR_IRQ_CONFLICT_DETECTED = 0xC0040018
    # MessageId: IO_ERR_DMA_RESOURCE_CONFLICT
    # MessageText:
    # The device could not allocate one or more required resources due to
    # conflicts
    # with other devices. The device DMA setting of '%2' could not be
    # satisified due to a conflict with Driver '%3'.
    IO_ERR_DMA_RESOURCE_CONFLICT = 0xC004001B
    # MessageId: IO_ERR_INTERRUPT_RESOURCE_CONFLICT
    # MessageText:
    # The device could not allocate one or more required resources due to
    # conflicts
    # with other devices. The device interrupt setting of '%2' could not be
    # satisified due to a conflict with Driver '%3'.
    IO_ERR_INTERRUPT_RESOURCE_CONFLICT = 0xC004001C
    # MessageId: IO_ERR_MEMORY_RESOURCE_CONFLICT
    # MessageText:
    # The device could not allocate one or more required resources due to
    # conflicts
    # with other devices. The device memory setting of '%2' could not be
    # satisified due to a conflict with Driver '%3'.
    IO_ERR_MEMORY_RESOURCE_CONFLICT = 0xC004001D
    # MessageId: IO_ERR_PORT_RESOURCE_CONFLICT
    # MessageText:
    # The device could not allocate one or more required resources due to
    # conflicts
    # with other devices. The device port setting of '%2' could not be
    # satisified due to a conflict with Driver '%3'.
    IO_ERR_PORT_RESOURCE_CONFLICT = 0xC004001E
    # MessageId: IO_BAD_BLOCK_WITH_NAME
    # MessageText:
    # The file %2 on device %1 contains a bad disk block.
    IO_BAD_BLOCK_WITH_NAME = 0xC004001F
    # MessageId: IO_FILE_QUOTA_THRESHOLD
    # MessageText:
    # A user hit their quota threshold on volume %2.
    IO_FILE_QUOTA_THRESHOLD = 0x40040024
    # MessageId: IO_FILE_QUOTA_LIMIT
    # MessageText:
    # A user hit their quota limit on volume %2.
    IO_FILE_QUOTA_LIMIT = 0x40040025
    # MessageId: IO_FILE_QUOTA_STARTED
    # MessageText:
    # The system has started rebuilding the user disk quota information on
    # device %1 with label "%2".
    IO_FILE_QUOTA_STARTED = 0x40040026
    # MessageId: IO_FILE_QUOTA_SUCCEEDED
    # MessageText:
    # The system has successfully rebuilt the user disk quota information on
    # device %1 with label "%2".
    IO_FILE_QUOTA_SUCCEEDED = 0x40040027
    # MessageId: IO_FILE_QUOTA_FAILED
    # MessageText:
    # The system has encounted an error rebuilding the user disk quota
    # information on device %1 with label "%2".
    IO_FILE_QUOTA_FAILED = 0x80040028
    # MessageId: IO_FILE_SYSTEM_CORRUPT
    # MessageText:
    # The file system structure on the disk is corrupt and unusable.
    # Please run the chkdsk utility on the device %1 with label "%2".
    IO_FILE_SYSTEM_CORRUPT = 0xC0040029
    # MessageId: IO_FILE_QUOTA_CORRUPT
    # MessageText:
    # The user disk quota information is unusable.
    # To ensure accuracy, the file system quota information on the device %1
    # with label "%2" will
    # be rebuilt.
    IO_FILE_QUOTA_CORRUPT = 0xC004002A
    # MessageId: IO_SYSTEM_SLEEP_FAILED
    # MessageText:
    # The system sleep operation failed
    IO_SYSTEM_SLEEP_FAILED = 0xC004002B
    # MessageId: IO_DUMP_POINTER_FAILURE
    # MessageText:
    # The system could not get file retrieval pointers for the dump file.
    IO_DUMP_POINTER_FAILURE = 0xC004002C
    # MessageId: IO_DUMP_DRIVER_LOAD_FAILURE
    # MessageText:
    # The system could not sucessfully load the crash dump driver.
    IO_DUMP_DRIVER_LOAD_FAILURE = 0xC004002D
    # MessageId: IO_DUMP_INITIALIZATION_FAILURE
    # MessageText:
    # Crash dump initialization failednot
    IO_DUMP_INITIALIZATION_FAILURE = 0xC004002E
    # MessageId: IO_DUMP_DUMPFILE_CONFLICT
    # MessageText:
    # A valid crash dump was found in the paging file while trying to configure
    # a direct dump. Direct dump is disablednot This occurs when the direct
    # dump
    # option is set in the registry but a stop error occured before
    # configuration
    # completed
    IO_DUMP_DUMPFILE_CONFLICT = 0xC004002F
    # MessageId: IO_DUMP_DIRECT_CONFIG_FAILED
    # MessageText:
    # Direct dump configuration failed. Validate the filename and make sure
    # the target device
    # is not a Fault Tolerant set member, remote, or floppy device. The
    # failure may
    # be because there is not enough room on the dump device to create the
    # dump file.
    IO_DUMP_DIRECT_CONFIG_FAILED = 0xC0040030
    # MessageId: IO_DUMP_PAGE_CONFIG_FAILED
    # MessageText:
    # Configuring the Page file for crash dump failed. Make sure there is a
    # page
    # file on the boot partition and that is large enough to contain all
    # physical
    # memory.
    IO_DUMP_PAGE_CONFIG_FAILED = 0xC0040031
    # MessageId: IO_LOST_DELAYED_WRITE
    # MessageText:
    # {Delayed Write Failed}
    # Windows was unable to save all the data for the file %2. The data has
    # been lost.
    # This error may be caused by a failure of your computer hardware or
    # network connection. Please try to save this file elsewhere.
    IO_LOST_DELAYED_WRITE = 0x80040032
    # MessageId: IO_WARNING_INTERRUPT_STILL_PENDING
    # MessageText:
    # A pending interrupt was detected on device %1 during a timeout
    # operation. A
    # large number of these warnings may indicate that the system is not
    # correctly
    # receiving or processing interrupts from the device.
    IO_WARNING_INTERRUPT_STILL_PENDING = 0x80040035
    # MessageId: IO_DRIVER_CANCEL_TIMEOUT
    # MessageText:
    # An Io Request to the device %1 did not complete or canceled within the
    # specific timeout. This can occur if the device driver does not set a
    # cancel routine for a given IO request packet.
    IO_DRIVER_CANCEL_TIMEOUT = 0x80040036
    # MessageId: IO_FILE_SYSTEM_CORRUPT_WITH_NAME
    # MessageText:
    # The file system structure on the disk is corrupt and unusable.
    # Please run the chkdsk utility on the volume %2.
    IO_FILE_SYSTEM_CORRUPT_WITH_NAME = 0xC0040037
    # MessageId: IO_WARNING_LOG_FLUSH_FAILED
    # MessageText:
    # The system failed to flush data to the transaction log. Corruption may
    # occur.
    IO_WARNING_LOG_FLUSH_FAILED = 0x80040039
    # MessageId: MCA_WARNING_CACHE
    # MessageText:
    # Machine Check Event reported is a corrected level %3 Cache error
    # reported to CPU %1. %2 additional error(s) are contained within the
    # record.
    MCA_WARNING_CACHE = 0x8005003C
    # MessageId: MCA_ERROR_CACHE
    # MessageText:
    # Machine Check Event reported is a fatal level %3 Cache error reported to
    # CPU %1. %2 additional error(s) are contained within the record.
    MCA_ERROR_CACHE = 0xC005003D
    # MessageId: MCA_WARNING_TLB
    # MessageText:
    # Machine Check Event reported is a corrected level %3 translation Buffer
    # error reported to CPU %1. %2 additional error(s) are contained within
    # the record.
    MCA_WARNING_TLB = 0x8005003E
    # MessageId: MCA_ERROR_TLB
    # MessageText:
    # Machine Check Event reported is a fatal level %3 translation Buffer
    # error reported to CPU %1. %2 additional error(s) are contained within
    # the record.
    MCA_ERROR_TLB = 0xC005003F
    # MessageId: MCA_WARNING_CPU_BUS
    # MessageText:
    # Machine Check Event reported is a corrected External/Internal bus error
    # reported to CPU %1. %2 additional error(s) are contained within the
    # record.
    MCA_WARNING_CPU_BUS = 0x80050040
    # MessageId: MCA_ERROR_CPU_BUS
    # MessageText:
    # Machine Check Event reported is a fatal External/Internal bus error
    # reported to CPU %1. %2 additional error(s) are contained within the
    # record.
    MCA_ERROR_CPU_BUS = 0xC0050041
    # MessageId: MCA_WARNING_REGISTER_FILE
    # MessageText:
    # Machine Check Event reported is a corrected internal CPU register access
    # error reported to CPU %1. %2 additional error(s) are contained within
    # the record.
    MCA_WARNING_REGISTER_FILE = 0x80050042
    # MessageId: MCA_ERROR_REGISTER_FILE
    # MessageText:
    # Machine Check Event reported is a fatal internal CPU register access
    # error reported to CPU %1. %2 additional error(s) are contained within
    # the record.
    MCA_ERROR_REGISTER_FILE = 0xC0050043
    # MessageId: MCA_WARNING_MAS
    # MessageText:
    # Machine Check Event reported is a corrected Micro Architecture Structure
    # error reported to CPU %1. %2 additional error(s) are contained within
    # the record.
    MCA_WARNING_MAS = 0x80050044
    # MessageId: MCA_ERROR_MAS
    # MessageText:
    # Machine Check Event reported is a fatal Micro Architecture Structure
    # error reported to CPU %1. %2 additional error(s) are contained within
    # the record.
    MCA_ERROR_MAS = 0xC0050045
    # MessageId: MCA_WARNING_MEM_UNKNOWN
    # MessageText:
    # Machine Check Event reported is a corrected ECC memory error at an
    # unknown physical address reported to CPU %1. %2 additional error(s) are
    # contained within the record.
    MCA_WARNING_MEM_UNKNOWN = 0x80050046
    # MessageId: MCA_ERROR_MEM_UNKNOWN
    # MessageText:
    # Machine Check Event reported is a fatal ECC memory error at an unknown
    # physical address reported to CPU %1. %2 additional error(s) are
    # contained within the record.
    MCA_ERROR_MEM_UNKNOWN = 0xC0050047
    # MessageId: MCA_WARNING_MEM_1_2
    # MessageText:
    # Machine Check Event reported is a corrected ECC memory error at physical
    # address %3 reported to CPU %1. %2 additional error(s) are contained
    # within the record.
    MCA_WARNING_MEM_1_2 = 0x80050048
    # MessageId: MCA_ERROR_MEM_1_2
    # MessageText:
    # Machine Check Event reported is a fatal ECC memory error at physical
    # address %3 reported to CPU %1. %2 additional error(s) are contained
    # within the record.
    MCA_ERROR_MEM_1_2 = 0xC0050049
    # MessageId: MCA_WARNING_MEM_1_2_5
    # MessageText:
    # Machine Check Event reported is a corrected ECC memory error at physical
    # address %3 on memory module %4 reported to CPU %1. %2 additional
    # error(s) are contained within the record.
    MCA_WARNING_MEM_1_2_5 = 0x8005004A
    # MessageId: MCA_ERROR_MEM_1_2_5
    # MessageText:
    # Machine Check Event reported is a fatal ECC memory error at physical
    # address %3 on memory module %4 reported to CPU %1. %2 additional
    # error(s) are contained within the record.
    MCA_ERROR_MEM_1_2_5 = 0xC005004B
    # MessageId: MCA_WARNING_MEM_1_2_5_4
    # MessageText:
    # Machine Check Event reported is a corrected ECC memory error at physical
    # address %3 on memory module %4 on memory card %5 reported to CPU %1. %2
    # additional error(s) are contained within the record.
    MCA_WARNING_MEM_1_2_5_4 = 0x8005004C
    # MessageId: MCA_ERROR_MEM_1_2_5_4
    # MessageText:
    # Machine Check Event reported is a fatal ECC memory error at physical
    # address %3 on memory module %4 on memory card %5 reported to CPU %1. %2
    # additional error(s) are contained within the record.
    MCA_ERROR_MEM_1_2_5_4 = 0xC005004D
    # MessageId: MCA_WARNING_SYSTEM_EVENT
    # MessageText:
    # Machine Check Event reported is a corrected System Event error reported
    # to CPU %1. %2 additional error(s) are contained within the record.
    MCA_WARNING_SYSTEM_EVENT = 0x8005004E
    # MessageId: MCA_ERROR_SYSTEM_EVENT
    # MessageText:
    # Machine Check Event reported is a fatal System Event error reported to
    # CPU %1. %2 additional error(s) are contained within the record.
    MCA_ERROR_SYSTEM_EVENT = 0xC005004F
    # MessageId: MCA_WARNING_PCI_BUS_PARITY
    # MessageText:
    # Machine Check Event reported is a corrected PCI bus Parity error during
    # a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2
    # additional error(s) are contained within the record.
    MCA_WARNING_PCI_BUS_PARITY = 0x80050050
    # MessageId: MCA_ERROR_PCI_BUS_PARITY
    # MessageText:
    # Machine Check Event reported is a fatal PCI bus Parity error during a
    # transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2
    # additional error(s) are contained within the record.
    MCA_ERROR_PCI_BUS_PARITY = 0xC0050051
    # MessageId: MCA_WARNING_PCI_BUS_PARITY_NO_INFO
    # MessageText:
    # Machine Check Event reported is a corrected PCI bus Parity error
    # reported to CPU %1. %2 additional error(s) are contained within the
    # record.
    MCA_WARNING_PCI_BUS_PARITY_NO_INFO = 0x80050052
    # MessageId: MCA_ERROR_PCI_BUS_PARITY_NO_INFO
    # MessageText:
    # Machine Check Event reported is a fatal PCI bus Parity error reported to
    # CPU %1. %2 additional error(s) are contained within the record.
    MCA_ERROR_PCI_BUS_PARITY_NO_INFO = 0xC0050053
    # MessageId: MCA_WARNING_PCI_BUS_SERR
    # MessageText:
    # Machine Check Event reported is a corrected PCI bus SERR error during a
    # transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2
    # additional error(s) are contained within the record.
    MCA_WARNING_PCI_BUS_SERR = 0x80050054
    # MessageId: MCA_ERROR_PCI_BUS_SERR
    # MessageText:
    # Machine Check Event reported is a fatal PCI bus SERR error during a
    # transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2
    # additional error(s) are contained within the record.
    MCA_ERROR_PCI_BUS_SERR = 0xC0050055
    # MessageId: MCA_WARNING_PCI_BUS_SERR_NO_INFO
    # MessageText:
    # Machine Check Event reported is a corrected PCI bus SERR error reported
    # to CPU %1. %2 additional error(s) are contained within the record.
    MCA_WARNING_PCI_BUS_SERR_NO_INFO = 0x80050056
    # MessageId: MCA_ERROR_PCI_BUS_SERR_NO_INFO
    # MessageText:
    # Machine Check Event reported is a fatal PCI bus SERR error reported to
    # CPU %1. %2 additional error(s) are contained within the record.
    MCA_ERROR_PCI_BUS_SERR_NO_INFO = 0xC0050057
    # MessageId: MCA_WARNING_PCI_BUS_MASTER_ABORT
    # MessageText:
    # Machine Check Event reported is a corrected PCI bus Master abort error
    # during a transaction type %3 at address %4 on PCI bus %5 reported to CPU
    # %1. %2 additional error(s) are contained within the record.
    MCA_WARNING_PCI_BUS_MASTER_ABORT = 0x80050058
    # MessageId: MCA_ERROR_PCI_BUS_MASTER_ABORT
    # MessageText:
    # Machine Check Event reported is a fatal PCI bus Master abort error
    # during a transaction type %3 at address %4 on PCI bus %5 reported to CPU
    # %1. %2 additional error(s) are contained within the record.
    MCA_ERROR_PCI_BUS_MASTER_ABORT = 0xC0050059
    # MessageId: MCA_WARNING_PCI_BUS_MASTER_ABORT_NO_INFO
    # MessageText:
    # Machine Check Event reported is a corrected PCI bus Master abort error
    # reported to CPU %1. %2 additional error(s) are contained within the
    # record.
    MCA_WARNING_PCI_BUS_MASTER_ABORT_NO_INFO = 0x8005005A
    # MessageId: MCA_ERROR_PCI_BUS_MASTER_ABORT_NO_INFO
    # MessageText:
    # Machine Check Event reported is a fatal PCI bus Master abort error
    # reported to CPU %1. %2 additional error(s) are contained within the
    # record.
    MCA_ERROR_PCI_BUS_MASTER_ABORT_NO_INFO = 0xC005005B
    # MessageId: MCA_WARNING_PCI_BUS_TIMEOUT
    # MessageText:
    # Machine Check Event reported is a corrected PCI bus Timeout error during
    # a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2
    # additional error(s) are contained within the record.
    MCA_WARNING_PCI_BUS_TIMEOUT = 0x8005005C
    # MessageId: MCA_ERROR_PCI_BUS_TIMEOUT
    # MessageText:
    # Machine Check Event reported is a fatal PCI bus Timeout error during a
    # transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2
    # additional error(s) are contained within the record.
    MCA_ERROR_PCI_BUS_TIMEOUT = 0xC005005D
    # MessageId: MCA_WARNING_PCI_BUS_TIMEOUT_NO_INFO
    # MessageText:
    # Machine Check Event reported is a corrected PCI bus Timeout error
    # reported to CPU %1. %2 additional error(s) are contained within the
    # record.
    MCA_WARNING_PCI_BUS_TIMEOUT_NO_INFO = 0x8005005E
    # MessageId: MCA_ERROR_PCI_BUS_TIMEOUT_NO_INFO
    # MessageText:
    # Machine Check Event reported is a fatal PCI bus Timeout error reported
    # to CPU %1. %2 additional error(s) are contained within the record.
    MCA_ERROR_PCI_BUS_TIMEOUT_NO_INFO = 0xC005005F
    # MessageId: MCA_WARNING_PCI_BUS_UNKNOWN
    # MessageText:
    # Machine Check Event reported is an unknown corrected PCI bus error
    # reported to CPU %1. %2 additional error(s) are contained within the
    # record.
    MCA_WARNING_PCI_BUS_UNKNOWN = 0x80050060
    # MessageId: MCA_ERROR_PCI_BUS_UNKNOWN
    # MessageText:
    # Machine Check Event reported is an unknown fatal PCI bus error reported
    # to CPU %1. %2 additional error(s) are contained within the record.
    MCA_ERROR_PCI_BUS_UNKNOWN = 0xC0050061
    # MessageId: MCA_WARNING_PCI_DEVICE
    # MessageText:
    # Machine Check Event reported is a corrected PCI component error reported
    # to CPU %1. %2 additional error(s) are contained within the record.
    MCA_WARNING_PCI_DEVICE = 0x80050062
    # MessageId: MCA_ERROR_PCI_DEVICE
    # MessageText:
    # Machine Check Event reported is a fatal PCI component error reported to
    # CPU %1. %2 additional error(s) are contained within the record.
    MCA_ERROR_PCI_DEVICE = 0xC0050063
    # MessageId: MCA_WARNING_SMBIOS
    # MessageText:
    # Machine Check Event reported is a corrected SMBIOS Device Type %3 error
    # reported to CPU %1. %2 additional error(s) are contained within the
    # record.
    MCA_WARNING_SMBIOS = 0x80050064
    # MessageId: MCA_ERROR_SMBIOS
    # MessageText:
    # Machine Check Event reported is a fatal SMBIOS Device Type %3 error
    # reported to CPU %1. %2 additional error(s) are contained within the
    # record.
    MCA_ERROR_SMBIOS = 0xC0050065
    # MessageId: MCA_WARNING_PLATFORM_SPECIFIC
    # MessageText:
    # Machine Check Event reported is a corrected Platform Specific error
    # reported to CPU %1. %2 additional error(s) are contained within the
    # record.
    MCA_WARNING_PLATFORM_SPECIFIC = 0x80050066
    # MessageId: MCA_ERROR_PLATFORM_SPECIFIC
    # MessageText:
    # Machine Check Event reported is a fatal Platform Specific error reported
    # to CPU %1. %2 additional error(s) are contained within the record.
    MCA_ERROR_PLATFORM_SPECIFIC = 0xC0050067
    # MessageId: MCA_WARNING_UNKNOWN
    # MessageText:
    # Machine Check Event reported is a corrected error reported to CPU %1.
    MCA_WARNING_UNKNOWN = 0x80050068
    # MessageId: MCA_ERROR_UNKNOWN
    # MessageText:
    # Machine Check Event reported is a fatal error reported to CPU %1.
    MCA_ERROR_UNKNOWN = 0xC0050069
    # MessageId: MCA_WARNING_UNKNOWN_NO_CPU
    # MessageText:
    # Machine Check Event reported is a corrected error.
    MCA_WARNING_UNKNOWN_NO_CPU = 0x8005006A
    # MessageId: MCA_ERROR_UNKNOWN_NO_CPU
    # MessageText:
    # Machine Check Event reported is a fatal error.
    MCA_ERROR_UNKNOWN_NO_CPU = 0xC005006B
    # MessageId: IO_ERR_THREAD_STUCK_IN_DEVICE_DRIVER
    # MessageText:
    # The driver %3 for the %2 device %1 got stuck in an infinite loop. This
    # usually indicates a problem with the device itself or with the device
    # driver programming the hardware incorrectly. Please check with your
    # hardware device vendor for any driver updates.
    IO_ERR_THREAD_STUCK_IN_DEVICE_DRIVER = 0xC004006C
    # MessageId: MCA_WARNING_CMC_THRESHOLD_EXCEEDED
    # MessageText:
    # Corrected Machine Check Interrupt threshold exceeded. Interrupt has been
    # disabled. Polling mode has been enabled.
    MCA_WARNING_CMC_THRESHOLD_EXCEEDED = 0x8005006D
    # MessageId: MCA_WARNING_CPE_THRESHOLD_EXCEEDED
    # MessageText:
    # Corrected Platform Error Interrupt threshold exceeded. Interrupt has
    # been disabled. Polling mode has been enabled.
    MCA_WARNING_CPE_THRESHOLD_EXCEEDED = 0x8005006E
    # MessageId: MCA_WARNING_CPU_THERMAL_THROTTLED
    # MessageText:
    # Machine Check Event reported is a CPU thermal throttling event reported
    # from CPU %1. The CPU has exceeded the temperature limit and has been
    # throttled down. %2 additional error(s) are contained within the record.
    MCA_WARNING_CPU_THERMAL_THROTTLED = 0x8005006F
    # MessageId: MCA_INFO_CPU_THERMAL_THROTTLING_REMOVED
    # MessageText:
    # Machine Check Event reported is a CPU thermal throttling event reported
    # from CPU %1. The CPU has dropped below the temperature limit and
    # throttling has been removed. %2 additional error(s) are contained within
    # the record.
    MCA_INFO_CPU_THERMAL_THROTTLING_REMOVED = 0x40050070
    # MessageId: MCA_WARNING_CPU
    # MessageText:
    # Machine Check Event reported is a corrected CPU error reported from CPU
    # %1. %2 additional error(s) are contained within the record.
    MCA_WARNING_CPU = 0x80050071
    # MessageId: MCA_ERROR_CPU
    # MessageText:
    # Machine Check Event reported is a fatal CPU error reported to CPU %1. %2
    # additional error(s) are contained within the record.
    MCA_ERROR_CPU = 0xC0050072
    # MessageId: MCA_INFO_NO_MORE_CORRECTED_ERROR_LOGS
    # MessageText:
    # The maximum number of Machine Check Event corrected error events that
    # can be saved to the Event Log has been reached. Logging of these events
    # has been disabled.
    MCA_INFO_NO_MORE_CORRECTED_ERROR_LOGS = 0x40050073
    # MessageId: MCA_INFO_MEMORY_PAGE_MARKED_BAD
    # MessageText:
    # The memory page at physical address %1 has encountered multiple
    # corrected hardware error events. As a result it will no longer be used
    # by Windows.
    MCA_INFO_MEMORY_PAGE_MARKED_BAD = 0x40050074
    # MessageId: IO_ERR_PORT_TIMEOUT
    # MessageText:
    # The driver for device %1 detected a port timeout due to prolonged
    # inactivity. All associated busses were reset in an effort to clear the
    # condition.
    IO_ERR_PORT_TIMEOUT = 0xC0040075
    # MessageId: IO_WARNING_BUS_RESET
    # MessageText:
    # The driver for device %1 performed a bus reset upon request.
    IO_WARNING_BUS_RESET = 0x80040076
    # MessageId: IO_INFO_THROTTLE_COMPLETE
    # MessageText:
    # The driver for device %1 delayed non-paging Io requests for %2 ms to
    # recover from a low memory condition.
    IO_INFO_THROTTLE_COMPLETE = 0x40040077
    # MessageId: MCA_MEMORYHIERARCHY_ERROR
    # MessageText:
    # Machine Check Event reported is a fatal memory hierarchy error.%r
    # Trasaction Type: %1%r Memory Hierarchy Level: %2%r Request Type: %3%r
    # Address: %4
    MCA_MEMORYHIERARCHY_ERROR = 0xC0050078
    # MessageId: MCA_TLB_ERROR
    # MessageText:
    # Machine Check Event reported is a fatal TLB error.%r Transaction Type:
    # %1%r Memory Hierarchy Level: %2%r Address: %3
    MCA_TLB_ERROR = 0xC0050079
    # MessageId: MCA_BUS_ERROR
    # MessageText:
    # Machine Check Event reported is a fatal Bus or Interconnect error.%r
    # Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r
    # Memory/IO: %4%r Address: %5
    MCA_BUS_ERROR = 0xC005007A
    # MessageId: MCA_BUS_TIMEOUT_ERROR
    # MessageText:
    # Machine Check Event reported is a fatal Bus or Interconnect timeout
    # error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type:
    # %3%r Memory/IO: %4%r Address: %5
    MCA_BUS_TIMEOUT_ERROR = 0xC005007B
    # MessageId: MCA_INTERNALTIMER_ERROR
    # MessageText:
    # Machine Check Event reported is a fatal internal watchdog timer error.
    MCA_INTERNALTIMER_ERROR = 0xC005007C
    # MessageId: MCA_MICROCODE_ROM_PARITY_ERROR
    # MessageText:
    # Machine Check Event reported is a fatal microsoft ROM parity error.
    MCA_MICROCODE_ROM_PARITY_ERROR = 0xC005007E
    # MessageId: MCA_EXTERNAL_ERROR
    # MessageText:
    # Machine Check Event reported is a fatal condition. A processor received
    # an external signal that an unrecoverable error has occurred.
    MCA_EXTERNAL_ERROR = 0xC005007F
    # MessageId: MCA_FRC_ERROR
    # MessageText:
    # Machine Check Event reported is a fatal functional redundancy check
    # error.
    MCA_FRC_ERROR = 0xC0050080
    # MessageId: IO_WARNING_RESET
    # MessageText:
    # Reset to device, %1, was issued.
    IO_WARNING_RESET = 0x80040081
    # MessageId: IO_CDROM_EXCLUSIVE_LOCK
    # MessageText:
    # Device %1 is locked for exclusive access.
    IO_CDROM_EXCLUSIVE_LOCK = 0x40040085
    # MessageId: IO_LOST_DELAYED_WRITE_NETWORK_DISCONNECTED
    # MessageText:
    # {Delayed Write Failed}
    # Windows was unable to save all the data for the file %2; the data has
    # been lost.
    # This error may be caused by network connectivity issues. Please try to
    # save this file elsewhere.
    IO_LOST_DELAYED_WRITE_NETWORK_DISCONNECTED = 0x8004008B
    # MessageId: IO_LOST_DELAYED_WRITE_NETWORK_SERVER_ERROR
    # MessageText:
    # {Delayed Write Failed}
    # Windows was unable to save all the data for the file %2; the data has
    # been lost.
    # This error was returned by the server on which the file exists. Please
    # try to save this file elsewhere.
    IO_LOST_DELAYED_WRITE_NETWORK_SERVER_ERROR = 0x8004008C
    # MessageId: IO_LOST_DELAYED_WRITE_NETWORK_LOCAL_DISK_ERROR
    # MessageText:
    # {Delayed Write Failed}
    # Windows was unable to save all the data for the file %2; the data has
    # been lost.
    # This error may be caused if the device has been removed or the media is
    # write-protected.
    IO_LOST_DELAYED_WRITE_NETWORK_LOCAL_DISK_ERROR = 0x8004008D
    # MessageId: IO_WARNING_DUMP_DISABLED_DEVICE_GONE
    # MessageText:
    # Crash dump is disabled. Crash dump device is not present in the system.
    IO_WARNING_DUMP_DISABLED_DEVICE_GONE = 0x8004009C
    # MessageId: IO_WARNING_ADAPTER_FIRMWARE_UPDATED
    # MessageText:
    # Firmware update for Adapter %1 is completed.
    IO_WARNING_ADAPTER_FIRMWARE_UPDATED = 0x400400A0
    # MessageId: IO_ERROR_DUMP_CREATION_ERROR
    # MessageText:
    # Dump file creation failed due to error during dump creation.
    IO_ERROR_DUMP_CREATION_ERROR = 0xC00400A1
# END IF  _NTIOLOGC_
