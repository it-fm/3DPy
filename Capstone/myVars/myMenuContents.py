# myMenuContents.py

# I'm just using this class as a container for variables, more or less.
class main:
    mainChars = ['q', 'm', 'x']
    mainOpts = ["Quick Calculate", "Change/Edit Material", "Exit"]
    mainComposite = [mainChars, mainOpts]

class quickCalcMenu:
    mainChars = ['q', 't', 'h', 'c', 'x']
    mainOpts = ["Change length used", "Change Time Spent", "Toggle flat handling charge", "Calculate", "Return to Main Menu"]
    mainComposite = [mainChars, mainOpts]

class editMaterialMenu:
    mainChars = ['n', 'd', 'g', 'p', 'h', 'j', 's', 'w', 'q']
    mainOpts = ["Name", "Diameter", "Density", "Price per kilo", "Price per Hour", "Flat Handling Charge", "Select New Material".upper(), "SAVE MATERIAL TO FILE", "Return to main menu"]
    mainComposite = [mainChars, mainOpts]