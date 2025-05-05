# golf_agent/main.py
from fastapi import FastAPI, Depends
# Corrected imports based on new structure
# Remove unused imports if parse_scorecard etc. are only used in routes
# from app.services.parser import parse_scorecard
# from app.services.round_manager import (
#     start_new_round,
#     add_hole_to_round,
#     end_round,
#     load_rounds
# )
from app.services.round_manager import router as round_manager_router # Renamed for clarity
from app.api.routes import router as api_router # Import the new API router
from app.auth import verify_api_key # Corrected import

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(dependencies=[Depends(verify_api_key)])

# Include routers
app.include_router(round_manager_router) # Include router from round_manager
app.include_router(api_router) # Include the main API router