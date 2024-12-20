import requests
import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

st.title(f"Your Applications:")

# Fetch the student_nuid from session state
if "student_nuid" in st.session_state and st.session_state.student_nuid is not None:
    student_nuid = st.session_state.student_nuid

    # Fetch applications for the student
    try:
        API_URL = "http://api:4000/a/applications"
        response = requests.get(f"{API_URL}/{student_nuid}")
        response.raise_for_status()
        applications = response.json()

        if not applications:
            st.write("No applications found.")
        else:
            # Convert applications to a structured format for the table
            data = [
                {
                    "Application ID": app["ApplicationID"],
                    "Date Submitted": app["DateSubmitted"],
                    "Status": app["Status"],
                    "Priority": app["Priority"],
                    "Job": app["JobDescription"],
                    "Company": app["CompanyName"],
                    "Notes": app["Notes"],
                }
                for app in applications
            ]

            # Display applications as a table
            st.table(data)

    except requests.exceptions.RequestException as e:
        st.error("Failed to fetch applications. Please try again later.")
        st.error(e)

else:
    st.error("No student NUID found in session state. Please navigate from the main page.")