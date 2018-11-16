import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *


class _BLUETOOTH_ADDRESS(ctypes.Structure):
    pass


BLUETOOTH_ADDRESS_STRUCT = _BLUETOOTH_ADDRESS


class _BLUETOOTH_LOCAL_SERVICE_INFO(ctypes.Structure):
    pass


BLUETOOTH_LOCAL_SERVICE_INFO_STRUCT = _BLUETOOTH_LOCAL_SERVICE_INFO


class _BLUETOOTH_FIND_RADIO_PARAMS(ctypes.Structure):
    pass


BLUETOOTH_FIND_RADIO_PARAMS = _BLUETOOTH_FIND_RADIO_PARAMS


class _BLUETOOTH_RADIO_INFO(ctypes.Structure):
    pass


BLUETOOTH_RADIO_INFO = _BLUETOOTH_RADIO_INFO
PBLUETOOTH_RADIO_INFO = POINTER(_BLUETOOTH_RADIO_INFO)


class _BLUETOOTH_DEVICE_INFO(ctypes.Structure):
    pass


BLUETOOTH_DEVICE_INFO_STRUCT = _BLUETOOTH_DEVICE_INFO


class _BLUETOOTH_AUTHENTICATION_CALLBACK_PARAMS(ctypes.Structure):
    pass


BLUETOOTH_AUTHENTICATION_CALLBACK_PARAMS = (
    _BLUETOOTH_AUTHENTICATION_CALLBACK_PARAMS
)
PBLUETOOTH_AUTHENTICATION_CALLBACK_PARAMS = (
    POINTER(_BLUETOOTH_AUTHENTICATION_CALLBACK_PARAMS)
)


class _BLUETOOTH_DEVICE_SEARCH_PARAMS(ctypes.Structure):
    pass


BLUETOOTH_DEVICE_SEARCH_PARAMS = _BLUETOOTH_DEVICE_SEARCH_PARAMS


class _BLUETOOTH_COD_PAIRS(ctypes.Structure):
    pass


BLUETOOTH_COD_PAIRS = _BLUETOOTH_COD_PAIRS


class _BLUETOOTH_SELECT_DEVICE_PARAMS(ctypes.Structure):
    pass


BLUETOOTH_SELECT_DEVICE_PARAMS = _BLUETOOTH_SELECT_DEVICE_PARAMS


class _BLUETOOTH_PIN_INFO(ctypes.Structure):
    pass


BLUETOOTH_PIN_INFO = _BLUETOOTH_PIN_INFO
PBLUETOOTH_PIN_INFO = POINTER(_BLUETOOTH_PIN_INFO)


class _BLUETOOTH_OOB_DATA_INFO(ctypes.Structure):
    pass


BLUETOOTH_OOB_DATA_INFO = _BLUETOOTH_OOB_DATA_INFO
PBLUETOOTH_OOB_DATA_INFO = POINTER(_BLUETOOTH_OOB_DATA_INFO)


class _BLUETOOTH_NUMERIC_COMPARISON_INFO(ctypes.Structure):
    pass


BLUETOOTH_NUMERIC_COMPARISON_INFO = _BLUETOOTH_NUMERIC_COMPARISON_INFO
PBLUETOOTH_NUMERIC_COMPARISON_INFO = (
    POINTER(_BLUETOOTH_NUMERIC_COMPARISON_INFO)
)


class _BLUETOOTH_PASSKEY_INFO(ctypes.Structure):
    pass


BLUETOOTH_PASSKEY_INFO = _BLUETOOTH_PASSKEY_INFO
PBLUETOOTH_PASSKEY_INFO = POINTER(_BLUETOOTH_PASSKEY_INFO)


class _BLUETOOTH_AUTHENTICATE_RESPONSE(ctypes.Structure):
    pass


BLUETOOTH_AUTHENTICATE_RESPONSE = _BLUETOOTH_AUTHENTICATE_RESPONSE
PBLUETOOTH_AUTHENTICATE_RESPONSE = POINTER(_BLUETOOTH_AUTHENTICATE_RESPONSE)


class _SDP_ELEMENT_DATA(ctypes.Structure):
    pass


SDP_ELEMENT_DATA = _SDP_ELEMENT_DATA
PSDP_ELEMENT_DATA = POINTER(_SDP_ELEMENT_DATA)


class _SDP_STRING_TYPE_DATA(ctypes.Structure):
    pass


SDP_STRING_TYPE_DATA = _SDP_STRING_TYPE_DATA
PSDP_STRING_TYPE_DATA = POINTER(_SDP_STRING_TYPE_DATA)


# Copyright 2002 - 2004, Microsoft Corporation
# ////////////////////////////////////////////////////////////////////////////
from pyWinAPI.shared.winapifamily_h import * # NOQA

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

    from pyWinAPI.shared.bthdef_h import * # NOQA

    BLUETOOTH_MAX_NAME_SIZE = 248
    BLUETOOTH_MAX_PASSKEY_SIZE = 16
    BLUETOOTH_MAX_PASSKEY_BUFFER_SIZE = BLUETOOTH_MAX_PASSKEY_SIZE + 1
    BLUETOOTH_MAX_SERVICE_NAME_SIZE = 256
    BLUETOOTH_DEVICE_NAME_SIZE = 256
    if defined(__cplusplus):
        pass
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXPSP2:
        # *********************************************************************
        #
        # Bluetooth Address
        # *********************************************************************
        #
        BTH_ADDR = ULONGLONG

        BLUETOOTH_ADDRESS = BLUETOOTH_ADDRESS_STRUCT
        BLUETOOTH_NULL_ADDRESS = 0x0

        _BLUETOOTH_LOCAL_SERVICE_INFO._fields_ = [
            # If TRUE, the enable the services
            ('Enabled', BOOL),
            # If service is to be advertised for a particular remote device
            ('btAddr', BLUETOOTH_ADDRESS),
            # SDP Service Name to be advertised.
            ('szName', WCHAR * BLUETOOTH_MAX_SERVICE_NAME_SIZE),
            # Local device name (if any) like COM4 or LPT1
            ('szDeviceString', WCHAR * BLUETOOTH_DEVICE_NAME_SIZE),
        ]
        BLUETOOTH_LOCAL_SERVICE_INFO = BLUETOOTH_LOCAL_SERVICE_INFO_STRUCT
        PBLUETOOTH_LOCAL_SERVICE_INFO = POINTER(BLUETOOTH_LOCAL_SERVICE_INFO)

        # *********************************************************************
        #
        # Radio Enumeration
        # Description:
        # This group of APIs enumerates the installed Bluetooth radios.
        # Sample Usage:
        # HANDLE hRadio;
        # BLUETOOTH_FIND_RADIO_PARAMS btfrp = { (ctypes.sizeof(btfrp) };
        # HBLUETOOTH_RADIO_FIND hFind =
        # BluetoothFindFirstRadio( & btfrp, & hRadio );
        # if ( NULL != hFind )
        # {
        # do
        # {
        # //
        # // TODO: Do something with the radio handle.
        # //
        # CloseHandle( hRadio );
        # } while( BluetoothFindNextRadio( hFind, & hRadio ) );
        # BluetoothFindRadioClose( hFind );
        # }
        # *********************************************************************
        #
        _BLUETOOTH_FIND_RADIO_PARAMS._fields_ = [
            # IN (ctypes.sizeof this structure
            ('dwSize', DWORD),
        ]
        HBLUETOOTH_RADIO_FIND = HANDLE
        # Description:
        # Begins the enumeration of local Bluetooth radios.
        # Parameters:
        # pbtfrp
        # A pointer to a BLUETOOTH_FIND_RADIO_PARAMS structure. The dwSize
        # member of this structure must match the
        # (ctypes.sizeof the of the structure.
        # phRadio
        # A pointer where the first radio HANDLE enumerated will be returned.
        # Return Values:
        # NULL
        # Error opening radios or no devices found. Use GetLastError() for
        # more info.
        # ERROR_INVALID_PARAMETER
        # pbtfrp parameter is NULL.
        # ERROR_REVISION_MISMATCH
        # The pbtfrp structure is not the right length.
        # ERROR_OUTOFMEMORY
        # Out of memory.
        # other Win32 errors.
        # any other
        # Success. The return handle is valid and phRadio points to a valid
        # handle.
        bthprops = ctypes.windll.BTHPROPS

        # _Must_inspect_result_
        # _Success_(return != NULL)
        # HBLUETOOTH_RADIO_FIND
        # WINAPI
        # BluetoothFindFirstRadio(
        # _In_ BLUETOOTH_FIND_RADIO_PARAMS * pbtfrp,
        # _Out_ HANDLE * phRadio
        # );
        BluetoothFindFirstRadio = bthprops.BluetoothFindFirstRadio
        BluetoothFindFirstRadio.restype = HBLUETOOTH_RADIO_FIND

        # Description:
        # Finds the next installed Bluetooth radio.
        # Parameters:
        # hFind
        # The handle returned by BluetoothFindFirstRadio().
        # phRadio
        # A pointer where the next radio HANDLE enumerated will be returned.
        # Return Values:
        # TRUE
        # Next device succesfully found. pHandleOut points to valid handle.
        # FALSE
        # No device found. pHandleOut points to an invalid handle. Call
        # GetLastError() for more details.
        # ERROR_INVALID_HANDLE
        # The handle is NULL.
        # ERROR_NO_MORE_ITEMS
        # No more radios found.
        # ERROR_OUTOFMEMORY
        # Out of memory.
        # other Win32 errors
        # _Must_inspect_result_
        # _Success_(return)
        # BOOL
        # WINAPI
        # BluetoothFindNextRadio(
        # _In_  HBLUETOOTH_RADIO_FIND hFind,
        # _Out_ HANDLE * phRadio
        # );
        BluetoothFindNextRadio = bthprops.BluetoothFindNextRadio
        BluetoothFindNextRadio.restype = BOOL

        # Description:
        # Closes the enumeration handle.
        # Parameters
        # hFind
        # The handle returned by BluetoothFindFirstRadio().
        # Return Values:
        # TRUE
        # Handle succesfully closed.
        # FALSE
        # Failure. Check GetLastError() for details.
        # ERROR_INVALID_HANDLE
        # The handle is NULL.
        # BOOL
        # WINAPI
        # BluetoothFindRadioClose(
        # _In_ HBLUETOOTH_RADIO_FIND hFind
        # );
        BluetoothFindRadioClose = bthprops.BluetoothFindRadioClose
        BluetoothFindRadioClose.restype = WINAPI

        # *********************************************************************
        #
        # Radio Information
        # *********************************************************************
        #
        _BLUETOOTH_RADIO_INFO._fields_ = [
            # Size, in bytes, of this entire data structure
            ('dwSize', DWORD),
            # Address of the local radio
            ('address', BLUETOOTH_ADDRESS),
            # Name of the local radio
            ('szName', WCHAR * BLUETOOTH_MAX_NAME_SIZE),
            # Class of device for the local radio
            ('ulClassofDevice', ULONG),
            # lmpSubversion, manufacturer specifc.
            ('lmpSubversion', USHORT),
            # Manufacturer of the radio, BTH_MFG_Xxx value. For the most up to
            # date
            ('manufacturer', USHORT),
        ]

        # Description:
        # Retrieves the information about the radio represented by the handle.
        # Parameters:
        # hRadio
        # Handle to a local radio retrieved through BluetoothFindFirstRadio()
        # et al or SetupDiEnumerateDeviceInterfaces()
        # pRadioInfo
        # Radio information to be filled in. The dwSize member must match the
        # size of the structure.
        # Return Values:
        # ERROR_SUCCESS
        # The information was retrieved successfully.
        # ERROR_INVALID_PARAMETER
        # pRadioInfo or hRadio is NULL.
        # ERROR_REVISION_MISMATCH
        # pRadioInfo - >dwSize is invalid.
        # other Win32 error codes.
        # _Must_inspect_result_
        # DWORD
        # WINAPI
        # BluetoothGetRadioInfo(
        # _In_    HANDLE hRadio,
        # _Inout_ PBLUETOOTH_RADIO_INFO pRadioInfo
        # );
        BluetoothGetRadioInfo = bthprops.BluetoothGetRadioInfo
        BluetoothGetRadioInfo.restype = DWORD

        # *********************************************************************
        #
        # Device Information Stuctures
        # *********************************************************************
        #
        _BLUETOOTH_DEVICE_INFO._fields_ = [
            # size, in bytes, of this structure - must be the
            # (ctypes.sizeof(BLUETOOTH_DEVICE_INFO)
            ('dwSize', DWORD),
            # Bluetooth address
            ('Address', BLUETOOTH_ADDRESS),
            # Bluetooth "Class of Device"
            ('ulClassofDevice', ULONG),
            # Device connected/in use
            ('fConnected', BOOL),
            # Device remembered
            ('fRemembered', BOOL),
            # Device authenticated/paired/bonded
            ('fAuthenticated', BOOL),
            # Last time the device was seen
            ('stLastSeen', SYSTEMTIME),
            # Last time the device was used for other than RNR, inquiry, or SDP
            ('stLastUsed', SYSTEMTIME),
            # Name of the device
            ('szName', WCHAR * BLUETOOTH_MAX_NAME_SIZE),
        ]
        BLUETOOTH_DEVICE_INFO = BLUETOOTH_DEVICE_INFO_STRUCT
        PBLUETOOTH_DEVICE_INFO = POINTER(BLUETOOTH_DEVICE_INFO)

        # Support added after KB942567
        if (
            NTDDI_VERSION > NTDDI_VISTASP1 or
            (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))
        ):
            class _BLUETOOTH_AUTHENTICATION_METHOD(ENUM):
                BLUETOOTH_AUTHENTICATION_METHOD_LEGACY = 0x1
                BLUETOOTH_AUTHENTICATION_METHOD_OOB = 2
                BLUETOOTH_AUTHENTICATION_METHOD_NUMERIC_COMPARISON = 3
                BLUETOOTH_AUTHENTICATION_METHOD_PASSKEY_NOTIFICATION = 4
                BLUETOOTH_AUTHENTICATION_METHOD_PASSKEY = 5


            BLUETOOTH_AUTHENTICATION_METHOD = _BLUETOOTH_AUTHENTICATION_METHOD
            PBLUETOOTH_AUTHENTICATION_METHOD = (
                POINTER(_BLUETOOTH_AUTHENTICATION_METHOD)
            )


            class _BLUETOOTH_IO_CAPABILITY(ENUM):
                BLUETOOTH_IO_CAPABILITY_DISPLAYONLY = 0x00
                BLUETOOTH_IO_CAPABILITY_DISPLAYYESNO = 0x01
                BLUETOOTH_IO_CAPABILITY_KEYBOARDONLY = 0x02
                BLUETOOTH_IO_CAPABILITY_NOINPUTNOOUTPUT = 0x03
                BLUETOOTH_IO_CAPABILITY_UNDEFINED = 0xFF


            BLUETOOTH_IO_CAPABILITY = _BLUETOOTH_IO_CAPABILITY


            class _BLUETOOTH_AUTHENTICATION_REQUIREMENTS(ENUM):
                BLUETOOTH_MITM_ProtectionNotRequired = 0
                BLUETOOTH_MITM_ProtectionRequired = 0x1
                BLUETOOTH_MITM_ProtectionNotRequiredBonding = 0x2
                BLUETOOTH_MITM_ProtectionRequiredBonding = 0x3
                BLUETOOTH_MITM_ProtectionNotRequiredGeneralBonding = 0x4
                BLUETOOTH_MITM_ProtectionRequiredGeneralBonding = 0x5
                BLUETOOTH_MITM_ProtectionNotDefined = 0xFF


            BLUETOOTH_AUTHENTICATION_REQUIREMENTS = (
                _BLUETOOTH_AUTHENTICATION_REQUIREMENTS
            )

            _BLUETOOTH_AUTHENTICATION_CALLBACK_PARAMS._fields_ = [
                ('deviceInfo', BLUETOOTH_DEVICE_INFO),
                ('authenticationMethod', BLUETOOTH_AUTHENTICATION_METHOD),
                ('ioCapability', BLUETOOTH_IO_CAPABILITY),
                ('authenticationRequirements', BLUETOOTH_AUTHENTICATION_REQUIREMENTS),
                ('Numeric_Value', ULONG),
                ('Passkey', ULONG),
            ]

        # END IF   >= SP1 + KB942567

        # *********************************************************************
        #
        # Device Enumeration
        # Description:
        # Enumerates the Bluetooth devices. The types of returned device
        # depends
        # on the flags set in the BLUETOOTH_DEVICE_SEARCH_PARAMS (see structure
        # definition for details).
        # Sample Usage:
        # HBLUETOOTH_DEVICE_FIND hFind;
        # BLUETOOTH_DEVICE_SEARCH_PARAMS btsp = { (ctypes.sizeof(btsp) };
        # BLUETOOTH_DEVICE_INFO btdi = { (ctypes.sizeof(btdi) };
        # btsp.fReturnAuthenticated = TRUE;
        # btsp.fReturnRemembered = TRUE;
        # hFind = BluetoothFindFirstDevice( & btsp, & btdi );
        # if ( NULL != hFind )
        # {
        # do
        # {
        # //
        # // TODO: Do something useful with the device info.
        # //
        # } while( BluetoothFindNextDevice( hFind, & btdi ) );
        # BluetoothFindDeviceClose( hFind );
        # }
        # *********************************************************************
        #
        _BLUETOOTH_DEVICE_SEARCH_PARAMS._fields_ = [
            # IN (ctypes.sizeof this structure
            ('dwSize', DWORD),
            # IN return authenticated devices
            ('fReturnAuthenticated', BOOL),
            # IN return remembered devices
            ('fReturnRemembered', BOOL),
            # IN return unknown devices
            ('fReturnUnknown', BOOL),
            # IN return connected devices
            ('fReturnConnected', BOOL),
            # IN issue a new inquiry
            ('fIssueInquiry', BOOL),
            # IN timeout for the inquiry
            ('cTimeoutMultiplier', UCHAR),
            # IN handle to radio to enumerate - NULL == all radios will be
            # searched
            ('hRadio', HANDLE),
        ]

        HBLUETOOTH_DEVICE_FIND = HANDLE
        # Description:
        # Begins the enumeration of Bluetooth devices.
        # Parameters:
        # pbtsp
        # A pointer to a BLUETOOTH_DEVICE_SEARCH_PARAMS structure. This
        # structure contains the flags and inputs used to conduct the search.
        # See BLUETOOTH_DEVICE_SEARCH_PARAMS for details.
        # pbtdi
        # A pointer to a BLUETOOTH_DEVICE_INFO structure to return information
        # about the first Bluetooth device found. Note that the dwSize member
        # of the structure must be the
        # (ctypes.sizeof(BLUETOOTH_DEVICE_INFO) before
        # calling because the APIs hast to know the size of the buffer being
        # past in. The dwSize member must also match the exact
        # (ctypes.sizeof(BLUETOOTH_DEVICE_INFO) or the call will fail.
        # Return Values:
        # NULL
        # Error opening radios or not devices found. Use GetLastError for more
        # info.
        # ERROR_INVALID_PARAMETER
        # pbtsp parameter or pbtdi parameter is NULL.
        # ERROR_REVISION_MISMATCH
        # The pbtfrp structure is not the right length.
        # other Win32 errors
        # any other value
        # Success. The return handle is valid and pbtdi points to valid data.
        # _Must_inspect_result_
        # _Success_(return != NULL)
        # HBLUETOOTH_DEVICE_FIND
        # WINAPI
        # BluetoothFindFirstDevice(
        # _In_   BLUETOOTH_DEVICE_SEARCH_PARAMS * pbtsp,
        # _Inout_ BLUETOOTH_DEVICE_INFO *   pbtdi
        # );
        BluetoothFindFirstDevice = bthprops.BluetoothFindFirstDevice
        BluetoothFindFirstDevice.restype = HBLUETOOTH_DEVICE_FIND

        # Description:
        # Finds the next Bluetooth device in the enumeration.
        # Parameters:
        # hFind
        # The handle returned from BluetoothFindFirstDevice().
        # pbtdi
        # A pointer to a BLUETOOTH_DEVICE_INFO structure to return information
        # about the first Bluetooth device found. Note that the dwSize member
        # of the structure must be the
        # (ctypes.sizeof(BLUETOOTH_DEVICE_INFO) before
        # calling because the APIs hast to know the size of the buffer being
        # past in. The dwSize member must also match the exact
        # (ctypes.sizeof(BLUETOOTH_DEVICE_INFO) or the call will fail.
        # Return Values:
        # TRUE
        # Next device succesfully found. pHandleOut points to valid handle.
        # FALSE
        # No device found. pHandleOut points to an invalid handle. Call
        # GetLastError() for more details.
        # ERROR_INVALID_HANDLE
        # The handle is NULL.
        # ERROR_NO_MORE_ITEMS
        # No more radios found.
        # ERROR_OUTOFMEMORY
        # Out of memory.
        # other Win32 errors
        # _Must_inspect_result_
        # BOOL
        # WINAPI
        # BluetoothFindNextDevice(
        # _In_    HBLUETOOTH_DEVICE_FIND  hFind,
        # _Inout_ BLUETOOTH_DEVICE_INFO * pbtdi
        # );
        BluetoothFindNextDevice = bthprops.BluetoothFindNextDevice
        BluetoothFindNextDevice.restype = BOOL

        # Description:
        # Closes the enumeration handle.
        # Parameters:
        # hFind
        # The handle returned from BluetoothFindFirstDevice().
        # Return Values:
        # TRUE
        # Handle succesfully closed.
        # FALSE
        # Failure. Check GetLastError() for details.
        # ERROR_INVALID_HANDLE
        # The handle is NULL.
        # BOOL
        # WINAPI
        # BluetoothFindDeviceClose(
        # _In_ HBLUETOOTH_DEVICE_FIND hFind
        # );
        BluetoothFindDeviceClose = bthprops.BluetoothFindDeviceClose
        BluetoothFindDeviceClose.restype = WINAPI

        # Description:
        # Retrieves information about a remote device.
        # Fill in the dwSize and the Address members of the pbtdi structure
        # being passed in. On success, the rest of the members will be filled
        # out with the information that the system knows.
        # Parameters:
        # hRadio
        # Handle to a local radio retrieved through BluetoothFindFirstRadio()
        # et al or SetupDiEnumerateDeviceInterfaces()
        # pbtdi
        # A pointer to a BLUETOOTH_DEVICE_INFO structure to return information
        # about the first Bluetooth device found. The dwSize member of the
        # structure must be the
        # (ctypes.sizeof the structure in bytes. The Address
        # member must be filled out with the Bluetooth address of the remote
        # device.
        # Return Values:
        # ERROR_SUCCESS
        # Success. Information returned.
        # ERROR_REVISION_MISMATCH
        # The size of the BLUETOOTH_DEVICE_INFO isn't compatible. Check
        # the dwSize member of the BLUETOOTH_DEVICE_INFO structure you
        # passed in.
        # ERROR_NOT_FOUND
        # The radio is not known by the system or the Address field of
        # the BLUETOOTH_DEVICE_INFO structure is all zeros.
        # ERROR_INVALID_PARAMETER
        # pbtdi is NULL.
        # other error codes
        # _Must_inspect_result_
        # DWORD
        # WINAPI
        # BluetoothGetDeviceInfo(
        # _In_opt_ HANDLE  hRadio,
        # _Inout_ BLUETOOTH_DEVICE_INFO * pbtdi
        # );
        BluetoothGetDeviceInfo = bthprops.BluetoothGetDeviceInfo
        BluetoothGetDeviceInfo.restype = DWORD

        # Description:
        # Updates the computer local cache about the device.
        # Parameters:
        # pbtdi
        # A pointer to the BLUETOOTH_DEVICE_INFO structure to be updated.
        # The following members must be valid:
        # dwSize
        # Must match the size of the structure.
        # Address
        # Must be a previously found radio address.
        # szName
        # New name to be stored.
        # Return Values:
        # ERROR_SUCCESS
        # The device information was updated successfully.
        # ERROR_INVALID_PARAMETER
        # pbtdi is NULL.
        # ERROR_REVISION_MISMATCH
        # pbtdi - >dwSize is invalid.
        # other Win32 error codes.
        # _Must_inspect_result_
        # DWORD
        # WINAPI
        # BluetoothUpdateDeviceRecord(
        # _In_ BLUETOOTH_DEVICE_INFO * pbtdi
        # );
        BluetoothUpdateDeviceRecord = bthprops.BluetoothUpdateDeviceRecord
        BluetoothUpdateDeviceRecord.restype = DWORD

        # Description:
        # Delete the authentication (aka "bond") between the computer and the
        # device. Also purges any cached information about the device.
        # Return Values:
        # ERROR_SUCCESS
        # The device was removed successfully.
        # ERROR_NOT_FOUND
        # The device was not found. If no Bluetooth radio is installed,
        # the devices could not be enumerated or removed.
        # DWORD
        # WINAPI
        # BluetoothRemoveDevice(
        # _In_ BLUETOOTH_ADDRESS * pAddress
        # );
        BluetoothRemoveDevice = bthprops.BluetoothRemoveDevice
        BluetoothRemoveDevice.restype = WINAPI

        if not defined(_ARM_):
            # *****************************************************************
            #
            # Device Picker Dialog
            # Description:
            # Invokes a common dialog for selecting Bluetooth devices. The list
            # of devices displayed to the user is determined by the flags and
            # settings the caller specifies in the
            # BLUETOOTH_SELECT_DEVICE_PARAMS
            # (see structure definition for more details).
            # If BluetoothSelectDevices() returns TRUE, the caller must call
            # BluetoothSelectDevicesFree() or memory will be leaked within the
            # process.
            # Sample Usage:
            # BLUETOOTH_SELECT_DEVICE_PARAMS btsdp = { (ctypes.sizeof(btsdp) };
            # btsdp.hwndParent = hDlg;
            # btsdp.fShowUnknown = TRUE;
            # btsdp.fAddNewDeviceWizard = TRUE;
            # BOOL b = BluetoothSelectDevices( & btsdp );
            # if ( b )
            # {
            # BLUETOOTH_DEVICE_INFO * pbtdi = btsdp.pDevices;
            # for
            # ( ULONG cDevice = 0; cDevice < btsdp.cNumDevices; cDevice + + )
            # {
            # if ( pbtdi - >fAuthenticated or pbtdi - >fRemembered )
            # {
            # //
            # // TODO: Do something usefull with the device info
            # //
            # }
            # pbtdi = (BLUETOOTH_DEVICE_INFO *)
            # ((LPBYTE)pbtdi + pbtdi - >dwSize);
            # }
            # BluetoothSelectDevicesFree( & btsdp );
            # }
            # *****************************************************************
            #

            _BLUETOOTH_COD_PAIRS._fields_ = [
                # ClassOfDevice mask to compare
                ('ulCODMask', ULONG),
                # Descriptive string of mask
                ('pcszDescription', LPCWSTR),
            ]

            # typedef BOOL (WINAPI *PFN_DEVICE_CALLBACK)(
            # LPVOID pvParam,
            #  BLUETOOTH_DEVICE_INFO * pDevice
            # );
            PFN_DEVICE_CALLBACK = WINAPI(
                BOOL,
                LPVOID,
                POINTER(BLUETOOTH_DEVICE_INFO)
            )

            _BLUETOOTH_SELECT_DEVICE_PARAMS._fields_ = [
                # IN (ctypes.sizeof this structure
                ('dwSize', DWORD),
                # IN Number in prgClassOfDevice - if ZERO search for all
                # devices
                ('cNumOfClasses', ULONG),
                # IN Array of CODs to find.
                ('prgClassOfDevices', POINTER(BLUETOOTH_COD_PAIRS)),
                # IN If not NULL, sets the "information" text
                ('pszInfo', LPWSTR),
                # IN parent window - NULL == no parent
                ('hwndParent', HWND),
                # IN If TRUE, authenication will be forced before returning
                ('fForceAuthentication', BOOL),
                # IN If TRUE, authenticated devices will be shown in the picker
                ('fShowAuthenticated', BOOL),
                # IN If TRUE, remembered devices will be shown in the picker
                ('fShowRemembered', BOOL),
                # IN If TRUE, unknown devices that are not authenticated or
                # "remember" will be shown.
                ('fShowUnknown', BOOL),
                # IN If TRUE, invokes the add new device wizard.
                ('fAddNewDeviceWizard', BOOL),
                # IN If TRUE, skips the "Services" page in the wizard.
                ('fSkipServicesPage', BOOL),
                # IN If non - NULL, a callback that will be called for each
                # device. If the
                ('pfnDeviceCallback', PFN_DEVICE_CALLBACK),
                # IN Parameter to be passed to pfnDeviceCallback as the
                # pvParam.
                ('pvParam', LPVOID),
                # IN number calles wants - ZERO == no limit.
                ('cNumDevices', DWORD),
                # OUT pointer to an array for BLUETOOTH_DEVICE_INFOs.
                ('pDevices', PBLUETOOTH_DEVICE_INFO),
            ]

            # Description:
            # (See header above)
            # Return Values:
            # TRUE
            # User selected a device. pbtsdp - >pDevices points to valid data.
            # Caller should check the fAuthenticated and fRemembered flags to
            # determine which devices we successfuly authenticated or valid
            # selections by the user.
            # Use BluetoothSelectDevicesFree() to free the nessecary data
            # such as pDevices only if this function returns TRUE.
            # FALSE
            # No valid data returned. Call GetLastError() for possible details
            # of the failure. If GLE() is:
            # ERROR_CANCELLED
            # The user cancelled the request.
            # ERROR_INVALID_PARAMETER
            # The pbtsdp is NULL.
            # ERROR_REVISION_MISMATCH
            # The structure passed in as pbtsdp is of an unknown size.
            # other WIN32 errors
            # _Must_inspect_result_
            # BOOL
            # WINAPI
            # BluetoothSelectDevices(
            # _Inout_ BLUETOOTH_SELECT_DEVICE_PARAMS * pbtsdp
            # );
            BluetoothSelectDevices = bthprops.BluetoothSelectDevices
            BluetoothSelectDevices.restype = BOOL

            # Description:
            # This function should only be called if BluetoothSelectDevices()
            # returns
            # TRUE. This function will free any memory and resource returned
            # by the
            # BluetoothSelectDevices() in the BLUETOOTH_SELECT_DEVICE_PARAMS
            # structure.
            # Return Values:
            # TRUE
            # Success.
            # FALSE
            # Nothing to free.
            # BOOL
            # WINAPI
            # BluetoothSelectDevicesFree(
            # _Inout_ BLUETOOTH_SELECT_DEVICE_PARAMS * pbtsdp
            # );

            BluetoothSelectDevicesFree = bthprops.BluetoothSelectDevicesFree
            BluetoothSelectDevicesFree.restype = WINAPI
        # END IF  not defined(_ARM_)

        # *********************************************************************
        #
        # Device Property Sheet
        # *********************************************************************
        
        # Description:
        # Invokes the CPLs device info property sheet.
        # Parameters:
        # hwndParent
        # HWND to parent the property sheet.
        # pbtdi
        # A pointer to a BLUETOOTH_DEVICE_INFO structure of the device
        # to be displayed.
        # Return Values:
        # TRUE
        # The property page was successfully displayed.
        # FALSE
        # Failure. The property page was not displayed. Check GetLastError
        # for more details.
        # BOOL
        # WINAPI
        # BluetoothDisplayDeviceProperties(
        # _In_opt_ HWND hwndParent,
        # _Inout_ BLUETOOTH_DEVICE_INFO * pbtdi
        # );
        BluetoothDisplayDeviceProperties = (
            bthprops.BluetoothDisplayDeviceProperties
        )
        BluetoothDisplayDeviceProperties.restype = WINAPI

        # *********************************************************************
        #
        # Radio Authentication
        # *********************************************************************
        #
        # Description:
        # Sends an authentication request to a remote device.
        # There are two modes of operation. "Wizard mode" and "Blind mode."
        # "Wizard mode" is invoked when the pszPasskey is NULL. This will cause
        # the "Bluetooth Connection Wizard" to be invoked. The user will be
        # prompted to enter a passkey during the wizard after which the
        # authentication request will be sent. The user will see the success
        # or failure of the authentication attempt. The user will also be
        # given the oppurtunity to try to fix a failed authentication.
        # "Blind mode" is invoked when the pszPasskey is non - NULL. This will
        # cause the computer to send a authentication request to the remote
        # device. No UI is ever displayed. The Bluetooth status code will be
        # mapped to a Win32 Error code.
        # Parameters:
        # hwndParent
        # The window to parent the authentication wizard. If NULL, the
        # wizard will be parented off the desktop.
        # hRadio
        # A valid local radio handle or NULL. If NULL, then all radios will
        # be tired. If any of the radios succeed, then the call will
        # succeed.
        # pbtdi
        # BLUETOOTH_DEVICE_INFO record of the device to be authenticated.
        # pszPasskey
        # PIN to be used to authenticate the device. If NULL, then UI is
        # displayed and the user steps through the authentication process.
        # If not NULL, no UI is shown. The passkey is NOT NULL terminated.
        # ulPasskeyLength
        # Length of szPassKey in bytes. The length must be less than or
        # equal to BLUETOOTH_MAX_PASSKEY_SIZE * (ctypes.sizeof(WCHAR).
        # Return Values:
        # ERROR_SUCCESS
        # Success.
        # ERROR_CANCELLED
        # User aborted the operation.
        # ERROR_INVALID_PARAMETER
        # The device structure in pbtdi is invalid.
        # ERROR_NO_MORE_ITEMS
        # The device in pbtdi is already been marked as authenticated.
        # other WIN32 error
        # Failure. Return value is the error code.
        # For "Blind mode," here is the current mapping of Bluetooth status
        # code to Win32 error codes:
        # { BTH_ERROR_SUCCESS,   ERROR_SUCCESS },
        # { BTH_ERROR_NO_CONNECTION,  ERROR_DEVICE_NOT_CONNECTED },
        # { BTH_ERROR_PAGE_TIMEOUT,   WAIT_TIMEOUT },
        # { BTH_ERROR_HARDWARE_FAILURE,  ERROR_GEN_FAILURE },
        # { BTH_ERROR_AUTHENTICATION_FAILURE, ERROR_NOT_AUTHENTICATED },
        # { BTH_ERROR_MEMORY_FULL,  ERROR_NOT_ENOUGH_MEMORY },
        # { BTH_ERROR_CONNECTION_TIMEOUT,  WAIT_TIMEOUT },
        # { BTH_ERROR_LMP_RESPONSE_TIMEOUT, WAIT_TIMEOUT },
        # { BTH_ERROR_MAX_NUMBER_OF_CONNECTIONS, ERROR_REQ_NOT_ACCEP },
        # { BTH_ERROR_PAIRING_NOT_ALLOWED, ERROR_ACCESS_DENIED },
        # { BTH_ERROR_UNSPECIFIED_ERROR, ERROR_NOT_READY },
        # { BTH_ERROR_LOCAL_HOST_TERMINATED_CONNECTION, ERROR_VC_DISCONNECTED }

        # _Must_inspect_result_
        # DWORD
        # WINAPI
        # BluetoothAuthenticateDevice(
        # _In_opt_ HWND hwndParent,
        # _In_opt_ HANDLE hRadio,
        # _Inout_  BLUETOOTH_DEVICE_INFO * pbtbi,
        # _In_reads_opt_(ulPasskeyLength) PWSTR pszPasskey,
        # _In_ ULONG ulPasskeyLength
        # );
        BluetoothAuthenticateDevice = bthprops.BluetoothAuthenticateDevice
        BluetoothAuthenticateDevice.restype = DWORD

        # Support added after KB942567
        if (
            NTDDI_VERSION > NTDDI_VISTASP1 or
            (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))
        ):
            # Replaces previous API
            # Common header for all PIN related structures
            _BLUETOOTH_PIN_INFO._fields_ = [
                ('pin', UCHAR * BTH_MAX_PIN_SIZE),
                ('pinLength', UCHAR),
            ]
            _BLUETOOTH_OOB_DATA_INFO._fields_ = [
                ('C', UCHAR * 16),
                ('R', UCHAR * 16),
            ]
            _BLUETOOTH_NUMERIC_COMPARISON_INFO._fields_ = [
                ('NumericValue', ULONG),
            ]
            _BLUETOOTH_PASSKEY_INFO._fields_ = [
                ('passkey', ULONG),
            ]

            # Description:
            # Sends an authentication request to a remote device.
            # There are two modes of operation. "Wizard mode" and "Blind mode."
            # "Wizard mode" is invoked when the pbtOobData is NULL. This will
            # cause
            # the "Bluetooth Connection Wizard" to be invoked. The user will be
            # prompted to respond to the device authentication during the
            # wizard
            # after which the authentication request will be sent. The user
            # will see the success
            # or failure of the authentication attempt. The user will also be
            # given the oppurtunity to try to fix a failed authentication.
            # "Blind mode" is invoked when the pbtOobData is non - NULL. This
            # will
            # cause the computer to send a authentication request to the remote
            # device. No UI is ever displayed. The Bluetooth status code will
            # be
            # mapped to a Win32 Error code.
            # Parameters:
            # hwndParent
            # The window to parent the authentication wizard. If NULL, the
            # wizard will be parented off the desktop.
            # hRadio
            # A valid local radio handle or NULL. If NULL, then all radios will
            # be tired. If any of the radios succeed, then the call will
            # succeed.
            # pbtdi
            # BLUETOOTH_DEVICE_INFO record of the device to be authenticated.
            # pbtOobData
            # Out of band data to be used to authenticate the device. If NULL,
            # then UI is
            # displayed and the user steps through the authentication process.
            # If not NULL, no UI is shown.
            # authenticationRequirement
            # The Authentication Requirement of the caller. MITMProtection*
            # Return Values:
            # ERROR_SUCCESS
            # Success.
            # ERROR_CANCELLED
            # User aborted the operation.
            # ERROR_INVALID_PARAMETER
            # The device structure in pbtdi is invalid.
            # ERROR_NO_MORE_ITEMS
            # The device in pbtdi is already been marked as authenticated.
            # other WIN32 error
            # Failure. Return value is the error code.
            # For "Blind mode," here is the current mapping of Bluetooth status
            # code to Win32 error codes:
            # { BTH_ERROR_SUCCESS,   ERROR_SUCCESS },
            # { BTH_ERROR_NO_CONNECTION,  ERROR_DEVICE_NOT_CONNECTED },
            # { BTH_ERROR_PAGE_TIMEOUT,   WAIT_TIMEOUT },
            # { BTH_ERROR_HARDWARE_FAILURE,  ERROR_GEN_FAILURE },
            # { BTH_ERROR_AUTHENTICATION_FAILURE, ERROR_NOT_AUTHENTICATED },
            # { BTH_ERROR_MEMORY_FULL,  ERROR_NOT_ENOUGH_MEMORY },
            # { BTH_ERROR_CONNECTION_TIMEOUT,  WAIT_TIMEOUT },
            # { BTH_ERROR_LMP_RESPONSE_TIMEOUT, WAIT_TIMEOUT },
            # { BTH_ERROR_MAX_NUMBER_OF_CONNECTIONS, ERROR_REQ_NOT_ACCEP },
            # { BTH_ERROR_PAIRING_NOT_ALLOWED, ERROR_ACCESS_DENIED },
            # { BTH_ERROR_UNSPECIFIED_ERROR, ERROR_NOT_READY },
            # { BTH_ERROR_LOCAL_HOST_TERMINATED_CONNECTION, ERROR_VC_DISCONNECTED },

            # _Must_inspect_result_
            # DWORD
            # WINAPI
            # BluetoothAuthenticateDeviceEx(
            # _In_opt_ HWND hwndParentIn
            # , _In_opt_ HANDLE hRadioIn
            # , _Inout_ BLUETOOTH_DEVICE_INFO * pbtdiInout
            # , _In_opt_ PBLUETOOTH_OOB_DATA_INFO pbtOobData
            # , _In_ AUTHENTICATION_REQUIREMENTS authenticationRequirement
            # );
            BluetoothAuthenticateDeviceEx = (
                bthprops.BluetoothAuthenticateDeviceEx
            )
            BluetoothAuthenticateDeviceEx.restype = DWORD

        # END IF   >= SP1 + KB942567
        # Description:
        # Allows the caller to prompt for multiple devices to be authenticated
        # within a single instance of the "Bluetooth Connection Wizard."
        # Parameters:
        # hwndParent
        # The window to parent the authentication wizard. If NULL, the
        # wizard will be parented off the desktop.
        # hRadio
        # A valid local radio handle or NULL. If NULL, then all radios will
        # be tired. If any of the radios succeed, then the call will
        # succeed.
        # cDevices
        # Number of devices in the rgbtdi array.
        # rgbtdi
        # An array BLUETOOTH_DEVICE_INFO records of the devices to be
        # authenticated.
        # Return Values:
        # ERROR_SUCCESS
        # Success. Check the fAuthenticate flag on each of the devices.
        # ERROR_CANCELLED
        # User aborted the operation. Check the fAuthenticate flags on
        # each device to determine if any of the devices were authenticated
        # before the user cancelled the operation.
        # ERROR_INVALID_PARAMETER
        # One of the items in the array of devices is invalid.
        # ERROR_NO_MORE_ITEMS
        # All the devices in the array of devices are already been marked as
        # being authenticated.
        # other WIN32 error
        # Failure. Return value is the error code.
        # _Must_inspect_result_
        # DWORD
        # WINAPI
        # BluetoothAuthenticateMultipleDevices(
        # _In_opt_ HWND hwndParent,
        # _In_opt_ HANDLE hRadio,
        # _In_ DWORD cDevices,
        # _Inout_updates_(cDevices) BLUETOOTH_DEVICE_INFO * rgbtdi
        # );
        BluetoothAuthenticateMultipleDevices = (
            bthprops.BluetoothAuthenticateMultipleDevices
        )
        BluetoothAuthenticateMultipleDevices.restype = DWORD

        # Deprecated after Vista SP1 and KB942567
        if (
            NTDDI_VERSION > NTDDI_VISTASP1 or
            (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))
        ):
            pass
        # END IF   >= SP1 + KB942567

        # *********************************************************************
        #
        # Bluetooth Services
        # *********************************************************************
        #
        BLUETOOTH_SERVICE_DISABLE = 0x00
        BLUETOOTH_SERVICE_ENABLE = 0x01
        BLUETOOTH_SERVICE_MASK = (
            BLUETOOTH_SERVICE_DISABLE |
            BLUETOOTH_SERVICE_ENABLE
        )

        # Description:
        # Enables/disables the services for a particular device.
        # The system maintains a mapping of service guids to supported drivers
        # for
        # Bluetooth - enabled devices. Enabling a service installs the
        # corresponding
        # device driver. Disabling a service removes the corresponding device
        # driver.
        # If a non - supported service is enabled, a driver will not be
        # installed.
        # Parameters
        # hRadio
        # Handle of the local Bluetooth radio device.
        # pbtdi
        # Pointer to a BLUETOOTH_DEVICE_INFO record.
        # pGuidService
        # The service GUID on the remote device.
        # dwServiceFlags
        # Flags to adjust the service.
        # BLUETOOTH_SERVICE_DISABLE - disable the service
        # BLUETOOTH_SERVICE_ENABLE - enables the service
        # Return Values:
        # ERROR_SUCCESS
        # The call was successful.
        # ERROR_INVALID_PARAMETER
        # dwServiceFlags are invalid.
        # ERROR_SERVICE_DOES_NOT_EXIST
        # The GUID in pGuidService is not supported.
        # other WIN32 error
        # The call failed.
        # _Must_inspect_result_
        # DWORD
        # WINAPI
        # BluetoothSetServiceState(
        # _In_opt_ HANDLE  hRadio,
        # _In_ BLUETOOTH_DEVICE_INFO * pbtdi,
        # _In_ GUID *  pGuidService,
        # _In_ DWORD   dwServiceFlags
        # );
        BluetoothSetServiceState = bthprops.BluetoothSetServiceState
        BluetoothSetServiceState.restype = DWORD

        # Description:
        # Enumerates the services guids enabled on a particular device. If
        # hRadio
        # is NULL, all device will be searched for the device and all the
        # services
        # enabled will be returned.
        # Parameters:
        # hRadio
        # Handle of the local Bluetooth radio device. If NULL, it will search
        # all the radios for the address in the pbtdi.
        # pbtdi
        # Pointer to a BLUETOOTH_DEVICE_INFO record.
        # pcService
        # On input, the number of records pointed to by pGuidServices.
        # On output, the number of valid records return in pGuidServices.
        # pGuidServices
        # Pointer to memory that is at least *pcService in length.
        # Return Values:
        # ERROR_SUCCESS
        # The call succeeded. pGuidServices is valid.
        # ERROR_MORE_DATA
        # The call succeeded. pGuidService contains an incomplete list of
        # enabled service GUIDs.
        # other WIN32 errors
        # The call failed.
        # _Must_inspect_result_
        # _Success_(return == ERROR_SUCCESS)
        # DWORD
        # WINAPI
        # BluetoothEnumerateInstalledServices(
        # _In_opt_ HANDLE  hRadio,
        # _In_ BLUETOOTH_DEVICE_INFO * pbtdi,
        # _Inout_ DWORD * pcServiceInout,
        # _Out_writes_to_opt_(*pcServiceInout, *pcServiceInout) GUID *  pGuidServices
        # );
        BluetoothEnumerateInstalledServices = (
            bthprops.BluetoothEnumerateInstalledServices
        )
        BluetoothEnumerateInstalledServices.restype = DWORD

        # Description:
        # Change the discovery state of the local radio(s).
        # If hRadio is NULL, all the radios will be set.
        # Use BluetoothIsDiscoverable() to determine the radios current state.
        # The system ensures that a discoverable system is connectable, thus
        # the radio must allow incoming connections (see
        # BluetoothEnableIncomingConnections) prior to making a radio
        # discoverable. Failure to do so will result in this call failing
        # (returns FALSE).
        # Parameters:
        # hRadio
        # If not NULL, changes the state of a specific radio.
        # If NULL, the API will interate through all the radios.
        # fEnabled
        # If FALSE, discovery will be disabled.
        # Return Values
        # TRUE
        # State was successfully changed. If the caller specified NULL for
        # hRadio, at least of the radios accepted the state change.
        # FALSE
        # State was not changed. If the caller specified NULL for hRadio, all
        # of the radios did not accept the state change.
        # BOOL
        # WINAPI
        # BluetoothEnableDiscovery(
        # _In_opt_ HANDLE hRadio,
        # _In_ BOOL fEnabled
        # );
        BluetoothEnableDiscovery = bthprops.BluetoothEnableDiscovery
        BluetoothEnableDiscovery.restype = WINAPI

        # Description:
        # Determines if the Bluetooth radios are discoverable. If there are
        # multiple radios, the first one to say it is discoverable will cause
        # this function to return TRUE.
        # Parameters:
        # hRadio
        # Handle of the radio to check. If NULL, it will check all local
        # radios.
        # Return Values:
        # TRUE
        # A least one radio is discoverable.
        # FALSE
        # No radios are discoverable.
        # _Must_inspect_result_
        # BOOL
        # WINAPI
        # BluetoothIsDiscoverable(
        # _In_opt_ HANDLE hRadio
        # );
        BluetoothIsDiscoverable = bthprops.BluetoothIsDiscoverable
        BluetoothIsDiscoverable.restype = BOOL

        # Description:
        # Enables/disables the state of a radio to accept incoming connections.
        # If hRadio is NULL, all the radios will be set.
        # Use BluetoothIsConnectable() to determine the radios current state.
        # The system enforces that a radio that is not connectable is not
        # discoverable too. The radio must be made non - discoverable
        # (see BluetoothEnableDiscovery)
        # prior to making a radio non - connectionable.

        # Failure to do so will result in this call failing (returns FALSE).
        # Parameters:
        # hRadio
        # If not NULL, changes the state of a specific radio.
        # If NULL, the API will interate through all the radios.
        # fEnabled
        # If FALSE, incoming connection will be disabled.
        # Return Values
        # TRUE
        # State was successfully changed. If the caller specified NULL for
        # hRadio, at least of the radios accepted the state change.
        # FALSE
        # State was not changed. If the caller specified NULL for hRadio, all
        # of the radios did not accept the state change.
        # _Must_inspect_result_
        # BOOL
        # WINAPI
        # BluetoothEnableIncomingConnections(
        # _In_opt_ HANDLE hRadio,
        # _In_ BOOL fEnabled
        # );
        BluetoothEnableIncomingConnections = (
            bthprops.BluetoothEnableIncomingConnections
        )
        BluetoothEnableIncomingConnections.restype = BOOL

        # Description:
        # Determines if the Bluetooth radios are connectable. If there are
        # multiple radios, the first one to say it is connectable will cause
        # this function to return TRUE.
        # Parameters:
        # hRadio
        # Handle of the radio to check. If NULL, it will check all local
        # radios.
        # Return Values:
        # TRUE
        # A least one radio is allowing incoming connections.
        # FALSE
        # No radios are allowing incoming connections.
        # _Must_inspect_result_
        # BOOL
        # WINAPI
        # BluetoothIsConnectable(
        # _In_opt_ HANDLE hRadio
        # );
        BluetoothIsConnectable = bthprops.BluetoothIsConnectable
        BluetoothIsConnectable.restype = BOOL

        # *********************************************************************
        #
        # Authentication Registration
        # *********************************************************************
        #
        HBLUETOOTH_AUTHENTICATION_REGISTRATION = HANDLE

        # typedef BOOL (CALLBACK *PFN_AUTHENTICATION_CALLBACK)(
        # LPVOID pvParam,
        #  PBLUETOOTH_DEVICE_INFO pDevice
        # );
        PFN_AUTHENTICATION_CALLBACK = CALLBACK(
            BOOL,
            LPVOID,
            PBLUETOOTH_DEVICE_INFO
        )

        # Description:
        # Registers a callback function to be called when a particular device
        # requests authentication. The request is sent to the last application
        # that requested authentication for a particular device.
        # Parameters:
        # pbtdi
        # A pointer to a BLUETOOTH_DEVICE_INFO structure. The Bluetooth
        # address will be used for comparision.
        # phRegHandle
        # A pointer to where the registration HANDLE value will be
        # stored. Call BluetoothUnregisterAuthentication() to close
        # the handle.
        # pfnCallback
        # The function that will be called when the authentication event
        # occurs. This function should match PFN_AUTHENTICATION_CALLBACK's
        # prototype.
        # pvParam
        # Optional parameter to be passed through to the callback function.
        # This can be anything the application was to define.
        # Return Values:
        # ERROR_SUCCESS
        # Success. A valid registration handle was returned.
        # ERROR_OUTOFMEMORY
        # Out of memory.
        # other Win32 error.
        # Failure. The registration handle is invalid.
        # _Must_inspect_result_
        # DWORD
        # WINAPI
        # BluetoothRegisterForAuthentication(
        # _In_opt_ BLUETOOTH_DEVICE_INFO * pbtdi,
        # _Out_ HBLUETOOTH_AUTHENTICATION_REGISTRATION * phRegHandle,
        # _In_opt_ PFN_AUTHENTICATION_CALLBACK pfnCallback,
        # _In_opt_ PVOID pvParam
        # );
        BluetoothRegisterForAuthentication = (
            bthprops.BluetoothRegisterForAuthentication
        )
        BluetoothRegisterForAuthentication.restype = DWORD

        # Support added in KB942567
        if (
            NTDDI_VERSION > NTDDI_VISTASP1 or
            (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))
        ):
            # Replaces previous API
            # typedef BOOL (CALLBACK *PFN_AUTHENTICATION_CALLBACK_EX)(
            # _In_opt_ LPVOID pvParam,
            # _In_PBLUETOOTH_AUTHENTICATION_CALLBACK_PARAMS pAuthCallbackParams
            # );
            PFN_AUTHENTICATION_CALLBACK_EX = CALLBACK(
                BOOL,
                LPVOID,
                PBLUETOOTH_AUTHENTICATION_CALLBACK_PARAMS
            )

            # Description:
            # Registers a callback function to be called when a particular
            # device
            # requests authentication. The request is sent to the last
            # application
            # that requested authentication for a particular device.
            # Parameters:
            # pbtdi
            # A pointer to a BLUETOOTH_DEVICE_INFO structure. The Bluetooth
            # address will be used for comparision.
            # phRegHandle
            # A pointer to where the registration HANDLE value will be
            # stored. Call BluetoothUnregisterAuthentication() to close
            # the handle.
            # pfnCallback
            # The function that will be called when the authentication event
            # occurs. This function should match
            # PFN_AUTHENTICATION_CALLBACK_EX's
            # prototype.
            # pvParam
            # Optional parameter to be passed through to the callback function.
            # This can be anything the application was to define.
            # Return Values:
            # ERROR_SUCCESS
            # Success. A valid registration handle was returned.
            # ERROR_OUTOFMEMORY
            # Out of memory.
            # other Win32 error.
            # Failure. The registration handle is invalid.
            # _Must_inspect_result_
            # DWORD
            # WINAPI
            # BluetoothRegisterForAuthenticationEx(
            # _In_opt_ BLUETOOTH_DEVICE_INFO * pbtdiIn
            # , _Out_ HBLUETOOTH_AUTHENTICATION_REGISTRATION * phRegHandleOut
            # , _In_opt_ PFN_AUTHENTICATION_CALLBACK_EX pfnCallbackIn
            # , _In_opt_ PVOID pvParam
            # );
            BluetoothRegisterForAuthenticationEx = (
                bthprops.BluetoothRegisterForAuthenticationEx
            )
            BluetoothRegisterForAuthenticationEx.restype = DWORD

        # END IF   >= SP1 + KB942567
        # Description:
        # Unregisters an authentication callback and closes the handle. See
        # BluetoothRegisterForAuthentication() for more information about
        # authentication registration.
        # Parameters:
        # hRegHandle
        # Handle returned by BluetoothRegisterForAuthentication().
        # Return Value:
        # TRUE
        # The handle was successfully closed.
        # FALSE
        # The handle was not successfully closed. Check GetLastError for
        # more details.
        # ERROR_INVALID_HANDLE
        # The handle is NULL.
        # other Win32 errors.
        # BOOL
        # WINAPI
        # BluetoothUnregisterAuthentication(
        # _In_ HBLUETOOTH_AUTHENTICATION_REGISTRATION hRegHandle
        # );
        BluetoothUnregisterAuthentication = (
            bthprops.BluetoothUnregisterAuthentication
        )
        BluetoothUnregisterAuthentication.restype = WINAPI

        # Description:
        # This function should be called after receiving an authentication
        # request
        # to send the passkey response.
        # Parameters:
        # hRadio
        # Optional handle to the local radio. If NULL, the function will try
        # each radio until one succeeds.
        # pbtdi
        # A pointer to a BLUETOOTH_DEVICE_INFO structure describing the device
        # being authenticated. This can be the same structure passed to the
        # callback function.
        # pszPasskey
        # A pointer to UNICODE zero - terminated string of the passkey response
        # that should be sent back to the authenticating device.
        # Return Values:
        # ERROR_SUCESS
        # The device accepted the passkey response. The device is
        # authenticated.
        # ERROR_CANCELED
        # The device denied the passkey reponse. This also will returned if
        # there
        # is a communications problem with the local radio.
        # E_FAIL
        # The device returned a failure code during authentication.
        # other Win32 error codes
        # _Must_inspect_result_
        # DWORD
        # WINAPI
        # BluetoothSendAuthenticationResponse(
        # _In_opt_ HANDLE hRadio,
        # _In_ BLUETOOTH_DEVICE_INFO * pbtdi,
        # _In_ LPCWSTR pszPasskey
        # );
        BluetoothSendAuthenticationResponse = (
            bthprops.BluetoothSendAuthenticationResponse
        )
        BluetoothSendAuthenticationResponse.restype = DWORD

        # Support added in KB942567
        if (
            NTDDI_VERSION > NTDDI_VISTASP1 or
            (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))
        ):
            # Replaces previous API
            # Structure used when responding to
            # BTH_REMOTE_AUTHENTICATE_REQUEST event
            _BLUETOOTH_AUTHENTICATE_RESPONSE._fields_ = [
                ('bthAddressRemote', BLUETOOTH_ADDRESS),
                ('authMethod', BLUETOOTH_AUTHENTICATION_METHOD),
                ('pinInfo', BLUETOOTH_PIN_INFO),
                ('oobInfo', BLUETOOTH_OOB_DATA_INFO),
                ('numericCompInfo', BLUETOOTH_NUMERIC_COMPARISON_INFO),
                ('passkeyInfo', BLUETOOTH_PASSKEY_INFO),
                ('negativeResponse', UCHAR),
            ]

            # Description:
            # This function should be called after receiving an authentication
            # request
            # to send the authentication response. (Bluetooth 2.1 and above)
            # Parameters:
            # hRadio
            # Optional handle to the local radio. If NULL, the function will
            # try
            # each radio until one succeeds.
            # pbtdi
            # A pointer to a BLUETOOTH_DEVICE_INFO structure describing the
            # device
            # being authenticated. This can be the same structure passed to the
            # callback function.
            # pauthResponse
            # A pointer to a BTH_AUTHENTICATION_RESPONSE structure.
            # Return Values:
            # ERROR_SUCESS
            # The device accepted the passkey response. The device is
            # authenticated.
            # ERROR_CANCELED
            # The device denied the passkey reponse. This also will returned
            # if there
            # is a communications problem with the local radio.
            # E_FAIL
            # The device returned a failure code during authentication.
            # other Win32 error codes
            # _Must_inspect_result_
            # DWORD
            # WINAPI
            # BluetoothSendAuthenticationResponseEx(
            # _In_opt_ HANDLE hRadioIn
            # , _In_ PBLUETOOTH_AUTHENTICATE_RESPONSE pauthResponse
            # );
            BluetoothSendAuthenticationResponseEx = (
                bthprops.BluetoothSendAuthenticationResponseEx
            )
            BluetoothSendAuthenticationResponseEx.restype = DWORD

        # END IF   >= SP1 + KB942567

        # *********************************************************************
        #
        # SDP Parsing Functions
        # *********************************************************************
        #
        class data(ctypes.Structure):
            pass


        class string(ctypes.Structure):
            pass


        string._fields_ = [
            # by the base language attribute ID list
            ('value', LPBYTE),
            # raw length of the string, may not be NULL terminuated
            ('length', ULONG),
        ]
        data.string = string


        class url(ctypes.Structure):
            pass


        url._fields_ = [
            ('value', LPBYTE),
            ('length', ULONG),
        ]
        data.url = url


        class sequence(ctypes.Structure):
            pass


        sequence._fields_ = [
            # raw sequence, starts at sequence element header
            ('value', LPBYTE),
            # raw sequence length
            ('length', ULONG),
        ]
        data.sequence = sequence


        class alternative(ctypes.Structure):
            pass


        alternative._fields_ = [
            # raw alternative, starts at alternative element header
            ('value', LPBYTE),
            # raw alternative length
            ('length', ULONG),
        ]
        data.alternative = alternative

        data._fields_ = [
            # specificType == SDP_ST_INT128
            ('int128', SDP_LARGE_INTEGER_16),
            # specificType == SDP_ST_INT64
            ('int64', LONGLONG),
            # specificType == SDP_ST_INT32
            ('int32', LONG),
            # specificType == SDP_ST_INT16
            ('int16', SHORT),
            # specificType == SDP_ST_INT8
            ('int8', CHAR),
            # specificType == SDP_ST_UINT128
            ('uint128', SDP_ULARGE_INTEGER_16),
            # specificType == SDP_ST_UINT64
            ('uint64', ULONGLONG),
            # specificType == SDP_ST_UINT32
            ('uint32', ULONG),
            # specificType == SDP_ST_UINT16
            ('uint16', USHORT),
            # specificType == SDP_ST_UINT8
            ('uint8', UCHAR),
            # type == SDP_TYPE_BOOLEAN
            ('booleanVal', UCHAR),
            # specificType == SDP_ST_UUID128
            ('uuid128', GUID),
            # specificType == SDP_ST_UUID32
            ('uuid32', ULONG),
            # specificType == SDP_ST_UUID32
            ('uuid16', USHORT),
            # type == SDP_TYPE_STRING
            ('string', data.string),
            # type == SDP_TYPE_URL
            ('url', data.url),
            # type == SDP_TYPE_SEQUENCE
            ('sequence', data.sequence),
            # type == SDP_TYPE_ALTERNATIVE
            ('alternative', data.alternative),
        ]
        _SDP_ELEMENT_DATA.data = data

        _SDP_ELEMENT_DATA._fields_ = [
            # o SDP_TYPE_UUID
            ('type', SDP_TYPE),
            # Specific types for the generic SDP element types.
            ('specificType', SDP_SPECIFICTYPE),
            # specific type will be SDP_ST_NONE.
            ('data', _SDP_ELEMENT_DATA.data),
        ]

        # Description:
        # Retrieves and parses the element found at pSdpStream
        # Parameters:
        # IN pSdpStream
        # pointer to valid SDP stream
        # IN cbSdpStreamLength
        # length of pSdpStream in bytes
        # OUT pData
        # pointer to be filled in with the data of the SDP element at the
        # beginning of pSdpStream
        # Return Values:
        # ERROR_INVALID_PARAMETER
        # one of required parameters is NULL or the pSdpStream is invalid
        # ERROR_SUCCESS
        # the sdp element was parsed correctly
        # _Must_inspect_result_
        # _Success_(return == ERROR_SUCCESS)
        # DWORD
        # WINAPI
        # BluetoothSdpGetElementData(
        # _In_reads_bytes_(cbSdpStreamLength) LPBYTE pSdpStream,
        # _In_ ULONG cbSdpStreamLength,
        # _Out_ PSDP_ELEMENT_DATA pData
        # );
        BluetoothSdpGetElementData = bthprops.BluetoothSdpGetElementData
        BluetoothSdpGetElementData.restype = DWORD

        HBLUETOOTH_CONTAINER_ELEMENT = HANDLE

        # Description:
        # Iterates over a container stream, returning each elemetn contained
        # with
        # in the container element at the beginning of pContainerStream
        # Parameters:
        # IN pContainerStream
        # pointer to valid SDP stream whose first element is either a sequence
        # or alternative
        # IN cbContainerlength
        # length in bytes of pContainerStream
        # IN OUT pElement
        # Value used to keep track of location within the stream. The first
        # time this function is called for a particular container, *pElement
        # should equal NULL. Upon subsequent calls, the value should be
        # unmodified.
        # OUT pData
        # pointer to be filled in with the data of the SDP element at the
        # current element of pContainerStream
        # Return Values:
        # ERROR_SUCCESS
        # The call succeeded, pData contains the data
        # ERROR_NO_MORE_ITEMS
        # There are no more items in the list, the caller should cease calling
        # BluetoothSdpGetContainerElementData for this container.
        # ERROR_INVALID_PARAMETER
        # A required pointer is NULL or the container is not a valid SDP
        # stream
        # Usage example:
        # HBLUETOOTH_CONTAINER_ELEMENT element;
        # SDP_ELEMENT_DATA data;
        # ULONG result;
        # element = NULL;
        # while (TRUE) {
        # result = BluetoothSdpGetContainerElementData(
        # pContainer, ulContainerLength, & element, & data);
        # if (result == ERROR_NO_MORE_ITEMS) {
        # // We are done
        # break;
        # }
        # else if (result != ERROR_SUCCESS) {
        # // error
        # }
        # // do something with data ...
        # }
        # _Must_inspect_result_
        # _Success_(return == ERROR_SUCCESS)
        # DWORD
        # WINAPI
        # BluetoothSdpGetContainerElementData(
        # _In_reads_bytes_(cbContainerLength) LPBYTE pContainerStream,
        # _In_ ULONG cbContainerLength,
        # _Inout_ HBLUETOOTH_CONTAINER_ELEMENT* pElement,
        # _Out_ PSDP_ELEMENT_DATA pData
        # );
        BluetoothSdpGetContainerElementData = (
            bthprops.BluetoothSdpGetContainerElementData
        )
        BluetoothSdpGetContainerElementData.restype = DWORD

        # Description:
        # Retrieves the attribute value for the given attribute ID.
        # pRecordStream
        # must be an SDP stream that is formatted as an SDP record, a SEQUENCE
        # containing UINT16 + element pairs.
        # Parameters:
        # IN pRecordStream
        # pointer to a valid SDP stream which is formatted as a singl SDP
        # record
        # IN cbRecordlnegh
        # length of pRecordStream in bytes
        # IN usAttributeId
        # the attribute ID to search for. see bthdef.h for SDP_ATTRIB_Xxx
        # values.
        # OUT pAttributeData
        # pointer that will contain the attribute ID's value
        # Return Values:
        # ERRROR_SUCCESS
        # Call succeeded, pAttributeData contains the attribute value
        # ERROR_INVALID_PARAMETER
        # One of the required pointers was NULL, pRecordStream was not a valid
        # SDP stream, or pRecordStream was not a properly formatted SDP record
        # ERROR_FILE_NOT_FOUND
        # usAttributeId was not found in the record
        # Usage:
        # ULONG result;
        # SDP_DATA_ELEMENT data;
        # result = BluetoothSdpGetAttributeValue(
        # pRecordStream, cbRecordLength, SDP_ATTRIB_RECORD_HANDLE, & data);
        # if (result == ERROR_SUCCESS) {
        # printf("record handle is 0x%x\n", data.data.uint32);
        # }
        # _Must_inspect_result_
        # _Success_(return == ERROR_SUCCESS)
        # DWORD
        # WINAPI
        # BluetoothSdpGetAttributeValue(
        # _In_reads_bytes_(cbRecordLength) LPBYTE pRecordStream,
        # _In_ ULONG cbRecordLength,
        # _In_ USHORT usAttributeId,
        # _Out_ PSDP_ELEMENT_DATA pAttributeData
        # );
        BluetoothSdpGetAttributeValue = bthprops.BluetoothSdpGetAttributeValue
        BluetoothSdpGetAttributeValue.restype = DWORD

        # These three fields correspond one to one with the triplets defined
        # in the
        # SDP specification for the language base attribute ID list.
        _SDP_STRING_TYPE_DATA._fields_ = [
            # for the representation of names of languages".
            ('encoding', USHORT),
            # MIBE number from IANA database
            ('mibeNum', USHORT),
            # The base attribute where the string is to be found in the record
            ('attributeId', USHORT),
        ]

        # Description:
        # Converts a raw string embedded in the SDP record into a UNICODE
        # string
        # Parameters:
        # IN pRecordStream
        # a valid SDP stream which is formatted as an SDP record
        # IN cbRecordLength
        # length of pRecordStream in bytes
        # IN pStringData
        # if NULL, then the calling thread's locale will be used to search
        # for a matching string in the SDP record. If not NUL, the mibeNum
        # and attributeId will be used to find the string to convert.
        # IN usStringOffset
        # the SDP string type offset to convert. usStringOffset is added to
        # the base attribute id of the string. SDP specification defined
        # offsets are: STRING_NAME_OFFSET, STRING_DESCRIPTION_OFFSET, and
        # STRING_PROVIDER_NAME_OFFSET (found in bthdef.h).
        # OUT pszString
        # if NULL, pcchStringLength will be filled in with the required number
        # of characters (not bytes) to retrieve the converted string.
        # IN OUT pcchStringLength
        # Upon input, if pszString is not NULL, will contain the length of
        # pszString in characters. Upon output, it will contain either the
        # number of required characters including NULL if an error is returned
        # or the number of characters written to pszString (including NULL).
        # Return Values:
        # ERROR_SUCCES
        # Call was successful and pszString contains the converted string
        # ERROR_MORE_DATA
        # pszString was NULL or too small to contain the converted string,
        # pccxhStringLength contains the required length in characters
        # ERROR_INVALID_DATA
        # Could not perform the conversion
        # ERROR_NO_SYSTEM_RESOURCES
        # Could not allocate memory internally to perform the conversion
        # ERROR_INVALID_PARAMETER
        # One of the rquired pointers was NULL, pRecordStream was not a valid
        # SDP stream, pRecordStream was not a properly formatted record, or
        # the desired attribute + offset was not a string.
        # Other HRESULTs returned by COM
        # _Must_inspect_result_
        # _Success_(return == 0)
        # DWORD
        # WINAPI
        # BluetoothSdpGetString(
        # _In_reads_bytes_(cbRecordLength) LPBYTE pRecordStream,
        # _In_ ULONG cbRecordLength,
        # _In_opt_ PSDP_STRING_TYPE_DATA pStringData,
        # _In_ USHORT usStringOffset,
        # _Out_writes_to_(*pcchStringLength, *pcchStringLength) PWSTR pszString
        # _Inout_ PULONG pcchStringLength
        # );
        BluetoothSdpGetString = bthprops.BluetoothSdpGetString
        BluetoothSdpGetString.restype = DWORD

        # *********************************************************************
        #
        # Raw Attribute Enumeration
        # *********************************************************************
        #
        # typedef BOOL (CALLBACK *PFN_BLUETOOTH_ENUM_ATTRIBUTES_CALLBACK)(
        #     _In_ ULONG   uAttribId,
        #     _In_reads_bytes_(cbStreamSize) LPBYTE  pValueStream,
        #     _In_ ULONG   cbStreamSize,
        #     _In_opt_ LPVOID  pvParam
        #     );
        PFN_BLUETOOTH_ENUM_ATTRIBUTES_CALLBACK = CALLBACK(
            BOOL,
            ULONG,
            LPBYTE,
            ULONG,
            LPVOID
        )

        # Description:
        # Enumerates through the SDP record stream calling the Callback
        # function
        # for each attribute in the record. If the Callback function returns
        # FALSE, the enumeration is stopped.
        # Return Values:
        # TRUE
        # Successnot Something was enumerated.
        # FALSE
        # Failure. GetLastError() could be one of the following:
        # ERROR_INVALID_PARAMETER
        # pSDPStream or pfnCallback is NULL.
        # ERROR_INVALID_DATA
        # The SDP stream is corrupt.
        # other Win32 errors.

        # _Must_inspect_result_
        # BOOL
        # WINAPI
        # BluetoothSdpEnumAttributes(
        # _In_reads_bytes_(cbStreamSize) LPBYTE  pSDPStream,
        # _In_ ULONG   cbStreamSize,
        # _In_ PFN_BLUETOOTH_ENUM_ATTRIBUTES_CALLBACK pfnCallback,
        # _In_ LPVOID  pvParam
        # );
        BluetoothSdpEnumAttributes = bthprops.BluetoothSdpEnumAttributes
        BluetoothSdpEnumAttributes.restype = BOOL

        BluetoothEnumAttributes = BluetoothSdpEnumAttributes

    # END IF   (NTDDI_VERSION >= NTDDI_WINXPSP2)
    if NTDDI_VERSION >= NTDDI_VISTA:
        # The following APIs are only available on Vista or later
        bthprops = ctypes.windll.BTHPROPS

        # _Must_inspect_result_
        # DWORD
        # WINAPI
        # BluetoothSetLocalServiceInfo(
        # _In_opt_ HANDLE  hRadioIn
        # , _In_ GUID * pClassGuid
        # , _In_ ULONG ulInstance
        # , _In_ BLUETOOTH_LOCAL_SERVICE_INFO * pServiceInfoIn
        # );
        BluetoothSetLocalServiceInfo = bthprops.BluetoothSetLocalServiceInfo
        BluetoothSetLocalServiceInfo.restype = DWORD

    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
    # Support added in KB942567
    if (
        NTDDI_VERSION > NTDDI_VISTASP1 or
        (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))
    ):
        # IsBluetoothVersionAvailable
        # Description:
        # Indicate if the installed Bluetooth binary set supports
        # the requested version
        # Return Values:
        # TRUE if the installed bluetooth binaries support the given
        # Major & Minor versions
        # Note this function is only exported in version 2.1 and later.
        bthprops = ctypes.windll.BTHPROPS

        # _Must_inspect_result_
        # BOOL
        # WINAPI
        # BluetoothIsVersionAvailable(
        # _In_ UCHAR MajorVersion,
        # _In_ UCHAR MinorVersion
        # );
        BluetoothIsVersionAvailable = bthprops.BluetoothIsVersionAvailable
        BluetoothIsVersionAvailable.restype = BOOL

    # END IF   >= SP1 + KB942567
    if defined(__cplusplus):
        pass
    # END IF
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
