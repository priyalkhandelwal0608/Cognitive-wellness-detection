import json
import os

db_path = os.path.join(os.path.dirname(__file__), "activity_db.json")
with open(db_path, "r") as f:
    activity_db = json.load(f)

def recommend_activity(state):
    return activity_db.get(state, "Take a short break and recharge.")