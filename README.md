# __KDTree-BSP__
## KDTree for 2-Dimensional Binary Space Partitioning 

```kd_tree.py``` contains the class of the algorithm.

__Input__: an array P of 2 dimensional points, and the depth of the node.

__Output__: KDTree2 struct - root of the (sub)tree

Use ```KDTree2.printTree()``` to get the tree representation in terminal
````python
    P = numpy.random.uniform(-100, 100, size=(n,2))
    root = KDTree2(P)
    root.printTree()
````

Use ```KDTree2.printArea()``` to get a plot of the divided space
````python
    P = numpy.random.uniform(-100, 100, size=(n,2))
    root = KDTree2(P)
    root.printArea()
````

### __Example Execution__
````
    python3 main.py -n <number_of_points>
````