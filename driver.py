import pandas as pd

from preprocessing import get_state_data, get_daily_data, remove_outliers

# States allocates: Connecticut (CT) and Florida (FL)
if __name__ == "__main__":
	# Mandatory Task 1: To clean the given dataset
	covid_cases_data_path = './dataset/United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv'

	states_data = get_state_data(filename=covid_cases_data_path,
								 states=['CT', 'FL'],
								 cols=['submission_date', 'state', 'tot_cases', 'tot_death'])

	daily_data = get_daily_data(states_data)

	cleaned_data = remove_outliers(daily_data)
