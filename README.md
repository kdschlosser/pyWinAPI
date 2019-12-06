pyWinAPI

NOTICE

This project is never intended to run. It is to be used as a reference in order to obtain python version of the c code located in the Windows SDK. TheWindows SDK is a behemoth clockin in at almost 10 million lines of code. I think that Python would cringe and then run away if we tried to run a program that contained that many lines of code. Not to mention what the memory hit would be if we loaded that much code.

WARNING

Most objects created using ctypes or comtypes is going to require you to release them explicitly. Releasing an object is freeing the memory the object is using. Simply deleting the object in python is not going to release the memory that is being used. This is extremely important because if you do not do this you are going to end up with memory fragmentation and leaks, and this is never a nice thing to have to deal with. Make sure you read the Windows SDK documentation, it will tell you if you need to release or (free) an object. and if it tells you that you do then you MUST do it. 

Another suggestion is when you need to access some information from an object in the Windows API DO NOT HOLD REFERENCE to this object.. collect whatever data it is you need then release (free) it. It is far easier then having to keep tack of objects. and quite often the objct can become invalid which is a whole other issue because the invalid object you are not going to be able to release so you end up with your memory being held hostage. 


This is a work in progress. If you feel like helping to build the file and clean them up let me know ahead of time so we do not work on the same files.

Plus I will need to explain how to use the code converter. It does a pretty decent job. It is not 100% so there is manual work that does need to be done to each file. It sure does speed up the process of creating a python version of the Windows SDK.

If you are interested in helping there is a special set of h and idl files that needs to be used with the code converter. these special files are from the latest Windows 10 sdk and have been formatted to make reading them alot easier. the preprocessor commands are indented like you would see in python. so following the code to make any manual alterations is far easier.

Now that I have come up with a layout I am going to stick to you will see additions and changes to this repo pretty often. My goal is to do the whole Windows SDK. creating what would be a pure python version of pywin32. except it will include the whole Windows API.

The file/folder structure is an identical replica of the latest Windows 10 SDK this makes it easier to locate things because you can use the information found on the Microsoft Developer website along with the Microsoft docs. if it tells you what file in the SDK something is located it will be in the same location with this package

I am still learning how to handle some of the conversions from c/cpp to ctypes. so some things may not work properly. There are also unfinished conversions that could throw you an exception. let me know if there is a specific part you need and i will shift gears and get that part working for ya.

These are incorrect statictics.

total number of C code files 2397
number of files converted 335

total number of C code lines 3823868
number of line converted 667026

percentage of files completed: 13.98 %
percentage of line of code converted 17.44 %

There are actually
c header  files (  .h)    3966 files containing 7,303,908 lines of code.
interface files (.idl)     892 files containing   607,420 lines of code.

Where I am currently
python files    ( .py)     432 files containing   780,000 lines of code




