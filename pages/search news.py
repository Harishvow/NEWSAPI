import streamlit as pd
import requests
vd=pd.text_input(label="Search News",value="")
url = f'https://newsapi.org/v2/everything?q={vd}&apiKey=cf6719f527a54c2a9956b89f35e53255'
api = "cf6719f527a54c2a9956b89f35e53255"
req = requests.get(url)
content = req.json()
print(content)
try:
    try:
            articles = content["articles"]
            pd.title("Search News")
            col1, col2, col3 = pd.columns(3)
            with col1:
                    for i in articles[0:10]:
                        with pd.container(key=i['title'], border=True):
                            pd.subheader(i["title"])
                            pd.text(i["description"])
                            try:
                                pd.image(i["urlToImage"])
                            except AttributeError:
                                pass
                            pd.badge(i["url"])
            with col2:

                    for i in articles[10:20]:
                        with pd.container(key=i['title'], border=True):
                            pd.subheader(i["title"])
                            pd.text(i["description"])
                            try:
                                pd.image(i["urlToImage"])
                            except AttributeError:
                                pass
                            pd.badge(i["url"])
            with col3:
                for i in articles[20:30]:
                    with pd.container(key=i['title'], border=True):
                        pd.subheader(i["title"])
                        pd.text(i["description"])
                        try:
                            pd.image(i["urlToImage"])
                        except AttributeError:
                            pass
                        pd.badge(i["url"])

    except KeyError:
            pass
except TypeError:
    pass