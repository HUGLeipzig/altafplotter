import streamlit as st

def get_url_param(param):
	try:
		query_params = st.query_params.to_dict()
		query_option = query_params[param]
		
		return query_option
	except:
		return "no person ID in params"