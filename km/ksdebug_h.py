from pyWinAPI import *

# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: ksdebug.h Abstract: Debug header. - -

from pyWinAPI.shared.evntrace_h import * # NOQA
_KSDEBUG_ = None

KSDEBUG_INIT = None
DEBUG_VARIABLE = None
DEBUG_LEVEL = None

if not defined(_KSDEBUG_):
    _KSDEBUG_ = 1

    REMIND = None
    if not defined(REMIND):
        def QUOTE(x):
            return '"' + x + '"'


        def QQUOTE(y):
            return QUOTE(y)


        def REMIND(str):
            return "(" + QQUOTE(str) + ")"

    # END IF   not defined(REMIND)
    if defined(__cplusplus):
        pass
    # END IF   defined(__cplusplus)

    if defined(_NTDDK_):
        DEBUGLVL_BLAB = TRACE_LEVEL_VERBOSE
        DEBUGLVL_VERBOSE = TRACE_LEVEL_VERBOSE
        DEBUGLVL_TERSE = TRACE_LEVEL_INFORMATION
        DEBUGLVL_ERROR = TRACE_LEVEL_ERROR
        DEBUGLVL_WARNING = TRACE_LEVEL_WARNING
        DEBUGLVL_INFO = TRACE_LEVEL_INFORMATION

        if DBG:
            if not defined(DEBUG_LEVEL):
                if defined(DEBUG_VARIABLE):
                    if defined(KSDEBUG_INIT):
                        DEBUG_VARIABLE = DEBUGLVL_TERSE
                    else:
                        DEBUG_VARIABLE = DEBUGLVL_TERSE
                    # END IF
                else:
                    DEBUG_VARIABLE = DEBUGLVL_TERSE
                # END IF
            else:
                if defined( DEBUG_VARIABLE ):
                    if defined(KSDEBUG_INIT):
                        DEBUG_VARIABLE = DEBUG_LEVEL
                    else:
                        DEBUG_VARIABLE = ULONG
                    # END IF
                else:
                    DEBUG_VARIABLE = DEBUG_LEVEL
                # END IF
            # END IF

            def _DbgPrintF(lvl, strings):
                if lvl == DEBUG_VARIABLE or lvl < DEBUG_VARIABLE:
                    DbgPrint(STR_MODULENAME)
                    DbgPrint(strings)
                    DbgPrint("\n")
                    if lvl == DEBUGLVL_ERROR:
                        DbgBreakPoint()


            if NTDDI_VERSION >= NTDDI_WINXP:
                def _DbgPrintFEx(component, lvl, strings):
                    if lvl <= DEBUG_VARIABLE:
                        DbgPrintEx(component, lvl, STR_MODULENAME)
                        DbgPrintEx(component, lvl, strings)
                        DbgPrintEx(component, lvl, "\n")
                        if lvl == DEBUGLVL_ERROR:
                            DbgBreakPoint()

            # END IF
        else:
            def _DbgPrintF(lvl, strings):
                pass


            if NTDDI_VERSION >= NTDDI_WINXP:
                def _DbgPrintFEx(component, lvl, strings):
                    pass
            # END IF
        # END IF   not DBG
    # END IF   not defined(_NTDDK_)

    # macros
    if defined(__cplusplus):
        pass
    # END IF   defined(__cplusplus)

    # constants

    if DBG:
        IRPMJFUNCDESC = None
        if defined(IRPMJFUNCDESC):
            IrpMjFuncDesc = [
                "IRP_MJ_CREATE",
                "IRP_MJ_CREATE_NAMED_PIPE",
                "IRP_MJ_CLOSE",
                "IRP_MJ_READ",
                "IRP_MJ_WRITE",
                "IRP_MJ_QUERY_INFORMATION",
                "IRP_MJ_SET_INFORMATION",
                "IRP_MJ_QUERY_EA",
                "IRP_MJ_SET_EA",
                "IRP_MJ_FLUSH_BUFFERS",
                "IRP_MJ_QUERY_VOLUME_INFORMATION",
                "IRP_MJ_SET_VOLUME_INFORMATION",
                "IRP_MJ_DIRECTORY_CONTROL",
                "IRP_MJ_FILE_SYSTEM_CONTROL",
                "IRP_MJ_DEVICE_CONTROL",
                "IRP_MJ_INTERNAL_DEVICE_CONTROL",
                "IRP_MJ_SHUTDOWN",
                "IRP_MJ_LOCK_CONTROL",
                "IRP_MJ_CLEANUP",
                "IRP_MJ_CREATE_MAILSLOT",
                "IRP_MJ_QUERY_SECURITY",
                "IRP_MJ_SET_SECURITY",
                "IRP_MJ_SET_POWER",
                "IRP_MJ_QUERY_POWER"
            ]
        # END IF   defined(IRPMJFUNCDESC)
    # END IF   DBG
# END IF   not _KSDEBUG_
