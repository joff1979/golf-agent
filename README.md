# Golf Agent

This project provides a simple API endpoint to parse natural language descriptions of golf hole performance into structured JSON data using a local Ollama language model.

## Features

*   Parses unstructured text about a golf hole (e.g., "Hole 5, made a par 4. Hit the fairway with driver, green in regulation with 8 iron. 2 putts.")
*   Extracts key information: hole number, score, fairway hit status, green in regulation status, number of putts, and clubs used.
*   Provides a FastAPI web server with a `/parse` endpoint.
*   Uses an Ollama model (configurable via environment variables) for the natural language processing task.

## Technology Stack

*   Python 3
*   FastAPI (for the web API)
*   Pydantic (for data validation)
*   Requests (for communicating with Ollama)
*   python-dotenv (for managing environment variables)
*   Ollama (for the local language model)

## Setup

1.  **Prerequisites:**
    *   Python 3.8+ installed.
    *   Ollama installed and running. Make sure the model specified in your environment variables (or the default 'mistral') is pulled (`ollama pull mistral`).

2.  **Clone the repository (if applicable):**
    ```bash
    # git clone <your-repo-url>
    # cd <your-repo-directory>/golf_agent
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv ../.venv # Create venv in the parent directory
    source ../.venv/Scripts/activate # On Windows Git Bash or Linux/macOS
    # or ..\.venv\Scripts\activate.bat # On Windows CMD
    # or ..\.venv\Scripts\Activate.ps1 # On Windows PowerShell
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    pip install requests # Add requests if not already in requirements.txt
    ```
    *Note: `requirements.txt` should ideally include `requests` and `python-dotenv` instead of just `dotenv`.*

5.  **Configure Environment Variables:**
    Create a `.env` file in the `research-env` directory (or wherever you run the script from) with the following content:
    ```dotenv
    # .env
    OLLAMA_URL=http://localhost:11434 # Replace if Ollama runs elsewhere
    OLLAMA_MODEL=mistral           # Replace with your desired Ollama model
    ```

## Usage

1.  **Run the API Server:**
    Navigate to the `research-env` directory in your terminal (the parent directory of `golf_agent`) and run:
    ```bash
    uvicorn golf_agent.main:app --reload --port 8000
    ```
    The API will be available at `http://localhost:8000`.

2.  **Send a Parsing Request:**
    You can use tools like `curl` or a web browser to send requests to the `/parse` endpoint.

    *Example using `curl`:*
    ```bash
    curl -X GET "http://localhost:8000/parse?input=Hole%205%2C%20made%20a%20par%204.%20Hit%20the%20fairway%20with%20driver%2C%20green%20in%20regulation%20with%208%20iron.%202%20putts."
    ```

    *Expected Response:*
    ```json
    {
      "hole": 5,
      "score": 4,
      "fairway": "hit",
      "green": "in regulation",
      "putts": 2,
      "clubs": ["driver", "8 iron"]
    }
    ```
    *(Note: The exact club list might vary based on the model's interpretation)*

## Modules

*   **`golf_parser.py`**: Contains the `parse_scorecard` function which takes a natural language string, constructs a prompt for the Ollama model, sends the request, and parses the JSON response.
*   **`main.py`**: Sets up the FastAPI application and defines the `/parse` endpoint which uses `parse_scorecard` to process requests.
*   **`requirements.txt`**: Lists the necessary Python packages.

