import pandas as pd
import csv
import Constants
from ast import literal_eval
import matplotlib.pyplot as plt
import numpy as np


def string_arr_to_int(arr):
    int_arr = []
    arr = arr.replace('[', '').replace(']', '').replace('\'', '').split(',')
    for a in arr:
        int_arr.append(int(a))
    return np.array(int_arr)


def compare_time_money():
    f = pd.read_csv(Constants.FILE)
    data = pd.DataFrame(f)
    time_arr = []
    for index, row in data.iterrows():
        time_arr.append((row[Constants.MONEY], row[Constants.TIME]))


def compare_expended_nodes_money():
    f = pd.read_csv(Constants.FILE)
    data = pd.DataFrame(f)
    time_arr = []
    for index, row in data.iterrows():
        time_arr.append((row[Constants.MONEY], row[Constants.TIME]))


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

# compare_time_money()
compare_average_optimi()
