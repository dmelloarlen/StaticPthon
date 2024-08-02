import pandas as pd
import streamlit as sl
import exception2 as e

def cleaning(ch):
    df=pd.read_csv("country_wise_latest.csv")
    try:
        if ch==1:
            print(df.isna().sum())
        elif ch==2:
            print(df.duplicated().sum())
        else:
            raise(e.DataCleaningError("Invalid choice for data cleaning!!"))
        return df
    except e.DataCleaningError as err:
        print(err)
