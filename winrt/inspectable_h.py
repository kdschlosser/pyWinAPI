

from wtypes_h import (
    ENUM,
    ULONG,
    POINTER,
    HRESULT,
)
from guiddef_h import (
    IID,
)
import comtypes


# this ALWAYS GENERATED file contains the definitions for the INTerfaces
# File created by MIDL compiler version 8.01.0622
# @@MIDL_FILE_HEADING(  )
# verify that the <rpcndr.h> version is high enough to compile this file
__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
# verify that the <rpcsal.h> version is high enough to compile this file
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# # __RPCNDR_H_VERSION__
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
# COM_NO_WINDOWS_H
# Forward Declarations
IID_IInspectable = IID(
    '{AF86E2E0-B12D-4c6a-9C5A-D7AA65101E90}'
)


class IInspectable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInspectable
    _idlflags_ = []


# __IInspectable_FWD_DEFINED__
# header files for imported files
from unknwn_h import * # NOQA
from hstring_h import * # NOQA
# INTerface __MIDL_itf_inspectable_0000_0000
# [local]
# +-------------------------------------------------------------------------

# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.

# --------------------------------------------------------------------------
# [unique]
LPINSPECTABLE = POINTER(IInspectable)
# [v1_enum]


class TrustLevel(ENUM):
    BaseTrust = 0
    PartialTrust = BaseTrust + 1
    FullTrust = PartialTrust + 1


# INTerface IInspectable
# [unique][uuid][object]
COMMETHOD = comtypes.COMMETHOD


IInspectable._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetIids',
        (['out'], POINTER(ULONG), 'iidCount'),
        (['out'], POINTER(POINTER(IID)), 'iids'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRuntimeClassName',
        (['out'], POINTER(HSTRING), 'className'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTrustLevel',
        (['out'], POINTER(TrustLevel), 'trustLevel'),
    ),
]


# C style INTerface
# [in]  __RPC__in REFIID riid,
# [annotation][iid_is][out]
# [out]  __RPC__out ULONG *iidCount,
# [size_is][size_is][out]  __RPC__deref_out_ecount_full_opt(*iidCount) IID
# **iids);

# HRESULT ( STDMETHODCALLTYPE *GetRuntimeClassName )(
# __RPC__in IInspectable * This,
# [out]  __RPC__deref_out_opt HSTRING *className);

# HRESULT ( STDMETHODCALLTYPE *GetTrustLevel )(
# __RPC__in IInspectable * This,
# [out]  __RPC__out TrustLevel *trustLevel);

# END_INTERFACE
# } IInspectableVtbl;
# INTerface IInspectable
# {
# CONST_VTBL struct IInspectableVtbl *lpVtbl;
# };

# #ifdef COBJMACROS
# #define IInspectable_QueryInterface(This,riid,ppvObject)    \
# ( (This)->lpVtbl -> QueryInterface(This,riid,ppvObject) )
# #define IInspectable_AddRef(This)    \
# ( (This)->lpVtbl -> AddRef(This) )
# #define IInspectable_Release(This)    \
# ( (This)->lpVtbl -> Release(This) )
# #define IInspectable_GetIids(This,iidCount,iids)    \
# ( (This)->lpVtbl -> GetIids(This,iidCount,iids) )
# #define IInspectable_GetRuntimeClassName(This,className)    \
# ( (This)->lpVtbl -> GetRuntimeClassName(This,className) )
# #define IInspectable_GetTrustLevel(This,trustLevel)    \
# ( (This)->lpVtbl -> GetTrustLevel(This,trustLevel) )
# #endif  COBJMACROS
# C style INTerface
# __IInspectable_INTERFACE_DEFINED__
# INTerface __MIDL_itf_inspectable_0000_0001
# [local]
# IInspectable equivalent of IID_PPV_ARGS
# IID_INS_ARGS(ppType)
# ppType is the variable of type IType that will be filled

# RESULTS in:  IID_IType, ppvType
# will create a compiler error if wrong level of indirection is used.

# make sure everyone derives from IInspectable


def IID_INS_ARGS(ppType):
    return ppType._iid_

# Additional Prototypes for ALL INTerfaces
# end of Additional Prototypes

__all__ = (
    'IInspectable', '__REQUIRED_RPCSAL_H_VERSION__', 'IID_INS_ARGS',
    '__REQUIRED_RPCNDR_H_VERSION__', 'TrustLevel', 'LPINSPECTABLE',
)
