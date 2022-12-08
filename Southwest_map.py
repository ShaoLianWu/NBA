import streamlit as st
import folium 
from PIL import Image  
from streamlit_folium import folium_static 

def Dallas_Mavericks_map():  #獨行俠
    st.header('主場:美國航空中心')
    American_Airlines_Center= folium.Map(location=[32.790556, -96.810278], zoom_start=16ㄢ
        # add marker for Liberty Bell
    tooltip = "美國航空中心"
    folium.Marker([32.790556, -96.810278], popup="美國航空中心", tooltip=tooltip
    ).add_to(American_Airlines_Center)
    folium_static(American_Airlines_Center)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('teams picture/American_Airlines.jpg')
        st.image(image)        
    with col2:        
        image1 = Image.open('teams picture/American_Airlines_Tickets.jpg')
        st.image(image1)
    st.write('地址：2500 Victory Ave, Dallas, TX 75219美國, 觀眾席數：20,000-21,041席')
  
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
