#!/usr/bin/python
import matplotlib.pyplot as plt
import glob
from pylab import *
import numpy as np
#import quaternion
from numpy import linalg
import matplotlib
from matplotlib.font_manager import FontProperties
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import re
import itertools
#['spline/start_google_old_scan_no_const','spline/start_google_old_scan_angle_no_const','spline/start_google_old_scan_angle_acc_no_const',
#Folder = ['spline/start_google_new_scan_no_const', 'spline/start_google_new_scan_angle_no_const','spline/start_google_new_scan_angle_acc_no_const']
#Folder = [
#          'spline/start_google_new_scan_no_const', 'spline/start_google_new_scan_angle_no_const','spline/start_google_new_scan_angle_acc_no_const']
#Folder = [
#    'spline/Hallway_old_scan_no_const','spline/Hallway_old_scan_angle_no_const','spline/Hallway_old_scan_angle_acc_no_const']#'spline/Hallway_new_scan_angle_acc_low_const']
Folder = [
    'spline/Treppe_old_scan_no_const','spline/Treppe_old_scan_angle_no_const','spline/Treppe_old_scan_angle_acc_new',
    'spline/Treppe_new_scan_no_const','spline/Treppe_new_scan_angle_no_const','spline/Treppe_new_scan_angle_acc_new']
path = '/home/schnattinger/.ros/nurbs/'
path_standard = '/home/schnattinger/.ros/nurbs/standard/Treppe_normal'
x_standard = []
y_standard = []
z_standard = []
time_list_standard = []
mean_list = []
def read_standard_params():
    global x_standard, y_standard, z_standard, time_list_standard
    last_time = 0
    file_list = []
    file_name_ = path_standard + '/standard_orientation_.txt'
    with open(file_name_, 'r') as file_stream:
        for line in file_stream:
            pos_begin = line.find(": ")
            pos_end = line[pos_begin + 2:].find(" ")
            trans_string = line[pos_begin + 2: pos_end + pos_begin + 2]
            time_list_standard.append(last_time + float(trans_string))
            x_string = line[pos_end + pos_begin + 2 + 1:]
            pos_begin = x_string.find(":")
            pos_end = x_string[pos_begin + 2:].find(" ")
            trans_string = x_string[pos_begin + 2: pos_end + pos_begin + 2]
            x_standard.append(float(trans_string)* 180/math.pi)
            y_string = x_string[pos_end + pos_begin + 2 + 1:]
            pos_begin = y_string.find(":")
            pos_end = y_string[pos_begin + 2:].find(" ")
            trans_string = y_string[pos_begin + 2: pos_end + pos_begin + 2]
            y_standard.append(float(trans_string)* 180/math.pi)
            z_string = y_string[pos_end + pos_begin + 2 + 1:]
            pos_begin = z_string.find(":")
            pos_end = len(z_string) - 1
            trans_string = z_string[pos_begin + 2: pos_end + pos_begin + 2]
            z_standard.append(float(trans_string)* 180/math.pi)
            last_time = time_list_standard[len(time_list_standard) - 1]


x_spline_lists = []
y_spline_lists = []
z_spline_lists = []
time_spline_lists = []
def read_spline_params(start, end):
    global x_spline_lists, y_spline_lists, z_spline_lists, time_spline_lists
    for folder in Folder:
        last_time = 0
        time_list = []
        x_list = []
        y_list = []
        z_list = []
        file_list = []
        for i in range(start, end + 1):
            file_name_ = path + folder + '/' + str(i) + '_orientation.txt'
            with open(file_name_, 'r') as file_stream:
                for line in file_stream:
                    jump = False
                    pos_begin = line.find(": ")
                    pos_end = line[pos_begin + 2:].find(" ")
                    trans_string = line[pos_begin + 2: pos_end + pos_begin + 2]
                    time_list.append(last_time + float(trans_string))
                    if (len(x_list) > 0 and (float(trans_string) * 180 / math.pi - x_list[-1]) > 160):
#                        print float(trans_string) * 180 / math.pi
#                        print "last:" + str(x_list[-1])
                        jump = True
                    x_string = line[pos_end + pos_begin + 2 + 1:]
                    pos_begin = x_string.find(":")
                    pos_end = x_string[pos_begin + 2:].find(" ")
                    trans_string = x_string[pos_begin + 2: pos_end + pos_begin + 2]
                    x_list.append(float(trans_string)* 180/math.pi)
                    y_string = x_string[pos_end + pos_begin + 2 + 1:]
                    pos_begin = y_string.find(":")
                    pos_end = y_string[pos_begin + 2:].find(" ")
                    trans_string = y_string[pos_begin + 2: pos_end + pos_begin + 2]
                    y_list.append(float(trans_string)* 180/math.pi)
                    z_string = y_string[pos_end + pos_begin + 2 + 1:]
                    pos_begin = z_string.find(":")
                    pos_end = len(z_string) - 1
                    trans_string = z_string[pos_begin + 2: pos_end + pos_begin + 2]
                    z_list.append(float(trans_string)* 180/math.pi)
                    if (jump):
                        print "before" + str(x_list[-1])
                        x_list[len(x_list) - 1] = x_list[-1] - 180
                        print "x:" + str(x_list[-1])
                        y_list[len(y_list) - 1] = -y_list[-1] - 180
                        print "y:" + str(y_list[-1])
                        z_list[len(z_list) - 1] = z_list[-1] - 180
                        print "z:" + str(z_list[len(z_list) - 1])
                        jump = False
                last_time = time_list[len(time_list) - 1]
        x_spline_lists.append(x_list)
        y_spline_lists.append(y_list)
        z_spline_lists.append(z_list)
        time_spline_lists.append(time_list)

def calcDifferenceStandard():
    global x_spline_lists, y_spline_lists, z_spline_lists, time_spline_lists
    global x_standard, y_standard, z_standard, time_list_standard
    dist_lists =[]
    spline_counter = 0
    colors = ['r', 'g', 'b', 'y', 'k', 'm']
    labels = ['End', 'EndWi ', 'EndWiBe', 'Frei', 'FreiWi', 'FreiWiBe']
#    labels = ['Freiraum', 'Freiraum + Winkel',
#              'Freiraum + Winkel + Beschleunigung','test']
    for j in range(0, len(Folder)):
        dist_list = []
        spline_number = spline_counter
        for i in range(0,len(time_list_standard)):
            if (time_list_standard[i] > time_spline_lists[j][-1] or time_list_standard[i] > 20):
                break
            time_diff = abs(time_list_standard[i] - time_spline_lists[j][spline_number + 1])
            last_time_diff = abs(time_list_standard[i] - time_spline_lists[j][spline_number])
            while (time_diff <= last_time_diff):
                if spline_number == len(time_spline_lists[j]) - 1:
                    break
                spline_number = spline_number + 1
                last_time_diff = time_diff
                time_diff = abs(time_list_standard[i] - time_spline_lists[j][spline_number])
            if spline_number == len(time_spline_lists[j]) - 1:
                break
            if spline_number != 0:
                spline_number = spline_number - 1
            standard_point = np.array([x_standard[i], y_standard[i], z_standard[i]])
            spline_point = np.array([x_spline_lists[j][spline_number],
                                     y_spline_lists[j][spline_number],
                                     z_spline_lists[j][spline_number]])
#            quaternion.from_euler_angles(standard_point[0], standard_point[1], standard_point[2])
#            print "spline_number: "+str(spline_number)
            dist = np.linalg.norm(standard_point - spline_point)
            if dist > 100 and standard_point[0] > spline_point[0]:
                #print standard_point
                #print spline_point
                standard_point = np.array([180 - standard_point[0], -standard_point[1] - 180, standard_point[2] - 180])
                dist = np.linalg.norm(standard_point - spline_point)
            elif dist > 100 and standard_point[0] < spline_point[0]:
                spline_point = np.array([180 - spline_point[0], -spline_point[1] - 180, spline_point[2] - 180])
                dist = np.linalg.norm(standard_point - spline_point)
            if dist < 200:
                dist_list.append(dist)
        print labels[j] + ":" + str(mean(dist_list))
        print labels[j] + " std_dev:" + str(std(dist_list))
        dist_lists.append(dist_list)
        length_diff = len(time_list_standard) - len(dist_list)
        plot(time_list_standard[0:len(time_list_standard)-length_diff], dist_list, color=colors[j], linewidth=4.0, label=labels[j])
    plt.legend(loc='upper right',fontsize='24')
    plt.title('Abweichung des rotatorischen Anteils der lokalen Pose zum Google Cartographer', fontsize='30')
    plt.ylabel('rotatorische Abweichung in Grad', fontsize='24')
    plt.xlabel('t in s', fontsize='24' ,weight='bold')
    plt.grid()
    plt.tick_params(labelsize=24)






if __name__ == '__main__':
    start_var = input("Enter splinenumber for start: ")
    end_var = input("Enter splinenumber for end: ")
    read_standard_params()
    read_spline_params(int(start_var), int(end_var))
    calcDifferenceStandard()
    show()
