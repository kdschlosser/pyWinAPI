from pyWinAPI import *
from pyWinAPI.shared.guiddef_h import *


# ***************************************************************************\
# *   * * coguid.h - Master definition of GUIDs for compobj.dll * *   * * OLE
# Version 2.0 * * * * Copyright (c) Microsoft Corporation. All rights
# reserved. * * *
# \***************************************************************************
# this file is the master definition of all GUIDs for the component object
# model and is included in compobj.h. Some GUIDs for moinkers and storage
# appear here as well. All of these GUIDs are OLE GUIDs only in the sense that
# part of the GUID range owned by OLE was used to define them. NOTE: The
# second byte of all of these GUIDs is 0.
if _MSC_VER > 1000:
    pass
# END IF
from  pyWinAPI.shared.winapifamily_h import * # NOQA
if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    GUID_NULL = DEFINE_GUID(
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0
    )
    IID_IUnknown = DEFINE_OLEGUID(
        0x00000000,
        0x0,
        0x0
    )
    IID_IClassFactory = DEFINE_OLEGUID(
        0x00000001,
        0x0,
        0x0
    )
    IID_IMalloc = DEFINE_OLEGUID(
        0x00000002,
        0x0,
        0x0
    )
    IID_IMarshal = DEFINE_OLEGUID(
        0x00000003,
        0x0,
        0x0
    )

    # RPC related interfaces
    IID_IRpcChannel = DEFINE_OLEGUID(
        0x00000004,
        0x0,
        0x0
    )
    IID_IRpcStub = DEFINE_OLEGUID(
        0x00000005,
        0x0,
        0x0
    )
    IID_IStubManager = DEFINE_OLEGUID(
        0x00000006,
        0x0,
        0x0
    )
    IID_IRpcProxy = DEFINE_OLEGUID(
        0x00000007,
        0x0,
        0x0
    )
    IID_IProxyManager = DEFINE_OLEGUID(
        0x00000008,
        0x0,
        0x0
    )
    IID_IPSFactory = DEFINE_OLEGUID(
        0x00000009,
        0x0,
        0x0
    )

    # storage related interfaces
    IID_ILockBytes = DEFINE_OLEGUID(
        0x0000000A,
        0x0,
        0x0
    )
    IID_IStorage = DEFINE_OLEGUID(
        0x0000000B,
        0x0,
        0x0
    )
    IID_IStream = DEFINE_OLEGUID(
        0x0000000C,
        0x0,
        0x0
    )
    IID_IEnumSTATSTG = DEFINE_OLEGUID(
        0x0000000D,
        0x0,
        0x0
    )

    # moniker related interfaces
    IID_IBindCtx = DEFINE_OLEGUID(
        0x0000000E,
        0x0,
        0x0
    )
    IID_IMoniker = DEFINE_OLEGUID(
        0x0000000F,
        0x0,
        0x0
    )
    IID_IRunningObjectTable = DEFINE_OLEGUID(
        0x00000010,
        0x0,
        0x0
    )
    IID_IInternalMoniker = DEFINE_OLEGUID(
        0x00000011,
        0x0,
        0x0
    )

    # storage related interfaces
    IID_IRootStorage = DEFINE_OLEGUID(
        0x00000012,
        0x0,
        0x0
    )
    IID_IDfReserved1 = DEFINE_OLEGUID(
        0x00000013,
        0x0,
        0x0
    )
    IID_IDfReserved2 = DEFINE_OLEGUID(
        0x00000014,
        0x0,
        0x0
    )
    IID_IDfReserved3 = DEFINE_OLEGUID(
        0x00000015,
        0x0,
        0x0
    )

    # concurrency releated interfaces
    IID_IMessageFilter = DEFINE_OLEGUID(
        0x00000016,
        0x0,
        0x0
    )

    # CLSID of standard marshaler
    CLSID_StdMarshal = DEFINE_OLEGUID(
        0x00000017,
        0x0,
        0x0
    )

    # interface on server for getting info for std marshaler
    IID_IStdMarshalInfo = DEFINE_OLEGUID(
        0x00000018,
        0x0,
        0x0
    )

    # interface to inform object of number of external connections
    IID_IExternalConnection = DEFINE_OLEGUID(
        0x00000019,
        0x0,
        0x0
    )

    # CLSID of aggregated standard marshaler
    CLSID_AggStdMarshal = DEFINE_OLEGUID(
        0x00000027,
        0x0,
        0x0
    )

    # NOTE: LSB 0x33 through 0xff are reserved for future use
    # CLSID of various implementations of ISynchronize
    # DEFINE_OLEGUID(CLSID_Synchronize_AutoComplete,  0x00000324L, 0, 0);
    # obsolete
    # DEFINE_OLEGUID(CLSID_Synchronize_ManualResetEvent, 0x00000325L, 0, 0);
    # obsolete
    # DEFINE_OLEGUID(CLSID_WaitMultiple,    0x00000326L, 0, 0); obsolete
    CLSID_StdEvent = DEFINE_OLEGUID(
        0x0000032B,
        0x0,
        0x0
    )
    CLSID_ManualResetEvent = DEFINE_OLEGUID(
        0x0000032C,
        0x0,
        0x0
    )
    CLSID_SynchronizeContainer = DEFINE_OLEGUID(
        0x0000032D,
        0x0,
        0x0
    )
    CLSID_SurrogateManager = DEFINE_OLEGUID(
        0x0000034C,
        0x0,
        0x0
    )
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
