'''
Terry Palmer
03/13/2020

Stock Current Value Pie Chart

This program will read the stock data from a json file.
It will then parse the data into into a list containing
current values and a list containing symbols. It will then
create the plot for the pie chart using matplotlib. The chart
will have a title as well as labels for each wedge containing
the symbol and price.
'''

import json
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt


# Load the data into a list.
file_name = 'Stocks.json'

try:
    # Open the json file to be processed
    # load the json data once opened
    with open(file_name) as f:
        pop_data = json.load(f)

    # Create the data array of the current price for each stock
    data = [float(stock['current_value']) for stock in pop_data]
    # Create an array containing the symbols for each stock used for labels
    symbols = [stock['symbol'] for stock in pop_data]

    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))

    # wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)
    wedges, texts = ax.pie(data, startangle=60)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    # create the labels for each wedge
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(symbols[i] + ' - $' + str(data[i]), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

    # Add a title to the chart
    ax.set_title("Stocks: Current Value")

    # Display the chart
    plt.show()

except FileNotFoundError:
    print('The file "' + file_name +
          '" was not found or could not be opened for output.')
except Exception as e:
    print('An error occurred: ', e)
