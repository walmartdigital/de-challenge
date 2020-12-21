from typing import List, Optional
from pydantic import BaseModel, Field

class Classification(BaseModel):
    
    name: str = Field(...,description="Game title") 
    console: str = Field(...,description="Console model") 
    company: Optional [str] = Field(description="Company name") 
    metascore:int  = Field(... , description="Score of game")
  
class ApiResponse(BaseModel ):
    status: int = Field(..., alias='status', description='Status code for response')
    data:  List[Classification]
