from fastapi import APIRouter, status 
from .model import ApiResponse ,Classification
from .service import GamesService  

TAG = 'game_service'

router = APIRouter()

@router.get(
    "/get_top_10_games_console_company", 
    tags = [TAG],
    response_model = ApiResponse,
    responses={
        status.HTTP_200_OK: {
            "description":"""The top 10 best games for each console/company.""",
        }
    }
)
async def get_top_10_games_console_company( ):
    return GamesService.get_top_10_games_console_company( )


@router.get(
    "/get_top_10_games_consoles", 
    tags = [TAG],
    response_model = ApiResponse,
    responses={
        status.HTTP_200_OK: {
            "description":"The top 10 best games for each console.",
        }
    },
    response_model_exclude=["company"],
    response_model_exclude_defaults=True
)
async def get_top_10_games_consoles( ):
    return GamesService.get_top_10_games_consoles()


@router.get(
    "/get_worst_10_games_console_company", 
    tags = [TAG],
    response_model = ApiResponse,
    responses={
        status.HTTP_200_OK: {
            "description":"The worst 10 games for each console/company.",
        }
    }
)
async def get_worst_10_games_console_company( ):
    return GamesService.get_worst_10_games_console_company()



@router.get(
    "/get_worst_10_games_consoles", 
    tags = [TAG],
    response_model = ApiResponse,
    responses={
        status.HTTP_200_OK: {
            "description":"he worst 10 games for all consoles.",
        }
    },
    response_model_exclude=["company"],
    response_model_exclude_defaults=True
)
async def get_worst_10_games_consoles( ):
    return GamesService.get_worst_10_games_consoles()
 