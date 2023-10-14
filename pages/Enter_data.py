import streamlit as st
import pandas as pd
import numpy as np

# for k, v in st.session_state.items():
#     st.session_state[k] = v

# for key in st.session_state:
# 	st.session_state[key] = st.session_state[key]

"Enter your data here and view a quick breakdown."

preview,view = st.tabs(["Preview","View"])


with st.sidebar:
	"Upload your data here. Note that the following MUST be observed:"
	"1. All files must be in .csv format"
	"2. All dates must be in YYYY-MM-DD format"
	"3. Data columns must be ordered as follows:"
	# Try to move the formatting template over a bit? Hard to align with the list
	"Date | Y | X1 | X2 | X3 | etc."

	timescale = st.selectbox("Data timescale", ("Annually","Monthly","Daily"))

	# Add file input
	# Should we allow the upload of multiple data sets?
	data = st.file_uploader("Time series data", type=["csv"])

	# If no data is uploaded at first 
	if data is not None:
		try:
			st.session_state['user_data'] = pd.read_csv(data)

			# Check for errors in here?
			# Date: dates in YYYY-MM-DD; then check that timescale is ok
			# Columns: floating point only (integer only?)

		except pd.errors.EmptyDataError:
			st.session_state['user_data'] = "File is empty! Please try uploading again and ensure proper formatting."

		# Check that the data is formatted correctly
		# 1. Read the first column and ensure it is YYYY-MM-DD
		# 	 with proper dates only (?)
		# 2. Ensure remaining columns are floating-point numbers (or integers?)
		# 3. If all goes well, set st.session_state['user_data'] to the data that was inputted; otherwise set it to an error message



with preview:
	# Check errors here
	# Only execute this if the type is not string, since only then can we access columns 
	if type(st.session_state['user_data']) is not str:
		if timescale == 'Annually':
			pass
		elif timescale == 'Monthly':
			pass
		elif timescale == 'Daily':
			pass

	st.session_state['user_data']
