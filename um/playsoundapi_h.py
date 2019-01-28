import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_PLAYSOUNDAPI_H_ = None
MMNOSOUND = None

# * ***************************************************************************
# * playsoundapi.h -- ApiSet Contract for api-ms-win-mm-playsound-l1-1-0
# *
# * Copyright (c) Microsoft Corporation. All rights reserved.
# *
# * ***************************************************************************
#
if defined(_MSC_VER):
    pass
# END IF   _MSC_VER

if not defined(_PLAYSOUNDAPI_H_):
    _PLAYSOUNDAPI_H_ = VOID

    from pyWinAPI.shared.apiset_h import * # NOQA
    from pyWinAPI.shared.apisetcconv_h import * # NOQA

    # mm common definitions
    from pyWinAPI.um.mmsyscom_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    winmm = ctypes.windll.WINMM

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # *********************************************************************
        # ***** Sound support **************
        # ***********************************************************

        if not defined(MMNOSOUND):
            if defined(_WIN32):
                # WINMMAPI
                # BOOL
                # WINAPI
                # sndPlaySoundA(
                # _In_opt_ LPCSTR pszSound,
                # _In_ UINT fuSound
                # );
                sndPlaySoundA = winmm.sndPlaySoundA
                sndPlaySoundA.restype = BOOL

                # WINMMAPI
                # BOOL
                # WINAPI
                # sndPlaySoundW(
                # _In_opt_ LPCWSTR pszSound,
                # _In_ UINT fuSound
                # );
                sndPlaySoundW = winmm.sndPlaySoundW
                sndPlaySoundW.restype = BOOL

                if defined(UNICODE):
                    sndPlaySound = sndPlaySoundW
                else:
                    sndPlaySound = sndPlaySoundA
                # END IF   not UNICODE

            else:
                pass
            # END IF

            # /* flag values for fuSound and fdwSound arguments on
            # [snd]PlaySound
            SND_SYNC = 0x0000            # play synchronously (default)
            SND_ASYNC = 0x0001            # play asynchronously
            SND_NODEFAULT = 0x0002            # silence (not default) if sound not found
            SND_MEMORY = 0x0004            # pszSound points to a memory file
            SND_LOOP = 0x0008            # loop the sound until next sndPlaySound
            SND_NOSTOP = 0x0010            # don't stop any currently playing sound
            SND_NOWAIT = 0x00002000            # don't wait if the driver is busy
            SND_ALIAS = 0x00010000            # name is a registry alias
            SND_ALIAS_ID = 0x00110000            # alias is a predefined ID
            SND_FILENAME = 0x00020000            # name is file name
            SND_RESOURCE = 0x00040004            # name is resource name or atom

            if WINVER >= 0x0400:
                SND_PURGE = 0x0040                # purge non-static events for task
                SND_APPLICATION = 0x0080                # look for application specific association
            # END IF  WINVER >= 0x0400

            SND_SENTRY = 0x00080000            # Generate a SoundSentry event with this sound
            SND_RING = 0x00100000            # Treat this as a "ring" from a communications app - don't duck me
            SND_SYSTEM = 0x00200000            # Treat this as a system sound
            SND_ALIAS_START = 0            # alias base
            if defined(_WIN32):


                def sndAlias(ch0, ch1):
                    return (SND_ALIAS_START + ch0) | (ch1 << 8)


                SND_ALIAS_SYSTEMASTERISK = sndAlias('S', '*')
                SND_ALIAS_SYSTEMQUESTION = sndAlias('S', '?')
                SND_ALIAS_SYSTEMHAND = sndAlias('S', 'H')
                SND_ALIAS_SYSTEMEXIT = sndAlias('S', 'E')
                SND_ALIAS_SYSTEMSTART = sndAlias('S', 'S')
                SND_ALIAS_SYSTEMWELCOME = sndAlias('S', 'W')
                SND_ALIAS_SYSTEMEXCLAMATION = sndAlias('S', '!')
                SND_ALIAS_SYSTEMDEFAULT = sndAlias('S', 'D')

                # WINMMAPI
                # BOOL
                # WINAPI
                # PlaySoundA(
                # _In_opt_ LPCSTR pszSound,
                # _In_opt_ HMODULE hmod,
                # _In_ DWORD fdwSound
                # );
                PlaySoundA = winmm.PlaySoundA
                PlaySoundA.restype = BOOL

                # WINMMAPI
                # BOOL
                # WINAPI
                # PlaySoundW(
                # _In_opt_ LPCWSTR pszSound,
                # _In_opt_ HMODULE hmod,
                # _In_ DWORD fdwSound
                # );
                PlaySoundW = winmm.PlaySoundW
                PlaySoundW.restype = BOOL

                if defined(UNICODE):
                    PlaySound = PlaySoundW
                else:
                    PlaySound = PlaySoundA
                # END IF   not UNICODE

            else:
                # BOOL WINAPI PlaySound(LPCSTR pszSound, HMODULE hmod, DWORD fdwSound);
                PlaySound = winmm.PlaySound
                PlaySound.restype = BOOL
            # END IF

        # END IF  ifndef MMNOSOUND
    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if defined(__cplusplus):
        pass
    # END IF

# END IF   _PLAYSOUNDAPI_H_


