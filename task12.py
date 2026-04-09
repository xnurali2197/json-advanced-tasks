import json

with open("old.json") as f: old=json.load(f)
with open("new.json") as f: new=json.load(f)

res={u["id"]:u for u in old+new}
