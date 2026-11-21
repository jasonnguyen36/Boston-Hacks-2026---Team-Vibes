# Backend — Boston Unscripted

## Overview

The backend handles activity recommendations, user preferences, budget tracking, and adventure history. It uses Python and Flask to process frontend requests and return activity recommendations in JSON format.

## Tech Stack

- Python
- Flask
- Flask-CORS
- JSON

## File Descriptions

| File | Purpose |
|---|---|
| `app.py` | Main Flask server. Receives frontend requests and returns backend responses. |
| `recommendations.py` | Filters activities based on budget, group size, category, location, and previously visited activities. Randomly selects up to two eligible activities. |
| `adventure.py` | Manages adventure sessions, user decisions, remaining budget, and activity history. |
| `activities.json` | Contains temporary sample activity data for testing recommendations. |
| `test_recommendations.py` | Contains automated tests for recommendation and adventure logic. |
| `requirements.txt` | Lists the Python dependencies needed to run the backend. |
| `.gitignore` | Excludes virtual environments, cache files, and other unnecessary files from GitHub. |

## Running the Backend

From the backend directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

The server runs at `http://127.0.0.1:5000`.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check server status |
| POST | `/api/adventures` | Start an adventure and generate initial recommendations |
| GET | `/api/adventures/{id}` | Retrieve current adventure information |
| POST | `/api/adventures/{id}/complete` | Complete an activity, update the budget, and generate new recommendations |
| POST | `/api/adventures/{id}/finish` | Return the final adventure history and spending summary |

## Backend Logic

1. Receive the user's budget, group size, categories, and preferred location.
2. Filter the available activities based on these preferences.
3. Return up to two eligible activities.
4. Record the user's chosen activity and alternative option.
5. Update the remaining budget and visited activities.
6. Generate the next set of recommendations.
7. Return the complete adventure history when the user finishes.

## Testing

```bash
python -m unittest test_recommendations -v
```

## Current Status

- [x] Activity filtering
- [x] Recommendation generation
- [x] Budget tracking
- [x] Completed activity tracking
- [x] Adventure history
- [x] Flask API endpoints
- [x] Local testing
- [ ] Real-world activity data integration
- [ ] Frontend integration
- [ ] Deployment

## Current Limitations

The backend currently uses sample activity data from `activities.json`. Adventure sessions are stored in memory and reset when the server restarts. Real-world activity data and persistent storage can be integrated later.
