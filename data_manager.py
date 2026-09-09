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


if __name__ == "__main__":
    # Temporary check used during development to verify CSV loading.
    questions = load_questions("data/questions.csv")

    print(f"Loaded {len(questions)} questions")

    if questions:
        print(questions[0].question_text)