import streamlit as st  
from PIL import Image
import pandas as pd
import xlrd
import openpyxl

df = pd.read_excel("star/Pacific_Southwest_star.xlsx",sheet_name="工作表1",usecols="A:H") 

def Golden_State_Warriors_star():
  st.header('Golden State Warriors三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Tim Hardaway', 'Klay thompson', 'Stephen Curry'])
    if option=='Tim Hardaway':
      new_df = df[0:1]  
      st.dataframe(new_df))
    if option=='Klay thompson':
      new_df = df[1:2]
      st.dataframe(new_df)
    if option=='Stephen Curry':
      new_df = df[2:3]
      st.dataframe(new_df)
  with col2:
    if option=='Tim Hardaway':
      image = Image.open('star/Tim Hardaway.jpg')
      st.image(image)
    if option=='Klay thompson':
      image = Image.open('star/Klay thompson.jpg')
      st.image(image)
    if option=='Stephen Curry':
      image = Image.open('star/Stephen Curry.jpg')
      st.image(image)
      
def Los_Angeles_Clippers_star():
  st.header('Los Angeles Clippers三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Bob McAdoo', 'Blake Griffin', 'Chris Paul'])
    if option=='Bob McAdoo':
      new_df = df[5:6]
      st.dataframe(new_df)
    if option=='Blake Griffin':
      new_df = df[6:7]
      st.dataframe(new_df)
    if option=='Chris Paul':
      new_df = df[7:8]
      st.dataframe(new_df)
  with col2:
    if option=='Bob McAdoo':
      image = Image.open('star/Bob McAdoo.jpg')
      st.image(image)
    if option=='Blake Griffin':
      image = Image.open('star/Blake Griffin.jpg')
      st.image(image)
    if option=='Chris Paul':
      image = Image.open('star/Chris Paul.jpg')
      st.image(image)
      
def Los_Angeles_Lakers_star():
  st.header('Los Angeles Lakers star三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Magic Johnson', 'Shaquille O`Neal', 'Kobe Bryant'])
    if option=='Magic Johnson':
      new_df = df[9:10]
      st.dataframe(new_df)
    if option=='Shaquille O`Neal':
      new_df = df[10:11]
      st.dataframe(new_df)
    if option=='Kobe Bryant':
      new_df = df[11:12]
      st.dataframe(new_df)
  with col2:
    if option=='Magic Johnson':
      image = Image.open('star/Magic Johnson.jpg')
      st.image(image)
    if option=='Shaquille O`Neal':
      image = Image.open('star/Shaquille ONeal.jpg')
      st.image(image)
    if option=='Kobe Bryant':
      image = Image.open('star/Kobe Bryant.jpg')
      st.image(image)

def  Phoenix_Suns_star():
  st.header('Phoenix Suns Star三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Amar`e Stoudemire', 'Steve Nash', 'Shawn Marion'])
    if option=='Amar`e Stoudemire':
      new_df = df[0:1]
      st.dataframe(new_df)
    if option=='Steve Nash':
      new_df = df[1:2]
      st.dataframe(new_df)
    if option=='Shawn Marion':
      new_df = df[2:3]
      st.dataframe(new_df)
  with col2:
    if option=='Amar`e Stoudemire':
      image = Image.open('star/Amare Stoudemire.jpg')
      st.image(image)
    if option=='Steve Nash':
      image = Image.open('star/Steve Nash.jpg')
      st.image(image)
    if option=='Shawn Marion':
      image = Image.open('star/Shawn Marion.jpg')
      st.image(image)
      
def Sacramento_Kings_star():
  st.header('Sacramento Kings star三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Chris Webber', 'Oscar Robertson', 'Doug Christie'])
    if option=='Chris Webber':
      new_df = df[5:6]
      st.dataframe(new_df)
    if option=='Oscar Robertson':
      new_df = df[6:7]
      st.dataframe(new_df)
    if option=='Doug Christie':
      new_df = df[7:8]
      st.dataframe(new_df)
  with col2:
    if option=='Chris Webber':
      image = Image.open('star/Chris Webber.jpg')
      st.image(image)
    if option=='Oscar Robertson':
      image = Image.open('star/Oscar Robertson.jpg')
      st.image(image)
    if option=='Doug Christie':
      image = Image.open('star/Doug Christie.jpg')
      st.image(image)
