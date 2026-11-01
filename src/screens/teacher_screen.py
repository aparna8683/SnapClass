import streamlit as st

from src.ui.base_layout import style_background_dashboard


def teacher_screen():
    style_background_dashboard()

    top_left, top_right = st.columns([5, 1])
    with top_left:
        st.markdown('<div class="sc-eyebrow">Teaching workspace</div>', unsafe_allow_html=True)
        st.title("Teacher dashboard")
        st.caption("Your classroom overview, all in one place.")
    with top_right:
        if st.button("← Home", use_container_width=True):
            st.session_state["login_type"] = None
            st.rerun()

    st.divider()
    st.markdown("### Classroom overview")
    metrics = st.columns(3)
    metrics[0].metric("Active classes", "—", help="Connect your class data to display this value.")
    metrics[1].metric("Students", "—", help="Connect your student records to display this value.")
    metrics[2].metric("Assignments", "—", help="Connect assignment data to display this value.")

    st.markdown("### Teaching tools")
    left, right = st.columns(2, gap="large")
    with left:
        with st.container(border=True):
            st.markdown("#### 🏫 Manage classes")
            st.write("Create and organise class spaces for your learners.")
            st.button("Manage classes", disabled=True, use_container_width=True)
    with right:
        with st.container(border=True):
            st.markdown("#### 📝 Assign learning")
            st.write("Prepare and share classwork with your students.")
            st.button("Manage assignments", disabled=True, use_container_width=True)

    st.caption("Dashboard preview · Connect your backend to enable classroom management.")
