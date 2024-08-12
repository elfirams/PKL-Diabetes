import numpy as np
import pandas as pd
import re
import pickle
import streamlit as st
import sklearn

@st.cache(ttl=12500, allow_output_mutation=True)
def load_model():
    model = pickle.load(open(r"C:\Users\HP\Documents\PKL\nb_diabetes\nb1_model.pkl", "rb"))
    return model
