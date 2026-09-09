import streamlit as st

from data_manager import load_questions
from quiz import Quiz
from validation import validate_name


# Configure the browser page before displaying any Streamlit content.
st.set_page_config(
    page_title="UK Generations & Consumer Insight Quiz",
    page_icon="📊",
    layout="centered"
)

# Display the application title and a short explanation for the user.
st.title("UK Generations & Consumer Insight Quiz")
st.write(
    "Test your knowledge of UK generations, demographics "
    "and consumer characteristics."
)

# Load quiz questions from persistent CSV storage.
questions = load_questions("data/questions.csv")

# Stop the application gracefully if the question data cannot be loaded.
if not questions:
    st.error("Quiz questions could not be loaded.")
    st.stop()

# Collect and validate the participant's name before displaying the quiz.
name = st.text_input("Enter your name:")

if name:
    if validate_name(name):
        st.success(f"Welcome, {name}!")

        # Create a Quiz object using the questions loaded from the CSV file.
        quiz = Quiz(questions)

        st.subheader("Quiz")

        # Store each answer using the question's position as the dictionary key.
        answers = {}

        # Display every question and its four possible answers.
        for index, question in enumerate(quiz.questions):
            st.write(
                f"**Question {index + 1}: {question.question_text}**"
            )

            answers[index] = st.radio(
                "Select an answer:",
                question.options,
                key=f"question_{index}",
                index=None
            )

            # Display data provenance so users understand the source and context.
            st.caption(
                f"Category: {question.category} | Source: {question.source}"
            )

        if st.button("Submit Quiz"):
            # Identify unanswered questions before attempting to calculate a score.
            unanswered = [
                index
                for index, answer in answers.items()
                if answer is None
            ]

            if unanswered:
                st.warning(
                    "Please answer every question before submitting."
                )

            else:
                # Submit each selected answer to the Quiz object's scoring logic.
                for index, answer in answers.items():
                    quiz.submit_answer(
                        quiz.questions[index],
                        answer
                    )

                percentage = quiz.calculate_percentage()

                # Display the participant's final quiz result.
                st.subheader("Your Result")
                st.write(
                    f"**Score:** {quiz.score}/{len(quiz.questions)}"
                )
                st.write(f"**Percentage:** {percentage:.1f}%")

                # A score of 70% or above is treated as a pass.
                if percentage >= 70:
                    st.success("Pass")
                else:
                    st.error("Not yet passed")

    else:
        st.error(
            "Please enter a valid name using letters and spaces only."
        )