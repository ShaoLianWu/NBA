import streamlit as st
import folium 
from PIL import Image  
from streamlit_folium import folium_static 
def Golden_State_Warriors_map():
    st.header('主場:甲骨文球場')
    StateFarmArena= folium.Map(location=[33.75737827997708, -84.39633513151331], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "州立農業球館"
    folium.Marker([33.75737827997708, -84.39633513151331], popup="州立農業球館", tooltip=tooltip
    ).add_to(StateFarmArena)
    folium_static(StateFarmArena)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('State Farm Arena.jpeg')
        st.image(image)        
    with col2:        
        image1 = Image.open('State Farm Arena1.jpeg')
        st.image(image1)
    st.write('地址：1 State Farm Dr, Atlanta, GA 30303美國,觀眾席數：18,371席')
  
