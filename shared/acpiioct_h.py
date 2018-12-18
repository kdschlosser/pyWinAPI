import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *


class _ACPI_EVAL_INPUT_BUFFER_V1(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_V1 = _ACPI_EVAL_INPUT_BUFFER_V1
PACPI_EVAL_INPUT_BUFFER_V1 = POINTER(_ACPI_EVAL_INPUT_BUFFER_V1)


class _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1 = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1
PACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1 = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1)


class _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1 = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1
PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1 = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1)


class _ACPI_METHOD_ARGUMENT_V1(ctypes.Structure):
    pass


ACPI_METHOD_ARGUMENT_V1 = _ACPI_METHOD_ARGUMENT_V1


class _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1 = _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1
PACPI_EVAL_INPUT_BUFFER_COMPLEX_V1 = POINTER(_ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1)


class _ACPI_EVAL_OUTPUT_BUFFER_V1(ctypes.Structure):
    pass


ACPI_EVAL_OUTPUT_BUFFER_V1 = _ACPI_EVAL_OUTPUT_BUFFER_V1


class _ACPI_EVAL_INPUT_BUFFER_V1_EX(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_V1_EX = _ACPI_EVAL_INPUT_BUFFER_V1_EX
PACPI_EVAL_INPUT_BUFFER_V1_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_V1_EX)


class _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX
PACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX)


class _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1_EX(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1_EX = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1_EX
PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1_EX)


class _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX = _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX
PACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX)


class _ACPI_EVAL_INPUT_BUFFER_V2(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_V2 = _ACPI_EVAL_INPUT_BUFFER_V2
PACPI_EVAL_INPUT_BUFFER_V2 = POINTER(_ACPI_EVAL_INPUT_BUFFER_V2)


class _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2 = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2
PACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2 = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2)


class _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2 = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2
PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2 = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2)


class _ACPI_METHOD_ARGUMENT_V2(ctypes.Structure):
    pass


ACPI_METHOD_ARGUMENT_V2 = _ACPI_METHOD_ARGUMENT_V2


class _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2 = _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2
PACPI_EVAL_INPUT_BUFFER_COMPLEX_V2 = POINTER(_ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2)


class _ACPI_EVAL_OUTPUT_BUFFER_V2(ctypes.Structure):
    pass


ACPI_EVAL_OUTPUT_BUFFER_V2 = _ACPI_EVAL_OUTPUT_BUFFER_V2


class _ACPI_EVAL_INPUT_BUFFER_V2_EX(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_V2_EX = _ACPI_EVAL_INPUT_BUFFER_V2_EX
PACPI_EVAL_INPUT_BUFFER_V2_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_V2_EX)


class _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2_EX(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2_EX = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2_EX
PACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2_EX)


class _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2_EX(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2_EX = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2_EX
PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2_EX)


class _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX(ctypes.Structure):
    pass


ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX = _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX
PACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX)


class _ACPI_MANIPULATE_GLOBAL_LOCK_BUFFER(ctypes.Structure):
    pass


ACPI_MANIPULATE_GLOBAL_LOCK_BUFFER = _ACPI_MANIPULATE_GLOBAL_LOCK_BUFFER
PACPI_MANIPULATE_GLOBAL_LOCK_BUFFER = POINTER(_ACPI_MANIPULATE_GLOBAL_LOCK_BUFFER)


class _ACPI_ENUM_CHILDREN_INPUT_BUFFER(ctypes.Structure):
    pass


ACPI_ENUM_CHILDREN_INPUT_BUFFER = _ACPI_ENUM_CHILDREN_INPUT_BUFFER
PACPI_ENUM_CHILDREN_INPUT_BUFFER = POINTER(_ACPI_ENUM_CHILDREN_INPUT_BUFFER)


class _ACPI_ENUM_CHILD(ctypes.Structure):
    pass


ACPI_ENUM_CHILD = _ACPI_ENUM_CHILD
PACPI_ENUM_CHILD = POINTER(_ACPI_ENUM_CHILD)


class _ACPI_ENUM_CHILDREN_OUTPUT_BUFFER(ctypes.Structure):
    pass


ACPI_ENUM_CHILDREN_OUTPUT_BUFFER = _ACPI_ENUM_CHILDREN_OUTPUT_BUFFER
PACPI_ENUM_CHILDREN_OUTPUT_BUFFER = POINTER(_ACPI_ENUM_CHILDREN_OUTPUT_BUFFER)


class _ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER(ctypes.Structure):
    pass


ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER = _ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER
PACPI_DEVICE_INFORMATION_OUTPUT_BUFFER = POINTER(_ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER)


class _ACPI_GET_DEVICE_SPECIFIC_DATA(ctypes.Structure):
    pass


ACPI_GET_DEVICE_SPECIFIC_DATA = _ACPI_GET_DEVICE_SPECIFIC_DATA
PACPI_GET_DEVICE_SPECIFIC_DATA = POINTER(_ACPI_GET_DEVICE_SPECIFIC_DATA)


# /* + + Copyright (c) 1997 Microsoft Corporation Module Name: acpiioct.h
# Abstract: This module handles all of the INTERNAL_DEVICE_CONTROLS requested
# to the ACPI driver Author: Environment: NT Kernel Model Driver only - -
_ACPIIOCT_H_ = None

if not defined(_ACPIIOCT_H_):

    from pyWinAPI.shared.devioctl_h import * # NOQA
    _ACPIIOCT_H_ = 1

    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # IRP_MJ_INTERNAL_DEVICE_CONTROL CODES
    IOCTL_ACPI_ASYNC_EVAL_METHOD_V1 = CTL_CODE(
        FILE_DEVICE_ACPI,
        0,
        METHOD_BUFFERED,
        FILE_READ_ACCESS | FILE_WRITE_ACCESS,
    )
    IOCTL_ACPI_EVAL_METHOD_V1 = CTL_CODE(
        FILE_DEVICE_ACPI,
        1,
        METHOD_BUFFERED,
        FILE_READ_ACCESS | FILE_WRITE_ACCESS,
    )
    IOCTL_ACPI_ACQUIRE_GLOBAL_LOCK = CTL_CODE(
        FILE_DEVICE_ACPI,
        4,
        METHOD_BUFFERED,
        FILE_READ_ACCESS | FILE_WRITE_ACCESS,
    )
    IOCTL_ACPI_RELEASE_GLOBAL_LOCK = CTL_CODE(
        FILE_DEVICE_ACPI,
        5,
        METHOD_BUFFERED,
        FILE_READ_ACCESS | FILE_WRITE_ACCESS,
    )
    IOCTL_ACPI_EVAL_METHOD = IOCTL_ACPI_EVAL_METHOD_V1
    IOCTL_ACPI_ASYNC_EVAL_METHOD = IOCTL_ACPI_ASYNC_EVAL_METHOD_V1

    if NTDDI_VERSION >= NTDDI_VISTA:
        IOCTL_ACPI_EVAL_METHOD_V1_EX = CTL_CODE(
            FILE_DEVICE_ACPI,
            6,
            METHOD_BUFFERED,
            FILE_READ_ACCESS | FILE_WRITE_ACCESS,
        )
        IOCTL_ACPI_ASYNC_EVAL_METHOD_V1_EX = CTL_CODE(
            FILE_DEVICE_ACPI,
            7,
            METHOD_BUFFERED,
            FILE_READ_ACCESS | FILE_WRITE_ACCESS,
        )
        IOCTL_ACPI_ENUM_CHILDREN = CTL_CODE(
            FILE_DEVICE_ACPI,
            8,
            METHOD_BUFFERED,
            FILE_READ_ACCESS | FILE_WRITE_ACCESS,
        )
        IOCTL_ACPI_EVAL_METHOD_EX = IOCTL_ACPI_EVAL_METHOD_V1_EX
        IOCTL_ACPI_ASYNC_EVAL_METHOD_EX = IOCTL_ACPI_ASYNC_EVAL_METHOD_V1_EX
    # END IF

    # Windows8+ only IOCTLs.
    if NTDDI_VERSION >= NTDDI_WIN8:
        IOCTL_ACPI_GET_DEVICE_INFORMATION = CTL_CODE(
            FILE_DEVICE_ACPI,
            10,
            METHOD_BUFFERED,
            FILE_READ_ACCESS | FILE_WRITE_ACCESS,
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        IOCTL_ACPI_GET_DEVICE_SPECIFIC_DATA = CTL_CODE(
            FILE_DEVICE_ACPI,
            14,
            METHOD_BUFFERED,
            FILE_READ_ACCESS | FILE_WRITE_ACCESS,
        )
    # END IF

    # V2 ACPI IOCTLs.
    if NTDDI_VERSION >= NTDDI_WIN10_RS2:
        IOCTL_ACPI_EVAL_METHOD_V2 = CTL_CODE(
            FILE_DEVICE_ACPI,
            15,
            METHOD_BUFFERED,
            FILE_READ_ACCESS | FILE_WRITE_ACCESS,
        )
        IOCTL_ACPI_ASYNC_EVAL_METHOD_V2 = CTL_CODE(
            FILE_DEVICE_ACPI,
            16,
            METHOD_BUFFERED,
            FILE_READ_ACCESS | FILE_WRITE_ACCESS,
        )
        IOCTL_ACPI_EVAL_METHOD_V2_EX = CTL_CODE(
            FILE_DEVICE_ACPI,
            17,
            METHOD_BUFFERED,
            FILE_READ_ACCESS | FILE_WRITE_ACCESS,
        )
        IOCTL_ACPI_ASYNC_EVAL_METHOD_V2_EX = CTL_CODE(
            FILE_DEVICE_ACPI,
            18,
            METHOD_BUFFERED,
            FILE_READ_ACCESS | FILE_WRITE_ACCESS,
        )

    # END IF
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - V1 Data
    # Structures - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Data structures used for IOCTL_ACPI_ASYNC_EVAL_METHOD_V1 and
    # IOCTL_ACPI_EVAL_METHOD_V1
    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('MethodName', UCHAR * 4),
        ('MethodNameAsUlong', ULONG),
    ]
    _ACPI_EVAL_INPUT_BUFFER_V1.DUMMYUNIONNAME = DUMMYUNIONNAME

    _ACPI_EVAL_INPUT_BUFFER_V1._fields_ = [
        ('Signature', ULONG),
        ('DUMMYUNIONNAME', _ACPI_EVAL_INPUT_BUFFER_V1.DUMMYUNIONNAME),
    ]


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('MethodName', UCHAR * 4),
        ('MethodNameAsUlong', ULONG),
    ]
    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1.DUMMYUNIONNAME = DUMMYUNIONNAME

    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1._fields_ = [
        ('Signature', ULONG),
        ('DUMMYUNIONNAME', _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1.DUMMYUNIONNAME),
        ('IntegerArgument', ULONG),
    ]


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('MethodName', UCHAR * 4),
        ('MethodNameAsUlong', ULONG),
    ]
    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1.DUMMYUNIONNAME = DUMMYUNIONNAME

    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1._fields_ = [
        ('Signature', ULONG),
        ('DUMMYUNIONNAME', _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1.DUMMYUNIONNAME),
        ('StringLength', ULONG),
        ('String', UCHAR * ANYSIZE_ARRAY),
    ]


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('Argument', ULONG),
        ('Data', UCHAR * ANYSIZE_ARRAY),
    ]
    _ACPI_METHOD_ARGUMENT_V1.DUMMYUNIONNAME = DUMMYUNIONNAME

    _ACPI_METHOD_ARGUMENT_V1._fields_ = [
        ('Type', USHORT),
        ('DataLength', USHORT),
        ('DUMMYUNIONNAME', _ACPI_METHOD_ARGUMENT_V1.DUMMYUNIONNAME),
    ]


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('MethodName', UCHAR * 4),
        ('MethodNameAsUlong', ULONG),
    ]
    _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1.DUMMYUNIONNAME = DUMMYUNIONNAME

    _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1._fields_ = [
        ('Signature', ULONG),
        ('DUMMYUNIONNAME', _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1.DUMMYUNIONNAME),
        ('Size', ULONG),
        ('ArgumentCount', ULONG),
        ('Argument', ACPI_METHOD_ARGUMENT_V1 * ANYSIZE_ARRAY),
    ]

    _ACPI_EVAL_OUTPUT_BUFFER_V1._fields_ = [
        ('Signature', ULONG),
        ('Length', ULONG),
        ('Count', ULONG),
        ('Argument', ACPI_METHOD_ARGUMENT_V1 * ANYSIZE_ARRAY),
    ]

    # Data structure used for IOCTL_ACPI_ASYNC_EVAL_METHOD_V1_EX,
    # IOCTL_ACPI_EVAL_METHOD_V1_EX and
    _ACPI_EVAL_INPUT_BUFFER_V1_EX._fields_ = [
        ('Signature', ULONG),
        # NULL terminated name string
        ('MethodName', CHAR * 256),
    ]

    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX._fields_ = [
        ('Signature', ULONG),
        # NULL terminated name string
        ('MethodName', CHAR * 256),
        ('IntegerArgument', ULONG64),
    ]

    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1_EX._fields_ = [
        ('Signature', ULONG),
        # NULL terminated name string
        ('MethodName', CHAR * 256),
        ('StringLength', ULONG),
        ('String', UCHAR * ANYSIZE_ARRAY),
    ]

    _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX._fields_ = [
        ('Signature', ULONG),
        # NULL terminated name string
        ('MethodName', CHAR * 256),
        ('Size', ULONG),
        ('ArgumentCount', ULONG),
        ('Argument', ACPI_METHOD_ARGUMENT_V1 * ANYSIZE_ARRAY),
    ]

    # Define ACPI_METHOD_ARGUMENT structure as V1 for DDKVERSION <
    # NTDDI_WIN10_RS2
    ACPI_METHOD_ARGUMENT = _ACPI_METHOD_ARGUMENT_V1
    PACPI_METHOD_ARGUMENT = POINTER(_ACPI_METHOD_ARGUMENT_V1)

    # Define ACPI_EVAL_INPUT_BUFFER structure as V1 for DDKVERSION <
    # NTDDI_WIN10_RS2
    ACPI_EVAL_INPUT_BUFFER = _ACPI_EVAL_INPUT_BUFFER_V1
    PACPI_EVAL_INPUT_BUFFER = POINTER(_ACPI_EVAL_INPUT_BUFFER_V1)

    ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1
    PACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1)

    ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1
    PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1)

    ACPI_EVAL_INPUT_BUFFER_COMPLEX = _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1
    PACPI_EVAL_INPUT_BUFFER_COMPLEX = POINTER(_ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1)

    # Define ACPI_EVAL_INPUT_BUFFER_EX structure as V1 for DDKVERSION <
    # NTDDI_WIN10_RS2
    ACPI_EVAL_INPUT_BUFFER_EX = _ACPI_EVAL_INPUT_BUFFER_V1_EX
    PACPI_EVAL_INPUT_BUFFER_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_V1_EX)

    ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_EX = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX
    PACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX)

    ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_EX = _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1_EX
    PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1_EX)

    ACPI_EVAL_INPUT_BUFFER_COMPLEX_EX = _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX
    PACPI_EVAL_INPUT_BUFFER_COMPLEX_EX = POINTER(_ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX)

    # Define ACPI_EVAL_OUTPUT_BUFFER structure as V1 for DDKVERSION <
    # NTDDI_WIN10_RS2
    ACPI_EVAL_OUTPUT_BUFFER = _ACPI_EVAL_OUTPUT_BUFFER_V1

    PACPI_EVAL_OUTPUT_BUFFER = POINTER(_ACPI_EVAL_OUTPUT_BUFFER_V1)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - V1 Macros
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def ACPI_METHOD_ARGUMENT_LENGTH(DataLength):
        return (
            FIELD_OFFSET(ACPI_METHOD_ARGUMENT, 'Data') +
            max(ctypes.sizeof(ULONG), DataLength)
        )


    def ACPI_METHOD_ARGUMENT_LENGTH_FROM_ARGUMENT(Argument):
        return (
            ACPI_METHOD_ARGUMENT_LENGTH(PACPI_METHOD_ARGUMENT(Argument).DataLength)
        )


    def ACPI_METHOD_NEXT_ARGUMENT(Argument):
        return PACPI_METHOD_ARGUMENT(
            PUCHAR(Argument) + ACPI_METHOD_ARGUMENT_LENGTH_FROM_ARGUMENT(Argument)
        )


    def ACPI_METHOD_SET_ARGUMENT_INTEGER(MethodArgument, IntData):
        MethodArgument.Type = ACPI_METHOD_ARGUMENT_INTEGER
        MethodArgument.DataLength = ctypes.sizeof(ULONG)
        MethodArgument.Argument = IntData
        return MethodArgument


    def ACPI_METHOD_SET_ARGUMENT_STRING(Argument, StrData):
        Argument.Type = ACPI_METHOD_ARGUMENT_STRING
        Argument.DataLength = strlen(StrData) + ctypes.sizeof(UCHAR)
        memcpy_s(
            ctypes.byref(Argument.Data[0]),
            Argument.DataLength,
            StrData,
            Argument.DataLength
        )

        return Argument


    def ACPI_METHOD_SET_ARGUMENT_BUFFER(Argument, BuffData, BuffLength):
        Argument.Type = ACPI_METHOD_ARGUMENT_BUFFER
        Argument.DataLength = BuffLength
        memcpy_s(
            ctypes.byref(Argument.Data[0]),
            Argument.DataLength,
            BuffData,
            BuffLength
        )
        return Argument


    def ACPI_EVAL_OUTPUT_BUFFER_ARGUMENT_LENGTH(EvalOutputBuffer):
        return (
            EvalOutputBuffer.Length -
            FIELD_OFFSET(ACPI_EVAL_OUTPUT_BUFFER, 'Argument')
        )


    def ACPI_EVAL_OUTPUT_BUFFER_ARGUMENTS_BEGIN(EvalOutputBuffer):
        return PACPI_METHOD_ARGUMENT(EvalOutputBuffer).Argument


    def ACPI_EVAL_OUTPUT_BUFFER_ARGUMENTS_END(EvalOutputBuffer):
        return PACPI_METHOD_ARGUMENT(
            EvalOutputBuffer.Argument +
            ACPI_EVAL_OUTPUT_BUFFER_ARGUMENT_LENGTH(EvalOutputBuffer)
        )


    def FOR_EACH_ACPI_METHOD_ARGUMENT(
        MethodArgument,
        MethodArgumentsBegin,
        MethodArgumentsEnd
    ):
        MethodArgument = MethodArgumentsBegin

        while MethodArgument < MethodArgumentsEnd:
            MethodArgument = ACPI_METHOD_NEXT_ARGUMENT(MethodArgument)

        return MethodArgument


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - V2 Data
    # Structures - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Data structures used for IOCTL_ACPI_ASYNC_EVAL_METHOD_V2 and
    # IOCTL_ACPI_EVAL_METHOD_V2
    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('MethodName', UCHAR * 4),
        ('MethodNameAsUlong', ULONG),
    ]
    _ACPI_EVAL_INPUT_BUFFER_V2.DUMMYUNIONNAME = DUMMYUNIONNAME

    _ACPI_EVAL_INPUT_BUFFER_V2._fields_ = [
        ('Signature', ULONG),
        ('DUMMYUNIONNAME', _ACPI_EVAL_INPUT_BUFFER_V2.DUMMYUNIONNAME),
    ]


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('MethodName', UCHAR * 4),
        ('MethodNameAsUlong', ULONG),
    ]
    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2.DUMMYUNIONNAME = DUMMYUNIONNAME


    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2._fields_ = [
        ('Signature', ULONG),
        ('DUMMYUNIONNAME', _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2.DUMMYUNIONNAME),
        ('IntegerArgument', ULONG),
    ]


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('MethodName', UCHAR * 4),
        ('MethodNameAsUlong', ULONG),
    ]
    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2.DUMMYUNIONNAME = DUMMYUNIONNAME


    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2._fields_ = [
        ('Signature', ULONG),
        ('DUMMYUNIONNAME', _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2.DUMMYUNIONNAME),
        ('StringLength', ULONG),
        ('String', UCHAR * ANYSIZE_ARRAY),
    ]


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('Argument', ULONG),
        ('Data', UCHAR * ANYSIZE_ARRAY),
    ]
    _ACPI_METHOD_ARGUMENT_V2.DUMMYUNIONNAME = DUMMYUNIONNAME


    _ACPI_METHOD_ARGUMENT_V2._fields_ = [
        ('Type', USHORT),
        ('DataLength', ULONG),
        ('DUMMYUNIONNAME', _ACPI_METHOD_ARGUMENT_V2.DUMMYUNIONNAME),
    ]


    class DUMMYUNIONNAME(ctypes.Union):
        pass


    DUMMYUNIONNAME._fields_ = [
        ('MethodName', UCHAR * 4),
        ('MethodNameAsUlong', ULONG),
    ]
    _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2.DUMMYUNIONNAME = DUMMYUNIONNAME


    _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2._fields_ = [
        ('Signature', ULONG),
        ('DUMMYUNIONNAME', _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2.DUMMYUNIONNAME),
        ('Size', ULONG),
        ('ArgumentCount', ULONG),
        ('Argument', ACPI_METHOD_ARGUMENT_V2 * ANYSIZE_ARRAY),
    ]

    _ACPI_EVAL_OUTPUT_BUFFER_V2._fields_ = [
        ('Signature', ULONG),
        ('Length', ULONG),
        ('Count', ULONG),
        ('Argument', ACPI_METHOD_ARGUMENT_V2 * ANYSIZE_ARRAY),
    ]


    # Data structure used for IOCTL_ACPI_ASYNC_EVAL_METHOD_V2_EX,
    # IOCTL_ACPI_EVAL_METHOD_V2_EX and
    _ACPI_EVAL_INPUT_BUFFER_V2_EX._fields_ = [
        ('Signature', ULONG),
        # NULL terminated name string
        ('MethodName', CHAR * 256),
    ]

    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2_EX._fields_ = [
        ('Signature', ULONG),
        # NULL terminated name string
        ('MethodName', CHAR * 256),
        ('IntegerArgument', ULONG64),
    ]

    _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2_EX._fields_ = [
        ('Signature', ULONG),
        # NULL terminated name string
        ('MethodName', CHAR * 256),
        ('StringLength', ULONG),
        ('String', UCHAR * ANYSIZE_ARRAY),
    ]

    PACPI_METHOD_ARGUMENT_V2 = POINTER(ACPI_METHOD_ARGUMENT_V2)

    _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX._fields_ = [
        ('Signature', ULONG),
        # NULL terminated name string
        ('MethodName', CHAR * 256),
        ('Size', ULONG),
        ('ArgumentCount', ULONG),
        ('Argument', ACPI_METHOD_ARGUMENT_V2 * ANYSIZE_ARRAY),
    ]


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - V2 Macros
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def ACPI_METHOD_ARGUMENT_V2_LENGTH(DataLength):
        return (
            FIELD_OFFSET(ACPI_METHOD_ARGUMENT_V2, 'Data') +
            max(ctypes.sizeof(ULONG), DataLength)
        )


    def ACPI_METHOD_ARGUMENT_V2_LENGTH_FROM_ARGUMENT(Argument):
        return (
            ACPI_METHOD_ARGUMENT_V2_LENGTH(
                PACPI_METHOD_ARGUMENT_V2(Argument).DataLength)
        )


    def ACPI_METHOD_NEXT_ARGUMENT_V2(Argument):
        return PACPI_METHOD_ARGUMENT_V2(
            Argument +
            ACPI_METHOD_ARGUMENT_V2_LENGTH_FROM_ARGUMENT(Argument)
        )


    def ACPI_METHOD_SET_ARGUMENT_INTEGER_V2(MethodArgument, IntData):
        MethodArgument.Type = ACPI_METHOD_ARGUMENT_INTEGER
        MethodArgument.DataLength = ctypes.sizeof(ULONG)
        MethodArgument.Argument = IntData
        return MethodArgument

    def ACPI_METHOD_SET_ARGUMENT_STRING_V2(Argument, StrData):
        Argument.Type = ACPI_METHOD_ARGUMENT_STRING
        Argument.DataLength = strlen(StrData) + ctypes.sizeof(UCHAR)

        memcpy_s(
            ctypes.byref(Argument.Data[0]),
            Argument.DataLength,
            StrData,
            Argument.DataLength
        )
        return Argument


    def ACPI_METHOD_SET_ARGUMENT_BUFFER_V2(Argument, BuffData, BuffLength):
        Argument.Type = ACPI_METHOD_ARGUMENT_BUFFER
        Argument.DataLength = BuffLength
        memcpy_s(
            ctypes.byref(Argument.Data[0]),
            Argument.DataLength,
            BuffData,
            BuffLength
        )

        return Argument


    def ACPI_EVAL_OUTPUT_BUFFER_V2_ARGUMENT_LENGTH(EvalOutputBuffer):
        return (
            EvalOutputBuffer.Length -
            FIELD_OFFSET(ACPI_EVAL_OUTPUT_BUFFER_V2, 'Argument')
        )


    def ACPI_EVAL_OUTPUT_BUFFER_V2_ARGUMENTS_BEGIN(EvalOutputBuffer):
        return PACPI_METHOD_ARGUMENT_V2(EvalOutputBuffer.Argument)


    def ACPI_EVAL_OUTPUT_BUFFER_V2_ARGUMENTS_END(EvalOutputBuffer):
        return PACPI_METHOD_ARGUMENT_V2(
            EvalOutputBuffer.Argument +
            ACPI_EVAL_OUTPUT_BUFFER_V2_ARGUMENT_LENGTH(EvalOutputBuffer)
        )

    def FOR_EACH_ACPI_METHOD_ARGUMENT_V2(MethodArgument, MethodArgumentsBegin, MethodArgumentsEnd):
        MethodArgument = MethodArgumentsBegin

        while MethodArgument < MethodArgumentsEnd:
            MethodArgument = ACPI_METHOD_NEXT_ARGUMENT_V2(MethodArgument)

        return MethodArgument



    ACPI_EVAL_INPUT_BUFFER_SIGNATURE_V1 = 'BieA'
    ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_SIGNATURE_V1 = 'IieA'
    ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_SIGNATURE_V1 = 'SieA'
    ACPI_EVAL_INPUT_BUFFER_COMPLEX_SIGNATURE_V1 = 'CieA'
    ACPI_EVAL_OUTPUT_BUFFER_SIGNATURE_V1 = 'BoeA'
    ACPI_EVAL_INPUT_BUFFER_SIGNATURE = ACPI_EVAL_INPUT_BUFFER_SIGNATURE_V1
    ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_SIGNATURE = (
        ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_SIGNATURE_V1
    )
    ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_SIGNATURE = (
        ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_SIGNATURE_V1
    )
    ACPI_EVAL_INPUT_BUFFER_COMPLEX_SIGNATURE = (
        ACPI_EVAL_INPUT_BUFFER_COMPLEX_SIGNATURE_V1
    )
    ACPI_EVAL_OUTPUT_BUFFER_SIGNATURE = ACPI_EVAL_OUTPUT_BUFFER_SIGNATURE_V1
    if NTDDI_VERSION >= NTDDI_VISTA:
        ACPI_EVAL_INPUT_BUFFER_SIGNATURE_V1_EX = 'AieA'
        ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_SIGNATURE_V1_EX = 'DieA'
        ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_SIGNATURE_V1_EX = 'EieA'
        ACPI_EVAL_INPUT_BUFFER_COMPLEX_SIGNATURE_V1_EX = 'FieA'
        ACPI_ENUM_CHILDREN_OUTPUT_BUFFER_SIGNATURE = 'GieA'
        ACPI_ENUM_CHILDREN_INPUT_BUFFER_SIGNATURE = 'HieA'
        ACPI_EVAL_INPUT_BUFFER_SIGNATURE_EX = (
            ACPI_EVAL_INPUT_BUFFER_SIGNATURE_V1_EX
        )
        ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_SIGNATURE_EX = (
            ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_SIGNATURE_V1_EX
        )
        ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_SIGNATURE_EX = (
            ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_SIGNATURE_V1_EX
        )
        ACPI_EVAL_INPUT_BUFFER_COMPLEX_SIGNATURE_EX = (
            ACPI_EVAL_INPUT_BUFFER_COMPLEX_SIGNATURE_V1_EX
        )
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN7:
        IOCTL_ACPI_GET_DEVICE_INFORMATION_SIGNATURE = 'JieA'
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN10_RS1:
        IOCTL_ACPI_GET_DEVICE_SPECIFIC_DATA_SIGNATURE = 'HieA'
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN10_RS2:
        ACPI_EVAL_INPUT_BUFFER_SIGNATURE_V2 = 'KieA'
        ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_SIGNATURE_V2 = 'LieA'
        ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_SIGNATURE_V2 = 'MieA'
        ACPI_EVAL_INPUT_BUFFER_COMPLEX_SIGNATURE_V2 = 'NieA'
        ACPI_EVAL_INPUT_BUFFER_SIGNATURE_V2_EX = 'OieA'
        ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_SIGNATURE_V2_EX = 'PieA'
        ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_SIGNATURE_V2_EX = 'QieA'
        ACPI_EVAL_INPUT_BUFFER_COMPLEX_SIGNATURE_V2_EX = 'RieA'
        ACPI_EVAL_OUTPUT_BUFFER_SIGNATURE_V2 = 'KoeA'
    # END IF

    ACPI_METHOD_ARGUMENT_INTEGER = 0x0
    ACPI_METHOD_ARGUMENT_STRING = 0x1
    ACPI_METHOD_ARGUMENT_BUFFER = 0x2
    ACPI_METHOD_ARGUMENT_PACKAGE = 0x3
    ACPI_METHOD_ARGUMENT_PACKAGE_EX = 0x4


    # Data structures used for IOCTL_ACPI_ACQUIRE_GLOBAL_LOCK
    # IOCTL_ACPI_RELEASE_GLOBAL_LOCK
    _ACPI_MANIPULATE_GLOBAL_LOCK_BUFFER._fields_ = [
        ('Signature', ULONG),
        ('LockObject', PVOID),
    ]
    ACPI_ACQUIRE_GLOBAL_LOCK_SIGNATURE = 'LgaA'
    ACPI_RELEASE_GLOBAL_LOCK_SIGNATURE = 'LgrA'


    # IOCTL_ACPI_ENUM_CHILDREN
    _ACPI_ENUM_CHILDREN_INPUT_BUFFER._fields_ = [
        ('Signature', ULONG),
        ('Flags', ULONG),
        ('NameLength', ULONG),
        ('Name', CHAR * ANYSIZE_ARRAY),
    ]


    # Enum child structures.
    _ACPI_ENUM_CHILD._fields_ = [
        ('Flags', ULONG),
        # length including null terminator
        ('NameLength', ULONG),
        ('Name', CHAR * ANYSIZE_ARRAY),
    ]

    _ACPI_ENUM_CHILDREN_OUTPUT_BUFFER._fields_ = [
        ('Signature', ULONG),
        ('NumberOfChildren', ULONG),
        ('Children', ACPI_ENUM_CHILD * ANYSIZE_ARRAY),
    ]


    def ACPI_ENUM_CHILD_LENGTH_FROM_CHILD(Child):
        return (2 * ctypes.sizeof(ULONG)) + Child.NameLength


    def ACPI_ENUM_CHILD_NEXT(Child):
        return PACPI_ENUM_CHILD(
            Child + ACPI_ENUM_CHILD_LENGTH_FROM_CHILD(Child)
        )


    _ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER._fields_ = [
        ('Signature', ULONG),
        ('Size', USHORT),
        ('Revision', UCHAR),
        ('Reserved0', UCHAR),
        # Vendor and device strings.
        ('VendorIdStringOffset', USHORT),
        ('VendorStringLength', USHORT),
        ('DeviceIdStringOffset', USHORT),
        # Sub system and sub device strings.
        ('SubSystemIdStringOffset', USHORT),
        ('SubSystemStringLength', USHORT),
        ('SubDeviceIdStringOffset', USHORT),
        # Instance string.
        ('InstanceIdLength', USHORT),
        ('InstanceIdOffset', USHORT),
        # Classcodes hardware revision and programming interface.
        ('BaseClassCode', USHORT),
        ('HardwareRevision', USHORT),
        ('ProgrammingInterface', UCHAR),
        ('Reserved1', UCHAR),
        ('SubClassCode', USHORT),
    ]

    # valid flags for ACPI_ENUM_CHILDREN_INPUT_BUFFER.Flags
    ENUM_CHILDREN_IMMEDIATE_ONLY = 0x1
    ENUM_CHILDREN_MULTILEVEL = 0x2
    ENUM_CHILDREN_NAME_IS_FILTER = 0x4

    # valid flags for ACPI_ENUM_CHILD
    ACPI_OBJECT_HAS_CHILDREN = 0x1

    # INTERNAL - ONLY DEFINITION SECTION.
    # Input buffer for the IOCTL_ACPI_GET_DEVICE_SPECIFIC_DATA.
    _ACPI_GET_DEVICE_SPECIFIC_DATA._fields_ = [
        ('Signature', ULONG),
        ('Section', GUID),
        ('PropertyNameLength', ULONG),
        ('PropertyName', UCHAR * ANYSIZE_ARRAY),
    ]
    if defined(_MSC_VER) and _MSC_VER >= 1020:
        pass
    # END IF
# END IF
