# mlops-example


# How to run

## Create GCP projects
That's it.

## Prepare GCP credentials
```
gcloud auth login  
gcloud init  
gcloud iam service-accounts create dsdemo  
your_project_id={enter your project_id}  
gcloud projects add-iam-policy-binding $your_project_id  --member "serviceAccount:dsdemo@$your_project_id.iam.gserviceaccount.com" --role "roles/owner"  
gcloud iam service-accounts keys  create dsdemo.json --iam-account  dsdemo@$your_project_id.iam.gserviceaccount.com  
```

Weber, Ben. Data Science in Production: Building Scalable Model Pipelines with Python (p.17). Kindle 版. 

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