import streamlit as st
import pandas as pd
import numpy as np

# for k, v in st.session_state.items():
#     st.session_state[k] = v

# for key in st.session_state:
# 	st.session_state[key] = st.session_state[key]

results,visualize = st.tabs(["Prediction Results", "Visualize"])

# Remember to incorporate appropriate UPPER bounds on input

with st.sidebar:
	st.session_state.lead_time = st.number_input("Lead time", min_value=0, step=1)
	lag_y = st.number_input("Lag_Y", min_value=0, step=1)
	lag_x = st.number_input("Lag_X", min_value=0, step=1)
	nval = st.number_input("Number of validation samples", min_value=0, value=10)

	# Should it be called ntst, as in Shiny app?
	ntest = st.number_input("Number of test samples", min_value=0, value=10)

	# How can each selection be associated with a variable, 
	# 	as in Shiny app?
	wfm = st.selectbox("Wavelet-based forecasting method",
						("None","Single","Within","Across",
						 "Single-hybrid", "Within-hybrid","Across-hybrid"))

	wt = st.selectbox("Wavelet transform", ("à trous", "MODWT"))
	wavelet = st.selectbox("Wavelet scaling filter",
						   ("Haar", "Daubechies 1","Daubechies 2",
						   	"Fejér-Korovkin 4", "Daubechies 3", "Fejér-Korovkin 6",
						   	"Coiflet 1", "Daubechies 4", "symlet 4","Fejér-Korovkin 8",
						   	"Least asymmetric 8", "Daubechies 5" , "Least asymmetric 10", 
						   	"Daubechies 6", "symlet 6", "Coiflet 2", "Least asymmetric 12", 
						   	"Best-localized Daubechies"), index=2)

	decomp_level = st.number_input("Decomposition level", min_value=1, step=1)
	ivsm = st.selectbox("Input variable selection method", 
						("None", "BA", "RRF", "EA CMI HTC", "EA CMI TOL", 
						 "KNN CMI TOL", "KNN CMI BI TOL", "PMIS BIC", "PCIS BIC"))

	ddm = st.selectbox("Data-driven model", 
					   ("sparse p-th order Volterra series model",
                        "k nearest neighbours regression",
                         "general regression neural network",
                         "regularized random forests regression",
                         "eXtreme gradient boosting"))

	# Define these variables as placeholders for the conditional statement below
	order = 1
	nneighbours = 2
	ntrees = 128

	# Depending on the data-driven model selected, add DDM parameters
	# NOTE: whenever a different DDM is selected, the values of order, nneighbours, and ntrees
	# 	default back to the values defined above.
	if (ddm == "sparse p-th order Volterra series model"):
		order = st.number_input("Model order", value=1, min_value=1, max_value=3)
	elif (ddm == "k nearest neighbours regression"):
		nneighbours = st.number_input("Number of nearest neighbours", value=2, min_value=2)
	elif (ddm == "regularized random forests regression"):
		ntrees = st.number_input("Number of trees in forest", value=128, min_value=128)

	# Do True, False here need to be replaced with strs?
	scale_inputs = st.radio("Scale inputs", (True,False))
	scale_target = st.radio("Scale target", (True,False))
	cutoff0 = st.radio("Cutoff", (True,False))

	# Is this button necessary if the app refreshes every time there's a change?
	# 	Is there some way to suspend that feature?
	train = st.button("Train",use_container_width=True)

# For testing
# "Order: ", order
# "Nneighbours: ", nneighbours
# "Ntrees: ", ntrees

with visualize:
	st.session_state['user_data']