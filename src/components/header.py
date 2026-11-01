import streamlit as st

def header_home():
    logo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZX23dFVoKk6RP9KR5ulVneI1cCnkgQg2MAGP0n9RgVXA1uZF5mq62404&s=10"

    st.markdown(f"""
    <div>
    <img src="{logo_url}" alt="Logo" style="width: 100px; height: 100px; margin-bottom: 10px;">

    </div>


     



    """, unsafe_allow_html=True)