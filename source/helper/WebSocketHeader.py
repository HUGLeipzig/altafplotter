import streamlit as st
import base64

from settings import settings

def get_header(DEV=False):

    if settings.DEV == True:
        from settings import credentialsDEV
        x = base64.b64encode(f"{credentialsDEV.user}:{credentialsDEV.pw}".encode()).decode()
        headers = {'Authorization': f'Basic {x}'}

    else:
        headers_complete = st.context.headers 
        headers = {'Authorization':headers_complete.get('Authorization')}

    return headers
