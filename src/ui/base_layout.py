import streamlit as st


def style_background_home():
    """Styles for the minimal SnapClass home screen."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&display=swap');

        .stApp {
            background: #5865f2;
            font-family: 'Outfit', sans-serif;
        }

        #MainMenu, footer, header { visibility: hidden; }

        .block-container {
            max-width: 900px;
            min-height: 100vh;
            padding: 2.2rem 1.5rem 1.2rem !important;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .sc-home-logo {
            text-align: center;
            margin: 0 auto 1.6rem;
        }

        .sc-logo-mark {
            width: 58px;
            height: 58px;
            margin: 0 auto .8rem;
            border-radius: 15px;
            background: #ffeb00;
            border: 2px solid #30336f;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            box-shadow: 0 3px 0 rgba(25, 28, 85, .15);
        }

        .sc-wordmark {
            color: #fff;
            font-family: 'Outfit', sans-serif;
            font-size: 2.55rem;
            line-height: .82;
            font-weight: 900;
            letter-spacing: -2px;
            text-align: center;
            text-shadow: 0 2px 1px rgba(30, 35, 120, .08);
        }

        .sc-portal-card {
            min-height: 186px;
            background: #e7e6ff;
            border-radius: 42px;
            padding: 1.5rem 1.35rem 1.1rem;
            text-align: left;
            color: #17172b;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .sc-card-title {
            color: #17172b;
            font-size: 1.25rem;
            font-weight: 900;
            line-height: .95;
            letter-spacing: -.7px;
            margin-bottom: .35rem;
        }

        .sc-card-art {
            height: 66px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 3.5rem;
            line-height: 1;
            margin: .1rem 0 .35rem;
        }

        div.stButton > button {
            background: #5865f2 !important;
            color: #fff !important;
            border: 0 !important;
            border-radius: 999px !important;
            min-height: 2.2rem !important;
            padding: .35rem 1.1rem !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
            font-size: .78rem !important;
            box-shadow: none !important;
        }

        div.stButton > button:hover {
            background: #4652df !important;
            transform: translateY(-1px);
        }

        .sc-footer {
            color: #fff;
            text-align: center;
            font-family: 'Outfit', sans-serif;
            font-size: .72rem;
            font-weight: 600;
            margin-top: 1.8rem;
            opacity: .96;
        }

        @media (max-width: 640px) {
            .block-container { padding: 1.5rem 1rem !important; }
            .sc-wordmark { font-size: 2.2rem; }
            .sc-portal-card { min-height: 175px; border-radius: 34px; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    """Dashboard screens are intentionally blank."""
    pass


def style_base_layout():
    style_background_home()
