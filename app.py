import pandas as pd
import streamlit as st

from data_manager import load_questions, load_results, save_result
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
            # Identify unanswered questions before calculating a score.
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
                # Submit each answer to the Quiz object's scoring logic.
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
                    result = "Pass"
                    st.success(result)
                else:
                    result = "Not yet passed"
                    st.error(result)

                # Save the completed attempt to persistent CSV storage.
                save_result(
                    name=name,
                    score=quiz.score,
                    total_questions=len(quiz.questions),
                    percentage=percentage,
                    result=result,
                    file_path="data/results.csv"
                )

                # Display performance for each quiz category.
                st.subheader("Performance by Category")

                category_performance = quiz.calculate_category_performance()

                for category, performance in category_performance.items():
                    st.write(
                        f"**{category}:** "
                        f"{performance['correct']}/{performance['total']} "
                        f"({performance['percentage']:.1f}%)"
                    )

                # Allow participants to review every answer after submission.
                st.subheader("Answer Review")

                for index, answer_record in enumerate(quiz.answers):
                    question = answer_record["question"]
                    user_answer = answer_record["answer"]
                    is_correct = answer_record["is_correct"]

                    if is_correct:
                        st.success(
                            f"Question {index + 1}: Correct"
                        )
                    else:
                        st.error(
                            f"Question {index + 1}: Incorrect"
                        )

                    st.write(f"**{question.question_text}**")
                    st.write(f"Your answer: **{user_answer}**")

                    # Reveal the correct answer when the participant was incorrect.
                    if not is_correct:
                        st.write(
                            f"Correct answer: **{question.correct_answer}**"
                        )

                    st.caption(
                        f"Category: {question.category} | "
                        f"Source: {question.source}"
                    )

                # Confirm that the completed attempt has been stored.
                st.info("Your result has been saved.")

    else:
        st.error(
            "Please enter a valid name using letters and spaces only."
        )


# Separate the quiz from the results dashboard.
st.divider()
st.header("Results Dashboard")

# Load all previous quiz attempts from persistent storage.
results = load_results("data/results.csv")

if results.empty:
    st.info("No quiz results have been recorded yet.")

else:
    # Calculate summary measures from the stored results.
    total_attempts = len(results)
    average_score = results["percentage"].mean()
    pass_rate = (results["result"] == "Pass").mean() * 100

    # Display headline performance measures in three columns.
    metric_1, metric_2, metric_3 = st.columns(3)

    metric_1.metric("Total Attempts", total_attempts)
    metric_2.metric("Average Score", f"{average_score:.1f}%")
    metric_3.metric("Pass Rate", f"{pass_rate:.1f}%")

    st.subheader("Results Over Time")

    # Prepare timestamped percentage scores for visualisation.
    chart_data = results.copy()
    chart_data["date_time"] = pd.to_datetime(chart_data["date_time"])
    chart_data = chart_data.set_index("date_time")

    st.line_chart(chart_data["percentage"])

    st.subheader("Previous Attempts")

    # Display stored results in a readable table.
    st.dataframe(
        results,
        width="stretch",
        hide_index=True
    )

    # Convert the DataFrame to CSV data for user download.
    csv_data = results.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Results CSV",
        data=csv_data,
        file_name="quiz_results.csv",
        mime="text/csv"
    )