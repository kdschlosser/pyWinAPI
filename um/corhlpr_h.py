import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__CORHLPR_H__ = None
_BLD_CLR = None
IfFailGoto = None
IfFailGo = None
IfFailRet = None
IfNullRet = None
_ASSERTE = None
COUNTOF = None
SOS_INCLUDE = None

class IMAGE_COR_ILMETHOD_SECT_SMALL(tagCOR_ILMETHOD_SECT_SMALL):
    pass


COR_ILMETHOD_SECT_SMALL = IMAGE_COR_ILMETHOD_SECT_SMALL


class IMAGE_COR_ILMETHOD_SECT_FAT(tagCOR_ILMETHOD_SECT_FAT):
    pass


COR_ILMETHOD_SECT_FAT = IMAGE_COR_ILMETHOD_SECT_FAT


class COR_ILMETHOD_SECT(ctypes.Structure):
    pass


class IMAGE_COR_ILMETHOD_TINY(tagCOR_ILMETHOD_TINY):
    pass


COR_ILMETHOD_TINY = IMAGE_COR_ILMETHOD_TINY


class IMAGE_COR_ILMETHOD_FAT(tagCOR_ILMETHOD_FAT):
    pass


COR_ILMETHOD_FAT = IMAGE_COR_ILMETHOD_FAT


class COR_ILMETHOD(ctypes.Structure):
    pass


# == + + ==
# Copyright (c) Microsoft Corporation. All rights reserved.
# == -- ==
# ***************************************************************************
# *   ** * Corhlpr.h - <STRIP>this file contains a set of "as is" code that
# may be ** * used by developers writing compilers and tools against ** * the
# Common Language Runtime. The code is not officially ** * supported, but is
# code being used by the Runtime itself. ** * </STRIP> ** * **
# **************************************************************************
if not defined(__CORHLPR_H__):
    __CORHLPR_H__ = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        from pyWinAPI.um.cor_h import * # NOQA
        from pyWinAPI.um.corhdr_h import * # NOQA
        from pyWinAPI.um.corerror_h import * # NOQA

        # This header is consumed both within the runtime and externally. In
        # the former
        # case we need to wrap memory allocations, in the latter there is no
        # infrastructure to support this. Detect which way we're building and
        # provide a
        # very simple abstraction layer (handles allocating bytes only).
        if defined(_BLD_CLR):
            from new_hpp import * # NOQA


            def NEW_NOTHROW(_bytes):
                return n_bytes


            def NEW_THROWS(_bytes):
                return _bytes
        else:
            def NEW_NOTHROW(_bytes):
                return _bytes


            def NEW_THROWS(_bytes):
                return __CorHlprNewThrows(_bytes)

        # END IF


        # ******************************************************************
        # There are a set of macros commonly used in the helpers which you
        # will want
        # to override to get richer behavior. The following defines what is
        # needed
        # if you chose not to do the extra work.
        # ******************************************************************
        if not defined(IfFailGoto):
            def IfFailGoto(EXPR, LABEL):
                hr = EXPR
                if FAILED(hr):
                    LABEL()
        # END IF


        if not defined(IfFailGo):
            def IfFailGo(EXPR):
                return IfFailGoto(EXPR, ErrExit)
        # END IF


        if not defined(IfFailRet):
            def IfFailRet(EXPR):
                hr = EXPR
                if FAILED(hr):
                    return hr

        # END IF


        if not defined(IfNullRet):
            def IfNullRet(EXPR):
                if (EXPR == NULL):
                    return E_OUTOFMEMORY

        # END IF


        if not defined(_ASSERTE):
            _ASSERTE = VOID
        # END IF


        if not defined(COUNTOF):
            def COUNTOF(a):
                return ctypes.sizeof(a) / ctypes.sizeof(ctypes.byref(a))


        # END IF
        if not BIGENDIAN:
            def VAL16(x):
                return x


            def VAL32(x):
                return x
        # END IF


        # ******************************************************************
        # **** Macro to assist with cleaning up local static variables
        # ******************************************************************
        def CHECK_LOCAL_STATIC_VAR(x):
            return x

        # ******************************************************************
        # **** Utility helpers
        # ******************************************************************
        MAX_CLASSNAME_LENGTH = 1024
        if not defined(SOS_INCLUDE):
            # **************************************************************
            # **** CQuickBytes
            # This helper class is useful for cases where 90% of the time you
            # allocate 512
            # or less bytes for a data structure. This class contains a 512
            # byte buffer.
            # Alloc() will return a pointer to this buffer if your allocation
            # is small
            # enough, otherwise it asks the heap for a larger buffer which is
            # freed for
            # you. No mutex locking is required for the small allocation case,
            # making the
            # code run faster, less heap fragmentation, etc... Each instance
            # will allocate
            # 520 bytes, so use accordinly.
            # **************************************************************
            if defined(_BLD_CLR):
                if defined(_DEBUG):
                    # Exercise heap for OOM-fault injection purposes
                    pass
                # END IF
            # END IF


            # We need the following line to make data structure consistant if
            # new throws.
            if defined(_BLD_CLR):
                if defined(_DEBUG):
                    # Exercise heap for OOM-fault injection purposes
                    pass
                # END IF
            # END IF


            if defined(_BLD_CLR):
                if defined(_DEBUG):
                    # Exercise heap for OOM-fault injection purposes
                    pass
                # END IF
            # END IF


            # number of bytes used            # total bytes allocated in the buffer
            # use UINT64 to enforce the alignment of the memory
            # These should be multiples of 8 so that data can be naturally
            # aligned.
            CQUICKBYTES_BASE_SIZE = 512
            CQUICKBYTES_INCREMENTAL_SIZE = 128
            # /* to be used as static variable - no constructor/destructor,
            # assumes zero initialized memory
            # /* to be used as static variable - no constructor/destructor,
            # assumes zero initialized memory
            # /* to be used as static variable - no constructor/destructor,
            # assumes zero initialized memory

        # END IF   SOS_INCLUDE
        # ******************************************************************
        # **** Signature helpers
        # ******************************************************************
        #  S_OK or error.
        #  [IN] point to a blob of CLR signature
        #  [IN] size of signature
        #  [OUT] output buffer for fixed part of VarArg Signature
        #  [OUT] number of bytes written to the above output buffer
        # ******************************************************************
        # **** File format helper classes
        # ******************************************************************
        # ******************************************************************
        # Data follows

        # ********************************
        # NOTE this structure must be DWORD alignednot not
        # Data follows

        # Endian-safe wrappers
        # ******************************************************************
        # Endian-safe wrappers
        # ******************************************************************
        # ********************************
        # NOTE this structure must be DWORD alignednot not

        # *******************************
        # exported functions (implementation in Format\Format.cpp:
        # compute the size of the section (best format)
        # codeSize is the size of the method
        # deprecated
        # will return worse-case size and then Emit will return actual size
        # will return exact size which will match the size returned by Emit
        # emit the section (best format);        # extern "C"
        # *************************************************************
        # Used when the method is tiny (< 64 bytes), and there are no local
        # vars

        # ********************************
        # This strucuture is the 'fat' layout, where no compression is
        # attempted.
        # Note that this structure can be added on at the end, thus making it
        # extensible

        # ********************************
        # exported functions (impl. Format\Format.cpp)
        # emit the header (bestFormat) return amount emitted
        class _Union_2(ctypes.Union):
            pass


        _Union_2._fields_ = [
            ('Tiny', COR_ILMETHOD_TINY),
            ('Fat', COR_ILMETHOD_FAT),
        ]
        COR_ILMETHOD._Union_2 = _Union_2

        COR_ILMETHOD._anonymous_ = (
            '_Union_2',
        )

        COR_ILMETHOD._fields_ = [
            # COR_ILMETHOD_DECODER to decode it.
            ('class COR_ILMETHOD_DECODER', friend),
            # compute the size of the header (best format)
            ('static Size( COR_ILMETHOD_FAT* header', UINT),
            # compute the size of the header (best format)
            ('BOOL MoreSections) return IlmethodSize((COR_ILMETHOD_FAT*)header', UINT),
            # compute the size of the header (best format)
            ('MoreSections)', UINT),
            # emit the header (bestFormat) return amount emitted
            ('static Emit(unsigned size', UINT),
            # emit the header (bestFormat) return amount emitted
            ('COR_ILMETHOD_FAT* header', UINT),
            # emit the header (bestFormat) return amount emitted
            ('BOOL moreSections', UINT),
            # emit the header (bestFormat) return amount emitted
            ('BYTE* outBuff) return IlmethodEmit(size', UINT),
            # emit the header (bestFormat) return amount emitted
            ('(COR_ILMETHOD_FAT*)header', UINT),
            # emit the header (bestFormat) return amount emitted
            ('moreSections', UINT),
            # emit the header (bestFormat) return amount emitted
            ('outBuff)', UINT),
            # private:
            ('_Union_2', COR_ILMETHOD._Union_2),
        ]

        # *************************************************************
        # /* COR_ILMETHOD_DECODER is the only way functions internal to the EE
        # should fetch data from a COR_ILMETHOD. This way any dependancy on
        # the file format (and the multiple ways of encoding the header) is
        # centralized to the COR_ILMETHOD_DECODER constructor)        # extern "C"
        # Typically the ONLY way you should access COR_ILMETHOD is through
        # this constructor so format changes are easier.
        # The above variant of the constructor can not do a 'complete' job,
        # because
        # it can not look up the local variable signature meta-data token.
        # This method should be used when you have access to the Meta data API
        # If the construction fails, the 'Code' field is set to 0

        # If we want the decoder to verify the that local signature is OK we
        # will pass a non-NULL value for wbStatus
        # When using LazyInit we want ask that the local signature be verified
        # But if we fail verification we still need access to the 'Code' field
        # Because we may be able to demand SkipVerification and thus it was OK
        # to have had a verification error.
        # returns total size of method for use in copying
        # Flags  these are available because we inherit COR_ILMETHOD_FAT
        # MaxStack
        # CodeSize
        #  pointer to signature blob, or 0 if none
        #  eh table if any 0 if none
        #  additional sections 0 if none
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   __CORHLPR_H__
