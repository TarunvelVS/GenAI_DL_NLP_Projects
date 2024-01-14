from dotenv import load_dotenv

load_dotenv() ## loading all our environment variables

import streamlit as st
import os
import sqlite3
import streamlit.components.v1 as components

import google.generativeai as genai

## Configuration - API Key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#Load Gemini Model
# Response --> SQL Query
def get_gemini_response(qs,prompt):
    gemini_model = genai.GenerativeModel('gemini-pro')
    response = gemini_model.generate_content([prompt[0],qs])
    return response.text

##SQL Query from Model ---> To the DB
def sql_query(sql,db):
    print(sql)
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

prompt = [
    """
Your task is to convert plain English questions into SQL queries. This involves understanding the user's intent and translating it into a structured query that can be executed against a database. Focus on key elements like SELECT, FROM, WHERE, JOIN, ORDER BY, and GROUP BY, based on the requirements of the question.
English Question: "What are the names and prices of all products that cost more than $100?"

SQL Query:SELECT Name, Price FROM Products WHERE Price > 100;

English Question: "Can you list all users who joined after January 1, 2023, along with their emails?"

SQL Query:SELECT Username, Email FROM Users WHERE CreatedAt > '2023-01-01';

English Question: "Show me the total number of orders placed by each user."

SQL Query: SELECT UserID, COUNT(OrderID) as TotalOrders FROM Orders GROUP BY UserID;

English Question: "I need to know the average price of all products in our inventory."

SELECT AVG(Price) as AveragePrice FROM Products;

English Question: "List the top 5 most expensive products we have."

SQL Query:SELECT Name, Price FROM Products ORDER BY Price DESC LIMIT 5;

just a plain SQL query without any markdown formatting. 
    """
]


st.set_page_config(page_title="Retrieve data from Database without using SQL")
st.header("GenAI model to retrieve SQL Data")

st.markdown('''
    ## Welcome to Our Data Retrieval Model
    Enter your queries in **plain English** and get instant results!
    ''')

qs = st.text_input("Input: ", key="input")
submit = st.button("submit")

if submit:
    try:
        result = get_gemini_response(qs, prompt)
        response = sql_query(result,"sample.db")
        st.subheader("Output is")
        for row in response:
            print(row)
            st.header(row)
    except Exception as e:
         st.error(f"Error: {e}")

