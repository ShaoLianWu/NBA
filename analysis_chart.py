import streamlit as st  #streamlit套件
import xlrd             #excel套件
import openpyxl         #excel套件
import pandas as pd     #pandas套件(資料分析)
import matplotlib.pyplot as plt #matplotlib(資料繪圖)
import seaborn as sns
def analysis_chart(option_teams):
    data_list={"三分球命中率":"3P%","兩分球命中率":"2P%","罰球命中率":"FT%","投籃命中率":"FG%","進攻籃板":"ORB","防守籃板":"DRB",
               "總籃板數":"TRB","總助攻":"AST","總抄截":"STL","總火鍋":"BLK","總失誤":"TOV","犯規次數":"PF","總得分":"PTS"}
    teams_data=pd.read_excel("data/nbateamsdata.xlsx",sheet_name=option_teams) 
    league_data=pd.read_excel("data/nbateamsdata.xlsx",sheet_name="LeagueAverage") 
    col1,col2=st.columns((4,6))
    with col1:
        option_data = st.selectbox('想查看數據？',data_list)
    with col2:
#-----折線圖---------------------------------------------------------------
        if option_data=='三分球命中率':
            plt.style.use("ggplot")
            plt.plot(teams_data.年度,teams_data.三分球命中率 ,'.-' ) 
            plt.plot(league_data.年度,league_data.三分球命中率,'.-' )
             
        if option_data=='兩分球命中率':
            plt.style.use("ggplot")
            plt.plot(teams_data.年度,teams_data.兩分球命中率 ,'.-' ) 
            plt.plot(league_data.年度,league_data.兩分球命中率,'.-' )        
            
        if option_data=='罰球命中率':
            plt.style.use("ggplot")
            plt.plot(teams_data.年度,teams_data.罰球命中率 ,'.-' ) 
            plt.plot(league_data.年度,league_data.罰球命中率,'.-' )
                  
        if option_data=='投籃命中率':
            plt.style.use("ggplot")
            plt.plot(teams_data.年度,teams_data.投籃命中率 ,'.-' ) 
            plt.plot(league_data.年度,league_data.投籃命中率,'.-' )
#-----長條圖---------------------------------------------------------------            
        if option_data=='進攻籃板':
           width=0.25
           x1=teams_data.年度
           y1=teams_data.進攻籃板
           x2=[p + width for p in x1]   
           y2=league_data.進攻籃板
           plt.bar(x1,y1)
           plt.bar(x2,y2)   
           plt.xticks([p + width/2 for p in x1], x1)   
           
            
        if option_data=='防守籃板': 
           plt.bar(teams_data.年度,teams_data.防守籃板)
           plt.bar(league_data.年度,league_data.防守籃板)   
     
        if option_data=='總籃板數': 
           plt.bar(teams_data.年度,teams_data.總籃板數)
           plt.bar(league_data.年度,league_data.總籃板數)   
       
        if option_data=='總助攻': 
           plt.bar(teams_data.年度,teams_data.總助攻)
           plt.bar(league_data.年度,league_data.總助攻)  
        
        if option_data=='總抄截': 
           plt.bar(teams_data.年度,teams_data.總抄截)
           plt.bar(league_data.年度,league_data.總抄截)  
            
        if option_data=='總火鍋': 
           plt.bar(teams_data.年度,teams_data.總火鍋)
           plt.bar(league_data.年度,league_data.總火鍋)       
        
        if option_data=='總失誤': 
           plt.bar(teams_data.年度,teams_data.總失誤)
           plt.bar(league_data.年度,league_data.總失誤)    
         
        if option_data=='犯規次數': 
           plt.bar(teams_data.年度,teams_data.犯規次數)
           plt.bar(league_data.年度,league_data.犯規次數)    
        
        if option_data=='總得分':
           plt.bar(teams_data.年度,teams_data.總得分)
           plt.bar(league_data.年度,league_data.總得分)  
#-----顯示圖表------------------------------------------------------------------------
        plt.xlabel('Season',fontsize="10")
        plt.title(option_teams+" "+data_list[option_data]+" vs League Average")
        plt.legend(labels=[option_teams+" "+data_list[option_data],"League Average "+data_list[option_data]], loc = 'best')
        st.pyplot(plt)
        
#-----TOP10RANK👑-----------------------------------------------------------------------------------------------------
def TOP10RANK(option_teams):
    st.markdown('### TOP 10 RANK👑')
    rank_data = pd.read_excel("data/Rank.xlsx",sheet_name=option_teams)
    col1,col2,col3=st.columns(3)
    with col1:
      rank_data.sort_values(by='Games',inplace=True,ascending=False)
      fig, ax = plt.subplots()
      ax = sns.barplot(x=rank_data.Games, y=rank_data.PLAYER)
      ax.set_title(option_teams+' TOP 10 Rank to Games')
      ax.set(xlabel="Games" , ylabel='PLAYER')
      st.pyplot(fig)

    with col2:
      rank_data.sort_values(by='MinutesPlayed',inplace=True,ascending=False)
      fig, ax = plt.subplots()
      ax = sns.barplot(x=rank_data.MinutesPlayed, y=rank_data.PLAYER1)
      ax.set_title(option_teams+' TOP 10 Rank to Minutes Played')
      ax.set(xlabel="Minutes Played" ,ylabel='PLAYER')
      st.pyplot(fig)

    with col3:
     rank_data.sort_values(by='FieldGoals',inplace=True,ascending=False)
     fig, ax = plt.subplots()
     ax = sns.barplot(x=rank_data.FieldGoals, y=rank_data.PLAYER2)
     ax.set_title(option_teams+' TOP 10 Rank to Field Goals')
     ax.set( xlabel="Field Goals",ylabel='PLAYER')
     st.pyplot(fig)
    x=st.button('點取看更多')
    if x:
        col4,col5,col6=st.columns(3)
        with col4:  
          rank_data.sort_values(by='PtFieldGoals',inplace=True,ascending=False)
          fig, ax = plt.subplots()
          ax = sns.barplot(x=rank_data.PtFieldGoals, y=rank_data.PLAYER3)
          ax.set_title(option_teams+' TOP 10 Rank to 3-Pt Field Goals')
          ax.set( xlabel="3-Pt Field Goals",ylabel='PLAYER')
          st.pyplot(fig)

        with col5:
          rank_data.sort_values(by='FreeThrows',inplace=True,ascending=False)
          fig, ax = plt.subplots()
          ax = sns.barplot(x=rank_data.FreeThrows, y=rank_data.PLAYER4)
          ax.set_title(option_teams+' TOP 10 Rank to Free Throws')
          ax.set( xlabel="Free Throws",ylabel='PLAYER')
          st.pyplot(fig)

        with col6:  
          rank_data.sort_values(by='TotalRebounds',inplace=True,ascending=False)
          fig, ax = plt.subplots()
          ax = sns.barplot(x=rank_data.TotalRebounds, y=rank_data.PLAYER5)
          ax.set_title(option_teams+' TOP 10 Rank to Total Rebounds')
          ax.set( xlabel="Total Rebounds",ylabel='PLAYER')
          st.pyplot(fig)
        col7,col8,col9=st.columns(3)
        with col7:
           rank_data.sort_values(by='Assists',inplace=True,ascending=False)
           fig, ax = plt.subplots()
           ax = sns.barplot(x=rank_data.Assists, y=rank_data.PLAYER6)
           ax.set_title(option_teams+' TOP 10 Rank to Assists')
           ax.set( xlabel="Assists",ylabel='PLAYER')
           st.pyplot(fig)
        with col8:
           rank_data.sort_values(by='Steals',inplace=True,ascending=False)
           fig, ax = plt.subplots()
           ax = sns.barplot(x=rank_data.Steals, y=rank_data.PLAYER7)
           ax.set_title(option_teams+' TOP 10 Rank to Steals')
           ax.set( xlabel="Steals",ylabel='PLAYER')
           st.pyplot(fig)
        with col9:
            rank_data.sort_values(by='Blocks',inplace=True,ascending=False)
            fig, ax = plt.subplots()
            ax = sns.barplot(x=rank_data.Blocks, y=rank_data.PLAYER8)
            ax.set_title(option_teams+' TOP 10 Rank to Blocks')
            ax.set( xlabel="Blocks",ylabel='PLAYER')
            st.pyplot(fig)
