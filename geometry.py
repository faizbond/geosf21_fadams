import math

# def main():
"""
Function for adding up the components of a list.

Parameters
----------
sumNum: <list>
    A list of numbers in numerical or string format. The function converts them into integers before calculating.

Returns
-------
<int>
    Summed up values

Type
----
function
"""
# Defining a class Point
class Point:

    def __init__(self, x=0.0, y=0.0): # initial values of x and y coordinates are 0 
        self.x = x
        self.y = y

    def display(self):  # displays the coordinates
        print('xCoord = ', self.x)
        print('yCoord = ', self.y)

class Square:

    def __init__(self, point, length, angle): # starting coordinates, unit dimension and rotation angle are accepted for the constructor here
        self.point = point
        self.length = length
        self.angle = angle

    def getCorners(self):  

        pointList = [[self.point.x, self.point.y]]  # starting points as placeholders in a list 

        sq_x = [self.point.x + self.length, self.point.x + self.length, self.point.x]  # calculating the coordinates of non rotated square
        sq_y = [self.point.y , self.point.y - self.length, self.point.y - self.length]

        p = self.point.x #+ self.length/2    #function can be modified assuming the rotation is about the origin 
        q = self.point.y #- self.length/2  

        for i in range(0,3):
            # formula obtained from https://math.stackexchange.com/questions/270194/how-to-find-the-vertices-angle-after-rotation
#             equation to calculate coordinates based on given inputs 
            x_Rotate = (sq_x[i] - p)* math.cos(math.radians(self.angle))- (sq_y[i] - q) * math.sin(math.radians(self.angle)) + p  
            y_Rotate = (sq_x[i] - p)* math.sin(math.radians(self.angle)) + (sq_y[i] - q) * math.cos(math.radians(self.angle)) + p
            x_Rotate = round(x_Rotate, 2)
            y_Rotate = round(y_Rotate, 2)

            pnt = [x_Rotate,y_Rotate]   # append results to aforementioned list
            pointList.append(pnt)

            self.polyPnts = pointList   

#         print('The coordinates of all points of the square in the clockwise directions is as follows:')
        print(self.polyPnts)


# if __name__ == '__main__':
#     main()