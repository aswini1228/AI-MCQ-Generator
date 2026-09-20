import streamlit as st
import os
from groq import Groq

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Quizora AI",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# Custom Header
# -----------------------------
st.title("🧠 Quizora AI")
st.subheader("AI-Powered MCQ Generator")
st.write(
    "Generate multiple-choice questions instantly "
    "from any topic using Artificial Intelligence."
)

st.divider()

# -----------------------------
# Get API Key
# -----------------------------
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY is not configured.")
    st.info("Add your Groq API key in Streamlit Secrets.")
    st.stop()

client = Groq(api_key=api_key)

# -----------------------------
# User Inputs
# -----------------------------
topic = st.text_input(
    "📚 Enter Topic",
    placeholder="Example: Python OOP"
)

col1, col2 = st.columns(2)

with col1:
    num_questions = st.selectbox(
        "🔢 Number of Questions",
        [5, 10, 15, 20]
    )

with col2:
    difficulty = st.selectbox(
        "🎯 Difficulty",
        ["Easy", "Medium", "Hard"]
    )

question_type = st.selectbox(
    "❓ Question Type",
    [
        "Concept Based",
        "Application Based",
        "Scenario Based",
        "Mixed"
    ]
)

st.divider()

# -----------------------------
# Generate MCQs
# -----------------------------
if st.button("🚀 Generate MCQs", use_container_width=True):

    if not topic.strip():
        st.warning("Please enter a topic first.")
        st.stop()

    prompt = f"""
You are an expert educational MCQ generator.

Generate {num_questions} high-quality multiple-choice questions
on the topic: {topic}

Difficulty level: {difficulty}
Question type: {question_type}

For every question provide:

Question:
A)
B)
C)
D)

Correct Answer:
Explanation:

Rules:
- Each question must have exactly four options.
- Only one option must be correct.
- Do not repeat questions.
- Make the questions educational and accurate.
- The correct answer should not always be the same option.
- Keep explanations short and clear.
"""

    try:

        with st.spinner("🤖 AI is generating your MCQs..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a professional teacher and "
                            "MCQ question generator."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7
            )

        result = response.choices[0].message.content

        st.success("MCQs generated successfully! 🎉")

        st.divider()

        st.subheader("📝 Generated Questions")

        st.markdown(result)

    except Exception as e:

        st.error("Something went wrong while generating the questions.")

        st.write("Error:", e)

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption("Quizora AI • AI-Powered Learning Assistant")
