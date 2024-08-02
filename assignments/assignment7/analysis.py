import streamlit as sl
import file_handling as fh
import exceptions as e

sl.subheader("clean_covid_data.csv files")
df=fh.load_from_csv()
df.sort_values(df.columns[1],axis=0,ascending=True,inplace=True)
sl.title("Analysis")
try:
    sl.subheader(f"{df["Confirmed"].sum()} confirmed cases")
    sl.subheader(f"{df["Deaths"].sum()} deaths")
    sl.subheader(f"{df["Recovered"].sum()} recovered")
    sl.subheader(f"{df["New cases"].sum()} dalye new cases")
except e.DataCleaningError("Type error!!") as e:
    sl.write(e)

sl.subheader("Countory with most casses")
sl.write(df.tail(1))
sl.subheader("Countory with least casses")
sl.write(df.head(1))
