# Create a class that represents a triangle.

# ------------------------
# | Triangle             |
# ------------------------
# | side_a               |
# | side_b               |
# | side_c               |
# ------------------------
# calculate_perimeter()  |
# ------------------------

# Create a program that uses this class. The program should 
# ask the user to enter the measurements of the three sides 
# of a triangle. Then you must create an object with these 
# measurements and display its perimeter.


class Triangle:
    def __init__(self):
        self.side_a = None
        self.side_b = None
        self.side_c = None


    def calculate_perimeter(self, side_a, side_b, side_c):
        perimeter = (side_a + side_b + side_c)
        return perimeter


triangle = Triangle()
triangle.side_a = int(input("Enter the length of one side of the triangle: "))
triangle.side_b = int(input("Enter the length of the other side of the triangle: "))
triangle.side_c = int(input("Enter the length of the other side of the triangle: "))
perimeter = triangle.calculate_perimeter(triangle.side_a, triangle.side_b, triangle.side_c)
print("The perimeter of this triangle is: " + (str(perimeter)))

