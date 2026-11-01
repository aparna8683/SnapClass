import streamlit as st

from src.components.footer import footer_home


def _teacher_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background: #e3e3ff !important;
            font-family: 'Outfit', sans-serif;
        }
        .block-container {
            max-width: 850px !important;
            padding: 1.4rem 1.5rem 1rem !important;
        }
        .teacher-topbar {
            display:flex;
            align-items:center;
            justify-content:space-between;
            gap:1rem;
            margin: .2rem 0 1.15rem;
        }
        .teacher-brand {
            display:flex;
            align-items:center;
            gap:.55rem;
        }
        .teacher-brand-mark {
            width:58px;height:58px;flex:0 0 58px;
            display:flex;align-items:center;justify-content:center;
            background:#ffeb00;border:2px solid #37376f;border-radius:15px;
            font-size:2rem;line-height:1;
        }
        .teacher-brand-name {
            color:#5865f2;font-weight:1000;font-size:1.55rem;
            line-height:.78;letter-spacing:-1.5px;
            text-shadow:0 1px 0 rgba(255,255,255,.4);
        }
        .teacher-page-title {
            color:#050505;font-size:clamp(1.55rem,3.4vw,2.2rem);
            line-height:1.05;font-weight:1000;letter-spacing:-1.2px;
            margin: .4rem 0 2.7rem;
        }
        .teacher-form-label {
            color:#34344c;font-size:.83rem;font-weight:600;
            margin:.95rem 0 .35rem;
        }
        div[data-testid="stTextInput"] label {display:none;}
        div[data-testid="stTextInput"] input {
            height:2.65rem;background:#f4f5fa;border:1px solid #eef0f8;
            border-radius:8px;color:#34344c;padding:0 .85rem;
        }
        div[data-testid="stTextInput"] input:focus {
            border-color:#5865f2;box-shadow:0 0 0 1px #5865f2;
        }
        div.stButton > button {
            border:0;border-radius:999px;min-height:2.65rem;
            font-weight:700;font-size:.85rem;
            transition:filter .15s ease,transform .15s ease;
        }
        div.stButton > button:hover {filter:brightness(.96);transform:translateY(-1px);}
        div.stButton > button[kind="primary"] {
            background:#5865f2;color:white;
        }
        .teacher-divider {
            border:0;border-top:1px solid #cfd0ed;margin:1.6rem 0 1.15rem;
        }
        .teacher-footer {
            color:#101020;text-align:center;font-size:.75rem;
            font-weight:700;margin-top:2.6rem;padding-bottom:.4rem;
        }
        @media(max-width:600px) {
            .block-container {padding:1rem .9rem !important;}
            .teacher-brand-mark {width:48px;height:48px;flex-basis:48px;}
            .teacher-brand-name {font-size:1.25rem;}
            .teacher-page-title {margin-bottom:1.8rem;}
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _password_field(label, key, placeholder, visible_key):
    st.markdown(f'<div class="teacher-form-label">{label}</div>', unsafe_allow_html=True)
    field_col, eye_col = st.columns([12, 1.25], gap="small", vertical_alignment="bottom")
    with field_col:
        st.text_input(
            label,
            placeholder=placeholder,
            type="default" if st.session_state.get(visible_key, False) else "password",
            key=key,
            label_visibility="collapsed",
        )
    with eye_col:
        if st.button("◉", key=f"{visible_key}_button", use_container_width=True):
            st.session_state[visible_key] = not st.session_state.get(visible_key, False)
            st.rerun()


def teacher_screen():
    _teacher_styles()

    if "teacher_auth_mode" not in st.session_state:
        st.session_state["teacher_auth_mode"] = "register"

    top_left, top_right = st.columns([1.35, 1], vertical_alignment="center")
    with top_left:
        st.markdown(
            """
            <div class="teacher-brand">
                <div class="teacher-brand-mark">♟</div>
                <div class="teacher-brand-name">SNAP<br>CLASS</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with top_right:
        if st.button("Go back to Home  ⌘ · Backspace", key="teacher_home", use_container_width=True):
            st.session_state["login_type"] = None
            st.session_state["teacher_auth_mode"] = "register"
            st.rerun()

    is_register = st.session_state["teacher_auth_mode"] == "register"
    title = "Register your teacher profile" if is_register else "Login to your teacher profile"
    st.markdown(f'<div class="teacher-page-title">{title}</div>', unsafe_allow_html=True)

    st.markdown('<div class="teacher-form-label">Enter username</div>', unsafe_allow_html=True)
    username = st.text_input(
        "Enter username",
        placeholder="@abhishek",
        key="teacher_username",
        label_visibility="collapsed",
    )

    if is_register:
        st.markdown('<div class="teacher-form-label">Enter name</div>', unsafe_allow_html=True)
        full_name = st.text_input(
            "Enter name",
            placeholder="Abhishek Sharma",
            key="teacher_full_name",
            label_visibility="collapsed",
        )
    else:
        full_name = ""

    _password_field("Enter password", "teacher_password", "Enter your password", "teacher_password_visible")

    if is_register:
        _password_field(
            "Confirm password",
            "teacher_confirm_password",
            "Confirm your password",
            "teacher_confirm_visible",
        )

    st.markdown('<hr class="teacher-divider">', unsafe_allow_html=True)
    primary_col, secondary_col = st.columns(2, gap="small")

    with primary_col:
        primary_label = "♟  Register Now  ⌘ · Enter" if is_register else "♟  Login Now  ⌘ · Enter"
        if st.button(primary_label, key="teacher_submit", type="primary", use_container_width=True):
            password = st.session_state.get("teacher_password", "")
            confirm = st.session_state.get("teacher_confirm_password", "")
            if not username.strip() or not password.strip():
                st.warning("Please enter your username and password.")
            elif is_register and not full_name.strip():
                st.warning("Please enter your name.")
            elif is_register and password != confirm:
                st.error("The passwords do not match.")
            else:
                st.info("The teacher registration/login interface is ready. Connect your authentication backend to create or verify accounts.")

    with secondary_col:
        secondary_label = "♟  Login instead" if is_register else "♟  Register instead"
        if st.button(secondary_label, key="teacher_switch_mode", use_container_width=True):
            st.session_state["teacher_auth_mode"] = "login" if is_register else "register"
            st.rerun()

    footer_home()
