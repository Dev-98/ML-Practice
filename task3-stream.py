import streamlit as st
import pandas as pd

data = pd.read_csv('data/task3/rawdata.csv')

# Ensure 'timestamp' column is in datetime format
data['newdate'] = pd.to_datetime(data["date"])
data['timestamp'] = pd.to_datetime(data['time']).dt.second

# Calculating total number of duration for each inside and outside
duration_data = data.groupby(['date', 'position'])['timestamp'].sum().unstack(fill_value=0).reset_index()

# Count the number of picking and placing activities per day
activity_count = data.groupby(['date', 'activity'])['activity'].count().unstack(fill_value=0).reset_index()

# Streamlit app
st.title("Activity Analysis")

# Display duration data
st.header("Datewise Total Duration for Inside and Outside Activities")
st.dataframe(duration_data)

# Display activity count data
st.header("Datewise Number of Picking and Placing Activities")
st.dataframe(activity_count)

# Plot duration data
st.header("Total Duration for Inside and Outside Activities")
st.line_chart(duration_data.set_index('date'))

# Plot activity count data
st.header("Number of Picking and Placing Activities")
st.bar_chart(activity_count.set_index('date'))