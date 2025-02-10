import streamlit as st
# import time
from navigation import render_navigation_bar
from footer import render_footer
from helpers import generate_pitch

def load_css():
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Reload the CSS file on change so that the changes are reflected immediately
# def reload_css():
#     time.sleep(0.1)  # Small delay to ensure file changes are detected
#     st.markdown(f'<meta http-equiv="refresh" content="0">', unsafe_allow_html=True)

# Load CSS
load_css()

render_navigation_bar()
st.title("ComUnity Canada - Elevator Pitch")
st.write("Generate a compelling, personalized elevator pitch for career growth.")

# Input fields
st.markdown("### Personal Information")
name = st.text_input("Your Name", placeholder="Enter the name you want to introduce yourself with")

# Required fields with red asterisk *
role = st.text_input("Current Role / Aspiration *", placeholder="E.g., Full-Stack Developer, Aspiring Web Developer")
industry = st.text_input("Industry / Field of Interest *", placeholder="E.g., Tech, FinTech, AI, eCommerce")
work_experience = st.text_area("Work Experience *", placeholder="Summarize your work experience")
strengths = st.text_area("Top Skills & Strengths *", placeholder="E.g., JavaScript, React, problem-solving, teamwork")
career_goals = st.text_area("Career Goals *", placeholder="What are you looking for? (Job, networking, freelance, mentorship, etc.)")
target_audience = st.text_input("Target Audience *", placeholder="E.g., Recruiters, hiring managers, startup founders")

# Achievements (Optional)
achievements = st.text_area("Key Achievements (Optional)", placeholder="Highlight key projects, awards, or notable work")

# Educational Qualification (Mandatory)
education_level = st.selectbox(
    "Educational Qualification *",
    ["High School", "College Diploma", "Bachelor’s Degree", "Master’s Degree", "PhD"]
)

# Duration dropdown
duration_label = st.selectbox("Select Pitch Duration *", ["30 seconds", "1 minute", "2 minutes"])
duration_mapping = {"30 seconds": 30, "1 minute": 60, "2 minutes": 120}
duration = duration_mapping[duration_label]

# Generate button
if st.button("Generate"):
    if name and role and industry and work_experience and strengths and career_goals and target_audience and education_level:
        with st.spinner("Generating your pitch..."):
            pitch = generate_pitch(name, role, industry, work_experience, achievements, strengths, career_goals, target_audience, education_level, duration)

        st.subheader("Here is a striking elevator pitch:")
        st.write(pitch)
    else:
        st.warning("Please fill in all required fields marked with * to generate your pitch.")

# Render footer
render_footer()
