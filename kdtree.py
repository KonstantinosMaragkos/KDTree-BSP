#-----------------------------------------
# K Dimensional Tree (KD-Tree) Algorithm
# Binary space partitioning data structure 
# for 2D points
# Input: an array P of 2 dimensional points,
# and the depth node
#-----------------------------------------

import gc
import numpy as np
import matplotlib.pyplot as plt

class KDTree2:
    def __init__(self, P, depth = 0):
        self.depth = depth
        if type(P).__module__ != np.__name__:
            self.P = np.asarray(P)
        else:
            self.P = P
        
        # Initialize current Node        
        self.l = 0
        self.l_child = None
        self.r_child = None

        if P.shape[0] == 1:
            self.P = self.P[0]
        else:
            if (depth % 2) == 0: # depth is even number
                # find l: x = x0, where x0 is the median xi of P
                self.l = np.median(self.P, axis=0)[0]
                
                # split P into left and right subspace of l
                P1 = P[P[:,0] <= self.l]
                P2 = P[P[:,0] > self.l]

            else: # depth is odd number
                # find l: y = y0, where y0 is the median yi of P
                self.l = np.median(self.P, axis=0)[1]

                # split P into left(upper) and right(lower) subspace of l
                P1 = P[P[:,1] <= self.l]
                P2 = P[P[:,1] > self.l]

            # find left and right subnodes(children)
            self.l_child = KDTree2(P1, self.depth+1)
            self.r_child = KDTree2(P2, self.depth+1)
    
    def print_tree(self):
        if not self.l_child and not self.r_child:
            for i in range(self.depth):
                print('| ', end='')
            print('|-({}, {})'.format(self.P[0], self.P[1]))
        else:
            axis = 'x' if (self.depth % 2) == 0 else 'y'
            for i in range(self.depth):
                print('| ', end='')
            print('|-{}={}'.format(axis, self.l))

            ch = []
            ch.append(self.l_child)
            ch.append(self.r_child)
            for child in ch:
                child.print_tree()

    def print_area(self):
        ax = plt.axes()
        ax.scatter(self.P[:,0], self.P[:,1])
        self.print_area_rec()
        plt.show()
    
    def print_area_rec(self, left = 0, right = 0):
        if self.depth == 0:     # root case
            left = self.P.min(axis=0)[1]
            right = self.P.max(axis=0)[1]
        if self.l_child or self.r_child:   # Not leaf 
            if self.depth % 2 == 0:
                # plot vertical line
                plt.plot([self.l, self.l], [left, right], color='y')

                # call subtrees
                if self.l_child:
                    left = self.P.min(axis=0)[0]        # min x
                    right = self.l
                    self.l_child.print_area_rec(left, right)
                if self.r_child:
                    left = self.l
                    right = self.P.max(axis=0)[0]       # max x
                    self.r_child.print_area_rec(left, right)
            else:
                # plot horizontal line
                plt.plot([left, right], [self.l, self.l], color='y')

                # call subtrees
                if self.l_child:
                    left = self.P.min(axis=0)[1]       # max y
                    right = self.l                    
                    self.l_child.print_area_rec(left, right)
                if self.r_child:
                    left = self.l
                    right = self.P.max(axis=0)[1]       # max y
                    self.r_child.print_area_rec(left, right)

            
    def delete_tree(self):
        if self.l_child :
            self.l_child.delete_tree()
        
        if self.r_child:
            self.r_child.delete_tree()

        del self