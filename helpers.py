import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch API key
api_key = os.getenv("OPENAI_API_KEY")

# Debugging: TO ensure API key is loaded
if not api_key:
    raise ValueError("Error: OPENAI_API_KEY is not set. Check your .env file.")

async def generate_pitch_async(name, role, industry, work_experience, achievements, strengths, career_goals, target_audience, education_level, duration):
    """Generates an elevator pitch asynchronously using OpenAI's API."""
    prompt = (
        f"Assume the role of a professional career coach and public speaking extraordinaire. "
        f"Your task is to create a concise, engaging, striking and professional elevator pitch lasting approximately {duration} seconds for:\n"
        f"Name: {name}\n"
        f"Role: {role}\n"
        f"Industry: {industry}\n"
        f"Work Experience: {work_experience}\n"
        f"Achievements: {achievements}\n"
        f"Strengths: {strengths}\n"
        f"Career Goals: {career_goals}\n"
        f"Target Audience: {target_audience}\n"
        f"Education Level: {education_level}\n\n"
        "Pitch:"
    )
    
    try:
        # Initialize OpenAI Async Client
        client = AsyncOpenAI(api_key=api_key)

        # Make async API request
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error generating pitch: {str(e)}"

def generate_pitch(name, role, industry, work_experience, achievements, strengths, career_goals, target_audience, education_level, duration):
    """Wrapper to run the async function synchronously for compatibility with non-async environments."""
    return asyncio.run(generate_pitch_async(name, role, industry, work_experience, achievements, strengths, career_goals, target_audience, education_level, duration))
