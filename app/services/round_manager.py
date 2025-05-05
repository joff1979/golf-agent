# golf_agent/round_manager.py
import os
import json
import uuid
from datetime import datetime
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

ROUNDS_DIR = "golf_rounds"
os.makedirs(ROUNDS_DIR, exist_ok=True)

_active_round = None
_round_filename = None

router = APIRouter()

class Hole(BaseModel):
    hole: int
    score: int | None
    fairway: str
    green: str
    putts: int | None
    clubs: list[str]

class RoundUpdate(BaseModel):
    course: str | None = None
    date: str | None = None
    holes: list[Hole] | None = None

def start_new_round(course_name: str):
    global _active_round, _round_filename
    today = datetime.now().strftime("%Y-%m-%d")
    round_id = str(uuid.uuid4())[:8]
    _active_round = {
        "round_id": round_id,
        "course": course_name,
        "date": today,
        "holes": []
    }
    _round_filename = os.path.join(ROUNDS_DIR, f"{round_id}.json")
    print(f"📗 New round started: {_round_filename}")
    return round_id

@router.post("/start_round")
def api_start_round(course: str):
    round_id = start_new_round(course)
    return {"message": f"Started new round at {course}", "round_id": round_id}

def add_hole_to_round(hole_data: dict):
    if not _active_round:
        raise RuntimeError("No round in progress. Call start_new_round(course_name) first.")
    _active_round["holes"].append(hole_data)
    print(f"➕ Hole {hole_data.get('hole', '?')} added to round")

@router.post("/add_hole")
def api_add_hole(hole: Hole):
    add_hole_to_round(hole.dict())
    return {"message": f"Hole {hole.hole} added"}

def end_round(force_save: bool = False):
    if not _active_round:
        raise RuntimeError("No round in progress to end.")

    num_holes = len(_active_round["holes"])
    if num_holes < 18 and not force_save:
        raise ValueError(f"Only {num_holes} holes played. Use force_save=True to override.")

    with open(_round_filename, "w", encoding="utf-8") as f:
        json.dump(_active_round, f, indent=2)
    print(f"✅ Round saved with {num_holes} holes: {_round_filename}")

    clear_round()

@router.post("/end_round")
def api_end_round(force: bool = False):
    try:
        end_round(force_save=force)
        return {"message": "Round saved."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def clear_round():
    global _active_round, _round_filename
    _active_round = None
    _round_filename = None

def load_rounds():
    rounds = []
    for filename in os.listdir(ROUNDS_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(ROUNDS_DIR, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                data["round_id"] = filename.replace(".json", "")
                rounds.append(data)
    return rounds

@router.get("/rounds")
def api_get_rounds():
    return load_rounds()

def update_hole_in_round(hole_number: int, updated_data: dict):
    if not _active_round:
        raise RuntimeError("No round in progress to update.")

    for i, hole in enumerate(_active_round["holes"]):
        if hole.get("hole") == hole_number:
            _active_round["holes"][i].update(updated_data)
            print(f"✏️ Updated hole {hole_number} in round")
            return

    raise ValueError(f"Hole {hole_number} not found in current round")

@router.put("/update_hole/{hole_number}")
def api_update_hole(hole_number: int, hole: Hole):
    try:
        update_hole_in_round(hole_number, hole.dict())
        return {"message": f"Hole {hole_number} updated"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def delete_hole_from_round(hole_number: int):
    if not _active_round:
        raise RuntimeError("No round in progress to delete from.")

    original_count = len(_active_round["holes"])
    _active_round["holes"] = [h for h in _active_round["holes"] if h.get("hole") != hole_number]

    if len(_active_round["holes"]) < original_count:
        print(f"🗑️ Deleted hole {hole_number} from round")
    else:
        raise ValueError(f"Hole {hole_number} not found in current round")

@router.delete("/delete_hole/{hole_number}")
def api_delete_hole(hole_number: int):
    try:
        delete_hole_from_round(hole_number)
        return {"message": f"Hole {hole_number} deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def update_saved_round(round_id: str, updated_data: dict):
    filename = os.path.join(ROUNDS_DIR, f"{round_id}.json")

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Round file not found: {filename}")

    with open(filename, "r", encoding="utf-8") as f:
        round_data = json.load(f)

    round_data.update(updated_data)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(round_data, f, indent=2)

    print(f"✏️ Updated round {filename}")

@router.put("/update_round/{round_id}")
def api_update_saved_round(round_id: str, update: RoundUpdate):
    try:
        update_saved_round(round_id, update.dict(exclude_unset=True))
        return {"message": "Round updated"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def delete_saved_round(round_id: str):
    filename = os.path.join(ROUNDS_DIR, f"{round_id}.json")

    if os.path.exists(filename):
        os.remove(filename)
        print(f"🗑️ Deleted round: {filename}")
    else:
        raise FileNotFoundError(f"Round file not found: {filename}")

@router.delete("/delete_round/{round_id}")
def api_delete_saved_round(round_id: str):
    try:
        delete_saved_round(round_id)
        return {"message": "Round deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
