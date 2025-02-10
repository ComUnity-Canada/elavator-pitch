import streamlit as st

def render_navigation_bar():
    st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: center;'>
            <img src='static/logo.png' width='100' height='100' style='margin-right: 10px;'>
            <h1>ComUnity</h1>
        </div>
        <hr>
        """,
        unsafe_allow_html=True
    )
