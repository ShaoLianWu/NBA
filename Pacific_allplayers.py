import streamlit as st  
import pandas as pd
import xlrd  
import openpyxl
def BostonCeltics_allplayers():
  df = pd.read_excel("star/sportsref_download.xls") 
  st.dataframe(df)
