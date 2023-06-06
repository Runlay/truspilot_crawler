import streamlit as st
import json
import crawler
import time

st.title('Trustpilot Summary Generator')

col1, col2 = st.columns(2)

url_input=col1.text_input('Enter 1st Trustpilot URL: ')
url_input2=col2.text_input('Enter 2nd Trustpilot URL: ')
if url_input:
    st.write('Crawling: ', url_input)

    crawler.createSumSent(url_input)

    # time.sleep(10)
    # st.text('Fixed width text')
    jsonObject = json.load(open('summary.json'))
    col1.json(jsonObject)
    jsonObject2 = json.load(open('sentiment.json'))
    col1.json(jsonObject2)

    # st.header('Number of Stars')

if url_input2:
    st.write('Crawling: ', url_input)

    crawler.createSumSent(url_input)

    # time.sleep(10)
    # st.text('Fixed width text')
    jsonObject = json.load(open('summary.json'))
    col2.json(jsonObject)
    jsonObject2 = json.load(open('sentiment.json'))
    col2.json(jsonObject2)

    # st.header('Number of Stars')


