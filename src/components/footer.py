import streamlit as st


def footer_home():
    """Small footer shown only on the home screen."""
    st.markdown(
        '<div class="sc-footer">Created with ❤️ by &nbsp;<strong>APNA COLLEGE</strong></div>',
        unsafe_allow_html=True,
    )
