from typing import Dict, Any, List
import pandas as pd


def get_state_data(filename: str, states: List[str], remove_nan: bool = True):
	data_df = pd.read_csv(filename)
	states_data = []
	for state in states:
		state_data = data_df.loc[data_df['state'] == state]
		if remove_nan:
			state_data = state_data.dropna()
		states_data.append(state_data)
	return states_data


def get_daily_data(data, remove_nan=True):
	return 0


def remove_outliers():
	return 0