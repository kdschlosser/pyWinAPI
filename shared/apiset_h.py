from pyWinAPI import *

# /* + + Copyright (c) 2008 Microsoft Corporation Module Name: apiset.h
# Abstract: This module contains definitions related to the management of API
# namespaces. Author: Arun Kishan (arunki) 14 - Sep - 2008 - -
_API_SET_H_ = None
if not defined(_API_SET_H_):
    _API_SET_H_ = 1

    # API set interface definitions.
    def API_SET_OVERRIDE(X):
        return X ##Implementation


    def API_SET_LEGACY_OVERRIDE_DEF(X):
        return API_SET_OVERRIDE(X)


    def API_SET_OVERRIDE_DEF(X):
        return API_SET_LEGACY_OVERRIDE_DEF(X) # PRIVATE


    _M_HYBRID_X86_ARM64 = None

    if defined(_M_HYBRID_X86_ARM64):
        API_SET_CHPE_GUEST = X86
    else:
        API_SET_CHPE_GUEST = 1

    _API_SET_HOST = 1
    if defined(_API_SET_HOST):

        def API_SET_LIBRARY(X):
            pass

        def API_SET(X):
            return X # PRIVATE


        def API_SET_DIR(X, DIR):
            return X # DIR PRIVATE


        def API_SET_PRIVATE(X):
            return X # PRIVATE


        def API_SET_PRIVATE_DIR(X, DIR):
            return X # DIR PRIVATE


        def API_SET_BY_ORDINAL(X, O, PO):
            return X # @##O NONAME PRIVATE


        def API_SET_BY_ORDINAL_DIR(X, O, PO, DIR):
            return X #  @##O NONAME DIR PRIVATE


        def API_SET_BY_ORDINAL_PRIVATE(X, O, PO):
            return X # @##O NONAME PRIVATE


        def API_SET_BY_ORDINAL_PRIVATE_DIR(X, O, PO, DIR):
            return X # @##O NONAME DIR PRIVATE


        def API_SET_LEGACY(X, L):
            return X # PRIVATE


        def API_SET_LEGACY_DIR(X, L, DIR):
            return X # DIR PRIVATE


        def API_SET_LEGACY_PRIVATE(X, L):
            return X # PRIVATE


        def API_SET_LEGACY_PRIVATE_DIR(X, L, DIR):
            return X # DIR PRIVATE


        def API_SET_LEGACY_BY_ORDINAL(X, L, O, PO):
            return X # @##O NONAME PRIVATE


        def API_SET_LEGACY_BY_ORDINAL_DIR(X, L, O, PO, DIR):
            return X # @##O NONAME DIR PRIVATE


        def API_SET_LEGACY_BY_ORDINAL_PRIVATE(X, L, O, PO):
            return X # @##O NONAME PRIVATE


        def API_SET_LEGACY_BY_ORDINAL_PRIVATE_DIR(X, L, O, PO, DIR):
            return X # @##O NONAME DIR PRIVATE
    else:
        _API_SET_LEGACY_TARGET = 1

        if not defined(_API_SET_LEGACY_TARGET):
            def API_SET(X):
                return X


            def API_SET_DIR(X, DIR):
                return X # DIR


            def API_SET_PRIVATE(X):
                return X # PRIVATE


            def API_SET_PRIVATE_DIR(X, DIR):
                return X # DIR PRIVATE


            def API_SET_BY_ORDINAL(X, O, PO):
                return X # @##O NONAME


            def API_SET_BY_ORDINAL_DIR(X, O, PO, DIR):
                return X # @##O NONAME DIR


            def API_SET_BY_ORDINAL_PRIVATE(X, O, PO):
                return X # @##O NONAME PRIVATE


            def API_SET_BY_ORDINAL_PRIVATE_DIR(X, O, PO, DIR):
                return X # @##O NONAME DIR PRIVATE


            def API_SET_LEGACY(X, L):
                return X


            def API_SET_LEGACY_DIR(X, L, DIR):
                return X # DIR


            def API_SET_LEGACY_PRIVATE(X, L):
                return X # PRIVATE


            def API_SET_LEGACY_PRIVATE_DIR(X, L, DIR):
                return X # DIR PRIVATE


            def API_SET_LEGACY_BY_ORDINAL(X, L, O, PO):
                return X # @##O NONAME


            def API_SET_LEGACY_BY_ORDINAL_DIR(X, L, O, PO, DIR):
                return X # @##O NONAME DIR


            def API_SET_LEGACY_BY_ORDINAL_PRIVATE(X, L, O, PO):
                return X # @##O NONAME PRIVATE


            def API_SET_LEGACY_BY_ORDINAL_PRIVATE_DIR(X, L, O, PO, DIR):
                return X # @##O NONAME DIR PRIVATE
        else:
            def API_SET(X):
                return _API_SET_LEGACY_TARGET##.##X


            def API_SET_DIR(X, DIR):
                return _API_SET_LEGACY_TARGET##.##X DIR


            def API_SET_PRIVATE(X):
                return _API_SET_LEGACY_TARGET##.##X PRIVATE


            def API_SET_PRIVATE_DIR(X, DIR):
                return _API_SET_LEGACY_TARGET##.##X DIR PRIVATE


            def API_SET_BY_ORDINAL(X, O, PO):
                return  _API_SET_LEGACY_TARGET##.##PO @##O NONAME


            def API_SET_BY_ORDINAL_DIR(X, O, PO, DIR):
                return _API_SET_LEGACY_TARGET##.##PO @##O NONAME DIR


            def API_SET_BY_ORDINAL_PRIVATE(X, O, PO):
                return _API_SET_LEGACY_TARGET##.##PO @##O NONAME PRIVATE


            def API_SET_BY_ORDINAL_PRIVATE_DIR(X, O, PO, DIR):
                return  _API_SET_LEGACY_TARGET##.##PO @##O NONAME DIR PRIVATE


            def API_SET_LEGACY(X, L):
                return  L##.##X


            def API_SET_LEGACY_DIR(X, L, DIR):
                return L##.##X DIR


            def API_SET_LEGACY_PRIVATE(X, L):
                return L##.##X PRIVATE


            def API_SET_LEGACY_PRIVATE_DIR(X, L, DIR):
                return L##.##X DIR PRIVATE


            def API_SET_LEGACY_BY_ORDINAL(X, L, O, PO):
                return L##.##PO @##O NONAME


            def API_SET_LEGACY_BY_ORDINAL_DIR(X, L, O, PO, DIR):
                return L##.##PO @##O NONAME DIR


            def API_SET_LEGACY_BY_ORDINAL_PRIVATE(X, L, O, PO):
                return L##.##PO @##O NONAME PRIVATE


            def API_SET_LEGACY_BY_ORDINAL_PRIVATE_DIR(X, L, O, PO, DIR):
                return L##.##PO @##O NONAME DIR PRIVATE
        # END IF   _API_SET_LEGACY_TARGET

        def API_SET_LIBRARY(X):
            return X
    # END IF   _API_SET_HOST
# END IF   _API_SET_H_
