import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__WUSB_H__ = None
__USB_TIME_SYNC_DEFINED = None

class _WINUSB_SETUP_PACKET(ctypes.Structure):
    pass


WINUSB_SETUP_PACKET = _WINUSB_SETUP_PACKET
PWINUSB_SETUP_PACKET = POINTER(_WINUSB_SETUP_PACKET)


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




# /* + + Copyright (c) 2002 Microsoft Corporation Module Name: wusb.h
# Abstract: Public interface to winusb.dll Environment: Kernel Mode Only
# Notes: THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
# KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# Copyright (c) 2001 Microsoft Corporation. All Rights Reserved. Revision
# History: 11/19/2002 : created Authors: --
if not defined(__WUSB_H__):
    __WUSB_H__ = VOID
    from winapifamily_h import * # NOQA
        if defined(__cplusplus):
            pass
        # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if NTDDI_VERSION >= NTDDI_WINXP:
            from winusbio_h import * # NOQA
            WINUSB_INTERFACE_HANDLE = PVOID
            PWINUSB_INTERFACE_HANDLE = POINTER(PVOID)
            WINUSB_ISOCH_BUFFER_HANDLE = PVOID
            PWINUSB_ISOCH_BUFFER_HANDLE = POINTER(PVOID)


            _WINUSB_SETUP_PACKET._fields_ = [
                ('RequestType', UCHAR),
                ('Request', UCHAR),
                ('Value', USHORT),
                ('Index', USHORT),
                ('Length', USHORT),
            ]
            winusb = ctypes.windll.WINUSB


            # BOOL __stdcall
            # WinUsb_Initialize(
            # _In_  HANDLE DeviceHandle,
            # _Out_ PWINUSB_INTERFACE_HANDLE InterfaceHandle
            # );
            WinUsb_Initialize = winusb.WinUsb_Initialize
            WinUsb_Initialize.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_Free(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle
            # );
            WinUsb_Free = winusb.WinUsb_Free
            WinUsb_Free.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_GetAssociatedInterface(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR AssociatedInterfaceIndex,
            # _Out_ PWINUSB_INTERFACE_HANDLE AssociatedInterfaceHandle
            # );
            WinUsb_GetAssociatedInterface = (
                winusb.WinUsb_GetAssociatedInterface
            )
            WinUsb_GetAssociatedInterface.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_GetDescriptor(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR DescriptorType,
            # _In_  UCHAR Index,
            # _In_  USHORT LanguageID,
            # _Out_writes_bytes_to_opt_(BufferLength, *LengthTransferred) PUCHAR Buffer,
            # _In_  ULONG BufferLength,
            # _Out_ PULONG LengthTransferred
            # );
            WinUsb_GetDescriptor = winusb.WinUsb_GetDescriptor
            WinUsb_GetDescriptor.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_QueryInterfaceSettings(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR AlternateInterfaceNumber,
            # _Out_ PUSB_INTERFACE_DESCRIPTOR UsbAltInterfaceDescriptor
            # );
            WinUsb_QueryInterfaceSettings = (
                winusb.WinUsb_QueryInterfaceSettings
            )
            WinUsb_QueryInterfaceSettings.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_QueryDeviceInformation(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  ULONG InformationType,
            # _Inout_ PULONG BufferLength,
            # _Out_writes_bytes_(*BufferLength) PVOID Buffer
            # );
            WinUsb_QueryDeviceInformation = (
                winusb.WinUsb_QueryDeviceInformation
            )
            WinUsb_QueryDeviceInformation.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_SetCurrentAlternateSetting(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR SettingNumber
            # );
            WinUsb_SetCurrentAlternateSetting = (
                winusb.WinUsb_SetCurrentAlternateSetting
            )
            WinUsb_SetCurrentAlternateSetting.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_GetCurrentAlternateSetting(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _Out_ PUCHAR SettingNumber
            # );
            WinUsb_GetCurrentAlternateSetting = (
                winusb.WinUsb_GetCurrentAlternateSetting
            )
            WinUsb_GetCurrentAlternateSetting.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_QueryPipe(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR AlternateInterfaceNumber,
            # _In_  UCHAR PipeIndex,
            # _Out_ PWINUSB_PIPE_INFORMATION PipeInformation
            # );
            WinUsb_QueryPipe = winusb.WinUsb_QueryPipe
            WinUsb_QueryPipe.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_SetPipePolicy(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR PipeID,
            # _In_  ULONG PolicyType,
            # _In_  ULONG ValueLength,
            # _In_reads_bytes_(ValueLength) PVOID Value
            # );
            WinUsb_SetPipePolicy = winusb.WinUsb_SetPipePolicy
            WinUsb_SetPipePolicy.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_GetPipePolicy(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR PipeID,
            # _In_  ULONG PolicyType,
            # _Inout_ PULONG ValueLength,
            # _Out_writes_bytes_(*ValueLength) PVOID Value
            # );
            WinUsb_GetPipePolicy = winusb.WinUsb_GetPipePolicy
            WinUsb_GetPipePolicy.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_ReadPipe(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR PipeID,
            # _Out_writes_bytes_to_opt_(BufferLength,*LengthTransferred) PUCHAR Buffer,
            # _In_  ULONG BufferLength,
            # _Out_opt_ PULONG LengthTransferred,
            # _In_opt_ LPOVERLAPPED Overlapped
            # );
            WinUsb_ReadPipe = winusb.WinUsb_ReadPipe
            WinUsb_ReadPipe.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_WritePipe(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR PipeID,
            # _In_reads_bytes_(BufferLength) PUCHAR Buffer,
            # _In_  ULONG BufferLength,
            # _Out_opt_ PULONG LengthTransferred,
            # _In_opt_ LPOVERLAPPED Overlapped
            # );
            WinUsb_WritePipe = winusb.WinUsb_WritePipe
            WinUsb_WritePipe.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_ControlTransfer(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  WINUSB_SETUP_PACKET SetupPacket,
            # _Out_writes_bytes_to_opt_(BufferLength, *LengthTransferred) PUCHAR Buffer,
            # _In_  ULONG BufferLength,
            # _Out_opt_ PULONG LengthTransferred,
            # _In_opt_  LPOVERLAPPED Overlapped
            # );
            WinUsb_ControlTransfer = winusb.WinUsb_ControlTransfer
            WinUsb_ControlTransfer.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_ResetPipe(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR PipeID
            # );
            WinUsb_ResetPipe = winusb.WinUsb_ResetPipe
            WinUsb_ResetPipe.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_AbortPipe(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR PipeID
            # );
            WinUsb_AbortPipe = winusb.WinUsb_AbortPipe
            WinUsb_AbortPipe.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_FlushPipe(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  UCHAR PipeID
            # );
            WinUsb_FlushPipe = winusb.WinUsb_FlushPipe
            WinUsb_FlushPipe.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_SetPowerPolicy(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  ULONG PolicyType,
            # _In_  ULONG ValueLength,
            # _In_reads_bytes_(ValueLength) PVOID Value
            # );
            WinUsb_SetPowerPolicy = winusb.WinUsb_SetPowerPolicy
            WinUsb_SetPowerPolicy.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_GetPowerPolicy(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  ULONG PolicyType,
            # _Inout_ PULONG ValueLength,
            # _Out_writes_bytes_(*ValueLength) PVOID Value
            # );
            WinUsb_GetPowerPolicy = winusb.WinUsb_GetPowerPolicy
            WinUsb_GetPowerPolicy.restype = __stdcall


            # BOOL __stdcall
            # WinUsb_GetOverlappedResult(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  LPOVERLAPPED lpOverlapped,
            # _Out_ LPDWORD lpNumberOfBytesTransferred,
            # _In_  BOOL bWait
            # );
            WinUsb_GetOverlappedResult = winusb.WinUsb_GetOverlappedResult
            WinUsb_GetOverlappedResult.restype = __stdcall


            # PUSB_INTERFACE_DESCRIPTOR __stdcall
            # WinUsb_ParseConfigurationDescriptor(
            # _In_  PUSB_CONFIGURATION_DESCRIPTOR ConfigurationDescriptor,
            # _In_  PVOID StartPosition,
            # _In_  LONG InterfaceNumber,
            # _In_  LONG AlternateSetting,
            # _In_  LONG InterfaceClass,
            # _In_  LONG InterfaceSubClass,
            # _In_  LONG InterfaceProtocol
            # );
            WinUsb_ParseConfigurationDescriptor = (
                winusb.WinUsb_ParseConfigurationDescriptor
            )
            WinUsb_ParseConfigurationDescriptor.restype = __stdcall


            # PUSB_COMMON_DESCRIPTOR __stdcall
            # WinUsb_ParseDescriptors(
            # _In_reads_bytes_(TotalLength) PVOID    DescriptorBuffer,
            # _In_  ULONG    TotalLength,
            # _In_  PVOID    StartPosition,
            # _In_  LONG     DescriptorType
            # );
            WinUsb_ParseDescriptors = winusb.WinUsb_ParseDescriptors
            WinUsb_ParseDescriptors.restype = __stdcall


            if not defined(__USB_TIME_SYNC_DEFINED):
                __USB_TIME_SYNC_DEFINED = VOID
                from pshpack1_h import * # NOQA


                _USB_START_TRACKING_FOR_TIME_SYNC_INFORMATION._fields_ = [
                    ('TimeTrackingHandle', HANDLE),
                    ('IsStartupDelayTolerable', BOOLEAN),
                ]

                _USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION._fields_ = [
                    ('TimeTrackingHandle', HANDLE),
                ]

                _USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION._fields_ = [
                    # Input
                    ('TimeTrackingHandle', HANDLE),
                    ('InputFrameNumber', ULONG),
                    ('InputMicroFrameNumber', ULONG),
                    # Output
                    ('QueryPerformanceCounterAtInputFrameOrMicroFrame', LARGE_INTEGER),
                    ('QueryPerformanceCounterFrequency', LARGE_INTEGER),
                    ('PredictedAccuracyInMicroSeconds', ULONG),
                    ('CurrentGenerationID', ULONG),
                    ('CurrentQueryPerformanceCounter', LARGE_INTEGER),
                    # 11 bits from hardware/MFINDEX
                    ('CurrentHardwareFrameNumber', ULONG),
                    # 3 bits from hardware/MFINDEX
                    ('CurrentHardwareMicroFrameNumber', ULONG),
                    # 32 bit USB Frame Number
                    ('CurrentUSBFrameNumber', ULONG),
                ]
                from poppack_h import * # NOQA
            # END IF


            winusb = ctypes.windll.WINUSB


            # BOOL __stdcall WinUsb_StartTrackingForTimeSync(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  PUSB_START_TRACKING_FOR_TIME_SYNC_INFORMATION StartTrackingInfo
            # );
            WinUsb_StartTrackingForTimeSync = (
                winusb.WinUsb_StartTrackingForTimeSync
            )
            WinUsb_StartTrackingForTimeSync.restype = __stdcall


            # BOOL __stdcall WinUsb_GetCurrentFrameNumberAndQpc(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  PUSB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION FrameQpcInfo
            # );
            WinUsb_GetCurrentFrameNumberAndQpc = (
                winusb.WinUsb_GetCurrentFrameNumberAndQpc
            )
            WinUsb_GetCurrentFrameNumberAndQpc.restype = __stdcall


            # BOOL __stdcall WinUsb_StopTrackingForTimeSync(
            # _In_  WINUSB_INTERFACE_HANDLE InterfaceHandle,
            # _In_  PUSB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION StopTrackingInfo
            # );
            WinUsb_StopTrackingForTimeSync = (
                winusb.WinUsb_StopTrackingForTimeSync
            )
            WinUsb_StopTrackingForTimeSync.restype = __stdcall

        # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF  __WUSB_H__


