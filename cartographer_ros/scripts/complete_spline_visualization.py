#!/usr/bin/python
import matplotlib.pyplot as plt
import glob
from pylab import *
import re
import itertools

path = '/home/schnattinger/.ros/nurbs'

def draw_acc(spline_number):
    time_acc_list = []
    x_acc_list = []
    y_acc_list = []
    z_acc_list = []
    last_time_acc = 0
    file_list = []
    for i in range(spline_number):
        file_name_ = path + '/' +str(i) + '_acc.txt'
        with open(file_name_,'r') as file_stream:
            for line in file_stream:
                pos_begin = line.find(": ")
                pos_end = line[pos_begin + 2:].find(" ")
                trans_string = line[pos_begin + 2: pos_end + pos_begin +2]
                time_acc_list.append(last_time_acc + float(trans_string))
                x_string = line[pos_end + pos_begin + 2 +1:]
                pos_begin = x_string.find(":")
                pos_end = x_string[pos_begin + 2:].find(" ")
                trans_string = x_string[pos_begin + 2: pos_end + pos_begin + 2]
                x_acc_list.append(float(trans_string))
                y_string = x_string[pos_end + pos_begin + 2 +1:]
                pos_begin = y_string.find(":")
                pos_end = y_string[pos_begin + 2:].find(" ")
                trans_string = y_string[pos_begin + 2: pos_end + pos_begin + 2]
                y_acc_list.append(float(trans_string))
                z_string = y_string[pos_end + pos_begin + 2 +1:]
                pos_begin = z_string.find(":")
                pos_end = len(z_string) -1
                trans_string = z_string[pos_begin + 2: pos_end + pos_begin + 2]
                z_acc_list.append(float(trans_string))
        last_time_acc = time_acc_list[len(time_acc_list) -1]
    fig = plt.figure()
    ax = fig.add_subplot(3,1,1)
    plot(time_acc_list, x_acc_list, 'r')
    xlabel('t')
    ylabel('x_acc')
    title('x_acc in m/s^2')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_acc_list, y_acc_list, 'r')
    xlabel('t')
    ylabel('y_acc')
    title('y_acc in m/s^2')
    subplot(3,1,3)
    plot(time_acc_list, z_acc_list, 'r')
    xlabel('t')
    ylabel('z_acc')
    title('z_acc in m/s^2')
def draw_trans(spline_number):
    time_list = []
    last_time = 0
    x_list = []
    y_list = []
    z_list = []
    file_list = []
    for i in range(spline_number):
        file_name_ = path + '/' + str(i) + '_trans.txt'
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
    fig = plt.figure()
    ax = fig.add_subplot(3, 1, 1)
    plot(time_list, x_list, 'r')
    xlabel('t')
    ylabel('x')
    title('x in m')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_list, y_list, 'r')
    xlabel('t')
    ylabel('y')
    title('y in m')
    subplot(3, 1, 3)
    plot(time_list, z_list, 'r')
    xlabel('t')
    ylabel('z')
    title('z in m')
    fig2 = plt.figure()
    plot(x_list,y_list, 'g')
    fig3 = plt.figure()
    plot(x_list,z_list, 'g')

def draw_vel(spline_number):
    time_list = []
    last_time = 0
    x_list = []
    y_list = []
    z_list = []
    file_list = []
    for i in range(spline_number):
        file_name_ = path + '/' + str(i) + '_vel.txt'
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
    fig = plt.figure()
    ax = fig.add_subplot(3, 1, 1)
    plot(time_list, x_list, 'r')
    xlabel('t')
    ylabel('x_vel')
    title('x in m/s')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_list, y_list, 'r')
    xlabel('t')
    ylabel('y_vel')
    title('y_vel in m/s')
    subplot(3, 1, 3)
    plot(time_list, z_list, 'r')
    xlabel('t')
    ylabel('z_vel')
    title('z_vel in m/s')

def draw_acc_imu(spline_number):
    time_acc_list = []
    x_acc_list = []
    y_acc_list = []
    z_acc_list = []
    last_time_acc = 0
    file_list = []
    for i in range(spline_number):
        file_name_ = path + '/' +str(i) + '_acc_imu.txt'
        with open(file_name_,'r') as file_stream:
            for line in file_stream:
                pos_begin = line.find(": ")
                pos_end = line[pos_begin + 2:].find(" ")
                trans_string = line[pos_begin + 2: pos_end + pos_begin +2]
                time_acc_list.append(last_time_acc + float(trans_string))
                x_string = line[pos_end + pos_begin + 2 +1:]
                pos_begin = x_string.find(":")
                pos_end = x_string[pos_begin + 2:].find(" ")
                trans_string = x_string[pos_begin + 2: pos_end + pos_begin + 2]
                x_acc_list.append(float(trans_string))
                y_string = x_string[pos_end + pos_begin + 2 +1:]
                pos_begin = y_string.find(":")
                pos_end = y_string[pos_begin + 2:].find(" ")
                trans_string = y_string[pos_begin + 2: pos_end + pos_begin + 2]
                y_acc_list.append(float(trans_string))
                z_string = y_string[pos_end + pos_begin + 2 +1:]
                pos_begin = z_string.find(":")
                pos_end = len(z_string) -1
                trans_string = z_string[pos_begin + 2: pos_end + pos_begin + 2]
                z_acc_list.append(float(trans_string))
        last_time_acc = time_acc_list[len(time_acc_list) -1]
    fig = plt.figure()
    ax = fig.add_subplot(3,1,1)
    plot(time_acc_list, x_acc_list, 'r')
    xlabel('t')
    ylabel('x_acc')
    title('x_acc in m/s^2')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_acc_list, y_acc_list, 'r')
    xlabel('t')
    ylabel('y_acc')
    title('y_acc in m/s^2')
    subplot(3,1,3)
    plot(time_acc_list, z_acc_list, 'r')
    xlabel('t')
    ylabel('z_acc')
    title('z_acc in m/s^2')

if __name__ == '__main__':
    input_var = input("Enter splinenumber for end: ")
    draw_acc(int(input_var))
    draw_vel(int(input_var))
    draw_trans(int(input_var))
    draw_acc_imu(int(input_var))
    show()