import asyncio
import os
from openai import AsyncOpenAI
import streamlit as st


# Load environment variables
# load_dotenv()

# Fetch API key
# api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
# api_key = st.secrets["OPENAI_API_KEY"]

sample_pitches = {
    "general_professional": """Hi, my name is {name}, and I'm a {role} with expertise in {industry}. 
    I help {target_audience} achieve {key_benefit} by {unique_value_proposition}. 
    Recently, I {notable_achievement}, which has allowed me to {impact}. 
    I'm currently looking to {goal}, and I'd love to connect with like-minded professionals 
    who share an interest in {relevant_topic}. Would you be open to discussing how we can collaborate?""",

    "job_seeker": """Hi, I'm {name}, a {profession} with {years_experience} years of experience in {industry}. 
    My background includes working with {companies_projects}, where I {key_accomplishment}. 
    I specialize in {key_skills} and have a passion for {field}. 
    Right now, I'm exploring opportunities where I can leverage my skills to {value_proposition}. 
    If you know of any opportunities in this space, I'd love to connect!""",

    "entrepreneur": """Hi, I'm {name}, the founder of {startup_name}, where we help {target_audience} solve {pain_point} 
    through {unique_solution}. Unlike {competitor}, our approach {differentiator}. 
    We've already {milestone}, and we're looking for {looking_for} to scale our impact. 
    Let's connect if this aligns with your interests!""",

    "networking_event": """Hi, I'm {name}, a {profession} specializing in {expertise}. 
    I love helping {target_audience} achieve {benefit} by {approach}. 
    Right now, I'm focused on {current_project}, and I'm looking to connect with others who are passionate about {industry_topic}. 
    Let's chat and see how we can collaborate!"""
}


async def generate_pitch_async(name, role, industry, work_experience, achievements, strengths, short_career_goals, long_career_goals, target_audience, education_level, duration):
    prompt = (
        f"Assume the role of a professional career coach and public speaking extraordinaire. "
        f"I am providing you with a list of sample pitches and you should analyze them and create a new pitch that is better than the ones provided using the information provided by th user. "
        f"The sample pitches are as follows: {sample_pitches}"
        f"Your task is to create a concise, engaging, striking and professional elevator pitch lasting approximately {duration} seconds for:\n"
        f"Name: {name}\n"
        f"Role: {role}\n"
        f"Industry: {industry}\n"
        f"Work Experience: {work_experience}\n"
        f"Achievements: {achievements}\n"
        f"Strengths: {strengths}\n"
        f"Short Term Career Goals: {short_career_goals}\n"
        f"Long Term Career Goals: {long_career_goals}\n"
        f"Target Audience: {target_audience}\n"
        f"Education Level: {education_level}\n\n"
        "Pitch:"
    )
    
    try:
        # Initialize OpenAI Async Client (uses API key from environment variables)
        client = AsyncOpenAI()

        # Make async API request
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error generating pitch: {str(e)}"

def generate_pitch(name, role, industry, work_experience, achievements, strengths, short_career_goals, long_career_goals, target_audience, education_level, duration):
    """Wrapper to run the async function synchronously for compatibility with non-async environments."""
    return asyncio.run(generate_pitch_async(name, role, industry, work_experience, achievements, strengths, short_career_goals, long_career_goals, target_audience, education_level, duration))
