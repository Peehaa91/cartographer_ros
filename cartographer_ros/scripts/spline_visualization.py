#!/usr/bin/python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import glob
import re
import itertools
import numpy
from mpl_toolkits.mplot3d import Axes3D

path = '/home/schnattinger/.ros/nurbs'
point_x = []
point_y = []
point_z = []
def read_file():
    global point_x, point_y, point_z
    file_list = glob.glob(path +'/*txt')
    print file_list
    file_list.sort(key=str)
    print file_list
    m = 'x'
    colors = itertools.cycle(["r", "b", "g", "y"])
    knot_finished = False
    for file in file_list:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        with open(file,'r') as file_stream:
            for line in file_stream:
                if (line.find("point") != -1):
                    m = 'x'
                    c = 'r'
                    knot_finished = True
                pos_begin = line.find("[")
                if pos_begin != -1:
                    pos_end = line[pos_begin + 1:].find("]")
                    trans_string = line[pos_begin + 1: pos_end+ pos_begin +1]
                    point = re.findall("\d+\.\d+", trans_string)
                    if knot_finished:
                        point_x.append(float(point[0]))
                        point_y.append(float(point[1]))
                        point_z.append(float(point[2]))
                    else:
                        ax.scatter(float(point[0]), float(point[1]), float(point[2]),  c=next(colors), marker=m)
            plt.plot(point_x, point_y, point_z)
            plt.show()
            point_x[:] = []
            point_y[:] = []
            point_z[:] = []
            knot_finished = False


if __name__ == '__main__':
    read_file()

