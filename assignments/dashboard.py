import pandas as pd
import streamlit as sl
import matplotlib.pyplot as plt
import visualization as v
import file_handling2 as fh

df=fh.load_from_csv() 
def dash(df):
    sl.write("Death range")
    ch=sl.slider("choose death range",df["Deaths"].min(),df["Deaths"].max(),step=1000)
    sl.write("Death range selection",ch)
    sl.bar_chart(df[df["Deaths"]>=ch]["Country/Region"])
    
    ch0=sl.selectbox("Select a country",df["Country/Region"])
    cd=df[df["Country/Region"] == ch0]
    plt.scatter(cd["Confirmed"],cd["Country/Region"])
    sl.pyplot(plt)

    ch1=sl.selectbox("Select a case type",{"Confirmed","Deaths","Recovered"})
    v.plot_total_cases(df,ch1)

    ch2=sl.selectbox("Select a case type",{"Top 10 countries whith highest cases","Daily cases"})
    if ch2=="Top 10 countries whith highest cases":
        v.plot_top_cases(df)
    elif ch2=="Daily cases":
        v.plot_daily_cases(df)

dash(df)
    
