import streamlit as st


def header_home():
    """Render the compact SnapClass brand header."""
    st.markdown(
        """
        <div style="
            display:flex;
            align-items:center;
            justify-content:space-between;
            gap:1rem;
            padding:.2rem 0 1.35rem 0;
            border-bottom:1px solid #e8eaf3;
            margin-bottom:2.2rem;
        ">
            <div style="display:flex;align-items:center;gap:.7rem;">
                <div style="
                    width:42px;height:42px;border-radius:13px;
                    display:flex;align-items:center;justify-content:center;
                    color:white;background:linear-gradient(135deg,#7778f3,#5051d6);
                    font-size:1.35rem;font-weight:800;
                    box-shadow:0 7px 17px rgba(91,92,226,.22);
                ">S</div>
                <div>
                    <div style="font-size:1.2rem;font-weight:800;letter-spacing:-.04em;color:#17233d;line-height:1.1;">SnapClass</div>
                    <div style="font-size:.72rem;color:#8490a6;letter-spacing:.04em;">SMART CLASSROOM, SIMPLIFIED</div>
                </div>
            </div>
            <span class="sc-pill">Learning, connected</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
