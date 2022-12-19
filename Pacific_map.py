import streamlit as st
import folium 
from PIL import Image  
from streamlit_folium import folium_static 

def Golden_State_Warriors_map():  #勇士
    st.header('主場:大通銀行中心')
    col1,col2 = st.columns((6,4))
    with col1:
        Chase_Center= folium.Map(location=[37.768056, -122.3875], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "大通銀行中心"
        folium.Marker([37.768056, -122.3875], popup="大通銀行中心", tooltip=tooltip
        ).add_to(Chase_Center)
        folium_static(Chase_Center)
    with col2:
        image = Image.open('teams picture/Chase_Center.jpg')
        st.image(image)        
        image1 = Image.open('teams picture/Chase_Center_Tickets.jpg')
        st.image(image1)
        st.write('地址：1 Warriors Way, San Francisco, CA 94158美國, 觀眾席數：18,064席')
  
def Los_Angeles_Clippers_map():  #快艇
    st.header('主場:加密貨幣網體育館')
    Staples_Center= folium.Map(location=[34.043056, -118.267222], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "加密貨幣網體育館"
    folium.Marker([34.043056, -118.267222], popup="加密貨幣網體育館", tooltip=tooltip
    ).add_to(Staples_Center)
    folium_static(Staples_Center)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('teams picture/Staples_Center.jpg')
        st.image(image)        
    with col2:        
        image1 = Image.open('teams picture/Staples_Center_Tickets.jpg')
        st.image(image1)
    st.write('地址：1111 S Figueroa St, Los Angeles, CA 90015美國, 觀眾席數：19,060人')
    
def Los_Angeles_Lakers_map():  #湖人
    st.header('主場:加密貨幣網體育館')
    Staples_Center= folium.Map(location=[34.043056, -118.267222], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "加密貨幣網體育館"
    folium.Marker([34.043056, -118.267222], popup="加密貨幣網體育館", tooltip=tooltip
    ).add_to(Staples_Center)
    folium_static(Staples_Center)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('teams picture/Staples_Center.jpg')
        st.image(image)        
    with col2:        
        image1 = Image.open('teams picture/Staples_Center_Tickets.jpg')
        st.image(image1)
    st.write('地址：1111 S Figueroa St, Los Angeles, CA 90015美國, 觀眾席數：18,997人')
    
def Phoenix_Suns_map():  #太陽
    st.header('主場:足跡中心')
    Footprint_Center= folium.Map(location=[33.445833,-112.071389], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "足跡中心"
    folium.Marker([33.445833,-112.071389], popup="足跡中心", tooltip=tooltip
    ).add_to(Footprint_Center)
    folium_static(Footprint_Center)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('teams picture/Footprint_Center.jpg')
        st.image(image)        
    with col2:        
        image1 = Image.open('teams picture/Footprint_Center_Tickets.jpg')
        st.image(image1)
    st.write('地址：US Airways Center, 201S 1st St, Phoenix, AZ 85004美國, 觀眾席數：18,422人')

def Sacramento_Kings_map():  #國王
    st.header('主場:金州第一中心')
    Golden1_Center= folium.Map(location=[38.580361, -121.499611], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "金州第一中心"
    folium.Marker([38.580361, -121.499611], popup="金州第一中心", tooltip=tooltip
    ).add_to(Golden1_Center)
    folium_static(Golden1_Center)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('teams picture/Golden1_Center.jpg')
        st.image(image)        
    with col2:        
        image1 = Image.open('teams picture/Golden1_Center_Tickets.jpg')
        st.image(image1)
    st.write('地址：500 David J Stern Walk, Sacramento, CA 95814美國, 觀眾席數：17,500人')  
