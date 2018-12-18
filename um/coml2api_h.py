import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_COML2API_H_ = None
_STGCREATEPROPSTG_DEFINED_ = None


class tagSTGOPTIONS(ctypes.Structure):
    pass


STGOPTIONS = tagSTGOPTIONS


# + ---------------------------------------------------------------------------
# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.
# File:  coml2api.h
# Contents: Structured storage, property sets, and related APIs.
# ----------------------------------------------------------------------------
if not defined(_COML2API_H_):
    _COML2API_H_ = VOID
    if defined(_MSC_VER):
        pass
    # END IF   _MSC_VER

    from pyWinAPI.shared.apiset_h import * # NOQA
    from pyWinAPI.shared.apisetcconv_h import * # NOQA
    from pyWinAPI.um.combaseapi_h import * # NOQA
    from pyWinAPI.um.objidl_h import * # NOQA
    from pyWinAPI.um.propidlbase_h import * # NOQA

    ole32 = ctypes.windll.OLE32

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # Common typedefs for paramaters used in Storage API's, gleamed from
        # storage.h
        # Also contains Storage error codes, which should be moved into the
        # storage
        # idl files.
        CWCSTORAGENAME = 32

        # Storage instantiation modes
        STGM_DIRECT = 0x00000000
        STGM_TRANSACTED = 0x00010000
        STGM_SIMPLE = 0x08000000
        STGM_READ = 0x00000000
        STGM_WRITE = 0x00000001
        STGM_READWRITE = 0x00000002
        STGM_SHARE_DENY_NONE = 0x00000040
        STGM_SHARE_DENY_READ = 0x00000030
        STGM_SHARE_DENY_WRITE = 0x00000020
        STGM_SHARE_EXCLUSIVE = 0x00000010
        STGM_PRIORITY = 0x00040000
        STGM_DELETEONRELEASE = 0x04000000
        if WINVER >= 400:
            STGM_NOSCRATCH = 0x00100000
        # END IF  WINVER

        STGM_CREATE = 0x00001000
        STGM_CONVERT = 0x00020000
        STGM_FAILIFTHERE = 0x00000000
        STGM_NOSNAPSHOT = 0x00200000
        if _WIN32_WINNT >= 0x0500:
            STGM_DIRECT_SWMR = 0x00400000
        # END IF


        STGFMT = DWORD
        STGFMT_STORAGE = 0
        STGFMT_NATIVE = 1
        STGFMT_FILE = 3
        STGFMT_ANY = 4
        STGFMT_DOCFILE = 5

        # This is a legacy define to allow old component to builds
        STGFMT_DOCUMENT = 0

        # Structured storage APIs
        # _Check_return_
        # WINOLEAPI
        # StgCreateDocfile(
        # _In_opt_ _Null_terminated_ WCHAR* pwcsName,
        # _In_ DWORD grfMode,
        # _Reserved_ DWORD reserved,
        # _Outptr_ IStorage** ppstgOpen
        # );
        StgCreateDocfile = ole32.StgCreateDocfile
        StgCreateDocfile.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI
        # StgCreateDocfileOnILockBytes(
        # _In_ ILockBytes* plkbyt,
        # _In_ DWORD grfMode,
        # _In_ DWORD reserved,
        # _Outptr_ IStorage** ppstgOpen
        # );
        StgCreateDocfileOnILockBytes = ole32.StgCreateDocfileOnILockBytes
        StgCreateDocfileOnILockBytes.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI
        # StgOpenStorage(
        # _In_opt_ _Null_terminated_ WCHAR* pwcsName,
        # _In_opt_ IStorage* pstgPriority,
        # _In_ DWORD grfMode,
        # _In_opt_z_ SNB snbExclude,
        # _In_ DWORD reserved,
        # _Outptr_ IStorage** ppstgOpen
        # );
        StgOpenStorage = ole32.StgOpenStorage
        StgOpenStorage.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI
        # StgOpenStorageOnILockBytes(
        # _In_ ILockBytes* plkbyt,
        # _In_opt_ IStorage* pstgPriority,
        # _In_ DWORD grfMode,
        # _In_opt_z_ SNB snbExclude,
        # _Reserved_ DWORD reserved,
        # _Outptr_ IStorage** ppstgOpen
        # );
        StgOpenStorageOnILockBytes = ole32.StgOpenStorageOnILockBytes
        StgOpenStorageOnILockBytes.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI
        # StgIsStorageFile(
        # _In_ _Null_terminated_ WCHAR* pwcsName
        # );
        StgIsStorageFile = ole32.StgIsStorageFile
        StgIsStorageFile.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI
        # StgIsStorageILockBytes(
        # _In_ ILockBytes* plkbyt
        # );
        StgIsStorageILockBytes = ole32.StgIsStorageILockBytes
        StgIsStorageILockBytes.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI
        # StgSetTimes(
        # _In_ _Null_terminated_ WCHAR* lpszName,
        # _In_opt_ FILETIME* pctime,
        # _In_opt_ FILETIME* patime,
        # _In_opt_ FILETIME* pmtime
        # );
        StgSetTimes = ole32.StgSetTimes
        StgSetTimes.restype = WINOLEAPI

        # STG initialization options for StgCreateStorageEx and
        # StgOpenStorageEx
        if _WIN32_WINNT == 0x500:
            STGOPTIONS_VERSION = 1
        elif _WIN32_WINNT > 0x500:
            STGOPTIONS_VERSION = 2
        else:
            STGOPTIONS_VERSION = 0
        # END IF

        _TEMP_tagSTGOPTIONS = [
            # Versions 1 and 2 supported
            ('usVersion', USHORT),
            # must be 0 for padding
            ('reserved', USHORT),
            # docfile header sector size (512)
            ('ulSectorSize', ULONG),
        ]
        if STGOPTIONS_VERSION >= 2:
            _TEMP_tagSTGOPTIONS += [
                # version 2 or above
                ('pwcsTemplateFile', POINTER(WCHAR)),
            ]
            # END IF

        tagSTGOPTIONS._fields_ = _TEMP_tagSTGOPTIONS

        # _Check_return_
        # WINOLEAPI
        # StgCreateStorageEx(
        # _In_opt_ _Null_terminated_ WCHAR* pwcsName,
        # _In_ DWORD grfMode,
        # _In_ DWORD stgfmt,
        # _In_ DWORD grfAttrs,
        # _Inout_opt_ STGOPTIONS* pStgOptions,
        # _In_opt_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
        # _In_ REFIID riid,
        # _Outptr_ void** ppObjectOpen
        # );
        StgCreateStorageEx = ole32.StgCreateStorageEx
        StgCreateStorageEx.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI
        # StgOpenStorageEx(
        # _In_ _Null_terminated_ WCHAR* pwcsName,
        # _In_ DWORD grfMode,
        # _In_ DWORD stgfmt,
        # _In_ DWORD grfAttrs,
        # _Inout_opt_ STGOPTIONS* pStgOptions,
        # _In_opt_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
        # _In_ REFIID riid,
        # _Outptr_ void** ppObjectOpen
        # );
        StgOpenStorageEx = ole32.StgOpenStorageEx
        StgOpenStorageEx.restype = WINOLEAPI

        if not defined(_STGCREATEPROPSTG_DEFINED_):
            # _Check_return_
            # WINOLEAPI
            # StgCreatePropStg(
            # _In_ IUnknown* pUnk,
            # _In_ REFFMTID fmtid,
            # _In_ CLSID* pclsid,
            # _In_ DWORD grfFlags,
            # _Reserved_ DWORD dwReserved,
            # _Outptr_ IPropertyStorage** ppPropStg
            # );
            StgCreatePropStg = ole32.StgCreatePropStg
            StgCreatePropStg.restype = WINOLEAPI

            # _Check_return_
            # WINOLEAPI
            # StgOpenPropStg(
            # _In_ IUnknown* pUnk,
            # _In_ REFFMTID fmtid,
            # _In_ DWORD grfFlags,
            # _Reserved_ DWORD dwReserved,
            # _Outptr_ IPropertyStorage** ppPropStg
            # );
            StgOpenPropStg = ole32.StgOpenPropStg
            StgOpenPropStg.restype = WINOLEAPI

            # _Check_return_
            # WINOLEAPI
            # StgCreatePropSetStg(
            # _In_ IStorage* pStorage,
            # _Reserved_ DWORD dwReserved,
            # _Outptr_ IPropertySetStorage** ppPropSetStg
            # );
            StgCreatePropSetStg = ole32.StgCreatePropSetStg
            StgCreatePropSetStg.restype = WINOLEAPI

            CCH_MAX_PROPSTG_NAME = 31

            # _Check_return_
            # WINOLEAPI
            # FmtIdToPropStgName(
            # _In_ FMTID* pfmtid,
            # _Out_writes_(CCH_MAX_PROPSTG_NAME + 1) LPOLESTR oszName
            # );
            FmtIdToPropStgName = ole32.FmtIdToPropStgName
            FmtIdToPropStgName.restype = WINOLEAPI

            # _Check_return_
            # WINOLEAPI
            # PropStgNameToFmtId(
            # _In_ LPOLESTR oszName,
            # _Out_ FMTID* pfmtid
            # );
            PropStgNameToFmtId = ole32.PropStgNameToFmtId
            PropStgNameToFmtId.restype = WINOLEAPI

        # END IF   _STGCREATEPROPSTG_DEFINED_

        # Helper functions
        # WINOLEAPI
        # ReadClassStg(
        # _In_ LPSTORAGE pStg,
        # _Out_ CLSID  FAR * pclsid
        # );
        ReadClassStg = ole32.ReadClassStg
        ReadClassStg.restype = WINOLEAPI

        # WINOLEAPI
        # WriteClassStg(
        # _In_ LPSTORAGE pStg,
        # _In_ REFCLSID rclsid
        # );
        WriteClassStg = ole32.WriteClassStg
        WriteClassStg.restype = WINOLEAPI

        # WINOLEAPI
        # ReadClassStm(
        # _In_ LPSTREAM pStm,
        # _Out_ CLSID  FAR * pclsid
        # );
        ReadClassStm = ole32.ReadClassStm
        ReadClassStm.restype = WINOLEAPI

        # WINOLEAPI
        # WriteClassStm(
        # _In_ LPSTREAM pStm,
        # _In_ REFCLSID rclsid
        # );
        WriteClassStm = ole32.WriteClassStm
        WriteClassStm.restype = WINOLEAPI

        # Storage utility APIs
        # _Check_return_
        # WINOLEAPI
        # GetHGlobalFromILockBytes(
        # _In_ LPLOCKBYTES plkbyt,
        # _Out_ HGLOBAL  FAR * phglobal
        # );
        GetHGlobalFromILockBytes = ole32.GetHGlobalFromILockBytes
        GetHGlobalFromILockBytes.restype = WINOLEAPI

        # _Check_return_
        # WINOLEAPI
        # CreateILockBytesOnHGlobal(
        # _In_opt_ HGLOBAL hGlobal,
        # _In_ BOOL fDeleteOnRelease,
        # _Outptr_ LPLOCKBYTES  FAR * pplkbyt
        # );
        CreateILockBytesOnHGlobal = ole32.CreateILockBytesOnHGlobal
        CreateILockBytesOnHGlobal.restype = WINOLEAPI

        # ConvertTo APIs
        # WINOLEAPI
        # GetConvertStg(
        # _In_ LPSTORAGE pStg
        # );
        GetConvertStg = ole32.GetConvertStg
        GetConvertStg.restype = WINOLEAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
# END IF   __COML2API_H__


