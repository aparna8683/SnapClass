import streamlit as st

from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_background_home


def home_screen():
    style_background_home()
    header_home()

    student_col, teacher_col = st.columns(2, gap="medium")

    with student_col:
        with st.container(border=True):
            st.markdown(
                """
                <div class="sc-card-title">I'm<br>Student</div>
                <div class="sc-card-art">🧑‍🎓</div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Student Portal  ↗", key="student_portal", use_container_width=True):
                st.session_state["login_type"] = "student"
                st.rerun()

    with teacher_col:
        with st.container(border=True):
            st.markdown(
                """
                <div class="sc-card-title">I'm<br>Teacher</div>
                <div class="sc-card-art">👩‍🏫</div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Teacher Portal  ↗", key="teacher_portal", use_container_width=True):
                st.session_state["login_type"] = "teacher"
                st.rerun()

    footer_home()
