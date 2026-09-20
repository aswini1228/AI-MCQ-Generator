import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Quizora AI",
    page_icon="🧠"
)

st.title("🧠 Quizora AI")
st.write("AI-Powered MCQ Generator")

st.divider()

topic = st.text_input(
    "Enter your topic",
    placeholder="Example: Python"
)

number = st.selectbox(
    "Number of Questions",
    [5, 10, 15, 20]
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

question_type = st.selectbox(
    "Question Type",
    [
        "Concept Based",
        "Application Based",
        "Scenario Based",
        "Mixed"
    ]
)

if st.button("🚀 Generate MCQs"):

    if not topic.strip():
        st.warning("Please enter a topic.")
        st.stop()

    try:
        api_key = st.secrets["GROQ_API_KEY"]

        client = Groq(api_key=api_key)

        prompt = f"""
Generate {number} multiple-choice questions about {topic}.

Difficulty: {difficulty}
Question Type: {question_type}

For each question provide:

Question:
A)
B)
C)
D)

Correct Answer:
Explanation:

Rules:
- Exactly four options.
- Only one correct answer.
- Do not repeat questions.
- Make the questions accurate and educational.
- Give a short explanation.
"""

        with st.spinner("🤖 Generating MCQs..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert MCQ generator."
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

        st.subheader("📝 Generated MCQs")

        st.markdown(result)

    except Exception as e:
        st.error("Unable to generate MCQs.")
        st.write("Error:", e)
