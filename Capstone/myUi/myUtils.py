# myUtils.py
#Copyright (c) 2016, Logan Power
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
#THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
#IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from sys import platform, exit
import os


# I wrote this clear screen function, and I'm rather proud of it.  It works perfectly on Windows.
#   I have not tested it on Mac or Linux yet, but it --should-- work.
def clrsc(opsys = None):
    """
    Clear the screen using the shell command for the current OS.

    Arguments:
    opsys (optional) - Operating System String, as stated by sys.platform.
    Note: Given no arguments, the function will determine the OS by itself.

    """
    if opsys == None:
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            os.system('clear')
        elif platform == "win32":
            os.system('cls')
        else:
            print("[ERROR] System unknown.  Exiting")
            exit()

# Honestly this function will do more later.  I think it'll be a time-saver.
def ni(which = 0):
    """
    Print a defined message, easily.

    Argument:
    0: Print a Not implemented message.  (Default)

    """
    if which == 0:
        return("[NOTICE] This feature is not yet implemented.")
    else:
        return("[NOTICE] This message is being delivered in error.")


# I wrote this so I can easily reuse it.
def nvPrompt(valName = "this property", shouldBeNumeric = False, shouldBeFloat = False):
    """
    Prompt the user to enter a new value for a variable.

    Arguments:
    valName (str) : The name of the value you are prompting the user to modify.
        Should be short.
    shouldBeNumeric (bool) : Uses regex to ensure the user's input is a number (can include decimal points).
    shouldbeFloat (bool) : Modifies the regex to require a decimal point in there somewhere.

    Returns:
    val (str) : What the user typed.  Note that this is always a string regardless of the value of shouldBeNumeric.
    """
    clrsc() # clrsc is in this module.
    val = ''  # val will always be a string.
    
    if shouldBeNumeric:
        import re  # We need this module for regex
        if shouldBeFloat:
            num_format = re.compile("^\d+\.\d+$")  # We expect numbers, a decimal point, then more numbers.
        else:
            num_format = re.compile("^\d+\.?\d*$")  # Decimal point is optional.
        val = input("Enter a new value for " + valName + ": ")
        while re.match(num_format, val) == None:  # re.match() returns a match object if there is one, and returns None if there is not.
            val = input("Enter a new value for " + valName + ": ")
    else:
        val = input("Enter a new value for " + valName + ": ")  # If we don't care,just ask straight away.
    return val