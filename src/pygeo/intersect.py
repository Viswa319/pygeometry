from .objects import Point,Ray, Sphere
import numpy as np

def intersect(first_object, second_object):
    if isinstance(first_object,Ray) and isinstance(second_object,Sphere):
        return _intersect_ray_with_sphere(first_object,second_object)

def _intersect_ray_with_sphere(ray, sphere):
    

