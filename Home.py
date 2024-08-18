import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(r"D:\Udemy\Python Mega Course Learn Python in 60 Days, Build 20 Apps\App2-portfolio\images\Photo.jpg")

with col2:
    st.title("Phan Hoang")
    content = """
    Xin chao moi nguoi toi la Hoang
    """
    st.info(content)

content2 = """
Contact me
"""
st.write(content2)

col3,empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv',sep=";")

with col3:
    # Display the first 10 rows
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(r"D:\Udemy\Python Mega Course Learn Python in 60 Days, Build 20 Apps\App2-portfolio\images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    # Display rows from index 10 onwards
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(r"D:\Udemy\Python Mega Course Learn Python in 60 Days, Build 20 Apps\App2-portfolio\images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")



