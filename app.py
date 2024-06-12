from dotenv import load_dotenv
load_dotenv() ##load all the environment variables from .env file

import os
import streamlit as st
import sqlite3

import google.generativeai as genai

##Configure our api key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Function to load google gemin model and provide query as response

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

## Function to retrive query from the sql database

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

##Prompt
prompt =[  """
   You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
"""
]

st.set_page_config(page_title="SQL Query Converter")
st.header("SQL Query Converter")

question = st.text_input("Enter your question",key='input')

submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response,"student.db")
    st.subheader("The response is")
    for row in data:
        print(row)
        st.header(row)   