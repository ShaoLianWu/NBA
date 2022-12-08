import streamlit as st
import folium 
from PIL import Image  
from streamlit_folium import folium_static 
def Golden_State_Warriors_map():
    st.header('主場:大通銀行中心')
    Chase_Center= folium.Map(location=[37.768056, -122.3875], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "大通銀行中心"
    folium.Marker([37.768056, -122.3875], popup="大通銀行中心", tooltip=tooltip
    ).add_to(Chase_Center)
    folium_static(Chase_Center)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('teams picture/Chase_Center.jpeg')
        st.image(image)        
    with col2:        
        image1 = Image.open('teams picture/Chase_Center_Tickets.jpeg')
        st.image(image1)
    st.write('地址：1 Warriors Way, San Francisco, CA 94158美國, 觀眾席數：18,064席, 演唱會 19,500')
  
