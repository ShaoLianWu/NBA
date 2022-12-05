import streamlit as st  
from PIL import Image  
def Golden_State_Warriors():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Golden_State_Warriors.png')
    st.image(image) 
  with col2:
     st.title('Golden State Warriors')
     st.subheader('老闆:Rick Welts')
     st.subheader('GM:Robert Michael')
     st.subheader('總教練:Stephen Douglas')     
  st.write('金州勇士（1971年至今）') 
  st.write('1971-1972年賽季開始，勇士隊改名為金州勇士（Golden State Warriors)。球隊離開舊金山，在奧克蘭進行絕大部份的主場比賽，沒有任何一場主場比賽於舊金山或戴利市舉行。但在那個球季中，有六場比賽的主場在於聖地牙哥舉行。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "12  次")
  col2.metric("分組冠軍🏆", "8  次")   
def Los_Angeles_Clippers():
  st.header('Los_Angeles_Clippers')
  image = Image.open('teams logo/Los_Angeles_Clippers_(2015).svg.png')
  st.image(image) 
  st.write('水牛城勇士（1970年–1978年）')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "0  次")
  col2.metric("分組冠軍🏆", "2  次")
  st.write('　布魯克林籃網隊的英文隊名為Brooklyn Nets，球隊成立於1967年，目前所在城市是美國紐約州布魯克林(Brooklyn, New York)，主場為大陸航空中心體育館(Prudential Center)。球隊原名紐澤西籃網隊（New Jersey Nets），2012年球隊遷至紐約布魯克林，4月底更名為「布魯克林籃網隊（Brooklyn Nets）。')
