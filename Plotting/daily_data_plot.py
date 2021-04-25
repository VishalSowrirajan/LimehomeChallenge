import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib import pyplot
from scipy.ndimage.filters import gaussian_filter1d


def plot_line_graph_to_get_daily_trend(country_wise_data, y_axis_col):

    x = country_wise_data['Year_Month']
    y = country_wise_data.iloc[:, y_axis_col].to_list()
    country_wise_data['short_month_name'] = country_wise_data['Year_Month'].astype(str).str[:2]
    x_ticks = country_wise_data.iloc[:, -1].to_list()

    ysmoothed = gaussian_filter1d(y, sigma=0.9)
    #plt.plot(x, ysmoothed)
    #plt.show()

    plt.title('Spain Daily trend in Peak Seasons')
    plt.xlabel('Days in specified month')

    plt.ylabel('Number of Customers')
    #plt.xticks(range(0, len(x_ticks)), x_ticks)

    #for i, txt in enumerate(y):
    #    plt.annotate(txt, (x.iloc[i], y[i]))

    #plt.plot(x.iloc[:10].astype(str), ysmoothed[:10], linewidth=1, color='blue', marker='.')
    #plt.plot(x.iloc[9:33].astype(str), ysmoothed[9:33], linewidth=1, linestyle='--', color='red', marker='.')
    #plt.plot(x.iloc[32:63].astype(str), ysmoothed[32:63], linewidth=1, color='blue', marker='.')
    #plt.plot(x.iloc[62:94].astype(str), ysmoothed[62:94], linewidth=1, linestyle='--', color='red', marker='.')
    #plt.plot(x.iloc[93:124].astype(str), ysmoothed[93:124], linewidth=1, color='blue', marker='.')
    #plt.plot(x.iloc[123:].astype(str), ysmoothed[123:], linewidth=1, linestyle='--', color='red', marker='.')

    #plt.tick_params(axis='x', which='major', labelsize=10, rotation=90)
    plt.xticks([])

    plt.plot(x.iloc[:32].astype(str), ysmoothed[:32], linewidth=1, color='blue', marker='.')
    plt.plot(x.iloc[31:63].astype(str), ysmoothed[31:63], linewidth=1, linestyle='--', color='red', marker='.')
    plt.plot(x.iloc[62:94].astype(str), ysmoothed[62:94], linewidth=1, color='blue', marker='.')
    plt.plot(x.iloc[93:124].astype(str), ysmoothed[93:124], linewidth=1, linestyle='--', color='red', marker='.')
    plt.plot(x.iloc[123:156].astype(str), ysmoothed[123:156], linewidth=1, color='blue', marker='.')
    plt.plot(x.iloc[155:].astype(str), ysmoothed[155:], linewidth=1, linestyle='--', color='red', marker='.')

    #plt.plot(x.iloc[:10].astype(str), ysmoothed[:10], linewidth=1, color='blue', marker='.')
    #plt.plot(x.iloc[9:33].astype(str), ysmoothed[9:33], linewidth=1, linestyle='--', color='red', marker='.')
    #plt.plot(x.iloc[32:63].astype(str), ysmoothed[32:63], linewidth=1, color='blue', marker='.')
    #plt.plot(x.iloc[62:94].astype(str), ysmoothed[62:94], linewidth=1, linestyle='--', color='red', marker='.')
    #plt.plot(x.iloc[93:124].astype(str), ysmoothed[93:124], linewidth=1, color='blue', marker='.')
    #plt.plot(x.iloc[123:].astype(str), ysmoothed[123:], linewidth=1, linestyle='--', color='red', marker='.')

    plt.axvspan(0, 31, facecolor='#8533ff', alpha=0.5, label='July 2015')
    plt.axvspan(31, 62, facecolor='#b3b3ff', alpha=0.5, label='August 2015')
    plt.axvspan(62, 93, facecolor='#8533ff', alpha=0.5, label='July 2016')
    plt.axvspan(93, 124, facecolor='#b3b3ff', alpha=0.5, label='August 2016')
    plt.axvspan(124, 155, facecolor='#8533ff', alpha=0.5, label='July 2017')
    plt.axvspan(155, 186, facecolor='#b3b3ff', alpha=0.5, label='August 2017')

    plt.legend()
    plt.show()
