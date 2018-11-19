import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _DEBUG_TRACE_CONTROLPOINT(ctypes.Structure):
    pass


DEBUG_TRACE_CONTROLPOINT = _DEBUG_TRACE_CONTROLPOINT
PDEBUG_TRACE_CONTROLPOINT = POINTER(_DEBUG_TRACE_CONTROLPOINT)


class RX_DEBUG_TRACE_CONTROL(ctypes.Structure):
    pass


PRX_DEBUG_TRACE_CONTROL = POINTER(RX_DEBUG_TRACE_CONTROL)


class rxrxrx_AlwaysHelper(ctypes.Structure):
    pass

# /* + + Copyright (c) 1989 Microsoft Corporation Module Name: rxtrace.h
# Abstract: This module defines the macros which provide debugging support
# ( tracing ). Author: Revision History: - -

_RDBSSTRACE_INCLUDED_ = None
if not defined(_RDBSSTRACE_INCLUDED_):
    _RDBSSTRACE_INCLUDED_ = 1
    if not DBG:
        pass
    # END IF   not DBG

    _DEBUG_TRACE_CONTROLPOINT._fields_ = [
        ('ControlPointNumber', ULONG),
        ('Name', PSZ),
    ]

    RX_DEBUG_TRACE_CONTROL._fields_ = [
        ('PrintLevel', LONG),
        ('BreakMask', ULONG),
        ('Name', PSZ),
    ]

    RDBSSTRACE = None

    if defined(RDBSSTRACE):
        # define so that & RX_DEBUG_TRACE_CONTROL is NULL
        rxrxrx_AlwaysHelper._fields_ = [
            ('Junk', RX_DEBUG_TRACE_CONTROL),
        ]
        RX_DEBUG_TRACE_ALWAYS = RX_DEBUG_TRACE_CONTROL

        # The following macros provide fine grained control for selectively
        # enabling
        # and disabling tracing.
        def RXDT_Extern():
            return DEBUG_TRACE_CONTROLPOINT


        def RXDT_DeclareCategory():
            return DEBUG_TRACE_CONTROLPOINT


        def RXDT_DefineCategory():
            return DEBUG_TRACE_CONTROLPOINT


        RX_DEBUG_TRACE_ERROR = RXDT_Extern()
        RX_DEBUG_TRACE_HOOKS = RXDT_Extern()
        RX_DEBUG_TRACE_CATCH_EXCEPTIONS = RXDT_Extern()
        RX_DEBUG_TRACE_UNWIND = RXDT_Extern()
        RX_DEBUG_TRACE_CLEANUP = RXDT_Extern()
        RX_DEBUG_TRACE_CLOSE = RXDT_Extern()
        RX_DEBUG_TRACE_CREATE = RXDT_Extern()
        RX_DEBUG_TRACE_DIRCTRL = RXDT_Extern()
        RX_DEBUG_TRACE_EA = RXDT_Extern()
        RX_DEBUG_TRACE_FILEINFO = RXDT_Extern()
        RX_DEBUG_TRACE_FSCTRL = RXDT_Extern()
        RX_DEBUG_TRACE_LOCKCTRL = RXDT_Extern()
        RX_DEBUG_TRACE_READ = RXDT_Extern()
        RX_DEBUG_TRACE_VOLINFO = RXDT_Extern()
        RX_DEBUG_TRACE_WRITE = RXDT_Extern()
        RX_DEBUG_TRACE_FLUSH = RXDT_Extern()
        RX_DEBUG_TRACE_DEVCTRL = RXDT_Extern()
        RX_DEBUG_TRACE_SHUTDOWN = RXDT_Extern()
        RX_DEBUG_TRACE_PREFIX = RXDT_Extern()
        RX_DEBUG_TRACE_DEVFCB = RXDT_Extern()
        RX_DEBUG_TRACE_ACCHKSUP = RXDT_Extern()
        RX_DEBUG_TRACE_ALLOCSUP = RXDT_Extern()
        RX_DEBUG_TRACE_DIRSUP = RXDT_Extern()
        RX_DEBUG_TRACE_FILOBSUP = RXDT_Extern()
        RX_DEBUG_TRACE_NAMESUP = RXDT_Extern()
        RX_DEBUG_TRACE_VERFYSUP = RXDT_Extern()
        RX_DEBUG_TRACE_CACHESUP = RXDT_Extern()
        RX_DEBUG_TRACE_SPLAYSUP = RXDT_Extern()
        RX_DEBUG_TRACE_DEVIOSUP = RXDT_Extern()
        RX_DEBUG_TRACE_FCBSTRUCTS = RXDT_Extern()
        RX_DEBUG_TRACE_STRUCSUP = RXDT_Extern()
        RX_DEBUG_TRACE_FSP_DISPATCHER = RXDT_Extern()
        RX_DEBUG_TRACE_FSP_DUMP = RXDT_Extern()
        RX_DEBUG_TRACE_RXCONTX = RXDT_Extern()
        RX_DEBUG_TRACE_DISPATCH = RXDT_Extern()
        RX_DEBUG_TRACE_NTFASTIO = RXDT_Extern()
        RX_DEBUG_TRACE_LOWIO = RXDT_Extern()
        RX_DEBUG_TRACE_MINIRDR = RXDT_Extern()
        RX_DEBUG_TRACE_DISCCODE = RXDT_Extern()
        RX_DEBUG_TRACE_BROWSER = RXDT_Extern()
        RX_DEBUG_TRACE_CONNECT = RXDT_Extern()
        RX_DEBUG_TRACE_NTTIMER = RXDT_Extern()
        RX_DEBUG_TRACE_SCAVTHRD = RXDT_Extern()
        RX_DEBUG_TRACE_SCAVENGER = RXDT_Extern()
        RX_DEBUG_TRACE_SHAREACCESS = RXDT_Extern()
        RX_DEBUG_TRACE_NAMECACHE = RXDT_Extern()
        RX_DEBUG_TRACE_RXCEBINDING = RXDT_Extern()
        RX_DEBUG_TRACE_RXCEDBIMPLEMENTATION = RXDT_Extern()
        RX_DEBUG_TRACE_RXCEMANAGEMENT = RXDT_Extern()
        RX_DEBUG_TRACE_RXCEXMIT = RXDT_Extern()
        RX_DEBUG_TRACE_RXCEPOOL = RXDT_Extern()
        RX_DEBUG_TRACE_RXCETDI = RXDT_Extern()


        # for the browser interface stuff
        # connection engines categories
    else:
        def RXDT_Extern():
            pass

        def RXDT_DeclareCategory():
            pass

        def RXDT_DefineCategory():
            pass

    # END IF RDBSSTRACE

    if defined(RDBSSTRACE):

        RxGlobalTraceSuppress = BOOLEAN
        RxNextGlobalTraceSuppress = BOOLEAN
        RxGlobalTraceIrpCount = ULONG

        def RxDbgTraceDoit(___x):
            return ___x


        MINIRDR__NAME = None

        if not defined(MINIRDR__NAME):
            RxDebugTraceIndent = LONG
        else:
            # RxDebugTraceIndent = ___MINIRDR_IMPORTS_NAME.pRxDebugTraceIndent
            pass

        # END IF
    else:
        def RxInitializeDebugTrace():
            pass

        def RxDbgTraceDoit(___x):
            pass

    # END IF  RDBSSTRACE

    if DBG:
        RxDT_INDENT_EXCESS = 16        # this is the offset for excess - n for the indent
        RxDT_INDENT_SHIFT = 20
        RxDT_INDENT_MASK = 0x3F
        RxDT_LEVEL_MASK = (1 << RxDT_INDENT_SHIFT) - 1
        RxDT_SUPPRESS_PRINT = 0x80000000
        RxDT_OVERRIDE_RETURN = 0x40000000

        # TODO: Find location of functions below
        # VOID
        # RxDebugTraceActual (
        # _In_ ULONG NewMask,
        # _In_ PSZ Format,
        # ...
        # );
        #
        # BOOLEAN
        # RxDbgTraceActualNew (
        # IN ULONG NewMask,
        # IN OUT PDEBUG_TRACE_CONTROLPOINT ControlPoint
        # );
        #
        # PRX_DEBUG_TRACE_CONTROL
        # RxDbgTraceFindControlPointActual(
        # IN OUT PDEBUG_TRACE_CONTROLPOINT ControlPoint
        # );
        #
        # VOID
        # RxInitializeDebugTraceControlPoint(
        # _In_ PSZ Name,
        # PDEBUG_TRACE_CONTROLPOINT ControlPoint
        # );

        # The implementation details of the tracing feature.
        RxIrpCodeToName = PCHAR * 0

    # END IF  DBG

    if defined(RDBSSTRACE):
        def RxDTMASK(INDENT, WRITELEVEL):
            return ((INDENT + RxDT_INDENT_EXCESS) << RxDT_INDENT_SHIFT) + (WRITELEVEL & RxDT_LEVEL_MASK)


        def RxDTPrefixRx(___x):
            return 'RX_' + ___x


        def RxDbgTraceLV__norx_reverseaction(INDENT, CONTROLPOINT, LEVEL, Z):
            # return {BOOLEAN PrintIt = RxDbgTraceActualNew((RxDT_SUPPRESS_PRINT | RxDT_OVERRIDE_RETURN | RxDTMASK(INDENT,LEVEL)), CONTROLPOINT); if not PrintIt Z; }
            pass


        def RxDbgTraceLV__norx(INDENT, CONTROLPOINT, LEVEL, Z):
            # return {BOOLEAN PrintIt = RxDbgTraceActualNew( RxDTMASKINDENT,LEVEL,CONTROLPOINT); if PrintIt DbgPrint Z; }
            pass


        def RxDbgTraceLVUnIndent__norx(INDENT, CONTROLPOINT, LEVEL):
            # return {BOOLEAN PrintIt = RxDbgTraceActualNew((RxDT_SUPPRESS_PRINT | RxDTMASK(INDENT,LEVEL)),CONTROLPOINT); }
            pass


        def RxDbgTraceLV__(INDENT, CONTROLPOINT, LEVEL, Z):
            return RxDbgTraceLV__norx(
                INDENT,
                ctypes.byref(globals()['RxDTPrefixRx' + CONTROLPOINT]),
                LEVEL,
                Z
            )


        def RxDbgTraceLVUnIndent__(INDENT, CONTROLPOINT, LEVEL):
            return RxDbgTraceLVUnIndent__norx(
                INDENT,
                ctypes.byref(globals()['RxDTPrefixRx' + CONTROLPOINT]),
                LEVEL
            )


        def RxDbgTrace(INDENT, CONTROLPOINT, Z):
            return RxDbgTraceLV__(INDENT, CONTROLPOINT, 1, Z)


        def RxDbgTraceLV(INDENT, CONTROLPOINT, LEVEL, Z):
            return RxDbgTraceLV__(INDENT, CONTROLPOINT, LEVEL, Z)


        def RxDbgTraceUnIndent(INDENT, CONTROLPOINT):
            return RxDbgTraceLVUnIndent__(INDENT, CONTROLPOINT, 1)

        # do not define this for nonrdbsstrace; so to catch references not
        # ifdef'd

        def RxDbgTraceFindControlPoint(CONTROLPOINT):
            return RxDbgTraceFindControlPointActual(
                ctypes.byref(globals()['RxDTPrefixRx' + CONTROLPOINT])
            )


        def DebugBreakPoint(CONTROLPOINT, MASKBIT):
            if MASKBIT == 0 or RxDbgTraceFindControlPoint(CONTROLPOINT).BreakMask & (1 << (MASKBIT - 1)):
                return DbgBreakPoint


        def DebugUnwind(X):
            if AbnormalTermination:
                RxDbgTrace(0, DEBUG_TRACE_UNWIND,  X + ", Abnormal termination.\n")

        if defined(RX_PERFPORMANCE_TIMER):

            def TimerStart(LEVEL):
                # return {
                # LARGE_INTEGER TStart, TEnd;
                # LARGE_INTEGER TElapsed;
                # TStart = KeQueryPerformanceCounter NULL ;
                pass

            def TimerStop(LEVEL, s):
                # return
                # TEnd = KeQueryPerformanceCounter NULL ;
                # TElapsed.QuadPart = TEnd.QuadPart - TStart.QuadPart;
                # RxTotalTicks[RxLogOfLEVEL] + = TElapsed.LowPart;
                # if (FlagOn( RxPerformanceTimerLevel, LEVEL)) {
                # DbgPrint("Time of %s %ld\n", s, TElapsed.LowPart );
                # } }
                pass
        # END IF  RX_PERFPORMANCE_TIMER

    else:
        def RxDbgTraceLV__norx_reverseaction(INDENT, CONTROLPOINT, LEVEL, Z):
            pass

        def RxDbgTraceLV(INDENT, CONTROLPOINTNUM, LEVEL, Z):
            pass


        def RxDbgTraceLVUnIndent(INDENT, CONTROLPOINTNUM, LEVEL):
            pass


        def RxDbgTrace(INDENT, CONTROLPOINTNUM, Z):
            pass


        def RxDbgTraceUnIndent(INDENT, CONTROLPOINTNUM):
            pass


        def DebugBreakPoint(CONTROLPOINTNUM, MASKBIT):
            pass


        def DebugUnwind(X):
            pass


        def RxDbgTraceDisableGlobally():
            pass


        def RxDbgTraceEnableGlobally(f):
            pass


        RX_PERFPORMANCE_TIMER = None
        if defined(RX_PERFPORMANCE_TIMER):
            def TimerStart(LEVEL):
                pass

            def TimerStop(LEVEL,s):
                pass
        # END IF
    # END IF   RDBSSTRACE
# END IF   _RDBSSTRACE_INCLUDED_
