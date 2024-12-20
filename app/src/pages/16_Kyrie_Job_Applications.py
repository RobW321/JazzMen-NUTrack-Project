import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Welcome Kyrie!')

if st.button(
    'View Applications',
    type='primary',
    use_container_width=True
):
    # Set the student_nuid value in session state
    st.session_state.student_nuid = 1004
    # Navigate to the page displaying applications
    st.switch_page('pages/12_Get_Applications.py')

if st.button('Add Applications', 
             type='primary',
             use_container_width=True):
  st.session_state.student_nuid = 1004
  st.switch_page('pages/12_Add_Applications.py')

if st.button('Edit Applications', 
             type='primary',
             use_container_width=True):
  st.session_state.student_nuid = 1004
  st.switch_page('pages/12_Update_Application.py')

if st.button('Delete Applications', 
             type='primary',
             use_container_width=True):
  st.session_state.student_nuid = 1004
  st.switch_page('pages/12_Delete_Application.py')

if st.button('Filter Applications by Priority',
            type='primary',
            use_container_width=True):
    st.session_state.student_nuid = 1004
    st.switch_page('pages/12_Filter_Application.py')
    
if st.button('Filter Applications by Status',
            type='primary',
            use_container_width=True):
    st.session_state.student_nuid = 1004
    st.switch_page('pages/12_Filter_By_Status_Application.py')

if "student_nuid" not in st.session_state:
    st.session_state.student_nuid = None
    