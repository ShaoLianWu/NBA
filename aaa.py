import streamlit as st
from PIL import Image
import Pacific 
import Southwest
import Pacific_map
import Southwest_map
import Pacific_star
import Southwest_star
import Pacific_allplayers
import Southwest_allplayers

st.set_page_config(page_title="NBA Dashboard",
                   page_icon='🏀',
                   layout="wide")
st.title('NBA資訊面板系統')

image=Image.open('NBA logo.jpg')
st.set_page_config(page_title='NBA introduction')
st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇分組？', ['Atlantic','Central', 'Southeast', 'Northwest','Pacific','Southwest'])

if option=='Pacific':
  
  teams=st.sidebar.selectbox( '選擇球隊？', ['Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings'])
  if teams=='Golden State Warriors':
    Pacific.Golden_State_Warriors()
    Pacific_map.Golden_State_Warriors_map()
    Pacific_star.Golden_State_Warriors_star()
  if teams=='Los Angeles Clippers':
    Pacific.Los_Angeles_Clippers()
    Pacific_map.Los_Angeles_Clippers_map()
    Pacific_star.Los_Angeles_Clippers_star()
  if teams=='Los Angeles Lakers':
    Pacific.Los_Angeles_Lakers()
    Pacific_map.Los_Angeles_Lakers_map()
    Pacific_star.Los_Angeles_Lakers_star()
  if teams=='Phoenix Suns':
    Pacific.Phoenix_Suns()
    Pacific_map.Phoenix_Suns_map()
    Pacific_star.Phoenix_Suns_star()
  if teams=='Sacramento Kings':
    Pacific.Sacramento_Kings()
    Pacific_map.Sacramento_Kings_map()
    Pacific_star.Sacramento_Kings_star()
    
if option=='Southwest':
  
  teams=st.sidebar.selectbox( '選擇球隊？', ['Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans','San Antonio Spurs'])
  if teams=='Dallas Mavericks':
    Southwest.Dallas_Mavericks()
    Southwest_map.Dallas_Mavericks_map()
    Southwest_star.Dallas_Mavericks_star()
  if teams=='Houston Rockets':
    Southwest.Houston_Rockets()
    Southwest_map.Houston_Rockets_map()
    Southwest_star.Houston_Rockets_star()
  if teams=='Memphis Grizzlies':
    Southwest.Memphis_Grizzlies()
    Southwest_map.Memphis_Grizzlies_map()
    Southwest_star.Memphis_Grizzlies_star()
  if teams=='New Orleans Pelicans':
    Southwest.New_Orleans_Pelicans()
    Southwest_map.New_Orleans_Pelicans_map()
    Southwest_star.New_Orleans_Pelicans_star()
  if teams=='San Antonio Spurs':
    Southwest.San_Antonio_Spurs()
    Southwest_map.San_Antonio_Spurs_map()
    Southwest_star.San_Antonio_Spurs_star()
    
