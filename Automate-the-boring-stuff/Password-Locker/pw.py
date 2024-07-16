#! python3 
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
 'luggage': '12345'} # A Dictionary which contains the account name as a key and the password as a Value 

import sys , pyperclip 
# pyperclip module contains the methods pyperclip.copy() and pyperclip.paste(), to copy and paste text from the clipboard respectively. 
# if pyperclip isn't installed in ur computer u can use the command "pip install pyperclip" to install it. 
# the command line arguments are stored in the sys.argv 

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
#let's the command is "py pw.py email" here the arguments(pw.py and email) are stored on the sys.argv and sys.argv[1] indicates the account name, in this case "email"

if account in PASSWORDS:
 pyperclip.copy(PASSWORDS[account])
 print('Password for ' + account + ' copied to clipboard.')
else:
 print('There is no account named ' + account)

# First check if the account is found in the dictionary, if yes then copy the cooresponding password value to the clipboard using pyperclip and if no then let the user know the account isn't registered in the dictionary 



""" 
Runing Python Script in the Command Line With Shabang Line

Shebang Line
A shebang line is a special line at the beginning of your Python program that tells your computer which interpreter to use to run the script. It starts with #!.

Why Use a Shebang Line:

It’s needed if you want to run your Python script directly from the command line without having to specify the Python interpreter each time.
Shebang Line Depending on Operating System:
Windows: #! python3
OS X (Mac): #! /usr/bin/env python3
Linux: #! /usr/bin/python3


Running Python Programs on Windows

Python Interpreter Location: On Windows, the Python interpreter for Python 3.4 is located at C:\Python34\python.exe.

Using py.exe:
py.exe is a convenient program that reads the shebang line in your script and runs the appropriate version of Python.
If you have multiple Python versions installed, py.exe ensures the correct version runs your script.
Creating a Batch File:

A batch file is a text file that contains commands to be executed by the command prompt.
To make a batch file to run your Python script:
Create a new text file.
Write the following line in it:

@py.exe C:\path\to\your\pythonScript.py %*


Replace C:\path\to\your\pythonScript.py with the actual path to your script.

Save this file with a .bat extension (e.g., pythonScript.bat).

Using the Batch File: You can run your Python script by simply double-clicking the batch file or typing its name in the command prompt.

"""