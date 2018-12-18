import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *



from winapifamily_h import * # NOQA

# /* + + BUILD Version: 0001 Increment this if a change has global effects
# Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# windows.h Abstract: Master include file for Windows applications. - -
if not defined(_WINDOWS_):
    #~#~#~    #define _WINDOWS_
    from sdkddkver_h import * # NOQA
    if not defined(_INC_WINDOWS):
        #~#~#~        #define _INC_WINDOWS
        if defined (_MSC_VER) and (_MSC_VER >= 1020):
            pass
        # END IF
            # /* If defined, the following flags inhibit definition of the
            # indicated items. NOGDICAPMASKS - CC_*, LC_*, PC_*, CP_*, TC_*,
            # RC_ NOVIRTUALKEYCODES - VK_* NOWINMESSAGES - WM_*, EM_*, LB_*,
            # CB_* NOWINSTYLES - WS_*, CS_*, ES_*, LBS_*, SBS_*, CBS_*
            # NOSYSMETRICS - SM_* NOMENUS - MF_* NOICONS - IDI_* NOKEYSTATES -
            # MK_* NOSYSCOMMANDS - SC_* NORASTEROPS - Binary and Tertiary
            # raster ops NOSHOWWINDOW - SW_* OEMRESOURCE - OEM Resource values
            # NOATOM - Atom Manager routines NOCLIPBOARD - Clipboard routines
            # NOCOLOR - Screen colors NOCTLMGR - Control and Dialog routines
            # NODRAWTEXT - DrawText() and DT_* NOGDI - All GDI defines and
            # routines NOKERNEL - All KERNEL defines and routines NOUSER - All
            # USER defines and routines NONLS - All NLS defines and routines
            # NOMB - MB_* and MessageBox() NOMEMMGR - GMEM_*, LMEM_*, GHND,
            # LHND, associated routines NOMETAFILE - typedef METAFILEPICT
            # NOMINMAX - Macros min(a,b) and max(a,b) NOMSG - typedef MSG and
            # associated routines NOOPENFILE - OpenFile(), OemToAnsi,
            # AnsiToOem, and OF_* NOSCROLL - SB_* and scrolling routines
            # NOSERVICE - All Service Controller routines, SERVICE_ equates,
            # etc. NOSOUND - Sound driver routines NOTEXTMETRIC - typedef
            # TEXTMETRIC and associated routines NOWH - SetWindowsHook and
            # WH_* NOWINOFFSETS - GWL_*, GCL_*, associated routines NOCOMM -
            # COMM driver routines NOKANJI - Kanji support stuff. NOHELP -
            # Help engine interface. NOPROFILER - Profiler interface.
            # NODEFERWINDOWPOS - DeferWindowPos routines NOMCX - Modem
            # Configuration Extensions
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            if defined(RC_INVOKED) and not defined(NOWINRES):
                from winresrc_h import * # NOQA
            else:
                if defined(RC_INVOKED):
                    # Turn off a bunch of stuff to ensure that RC files
                    # compile OK.                    #~#~#~                    #define NOATOM                    #~#~#~                    #define NOGDI                    #~#~#~                    #define NOGDICAPMASKS                    #~#~#~                    #define NOMETAFILE                    #~#~#~                    #define NOMINMAX                    #~#~#~                    #define NOMSG                    #~#~#~                    #define NOOPENFILE                    #~#~#~                    #define NORASTEROPS                    #~#~#~                    #define NOSCROLL                    #~#~#~                    #define NOSOUND                    #~#~#~                    #define NOSYSMETRICS                    #~#~#~                    #define NOTEXTMETRIC                    #~#~#~                    #define NOWH                    #~#~#~                    #define NOCOMM                    #~#~#~                    #define NOKANJI                    #~#~#~                    #define NOCRYPT                    #~#~#~                    #define NOMCX                # END IF
                if not defined(_68K_) and not defined(_MPPC_) and not defined(_X86_) and not defined(_IA64_) and not defined(_AMD64_) and not defined(_ARM_) and not defined(_ARM64_) and defined(_M_IX86):
                    #~#~#~                    #define _X86_
                    if not defined(_CHPE_X86_ARM64_) and defined(_M_HYBRID):
                        #~#~#~                        #define _CHPE_X86_ARM64_                    # END IF
                # END IF
                if not defined(_68K_) and not defined(_MPPC_) and not defined(_X86_) and not defined(_IA64_) and not defined(_AMD64_) and not defined(_ARM_) and not defined(_ARM64_) and defined(_M_AMD64):
                    #~#~#~                    #define _AMD64_                # END IF
                if not defined(_68K_) and not defined(_MPPC_) and not defined(_X86_) and not defined(_IA64_) and not defined(_AMD64_) and not defined(_ARM_) and not defined(_ARM64_) and defined(_M_ARM):
                    #~#~#~                    #define _ARM_                # END IF
                if not defined(_68K_) and not defined(_MPPC_) and not defined(_X86_) and not defined(_IA64_) and not defined(_AMD64_) and not defined(_ARM_) and not defined(_ARM64_) and defined(_M_ARM64):
                    #~#~#~                    #define _ARM64_                # END IF
                if not defined(_68K_) and not defined(_MPPC_) and not defined(_X86_) and not defined(_IA64_) and not defined(_AMD64_) and not defined(_ARM_) and not defined(_ARM64_) and defined(_M_M68K):
                    #~#~#~                    #define _68K_                # END IF
                if not defined(_68K_) and not defined(_MPPC_) and not defined(_X86_) and not defined(_IA64_) and not defined(_AMD64_) and not defined(_ARM_) and not defined(_ARM64_) and defined(_M_MPPC):
                    #~#~#~                    #define _MPPC_                # END IF
                if not defined(_68K_) and not defined(_MPPC_) and not defined(_X86_) and not defined(_M_IX86) and not defined(_AMD64_) and not defined(_ARM_) and not defined(_ARM64_) and defined(_M_IA64):
                    if not defined(_IA64_):
                        #~#~#~                        #define _IA64_                    # END IF  not _IA64_
                # END IF
                if not defined(_MAC):
                    if defined(_68K_) or defined(_MPPC_):
                        #~#~#~                        #define _MAC                    # END IF
                # END IF
                if defined (_MSC_VER):
                    if  _MSC_VER >= 800 :
                        if not defined(__cplusplus):
                            # outside the warning push/pop scope.                        # END IF
                    # END IF
                # END IF
                        if not defined(__WINDOWS_DONT_DISABLE_PRAGMA_PACK_WARNING__):
                            pass
                        # END IF
                        if _MSC_VER >= 1200:
                            pass
                        # END IF
                    if  _MSC_VER >= 800 :
                        pass
                    # END IF
                if not defined(RC_INVOKED):
                    from excpt_h import * # NOQA
                    from stdarg_h import * # NOQA
                # END IF  RC_INVOKED
                from windef_h import * # NOQA
                from winbase_h import * # NOQA
                from wingdi_h import * # NOQA
                from winuser_h import * # NOQA
                if not defined(_MAC) or defined(_WIN32NLS):
                    from winnls_h import * # NOQA
                # END IF
                if not defined(_MAC):
                    from wincon_h import * # NOQA
                    from winver_h import * # NOQA
                # END IF
                if not defined(_MAC) or defined(_WIN32REG):
                    from winreg_h import * # NOQA
                # END IF
                if not defined(_MAC):
                    from winnetwk_h import * # NOQA
                # END IF
                if not defined(WIN32_LEAN_AND_MEAN):
                    from cderr_h import * # NOQA
                    from dde_h import * # NOQA
                    from ddeml_h import * # NOQA
                    from dlgs_h import * # NOQA
                    if not defined(_MAC):
                        from lzexpand_h import * # NOQA
                        from mmsystem_h import * # NOQA
                        from nb30_h import * # NOQA
                        from rpc_h import * # NOQA
                    # END IF
                    from shellapi_h import * # NOQA
                    if not defined(_MAC):
                        from winperf_h import * # NOQA
                        from winsock_h import * # NOQA
                    # END IF
                    if not defined(NOCRYPT):
                        from wincrypt_h import * # NOQA
                        from winefs_h import * # NOQA
                        from winscard_h import * # NOQA
                    # END IF
                    if not defined(NOGDI):
                        if not defined(_MAC):
                            from winspool_h import * # NOQA
                            if defined(INC_OLE1):
                                from ole_h import * # NOQA
                            else:
                                from ole2_h import * # NOQA
                            # END IF  not INC_OLE1
                        # END IF  not MAC
                        from commdlg_h import * # NOQA
                    # END IF  not NOGDI
                # END IF  WIN32_LEAN_AND_MEAN
                from stralign_h import * # NOQA
                if defined(_MAC):
                    from winwlm_h import * # NOQA
                # END IF
                if defined(INC_OLE2):
                    from ole2_h import * # NOQA
                # END IF  INC_OLE2
                if not defined(_MAC):
                    if not defined(NOSERVICE):
                        from winsvc_h import * # NOQA
                    # END IF
                    if WINVER >= 0x0400:
                        if not defined(NOMCX):
                            from mcx_h import * # NOQA
                        # END IF  NOMCX
                        if not defined(NOIME):
                            from imm_h import * # NOQA
                        # END IF
                    # END IF  WINVER >= 0x0400
                # END IF
                        if _MSC_VER >= 1200:
                            pass
                if not defined(RC_INVOKED):
                    if  _MSC_VER >= 800 :
                        else:
                            # Leave 4514 disabled. It's an unneeded warning
                            # anyway.                        # END IF
                    # END IF
                # END IF  RC_INVOKED
            # END IF  RC_INVOKED
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    # END IF  _INC_WINDOWS
# END IF  _WINDOWS_
