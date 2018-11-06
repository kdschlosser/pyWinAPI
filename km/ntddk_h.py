import comtypes


from pyWinAPI import *



# + + BUILD Version: 0184 // Increment this if a change has global effects
# Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# ntddk.h Abstract: This module defines the NT types, constants, and functions
# that are exposed to device drivers. Revision History: - -
if not defined(_NTDDK_):
    _NTDDK_ = 1

    if not defined(_NTHAL_) and not defined(_NTIFS_):
        _NTDDK_INCLUDED_ = 1
        _DDK_DRIVER_ = 1
    # END IF

        if _MSC_VER < 1300:
            pass
        # END IF
    if not defined(RC_INVOKED):
        pass
    # END IF   RC_INVOKED
    NT_INCLUDED = 1
    _CTYPE_DISABLE_MACROS = 1

    if _MSC_VER >= 1200:
        pass
    # END IF
    if defined(__cplusplus):
        pass
    # END IF
    PBUS_HANDLER = POINTER(_BUS_HANDLER)


    PCALLBACK_OBJECT = POINTER(_CALLBACK_OBJECT)


    PDEVICE_HANDLER_OBJECT = POINTER(_DEVICE_HANDLER_OBJECT)


    if defined(_NTHAL_INCLUDED_):
        PEPROCESS = POINTER(_KPROCESS)


        PETHREAD = POINTER(_ETHREAD)


        PKAFFINITY_EX = POINTER(_KAFFINITY_EX)


elif defined(_NTIFS_INCLUDED_):
        PEPROCESS = POINTER(_KPROCESS)


        PETHREAD = POINTER(_KTHREAD)


else:
        PEPROCESS = POINTER(_EPROCESS)


        PETHREAD = POINTER(_ETHREAD)


    # END IF
    PEJOB = POINTER(_EJOB)


    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        PESILO = POINTER(_EJOB)


        PSILO_MONITOR = POINTER(_SILO_MONITOR)


    # END IF
    PIO_TIMER = POINTER(_IO_TIMER)


    PKINTERRUPT = POINTER(_KINTERRUPT)


    PRKTHREAD = POINTER(*PKTHREAD,)


    POBJECT_TYPE = POINTER(_OBJECT_TYPE)


    PPEB = POINTER(_PEB)


    PIMAGE_NT_HEADERS32 = POINTER(_IMAGE_NT_HEADERS)


    PIMAGE_NT_HEADERS64 = POINTER(_IMAGE_NT_HEADERS64)


    if defined(_WIN64):
        pass
else:
        pass
    # END IF
    PsGetCurrentProcess = IoGetCurrentProcess

        if defined(_X86_) or defined(_AMD64_):
            pass
    else:
            pass
        # END IF
    if (NTDDI_VERSION >= NTDDI_VISTA):
        pass
elif (NTDDI_VERSION >= NTDDI_WINXP):
        pass
else:
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        pass
    # END IF
    if not defined(FAR):
        FAR = 1
    # END IF

    if defined(_X86_):
        if defined(_M_CEE_PURE):
            CDECL_NON_WVMPURE = 1
    else:
            CDECL_NON_WVMPURE = __cdecl
        # END IF

                if _MSC_VER >= 1200:
                    pass
                # END IF   _MSC_VER >= 1200
                if _MSC_VER >= 1200:
                    pass
            else:
                    pass
                # END IF   _MSC_VER >= 1200
            if not defined(RC_INVOKED):
                pass
            # END IF   not defined(MIDL_PASS)
        if not defined(MIDL_PASS):
            pass
        # END IF   not defined(RC_INVOKED)
        KERNEL_STACK_SIZE = 12288
        KERNEL_LARGE_STACK_SIZE = 61440
        KERNEL_LARGE_STACK_COMMIT = 12288

                if not defined(_M_CEE_PURE) and not defined(_M_HYBRID_X86_ARM64):
                    pass
                # END IF  not _M_CEE_PURE or not _M_HYBRID_X86_ARM64
        if defined(_X86_):
            if not defined(MIDL_PASS) and defined(_M_IX86):
                if not defined(_M_HYBRID_X86_ARM64):
                    _MM_HINT_T0 = 1
                    _MM_HINT_T1 = 2
                    _MM_HINT_T2 = 3
                    _MM_HINT_NTA = 0
                    PF_TEMPORAL_LEVEL_1 = _MM_HINT_T0
                    PF_TEMPORAL_LEVEL_2 = _MM_HINT_T1
                    PF_TEMPORAL_LEVEL_3 = _MM_HINT_T2
                    # PF_NON_TEMPORAL_LEVEL_ALL = _MM_HINT_NTA


def PreFetchCacheLine(l, a):
    return _mm_prefetch(CHAR CONST * a, l)


def PrefetchForWrite(p):
    return 1


def ReadForWriteAccess(p):
    return (*p)

                    if not defined(_MANAGED):
                        ReadPMC = __readpmc


def ReadTimeStampCounter():
    return __rdtsc
                    # END IF   not defined(_MANAGED)
                # END IF   not defined(_M_HYBRID_X86_ARM64)
            # END IF   not defined(MIDL_PASS) and defined(_M_IX86)
            SIZE_OF_80387_REGISTERS = 80

            if not defined(RC_INVOKED):
                CONTEXT_i386 = 0x00010000
                CONTEXT_i486 = 0x00010000
                CONTEXT_CONTROL = CONTEXT_i386 | 0x00000001
                CONTEXT_INTEGER = CONTEXT_i386 | 0x00000002
                CONTEXT_SEGMENTS = CONTEXT_i386 | 0x00000004
                CONTEXT_FLOATING_POINT = CONTEXT_i386 | 0x00000008
                CONTEXT_DEBUG_REGISTERS = CONTEXT_i386 | 0x00000010
                CONTEXT_EXTENDED_REGISTERS = CONTEXT_i386 | 0x00000020
                CONTEXT_FULL = CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_SEGMENTS
                CONTEXT_ALL = (
    CONTEXT_CONTROL  |
     CONTEXT_INTEGER  |
     CONTEXT_SEGMENTS  |
     CONTEXT_FLOATING_POINT  |
     CONTEXT_DEBUG_REGISTERS  |
     CONTEXT_EXTENDED_REGISTERS
)
                CONTEXT_XSTATE = CONTEXT_i386 | 0x00000040
                CONTEXT_EXCEPTION_ACTIVE = 0x08000000
                CONTEXT_SERVICE_ACTIVE = 0x10000000
                CONTEXT_EXCEPTION_REQUEST = 0x40000000
                CONTEXT_EXCEPTION_REPORTING = 0x80000000
            # END IF   not defined(RC_INVOKED)
            class _FLOATING_SAVE_AREA(ctypes.Structure):
                pass
            _FLOATING_SAVE_AREA._fields_ = [
                ('ControlWord', ULONG),
                ('StatusWord', ULONG),
                ('TagWord', ULONG),
                ('ErrorOffset', ULONG),
                ('ErrorSelector', ULONG),
                ('DataOffset', ULONG),
                ('DataSelector', ULONG),
                ('RegisterArea', UCHAR * SIZE_OF_80387_REGISTERS),
                ('Spare0', ULONG),
            ]


            FLOATING_SAVE_AREA = _FLOATING_SAVE_AREA


            class _CONTEXT(ctypes.Structure):
                pass
            _CONTEXT._fields_ = [
                ('ContextFlags', ULONG), # The context record is never used as an OUT only parameter.
                ('Dr0', ULONG), # included in CONTEXT_FULL.
                ('Dr1', ULONG),
                ('Dr2', ULONG),
                ('Dr3', ULONG),
                ('Dr6', ULONG),
                ('Dr7', ULONG),
                ('FloatSave', FLOATING_SAVE_AREA), # ContextFlags word contians the flag CONTEXT_FLOATING_POINT.
                ('SegGs', ULONG), # ContextFlags word contians the flag CONTEXT_SEGMENTS.
                ('SegFs', ULONG),
                ('SegEs', ULONG),
                ('SegDs', ULONG),
                ('Edi', ULONG), # ContextFlags word contians the flag CONTEXT_INTEGER.
                ('Esi', ULONG),
                ('Ebx', ULONG),
                ('Edx', ULONG),
                ('Ecx', ULONG),
                ('Eax', ULONG),
                ('Ebp', ULONG), # ContextFlags word contians the flag CONTEXT_CONTROL.
                ('Eip', ULONG),
                ('SegCs', ULONG), # MUST BE SANITIZED
                ('EFlags', ULONG), # MUST BE SANITIZED
                ('Esp', ULONG),
                ('SegSs', ULONG),
                ('ExtendedRegisters', UCHAR * MAXIMUM_SUPPORTED_EXTENSION), # The format and contexts are processor specific
            ]


            CONTEXT = _CONTEXT


        # END IF  _X86_
    # END IF   _X86_

    if defined(_AMD64_):
        KERNEL_STACK_SIZE = 0x6000
        KERNEL_LARGE_STACK_SIZE = 0x12000
        KERNEL_LARGE_STACK_COMMIT = KERNEL_STACK_SIZE
        KERNEL_MCA_EXCEPTION_STACK_SIZE = 0x2000
        EXCEPTION_READ_FAULT = 0
        EXCEPTION_WRITE_FAULT = 1
        EXCEPTION_EXECUTE_FAULT = 8

        if not defined(RC_INVOKED):
            CONTEXT_AMD64 = 0x00100000
            CONTEXT_CONTROL = CONTEXT_AMD64 | 0x00000001
            CONTEXT_INTEGER = CONTEXT_AMD64 | 0x00000002
            CONTEXT_SEGMENTS = CONTEXT_AMD64 | 0x00000004
            CONTEXT_FLOATING_POINT = CONTEXT_AMD64 | 0x00000008
            CONTEXT_DEBUG_REGISTERS = CONTEXT_AMD64 | 0x00000010
            CONTEXT_FULL = CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_FLOATING_POINT
            CONTEXT_ALL = (
    CONTEXT_CONTROL  |
     CONTEXT_INTEGER  |
     CONTEXT_SEGMENTS  |
     CONTEXT_FLOATING_POINT  |
     CONTEXT_DEBUG_REGISTERS
)
            CONTEXT_XSTATE = CONTEXT_AMD64 | 0x00000040

            if defined(XBOX_SYSTEMOS):
                CONTEXT_KERNEL_DEBUGGER = 0x04000000
            # END IF
            CONTEXT_EXCEPTION_ACTIVE = 0x08000000
            CONTEXT_SERVICE_ACTIVE = 0x10000000
            CONTEXT_EXCEPTION_REQUEST = 0x40000000
            CONTEXT_EXCEPTION_REPORTING = 0x80000000
        # END IF   not defined(RC_INVOKED)
        INITIAL_MXCSR = 0x1F80
        INITIAL_FPCSR = 0x027F
        class (ctypes.Structure):
            pass
        DUMMYSTRUCTNAME._fields_ = [
            ('Header', M128A * 2),
            ('Legacy', M128A * 8),
            ('Xmm0', M128A),
            ('Xmm1', M128A),
            ('Xmm2', M128A),
            ('Xmm3', M128A),
            ('Xmm4', M128A),
            ('Xmm5', M128A),
            ('Xmm6', M128A),
            ('Xmm7', M128A),
            ('Xmm8', M128A),
            ('Xmm9', M128A),
            ('Xmm10', M128A),
            ('Xmm11', M128A),
            ('Xmm12', M128A),
            ('Xmm13', M128A),
            ('Xmm14', M128A),
            ('Xmm15', M128A),
        ]


        DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        DUMMYUNIONNAME._fields_ = [
            ('FltSave', XMM_SAVE_AREA32),
            ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
        ]


        _CONTEXT.DUMMYUNIONNAME = DUMMYUNIONNAME
        _CONTEXT._fields_ = [
            ('P1Home', ULONG64), # context record in the future.
            ('P2Home', ULONG64),
            ('P3Home', ULONG64),
            ('P4Home', ULONG64),
            ('P5Home', ULONG64),
            ('P6Home', ULONG64),
            ('ContextFlags', ULONG), # Control flags.
            ('MxCsr', ULONG),
            ('SegCs', USHORT), # Segment Registers and processor flags.
            ('SegDs', USHORT),
            ('SegEs', USHORT),
            ('SegFs', USHORT),
            ('SegGs', USHORT),
            ('SegSs', USHORT),
            ('EFlags', ULONG),
            ('Dr0', ULONG64), # Debug registers
            ('Dr1', ULONG64),
            ('Dr2', ULONG64),
            ('Dr3', ULONG64),
            ('Dr6', ULONG64),
            ('Dr7', ULONG64),
            ('Rax', ULONG64), # Integer registers.
            ('Rcx', ULONG64),
            ('Rdx', ULONG64),
            ('Rbx', ULONG64),
            ('Rsp', ULONG64),
            ('Rbp', ULONG64),
            ('Rsi', ULONG64),
            ('Rdi', ULONG64),
            ('R8', ULONG64),
            ('R9', ULONG64),
            ('R10', ULONG64),
            ('R11', ULONG64),
            ('R12', ULONG64),
            ('R13', ULONG64),
            ('R14', ULONG64),
            ('R15', ULONG64),
            ('Rip', ULONG64), # Program counter.
            ('DUMMYUNIONNAME', _CONTEXT.DUMMYUNIONNAME), # Floating point state.
            ('VectorRegister', M128A * 26), # Vector registers.
            ('VectorControl', ULONG64),
            ('DebugControl', ULONG64), # Special debug control registers.
            ('LastBranchToRip', ULONG64),
            ('LastBranchFromRip', ULONG64),
            ('LastExceptionToRip', ULONG64),
            ('LastExceptionFromRip', ULONG64),
        ]


        CONTEXT = _CONTEXT
        PCONTEXT = POINTER(_CONTEXT)


        DUMMYSTRUCTNAME._fields_ = [
            ('Header', M128A * 2),
            ('Legacy', M128A * 8),
            ('Xmm0', M128A),
            ('Xmm1', M128A),
            ('Xmm2', M128A),
            ('Xmm3', M128A),
            ('Xmm4', M128A),
            ('Xmm5', M128A),
            ('Xmm6', M128A),
            ('Xmm7', M128A),
            ('Xmm8', M128A),
            ('Xmm9', M128A),
            ('Xmm10', M128A),
            ('Xmm11', M128A),
            ('Xmm12', M128A),
            ('Xmm13', M128A),
            ('Xmm14', M128A),
            ('Xmm15', M128A),
        ]


        DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
        DUMMYUNIONNAME._fields_ = [
            ('FltSave', XMM_SAVE_AREA32),
            ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
        ]


        DUMMYSTRUCTNAME._fields_ = [
            ('Header', M128A * 2),
            ('Legacy', M128A * 8),
            ('Xmm0', M128A),
            ('Xmm1', M128A),
            ('Xmm2', M128A),
            ('Xmm3', M128A),
            ('Xmm4', M128A),
            ('Xmm5', M128A),
            ('Xmm6', M128A),
            ('Xmm7', M128A),
            ('Xmm8', M128A),
            ('Xmm9', M128A),
            ('Xmm10', M128A),
            ('Xmm11', M128A),
            ('Xmm12', M128A),
            ('Xmm13', M128A),
            ('Xmm14', M128A),
            ('Xmm15', M128A),
        ]


    # END IF   _AMD64_

    if defined(_ARM_):
        KERNEL_STACK_SIZE = 0x3000
        KERNEL_LARGE_STACK_SIZE = 0xF000
        KERNEL_LARGE_STACK_COMMIT = KERNEL_STACK_SIZE
        KERNEL_MCA_EXCEPTION_STACK_SIZE = 0x2000
        EXCEPTION_READ_FAULT = 0
        EXCEPTION_WRITE_FAULT = 1
        EXCEPTION_EXECUTE_FAULT = 8

        if not defined(RC_INVOKED):
            CONTEXT_ARM = 0x00200000
            CONTEXT_CONTROL = CONTEXT_ARM | 0x1
            CONTEXT_INTEGER = CONTEXT_ARM | 0x2
            CONTEXT_FLOATING_POINT = CONTEXT_ARM | 0x4
            CONTEXT_DEBUG_REGISTERS = CONTEXT_ARM | 0x8
            CONTEXT_FULL = CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_FLOATING_POINT
            CONTEXT_ALL = (
    CONTEXT_CONTROL  |
     CONTEXT_INTEGER  |
     CONTEXT_FLOATING_POINT  |
     CONTEXT_DEBUG_REGISTERS
)
            CONTEXT_EXCEPTION_ACTIVE = 0x8000000
            CONTEXT_SERVICE_ACTIVE = 0x10000000
            CONTEXT_EXCEPTION_REQUEST = 0x40000000
            CONTEXT_EXCEPTION_REPORTING = 0x80000000
            CONTEXT_UNWOUND_TO_CALL = 0x20000000
        # END IF   not defined(RC_INVOKED)
        INITIAL_CPSR = 0x10
        INITIAL_FPSCR = 0
        ARM_MAX_BREAKPOINTS = 8
        ARM_MAX_WATCHPOINTS = 1
        class _NEON128(ctypes.Structure):
            pass
        _NEON128._fields_ = [
            ('Low', ULONGLONG),
            ('High', LONGLONG),
        ]


        NEON128 = _NEON128
        PNEON128 = POINTER(_NEON128)


        DUMMYUNIONNAME._fields_ = [
            ('Q', NEON128 * 16),
            ('D', ULONGLONG * 32),
            ('S', ULONG * 32),
        ]


        _CONTEXT.DUMMYUNIONNAME = DUMMYUNIONNAME
        _CONTEXT._fields_ = [
            ('ContextFlags', ULONG), # Control flags.
            ('R0', ULONG), # Integer registers
            ('R1', ULONG),
            ('R2', ULONG),
            ('R3', ULONG),
            ('R4', ULONG),
            ('R5', ULONG),
            ('R6', ULONG),
            ('R7', ULONG),
            ('R8', ULONG),
            ('R9', ULONG),
            ('R10', ULONG),
            ('R11', ULONG),
            ('R12', ULONG),
            ('Sp', ULONG), # Control Registers
            ('Lr', ULONG),
            ('Pc', ULONG),
            ('Cpsr', ULONG),
            ('Fpscr', ULONG), # Floating Point/NEON Registers
            ('Padding', ULONG),
            ('DUMMYUNIONNAME', _CONTEXT.DUMMYUNIONNAME),
            ('Bvr', ULONG * ARM_MAX_BREAKPOINTS), # Debug registers
            ('Bcr', ULONG * ARM_MAX_BREAKPOINTS),
            ('Wvr', ULONG * ARM_MAX_WATCHPOINTS),
            ('Wcr', ULONG * ARM_MAX_WATCHPOINTS),
            ('Padding2', ULONG * 2),
        ]


        CONTEXT = _CONTEXT
        PCONTEXT = POINTER(_CONTEXT)


        DUMMYUNIONNAME._fields_ = [
            ('Q', NEON128 * 16),
            ('D', ULONGLONG * 32),
            ('S', ULONG * 32),
        ]


    # END IF   _ARM_

    if defined(_ARM64_) or defined(_CHPE_X86_ARM64_):
        if defined(_ARM64_):
            KERNEL_STACK_SIZE = 0x8000
            KERNEL_LARGE_STACK_SIZE = 0x12000
            KERNEL_LARGE_STACK_COMMIT = KERNEL_STACK_SIZE
            KERNEL_MCA_EXCEPTION_STACK_SIZE = 0x2000
        # END IF
        EXCEPTION_READ_FAULT = 0
        EXCEPTION_WRITE_FAULT = 1
        EXCEPTION_EXECUTE_FAULT = 8
        INITIAL_CPSR = 0x10
        INITIAL_FPSCR = 0
    # END IF   defined(_ARM64_) or defined(_CHPE_X86_ARM64_)

    if not defined(RC_INVOKED):
        CONTEXT_ARM64 = 0x00400000
        CONTEXT_ARM64_CONTROL = CONTEXT_ARM64 | 0x1
        CONTEXT_ARM64_INTEGER = CONTEXT_ARM64 | 0x2
        CONTEXT_ARM64_FLOATING_POINT = CONTEXT_ARM64 | 0x4
        CONTEXT_ARM64_DEBUG_REGISTERS = CONTEXT_ARM64 | 0x8
        CONTEXT_ARM64_X18 = CONTEXT_ARM64 | 0x10
        CONTEXT_ARM64_FULL = (
    CONTEXT_ARM64_CONTROL  |
     CONTEXT_ARM64_INTEGER  |
     CONTEXT_ARM64_FLOATING_POINT
)
        CONTEXT_ARM64_ALL = (
    CONTEXT_ARM64_CONTROL  |
     CONTEXT_ARM64_INTEGER  |
     CONTEXT_ARM64_FLOATING_POINT  |
     CONTEXT_ARM64_DEBUG_REGISTERS  |
     CONTEXT_ARM64_X18
)

        if defined(_ARM64_):
            CONTEXT_CONTROL = CONTEXT_ARM64_CONTROL
            CONTEXT_INTEGER = CONTEXT_ARM64_INTEGER
            CONTEXT_FLOATING_POINT = CONTEXT_ARM64_FLOATING_POINT
            CONTEXT_DEBUG_REGISTERS = CONTEXT_ARM64_DEBUG_REGISTERS
            CONTEXT_FULL = CONTEXT_ARM64_FULL
            CONTEXT_ALL = CONTEXT_ARM64_ALL
            CONTEXT_EXCEPTION_ACTIVE = 0x08000000
            CONTEXT_SERVICE_ACTIVE = 0x10000000
            CONTEXT_EXCEPTION_REQUEST = 0x40000000
            CONTEXT_EXCEPTION_REPORTING = 0x80000000
        # END IF

        if defined(_ARM64_) or defined(_CHPE_X86_ARM64_) or defined(_X86_):
            CONTEXT_UNWOUND_TO_CALL = 0x20000000
            CONTEXT_RET_TO_GUEST = 0x04000000
        # END IF
    # END IF   not defined(RC_INVOKED)
    ARM64_MAX_BREAKPOINTS = 8
    ARM64_MAX_WATCHPOINTS = 2
    class _ARM64_NT_NEON128(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Low', ULONGLONG),
        ('High', LONGLONG),
    ]


    _ARM64_NT_NEON128.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _ARM64_NT_NEON128._fields_ = [
        ('DUMMYSTRUCTNAME', _ARM64_NT_NEON128.DUMMYSTRUCTNAME),
        ('D', DOUBLE * 2),
        ('S', FLOAT * 4),
        ('H', USHORT * 8),
        ('B', UCHAR * 16),
    ]


    ARM64_NT_NEON128 = _ARM64_NT_NEON128
    PARM64_NT_NEON128 = POINTER(_ARM64_NT_NEON128)


    DUMMYSTRUCTNAME._fields_ = [
        ('Low', ULONGLONG),
        ('High', LONGLONG),
    ]



    if defined(_ARM64_):
        pass
    # END IF
    if defined(_ARM64_):
        _ARM64_NT_CONTEXT = _CONTEXT
        ARM64_NT_NEON128 = NEON128
    # END IF
    class _ARM64_NT_CONTEXT(DECLSPEC_ALIGN(16)):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('X0', ULONG64),
        ('X1', ULONG64),
        ('X2', ULONG64),
        ('X3', ULONG64),
        ('X4', ULONG64),
        ('X5', ULONG64),
        ('X6', ULONG64),
        ('X7', ULONG64),
        ('X8', ULONG64),
        ('X9', ULONG64),
        ('X10', ULONG64),
        ('X11', ULONG64),
        ('X12', ULONG64),
        ('X13', ULONG64),
        ('X14', ULONG64),
        ('X15', ULONG64),
        ('X16', ULONG64),
        ('X17', ULONG64),
        ('X18', ULONG64),
        ('X19', ULONG64),
        ('X20', ULONG64),
        ('X21', ULONG64),
        ('X22', ULONG64),
        ('X23', ULONG64),
        ('X24', ULONG64),
        ('X25', ULONG64),
        ('X26', ULONG64),
        ('X27', ULONG64),
        ('X28', ULONG64),
        ('Fp', ULONG64), # + 0x0f0
        ('Lr', ULONG64), # + 0x0f8
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
        ('X', ULONG64 * 31),
    ]


    _ARM64_NT_CONTEXT.DUMMYUNIONNAME = DUMMYUNIONNAME
    _ARM64_NT_CONTEXT._fields_ = [
        ('ContextFlags', ULONG), # + 0x000
        ('Cpsr', ULONG), # + 0x004
        ('DUMMYUNIONNAME', _ARM64_NT_CONTEXT.DUMMYUNIONNAME), # + 0x008
        ('Sp', ULONG64), # + 0x100
        ('Pc', ULONG64), # + 0x108
        ('V', ARM64_NT_NEON128 * 32), # + 0x110
        ('Fpcr', ULONG), # + 0x310
        ('Fpsr', ULONG), # + 0x314
        ('Bcr', ULONG * ARM64_MAX_BREAKPOINTS), # + 0x318
        ('Bvr', ULONG64 * ARM64_MAX_BREAKPOINTS), # + 0x338
        ('Wcr', ULONG * ARM64_MAX_WATCHPOINTS), # + 0x378
        ('Wvr', ULONG64 * ARM64_MAX_WATCHPOINTS), # + 0x380
    ]


    ARM64_NT_CONTEXT = _ARM64_NT_CONTEXT
    PARM64_NT_CONTEXT = POINTER(_ARM64_NT_CONTEXT)


    DUMMYSTRUCTNAME._fields_ = [
        ('X0', ULONG64),
        ('X1', ULONG64),
        ('X2', ULONG64),
        ('X3', ULONG64),
        ('X4', ULONG64),
        ('X5', ULONG64),
        ('X6', ULONG64),
        ('X7', ULONG64),
        ('X8', ULONG64),
        ('X9', ULONG64),
        ('X10', ULONG64),
        ('X11', ULONG64),
        ('X12', ULONG64),
        ('X13', ULONG64),
        ('X14', ULONG64),
        ('X15', ULONG64),
        ('X16', ULONG64),
        ('X17', ULONG64),
        ('X18', ULONG64),
        ('X19', ULONG64),
        ('X20', ULONG64),
        ('X21', ULONG64),
        ('X22', ULONG64),
        ('X23', ULONG64),
        ('X24', ULONG64),
        ('X25', ULONG64),
        ('X26', ULONG64),
        ('X27', ULONG64),
        ('X28', ULONG64),
        ('Fp', ULONG64), # + 0x0f0
        ('Lr', ULONG64), # + 0x0f8
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
        ('X', ULONG64 * 31),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('X0', ULONG64),
        ('X1', ULONG64),
        ('X2', ULONG64),
        ('X3', ULONG64),
        ('X4', ULONG64),
        ('X5', ULONG64),
        ('X6', ULONG64),
        ('X7', ULONG64),
        ('X8', ULONG64),
        ('X9', ULONG64),
        ('X10', ULONG64),
        ('X11', ULONG64),
        ('X12', ULONG64),
        ('X13', ULONG64),
        ('X14', ULONG64),
        ('X15', ULONG64),
        ('X16', ULONG64),
        ('X17', ULONG64),
        ('X18', ULONG64),
        ('X19', ULONG64),
        ('X20', ULONG64),
        ('X21', ULONG64),
        ('X22', ULONG64),
        ('X23', ULONG64),
        ('X24', ULONG64),
        ('X25', ULONG64),
        ('X26', ULONG64),
        ('X27', ULONG64),
        ('X28', ULONG64),
        ('Fp', ULONG64), # + 0x0f0
        ('Lr', ULONG64), # + 0x0f8
    ]



    if defined(_ARM64_):
        pass
    # END IF
    class WELL_KNOWN_SID_TYPE(ENUM):
        WinNullSid = 0
        WinWorldSid = 1
        WinLocalSid = 2
        WinCreatorOwnerSid = 3
        WinCreatorGroupSid = 4
        WinCreatorOwnerServerSid = 5
        WinCreatorGroupServerSid = 6
        WinNtAuthoritySid = 7
        WinDialupSid = 8
        WinNetworkSid = 9
        WinBatchSid = 10
        WinInteractiveSid = 11
        WinServiceSid = 12
        WinAnonymousSid = 13
        WinProxySid = 14
        WinEnterpriseControllersSid = 15
        WinSelfSid = 16
        WinAuthenticatedUserSid = 17
        WinRestrictedCodeSid = 18
        WinTerminalServerSid = 19
        WinRemoteLogonIdSid = 20
        WinLogonIdsSid = 21
        WinLocalSystemSid = 22
        WinLocalServiceSid = 23
        WinNetworkServiceSid = 24
        WinBuiltinDomainSid = 25
        WinBuiltinAdministratorsSid = 26
        WinBuiltinUsersSid = 27
        WinBuiltinGuestsSid = 28
        WinBuiltinPowerUsersSid = 29
        WinBuiltinAccountOperatorsSid = 30
        WinBuiltinSystemOperatorsSid = 31
        WinBuiltinPrintOperatorsSid = 32
        WinBuiltinBackupOperatorsSid = 33
        WinBuiltinReplicatorSid = 34
        WinBuiltinPreWindows2000CompatibleAccessSid = 35
        WinBuiltinRemoteDesktopUsersSid = 36
        WinBuiltinNetworkConfigurationOperatorsSid = 37
        WinAccountAdministratorSid = 38
        WinAccountGuestSid = 39
        WinAccountKrbtgtSid = 40
        WinAccountDomainAdminsSid = 41
        WinAccountDomainUsersSid = 42
        WinAccountDomainGuestsSid = 43
        WinAccountComputersSid = 44
        WinAccountControllersSid = 45
        WinAccountCertAdminsSid = 46
        WinAccountSchemaAdminsSid = 47
        WinAccountEnterpriseAdminsSid = 48
        WinAccountPolicyAdminsSid = 49
        WinAccountRasAndIasServersSid = 50
        WinNTLMAuthenticationSid = 51
        WinDigestAuthenticationSid = 52
        WinSChannelAuthenticationSid = 53
        WinThisOrganizationSid = 54
        WinOtherOrganizationSid = 55
        WinBuiltinIncomingForestTrustBuildersSid = 56
        WinBuiltinPerfMonitoringUsersSid = 57
        WinBuiltinPerfLoggingUsersSid = 58
        WinBuiltinAuthorizationAccessSid = 59
        WinBuiltinTerminalServerLicenseServersSid = 60
        WinBuiltinDCOMUsersSid = 61
        WinBuiltinIUsersSid = 62
        WinIUserSid = 63
        WinBuiltinCryptoOperatorsSid = 64
        WinUntrustedLabelSid = 65
        WinLowLabelSid = 66
        WinMediumLabelSid = 67
        WinHighLabelSid = 68
        WinSystemLabelSid = 69
        WinWriteRestrictedCodeSid = 70
        WinCreatorOwnerRightsSid = 71
        WinCacheablePrincipalsGroupSid = 72
        WinNonCacheablePrincipalsGroupSid = 73
        WinEnterpriseReadonlyControllersSid = 74
        WinAccountReadonlyControllersSid = 75
        WinBuiltinEventLogReadersGroup = 76
        WinNewEnterpriseReadonlyControllersSid = 77
        WinBuiltinCertSvcDComAccessGroup = 78
        WinMediumPlusLabelSid = 79
        WinLocalLogonSid = 80
        WinConsoleLogonSid = 81
        WinThisOrganizationCertificateSid = 82
        WinApplicationPackageAuthoritySid = 83
        WinBuiltinAnyPackageSid = 84
        WinCapabilityInternetClientSid = 85
        WinCapabilityInternetClientServerSid = 86
        WinCapabilityPrivateNetworkClientServerSid = 87
        WinCapabilityPicturesLibrarySid = 88
        WinCapabilityVideosLibrarySid = 89
        WinCapabilityMusicLibrarySid = 90
        WinCapabilityDocumentsLibrarySid = 91
        WinCapabilitySharedUserCertificatesSid = 92
        WinCapabilityEnterpriseAuthenticationSid = 93
        WinCapabilityRemovableStorageSid = 94
        WinBuiltinRDSRemoteAccessServersSid = 95
        WinBuiltinRDSEndpointServersSid = 96
        WinBuiltinRDSManagementServersSid = 97
        WinUserModeDriversSid = 98
        WinBuiltinHyperVAdminsSid = 99
        WinAccountCloneableControllersSid = 100
        WinBuiltinAccessControlAssistanceOperatorsSid = 101
        WinBuiltinRemoteManagementUsersSid = 102
        WinAuthenticationAuthorityAssertedSid = 103
        WinAuthenticationServiceAssertedSid = 104
        WinLocalAccountSid = 105
        WinLocalAccountAndAdministratorSid = 106
        WinAccountProtectedUsersSid = 107
        WinCapabilityAppointmentsSid = 108
        WinCapabilityContactsSid = 109
        WinAccountDefaultSystemManagedSid = 110
        WinBuiltinDefaultSystemManagedGroupSid = 111
        WinBuiltinStorageReplicaAdminsSid = 112
        WinAccountKeyAdminsSid = 113
        WinAccountEnterpriseKeyAdminsSid = 114
        WinAuthenticationKeyTrustSid = 115
        WinAuthenticationKeyPropertyMFASid = 116
        WinAuthenticationKeyPropertyAttestationSid = 117
        WinAuthenticationFreshKeyAuthSid = 118
        WinBuiltinDeviceOwnersSid = 119


    WinNullSid = WELL_KNOWN_SID_TYPE.WinNullSid
    WinWorldSid = WELL_KNOWN_SID_TYPE.WinWorldSid
    WinLocalSid = WELL_KNOWN_SID_TYPE.WinLocalSid
    WinCreatorOwnerSid = WELL_KNOWN_SID_TYPE.WinCreatorOwnerSid
    WinCreatorGroupSid = WELL_KNOWN_SID_TYPE.WinCreatorGroupSid
    WinCreatorOwnerServerSid = WELL_KNOWN_SID_TYPE.WinCreatorOwnerServerSid
    WinCreatorGroupServerSid = WELL_KNOWN_SID_TYPE.WinCreatorGroupServerSid
    WinNtAuthoritySid = WELL_KNOWN_SID_TYPE.WinNtAuthoritySid
    WinDialupSid = WELL_KNOWN_SID_TYPE.WinDialupSid
    WinNetworkSid = WELL_KNOWN_SID_TYPE.WinNetworkSid
    WinBatchSid = WELL_KNOWN_SID_TYPE.WinBatchSid
    WinInteractiveSid = WELL_KNOWN_SID_TYPE.WinInteractiveSid
    WinServiceSid = WELL_KNOWN_SID_TYPE.WinServiceSid
    WinAnonymousSid = WELL_KNOWN_SID_TYPE.WinAnonymousSid
    WinProxySid = WELL_KNOWN_SID_TYPE.WinProxySid
    WinEnterpriseControllersSid = WELL_KNOWN_SID_TYPE.WinEnterpriseControllersSid
    WinSelfSid = WELL_KNOWN_SID_TYPE.WinSelfSid
    WinAuthenticatedUserSid = WELL_KNOWN_SID_TYPE.WinAuthenticatedUserSid
    WinRestrictedCodeSid = WELL_KNOWN_SID_TYPE.WinRestrictedCodeSid
    WinTerminalServerSid = WELL_KNOWN_SID_TYPE.WinTerminalServerSid
    WinRemoteLogonIdSid = WELL_KNOWN_SID_TYPE.WinRemoteLogonIdSid
    WinLogonIdsSid = WELL_KNOWN_SID_TYPE.WinLogonIdsSid
    WinLocalSystemSid = WELL_KNOWN_SID_TYPE.WinLocalSystemSid
    WinLocalServiceSid = WELL_KNOWN_SID_TYPE.WinLocalServiceSid
    WinNetworkServiceSid = WELL_KNOWN_SID_TYPE.WinNetworkServiceSid
    WinBuiltinDomainSid = WELL_KNOWN_SID_TYPE.WinBuiltinDomainSid
    WinBuiltinAdministratorsSid = WELL_KNOWN_SID_TYPE.WinBuiltinAdministratorsSid
    WinBuiltinUsersSid = WELL_KNOWN_SID_TYPE.WinBuiltinUsersSid
    WinBuiltinGuestsSid = WELL_KNOWN_SID_TYPE.WinBuiltinGuestsSid
    WinBuiltinPowerUsersSid = WELL_KNOWN_SID_TYPE.WinBuiltinPowerUsersSid
    WinBuiltinAccountOperatorsSid = WELL_KNOWN_SID_TYPE.WinBuiltinAccountOperatorsSid
    WinBuiltinSystemOperatorsSid = WELL_KNOWN_SID_TYPE.WinBuiltinSystemOperatorsSid
    WinBuiltinPrintOperatorsSid = WELL_KNOWN_SID_TYPE.WinBuiltinPrintOperatorsSid
    WinBuiltinBackupOperatorsSid = WELL_KNOWN_SID_TYPE.WinBuiltinBackupOperatorsSid
    WinBuiltinReplicatorSid = WELL_KNOWN_SID_TYPE.WinBuiltinReplicatorSid
    WinBuiltinPreWindows2000CompatibleAccessSid = WELL_KNOWN_SID_TYPE.WinBuiltinPreWindows2000CompatibleAccessSid
    WinBuiltinRemoteDesktopUsersSid = WELL_KNOWN_SID_TYPE.WinBuiltinRemoteDesktopUsersSid
    WinBuiltinNetworkConfigurationOperatorsSid = WELL_KNOWN_SID_TYPE.WinBuiltinNetworkConfigurationOperatorsSid
    WinAccountAdministratorSid = WELL_KNOWN_SID_TYPE.WinAccountAdministratorSid
    WinAccountGuestSid = WELL_KNOWN_SID_TYPE.WinAccountGuestSid
    WinAccountKrbtgtSid = WELL_KNOWN_SID_TYPE.WinAccountKrbtgtSid
    WinAccountDomainAdminsSid = WELL_KNOWN_SID_TYPE.WinAccountDomainAdminsSid
    WinAccountDomainUsersSid = WELL_KNOWN_SID_TYPE.WinAccountDomainUsersSid
    WinAccountDomainGuestsSid = WELL_KNOWN_SID_TYPE.WinAccountDomainGuestsSid
    WinAccountComputersSid = WELL_KNOWN_SID_TYPE.WinAccountComputersSid
    WinAccountControllersSid = WELL_KNOWN_SID_TYPE.WinAccountControllersSid
    WinAccountCertAdminsSid = WELL_KNOWN_SID_TYPE.WinAccountCertAdminsSid
    WinAccountSchemaAdminsSid = WELL_KNOWN_SID_TYPE.WinAccountSchemaAdminsSid
    WinAccountEnterpriseAdminsSid = WELL_KNOWN_SID_TYPE.WinAccountEnterpriseAdminsSid
    WinAccountPolicyAdminsSid = WELL_KNOWN_SID_TYPE.WinAccountPolicyAdminsSid
    WinAccountRasAndIasServersSid = WELL_KNOWN_SID_TYPE.WinAccountRasAndIasServersSid
    WinNTLMAuthenticationSid = WELL_KNOWN_SID_TYPE.WinNTLMAuthenticationSid
    WinDigestAuthenticationSid = WELL_KNOWN_SID_TYPE.WinDigestAuthenticationSid
    WinSChannelAuthenticationSid = WELL_KNOWN_SID_TYPE.WinSChannelAuthenticationSid
    WinThisOrganizationSid = WELL_KNOWN_SID_TYPE.WinThisOrganizationSid
    WinOtherOrganizationSid = WELL_KNOWN_SID_TYPE.WinOtherOrganizationSid
    WinBuiltinIncomingForestTrustBuildersSid = WELL_KNOWN_SID_TYPE.WinBuiltinIncomingForestTrustBuildersSid
    WinBuiltinPerfMonitoringUsersSid = WELL_KNOWN_SID_TYPE.WinBuiltinPerfMonitoringUsersSid
    WinBuiltinPerfLoggingUsersSid = WELL_KNOWN_SID_TYPE.WinBuiltinPerfLoggingUsersSid
    WinBuiltinAuthorizationAccessSid = WELL_KNOWN_SID_TYPE.WinBuiltinAuthorizationAccessSid
    WinBuiltinTerminalServerLicenseServersSid = WELL_KNOWN_SID_TYPE.WinBuiltinTerminalServerLicenseServersSid
    WinBuiltinDCOMUsersSid = WELL_KNOWN_SID_TYPE.WinBuiltinDCOMUsersSid
    WinBuiltinIUsersSid = WELL_KNOWN_SID_TYPE.WinBuiltinIUsersSid
    WinIUserSid = WELL_KNOWN_SID_TYPE.WinIUserSid
    WinBuiltinCryptoOperatorsSid = WELL_KNOWN_SID_TYPE.WinBuiltinCryptoOperatorsSid
    WinUntrustedLabelSid = WELL_KNOWN_SID_TYPE.WinUntrustedLabelSid
    WinLowLabelSid = WELL_KNOWN_SID_TYPE.WinLowLabelSid
    WinMediumLabelSid = WELL_KNOWN_SID_TYPE.WinMediumLabelSid
    WinHighLabelSid = WELL_KNOWN_SID_TYPE.WinHighLabelSid
    WinSystemLabelSid = WELL_KNOWN_SID_TYPE.WinSystemLabelSid
    WinWriteRestrictedCodeSid = WELL_KNOWN_SID_TYPE.WinWriteRestrictedCodeSid
    WinCreatorOwnerRightsSid = WELL_KNOWN_SID_TYPE.WinCreatorOwnerRightsSid
    WinCacheablePrincipalsGroupSid = WELL_KNOWN_SID_TYPE.WinCacheablePrincipalsGroupSid
    WinNonCacheablePrincipalsGroupSid = WELL_KNOWN_SID_TYPE.WinNonCacheablePrincipalsGroupSid
    WinEnterpriseReadonlyControllersSid = WELL_KNOWN_SID_TYPE.WinEnterpriseReadonlyControllersSid
    WinAccountReadonlyControllersSid = WELL_KNOWN_SID_TYPE.WinAccountReadonlyControllersSid
    WinBuiltinEventLogReadersGroup = WELL_KNOWN_SID_TYPE.WinBuiltinEventLogReadersGroup
    WinNewEnterpriseReadonlyControllersSid = WELL_KNOWN_SID_TYPE.WinNewEnterpriseReadonlyControllersSid
    WinBuiltinCertSvcDComAccessGroup = WELL_KNOWN_SID_TYPE.WinBuiltinCertSvcDComAccessGroup
    WinMediumPlusLabelSid = WELL_KNOWN_SID_TYPE.WinMediumPlusLabelSid
    WinLocalLogonSid = WELL_KNOWN_SID_TYPE.WinLocalLogonSid
    WinConsoleLogonSid = WELL_KNOWN_SID_TYPE.WinConsoleLogonSid
    WinThisOrganizationCertificateSid = WELL_KNOWN_SID_TYPE.WinThisOrganizationCertificateSid
    WinApplicationPackageAuthoritySid = WELL_KNOWN_SID_TYPE.WinApplicationPackageAuthoritySid
    WinBuiltinAnyPackageSid = WELL_KNOWN_SID_TYPE.WinBuiltinAnyPackageSid
    WinCapabilityInternetClientSid = WELL_KNOWN_SID_TYPE.WinCapabilityInternetClientSid
    WinCapabilityInternetClientServerSid = WELL_KNOWN_SID_TYPE.WinCapabilityInternetClientServerSid
    WinCapabilityPrivateNetworkClientServerSid = WELL_KNOWN_SID_TYPE.WinCapabilityPrivateNetworkClientServerSid
    WinCapabilityPicturesLibrarySid = WELL_KNOWN_SID_TYPE.WinCapabilityPicturesLibrarySid
    WinCapabilityVideosLibrarySid = WELL_KNOWN_SID_TYPE.WinCapabilityVideosLibrarySid
    WinCapabilityMusicLibrarySid = WELL_KNOWN_SID_TYPE.WinCapabilityMusicLibrarySid
    WinCapabilityDocumentsLibrarySid = WELL_KNOWN_SID_TYPE.WinCapabilityDocumentsLibrarySid
    WinCapabilitySharedUserCertificatesSid = WELL_KNOWN_SID_TYPE.WinCapabilitySharedUserCertificatesSid
    WinCapabilityEnterpriseAuthenticationSid = WELL_KNOWN_SID_TYPE.WinCapabilityEnterpriseAuthenticationSid
    WinCapabilityRemovableStorageSid = WELL_KNOWN_SID_TYPE.WinCapabilityRemovableStorageSid
    WinBuiltinRDSRemoteAccessServersSid = WELL_KNOWN_SID_TYPE.WinBuiltinRDSRemoteAccessServersSid
    WinBuiltinRDSEndpointServersSid = WELL_KNOWN_SID_TYPE.WinBuiltinRDSEndpointServersSid
    WinBuiltinRDSManagementServersSid = WELL_KNOWN_SID_TYPE.WinBuiltinRDSManagementServersSid
    WinUserModeDriversSid = WELL_KNOWN_SID_TYPE.WinUserModeDriversSid
    WinBuiltinHyperVAdminsSid = WELL_KNOWN_SID_TYPE.WinBuiltinHyperVAdminsSid
    WinAccountCloneableControllersSid = WELL_KNOWN_SID_TYPE.WinAccountCloneableControllersSid
    WinBuiltinAccessControlAssistanceOperatorsSid = WELL_KNOWN_SID_TYPE.WinBuiltinAccessControlAssistanceOperatorsSid
    WinBuiltinRemoteManagementUsersSid = WELL_KNOWN_SID_TYPE.WinBuiltinRemoteManagementUsersSid
    WinAuthenticationAuthorityAssertedSid = WELL_KNOWN_SID_TYPE.WinAuthenticationAuthorityAssertedSid
    WinAuthenticationServiceAssertedSid = WELL_KNOWN_SID_TYPE.WinAuthenticationServiceAssertedSid
    WinLocalAccountSid = WELL_KNOWN_SID_TYPE.WinLocalAccountSid
    WinLocalAccountAndAdministratorSid = WELL_KNOWN_SID_TYPE.WinLocalAccountAndAdministratorSid
    WinAccountProtectedUsersSid = WELL_KNOWN_SID_TYPE.WinAccountProtectedUsersSid
    WinCapabilityAppointmentsSid = WELL_KNOWN_SID_TYPE.WinCapabilityAppointmentsSid
    WinCapabilityContactsSid = WELL_KNOWN_SID_TYPE.WinCapabilityContactsSid
    WinAccountDefaultSystemManagedSid = WELL_KNOWN_SID_TYPE.WinAccountDefaultSystemManagedSid
    WinBuiltinDefaultSystemManagedGroupSid = WELL_KNOWN_SID_TYPE.WinBuiltinDefaultSystemManagedGroupSid
    WinBuiltinStorageReplicaAdminsSid = WELL_KNOWN_SID_TYPE.WinBuiltinStorageReplicaAdminsSid
    WinAccountKeyAdminsSid = WELL_KNOWN_SID_TYPE.WinAccountKeyAdminsSid
    WinAccountEnterpriseKeyAdminsSid = WELL_KNOWN_SID_TYPE.WinAccountEnterpriseKeyAdminsSid
    WinAuthenticationKeyTrustSid = WELL_KNOWN_SID_TYPE.WinAuthenticationKeyTrustSid
    WinAuthenticationKeyPropertyMFASid = WELL_KNOWN_SID_TYPE.WinAuthenticationKeyPropertyMFASid
    WinAuthenticationKeyPropertyAttestationSid = WELL_KNOWN_SID_TYPE.WinAuthenticationKeyPropertyAttestationSid
    WinAuthenticationFreshKeyAuthSid = WELL_KNOWN_SID_TYPE.WinAuthenticationFreshKeyAuthSid
    WinBuiltinDeviceOwnersSid = WELL_KNOWN_SID_TYPE.WinBuiltinDeviceOwnersSid
    SE_UNSOLICITED_INPUT_PRIVILEGE = 6L
    SE_SIGNING_LEVEL_UNCHECKED = 0x00000000
    SE_SIGNING_LEVEL_UNSIGNED = 0x00000001
    SE_SIGNING_LEVEL_ENTERPRISE = 0x00000002
    SE_SIGNING_LEVEL_CUSTOM_1 = 0x00000003
    SE_SIGNING_LEVEL_AUTHENTICODE = 0x00000004
    SE_SIGNING_LEVEL_CUSTOM_2 = 0x00000005
    SE_SIGNING_LEVEL_STORE = 0x00000006
    SE_SIGNING_LEVEL_CUSTOM_3 = 0x00000007
    SE_SIGNING_LEVEL_ANTIMALWARE = SE_SIGNING_LEVEL_CUSTOM_3
    SE_SIGNING_LEVEL_MICROSOFT = 0x00000008
    SE_SIGNING_LEVEL_CUSTOM_4 = 0x00000009
    SE_SIGNING_LEVEL_CUSTOM_5 = 0x0000000A
    SE_SIGNING_LEVEL_DYNAMIC_CODEGEN = 0x0000000B
    SE_SIGNING_LEVEL_WINDOWS = 0x0000000C
    SE_SIGNING_LEVEL_CUSTOM_7 = 0x0000000D
    SE_SIGNING_LEVEL_WINDOWS_TCB = 0x0000000E
    SE_SIGNING_LEVEL_CUSTOM_6 = 0x0000000F


    class _SE_IMAGE_SIGNATURE_TYPE(ENUM):
        SeImageSignatureNone = 0
        SeImageSignatureEmbedded = 1
        SeImageSignatureCache = 2
        SeImageSignatureCatalogCached = 3
        SeImageSignatureCatalogNotCached = 4
        SeImageSignatureCatalogHint = 5
        SeImageSignaturePackageCatalog = 6


    SE_IMAGE_SIGNATURE_TYPE = _SE_IMAGE_SIGNATURE_TYPE
    PSE_IMAGE_SIGNATURE_TYPE = POINTER(_SE_IMAGE_SIGNATURE_TYPE)
    if not defined(_NTLSA_IFS_):
        if not defined(_NTLSA_AUDIT_):
            _NTLSA_AUDIT_ = 1


            class _SE_ADT_PARAMETER_TYPE(ENUM):
                SeAdtParmTypeNone = 0
                SeAdtParmTypeString = 1
                SeAdtParmTypeFileSpec = 2
                SeAdtParmTypeULONG = 3
                SeAdtParmTypeSid = 4
                SeAdtParmTypeLogonId = 5
                SeAdtParmTypeNoLogonId = 6
                SeAdtParmTypeAccessMask = 7
                SeAdtParmTypePrivs = 8
                SeAdtParmTypeObjectTypes = 9
                SeAdtParmTypeHexULONG = 10
                SeAdtParmTypePtr = 11
                SeAdtParmTypeTime = 12
                SeAdtParmTypeGuid = 13
                SeAdtParmTypeLuid = 14
                SeAdtParmTypeHexInt64 = 15
                SeAdtParmTypeStringList = 16
                SeAdtParmTypeSidList = 17
                SeAdtParmTypeDuration = 18
                SeAdtParmTypeUserAccountControl = 19
                SeAdtParmTypeNoUac = 20
                SeAdtParmTypeMessage = 21
                SeAdtParmTypeDateTime = 22
                SeAdtParmTypeSockAddr = 23
                SeAdtParmTypeSD = 24
                SeAdtParmTypeLogonHours = 25
                SeAdtParmTypeLogonIdNoSid = 26
                SeAdtParmTypeULONGNoConv = 27
                SeAdtParmTypeSockAddrNoPort = 28
                SeAdtParmTypeAccessReason = 29
                SeAdtParmTypeStagingReason = 30
                SeAdtParmTypeResourceAttribute = 31
                SeAdtParmTypeClaims = 32
                SeAdtParmTypeLogonIdAsSid = 33
                SeAdtParmTypeMultiSzString = 34
                SeAdtParmTypeLogonIdEx = 35


            SE_ADT_PARAMETER_TYPE = _SE_ADT_PARAMETER_TYPE
            PSE_ADT_PARAMETER_TYPE = POINTER(_SE_ADT_PARAMETER_TYPE)
            if not defined(GUID_DEFINED):
                pass
            # END IF  GUID_DEFINED
            class _SE_ADT_OBJECT_TYPE(ctypes.Structure):
                pass
            _SE_ADT_OBJECT_TYPE._fields_ = [
                ('ObjectType', GUID),
                ('Flags', USHORT),
                ('Level', USHORT),
                ('AccessMask', ACCESS_MASK),
            ]


            SE_ADT_OBJECT_TYPE = _SE_ADT_OBJECT_TYPE
            PSE_ADT_OBJECT_TYPE = POINTER(_SE_ADT_OBJECT_TYPE)


            SE_ADT_OBJECT_ONLY = 0x1
            class _SE_ADT_PARAMETER_ARRAY_ENTRY(ctypes.Structure):
                pass
            _SE_ADT_PARAMETER_ARRAY_ENTRY._fields_ = [
                ('Type', SE_ADT_PARAMETER_TYPE),
                ('Length', ULONG),
                ('Data', ULONG_PTR * 2),
                ('Address', PVOID),
            ]


            SE_ADT_PARAMETER_ARRAY_ENTRY = _SE_ADT_PARAMETER_ARRAY_ENTRY
            PSE_ADT_PARAMETER_ARRAY_ENTRY = POINTER(_SE_ADT_PARAMETER_ARRAY_ENTRY)


            class _SE_ADT_ACCESS_REASON(ctypes.Structure):
                pass
            _SE_ADT_ACCESS_REASON._fields_ = [
                ('AccessMask', ACCESS_MASK),
                ('AccessReasons', ULONG * 32),
                ('ObjectTypeIndex', ULONG),
                ('AccessGranted', ULONG),
                ('SecurityDescriptor', PSECURITY_DESCRIPTOR), # multple SDs may be stored here in self - relative way.
            ]


            SE_ADT_ACCESS_REASON = _SE_ADT_ACCESS_REASON
            PSE_ADT_ACCESS_REASON = POINTER(_SE_ADT_ACCESS_REASON)


            class _SE_ADT_CLAIMS(ctypes.Structure):
                pass
            _SE_ADT_CLAIMS._fields_ = [
                ('Length', ULONG),
                ('Claims', PCLAIMS_BLOB), # one claim blob will be stored here in self - relative way
            ]


            SE_ADT_CLAIMS = _SE_ADT_CLAIMS
            PSE_ADT_CLAIMS = POINTER(_SE_ADT_CLAIMS)


            SE_MAX_AUDIT_PARAMETERS = 32
            SE_MAX_GENERIC_AUDIT_PARAMETERS = 28
            class _SE_ADT_PARAMETER_ARRAY(ctypes.Structure):
                pass
            _SE_ADT_PARAMETER_ARRAY._fields_ = [
                ('CategoryId', ULONG),
                ('AuditId', ULONG),
                ('ParameterCount', ULONG),
                ('Length', ULONG),
                ('FlatSubCategoryId', USHORT),
                ('Type', USHORT),
                ('Flags', ULONG),
                ('Parameters', SE_ADT_PARAMETER_ARRAY_ENTRY * SE_MAX_AUDIT_PARAMETERS),
            ]


            SE_ADT_PARAMETER_ARRAY = _SE_ADT_PARAMETER_ARRAY
            PSE_ADT_PARAMETER_ARRAY = POINTER(_SE_ADT_PARAMETER_ARRAY)


            class _SE_ADT_PARAMETER_ARRAY_EX(ctypes.Structure):
                pass
            _SE_ADT_PARAMETER_ARRAY_EX._fields_ = [
                ('CategoryId', ULONG),
                ('AuditId', ULONG),
                ('Version', ULONG),
                ('ParameterCount', ULONG),
                ('Length', ULONG),
                ('FlatSubCategoryId', USHORT),
                ('Type', USHORT),
                ('Flags', ULONG),
                ('Parameters', SE_ADT_PARAMETER_ARRAY_ENTRY * SE_MAX_AUDIT_PARAMETERS),
            ]


            SE_ADT_PARAMETER_ARRAY_EX = _SE_ADT_PARAMETER_ARRAY_EX
            PSE_ADT_PARAMETER_ARRAY_EX = POINTER(_SE_ADT_PARAMETER_ARRAY_EX)


            SE_ADT_PARAMETERS_SELF_RELATIVE = 0x00000001
            SE_ADT_PARAMETERS_SEND_TO_LSA = 0x00000002
            SE_ADT_PARAMETER_EXTENSIBLE_AUDIT = 0x00000004
            SE_ADT_PARAMETER_GENERIC_AUDIT = 0x00000008
            SE_ADT_PARAMETER_WRITE_SYNCHRONOUS = 0x00000010


def LSAP_SE_ADT_PARAMETER_ARRAY_TRUE_SIZE(AuditParameters):
    return (ctypes.sizeofSE_ADT_PARAMETER_ARRAY - ctypes.sizeofSE_ADT_PARAMETER_ARRAY_ENTRY * (SE_MAX_AUDIT_PARAMETERS - AuditParameters - >ParameterCount))
        # END IF   _NTLSA_AUDIT_
    # END IF   _NTLSA_IFS_

    if not defined(_RTL_RUN_ONCE_DEF):
        _RTL_RUN_ONCE_DEF = 1
        RTL_RUN_ONCE_INIT = [0]
        RTL_RUN_ONCE_CHECK_ONLY = 0x00000001
        RTL_RUN_ONCE_ASYNC = 0x00000002
        RTL_RUN_ONCE_INIT_FAILED = 0x00000004
        RTL_RUN_ONCE_CTX_RESERVED_BITS = 2
        class _RTL_RUN_ONCE(ctypes.Union):
            pass
        _RTL_RUN_ONCE._fields_ = [
            ('Ptr', PVOID),
        ]


        RTL_RUN_ONCE = _RTL_RUN_ONCE
        PRTL_RUN_ONCE = POINTER(_RTL_RUN_ONCE)


    # END IF   _RTL_RUN_ONCE_DEF

    if (NTDDI_VERSION >= NTDDI_LONGHORN):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_LONGHORN
    class _TABLE_SEARCH_RESULT(ENUM):
        TableEmptyTree = 1
        TableFoundNode = 2
        TableInsertAsLeft = 3
        TableInsertAsRight = 4


    TABLE_SEARCH_RESULT = _TABLE_SEARCH_RESULT
    class _RTL_GENERIC_COMPARE_RESULTS(ENUM):
        GenericLessThan = 1
        GenericGreaterThan = 2
        GenericEqual = 3


    RTL_GENERIC_COMPARE_RESULTS = _RTL_GENERIC_COMPARE_RESULTS
    _RTL_AVL_TABLE = struct


    class _RTL_BALANCED_LINKS(ctypes.Structure):
        pass
    _RTL_BALANCED_LINKS._fields_ = [
        ('Parent', POINTER(_RTL_BALANCED_LINKS)),
        ('LeftChild', POINTER(_RTL_BALANCED_LINKS)),
        ('RightChild', POINTER(_RTL_BALANCED_LINKS)),
        ('Balance', CHAR),
        ('Reserved', UCHAR * 3),
    ]


    RTL_BALANCED_LINKS = _RTL_BALANCED_LINKS


    Parent = POINTER(_RTL_BALANCED_LINKS)


    LeftChild = POINTER(_RTL_BALANCED_LINKS)


    RightChild = POINTER(_RTL_BALANCED_LINKS)


    class _RTL_AVL_TABLE(ctypes.Structure):
        pass
    _RTL_AVL_TABLE._fields_ = [
        ('BalancedRoot', RTL_BALANCED_LINKS),
        ('OrderedPointer', PVOID),
        ('WhichOrderedElement', ULONG),
        ('NumberGenericTableElements', ULONG),
        ('DepthOfTree', ULONG),
        ('RestartKey', PRTL_BALANCED_LINKS),
        ('DeleteCount', ULONG),
        ('CompareRoutine', PRTL_AVL_COMPARE_ROUTINE),
        ('AllocateRoutine', PRTL_AVL_ALLOCATE_ROUTINE),
        ('FreeRoutine', PRTL_AVL_FREE_ROUTINE),
        ('TableContext', PVOID),
    ]


    RTL_AVL_TABLE = _RTL_AVL_TABLE


    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN8
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WINXP
    if defined(RTL_USE_AVL_TABLES):
        PRTL_GENERIC_COMPARE_ROUTINE = PRTL_AVL_COMPARE_ROUTINE
        RTL_GENERIC_COMPARE_ROUTINE = RTL_AVL_COMPARE_ROUTINE
        PRTL_GENERIC_ALLOCATE_ROUTINE = PRTL_AVL_ALLOCATE_ROUTINE
        RTL_GENERIC_ALLOCATE_ROUTINE = RTL_AVL_ALLOCATE_ROUTINE
        PRTL_GENERIC_FREE_ROUTINE = PRTL_AVL_FREE_ROUTINE
        RTL_GENERIC_FREE_ROUTINE = RTL_AVL_FREE_ROUTINE
        RTL_GENERIC_TABLE = RTL_AVL_TABLE
        PRTL_GENERIC_TABLE = PRTL_AVL_TABLE
        RtlInitializeGenericTable = RtlInitializeGenericTableAvl
        RtlInsertElementGenericTable = RtlInsertElementGenericTableAvl
        RtlInsertElementGenericTableFull = RtlInsertElementGenericTableFullAvl
        RtlDeleteElementGenericTable = RtlDeleteElementGenericTableAvl
        RtlLookupElementGenericTable = RtlLookupElementGenericTableAvl
        RtlLookupElementGenericTableFull = RtlLookupElementGenericTableFullAvl
        RtlEnumerateGenericTable = RtlEnumerateGenericTableAvl
        RtlEnumerateGenericTableWithoutSplaying = (
    RtlEnumerateGenericTableWithoutSplayingAvl
)
        RtlGetElementGenericTable = RtlGetElementGenericTableAvl
        RtlNumberGenericTableElements = RtlNumberGenericTableElementsAvl
        RtlIsGenericTableEmpty = RtlIsGenericTableEmptyAvl
    # END IF   RTL_USE_AVL_TABLES
    class _RTL_SPLAY_LINKS(ctypes.Structure):
        pass
    _RTL_SPLAY_LINKS._fields_ = [
        ('Parent', POINTER(_RTL_SPLAY_LINKS)),
        ('LeftChild', POINTER(_RTL_SPLAY_LINKS)),
        ('RightChild', POINTER(_RTL_SPLAY_LINKS)),
    ]


    RTL_SPLAY_LINKS = _RTL_SPLAY_LINKS


    Parent = POINTER(_RTL_SPLAY_LINKS)


    LeftChild = POINTER(_RTL_SPLAY_LINKS)


    RightChild = POINTER(_RTL_SPLAY_LINKS)



    if not defined(MIDL_PASS) and not defined(SORTPP_PASS):
        pass
    # END IF   not defined(MIDL_PASS) and not defined(SORTPP_PASS)


def RtlParent(Links):
    return (PRTL_SPLAY_LINKSLinks - >Parent)


def RtlLeftChild(Links):
    return (PRTL_SPLAY_LINKSLinks - >LeftChild)


def RtlRightChild(Links):
    return (PRTL_SPLAY_LINKSLinks - >RightChild)


def RtlIsRoot(Links):
    return ((RtlParentLinks == PRTL_SPLAY_LINKSLinks))


def RtlIsLeftChild(Links):
    return ((RtlLeftChild(RtlParentLinks) == PRTL_SPLAY_LINKSLinks))


def RtlIsRightChild(Links):
    return ((RtlRightChild(RtlParentLinks) == PRTL_SPLAY_LINKSLinks))

    if not defined(MIDL_PASS) and not defined(SORTPP_PASS):
        pass
    # END IF   not defined(MIDL_PASS) and not defined(SORTPP_PASS)
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if not defined(RTL_USE_AVL_TABLES):
        _RTL_GENERIC_TABLE = struct


        class _RTL_GENERIC_TABLE(ctypes.Structure):
            pass
        _RTL_GENERIC_TABLE._fields_ = [
            ('TableRoot', PRTL_SPLAY_LINKS),
            ('InsertOrderList', LIST_ENTRY),
            ('OrderedPointer', PLIST_ENTRY),
            ('WhichOrderedElement', ULONG),
            ('NumberGenericTableElements', ULONG),
            ('CompareRoutine', PRTL_GENERIC_COMPARE_ROUTINE),
            ('AllocateRoutine', PRTL_GENERIC_ALLOCATE_ROUTINE),
            ('FreeRoutine', PRTL_GENERIC_FREE_ROUTINE),
            ('TableContext', PVOID),
        ]


        RTL_GENERIC_TABLE = _RTL_GENERIC_TABLE


        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
    # END IF   RTL_USE_AVL_TABLES
    RTL_HASH_ALLOCATED_HEADER = 0x00000001
    RTL_HASH_RESERVED_SIGNATURE = 0
    class _RTL_DYNAMIC_HASH_TABLE_ENTRY(ctypes.Structure):
        pass
    _RTL_DYNAMIC_HASH_TABLE_ENTRY._fields_ = [
        ('Linkage', LIST_ENTRY),
        ('Signature', ULONG_PTR),
    ]


    RTL_DYNAMIC_HASH_TABLE_ENTRY = _RTL_DYNAMIC_HASH_TABLE_ENTRY
    PRTL_DYNAMIC_HASH_TABLE_ENTRY = POINTER(_RTL_DYNAMIC_HASH_TABLE_ENTRY)




def HASH_ENTRY_KEY(x):
    return (x - >Signature)
    class _RTL_DYNAMIC_HASH_TABLE_CONTEXT(ctypes.Structure):
        pass
    _RTL_DYNAMIC_HASH_TABLE_CONTEXT._fields_ = [
        ('ChainHead', PLIST_ENTRY),
        ('PrevLinkage', PLIST_ENTRY),
        ('Signature', ULONG_PTR),
    ]


    RTL_DYNAMIC_HASH_TABLE_CONTEXT = _RTL_DYNAMIC_HASH_TABLE_CONTEXT
    PRTL_DYNAMIC_HASH_TABLE_CONTEXT = POINTER(_RTL_DYNAMIC_HASH_TABLE_CONTEXT)


    class _RTL_DYNAMIC_HASH_TABLE_ENUMERATOR(ctypes.Structure):
        pass
    _Union_1._fields_ = [
        ('HashEntry', RTL_DYNAMIC_HASH_TABLE_ENTRY),
        ('CurEntry', PLIST_ENTRY),
    ]


    _RTL_DYNAMIC_HASH_TABLE_ENUMERATOR._Union_1 = _Union_1
    _RTL_DYNAMIC_HASH_TABLE_ENUMERATOR._anonymous_ = (
        '_Union_1',
    )
    _RTL_DYNAMIC_HASH_TABLE_ENUMERATOR._fields_ = [
        ('_Union_1', _RTL_DYNAMIC_HASH_TABLE_ENUMERATOR._Union_1),
        ('ChainHead', PLIST_ENTRY),
        ('BucketIndex', ULONG),
    ]


    RTL_DYNAMIC_HASH_TABLE_ENUMERATOR = _RTL_DYNAMIC_HASH_TABLE_ENUMERATOR
    PRTL_DYNAMIC_HASH_TABLE_ENUMERATOR = POINTER(_RTL_DYNAMIC_HASH_TABLE_ENUMERATOR)


    ._fields_ = [
        ('HashEntry', RTL_DYNAMIC_HASH_TABLE_ENTRY),
        ('CurEntry', PLIST_ENTRY),
    ]


    class _RTL_DYNAMIC_HASH_TABLE(ctypes.Structure):
        pass
    _RTL_DYNAMIC_HASH_TABLE._fields_ = [
        ('Flags', ULONG), # Entries initialized at creation
        ('Shift', ULONG),
        ('TableSize', ULONG), # Entries used in bucket computation.
        ('Pivot', ULONG),
        ('DivisorMask', ULONG),
        ('NumEntries', ULONG), # Counters
        ('NonEmptyBuckets', ULONG),
        ('NumEnumerators', ULONG),
        ('Directory', PVOID), # The directory. This field is for internal use only.
    ]


    RTL_DYNAMIC_HASH_TABLE = _RTL_DYNAMIC_HASH_TABLE
    PRTL_DYNAMIC_HASH_TABLE = POINTER(_RTL_DYNAMIC_HASH_TABLE)



        if (NTDDI_VERSION >= NTDDI_WIN7):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN7):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN7):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN7):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN7):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN7):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN7):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN7):
            pass
        # END IF
    if not defined(MIDL_PASS) and not defined(SORTPP_PASS):
        pass
    # END IF   not defined(MIDL_PASS) and not defined(SORTPP_PASS)
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINTHRESHOLD):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINTHRESHOLD):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINTHRESHOLD):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if defined (_MSC_VER) and ( _MSC_VER >= 900 ):
        pass
    # END IF
    if (defined(_M_AMD64) or defined(_M_IA64)) and not defined(_REALLY_GET_CALLERS_CALLER_):


def RtlGetCallersAddress(CallersAddress, CallersCaller):
    return *CallersAddress = PVOID_ReturnAddress; *CallersCaller = NULL;

        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
else:
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        RTL_STACK_WALKING_MODE_FRAMES_TO_SKIP_SHIFT = 8
    # END IF

        if (NTDDI_VERSION >= NTDDI_WIN7):
            pass
        # END IF
    if not defined(MIDL_PASS):
        pass
    # END IF
        if (NTDDI_VERSION >= NTDDI_WIN10_RS3):
            pass
        # END IF
    if not defined(MIDL_PASS):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_THRESHOLD):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
        if defined(_AMD64_) or defined(_ARM_) or defined(_ARM64_) or defined(_IA64_) or defined(_CHPE_X86_ARM64_):
            pass
            if (NTDDI_VERSION >= NTDDI_WIN2K):
                pass
            # END IF
    else:
            pass
        # END IF   defined(_AMD64_) or defined(_ARM_) or defined(_ARM64_) or defined(_IA64_)
    if not defined(MIDL_PASS):
        pass
    # END IF   not defined(MIDL_PASS)


def RtlEqualLuid(L1, L2):
    return (L1 - >LowPart == L2 - >LowPart) and (L1 - >HighPart == L2 - >HighPart)


def RtlIsZeroLuid(L1):
    return BOOLEAN ((L1 - >LowPart | L1 - >HighPart) == 0)

    if not defined(MIDL_PASS):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_VISTA):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8) and not defined(MIDL_PASS):
        pass
    # END IF   (NTDDI_VERSION >= NTDDI_WIN8) and not defined(MIDL_PASS)
    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_RS1
    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN10_RS1
    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN10_RS1
    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN10_RS1
    if (NTDDI_VERSION >= NTDDI_WIN10_RS4):
        class _STATE_LOCATION_TYPE(ENUM):
            LocationTypeRegistry = 0
            LocationTypeFileSystem = 1
            LocationTypeMaximum = 2


        STATE_LOCATION_TYPE = _STATE_LOCATION_TYPE
    # END IF   NTDDI_VERSION >= NTDDI_WIN10_RS3
    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN10_RS1
    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN10_RS1
    if (NTDDI_VERSION >= NTDDI_WIN10_RS2):
        pass
    # END IF   NTDDI_VERSION >= NTDDI_WIN10_RS2
    if (NTDDI_VERSION >= NTDDI_WIN10_RS2) and defined(_AMD64_):
        class _NV_MEMORY_RANGE(ctypes.Structure):
            pass
        _NV_MEMORY_RANGE._fields_ = [
            ('BaseAddress', POINTER(VOID)),
            ('Length', SIZE_T),
        ]


        NV_MEMORY_RANGE = _NV_MEMORY_RANGE
        PNV_MEMORY_RANGE = POINTER(_NV_MEMORY_RANGE)


        FLUSH_NV_MEMORY_IN_FLAG_NO_DRAIN = 0x00000001
        FLUSH_NV_MEMORY_DEFAULT_TOKEN = ULONG_PTR)( - 1
    # END IF   (NTDDI_VERSION >= NTDDI_RS2) and defined(_AMD64_)

    if (NTDDI_VERSION >= NTDDI_WIN10_RS2):
        RTL_CORRELATION_VECTOR_STRING_LENGTH = 129
        RTL_CORRELATION_VECTOR_VERSION_1 = (CHAR)1
        RTL_CORRELATION_VECTOR_VERSION_2 = (CHAR)2
        RTL_CORRELATION_VECTOR_VERSION_CURRENT = RTL_CORRELATION_VECTOR_VERSION_2
        RTL_CORRELATION_VECTOR_V1_PREFIX_LENGTH = 16
        RTL_CORRELATION_VECTOR_V1_LENGTH = 64
        RTL_CORRELATION_VECTOR_V2_PREFIX_LENGTH = 22
        RTL_CORRELATION_VECTOR_V2_LENGTH = 128
        class CORRELATION_VECTOR(ctypes.Structure):
            pass
        CORRELATION_VECTOR._fields_ = [
            ('Version', CHAR),
            ('Vector', CHAR * RTL_CORRELATION_VECTOR_STRING_LENGTH),
        ]




def TraceLoggingCORRELATION_VECTOR(cv):
    return TraceLoggingString(cv.Vector, "__TlgCV__")
    # END IF   NTDDI_VERSION >= NTDDI_RS2

    if (NTDDI_VERSION >= NTDDI_WIN10_RS4):
        class _CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG(ctypes.Structure):
            pass
        _CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG._fields_ = [
            ('Size', ULONG), # Size of the structure in bytes
            ('TriggerId', PCWSTR), # Guid used to identify background task to trigger
        ]


        CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG = _CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG
        PCUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG = POINTER(_CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG)


        if not defined(MIDL_PASS):
            pass
        # END IF   not defined(MIDL_PASS)
    # END IF   NTDDI_VERSION >= NTDDI_WIN10_RS4
    DEVICE_TYPE = ULONG
    FILE_DEVICE_BEEP = 0x00000001
    FILE_DEVICE_CD_ROM = 0x00000002
    FILE_DEVICE_CD_ROM_FILE_SYSTEM = 0x00000003
    FILE_DEVICE_CONTROLLER = 0x00000004
    FILE_DEVICE_DATALINK = 0x00000005
    FILE_DEVICE_DFS = 0x00000006
    FILE_DEVICE_DISK = 0x00000007
    FILE_DEVICE_DISK_FILE_SYSTEM = 0x00000008
    FILE_DEVICE_FILE_SYSTEM = 0x00000009
    FILE_DEVICE_INPORT_PORT = 0x0000000A
    FILE_DEVICE_KEYBOARD = 0x0000000B
    FILE_DEVICE_MAILSLOT = 0x0000000C
    FILE_DEVICE_MIDI_IN = 0x0000000D
    FILE_DEVICE_MIDI_OUT = 0x0000000E
    FILE_DEVICE_MOUSE = 0x0000000F
    FILE_DEVICE_MULTI_UNC_PROVIDER = 0x00000010
    FILE_DEVICE_NAMED_PIPE = 0x00000011
    FILE_DEVICE_NETWORK = 0x00000012
    FILE_DEVICE_NETWORK_BROWSER = 0x00000013
    FILE_DEVICE_NETWORK_FILE_SYSTEM = 0x00000014
    FILE_DEVICE_NULL = 0x00000015
    FILE_DEVICE_PARALLEL_PORT = 0x00000016
    FILE_DEVICE_PHYSICAL_NETCARD = 0x00000017
    FILE_DEVICE_PRINTER = 0x00000018
    FILE_DEVICE_SCANNER = 0x00000019
    FILE_DEVICE_SERIAL_MOUSE_PORT = 0x0000001A
    FILE_DEVICE_SERIAL_PORT = 0x0000001B
    FILE_DEVICE_SCREEN = 0x0000001C
    FILE_DEVICE_SOUND = 0x0000001D
    FILE_DEVICE_STREAMS = 0x0000001E
    FILE_DEVICE_TAPE = 0x0000001F
    FILE_DEVICE_TAPE_FILE_SYSTEM = 0x00000020
    FILE_DEVICE_TRANSPORT = 0x00000021
    FILE_DEVICE_UNKNOWN = 0x00000022
    FILE_DEVICE_VIDEO = 0x00000023
    FILE_DEVICE_VIRTUAL_DISK = 0x00000024
    FILE_DEVICE_WAVE_IN = 0x00000025
    FILE_DEVICE_WAVE_OUT = 0x00000026
    FILE_DEVICE_8042_PORT = 0x00000027
    FILE_DEVICE_NETWORK_REDIRECTOR = 0x00000028
    FILE_DEVICE_BATTERY = 0x00000029
    FILE_DEVICE_BUS_EXTENDER = 0x0000002A
    FILE_DEVICE_MODEM = 0x0000002B
    FILE_DEVICE_VDM = 0x0000002C
    FILE_DEVICE_MASS_STORAGE = 0x0000002D
    FILE_DEVICE_SMB = 0x0000002E
    FILE_DEVICE_KS = 0x0000002F
    FILE_DEVICE_CHANGER = 0x00000030
    FILE_DEVICE_SMARTCARD = 0x00000031
    FILE_DEVICE_ACPI = 0x00000032
    FILE_DEVICE_DVD = 0x00000033
    FILE_DEVICE_FULLSCREEN_VIDEO = 0x00000034
    FILE_DEVICE_DFS_FILE_SYSTEM = 0x00000035
    FILE_DEVICE_DFS_VOLUME = 0x00000036
    FILE_DEVICE_SERENUM = 0x00000037
    FILE_DEVICE_TERMSRV = 0x00000038
    FILE_DEVICE_KSEC = 0x00000039
    FILE_DEVICE_FIPS = 0x0000003A
    FILE_DEVICE_INFINIBAND = 0x0000003B
    FILE_DEVICE_VMBUS = 0x0000003E
    FILE_DEVICE_CRYPT_PROVIDER = 0x0000003F
    FILE_DEVICE_WPD = 0x00000040
    FILE_DEVICE_BLUETOOTH = 0x00000041
    FILE_DEVICE_MT_COMPOSITE = 0x00000042
    FILE_DEVICE_MT_TRANSPORT = 0x00000043
    FILE_DEVICE_BIOMETRIC = 0x00000044
    FILE_DEVICE_PMI = 0x00000045
    FILE_DEVICE_EHSTOR = 0x00000046
    FILE_DEVICE_DEVAPI = 0x00000047
    FILE_DEVICE_GPIO = 0x00000048
    FILE_DEVICE_USBEX = 0x00000049
    FILE_DEVICE_CONSOLE = 0x00000050
    FILE_DEVICE_NFP = 0x00000051
    FILE_DEVICE_SYSENV = 0x00000052
    FILE_DEVICE_VIRTUAL_BLOCK = 0x00000053
    FILE_DEVICE_POINT_OF_SERVICE = 0x00000054
    FILE_DEVICE_STORAGE_REPLICATION = 0x00000055
    FILE_DEVICE_TRUST_ENV = 0x00000056
    FILE_DEVICE_UCM = 0x00000057
    FILE_DEVICE_UCMTCPCI = 0x00000058
    FILE_DEVICE_PERSISTENT_MEMORY = 0x00000059
    FILE_DEVICE_NVDIMM = 0x0000005A
    FILE_DEVICE_HOLOGRAPHIC = 0x0000005B
    FILE_DEVICE_SDFXHCI = 0x0000005C


def CTL_CODE(DeviceType, Function, Method, Access):
    return (DeviceType << 16) | (Access << 14) | (Function << 2) | Method


def DEVICE_TYPE_FROM_CTL_CODE(ctrlCode):
    return ((ULONG(ctrlCode & 0xFFFF0000)) >> 16)


def METHOD_FROM_CTL_CODE(ctrlCode):
    return ULONG(ctrlCode & 3)
    METHOD_BUFFERED = 0
    METHOD_IN_DIRECT = 1
    METHOD_OUT_DIRECT = 2
    METHOD_NEITHER = 3
    METHOD_DIRECT_TO_HARDWARE = METHOD_IN_DIRECT
    METHOD_DIRECT_FROM_HARDWARE = METHOD_OUT_DIRECT
    FILE_ANY_ACCESS = 0
    FILE_SPECIAL_ACCESS = FILE_ANY_ACCESS
    FILE_READ_ACCESS = 0x0001
    FILE_WRITE_ACCESS = 0x0002

    if (NTDDI_VERSION >= NTDDI_WIN7):
        FILE_CHARACTERISTICS_EXPECT_ORDERLY_REMOVAL_EX = 0x00004000
        FILE_CHARACTERISTICS_EXPECT_SURPRISE_REMOVAL_EX = 0x00008000
        FILE_CHARACTERISTICS_REMOVAL_POLICY_MASK_EX = (
    FILE_CHARACTERISTICS_EXPECT_ORDERLY_REMOVAL_EX  |
     FILE_CHARACTERISTICS_EXPECT_SURPRISE_REMOVAL_EX
)
        FILE_CHARACTERISTICS_EXPECT_ORDERLY_REMOVAL_DEPRECATED = 0x00000200
        FILE_CHARACTERISTICS_EXPECT_SURPRISE_REMOVAL_DEPRECATED = 0x00000300
        FILE_CHARACTERISTICS_REMOVAL_POLICY_MASK_DEPRECATED = 0x00000300
else:
        FILE_CHARACTERISTICS_EXPECT_ORDERLY_REMOVAL = 0x00000200
        FILE_CHARACTERISTICS_EXPECT_SURPRISE_REMOVAL = 0x00000300
        FILE_CHARACTERISTICS_REMOVAL_POLICY_MASK = 0x00000300
        FILE_CHARACTERISTICS_EXPECT_ORDERLY_REMOVAL_EX = (
    FILE_CHARACTERISTICS_EXPECT_ORDERLY_REMOVAL
)
        FILE_CHARACTERISTICS_EXPECT_SURPRISE_REMOVAL_EX = (
    FILE_CHARACTERISTICS_EXPECT_SURPRISE_REMOVAL
)
        FILE_CHARACTERISTICS_REMOVAL_POLICY_MASK_EX = (
    FILE_CHARACTERISTICS_REMOVAL_POLICY_MASK
)
    # END IF
    FILE_CHARACTERISTICS_PROPAGATED = (
    FILE_REMOVABLE_MEDIA  |
     FILE_READ_ONLY_DEVICE  |
     FILE_FLOPPY_DISKETTE  |
     FILE_WRITE_ONCE_MEDIA  |
     FILE_DEVICE_SECURE_OPEN  |
     FILE_CHARACTERISTIC_CSV  |
     FILE_PORTABLE_DEVICE
)
    class _FILE_ALIGNMENT_INFORMATION(ctypes.Structure):
        pass
    _FILE_ALIGNMENT_INFORMATION._fields_ = [
        ('AlignmentRequirement', ULONG),
    ]


    FILE_ALIGNMENT_INFORMATION = _FILE_ALIGNMENT_INFORMATION
    PFILE_ALIGNMENT_INFORMATION = POINTER(_FILE_ALIGNMENT_INFORMATION)


    class _FILE_NAME_INFORMATION(ctypes.Structure):
        pass
    _FILE_NAME_INFORMATION._fields_ = [
        ('FileNameLength', ULONG),
        ('FileName', WCHAR * 1),
    ]


    FILE_NAME_INFORMATION = _FILE_NAME_INFORMATION
    PFILE_NAME_INFORMATION = POINTER(_FILE_NAME_INFORMATION)


    class _FILE_ATTRIBUTE_TAG_INFORMATION(ctypes.Structure):
        pass
    _FILE_ATTRIBUTE_TAG_INFORMATION._fields_ = [
        ('FileAttributes', ULONG),
        ('ReparseTag', ULONG),
    ]


    FILE_ATTRIBUTE_TAG_INFORMATION = _FILE_ATTRIBUTE_TAG_INFORMATION
    PFILE_ATTRIBUTE_TAG_INFORMATION = POINTER(_FILE_ATTRIBUTE_TAG_INFORMATION)


    class _FILE_DISPOSITION_INFORMATION(ctypes.Structure):
        pass
    _FILE_DISPOSITION_INFORMATION._fields_ = [
        ('DeleteFile', BOOLEAN),
    ]


    FILE_DISPOSITION_INFORMATION = _FILE_DISPOSITION_INFORMATION
    PFILE_DISPOSITION_INFORMATION = POINTER(_FILE_DISPOSITION_INFORMATION)



    if (_WIN32_WINNT >= _WIN32_WINNT_WIN10_RS1):
        FILE_DISPOSITION_DO_NOT_DELETE = 0x00000000
        FILE_DISPOSITION_DELETE = 0x00000001
        FILE_DISPOSITION_POSIX_SEMANTICS = 0x00000002
        FILE_DISPOSITION_FORCE_IMAGE_SECTION_CHECK = 0x00000004
        FILE_DISPOSITION_ON_CLOSE = 0x00000008
        class _FILE_DISPOSITION_INFORMATION_EX(ctypes.Structure):
            pass
        _FILE_DISPOSITION_INFORMATION_EX._fields_ = [
            ('Flags', ULONG),
        ]


        FILE_DISPOSITION_INFORMATION_EX = _FILE_DISPOSITION_INFORMATION_EX
        PFILE_DISPOSITION_INFORMATION_EX = POINTER(_FILE_DISPOSITION_INFORMATION_EX)


    # END IF
    class _FILE_END_OF_FILE_INFORMATION(ctypes.Structure):
        pass
    _FILE_END_OF_FILE_INFORMATION._fields_ = [
        ('EndOfFile', LARGE_INTEGER),
    ]


    FILE_END_OF_FILE_INFORMATION = _FILE_END_OF_FILE_INFORMATION
    PFILE_END_OF_FILE_INFORMATION = POINTER(_FILE_END_OF_FILE_INFORMATION)


    class _FILE_VALID_DATA_LENGTH_INFORMATION(ctypes.Structure):
        pass
    _FILE_VALID_DATA_LENGTH_INFORMATION._fields_ = [
        ('ValidDataLength', LARGE_INTEGER),
    ]


    FILE_VALID_DATA_LENGTH_INFORMATION = _FILE_VALID_DATA_LENGTH_INFORMATION
    PFILE_VALID_DATA_LENGTH_INFORMATION = POINTER(_FILE_VALID_DATA_LENGTH_INFORMATION)


    class _FILE_FS_LABEL_INFORMATION(ctypes.Structure):
        pass
    _FILE_FS_LABEL_INFORMATION._fields_ = [
        ('VolumeLabelLength', ULONG),
        ('VolumeLabel', WCHAR * 1),
    ]


    FILE_FS_LABEL_INFORMATION = _FILE_FS_LABEL_INFORMATION
    PFILE_FS_LABEL_INFORMATION = POINTER(_FILE_FS_LABEL_INFORMATION)


    class _FILE_FS_VOLUME_INFORMATION(ctypes.Structure):
        pass
    _FILE_FS_VOLUME_INFORMATION._fields_ = [
        ('VolumeCreationTime', LARGE_INTEGER),
        ('VolumeSerialNumber', ULONG),
        ('VolumeLabelLength', ULONG),
        ('SupportsObjects', BOOLEAN),
        ('VolumeLabel', WCHAR * 1),
    ]


    FILE_FS_VOLUME_INFORMATION = _FILE_FS_VOLUME_INFORMATION
    PFILE_FS_VOLUME_INFORMATION = POINTER(_FILE_FS_VOLUME_INFORMATION)


    class _FILE_FS_SIZE_INFORMATION(ctypes.Structure):
        pass
    _FILE_FS_SIZE_INFORMATION._fields_ = [
        ('TotalAllocationUnits', LARGE_INTEGER),
        ('AvailableAllocationUnits', LARGE_INTEGER),
        ('SectorsPerAllocationUnit', ULONG),
        ('BytesPerSector', ULONG),
    ]


    FILE_FS_SIZE_INFORMATION = _FILE_FS_SIZE_INFORMATION
    PFILE_FS_SIZE_INFORMATION = POINTER(_FILE_FS_SIZE_INFORMATION)


    class _FILE_FS_FULL_SIZE_INFORMATION(ctypes.Structure):
        pass
    _FILE_FS_FULL_SIZE_INFORMATION._fields_ = [
        ('TotalAllocationUnits', LARGE_INTEGER),
        ('CallerAvailableAllocationUnits', LARGE_INTEGER),
        ('ActualAvailableAllocationUnits', LARGE_INTEGER),
        ('SectorsPerAllocationUnit', ULONG),
        ('BytesPerSector', ULONG),
    ]


    FILE_FS_FULL_SIZE_INFORMATION = _FILE_FS_FULL_SIZE_INFORMATION
    PFILE_FS_FULL_SIZE_INFORMATION = POINTER(_FILE_FS_FULL_SIZE_INFORMATION)



    if (_WIN32_WINNT >= _WIN32_WINNT_WINTHRESHOLD):
        class _FILE_FS_METADATA_SIZE_INFORMATION(ctypes.Structure):
            pass
        _FILE_FS_METADATA_SIZE_INFORMATION._fields_ = [
            ('TotalMetadataAllocationUnits', LARGE_INTEGER),
            ('SectorsPerAllocationUnit', ULONG),
            ('BytesPerSector', ULONG),
        ]


        FILE_FS_METADATA_SIZE_INFORMATION = _FILE_FS_METADATA_SIZE_INFORMATION
        PFILE_FS_METADATA_SIZE_INFORMATION = POINTER(_FILE_FS_METADATA_SIZE_INFORMATION)


    # END IF
    SSINFO_FLAGS_ALIGNED_DEVICE = 0x00000001
    SSINFO_FLAGS_PARTITION_ALIGNED_ON_DEVICE = 0x00000002
    SSINFO_FLAGS_NO_SEEK_PENALTY = 0x00000004
    SSINFO_FLAGS_TRIM_ENABLED = 0x00000008
    SSINFO_FLAGS_BYTE_ADDRESSABLE = 0x00000010
    SSINFO_OFFSET_UNKNOWN = 0xFFFFFFFF
    class _FILE_FS_SECTOR_SIZE_INFORMATION(ctypes.Structure):
        pass
    _FILE_FS_SECTOR_SIZE_INFORMATION._fields_ = [
        ('LogicalBytesPerSector', ULONG),
        ('PhysicalBytesPerSectorForAtomicity', ULONG),
        ('PhysicalBytesPerSectorForPerformance', ULONG),
        ('FileSystemEffectivePhysicalBytesPerSectorForAtomicity', ULONG),
        ('Flags', ULONG),
        ('ByteOffsetForSectorAlignment', ULONG),
        ('ByteOffsetForPartitionAlignment', ULONG),
    ]


    FILE_FS_SECTOR_SIZE_INFORMATION = _FILE_FS_SECTOR_SIZE_INFORMATION
    PFILE_FS_SECTOR_SIZE_INFORMATION = POINTER(_FILE_FS_SECTOR_SIZE_INFORMATION)


    class _FILE_FS_OBJECTID_INFORMATION(ctypes.Structure):
        pass
    _FILE_FS_OBJECTID_INFORMATION._fields_ = [
        ('ObjectId', UCHAR * 16),
        ('ExtendedInfo', UCHAR * 48),
    ]


    FILE_FS_OBJECTID_INFORMATION = _FILE_FS_OBJECTID_INFORMATION
    PFILE_FS_OBJECTID_INFORMATION = POINTER(_FILE_FS_OBJECTID_INFORMATION)


    IOCTL_AVIO_ALLOCATE_STREAM = CTL_CODE(
    (FILE_DEVICE_AVIO,
    1,
    METHOD_BUFFERED,
    FILE_SPECIAL_ACCESS,
)
    IOCTL_AVIO_FREE_STREAM = CTL_CODE(
    (FILE_DEVICE_AVIO,
    2,
    METHOD_BUFFERED,
    FILE_SPECIAL_ACCESS,
)
    IOCTL_AVIO_MODIFY_STREAM = CTL_CODE(
    (FILE_DEVICE_AVIO,
    3,
    METHOD_BUFFERED,
    FILE_SPECIAL_ACCESS,
)


    class _BUS_DATA_TYPE(ENUM):
        ConfigurationSpaceUndefined = - 1
        Cmos = 0
        EisaConfiguration = 1
        Pos = 2
        CbusConfiguration = 3
        PCIConfiguration = 4
        VMEConfiguration = 5
        NuBusConfiguration = 6
        PCMCIAConfiguration = 7
        MPIConfiguration = 8
        MPSAConfiguration = 9
        PNPISAConfiguration = 10
        SgiInternalConfiguration = 11
        MaximumBusDataType = 12


    BUS_DATA_TYPE = _BUS_DATA_TYPE
    PBUS_DATA_TYPE = POINTER(_BUS_DATA_TYPE)
    class _KEY_NAME_INFORMATION(ctypes.Structure):
        pass
    _KEY_NAME_INFORMATION._fields_ = [
        ('NameLength', ULONG),
        ('Name', WCHAR * 1), # Variable length string
    ]


    KEY_NAME_INFORMATION = _KEY_NAME_INFORMATION
    PKEY_NAME_INFORMATION = POINTER(_KEY_NAME_INFORMATION)


    class _KEY_CACHED_INFORMATION(ctypes.Structure):
        pass
    _KEY_CACHED_INFORMATION._fields_ = [
        ('LastWriteTime', LARGE_INTEGER),
        ('TitleIndex', ULONG),
        ('SubKeys', ULONG),
        ('MaxNameLen', ULONG),
        ('Values', ULONG),
        ('MaxValueNameLen', ULONG),
        ('MaxValueDataLen', ULONG),
        ('NameLength', ULONG),
    ]


    KEY_CACHED_INFORMATION = _KEY_CACHED_INFORMATION
    PKEY_CACHED_INFORMATION = POINTER(_KEY_CACHED_INFORMATION)


    class _KEY_VIRTUALIZATION_INFORMATION(ctypes.Structure):
        pass
    _KEY_VIRTUALIZATION_INFORMATION._fields_ = [

        # Tells whether the key is part of the virtualization namespace scope
        # (only HKLM\Software for now)
        ('VirtualizationCandidate : 1', ULONG),

        # Tells whether virtualization is enabled on this key. Can be 1 only
        # if above flag is 1.
        ('VirtualizationEnabled   : 1', ULONG),

        # Tells if the key is a virtual key. Can be 1 only if above 2 are 0.
        # Valid only on the virtual store key handles.
        ('VirtualTarget           : 1', ULONG),

        # Tells if the key is a part of the virtual sore path. Valid only on
        # the virtual store key handles.
        ('VirtualStore            : 1', ULONG),

        # Tells if the key has ever been virtualized, Can be 1 only if
        # VirtualizationCandidate is 1
        ('VirtualSource           : 1', ULONG),
        ('Reserved                : 27', ULONG),
    ]


    KEY_VIRTUALIZATION_INFORMATION = _KEY_VIRTUALIZATION_INFORMATION
    PKEY_VIRTUALIZATION_INFORMATION = POINTER(_KEY_VIRTUALIZATION_INFORMATION)


    class _KEY_LAYER_INFORMATION(ctypes.Structure):
        pass
    _KEY_LAYER_INFORMATION._fields_ = [
        ('IsTombstone      : 1', ULONG),
        ('IsSupersedeLocal : 1', ULONG),
        ('IsSupersedeTree  : 1', ULONG),
        ('ClassIsInherited : 1', ULONG),
        ('Reserved         : 28', ULONG),
    ]


    KEY_LAYER_INFORMATION = _KEY_LAYER_INFORMATION
    PKEY_LAYER_INFORMATION = POINTER(_KEY_LAYER_INFORMATION)


    class _EXCEPTION_REGISTRATION_RECORD(ctypes.Structure):
        pass
    _EXCEPTION_REGISTRATION_RECORD._fields_ = [
        ('Next', POINTER(_EXCEPTION_REGISTRATION_RECORD)),
        ('Handler', PEXCEPTION_ROUTINE),
    ]


    EXCEPTION_REGISTRATION_RECORD = _EXCEPTION_REGISTRATION_RECORD


    Next = POINTER(_EXCEPTION_REGISTRATION_RECORD)


    class _NT_TIB(ctypes.Structure):
        pass
        _Union_2._fields_ = [
            ('FiberData', PVOID),
            ('Version', ULONG),
        ]


        _NT_TIB._Union_2 = _Union_2
    _NT_TIB._anonymous_ = (
        '_Union_2',
    )
    _NT_TIB._fields_ = [
        ('ExceptionList', POINTER(_EXCEPTION_REGISTRATION_RECORD)),
        ('StackBase', PVOID),
        ('StackLimit', PVOID),
        ('SubSystemTib', PVOID),
            ('_Union_2', _NT_TIB._Union_2),
            ('FiberData', PVOID),
        ('ArbitraryUserPointer', PVOID),
        ('Self', POINTER(_NT_TIB)),
    ]


    NT_TIB = _NT_TIB


    ExceptionList = POINTER(_EXCEPTION_REGISTRATION_RECORD)


    if defined(_MSC_EXTENSIONS):
        ._fields_ = [
            ('FiberData', PVOID),
            ('Version', ULONG),
        ]


else:
        pass
    # END IF
    Self = POINTER(_NT_TIB)


    class _NT_TIB32(ctypes.Structure):
        pass
        _Union_3._fields_ = [
            ('FiberData', ULONG),
            ('Version', ULONG),
        ]


        _NT_TIB32._Union_3 = _Union_3
    _NT_TIB32._anonymous_ = (
        '_Union_3',
    )
    _NT_TIB32._fields_ = [
        ('ExceptionList', ULONG),
        ('StackBase', ULONG),
        ('StackLimit', ULONG),
        ('SubSystemTib', ULONG),
            ('_Union_3', _NT_TIB32._Union_3),
            ('FiberData', ULONG),
        ('ArbitraryUserPointer', ULONG),
        ('Self', ULONG),
    ]


    NT_TIB32 = _NT_TIB32
    PNT_TIB32 = POINTER(_NT_TIB32)


    if defined(_MSC_EXTENSIONS):
        ._fields_ = [
            ('FiberData', ULONG),
            ('Version', ULONG),
        ]


else:
        pass
    # END IF
    class _NT_TIB64(ctypes.Structure):
        pass
        _Union_4._fields_ = [
            ('FiberData', ULONG64),
            ('Version', ULONG),
        ]


        _NT_TIB64._Union_4 = _Union_4
    _NT_TIB64._anonymous_ = (
        '_Union_4',
    )
    _NT_TIB64._fields_ = [
        ('ExceptionList', ULONG64),
        ('StackBase', ULONG64),
        ('StackLimit', ULONG64),
        ('SubSystemTib', ULONG64),
            ('_Union_4', _NT_TIB64._Union_4),
            ('FiberData', ULONG64),
        ('ArbitraryUserPointer', ULONG64),
        ('Self', ULONG64),
    ]


    NT_TIB64 = _NT_TIB64
    PNT_TIB64 = POINTER(_NT_TIB64)


    if defined(_MSC_EXTENSIONS):
        ._fields_ = [
            ('FiberData', ULONG64),
            ('Version', ULONG),
        ]


else:
        pass
    # END IF
    class _PROCESSINFOCLASS(ENUM):
        ProcessBasicInformation = 0
        ProcessQuotaLimits = 1
        ProcessIoCounters = 2
        ProcessVmCounters = 3
        ProcessTimes = 4
        ProcessBasePriority = 5
        ProcessRaisePriority = 6
        ProcessDebugPort = 7
        ProcessExceptionPort = 8
        ProcessAccessToken = 9
        ProcessLdtInformation = 10
        ProcessLdtSize = 11
        ProcessDefaultHardErrorMode = 12
        ProcessIoPortHandlers = 13
        ProcessPooledUsageAndLimits = 14
        ProcessWorkingSetWatch = 15
        ProcessUserModeIOPL = 16
        ProcessEnableAlignmentFaultFixup = 17
        ProcessPriorityClass = 18
        ProcessWx86Information = 19
        ProcessHandleCount = 20
        ProcessAffinityMask = 21
        ProcessPriorityBoost = 22
        ProcessDeviceMap = 23
        ProcessSessionInformation = 24
        ProcessForegroundInformation = 25
        ProcessWow64Information = 26
        ProcessImageFileName = 27
        ProcessLUIDDeviceMapsEnabled = 28
        ProcessBreakOnTermination = 29
        ProcessDebugObjectHandle = 30
        ProcessDebugFlags = 31
        ProcessHandleTracing = 32
        ProcessIoPriority = 33
        ProcessExecuteFlags = 34
        ProcessTlsInformation = 35
        ProcessCookie = 36
        ProcessImageInformation = 37
        ProcessCycleTime = 38
        ProcessPagePriority = 39
        ProcessInstrumentationCallback = 40
        ProcessThreadStackAllocation = 41
        ProcessWorkingSetWatchEx = 42
        ProcessImageFileNameWin32 = 43
        ProcessImageFileMapping = 44
        ProcessAffinityUpdateMode = 45
        ProcessMemoryAllocationMode = 46
        ProcessGroupInformation = 47
        ProcessTokenVirtualizationEnabled = 48
        ProcessOwnerInformation = 49
        ProcessWindowInformation = 50
        ProcessHandleInformation = 51
        ProcessMitigationPolicy = 52
        ProcessDynamicFunctionTableInformation = 53
        ProcessHandleCheckingMode = 54
        ProcessKeepAliveCount = 55
        ProcessRevokeFileHandles = 56
        ProcessWorkingSetControl = 57
        ProcessHandleTable = 58
        ProcessCheckStackExtentsMode = 59
        ProcessCommandLineInformation = 60
        ProcessProtectionInformation = 61
        ProcessMemoryExhaustion = 62
        ProcessFaultInformation = 63
        ProcessTelemetryIdInformation = 64
        ProcessCommitReleaseInformation = 65
        ProcessReserved1Information = 66
        ProcessReserved2Information = 67
        ProcessSubsystemProcess = 68
        ProcessInPrivate = 70
        ProcessRaiseUMExceptionOnInvalidHandleClose = 71
        ProcessSubsystemInformation = 75
        ProcessWin32kSyscallFilterInformation = 79
        ProcessEnergyTrackingState = 82
        MaxProcessInfoClass = 83


    PROCESSINFOCLASS = _PROCESSINFOCLASS
    class _THREADINFOCLASS(ENUM):
        ThreadBasicInformation = 0
        ThreadTimes = 1
        ThreadPriority = 2
        ThreadBasePriority = 3
        ThreadAffinityMask = 4
        ThreadImpersonationToken = 5
        ThreadDescriptorTableEntry = 6
        ThreadEnableAlignmentFaultFixup = 7
        ThreadEventPair_Reusable = 8
        ThreadQuerySetWin32StartAddress = 9
        ThreadZeroTlsCell = 10
        ThreadPerformanceCount = 11
        ThreadAmILastThread = 12
        ThreadIdealProcessor = 13
        ThreadPriorityBoost = 14
        ThreadSetTlsArrayAddress = 15
        ThreadIsIoPending = 16
        ThreadHideFromDebugger = 17
        ThreadBreakOnTermination = 18
        ThreadSwitchLegacyState = 19
        ThreadIsTerminated = 20
        ThreadLastSystemCall = 21
        ThreadIoPriority = 22
        ThreadCycleTime = 23
        ThreadPagePriority = 24
        ThreadActualBasePriority = 25
        ThreadTebInformation = 26
        ThreadCSwitchMon = 27
        ThreadCSwitchPmu = 28
        ThreadWow64Context = 29
        ThreadGroupInformation = 30
        ThreadUmsInformation = 31
        ThreadCounterProfiling = 32
        ThreadIdealProcessorEx = 33
        ThreadCpuAccountingInformation = 34
        ThreadSuspendCount = 35
        ThreadActualGroupAffinity = 41
        ThreadDynamicCodePolicyInfo = 42
        ThreadSubsystemInformation = 45
        MaxThreadInfoClass = 50


    THREADINFOCLASS = _THREADINFOCLASS
    THREAD_CSWITCH_PMU_DISABLE = FALSE
    THREAD_CSWITCH_PMU_ENABLE = TRUE
    MEMORY_PRIORITY_LOWEST = 0
    MEMORY_PRIORITY_VERY_LOW = 1
    MEMORY_PRIORITY_LOW = 2
    MEMORY_PRIORITY_MEDIUM = 3
    MEMORY_PRIORITY_BELOW_NORMAL = 4
    MEMORY_PRIORITY_NORMAL = 5
    class _PAGE_PRIORITY_INFORMATION(ctypes.Structure):
        pass
    _PAGE_PRIORITY_INFORMATION._fields_ = [
        ('PagePriority', ULONG),
    ]


    PAGE_PRIORITY_INFORMATION = _PAGE_PRIORITY_INFORMATION
    PPAGE_PRIORITY_INFORMATION = POINTER(_PAGE_PRIORITY_INFORMATION)


    class _PROCESS_WS_WATCH_INFORMATION(ctypes.Structure):
        pass
    _PROCESS_WS_WATCH_INFORMATION._fields_ = [
        ('FaultingPc', PVOID),
        ('FaultingVa', PVOID),
    ]


    PROCESS_WS_WATCH_INFORMATION = _PROCESS_WS_WATCH_INFORMATION
    PPROCESS_WS_WATCH_INFORMATION = POINTER(_PROCESS_WS_WATCH_INFORMATION)


    class _PROCESS_BASIC_INFORMATION(ctypes.Structure):
        pass
    _PROCESS_BASIC_INFORMATION._fields_ = [
        ('ExitStatus', NTSTATUS),
        ('PebBaseAddress', PPEB),
        ('AffinityMask', ULONG_PTR),
        ('BasePriority', KPRIORITY),
        ('UniqueProcessId', ULONG_PTR),
        ('InheritedFromUniqueProcessId', ULONG_PTR),
    ]


    PROCESS_BASIC_INFORMATION = _PROCESS_BASIC_INFORMATION
    PPROCESS_BASIC_INFORMATION = POINTER(_PROCESS_BASIC_INFORMATION)


    class _PROCESS_EXTENDED_BASIC_INFORMATION(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('IsProtectedProcess : 1', ULONG),
        ('IsWow64Process : 1', ULONG),
        ('IsProcessDeleting : 1', ULONG),
        ('IsCrossSessionCreate : 1', ULONG),
        ('IsFrozen : 1', ULONG),
        ('IsBackground : 1', ULONG),
        ('IsStronglyNamed : 1', ULONG),
        ('IsSecureProcess : 1', ULONG),
        ('IsSubsystemProcess : 1', ULONG),
        ('SpareBits : 23', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_EXTENDED_BASIC_INFORMATION.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_EXTENDED_BASIC_INFORMATION._fields_ = [
        ('Size', SIZE_T), # Ignored as input, written with structure size on output
        ('BasicInfo', PROCESS_BASIC_INFORMATION),
        ('DUMMYUNIONNAME', _PROCESS_EXTENDED_BASIC_INFORMATION.DUMMYUNIONNAME),
    ]


    PROCESS_EXTENDED_BASIC_INFORMATION = _PROCESS_EXTENDED_BASIC_INFORMATION
    PPROCESS_EXTENDED_BASIC_INFORMATION = POINTER(_PROCESS_EXTENDED_BASIC_INFORMATION)


    DUMMYSTRUCTNAME._fields_ = [
        ('IsProtectedProcess : 1', ULONG),
        ('IsWow64Process : 1', ULONG),
        ('IsProcessDeleting : 1', ULONG),
        ('IsCrossSessionCreate : 1', ULONG),
        ('IsFrozen : 1', ULONG),
        ('IsBackground : 1', ULONG),
        ('IsStronglyNamed : 1', ULONG),
        ('IsSecureProcess : 1', ULONG),
        ('IsSubsystemProcess : 1', ULONG),
        ('SpareBits : 23', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('IsProtectedProcess : 1', ULONG),
        ('IsWow64Process : 1', ULONG),
        ('IsProcessDeleting : 1', ULONG),
        ('IsCrossSessionCreate : 1', ULONG),
        ('IsFrozen : 1', ULONG),
        ('IsBackground : 1', ULONG),
        ('IsStronglyNamed : 1', ULONG),
        ('IsSecureProcess : 1', ULONG),
        ('IsSubsystemProcess : 1', ULONG),
        ('SpareBits : 23', ULONG),
    ]


    class _PROCESS_DEVICEMAP_INFORMATION(ctypes.Structure):
        pass
    Set._fields_ = [
        ('DirectoryHandle', HANDLE),
    ]


    DUMMYUNIONNAME.Set = Set
    Query._fields_ = [
        ('DriveMap', ULONG),
        ('DriveType', UCHAR * 32),
    ]


    DUMMYUNIONNAME.Query = Query
    DUMMYUNIONNAME._fields_ = [
        ('Set', DUMMYUNIONNAME.Set),
        ('Query', DUMMYUNIONNAME.Query),
    ]


    _PROCESS_DEVICEMAP_INFORMATION.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_DEVICEMAP_INFORMATION._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_DEVICEMAP_INFORMATION.DUMMYUNIONNAME),
    ]


    PROCESS_DEVICEMAP_INFORMATION = _PROCESS_DEVICEMAP_INFORMATION
    PPROCESS_DEVICEMAP_INFORMATION = POINTER(_PROCESS_DEVICEMAP_INFORMATION)


    Set._fields_ = [
        ('DirectoryHandle', HANDLE),
    ]


    DUMMYUNIONNAME.Set = Set
    Query._fields_ = [
        ('DriveMap', ULONG),
        ('DriveType', UCHAR * 32),
    ]


    DUMMYUNIONNAME.Query = Query
    DUMMYUNIONNAME._fields_ = [
        ('Set', DUMMYUNIONNAME.Set),
        ('Query', DUMMYUNIONNAME.Query),
    ]


    Set._fields_ = [
        ('DirectoryHandle', HANDLE),
    ]


    Query._fields_ = [
        ('DriveMap', ULONG),
        ('DriveType', UCHAR * 32),
    ]


    class _PROCESS_DEVICEMAP_INFORMATION_EX(ctypes.Structure):
        pass
    Set._fields_ = [
        ('DirectoryHandle', HANDLE),
    ]


    DUMMYUNIONNAME.Set = Set
    Query._fields_ = [
        ('DriveMap', ULONG),
        ('DriveType', UCHAR * 32),
    ]


    DUMMYUNIONNAME.Query = Query
    DUMMYUNIONNAME._fields_ = [
        ('Set', DUMMYUNIONNAME.Set),
        ('Query', DUMMYUNIONNAME.Query),
    ]


    _PROCESS_DEVICEMAP_INFORMATION_EX.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_DEVICEMAP_INFORMATION_EX._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_DEVICEMAP_INFORMATION_EX.DUMMYUNIONNAME),
        ('Flags', ULONG), # specifies that the query type
    ]


    PROCESS_DEVICEMAP_INFORMATION_EX = _PROCESS_DEVICEMAP_INFORMATION_EX
    PPROCESS_DEVICEMAP_INFORMATION_EX = POINTER(_PROCESS_DEVICEMAP_INFORMATION_EX)


    Set._fields_ = [
        ('DirectoryHandle', HANDLE),
    ]


    DUMMYUNIONNAME.Set = Set
    Query._fields_ = [
        ('DriveMap', ULONG),
        ('DriveType', UCHAR * 32),
    ]


    DUMMYUNIONNAME.Query = Query
    DUMMYUNIONNAME._fields_ = [
        ('Set', DUMMYUNIONNAME.Set),
        ('Query', DUMMYUNIONNAME.Query),
    ]


    Set._fields_ = [
        ('DirectoryHandle', HANDLE),
    ]


    Query._fields_ = [
        ('DriveMap', ULONG),
        ('DriveType', UCHAR * 32),
    ]


    PROCESS_LUID_DOSDEVICES_ONLY = 0x00000001
    class _PROCESS_SESSION_INFORMATION(ctypes.Structure):
        pass
    _PROCESS_SESSION_INFORMATION._fields_ = [
        ('SessionId', ULONG),
    ]


    PROCESS_SESSION_INFORMATION = _PROCESS_SESSION_INFORMATION
    PPROCESS_SESSION_INFORMATION = POINTER(_PROCESS_SESSION_INFORMATION)


    class _PROCESS_HANDLE_TRACING_ENABLE(ctypes.Structure):
        pass
    _PROCESS_HANDLE_TRACING_ENABLE._fields_ = [
        ('Flags', ULONG),
    ]


    PROCESS_HANDLE_TRACING_ENABLE = _PROCESS_HANDLE_TRACING_ENABLE
    PPROCESS_HANDLE_TRACING_ENABLE = POINTER(_PROCESS_HANDLE_TRACING_ENABLE)


    class _PROCESS_HANDLE_TRACING_ENABLE_EX(ctypes.Structure):
        pass
    _PROCESS_HANDLE_TRACING_ENABLE_EX._fields_ = [
        ('Flags', ULONG),
        ('TotalSlots', ULONG),
    ]


    PROCESS_HANDLE_TRACING_ENABLE_EX = _PROCESS_HANDLE_TRACING_ENABLE_EX
    PPROCESS_HANDLE_TRACING_ENABLE_EX = POINTER(_PROCESS_HANDLE_TRACING_ENABLE_EX)


    PROCESS_HANDLE_EXCEPTIONS_ENABLED = 0x00000001
    PROCESS_HANDLE_RAISE_UM_EXCEPTION_ON_INVALID_HANDLE_CLOSE_DISABLED = 0x00000000
    PROCESS_HANDLE_RAISE_UM_EXCEPTION_ON_INVALID_HANDLE_CLOSE_ENABLED = 0x00000001
    PROCESS_HANDLE_TRACING_MAX_STACKS = 16
    class _PROCESS_HANDLE_TRACING_ENTRY(ctypes.Structure):
        pass
    _PROCESS_HANDLE_TRACING_ENTRY._fields_ = [
        ('Handle', HANDLE),
        ('ClientId', CLIENT_ID),
        ('Type', ULONG),
        ('Stacks', PVOID * PROCESS_HANDLE_TRACING_MAX_STACKS),
    ]


    PROCESS_HANDLE_TRACING_ENTRY = _PROCESS_HANDLE_TRACING_ENTRY
    PPROCESS_HANDLE_TRACING_ENTRY = POINTER(_PROCESS_HANDLE_TRACING_ENTRY)


    class _PROCESS_HANDLE_TRACING_QUERY(ctypes.Structure):
        pass
    _PROCESS_HANDLE_TRACING_QUERY._fields_ = [
        ('Handle', HANDLE),
        ('TotalTraces', ULONG),
        ('HandleTrace', PROCESS_HANDLE_TRACING_ENTRY * 1),
    ]


    PROCESS_HANDLE_TRACING_QUERY = _PROCESS_HANDLE_TRACING_QUERY
    PPROCESS_HANDLE_TRACING_QUERY = POINTER(_PROCESS_HANDLE_TRACING_QUERY)


    class _QUOTA_LIMITS(ctypes.Structure):
        pass
    _QUOTA_LIMITS._fields_ = [
        ('PagedPoolLimit', SIZE_T),
        ('NonPagedPoolLimit', SIZE_T),
        ('MinimumWorkingSetSize', SIZE_T),
        ('MaximumWorkingSetSize', SIZE_T),
        ('PagefileLimit', SIZE_T),
        ('TimeLimit', LARGE_INTEGER),
    ]


    QUOTA_LIMITS = _QUOTA_LIMITS
    PQUOTA_LIMITS = POINTER(_QUOTA_LIMITS)


    QUOTA_LIMITS_HARDWS_MIN_ENABLE = 0x00000001
    QUOTA_LIMITS_HARDWS_MIN_DISABLE = 0x00000002
    QUOTA_LIMITS_HARDWS_MAX_ENABLE = 0x00000004
    QUOTA_LIMITS_HARDWS_MAX_DISABLE = 0x00000008
    QUOTA_LIMITS_USE_DEFAULT_LIMITS = 0x00000010
    class _RATE_QUOTA_LIMIT(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('RatePercent : 7', ULONG),
        ('Reserved0   : 25', ULONG),
    ]


    _RATE_QUOTA_LIMIT.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _RATE_QUOTA_LIMIT._fields_ = [
        ('RateData', ULONG),
        ('DUMMYSTRUCTNAME', _RATE_QUOTA_LIMIT.DUMMYSTRUCTNAME),
    ]


    RATE_QUOTA_LIMIT = _RATE_QUOTA_LIMIT
    PRATE_QUOTA_LIMIT = POINTER(_RATE_QUOTA_LIMIT)


    DUMMYSTRUCTNAME._fields_ = [
        ('RatePercent : 7', ULONG),
        ('Reserved0   : 25', ULONG),
    ]


    class _QUOTA_LIMITS_EX(ctypes.Structure):
        pass
    _QUOTA_LIMITS_EX._fields_ = [
        ('PagedPoolLimit', SIZE_T),
        ('NonPagedPoolLimit', SIZE_T),
        ('MinimumWorkingSetSize', SIZE_T),
        ('MaximumWorkingSetSize', SIZE_T),
        ('PagefileLimit', SIZE_T), # Limit expressed in pages
        ('TimeLimit', LARGE_INTEGER),
        ('WorkingSetLimit', SIZE_T), # Limit expressed in pages
        ('Reserved2', SIZE_T),
        ('Reserved3', SIZE_T),
        ('Reserved4', SIZE_T),
        ('Flags', ULONG),
        ('CpuRateLimit', RATE_QUOTA_LIMIT),
    ]


    QUOTA_LIMITS_EX = _QUOTA_LIMITS_EX
    PQUOTA_LIMITS_EX = POINTER(_QUOTA_LIMITS_EX)


    class _IO_COUNTERS(ctypes.Structure):
        pass
    _IO_COUNTERS._fields_ = [
        ('ReadOperationCount', ULONGLONG),
        ('WriteOperationCount', ULONGLONG),
        ('OtherOperationCount', ULONGLONG),
        ('ReadTransferCount', ULONGLONG),
        ('WriteTransferCount', ULONGLONG),
        ('OtherTransferCount', ULONGLONG),
    ]


    IO_COUNTERS = _IO_COUNTERS


    class _VM_COUNTERS(ctypes.Structure):
        pass
    _VM_COUNTERS._fields_ = [
        ('PeakVirtualSize', SIZE_T),
        ('VirtualSize', SIZE_T),
        ('PageFaultCount', ULONG),
        ('PeakWorkingSetSize', SIZE_T),
        ('WorkingSetSize', SIZE_T),
        ('QuotaPeakPagedPoolUsage', SIZE_T),
        ('QuotaPagedPoolUsage', SIZE_T),
        ('QuotaPeakNonPagedPoolUsage', SIZE_T),
        ('QuotaNonPagedPoolUsage', SIZE_T),
        ('PagefileUsage', SIZE_T),
        ('PeakPagefileUsage', SIZE_T),
    ]


    VM_COUNTERS = _VM_COUNTERS


    class _VM_COUNTERS_EX(ctypes.Structure):
        pass
    _VM_COUNTERS_EX._fields_ = [
        ('PeakVirtualSize', SIZE_T),
        ('VirtualSize', SIZE_T),
        ('PageFaultCount', ULONG),
        ('PeakWorkingSetSize', SIZE_T),
        ('WorkingSetSize', SIZE_T),
        ('QuotaPeakPagedPoolUsage', SIZE_T),
        ('QuotaPagedPoolUsage', SIZE_T),
        ('QuotaPeakNonPagedPoolUsage', SIZE_T),
        ('QuotaNonPagedPoolUsage', SIZE_T),
        ('PagefileUsage', SIZE_T),
        ('PeakPagefileUsage', SIZE_T),
        ('PrivateUsage', SIZE_T),
    ]


    VM_COUNTERS_EX = _VM_COUNTERS_EX


    class _VM_COUNTERS_EX2(ctypes.Structure):
        pass
    _VM_COUNTERS_EX2._fields_ = [
        ('CountersEx', VM_COUNTERS_EX),
        ('PrivateWorkingSetSize', SIZE_T),
        ('SharedCommitUsage', ULONGLONG),
    ]


    VM_COUNTERS_EX2 = _VM_COUNTERS_EX2
    PVM_COUNTERS_EX2 = POINTER(_VM_COUNTERS_EX2)


    MAX_HW_COUNTERS = 16
    THREAD_PROFILING_FLAG_DISPATCH = 0x00000001


    class _HARDWARE_COUNTER_TYPE(ENUM):
        PMCCounter = 1
        MaxHardwareCounterType = 2


    HARDWARE_COUNTER_TYPE = _HARDWARE_COUNTER_TYPE
    PHARDWARE_COUNTER_TYPE = POINTER(_HARDWARE_COUNTER_TYPE)
    class _HARDWARE_COUNTER(ctypes.Structure):
        pass
    _HARDWARE_COUNTER._fields_ = [
        ('Type', HARDWARE_COUNTER_TYPE),
        ('Reserved', ULONG),
        ('Index', ULONG64),
    ]


    HARDWARE_COUNTER = _HARDWARE_COUNTER
    PHARDWARE_COUNTER = POINTER(_HARDWARE_COUNTER)


    class _PROCESS_MITIGATION_POLICY(ENUM):
        ProcessDEPPolicy = 1
        ProcessASLRPolicy = 2
        ProcessDynamicCodePolicy = 3
        ProcessStrictHandleCheckPolicy = 4
        ProcessSystemCallDisablePolicy = 5
        ProcessMitigationOptionsMask = 6
        ProcessExtensionPointDisablePolicy = 7
        ProcessControlFlowGuardPolicy = 8
        ProcessSignaturePolicy = 9
        ProcessFontDisablePolicy = 10
        ProcessImageLoadPolicy = 11
        ProcessSystemCallFilterPolicy = 12
        ProcessPayloadRestrictionPolicy = 13
        ProcessChildProcessPolicy = 14
        MaxProcessMitigationPolicy = 15


    PROCESS_MITIGATION_POLICY = _PROCESS_MITIGATION_POLICY
    PPROCESS_MITIGATION_POLICY = POINTER(_PROCESS_MITIGATION_POLICY)
    class _PROCESS_MITIGATION_ASLR_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('EnableBottomUpRandomization : 1', ULONG),
        ('EnableForceRelocateImages : 1', ULONG),
        ('EnableHighEntropy : 1', ULONG),
        ('DisallowStrippedImages : 1', ULONG),
        ('ReservedFlags : 28', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_ASLR_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_ASLR_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_ASLR_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_ASLR_POLICY = _PROCESS_MITIGATION_ASLR_POLICY
    PPROCESS_MITIGATION_ASLR_POLICY = POINTER(_PROCESS_MITIGATION_ASLR_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('EnableBottomUpRandomization : 1', ULONG),
        ('EnableForceRelocateImages : 1', ULONG),
        ('EnableHighEntropy : 1', ULONG),
        ('DisallowStrippedImages : 1', ULONG),
        ('ReservedFlags : 28', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('EnableBottomUpRandomization : 1', ULONG),
        ('EnableForceRelocateImages : 1', ULONG),
        ('EnableHighEntropy : 1', ULONG),
        ('DisallowStrippedImages : 1', ULONG),
        ('ReservedFlags : 28', ULONG),
    ]


    class _PROCESS_MITIGATION_DEP_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Enable : 1', ULONG),
        ('DisableAtlThunkEmulation : 1', ULONG),
        ('ReservedFlags : 30', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_DEP_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_DEP_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_DEP_POLICY.DUMMYUNIONNAME),
        ('Permanent', BOOLEAN),
    ]


    PROCESS_MITIGATION_DEP_POLICY = _PROCESS_MITIGATION_DEP_POLICY
    PPROCESS_MITIGATION_DEP_POLICY = POINTER(_PROCESS_MITIGATION_DEP_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('Enable : 1', ULONG),
        ('DisableAtlThunkEmulation : 1', ULONG),
        ('ReservedFlags : 30', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('Enable : 1', ULONG),
        ('DisableAtlThunkEmulation : 1', ULONG),
        ('ReservedFlags : 30', ULONG),
    ]


    class _PROCESS_MITIGATION_STRICT_HANDLE_CHECK_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('RaiseExceptionOnInvalidHandleReference : 1', ULONG),
        ('HandleExceptionsPermanentlyEnabled : 1', ULONG),
        ('ReservedFlags : 30', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_STRICT_HANDLE_CHECK_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_STRICT_HANDLE_CHECK_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_STRICT_HANDLE_CHECK_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_STRICT_HANDLE_CHECK_POLICY = _PROCESS_MITIGATION_STRICT_HANDLE_CHECK_POLICY
    PPROCESS_MITIGATION_STRICT_HANDLE_CHECK_POLICY = POINTER(_PROCESS_MITIGATION_STRICT_HANDLE_CHECK_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('RaiseExceptionOnInvalidHandleReference : 1', ULONG),
        ('HandleExceptionsPermanentlyEnabled : 1', ULONG),
        ('ReservedFlags : 30', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('RaiseExceptionOnInvalidHandleReference : 1', ULONG),
        ('HandleExceptionsPermanentlyEnabled : 1', ULONG),
        ('ReservedFlags : 30', ULONG),
    ]


    class _PROCESS_MITIGATION_SYSTEM_CALL_DISABLE_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('DisallowWin32kSystemCalls : 1', ULONG),
        ('AuditDisallowWin32kSystemCalls : 1', ULONG),
        ('ReservedFlags : 30', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_SYSTEM_CALL_DISABLE_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_SYSTEM_CALL_DISABLE_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_SYSTEM_CALL_DISABLE_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_SYSTEM_CALL_DISABLE_POLICY = _PROCESS_MITIGATION_SYSTEM_CALL_DISABLE_POLICY
    PPROCESS_MITIGATION_SYSTEM_CALL_DISABLE_POLICY = POINTER(_PROCESS_MITIGATION_SYSTEM_CALL_DISABLE_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('DisallowWin32kSystemCalls : 1', ULONG),
        ('AuditDisallowWin32kSystemCalls : 1', ULONG),
        ('ReservedFlags : 30', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('DisallowWin32kSystemCalls : 1', ULONG),
        ('AuditDisallowWin32kSystemCalls : 1', ULONG),
        ('ReservedFlags : 30', ULONG),
    ]


    class _PROCESS_MITIGATION_EXTENSION_POINT_DISABLE_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('DisableExtensionPoints : 1', ULONG),
        ('ReservedFlags : 31', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_EXTENSION_POINT_DISABLE_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_EXTENSION_POINT_DISABLE_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_EXTENSION_POINT_DISABLE_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_EXTENSION_POINT_DISABLE_POLICY = _PROCESS_MITIGATION_EXTENSION_POINT_DISABLE_POLICY
    PPROCESS_MITIGATION_EXTENSION_POINT_DISABLE_POLICY = POINTER(_PROCESS_MITIGATION_EXTENSION_POINT_DISABLE_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('DisableExtensionPoints : 1', ULONG),
        ('ReservedFlags : 31', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('DisableExtensionPoints : 1', ULONG),
        ('ReservedFlags : 31', ULONG),
    ]


    class _PROCESS_MITIGATION_DYNAMIC_CODE_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ProhibitDynamicCode : 1', ULONG),
        ('AllowThreadOptOut : 1', ULONG),
        ('AllowRemoteDowngrade : 1', ULONG),
        ('AuditProhibitDynamicCode : 1', ULONG),
        ('ReservedFlags : 28', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_DYNAMIC_CODE_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_DYNAMIC_CODE_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_DYNAMIC_CODE_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_DYNAMIC_CODE_POLICY = _PROCESS_MITIGATION_DYNAMIC_CODE_POLICY
    PPROCESS_MITIGATION_DYNAMIC_CODE_POLICY = POINTER(_PROCESS_MITIGATION_DYNAMIC_CODE_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('ProhibitDynamicCode : 1', ULONG),
        ('AllowThreadOptOut : 1', ULONG),
        ('AllowRemoteDowngrade : 1', ULONG),
        ('AuditProhibitDynamicCode : 1', ULONG),
        ('ReservedFlags : 28', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('ProhibitDynamicCode : 1', ULONG),
        ('AllowThreadOptOut : 1', ULONG),
        ('AllowRemoteDowngrade : 1', ULONG),
        ('AuditProhibitDynamicCode : 1', ULONG),
        ('ReservedFlags : 28', ULONG),
    ]


    class _PROCESS_MITIGATION_CONTROL_FLOW_GUARD_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('EnableControlFlowGuard : 1', ULONG),
        ('EnableExportSuppression : 1', ULONG),
        ('StrictMode : 1', ULONG),
        ('ReservedFlags : 29', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_CONTROL_FLOW_GUARD_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_CONTROL_FLOW_GUARD_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_CONTROL_FLOW_GUARD_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_CONTROL_FLOW_GUARD_POLICY = _PROCESS_MITIGATION_CONTROL_FLOW_GUARD_POLICY
    PPROCESS_MITIGATION_CONTROL_FLOW_GUARD_POLICY = POINTER(_PROCESS_MITIGATION_CONTROL_FLOW_GUARD_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('EnableControlFlowGuard : 1', ULONG),
        ('EnableExportSuppression : 1', ULONG),
        ('StrictMode : 1', ULONG),
        ('ReservedFlags : 29', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('EnableControlFlowGuard : 1', ULONG),
        ('EnableExportSuppression : 1', ULONG),
        ('StrictMode : 1', ULONG),
        ('ReservedFlags : 29', ULONG),
    ]


    class _PROCESS_MITIGATION_BINARY_SIGNATURE_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('MicrosoftSignedOnly : 1', ULONG),
        ('StoreSignedOnly : 1', ULONG),
        ('MitigationOptIn : 1', ULONG),
        ('AuditMicrosoftSignedOnly : 1', ULONG),
        ('AuditStoreSignedOnly : 1', ULONG),
        ('ReservedFlags : 27', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_BINARY_SIGNATURE_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_BINARY_SIGNATURE_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_BINARY_SIGNATURE_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_BINARY_SIGNATURE_POLICY = _PROCESS_MITIGATION_BINARY_SIGNATURE_POLICY
    PPROCESS_MITIGATION_BINARY_SIGNATURE_POLICY = POINTER(_PROCESS_MITIGATION_BINARY_SIGNATURE_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('MicrosoftSignedOnly : 1', ULONG),
        ('StoreSignedOnly : 1', ULONG),
        ('MitigationOptIn : 1', ULONG),
        ('AuditMicrosoftSignedOnly : 1', ULONG),
        ('AuditStoreSignedOnly : 1', ULONG),
        ('ReservedFlags : 27', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('MicrosoftSignedOnly : 1', ULONG),
        ('StoreSignedOnly : 1', ULONG),
        ('MitigationOptIn : 1', ULONG),
        ('AuditMicrosoftSignedOnly : 1', ULONG),
        ('AuditStoreSignedOnly : 1', ULONG),
        ('ReservedFlags : 27', ULONG),
    ]


    class _PROCESS_MITIGATION_FONT_DISABLE_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('DisableNonSystemFonts     : 1', ULONG),
        ('AuditNonSystemFontLoading : 1', ULONG),
        ('ReservedFlags             : 30', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_FONT_DISABLE_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_FONT_DISABLE_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_FONT_DISABLE_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_FONT_DISABLE_POLICY = _PROCESS_MITIGATION_FONT_DISABLE_POLICY
    PPROCESS_MITIGATION_FONT_DISABLE_POLICY = POINTER(_PROCESS_MITIGATION_FONT_DISABLE_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('DisableNonSystemFonts     : 1', ULONG),
        ('AuditNonSystemFontLoading : 1', ULONG),
        ('ReservedFlags             : 30', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('DisableNonSystemFonts     : 1', ULONG),
        ('AuditNonSystemFontLoading : 1', ULONG),
        ('ReservedFlags             : 30', ULONG),
    ]


    class _PROCESS_MITIGATION_IMAGE_LOAD_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('NoRemoteImages : 1', ULONG),
        ('NoLowMandatoryLabelImages : 1', ULONG),
        ('PreferSystem32Images : 1', ULONG),
        ('AuditNoRemoteImages : 1', ULONG),
        ('AuditNoLowMandatoryLabelImages : 1', ULONG),
        ('ReservedFlags : 27', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_IMAGE_LOAD_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_IMAGE_LOAD_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_IMAGE_LOAD_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_IMAGE_LOAD_POLICY = _PROCESS_MITIGATION_IMAGE_LOAD_POLICY
    PPROCESS_MITIGATION_IMAGE_LOAD_POLICY = POINTER(_PROCESS_MITIGATION_IMAGE_LOAD_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('NoRemoteImages : 1', ULONG),
        ('NoLowMandatoryLabelImages : 1', ULONG),
        ('PreferSystem32Images : 1', ULONG),
        ('AuditNoRemoteImages : 1', ULONG),
        ('AuditNoLowMandatoryLabelImages : 1', ULONG),
        ('ReservedFlags : 27', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('NoRemoteImages : 1', ULONG),
        ('NoLowMandatoryLabelImages : 1', ULONG),
        ('PreferSystem32Images : 1', ULONG),
        ('AuditNoRemoteImages : 1', ULONG),
        ('AuditNoLowMandatoryLabelImages : 1', ULONG),
        ('ReservedFlags : 27', ULONG),
    ]


    class _PROCESS_MITIGATION_SYSTEM_CALL_FILTER_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('FilterId: 4', ULONG),
        ('ReservedFlags : 28', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_SYSTEM_CALL_FILTER_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_SYSTEM_CALL_FILTER_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_SYSTEM_CALL_FILTER_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_SYSTEM_CALL_FILTER_POLICY = _PROCESS_MITIGATION_SYSTEM_CALL_FILTER_POLICY
    PPROCESS_MITIGATION_SYSTEM_CALL_FILTER_POLICY = POINTER(_PROCESS_MITIGATION_SYSTEM_CALL_FILTER_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('FilterId: 4', ULONG),
        ('ReservedFlags : 28', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('FilterId: 4', ULONG),
        ('ReservedFlags : 28', ULONG),
    ]


    class _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('EnableExportAddressFilter     : 1', ULONG),
        ('AuditExportAddressFilter      : 1', ULONG),
        ('EnableExportAddressFilterPlus : 1', ULONG),
        ('AuditExportAddressFilterPlus  : 1', ULONG),
        ('EnableImportAddressFilter     : 1', ULONG),
        ('AuditImportAddressFilter      : 1', ULONG),
        ('EnableRopStackPivot           : 1', ULONG),
        ('AuditRopStackPivot            : 1', ULONG),
        ('EnableRopCallerCheck          : 1', ULONG),
        ('AuditRopCallerCheck           : 1', ULONG),
        ('EnableRopSimExec              : 1', ULONG),
        ('AuditRopSimExec               : 1', ULONG),
        ('ReservedFlags                 : 20', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY = _PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY
    PPROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY = POINTER(_PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('EnableExportAddressFilter     : 1', ULONG),
        ('AuditExportAddressFilter      : 1', ULONG),
        ('EnableExportAddressFilterPlus : 1', ULONG),
        ('AuditExportAddressFilterPlus  : 1', ULONG),
        ('EnableImportAddressFilter     : 1', ULONG),
        ('AuditImportAddressFilter      : 1', ULONG),
        ('EnableRopStackPivot           : 1', ULONG),
        ('AuditRopStackPivot            : 1', ULONG),
        ('EnableRopCallerCheck          : 1', ULONG),
        ('AuditRopCallerCheck           : 1', ULONG),
        ('EnableRopSimExec              : 1', ULONG),
        ('AuditRopSimExec               : 1', ULONG),
        ('ReservedFlags                 : 20', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('EnableExportAddressFilter     : 1', ULONG),
        ('AuditExportAddressFilter      : 1', ULONG),
        ('EnableExportAddressFilterPlus : 1', ULONG),
        ('AuditExportAddressFilterPlus  : 1', ULONG),
        ('EnableImportAddressFilter     : 1', ULONG),
        ('AuditImportAddressFilter      : 1', ULONG),
        ('EnableRopStackPivot           : 1', ULONG),
        ('AuditRopStackPivot            : 1', ULONG),
        ('EnableRopCallerCheck          : 1', ULONG),
        ('AuditRopCallerCheck           : 1', ULONG),
        ('EnableRopSimExec              : 1', ULONG),
        ('AuditRopSimExec               : 1', ULONG),
        ('ReservedFlags                 : 20', ULONG),
    ]


    class _PROCESS_MITIGATION_CHILD_PROCESS_POLICY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('NoChildProcessCreation : 1', ULONG),
        ('AuditNoChildProcessCreation : 1', ULONG),
        ('AllowSecureProcessCreation : 1', ULONG),
        ('ReservedFlags : 29', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    _PROCESS_MITIGATION_CHILD_PROCESS_POLICY.DUMMYUNIONNAME = DUMMYUNIONNAME
    _PROCESS_MITIGATION_CHILD_PROCESS_POLICY._fields_ = [
        ('DUMMYUNIONNAME', _PROCESS_MITIGATION_CHILD_PROCESS_POLICY.DUMMYUNIONNAME),
    ]


    PROCESS_MITIGATION_CHILD_PROCESS_POLICY = _PROCESS_MITIGATION_CHILD_PROCESS_POLICY
    PPROCESS_MITIGATION_CHILD_PROCESS_POLICY = POINTER(_PROCESS_MITIGATION_CHILD_PROCESS_POLICY)


    DUMMYSTRUCTNAME._fields_ = [
        ('NoChildProcessCreation : 1', ULONG),
        ('AuditNoChildProcessCreation : 1', ULONG),
        ('AllowSecureProcessCreation : 1', ULONG),
        ('ReservedFlags : 29', ULONG),
    ]


    DUMMYUNIONNAME.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME._fields_ = [
        ('Flags', ULONG),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('NoChildProcessCreation : 1', ULONG),
        ('AuditNoChildProcessCreation : 1', ULONG),
        ('AllowSecureProcessCreation : 1', ULONG),
        ('ReservedFlags : 29', ULONG),
    ]


    class _PROCESS_KEEPALIVE_COUNT_INFORMATION(ctypes.Structure):
        pass
    _PROCESS_KEEPALIVE_COUNT_INFORMATION._fields_ = [
        ('WakeCount', ULONG),
        ('NoWakeCount', ULONG),
    ]


    PROCESS_KEEPALIVE_COUNT_INFORMATION = _PROCESS_KEEPALIVE_COUNT_INFORMATION
    PPROCESS_KEEPALIVE_COUNT_INFORMATION = POINTER(_PROCESS_KEEPALIVE_COUNT_INFORMATION)


    class _PROCESS_REVOKE_FILE_HANDLES_INFORMATION(ctypes.Structure):
        pass
    _PROCESS_REVOKE_FILE_HANDLES_INFORMATION._fields_ = [
        ('TargetDevicePath', UNICODE_STRING),
    ]


    PROCESS_REVOKE_FILE_HANDLES_INFORMATION = _PROCESS_REVOKE_FILE_HANDLES_INFORMATION
    PPROCESS_REVOKE_FILE_HANDLES_INFORMATION = POINTER(_PROCESS_REVOKE_FILE_HANDLES_INFORMATION)


    PROCESS_READWRITEVM_LOGGING_ENABLE_READVM = 0x01
    PROCESS_READWRITEVM_LOGGING_ENABLE_READVM_V = 1UL
    PROCESS_READWRITEVM_LOGGING_ENABLE_WRITEVM = 0x02
    PROCESS_READWRITEVM_LOGGING_ENABLE_WRITEVM_V = 2UL
    class _PROCESS_READWRITEVM_LOGGING_INFORMATION(ctypes.Union):
        pass
    _Struct_1._fields_ = [
        ('EnableReadVmLogging : 1', UCHAR),
        ('EnableWriteVmLogging : 1', UCHAR),
        ('Unused : 6', UCHAR),
    ]


    _PROCESS_READWRITEVM_LOGGING_INFORMATION._Struct_1 = _Struct_1
    _PROCESS_READWRITEVM_LOGGING_INFORMATION._anonymous_ = (
        '_Struct_1',
    )
    _PROCESS_READWRITEVM_LOGGING_INFORMATION._fields_ = [
        ('Flags', UCHAR),
        ('_Struct_1', _PROCESS_READWRITEVM_LOGGING_INFORMATION._Struct_1),
    ]


    PROCESS_READWRITEVM_LOGGING_INFORMATION = _PROCESS_READWRITEVM_LOGGING_INFORMATION
    PPROCESS_READWRITEVM_LOGGING_INFORMATION = POINTER(_PROCESS_READWRITEVM_LOGGING_INFORMATION)


    ._fields_ = [
        ('EnableReadVmLogging : 1', UCHAR),
        ('EnableWriteVmLogging : 1', UCHAR),
        ('Unused : 6', UCHAR),
    ]


    class _POOLED_USAGE_AND_LIMITS(ctypes.Structure):
        pass
    _POOLED_USAGE_AND_LIMITS._fields_ = [
        ('PeakPagedPoolUsage', SIZE_T),
        ('PagedPoolUsage', SIZE_T),
        ('PagedPoolLimit', SIZE_T),
        ('PeakNonPagedPoolUsage', SIZE_T),
        ('NonPagedPoolUsage', SIZE_T),
        ('NonPagedPoolLimit', SIZE_T),
        ('PeakPagefileUsage', SIZE_T),
        ('PagefileUsage', SIZE_T),
        ('PagefileLimit', SIZE_T),
    ]


    POOLED_USAGE_AND_LIMITS = _POOLED_USAGE_AND_LIMITS


    class _PROCESS_ACCESS_TOKEN(ctypes.Structure):
        pass
    _PROCESS_ACCESS_TOKEN._fields_ = [
        ('Token', HANDLE), # TOKEN_ASSIGN_PRIMARY access to this token is needed.
        ('Thread', HANDLE), # N.B. This field is unused.
    ]


    PROCESS_ACCESS_TOKEN = _PROCESS_ACCESS_TOKEN
    PPROCESS_ACCESS_TOKEN = POINTER(_PROCESS_ACCESS_TOKEN)


    PROCESS_EXCEPTION_PORT_ALL_STATE_BITS = 0x00000003
    PROCESS_EXCEPTION_PORT_ALL_STATE_FLAGS = (
    (ULONG_PTR)((1UL << PROCESS_EXCEPTION_PORT_ALL_STATE_BITS) - 1)
)
    class _PROCESS_EXCEPTION_PORT(ctypes.Structure):
        pass
    _PROCESS_EXCEPTION_PORT._fields_ = [
        ('HANDLE ExceptionPortHandle', _In_), # Handle to the exception port. No particular access required.
        ('ULONG StateFlags', _Inout_), # port in the kernel.
    ]


    PROCESS_EXCEPTION_PORT = _PROCESS_EXCEPTION_PORT
    PPROCESS_EXCEPTION_PORT = POINTER(_PROCESS_EXCEPTION_PORT)


    class _KERNEL_USER_TIMES(ctypes.Structure):
        pass
    _KERNEL_USER_TIMES._fields_ = [
        ('CreateTime', LARGE_INTEGER),
        ('ExitTime', LARGE_INTEGER),
        ('KernelTime', LARGE_INTEGER),
        ('UserTime', LARGE_INTEGER),
    ]


    KERNEL_USER_TIMES = _KERNEL_USER_TIMES




    class _SUBSYSTEM_INFORMATION_TYPE(ENUM):
        SubsystemInformationTypeWin32 = 0
        SubsystemInformationTypeWSL = 1
        MaxSubsystemInformationType = 2


    SUBSYSTEM_INFORMATION_TYPE = _SUBSYSTEM_INFORMATION_TYPE
    PSUBSYSTEM_INFORMATION_TYPE = POINTER(_SUBSYSTEM_INFORMATION_TYPE)
    POWER_THROTTLING_PROCESS_CURRENT_VERSION = 1
    POWER_THROTTLING_PROCESS_EXECUTION_SPEED = 0x1
    POWER_THROTTLING_PROCESS_DELAYTIMERS = 0x2
    POWER_THROTTLING_PROCESS_VALID_FLAGS = (
    (POWER_THROTTLING_PROCESS_EXECUTION_SPEED  |
     POWER_THROTTLING_PROCESS_DELAYTIMERS)
)
    class _POWER_THROTTLING_PROCESS_STATE(ctypes.Structure):
        pass
    _POWER_THROTTLING_PROCESS_STATE._fields_ = [
        ('Version', ULONG),
        ('ControlMask', ULONG),
        ('StateMask', ULONG),
    ]


    POWER_THROTTLING_PROCESS_STATE = _POWER_THROTTLING_PROCESS_STATE
    PPOWER_THROTTLING_PROCESS_STATE = POINTER(_POWER_THROTTLING_PROCESS_STATE)


    POWER_THROTTLING_THREAD_CURRENT_VERSION = 1
    POWER_THROTTLING_THREAD_EXECUTION_SPEED = 0x1
    POWER_THROTTLING_THREAD_VALID_FLAGS = POWER_THROTTLING_THREAD_EXECUTION_SPEED
    class _POWER_THROTTLING_THREAD_STATE(ctypes.Structure):
        pass
    _POWER_THROTTLING_THREAD_STATE._fields_ = [
        ('Version', ULONG),
        ('ControlMask', ULONG),
        ('StateMask', ULONG),
    ]


    POWER_THROTTLING_THREAD_STATE = _POWER_THROTTLING_THREAD_STATE
    PPOWER_THROTTLING_THREAD_STATE = POINTER(_POWER_THROTTLING_THREAD_STATE)


    NTKERNELAPI = DECLSPEC_IMPORT

        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
    if defined(_X86_):
        if defined(_NTDRIVER_) or defined(_NTDDK_) or defined(_NTIFS_):


def KeQueryTickCount(CurrentCount):
    return { KSYSTEM_TIME volatile *_TickCount = *PKSYSTEM_TIME *( & KeTickCount); for ;; { CurrentCount - >HighPart = _TickCount - >High1Time; CurrentCount - >LowPart = _TickCount - >LowPart; if (CurrentCount - >HighPart == _TickCount - >High2Time) break; YieldProcessor; } }
    else:
            pass
        # END IF   defined(_NTDRIVER_) or defined(_NTDDK_) or defined(_NTIFS_)
        PCR_MINOR_VERSION = 1
        PCR_MAJOR_VERSION = 1
        class _KPCR(ctypes.Structure):
            pass
        _Struct_3._fields_ = [
            ('Used_ExceptionList', POINTER(_EXCEPTION_REGISTRATION_RECORD)),
            ('Used_StackBase', PVOID),
            ('MxCsr', ULONG),
            ('TssCopy', PVOID),
            ('ContextSwitches', ULONG),
            ('SetMemberCopy', KAFFINITY),
            ('Used_Self', PVOID),
        ]


        _Struct_2._Struct_3 = _Struct_3
        _Struct_2._anonymous_ = (
            '_Struct_3',
        )
        _Struct_2._fields_ = [
            ('NtTib', NT_TIB),
            ('_Struct_3', _Struct_2._Struct_3),
        ]


        _KPCR._Struct_2 = _Struct_2
        _KPCR._anonymous_ = (
            '_Struct_2',
        )
        _KPCR._fields_ = [
            ('_Struct_2', _KPCR._Struct_2), # better cache locality.
            ('SelfPcr', POINTER(_KPCR)), # flat address of this PCR
            ('Prcb', POINTER(_KPRCB)), # pointer to Prcb
            ('Irql', KIRQL), # do not use 3 bytes after this as
            ('IRR', ULONG), # HALs assume they are zero.
            ('IrrActive', ULONG),
            ('IDR', ULONG),
            ('KdVersionBlock', PVOID),
            ('IDT', POINTER(_KIDTENTRY)),
            ('GDT', POINTER(_KGDTENTRY)),
            ('TSS', POINTER(_KTSS)),
            ('MajorVersion', USHORT),
            ('MinorVersion', USHORT),
            ('SetMember', KAFFINITY),
            ('StallScaleFactor', ULONG),
            ('SpareUnused', UCHAR),
            ('Number', UCHAR),
            ('Spare0', UCHAR),
            ('SecondLevelCacheAssociativity', UCHAR),
            ('VdmAlert', ULONG),
            ('KernelReserved', ULONG * 14), # For use by the kernel
            ('SecondLevelCacheSize', ULONG),
            ('HalReserved', ULONG * 16), # For use by Hal
        ]


        KPCR = _KPCR
        PKPCR = POINTER(_KPCR)


        _Struct_3._fields_ = [
            ('Used_ExceptionList', POINTER(_EXCEPTION_REGISTRATION_RECORD)),
            ('Used_StackBase', PVOID),
            ('MxCsr', ULONG),
            ('TssCopy', PVOID),
            ('ContextSwitches', ULONG),
            ('SetMemberCopy', KAFFINITY),
            ('Used_Self', PVOID),
        ]


        ._Struct_3 = _Struct_3
        ._anonymous_ = (
            '_Struct_3',
        )
        ._fields_ = [
            ('NtTib', NT_TIB),
            ('_Struct_3', ._Struct_3),
        ]


        ._fields_ = [
            ('Used_ExceptionList', POINTER(_EXCEPTION_REGISTRATION_RECORD)),
            ('Used_StackBase', PVOID),
            ('MxCsr', ULONG),
            ('TssCopy', PVOID),
            ('ContextSwitches', ULONG),
            ('SetMemberCopy', KAFFINITY),
            ('Used_Self', PVOID),
        ]


        Used_ExceptionList = POINTER(_EXCEPTION_REGISTRATION_RECORD)


        PCR = this


        Prcb = to


        IDT = POINTER(_KIDTENTRY)


        GDT = POINTER(_KGDTENTRY)


        TSS = POINTER()


        PDI_SHIFT = 21
        PPI_SHIFT = 30
        PTI_SHIFT = 12
        PTE_PER_PAGE = 512
        PDE_PER_PAGE = 512
        MM_HIGHEST_USER_ADDRESS = MmHighestUserAddress
        MM_SYSTEM_RANGE_START = MmSystemRangeStart

        if defined(_LOCAL_COPY_USER_PROBE_ADDRESS_):
            MM_USER_PROBE_ADDRESS = _LOCAL_COPY_USER_PROBE_ADDRESS_

            if defined(__CONVERGED_WIN32K_DRIVER__):
                pass
        else:
                pass
            # END IF
    else:
            MM_USER_PROBE_ADDRESS = MmUserProbeAddress
        # END IF
        MM_KSEG0_BASE = MM_SYSTEM_RANGE_START
        MM_SYSTEM_SPACE_END = 0xFFFFFFFF
        MM_LOWEST_USER_ADDRESS = (PVOID)0x10000


        class _INTERLOCKED_RESULT(ENUM):
            #~#~#~ ResultNegative = RESULT_NEGATIVE
            #~#~#~ ResultZero     = RESULT_ZERO
            #~#~#~ ResultPositive = RESULT_POSITIVE
            pass


        INTERLOCKED_RESULT = _INTERLOCKED_RESULT
        if not defined(MIDL_PASS) and defined(_M_IX86):
            pass
        # END IF   not defined(MIDL_PASS) and defined(_M_IX86)
    # END IF   defined(_X86_)
        if defined(IsNEC_98):
            pass
        # END IF
        if defined(IsNotNEC_98):
            pass
        # END IF
        if defined(SetNEC_98):
            pass
        # END IF
        if defined(SetNotNEC_98):
            pass
        # END IF
    if defined(_X86_):
        IsNEC_98 = SharedUserData - >AlternativeArchitecture == NEC98x86
        IsNotNEC_98 = SharedUserData - >AlternativeArchitecture != NEC98x86
        SetNEC_98 = SharedUserData - >AlternativeArchitecture = NEC98x86
        SetNotNEC_98 = SharedUserData - >AlternativeArchitecture = StandardDesign
    # END IF

    if defined(_AMD64_):
        PCR_MINOR_VERSION = 1
        PCR_MAJOR_VERSION = 1
        _Struct_5._fields_ = [
            ('GdtBase', POINTER(_KGDTENTRY64)),
            ('TssBase', POINTER(_KTSS64)),
            ('UserRsp', ULONG64),
            ('Self', POINTER(_KPCR)),
            ('CurrentPrcb', POINTER(_KPRCB)),
            ('LockArray', PKSPIN_LOCK_QUEUE),
            ('Used_Self', PVOID),
        ]


        _Struct_4._Struct_5 = _Struct_5
        _Struct_4._anonymous_ = (
            '_Struct_5',
        )
        _Struct_4._fields_ = [
            ('NtTib', NT_TIB),
            ('_Struct_5', _Struct_4._Struct_5),
        ]


        _KPCR._Struct_4 = _Struct_4
        _KPCR._anonymous_ = (
            '_Struct_4',
        )
        _KPCR._fields_ = [
            ('_Struct_4', _KPCR._Struct_4), # N.B. The offset to the PRCB in the PCR is fixed for all time.
            ('IdtBase', POINTER(_KIDTENTRY64)),
            ('Unused', ULONG64 * 2),
            ('Irql', KIRQL),
            ('SecondLevelCacheAssociativity', UCHAR),
            ('ObsoleteNumber', UCHAR),
            ('Fill0', UCHAR),
            ('Unused0', ULONG * 3),
            ('MajorVersion', USHORT),
            ('MinorVersion', USHORT),
            ('StallScaleFactor', ULONG),
            ('Unused1', PVOID * 3),
            ('KernelReserved', ULONG * 15),
            ('SecondLevelCacheSize', ULONG),
            ('HalReserved', ULONG * 16),
            ('Unused2', ULONG),
            ('KdVersionBlock', PVOID),
            ('Unused3', PVOID),
            ('PcrAlign1', ULONG * 24),
        ]


        KPCR = _KPCR
        PKPCR = POINTER(_KPCR)


        _Struct_5._fields_ = [
            ('GdtBase', POINTER(_KGDTENTRY64)),
            ('TssBase', POINTER(_KTSS64)),
            ('UserRsp', ULONG64),
            ('Self', POINTER(_KPCR)),
            ('CurrentPrcb', POINTER(_KPRCB)),
            ('LockArray', PKSPIN_LOCK_QUEUE),
            ('Used_Self', PVOID),
        ]


        ._Struct_5 = _Struct_5
        ._anonymous_ = (
            '_Struct_5',
        )
        ._fields_ = [
            ('NtTib', NT_TIB),
            ('_Struct_5', ._Struct_5),
        ]


        ._fields_ = [
            ('GdtBase', POINTER(_KGDTENTRY64)),
            ('TssBase', POINTER(_KTSS64)),
            ('UserRsp', ULONG64),
            ('Self', POINTER(_KPCR)),
            ('CurrentPrcb', POINTER(_KPRCB)),
            ('LockArray', PKSPIN_LOCK_QUEUE),
            ('Used_Self', PVOID),
        ]


        GdtBase = POINTER(_KGDTENTRY64)


        TssBase = POINTER(_KTSS64)


        Self = POINTER(_KPCR)


        CurrentPrcb = POINTER(_KPRCB)


        IdtBase = POINTER(_KIDTENTRY64)


        class _KEXCEPTION_FRAME(ctypes.Structure):
            pass
        _KEXCEPTION_FRAME._fields_ = [
            ('P1Home', ULONG64), # Home address for the parameter registers.
            ('P2Home', ULONG64),
            ('P3Home', ULONG64),
            ('P4Home', ULONG64),
            ('P5', ULONG64),
            ('Spare1', ULONG64),
            ('Xmm6', M128A), # Saved nonvolatile FLOATing registers.
            ('Xmm7', M128A),
            ('Xmm8', M128A),
            ('Xmm9', M128A),
            ('Xmm10', M128A),
            ('Xmm11', M128A),
            ('Xmm12', M128A),
            ('Xmm13', M128A),
            ('Xmm14', M128A),
            ('Xmm15', M128A),
            ('TrapFrame', ULONG64), # Kernel callout frame variables.
            ('OutputBuffer', ULONG64),
            ('OutputLength', ULONG64),
            ('Spare2', ULONG64),
            ('MxCsr', ULONG64), # interrupt.
            ('Rbp', ULONG64), # Saved nonvolatile register - not always saved.
            ('Rbx', ULONG64), # Saved nonvolatile registers.
            ('Rdi', ULONG64),
            ('Rsi', ULONG64),
            ('R12', ULONG64),
            ('R13', ULONG64),
            ('R14', ULONG64),
            ('R15', ULONG64),
            ('Return', ULONG64), # EFLAGS and return address.
        ]


        KEXCEPTION_FRAME = _KEXCEPTION_FRAME
        PKEXCEPTION_FRAME = POINTER(_KEXCEPTION_FRAME)


        class _KTRAP_FRAME(ctypes.Structure):
            pass
        _Union_5._fields_ = [
            ('GsBase', ULONG64),
            ('GsSwap', ULONG64),
        ]


        _KTRAP_FRAME._Union_5 = _Union_5
        _Union_6._fields_ = [
            ('FaultAddress', ULONG64),
            ('ContextRecord', ULONG64),
        ]


        _KTRAP_FRAME._Union_6 = _Union_6
        _Struct_6._fields_ = [
            ('DebugControl', ULONG64),
            ('LastBranchToRip', ULONG64),
            ('LastBranchFromRip', ULONG64),
            ('LastExceptionToRip', ULONG64),
            ('LastExceptionFromRip', ULONG64),
        ]


        _KTRAP_FRAME._Struct_6 = _Struct_6
        _Union_7._fields_ = [
            ('ErrorCode', ULONG64),
            ('ExceptionFrame', ULONG64),
        ]


        _KTRAP_FRAME._Union_7 = _Union_7
        _KTRAP_FRAME._anonymous_ = (
            '_Union_5',
            '_Union_6',
            '_Struct_6',
            '_Union_7',
        )
        _KTRAP_FRAME._fields_ = [
            ('P1Home', ULONG64), # Home address for the parameter registers.
            ('P2Home', ULONG64),
            ('P3Home', ULONG64),
            ('P4Home', ULONG64),
            ('P5', ULONG64),
            ('PreviousMode', KPROCESSOR_MODE), # (interrupts only).
            ('PreviousIrql', KIRQL),
            ('FaultIndicator', UCHAR), # Page fault load/store indicator.
            ('ExceptionActive', UCHAR), # 2 - service frame.
            ('MxCsr', ULONG), # Floating point state.
            ('Rax', ULONG64), # are not saved for system calls.
            ('Rcx', ULONG64),
            ('Rdx', ULONG64),
            ('R8', ULONG64),
            ('R9', ULONG64),
            ('R10', ULONG64),
            ('R11', ULONG64),
            ('_Union_5', _KTRAP_FRAME._Union_5), # GsSwap is only used if the previous mode was user.
            ('Xmm0', M128A), # are not saved for system calls.
            ('Xmm1', M128A),
            ('Xmm2', M128A),
            ('Xmm3', M128A),
            ('Xmm4', M128A),
            ('Xmm5', M128A),
            ('_Union_6', _KTRAP_FRAME._Union_6), # bypass.
            ('Dr0', ULONG64), # Debug registers.
            ('Dr1', ULONG64),
            ('Dr2', ULONG64),
            ('Dr3', ULONG64),
            ('Dr6', ULONG64),
            ('Dr7', ULONG64),
            ('_Struct_6', _KTRAP_FRAME._Struct_6), # Special debug registers.
            ('SegDs', USHORT), # Segment registers
            ('SegEs', USHORT),
            ('SegFs', USHORT),
            ('SegGs', USHORT),
            ('TrapFrame', ULONG64), # Previous trap frame address.
            ('Rbx', ULONG64), # saved in system service trap frames.
            ('Rdi', ULONG64),
            ('Rsi', ULONG64),
            ('Rbp', ULONG64), # pointer during trap processing and is saved in all trap frames.
            ('_Union_7', _KTRAP_FRAME._Union_7), # on the stack.
            ('Rip', ULONG64),
            ('SegCs', USHORT),
            ('Fill0', UCHAR),
            ('Logging', UCHAR),
            ('Fill1', USHORT * 2),
            ('EFlags', ULONG),
            ('Fill2', ULONG),
            ('Rsp', ULONG64),
            ('SegSs', USHORT),
            ('Fill3', USHORT),
            ('Fill4', ULONG),
        ]


        KTRAP_FRAME = _KTRAP_FRAME
        PKTRAP_FRAME = POINTER(_KTRAP_FRAME)


        ._fields_ = [
            ('GsBase', ULONG64),
            ('GsSwap', ULONG64),
        ]


        ._fields_ = [
            ('FaultAddress', ULONG64),
            ('ContextRecord', ULONG64),
        ]


        ._fields_ = [
            ('DebugControl', ULONG64),
            ('LastBranchToRip', ULONG64),
            ('LastBranchFromRip', ULONG64),
            ('LastExceptionToRip', ULONG64),
            ('LastExceptionFromRip', ULONG64),
        ]


        ._fields_ = [
            ('ErrorCode', ULONG64),
            ('ExceptionFrame', ULONG64),
        ]


        class _KUMS_CONTEXT_HEADER(ctypes.Structure):
            pass
        _Struct_8._fields_ = [
            ('Volatile : 1', ULONG64),
            ('Reserved : 63', ULONG64),
        ]


        _Struct_7._Struct_8 = _Struct_8
        _Struct_7._anonymous_ = (
            '_Struct_8',
        )
        _Struct_7._fields_ = [
            ('_Struct_8', _Struct_7._Struct_8),
            ('Flags', ULONG64),
        ]


        _KUMS_CONTEXT_HEADER._Struct_7 = _Struct_7
        _KUMS_CONTEXT_HEADER._anonymous_ = (
            '_Struct_7',
        )
        _KUMS_CONTEXT_HEADER._fields_ = [
            ('P1Home', ULONG64),
            ('P2Home', ULONG64),
            ('P3Home', ULONG64),
            ('P4Home', ULONG64),
            ('StackTop', PVOID),
            ('StackSize', ULONG64),
            ('RspOffset', ULONG64),
            ('Rip', ULONG64),
            ('FltSave', PXMM_SAVE_AREA32),
            ('_Struct_7', _KUMS_CONTEXT_HEADER._Struct_7),
            ('TrapFrame', PKTRAP_FRAME),
            ('ExceptionFrame', PKEXCEPTION_FRAME),
            ('SourceThread', POINTER(_KTHREAD)),
            ('Return', ULONG64),
        ]


        KUMS_CONTEXT_HEADER = _KUMS_CONTEXT_HEADER
        PKUMS_CONTEXT_HEADER = POINTER(_KUMS_CONTEXT_HEADER)


        KUMS_UCH_VOLATILE_BIT = 0
        KUMS_UCH_VOLATILE_MASK = 1ULL << KUMS_UCH_VOLATILE_BIT
        _Struct_8._fields_ = [
            ('Volatile : 1', ULONG64),
            ('Reserved : 63', ULONG64),
        ]


        ._Struct_8 = _Struct_8
        ._anonymous_ = (
            '_Struct_8',
        )
        ._fields_ = [
            ('_Struct_8', ._Struct_8),
            ('Flags', ULONG64),
        ]


        ._fields_ = [
            ('Volatile : 1', ULONG64),
            ('Reserved : 63', ULONG64),
        ]


        SourceThread = POINTER(_KTHREAD)


        MM_HIGHEST_USER_ADDRESS = MmHighestUserAddress
        MM_SYSTEM_RANGE_START = MmSystemRangeStart

        if defined(_LOCAL_COPY_USER_PROBE_ADDRESS_):
            MM_USER_PROBE_ADDRESS = _LOCAL_COPY_USER_PROBE_ADDRESS_

            if defined(__CONVERGED_WIN32K_DRIVER__):
                pass
        else:
                pass
            # END IF
    else:
            MM_USER_PROBE_ADDRESS = MmUserProbeAddress
        # END IF
        MM_LOWEST_USER_ADDRESS = (PVOID)(LONG_PTR)0x10000

            if PRAGMA_DEPRECATED_DDK:
                pass
            # END IF
        if defined(_M_AMD64) and not defined(RC_INVOKED)  and not defined(MIDL_PASS):
            RESULT_ZERO = 0
            RESULT_NEGATIVE = 1
            RESULT_POSITIVE = 2


            class _INTERLOCKED_RESULT(ENUM):
                #~#~#~ ResultNegative = RESULT_NEGATIVE
                #~#~#~ ResultZero = RESULT_ZERO
                #~#~#~ ResultPositive = RESULT_POSITIVE
                pass


            INTERLOCKED_RESULT = _INTERLOCKED_RESULT


def ExInterlockedDecrementLong(Addend, Lock):
    return _ExInterlockedDecrementLongAddend


def ExInterlockedIncrementLong(Addend, Lock):
    return _ExInterlockedIncrementLongAddend


def ExInterlockedExchangeULONG(Target, Value, Lock):
    return _ExInterlockedExchangeULONGTarget, Value
        # END IF   defined(_M_AMD64) and not defined(RC_INVOKED)  and not defined(MIDL_PASS)

            if (NTDDI_VERSION < NTDDI_WIN7) or not defined(NT_PROCESSOR_GROUPS):
                pass
            # END IF
        if not defined(MIDL_PASS) and defined(_M_AMD64):
            pass
        # END IF   not defined(MIDL_PASS) and defined(_M_AMD64)
    # END IF   defined(_AMD64_)
    if defined(_AMD64_) and not defined(MIDL_PASS):
        pass
    # END IF   defined(_AMD64_) and not defined(MIDL_PASS)
    if defined(_ARM_):
        if defined(_NTDRIVER_) or defined(_NTDDK_) or defined(_NTIFS_):


def KeQueryTickCount(CurrentCount):
    return { KSYSTEM_TIME volatile *_TickCount = *PKSYSTEM_TIME *( & KeTickCount); for ;; { CurrentCount - >HighPart = _TickCount - >High1Time; CurrentCount - >LowPart = _TickCount - >LowPart; if (CurrentCount - >HighPart == _TickCount - >High2Time) break; YieldProcessor; } }
    else:
            pass
        # END IF   defined(_NTDRIVER_) or defined(_NTDDK_) or defined(_NTIFS_)
        PCR_MINOR_VERSION = 1
        PCR_MAJOR_VERSION = 1
        _Struct_10._fields_ = [
            ('TibPad0', ULONG * 2),
            ('Spare1', PVOID),
            ('Self', POINTER(_KPCR)),
            ('CurrentPrcb', POINTER(_KPRCB)),
            ('LockArray', PKSPIN_LOCK_QUEUE),
            ('Used_Self', PVOID),
        ]


        _Struct_9._Struct_10 = _Struct_10
        _Struct_9._anonymous_ = (
            '_Struct_10',
        )
        _Struct_9._fields_ = [
            ('NtTib', NT_TIB),
            ('_Struct_10', _Struct_9._Struct_10),
        ]


        _KPCR._Struct_9 = _Struct_9
        _Struct_11._fields_ = [
            ('ApcInterrupt', UCHAR), # 0x01 if APC INT pending
            ('DispatchInterrupt', UCHAR), # 0x01 if dispatch INT pending
        ]


        _Struct_10._Struct_11 = _Struct_11
        _Struct_10._anonymous_ = (
            '_Struct_11',
        )
        _Struct_10._fields_ = [
            ('SoftwareInterruptPending', USHORT), # Software Interrupt Pending Flag
            ('_Struct_11', _Struct_10._Struct_11),
        ]


        _KPCR._Struct_10 = _Struct_10
        _KPCR._anonymous_ = (
            '_Struct_9',
            '_Struct_10',
        )
        _KPCR._fields_ = [
            ('_Struct_9', _KPCR._Struct_9), # N.B. The offset to the PRCB in the PCR is fixed for all time.
            ('CurrentIrql', KIRQL),
            ('SecondLevelCacheAssociativity', UCHAR),
            ('Unused0', ULONG * 3),
            ('MajorVersion', USHORT),
            ('MinorVersion', USHORT),
            ('StallScaleFactor', ULONG),
            ('Unused1', PVOID * 3),
            ('KernelReserved', ULONG * 15),
            ('SecondLevelCacheSize', ULONG),
            ('_Struct_10', _KPCR._Struct_10),
            ('InterruptPad', USHORT),
            ('HalReserved', ULONG * 32),
            ('KdVersionBlock', PVOID),
            ('Unused3', PVOID),
            ('PcrAlign1', ULONG * 8),
        ]


        KPCR = _KPCR
        PKPCR = POINTER(_KPCR)


        _Struct_11._fields_ = [
            ('TibPad0', ULONG * 2),
            ('Spare1', PVOID),
            ('Self', POINTER(_KPCR)),
            ('CurrentPrcb', POINTER(_KPRCB)),
            ('LockArray', PKSPIN_LOCK_QUEUE),
            ('Used_Self', PVOID),
        ]


        ._Struct_11 = _Struct_11
        ._anonymous_ = (
            '_Struct_11',
        )
        ._fields_ = [
            ('NtTib', NT_TIB),
            ('_Struct_11', ._Struct_11),
        ]


        ._fields_ = [
            ('TibPad0', ULONG * 2),
            ('Spare1', PVOID),
            ('Self', POINTER(_KPCR)),
            ('CurrentPrcb', POINTER(_KPRCB)),
            ('LockArray', PKSPIN_LOCK_QUEUE),
            ('Used_Self', PVOID),
        ]


        Self = POINTER(_KPCR)


        CurrentPrcb = POINTER(_KPRCB)


        _Struct_12._fields_ = [
            ('ApcInterrupt', UCHAR), # 0x01 if APC INT pending
            ('DispatchInterrupt', UCHAR), # 0x01 if dispatch INT pending
        ]


        ._Struct_12 = _Struct_12
        ._anonymous_ = (
            '_Struct_12',
        )
        ._fields_ = [
            ('SoftwareInterruptPending', USHORT), # Software Interrupt Pending Flag
            ('_Struct_12', ._Struct_12),
        ]


        ._fields_ = [
            ('ApcInterrupt', UCHAR), # 0x01 if APC INT pending
            ('DispatchInterrupt', UCHAR), # 0x01 if dispatch INT pending
        ]


        _KEXCEPTION_FRAME._fields_ = [
            ('Param5', ULONG),
            ('TrapFrame', ULONG), # Kernel callout frame variables.
            ('OutputBuffer', ULONG),
            ('OutputLength', ULONG),
            ('Pad', ULONG), # Saved nonvolatile registers.
            ('R4', ULONG),
            ('R5', ULONG),
            ('R6', ULONG),
            ('R7', ULONG),
            ('R8', ULONG),
            ('R9', ULONG),
            ('R10', ULONG),
            ('R11', ULONG),
            ('Return', ULONG),
        ]


        KEXCEPTION_FRAME = _KEXCEPTION_FRAME
        PKEXCEPTION_FRAME = POINTER(_KEXCEPTION_FRAME)


        class _KARM_VFP_STATE(ctypes.Structure):
            pass
        _KARM_VFP_STATE._fields_ = [
            ('Link', POINTER(_KARM_VFP_STATE)), # link to next state entry
            ('Fpscr', ULONG), # FPSCR register
            ('Reserved', ULONG), # reserved for future use
            ('Reserved2', ULONG), # reserved for future use
            ('VfpD', ULONGLONG * 32), # All D registers (0 - 31)
        ]


        KARM_VFP_STATE = _KARM_VFP_STATE
        PKARM_VFP_STATE = POINTER(_KARM_VFP_STATE)


        entry = state


        KTRAP_FRAME_ARGUMENTS = 14 * 4
        _Union_8._fields_ = [
            ('FaultAddress', ULONG), # page faults only
            ('TrapFrame', ULONG), # system services only
        ]


        _KTRAP_FRAME._Union_8 = _Union_8
        _Union_9._fields_ = [
            ('PreviousMode', KPROCESSOR_MODE), # system services only
            ('PreviousIrql', KIRQL), # interrupts only
        ]


        _KTRAP_FRAME._Union_9 = _Union_9
        _KTRAP_FRAME._anonymous_ = (
            '_Union_8',
            '_Union_9',
        )
        _KTRAP_FRAME._fields_ = [
            ('Arg3', ULONG), # page faults only
            ('FaultStatus', ULONG), # page faults only
            ('_Union_8', _KTRAP_FRAME._Union_8),
            ('Reserved', ULONG), # always valid, internal use
            ('ExceptionActive', UCHAR), # always valid
            ('ContextFromKFramesUnwound', UCHAR), # set if KeContextFromKFrames created this frame
            ('DebugRegistersValid', UCHAR), # always valid
            ('_Union_9', _KTRAP_FRAME._Union_9),
            ('VfpState', PKARM_VFP_STATE), # trap was taken.
            ('Bvr', ULONG * ARM_MAX_BREAKPOINTS), # Debug registers
            ('Bcr', ULONG * ARM_MAX_BREAKPOINTS),
            ('Wvr', ULONG * ARM_MAX_WATCHPOINTS),
            ('Wcr', ULONG * ARM_MAX_WATCHPOINTS),
            ('R0', ULONG), # Volatile registers R0 - R3, R12, and the SP, LR
            ('R1', ULONG),
            ('R2', ULONG),
            ('R3', ULONG),
            ('R12', ULONG),
            ('Sp', ULONG),
            ('Lr', ULONG),
            ('R11', ULONG), # R11/PC for a frame chain, plus the saved CPSR
            ('Pc', ULONG),
            ('Cpsr', ULONG),
        ]


        KTRAP_FRAME = _KTRAP_FRAME
        PKTRAP_FRAME = POINTER(_KTRAP_FRAME)


        ._fields_ = [
            ('FaultAddress', ULONG), # page faults only
            ('TrapFrame', ULONG), # system services only
        ]


        ._fields_ = [
            ('PreviousMode', KPROCESSOR_MODE), # system services only
            ('PreviousIrql', KIRQL), # interrupts only
        ]


        PDE_BASE = 0xC0300000
        PTE_BASE = 0xC0000000
        PTE_TOP = 0xC03FFFFF
        PDE_TOP = 0xC0300FFF
        PDI_SHIFT = 22
        PTI_SHIFT = 12
        PTE_PER_PAGE = PAGE_SIZE / ctypes.sizeof(ULONG)
        PDE_PER_PAGE = PAGE_SIZE / ctypes.sizeof(ULONG)
        MM_HIGHEST_USER_ADDRESS = MmHighestUserAddress
        MM_SYSTEM_RANGE_START = MmSystemRangeStart

        if defined(_LOCAL_COPY_USER_PROBE_ADDRESS_):
            MM_USER_PROBE_ADDRESS = _LOCAL_COPY_USER_PROBE_ADDRESS_

            if defined(__CONVERGED_WIN32K_DRIVER__):
                pass
        else:
                pass
            # END IF
    else:
            MM_USER_PROBE_ADDRESS = MmUserProbeAddress
        # END IF
        MM_KSEG0_BASE = MM_SYSTEM_RANGE_START
        MM_SYSTEM_SPACE_END = 0xFFFFFFFF
        MM_LOWEST_USER_ADDRESS = (PVOID)(LONG_PTR)0x10000

            if PRAGMA_DEPRECATED_DDK:
                pass
            # END IF
        if defined(_M_ARM) and not defined(RC_INVOKED)  and not defined(MIDL_PASS):
            RESULT_ZERO = 0
            RESULT_NEGATIVE = 1
            RESULT_POSITIVE = 2


            class _INTERLOCKED_RESULT(ENUM):
                #~#~#~ ResultNegative = RESULT_NEGATIVE
                #~#~#~ ResultZero = RESULT_ZERO
                #~#~#~ ResultPositive = RESULT_POSITIVE
                pass


            INTERLOCKED_RESULT = _INTERLOCKED_RESULT


def ExInterlockedDecrementLong(Addend, Lock):
    return _ExInterlockedDecrementLongAddend


def ExInterlockedIncrementLong(Addend, Lock):
    return _ExInterlockedIncrementLongAddend


def ExInterlockedExchangeULONG(Target, Value, Lock):
    return _ExInterlockedExchangeULONGTarget, Value
        # END IF   defined(_M_ARM) and not defined(RC_INVOKED)  and not defined(MIDL_PASS)
        CP15_PCR_RESERVED_MASK = 0xFFF


def KIPCR():
    return (ULONG_PTR(_MoveFromCoprocessorCP15_TPIDRPRW) & ~CP15_PCR_RESERVED_MASK)

            if (NTDDI_VERSION < NTDDI_WIN7) or not defined(NT_PROCESSOR_GROUPS):
                pass
            # END IF
        if not defined(MIDL_PASS) and defined(_M_ARM):
            pass
        # END IF   not defined(MIDL_PASS) and defined(_M_ARM)
    # END IF   defined(_ARM_)
    if defined(_ARM_) and not defined(MIDL_PASS):
        pass
    # END IF   defined(_ARM_) and not defined(MIDL_PASS)
    if defined(_ARM64_):
        PCR_MINOR_VERSION = 1
        PCR_MAJOR_VERSION = 1
        _Struct_14._fields_ = [
            ('TibPad0', PVOID * 2), # + 000
            ('Spare1', PVOID), # + 010
            ('Self', POINTER(_KPCR)), # + 018
            ('PcrReserved0', PVOID), # + 020
            ('LockArray', PKSPIN_LOCK_QUEUE), # + 028
            ('Used_Self', PVOID), # + 030
        ]


        _Struct_13._Struct_14 = _Struct_14
        _Struct_13._anonymous_ = (
            '_Struct_14',
        )
        _Struct_13._fields_ = [
            ('NtTib', NT_TIB), # + 000
            ('_Struct_14', _Struct_13._Struct_14),
        ]


        _KPCR._Struct_13 = _Struct_13
        _Struct_15._fields_ = [
            ('ApcInterrupt', UCHAR), # + 048 - - 0x01 if APC INT pending
            ('DispatchInterrupt', UCHAR), # + 049 - - 0x01 if dispatch INT pending
        ]


        _Struct_14._Struct_15 = _Struct_15
        _Struct_14._anonymous_ = (
            '_Struct_15',
        )
        _Struct_14._fields_ = [
            ('SoftwareInterruptPending', USHORT), # + 048 - - Software Interrupt Pending Flag
            ('_Struct_15', _Struct_14._Struct_15),
        ]


        _KPCR._Struct_14 = _Struct_14
        _KPCR._anonymous_ = (
            '_Struct_13',
            '_Struct_14',
        )
        _KPCR._fields_ = [
            ('_Struct_13', _KPCR._Struct_13), # N.B. The offset to the PRCB in the PCR is fixed for all time.
            ('CurrentIrql', KIRQL), # + 038
            ('SecondLevelCacheAssociativity', UCHAR), # + 039
            ('Pad1', UCHAR * 2), # + 03A
            ('MajorVersion', USHORT), # + 03C
            ('MinorVersion', USHORT), # + 03E
            ('StallScaleFactor', ULONG), # + 040
            ('SecondLevelCacheSize', ULONG), # + 044
            ('_Struct_14', _KPCR._Struct_14),
            ('InterruptPad', USHORT), # + 04A
            ('PanicStorage', ULONG64 * 6), # + 050 - - Must be 16 - byte aligned
            ('KdVersionBlock', PVOID), # + 080
            ('HalReserved', PVOID * 15), # + 088
        ]


        KPCR = _KPCR
        PKPCR = POINTER(_KPCR)


        _Struct_15._fields_ = [
            ('TibPad0', PVOID * 2), # + 000
            ('Spare1', PVOID), # + 010
            ('Self', POINTER(_KPCR)), # + 018
            ('PcrReserved0', PVOID), # + 020
            ('LockArray', PKSPIN_LOCK_QUEUE), # + 028
            ('Used_Self', PVOID), # + 030
        ]


        ._Struct_15 = _Struct_15
        ._anonymous_ = (
            '_Struct_15',
        )
        ._fields_ = [
            ('NtTib', NT_TIB), # + 000
            ('_Struct_15', ._Struct_15),
        ]


        ._fields_ = [
            ('TibPad0', PVOID * 2), # + 000
            ('Spare1', PVOID), # + 010
            ('Self', POINTER(_KPCR)), # + 018
            ('PcrReserved0', PVOID), # + 020
            ('LockArray', PKSPIN_LOCK_QUEUE), # + 028
            ('Used_Self', PVOID), # + 030
        ]


        018 = +


        _Struct_16._fields_ = [
            ('ApcInterrupt', UCHAR), # + 048 - - 0x01 if APC INT pending
            ('DispatchInterrupt', UCHAR), # + 049 - - 0x01 if dispatch INT pending
        ]


        ._Struct_16 = _Struct_16
        ._anonymous_ = (
            '_Struct_16',
        )
        ._fields_ = [
            ('SoftwareInterruptPending', USHORT), # + 048 - - Software Interrupt Pending Flag
            ('_Struct_16', ._Struct_16),
        ]


        ._fields_ = [
            ('ApcInterrupt', UCHAR), # + 048 - - 0x01 if APC INT pending
            ('DispatchInterrupt', UCHAR), # + 049 - - 0x01 if dispatch INT pending
        ]


        _KEXCEPTION_FRAME._fields_ = [
            ('X19', ULONG64), # Saved nonvolatile registers.
            ('X20', ULONG64),
            ('X21', ULONG64),
            ('X22', ULONG64),
            ('X23', ULONG64),
            ('X24', ULONG64),
            ('X25', ULONG64),
            ('X26', ULONG64),
            ('X27', ULONG64),
            ('X28', ULONG64),
            ('Fp', ULONG64),
            ('Return', ULONG64),
        ]


        KEXCEPTION_FRAME = _KEXCEPTION_FRAME
        PKEXCEPTION_FRAME = POINTER(_KEXCEPTION_FRAME)


        class _KARM64_VFP_STATE(ctypes.Structure):
            pass
        _KARM64_VFP_STATE._fields_ = [
            ('Link', POINTER(_KARM64_VFP_STATE)), # link to next state entry
            ('Fpcr', ULONG), # FPCR register
            ('Fpsr', ULONG), # FPSR register
            ('V', NEON128 * 32), # All V registers (0 - 31)
        ]


        KARM64_VFP_STATE = _KARM64_VFP_STATE
        PKARM64_VFP_STATE = POINTER(_KARM64_VFP_STATE)


        entry = state


        KTRAP_FRAME_ARGUMENTS = 10 * 8
        KTRAP_FRAME_SIGNATURE = 'prTK'
        _Union_10._fields_ = [
            ('PreviousMode', KPROCESSOR_MODE), # system services only
            ('PreviousIrql', KIRQL), # interrupts only
        ]


        _KTRAP_FRAME._Union_10 = _Union_10
        _Union_11._fields_ = [
            ('FaultAddress', ULONG64), # page faults only
            ('TrapFrame', ULONG64), # system services only
        ]


        _KTRAP_FRAME._Union_11 = _Union_11
        _Struct_18._fields_ = [
            ('X0', ULONG64),
            ('X1', ULONG64),
            ('X2', ULONG64),
            ('X3', ULONG64),
            ('X4', ULONG64),
            ('X5', ULONG64),
            ('X6', ULONG64),
            ('X7', ULONG64),
            ('X8', ULONG64),
            ('X9', ULONG64),
            ('X10', ULONG64),
            ('X11', ULONG64),
            ('X12', ULONG64),
            ('X13', ULONG64),
            ('X14', ULONG64),
            ('X15', ULONG64),
            ('X16', ULONG64),
            ('X17', ULONG64),
            ('X18', ULONG64),
        ]


        _Struct_17._Struct_18 = _Struct_18
        _Struct_17._anonymous_ = (
            '_Struct_18',
        )
        _Struct_17._fields_ = [
            ('X', ULONG64 * 19),
            ('_Struct_18', _Struct_17._Struct_18),
        ]


        _KTRAP_FRAME._Struct_17 = _Struct_17
        _KTRAP_FRAME._anonymous_ = (
            '_Union_10',
            '_Union_11',
            '_Struct_17',
        )
        _KTRAP_FRAME._fields_ = [
            ('ExceptionActive', UCHAR), # + 0x000
            ('ContextFromKFramesUnwound', UCHAR), # + 0x001
            ('DebugRegistersValid', UCHAR), # + 0x002
            ('_Union_10', _KTRAP_FRAME._Union_10), # + 0x003
            ('Reserved', ULONG), # + 0x004
            ('_Union_11', _KTRAP_FRAME._Union_11), # + 0x008
            ('VfpState', PKARM64_VFP_STATE), # + 0x010
            ('Bcr', ULONG * ARM64_MAX_BREAKPOINTS), # + 0x018
            ('Bvr', ULONG64 * ARM64_MAX_BREAKPOINTS), # + 0x038
            ('Wcr', ULONG * ARM64_MAX_WATCHPOINTS), # + 0x078
            ('Wvr', ULONG64 * ARM64_MAX_WATCHPOINTS), # + 0x080
            ('Spsr', ULONG), # + 0x090
            ('Esr', ULONG), # + 0x094
            ('Sp', ULONG64), # + 0x098
            ('_Struct_17', _KTRAP_FRAME._Struct_17), # + 0x0A0
            ('Lr', ULONG64), # + 0x138
            ('Fp', ULONG64), # + 0x140
            ('Pc', ULONG64), # + 0x148
        ]


        KTRAP_FRAME = _KTRAP_FRAME
        PKTRAP_FRAME = POINTER(_KTRAP_FRAME)


        ._fields_ = [
            ('PreviousMode', KPROCESSOR_MODE), # system services only
            ('PreviousIrql', KIRQL), # interrupts only
        ]


        ._fields_ = [
            ('FaultAddress', ULONG64), # page faults only
            ('TrapFrame', ULONG64), # system services only
        ]


        _Struct_18._fields_ = [
            ('X0', ULONG64),
            ('X1', ULONG64),
            ('X2', ULONG64),
            ('X3', ULONG64),
            ('X4', ULONG64),
            ('X5', ULONG64),
            ('X6', ULONG64),
            ('X7', ULONG64),
            ('X8', ULONG64),
            ('X9', ULONG64),
            ('X10', ULONG64),
            ('X11', ULONG64),
            ('X12', ULONG64),
            ('X13', ULONG64),
            ('X14', ULONG64),
            ('X15', ULONG64),
            ('X16', ULONG64),
            ('X17', ULONG64),
            ('X18', ULONG64),
        ]


        ._Struct_18 = _Struct_18
        ._anonymous_ = (
            '_Struct_18',
        )
        ._fields_ = [
            ('X', ULONG64 * 19),
            ('_Struct_18', ._Struct_18),
        ]


        ._fields_ = [
            ('X0', ULONG64),
            ('X1', ULONG64),
            ('X2', ULONG64),
            ('X3', ULONG64),
            ('X4', ULONG64),
            ('X5', ULONG64),
            ('X6', ULONG64),
            ('X7', ULONG64),
            ('X8', ULONG64),
            ('X9', ULONG64),
            ('X10', ULONG64),
            ('X11', ULONG64),
            ('X12', ULONG64),
            ('X13', ULONG64),
            ('X14', ULONG64),
            ('X15', ULONG64),
            ('X16', ULONG64),
            ('X17', ULONG64),
            ('X18', ULONG64),
        ]


        MM_HIGHEST_USER_ADDRESS = MmHighestUserAddress
        MM_SYSTEM_RANGE_START = MmSystemRangeStart

        if defined(_LOCAL_COPY_USER_PROBE_ADDRESS_):
            MM_USER_PROBE_ADDRESS = _LOCAL_COPY_USER_PROBE_ADDRESS_

            if defined(__CONVERGED_WIN32K_DRIVER__):
                pass
        else:
                pass
            # END IF
    else:
            MM_USER_PROBE_ADDRESS = MmUserProbeAddress
        # END IF
        MM_LOWEST_USER_ADDRESS = (PVOID)(LONG_PTR)0x10000

            if PRAGMA_DEPRECATED_DDK:
                pass
            # END IF
        if defined(_M_ARM64) and not defined(RC_INVOKED)  and not defined(MIDL_PASS):
            RESULT_ZERO = 0
            RESULT_NEGATIVE = 1
            RESULT_POSITIVE = 2


            class _INTERLOCKED_RESULT(ENUM):
                #~#~#~ ResultNegative = RESULT_NEGATIVE
                #~#~#~ ResultZero = RESULT_ZERO
                #~#~#~ ResultPositive = RESULT_POSITIVE
                pass


            INTERLOCKED_RESULT = _INTERLOCKED_RESULT


def ExInterlockedDecrementLong(Addend, Lock):
    return _ExInterlockedDecrementLongAddend


def ExInterlockedIncrementLong(Addend, Lock):
    return _ExInterlockedIncrementLongAddend


def ExInterlockedExchangeULONG(Target, Value, Lock):
    return _ExInterlockedExchangeULONGTarget, Value
        # END IF   defined(_M_ARM64) and not defined(RC_INVOKED)  and not defined(MIDL_PASS)
        ARM64_PCR_RESERVED_MASK = 0xFFF


def KIPCR():
    return (ULONG_PTR(_ReadStatusRegARM64_TPIDR_EL1) & ~ARM64_PCR_RESERVED_MASK)

            if (NTDDI_VERSION < NTDDI_WIN7) or not defined(NT_PROCESSOR_GROUPS):
                pass
            # END IF
        if not defined(MIDL_PASS) and defined(_M_ARM64):
            pass
        # END IF   not defined(MIDL_PASS) and defined(_M_ARM64)
    # END IF   defined(_ARM64_)
    if defined(_ARM64_) and not defined(MIDL_PASS):
        pass
    # END IF   defined(_ARM64_) and not defined(MIDL_PASS)
    class _SYSTEM_FIRMWARE_TABLE_ACTION(ENUM):
        SystemFirmwareTable_Enumerate = 1
        SystemFirmwareTable_Get = 2


    SYSTEM_FIRMWARE_TABLE_ACTION = _SYSTEM_FIRMWARE_TABLE_ACTION
    class _SYSTEM_FIRMWARE_TABLE_INFORMATION(ctypes.Structure):
        pass
    _SYSTEM_FIRMWARE_TABLE_INFORMATION._fields_ = [
        ('ProviderSignature', ULONG),
        ('Action', SYSTEM_FIRMWARE_TABLE_ACTION),
        ('TableID', ULONG),
        ('TableBufferLength', ULONG),
        ('TableBuffer', UCHAR * ANYSIZE_ARRAY),
    ]


    SYSTEM_FIRMWARE_TABLE_INFORMATION = _SYSTEM_FIRMWARE_TABLE_INFORMATION
    PSYSTEM_FIRMWARE_TABLE_INFORMATION = POINTER(_SYSTEM_FIRMWARE_TABLE_INFORMATION)


    class _SYSTEM_FIRMWARE_TABLE_HANDLER(ctypes.Structure):
        pass
    _SYSTEM_FIRMWARE_TABLE_HANDLER._fields_ = [
        ('ProviderSignature', ULONG),
        ('Register', BOOLEAN),
        ('FirmwareTableHandler', PFNFTH),
        ('DriverObject', PVOID),
    ]


    SYSTEM_FIRMWARE_TABLE_HANDLER = _SYSTEM_FIRMWARE_TABLE_HANDLER
    PSYSTEM_FIRMWARE_TABLE_HANDLER = POINTER(_SYSTEM_FIRMWARE_TABLE_HANDLER)


    class _TIMER_SET_INFORMATION_CLASS(ENUM):
        TimerSetCoalescableTimer = 1
        MaxTimerInfoClass = 2


    TIMER_SET_INFORMATION_CLASS = _TIMER_SET_INFORMATION_CLASS
    if (NTDDI_VERSION >= NTDDI_WIN7):
        class _TIMER_SET_COALESCABLE_TIMER_INFO(ctypes.Structure):
            pass
        _TIMER_SET_COALESCABLE_TIMER_INFO._fields_ = [
            ('LARGE_INTEGER DueTime', _In_),
            ('PTIMER_APC_ROUTINE TimerApcRoutine', _In_opt_),
            ('PVOID TimerContext', _In_opt_),
            ('struct _COUNTED_REASON_CONTEXT *WakeContext', _In_opt_),
            ('ULONG Period', _In_opt_),
            ('ULONG TolerableDelay', _In_),
            ('PBOOLEAN PreviousState', _Out_opt_),
        ]


        TIMER_SET_COALESCABLE_TIMER_INFO = _TIMER_SET_COALESCABLE_TIMER_INFO
        PTIMER_SET_COALESCABLE_TIMER_INFO = POINTER(_TIMER_SET_COALESCABLE_TIMER_INFO)


    # END IF   (NTDDI_VERSION >= NTDDI_WIN7)
    class _DRIVER_VERIFIER_THUNK_PAIRS(ctypes.Structure):
        pass
    _DRIVER_VERIFIER_THUNK_PAIRS._fields_ = [
        ('PristineRoutine', PDRIVER_VERIFIER_THUNK_ROUTINE),
        ('NewRoutine', PDRIVER_VERIFIER_THUNK_ROUTINE),
    ]


    DRIVER_VERIFIER_THUNK_PAIRS = _DRIVER_VERIFIER_THUNK_PAIRS
    PDRIVER_VERIFIER_THUNK_PAIRS = POINTER(_DRIVER_VERIFIER_THUNK_PAIRS)


    DRIVER_VERIFIER_SPECIAL_POOLING = 0x0001
    DRIVER_VERIFIER_FORCE_IRQL_CHECKING = 0x0002
    DRIVER_VERIFIER_INJECT_ALLOCATION_FAILURES = 0x0004
    DRIVER_VERIFIER_TRACK_POOL_ALLOCATIONS = 0x0008
    DRIVER_VERIFIER_IO_CHECKING = 0x0010
    XSTATE_LEGACY_FLOATING_POINT = 0
    XSTATE_LEGACY_SSE = 1
    XSTATE_GSSE = 2
    XSTATE_AVX = XSTATE_GSSE
    XSTATE_MPX_BNDREGS = 3
    XSTATE_MPX_BNDCSR = 4
    XSTATE_AVX512_KMASK = 5
    XSTATE_AVX512_ZMM_H = 6
    XSTATE_AVX512_ZMM = 7
    XSTATE_IPT = 8
    XSTATE_LWP = 62
    MAXIMUM_XSTATE_FEATURES = 64
    XSTATE_MASK_LEGACY_FLOATING_POINT = 1ui64 << (XSTATE_LEGACY_FLOATING_POINT)
    XSTATE_MASK_LEGACY_SSE = 1ui64 << (XSTATE_LEGACY_SSE)
    XSTATE_MASK_LEGACY = XSTATE_MASK_LEGACY_FLOATING_POINT | XSTATE_MASK_LEGACY_SSE
    XSTATE_MASK_GSSE = 1ui64 << (XSTATE_GSSE)
    XSTATE_MASK_AVX = XSTATE_MASK_GSSE
    XSTATE_MASK_MPX = (
    (1ui64 << (XSTATE_MPX_BNDREGS))  |
     (1ui64 << (XSTATE_MPX_BNDCSR))
)
    XSTATE_MASK_AVX512 = (
    (1ui64 << (XSTATE_AVX512_KMASK))  |
     (1ui64 << (XSTATE_AVX512_ZMM_H))  |
     (1ui64 << (XSTATE_AVX512_ZMM))
)
    XSTATE_MASK_IPT = 1ui64 << (XSTATE_IPT)
    XSTATE_MASK_LWP = 1ui64 << (XSTATE_LWP)
    XSTATE_MASK_ALLOWED = (
    XSTATE_MASK_LEGACY  |
     XSTATE_MASK_AVX  |
     XSTATE_MASK_MPX  |
     XSTATE_MASK_AVX512  |
     XSTATE_MASK_IPT  |
     XSTATE_MASK_LWP
)
    XSTATE_MASK_PERSISTENT = (1ui64 << (XSTATE_MPX_BNDCSR)) | XSTATE_MASK_LWP
    XSTATE_COMPACTION_ENABLE = 63
    XSTATE_COMPACTION_ENABLE_MASK = 1ui64 << (XSTATE_COMPACTION_ENABLE)
    XSTATE_ALIGN_BIT = 1
    XSTATE_ALIGN_MASK = 1ui64 << (XSTATE_ALIGN_BIT)
    XSTATE_CONTROLFLAG_XSAVEOPT_MASK = 1
    XSTATE_CONTROLFLAG_XSAVEC_MASK = 2
    XSTATE_CONTROLFLAG_VALID_MASK = (
    XSTATE_CONTROLFLAG_XSAVEOPT_MASK  |
     XSTATE_CONTROLFLAG_XSAVEC_MASK
)
    class _XSTATE_FEATURE(ctypes.Structure):
        pass
    _XSTATE_FEATURE._fields_ = [
        ('Offset', ULONG),
        ('Size', ULONG),
    ]


    XSTATE_FEATURE = _XSTATE_FEATURE
    PXSTATE_FEATURE = POINTER(_XSTATE_FEATURE)


    class _XSTATE_CONFIGURATION(ctypes.Structure):
        pass
    _Struct_20._fields_ = [
        ('OptimizedSave : 1', ULONG),
        ('CompactionEnabled : 1', ULONG),
    ]


    _Struct_19._Struct_20 = _Struct_20
    _Struct_19._anonymous_ = (
        '_Struct_20',
    )
    _Struct_19._fields_ = [
        ('ControlFlags', ULONG),
        ('_Struct_20', _Struct_19._Struct_20),
    ]


    _XSTATE_CONFIGURATION._Struct_19 = _Struct_19
    _XSTATE_CONFIGURATION._anonymous_ = (
        '_Struct_19',
    )
    _XSTATE_CONFIGURATION._fields_ = [
        ('EnabledFeatures', ULONG64), # Mask of all enabled features
        ('EnabledVolatileFeatures', ULONG64), # Mask of volatile enabled features
        ('Size', ULONG), # Total size of the save area for user states
        ('_Struct_19', _XSTATE_CONFIGURATION._Struct_19), # Control Flags
        ('Features', XSTATE_FEATURE * MAXIMUM_XSTATE_FEATURES), # List of features
        ('EnabledSupervisorFeatures', ULONG64), # Mask of all supervisor features
        ('AlignedFeatures', ULONG64), # Mask of features that require start address to be 64 byte aligned
        ('AllFeatureSize', ULONG), # Total size of the save area for user and supervisor states

        # List which holds size of each user and supervisor state supported by
        # CPU
        ('AllFeatures', ULONG * MAXIMUM_XSTATE_FEATURES),
    ]


    XSTATE_CONFIGURATION = _XSTATE_CONFIGURATION
    PXSTATE_CONFIGURATION = POINTER(_XSTATE_CONFIGURATION)


    _Struct_20._fields_ = [
        ('OptimizedSave : 1', ULONG),
        ('CompactionEnabled : 1', ULONG),
    ]


    ._Struct_20 = _Struct_20
    ._anonymous_ = (
        '_Struct_20',
    )
    ._fields_ = [
        ('ControlFlags', ULONG),
        ('_Struct_20', ._Struct_20),
    ]


    ._fields_ = [
        ('OptimizedSave : 1', ULONG),
        ('CompactionEnabled : 1', ULONG),
    ]



    if defined(_MAC):
        pass
    # END IF
    NX_SUPPORT_POLICY_ALWAYSOFF = 0
    NX_SUPPORT_POLICY_ALWAYSON = 1
    NX_SUPPORT_POLICY_OPTIN = 2
    NX_SUPPORT_POLICY_OPTOUT = 3
    SEH_VALIDATION_POLICY_ON = 0
    SEH_VALIDATION_POLICY_OFF = 1
    SEH_VALIDATION_POLICY_TELEMETRY = 2
    SEH_VALIDATION_POLICY_DEFER = 3
    SHARED_GLOBAL_FLAGS_ERROR_PORT_V = 0x0
    SHARED_GLOBAL_FLAGS_ERROR_PORT = 1UL << SHARED_GLOBAL_FLAGS_ERROR_PORT_V
    SHARED_GLOBAL_FLAGS_ELEVATION_ENABLED_V = 0x1
    SHARED_GLOBAL_FLAGS_ELEVATION_ENABLED = (
    1UL << SHARED_GLOBAL_FLAGS_ELEVATION_ENABLED_V
)
    SHARED_GLOBAL_FLAGS_VIRT_ENABLED_V = 0x2
    SHARED_GLOBAL_FLAGS_VIRT_ENABLED = 1UL << SHARED_GLOBAL_FLAGS_VIRT_ENABLED_V
    SHARED_GLOBAL_FLAGS_INSTALLER_DETECT_ENABLED_V = 0x3
    SHARED_GLOBAL_FLAGS_INSTALLER_DETECT_ENABLED = (
    1UL << SHARED_GLOBAL_FLAGS_INSTALLER_DETECT_ENABLED_V
)
    SHARED_GLOBAL_FLAGS_LKG_ENABLED_V = 0x4
    SHARED_GLOBAL_FLAGS_LKG_ENABLED = 1UL << SHARED_GLOBAL_FLAGS_LKG_ENABLED_V
    SHARED_GLOBAL_FLAGS_DYNAMIC_PROC_ENABLED_V = 0x5
    SHARED_GLOBAL_FLAGS_DYNAMIC_PROC_ENABLED = (
    1UL << SHARED_GLOBAL_FLAGS_DYNAMIC_PROC_ENABLED_V
)
    SHARED_GLOBAL_FLAGS_CONSOLE_BROKER_ENABLED_V = 0x6
    SHARED_GLOBAL_FLAGS_CONSOLE_BROKER_ENABLED = (
    1UL << SHARED_GLOBAL_FLAGS_CONSOLE_BROKER_ENABLED_V
)
    SHARED_GLOBAL_FLAGS_SECURE_BOOT_ENABLED_V = 0x7
    SHARED_GLOBAL_FLAGS_SECURE_BOOT_ENABLED = (
    1UL << SHARED_GLOBAL_FLAGS_SECURE_BOOT_ENABLED_V
)
    SHARED_GLOBAL_FLAGS_MULTI_SESSION_SKU_V = 0x8
    SHARED_GLOBAL_FLAGS_MULTI_SESSION_SKU = (
    1UL << SHARED_GLOBAL_FLAGS_MULTI_SESSION_SKU_V
)
    SHARED_GLOBAL_FLAGS_MULTIUSERS_IN_SESSION_SKU_V = 0x9
    SHARED_GLOBAL_FLAGS_MULTIUSERS_IN_SESSION_SKU = (
    1UL << SHARED_GLOBAL_FLAGS_MULTIUSERS_IN_SESSION_SKU_V
)
    SHARED_GLOBAL_FLAGS_STATE_SEPARATION_ENABLED_V = 0xA
    SHARED_GLOBAL_FLAGS_STATE_SEPARATION_ENABLED = (
    1UL << SHARED_GLOBAL_FLAGS_STATE_SEPARATION_ENABLED_V
)


def EX_INIT_BITS(Flags, Bit):
    return *Flags | = Bit    # Safe to use before concurrently accessible


def EX_TEST_SET_BIT(Flags, Bit):
    return InterlockedBitTestAndSet PLONGFlags, Bit


def EX_TEST_CLEAR_BIT(Flags, Bit):
    return InterlockedBitTestAndReset PLONGFlags, Bit
    SYSTEM_CALL_SYSCALL = 0
    SYSTEM_CALL_INT_2E = 1
    SHARED_GLOBAL_FLAGS_QPC_BYPASS_ENABLED = 0x01
    SHARED_GLOBAL_FLAGS_QPC_BYPASS_USE_HV_PAGE = 0x02
    SHARED_GLOBAL_FLAGS_QPC_BYPASS_USE_MFENCE = 0x10
    SHARED_GLOBAL_FLAGS_QPC_BYPASS_USE_LFENCE = 0x20
    SHARED_GLOBAL_FLAGS_QPC_BYPASS_A73_ERRATA = 0x40
    SHARED_GLOBAL_FLAGS_QPC_BYPASS_USE_RDTSCP = 0x80
    class _KUSER_SHARED_DATA(ctypes.Structure):
        pass
    _Struct_22._fields_ = [
        ('NXSupportPolicy : 2', UCHAR),
        ('SEHValidationPolicy : 2', UCHAR),
        ('CurDirDevicesSkippedForDlls : 2', UCHAR),
        ('Reserved : 2', UCHAR),
    ]


    _Struct_21._Struct_22 = _Struct_22
    _Struct_21._anonymous_ = (
        '_Struct_22',
    )
    _Struct_21._fields_ = [
        ('MitigationPolicies', UCHAR),
        ('_Struct_22', _Struct_21._Struct_22),
    ]


    _KUSER_SHARED_DATA._Struct_21 = _Struct_21
    DUMMYSTRUCTNAME2._fields_ = [
        ('DbgErrorPortPresent       : 1', ULONG), # Use the bit definitions instead.
        ('DbgElevationEnabled       : 1', ULONG),
        ('DbgVirtEnabled            : 1', ULONG),
        ('DbgInstallerDetectEnabled : 1', ULONG),
        ('DbgLkgEnabled             : 1', ULONG),
        ('DbgDynProcessorEnabled    : 1', ULONG),
        ('DbgConsoleBrokerEnabled   : 1', ULONG),
        ('DbgSecureBootEnabled      : 1', ULONG),
        ('DbgMultiSessionSku        : 1', ULONG),
        ('DbgMultiUsersInSessionSku : 1', ULONG),
        ('DbgStateSeparationEnabled : 1', ULONG),
        ('SpareBits                 : 21', ULONG),
    ]


    DUMMYUNIONNAME2.DUMMYSTRUCTNAME2 = DUMMYSTRUCTNAME2
    DUMMYUNIONNAME2._fields_ = [
        ('SharedDataFlags', ULONG),
        ('DUMMYSTRUCTNAME2', DUMMYUNIONNAME2.DUMMYSTRUCTNAME2),
    ]


    _KUSER_SHARED_DATA.DUMMYUNIONNAME2 = DUMMYUNIONNAME2
    DUMMYSTRUCTNAME._fields_ = [
        ('ReservedTickCountOverlay', ULONG * 3),
        ('TickCountPad', ULONG * 1),
    ]


    DUMMYUNIONNAME3.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME3._fields_ = [
        ('KSYSTEM_TIME TickCount', volatile),
        ('ULONG64 TickCountQuad', volatile),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME3.DUMMYSTRUCTNAME),
    ]


    _KUSER_SHARED_DATA.DUMMYUNIONNAME3 = DUMMYUNIONNAME3
    _Struct_23._fields_ = [
        ('UCHAR QpcBypassEnabled', volatile), # can read the counter directly (bypassing the system call).
        ('QpcShift', UCHAR), # QPC count.
    ]


    _Struct_22._Struct_23 = _Struct_23
    _Struct_22._anonymous_ = (
        '_Struct_23',
    )
    _Struct_22._fields_ = [
        ('QpcData', USHORT),
        ('_Struct_23', _Struct_22._Struct_23),
    ]


    _KUSER_SHARED_DATA._Struct_22 = _Struct_22
    _KUSER_SHARED_DATA._anonymous_ = (
        '_Struct_21',
        '_Struct_22',
    )
    _KUSER_SHARED_DATA._fields_ = [
        ('TickCountLowDeprecated', ULONG), # N.B. The tick count is updated each time the clock ticks.
        ('TickCountMultiplier', ULONG),
        ('KSYSTEM_TIME InterruptTime', volatile), # Current 64 - bit interrupt time in 100ns units.
        ('KSYSTEM_TIME SystemTime', volatile), # Current 64 - bit system time in 100ns units.
        ('KSYSTEM_TIME TimeZoneBias', volatile), # Current 64 - bit time zone bias.
        ('ImageNumberLow', USHORT), # N.B. This is an inclusive range.
        ('ImageNumberHigh', USHORT),
        ('NtSystemRoot', WCHAR * 260), # an accurate result.
        ('MaxStackTraceDepth', ULONG), # Maximum stack trace depth if tracing enabled.
        ('CryptoExponent', ULONG), # Crypto exponent value.
        ('TimeZoneId', ULONG), # Time zone ID.
        ('LargePageMinimum', ULONG),
        ('AitSamplingValue', ULONG), # This value controls the AIT Sampling rate.
        ('AppCompatFlag', ULONG), # This value controls switchback processing.
        ('RNGSeedVersion', ULONGLONG), # Current Kernel Root RNG state seed version
        ('GlobalValidationRunlevel', ULONG), # This value controls assertion failure handling.
        ('LONG TimeZoneBiasStamp', volatile),
        ('NtBuildNumber', ULONG), # GetVersionEx hides the real number
        ('NtProductType', NT_PRODUCT_TYPE), # an accurate result.
        ('ProductTypeIsValid', BOOLEAN),
        ('Reserved0', BOOLEAN * 1),
        ('NativeProcessorArchitecture', USHORT),
        ('NtMajorVersion', ULONG), # version
        ('NtMinorVersion', ULONG),
        ('ProcessorFeatures', BOOLEAN * PROCESSOR_FEATURE_MAX), # Processor features.
        ('Reserved1', ULONG), # Reserved fields - do not use.
        ('Reserved3', ULONG),
        ('ULONG TimeSlip', volatile), # Time slippage while in debugger.
        ('AlternativeArchitecture', ALTERNATIVE_ARCHITECTURE_TYPE), # Alternative system architecture, e.g., NEC PC98xx on x86.
        ('BootId', ULONG), # Boot sequence, incremented for each boot attempt by the OS loader.
        ('SystemExpirationDate', LARGE_INTEGER), # that the system expires.
        ('SuiteMask', ULONG), # an accurate result.
        ('KdDebuggerEnabled', BOOLEAN), # TRUE if a kernel debugger is connected/enabled.
        ('_Struct_21', _KUSER_SHARED_DATA._Struct_21), # Mitigation policies.
        ('Reserved6', UCHAR * 2), # Two bytes of padding here - - offsets 0x2d6, 0x2d7
        ('ULONG ActiveConsoleId', volatile), # accurate result.
        ('ULONG DismountCount', volatile), # can use to see if they need to probe handles.

        # images need to use the 64 - bit COM+ runtime or the 32 - bit COM+
        # runtime.
        ('ComPlusPackage', ULONG),
        ('LastSystemRITEventTickCount', ULONG), # a minute per session). It is used for idle detection.
        ('NumberOfPhysicalPages', ULONG), # physical memory can be added or removed from a running system.
        ('SafeBootMode', BOOLEAN), # True if the system was booted in safe boot mode.
        ('VirtualizationFlags', UCHAR), # Virtualization flags
        ('Reserved12', UCHAR * 2), # Reserved (available for reuse).
        ('DUMMYUNIONNAME2', _KUSER_SHARED_DATA.DUMMYUNIONNAME2), # API for an accurate result
        ('DataFlagsPad', ULONG * 1),
        ('TestRetInstruction', ULONGLONG), # N.B. The following field is only used on 32 - bit systems.
        ('QpcFrequency', LONGLONG),
        ('SystemCall', ULONG), # operates with an altered view of the system service call mechanism.
        ('SystemCallPad0', ULONG), # Reserved, available for reuse.
        ('SystemCallPad', ULONGLONG * 2),
        ('DUMMYUNIONNAME3', _KUSER_SHARED_DATA.DUMMYUNIONNAME3), # The 64 - bit tick count.
        ('Cookie', ULONG), # Cookie for encoding pointers system wide.
        ('CookiePad', ULONG * 1),
        ('ConsoleSessionForegroundProcessId', LONGLONG), # RtlGetConsoleSessionForegroundProcessId API for an accurate result.
        ('TimeUpdateLock', ULONGLONG), # Placeholder for the (internal) time update lock.

        # The performance counter value used to establish the current system
        # time.
        ('BaselineSystemTimeQpc', ULONGLONG),

        # The performance counter value used to compute the last interrupt
        # time.
        ('BaselineInterruptTimeQpc', ULONGLONG),

        # performance count
        # (this value may vary to achieve time synchronization).
        ('QpcSystemTimeIncrement', ULONGLONG),

        # performance count
        # (this value is constant after the system is booted).
        ('QpcInterruptTimeIncrement', ULONGLONG),
        ('QpcSystemTimeIncrementShift', UCHAR), # increment.
        ('QpcInterruptTimeIncrementShift', UCHAR), # increment.
        ('UnparkedProcessorCount', USHORT), # The count of unparked processors.
        ('EnclaveFeatureMask', ULONG * 4), # A bitmask of enclave features supported on this system.
        ('TelemetryCoverageRound', ULONG), # Current coverage round for telemetry based coverage.
        ('UserModeGlobalLogger', USHORT * 16), # (UMGL).
        ('ImageFileExecutionOptions', ULONG), # from HKCU in addition to the original HKLM.

        # Generation of the kernel structure holding system language
        # information
        ('LangGenerationCount', ULONG),
        ('Reserved4', ULONGLONG), # Reserved (available for reuse).
        ('ULONGLONG InterruptTimeBias', volatile), # Current 64 - bit interrupt time bias in 100ns units.
        ('ULONGLONG QpcBias', volatile), # before the shift is applied.
        ('ActiveProcessorCount', ULONG), # Number of active processors and groups.
        ('UCHAR ActiveGroupCount', volatile),
        ('Reserved9', UCHAR), # Reserved (available for re - use).
        ('_Struct_22', _KUSER_SHARED_DATA._Struct_22),
        ('TimeZoneBiasEffectiveStart', LARGE_INTEGER),
        ('TimeZoneBiasEffectiveEnd', LARGE_INTEGER),
        ('XState', XSTATE_CONFIGURATION), # Extended processor state configuration
    ]


    KUSER_SHARED_DATA = _KUSER_SHARED_DATA
    PKUSER_SHARED_DATA = POINTER(_KUSER_SHARED_DATA)


    _Struct_23._fields_ = [
        ('NXSupportPolicy : 2', UCHAR),
        ('SEHValidationPolicy : 2', UCHAR),
        ('CurDirDevicesSkippedForDlls : 2', UCHAR),
        ('Reserved : 2', UCHAR),
    ]


    ._Struct_23 = _Struct_23
    ._anonymous_ = (
        '_Struct_23',
    )
    ._fields_ = [
        ('MitigationPolicies', UCHAR),
        ('_Struct_23', ._Struct_23),
    ]


    ._fields_ = [
        ('NXSupportPolicy : 2', UCHAR),
        ('SEHValidationPolicy : 2', UCHAR),
        ('CurDirDevicesSkippedForDlls : 2', UCHAR),
        ('Reserved : 2', UCHAR),
    ]


    DUMMYSTRUCTNAME2._fields_ = [
        ('DbgErrorPortPresent       : 1', ULONG), # Use the bit definitions instead.
        ('DbgElevationEnabled       : 1', ULONG),
        ('DbgVirtEnabled            : 1', ULONG),
        ('DbgInstallerDetectEnabled : 1', ULONG),
        ('DbgLkgEnabled             : 1', ULONG),
        ('DbgDynProcessorEnabled    : 1', ULONG),
        ('DbgConsoleBrokerEnabled   : 1', ULONG),
        ('DbgSecureBootEnabled      : 1', ULONG),
        ('DbgMultiSessionSku        : 1', ULONG),
        ('DbgMultiUsersInSessionSku : 1', ULONG),
        ('DbgStateSeparationEnabled : 1', ULONG),
        ('SpareBits                 : 21', ULONG),
    ]


    DUMMYUNIONNAME2.DUMMYSTRUCTNAME2 = DUMMYSTRUCTNAME2
    DUMMYUNIONNAME2._fields_ = [
        ('SharedDataFlags', ULONG),
        ('DUMMYSTRUCTNAME2', DUMMYUNIONNAME2.DUMMYSTRUCTNAME2),
    ]


    DUMMYSTRUCTNAME2._fields_ = [
        ('DbgErrorPortPresent       : 1', ULONG), # Use the bit definitions instead.
        ('DbgElevationEnabled       : 1', ULONG),
        ('DbgVirtEnabled            : 1', ULONG),
        ('DbgInstallerDetectEnabled : 1', ULONG),
        ('DbgLkgEnabled             : 1', ULONG),
        ('DbgDynProcessorEnabled    : 1', ULONG),
        ('DbgConsoleBrokerEnabled   : 1', ULONG),
        ('DbgSecureBootEnabled      : 1', ULONG),
        ('DbgMultiSessionSku        : 1', ULONG),
        ('DbgMultiUsersInSessionSku : 1', ULONG),
        ('DbgStateSeparationEnabled : 1', ULONG),
        ('SpareBits                 : 21', ULONG),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('ReservedTickCountOverlay', ULONG * 3),
        ('TickCountPad', ULONG * 1),
    ]


    DUMMYUNIONNAME3.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYUNIONNAME3._fields_ = [
        ('KSYSTEM_TIME TickCount', volatile),
        ('ULONG64 TickCountQuad', volatile),
        ('DUMMYSTRUCTNAME', DUMMYUNIONNAME3.DUMMYSTRUCTNAME),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('ReservedTickCountOverlay', ULONG * 3),
        ('TickCountPad', ULONG * 1),
    ]


    _Struct_24._fields_ = [
        ('UCHAR QpcBypassEnabled', volatile), # can read the counter directly (bypassing the system call).
        ('QpcShift', UCHAR), # QPC count.
    ]


    ._Struct_24 = _Struct_24
    ._anonymous_ = (
        '_Struct_24',
    )
    ._fields_ = [
        ('QpcData', USHORT),
        ('_Struct_24', ._Struct_24),
    ]


    ._fields_ = [
        ('UCHAR QpcBypassEnabled', volatile), # can read the counter directly (bypassing the system call).
        ('QpcShift', UCHAR), # QPC count.
    ]



        if defined(_MSC_EXTENSIONS):
            pass
        # END IF
        if defined(_MSC_EXTENSIONS):
            pass
        # END IF
    if not defined(__midl) and not defined(MIDL_PASS):
        pass
    # END IF  __midl | MIDL_PASS
    if defined(_MAC):
        pass
    # END IF
    CmResourceTypeMaximum = 8
    class _CM_PCCARD_DEVICE_DATA(ctypes.Structure):
        pass
    _CM_PCCARD_DEVICE_DATA._fields_ = [
        ('Flags', UCHAR),
        ('ErrorCode', UCHAR),
        ('Reserved', USHORT),
        ('BusData', ULONG),
        ('DeviceId', ULONG),
        ('LegacyBaseAddress', ULONG),
        ('IRQMap', UCHAR * 16),
    ]


    CM_PCCARD_DEVICE_DATA = _CM_PCCARD_DEVICE_DATA
    PCM_PCCARD_DEVICE_DATA = POINTER(_CM_PCCARD_DEVICE_DATA)


    PCCARD_MAP_ERROR = 0x01
    PCCARD_DEVICE_PCI = 0x10
    PCCARD_SCAN_DISABLED = 0x01
    PCCARD_MAP_ZERO = 0x02
    PCCARD_NO_TIMER = 0x03
    PCCARD_NO_PIC = 0x04
    PCCARD_NO_LEGACY_BASE = 0x05
    PCCARD_DUP_LEGACY_BASE = 0x06
    PCCARD_NO_CONTROLLERS = 0x07

    if not defined(_ARC_DDK_):
        _ARC_DDK_ = 1


        class _CONFIGURATION_TYPE(ENUM):
            ArcSystem = 1
            CentralProcessor = 2
            FloatingPointProcessor = 3
            PrimaryIcache = 4
            PrimaryDcache = 5
            SecondaryIcache = 6
            SecondaryDcache = 7
            SecondaryCache = 8
            EisaAdapter = 9
            TcAdapter = 10
            ScsiAdapter = 11
            DtiAdapter = 12
            MultiFunctionAdapter = 13
            DiskController = 14
            TapeController = 15
            CdromController = 16
            WormController = 17
            SerialController = 18
            NetworkController = 19
            DisplayController = 20
            ParallelController = 21
            PointerController = 22
            KeyboardController = 23
            AudioController = 24
            OtherController = 25
            DiskPeripheral = 26
            FloppyDiskPeripheral = 27
            TapePeripheral = 28
            ModemPeripheral = 29
            MonitorPeripheral = 30
            PrinterPeripheral = 31
            PointerPeripheral = 32
            KeyboardPeripheral = 33
            TerminalPeripheral = 34
            OtherPeripheral = 35
            LinePeripheral = 36
            NetworkPeripheral = 37
            SystemMemory = 38
            DockingInformation = 39
            RealModeIrqRoutingTable = 40
            RealModePCIEnumeration = 41
            MaximumType = 42


        CONFIGURATION_TYPE = _CONFIGURATION_TYPE
        PCONFIGURATION_TYPE = POINTER(_CONFIGURATION_TYPE)
    # END IF   _ARC_DDK_
    if not (defined(_X86_) or defined(_AMD64_) or defined(_ARM_) or defined(_ARM64_)):
        pass
    # END IF
    if (NTDDI_VERSION < NTDDI_WIN7) or defined(_X86_) or not defined(NT_PROCESSOR_GROUPS):
        SINGLE_GROUP_LEGACY_API = 1
    # END IF

    if defined(_X86_) or defined(_AMD64_):
        PAUSE_PROCESSOR = YieldProcessor();
elif defined(_ARM_) or defined(_ARM64_):
        PAUSE_PROCESSOR = __yield();
    # END IF

    if (NTDDI_VERSION >= NTDDI_WS03SP1):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K) and defined(SINGLE_GROUP_LEGACY_API):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    MAXIMUM_EXPANSION_SIZE = KERNEL_LARGE_STACK_SIZE - (PAGE_SIZE / 2)

    if (NTDDI_VERSION >= NTDDI_WS03SP1):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_VISTA):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WS03SP1):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WS03SP1):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
        if (NTDDI_VERSION >= NTDDI_WS03):
            pass
        # END IF
    if not defined(_ARM64_):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K) and defined(SINGLE_GROUP_LEGACY_API):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_VISTA) and defined(SINGLE_GROUP_LEGACY_API):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_LONGHORN) and defined(SINGLE_GROUP_LEGACY_API):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    CP_GET_SUCCESS = 0
    CP_GET_NODATA = 1
    CP_GET_ERROR = 2

    if defined(POOL_TAGGING):


def ExFreePool(a):
    return ExFreePoolWithTag a,0
    # END IF
    PROTECTED_POOL = 0x0

    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    class _ZONE_SEGMENT_HEADER(ctypes.Structure):
        pass
    _ZONE_SEGMENT_HEADER._fields_ = [
        ('SegmentList', SINGLE_LIST_ENTRY),
        ('Reserved', PVOID),
    ]


    ZONE_SEGMENT_HEADER = _ZONE_SEGMENT_HEADER
    PZONE_SEGMENT_HEADER = POINTER(_ZONE_SEGMENT_HEADER)


    class _ZONE_HEADER(ctypes.Structure):
        pass
    _ZONE_HEADER._fields_ = [
        ('FreeList', SINGLE_LIST_ENTRY),
        ('SegmentList', SINGLE_LIST_ENTRY),
        ('BlockSize', ULONG),
        ('TotalSegmentSize', ULONG),
    ]


    ZONE_HEADER = _ZONE_HEADER
    PZONE_HEADER = POINTER(_ZONE_HEADER)


    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if PRAGMA_DEPRECATED_DDK:
        pass
    # END IF


def ExAllocateFromZone(Zone):
    return PVOID(Zone - >FreeList.Next); if ( Zone - >FreeList.Next ) Zone - >FreeList.Next = Zone - >FreeList.Next - >Next

    if PRAGMA_DEPRECATED_DDK:
        pass
    # END IF


def ExFreeToZone(Zone, Block):
    return ((PSINGLE_LIST_ENTRYBlock) - >Next = Zone - >FreeList.Next, Zone - >FreeList.Next = (PSINGLE_LIST_ENTRYBlock), (PSINGLE_LIST_ENTRYBlock) - >Next)

    if PRAGMA_DEPRECATED_DDK:
        pass
    # END IF


def ExIsFullZone(Zone):
    return (Zone - >FreeList.Next == PSINGLE_LIST_ENTRYNULL)

    if PRAGMA_DEPRECATED_DDK:
        pass
    # END IF


def ExInterlockedAllocateFromZone(Zone, Lock):
    return PVOID ExInterlockedPopEntryList( & Zone - >FreeList, Lock)

    if PRAGMA_DEPRECATED_DDK:
        pass
    # END IF


def ExInterlockedFreeToZone(Zone, Block, Lock):
    return ExInterlockedPushEntryList( & Zone - >FreeList, PSINGLE_LIST_ENTRY Block, Lock)

    if PRAGMA_DEPRECATED_DDK:
        pass
    # END IF


def ExIsObjectInFirstZoneSegment(Zone, Object):
    return (BOOLEAN ((PUCHARObject >= PUCHARZone - >SegmentList.Next) and (PUCHARObject < PUCHARZone - >SegmentList.Next + Zone - >TotalSegmentSize)))

    if PRAGMA_DEPRECATED_DDK:
        pass
    # END IF
    ExInitializeResource = ExInitializeResourceLite
    ExAcquireResourceShared = ExAcquireResourceSharedLite
    ExAcquireResourceExclusive = ExAcquireResourceExclusiveLite
    ExReleaseResourceForThread = ExReleaseResourceForThreadLite
    ExConvertExclusiveToShared = ExConvertExclusiveToSharedLite
    ExDeleteResource = ExDeleteResourceLite
    ExIsResourceAcquiredExclusive = ExIsResourceAcquiredExclusiveLite
    ExIsResourceAcquiredShared = ExIsResourceAcquiredSharedLite
    ExIsResourceAcquired = ExIsResourceAcquiredSharedLite

    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    EVENT_INCREMENT = 1
    IO_NO_INCREMENT = 0
    IO_CD_ROM_INCREMENT = 1
    IO_DISK_INCREMENT = 1
    IO_KEYBOARD_INCREMENT = 6
    IO_MAILSLOT_INCREMENT = 2
    IO_MOUSE_INCREMENT = 6
    IO_NAMED_PIPE_INCREMENT = 2
    IO_NETWORK_INCREMENT = 2
    IO_PARALLEL_INCREMENT = 1
    IO_SERIAL_INCREMENT = 2
    IO_SOUND_INCREMENT = 8
    IO_VIDEO_INCREMENT = 1
    SEMAPHORE_INCREMENT = 1

    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    class _PHYSICAL_MEMORY_RANGE(ctypes.Structure):
        pass
    _PHYSICAL_MEMORY_RANGE._fields_ = [
        ('BaseAddress', PHYSICAL_ADDRESS),
        ('NumberOfBytes', LARGE_INTEGER),
    ]


    PHYSICAL_MEMORY_RANGE = _PHYSICAL_MEMORY_RANGE
    PPHYSICAL_MEMORY_RANGE = POINTER(_PHYSICAL_MEMORY_RANGE)


    if (NTDDI_VERSION >= NTDDI_WIN2K):
        if (NTDDI_VERSION >= NTDDI_WIN10_RS2):
            MM_ADD_PHYSICAL_MEMORY_ALREADY_ZEROED = 0x1
        # END IF
    # END IF


    class _MM_ROTATE_DIRECTION(ENUM):
        MmToFrameBuffer = 1
        MmToFrameBufferNoCopy = 2
        MmToRegularMemory = 3
        MmToRegularMemoryNoCopy = 4
        MmMaximumRotateDirection = 5


    MM_ROTATE_DIRECTION = _MM_ROTATE_DIRECTION
    PMM_ROTATE_DIRECTION = POINTER(_MM_ROTATE_DIRECTION)
    if (NTDDI_VERSION >= NTDDI_VISTA):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        MM_SYSTEM_PARTITION_OBJECT = NULL
        MM_CURRENT_PROCESS_PARTITION_OBJECT = (PVOID) MAXULONG_PTR
    # END IF

    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINBLUE):
        class _MM_COPY_ADDRESS(ctypes.Structure):
            pass
        _Union_12._fields_ = [
            ('VirtualAddress', PVOID),
            ('PhysicalAddress', PHYSICAL_ADDRESS),
        ]


        _MM_COPY_ADDRESS._Union_12 = _Union_12
        _MM_COPY_ADDRESS._anonymous_ = (
            '_Union_12',
        )
        _MM_COPY_ADDRESS._fields_ = [
            ('_Union_12', _MM_COPY_ADDRESS._Union_12),
        ]


        MM_COPY_ADDRESS = _MM_COPY_ADDRESS
        PMMCOPY_ADDRESS = POINTER(_MM_COPY_ADDRESS)


        ._fields_ = [
            ('VirtualAddress', PVOID),
            ('PhysicalAddress', PHYSICAL_ADDRESS),
        ]


        MM_COPY_MEMORY_PHYSICAL = 0x1
        MM_COPY_MEMORY_VIRTUAL = 0x2
    # END IF

    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        MM_ANY_NODE_OK = 0x80000000
    # END IF

    if (NTDDI_VERSION >= NTDDI_VISTA):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        MM_SYSTEM_VIEW_EXCEPTIONS_FOR_INPAGE_ERRORS = 0x1
    # END IF

    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WS03):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if not defined(_PSGETCURRENTTHREAD_):
        _PSGETCURRENTTHREAD_ = 1
    # END IF
    class _PS_CREATE_NOTIFY_INFO(ctypes.Structure):
        pass
    _Struct_26._fields_ = [
        ('ULONG FileOpenNameAvailable : 1', _In_),
        ('ULONG IsSubsystemProcess : 1', _In_),
        ('ULONG Reserved : 30', _In_),
    ]


    _Struct_25._Struct_26 = _Struct_26
    _Struct_25._anonymous_ = (
        '_Struct_26',
    )
    _Struct_25._fields_ = [
        ('ULONG Flags', _In_),
        ('_Struct_26', _Struct_25._Struct_26),
    ]


    _PS_CREATE_NOTIFY_INFO._Struct_25 = _Struct_25
    _PS_CREATE_NOTIFY_INFO._anonymous_ = (
        '_Struct_25',
    )
    _PS_CREATE_NOTIFY_INFO._fields_ = [
        ('SIZE_T Size', _In_),
        ('_Struct_25', _PS_CREATE_NOTIFY_INFO._Struct_25),
        ('HANDLE ParentProcessId', _In_),
        ('CLIENT_ID CreatingThreadId', _In_),
        ('struct _FILE_OBJECT *FileObject', _Inout_),
        ('PCUNICODE_STRING ImageFileName', _In_),
        ('PCUNICODE_STRING CommandLine', _In_opt_),
        ('NTSTATUS CreationStatus', _Inout_),
    ]


    PS_CREATE_NOTIFY_INFO = _PS_CREATE_NOTIFY_INFO
    PPS_CREATE_NOTIFY_INFO = POINTER(_PS_CREATE_NOTIFY_INFO)


    _Struct_26._fields_ = [
        ('ULONG FileOpenNameAvailable : 1', _In_),
        ('ULONG IsSubsystemProcess : 1', _In_),
        ('ULONG Reserved : 30', _In_),
    ]


    ._Struct_26 = _Struct_26
    ._anonymous_ = (
        '_Struct_26',
    )
    ._fields_ = [
        ('ULONG Flags', _In_),
        ('_Struct_26', ._Struct_26),
    ]


    ._fields_ = [
        ('ULONG FileOpenNameAvailable : 1', _In_),
        ('ULONG IsSubsystemProcess : 1', _In_),
        ('ULONG Reserved : 30', _In_),
    ]



    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_VISTASP1):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN10_RS2):
        class _PSCREATEPROCESSNOTIFYTYPE(ENUM):
            PsCreateProcessNotifySubsystems = 0


        PSCREATEPROCESSNOTIFYTYPE = _PSCREATEPROCESSNOTIFYTYPE
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINTHRESHOLD):
        class _PSCREATETHREADNOTIFYTYPE(ENUM):
            PsCreateThreadNotifyNonSystem = 0
            PsCreateThreadNotifySubsystems = 1


        PSCREATETHREADNOTIFYTYPE = _PSCREATETHREADNOTIFYTYPE
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    IMAGE_ADDRESSING_MODE_32BIT = 3
    class _IMAGE_INFO(ctypes.Structure):
        pass
    _Struct_28._fields_ = [
        ('ImageAddressingMode  : 8', ULONG), # Code addressing mode
        ('SystemModeImage      : 1', ULONG), # System mode image
        ('ImageMappedToAllPids : 1', ULONG), # Image mapped into all processes
        ('ExtendedInfoPresent  : 1', ULONG), # IMAGE_INFO_EX available
        ('MachineTypeMismatch  : 1', ULONG), # Architecture type mismatch
        ('ImageSignatureLevel  : 4', ULONG), # Signature level
        ('ImageSignatureType   : 3', ULONG), # Signature type
        ('ImagePartialMap      : 1', ULONG), # Nonzero if entire image is not mapped
        ('Reserved             : 12', ULONG),
    ]


    _Struct_27._Struct_28 = _Struct_28
    _Struct_27._anonymous_ = (
        '_Struct_28',
    )
    _Struct_27._fields_ = [
        ('Properties', ULONG),
        ('_Struct_28', _Struct_27._Struct_28),
    ]


    _IMAGE_INFO._Struct_27 = _Struct_27
    _IMAGE_INFO._anonymous_ = (
        '_Struct_27',
    )
    _IMAGE_INFO._fields_ = [
        ('_Struct_27', _IMAGE_INFO._Struct_27),
        ('ImageBase', PVOID),
        ('ImageSelector', ULONG),
        ('ImageSize', SIZE_T),
        ('ImageSectionNumber', ULONG),
    ]


    IMAGE_INFO = _IMAGE_INFO
    PIMAGE_INFO = POINTER(_IMAGE_INFO)


    _Struct_28._fields_ = [
        ('ImageAddressingMode  : 8', ULONG), # Code addressing mode
        ('SystemModeImage      : 1', ULONG), # System mode image
        ('ImageMappedToAllPids : 1', ULONG), # Image mapped into all processes
        ('ExtendedInfoPresent  : 1', ULONG), # IMAGE_INFO_EX available
        ('MachineTypeMismatch  : 1', ULONG), # Architecture type mismatch
        ('ImageSignatureLevel  : 4', ULONG), # Signature level
        ('ImageSignatureType   : 3', ULONG), # Signature type
        ('ImagePartialMap      : 1', ULONG), # Nonzero if entire image is not mapped
        ('Reserved             : 12', ULONG),
    ]


    ._Struct_28 = _Struct_28
    ._anonymous_ = (
        '_Struct_28',
    )
    ._fields_ = [
        ('Properties', ULONG),
        ('_Struct_28', ._Struct_28),
    ]


    ._fields_ = [
        ('ImageAddressingMode  : 8', ULONG), # Code addressing mode
        ('SystemModeImage      : 1', ULONG), # System mode image
        ('ImageMappedToAllPids : 1', ULONG), # Image mapped into all processes
        ('ExtendedInfoPresent  : 1', ULONG), # IMAGE_INFO_EX available
        ('MachineTypeMismatch  : 1', ULONG), # Architecture type mismatch
        ('ImageSignatureLevel  : 4', ULONG), # Signature level
        ('ImageSignatureType   : 3', ULONG), # Signature type
        ('ImagePartialMap      : 1', ULONG), # Nonzero if entire image is not mapped
        ('Reserved             : 12', ULONG),
    ]


    class _IMAGE_INFO_EX(ctypes.Structure):
        pass
    _IMAGE_INFO_EX._fields_ = [
        ('Size', SIZE_T),
        ('ImageInfo', IMAGE_INFO),
        ('FileObject', POINTER(_FILE_OBJECT)),
    ]


    IMAGE_INFO_EX = _IMAGE_INFO_EX
    PIMAGE_INFO_EX = POINTER(_IMAGE_INFO_EX)


    FileObject = POINTER(_FILE_OBJECT)



    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN10_RS3):
        PS_IMAGE_NOTIFY_CONFLICTING_ARCHITECTURE = 0x1
    # END IF

    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_VISTA):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN10_RS2):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WS03):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINTHRESHOLD):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WS03SP1):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        SILO_MONITOR_REGISTRATION_VERSION = 1
        class _SILO_MONITOR_REGISTRATION(ctypes.Structure):
            pass
        _Union_13._fields_ = [
            ('DriverObjectName', PUNICODE_STRING),
            ('ComponentName', PUNICODE_STRING),
        ]


        _SILO_MONITOR_REGISTRATION._Union_13 = _Union_13
        _SILO_MONITOR_REGISTRATION._anonymous_ = (
            '_Union_13',
        )
        _SILO_MONITOR_REGISTRATION._fields_ = [
            ('Version', UCHAR),
            ('MonitorHost', BOOLEAN),
            ('MonitorExistingSilos', BOOLEAN),
            ('Reserved', UCHAR * 5),
            ('_Union_13', _SILO_MONITOR_REGISTRATION._Union_13),
            ('CreateCallback', SILO_MONITOR_CREATE_CALLBACK),
            ('TerminateCallback', SILO_MONITOR_TERMINATE_CALLBACK),
        ]


        SILO_MONITOR_REGISTRATION = _SILO_MONITOR_REGISTRATION
        PSILO_MONITOR_REGISTRATION = POINTER(_SILO_MONITOR_REGISTRATION)


        ._fields_ = [
            ('DriverObjectName', PUNICODE_STRING),
            ('ComponentName', PUNICODE_STRING),
        ]


        PS_INVALID_SILO_CONTEXT_SLOT = 0xFFFFFFFF
    # END IF

    if (NTDDI_VERSION >= NTDDI_WIN10_RS3):
        pass
    # END IF
    IRP_MN_QUERY_DIRECTORY = 0x01
    IRP_MN_NOTIFY_CHANGE_DIRECTORY = 0x02
    IRP_MN_NOTIFY_CHANGE_DIRECTORY_EX = 0x03
    IRP_MN_USER_FS_REQUEST = 0x00
    IRP_MN_MOUNT_VOLUME = 0x01
    IRP_MN_VERIFY_VOLUME = 0x02
    IRP_MN_LOAD_FILE_SYSTEM = 0x03
    IRP_MN_TRACK_LINK = 0x04
    IRP_MN_KERNEL_CALL = 0x04
    IRP_MN_LOCK = 0x01
    IRP_MN_UNLOCK_SINGLE = 0x02
    IRP_MN_UNLOCK_ALL = 0x03
    IRP_MN_UNLOCK_ALL_BY_KEY = 0x04
    IRP_MN_FLUSH_AND_PURGE = 0x01

    if (NTDDI_VERSION >= NTDDI_WIN8):
        IRP_MN_FLUSH_DATA_ONLY = 0x02
        IRP_MN_FLUSH_NO_SYNC = 0x03
    # END IF

    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        IRP_MN_FLUSH_DATA_SYNC_ONLY = 0x04
    # END IF
    IRP_MN_NORMAL = 0x00
    IRP_MN_DPC = 0x01
    IRP_MN_MDL = 0x02
    IRP_MN_COMPLETE = 0x04
    IRP_MN_COMPRESSED = 0x08
    IRP_MN_MDL_DPC = IRP_MN_MDL | IRP_MN_DPC
    IRP_MN_COMPLETE_MDL = IRP_MN_COMPLETE | IRP_MN_MDL
    IRP_MN_COMPLETE_MDL_DPC = IRP_MN_COMPLETE_MDL | IRP_MN_DPC
    IRP_MN_QUERY_LEGACY_BUS_INFORMATION = 0x18
    IO_CHECK_CREATE_PARAMETERS = 0x0200
    IO_ATTACH_DEVICE = 0x0400
    IO_IGNORE_SHARE_ACCESS_CHECK = 0x0800


    class _IO_QUERY_DEVICE_DATA_FORMAT(ENUM):
        IoQueryDeviceIdentifier = 0
        IoQueryDeviceConfigurationData = 1
        IoQueryDeviceComponentInformation = 2
        IoQueryDeviceMaxData = 3


    IO_QUERY_DEVICE_DATA_FORMAT = _IO_QUERY_DEVICE_DATA_FORMAT
    PIO_QUERY_DEVICE_DATA_FORMAT = POINTER(_IO_QUERY_DEVICE_DATA_FORMAT)
    class _CONTROLLER_OBJECT(ctypes.Structure):
        pass
    _CONTROLLER_OBJECT._fields_ = [
        ('Type', CSHORT),
        ('Size', CSHORT),
        ('ControllerExtension', PVOID),
        ('DeviceWaitQueue', KDEVICE_QUEUE),
        ('Spare1', ULONG),
        ('Spare2', LARGE_INTEGER),
    ]


    CONTROLLER_OBJECT = _CONTROLLER_OBJECT
    PCONTROLLER_OBJECT = POINTER(_CONTROLLER_OBJECT)


    DO_VERIFY_VOLUME = 0x00000002
    DO_BUFFERED_IO = 0x00000004
    DO_EXCLUSIVE = 0x00000008
    DO_DIRECT_IO = 0x00000010
    DO_MAP_IO_BUFFER = 0x00000020
    DO_DEVICE_HAS_NAME = 0x00000040
    DO_DEVICE_INITIALIZING = 0x00000080
    DO_SYSTEM_BOOT_PARTITION = 0x00000100
    DO_LONG_TERM_REQUESTS = 0x00000200
    DO_NEVER_LAST_DEVICE = 0x00000400
    DO_SHUTDOWN_REGISTERED = 0x00000800
    DO_BUS_ENUMERATED_DEVICE = 0x00001000
    DO_POWER_PAGABLE = 0x00002000
    DO_POWER_INRUSH = 0x00004000
    DO_LOW_PRIORITY_FILESYSTEM = 0x00010000
    DO_SUPPORTS_TRANSACTIONS = 0x00040000
    DO_FORCE_NEITHER_IO = 0x00080000
    DO_VOLUME_DEVICE_OBJECT = 0x00100000
    DO_SYSTEM_SYSTEM_PARTITION = 0x00200000
    DO_SYSTEM_CRITICAL_PARTITION = 0x00400000
    DO_DISALLOW_EXECUTE = 0x00800000
    DO_DEVICE_TO_BE_RESET = 0x04000000
    DO_DEVICE_IRP_REQUIRES_EXTENSION = 0x08000000
    DO_DAX_VOLUME = 0x10000000
    DRVO_REINIT_REGISTERED = 0x00000008
    DRVO_INITIALIZED = 0x00000010
    DRVO_BOOTREINIT_REGISTERED = 0x00000020
    DRVO_LEGACY_RESOURCES = 0x00000040
    class _CONFIGURATION_INFORMATION(ctypes.Structure):
        pass
    _CONFIGURATION_INFORMATION._fields_ = [
        ('DiskCount', ULONG), # Count of hard disks thus far
        ('FloppyCount', ULONG), # Count of floppy disks thus far
        ('CdRomCount', ULONG), # Count of CD - ROM drives thus far
        ('TapeCount', ULONG), # Count of tape drives thus far
        ('ScsiPortCount', ULONG), # Count of SCSI port adapters thus far
        ('SerialCount', ULONG), # Count of serial devices thus far
        ('ParallelCount', ULONG), # Count of parallel devices thus far
        ('AtDiskPrimaryAddressClaimed', BOOLEAN), # 0x1F0 - 0x1FF
        ('AtDiskSecondaryAddressClaimed', BOOLEAN), # 0x170 - 0x17F
        ('Version', ULONG), # Use the structure size as the version.
        ('MediumChangerCount', ULONG), # new devices have been found and will be supported.
    ]


    CONFIGURATION_INFORMATION = _CONFIGURATION_INFORMATION
    PCONFIGURATION_INFORMATION = POINTER(_CONFIGURATION_INFORMATION)



        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
    if not (defined(USE_DMA_MACROS) and (defined(_NTDDK_) or defined(_NTDRIVER_)) or defined(_WDM_INCLUDED_)):
        pass
    # END IF   not (defined(USE_DMA_MACROS) and (defined(_NTDDK_) or defined(_NTDRIVER_)) or defined(_WDM_INCLUDED_))
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF


def IoAssignArcName(ArcName, DeviceName):
    return (IoCreateSymbolicLink( ArcName, DeviceName ))

    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF


def IoDeassignArcName(ArcName):
    return (IoDeleteSymbolicLink( ArcName ))

    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINTHRESHOLD):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WS03SP1):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    class _DISK_SIGNATURE(ctypes.Structure):
        pass
    Mbr._fields_ = [
        ('Signature', ULONG),
        ('CheckSum', ULONG),
    ]


    _Struct_29.Mbr = Mbr
    Gpt._fields_ = [
        ('DiskId', GUID),
    ]


    _Struct_29.Gpt = Gpt
    _Struct_29._fields_ = [
        ('Mbr', _Struct_29.Mbr),
        ('Gpt', _Struct_29.Gpt),
    ]


    _DISK_SIGNATURE._Struct_29 = _Struct_29
    _DISK_SIGNATURE._anonymous_ = (
        '_Struct_29',
    )
    _DISK_SIGNATURE._fields_ = [
        ('PartitionStyle', ULONG),
        ('_Struct_29', _DISK_SIGNATURE._Struct_29),
    ]


    DISK_SIGNATURE = _DISK_SIGNATURE
    PDISK_SIGNATURE = POINTER(_DISK_SIGNATURE)


    Mbr._fields_ = [
        ('Signature', ULONG),
        ('CheckSum', ULONG),
    ]


    .Mbr = Mbr
    Gpt._fields_ = [
        ('DiskId', GUID),
    ]


    .Gpt = Gpt
    ._fields_ = [
        ('Mbr', .Mbr),
        ('Gpt', .Gpt),
    ]


    Mbr._fields_ = [
        ('Signature', ULONG),
        ('CheckSum', ULONG),
    ]


    Gpt._fields_ = [
        ('DiskId', GUID),
    ]


    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN10):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN10):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        class _IO_FOEXT_SILO_PARAMETERS(ctypes.Structure):
            pass
        _Struct_31._fields_ = [
            ('HasHardReference : 1', ULONG),
            ('SpareFlags : 31', ULONG),
        ]


        _Struct_30._Struct_31 = _Struct_31
        _Struct_30._anonymous_ = (
            '_Struct_31',
        )
        _Struct_30._fields_ = [
            ('_Struct_31', _Struct_30._Struct_31),
            ('Flags', ULONG),
        ]


        _IO_FOEXT_SILO_PARAMETERS._Struct_30 = _Struct_30
        _IO_FOEXT_SILO_PARAMETERS._anonymous_ = (
            '_Struct_30',
        )
        _IO_FOEXT_SILO_PARAMETERS._fields_ = [
            ('Length', ULONG),
            ('_Struct_30', _IO_FOEXT_SILO_PARAMETERS._Struct_30),
            ('SiloContext', PESILO),
        ]


        IO_FOEXT_SILO_PARAMETERS = _IO_FOEXT_SILO_PARAMETERS
        PIO_FOEXT_SILO_PARAMETERS = POINTER(_IO_FOEXT_SILO_PARAMETERS)


        _Struct_31._fields_ = [
            ('HasHardReference : 1', ULONG),
            ('SpareFlags : 31', ULONG),
        ]


        ._Struct_31 = _Struct_31
        ._anonymous_ = (
            '_Struct_31',
        )
        ._fields_ = [
            ('_Struct_31', ._Struct_31),
            ('Flags', ULONG),
        ]


        ._fields_ = [
            ('HasHardReference : 1', ULONG),
            ('SpareFlags : 31', ULONG),
        ]


    # END IF
    class _TXN_PARAMETER_BLOCK(ctypes.Structure):
        pass
    _TXN_PARAMETER_BLOCK._fields_ = [
        ('Length', USHORT), # ctypes.sizeof( TXN_PARAMETER_BLOCK )
        ('TxFsContext', USHORT), # this is mini version of the requested file
        ('TransactionObject', PVOID), # referenced pointer to KTRANSACTION
    ]


    TXN_PARAMETER_BLOCK = _TXN_PARAMETER_BLOCK
    PTXN_PARAMETER_BLOCK = POINTER(_TXN_PARAMETER_BLOCK)


    TXF_MINIVERSION_DEFAULT_VIEW = 0xFFFE

    if (NTDDI_VERSION >= NTDDI_VISTA):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINTHRESHOLD):
        class _CREATE_USER_PROCESS_ECP_CONTEXT(ctypes.Structure):
            pass
        _CREATE_USER_PROCESS_ECP_CONTEXT._fields_ = [
            ('Size', USHORT), # This must be set to the size of this structure.
            ('Reserved', USHORT), # This must be set to zero.
            ('AccessToken', PACCESS_TOKEN), # The access token of the process that is getting created.
        ]


        CREATE_USER_PROCESS_ECP_CONTEXT = _CREATE_USER_PROCESS_ECP_CONTEXT
        PCREATE_USER_PROCESS_ECP_CONTEXT = POINTER(_CREATE_USER_PROCESS_ECP_CONTEXT)


    # END IF   NTDDI_VERSION >= NTDDI_WINTHRESHOLD
    if (NTDDI_VERSION >= NTDDI_WIN7):
        POPLOCK_KEY_ECP_CONTEXT = POINTER(_OPLOCK_KEY_ECP_CONTEXT)


    # END IF   NTDDI_VERSION >= NTDDI_WIN7
    if (NTDDI_VERSION >= NTDDI_WIN8):
        class _OPLOCK_KEY_CONTEXT(ctypes.Structure):
            pass
        _OPLOCK_KEY_CONTEXT._fields_ = [
            ('Version', USHORT), # OPLOCK_KEY_VERSION_*
            ('Flags', USHORT), # OPLOCK_KEY_FLAG_*
            ('ParentOplockKey', GUID),
            ('TargetOplockKey', GUID),
            ('Reserved', ULONG),
        ]


        OPLOCK_KEY_CONTEXT = _OPLOCK_KEY_CONTEXT
        POPLOCK_KEY_CONTEXT = POINTER(_OPLOCK_KEY_CONTEXT)


        OPLOCK_KEY_VERSION_WIN7 = 0x0001
        OPLOCK_KEY_VERSION_WIN8 = 0x0002
        OPLOCK_KEY_FLAG_PARENT_KEY = 0x0001
        OPLOCK_KEY_FLAG_TARGET_KEY = 0x0002
    # END IF   NTDDI_VERSION >= NTDDI_WIN8
    class _IO_DRIVER_CREATE_CONTEXT(ctypes.Structure):
        pass
    _IO_DRIVER_CREATE_CONTEXT._fields_ = [
        ('Size', CSHORT),
        ('ExtraCreateParameter', POINTER(_ECP_LIST)),
        ('DeviceObjectHint', PVOID),
        ('TxnParameters', PTXN_PARAMETER_BLOCK),
            ('SiloContext', PESILO),
    ]


    IO_DRIVER_CREATE_CONTEXT = _IO_DRIVER_CREATE_CONTEXT
    PIO_DRIVER_CREATE_CONTEXT = POINTER(_IO_DRIVER_CREATE_CONTEXT)


    ExtraCreateParameter = POINTER(_ECP_LIST)



    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        pass
    # END IF


def IO_DRIVER_CREATE_CONTEXT_IS_MIN_SIZE(DriverContext):
    return (DriverContext - >Size >= (FIELD_OFFSETIO_DRIVER_CREATE_CONTEXT, TxnParameters + ctypes.sizeof(DriverContext - >TxnParameters)))


def IO_DRIVER_CREATE_CONTEXT_CONTAINS_SILO_CONTEXT(DriverContext):
    return (DriverContext - >Size >= (FIELD_OFFSETIO_DRIVER_CREATE_CONTEXT, SiloContext + ctypes.sizeof(DriverContext - >SiloContext)))

    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        IO_USE_AMBIENT_SILO = (PESILO)1
    # END IF

    if (NTDDI_VERSION >= NTDDI_WIN10_RS1):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_VISTA):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN10_RS2):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINXP):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2KSP3):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2KSP3):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_VISTA):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WS03):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        BDCB_IMAGEFLAGS_FAILED_CODE_INTEGRITY = 1UL << 0


        class _BDCB_CALLBACK_TYPE(ENUM):
            BdCbStatusUpdate = 1
            BdCbInitializeImage = 2


        BDCB_CALLBACK_TYPE = _BDCB_CALLBACK_TYPE
        PBDCB_CALLBACK_TYPE = POINTER(_BDCB_CALLBACK_TYPE)
        class _BDCB_CLASSIFICATION(ENUM):
            BdCbClassificationUnknownImage = 1
            BdCbClassificationKnownGoodImage = 2
            BdCbClassificationKnownBadImage = 3
            BdCbClassificationKnownBadImageBootCritical = 4
            BdCbClassificationEnd = 5


        BDCB_CLASSIFICATION = _BDCB_CLASSIFICATION
        PBDCB_CLASSIFICATION = POINTER(_BDCB_CLASSIFICATION)
        class _BDCB_STATUS_UPDATE_TYPE(ENUM):
            BdCbStatusPrepareForDependencyLoad = 1
            BdCbStatusPrepareForDriverLoad = 2
            BdCbStatusPrepareForUnload = 3


        BDCB_STATUS_UPDATE_TYPE = _BDCB_STATUS_UPDATE_TYPE
        PBDCB_STATUS_UPDATE_TYPE = POINTER(_BDCB_STATUS_UPDATE_TYPE)
        class _BDCB_STATUS_UPDATE_CONTEXT(ctypes.Structure):
            pass
        _BDCB_STATUS_UPDATE_CONTEXT._fields_ = [
            ('StatusType', BDCB_STATUS_UPDATE_TYPE),
        ]


        BDCB_STATUS_UPDATE_CONTEXT = _BDCB_STATUS_UPDATE_CONTEXT
        PBDCB_STATUS_UPDATE_CONTEXT = POINTER(_BDCB_STATUS_UPDATE_CONTEXT)


        class _BDCB_IMAGE_INFORMATION(ctypes.Structure):
            pass
        _BDCB_IMAGE_INFORMATION._fields_ = [
            ('Classification', BDCB_CLASSIFICATION),
            ('ImageFlags', ULONG),
            ('ImageName', UNICODE_STRING),
            ('RegistryPath', UNICODE_STRING),
            ('CertificatePublisher', UNICODE_STRING),
            ('CertificateIssuer', UNICODE_STRING),
            ('ImageHash', PVOID),
            ('CertificateThumbprint', PVOID),
            ('ImageHashAlgorithm', ULONG),
            ('ThumbprintHashAlgorithm', ULONG),
            ('ImageHashLength', ULONG),
            ('CertificateThumbprintLength', ULONG),
        ]


        BDCB_IMAGE_INFORMATION = _BDCB_IMAGE_INFORMATION
        PBDCB_IMAGE_INFORMATION = POINTER(_BDCB_IMAGE_INFORMATION)


    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINBLUE):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN8):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WINBLUE):
        pass
    # END IF
    class _AGP_TARGET_BUS_INTERFACE_STANDARD(ctypes.Structure):
        pass
    _AGP_TARGET_BUS_INTERFACE_STANDARD._fields_ = [
        ('Size', USHORT), # generic interface header
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('SetBusData', PGET_SET_DEVICE_DATA), # config munging routines
        ('GetBusData', PGET_SET_DEVICE_DATA),
        ('CapabilityID', UCHAR), # 2 (AGPv2 host) or new 0xE (AGPv3 bridge)
    ]


    AGP_TARGET_BUS_INTERFACE_STANDARD = _AGP_TARGET_BUS_INTERFACE_STANDARD
    PAGP_TARGET_BUS_INTERFACE_STANDARD = POINTER(_AGP_TARGET_BUS_INTERFACE_STANDARD)


    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    class _PNP_LOCATION_INTERFACE(ctypes.Structure):
        pass
    _PNP_LOCATION_INTERFACE._fields_ = [
        ('Size', USHORT), # generic interface header
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('GetLocationString', PGET_LOCATION_STRING), # interface specific entry
    ]


    PNP_LOCATION_INTERFACE = _PNP_LOCATION_INTERFACE
    PPNP_LOCATION_INTERFACE = POINTER(_PNP_LOCATION_INTERFACE)


    class _ARBITER_ACTION(ENUM):
        ArbiterActionTestAllocation = 1
        ArbiterActionRetestAllocation = 2
        ArbiterActionCommitAllocation = 3
        ArbiterActionRollbackAllocation = 4
        ArbiterActionQueryAllocatedResources = 5
        ArbiterActionWriteReservedResources = 6
        ArbiterActionQueryConflict = 7
        ArbiterActionQueryArbitrate = 8
        ArbiterActionAddReserved = 9
        ArbiterActionBootAllocation = 10


    ARBITER_ACTION = _ARBITER_ACTION
    PARBITER_ACTION = POINTER(_ARBITER_ACTION)
    class _ARBITER_CONFLICT_INFO(ctypes.Structure):
        pass
    _ARBITER_CONFLICT_INFO._fields_ = [
        ('OwningObject', PDEVICE_OBJECT), # The device object owning the device that is causing the conflict
        ('Start', ULONGLONG), # The start of the conflicting range
        ('End', ULONGLONG), # The end of the conflicting range
    ]


    ARBITER_CONFLICT_INFO = _ARBITER_CONFLICT_INFO
    PARBITER_CONFLICT_INFO = POINTER(_ARBITER_CONFLICT_INFO)


    class _ARBITER_TEST_ALLOCATION_PARAMETERS(ctypes.Structure):
        pass
    _ARBITER_TEST_ALLOCATION_PARAMETERS._fields_ = [
        ('PLIST_ENTRY ArbitrationList', _Inout_), # Doubly linked list of ARBITER_LIST_ENTRY's
        ('ULONG AllocateFromCount', _In_), # The size of the AllocateFrom array
        ('PCM_PARTIAL_RESOURCE_DESCRIPTOR AllocateFrom', _In_), # to the arbiter for it to arbitrate
    ]


    ARBITER_TEST_ALLOCATION_PARAMETERS = _ARBITER_TEST_ALLOCATION_PARAMETERS
    PARBITER_TEST_ALLOCATION_PARAMETERS = POINTER(_ARBITER_TEST_ALLOCATION_PARAMETERS)


    class _ARBITER_RETEST_ALLOCATION_PARAMETERS(ctypes.Structure):
        pass
    _ARBITER_RETEST_ALLOCATION_PARAMETERS._fields_ = [
        ('PLIST_ENTRY ArbitrationList', _Inout_), # Doubly linked list of ARBITER_LIST_ENTRY's
        ('ULONG AllocateFromCount', _In_), # The size of the AllocateFrom array
        ('PCM_PARTIAL_RESOURCE_DESCRIPTOR AllocateFrom', _In_), # to the arbiter for it to arbitrate
    ]


    ARBITER_RETEST_ALLOCATION_PARAMETERS = _ARBITER_RETEST_ALLOCATION_PARAMETERS
    PARBITER_RETEST_ALLOCATION_PARAMETERS = POINTER(_ARBITER_RETEST_ALLOCATION_PARAMETERS)


    class _ARBITER_BOOT_ALLOCATION_PARAMETERS(ctypes.Structure):
        pass
    _ARBITER_BOOT_ALLOCATION_PARAMETERS._fields_ = [
        ('PLIST_ENTRY ArbitrationList', _Inout_), # Doubly linked list of ARBITER_LIST_ENTRY's
    ]


    ARBITER_BOOT_ALLOCATION_PARAMETERS = _ARBITER_BOOT_ALLOCATION_PARAMETERS
    PARBITER_BOOT_ALLOCATION_PARAMETERS = POINTER(_ARBITER_BOOT_ALLOCATION_PARAMETERS)


    class _ARBITER_QUERY_ALLOCATED_RESOURCES_PARAMETERS(ctypes.Structure):
        pass
    _ARBITER_QUERY_ALLOCATED_RESOURCES_PARAMETERS._fields_ = [
        ('PCM_PARTIAL_RESOURCE_LIST *AllocatedResources', _Out_), # The resources that are currently allocated
    ]


    ARBITER_QUERY_ALLOCATED_RESOURCES_PARAMETERS = _ARBITER_QUERY_ALLOCATED_RESOURCES_PARAMETERS
    PARBITER_QUERY_ALLOCATED_RESOURCES_PARAMETERS = POINTER(_ARBITER_QUERY_ALLOCATED_RESOURCES_PARAMETERS)


    class _ARBITER_QUERY_CONFLICT_PARAMETERS(ctypes.Structure):
        pass
    _ARBITER_QUERY_CONFLICT_PARAMETERS._fields_ = [
        ('PDEVICE_OBJECT PhysicalDeviceObject', _In_), # This is the device we are trying to find a conflict for
        ('PIO_RESOURCE_DESCRIPTOR ConflictingResource', _In_), # This is the resource to find the conflict for
        ('PULONG ConflictCount', _Out_), # Number of devices conflicting on the resource
        ('PARBITER_CONFLICT_INFO *Conflicts', _Out_), # Pointer to array describing the conflicting device objects and ranges
    ]


    ARBITER_QUERY_CONFLICT_PARAMETERS = _ARBITER_QUERY_CONFLICT_PARAMETERS
    PARBITER_QUERY_CONFLICT_PARAMETERS = POINTER(_ARBITER_QUERY_CONFLICT_PARAMETERS)


    class _ARBITER_QUERY_ARBITRATE_PARAMETERS(ctypes.Structure):
        pass
    _ARBITER_QUERY_ARBITRATE_PARAMETERS._fields_ = [
        ('PLIST_ENTRY ArbitrationList', _In_), # only one entry
    ]


    ARBITER_QUERY_ARBITRATE_PARAMETERS = _ARBITER_QUERY_ARBITRATE_PARAMETERS
    PARBITER_QUERY_ARBITRATE_PARAMETERS = POINTER(_ARBITER_QUERY_ARBITRATE_PARAMETERS)


    class _ARBITER_ADD_RESERVED_PARAMETERS(ctypes.Structure):
        pass
    _ARBITER_ADD_RESERVED_PARAMETERS._fields_ = [
        ('PDEVICE_OBJECT ReserveDevice', _In_), # only one entry
    ]


    ARBITER_ADD_RESERVED_PARAMETERS = _ARBITER_ADD_RESERVED_PARAMETERS
    PARBITER_ADD_RESERVED_PARAMETERS = POINTER(_ARBITER_ADD_RESERVED_PARAMETERS)


    class _ARBITER_PARAMETERS(ctypes.Structure):
        pass
    Parameters._fields_ = [
        ('TestAllocation', ARBITER_TEST_ALLOCATION_PARAMETERS),
        ('RetestAllocation', ARBITER_RETEST_ALLOCATION_PARAMETERS),
        ('BootAllocation', ARBITER_BOOT_ALLOCATION_PARAMETERS),
        ('QueryAllocatedResources', ARBITER_QUERY_ALLOCATED_RESOURCES_PARAMETERS),
        ('QueryConflict', ARBITER_QUERY_CONFLICT_PARAMETERS),
        ('QueryArbitrate', ARBITER_QUERY_ARBITRATE_PARAMETERS),
        ('AddReserved', ARBITER_ADD_RESERVED_PARAMETERS),
    ]


    _ARBITER_PARAMETERS.Parameters = Parameters
    _ARBITER_PARAMETERS._fields_ = [
        ('Parameters', _ARBITER_PARAMETERS.Parameters),
    ]


    ARBITER_PARAMETERS = _ARBITER_PARAMETERS
    PARBITER_PARAMETERS = POINTER(_ARBITER_PARAMETERS)


    Parameters._fields_ = [
        ('TestAllocation', ARBITER_TEST_ALLOCATION_PARAMETERS),
        ('RetestAllocation', ARBITER_RETEST_ALLOCATION_PARAMETERS),
        ('BootAllocation', ARBITER_BOOT_ALLOCATION_PARAMETERS),
        ('QueryAllocatedResources', ARBITER_QUERY_ALLOCATED_RESOURCES_PARAMETERS),
        ('QueryConflict', ARBITER_QUERY_CONFLICT_PARAMETERS),
        ('QueryArbitrate', ARBITER_QUERY_ARBITRATE_PARAMETERS),
        ('AddReserved', ARBITER_ADD_RESERVED_PARAMETERS),
    ]


    class _ARBITER_REQUEST_SOURCE(ENUM):
        ArbiterRequestUndefined = - 1
        ArbiterRequestLegacyReported = 0
        ArbiterRequestHalReported = 1
        ArbiterRequestLegacyAsINT = 2
        ArbiterRequestPnpDetected = 3
        ArbiterRequestPnpEnumerated = 4


    ARBITER_REQUEST_SOURCE = _ARBITER_REQUEST_SOURCE
    class _ARBITER_RESULT(ENUM):
        ArbiterResultUndefined = - 1
        ArbiterResultSuccess = 0

        # This indicates that the request can never be solved for devices in
        # this list
        ArbiterResultExternalConflict = 1

        # The request was for length zero and thus no translation should be
        # attempted
        ArbiterResultNullRequest = 2


    ARBITER_RESULT = _ARBITER_RESULT
    ARBITER_FLAG_BOOT_CONFIG = 0x00000001
    ARBITER_FLAG_ROOT_ENUM = 0x00000002
    ARBITER_FLAG_OTHER_ENUM = 0x00000004

    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    class _ARBITER_LIST_ENTRY(ctypes.Structure):
        pass
    _ARBITER_LIST_ENTRY._fields_ = [
        ('ListEntry', LIST_ENTRY), # This is a doubly linked list of entries for easy sorting
        ('AlternativeCount', ULONG), # The number of alternative allocation

        # Pointer to an array of resource descriptors for the possible
        # allocations
        ('Alternatives', PIO_RESOURCE_DESCRIPTOR),
        ('PhysicalDeviceObject', PDEVICE_OBJECT), # The device object of the device requesting these resources.
        ('RequestSource', ARBITER_REQUEST_SOURCE), # Indicates where the request came from
        ('Flags', ULONG), # Flags these indicate a variety of things (use ARBITER_FLAG_*)
        ('WorkSpace', LONG_PTR), # the entry is created. The system will not attempt to interpret it.
        ('InterfaceType', INTERFACE_TYPE), # used only for reverse identification.
        ('SlotNumber', ULONG),
        ('BusNumber', ULONG),
        ('Assignment', PCM_PARTIAL_RESOURCE_DESCRIPTOR), # ArbiterActionTestAllocation.

        # This is filled in by the arbiter in response to an
        # ArbiterActionTestAllocation.
        ('SelectedAlternative', PIO_RESOURCE_DESCRIPTOR),

        # This is filled in by the arbiter in response to an
        # ArbiterActionTestAllocation.
        ('Result', ARBITER_RESULT),
    ]


    ARBITER_LIST_ENTRY = _ARBITER_LIST_ENTRY
    PARBITER_LIST_ENTRY = POINTER(_ARBITER_LIST_ENTRY)


    ARBITER_PARTIAL = 0x00000001
    class _ARBITER_INTERFACE(ctypes.Structure):
        pass
    _ARBITER_INTERFACE._fields_ = [
        ('Size', USHORT), # Generic interface header
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('ArbiterHandler', PARBITER_HANDLER), # Entry point to the arbiter
        ('Flags', ULONG), # Other information about the arbiter, use ARBITER_* flags
    ]


    ARBITER_INTERFACE = _ARBITER_INTERFACE
    PARBITER_INTERFACE = POINTER(_ARBITER_INTERFACE)




    class _RESOURCE_TRANSLATION_DIRECTION(ENUM):
        TranslateChildToParent = 1
        TranslateParentToChild = 2


    RESOURCE_TRANSLATION_DIRECTION = _RESOURCE_TRANSLATION_DIRECTION
    class _TRANSLATOR_INTERFACE(ctypes.Structure):
        pass
    _TRANSLATOR_INTERFACE._fields_ = [
        ('Size', USHORT),
        ('Version', USHORT),
        ('Context', PVOID),
        ('InterfaceReference', PINTERFACE_REFERENCE),
        ('InterfaceDereference', PINTERFACE_DEREFERENCE),
        ('TranslateResources', PTRANSLATE_RESOURCE_HANDLER),
        ('TranslateResourceRequirements', PTRANSLATE_RESOURCE_REQUIREMENTS_HANDLER),
    ]


    TRANSLATOR_INTERFACE = _TRANSLATOR_INTERFACE
    PTRANSLATOR_INTERFACE = POINTER(_TRANSLATOR_INTERFACE)


    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if defined(_M_IX86) or defined(_M_AMD64):


def HalGetDmaAlignmentRequirement():
    return 1L
elif defined(_M_ARM) or defined(_M_ARM64):


def HalGetDmaAlignmentRequirement():
    return 1L
    # END IF

    if defined(_ARM_) or defined(_ARM64_):
        pass
    # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
    if not defined(NO_LEGACY_DRIVERS):
        pass
    # END IF   NO_LEGACY_DRIVERS
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
    if not defined(XBOX_SYSTEMOS):
        pass
    # END IF
    if not defined(XBOX_SYSTEMOS):
        if (NTDDI_VERSION >= NTDDI_WIN8):
            class _HAL_DMA_CRASH_DUMP_REGISTER_TYPE(ENUM):
                HalDmaCrashDumpRegisterSet1 = 0
                HalDmaCrashDumpRegisterSet2 = 1
                HalDmaCrashDumpRegisterSetMax = 2


            HAL_DMA_CRASH_DUMP_REGISTER_TYPE = _HAL_DMA_CRASH_DUMP_REGISTER_TYPE
            PHAL_DMA_CRASH_DUMP_REGISTER_TYPE = POINTER(_HAL_DMA_CRASH_DUMP_REGISTER_TYPE)
        # END IF
    # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
    if not defined(NO_LEGACY_DRIVERS):
        pass
    # END IF   NO_LEGACY_DRIVERS
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
    if not defined(NO_LEGACY_DRIVERS):
        pass
    # END IF   NO_LEGACY_DRIVERS
    class _HAL_QUERY_INFORMATION_CLASS(ENUM):
        HalInstalledBusInformation = 1
        HalProfileSourceInformation = 2
        HalInformationClassUnused1 = 3
        HalPowerInformation = 4
        HalProcessorSpeedInformation = 5
        HalCallbackInformation = 6
        HalMapRegisterInformation = 7
        HalMcaLogInformation = 8
        HalFrameBufferCachingInformation = 9
        HalDisplayBiosInformation = 10
        HalProcessorFeatureInformation = 11
        HalNumaTopologyInterface = 12
        HalErrorInformation = 13
        HalCmcLogInformation = 14
        HalCpeLogInformation = 15
        HalQueryMcaInterface = 16
        HalQueryAMLIIllegalIOPortAddresses = 17
        HalQueryMaxHotPlugMemoryAddress = 18
        HalPartitionIpiInterface = 19
        HalPlatformInformation = 20
        HalQueryProfileSourceList = 21
        HalInitLogInformation = 22
        HalFrequencyInformation = 23
        HalProcessorBrandString = 24
        HalHypervisorInformation = 25
        HalPlatformTimerInformation = 26
        HalAcpiAuditInformation = 27
        HalIrtInformation = 28
        HalSecondaryInterruptInformation = 29
        HalParkingPageInformation = 30
        HalNumaRangeTableInformation = 31
        HalChannelTopologyInformation = 32
        HalExternalCacheInformation = 33
        HalQueryDebuggerInformation = 34
        HalFwBootPerformanceInformation = 35
        HalFwS3PerformanceInformation = 36
        HalGetChannelPowerInformation = 37
        HalQueryStateElementInformation = 38
        HalPsciInformation = 39
        HalInterruptControllerInformation = 40
        HalQueryIommuReservedRegionInformation = 41
        HalQueryArmErrataInformation = 42
        HalQueryProcessorEfficiencyInformation = 43
        HalQueryAcpiWakeAlarmSystemPowerStateInformation = 44
        HalQueryProfileNumberOfCounters = 45
        HalQueryHyperlaunchEntrypoint = 46
        HalHardwareWatchdogInformation = 47
        HalDmaRemappingInformation = 48
        HalQueryRuntimeServicesBlockInformation = 49


    HAL_QUERY_INFORMATION_CLASS = _HAL_QUERY_INFORMATION_CLASS
    PHAL_QUERY_INFORMATION_CLASS = POINTER(_HAL_QUERY_INFORMATION_CLASS)
    class _HAL_SET_INFORMATION_CLASS(ENUM):
        HalProfileSourceInterval = 1
        HalProfileSourceInterruptHandler = 2
        HalMcaRegisterDriver = 3
        HalKernelErrorHandler = 4
        HalCmcRegisterDriver = 5
        HalCpeRegisterDriver = 6
        HalMcaLog = 7
        HalCmcLog = 8
        HalCpeLog = 9
        HalGenerateCmcInterrupt = 10
        HalProfileSourceTimerHandler = 11
        HalEnlightenment = 12
        HalProfileDpgoSourceInterruptHandler = 13
        HalRegisterSecondaryInterruptInterface = 14
        HalSetChannelPowerInformation = 15
        HalI386ExceptionChainTerminatorInformation = 16
        HalSetResetParkDisposition = 17
        HalSetPsciSuspendMode = 18
        HalSetHvciEnabled = 19

        # Register performance monitor interrupt callback for Intel Processor
        # Trace
        HalSetProcessorTraceInterruptHandler = 20
        HalProfileSourceAdd = 21
        HalProfileSourceRemove = 22


    HAL_SET_INFORMATION_CLASS = _HAL_SET_INFORMATION_CLASS
    PHAL_SET_INFORMATION_CLASS = POINTER(_HAL_SET_INFORMATION_CLASS)
    class _PM_DISPATCH_TABLE(ctypes.Structure):
        pass
    _PM_DISPATCH_TABLE._fields_ = [
        ('Signature', ULONG),
        ('Version', ULONG),
        ('Function', PVOID * 1),
    ]


    PM_DISPATCH_TABLE = _PM_DISPATCH_TABLE
    PPM_DISPATCH_TABLE = POINTER(_PM_DISPATCH_TABLE)


    ) = _DMA_ADAPTER * (*pHalGetDmaAdapter)(        _In_opt_ PVOID PhysicalDeviceObject,        _In_  _DEVICE_DESCRIPTION *DeviceDescriptor,        _Out_ PULONG NumberOfMapRegisters
    class _MAP_REGISTER_ENTRY(ctypes.Structure):
        pass
    _MAP_REGISTER_ENTRY._fields_ = [
        ('MapRegister', PVOID),
        ('WriteToDevice', BOOLEAN),
    ]


    MAP_REGISTER_ENTRY = _MAP_REGISTER_ENTRY
    PMAP_REGISTER_ENTRY = POINTER(_MAP_REGISTER_ENTRY)


    _Struct_33._fields_ = [
        ('BitWidth', UCHAR),
        ('AccessSize', UCHAR),
    ]


    _Struct_32._Struct_33 = _Struct_33
    _Struct_32._anonymous_ = (
        '_Struct_33',
    )
    _Struct_32._fields_ = [
        ('Reserved', UCHAR * 2),
        ('_Struct_33', _Struct_32._Struct_33),
    ]


    DEBUG_DEVICE_ADDRESS._Struct_32 = _Struct_32
    DEBUG_DEVICE_ADDRESS._anonymous_ = (
        '_Struct_32',
    )
    DEBUG_DEVICE_ADDRESS._fields_ = [
        ('Type', UCHAR), # CmResourceType
        ('Valid', BOOLEAN),
        ('_Struct_32', DEBUG_DEVICE_ADDRESS._Struct_32),
        ('TranslatedAddress', PUCHAR),
        ('Length', ULONG),
    ]


    PDEBUG_DEVICE_ADDRESS = POINTER(DEBUG_DEVICE_ADDRESS)


    _Struct_33._fields_ = [
        ('BitWidth', UCHAR),
        ('AccessSize', UCHAR),
    ]


    ._Struct_33 = _Struct_33
    ._anonymous_ = (
        '_Struct_33',
    )
    ._fields_ = [
        ('Reserved', UCHAR * 2),
        ('_Struct_33', ._Struct_33),
    ]


    ._fields_ = [
        ('BitWidth', UCHAR),
        ('AccessSize', UCHAR),
    ]


    DEBUG_MEMORY_REQUIREMENTS._fields_ = [
        ('Start', PHYSICAL_ADDRESS),
        ('MaxEnd', PHYSICAL_ADDRESS),
        ('VirtualAddress', PVOID),
        ('Length', ULONG),
        ('Cached', BOOLEAN),
        ('Aligned', BOOLEAN),
    ]


    PDEBUG_MEMORY_REQUIREMENTS = POINTER(DEBUG_MEMORY_REQUIREMENTS)


    class KD_NAMESPACE_ENUM(ENUM):
        KdNameSpacePCI = 1
        KdNameSpaceACPI = 2
        KdNameSpaceAny = 3
        KdNameSpaceNone = 4
        KdNameSpaceMax = 5


    PKD_NAMESPACE_ENUM = POINTER(KD_NAMESPACE_ENUM)
    KdNameSpacePCI = KD_NAMESPACE_ENUM.KdNameSpacePCI
    KdNameSpaceACPI = KD_NAMESPACE_ENUM.KdNameSpaceACPI
    KdNameSpaceAny = KD_NAMESPACE_ENUM.KdNameSpaceAny
    KdNameSpaceNone = KD_NAMESPACE_ENUM.KdNameSpaceNone
    KdNameSpaceMax = KD_NAMESPACE_ENUM.KdNameSpaceMax
    class KD_CALLBACK_ACTION(ENUM):
        KdConfigureDeviceAndContinue = 1
        KdSkipDeviceAndContinue = 2
        KdConfigureDeviceAndStop = 3
        KdSkipDeviceAndStop = 4


    PKD_CALLBACK_ACTION = POINTER(KD_CALLBACK_ACTION)
    KdConfigureDeviceAndContinue = KD_CALLBACK_ACTION.KdConfigureDeviceAndContinue
    KdSkipDeviceAndContinue = KD_CALLBACK_ACTION.KdSkipDeviceAndContinue
    KdConfigureDeviceAndStop = KD_CALLBACK_ACTION.KdConfigureDeviceAndStop
    KdSkipDeviceAndStop = KD_CALLBACK_ACTION.KdSkipDeviceAndStop
    class _DEBUG_TRANSPORT_DATA(ctypes.Structure):
        pass
    _DEBUG_TRANSPORT_DATA._fields_ = [
        ('HwContextSize', ULONG),
        ('UseSerialFraming', BOOLEAN),
    ]


    DEBUG_TRANSPORT_DATA = _DEBUG_TRANSPORT_DATA
    PDEBUG_TRANSPORT_DATA = POINTER(_DEBUG_TRANSPORT_DATA)


    MAXIMUM_DEBUG_BARS = 6
    DBG_DEVICE_FLAG_HAL_SCRATCH_ALLOCATED = 0x01
    DBG_DEVICE_FLAG_BARS_MAPPED = 0x02
    DBG_DEVICE_FLAG_SCRATCH_ALLOCATED = 0x04
    DBG_DEVICE_FLAG_UNCACHED_MEMORY = 0x08
    DBG_DEVICE_FLAG_SYNTHETIC = 0x10
    class _DEBUG_DEVICE_DESCRIPTOR(ctypes.Structure):
        pass
    _Struct_35._fields_ = [
        ('DbgHalScratchAllocated : 1', UCHAR),
        ('DbgBarsMapped : 1', UCHAR),
        ('DbgScratchAllocated : 1', UCHAR),
    ]


    _Struct_34._Struct_35 = _Struct_35
    _Struct_34._anonymous_ = (
        '_Struct_35',
    )
    _Struct_34._fields_ = [
        ('Flags', UCHAR),
        ('_Struct_35', _Struct_34._Struct_35),
    ]


    _DEBUG_DEVICE_DESCRIPTOR._Struct_34 = _Struct_34
    _DEBUG_DEVICE_DESCRIPTOR._anonymous_ = (
        '_Struct_34',
    )
    _DEBUG_DEVICE_DESCRIPTOR._fields_ = [
        ('Bus', ULONG),
        ('Slot', ULONG),
        ('Segment', USHORT),
        ('VendorID', USHORT),
        ('DeviceID', USHORT),
        ('BaseClass', UCHAR),
        ('SubClass', UCHAR),
        ('ProgIf', UCHAR),
        ('_Struct_34', _DEBUG_DEVICE_DESCRIPTOR._Struct_34),
        ('Initialized', BOOLEAN),
        ('Configured', BOOLEAN),
        ('BaseAddress', DEBUG_DEVICE_ADDRESS * MAXIMUM_DEBUG_BARS),
        ('Memory', DEBUG_MEMORY_REQUIREMENTS),
        ('PortType', USHORT),
        ('PortSubtype', USHORT),
        ('OemData', PVOID),
        ('OemDataLength', ULONG),
        ('NameSpace', KD_NAMESPACE_ENUM),
        ('NameSpacePath', PWCHAR),
        ('NameSpacePathLength', ULONG),
        ('TransportType', ULONG),
        ('TransportData', DEBUG_TRANSPORT_DATA),
    ]


    DEBUG_DEVICE_DESCRIPTOR = _DEBUG_DEVICE_DESCRIPTOR
    PDEBUG_DEVICE_DESCRIPTOR = POINTER(_DEBUG_DEVICE_DESCRIPTOR)


    _Struct_35._fields_ = [
        ('DbgHalScratchAllocated : 1', UCHAR),
        ('DbgBarsMapped : 1', UCHAR),
        ('DbgScratchAllocated : 1', UCHAR),
    ]


    ._Struct_35 = _Struct_35
    ._anonymous_ = (
        '_Struct_35',
    )
    ._fields_ = [
        ('Flags', UCHAR),
        ('_Struct_35', ._Struct_35),
    ]


    ._fields_ = [
        ('DbgHalScratchAllocated : 1', UCHAR),
        ('DbgBarsMapped : 1', UCHAR),
        ('DbgScratchAllocated : 1', UCHAR),
    ]


    class _PCI_DEBUGGING_DEVICE_IN_USE(ctypes.Structure):
        pass
    _PCI_DEBUGGING_DEVICE_IN_USE._fields_ = [
        ('Segment', USHORT),
        ('Bus', ULONG),
        ('Slot', ULONG),
    ]


    PCI_DEBUGGING_DEVICE_IN_USE = _PCI_DEBUGGING_DEVICE_IN_USE
    PPCI_DEBUGGING_DEVICE_IN_USE = POINTER(_PCI_DEBUGGING_DEVICE_IN_USE)


    class _ACPI_DEBUGGING_DEVICE_IN_USE(ctypes.Structure):
        pass
    _ACPI_DEBUGGING_DEVICE_IN_USE._fields_ = [
        ('NameSpacePathLength', ULONG),
        ('NameSpacePath', WCHAR * ANYSIZE_ARRAY),
    ]


    ACPI_DEBUGGING_DEVICE_IN_USE = _ACPI_DEBUGGING_DEVICE_IN_USE
    PACPI_DEBUGGING_DEVICE_IN_USE = POINTER(_ACPI_DEBUGGING_DEVICE_IN_USE)


    class _DEBUGGING_DEVICE_IN_USE(ctypes.Structure):
        pass
    _Union_14._fields_ = [
        ('AcpiDevice', ACPI_DEBUGGING_DEVICE_IN_USE),
        ('PciDevice', PCI_DEBUGGING_DEVICE_IN_USE),
    ]


    _DEBUGGING_DEVICE_IN_USE._Union_14 = _Union_14
    _DEBUGGING_DEVICE_IN_USE._anonymous_ = (
        '_Union_14',
    )
    _DEBUGGING_DEVICE_IN_USE._fields_ = [
        ('NameSpace', KD_NAMESPACE_ENUM),
        ('StructureLength', ULONG),
        ('_Union_14', _DEBUGGING_DEVICE_IN_USE._Union_14),
    ]


    DEBUGGING_DEVICE_IN_USE = _DEBUGGING_DEVICE_IN_USE
    PDEBUGGING_DEVICE_IN_USE = POINTER(_DEBUGGING_DEVICE_IN_USE)


    ._fields_ = [
        ('AcpiDevice', ACPI_DEBUGGING_DEVICE_IN_USE),
        ('PciDevice', PCI_DEBUGGING_DEVICE_IN_USE),
    ]


    class _DEBUGGING_DEVICE_IN_USE_INFORMATION(ctypes.Structure):
        pass
    _DEBUGGING_DEVICE_IN_USE_INFORMATION._fields_ = [
        ('DeviceCount', ULONG),
        ('Device', DEBUGGING_DEVICE_IN_USE * ANYSIZE_ARRAY),
    ]


    DEBUGGING_DEVICE_IN_USE_INFORMATION = _DEBUGGING_DEVICE_IN_USE_INFORMATION
    PDEBUGGING_DEVICE_IN_USE_INFORMATION = POINTER(_DEBUGGING_DEVICE_IN_USE_INFORMATION)


    HAL_DISPATCH._fields_ = [
        ('Version', ULONG),
        ('HalQuerySystemInformation', pHalQuerySystemInformation),
        ('HalSetSystemInformation', pHalSetSystemInformation),
        ('HalQueryBusSlots', pHalQueryBusSlots),
        ('Spare1', ULONG),
        ('HalExamineMBR', pHalExamineMBR),
        ('HalIoReadPartitionTable', pHalIoReadPartitionTable),
        ('HalIoSetPartitionInformation', pHalIoSetPartitionInformation),
        ('HalIoWritePartitionTable', pHalIoWritePartitionTable),
        ('HalReferenceHandlerForBus', pHalHandlerForBus),
        ('HalReferenceBusHandler', pHalReferenceBusHandler),
        ('HalDereferenceBusHandler', pHalReferenceBusHandler),
        ('HalInitPnpDriver', pHalInitPnpDriver),
        ('HalInitPowerManagement', pHalInitPowerManagement),
        ('HalGetDmaAdapter', pHalGetDmaAdapter),
        ('HalGetInterruptTranslator', pHalGetInterruptTranslator),
        ('HalStartMirroring', pHalStartMirroring),
        ('HalEndMirroring', pHalEndMirroring),
        ('HalMirrorPhysicalMemory', pHalMirrorPhysicalMemory),
        ('HalEndOfBoot', pHalEndOfBoot),
        ('HalMirrorVerify', pHalMirrorVerify),
        ('HalGetCachedAcpiTable', pHalGetAcpiTable),
        ('HalSetPciErrorHandlerCallback', pHalSetPciErrorHandlerCallback),
    ]


    PHAL_DISPATCH = POINTER(HAL_DISPATCH)



    if defined(_NTDRIVER_) or defined(_NTDDK_) or defined(_NTIFS_) or defined(_NTHAL_):
        HALDISPATCH = HalDispatchTable
else:
        HALDISPATCH = & HalDispatchTable
    # END IF
    HAL_DISPATCH_VERSION = 4
    HalDispatchTableVersion = HALDISPATCH - >Version
    HalQuerySystemInformation = HALDISPATCH - >HalQuerySystemInformation
    HalSetSystemInformation = HALDISPATCH - >HalSetSystemInformation
    HalQueryBusSlots = HALDISPATCH - >HalQueryBusSlots
    HalReferenceHandlerForBus = HALDISPATCH - >HalReferenceHandlerForBus
    HalReferenceBusHandler = HALDISPATCH - >HalReferenceBusHandler
    HalDereferenceBusHandler = HALDISPATCH - >HalDereferenceBusHandler
    HalInitPnpDriver = HALDISPATCH - >HalInitPnpDriver
    HalInitPowerManagement = HALDISPATCH - >HalInitPowerManagement
    HalGetDmaAdapter = HALDISPATCH - >HalGetDmaAdapter
    HalGetInterruptTranslator = HALDISPATCH - >HalGetInterruptTranslator
    HalStartMirroring = HALDISPATCH - >HalStartMirroring
    HalEndMirroring = HALDISPATCH - >HalEndMirroring
    HalMirrorPhysicalMemory = HALDISPATCH - >HalMirrorPhysicalMemory
    HalEndOfBoot = HALDISPATCH - >HalEndOfBoot
    HalMirrorVerify = HALDISPATCH - >HalMirrorVerify
    HalGetCachedAcpiTable = HALDISPATCH - >HalGetCachedAcpiTable
    HalSetPciErrorHandlerCallback = HALDISPATCH - >HalSetPciErrorHandlerCallback
    class _HAL_BUS_INFORMATION(ctypes.Structure):
        pass
    _HAL_BUS_INFORMATION._fields_ = [
        ('BusType', INTERFACE_TYPE),
        ('ConfigurationType', BUS_DATA_TYPE),
        ('BusNumber', ULONG),
        ('Reserved', ULONG),
    ]


    HAL_BUS_INFORMATION = _HAL_BUS_INFORMATION
    PHAL_BUS_INFORMATION = POINTER(_HAL_BUS_INFORMATION)




    class _HAL_DISPLAY_BIOS_INFORMATION(ENUM):
        HalDisplayInt10Bios = 1
        HalDisplayEmulatedBios = 2
        HalDisplayNoBios = 3


    HAL_DISPLAY_BIOS_INFORMATION = _HAL_DISPLAY_BIOS_INFORMATION
    PHAL_DISPLAY_BIOS_INFORMATION = POINTER(_HAL_DISPLAY_BIOS_INFORMATION)
    class _HAL_POWER_INFORMATION(ctypes.Structure):
        pass
    _HAL_POWER_INFORMATION._fields_ = [
        ('TBD', ULONG),
    ]


    HAL_POWER_INFORMATION = _HAL_POWER_INFORMATION
    PHAL_POWER_INFORMATION = POINTER(_HAL_POWER_INFORMATION)


    class _HAL_PROCESSOR_SPEED_INFO(ctypes.Structure):
        pass
    _HAL_PROCESSOR_SPEED_INFO._fields_ = [
        ('ProcessorSpeed', ULONG),
    ]


    HAL_PROCESSOR_SPEED_INFORMATION = _HAL_PROCESSOR_SPEED_INFO
    PHAL_PROCESSOR_SPEED_INFORMATION = POINTER(_HAL_PROCESSOR_SPEED_INFO)


    class _HAL_CALLBACKS(ctypes.Structure):
        pass
    _HAL_CALLBACKS._fields_ = [
        ('SetSystemInformation', PCALLBACK_OBJECT),
        ('BusCheck', PCALLBACK_OBJECT),
    ]


    HAL_CALLBACKS = _HAL_CALLBACKS
    PHAL_CALLBACKS = POINTER(_HAL_CALLBACKS)


    class _HAL_PROCESSOR_FEATURE(ctypes.Structure):
        pass
    _HAL_PROCESSOR_FEATURE._fields_ = [
        ('UsableFeatureBits', ULONG),
    ]


    HAL_PROCESSOR_FEATURE = _HAL_PROCESSOR_FEATURE


    class _HAL_AMLI_BAD_IO_ADDRESS_LIST(ctypes.Structure):
        pass
    _HAL_AMLI_BAD_IO_ADDRESS_LIST._fields_ = [
        ('BadAddrBegin', ULONG),
        ('BadAddrSize', ULONG),
        ('OSVersionTrigger', ULONG),
        ('IOHandler', PHALIOREADWRITEHANDLER),
    ]


    HAL_AMLI_BAD_IO_ADDRESS_LIST = _HAL_AMLI_BAD_IO_ADDRESS_LIST
    PHAL_AMLI_BAD_IO_ADDRESS_LIST = POINTER(_HAL_AMLI_BAD_IO_ADDRESS_LIST)


    class _HAL_MCA_INTERFACE(ctypes.Structure):
        pass
    _HAL_MCA_INTERFACE._fields_ = [
        ('Lock', PHALMCAINTERFACELOCK),
        ('Unlock', PHALMCAINTERFACEUNLOCK),
        ('ReadRegister', PHALMCAINTERFACEREADREGISTER),
    ]


    HAL_MCA_INTERFACE = _HAL_MCA_INTERFACE


    class HAL_APIC_DESTINATION_MODE(ENUM):
        ApicDestinationModePhysical = 1
        ApicDestinationModeLogicalFlat = 2
        ApicDestinationModeLogicalClustered = 3
        ApicDestinationModeUnknown = 4


    PHAL_APIC_DESTINATION_MODE = POINTER(HAL_APIC_DESTINATION_MODE)
    ApicDestinationModePhysical = HAL_APIC_DESTINATION_MODE.ApicDestinationModePhysical
    ApicDestinationModeLogicalFlat = HAL_APIC_DESTINATION_MODE.ApicDestinationModeLogicalFlat
    ApicDestinationModeLogicalClustered = HAL_APIC_DESTINATION_MODE.ApicDestinationModeLogicalClustered
    ApicDestinationModeUnknown = HAL_APIC_DESTINATION_MODE.ApicDestinationModeUnknown
    if defined(_AMD64_):
        _KTRAP_FRAME = struct


        _KEXCEPTION_FRAME = struct


    # END IF
    if defined(_ARM_) or defined(_ARM64_):
        _KTRAP_FRAME = struct


        _KEXCEPTION_FRAME = struct


    # END IF
    if defined(_X86_):
        pass
    # END IF
    class _MCA_DRIVER_INFO(ctypes.Structure):
        pass
    _MCA_DRIVER_INFO._fields_ = [
        ('ExceptionCallback', PDRIVER_MCA_EXCEPTION_CALLBACK),
        ('DpcCallback', PKDEFERRED_ROUTINE),
        ('DeviceContext', PVOID),
    ]


    MCA_DRIVER_INFO = _MCA_DRIVER_INFO
    PMCA_DRIVER_INFO = POINTER(_MCA_DRIVER_INFO)


    class _HAL_ERROR_INFO(ctypes.Structure):
        pass
    _HAL_ERROR_INFO._fields_ = [
        ('Version', ULONG), # Version of this structure
        ('InitMaxSize', ULONG), # Maximum size of the INIT record.
        ('McaMaxSize', ULONG), # Maximum size of a Machine Check Abort record
        ('McaPreviousEventsCount', ULONG), # Flag indicating previous or early - boot MCA event logs.
        ('McaCorrectedEventsCount', ULONG), # Number of corrected MCA events since boot. approx.
        ('McaKernelDeliveryFails', ULONG), # Number of Kernel callback failures.   approx.
        ('McaDriverDpcQueueFails', ULONG), # Number of OEM MCA Driver Dpc queuing failures. approx.
        ('McaReserved', ULONG),
        ('CmcMaxSize', ULONG), # Maximum size of a Corrected Machine Check record
        ('CmcPollingInterval', ULONG), # In units of seconds
        ('CmcInterruptsCount', ULONG), # Number of CMC interrupts.     approx.
        ('CmcKernelDeliveryFails', ULONG), # Number of Kernel callback failures.   approx.
        ('CmcDriverDpcQueueFails', ULONG), # Number of OEM CMC Driver Dpc queuing failures. approx.
        ('CmcGetStateFails', ULONG), # Number of failures in getting the log from FW.
        ('CmcClearStateFails', ULONG), # Number of failures in clearing the log from FW.
        ('CmcReserved', ULONG),
        ('CmcLogId', ULONGLONG), # Last seen record identifier.
        ('CpeMaxSize', ULONG), # Maximum size of a Corrected Platform Event record
        ('CpePollingInterval', ULONG), # In units of seconds
        ('CpeInterruptsCount', ULONG), # Number of CPE interrupts.     approx.
        ('CpeKernelDeliveryFails', ULONG), # Number of Kernel callback failures.   approx.
        ('CpeDriverDpcQueueFails', ULONG), # Number of OEM CPE Driver Dpc queuing failures. approx.
        ('CpeGetStateFails', ULONG), # Number of failures in getting the log from FW.
        ('CpeClearStateFails', ULONG), # Number of failures in clearing the log from FW.
        ('CpeInterruptSources', ULONG), # Number of SAPIC Platform Interrupt Sources
        ('CpeLogId', ULONGLONG), # Last seen record identifier.
        ('KernelReserved', ULONGLONG * 4),
    ]


    HAL_ERROR_INFO = _HAL_ERROR_INFO
    PHAL_ERROR_INFO = POINTER(_HAL_ERROR_INFO)


    HAL_MCE_INTERRUPTS_BASED = (ULONG) - 1
    HAL_MCE_DISABLED = (ULONG)0
    HAL_CMC_INTERRUPTS_BASED = HAL_MCE_INTERRUPTS_BASED
    HAL_CMC_DISABLED = HAL_MCE_DISABLED
    HAL_CPE_INTERRUPTS_BASED = HAL_MCE_INTERRUPTS_BASED
    HAL_CPE_DISABLED = HAL_MCE_DISABLED
    HAL_MCA_INTERRUPTS_BASED = HAL_MCE_INTERRUPTS_BASED
    HAL_MCA_DISABLED = HAL_MCE_DISABLED
    class _CMC_DRIVER_INFO(ctypes.Structure):
        pass
    _CMC_DRIVER_INFO._fields_ = [
        ('ExceptionCallback', PDRIVER_CMC_EXCEPTION_CALLBACK),
        ('DpcCallback', PKDEFERRED_ROUTINE),
        ('DeviceContext', PVOID),
    ]


    CMC_DRIVER_INFO = _CMC_DRIVER_INFO
    PCMC_DRIVER_INFO = POINTER(_CMC_DRIVER_INFO)


    class _CPE_DRIVER_INFO(ctypes.Structure):
        pass
    _CPE_DRIVER_INFO._fields_ = [
        ('ExceptionCallback', PDRIVER_CPE_EXCEPTION_CALLBACK),
        ('DpcCallback', PKDEFERRED_ROUTINE),
        ('DeviceContext', PVOID),
    ]


    CPE_DRIVER_INFO = _CPE_DRIVER_INFO
    PCPE_DRIVER_INFO = POINTER(_CPE_DRIVER_INFO)


    class _HAL_PLATFORM_INFORMATION(ctypes.Structure):
        pass
    _HAL_PLATFORM_INFORMATION._fields_ = [
        ('PlatformFlags', ULONG),
    ]


    HAL_PLATFORM_INFORMATION = _HAL_PLATFORM_INFORMATION
    PHAL_PLATFORM_INFORMATION = POINTER(_HAL_PLATFORM_INFORMATION)


    HAL_PLATFORM_DISABLE_WRITE_COMBINING = 0x01
    HAL_PLATFORM_DISABLE_PTCG = 0x04
    HAL_PLATFORM_DISABLE_UC_MAIN_MEMORY = 0x08
    HAL_PLATFORM_ENABLE_WRITE_COMBINING_MMIO = 0x10
    HAL_PLATFORM_ACPI_TABLES_CACHED = 0x20

    if defined(_WIN64) or defined(_ARM_):
        if not defined(USE_DMA_MACROS):
            USE_DMA_MACROS = 1
        # END IF

        if not defined(NO_LEGACY_DRIVERS):
            NO_LEGACY_DRIVERS = 1
        # END IF
    # END IF   _WIN64

    if defined(USE_DMA_MACROS) and not defined(_NTHAL_) and (defined(_NTDDK_) or defined(_NTDRIVER_)) or defined(_WDM_INCLUDED_):
        pass
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            pass
        # END IF
else:
        pass
    # END IF   USE_DMA_MACROS and (_NTDDK_ or _NTDRIVER_)
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if not defined(XBOX_SYSTEMOS):
        if (NTDDI_VERSION >= NTDDI_WIN7):
            PWHEA_ERROR_SOURCE_DESCRIPTOR = POINTER(_WHEA_ERROR_SOURCE_DESCRIPTOR)


            PWHEA_ERROR_RECORD = POINTER(_WHEA_ERROR_RECORD)


    elif (NTDDI_VERSION >= NTDDI_VISTA):
            PWHEA_ERROR_RECORD = POINTER(_WHEA_ERROR_RECORD)


        # END IF
    # END IF
    class _PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE(ENUM):
        ResourceTypeSingle = 0
        ResourceTypeRange = 1
        ResourceTypeExtendedCounterConfiguration = 2
        ResourceTypeOverflow = 3
        ResourceTypeMax = 4


    PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE = _PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE
    class _PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR(ctypes.Structure):
        pass
    Range._fields_ = [
        ('Begin', ULONG),
        ('End', ULONG),
    ]


    u.Range = Range
    u._fields_ = [
        ('CounterIndex', ULONG),
        ('ExtendedRegisterAddress', ULONG),
        ('Range', u.Range),
    ]


    _PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR.u = u
    _PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR._fields_ = [
        ('Type', PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR_TYPE),
        ('Flags', ULONG),
        ('u', _PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR.u),
    ]


    PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR = _PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR
    PPHYSICAL_COUNTER_RESOURCE_DESCRIPTOR = POINTER(_PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR)


    Range._fields_ = [
        ('Begin', ULONG),
        ('End', ULONG),
    ]


    u.Range = Range
    u._fields_ = [
        ('CounterIndex', ULONG),
        ('ExtendedRegisterAddress', ULONG),
        ('Range', u.Range),
    ]


    Range._fields_ = [
        ('Begin', ULONG),
        ('End', ULONG),
    ]


    class _PHYSICAL_COUNTER_RESOURCE_LIST(ctypes.Structure):
        pass
    _PHYSICAL_COUNTER_RESOURCE_LIST._fields_ = [
        ('Count', ULONG),
        ('Descriptors', PHYSICAL_COUNTER_RESOURCE_DESCRIPTOR * ANYSIZE_ARRAY),
    ]


    PHYSICAL_COUNTER_RESOURCE_LIST = _PHYSICAL_COUNTER_RESOURCE_LIST
    PPHYSICAL_COUNTER_RESOURCE_LIST = POINTER(_PHYSICAL_COUNTER_RESOURCE_LIST)


    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):


def FsRtlIsChecksumError(STS):
    return BOOLEANnot FsRtlIsTotalDeviceFailureSTS
    # END IF
    class _PCI_AGP_CAPABILITY(ctypes.Structure):
        pass
    AGPStatus._fields_ = [
        ('Rate:3', ULONG),
        ('Agp3Mode:1', ULONG),
        ('FastWrite:1', ULONG),
        ('FourGB:1', ULONG),
        ('HostTransDisable:1', ULONG),
        ('Gart64:1', ULONG),
        ('ITA_Coherent:1', ULONG),
        ('SideBandAddressing:1', ULONG), # SBA
        ('CalibrationCycle:3', ULONG),
        ('AsyncRequestSize:3', ULONG),
        ('Rsvd1:1', ULONG),
        ('Isoch:1', ULONG),
        ('Rsvd2:6', ULONG),
        ('RequestQueueDepthMaximum:8', ULONG), # RQ
    ]


    _PCI_AGP_CAPABILITY.AGPStatus = AGPStatus
    AGPCommand._fields_ = [
        ('Rate:3', ULONG),
        ('Rsvd1:1', ULONG),
        ('FastWriteEnable:1', ULONG),
        ('FourGBEnable:1', ULONG),
        ('Rsvd2:1', ULONG),
        ('Gart64:1', ULONG),
        ('AGPEnable:1', ULONG),
        ('SBAEnable:1', ULONG),
        ('CalibrationCycle:3', ULONG),
        ('AsyncReqSize:3', ULONG),
        ('Rsvd3:8', ULONG),
        ('RequestQueueDepth:8', ULONG),
    ]


    _PCI_AGP_CAPABILITY.AGPCommand = AGPCommand
    _PCI_AGP_CAPABILITY._fields_ = [
        ('Header', PCI_CAPABILITIES_HEADER),
        ('Minor:4', USHORT),
        ('Major:4', USHORT),
        ('Rsvd1:8', USHORT),
        ('AGPStatus', _PCI_AGP_CAPABILITY.AGPStatus),
        ('AGPCommand', _PCI_AGP_CAPABILITY.AGPCommand),
    ]


    PCI_AGP_CAPABILITY = _PCI_AGP_CAPABILITY
    PPCI_AGP_CAPABILITY = POINTER(_PCI_AGP_CAPABILITY)


    class _PCI_AGP_STATUS(ctypes.Structure):
        pass
    _PCI_AGP_STATUS._fields_ = [
        ('Rate:3', ULONG),
        ('Agp3Mode:1', ULONG),
        ('FastWrite:1', ULONG),
        ('FourGB:1', ULONG),
        ('HostTransDisable:1', ULONG),
        ('Gart64:1', ULONG),
        ('ITA_Coherent:1', ULONG),
        ('SideBandAddressing:1', ULONG), # SBA
        ('CalibrationCycle:3', ULONG),
        ('AsyncRequestSize:3', ULONG),
        ('Rsvd1:1', ULONG),
        ('Isoch:1', ULONG),
        ('Rsvd2:6', ULONG),
        ('RequestQueueDepthMaximum:8', ULONG), # RQ
    ]


    AGPStatus = _PCI_AGP_STATUS


    class _PCI_AGP_COMMAND(ctypes.Structure):
        pass
    _PCI_AGP_COMMAND._fields_ = [
        ('Rate:3', ULONG),
        ('Rsvd1:1', ULONG),
        ('FastWriteEnable:1', ULONG),
        ('FourGBEnable:1', ULONG),
        ('Rsvd2:1', ULONG),
        ('Gart64:1', ULONG),
        ('AGPEnable:1', ULONG),
        ('SBAEnable:1', ULONG),
        ('CalibrationCycle:3', ULONG),
        ('AsyncReqSize:3', ULONG),
        ('Rsvd3:8', ULONG),
        ('RequestQueueDepth:8', ULONG),
    ]


    AGPCommand = _PCI_AGP_COMMAND




    class _EXTENDED_AGP_REGISTER(ENUM):
        IsochStatus = 1
        AgpControl = 2
        ApertureSize = 3
        AperturePageSize = 4
        GartLow = 5
        GartHigh = 6
        IsochCommand = 7


    EXTENDED_AGP_REGISTER = _EXTENDED_AGP_REGISTER
    PEXTENDED_AGP_REGISTER = POINTER(_EXTENDED_AGP_REGISTER)
    class _PCI_AGP_ISOCH_STATUS(ctypes.Structure):
        pass
    _PCI_AGP_ISOCH_STATUS._fields_ = [
        ('ErrorCode: 2', ULONG),
        ('Rsvd1: 1', ULONG),
        ('Isoch_L: 3', ULONG),
        ('Isoch_Y: 2', ULONG),
        ('Isoch_N: 8', ULONG),
        ('Rsvd2: 16', ULONG),
    ]


    PCI_AGP_ISOCH_STATUS = _PCI_AGP_ISOCH_STATUS
    PPCI_AGP_ISOCH_STATUS = POINTER(_PCI_AGP_ISOCH_STATUS)


    class _PCI_AGP_CONTROL(ctypes.Structure):
        pass
    _PCI_AGP_CONTROL._fields_ = [
        ('Rsvd1: 7', ULONG),
        ('GTLB_Enable: 1', ULONG),
        ('AP_Enable: 1', ULONG),
        ('CAL_Disable: 1', ULONG),
        ('Rsvd2: 22', ULONG),
    ]


    PCI_AGP_CONTROL = _PCI_AGP_CONTROL
    PPCI_AGP_CONTROL = POINTER(_PCI_AGP_CONTROL)


    class _PCI_AGP_APERTURE_PAGE_SIZE(ctypes.Structure):
        pass
    _PCI_AGP_APERTURE_PAGE_SIZE._fields_ = [
        ('PageSizeMask: 11', USHORT),
        ('Rsvd1: 1', USHORT),
        ('PageSizeSelect: 4', USHORT),
    ]


    PCI_AGP_APERTURE_PAGE_SIZE = _PCI_AGP_APERTURE_PAGE_SIZE
    PPCI_AGP_APERTURE_PAGE_SIZE = POINTER(_PCI_AGP_APERTURE_PAGE_SIZE)


    class _PCI_AGP_ISOCH_COMMAND(ctypes.Structure):
        pass
    _PCI_AGP_ISOCH_COMMAND._fields_ = [
        ('Rsvd1: 6', USHORT),
        ('Isoch_Y: 2', USHORT),
        ('Isoch_N: 8', USHORT),
    ]


    PCI_AGP_ISOCH_COMMAND = _PCI_AGP_ISOCH_COMMAND
    PPCI_AGP_ISOCH_COMMAND = POINTER(_PCI_AGP_ISOCH_COMMAND)


    class PCI_AGP_EXTENDED_CAPABILITY(ctypes.Structure):
        pass
    PCI_AGP_EXTENDED_CAPABILITY._fields_ = [
        ('IsochStatus', PCI_AGP_ISOCH_STATUS),
        ('AgpControl', PCI_AGP_CONTROL), # Target only - - - - - - - - - - - - - - - - << - begin - >>
        ('ApertureSize', USHORT),
        ('AperturePageSize', PCI_AGP_APERTURE_PAGE_SIZE),
        ('GartLow', ULONG),
        ('GartHigh', ULONG),

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - << - end
        # - >>
        ('IsochCommand', PCI_AGP_ISOCH_COMMAND),
    ]


    PPCI_AGP_EXTENDED_CAPABILITY = POINTER(PCI_AGP_EXTENDED_CAPABILITY)


    PCI_AGP_RATE_1X = 0x1
    PCI_AGP_RATE_2X = 0x2
    PCI_AGP_RATE_4X = 0x4
    PCIX_MODE_CONVENTIONAL_PCI = 0x0
    PCIX_MODE1_66MHZ = 0x1
    PCIX_MODE1_100MHZ = 0x2
    PCIX_MODE1_133MHZ = 0x3
    PCIX_MODE2_266_66MHZ = 0x9
    PCIX_MODE2_266_100MHZ = 0xA
    PCIX_MODE2_266_133MHZ = 0xB
    PCIX_MODE2_533_66MHZ = 0xD
    PCIX_MODE2_533_100MHZ = 0xE
    PCIX_MODE2_533_133MHZ = 0xF
    PCIX_VERSION_MODE1_ONLY = 0x0
    PCIX_VERSION_MODE2_ECC = 0x1
    PCIX_VERSION_DUAL_MODE_ECC = 0x2
    class _PCIX_BRIDGE_CAPABILITY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Bus64Bit:1', USHORT),
        ('Bus133MHzCapable:1', USHORT),
        ('SplitCompletionDiscarded:1', USHORT),
        ('UnexpectedSplitCompletion:1', USHORT),
        ('SplitCompletionOverrun:1', USHORT),
        ('SplitRequestDelayed:1', USHORT),
        ('BusModeFrequency:4', USHORT), # PCIX_MODE_x
        ('Rsvd:2', USHORT),
        ('Version:2', USHORT), # PCIX_VERSION_x
        ('Bus266MHzCapable:1', USHORT),
        ('Bus533MHzCapable:1', USHORT),
    ]


    SecondaryStatus.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    SecondaryStatus._fields_ = [
        ('DUMMYSTRUCTNAME', SecondaryStatus.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    _PCIX_BRIDGE_CAPABILITY.SecondaryStatus = SecondaryStatus
    DUMMYSTRUCTNAME._fields_ = [
        ('FunctionNumber:3', ULONG),
        ('DeviceNumber:5', ULONG),
        ('BusNumber:8', ULONG),
        ('Device64Bit:1', ULONG),
        ('Device133MHzCapable:1', ULONG),
        ('SplitCompletionDiscarded:1', ULONG),
        ('UnexpectedSplitCompletion:1', ULONG),
        ('SplitCompletionOverrun:1', ULONG),
        ('SplitRequestDelayed:1', ULONG),
        ('Rsvd:7', ULONG),
        ('DIMCapable:1', ULONG),
        ('Device266MHzCapable:1', ULONG),
        ('Device533MHzCapable:1', ULONG),
    ]


    BridgeStatus.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    BridgeStatus._fields_ = [
        ('DUMMYSTRUCTNAME', BridgeStatus.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    _PCIX_BRIDGE_CAPABILITY.BridgeStatus = BridgeStatus
    DUMMYSTRUCTNAME._fields_ = [
        ('SelectSecondaryRegisters:1', ULONG),
        ('ErrorPresentInOtherBank:1', ULONG),
        ('AdditionalCorrectableError:1', ULONG),
        ('AdditionalUncorrectableError:1', ULONG),
        ('ErrorPhase:3', ULONG),
        ('ErrorCorrected:1', ULONG),
        ('Syndrome:8', ULONG),
        ('ErrorFirstCommand:4', ULONG),
        ('ErrorSecondCommand:4', ULONG),
        ('ErrorUpperAttributes:4', ULONG),
        ('ControlUpdateEnable:1', ULONG),
        ('Rsvd:1', ULONG),
        ('DisableSingleBitCorrection:1', ULONG),
        ('EccMode:1', ULONG),
    ]


    EccControlStatus.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    EccControlStatus._fields_ = [
        ('DUMMYSTRUCTNAME', EccControlStatus.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    _PCIX_BRIDGE_CAPABILITY.EccControlStatus = EccControlStatus
    _PCIX_BRIDGE_CAPABILITY._fields_ = [
        ('Header', PCI_CAPABILITIES_HEADER),
        ('SecondaryStatus', _PCIX_BRIDGE_CAPABILITY.SecondaryStatus),
        ('BridgeStatus', _PCIX_BRIDGE_CAPABILITY.BridgeStatus),
        ('UpstreamSplitTransactionCapacity', USHORT),
        ('UpstreamSplitTransactionLimit', USHORT),
        ('DownstreamSplitTransactionCapacity', USHORT),
        ('DownstreamSplitTransactionLimit', USHORT),
        ('EccControlStatus', _PCIX_BRIDGE_CAPABILITY.EccControlStatus),
        ('EccFirstAddress', ULONG),
        ('EccSecondAddress', ULONG),
        ('EccAttribute', ULONG),
    ]


    PCIX_BRIDGE_CAPABILITY = _PCIX_BRIDGE_CAPABILITY
    PPCIX_BRIDGE_CAPABILITY = POINTER(_PCIX_BRIDGE_CAPABILITY)


    DUMMYSTRUCTNAME._fields_ = [
        ('Bus64Bit:1', USHORT),
        ('Bus133MHzCapable:1', USHORT),
        ('SplitCompletionDiscarded:1', USHORT),
        ('UnexpectedSplitCompletion:1', USHORT),
        ('SplitCompletionOverrun:1', USHORT),
        ('SplitRequestDelayed:1', USHORT),
        ('BusModeFrequency:4', USHORT), # PCIX_MODE_x
        ('Rsvd:2', USHORT),
        ('Version:2', USHORT), # PCIX_VERSION_x
        ('Bus266MHzCapable:1', USHORT),
        ('Bus533MHzCapable:1', USHORT),
    ]


    SecondaryStatus.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    SecondaryStatus._fields_ = [
        ('DUMMYSTRUCTNAME', SecondaryStatus.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('Bus64Bit:1', USHORT),
        ('Bus133MHzCapable:1', USHORT),
        ('SplitCompletionDiscarded:1', USHORT),
        ('UnexpectedSplitCompletion:1', USHORT),
        ('SplitCompletionOverrun:1', USHORT),
        ('SplitRequestDelayed:1', USHORT),
        ('BusModeFrequency:4', USHORT), # PCIX_MODE_x
        ('Rsvd:2', USHORT),
        ('Version:2', USHORT), # PCIX_VERSION_x
        ('Bus266MHzCapable:1', USHORT),
        ('Bus533MHzCapable:1', USHORT),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('FunctionNumber:3', ULONG),
        ('DeviceNumber:5', ULONG),
        ('BusNumber:8', ULONG),
        ('Device64Bit:1', ULONG),
        ('Device133MHzCapable:1', ULONG),
        ('SplitCompletionDiscarded:1', ULONG),
        ('UnexpectedSplitCompletion:1', ULONG),
        ('SplitCompletionOverrun:1', ULONG),
        ('SplitRequestDelayed:1', ULONG),
        ('Rsvd:7', ULONG),
        ('DIMCapable:1', ULONG),
        ('Device266MHzCapable:1', ULONG),
        ('Device533MHzCapable:1', ULONG),
    ]


    BridgeStatus.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    BridgeStatus._fields_ = [
        ('DUMMYSTRUCTNAME', BridgeStatus.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('FunctionNumber:3', ULONG),
        ('DeviceNumber:5', ULONG),
        ('BusNumber:8', ULONG),
        ('Device64Bit:1', ULONG),
        ('Device133MHzCapable:1', ULONG),
        ('SplitCompletionDiscarded:1', ULONG),
        ('UnexpectedSplitCompletion:1', ULONG),
        ('SplitCompletionOverrun:1', ULONG),
        ('SplitRequestDelayed:1', ULONG),
        ('Rsvd:7', ULONG),
        ('DIMCapable:1', ULONG),
        ('Device266MHzCapable:1', ULONG),
        ('Device533MHzCapable:1', ULONG),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('SelectSecondaryRegisters:1', ULONG),
        ('ErrorPresentInOtherBank:1', ULONG),
        ('AdditionalCorrectableError:1', ULONG),
        ('AdditionalUncorrectableError:1', ULONG),
        ('ErrorPhase:3', ULONG),
        ('ErrorCorrected:1', ULONG),
        ('Syndrome:8', ULONG),
        ('ErrorFirstCommand:4', ULONG),
        ('ErrorSecondCommand:4', ULONG),
        ('ErrorUpperAttributes:4', ULONG),
        ('ControlUpdateEnable:1', ULONG),
        ('Rsvd:1', ULONG),
        ('DisableSingleBitCorrection:1', ULONG),
        ('EccMode:1', ULONG),
    ]


    EccControlStatus.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    EccControlStatus._fields_ = [
        ('DUMMYSTRUCTNAME', EccControlStatus.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('SelectSecondaryRegisters:1', ULONG),
        ('ErrorPresentInOtherBank:1', ULONG),
        ('AdditionalCorrectableError:1', ULONG),
        ('AdditionalUncorrectableError:1', ULONG),
        ('ErrorPhase:3', ULONG),
        ('ErrorCorrected:1', ULONG),
        ('Syndrome:8', ULONG),
        ('ErrorFirstCommand:4', ULONG),
        ('ErrorSecondCommand:4', ULONG),
        ('ErrorUpperAttributes:4', ULONG),
        ('ControlUpdateEnable:1', ULONG),
        ('Rsvd:1', ULONG),
        ('DisableSingleBitCorrection:1', ULONG),
        ('EccMode:1', ULONG),
    ]


    class _PCI_SUBSYSTEM_IDS_CAPABILITY(ctypes.Structure):
        pass
    _PCI_SUBSYSTEM_IDS_CAPABILITY._fields_ = [
        ('Header', PCI_CAPABILITIES_HEADER),
        ('Reserved', USHORT),
        ('SubVendorID', USHORT),
        ('SubSystemID', USHORT),
    ]


    PCI_SUBSYSTEM_IDS_CAPABILITY = _PCI_SUBSYSTEM_IDS_CAPABILITY
    PPCI_SUBSYSTEM_IDS_CAPABILITY = POINTER(_PCI_SUBSYSTEM_IDS_CAPABILITY)


    class _PCI_ADVANCED_FEATURES_CAPABILITY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('FunctionLevelResetSupported:1', UCHAR),
        ('TransactionsPendingSupported:1', UCHAR),
        ('Rsvd:6', UCHAR),
    ]


    Capabilities.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    Capabilities._fields_ = [
        ('DUMMYSTRUCTNAME', Capabilities.DUMMYSTRUCTNAME),
        ('AsUCHAR', UCHAR),
    ]


    _PCI_ADVANCED_FEATURES_CAPABILITY.Capabilities = Capabilities
    DUMMYSTRUCTNAME._fields_ = [
        ('InitiateFunctionLevelReset:1', UCHAR),
        ('Rsvd:7', UCHAR),
    ]


    Control.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    Control._fields_ = [
        ('DUMMYSTRUCTNAME', Control.DUMMYSTRUCTNAME),
        ('AsUCHAR', UCHAR),
    ]


    _PCI_ADVANCED_FEATURES_CAPABILITY.Control = Control
    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionsPending:1', UCHAR),
        ('Rsvd:7', UCHAR),
    ]


    Status.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    Status._fields_ = [
        ('DUMMYSTRUCTNAME', Status.DUMMYSTRUCTNAME),
        ('AsUCHAR', UCHAR),
    ]


    _PCI_ADVANCED_FEATURES_CAPABILITY.Status = Status
    _PCI_ADVANCED_FEATURES_CAPABILITY._fields_ = [
        ('Header', PCI_CAPABILITIES_HEADER),
        ('Length', UCHAR),
        ('Capabilities', _PCI_ADVANCED_FEATURES_CAPABILITY.Capabilities),
        ('Control', _PCI_ADVANCED_FEATURES_CAPABILITY.Control),
        ('Status', _PCI_ADVANCED_FEATURES_CAPABILITY.Status),
    ]


    PCI_ADVANCED_FEATURES_CAPABILITY = _PCI_ADVANCED_FEATURES_CAPABILITY
    PPCI_ADVANCED_FEATURES_CAPABILITY = POINTER(_PCI_ADVANCED_FEATURES_CAPABILITY)


    DUMMYSTRUCTNAME._fields_ = [
        ('FunctionLevelResetSupported:1', UCHAR),
        ('TransactionsPendingSupported:1', UCHAR),
        ('Rsvd:6', UCHAR),
    ]


    Capabilities.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    Capabilities._fields_ = [
        ('DUMMYSTRUCTNAME', Capabilities.DUMMYSTRUCTNAME),
        ('AsUCHAR', UCHAR),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('FunctionLevelResetSupported:1', UCHAR),
        ('TransactionsPendingSupported:1', UCHAR),
        ('Rsvd:6', UCHAR),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('InitiateFunctionLevelReset:1', UCHAR),
        ('Rsvd:7', UCHAR),
    ]


    Control.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    Control._fields_ = [
        ('DUMMYSTRUCTNAME', Control.DUMMYSTRUCTNAME),
        ('AsUCHAR', UCHAR),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('InitiateFunctionLevelReset:1', UCHAR),
        ('Rsvd:7', UCHAR),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionsPending:1', UCHAR),
        ('Rsvd:7', UCHAR),
    ]


    Status.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    Status._fields_ = [
        ('DUMMYSTRUCTNAME', Status.DUMMYSTRUCTNAME),
        ('AsUCHAR', UCHAR),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionsPending:1', UCHAR),
        ('Rsvd:7', UCHAR),
    ]


    OSC_FIRMWARE_FAILURE = 0x02
    OSC_UNRECOGNIZED_UUID = 0x04
    OSC_UNRECOGNIZED_REVISION = 0x08
    OSC_CAPABILITIES_MASKED = 0x10
    PCI_ROOT_BUS_OSC_METHOD_CAPABILITY_REVISION = 0x01
    class _PCI_ROOT_BUS_OSC_SUPPORT_FIELD(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ExtendedConfigOpRegions:1', ULONG),
        ('ActiveStatePowerManagement:1', ULONG),
        ('ClockPowerManagement:1', ULONG),
        ('SegmentGroups:1', ULONG),
        ('MessageSignaledInterrupts:1', ULONG),
        ('OptimizedBufferFlushAndFill:1', ULONG),
        ('AspmOptionality:1', ULONG),
        ('Reserved:25', ULONG),
    ]


    u.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    u._fields_ = [
        ('DUMMYSTRUCTNAME', u.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    _PCI_ROOT_BUS_OSC_SUPPORT_FIELD.u = u
    _PCI_ROOT_BUS_OSC_SUPPORT_FIELD._fields_ = [
        ('u', _PCI_ROOT_BUS_OSC_SUPPORT_FIELD.u),
    ]


    PCI_ROOT_BUS_OSC_SUPPORT_FIELD = _PCI_ROOT_BUS_OSC_SUPPORT_FIELD
    PPCI_ROOT_BUS_OSC_SUPPORT_FIELD = POINTER(_PCI_ROOT_BUS_OSC_SUPPORT_FIELD)


    DUMMYSTRUCTNAME._fields_ = [
        ('ExtendedConfigOpRegions:1', ULONG),
        ('ActiveStatePowerManagement:1', ULONG),
        ('ClockPowerManagement:1', ULONG),
        ('SegmentGroups:1', ULONG),
        ('MessageSignaledInterrupts:1', ULONG),
        ('OptimizedBufferFlushAndFill:1', ULONG),
        ('AspmOptionality:1', ULONG),
        ('Reserved:25', ULONG),
    ]


    u.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    u._fields_ = [
        ('DUMMYSTRUCTNAME', u.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('ExtendedConfigOpRegions:1', ULONG),
        ('ActiveStatePowerManagement:1', ULONG),
        ('ClockPowerManagement:1', ULONG),
        ('SegmentGroups:1', ULONG),
        ('MessageSignaledInterrupts:1', ULONG),
        ('OptimizedBufferFlushAndFill:1', ULONG),
        ('AspmOptionality:1', ULONG),
        ('Reserved:25', ULONG),
    ]


    class _PCI_ROOT_BUS_OSC_CONTROL_FIELD(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ExpressNativeHotPlug:1', ULONG),
        ('ShpcNativeHotPlug:1', ULONG),
        ('ExpressNativePME:1', ULONG),
        ('ExpressAdvancedErrorReporting:1', ULONG),
        ('ExpressCapabilityStructure:1', ULONG),
        ('LatencyToleranceReporting:1', ULONG),
        ('Reserved:26', ULONG),
    ]


    u.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    u._fields_ = [
        ('DUMMYSTRUCTNAME', u.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    _PCI_ROOT_BUS_OSC_CONTROL_FIELD.u = u
    _PCI_ROOT_BUS_OSC_CONTROL_FIELD._fields_ = [
        ('u', _PCI_ROOT_BUS_OSC_CONTROL_FIELD.u),
    ]


    PCI_ROOT_BUS_OSC_CONTROL_FIELD = _PCI_ROOT_BUS_OSC_CONTROL_FIELD
    PPCI_ROOT_BUS_OSC_CONTROL_FIELD = POINTER(_PCI_ROOT_BUS_OSC_CONTROL_FIELD)


    DUMMYSTRUCTNAME._fields_ = [
        ('ExpressNativeHotPlug:1', ULONG),
        ('ShpcNativeHotPlug:1', ULONG),
        ('ExpressNativePME:1', ULONG),
        ('ExpressAdvancedErrorReporting:1', ULONG),
        ('ExpressCapabilityStructure:1', ULONG),
        ('LatencyToleranceReporting:1', ULONG),
        ('Reserved:26', ULONG),
    ]


    u.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    u._fields_ = [
        ('DUMMYSTRUCTNAME', u.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    DUMMYSTRUCTNAME._fields_ = [
        ('ExpressNativeHotPlug:1', ULONG),
        ('ShpcNativeHotPlug:1', ULONG),
        ('ExpressNativePME:1', ULONG),
        ('ExpressAdvancedErrorReporting:1', ULONG),
        ('ExpressCapabilityStructure:1', ULONG),
        ('LatencyToleranceReporting:1', ULONG),
        ('Reserved:26', ULONG),
    ]


    class _PCI_FIRMWARE_BUS_CAPS(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('SixtyFourBitDevice:1', UCHAR),
        ('PciXMode1EccCapable:1', UCHAR),
        ('DeviceIdMessagingCapable:1', UCHAR),
        ('ObffWakeSignalCapable:1', UCHAR),
        ('Reserved1:4', UCHAR),
    ]


    _PCI_FIRMWARE_BUS_CAPS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_FIRMWARE_BUS_CAPS._fields_ = [
        ('Type', USHORT),
        ('Length', USHORT), # must be 16
        ('DUMMYSTRUCTNAME', _PCI_FIRMWARE_BUS_CAPS.DUMMYSTRUCTNAME),
        ('CurrentSpeedAndMode', UCHAR),
        ('SupportedSpeedsAndModesLowByte', UCHAR),
        ('SupportedSpeedsAndModesHighByte', UCHAR),
        ('Voltage', UCHAR),
        ('Reserved2', UCHAR * 7),
    ]


    PCI_FIRMWARE_BUS_CAPS = _PCI_FIRMWARE_BUS_CAPS
    PPCI_FIRMWARE_BUS_CAPS = POINTER(_PCI_FIRMWARE_BUS_CAPS)


    DUMMYSTRUCTNAME._fields_ = [
        ('SixtyFourBitDevice:1', UCHAR),
        ('PciXMode1EccCapable:1', UCHAR),
        ('DeviceIdMessagingCapable:1', UCHAR),
        ('ObffWakeSignalCapable:1', UCHAR),
        ('Reserved1:4', UCHAR),
    ]


    class _PCI_FIRMWARE_BUS_CAPS_RETURN_BUFFER(ctypes.Structure):
        pass
    _PCI_FIRMWARE_BUS_CAPS_RETURN_BUFFER._fields_ = [
        ('Version', USHORT),
        ('Status', USHORT),
        ('Length', ULONG),
        ('Caps', PCI_FIRMWARE_BUS_CAPS),
    ]


    PCI_FIRMWARE_BUS_CAPS_RETURN_BUFFER = _PCI_FIRMWARE_BUS_CAPS_RETURN_BUFFER
    PPCI_FIRMWARE_BUS_CAPS_RETURN_BUFFER = POINTER(_PCI_FIRMWARE_BUS_CAPS_RETURN_BUFFER)




    class _PCI_HARDWARE_INTERFACE(ENUM):
        PciConventional = 1
        PciXMode1 = 2
        PciXMode2 = 3
        PciExpress = 4


    PCI_HARDWARE_INTERFACE = _PCI_HARDWARE_INTERFACE
    PPCI_HARDWARE_INTERFACE = POINTER(_PCI_HARDWARE_INTERFACE)
    class PCI_BUS_WIDTH(ENUM):
        BusWidth32Bits = 1
        BusWidth64Bits = 2


    BusWidth32Bits = PCI_BUS_WIDTH.BusWidth32Bits
    BusWidth64Bits = PCI_BUS_WIDTH.BusWidth64Bits
    class _PCI_ROOT_BUS_HARDWARE_CAPABILITY(ctypes.Structure):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('BusCapabilitiesFound', BOOLEAN), # capabilities are valid or not.
        ('CurrentSpeedAndMode', ULONG), # Provides information on current and supported speeds/modes.
        ('SupportedSpeedsAndModes', ULONG),
        ('DeviceIDMessagingCapable', BOOLEAN), # transactions.
        ('SecondaryBusWidth', PCI_BUS_WIDTH), # Provides the width for a PCI interface.
    ]


    _PCI_ROOT_BUS_HARDWARE_CAPABILITY.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_ROOT_BUS_HARDWARE_CAPABILITY._fields_ = [
        ('SecondaryInterface', PCI_HARDWARE_INTERFACE), # Describes the secondary side of a PCI root bus.
        ('DUMMYSTRUCTNAME', _PCI_ROOT_BUS_HARDWARE_CAPABILITY.DUMMYSTRUCTNAME), # 3. A _DSM function 4 is defined for the root bus.
        ('OscFeatureSupport', PCI_ROOT_BUS_OSC_SUPPORT_FIELD), # the bios.
        ('OscControlRequest', PCI_ROOT_BUS_OSC_CONTROL_FIELD),
        ('OscControlGranted', PCI_ROOT_BUS_OSC_CONTROL_FIELD),
    ]


    PCI_ROOT_BUS_HARDWARE_CAPABILITY = _PCI_ROOT_BUS_HARDWARE_CAPABILITY
    PPCI_ROOT_BUS_HARDWARE_CAPABILITY = POINTER(_PCI_ROOT_BUS_HARDWARE_CAPABILITY)


    DUMMYSTRUCTNAME._fields_ = [
        ('BusCapabilitiesFound', BOOLEAN), # capabilities are valid or not.
        ('CurrentSpeedAndMode', ULONG), # Provides information on current and supported speeds/modes.
        ('SupportedSpeedsAndModes', ULONG),
        ('DeviceIDMessagingCapable', BOOLEAN), # transactions.
        ('SecondaryBusWidth', PCI_BUS_WIDTH), # Provides the width for a PCI interface.
    ]


    class _PCI_EXPRESS_CAPABILITIES_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('CapabilityVersion:4', USHORT),
        ('DeviceType:4', USHORT), # PCI_EXPRESS_DEVICE_TYPE
        ('SlotImplemented:1', USHORT),
        ('InterruptMessageNumber:5', USHORT),
        ('Rsvd:2', USHORT),
    ]


    _PCI_EXPRESS_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_CAPABILITIES_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_CAPABILITIES_REGISTER = _PCI_EXPRESS_CAPABILITIES_REGISTER
    PPCI_EXPRESS_CAPABILITIES_REGISTER = POINTER(_PCI_EXPRESS_CAPABILITIES_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('CapabilityVersion:4', USHORT),
        ('DeviceType:4', USHORT), # PCI_EXPRESS_DEVICE_TYPE
        ('SlotImplemented:1', USHORT),
        ('InterruptMessageNumber:5', USHORT),
        ('Rsvd:2', USHORT),
    ]


    class _PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('MaxPayloadSizeSupported:3', ULONG), # EXPRESS_MAX_PAYLOAD_SIZE
        ('PhantomFunctionsSupported:2', ULONG),
        ('ExtendedTagSupported:1', ULONG),
        ('L0sAcceptableLatency:3', ULONG), # EXPRESS_L0S_LATENCY
        ('L1AcceptableLatency:3', ULONG), # EXPRESS_L1_LATENCY
        ('Undefined:3', ULONG),
        ('RoleBasedErrorReporting:1', ULONG),
        ('Rsvd1:2', ULONG),
        ('CapturedSlotPowerLimit:8', ULONG),
        ('CapturedSlotPowerLimitScale:2', ULONG),
        ('FunctionLevelResetCapability:1', ULONG),
        ('Rsvd2:3', ULONG),
    ]


    _PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER = _PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER
    PPCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER = POINTER(_PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('MaxPayloadSizeSupported:3', ULONG), # EXPRESS_MAX_PAYLOAD_SIZE
        ('PhantomFunctionsSupported:2', ULONG),
        ('ExtendedTagSupported:1', ULONG),
        ('L0sAcceptableLatency:3', ULONG), # EXPRESS_L0S_LATENCY
        ('L1AcceptableLatency:3', ULONG), # EXPRESS_L1_LATENCY
        ('Undefined:3', ULONG),
        ('RoleBasedErrorReporting:1', ULONG),
        ('Rsvd1:2', ULONG),
        ('CapturedSlotPowerLimit:8', ULONG),
        ('CapturedSlotPowerLimitScale:2', ULONG),
        ('FunctionLevelResetCapability:1', ULONG),
        ('Rsvd2:3', ULONG),
    ]


    PCI_EXPRESS_AER_DEVICE_CONTROL_MASK = 0x07;
    class _PCI_EXPRESS_DEVICE_CONTROL_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('CorrectableErrorEnable:1', USHORT),
        ('NonFatalErrorEnable:1', USHORT),
        ('FatalErrorEnable:1', USHORT),
        ('UnsupportedRequestErrorEnable:1', USHORT),
        ('EnableRelaxedOrder:1', USHORT),
        ('MaxPayloadSize:3', USHORT), # EXPRESS_MAX_PAYLOAD_SIZE
        ('ExtendedTagEnable:1', USHORT),
        ('PhantomFunctionsEnable:1', USHORT),
        ('AuxPowerEnable:1', USHORT),
        ('NoSnoopEnable:1', USHORT),
        ('MaxReadRequestSize:3', USHORT), # EXPRESS_MAX_PAYLOAD_SIZE
        ('BridgeConfigRetryEnable:1', USHORT),
    ]


    _PCI_EXPRESS_DEVICE_CONTROL_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    DUMMYSTRUCTNAME2._fields_ = [
        (':15', USHORT),
        ('InitiateFunctionLevelReset:1', USHORT),
    ]


    _PCI_EXPRESS_DEVICE_CONTROL_REGISTER.DUMMYSTRUCTNAME2 = DUMMYSTRUCTNAME2
    _PCI_EXPRESS_DEVICE_CONTROL_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_DEVICE_CONTROL_REGISTER.DUMMYSTRUCTNAME),
        ('DUMMYSTRUCTNAME2', _PCI_EXPRESS_DEVICE_CONTROL_REGISTER.DUMMYSTRUCTNAME2), # Hack to allow alias of BridgeConfigRetryEnable bit for FLR.
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_DEVICE_CONTROL_REGISTER = _PCI_EXPRESS_DEVICE_CONTROL_REGISTER
    PPCI_EXPRESS_DEVICE_CONTROL_REGISTER = POINTER(_PCI_EXPRESS_DEVICE_CONTROL_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('CorrectableErrorEnable:1', USHORT),
        ('NonFatalErrorEnable:1', USHORT),
        ('FatalErrorEnable:1', USHORT),
        ('UnsupportedRequestErrorEnable:1', USHORT),
        ('EnableRelaxedOrder:1', USHORT),
        ('MaxPayloadSize:3', USHORT), # EXPRESS_MAX_PAYLOAD_SIZE
        ('ExtendedTagEnable:1', USHORT),
        ('PhantomFunctionsEnable:1', USHORT),
        ('AuxPowerEnable:1', USHORT),
        ('NoSnoopEnable:1', USHORT),
        ('MaxReadRequestSize:3', USHORT), # EXPRESS_MAX_PAYLOAD_SIZE
        ('BridgeConfigRetryEnable:1', USHORT),
    ]


    DUMMYSTRUCTNAME2._fields_ = [
        (':15', USHORT),
        ('InitiateFunctionLevelReset:1', USHORT),
    ]


    PCI_EXPRESS_AER_DEVICE_STATUS_MASK = 0x0F;
    class _PCI_EXPRESS_DEVICE_STATUS_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('CorrectableErrorDetected:1', USHORT),
        ('NonFatalErrorDetected:1', USHORT),
        ('FatalErrorDetected:1', USHORT),
        ('UnsupportedRequestDetected:1', USHORT),
        ('AuxPowerDetected:1', USHORT),
        ('TransactionsPending:1', USHORT),
        ('Rsvd:10', USHORT),
    ]


    _PCI_EXPRESS_DEVICE_STATUS_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_DEVICE_STATUS_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_DEVICE_STATUS_REGISTER.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_DEVICE_STATUS_REGISTER = _PCI_EXPRESS_DEVICE_STATUS_REGISTER
    PPCI_EXPRESS_DEVICE_STATUS_REGISTER = POINTER(_PCI_EXPRESS_DEVICE_STATUS_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('CorrectableErrorDetected:1', USHORT),
        ('NonFatalErrorDetected:1', USHORT),
        ('FatalErrorDetected:1', USHORT),
        ('UnsupportedRequestDetected:1', USHORT),
        ('AuxPowerDetected:1', USHORT),
        ('TransactionsPending:1', USHORT),
        ('Rsvd:10', USHORT),
    ]


    class _PCI_EXPRESS_LINK_CAPABILITIES_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('MaximumLinkSpeed:4', ULONG),
        ('MaximumLinkWidth:6', ULONG),
        ('ActiveStatePMSupport:2', ULONG), # EXPRESS_ASPM_CONFIG
        ('L0sExitLatency:3', ULONG), # EXPRESS_L0S_LATENCY
        ('L1ExitLatency:3', ULONG), # EXPRESS_L1_LATENCY
        ('ClockPowerManagement:1', ULONG),
        ('SurpriseDownErrorReportingCapable:1', ULONG),
        ('DataLinkLayerActiveReportingCapable:1', ULONG),
        ('LinkBandwidthNotificationCapability:1', ULONG),
        ('AspmOptionalityCompliance:1', ULONG),
        ('Rsvd:1', ULONG),
        ('PortNumber:8', ULONG),
    ]


    _PCI_EXPRESS_LINK_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_LINK_CAPABILITIES_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_LINK_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_LINK_CAPABILITIES_REGISTER = _PCI_EXPRESS_LINK_CAPABILITIES_REGISTER
    PPCI_EXPRESS_LINK_CAPABILITIES_REGISTER = POINTER(_PCI_EXPRESS_LINK_CAPABILITIES_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('MaximumLinkSpeed:4', ULONG),
        ('MaximumLinkWidth:6', ULONG),
        ('ActiveStatePMSupport:2', ULONG), # EXPRESS_ASPM_CONFIG
        ('L0sExitLatency:3', ULONG), # EXPRESS_L0S_LATENCY
        ('L1ExitLatency:3', ULONG), # EXPRESS_L1_LATENCY
        ('ClockPowerManagement:1', ULONG),
        ('SurpriseDownErrorReportingCapable:1', ULONG),
        ('DataLinkLayerActiveReportingCapable:1', ULONG),
        ('LinkBandwidthNotificationCapability:1', ULONG),
        ('AspmOptionalityCompliance:1', ULONG),
        ('Rsvd:1', ULONG),
        ('PortNumber:8', ULONG),
    ]


    class _PCI_EXPRESS_LINK_CONTROL_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ActiveStatePMControl:2', USHORT), # EXPRESS_ASPM_CONFIG
        ('Rsvd1:1', USHORT),
        ('ReadCompletionBoundary:1', USHORT), # EXPRESS_RCB
        ('LinkDisable:1', USHORT),
        ('RetrainLink:1', USHORT),
        ('CommonClockConfig:1', USHORT),
        ('ExtendedSynch:1', USHORT),
        ('EnableClockPowerManagement:1', USHORT),
        ('Rsvd2:7', USHORT),
    ]


    _PCI_EXPRESS_LINK_CONTROL_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_LINK_CONTROL_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_LINK_CONTROL_REGISTER.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_LINK_CONTROL_REGISTER = _PCI_EXPRESS_LINK_CONTROL_REGISTER
    PPCI_EXPRESS_LINK_CONTROL_REGISTER = POINTER(_PCI_EXPRESS_LINK_CONTROL_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('ActiveStatePMControl:2', USHORT), # EXPRESS_ASPM_CONFIG
        ('Rsvd1:1', USHORT),
        ('ReadCompletionBoundary:1', USHORT), # EXPRESS_RCB
        ('LinkDisable:1', USHORT),
        ('RetrainLink:1', USHORT),
        ('CommonClockConfig:1', USHORT),
        ('ExtendedSynch:1', USHORT),
        ('EnableClockPowerManagement:1', USHORT),
        ('Rsvd2:7', USHORT),
    ]


    class _PCI_EXPRESS_LINK_STATUS_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('LinkSpeed:4', USHORT),
        ('LinkWidth:6', USHORT),
        ('Undefined:1', USHORT),
        ('LinkTraining:1', USHORT),
        ('SlotClockConfig:1', USHORT),
        ('DataLinkLayerActive:1', USHORT),
        ('Rsvd:2', USHORT),
    ]


    _PCI_EXPRESS_LINK_STATUS_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_LINK_STATUS_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_LINK_STATUS_REGISTER.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_LINK_STATUS_REGISTER = _PCI_EXPRESS_LINK_STATUS_REGISTER
    PPCI_EXPRESS_LINK_STATUS_REGISTER = POINTER(_PCI_EXPRESS_LINK_STATUS_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('LinkSpeed:4', USHORT),
        ('LinkWidth:6', USHORT),
        ('Undefined:1', USHORT),
        ('LinkTraining:1', USHORT),
        ('SlotClockConfig:1', USHORT),
        ('DataLinkLayerActive:1', USHORT),
        ('Rsvd:2', USHORT),
    ]


    class _PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('AttentionButtonPresent:1', ULONG),
        ('PowerControllerPresent:1', ULONG),
        ('MRLSensorPresent:1', ULONG),
        ('AttentionIndicatorPresent:1', ULONG),
        ('PowerIndicatorPresent:1', ULONG),
        ('HotPlugSurprise:1', ULONG),
        ('HotPlugCapable:1', ULONG),
        ('SlotPowerLimit:8', ULONG),
        ('SlotPowerLimitScale:2', ULONG),
        ('ElectromechanicalLockPresent:1', ULONG),
        ('NoCommandCompletedSupport:1', ULONG),
        ('PhysicalSlotNumber:13', ULONG),
    ]


    _PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER = _PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER
    PPCI_EXPRESS_SLOT_CAPABILITIES_REGISTER = POINTER(_PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('AttentionButtonPresent:1', ULONG),
        ('PowerControllerPresent:1', ULONG),
        ('MRLSensorPresent:1', ULONG),
        ('AttentionIndicatorPresent:1', ULONG),
        ('PowerIndicatorPresent:1', ULONG),
        ('HotPlugSurprise:1', ULONG),
        ('HotPlugCapable:1', ULONG),
        ('SlotPowerLimit:8', ULONG),
        ('SlotPowerLimitScale:2', ULONG),
        ('ElectromechanicalLockPresent:1', ULONG),
        ('NoCommandCompletedSupport:1', ULONG),
        ('PhysicalSlotNumber:13', ULONG),
    ]


    class _PCI_EXPRESS_SLOT_CONTROL_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('AttentionButtonEnable:1', USHORT),
        ('PowerFaultDetectEnable:1', USHORT),
        ('MRLSensorEnable:1', USHORT),
        ('PresenceDetectEnable:1', USHORT),
        ('CommandCompletedEnable:1', USHORT),
        ('HotPlugInterruptEnable:1', USHORT),
        ('AttentionIndicatorControl:2', USHORT), # EXPRESS_INDICATOR_STATE
        ('PowerIndicatorControl:2', USHORT), # EXPRESS_INDICATOR_STATE
        ('PowerControllerControl:1', USHORT), # EXPRESS_POWER_STATE
        ('ElectromechanicalLockControl:1', USHORT),
        ('DataLinkStateChangeEnable:1', USHORT),
        ('Rsvd:3', USHORT),
    ]


    _PCI_EXPRESS_SLOT_CONTROL_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_SLOT_CONTROL_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_SLOT_CONTROL_REGISTER.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_SLOT_CONTROL_REGISTER = _PCI_EXPRESS_SLOT_CONTROL_REGISTER
    PPCI_EXPRESS_SLOT_CONTROL_REGISTER = POINTER(_PCI_EXPRESS_SLOT_CONTROL_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('AttentionButtonEnable:1', USHORT),
        ('PowerFaultDetectEnable:1', USHORT),
        ('MRLSensorEnable:1', USHORT),
        ('PresenceDetectEnable:1', USHORT),
        ('CommandCompletedEnable:1', USHORT),
        ('HotPlugInterruptEnable:1', USHORT),
        ('AttentionIndicatorControl:2', USHORT), # EXPRESS_INDICATOR_STATE
        ('PowerIndicatorControl:2', USHORT), # EXPRESS_INDICATOR_STATE
        ('PowerControllerControl:1', USHORT), # EXPRESS_POWER_STATE
        ('ElectromechanicalLockControl:1', USHORT),
        ('DataLinkStateChangeEnable:1', USHORT),
        ('Rsvd:3', USHORT),
    ]


    class _PCI_EXPRESS_SLOT_STATUS_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('AttentionButtonPressed:1', USHORT),
        ('PowerFaultDetected:1', USHORT),
        ('MRLSensorChanged:1', USHORT),
        ('PresenceDetectChanged:1', USHORT),
        ('CommandCompleted:1', USHORT),
        ('MRLSensorState:1', USHORT), # EXPRESS_MRL_STATE
        ('PresenceDetectState:1', USHORT), # EXPRESS_CARD_PRESENCE
        ('ElectromechanicalLockEngaged:1', USHORT),
        ('DataLinkStateChanged:1', USHORT),
        ('Rsvd:7', USHORT),
    ]


    _PCI_EXPRESS_SLOT_STATUS_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_SLOT_STATUS_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_SLOT_STATUS_REGISTER.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_SLOT_STATUS_REGISTER = _PCI_EXPRESS_SLOT_STATUS_REGISTER
    PPCI_EXPRESS_SLOT_STATUS_REGISTER = POINTER(_PCI_EXPRESS_SLOT_STATUS_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('AttentionButtonPressed:1', USHORT),
        ('PowerFaultDetected:1', USHORT),
        ('MRLSensorChanged:1', USHORT),
        ('PresenceDetectChanged:1', USHORT),
        ('CommandCompleted:1', USHORT),
        ('MRLSensorState:1', USHORT), # EXPRESS_MRL_STATE
        ('PresenceDetectState:1', USHORT), # EXPRESS_CARD_PRESENCE
        ('ElectromechanicalLockEngaged:1', USHORT),
        ('DataLinkStateChanged:1', USHORT),
        ('Rsvd:7', USHORT),
    ]


    class _PCI_EXPRESS_ROOT_CONTROL_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('CorrectableSerrEnable:1', USHORT),
        ('NonFatalSerrEnable:1', USHORT),
        ('FatalSerrEnable:1', USHORT),
        ('PMEInterruptEnable:1', USHORT),
        ('CRSSoftwareVisibilityEnable:1', USHORT),
        ('Rsvd:11', USHORT),
    ]


    _PCI_EXPRESS_ROOT_CONTROL_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_ROOT_CONTROL_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_ROOT_CONTROL_REGISTER.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_ROOT_CONTROL_REGISTER = _PCI_EXPRESS_ROOT_CONTROL_REGISTER
    PPCI_EXPRESS_ROOT_CONTROL_REGISTER = POINTER(_PCI_EXPRESS_ROOT_CONTROL_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('CorrectableSerrEnable:1', USHORT),
        ('NonFatalSerrEnable:1', USHORT),
        ('FatalSerrEnable:1', USHORT),
        ('PMEInterruptEnable:1', USHORT),
        ('CRSSoftwareVisibilityEnable:1', USHORT),
        ('Rsvd:11', USHORT),
    ]


    class _PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('CRSSoftwareVisibility:1', USHORT),
        ('Rsvd:15', USHORT),
    ]


    _PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER = _PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER
    PPCI_EXPRESS_ROOT_CAPABILITIES_REGISTER = POINTER(_PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('CRSSoftwareVisibility:1', USHORT),
        ('Rsvd:15', USHORT),
    ]


    class _PCI_EXPRESS_ROOT_STATUS_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('PMERequestorId:16', ULONG), # PCI_EXPRESS_REQUESTOR_ID
        ('PMEStatus:1', ULONG),
        ('PMEPending:1', ULONG),
        ('Rsvd:14', ULONG),
    ]


    _PCI_EXPRESS_ROOT_STATUS_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_ROOT_STATUS_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_ROOT_STATUS_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_ROOT_STATUS_REGISTER = _PCI_EXPRESS_ROOT_STATUS_REGISTER
    PPCI_EXPRESS_ROOT_STATUS_REGISTER = POINTER(_PCI_EXPRESS_ROOT_STATUS_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('PMERequestorId:16', ULONG), # PCI_EXPRESS_REQUESTOR_ID
        ('PMEStatus:1', ULONG),
        ('PMEPending:1', ULONG),
        ('Rsvd:14', ULONG),
    ]


    class _PCI_EXPRESS_DEVICE_CAPABILITIES_2_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('CompletionTimeoutRangesSupported:4', ULONG),
        ('CompletionTimeoutDisableSupported:1', ULONG),
        ('AriForwardingSupported:1', ULONG),
        ('AtomicOpRoutingSupported:1', ULONG),
        ('AtomicOpCompleterSupported32Bit:1', ULONG),
        ('AtomicOpCompleterSupported64Bit:1', ULONG),
        ('CASCompleterSupported128Bit:1', ULONG),
        ('NoROEnabledPRPRPassing:1', ULONG),
        ('LTRMechanismSupported:1', ULONG),
        ('TPHCompleterSupported:2', ULONG),
        ('Rsvd:4', ULONG),
        ('OBFFSupported:2', ULONG),
        ('ExtendedFmtFieldSuported:1', ULONG),
        ('EndEndTLPPrefixSupported:1', ULONG),
        ('MaxEndEndTLPPrefixes:2', ULONG),
        ('Rsvd2:8', ULONG),
    ]


    _PCI_EXPRESS_DEVICE_CAPABILITIES_2_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_DEVICE_CAPABILITIES_2_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_DEVICE_CAPABILITIES_2_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_DEVICE_CAPABILITIES_2_REGISTER = _PCI_EXPRESS_DEVICE_CAPABILITIES_2_REGISTER
    PPCI_EXPRESS_DEVICE_CAPABILITIES_2_REGISTER = POINTER(_PCI_EXPRESS_DEVICE_CAPABILITIES_2_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('CompletionTimeoutRangesSupported:4', ULONG),
        ('CompletionTimeoutDisableSupported:1', ULONG),
        ('AriForwardingSupported:1', ULONG),
        ('AtomicOpRoutingSupported:1', ULONG),
        ('AtomicOpCompleterSupported32Bit:1', ULONG),
        ('AtomicOpCompleterSupported64Bit:1', ULONG),
        ('CASCompleterSupported128Bit:1', ULONG),
        ('NoROEnabledPRPRPassing:1', ULONG),
        ('LTRMechanismSupported:1', ULONG),
        ('TPHCompleterSupported:2', ULONG),
        ('Rsvd:4', ULONG),
        ('OBFFSupported:2', ULONG),
        ('ExtendedFmtFieldSuported:1', ULONG),
        ('EndEndTLPPrefixSupported:1', ULONG),
        ('MaxEndEndTLPPrefixes:2', ULONG),
        ('Rsvd2:8', ULONG),
    ]


    class _PCI_EXPRESS_DEVICE_CONTROL_2_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('CompletionTimeoutValue:4', USHORT),
        ('CompletionTimeoutDisable:1', USHORT),
        ('AriForwardingEnable:1', USHORT),
        ('AtomicOpRequesterEnable:1', USHORT),
        ('AtomicOpEgresBlocking:1', USHORT),
        ('IDORequestEnable:1', USHORT),
        ('IDOCompletionEnable:1', USHORT),
        ('LTRMechanismEnable:1', USHORT),
        ('Rsvd:2', USHORT),
        ('OBFFEnable:2', USHORT),
        ('EndEndTLPPrefixBlocking:1', USHORT),
    ]


    _PCI_EXPRESS_DEVICE_CONTROL_2_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_DEVICE_CONTROL_2_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_DEVICE_CONTROL_2_REGISTER.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_DEVICE_CONTROL_2_REGISTER = _PCI_EXPRESS_DEVICE_CONTROL_2_REGISTER
    PPCI_EXPRESS_DEVICE_CONTROL_2_REGISTER = POINTER(_PCI_EXPRESS_DEVICE_CONTROL_2_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('CompletionTimeoutValue:4', USHORT),
        ('CompletionTimeoutDisable:1', USHORT),
        ('AriForwardingEnable:1', USHORT),
        ('AtomicOpRequesterEnable:1', USHORT),
        ('AtomicOpEgresBlocking:1', USHORT),
        ('IDORequestEnable:1', USHORT),
        ('IDOCompletionEnable:1', USHORT),
        ('LTRMechanismEnable:1', USHORT),
        ('Rsvd:2', USHORT),
        ('OBFFEnable:2', USHORT),
        ('EndEndTLPPrefixBlocking:1', USHORT),
    ]


    class _PCI_EXPRESS_DEVICE_STATUS_2_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Rsvd:16', USHORT),
    ]


    _PCI_EXPRESS_DEVICE_STATUS_2_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_DEVICE_STATUS_2_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_DEVICE_STATUS_2_REGISTER.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_DEVICE_STATUS_2_REGISTER = _PCI_EXPRESS_DEVICE_STATUS_2_REGISTER
    PPCI_EXPRESS_DEVICE_STATUS_2_REGISTER = POINTER(_PCI_EXPRESS_DEVICE_STATUS_2_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('Rsvd:16', USHORT),
    ]


    class _PCI_EXPRESS_CAPABILITY(ctypes.Structure):
        pass
    _PCI_EXPRESS_CAPABILITY._fields_ = [
        ('Header', PCI_CAPABILITIES_HEADER),
        ('ExpressCapabilities', PCI_EXPRESS_CAPABILITIES_REGISTER),
        ('DeviceCapabilities', PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER),
        ('DeviceControl', PCI_EXPRESS_DEVICE_CONTROL_REGISTER),
        ('DeviceStatus', PCI_EXPRESS_DEVICE_STATUS_REGISTER),
        ('LinkCapabilities', PCI_EXPRESS_LINK_CAPABILITIES_REGISTER),
        ('LinkControl', PCI_EXPRESS_LINK_CONTROL_REGISTER),
        ('LinkStatus', PCI_EXPRESS_LINK_STATUS_REGISTER),
        ('SlotCapabilities', PCI_EXPRESS_SLOT_CAPABILITIES_REGISTER),
        ('SlotControl', PCI_EXPRESS_SLOT_CONTROL_REGISTER),
        ('SlotStatus', PCI_EXPRESS_SLOT_STATUS_REGISTER),
        ('RootControl', PCI_EXPRESS_ROOT_CONTROL_REGISTER),
        ('RootCapabilities', PCI_EXPRESS_ROOT_CAPABILITIES_REGISTER),
        ('RootStatus', PCI_EXPRESS_ROOT_STATUS_REGISTER),
        ('DeviceCapabilities2', PCI_EXPRESS_DEVICE_CAPABILITIES_2_REGISTER),
        ('DeviceControl2', PCI_EXPRESS_DEVICE_CONTROL_2_REGISTER),
        ('DeviceStatus2', PCI_EXPRESS_DEVICE_STATUS_2_REGISTER),
    ]


    PCI_EXPRESS_CAPABILITY = _PCI_EXPRESS_CAPABILITY
    PPCI_EXPRESS_CAPABILITY = POINTER(_PCI_EXPRESS_CAPABILITY)




    class PCI_EXPRESS_MRL_STATE(ENUM):
        MRLClosed = 0
        MRLOpen = 1


    MRLClosed = PCI_EXPRESS_MRL_STATE.MRLClosed
    MRLOpen = PCI_EXPRESS_MRL_STATE.MRLOpen
    class PCI_EXPRESS_CARD_PRESENCE(ENUM):
        SlotEmpty = 0
        CardPresent = 1


    SlotEmpty = PCI_EXPRESS_CARD_PRESENCE.SlotEmpty
    CardPresent = PCI_EXPRESS_CARD_PRESENCE.CardPresent
    class PCI_EXPRESS_INDICATOR_STATE(ENUM):
        IndicatorOn = 1
        IndicatorBlink = 2
        IndicatorOff = 3


    IndicatorOn = PCI_EXPRESS_INDICATOR_STATE.IndicatorOn
    IndicatorBlink = PCI_EXPRESS_INDICATOR_STATE.IndicatorBlink
    IndicatorOff = PCI_EXPRESS_INDICATOR_STATE.IndicatorOff
    class PCI_EXPRESS_POWER_STATE(ENUM):
        PowerOn = 0
        PowerOff = 1


    PowerOn = PCI_EXPRESS_POWER_STATE.PowerOn
    PowerOff = PCI_EXPRESS_POWER_STATE.PowerOff
    class PCI_EXPRESS_ASPM_SUPPORT(ENUM):
        NoAspmSupport = 0
        L0sEntrySupport = 1
        L1EntrySupport = 2
        L0sAndL1EntrySupport = 3


    NoAspmSupport = PCI_EXPRESS_ASPM_SUPPORT.NoAspmSupport
    L0sEntrySupport = PCI_EXPRESS_ASPM_SUPPORT.L0sEntrySupport
    L1EntrySupport = PCI_EXPRESS_ASPM_SUPPORT.L1EntrySupport
    L0sAndL1EntrySupport = PCI_EXPRESS_ASPM_SUPPORT.L0sAndL1EntrySupport
    class PCI_EXPRESS_ASPM_CONTROL(ENUM):
        L0sAndL1EntryDisabled = 1
        L0sEntryEnabled = 2
        L1EntryEnabled = 3
        L0sAndL1EntryEnabled = 4


    L0sAndL1EntryDisabled = PCI_EXPRESS_ASPM_CONTROL.L0sAndL1EntryDisabled
    L0sEntryEnabled = PCI_EXPRESS_ASPM_CONTROL.L0sEntryEnabled
    L1EntryEnabled = PCI_EXPRESS_ASPM_CONTROL.L1EntryEnabled
    L0sAndL1EntryEnabled = PCI_EXPRESS_ASPM_CONTROL.L0sAndL1EntryEnabled
    class PCI_EXPRESS_L0s_EXIT_LATENCY(ENUM):
        L0s_Below64ns = 0
        L0s_64ns_128ns = 1
        L0s_128ns_256ns = 2
        L0s_256ns_512ns = 3
        L0s_512ns_1us = 4
        L0s_1us_2us = 5
        L0s_2us_4us = 6
        L0s_Above4us = 7


    L0s_Below64ns = PCI_EXPRESS_L0s_EXIT_LATENCY.L0s_Below64ns
    L0s_64ns_128ns = PCI_EXPRESS_L0s_EXIT_LATENCY.L0s_64ns_128ns
    L0s_128ns_256ns = PCI_EXPRESS_L0s_EXIT_LATENCY.L0s_128ns_256ns
    L0s_256ns_512ns = PCI_EXPRESS_L0s_EXIT_LATENCY.L0s_256ns_512ns
    L0s_512ns_1us = PCI_EXPRESS_L0s_EXIT_LATENCY.L0s_512ns_1us
    L0s_1us_2us = PCI_EXPRESS_L0s_EXIT_LATENCY.L0s_1us_2us
    L0s_2us_4us = PCI_EXPRESS_L0s_EXIT_LATENCY.L0s_2us_4us
    L0s_Above4us = PCI_EXPRESS_L0s_EXIT_LATENCY.L0s_Above4us
    class PCI_EXPRESS_L1_EXIT_LATENCY(ENUM):
        L1_Below1us = 0
        L1_1us_2us = 1
        L1_2us_4us = 2
        L1_4us_8us = 3
        L1_8us_16us = 4
        L1_16us_32us = 5
        L1_32us_64us = 6
        L1_Above64us = 7


    L1_Below1us = PCI_EXPRESS_L1_EXIT_LATENCY.L1_Below1us
    L1_1us_2us = PCI_EXPRESS_L1_EXIT_LATENCY.L1_1us_2us
    L1_2us_4us = PCI_EXPRESS_L1_EXIT_LATENCY.L1_2us_4us
    L1_4us_8us = PCI_EXPRESS_L1_EXIT_LATENCY.L1_4us_8us
    L1_8us_16us = PCI_EXPRESS_L1_EXIT_LATENCY.L1_8us_16us
    L1_16us_32us = PCI_EXPRESS_L1_EXIT_LATENCY.L1_16us_32us
    L1_32us_64us = PCI_EXPRESS_L1_EXIT_LATENCY.L1_32us_64us
    L1_Above64us = PCI_EXPRESS_L1_EXIT_LATENCY.L1_Above64us
    class PCI_EXPRESS_DEVICE_TYPE(ENUM):
        PciExpressEndpoint = 0
        PciExpressLegacyEndpoint = 1
        PciExpressRootPort = 4
        PciExpressUpstreamSwitchPort = 5
        PciExpressDownstreamSwitchPort = 6
        PciExpressToPciXBridge = 7
        PciXToExpressBridge = 8
        PciExpressRootComplexIntegratedEndpoint = 9
        PciExpressRootComplexEventCollector = 10


    PciExpressEndpoint = PCI_EXPRESS_DEVICE_TYPE.PciExpressEndpoint
    PciExpressLegacyEndpoint = PCI_EXPRESS_DEVICE_TYPE.PciExpressLegacyEndpoint
    PciExpressRootPort = PCI_EXPRESS_DEVICE_TYPE.PciExpressRootPort
    PciExpressUpstreamSwitchPort = PCI_EXPRESS_DEVICE_TYPE.PciExpressUpstreamSwitchPort
    PciExpressDownstreamSwitchPort = PCI_EXPRESS_DEVICE_TYPE.PciExpressDownstreamSwitchPort
    PciExpressToPciXBridge = PCI_EXPRESS_DEVICE_TYPE.PciExpressToPciXBridge
    PciXToExpressBridge = PCI_EXPRESS_DEVICE_TYPE.PciXToExpressBridge
    PciExpressRootComplexIntegratedEndpoint = PCI_EXPRESS_DEVICE_TYPE.PciExpressRootComplexIntegratedEndpoint
    PciExpressRootComplexEventCollector = PCI_EXPRESS_DEVICE_TYPE.PciExpressRootComplexEventCollector
    class PCI_EXPRESS_MAX_PAYLOAD_SIZE(ENUM):
        MaxPayload128Bytes = 0
        MaxPayload256Bytes = 1
        MaxPayload512Bytes = 2
        MaxPayload1024Bytes = 3
        MaxPayload2048Bytes = 4
        MaxPayload4096Bytes = 5


    MaxPayload128Bytes = PCI_EXPRESS_MAX_PAYLOAD_SIZE.MaxPayload128Bytes
    MaxPayload256Bytes = PCI_EXPRESS_MAX_PAYLOAD_SIZE.MaxPayload256Bytes
    MaxPayload512Bytes = PCI_EXPRESS_MAX_PAYLOAD_SIZE.MaxPayload512Bytes
    MaxPayload1024Bytes = PCI_EXPRESS_MAX_PAYLOAD_SIZE.MaxPayload1024Bytes
    MaxPayload2048Bytes = PCI_EXPRESS_MAX_PAYLOAD_SIZE.MaxPayload2048Bytes
    MaxPayload4096Bytes = PCI_EXPRESS_MAX_PAYLOAD_SIZE.MaxPayload4096Bytes
    class _PCI_EXPRESS_PME_REQUESTOR_ID(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('FunctionNumber:3', USHORT),
        ('DeviceNumber:5', USHORT),
        ('BusNumber:8', USHORT),
    ]


    _PCI_EXPRESS_PME_REQUESTOR_ID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_PME_REQUESTOR_ID._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_PME_REQUESTOR_ID.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_PME_REQUESTOR_ID = _PCI_EXPRESS_PME_REQUESTOR_ID
    PPCI_EXPRESS_PME_REQUESTOR_ID = POINTER(_PCI_EXPRESS_PME_REQUESTOR_ID)


    DUMMYSTRUCTNAME._fields_ = [
        ('FunctionNumber:3', USHORT),
        ('DeviceNumber:5', USHORT),
        ('BusNumber:8', USHORT),
    ]


    PCI_DATA_TAG = ' ICP'
    PCI_DATA_VERSION = 1
    class _PCIBUSDATA(ctypes.Structure):
        pass
    _PCIBUSDATA._fields_ = [
        ('Tag', ULONG),
        ('Version', ULONG),
        ('ReadConfig', PciReadWriteConfig),
        ('WriteConfig', PciReadWriteConfig),
        ('Pin2Line', PciPin2Line),
        ('Line2Pin', PciLine2Pin),
        ('ParentSlot', PCI_SLOT_NUMBER),
        ('Reserved', PVOID * 4),
    ]


    PCIBUSDATA = _PCIBUSDATA
    PPCIBUSDATA = POINTER(_PCIBUSDATA)


    class _PCI_EXPRESS_LTR_MAX_LATENCY_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('MaxSnoopLatencyValue:10', ULONG),
        ('MaxSnoopLatencyScale:3', ULONG),
        ('Rsvd:2', ULONG),
        ('MaxSnoopRequirement:1', ULONG),
        ('MaxNoSnoopLatencyValue:10', ULONG),
        ('MaxNoSnoopLatencyScale:3', ULONG),
        ('Rsvd2:2', ULONG),
        ('MaxNoSnoopRequirement:1', ULONG),
    ]


    _PCI_EXPRESS_LTR_MAX_LATENCY_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_LTR_MAX_LATENCY_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_LTR_MAX_LATENCY_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_LTR_MAX_LATENCY_REGISTER = _PCI_EXPRESS_LTR_MAX_LATENCY_REGISTER
    PPCI_EXPRESS_LTR_MAX_LATENCY_REGISTER = POINTER(_PCI_EXPRESS_LTR_MAX_LATENCY_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('MaxSnoopLatencyValue:10', ULONG),
        ('MaxSnoopLatencyScale:3', ULONG),
        ('Rsvd:2', ULONG),
        ('MaxSnoopRequirement:1', ULONG),
        ('MaxNoSnoopLatencyValue:10', ULONG),
        ('MaxNoSnoopLatencyScale:3', ULONG),
        ('Rsvd2:2', ULONG),
        ('MaxNoSnoopRequirement:1', ULONG),
    ]


    class _PCI_EXPRESS_LTR_CAPABILITY(ctypes.Structure):
        pass
    _PCI_EXPRESS_LTR_CAPABILITY._fields_ = [
        ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
        ('Latency', PCI_EXPRESS_LTR_MAX_LATENCY_REGISTER),
    ]


    PCI_EXPRESS_LTR_CAPABILITY = _PCI_EXPRESS_LTR_CAPABILITY
    PPCI_EXPRESS_LTR_CAPABILITY = POINTER(_PCI_EXPRESS_LTR_CAPABILITY)


    PCI_EXPRESS_TPH_ST_LOCATION_NONE = 0
    PCI_EXPRESS_TPH_ST_LOCATION_TPH_CAPABILITY = 1
    PCI_EXPRESS_TPH_ST_LOCATION_MSIX_TABLE = 2
    PCI_EXPRESS_TPH_ST_LOCATION_RESERVED = 3
    class _PCI_EXPRESS_TPH_REQUESTER_CAPABILITY_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('NoStModeSupported:1', ULONG),
        ('InteruptVectorModeSupported:1', ULONG),
        ('DeviceSpecificModeSupported:1', ULONG),
        ('Rsvd:5', ULONG),
        ('ExtendedTPHRequesterSupported:1', ULONG),
        ('StTableLocation:2', ULONG),
        ('Rsvd2:5', ULONG),
        ('StTableSize:11', ULONG),
        ('Rsvd3:5', ULONG),
    ]


    _PCI_EXPRESS_TPH_REQUESTER_CAPABILITY_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_TPH_REQUESTER_CAPABILITY_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_TPH_REQUESTER_CAPABILITY_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_TPH_REQUESTER_CAPABILITY_REGISTER = _PCI_EXPRESS_TPH_REQUESTER_CAPABILITY_REGISTER
    PPCI_EXPRESS_TPH_REQUESTER_CAPABILITY_REGISTER = POINTER(_PCI_EXPRESS_TPH_REQUESTER_CAPABILITY_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('NoStModeSupported:1', ULONG),
        ('InteruptVectorModeSupported:1', ULONG),
        ('DeviceSpecificModeSupported:1', ULONG),
        ('Rsvd:5', ULONG),
        ('ExtendedTPHRequesterSupported:1', ULONG),
        ('StTableLocation:2', ULONG),
        ('Rsvd2:5', ULONG),
        ('StTableSize:11', ULONG),
        ('Rsvd3:5', ULONG),
    ]


    class _PCI_EXPRESS_TPH_REQUESTER_CONTROL_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('StModeSelect:3', ULONG),
        ('Rsvd:5', ULONG),
        ('TphRequesterEnable:2', ULONG),
        ('Rsvd2:22', ULONG),
    ]


    _PCI_EXPRESS_TPH_REQUESTER_CONTROL_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_TPH_REQUESTER_CONTROL_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_TPH_REQUESTER_CONTROL_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_TPH_REQUESTER_CONTROL_REGISTER = _PCI_EXPRESS_TPH_REQUESTER_CONTROL_REGISTER
    PPCI_EXPRESS_TPH_REQUESTER_CONTROL_REGISTER = POINTER(_PCI_EXPRESS_TPH_REQUESTER_CONTROL_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('StModeSelect:3', ULONG),
        ('Rsvd:5', ULONG),
        ('TphRequesterEnable:2', ULONG),
        ('Rsvd2:22', ULONG),
    ]


    class _PCI_EXPRESS_TPH_ST_TABLE_ENTRY(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('LowerEntry:8', USHORT),
        ('UpperEntry:8', USHORT),
    ]


    _PCI_EXPRESS_TPH_ST_TABLE_ENTRY.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_TPH_ST_TABLE_ENTRY._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_TPH_ST_TABLE_ENTRY.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_TPH_ST_TABLE_ENTRY = _PCI_EXPRESS_TPH_ST_TABLE_ENTRY
    PPCI_EXPRESS_TPH_ST_TABLE_ENTRY = POINTER(_PCI_EXPRESS_TPH_ST_TABLE_ENTRY)


    DUMMYSTRUCTNAME._fields_ = [
        ('LowerEntry:8', USHORT),
        ('UpperEntry:8', USHORT),
    ]


    class _PCI_EXPRESS_TPH_REQUESTER_CAPABILITY(ctypes.Structure):
        pass
    _PCI_EXPRESS_TPH_REQUESTER_CAPABILITY._fields_ = [
        ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
        ('RequesterCapability', PCI_EXPRESS_TPH_REQUESTER_CAPABILITY_REGISTER),
        ('RequesterControl', PCI_EXPRESS_TPH_REQUESTER_CONTROL_REGISTER),
    ]


    PCI_EXPRESS_TPH_REQUESTER_CAPABILITY = _PCI_EXPRESS_TPH_REQUESTER_CAPABILITY
    PPCI_EXPRESS_TPH_REQUESTER_CAPABILITY = POINTER(_PCI_EXPRESS_TPH_REQUESTER_CAPABILITY)


    class _PCI_EXPRESS_L1_PM_SS_CAPABILITIES_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('PciPmL12Supported:1', ULONG),
        ('PciPmL11Supported:1', ULONG),
        ('AspmL12Supported:1', ULONG),
        ('AspmL11Supported:1', ULONG),
        ('L1PmSsSupported:1', ULONG),
        ('Rsvd:3', ULONG),
        ('PortCommonModeRestoreTime:8', ULONG),
        ('PortTPowerOnScale:2', ULONG),
        ('Rsvd2:1', ULONG),
        ('PortTPowerOnValue:5', ULONG),
        ('Rsvd3:8', ULONG),
    ]


    _PCI_EXPRESS_L1_PM_SS_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_L1_PM_SS_CAPABILITIES_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_L1_PM_SS_CAPABILITIES_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_L1_PM_SS_CAPABILITIES_REGISTER = _PCI_EXPRESS_L1_PM_SS_CAPABILITIES_REGISTER
    PPCI_EXPRESS_L1_PM_SS_CAPABILITIES_REGISTER = POINTER(_PCI_EXPRESS_L1_PM_SS_CAPABILITIES_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('PciPmL12Supported:1', ULONG),
        ('PciPmL11Supported:1', ULONG),
        ('AspmL12Supported:1', ULONG),
        ('AspmL11Supported:1', ULONG),
        ('L1PmSsSupported:1', ULONG),
        ('Rsvd:3', ULONG),
        ('PortCommonModeRestoreTime:8', ULONG),
        ('PortTPowerOnScale:2', ULONG),
        ('Rsvd2:1', ULONG),
        ('PortTPowerOnValue:5', ULONG),
        ('Rsvd3:8', ULONG),
    ]


    class _PCI_EXPRESS_L1_PM_SS_CONTROL_1_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('PciPmL12Enabled:1', ULONG),
        ('PciPmL11Enabled:1', ULONG),
        ('AspmL12Enabled:1', ULONG),
        ('AspmL11Enabled:1', ULONG),
        ('Rsvd:4', ULONG),
        ('CommonModeRestoreTime:8', ULONG),
        ('LtrL12ThresholdValue:10', ULONG),
        ('Rsvd2:3', ULONG),
        ('LtrL12ThresholdScale:3', ULONG),
    ]


    _PCI_EXPRESS_L1_PM_SS_CONTROL_1_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_L1_PM_SS_CONTROL_1_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_L1_PM_SS_CONTROL_1_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_L1_PM_SS_CONTROL_1_REGISTER = _PCI_EXPRESS_L1_PM_SS_CONTROL_1_REGISTER
    PPCI_EXPRESS_L1_PM_SS_CONTROL_1_REGISTER = POINTER(_PCI_EXPRESS_L1_PM_SS_CONTROL_1_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('PciPmL12Enabled:1', ULONG),
        ('PciPmL11Enabled:1', ULONG),
        ('AspmL12Enabled:1', ULONG),
        ('AspmL11Enabled:1', ULONG),
        ('Rsvd:4', ULONG),
        ('CommonModeRestoreTime:8', ULONG),
        ('LtrL12ThresholdValue:10', ULONG),
        ('Rsvd2:3', ULONG),
        ('LtrL12ThresholdScale:3', ULONG),
    ]


    class _PCI_EXPRESS_L1_PM_SS_CONTROL_2_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('TPowerOnScale:2', ULONG),
        ('Rsvd:1', ULONG),
        ('TPowerOnValue:5', ULONG),
        ('Rsvd2:24', ULONG),
    ]


    _PCI_EXPRESS_L1_PM_SS_CONTROL_2_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_L1_PM_SS_CONTROL_2_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_L1_PM_SS_CONTROL_2_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_L1_PM_SS_CONTROL_2_REGISTER = _PCI_EXPRESS_L1_PM_SS_CONTROL_2_REGISTER
    PPCI_EXPRESS_L1_PM_SS_CONTROL_2_REGISTER = POINTER(_PCI_EXPRESS_L1_PM_SS_CONTROL_2_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('TPowerOnScale:2', ULONG),
        ('Rsvd:1', ULONG),
        ('TPowerOnValue:5', ULONG),
        ('Rsvd2:24', ULONG),
    ]


    class _PCI_EXPRESS_L1_PM_SS_CAPABILITY(ctypes.Structure):
        pass
    _PCI_EXPRESS_L1_PM_SS_CAPABILITY._fields_ = [
        ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
        ('L1PmSsCapabilities', PCI_EXPRESS_L1_PM_SS_CAPABILITIES_REGISTER),
        ('L1PmSsControl1', PCI_EXPRESS_L1_PM_SS_CONTROL_1_REGISTER),
        ('L1PmSsControl2', PCI_EXPRESS_L1_PM_SS_CONTROL_2_REGISTER),
    ]


    PCI_EXPRESS_L1_PM_SS_CAPABILITY = _PCI_EXPRESS_L1_PM_SS_CAPABILITY
    PPCI_EXPRESS_L1_PM_SS_CAPABILITY = POINTER(_PCI_EXPRESS_L1_PM_SS_CAPABILITY)


    class _PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Rsvd:4', ULONG),
        ('SizesSupported:20', ULONG),
        ('Rsvd2:8', ULONG),
    ]


    _PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY_REGISTER = _PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY_REGISTER
    PPCI_EXPRESS_RESIZABLE_BAR_CAPABILITY_REGISTER = POINTER(_PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('Rsvd:4', ULONG),
        ('SizesSupported:20', ULONG),
        ('Rsvd2:8', ULONG),
    ]


    class _PCI_EXPRESS_RESIZABLE_BAR_CONTROL_REGISTER(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('BarIndex:3', ULONG),
        ('Rsvd:2', ULONG),
        ('NumberOfResizableBars:3', ULONG),
        ('BarSize:5', ULONG),
        ('Rsvd2:19', ULONG),
    ]


    _PCI_EXPRESS_RESIZABLE_BAR_CONTROL_REGISTER.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_RESIZABLE_BAR_CONTROL_REGISTER._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_RESIZABLE_BAR_CONTROL_REGISTER.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_RESIZABLE_BAR_CONTROL_REGISTER = _PCI_EXPRESS_RESIZABLE_BAR_CONTROL_REGISTER
    PPCI_EXPRESS_RESIZABLE_BAR_CONTROL_REGISTER = POINTER(_PCI_EXPRESS_RESIZABLE_BAR_CONTROL_REGISTER)


    DUMMYSTRUCTNAME._fields_ = [
        ('BarIndex:3', ULONG),
        ('Rsvd:2', ULONG),
        ('NumberOfResizableBars:3', ULONG),
        ('BarSize:5', ULONG),
        ('Rsvd2:19', ULONG),
    ]


    class _PCI_EXPRESS_RESIZABLE_BAR_ENTRY(ctypes.Structure):
        pass
    _PCI_EXPRESS_RESIZABLE_BAR_ENTRY._fields_ = [
        ('Capability', PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY_REGISTER),
        ('Control', PCI_EXPRESS_RESIZABLE_BAR_CONTROL_REGISTER),
    ]


    PCI_EXPRESS_RESIZABLE_BAR_ENTRY = _PCI_EXPRESS_RESIZABLE_BAR_ENTRY
    PPCI_EXPRESS_RESIZABLE_BAR_ENTRY = POINTER(_PCI_EXPRESS_RESIZABLE_BAR_ENTRY)


    class _PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY(ctypes.Structure):
        pass
    _PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY._fields_ = [
        ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
        ('Entry', PCI_EXPRESS_RESIZABLE_BAR_ENTRY * 6),
    ]


    PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY = _PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY
    PPCI_EXPRESS_RESIZABLE_BAR_CAPABILITY = POINTER(_PCI_EXPRESS_RESIZABLE_BAR_CAPABILITY)


    class _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('DvsecVendorId:16', ULONG),
        ('DvsecVersion:4', ULONG),
        ('DvsecLength:12', ULONG),
    ]


    _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1 = _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1
    PPCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1 = POINTER(_PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1)


    DUMMYSTRUCTNAME._fields_ = [
        ('DvsecVendorId:16', ULONG),
        ('DvsecVersion:4', ULONG),
        ('DvsecLength:12', ULONG),
    ]


    class _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('DvsecId:16', USHORT),
    ]


    _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2._fields_ = [
        ('DUMMYSTRUCTNAME', _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2 = _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2
    PPCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2 = POINTER(_PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2)


    DUMMYSTRUCTNAME._fields_ = [
        ('DvsecId:16', USHORT),
    ]


    class _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_CAPABILITY(ctypes.Structure):
        pass
    _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_CAPABILITY._fields_ = [
        ('Header', PCI_EXPRESS_ENHANCED_CAPABILITY_HEADER),
        ('DvsecHeader1', PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1),
        ('DvsecHeader2', PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2),
        ('DvsecRegisters', USHORT * 1),
    ]


    PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_CAPABILITY = _PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_CAPABILITY
    PPCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_CAPABILITY = POINTER(_PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_CAPABILITY)


    PCI_INVALID_ALTERNATE_FUNCTION_NUMBER = 0xFF

    if not defined(_PCIINTRF_X_):
        _PCIINTRF_X_ = 1
        class _PCI_BUS_INTERFACE_STANDARD(ctypes.Structure):
            pass
        _PCI_BUS_INTERFACE_STANDARD._fields_ = [
            ('Size', USHORT), # generic interface header
            ('Version', USHORT),
            ('Context', PVOID),
            ('InterfaceReference', PINTERFACE_REFERENCE),
            ('InterfaceDereference', PINTERFACE_DEREFERENCE),
            ('ReadConfig', PPCI_READ_WRITE_CONFIG), # standard PCI bus interfaces
            ('WriteConfig', PPCI_READ_WRITE_CONFIG),
            ('PinToLine', PPCI_PIN_TO_LINE),
            ('LineToPin', PPCI_LINE_TO_PIN),
            ('RootBusCapability', PPCI_ROOT_BUS_CAPABILITY),
            ('ExpressWakeControl', PPCI_EXPRESS_WAKE_CONTROL),
            ('PrepareMultistageResume', PPCI_PREPARE_MULTISTAGE_RESUME),
        ]


        PCI_BUS_INTERFACE_STANDARD = _PCI_BUS_INTERFACE_STANDARD
        PPCI_BUS_INTERFACE_STANDARD = POINTER(_PCI_BUS_INTERFACE_STANDARD)


        PCI_BUS_INTERFACE_STANDARD_VERSION = 2
        PCI_BUS_INTERFACE_STANDARD_VERSION_1_LENGTH = FIELD_OFFSET(
    PCI_BUS_INTERFACE_STANDARD,
    PrepareMultistageResume,
)
    # END IF

    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN7):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WIN2K):
        pass
    # END IF
    WHEA_PHYSICAL_ADDRESS = LARGE_INTEGER


    class _WHEA_ERROR_SOURCE_TYPE(ENUM):
        WheaErrSrcTypeMCE = 0x00
        WheaErrSrcTypeCMC = 0x01
        WheaErrSrcTypeCPE = 0x02
        WheaErrSrcTypeNMI = 0x03
        WheaErrSrcTypePCIe = 0x04
        WheaErrSrcTypeGeneric = 0x05
        WheaErrSrcTypeINIT = 0x06
        WheaErrSrcTypeBOOT = 0x07
        WheaErrSrcTypeSCIGeneric = 0x08
        WheaErrSrcTypeIPFMCA = 0x09
        WheaErrSrcTypeIPFCMC = 0x0A
        WheaErrSrcTypeIPFCPE = 0x0B
        WheaErrSrcTypeGenericV2 = 0x0C
        WheaErrSrcTypeSCIGenericV2 = 0x0D
        WheaErrSrcTypeMax = 14


    WHEA_ERROR_SOURCE_TYPE = _WHEA_ERROR_SOURCE_TYPE
    PWHEA_ERROR_SOURCE_TYPE = POINTER(_WHEA_ERROR_SOURCE_TYPE)
    class _WHEA_ERROR_SOURCE_STATE(ENUM):
        WheaErrSrcStateStopped = 0x01
        WheaErrSrcStateStarted = 0x02


    WHEA_ERROR_SOURCE_STATE = _WHEA_ERROR_SOURCE_STATE
    PWHEA_ERROR_SOURCE_STATE = POINTER(_WHEA_ERROR_SOURCE_STATE)
    WHEA_ERROR_SOURCE_DESCRIPTOR_VERSION_10 = 10
    WHEA_MAX_MC_BANKS = 32
    WHEA_ERROR_SOURCE_FLAG_FIRMWAREFIRST = 0x00000001
    WHEA_ERROR_SOURCE_FLAG_GLOBAL = 0x00000002
    WHEA_ERROR_SOURCE_FLAG_PREALLOCATE_PER_PROCESSOR = 0x00000004
    WHEA_ERROR_SOURCE_FLAG_DEFAULTSOURCE = 0x80000000
    WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_XPFMCE = 0
    WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_XPFCMC = 1
    WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_XPFNMI = 2
    WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_IPFMCA = 3
    WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_IPFCMC = 4
    WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_IPFCPE = 5
    WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_AERROOTPORT = 6
    WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_AERENDPOINT = 7
    WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_AERBRIDGE = 8
    WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_GENERIC = 9
    WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_GENERIC_V2 = 10
    WHEA_XPF_MC_BANK_STATUSFORMAT_IA32MCA = 0
    WHEA_XPF_MC_BANK_STATUSFORMAT_Intel64MCA = 1
    WHEA_XPF_MC_BANK_STATUSFORMAT_AMD64MCA = 2
    WHEA_NOTIFICATION_TYPE_POLLED = 0
    WHEA_NOTIFICATION_TYPE_EXTERNALINTERRUPT = 1
    WHEA_NOTIFICATION_TYPE_LOCALINTERRUPT = 2
    WHEA_NOTIFICATION_TYPE_SCI = 3
    WHEA_NOTIFICATION_TYPE_NMI = 4
    WHEA_NOTIFICATION_TYPE_CMCI = 5
    WHEA_NOTIFICATION_TYPE_MCE = 6
    WHEA_NOTIFICATION_TYPE_GPIO_SIGNAL = 7
    WHEA_NOTIFICATION_TYPE_ARMV8_SEA = 8
    WHEA_NOTIFICATION_TYPE_ARMV8_SEI = 9
    WHEA_NOTIFICATION_TYPE_EXTERNALINTERRUPT_GSIV = 10
    WHEA_NOTIFICATION_TYPE_SDEI = 11
    class _WHEA_NOTIFICATION_FLAGS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('PollIntervalRW:1', USHORT),
        ('SwitchToPollingThresholdRW:1', USHORT),
        ('SwitchToPollingWindowRW:1', USHORT),
        ('ErrorThresholdRW:1', USHORT),
        ('ErrorThresholdWindowRW:1', USHORT),
        ('Reserved:11', USHORT),
    ]


    _WHEA_NOTIFICATION_FLAGS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_NOTIFICATION_FLAGS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_NOTIFICATION_FLAGS.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    WHEA_NOTIFICATION_FLAGS = _WHEA_NOTIFICATION_FLAGS
    PWHEA_NOTIFICATION_FLAGS = POINTER(_WHEA_NOTIFICATION_FLAGS)


    DUMMYSTRUCTNAME._fields_ = [
        ('PollIntervalRW:1', USHORT),
        ('SwitchToPollingThresholdRW:1', USHORT),
        ('SwitchToPollingWindowRW:1', USHORT),
        ('ErrorThresholdRW:1', USHORT),
        ('ErrorThresholdWindowRW:1', USHORT),
        ('Reserved:11', USHORT),
    ]


    class _XPF_MC_BANK_FLAGS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ClearOnInitializationRW:1', UCHAR),
        ('ControlDataRW:1', UCHAR),
        ('Reserved:6', UCHAR),
    ]


    _XPF_MC_BANK_FLAGS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _XPF_MC_BANK_FLAGS._fields_ = [
        ('DUMMYSTRUCTNAME', _XPF_MC_BANK_FLAGS.DUMMYSTRUCTNAME),
        ('AsUCHAR', UCHAR),
    ]


    XPF_MC_BANK_FLAGS = _XPF_MC_BANK_FLAGS
    PXPF_MC_BANK_FLAGS = POINTER(_XPF_MC_BANK_FLAGS)


    DUMMYSTRUCTNAME._fields_ = [
        ('ClearOnInitializationRW:1', UCHAR),
        ('ControlDataRW:1', UCHAR),
        ('Reserved:6', UCHAR),
    ]


    class _XPF_MCE_FLAGS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('MCG_CapabilityRW:1', ULONG),
        ('MCG_GlobalControlRW:1', ULONG),
        ('Reserved:30', ULONG),
    ]


    _XPF_MCE_FLAGS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _XPF_MCE_FLAGS._fields_ = [
        ('DUMMYSTRUCTNAME', _XPF_MCE_FLAGS.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    XPF_MCE_FLAGS = _XPF_MCE_FLAGS
    PXPF_MCE_FLAGS = POINTER(_XPF_MCE_FLAGS)


    DUMMYSTRUCTNAME._fields_ = [
        ('MCG_CapabilityRW:1', ULONG),
        ('MCG_GlobalControlRW:1', ULONG),
        ('Reserved:30', ULONG),
    ]


    class _AER_ROOTPORT_DESCRIPTOR_FLAGS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('UncorrectableErrorMaskRW:1', USHORT),
        ('UncorrectableErrorSeverityRW:1', USHORT),
        ('CorrectableErrorMaskRW:1', USHORT),
        ('AdvancedCapsAndControlRW:1', USHORT),
        ('RootErrorCommandRW:1', USHORT),
        ('Reserved:11', USHORT),
    ]


    _AER_ROOTPORT_DESCRIPTOR_FLAGS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _AER_ROOTPORT_DESCRIPTOR_FLAGS._fields_ = [
        ('DUMMYSTRUCTNAME', _AER_ROOTPORT_DESCRIPTOR_FLAGS.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    AER_ROOTPORT_DESCRIPTOR_FLAGS = _AER_ROOTPORT_DESCRIPTOR_FLAGS
    PAER_ROOTPORT_DESCRIPTOR_FLAGS = POINTER(_AER_ROOTPORT_DESCRIPTOR_FLAGS)


    DUMMYSTRUCTNAME._fields_ = [
        ('UncorrectableErrorMaskRW:1', USHORT),
        ('UncorrectableErrorSeverityRW:1', USHORT),
        ('CorrectableErrorMaskRW:1', USHORT),
        ('AdvancedCapsAndControlRW:1', USHORT),
        ('RootErrorCommandRW:1', USHORT),
        ('Reserved:11', USHORT),
    ]


    class _AER_ENDPOINT_DESCRIPTOR_FLAGS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('UncorrectableErrorMaskRW:1', USHORT),
        ('UncorrectableErrorSeverityRW:1', USHORT),
        ('CorrectableErrorMaskRW:1', USHORT),
        ('AdvancedCapsAndControlRW:1', USHORT),
        ('Reserved:12', USHORT),
    ]


    _AER_ENDPOINT_DESCRIPTOR_FLAGS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _AER_ENDPOINT_DESCRIPTOR_FLAGS._fields_ = [
        ('DUMMYSTRUCTNAME', _AER_ENDPOINT_DESCRIPTOR_FLAGS.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    AER_ENDPOINT_DESCRIPTOR_FLAGS = _AER_ENDPOINT_DESCRIPTOR_FLAGS
    PAER_ENDPOINT_DESCRIPTOR_FLAGS = POINTER(_AER_ENDPOINT_DESCRIPTOR_FLAGS)


    DUMMYSTRUCTNAME._fields_ = [
        ('UncorrectableErrorMaskRW:1', USHORT),
        ('UncorrectableErrorSeverityRW:1', USHORT),
        ('CorrectableErrorMaskRW:1', USHORT),
        ('AdvancedCapsAndControlRW:1', USHORT),
        ('Reserved:12', USHORT),
    ]


    class _AER_BRIDGE_DESCRIPTOR_FLAGS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('UncorrectableErrorMaskRW:1', USHORT),
        ('UncorrectableErrorSeverityRW:1', USHORT),
        ('CorrectableErrorMaskRW:1', USHORT),
        ('AdvancedCapsAndControlRW:1', USHORT),
        ('SecondaryUncorrectableErrorMaskRW:1', USHORT),
        ('SecondaryUncorrectableErrorSevRW:1', USHORT),
        ('SecondaryCapsAndControlRW:1', USHORT),
        ('Reserved:9', USHORT),
    ]


    _AER_BRIDGE_DESCRIPTOR_FLAGS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _AER_BRIDGE_DESCRIPTOR_FLAGS._fields_ = [
        ('DUMMYSTRUCTNAME', _AER_BRIDGE_DESCRIPTOR_FLAGS.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    AER_BRIDGE_DESCRIPTOR_FLAGS = _AER_BRIDGE_DESCRIPTOR_FLAGS
    PAER_BRIDGE_DESCRIPTOR_FLAGS = POINTER(_AER_BRIDGE_DESCRIPTOR_FLAGS)


    DUMMYSTRUCTNAME._fields_ = [
        ('UncorrectableErrorMaskRW:1', USHORT),
        ('UncorrectableErrorSeverityRW:1', USHORT),
        ('CorrectableErrorMaskRW:1', USHORT),
        ('AdvancedCapsAndControlRW:1', USHORT),
        ('SecondaryUncorrectableErrorMaskRW:1', USHORT),
        ('SecondaryUncorrectableErrorSevRW:1', USHORT),
        ('SecondaryCapsAndControlRW:1', USHORT),
        ('Reserved:9', USHORT),
    ]


    class _WHEA_NOTIFICATION_DESCRIPTOR(ctypes.Structure):
        pass
    Polled._fields_ = [
        ('PollInterval', ULONG),
    ]


    u.Polled = Polled
    Interrupt._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Interrupt = Interrupt
    LocalInterrupt._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.LocalInterrupt = LocalInterrupt
    Sci._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Sci = Sci
    Nmi._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Nmi = Nmi
    Sea._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Sea = Sea
    Sei._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Sei = Sei
    Gsiv._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Gsiv = Gsiv
    u._fields_ = [
        ('Polled', u.Polled),
        ('Interrupt', u.Interrupt),
        ('LocalInterrupt', u.LocalInterrupt),
        ('Sci', u.Sci),
        ('Nmi', u.Nmi),
        ('Sea', u.Sea),
        ('Sei', u.Sei),
        ('Gsiv', u.Gsiv),
    ]


    _WHEA_NOTIFICATION_DESCRIPTOR.u = u
    _WHEA_NOTIFICATION_DESCRIPTOR._fields_ = [
        ('Type', UCHAR),
        ('Length', UCHAR),
        ('Flags', WHEA_NOTIFICATION_FLAGS),
        ('u', _WHEA_NOTIFICATION_DESCRIPTOR.u),
    ]


    WHEA_NOTIFICATION_DESCRIPTOR = _WHEA_NOTIFICATION_DESCRIPTOR
    PWHEA_NOTIFICATION_DESCRIPTOR = POINTER(_WHEA_NOTIFICATION_DESCRIPTOR)


    Polled._fields_ = [
        ('PollInterval', ULONG),
    ]


    u.Polled = Polled
    Interrupt._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Interrupt = Interrupt
    LocalInterrupt._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.LocalInterrupt = LocalInterrupt
    Sci._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Sci = Sci
    Nmi._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Nmi = Nmi
    Sea._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Sea = Sea
    Sei._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Sei = Sei
    Gsiv._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    u.Gsiv = Gsiv
    u._fields_ = [
        ('Polled', u.Polled),
        ('Interrupt', u.Interrupt),
        ('LocalInterrupt', u.LocalInterrupt),
        ('Sci', u.Sci),
        ('Nmi', u.Nmi),
        ('Sea', u.Sea),
        ('Sei', u.Sei),
        ('Gsiv', u.Gsiv),
    ]


    Polled._fields_ = [
        ('PollInterval', ULONG),
    ]


    Interrupt._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    LocalInterrupt._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    Sci._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    Nmi._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    Sea._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    Sei._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    Gsiv._fields_ = [
        ('PollInterval', ULONG),
        ('Vector', ULONG),
        ('SwitchToPollingThreshold', ULONG),
        ('SwitchToPollingWindow', ULONG),
        ('ErrorThreshold', ULONG),
        ('ErrorThresholdWindow', ULONG),
    ]


    class _WHEA_XPF_MC_BANK_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_XPF_MC_BANK_DESCRIPTOR._fields_ = [
        ('BankNumber', UCHAR),
        ('ClearOnInitialization', BOOLEAN),
        ('StatusDataFormat', UCHAR),
        ('Flags', XPF_MC_BANK_FLAGS),
        ('ControlMsr', ULONG),
        ('StatusMsr', ULONG),
        ('AddressMsr', ULONG),
        ('MiscMsr', ULONG),
        ('ControlData', ULONGLONG),
    ]


    WHEA_XPF_MC_BANK_DESCRIPTOR = _WHEA_XPF_MC_BANK_DESCRIPTOR
    PWHEA_XPF_MC_BANK_DESCRIPTOR = POINTER(_WHEA_XPF_MC_BANK_DESCRIPTOR)


    class _WHEA_XPF_MCE_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_XPF_MCE_DESCRIPTOR._fields_ = [
        ('Type', USHORT),
        ('Enabled', UCHAR),
        ('NumberOfBanks', UCHAR),
        ('Flags', XPF_MCE_FLAGS),
        ('MCG_Capability', ULONGLONG),
        ('MCG_GlobalControl', ULONGLONG),
        ('Banks', WHEA_XPF_MC_BANK_DESCRIPTOR * WHEA_MAX_MC_BANKS),
    ]


    WHEA_XPF_MCE_DESCRIPTOR = _WHEA_XPF_MCE_DESCRIPTOR
    PWHEA_XPF_MCE_DESCRIPTOR = POINTER(_WHEA_XPF_MCE_DESCRIPTOR)


    class _WHEA_XPF_CMC_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_XPF_CMC_DESCRIPTOR._fields_ = [
        ('Type', USHORT),
        ('Enabled', BOOLEAN),
        ('NumberOfBanks', UCHAR),
        ('Reserved', ULONG),
        ('Notify', WHEA_NOTIFICATION_DESCRIPTOR),
        ('Banks', WHEA_XPF_MC_BANK_DESCRIPTOR * WHEA_MAX_MC_BANKS),
    ]


    WHEA_XPF_CMC_DESCRIPTOR = _WHEA_XPF_CMC_DESCRIPTOR
    PWHEA_XPF_CMC_DESCRIPTOR = POINTER(_WHEA_XPF_CMC_DESCRIPTOR)


    class _WHEA_PCI_SLOT_NUMBER(ctypes.Structure):
        pass
    bits._fields_ = [
        ('DeviceNumber:5', ULONG),
        ('FunctionNumber:3', ULONG),
        ('Reserved:24', ULONG),
    ]


    u.bits = bits
    u._fields_ = [
        ('bits', u.bits),
        ('AsULONG', ULONG),
    ]


    _WHEA_PCI_SLOT_NUMBER.u = u
    _WHEA_PCI_SLOT_NUMBER._fields_ = [
        ('u', _WHEA_PCI_SLOT_NUMBER.u),
    ]


    WHEA_PCI_SLOT_NUMBER = _WHEA_PCI_SLOT_NUMBER
    PWHEA_PCI_SLOT_NUMBER = POINTER(_WHEA_PCI_SLOT_NUMBER)


    bits._fields_ = [
        ('DeviceNumber:5', ULONG),
        ('FunctionNumber:3', ULONG),
        ('Reserved:24', ULONG),
    ]


    u.bits = bits
    u._fields_ = [
        ('bits', u.bits),
        ('AsULONG', ULONG),
    ]


    bits._fields_ = [
        ('DeviceNumber:5', ULONG),
        ('FunctionNumber:3', ULONG),
        ('Reserved:24', ULONG),
    ]


    class _WHEA_XPF_NMI_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_XPF_NMI_DESCRIPTOR._fields_ = [
        ('Type', USHORT),
        ('Enabled', BOOLEAN),
    ]


    WHEA_XPF_NMI_DESCRIPTOR = _WHEA_XPF_NMI_DESCRIPTOR
    PWHEA_XPF_NMI_DESCRIPTOR = POINTER(_WHEA_XPF_NMI_DESCRIPTOR)


    class _WHEA_AER_ROOTPORT_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_AER_ROOTPORT_DESCRIPTOR._fields_ = [
        ('Type', USHORT),
        ('Enabled', BOOLEAN),
        ('Reserved', UCHAR),
        ('BusNumber', ULONG),
        ('Slot', WHEA_PCI_SLOT_NUMBER),
        ('DeviceControl', USHORT),
        ('Flags', AER_ROOTPORT_DESCRIPTOR_FLAGS),
        ('UncorrectableErrorMask', ULONG),
        ('UncorrectableErrorSeverity', ULONG),
        ('CorrectableErrorMask', ULONG),
        ('AdvancedCapsAndControl', ULONG),
        ('RootErrorCommand', ULONG),
    ]


    WHEA_AER_ROOTPORT_DESCRIPTOR = _WHEA_AER_ROOTPORT_DESCRIPTOR
    PWHEA_AER_ROOTPORT_DESCRIPTOR = POINTER(_WHEA_AER_ROOTPORT_DESCRIPTOR)


    class _WHEA_AER_ENDPOINT_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_AER_ENDPOINT_DESCRIPTOR._fields_ = [
        ('Type', USHORT),
        ('Enabled', BOOLEAN),
        ('Reserved', UCHAR),
        ('BusNumber', ULONG),
        ('Slot', WHEA_PCI_SLOT_NUMBER),
        ('DeviceControl', USHORT),
        ('Flags', AER_ENDPOINT_DESCRIPTOR_FLAGS),
        ('UncorrectableErrorMask', ULONG),
        ('UncorrectableErrorSeverity', ULONG),
        ('CorrectableErrorMask', ULONG),
        ('AdvancedCapsAndControl', ULONG),
    ]


    WHEA_AER_ENDPOINT_DESCRIPTOR = _WHEA_AER_ENDPOINT_DESCRIPTOR
    PWHEA_AER_ENDPOINT_DESCRIPTOR = POINTER(_WHEA_AER_ENDPOINT_DESCRIPTOR)


    class _WHEA_AER_BRIDGE_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_AER_BRIDGE_DESCRIPTOR._fields_ = [
        ('Type', USHORT),
        ('Enabled', BOOLEAN),
        ('Reserved', UCHAR),
        ('BusNumber', ULONG),
        ('Slot', WHEA_PCI_SLOT_NUMBER),
        ('DeviceControl', USHORT),
        ('Flags', AER_BRIDGE_DESCRIPTOR_FLAGS),
        ('UncorrectableErrorMask', ULONG),
        ('UncorrectableErrorSeverity', ULONG),
        ('CorrectableErrorMask', ULONG),
        ('AdvancedCapsAndControl', ULONG),
        ('SecondaryUncorrectableErrorMask', ULONG),
        ('SecondaryUncorrectableErrorSev', ULONG),
        ('SecondaryCapsAndControl', ULONG),
    ]


    WHEA_AER_BRIDGE_DESCRIPTOR = _WHEA_AER_BRIDGE_DESCRIPTOR
    PWHEA_AER_BRIDGE_DESCRIPTOR = POINTER(_WHEA_AER_BRIDGE_DESCRIPTOR)


    class _WHEA_GENERIC_ERROR_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_GENERIC_ERROR_DESCRIPTOR._fields_ = [
        ('Type', USHORT), # Type is WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_GENERIC.
        ('Reserved', UCHAR), # This field is reserved.
        ('Enabled', UCHAR), # Indicates whether the generic error source is to be enabled.
        ('ErrStatusBlockLength', ULONG), # Length of the error status block.
        ('RelatedErrorSourceId', ULONG), # it's identifier here.
        ('ErrStatusAddressSpaceID', UCHAR), # from the error source.
        ('ErrStatusAddressBitWidth', UCHAR),
        ('ErrStatusAddressBitOffset', UCHAR),
        ('ErrStatusAddressAccessSize', UCHAR),
        ('ErrStatusAddress', WHEA_PHYSICAL_ADDRESS),
        ('Notify', WHEA_NOTIFICATION_DESCRIPTOR), # information is available.
    ]


    WHEA_GENERIC_ERROR_DESCRIPTOR = _WHEA_GENERIC_ERROR_DESCRIPTOR
    PWHEA_GENERIC_ERROR_DESCRIPTOR = POINTER(_WHEA_GENERIC_ERROR_DESCRIPTOR)


    class _WHEA_GENERIC_ERROR_DESCRIPTOR_V2(ctypes.Structure):
        pass
    _WHEA_GENERIC_ERROR_DESCRIPTOR_V2._fields_ = [
        ('Type', USHORT), # Type is WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_GENERIC_V2.
        ('Reserved', UCHAR), # This field is reserved.
        ('Enabled', UCHAR), # Indicates whether the generic error source is to be enabled.
        ('ErrStatusBlockLength', ULONG), # Length of the error status block.
        ('RelatedErrorSourceId', ULONG), # it's identifier here.
        ('ErrStatusAddressSpaceID', UCHAR), # from the error source.
        ('ErrStatusAddressBitWidth', UCHAR),
        ('ErrStatusAddressBitOffset', UCHAR),
        ('ErrStatusAddressAccessSize', UCHAR),
        ('ErrStatusAddress', WHEA_PHYSICAL_ADDRESS),
        ('Notify', WHEA_NOTIFICATION_DESCRIPTOR), # information is available.
        ('ReadAckAddressSpaceID', UCHAR), # error status block.
        ('ReadAckAddressBitWidth', UCHAR),
        ('ReadAckAddressBitOffset', UCHAR),
        ('ReadAckAddressAccessSize', UCHAR),
        ('ReadAckAddress', WHEA_PHYSICAL_ADDRESS),
        ('ReadAckPreserveMask', ULONGLONG),
        ('ReadAckWriteMask', ULONGLONG),
    ]


    WHEA_GENERIC_ERROR_DESCRIPTOR_V2 = _WHEA_GENERIC_ERROR_DESCRIPTOR_V2
    PWHEA_GENERIC_ERROR_DESCRIPTOR_V2 = POINTER(_WHEA_GENERIC_ERROR_DESCRIPTOR_V2)


    class _WHEA_IPF_MCA_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_IPF_MCA_DESCRIPTOR._fields_ = [
        ('Type', USHORT),
        ('Enabled', UCHAR),
        ('Reserved', UCHAR),
    ]


    WHEA_IPF_MCA_DESCRIPTOR = _WHEA_IPF_MCA_DESCRIPTOR
    PWHEA_IPF_MCA_DESCRIPTOR = POINTER(_WHEA_IPF_MCA_DESCRIPTOR)


    class _WHEA_IPF_CMC_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_IPF_CMC_DESCRIPTOR._fields_ = [
        ('Type', USHORT),
        ('Enabled', UCHAR),
        ('Reserved', UCHAR),
    ]


    WHEA_IPF_CMC_DESCRIPTOR = _WHEA_IPF_CMC_DESCRIPTOR
    PWHEA_IPF_CMC_DESCRIPTOR = POINTER(_WHEA_IPF_CMC_DESCRIPTOR)


    class _WHEA_IPF_CPE_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_IPF_CPE_DESCRIPTOR._fields_ = [
        ('Type', USHORT),
        ('Enabled', UCHAR),
        ('Reserved', UCHAR),
    ]


    WHEA_IPF_CPE_DESCRIPTOR = _WHEA_IPF_CPE_DESCRIPTOR
    PWHEA_IPF_CPE_DESCRIPTOR = POINTER(_WHEA_IPF_CPE_DESCRIPTOR)


    class _WHEA_ERROR_SOURCE_DESCRIPTOR(ctypes.Structure):
        pass
    Info._fields_ = [
        ('XpfMceDescriptor', WHEA_XPF_MCE_DESCRIPTOR),
        ('XpfCmcDescriptor', WHEA_XPF_CMC_DESCRIPTOR),
        ('XpfNmiDescriptor', WHEA_XPF_NMI_DESCRIPTOR),
        ('IpfMcaDescriptor', WHEA_IPF_MCA_DESCRIPTOR),
        ('IpfCmcDescriptor', WHEA_IPF_CMC_DESCRIPTOR),
        ('IpfCpeDescriptor', WHEA_IPF_CPE_DESCRIPTOR),
        ('AerRootportDescriptor', WHEA_AER_ROOTPORT_DESCRIPTOR),
        ('AerEndpointDescriptor', WHEA_AER_ENDPOINT_DESCRIPTOR),
        ('AerBridgeDescriptor', WHEA_AER_BRIDGE_DESCRIPTOR),
        ('GenErrDescriptor', WHEA_GENERIC_ERROR_DESCRIPTOR),
        ('GenErrDescriptorV2', WHEA_GENERIC_ERROR_DESCRIPTOR_V2),
    ]


    _WHEA_ERROR_SOURCE_DESCRIPTOR.Info = Info
    _WHEA_ERROR_SOURCE_DESCRIPTOR._fields_ = [
        ('Length', ULONG), # + 00 (0)
        ('Version', ULONG), # + 04 (4)
        ('Type', WHEA_ERROR_SOURCE_TYPE), # + 08 (8)
        ('State', WHEA_ERROR_SOURCE_STATE), # + 0C (12)
        ('MaxRawDataLength', ULONG), # + 10 (16)
        ('NumRecordsToPreallocate', ULONG), # + 14 (20)
        ('MaxSectionsPerRecord', ULONG), # + 18 (24)
        ('ErrorSourceId', ULONG), # + 1C (28)
        ('PlatformErrorSourceId', ULONG), # + 20 (32)
        ('Flags', ULONG), # + 24 (36)
        ('Info', _WHEA_ERROR_SOURCE_DESCRIPTOR.Info), # + 28 (40)
    ]


    WHEA_ERROR_SOURCE_DESCRIPTOR = _WHEA_ERROR_SOURCE_DESCRIPTOR
    PWHEA_ERROR_SOURCE_DESCRIPTOR = POINTER(_WHEA_ERROR_SOURCE_DESCRIPTOR)


    Info._fields_ = [
        ('XpfCmcDescriptor', WHEA_XPF_CMC_DESCRIPTOR), # + 28 (40) WHEA_XPF_MCE_DESCRIPTOR XpfMceDescriptor;
        ('XpfNmiDescriptor', WHEA_XPF_NMI_DESCRIPTOR),
        ('IpfMcaDescriptor', WHEA_IPF_MCA_DESCRIPTOR),
        ('IpfCmcDescriptor', WHEA_IPF_CMC_DESCRIPTOR),
        ('IpfCpeDescriptor', WHEA_IPF_CPE_DESCRIPTOR),
        ('AerRootportDescriptor', WHEA_AER_ROOTPORT_DESCRIPTOR),
        ('AerEndpointDescriptor', WHEA_AER_ENDPOINT_DESCRIPTOR),
        ('AerBridgeDescriptor', WHEA_AER_BRIDGE_DESCRIPTOR),
        ('GenErrDescriptor', WHEA_GENERIC_ERROR_DESCRIPTOR),
        ('GenErrDescriptorV2', WHEA_GENERIC_ERROR_DESCRIPTOR_V2),
    ]


    WHEA_DISABLE_OFFLINE = 0
    WHEA_MEM_PERSISTOFFLINE = 1
    WHEA_MEM_PFA_DISABLE = 2
    WHEA_MEM_PFA_PAGECOUNT = 3
    WHEA_MEM_PFA_THRESHOLD = 4
    WHEA_MEM_PFA_TIMEOUT = 5
    WHEA_DISABLE_DUMMY_WRITE = 6


def CPER_FIELD_CHECK(type, field, offset, length):
    return C_ASSERT(((FIELD_OFFSETtype, field == offset) and (RTL_FIELD_SIZEtype, field == length)))

    if WHEA_DOWNLEVEL_TYPE_NAMES:
        PROCESSOR_GENERIC_SECTION_GUID = PROCESSOR_GENERIC_ERROR_SECTION_GUID
        X86_PROCESSOR_SPECIFIC_SECTION_GUID = XPF_PROCESSOR_ERROR_SECTION_GUID
        IPF_PROCESSOR_SPECIFIC_SECTION_GUID = IPF_PROCESSOR_ERROR_SECTION_GUID
        ARM_PROCESSOR_SPECIFIC_SECTION_GUID = ARM_PROCESSOR_ERROR_SECTION_GUID
        PLATFORM_MEMORY_SECTION_GUID = MEMORY_ERROR_SECTION_GUID
        PCIEXPRESS_SECTION_GUID = PCIEXPRESS_ERROR_SECTION_GUID
        PCIX_BUS_SECTION_GUID = PCIXBUS_ERROR_SECTION_GUID
        PCIX_COMPONENT_SECTION_GUID = PCIXDEVICE_ERROR_SECTION_GUID
        IPF_SAL_RECORD_REFERENCE_SECTION_GUID = FIRMWARE_ERROR_RECORD_REFERENCE_GUID
    # END IF
    class _WHEA_REVISION(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('MinorRevision', UCHAR),
        ('MajorRevision', UCHAR),
    ]


    _WHEA_REVISION.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_REVISION._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_REVISION.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    WHEA_REVISION = _WHEA_REVISION
    PWHEA_REVISION = POINTER(_WHEA_REVISION)


    DUMMYSTRUCTNAME._fields_ = [
        ('MinorRevision', UCHAR),
        ('MajorRevision', UCHAR),
    ]




    class _WHEA_ERROR_SEVERITY(ENUM):
        WheaErrSevRecoverable = 0
        WheaErrSevFatal = 1
        WheaErrSevCorrected = 2
        WheaErrSevInformational = 3


    WHEA_ERROR_SEVERITY = _WHEA_ERROR_SEVERITY
    PWHEA_ERROR_SEVERITY = POINTER(_WHEA_ERROR_SEVERITY)
    class _WHEA_TIMESTAMP(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Seconds:8', ULONGLONG),
        ('Minutes:8', ULONGLONG),
        ('Hours:8', ULONGLONG),
        ('Precise:1', ULONGLONG),
        ('Reserved:7', ULONGLONG),
        ('Day:8', ULONGLONG),
        ('Month:8', ULONGLONG),
        ('Year:8', ULONGLONG),
        ('Century:8', ULONGLONG),
    ]


    _WHEA_TIMESTAMP.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_TIMESTAMP._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_TIMESTAMP.DUMMYSTRUCTNAME),
        ('AsLARGE_INTEGER', LARGE_INTEGER),
    ]


    WHEA_TIMESTAMP = _WHEA_TIMESTAMP
    PWHEA_TIMESTAMP = POINTER(_WHEA_TIMESTAMP)


    DUMMYSTRUCTNAME._fields_ = [
        ('Seconds:8', ULONGLONG),
        ('Minutes:8', ULONGLONG),
        ('Hours:8', ULONGLONG),
        ('Precise:1', ULONGLONG),
        ('Reserved:7', ULONGLONG),
        ('Day:8', ULONGLONG),
        ('Month:8', ULONGLONG),
        ('Year:8', ULONGLONG),
        ('Century:8', ULONGLONG),
    ]


    class _WHEA_PERSISTENCE_INFO(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Signature:16', ULONGLONG),
        ('Length:24', ULONGLONG),
        ('Identifier:16', ULONGLONG),
        ('Attributes:2', ULONGLONG),
        ('DoNotLog:1', ULONGLONG),
        ('Reserved:5', ULONGLONG),
    ]


    _WHEA_PERSISTENCE_INFO.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_PERSISTENCE_INFO._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_PERSISTENCE_INFO.DUMMYSTRUCTNAME),
        ('AsULONGLONG', ULONGLONG),
    ]


    WHEA_PERSISTENCE_INFO = _WHEA_PERSISTENCE_INFO
    PWHEA_PERSISTENCE_INFO = POINTER(_WHEA_PERSISTENCE_INFO)


    DUMMYSTRUCTNAME._fields_ = [
        ('Signature:16', ULONGLONG),
        ('Length:24', ULONGLONG),
        ('Identifier:16', ULONGLONG),
        ('Attributes:2', ULONGLONG),
        ('DoNotLog:1', ULONGLONG),
        ('Reserved:5', ULONGLONG),
    ]


    ERRTYP_INTERNAL = 0x01
    ERRTYP_BUS = 0x10
    ERRTYP_MEM = 0x04
    ERRTYP_TLB = 0x05
    ERRTYP_CACHE = 0x06
    ERRTYP_FUNCTION = 0x07
    ERRTYP_SELFTEST = 0x08
    ERRTYP_FLOW = 0x09
    ERRTYP_MAP = 0x11
    ERRTYP_IMPROPER = 0x12
    ERRTYP_UNIMPL = 0x13
    ERRTYP_LOSSOFLOCKSTEP = 0x14
    ERRTYP_RESPONSE = 0x15
    ERRTYP_PARITY = 0x16
    ERRTYP_PROTOCOL = 0x17
    ERRTYP_PATHERROR = 0x18
    ERRTYP_TIMEOUT = 0x19
    ERRTYP_POISONED = 0x1A
    class _WHEA_ERROR_STATUS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Reserved1:8', ULONGLONG),
        ('ErrorType:8', ULONGLONG),
        ('Address:1', ULONGLONG),
        ('Control:1', ULONGLONG),
        ('Data:1', ULONGLONG),
        ('Responder:1', ULONGLONG),
        ('Requester:1', ULONGLONG),
        ('FirstError:1', ULONGLONG),
        ('Overflow:1', ULONGLONG),
        ('Reserved2:41', ULONGLONG),
    ]


    _WHEA_ERROR_STATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ERROR_STATUS._fields_ = [
        ('ErrorStatus', ULONGLONG),
        ('DUMMYSTRUCTNAME', _WHEA_ERROR_STATUS.DUMMYSTRUCTNAME),
    ]


    WHEA_ERROR_STATUS = _WHEA_ERROR_STATUS
    PWHEA_ERROR_STATUS = POINTER(_WHEA_ERROR_STATUS)


    DUMMYSTRUCTNAME._fields_ = [
        ('Reserved1:8', ULONGLONG),
        ('ErrorType:8', ULONGLONG),
        ('Address:1', ULONGLONG),
        ('Control:1', ULONGLONG),
        ('Data:1', ULONGLONG),
        ('Responder:1', ULONGLONG),
        ('Requester:1', ULONGLONG),
        ('FirstError:1', ULONGLONG),
        ('Overflow:1', ULONGLONG),
        ('Reserved2:41', ULONGLONG),
    ]


    class _WHEA_ERROR_RECORD_HEADER_VALIDBITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('PlatformId:1', ULONG),
        ('Timestamp:1', ULONG),
        ('PartitionId:1', ULONG),
        ('Reserved:29', ULONG),
    ]


    _WHEA_ERROR_RECORD_HEADER_VALIDBITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ERROR_RECORD_HEADER_VALIDBITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ERROR_RECORD_HEADER_VALIDBITS.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_ERROR_RECORD_HEADER_VALIDBITS = _WHEA_ERROR_RECORD_HEADER_VALIDBITS
    PWHEA_ERROR_RECORD_HEADER_VALIDBITS = POINTER(_WHEA_ERROR_RECORD_HEADER_VALIDBITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('PlatformId:1', ULONG),
        ('Timestamp:1', ULONG),
        ('PartitionId:1', ULONG),
        ('Reserved:29', ULONG),
    ]


    WHEA_ERROR_RECORD_VALID_PLATFORMID = 0x00000001
    WHEA_ERROR_RECORD_VALID_TIMESTAMP = 0x00000002
    WHEA_ERROR_RECORD_VALID_PARTITIONID = 0x00000004
    class _WHEA_ERROR_RECORD_HEADER_FLAGS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Recovered:1', ULONG),
        ('PreviousError:1', ULONG),
        ('Simulated:1', ULONG),
        ('Reserved:29', ULONG),
    ]


    _WHEA_ERROR_RECORD_HEADER_FLAGS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ERROR_RECORD_HEADER_FLAGS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ERROR_RECORD_HEADER_FLAGS.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_ERROR_RECORD_HEADER_FLAGS = _WHEA_ERROR_RECORD_HEADER_FLAGS
    PWHEA_ERROR_RECORD_HEADER_FLAGS = POINTER(_WHEA_ERROR_RECORD_HEADER_FLAGS)


    DUMMYSTRUCTNAME._fields_ = [
        ('Recovered:1', ULONG),
        ('PreviousError:1', ULONG),
        ('Simulated:1', ULONG),
        ('Reserved:29', ULONG),
    ]


    WHEA_ERROR_RECORD_FLAGS_RECOVERED = 0x00000001
    WHEA_ERROR_RECORD_FLAGS_PREVIOUSERROR = 0x00000002
    WHEA_ERROR_RECORD_FLAGS_SIMULATED = 0x00000004
    class _WHEA_ERROR_RECORD_HEADER(ctypes.Structure):
        pass
    _WHEA_ERROR_RECORD_HEADER._fields_ = [
        ('Signature', ULONG),
        ('Revision', WHEA_REVISION),
        ('SignatureEnd', ULONG),
        ('SectionCount', USHORT),
        ('Severity', WHEA_ERROR_SEVERITY),
        ('ValidBits', WHEA_ERROR_RECORD_HEADER_VALIDBITS),
        ('>=', _Field_range_(),
        ('(ctypes.sizeof(WHEA_ERROR_RECORD_HEADER) + (SectionCount * ctypes.sizeof(WHEA_ERROR_RECORD_SECTION_DESCRIPTOR)))) ULONG Length', _Field_range_(),
        ('Timestamp', WHEA_TIMESTAMP),
        ('PlatformId', GUID),
        ('PartitionId', GUID),
        ('CreatorId', GUID),
        ('NotifyType', GUID),
        ('RecordId', ULONGLONG),
        ('Flags', WHEA_ERROR_RECORD_HEADER_FLAGS),
        ('PersistenceInfo', WHEA_PERSISTENCE_INFO),
        ('Reserved', UCHAR * 12),
    ]


    WHEA_ERROR_RECORD_HEADER = _WHEA_ERROR_RECORD_HEADER
    PWHEA_ERROR_RECORD_HEADER = POINTER(_WHEA_ERROR_RECORD_HEADER)


    WHEA_ERROR_RECORD_SIGNATURE = 'REPC'
    WHEA_ERROR_RECORD_REVISION = 0x0210
    WHEA_ERROR_RECORD_SIGNATURE_END = 0xFFFFFFFF
    class _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Primary:1', ULONG),
        ('ContainmentWarning:1', ULONG),
        ('Reset:1', ULONG),
        ('ThresholdExceeded:1', ULONG),
        ('ResourceNotAvailable:1', ULONG),
        ('LatentError:1', ULONG),
        ('Propagated:1', ULONG),
        ('Reserved:25', ULONG),
    ]


    _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS = _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS
    PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS = POINTER(_WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS)


    DUMMYSTRUCTNAME._fields_ = [
        ('Primary:1', ULONG),
        ('ContainmentWarning:1', ULONG),
        ('Reset:1', ULONG),
        ('ThresholdExceeded:1', ULONG),
        ('ResourceNotAvailable:1', ULONG),
        ('LatentError:1', ULONG),
        ('Propagated:1', ULONG),
        ('Reserved:25', ULONG),
    ]


    WHEA_SECTION_DESCRIPTOR_FLAGS_PRIMARY = 0x00000001
    WHEA_SECTION_DESCRIPTOR_FLAGS_CONTAINMENTWRN = 0x00000002
    WHEA_SECTION_DESCRIPTOR_FLAGS_RESET = 0x00000004
    WHEA_SECTION_DESCRIPTOR_FLAGS_THRESHOLDEXCEEDED = 0x00000008
    WHEA_SECTION_DESCRIPTOR_FLAGS_RESOURCENA = 0x00000010
    WHEA_SECTION_DESCRIPTOR_FLAGS_LATENTERROR = 0x00000020
    WHEA_SECTION_DESCRIPTOR_FLAGS_PROPAGATED = 0x00000040
    class _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('FRUId:1', UCHAR),
        ('FRUText:1', UCHAR),
        ('Reserved:6', UCHAR),
    ]


    _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS.DUMMYSTRUCTNAME),
        ('AsUCHAR', UCHAR),
    ]


    WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS = _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS
    PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS = POINTER(_WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('FRUId:1', UCHAR),
        ('FRUText:1', UCHAR),
        ('Reserved:6', UCHAR),
    ]


    class _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR(ctypes.Structure):
        pass
    _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR._fields_ = [
        ('SectionOffset', ULONG),
        ('SectionLength', ULONG),
        ('Revision', WHEA_REVISION),
        ('ValidBits', WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS),
        ('Reserved', UCHAR),
        ('Flags', WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS),
        ('SectionType', GUID),
        ('FRUId', GUID),
        ('SectionSeverity', WHEA_ERROR_SEVERITY),
        ('FRUText', CCHAR * 20),
    ]


    WHEA_ERROR_RECORD_SECTION_DESCRIPTOR = _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR
    PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR = POINTER(_WHEA_ERROR_RECORD_SECTION_DESCRIPTOR)


    WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_REVISION = 0x0300

    if WHEA_DOWNLEVEL_TYPE_NAMES:
        WHEA_SECTION_DESCRIPTOR_REVISION = (
    WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_REVISION
)
    # END IF
    GENPROC_PROCTYPE_XPF = 0
    GENPROC_PROCTYPE_IPF = 1
    GENPROC_PROCTYPE_ARM = 2
    GENPROC_PROCISA_X86 = 0
    GENPROC_PROCISA_IPF = 1
    GENPROC_PROCISA_X64 = 2
    GENPROC_PROCISA_ARM32 = 4
    GENPROC_PROCISA_ARM64 = 8
    GENPROC_PROCERRTYPE_UNKNOWN = 0
    GENPROC_PROCERRTYPE_CACHE = 1
    GENPROC_PROCERRTYPE_TLB = 2
    GENPROC_PROCERRTYPE_BUS = 4
    GENPROC_PROCERRTYPE_MAE = 8
    GENPROC_OP_GENERIC = 0
    GENPROC_OP_DATAREAD = 1
    GENPROC_OP_DATAWRITE = 2
    GENPROC_OP_INSTRUCTIONEXE = 3
    GENPROC_FLAGS_RESTARTABLE = 0x01
    GENPROC_FLAGS_PRECISEIP = 0x02
    GENPROC_FLAGS_OVERFLOW = 0x04
    GENPROC_FLAGS_CORRECTED = 0x08
    class _WHEA_PROCESSOR_FAMILY_INFO(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Stepping:4', ULONG),
        ('Model:4', ULONG),
        ('Family:4', ULONG),
        ('ProcessorType:2', ULONG),
        ('Reserved1:2', ULONG),
        ('ExtendedModel:4', ULONG),
        ('ExtendedFamily:8', ULONG),
        ('Reserved2:4', ULONG),
        ('Reserved3', ULONG),
    ]


    _WHEA_PROCESSOR_FAMILY_INFO.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_PROCESSOR_FAMILY_INFO._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_PROCESSOR_FAMILY_INFO.DUMMYSTRUCTNAME),
        ('AsULONGLONG', ULONGLONG),
    ]


    WHEA_PROCESSOR_FAMILY_INFO = _WHEA_PROCESSOR_FAMILY_INFO
    PWHEA_PROCESSOR_FAMILY_INFO = POINTER(_WHEA_PROCESSOR_FAMILY_INFO)


    DUMMYSTRUCTNAME._fields_ = [
        ('Stepping:4', ULONG),
        ('Model:4', ULONG),
        ('Family:4', ULONG),
        ('ProcessorType:2', ULONG),
        ('Reserved1:2', ULONG),
        ('ExtendedModel:4', ULONG),
        ('ExtendedFamily:8', ULONG),
        ('Reserved2:4', ULONG),
        ('Reserved3', ULONG),
    ]


    class _WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ProcessorType:1', ULONGLONG),
        ('InstructionSet:1', ULONGLONG),
        ('ErrorType:1', ULONGLONG),
        ('Operation:1', ULONGLONG),
        ('Flags:1', ULONGLONG),
        ('Level:1', ULONGLONG),
        ('CPUVersion:1', ULONGLONG),
        ('CPUBrandString:1', ULONGLONG),
        ('ProcessorId:1', ULONGLONG),
        ('TargetAddress:1', ULONGLONG),
        ('RequesterId:1', ULONGLONG),
        ('ResponderId:1', ULONGLONG),
        ('InstructionPointer:1', ULONGLONG),
        ('Reserved:51', ULONGLONG),
    ]


    _WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME),
        ('ValidBits', ULONGLONG),
    ]


    WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS = _WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS
    PWHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS = POINTER(_WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('ProcessorType:1', ULONGLONG),
        ('InstructionSet:1', ULONGLONG),
        ('ErrorType:1', ULONGLONG),
        ('Operation:1', ULONGLONG),
        ('Flags:1', ULONGLONG),
        ('Level:1', ULONGLONG),
        ('CPUVersion:1', ULONGLONG),
        ('CPUBrandString:1', ULONGLONG),
        ('ProcessorId:1', ULONGLONG),
        ('TargetAddress:1', ULONGLONG),
        ('RequesterId:1', ULONGLONG),
        ('ResponderId:1', ULONGLONG),
        ('InstructionPointer:1', ULONGLONG),
        ('Reserved:51', ULONGLONG),
    ]


    class _WHEA_PROCESSOR_GENERIC_ERROR_SECTION(ctypes.Structure):
        pass
    _WHEA_PROCESSOR_GENERIC_ERROR_SECTION._fields_ = [
        ('ValidBits', WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS),
        ('ProcessorType', UCHAR),
        ('InstructionSet', UCHAR),
        ('ErrorType', UCHAR),
        ('Operation', UCHAR),
        ('Flags', UCHAR),
        ('Level', UCHAR),
        ('Reserved', USHORT),
        ('CPUVersion', ULONGLONG),
        ('CPUBrandString', UCHAR * 128),
        ('ProcessorId', ULONGLONG),
        ('TargetAddress', ULONGLONG),
        ('RequesterId', ULONGLONG),
        ('ResponderId', ULONGLONG),
        ('InstructionPointer', ULONGLONG),
    ]


    WHEA_PROCESSOR_GENERIC_ERROR_SECTION = _WHEA_PROCESSOR_GENERIC_ERROR_SECTION
    PWHEA_PROCESSOR_GENERIC_ERROR_SECTION = POINTER(_WHEA_PROCESSOR_GENERIC_ERROR_SECTION)



    if WHEA_DOWNLEVEL_TYPE_NAMES:
        pass
    # END IF
    XPF_CACHE_CHECK_TRANSACTIONTYPE_INSTRUCTION = 0
    XPF_CACHE_CHECK_TRANSACTIONTYPE_DATAACCESS = 1
    XPF_CACHE_CHECK_TRANSACTIONTYPE_GENERIC = 2
    XPF_CACHE_CHECK_OPERATION_GENERIC = 0
    XPF_CACHE_CHECK_OPERATION_GENREAD = 1
    XPF_CACHE_CHECK_OPERATION_GENWRITE = 2
    XPF_CACHE_CHECK_OPERATION_DATAREAD = 3
    XPF_CACHE_CHECK_OPERATION_DATAWRITE = 4
    XPF_CACHE_CHECK_OPERATION_INSTRUCTIONFETCH = 5
    XPF_CACHE_CHECK_OPERATION_PREFETCH = 6
    XPF_CACHE_CHECK_OPERATION_EVICTION = 7
    XPF_CACHE_CHECK_OPERATION_SNOOP = 8
    class _WHEA_XPF_CACHE_CHECK(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionTypeValid:1', ULONGLONG),
        ('OperationValid:1', ULONGLONG),
        ('LevelValid:1', ULONGLONG),
        ('ProcessorContextCorruptValid:1', ULONGLONG),
        ('UncorrectedValid:1', ULONGLONG),
        ('PreciseIPValid:1', ULONGLONG),
        ('RestartableIPValid:1', ULONGLONG),
        ('OverflowValid:1', ULONGLONG),
        ('ReservedValid:8', ULONGLONG),
        ('TransactionType:2', ULONGLONG),
        ('Operation:4', ULONGLONG),
        ('Level:3', ULONGLONG),
        ('ProcessorContextCorrupt:1', ULONGLONG),
        ('Uncorrected:1', ULONGLONG),
        ('PreciseIP:1', ULONGLONG),
        ('RestartableIP:1', ULONGLONG),
        ('Overflow:1', ULONGLONG),
        ('Reserved:34', ULONGLONG),
    ]


    _WHEA_XPF_CACHE_CHECK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_XPF_CACHE_CHECK._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_XPF_CACHE_CHECK.DUMMYSTRUCTNAME),
        ('XpfCacheCheck', ULONGLONG),
    ]


    WHEA_XPF_CACHE_CHECK = _WHEA_XPF_CACHE_CHECK
    PWHEA_XPF_CACHE_CHECK = POINTER(_WHEA_XPF_CACHE_CHECK)


    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionTypeValid:1', ULONGLONG),
        ('OperationValid:1', ULONGLONG),
        ('LevelValid:1', ULONGLONG),
        ('ProcessorContextCorruptValid:1', ULONGLONG),
        ('UncorrectedValid:1', ULONGLONG),
        ('PreciseIPValid:1', ULONGLONG),
        ('RestartableIPValid:1', ULONGLONG),
        ('OverflowValid:1', ULONGLONG),
        ('ReservedValid:8', ULONGLONG),
        ('TransactionType:2', ULONGLONG),
        ('Operation:4', ULONGLONG),
        ('Level:3', ULONGLONG),
        ('ProcessorContextCorrupt:1', ULONGLONG),
        ('Uncorrected:1', ULONGLONG),
        ('PreciseIP:1', ULONGLONG),
        ('RestartableIP:1', ULONGLONG),
        ('Overflow:1', ULONGLONG),
        ('Reserved:34', ULONGLONG),
    ]


    XPF_TLB_CHECK_TRANSACTIONTYPE_INSTRUCTION = 0
    XPF_TLB_CHECK_TRANSACTIONTYPE_DATAACCESS = 1
    XPF_TLB_CHECK_TRANSACTIONTYPE_GENERIC = 2
    XPF_TLB_CHECK_OPERATION_GENERIC = 0
    XPF_TLB_CHECK_OPERATION_GENREAD = 1
    XPF_TLB_CHECK_OPERATION_GENWRITE = 2
    XPF_TLB_CHECK_OPERATION_DATAREAD = 3
    XPF_TLB_CHECK_OPERATION_DATAWRITE = 4
    XPF_TLB_CHECK_OPERATION_INSTRUCTIONFETCH = 5
    XPF_TLB_CHECK_OPERATION_PREFETCH = 6
    class _WHEA_XPF_TLB_CHECK(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionTypeValid:1', ULONGLONG),
        ('OperationValid:1', ULONGLONG),
        ('LevelValid:1', ULONGLONG),
        ('ProcessorContextCorruptValid:1', ULONGLONG),
        ('UncorrectedValid:1', ULONGLONG),
        ('PreciseIPValid:1', ULONGLONG),
        ('RestartableIPValid:1', ULONGLONG),
        ('OverflowValid:1', ULONGLONG),
        ('ReservedValid:8', ULONGLONG),
        ('TransactionType:2', ULONGLONG),
        ('Operation:4', ULONGLONG),
        ('Level:3', ULONGLONG),
        ('ProcessorContextCorrupt:1', ULONGLONG),
        ('Uncorrected:1', ULONGLONG),
        ('PreciseIP:1', ULONGLONG),
        ('RestartableIP:1', ULONGLONG),
        ('Overflow:1', ULONGLONG),
        ('Reserved:34', ULONGLONG),
    ]


    _WHEA_XPF_TLB_CHECK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_XPF_TLB_CHECK._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_XPF_TLB_CHECK.DUMMYSTRUCTNAME),
        ('XpfTLBCheck', ULONGLONG),
    ]


    WHEA_XPF_TLB_CHECK = _WHEA_XPF_TLB_CHECK
    PWHEA_XPF_TLB_CHECK = POINTER(_WHEA_XPF_TLB_CHECK)


    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionTypeValid:1', ULONGLONG),
        ('OperationValid:1', ULONGLONG),
        ('LevelValid:1', ULONGLONG),
        ('ProcessorContextCorruptValid:1', ULONGLONG),
        ('UncorrectedValid:1', ULONGLONG),
        ('PreciseIPValid:1', ULONGLONG),
        ('RestartableIPValid:1', ULONGLONG),
        ('OverflowValid:1', ULONGLONG),
        ('ReservedValid:8', ULONGLONG),
        ('TransactionType:2', ULONGLONG),
        ('Operation:4', ULONGLONG),
        ('Level:3', ULONGLONG),
        ('ProcessorContextCorrupt:1', ULONGLONG),
        ('Uncorrected:1', ULONGLONG),
        ('PreciseIP:1', ULONGLONG),
        ('RestartableIP:1', ULONGLONG),
        ('Overflow:1', ULONGLONG),
        ('Reserved:34', ULONGLONG),
    ]


    XPF_BUS_CHECK_TRANSACTIONTYPE_INSTRUCTION = 0
    XPF_BUS_CHECK_TRANSACTIONTYPE_DATAACCESS = 1
    XPF_BUS_CHECK_TRANSACTIONTYPE_GENERIC = 2
    XPF_BUS_CHECK_OPERATION_GENERIC = 0
    XPF_BUS_CHECK_OPERATION_GENREAD = 1
    XPF_BUS_CHECK_OPERATION_GENWRITE = 2
    XPF_BUS_CHECK_OPERATION_DATAREAD = 3
    XPF_BUS_CHECK_OPERATION_DATAWRITE = 4
    XPF_BUS_CHECK_OPERATION_INSTRUCTIONFETCH = 5
    XPF_BUS_CHECK_OPERATION_PREFETCH = 6
    XPF_BUS_CHECK_PARTICIPATION_PROCORIGINATED = 0
    XPF_BUS_CHECK_PARTICIPATION_PROCRESPONDED = 1
    XPF_BUS_CHECK_PARTICIPATION_PROCOBSERVED = 2
    XPF_BUS_CHECK_PARTICIPATION_GENERIC = 3
    XPF_BUS_CHECK_ADDRESS_MEMORY = 0
    XPF_BUS_CHECK_ADDRESS_RESERVED = 1
    XPF_BUS_CHECK_ADDRESS_IO = 2
    XPF_BUS_CHECK_ADDRESS_OTHER = 3
    class _WHEA_XPF_BUS_CHECK(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionTypeValid:1', ULONGLONG),
        ('OperationValid:1', ULONGLONG),
        ('LevelValid:1', ULONGLONG),
        ('ProcessorContextCorruptValid:1', ULONGLONG),
        ('UncorrectedValid:1', ULONGLONG),
        ('PreciseIPValid:1', ULONGLONG),
        ('RestartableIPValid:1', ULONGLONG),
        ('OverflowValid:1', ULONGLONG),
        ('ParticipationValid:1', ULONGLONG),
        ('TimeoutValid:1', ULONGLONG),
        ('AddressSpaceValid:1', ULONGLONG),
        ('ReservedValid:5', ULONGLONG),
        ('TransactionType:2', ULONGLONG),
        ('Operation:4', ULONGLONG),
        ('Level:3', ULONGLONG),
        ('ProcessorContextCorrupt:1', ULONGLONG),
        ('Uncorrected:1', ULONGLONG),
        ('PreciseIP:1', ULONGLONG),
        ('RestartableIP:1', ULONGLONG),
        ('Overflow:1', ULONGLONG),
        ('Participation:2', ULONGLONG),
        ('Timeout:1', ULONGLONG),
        ('AddressSpace:2', ULONGLONG),
        ('Reserved:29', ULONGLONG),
    ]


    _WHEA_XPF_BUS_CHECK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_XPF_BUS_CHECK._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_XPF_BUS_CHECK.DUMMYSTRUCTNAME),
        ('XpfBusCheck', ULONGLONG),
    ]


    WHEA_XPF_BUS_CHECK = _WHEA_XPF_BUS_CHECK
    PWHEA_XPF_BUS_CHECK = POINTER(_WHEA_XPF_BUS_CHECK)


    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionTypeValid:1', ULONGLONG),
        ('OperationValid:1', ULONGLONG),
        ('LevelValid:1', ULONGLONG),
        ('ProcessorContextCorruptValid:1', ULONGLONG),
        ('UncorrectedValid:1', ULONGLONG),
        ('PreciseIPValid:1', ULONGLONG),
        ('RestartableIPValid:1', ULONGLONG),
        ('OverflowValid:1', ULONGLONG),
        ('ParticipationValid:1', ULONGLONG),
        ('TimeoutValid:1', ULONGLONG),
        ('AddressSpaceValid:1', ULONGLONG),
        ('ReservedValid:5', ULONGLONG),
        ('TransactionType:2', ULONGLONG),
        ('Operation:4', ULONGLONG),
        ('Level:3', ULONGLONG),
        ('ProcessorContextCorrupt:1', ULONGLONG),
        ('Uncorrected:1', ULONGLONG),
        ('PreciseIP:1', ULONGLONG),
        ('RestartableIP:1', ULONGLONG),
        ('Overflow:1', ULONGLONG),
        ('Participation:2', ULONGLONG),
        ('Timeout:1', ULONGLONG),
        ('AddressSpace:2', ULONGLONG),
        ('Reserved:29', ULONGLONG),
    ]


    XPF_MS_CHECK_ERRORTYPE_NOERROR = 0
    XPF_MS_CHECK_ERRORTYPE_UNCLASSIFIED = 1
    XPF_MS_CHECK_ERRORTYPE_MCROMPARITY = 2
    XPF_MS_CHECK_ERRORTYPE_EXTERNAL = 3
    XPF_MS_CHECK_ERRORTYPE_FRC = 4
    XPF_MS_CHECK_ERRORTYPE_INTERNALUNCLASSIFIED = 5
    class _WHEA_XPF_MS_CHECK(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ErrorTypeValid:1', ULONGLONG),
        ('ProcessorContextCorruptValid:1', ULONGLONG),
        ('UncorrectedValid:1', ULONGLONG),
        ('PreciseIPValid:1', ULONGLONG),
        ('RestartableIPValid:1', ULONGLONG),
        ('OverflowValid:1', ULONGLONG),
        ('ReservedValue:10', ULONGLONG),
        ('ErrorType:3', ULONGLONG),
        ('ProcessorContextCorrupt:1', ULONGLONG),
        ('Uncorrected:1', ULONGLONG),
        ('PreciseIP:1', ULONGLONG),
        ('RestartableIP:1', ULONGLONG),
        ('Overflow:1', ULONGLONG),
        ('Reserved:40', ULONGLONG),
    ]


    _WHEA_XPF_MS_CHECK.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_XPF_MS_CHECK._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_XPF_MS_CHECK.DUMMYSTRUCTNAME),
        ('XpfMsCheck', ULONGLONG),
    ]


    WHEA_XPF_MS_CHECK = _WHEA_XPF_MS_CHECK
    PWHEA_XPF_MS_CHECK = POINTER(_WHEA_XPF_MS_CHECK)


    DUMMYSTRUCTNAME._fields_ = [
        ('ErrorTypeValid:1', ULONGLONG),
        ('ProcessorContextCorruptValid:1', ULONGLONG),
        ('UncorrectedValid:1', ULONGLONG),
        ('PreciseIPValid:1', ULONGLONG),
        ('RestartableIPValid:1', ULONGLONG),
        ('OverflowValid:1', ULONGLONG),
        ('ReservedValue:10', ULONGLONG),
        ('ErrorType:3', ULONGLONG),
        ('ProcessorContextCorrupt:1', ULONGLONG),
        ('Uncorrected:1', ULONGLONG),
        ('PreciseIP:1', ULONGLONG),
        ('RestartableIP:1', ULONGLONG),
        ('Overflow:1', ULONGLONG),
        ('Reserved:40', ULONGLONG),
    ]


    class _WHEA_XPF_PROCINFO_VALIDBITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('CheckInfo:1', ULONGLONG),
        ('TargetId:1', ULONGLONG),
        ('RequesterId:1', ULONGLONG),
        ('ResponderId:1', ULONGLONG),
        ('InstructionPointer:1', ULONGLONG),
        ('Reserved:59', ULONGLONG),
    ]


    _WHEA_XPF_PROCINFO_VALIDBITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_XPF_PROCINFO_VALIDBITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_XPF_PROCINFO_VALIDBITS.DUMMYSTRUCTNAME),
        ('ValidBits', ULONGLONG),
    ]


    WHEA_XPF_PROCINFO_VALIDBITS = _WHEA_XPF_PROCINFO_VALIDBITS
    PWHEA_XPF_PROCINFO_VALIDBITS = POINTER(_WHEA_XPF_PROCINFO_VALIDBITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('CheckInfo:1', ULONGLONG),
        ('TargetId:1', ULONGLONG),
        ('RequesterId:1', ULONGLONG),
        ('ResponderId:1', ULONGLONG),
        ('InstructionPointer:1', ULONGLONG),
        ('Reserved:59', ULONGLONG),
    ]


    class _WHEA_XPF_PROCINFO(ctypes.Structure):
        pass
    CheckInfo._fields_ = [
        ('CacheCheck', WHEA_XPF_CACHE_CHECK),
        ('TlbCheck', WHEA_XPF_TLB_CHECK),
        ('BusCheck', WHEA_XPF_BUS_CHECK),
        ('MsCheck', WHEA_XPF_MS_CHECK),
        ('AsULONGLONG', ULONGLONG),
    ]


    _WHEA_XPF_PROCINFO.CheckInfo = CheckInfo
    _WHEA_XPF_PROCINFO._fields_ = [
        ('CheckInfoId', GUID),
        ('ValidBits', WHEA_XPF_PROCINFO_VALIDBITS),
        ('CheckInfo', _WHEA_XPF_PROCINFO.CheckInfo),
        ('TargetId', ULONGLONG),
        ('RequesterId', ULONGLONG),
        ('ResponderId', ULONGLONG),
        ('InstructionPointer', ULONGLONG),
    ]


    WHEA_XPF_PROCINFO = _WHEA_XPF_PROCINFO
    PWHEA_XPF_PROCINFO = POINTER(_WHEA_XPF_PROCINFO)


    CheckInfo._fields_ = [
        ('CacheCheck', WHEA_XPF_CACHE_CHECK),
        ('TlbCheck', WHEA_XPF_TLB_CHECK),
        ('BusCheck', WHEA_XPF_BUS_CHECK),
        ('MsCheck', WHEA_XPF_MS_CHECK),
        ('AsULONGLONG', ULONGLONG),
    ]


    class _WHEA_X86_REGISTER_STATE(ctypes.Structure):
        pass
    _WHEA_X86_REGISTER_STATE._fields_ = [
        ('Eax', ULONG),
        ('Ebx', ULONG),
        ('Ecx', ULONG),
        ('Edx', ULONG),
        ('Esi', ULONG),
        ('Edi', ULONG),
        ('Ebp', ULONG),
        ('Esp', ULONG),
        ('Cs', USHORT),
        ('Ds', USHORT),
        ('Ss', USHORT),
        ('Es', USHORT),
        ('Fs', USHORT),
        ('Gs', USHORT),
        ('Eflags', ULONG),
        ('Eip', ULONG),
        ('Cr0', ULONG),
        ('Cr1', ULONG),
        ('Cr2', ULONG),
        ('Cr3', ULONG),
        ('Cr4', ULONG),
        ('Gdtr', ULONGLONG),
        ('Idtr', ULONGLONG),
        ('Ldtr', USHORT),
        ('Tr', USHORT),
    ]


    WHEA_X86_REGISTER_STATE = _WHEA_X86_REGISTER_STATE
    PWHEA_X86_REGISTER_STATE = POINTER(_WHEA_X86_REGISTER_STATE)


    class _WHEA128A(DECLSPEC_ALIGN(16)):
        pass
    _WHEA128A._fields_ = [
        ('Low', ULONGLONG),
        ('High', LONGLONG),
    ]


    WHEA128A = _WHEA128A
    PWHEA128A = POINTER(_WHEA128A)



        if (_MSC_VER >= 1200):
            pass
        # END IF
    if defined(_MSC_VER):
        pass
    # END IF
    class _WHEA_X64_REGISTER_STATE(ctypes.Structure):
        pass
    _WHEA_X64_REGISTER_STATE._fields_ = [
        ('Rax', ULONGLONG),
        ('Rbx', ULONGLONG),
        ('Rcx', ULONGLONG),
        ('Rdx', ULONGLONG),
        ('Rsi', ULONGLONG),
        ('Rdi', ULONGLONG),
        ('Rbp', ULONGLONG),
        ('Rsp', ULONGLONG),
        ('R8', ULONGLONG),
        ('R9', ULONGLONG),
        ('R10', ULONGLONG),
        ('R11', ULONGLONG),
        ('R12', ULONGLONG),
        ('R13', ULONGLONG),
        ('R14', ULONGLONG),
        ('R15', ULONGLONG),
        ('Cs', USHORT),
        ('Ds', USHORT),
        ('Ss', USHORT),
        ('Es', USHORT),
        ('Fs', USHORT),
        ('Gs', USHORT),
        ('Reserved', ULONG),
        ('Rflags', ULONGLONG),
        ('Eip', ULONGLONG),
        ('Cr0', ULONGLONG),
        ('Cr1', ULONGLONG),
        ('Cr2', ULONGLONG),
        ('Cr3', ULONGLONG),
        ('Cr4', ULONGLONG),
        ('Cr8', ULONGLONG),
        ('Gdtr', WHEA128A),
        ('Idtr', WHEA128A),
        ('Ldtr', USHORT),
        ('Tr', USHORT),
    ]


    WHEA_X64_REGISTER_STATE = _WHEA_X64_REGISTER_STATE
    PWHEA_X64_REGISTER_STATE = POINTER(_WHEA_X64_REGISTER_STATE)


        if (_MSC_VER >= 1200):
            pass
        # END IF
    if defined(_MSC_VER):
        pass
    # END IF
    XPF_CONTEXT_INFO_UNCLASSIFIEDDATA = 0
    XPF_CONTEXT_INFO_MSRREGISTERS = 1
    XPF_CONTEXT_INFO_32BITCONTEXT = 2
    XPF_CONTEXT_INFO_64BITCONTEXT = 3
    XPF_CONTEXT_INFO_FXSAVE = 4
    XPF_CONTEXT_INFO_32BITDEBUGREGS = 5
    XPF_CONTEXT_INFO_64BITDEBUGREGS = 6
    XPF_CONTEXT_INFO_MMREGISTERS = 7
    class _WHEA_XPF_CONTEXT_INFO(ctypes.Structure):
        pass
    _WHEA_XPF_CONTEXT_INFO._fields_ = [
        ('RegisterContextType', USHORT),
        ('RegisterDataSize', USHORT),
        ('MSRAddress', ULONG),
        ('MmRegisterAddress', ULONGLONG),
    ]


    WHEA_XPF_CONTEXT_INFO = _WHEA_XPF_CONTEXT_INFO
    PWHEA_XPF_CONTEXT_INFO = POINTER(_WHEA_XPF_CONTEXT_INFO)


    class _WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('LocalAPICId:1', ULONGLONG),
        ('CpuId:1', ULONGLONG),
        ('ProcInfoCount:6', ULONGLONG),
        ('ContextInfoCount:6', ULONGLONG),
        ('Reserved:50', ULONGLONG),
    ]


    _WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME),
        ('ValidBits', ULONGLONG),
    ]


    WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS = _WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS
    PWHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS = POINTER(_WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('LocalAPICId:1', ULONGLONG),
        ('CpuId:1', ULONGLONG),
        ('ProcInfoCount:6', ULONGLONG),
        ('ContextInfoCount:6', ULONGLONG),
        ('Reserved:50', ULONGLONG),
    ]


    class _WHEA_XPF_PROCESSOR_ERROR_SECTION(ctypes.Structure):
        pass
    _WHEA_XPF_PROCESSOR_ERROR_SECTION._fields_ = [
        ('ValidBits', WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS),
        ('LocalAPICId', ULONGLONG),
        ('CpuId', UCHAR * 48),
        ('VariableInfo', UCHAR * ANYSIZE_ARRAY), # WHEA_XPF_CONTEXT_INFO ContextInfo[ANYSIZE_ARRAY];
    ]


    WHEA_XPF_PROCESSOR_ERROR_SECTION = _WHEA_XPF_PROCESSOR_ERROR_SECTION
    PWHEA_XPF_PROCESSOR_ERROR_SECTION = POINTER(_WHEA_XPF_PROCESSOR_ERROR_SECTION)



    if WHEA_DOWNLEVEL_TYPE_NAMES:
        PWHEA_XPF_PROCESSOR_ERROR_VALIDBITS = POINTER(WHEA_XPF_PROCESSOR_ERROR_SECTION_VALIDBITS WHEA_XPF_PROCESSOR_ERROR_VALIDBITS,)
        PWHEA_XPF_PROCESSOR_ERROR = POINTER(WHEA_XPF_PROCESSOR_ERROR_SECTION WHEA_XPF_PROCESSOR_ERROR,)
    # END IF
    class _WHEA_MEMORY_ERROR_SECTION_VALIDBITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ErrorStatus:1', ULONGLONG),
        ('PhysicalAddress:1', ULONGLONG),
        ('PhysicalAddressMask:1', ULONGLONG),
        ('Node:1', ULONGLONG),
        ('Card:1', ULONGLONG),
        ('Module:1', ULONGLONG),
        ('Bank:1', ULONGLONG),
        ('Device:1', ULONGLONG),
        ('Row:1', ULONGLONG),
        ('Column:1', ULONGLONG),
        ('BitPosition:1', ULONGLONG),
        ('RequesterId:1', ULONGLONG),
        ('ResponderId:1', ULONGLONG),
        ('TargetId:1', ULONGLONG),
        ('ErrorType:1', ULONGLONG),
        ('RankNumber:1', ULONGLONG),
        ('CardHandle:1', ULONGLONG),
        ('ModuleHandle:1', ULONGLONG),
        ('ExtendedRow:1', ULONGLONG),
        ('BankGroup:1', ULONGLONG),
        ('BankAddress:1', ULONGLONG),
        ('ChipIdentification:1', ULONGLONG),
        ('Reserved:42', ULONGLONG),
    ]


    _WHEA_MEMORY_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_MEMORY_ERROR_SECTION_VALIDBITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_MEMORY_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME),
        ('ValidBits', ULONGLONG),
    ]


    WHEA_MEMORY_ERROR_SECTION_VALIDBITS = _WHEA_MEMORY_ERROR_SECTION_VALIDBITS
    PWHEA_MEMORY_ERROR_SECTION_VALIDBITS = POINTER(_WHEA_MEMORY_ERROR_SECTION_VALIDBITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('ErrorStatus:1', ULONGLONG),
        ('PhysicalAddress:1', ULONGLONG),
        ('PhysicalAddressMask:1', ULONGLONG),
        ('Node:1', ULONGLONG),
        ('Card:1', ULONGLONG),
        ('Module:1', ULONGLONG),
        ('Bank:1', ULONGLONG),
        ('Device:1', ULONGLONG),
        ('Row:1', ULONGLONG),
        ('Column:1', ULONGLONG),
        ('BitPosition:1', ULONGLONG),
        ('RequesterId:1', ULONGLONG),
        ('ResponderId:1', ULONGLONG),
        ('TargetId:1', ULONGLONG),
        ('ErrorType:1', ULONGLONG),
        ('RankNumber:1', ULONGLONG),
        ('CardHandle:1', ULONGLONG),
        ('ModuleHandle:1', ULONGLONG),
        ('ExtendedRow:1', ULONGLONG),
        ('BankGroup:1', ULONGLONG),
        ('BankAddress:1', ULONGLONG),
        ('ChipIdentification:1', ULONGLONG),
        ('Reserved:42', ULONGLONG),
    ]


    WHEA_MEMERRTYPE_UNKNOWN = 0x00
    WHEA_MEMERRTYPE_NOERROR = 0x01
    WHEA_MEMERRTYPE_SINGLEBITECC = 0x02
    WHEA_MEMERRTYPE_MULTIBITECC = 0x03
    WHEA_MEMERRTYPE_SINGLESYMCHIPKILL = 0x04
    WHEA_MEMERRTYPE_MULTISYMCHIPKILL = 0x05
    WHEA_MEMERRTYPE_MASTERABORT = 0x06
    WHEA_MEMERRTYPE_TARGETABORT = 0x07
    WHEA_MEMERRTYPE_PARITYERROR = 0x08
    WHEA_MEMERRTYPE_WATCHDOGTIMEOUT = 0x09
    WHEA_MEMERRTYPE_INVALIDADDRESS = 0x0A
    WHEA_MEMERRTYPE_MIRRORBROKEN = 0x0B
    WHEA_MEMERRTYPE_MEMORYSPARING = 0x0C
    class _WHEA_MEMORY_ERROR_SECTION(ctypes.Structure):
        pass
    _WHEA_MEMORY_ERROR_SECTION._fields_ = [
        ('ValidBits', WHEA_MEMORY_ERROR_SECTION_VALIDBITS),
        ('ErrorStatus', WHEA_ERROR_STATUS),
        ('PhysicalAddress', ULONGLONG),
        ('PhysicalAddressMask', ULONGLONG),
        ('Node', USHORT),
        ('Card', USHORT),
        ('Module', USHORT),
        ('Bank', USHORT),
        ('Device', USHORT),
        ('Row', USHORT),
        ('Column', USHORT),
        ('BitPosition', USHORT),
        ('RequesterId', ULONGLONG),
        ('ResponderId', ULONGLONG),
        ('TargetId', ULONGLONG),
        ('ErrorType', UCHAR),
        ('Extended', UCHAR),
        ('RankNumber', USHORT),
        ('CardHandle', USHORT),
        ('ModuleHandle', USHORT),
    ]


    WHEA_MEMORY_ERROR_SECTION = _WHEA_MEMORY_ERROR_SECTION
    PWHEA_MEMORY_ERROR_SECTION = POINTER(_WHEA_MEMORY_ERROR_SECTION)



    if WHEA_DOWNLEVEL_TYPE_NAMES:
        pass
    # END IF
    class _WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('PortType:1', ULONGLONG),
        ('Version:1', ULONGLONG),
        ('CommandStatus:1', ULONGLONG),
        ('DeviceId:1', ULONGLONG),
        ('DeviceSerialNumber:1', ULONGLONG),
        ('BridgeControlStatus:1', ULONGLONG),
        ('ExpressCapability:1', ULONGLONG),
        ('AerInfo:1', ULONGLONG),
        ('Reserved:56', ULONGLONG),
    ]


    _WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME),
        ('ValidBits', ULONGLONG),
    ]


    WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS = _WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS
    PWHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS = POINTER(_WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('PortType:1', ULONGLONG),
        ('Version:1', ULONGLONG),
        ('CommandStatus:1', ULONGLONG),
        ('DeviceId:1', ULONGLONG),
        ('DeviceSerialNumber:1', ULONGLONG),
        ('BridgeControlStatus:1', ULONGLONG),
        ('ExpressCapability:1', ULONGLONG),
        ('AerInfo:1', ULONGLONG),
        ('Reserved:56', ULONGLONG),
    ]


    class _WHEA_PCIEXPRESS_DEVICE_ID(ctypes.Structure):
        pass
    _WHEA_PCIEXPRESS_DEVICE_ID._fields_ = [
        ('VendorID', USHORT),
        ('DeviceID', USHORT),
        ('ClassCode:24', ULONG),
        ('FunctionNumber:8', ULONG),
        ('DeviceNumber:8', ULONG),
        ('Segment:16', ULONG),
        ('PrimaryBusNumber:8', ULONG),
        ('SecondaryBusNumber:8', ULONG),
        ('Reserved1:3', ULONG),
        ('SlotNumber:13', ULONG),
        ('Reserved2:8', ULONG),
    ]


    WHEA_PCIEXPRESS_DEVICE_ID = _WHEA_PCIEXPRESS_DEVICE_ID
    PWHEA_PCIEXPRESS_DEVICE_ID = POINTER(_WHEA_PCIEXPRESS_DEVICE_ID)


    class _WHEA_PCIEXPRESS_VERSION(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('MinorVersion', UCHAR),
        ('MajorVersion', UCHAR),
        ('Reserved', USHORT),
    ]


    _WHEA_PCIEXPRESS_VERSION.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_PCIEXPRESS_VERSION._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_PCIEXPRESS_VERSION.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_PCIEXPRESS_VERSION = _WHEA_PCIEXPRESS_VERSION
    PWHEA_PCIEXPRESS_VERSION = POINTER(_WHEA_PCIEXPRESS_VERSION)


    DUMMYSTRUCTNAME._fields_ = [
        ('MinorVersion', UCHAR),
        ('MajorVersion', UCHAR),
        ('Reserved', USHORT),
    ]


    class _WHEA_PCIEXPRESS_COMMAND_STATUS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Command', USHORT),
        ('Status', USHORT),
    ]


    _WHEA_PCIEXPRESS_COMMAND_STATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_PCIEXPRESS_COMMAND_STATUS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_PCIEXPRESS_COMMAND_STATUS.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_PCIEXPRESS_COMMAND_STATUS = _WHEA_PCIEXPRESS_COMMAND_STATUS
    PWHEA_PCIEXPRESS_COMMAND_STATUS = POINTER(_WHEA_PCIEXPRESS_COMMAND_STATUS)


    DUMMYSTRUCTNAME._fields_ = [
        ('Command', USHORT),
        ('Status', USHORT),
    ]


    class _WHEA_PCIEXPRESS_BRIDGE_CONTROL_STATUS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('BridgeSecondaryStatus', USHORT),
        ('BridgeControl', USHORT),
    ]


    _WHEA_PCIEXPRESS_BRIDGE_CONTROL_STATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_PCIEXPRESS_BRIDGE_CONTROL_STATUS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_PCIEXPRESS_BRIDGE_CONTROL_STATUS.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_PCIEXPRESS_BRIDGE_CONTROL_STATUS = _WHEA_PCIEXPRESS_BRIDGE_CONTROL_STATUS
    PWHEA_PCIEXPRESS_BRIDGE_CONTROL_STATUS = POINTER(_WHEA_PCIEXPRESS_BRIDGE_CONTROL_STATUS)


    DUMMYSTRUCTNAME._fields_ = [
        ('BridgeSecondaryStatus', USHORT),
        ('BridgeControl', USHORT),
    ]


    class _WHEA_PCIEXPRESS_DEVICE_TYPE(ENUM):
        WheaPciExpressEndpoint = 0
        WheaPciExpressLegacyEndpoint = 1
        WheaPciExpressRootPort = 4
        WheaPciExpressUpstreamSwitchPort = 5
        WheaPciExpressDownstreamSwitchPort = 6
        WheaPciExpressToPciXBridge = 7
        WheaPciXToExpressBridge = 8
        WheaPciExpressRootComplexIntegratedEndpoint = 9
        WheaPciExpressRootComplexEventCollector = 10


    WHEA_PCIEXPRESS_DEVICE_TYPE = _WHEA_PCIEXPRESS_DEVICE_TYPE
    class _WHEA_PCIEXPRESS_ERROR_SECTION(ctypes.Structure):
        pass
    _WHEA_PCIEXPRESS_ERROR_SECTION._fields_ = [
        ('ValidBits', WHEA_PCIEXPRESS_ERROR_SECTION_VALIDBITS),
        ('PortType', WHEA_PCIEXPRESS_DEVICE_TYPE),
        ('Version', WHEA_PCIEXPRESS_VERSION),
        ('CommandStatus', WHEA_PCIEXPRESS_COMMAND_STATUS),
        ('Reserved', ULONG),
        ('DeviceId', WHEA_PCIEXPRESS_DEVICE_ID),
        ('DeviceSerialNumber', ULONGLONG),
        ('BridgeControlStatus', WHEA_PCIEXPRESS_BRIDGE_CONTROL_STATUS),
        ('ExpressCapability', UCHAR * 60),
        ('AerInfo', UCHAR * 96),
    ]


    WHEA_PCIEXPRESS_ERROR_SECTION = _WHEA_PCIEXPRESS_ERROR_SECTION
    PWHEA_PCIEXPRESS_ERROR_SECTION = POINTER(_WHEA_PCIEXPRESS_ERROR_SECTION)


    if WHEA_DOWNLEVEL_TYPE_NAMES:
        pass
    # END IF
    PCIXBUS_ERRTYPE_UNKNOWN = 0x0000
    PCIXBUS_ERRTYPE_DATAPARITY = 0x0001
    PCIXBUS_ERRTYPE_SYSTEM = 0x0002
    PCIXBUS_ERRTYPE_MASTERABORT = 0x0003
    PCIXBUS_ERRTYPE_BUSTIMEOUT = 0x0004
    PCIXBUS_ERRTYPE_MASTERDATAPARITY = 0x0005
    PCIXBUS_ERRTYPE_ADDRESSPARITY = 0x0006
    PCIXBUS_ERRTYPE_COMMANDPARITY = 0x0007
    class _WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ErrorStatus:1', ULONGLONG),
        ('ErrorType:1', ULONGLONG),
        ('BusId:1', ULONGLONG),
        ('BusAddress:1', ULONGLONG),
        ('BusData:1', ULONGLONG),
        ('BusCommand:1', ULONGLONG),
        ('RequesterId:1', ULONGLONG),
        ('CompleterId:1', ULONGLONG),
        ('TargetId:1', ULONGLONG),
        ('Reserved:55', ULONGLONG),
    ]


    _WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME),
        ('ValidBits', ULONGLONG),
    ]


    WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS = _WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS
    PWHEA_PCIXBUS_ERROR_SECTION_VALIDBITS = POINTER(_WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('ErrorStatus:1', ULONGLONG),
        ('ErrorType:1', ULONGLONG),
        ('BusId:1', ULONGLONG),
        ('BusAddress:1', ULONGLONG),
        ('BusData:1', ULONGLONG),
        ('BusCommand:1', ULONGLONG),
        ('RequesterId:1', ULONGLONG),
        ('CompleterId:1', ULONGLONG),
        ('TargetId:1', ULONGLONG),
        ('Reserved:55', ULONGLONG),
    ]


    class _WHEA_PCIXBUS_ID(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('BusNumber', UCHAR),
        ('BusSegment', UCHAR),
    ]


    _WHEA_PCIXBUS_ID.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_PCIXBUS_ID._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_PCIXBUS_ID.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    WHEA_PCIXBUS_ID = _WHEA_PCIXBUS_ID
    PWHEA_PCIXBUS_ID = POINTER(_WHEA_PCIXBUS_ID)


    DUMMYSTRUCTNAME._fields_ = [
        ('BusNumber', UCHAR),
        ('BusSegment', UCHAR),
    ]


    class _WHEA_PCIXBUS_COMMAND(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('Command:56', ULONGLONG),
        ('PCIXCommand:1', ULONGLONG),
        ('Reserved:7', ULONGLONG),
    ]


    _WHEA_PCIXBUS_COMMAND.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_PCIXBUS_COMMAND._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_PCIXBUS_COMMAND.DUMMYSTRUCTNAME),
        ('AsULONGLONG', ULONGLONG),
    ]


    WHEA_PCIXBUS_COMMAND = _WHEA_PCIXBUS_COMMAND
    PWHEA_PCIXBUS_COMMAND = POINTER(_WHEA_PCIXBUS_COMMAND)


    DUMMYSTRUCTNAME._fields_ = [
        ('Command:56', ULONGLONG),
        ('PCIXCommand:1', ULONGLONG),
        ('Reserved:7', ULONGLONG),
    ]


    class _WHEA_PCIXBUS_ERROR_SECTION(ctypes.Structure):
        pass
    _WHEA_PCIXBUS_ERROR_SECTION._fields_ = [
        ('ValidBits', WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS),
        ('ErrorStatus', WHEA_ERROR_STATUS),
        ('ErrorType', USHORT),
        ('BusId', WHEA_PCIXBUS_ID),
        ('Reserved', ULONG),
        ('BusAddress', ULONGLONG),
        ('BusData', ULONGLONG),
        ('BusCommand', WHEA_PCIXBUS_COMMAND),
        ('RequesterId', ULONGLONG),
        ('CompleterId', ULONGLONG),
        ('TargetId', ULONGLONG),
    ]


    WHEA_PCIXBUS_ERROR_SECTION = _WHEA_PCIXBUS_ERROR_SECTION
    PWHEA_PCIXBUS_ERROR_SECTION = POINTER(_WHEA_PCIXBUS_ERROR_SECTION)



    if WHEA_DOWNLEVEL_TYPE_NAMES:
        pass
    # END IF
    class _WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ErrorStatus:1', ULONGLONG),
        ('IdInfo:1', ULONGLONG),
        ('MemoryNumber:1', ULONGLONG),
        ('IoNumber:1', ULONGLONG),
        ('RegisterDataPairs:1', ULONGLONG),
        ('Reserved:59', ULONGLONG),
    ]


    _WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS.DUMMYSTRUCTNAME),
        ('ValidBits', ULONGLONG),
    ]


    WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS = _WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS
    PWHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS = POINTER(_WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('ErrorStatus:1', ULONGLONG),
        ('IdInfo:1', ULONGLONG),
        ('MemoryNumber:1', ULONGLONG),
        ('IoNumber:1', ULONGLONG),
        ('RegisterDataPairs:1', ULONGLONG),
        ('Reserved:59', ULONGLONG),
    ]


    class _WHEA_PCIXDEVICE_ID(ctypes.Structure):
        pass
    _WHEA_PCIXDEVICE_ID._fields_ = [
        ('VendorId', USHORT),
        ('DeviceId', USHORT),
        ('ClassCode:24', ULONG),
        ('FunctionNumber:8', ULONG),
        ('DeviceNumber:8', ULONG),
        ('BusNumber:8', ULONG),
        ('SegmentNumber:8', ULONG),
        ('Reserved1:8', ULONG),
        ('Reserved2', ULONG),
    ]


    WHEA_PCIXDEVICE_ID = _WHEA_PCIXDEVICE_ID
    PWHEA_PCIXDEVICE_ID = POINTER(_WHEA_PCIXDEVICE_ID)


    class WHEA_PCIXDEVICE_REGISTER_PAIR(ctypes.Structure):
        pass
    WHEA_PCIXDEVICE_REGISTER_PAIR._fields_ = [
        ('Register', ULONGLONG),
        ('Data', ULONGLONG),
    ]


    PWHEA_PCIXDEVICE_REGISTER_PAIR = POINTER(WHEA_PCIXDEVICE_REGISTER_PAIR)


    class _WHEA_PCIXDEVICE_ERROR_SECTION(ctypes.Structure):
        pass
    _WHEA_PCIXDEVICE_ERROR_SECTION._fields_ = [
        ('ValidBits', WHEA_PCIXDEVICE_ERROR_SECTION_VALIDBITS),
        ('ErrorStatus', WHEA_ERROR_STATUS),
        ('IdInfo', WHEA_PCIXDEVICE_ID),
        ('MemoryNumber', ULONG),
        ('IoNumber', ULONG),
        ('RegisterDataPairs', WHEA_PCIXDEVICE_REGISTER_PAIR * ANYSIZE_ARRAY),
    ]


    WHEA_PCIXDEVICE_ERROR_SECTION = _WHEA_PCIXDEVICE_ERROR_SECTION
    PWHEA_PCIXDEVICE_ERROR_SECTION = POINTER(_WHEA_PCIXDEVICE_ERROR_SECTION)


    if WHEA_DOWNLEVEL_TYPE_NAMES:
        pass
    # END IF
    WHEA_FIRMWARE_RECORD_TYPE_IPFSAL = 0
    class _WHEA_FIRMWARE_ERROR_RECORD_REFERENCE(ctypes.Structure):
        pass
    _WHEA_FIRMWARE_ERROR_RECORD_REFERENCE._fields_ = [
        ('Type', UCHAR),
        ('Reserved', UCHAR * 7),
        ('FirmwareRecordId', ULONGLONG),
    ]


    WHEA_FIRMWARE_ERROR_RECORD_REFERENCE = _WHEA_FIRMWARE_ERROR_RECORD_REFERENCE
    PWHEA_FIRMWARE_ERROR_RECORD_REFERENCE = POINTER(_WHEA_FIRMWARE_ERROR_RECORD_REFERENCE)



    if WHEA_DOWNLEVEL_TYPE_NAMES:
        pass
    # END IF
    class _MCG_STATUS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('RestartIpValid:1', ULONG),
        ('ErrorIpValid:1', ULONG),
        ('MachineCheckInProgress:1', ULONG),
        ('Reserved1:29', ULONG),
        ('Reserved2', ULONG),
    ]


    _MCG_STATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _MCG_STATUS._fields_ = [
        ('DUMMYSTRUCTNAME', _MCG_STATUS.DUMMYSTRUCTNAME),
        ('QuadPart', ULONGLONG),
    ]


    MCG_STATUS = _MCG_STATUS
    PMCG_STATUS = POINTER(_MCG_STATUS)


    DUMMYSTRUCTNAME._fields_ = [
        ('RestartIpValid:1', ULONG),
        ('ErrorIpValid:1', ULONG),
        ('MachineCheckInProgress:1', ULONG),
        ('Reserved1:29', ULONG),
        ('Reserved2', ULONG),
    ]


    class _MCI_STATUS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('McaErrorCode', USHORT),
        ('ModelErrorCode', USHORT),
        ('OtherInformation : 23', ULONG),
        ('ActionRequired : 1', ULONG),
        ('Signalling : 1', ULONG),
        ('ContextCorrupt : 1', ULONG),
        ('AddressValid : 1', ULONG),
        ('MiscValid : 1', ULONG),
        ('ErrorEnabled : 1', ULONG),
        ('UncorrectedError : 1', ULONG),
        ('StatusOverFlow : 1', ULONG),
        ('Valid : 1', ULONG),
    ]


    _MCI_STATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _MCI_STATUS._fields_ = [
        ('DUMMYSTRUCTNAME', _MCI_STATUS.DUMMYSTRUCTNAME),
        ('QuadPart', ULONG64),
    ]


    MCI_STATUS = _MCI_STATUS
    PMCI_STATUS = POINTER(_MCI_STATUS)


    DUMMYSTRUCTNAME._fields_ = [
        ('McaErrorCode', USHORT),
        ('ModelErrorCode', USHORT),
        ('OtherInformation : 23', ULONG),
        ('ActionRequired : 1', ULONG),
        ('Signalling : 1', ULONG),
        ('ContextCorrupt : 1', ULONG),
        ('AddressValid : 1', ULONG),
        ('MiscValid : 1', ULONG),
        ('ErrorEnabled : 1', ULONG),
        ('UncorrectedError : 1', ULONG),
        ('StatusOverFlow : 1', ULONG),
        ('Valid : 1', ULONG),
    ]


    class _WHEA_CPU_VENDOR(ENUM):
        WheaCpuVendorOther = 0
        WheaCpuVendorIntel = 1
        WheaCpuVendorAmd = 2


    WHEA_CPU_VENDOR = _WHEA_CPU_VENDOR
    PWHEA_CPU_VENDOR = POINTER(_WHEA_CPU_VENDOR)
    WHEA_XPF_MCA_EXTREG_MAX_COUNT = 24
    WHEA_XPF_MCA_SECTION_VERSION_2 = 2
    WHEA_XPF_MCA_SECTION_VERSION = WHEA_XPF_MCA_SECTION_VERSION_2
    class _WHEA_XPF_MCA_SECTION(ctypes.Structure):
        pass
    _WHEA_XPF_MCA_SECTION._fields_ = [
        ('VersionNumber', ULONG),
        ('CpuVendor', WHEA_CPU_VENDOR),
        ('Timestamp', LARGE_INTEGER),
        ('ProcessorNumber', ULONG),
        ('GlobalStatus', MCG_STATUS),
        ('InstructionPointer', ULONGLONG),
        ('BankNumber', ULONG),
        ('Status', MCI_STATUS),
        ('Address', ULONGLONG),
        ('Misc', ULONGLONG),
        ('ExtendedRegisterCount', ULONG),
        ('ApicId', ULONG),
        ('ExtendedRegisters', ULONGLONG * WHEA_XPF_MCA_EXTREG_MAX_COUNT),
    ]


    WHEA_XPF_MCA_SECTION = _WHEA_XPF_MCA_SECTION
    PWHEA_XPF_MCA_SECTION = POINTER(_WHEA_XPF_MCA_SECTION)


    class _WHEA_NMI_ERROR_SECTION_FLAGS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('HypervisorError:1', ULONG),
        ('Reserved:31', ULONG),
    ]


    _WHEA_NMI_ERROR_SECTION_FLAGS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_NMI_ERROR_SECTION_FLAGS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_NMI_ERROR_SECTION_FLAGS.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_NMI_ERROR_SECTION_FLAGS = _WHEA_NMI_ERROR_SECTION_FLAGS
    PWHEA_NMI_ERROR_SECTION_FLAGS = POINTER(_WHEA_NMI_ERROR_SECTION_FLAGS)


    DUMMYSTRUCTNAME._fields_ = [
        ('HypervisorError:1', ULONG),
        ('Reserved:31', ULONG),
    ]


    class _WHEA_NMI_ERROR_SECTION(ctypes.Structure):
        pass
    _WHEA_NMI_ERROR_SECTION._fields_ = [
        ('Data', UCHAR * 8),
        ('Flags', WHEA_NMI_ERROR_SECTION_FLAGS),
    ]


    WHEA_NMI_ERROR_SECTION = _WHEA_NMI_ERROR_SECTION
    PWHEA_NMI_ERROR_SECTION = POINTER(_WHEA_NMI_ERROR_SECTION)


    class _WHEA_ARM_PROCESSOR_ERROR_SECTION_VALID_BITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('MPIDR:1', ULONG),
        ('AffinityLevel:1', ULONG),
        ('RunningState:1', ULONG),
        ('VendorSpecificInfo:1', ULONG),
        ('Reserved:28', ULONG),
    ]


    _WHEA_ARM_PROCESSOR_ERROR_SECTION_VALID_BITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ARM_PROCESSOR_ERROR_SECTION_VALID_BITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ARM_PROCESSOR_ERROR_SECTION_VALID_BITS.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_ARM_PROCESSOR_ERROR_SECTION_VALID_BITS = _WHEA_ARM_PROCESSOR_ERROR_SECTION_VALID_BITS
    PWHEA_ARM_PROCESSOR_ERROR_SECTION_VALID_BITS = POINTER(_WHEA_ARM_PROCESSOR_ERROR_SECTION_VALID_BITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('MPIDR:1', ULONG),
        ('AffinityLevel:1', ULONG),
        ('RunningState:1', ULONG),
        ('VendorSpecificInfo:1', ULONG),
        ('Reserved:28', ULONG),
    ]


    class _WHEA_ARM_PROCESSOR_ERROR_SECTION(ctypes.Structure):
        pass
    _WHEA_ARM_PROCESSOR_ERROR_SECTION._fields_ = [
        ('ValidBits', WHEA_ARM_PROCESSOR_ERROR_SECTION_VALID_BITS),
        ('ErrorInformationStructures', USHORT),
        ('ContextInformationStructures', USHORT),
        ('SectionLength', ULONG),
        ('ErrorAffinityLevel', UCHAR),
        ('Reserved', UCHAR * 3),
        ('MPIDR_EL1', ULONGLONG),
        ('MIDR_EL1', ULONGLONG),
        ('RunningState', ULONG),
        ('PSCIState', ULONG),
        ('Data', UCHAR * 1),
    ]


    WHEA_ARM_PROCESSOR_ERROR_SECTION = _WHEA_ARM_PROCESSOR_ERROR_SECTION
    PWHEA_ARM_PROCESSOR_ERROR_SECTION = POINTER(_WHEA_ARM_PROCESSOR_ERROR_SECTION)


    class _WHEA_ARM_PROCESSOR_ERROR_INFORMATION_VALID_BITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('MultipleError:1', USHORT),
        ('Flags:1', USHORT),
        ('ErrorInformation:1', USHORT),
        ('VirtualFaultAddress:1', USHORT),
        ('PhysicalFaultAddress:1', USHORT),
        ('Reserved:11', USHORT),
    ]


    _WHEA_ARM_PROCESSOR_ERROR_INFORMATION_VALID_BITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ARM_PROCESSOR_ERROR_INFORMATION_VALID_BITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ARM_PROCESSOR_ERROR_INFORMATION_VALID_BITS.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    WHEA_ARM_PROCESSOR_ERROR_INFORMATION_VALID_BITS = _WHEA_ARM_PROCESSOR_ERROR_INFORMATION_VALID_BITS
    PWHEA_ARM_PROCESSOR_ERROR_INFORMATION_VALID_BITS = POINTER(_WHEA_ARM_PROCESSOR_ERROR_INFORMATION_VALID_BITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('MultipleError:1', USHORT),
        ('Flags:1', USHORT),
        ('ErrorInformation:1', USHORT),
        ('VirtualFaultAddress:1', USHORT),
        ('PhysicalFaultAddress:1', USHORT),
        ('Reserved:11', USHORT),
    ]


    class _WHEA_ARM_CACHE_ERROR_VALID_BITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionType:1', USHORT),
        ('Operation:1', USHORT),
        ('Level:1', USHORT),
        ('ProcessorContextCorrupt:1', USHORT),
        ('Corrected:1', USHORT),
        ('PrecisePC:1', USHORT),
        ('RestartablePC:1', USHORT),
        ('Reserved:9', USHORT),
    ]


    _WHEA_ARM_CACHE_ERROR_VALID_BITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ARM_CACHE_ERROR_VALID_BITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ARM_CACHE_ERROR_VALID_BITS.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    WHEA_ARM_CACHE_ERROR_VALID_BITS = _WHEA_ARM_CACHE_ERROR_VALID_BITS
    PWHEA_ARM_CACHE_ERROR_VALID_BITS = POINTER(_WHEA_ARM_CACHE_ERROR_VALID_BITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionType:1', USHORT),
        ('Operation:1', USHORT),
        ('Level:1', USHORT),
        ('ProcessorContextCorrupt:1', USHORT),
        ('Corrected:1', USHORT),
        ('PrecisePC:1', USHORT),
        ('RestartablePC:1', USHORT),
        ('Reserved:9', USHORT),
    ]


    class _WHEA_ARM_CACHE_ERROR(ctypes.Structure):
        pass
    _WHEA_ARM_CACHE_ERROR._fields_ = [
        ('ValidationBit', WHEA_ARM_CACHE_ERROR_VALID_BITS),
        ('TransactionType:2', UCHAR),
        ('Operation:4', UCHAR),
        ('Level:3', UCHAR),
        ('ProcessorContextCorrupt:1', UCHAR),
        ('Corrected:1', UCHAR),
        ('PrecisePC:1', UCHAR),
        ('RestartablePC:1', UCHAR),
        ('Reserved:35', ULONGLONG),
    ]


    WHEA_ARM_CACHE_ERROR = _WHEA_ARM_CACHE_ERROR
    PWHEA_ARM_CACHE_ERROR = POINTER(_WHEA_ARM_CACHE_ERROR)


    class _WHEA_ARM_TLB_ERROR_VALID_BITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionType:1', USHORT),
        ('Operation:1', USHORT),
        ('Level:1', USHORT),
        ('ProcessorContextCorrupt:1', USHORT),
        ('Corrected:1', USHORT),
        ('PrecisePC:1', USHORT),
        ('RestartablePC:1', USHORT),
        ('Reserved:9', USHORT),
    ]


    _WHEA_ARM_TLB_ERROR_VALID_BITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ARM_TLB_ERROR_VALID_BITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ARM_TLB_ERROR_VALID_BITS.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    WHEA_ARM_TLB_ERROR_VALID_BITS = _WHEA_ARM_TLB_ERROR_VALID_BITS
    PWHEA_ARM_TLB_ERROR_VALID_BITS = POINTER(_WHEA_ARM_TLB_ERROR_VALID_BITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionType:1', USHORT),
        ('Operation:1', USHORT),
        ('Level:1', USHORT),
        ('ProcessorContextCorrupt:1', USHORT),
        ('Corrected:1', USHORT),
        ('PrecisePC:1', USHORT),
        ('RestartablePC:1', USHORT),
        ('Reserved:9', USHORT),
    ]


    class _WHEA_ARM_TLB_ERROR(ctypes.Structure):
        pass
    _WHEA_ARM_TLB_ERROR._fields_ = [
        ('ValidationBit', WHEA_ARM_TLB_ERROR_VALID_BITS),
        ('TransactionType:2', UCHAR),
        ('Operation:4', UCHAR),
        ('Level:3', UCHAR),
        ('ProcessorContextCorrupt:1', UCHAR),
        ('Corrected:1', UCHAR),
        ('PrecisePC:1', UCHAR),
        ('RestartablePC:1', UCHAR),
        ('Reserved:36', ULONGLONG),
    ]


    WHEA_ARM_TLB_ERROR = _WHEA_ARM_TLB_ERROR
    PWHEA_ARM_TLB_ERROR = POINTER(_WHEA_ARM_TLB_ERROR)


    class _WHEA_ARM_BUS_ERROR_VALID_BITS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionType:1', USHORT),
        ('Operation:1', USHORT),
        ('Level:1', USHORT),
        ('ProcessorContextCorrupt:1', USHORT),
        ('Corrected:1', USHORT),
        ('PrecisePC:1', USHORT),
        ('RestartablePC:1', USHORT),
        ('ParticipationType:1', USHORT),
        ('Timeout:1', USHORT),
        ('AddressSpace:1', USHORT),
        ('MemoryAttributes:1', USHORT),
        ('AccessMode:1', USHORT),
        ('Reserved:4', USHORT),
    ]


    _WHEA_ARM_BUS_ERROR_VALID_BITS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ARM_BUS_ERROR_VALID_BITS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ARM_BUS_ERROR_VALID_BITS.DUMMYSTRUCTNAME),
        ('AsUSHORT', USHORT),
    ]


    WHEA_ARM_BUS_ERROR_VALID_BITS = _WHEA_ARM_BUS_ERROR_VALID_BITS
    PWHEA_ARM_BUS_ERROR_VALID_BITS = POINTER(_WHEA_ARM_BUS_ERROR_VALID_BITS)


    DUMMYSTRUCTNAME._fields_ = [
        ('TransactionType:1', USHORT),
        ('Operation:1', USHORT),
        ('Level:1', USHORT),
        ('ProcessorContextCorrupt:1', USHORT),
        ('Corrected:1', USHORT),
        ('PrecisePC:1', USHORT),
        ('RestartablePC:1', USHORT),
        ('ParticipationType:1', USHORT),
        ('Timeout:1', USHORT),
        ('AddressSpace:1', USHORT),
        ('MemoryAttributes:1', USHORT),
        ('AccessMode:1', USHORT),
        ('Reserved:4', USHORT),
    ]


    class _WHEA_ARM_BUS_ERROR(ctypes.Structure):
        pass
    _WHEA_ARM_BUS_ERROR._fields_ = [
        ('ValidationBit', WHEA_ARM_BUS_ERROR_VALID_BITS),
        ('TransactionType:2', UCHAR),
        ('Operation:4', UCHAR),
        ('Level:3', UCHAR),
        ('ProcessorContextCorrupt:1', UCHAR),
        ('Corrected:1', UCHAR),
        ('PrecisePC:1', UCHAR),
        ('RestartablePC:1', UCHAR),
        ('ParticipationType:2', UCHAR),
        ('TimeOut:1', UCHAR),
        ('AddressSpace:2', UCHAR),
        ('MemoryAccessAttributes:9', USHORT),
        ('AccessMode:1', UCHAR),
        ('Reserved:20', ULONG),
    ]


    WHEA_ARM_BUS_ERROR = _WHEA_ARM_BUS_ERROR
    PWHEA_ARM_BUS_ERROR = POINTER(_WHEA_ARM_BUS_ERROR)


    class _WHEA_ARM_PROCESSOR_ERROR(ctypes.Union):
        pass
    _WHEA_ARM_PROCESSOR_ERROR._fields_ = [
        ('CacheError', WHEA_ARM_CACHE_ERROR),
        ('TlbError', WHEA_ARM_TLB_ERROR),
        ('BusError', WHEA_ARM_BUS_ERROR),
        ('AsULONGLONG', ULONGLONG),
    ]


    WHEA_ARM_PROCESSOR_ERROR = _WHEA_ARM_PROCESSOR_ERROR
    PWHEA_ARM_PROCESSOR_ERROR = POINTER(_WHEA_ARM_PROCESSOR_ERROR)


    class _WHEA_ARM_PROCESSOR_ERROR_INFORMATION(ctypes.Structure):
        pass
    _WHEA_ARM_PROCESSOR_ERROR_INFORMATION._fields_ = [
        ('Version', UCHAR),
        ('Length', UCHAR),
        ('ValidationBit', WHEA_ARM_PROCESSOR_ERROR_INFORMATION_VALID_BITS),
        ('Type', UCHAR),
        ('MultipleError', USHORT),
        ('Flags', UCHAR),
        ('ErrorInformation', ULONGLONG),
        ('VirtualFaultAddress', ULONGLONG),
        ('PhysicalFaultAddress', ULONGLONG),
    ]


    WHEA_ARM_PROCESSOR_ERROR_INFORMATION = _WHEA_ARM_PROCESSOR_ERROR_INFORMATION
    PWHEA_ARM_PROCESSOR_ERROR_INFORMATION = POINTER(_WHEA_ARM_PROCESSOR_ERROR_INFORMATION)


    class _WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER_FLAGS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ExceptionLevel:1', ULONG),
        ('NonSecure:1', ULONG),
        ('AArch64:1', ULONG),
        ('Reserved:29', ULONG),
    ]


    _WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER_FLAGS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER_FLAGS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER_FLAGS.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER_FLAGS = _WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER_FLAGS
    PWHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER_FLAGS = POINTER(_WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER_FLAGS)


    DUMMYSTRUCTNAME._fields_ = [
        ('ExceptionLevel:1', ULONG),
        ('NonSecure:1', ULONG),
        ('AArch64:1', ULONG),
        ('Reserved:29', ULONG),
    ]


    class _WHEA_ARMV8_AARCH32_GPRS(ctypes.Structure):
        pass
    _WHEA_ARMV8_AARCH32_GPRS._fields_ = [
        ('R0', ULONG),
        ('R1', ULONG),
        ('R2', ULONG),
        ('R3', ULONG),
        ('R4', ULONG),
        ('R5', ULONG),
        ('R6', ULONG),
        ('R7', ULONG),
        ('R8', ULONG),
        ('R9', ULONG),
        ('R10', ULONG),
        ('R11', ULONG),
        ('R12', ULONG),
        ('R13', ULONG), # SP
        ('R14', ULONG), # LR
        ('R15', ULONG), # PC
    ]


    WHEA_ARMV8_AARCH32_GPRS = _WHEA_ARMV8_AARCH32_GPRS
    PWHEA_ARMV8_AARCH32_GPRS = POINTER(_WHEA_ARMV8_AARCH32_GPRS)


    class _WHEA_ARM_AARCH32_EL1_CSR(ctypes.Structure):
        pass
    _WHEA_ARM_AARCH32_EL1_CSR._fields_ = [
        ('DFAR', ULONG),
        ('DFSR', ULONG),
        ('IFAR', ULONG),
        ('ISR', ULONG),
        ('MAIR0', ULONG),
        ('MAIR1', ULONG),
        ('MIDR', ULONG),
        ('MPIDR', ULONG),
        ('NMRR', ULONG),
        ('PRRR', ULONG),
        ('SCTLR', ULONG), # NS
        ('SPSR', ULONG),
        ('SPSR_abt', ULONG),
        ('SPSR_fiq', ULONG),
        ('SPSR_irq', ULONG),
        ('SPSR_svc', ULONG),
        ('SPSR_und', ULONG),
        ('TPIDRPRW', ULONG),
        ('TPIDRURO', ULONG),
        ('TPIDRURW', ULONG),
        ('TTBCR', ULONG),
        ('TTBR0', ULONG),
        ('TTBR1', ULONG),
        ('DACR', ULONG),
    ]


    WHEA_ARM_AARCH32_EL1_CSR = _WHEA_ARM_AARCH32_EL1_CSR
    PWHEA_ARM_AARCH32_EL1 = POINTER(_WHEA_ARM_AARCH32_EL1_CSR)


    class _WHEA_ARM_AARCH32_EL2_CSR(ctypes.Structure):
        pass
    _WHEA_ARM_AARCH32_EL2_CSR._fields_ = [
        ('ELR_hyp', ULONG),
        ('HAMAIR0', ULONG),
        ('HAMAIR1', ULONG),
        ('HCR', ULONG),
        ('HCR2', ULONG),
        ('HDFAR', ULONG),
        ('HIFAR', ULONG),
        ('HPFAR', ULONG),
        ('HSR', ULONG),
        ('HTCR', ULONG),
        ('HTPIDR', ULONG),
        ('HTTBR', ULONG),
        ('SPSR_hyp', ULONG),
        ('VTCR', ULONG),
        ('VTTBR', ULONG),
        ('DACR32_EL2', ULONG),
    ]


    WHEA_ARM_AARCH32_EL2_CSR = _WHEA_ARM_AARCH32_EL2_CSR
    PWHEA_ARM_AARCH32_EL2_CSR = POINTER(_WHEA_ARM_AARCH32_EL2_CSR)


    class _WHEA_ARM_AARCH32_SECURE_CSR(ctypes.Structure):
        pass
    _WHEA_ARM_AARCH32_SECURE_CSR._fields_ = [
        ('SCTLR', ULONG),
        ('SPSR_mon', ULONG),
    ]


    WHEA_ARM_AARCH32_SECURE_CSR = _WHEA_ARM_AARCH32_SECURE_CSR
    PWHEA_ARM_AARCH32_SECURE_CSR = POINTER(_WHEA_ARM_AARCH32_SECURE_CSR)


    class _WHEA_ARMV8_AARCH64_GPRS(ctypes.Structure):
        pass
    _WHEA_ARMV8_AARCH64_GPRS._fields_ = [
        ('X0', ULONGLONG),
        ('X1', ULONGLONG),
        ('X2', ULONGLONG),
        ('X3', ULONGLONG),
        ('X4', ULONGLONG),
        ('X5', ULONGLONG),
        ('X6', ULONGLONG),
        ('X7', ULONGLONG),
        ('X8', ULONGLONG),
        ('X9', ULONGLONG),
        ('X10', ULONGLONG),
        ('X11', ULONGLONG),
        ('X12', ULONGLONG),
        ('X13', ULONGLONG),
        ('X14', ULONGLONG),
        ('X15', ULONGLONG),
        ('X16', ULONGLONG),
        ('X17', ULONGLONG),
        ('X18', ULONGLONG),
        ('X19', ULONGLONG),
        ('X20', ULONGLONG),
        ('X21', ULONGLONG),
        ('X22', ULONGLONG),
        ('X23', ULONGLONG),
        ('X24', ULONGLONG),
        ('X25', ULONGLONG),
        ('X26', ULONGLONG),
        ('X27', ULONGLONG),
        ('X28', ULONGLONG),
        ('X29', ULONGLONG),
        ('X30', ULONGLONG),
        ('SP', ULONGLONG),
    ]


    WHEA_ARMV8_AARCH64_GPRS = _WHEA_ARMV8_AARCH64_GPRS
    PWHEA_ARMV8_AARCH64_GPRS = POINTER(_WHEA_ARMV8_AARCH64_GPRS)


    class _WHEA_ARM_AARCH64_EL1_CSR(ctypes.Structure):
        pass
    _WHEA_ARM_AARCH64_EL1_CSR._fields_ = [
        ('ELR_EL1', ULONGLONG),
        ('ESR_EL2', ULONGLONG),
        ('FAR_EL1', ULONGLONG),
        ('ISR_EL1', ULONGLONG),
        ('MAIR_EL1', ULONGLONG),
        ('MIDR_EL1', ULONGLONG),
        ('MPIDR_EL1', ULONGLONG),
        ('SCTLR_EL1', ULONGLONG),
        ('SP_EL0', ULONGLONG),
        ('SP_EL1', ULONGLONG),
        ('SPSR_EL1', ULONGLONG),
        ('TCR_EL1', ULONGLONG),
        ('TPIDR_EL0', ULONGLONG),
        ('TPIDR_EL1', ULONGLONG),
        ('TPIDRRO_EL0', ULONGLONG),
        ('TTBR0_EL1', ULONGLONG),
        ('TTBR1_EL1', ULONGLONG),
    ]


    WHEA_ARM_AARCH64_EL1_CSR = _WHEA_ARM_AARCH64_EL1_CSR
    PWHEA_ARM_AARCH64_EL1_CSR = POINTER(_WHEA_ARM_AARCH64_EL1_CSR)


    class _WHEA_ARM_AARCH64_EL2_CSR(ctypes.Structure):
        pass
    _WHEA_ARM_AARCH64_EL2_CSR._fields_ = [
        ('ELR_EL2', ULONGLONG),
        ('ESR_EL2', ULONGLONG),
        ('FAR_EL2', ULONGLONG),
        ('HACR_EL2', ULONGLONG),
        ('HCR_EL2', ULONGLONG),
        ('HPFAR_EL2', ULONGLONG),
        ('MAIR_EL2', ULONGLONG),
        ('SCTLR_EL2', ULONGLONG),
        ('SP_EL2', ULONGLONG),
        ('SPSR_EL2', ULONGLONG),
        ('TCR_EL2', ULONGLONG),
        ('TPIDR_EL2', ULONGLONG),
        ('TTBR0_EL2', ULONGLONG),
        ('VTCR_EL2', ULONGLONG),
        ('VTTBR_EL2', ULONGLONG),
    ]


    WHEA_ARM_AARCH64_EL2_CSR = _WHEA_ARM_AARCH64_EL2_CSR
    PWHEA_ARM_AARCH64_EL2_CSR = POINTER(_WHEA_ARM_AARCH64_EL2_CSR)


    class _WHEA_ARMV8_AARCH64_EL3_CSR(ctypes.Structure):
        pass
    _WHEA_ARMV8_AARCH64_EL3_CSR._fields_ = [
        ('ELR_EL3', ULONGLONG),
        ('ESR_EL3', ULONGLONG),
        ('FAR_EL3', ULONGLONG),
        ('MAIR_EL3', ULONGLONG),
        ('SCTLR_EL3', ULONGLONG),
        ('SP_EL3', ULONGLONG),
        ('SPSR_EL3', ULONGLONG),
        ('TCR_EL3', ULONGLONG),
        ('TPIDR_EL3', ULONGLONG),
        ('TTBR0_EL3', ULONGLONG),
    ]


    WHEA_ARMV8_AARCH64_EL3_CSR = _WHEA_ARMV8_AARCH64_EL3_CSR
    PWHEA_ARMV8_AARCH64_EL3_CSR = POINTER(_WHEA_ARMV8_AARCH64_EL3_CSR)


    class _WHEA_ARM_MISC_CSR(ctypes.Structure):
        pass
    _WHEA_ARM_MISC_CSR._fields_ = [
        ('MRSEncoding', USHORT),
        ('Value', ULONGLONG),
    ]


    WHEA_ARM_MISC_CSR = _WHEA_ARM_MISC_CSR
    PWHEA_ARM_MISC_CSR = POINTER(_WHEA_ARM_MISC_CSR)


    class _WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER(ctypes.Structure):
        pass
    _WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER._fields_ = [
        ('Version', USHORT),
        ('RegisterContextType', USHORT),
        ('RegisterArraySize', ULONG),
        ('RegisterArray', UCHAR * 1),
    ]


    WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER = _WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER
    PWHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER = POINTER(_WHEA_ARM_PROCESSOR_ERROR_CONTEXT_INFORMATION_HEADER)



    if defined(_NTPSHEDDLL_):
        NTPSHEDAPI = 1
else:
        NTPSHEDAPI = DECLSPEC_IMPORT
    # END IF


    class _WHEA_ERROR_TYPE(ENUM):
        WheaErrTypeProcessor = 0
        WheaErrTypeMemory = 1
        WheaErrTypePCIExpress = 2
        WheaErrTypeNMI = 3
        WheaErrTypePCIXBus = 4
        WheaErrTypePCIXDevice = 5
        WheaErrTypeGeneric = 6


    WHEA_ERROR_TYPE = _WHEA_ERROR_TYPE
    PWHEA_ERROR_TYPE = POINTER(_WHEA_ERROR_TYPE)
    class _WHEA_ERROR_PACKET_FLAGS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('PreviousError:1', ULONG),
        ('Reserved1:1', ULONG),
        ('HypervisorError:1', ULONG),
        ('Simulated:1', ULONG),
        ('PlatformPfaControl:1', ULONG),
        ('PlatformDirectedOffline:1', ULONG),
        ('Reserved2:26', ULONG),
    ]


    _WHEA_ERROR_PACKET_FLAGS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ERROR_PACKET_FLAGS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ERROR_PACKET_FLAGS.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_ERROR_PACKET_FLAGS = _WHEA_ERROR_PACKET_FLAGS
    PWHEA_ERROR_PACKET_FLAGS = POINTER(_WHEA_ERROR_PACKET_FLAGS)


    DUMMYSTRUCTNAME._fields_ = [
        ('PreviousError:1', ULONG),
        ('Reserved1:1', ULONG),
        ('HypervisorError:1', ULONG),
        ('Simulated:1', ULONG),
        ('PlatformPfaControl:1', ULONG),
        ('PlatformDirectedOffline:1', ULONG),
        ('Reserved2:26', ULONG),
    ]


    class _WHEA_ERROR_PACKET_DATA_FORMAT(ENUM):
        WheaDataFormatIPFSalRecord = 0
        WheaDataFormatXPFMCA = 1
        WheaDataFormatMemory = 2
        WheaDataFormatPCIExpress = 3
        WheaDataFormatNMIPort = 4
        WheaDataFormatPCIXBus = 5
        WheaDataFormatPCIXDevice = 6
        WheaDataFormatGeneric = 7
        WheaDataFormatMax = 8


    WHEA_ERROR_PACKET_DATA_FORMAT = _WHEA_ERROR_PACKET_DATA_FORMAT
    PWHEA_ERROR_PACKET_DATA_FORMAT = POINTER(_WHEA_ERROR_PACKET_DATA_FORMAT)
    class _WHEA_RAW_DATA_FORMAT(ENUM):
        WheaRawDataFormatIPFSalRecord = 0x00
        WheaRawDataFormatIA32MCA = 1
        WheaRawDataFormatIntel64MCA = 2
        WheaRawDataFormatAMD64MCA = 3
        WheaRawDataFormatMemory = 4
        WheaRawDataFormatPCIExpress = 5
        WheaRawDataFormatNMIPort = 6
        WheaRawDataFormatPCIXBus = 7
        WheaRawDataFormatPCIXDevice = 8
        WheaRawDataFormatGeneric = 9
        WheaRawDataFormatMax = 10


    WHEA_RAW_DATA_FORMAT = _WHEA_RAW_DATA_FORMAT
    PWHEA_RAW_DATA_FORMAT = POINTER(_WHEA_RAW_DATA_FORMAT)
    class _WHEA_ERROR_PACKET_V1(ctypes.Structure):
        pass
    u._fields_ = [
        ('ProcessorError', WHEA_PROCESSOR_GENERIC_ERROR_SECTION), # + 0x40 (64)
        ('MemoryError', WHEA_MEMORY_ERROR_SECTION),
        ('NmiError', WHEA_NMI_ERROR_SECTION),
        ('PciExpressError', WHEA_PCIEXPRESS_ERROR_SECTION),
        ('PciXBusError', WHEA_PCIXBUS_ERROR_SECTION),
        ('PciXDeviceError', WHEA_PCIXDEVICE_ERROR_SECTION),
    ]


    _WHEA_ERROR_PACKET_V1.u = u
    _WHEA_ERROR_PACKET_V1._fields_ = [
        ('Signature', ULONG), # + 0x00 (0)
        ('Flags', WHEA_ERROR_PACKET_FLAGS), # + 0x04 (4)
        ('Size', ULONG), # + 0x08 (8)
        ('RawDataLength', ULONG), # + 0x0C (12)
        ('Reserved1', ULONGLONG), # + 0x10 (16)
        ('Context', ULONGLONG), # + 0x18 (24)
        ('ErrorType', WHEA_ERROR_TYPE), # + 0x20 (32)
        ('ErrorSeverity', WHEA_ERROR_SEVERITY), # + 0x24 (36)
        ('ErrorSourceId', ULONG), # + 0x28 (40)
        ('ErrorSourceType', WHEA_ERROR_SOURCE_TYPE), # + 0x2C (44)
        ('Reserved2', ULONG), # + 0x30 (48)
        ('Version', ULONG), # + 0x34 (52)
        ('Cpu', ULONGLONG), # + 0x38 (56)
        ('u', _WHEA_ERROR_PACKET_V1.u),
        ('RawDataFormat', WHEA_RAW_DATA_FORMAT), # + 0x110 (272)
        ('RawDataOffset', ULONG), # + 0x114 (276)
        ('RawData', UCHAR * 1), # + 0x118 (280)
    ]


    WHEA_ERROR_PACKET_V1 = _WHEA_ERROR_PACKET_V1
    PWHEA_ERROR_PACKET_V1 = POINTER(_WHEA_ERROR_PACKET_V1)


    u._fields_ = [
        ('ProcessorError', WHEA_PROCESSOR_GENERIC_ERROR_SECTION), # + 0x40 (64)
        ('MemoryError', WHEA_MEMORY_ERROR_SECTION),
        ('NmiError', WHEA_NMI_ERROR_SECTION),
        ('PciExpressError', WHEA_PCIEXPRESS_ERROR_SECTION),
        ('PciXBusError', WHEA_PCIXBUS_ERROR_SECTION),
        ('PciXDeviceError', WHEA_PCIXDEVICE_ERROR_SECTION),
    ]


    WHEA_ERROR_PACKET_V1_SIGNATURE = 'tPrE'
    WHEA_ERROR_PACKET_V1_VERSION = 2
    class _WHEA_ERROR_PACKET_V2(ctypes.Structure):
        pass
    _WHEA_ERROR_PACKET_V2._fields_ = [
        ('Signature', ULONG),
        ('Version', ULONG),
        ('Length', ULONG),
        ('Flags', WHEA_ERROR_PACKET_FLAGS),
        ('ErrorType', WHEA_ERROR_TYPE),
        ('ErrorSeverity', WHEA_ERROR_SEVERITY),
        ('ErrorSourceId', ULONG),
        ('ErrorSourceType', WHEA_ERROR_SOURCE_TYPE),
        ('NotifyType', GUID),
        ('Context', ULONGLONG),
        ('DataFormat', WHEA_ERROR_PACKET_DATA_FORMAT),
        ('Reserved1', ULONG),
        ('DataOffset', ULONG),
        ('DataLength', ULONG),
        ('PshedDataOffset', ULONG),
        ('PshedDataLength', ULONG),
    ]


    WHEA_ERROR_PACKET_V2 = _WHEA_ERROR_PACKET_V2
    PWHEA_ERROR_PACKET_V2 = POINTER(_WHEA_ERROR_PACKET_V2)


    WHEA_ERROR_PACKET_V2_SIGNATURE = 'AEHW'
    WHEA_ERROR_PACKET_V2_VERSION = 3

    if (NTDDI_VERSION >= NTDDI_WIN7):
        WHEA_ERROR_PACKET_SIGNATURE = WHEA_ERROR_PACKET_V2_SIGNATURE
        WHEA_ERROR_PACKET_VERSION = WHEA_ERROR_PACKET_V2_VERSION
        PWHEA_ERROR_PACKET = POINTER(WHEA_ERROR_PACKET,)


else:
        WHEA_ERROR_PACKET_SIGNATURE = WHEA_ERROR_PACKET_V1_SIGNATURE
        WHEA_ERROR_PACKET_VERSION = WHEA_ERROR_PACKET_V1_VERSION
        WHEA_ERROR_PKT_SIGNATURE = WHEA_ERROR_PACKET_SIGNATURE
        WHEA_ERROR_PKT_VERSION = WHEA_ERROR_PACKET_VERSION
        PWHEA_ERROR_PACKET = POINTER(WHEA_ERROR_PACKET,)


    # END IF
    class _WHEA_GENERIC_ERROR_BLOCKSTATUS(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('UncorrectableError:1', ULONG),
        ('CorrectableError:1', ULONG),
        ('MultipleUncorrectableErrors:1', ULONG),
        ('MultipleCorrectableErrors:1', ULONG),
        ('ErrorDataEntryCount:10', ULONG),
        ('Reserved:18', ULONG),
    ]


    _WHEA_GENERIC_ERROR_BLOCKSTATUS.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_GENERIC_ERROR_BLOCKSTATUS._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_GENERIC_ERROR_BLOCKSTATUS.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_GENERIC_ERROR_BLOCKSTATUS = _WHEA_GENERIC_ERROR_BLOCKSTATUS
    PWHEA_GENERIC_ERROR_BLOCKSTATUS = POINTER(_WHEA_GENERIC_ERROR_BLOCKSTATUS)


    DUMMYSTRUCTNAME._fields_ = [
        ('UncorrectableError:1', ULONG),
        ('CorrectableError:1', ULONG),
        ('MultipleUncorrectableErrors:1', ULONG),
        ('MultipleCorrectableErrors:1', ULONG),
        ('ErrorDataEntryCount:10', ULONG),
        ('Reserved:18', ULONG),
    ]


    class _WHEA_GENERIC_ERROR(ctypes.Structure):
        pass
    _WHEA_GENERIC_ERROR._fields_ = [
        ('BlockStatus', WHEA_GENERIC_ERROR_BLOCKSTATUS),
        ('RawDataOffset', ULONG),
        ('RawDataLength', ULONG),
        ('DataLength', ULONG),
        ('ErrorSeverity', WHEA_ERROR_SEVERITY),
        ('Data', UCHAR * 1),
    ]


    WHEA_GENERIC_ERROR = _WHEA_GENERIC_ERROR
    PWHEA_GENERIC_ERROR = POINTER(_WHEA_GENERIC_ERROR)


    class _WHEA_GENERIC_ERROR_DATA_ENTRY_V1(ctypes.Structure):
        pass
    _WHEA_GENERIC_ERROR_DATA_ENTRY_V1._fields_ = [
        ('SectionType', GUID),
        ('ErrorSeverity', WHEA_ERROR_SEVERITY),
        ('Revision', WHEA_REVISION),
        ('ValidBits', UCHAR),
        ('Flags', UCHAR),
        ('ErrorDataLength', ULONG),
        ('FRUId', GUID),
        ('FRUText', UCHAR * 20),
        ('Data', UCHAR * 1),
    ]


    WHEA_GENERIC_ERROR_DATA_ENTRY_V1 = _WHEA_GENERIC_ERROR_DATA_ENTRY_V1
    PWHEA_GENERIC_ERROR_DATA_ENTRY_V1 = POINTER(_WHEA_GENERIC_ERROR_DATA_ENTRY_V1)


    class _WHEA_GENERIC_ERROR_DATA_ENTRY_V2(ctypes.Structure):
        pass
    _WHEA_GENERIC_ERROR_DATA_ENTRY_V2._fields_ = [
        ('SectionType', GUID),
        ('ErrorSeverity', WHEA_ERROR_SEVERITY),
        ('Revision', WHEA_REVISION),
        ('ValidBits', UCHAR),
        ('Flags', UCHAR),
        ('ErrorDataLength', ULONG),
        ('FRUId', GUID),
        ('FRUText', UCHAR * 20),
        ('Timestamp', WHEA_TIMESTAMP),
        ('Data', UCHAR * 1),
    ]


    WHEA_GENERIC_ERROR_DATA_ENTRY_V2 = _WHEA_GENERIC_ERROR_DATA_ENTRY_V2
    PWHEA_GENERIC_ERROR_DATA_ENTRY_V2 = POINTER(_WHEA_GENERIC_ERROR_DATA_ENTRY_V2)


    WHEA_GENERIC_ENTRY_V2_VERSION = 0x300
    WHEA_GENERIC_ENTRY_VERSION = WHEA_GENERIC_ENTRY_V2_VERSION
    PWHEA_GENERIC_ERROR_DATA_ENTRY = POINTER(WHEA_GENERIC_ERROR_DATA_ENTRY,)


    class _WHEA_ERROR_INJECTION_CAPABILITIES(ctypes.Union):
        pass
    DUMMYSTRUCTNAME._fields_ = [
        ('ProcessorCorrectable:1', ULONG), # 0x00000001
        ('ProcessorUncorrectableNonFatal:1', ULONG), # 0x00000002
        ('ProcessorUncorrectableFatal:1', ULONG), # 0x00000004
        ('MemoryCorrectable:1', ULONG), # 0x00000008
        ('MemoryUncorrectableNonFatal:1', ULONG), # 0x00000010
        ('MemoryUncorrectableFatal:1', ULONG), # 0x00000020
        ('PCIExpressCorrectable:1', ULONG), # 0x00000040
        ('PCIExpressUncorrectableNonFatal:1', ULONG), # 0x00000080
        ('PCIExpressUncorrectableFatal:1', ULONG), # 0x00000100
        ('PlatformCorrectable:1', ULONG), # 0x00000200
        ('PlatformUncorrectableNonFatal:1', ULONG), # 0x00000400
        ('PlatformUncorrectableFatal:1', ULONG), # 0x00000800
        ('IA64Corrected:1', ULONG), # 0x00001000
        ('IA64Recoverable:1', ULONG), # 0x00002000
        ('IA64Fatal:1', ULONG), # 0x00004000
        ('IA64RecoverableCache:1', ULONG), # 0x00008000
        ('IA64RecoverableRegFile:1', ULONG), # 0x00010000
        ('Reserved:15', ULONG),
    ]


    _WHEA_ERROR_INJECTION_CAPABILITIES.DUMMYSTRUCTNAME = DUMMYSTRUCTNAME
    _WHEA_ERROR_INJECTION_CAPABILITIES._fields_ = [
        ('DUMMYSTRUCTNAME', _WHEA_ERROR_INJECTION_CAPABILITIES.DUMMYSTRUCTNAME),
        ('AsULONG', ULONG),
    ]


    WHEA_ERROR_INJECTION_CAPABILITIES = _WHEA_ERROR_INJECTION_CAPABILITIES
    PWHEA_ERROR_INJECTION_CAPABILITIES = POINTER(_WHEA_ERROR_INJECTION_CAPABILITIES)


    DUMMYSTRUCTNAME._fields_ = [
        ('ProcessorCorrectable:1', ULONG), # 0x00000001
        ('ProcessorUncorrectableNonFatal:1', ULONG), # 0x00000002
        ('ProcessorUncorrectableFatal:1', ULONG), # 0x00000004
        ('MemoryCorrectable:1', ULONG), # 0x00000008
        ('MemoryUncorrectableNonFatal:1', ULONG), # 0x00000010
        ('MemoryUncorrectableFatal:1', ULONG), # 0x00000020
        ('PCIExpressCorrectable:1', ULONG), # 0x00000040
        ('PCIExpressUncorrectableNonFatal:1', ULONG), # 0x00000080
        ('PCIExpressUncorrectableFatal:1', ULONG), # 0x00000100
        ('PlatformCorrectable:1', ULONG), # 0x00000200
        ('PlatformUncorrectableNonFatal:1', ULONG), # 0x00000400
        ('PlatformUncorrectableFatal:1', ULONG), # 0x00000800
        ('IA64Corrected:1', ULONG), # 0x00001000
        ('IA64Recoverable:1', ULONG), # 0x00002000
        ('IA64Fatal:1', ULONG), # 0x00004000
        ('IA64RecoverableCache:1', ULONG), # 0x00008000
        ('IA64RecoverableRegFile:1', ULONG), # 0x00010000
        ('Reserved:15', ULONG),
    ]


    INJECT_ERRTYPE_PROCESSOR_CORRECTABLE = 0x00000001
    INJECT_ERRTYPE_PROCESSOR_UNCORRECTABLENONFATAL = 0x00000002
    INJECT_ERRTYPE_PROCESSOR_UNCORRECTABLEFATAL = 0x00000004
    INJECT_ERRTYPE_MEMORY_CORRECTABLE = 0x00000008
    INJECT_ERRTYPE_MEMORY_UNCORRECTABLENONFATAL = 0x00000010
    INJECT_ERRTYPE_MEMORY_UNCORRECTABLEFATAL = 0x00000020
    INJECT_ERRTYPE_PCIEXPRESS_CORRECTABLE = 0x00000040
    INJECT_ERRTYPE_PCIEXPRESS_UNCORRECTABLENONFATAL = 0x00000080
    INJECT_ERRTYPE_PCIEXPRESS_UNCORRECTABLEFATAL = 0x00000100
    INJECT_ERRTYPE_PLATFORM_CORRECTABLE = 0x00000200
    INJECT_ERRTYPE_PLATFORM_UNCORRECTABLENONFATAL = 0x00000400
    INJECT_ERRTYPE_PLATFORM_UNCORRECTABLEFATAL = 0x00000800

    if defined (_AMD64_):
        pass
    # END IF   _AMD64_
    class _WHEA_RECOVERY_CONTEXT(ctypes.Structure):
        pass
    MemoryError._fields_ = [
        ('Address', ULONG_PTR),
        ('Consumed', BOOLEAN),
        ('ErrorCode', UINT16),
        ('ErrorIpValid', BOOLEAN),
        ('RestartIpValid', BOOLEAN),
    ]


    _Struct_36.MemoryError = MemoryError
    _Struct_36._fields_ = [
        ('MemoryError', _Struct_36.MemoryError),
    ]


    _WHEA_RECOVERY_CONTEXT._Struct_36 = _Struct_36
    _WHEA_RECOVERY_CONTEXT._anonymous_ = (
        '_Struct_36',
    )
    _WHEA_RECOVERY_CONTEXT._fields_ = [
        ('_Struct_36', _WHEA_RECOVERY_CONTEXT._Struct_36),
        ('PartitionId', UINT64), # HV_PARTITION_ID
        ('VpIndex', UINT32), # HV_VP_INDEX
    ]


    WHEA_RECOVERY_CONTEXT = _WHEA_RECOVERY_CONTEXT
    PWHEA_RECOVERY_CONTEXT = POINTER(_WHEA_RECOVERY_CONTEXT)


    MemoryError._fields_ = [
        ('Address', ULONG_PTR),
        ('Consumed', BOOLEAN),
        ('ErrorCode', UINT16),
        ('ErrorIpValid', BOOLEAN),
        ('RestartIpValid', BOOLEAN),
    ]


    .MemoryError = MemoryError
    ._fields_ = [
        ('MemoryError', .MemoryError),
    ]


    MemoryError._fields_ = [
        ('Address', ULONG_PTR),
        ('Consumed', BOOLEAN),
        ('ErrorCode', UINT16),
        ('ErrorIpValid', BOOLEAN),
        ('RestartIpValid', BOOLEAN),
    ]


    if not defined(XBOX_SYSTEMOS):
        pass
    # END IF
    class _WHEA_PSHED_PLUGIN_CALLBACKS(ctypes.Structure):
        pass
    _WHEA_PSHED_PLUGIN_CALLBACKS._fields_ = [
        ('GetAllErrorSources', PSHED_PI_GET_ALL_ERROR_SOURCES),
        ('Reserved', PVOID),
        ('GetErrorSourceInfo', PSHED_PI_GET_ERROR_SOURCE_INFO),
        ('SetErrorSourceInfo', PSHED_PI_SET_ERROR_SOURCE_INFO),
        ('EnableErrorSource', PSHED_PI_ENABLE_ERROR_SOURCE),
        ('DisableErrorSource', PSHED_PI_DISABLE_ERROR_SOURCE),
        ('WriteErrorRecord', PSHED_PI_WRITE_ERROR_RECORD),
        ('ReadErrorRecord', PSHED_PI_READ_ERROR_RECORD),
        ('ClearErrorRecord', PSHED_PI_CLEAR_ERROR_RECORD),
        ('RetrieveErrorInfo', PSHED_PI_RETRIEVE_ERROR_INFO),
        ('FinalizeErrorRecord', PSHED_PI_FINALIZE_ERROR_RECORD),
        ('ClearErrorStatus', PSHED_PI_CLEAR_ERROR_STATUS),
        ('AttemptRecovery', PSHED_PI_ATTEMPT_ERROR_RECOVERY),
        ('GetInjectionCapabilities', PSHED_PI_GET_INJECTION_CAPABILITIES),
        ('InjectError', PSHED_PI_INJECT_ERROR),
    ]


    WHEA_PSHED_PLUGIN_CALLBACKS = _WHEA_PSHED_PLUGIN_CALLBACKS
    PWHEA_PSHED_PLUGIN_CALLBACKS = POINTER(_WHEA_PSHED_PLUGIN_CALLBACKS)


    class _WHEA_PSHED_PLUGIN_REGISTRATION_PACKET(ctypes.Structure):
        pass
    _WHEA_PSHED_PLUGIN_REGISTRATION_PACKET._fields_ = [
        ('Length', ULONG),
        ('Version', ULONG),
        ('Context', PVOID),
        ('FunctionalAreaMask', ULONG),
        ('Reserved', ULONG),
        ('Callbacks', WHEA_PSHED_PLUGIN_CALLBACKS),
    ]


    WHEA_PSHED_PLUGIN_REGISTRATION_PACKET = _WHEA_PSHED_PLUGIN_REGISTRATION_PACKET
    PWHEA_PSHED_PLUGIN_REGISTRATION_PACKET = POINTER(_WHEA_PSHED_PLUGIN_REGISTRATION_PACKET)


    WHEA_PLUGIN_REGISTRATION_PACKET_VERSION = 0x00010000
    PshedFADiscovery = 0x00000001
    PshedFAErrorSourceControl = 0x00000002
    PshedFAErrorRecordPersistence = 0x00000004
    PshedFAErrorInfoRetrieval = 0x00000008
    PshedFAErrorRecovery = 0x00000010
    PshedFAErrorInjection = 0x00000020
    WHEA_WRITE_FLAG_DUMMY = 0x00000001

    if (NTDDI_VERSION >= NTDDI_WS08):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WS08):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WS08):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WS08):
        pass
    # END IF
    if (NTDDI_VERSION >= NTDDI_WS08):
        pass
    # END IF
    class _SOC_SUBSYSTEM_TYPE(ENUM):
        SOC_SUBSYS_WIRELESS_MODEM = 0
        SOC_SUBSYS_AUDIO_DSP = 1
        SOC_SUBSYS_WIRELSS_CONNECTIVITY = 2
        SOC_SUBSYS_SENSORS = 3
        SOC_SUBSYS_COMPUTE_DSP = 4
        SOC_SUBSYS_VENDOR_DEFINED = 0x10000


    SOC_SUBSYSTEM_TYPE = _SOC_SUBSYSTEM_TYPE
    PSOC_SUBSYSTEM_TYPE = POINTER(_SOC_SUBSYSTEM_TYPE)
    class _SOC_SUBSYSTEM_FAILURE_DETAILS(ctypes.Structure):
        pass
    _SOC_SUBSYSTEM_FAILURE_DETAILS._fields_ = [
        ('SubsysType', SOC_SUBSYSTEM_TYPE),
        ('FirmwareVersion', ULONG64),
        ('HardwareVersion', ULONG64),
        ('UnifiedFailureRegionSize', ULONG),
        ('UnifiedFailureRegion', CHAR * 1),
    ]


    SOC_SUBSYSTEM_FAILURE_DETAILS = _SOC_SUBSYSTEM_FAILURE_DETAILS
    PSOC_SUBSYSTEM_FAILURE_DETAILS = POINTER(_SOC_SUBSYSTEM_FAILURE_DETAILS)


    if defined(__cplusplus):
        pass
    # END IF
    if _MSC_VER >= 1200:
        pass
else:
        pass
    # END IF
# END IF   _NTDDK_
