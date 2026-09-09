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

        # Convert each DataFrame row into a Question object.
        for _, row in data.iterrows():
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

    path = Path(file_path)

    # Check whether an existing results file contains the expected columns.
    file_is_valid = False

    if path.exists() and path.read_text(encoding="utf-8").strip():
        try:
            existing_results = pd.read_csv(file_path)

            required_columns = [
                "name",
                "date_time",
                "score",
                "total_questions",
                "percentage",
                "result"
            ]

            file_is_valid = all(
                column in existing_results.columns
                for column in required_columns
            )

        except (pd.errors.EmptyDataError, pd.errors.ParserError):
            file_is_valid = False

    if file_is_valid:
        # Append the new result to an existing valid results file.
        new_result.to_csv(
            file_path,
            mode="a",
            header=False,
            index=False
        )
    else:
        # Recreate the file with the correct headers if it is missing,
        # empty or malformed.
        new_result.to_csv(
            file_path,
            mode="w",
            header=True,
            index=False
        )


def load_results(file_path: str) -> pd.DataFrame:
    """Load valid saved quiz results into a pandas DataFrame."""
    try:
        # Read the stored results from persistent CSV storage.
        results = pd.read_csv(file_path)

        required_columns = [
            "name",
            "date_time",
            "score",
            "total_questions",
            "percentage",
            "result"
        ]

        # Only return results when all expected columns are present.
        if all(column in results.columns for column in required_columns):
            return results

        # Treat malformed result files as having no usable results.
        return pd.DataFrame()

    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError):
        # Return an empty DataFrame when usable results are unavailable.
        return pd.DataFrame()


if __name__ == "__main__":
    # Temporary development check for the question-loading functionality.
    questions = load_questions("data/questions.csv")

    print(f"Loaded {len(questions)} questions")

    if questions:
        print(questions[0].question_text)