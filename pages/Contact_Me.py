import streamlit as st
from Send_Email import  send_mail
import  pandas


st.header("Contact Me")

df=pandas.read_csv("CompanyWebsiteDatas/Datas/topics.csv")

with st.form(key="email_form"):
    user_email=st.text_input("Enter your email")

    options = ["Job Inquiries", "Project Proposals", "Other"]

    selected_option = st.selectbox("What topic do you want to discuss?", df["topic"])

    raw_message=st.text_area("Your message")

#bosluklara dikkat edelim .Bosluk koydugumuzda ya da hic karakter olmadan direk olarak degiskeni tanimladigimizda
#Subject gorunmuyor.
    message = f"""\
Subject: New email from {user_email}
Selected option={selected_option} 
From:{user_email}
{raw_message} 
"""

    button = st.form_submit_button("Submit")

    if button:
        send_mail(message)
        st.info("Your email was sent succesfully")

st.markdown(f"[My Linkedin Profile](https://www.linkedin.com/in/yusuf-koray-can-5a19a4231/)")

