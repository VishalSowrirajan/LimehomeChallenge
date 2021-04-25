import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib import pyplot
from scipy.ndimage.filters import gaussian_filter1d


def plot_line_graph_to_get_country_trend(country_wise_data1, country_wise_data2, country_wise_data3, y_axis_col):

    x = country_wise_data2['Year_Month']
    y1 = country_wise_data1.iloc[:, y_axis_col].to_list()
    y2 = country_wise_data2.iloc[:, y_axis_col].to_list()
    y3 = country_wise_data3.iloc[:, y_axis_col].to_list()
    country_wise_data1['short_month_name'] = country_wise_data1['arrival_date_month'].astype(str).str[:3]
    y1 = gaussian_filter1d(y1, sigma=0.2)
    y2 = gaussian_filter1d(y2, sigma=0.2)
    y3 = gaussian_filter1d(y3, sigma=0.2)
    x_ticks = country_wise_data1.iloc[:, -1].to_list()

    plt.title('PRT - City vs Resort Hotel Month-Wise Trend')
    plt.xlabel('Months')

    plt.ylabel('Number of Customers')
    plt.xticks(range(0, len(x_ticks)), x_ticks)

    plt.axvspan(0, 6, facecolor='#A8A8A8', alpha=0.5, label='2015')
    plt.axvspan(6, 18, facecolor='#CC9999', alpha=0.5, label='2016')
    plt.axvspan(18, 26, facecolor='#FFCC66', alpha=0.5, label='2017')

    plt.tick_params(axis='x', which='major', labelsize=10, rotation=90)
    #plt.plot(x.iloc[:7], y1[:7], linewidth=1, linestyle='--', color='blue', marker='.', label='PRT_Overall')
    #plt.plot(x.iloc[6:19], y1[6:19], linewidth=1, linestyle='--', color='blue', marker='.')
    #plt.plot(x.iloc[18:], y1[18:], linewidth=1, linestyle='--', color='blue', marker='.')

    plt.plot(x.iloc[:7], y2[:7], linewidth=1, linestyle='--', color='red', marker='.', label='PRT_City')
    plt.plot(x.iloc[6:19], y2[6:19], linewidth=1, linestyle='--', color='red', marker='.')
    plt.plot(x.iloc[18:], y2[18:], linewidth=1, linestyle='--', color='red', marker='.')

    plt.plot(x.iloc[:7], y3[:7], linewidth=1, color='purple', marker='.', label='PRT_Resort')
    plt.plot(x.iloc[6:19], y3[6:19], linewidth=1, color='purple', marker='.')
    plt.plot(x.iloc[18:], y3[18:], linewidth=1, color='purple', marker='.')

    #plt.legend(loc = "upper left")
    plt.legend()
    plt.show()