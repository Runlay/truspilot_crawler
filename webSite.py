import streamlit as st
import json
# st.text('Fixed width text')
# st.markdown('_Markdown_') # see *
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# st.write('Most objects') # df, err, func, keras!
# st.write(['st', 'is <', 3]) # see *
st.title('Summary')
st.header('Data of the software: ')
st.subheader('Publication date: ')
st.subheader('Kind of Software: ')
st.subheader('Number of evaluation:')
st.header('Data of the company: ')
st.subheader('Name of the company:')
st.subheader('Number of employees:')
st.header('Summary')


st.text('Fixed width text')
jsonObject = json.load('summary.json')
st.json(jsonObject)
jsonObject2 = json.load('sentiment.json')
st.json(jsonObject2)
# st.header('Number of Stars')


