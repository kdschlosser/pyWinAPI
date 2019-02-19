import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_CFG_INCLUDED_ = None

# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: cfg.h Abstract: This module contains the common Configuration Manager
# definitions for both user mode and kernel mode code. Revision History: --
if not defined(_CFG_INCLUDED_):
    _CFG_INCLUDED_ = VOID
    if _MSC_VER  >  1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if defined(_MSC_VER):
        if _MSC_VER  >= 1200:
            pass
        # END IF
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # The following definitions are also used by kernel mode code to
        # set up the registry.
        # VetoType used in
        # CM_Disable_DevNode
        # CM_Uninstall_DevNode
        # CM_Query_And_Remove_SubTree
        class _PNP_VETO_TYPE(ENUM):
            PNP_VetoTypeUnknown = 1
            PNP_VetoLegacyDevice = 2
            PNP_VetoPendingClose = 3
            PNP_VetoWindowsApp = 4
            PNP_VetoWindowsService = 5
            PNP_VetoOutstandingOpen = 6
            PNP_VetoDevice = 7
            PNP_VetoDriver = 8
            PNP_VetoIllegalDeviceRequest = 9
            PNP_VetoInsufficientPower = 10
            PNP_VetoNonDisableable = 11
            PNP_VetoLegacyDriver = 12
            PNP_VetoInsufficientRights = 13

        PNP_VETO_TYPE = _PNP_VETO_TYPE
        PPNP_VETO_TYPE = POINTER(_PNP_VETO_TYPE)

        # DevInst problem values, returned by call to CM_Get_DevInst_Status
        # no config for device
        CM_PROB_NOT_CONFIGURED = 0x00000001

        # service load failed
        CM_PROB_DEVLOADER_FAILED = 0x00000002

        # out of memory
        CM_PROB_OUT_OF_MEMORY = 0x00000003
        CM_PROB_ENTRY_IS_WRONG_TYPE = 0x00000004
        CM_PROB_LACKED_ARBITRATOR = 0x00000005

        # boot config conflict
        CM_PROB_BOOT_CONFIG_CONFLICT = 0x00000006
        CM_PROB_FAILED_FILTER = 0x00000007

        # Devloader not found
        CM_PROB_DEVLOADER_NOT_FOUND = 0x00000008

        # Invalid ID
        CM_PROB_INVALID_DATA = 0x00000009
        CM_PROB_FAILED_START = 0x0000000A
        CM_PROB_LIAR = 0x0000000B

        # config conflict
        CM_PROB_NORMAL_CONFLICT = 0x0000000C
        CM_PROB_NOT_VERIFIED = 0x0000000D

        # requires restart
        CM_PROB_NEED_RESTART = 0x0000000E
        CM_PROB_REENUMERATION = 0x0000000F
        CM_PROB_PARTIAL_LOG_CONF = 0x00000010

        # unknown res type
        CM_PROB_UNKNOWN_RESOURCE = 0x00000011
        CM_PROB_REINSTALL = 0x00000012
        CM_PROB_REGISTRY = 0x00000013

        # WINDOWS 95 ONLY
        CM_PROB_VXDLDR = 0x00000014

        # devinst will remove
        CM_PROB_WILL_BE_REMOVED = 0x00000015

        # devinst is disabled
        CM_PROB_DISABLED = 0x00000016

        # Devloader not ready
        CM_PROB_DEVLOADER_NOT_READY = 0x00000017

        # device doesn't exist
        CM_PROB_DEVICE_NOT_THERE = 0x00000018
        CM_PROB_MOVED = 0x00000019
        CM_PROB_TOO_EARLY = 0x0000001A

        # no valid log config
        CM_PROB_NO_VALID_LOG_CONF = 0x0000001B

        # install failed
        CM_PROB_FAILED_INSTALL = 0x0000001C

        # device disabled
        CM_PROB_HARDWARE_DISABLED = 0x0000001D

        # can't share IRQ
        CM_PROB_CANT_SHARE_IRQ = 0x0000001E

        # driver failed add
        CM_PROB_FAILED_ADD = 0x0000001F

        # service's Start = 4
        CM_PROB_DISABLED_SERVICE = 0x00000020

        # resource translation failed
        CM_PROB_TRANSLATION_FAILED = 0x00000021

        # no soft config
        CM_PROB_NO_SOFTCONFIG = 0x00000022

        # device missing in BIOS table
        CM_PROB_BIOS_TABLE = 0x00000023

        # IRQ translator failed
        CM_PROB_IRQ_TRANSLATION_FAILED = 0x00000024

        # DriverEntry() failed.
        CM_PROB_FAILED_DRIVER_ENTRY = 0x00000025

        # Driver should have unloaded.
        CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD = 0x00000026

        # Driver load unsuccessful.
        CM_PROB_DRIVER_FAILED_LOAD = 0x00000027

        # Error accessing driver's service key
        CM_PROB_DRIVER_SERVICE_KEY_INVALID = 0x00000028

        # Loaded legacy service created no devices
        CM_PROB_LEGACY_SERVICE_NO_DEVICES = 0x00000029

        # Two devices were discovered with the same name
        CM_PROB_DUPLICATE_DEVICE = 0x0000002A

        # The drivers set the device state to failed
        CM_PROB_FAILED_POST_START = 0x0000002B

        # The devinst currently exists only in the registry
        CM_PROB_PHANTOM = 0x0000002D

        # The system is shutting down
        CM_PROB_SYSTEM_SHUTDOWN = 0x0000002E

        # The device is offline awaiting removal
        CM_PROB_HELD_FOR_EJECT = 0x0000002F

        # One or more drivers is blocked from loading
        CM_PROB_DRIVER_BLOCKED = 0x00000030

        # System hive has grown too large
        CM_PROB_REGISTRY_TOO_LARGE = 0x00000031

        # Failed to apply one or more registry properties
        CM_PROB_SETPROPERTIES_FAILED = 0x00000032

        # Device is stalled waiting on a dependency to start
        CM_PROB_WAITING_ON_DEPENDENCY = 0x00000033

        # Failed load driver due to UINT image.
        CM_PROB_UNSIGNED_DRIVER = 0x00000034

        # Device is being used by kernel debugger
        CM_PROB_USED_BY_DEBUGGER = 0x00000035

        # Device is being reset
        CM_PROB_DEVICE_RESET = 0x00000036

        # Device is blocked while console is locked
        CM_PROB_CONSOLE_LOCKED = 0x00000037

        # Device needs extended class configuration to start
        CM_PROB_NEED_CLASS_CONFIG = 0x00000038
        NUM_CM_PROB_V1 = 0x00000025
        NUM_CM_PROB_V2 = 0x00000032
        NUM_CM_PROB_V3 = 0x00000033
        NUM_CM_PROB_V4 = 0x00000034
        NUM_CM_PROB_V5 = 0x00000035
        NUM_CM_PROB_V6 = 0x00000036
        NUM_CM_PROB_V7 = 0x00000037
        NUM_CM_PROB_V8 = 0x00000039
        if NTDDI_VERSION  >= NTDDI_WIN10_RS3:
            NUM_CM_PROB = NUM_CM_PROB_V8
        elif NTDDI_VERSION  >= NTDDI_WINTHRESHOLD:
            NUM_CM_PROB = NUM_CM_PROB_V7
        elif NTDDI_VERSION  >= NTDDI_WINBLUE:
            NUM_CM_PROB = NUM_CM_PROB_V6
        elif NTDDI_VERSION  >= NTDDI_WIN7:
            NUM_CM_PROB = NUM_CM_PROB_V5
        elif NTDDI_VERSION  >= NTDDI_WS08:
            NUM_CM_PROB = NUM_CM_PROB_V4
        elif NTDDI_VERSION  >= NTDDI_WS03:
            NUM_CM_PROB = NUM_CM_PROB_V3
        elif NTDDI_VERSION  >= NTDDI_WINXP:
            NUM_CM_PROB = NUM_CM_PROB_V2
        elif NTDDI_VERSION  >= WIN2K:
            NUM_CM_PROB = NUM_CM_PROB_V1
        # END IF

        # Device Instance status flags, returned by call to
        # CM_Get_DevInst_Status
        # Was enumerated by ROOT
        DN_ROOT_ENUMERATED = 0x00000001

        # Has Register_Device_Driver
        DN_DRIVER_LOADED = 0x00000002

        # Has Register_Enumerator
        DN_ENUM_LOADED = 0x00000004

        # Is currently configured
        DN_STARTED = 0x00000008

        # Manually installed
        DN_MANUAL = 0x00000010

        # May need reenumeration
        DN_NEED_TO_ENUM = 0x00000020

        # Has received a config
        DN_NOT_FIRST_TIME = 0x00000040

        # Enum generates hardware ID
        DN_HARDWARE_ENUM = 0x00000080

        # Lied about can reconfig once
        DN_LIAR = 0x00000100

        # Not CM_Create_DevInst lately
        DN_HAS_MARK = 0x00000200

        # Need device installer
        DN_HAS_PROBLEM = 0x00000400

        # Is filtered
        DN_FILTERED = 0x00000800

        # Has been moved
        DN_MOVED = 0x00001000

        # Can be disabled
        DN_DISABLEABLE = 0x00002000

        # Can be removed
        DN_REMOVABLE = 0x00004000

        # Has a private problem
        DN_PRIVATE_PROBLEM = 0x00008000

        # Multi function parent
        DN_MF_PARENT = 0x00010000

        # Multi function child
        DN_MF_CHILD = 0x00020000

        # DevInst is being removed
        DN_WILL_BE_REMOVED = 0x00040000


        # Windows 4 OPK2 Flags
        # S: Has received a config enumerate
        DN_NOT_FIRST_TIMEE = 0x00080000

        # S: When child is stopped, free resources
        DN_STOP_FREE_RES = 0x00100000

        # S: Don't skip during rebalance
        DN_REBAL_CANDIDATE = 0x00200000

        # Windows 4.1 Flags
        # S: Devnode need lock resume processing
        DN_NEEDS_LOCKING = 0x02000000

        # S: Devnode can be the wakeup device
        DN_ARM_WAKEUP = 0x04000000

        # S: APM aware enumerator
        DN_APM_ENUMERATOR = 0x08000000

        # S: APM aware driver
        DN_APM_DRIVER = 0x10000000

        # S: Silent install
        DN_SILENT_INSTALL = 0x20000000

        # S: No show in device manager
        DN_NO_SHOW_IN_DM = 0x40000000

        # S: Had a problem during preassignment of boot log conf
        DN_BOOT_LOG_PROB = 0x80000000

        # Windows NT Flags
        # These are overloaded on top of unused Win 9X flags
        if NTDDI_VERSION  >= NTDDI_WIN2K:
            # System needs to be restarted for this Devnode to work properly
            DN_NEED_RESTART = DN_LIAR
        # END IF

        if NTDDI_VERSION  >= NTDDI_WINXP:
            # One or more drivers are blocked from loading for this Devnode
            DN_DRIVER_BLOCKED = DN_NOT_FIRST_TIME

            # One or more children have invalid ID(s)
            DN_CHILD_WITH_INVALID_ID = DN_HAS_MARK
        # END IF

        if NTDDI_VERSION  >= NTDDI_WIN8:
            # The function driver for a device reported that the device is not
            # connected. Typically this means a wireless device is out of
            # range.
            DN_DEVICE_DISCONNECTED = DN_NEEDS_LOCKING
        # END IF

        if NTDDI_VERSION  >= NTDDI_WIN10:
            # Device is part of a set of related devices collectively pending
            # query-removal
            DN_QUERY_REMOVE_PENDING = DN_MF_PARENT

            # Device is actively engaged in a query-remove IRP
            DN_QUERY_REMOVE_ACTIVE = DN_MF_CHILD
        # END IF

        DN_CHANGEABLE_FLAGS = (
            DN_NOT_FIRST_TIME +
            DN_HARDWARE_ENUM +
            DN_HAS_MARK +
            DN_DISABLEABLE +
            DN_REMOVABLE +
            DN_MF_CHILD +
            DN_MF_PARENT +
            DN_NOT_FIRST_TIMEE +
            DN_STOP_FREE_RES +
            DN_REBAL_CANDIDATE +
            DN_NT_ENUMERATOR +
            DN_NT_DRIVER +
            DN_SILENT_INSTALL +
            DN_NO_SHOW_IN_DM
        )

        # Logical configuration Priority values
        # These priority values are used in user-mode calls to
        # CM_Add_Empty_Log_Conf.
        # Drivers may also specify priority values for a given IO_RESOURCE_LIST
        # structure by including a ConfigData member union as the first
        # IO_RESOURCE_DESCRIPTOR in the IO_RESOURCE_LIST. In this case, the
        # descriptor
        # type would be CmResourceTypeConfigData.
        # Coming from a forced config
        LCPRI_FORCECONFIG = 0x00000000

        # Coming from a boot config
        LCPRI_BOOTCONFIG = 0x00000001

        # Preferable (better performance)
        LCPRI_DESIRED = 0x00002000

        # Workable (acceptable performance)
        LCPRI_NORMAL = 0x00003000

        # CM only--do not use
        LCPRI_LASTBESTCONFIG = 0x00003FFF

        # Not desired, but will work
        LCPRI_SUBOPTIMAL = 0x00005000

        # CM only--do not use
        LCPRI_LASTSOFTCONFIG = 0x00007FFF

        # Need to restart
        LCPRI_RESTART = 0x00008000

        # Need to reboot
        LCPRI_REBOOT = 0x00009000

        # Need to shutdown/power-off
        LCPRI_POWEROFF = 0x0000A000

        # Need to change a jumper
        LCPRI_HARDRECONFIG = 0x0000C000

        # Cannot be changed
        LCPRI_HARDWIRED = 0x0000E000

        # Impossible configuration
        LCPRI_IMPOSSIBLE = 0x0000F000

        # Disabled configuration
        LCPRI_DISABLED = 0x0000FFFF

        # Maximum known LC Priority
        MAX_LCPRI = 0x0000FFFF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if defined(_MSC_VER):
        if _MSC_VER >= 1200:
            pass
        # END IF
    # END IF

# END IF   _CFG_INCLUDED_


