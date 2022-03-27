# A*-Python

This repository offers a library implementing the A* algorithm in Python.
The file `base.py` includes the `AStar`base-class. Inherit from this class and override the `g` and `h` as well as `get_neighbors` methods to create a functional child. Use `AStar.evaluate` to calculate a path from a starting node to an ending node. How these nodes are defined is up to you when creating the methods described previously.
It is recommend to use the `Position` class instead of two element tuples as it offers much more functionality. However, a class like the built-in `complex` might also be better depending on your application.

## Examples

This repository includes two examples using the `Board`-class also included in `base.py`. One includes walls and one lacks it.
It is important not to delete `wallless` if you wish to use `walls` as the latter builds on the former.
