import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.header("The best company")
st.write("My name is")
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('data.csv')

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(r"D:\Udemy\Python Mega Course Learn Python in 60 Days, Build 20 Apps\App2portfolio\Student_project\images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(r"D:\Udemy\Python Mega Course Learn Python in 60 Days, Build 20 Apps\App2portfolio\Student_project\images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(r"D:\Udemy\Python Mega Course Learn Python in 60 Days, Build 20 Apps\App2portfolio\Student_project\images/" + row["image"])