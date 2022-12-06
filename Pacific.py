import streamlit as st  
from PIL import Image

def Golden_State_Warriors():   #勇士
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
  col1.metric("總冠軍🏆", "7  次")
  col2.metric("區冠軍🏆", "12  次")  
  
def Los_Angeles_Clippers():   #快艇
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Los_Angeles_Clippers.png')
    st.image(image) 
  with col2:
    st.title('Los Angeles Clippers')
    st.subheader('老闆:Gillian Zucker')
    st.subheader('GM:Michael Winger')
    st.subheader('總教練:Tyronn Jamar Lue') 
  st.write('水牛城勇士（1970年–1978年）-聖地牙哥快艇（1978年–1984年）-洛杉磯快艇（1984年至今）')
  st.write('是一支位於美國加利福尼亞州洛杉磯的NBA籃球隊，分屬於西區的太平洋組，主場為加密貨幣網體育館，預計2024年將遷往英格伍德。球隊在1970年成立於水牛城，1978年遷至聖地牙哥，1984年再遷至現今的洛杉磯。2014年8月13日，由於前任老闆在該年季後賽期間的言論爭議，前微軟CEO史蒂夫·鮑爾默成功收購洛杉磯快艇，正式接替唐納德·斯特林成為球隊新任老闆')
  col1, col2= st.columns(2)
  col1.metric("總冠軍🏆", "0  次")
  col2.metric("區冠軍🏆", "0  次")
  
def Los_Angeles_Lakers():   #湖人
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Los_Angeles_Lakers.png')
    st.image(image) 
  with col2:
    st.title('Los Angeles Lakers')
    st.subheader('老闆:Jeanie Buss')
    st.subheader('GM:Rob Pelinka')
    st.subheader('總教練:Darvin Ham') 
  st.write('NBL時代與NBA早期（1946–1979）-魔術師時代（1979–1991）-柯比·布萊恩與俠客·歐尼爾時期（1996–2004）-柯比·布萊恩時期（2004–2016）-後柯比·布萊恩時期（2016–2018）-雷霸龍·詹姆士時期（2018–至今）')
  st.write('一支位於美國加利福尼亞州洛杉磯的職業籃球隊，隸屬於NBA西區太平洋組，主場為加密貨幣網體育館。球隊前身為「明尼亞波利斯湖人」（Minneapolis Lakers）。至今共奪得17次總冠軍，與東區球隊波士頓塞爾提克並列NBA第一。')
  col1, col2= st.columns(2)
  col1.metric("總冠軍🏆", "32  次")
  col2.metric("區冠軍🏆", "2  次")

def Phoenix_Suns():   #太陽
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Los_Angeles_Lakers.png')
    st.image(image) 
  with col2:
    st.title('Los Angeles Lakers')
    st.subheader('老闆:Jeanie Buss')
    st.subheader('GM:Rob Pelinka')
    st.subheader('總教練:Darvin Ham') 
  st.write('NBL時代與NBA早期（1946–1979）-魔術師時代（1979–1991）-柯比·布萊恩與俠客·歐尼爾時期（1996–2004）-柯比·布萊恩時期（2004–2016）-後柯比·布萊恩時期（2016–2018）-雷霸龍·詹姆士時期（2018–至今）')
  st.write('一支位於美國加利福尼亞州洛杉磯的職業籃球隊，隸屬於NBA西區太平洋組，主場為加密貨幣網體育館。球隊前身為「明尼亞波利斯湖人」（Minneapolis Lakers）。至今共奪得17次總冠軍，與東區球隊波士頓塞爾提克並列NBA第一。')
  col1, col2= st.columns(2)
  col1.metric("總冠軍🏆", "32  次")
  col2.metric("區冠軍🏆", "2  次")
