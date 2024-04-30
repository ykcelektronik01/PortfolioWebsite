import streamlit as st
import pandas

st.set_page_config(layout="wide")

contentHeader="the best company"
contentSubheader="our team"


st.title(contentHeader.title())
st.header(contentSubheader.title())


col1,space1,col2,space2,col3=st.columns([1,0.25,1,0.25,1])


contentData=pandas.read_csv("CompanyWebsiteDatas/Datas/data.csv", sep=",")

with col1:
    for index,row in contentData[0:4].iterrows():
        st.subheader(str(row["first name"]).title()+" "+str(row["last name"]).title())
        st.text("\n")
        st.text(row["role"])
        st.text("\n")
        st.image("CompanyWebsiteDatas/images/"+row["image"])
        st.text("\n")
        st.text("\n")

with col2:
    for index,row in contentData[4:8].iterrows():
        st.subheader(str(row["first name"]).title()+" "+str(row["last name"]).title())
        st.text("\n")
        st.text(row["role"])
        st.text("\n")
        st.image("CompanyWebsiteDatas/images/"+row["image"])
        st.text("\n")
        st.text("\n")
with col3:
    for index,row in contentData[8:].iterrows():
        st.subheader(str(row["first name"]).title()+" "+str(row["last name"]).title())
        st.text("\n")
        st.text(row["role"])
        st.text("\n")
        st.image("CompanyWebsiteDatas/images/"+row["image"])
        st.text("\n")
        st.text("\n")