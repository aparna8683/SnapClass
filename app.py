import streamlit as st

# Configure the page before importing any screen modules.
# This prevents StreamlitAPIException if a screen later adds top-level UI code.
st.set_page_config(
    page_title="SnapClass",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen


def main():
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
