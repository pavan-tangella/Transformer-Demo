import streamlit as st
st.get_page_config(page_title="Kings in flim Industry")
st.header("Types of HEROS in Film industry")
col1,col2=st.columns(2)
with col1:
  st.subheader("Prabhas")
  st.image("prabhas.jpg",caption="Prabhas",width=300)
  st.write("Image from SALAAR")
with col2:
  st.subheader("Yesh")
  st.image("Rocky.jpg",caption="YESH",width=300)
  st.write("Image from KGF")
