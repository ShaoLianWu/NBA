import streamlit as st  
from PIL import Image  
def BostonCeltics():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/BostonCeltics.png')
    st.image(image) 
  with col2:
     st.title('Boston Celtics')
     st.subheader('老闆:Wyc Grousbeck')
     st.subheader('GM:Juka Mcehaic')
     st.subheader('總教練:Joe Mazzulla (臨時)')     
  st.write('波士頓塞爾提克(1946年-至今)') 
  st.write('波士頓塞爾蒂克隊的英文隊名為Boston Celtics，成立於1946年，目前所在地區是美國麻塞諸塞州波士頓市，主場為TD北岸花園球館，為美國職籃史上獲得總冠軍次數最多的球隊。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "22  次")
  col2.metric("分組冠軍🏆", "32  次")   
def BrooklynNets():
  st.header('Brooklyn Nets')
  image = Image.open('teams logo/BrooklynNets.png')
  st.image(image) 
  st.write('Brooklyn Nets(1946年-至今)')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "22  次")
  col2.metric("分組冠軍🏆", "32  次")
  st.write('　布魯克林籃網隊的英文隊名為Brooklyn Nets，球隊成立於1967年，目前所在城市是美國紐約州布魯克林(Brooklyn, New York)，主場為大陸航空中心體育館(Prudential Center)。球隊原名紐澤西籃網隊（New Jersey Nets），2012年球隊遷至紐約布魯克林，4月底更名為「布魯克林籃網隊（Brooklyn Nets）。')
