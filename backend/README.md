# Boston Unscripted backend
Sample activities are fictional placeholders with estimated prices and group limits. Replace them with your teammate's normalized data. Budget is per person in whole dollars. Run locally only; no authentication or persistent storage.

## Run
`python3 -m venv .venv` then `source .venv/bin/activate`, `python -m pip install -r requirements.txt`, `python app.py`.

## API
Base URL: http://127.0.0.1:5000
- POST /api/adventures with {"budget":50,"groupSize":4,"categories":["All"],"location":"Back Bay"}. Returns adventureId, options and state.
- POST /api/adventures/{adventureId}/complete with {"chosenId":1} (use an ID from current options). Call after finishing the chosen activity. Returns updated state and next options.
- GET /api/adventures/{adventureId} returns current state.
- POST /api/adventures/{adventureId}/finish returns summary including both options and choice for every completed step.
- Options may contain 0, 1 or 2 entries. Frontend should handle all cases. Declined activities may appear again; completed ones cannot.

Run logic tests: `python3 -m unittest test_recommendations`.
