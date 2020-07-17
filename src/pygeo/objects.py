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
    """A ray."""
    def __init__(self, ray):
        self._ray = np.array(ray, dtype=float)

    def __repr__(self):
        return f"Ray({self._point.tolist()})"

    def __eq__(self, other):
        if isinstance(other, Ray):
            return np.array_equal(other._ray, self._ray)
        return False


class Sphere:
    """A sphere."""

    def __init__(self, sphere):
        self._sphere = np.array(sphere, dtype=float)

    def __repr__(self):
        return f"Sphere({self._point.tolist()})"

    def __eq__(self, other):
        if isinstance(other, Sphere):
            return np.array_equal(other._sphere, self._sphere)
        return False


class Triangle:
    """A triangle."""

    def __init__(self, triangle):
        self._triangle = np.array(triangle, dtype=float)

    def __repr__(self):
        return f"Triangle({self._point.tolist()})"

    def __eq__(self, other):
        if isinstance(other, Triangle):
            return np.array_equal(other._triangle, self._triangle)
        return False