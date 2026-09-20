import streamlit as st
import os
from groq import Groq

st.set_page_config(
    page_title="Quizora AI",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Quizora AI")
st.write("Generate AI-powered MCQs from any topic.")

# API Key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.warning("GROQ_API_KEY is not configured.")
    st.stop()

client = Groq(api_key=api_key)

# User inputs
topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Python OOP"
)

num_questions = st.selectbox(
    "Number of Questions",
    [5, 10, 15, 20]
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

question_type = st.selectbox(
    "Question Type",
    ["Concept Based", "Application Based", "Mixed"]
)

if st.button("Generate MCQs"):

    if not topic:
        st.error("Please enter a topic.")
        st.stop()

    prompt = f"""
Generate {num_questions} multiple-choice questions about {topic}.

Difficulty: {difficulty}
Question Type: {question_type}

For every question provide:
1. Question
2. Four options: A, B, C, D
3. Correct answer
4. Short explanation

Make sure the questions are accurate and do not repeat.
"""

    with st.spinner("Generating questions..."):

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )

    result = response.choices[0].message.content

    st.subheader("Generated MCQs")
    st.write(result)
