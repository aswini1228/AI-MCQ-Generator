# Quizora AI

## AI-Powered MCQ Generator

Quizora AI is an AI-powered application that generates customized Multiple Choice Questions based on the selected topic, difficulty level, number of questions, and question type.

##  Live App

[Try Quizora AI](https://ai-app-generator.streamlit.app/)

##  Features

- AI-generated MCQs
- Custom topic selection
- Easy, Medium, and Hard difficulty levels
- Concept Based questions
- Application Based questions
- Scenario Based questions
- Mixed question generation
- Four options with correct answers
- Short explanations
- Simple and user-friendly interface

##  Workflow

```text
User Input
    ↓
Topic + Number of Questions
    ↓
Difficulty + Question Type
    ↓
Prompt Generation
    ↓
Groq API + AI Model
    ↓
MCQ Generation
    ↓
Questions + Options
    ↓
Correct Answers + Explanations
    ↓
Display Results

Tech Stack
Python
Streamlit
Groq API
Large Language Model (LLM)
Project Structure
AI-App-Generator/
│
├── app.py
├── requirements.txt
└── README.md
 Security

The Groq API key is securely stored using Streamlit Secrets and is not exposed in the source code.

Future Enhancements
Interactive quiz mode
Automatic score calculation
Quiz timer
PDF-based MCQ generation
Document-based question generation
Performance analysis
Topic-wise weak-area detection
Quiz history
Personalized quizzes
Download quizzes as PDF
Leaderboard functionality
Adaptive question difficulty
 Links

Live App:
https://ai-app-generator.streamlit.app/

GitHub Repository:
https://github.com/aswini1228/AI-App-Generator

Author

Aswini.S

B.Sc. Computer Science with Artificial Intelligence
