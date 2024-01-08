import streamlit as st
st.set_page_config(page_title="Bikes")
st.header("JAWA vs RE")
col1,col2,col3,col4=st.columns(4)
with col1:
  st.subheader("JAWA PERAK")
  st.image("Jawa.jpeg",caption="JAWA PERAK",width=300)
  st.write("Jawa image")
with col2:
  st.subheader("Royal Enfiled")
  st.image("RoyalEnfiled.jpeg",caption="ROYAL ENFILED 350",width=300)
  st.write("RE image")
with col3:
  st.subheader("JAWA PERAK")
  st.image("Jawa.jpeg",caption="JAWA PERAK",width=300)
  st.write("Jawa image")
with col4:
  st.subheader("Royal Enfiled")
  st.image("RoyalEnfiled.jpeg",caption="ROYAL ENFILED 350",width=300)
  st.write("RE image")
