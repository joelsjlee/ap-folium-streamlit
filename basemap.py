import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide")

st.title("Headline Variation in AP Wire Copy")

page = st.radio(
    "Select Date", ["November 25th, 1942 A", "November 25th, 1942 B"], index=0
)

def marker(m, filename):
    df = pd.read_csv(filename)
    for i, r in df.iterrows():
        tooltip = "<b>{}</b><br/>{}".format(r["Headline"], r['Sub Headline'])
        popup = "<a href='{}' target='_blank'>{}</a>".format(r['Page URL'], r['Page URL'])
        folium.Marker([r["Latitude"], r["Longitude"]], 
            tooltip=folium.Tooltip(tooltip, permanent=True),
            popup=folium.Popup(popup)).add_to(m)

m = folium.Map(tiles='OpenStreetMap', width=1300,height=600, location=[39, -95], zoom_start=4)

if page == "November 25th, 1942 A":
    marker(m, "nov-25-a.csv")

if page == "November 25th, 1942 B":
    marker(m, "nov-25-b.csv")

folium_static(m, width=1300, height=600)



