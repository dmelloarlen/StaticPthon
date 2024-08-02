import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as sl

def plot_total_cases(df,ch):
    plt.figure(figsize=(10,35))
    if ch=="Confirmed":
        sl.write("Total confirm cases")
        plt.scatter(df["Confirmed"],df["Country/Region"],alpha=0.5)
        plt.savefig("confirm.png")
        sl.pyplot(plt)
    elif ch=="Deaths":
        sl.write("Total death cases")
        plt.scatter(df["Deaths"],df["Country/Region"],alpha=0.5)
        plt.savefig("deaths.png")
        sl.pyplot(plt)
    else:
        sl.write("Total recovered cases")
        plt.scatter(df["Recovered"],df["Country/Region"],alpha=0.5)
        plt.savefig("recovered.png")
        sl.pyplot(plt)


def plot_top_cases(df):
    plt.figure(figsize=(10,10))
    sl.write("Top 10 countaries with highest cases")
    plt.bar(df.head(10)["Country/Region"],df.head(10)["Confirmed"])
    plt.savefig("plot_top_cases.png")
    sl.pyplot(plt)
    
def plot_daily_cases(df):
    plt.figure(figsize=(10,35))
    sl.write("Top 10 countaries with highest cases")
    plt.scatter(df["New cases"],df["Country/Region"])
    plt.savefig("plot_daily_cases.png")
    sl.pyplot(plt)





