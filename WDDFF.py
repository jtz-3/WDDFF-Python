import streamlit as st
import pandas as pd
import numpy as np

# for k, v in st.session_state.items():
#     st.session_state[k] = v

# for key in st.session_state:
# 	st.session_state[key] = st.session_state[key]

st.title('Wavelet-Driven Data Forecasting Framework :droplet:')

st.header("Introduction")
"(We can put a blurb about how it works here, along with some headings)"



st.header("Details")
"(More stuff here)"

# Initialize session variable: user data
if 'user_data' not in st.session_state:
	st.session_state['user_data'] = "No data uploaded :pensive:"

# Initialize session variables: WDDFF parameters (can be altered later)
if 'lead_time' not in st.session_state:
	st.session_state['lead_time'] = 0

# "Lead time input: " 
# st.session_state.lead_time

# if 'lag_y' not in st.session_state:
# 	st.session_state['lag_y'] = 0

# if 'lag_x' not in st.session_state:
# 	st.session_state['lag_x'] = 0

# if 'nval' not in st.session_state:
# 	st.session_state['nval'] = 10

# if 'ntest' not in st.session_state:
# 	st.session_state[''] = 

# if 'wfm' not in st.session_state:
# 	st.session_state[''] = 

# if 'wt' not in st.session_state:
# 	st.session_state[''] = 

# if 'wavelet' not in st.session_state:
# 	st.session_state[''] = 

# if 'decomp_level' not in st.session_state:
# 	st.session_state[''] = 


st.session_state

# with tab1:
# 	with st.sidebar:
# 		"Test"