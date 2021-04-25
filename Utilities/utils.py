import pandas as pd
from Utilities.Constants import *


def get_total_customers(df):
    df['total_customers'] = df['adults'] + df['children'] + df['babies']
    return df


def get_unique_year_month(df):
    unique_years = df['arrival_date_year'].unique()
    unique_months = df['arrival_date_month'].unique()
    return unique_years, unique_months


def get_peak_country_name(df, unique_years, unique_months):
    idx = 0
    for year in unique_years:
        for month in unique_months:
            year_month_country_data = df.loc[(df['arrival_date_year'] == year) & (df['arrival_date_month'] == month) & (df["hotel"] == HOTEL_NAME)]
            if year_month_country_data.empty:
                continue
            sorted_transformed_country_data = year_month_country_data.sort_values(year_month_country_data.columns[-2], ascending=False)
            if idx == 0:
                top_country = sorted_transformed_country_data.iloc[TOP_N_COUNTRY, -4]
                idx += 1
    return top_country


def sort_month_column(df):
    custom_dict = get_months_mapping()
    idx = df['arrival_date_month'].map(custom_dict)
    df['sort_month_order'] = pd.Series(idx)
    df['Year_Month'] = df.loc[:, "arrival_date_month"].astype(str) + ' ' + df.loc[:, "arrival_date_year"].astype(str)
    return df.sort_values(['arrival_date_year', 'sort_month_order'])


def sort_month_column_for_daily_data(df):
    custom_dict = get_months_mapping()
    idx = df['arrival_date_month'].map(custom_dict)
    df['sort_month_order'] = pd.Series(idx)
    df['Year_Month'] = df.loc[:, "arrival_date_day_of_month"].astype(str) + ' ' + df.loc[:, "arrival_date_month"].astype(str) + ' ' + df.loc[:, "arrival_date_year"].astype(str)
    return df.sort_values(['arrival_date_year', 'sort_month_order'])


def get_months_mapping():
    return {'January': 0, 'February': 1, 'March': 2, 'April': 3, 'May': 4, 'June': 5, 'July': 6, 'August': 7, 'September': 8, 'October': 9, 'November': 10, 'December': 11}
