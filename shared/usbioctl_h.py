import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

class _USB_START_FAILDATA(ctypes.Structure):
    pass


USB_START_FAILDATA = _USB_START_FAILDATA
PUSB_START_FAILDATA = POINTER(_USB_START_FAILDATA)


class _USB_TOPOLOGY_ADDRESS(ctypes.Structure):
    pass


USB_TOPOLOGY_ADDRESS = _USB_TOPOLOGY_ADDRESS
PUSB_TOPOLOGY_ADDRESS = POINTER(_USB_TOPOLOGY_ADDRESS)


class _USB_HUB_INFORMATION(ctypes.Structure):
    pass


USB_HUB_INFORMATION = _USB_HUB_INFORMATION
PUSB_HUB_INFORMATION = POINTER(_USB_HUB_INFORMATION)


class _USB_MI_PARENT_INFORMATION(ctypes.Structure):
    pass


USB_MI_PARENT_INFORMATION = _USB_MI_PARENT_INFORMATION
PUSB_MI_PARENT_INFORMATION = POINTER(_USB_MI_PARENT_INFORMATION)


class _USB_NODE_INFORMATION(ctypes.Structure):
    pass


USB_NODE_INFORMATION = _USB_NODE_INFORMATION
PUSB_NODE_INFORMATION = POINTER(_USB_NODE_INFORMATION)


class _USB_PIPE_INFO(ctypes.Structure):
    pass


USB_PIPE_INFO = _USB_PIPE_INFO
PUSB_PIPE_INFO = POINTER(_USB_PIPE_INFO)


class _USB_NODE_CONNECTION_INFORMATION(ctypes.Structure):
    pass


USB_NODE_CONNECTION_INFORMATION = _USB_NODE_CONNECTION_INFORMATION
PUSB_NODE_CONNECTION_INFORMATION = POINTER(_USB_NODE_CONNECTION_INFORMATION)


class _USB_NODE_CONNECTION_DRIVERKEY_NAME(ctypes.Structure):
    pass


USB_NODE_CONNECTION_DRIVERKEY_NAME = _USB_NODE_CONNECTION_DRIVERKEY_NAME
PUSB_NODE_CONNECTION_DRIVERKEY_NAME = POINTER(_USB_NODE_CONNECTION_DRIVERKEY_NAME)


class _USB_NODE_CONNECTION_NAME(ctypes.Structure):
    pass


USB_NODE_CONNECTION_NAME = _USB_NODE_CONNECTION_NAME
PUSB_NODE_CONNECTION_NAME = POINTER(_USB_NODE_CONNECTION_NAME)


class _USB_HUB_NAME(ctypes.Structure):
    pass


USB_HUB_NAME = _USB_HUB_NAME
PUSB_HUB_NAME = POINTER(_USB_HUB_NAME)


class _USB_ROOT_HUB_NAME(ctypes.Structure):
    pass


USB_ROOT_HUB_NAME = _USB_ROOT_HUB_NAME
PUSB_ROOT_HUB_NAME = POINTER(_USB_ROOT_HUB_NAME)


class _USB_HCD_DRIVERKEY_NAME(ctypes.Structure):
    pass


USB_HCD_DRIVERKEY_NAME = _USB_HCD_DRIVERKEY_NAME
PUSB_HCD_DRIVERKEY_NAME = POINTER(_USB_HCD_DRIVERKEY_NAME)


class _USB_DESCRIPTOR_REQUEST(ctypes.Structure):
    pass


USB_DESCRIPTOR_REQUEST = _USB_DESCRIPTOR_REQUEST
PUSB_DESCRIPTOR_REQUEST = POINTER(_USB_DESCRIPTOR_REQUEST)


class _USB_HUB_CAPABILITIES(ctypes.Structure):
    pass


USB_HUB_CAPABILITIES = _USB_HUB_CAPABILITIES
PUSB_HUB_CAPABILITIES = POINTER(_USB_HUB_CAPABILITIES)


class _USB_NODE_CONNECTION_ATTRIBUTES(ctypes.Structure):
    pass


USB_NODE_CONNECTION_ATTRIBUTES = _USB_NODE_CONNECTION_ATTRIBUTES
PUSB_NODE_CONNECTION_ATTRIBUTES = POINTER(_USB_NODE_CONNECTION_ATTRIBUTES)


class _USB_NODE_CONNECTION_INFORMATION_EX(ctypes.Structure):
    pass


USB_NODE_CONNECTION_INFORMATION_EX = _USB_NODE_CONNECTION_INFORMATION_EX
PUSB_NODE_CONNECTION_INFORMATION_EX = POINTER(_USB_NODE_CONNECTION_INFORMATION_EX)


class _USB_HUB_CAP_FLAGS(ctypes.Union):
    pass


USB_HUB_CAP_FLAGS = _USB_HUB_CAP_FLAGS
PUSB_HUB_CAP_FLAGS = POINTER(_USB_HUB_CAP_FLAGS)


class _USB_HUB_CAPABILITIES_EX(ctypes.Structure):
    pass


USB_HUB_CAPABILITIES_EX = _USB_HUB_CAPABILITIES_EX
PUSB_HUB_CAPABILITIES_EX = POINTER(_USB_HUB_CAPABILITIES_EX)


class _USB_CYCLE_PORT_PARAMS(ctypes.Structure):
    pass


USB_CYCLE_PORT_PARAMS = _USB_CYCLE_PORT_PARAMS
PUSB_CYCLE_PORT_PARAMS = POINTER(_USB_CYCLE_PORT_PARAMS)


class _USB_ID_STRING(ctypes.Structure):
    pass


USB_ID_STRING = _USB_ID_STRING
PUSB_ID_STRING = POINTER(_USB_ID_STRING)


class _USB_HUB_DEVICE_UXD_SETTINGS(ctypes.Structure):
    pass


USB_HUB_DEVICE_UXD_SETTINGS = _USB_HUB_DEVICE_UXD_SETTINGS
PUSB_HUB_DEVICE_UXD_SETTINGS = POINTER(_USB_HUB_DEVICE_UXD_SETTINGS)


class _HUB_DEVICE_CONFIG_INFO_V1(ctypes.Structure):
    pass


HUB_DEVICE_CONFIG_INFO = _HUB_DEVICE_CONFIG_INFO_V1
PHUB_DEVICE_CONFIG_INFO = POINTER(_HUB_DEVICE_CONFIG_INFO_V1)


class _HCD_STAT_COUNTERS(ctypes.Structure):
    pass


HCD_STAT_COUNTERS = _HCD_STAT_COUNTERS
PHCD_STAT_COUNTERS = POINTER(_HCD_STAT_COUNTERS)


class _HCD_ISO_STAT_COUNTERS(ctypes.Structure):
    pass


HCD_ISO_STAT_COUNTERS = _HCD_ISO_STAT_COUNTERS
PHCD_ISO_STAT_COUNTERS = POINTER(_HCD_ISO_STAT_COUNTERS)


class _HCD_STAT_INFORMATION_1(ctypes.Structure):
    pass


HCD_STAT_INFORMATION_1 = _HCD_STAT_INFORMATION_1
PHCD_STAT_INFORMATION_1 = POINTER(_HCD_STAT_INFORMATION_1)


class _HCD_STAT_INFORMATION_2(ctypes.Structure):
    pass


HCD_STAT_INFORMATION_2 = _HCD_STAT_INFORMATION_2
PHCD_STAT_INFORMATION_2 = POINTER(_HCD_STAT_INFORMATION_2)


class _USB_NOTIFICATION(ctypes.Structure):
    pass


USB_NOTIFICATION = _USB_NOTIFICATION
PUSB_NOTIFICATION = POINTER(_USB_NOTIFICATION)


class _USB_CONNECTION_NOTIFICATION(ctypes.Structure):
    pass


USB_CONNECTION_NOTIFICATION = _USB_CONNECTION_NOTIFICATION
PUSB_CONNECTION_NOTIFICATION = POINTER(_USB_CONNECTION_NOTIFICATION)


class _USB_BUS_NOTIFICATION(ctypes.Structure):
    pass


USB_BUS_NOTIFICATION = _USB_BUS_NOTIFICATION
PUSB_BUS_NOTIFICATION = POINTER(_USB_BUS_NOTIFICATION)


class _USB_ACQUIRE_INFO(ctypes.Structure):
    pass


USB_ACQUIRE_INFO = _USB_ACQUIRE_INFO
PUSB_ACQUIRE_INFO = POINTER(_USB_ACQUIRE_INFO)


class _USB_DEVICE_STATE(ctypes.Structure):
    pass


USB_DEVICE_STATE = _USB_DEVICE_STATE
PUSB_DEVICE_STATE = POINTER(_USB_DEVICE_STATE)


class _USB_HUB_PORT_INFORMATION(ctypes.Structure):
    pass


USB_HUB_PORT_INFORMATION = _USB_HUB_PORT_INFORMATION
PUSB_HUB_PORT_INFORMATION = POINTER(_USB_HUB_PORT_INFORMATION)


class _USB_HUB_DEVICE_INFO(ctypes.Structure):
    pass


USB_HUB_DEVICE_INFO = _USB_HUB_DEVICE_INFO
PUSB_HUB_DEVICE_INFO = POINTER(_USB_HUB_DEVICE_INFO)


class _USB_COMPOSITE_FUNCTION_INFO(ctypes.Structure):
    pass


USB_COMPOSITE_FUNCTION_INFO = _USB_COMPOSITE_FUNCTION_INFO
PUSB_COMPOSITE_FUNCTION_INFO = POINTER(_USB_COMPOSITE_FUNCTION_INFO)


class _USB_COMPOSITE_DEVICE_INFO(ctypes.Structure):
    pass


USB_COMPOSITE_DEVICE_INFO = _USB_COMPOSITE_DEVICE_INFO
PUSB_COMPOSITE_DEVICE_INFO = POINTER(_USB_COMPOSITE_DEVICE_INFO)


class _USB_CONTROLLER_DEVICE_INFO(ctypes.Structure):
    pass


USB_CONTROLLER_DEVICE_INFO = _USB_CONTROLLER_DEVICE_INFO
PUSB_CONTROLLER_DEVICE_INFO = POINTER(_USB_CONTROLLER_DEVICE_INFO)


class _USB_DEVICE_INFO(ctypes.Structure):
    pass


USB_DEVICE_INFO = _USB_DEVICE_INFO
PUSB_DEVICE_INFO = POINTER(_USB_DEVICE_INFO)


class _USB_DEVICE_NODE_INFO(ctypes.Structure):
    pass


USB_DEVICE_NODE_INFO = _USB_DEVICE_NODE_INFO
PUSB_DEVICE_NODE_INFO = POINTER(_USB_DEVICE_NODE_INFO)


class _USB_DEVICE_PERFORMANCE_INFO(ctypes.Structure):
    pass


USB_DEVICE_PERFORMANCE_INFO = _USB_DEVICE_PERFORMANCE_INFO
PUSB_DEVICE_PERFORMANCE_INFO = POINTER(_USB_DEVICE_PERFORMANCE_INFO)


class _USB_HUB_INFORMATION_EX(ctypes.Structure):
    pass


USB_HUB_INFORMATION_EX = _USB_HUB_INFORMATION_EX
PUSB_HUB_INFORMATION_EX = POINTER(_USB_HUB_INFORMATION_EX)


class _USB_PORT_PROPERTIES(ctypes.Union):
    pass


USB_PORT_PROPERTIES = _USB_PORT_PROPERTIES
PUSB_PORT_PROPERTIES = POINTER(_USB_PORT_PROPERTIES)


class _USB_PORT_CONNECTOR_PROPERTIES(ctypes.Structure):
    pass


USB_PORT_CONNECTOR_PROPERTIES = _USB_PORT_CONNECTOR_PROPERTIES
PUSB_PORT_CONNECTOR_PROPERTIES = POINTER(_USB_PORT_CONNECTOR_PROPERTIES)


class _USB_PROTOCOLS(ctypes.Union):
    pass


USB_PROTOCOLS = _USB_PROTOCOLS
PUSB_PROTOCOLS = POINTER(_USB_PROTOCOLS)


class _USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS(ctypes.Union):
    pass


USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS = _USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS
PUSB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS = POINTER(_USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS)


class _USB_NODE_CONNECTION_INFORMATION_EX_V2(ctypes.Structure):
    pass


USB_NODE_CONNECTION_INFORMATION_EX_V2 = _USB_NODE_CONNECTION_INFORMATION_EX_V2
PUSB_NODE_CONNECTION_INFORMATION_EX_V2 = POINTER(_USB_NODE_CONNECTION_INFORMATION_EX_V2)


class _USB_TRANSPORT_CHARACTERISTICS(ctypes.Structure):
    pass


USB_TRANSPORT_CHARACTERISTICS = _USB_TRANSPORT_CHARACTERISTICS
PUSB_TRANSPORT_CHARACTERISTICS = POINTER(_USB_TRANSPORT_CHARACTERISTICS)


class _USB_TRANSPORT_CHARACTERISTICS_CHANGE_REGISTRATION(ctypes.Structure):
    pass


USB_TRANSPORT_CHARACTERISTICS_CHANGE_REGISTRATION = _USB_TRANSPORT_CHARACTERISTICS_CHANGE_REGISTRATION
PUSB_TRANSPORT_CHARACTERISTICS_CHANGE_REGISTRATION = POINTER(_USB_TRANSPORT_CHARACTERISTICS_CHANGE_REGISTRATION)


class _USB_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION(ctypes.Structure):
    pass


USB_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION = _USB_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION
PUSB_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION = POINTER(_USB_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION)


class _USB_TRANSPORT_CHARACTERISTICS_CHANGE_UNREGISTRATION(ctypes.Structure):
    pass


USB_TRANSPORT_CHARACTERISTICS_CHANGE_UNREGISTRATION = _USB_TRANSPORT_CHARACTERISTICS_CHANGE_UNREGISTRATION
PUSB_TRANSPORT_CHARACTERISTICS_CHANGE_UNREGISTRATION = POINTER(_USB_TRANSPORT_CHARACTERISTICS_CHANGE_UNREGISTRATION)


class _USB_DEVICE_CHARACTERISTICS(ctypes.Structure):
    pass


USB_DEVICE_CHARACTERISTICS = _USB_DEVICE_CHARACTERISTICS
PUSB_DEVICE_CHARACTERISTICS = POINTER(_USB_DEVICE_CHARACTERISTICS)


class _USB_START_TRACKING_FOR_TIME_SYNC_INFORMATION(ctypes.Structure):
    pass


USB_START_TRACKING_FOR_TIME_SYNC_INFORMATION = _USB_START_TRACKING_FOR_TIME_SYNC_INFORMATION
PUSB_START_TRACKING_FOR_TIME_SYNC_INFORMATION = POINTER(_USB_START_TRACKING_FOR_TIME_SYNC_INFORMATION)


class _USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION(ctypes.Structure):
    pass


USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION = _USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION
PUSB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION = POINTER(_USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION)


class _USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION(ctypes.Structure):
    pass


USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION = _USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION
PUSB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION = POINTER(_USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION)


# + + Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# USBIOCTL.H Abstract: This file defines both kernel and user mode IOCTL codes
# supported by the USB core stack. These APIs are the APIS supported by th USB
# hub driver and the USB bus driver AKA USBPORT. Typically only user mode
# applications (usbui) or the hub driver include this file, USB drivers should
# use usbdrivr.h usb bus drivers should include usbkern.h Environment: Kernel
# & user mode Revision History: 09 - 29 - 95 : created 01 - 06 - 97 : added
# user mode hub ioctls 10 - 31 - 99 : cleanup and document, jdunn 1 - 25 - 03
# : more cleanup and documentation 2 - 10 - 04 : header versioning - -

__USBIOCTL_H__ = None

if not defined(__USBIOCTL_H__):
    __USBIOCTL_H__ = 1
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.shared.devioctl_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        from pyWinAPI.shared.usb200_h import * # NOQA
        if _MSC_VER >= 1200:
            pass
        # END IF
        if not defined(FAR):
            FAR = 1
        # END IF
        from pyWinAPI.shared.usbiodef_h import * # NOQA

        # IOCTL definitions
        # USB kernel Mode IOCTLS
        # Routine Description: Define the standard USB 'URB' IOCTL
        # IOCTL_INTERNAL_USB_SUBMIT_URB This IOCTL is used by client drivers
        # to submit URB (USB Request Blocks) Parameters.Others.Argument1 =
        # pointer to URB
        IOCTL_INTERNAL_USB_SUBMIT_URB = CTL_CODE(
            FILE_DEVICE_USB,
            USB_SUBMIT_URB,
            METHOD_NEITHER,
            FILE_ANY_ACCESS,
        )

        # IOCTL_INTERNAL_USB_RESET_PORT This IOCTL is used by kernel mode
        # drivers to reset their upstream port. After a successful reset the
        # device is re - configured to the same configuration it was in before
        # the reset. All pipe handles, configuration handles and interface
        # handles remain valid.
        IOCTL_INTERNAL_USB_RESET_PORT = CTL_CODE(
            FILE_DEVICE_USB,
            USB_RESET_PORT,
            METHOD_NEITHER,
            FILE_ANY_ACCESS,
        )

        # IOCTL_INTERNAL_USB_GET_ROOTHUB_PDO Routine Description: This
        # function is used to by hubs to get the top of the physical USB
        # stack. All IRPs passed to a hub PDO are either serviced by the hub
        # or forwarded directly to the top of the bus driver stack i.e. the
        # root hub PDO. A filter driver interested only in bus traffic
        # (AKA Urbs) can see such traffic by attaching to the top of the root
        # hub PDO, see section 9. Parameters: ioStackLocation -
        # >Parameters.Others.Argument1 >> RootHubPhysicalDeviceObject This
        # parameter contains a pointer that is filled in with the root hub
        # PDO. This is the actual PDO created by the USBPORT driver for the
        # root hub. ioStackLocation - >Parameters.Others.Argument2 >>
        # HcdTopOfStack This parameter contains a pointer that is filled in
        # with the top of the bus driver stack is the device object returned
        # when the hub driver attached to top of the device stack associated
        # with the root hub PDO.
        IOCTL_INTERNAL_USB_GET_ROOTHUB_PDO = CTL_CODE(
            FILE_DEVICE_USB,
            USB_GET_ROOTHUB_PDO,
            METHOD_NEITHER,
            FILE_ANY_ACCESS,
        )
        USBD_PORT_ENABLED = 0x00000001
        USBD_PORT_CONNECTED = 0x00000002

        # IOCTL_INTERNAL_USB_GET_PORT_STATUS Routine Description: This
        # function returns the current 'live' status of the port. It can be
        # used by client drivers to determine the current state of their
        # device because certain hardware errors on the bus can result in a
        # device port being disabled . The hub driver must communicate with
        # the hub to get this information, if it cannot for some reason a
        # failure status is returned. This API will fail if called at raised
        # IRQL. IRQL: Passive Parameters: ioStackLocation -
        # >Parameters.Others.Argument1 A pointer to a ULONG that is filled in
        # with the port status bits defined below:
        IOCTL_INTERNAL_USB_GET_PORT_STATUS = CTL_CODE(
            FILE_DEVICE_USB,
            USB_GET_PORT_STATUS,
            METHOD_NEITHER,
            FILE_ANY_ACCESS,
        )

        # IOCTL_INTERNAL_USB_ENABLE_PORT is obsolete, drivers should use
        # IOCTL_INTERNAL_USB_RESET_PORT
        IOCTL_INTERNAL_USB_ENABLE_PORT = CTL_CODE(
            FILE_DEVICE_USB,
            USB_ENABLE_PORT,
            METHOD_NEITHER,
            FILE_ANY_ACCESS,
        )

        # IOCTL_INTERNAL_USB_GET_HUB_COUNT Routine Description: This function
        # is used to count the number of hubs in the stack. It is used to
        # enforce the electrical limitation of no more that 5 hubs plus the
        # root being chained together. Parameters: ioStackLocation -
        # >Parameters.Others.Argument1 >> Count This parameter contains a
        # pointer that is filled in with the current count of hubs in the
        # stack. Each instance of the hub driver that receives the IRP
        # increments the counter and passes the irp on to its' PDO. When the
        # Irp reaches the hub that is the root the IRP is completed. This will
        # result in the count value being equal to the number of hubs
        # (including the root).
        IOCTL_INTERNAL_USB_GET_HUB_COUNT = CTL_CODE(
            FILE_DEVICE_USB,
            USB_GET_HUB_COUNT,
            METHOD_NEITHER,
            FILE_ANY_ACCESS,
        )

        # IOCTL_INTERNAL_USB_CYCLE_PORT This IOCTL will simulate a plug/unplug
        # on the drivers upstream port. The device will be removed and re -
        # added by PnP.
        IOCTL_INTERNAL_USB_CYCLE_PORT = CTL_CODE(
            FILE_DEVICE_USB,
            USB_CYCLE_PORT,
            METHOD_NEITHER,
            FILE_ANY_ACCESS,
        )

        # IOCTL_INTERNAL_USB_GET_HUB_NAME Routine Description: This API
        # returns the UNICODE symbolic name for the PDO if the PDO is for a
        # usbhub, otherwise a NULL string is returned. The symbolic name can
        # be used to retrieve additional information about the hub through
        # user mode ioctl apis and WMI calls. Parameters: ioStackLocation -
        # >Parameters.DeviceIoControl.OutputBufferLength Length of buffer
        # passed bytes. Irp - >AssociatedIrp.SystemBuffer A pointer to a
        # structure (USB_HUB_NAME) to receive the symbolic name.
        # USB_BUS_NOTIFICATION. ActualLength - The structure size in bytes
        # necessary to hold the NULL terminated symbolic link name. This
        # includes the entire structure, not just the name. HubName - The
        # UNICODE NULL terminated symbolic link name of the external hub
        # attached to the port. If there is no external hub attached to the
        # port a single NULL is returned.
        IOCTL_INTERNAL_USB_GET_HUB_NAME = CTL_CODE(
            FILE_DEVICE_USB,
            USB_GET_HUB_NAME,
            METHOD_BUFFERED,
            FILE_ANY_ACCESS,
        )

        # IOCTL_INTERNAL_USB_GET_BUS_INFO is obsolete - - it has been replaced
        # by the USB_BUSIFFN_QUERY_BUS_INFORMATION service available thru the
        # usb stack bus interface. Drivers should use the bus interface
        # function instead
        IOCTL_INTERNAL_USB_GET_BUS_INFO = CTL_CODE(
            FILE_DEVICE_USB,
            USB_GET_BUS_INFO,
            METHOD_BUFFERED,
            FILE_ANY_ACCESS,
        )
        IOCTL_INTERNAL_USB_GET_CONTROLLER_NAME = CTL_CODE(
            FILE_DEVICE_USB,
            USB_GET_CONTROLLER_NAME,
            METHOD_BUFFERED,
            FILE_ANY_ACCESS,
        )
        IOCTL_INTERNAL_USB_GET_BUSGUID_INFO = CTL_CODE(
            FILE_DEVICE_USB,
            USB_GET_BUSGUID_INFO,
            METHOD_BUFFERED,
            FILE_ANY_ACCESS,
        )
        IOCTL_INTERNAL_USB_GET_PARENT_HUB_INFO = CTL_CODE(
            FILE_DEVICE_USB,
            USB_GET_PARENT_HUB_INFO,
            METHOD_BUFFERED,
            FILE_ANY_ACCESS,
        )

        # USB kernel Mode IOCTLS defined for windows XP and later
        if _WIN32_WINNT >= 0x0501:
            # IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION This ioctl registers
            # a device to receive notification when a specific timeout has
            # expired and it should now be suspended in order to conserve
            # power. If all devices on a hub are suspended, then the actual
            # hub can be suspended. Routine Description: This function is part
            # of the hub drivers selective suspend feature
            # (see section 2 usbhub.doc). This API is serviced only by hubs it
            # is not supported by a USB Port driver. The client USB drivers
            # use this API to register an idle callback request with the
            # parent hub. The details on how this API is handled can be found
            # in section 2. Parameters: ioStackLocation -
            # >Parameters.Others.Argument1 >> IdeCallbackInfo A pointer to a
            # structure containing the callback routine and a context value.
            # _IRQL_requires_max_(PASSIVE_LEVEL) typedef VOID
            # (*USB_IDLE_CALLBACK)( _In_ PVOID Context ); typedef struct
            # _USB_IDLE_CALLBACK_INFO
            # { USB_IDLE_CALLBACK IdleCallback; PVOID IdleContext; }
            # USB_IDLE_CALLBACK_INFO, *PUSB_IDLE_CALLBACK_INFO;
            IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION = CTL_CODE(
                FILE_DEVICE_USB,
                USB_IDLE_NOTIFICATION,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )

            # IOCTL_INTERNAL_USB_GET_DEVICE_HANDLE Routine Description: This
            # function returns the device handle associated with the callers
            # PDO. The device handle is an opaque structure that is used as a
            # parameter for other APIs/ Parameters: ioStackLocation -
            # >Parameters.Others.Argument1 A pointer to a device handle
            # (pointer to pointer).
            IOCTL_INTERNAL_USB_GET_DEVICE_HANDLE = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_DEVICE_HANDLE,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )
        # END IF
        # USB kernel Mode IOCTLS defined for windows Longhorn and later
        if _WIN32_WINNT >= 0x0600:
            IOCTL_INTERNAL_USB_NOTIFY_IDLE_READY = CTL_CODE(
                FILE_DEVICE_USB,
                USB_IDLE_NOTIFICATION_EX,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )
            IOCTL_INTERNAL_USB_REQ_GLOBAL_SUSPEND = CTL_CODE(
                FILE_DEVICE_USB,
                USB_REQ_GLOBAL_SUSPEND,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )
            IOCTL_INTERNAL_USB_REQ_GLOBAL_RESUME = CTL_CODE(
                FILE_DEVICE_USB,
                USB_REQ_GLOBAL_RESUME,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )

            # IOCTL_INTERNAL_USB_RECORD_FAILURE

            USB20_API = 0

            if defined(USB20_API):
                from pyWinAPI.shared.usb_h import * # NOQA

                _USB_START_FAILDATA._fields_ = [
                    ('LengthInBytes', ULONG),
                    ('NtStatus', NTSTATUS),
                    ('UsbdStatus', USBD_STATUS),
                    ('ConnectStatus', ULONG),
                    ('DriverData', UCHAR * 4),
                ]
            # END IF
            IOCTL_INTERNAL_USB_RECORD_FAILURE = CTL_CODE(
                FILE_DEVICE_USB,
                USB_RECORD_FAILURE,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )
            IOCTL_INTERNAL_USB_GET_DEVICE_HANDLE_EX = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_DEVICE_HANDLE_EX,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )
            IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_TT_DEVICE_HANDLE,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )

            # IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS
            _USB_TOPOLOGY_ADDRESS._fields_ = [
                ('PciBusNumber', ULONG),
                ('PciDeviceNumber', ULONG),
                ('PciFunctionNumber', ULONG),
                ('Reserved', ULONG),
                ('RootHubPortNumber', USHORT),
                ('HubPortNumber', USHORT * 5),
                ('Reserved2', USHORT),
            ]
            IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_TOPOLOGY_ADDRESS,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )
            IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_HUB_CONFIG_INFO,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN8:
            # USB kernel Mode IOCTLS defined for Win8 and later. Pivot on
            # NTDDI_VERSION instead of _WIN32_WINNT Note: These ioctls use
            # FILE_DEVICE_USBEX. All previously defined USB Ioctls use
            # FILE_DEVICE_USB (aka FILE_DEVICE_UNKNOWN).
            IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE = CTL_CODE(
                FILE_DEVICE_USBEX,
                USB_REGISTER_COMPOSITE_DEVICE,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )
            IOCTL_INTERNAL_USB_UNREGISTER_COMPOSITE_DEVICE = CTL_CODE(
                FILE_DEVICE_USBEX,
                USB_UNREGISTER_COMPOSITE_DEVICE,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )
            IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION = CTL_CODE(
                FILE_DEVICE_USBEX,
                USB_REQUEST_REMOTE_WAKE_NOTIFICATION,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN10:
            # IOCTL_INTERNAL_USB_FAIL_GET_STATUS_FROM_DEVICE This IOCTL is
            # used by kernel mode drivers to inform HUB driver that device
            # doesn't support IOCTL_INTERNAL_USB_GET_STATUS_FROM_DEVICE
            IOCTL_INTERNAL_USB_FAIL_GET_STATUS_FROM_DEVICE = CTL_CODE(
                FILE_DEVICE_USB,
                USB_FAIL_GET_STATUS,
                METHOD_NEITHER,
                FILE_ANY_ACCESS,
            )
        # END IF
        # USB user mode IOCTLS

        USB_KERNEL_IOCTL = None
        if not defined(USB_KERNEL_IOCTL):
            # ************************************************************************ The following IOCTLS are always sent to the HCD symbolic name ************************************************************************
            #
            # IOCTL_USB_HCD_GET_STATS_1 (OPTIONAL) The following IOCTL is used
            # to return internal statictics for HCDs
            IOCTL_USB_HCD_GET_STATS_1 = CTL_CODE(
                FILE_DEVICE_USB,
                HCD_GET_STATS_1,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )

            # IOCTL_USB_HCD_GET_STATS_2 (OPTIONAL) The following IOCTL is used
            # to return internal statictics for HCDs
            IOCTL_USB_HCD_GET_STATS_2 = CTL_CODE(
                FILE_DEVICE_USB,
                HCD_GET_STATS_2,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_HCD_DISABLE_PORT = CTL_CODE(
                FILE_DEVICE_USB,
                HCD_DISABLE_PORT,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_HCD_ENABLE_PORT = CTL_CODE(
                FILE_DEVICE_USB,
                HCD_ENABLE_PORT,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )

            # These ioctls are used for USB diagnostic and test applications

            IOCTL_USB_DIAGNOSTIC_MODE_ON = None
            if not defined(IOCTL_USB_DIAGNOSTIC_MODE_ON):
                IOCTL_USB_DIAGNOSTIC_MODE_ON = CTL_CODE(
                    FILE_DEVICE_USB,
                    HCD_DIAGNOSTIC_MODE_ON,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
            # END IF

            IOCTL_USB_DIAGNOSTIC_MODE_OFF = None
            if not defined(IOCTL_USB_DIAGNOSTIC_MODE_OFF):
                IOCTL_USB_DIAGNOSTIC_MODE_OFF = CTL_CODE(
                    FILE_DEVICE_USB,
                    HCD_DIAGNOSTIC_MODE_OFF,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
            # END IF

            IOCTL_USB_GET_ROOT_HUB_NAME = None
            if not defined(IOCTL_USB_GET_ROOT_HUB_NAME):
                IOCTL_USB_GET_ROOT_HUB_NAME = CTL_CODE(
                    FILE_DEVICE_USB,
                    HCD_GET_ROOT_HUB_NAME,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
            # END IF

            IOCTL_GET_HCD_DRIVERKEY_NAME = None
            if not defined(IOCTL_GET_HCD_DRIVERKEY_NAME):
                IOCTL_GET_HCD_DRIVERKEY_NAME = CTL_CODE(
                    FILE_DEVICE_USB,
                    HCD_GET_DRIVERKEY_NAME,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
            # END IF
            # *****************************************************************
            # ******* The following IOCTLS are always sent to symbolic names
            # created by usbhub **********************************************
            # **************************
            #
            # Utility IOCTLS supported by the hub device
            # These ioctls are supported by the hub driver for use by user
            # mode USB utilities.
            # IOCTL_USB_GET_NODE_INFORMATION Routine Description: Returns
            # information about the USB hub in the user buffer passed in. If
            # the IOCTL is sent to the hub NodeType is set to UsbHub and
            # USB_HUB_INFORMATION is returned this includes the hub descriptor
            # and a flag indicating if the hub is bus vs self powered . This
            # API returns FAILURE (STATUS_UNSUCCESSFUL) if the hub is not
            # started or otherwise not functional. Parameters: Input: Irp -
            # >AssociatedIrp.SystemBuffer - pointer to USB_NODE_INFORMATION
            # structure Ouput: USB_NODE_INFORMATION filled in as appropriate
            IOCTL_USB_GET_NODE_INFORMATION = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_NODE_INFORMATION,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )

            # IOCTL_USB_GET_NODE_CONNECTION_INFORMATION Exactly the same as
            # _EX but the speed field is a Boolean LowSpeed - TRUE if the
            # device is low speed.
            IOCTL_USB_GET_NODE_CONNECTION_INFORMATION = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_NODE_CONNECTION_INFORMATION,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_GET_NODE_CONNECTION_NAME = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_NODE_CONNECTION_NAME,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_DIAG_IGNORE_HUBS_ON = CTL_CODE(
                FILE_DEVICE_USB,
                USB_DIAG_IGNORE_HUBS_ON,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_DIAG_IGNORE_HUBS_OFF = CTL_CODE(
                FILE_DEVICE_USB,
                USB_DIAG_IGNORE_HUBS_OFF,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_GET_NODE_CONNECTION_DRIVERKEY_NAME = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_NODE_CONNECTION_DRIVERKEY_NAME,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )

            # IOCTLS defined for Windows XP and later
            if _WIN32_WINNT >= 0x0501:
                IOCTL_USB_GET_HUB_CAPABILITIES = CTL_CODE(
                    FILE_DEVICE_USB,
                    USB_GET_HUB_CAPABILITIES,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
                IOCTL_USB_HUB_CYCLE_PORT = CTL_CODE(
                    FILE_DEVICE_USB,
                    USB_HUB_CYCLE_PORT,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )

                # IOCTL_USB_GET_NODE_CONNECTION_ATTRIBUTES Routine
                # Description: Returns the Microsoft extended port attributes
                # for a specific port. The caller inputs the port number as
                # the 'ConnectionIndex'. Microsoft extended port attributes
                # are defined in the Extended Port Attribute specification.
                # This API also returns the current connection status of the
                # port. This API returns FAILURE (STATUS_UNSUCCESSFUL) if the
                # hub is not started or otherwise not functional. Parameters:
                # Input: Irp - >AssociatedIrp.SystemBuffer - pointer to Struct
                # _USB_NODE_CONNECTION_INFORMATION { ULONG ConnectionIndex; }
                # ConnectionIndex - is the one based port number. Ouput:
                # (if a device is attached) ConnectionStatus - The current USB
                # connection status. Indicates things like enumeration failure
                # or overcurrent. PortAttributes - Extended port attributes
                # defined in usb.h.
                IOCTL_USB_GET_NODE_CONNECTION_ATTRIBUTES = CTL_CODE(
                    FILE_DEVICE_USB,
                    USB_GET_NODE_CONNECTION_ATTRIBUTES,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )

                # IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX Routine
                # Description: Returns information about a specific USB hub
                # port (AKA connection). If there is a device connected to the
                # port information about the device is also returned. The
                # caller inputs the port number as the 'ConnectionIndex'. This
                # API returns FAILURE (STATUS_UNSUCCESSFUL) if the hub is not
                # started or otherwise not functional. Parameters: Input: Irp
                # - >AssociatedIrp.SystemBuffer - pointer to Struct
                # _USB_NODE_CONNECTION_INFORMATION {
                #       ULONG ConnectionIndex;
                #       USB_DEVICE_DESCRIPTOR DeviceDescriptor;
                #       UCHAR CurrentConfigurationValue;
                #       BOOLEAN LowSpeed;
                #       BOOLEAN DeviceIsHub;
                #       USHORT DeviceAddress;
                #       ULONG NumberOfOpenPipes;
                #       USB_CONNECTION_STATUS ConnectionStatus;
                #       USB_PIPE_INFO PipeList[0];
                # } ConnectionIndex - is the one based port number.
                #  Ouput: (if a device is attached)
                # DeviceDescriptor - USB device descriptor.
                # CurrentConfigurationValue - Currently selected
                # configuration value.
                # Speed - indicates the 'current' operating speed, note
                # that high speed devices can operate at full speed when
                # necessary.
                # DeviceIsHub - TRUE if the attached device is a hub
                # DeviceAddress - USB asINT device address.
                # NumberOfOpenPipes - Number of open USB pipes in the
                # current configuration
                # ConnectionStatus - The current USB connection status.
                # USB_PIPE_INFO PipeList[0]; - list of open pipes including
                # schedule offset and endpoint descriptor.
                # This information can be used to calculate bandwidthusage.
                #
                IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX = CTL_CODE(
                    FILE_DEVICE_USB,
                    USB_GET_NODE_CONNECTION_INFORMATION_EX,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
            # END IF
            # The following IOCTLS are defined for Windows Longhorn and Later
            if _WIN32_WINNT >= 0x0600:
                IOCTL_USB_RESET_HUB = CTL_CODE(
                    FILE_DEVICE_USB,
                    USB_RESET_HUB,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
                IOCTL_USB_GET_HUB_CAPABILITIES_EX = CTL_CODE(
                    FILE_DEVICE_USB,
                    USB_GET_HUB_CAPABILITIES_EX,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
            # END IF
            # The following IOCTLs are defined for Windows 8 and later
            if NTDDI_VERSION >= NTDDI_WIN8:
                IOCTL_USB_GET_HUB_INFORMATION_EX = CTL_CODE(
                    FILE_DEVICE_USB,
                    USB_GET_HUB_INFORMATION_EX,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
                IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES = CTL_CODE(
                    FILE_DEVICE_USB,
                    USB_GET_PORT_CONNECTOR_PROPERTIES,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
                IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2 = CTL_CODE(
                    FILE_DEVICE_USB,
                    USB_GET_NODE_CONNECTION_INFORMATION_EX_V2,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
            # END IF        # END IF  #ifndef USB_KERNEL_IOCTL
        if NTDDI_VERSION >= NTDDI_WIN10_RS3:
            IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_TRANSPORT_CHARACTERISTICS,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE = CTL_CODE(
                FILE_DEVICE_USB,
                USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE = CTL_CODE(
                FILE_DEVICE_USB,
                USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE = CTL_CODE(
                FILE_DEVICE_USB,
                USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_START_TRACKING_FOR_TIME_SYNC = CTL_CODE(
                FILE_DEVICE_USB,
                USB_START_TRACKING_FOR_TIME_SYNC,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC = CTL_CODE(
                FILE_DEVICE_USB,
                USB_STOP_TRACKING_FOR_TIME_SYNC,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_USB_GET_DEVICE_CHARACTERISTICS = CTL_CODE(
                FILE_DEVICE_USB,
                USB_GET_DEVICE_CHARACTERISTICS,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
        # END IF
        if not defined(USB_KERNEL_IOCTL):
            # structures for user mode ioctls

            class _USB_HUB_NODE(ENUM):
                UsbHub = 1
                UsbMIParent = 2


            USB_HUB_NODE = _USB_HUB_NODE
            _USB_HUB_INFORMATION._fields_ = [
                ('HubDescriptor', USB_HUB_DESCRIPTOR), # copy of data from hub descriptor
                ('HubIsBusPowered', BOOLEAN),
            ]
            _USB_MI_PARENT_INFORMATION._fields_ = [
                ('NumberOfInterfaces', ULONG),
            ]


            class u(ctypes.Union):
                pass


            u._fields_ = [
                ('HubInformation', USB_HUB_INFORMATION),
                ('MiParentInformation', USB_MI_PARENT_INFORMATION),
            ]
            _USB_NODE_INFORMATION.u = u

            _USB_NODE_INFORMATION._fields_ = [
                ('NodeType', USB_HUB_NODE), # hub, mi parent
                ('u', _USB_NODE_INFORMATION.u),
            ]
            _USB_PIPE_INFO._fields_ = [
                ('EndpointDescriptor', USB_ENDPOINT_DESCRIPTOR),
                ('ScheduleOffset', ULONG),
            ]
            if _WIN32_WINNT >= 0x0600:
                # For Windows Longhorn
                class _USB_CONNECTION_STATUS(ENUM):
                    NoDeviceConnected = 1
                    DeviceConnected = 2
                    DeviceFailedEnumeration = 3
                    DeviceGeneralFailure = 4
                    DeviceCausedOvercurrent = 5
                    DeviceNotEnoughPower = 6
                    DeviceNotEnoughBandwidth = 7
                    DeviceHubNestedTooDeeply = 8
                    DeviceInLegacyHub = 9
                    DeviceEnumerating = 10
                    DeviceReset = 11


                USB_CONNECTION_STATUS = _USB_CONNECTION_STATUS
                PUSB_CONNECTION_STATUS = POINTER(_USB_CONNECTION_STATUS)
            elif _WIN32_WINNT >= 0x0501:
                # For Windows XP
                class _USB_CONNECTION_STATUS(ENUM):
                    NoDeviceConnected = 1
                    DeviceConnected = 2
                    DeviceFailedEnumeration = 3
                    DeviceGeneralFailure = 4
                    DeviceCausedOvercurrent = 5
                    DeviceNotEnoughPower = 6
                    DeviceNotEnoughBandwidth = 7
                    DeviceHubNestedTooDeeply = 8
                    DeviceInLegacyHub = 9


                USB_CONNECTION_STATUS = _USB_CONNECTION_STATUS
                PUSB_CONNECTION_STATUS = POINTER(_USB_CONNECTION_STATUS)
            else:
                # For Windows 2000
                class _USB_CONNECTION_STATUS(ENUM):
                    NoDeviceConnected = 1
                    DeviceConnected = 2
                    DeviceFailedEnumeration = 3
                    DeviceGeneralFailure = 4
                    DeviceCausedOvercurrent = 5
                    DeviceNotEnoughPower = 6
                    DeviceNotEnoughBandwidth = 7


                USB_CONNECTION_STATUS = _USB_CONNECTION_STATUS
                PUSB_CONNECTION_STATUS = POINTER(_USB_CONNECTION_STATUS)
            # END IF
            # IOCTL_USB_GET_NODE_CONNECTION_INFORMATION
            _USB_NODE_CONNECTION_INFORMATION._fields_ = [
                ('ConnectionIndex', ULONG), # INPUT
                ('DeviceDescriptor', USB_DEVICE_DESCRIPTOR), # OUTPUT
                ('CurrentConfigurationValue', UCHAR), # OUTPUT
                ('LowSpeed', BOOLEAN), # OUTPUT
                ('DeviceIsHub', BOOLEAN), # OUTPUT
                ('DeviceAddress', USHORT), # OUTPUT
                ('NumberOfOpenPipes', ULONG), # OUTPUT
                ('ConnectionStatus', USB_CONNECTION_STATUS), # OUTPUT
                ('PipeList', USB_PIPE_INFO * 0), # OUTPUT
            ]

            # IOCTL_USB_GET_NODE_CONNECTION_DRIVERKEY_NAME
            _USB_NODE_CONNECTION_DRIVERKEY_NAME._fields_ = [
                ('ConnectionIndex', ULONG), # INPUT
                ('ActualLength', ULONG), # OUTPUT
                ('DriverKeyName', WCHAR * 1), # OUTPUT
            ]

            # IOCTL_USB_GET_NODE_CONNECTION_NAME
            _USB_NODE_CONNECTION_NAME._fields_ = [
                ('ConnectionIndex', ULONG), # INPUT
                ('ActualLength', ULONG), # OUTPUT
                ('NodeName', WCHAR * 1), # OUTPUT
            ]
            _USB_HUB_NAME._fields_ = [
                ('ActualLength', ULONG), # OUTPUT
                ('HubName', WCHAR * 1), # OUTPUT
            ]
            _USB_ROOT_HUB_NAME._fields_ = [
                ('ActualLength', ULONG), # OUTPUT
                ('RootHubName', WCHAR * 1), # OUTPUT
            ]
            _USB_HCD_DRIVERKEY_NAME._fields_ = [
                ('ActualLength', ULONG), # OUTPUT
                ('DriverKeyName', WCHAR * 1), # OUTPUT
            ]


            class SetupPacket(ctypes.Structure):
                pass


            SetupPacket._fields_ = [
                ('bmRequest', UCHAR),
                ('bRequest', UCHAR),
                ('wValue', USHORT),
                ('wIndex', USHORT),
                ('wLength', USHORT),
            ]
            _USB_DESCRIPTOR_REQUEST.SetupPacket = SetupPacket

            _USB_DESCRIPTOR_REQUEST._fields_ = [
                ('ConnectionIndex', ULONG),
                ('SetupPacket', _USB_DESCRIPTOR_REQUEST.SetupPacket),
                ('Data', UCHAR * 0),
            ]

            # Structures defined for Windows XP and later only
            if _WIN32_WINNT >= 0x0501:
                _USB_HUB_CAPABILITIES._fields_ = [

                    # Unlike the USB_HUB_INFORMATION structure used by
                    # IOCTL_USB_GET_NODE_INFORMATION, this structure can be
                    # extended in the future to accomodate more data. The
                    # IOCTL will return only as much data as indicated by the
                    # size of the request buffer, to maintain backward
                    # compatibility with older callers that don't know about
                    # the new data.
                    ('HubIs2xCapable', ULONG, 1),
                ]

                # IOCTL_USB_GET_NODE_CONNECTION_ATTRIBUTES
                _USB_NODE_CONNECTION_ATTRIBUTES._fields_ = [
                    ('ConnectionIndex', ULONG), # INPUT
                    ('ConnectionStatus', USB_CONNECTION_STATUS), # OUTPUT
                    ('PortAttributes', ULONG), # OUTPUT
                ]

                # IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX
                _USB_NODE_CONNECTION_INFORMATION_EX._fields_ = [
                    ('ConnectionIndex', ULONG), # INPUT
                    ('DeviceDescriptor', USB_DEVICE_DESCRIPTOR), # OUTPUT
                    ('CurrentConfigurationValue', UCHAR), # OUTPUT
                    ('Speed', UCHAR), # OUTPUT
                    ('DeviceIsHub', BOOLEAN), # OUTPUT
                    ('DeviceAddress', USHORT), # OUTPUT
                    ('NumberOfOpenPipes', ULONG), # OUTPUT
                    ('ConnectionStatus', USB_CONNECTION_STATUS), # OUTPUT
                    ('PipeList', USB_PIPE_INFO * 0), # OUTPUT
                ]
            # END IF
            # Structures defined for windows Longhorn and later only
            if _WIN32_WINNT >= 0x0600:
                class _Struct_1(ctypes.Structure):
                    pass


                _Struct_1._fields_ = [
                    ('HubIsHighSpeedCapable', ULONG, 1),
                    ('HubIsHighSpeed', ULONG, 1),
                    ('HubIsMultiTtCapable', ULONG, 1),
                    ('HubIsMultiTt', ULONG, 1),
                    ('HubIsRoot', ULONG, 1),
                    ('HubIsArmedWakeOnConnect', ULONG, 1),
                    ('HubIsBusPowered', ULONG, 1),
                    ('ReservedMBZ', ULONG, 25),
                ]
                _USB_HUB_CAP_FLAGS._Struct_1 = _Struct_1

                _USB_HUB_CAP_FLAGS._anonymous_ = (
                    '_Struct_1',
                )
                _USB_HUB_CAP_FLAGS._fields_ = [
                    ('ul', ULONG),
                    ('_Struct_1', _USB_HUB_CAP_FLAGS._Struct_1),
                ]
                _USB_HUB_CAPABILITIES_EX._fields_ = [
                    ('CapabilityFlags', USB_HUB_CAP_FLAGS),
                ]
                _USB_CYCLE_PORT_PARAMS._fields_ = [
                    ('ConnectionIndex', ULONG), # INPUT
                    ('StatusReturned', ULONG), # OUTPUT
                ]

                # ***********************************************************
                # *********** Structures used for
                # IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO *****************
                # ******************************************************
                #
                # structure for storing PnP ids the length includes any
                # trailing NULLs
                _USB_ID_STRING._fields_ = [
                    ('LanguageId', USHORT), # laguage id where apllicable
                    ('Pad', USHORT),
                    ('LengthInBytes', ULONG), # length of <Buffer> in Bytes includes NULLs etc
                    ('Buffer', PWCHAR),
                ]
                _USB_HUB_DEVICE_UXD_SETTINGS._fields_ = [
                    ('Version', ULONG),
                    ('PnpGuid', GUID),
                    ('OwnerGuid', GUID),
                    ('DeleteOnShutdown', ULONG),
                    ('DeleteOnReload', ULONG),
                    ('DeleteOnDisconnect', ULONG),
                    ('Reserved', ULONG * 5),
                ]
                _HUB_DEVICE_CONFIG_INFO_V1._fields_ = [
                    ('Version', ULONG),
                    ('Length', ULONG),
                    ('HubFlags', USB_HUB_CAP_FLAGS),
                    ('HardwareIds', USB_ID_STRING),
                    ('CompatibleIds', USB_ID_STRING),
                    ('DeviceDescription', USB_ID_STRING),
                    ('Reserved', ULONG * 19),
                    ('UxdSettings', USB_HUB_DEVICE_UXD_SETTINGS),
                ]
            # END IF
            # Structure for returning HCD debug and statistic information to a
            # user mode application.
            _HCD_STAT_COUNTERS._fields_ = [
                ('BytesTransferred', ULONG),
                ('IsoMissedCount', USHORT),
                ('DataOverrunErrorCount', USHORT),
                ('CrcErrorCount', USHORT),
                ('ScheduleOverrunCount', USHORT),
                ('TimeoutErrorCount', USHORT),
                ('InternalHcErrorCount', USHORT),
                ('BufferOverrunErrorCount', USHORT),
                ('SWErrorCount', USHORT),
                ('StallPidCount', USHORT),
                ('PortDisableCount', USHORT),
            ]
            _HCD_ISO_STAT_COUNTERS._fields_ = [
                ('LateUrbs', USHORT),
                ('DoubleBufferedPackets', USHORT),
                ('TransfersCF_5ms', USHORT),
                ('TransfersCF_2ms', USHORT),
                ('TransfersCF_1ms', USHORT),
                ('MaxInterruptLatency', USHORT),
                ('BadStartFrame', USHORT),
                ('StaleUrbs', USHORT),

                # total count of packets programmed but not accessed by the
                # controller either due to software scheduling problems or HW
                # problems
                ('IsoPacketNotAccesed', USHORT),
                ('IsoPacketHWError', USHORT),
                ('SmallestUrbPacketCount', USHORT),
                ('LargestUrbPacketCount', USHORT),
                ('IsoCRC_Error', USHORT),
                ('IsoOVERRUN_Error', USHORT),
                ('IsoINTERNAL_Error', USHORT),
                ('IsoUNKNOWN_Error', USHORT),
                ('IsoBytesTransferred', ULONG),
                ('LateMissedCount', USHORT), # count of packets missed due to software scheduling problems
                # incremented when a packet is scheduled but not accessed by
                # the controller
                ('HWIsoMissedCount', USHORT),
                ('Reserved7', ULONG * 8),
            ]
            _HCD_STAT_INFORMATION_1._fields_ = [
                ('Reserved1', ULONG),
                ('Reserved2', ULONG),
                ('ResetCounters', ULONG),
                ('TimeRead', LARGE_INTEGER),
                ('Counters', HCD_STAT_COUNTERS), # stat registers
            ]
            _HCD_STAT_INFORMATION_2._fields_ = [
                ('Reserved1', ULONG),
                ('Reserved2', ULONG),
                ('ResetCounters', ULONG),
                ('TimeRead', LARGE_INTEGER),
                ('LockedMemoryUsed', LONG),
                ('Counters', HCD_STAT_COUNTERS), # stat registers
                ('IsoCounters', HCD_ISO_STAT_COUNTERS),
            ]

            # WMI related structures
            # these index in to our array of guids for the hub FDO
            WMI_USB_DRIVER_INFORMATION = 0
            WMI_USB_DRIVER_NOTIFICATION = 1
            WMI_USB_POWER_DEVICE_ENABLE = 2
            WMI_USB_HUB_NODE_INFORMATION = 4

            # Index into array of guids for the HUB pdos
            WMI_USB_PERFORMANCE_INFORMATION = 1
            WMI_USB_DEVICE_NODE_INFORMATION = 2

            if _WIN32_WINNT >= 0x0501:
                # Windows XP and later
                class _USB_NOTIFICATION_TYPE(ENUM):

                    # the following return a USB_CONNECTION_NOTIFICATION
                    # structure:
                    EnumerationFailure = 0
                    InsufficentBandwidth = 1
                    InsufficentPower = 2
                    OverCurrent = 3
                    ResetOvercurrent = 4

                    # the following return a USB_BUS_NOTIFICATION structure:
                    AcquireBusInfo = 5

                    # the following return a USB_ACQUIRE_INFO structure:
                    AcquireHubName = 6
                    AcquireControllerName = 7

                    # the following return a USB_HUB_NOTIFICATION structure:
                    HubOvercurrent = 8
                    HubPowerChange = 9
                    HubNestedTooDeeply = 10
                    ModernDeviceInLegacyHub = 11


                USB_NOTIFICATION_TYPE = _USB_NOTIFICATION_TYPE
            else:
                # For Windows 2000
                class _USB_NOTIFICATION_TYPE(ENUM):

                    # the following return a USB_CONNECTION_NOTIFICATION
                    # structure:
                    EnumerationFailure = 0
                    InsufficentBandwidth = 1
                    InsufficentPower = 2
                    OverCurrent = 3
                    ResetOvercurrent = 4

                    # the following return a USB_BUS_NOTIFICATION structure:
                    AcquireBusInfo = 5

                    # the following return a USB_ACQUIRE_INFO structure:
                    AcquireHubName = 6
                    AcquireControllerName = 7

                    # the following return a USB_HUB_NOTIFICATION structure:
                    HubOvercurrent = 8
                    HubPowerChange = 9


                USB_NOTIFICATION_TYPE = _USB_NOTIFICATION_TYPE
            # END IF

            _USB_NOTIFICATION._fields_ = [
                ('NotificationType', USB_NOTIFICATION_TYPE), # indicates type of notification
            ]

            # this structure is used for connection notification codes
            _USB_CONNECTION_NOTIFICATION._fields_ = [
                ('NotificationType', USB_NOTIFICATION_TYPE), # indicates type of notification

                # valid for all connection notifictaion codes, 0 indicates
                # global condition for hub or parent this value will be a port
                # number for devices attached to a hub, otherwise a one based
                # index if the device is a child of a composite parent
                ('ConnectionNumber', ULONG),

                # valid for InsufficentBandwidth, the amount of bandwidth the
                # device tried to allocate and was denied.
                ('RequestedBandwidth', ULONG),

                # valid for EnumerationFailure, gives some indication why the
                # device failed to enumerate
                ('EnumerationFailReason', ULONG),

                # valid for InsufficentPower, the amount of power requested to
                # configure this device.
                ('PowerRequested', ULONG),

                # length of the UNICODE symbolic name (in bytes) for the HUB
                # that this device is attached to. not including NULL
                ('HubNameLength', ULONG),
            ]

            # This structure is used for the bus notification code
            # 'AcquireBusInfo'
            _USB_BUS_NOTIFICATION._fields_ = [
                ('NotificationType', USB_NOTIFICATION_TYPE), # indicates type of
                ('TotalBandwidth', ULONG), # notification
                ('ConsumedBandwidth', ULONG),

                # length of the UNICODE symbolic name (in bytes) for the
                # controller that this device is attached to. not including
                # NULL
                ('ControllerNameLength', ULONG),
            ]

            # used to acquire user mode filenames to open respective objects
            _USB_ACQUIRE_INFO._fields_ = [
                ('NotificationType', USB_NOTIFICATION_TYPE), # indicates type of notification
                ('TotalSize', ULONG), # TotalSize of this struct
                ('Buffer', WCHAR * 1),
            ]

            # Structures defined for windows Longhorn and later only
            if _WIN32_WINNT >= 0x0600:
                # structures used to acquire device specific info via
                # GUID_USB_WMI_NODE_INFO
                USB_NODE_INFO_SIG = 'USBN'


                class _USB_WMI_DEVICE_NODE_TYPE(ENUM):
                    UsbDevice = 1
                    HubDevice = 2
                    CompositeDevice = 3
                    UsbController = 4


                USB_WMI_DEVICE_NODE_TYPE = _USB_WMI_DEVICE_NODE_TYPE
                PUSB_WMI_DEVICE_NODE_TYPE = POINTER(_USB_WMI_DEVICE_NODE_TYPE)
                _USB_DEVICE_STATE._fields_ = [
                    ('DeviceConnected', ULONG, 1),
                    ('DeviceStarted', ULONG, 1),
                ]

                # Specific information about a hub device
                _USB_HUB_PORT_INFORMATION._fields_ = [
                    ('DeviceState', USB_DEVICE_STATE),
                    ('PortNumber', USHORT),
                    ('DeviceAddress', USHORT),
                    ('ConnectionIndex', ULONG), # Legacy ConnectionIndex used with USB user IOCTLS
                    ('ConnectionStatus', USB_CONNECTION_STATUS), # Legacy ConnectionStatus
                ]
                _USB_HUB_DEVICE_INFO._fields_ = [
                    ('HubDescriptor', USB_HUB_DESCRIPTOR), # Hub Descriptor
                    ('HubNumber', ULONG), # Unique Hub number
                    ('DeviceAddress', USHORT), # Device Address
                    ('HubIsSelfPowered', BOOLEAN), # Hub power bit
                    ('HubIsRootHub', BOOLEAN), # Root hub
                    ('HubCapabilities', USB_HUB_CAPABILITIES), # Hub capabilities
                    ('NumberOfHubPorts', ULONG), # Number of hub ports
                    ('PortInfo', USB_HUB_PORT_INFORMATION * 1), # Variable length array of info about hub ports
                ]

                # Specific info about a composite device
                _USB_COMPOSITE_FUNCTION_INFO._fields_ = [
                    ('FunctionNumber', UCHAR),
                    ('BaseInterfaceNumber', UCHAR),
                    ('NumberOfInterfaces', UCHAR),
                    ('FunctionIsIdle', BOOLEAN),
                ]
                _USB_COMPOSITE_DEVICE_INFO._fields_ = [
                    ('DeviceDescriptor', USB_DEVICE_DESCRIPTOR), # USB Device Descriptor
                    ('CurrentConfigDescriptor', USB_CONFIGURATION_DESCRIPTOR), # Usb Configuration Descriptor
                    ('CurrentConfigurationValue', UCHAR), # 0 - based configuration number
                    ('NumberOfFunctions', UCHAR), # Number of composite PDOs
                    ('FunctionInfo', USB_COMPOSITE_FUNCTION_INFO * 1),
                ]

                # Specific info about a USB controller
                _USB_CONTROLLER_DEVICE_INFO._fields_ = [
                    ('PciVendorId', ULONG),
                    ('PciDeviceId', ULONG),
                    ('PciRevision', ULONG),
                    ('NumberOfRootPorts', ULONG),
                    ('HcFeatureFlags', ULONG),
                ]

                # Specific info about a connected USB device
                _USB_DEVICE_INFO._fields_ = [
                    ('DeviceState', USB_DEVICE_STATE), # Device State
                    ('PortNumber', USHORT), # Hub Port Number
                    ('DeviceDescriptor', USB_DEVICE_DESCRIPTOR), # USB Device Descriptor
                    ('CurrentConfigurationValue', UCHAR), # Current configuration value
                    ('Speed', USB_DEVICE_SPEED), # Device speed
                    ('DeviceAddress', USHORT), # Device Address
                    ('ConnectionIndex', ULONG), # Legacy ConnectionIndex used with USB user IOCTLS
                    ('ConnectionStatus', USB_CONNECTION_STATUS), # Legacy ConnectionStatus
                    ('PnpHardwareId', WCHAR * 128), # PNP HardwareID in multi - string format
                    ('PnpCompatibleId', WCHAR * 128), # PNP Compatible ID in multi - string format
                    ('SerialNumberId', WCHAR * 128), # USB Serial Number string if present
                    ('PnpDeviceDescription', WCHAR * 128), # PNP Device Description
                    ('NumberOfOpenPipes', ULONG), # Number of pipes contained in the PipeList
                    ('PipeList', USB_PIPE_INFO * 1), # Variable length list of open pipes
                ]


                class _Union_1(ctypes.Union):
                    pass


                _Union_1._fields_ = [
                    ('UsbDeviceInfo', USB_DEVICE_INFO),
                    ('HubDeviceInfo', USB_HUB_DEVICE_INFO),
                    ('CompositeDeviceInfo', USB_COMPOSITE_DEVICE_INFO),
                    ('ControllerDeviceInfo', USB_CONTROLLER_DEVICE_INFO),
                    ('DeviceInformation', UCHAR * 4),
                ]
                _USB_DEVICE_NODE_INFO._Union_1 = _Union_1

                _USB_DEVICE_NODE_INFO._anonymous_ = (
                    '_Union_1',
                )
                _USB_DEVICE_NODE_INFO._fields_ = [
                    ('Sig', ULONG), # Structure signature
                    ('LengthInBytes', ULONG), # Length of structure
                    ('DeviceDescription', WCHAR * 40), # Device Description
                    ('NodeType', USB_WMI_DEVICE_NODE_TYPE), # Device Type
                    ('BusAddress', USB_TOPOLOGY_ADDRESS), # Bus Address
                    ('_Union_1', _USB_DEVICE_NODE_INFO._Union_1), # device information
                ]

                # structures used to acquire device specific performance info
                # GUID_USB_WMI_DEVICE_PERF_INFO
                _USB_DEVICE_PERFORMANCE_INFO._fields_ = [
                    ('BulkBytes', ULONG), # total bulk bytes transfered for this device
                    ('ControlDataBytes', ULONG), # total control bytes transfered for this device
                    ('IsoBytes', ULONG), # total iso bytes transfered for this device
                    ('InterruptBytes', ULONG), # total interrupt bytes transfered for this device
                    ('BulkUrbCount', ULONG), # Total number of transfer URBs processed for this device
                    ('ControlUrbCount', ULONG),
                    ('IsoUrbCount', ULONG),
                    ('InterruptUrbCount', ULONG),
                    ('AllocedInterrupt', ULONG * 6), # for all periods
                    ('AllocedIso', ULONG), # Reported in bits/32ms(32 frames)
                    ('Total32secBandwidth', ULONG), # Total USB controller BW available in bits/32ms.
                    ('TotalTtBandwidth', ULONG), # Total USB BW available on the device's TT in bits/32ms
                    ('DeviceDescription', WCHAR * 60), # Text description of the device
                    ('DeviceSpeed', USB_DEVICE_SPEED), # operating speed of the device

                    # total number of ms iso transfers have waited after being
                    # scheduled
                    ('TotalIsoLatency', ULONG),

                    # Number of ISO packets that were not scheduled or
                    # processed by the controller
                    ('DroppedIsoPackets', ULONG),
                    ('TransferErrors', ULONG), # Number of transfers completing with an error
                    ('PciInterruptCount', ULONG), # Number of controller interrupts
                    ('HcIdleState', ULONG), # HC Idle State - - non zero if the HC is not running

                    # Async (EHCI) Idle State - - non zero if the async
                    # segment is off
                    ('HcAsyncIdleState', ULONG),

                    # Async (EHCI) Cache stats - - incremented each time we
                    # flush the async cache (doorbell).
                    ('HcAsyncCacheFlushCount', ULONG),

                    # Periodic (EHCI) Idle State - - non zero if the periodic
                    # segment is off
                    ('HcPeriodicIdleState', ULONG),

                    # Periodic (EHCI) Cache stats - - incremented each time we
                    # flush the periodic prefetch cache.
                    ('HcPeriodicCacheFlushCount', ULONG),
                ]
            # END IF

            # Structures defined for Windows 8 and later only
            if NTDDI_VERSION >= NTDDI_WIN8:
                class _USB_HUB_TYPE(ENUM):
                    UsbRootHub = 1
                    Usb20Hub = 2
                    Usb30Hub = 3


                USB_HUB_TYPE = _USB_HUB_TYPE


                class u(ctypes.Union):
                    pass


                u._fields_ = [
                    ('UsbHubDescriptor', USB_HUB_DESCRIPTOR),
                    ('Usb30HubDescriptor', USB_30_HUB_DESCRIPTOR),
                ]
                _USB_HUB_INFORMATION_EX.u = u

                _USB_HUB_INFORMATION_EX._fields_ = [
                    ('HubType', USB_HUB_TYPE),
                    ('HighestPortNumber', USHORT), # The higest valid port number on the hub
                    ('u', _USB_HUB_INFORMATION_EX.u),
                ]


                class _Struct_2(ctypes.Structure):
                    pass


                _Struct_2._fields_ = [
                    ('PortIsUserConnectable', ULONG, 1),
                    ('PortIsDebugCapable', ULONG, 1),
                    ('PortHasMultipleCompanions', ULONG, 1),
                    ('PortConnectorIsTypeC', ULONG, 1),
                    ('ReservedMBZ', ULONG, 28),
                ]
                _USB_PORT_PROPERTIES._Struct_2 = _Struct_2

                _USB_PORT_PROPERTIES._anonymous_ = (
                    '_Struct_2',
                )
                _USB_PORT_PROPERTIES._fields_ = [
                    ('ul', ULONG),
                    ('_Struct_2', _USB_PORT_PROPERTIES._Struct_2),
                ]
                _USB_PORT_CONNECTOR_PROPERTIES._fields_ = [
                    ('ConnectionIndex', ULONG), # one based port number

                    # structure, including the full
                    # CompanionHubSymbolicLinkName string
                    ('ActualLength', ULONG),

                    # bitmask of flags indicating properties and capabilities
                    # of the port
                    ('UsbPortProperties', USB_PORT_PROPERTIES),

                    # Zero based index number of the companion port being
                    # queried.
                    ('CompanionIndex', USHORT),
                    ('CompanionPortNumber', USHORT), # Port number of the companion port
                    ('CompanionHubSymbolicLinkName', WCHAR * 1), # Symbolic link name for the companion hub
                ]


                class _Struct_3(ctypes.Structure):
                    pass


                _Struct_3._fields_ = [
                    ('Usb110', ULONG, 1),
                    ('Usb200', ULONG, 1),
                    ('Usb300', ULONG, 1),
                    ('ReservedMBZ', ULONG, 29),
                ]
                _USB_PROTOCOLS._Struct_3 = _Struct_3

                _USB_PROTOCOLS._anonymous_ = (
                    '_Struct_3',
                )
                _USB_PROTOCOLS._fields_ = [
                    ('ul', ULONG),
                    ('_Struct_3', _USB_PROTOCOLS._Struct_3),
                ]


                class _Struct_4(ctypes.Structure):
                    pass


                _Struct_4._fields_ = [
                    ('DeviceIsOperatingAtSuperSpeedOrHigher', ULONG, 1),
                    ('DeviceIsSuperSpeedCapableOrHigher', ULONG, 1),
                    ('DeviceIsOperatingAtSuperSpeedPlusOrHigher', ULONG, 1),
                    ('DeviceIsSuperSpeedPlusCapableOrHigher', ULONG, 1),
                    ('ReservedMBZ', ULONG, 28),
                ]
                _USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS._Struct_4 = _Struct_4

                _USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS._anonymous_ = (
                    '_Struct_4',
                )
                _USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS._fields_ = [
                    ('ul', ULONG),
                    ('_Struct_4', _USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS._Struct_4),
                ]
                _USB_NODE_CONNECTION_INFORMATION_EX_V2._fields_ = [
                    ('ConnectionIndex', ULONG), # one based port number
                    ('Length', ULONG), # length of the structure

                    # On output a bitmask that indicates which USB signaling
                    # protocols are supported by the port
                    ('SupportedUsbProtocols', USB_PROTOCOLS),

                    # A bitmask indicating properties of the connected device
                    # or port
                    ('Flags', USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS),
                ]
            # END IF
        # END IF  #if USB_KERNEL_IOCTL

        if NTDDI_VERSION >= NTDDI_WIN10_RS3:
            USB_TRANSPORT_CHARACTERISTICS_VERSION_1 = 0x01
            USB_TRANSPORT_CHARACTERISTICS_LATENCY_AVAILABLE = 0x1
            USB_TRANSPORT_CHARACTERISTICS_BANDWIDTH_AVAILABLE = 0x2
            _USB_TRANSPORT_CHARACTERISTICS._fields_ = [
                ('Version', ULONG),
                ('TransportCharacteristicsFlags', ULONG),
                ('CurrentRoundtripLatencyInMilliSeconds', ULONG64),
                ('MaxPotentialBandwidth', ULONG64),
            ]
            USB_REGISTER_FOR_TRANSPORT_LATENCY_CHANGE = 0x1
            USB_REGISTER_FOR_TRANSPORT_BANDWIDTH_CHANGE = 0x2
            USB_CHANGE_REGISTRATION_HANDLE = DECLARE_HANDLE()
            _USB_TRANSPORT_CHARACTERISTICS_CHANGE_REGISTRATION._fields_ = [
                ('ChangeNotificationInputFlags', ULONG),
                ('Handle', USB_CHANGE_REGISTRATION_HANDLE),
                ('UsbTransportCharacteristics', USB_TRANSPORT_CHARACTERISTICS),
            ]
            _USB_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION._fields_ = [
                ('Handle', USB_CHANGE_REGISTRATION_HANDLE),
                ('UsbTransportCharacteristics', USB_TRANSPORT_CHARACTERISTICS),
            ]
            _USB_TRANSPORT_CHARACTERISTICS_CHANGE_UNREGISTRATION._fields_ = [
                ('Handle', USB_CHANGE_REGISTRATION_HANDLE),
            ]
            USB_DEVICE_CHARACTERISTICS_VERSION_1 = 0x01
            USB_DEVICE_CHARACTERISTICS_MAXIMUM_PATH_DELAYS_AVAILABLE = 0x1
            _USB_DEVICE_CHARACTERISTICS._fields_ = [
                ('Version', ULONG),
                ('Reserved', ULONG * 2),
                ('UsbDeviceCharacteristicsFlags', ULONG),
                ('MaximumSendPathDelayInMilliSeconds', ULONG),
                ('MaximumCompletionPathDelayInMilliSeconds', ULONG),
            ]

            __USB_TIME_SYNC_DEFINED = None
            if not defined(__USB_TIME_SYNC_DEFINED):
                __USB_TIME_SYNC_DEFINED = 1
                _USB_START_TRACKING_FOR_TIME_SYNC_INFORMATION._fields_ = [
                    ('TimeTrackingHandle', HANDLE),
                    ('IsStartupDelayTolerable', BOOLEAN),
                ]
                _USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION._fields_ = [
                    ('TimeTrackingHandle', HANDLE),
                ]
                _USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION._fields_ = [
                    ('TimeTrackingHandle', HANDLE), # Input
                    ('InputFrameNumber', ULONG),
                    ('InputMicroFrameNumber', ULONG),
                    ('QueryPerformanceCounterAtInputFrameOrMicroFrame', LARGE_INTEGER), # Output
                    ('QueryPerformanceCounterFrequency', LARGE_INTEGER),
                    ('PredictedAccuracyInMicroSeconds', ULONG),
                    ('CurrentGenerationID', ULONG),
                    ('CurrentQueryPerformanceCounter', LARGE_INTEGER),
                    ('CurrentHardwareFrameNumber', ULONG), # 11 bits from hardware/MFINDEX
                    ('CurrentHardwareMicroFrameNumber', ULONG), # 3 bits from hardware/MFINDEX
                    ('CurrentUSBFrameNumber', ULONG), # 32 bit USB Frame Number
                ]
            # END IF
        # END IF
        if _MSC_VER >= 1200:
            pass
        else:
            pass
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF  __USBIOCTL_H__
