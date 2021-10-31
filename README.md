# mlops-example


# How to run
## Set up
`source local.env`
`poetry install`


## No UI
1. Create and save model

`poetry run python ml_api/model.py`  

2. Setup server

`poetry run python ml_api/server.py`  


3. Request prediction

`poetry run python ml_api/request.py`

## With UI
1. Create and save model

`poetry run python ml_api/model.py`  

2. Setup server

`poetry run python ml_api/dash_server.py`  



## Reference
https://github.com/bgweber/DS_Production

https://www.amazon.co.jp/Data-Science-Production-Building-Pipelines/dp/165206463X