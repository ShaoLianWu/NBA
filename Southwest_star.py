import streamlit as st  
from PIL import Image
import pandas as pd
import xlrd  
import openpyxl

df = pd.read_excel("star/Pacific_Southwest_star.xlsx",sheet_name="工作表1",usecols="A:H") 

def  Dallas_Maverick_Star():
  st.header('Boston Celtics三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Dirk Nowitzki', 'Derek Harper', 'Rolando Blackman'])
    if option=='Dirk Nowitzki':
      new_df = df[0:1]
      st.dataframe(new_df)
    if option=='Derek Harper':
      new_df = df[1:2]
      st.dataframe(new_df)
    if option=='Rolando Blackman':
      new_df = df[2:3]
      st.dataframe(new_df)
  with col2:
    if option=='Dirk Nowitzki':
      image = Image.open('star/Dirk Nowitzki.jpg')
      st.image(image)
    if option=='Derek Harper':
      image = Image.open('star/Derek Harper.jpg')
      st.image(image)
    if option=='Rolando Blackman':
      image = Image.open('star/Rolando Blackman.jpg')
      st.image(image)
      
def Houston_Rockets_star():
  st.header('Brooklyn Nets三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Hakeem Olajuwon', 'Moses Malone', 'Yao Ming'])
    if option=='Hakeem Olajuwon':
      new_df = df[5:6]
      st.dataframe(new_df)
    if option=='Moses Malone':
      new_df = df[6:7]
      st.dataframe(new_df)
    if option=='Yao Ming':
      new_df = df[7:8]
      st.dataframe(new_df)
  with col2:
    if option=='Hakeem Olajuwon':
      image = Image.open('star/Hakeem Olajuwon.jpg')
      st.image(image)
    if option=='Moses Malone':
      image = Image.open('star/Moses Malone.jpg')
      st.image(image)
    if option=='Yao Ming':
      image = Image.open('star/Yao Ming.jpg')
      st.image(image)
      
def Memphis_Grizzlies_star():
  st.header('New York Knicks三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Zach Randolph', 'Marc Gasol', 'Mike Miller'])
    if option=='Zach Randolph':
      new_df = df[9:10]
      st.dataframe(new_df)
    if option=='Marc Gasol':
      new_df = df[10:11]
      st.dataframe(new_df)
    if option=='Mike Miller':
      new_df = df[11:12]
      st.dataframe(new_df)
  with col2:
    if option=='Zach Randolph':
      image = Image.open('star/Zach Randolph.jpg')
      st.image(image)
    if option=='Marc Gasol':
      image = Image.open('star/Marc Gasol.jpg')
      st.image(image)
    if option=='Mike Miller':
      image = Image.open('star/Mike Miller.jpg')
      st.image(image)

def  New_Orleans_Pelicans_Star():
  st.header('Boston Celtics三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Pete Maravich', 'Chris Paul', 'Anthony Davis'])
    if option=='Pete Maravich':
      new_df = df[0:1]
      st.dataframe(new_df)
    if option=='Chris Paul':
      new_df = df[1:2]
      st.dataframe(new_df)
    if option=='Anthony Davis':
      new_df = df[2:3]
      st.dataframe(new_df)
  with col2:
    if option=='Pete Maravich':
      image = Image.open('star/Pete Maravich.jpg')
      st.image(image)
    if option=='Chris Paul':
      image = Image.open('star/Chris Paul.jepg')
      st.image(image)
    if option=='Anthony Davis':
      image = Image.open('star/Anthony Davis.jpg')
      st.image(image)
      
def San_Antonio_Spurs_star():
  st.header('Brooklyn Nets三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Tim Duncan', 'David Robinson', 'Manu Ginóbili'])
    if option=='Tim Duncan':
      new_df = df[5:6]
      st.dataframe(new_df)
    if option=='David Robinson':
      new_df = df[6:7]
      st.dataframe(new_df)
    if option=='Manu Ginóbili':
      new_df = df[7:8]
      st.dataframe(new_df)
  with col2:
    if option=='Tim Duncan':
      image = Image.open('star/Tim Duncan.jpg')
      st.image(image)
    if option=='David Robinson':
      image = Image.open('star/David Robinson.jpg')
      st.image(image)
    if option=='Manu Ginóbili':
      image = Image.open('star/Manu Ginóbili.jpg')
      st.image(image)
