import streamlit as st
import requests
import pandas as pd
import streamlit.components.v1 as components

fmURL = "https://ice.home.zero.mv/fm"
stations = "https://radio.home.zero.mv/api/stations"

r = requests.get(stations)
data = r.json()
df = pd.DataFrame(data)

#df
df['fq+Name'] = df['frequency'] + " - " + df['name']
stations = df['name']
default_station = "89.0 - DhivehiRaajjeyge Adu"

st.title("Zero FM")
selected_station = st.selectbox("Select Station, ", df['fq+Name'])

def getStreamURL(selected_station, defaultStation, df):
    if(selected_station == defaultStation):
        return fmURL
    elif(df['fq+Name'] == selected_station).any():
        filtered_df = df[df['fq+Name'] == selected_station]
        return filtered_df['alt_stream_url'].values[0]
    else:
        return None

stream = getStreamURL(selected_station,  "89.0 - DhivehiRaajjeyge Adu", df)

st.audio(stream, autoplay=True)