# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:09:02 2024

@author: ACER
"""

import numpy as np
import pickle
import streamlit as st

#loading a model
pickled_model=pickle.load(open('C:/Users/ACER/Desktop/Deployment/diabetes/diabeticCheck.sav','rb'))


# creating a function 

def diabetesPrediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)

    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction=pickled_model.predict(input_data_reshaped)
    if(prediction[0]==1):
        return "The person is diabetic"
    else:
        return "The person is not diabetic"

def main():
    # giving a title 
    
    st.title("Diabetes Prediction webapp")
    
    # getting the input data from user
    
    Pregnancies=st.text_input('Number of pregnancies : ')
    Glucose=st.text_input('Blood Glucode level : ')
    BloodPressure=st.text_input('Blood Pressure value : ')
    SkinThickness=st.text_input('Skin Thickness : ')
    Insulin=st.text_input('Insulin level : ')
    BMI=st.text_input('BMI : ')
    DiabetesPedigreeFunction=st.text_input('Diabetes pedigree function value : ')
    Age=st.text_input('Age of the person : ')
    
    # code for prediction 
    
    diagnosis=''
    
    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis=diabetesPrediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()
    