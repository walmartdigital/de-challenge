
import pandas as pd 
#import etl as etl 
from helpers import this_function,Emoji ,log , make_folder
from env import (DIR_PROCESSED_DATA , DIR_DATA)
 

def get_data(path : str): 
    
    global DIR_DATA

    df_consoles = pd.read_csv(path+'consoles.csv' , sep=',')
    df_result = pd.read_csv(path+'result.csv' , sep=',')
    print(f"{Emoji.ok} {this_function()}")
    return df_consoles , df_result


def transform_data( df_consoles , df_result) :
    
    TOP_N =10
    df_dic = {} 
    
    df_merge = df_result.merge(df_consoles , how='left')

    df_game_con_compa = df_merge.groupby(['name' , "console","company"])["metascore"].mean().sort_values(0 ,ascending=False).reset_index( )

    df_game_con = df_merge.groupby(['name' , "console" ])["metascore"].mean().sort_values(0 ,ascending=False).reset_index( )
      
    df_dic['tcc']=df_game_con_compa.head(TOP_N)
    df_dic['wcc']=df_game_con_compa.tail(TOP_N)
    df_dic['tc']=df_game_con.head(TOP_N)
    df_dic['wc']=df_game_con.tail(TOP_N)
    
    print(f"{Emoji.ok} {this_function()}")

    return df_dic


def save_data(df_dic):
    global DIR_PROCESSED_DATA 

    make_folder(DIR_PROCESSED_DATA , 755)
 
    df_dic['tcc'].to_csv(DIR_PROCESSED_DATA+'top_10_games_console_company.csv' , index=False)
    df_dic['wcc'].to_csv(DIR_PROCESSED_DATA+'top_10_games_consoles.csv' , index=False)
    df_dic['tc'].to_csv(DIR_PROCESSED_DATA+'worst_10_games_console_company.csv' , index=False)
    df_dic['wc'].to_csv(DIR_PROCESSED_DATA+'worst_10_games_consoles.csv' , index=False)

    print(f"{Emoji.ok} {this_function()}")


def start_etl():
    global DIR_DATA
    print(f"Start ETL's stages {Emoji.race}")
    df_consoles , df_result = get_data(DIR_DATA) 
    df_dic = transform_data(df_consoles , df_result) 
    save_data(df_dic)

    print(f"{Emoji.ok} {this_function()} completed")

try:
    start_etl() 
except Exception as e:
     print(f"Job fail : {log(e)}")
