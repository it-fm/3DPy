# myUtils.py
# By Logan Power

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
            num_format = re.compile("^[1-9][0-9]*\.?[0-9]+$")  # Can't begin with a zero, and decimal point is optional.
        val = input("Enter a new value for " + valName + ": ")
        while re.match(num_format, val) == None:  # re.match() returns a match object if there is one, and returns None if there is not.
            val = input("Enter a new value for " + valName + ": ")
    else:
        val = input("Enter a new value for " + valName + ": ")  # If we don't care,just ask straight away.
    return val