import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
     layout="wide"
 )

# st.title("🔍 Partners")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

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
df = pd.read_excel("partners.xlsx")

home_page = st.Page(
    page = "view/home.py",
    title = "Partners",
    icon = "🔍",
    default = True
)

add_new_page = st.Page(
    page = "view/add_new.py",
    title = "Add New Employee",
    icon = "✍🏼"
)

pg = st.navigation(pages=[home_page, add_new_page])
pg.run()