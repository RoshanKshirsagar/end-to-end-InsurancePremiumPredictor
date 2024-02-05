import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import pickle
import xgboost as xg
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

# Loading the objects
model = pickle.load(open('model.pkl','rb'))
encoder = pickle.load(open('target_encoder.pkl','rb'))
transformer = pickle.load(open('transformer.pkl','rb'))

st.title("Insurance Premium Prediction")
age = st.text_input('Enter Age', 18)
age = int(age)

sex = st.selectbox('Please select gender',('male', 'female'))

bmi = st.text_input('Enter BMI', 20)
bmi = float(bmi)

children = st.selectbox('Please select number of children ',(0,1,2,3,4,5))
children = int(children)

smoker = st.selectbox('Please select smoker category ',("yes","no"))

region = st.selectbox('Please select region ',
                      ("southwest", "southeast", "northeast", "northwest"))

# Making dictory for a row
l = {}
l['age'] = age
l['sex'] = sex
l['bmi'] = bmi
l['children'] = children
l['smoker'] = smoker
l['region'] = region

# Converting dic into dataframe
df = pd.DataFrame(l, index=[0])

# Encoding categorical variable
df['region'] = encoder.transform(df['region'])
df['sex'] = df['sex'].map({'male':1, 'female':0})
df['smoker'] = df['smoker'].map({'yes':1, 'no':0})

# Transforming the dataframe
df = transformer.transform(df)

# Generating prediction
y_pred = model.predict(df)

# printing result
if st.button("Show Result"):
    st.header(f"{round(y_pred[0],2)} INR")