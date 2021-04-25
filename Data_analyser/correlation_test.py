import numpy as np
from scipy.stats import pearsonr, spearmanr
import seaborn as sn
import matplotlib.pyplot as plt
from pylab import savefig


def get_correlation_btn_lead_time_and_cancelled(df):
    coor_data = df[["lead_time", "days_in_waiting_list", "is_canceled", "arrival_date_year"]]
    coor_data = coor_data[coor_data.lead_time != 0]
    coor_data = coor_data.loc[(coor_data["arrival_date_year"] == 2017)]
    coor_data = coor_data.drop('arrival_date_year', 1)
    coor_data.columns = ['leadTime', 'waitingDays', 'isCanceled']
    corrMatrix = coor_data.corr(method='spearman')
    svm = sn.heatmap(corrMatrix, annot=True, cmap='coolwarm', linecolor='white', linewidths=1)
    figure = svm.get_figure()
    figure.savefig('heat_map_2017_corr.png', dpi=400)
