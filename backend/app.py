import json
from pathlib import Path
from uuid import uuid4
from flask import Flask, jsonify, request
from flask_cors import CORS
from adventure import start_adventure, complete_activity, finish_adventure

app = Flask(__name__)
CORS(app)  # Local hackathon development only; restrict origins before public deployment.
activities = json.loads(Path(__file__).with_name('activities.json').read_text())
adventures = {}  # In-memory prototype: restarting the server clears adventures.

@app.get('/')
def home():
    return jsonify(message='Boston Unscripted backend is running!')

@app.post('/api/adventures')
def start():
    p = request.get_json(silent=True)
    if not isinstance(p, dict):
        return jsonify(error='Expected a JSON object'), 400
    budget, group, categories, location = (p.get(k) for k in ('budget', 'groupSize', 'categories', 'location'))
    if (type(budget) is not int or budget < 0 or type(group) is not int or group < 1
        or not isinstance(categories, list) or not categories or not all(isinstance(c, str) for c in categories)
        or not isinstance(location, str) or not location.strip()):
        return jsonify(error='Provide a nonnegative integer budget, positive groupSize, categories list and location'), 400
    adventure_id = str(uuid4())
    state = start_adventure(activities, p)
    adventures[adventure_id] = state
    return jsonify(adventureId=adventure_id, **state), 201

@app.post('/api/adventures/<adventure_id>/complete')
def complete(adventure_id):
    state = adventures.get(adventure_id)
    if state is None:
        return jsonify(error='Adventure not found'), 404
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or type(data.get('chosenId')) is not int:
        return jsonify(error='Provide an integer chosenId'), 400
    try:
        return jsonify(adventureId=adventure_id, **complete_activity(activities, state, data['chosenId']))
    except ValueError as e:
        return jsonify(error=str(e)), 400

@app.get('/api/adventures/<adventure_id>')
def get_adventure(adventure_id):
    state = adventures.get(adventure_id)
    if state is None:
        return jsonify(error='Adventure not found'), 404
    return jsonify(adventureId=adventure_id, **state)

@app.post('/api/adventures/<adventure_id>/finish')
def finish(adventure_id):
    state = adventures.get(adventure_id)
    if state is None:
        return jsonify(error='Adventure not found'), 404
    return jsonify(adventureId=adventure_id, **finish_adventure(state))

if __name__ == '__main__':
    app.run(port=5000)
