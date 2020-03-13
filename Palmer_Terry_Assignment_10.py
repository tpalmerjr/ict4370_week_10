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


    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    data = [float(stock['current_value']) for stock in pop_data]
    symbols = [stock['symbol'] for stock in pop_data]

    def func(pct, allvals):
        print(allvals)
        print(pct)
        absolute = float(pct/100.*np.sum(allvals))
        print(absolute)
        return "${:.2f}".format(absolute)
        # return "{:.1f}%\n(${})".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

    ax.legend(wedges, symbols,
            title="Ingredients",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Matplotlib bakery: A pie")

    plt.show()

    # # provide dictionary variable to hold stock data by symbol
    # # provide list variable to hold stock symbols for the legend
    # stock_data_by_symbol = {}
    # stock_symbols = []

    # # loop through the json data and add stock info to dictionary by stock symbol
    # # append dates to date list and prices to price list per stock symbol
    # for pop_dict in pop_data:
    #     if not pop_dict['Symbol'] in stock_data_by_symbol:
    #         stock_data_by_symbol[pop_dict['Symbol']] = {
    #             'dates': [],
    #             'price': [],
    #         }
    #         stock_symbols.append(pop_dict['Symbol'])

    #     stock_data_by_symbol[pop_dict['Symbol']]['dates'].append(datetime.strptime(pop_dict['Date'], "%d-%b-%y"))
    #     stock_data_by_symbol[pop_dict['Symbol']]['price'].append(int(float(pop_dict['Close'])))

    # # Plot data.
    # # Create a figure for the plot
    # fig = plt.figure(dpi=128, figsize=(10, 6))

    # # loop through the stock data by symbol to plot
    # # the data as a line on the chart per symbol
    # for sym, stock in stock_data_by_symbol.items():
    #     plt.plot(stock['dates'], stock['price'])

    # # Add a title, xlabel, ylabel, and legend to the chart
    # plt.title("Stock Prices by Date", fontsize=24)
    # plt.xlabel("Date", fontsize=14)
    # fig.autofmt_xdate()
    # plt.ylabel("Price", fontsize=14)
    # plt.legend(stock_symbols, loc='upper left')

    # #show the chart
    # plt.show()


    # # Plot total price by date
    # # saving to .png file.
    # # provide dictionary variable to hold stock data by date
    # # provide list variable to hold stock dates
    # # provide list variable to hold stock prices
    # stock_data_by_date = {}
    # stock_dates = []
    # stock_price = []

    # # loop through the json data and add stock info to dictionary by stock date
    # # add the price by date together and save in the price attribute under the date
    # for pop_dict in pop_data:
    #     if not pop_dict['Date'] in stock_data_by_date:
    #         stock_data_by_date[pop_dict['Date']] = {
    #             'price': 0,
    #         }

    #     stock_data_by_date[pop_dict['Date']]['price'] = stock_data_by_date[pop_dict['Date']]['price'] + int(float(pop_dict['Close']))

    # # loop through the stock data by date and append the
    # # dates to the date list and the prices to the price list
    # for date, stock in stock_data_by_date.items():
    #     stock_dates.append(datetime.strptime(date, "%d-%b-%y"))
    #     stock_price.append(stock['price'])

    # # Plot data.
    # # Create a figure for the plot
    # fig = plt.figure(dpi=128, figsize=(10, 6))

    # # add a bar plot to the chart for the dates
    # # list and the prices list
    # plt.bar(stock_dates, stock_price)

    # # Add a title, xlabel, and ylabel to the chart
    # plt.title("Total Stock Price by Date", fontsize=24)
    # plt.xlabel("Date", fontsize=14)
    # fig.autofmt_xdate()
    # plt.ylabel("Price", fontsize=14)

    # # save the chart to .png file
    # plt.savefig('Palmer_Terry_Assignment_8.png')

except FileNotFoundError:
    print('The file "' + file_name +
          '" was not found or could not be opened for output.')
except Exception as e:
    print('An error occurred: ', e)
