import streamlit as st


def style_background_home():
    """Apply the shared SnapClass visual system."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

        :root {
            --sc-ink: #17233d;
            --sc-muted: #64748b;
            --sc-primary: #5b5ce2;
            --sc-primary-dark: #4546c8;
            --sc-lilac: #eeedff;
            --sc-line: #e8eaf3;
            --sc-surface: #ffffff;
        }

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at 8% 8%, rgba(188, 185, 255, .34), transparent 28rem),
                radial-gradient(circle at 92% 22%, rgba(216, 230, 255, .55), transparent 25rem),
                #f7f8fc;
            color: var(--sc-ink);
        }

        #MainMenu, footer, header { visibility: hidden; }
        .block-container {
            max-width: 1120px;
            padding-top: 2rem !important;
            padding-bottom: 3rem !important;
        }

        h1, h2, h3 {
            font-family: 'Manrope', sans-serif !important;
            color: var(--sc-ink);
            letter-spacing: -0.04em;
        }
        h1 { font-size: clamp(2.35rem, 5vw, 3.7rem) !important; line-height: 1.08 !important; }
        h2 { font-size: 1.8rem !important; }
        h3 { font-size: 1.25rem !important; letter-spacing: -0.02em; }
        p, label, li { color: var(--sc-muted); }

        [data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--sc-surface);
            border: 1px solid var(--sc-line);
            border-radius: 22px;
            box-shadow: 0 12px 34px rgba(32, 42, 78, .055);
        }

        div.stButton > button {
            border-radius: 12px;
            min-height: 2.8rem;
            padding: .55rem 1.15rem;
            font-weight: 700;
            border: 1px solid #dedff5;
            transition: transform .18s ease, box-shadow .18s ease, background .18s ease;
        }
        div.stButton > button[kind="primary"] {
            color: white;
            background: var(--sc-primary);
            border-color: var(--sc-primary);
        }
        div.stButton > button[kind="primary"]:hover {
            background: var(--sc-primary-dark);
            border-color: var(--sc-primary-dark);
            box-shadow: 0 8px 18px rgba(91, 92, 226, .2);
            transform: translateY(-1px);
        }
        div.stButton > button:hover { transform: translateY(-1px); }

        [data-testid="stMetric"] {
            background: #fff;
            border: 1px solid var(--sc-line);
            padding: 1rem 1.1rem;
            border-radius: 16px;
        }
        [data-testid="stMetricValue"] {
            color: var(--sc-ink);
            font-family: 'Manrope', sans-serif;
            font-weight: 800;
        }
        .sc-eyebrow {
            color: var(--sc-primary);
            font-size: .76rem;
            text-transform: uppercase;
            letter-spacing: .14em;
            font-weight: 800;
            margin-bottom: .65rem;
        }
        .sc-muted { color: var(--sc-muted); }
        .sc-pill {
            display: inline-block;
            background: var(--sc-lilac);
            color: var(--sc-primary-dark);
            border-radius: 999px;
            padding: .38rem .8rem;
            font-size: .78rem;
            font-weight: 700;
        }
        .sc-feature {
            background: white;
            border: 1px solid var(--sc-line);
            border-radius: 18px;
            padding: 1.15rem;
            min-height: 135px;
        }
        .sc-feature-icon { font-size: 1.5rem; margin-bottom: .55rem; }
        .sc-feature-title { color: var(--sc-ink); font-weight: 800; margin-bottom: .25rem; }
        .sc-feature-copy { color: var(--sc-muted); font-size: .9rem; line-height: 1.5; }
        .sc-footer {
            text-align: center;
            color: #8b94a9;
            font-size: .82rem;
            padding-top: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    """Keep dashboard pages visually consistent with the landing page."""
    style_background_home()


def style_base_layout():
    """Backward-compatible alias used by existing screens."""
    style_background_home()
