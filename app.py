import streamlit as st

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

if st.button("Generate MCQs"):

    if topic == "":
        st.warning("Please enter a topic.")
    else:
        st.success("Your MCQs will be generated here!")
