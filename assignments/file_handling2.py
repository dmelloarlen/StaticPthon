import pandas as pd
import streamlit as sl
import data_cleaning2 as dc

df=dc.cleaning(1)
def save_to_csv():
    try:
        df.to_csv("clean_covid_data.csv",index=False)
        sl.write("File saved sucessfully!!")
    except FileNotFoundError as e:
        sl.write(e)

def load_from_csv():
    try:
        df=pd.read_csv("clean_covid_data.csv")
        sl.write(df)
        return df
    except FileNotFoundError as e:
        sl.write(e)