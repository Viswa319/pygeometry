PyGeo
=====

A Python package for three-dimensional geometry.


Installation
------------

Run
```
python -m pip install -e ".[dev]"
```
to install `pygeo` and all dependencies required for local development.


Testing
-------

Run
```
pytest tests
```
to run all the tests for `pygeo`.


Implemented Tasks
-----

1. The `Ray` class. A ray may be represented as its origin and a direction.

   1. An `__init__` method that takes the origin and direction as argument and stores them as attributes on the instance.
   1. A `__repr__` method.
   1. An `__eq__` method that works by comparing both the origin and direction of the other ray. Provided tests for this method.

1. The `Sphere` class. A sphere may be represented by its center and a radius.

   1. An `__init__` method that takes the center and radius as argument and stores them as attributes on the instance.
   1. A `__repr__` method.
   1. An `__eq__` method that works by comparing both the center and radius of the other sphere. Provided tests for this method.

1. The `_intersect_ray_and_sphere` function and provided tests for this method.

1. The `intersect` that calls either `_intersect_ray_and_sphere` or `_intersect_ray_and_triangle` depending on the arguments.
