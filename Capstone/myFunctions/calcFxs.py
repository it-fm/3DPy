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

from myUi import myUtils, menu
from myFileFxs import *
from myVars import *
import math, copy

# This function works, but it's just math.  
def doCalculateMass(diameter, length, density):
    radius = diameter / 2.0
    area = math.pi * radius * radius
    mass = area * length * density
    return mass

# This could be done more elegantly, but it works fine as is so I'm leaving it.
def formMaterialInfoString(firstString, flatRate, length, time = None):
        titleString = firstString
        matNameString =           "Selected Material: " + myCurrentMat.currentMat.name + '\n'
        matDensityString =        "   Material Density:  " + str(myCurrentMat.currentMat.density) + '\n'
        matDiameterString =       "   Material Diameter: " + str(myCurrentMat.currentMat.diameter) + '\n'
        matPriceString =          "   Cost Per kg:       " + str(myCurrentMat.currentMat.pricePerKilo) + '\n'
        matHourlyString =         "   Cost Per Hour:     " + str(myCurrentMat.currentMat.matPricePerHr) + '\n'
        if flatRate:
            matFlatChargeString = "   Handling Charge:   " + str(myCurrentMat.currentMat.matFlatHandling) + '\n'
        else:
            matFlatChargeString = "   Handling Charge:   DISABLED\n"
        if length != None:
            currentLengthString =     "Length set:        " + str(length) + '\n'
        else:
            currentLengthString = ''
        if time != None:
            currentTimeString =       "Time set:          " + str(time) + '\n'
        else:
            currentTimeString = ''
        openingString = titleString + matNameString + matDensityString + matDiameterString + matPriceString + matHourlyString + matFlatChargeString + currentLengthString + currentTimeString
        return openingString


# This now works fine.
def selectMaterial(matFile):
    matnames = []
    compList = []
    listLabels = []
    matsList = matFile.get()  # Gets a list of the material instances in the file.
    if matsList == -1:
        return()
    for iter1 in range(len(matsList)):
        matnames.append(matsList[iter1].name)  # Makes a list of the name attributes of the material instances.
    TITLE = "Select Material"
    for iter3 in range(len(matnames)):
        listLabels.append(str(iter3))  # I have to iterate over this list to convert all of them to strings.
    compList.append(listLabels)  # compList is the composite list for the mainmenu() fx.
    compList.append(matnames)
    newOpt = range(len(matnames))[-1] + 1  # Get the number to print as the identifier.
    newMsg = "CREATE NEW MATERIAL"
    compList[0].append(str(newOpt))
    compList[1].append(newMsg)
    myUtils.clrsc()
    userSel = menu.mainmenu(compList, ": ", TITLE)
    if userSel != newOpt:
        myCurrentMat.currentMat = copy.copy(matsList[userSel])  # Copies the specified instance into currentMat.
    else:
        myCurrentMat.currentMat = copy.copy(myCurrentMat.material()) # Sets the current material to a blank instance.
        myCurrentMat.currentMat.name = myUtils.nvPrompt("material name") # Ensure we have a name right away for saving purposes.


# This now works fine.
def saveCurrentMat(matFile):
    matnames = []
    matslist = []
    matsList = matFile.get()  # Gets a list of the material instances in the file.
    if matsList == -1:  # Account for our error value.  This means our file is probably empty.
        matFile.set([copy.copy(myCurrentMat.currentMat)])  # Just throw in our current material.
    else:
        for iter1 in range(len(matsList)):
            matnames.append(matsList[iter1].name)  # Makes a list of the name attributes of the material instances.
        newMatsList = copy.deepcopy(matsList)  # Used Deep Copy here to ensure we don't modify the material instances in memory with this fx.
        if myCurrentMat.currentMat.name in matnames:  # Check to see if the material with that name already exists in the file.
            index = matnames.index(myCurrentMat.currentMat.name)  # Get the index of the material we want to modify
            newMatsList[index] = copy.copy(myCurrentMat.currentMat) # Modify the material data in the new list.
        else: # We have a new material, so append it to the end of the list.
            newMatsList.append(copy.copy(myCurrentMat.currentMat))  # Again, copying rather than passing a reference.
        matFile.set(newMatsList)


# Works perfectly.
def quickCalculate():
    """
    Run theCalculate interface.
    """

    menuCL = myMenuContents.quickCalcMenu  # Make an instance of the menu contents class.
    doFlatCharge = False
    length = 0.0
    time = 0.0
    exitval = False
    while exitval == False:
        openingString = formMaterialInfoString("~~Quick Calculate~~\n", doFlatCharge, length, time)  # Form our title string so we can pass it to mainmenu()
        myUtils.clrsc()
        userSel = menu.mainmenu(menuCL.mainComposite, ": ", openingString)  # Display the menu.
        # For these values, prompt the user to change them:
        if userSel == 0:
            myUtils.clrsc()
            length = float(myUtils.nvPrompt("Length of material used (mm)", True))
        elif userSel == 1:
            time = float(myUtils.nvPrompt("Time Spent", True))
        # Toggle the handling charge:
        elif userSel == 2:
            doFlatCharge = not doFlatCharge
        # Do the calculation:
        elif userSel == 3:
            mass = doCalculateMass(myCurrentMat.currentMat.diameter, length, myCurrentMat.currentMat.density)
            cost = myCurrentMat.currentMat.pricePerKilo * mass
            if doFlatCharge:
                cost += myCurrentMat.currentMat.matFlatHandling
            cost += myCurrentMat.currentMat.matPricePerHr * time
            myUtils.clrsc()
            print("Total mass: " + "%.5f" % mass)  # Display with 5 digits after the point, as this can be small.
            print("Total cost: " + "%.2f" % cost)  # Display with 2 digits after the point, because it's money.
            input("Press RETURN to return to QuickCalc...")
        elif userSel == 4:  # Exit.
            exitval = True


#  Works just fine.
def editMaterial(matFile):
    menuCL = myMenuContents.editMaterialMenu.mainComposite
    exitval = False
    while exitval is False:
        myUtils.clrsc()

        print(formMaterialInfoString("~~ Material Information ~~\n", True, None))
        userSel = menu.mainmenu(menuCL,": ", "Choose a property to modify:")
        if userSel == 0:
            myCurrentMat.currentMat.name = myUtils.nvPrompt("name")
        elif userSel == 1:
            myCurrentMat.currentMat.diameter = float(myUtils.nvPrompt("diameter (mm)", True))
        elif userSel == 2:
            myCurrentMat.currentMat.density = float(myUtils.nvPrompt("density (kg/mm^3)", True, True))
        elif userSel == 3:
            myCurrentMat.currentMat.pricePerKilo = float(myUtils.nvPrompt("Price per Kilo", True))
        elif userSel == 4:
            myCurrentMat.currentMat.matPricePerHr = float(myUtils.nvPrompt("Price per Hour Machine Time (X.XX)", True, True))
        elif userSel == 5:
            myCurrentMat.currentMat.matFlatHandling = float(myUtils.nvPrompt("Flat rate per part (X.XX)", True, True))
        elif userSel == 6:
            selectMaterial(matFile)
        elif userSel == 7:
            saveCurrentMat(matFile)
        else:
            exitval = True




# This is just a simple math function.
def doCalculateMass(diameter, length, density):
    """ Calculate the mass of a cylinder with a given diameter, length, and density."""
    radius = diameter / 2.0
    area = math.pi * radius * radius
    mass = area * length * density  # length is height in this case.
    return mass

