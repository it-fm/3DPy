import json, os
from myVars import myCurrentMat

class materialsFile:
    """
    More abstract object for the current materials file.

    Methods:
    get(): Gets and interprets the materials file.  Returns a list of material() objects.
    getraw(): Gets and de-serializes the object, but that's it.  List is in this form:
        [Number of material entries, [[mat1 name, mat1 density, ...], [mat2...]]]
    set(materials): Takes a list in the get() output style and saves it to file.
    """

    FILENAME = "materials.json"

    def __init__(self):  # This must work okay because the files work fine.
        """ Open (or create) the materials data file. """
        if os.path.exists(self.FILENAME):
            self.fileObject = open(self.FILENAME, "r+")
        else:
            tempfile = open(self.FILENAME, 'x')
            tempfile.close()


    def getraw(self):  # Works fine.
        """Get and de-serialize the material data"""
        self.fileObject.seek(0,0)  # Make sure we seek to the beginning of the file.
        try:
            out = json.load(self.fileObject)  # Decode the file.
        except json.JSONDecodeError as err:  # This is the only exception we should have here.
            print("[DEBUG] JSON decode: {}".format(err.msg))  # Complain to the output.
            return(-1)  # Use -1 as an error value, to catch later.
        return(out)

    def get(self):  # This works fine.
        """Get, de-serialize, and interperet the material data."""

        data = self.getraw()    # Get the data
        if data == -1:  # Catch our error value from getraw()
            return(-1)  # Pass it along the line.
        numberOfEntries = data[0]  # The first element of the data list is the number of entires to facilitate error checking.
        materials = []
        for iter1 in range(numberOfEntries):
            materials.append(myCurrentMat.material())  # Instantiate the class here
            cmat = data[1][iter1]   # Shortcut to save typing
            # Assign all of the file's list contents to the right material attribute:
            materials[iter1].name = cmat[0]
            materials[iter1].longName = cmat[1]
            materials[iter1].diameter = cmat[2]
            materials[iter1].density = cmat[3]
            materials[iter1].pricePerKilo = cmat[4]
            materials[iter1].matFlatHandling = cmat[5]
            materials[iter1].matPricePerHr = cmat[6]
        assert len(materials) == numberOfEntries    # This ensures we have the proper number of entries, and that there were no encoding errors.
        return (materials) # Materials is now an array of material objects.

    def set(self, materials):   # So far, this is the one thing that doesn't work right.  I will fix it when I figure out a good way to.
        """
        Serialize and write the provided data to file.

        Arguments:
        materials ([] of material objects) : 
        """
        self.fileObject.seek(0,0)   # Make sure we're looking at the beginning of the file.
        output = []
        output.append(len(materials))  # That error checking number.
        output.append([])  # Make sure that's a list so we can append to it.
        for iter2 in materials:
            tempList = []  # A temporary list to save trouble.  This statement clears it for every material in the list.
            # Turn the class variables into a list.
            tempList.append(iter2.name)
            tempList.append(iter2.longName) 
            tempList.append(iter2.diameter)
            tempList.append(iter2.density)
            tempList.append(iter2.pricePerKilo)
            tempList.append(iter2.matFlatHandling) 
            tempList.append(iter2.matPricePerHr)
            output[1].append(tempList)
        json.dump(output, self.fileObject)  # Dump the list to file.

    def __del__(self):  # I don't know if this really works, and I don't know that it matters a whole lot.
        while fileObject.closed == False:
            fileObject.close()
