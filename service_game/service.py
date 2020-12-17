import datetime
import pandas as pd
import json 
import requests
from io import StringIO
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

#from core import db, utils, env

class GamesService:

    @staticmethod
    def get_top_10_games_console_company():
  
        #df=pd.read_csv('data_ruta', sep=";")

        data = {
            "status": 200,
            "data":  0
        }
 

        return data