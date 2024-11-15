import streamlit as st
import pandas as pd
from datetime import datetime

st.title("🔍 Partners")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# remove streamlit header and footer
#hide_st_style = """
 #               <style>
 #               header {visibility: hidden;}
 #               footer {visibility: hidden;}
 #               </style>
 #               """
#st.markdown(hide_st_style, unsafe_allow_html=True)

# Authenticate user
#def authenticate():
#    if "authenticated" not in st.session_state:
#        st.session_state.authenticated = False

#    password = st.text_input("Password", type="password")
#    if st.button("Login"):
#        if password == "partners":
#            st.session_state.authenticated = True
#            st.success("Login successful!")
#        else:
#            st.error("Incorrect password")

#    return st.session_state.authenticated

#if not authenticate():
#    st.stop()

# Load employee data
df = pd.read_excel("partners.xlsx", index_col=0) # Set the first column as index

# Reset the index, start from 1
df = df.reset_index(drop=True)
df.index += 1 # Add 1 to each index

col1, col2 = st.columns(2)
with col1:
    # Search field
    search_by = st.selectbox(
        "Search By", 
        [
            "", 
            "Company", 
            "Country", 
            "Festivity", 
            "Golf", 
            "Name", 
            "Reception", 
            "BigS/SmallS", 
            "Tier",
        ], 
        key="search_by",
    )
with col2:
    # Search query
    search_query = st.text_input(f"Search {search_by}", key = "search_query")
    filtered_df = df.copy() # store copy of current df into filtered_df

# Filter cards based on search by
if search_query:
    if search_by == "":
        filtered_df = df.copy()
    elif search_by == "Name":
        #search_query = st.selectbox(f"Search {search_by}", df[search_by].unique())
        filtered_df = filtered_df[
            filtered_df['Name'].str.contains(search_query, case=False)
        ]
    elif search_by == "Company":
        filtered_df = filtered_df[
            filtered_df['Company'].str.contains(search_query, case=False)
        ]
    elif search_by == "Country":
        filtered_df = filtered_df[
            filtered_df['Country'].str.contains(search_query, case=False)
        ]
    elif search_by == "Golf":
        filtered_df = filtered_df[
            filtered_df['Golf'].str.contains(search_query, case=False)
        ]
    elif search_by == "Reception":
        filtered_df = filtered_df[
            filtered_df['Reception'].str.contains(search_query, case=False)
        ]
    elif search_by == "Festivity":
        filtered_df = filtered_df[
            filtered_df['Festivity'].str.contains(search_query, case=False)
        ]
    elif search_by == "BigS/SmallS":
        filtered_df = filtered_df[
            filtered_df['BigS/SmallS'].str.contains(search_query, case=False)
        ]
    elif search_by == "Tier":
        filtered_df = filtered_df[
            filtered_df['Tier'].str.lower() == search_query.lower()
        ]

# Download the DataFrame as an Excel file
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"partner_list_{current_time}.csv"
st.download_button(
    label="Download Data (.csv)",
    data=filtered_df.to_csv(),
    file_name=file_name,
    mime="text/csv"
)

def toggle_edit_mode(index):
    st.session_state[f"edit_mode_{index}"] = not st.session_state[f"edit_mode_{index}"]

def get_tier_color(tier):
    # Define color mappings for different tiers
    tier_colors = {
        "A+": "green",
        "A": "blue",
        "B": "purple",
        "C": "orange"
        # Add more tiers and colors as needed
    }
    return tier_colors.get(tier, "gray")  # Default color for unknown tiers

def get_status_color(status):
    return "green" if status == "Active" else "red"

# Display employee cards setup with edit functionality
def display_employee_card(employee_data,index):
    employee_data = employee_data.fillna('Nil')
    with st.container():

        # Format the date to display only the date, handling potential missing values and invalid formats
        posting_date = employee_data['Posting Date']
        formatted_posting_date = ""
        if pd.notnull(posting_date) and posting_date != 'Nil':
            if isinstance(posting_date, str):
                try:
                    formatted_posting_date = datetime.strptime(
                        posting_date, '%Y-%m-%d %H:%M:%S'
                    ).strftime('%Y-%m-%d')
                except ValueError:
                    formatted_posting_date = "Invalid Date"
            else:
                formatted_posting_date = posting_date.strftime('%Y-%m-%d')

        deposted_date = employee_data['De-posted Date']
        formatted_deposted_date = ""
        if pd.notnull(deposted_date) and deposted_date != 'Nil':
            if isinstance(deposted_date, str):
                try:
                    formatted_deposted_date = datetime.strptime(
                        deposted_date, '%Y-%m-%d %H:%M:%S'
                    ).strftime('%Y-%m-%d')
                except ValueError:
                    formatted_deposted_date = "Invalid Date"
            else:
                formatted_deposted_date = deposted_date.strftime('%Y-%m-%d')

        # Flag to track edit mode
        if f"edit_mode_{index}" not in st.session_state:
            st.session_state[f"edit_mode_{index}"] = False
        
        # Read-only mode by default
        if not st.session_state[f"edit_mode_{index}"]:
                
            st.markdown(
                f"""
                <div style="border-radius: 10px; border: 1px solid #ccc; padding: 10px; margin-bottom: 20px; background-color: #f9f9f9;">
                    <div style="float: right; background-color: {get_status_color(employee_data['Status'])}; color: white; padding: 5px 10px; border-radius: 5px;">
                        {employee_data['Status']}
                    </div>
                    <div style="float: right; color: white; padding: 5px 10px; border-radius: 5px;">
                    </div>
                    <div style="float: right; background-color: {get_tier_color(employee_data['Tier'])}; color: white; padding: 5px 10px; border-radius: 5px;">
                        <b>Tier: </b>{employee_data['Tier']}
                    </div>
                    <p style="font-weight: bold; font-size: 25px;">
                        {employee_data['Name']} ({employee_data['Designation']}), {employee_data['Company']}    
                    </p>
                    <div style="display: flex; flex-wrap: wrap;">
                        <div style="flex: 1; margin-right: 10px;">
                            <p><b>Country:</b><br>{employee_data['Country']}</p>
                            <p><b>Contact No.:</b><br> {int(employee_data['Contact No.'])}</p>
                            <p><b>Vehicle(s):</b><br> {employee_data['Vehicle']}</p>
                            <p><b>Address:</b><br> {employee_data['Address']}</p>
                        </div>
                        <div style="flex: 1; margin-right: 10px;">
                            <p><b>Posting Date:</b><br> {formatted_posting_date}</p>
                            <p><b>De-posted Date:</b><br> {formatted_deposted_date}</p>
                            <p><b>Golf:</b><br> {employee_data['Golf']}</p>
                            <p><b>Golf Handicap:</b><br> {employee_data['Golf Handicap']}</p>
                        </div>
                        <div style="flex: 1; margin-right: 10px;">
                            <p><b>Dietary Restrictions:</b><br> {employee_data['Dietary Restrictions']}</p>
                            <p><b>Reception:</b><br> {employee_data['Reception']}</p>
                            <p><b>Festivity:</b><br> {employee_data['Festivity']}</p>
                        </div>
                        <div style="flex: 1; margin-right: 10px;">
                            <p><b>BigS/SmallS:</b><br> {employee_data['BigS/SmallS']}</p>
                            <p><b>Interest(s):</b><br> {employee_data['Interests']} </p>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.button(
                f"Edit {employee_data['Name']}'s info", 
                key=f"edit_{index}", 
                on_click=lambda: toggle_edit_mode(index),
            )
        else:
            # Edit mode
            with st.form(f"edit_form_{index}"):
                # Create form fields for each detail
                new_name = st.text_input("Name", value=employee_data['Name'])
                new_designation = st.text_input(
                    "Designation", value=employee_data['Designation']
                )
                new_status = st.text_input("Status (Active/Deposted)", value=employee_data['Status'])
                new_contact = st.text_input(
                    "Contact No.", value=employee_data['Contact No.']
                )
                new_vehicle = st.text_input("Vehicle", value=employee_data['Vehicle'])
                new_address = st.text_input("Address", value=employee_data['Address'])
                new_posting_date = st.date_input(
                    "Posting Date (YYYY/MM/DD)", value=employee_data['Posting Date']
                )
                new_depost_date = st.text_input(
                    "De-posted Date (YYYY/MM/DD)", value=employee_data['De-posted Date']
                )
                new_golf = st.text_input("Golf", value=employee_data['Golf'])
                new_golf_handicap = st.text_input(
                    "Golf Handicap", value=employee_data['Golf Handicap']
                )
                new_dietary = st.text_input(
                    "Dietary Restrictions", value=employee_data['Dietary Restrictions']
                )
                new_reception = st.text_input(
                    "Reception", value=employee_data['Reception']
                )
                new_festivity = st.text_input(
                    "Festivity", value=employee_data['Festivity']
                )
                new_interest = st.text_input(
                    "Interests", value=employee_data['Interests']
                )
                new_tier = st.text_input("Tier (A+, A, B, C, Untiered)", value=employee_data['Tier'])
                new_sip = st.text_input(
                    "BigS/SmallS", value=employee_data['BigS/SmallS']
                )
                
                submitted = st.form_submit_button("Save")
                cancelled = st.form_submit_button("Cancel")

                if submitted:
                    df.at[index, "Name"] = new_name
                    df.at[index, "Designation"] = new_designation
                    df.at[index, "Contact No."] = int(new_contact)
                    df.at[index, "Vehicle"] = new_vehicle
                    df.at[index, "Address"] = new_address
                    df.at[index, "Posting Date"] = new_posting_date
                    df.at[index, "De-posted Date"] = new_depost_date
                    df.at[index, "Golf"] = new_golf
                    df.at[index, "Golf Handicap"] = new_golf_handicap
                    df.at[index, "Dietary Restriction"] = new_dietary
                    df.at[index, "Reception"] = new_reception
                    df.at[index, "Festivity"] = new_festivity
                    df.at[index, "Interests"] = new_interest
                    df.at[index, "Tier"] = new_tier
                    df.at[index, "BigS/SmallS"] = new_sip
                    df.at[index, "Status"] = new_status
                    
                    # updates = { # currently not working as well
                    #     "Name": new_name,
                    #     "Designation": new_designation,
                    #     "Contact No.": new_contact,
                    #     "Vehicle": new_vehicle,
                    #     "Address": new_address,
                    #     "Posting Date": new_posting_date,
                    #     "De-posted Date": new_depost_date,
                    #     "Golf": new_golf,
                    #     "Golf Handicap": new_golf_handicap,
                    #     "Dietary Restrictions": new_dietary,
                    #     "Reception": ", ".join(new_reception), # convert list to string format
                    #     "Festivity": ", ".join(new_festivity),
                    #     "Interests": new_interest,
                    #     "Tier": new_tier,
                    #     "BigS/SmallS": ", ".join(new_sip),
                    #     "Status": new_status
                    # }
                    #df.loc[{index}] = updates
                    df.to_excel("partners.xlsx", index=True)
                    st.success("Employee information updated successfully!")
                    st.session_state[f"edit_mode_{index}"] = False    
                    st.rerun()
                if cancelled:
                    st.session_state[f"edit_mode_{index}"]=False
                    st.rerun()
            
# Display number of employee cards shown
def display_employee_cards(df):
    num_cards = len(filtered_df)
    st.write(f"Showing {num_cards} results")
    
    for index, employee_data in filtered_df.iterrows():
        display_employee_card(employee_data, index)

# Display the filtered DataFrame
with st.expander("List view"):
    #st.write(filtered_df.drop('ID', axis=1))
    st.write(filtered_df)

# Display filtered or unfiltered data
display_employee_cards(filtered_df)