import streamlit as st
from datetime import datetime

st.title("User Information Form")

forms_value = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None
}

mindate = datetime(1900, 1, 1)
maxdate = datetime.now()

with st.form(key='user_info_form'):
    forms_value["name"] = st.text_input("Enter your name:")
    forms_value["height"] = st.number_input("Enter your height:")
    forms_value["gender"] = st.selectbox("Gender", ["Male", "Female"])
    forms_value["dob"] = st.date_input("Enter your Date of Birth:", max_value =maxdate, min_value=mindate)
        
    submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        if not all(forms_value.values()):
            st.error("Please fill all the fields.")
        else:
            st.balloons()
            st.write("### Thank you for submitting the form!")
            for (key, value) in forms_value.items():
                st.write(f"{key.capitalize()}: {value}")
    
