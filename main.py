#-----------------------------------
# Main execution of code
#-----------------------------------

import sys, getopt
import time
import numpy as np
import matplotlib.pyplot as plt

from kdtree import KDTree2

def main(argv):
    # get arguments
    if argv == []:
        print('python3 main.py -n <number_of_points>')
        sys.exit()
    try:
        opts, args = getopt.getopt(argv,"hn:",["help", "numer_of_points="])
    except getopt.GetoptError:
        print('python3 main.py -n <number_of_points>')
        sys.exit(2)
    
    n = 0
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('python 3 main.py -n <number_of_points>')
            sys.exit()
        elif opt in ("-n", "--number_of_points"):
            n = int(arg)

    P = np.random.uniform(-100, 100, size=(n,2))
    print(P)

    start_time = time.time()
    root = KDTree2(P)
    end_time = time.time()
    print("Created KDTree in {} seconds".format(end_time-start_time))

    # print tree representation in terminal
    root.print_tree()

    # create a plot of the divided space
    root.print_area()

    root.delete_tree()


if __name__ == '__main__':
    main(sys.argv[1:])