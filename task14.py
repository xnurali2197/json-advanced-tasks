import json

def load():
    try:
        return json.load(open("db.json"))
    except:
        return []
