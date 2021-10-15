from math import pi

class Sphere: #creating Sphere class
    
    def __init__(self, name, radius):
        """
        Constructor function for the Sphere class. Generates geomtric properties

        Parameters
        ----------
        name: <str>
            Name that will be associated with a created instance of the Sphere class.
        radius: <numerical>
            Radius of the class instance used in calculations. 


        Returns
        -------
        None

        Type
        ----
        function
        """
        self.name = name
        self.radius = radius
        
    # creating a method to calculate the radius
    def getRadius(self):
        return self.radius 
    
    # creating a method to calculate the circumference
    def getCircumference(self):
        circum = 2*pi*self.radius
        return circum
    
    # creating a method to calculate the surface area 
    def surfaceArea(self):
        sArea = pi* self.radius**2
        return sArea

    # creating a method to calculate the surface area     
    def volume(self):
        vol = 4/3 * pi * self.radius**3
        return vol
    
    # defining a function that provides details of the calculated geometries in a print statement
    def printResults(self):
        
        radius = self.getRadius()
        circum = self.getCircumference()
        sArea = self.surfaceArea()
        vol = self.volume()
        
        # printing the calculated geometry outputs
        print('\nThe sphere, {}, posseses the following geometric properties: \n'\
             'a radius of {:.1f} units,\n'\
             'a circumference of {:.1f} units,\n'\
             'a surface area of {:.1e} square units,\n'\
             'a volume of {:.1e} cubic units,\n'.format (self.name, radius, circum, sArea, vol))
        
def main():
    
    """
    This script returns geometrical properties of specified objects.

    Parameters
    ----------
    None

    Returns
    -------
    <str>
        A print out of geometric properties

    Type
    ----
    function
    """
    # creating 3 different instances of Sphere with relevant inputs
    earth = Sphere ('Earth', 6371) 
    moon = Sphere ('Moon', 1737)
    sun = Sphere ('Sun', 695700)
    
    # calling the printResults method for each instance
    earth.printResults()
    moon.printResults()
    sun.printResults()
    
if __name__ == '__main__':
    main()