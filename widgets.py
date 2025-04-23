import streamlit as st

if "slider" not in st.session_state:
    st.session_state.slider = 25
    
min_value = st.slider("set min value", 0, 50, 25)

st.session_state.slider = st.slider("Slider", min_value, 100, st.session_state.slider)


if "Checkbox" not in st.session_state:
    st.session_state.Checkbox = False
    
def toggle_checkbox():
    st.session_state.Checkbox = not st.session_state.Checkbox
    
st.checkbox("Show Input Field", value=st.session_state.Checkbox, on_change=toggle_checkbox)

if st.session_state.Checkbox:
    user_input = st.text_input("Enter your name:", value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")

st.write("User Input:", user_input)
    
