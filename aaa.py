import streamlit as st  
import Pacific 
import Southwest
import Pacific_map
import Southwest_map

st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇分組？', ['Atlantic','Central', 'Southeast', 'Northwest','Pacific','Southwest'])

if option=='Pacific':
  
  teams=st.sidebar.selectbox( '選擇球隊？', ['Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings'])
  if teams=='Golden State Warriors':
    Pacific.Golden_State_Warriors()
    Pacific_map.Golden_State_Warriors_map()
  if teams=='Los Angeles Clippers':
    Pacific.Los_Angeles_Clippers()
    Pacific_map.Los_Angeles_Clippers_map()
  if teams=='Los Angeles Lakers':
    Pacific.Los_Angeles_Lakers()
    Pacific_map.Los_Angeles_Lakers_map()
  if teams=='Phoenix Suns':
    Pacific.Phoenix_Suns()
    Pacific_map.Phoenix_Suns_map()
  if teams=='Sacramento Kings':
    Pacific.Sacramento_Kings()
    Pacific_map.Sacramento_Kings_map()
    
if option=='Southwest':
  
  teams=st.sidebar.selectbox( '選擇球隊？', ['Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans','San Antonio Spurs'])
  if teams=='Dallas Mavericks':
    Southwest.Dallas_Mavericks()
    Southwest_map.Dallas_Mavericks_map()
  if teams=='Houston Rockets':
    Southwest.Houston_Rockets()
    Southwest_map.Houston_Rockets_map()
  if teams=='Memphis Grizzlies':
    Southwest.Memphis_Grizzlies()
    Southwest_map.Memphis_Grizzlies_map()
  if teams=='New Orleans Pelicans':
    Southwest.New_Orleans_Pelicans()
    Southwest_map.New_Orleans_Pelicans_map()
  if teams=='San Antonio Spurs':
    Southwest.San_Antonio_Spurs()
    Southwest_map.San_Antonio_Spurs_map()
