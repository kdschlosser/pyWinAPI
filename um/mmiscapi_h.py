import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_MMISCAPI_H_ = None
MMNODRV = None
DRV_LOAD = None
MMNOMMIO = None
SEEK_SET = None


class DRVCONFIGINFOEX(ctypes.Structure):
    pass


PDRVCONFIGINFOEX = POINTER(DRVCONFIGINFOEX)
NPDRVCONFIGINFOEX = POINTER(DRVCONFIGINFOEX)
LPDRVCONFIGINFOEX = POINTER(DRVCONFIGINFOEX)


PDRVCONFIGINFOEX = POINTER(DRVCONFIGINFOEX)
NPDRVCONFIGINFOEX = POINTER(DRVCONFIGINFOEX)
LPDRVCONFIGINFOEX = POINTER(DRVCONFIGINFOEX)


class tagDRVCONFIGINFO(ctypes.Structure):
    pass


DRVCONFIGINFO = tagDRVCONFIGINFO
PDRVCONFIGINFO = POINTER(tagDRVCONFIGINFO)
NPDRVCONFIGINFO = POINTER(tagDRVCONFIGINFO)
LPDRVCONFIGINFO = POINTER(tagDRVCONFIGINFO)


DRVCONFIGINFO = tagDRVCONFIGINFO
PDRVCONFIGINFO = POINTER(tagDRVCONFIGINFO)
NPDRVCONFIGINFO = POINTER(tagDRVCONFIGINFO)
LPDRVCONFIGINFO = POINTER(tagDRVCONFIGINFO)


class _MMIOINFO(ctypes.Structure):
    pass


MMIOINFO = _MMIOINFO
PMMIOINFO = POINTER(_MMIOINFO)
NPMMIOINFO = POINTER(_MMIOINFO)
LPMMIOINFO = POINTER(_MMIOINFO)


class _MMCKINFO(ctypes.Structure):
    pass


MMCKINFO = _MMCKINFO
PMMCKINFO = POINTER(_MMCKINFO)
NPMMCKINFO = POINTER(_MMCKINFO)
LPMMCKINFO = POINTER(_MMCKINFO)

# *****************************************************************************
# mmiscapi.h -- ApiSet Contract for api-ms-win-mm-misc-l1-1
# Copyright (c) Microsoft Corporation. All rights reserved.
# *****************************************************************************

if defined(_MSC_VER):
    pass
# END IF   _MSC_VER

if not defined(_MMISCAPI_H_):
    winmm = ctypes.windll.WINMM

    _MMISCAPI_H_ = VOID
    from pyWinAPI.shared.apiset_h import * # NOQA
    from pyWinAPI.shared.apisetcconv_h import * # NOQA

    # mm common definitions
    from pyWinAPI.um.mmsyscom_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(MMNODRV):
            # *****************************************************************
            # Installable driver support
            # *****************************************************************

            if defined(_WIN32):
                DRVCONFIGINFOEX._fields_ = [
                    ('dwDCISize', DWORD),
                    ('lpszDCISectionName', LPCWSTR),
                    ('lpszDCIAliasName', LPCWSTR),
                    ('dnDevNode', DWORD),
                ]
            else:
                DRVCONFIGINFOEX._fields_ = [
                    ('dwDCISize', DWORD),
                    ('lpszDCISectionName', LPCSTR),
                    ('lpszDCIAliasName', LPCSTR),
                    ('dnDevNode', DWORD),
                ]
            # END IF

            if WINVER < 0x030a or defined(_WIN32):
                if not defined(DRV_LOAD):
                    # Driver messages
                    DRV_LOAD = 0x0001
                    DRV_ENABLE = 0x0002
                    DRV_OPEN = 0x0003
                    DRV_CLOSE = 0x0004
                    DRV_DISABLE = 0x0005
                    DRV_FREE = 0x0006
                    DRV_CONFIGURE = 0x0007
                    DRV_QUERYCONFIGURE = 0x0008
                    DRV_INSTALL = 0x0009
                    DRV_REMOVE = 0x000A
                    DRV_EXITSESSION = 0x000B
                    DRV_POWER = 0x000F
                    DRV_RESERVED = 0x0800
                    DRV_USER = 0x4000

                    # LPARAM of DRV_CONFIGURE message
                    if defined(_WIN32):
                        tagDRVCONFIGINFO._fields_ = [
                            ('dwDCISize', DWORD),
                            ('lpszDCISectionName', LPCWSTR),
                            ('lpszDCIAliasName', LPCWSTR),
                        ]
                    else:
                        tagDRVCONFIGINFO._fields_ = [
                            ('dwDCISize', DWORD),
                            ('lpszDCISectionName', LPCSTR),
                            ('lpszDCIAliasName', LPCSTR),
                        ]
                    # END IF

                    # Supported return values for DRV_CONFIGURE message
                    DRVCNF_CANCEL = 0x0000
                    DRVCNF_OK = 0x0001
                    DRVCNF_RESTART = 0x0002

                    # installable driver function prototypes
                    if defined(_WIN32):
                        # typedef LRESULT (CALLBACK* DRIVERPROC)(
                        # DWORD_PTR,
                        # HDRVR,
                        # UINT,
                        # LPARAM,
                        # LPARAM
                        # );
                        CALLBACKDRIVERPROC = CALLBACK(
                            LRESULT,
                            DWORD_PTR,
                            HDRVR,
                            UINT,
                            LPARAM,
                            LPARAM
                        )

                        # WINMMAPI
                        # LRESULT
                        # WINAPI
                        # CloseDriver(
                        # _In_ HDRVR hDriver,
                        # _In_ LPARAM lParam1,
                        # _In_ LPARAM lParam2
                        # );
                        CloseDriver = winmm.CloseDriver
                        CloseDriver.restype = LRESULT

                        # WINMMAPI
                        # HDRVR
                        # WINAPI
                        # OpenDriver(
                        # _In_ LPCWSTR szDriverName,
                        # _In_ LPCWSTR szSectionName,
                        # _In_ LPARAM lParam2
                        # );
                        OpenDriver = winmm.OpenDriver
                        OpenDriver.restype = HDRVR

                        # WINMMAPI
                        # LRESULT
                        # WINAPI
                        # SendDriverMessage(
                        # _In_ HDRVR hDriver,
                        # _In_ UINT message,
                        # _In_ LPARAM lParam1,
                        # _In_ LPARAM lParam2
                        # );
                        SendDriverMessage = winmm.SendDriverMessage
                        SendDriverMessage.restype = LRESULT

                        # WINMMAPI
                        # HMODULE
                        # WINAPI
                        # DrvGetModuleHandle(
                        # _In_ HDRVR hDriver
                        # );
                        DrvGetModuleHandle = winmm.DrvGetModuleHandle
                        DrvGetModuleHandle.restype = HMODULE

                        # WINMMAPI
                        # HMODULE
                        # WINAPI
                        # GetDriverModuleHandle(
                        # _In_ HDRVR hDriver
                        # );
                        GetDriverModuleHandle = winmm.GetDriverModuleHandle
                        GetDriverModuleHandle.restype = HMODULE

                        # WINMMAPI
                        # LRESULT
                        # WINAPI
                        # DefDriverProc(
                        # _In_ DWORD_PTR dwDriverIdentifier,
                        # _In_ HDRVR hdrvr,
                        # _In_ UINT uMsg,
                        # _In_ LPARAM lParam1,
                        # _In_ LPARAM lParam2
                        # );
                        DefDriverProc = winmm.DefDriverProc
                        DefDriverProc.restype = LRESULT

                    else:
                        # HINSTANCE WINAPI DrvGetModuleHandle(HDRVR hdrvr);
                        DrvGetModuleHandle = winmm.DrvGetModuleHandle
                        DrvGetModuleHandle.restype = WINAPI

                        DefDriverProc = DrvDefDriverProc
                    # END IF  ifdef _WIN32
                # END IF  DRV_LOAD
            # END IF  ifdef (WINVER < 0x030a) or defined(_WIN32)

            if WINVER >= 0x030a:
                # return values from DriverProc() function
                DRV_CANCEL = DRVCNF_CANCEL
                DRV_OK = DRVCNF_OK
                DRV_RESTART = DRVCNF_RESTART
            # END IF  ifdef WINVER >= 0x030a

            DRV_MCI_FIRST = DRV_RESERVED
            DRV_MCI_LAST = DRV_RESERVED + 0xFFF

            # *****************************************************************
            # Driver Helper function moved from mmddk.h
            # *****************************************************************

            # BOOL
            # APIENTRY
            # DriverCallback(
            # DWORD_PTR dwCallback,
            # DWORD dwFlags,
            # HDRVR hDevice,
            # DWORD dwMsg,
            # DWORD_PTR dwUser,
            # DWORD_PTR dwParam1,
            # DWORD_PTR dwParam2
            # );
            DriverCallback = winmm.DriverCallback
            DriverCallback.restype = BOOL

            # *****************************************************************
            # Sound schemes
            # *****************************************************************

            winmmbse = ctypes.windll.WINMMBSE

            # WINAPI
            # sndOpenSound(
            # _In_ LPCWSTR EventName,
            # _In_ LPCWSTR AppName,
            # _In_ INT32 Flags,
            # _Outptr_ PHANDLE FileHandle
            # );
            sndOpenSound = winmmbse.sndOpenSound

            # removed from winmmi.h
            # *****************************************************************
            # API to install/remove/query a MMSYS driver
            # *****************************************************************

            # /* generic prototype for audio device driver entry-point
            # functions // midMessage(), modMessage(), widMessage(),
            # wodMessage(), auxMessage()
            # typedef DWORD (APIENTRY *DRIVERMSGPROC)(
            # DWORD,
            # DWORD,
            # DWORD_PTR,
            # DWORD_PTR,
            # DWORD_PTR
            # );
            DRIVERMSGPROC = APIENTRY(
                DWORD,
                DWORD,
                DWORD,
                DWORD_PTR,
                DWORD_PTR,
                DWORD_PTR
            )

            # UINT
            # APIENTRY
            # mmDrvInstall(
            # HDRVR hDriver,
            # LPCWSTR wszDrvEntry,
            # DRIVERMSGPROC drvMessage,
            # UINT wFlags
            # );
            mmDrvInstall = winmm.mmDrvInstall
            mmDrvInstall.restype = UINT
        # END IF  ifndef MMNODRV

        if not defined(MMNOMMIO):
            # *****************************************************************
            # Multimedia File I/O support
            # *****************************************************************

            # MMIO error return values
            MMIOERR_BASE = 256
            MMIOERR_FILENOTFOUND = MMIOERR_BASE + 1 # file not found
            MMIOERR_OUTOFMEMORY = MMIOERR_BASE + 2 # out of memory
            MMIOERR_CANNOTOPEN = MMIOERR_BASE + 3 # cannot open
            MMIOERR_CANNOTCLOSE = MMIOERR_BASE + 4 # cannot close
            MMIOERR_CANNOTREAD = MMIOERR_BASE + 5 # cannot read
            MMIOERR_CANNOTWRITE = MMIOERR_BASE + 6 # cannot write
            MMIOERR_CANNOTSEEK = MMIOERR_BASE + 7 # cannot seek
            MMIOERR_CANNOTEXPAND = MMIOERR_BASE + 8 # cannot expand file
            MMIOERR_CHUNKNOTFOUND = MMIOERR_BASE + 9 # chunk not found
            MMIOERR_UNBUFFERED = MMIOERR_BASE + 10
            MMIOERR_PATHNOTFOUND = MMIOERR_BASE + 11 # path incorrect
            MMIOERR_ACCESSDENIED = MMIOERR_BASE + 12 # file was protected
            MMIOERR_SHARINGVIOLATION = MMIOERR_BASE + 13 # file in use
            MMIOERR_NETWORKERROR = MMIOERR_BASE + 14 # network not responding
            MMIOERR_TOOMANYOPENFILES = MMIOERR_BASE + 15 # no more file handles
            MMIOERR_INVALIDFILE = MMIOERR_BASE + 16 # default error file error

            # MMIO constants
            CFSEPCHAR = ' + '            # compound file name separator char.

            # MMIO data types
            # a four character code
            FOURCC = DWORD

            # a huge version of LPSTR
            HPSTR = POINTER(CHAR)
            HMMIO = DECLARE_HANDLE

            # typedef LRESULT (CALLBACK MMIOPROC)(LPSTR lpmmioinfo, UINT uMsg,
            # LPARAM lParam1, LPARAM lParam2);
            MMIOPROC = CALLBACK(
                LRESULT,
                UINT,
                LPARAM,
                LPARAM,
            )

            LPMMIOPROC = POINTER(MMIOPROC)

            # general MMIO information data structure
            _MMIOINFO._fields_ = [
                # general status flags
                ('dwFlags', DWORD),
                # pointer to I/O procedure
                ('fccIOProc', FOURCC),
                # pointer to I/O procedure
                ('pIOProc', LPMMIOPROC),
                # place for error to be returned
                ('wErrorRet', UINT),
                # alternate local task
                ('htask', HTASK),
                # size of I/O buffer (or 0L)
                ('cchBuffer', LONG),
                # start of I/O buffer (or NULL)
                ('pchBuffer', HPSTR),
                # pointer to next byte to read/write
                ('pchNext', HPSTR),
                # pointer to last valid byte to read
                ('pchEndRead', HPSTR),
                # pointer to last byte to write
                ('pchEndWrite', HPSTR),
                # disk offset of start of buffer
                ('lBufOffset', LONG),
                # disk offset of next read or write
                ('lDiskOffset', LONG),
                # data specific to type of MMIOPROC
                ('adwInfo', DWORD * 3),
                # reserved for MMIO use
                ('dwReserved1', DWORD),
                # reserved for MMIO use
                ('dwReserved2', DWORD),
                # handle to open file
                ('hmmio', HMMIO),
            ]
            LPCMMIOINFO = POINTEER(MMIOINFO)

            # RIFF chunk information data structure
            _MMCKINFO._fields_ = [
                # chunk ID
                ('ckid', FOURCC),
                # chunk size
                ('cksize', DWORD),
                # form type or list type
                ('fccType', FOURCC),
                # offset of data portion of chunk
                ('dwDataOffset', DWORD),
                # flags used by MMIO functions
                ('dwFlags', DWORD),
            ]
            LPCMMCKINFO = POINTER(MMCKINFO)

            # bit field masks
            MMIO_RWMODE = 0x00000003 # open file for reading/writing/both
            MMIO_SHAREMODE = 0x00000070 # file sharing mode number

            # constants for dwFlags field of MMIOINFO
            MMIO_CREATE = 0x00001000 # create new file (or truncate file)
            MMIO_PARSE = 0x00000100 # parse new file returning path
            MMIO_DELETE = 0x00000200 # create new file (or truncate file)
            MMIO_EXIST = 0x00004000 # checks for existence of file
            MMIO_ALLOCBUF = 0x00010000 # mmioOpen() should allocate a buffer
            MMIO_GETTEMP = 0x00020000 # mmioOpen() should retrieve temp name
            MMIO_DIRTY = 0x10000000 # I/O buffer is dirty

            # read/write mode numbers (bit field MMIO_RWMODE)
            MMIO_READ = 0x00000000 # open file for reading only
            MMIO_WRITE = 0x00000001 # open file for writing only
            MMIO_READWRITE = 0x00000002 # open file for reading and writing

            # share mode numbers (bit field MMIO_SHAREMODE)
            MMIO_COMPAT = 0x00000000 # compatibility mode
            MMIO_EXCLUSIVE = 0x00000010 # exclusive-access mode
            MMIO_DENYWRITE = 0x00000020 # deny writing to other processes
            MMIO_DENYREAD = 0x00000030 # deny reading to other processes
            MMIO_DENYNONE = 0x00000040 # deny nothing to other processes

            # various MMIO flags
            MMIO_FHOPEN = 0x0010 # mmioClose: keep file handle open
            MMIO_EMPTYBUF = 0x0010 # mmioFlush: empty the I/O buffer
            MMIO_TOUPPER = 0x0010 # mmioStringToFOURCC: to u-case
            MMIO_INSTALLPROC = 0x00010000 # mmioInstallIOProc: install MMIOProc
            MMIO_GLOBALPROC = 0x10000000 # mmioInstallIOProc: install globally
            MMIO_REMOVEPROC = 0x00020000 # mmioInstallIOProc: remove MMIOProc
            MMIO_UNICODEPROC = 0x01000000 # mmioInstallIOProc: Unicode MMIOProc
            MMIO_FINDPROC = 0x00040000 # mmioInstallIOProc: find an MMIOProc
            MMIO_FINDCHUNK = 0x0010 # mmioDescend: find a chunk by ID
            MMIO_FINDRIFF = 0x0020 # mmioDescend: find a LIST chunk
            MMIO_FINDLIST = 0x0040 # mmioDescend: find a RIFF chunk
            MMIO_CREATERIFF = 0x0020 # mmioCreateChunk: make a LIST chunk
            MMIO_CREATELIST = 0x0040 # mmioCreateChunk: make a RIFF chunk

            # message numbers for MMIOPROC I/O procedure functions
            MMIOM_READ = MMIO_READ            # read
            MMIOM_WRITE = MMIO_WRITE            # write
            MMIOM_SEEK = 2            # seek to a new position in file
            MMIOM_OPEN = 3            # open file
            MMIOM_CLOSE = 4            # close file
            MMIOM_WRITEFLUSH = 5            # write and flush
            if WINVER >= 0x030a:
                MMIOM_RENAME = 6                # rename specified file
            # END IF  ifdef WINVER >= 0x030a

            MMIOM_USER = 0x8000            # beginning of user-defined messages

            # MMIO macros
            def mmioFOURCC(ch0, ch1, ch2, ch3):
                return MAKEFOURCC(ch0, ch1, ch2, ch3)

            # standard four character codes
            FOURCC_RIFF = mmioFOURCC('R', 'I', 'F', 'F')
            FOURCC_LIST = mmioFOURCC('L', 'I', 'S', 'T')

            # four character codes used to identify standard built-in I/O
            # procedures
            FOURCC_DOS = mmioFOURCC('D', 'O', 'S', ' ')
            FOURCC_MEM = mmioFOURCC('M', 'E', 'M', ' ')

            # flags for mmioSeek()
            if not defined(SEEK_SET):
                SEEK_SET = 0                # seek to an absolute position
                SEEK_CUR = 1                # seek relative to current position
                SEEK_END = 2                # seek relative to end of file
            # END IF  ifndef SEEK_SET

            # other constants
            MMIO_DEFAULTBUFFER = 8192            # default buffer size

            # MMIO function prototypes
            if defined(_WIN32):
                # WINMMAPI
                # FOURCC
                # WINAPI
                # mmioStringToFOURCCA(
                # LPCSTR sz,
                # _In_ UINT uFlags
                # );
                mmioStringToFOURCCA = winmm.mmioStringToFOURCCA
                mmioStringToFOURCCA.restype = FOURCC

                # WINMMAPI
                # FOURCC
                # WINAPI
                # mmioStringToFOURCCW(
                # LPCWSTR sz,
                # _In_ UINT uFlags
                # );
                mmioStringToFOURCCW = winmm.mmioStringToFOURCCW
                mmioStringToFOURCCW.restype = FOURCC

                if defined(UNICODE):
                    mmioStringToFOURCC = mmioStringToFOURCCW
                else:
                    mmioStringToFOURCC = mmioStringToFOURCCA
                # END IF   not UNICODE

                # WINMMAPI
                # LPMMIOPROC
                # WINAPI
                # mmioInstallIOProcA(
                # _In_ FOURCC fccIOProc,
                # _In_opt_ LPMMIOPROC pIOProc,
                # _In_ DWORD dwFlags
                # );
                mmioInstallIOProcA = winmm.mmioInstallIOProcA
                mmioInstallIOProcA.restype = LPMMIOPROC

                # WINMMAPI
                # LPMMIOPROC
                # WINAPI
                # mmioInstallIOProcW(
                # _In_ FOURCC fccIOProc,
                # _In_opt_ LPMMIOPROC pIOProc,
                # _In_ DWORD dwFlags
                # );
                mmioInstallIOProcW = winmm.mmioInstallIOProcW
                mmioInstallIOProcW.restype = LPMMIOPROC

                if defined(UNICODE):
                    mmioInstallIOProc = mmioInstallIOProcW
                else:
                    mmioInstallIOProc = mmioInstallIOProcA
                # END IF   not UNICODE

                # WINMMAPI
                # HMMIO
                # WINAPI
                # mmioOpenA(
                # _Inout_updates_bytes_opt_(128) LPSTR pszFileName,
                # _Inout_opt_ LPMMIOINFO pmmioinfo,
                # _In_ DWORD fdwOpen
                # );
                mmioOpenA = winmm.mmioOpenA
                mmioOpenA.restype = HMMIO

                # WINMMAPI
                # HMMIO
                # WINAPI
                # mmioOpenW(
                # _Inout_updates_bytes_opt_(128) LPWSTR pszFileName,
                # _Inout_opt_ LPMMIOINFO pmmioinfo,
                # _In_ DWORD fdwOpen
                # );
                mmioOpenW = winmm.mmioOpenW
                mmioOpenW.restype = HMMIO

                if defined(UNICODE):
                    mmioOpen = mmioOpenW
                else:
                    mmioOpen = mmioOpenA
                # END IF   not UNICODE

                # WINMMAPI
                # MMRESULT
                # WINAPI
                # mmioRenameA(
                # _In_ LPCSTR pszFileName,
                # _In_ LPCSTR pszNewFileName,
                # _In_opt_ LPCMMIOINFO pmmioinfo,
                # _In_ DWORD fdwRename
                # );
                mmioRenameA = winmm.mmioRenameA
                mmioRenameA.restype = MMRESULT

                # WINMMAPI
                # MMRESULT
                # WINAPI
                # mmioRenameW(
                # _In_ LPCWSTR pszFileName,
                # _In_ LPCWSTR pszNewFileName,
                # _In_opt_ LPCMMIOINFO pmmioinfo,
                # _In_ DWORD fdwRename
                # );
                mmioRenameW = winmm.mmioRenameW
                mmioRenameW.restype = MMRESULT

                if defined(UNICODE):
                    mmioRename = mmioRenameW
                else:
                    mmioRename = mmioRenameA
                # END IF   not UNICODE

                if WINVER >= 0x030a:
                    pass
                # END IF  ifdef WINVER >= 0x030a

            else:
                pass
            # END IF

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # mmioClose(
            # _In_ HMMIO hmmio,
            # _In_ UINT fuClose
            # );
            mmioClose = winmm.mmioClose
            mmioClose.restype = MMRESULT

            # WINMMAPI
            # LONG
            # WINAPI
            # mmioRead(
            # _In_ HMMIO hmmio,
            # _Out_writes_bytes_(cch) HPSTR pch,
            # _In_ LONG cch
            # );
            mmioRead = winmm.mmioRead
            mmioRead.restype = LONG

            # WINMMAPI
            # LONG
            # WINAPI
            # mmioWrite(
            # _In_ HMMIO hmmio,
            # _In_reads_bytes_(cch) CHAR  _huge * pch,
            # _In_ LONG cch
            # );
            mmioWrite = winmm.mmioWrite
            mmioWrite.restype = LONG

            # WINMMAPI
            # LONG
            # WINAPI
            # mmioSeek(
            # _In_ HMMIO hmmio,
            # _In_ LONG lOffset,
            # _In_ INT iOrigin
            # );
            mmioSeek = winmm.mmioSeek
            mmioSeek.restype = LONG

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # mmioGetInfo(
            # _In_ HMMIO hmmio,
            # _Out_ LPMMIOINFO pmmioinfo,
            # _In_ UINT fuInfo
            # );
            mmioGetInfo = winmm.mmioGetInfo
            mmioGetInfo.restype = MMRESULT

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # mmioSetInfo(
            # _In_ HMMIO hmmio,
            # _In_ LPCMMIOINFO pmmioinfo,
            # _In_ UINT fuInfo
            # );
            mmioSetInfo = winmm.mmioSetInfo
            mmioSetInfo.restype = MMRESULT

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # mmioSetBuffer(
            # _In_ HMMIO hmmio,
            # _Out_writes_opt_(cchBuffer) LPSTR pchBuffer,
            # _In_ LONG cchBuffer,
            # _In_ UINT fuBuffer
            # );
            mmioSetBuffer = winmm.mmioSetBuffer
            mmioSetBuffer.restype = MMRESULT

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # mmioFlush(
            # _In_ HMMIO hmmio,
            # _In_ UINT fuFlush
            # );
            mmioFlush = winmm.mmioFlush
            mmioFlush.restype = MMRESULT

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # mmioAdvance(
            # _In_ HMMIO hmmio,
            # _In_opt_ LPMMIOINFO pmmioinfo,
            # _In_ UINT fuAdvance
            # );
            mmioAdvance = winmm.mmioAdvance
            mmioAdvance.restype = MMRESULT

            # WINMMAPI
            # LRESULT
            # WINAPI
            # mmioSendMessage(
            # _In_ HMMIO hmmio,
            # _In_ UINT uMsg,
            # _In_opt_ LPARAM lParam1,
            # _In_opt_ LPARAM lParam2
            # );
            mmioSendMessage = winmm.mmioSendMessage
            mmioSendMessage.restype = LRESULT

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # mmioDescend(
            # _In_ HMMIO hmmio,
            # _Inout_ LPMMCKINFO pmmcki,
            # _In_opt_ MMCKINFO  FAR * pmmckiParent,
            # _In_ UINT fuDescend
            # );
            mmioDescend = winmm.mmioDescend
            mmioDescend.restype = MMRESULT

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # mmioAscend(
            # _In_ HMMIO hmmio,
            # _In_ LPMMCKINFO pmmcki,
            # _In_ UINT fuAscend
            # );
            mmioAscend = winmm.mmioAscend
            mmioAscend.restype = MMRESULT

            # WINMMAPI
            # MMRESULT
            # WINAPI
            # mmioCreateChunk(
            # _In_ HMMIO hmmio,
            # _In_ LPMMCKINFO pmmcki,
            # _In_ UINT fuCreate
            # );
            mmioCreateChunk = winmm.mmioCreateChunk
            mmioCreateChunk.restype = MMRESULT
        # END IF  ifndef MMNOMMIO
    # END IF   WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if defined(__cplusplus):
        pass
    # END IF
# END IF   _MMISCAPI_H_
