#!/usr/bin/python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import glob
import re
import itertools
import numpy
import sys
from mpl_toolkits.mplot3d import Axes3D

path = '/home/schnattinger/.ros/nurbs'
point_x = [[],[]]
point_y = [[],[]]
point_z = [[],[]]
def read_file(spline_number):
    global point_x, point_y, point_z
    file_list = []
    if spline_number == -1:
        file_list = glob.glob(path +'/*txt')
        print file_list
        file_list.sort(key=str)
        print file_list
    else:
        file_list.append(path + '/' +str(spline_number) + '.txt')
        file_list.append(path + '/' +str(spline_number) + '_init' + '.txt')
    m = 'x'
    colors = itertools.cycle(["r", "b", "g", "k", "y", "c", "m", "r", "y", "k"])
    knot_finished = False
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel("x in m")
    ax.set_ylabel("y in m")
    ax.set_zlabel("z in m")
    i = 0
    for file in file_list:
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
                        point_x[i].append(float(point[0]))
                        point_y[i].append(float(point[1]))
                        point_z[i].append(float(point[2]))
                    else:
                        ax.scatter(float(point[0]), float(point[1]), float(point[2]),  c=next(colors), marker=m)
#                point_x[:] = []
#                point_y[:] = []
#                point_z[:] = []
            knot_finished = False
        i = i + 1
    plt.plot(point_x[0], point_y[0], point_z[0], 'b--')
    plt.plot(point_x[1], point_y[1], point_z[1], 'g')
    plt.show()


if __name__ == '__main__':
    input_var = input("Enter splinenumber to visulize (-1 for all splines): ")
    read_file(int(input_var))
