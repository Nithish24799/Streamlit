#!/usr/bin/env python
# coding: utf-8

# In[24]:


import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter("ignore")


# In[25]:


X=joblib.load("x.sav")
model=joblib.load("model.sav")


# In[26]:


def price_predict(location,sqft,bath,BHK):
    loc_index=np.where(X.columns==location)[0][0]
    x=np.zeros(len(X.columns))
    x[0]=sqft
    x[1]=bath
    x[2]=BHK
    if loc_index >=0:
        x[loc_index]=1
    return round((model.predict([x])[0]*100000),0)


# In[12]:


st.title("Bangalore house price prediction")
BHK=st.text_input("Please select size(BHK) 1,2,3,4,5")
sqft=st.text_input("Please select sqftf from 1000 - 5000")
bath=st.text_input("Please select bath 1,2,3,4,5,")
location=st.text_input("Please choose area if not specify known please fill 'other'")
if st.button("Calcuate"):
    try:
        st.success(price_predict(location,sqft,bath,BHK))
    except:
        st.error("Location is not found Try again")

