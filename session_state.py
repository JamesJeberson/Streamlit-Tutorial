import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write("Counter incremented to ", st.session_state.counter) 

if st.button("Reset Counter"):
    st.session_state.counter = 0
    
st.write("Counter: ", st.session_state.counter)