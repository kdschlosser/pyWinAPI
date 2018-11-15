# ++
# Copyright (c) Microsoft Corporation.  All rights reserved.
# Module Name:
# devpkey.h
# Abstract:
# Defines property keys for the Plug and Play Device Property API.
# Environment:
# User and Kernel modes.
# --
from shared.winapifamily_h import * # NOQA
from shared.devpropdef_h import * # NOQA

# DEVPKEY_NAME
# Common DEVPKEY used to retrieve the display name for an object.

# DEVPROP_TYPE_STRING
DEVPKEY_NAME = DEFINE_DEVPROPKEY(
    0xB725F130,
    0x47EF,
    0x101A,
    0xA5,
    0xF1,
    0x02,
    0x60,
    0x8C,
    0x9E,
    0xEB,
    0xAC,
    0xA
)

# Device properties
# These DEVPKEYs correspond to the SetupAPI SPDRP_XXX device properties.

# DEVPROP_TYPE_STRING
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_DeviceDesc = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x2
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_HardwareIds = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x3
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_CompatibleIds = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x4
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_Service = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x6
)
# DEVPROP_TYPE_GUID
DEVPKEY_Device_Class = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x9
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_ClassGuid = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0xA
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_Driver = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0xB
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_ConfigFlags = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0xC
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_Manufacturer = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0xD
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_FriendlyName = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0xE
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_LocationInfo = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0xF
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_PDOName = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x10
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_Capabilities = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x11
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_UINumber = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x12
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_UpperFilters = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x13
)
# DEVPROP_TYPE_GUID
DEVPKEY_Device_LowerFilters = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x14
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_BusTypeGuid = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x15
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_LegacyBusType = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x16
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_BusNumber = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x17
)
# DEVPROP_TYPE_SECURITY_DESCRIPTOR
DEVPKEY_Device_EnumeratorName = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x18
)
# DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING
DEVPKEY_Device_Security = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x19
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_SecuritySDS = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x1A
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_DevType = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x1B
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_Exclusive = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x1C
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_Characteristics = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x1D
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_Address = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x1E
)
# DEVPROP_TYPE_BINARY
DEVPKEY_Device_UINumberDescFormat = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x1F
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_PowerData = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x20
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_RemovalPolicy = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x21
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_RemovalPolicyDefault = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x22
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_RemovalPolicyOverride = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x23
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_InstallState = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x24
)
# DEVPROP_TYPE_GUID
DEVPKEY_Device_LocationPaths = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x25
)
DEVPKEY_Device_BaseContainerId = DEFINE_DEVPROPKEY(
    0xA45C254E,
    0xDF1C,
    0x4EFD,
    0x80,
    0x20,
    0x67,
    0xD1,
    0x46,
    0xA8,
    0x50,
    0xE0,
    0x26
)

# Device and Device Interface property
# Common DEVPKEY used to retrieve the device instance id associated with
# devices and device INTerfaces.

# DEVPROP_TYPE_STRING
DEVPKEY_Device_InstanceId = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x100
)

# Device properties
# These DEVPKEYs correspond to a device's status and problem code.

# DEVPROP_TYPE_UINT32
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_DevNodeStatus = DEFINE_DEVPROPKEY(
    0x4340A6C5,
    0x93FA,
    0x4706,
    0x97,
    0x2C,
    0x7B,
    0x64,
    0x80,
    0x08,
    0xA5,
    0xA7,
    0x2
)
DEVPKEY_Device_ProblemCode = DEFINE_DEVPROPKEY(
    0x4340A6C5,
    0x93FA,
    0x4706,
    0x97,
    0x2C,
    0x7B,
    0x64,
    0x80,
    0x08,
    0xA5,
    0xA7,
    0x3
)

# Device properties
# These DEVPKEYs correspond to a device's relations.

# DEVPROP_TYPE_STRING_LIST
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_EjectionRelations = DEFINE_DEVPROPKEY(
    0x4340A6C5,
    0x93FA,
    0x4706,
    0x97,
    0x2C,
    0x7B,
    0x64,
    0x80,
    0x08,
    0xA5,
    0xA7,
    0x4
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_RemovalRelations = DEFINE_DEVPROPKEY(
    0x4340A6C5,
    0x93FA,
    0x4706,
    0x97,
    0x2C,
    0x7B,
    0x64,
    0x80,
    0x08,
    0xA5,
    0xA7,
    0x5
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_PowerRelations = DEFINE_DEVPROPKEY(
    0x4340A6C5,
    0x93FA,
    0x4706,
    0x97,
    0x2C,
    0x7B,
    0x64,
    0x80,
    0x08,
    0xA5,
    0xA7,
    0x6
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_BusRelations = DEFINE_DEVPROPKEY(
    0x4340A6C5,
    0x93FA,
    0x4706,
    0x97,
    0x2C,
    0x7B,
    0x64,
    0x80,
    0x08,
    0xA5,
    0xA7,
    0x7
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_Parent = DEFINE_DEVPROPKEY(
    0x4340A6C5,
    0x93FA,
    0x4706,
    0x97,
    0x2C,
    0x7B,
    0x64,
    0x80,
    0x08,
    0xA5,
    0xA7,
    0x8
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_Children = DEFINE_DEVPROPKEY(
    0x4340A6C5,
    0x93FA,
    0x4706,
    0x97,
    0x2C,
    0x7B,
    0x64,
    0x80,
    0x08,
    0xA5,
    0xA7,
    0x9
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_Siblings = DEFINE_DEVPROPKEY(
    0x4340A6C5,
    0x93FA,
    0x4706,
    0x97,
    0x2C,
    0x7B,
    0x64,
    0x80,
    0x08,
    0xA5,
    0xA7,
    0xA
)
DEVPKEY_Device_TransportRelations = DEFINE_DEVPROPKEY(
    0x4340A6C5,
    0x93FA,
    0x4706,
    0x97,
    0x2C,
    0x7B,
    0x64,
    0x80,
    0x08,
    0xA5,
    0xA7,
    0xB
)

# Device property
# This DEVPKEY corresponds to a the status code that resulted in a device to
# be in a problem state.

# DEVPROP_TYPE_NTSTATUS
DEVPKEY_Device_ProblemStatus = DEFINE_DEVPROPKEY(
    0x4340A6C5,
    0x93FA,
    0x4706,
    0x97,
    0x2C,
    0x7B,
    0x64,
    0x80,
    0x08,
    0xA5,
    0xA7,
    0xC
)

# Device properties
# These DEVPKEYs are set for the corresponding types of root-enumerated
# devices.

# DEVPROP_TYPE_BOOLEAN
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_Reported = DEFINE_DEVPROPKEY(
    0x80497100,
    0x8C73,
    0x48B9,
    0xAA,
    0xD9,
    0xCE,
    0x38,
    0x7E,
    0x19,
    0xC5,
    0x6E,
    0x2
)
DEVPKEY_Device_Legacy = DEFINE_DEVPROPKEY(
    0x80497100,
    0x8C73,
    0x48B9,
    0xAA,
    0xD9,
    0xCE,
    0x38,
    0x7E,
    0x19,
    0xC5,
    0x6E,
    0x3
)

# Device Container Id

# DEVPROP_TYPE_GUID
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_ContainerId = DEFINE_DEVPROPKEY(
    0x8C7ED206,
    0x3F8A,
    0x4827,
    0xB3,
    0xAB,
    0xAE,
    0x9E,
    0x1F,
    0xAE,
    0xFC,
    0x6C,
    0x2
)
DEVPKEY_Device_InLocalMachineContainer = DEFINE_DEVPROPKEY(
    0x8C7ED206,
    0x3F8A,
    0x4827,
    0xB3,
    0xAB,
    0xAE,
    0x9E,
    0x1F,
    0xAE,
    0xFC,
    0x6C,
    0x4
)

# Device property
# This DEVPKEY correspond to a device's model.

# DEVPROP_TYPE_STRING
DEVPKEY_Device_Model = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x27
)

# Device Experience related Keys

# DEVPROP_TYPE_GUID
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_ModelId = DEFINE_DEVPROPKEY(
    0x80D81EA6,
    0x7473,
    0x4B0C,
    0x82,
    0x16,
    0xEF,
    0xC1,
    0x1A,
    0x2C,
    0x4C,
    0x8B,
    0x2
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_FriendlyNameAttributes = DEFINE_DEVPROPKEY(
    0x80D81EA6,
    0x7473,
    0x4B0C,
    0x82,
    0x16,
    0xEF,
    0xC1,
    0x1A,
    0x2C,
    0x4C,
    0x8B,
    0x3
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_ManufacturerAttributes = DEFINE_DEVPROPKEY(
    0x80D81EA6,
    0x7473,
    0x4B0C,
    0x82,
    0x16,
    0xEF,
    0xC1,
    0x1A,
    0x2C,
    0x4C,
    0x8B,
    0x4
)
# DEVPROP_TYPE_INT32
DEVPKEY_Device_PresenceNotForDevice = DEFINE_DEVPROPKEY(
    0x80D81EA6,
    0x7473,
    0x4B0C,
    0x82,
    0x16,
    0xEF,
    0xC1,
    0x1A,
    0x2C,
    0x4C,
    0x8B,
    0x5
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_SignalStrength = DEFINE_DEVPROPKEY(
    0x80D81EA6,
    0x7473,
    0x4B0C,
    0x82,
    0x16,
    0xEF,
    0xC1,
    0x1A,
    0x2C,
    0x4C,
    0x8B,
    0x6
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_IsAssociateableByUserAction = DEFINE_DEVPROPKEY(
    0x80D81EA6,
    0x7473,
    0x4B0C,
    0x82,
    0x16,
    0xEF,
    0xC1,
    0x1A,
    0x2C,
    0x4C,
    0x8B,
    0x7
)
DEVPKEY_Device_ShowInUninstallUI = DEFINE_DEVPROPKEY(
    0x80D81EA6,
    0x7473,
    0x4B0C,
    0x82,
    0x16,
    0xEF,
    0xC1,
    0x1A,
    0x2C,
    0x4C,
    0x8B,
    0x8
)

# Other Device properties

# DEVPROP_TYPE_UINT32
DEVPKEY_Device_Numa_Proximity_Domain = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x1
)

# DEVPROP_TYPE_UINT32
DEVPKEY_Numa_Proximity_Domain = DEVPKEY_Device_Numa_Proximity_Domain

# DEVPROP_TYPE_UINT32
DEVPKEY_Device_DHP_Rebalance_Policy = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x2
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_Numa_Node = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x3
)
# DEVPROP_TYPE_BOOL
DEVPKEY_Device_BusReportedDeviceDesc = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x4
)
# DEVPROP_TYPE_BOOL
DEVPKEY_Device_IsPresent = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x5
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_HasProblem = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x6
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_ConfigurationId = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x7
)
# DEVPROP_TYPE_BINARY
DEVPKEY_Device_ReportedDeviceIdsHash = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x8
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_PhysicalDeviceLocation = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x9
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_BiosDeviceName = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0xA
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_DriverProblemDesc = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0xB
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_DebuggerSafe = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0xC
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_PostInstallInProgress = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0xD
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_Stack = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0xE
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_ExtendedConfigurationIds = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0xF
)
# DEVPROP_TYPE_FILETIME
DEVPKEY_Device_IsRebootRequired = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x10
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_FirmwareDate = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x11
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_FirmwareVersion = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x12
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_FirmwareRevision = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x13
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_DependencyProviders = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x14
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_DependencyDependents = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x15
)
# DEVPROP_TYPE_UINT64
DEVPKEY_Device_SoftRestartSupported = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x16
)
DEVPKEY_Device_ExtendedAddress = DEFINE_DEVPROPKEY(
    0x540B947E,
    0x8B40,
    0x45BC,
    0xA8,
    0xA2,
    0x6A,
    0x0B,
    0x89,
    0x4C,
    0xBD,
    0xA2,
    0x17
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_SessionId = DEFINE_DEVPROPKEY(
    0x83DA6326,
    0x97A6,
    0x4088,
    0x94,
    0x53,
    0xA1,
    0x92,
    0x3F,
    0x57,
    0x3B,
    0x29,
    0x6
)

# Device activity timestamp properties

# DEVPROP_TYPE_FILETIME
# DEVPROP_TYPE_FILETIME
DEVPKEY_Device_InstallDate = DEFINE_DEVPROPKEY(
    0x83DA6326,
    0x97A6,
    0x4088,
    0x94,
    0x53,
    0xA1,
    0x92,
    0x3F,
    0x57,
    0x3B,
    0x29,
    0x64
)
# DEVPROP_TYPE_FILETIME
DEVPKEY_Device_FirstInstallDate = DEFINE_DEVPROPKEY(
    0x83DA6326,
    0x97A6,
    0x4088,
    0x94,
    0x53,
    0xA1,
    0x92,
    0x3F,
    0x57,
    0x3B,
    0x29,
    0x65
)
# DEVPROP_TYPE_FILETIME
DEVPKEY_Device_LastArrivalDate = DEFINE_DEVPROPKEY(
    0x83DA6326,
    0x97A6,
    0x4088,
    0x94,
    0x53,
    0xA1,
    0x92,
    0x3F,
    0x57,
    0x3B,
    0x29,
    0x66
)
DEVPKEY_Device_LastRemovalDate = DEFINE_DEVPROPKEY(
    0x83DA6326,
    0x97A6,
    0x4088,
    0x94,
    0x53,
    0xA1,
    0x92,
    0x3F,
    0x57,
    0x3B,
    0x29,
    0x67
)

# Device driver properties

# DEVPROP_TYPE_FILETIME
# DEVPROP_TYPE_STRING
DEVPKEY_Device_DriverDate = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0x2
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_DriverVersion = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0x3
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_DriverDesc = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0x4
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_DriverInfPath = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0x5
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_DriverInfSection = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0x6
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_DriverInfSectionExt = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0x7
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_MatchingDeviceId = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0x8
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_DriverProvider = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0x9
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_Device_DriverPropPageProvider = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0xA
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_DriverCoInstallers = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0xB
)
# DEVPROP_TYPE_STRING
DEVPKEY_Device_ResourcePickerTags = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0xC
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_ResourcePickerExceptions = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0xD
)
# DEVPROP_TYPE_UINT32
DEVPKEY_Device_DriverRank = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0xE
)
DEVPKEY_Device_DriverLogoLevel = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0xF
)

# Device properties
# These DEVPKEYs may be set by the driver package installed for a device.

# DEVPROP_TYPE_BOOLEAN
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_NoConnectSound = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0x11
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_GenericDriverInstalled = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0x12
)
DEVPKEY_Device_AdditionalSoftwareRequested = DEFINE_DEVPROPKEY(
    0xA8B865DD,
    0x2E3D,
    0x4094,
    0xAD,
    0x97,
    0xE5,
    0x93,
    0xA7,
    0xC,
    0x75,
    0xD6,
    0x13
)

# Device safe-removal properties

# DEVPROP_TYPE_BOOLEAN
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_Device_SafeRemovalRequired = DEFINE_DEVPROPKEY(
    0xAFD97640,
    0x86A3,
    0x4210,
    0xB6,
    0x7C,
    0x28,
    0x9C,
    0x41,
    0xAA,
    0xBE,
    0x55,
    0x2
)
DEVPKEY_Device_SafeRemovalRequiredOverride = DEFINE_DEVPROPKEY(
    0xAFD97640,
    0x86A3,
    0x4210,
    0xB6,
    0x7C,
    0x28,
    0x9C,
    0x41,
    0xAA,
    0xBE,
    0x55,
    0x3
)

# Device properties
# These DEVPKEYs may be set by the driver package installed for a device.

# DEVPROP_TYPE_STRING
# DEVPROP_TYPE_STRING
DEVPKEY_DrvPkg_Model = DEFINE_DEVPROPKEY(
    0xCF73BB51,
    0x3ABF,
    0x44A2,
    0x85,
    0xE0,
    0x9A,
    0x3D,
    0xC7,
    0xA1,
    0x21,
    0x32,
    0x2
)
# DEVPROP_TYPE_STRING
DEVPKEY_DrvPkg_VendorWebSite = DEFINE_DEVPROPKEY(
    0xCF73BB51,
    0x3ABF,
    0x44A2,
    0x85,
    0xE0,
    0x9A,
    0x3D,
    0xC7,
    0xA1,
    0x21,
    0x32,
    0x3
)
# DEVPROP_TYPE_STRING
DEVPKEY_DrvPkg_DetailedDescription = DEFINE_DEVPROPKEY(
    0xCF73BB51,
    0x3ABF,
    0x44A2,
    0x85,
    0xE0,
    0x9A,
    0x3D,
    0xC7,
    0xA1,
    0x21,
    0x32,
    0x4
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DrvPkg_DocumentationLink = DEFINE_DEVPROPKEY(
    0xCF73BB51,
    0x3ABF,
    0x44A2,
    0x85,
    0xE0,
    0x9A,
    0x3D,
    0xC7,
    0xA1,
    0x21,
    0x32,
    0x5
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DrvPkg_Icon = DEFINE_DEVPROPKEY(
    0xCF73BB51,
    0x3ABF,
    0x44A2,
    0x85,
    0xE0,
    0x9A,
    0x3D,
    0xC7,
    0xA1,
    0x21,
    0x32,
    0x6
)
DEVPKEY_DrvPkg_BrandingIcon = DEFINE_DEVPROPKEY(
    0xCF73BB51,
    0x3ABF,
    0x44A2,
    0x85,
    0xE0,
    0x9A,
    0x3D,
    0xC7,
    0xA1,
    0x21,
    0x32,
    0x7
)

# Device setup class properties
# These DEVPKEYs correspond to the SetupAPI SPCRP_XXX setup class properties.

# DEVPROP_TYPE_STRING_LIST
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceClass_UpperFilters = DEFINE_DEVPROPKEY(
    0x4321918B,
    0xF69E,
    0x470D,
    0xA5,
    0xDE,
    0x4D,
    0x88,
    0xC7,
    0x5A,
    0xD2,
    0x4B,
    0x13
)
# DEVPROP_TYPE_SECURITY_DESCRIPTOR
DEVPKEY_DeviceClass_LowerFilters = DEFINE_DEVPROPKEY(
    0x4321918B,
    0xF69E,
    0x470D,
    0xA5,
    0xDE,
    0x4D,
    0x88,
    0xC7,
    0x5A,
    0xD2,
    0x4B,
    0x14
)
# DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING
DEVPKEY_DeviceClass_Security = DEFINE_DEVPROPKEY(
    0x4321918B,
    0xF69E,
    0x470D,
    0xA5,
    0xDE,
    0x4D,
    0x88,
    0xC7,
    0x5A,
    0xD2,
    0x4B,
    0x19
)
# DEVPROP_TYPE_UINT32
DEVPKEY_DeviceClass_SecuritySDS = DEFINE_DEVPROPKEY(
    0x4321918B,
    0xF69E,
    0x470D,
    0xA5,
    0xDE,
    0x4D,
    0x88,
    0xC7,
    0x5A,
    0xD2,
    0x4B,
    0x1A
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceClass_DevType = DEFINE_DEVPROPKEY(
    0x4321918B,
    0xF69E,
    0x470D,
    0xA5,
    0xDE,
    0x4D,
    0x88,
    0xC7,
    0x5A,
    0xD2,
    0x4B,
    0x1B
)
# DEVPROP_TYPE_UINT32
DEVPKEY_DeviceClass_Exclusive = DEFINE_DEVPROPKEY(
    0x4321918B,
    0xF69E,
    0x470D,
    0xA5,
    0xDE,
    0x4D,
    0x88,
    0xC7,
    0x5A,
    0xD2,
    0x4B,
    0x1C
)
DEVPKEY_DeviceClass_Characteristics = DEFINE_DEVPROPKEY(
    0x4321918B,
    0xF69E,
    0x470D,
    0xA5,
    0xDE,
    0x4D,
    0x88,
    0xC7,
    0x5A,
    0xD2,
    0x4B,
    0x1D
)

# Device setup class properties

# DEVPROP_TYPE_STRING
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceClass_Name = DEFINE_DEVPROPKEY(
    0x259ABFFC,
    0x50A7,
    0x47CE,
    0xAF,
    0x8,
    0x68,
    0xC9,
    0xA7,
    0xD7,
    0x33,
    0x66,
    0x2
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceClass_ClassName = DEFINE_DEVPROPKEY(
    0x259ABFFC,
    0x50A7,
    0x47CE,
    0xAF,
    0x8,
    0x68,
    0xC9,
    0xA7,
    0xD7,
    0x33,
    0x66,
    0x3
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceClass_Icon = DEFINE_DEVPROPKEY(
    0x259ABFFC,
    0x50A7,
    0x47CE,
    0xAF,
    0x8,
    0x68,
    0xC9,
    0xA7,
    0xD7,
    0x33,
    0x66,
    0x4
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceClass_ClassInstaller = DEFINE_DEVPROPKEY(
    0x259ABFFC,
    0x50A7,
    0x47CE,
    0xAF,
    0x8,
    0x68,
    0xC9,
    0xA7,
    0xD7,
    0x33,
    0x66,
    0x5
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceClass_PropPageProvider = DEFINE_DEVPROPKEY(
    0x259ABFFC,
    0x50A7,
    0x47CE,
    0xAF,
    0x8,
    0x68,
    0xC9,
    0xA7,
    0xD7,
    0x33,
    0x66,
    0x6
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceClass_NoInstallClass = DEFINE_DEVPROPKEY(
    0x259ABFFC,
    0x50A7,
    0x47CE,
    0xAF,
    0x8,
    0x68,
    0xC9,
    0xA7,
    0xD7,
    0x33,
    0x66,
    0x7
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceClass_NoDisplayClass = DEFINE_DEVPROPKEY(
    0x259ABFFC,
    0x50A7,
    0x47CE,
    0xAF,
    0x8,
    0x68,
    0xC9,
    0xA7,
    0xD7,
    0x33,
    0x66,
    0x8
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceClass_SilentInstall = DEFINE_DEVPROPKEY(
    0x259ABFFC,
    0x50A7,
    0x47CE,
    0xAF,
    0x8,
    0x68,
    0xC9,
    0xA7,
    0xD7,
    0x33,
    0x66,
    0x9
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceClass_NoUseClass = DEFINE_DEVPROPKEY(
    0x259ABFFC,
    0x50A7,
    0x47CE,
    0xAF,
    0x8,
    0x68,
    0xC9,
    0xA7,
    0xD7,
    0x33,
    0x66,
    0xA
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceClass_DefaultService = DEFINE_DEVPROPKEY(
    0x259ABFFC,
    0x50A7,
    0x47CE,
    0xAF,
    0x8,
    0x68,
    0xC9,
    0xA7,
    0xD7,
    0x33,
    0x66,
    0xB
)

DEVPKEY_DeviceClass_IconPath = DEFINE_DEVPROPKEY(
    0x259ABFFC,
    0x50A7,
    0x47CE,
    0xAF,
    0x8,
    0x68,
    0xC9,
    0xA7,
    0xD7,
    0x33,
    0x66,
    0xC
)
# Other Device setup class properties

# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceClass_DHPRebalanceOptOut = DEFINE_DEVPROPKEY(
    0xD14D3EF3,
    0x66CF,
    0x4BA2,
    0x9D,
    0x38,
    0x0D,
    0xDB,
    0x37,
    0xAB,
    0x47,
    0x01,
    0x2
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceClass_ClassCoInstallers = DEFINE_DEVPROPKEY(
    0x713D1703,
    0xA2E2,
    0x49F5,
    0x92,
    0x14,
    0x56,
    0x47,
    0x2E,
    0xF3,
    0xDA,
    0x5C,
    0x2
)

# Device INTerface properties

# DEVPROP_TYPE_STRING
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceInterface_FriendlyName = DEFINE_DEVPROPKEY(
    0x026E516E,
    0xB814,
    0x414B,
    0x83,
    0xCD,
    0x85,
    0x6D,
    0x6F,
    0xEF,
    0x48,
    0x22,
    0x2
)
# DEVPROP_TYPE_GUID
DEVPKEY_DeviceInterface_Enabled = DEFINE_DEVPROPKEY(
    0x026E516E,
    0xB814,
    0x414B,
    0x83,
    0xCD,
    0x85,
    0x6D,
    0x6F,
    0xEF,
    0x48,
    0x22,
    0x3
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceInterface_ClassGuid = DEFINE_DEVPROPKEY(
    0x026E516E,
    0xB814,
    0x414B,
    0x83,
    0xCD,
    0x85,
    0x6D,
    0x6F,
    0xEF,
    0x48,
    0x22,
    0x4
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceInterface_ReferenceString = DEFINE_DEVPROPKEY(
    0x026E516E,
    0xB814,
    0x414B,
    0x83,
    0xCD,
    0x85,
    0x6D,
    0x6F,
    0xEF,
    0x48,
    0x22,
    0x5
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceInterface_Restricted = DEFINE_DEVPROPKEY(
    0x026E516E,
    0xB814,
    0x414B,
    0x83,
    0xCD,
    0x85,
    0x6D,
    0x6F,
    0xEF,
    0x48,
    0x22,
    0x6
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities = DEFINE_DEVPROPKEY(
    0x026E516E,
    0xB814,
    0x414B,
    0x83,
    0xCD,
    0x85,
    0x6D,
    0x6F,
    0xEF,
    0x48,
    0x22,
    0x8
)
DEVPKEY_DeviceInterface_SchematicName = DEFINE_DEVPROPKEY(
    0x026E516E,
    0xB814,
    0x414B,
    0x83,
    0xCD,
    0x85,
    0x6D,
    0x6F,
    0xEF,
    0x48,
    0x22,
    0x9
)

# Device INTerface class properties

# DEVPROP_TYPE_STRING
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceInterfaceClass_DefaultInterface = DEFINE_DEVPROPKEY(
    0x14C83A99,
    0x0B3F,
    0x44B7,
    0xBE,
    0x4C,
    0xA1,
    0x78,
    0xD3,
    0x99,
    0x05,
    0x64,
    0x2
)
DEVPKEY_DeviceInterfaceClass_Name = DEFINE_DEVPROPKEY(
    0x14C83A99,
    0x0B3F,
    0x44B7,
    0xBE,
    0x4C,
    0xA1,
    0x78,
    0xD3,
    0x99,
    0x05,
    0x64,
    0x3
)

# Device Container Properties

# DEVPROP_TYPE_STRING | DEVPROP_TYPE_STRING_LIST
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceContainer_Address = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x33
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_DiscoveryMethod = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x34
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_IsEncrypted = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x35
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_IsAuthenticated = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x36
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_IsConnected = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x37
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceContainer_IsPaired = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x38
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceContainer_Icon = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x39
)
# DEVPROP_TYPE_FILETIME
DEVPKEY_DeviceContainer_Version = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x41
)
# DEVPROP_TYPE_FILETIME
DEVPKEY_DeviceContainer_Last_Seen = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x42
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_Last_Connected = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x43
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_IsShowInDisconnectedState = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x44
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceContainer_IsLocalMachine = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x46
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_MetadataPath = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x47
)
# DEVPROP_TYPE_BINARY
DEVPKEY_DeviceContainer_IsMetadataSearchInProgress = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x48
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_MetadataChecksum = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x49
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_IsNotInterestingForDisplay = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x4A
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_LaunchDeviceStageOnDeviceConnect = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x4C
)
# DEVPROP_TYPE_GUID
DEVPKEY_DeviceContainer_LaunchDeviceStageFromExplorer = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x4D
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_BaselineExperienceId = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x4E
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceContainer_IsDeviceUniquelyIdentifiable = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x4F
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceContainer_AssociationArray = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x50
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceContainer_DeviceDescription1 = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x51
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_DeviceDescription2 = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x52
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_HasProblem = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x53
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_IsSharedDevice = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x54
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_IsNetworkDevice = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x55
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceContainer_IsDefaultDevice = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x56
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_MetadataCabinet = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x57
)
# DEVPROP_TYPE_GUID
DEVPKEY_DeviceContainer_RequiresPairingElevation = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x58
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceContainer_ExperienceId = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x59
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceContainer_Category = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x5A
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceContainer_Category_Desc_Singular = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x5B
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceContainer_Category_Desc_Plural = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x5C
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceContainer_Category_Icon = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x5D
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceContainer_CategoryGroup_Desc = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x5E
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceContainer_CategoryGroup_Icon = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x5F
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_PrimaryCategory = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x61
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_UnpairUninstall = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x62
)
# DEVPROP_TYPE_UINT32
DEVPKEY_DeviceContainer_RequiresUninstallElevation = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x63
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_DeviceFunctionSubRank = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x64
)
# DEVPROP_TYPE_UINT32
DEVPKEY_DeviceContainer_AlwaysShowDeviceAsConnected = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x65
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceContainer_ConfigFlags = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x69
)
# DEVPROP_TYPE_STRING_LIST
DEVPKEY_DeviceContainer_PrivilegedPackageFamilyNames = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x6A
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_CustomPrivilegedPackageFamilyNames = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x6B
)
DEVPKEY_DeviceContainer_IsRebootRequired = DEFINE_DEVPROPKEY(
    0x78C34FC8,
    0x104A,
    0x4ACA,
    0x9E,
    0xA4,
    0x52,
    0x4D,
    0x52,
    0x99,
    0x6E,
    0x57,
    0x6C
)
# DEVPROP_TYPE_STRING
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceContainer_FriendlyName = DEFINE_DEVPROPKEY(
    0x656A3BB3,
    0xECC0,
    0x43FD,
    0x84,
    0x77,
    0x4A,
    0xE0,
    0x40,
    0x4A,
    0x96,
    0xCD,
    0x3000
)
# DEVPROP_TYPE_STRING (localizable)
DEVPKEY_DeviceContainer_Manufacturer = DEFINE_DEVPROPKEY(
    0x656A3BB3,
    0xECC0,
    0x43FD,
    0x84,
    0x77,
    0x4A,
    0xE0,
    0x40,
    0x4A,
    0x96,
    0xCD,
    0x2000
)
# DEVPROP_TYPE_STRING
DEVPKEY_DeviceContainer_ModelName = DEFINE_DEVPROPKEY(
    0x656A3BB3,
    0xECC0,
    0x43FD,
    0x84,
    0x77,
    0x4A,
    0xE0,
    0x40,
    0x4A,
    0x96,
    0xCD,
    0x2002
)
DEVPKEY_DeviceContainer_ModelNumber = DEFINE_DEVPROPKEY(
    0x656A3BB3,
    0xECC0,
    0x43FD,
    0x84,
    0x77,
    0x4A,
    0xE0,
    0x40,
    0x4A,
    0x96,
    0xCD,
    0x2003
)
# DEVPROP_TYPE_BOOLEAN
DEVPKEY_DeviceContainer_InstallInProgress = DEFINE_DEVPROPKEY(
    0x83DA6326,
    0x97A6,
    0x4088,
    0x94,
    0x53,
    0xA1,
    0x92,
    0x3F,
    0x57,
    0x3B,
    0x29,
    0x9
)

# DeviceContainer properties that can be set on a devnode.
# These used to be defined as DeviceDisplay

DEVPKEY_DeviceDisplay_DiscoveryMethod = (
    DEVPKEY_DeviceContainer_DiscoveryMethod
)
DEVPKEY_DeviceDisplay_IsShowInDisconnectedState = (
    DEVPKEY_DeviceContainer_IsShowInDisconnectedState
)
DEVPKEY_DeviceDisplay_IsNotInterestingForDisplay = (
    DEVPKEY_DeviceContainer_IsNotInterestingForDisplay
)
DEVPKEY_DeviceDisplay_IsNetworkDevice = DEVPKEY_DeviceContainer_IsNetworkDevice
DEVPKEY_DeviceDisplay_Category = DEVPKEY_DeviceContainer_Category
DEVPKEY_DeviceDisplay_UnpairUninstall = DEVPKEY_DeviceContainer_UnpairUninstall
DEVPKEY_DeviceDisplay_RequiresUninstallElevation = (
    DEVPKEY_DeviceContainer_RequiresUninstallElevation
)
DEVPKEY_DeviceDisplay_AlwaysShowDeviceAsConnected = (
    DEVPKEY_DeviceContainer_AlwaysShowDeviceAsConnected
)

# DevQuery properties

# DEVPROP_TYPE_UINT32
DEVPKEY_DevQuery_ObjectType = DEFINE_DEVPROPKEY(
    0x13673F42,
    0xA3D6,
    0x49F6,
    0xB4,
    0xDA,
    0xAE,
    0x46,
    0xE0,
    0xC5,
    0x23,
    0x7C,
    0x2
)
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

__all__ = (
    'DEVPKEY_DevQuery_ObjectType', 'DEVPKEY_DeviceClass_Characteristics',
    'DEVPKEY_DeviceClass_ClassCoInstallers', 'DEVPKEY_DeviceClass_ClassName',
    'DEVPKEY_DeviceClass_ClassInstaller', 'DEVPKEY_DeviceClass_DevType',
    'DEVPKEY_DeviceClass_DHPRebalanceOptOut', 'DEVPKEY_DeviceClass_Exclusive',
    'DEVPKEY_DeviceClass_DefaultService', 'DEVPKEY_DeviceClass_Icon',
    'DEVPKEY_DeviceClass_IconPath', 'DEVPKEY_DeviceClass_LowerFilters',
    'DEVPKEY_DeviceClass_Name', 'DEVPKEY_DeviceClass_NoDisplayClass',
    'DEVPKEY_DeviceClass_NoInstallClass', 'DEVPKEY_DeviceClass_NoUseClass',
    'DEVPKEY_DeviceClass_PropPageProvider', 'DEVPKEY_DeviceClass_Security',
    'DEVPKEY_DeviceClass_SecuritySDS', 'DEVPKEY_DeviceClass_SilentInstall',
    'DEVPKEY_DeviceClass_UpperFilters', 'DEVPKEY_DeviceContainer_Address',
    'DEVPKEY_DeviceContainer_AlwaysShowDeviceAsConnected', 'DEVPKEY_NAME',
    'DEVPKEY_DeviceContainer_AssociationArray', 'DEVPKEY_Device_Address',
    'DEVPKEY_DeviceContainer_BaselineExperienceId', 'DEVPKEY_Device_Children',
    'DEVPKEY_DeviceContainer_Category', 'DEVPKEY_DeviceContainer_ConfigFlags',
    'DEVPKEY_DeviceContainer_CategoryGroup_Desc', 'DEVPKEY_Device_BusNumber',
    'DEVPKEY_DeviceContainer_CategoryGroup_Icon', 'DEVPKEY_Device_Class',
    'DEVPKEY_DeviceContainer_Category_Desc_Plural', 'DEVPKEY_Device_DevType',
    'DEVPKEY_DeviceContainer_Category_Desc_Singular', 'DEVPKEY_Device_Driver',
    'DEVPKEY_DeviceContainer_Category_Icon', 'DEVPKEY_DeviceContainer_Icon',
    'DEVPKEY_DeviceContainer_CustomPrivilegedPackageFamilyNames',
    'DEVPKEY_DeviceContainer_DeviceDescription1', 'DEVPKEY_Device_ClassGuid',
    'DEVPKEY_DeviceContainer_DeviceDescription2', 'DEVPKEY_Device_DeviceDesc',
    'DEVPKEY_DeviceContainer_DeviceFunctionSubRank', 'DEVPKEY_Device_Legacy',
    'DEVPKEY_DeviceContainer_DiscoveryMethod', 'DEVPKEY_Device_BusRelations',
    'DEVPKEY_DeviceContainer_ExperienceId', 'DEVPKEY_DeviceContainer_Version',
    'DEVPKEY_DeviceContainer_FriendlyName', 'DEVPKEY_DeviceDisplay_Category',
    'DEVPKEY_DeviceContainer_HasProblem', 'DEVPKEY_DeviceContainer_IsPaired',
    'DEVPKEY_DeviceContainer_InstallInProgress', 'DEVPKEY_Device_BusTypeGuid',
    'DEVPKEY_DeviceContainer_IsAuthenticated', 'DEVPKEY_Device_Capabilities',
    'DEVPKEY_DeviceContainer_IsConnected', 'DEVPKEY_DeviceInterface_Enabled',
    'DEVPKEY_DeviceContainer_IsDefaultDevice', 'DEVPKEY_Device_CompatibleIds',
    'DEVPKEY_DeviceContainer_IsDeviceUniquelyIdentifiable',
    'DEVPKEY_DeviceContainer_IsEncrypted', 'DEVPKEY_Device_BaseContainerId',
    'DEVPKEY_DeviceContainer_IsLocalMachine', 'DEVPKEY_Device_BiosDeviceName',
    'DEVPKEY_DeviceContainer_IsMetadataSearchInProgress',
    'DEVPKEY_DeviceContainer_IsNetworkDevice', 'DEVPKEY_Device_ConfigFlags',
    'DEVPKEY_DeviceContainer_IsNotInterestingForDisplay',
    'DEVPKEY_DeviceContainer_IsRebootRequired', 'DEVPKEY_Device_ContainerId',
    'DEVPKEY_DeviceContainer_IsSharedDevice', 'DEVPKEY_Device_DebuggerSafe',
    'DEVPKEY_DeviceContainer_IsShowInDisconnectedState',
    'DEVPKEY_DeviceContainer_Last_Connected', 'DEVPKEY_Device_DevNodeStatus',
    'DEVPKEY_DeviceContainer_Last_Seen', 'DEVPKEY_DeviceContainer_ModelName',
    'DEVPKEY_DeviceContainer_LaunchDeviceStageFromExplorer',
    'DEVPKEY_DeviceContainer_LaunchDeviceStageOnDeviceConnect',
    'DEVPKEY_DeviceContainer_Manufacturer', 'DEVPKEY_Device_Characteristics',
    'DEVPKEY_DeviceContainer_MetadataCabinet', 'DEVPKEY_Device_DriverDate',
    'DEVPKEY_DeviceContainer_MetadataChecksum', 'DEVPKEY_Device_DriverDesc',
    'DEVPKEY_DeviceContainer_MetadataPath', 'DEVPKEY_Device_ConfigurationId',
    'DEVPKEY_DeviceContainer_ModelNumber', 'DEVPKEY_Device_DriverInfPath',
    'DEVPKEY_DeviceContainer_PrimaryCategory', 'DEVPKEY_Device_DriverRank',
    'DEVPKEY_DeviceContainer_PrivilegedPackageFamilyNames',
    'DEVPKEY_DeviceContainer_RequiresPairingElevation', 'DEVPKEY_DrvPkg_Icon',
    'DEVPKEY_DeviceContainer_RequiresUninstallElevation',
    'DEVPKEY_DeviceContainer_UnpairUninstall', 'DEVPKEY_Device_DriverVersion',
    'DEVPKEY_DeviceDisplay_AlwaysShowDeviceAsConnected',
    'DEVPKEY_DeviceDisplay_DiscoveryMethod', 'DEVPKEY_Device_DriverLogoLevel',
    'DEVPKEY_DeviceDisplay_IsNetworkDevice', 'DEVPKEY_Device_DriverProvider',
    'DEVPKEY_DeviceDisplay_IsNotInterestingForDisplay',
    'DEVPKEY_DeviceDisplay_IsShowInDisconnectedState', 'DEVPKEY_Device_Model',
    'DEVPKEY_DeviceDisplay_RequiresUninstallElevation',
    'DEVPKEY_DeviceDisplay_UnpairUninstall', 'DEVPKEY_Device_EnumeratorName',
    'DEVPKEY_DeviceInterfaceClass_DefaultInterface', 'DEVPKEY_Device_ModelId',
    'DEVPKEY_DeviceInterfaceClass_Name', 'DEVPKEY_DeviceInterface_ClassGuid',
    'DEVPKEY_DeviceInterface_FriendlyName', 'DEVPKEY_Device_DriverInfSection',
    'DEVPKEY_DeviceInterface_ReferenceString', 'DEVPKEY_Device_Exclusive',
    'DEVPKEY_DeviceInterface_Restricted', 'DEVPKEY_Device_DriverCoInstallers',
    'DEVPKEY_DeviceInterface_SchematicName', 'DEVPKEY_Device_ExtendedAddress',
    'DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities',
    'DEVPKEY_Device_AdditionalSoftwareRequested', 'DEVPKEY_Device_HasProblem',
    'DEVPKEY_Device_BusReportedDeviceDesc', 'DEVPKEY_Device_FirmwareDate',
    'DEVPKEY_Device_DHP_Rebalance_Policy', 'DEVPKEY_Device_DriverProblemDesc',
    'DEVPKEY_Device_DependencyDependents', 'DEVPKEY_Device_EjectionRelations',
    'DEVPKEY_Device_DependencyProviders', 'DEVPKEY_Device_FirmwareRevision',
    'DEVPKEY_Device_DriverInfSectionExt', 'DEVPKEY_Device_FirmwareVersion',
    'DEVPKEY_Device_DriverPropPageProvider', 'DEVPKEY_Device_FriendlyName',
    'DEVPKEY_Device_ExtendedConfigurationIds', 'DEVPKEY_Device_HardwareIds',
    'DEVPKEY_Device_FirstInstallDate', 'DEVPKEY_Device_InstallDate',
    'DEVPKEY_Device_FriendlyNameAttributes', 'DEVPKEY_Device_InstallState',
    'DEVPKEY_Device_GenericDriverInstalled', 'DEVPKEY_Device_InstanceId',
    'DEVPKEY_Device_InLocalMachineContainer', 'DEVPKEY_Device_IsPresent',
    'DEVPKEY_Device_IsAssociateableByUserAction', 'DEVPKEY_Device_Numa_Node',
    'DEVPKEY_Device_IsRebootRequired', 'DEVPKEY_Device_LastArrivalDate',
    'DEVPKEY_Device_LastRemovalDate', 'DEVPKEY_Device_LegacyBusType',
    'DEVPKEY_Device_LocationInfo', 'DEVPKEY_Device_LocationPaths',
    'DEVPKEY_Device_LowerFilters', 'DEVPKEY_Device_Manufacturer',
    'DEVPKEY_Device_ManufacturerAttributes', 'DEVPKEY_Device_NoConnectSound',
    'DEVPKEY_Device_MatchingDeviceId', 'DEVPKEY_Device_Numa_Proximity_Domain',
    'DEVPKEY_Device_PDOName', 'DEVPKEY_Device_Parent', 'DEVPKEY_Device_Stack',
    'DEVPKEY_Device_PhysicalDeviceLocation', 'DEVPKEY_Device_PowerData',
    'DEVPKEY_Device_PostInstallInProgress', 'DEVPKEY_Device_PowerRelations',
    'DEVPKEY_Device_PresenceNotForDevice', 'DEVPKEY_Device_ProblemCode',
    'DEVPKEY_Device_ProblemStatus', 'DEVPKEY_Device_RemovalPolicy',
    'DEVPKEY_Device_RemovalPolicyDefault', 'DEVPKEY_Device_RemovalRelations',
    'DEVPKEY_Device_RemovalPolicyOverride', 'DEVPKEY_Device_Reported',
    'DEVPKEY_Device_ReportedDeviceIdsHash', 'DEVPKEY_Device_Security',
    'DEVPKEY_Device_ResourcePickerExceptions', 'DEVPKEY_Device_SecuritySDS',
    'DEVPKEY_Device_ResourcePickerTags', 'DEVPKEY_Device_SafeRemovalRequired',
    'DEVPKEY_Device_SafeRemovalRequiredOverride', 'DEVPKEY_Device_Service',
    'DEVPKEY_Device_SessionId', 'DEVPKEY_Device_ShowInUninstallUI',
    'DEVPKEY_Device_Siblings', 'DEVPKEY_Device_SignalStrength',
    'DEVPKEY_Device_SoftRestartSupported', 'DEVPKEY_Device_UINumber',
    'DEVPKEY_Device_TransportRelations', 'DEVPKEY_Device_UINumberDescFormat',
    'DEVPKEY_Device_UpperFilters', 'DEVPKEY_DrvPkg_BrandingIcon',
    'DEVPKEY_DrvPkg_DetailedDescription', 'DEVPKEY_DrvPkg_DocumentationLink',
    'DEVPKEY_DrvPkg_Model', 'DEVPKEY_DrvPkg_VendorWebSite',
    'DEVPKEY_Numa_Proximity_Domain',
)
