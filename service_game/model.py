#from typing import List, Optional
from pydantic import BaseModel, Field

class GamesConsoleCompany(BaseModel):
    game: str = Field(...,description="Game title") 
    console: str = Field(...,description="Console model") 
    company: str = Field(...,description="Company name") 


class GamesConsole(BaseModel):
    game: str = Field(...,description="Game title")
    console: str = Field(...,description="Console model")