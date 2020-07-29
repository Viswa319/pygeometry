from .objects import Point,Ray,Sphere,Triangle
import numpy as np

def intersect(first_object, second_object):
    """Common function for calling either _intersect_ray_with_sphere or _intersect_ray_with_triangle
     depending on the arguments """
    if isinstance(first_object,Ray) and isinstance(second_object,Sphere):
        return _intersect_ray_with_sphere(first_object,second_object)
    
    if isinstance(first_object,Ray) and isinstance(second_object,Triangle):
        return _intersect_ray_with_triangle(first_object,second_object)

def _intersect_ray_with_sphere(Ray, Sphere):
    """Function for determining whether ray intersects with sphere or not
    \\
    Input: Ray,from class Ray, and Sphere, from class Sphere.
    \\
    Output:
    returns None and prints No intersection between ray and sphere if there is no intersection
    return point/points of intersection if ray intersects with sphere 
    """
    diff_sphereCenter_rayOrigin = np.subtract(Ray._origin,Sphere._center)
    nabla = (np.dot(Ray._direction,diff_sphereCenter_rayOrigin))**2 - ((np.dot(diff_sphereCenter_rayOrigin,diff_sphereCenter_rayOrigin)) - Sphere._radius**2)
    if nabla < 0:
        print("No intersection between ray and a sphere")
        return None
    elif nabla == 0:
        d = -1*np.dot(Ray._direction,diff_sphereCenter_rayOrigin) # one intersection point, if a ray intersects as a tangent to the sphere or ray ends in the sphere 
        return Point((Ray._origin) + (d*Ray._direction))
    else:
        d = np.array([-1*np.dot(Ray._direction,diff_sphereCenter_rayOrigin)-np.sqrt(nabla),-1*np.dot(Ray._direction,diff_sphereCenter_rayOrigin)+np.sqrt(nabla)])
        points = []
        for d in d[d>=0]:
            points.append(Point((Ray._origin) + (d*Ray._direction))) # two intersection points, if a ray passes through the sphere
        return np.array(points)    

def _intersect_ray_with_triangle(Ray,Triangle):
    ...