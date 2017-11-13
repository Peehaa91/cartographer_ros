#!/usr/bin/python
from pylab import *
Folder='Treppe_free_space'
path = '/home/schnattinger/.ros/nurbs/standard/' + Folder


def draw_trans():
    time_list = []
    last_time = 0
    x_acc = 0
    y_acc = 0
    z_acc = 0
    x_list = []
    y_list = []
    z_list = []
    file_list = []
    file_name_ = path + '/standard_trans_.txt'
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

def draw_angles():
    time_list = []
    last_time = 0
    x_list = []
    y_list = []
    z_list = []
    file_list = []
    jump = False
    file_name_ = path + '/' + '/standard_orientation_.txt'
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
            if (len(x_list) > 0 and abs(float(trans_string) * 180 / math.pi - x_list[len(x_list) - 1]) > 170):
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
                x_list[len(x_list)-1] = x_list[len(x_list)-1] -180
                y_list[len(y_list) - 1] = -y_list[len(y_list) - 1] - 180
                z_list[len(z_list) - 1] = z_list[len(z_list) - 1] - 180
                jump = False
            last_time = time_list[len(time_list) - 1]
    fig = plt.figure()
    fig.canvas.set_window_title(Folder)
    ax = fig.add_subplot(3, 1, 1)
    plot(time_list, x_list, 'r')
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
    draw_trans()
    draw_angles()
    show()