from typing import Dict, Any, List
import pandas as pd


def get_state_data(filename: str, states: List[str], cols: List[str], remove_nan: bool = True):
	"""
	Select data corresponding to each state
	Additionally, remove missing (nan) values

	:param filename: data path for full data
	:param states: states for which we want data
	:param cols: columns of interest
	:param remove_nan: flag to check if nan values need to be removed

	:return: List[dataframe]: data corresponding to each state
	"""
	data_df = pd.read_csv(filename)
	states_data = []
	for state in states:
		state_data = data_df.loc[data_df['state'] == state]
		state_data_cols = state_data[cols]
		total_rows = state_data_cols.shape[0]
		if remove_nan:
			state_data_cols = state_data_cols.dropna()
			total_rows_after_nan_removal = state_data_cols.shape[0]
			print("State: {} rows with missing values: {}".format(state, total_rows - total_rows_after_nan_removal))
		states_data.append(state_data_cols)
	return states_data


def get_daily_data(data):
	return 0


def remove_outliers():
	return 0