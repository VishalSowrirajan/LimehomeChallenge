import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot


def plot_bar_graph_for_user_data(country_wise_data):

    x = country_wise_data['Year_Month']
    y = country_wise_data.iloc[:, 3].to_list()
    country_wise_data['short_month_name'] = country_wise_data['arrival_date_month'].astype(str).str[:3]
    x_ticks = country_wise_data.iloc[:, -1].to_list()

    plt.title('Spain Booking Year-Wise Trend')
    plt.xlabel('Months')

    plt.ylabel('Number of Customers')
    plt.xticks(range(0, len(x_ticks)), x_ticks)

    plt.axvspan(0, 6, facecolor='#A8A8A8', alpha=0.5, label='2015')
    plt.axvspan(6, 18, facecolor='#CC9999', alpha=0.5, label='2016')
    plt.axvspan(18, 26, facecolor='#FFCC66', alpha=0.5, label='2017')

    plt.tick_params(axis='x', which='major', labelsize=10, rotation=90)
    plt.plot(x.iloc[:7], y[:7], linewidth=1, linestyle='--', color='red', marker='.')
    plt.plot(x.iloc[6:19], y[6:19], linewidth=1, color='green', marker='.')
    plt.plot(x.iloc[18:], y[18:], linewidth=1, linestyle='--', color='purple', marker='.')
    plt.scatter(x, y)
    plt.legend()
    plt.show()