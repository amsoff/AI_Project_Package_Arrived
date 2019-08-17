import pandas as pd
import csv
import Constants
from ast import literal_eval
import matplotlib.pyplot as plt
import numpy as np

files = ["output_gen1_sum.csv", "output_gen2_sum.csv", "output_gen3_sum.csv"]
files_heuristics = ["output_gen2_sum.csv", "output_gen2_max.csv"]
colors = ['r', 'b', 'g']


def string_arr_to_int(arr):
    """
    String array in csv file to int array
    :param arr: string array
    :return: int array
    """
    int_arr = []
    arr = arr.replace('[', '').replace(']', '').replace('\'', '').split(',')
    for a in arr:
        int_arr.append(int(a))
    return np.array(int_arr)


def compare_time_money():
    """
    Plots graph of money vs running time
    """
    time_arr = []
    for i, f in enumerate(files):
        data = pd.read_csv(f)
        data = pd.DataFrame(data)
        time_arr1 = []
        for index, row in data.iterrows():
            time_arr1.append((row[Constants.MONEY], row[Constants.TIME]))
        time_arr1 = sorted(time_arr1, key=lambda x: x[0])
        time_arr.append(time_arr1)

    time_arr = np.mean(time_arr, axis=0)
    plot_data(time_arr, colors[0])
    plt.xlabel('Money')
    plt.xticks([0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200])
    plt.ylabel('Time in Seconds')
    plt.title('Running time as function of money:')
    plt.show()


def compare_expanded_nodes_money():
    """
    Plots the average number of expanded nodes vs amount of money
    :return:
    """
    time_arr = []
    for i, f in enumerate(files):
        data = pd.read_csv(f)
        data = pd.DataFrame(data)
        time_arr1 = []
        for index, row in data.iterrows():
            time_arr1.append((row[Constants.MONEY], np.average(string_arr_to_int(row[Constants.EXPANDED]))))
        time_arr1 = sorted(time_arr1, key=lambda x: x[0])
        time_arr.append(time_arr1)

    time_arr = np.mean(time_arr, axis=0)
    plot_data(time_arr, colors[0])
    plt.xlabel('Money')
    plt.xticks([0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200])
    plt.ylabel('Number of expanded nodes in average in round')
    plt.title('expanded nodes as function of money:')
    plt.show()


def compare_max_sum_heuristics_expanded_average():
    for i, f in enumerate(files_heuristics):
        data = pd.read_csv(f)
        data = pd.DataFrame(data)
        time_arr = []
        for index, row in data.iterrows():
            time_arr.append((row[Constants.MONEY], np.average(string_arr_to_int(row[Constants.EXPANDED]))))
        time_arr = sorted(time_arr, key=lambda x: x[0])
        plot_data_legend(time_arr, colors[i], i)
    plt.xlabel('Money')
    plt.ylabel('Number of expanded nodes in average in round')
    plt.title('Average expanded nodes as function of money:')
    plt.show()


def compare_max_sum_heuristics_expanded_max():
    for i, f in enumerate(files_heuristics):
        data = pd.read_csv(f)
        data = pd.DataFrame(data)
        time_arr = []
        for index, row in data.iterrows():
            time_arr.append((row[Constants.MONEY], np.max(string_arr_to_int(row[Constants.EXPANDED]))))
        time_arr = sorted(time_arr, key=lambda x: x[0])
        plot_data_legend(time_arr, colors[i], i)
    plt.xlabel('Money')
    plt.ylabel('Number of maximum expanded nodes in round')
    plt.title('Max expanded nodes as function of money:')
    plt.show()


def compare_max_sum_heuristics_time():
    for i,f in enumerate(files_heuristics):
        data = pd.read_csv(f)
        data = pd.DataFrame(data)
        time_arr = []
        for index, row in data.iterrows():
            time_arr.append((row[Constants.MONEY], row[Constants.TIME]))
        time_arr = sorted(time_arr, key=lambda x: x[0])
        plot_data_legend(time_arr, colors[i], i)
    plt.xlabel('Money')
    plt.ylabel('Time in Seconds')
    plt.title('Running time as function of money:')
    plt.show()

def compare_turns_money():
    """
    Plots turns per game vs amount of money
    :return:
    """
    time_arr = []
    for i, f in enumerate(files):
        data = pd.read_csv(f)
        data = pd.DataFrame(data)
        time_arr1 = []
        for index, row in data.iterrows():
            time_arr1.append((row[Constants.MONEY], row[Constants.TURNS]))
        time_arr1 = sorted(time_arr1, key=lambda x: x[0])
        time_arr.append(time_arr1)

    time_arr = np.mean(time_arr, axis=0)
    plot_data(time_arr, colors[0])
    plt.xlabel('Money')
    plt.xticks([0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200])
    plt.ylabel('Number of Turns in the game')
    plt.title('Turns as function of money:')
    plt.show()

def calc_optimization_improvement():
    p, total = 0, 0
    for i, f in enumerate(files):
        data = pd.read_csv(f)
        data = pd.DataFrame(data)
        for index, row in data.iterrows():
            list1 = string_arr_to_int(row[Constants.EXPANDED])
            for l in list1:
                if l == 0:
                    p += 1
            total += len(list1)
    print(p / total)

def connectpoints(x, y, p1, p2, color):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1, x2], [y1, y2], color)


def plot_data(data, color):
    x = [d[0] for d in data]
    y = [d[1] for d in data]
    plt.plot(x, y, '%so' % color, label="Max heuristic")
    plt.legend()
    for i in range(0, len(x) - 1):
        connectpoints(x, y, i, i + 1, '%s-' % color)


def plot_data_legend(data, color, num):
    x = [d[0] for d in data]
    y = [d[1] for d in data]
    if num == 0:
        label = "Sum heuristic"
    else:
        label = "Max heuristic"
    plt.plot(x, y, '%so' % color, label=label)
    plt.legend()
    for i in range(0, len(x) - 1):
        connectpoints(x, y, i, i + 1, '%s-' % color)


def plot_average_optimi(avg_arr, opt_arr, labels, xlabel, title):
    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.bar(x - width / 2,avg_arr ,width, label='Average')
    ax2.bar(x + width / 2,opt_arr, width, label='Optimistic')
    # set the bbox for the text. Increase txt_width for wider text.
    txt_height = 0.04 * (plt.ylim()[1] - plt.ylim()[0])
    txt_width = 0.02 * (plt.xlim()[1] - plt.xlim()[0])
    # Get the corrected text positions, then write the text.
    text_positions = get_text_positions(x - width / 2,avg_arr, txt_width, txt_height)
    text_positions2 = get_text_positions(x + width / 2,opt_arr, txt_width, txt_height)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel('Values')
    # ax.set_title("time Comparison of the two players ")
    ax2.set_title(title)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels, fontdict={'fontsize': 7})
    ax2.legend(loc='upper left')

    text_plotter(x - width / 2,avg_arr, text_positions, ax2, txt_width, txt_height)
    text_plotter(x + width / 2,opt_arr, text_positions2, ax2, txt_width, txt_height)

    plt.show()


def compare_average_optimi():
    """
    Comparing 4 parameters: time, total expanded nodes, turns, maximum of expanded nodes. Comparison between
    the average player and the optimistic player for 1500 and 300 (amounts of money)
    """
    time_his_labels = ["Time (1500) Opt","Time (300) Opt","Time (1500) Not Opt","Time (300) Not Opt"]
    turns_his_labels = ["Turns (1500) Opt","Turns (300) Opt","Turns (1500) Not Opt","Turns (300) Not Opt"]
    average_nodes_his_labels = ["Average Nodes (1500) Opt","Average Nodes (300) Opt","Average Nodes (1500) Not Opt","Average Nodes (300) Not Opt"]
    max_nodes_his_labels = ["Max Nodes (1500) Opt","Max Nodes (300) Opt","Max Nodes (1500) Not Opt","Max Nodes (300) Not Opt"]
    f = pd.read_csv("output_players_and_optimizations.csv")
    data = pd.DataFrame(f)
    avg_arr_time  = [0] * 4
    opt_arr_time  = [0] * 4
    avg_arr_turns = [0] * 4
    opt_arr_turns = [0] * 4
    avg_arr_avg_node  = [0] * 4
    opt_arr_avg_node  = [0] * 4
    avg_arr_max_nodes = [0] * 4
    opt_arr_max_nodes = [0] * 4

    for index, row in data.iterrows():
        if row[Constants.TYPE] == Constants.OPTIMISTIC and row[Constants.MONEY] == 1500:
            if row[Constants.IS_OPTIMAL]:
                opt_arr_time[0] = row[Constants.TIME]
                opt_arr_turns[0] = row[Constants.TURNS]
                opt_arr_avg_node[0] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                opt_arr_max_nodes[0] = np.max(string_arr_to_int(row[Constants.EXPANDED]))
            else:
                opt_arr_time[2] = row[Constants.TIME]
                opt_arr_turns[2] = row[Constants.TURNS]
                opt_arr_avg_node[2] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                opt_arr_max_nodes[2] = np.max(string_arr_to_int(row[Constants.EXPANDED]))
        elif row[Constants.TYPE] == Constants.OPTIMISTIC and row[Constants.MONEY] == 300:
            if row[Constants.IS_OPTIMAL]:
                opt_arr_time[1] = row[Constants.TIME]
                opt_arr_turns[1] = row[Constants.TURNS]
                opt_arr_avg_node[1] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                opt_arr_max_nodes[1] = np.max(string_arr_to_int(row[Constants.EXPANDED]))
            else:
                opt_arr_time[3] = row[Constants.TIME]
                opt_arr_turns[3] = row[Constants.TURNS]
                opt_arr_avg_node[3] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                opt_arr_max_nodes[3] = np.max(string_arr_to_int(row[Constants.EXPANDED]))
        elif row[Constants.TYPE] == Constants.AVERAGE and row[Constants.MONEY] == 1500:
            if row[Constants.IS_OPTIMAL]:
                avg_arr_time[0] = row[Constants.TIME]
                avg_arr_turns[0] = row[Constants.TURNS]
                avg_arr_avg_node[0] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                avg_arr_max_nodes[0] = np.max(string_arr_to_int(row[Constants.EXPANDED]))
            else:
                avg_arr_time[2] = row[Constants.TIME]
                avg_arr_turns[2] = row[Constants.TURNS]
                avg_arr_avg_node[2] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                avg_arr_max_nodes[2] = np.max(string_arr_to_int(row[Constants.EXPANDED]))
        elif row[Constants.TYPE] == Constants.AVERAGE and row[Constants.MONEY] == 300:
            if row[Constants.IS_OPTIMAL]:
                avg_arr_time[1] = row[Constants.TIME]
                avg_arr_turns[1] = row[Constants.TURNS]
                avg_arr_avg_node[1] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                avg_arr_max_nodes[1] = np.max(string_arr_to_int(row[Constants.EXPANDED]))
            else:
                avg_arr_time[3] = row[Constants.TIME]
                avg_arr_turns[3] = row[Constants.TURNS]
                avg_arr_avg_node[3] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                avg_arr_max_nodes[3] = np.max(string_arr_to_int(row[Constants.EXPANDED]))

    plot_average_optimi(avg_arr_time,opt_arr_time,time_his_labels,
                        "time divided by optimize run and not",
                        "time comparison of two players")
    plot_average_optimi(avg_arr_turns, opt_arr_turns, turns_his_labels,
                        "turns divided by optimize run and not",
                        "number of turns comparison of two players")
    plot_average_optimi(avg_arr_avg_node, opt_arr_avg_node, average_nodes_his_labels,
                        "average expanded nodes per game divided by optimize run and not",
                        "average expanded nodes comparison of two players")
    plot_average_optimi(avg_arr_max_nodes, opt_arr_max_nodes, max_nodes_his_labels,
                        "highest expansions per game divided by optimize run and not",
                        "maximum number of expansions comparison of two players")


def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 3, height),
                    xytext=(0, 1),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')




def get_text_positions(x_data, y_data, txt_width, txt_height):
    a = zip(y_data, x_data)
    text_positions = y_data.copy()
    for index, (y, x) in enumerate(a):
        local_text_positions = [i for i in a if i[0] > (y - txt_height)
                                and (abs(i[1] - x) < txt_width * 2) and i != (y, x)]
        if local_text_positions:
            sorted_ltp = sorted(local_text_positions)
            if abs(sorted_ltp[0][0] - y) < txt_height:  # True == collision
                differ = np.diff(sorted_ltp, axis=0)
                a[index] = (sorted_ltp[-1][0] + txt_height, a[index][1])
                text_positions[index] = sorted_ltp[-1][0] + txt_height
                for k, (j, m) in enumerate(differ):
                    # j is the vertical distance between words
                    if j > txt_height * 2:  # if True then room to fit a word in
                        a[index] = (sorted_ltp[k][0] + txt_height, a[index][1])
                        text_positions[index] = sorted_ltp[k][0] + txt_height
                        break
    return text_positions


def text_plotter(x_data, y_data, text_positions, axis, txt_width, txt_height):
    for x, y, t in zip(x_data, y_data, text_positions):
        axis.text(x - txt_width, 1.01 * t, '%d' % int(y), rotation=0, color='blue')
        if y != t:
            axis.arrow(x, t, 0, y - t, color='red', alpha=0.3, width=txt_width * 0.1,
                       head_width=txt_width, head_length=txt_height * 0.5,
                       zorder=0, length_includes_head=True)


compare_average_optimi()
# compare_time_money()
# compare_expanded_nodes_money()
# compare_turns_money()
# calc_optimization_improvement()
# compare_max_sum_heuristics_time()
# compare_max_sum_heuristics_expanded_average()
# compare_max_sum_heuristics_expanded_max()