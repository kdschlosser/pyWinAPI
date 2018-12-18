import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *




# ***************************************************************************\
# * KernelSpecs.h - markers for documenting the semantics of driver APIs * See
# DriverSpecs.h for detailed comments * See also <SpecStrings.h> * * Version
# 1.2.00 * * Copyright (c) Microsoft Corporation. All rights reserved. * *
# \***************************************************************************
# ***************************************************************************\
# NOTE  * NOTE  * NOTE  * The macro bodies in this file are subject to change
# without notice. * Attempting to use the annotations in the macro bodies
# directly is not * supported. * NOTE * NOTE * NOTE *
# \***************************************************************************
# ***************************************************************************\
# As noted in DriverSpecs.h, this header contains "real" definitions for
# annotations that either never appear in user space, or which are meaningles
# in user space and are defined to nothing by DriverSpecs.h. Further
# commentary appears in DriverSpecs.h.
# \***************************************************************************
if not defined(KERNELSPECS_H):
    #~#~#~    #define KERNELSPECS_H
    from DriverSpecs_h import * # NOQA
    if _MSC_VER > 1000:
        pass
    # END IF   ]
    if defined(__cplusplus):
        pass
    # END IF   ]
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # The symbolic IRQL values can sometimes end up undefined, so define
    # the usual ones here, for PREfast purposes only.
    DISPATCH_LEVEL = 2
    APC_LEVEL = 1
    PASSIVE_LEVEL = 0
    if defined(_X86_):
        HIGH_LEVEL = 31
    # END IF
    if defined(_AMD64_):
        HIGH_LEVEL = 15
    # END IF
    if defined(_ARM_):
        HIGH_LEVEL = 15
    # END IF
    if defined(_IA64_):
        HIGH_LEVEL = 15
    # END IF
    if defined(_ARM64_):
        HIGH_LEVEL = 15
    # END IF
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # IRQL annotations:
    # _IRQL_raises_(irql)
    # _IRQL_requires_(irql)
    # _IRQL_requires_max_(irql)
    # _IRQL_requires_min_(irql)
    # _IRQL_saves_
    # _IRQL_saves_global_(kind,param)
    # _IRQL_restores_
    # _IRQL_restores_global_(kind,param)
    # _IRQL_always_function_min_(irql)
    # _IRQL_always_function_max_(irql)
    # _IRQL_requires_same_
    # _IRQL_uses_cancel_
    # Legacy IRQL annotations:
    # Legacy annotation:  Use instead:
    # __drv_setsIRQL  (Obsolete, use _IRQL_raises_)
    # __drv_raisesIRQL  _IRQL_raises_
    # __drv_requiresIRQL  _IRQL_requires_
    # __drv_maxIRQL   _IRQL_requires_max_
    # __drv_minIRQL   _IRQL_requires_min_
    # __drv_savesIRQL   _IRQL_saves_
    # __drv_savesIRQLGlobal  _IRQL_saves_global_
    # __drv_restoresIRQL  _IRQL_restores_
    # __drv_restoresIRQLGlobal _IRQL_restores_global_
    # __drv_minFunctionIRQL  _IRQL_always_function_min_
    # __drv_maxFunctionIRQL  _IRQL_always_function_max_
    # __drv_sameIRQL  _IRQL_requires_same_
    # __drv_useCancelIRQL  _IRQL_uses_cancel_
    # The function exits at IRQL irql (obsolete, use _IRQL_raises_)
    # ';' inside the parens to keep MIDL happy
    def __drv_setsIRQL(irql):
        return _SAL1_Source_(__drv_setsIRQL, , _Post_ _SA_annotes1SAL_IRQL,irql)    # legacy


    # The function exits at IRQL irql, but this may only raise the irql.
    def _IRQL_raises_(irql):
        return _SAL2_Source_(_IRQL_raises_, , _Post_ _SA_annotes1SAL_raiseIRQL,irql)
    

    def __drv_raisesIRQL(irql):
        return _SAL1_Source_(__drv_raisesIRQL, , _IRQL_raises_irql)    # legacy


    # The called function must be entered at IRQL level
    def _IRQL_requires_(irql):
        return _SAL2_Source_(_IRQL_requires_, irql, _Pre_ _SA_annotes1SAL_IRQL,irql)
    

    def __drv_requiresIRQL(irql):
        return _SAL1_Source_(__drv_requiresIRQL, , _IRQL_requires_irql)    # legacy


    # The maximum IRQL at which the function may be called.
    def _IRQL_requires_max_(irql):
        return _SAL2_Source_(_IRQL_requires_max_, irql, _Pre_ _SA_annotes1SAL_maxIRQL,irql)
    

    def __drv_maxIRQL(irql):
        return _SAL1_Source_(__drv_maxIRQL, , _IRQL_requires_max_irql)    # legacy


    # The minimum IRQL at which the function may be called.
    def _IRQL_requires_min_(irql):
        return _SAL2_Source_(_IRQL_requires_min_, irql, _Pre_ _SA_annotes1SAL_minIRQL,irql)
    

    def __drv_minIRQL(irql):
        return _SAL1_Source_(__drv_minIRQL, , _IRQL_requires_min_irql)    # legacy


    # The current IRQL is saved in the annotated parameter
    _IRQL_saves_ =         _SAL2_Source_(_IRQL_saves_,
(
        ),
         _Post_ _SA_annotes0(SAL_saveIRQL)
    )
    __drv_savesIRQL = _SAL1_Source_(__drv_savesIRQL, (), _IRQL_saves_)    # legacy


    # The current IRQL is saved in the (otherwise anonymous) global object
    # identified by kind and further refined by param.
    def _IRQL_saves_global_(kind, param):
        return _SAL2_Source_(_IRQL_saves_global_, kind, param, _Post_ _SA_annotes2SAL_saveIRQLGlobal,#kind, param\t)
    

    def __drv_savesIRQLGlobal(kind, param):
        return _SAL1_Source_(__drv_savesIRQLGlobal, , _IRQL_saves_global_kind, param)    # legacy


    # The current IRQL is restored from the annotated parameter
    _IRQL_restores_ =         _SAL2_Source_(_IRQL_restores_,
(
        ),
         _Post_ _SA_annotes0(SAL_restoreIRQL)
    )
    __drv_restoresIRQL =         _SAL1_Source_(__drv_restoresIRQL,
(
        ),
         _IRQL_restores_
    )    # legacy


    # The current IRQL is restored from the (otherwise anonymous) global
    # object identified by kind and further refined by param.
    def _IRQL_restores_global_(kind, param):
        return _SAL2_Source_(_IRQL_restores_global_, kind, param, _Post_ _SA_annotes2SAL_restoreIRQLGlobal, #kind, param\t)
    

    def __drv_restoresIRQLGlobal(kind, param):
        return _SAL1_Source_(__drv_restoresIRQLGlobal, , _IRQL_restores_global_kind, param)    # legacy


    # The minimum IRQL to which the function can lower itself. The IRQL
    # at entry is assumed to be that value unless overridden.
    def _IRQL_always_function_min_(irql):
        return _SAL2_Source_(_IRQL_always_function_min_, irql, _Pre_ _SA_annotes1SAL_minFunctionIrql,irql)
    

    def __drv_minFunctionIRQL(irql):
        return _SAL1_Source_(__drv_minFunctionIRQL, , _IRQL_always_function_min_irql)    # legacy


    # The maximum IRQL to which the function can raise itself.
    def _IRQL_always_function_max_(irql):
        return _SAL2_Source_(_IRQL_always_function_max_, irql, _Pre_ _SA_annotes1SAL_maxFunctionIrql,irql)
    

    def __drv_maxFunctionIRQL(irql):
        return _SAL1_Source_(__drv_maxFunctionIRQL, , _IRQL_always_function_max_irql)    # legacy


    # The function must exit with the same IRQL it was entered with.
    # (It may change it but it must restore it.)
    _IRQL_requires_same_ =         _SAL2_Source_(_IRQL_requires_same_,
(
        ),
         _Post_ _SA_annotes0(SAL_sameIRQL)
    )
    __drv_sameIRQL = _SAL1_Source_(__drv_sameIRQL, (), _IRQL_requires_same_)    # legacy


    # The annotated parameter contains the cancelIRQL, which will be restored
    # by the called function.
    _IRQL_uses_cancel_ =         _SAL2_Source_(_IRQL_uses_cancel_,
(
        ),
         _Post_ _SA_annotes0(SAL_UseCancelIrql)
    )
    __drv_useCancelIRQL =         _SAL1_Source_(__drv_useCancelIRQL,
(
        ),
         _IRQL_uses_cancel_
    )    # legacy


    # The annotated parameter is an IRQL that will be restored and a new
    # (probably the same)
    # value will be inserted. (Use this in preference to directly coding it.)
    _IRQL_inout_ = _IRQL_saves_ _IRQL_restores_
    if defined(_PREFAST_):
        # Passing the cancel Irql to a utility function
        _IRQL_is_cancel_ =             _SAL2_Source_(_IRQL_is_cancel_,
(
            ),
            _IRQL_uses_cancel_ _Releases_nonreentrant_lock_(_Global_cancel_spin_lock_) _At_(return,
             _IRQL_always_function_min_(DISPATCH_LEVEL) _IRQL_requires_(DISPATCH_LEVEL)
        )
        __drv_isCancelIRQL =             _SAL1_Source_(__drv_isCancelIRQL,
(
            ),
             _IRQL_is_cancel_
        )        # legacy
    # END IF
    if defined(__cplusplus):
        pass
    # END IF
# END IF   KERNELSPECS_H
