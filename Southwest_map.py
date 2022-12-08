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
  
def Houston_Rockets_map():  #火箭
    st.header('主場:豐田中心')
    Toyota_Center= folium.Map(location=[29.750833, -95.362222], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "豐田中心"
    folium.Marker([29.750833, -95.362222], popup="豐田中心", tooltip=tooltip
    ).add_to(Toyota_Center)
    folium_static(Toyota_Center)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('teams picture/Toyota_Center.jpg')
        st.image(image)        
    with col2:        
        image1 = Image.open('teams picture/Toyota_Center_Tickets.jpg')
        st.image(image1)
    st.write('地址：1510 Polk St, Houston, TX 77002美國, 觀眾席數：18,300人')
    
def Memphis_Grizzlies_map():  #灰熊
    st.header('主場:聯邦快遞廣場')
    FedExForum_Center= folium.Map(location=[35.138333, -90.050556], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "聯邦快遞廣場"
    folium.Marker([35.138333, -90.050556], popup="聯邦快遞廣場", tooltip=tooltip
    ).add_to(FedExForum_Center)
    folium_static(FedExForum_Center)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('teams picture/FedExForum_Center.jpg')
        st.image(image)        
    with col2:        
        image1 = Image.open('teams picture/FedExForum_Center_Tickets.jpg')
        st.image(image1)
    st.write('地址：191 Beale St, Memphis, TN 38103美國, 觀眾席數：17,794人')
    
def New_Orleans_Pelicans_map():  #鵜鶘
    st.header('主場:冰沙國王中心')
    Smoothie_King_Center= folium.Map(location=[29.948889, -90.081944], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "冰沙國王中心"
    folium.Marker([29.948889, -90.081944], popup="冰沙國王中心", tooltip=tooltip
    ).add_to(Smoothie_King_Center)
    folium_static(Smoothie_King_Center)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('teams picture/Smoothie_King_Center.jpg')
        st.image(image)        
    with col2:        
        image1 = Image.open('teams picture/Smoothie_King_Center_Tickets.jpg')
        st.image(image1)
    st.write('地址：1501 Dave Dixon Dr, New Orleans, LA 70113美國, 觀眾席數：16,867人')

def San_Antonio_Spurs_map():  #馬刺
    st.header('主場:美國電話電報中心')
    AT&T_Center= folium.Map(location=[29.426944, -98.4375], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "美國電話電報中心"
    folium.Marker([29.426944, -98.4375], popup="美國電話電報中心", tooltip=tooltip
    ).add_to(AT&T_Center)
    folium_static(AT&T_Center)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('teams picture/AT&T_Center.jpg')
        st.image(image)        
    with col2:        
        image1 = Image.open('teams picture/AT&T_Center_Tickets.jpg')
        st.image(image1)
    st.write('地址：1 AT&T Center Parkway, San Antonio, TX 78219美國, 觀眾席數：18,418人')
