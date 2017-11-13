#!/usr/bin/python
import matplotlib.pyplot as plt
import glob
from pylab import *
import math
import re
import itertools

path = '/home/schnattinger/.ros/nurbs'

def draw_acc(spline_number):
    time_acc_list = []
    x_acc_list = []
    y_acc_list = []
    z_acc_list = []
    file_list = []
    file_name_ = path + '/' +str(spline_number) + '_acc.txt'
    with open(file_name_,'r') as file_stream:
        for line in file_stream:
            pos_begin = line.find(": ")
            pos_end = line[pos_begin + 2:].find(" ")
            trans_string = line[pos_begin + 2: pos_end + pos_begin +2]
            time_acc_list.append(float(trans_string))
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
    x_list = []
    y_list = []
    z_list = []
    file_list = []
    file_name_ = path + '/' + str(spline_number) + '_trans.txt'
    with open(file_name_, 'r') as file_stream:
        for line in file_stream:
            pos_begin = line.find(": ")
            pos_end = line[pos_begin + 2:].find(" ")
            trans_string = line[pos_begin + 2: pos_end + pos_begin + 2]
            time_list.append(float(trans_string))
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

def draw_vel(spline_number):
    time_list = []
    x_list = []
    y_list = []
    z_list = []
    file_list = []
    file_name_ = path + '/' + str(spline_number) + '_vel.txt'
    with open(file_name_, 'r') as file_stream:
        for line in file_stream:
            pos_begin = line.find(": ")
            pos_end = line[pos_begin + 2:].find(" ")
            trans_string = line[pos_begin + 2: pos_end + pos_begin + 2]
            time_list.append(float(trans_string))
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
    file_list = []
    file_name_ = path + '/' +str(spline_number) + '_acc_imu.txt'
    with open(file_name_,'r') as file_stream:
        for line in file_stream:
            pos_begin = line.find(": ")
            pos_end = line[pos_begin + 2:].find(" ")
            trans_string = line[pos_begin + 2: pos_end + pos_begin +2]
            time_acc_list.append(float(trans_string))
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
    fig = plt.figure()
    ax = fig.add_subplot(3,1,1)
    plot(time_acc_list, x_acc_list, 'r')
    xlabel('t')
    ylabel('x_imu')
    title('x_imu in m/s^2')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_acc_list, y_acc_list, 'r')
    xlabel('t')
    ylabel('y_imu')
    title('y_imu in m/s^2')
    subplot(3,1,3)
    plot(time_acc_list, z_acc_list, 'r')
    xlabel('t')
    ylabel('z_imu')
    title('z_imu in m/s^2')

def draw_res_acc_imu(spline_number):
    time_acc_list = []
    x_acc_list = []
    y_acc_list = []
    z_acc_list = []
    file_list = []
    file_name_ = path + '/' + str(spline_number) + 'res_acc_imu.txt'
    with open(file_name_, 'r') as file_stream:
        for line in file_stream:
            pos_begin = line.find(": ")
            pos_end = line[pos_begin + 2:].find(" ")
            trans_string = line[pos_begin + 2: pos_end + pos_begin + 2]
            time_acc_list.append(float(trans_string))
            x_string = line[pos_end + pos_begin + 2 + 1:]
            pos_begin = x_string.find(":")
            pos_end = x_string[pos_begin + 2:].find(" ")
            trans_string = x_string[pos_begin + 2: pos_end + pos_begin + 2]
            x_acc_list.append(float(trans_string))
            y_string = x_string[pos_end + pos_begin + 2 + 1:]
            pos_begin = y_string.find(":")
            pos_end = y_string[pos_begin + 2:].find(" ")
            trans_string = y_string[pos_begin + 2: pos_end + pos_begin + 2]
            y_acc_list.append(float(trans_string))
            z_string = y_string[pos_end + pos_begin + 2 + 1:]
            pos_begin = z_string.find(":")
            pos_end = len(z_string) - 1
            trans_string = z_string[pos_begin + 2: pos_end + pos_begin + 2]
            z_acc_list.append(float(trans_string))
    fig = plt.figure()
    ax = fig.add_subplot(3, 1, 1)
    plot(time_acc_list, x_acc_list, 'r')
    xlabel('t')
    ylabel('x_res_imu')
    title('x_res_imu in m/s^2')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_acc_list, y_acc_list, 'r')
    xlabel('t')
    ylabel('y_res_imu')
    title('y_res_imu in m/s^2')
    subplot(3, 1, 3)
    plot(time_acc_list, z_acc_list, 'r')
    xlabel('t')
    ylabel('z_res_imu')
    title('z_res_imu in m/s^2')

def draw_ang_vel(spline_number):
    time_acc_list = []
    x_acc_list = []
    y_acc_list = []
    z_acc_list = []
    file_list = []
    file_name_ = path + '/' + str(spline_number) + '_ang_vel.txt'
    with open(file_name_, 'r') as file_stream:
        for line in file_stream:
            pos_begin = line.find(": ")
            pos_end = line[pos_begin + 2:].find(" ")
            trans_string = line[pos_begin + 2: pos_end + pos_begin + 2]
            time_acc_list.append(float(trans_string))
            x_string = line[pos_end + pos_begin + 2 + 1:]
            pos_begin = x_string.find(":")
            pos_end = x_string[pos_begin + 2:].find(" ")
            trans_string = x_string[pos_begin + 2: pos_end + pos_begin + 2]
            x_acc_list.append(float(trans_string))
            y_string = x_string[pos_end + pos_begin + 2 + 1:]
            pos_begin = y_string.find(":")
            pos_end = y_string[pos_begin + 2:].find(" ")
            trans_string = y_string[pos_begin + 2: pos_end + pos_begin + 2]
            y_acc_list.append(float(trans_string))
            z_string = y_string[pos_end + pos_begin + 2 + 1:]
            pos_begin = z_string.find(":")
            pos_end = len(z_string) - 1
            trans_string = z_string[pos_begin + 2: pos_end + pos_begin + 2]
            z_acc_list.append(float(trans_string))
    fig = plt.figure()
    ax = fig.add_subplot(3, 1, 1)
    plot(time_acc_list, x_acc_list, 'r')
    xlabel('t')
    ylabel('x_ang_vel')
    title('x_ang_vel in m/s')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_acc_list, y_acc_list, 'r')
    xlabel('t')
    ylabel('y_ang_vel')
    title('y_ang_vel in m/s')
    subplot(3, 1, 3)
    plot(time_acc_list, z_acc_list, 'r')
    xlabel('t')
    ylabel('z_ang_vel')
    title('z_ang_vel in m/s')

def draw_ang_vel_imu(spline_number):
    time_acc_list = []
    x_acc_list = []
    y_acc_list = []
    z_acc_list = []
    file_list = []
    file_name_ = path + '/' + str(spline_number) + '_ang_vel_imu.txt'
    with open(file_name_, 'r') as file_stream:
        for line in file_stream:
            pos_begin = line.find(": ")
            pos_end = line[pos_begin + 2:].find(" ")
            trans_string = line[pos_begin + 2: pos_end + pos_begin + 2]
            time_acc_list.append(float(trans_string))
            x_string = line[pos_end + pos_begin + 2 + 1:]
            pos_begin = x_string.find(":")
            pos_end = x_string[pos_begin + 2:].find(" ")
            trans_string = x_string[pos_begin + 2: pos_end + pos_begin + 2]
            x_acc_list.append(float(trans_string))
            y_string = x_string[pos_end + pos_begin + 2 + 1:]
            pos_begin = y_string.find(":")
            pos_end = y_string[pos_begin + 2:].find(" ")
            trans_string = y_string[pos_begin + 2: pos_end + pos_begin + 2]
            y_acc_list.append(float(trans_string))
            z_string = y_string[pos_end + pos_begin + 2 + 1:]
            pos_begin = z_string.find(":")
            pos_end = len(z_string) - 1
            trans_string = z_string[pos_begin + 2: pos_end + pos_begin + 2]
            z_acc_list.append(float(trans_string))
    fig = plt.figure()
    ax = fig.add_subplot(3, 1, 1)
    plot(time_acc_list, x_acc_list, 'r')
    xlabel('t')
    ylabel('x_ang_vel_imu')
    title('x_ang_vel_imu in m/s')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_acc_list, y_acc_list, 'r')
    xlabel('t')
    ylabel('y_ang_vel_imu')
    title('y_ang_vel_imu in m/s')
    subplot(3, 1, 3)
    plot(time_acc_list, z_acc_list, 'r')
    xlabel('t')
    ylabel('z_ang_vel_imu')
    title('z_ang_vel in m/s')

def draw_angles_spline(spline_number):
    time_acc_list = []
    x_acc_list = []
    y_acc_list = []
    z_acc_list = []
    file_list = []
    file_name_ = path + '/' + str(spline_number) + '_orientation.txt'
    with open(file_name_, 'r') as file_stream:
        for line in file_stream:
            pos_begin = line.find(": ")
            pos_end = line[pos_begin + 2:].find(" ")
            trans_string = line[pos_begin + 2: pos_end + pos_begin + 2]
            time_acc_list.append(float(trans_string))
            x_string = line[pos_end + pos_begin + 2 + 1:]
            pos_begin = x_string.find(":")
            pos_end = x_string[pos_begin + 2:].find(" ")
            trans_string = x_string[pos_begin + 2: pos_end + pos_begin + 2]
            x_acc_list.append(float(trans_string) * 180/math.pi)
            y_string = x_string[pos_end + pos_begin + 2 + 1:]
            pos_begin = y_string.find(":")
            pos_end = y_string[pos_begin + 2:].find(" ")
            trans_string = y_string[pos_begin + 2: pos_end + pos_begin + 2]
            y_acc_list.append(float(trans_string) * 180/math.pi)
            z_string = y_string[pos_end + pos_begin + 2 + 1:]
            pos_begin = z_string.find(":")
            pos_end = len(z_string) - 1
            trans_string = z_string[pos_begin + 2: pos_end + pos_begin + 2]
            z_acc_list.append(float(trans_string) * 180/math.pi)
    fig = plt.figure()
    ax = fig.add_subplot(3, 1, 1)
    plot(time_acc_list, x_acc_list, 'r')
    xlabel('t')
    ylabel('roll')
    title('roll in degree')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_acc_list, y_acc_list, 'r')
    xlabel('t')
    ylabel('pitch')
    title('pitch in degree')
    subplot(3, 1, 3)
    plot(time_acc_list, z_acc_list, 'r')
    xlabel('t')
    ylabel('yaw')
    title('yaw in degree')


if __name__ == '__main__':
    input_var = input("Enter splinenumber to visulize (-1 for all splines): ")
    draw_acc(int(input_var))
    draw_vel(int(input_var))
    draw_trans(int(input_var))
    draw_acc_imu(int(input_var))
    draw_res_acc_imu(int(input_var))
    draw_ang_vel(int(input_var))
    draw_ang_vel_imu(int(input_var))
    draw_angles_spline(int(input_var))
    show()