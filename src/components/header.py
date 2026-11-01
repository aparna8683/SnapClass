import streamlit as st


def header_home():
    """Centered SnapClass logo and wordmark."""
    st.markdown(
        """
        <div class="sc-home-logo">
            <div class="sc-logo-mark">🎓</div>
            <div class="sc-wordmark">SNAP<br>CLASS</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
