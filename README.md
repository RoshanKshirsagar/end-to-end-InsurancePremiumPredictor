# end-to-end-InsurancePremiumPredictor
## Problem Statement
The goal of this project is to give people an estimate of how much they need based on
their individual health situation. After that, customers can work with any health
insurance carrier and its plans and perks while keeping the projected cost from our
study in mind. This can assist a person in concentrating on the health side of an
insurance policy rather han the ineffective part.

## Solution Proposed
The project focuses on predicting the premium amount for an individual so that he can choose 
an appropriate one. We are using an Machine learning model to get a prediction. This model gets 
the data of the user and after processing it predicts the premium amount.
There are two solution for this :
1. Batch Predictor (generates an csv file with predicted value)
2. Instance Predictor (an User Interface is provided to user)

## Tech Stack Used
1. Python 
2. MongoDB Database
3. Machine learning Algorithm
4. Streamlit

## How to use
Step 1- Clone this repository
```
git clone https://github.com/RoshanKshirsagar/end-to-end-InsurancePremiumPredictor.git
```

Step 2- We need to create an virtual enviornment to install our dependencies
```
conda create -n insur python=3.7 -y
conda activate insur
```
Step 3- Get data into local
```
wget https://github.com/RoshanKshirsagar/end-to-end-InsurancePremiumPredictor/blob/main/insurance.csv
```
Step 4- Set Mongo Client with your atlas url
```
client = pymongo.MongoClient(mongodb_url)
```
Step 5- Dump the dataset inside mongodb
```
python data_dump.py
```
Step 6- Install requirements
```
pip install -r requirements.txt
```
Step 7- For Batch Prediction (change filepath)
```
python batch_predictor.py
```
Step 8- For Instance Prediction
```
streamlit run app.py
```
