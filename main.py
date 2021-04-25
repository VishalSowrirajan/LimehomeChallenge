from Data_analyser.Data_Parser import *
from Data_analyser.correlation_test import get_correlation_btn_lead_time_and_cancelled


def main():
    parsed_data = parse_data(DATASET_PATH)
    if GET_COUNTRY_PATTERNS:
        get_country_data(parsed_data)
    if GET_DAY_WISE_COUNTRY_TREND:
        get_day_wise_peak_season_data(parsed_data)
    if GET_USER_BOOKING_DATA:
        get_user_booking_data(parsed_data)
    if GET_CORRELATION:
        get_correlation_btn_lead_time_and_cancelled(parsed_data)
    # send that variable to correlation class and return the coorelation between the two variables


if __name__ == '__main__':
    main()