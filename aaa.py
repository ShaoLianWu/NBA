import streamlit as st  
import Pacific 
st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇分組？', ['Atlantic','Central', 'Southeast', 'Northwest','Pacific','Southwest'])
if option=='Pacific':
  
  teams=st.sidebar.selectbox( '選擇球隊？', ['Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings'])
  if teams=='Golden State Warriors':
    Pacific.Golden_State_Warriors()
  if teams=='Los Angeles Clippers':
    Pacific.Los_Angeles_Clippers()
  if teams=='Los Angeles Lakers':
    Pacific.Los_Angeles_Lakers()
  if teams=='Phoenix Suns':
    Pacific.Phoenix_Suns()
  if teams=='Sacramento Kings':
    Pacific.Sacramento_Kings()
    
  else option=='Southwest':
  
    teams=st.sidebar.selectbox( '選擇球隊？', ['Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans','San Antonio Spurs'])
    if teams=='Dallas Mavericks':
      Pacific.Dallas_Mavericks()
    if teams=='Houston Rockets':
      Pacific.Houston_Rockets()
    if teams=='Memphis Grizzlies':
      Pacific.Memphis_Grizzlies()
    if teams=='New Orleans Pelicans':
      Pacific.New_Orleans_Pelicans()
    if teams=='San Antonio Spurs':
      Pacific.San_Antonio_Spurs()
