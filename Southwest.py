import streamlit as st  
from PIL import Image

def Dallas_Mavericks():   #獨行俠
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Dallas_Mavericks.png')
    st.image(image) 
  with col2:
     st.title('Dallas Mavericks')
     st.subheader('老闆:Mark Cuban')
     st.subheader('GM:Nico Harrison')
     st.subheader('總教練:Jason Frederick kidd')     
  st.write('達拉斯獨行俠(1980年至今)') 
  st.write('獨行俠最初由唐・卡特和Norm Sonju於1979年創辦。他們請求NBA聯盟准許於德克薩斯州建立一隊NBA球隊。達拉斯城的最後一隊職業籃球隊是美國籃球協會（ABA，後併入NBA）的達拉斯叢林隊，但由於ABA併入NBA，達拉斯叢林隊在1973年改組成為現今的聖安東尼奧馬刺隊而且把主場遷移到聖安東尼奧。從此，達拉斯城就沒有職業籃球隊伍了。')
  col1, col2= st.columns(2)
  col1.metric("總冠軍🏆", "1  次")
  col2.metric("區冠軍🏆", "2  次")  
  
def Houston_Rockets():   #火箭
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Houston_Rockets.png')
    st.image(image) 
  with col2:
    st.title('Houston Rockets')
    st.subheader('老闆:Tilman Fertitta')
    st.subheader('GM:Rafel Stone')
    st.subheader('總教練:Stephen Silas') 
  st.write('聖地牙哥火箭（1967年至1971年）-休士頓火箭（1971年至今）')
  st.write('火箭隊成立於1967年，目前所在地區是美國德克薩斯州休士頓市，主場為豐田中心球館。休士頓因為有NASA的存在，讓人容易聯想到「火箭隊」這名稱是否和太空有瓜葛，但其實火箭隊最開始的主場在聖地牙哥，而火箭的涵意則是代表著速度和高遠的意思。')
  col1, col2= st.columns(2)
  col1.metric("總冠軍🏆", "0  次")
  col2.metric("區冠軍🏆", "0  次")

def Memphis_Grizzlies():   #灰熊
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Memphis_Grizzlies.png')
    st.image(image) 
  with col2:
    st.title('Memphis Grizzlies')
    st.subheader('老闆:Robert Pera')
    st.subheader('GM:Zach Kleiman')
    st.subheader('總教練:Taylor Vetter Jenkins') 
  st.write('溫哥華灰熊(1995年至2001年)-曼非斯灰熊(2001年至今)')
  st.write('灰熊成立於1995年，位於美國田納西州曼非斯的NBA籃球隊，分屬於西區的西南組，主場為聯邦快遞廣場。現任總教練為Taylor Vetter Jenkins。1995年，球隊創立於溫哥華，命名溫哥華灰熊（Vancouver Grizzlies），是第二支非美國本土的NBA球隊（第一支是多倫多暴龍）。2001年，球隊遷至美國曼非斯，更名為現今的曼非斯灰熊。因此，灰熊不再是非美國本土的NBA球隊。')
  col1, col2= st.columns(2)
  col1.metric("總冠軍🏆", "0  次")
  col2.metric("區冠軍🏆", "0  次")
  
def New_Orleans_Pelicans():   #鵜鶘
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/New_Orleans_Pelicans.png')
    st.image(image) 
  with col2:
    st.title('New Orleans Pelicans')
    st.subheader('老闆:Gayle Benson')
    st.subheader('GM:Trajan Shaka Langdon')
    st.subheader('總教練:Willie J. Green') 
  st.write('紐奧良黃蜂(2002年至2005年)(2007年至2013年)-紐奧良/奧克拉荷馬市黃蜂(2005年至2007年)-紐奧良鵜鶘(2013年至今)')
  st.write('鵜鶘成立於2002年，位於美國路易斯安那州紐奧良的NBA籃球隊，分屬於西區的西南組，主場為冰沙國王中心。目前球隊的擁有者是汽車業界大亨Gayle Benson，現任總教練是Willie J. Green。紐奧良鵜鶘的前身為紐奧良黃蜂（New Orleans Hornets），為2002年夏洛特黃蜂遷至紐奧良時所改名成立的。2005年，由於紐奧良受到颶風卡崔娜侵襲而嚴重損毀，球隊一度遷移主場至奧克拉荷馬市，直到2007年才重返紐奧良。2013年4月，球隊更名為現今的紐奧良鵜鶘。2014年，球隊將原先所擁有的夏洛特黃蜂隊名與1988年至2002年的球季記錄，回歸至夏洛特，由夏洛特黃蜂接收。')
  col1, col2= st.columns(2)
  col1.metric("總冠軍🏆", "0  次")
  col2.metric("區冠軍🏆", "0  次")


def San_Antonio_Spurs():   #馬刺
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/San_Antonio_Spurs.png')
    st.image(image) 
  with col2:
    st.title('San Antonio Spurs')
    st.subheader('老闆:Spurs Sports & Entertainment')
    st.subheader('GM:Brian Wright')
    st.subheader('總教練:Gregg Popovich') 
  st.write('達拉斯矮樹叢(1967年至1970年)(1971年–1973年)-德克薩斯矮樹叢(1970年至1971年)-聖安東尼奧馬刺(1973年至1976年)-聖安東尼奧馬刺(1976年至今)')
  st.write('馬刺成立於1967年，位於美國德克薩斯州聖安東尼奧國家籃球協會（NBA聯盟）旗下職業球隊，分屬於西區西南賽區，球隊主場為AT&T中心。目前球隊之所有人為Peter John Holt，總教練則是Gregg Popovich。球隊最初是美國籃球協會（ABA）達拉斯叢林隊，也是ABA與NBA合併後，獲得過NBA總冠軍前ABA球隊。馬刺一共先後於1998–99賽季、2002–03賽季、2004–05賽季、2006–07賽季、2013–14賽季獲得過5次總冠軍，而且馬刺奪下5次總冠軍中「石佛」Timothy Theodore Duncan就拿下了3次FMVP。')
  col1, col2= st.columns(2)
  col1.metric("總冠軍🏆", "5  次")
  col2.metric("區冠軍🏆", "6  次")
