from typing import Dict, Any, List
import pandas as pd


def get_state_data(filename: str, states: List[str], remove_nan: bool = True):
	"""
	Select data corresponding to each state
	Additionally, remove missing (nan) values

	:param filename: data path for full data
	:param states: states for which we want data
	:param remove_nan: flag to check if nan values need to be removed

	:return: List[dataframe]: data corresponding to each state
	"""
	data_df = pd.read_csv(filename)
	states_data = []
	for state in states:
		state_data = data_df.loc[data_df['state'] == state]
		if remove_nan:
			state_data = state_data.dropna()
		states_data.append(state_data)
	return states_data


def get_daily_data(data):
	return 0


def remove_outliers():
	return 0