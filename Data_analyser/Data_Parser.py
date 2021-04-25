from Plotting.country_wise_plot import *
from Utilities.utils import *
from Plotting.daily_data_plot import *
from Plotting.User_Room_Change_Analysis import *

pd.options.mode.chained_assignment = None


def parse_data(data):
    data_values = pd.read_csv(data, delimiter=',')
    return data_values


def get_country_data(df):
    df = get_total_customers(df)
    req_country_data_cols = df[["hotel", "arrival_date_year", "arrival_date_month", "country", "total_customers", "arrival_date_day_of_month"]]
    transformed_country_data = req_country_data_cols.groupby(['arrival_date_year', 'arrival_date_month', 'country', 'hotel']).sum().reset_index()
    entire_transformed_country_data = req_country_data_cols.groupby(
        ['arrival_date_year', 'arrival_date_month', 'country']).sum().reset_index()

    # Get the Unique Years and Month to find the top countries
    #unique_years, unique_months = get_unique_year_month(transformed_country_data)

    #top_country = get_peak_country_name(transformed_country_data, unique_years, unique_months)

    # Get the data according to the top countries
    prt_top_country_data_city_hotel = transformed_country_data.loc[(transformed_country_data["country"] == 'PRT') & (transformed_country_data["hotel"] == CITY_HOTEL_NAME)]
    prt_top_country_data_resort_hotel = transformed_country_data.loc[
        (transformed_country_data["country"] == 'PRT') & (transformed_country_data["hotel"] == RESORT_HOTEL_NAME)]
    prt_top_country_data = entire_transformed_country_data.loc[(entire_transformed_country_data["country"] == 'PRT')]

    #top_country_data = transformed_country_data.loc[(transformed_country_data["country"] == top_country)]

    # Sort using the Month column to Plot the data
    prt_top_country_data_city_hotel = sort_month_column(prt_top_country_data_city_hotel)
    prt_top_country_data_resort_hotel = sort_month_column(prt_top_country_data_resort_hotel)
    prt_top_country_data = sort_month_column(prt_top_country_data)
    col_to_plot = 4
    plot_line_graph_to_get_country_trend(prt_top_country_data, prt_top_country_data_city_hotel, prt_top_country_data_resort_hotel, col_to_plot)


def get_user_booking_data(df):
    req_user_data_cols = df[["arrival_date_year", "arrival_date_month", "country", "reserved_room_type", "assigned_room_type"]]
    req_user_data_cols['perfectly_allocated'] = np.where((req_user_data_cols['reserved_room_type'] == req_user_data_cols['assigned_room_type']), 0, 1)
    transformed_country_data = req_user_data_cols.loc[req_user_data_cols.perfectly_allocated == 1].groupby(
        ['arrival_date_year', 'arrival_date_month', 'country']).count().reset_index()

    # Get the Unique Years and Month to find the top countries
    unique_years, _ = get_unique_year_month(transformed_country_data)
    for year in unique_years:
        year_wise_report = transformed_country_data.loc[(transformed_country_data['arrival_date_year'] == year) &
        (transformed_country_data['country'] == 'PRT')]
        sorted_transformed_country_data = year_wise_report.sort_values(year_wise_report.columns[-1], ascending=False)
        #plot_number_of_user_rooms_changed(sorted_transformed_country_data.iloc[:5, :], year)
        plot_number_of_user_rooms_changed(year_wise_report, year)


def get_day_wise_peak_season_data(df):
    # This analysis is performed on PRT, ESP and ITA countries
    df = get_total_customers(df)
    req_country_data_cols = df[
        ["arrival_date_year", "arrival_date_month", "country", "total_customers", "arrival_date_day_of_month"]]
    transformed_country_data = req_country_data_cols.groupby(
        ['arrival_date_year', 'arrival_date_month', 'country', 'arrival_date_day_of_month']).sum().reset_index()

    top_country = SPAIN
    # Get the data according to the top countries
    top_country_data = transformed_country_data.loc[(transformed_country_data["country"] == top_country) &
                                                    ((transformed_country_data["arrival_date_month"] == 'August') |
                                                     (transformed_country_data["arrival_date_month"] == 'July'))]

    # Sort using the Month column to Plot the data
    top_country_data_for_plotting = sort_month_column_for_daily_data(top_country_data)
    col_to_plot = 4
    plot_line_graph_to_get_daily_trend(top_country_data_for_plotting, col_to_plot)
