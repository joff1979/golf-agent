# golf_agent/main.py
from fastapi import FastAPI, HTTPException, Query, Depends, Header
from pydantic import BaseModel
from golf_parser import parse_scorecard   # ✅ must match actual import
from round_manager import (
    start_new_round,
    add_hole_to_round,
    end_round,
    load_rounds
)
from round_manager import router as round_router
from auth import verify_api_key

app = FastAPI(dependencies=[Depends(verify_api_key)])
app.include_router(round_router)

class ParsedResult(BaseModel):
    hole: int
    score: int
    fairway: str | None = None
    green: str | None = None
    putts: int | None = None
    clubs: list[str] | None = []
   
import os

API_KEY = os.getenv("API_KEY")

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.get("/parse")
def parse(input: str = Query(...)):
    results = parse_scorecard(input)

    if isinstance(results, list):
        for hole in results:
            add_hole_to_round(hole)
    elif isinstance(results, dict):
        add_hole_to_round(results)
    else:
        raise HTTPException(status_code=400, detail="Invalid parse result structure")

    return results

@app.post("/start_round")
def start_round(course: str = Query(...)):
    round_id = start_new_round(course)
    return {"message": f"Started new round at {course}", "round_id": round_id}

@app.post("/end_round", dependencies=[Depends(verify_api_key)])
def end(force: bool = Query(False)):
    try:
        end_round(force_save=force)
        return {"message": "Round saved successfully"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    
from fastapi.responses import JSONResponse

@app.get("/rounds")
def list_saved_rounds():
    try:
        rounds = load_rounds()
        return JSONResponse(content=rounds)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})