# golf_agent/golf_parser.py
from dotenv import load_dotenv
load_dotenv()

import os
import json
import requests
from typing import Optional, Dict, Any, List

OLLAMA_BASE_URL = os.getenv("OLLAMA_HOST", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "mistral")

DEFAULT_SCORE_DATA: Dict[str, Any] = {
    "hole": None,
    "score": None,
    "fairway": None,
    "green": None,
    "putts": None,
    "clubs": []
}

def parse_scorecard(note: str) -> Optional[Dict[str, Any]]:
    """
    Parses a natural language golf note to extract structured scorecard data for a single hole using an Ollama model.

    Args:
        note: The natural language text describing the play on a hole.

    Returns:
        A dictionary containing the parsed score data (hole, score, fairway, green, putts, clubs)
        or None if parsing fails or communication with Ollama fails.
    """

    
    prompt = f"""
        You are a golf score parser. Given a natural language input, extract structured score data for one or more holes.

        Input: "{note}"

        Output as a JSON array of objects. Each object should include:
        - hole (int)
        - score (int)
        - fairway ("hit" / "miss left/right")
        - green ("in regulation" or "miss short/long/left/right")
        - putts (int)
        - clubs (list of strings)

        Return pure JSON only — no comments, no explanation.
    """


    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload, timeout=30) # Added timeout
        response.raise_for_status()
        raw = response.json().get("response", "").strip()
         # DEBUG: print raw content
        print("🔎 Raw Ollama response:", raw)

        # If the response starts with '[' assume it's a JSON list string
        if raw.startswith("["):
            return json.loads(raw)
        else:
            raise ValueError("Response was not a valid JSON array")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error communicating with Ollama: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"⚠️ Error decoding JSON response: {e}")
        print(f"Raw content: {raw}") # Log raw content for debugging
        return None
    except Exception as e: # Catch other potential exceptions
        print(f"⚠️ An unexpected error occurred: {e}")
        return None

# Example usage (optional, can be removed or placed in main.py)
if __name__ == "__main__":
    test_note = "Hole 5, made a par 4. Hit the fairway with driver, green in regulation with 8 iron. 2 putts."
    parsed_data = parse_scorecard(test_note)
    if parsed_data:
        print("Parsed Score Data:")
        print(json.dumps(parsed_data, indent=2))
    else:
        print("Failed to parse scorecard.")

    test_note_fail = "Just had a great time on the course today."
    parsed_data_fail = parse_scorecard(test_note_fail)
    if parsed_data_fail:
         print("\nParsed Score Data (Fail Case):")
         print(json.dumps(parsed_data_fail, indent=2))
    else:
        print("\nFailed to parse scorecard (Fail Case).")
