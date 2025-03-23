import streamlit as st
from PIL import Image
import os

def render_navigation_bar():
    st.markdown("<div style='padding-top: 1rem;'></div>", unsafe_allow_html=True)
    
    # Create columns for layout 
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col2:
        # Center align all content
        st.markdown(
            """
            <style>
                div[data-testid="column"] {
                    text-align: center;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        try:
            # Load and display the logo
            logo_path = os.path.join("static", "logo.png")
            if os.path.exists(logo_path):
                logo = Image.open(logo_path)
                st.image(logo, width=50, use_container_width=True)
            else:
                st.error(f"Logo file not found at: {os.path.abspath(logo_path)}")
        except Exception as e:
            st.error(f"Error loading logo: {str(e)}")
    
    # Add some spacing after the navigation
    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
