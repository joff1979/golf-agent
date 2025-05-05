\
from pydantic import BaseModel
from typing import List, Optional

class ParsedResult(BaseModel):
    hole: int
    score: int
    fairway: Optional[str] = None
    green: Optional[str] = None
    putts: Optional[int] = None
    clubs: Optional[List[str]] = []

class Hole(BaseModel):
    hole: int
    score: Optional[int]
    fairway: Optional[str] # Changed to Optional to match usage
    green: Optional[str] # Changed to Optional to match usage
    putts: Optional[int]
    clubs: Optional[List[str]] = [] # Changed to Optional and added default

class RoundUpdate(BaseModel):
    course: Optional[str] = None
    date: Optional[str] = None
    holes: Optional[List[Hole]] = None

class Round(BaseModel):
    round_id: str
    course: str
    date: str
    holes: List[Hole]
