import streamlit as st

from src.components.header import header_home
from src.ui.base_layout import style_background_home


def home_screen():
    style_background_home()
    header_home()

    st.markdown(
        """
        <div class="sc-eyebrow">A better classroom experience</div>
        <h1>Every class has a<br>story. Make yours<br><span style="color:#5b5ce2;">count.</span></h1>
        <p style="max-width:590px;font-size:1.08rem;line-height:1.7;margin-top:1rem;">
            One simple space for teachers to manage learning and students to stay
            connected, focused, and ready for what comes next.
        </p>
        <div style="display:flex;gap:.55rem;flex-wrap:wrap;margin:1.25rem 0 2rem;">
            <span class="sc-pill">Organised learning</span>
            <span class="sc-pill">Simple workflows</span>
            <span class="sc-pill">One classroom hub</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Choose your space")
    st.caption("Select the portal that matches your role to continue.")

    teacher_col, student_col = st.columns(2, gap="large")

    with teacher_col:
        with st.container(border=True):
            st.markdown(
                """
                <div style="font-size:2rem;margin-bottom:.7rem;">👩‍🏫</div>
                <div class="sc-eyebrow">For educators</div>
                <h3 style="margin-bottom:.35rem;">Teacher portal</h3>
                <p style="line-height:1.6;min-height:3.2rem;">
                    Organise your classroom, plan learning activities, and keep
                    your students moving forward.
                </p>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Continue as teacher  →", key="teacher_portal", type="primary", use_container_width=True):
                st.session_state["login_type"] = "teacher"
                st.rerun()

    with student_col:
        with st.container(border=True):
            st.markdown(
                """
                <div style="font-size:2rem;margin-bottom:.7rem;">🎒</div>
                <div class="sc-eyebrow">For learners</div>
                <h3 style="margin-bottom:.35rem;">Student portal</h3>
                <p style="line-height:1.6;min-height:3.2rem;">
                    Find your learning space, keep track of classwork, and stay
                    on top of your academic journey.
                </p>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Continue as student  →", key="student_portal", use_container_width=True):
                st.session_state["login_type"] = "student"
                st.rerun()

    st.markdown(
        """
        <div style="margin-top:2.7rem;">
            <div class="sc-eyebrow">Designed around the classroom</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    feature_cols = st.columns(3, gap="medium")
    features = [
        ("📚", "Stay organised", "Keep classroom activity and learning resources in one place."),
        ("🤝", "Work together", "Make it easier for educators and learners to stay connected."),
        ("✨", "Keep it simple", "A clear, focused experience without unnecessary clutter."),
    ]
    for col, (icon, title, copy) in zip(feature_cols, features):
        with col:
            st.markdown(
                f"""
                <div class="sc-feature">
                    <div class="sc-feature-icon">{icon}</div>
                    <div class="sc-feature-title">{title}</div>
                    <div class="sc-feature-copy">{copy}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('<div class="sc-footer">© SnapClass · A smarter space to learn together</div>', unsafe_allow_html=True)
