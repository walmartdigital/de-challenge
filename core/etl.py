
import pandas as pd 
 
DIR_DATA = '/root/data/'
 
def get_data():
    global DIR_DATA
    df_consoles = pd.read_csv(DIR_DATA+'consoles.csv' , sep=',')
    df_result = pd.read_csv(DIR_DATA+'result.csv' , sep=',')
    return df_consoles , df_result


def tranform_data( df_consoles , df_result) :
    
    TOP_N =10
    df_dic = {} 
    
    df_merge = df_result.merge(df_consoles , how='left')
    df_game_con_compa = df_merge.groupby(['name' , "console","company"])["metascore"].mean().sort_values(0 ,ascending=False).reset_index( )
    df_game_con = df_merge.groupby(['name' , "console" ])["metascore"].mean().sort_values(0 ,ascending=False).reset_index( )
      
    df_dic['tcc']=df_game_con_compa.head(TOP_N)
    df_dic['wcc']=df_game_con_compa.tail(TOP_N)
    df_dic['tc']=df_game_con_compa.head(TOP_N)
    df_dic['wc']=df_game_con_compa.tail(TOP_N)
     
    return df_dic


def save_data(df_dic):
    df_dic['tcc'].to_csv('top_10_games_console_company.csv' , index=False)
    df_dic['wcc'].to_csv('top_10_games_consoles.csv' , index=False)
    df_dic['tc'].to_csv('worst_10_games_console_company.csv' , index=False)
    df_dic['wc'].to_csv('worst_10_games_consoles.csv' , index=False)


try:
    df_consoles , df_result = get_data() 
    df_dic = tranform_data(df_consoles , df_result) 
    save_data(df_dic) 
    print("Job completed")

except Exception as e:
     print(f"Job fail : {e}")
