# Capstone project, 3DPy Cost Calculator
# Function: A program that allows a user to easily calculate the cost of a 3-D Printed object, with the ability to save and retrieve material data to and from file.

# Import my modules.  WORKS.
from myUi import *
from myFileFxs import *
from myFunctions import *
from myVars import *

INTROTEXT = """3DPy Cost Calculator -- Version 1.0.5
    Copyright (c) 2016 Logan Power.
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