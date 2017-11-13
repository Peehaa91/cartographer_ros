#!/usr/bin/python
import matplotlib.pyplot as plt
import glob
from pylab import *
import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import re
import itertools
Folder = 'spline/start_google_old_scan_no_const'
path = '/home/schnattinger/.ros/nurbs/'+ Folder

def draw_acc(start, end):
    time_acc_list = []
    x_acc_list = []
    y_acc_list = []
    z_acc_list = []
    last_time_acc = 0
    file_list = []
    for i in range(start, end + 1):
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
    fig.canvas.set_window_title(Folder)
    ax = fig.add_subplot(3,1,1)
    plot(time_acc_list, x_acc_list, 'r')
    xlabel('t in s')
    ylabel('x_acc')
    title('x_acc in m/s^2')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_acc_list, y_acc_list, 'r')
    xlabel('t in s')
    ylabel('y_acc')
    title('y_acc in m/s^2')
    subplot(3,1,3)
    plot(time_acc_list, z_acc_list, 'r')
    xlabel('t in s')
    ylabel('z_acc')
    title('z_acc in m/s^2')
def draw_trans(start, end):
    time_list = []
    last_time = 0
    x_list = []
    y_list = []
    z_list = []
    file_list = []
    for i in range(start, end + 1):
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
    fig.canvas.set_window_title(Folder)
    ax = fig.add_subplot(3, 1, 1)
    plot(time_list, x_list, 'r', linewidth=2.0)
    xlabel('t in s', fontsize='16')
    ylabel(r"x in m", fontsize='16')
    title('Posenfunktion x(t)', fontsize='18')
    plt.grid(True)
    ax.tick_params(labelsize=14)
    ax = fig.add_subplot(3, 1, 2)
    plot(time_list, y_list, 'r', linewidth=2.0)
    xlabel('t in s', fontsize='16')
    ylabel(r"y in m", fontsize='16')
    title('Posenfunktion y(t)', fontsize='18')
    plt.grid(True)
    ax.tick_params(labelsize=14)
    ax = fig.add_subplot(3, 1, 2)
    plt.grid(True)
    ax = subplot(3, 1, 3)
    plot(time_list, z_list, 'r', linewidth=2.0)
    xlabel('t in s', fontsize='16')
    ylabel(r"z in m", fontsize='16')
    title('Posenfunktion z(t)', fontsize='18')
    plt.grid(True)
    ax.tick_params(labelsize=14)
    fig.tight_layout()


def draw_vel(start, end):
    time_list = []
    last_time = 0
    x_list = []
    y_list = []
    z_list = []
    file_list = []
    for i in range(start, end + 1):
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
    fig.canvas.set_window_title(Folder)
    ax = fig.add_subplot(3, 1, 1)
    plot(time_list, x_list, 'r')
    xlabel('t in s')
    ylabel('x in m/s')
    title('Spline x-Geschwindigkeit')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_list, y_list, 'r')
    xlabel('t in s')
    ylabel('y in m/s')
    title('Spline y-Geschwindigkeit')
    subplot(3, 1, 3)
    plot(time_list, z_list, 'r')
    xlabel('t in s')
    ylabel('z in m/s')
    title('Spline z-Geschwindigkeit')

def draw_acc_imu(start, end):
    time_acc_list = []
    x_acc_list = []
    y_acc_list = []
    z_acc_list = []
    last_time_acc = 0
    file_list = []
    for i in range(start, end + 1):
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
    fig.canvas.set_window_title(Folder)
    ax = fig.add_subplot(3,1,1)
    plot(time_acc_list, x_acc_list, 'r')
    xlabel('t in s')
    ylabel(r"$a_x$ $(m/s^2)$", fontsize=16, color='black')
    title('Imu-Beschleunigung ')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_acc_list, y_acc_list, 'r')
    xlabel('t in s')
    ylabel('y in m/s^2')
    title('y-Imu-Beschleunigung')
    subplot(3,1,3)
    plot(time_acc_list, z_acc_list, 'r')
    xlabel('t in s')
    ylabel('z in m/s^2')
    title('z-Imu-Beschleunigung')

def draw_ang_vel(start, end):
    time_acc_list = []
    x_acc_list = []
    y_acc_list = []
    z_acc_list = []
    last_time_acc = 0
    file_list = []
    for i in range(start, end + 1):
        file_name_ = path + '/' +str(i) + '_ang_vel.txt'
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
    fig.canvas.set_window_title(Folder)
    ax = fig.add_subplot(3,1,1)
    plot(time_acc_list, x_acc_list, 'r')
    xlabel('t in s')
    ylabel('x in rad/s')
    title('Spline Winkelgeschwindigkeit w_x')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_acc_list, y_acc_list, 'r')
    xlabel('t in s')
    ylabel('y in rad/s')
    title('Spline Winkelgeschwindigkeit w_y')
    subplot(3,1,3)
    plot(time_acc_list, z_acc_list, 'r')
    xlabel('t in s')
    ylabel('z in rad/s')
    title('Spline Winkelgeschwindigkeit w_z')

def draw_ang_vel_imu(start, end):
    time_acc_list = []
    x_acc_list = []
    y_acc_list = []
    z_acc_list = []
    last_time_acc = 0
    file_list = []
    for i in range(start, end + 1):
        file_name_ = path + '/' +str(i) + '_ang_vel_imu.txt'
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
    fig.canvas.set_window_title(Folder)
    ax = fig.add_subplot(3,1,1)
    plot(time_acc_list, x_acc_list, 'r')
    xlabel('t in s')
    ylabel('x in rad/s')
    title('IMU Winkelgeschwindigkeit w_x')
    ax = fig.add_subplot(3, 1, 2)
    plot(time_acc_list, y_acc_list, 'r')
    xlabel('t in s')
    ylabel('y_ang_vel')
    title('y_ang_vel in rad/s')
    subplot(3,1,3)
    plot(time_acc_list, z_acc_list, 'r')
    xlabel('t in s')
    ylabel('z_ang_vel')
    title('z_ang_vel in rad/s')

def draw_angles_spline(start, end):
    time_list = []
    x_list = []
    y_list = []
    z_list = []
    file_list = []
    jump = False
    last_time_acc = 0
    for i in range(start, end + 1):
        file_name_ = path + '/' + str(i) + '_orientation.txt'
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
                    print "before" + str(x_list[-1])
                    x_list[len(x_list) - 1] = x_list[-1] - 180
                    print "x:" + str(x_list[-1])
                    y_list[len(y_list) - 1] = -y_list[-1] - 180
                    print "y:" + str(y_list[-1])
                    z_list[len(z_list) - 1] = z_list[-1] - 180
                    print "z:" + str(z_list[len(z_list) - 1])
                    jump = False
            last_time_acc = time_list[len(time_list) - 1]
    fig = plt.figure()
    fig.canvas.set_window_title(Folder)
    ax = fig.add_subplot(3, 1, 1)
    plot(time_list, x_list, 'r', linewidth=2.0)
    xlabel('t in s', fontsize='16')
    ylabel(r"roll in degree", fontsize='16')
    title('Posenfunktion roll(t)', fontsize='18')
    plt.grid(True)
    ax.tick_params(labelsize=14)
    ax = fig.add_subplot(3, 1, 2)
    plot(time_list, y_list, 'r', linewidth=2.0)
    xlabel('t in s', fontsize='16')
    ylabel(r"pitch in degree", fontsize='16')
    title('Posenfunktion pitch(t)', fontsize='18')
    plt.grid(True)
    ax.tick_params(labelsize=14)
    ax = fig.add_subplot(3, 1, 2)
    plt.grid(True)
    ax = subplot(3, 1, 3)
    plot(time_list, z_list, 'r', linewidth=2.0)
    xlabel('t in s', fontsize='16')
    ylabel(r"yaw in degree", fontsize='16')
    title('Posenfunktion yaw(t)', fontsize='18')
    plt.grid(True)
    ax.tick_params(labelsize=14)
    fig.tight_layout()

if __name__ == '__main__':
    start_var = input("Enter splinenumber for start: ")
    end_var = input("Enter splinenumber for end: ")
#    draw_acc(int(start_var), int(end_var))
#    draw_vel(int(start_var), int(end_var))
    draw_trans(int(start_var), int(end_var))
#    draw_acc_imu(int(start_var), int(end_var))
#    draw_ang_vel(int(start_var), int(end_var))
#    draw_ang_vel_imu(int(start_var), int(end_var))
    draw_angles_spline(int(start_var), int(end_var))
    show()