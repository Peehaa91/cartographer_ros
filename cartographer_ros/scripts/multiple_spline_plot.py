#!/usr/bin/python
import matplotlib.pyplot as plt
import glob
from pylab import *
import matplotlib
from matplotlib.font_manager import FontProperties
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import re
import itertools
Folder = [
          'spline/start_google_new_scan_no_const', 'spline/start_google_new_scan_angle_no_const',
          'spline/start_google_new_scan_angle_acc_no_const']
path = '/home/schnattinger/.ros/nurbs/'


def draw_trans(start, end):

    fig = plt.figure()
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = subplot(3, 1, 2)
    ax3 = subplot(3, 1, 3)
    fontP = FontProperties()
    fontP.set_size('small')
    colors = ['r','g','y','y']
    line_sytle = ['-', '-','-',':']
    labels = ['old scan', 'old scan angle ', 'old scan angle acc', 'new scan angle acc']
    time_lists = []
    x_lists = []
    y_lists = []
    z_lists = []
    patches =[]
    counter = 0
    for folder in Folder:
        last_time = 0
        time_list = []
        x_list = []
        y_list = []
        z_list = []
        file_list = []
        for i in range(start, end + 1):
            file_name_ = path + folder + '/' + str(i) + '_trans.txt'
            with open(file_name_, 'r') as file_stream:
                for line in file_stream:
                    pos_begin = line.find(": ")
                    pos_end = line[pos_begin + 2:].find(" ")
                    trans_string = line[pos_begin + 2: pos_end + pos_begin + 2]
                    time_list.append(last_time + float(trans_string))
                    x_string = line[pos_end + pos_begin + 2 + 1:]
                    pos_begin = x_string.find(":")
                    pos_end = x_string[pos_begin + 2:].find(" ")
                    trans_string = x_string[pos_begin + 2: pos_end + pos_begin + 2]
                    x_list.append(float(trans_string))
                    y_string = x_string[pos_end + pos_begin + 2 + 1:]
                    pos_begin = y_string.find(":")
                    pos_end = y_string[pos_begin + 2:].find(" ")
                    trans_string = y_string[pos_begin + 2: pos_end + pos_begin + 2]
                    y_list.append(float(trans_string))
                    z_string = y_string[pos_end + pos_begin + 2 + 1:]
                    pos_begin = z_string.find(":")
                    pos_end = len(z_string) - 1
                    trans_string = z_string[pos_begin + 2: pos_end + pos_begin + 2]
                    z_list.append(float(trans_string))
                last_time = time_list[len(time_list) - 1]
                x_lists.append(x_list)
                y_lists.append(y_list)
                z_lists.append(z_list)

        ax = subplot(3,1,1)
        plot(time_list, x_list, linestyle=line_sytle[counter], color=colors[counter], linewidth=3.0, label=labels[counter])
        xlabel('t in s', fontsize='16')
        ylabel(r"x in m", fontsize='16')
        title('Posenfunktion x(t)', fontsize='18')
        plt.grid(True)
        ax.tick_params(labelsize=14)
        plt.legend(loc='upper left')
        ax = subplot(3, 1, 2)
        plot(time_list, y_list, linestyle=line_sytle[counter], color=colors[counter], linewidth=3.0, label=labels[counter])
        xlabel('t in s', fontsize='16')
        ylabel(r"y in m", fontsize='16')
        title('Posenfunktion y(t)', fontsize='18')
        plt.grid(True)
        ax.tick_params(labelsize=14)
        plt.legend(loc='center left')
        ax = subplot(3, 1, 3)
        plot(time_list, z_list, linestyle=line_sytle[counter], color=colors[counter], linewidth=3.0, label=labels[counter])
        xlabel('t in s', fontsize='16')
        ylabel(r"z in m", fontsize='16')
        title('Posenfunktion z(t)', fontsize='18')
        plt.legend(loc='upper left')
        plt.grid(True)
        tick_params(labelsize=14)
        fig.tight_layout()
        counter = counter + 1



def draw_angles_spline(start, end):
    fig = plt.figure()
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = subplot(3, 1, 2)
    ax3 = subplot(3, 1, 3)
    fontP = FontProperties()
    fontP.set_size('small')
    colors = ['r', 'g', 'y', 'y']
    line_sytle = ['-', '-', '-', '-']
    labels = ['old scan', 'old scan angle ', 'old scan angle acc', 'new scan angle acc']
    time_lists = []
    x_lists = []
    y_lists = []
    z_lists = []
    patches = []
    counter = 0
    for folder in Folder:
        last_time = 0
        time_list = []
        x_list = []
        y_list = []
        z_list = []
        last_time_acc = 0
        jump = False
        for i in range(start, end + 1):
            file_name_ = path + folder +'/' + str(i) + '_orientation.txt'
            with open(file_name_, 'r') as file_stream:
                for line in file_stream:
                    pos_begin = line.find(": ")
                    pos_end = line[pos_begin + 2:].find(" ")
                    trans_string = line[pos_begin + 2: pos_end + pos_begin + 2]
                    time_list.append(last_time_acc + float(trans_string))
                    x_string = line[pos_end + pos_begin + 2 + 1:]
                    pos_begin = x_string.find(":")
                    pos_end = x_string[pos_begin + 2:].find(" ")
                    trans_string = x_string[pos_begin + 2: pos_end + pos_begin + 2]
                    if (len(x_list) > 0 and (float(trans_string)* 180/math.pi  - x_list[-1]) > 160):
                        print float(trans_string)* 180/math.pi
                        print "last:" +str(x_list[-1])
                        jump = True
                    x_list.append(float(trans_string) * 180/math.pi)
                    y_string = x_string[pos_end + pos_begin + 2 + 1:]
                    pos_begin = y_string.find(":")
                    pos_end = y_string[pos_begin + 2:].find(" ")
                    trans_string = y_string[pos_begin + 2: pos_end + pos_begin + 2]
                    y_list.append(float(trans_string) * 180/math.pi)
                    z_string = y_string[pos_end + pos_begin + 2 + 1:]
                    pos_begin = z_string.find(":")
                    pos_end = len(z_string) - 1
                    trans_string = z_string[pos_begin + 2: pos_end + pos_begin + 2]
                    z_list.append(float(trans_string) * 180/math.pi)
                    if (jump):
                        print "before x:" + str(x_list[-1])
                        x_list[-1] = x_list[-1] - 180
                        print "x:" + str(x_list[-1])
                        print "before y:" + str(y_list[-1])
                        y_list[-1] = -y_list[-1] - 180
                        print "y:" + str(y_list[-1])
                        print "before z:" + str(z_list[-1])
                        if (z_list[-1] > 0):
                            z_list[-1] = z_list[-1] - 180
                        else:
                            z_list[-1] = z_list[-1] + 180
                        print "z:" + str(z_list[-1])
                        jump = False
                last_time_acc = time_list[len(time_list) - 1]
        ax = subplot(3, 1, 1)
        plot(time_list, x_list, linestyle=line_sytle[counter], color=colors[counter], linewidth=3.0,
             label=labels[counter])
        xlabel('t in s', fontsize='16')
        ylabel(r"roll in degree", fontsize='16')
        title('Posenfunktion roll(t)', fontsize='18')
        plt.grid(True)
        ax.tick_params(labelsize=14)
        plt.legend()
        ax = fig.add_subplot(3, 1, 2)
        plot(time_list, y_list, linestyle=line_sytle[counter], color=colors[counter], linewidth=3.0,
             label=labels[counter])
        xlabel('t in s', fontsize='16')
        ylabel(r"pitch in degree", fontsize='16')
        title('Posenfunktion pitch(t)', fontsize='18')
        plt.grid(True)
        plt.legend()
        ax.tick_params(labelsize=14)
        ax = subplot(3, 1, 3)
        plot(time_list, z_list, linestyle=line_sytle[counter], color=colors[counter], linewidth=3.0,
             label=labels[counter])
        xlabel('t in s', fontsize='16')
        ylabel(r"yaw in degree", fontsize='16')
        title('Posenfunktion yaw(t)', fontsize='18')
        plt.grid(True)
        plt.legend()
        ax.tick_params(labelsize=14)
        fig.tight_layout()
        counter = counter +1

if __name__ == '__main__':
    start_var = input("Enter splinenumber for start: ")
    end_var = input("Enter splinenumber for end: ")
    draw_trans(int(start_var), int(end_var))
    draw_angles_spline(int(start_var), int(end_var))
    show()