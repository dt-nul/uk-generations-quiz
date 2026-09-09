from pathlib import Path

import pandas as pd

from quiz import Question


def load_questions(file_path: str) -> list[Question]:
    """Load quiz questions from a CSV file and return Question objects."""
    try:
        data = pd.read_csv(file_path)

        questions = []

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

    except FileNotFoundError:
        return []
    except (KeyError, pd.errors.ParserError):
        return []

if __name__ == "__main__":
    questions = load_questions("data/questions.csv")

    print(f"Loaded {len(questions)} questions")

    if questions:
        print(questions[0].question_text)