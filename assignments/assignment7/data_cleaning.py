import pandas as pd
import streamlit as sl

def cleaning():
    df=pd.read_csv("country_wise_latest.csv")
    sl.title("Cleaning")
    sl.write(df.isna().sum())
    sl.write(df.duplicated().sum())
    return df
