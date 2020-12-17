from fastapi import APIRouter, status, Depends, Form
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Optional

from .model import GamesConsoleCompany, GamesConsole
from .service import GamesService

TAG = 'game_service'

router = APIRouter()

  
@router.get(
    "/get_top_10_games_console_company", 
    tags = [TAG],
    #response_model = GamesConsoleCompany,
    responses={
        status.HTTP_200_OK: {
            "description":"""The top 10 best games for each console/company.""",
        }
    }
)
async def get_top_10_games_console_company( ):
    return GamesService.get_top_10_games_console_company( )




@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/s1")
def service_one():
    """
    lorem 
    loreDuis laboris nisi et enim pariatur quis aliqua nulla quis dolor. Reprehenderit tempor labore laboris veniam est et excepteur tempor anim sit cupidatat pariatur officia culpa. Officia aliqua deserunt consequat dolore esse aliquip et enim do nostrud nulla. Reprehenderit cupidatat Lorem anim sit eiusmod non eiusmod ipsum ullamco occaecat. Deserunt excepteur ipsum magna nostrud pariatur non amet.

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return {"s1": "Bienvenido"}


    