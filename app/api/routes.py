from fastapi import APIRouter, Query, HTTPException, Depends
from app.services.parser import parse_scorecard
from app.services.round_manager import add_hole_to_round
from app.auth import verify_api_key

router = APIRouter()

@router.get("/parse", dependencies=[Depends(verify_api_key)])
def parse(input: str = Query(...)):
    results = parse_scorecard(input)

    if isinstance(results, list):
        for hole in results:
            # Assuming add_hole_to_round expects a dictionary or Pydantic model
            # If results contains Pydantic models, convert them if necessary
            if hasattr(hole, 'dict'):
                add_hole_to_round(hole.dict())
            else:
                 add_hole_to_round(hole) # Assuming it's already a dict
    elif isinstance(results, dict):
         add_hole_to_round(results)
    elif hasattr(results, 'dict'): # Handle single Pydantic model result
        add_hole_to_round(results.dict())
    else:
        raise HTTPException(status_code=400, detail="Invalid parse result structure")

    return results

# Add other routes here later...