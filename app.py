import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen


def main():
    st.set_page_config(
        page_title="SnapClass | Smart Classroom",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    login_type = st.session_state.get("login_type")

    if login_type == "teacher":
        teacher_screen()
    elif login_type == "student":
        student_screen()
    else:
        st.session_state["login_type"] = None
        home_screen()


if __name__ == "__main__":
    main()
