import requests

new_row = {
    "G1": 0,
    "G2": 0,
    "G3": 0,
    "G4": 0,
    "G5": 0,
    "G6": 0,
    "G7": 0,
    "G8": 0,
    "G9": 0,
    "G10": 0,
}

result = requests.get("http://172.28.121.156:5000/", params=new_row)
print(result.json()["response"])
