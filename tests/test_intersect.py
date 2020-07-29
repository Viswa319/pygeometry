from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
import numpy as np
from pygeo.objects import Ray, Sphere, Triangle,Point


# _intersect_ray_with_sphere
def test_intersection__ray_with_sphere_intersects_at_one_point_given_tangent_point__return_true():
    assert (intersect(Ray((0,0,0),(1,1,0)),Sphere((0,0,0),1.0)) == Point([1/np.sqrt(2),1/np.sqrt(2),0]))

def test_intersection__ray_with_sphere_intersects_at_two_points_given_intersected_points__return_true():
    assert np.array_equal(intersect(Ray((-1,0,0),(1,0,0)),Sphere((0,0,0),1.0)),[Point([-1,0,0]),Point([1,0,0])]) is True

def test_intersection__ray_with_sphere_doesnot_intersect__return_true():
    assert (intersect(Ray((0,10,0),(1,0,0)),Sphere((0,0,0),6.0)) == None)

test_intersection__ray_with_sphere_intersects_at_one_point_given_tangent_point__return_true()
test_intersection__ray_with_sphere_intersects_at_two_points_given_intersected_points__return_true()
test_intersection__ray_with_sphere_doesnot_intersect__return_true()