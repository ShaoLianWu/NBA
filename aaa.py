import streamlit as st  
import Pacific 
st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇分組？', ['Atlantic','Central', 'Southeast', 'Northwest','Pacific','Southwest'])
if option=='Pacific':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings'])
  if teams=='Boston Celtics':
    Pacific.BostonCeltics()
  if teams=='Brooklyn Nets':
    Pacific.BrooklynNets()
    
