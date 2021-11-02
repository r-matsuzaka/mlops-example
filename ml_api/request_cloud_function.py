import requests

result = requests.post("https://asia-northeast1-mlops-331003.cloudfunctions.net/function-1", json={"msg": "Hello from cloud functions"})


print(result.json())
