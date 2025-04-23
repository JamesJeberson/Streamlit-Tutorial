import streamlit as st
import time

@st.cache_data(ttl=60) # cache data for 60 seconds
def fetch_data():
    # Simulate a long-running computation
    time.sleep(3) # Delay for 3 seconds
    return {"data": "This is cached data!"} # immutable data

st.write("Fetching Data...")
data = fetch_data()

st.write(data)


@st.cache_resource
def get_file_handler():
    # Open a file in append mode
    # This will create the file if it doesn't exist
    file = open("file.txt", "a+")
    return file

# USe the cached file handler
# This will be reused across reruns
file_handler = get_file_handler()

# Write to the file when the button is clicked
if st.button("Write to File"):
    file_handler.write("New line of text\n")
    file_handler.flush() # Ensure data is written to the file
    st.success("Data written to file!")
    
# Read abnd display the file content
if st.button("Read File"):
    file_handler.seek(0) # Move the cursor to the beginning of the file
    content = file_handler.read()
    st.text(content)

# Always close the file when done
if st.button("Close File"):
    file_handler.close()
    st.success("File closed successfully!")

