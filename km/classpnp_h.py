import ctypes
from pyWinAPI import *
from pyWinAPI.missing_structures_h import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _DICTIONARY(ctypes.Structure):
    pass


DICTIONARY = _DICTIONARY
PDICTIONARY = POINTER(_DICTIONARY)


class _CLASSPNP_SCAN_FOR_SPECIAL_INFO(ctypes.Structure):
    pass


CLASSPNP_SCAN_FOR_SPECIAL_INFO = _CLASSPNP_SCAN_FOR_SPECIAL_INFO
PCLASSPNP_SCAN_FOR_SPECIAL_INFO = POINTER(_CLASSPNP_SCAN_FOR_SPECIAL_INFO)


class _SRB_HISTORY_ITEM(ctypes.Structure):
    pass


SRB_HISTORY_ITEM = _SRB_HISTORY_ITEM
PSRB_HISTORY_ITEM = POINTER(_SRB_HISTORY_ITEM)


class _SRB_HISTORY(ctypes.Structure):
    pass


SRB_HISTORY = _SRB_HISTORY
PSRB_HISTORY = POINTER(_SRB_HISTORY)


class GUIDREGINFO(ctypes.Structure):
    pass


PGUIDREGINFO = POINTER(GUIDREGINFO)


class _CLASS_WMI_INFO(ctypes.Structure):
    pass


CLASS_WMI_INFO = _CLASS_WMI_INFO
PCLASS_WMI_INFO = POINTER(_CLASS_WMI_INFO)


class _CLASS_DEV_INFO(ctypes.Structure):
    pass


CLASS_DEV_INFO = _CLASS_DEV_INFO
PCLASS_DEV_INFO = POINTER(_CLASS_DEV_INFO)


class _CLASS_INIT_DATA(ctypes.Structure):
    pass


CLASS_INIT_DATA = _CLASS_INIT_DATA
PCLASS_INIT_DATA = POINTER(_CLASS_INIT_DATA)


class _FILE_OBJECT_EXTENSION(ctypes.Structure):
    pass


FILE_OBJECT_EXTENSION = _FILE_OBJECT_EXTENSION
PFILE_OBJECT_EXTENSION = POINTER(_FILE_OBJECT_EXTENSION)


class _CLASS_WORKING_SET(ctypes.Structure):
    pass


CLASS_WORKING_SET = _CLASS_WORKING_SET
PCLASS_WORKING_SET = POINTER(_CLASS_WORKING_SET)


class _CLASS_INTERPRET_SENSE_INFO2(ctypes.Structure):
    pass


CLASS_INTERPRET_SENSE_INFO2 = _CLASS_INTERPRET_SENSE_INFO2
PCLASS_INTERPRET_SENSE_INFO2 = POINTER(_CLASS_INTERPRET_SENSE_INFO2)


class _CLASS_DRIVER_EXTENSION(ctypes.Structure):
    pass


CLASS_DRIVER_EXTENSION = _CLASS_DRIVER_EXTENSION
PCLASS_DRIVER_EXTENSION = POINTER(_CLASS_DRIVER_EXTENSION)


class _COMMON_DEVICE_EXTENSION(ctypes.Structure):
    pass


COMMON_DEVICE_EXTENSION = _COMMON_DEVICE_EXTENSION
PCOMMON_DEVICE_EXTENSION = POINTER(_COMMON_DEVICE_EXTENSION)


class _CLASS_POWER_OPTIONS(ctypes.Structure):
    pass


CLASS_POWER_OPTIONS = _CLASS_POWER_OPTIONS
PCLASS_POWER_OPTIONS = POINTER(_CLASS_POWER_OPTIONS)


class _CLASS_POWER_CONTEXT(ctypes.Structure):
    pass


CLASS_POWER_CONTEXT = _CLASS_POWER_CONTEXT
PCLASS_POWER_CONTEXT = POINTER(_CLASS_POWER_CONTEXT)


class _CLASS_VPD_B1_DATA(ctypes.Structure):
    pass


CLASS_VPD_B1_DATA = _CLASS_VPD_B1_DATA
PCLASS_VPD_B1_DATA = POINTER(_CLASS_VPD_B1_DATA)


class _CLASS_VPD_B0_DATA(ctypes.Structure):
    pass


CLASS_VPD_B0_DATA = _CLASS_VPD_B0_DATA
PCLASS_VPD_B0_DATA = POINTER(_CLASS_VPD_B0_DATA)


class _CLASS_VPD_B2_DATA(ctypes.Structure):
    pass


CLASS_VPD_B2_DATA = _CLASS_VPD_B2_DATA
PCLASS_VPD_B2_DATA = POINTER(_CLASS_VPD_B2_DATA)


class _CLASS_READ_CAPACITY16_DATA(ctypes.Structure):
    pass


CLASS_READ_CAPACITY16_DATA = _CLASS_READ_CAPACITY16_DATA
PCLASS_READ_CAPACITY16_DATA = POINTER(_CLASS_READ_CAPACITY16_DATA)


class _CLASS_VPD_ECOP_BLOCK_DEVICE_ROD_LIMITS(ctypes.Structure):
    pass


CLASS_VPD_ECOP_BLOCK_DEVICE_ROD_LIMITS = _CLASS_VPD_ECOP_BLOCK_DEVICE_ROD_LIMITS
PCLASS_VPD_ECOP_BLOCK_DEVICE_ROD_LIMITS = POINTER(_CLASS_VPD_ECOP_BLOCK_DEVICE_ROD_LIMITS)


class _CLASS_FUNCTION_SUPPORT_INFO(ctypes.Structure):
    pass


CLASS_FUNCTION_SUPPORT_INFO = _CLASS_FUNCTION_SUPPORT_INFO
PCLASS_FUNCTION_SUPPORT_INFO = POINTER(_CLASS_FUNCTION_SUPPORT_INFO)


class _ADDITIONAL_FDO_DATA(ctypes.Structure):
    pass


ADDITIONAL_FDO_DATA = _ADDITIONAL_FDO_DATA
PADDITIONAL_FDO_DATA = POINTER(_ADDITIONAL_FDO_DATA)


class _FUNCTIONAL_DEVICE_EXTENSION(ctypes.Structure):
    pass


FUNCTIONAL_DEVICE_EXTENSION = _FUNCTIONAL_DEVICE_EXTENSION
PFUNCTIONAL_DEVICE_EXTENSION = POINTER(_FUNCTIONAL_DEVICE_EXTENSION)


class _PHYSICAL_DEVICE_EXTENSION(ctypes.Structure):
    pass


PHYSICAL_DEVICE_EXTENSION = _PHYSICAL_DEVICE_EXTENSION
PPHYSICAL_DEVICE_EXTENSION = POINTER(_PHYSICAL_DEVICE_EXTENSION)


class _COMPLETION_CONTEXT(ctypes.Structure):
    pass


COMPLETION_CONTEXT = _COMPLETION_CONTEXT
PCOMPLETION_CONTEXT = POINTER(_COMPLETION_CONTEXT)


class _CLASS_QUERY_WMI_REGINFO_EX_LIST(ctypes.Structure):
    pass


CLASS_QUERY_WMI_REGINFO_EX_LIST = _CLASS_QUERY_WMI_REGINFO_EX_LIST
PCLASS_QUERY_WMI_REGINFO_EX_LIST = POINTER(_CLASS_QUERY_WMI_REGINFO_EX_LIST)


class _FAILURE_PREDICTION_INFO(ctypes.Structure):
    pass


FAILURE_PREDICTION_INFO = _FAILURE_PREDICTION_INFO
PFAILURE_PREDICTION_INFO = POINTER(_FAILURE_PREDICTION_INFO)


# our first attempt at keeping private data actually private....

class _CLASS_PRIVATE_FDO_DATA(ctypes.Structure):
    pass


CLASS_PRIVATE_FDO_DATA = _CLASS_PRIVATE_FDO_DATA
PCLASS_PRIVATE_FDO_DATA = POINTER(_CLASS_PRIVATE_FDO_DATA)


class _CLASS_PRIVATE_PDO_DATA(ctypes.Structure):
    pass


CLASS_PRIVATE_PDO_DATA = _CLASS_PRIVATE_PDO_DATA
PCLASS_PRIVATE_PDO_DATA = POINTER(_CLASS_PRIVATE_PDO_DATA)


class _CLASS_PRIVATE_COMMON_DATA(ctypes.Structure):
    pass


CLASS_PRIVATE_COMMON_DATA = _CLASS_PRIVATE_COMMON_DATA
PCLASS_PRIVATE_COMMON_DATA = POINTER(_CLASS_PRIVATE_COMMON_DATA)


class _MEDIA_CHANGE_DETECTION_INFO(ctypes.Structure):
    pass


MEDIA_CHANGE_DETECTION_INFO = _MEDIA_CHANGE_DETECTION_INFO
PMEDIA_CHANGE_DETECTION_INFO = POINTER(_MEDIA_CHANGE_DETECTION_INFO)


# Structures for maintaining a dictionary list (list of objects
# referenced by a key value)

class _DICTIONARY_HEADER(ctypes.Structure):
    pass


DICTIONARY_HEADER = _DICTIONARY_HEADER
PDICTIONARY_HEADER = POINTER(_DICTIONARY_HEADER)

# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: classpnp.h Abstract: These are the structures and defines that are
# used in the SCSI class drivers. - -
_CLASS_ = None
if not defined(_CLASS_):
    _CLASS_ = 1

    from pyWinAPI.shared.ntdddisk_h import * # NOQA
    from pyWinAPI.shared.ntddcdrm_h import * # NOQA
    from pyWinAPI.shared.ntddtape_h import * # NOQA
    from pyWinAPI.shared.ntddscsi_h import * # NOQA
    from pyWinAPI.shared.ntddstor_h import * # NOQA
    from pyWinAPI.ucrt.stdio_h import * # NOQA
    from pyWinAPI.shared.scsi_h import * # NOQA
    from pyWinAPI.shared.srb_h import *  # NOQA


    DebugPrint = None
    if defined(DebugPrint):
        pass

    # END IF

    TRY = None
    if defined(TRY):
        pass
    # END IF
    LEAVE = None
    if defined(LEAVE):
        pass
    # END IF
    FINALLY = None
    if defined(FINALLY):
        pass
    # END IF

    ALLOCATE_SRB_FROM_POOL = 0
    # describes the well - known bit masks for ClassDebug, and describes the
    # bits
    # to enable in the debugger to view just those messages.
    # ClassDebugExternalX
    # are reserved for third - party components' debugging use. Anything above
    # 16 will only be printed if the lower two bytes of ClassDebug are higher
    # than the given level (no masking will be available).

    class _CLASS_DEBUG_LEVEL(ENUM):
        ClassDebugError = 0
        ClassDebugWarning = 1
        ClassDebugTrace = 2
        ClassDebugInfo = 3
        if 0:
            ClassDebugInternal = 4
            ClassDebugInternal = 5
            ClassDebugInternal = 6
            ClassDebugInternal = 7
        # END IF
        ClassDebugMediaLocks = 8
        ClassDebugMCN = 9
        ClassDebugDelayedRetry = 10
        ClassDebugSenseInfo = 11
        ClassDebugRemoveLock = 12
        ClassDebugExternal4 = 13
        ClassDebugExternal3 = 14
        ClassDebugExternal2 = 15
        ClassDebugExternal1 = 16

    CLASS_DEBUG_LEVEL = _CLASS_DEBUG_LEVEL
    PCLASS_DEBUG_LEVEL = POINTER(_CLASS_DEBUG_LEVEL)

    if DBG:
        def DebugPrint(x):
            return ClassDebugPrint(x)
    else:
        def DebugPrint(x):
            pass
    # END IF   DBG

    DEBUG_BUFFER_LENGTH = 256

    # Define our private SRB flags. The high nibble of the flag field is
    # reserved for class drivers's private use.
    # Used to indicate that this request shouldn't invoke any power type
    # operations
    # like spinning up the drive.
    SRB_CLASS_FLAGS_LOW_PRIORITY = 0x10000000

    # Used to indicate that the completion routine should not free the srb.
    SRB_CLASS_FLAGS_PERSISTANT = 0x20000000

    # Used to indicate that an SRB is the result of a paging operation.
    SRB_CLASS_FLAGS_PAGING = 0x40000000

    # Used to indicate the completion routine should free the MDL.
    SRB_CLASS_FLAGS_FREE_MDL = 0x80000000

    # Random macros which should probably be in the system header files
    # somewhere.
    def max(a, b):
        return a if a > b else b


    def min(a, b):
        return a if a < b else b


    # Bit Flag Macros
    def SET_FLAG(Flags, Bit):
        Flags |= Bit
        return Flags


    def CLEAR_FLAG(Flags, Bit):
        Flags &= ~Bit
        return Flags


    def TEST_FLAG(Flags, Bit):
        return Flags & Bit != 0


    # neat little hacks to count number of bits set efficiently
    # Helper macros to verify data types and cleanup the code.
    def ASSERT_FDO(x):
        return NT_ASSERT(PCOMMON_DEVICE_EXTENSION(x).DeviceExtension.IsFdo)


    def ASSERT_PDO(x):
        return NT_ASSERT(not PCOMMON_DEVICE_EXTENSION(x).DeviceExtension.IsFdo)


    def IS_CLEANUP_REQUEST(majorFunction):
        return majorFunction in (IRP_MJ_CLOSE, IRP_MJ_CLEANUP, IRP_MJ_SHUTDOWN)


    def DO_MCD(fdoExtension):
        return (
            fdoExtension.MediaChangeDetectionInfo != NULL and
            fdoExtension.MediaChangeDetectionInfo.MediaChangeDetectionDisableCount == 0
        )


    def IS_SCSIOP_READ(opCode):
        return opCode in (SCSIOP_READ6, SCSIOP_READ, SCSIOP_READ12, SCSIOP_READ16)


    def IS_SCSIOP_WRITE(opCode):
        return opCode in (SCSIOP_WRITE6, SCSIOP_WRITE, SCSIOP_WRITE12, SCSIOP_WRITE16)


    def IS_SCSIOP_READWRITE(opCode):
        return IS_SCSIOP_READ(opCode) or IS_SCSIOP_WRITE(opCode)


    def ADJUST_FUA_FLAG(fdoExt):
        if (
            TEST_FLAG(fdoExt.DeviceFlags, DEV_WRITE_CACHE) and
            not TEST_FLAG(fdoExt.DeviceFlags, DEV_POWER_PROTECTED) and
            not TEST_FLAG(fdoExt.ScanForSpecialFlags, CLASS_SPECIAL_FUA_NOT_SUPPORTED)
        ):
            fdoExt.CdbForceUnitAccess = TRUE
        else:
            fdoExt.CdbForceUnitAccess = False

        return fdoExt


    def FREE_POOL(_PoolPtr):
        if _PoolPtr != NULL:
            ExFreePool(_PoolPtr)
            _PoolPtr = NULL

        return _PoolPtr


    POOL_TAGGING = 0
    if defined(POOL_TAGGING):
        def ExAllocatePool(a, b):
            return ExAllocatePoolWithTag(a, b, 'nUcS')

        # ExAllocatePool(a,b) #NT_ASSERT(0)

        def ExAllocatePoolWithQuota(a,b):
            return ExAllocatePoolWithQuotaTag(a, b, 'nUcS')

    # END IF

    CLASS_TAG_AUTORUN_DISABLE = 'ALcS'
    CLASS_TAG_FILE_OBJECT_EXTENSION = 'FLcS'
    CLASS_TAG_MEDIA_CHANGE_DETECTION = 'MLcS'
    CLASS_TAG_MOUNT = 'mLcS'
    CLASS_TAG_RELEASE_QUEUE = 'qLcS'
    CLASS_TAG_POWER = 'WLcS'
    CLASS_TAG_WMI = 'wLcS'
    CLASS_TAG_FAILURE_PREDICT = 'fLcS'
    CLASS_TAG_DEVICE_CONTROL = 'OIcS'
    CLASS_TAG_MODE_DATA = 'oLcS'
    CLASS_TAG_MULTIPATH = 'mPcS'
    CLASS_TAG_LOCK_TRACKING = 'TLcS'
    CLASS_TAG_LB_PROVISIONING = 'PLcS'
    CLASS_TAG_MANAGE_DATASET = 'MDcS'
    CLASS_TAG_ZONE_INFO = 'ZIcS'
    MAXIMUM_RETRIES = 4
    CLASS_DRIVER_EXTENSION_KEY = ClassInitialize

    # Possible values for the IsRemoved flag
    NO_REMOVE = 0
    REMOVE_PENDING = 1
    REMOVE_COMPLETE = 2


    def ClassAcquireRemoveLock(devobj, tag):
        return ClassAcquireRemoveLockEx(devobj, tag, __FILE__, __LINE__)


    # Define start unit timeout to be 4 minutes.
    START_UNIT_TIMEOUT = 60 * 4

    # Define media change test time to be 1 second for quicker response
    MEDIA_CHANGE_DEFAULT_TIME = 1

    # Used to detect the loss of the autorun irp.
    MEDIA_CHANGE_TIMEOUT_TIME = 300

    # Define the various states that media can be in for autorun.
    class _MEDIA_CHANGE_DETECTION_STATE(ENUM):
        MediaUnknown = 1
        MediaPresent = 2
        MediaNotPresent = 3
        MediaUnavailable = 4

    MEDIA_CHANGE_DETECTION_STATE = _MEDIA_CHANGE_DETECTION_STATE
    PMEDIA_CHANGE_DETECTION_STATE = POINTER(_MEDIA_CHANGE_DETECTION_STATE)


    _DICTIONARY._fields_ = [
        ('Signature', ULONGLONG),
        ('List', PDICTIONARY_HEADER),
        ('SpinLock', KSPIN_LOCK),
    ]

    # structures to simplify matching devices, ids, and hacks required for
    # these ids.
    _CLASSPNP_SCAN_FOR_SPECIAL_INFO._fields_ = [
        # * array must end with all three PCHARs being set to NULL.
        ('VendorId', PCHAR),
        ('ProductId', PCHAR),
        ('ProductRevision', PCHAR),
        # so that it may be dynamically built.
        ('Data', ULONG_PTR),
    ]

    if defined(ALLOCATE_SRB_FROM_POOL):
        def ClasspAllocateSrb(ext):
            pass

        def ClasspFreeSrb(ext, srb):
            return ExFreePool(srb)
    else:
        def ClasspAllocateSrb(ext):
            return ExAllocateFromNPagedLookasideList(
                ctypes.byref(ext.CommonExtension.SrbLookasideList)
            )


        def ClasspFreeSrb(ext, srb):
            return ExFreeToNPagedLookasideList(
                ctypes.byref(ext.CommonExtension.SrbLookasideList),
                srb
            )
    # END IF

    # PCLASS_ERROR() Routine Description: This routine is a callback into the
    # driver to handle errors.
    # The queue shall not be unfrozen when this error handler is called,
    # even though the SRB flags may mark the queue as having been
    # frozen due to this SRB.
    # Irql: This routine will be called at KIRQL <= DISPATCH_LEVEL
    # Arguments: DeviceObject is the device object the error occurred on.
    # Srb is the Srb that was being processed when the error occurred.
    # Status may be overwritten by the routine if it decides that the error
    # was benign, or otherwise wishes to change the returned status code for
    # this command Retry may be overwritten to specify that this command
    # should or should not be retried (if the callee supports retrying
    # commands) Return Value: status - -
    #
    # VOID
    # (*PCLASS_ERROR) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PSCSI_REQUEST_BLOCK Srb,
    # _Out_ NTSTATUS *Status,
    # _Inout_ BOOLEAN *Retry
    # );
    PCLASS_ERROR = CALLBACK(
        VOID,
        PDEVICE_OBJECT,
        PSCSI_REQUEST_BLOCK,
        POINTER(NTSTATUS),
        POINTER(BOOLEAN)
    )

    # PCLASS_ADD_DEVICE() Routine Description: This routine is a callback into
    # the driver to create and initialize a new FDO for the corresponding PDO.
    # It may perform property queries on the PDO but cannot do any media
    # access operations. Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged. Arguments: DriverObject is the class
    # driver object this callback is registered for. PDO is the physical
    # device object being added to. Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_ADD_DEVICE) (
    # _In_ PDRIVER_OBJECT DriverObject,
    # _In_ PDEVICE_OBJECT Pdo
    # );
    PCLASS_ADD_DEVICE = CALLBACK(
        NTSTATUS,
        PDRIVER_OBJECT,
        PDEVICE_OBJECT
    )

    # CLASS_POWER_DEVICE() Routine Description: This routine is a callback
    # into the driver to handle power up and power down requests. Most drivers
    # can set this to ClassPowerHandler, which will send a STOP_UNIT on
    # powerdown, and a START_UNIT on powerup. ClassMinimalPowerHandler() may
    # also be used to do nothing for power operations (except succeed them).
    # Please see the DDK for proper handling of
    # IRP_MN_DEVICE_USAGE_NOTIFICATION for details regarding interaction of
    # paging device notifications and the IRQL at which this routine will be
    # called. Irql: This routine will be called at PASSIVE_LEVEL if
    # DO_POWER_PAGABLE is set. This code should NOT be pagable to prevent
    # race conditions during the setting and clearing of the DO_POWER_PAGABLE
    # bit. Arguments: DeviceObject is the device that has the pending power
    # request Irp is the power irp that needs to be handled Return Value:
    # status - -
    #
    # NTSTATUS
    # (*PCLASS_POWER_DEVICE) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp
    # );
    PCLASS_POWER_DEVICE = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        PIRP
    )

    # CLASS_START_DEVICE() Routine Description: This routine is a callback
    # into the driver to initialize the FDO or PDO for all requests,
    # typically due to a IRP_MN_START_DEVICE. Irql: This routine will
    # be called at PASSIVE_LEVEL. Its code may be safely paged.
    # Arguments: DeviceObject is the device object being started Return
    # Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_START_DEVICE) (
    # _In_ PDEVICE_OBJECT DeviceObject
    # );
    PCLASS_START_DEVICE = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT
    )

    # CLASS_STOP_DEVICE() Routine Description: This routine is a callback
    # into the driver to stop the device. For the storage stack, unless
    # there are known issues, this routine need only return. All queueing
    # shall be handled by the lower device drivers. Irql: This routine will
    # be called at PASSIVE_LEVEL. Its code may be safely paged.
    # Arguments: DeviceObject is the device object being stopped/query
    # stopped. Type is the IRP_MN_ type that must be handled.
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_STOP_DEVICE) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ UCHAR Type
    # );
    PCLASS_STOP_DEVICE = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        UCHAR
    )

    # CLASS_INIT_DEVICE() Routine Description: This routine is a callback into
    # the driver to do one - time initialization of new device objects. It
    # shall be called exactly once per device object, and it shall be called
    # prior to CLASS_START_DEVICE() routine. Irql: This routine will be
    # called at PASSIVE_LEVEL. Its code may be safely paged.
    # Arguments: DeviceObject is the device object to be initialized
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_INIT_DEVICE) (
    # _In_ PDEVICE_OBJECT DeviceObject
    # );
    PCLASS_INIT_DEVICE = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT
    )

    # CLASS_ENUM_DEVICE() Routine Description: This routine is a callback
    # into the driver to update the list of PDOs for a given FDO. See
    # DISK.SYS's DiskEnumerateDevice for an example of use. Irql: This
    # routine will be called at PASSIVE_LEVEL. Its code may be safely paged.
    # Arguments: DeviceObject is the FDO which is being enumerated.
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_ENUM_DEVICE) (
    # _In_ PDEVICE_OBJECT DeviceObject
    # );
    PCLASS_ENUM_DEVICE = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT
    )

    # PCLASS_READ_WRITE() Routine Description: This routine is a callback
    # into the driver to verify READ and WRITE irps. If the READ or WRITE
    # request is failed, this routine shall set the Irp's IoStatus.Status
    # to the returned error code and the IoStatus.Information field as
    # appropriate for the given error.
    # Irql: This routine will be called at KIRQL <= DISPATCH_LEVEL
    # Arguments: DeviceObject is the device object being read from or
    # written to Irp is the read or write request being processed
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_READ_WRITE) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp
    # );
    PCLASS_READ_WRITE = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        PIRP,
    )

    # PCLASS_DEVICE_CONTROL() Routine Description: This routine is a callback
    # into the driver to Irql: This routine will only be called at
    # PASSIVE_LEVEL for storage IOCTLs. The code must therefore not be
    # paged, but may call paged code for those ioctls which have been
    # defined to be sent at PASSIVE_LEVEL, such as the storage IOCTLS.
    #  Otherwise KIRQL <= DISPATCH_LEVEL. Arguments: DeviceObject is the
    # device object the IOCTL may be for Irp is the IOCTL request currently
    # being processed Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_DEVICE_CONTROL) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp
    # );
    PCLASS_DEVICE_CONTROL = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        PIRP,
    )

    # PCLASS_SHUTDOWN_FLUSH() Routine Description: This routine is a
    # callback into the driver to handle shutdown and flush irps.
    # These are sent by the system before it actually shuts down or when the
    # file system does a flush. This routine may synchronize the device's
    # media / cache and ensure the device is not locked if the system is in
    # the process of shutting down.
    # Irql: This routine will be called at KIRQL <= DISPATCH_LEVEL
    # Arguments: DeviceObject is the device object that needs to be
    # flushed Irp is the shutdown or flush request currently being processed
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_SHUTDOWN_FLUSH) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp
    # );
    PCLASS_SHUTDOWN_FLUSH = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        PIRP
    )

    # PCLASS_CREATE_CLOSE() Routine Description: This routine is a
    # callback into the driver when the device is opened or closed.
    # Irql: This routine will be called at PASSIVE_LEVEL. Its code may
    # be safely paged.
    # Arguments: DeviceObject that is handling the request Irp is the
    # create or close request currently being processed
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_CREATE_CLOSE) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp
    # );
    PCLASS_CREATE_CLOSE = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        PIRP
    )

    # PCLASS_QUERY_ID() Routine Description: This routine generates the
    # PNP id's for the device's enumerated PDOs. If the specified ID is
    # one that cannot be generated, then the return status shall be
    # STATUS_NOT_IMPLEMENTED so that classpnp shall not handle the request.
    # This routine shall allocate the buffer in the unicode string
    # "IdString" upon success; it is the caller's responsibility to
    # free this buffer when it is done.
    # Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged.
    # Arguments: DeviceObject is the PDO to generate an ID for
    # IdType is the type of ID to be generated UnicodeIdString is
    # the string to place the results into
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_QUERY_ID) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ BUS_QUERY_ID_TYPE IdType,
    # _In_ PUNICODE_STRING IdString
    # );
    PCLASS_QUERY_ID = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        BUS_QUERY_ID_TYPE,
        PUNICODE_STRING
    )

    # PCLASS_REMOVE_DEVICE() Routine Description: This routine is a
    # callback into the driver to release any resources the device may
    # have allocated for the device object.
    # Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged.
    # Arguments: DeviceObject is the device object being
    # removed/query removed/etc.
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_REMOVE_DEVICE) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ UCHAR Type
    # );
    PCLASS_REMOVE_DEVICE = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        UCHAR
    )

    # PCLASS_UNLOAD() Routine Description: This routine is a callback into
    # the driver to unload itself. It must free any resources allocated in
    # the DriverEntry portion of the driver.
    # Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged.
    # Arguments: X Irp is the IOCTL request currently being processed
    # Return Value: status - -
    #
    # VOID
    # (*PCLASS_UNLOAD) (
    # _In_ PDRIVER_OBJECT DriverObject
    # );
    PCLASS_UNLOAD = CALLBACK(
        VOID,
        PDRIVER_OBJECT
    )

    # PCLASS_QUERY_PNP_CAPABILITIES() Routine Description:
    # ISSUE - 2000/02/18 - henrygab - description required
    # Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged.
    # Arguments: PhysicalDeviceObject is the PDO for which this query
    # shall occur Capabilities is a structure that shall be modified by
    # this routine to report the device's capabilities.
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_QUERY_PNP_CAPABILITIES) (
    # _In_ PDEVICE_OBJECT PhysicalDeviceObject,
    # _In_ PDEVICE_CAPABILITIES Capabilities
    # );
    PCLASS_QUERY_PNP_CAPABILITIES = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        PDEVICE_CAPABILITIES
    )

    # PCLASS_TICK() Routine Description: This routine is a callback into
    # the driver that is called once per second.
    # Irql: This routine will be called at DISPATCH_LEVEL
    # Arguments: DeviceObject is the device object for which the timer
    # has fired
    # Return Value: status - -
    #
    # VOID
    # (*PCLASS_TICK) (
    # _In_ PDEVICE_OBJECT DeviceObject
    # );
    PCLASS_TICK = CALLBACK(
        VOID,
        PDEVICE_OBJECT
    )

    # PCLASS_QUERY_WMI_REGINFO_EX() Routine Description: This routine is a
    # callback into the driver to retrieve information about the guids being
    # registered.
    # Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged.
    # Arguments: DeviceObject is the device whose registration information
    # is needed RegFlags returns with a set of flags that describe the
    # guids being registered for this device. If the device wants enable
    # and disable collection callbacks before receiving queries for the
    # registered guids then it should return the WMIREG_FLAG_EXPENSIVE flag.
    # Also the returned flags may specify WMIREG_FLAG_INSTANCE_PDO in which
    #  case the instance name is determined from the PDO associated with the
    # device object. Note that the PDO must have an associated devnode.
    # If WMIREG_FLAG_INSTANCE_PDO is not set then Name must return a unique
    # name for the device. Name returns with the instance name for the guids
    # if WMIREG_FLAG_INSTANCE_PDO is not set in the returned *RegFlags.
    # The caller will call ExFreePool with the buffer returned.
    # MofResourceName returns filled with a static string that contains
    # the name of the MOF resource attached to the drivers image. The
    # caller does not free the buffer as it is expected that the caller
    # will use RtlInitializeUnicodeString to populate it.
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_QUERY_WMI_REGINFO_EX) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _Out_ ULONG *RegFlags,
    # _Out_ PUNICODE_STRING Name,
    # _Out_ PUNICODE_STRING MofResouceName
    # );
    PCLASS_QUERY_WMI_REGINFO_EX = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        POINTER(ULONG),
        PUNICODE_STRING,
        PUNICODE_STRING
    )

    # PCLASS_QUERY_WMI_REGINFO() Routine Description: This routine is a
    # callback into the driver to retrieve information about
    # the guids being registered.
    # Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged.
    # Arguments: DeviceObject is the device whose registration
    # information is needed RegFlags returns with a set of flags
    # that describe the guids being registered for this device.
    # If the device wants enable and disable collection callbacks
    # before receiving queries for the registered guids then it
    # should return the WMIREG_FLAG_EXPENSIVE flag. Also the returned
    # flags may specify WMIREG_FLAG_INSTANCE_PDO in which case the
    # instance name is determined from the PDO associated with the device
    # object. Note that the PDO must have an associated devnode. If
    # WMIREG_FLAG_INSTANCE_PDO is not set then Name must return a unique
    # name for the device. Name returns with the instance name for the
    # guids if WMIREG_FLAG_INSTANCE_PDO is not set in the returned
    # *RegFlags. The caller will call ExFreePool with the buffer
    # returned.
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_QUERY_WMI_REGINFO) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _Out_ ULONG *RegFlags,
    # _Out_ PUNICODE_STRING Name
    # );
    PCLASS_QUERY_WMI_REGINFO = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        POINTER(ULONG),
        PUNICODE_STRING
    )

    # PCLASS_QUERY_WMI_DATABLOCK() Routine Description: This routine is a
    # callback into the driver to query for the contents of a data block.
    # When the driver has finished filling the data block it must call
    # ClassWmiCompleteRequest to complete the irp. The driver can
    # return STATUS_PENDING if the irp cannot be completed immediately.
    # Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged.
    # Arguments: DeviceObject is the device whose data block is being
    # queried Irp is the Irp that makes this request GuidIndex is the index
    # into the list of guids provided when the device registered BufferAvail
    # on has the maximum size available to write the data block. Buffer on
    # return is filled with the returned data block
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_QUERY_WMI_DATABLOCK) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp,
    # _In_ ULONG GuidIndex,
    # _In_ ULONG BufferAvail,
    # _Out_writes_bytes_(BufferAvail) PUCHAR Buffer
    # );
    PCLASS_QUERY_WMI_DATABLOCK = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        PIRP,
        ULONG,
        ULONG,
        PUCHAR
    )

    # PCLASS_SET_WMI_DATABLOCK() Routine Description: This routine is a
    # callback into the driver to query for the contents of a data block.
    # When the driver has finished filling the data block it must call
    # ClassWmiCompleteRequest to complete the irp. The driver can return
    # STATUS_PENDING if the irp cannot be completed immediately.
    # Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged.
    # Arguments: DeviceObject is the device whose data block is being
    # queried Irp is the Irp that makes this request GuidIndex is the
    # index into the list of guids provided when the device registered
    # BufferSize has the size of the data block passed Buffer has the new
    # values for the data block
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_SET_WMI_DATABLOCK) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp,
    # _In_ ULONG GuidIndex,
    # _In_ ULONG BufferSize,
    # _In_reads_bytes_(BufferSize) PUCHAR Buffer
    # );
    PCLASS_SET_WMI_DATABLOCK = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        PIRP,
        ULONG,
        ULONG,
        PUCHAR,
    )

    # PCLASS_SET_WMI_DATAITEM() Routine Description: This routine is a
    # callback into the driver to query for the contents of a data block.
    # When the driver has finished filling the data block it must call
    # ClassWmiCompleteRequest to complete the irp. The driver can return
    # STATUS_PENDING if the irp cannot be completed immediately.
    # Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged.
    # Arguments: DeviceObject is the device whose data block is being queried
    # Irp is the Irp that makes this request GuidIndex is the index into the
    # list of guids provided when the device registered DataItemId has the id
    # of the data item being set BufferSize has the size of the data item
    # passed Buffer has the new values for the data item
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_SET_WMI_DATAITEM) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp,
    # _In_ ULONG GuidIndex,
    # _In_ ULONG DataItemId,
    # _In_ ULONG BufferSize,
    # _In_reads_bytes_(BufferSize) PUCHAR Buffer
    # );
    PCLASS_SET_WMI_DATAITEM = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        PIRP,
        ULONG,
        ULONG,
        ULONG,
        PUCHAR,
    )

    # PCLASS_EXECUTE_WMI_METHOD() Routine Description: This routine is a
    # callback into the driver to execute a method. When the driver has
    # finished filling the data block it must call ClassWmiCompleteRequest to
    # complete the irp. The driver can return STATUS_PENDING if the irp cannot
    # be completed immediately.
    # Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged.
    # Arguments: DeviceObject is the device whose data block is being queried
    # Irp is the Irp that makes this request GuidIndex is the index into the
    # list of guids provided when the device registered MethodId has the id
    # of the method being called InBufferSize has the size of the data block
    # passed in as the input to the method. OutBufferSize on entry has the
    # maximum size available to write the returned data block. Buffer is
    # filled with the returned data block
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_EXECUTE_WMI_METHOD) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp,
    # _In_ ULONG GuidIndex,
    # _In_ ULONG MethodId,
    # _In_ ULONG InBufferSize,
    # _In_ ULONG OutBufferSize,
    # _In_reads_(_Inexpressible_(max(InBufferSize, OutBufferSize))) PUCHAR Buffer
    # );
    PCLASS_EXECUTE_WMI_METHOD = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        PIRP,
        ULONG,
        ULONG,
        ULONG,
        ULONG,
        PUCHAR,
    )


    # used by PCLASS_WMI_FUNCTION_CONTROL
    class CLASSENABLEDISABLEFUNCTION(ENUM):
        EventGeneration = 1
        DataBlockCollection = 2

    EventGeneration = CLASSENABLEDISABLEFUNCTION.EventGeneration
    DataBlockCollection = CLASSENABLEDISABLEFUNCTION.DataBlockCollection

    # PCLASS_WMI_FUNCTION_CONTROL() Routine Description: This routine is a
    # callback into the driver to enabled or disable event generation or
    # data block collection. A device should only expect a single enable
    #  when the first event or data consumer enables events or data collection
    # and a single disable when the last event or data consumer disables
    # events or data collection. Data blocks will only receive collection
    # enable/disable if they were registered as requiring it.
    # Irql: This routine will be called at PASSIVE_LEVEL.
    # Its code may be safely paged.
    # Arguments: DeviceObject is the device whose data block is being queried
    # GuidIndex is the index into the list of guids provided when the device
    # registered Function specifies which functionality is being enabled or
    # disabled Enable is TRUE then the function is being enabled else disabled
    # Return Value: status - -
    #
    # NTSTATUS
    # (*PCLASS_WMI_FUNCTION_CONTROL) (
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp,
    # _In_ ULONG GuidIndex,
    # _In_ CLASSENABLEDISABLEFUNCTION Function,
    # _In_ BOOLEAN Enable
    # );
    PCLASS_WMI_FUNCTION_CONTROL = CALLBACK(
        NTSTATUS,
        PDEVICE_OBJECT,
        PIRP,
        ULONG,
        CLASSENABLEDISABLEFUNCTION,
        BOOLEAN,
    )

    # This structure defines the history kept for a given transfer packet.
    # It includes a srb status/sense data structure that is always either
    # valid or zero - filled for the full 18 bytes, time sent/completed,
    # and how long the retry delay was requested to be. - -
    #
    _SRB_HISTORY_ITEM._fields_ = [
        # 0x00..0x07
        ('TickCountSent', LARGE_INTEGER),
        # 0x08..0x0F
        ('TickCountCompleted', LARGE_INTEGER),
        # 0x10..0x13
        ('MillisecondsDelayOnRetry', ULONG),
        # 0x14..0x25 (0x12 bytes)
        ('NormalizedSenseData', SENSE_DATA),
        # 0x26
        ('SrbStatus', UCHAR),
        # 0x27 - - one byte free (alignment)
        ('ClassDriverUse', UCHAR),
    ]

    _SRB_HISTORY._fields_ = [
        # for the class driver to use as they please
        ('ClassDriverUse', ULONG_PTR * 4),
        ('TotalHistoryCount', ULONG),
        ('UsedHistoryCount', ULONG),
        ('History', SRB_HISTORY_ITEM * 1),
    ]

    # PCLASS_INTERPRET_SENSE_INFO() Routine Description: This routine is a
    # callback into the driver to perform interpretation of the errors that
    # may have occurred during an SRB transfer. It closely matches the API
    # set of ClassInterpretSenseInfo, with modifications to allow for a
    # history of why the request was previously retried (and when), and
    # changes the retry interval from being in seconds to being in
    # milliseconds. Finally, use of this extended API removes all retry
    # logic from classpnp for these requests. Thus, the provided routine
    # must return FALSE when it determines the number of times the request
    # should be retried has been exceeded.
    # Irql: This routine will be called at KIRQL <= DISPATCH_LEVEL
    # NOTE: Although it is not illegal to have both a
    # PCLASS_INTERPRET_SENSE_INFO() and a PCLASS_ERROR() routine,
    # the PCLASS_ERROR() function will only be called if the class driver
    # (as part of its PCLASS_INTERPRET_SENSE_INFO() routine) calls into the
    # legacy ClassInterpretSenseInfo().
    # Arguments:
    # Return Value: TRUE if the request should be retried FALSE
    # if the request should be failed - -
    #
    # NOTE: Start with a smaller 100 second maximum, due to current NT_ASSERT
    # in CLASSPNP
    # 0x0000 00C9'2A69 C000 (864,000,000,000) is 24 hours in 100ns units
    # 0x0000 0000'3B9A CA00 ( 1,000,000,000) is 100 seconds in 100ns units
    MAXIMUM_RETRY_FOR_SINGLE_IO_IN_100NS_UNITS = 0x3B9ACA00

    # BOOLEAN
    # (*PCLASS_INTERPRET_SENSE_INFO) (
    # _In_      PDEVICE_OBJECT      Fdo,
    # _In_opt_  PIRP                OriginalRequest, // not always the same as in SRB
    # _In_      PSCSI_REQUEST_BLOCK Srb,
    # _In_      UCHAR               MajorFunctionCode,
    # _In_      ULONG               IoDeviceCode,
    # _In_      ULONG               PreviousRetryCount,
    # // except for bits explicitly set aside for class driver to update
    # _In_opt_  SRB_HISTORY *       RequestHistory,
    # _Out_     NTSTATUS    *       Status,
    # _Out_ _Deref_out_range_(0,MAXIMUM_RETRY_FOR_SINGLE_IO_IN_100NS_UNITS)
    # LONGLONG * RetryIn100nsUnits
    # );
    PCLASS_INTERPRET_SENSE_INFO = CALLBACK(
        BOOLEAN,
        PDEVICE_OBJECT,
        PIRP,
        PSCSI_REQUEST_BLOCK,
        UCHAR,
        ULONG,
        ULONG,
        ULONG,
        POINTER(SRB_HISTORY),
        POINTER(NTSTATUS),
        POINTER(LONGLONG),
    )

    # PCLASS_COMPRESS_HISTORY_DATA() Routine Description: This routine is a
    # callback into the driver to perform "compression" of the history data
    # that is saved during retry of SRBs. The function will only be called
    # when the history array is full (UsedHistoryCount == TotalHistoryCount).
    # This function must reduce the overall UsedHistoryCount by at least one
    # element (and update the UsedHistoryCount field appropriately). . that
    # may have occurred during an SRB transfer. It closely matches the API set
    # of ClassInterpretSenseInfo, with modifications to allow for a history of
    # why the request was previously retried (and when), and changes the retry
    # interval from being in seconds to being in milliseconds. Finally, use of
    # this extended API removes all retry logic from classpnp for these
    # requests. Thus, the provided routine must return FALSE when it
    # determines the number of times the request should be retried has been
    # exceeded.
    # Irql: This routine will be called at KIRQL <= DISPATCH_LEVEL
    # NOTE: Although it is not illegal to have both a
    # PCLASS_INTERPRET_SENSE_INFO() and a PCLASS_ERROR() routine,
    # the PCLASS_ERROR() function will only be called if the class driver
    # (as part of its PCLASS_INTERPRET_SENSE_INFO() routine) calls into the
    # legacy ClassInterpretSenseInfo().
    # Arguments: - -
    #
    # VOID
    # (*PCLASS_COMPRESS_RETRY_HISTORY_DATA) (
    # _In_     PDEVICE_OBJECT DeviceObject,
    # _Inout_  PSRB_HISTORY   RequestHistory
    # );
    PCLASS_COMPRESS_RETRY_HISTORY_DATA = CALLBACK(
        VOID,
        PDEVICE_OBJECT,
        PSRB_HISTORY,
    )


    # Restricted - May only append to this structure for backwards
    # compatibility
    GUIDREGINFO._fields_ = [
        # Guid to registered
        ('Guid', GUID),
        # Count of Instances of Datablock
        ('InstanceCount', ULONG),
        # Additional flags (see WMIREGINFO in wmistr.h)
        ('Flags', ULONG),
    ]

    # Restricted - May only append to this structure for backwards
    # compatibility
    _CLASS_WMI_INFO._fields_ = [
        ('GuidCount', ULONG),
        ('GuidRegInfo', PGUIDREGINFO),
        ('ClassQueryWmiRegInfo', PCLASS_QUERY_WMI_REGINFO),
        ('ClassQueryWmiDataBlock', PCLASS_QUERY_WMI_DATABLOCK),
        ('ClassSetWmiDataBlock', PCLASS_SET_WMI_DATABLOCK),
        ('ClassSetWmiDataItem', PCLASS_SET_WMI_DATAITEM),
        ('ClassExecuteWmiMethod', PCLASS_EXECUTE_WMI_METHOD),
        ('ClassWmiFunctionControl', PCLASS_WMI_FUNCTION_CONTROL),
    ]

    # Restricted - May only append to this structure for backwards
    # compatibility
    _CLASS_DEV_INFO._fields_ = [
        # If this is zero, the driver does not expect to have any PDO's
        ('DeviceExtensionSize', ULONG),
        ('DeviceType', DEVICE_TYPE),
        ('StackSize', UCHAR),
        # FILE_VIRTUAL_VOLUME
        ('DeviceCharacteristics', ULONG),
        ('ClassError', PCLASS_ERROR),
        ('ClassReadWriteVerification', PCLASS_READ_WRITE),
        ('ClassDeviceControl', PCLASS_DEVICE_CONTROL),
        ('ClassShutdownFlush', PCLASS_SHUTDOWN_FLUSH),
        ('ClassCreateClose', PCLASS_CREATE_CLOSE),
        ('ClassInitDevice', PCLASS_INIT_DEVICE),
        ('ClassStartDevice', PCLASS_START_DEVICE),
        ('ClassPowerDevice', PCLASS_POWER_DEVICE),
        ('ClassStopDevice', PCLASS_STOP_DEVICE),
        ('ClassRemoveDevice', PCLASS_REMOVE_DEVICE),
        ('ClassQueryPnpCapabilities', PCLASS_QUERY_PNP_CAPABILITIES),
        # Registered Data Block info for wmi
        ('ClassWmiInfo', CLASS_WMI_INFO),
    ]

    # Restricted - May only append to this structure for backwards
    # compatibility
    _CLASS_INIT_DATA._fields_ = [
        # This structure size - version checking.
        ('InitializationDataSize', ULONG),
        # Specific init data for functional and physical device objects.
        ('FdoData', CLASS_DEV_INFO),
        ('PdoData', CLASS_DEV_INFO),
        # Device - specific driver routines
        ('ClassAddDevice', PCLASS_ADD_DEVICE),
        ('ClassEnumerateDevice', PCLASS_ENUM_DEVICE),
        ('ClassQueryId', PCLASS_QUERY_ID),
        ('ClassStartIo', PDRIVER_STARTIO),
        ('ClassUnload', PCLASS_UNLOAD),
        ('ClassTick', PCLASS_TICK),
    ]

    # this is a private structure, but must be kept here
    # to properly compile size of FUNCTIONAL_DEVICE_EXTENSION
    _FILE_OBJECT_EXTENSION._fields_ = [
        ('FileObject', PFILE_OBJECT),
        ('DeviceObject', PDEVICE_OBJECT),
        ('LockCount', ULONG),
        ('McnDisableCount', ULONG),
    ]

    _CLASS_WORKING_SET._fields_ = [
        # Must be (ctypes.sizeof(CLASS_WORKING_SET)
        ('Size', ULONG),
        # NOTE: This range can be made larger more easily than it can be
        # reduced
        ('XferPacketsWorkingSetMaximum', ULONG),
        ('XferPacketsWorkingSetMinimum', ULONG),
    ]
    CLASS_WORKING_SET_MAXIMUM = 2048
    _CLASS_INTERPRET_SENSE_INFO2._fields_ = [
        # Must be (ctypes.sizeof(CLASS_INTERPRET_SENSE_INFO2)
        ('Size', ULONG),
        # The number of SRB_HISTORY units that will be used
        ('HistoryCount', ULONG),
        ('Compress', PCLASS_COMPRESS_RETRY_HISTORY_DATA),
        ('Interpret', PCLASS_INTERPRET_SENSE_INFO),
    ]
    # A compile - time check of the 30,000 limit not overflowing ULONG size...
    # Note that it is not expected that a release (FRE) driver will normally
    # have such a large history, instead using the compression function.
    CLASS_INTERPRET_SENSE_INFO2_MAXIMUM_HISTORY_COUNT = 30000
    # Bit flags for SRB support in class drivers
    CLASS_SRB_SCSI_REQUEST_BLOCK = 0x1
    CLASS_SRB_STORAGE_REQUEST_BLOCK = 0x2
    # Restricted - May only append to this structure for backwards
    # compatibility

    _TEMP__CLASS_DRIVER_EXTENSION = [
        ('RegistryPath', UNICODE_STRING),
        ('InitData', CLASS_INIT_DATA),
        ('DeviceCount', ULONG)
    ]
    if NTDDI_VERSION >= NTDDI_WINXP:
        _TEMP__CLASS_DRIVER_EXTENSION +=  [
            ('ClassFdoQueryWmiRegInfoEx', PCLASS_QUERY_WMI_REGINFO_EX),
            ('ClassPdoQueryWmiRegInfoEx', PCLASS_QUERY_WMI_REGINFO_EX),
        ]
    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        _TEMP__CLASS_DRIVER_EXTENSION += [
            ('EtwHandle', REGHANDLE),
            ('DeviceMajorFunctionTable', PDRIVER_DISPATCH * IRP_MJ_MAXIMUM_FUNCTION + 1),
            ('MpDeviceMajorFunctionTable', PDRIVER_DISPATCH * IRP_MJ_MAXIMUM_FUNCTION + 1),
            # setup during DriverEntry, so must be placed here.
            ('InterpretSenseInfo', PCLASS_INTERPRET_SENSE_INFO2),
            # setup during DriverEntry, so must be placed here.
            ('WorkingSet', PCLASS_WORKING_SET)
        ]
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN8:
        _TEMP__CLASS_DRIVER_EXTENSION += [
            # Need to setup during DriverEntry, so must be placed here.
            ('SrbSupport', ULONG),
        ]
    # END IF

    _CLASS_DRIVER_EXTENSION._fields_ = _TEMP__CLASS_DRIVER_EXTENSION

    PCOMMON_DEVICE_EXTENSION = POINTER(COMMON_DEVICE_EXTENSION)
    PFUNCTIONAL_DEVICE_EXTENSION = POINTER(FUNCTIONAL_DEVICE_EXTENSION)


    PPHYSICAL_DEVICE_EXTENSION = POINTER(PHYSICAL_DEVICE_EXTENSION)

    # Restricted - May only append to this structure for backwards
    # compatibility

    class _Struct_1(ctypes.Structure):
        pass

    _COMMON_DEVICE_EXTENSION._anonymous_ = (
        '_Struct_1',
    )

    _Struct_1._fields_ = [
        ('IsFdo', BOOLEAN,  1),
        ('IsInitialized', BOOLEAN, 1),
        # Flag indicating whether the lookaside listhead for srbs has been
        # initialized.
        ('IsSrbLookasideListInitialized', BOOLEAN, 1)
    ]

    _COMMON_DEVICE_EXTENSION._Struct_1 = _Struct_1

    _TEMP__COMMON_DEVICE_EXTENSION = [
        # for any class driver using classpnp or a later version.
        ('Version', ULONG),
        # pointer so they can reference this with a bit of syntactic sugar.
        ('DeviceObject', PDEVICE_OBJECT),
        # Pointer to lower device object - send all requests through this
        ('LowerDeviceObject', PDEVICE_OBJECT),
        # routines need to access
        ('PartitionZeroExtension', PFUNCTIONAL_DEVICE_EXTENSION),
        # efficient than constantly getting the driver extension.
        ('DriverExtension', PCLASS_DRIVER_EXTENSION),
        # ClassDecrementRemoveLock.
        ('RemoveLock', LONG),
        # This event will be signalled when it is safe to remove the device
        # object
        ('RemoveEvent', KEVENT),
        # initialized to ff
        ('RemoveTrackingSpinlock', KSPIN_LOCK),
        ('RemoveTrackingList', PVOID),
        ('RemoveTrackingUntrackedCount', LONG),
        # Pointer to the driver specific data area
        ('DriverData', PVOID),
        #  Flag indicates whether this device object is
        # an FDO or a PDO
        ('_Struct_1', _COMMON_DEVICE_EXTENSION._Struct_1),
        # Contains the IRP_MN_CODE of the last state-changing pnp irps we
        # recieved (XXX_STOP, XXX_REMOVE, START, etc...).  Used in concert
        # with IsRemoved.
        ('PreviousState', UCHAR),
        ('CurrentState', UCHAR),
        # interlocked flag indicating that the device has been removed.
        ('IsRemoved', ULONG),
        # The name of the object
        ('DeviceName', UNICODE_STRING),
        # The next child device (or if this is an FDO, the first child device).
        ('ChildList', PPHYSICAL_DEVICE_EXTENSION),
        # Number of the partition or -1L if not partitionable.
        ('PartitionNumber', ULONG),
        # Length of partition in bytes
        ('PartitionLength', LARGE_INTEGER),
        # Number of bytes before start of partition
        ('StartingOffset', LARGE_INTEGER),
        # Dev-Info structure for this type of device object
        # Contains call-out routines for the class driver.
        ('DevInfo', PCLASS_DEV_INFO),
        # Count of page files going through this device object
        # and event to synchronize them with.
        ('PagingPathCount', ULONG),
        ('DumpPathCount', ULONG),
        ('HibernationPathCount', ULONG),
        ('PathCountEvent', KEVENT)
    ]

    if defined(ALLOCATE_SRB_FROM_POOL):
        _TEMP__COMMON_DEVICE_EXTENSION += [
             # Lookaside listhead for srbs.
            ('SrbLookasideList', NPAGED_LOOKASIDE_LIST)
        ]
    # END IF

    _TEMP__COMMON_DEVICE_EXTENSION += [
        # Interface name string returned by IoRegisterDeviceInterface.
        ('MountedDeviceInterfaceName', UNICODE_STRING),
        # Registered Data Block info for wmi
        ('GuidCount', ULONG),
        ('GuidRegInfo', PGUIDREGINFO),
        # File object dictionary for this device object.  Extensions are stored
        # in here rather than off the actual file object.
        ('FileObjectDictionary', DICTIONARY)
    ]


    # The following will be in the released product as reserved.
    # Leave these at the end of the structure.

    if NTDDI_VERSION >= NTDDI_WINXP:
        _TEMP__COMMON_DEVICE_EXTENSION += [
            ('PrivateCommonData', PCLASS_PRIVATE_COMMON_DATA)
        ]
    else:
        _TEMP__COMMON_DEVICE_EXTENSION += [
            ('Reserved1', ULONG_PTR)
        ]

    if NTDDI_VERSION >= NTDDI_VISTA:
        _TEMP__COMMON_DEVICE_EXTENSION += [
            # Pointer to the dispatch table for this object
            ('DispatchTable', POINTER(PDRIVER_DISPATCH))
        ]
    else:
        _TEMP__COMMON_DEVICE_EXTENSION += [
            ('Reserved2', ULONG_PTR)
        ]

    _TEMP__COMMON_DEVICE_EXTENSION += [
        ('Reserved3', ULONG_PTR),
        ('Reserved4', ULONG_PTR),
    ]

    _COMMON_DEVICE_EXTENSION._fields_ = _TEMP__COMMON_DEVICE_EXTENSION

    class FAILURE_PREDICTION_METHOD(ENUM):
        FailurePredictionNone = 0
        FailurePredictionIoctl = 1
        FailurePredictionSmart = 2
        FailurePredictionSense = 3


    PFAILURE_PREDICTION_METHOD = POINTER(FAILURE_PREDICTION_METHOD)

    FailurePredictionNone = FAILURE_PREDICTION_METHOD.FailurePredictionNone
    FailurePredictionIoctl = FAILURE_PREDICTION_METHOD.FailurePredictionIoctl
    FailurePredictionSmart = FAILURE_PREDICTION_METHOD.FailurePredictionSmart
    FailurePredictionSense = FAILURE_PREDICTION_METHOD.FailurePredictionSense

    # Default failure prediction polling interval is every hour
    DEFAULT_FAILURE_PREDICTION_PERIOD = 60 * 60 * 1

    # The failure prediction structure is internal to classpnp - drivers do not
    # need to know what it contains.

    if _MSC_VER >= 1200:
        pass
    # END IF

    # this is to allow for common code to handle
    # every option.
    _CLASS_POWER_OPTIONS._fields_ = [
        ('PowerDown', ULONG, 1),
        ('LockQueue', ULONG, 1),
        ('HandleSpinDown', ULONG, 1),
        ('HandleSpinUp', ULONG, 1),
        ('Reserved', ULONG, 27),
    ]
    if _MSC_VER >= 1200:
        pass
    # END IF

    # this is a private structure, but must be kept here
    # to properly compile size of FUNCTIONAL_DEVICE_EXTENSION
    class CLASS_POWER_DOWN_STATE(ENUM):
        PowerDownDeviceInitial = 1
        PowerDownDeviceLocked = 2
        PowerDownDeviceStopped = 3
        PowerDownDeviceOff = 4
        PowerDownDeviceUnlocked = 5

    PowerDownDeviceInitial = CLASS_POWER_DOWN_STATE.PowerDownDeviceInitial
    PowerDownDeviceLocked = CLASS_POWER_DOWN_STATE.PowerDownDeviceLocked
    PowerDownDeviceStopped = CLASS_POWER_DOWN_STATE.PowerDownDeviceStopped
    PowerDownDeviceOff = CLASS_POWER_DOWN_STATE.PowerDownDeviceOff
    PowerDownDeviceUnlocked = CLASS_POWER_DOWN_STATE.PowerDownDeviceUnlocked

    # same as above, but with an extra state.
    # should be ok to change the above structure, but that
    # would break someone somewhere who ignore the PRIVATE
    # nature of the structure.
    class CLASS_POWER_DOWN_STATE2(ENUM):
        PowerDownDeviceInitial2 = 1
        PowerDownDeviceLocked2 = 2
        PowerDownDeviceFlushed2 = 3
        PowerDownDeviceStopped2 = 4
        PowerDownDeviceOff2 = 5
        PowerDownDeviceUnlocked2 = 6

    PowerDownDeviceInitial2 = CLASS_POWER_DOWN_STATE2.PowerDownDeviceInitial2
    PowerDownDeviceLocked2 = CLASS_POWER_DOWN_STATE2.PowerDownDeviceLocked2
    PowerDownDeviceFlushed2 = CLASS_POWER_DOWN_STATE2.PowerDownDeviceFlushed2
    PowerDownDeviceStopped2 = CLASS_POWER_DOWN_STATE2.PowerDownDeviceStopped2
    PowerDownDeviceOff2 = CLASS_POWER_DOWN_STATE2.PowerDownDeviceOff2
    PowerDownDeviceUnlocked2 = CLASS_POWER_DOWN_STATE2.PowerDownDeviceUnlocked2

    # same as above, but with an extra state regarding to device quiescence
    class CLASS_POWER_DOWN_STATE3(ENUM):
        PowerDownDeviceInitial3 = 0
        PowerDownDeviceLocked3 = 1
        PowerDownDeviceQuiesced3 = 2
        PowerDownDeviceFlushed3 = 3
        PowerDownDeviceStopped3 = 4
        PowerDownDeviceOff3 = 5
        PowerDownDeviceUnlocked3 = 6

    PowerDownDeviceInitial3 = CLASS_POWER_DOWN_STATE3.PowerDownDeviceInitial3
    PowerDownDeviceLocked3 = CLASS_POWER_DOWN_STATE3.PowerDownDeviceLocked3
    PowerDownDeviceQuiesced3 = CLASS_POWER_DOWN_STATE3.PowerDownDeviceQuiesced3
    PowerDownDeviceFlushed3 = CLASS_POWER_DOWN_STATE3.PowerDownDeviceFlushed3
    PowerDownDeviceStopped3 = CLASS_POWER_DOWN_STATE3.PowerDownDeviceStopped3
    PowerDownDeviceOff3 = CLASS_POWER_DOWN_STATE3.PowerDownDeviceOff3
    PowerDownDeviceUnlocked3 = CLASS_POWER_DOWN_STATE3.PowerDownDeviceUnlocked3

    # this is a private enum, but must be kept here
    # to properly compile size of FUNCTIONAL_DEVICE_EXTENSION
    class CLASS_POWER_UP_STATE(ENUM):
        PowerUpDeviceInitial = 1
        PowerUpDeviceLocked = 2
        PowerUpDeviceOn = 3
        PowerUpDeviceStarted = 4
        PowerUpDeviceUnlocked = 5

    PowerUpDeviceInitial = CLASS_POWER_UP_STATE.PowerUpDeviceInitial
    PowerUpDeviceLocked = CLASS_POWER_UP_STATE.PowerUpDeviceLocked
    PowerUpDeviceOn = CLASS_POWER_UP_STATE.PowerUpDeviceOn
    PowerUpDeviceStarted = CLASS_POWER_UP_STATE.PowerUpDeviceStarted
    PowerUpDeviceUnlocked = CLASS_POWER_UP_STATE.PowerUpDeviceUnlocked

    # this is a private structure, but must be kept here
    # to properly compile size of FUNCTIONAL_DEVICE_EXTENSION
    class PowerChangeState(ctypes.Union):
        pass


    PowerChangeState._fields_ = [
        ('PowerDown', CLASS_POWER_DOWN_STATE),
        ('PowerDown2', CLASS_POWER_DOWN_STATE2),
        ('PowerDown3', CLASS_POWER_DOWN_STATE3),
        ('PowerUp', CLASS_POWER_UP_STATE),
    ]
    _CLASS_POWER_CONTEXT.PowerChangeState = PowerChangeState


    _CLASS_POWER_CONTEXT._fields_ = [
        ('PowerChangeState', _CLASS_POWER_CONTEXT.PowerChangeState),
        ('Options', CLASS_POWER_OPTIONS),
        ('InUse', BOOLEAN),
        ('QueueLocked', BOOLEAN),
        ('FinalStatus', NTSTATUS),
        ('RetryCount', ULONG),
        ('RetryInterval', ULONG),
        ('CompletionRoutine', PIO_COMPLETION_ROUTINE),
        ('DeviceObject', PDEVICE_OBJECT),
        ('Irp', PIRP),
        ('Srb', SCSI_REQUEST_BLOCK),
    ]

    # This structure is used to keep supportive information for
    # IOCTL_STORAGE_QUERY_PROPERTY,
    # especially for propertyid: StorageAccessAlignmentProperty,
    # StorageDeviceSeekPenaltyProperty and StorageDeviceTrimProperty.
    # Current implementation is to support them on for Disk device. As there
    # is possibility for other devices to use the same mechanism,
    # this information is kept in structure FUNCTIONAL_DEVICE_EXTENSION.
    class CLASS_FUNCTION_SUPPORT(ENUM):
        SupportUnknown = 0
        Supported = 1
        NotSupported = 2

    SupportUnknown = CLASS_FUNCTION_SUPPORT.SupportUnknown
    Supported = CLASS_FUNCTION_SUPPORT.Supported
    NotSupported = CLASS_FUNCTION_SUPPORT.NotSupported

    _CLASS_VPD_B1_DATA._fields_ = [
        ('CommandStatus', NTSTATUS),
        # Non - rotating medium if the value is 0001h
        ('MediumRotationRate', USHORT),
        ('NominalFormFactor', UCHAR),
        ('Zoned', UCHAR),
        ('MediumProductType', ULONG),
        ('DepopulationTime', ULONG),
    ]

    _CLASS_VPD_B0_DATA._fields_ = [
        ('CommandStatus', NTSTATUS),
        ('MaxUnmapLbaCount', ULONG),
        ('MaxUnmapBlockDescrCount', ULONG),
        ('OptimalUnmapGranularity', ULONG),
        ('UnmapGranularityAlignment', ULONG),
        ('UGAVALID', BOOLEAN),
        ('Reserved0', UCHAR),
        ('OptimalTransferLengthGranularity', USHORT),
        ('MaximumTransferLength', ULONG),
        ('OptimalTransferLength', ULONG),
    ]
    if _MSC_VER >= 1600:
        pass
    # END IF

    _CLASS_VPD_B2_DATA._fields_ = [
        ('CommandStatus', NTSTATUS),
        ('ThresholdExponent', UCHAR),
        ('DP', UCHAR, 1),
        ('ANC_SUP', UCHAR, 1),
        ('Reserved0', UCHAR, 2),
        ('LBPRZ', UCHAR, 1),
        ('LBPWS10', UCHAR, 1),
        ('LBPWS', UCHAR, 1),
        ('LBPU', UCHAR, 1),
        ('ProvisioningType', UCHAR, 3),
        ('Reserved1', UCHAR, 5),
        ('SoftThresholdEventPending', ULONG),
    ]
    if _MSC_VER >= 1600:
        pass
    # END IF

    _CLASS_READ_CAPACITY16_DATA._fields_ = [
        ('CommandStatus', NTSTATUS),
        ('BytesPerLogicalSector', ULONG),
        ('BytesPerPhysicalSector', ULONG),
        # starting offset of Logical Sector inside Physical Sector
        ('BytesOffsetForSectorAlignment', ULONG),
        # Don't use this field, use the Provisioning Type from VPD page 0xB2
        # instead.
        ('LBProvisioningEnabled', BOOLEAN),
        # Don't use this field, use LBPRZ from VPD page 0xB2 instead.
        ('LBProvisioningReadZeros', BOOLEAN),
        ('Reserved0', UCHAR * 2),
        ('Reserved1', ULONG),
    ]

    _CLASS_VPD_ECOP_BLOCK_DEVICE_ROD_LIMITS._fields_ = [
        ('CommandStatus', NTSTATUS),
        ('MaximumRangeDescriptors', USHORT),
        ('Restricted', UCHAR),
        ('Reserved', UCHAR),
        ('MaximumInactivityTimer', ULONG),
        ('DefaultInactivityTimer', ULONG),
        ('MaximumTokenTransferSize', ULONGLONG),
        ('OptimalTransferCount', ULONGLONG),
    ]

    # Restricted - May only append to this structure for backwards
    # compatibility
    class ValidInquiryPages(ctypes.Structure):
        pass


    ValidInquiryPages._fields_ = [
        ('BlockLimits', ULONG, 1),
        ('BlockDeviceCharacteristics', ULONG, 1),
        ('LBProvisioning', ULONG, 1),
        ('BlockDeviceRODLimits', ULONG, 1),
        ('ZonedBlockDeviceCharacteristics', ULONG, 1),
        ('Reserved', ULONG, 22),
        ('DeviceType', ULONG, 5),
    ]
    _CLASS_FUNCTION_SUPPORT_INFO.ValidInquiryPages = ValidInquiryPages


    class LowerLayerSupport(ctypes.Structure):
        pass


    LowerLayerSupport._fields_ = [
        ('SeekPenaltyProperty', CLASS_FUNCTION_SUPPORT),
        ('AccessAlignmentProperty', CLASS_FUNCTION_SUPPORT),
        ('TrimProperty', CLASS_FUNCTION_SUPPORT),
        ('TrimProcess', CLASS_FUNCTION_SUPPORT),
    ]
    _CLASS_FUNCTION_SUPPORT_INFO.LowerLayerSupport = LowerLayerSupport


    class IdlePower(ctypes.Structure):
        pass


    IdlePower._fields_ = [
        ('D3ColdSupported', ULONG, 1),
        ('DeviceWakeable', ULONG, 1),
        ('IdlePowerEnabled', ULONG, 1),
        # Idle timeout has been overridden by user
        ('D3IdleTimeoutOverridden', ULONG, 1),
        ('NoVerifyDuringIdlePower', ULONG, 1),
        ('Reserved2', ULONG, 27),
        # The D3 idle timeout in milliseconds.
        ('D3IdleTimeout', ULONG),
    ]

    _CLASS_FUNCTION_SUPPORT_INFO.IdlePower = IdlePower

    _TEMP__CLASS_FUNCTION_SUPPORT_INFO = [
        # are expected to change after initialization
        ('SyncLock', KSPIN_LOCK),
        ('GenerationCount', ULONG),
        ('ChangeRequestCount', ULONG),
        # VPD page support info, from INQUIRY - VPD Support Pages
        ('ValidInquiryPages', _CLASS_FUNCTION_SUPPORT_INFO.ValidInquiryPages),
        # IOCTL/Function supported by lower layer driver
        ('LowerLayerSupport', _CLASS_FUNCTION_SUPPORT_INFO.LowerLayerSupport),
        # user setting in registry
        ('RegAccessAlignmentQueryNotSupported', BOOLEAN),
        ('AsynchronousNotificationSupported', BOOLEAN)
    ]
    if NTDDI_VERSION >= NTDDI_WIN10_RS:
        _TEMP__CLASS_FUNCTION_SUPPORT_INFO += [
            ('UseModeSense10', BOOLEAN),
            ('Reserved', UCHAR)
        ]
    else:
        _TEMP__CLASS_FUNCTION_SUPPORT_INFO += [
            ('Reserved', UCHAR * 2)
        ]

    _TEMP__CLASS_FUNCTION_SUPPORT_INFO += [
        # cached data
        ('BlockLimitsData', CLASS_VPD_B0_DATA),
        ('DeviceCharacteristicsData', CLASS_VPD_B1_DATA),
        ('LBProvisioningData', CLASS_VPD_B2_DATA),
        ('ReadCapacity16Data', CLASS_READ_CAPACITY16_DATA),
        ('BlockDeviceRODLimitsData', CLASS_VPD_ECOP_BLOCK_DEVICE_ROD_LIMITS),
        # bit field types other than int
        ('IdlePower', _CLASS_FUNCTION_SUPPORT_INFO.IdlePower)
    ]

    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        _TEMP__CLASS_FUNCTION_SUPPORT_INFO += [
            ('HwFirmwareGetInfoSupport', CLASS_FUNCTION_SUPPORT),
            ('HwFirmwareInfo', PSTORAGE_HW_FIRMWARE_INFO),
        ]

    _CLASS_FUNCTION_SUPPORT_INFO._fields_ = _TEMP__CLASS_FUNCTION_SUPPORT_INFO


    # Restricted - May only append to this structure for backwards
    # compatibility
    _ADDITIONAL_FDO_DATA._fields_ = [
        ('DeviceGuidFlags', ULONG),
        ('DeviceGuid', GUID),
    ]

    # Restricted - May only append to this structure for backwards
    # compatibility

    class _Union_1(ctypes.Union):
        pass

    class _Struct_2(ctypes.Structure):
        pass

    _Struct_2._fields_ = [
        ('Version', ULONG),
        ('DeviceObject', PDEVICE_OBJECT),
    ]
    _Union_1._Struct_2 = _Struct_2

    _Union_1._anonymous_ = (
        '_Struct_2',
    )

    _Union_1._fields_ = [
        ('_Struct_2', _Union_1._Struct_2),
        ('CommonExtension', COMMON_DEVICE_EXTENSION),
    ]


    _FUNCTIONAL_DEVICE_EXTENSION._Union_1 = _Union_1
    _FUNCTIONAL_DEVICE_EXTENSION._anonymous_ = (
        '_Union_1',
    )

    _TEMP__FUNCTIONAL_DEVICE_EXTENSION = [
        ('_Union_1', _FUNCTIONAL_DEVICE_EXTENSION._Union_1),
        # Pointer to the physical device object we attached to - use this
        # for Pnp calls which need a PDO
        ('LowerPdo', PDEVICE_OBJECT),
        # Device capabilities
        ('DeviceDescriptor', PSTORAGE_DEVICE_DESCRIPTOR),
        # SCSI port driver capabilities
        ('AdapterDescriptor', PSTORAGE_ADAPTER_DESCRIPTOR),
        # Current Power state of the device
        ('DevicePowerState', DEVICE_POWER_STATE),
        # DM Driver for IDE drives hack (ie. OnTrack)
        # Bytes to skew all requests
        ('DMByteSkew', ULONG),
        # DM Driver for IDE drives hack (ie. OnTrack)
        # Sectors to skew all requests.
        ('DMSkew', ULONG),
        # DM Driver for IDE drives hack (ie. OnTrack)
        # Flag to indicate whether DM driver has been located on an IDE drive.
        ('DMActive', BOOLEAN),
    ]

    if NTDDI_VERSION >= NTDDI_WIN8:
        _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
            # Buffer length of SenseData
            ('SenseDataLength', UCHAR),
        ]

    else:
        _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
            ('Reserved', UCHAR),
        ]
    # END IF

    _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
        # For future expandability
        ('Reserved0', UCHAR * 2),
        # Buffer for drive parameters returned in IO device control.
        ('DiskGeometry', DISK_GEOMETRY),
        # Request Sense Buffer
        ('SenseData', PSENSE_DATA),
        # Request timeout in seconds
        ('TimeOutValue', ULONG),
        # System device number
        ('DeviceNumber', ULONG),
        # Add default Srb Flags.
        ('SrbFlags', ULONG),
        # Total number of SCSI protocol errors on the device.
        ('ErrorCount', ULONG),
        # Lock count for removable media.
        ('LockCount', LONG),
        ('ProtectedLockCount', LONG),
        ('InternalLockCount', LONG),
        ('EjectSynchronizationEvent', KEVENT),
        # Values for the flags are below.
        ('DeviceFlags', USHORT),
        # Log2 of sector size
        ('SectorShift', UCHAR),
        # Flags to optimize CDB handling.
    ]

    if NTDDI_VERSION >= NTDDI_VISTA:
        _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
            ('CdbForceUnitAccess', UCHAR),
        ]
    else:
        _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
            ('ReservedByte', UCHAR),
        ]
    # END IF

    _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
        # Indicates that the necessary data structures for media change
        # detection have been initialized.
        ('MediaChangeDetectionInfo', PMEDIA_CHANGE_DETECTION_INFO),
        ('Unused1', PKEVENT),
        ('Unused2', HANDLE),
        # File system context. Used for kernel-mode requests to disable autorun.
        ('KernelModeMcnContext', FILE_OBJECT_EXTENSION),
        # Count of media changes.  This field is only valid for the root partition
        # (ie. if PhysicalDevice == NULL).
        ('MediaChangeCount', ULONG),
        # Storage for a handle to the directory the PDO's are placed in
        ('DeviceDirectory', HANDLE),
        # Storage for a release queue request.
        ('ReleaseQueueSpinLock', KSPIN_LOCK),
        ('ReleaseQueueIrp', PIRP),
        ('ReleaseQueueSrb', SCSI_REQUEST_BLOCK),
        ('ReleaseQueueNeeded', BOOLEAN),
        ('ReleaseQueueInProgress', BOOLEAN),
        ('ReleaseQueueIrpFromPool', BOOLEAN),
        # Failure detection storage
        ('FailurePredicted', BOOLEAN),
        ('FailureReason', ULONG),
        ('FailurePredictionInfo', PFAILURE_PREDICTION_INFO),
        ('PowerDownInProgress', BOOLEAN),
        # Interlock for ensuring we don't recurse during enumeration.
        ('EnumerationInterlock', ULONG),
        # Synchronization object for manipulating the child list.
        ('ChildLock', KEVENT),
        # The thread which currently owns the ChildLock.  This is used to
        # avoid recursive acquisition.
        ('ChildLockOwner', PKTHREAD),
        # The number of times this event has been acquired.
        ('ChildLockAcquisitionCount', ULONG),
        # Flags for special behaviour required by
        # different hardware, such as never spinning down
        # or disabling advanced features such as write cache
        ('ScanForSpecialFlags', ULONG),
        # For delayed retry of power requests at DPC level
        ('PowerRetryDpc', KDPC),
        ('PowerRetryTimer', KTIMER),
        # Context structure for power operations.  Since we can only have
        # one D irp at any time in the stack we don't need to worry about
        # allocating multiple of these structures.
        ('PowerContext', CLASS_POWER_CONTEXT),
    ]

    if NTDDI_VERSION <= NTDDI_WIN2K:

        if SPVER(NTDDI_VERSION) < 2:
            _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
                ('Reserved1', ULONG_PTR),
                ('Reserved2', ULONG_PTR),
                ('Reserved3', ULONG_PTR),
                ('Reserved4', ULONG_PTR),
            ]

        else:
            _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
                # Indicates the number of successfully completed
                # requests, if error throttling has been applied.
                ('CompletionSuccessCount', ULONG),
                # When too many errors occur and features are turned off
                # the old SrbFlags are saved here, so that if the condition
                # is fixed, we can restore them to their proper state.
                ('SavedSrbFlags', ULONG),
                # Once recovery has been initiated, cache the old error count value.
                # If new errors occur, go back to the feature set as was earlier used.
                ('SavedErrorCount', ULONG),
                # For future expandability
                # leave these at the end of the structure.
                ('Reserved1', ULONG_PTR),
            ]
        # END IF

    else:
        _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
            # Hold new private data that only classpnp should modify
            # in this structure.
            ('PrivateFdoData', PCLASS_PRIVATE_FDO_DATA),
        ]

        if NTDDI_VERSION >= NTDDI_WIN8:
            _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
                ('FunctionSupportInfo', PCLASS_FUNCTION_SUPPORT_INFO),
                ('MiniportDescriptor', PSTORAGE_MINIPORT_DESCRIPTOR)
            ]

        else:
            _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
                ('Reserved2', ULONG_PTR),
                ('Reserved3', ULONG_PTR),
            ]
        # END IF

        if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
            _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
                ('AdditionalFdoData', PADDITIONAL_FDO_DATA),
            ]
        else:
            _TEMP__FUNCTIONAL_DEVICE_EXTENSION += [
                ('Reserved4', ULONG_PTR),
            ]

        # END IF

    # END IF

    _FUNCTIONAL_DEVICE_EXTENSION._fields_ = _TEMP__FUNCTIONAL_DEVICE_EXTENSION



    # The following CLASS_SPECIAL_ flags are set in ScanForSpecialFlags
    # in the FdoExtension
    # Never Spin Up/Down the drive (may not handle properly)
    CLASS_SPECIAL_DISABLE_SPIN_DOWN = 0x00000001
    CLASS_SPECIAL_DISABLE_SPIN_UP = 0x00000002

    # Don't bother to lock the queue when powering down
    # (used mostly to send a quick stop to a cdrom to abort audio playback)
    CLASS_SPECIAL_NO_QUEUE_LOCK = 0x00000008

    # Disable write cache due to known bugs
    CLASS_SPECIAL_DISABLE_WRITE_CACHE = 0x00000010

    # Special interpretation of "device not ready / cause not reportable" for
    # devices which don't tell us they need to be spun up manually after they
    # spin themselves down behind our back.
    # The down side of this is that if the drive chooses to report
    # "device not ready / cause not reportable" to mean "no media in device"
    # or any other error which really does require user intervention NT will
    # waste a large amount of time trying to spin up a disk which can't be spun
    # up.
    CLASS_SPECIAL_CAUSE_NOT_REPORTABLE_HACK = 0x00000020
    if NTDDI_VERSION == NTDDI_WIN2KSP3 or OSVER(NTDDI_VERSION) == NTDDI_WINXP:
        # Disabling the write cache is not supported on this device
        CLASS_SPECIAL_DISABLE_WRITE_CACHE_NOT_SUPPORTED = 0x00000040 # Obsolete
    # END IF

    CLASS_SPECIAL_MODIFY_CACHE_UNSUCCESSFUL = 0x00000040
    CLASS_SPECIAL_FUA_NOT_SUPPORTED = 0x00000080
    CLASS_SPECIAL_VALID_MASK = 0x000000FB
    CLASS_SPECIAL_RESERVED = ~CLASS_SPECIAL_VALID_MASK

    # Restricted - May only append to this structure for backwards
    # compatibility
    # Indicates that the device has write caching enabled.
    DEV_WRITE_CACHE = 0x00000001

    # Build SCSI 1 or SCSI 2 CDBs
    DEV_USE_SCSI1 = 0x00000002

    # Indicates whether is is safe to send StartUnit commands
    # to this device. It will only be off for some removeable devices.
    DEV_SAFE_START_UNIT = 0x00000004

    # Indicates whether it is unsafe to send SCSIOP_MECHANISM_STATUS commands
    # to
    # this device. Some devices don't like these 12 byte commands
    DEV_NO_12BYTE_CDB = 0x00000008

    # Indicates that the device is connected to a backup power supply
    # and hence write - through and synch cache requests may be ignored
    DEV_POWER_PROTECTED = 0x00000010

    # Indicates that the device supports 16 byte CDBs
    DEV_USE_16BYTE_CDB = 0x00000020

    # Indicates that IRP_MJ_READ, IRP_MJ_WRITE, and IRP_MJ_FLUSH
    # should be forwarded directly to the underlying device
    DEV_FORWARD_IO = 0x00000040

    if NTDDI_VERSION >= NTDDI_WIN8:
        # Size of extended SRB used for 16 byte SCSI cdbs
        CLASS_SRBEX_SCSI_CDB16_BUFFER_SIZE = (
            ctypes.sizeof(STORAGE_REQUEST_BLOCK) +
             ctypes.sizeof(STOR_ADDR_BTL8) +
              ctypes.sizeof(SRBEX_DATA_SCSI_CDB16)
        )
        # Size of extended SRB with no SRB extended data
        CLASS_SRBEX_NO_SRBEX_DATA_BUFFER_SIZE = (
            ctypes.sizeof(STORAGE_REQUEST_BLOCK) +
            ctypes.sizeof(STOR_ADDR_BTL8)
        )
    # END IF
    # Define context structure for asynchronous completions.

    _TEMP__COMPLETION_CONTEXT = [
        ('DeviceObject', PDEVICE_OBJECT),
    ]

    if NTDDI_VERSION >= NTDDI_WIN8:
        class Srb(ctypes.Union):
            pass

        Srb._fields_ = [
            ('Srb', SCSI_REQUEST_BLOCK),
            ('SrbEx', STORAGE_REQUEST_BLOCK),
            ('SrbExBuffer', UCHAR * CLASS_SRBEX_SCSI_CDB16_BUFFER_SIZE),
        ]

        _COMPLETION_CONTEXT.Srb = Srb

        _TEMP__COMPLETION_CONTEXT += [
            ('Srb', _COMPLETION_CONTEXT.Srb)
        ]
    else:
        _TEMP__COMPLETION_CONTEXT += [
            ('Srb', SCSI_REQUEST_BLOCK)
        ]

    _COMPLETION_CONTEXT._fields_ = _TEMP__COMPLETION_CONTEXT


    classpnp = ctypes.windll.CLASSPNP


    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # _Must_inspect_result_
    # SCSIPORT_API
    # ULONG
    # ClassInitialize(
    # _In_  PVOID            Argument1,
    # _In_  PVOID            Argument2,
    # _In_  PCLASS_INIT_DATA InitializationData
    # );
    ClassInitialize = classpnp.ClassInitialize
    ClassInitialize.restype = ULONG

    # List of the GUIDs supported by ClassInitializeEx() and the structure
    # type used for the data parameter for that GUID.
    # {00E34B11 - 2444 - 4745 - A53D - 620100CD82F7} ==
    # CLASS_QUERY_WMI_REGINFO_EX_LIST
    # {509a8c5f - 71d7 - 48f6 - 821e - 173c49bf2f18} ==
    # CLASS_INTERPRET_SENSE_INFO2
    # {105701b0 - 9e9b - 47cb - 9780 - 81198af7b524} == CLASS_WORKING_SET
    # {0a483941 - bdfd - 4f7b - be95 - cee2a216090c} == ULONG
    GUID_CLASSPNP_QUERY_REGINFOEX = [
        0x00E34B11,
        0x2444,
        0x4745,
        [0xA5, 0x3D, 0x62, 0x01, 0x00, 0xCD, 0x82, 0xF7],
    ]
    GUID_CLASSPNP_SENSEINFO2 = [
        0x509A8C5F,
        0x71D7,
        0x48F6,
        [0x82, 0x1E, 0x17, 0x3C, 0x49, 0xBF, 0x2F, 0x18],
    ]
    GUID_CLASSPNP_WORKING_SET = [
        0x105701B0,
        0x9E9B,
        0x47CB,
        [0x97, 0x80, 0x81, 0x19, 0x8A, 0xF7, 0xB5, 0x24],
    ]
    GUID_CLASSPNP_SRB_SUPPORT = [
        0x0A483941,
        0xBDFD,
        0x4F7B,
        [0xBE, 0x95, 0xCE, 0xE2, 0xA2, 0x16, 0x09, 0x0C],
    ]


    # The structure specifies callbacks that are used instead of the
    # PCLASS_QUERY_WMI_REGINFO callbacks.
    _CLASS_QUERY_WMI_REGINFO_EX_LIST._fields_ = [
        # Should be (ctypes.sizeof(CLASS_QUERY_REGINFO_EX_LIST)
        ('Size', ULONG),
        ('ClassFdoQueryWmiRegInfoEx', PCLASS_QUERY_WMI_REGINFO_EX),
        ('ClassPdoQueryWmiRegInfoEx', PCLASS_QUERY_WMI_REGINFO_EX),
    ]

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # _Must_inspect_result_
    # SCSIPORT_API
    # ULONG
    # ClassInitializeEx(
    # _In_  PDRIVER_OBJECT   DriverObject,
    # _In_  LPGUID           Guid,
    # _In_  PVOID            Data
    # );
    ClassInitializeEx = classpnp.ClassInitializeEx
    ClassInitializeEx.restype = ULONG

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # _Must_inspect_result_
    # _Post_satisfies_(return <= 0)
    # SCSIPORT_API
    # NTSTATUS
    # ClassCreateDeviceObject(
    # _In_ PDRIVER_OBJECT     DriverObject,
    # _In_z_ PCCHAR           ObjectNameBuffer,
    # _In_ PDEVICE_OBJECT     LowerDeviceObject,
    # _In_ BOOLEAN            IsFdo,
    # _Outptr_result_nullonfailure_
    # _At_(*DeviceObject, __drv_allocatesMem(Mem) __drv_aliasesMem)
    # PDEVICE_OBJECT          *DeviceObject
    # );
    ClassCreateDeviceObject = classpnp.ClassCreateDeviceObject
    ClassCreateDeviceObject.restype = NTSTATUS

    # _Must_inspect_result_
    # SCSIPORT_API
    # NTSTATUS
    # ClassReadDriveCapacity(
    # _In_ PDEVICE_OBJECT DeviceObject
    # );
    ClassReadDriveCapacity = classpnp.ClassReadDriveCapacity
    ClassReadDriveCapacity.restype = NTSTATUS

    # SCSIPORT_API
    # VOID
    # ClassReleaseQueue(
    # _In_ PDEVICE_OBJECT DeviceObject
    # );
    ClassReleaseQueue = classpnp.ClassReleaseQueue
    ClassReleaseQueue.restype = VOID

    # SCSIPORT_API
    # VOID
    # ClassSplitRequest(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp,
    # _In_ ULONG MaximumBytes
    # );
    ClassSplitRequest = classpnp.ClassSplitRequest
    ClassSplitRequest.restype = VOID

    # SCSIPORT_API
    # NTSTATUS
    # ClassDeviceControl(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _Inout_ PIRP Irp
    # );
    ClassDeviceControl = classpnp.ClassDeviceControl
    ClassDeviceControl.restype = NTSTATUS

    # SCSIPORT_API
    # IO_COMPLETION_ROUTINE ClassIoComplete;
    ClassIoComplete = classpnp.ClassIoComplete
    ClassIoComplete.restype = IO_COMPLETION_ROUTINE

    # SCSIPORT_API
    # IO_COMPLETION_ROUTINE ClassIoCompleteAssociated;
    ClassIoCompleteAssociated = classpnp.ClassIoCompleteAssociated
    ClassIoCompleteAssociated.restype = IO_COMPLETION_ROUTINE

    # SCSIPORT_API
    # BOOLEAN
    # ClassInterpretSenseInfo(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PSCSI_REQUEST_BLOCK Srb,
    # _In_ UCHAR MajorFunctionCode,
    # _In_ ULONG IoDeviceCode,
    # _In_ ULONG RetryCount,
    # _Out_ NTSTATUS *Status,
    # _Out_opt_ _Deref_out_range_(0,100) ULONG *RetryInterval
    # );
    ClassInterpretSenseInfo = classpnp.ClassInterpretSenseInfo
    ClassInterpretSenseInfo.restype = BOOLEAN

    # VOID
    # ClassSendDeviceIoControlSynchronous(
    # _In_ ULONG IoControlCode,
    # _In_ PDEVICE_OBJECT TargetDeviceObject,
    # _Inout_updates_opt_(_Inexpressible_(max(InputBufferLength, OutputBufferLength))) PVOID Buffer,
    # _In_ ULONG InputBufferLength,
    # _In_ ULONG OutputBufferLength,
    # _In_ BOOLEAN InternalDeviceIoControl,
    # _Out_ PIO_STATUS_BLOCK IoStatus
    # );
    ClassSendDeviceIoControlSynchronous = (
        classpnp.ClassSendDeviceIoControlSynchronous
    )
    ClassSendDeviceIoControlSynchronous.restype = VOID

    # SCSIPORT_API
    # NTSTATUS
    # ClassSendIrpSynchronous(
    # _In_ PDEVICE_OBJECT TargetDeviceObject,
    # _In_ PIRP Irp);
    ClassSendIrpSynchronous = classpnp.ClassSendIrpSynchronous
    ClassSendIrpSynchronous.restype = NTSTATUS

    # SCSIPORT_API
    # NTSTATUS ClassForwardIrpSynchronous(
    # _In_ PCOMMON_DEVICE_EXTENSION CommonExtension,
    # _In_ PIRP Irp
    # );
    ClassForwardIrpSynchronous = classpnp.ClassForwardIrpSynchronous
    ClassForwardIrpSynchronous.restype = NTSTATUS

    # SCSIPORT_API
    # NTSTATUS
    # ClassSendSrbSynchronous(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _Inout_ PSCSI_REQUEST_BLOCK Srb,
    # _In_reads_bytes_opt_(BufferLength) PVOID BufferAddress,
    # _In_ ULONG BufferLength,
    # _In_ BOOLEAN WriteToDevice
    # );
    ClassSendSrbSynchronous = classpnp.ClassSendSrbSynchronous
    ClassSendSrbSynchronous.restype = NTSTATUS

    # _Success_(return == STATUS_PENDING)
    # SCSIPORT_API
    # NTSTATUS
    # ClassSendSrbAsynchronous(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _Inout_ _On_failure_(__drv_freesMem(Mem)) __drv_aliasesMem PSCSI_REQUEST_BLOCK _Srb,
    # _In_ PIRP Irp,
    # _In_reads_bytes_opt_(BufferLength) __drv_aliasesMem PVOID BufferAddress,
    # _In_ ULONG BufferLength,
    # _In_ BOOLEAN WriteToDevice
    # );
    ClassSendSrbAsynchronous = classpnp.ClassSendSrbAsynchronous
    ClassSendSrbAsynchronous.restype = NTSTATUS

    # SCSIPORT_API
    # NTSTATUS
    # ClassBuildRequest(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp
    # );
    ClassBuildRequest = classpnp.ClassBuildRequest
    ClassBuildRequest.restype = NTSTATUS

    # SCSIPORT_API
    # ULONG
    # ClassModeSense(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_reads_bytes_(Length) PCHAR ModeSenseBuffer,
    # _In_ ULONG Length,
    # _In_ UCHAR PageMode
    # );
    ClassModeSense = classpnp.ClassModeSense
    ClassModeSense.restype = ULONG

    # SCSIPORT_API
    # NTSTATUS
    # ClassModeSenseTranslate(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PMODE_PARAMETER_HEADER ModeSenseData,
    # _Inout_ PULONG ModeSenseBufferSize
    # );

    ClassModeSenseTranslate = classpnp.ClassModeSenseTranslate
    ClassModeSenseTranslate.restype = NTSTATUS

    # SCSIPORT_API
    # PVOID
    # ClassFindModePage(
    # _In_reads_bytes_(Length) PCHAR ModeSenseBuffer,
    # _In_ ULONG Length,
    # _In_ UCHAR PageMode,
    # _In_ BOOLEAN Use6Byte
    # );
    ClassFindModePage = classpnp.ClassFindModePage
    ClassFindModePage.restype = PVOID

    if NTDDI_VERSION >= NTDDI_WINBLUE:
        # SCSIPORT_API
        # ULONG
        # ClassModeSenseEx(
        # _In_ PDEVICE_OBJECT Fdo,
        # _In_reads_bytes_(Length) PCHAR ModeSenseBuffer,
        # _In_ ULONG Length,
        # _In_ UCHAR PageMode,
        # _In_ UCHAR PageControl
        # );
        ClassModeSenseEx = classpnp.ClassModeSenseEx
        ClassModeSenseEx.restype = ULONG

        # SCSIPORT_API
        # NTSTATUS
        # ClassModeSelect(
        # _In_ PDEVICE_OBJECT Fdo,
        # _In_reads_bytes_(Length) PCHAR ModeSelectBuffer,
        # _In_ ULONG Length,
        # _In_ BOOLEAN SavePages
        # );
        ClassModeSelect = classpnp.ClassModeSelect
        ClassModeSelect.restype = NTSTATUS

    # END IF   (NTDDI_VERSION >= NTDDI_WINBLUE)

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # NTSTATUS
    # ClassClaimDevice(
    # _In_ PDEVICE_OBJECT LowerDeviceObject,
    # _In_ BOOLEAN Release
    # );
    ClassClaimDevice = classpnp.ClassClaimDevice
    ClassClaimDevice.restype = NTSTATUS

    # SCSIPORT_API
    # _Dispatch_type_(IRP_MJ_SCSI)
    # DRIVER_DISPATCH ClassInternalIoControl;
    ClassInternalIoControl = classpnp.ClassInternalIoControl
    ClassInternalIoControl.restype = DRIVER_DISPATCH

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # VOID
    # ClassInitializeSrbLookasideList(
    # _Inout_ PCOMMON_DEVICE_EXTENSION CommonExtension,
    # _In_ ULONG NumberElements
    # );
    ClassInitializeSrbLookasideList = classpnp.ClassInitializeSrbLookasideList
    ClassInitializeSrbLookasideList.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # VOID
    # ClassDeleteSrbLookasideList(
    # _Inout_ PCOMMON_DEVICE_EXTENSION CommonExtension
    # );
    ClassDeleteSrbLookasideList = classpnp.ClassDeleteSrbLookasideList
    ClassDeleteSrbLookasideList.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # ULONG
    # ClassQueryTimeOutRegistryValue(
    # _In_ PDEVICE_OBJECT DeviceObject
    # );
    ClassQueryTimeOutRegistryValue = classpnp.ClassQueryTimeOutRegistryValue
    ClassQueryTimeOutRegistryValue.restype = ULONG

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # NTSTATUS
    # ClassGetDescriptor(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PSTORAGE_PROPERTY_ID PropertyId,
    # _Outptr_ PVOID *Descriptor
    # );
    ClassGetDescriptor = classpnp.ClassGetDescriptor
    ClassGetDescriptor.restype = NTSTATUS

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # VOID
    # ClassInvalidateBusRelations(
    # _In_ PDEVICE_OBJECT Fdo
    # );
    ClassInvalidateBusRelations = classpnp.ClassInvalidateBusRelations
    ClassInvalidateBusRelations.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # VOID
    # ClassMarkChildrenMissing(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION Fdo
    # );
    ClassMarkChildrenMissing = classpnp.ClassMarkChildrenMissing
    ClassMarkChildrenMissing.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # BOOLEAN
    # ClassMarkChildMissing(
    # _In_ PPHYSICAL_DEVICE_EXTENSION PdoExtension,
    # _In_ BOOLEAN AcquireChildLock
    # );
    ClassMarkChildMissing = classpnp.ClassMarkChildMissing
    ClassMarkChildMissing.restype = BOOLEAN

    # SCSIPORT_API
    # VOID
    # ClassDebugPrint(
    # _In_ CLASS_DEBUG_LEVEL DebugPrintLevel,
    # _In_z_ PCCHAR DebugMessage,
    # ...
    # );
    ClassDebugPrint = classpnp.ClassDebugPrint
    ClassDebugPrint.restype = VOID

    # __drv_aliasesMem
    # _IRQL_requires_max_(DISPATCH_LEVEL)
    # SCSIPORT_API
    # PCLASS_DRIVER_EXTENSION
    # ClassGetDriverExtension(
    # _In_ PDRIVER_OBJECT DriverObject
    # );
    ClassGetDriverExtension = classpnp.ClassGetDriverExtension
    ClassGetDriverExtension.restype = PCLASS_DRIVER_EXTENSION

    # SCSIPORT_API
    # VOID
    # ClassCompleteRequest(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp,
    # _In_ CCHAR PriorityBoost
    # );
    ClassCompleteRequest = classpnp.ClassCompleteRequest
    ClassCompleteRequest.restype = VOID

    # SCSIPORT_API
    # VOID
    # ClassReleaseRemoveLock(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_opt_ PVOID Tag
    # );
    ClassReleaseRemoveLock = classpnp.ClassReleaseRemoveLock
    ClassReleaseRemoveLock.restype = VOID

    # SCSIPORT_API
    # ULONG
    # ClassAcquireRemoveLockEx(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PVOID Tag,
    # _In_ PCSTR File,
    # _In_ ULONG Line
    # );
    ClassAcquireRemoveLockEx = classpnp.ClassAcquireRemoveLockEx
    ClassAcquireRemoveLockEx.restype = ULONG

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # VOID
    # ClassUpdateInformationInRegistry(
    # _In_ PDEVICE_OBJECT   Fdo,
    # _In_ PCHAR            DeviceName,
    # _In_ ULONG            DeviceNumber,
    # _In_reads_bytes_opt_(InquiryDataLength) PINQUIRYDATA InquiryData,
    # _In_ ULONG            InquiryDataLength
    # );
    ClassUpdateInformationInRegistry = (
        classpnp.ClassUpdateInformationInRegistry
    )
    ClassUpdateInformationInRegistry.restype = VOID

    # SCSIPORT_API
    # NTSTATUS
    # ClassWmiCompleteRequest(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _Inout_ PIRP Irp,
    # _In_ NTSTATUS Status,
    # _In_ ULONG BufferUsed,
    # _In_ CCHAR PriorityBoost
    # );
    ClassWmiCompleteRequest = classpnp.ClassWmiCompleteRequest
    ClassWmiCompleteRequest.restype = NTSTATUS

    # _IRQL_requires_max_(DISPATCH_LEVEL)
    # SCSIPORT_API
    # NTSTATUS
    # ClassWmiFireEvent(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ LPGUID Guid,
    # _In_ ULONG InstanceIndex,
    # _In_ ULONG EventDataSize,
    # _In_reads_bytes_(EventDataSize) PVOID EventData
    # );
    ClassWmiFireEvent = classpnp.ClassWmiFireEvent
    ClassWmiFireEvent.restype = NTSTATUS

    # SCSIPORT_API
    # VOID
    # ClassResetMediaChangeTimer(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension
    # );
    ClassResetMediaChangeTimer = classpnp.ClassResetMediaChangeTimer
    ClassResetMediaChangeTimer.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # VOID
    # ClassInitializeMediaChangeDetection(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension,
    # _In_ PUCHAR EventPrefix
    # );
    ClassInitializeMediaChangeDetection = (
        classpnp.ClassInitializeMediaChangeDetection
    )
    ClassInitializeMediaChangeDetection.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # NTSTATUS
    # ClassInitializeTestUnitPolling(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension,
    # _In_ BOOLEAN AllowDriveToSleep
    # );
    ClassInitializeTestUnitPolling = classpnp.ClassInitializeTestUnitPolling
    ClassInitializeTestUnitPolling.restype = NTSTATUS

    # SCSIPORT_API
    # PVPB
    # ClassGetVpb(
    # _In_ PDEVICE_OBJECT DeviceObject
    # );
    ClassGetVpb = classpnp.ClassGetVpb
    ClassGetVpb.restype = PVPB


    # SCSIPORT_API
    # __control_entrypoint(DeviceDriver)
    # NTSTATUS
    # ClassSpinDownPowerHandler(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp
    # );
    ClassSpinDownPowerHandler = classpnp.ClassSpinDownPowerHandler
    ClassSpinDownPowerHandler.restype = NTSTATUS

    # NTSTATUS
    # ClassStopUnitPowerHandler(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ PIRP Irp
    # );
    ClassStopUnitPowerHandler = classpnp.ClassStopUnitPowerHandler
    ClassStopUnitPowerHandler.restype = NTSTATUS

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # NTSTATUS
    # ClassSetFailurePredictionPoll(
    # _Inout_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension,
    # _In_ FAILURE_PREDICTION_METHOD FailurePredictionMethod,
    # _In_ ULONG PollingPeriod
    # );
    ClassSetFailurePredictionPoll = classpnp.ClassSetFailurePredictionPoll
    ClassSetFailurePredictionPoll.restype = NTSTATUS

    # _IRQL_requires_max_(DISPATCH_LEVEL)
    # VOID
    # ClassNotifyFailurePredicted(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension,
    # _In_reads_bytes_(BufferSize) PUCHAR Buffer,
    # _In_ ULONG BufferSize,
    # _In_ BOOLEAN LogError,
    # _In_ ULONG UniqueErrorValue,
    # _In_ UCHAR PathId,
    # _In_ UCHAR TargetId,
    # _In_ UCHAR Lun
    # );
    ClassNotifyFailurePredicted = classpnp.ClassNotifyFailurePredicted
    ClassNotifyFailurePredicted.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # VOID
    # ClassAcquireChildLock(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension
    # );
    ClassAcquireChildLock = classpnp.ClassAcquireChildLock
    ClassAcquireChildLock.restype = VOID

    # SCSIPORT_API
    # VOID
    # ClassReleaseChildLock(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension
    # );
    ClassReleaseChildLock = classpnp.ClassReleaseChildLock
    ClassReleaseChildLock.restype = VOID

    # IO_COMPLETION_ROUTINE ClassSignalCompletion;
    ClassSignalCompletion = classpnp.ClassSignalCompletion
    ClassSignalCompletion.restype = IO_COMPLETION_ROUTINE

    # VOID
    # ClassSendStartUnit(
    # _In_ PDEVICE_OBJECT DeviceObject
    # );
    ClassSendStartUnit = classpnp.ClassSendStartUnit
    ClassSendStartUnit.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # NTSTATUS
    # ClassRemoveDevice(
    # _In_ PDEVICE_OBJECT DeviceObject,
    # _In_ UCHAR RemoveType
    # );
    ClassRemoveDevice = classpnp.ClassRemoveDevice
    ClassRemoveDevice.restype = NTSTATUS

    # SCSIPORT_API
    # IO_COMPLETION_ROUTINE ClassAsynchronousCompletion;
    ClassAsynchronousCompletion = classpnp.ClassAsynchronousCompletion
    ClassAsynchronousCompletion.restype = IO_COMPLETION_ROUTINE

    # SCSIPORT_API
    # VOID
    # ClassCheckMediaState(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension
    # );
    ClassCheckMediaState = classpnp.ClassCheckMediaState
    ClassCheckMediaState.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # VOID
    # ClassSetMediaChangeState(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension,
    # _In_ MEDIA_CHANGE_DETECTION_STATE State,
    # _In_ BOOLEAN Wait
    # );
    ClassSetMediaChangeState = classpnp.ClassSetMediaChangeState
    ClassSetMediaChangeState.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # VOID
    # ClassEnableMediaChangeDetection(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension
    # );
    ClassEnableMediaChangeDetection = classpnp.ClassEnableMediaChangeDetection
    ClassEnableMediaChangeDetection.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # VOID
    # ClassDisableMediaChangeDetection(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension
    # );
    ClassDisableMediaChangeDetection = (
        classpnp.ClassDisableMediaChangeDetection
    )
    ClassDisableMediaChangeDetection.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # SCSIPORT_API
    # VOID
    # ClassCleanupMediaChangeDetection(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension
    # );
    ClassCleanupMediaChangeDetection = (
        classpnp.ClassCleanupMediaChangeDetection
    )
    ClassCleanupMediaChangeDetection.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # VOID
    # ClassGetDeviceParameter(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension,
    # _In_opt_ PWSTR SubkeyName,
    # _In_ PWSTR ParameterName,
    # _Inout_ PULONG ParameterValue
    # );
    ClassGetDeviceParameter = classpnp.ClassGetDeviceParameter
    ClassGetDeviceParameter.restype = VOID

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # NTSTATUS
    # ClassSetDeviceParameter(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension,
    # _In_opt_ PWSTR SubkeyName,
    # _In_ PWSTR ParameterName,
    # _In_ ULONG ParameterValue
    # );
    ClassSetDeviceParameter = classpnp.ClassSetDeviceParameter
    ClassSetDeviceParameter.restype = NTSTATUS

    if NTDDI_VERSION >= NTDDI_VISTA:
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # PFILE_OBJECT_EXTENSION
        # ClassGetFsContext(
        # _In_ PCOMMON_DEVICE_EXTENSION CommonExtension,
        # _In_ PFILE_OBJECT FileObject
        # );
        ClassGetFsContext = classpnp.ClassGetFsContext
        ClassGetFsContext.restype = PFILE_OBJECT_EXTENSION

        # _IRQL_requires_max_(DISPATCH_LEVEL)
        # VOID
        # ClassSendNotification(
        # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension,
        # _In_ GUID * Guid,
        # _In_ ULONG  ExtraDataSize,
        # _In_reads_bytes_opt_(ExtraDataSize) PVOID  ExtraData
        # );
        ClassSendNotification = classpnp.ClassSendNotification
        ClassSendNotification.restype = VOID

    # END IF

    # PCLASS_SCAN_FOR_SPECIAL_HANDLER() Routine Description: This routine is a
    # callback into the driver to set device - specific flags based upon matches
    # made to the device's inquiry data. Drivers register for this callback using
    # ClassRegisterScanForSpecial().
    # Irql: This routine will be called at KIRQL == PASSIVE_LEVEL
    # Arguments: DeviceObject is the device object the error occurred on.
    # Srb is the Srb that was being processed when the error occurred.
    # Status may be overwritten by the routine if it decides that the error was
    # benign, or otherwise wishes to change the returned status code for this
    # command Retry may be overwritten to specify that this command should or
    # should not be retried (if the callee supports retrying commands)
    # Return Value: status - -
    #
    # VOID
    # (*PCLASS_SCAN_FOR_SPECIAL_HANDLER) (
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension,
    # _In_ ULONG_PTR Data
    # );
    PCLASS_SCAN_FOR_SPECIAL_HANDLER = CALLBACK(
        VOID,
        PFUNCTIONAL_DEVICE_EXTENSION,
        ULONG_PTR
    )

    # _IRQL_requires_max_(PASSIVE_LEVEL)
    # VOID
    # ClassScanForSpecial(
    # _In_ PFUNCTIONAL_DEVICE_EXTENSION FdoExtension,
    # _In_ CLASSPNP_SCAN_FOR_SPECIAL_INFO DeviceList[],
    # _In_ PCLASS_SCAN_FOR_SPECIAL_HANDLER Function
    # );
    ClassScanForSpecial = classpnp.ClassScanForSpecial
    ClassScanForSpecial.restype = VOID

# END IF  _CLASS_
