import streamlit as st
import json
import crawler
import time

st.title('Trustpilot Summary Generator')

col1, col2 = st.columns(2)

url_input=col1.text_input('Enter Trustpilot URL: ')
st.write('Crawling: ', url_input)
crawler.createSumSent(url_input)

url_input2=col2.text_input('Enter Trustpilot URL: ')

# time.sleep(10)
# st.text('Fixed width text')
jsonObject = json.load(open('summary.json'))
col1.json(jsonObject)
jsonObject2 = json.load(open('sentiment.json'))
col1.json(jsonObject2)

# st.header('Number of Stars')


