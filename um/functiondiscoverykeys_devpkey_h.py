

from .propkeydef_h import (
    DEFINE_PROPERTYKEY,
)

from .winapifamily_h import * # NOQA

# _NAME

# DEVPROP_TYPE_STRING
PKEY_NAME = DEFINE_PROPERTYKEY(
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
# These PKEYs correspond to the old setupapi SPDRP_XXX properties

# DEVPROP_TYPE_STRING
# DEVPROP_TYPE_STRING_LIST
PKEY_Device_DeviceDesc = DEFINE_PROPERTYKEY(
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
PKEY_Device_HardwareIds = DEFINE_PROPERTYKEY(
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
PKEY_Device_CompatibleIds = DEFINE_PROPERTYKEY(
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
PKEY_Device_Service = DEFINE_PROPERTYKEY(
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
PKEY_Device_Class = DEFINE_PROPERTYKEY(
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
PKEY_Device_ClassGuid = DEFINE_PROPERTYKEY(
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
PKEY_Device_Driver = DEFINE_PROPERTYKEY(
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
PKEY_Device_ConfigFlags = DEFINE_PROPERTYKEY(
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
PKEY_Device_Manufacturer = DEFINE_PROPERTYKEY(
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
PKEY_Device_FriendlyName = DEFINE_PROPERTYKEY(
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
PKEY_Device_LocationInfo = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_UNINT32
PKEY_Device_PDOName = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_STRING
PKEY_Device_Capabilities = DEFINE_PROPERTYKEY(
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
PKEY_Device_UINumber = DEFINE_PROPERTYKEY(
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
PKEY_Device_UpperFilters = DEFINE_PROPERTYKEY(
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
PKEY_Device_LowerFilters = DEFINE_PROPERTYKEY(
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
PKEY_Device_BusTypeGuid = DEFINE_PROPERTYKEY(
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
PKEY_Device_LegacyBusType = DEFINE_PROPERTYKEY(
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
PKEY_Device_BusNumber = DEFINE_PROPERTYKEY(
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
PKEY_Device_EnumeratorName = DEFINE_PROPERTYKEY(
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
PKEY_Device_Security = DEFINE_PROPERTYKEY(
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
PKEY_Device_SecuritySDS = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_UINT32
PKEY_Device_DevType = DEFINE_PROPERTYKEY(
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
PKEY_Device_Exclusive = DEFINE_PROPERTYKEY(
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
PKEY_Device_Characteristics = DEFINE_PROPERTYKEY(
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
PKEY_Device_Address = DEFINE_PROPERTYKEY(
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
PKEY_Device_UINumberDescFormat = DEFINE_PROPERTYKEY(
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
PKEY_Device_PowerData = DEFINE_PROPERTYKEY(
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
PKEY_Device_RemovalPolicy = DEFINE_PROPERTYKEY(
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
PKEY_Device_RemovalPolicyDefault = DEFINE_PROPERTYKEY(
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
PKEY_Device_RemovalPolicyOverride = DEFINE_PROPERTYKEY(
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
PKEY_Device_InstallState = DEFINE_PROPERTYKEY(
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
PKEY_Device_LocationPaths = DEFINE_PROPERTYKEY(
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
PKEY_Device_BaseContainerId = DEFINE_PROPERTYKEY(
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

# Device properties
# These PKEYs correspond to a device's status and problem code

# DEVPROP_TYPE_UINT32
# DEVPROP_TYPE_UINT32
PKEY_Device_DevNodeStatus = DEFINE_PROPERTYKEY(
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
PKEY_Device_ProblemCode = DEFINE_PROPERTYKEY(
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
# These PKEYs correspond to device relations

# DEVPROP_TYPE_STRING_LIST
# DEVPROP_TYPE_STRING_LIST
PKEY_Device_EjectionRelations = DEFINE_PROPERTYKEY(
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
PKEY_Device_RemovalRelations = DEFINE_PROPERTYKEY(
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
PKEY_Device_PowerRelations = DEFINE_PROPERTYKEY(
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
PKEY_Device_BusRelations = DEFINE_PROPERTYKEY(
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
PKEY_Device_Parent = DEFINE_PROPERTYKEY(
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
PKEY_Device_Children = DEFINE_PROPERTYKEY(
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
PKEY_Device_Siblings = DEFINE_PROPERTYKEY(
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
PKEY_Device_TransportRelations = DEFINE_PROPERTYKEY(
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

# Other Device properties

# DEVPROP_TYPE_BOOLEAN
# DEVPROP_TYPE_BOOLEAN
PKEY_Device_Reported = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_STRING
PKEY_Device_Legacy = DEFINE_PROPERTYKEY(
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
PKEY_Device_InstanceId = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_GUID
PKEY_Device_ContainerId = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_GUID
PKEY_Device_ModelId = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_UINT32
PKEY_Device_FriendlyNameAttributes = DEFINE_PROPERTYKEY(
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
PKEY_Device_ManufacturerAttributes = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_BOOLEAN
# DEVPROP_TYPE_UINT32
PKEY_Device_PresenceNotForDevice = DEFINE_PROPERTYKEY(
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
PKEY_Device_SignalStrength = DEFINE_PROPERTYKEY(
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
PKEY_Device_IsAssociateableByUserAction = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_UINT32
# DEVPROP_TYPE_UINT32
PKEY_Numa_Proximity_Domain = DEFINE_PROPERTYKEY(
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
PKEY_Device_DHP_Rebalance_Policy = DEFINE_PROPERTYKEY(
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
PKEY_Device_Numa_Node = DEFINE_PROPERTYKEY(
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
PKEY_Device_BusReportedDeviceDesc = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_BOOLEAN
PKEY_Device_InstallInProgress = DEFINE_PROPERTYKEY(
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

# Device driver properties

# DEVPROP_TYPE_FILETIME
# DEVPROP_TYPE_STRING
PKEY_Device_DriverDate = DEFINE_PROPERTYKEY(
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
PKEY_Device_DriverVersion = DEFINE_PROPERTYKEY(
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
PKEY_Device_DriverDesc = DEFINE_PROPERTYKEY(
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
PKEY_Device_DriverInfPath = DEFINE_PROPERTYKEY(
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
PKEY_Device_DriverInfSection = DEFINE_PROPERTYKEY(
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
PKEY_Device_DriverInfSectionExt = DEFINE_PROPERTYKEY(
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
PKEY_Device_MatchingDeviceId = DEFINE_PROPERTYKEY(
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
PKEY_Device_DriverProvider = DEFINE_PROPERTYKEY(
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
PKEY_Device_DriverPropPageProvider = DEFINE_PROPERTYKEY(
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
PKEY_Device_DriverCoInstallers = DEFINE_PROPERTYKEY(
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
PKEY_Device_ResourcePickerTags = DEFINE_PROPERTYKEY(
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
PKEY_Device_ResourcePickerExceptions = DEFINE_PROPERTYKEY(
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
PKEY_Device_DriverRank = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_BOOLEAN
PKEY_Device_DriverLogoLevel = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_BOOLEAN
PKEY_Device_NoConnectSound = DEFINE_PROPERTYKEY(
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
PKEY_Device_GenericDriverInstalled = DEFINE_PROPERTYKEY(
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
PKEY_Device_AdditionalSoftwareRequested = DEFINE_PROPERTYKEY(
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
PKEY_Device_SafeRemovalRequired = DEFINE_PROPERTYKEY(
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
PKEY_Device_SafeRemovalRequiredOverride = DEFINE_PROPERTYKEY(
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

# Device properties that were set by the driver package that was installed
# on the device.

# DEVPROP_TYPE_STRING
# DEVPROP_TYPE_STRING
PKEY_DrvPkg_Model = DEFINE_PROPERTYKEY(
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
PKEY_DrvPkg_VendorWebSite = DEFINE_PROPERTYKEY(
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
PKEY_DrvPkg_DetailedDescription = DEFINE_PROPERTYKEY(
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
PKEY_DrvPkg_DocumentationLink = DEFINE_PROPERTYKEY(
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
PKEY_DrvPkg_Icon = DEFINE_PROPERTYKEY(
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
PKEY_DrvPkg_BrandingIcon = DEFINE_PROPERTYKEY(
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
# These PKEYs correspond to the old setupapi SPCRP_XXX properties

# DEVPROP_TYPE_STRING_LIST
# DEVPROP_TYPE_STRING_LIST
PKEY_DeviceClass_UpperFilters = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_LowerFilters = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_Security = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_SecuritySDS = DEFINE_PROPERTYKEY(
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
# DEVPROP_TYPE_UINT32
PKEY_DeviceClass_DevType = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_Exclusive = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_Characteristics = DEFINE_PROPERTYKEY(
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
# These PKEYs correspond to registry values under the device class GUID key

# DEVPROP_TYPE_STRING
# DEVPROP_TYPE_STRING
PKEY_DeviceClass_Name = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_ClassName = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_Icon = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_ClassInstaller = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_PropPageProvider = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_NoInstallClass = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_NoDisplayClass = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_SilentInstall = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_NoUseClass = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_DefaultService = DEFINE_PROPERTYKEY(
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
PKEY_DeviceClass_IconPath = DEFINE_PROPERTYKEY(
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

# DEVPROP_TYPE_STRING_LIST
PKEY_DeviceClass_ClassCoInstallers = DEFINE_PROPERTYKEY(
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
PKEY_DeviceInterface_FriendlyName = DEFINE_PROPERTYKEY(
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
PKEY_DeviceInterface_Enabled = DEFINE_PROPERTYKEY(
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
PKEY_DeviceInterface_ClassGuid = DEFINE_PROPERTYKEY(
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

# Device INTerface class properties

# DEVPROP_TYPE_STRING
PKEY_DeviceInterfaceClass_DefaultInterface = DEFINE_PROPERTYKEY(
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
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

__all__ = (
    'PKEY_Device_DriverLogoLevel', 'PKEY_Device_BusRelations', 'PKEY_NAME',
    'PKEY_Device_LocationPaths', 'PKEY_Device_ModelId', 'PKEY_Device_Driver',
    'PKEY_Device_Exclusive', 'PKEY_Device_UpperFilters', 'PKEY_Device_Legacy',
    'PKEY_DeviceInterface_FriendlyName', 'PKEY_DeviceInterface_Enabled',
    'PKEY_DeviceClass_ClassName', 'PKEY_Device_GenericDriverInstalled',
    'PKEY_Device_DriverRank', 'PKEY_Device_DriverInfPath', 'PKEY_DrvPkg_Icon',
    'PKEY_Device_Capabilities', 'PKEY_Device_SafeRemovalRequired',
    'PKEY_Device_InstallInProgress', 'PKEY_Device_BusReportedDeviceDesc',
    'PKEY_Device_AdditionalSoftwareRequested', 'PKEY_Device_BusNumber',
    'PKEY_DeviceClass_PropPageProvider', 'PKEY_Device_EjectionRelations',
    'PKEY_DeviceClass_NoUseClass', 'PKEY_Device_DriverVersion',
    'PKEY_DeviceInterface_ClassGuid', 'PKEY_DrvPkg_DetailedDescription',
    'PKEY_Device_Reported', 'PKEY_Device_MatchingDeviceId',
    'PKEY_DeviceClass_Exclusive', 'PKEY_Device_BaseContainerId',
    'PKEY_DeviceClass_ClassCoInstallers', 'PKEY_Device_NoConnectSound',
    'PKEY_Device_ManufacturerAttributes', 'PKEY_Device_PresenceNotForDevice',
    'PKEY_Device_ResourcePickerExceptions', 'PKEY_DrvPkg_Model',
    'PKEY_Device_ClassGuid', 'PKEY_DeviceClass_DefaultService',
    'PKEY_Device_DriverInfSectionExt', 'PKEY_DeviceClass_Characteristics',
    'PKEY_Device_PDOName', 'PKEY_Device_RemovalPolicyDefault',
    'PKEY_DrvPkg_VendorWebSite', 'PKEY_DrvPkg_DocumentationLink',
    'PKEY_Device_TransportRelations', 'PKEY_Device_PowerData',
    'PKEY_DeviceClass_Icon', 'PKEY_Device_InstallState', 'PKEY_Device_Parent',
    'PKEY_Numa_Proximity_Domain', 'PKEY_DeviceClass_LowerFilters',
    'PKEY_Device_Address', 'PKEY_Device_ProblemCode', 'PKEY_Device_Siblings',
    'PKEY_DeviceClass_Security', 'PKEY_Device_LegacyBusType',
    'PKEY_Device_SignalStrength', 'PKEY_Device_DriverProvider',
    'PKEY_DeviceClass_ClassInstaller', 'PKEY_Device_Security',
    'PKEY_Device_RemovalPolicyOverride', 'PKEY_Device_SecuritySDS',
    'PKEY_DeviceClass_SilentInstall', 'PKEY_Device_DriverDate',
    'PKEY_Device_Characteristics', 'PKEY_Device_CompatibleIds',
    'PKEY_DeviceClass_UpperFilters', 'PKEY_DeviceClass_NoDisplayClass',
    'PKEY_Device_Manufacturer', 'PKEY_Device_UINumber', 'PKEY_Device_Class',
    'PKEY_DrvPkg_BrandingIcon', 'PKEY_Device_LowerFilters',
    'PKEY_Device_FriendlyName', 'PKEY_Device_ConfigFlags',
    'PKEY_DeviceClass_Name', 'PKEY_Device_ResourcePickerTags',
    'PKEY_Device_HardwareIds', 'PKEY_DeviceInterfaceClass_DefaultInterface',
    'PKEY_Device_BusTypeGuid', 'PKEY_Device_LocationInfo',
    'PKEY_Device_FriendlyNameAttributes', 'PKEY_Device_RemovalRelations',
    'PKEY_Device_DriverCoInstallers', 'PKEY_DeviceClass_DevType',
    'PKEY_Device_DriverPropPageProvider', 'PKEY_Device_Numa_Node',
    'PKEY_Device_DriverDesc', 'PKEY_DeviceClass_NoInstallClass',
    'PKEY_Device_EnumeratorName', 'PKEY_Device_Service',
    'PKEY_Device_DriverInfSection', 'PKEY_DeviceClass_IconPath',
    'PKEY_Device_DeviceDesc', 'PKEY_Device_ContainerId',
    'PKEY_Device_Children', 'PKEY_Device_IsAssociateableByUserAction',
    'PKEY_Device_DHP_Rebalance_Policy', 'PKEY_Device_PowerRelations',
    'PKEY_Device_SafeRemovalRequiredOverride', 'PKEY_DeviceClass_SecuritySDS',
    'PKEY_Device_UINumberDescFormat', 'PKEY_Device_DevNodeStatus',
    'PKEY_Device_RemovalPolicy', 'PKEY_Device_DevType',
    'PKEY_Device_InstanceId',
)
