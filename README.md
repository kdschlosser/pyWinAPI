pyWinAPI

This is a work in progress. If you feel like helping to build the file and clean them up let me know ahead of time so we do not work on the same files.

Plus I will need to explain how to use the code converter. It does a pretty decent job. It is not 100% so there is manual work that does need to be done to each file. It sure does speed up the process of creating a python version of the Windows SDK.

If you are interested in helping there is a special set of h and idl files that needs to be used with the code converter. these special files are from the latest Windows 10 sdk and have been formatted to make reading them alot easier. the preprocessor commands are indented like you would see in python. so following the code to make any manual alterations is far easier.

Now that I have come up with a layout I am going to stick to you will see additions and changes to this repo pretty often. My goal is to do the whole Windows SDK. creating what would be a pure python version of pywin32. except it will include the whole Windows API.

The file/folder structure is an identical replica of the latest Windows 10 SDK this makes it easier to locate things because you can use the information found on the Microsoft Developer website along with the Microsoft docs. if it tells you what file in the SDK something is located it will be in the same location with this package

I am still learning how to handle some of the conversions from c/cpp to ctypes. so some things may not work properly. There are also unfinished conversions that could throw you an exception. let me know if there is a specific part you need and i will shift gears and get that part working for ya.


current statistics
total number of C code files 1016
number of files converted 376

total number of C code lines 1328464
number of line converted 693756

percentage of files completed: 37.01 %
percentage of line of code converted 52.22 %

