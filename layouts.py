import streamlit as st


# Streamlit Layouts

# Sidebar in streamlit
st.sidebar.title("This is the sidebar")
st.sidebar.write("This is the sidebar content")
sidebar_inpout = st.sidebar.text_input("Enter something in the sidebar:")

# Tabs in streamlit
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("This is Tab 1")
    
with tab2:
    st.write("This is Tab 2")   
    
with tab3:
    st.write("This is Tab 3")
    
# Columns in streamlit
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is column 1")
    
with col2:
    st.header("Column 2")
    st.write("This is column 2")

# Containers in streamlit
with st.container(border=True):
    st.header("Container")
    st.write("This is container content")
    
# Empty placeholder
placeholder = st.empty()
placeholder.write("This is a placeholder")

if st.button("Update Placeholder"):
    placeholder.write("Placeholder updated!")
    
# Expander in streamlit
with st.expander("Expand to see more"):
    st.write("This is the expanded content")
    st.write("You can put any Streamlit component here.")
    
# Popover (Tooltip) in streamlit
st.button("Hover over me", help="This is a tooltip message")

# Sidebar input handling
if sidebar_inpout:
    st.sidebar.write(f"You entered: {sidebar_inpout}")
    st.write(f"You entered in the sidebar: {sidebar_inpout}")