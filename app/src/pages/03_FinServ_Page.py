import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

# Page Title
st.title("FinServ Inc. - Application Details")

# Retrieve application details
app_name = "FinServ Inc."
status = st.session_state.get(f"{app_name}_status", "Rejected")
favorite = st.session_state.get(f"{app_name}_favorite", False)

# Update Status
st.write("### Update Status")
new_status = st.selectbox(
    "Select Status",
    ["In Progress", "Accepted", "Rejected"],
    index=["In Progress", "Accepted", "Rejected"].index(status)
)
if st.button("Update Status"):
    st.session_state[f"{app_name}_status"] = new_status
    st.success(f"Status updated to {new_status}")

# Update Favorite
st.write("### Update Favorite")
new_favorite = st.checkbox("Favorite", value=favorite)
if st.button("Update Favorite"):
    st.session_state[f"{app_name}_favorite"] = new_favorite
    st.success(f"Favorite updated to {'Yes' if new_favorite else 'No'}")
