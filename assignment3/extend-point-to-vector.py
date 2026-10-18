#Task 5: Extending a Class-----------------------------------------------------
from math import sqrt
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def euclidian_distance(self, other):
        distance=(other.x - self.x)**2 + (other.y - self.y)**2
        return round(sqrt(distance))

    def ___str__(self):
        return f"Point({self.x},{self.y})" 



class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f"Vector({self.x},{self.y})"
    
    def __add__(self,other):
        return Vector(self.x + other.x ,self.y+other.y)
    
        
point1=Point(5,6)
point2=Point(3,4)
print(point1)
print(point2)
print(point1==point2)
print(point1.euclidian_distance(point2))

vector1=Vector(2,7)
vector2=Vector(0,9)
print(vector1)
print(vector2)
returned_vector=vector1.add_vectors(vector2)
print(f"class type: {type(returned_vector).__name__}")
print(returned_vector)
