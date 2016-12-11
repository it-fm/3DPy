# Capstone project, 3DPy Cost Calculator
# Function: A program that allows a user to easily calculate the cost of a 3-D Printed object, with the ability to save and retrieve material data to and from file.

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


# Import my modules.  WORKS.
from myUi import *
from myFileFxs import *
from myFunctions import *
from myVars import *

INTROTEXT = """3DPy Cost Calculator -- Version 1.0.7
    Copyright (c) 2016, Logan Power
    All Rights Reserved.
    This software is released under the terms of the FreeBSD License, included with this software in LICENSE.txt
"""

exitVal = False

# This class instantiation works fine enough.  I probably didn't need to use a class for this.
mainMenuClass = myMenuContents.main()

# Clear screen, then print intro.  WORKS.
print(INTROTEXT)

# Instantiate materials file.  WORKS.
matFile = myFile.materialsFile()

# Print Main Menu, print output for testing purposes.  WORKS.
while exitVal != True:
    # Print main menu.  Prints name of currently selected material with title.
    selectedOption = menu.mainmenu(mainMenuClass.mainComposite, ': ', "==Main Menu==\nCurrently Selected Material: " + myCurrentMat.currentMat.name)
    if selectedOption == 2:
         exitVal = 1  # This will cause the loop to exit.
    elif selectedOption == 0:
        calcFxs.quickCalculate()
    elif selectedOption == 1:
        calcFxs.editMaterial(matFile)
    else:
        print ("[ERROR]  Invalid Option returned.")
    myUtils.clrsc()
exit()
