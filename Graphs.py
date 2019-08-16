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


def compare_average_optimi():
    """
    Comparing 4 parameters: time, total expanded nodes, turns, maximum of expanded nodes. Comparison between
    the average player and the optimistic player for 1500 and 300 (amounts of money)
    """
    labels = ['Time (1500)', 'Turns (1500)', 'Average Nodes (1500)', 'Max Nodes (1500)',
              'Time (300)', 'Turns (300)', 'Average Nodes (300)', 'Max Nodes (300)']
    max_expanded = 3
    loc_dic = {Constants.TIME: 0, Constants.TURNS: 1, Constants.EXPANDED: 2}
    title_text = ["using optimization", "without using optimization"]
    file_name = [Constants.FILE_average_vs_optimi, Constants.FILE_average_vs_optimi_NO_OPT]
    for i in range(2):
        f = pd.read_csv(file_name[i])
        data = pd.DataFrame(f)
        avg_arr = [0] * 8
        opt_arr = [0] * 8
        for index, row in data.iterrows():
            if row[Constants.TYPE] == Constants.OPTIMISTIC and row[Constants.MONEY] == 1500:
                opt_arr[loc_dic[Constants.TIME]] = round(row[Constants.TIME], 2)
                opt_arr[loc_dic[Constants.TURNS]] = row[Constants.TURNS]
                opt_arr[loc_dic[Constants.EXPANDED]] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                opt_arr[max_expanded] = np.max(string_arr_to_int(row[Constants.EXPANDED]))
            elif row[Constants.TYPE] == Constants.OPTIMISTIC and row[Constants.MONEY] == 300:
                opt_arr[loc_dic[Constants.TIME] + 4] = round(row[Constants.TIME], 2)
                opt_arr[loc_dic[Constants.TURNS] + 4] = row[Constants.TURNS]
                opt_arr[loc_dic[Constants.EXPANDED] + 4] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                opt_arr[max_expanded + 4] = np.max(string_arr_to_int(row[Constants.EXPANDED]))

            elif row[Constants.TYPE] == Constants.AVERAGE and row[Constants.MONEY] == 1500:
                avg_arr[loc_dic[Constants.TIME]] = round(row[Constants.TIME], 2)
                avg_arr[loc_dic[Constants.TURNS]] = row[Constants.TURNS]
                avg_arr[loc_dic[Constants.EXPANDED]] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                avg_arr[max_expanded] = np.max(string_arr_to_int(row[Constants.EXPANDED]))
            elif row[Constants.TYPE] == Constants.AVERAGE and row[Constants.MONEY] == 300:
                avg_arr[loc_dic[Constants.TIME] + 4] = round(row[Constants.TIME], 2)
                avg_arr[loc_dic[Constants.TURNS] + 4] = row[Constants.TURNS]
                avg_arr[loc_dic[Constants.EXPANDED] + 4] = round(np.average(string_arr_to_int(row[Constants.EXPANDED])), 2)
                avg_arr[max_expanded + 4] = np.max(string_arr_to_int(row[Constants.EXPANDED]))

        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, avg_arr, width, label='Average')
        rects2 = ax.bar(x + width / 2, opt_arr, width, label='Optimistic')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_xlabel('Parameters + Amount of money')
        ax.set_ylabel('Values')
        ax.set_title("Comparison of the two players %s" % title_text[i])
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontdict={'fontsize': 7})
        ax.legend()

        autolabel(rects1, ax)
        autolabel(rects2, ax)
        fig.tight_layout()
        plt.show()
        # plt.savefig('avg_vs_opt.png')



def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 3, height),
                    xytext=(0, 1),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


# compare_time_money()
# compare_expanded_nodes_money()
# compare_turns_money()
# calc_optimization_improvement()
compare_max_sum_heuristics_time()
compare_max_sum_heuristics_expanded_average()
compare_max_sum_heuristics_expanded_max()