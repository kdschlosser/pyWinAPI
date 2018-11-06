

from wtypes_h import (
    ENUM,
)
import ntdef_h


def _SAL_L_Source_(Name, args, annotes):
    return _SA_annotes3SAL_name, #Name, "", "2" _Group_annotes _SAL_nop_impl_\n"


def _SAL_L_Source_(Name, args, annotes):
    return _SA_annotes3SAL_name, #Name, "", "2" _GrouP_annotes _SAL_nop_impl_\n"
from sal_h import * # NOQA
__SAL_H_FULL_VER = 0x08590127
__inner_bound = _SAL_L_Source_(__inner_bound, (), _SA_annotes0(SAL_bound))


def __inner_range(lb, ub):
    return _SAL_L_Source_(__inner_range, lb,ub, _SA_annotes2SAL_range,lb,ub)
__inner_assume_bound_dec = (
    __inline __nothrow VOID __AssumeBoundInt(_Post_ __inner_bound INT i) [i;]
)


def __inner_assume_bound(i):
    return __AssumeBoundInti;
__inner_allocator = _SAL_L_Source_(
    __inner_allocater,
    (),
    _SA_annotes0(SAL_allocator),
)


def __static_context(ctx, annotes):
    return _SAL_L_Source_(__static_context, ctx, annotes, _SA_annotes1SAL_context,ctx _Group_(__nop_implannotes))


def __failure(x):
    return __static_context(SAL_return_convention, _SAL_L_Source_(__failure, x, _SA_annotes1SAL_failure,x))
__valueUnd = _SAL_L_Source_(__valueUnd, (), _SA_annotes0(SAL_valueUnd))
= 0, __failureUndefined = 1} = __SAL_failureKind{__failureUnspecified


def __failureDefault(kind):
    return _SAL_L_Source_(__failureDefault, kind, __static_context(SAL_return_convention, _SA_annotes1SAL_failureDefault,kind))



def __xcount(size):
    return _SAL1_Source_(__xcount, size, __notnull __inexpressible_writableTosize)


def __in_xcount(size):
    return _SAL1_Source_(__in_xcount, size, __in _Pre_ __inexpressible_readableTosize)


def __out_xcount(size):
    return _SAL1_Source_(__out_xcount, size, __xcountsize _Post_ __valid __refparam)


def __out_xcount_part(size, length):
    return _SAL1_Source_(__out_xcount_part_, size,length, __out_xcountsize _Post_ __inexpressible_readableTolength)


def __out_xcount_full(size):
    return _SAL1_Source_(__out_xcount_full, size, __out_xcount_partsize,size)


def __inout_xcount(size):
    return _SAL1_Source_(__inout_xcount, size, __out_xcountsize _Pre_ __valid)


def __inout_xcount_part(size, length):
    return _SAL1_Source_(__inout_xcount_part, size,length, __out_xcount_partsize,length _Pre_ __valid _Pre_ __inexpressible_readableTolength)


def __inout_xcount_full(size):
    return _SAL1_Source_(__inout_xcount_full, size, __inout_xcount_partsize,size)


def __xcount_opt(size):
    return _SAL1_Source_(__xcount_opt, size, __xcountsize __exceptthat __maybenull)


def __in_xcount_opt(size):
    return _SAL1_Source_(__in_xcount_opt, size, __in_xcountsize __exceptthat __maybenull)


def __out_xcount_opt(size):
    return _SAL1_Source_(__out_xcount_opt, size, __out_xcountsize __exceptthat __maybenull)


def __out_xcount_part_opt(size, length):
    return _SAL1_Source_(__out_xcount_part_opt, size,length, __out_xcount_partsize,length __exceptthat __maybenull)


def __out_xcount_full_opt(size):
    return _SAL1_Source_(__out_xcount_full_opt, size, __out_xcount_fullsize __exceptthat __maybenull)


def __inout_xcount_opt(size):
    return _SAL1_Source_(__inout_xcount_opt, size, __inout_xcountsize __exceptthat __maybenull)


def __inout_xcount_part_opt(size, length):
    return _SAL1_Source_(__inout_xcount_part_opt, size, length, __inout_xcount_partsize,length __exceptthat __maybenull)


def __inout_xcount_full_opt(size):
    return _SAL1_Source_(__inout_xcount_full_opt, size, __inout_xcount_fullsize __exceptthat __maybenull)


def __deref_xcount(size):
    return _SAL1_Source_(__deref_xcount, size, __ecount1 _Post_ __elem_readableTo1 _Post_ __deref __notnull _Post_ __deref __inexpressible_writableTosize)
__deref_in = _SAL1_Source_(
    __deref_in,
    (),
    __in _Pre_ __deref __deref __readonly,
)


def __deref_in_ecount(size):
    return _SAL1_Source_(__deref_in_ecount, size, __deref_in _Pre_ __deref __elem_readableTosize)


def __deref_in_bcount(size):
    return _SAL1_Source_(__deref_in_bcount, size, __deref_in _Pre_ __deref __byte_readableTosize)


def __deref_in_xcount(size):
    return _SAL1_Source_(__deref_in_xcount, size, __deref_in _Pre_ __deref __inexpressible_readableTosize)


def __deref_out_xcount(size):
    return _SAL1_Source_(__deref_out_xcount, size, __deref_xcountsize _Post_ __deref __valid __refparam)


def __deref_out_xcount_part(size, length):
    return _SAL1_Source_(__deref_out_xcount_part, size,length, __deref_out_xcountsize _Post_ __deref __inexpressible_readableTolength)


def __deref_out_xcount_full(size):
    return _SAL1_Source_(__deref_out_xcount_full, size, __deref_out_xcount_partsize,size)


def __deref_out_xcount(size):
    return _SAL1_Source_(__deref_out_xcount, size, __deref_xcountsize _Post_ __deref __valid __refparam)


def __inout_xcount_opt(size):
    return _SAL1_Source_(__inout_xcount_opt, size, __inout_xcountsize __exceptthat __maybenull)


def __deref_xcount(size):
    return _SAL1_Source_(__deref_xcount, size, __ecount1 _Post_ __elem_readableTo1 _Post_ __deref __notnull _Post_ __deref __inexpressible_writableTosize)
__deref_in = _SAL1_Source_(
    __deref_in,
    (),
    __in _Pre_ __deref __deref __readonly,
)


def __deref_in_ecount(size):
    return _SAL1_Source_(__deref_in_ecount, size, __deref_in _Pre_ __deref __elem_readableTosize)


def __deref_in_bcount(size):
    return _SAL1_Source_(__deref_in_bcount, size, __deref_in _Pre_ __deref __byte_readableTosize)


def __deref_in_xcount(size):
    return _SAL1_Source_(__deref_in_xcount, size, __deref_in _Pre_ __deref __inexpressible_readableTosize)


def __deref_out_xcount(size):
    return _SAL1_Source_(__deref_out_xcount, size, __deref_xcountsize _Post_ __deref __valid __refparam)


def __deref_out_xcount_part(size, length):
    return _SAL1_Source_(__deref_out_xcount_part, size,length, __deref_out_xcountsize _Post_ __deref __inexpressible_readableTolength)


def __deref_out_xcount_full(size):
    return _SAL1_Source_(__deref_out_xcount_full, size, __deref_out_xcount_partsize,size)


def __deref_out_xcount(size):
    return _SAL1_Source_(__deref_out_xcount, size, __deref_xcountsize _Post_ __deref __valid __refparam)


def __deref_inout_xcount(size):
    return _SAL1_Source_(__deref_inout_xcount, size, __deref_inout _Pre_ __deref __inexpressible_writableTosize _Post_ __deref __inexpressible_writableTosize)


def __deref_inout_xcount_part(size, length):
    return _SAL1_Source_(__deref_inout_xcount_part, size,length, __deref_inout_xcountsize _Pre_ __deref __inexpressible_readableTolength _Post_ __deref __inexpressible_readableTolength)


def __deref_inout_xcount_full(size):
    return _SAL1_Source_(__deref_inout_xcount_full, size, __deref_inout_xcount_partsize,size)


def __deref_xcount_opt(size):
    return _SAL1_Source_(__deref_xcount_opt, size, __deref_xcountsize _Post_ __deref __exceptthat __maybenull)
__deref_in_opt = _SAL1_Source_(
    __deref_in_opt,
    (),
    __deref_in                                  _Pre_ __deref __exceptthat __maybenull,
)
__deref_in_opt_out = _SAL1_Source_(
    __deref_in_opt_out,
    (),
    __deref_inout                               _Pre_ __deref __exceptthat __maybenull  _Post_ __deref __notnull,
)


def __deref_in_ecount_opt(size):
    return _SAL1_Source_(__deref_in_ecount_opt, size, __deref_in_ecountsize _Pre_ __deref __exceptthat __maybenull)


def __deref_in_bcount_opt(size):
    return _SAL1_Source_(__deref_in_bcount_opt_, size, __deref_in_bcountsize _Pre_ __deref __exceptthat __maybenull)


def __deref_in_xcount_opt(size):
    return _SAL1_Source_(__deref_in_xcount_opt, size, __deref_in_xcountsize _Pre_ __deref __exceptthat __maybenull)


def __deref_out_xcount_opt(size):
    return _SAL1_Source_(__deref_out_xcount_opt, size, __deref_out_xcountsize _Post_ __deref __exceptthat __maybenull)


def __deref_out_xcount_part_opt(size, length):
    return _SAL1_Source_(__deref_out_xcount_part_opt, size,length, __deref_out_xcount_partsize,length _Post_ __deref __exceptthat __maybenull)


def __deref_out_xcount_full_opt(size):
    return _SAL1_Source_(__deref_out_xcount_full_opt, size, __deref_out_xcount_fullsize _Post_ __deref __exceptthat __maybenull)


def __deref_inout_xcount_opt(size):
    return _SAL1_Source_(__deref_inout_xcount_opt, size, __deref_inout_xcountsize _Pre_ __deref __exceptthat __maybenull _Post_ __deref __exceptthat __maybenull)


def __deref_inout_xcount_part_opt(size, length):
    return _SAL1_Source_(__deref_inout_xcount_part_opt, size,length, __deref_inout_xcount_partsize,length _Pre_ __deref __exceptthat __maybenull _Post_ __deref __exceptthat __maybenull)


def __deref_inout_xcount_full_opt(size):
    return _SAL1_Source_(__deref_inout_xcount_full_opt, size, __deref_inout_xcount_fullsize _Pre_ __deref __exceptthat __maybenull _Post_ __deref __exceptthat __maybenull)


def __deref_opt_xcount(size):
    return _SAL1_Source_(__deref_opt_xcount, size, __deref_xcountsize __exceptthat __maybenull)
__deref_opt_in = _SAL1_Source_(
    __deref_opt_in,
    (),
    __deref_in                                  __exceptthat __maybenull,
)


def __deref_opt_in_ecount(size):
    return _SAL1_Source_(__deref_opt_in_ecount, size, __deref_in_ecountsize __exceptthat __maybenull)


def __deref_opt_in_bcount(size):
    return _SAL1_Source_(__deref_opt_in_bcount, size, __deref_in_bcountsize __exceptthat __maybenull)


def __deref_opt_in_xcount(size):
    return _SAL1_Source_(__deref_opt_in_xcount, size, __deref_in_xcountsize __exceptthat __maybenull)


def __deref_opt_out_xcount(size):
    return _SAL1_Source_(__deref_opt_out_xcount, size, __deref_out_xcountsize __exceptthat __maybenull)


def __deref_opt_out_xcount_part(size, length):
    return _SAL1_Source_(__deref_opt_out_xcount_part, size,length, __deref_out_xcount_partsize,length __exceptthat __maybenull)


def __deref_opt_out_xcount_full(size):
    return _SAL1_Source_(__deref_opt_out_xcount_full, size, __deref_out_xcount_fullsize __exceptthat __maybenull)


def __deref_opt_inout_xcount(size):
    return _SAL1_Source_(__deref_opt_inout_xcount, size, __deref_inout_xcountsize __exceptthat __maybenull)


def __deref_opt_inout_xcount_part(size, length):
    return _SAL1_Source_(__deref_opt_inout_xcount_part, size,length, __deref_inout_xcount_partsize,length __exceptthat __maybenull)


def __deref_opt_inout_xcount_full(size):
    return _SAL1_Source_(__deref_opt_inout_xcount_full, size, __deref_inout_xcount_fullsize __exceptthat __maybenull)


def __deref_opt_xcount_opt(size):
    return _SAL1_Source_(__deref_opt_xcount_opt, size, __deref_xcount_optsize __exceptthat __maybenull)
__deref_opt_in_opt = _SAL1_Source_(
    __deref_opt_in_opt,
    (),
    __deref_in_opt                              __exceptthat __maybenull,
)


def __deref_opt_in_ecount_opt(size):
    return _SAL1_Source_(__deref_opt_in_ecount_opt, size, __deref_in_ecount_optsize __exceptthat __maybenull)


def __deref_opt_in_bcount_opt(size):
    return _SAL1_Source_(__deref_opt_in_bcount_opt, size, __deref_in_bcount_optsize __exceptthat __maybenull)


def __deref_opt_in_xcount_opt(size):
    return _SAL1_Source_(__deref_opt_in_xcount_opt, size, __deref_in_xcount_optsize __exceptthat __maybenull)


def __deref_opt_out_xcount_opt(size):
    return _SAL1_Source_(__deref_opt_out_xcount_opt, size, __deref_out_xcount_optsize __exceptthat __maybenull)


def __deref_opt_out_xcount_part_opt(size, length):
    return _SAL1_Source_(__deref_opt_out_xcount_part_opt, size,length, __deref_out_xcount_part_optsize,length __exceptthat __maybenull)


def __deref_opt_out_xcount_full_opt(size):
    return _SAL1_Source_(__deref_opt_out_scount_full_opt, size, __deref_out_xcount_full_optsize __exceptthat __maybenull)


def __deref_opt_inout_xcount_opt(size):
    return _SAL1_Source_(__deref_opt_inout_xcount_opt, size, __deref_inout_xcount_optsize __exceptthat __maybenull)


def __deref_opt_inout_xcount_part_opt(size, length):
    return _SAL1_Source_(__deref_inout_xcount_part_opt(size, size,length, length) __exceptthat __maybenull)


def __deref_opt_inout_xcount_full_opt(size):
    return _SAL1_Source_(__deref_opt_inout_scount_full_opt, size, __deref_inout_xcount_full_optsize __exceptthat __maybenull)


def __deref_in_ecount_iterator(size, incr):
    return _SAL1_Source_(__deref_in_ecount_iterator, size,incr, __inout _Pre_ __deref __elem_readableTosize __deref_out_range(==, _Old_*_Curr_ + incr))


def __deref_out_ecount_iterator(size, incr):
    return _SAL1_Source_(__deref_out_ecount_iterator, size,incr, __inout _Pre_ __deref __elem_writableTosize __deref_out_range(==, _Old_*_Curr_ + incr))


def __deref_inout_ecount_iterator(size, incr):
    return _SAL1_Source_(__deref_inout_ecount_iterator, size,incr, __inout _Pre_ __deref __elem_readableTosize _Pre_ __deref __elem_writableTosize __deref_out_range(==, _Old_*_Curr_ + incr))


def __post_bcount(size):
    return _SAL1_Source_(__post_bcount, size, _Post_ __byte_writableTosize)


def __post_ecount(size):
    return _SAL1_Source_(__post_ecount, size, _Post_ __elem_writableTosize)


def __deref_realloc_bcount(insize, outsize):
    return _SAL1_Source_(__deref_realloc_bcount, insize,outsize, __inout _Pre_ __deref __byte_readableToinsize _Post_ __deref __byte_writableTooutsize)


def __in_ecount_or_z(c):
    return _SAL1_Source_(__in_ecount_or_z, c, _When_(_String_length__Curr_ < c, __in_z) _When_(_String_length__Curr_ >= c, __in_ecountc))
__nullnullterminated = (
    _SAL1_Source_(__nullnullterminated, (),  __inexpressible_readableTo("string terminated by two nulls") __nullterminated)\n"
)
__post_nullnullterminated = (
    _SAL1_Source_(__post_nullnullterminated, (),  _Post_ __inexpressible_readableTo("string terminated by two nulls") _Post_ __nullterminated)\n"
)


def __file_parser(typ):
    return _SAL_L_Source_(__file_parser, typ, _SA_annotes2SAL_file_parser,"function",typ)\n"


def __file_parser_class(typ):
    return _SAL_L_Source_(__file_parser_class, typ, _SA_annotes2SAL_file_parser,"class",typ)\n"


def __file_parser_library(typ):
    return extern INT _SAL_L_Source_(__file_parser_library, typ, _SA_annotes2SAL_file_parser, "library", typ) __iSALFileParserLibrary##typ;\n"


def __source_code_content(typ):
    return extern INT _SAL_L_Source_(__source_code_content, typ, _SA_annotes1SAL_source_code_content, typ) __iSAL_Source_Code_Content##typ;


def __class_code_content(typ):
    return _SAL_L_Source_(__class_code_content, typ, _SA_annotes1SAL_class_code_content, typ)


def __analysis_assert(e):
    return __assumee


def __analysis_hINT(hINT):
    return _SAL_L_Source_(__analysis_hINT, hINT, _SA_annotes1SAL_analysisHINT, hINT)
__analysis_noreturn = __declspec(noreturn)


def __inner_data_source(src_raw):
    return _SAL_L_Source_(__inner_data_source, src_raw, _SA_annotes1SAL_untrusted_data_source,src_raw)


def __inner_this_data_source(src_raw):
    return _SAL_L_Source_(__inner_this_data_source, src_raw, _SA_annotes1SAL_untrusted_data_source_this,src_raw)


def __inner_out_validated(typ_raw):
    return _SAL_L_Source_(__inner_out_validated, typ_raw, _Post_ _SA_annotes1SAL_validated,typ_raw)


def __inner_this_out_validated(typ_raw):
    return _SAL_L_Source_(__inner_this_out_validated, typ_raw, _SA_annotes1SAL_validated_this,typ_raw)
__inner_assume_validated_dec = (
    __inline __nothrow VOID __AssumeValidated(__inner_out_validated("BY_DESIGN") VOID *p) [p;]\n"
)


def __inner_assume_validated(p):
    return __AssumeValidatedp


def __inner_transfer(formal):
    return _SAL_L_Source_(__inner_transfer, formal, _SA_annotes1SAL_transfer_adt_property_from,formal)
__inner_encoded = _SAL_L_Source_(
    __inner_encoded,
    (),
    _SA_annotes0(SAL_encoded),
)


def __inner_adt_prop(adt, prop):
    return _SAL_L_Source_(__inner_adt_prop, adt,prop, _SA_annotes2SAL_adt, adt,prop)


def __inner_adt_add_prop(adt, prop):
    return _SAL_L_Source_(__inner_adt_add_prop, adt,prop, _SA_annotes2SAL_add_adt_property,adt,prop)


def __inner_adt_remove_prop(adt, prop):
    return _SAL_L_Source_(__inner_adt_remove_prop, adt,prop, _SA_annotes2SAL_remove_adt_property,adt,prop)


def __inner_adt_transfer_prop(arg):
    return _SAL_L_Source_(__inner_adt_trasnfer_prop, arg, _SA_annotes1SAL_transfer_adt_property_from,arg)


def __inner_adt_type_props(typ):
    return _SAL_L_Source_(__inner_adt_type_props, typ, _SA_annotes1SAL_post_type,typ)
__inner_volatile = _SAL_L_Source_(
    __inner_volatile,
    (),
    _SA_annotes0(SAL_volatile),
)
__inner_nonvolatile = _SAL_L_Source_(
    __inner_nonvolatile,
    (),
    _SA_annotes0(SAL_nonvolatile),
)
__inner_possibly_notnullterminated = _SAL_L_Source_(
    __inner_possibly_notnulltermiated,
    (),
    _SA_annotes1(SAL_nullTerminated,
    __maybe),
)
{ SAL_KernelMode, SAL_UserMode } = _SAL_ExecutionContext
_Previous_execution_context_ = _SAL_ExecutionContext
_Current_execution_context_ = _SAL_ExecutionContext


def _Memory_origin_(context):
    return _SAL2_Source_(_Memory_origin_, context, _SA_annotes1SAL_MemoryOrigin, context)


def _Memory_origin_when_(previousContext, context):
    return _SAL2_Source_(_Memory_origin_when_, previousContext, context, _SA_annotes2SAL_MemoryOriginWhen, previousContext, context)


def _Accessible_bytes_(context, expr):
    return _SAL2_Source_(_Accessible_bytes_, context, expr, _SA_annotes2SAL_AccessibleTo, context, expr)


def _Accessible_bytes_when_(previousContext, context, expr):
    return _SAL2_Source_(_Accessible_bytes_when_, context, previousContext, expr, _SA_annotes3SAL_AccessibleToWhen, context, previousContext, expr)


def _Pre_accessible_bytes_(context, expr):
    return _Pre_ _Accessible_bytes_context, expr


def _Pre_accessible_bytes_when_(context, previousContext, expr):
    return _Pre_ _Accessible_bytes_when_context, previousContext, expr
_User_ = _Memory_origin_when_(
    SAL_UserMode,
    SAL_UserMode) _Pre_accessible_bytes_when_(SAL_UserMode,
    SAL_KernelMode,
    0,
)


def _User_on_(expr):
    return _When_(expr != SAL_KernelMode, _User_always_)
_User_always_ = _Memory_origin_(
    SAL_UserMode) _Pre_accessible_bytes_(SAL_KernelMode,
    0,
)


def _User_always_and_needs_probe_on_(mode):
    return _User_always_ _Pre_accessible_bytes_when_SAL_UserMode, SAL_KernelMode, 0 _Pre_satisfies_(mode == _Previous_execution_context_)
_Kernel_entry_ = _SAL2_Source_(
    _Kernel_entry_,
    (),
    __inner_control_entrypoINT(UserToKernel),
)
_Kernel_entry_always_ = _SAL2_Source_(
    _Kernel_entry_,
    (),
    __inner_control_entrypoINT(UserToKernel)) _Pre_satisfies_(_Previous_execution_context_ == SAL_UserMode,
)







def __field_ecount(size):
    return _SAL1_Source_(__field_ecount, size, __notnull __elem_writableTosize)


def __field_bcount(size):
    return _SAL1_Source_(__field_bcount, size, __notnull __byte_writableTosize)


def __field_xcount(size):
    return _SAL1_Source_(__field_xcount, size, __notnull __inexpressible_writableTosize)


def __field_ecount_opt(size):
    return _SAL1_Source_(__field_ecount_opt, size, __maybenull __elem_writableTosize)


def __field_bcount_opt(size):
    return _SAL1_Source_(__field_bcount_opt, size, __maybenull __byte_writableTosize)


def __field_xcount_opt(size):
    return _SAL1_Source_(__field_xcount_opt, size, __maybenull __inexpressible_writableTosize)


def __field_ecount_part(size, init):
    return _SAL1_Source_(__field_ecount_part, size,init, __notnull __elem_writableTosize __elem_readableToinit)


def __field_bcount_part(size, init):
    return _SAL1_Source_(__field_bcount_part, size,init, __notnull __byte_writableTosize __byte_readableToinit)


def __field_xcount_part(size, init):
    return _SAL1_Source_(__field_xcount_part, size,init, __notnull __inexpressible_writableTosize __inexpressible_readableToinit)


def __field_ecount_part_opt(size, init):
    return _SAL1_Source_(__field_ecount_part_opt, size,init, __maybenull __elem_writableTosize __elem_readableToinit)


def __field_bcount_part_opt(size, init):
    return _SAL1_Source_(__field_bcount_part_opt, size,init, __maybenull __byte_writableTosize __byte_readableToinit)


def __field_xcount_part_opt(size, init):
    return _SAL1_Source_(__field_xcount_part_opt, size,init, __maybenull __inexpressible_writableTosize __inexpressible_readableToinit)


def __field_ecount_full(size):
    return _SAL1_Source_(__field_ecount_full, size, __field_ecount_partsize,size)


def __field_bcount_full(size):
    return _SAL1_Source_(__field_bcount_full, size, __field_bcount_partsize,size)


def __field_xcount_full(size):
    return _SAL1_Source_(__field_xcount_full, size, __field_xcount_partsize,size)


def __field_ecount_full_opt(size):
    return _SAL1_Source_(__field_ecount_full_opt, size, __field_ecount_part_optsize,size)


def __field_bcount_full_opt(size):
    return _SAL1_Source_(__field_bcount_full_opt, size, __field_bcount_part_optsize,size)


def __field_xcount_full_opt(size):
    return _SAL1_Source_(__field_xcount_full_opt, size, __field_xcount_part_optsize,size)
__field_nullterminated = _SAL1_Source_(
    __field_nullterminated,
    (),
    __nullterminated,
)


def __struct_bcount(size):
    return _SAL1_Source_(__struct_bcount, size, __byte_writableTosize)


def __struct_xcount(size):
    return _SAL1_Source_(__struct_xcount, size, __inexpressible_writableTosize)


def __out_awcount(expr, size):
    return _SAL1_Source_(__out_awcount, expr,size, _Pre_ __notnull __byte_writableTo(expr ? size : size * 2) _Post_ __valid __refparam)


def __in_awcount(expr, size):
    return _SAL1_Source_(__in_awcount, expr,size, _Pre_ __valid _Pre_ _Notref_ __deref __readonly __byte_readableTo(expr ? size : size * 2))
__post_invalid = _SAL1_Source_(__post_invalid, (),  _Post_ __notvalid)
__allocator = _SAL_L_Source_(__allocator, (), __inner_allocator)


def __deallocate(kind):
    return _SAL_L_Source_(__deallocate, kind, _Pre_ __notnull __post_invalid)


def __deallocate_opt(kind):
    return _SAL_L_Source_(__deallocate_opt, kind, _Pre_ __maybenull __post_invalid)
__bound = _SAL_L_Source_(__bound, (), __inner_bound)


def __range(lb, ub):
    return _SAL_L_Source_(__range, lb,ub, __inner_rangelb,ub)
__in_bound = _SAL_L_Source_(__in_bound, (), _Pre_ __inner_bound)
__out_bound = _SAL_L_Source_(__out_bound, (), _Post_ __inner_bound)
__deref_out_bound = _SAL_L_Source_(
    __deref_out_bound,
    (),
    _Post_ __deref __inner_bound,
)


def __in_range(lb, ub):
    return _SAL_L_Source_(__in_range, lb,ub, _Pre_ __inner_rangelb,ub)


def __out_range(lb, ub):
    return _SAL_L_Source_(__out_range, lb,ub, _Post_ __inner_rangelb,ub)


def __deref_in_range(lb, ub):
    return _SAL_L_Source_(__deref_in_range, lb,ub, _Pre_ __deref __inner_rangelb,ub)


def __deref_out_range(lb, ub):
    return _SAL_L_Source_(__deref_out_range, lb,ub, _Post_ __deref __inner_rangelb,ub)


def __deref_inout_range(lb, ub):
    return _SAL_L_Source_(__deref_inout_range, lb,ub, __deref_in_rangelb,ub __deref_out_rangelb,ub)


def __field_range(lb, ub):
    return _SAL_L_Source_(__field_range, lb,ub, __rangelb,ub)


def __field_data_source(src_sym):
    return _SAL_L_Source_(__field_data_source, lb,ub, __inner_data_source#src_sym)


def __range_max(a, b):
    return _SAL_L_Source_(__range_max, a,b, __range(==, a > b ? a : b))


def __range_min(a, b):
    return _SAL_L_Source_(__range_min, a,b, __range(==, a < b ? a : b))


def __in_data_source(src_sym):
    return _SAL_L_Source_(__in_data_source, src_sym, _Pre_ __inner_data_source#src_sym)


def __out_data_source(src_sym):
    return _SAL_L_Source_(__out_data_source, src_sym, _Post_ __inner_data_source#src_sym)


def __out_validated(typ_sym):
    return _SAL_L_Source_(__out_validated, src_sym, __inner_out_validated#typ_sym)


def __this_out_data_source(src_sym):
    return _SAL_L_Source_(__this_out_data_source, src_sym, __inner_this_data_source#src_sym)


def __this_out_validated(typ_sym):
    return _SAL_L_Source_(__this_out_validated, src_sym, __inner_this_out_validated#typ_sym)


def __transfer(formal):
    return _SAL_L_Source_(__transfer, src_sym, _Post_ __inner_transferformal)
__rpc_entry = _SAL_L_Source_(
    __rpc_entry,
    (formal),
    __inner_control_entrypoINT(RPC),
)
__kernel_entry = _SAL_L_Source_(
    __kernel_entry,
    (),
    __inner_control_entrypoINT(UserToKernel),
)
__gdi_entry = _SAL_L_Source_(
    __gdi_entry,
    (),
    __inner_control_entrypoINT(GDI),
)
__encoded_poINTer = _SAL_L_Source_(__encoded_poINTer, (),  __inner_encoded)
__encoded_array = _SAL_L_Source_(__encoded_array, (),  __inner_encoded)
__field_encoded_poINTer = _SAL_L_Source_(
    __field_encoded_poINTer,
    (),
    __inner_encoded,
)
__field_encoded_array = _SAL_L_Source_(
    __field_encoded_array,
    (),
    __inner_encoded,
)


def __type_has_adt_prop(adt, prop):
    return _SAL_L_Source_(__type_has_adt_prop, adt,prop, __inner_adt_propadt,prop)


def __out_has_adt_prop(adt, prop):
    return _SAL_L_Source_(__out_has_adt_prop, adt,prop, _Post_ __inner_adt_add_propadt,prop)


def __out_not_has_adt_prop(adt, prop):
    return _SAL_L_Source_(__out_not_has_adt_prop, adt,prop, _Post_ __inner_adt_remove_propadt,prop)


def __out_transfer_adt_prop(arg):
    return _SAL_L_Source_(__out_transfer_adt_prop, arg, _Post_ __inner_adt_transfer_proparg)


def __out_has_type_adt_props(typ):
    return _SAL_L_Source_(__out_has_type_adt_props, typ, _Post_ __inner_adt_type_propstyp)
__possibly_notnullterminated = _SAL_L_Source_(
    __possibly_notnullterminated,
    (),
    __inner_possibly_notnullterminated,
)
__volatile = _SAL_L_Source_(__volatile, (),  __inner_volatile)
__nonvolatile = _SAL_L_Source_(__nonvolatile, (),  __inner_nonvolatile)
__deref_volatile = _SAL_L_Source_(__deref_volatile, (),  __deref __volatile)
__deref_nonvolatile = _SAL_L_Source_(
    __deref_nonvolatile,
    (),
    __deref __nonvolatile,
)


def __analysis_assume_nullterminated(x):
    return _Analysis_assume_nullterminated_x


def __assume_validated(p):
    return __inner_assume_validatedp


def __assume_bound(i):
    return __inner_assume_boundi
_Unreferenced_parameter_ = _SAL2_Source_(
    _Unreferenced_parameter_,
    (),
    _Const_,
)
_Frees_ptr_ = _SAL_L_Source_(
    _Frees_ptr_,
    (),
    _Pre_notnull_ _Post_ptr_invalid_ __drv_freesMem(Mem),
)
_Frees_ptr_opt_ = _SAL_L_Source_(
    _Frees_ptr_opt_,
    (),
    _Pre_maybenull_ _Post_ptr_invalid_ __drv_freesMem(Mem),
)


def _Reallocation_function_(after, before, size):
    return _Success_after != NULL or size == 0) _At_(after, _Post_maybenull_ _Post_writable_byte_size_size _When_((before == NULL or size > 0), _Must_inspect_result_) _At_(before, _Post_ptr_invalid_ __drv_freesMemMem)


def _Ret_reallocated_bytes_(before, size):
    return _Reallocation_function__Curr_, before, size


def _In_NLS_string_(size):
    return _SAL_L_Source_(_In_NLS_string_, size, _When_size < 0, _In_z_) _When_(size >= 0, _In_reads_size)
_Flt_CompletionContext_Outptr_ = _SAL_L_Source_(
    _Flt_CompletionContext_Outptr_,
    (),
    _Outptr_result_maybenull_ _Pre_valid_  _At_(*_Curr_,
    _Pre_null_  _When_(return != FLT_PREOP_SUCCESS_WITH_CALLBACK and return != FLT_PREOP_SYNCHRONIZE,
    _Post_null_)),
)
_Flt_ConnectionCookie_Outptr_ = _SAL_L_Source_(
    _Flt_ConnectionCookie_Outptr_,
    (),
    _Outptr_result_maybenull_ _Pre_valid_  _At_(*_Curr_,
    _Pre_null_ _On_failure_(_Post_null_)),
)


def _Writes_and_advances_ptr_(size):
    return _SAL2_Source_(_Writes_and_advances_ptr_, size, _At_VOID*_Curr_, _Inout_) _At_(_Curr_, _Pre_writable_size_size _Post_writable_size_size _Post_satisfies_(_Curr_ - _Old__Curr_ == _Old_size - size) _At_(_Old__Curr_, _Post_readable_size_(_Old_size - size)))


def _Writes_bytes_and_advances_ptr_(size):
    return _SAL2_Source_(_Writes_bytes_and_advances_ptr, size, _At_(VOID*_Curr_, _Inout_) _At_(_Curr_, _Pre_writable_byte_size_size _Post_writable_byte_size_size _Post_satisfies_((CHAR*_Curr_) - (CHAR*_Old__Curr_) == _Old_size - size)) _At_(_Old__Curr_, _Post_readable_byte_size_(_Old_size - size)))
_Post_equals_last_error_ = _SAL2_Source_(
    _Post_equals_last_error_,
    (),
    _Post_satisfies_(_Curr_ != 0),
)


def _Translates_Win32_to_HRESULT_(errorCode):
    return _SAL2_Source_(_Translates_Win32_to_HRESULT_, errorCode, _Always_( _When_(errorCode <= 0, _At_(_Curr_, _Post_equal_to_errorCode) _When_(errorCode > 0, _At_(_Curr_, _Post_equal_to_((errorCode & 0x0000FFFF) | (FACILITY_WIN32 << 16) | 0x80000000))))))


def _Translates_NTSTATUS_to_HRESULT_(status):
    return _SAL2_Source_(_Translates_NTSTATUS_to_HRESULT_, status, _Always_( _Post_equal_to_(status | FACILITY_NT_BIT)))
_Translates_last_error_to_HRESULT_ = _SAL2_Source_(
    _Translates_last_error_to_HRESULT_,
    (),
    _Always_(  _Post_satisfies_(_Curr_ < 0)),
)


def __analysis_assume(e):
    return (__pfx_assumee,"pfx_assume",__assumee);\n"


def __analysis_assert(e):
    return (__pfx_asserte,"pfx_assert",__assumee);\n"
from specstrings_strict_h import * # NOQA

from driverspecs_h import * # NOQA
from no_sal2_h import * # NOQA

__all__ = (
    '__inner_volatile', '__field_data_source', '__deref_out_range', '_User_',
    '__deref_opt_out_xcount', '__class_code_content', '__deref_in_range', '=',
    '__deref_opt_in_xcount_opt', '__inout_xcount_full', '__file_parser_class',
    '__field_xcount_part_opt', '_Translates_NTSTATUS_to_HRESULT_', '__xcount',
    '__inner_assume_validated', '__deref_opt_xcount', '__in_bound', '__range',
    '__in_range', '__analysis_assume', '__deref_inout_range', '_Frees_ptr_',
    '__inner_transfer', '__out_has_type_adt_props', '__in_awcount', '__bound',
    '__deref_opt_out_xcount_part_opt', '__deref_in_ecount', '__out_bound',
    '__analysis_assert', '__deref_opt_in_bcount', '__out_xcount_part_opt',
    '__deref_opt_out_xcount_full_opt', '__out_has_adt_prop', '__failure', '{',
    '__field_xcount_part', '__inout_xcount_part_opt', '__deref_xcount_opt',
    '__field_ecount_part_opt', '__out_xcount_part', '__field_bcount_part',
    '_User_always_and_needs_probe_on_', '__deref_inout_xcount_opt',
    '_User_on_', '__deref_inout_xcount_full_opt', '__out_xcount', '__PRIMOP',
    '__out_not_has_adt_prop', '__deref_opt_inout_xcount_full', '__deref_in',
    '__deref_out_xcount_part_opt', '__this_out_validated', '__out_awcount',
    '__deref_opt_out_xcount_full', '__analysis_assume_nullterminated',
    '_Flt_CompletionContext_Outptr_', '_Memory_origin_', '_Frees_ptr_opt_',
    '__field_bcount', '__field_ecount_full_opt', '__inner_this_data_source',
    '_Flt_ConnectionCookie_Outptr_', '__deref_in_bcount_opt', '__transfer',
    '_Writes_and_advances_ptr_', '__struct_xcount', '__field_encoded_array',
    '__static_context', '__deref_opt_out_xcount_part', '_Memory_origin_when_',
    '__this_out_data_source', '__out_xcount_full', '__inner_adt_type_props',
    '__deref_opt_in_ecount_opt', '_User_always_', '__in_data_source',
    '__out_validated', '__deref_opt_out_xcount_opt', '__failureDefault',
    '__deref_opt_inout_xcount_full_opt', '_Translates_Win32_to_HRESULT_',
    '__field_xcount_full', '__valueUnd', '__deref_opt_inout_xcount_part',
    '_Kernel_entry_', '__deref_inout_xcount_part', '__field_ecount_full',
    '__out_xcount_opt', '__deref_opt_inout_xcount_part_opt', '__range_min',
    '__deref_volatile', '__field_xcount_full_opt', '__field_xcount_opt',
    '__deref_in_ecount_opt', '__source_code_content', '__analysis_hINT',
    '_Pre_accessible_bytes_when_', '_Accessible_bytes_when_', '__inner_range',
    '__inner_adt_prop', '__deref_opt_xcount_opt', '__SAL_H_FULL_VER',
    '__field_nullterminated', '__out_transfer_adt_prop', '_Accessible_bytes_',
    '__deref_realloc_bcount', '__inner_nonvolatile', '__analysis_noreturn',
    '__deref_in_ecount_iterator', '__deref_opt_inout_xcount_opt',
    '__field_xcount', '__kernel_entry', '__in_xcount', '__inner_adt_add_prop',
    '__deref_opt_in_ecount', '__field_bcount_full', '__encoded_array',
    '__out_data_source', '_Pre_accessible_bytes_', '__deref_out_xcount_part',
    '__field_ecount_part', '__field_ecount_opt', '__field_bcount_part_opt',
    '__allocator', '__deref_inout_ecount_iterator', '__assume_bound',
    '__deref_opt_in_bcount_opt', '__field_ecount', '__inner_data_source',
    '__out_range', '__file_parser_library', '__deref_out_xcount_full',
    '__deallocate_opt', '__deref_opt_inout_xcount', '__deref_opt_in_xcount',
    '_Unreferenced_parameter_', '__file_parser', '__deref_inout_xcount',
    '__inner_out_validated', '__inner_allocator', '__deref_in_xcount_opt',
    '__range_max', '__deref_out_xcount_full_opt', '__in_xcount_opt',
    '__possibly_notnullterminated', '_Writes_bytes_and_advances_ptr_',
    '__volatile', '__field_bcount_full_opt', '__inout_xcount', '__xcount_opt',
    '__inner_possibly_notnullterminated', '__deref_in_xcount', '__rpc_entry',
    '_Ret_reallocated_bytes_', '__deref_inout_xcount_full', '_In_NLS_string_',
    '__inner_assume_bound', '__inner_this_out_validated', '__deref_in_bcount',
    '__assume_validated', '__type_has_adt_prop', '_Reallocation_function_',
    '__deref_opt_in_opt', '__deref_out_ecount_iterator', '__post_ecount',
    '__inner_adt_transfer_prop', '__nullnullterminated', '__deref_out_xcount',
    '__inout_xcount_full_opt', '_Post_equals_last_error_', '_SAL_L_Source_',
    '__inout_xcount_part', '__field_bcount_opt', '__post_nullnullterminated',
    '__deref_xcount', '__inner_encoded', '__field_encoded_poINTer',
    '_Translates_last_error_to_HRESULT_', '__field_range', '__nonvolatile',
    '__deref_out_xcount_opt', '__struct_bcount', '__out_xcount_full_opt',
    '__inner_assume_bound_dec', '__in_ecount_or_z', '__deref_opt_in',
    '__deref_in_opt', '__deref_inout_xcount_part_opt', '__deallocate',
    '__inout_xcount_opt', '__inner_adt_remove_prop', '__inner_bound',
    '__deref_out_bound', '__post_bcount', '__inner_assume_validated_dec',
    '__encoded_poINTer', '__post_invalid', '_Kernel_entry_always_',
    '__deref_in_opt_out', '__gdi_entry', '__deref_nonvolatile',
    '_Previous_execution_context_', '_Current_execution_context_',
)
