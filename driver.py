import pandas as pd

from preprocessing import get_state_data, get_daily_cases_data, remove_outliers

# States allocates: Connecticut (CT) and Florida (FL)
if __name__ == "__main__":
    # Mandatory Task 1: To clean the given dataset for cases
    covid_cases_data_path = './dataset/United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv'

    ct_state_cases_data, fl_state_cases_data = get_state_data(filename=covid_cases_data_path,
                                                              states=['CT', 'FL'],
                                                              location_col_name='state',
                                                              cols=['submission_date', 'state',
                                                                    'tot_cases', 'tot_death',
                                                                    'new_case', 'new_death'])

    ct_daily_cases_data = get_daily_cases_data(ct_state_cases_data,
                                               location_col_name='state',
                                               date_col_name='submission_date',
                                               non_cumulative_cols=['new_case', 'new_death'],
                                               set_zero_for_negatives=True)
    fl_daily_cases_data = get_daily_cases_data(fl_state_cases_data,
                                               location_col_name='state',
                                               date_col_name='submission_date',
                                               non_cumulative_cols=['new_case', 'new_death'],
                                               set_zero_for_negatives=True)

    ct_daily_cleaned_data = remove_outliers(ct_daily_cases_data)
    fl_daily_cleaned_data = remove_outliers(fl_daily_cases_data)

    # ct_daily_cleaned_data.to_csv('./processed/clean_ct_cases.csv')
    # fl_daily_cleaned_data.to_csv('./processed/clean_fl_cases.csv')

    # Mandatory Task 1: To clean the given dataset for vaccinations
    covid_vax_data_path = './dataset/COVID-19_Vaccinations_in_the_United_States_Jurisdiction.csv'
    ct_state_vax_data, fl_state_vax_data = get_state_data(filename=covid_vax_data_path,
                                                              states=['CT', 'FL'],
                                                              location_col_name='Location',
                                                              cols=['Date', 'Location',
                                                                    'Administered'])

    ct_daily_vax_data = get_daily_cases_data(ct_state_vax_data,
                                               location_col_name='Location',
                                               date_col_name='Date',
                                               non_cumulative_cols=[],
                                               set_zero_for_negatives=True)
    fl_daily_vax_data = get_daily_cases_data(fl_state_vax_data,
                                               location_col_name='Location',
                                               date_col_name='Date',
                                               non_cumulative_cols=[],
                                               set_zero_for_negatives=True)

    ct_daily_cleaned_vax_data = remove_outliers(ct_daily_vax_data,
                                                cols_to_consider=['Administered'])
    fl_daily_cleaned_vax_data = remove_outliers(fl_daily_vax_data,
                                                cols_to_consider=['Administered'])

    ct_daily_cleaned_vax_data.to_csv('./processed/clean_ct_vax.csv')
    fl_daily_cleaned_vax_data.to_csv('./processed/clean_fl_vax.csv')
