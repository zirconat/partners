import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Load employee data
df = pd.read_excel("partners.xlsx")

# Ensure 'images' folder exists
if not os.path.exists("images"):
    os.makedirs("images")

st.title("✍🏼 Add New Employee")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
    
# Add New Employee Button
with st.form("add_employee_form"):
    # File uploader for profile image
    uploaded_image = st.file_uploader("Upload Profile Image", type=["jpg", "jpeg", "png"])
    
    new_name = st.text_input("Name")
    new_designation = st.text_input("Designation")
    new_status = st.selectbox("Status", ("Active", "Deposted"))
    new_country = st.text_input("Country")
    new_company = st.text_input("Company")
    new_contact = st.text_input("Contact No.")
    new_vehicle = st.text_input("Vehicle")
    new_address = st.text_input("Address")
    new_posting_date = st.date_input("Posting Date")
    new_depost_date = st.text_input("De-posted Date (YYYY/MM/DD)") 
    new_golf = st.selectbox("Golf", ("Yes", "No"))
    new_golf_handicap = st.text_input("Golf Handicap (if N.A. please put 'Nil')")
    new_dietary = st.text_input("Dietary Restrictions (if none please put 'Nil')")
    new_reception = st.multiselect("Reception (You may select more than one)", ("NYR", "ALSE"))
    new_festivity = st.multiselect("Festivity (You may select more than one)", ("Chinese New Year", "Deepavali", "Hari Raya", "Rosh Hashanah", "Seasons Greetings", "Thanksgiving"))
    new_interest = st.text_input("Interests")
    new_tier = st.selectbox("Tier", ("A+", "A", "B", "C", "Untiered"))
    new_sip = st.multiselect("BigS/SmallS (You may select more than one)", ("BigS", "SmallS"))

    
    
    submitted = st.form_submit_button("Add Employee")

if submitted:

    # Save uploaded image if available
    photo_path = None
    if uploaded_image:
        image_save_path = f"images/{new_name.replace(' ', '_').lower()}.jpg"
        with open(image_save_path, "wb") as f:
            f.write(uploaded_image.read())
        photo_path = image_save_path

    new_employee_data = {
        "Name": new_name,
        "Designation": new_designation,
        "Contact No.": new_contact,
        "Vehicle": new_vehicle,
        "Address": new_address,
        "Posting Date": new_posting_date,
        "De-posted Date": new_depost_date,
        "Golf": new_golf,
        "Golf Handicap": new_golf_handicap,
        "Dietary Restrictions": new_dietary,
        "Reception": ", ".join(new_reception), # convert list to string format
        "Festivity": ", ".join(new_festivity),
        "Interests": new_interest,
        "Tier": new_tier,
        "BigS/SmallS": ", ".join(new_sip),
        "Country": new_country,
        "Company": new_company,
        "Status": new_status,
        "Photo": photo_path # Save photo path
    }
    df = pd.concat([df, pd.DataFrame([new_employee_data])], ignore_index=True)
    df.to_excel("partners.xlsx", index=False)
    st.success("New employee added successfully!") # Display success message
    st.rerun() # Trigger a re-render to display the new employee