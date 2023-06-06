import streamlit as st
import json
import crawler
import time

st.title('Trustpilot Summary Generator')
url_input=st.text_input('Enter Trustpilot URL: ')
st.write('Crawling: ', url_input)
crawler.createSumSent(url_input)

# time.sleep(10)
# st.text('Fixed width text')
jsonObject = json.load(open('summary.json'))
st.json(jsonObject)
jsonObject2 = json.load(open('sentiment.json'))
st.json(jsonObject2)

# st.header('Number of Stars')


