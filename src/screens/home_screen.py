import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_background_home, style_base_layout

def home_screen():
    # st.header('Home Screen')
    style_background_home()
    style_base_layout()

    header_home()

    # base_layout()

    

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.header("I'm a Teacher")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZX23dFVoKk6RP9KR5ulVneI1cCnkgQg2MAGP0n9RgVXA1uZF5mq62404&s=10", width=200)
        if st.button("Teacher Portal"):
            st.session_state["login_type"]="teacher"
            st.rerun()
    with col2:
        st.header("I'm a Student")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZX23dFVoKk6RP9KR5ulVneI1cCnkgQg2MAGP0n9RgVXA1uZF5mq62404&s=10", width=200)
        if st.button("Student Portal", type="primary"):
            st.session_state["login_type"]="student"
            st.rerun() 

