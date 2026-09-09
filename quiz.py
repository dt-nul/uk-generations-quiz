class Question:
    """Represent a single multiple-choice quiz question."""

    def __init__(
        self,
        question_text: str,
        options: list[str],
        correct_answer: str,
        category: str,
        source: str
    ) -> None:
        """Initialise a question with its text, answers, category and source."""
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.category = category
        self.source = source

    def is_correct(self, answer: str) -> bool:
        """Return True when the supplied answer matches the correct answer."""
        return answer == self.correct_answer


class Quiz:
    """Represent a quiz containing multiple questions."""

    def __init__(self, questions: list[Question]) -> None:
        """Initialise a quiz with questions, a score and empty answer history."""
        self.questions = questions
        self.score = 0
        self.answers = []

    def submit_answer(self, question: Question, answer: str) -> None:
        """Submit an answer, record it and update the score when correct."""
        # Use the Question object's method to determine whether the answer is correct.
        is_correct = question.is_correct(answer)

        if is_correct:
            self.score += 1

        # Keep an answer history for later category analysis and answer review.
        self.answers.append(
            {
                "question": question,
                "answer": answer,
                "is_correct": is_correct
            }
        )

    def calculate_percentage(self) -> float:
        """Calculate and return the quiz score as a percentage."""
        # Prevent a division-by-zero error if a quiz contains no questions.
        if not self.questions:
            return 0.0

        # Convert the raw score into a percentage of the available marks.
        return (self.score / len(self.questions)) * 100

    def calculate_category_performance(self) -> dict[str, dict[str, float]]:
        """Calculate correct answers and percentages for each quiz category."""
        category_results = {}

        # Group submitted answers by the category assigned to each question.
        for answer_record in self.answers:
            question = answer_record["question"]
            category = question.category

            if category not in category_results:
                category_results[category] = {
                    "correct": 0,
                    "total": 0,
                    "percentage": 0.0
                }

            category_results[category]["total"] += 1

            if answer_record["is_correct"]:
                category_results[category]["correct"] += 1

        # Calculate the percentage score achieved within each category.
        for category in category_results:
            correct = category_results[category]["correct"]
            total = category_results[category]["total"]

            category_results[category]["percentage"] = (
                correct / total
            ) * 100

        return category_results