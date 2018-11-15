import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.guiddef_h import *


class _USB_IDLE_CALLBACK_INFO(ctypes.Structure):
    pass


USB_IDLE_CALLBACK_INFO = _USB_IDLE_CALLBACK_INFO
PUSB_IDLE_CALLBACK_INFO = POINTER(_USB_IDLE_CALLBACK_INFO)


# + + Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# USBIODEF.H Abstract: Common header file for all USB IOCTLs defined for the
# core stack. We define them in this single header file so that we can
# maintain backward compatibilty with older versions of the stack. We divide
# the IOCTLS supported by the stack as follows: kernel IOCTLS: user IOCTLS:
# IOCTLS Handled by HCD (PORT) FDO IOCTLS Handled by HUB FDO IOCTLS Handled by
# USB (DEVICE) PDO Environment: kernel & user mode Revision History: - -
__USBIODEF_H__ = None
if not defined(__USBIODEF_H__):
    __USBIODEF_H__ = 1
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    # Function codes for kernel mode IOCTLs with DeviceType :
    # DEVICE_TYPE_USB (a.k.a DEVICE_TYPE_UNKNOWN) The following codes are
    # valid only if passed as in the icControlCode parameter for
    # IRP_MJ_INTERNAL_DEVICE_CONTROL
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        USB_SUBMIT_URB = 0
        USB_RESET_PORT = 1
        USB_GET_ROOTHUB_PDO = 3
        USB_GET_PORT_STATUS = 4
        USB_ENABLE_PORT = 5
        USB_GET_HUB_COUNT = 6
        USB_CYCLE_PORT = 7
        USB_GET_HUB_NAME = 8
        USB_IDLE_NOTIFICATION = 9
        USB_RECORD_FAILURE = 10
        USB_GET_BUS_INFO = 264
        USB_GET_CONTROLLER_NAME = 265
        USB_GET_BUSGUID_INFO = 266
        USB_GET_PARENT_HUB_INFO = 267
        USB_GET_DEVICE_HANDLE = 268
        USB_GET_DEVICE_HANDLE_EX = 269
        USB_GET_TT_DEVICE_HANDLE = 270
        USB_GET_TOPOLOGY_ADDRESS = 271
        USB_IDLE_NOTIFICATION_EX = 272
        USB_REQ_GLOBAL_SUSPEND = 273
        USB_REQ_GLOBAL_RESUME = 274
        USB_GET_HUB_CONFIG_INFO = 275
        USB_FAIL_GET_STATUS = 280

        # Function codes for kernel mode IOCTLs with DeviceType :
        # DEVICE_TYPE_USBEX The following codes are valid only if passed as in
        # the icControlCode parameter for IRP_MJ_INTERNAL_DEVICE_CONTROL The
        # range 0 - 2047 is reserved for use by Microsoft. The range 0 - 1023
        # is used for Public Ioctls defined by Microsoft.
        USB_REGISTER_COMPOSITE_DEVICE = 0
        USB_UNREGISTER_COMPOSITE_DEVICE = 1
        USB_REQUEST_REMOTE_WAKE_NOTIFICATION = 2

        # Function codes for user mode IOCTLs The following codes are valid
        # only if passed as in the icControlCode parameter for
        # IRP_MJ_DEVICE_CONTROL hence, they are callable by user mode
        # applications
        HCD_GET_STATS_1 = 255
        HCD_DIAGNOSTIC_MODE_ON = 256
        HCD_DIAGNOSTIC_MODE_OFF = 257
        HCD_GET_ROOT_HUB_NAME = 258
        HCD_GET_DRIVERKEY_NAME = 265
        HCD_GET_STATS_2 = 266
        HCD_DISABLE_PORT = 268
        HCD_ENABLE_PORT = 269
        HCD_USER_REQUEST = 270
        HCD_TRACE_READ_REQUEST = 275
        USB_GET_NODE_INFORMATION = 258
        USB_GET_NODE_CONNECTION_INFORMATION = 259
        USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION = 260
        USB_GET_NODE_CONNECTION_NAME = 261
        USB_DIAG_IGNORE_HUBS_ON = 262
        USB_DIAG_IGNORE_HUBS_OFF = 263
        USB_GET_NODE_CONNECTION_DRIVERKEY_NAME = 264
        USB_GET_HUB_CAPABILITIES = 271
        USB_GET_NODE_CONNECTION_ATTRIBUTES = 272
        USB_HUB_CYCLE_PORT = 273
        USB_GET_NODE_CONNECTION_INFORMATION_EX = 274
        USB_RESET_HUB = 275
        USB_GET_HUB_CAPABILITIES_EX = 276
        USB_GET_HUB_INFORMATION_EX = 277
        USB_GET_PORT_CONNECTOR_PROPERTIES = 278
        USB_GET_NODE_CONNECTION_INFORMATION_EX_V2 = 279
        USB_GET_TRANSPORT_CHARACTERISTICS = 281
        USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE = 282
        USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE = 283
        USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE = 284
        USB_START_TRACKING_FOR_TIME_SYNC = 285
        USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC = 286
        USB_STOP_TRACKING_FOR_TIME_SYNC = 287
        USB_GET_DEVICE_CHARACTERISTICS = 288

        # USB specific GUIDs
        # f18a0e88 - c30c - 11d0 - 8815 - 00a0c906bed8
        GUID_DEVINTERFACE_USB_HUB = DEFINE_GUID(
            0xF18A0E88,
            0xC30C,
            0x11D0,
            0x88,
            0x15,
            0x00,
            0xA0,
            0xC9,
            0x06,
            0xBE,
            0xD8
        )

        # 5e9adaef - f879 - 473f - b807 - 4e5ea77d1b1c
        GUID_DEVINTERFACE_USB_BILLBOARD = DEFINE_GUID(
            0x5E9ADAEF,
            0xF879,
            0x473F,
            0xB8,
            0x07,
            0x4E,
            0x5E,
            0xA7,
            0x7D,
            0x1B,
            0x1C
        )

        # A5DCBF10 - 6530 - 11D2 - 901F - 00C04FB951ED
        GUID_DEVINTERFACE_USB_DEVICE = DEFINE_GUID(
            0xA5DCBF10,
            0x6530,
            0x11D2,
            0x90,
            0x1F,
            0x00,
            0xC0,
            0x4F,
            0xB9,
            0x51,
            0xED
        )

        # 3ABF6F2D - 71C4 - 462a - 8A92 - 1E6861E6AF27
        GUID_DEVINTERFACE_USB_HOST_CONTROLLER = DEFINE_GUID(
            0x3ABF6F2D,
            0x71C4,
            0x462A,
            0x8A,
            0x92,
            0x1E,
            0x68,
            0x61,
            0xE6,
            0xAF,
            0x27
        )

        # 4E623B20 - CB14 - 11D1 - B331 - 00A0C959BBD2
        GUID_USB_WMI_STD_DATA = DEFINE_GUID(
            0x4E623B20,
            0xCB14,
            0x11D1,
            0xB3,
            0x31,
            0x00,
            0xA0,
            0xC9,
            0x59,
            0xBB,
            0xD2
        )

        # 4E623B20 - CB14 - 11D1 - B331 - 00A0C959BBD2
        GUID_USB_WMI_STD_NOTIFICATION = DEFINE_GUID(
            0x4E623B20,
            0xCB14,
            0x11D1,
            0xB3,
            0x31,
            0x00,
            0xA0,
            0xC9,
            0x59,
            0xBB,
            0xD2
        )

        # For windows LONGhorn and later
        if _WIN32_WINNT >= 0x0600:
            # 66C1AA3C - 499F - 49a0 - A9A5 - 61E2359F6407
            GUID_USB_WMI_DEVICE_PERF_INFO = DEFINE_GUID(
                0x66C1AA3C,
                0x499F,
                0x49A0,
                0xA9,
                0xA5,
                0x61,
                0xE2,
                0x35,
                0x9F,
                0x64,
                0x7
            )

            # {9C179357 - DC7A - 4f41 - B66B - 323B9DDCB5B1}
            GUID_USB_WMI_NODE_INFO = DEFINE_GUID(
                0x9C179357,
                0xDC7A,
                0x4F41,
                0xB6,
                0x6B,
                0x32,
                0x3B,
                0x9D,
                0xDC,
                0xB5,
                0xB1
            )

            # 3a61881b - b4e6 - 4bf9 - ae0f - 3cd8f394e52f
            GUID_USB_WMI_TRACING = DEFINE_GUID(
                0x3A61881B,
                0xB4E6,
                0x4BF9,
                0xAE,
                0xF,
                0x3C,
                0xD8,
                0xF3,
                0x94,
                0xE5,
                0x2F
            )

            # {681EB8AA - 403D - 452c - 9F8A - F0616FAC9540}
            GUID_USB_TRANSFER_TRACING = DEFINE_GUID(
                0x681EB8AA,
                0x403D,
                0x452C,
                0x9F,
                0x8A,
                0xF0,
                0x61,
                0x6F,
                0xAC,
                0x95,
                0x40
            )

            # {D5DE77A6 - 6AE9 - 425c - B1E2 - F5615FD348A9}
            GUID_USB_PERFORMANCE_TRACING = DEFINE_GUID(
                0xD5DE77A6,
                0x6AE9,
                0x425C,
                0xB1,
                0xE2,
                0xF5,
                0x61,
                0x5F,
                0xD3,
                0x48,
                0xA9
            )

            # {9BBBF831 - A2F2 - 43B4 - 96D1 - 86944B5914B3}
            GUID_USB_WMI_SURPRISE_REMOVAL_NOTIFICATION = DEFINE_GUID(
                0x9BBBF831,
                0xA2F2,
                0x43B4,
                0x96,
                0xD1,
                0x86,
                0x94,
                0x4B,
                0x59,
                0x14,
                0xB3
            )
        # END IF

        from pyWinAPI.shared.devioctl_h import *  # NOQA

        # Obsolete device interface class GUID names.
        # (use of above GUID_DEVINTERFACE_* names is recommended). - -
        GUID_CLASS_USBHUB = GUID_DEVINTERFACE_USB_HUB
        GUID_CLASS_USB_DEVICE = GUID_DEVINTERFACE_USB_DEVICE
        GUID_CLASS_USB_HOST_CONTROLLER = GUID_DEVINTERFACE_USB_HOST_CONTROLLER
        FILE_DEVICE_USB = FILE_DEVICE_UNKNOWN

        # common macro used by IOCTL header files
        def USB_CTL(id):
            return CTL_CODE(
                FILE_DEVICE_USB,
                id,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS
            )


        def USB_KERNEL_CTL(id):
            return CTL_CODE(
                FILE_DEVICE_USB,
                id,
                METHOD_NEITHER,
                FILE_ANY_ACCESS
            )


        def USB_KERNEL_CTL_BUFFERED(id):
            return CTL_CODE(
                FILE_DEVICE_USB,
                id,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS
            )

        # structures common to both usbioctl.h and usbdrivr.h
        # used by IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION. Available
        # on windows XP and later
        if _WIN32_WINNT >= 0x0501:

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # typedef
            # VOID
            # (*USB_IDLE_CALLBACK)(
            # _In_ PVOID Context
            # );

            USB_IDLE_CALLBACK = CALLBACK(VOID, PVOID)

            _USB_IDLE_CALLBACK_INFO._fields_ = [
                ('IdleCallback', USB_IDLE_CALLBACK),
                ('IdleContext', PVOID),
            ]
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF  __USBIODEF_H__
