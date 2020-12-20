from fastapi import  FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from core.env import   URL_PREFIX , API_NAME,API_VERSION

from service_game import controller as game 
from core.base_model import ErrorResponse
 
app = FastAPI(
    root_path= f'{URL_PREFIX}',
    title = API_NAME,
    version = API_VERSION ,
    docs_url="/docs",
    reload =True
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(
    game.router,
    prefix = f'/{game.TAG}',
    tags=[game.TAG],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ErrorResponse,
            "description": "Internal server error"
        },
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorResponse,
            "description": "Unauthorized"
        }
    }
)
