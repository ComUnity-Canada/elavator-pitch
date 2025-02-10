import streamlit as st
from datetime import datetime

def render_footer():
    st.markdown(
        f"""
        <hr>
        <div style='text-align: center;'>
            <img src='static/logo.png' alt='Company Logo' width='100' height='100'>
            <p>
                <a href='/about'>About Us</a> |
                <a href='/contact'>Contact Us</a> |
                <a href='/services'>What We Do</a>
            </p>
            <p>&copy; {datetime.now().year} ComUnity Canada. All rights reserved.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
