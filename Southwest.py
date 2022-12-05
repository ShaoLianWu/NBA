import streamlit as st  
import ATLANTIC 
st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇分組？', ['ATLANTIC', '中央組', '東南組', '西北組','太平洋組','西南組'])
if option=='ATLANTIC':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors'])
  if teams=='Boston Celtics':
    ATLANTIC.BostonCeltics()
  if teams=='Brooklyn Nets':
    ATLANTIC.BrooklynNets()
