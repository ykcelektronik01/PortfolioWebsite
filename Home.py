import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1,col2=st.columns([1,1.50]) #1'e 2 oranini bize sagiyor.

with col1:
    st.image("Images/photo.jpg",width=500)
    content2 = """Below you can find some of the apps I have built in Phyton. Feel free to contact me!
    """
    st.write(content2)
with col2:
    st.title("Yusuf Koray Can")
    content = """
    I am a final year student studying Electrical and Electronics Engineering at Çukurova University. During my academic journey, I have developed a strong foundation in various aspects of engineering, particularly in the realm of electronics.

Aside from my academic pursuits, I have also delved into the world of game development. Over the course of two years, I dedicated myself to exploring game design principles, honing my skills in programming and graphics, and understanding the intricacies of game mechanics.

Currently, I am expanding my knowledge and expertise by learning Python programming language. Python's versatility and widespread use across various domains intrigue me, and I am enthusiastic about mastering its capabilities.

Combining my engineering background with my passion for programming, I aspire to contribute to innovative projects that blend technology and creativity to make a meaningful impact on society.
    """
    st.info(content)



col3,space,col4=st.columns([1,0.25,1])

df=pandas.read_csv("data.csv",sep=';')
print(df)
with col3:
    for index,row in df[:10].iterrows(): #iterrows dememiz gerekir aksi halde erisemiyoruz hata aliyoruz.
        st.header(row["title"])
        st.text(row["description"])
        st.image("Images/"+row["image"])
        st.markdown(f"[Source Code](https://github.com/ykcelektronik01)")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.text(row["description"])
        st.image("Images/" + row["image"])
        st.markdown(f"[Source Code](https://github.com/ykcelektronik01)")