import streamlit as st

name=st.text_input("Enter Name: ")
fname=st.text_input("Enter Your Father's Name: ")
adr=st.text_area("Enter your text: ")
classdata=st.selectbox("Enter your class:",(1,2,3,4,5,6,7,8,9,10))
button=st.button("Done")
if button:
    st.markdown(f"""
    Name: {name}\n
    Father's Name: {fname}\n
    address= {adr}\n
    class: {classdata}
                """)