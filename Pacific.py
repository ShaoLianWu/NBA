import streamlit as st  
from PIL import Image

def Golden_State_Warriors():   #勇士
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Golden_State_Warriors.png')
    st.image(image) 
  with col2:
     st.title('Golden State Warriors')
     st.subheader('老闆:Joe Lacob & Peter Guber')
     st.subheader('GM:Robert Michael "Bob" Myers')
     st.subheader('總教練:Stephen Douglas "Steve" Kerr')     
  st.write('費城勇士（1946年至1962年）-舊金山勇士（1962年至1971年）-金州勇士（1971年至今）') 
  st.write('勇士成立於1946年，位於美國加利福尼亞州舊金山的美國職業籃球隊，分屬於NBA聯盟西區聯盟的太平洋組，主場球館為大通銀行中心。球隊的格言為「全隊即為一城」（The whole team is a city）。勇士隊是現今北美職業體育聯賽裡，少有的名稱不包含主場所在城市的隊伍')
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
    st.subheader('老闆:Steve Anthony Ballmer')
    st.subheader('GM:Michael Winger')
    st.subheader('總教練:Tyronn Jamar Lue') 
  st.write('水牛城勇士（1970年至1978年）-聖地牙哥快艇（1978年至1984年）-洛杉磯快艇（1984年至今）')
  st.write('快艇成立於1970年，位於美國加利福尼亞州洛杉磯的NBA籃球隊，分屬於西區的太平洋組，主場為加密貨幣網體育館，預計2024年將遷往英格伍德。球隊在1970年成立於水牛城，1978年遷至聖地牙哥，1984年再遷至現今的洛杉磯。2014年8月13日，由於前任老闆在該年季後賽期間的言論爭議，前微軟CEOSteve Anthony Ballmer成功收購洛杉磯快艇，正式接替Donald Sterling成為球隊新任老闆')
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
    st.subheader('老闆:Jerry Buss & Todd Boehly & Patrick Soon-Shiong')
    st.subheader('GM:Robert Todd Pelinka Jr.')
    st.subheader('總教練:Darvin Ham') 
  st.write('底特律寶石(1946年至1947年)-明尼亞波利斯湖人(1947年至1959年)-洛杉磯湖人(1960年至今')
  st.write('湖人成立於1946年，位於美國加利福尼亞州洛杉磯的職業籃球隊，隸屬於NBA西區太平洋組，主場為加密貨幣網體育館。球隊前身為「明尼亞波利斯湖人」（Minneapolis Lakers）。至今共奪得17次總冠軍，與東區球隊波士頓塞爾提克並列NBA第一。')
  col1, col2= st.columns(2)
  col1.metric("總冠軍🏆", "17  次")
  col2.metric("區冠軍🏆", "32  次")

def Phoenix_Suns():   #太陽
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Phoenix_Suns.png')
    st.image(image) 
  with col2:
    st.title('Phoenix Suns')
    st.subheader('老闆:Robert Gary Sarver')
    st.subheader('GM:James Jones')
    st.subheader('總教練:Montgomery Eli Williams') 
  st.write('鳳凰城太陽（1968-至今）')
  st.write('太陽成立於1968年，位於美國亞利桑那州鳳凰城的職業籃球隊，分屬於NBA西區太平洋組，是該組唯一不在加利福尼亞州的球隊，主場為足跡中心。共有10位入選籃球名人堂的球員曾效力過太陽，其中Charles Wade Barkley及Stephen John Nash更在效力期間榮獲最有價值球員。')
  col1, col2= st.columns(2)
  col1.metric("總冠軍🏆", "0  次")
  col2.metric("區冠軍🏆", "3  次")

 def Sacramento_Kings():   #國王
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Sacramento_Kings.png')
    st.image(image) 
  with col2:
    st.title('Sacramento Kings')
    st.subheader('老闆:Vivek Ranadivé')
    st.subheader('GM:Monte McNair')
    st.subheader('總教練:Michael “Mike” Brown') 
  st.write('羅徹斯特皇家(1945年至1957年)-辛辛那提皇家(1957年至1972年)-堪薩斯城•奧馬哈國王(1972年至1975年)-堪薩斯城國王(1975年至1985年)-沙加緬度國王(1950-至今)')
  st.write('國王成立於1950年，位於美國加利福尼亞州沙加緬度的NBA籃球隊，分屬於西區的太平洋組。國王隊於2016-17 NBA賽季遷入位於沙加緬度市中心的新主場金州第一中心。沙加緬度市已經是國王隊駐紮過的第5座城市，而國王隊於2012年可能又要考慮遷移主場去洛杉磯地區，但是遭到了洛杉磯湖人和洛杉磯快艇的強烈抵制')
  col1, col2= st.columns(2)
  col1.metric("總冠軍🏆", "1  次")
  col2.metric("區冠軍🏆", "1  次")
