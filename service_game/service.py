import pandas as pd
import json   
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

#from core import db, utils, env
from core.env import DIR_PROCESSED_DATA , API_NAME
from core.helpers import  error_handler 

class GamesService:

    @staticmethod 
    def get_top_10_games_console_company():
        try: 
            df=pd.read_csv(DIR_PROCESSED_DATA+'top_10_games_console_company.csv', sep=",")
            data = {
                "status": 200,
                "data":  df.to_dict('records')
            }
 
        except Exception as e:
            data =  error_handler(204, str(e))
        return data


    @staticmethod
    def get_top_10_games_consoles():
        try: 
            df=pd.read_csv(DIR_PROCESSED_DATA+'top_10_games_consoles.csv', sep=",")
            data = {
                "status": 200,
                "data":  df.to_dict('records')
            }
 
        except Exception as e:
            data =  error_handler(204, str(e))
        return data


    @staticmethod
    def get_worst_10_games_console_company():
        try: 
            df=pd.read_csv(DIR_PROCESSED_DATA+'worst_10_games_console_company.csv', sep=",")
            data = {
                "status": 200,
                "data":  df.to_dict('records')
            }
 
        except Exception as e:
            data =  error_handler(204, str(e))
        return data


    @staticmethod
    def get_worst_10_games_consoles():
        try: 
            df=pd.read_csv(DIR_PROCESSED_DATA+'worst_10_games_consoles.csv', sep=",")
            data = {
                "status": 200,
                "data":  df.to_dict('records')
            }
 
        except Exception as e:
            data =  error_handler(204, str(e))
        return data
 