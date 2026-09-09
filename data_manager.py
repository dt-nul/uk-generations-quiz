from datetime import datetime
from pathlib import Path

import pandas as pd

from quiz import Question


def load_questions(file_path: str) -> list[Question]:
    """Load quiz questions from a CSV file and return Question objects."""
    try:
        # Read the persistent question data into a pandas DataFrame.
        data = pd.read_csv(file_path)

        # Store the Question objects created from each row of the CSV file.
        questions = []

        for _, row in data.iterrows():
            # Convert each DataFrame row into a Question object.
            question = Question(
                question_text=row["question"],
                options=[
                    row["option_a"],
                    row["option_b"],
                    row["option_c"],
                    row["option_d"]
                ],
                correct_answer=row["correct_answer"],
                category=row["category"],
                source=row["source"]
            )

            questions.append(question)

        return questions

    # Return an empty list if the question file cannot be found.
    except FileNotFoundError:
        return []

    # Handle missing CSV columns or incorrectly formatted CSV data.
    except (KeyError, pd.errors.ParserError):
        return []


def save_result(
    name: str,
    score: int,
    total_questions: int,
    percentage: float,
    result: str,
    file_path: str
) -> None:
    """Save a completed quiz result to a CSV file."""

    # Create a record containing the details of the completed quiz.
    result_data = {
        "name": name,
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score": score,
        "total_questions": total_questions,
        "percentage": percentage,
        "result": result
    }

    # Convert the single result into a DataFrame for CSV storage.
    new_result = pd.DataFrame([result_data])

    # Check whether the results file already exists.
    # A file must exist and contain data before results can be appended without headers.
    file_exists = Path(file_path).exists() and Path(file_path).stat().st_size > 0

    # Append the result without overwriting previous quiz attempts.
    new_result.to_csv(
        file_path,
        mode="a",
        header=not file_exists,
        index=False
    )


if __name__ == "__main__":
    # Temporary development check for the question-loading functionality.
    questions = load_questions("data/questions.csv")

    print(f"Loaded {len(questions)} questions")

    if questions:
        print(questions[0].question_text)