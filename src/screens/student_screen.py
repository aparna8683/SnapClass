import streamlit as st

from src.ui.base_layout import style_background_dashboard


def student_screen():
    style_background_dashboard()

    top_left, top_right = st.columns([5, 1])
    with top_left:
        st.markdown('<div class="sc-eyebrow">Your learning space</div>', unsafe_allow_html=True)
        st.title("Student dashboard")
        st.caption("Welcome to your SnapClass learning space.")
    with top_right:
        if st.button("← Home", use_container_width=True):
            st.session_state["login_type"] = None
            st.rerun()

    st.divider()
    st.markdown("### Your classroom at a glance")
    metrics = st.columns(3)
    metrics[0].metric("My classes", "—", help="Connect your class data to display this value.")
    metrics[1].metric("Pending work", "—", help="Connect assignments to display this value.")
    metrics[2].metric("Learning progress", "—", help="Connect progress tracking to display this value.")

    st.markdown("### Quick access")
    left, right = st.columns(2, gap="large")
    with left:
        with st.container(border=True):
            st.markdown("#### 📖 Learning resources")
            st.write("Your class materials and learning resources will appear here.")
            st.button("View resources", disabled=True, use_container_width=True)
    with right:
        with st.container(border=True):
            st.markdown("#### ✅ Assignments")
            st.write("Keep track of upcoming and completed classwork here.")
            st.button("View assignments", disabled=True, use_container_width=True)

    st.caption("Dashboard preview · Connect your backend to display live student data.")
