import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *


class _HIDD_CONFIGURATION(ctypes.Structure):
    pass


HIDD_CONFIGURATION = _HIDD_CONFIGURATION
PHIDD_CONFIGURATION = POINTER(_HIDD_CONFIGURATION)


class _HIDD_ATTRIBUTES(ctypes.Structure):
    pass


HIDD_ATTRIBUTES = _HIDD_ATTRIBUTES
PHIDD_ATTRIBUTES = POINTER(_HIDD_ATTRIBUTES)


# + + Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# HIDSDI.H Abstract: This module contains the PUBLIC definitions for the code
# that implements the HID dll. Environment: Kernel & user mode - -

_HIDSDI_H = None
if not defined(_HIDSDI_H):
    _HIDSDI_H = 1
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

        if defined(__cplusplus):
            pass
        # END IF

        NTSTATUS = LONG

        from pyWinAPI.shared.hidusage_h import * # NOQA
        from pyWinAPI.shared.hidpi_h import * # NOQA

        _HIDD_CONFIGURATION._fields_ = [
            ('cookie', PVOID),
            ('size', ULONG),
            ('RingBufferSize', ULONG),
        ]
        _HIDD_ATTRIBUTES._fields_ = [
            ('Size', ULONG), # = ctypes.sizeof (struct _HIDD_ATTRIBUTES)
            ('VendorID', USHORT), # Vendor ids of this hid device
            ('ProductID', USHORT),
            ('VersionNumber', USHORT),
        ]
        hid = ctypes.windll.hid

        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetAttributes(
        # _In_  HANDLE              HidDeviceObject,
        # _Out_ PHIDD_ATTRIBUTES    Attributes
        # );
        HidD_GetAttributes = hid.HidD_GetAttributes
        HidD_GetAttributes.restype = BOOLEAN

        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetAttributes(
        # _In_  HANDLE              HidDeviceObject,
        # _Out_ PHIDD_ATTRIBUTES    Attributes
        # );
        HidD_GetAttributes = hid.HidD_GetAttributes
        HidD_GetAttributes.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_GetAttributes(
        # _In_  HANDLE              HidDeviceObject,
        # _Out_ PHIDD_ATTRIBUTES    Attributes
        # );
        HidD_GetAttributes = hid.HidD_GetAttributes
        HidD_GetAttributes.restype = BOOLEAN

        # + + Routine Description: Fill in the given HIDD_ATTRIBUTES structure
        # with the attributes of the given hid device. - -        # VOID __stdcall
        # HidD_GetHidGuid(
        # _Out_  LPGUID   HidGuid
        # );
        HidD_GetHidGuid = hid.HidD_GetHidGuid
        HidD_GetHidGuid.restype = VOID
        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetPreparsedData(
        # _In_   HANDLE                  HidDeviceObject,
        # _Out_ _When_(return != 0, __drv_allocatesMem(Mem))  PHIDP_PREPARSED_DATA  * PreparsedData
        # );
        HidD_GetPreparsedData = hid.HidD_GetPreparsedData
        HidD_GetPreparsedData.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetPreparsedData(
        # _In_   HANDLE                  HidDeviceObject,
        # _Out_ _When_(return != 0, __drv_allocatesMem(Mem))  PHIDP_PREPARSED_DATA  * PreparsedData
        # );
        HidD_GetPreparsedData = hid.HidD_GetPreparsedData
        HidD_GetPreparsedData.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_GetPreparsedData(
        # _In_   HANDLE                  HidDeviceObject,
        # _Out_ _When_(return != 0, __drv_allocatesMem(Mem))  PHIDP_PREPARSED_DATA  * PreparsedData
        # );
        HidD_GetPreparsedData = hid.HidD_GetPreparsedData
        HidD_GetPreparsedData.restype = BOOLEAN

        # + + Routine Description: Given a handle to a valid Hid Class Device
        # Object, retrieve the preparsed data for the device. This routine
        # will allocate the appropriately sized buffer to hold this preparsed
        # data. It is up to client to call HidP_FreePreparsedData to free the
        # memory allocated to this structure when it is no LONGer needed.
        # Arguments: HidDeviceObject A handle to a Hid Device that the client
        # obtains using a call to CreateFile on a valid Hid device string
        # name. The string name can be obtained using standard PnP calls.
        # PreparsedData An opaque data structure used by other functions in
        # this library to retrieve information about a given device. Return
        # Value: TRUE if successful. FALSE otherwise - - Use GetLastError() to
        # get extended error information - -        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_FreePreparsedData(
        # _In_ __drv_freesMem(Mem) PHIDP_PREPARSED_DATA PreparsedData
        # );
        HidD_FreePreparsedData = hid.HidD_FreePreparsedData
        HidD_FreePreparsedData.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_FreePreparsedData(
        # _In_ __drv_freesMem(Mem) PHIDP_PREPARSED_DATA PreparsedData
        # );
        HidD_FreePreparsedData = hid.HidD_FreePreparsedData
        HidD_FreePreparsedData.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_FlushQueue(
        # _In_    HANDLE                HidDeviceObject
        # );
        HidD_FlushQueue = hid.HidD_FlushQueue
        HidD_FlushQueue.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_FlushQueue(
        # _In_    HANDLE                HidDeviceObject
        # );
        HidD_FlushQueue = hid.HidD_FlushQueue
        HidD_FlushQueue.restype = BOOLEAN

        # + + Routine Description: Flush the input queue for the given HID
        # device. Arguments: HidDeviceObject A handle to a Hid Device that the
        # client obtains using a call to CreateFile on a valid Hid device
        # string name. The string name can be obtained using standard PnP
        # calls. Return Value: TRUE if successful FALSE otherwise - - Use
        # GetLastError() to get extended error information - -        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetConfiguration(
        # _In_   HANDLE               HidDeviceObject,
        # _Out_writes_bytes_(ConfigurationLength) PHIDD_CONFIGURATION Configuration,
        # _In_   ULONG                ConfigurationLength
        # );
        HidD_GetConfiguration = hid.HidD_GetConfiguration
        HidD_GetConfiguration.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetConfiguration(
        # _In_   HANDLE               HidDeviceObject,
        # _Out_writes_bytes_(ConfigurationLength) PHIDD_CONFIGURATION Configuration,
        # _In_   ULONG                ConfigurationLength
        # );
        HidD_GetConfiguration = hid.HidD_GetConfiguration
        HidD_GetConfiguration.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_GetConfiguration(
        # _In_   HANDLE               HidDeviceObject,
        # _Out_writes_bytes_(ConfigurationLength) PHIDD_CONFIGURATION Configuration,
        # _In_   ULONG                ConfigurationLength
        # );
        HidD_GetConfiguration = hid.HidD_GetConfiguration
        HidD_GetConfiguration.restype = BOOLEAN

        # + + Routine Description: Get the configuration information for this
        # Hid device Arguments: HidDeviceObject A handle to a Hid Device
        # Object. Configuration A configuration structure.
        # HidD_GetConfiguration MUST be called before the configuration can be
        # modified and set using HidD_SetConfiguration ConfigurationLength
        # That is ``ctypes.sizeof (HIDD_CONFIGURATION)''. Using this
        # parameter, we can later increase the length of the configuration
        # array and not break older apps. Return Value: TRUE if successful
        # FALSE otherwise - - Use GetLastError() to get extended error
        # information - -        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_SetConfiguration(
        # _In_   HANDLE               HidDeviceObject,
        # _In_reads_bytes_(ConfigurationLength) PHIDD_CONFIGURATION Configuration,
        # _In_   ULONG                ConfigurationLength
        # );
        HidD_SetConfiguration = hid.HidD_SetConfiguration
        HidD_SetConfiguration.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_SetConfiguration(
        # _In_   HANDLE               HidDeviceObject,
        # _In_reads_bytes_(ConfigurationLength) PHIDD_CONFIGURATION Configuration,
        # _In_   ULONG                ConfigurationLength
        # );
        HidD_SetConfiguration = hid.HidD_SetConfiguration
        HidD_SetConfiguration.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_SetConfiguration(
        # _In_   HANDLE               HidDeviceObject,
        # _In_reads_bytes_(ConfigurationLength) PHIDD_CONFIGURATION Configuration,
        # _In_   ULONG                ConfigurationLength
        # );
        HidD_SetConfiguration = hid.HidD_SetConfiguration
        HidD_SetConfiguration.restype = BOOLEAN

        # + + Routine Description: Set the configuration information for this
        # Hid device... NOTE: HidD_GetConfiguration must be called to retrieve
        # the current configuration information before this information can be
        # modified and set. Arguments: HidDeviceObject A handle to a Hid
        # Device Object. Configuration A configuration structure.
        # HidD_GetConfiguration MUST be called before the configuration can be
        # modified and set using HidD_SetConfiguration ConfigurationLength
        # That is ``ctypes.sizeof (HIDD_CONFIGURATION)''. Using this
        # parameter, we can later increase the length of the configuration
        # array and not break older apps. Return Value: TRUE if successful
        # FALSE otherwise - - Use GetLastError() to get extended error
        # information - -        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetFeature(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(ReportBufferLength) PVOID ReportBuffer,
        # _In_    ULONG    ReportBufferLength
        # );
        HidD_GetFeature = hid.HidD_GetFeature
        HidD_GetFeature.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetFeature(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(ReportBufferLength) PVOID ReportBuffer,
        # _In_    ULONG    ReportBufferLength
        # );
        HidD_GetFeature = hid.HidD_GetFeature
        HidD_GetFeature.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_GetFeature(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(ReportBufferLength) PVOID ReportBuffer,
        # _In_    ULONG    ReportBufferLength
        # );
        HidD_GetFeature = hid.HidD_GetFeature
        HidD_GetFeature.restype = BOOLEAN

        # + + Routine Description: Retrieve a feature report from a HID
        # device. Arguments: HidDeviceObject A handle to a Hid Device Object.
        # ReportBuffer The buffer that the feature report should be placed
        # into. The first byte of the buffer should be set to the report ID of
        # the desired report ReportBufferLength The size (in bytes) of
        # ReportBuffer. This value should be greater than or equal to the
        # FeatureReportByteLength field as specified in the HIDP_CAPS
        # structure for the device Return Value: TRUE if successful FALSE
        # otherwise - - Use GetLastError() to get extended error information -
        # -        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_SetFeature(
        # _In_    HANDLE   HidDeviceObject,
        # _In_reads_bytes_(ReportBufferLength) PVOID ReportBuffer,
        # _In_    ULONG    ReportBufferLength
        # );
        HidD_SetFeature = hid.HidD_SetFeature
        HidD_SetFeature.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_SetFeature(
        # _In_    HANDLE   HidDeviceObject,
        # _In_reads_bytes_(ReportBufferLength) PVOID ReportBuffer,
        # _In_    ULONG    ReportBufferLength
        # );
        HidD_SetFeature = hid.HidD_SetFeature
        HidD_SetFeature.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_SetFeature(
        # _In_    HANDLE   HidDeviceObject,
        # _In_reads_bytes_(ReportBufferLength) PVOID ReportBuffer,
        # _In_    ULONG    ReportBufferLength
        # );
        HidD_SetFeature = hid.HidD_SetFeature
        HidD_SetFeature.restype = BOOLEAN

        # + + Routine Description: Send a feature report to a HID device.
        # Arguments: HidDeviceObject A handle to a Hid Device Object.
        # ReportBuffer The buffer of the feature report to send to the device
        # ReportBufferLength The size (in bytes) of ReportBuffer. This value
        # should be greater than or equal to the FeatureReportByteLength field
        # as specified in the HIDP_CAPS structure for the device Return Value:
        # TRUE if successful FALSE otherwise - - Use GetLastError() to get
        # extended error information - -
        if NTDDI_VERSION >= NTDDI_WINXP:
            # _Must_inspect_result_
            # _Success_(return == TRUE)
            # BOOLEAN __stdcall
            # HidD_GetInputReport(
            # _In_    HANDLE   HidDeviceObject,
            # _Out_writes_bytes_(ReportBufferLength) PVOID ReportBuffer,
            # _In_    ULONG    ReportBufferLength
            # );
            HidD_GetInputReport = hid.HidD_GetInputReport
            HidD_GetInputReport.restype = BOOLEAN
            # _Success_(return == TRUE)
            # BOOLEAN __stdcall
            # HidD_GetInputReport(
            # _In_    HANDLE   HidDeviceObject,
            # _Out_writes_bytes_(ReportBufferLength) PVOID ReportBuffer,
            # _In_    ULONG    ReportBufferLength
            # );
            HidD_GetInputReport = hid.HidD_GetInputReport
            HidD_GetInputReport.restype = BOOLEAN
            # BOOLEAN __stdcall
            # HidD_GetInputReport(
            # _In_    HANDLE   HidDeviceObject,
            # _Out_writes_bytes_(ReportBufferLength) PVOID ReportBuffer,
            # _In_    ULONG    ReportBufferLength
            # );
            HidD_GetInputReport = hid.HidD_GetInputReport
            HidD_GetInputReport.restype = BOOLEAN

            # + + Routine Description: Retrieve an input report from a HID
            # device. Arguments: HidDeviceObject A handle to a Hid Device
            # Object. ReportBuffer The buffer that the input report should be
            # placed into. The first byte of the buffer should be set to the
            # report ID of the desired report ReportBufferLength The size
            # (in bytes) of ReportBuffer. This value should be greater than or
            # equal to the InputReportByteLength field as specified in the
            # HIDP_CAPS structure for the device Return Value: TRUE if
            # successful FALSE otherwise - - Use GetLastError() to get
            # extended error information - -            # _Must_inspect_result_
            # _Success_(return == TRUE)
            # BOOLEAN __stdcall
            # HidD_SetOutputReport(
            # _In_    HANDLE   HidDeviceObject,
            # _In_reads_bytes_(ReportBufferLength) PVOID ReportBuffer,
            # _In_    ULONG    ReportBufferLength
            # );
            HidD_SetOutputReport = hid.HidD_SetOutputReport
            HidD_SetOutputReport.restype = BOOLEAN
            # _Success_(return == TRUE)
            # BOOLEAN __stdcall
            # HidD_SetOutputReport(
            # _In_    HANDLE   HidDeviceObject,
            # _In_reads_bytes_(ReportBufferLength) PVOID ReportBuffer,
            # _In_    ULONG    ReportBufferLength
            # );
            HidD_SetOutputReport = hid.HidD_SetOutputReport
            HidD_SetOutputReport.restype = BOOLEAN
            # BOOLEAN __stdcall
            # HidD_SetOutputReport(
            # _In_    HANDLE   HidDeviceObject,
            # _In_reads_bytes_(ReportBufferLength) PVOID ReportBuffer,
            # _In_    ULONG    ReportBufferLength
            # );
            HidD_SetOutputReport = hid.HidD_SetOutputReport
            HidD_SetOutputReport.restype = BOOLEAN

            # + + Routine Description: Send an output report to a HID device.
            # Arguments: HidDeviceObject A handle to a Hid Device Object.
            # ReportBuffer The buffer of the output report to send to the
            # device ReportBufferLength The size (in bytes) of ReportBuffer.
            # This value should be greater than or equal to the
            # OutputReportByteLength field as specified in the HIDP_CAPS
            # structure for the device Return Value: TRUE if successful FALSE
            # otherwise - - Use GetLastError() to get extended error
            # information - -        # END IF        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetNumInputBuffers(
        # _In_  HANDLE  HidDeviceObject,
        # _Out_ PULONG  NumberBuffers
        # );
        HidD_GetNumInputBuffers = hid.HidD_GetNumInputBuffers
        HidD_GetNumInputBuffers.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetNumInputBuffers(
        # _In_  HANDLE  HidDeviceObject,
        # _Out_ PULONG  NumberBuffers
        # );
        HidD_GetNumInputBuffers = hid.HidD_GetNumInputBuffers
        HidD_GetNumInputBuffers.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_GetNumInputBuffers(
        # _In_  HANDLE  HidDeviceObject,
        # _Out_ PULONG  NumberBuffers
        # );
        HidD_GetNumInputBuffers = hid.HidD_GetNumInputBuffers
        HidD_GetNumInputBuffers.restype = BOOLEAN

        # + + Routine Description: This function returns the number of input
        # buffers used by the specified file handle to the Hid device. Each
        # file object has a number of buffers associated with it to queue
        # reports read from the device but which have not yet been read by the
        # user - mode app with a handle to that device. Arguments:
        # HidDeviceObject A handle to a Hid Device Object. NumberBuffers
        # Number of buffers currently being used for this file handle to the
        # Hid device Return Value: TRUE if successful FALSE otherwise - - Use
        # GetLastError() to get extended error information - -        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_SetNumInputBuffers(
        # _In_ HANDLE HidDeviceObject,
        # _In_ ULONG  NumberBuffers
        # );
        HidD_SetNumInputBuffers = hid.HidD_SetNumInputBuffers
        HidD_SetNumInputBuffers.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_SetNumInputBuffers(
        # _In_ HANDLE HidDeviceObject,
        # _In_ ULONG  NumberBuffers
        # );
        HidD_SetNumInputBuffers = hid.HidD_SetNumInputBuffers
        HidD_SetNumInputBuffers.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_SetNumInputBuffers(
        # _In_ HANDLE HidDeviceObject,
        # _In_ ULONG  NumberBuffers
        # );
        HidD_SetNumInputBuffers = hid.HidD_SetNumInputBuffers
        HidD_SetNumInputBuffers.restype = BOOLEAN

        # + + Routine Description: This function sets the number of input
        # buffers used by the specified file handle to the Hid device. Each
        # file object has a number of buffers associated with it to queue
        # reports read from the device but which have not yet been read by the
        # user - mode app with a handle to that device. Arguments:
        # HidDeviceObject A handle to a Hid Device Object. NumberBuffers New
        # number of buffers to use for this file handle to the Hid device
        # Return Value: TRUE if successful FALSE otherwise - - Use
        # GetLastError() to get extended error information - -        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetPhysicalDescriptor(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetPhysicalDescriptor = hid.HidD_GetPhysicalDescriptor
        HidD_GetPhysicalDescriptor.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetPhysicalDescriptor(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetPhysicalDescriptor = hid.HidD_GetPhysicalDescriptor
        HidD_GetPhysicalDescriptor.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_GetPhysicalDescriptor(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetPhysicalDescriptor = hid.HidD_GetPhysicalDescriptor
        HidD_GetPhysicalDescriptor.restype = BOOLEAN

        # + + Routine Description: This function retrieves the raw physical
        # descriptor for the specified Hid device. Arguments: HidDeviceObject
        # A handle to a Hid Device Object. Buffer Buffer which on return will
        # contain the physical descriptor if one exists for the specified
        # device handle BufferLength Length of buffer (in bytes) Return Value:
        # TRUE if successful FALSE otherwise - - Use GetLastError() to get
        # extended error information - -        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetManufacturerString(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetManufacturerString = hid.HidD_GetManufacturerString
        HidD_GetManufacturerString.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetManufacturerString(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetManufacturerString = hid.HidD_GetManufacturerString
        HidD_GetManufacturerString.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_GetManufacturerString(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetManufacturerString = hid.HidD_GetManufacturerString
        HidD_GetManufacturerString.restype = BOOLEAN

        # + + Routine Description: This function retrieves the manufacturer
        # string from the specified Hid device. Arguments: HidDeviceObject A
        # handle to a Hid Device Object. Buffer Buffer which on return will
        # contain the manufacturer string returned from the device. This
        # string is a wide - CHARacter string BufferLength Length of Buffer
        # (in bytes) Return Value: TRUE if successful FALSE otherwise - - Use
        # GetLastError() to get extended error information - -        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetProductString(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetProductString = hid.HidD_GetProductString
        HidD_GetProductString.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetProductString(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetProductString = hid.HidD_GetProductString
        HidD_GetProductString.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_GetProductString(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetProductString = hid.HidD_GetProductString
        HidD_GetProductString.restype = BOOLEAN

        # + + Routine Description: This function retrieves the product string
        # from the specified Hid device. Arguments: HidDeviceObject A handle
        # to a Hid Device Object. Buffer Buffer which on return will contain
        # the product string returned from the device. This string is a wide -
        # CHARacter string BufferLength Length of Buffer (in bytes) Return
        # Value: TRUE if successful FALSE otherwise - - Use GetLastError() to
        # get extended error information - -        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetIndexedString(
        # _In_    HANDLE   HidDeviceObject,
        # _In_    ULONG    StringIndex,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetIndexedString = hid.HidD_GetIndexedString
        HidD_GetIndexedString.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetIndexedString(
        # _In_    HANDLE   HidDeviceObject,
        # _In_    ULONG    StringIndex,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetIndexedString = hid.HidD_GetIndexedString
        HidD_GetIndexedString.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_GetIndexedString(
        # _In_    HANDLE   HidDeviceObject,
        # _In_    ULONG    StringIndex,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetIndexedString = hid.HidD_GetIndexedString
        HidD_GetIndexedString.restype = BOOLEAN

        # + + Routine Description: This function retrieves a string from the
        # specified Hid device that is specified with a certain string index.
        # Arguments: HidDeviceObject A handle to a Hid Device Object.
        # StringIndex Index of the string to retrieve Buffer Buffer which on
        # return will contain the product string returned from the device.
        # This string is a wide - CHARacter string BufferLength Length of
        # Buffer (in bytes) Return Value: TRUE if successful FALSE otherwise -
        # - Use GetLastError() to get extended error information - -
        # _Must_inspect_result_
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetSerialNumberString(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetSerialNumberString = hid.HidD_GetSerialNumberString
        HidD_GetSerialNumberString.restype = BOOLEAN
        # _Success_(return == TRUE)
        # BOOLEAN __stdcall
        # HidD_GetSerialNumberString(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetSerialNumberString = hid.HidD_GetSerialNumberString
        HidD_GetSerialNumberString.restype = BOOLEAN
        # BOOLEAN __stdcall
        # HidD_GetSerialNumberString(
        # _In_    HANDLE   HidDeviceObject,
        # _Out_writes_bytes_(BufferLength) PVOID Buffer,
        # _In_    ULONG    BufferLength
        # );
        HidD_GetSerialNumberString = hid.HidD_GetSerialNumberString
        HidD_GetSerialNumberString.restype = BOOLEAN

        # + + Routine Description: This function retrieves the serial number
        # string from the specified Hid device. Arguments: HidDeviceObject A
        # handle to a Hid Device Object. Buffer Buffer which on return will
        # contain the serial number string returned from the device. This
        # string is a wide - CHARacter string BufferLength Length of Buffer
        # (in bytes) Return Value: TRUE if successful FALSE otherwise - - Use
        # GetLastError() to get extended error information - -
        if NTDDI_VERSION >= NTDDI_WINXP:
            # _Must_inspect_result_
            # _Success_(return == TRUE)
            # BOOLEAN __stdcall
            # HidD_GetMsGenreDescriptor(
            # _In_    HANDLE   HidDeviceObject,
            # _Out_writes_bytes_(BufferLength) PVOID Buffer,
            # _In_    ULONG    BufferLength
            # );
            HidD_GetMsGenreDescriptor = hid.HidD_GetMsGenreDescriptor
            HidD_GetMsGenreDescriptor.restype = BOOLEAN
            # _Success_(return == TRUE)
            # BOOLEAN __stdcall
            # HidD_GetMsGenreDescriptor(
            # _In_    HANDLE   HidDeviceObject,
            # _Out_writes_bytes_(BufferLength) PVOID Buffer,
            # _In_    ULONG    BufferLength
            # );
            HidD_GetMsGenreDescriptor = hid.HidD_GetMsGenreDescriptor
            HidD_GetMsGenreDescriptor.restype = BOOLEAN
            # BOOLEAN __stdcall
            # HidD_GetMsGenreDescriptor(
            # _In_    HANDLE   HidDeviceObject,
            # _Out_writes_bytes_(BufferLength) PVOID Buffer,
            # _In_    ULONG    BufferLength
            # );
            HidD_GetMsGenreDescriptor = hid.HidD_GetMsGenreDescriptor
            HidD_GetMsGenreDescriptor.restype = BOOLEAN

            # + + Routine Description: This function retrieves the Microsoft
            # Genre descriptor from the specified Hid device. Arguments:
            # HidDeviceObject A handle to a Hid Device Object. Buffer Buffer
            # which on return will contain the descriptor returned from the
            # device. BufferLength Length of Buffer (in bytes) Return Value:
            # TRUE if successful FALSE otherwise - - Use GetLastError() to get
            # extended error information - -        # END IF
        if defined(__cplusplus):
            pass
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF
