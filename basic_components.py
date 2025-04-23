import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import os

# Some basic streamlit components
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.markdown("## Markdown")
st.caption("Caption")
st.divider()

# Showing code in streamlit
code_example = """
def hello_world():
    print("Hello, world!")          
    """
st.code(code_example, language='python')

# Showing image in streamlit
st.image(os.path.join(os.getcwd(), "static", "BG.jpg"))

# Showing dataframe in streamlit
st.subheader("Dataframe")

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

st.dataframe(df)

# Editable dataframe in streamlit
st.subheader("Data Editor")
edited_df = st.data_editor(df)

print(edited_df)

# Static table in streamlit
st.subheader("Static Table")
st.table(df)

# Metrics in streamlit
st.subheader("Metrics")
st.metric(label = "Total Rows", value = df.shape[0])
st.metric(label = "Average Age", value = df['Age'].mean())

# Json in streamlit
st.subheader("Json")
st.json(data)

# Dictionary in streamlit`
st.subheader("Dictionary")
st.write(data)

# Charts in streamlit
st.title("Charts")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# Area chart in streamlit
st.subheader("Area Chart")
st.area_chart(chart_data)

# Bar chart in streamlit
st.subheader("Bar Chart")      
st.bar_chart(chart_data)

# Line chart in streamlit
st.subheader("Line Chart")      
st.line_chart(chart_data)

# Scatter plot in streamlit
st.subheader("Scatter Plot")
scatter_data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=['x', 'y']
)
st.scatter_chart(scatter_data)

# Map in streamlit
st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

# Pyplot in streamlit
st.subheader("Pyplot")
fig, ax = plt.subplots()
ax.plot(chart_data['a'], label='a') 
ax.plot(chart_data['b'], label='b') 
ax.plot(chart_data['c'], label='c')
ax.set_title('Pyplot Example')
ax.legend()
st.pyplot(fig)


