import streamlit as st
from datetime import datetime
from PIL import Image
import os

def render_footer():
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # CSS for centering
    st.markdown(
        """
        <style>
            div[data-testid="column"] {
                text-align: center;
            }
            div[data-testid="stImage"] {
                display: flex;
                justify-content: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Center align the content
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        # Try to load and display the logo
        try:
            logo_path = os.path.join("static", "logo.png")
            if os.path.exists(logo_path):
                logo = Image.open(logo_path)
                st.image(logo, width=100, use_container_width=True)
        except Exception as e:
            st.error(f"Error loading footer logo: {str(e)}")
        
        # Footer links and copyright
        st.markdown(
            f"""
            <div style='text-align: center;'>
                <p style='margin-top: 1rem;'>
                    <a href='/about' style='color: #3B9B9B; text-decoration: none;'>About Us</a> |
                    <a href='/contact' style='color: #3B9B9B; text-decoration: none;'>Contact Us</a> |
                    <a href='/services' style='color: #3B9B9B; text-decoration: none;'>What We Do</a>
                </p>
                <p style='color: #666666;'>&copy; {datetime.now().year} ComUnity Canada. All rights reserved.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
