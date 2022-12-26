import streamlit as st  #streamlit套件
import xlrd             #excel套件
import openpyxl         #excel套件
import pandas as pd     #pandas套件(資料分析)
import plost            #plost套件(甜甜圈圖)
from PIL import Image   #圖片套件
import matplotlib.pyplot as plt #matplotlib(資料繪圖)
import teams_information
import teams_map
import Pacific_star
import Southwest_star
import Pacific_allplayers
import Southwest_allplayers

st.set_page_config(page_title="NBA Dashboard",
                   page_icon='🏀',
                   layout="wide")
st.title('NBA資訊面板系統')

image=Image.open('NBA logo.png')
st.sidebar.image(image)
st.sidebar.title('請選擇區域及球隊')
area_list={'Pacific':{'Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings'},
           'Southwest':{'Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans','San Antonio Spurs'}}
option_area = st.sidebar.selectbox('選擇區域？',area_list)
option_teams = st.sidebar.selectbox('選擇球隊？',area_list[option_area])

teams_information.teams_information(option_teams)
teams_map.teams_map(option_teams)
