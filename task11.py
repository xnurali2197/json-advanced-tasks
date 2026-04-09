import json

with open("products.json") as f:
    data=json.load(f)

for x in data:
    x["sum"]=x["price"]*x.get("amount",1)

print(sum(x["sum"] for x in data))
