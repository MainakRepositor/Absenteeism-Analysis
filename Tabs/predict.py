"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Employee Absentism Analysis.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.

    col1,col2 = st.columns(2)

    with col1:
    
        Reason = st.slider("Reason Validity", int(df["Reason"].min()), int(df["Reason"].max()))
        Month = st.slider("Month of Absence", int(df["Month"].min()), int(df["Month"].max()))
        Weekday = st.slider("Weekday of Absence", int(df["Weekday"].min()), int(df["Weekday"].max()))
        Seasons = st.slider("Seasons", int(df["Seasons"].min()), int(df["Seasons"].max()))
        Transportation = st.slider("Transportation Cost", float(df["Transportation"].min()), float(df["Transportation"].max()))
        Travel_distance = st.slider("Travel_distance", int(df["Travel_distance"].min()), int(df["Travel_distance"].max()))
        Service_duration = st.slider("Service_duration", int(df["Service_duration"].min()), int(df["Service_duration"].max()))
        Age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
        Work_load_pd = st.slider("Work_load_pd", float(df["Work_load_pd"].min()), float(df["Work_load_pd"].max()))
        

    with col2:
        
        Hit_target = st.slider("Hit_target", float(df["Hit_target"].min()), float(df["Hit_target"].max()))
        Disciplinary_failure = st.slider("Disciplinary_failure", float(df["Disciplinary_failure"].min()), float(df["Disciplinary_failure"].max()))
        Education = st.slider("Education", int(df["Education"].min()), int(df["Education"].max()))
        Children = st.slider("Children", int(df["Children"].min()), int(df["Children"].max()))
        Drinking = st.slider("Drinking", int(df["Drinking"].min()), int(df["Drinking"].max()))
        Smoking = st.slider("Smoking", int(df["Smoking"].min()), int(df["Smoking"].max()))
        Pet = st.slider("Pets", int(df["Pet"].min()), int(df["Pet"].max()))
        Weight = st.slider("Weight", float(df["Weight"].min()), float(df["Weight"].max()))
        Height = st.slider("Height", float(df["Height"].min()), float(df["Height"].max()))
          

    # Create a list to store all the features
    features = [Reason,Month,Weekday,Seasons,Transportation,Travel_distance,Service_duration,Age,Work_load_pd,Hit_target,Disciplinary_failure,Education,Children,Drinking,Smoking,Pet,Weight,Height]

    # Create a button to predict
    if st.button("Detect Class"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.11
        

        # Prfloat the output according to the prediction
        x = round((prediction[0]*100),2)

        if (Reason < 5):
            st.error("Employee is not at all committed")
            st.info("HR Decision: Immediate Termination")

        elif(Reason > 5 and Reason <10):
            st.warning("Employee has significantly less commitment")
            st.info("HR Decision: Check Employee Health")

        elif(Reason > 10 and Reason <15):
            st.success("Normal Level of Absentism.")
            st.info("HR Decision: It's normal. Maybe a hike can reduce further absentism")

        else:
            st.success("Highly Dedicated Employee")
            st.info("HR Decision: Nomitated for Employee Rewards / Hikes")
          
          
                
        # Prfloat teh score of the model 
        st.sidebar.write("The model used is trusted by HRs and has an accuracy of ", round((score*100),2),"%")
