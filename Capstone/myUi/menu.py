import os
from myUi import myUtils



# Menu function.  Works perfectly as far as I can tell.

def mainmenu(OptionCompositeList, sep, title = "==Main Menu=="):
    """
    Print a menu consisting of letter identifiers and description strings, then prompt the user for a choice.

    Arguments:
    OptionCompositeList: A list of the form:
            [[identifier1, identifier2], [description1, description2]]
        for any number of identifiers and descriptions.  Each entry must have both.
      --Note: This list may change to a dictionary in future versions.
    sep = \": \" : String to print between the identifier and description.
    title = \"==Main Menu==\" : String to print as a title.

    Notes:
        Identifiers are automatically lowercased.  User input is also automatically lowercased.

    User Inputs: identifier string.

    Output: index of user's chosen identifier string.

    """
    
    iter = 0
    chosenStr = ''
    print(title)
    # Iterate over the list, printing the identifier, the separator, then the name:
    for iter in range(len(OptionCompositeList[0])):
        print(OptionCompositeList[0][iter].lower() + sep + OptionCompositeList[1][iter])
    # Ask for input:
    while chosenStr.lower() not in OptionCompositeList[0]:
        print("Enter an option and press ENTER: ", end='')
        chosenStr = input()
    # Return the index of the chosen option:
    return(OptionCompositeList[0].index(chosenStr.lower()))

if __name__ == "__main__":
    print("[ERROR] This function cannot be run standalone.")