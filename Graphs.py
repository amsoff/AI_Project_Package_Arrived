import pandas as pd
import csv
import Constants
from ast import literal_eval
import matplotlib.pyplot as plt
import numpy as np

files = ["output_gen1.csv", "output_gen2.csv", "output_gen3.csv"]
colors = ['r', 'b', 'g']


def string_arr_to_int(arr):
    """
    String arrat in csv file to inr array
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
    for i,f in enumerate(files):
        data = pd.read_csv(f)
        data = pd.DataFrame(data)
        time_arr = []
        for index, row in data.iterrows():
            time_arr.append((row[Constants.MONEY], row[Constants.TIME]))
        time_arr = sorted(time_arr, key=lambda x: x[0])
        plot_data(time_arr, colors[i])
    plt.xlabel('Money')
    plt.ylabel('Time in Seconds')
    plt.title('Running time as function of money:')
    plt.show()


def compare_expended_nodes_money():
    """
    Plots the average number of expended nodes vs amount of money
    :return:
    """
    for i,f in enumerate(files):
        data = pd.read_csv(f)
        data = pd.DataFrame(data)
        time_arr = []
        for index, row in data.iterrows():
            time_arr.append((row[Constants.MONEY], np.average(string_arr_to_int(row[Constants.EXPANDED]))))
        time_arr = sorted(time_arr, key=lambda x: x[0])
        plot_data(time_arr, colors[i])
    plt.xlabel('Money')
    plt.ylabel('Number of expended nodes in average in round')
    plt.title('Expended nodes as function of money:')
    plt.show()


def compare_turns_money():
    """
    Plots turns per game vs amount of money
    :return:
    """
    for i,f in enumerate(files):
        data = pd.read_csv(f)
        data = pd.DataFrame(data)
        time_arr = []
        for index, row in data.iterrows():
            time_arr.append((row[Constants.MONEY], row[Constants.TURNS]))
        time_arr = sorted(time_arr, key=lambda x: x[0])
        plot_data(time_arr, colors[i])
    plt.xlabel('Money')
    plt.ylabel('Number of Turns in the game')
    plt.title('Turns as function of money:')
    plt.show()


def connectpoints(x,y,p1,p2, color):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2], color)


def plot_data(data, color):
    x = [d[0] for d in data]
    y = [d[1] for d in data]
    plt.plot(x,y, '%so' % color)
    for i in range(0, len(x) - 1):
        connectpoints(x, y, i, i+1, '%s-' % color)


def compare_average_optimi():
    """
    Comparing 4 parameters: time, total expended nodes, turns, maximum of expended nodes, comparing between
    the average palyer and the optimistic player for 1500 and 300 (amount of money)
    """
    labels = ['Time (1500)', 'Turns (1500)', 'Average Nodes (1500)', 'Max Nodes (1500)',
              'Time (300)', 'Turns (300)', 'Average Nodes (300)', 'Max Nodes (300)']
    max_expanded = 3
    loc_dic = {Constants.TIME: 0, Constants.TURNS: 1, Constants.EXPANDED: 2}
    f = pd.read_csv(Constants.FILE)
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
    ax.set_title('Comparison of the two players:')
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


compare_time_money()
compare_average_optimi()
compare_expended_nodes_money()
compare_turns_money()
