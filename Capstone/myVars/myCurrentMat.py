# myCurrentMat: Holds information about the current material, and the class structures for material data.  Works fine.

class material:
    def __init__(self):
        self.name = "NONE"
        self.longName = "Not Specified"
        self.diameter = 0.0
        self.density = 0.0
        self.pricePerKilo = 0.0
        self.matFlatHandling = 0.0
        self.matPricePerHr = 0.0

currentMat = material()  # This is a global instantiation.

