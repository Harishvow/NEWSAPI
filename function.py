import requests
import streamlit as pd


url="https://newsapi.org/v2/top-headlines?country=us&apiKey=cf6719f527a54c2a9956b89f35e53255"
api="cf6719f527a54c2a9956b89f35e53255"
req=requests.get(url)
content=req.json()
pd.set_page_config(layout="wide")
pd.header("Today News ")

col1, col2, col3=pd.columns(3)
with col1:
    for i in content["articles"][0:6]:
        with pd.container(key=i['title'], border=True):
            pd.subheader(i['title'])
            pd.text(i["description"])
            pd.image(i["urlToImage"])
            pd.badge(i["url"])
with col2:
    for i in content["articles"][6:12]:
        with pd.container(key=i['title'], border=True):
            pd.subheader(i['title'])
            pd.text(i["description"])
            pd.image(i["urlToImage"])
            pd.badge(i["url"])
with col3:
    for i in content["articles"][12:18]:
        with pd.container(key=i['title'], border=True):
            pd.subheader(i['title'])
            pd.text(i["description"])
            pd.image(i["urlToImage"])
            pd.badge(i["url"])







