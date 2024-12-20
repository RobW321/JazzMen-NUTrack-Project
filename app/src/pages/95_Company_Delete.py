import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()


with st.form("delete_company_form"):
    
   
    companyID = st.number_input("CompanyID to delete", min_value=1, step=1, format="%d")
    
   
# Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Delete Company")

    if submit_button:
        if companyID > 50:
            st.error("Please enter a valid Company ID")
        else:
            # We only get into this else clause if all the input fields have something 
            # in them. 
            #
            # Package the data up that the user entered into 
            # a dictionary (which is just like JSON in this case)
            company_data = {
                "CompanyID": companyID
            }

            try:
                # using the requests library to put to /p/product.  Passing
                # product_data to the endpoint through the json parameter.
                # This particular end point is located in the products_routes.py
                # file found in api/backend/products folder. 
                response = requests.delete('http://api:4000/co/deletebycompid', json=company_data)
                if response.status_code == 200:
                    st.success("Company deleted successfully!")
                else:
                    st.error(f"Error deleting company: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")