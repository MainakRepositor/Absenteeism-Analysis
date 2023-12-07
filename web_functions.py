"""This module contains necessary function needed"""

# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import streamlit as st

def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('absentism.csv')

    # Perform feature and target split
    X = df[["Reason","Month","Weekday","Seasons","Transportation","Travel_distance","Service_duration","Age","Work_load_pd","Hit_target","Disciplinary_failure","Education","Children","Drinking","Smoking","Pet","Weight","Height"]]
    y = df["Absent_time"]

    return df, X, y


@st.cache_data()
def train_model(X, y):
    """This function trains the model and return the model and model score"""
    # Create the model
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    # Fit the data on model
    model.fit(X, y)
    # Get the model score
    score = model.score(X, y)

    # Return the values
    return model, score

def predict(X, y, features):
    # Get model and model score
    model, score = train_model(X, y)
    # Predict the value
    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction, score

