import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


COMMETHOD = comtypes.COMMETHOD


__REQUIRED_RPCNDR_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__corsym_h__ = None
__CorSymWriter_deprecated_FWD_DEFINED__ = None
__CorSymReader_deprecated_FWD_DEFINED__ = None
__CorSymBinder_deprecated_FWD_DEFINED__ = None
__CorSymWriter_SxS_FWD_DEFINED__ = None
__CorSymReader_SxS_FWD_DEFINED__ = None
__CorSymBinder_SxS_FWD_DEFINED__ = None
__ISymUnmanagedBinder_FWD_DEFINED__ = None
__ISymUnmanagedBinder2_FWD_DEFINED__ = None
__ISymUnmanagedBinder3_FWD_DEFINED__ = None
__ISymUnmanagedDispose_FWD_DEFINED__ = None
__ISymUnmanagedDocument_FWD_DEFINED__ = None
__ISymUnmanagedDocumentWriter_FWD_DEFINED__ = None
__ISymUnmanagedMethod_FWD_DEFINED__ = None
__ISymENCUnmanagedMethod_FWD_DEFINED__ = None
__ISymUnmanagedNamespace_FWD_DEFINED__ = None
__ISymUnmanagedReader_FWD_DEFINED__ = None
__ISymUnmanagedSourceServerModule_FWD_DEFINED__ = None
__ISymUnmanagedENCUpdate_FWD_DEFINED__ = None
__ISymUnmanagedReaderSymbolSearchInfo_FWD_DEFINED__ = None
__ISymUnmanagedScope_FWD_DEFINED__ = None
__ISymUnmanagedConstant_FWD_DEFINED__ = None
__ISymUnmanagedScope2_FWD_DEFINED__ = None
__ISymUnmanagedVariable_FWD_DEFINED__ = None
__ISymUnmanagedSymbolSearchInfo_FWD_DEFINED__ = None
__ISymUnmanagedWriter_FWD_DEFINED__ = None
__ISymUnmanagedWriter2_FWD_DEFINED__ = None
__ISymUnmanagedWriter3_FWD_DEFINED__ = None
__ISymUnmanagedReader2_FWD_DEFINED__ = None
__CORHDR_H__ = None
__CorSymLib_LIBRARY_DEFINED__ = None
__ISymUnmanagedBinder_INTERFACE_DEFINED__ = None
__ISymUnmanagedBinder2_INTERFACE_DEFINED__ = None
__ISymUnmanagedBinder3_INTERFACE_DEFINED__ = None
__ISymUnmanagedDispose_INTERFACE_DEFINED__ = None
__ISymUnmanagedDocument_INTERFACE_DEFINED__ = None
__ISymUnmanagedDocumentWriter_INTERFACE_DEFINED__ = None
__ISymUnmanagedMethod_INTERFACE_DEFINED__ = None
__ISymENCUnmanagedMethod_INTERFACE_DEFINED__ = None
__ISymUnmanagedNamespace_INTERFACE_DEFINED__ = None
__ISymUnmanagedReader_INTERFACE_DEFINED__ = None
__ISymUnmanagedSourceServerModule_INTERFACE_DEFINED__ = None
__ISymUnmanagedENCUpdate_INTERFACE_DEFINED__ = None
__ISymUnmanagedReaderSymbolSearchInfo_INTERFACE_DEFINED__ = None
__ISymUnmanagedScope_INTERFACE_DEFINED__ = None
__ISymUnmanagedConstant_INTERFACE_DEFINED__ = None
__ISymUnmanagedScope2_INTERFACE_DEFINED__ = None
__ISymUnmanagedVariable_INTERFACE_DEFINED__ = None
__ISymUnmanagedSymbolSearchInfo_INTERFACE_DEFINED__ = None
__ISymUnmanagedWriter_INTERFACE_DEFINED__ = None
__ISymUnmanagedWriter2_INTERFACE_DEFINED__ = None
__ISymUnmanagedWriter3_INTERFACE_DEFINED__ = None
__ISymUnmanagedReader2_INTERFACE_DEFINED__ = None


class _SYMLINEDELTA(ctypes.Structure):
    pass


SYMLINEDELTA = _SYMLINEDELTA


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 6.00.0366
# @@MIDL_FILE_HEADING( )
# verify that the <rpcndr.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    __REQUIRED_RPCNDR_H_VERSION__ = 475
# END IF

from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA
if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF   __RPCNDR_H_VERSION__

if not defined(COM_NO_WINDOWS_H):
    from pyWinAPI.um.windows_h import * # NOQA
    from pyWinAPI.um.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H

if not defined(__corsym_h__):
    __corsym_h__ = VOID
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__CorSymWriter_deprecated_FWD_DEFINED__):
        __CorSymWriter_deprecated_FWD_DEFINED__ = VOID
        if defined(__cplusplus):
            pass

        else:
            class CorSymWriter_deprecated(comtypes.CoClass):
                pass
        # END IF  __cplusplus
    # END IF  __CorSymWriter_deprecated_FWD_DEFINED__

    if not defined(__CorSymReader_deprecated_FWD_DEFINED__):
        __CorSymReader_deprecated_FWD_DEFINED__ = VOID
        if defined(__cplusplus):
            pass
        else:
            class CorSymReader_deprecated(comtypes.CoClass):
                pass

        # END IF  __cplusplus
    # END IF  __CorSymReader_deprecated_FWD_DEFINED__

    if not defined(__CorSymBinder_deprecated_FWD_DEFINED__):
        __CorSymBinder_deprecated_FWD_DEFINED__ = VOID
        if defined(__cplusplus):
            pass
        else:
            class CorSymBinder_deprecated(comtypes.CoClass):
                pass
        # END IF  __cplusplus
    # END IF  __CorSymBinder_deprecated_FWD_DEFINED__

    if not defined(__CorSymWriter_SxS_FWD_DEFINED__):
        __CorSymWriter_SxS_FWD_DEFINED__ = VOID
        if defined(__cplusplus):
            pass

        else:
            class CorSymWriter_SxS(comtypes.CoClass):
                pass
        # END IF  __cplusplus
    # END IF  __CorSymWriter_SxS_FWD_DEFINED__

    if not defined(__CorSymReader_SxS_FWD_DEFINED__):
        __CorSymReader_SxS_FWD_DEFINED__ = VOID
        if defined(__cplusplus):
            pass
        else:
            class CorSymReader_SxS(comtypes.CoClass):
                pass
        # END IF  __cplusplus
    # END IF  __CorSymReader_SxS_FWD_DEFINED__

    if not defined(__CorSymBinder_SxS_FWD_DEFINED__):
        __CorSymBinder_SxS_FWD_DEFINED__ = VOID
        if defined(__cplusplus):
            pass
        else:
            class CorSymBinder_SxS(comtypes.CoClass):
                pass
        # END IF  __cplusplus
    # END IF  __CorSymBinder_SxS_FWD_DEFINED__

    if not defined(__ISymUnmanagedBinder_FWD_DEFINED__):
        __ISymUnmanagedBinder_FWD_DEFINED__ = VOID


        class ISymUnmanagedBinder(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedBinder_FWD_DEFINED__

    if not defined(__ISymUnmanagedBinder2_FWD_DEFINED__):
        __ISymUnmanagedBinder2_FWD_DEFINED__ = VOID


        class ISymUnmanagedBinder2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedBinder2_FWD_DEFINED__

    if not defined(__ISymUnmanagedBinder3_FWD_DEFINED__):
        __ISymUnmanagedBinder3_FWD_DEFINED__ = VOID


        class ISymUnmanagedBinder3(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedBinder3_FWD_DEFINED__

    if not defined(__ISymUnmanagedDispose_FWD_DEFINED__):
        __ISymUnmanagedDispose_FWD_DEFINED__ = VOID


        class ISymUnmanagedDispose(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedDispose_FWD_DEFINED__

    if not defined(__ISymUnmanagedDocument_FWD_DEFINED__):
        __ISymUnmanagedDocument_FWD_DEFINED__ = VOID


        class ISymUnmanagedDocument(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedDocument_FWD_DEFINED__

    if not defined(__ISymUnmanagedDocumentWriter_FWD_DEFINED__):
        __ISymUnmanagedDocumentWriter_FWD_DEFINED__ = VOID


        class ISymUnmanagedDocumentWriter(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedDocumentWriter_FWD_DEFINED__

    if not defined(__ISymUnmanagedMethod_FWD_DEFINED__):
        __ISymUnmanagedMethod_FWD_DEFINED__ = VOID


        class ISymUnmanagedMethod(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedMethod_FWD_DEFINED__

    if not defined(__ISymENCUnmanagedMethod_FWD_DEFINED__):
        __ISymENCUnmanagedMethod_FWD_DEFINED__ = VOID


        class ISymENCUnmanagedMethod(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymENCUnmanagedMethod_FWD_DEFINED__

    if not defined(__ISymUnmanagedNamespace_FWD_DEFINED__):
        __ISymUnmanagedNamespace_FWD_DEFINED__ = VOID


        class ISymUnmanagedNamespace(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedNamespace_FWD_DEFINED__

    if not defined(__ISymUnmanagedReader_FWD_DEFINED__):
        __ISymUnmanagedReader_FWD_DEFINED__ = VOID


        class ISymUnmanagedReader(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedReader_FWD_DEFINED__

    if not defined(__ISymUnmanagedSourceServerModule_FWD_DEFINED__):
        __ISymUnmanagedSourceServerModule_FWD_DEFINED__ = VOID


        class ISymUnmanagedSourceServerModule(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedSourceServerModule_FWD_DEFINED__

    if not defined(__ISymUnmanagedENCUpdate_FWD_DEFINED__):
        __ISymUnmanagedENCUpdate_FWD_DEFINED__ = VOID


        class ISymUnmanagedENCUpdate(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedENCUpdate_FWD_DEFINED__

    if not defined(__ISymUnmanagedReaderSymbolSearchInfo_FWD_DEFINED__):
        __ISymUnmanagedReaderSymbolSearchInfo_FWD_DEFINED__ = VOID


        class ISymUnmanagedReaderSymbolSearchInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedReaderSymbolSearchInfo_FWD_DEFINED__

    if not defined(__ISymUnmanagedScope_FWD_DEFINED__):
        __ISymUnmanagedScope_FWD_DEFINED__ = VOID


        class ISymUnmanagedScope(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedScope_FWD_DEFINED__

    if not defined(__ISymUnmanagedConstant_FWD_DEFINED__):
        __ISymUnmanagedConstant_FWD_DEFINED__ = VOID


        class ISymUnmanagedConstant(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedConstant_FWD_DEFINED__

    if not defined(__ISymUnmanagedScope2_FWD_DEFINED__):
        __ISymUnmanagedScope2_FWD_DEFINED__ = VOID


        class ISymUnmanagedScope2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedScope2_FWD_DEFINED__

    if not defined(__ISymUnmanagedVariable_FWD_DEFINED__):
        __ISymUnmanagedVariable_FWD_DEFINED__ = VOID


        class ISymUnmanagedVariable(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedVariable_FWD_DEFINED__

    if not defined(__ISymUnmanagedSymbolSearchInfo_FWD_DEFINED__):
        __ISymUnmanagedSymbolSearchInfo_FWD_DEFINED__ = VOID


        class ISymUnmanagedSymbolSearchInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedSymbolSearchInfo_FWD_DEFINED__

    if not defined(__ISymUnmanagedWriter_FWD_DEFINED__):
        __ISymUnmanagedWriter_FWD_DEFINED__ = VOID


        class ISymUnmanagedWriter(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedWriter_FWD_DEFINED__

    if not defined(__ISymUnmanagedWriter2_FWD_DEFINED__):
        __ISymUnmanagedWriter2_FWD_DEFINED__ = VOID


        class ISymUnmanagedWriter2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedWriter2_FWD_DEFINED__

    if not defined(__ISymUnmanagedWriter3_FWD_DEFINED__):
        __ISymUnmanagedWriter3_FWD_DEFINED__ = VOID


        class ISymUnmanagedWriter3(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedWriter3_FWD_DEFINED__

    if not defined(__ISymUnmanagedReader2_FWD_DEFINED__):
        __ISymUnmanagedReader2_FWD_DEFINED__ = VOID


        class ISymUnmanagedReader2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISymUnmanagedReader2_FWD_DEFINED__

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_corsym_0000
    # [local]
    _ZERO_ = 0
    if _ZERO_:
        UINT32 = UINT
        mdTypeDef = mdToken
        mdMethodDef = mdToken
        SIZE_T = ULONG_PTR
    else:
        mdTypeDef = mdToken
        mdMethodDef = mdToken
    # END IF

    if not defined(__CORHDR_H__):
        mdSignature = mdToken
    # END IF

    CorSym_LanguageType_C = EXTERN_GUID(
        0x63A08714,
        0xFC37,
        0x11D2,
        0x90,
        0x4C,
        0x0,
        0xC0,
        0x4F,
        0xA3,
        0x02,
        0xA1
    )
    CorSym_LanguageType_CPlusPlus = EXTERN_GUID(
        0x3A12D0B7,
        0xC26C,
        0x11D0,
        0xB4,
        0x42,
        0x0,
        0xA0,
        0x24,
        0x4A,
        0x1D,
        0xD2
    )
    CorSym_LanguageType_CSharp = EXTERN_GUID(
        0x3F5162F8,
        0x07C6,
        0x11D3,
        0x90,
        0x53,
        0x0,
        0xC0,
        0x4F,
        0xA3,
        0x02,
        0xA1
    )
    CorSym_LanguageType_Basic = EXTERN_GUID(
        0x3A12D0B8,
        0xC26C,
        0x11D0,
        0xB4,
        0x42,
        0x0,
        0xA0,
        0x24,
        0x4A,
        0x1D,
        0xD2
    )
    CorSym_LanguageType_Java = EXTERN_GUID(
        0x3A12D0B4,
        0xC26C,
        0x11D0,
        0xB4,
        0x42,
        0x0,
        0xA0,
        0x24,
        0x4A,
        0x1D,
        0xD2
    )
    CorSym_LanguageType_Cobol = EXTERN_GUID(
        0xAF046CD1,
        0xD0E1,
        0x11D2,
        0x97,
        0x7C,
        0x0,
        0xA0,
        0xC9,
        0xB4,
        0xD5,
        0xC
    )
    CorSym_LanguageType_Pascal = EXTERN_GUID(
        0xAF046CD2,
        0xD0E1,
        0x11D2,
        0x97,
        0x7C,
        0x0,
        0xA0,
        0xC9,
        0xB4,
        0xD5,
        0xC
    )
    CorSym_LanguageType_ILAssembly = EXTERN_GUID(
        0xAF046CD3,
        0xD0E1,
        0x11D2,
        0x97,
        0x7C,
        0x0,
        0xA0,
        0xC9,
        0xB4,
        0xD5,
        0xC
    )
    CorSym_LanguageType_JScript = EXTERN_GUID(
        0x3A12D0B6,
        0xC26C,
        0x11D0,
        0xB4,
        0x42,
        0x00,
        0xA0,
        0x24,
        0x4A,
        0x1D,
        0xD2
    )
    CorSym_LanguageType_SMC = EXTERN_GUID(
        0xD9B9F7B,
        0x6611,
        0x11D3,
        0xBD,
        0x2A,
        0x0,
        0x0,
        0xF8,
        0x8,
        0x49,
        0xBD
    )
    CorSym_LanguageType_MCPlusPlus = EXTERN_GUID(
        0x4B35FDE8,
        0x07C6,
        0x11D3,
        0x90,
        0x53,
        0x0,
        0xC0,
        0x4F,
        0xA3,
        0x02,
        0xA1
    )
    CorSym_LanguageVendor_Microsoft = EXTERN_GUID(
        0x994B45C4,
        0xE6E9,
        0x11D2,
        0x90,
        0x3F,
        0x00,
        0xC0,
        0x4F,
        0xA3,
        0x02,
        0xA1
    )
    CorSym_DocumentType_Text = EXTERN_GUID(
        0x5A869D0B,
        0x6611,
        0x11D3,
        0xBD,
        0x2A,
        0x0,
        0x0,
        0xF8,
        0x8,
        0x49,
        0xBD
    )
    CorSym_DocumentType_MC = EXTERN_GUID(
        0xEB40CB65,
        0x3C1F,
        0x4352,
        0x9D,
        0x7B,
        0xBA,
        0xF,
        0xC4,
        0x7A,
        0x9D,
        0x77
    )
    CorSym_SourceHash_MD5 = EXTERN_GUID(
        0x406EA660,
        0x64CF,
        0x4C82,
        0xB6,
        0xF0,
        0x42,
        0xD4,
        0x81,
        0x72,
        0xA7,
        0x99
    )
    CorSym_SourceHash_SHA1 = EXTERN_GUID(
        0xFF1816EC,
        0xAA5E,
        0x4D10,
        0x87,
        0xF7,
        0x6F,
        0x49,
        0x63,
        0x83,
        0x34,
        0x60
    )


    class CorSymAddrKind(ENUM):
        ADDR_IL_OFFSET = 1
        ADDR_NATIVE_RVA = 2
        ADDR_NATIVE_REGISTER = 3
        ADDR_NATIVE_REGREL = 4
        ADDR_NATIVE_OFFSET = 5
        ADDR_NATIVE_REGREG = 6
        ADDR_NATIVE_REGSTK = 7
        ADDR_NATIVE_STKREG = 8
        ADDR_BITFIELD = 9
        ADDR_NATIVE_ISECTOFFSET = 10


    class CorSymVarFlag(ENUM):
        VAR_IS_COMP_GEN = 1

    if not defined(__CorSymLib_LIBRARY_DEFINED__):
        __CorSymLib_LIBRARY_DEFINED__ = VOID

        LIBID_CorSymLib = DECLSPEC_UUID(
            "108296C1-281E-11d3-BD22-0000F80849BD"
        )

        class CorSymLib(object):
            name = 'CorSymLib'
            _reg_typelib_ = (LIBID_CorSymLib, 1, 0)


        CLSID_CorSymWriter_deprecated = CLSID(
            "108296C1-281E-11d3-BD22-0000F80849BD"
        )

        # library CorSymLib
        # [helpstring][version][uuid]
        if defined(__cplusplus):
            pass
        else:
            CorSymWriter_deprecated._reg_clsid_ = CLSID_CorSymWriter_deprecated
            CorSymWriter_deprecated._idlflags_ = []
            CorSymWriter_deprecated._reg_typelib_ = (LIBID_CorSymLib, 1, 0)
            CorSymWriter_deprecated._com_interfaces_ = [ICorSymWriter]
        # END IF

        CLSID_CorSymReader_deprecated = CLSID(
            "108296C2-281E-11d3-BD22-0000F80849BD"
        )

        if defined(__cplusplus):
            pass
        else:
            CorSymReader_deprecated._reg_clsid_ = CLSID_CorSymReader_deprecated
            CorSymReader_deprecated._idlflags_ = []
            CorSymReader_deprecated._reg_typelib_ = (LIBID_CorSymLib, 1, 0)
            CorSymReader_deprecated._com_interfaces_ = [ICorSymReader]
        # END IF

        CLSID_CorSymBinder_deprecated = CLSID(
            "AA544D41-28CB-11d3-BD22-0000F80849BD"
        )

        if defined(__cplusplus):
            pass
        else:
            CorSymBinder_deprecated._reg_clsid_ = CLSID_CorSymBinder_deprecated
            CorSymBinder_deprecated._idlflags_ = []
            CorSymBinder_deprecated._reg_typelib_ = (LIBID_CorSymLib, 1, 0)
            CorSymBinder_deprecated._com_interfaces_ = [ICorSymBinder]
        # END IF

        CLSID_CorSymWriter_SxS = CLSID(
            "0AE2DEB0-F901-478b-BB9F-881EE8066788"
        )

        if defined(__cplusplus):
            pass
        else:
            CorSymWriter_SxS._reg_clsid_ = CLSID_CorSymWriter_SxS
            CorSymWriter_SxS._idlflags_ = []
            CorSymWriter_SxS._reg_typelib_ = (LIBID_CorSymLib, 1, 0)
            CorSymWriter_SxS._com_interfaces_ = [ICorSymWriter_SxS]
        # END IF

        CLSID_CorSymReader_SxS = CLSID(
            "0A3976C5-4529-4ef8-B0B0-42EED37082CD"
        )

        if defined(__cplusplus):
            pass
        else:
            CorSymReader_SxS._reg_clsid_ = CLSID_CorSymReader_SxS
            CorSymReader_SxS._idlflags_ = []
            CorSymReader_SxS._reg_typelib_ = (LIBID_CorSymLib, 1, 0)
            CorSymReader_SxS._com_interfaces_ = [ICorSymReader_SxS]
        # END IF

        CLSID_CorSymBinder_SxS = CLSID(
            "0A29FF9E-7F9C-4437-8B11-F424491E3931"
        )

        if defined(__cplusplus):
            pass
        else:
            CorSymBinder_SxS._reg_clsid_ = CLSID_CorSymBinder_SxS
            CorSymBinder_SxS._idlflags_ = []
            CorSymBinder_SxS._reg_typelib_ = (LIBID_CorSymLib, 1, 0)
            CorSymBinder_SxS._com_interfaces_ = [ICorSymBinder_SxS]
        # END IF

    # END IF  __CorSymLib_LIBRARY_DEFINED__

    if not defined(__ISymUnmanagedBinder_INTERFACE_DEFINED__):
        __ISymUnmanagedBinder_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedBinder
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedBinder = MIDL_INTERFACE(
                "{AA544D42-28CB-11D3-BD22-0000F80849BD}"
            )
            ISymUnmanagedBinder._iid_ = IID_ISymUnmanagedBinder

            ISymUnmanagedBinder._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetReaderForFile')],
                    HRESULT,
                    'GetReaderForFile',
                    (['in'], POINTER(comtypes.IUnknown), 'importer'),
                    (['in'], POINTER(WCHAR), 'fileName'),
                    (['in'], POINTER(WCHAR), 'searchPath'),
                    (
                        ['out', 'retval'],
                        POINTER(POINTER(ISymUnmanagedReader)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetReaderFromStream')],
                    HRESULT,
                    'GetReaderFromStream',
                    (['in'], POINTER(comtypes.IUnknown), 'importer'),
                    (['in'], POINTER(IStream), 'pstream'),
                    (
                        ['out', 'retval'],
                        POINTER(POINTER(ISymUnmanagedReader)),
                        'pRetVal'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedBinder_INTERFACE_DEFINED__

    # interface __MIDL_itf_corsym_0115
    # [local]
    class CorSymSearchPolicyAttributes(ENUM):
        AllowRegistryAccess = 0x1
        AllowSymbolServerAccess = 0x2
        AllowOriginalPathAccess = 0x4
        AllowReferencePathAccess = 0x8

    if not defined(__ISymUnmanagedBinder2_INTERFACE_DEFINED__):
        __ISymUnmanagedBinder2_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedBinder2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedBinder2 = MIDL_INTERFACE(
                "{ACCEE350-89AF-4CCB-8B40-1C2C4C6F9434}"
            )
            ISymUnmanagedBinder2._iid_ = IID_ISymUnmanagedBinder2

            ISymUnmanagedBinder2._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetReaderForFile2')],
                    HRESULT,
                    'GetReaderForFile2',
                    (['in'], POINTER(comtypes.IUnknown), 'importer'),
                    (['in'], POINTER(WCHAR), 'fileName'),
                    (['in'], POINTER(WCHAR), 'searchPath'),
                    (['in'], ULONG32, 'searchPolicy'),
                    (
                        ['out', 'retval'],
                        POINTER(POINTER(ISymUnmanagedReader)),
                        'pRetVal'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedBinder2_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedBinder3_INTERFACE_DEFINED__):
        __ISymUnmanagedBinder3_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedBinder3
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedBinder3 = MIDL_INTERFACE(
                "{28AD3D43-B601-4D26-8A1B-25F9165AF9D7}"
            )
            ISymUnmanagedBinder3._iid_ = IID_ISymUnmanagedBinder3

            ISymUnmanagedBinder3._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetReaderFromCallback')],
                    HRESULT,
                    'GetReaderFromCallback',
                    (['in'], POINTER(comtypes.IUnknown), 'importer'),
                    (['in'], POINTER(WCHAR), 'fileName'),
                    (['in'], POINTER(WCHAR), 'searchPath'),
                    (['in'], ULONG32, 'searchPolicy'),
                    (['in'], POINTER(comtypes.IUnknown), 'callback'),
                    (
                        ['retval', 'out'],
                        POINTER(POINTER(ISymUnmanagedReader)),
                        'pRetVal'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedBinder3_INTERFACE_DEFINED__

    # interface __MIDL_itf_corsym_0117
    # [local]
    if not defined(__ISymUnmanagedDispose_INTERFACE_DEFINED__):
        __ISymUnmanagedDispose_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedDispose
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedDispose = MIDL_INTERFACE(
                "{969708D2-05E5-4861-A3B0-96E473CDF63F}"
            )
            ISymUnmanagedDispose._iid_ = IID_ISymUnmanagedDispose

            ISymUnmanagedDispose._methods_ = [
                COMMETHOD(
                    [helpstring('Method Destroy')],
                    HRESULT,
                    'Destroy',
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedDispose_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedDocument_INTERFACE_DEFINED__):
        __ISymUnmanagedDocument_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedDocument
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedDocument = MIDL_INTERFACE(
                "{40DE4037-7C81-3E1E-B022-AE1ABFF2CA08}"
            )
            ISymUnmanagedDocument._iid_ = IID_ISymUnmanagedDocument

            ISymUnmanagedDocument._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetURL')],
                    HRESULT,
                    'GetURL',
                    (['in'], ULONG32, 'cchUrl'),
                    (['out'], POINTER(ULONG32), 'pcchUrl'),
                    (['out'], WCHAR * 0, 'szUrl'),
                ),
                COMMETHOD(
                    [helpstring('Method GetDocumentType')],
                    HRESULT,
                    'GetDocumentType',
                    (['out', 'retval'], POINTER(GUID), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetLanguage')],
                    HRESULT,
                    'GetLanguage',
                    (['retval', 'out'], POINTER(GUID), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetLanguageVendor')],
                    HRESULT,
                    'GetLanguageVendor',
                    (['out', 'retval'], POINTER(GUID), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCheckSumAlgorithmId')],
                    HRESULT,
                    'GetCheckSumAlgorithmId',
                    (['retval', 'out'], POINTER(GUID), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCheckSum')],
                    HRESULT,
                    'GetCheckSum',
                    (['in'], ULONG32, 'cData'),
                    (['out'], POINTER(ULONG32), 'pcData'),
                    (['out'], BYTE * 0, 'data'),
                ),
                COMMETHOD(
                    [helpstring('Method FindClosestLine')],
                    HRESULT,
                    'FindClosestLine',
                    (['in'], ULONG32, 'line'),
                    (['retval', 'out'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method HasEmbeddedSource')],
                    HRESULT,
                    'HasEmbeddedSource',
                    (['retval', 'out'], POINTER(BOOL), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSourceLength')],
                    HRESULT,
                    'GetSourceLength',
                    (['retval', 'out'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSourceRange')],
                    HRESULT,
                    'GetSourceRange',
                    (['in'], ULONG32, 'startLine'),
                    (['in'], ULONG32, 'startColumn'),
                    (['in'], ULONG32, 'endLine'),
                    (['in'], ULONG32, 'endColumn'),
                    (['in'], ULONG32, 'cSourceBytes'),
                    (['out'], POINTER(ULONG32), 'pcSourceBytes'),
                    (['out'], BYTE * 0, 'source'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedDocument_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedDocumentWriter_INTERFACE_DEFINED__):
        __ISymUnmanagedDocumentWriter_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedDocumentWriter
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedDocumentWriter = MIDL_INTERFACE(
                "{B01FAFEB-C450-3A4D-BEEC-B4CEEC01E006}"
            )
            ISymUnmanagedDocumentWriter._iid_ = IID_ISymUnmanagedDocumentWriter

            ISymUnmanagedDocumentWriter._methods_ = [
                COMMETHOD(
                    [helpstring('Method SetSource')],
                    HRESULT,
                    'SetSource',
                    (['in'], ULONG32, 'sourceSize'),
                    (['in'], BYTE * 0, 'source'),
                ),
                COMMETHOD(
                    [helpstring('Method SetCheckSum')],
                    HRESULT,
                    'SetCheckSum',
                    (['in'], GUID, 'algorithmId'),
                    (['in'], ULONG32, 'checkSumSize'),
                    (['in'], BYTE * 0, 'checkSum'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedDocumentWriter_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedMethod_INTERFACE_DEFINED__):
        __ISymUnmanagedMethod_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedMethod
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedMethod = MIDL_INTERFACE(
                "{B62B923C-B500-3158-A543-24F307A8B7E1}"
            )
            ISymUnmanagedMethod._iid_ = IID_ISymUnmanagedMethod

            ISymUnmanagedMethod._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetToken')],
                    HRESULT,
                    'GetToken',
                    (['retval', 'out'], POINTER(mdMethodDef), 'pToken'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSequencePointCount')],
                    HRESULT,
                    'GetSequencePointCount',
                    (['out', 'retval'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRootScope')],
                    HRESULT,
                    'GetRootScope',
                    (
                        ['retval', 'out'],
                        POINTER(POINTER(ISymUnmanagedScope)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetScopeFromOffset')],
                    HRESULT,
                    'GetScopeFromOffset',
                    (['in'], ULONG32, 'offset'),
                    (
                        ['retval', 'out'],
                        POINTER(POINTER(ISymUnmanagedScope)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetOffset')],
                    HRESULT,
                    'GetOffset',
                    (['in'], POINTER(ISymUnmanagedDocument), 'document'),
                    (['in'], ULONG32, 'line'),
                    (['in'], ULONG32, 'column'),
                    (['retval', 'out'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRanges')],
                    HRESULT,
                    'GetRanges',
                    (['in'], POINTER(ISymUnmanagedDocument), 'document'),
                    (['in'], ULONG32, 'line'),
                    (['in'], ULONG32, 'column'),
                    (['in'], ULONG32, 'cRanges'),
                    (['out'], POINTER(ULONG32), 'pcRanges'),
                    (['out'], ULONG32 * 0, 'ranges'),
                ),
                COMMETHOD(
                    [helpstring('Method GetParameters')],
                    HRESULT,
                    'GetParameters',
                    (['in'], ULONG32, 'cParams'),
                    (['out'], POINTER(ULONG32), 'pcParams'),
                    (['out'], POINTER(ISymUnmanagedVariable * 0), 'params'),
                ),
                COMMETHOD(
                    [helpstring('Method GetNamespace')],
                    HRESULT,
                    'GetNamespace',
                    (
                        ['out'],
                        POINTER(POINTER(ISymUnmanagedNamespace)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetSourceStartEnd')],
                    HRESULT,
                    'GetSourceStartEnd',
                    (['in'], 2, ']'),
                    (['in'], 2, ']'),
                    (['in'], 2, ']'),
                    (['out'], POINTER(BOOL), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSequencePoints')],
                    HRESULT,
                    'GetSequencePoints',
                    (['in'], ULONG32, 'cPoints'),
                    (['out'], POINTER(ULONG32), 'pcPoints'),
                    (['in'], ULONG32 * 0, 'offsets'),
                    (['in'], POINTER(ISymUnmanagedDocument * 0), 'documents'),
                    (['in'], ULONG32 * 0, 'lines'),
                    (['in'], ULONG32 * 0, 'columns'),
                    (['in'], ULONG32 * 0, 'endLines'),
                    (['in'], ULONG32 * 0, 'endColumns'),
                ),
            ]
        # END IF  C style interface
    # END IF  __ISymUnmanagedMethod_INTERFACE_DEFINED__

    if not defined(__ISymENCUnmanagedMethod_INTERFACE_DEFINED__):
        __ISymENCUnmanagedMethod_INTERFACE_DEFINED__ = VOID

        # interface ISymENCUnmanagedMethod
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymENCUnmanagedMethod = MIDL_INTERFACE(
                "{85E891DA-A631-4C76-ACA2-A44A39C46B8C}"
            )
            ISymENCUnmanagedMethod._iid_ = IID_ISymENCUnmanagedMethod

            ISymENCUnmanagedMethod._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetFileNameFromOffset')],
                    HRESULT,
                    'GetFileNameFromOffset',
                    (['in'], ULONG32, 'dwOffset'),
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
                COMMETHOD(
                    [helpstring('Method GetLineFromOffset')],
                    HRESULT,
                    'GetLineFromOffset',
                    (['in'], ULONG32, 'dwOffset'),
                    (['out'], POINTER(ULONG32), 'pline'),
                    (['out'], POINTER(ULONG32), 'pcolumn'),
                    (['out'], POINTER(ULONG32), 'pendLine'),
                    (['out'], POINTER(ULONG32), 'pendColumn'),
                    (['out'], POINTER(ULONG32), 'pdwStartOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method GetDocumentsForMethodCount')],
                    HRESULT,
                    'GetDocumentsForMethodCount',
                    (['retval', 'out'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetDocumentsForMethod')],
                    HRESULT,
                    'GetDocumentsForMethod',
                    (['in'], ULONG32, 'cDocs'),
                    (['out'], POINTER(ULONG32), 'pcDocs'),
                    (['in'], POINTER(ISymUnmanagedDocument * 0), 'documents'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSourceExtentInDocument')],
                    HRESULT,
                    'GetSourceExtentInDocument',
                    (['in'], POINTER(ISymUnmanagedDocument), 'document'),
                    (['out'], POINTER(ULONG32), 'pstartLine'),
                    (['out'], POINTER(ULONG32), 'pendLine'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymENCUnmanagedMethod_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedNamespace_INTERFACE_DEFINED__):
        __ISymUnmanagedNamespace_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedNamespace
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedNamespace = MIDL_INTERFACE(
                "{0DFF7289-54F8-11D3-BD28-0000F80849BD}"
            )
            ISymUnmanagedNamespace._iid_ = IID_ISymUnmanagedNamespace

            ISymUnmanagedNamespace._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetName')],
                    HRESULT,
                    'GetName',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
                COMMETHOD(
                    [helpstring('Method GetNamespaces')],
                    HRESULT,
                    'GetNamespaces',
                    (['in'], ULONG32, 'cNameSpaces'),
                    (['out'], POINTER(ULONG32), 'pcNameSpaces'),
                    (
                        ['out'],
                        POINTER(ISymUnmanagedNamespace * 0),
                        'namespaces'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetVariables')],
                    HRESULT,
                    'GetVariables',
                    (['in'], ULONG32, 'cVars'),
                    (['out'], POINTER(ULONG32), 'pcVars'),
                    (['out'], POINTER(ISymUnmanagedVariable * 0), 'pVars'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedNamespace_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedReader_INTERFACE_DEFINED__):
        __ISymUnmanagedReader_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedReader
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedReader = MIDL_INTERFACE(
                "{B4CE6286-2A6B-3712-A3B7-1EE1DAD467B5}"
            )
            ISymUnmanagedReader._iid_ = IID_ISymUnmanagedReader

            ISymUnmanagedReader._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetDocument')],
                    HRESULT,
                    'GetDocument',
                    (['in'], POINTER(WCHAR), 'url'),
                    (['in'], GUID, 'language'),
                    (['in'], GUID, 'languageVendor'),
                    (['in'], GUID, 'documentType'),
                    (
                        ['out', 'retval'],
                        POINTER(POINTER(ISymUnmanagedDocument)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetDocuments')],
                    HRESULT,
                    'GetDocuments',
                    (['in'], ULONG32, 'cDocs'),
                    (['out'], POINTER(ULONG32), 'pcDocs'),
                    (['out'], POINTER(ISymUnmanagedDocument * 0), 'pDocs'),
                ),
                COMMETHOD(
                    [helpstring('Method GetUserEntryPoint')],
                    HRESULT,
                    'GetUserEntryPoint',
                    (['out', 'retval'], POINTER(mdMethodDef), 'pToken'),
                ),
                COMMETHOD(
                    [helpstring('Method GetMethod')],
                    HRESULT,
                    'GetMethod',
                    (['in'], mdMethodDef, 'token'),
                    (
                        ['retval', 'out'],
                        POINTER(POINTER(ISymUnmanagedMethod)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetMethodByVersion')],
                    HRESULT,
                    'GetMethodByVersion',
                    (['in'], mdMethodDef, 'token'),
                    (['in'], INT, 'version'),
                    (
                        ['out', 'retval'],
                        POINTER(POINTER(ISymUnmanagedMethod)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetVariables')],
                    HRESULT,
                    'GetVariables',
                    (['in'], mdToken, 'parent'),
                    (['in'], ULONG32, 'cVars'),
                    (['out'], POINTER(ULONG32), 'pcVars'),
                    (['out'], POINTER(ISymUnmanagedVariable * 0), 'pVars'),
                ),
                COMMETHOD(
                    [helpstring('Method GetGlobalVariables')],
                    HRESULT,
                    'GetGlobalVariables',
                    (['in'], ULONG32, 'cVars'),
                    (['out'], POINTER(ULONG32), 'pcVars'),
                    (['out'], POINTER(ISymUnmanagedVariable * 0), 'pVars'),
                ),
                COMMETHOD(
                    [helpstring('Method GetMethodFromDocumentPosition')],
                    HRESULT,
                    'GetMethodFromDocumentPosition',
                    (['in'], POINTER(ISymUnmanagedDocument), 'document'),
                    (['in'], ULONG32, 'line'),
                    (['in'], ULONG32, 'column'),
                    (
                        ['out', 'retval'],
                        POINTER(POINTER(ISymUnmanagedMethod)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetSymAttribute')],
                    HRESULT,
                    'GetSymAttribute',
                    (['in'], mdToken, 'parent'),
                    (['in'], POINTER(WCHAR), 'name'),
                    (['in'], ULONG32, 'cBuffer'),
                    (['out'], POINTER(ULONG32), 'pcBuffer'),
                    (['out'], BYTE * 0, 'buffer'),
                ),
                COMMETHOD(
                    [helpstring('Method GetNamespaces')],
                    HRESULT,
                    'GetNamespaces',
                    (['in'], ULONG32, 'cNameSpaces'),
                    (['out'], POINTER(ULONG32), 'pcNameSpaces'),
                    (
                        ['out'],
                        POINTER(ISymUnmanagedNamespace * 0),
                        'namespaces'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method Initialize')],
                    HRESULT,
                    'Initialize',
                    (['in'], POINTER(comtypes.IUnknown), 'importer'),
                    (['in'], POINTER(WCHAR), 'filename'),
                    (['in'], POINTER(WCHAR), 'searchPath'),
                    (['in'], POINTER(IStream), 'pIStream'),
                ),
                COMMETHOD(
                    [helpstring('Method UpdateSymbolStore')],
                    HRESULT,
                    'UpdateSymbolStore',
                    (['in'], POINTER(WCHAR), 'filename'),
                    (['in'], POINTER(IStream), 'pIStream'),
                ),
                COMMETHOD(
                    [helpstring('Method ReplaceSymbolStore')],
                    HRESULT,
                    'ReplaceSymbolStore',
                    (['in'], POINTER(WCHAR), 'filename'),
                    (['in'], POINTER(IStream), 'pIStream'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSymbolStoreFileName')],
                    HRESULT,
                    'GetSymbolStoreFileName',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
                COMMETHOD(
                    [helpstring('Method GetMethodsFromDocumentPosition')],
                    HRESULT,
                    'GetMethodsFromDocumentPosition',
                    (['in'], POINTER(ISymUnmanagedDocument), 'document'),
                    (['in'], ULONG32, 'line'),
                    (['in'], ULONG32, 'column'),
                    (['in'], ULONG32, 'cMethod'),
                    (['out'], POINTER(ULONG32), 'pcMethod'),
                    (['out'], POINTER(ISymUnmanagedMethod * 0), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetDocumentVersion')],
                    HRESULT,
                    'GetDocumentVersion',
                    (['in'], POINTER(ISymUnmanagedDocument), 'pDoc'),
                    (['out'], POINTER(INT), 'version'),
                    (['out'], POINTER(BOOL), 'pbCurrent'),
                ),
                COMMETHOD(
                    [helpstring('Method GetMethodVersion')],
                    HRESULT,
                    'GetMethodVersion',
                    (['in'], POINTER(ISymUnmanagedMethod), 'pMethod'),
                    (['out'], POINTER(INT), 'version'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedReader_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedSourceServerModule_INTERFACE_DEFINED__):
        __ISymUnmanagedSourceServerModule_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedSourceServerModule
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedSourceServerModule = MIDL_INTERFACE(
                "{997DD0CC-A76F-4C82-8D79-EA87559D27AD}"
            )
            ISymUnmanagedSourceServerModule._iid_ = IID_ISymUnmanagedSourceServerModule

            ISymUnmanagedSourceServerModule._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetSourceServerData')],
                    HRESULT,
                    'GetSourceServerData',
                    (['out'], POINTER(ULONG), 'pDataByteCount'),
                    (['out'], POINTER(POINTER(BYTE)), 'ppData'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedSourceServerModule_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedENCUpdate_INTERFACE_DEFINED__):
        __ISymUnmanagedENCUpdate_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedENCUpdate
        # [unique][uuid][object]
        _SYMLINEDELTA._fields_ = [
            ('mdMethod', mdMethodDef),
            ('delta', INT32),
        ]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedENCUpdate = MIDL_INTERFACE(
                "{E502D2DD-8671-4338-8F2A-FC08229628C4}"
            )
            ISymUnmanagedENCUpdate._iid_ = IID_ISymUnmanagedENCUpdate

            ISymUnmanagedENCUpdate._methods_ = [
                COMMETHOD(
                    [helpstring('Method UpdateSymbolStore2')],
                    HRESULT,
                    'UpdateSymbolStore2',
                    (['in'], POINTER(IStream), 'pIStream'),
                    (['in'], POINTER(SYMLINEDELTA), 'pDeltaLines'),
                    (['in'], ULONG, 'cDeltaLines'),
                ),
                COMMETHOD(
                    [helpstring('Method GetLocalVariableCount')],
                    HRESULT,
                    'GetLocalVariableCount',
                    (['in'], mdMethodDef, 'mdMethodToken'),
                    (['out'], POINTER(ULONG), 'pcLocals'),
                ),
                COMMETHOD(
                    [helpstring('Method GetLocalVariables')],
                    HRESULT,
                    'GetLocalVariables',
                    (['in'], mdMethodDef, 'mdMethodToken'),
                    (['in'], ULONG, 'cLocals'),
                    (['out'], POINTER(ISymUnmanagedVariable * 0), 'rgLocals'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
                COMMETHOD(
                    [helpstring('Method InitializeForEnc')],
                    HRESULT,
                    'InitializeForEnc',
                ),
                COMMETHOD(
                    [helpstring('Method UpdateMethodLines')],
                    HRESULT,
                    'UpdateMethodLines',
                    (['in'], mdMethodDef, 'mdMethodToken'),
                    (['in'], POINTER(INT32), 'pDeltas'),
                    (['in'], ULONG, 'cDeltas'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedENCUpdate_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedReaderSymbolSearchInfo_INTERFACE_DEFINED__):
        __ISymUnmanagedReaderSymbolSearchInfo_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedReaderSymbolSearchInfo
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedReaderSymbolSearchInfo = MIDL_INTERFACE(
                "{20D9645D-03CD-4E34-9C11-9848A5B084F1}"
            )
            ISymUnmanagedReaderSymbolSearchInfo._iid_ = IID_ISymUnmanagedReaderSymbolSearchInfo

            ISymUnmanagedReaderSymbolSearchInfo._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetSymbolSearchInfoCount')],
                    HRESULT,
                    'GetSymbolSearchInfoCount',
                    (['out'], POINTER(ULONG32), 'pcSearchInfo'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSymbolSearchInfo')],
                    HRESULT,
                    'GetSymbolSearchInfo',
                    (['in'], ULONG32, 'cSearchInfo'),
                    (['out'], POINTER(ULONG32), 'pcSearchInfo'),
                    (
                        ['out'],
                        POINTER(POINTER(ISymUnmanagedSymbolSearchInfo)),
                        'rgpSearchInfo'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedReaderSymbolSearchInfo_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedScope_INTERFACE_DEFINED__):
        __ISymUnmanagedScope_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedScope
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedScope = MIDL_INTERFACE(
                "{68005D0F-B8E0-3B01-84D5-A11A94154942}"
            )
            ISymUnmanagedScope._iid_ = IID_ISymUnmanagedScope

            ISymUnmanagedScope._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetMethod')],
                    HRESULT,
                    'GetMethod',
                    (
                        ['retval', 'out'],
                        POINTER(POINTER(ISymUnmanagedMethod)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetParent')],
                    HRESULT,
                    'GetParent',
                    (
                        ['out', 'retval'],
                        POINTER(POINTER(ISymUnmanagedScope)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetChildren')],
                    HRESULT,
                    'GetChildren',
                    (['in'], ULONG32, 'cChildren'),
                    (['out'], POINTER(ULONG32), 'pcChildren'),
                    (['out'], POINTER(ISymUnmanagedScope * 0), 'children'),
                ),
                COMMETHOD(
                    [helpstring('Method GetStartOffset')],
                    HRESULT,
                    'GetStartOffset',
                    (['out', 'retval'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetEndOffset')],
                    HRESULT,
                    'GetEndOffset',
                    (['retval', 'out'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetLocalCount')],
                    HRESULT,
                    'GetLocalCount',
                    (['out', 'retval'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetLocals')],
                    HRESULT,
                    'GetLocals',
                    (['in'], ULONG32, 'cLocals'),
                    (['out'], POINTER(ULONG32), 'pcLocals'),
                    (['out'], POINTER(ISymUnmanagedVariable * 0), 'locals'),
                ),
                COMMETHOD(
                    [helpstring('Method GetNamespaces')],
                    HRESULT,
                    'GetNamespaces',
                    (['in'], ULONG32, 'cNameSpaces'),
                    (['out'], POINTER(ULONG32), 'pcNameSpaces'),
                    (
                        ['out'],
                        POINTER(ISymUnmanagedNamespace * 0),
                        'namespaces'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedScope_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedConstant_INTERFACE_DEFINED__):
        __ISymUnmanagedConstant_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedConstant
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedConstant = MIDL_INTERFACE(
                "{48B25ED8-5BAD-41BC-9CEE-CD62FABC74E9}"
            )
            ISymUnmanagedConstant._iid_ = IID_ISymUnmanagedConstant

            ISymUnmanagedConstant._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetName')],
                    HRESULT,
                    'GetName',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
                COMMETHOD(
                    [helpstring('Method GetValue')],
                    HRESULT,
                    'GetValue',
                    ([], POINTER(VARIANT), 'pValue'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSignature')],
                    HRESULT,
                    'GetSignature',
                    (['in'], ULONG32, 'cSig'),
                    (['out'], POINTER(ULONG32), 'pcSig'),
                    (['out'], BYTE * 0, 'sig'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedConstant_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedScope2_INTERFACE_DEFINED__):
        __ISymUnmanagedScope2_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedScope2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedScope2 = MIDL_INTERFACE(
                "{AE932FBA-3FD8-4DBA-8232-30A2309B02DB}"
            )
            ISymUnmanagedScope2._iid_ = IID_ISymUnmanagedScope2

            ISymUnmanagedScope2._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetConstantCount')],
                    HRESULT,
                    'GetConstantCount',
                    (['retval', 'out'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetConstants')],
                    HRESULT,
                    'GetConstants',
                    (['in'], ULONG32, 'cConstants'),
                    (['out'], POINTER(ULONG32), 'pcConstants'),
                    (
                        ['out'],
                        POINTER(ISymUnmanagedConstant * 0),
                        'constants'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedScope2_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedVariable_INTERFACE_DEFINED__):
        __ISymUnmanagedVariable_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedVariable
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedVariable = MIDL_INTERFACE(
                "{9F60EEBE-2D9A-3F7C-BF58-80BC991C60BB}"
            )
            ISymUnmanagedVariable._iid_ = IID_ISymUnmanagedVariable

            ISymUnmanagedVariable._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetName')],
                    HRESULT,
                    'GetName',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
                COMMETHOD(
                    [helpstring('Method GetAttributes')],
                    HRESULT,
                    'GetAttributes',
                    (['out', 'retval'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSignature')],
                    HRESULT,
                    'GetSignature',
                    (['in'], ULONG32, 'cSig'),
                    (['out'], POINTER(ULONG32), 'pcSig'),
                    (['out'], BYTE * 0, 'sig'),
                ),
                COMMETHOD(
                    [helpstring('Method GetAddressKind')],
                    HRESULT,
                    'GetAddressKind',
                    (['retval', 'out'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetAddressField1')],
                    HRESULT,
                    'GetAddressField1',
                    (['out', 'retval'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetAddressField2')],
                    HRESULT,
                    'GetAddressField2',
                    (['out', 'retval'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetAddressField3')],
                    HRESULT,
                    'GetAddressField3',
                    (['retval', 'out'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetStartOffset')],
                    HRESULT,
                    'GetStartOffset',
                    (['retval', 'out'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method GetEndOffset')],
                    HRESULT,
                    'GetEndOffset',
                    (['retval', 'out'], POINTER(ULONG32), 'pRetVal'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedVariable_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedSymbolSearchInfo_INTERFACE_DEFINED__):
        __ISymUnmanagedSymbolSearchInfo_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedSymbolSearchInfo
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedSymbolSearchInfo = MIDL_INTERFACE(
                "{F8B3534A-A46B-4980-B520-BEC4ACEABA8F}"
            )
            ISymUnmanagedSymbolSearchInfo._iid_ = IID_ISymUnmanagedSymbolSearchInfo

            ISymUnmanagedSymbolSearchInfo._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetSearchPathLength')],
                    HRESULT,
                    'GetSearchPathLength',
                    (['out'], POINTER(ULONG32), 'pcchPath'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSearchPath')],
                    HRESULT,
                    'GetSearchPath',
                    (['in'], ULONG32, 'cchPath'),
                    (['out'], POINTER(ULONG32), 'pcchPath'),
                    (['out'], WCHAR * 0, 'szPath'),
                ),
                COMMETHOD(
                    [helpstring('Method GetHRESULT')],
                    HRESULT,
                    'GetHRESULT',
                    (['out'], POINTER(HRESULT), 'phr'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedSymbolSearchInfo_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedWriter_INTERFACE_DEFINED__):
        __ISymUnmanagedWriter_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedWriter
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedWriter = MIDL_INTERFACE(
                "{ED14AA72-78E2-4884-84E2-334293AE5214}"
            )
            ISymUnmanagedWriter._iid_ = IID_ISymUnmanagedWriter

            ISymUnmanagedWriter._methods_ = [
                COMMETHOD(
                    [helpstring('Method DefineDocument')],
                    HRESULT,
                    'DefineDocument',
                    (['in'], POINTER(WCHAR), 'url'),
                    (['in'], POINTER(GUID), 'language'),
                    (['in'], POINTER(GUID), 'languageVendor'),
                    (['in'], POINTER(GUID), 'documentType'),
                    (
                        ['out', 'retval'],
                        POINTER(POINTER(ISymUnmanagedDocumentWriter)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method SetUserEntryPoint')],
                    HRESULT,
                    'SetUserEntryPoint',
                    (['in'], mdMethodDef, 'entryMethod'),
                ),
                COMMETHOD(
                    [helpstring('Method OpenMethod')],
                    HRESULT,
                    'OpenMethod',
                    (['in'], mdMethodDef, 'method'),
                ),
                COMMETHOD(
                    [helpstring('Method CloseMethod')],
                    HRESULT,
                    'CloseMethod',
                ),
                COMMETHOD(
                    [helpstring('Method OpenScope')],
                    HRESULT,
                    'OpenScope',
                    (['in'], ULONG32, 'startOffset'),
                    (['retval', 'out'], POINTER(ULONG32), 'pRetVal'),
                ),
                COMMETHOD(
                    [helpstring('Method CloseScope')],
                    HRESULT,
                    'CloseScope',
                    (['in'], ULONG32, 'endOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method SetScopeRange')],
                    HRESULT,
                    'SetScopeRange',
                    (['in'], ULONG32, 'scopeID'),
                    (['in'], ULONG32, 'startOffset'),
                    (['in'], ULONG32, 'endOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method DefineLocalVariable')],
                    HRESULT,
                    'DefineLocalVariable',
                    (['in'], POINTER(WCHAR), 'name'),
                    (['in'], ULONG32, 'attributes'),
                    (['in'], ULONG32, 'cSig'),
                    (['in'], UCHAR * 0, 'signature'),
                    (['in'], ULONG32, 'addrKind'),
                    (['in'], ULONG32, 'addr1'),
                    (['in'], ULONG32, 'addr2'),
                    (['in'], ULONG32, 'addr3'),
                    (['in'], ULONG32, 'startOffset'),
                    (['in'], ULONG32, 'endOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method DefineParameter')],
                    HRESULT,
                    'DefineParameter',
                    (['in'], POINTER(WCHAR), 'name'),
                    (['in'], ULONG32, 'attributes'),
                    (['in'], ULONG32, 'sequence'),
                    (['in'], ULONG32, 'addrKind'),
                    (['in'], ULONG32, 'addr1'),
                    (['in'], ULONG32, 'addr2'),
                    (['in'], ULONG32, 'addr3'),
                ),
                COMMETHOD(
                    [helpstring('Method DefineField')],
                    HRESULT,
                    'DefineField',
                    (['in'], mdTypeDef, 'parent'),
                    (['in'], POINTER(WCHAR), 'name'),
                    (['in'], ULONG32, 'attributes'),
                    (['in'], ULONG32, 'cSig'),
                    (['in'], UCHAR * 0, 'signature'),
                    (['in'], ULONG32, 'addrKind'),
                    (['in'], ULONG32, 'addr1'),
                    (['in'], ULONG32, 'addr2'),
                    (['in'], ULONG32, 'addr3'),
                ),
                COMMETHOD(
                    [helpstring('Method DefineGlobalVariable')],
                    HRESULT,
                    'DefineGlobalVariable',
                    (['in'], POINTER(WCHAR), 'name'),
                    (['in'], ULONG32, 'attributes'),
                    (['in'], ULONG32, 'cSig'),
                    (['in'], UCHAR * 0, 'signature'),
                    (['in'], ULONG32, 'addrKind'),
                    (['in'], ULONG32, 'addr1'),
                    (['in'], ULONG32, 'addr2'),
                    (['in'], ULONG32, 'addr3'),
                ),
                COMMETHOD(
                    [helpstring('Method Close')],
                    HRESULT,
                    'Close',
                ),
                COMMETHOD(
                    [helpstring('Method SetSymAttribute')],
                    HRESULT,
                    'SetSymAttribute',
                    (['in'], mdToken, 'parent'),
                    (['in'], POINTER(WCHAR), 'name'),
                    (['in'], ULONG32, 'cData'),
                    (['in'], UCHAR * 0, 'data'),
                ),
                COMMETHOD(
                    [helpstring('Method OpenNamespace')],
                    HRESULT,
                    'OpenNamespace',
                    (['in'], POINTER(WCHAR), 'name'),
                ),
                COMMETHOD(
                    [helpstring('Method CloseNamespace')],
                    HRESULT,
                    'CloseNamespace',
                ),
                COMMETHOD(
                    [helpstring('Method UsingNamespace')],
                    HRESULT,
                    'UsingNamespace',
                    (['in'], POINTER(WCHAR), 'fullName'),
                ),
                COMMETHOD(
                    [helpstring('Method SetMethodSourceRange')],
                    HRESULT,
                    'SetMethodSourceRange',
                    (
                        ['in'],
                        POINTER(ISymUnmanagedDocumentWriter),
                        'startDoc'
                    ),
                    (['in'], ULONG32, 'startLine'),
                    (['in'], ULONG32, 'startColumn'),
                    (['in'], POINTER(ISymUnmanagedDocumentWriter), 'endDoc'),
                    (['in'], ULONG32, 'endLine'),
                    (['in'], ULONG32, 'endColumn'),
                ),
                COMMETHOD(
                    [helpstring('Method Initialize')],
                    HRESULT,
                    'Initialize',
                    (['in'], POINTER(comtypes.IUnknown), 'emitter'),
                    (['in'], POINTER(WCHAR), 'filename'),
                    (['in'], POINTER(IStream), 'pIStream'),
                    (['in'], BOOL, 'fFullBuild'),
                ),
                COMMETHOD(
                    [helpstring('Method GetDebugInfo')],
                    HRESULT,
                    'GetDebugInfo',
                    (['out', 'in'], POINTER(IMAGE_DEBUG_DIRECTORY), 'pIDD'),
                    (['in'], DWORD, 'cData'),
                    (['out'], POINTER(DWORD), 'pcData'),
                    (['out'], BYTE * 0, 'data'),
                ),
                COMMETHOD(
                    [helpstring('Method DefineSequencePoints')],
                    HRESULT,
                    'DefineSequencePoints',
                    (
                        ['in'],
                        POINTER(ISymUnmanagedDocumentWriter),
                        'document'
                    ),
                    (['in'], ULONG32, 'spCount'),
                    (['in'], ULONG32 * 0, 'offsets'),
                    (['in'], ULONG32 * 0, 'lines'),
                    (['in'], ULONG32 * 0, 'columns'),
                    (['in'], ULONG32 * 0, 'endLines'),
                    (['in'], ULONG32 * 0, 'endColumns'),
                ),
                COMMETHOD(
                    [helpstring('Method RemapToken')],
                    HRESULT,
                    'RemapToken',
                    (['in'], mdToken, 'oldToken'),
                    (['in'], mdToken, 'newToken'),
                ),
                COMMETHOD(
                    [helpstring('Method Initialize2')],
                    HRESULT,
                    'Initialize2',
                    (['in'], POINTER(comtypes.IUnknown), 'emitter'),
                    (['in'], POINTER(WCHAR), 'tempfilename'),
                    (['in'], POINTER(IStream), 'pIStream'),
                    (['in'], BOOL, 'fFullBuild'),
                    (['in'], POINTER(WCHAR), 'finalfilename'),
                ),
                COMMETHOD(
                    [helpstring('Method DefineConstant')],
                    HRESULT,
                    'DefineConstant',
                    (['in'], POINTER(WCHAR), 'name'),
                    (['in'], VARIANT, 'value'),
                    (['in'], ULONG32, 'cSig'),
                    (['in'], UCHAR * 0, 'signature'),
                ),
                COMMETHOD(
                    [helpstring('Method Abort')],
                    HRESULT,
                    'Abort',
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedWriter_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedWriter2_INTERFACE_DEFINED__):
        __ISymUnmanagedWriter2_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedWriter2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedWriter2 = MIDL_INTERFACE(
                "{0B97726E-9E6D-4F05-9A26-424022093CAA}"
            )
            ISymUnmanagedWriter2._iid_ = IID_ISymUnmanagedWriter2

            ISymUnmanagedWriter2._methods_ = [
                COMMETHOD(
                    [helpstring('Method DefineLocalVariable2')],
                    HRESULT,
                    'DefineLocalVariable2',
                    (['in'], POINTER(WCHAR), 'name'),
                    (['in'], ULONG32, 'attributes'),
                    (['in'], mdSignature, 'sigToken'),
                    (['in'], ULONG32, 'addrKind'),
                    (['in'], ULONG32, 'addr1'),
                    (['in'], ULONG32, 'addr2'),
                    (['in'], ULONG32, 'addr3'),
                    (['in'], ULONG32, 'startOffset'),
                    (['in'], ULONG32, 'endOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method DefineGlobalVariable2')],
                    HRESULT,
                    'DefineGlobalVariable2',
                    (['in'], POINTER(WCHAR), 'name'),
                    (['in'], ULONG32, 'attributes'),
                    (['in'], mdSignature, 'sigToken'),
                    (['in'], ULONG32, 'addrKind'),
                    (['in'], ULONG32, 'addr1'),
                    (['in'], ULONG32, 'addr2'),
                    (['in'], ULONG32, 'addr3'),
                ),
                COMMETHOD(
                    [helpstring('Method DefineConstant2')],
                    HRESULT,
                    'DefineConstant2',
                    (['in'], POINTER(WCHAR), 'name'),
                    (['in'], VARIANT, 'value'),
                    (['in'], mdSignature, 'sigToken'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedWriter2_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedWriter3_INTERFACE_DEFINED__):
        __ISymUnmanagedWriter3_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedWriter3
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedWriter3 = MIDL_INTERFACE(
                "{12F1E02C-1E05-4B0E-9468-EBC9D1BB040F}"
            )
            ISymUnmanagedWriter3._iid_ = IID_ISymUnmanagedWriter3

            ISymUnmanagedWriter3._methods_ = [
                COMMETHOD(
                    [helpstring('Method OpenMethod2')],
                    HRESULT,
                    'OpenMethod2',
                    (['in'], mdMethodDef, 'method'),
                    (['in'], ULONG32, 'isect'),
                    (['in'], ULONG32, 'offset'),
                ),
                COMMETHOD(
                    [helpstring('Method Commit')],
                    HRESULT,
                    'Commit',
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedWriter3_INTERFACE_DEFINED__

    if not defined(__ISymUnmanagedReader2_INTERFACE_DEFINED__):
        __ISymUnmanagedReader2_INTERFACE_DEFINED__ = VOID

        # interface ISymUnmanagedReader2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ISymUnmanagedReader2 = MIDL_INTERFACE(
                "{A09E53B2-2A57-4CCA-8F63-B84F7C35D4AA}"
            )
            ISymUnmanagedReader2._iid_ = IID_ISymUnmanagedReader2

            ISymUnmanagedReader2._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetMethodByVersionPreRemap')],
                    HRESULT,
                    'GetMethodByVersionPreRemap',
                    (['in'], mdMethodDef, 'token'),
                    (['in'], INT, 'version'),
                    (
                        ['out', 'retval'],
                        POINTER(POINTER(ISymUnmanagedMethod)),
                        'pRetVal'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetSymAttributePreRemap')],
                    HRESULT,
                    'GetSymAttributePreRemap',
                    (['in'], mdToken, 'parent'),
                    (['in'], POINTER(WCHAR), 'name'),
                    (['in'], ULONG32, 'cBuffer'),
                    (['out'], POINTER(ULONG32), 'pcBuffer'),
                    (['out'], BYTE * 0, 'buffer'),
                ),
                COMMETHOD(
                    [helpstring('Method GetMethodsInDocument')],
                    HRESULT,
                    'GetMethodsInDocument',
                    (['in'], POINTER(ISymUnmanagedDocument), 'document'),
                    (['in'], ULONG32, 'cMethod'),
                    (['out'], POINTER(ULONG32), 'pcMethod'),
                    (['out'], POINTER(ISymUnmanagedMethod * 0), 'pRetVal'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ISymUnmanagedReader2_INTERFACE_DEFINED__

    # Additional Prototypes for ALL interfaces
    oleaut32 = ctypes.windll.OLEAUT32

    # ULONG VARIANT_UserSize(ULONG *, ULONG, VARIANT *);
    VARIANT_UserSize = oleaut32.VARIANT_UserSize
    VARIANT_UserSize.restype = ULONG

    # UCHAR *  VARIANT_UserMarshal(  ULONG *, UCHAR *, VARIANT * );
    VARIANT_UserMarshal = oleaut32.VARIANT_UserMarshal
    VARIANT_UserMarshal.restype = UCHAR

    # UCHAR *  VARIANT_UserUnmarshal(unsigned LONG *, UCHAR *, VARIANT * );
    VARIANT_UserUnmarshal = oleaut32.VARIANT_UserUnmarshal
    VARIANT_UserUnmarshal.restype = UCHAR

    # VOID                       VARIANT_UserFree(     ULONG *, VARIANT * );
    VARIANT_UserFree = oleaut32.VARIANT_UserFree
    VARIANT_UserFree.restype = VOID

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


