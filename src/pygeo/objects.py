import numpy as np

class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False

class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Point({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """Class Ray \\
    Inputs (2): Origin(origin point of a ray, which is an array of the form (x,y,z), where x,y,z belongs to R), 
             \\ 
     Direction(direction vector of a ray, which is an array of the form (x ,y ,z), where x,y,z belongs to R)   
    Methods: Equality between two rays"""
    def __init__(self, origin,direction):
        self._origin = np.array(origin ,dtype = float)
        if np.linalg.norm(np.array(direction,dtype=float)) == 0:
            self._direction = np.array(direction,dtype=float)
        else:
            self._direction = np.array(direction,dtype = float)/np.linalg.norm(np.array(direction,dtype=float))


    def __repr__(self):
        return f"Ray(Origin:({self._origin.tolist()}),Direction:({self._direction.tolist()}))"

    def __eq__(self, other):
        if isinstance(other, Ray):
            return np.array_equal(other._origin, self._origin) and np.array_equal(other._direction, self._direction)
        return False


class Sphere:
    """Class Sphere \\
    Inputs (2): Center(center point of a sphere, which is an array of the form (x,y,z), where x,y,z belongs to R), 
             \\ 
     Radius(Radius of a sphere, which is a non-negative real number)   
    Methods: Equality between two spheres"""

    def __init__(self, Center,Radius ):
        self._center = np.array(Center,dtype=float)
        self._radius = np.array(Radius, dtype = float)

    def __repr__(self):
        return f"Sphere(Center:({self._center.tolist()}),Radius:({self._radius.tolist()}))"

    def __eq__(self, other):
        if isinstance(other, Sphere):
            return np.array_equal(other._center, self._center) and np.array_equal(other._radius, self._radius)
        return False    
