# golf_agent/round_manager.py
import os
import json
from datetime import datetime

ROUNDS_DIR = "golf_rounds"
os.makedirs(ROUNDS_DIR, exist_ok=True)

_active_round = None
_round_filename = None

def start_new_round(course_name: str):
    global _active_round, _round_filename
    today = datetime.now().strftime("%Y-%m-%d")
    _active_round = {
        "course": course_name,
        "date": today,
        "holes": []
    }
    safe_course = course_name.replace(" ", "_").lower()
    _round_filename = os.path.join(ROUNDS_DIR, f"{today}_{safe_course}.json")
    print(f"📗 New round started: {_round_filename}")

def add_hole_to_round(hole_data: dict):
    if not _active_round:
        raise RuntimeError("No round in progress. Call start_new_round(course_name) first.")
    _active_round["holes"].append(hole_data)
    print(f"➕ Hole {hole_data.get('hole', '?')} added to round")

def end_round(force_save: bool = False):
    if not _active_round:
        raise RuntimeError("No round in progress to end.")

    num_holes = len(_active_round["holes"])
    if num_holes < 18 and not force_save:
        raise ValueError(f"Only {num_holes} holes played. Use force_save=True to override.")

    with open(_round_filename, "w", encoding="utf-8") as f:
        json.dump(_active_round, f, indent=2)
    print(f"✅ Round saved with {num_holes} holes: {_round_filename}")

    # Clear active round
    clear_round()

def clear_round():
    global _active_round, _round_filename
    _active_round = None
    _round_filename = None

def load_rounds():
    rounds = []
    for filename in os.listdir(ROUNDS_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(ROUNDS_DIR, filename), "r", encoding="utf-8") as f:
                rounds.append(json.load(f))
    return rounds

def update_hole_in_round(hole_number: int, updated_data: dict):
    if not _active_round:
        raise RuntimeError("No round in progress to update.")

    for i, hole in enumerate(_active_round["holes"]):
        if hole.get("hole") == hole_number:
            _active_round["holes"][i].update(updated_data)
            print(f"✏️ Updated hole {hole_number} in round")
            return

    raise ValueError(f"Hole {hole_number} not found in current round")

def delete_hole_from_round(hole_number: int):
    if not _active_round:
        raise RuntimeError("No round in progress to delete from.")

    original_count = len(_active_round["holes"])
    _active_round["holes"] = [h for h in _active_round["holes"] if h.get("hole") != hole_number]

    if len(_active_round["holes"]) < original_count:
        print(f"🗑️ Deleted hole {hole_number} from round")
    else:
        raise ValueError(f"Hole {hole_number} not found in current round")

def update_saved_round(course_name: str, date: str, updated_data: dict):
    safe_course = course_name.replace(" ", "_").lower()
    filename = os.path.join(ROUNDS_DIR, f"{date}_{safe_course}.json")

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Round file not found: {filename}")

    with open(filename, "r", encoding="utf-8") as f:
        round_data = json.load(f)

    round_data.update(updated_data)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(round_data, f, indent=2)

    print(f"✏️ Updated round {filename}")

def delete_saved_round(course_name: str, date: str):
    safe_course = course_name.replace(" ", "_").lower()
    filename = os.path.join(ROUNDS_DIR, f"{date}_{safe_course}.json")

    if os.path.exists(filename):
        os.remove(filename)
        print(f"🗑️ Deleted round: {filename}")
    else:
        raise FileNotFoundError(f"Round file not found: {filename}")
